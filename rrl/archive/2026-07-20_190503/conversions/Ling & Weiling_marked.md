Received27January2025,accepted4March2025,dateofpublication11March2025,dateofcurrentversion21March2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3550339
Enhancing Segmentation: A Comparative Study of
Clustering Methods
LEWSOOKLING ,(SeniorMember,IEEE),ANDCLAIRETATANGWEILING
FacultyofInformationScienceandTechnology,MultimediaUniversity,Melaka75450,Malaysia
Correspondingauthor:LewSookLing(sllew@mmu.edu.my)
ThisworkwassupportedbyMultimediaUniversityandtheFRGSgrant(ProjectNumber:FRGS/1/2024/SSI09/MMU/02/2).
ABSTRACT With the increasing complexity of consumer preferences and behaviors, businesses face
challengestocapturethedynamicnatureofonlineconsumerbehavior,highlightingtheneedforadvanced
approaches.Thisstudyaimstoenhancecustomersegmentationine-marketingbyanalyzingandcomparing
various machine learning-based clustering methods, with a particular focus on unsupervised clustering
techniques for predicting Customer Lifetime Value (CLV). While prior research has utilized unsuper-
vised clustering for customer segmentation, this current study uniquely integrates K-Means++ with
other clustering techniques to enhance segmentation accuracy and gain deeper insights into consumer
behavior. This study adopts a structured, unsupervised clustering approach, enabling natural customer
groupingswithoutpredefinedlabels,whichisparticularlysuitableforcustomersegmentationinscenarios
with limited labeled data. Several clustering techniques are investigated, including K-Means, K-Medoids,
Agglomerative Clustering, DBSCAN, Fuzzy C-Means, K-Means++, Mini Batch K-Means, Mean Shift,
andGaussianMixtureModels(GMM).K-Means++demonstratedsuperiorperformanceinsegmentation
accuracy, outperforming other techniques under various conditions. Performance is evaluated using key
metrics such as the Silhouette Score and Davies-Bouldin Index. Utilizing Kaggle datasets, the analysis
followsacomprehensivepreprocessingprotocolcomprisingRFM(Recency,Frequency,Monetary)analysis,
outlier removal, and data normalization to ensure data integrity and facilitate systematic identification of
distinctconsumersegments.Thisresearchhighlightsthepotentialandsignificanceofmachinelearningin
refining customer segmentation processes within e-marketing, ultimately aiding businesses in optimizing
their marketing effectiveness and strategic planning. While focusing primarily on a limited selection of
clusteringmethods,thestudyunderscoresthenecessityforongoingexplorationintherealmofconsumer
segmentation.ByutilizingadvancedclusteringmethodssuchasK-Means++,businessescanenhancethe
marketing efforts to succeed in the competitive e-marketing landscape. Unlike previous studies that often
relied on traditional techniques, which may not fully capture the complexities of consumer behavior, this
studyintroducesacomprehensiveapproachthatleveragesmultipleclusteringmethodstogaindeeperinsights
into consumer behavior. Additionally, considering the study limitations, further research could explore
additionalclusteringtechniques,refinepredictivemodelingapproachesandinvestigatethegeneralizability
offindingstoindustriesbeyonde-marketing.
INDEXTERMS Customersegmentation,clustering,RFM,K-Means++,K-Medoids,CLVprediction.
I. INTRODUCTION Covid19 virus pandemic has made the Internet a necessity
Ourlivesaregrowingmoreandmoreconvenientasscience for everyday life. During that period of isolation, people
and technology improve and spread globally. The recent usedtheinternetforthingslikestudying,working,andshop-
ping [1]. As a result, people become increasingly reliant on
the Internet. Today, a lot of companies have switched to
The associate editor coordinating the review of this manuscript and
approvingitforpublicationwasClaudioZunino. e-marketing,andasmorepeopleshoponline,companiesface
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
47418 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
morecompetition.E-marketingisamethodofpurchasingor However, the issue is that the e-marketing sector lacks a
offering goods online. Customers can make purchases with structuredplan forconsumer segmentation.Traditionalseg-
a single click from anywhere in the world or at any time mentationtechniquesfrequentlyrelyonbasicstatisticaldata
without leaving home [2]. This increases the popularity of andfallshortofcapturingthechangingpatternsofconsumer
e-marketing around the world because of how convenient behaviorandpreferencesintheinternetspace.Additionally,
e-marketingis. the manual segmentation method takes a lot of time and
Due to the existence of many competitors in the market, hasdisadvantagesbecausethemanualmethodmissesslight
each company began to find ways to enhance performance, differences in the client base as well as cannot work when
including focusing on customer segmentation techniques. thecustomerrangeistoobig[4].Thishighlightstheneces-
Customersegmentationisamarketingtoolthatdividescus- sity for more automated and advanced methods to improve
tomers into groups. In a clear strategic business model and segmentationaccuracyandefficiency.
a specific market, the company groups customers accord- Consequently, e-marketing urgently needs an effective
ing to the customers’ attributes, behaviors, needs, prefer- methodofclientsegmentation.Byutilizingdatatechnology
ences, consumer psychology, or other characteristics, and and algorithms, businesses can identify different consumer
then uses different marketing strategies for each group of groups based on customers’ purchasing trends, browsing
customers. habits, preferences, and other valuable data [5]. Addressing
Thisstudyaimstoexplorethefieldofcustomersegmen- thisissuewillenhancetheunderstandingofclientsandenable
tation in the e-marketing sector with the clustering method businessestodevelopmarketingplansandproductsthatare
and business analytics techniques. By utilizing clustering specificallyaimedatboostingclientfulfilmentandloyalty.
techniques,theclusteringmethodcanclassifythecustomers The general objective of this research is to deter-
indifferentsegmentsefficientlybasedoncustomers’behav- minetheadvantagesofconsumersegmentationine-marketing.
iorsandpreferences.Utilizingbusinessanalyticstechniques The specific objectives of current study are: (1) To better
enablesthecompanytomakebettermarketingdecisionsthat understanding of consumer characteristics. (2) To examine
allows the companies to increase profits. This study will and compare the clustering methods. (3) To increase the
employ several clustering techniques, including K-Means, effectivenessofthebusiness’marketing.
K-Means++,MeanShift,GaussianMixtureModel(GMM) Thisstudyisdividedintofivesections:SectionIprovides
and K-Medoids, to effectively segment customers based on the introduction, Section II focuses on the literature review,
behaviorsandpreferences. SectionIIIoutlinesthemethodology,SectionIVpresentsthe
Thesignificanceofthisstudyliesinthepotentialtoprovide resultsanddiscussion,andSectionVconcludesthestudy.
e-marketing professionals with knowledge and insights that
canbereferencedtoimprovethecompany’smarketingeffi-
ciencyandimprovecustomersatisfaction.Byimplementing II. LITERATUREREVIEW
customer segmentation techniques, businesses can optimize A. ACUSTOMERSEGMENTATION
the marketing strategies and provide personalized experi- Accordingto[6],Smithwasthefirsttointroduce‘‘customer
ences to target customers. In addition, the study’s findings segmentation’’alsoknownas‘‘marketsubdivision’’concept.
couldcontributetothebroadere-marketingresearchfieldby Customersegmentationisamethodthatinvolvesclassifying
explainingtheeffectivenessandutilityofclusteringmethods customersintovariousgroupsbasedonsimilaritiesincharac-
forcustomersegmentation. teristicsorbehaviors.Thisapproachhelpsbusinessesgaina
Furthermore,throughthisstudy,e-marketingprofessionals deeperunderstandingofthecustomersandallowsbusinesses
cangainacomprehensiveunderstandingofthebenefits,chal- tocustomizestrategiesandofferstomeetthespecificneeds
lenges,andpracticalapplicationsofusingclusteringmethods and preferences of each customer segment [7]. By target-
for customer segmentation in the field of e-marketing. ing these segments with marketing efforts, businesses can
Byexaminingreal-worlddataandapplyingadvancedanalyt- increasecustomersatisfaction,improvemarketingefficiency,
ics, the study aims to generate actionable recommendations andcultivatestrongercustomerrelationships.
that businesses can implement to maximize the impact Ine-marketing,customersegmentationhasgainedimpor-
of the marketing efforts and foster long-term customer tance as businesses increasingly use digital data to target
relationships. customers more precisely. Over time, segmentation has
Businesses nowadays must deal with a wide range of evolved from simple groupings based on demographics like
clientdesiresandpreferencestodevelopefficientmarketing ageor incometoadvancedapproaches thatconsiderbehav-
strategies in the highly competitive e-marketing sector [3]. ioral patterns and analytics. For example, e-marketers often
Businesses would struggle to distinguish between various segmentcustomersbasedonagegroupsandspendinghabits,
clients and appropriate strategies withoutefficient customer suchasyoungadultswithhighpurchasefrequencyorsenior
segmentation. Failure to comprehend the audience will citizenswithapreferenceforpremiumproducts.Thesestrate-
preventcompaniesfromincreasingrevenue.So,understand- gies not only make marketing efforts more effective but
ing the customers’ desires and preferences is crucial for alsocreateastrongerconnectionwithcustomers,improving
businesses. satisfactionandloyalty.
VOLUME13,2025 47419

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
In addition to this, customer segmentation can enhance identify high-potential customers and customize marketing
customerexperienceandincreasetheprofitsofthebusiness. strategies [3]. However, this approach primarily focuses on
In this study, customer segmentation is employed to tailor customer behavior and may not fully capture other relevant
marketingstrategiesbasedondistinctconsumerprofiles,ulti- variables. Nevertheless, the integration of hierarchical and
matelyenhancingengagementanddrivingbusinesssuccess. K-Meansclusteringtechniquesshowspromiseinenhancing
marketingstrategies.
IntheotherstudybyDedietal.[11],researchersemployed
B. CLUSTERING
K-Meansclusteringtodeterminethebestclusterfortargeting
| Clustering | is a | technique | in  | machine learning | where | data |     |     |     |     |     |     |     |
| ---------- | ---- | --------- | --- | ---------------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
promotionalactivitiestowardsloyalcustomers.Researchers
| points are             | grouped | together |          | based on similarities, |       | allowing |             |      |               |               |                |     |             |
| ---------------------- | ------- | -------- | -------- | ---------------------- | ----- | -------- | ----------- | ---- | ------------- | ------------- | -------------- | --- | ----------- |
|                        |         |          |          |                        |       |          | acknowledge | that | this approach |               | only considers |     | some crite- |
| for the identification |         | of       | patterns | or relationships       | among | the      |             |      |               |               |                |     |             |
|                        |         |          |          |                        |       |          | ria, which  | may  | lead to       | inaccuracies. | Nonetheless,   |     | the value   |
datawithoutpriorknowledgeorguidance[8].Thistechnique
|            |          |     |            |                 |     |         | of K-Means | clustering    |     | lies in        | identifying | customers | that       |
| ---------- | -------- | --- | ---------- | --------------- | --- | ------- | ---------- | ------------- | --- | -------------- | ----------- | --------- | ---------- |
| helps find | patterns | or  | structures | in data without |     | knowing |            |               |     |                |             |           |            |
|            |          |     |            |                 |     |         | contribute | significantly |     | to a company’s |             | profits.  | Other than |
theoutcomesbeforehand.Clusteringalgorithmspartitionthe
|     |     |     |     |     |     |     | that, the | effectiveness | of  | K-Means | clustering |     | in identifying |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------- | ---------- | --- | -------------- |
dataintogroups,aimingtomaximizesimilaritywithingroups
profit-drivingcustomershasbeenhighlighted[12].However,
| and minimize         | similarity  |      | between    | groups.                | This method | has   |                 |             |                |              |           |     |                |
| -------------------- | ----------- | ---- | ---------- | ---------------------- | ----------- | ----- | --------------- | ----------- | -------------- | ------------ | --------- | --- | -------------- |
|                      |             |      |            |                        |             |       | the sensitivity |             | of the K-Means |              | algorithm | to  | initialization |
| various applications |             | such | as         | customer segmentation, |             | image |                 |             |                |              |           |     |                |
|                      |             |      |            |                        |             |       | is a known      | limitation. |                | Nonetheless, | companies |     | can utilize    |
| analysis,            | and anomaly |      | detection. | Clustering             | is useful   | for   |                 |             |                |              |           |     |                |
K-Meansclusteringtodevelopeffectivestrategiestoimprove
exploringdataandorganizingintomeaningfulgroups.Inthis
profits.
| study, clustering |     | is utilized | to  | segment customers |     | based on |         |            |     |          |       |           |            |
| ----------------- | --- | ----------- | --- | ----------------- | --- | -------- | ------- | ---------- | --- | -------- | ----- | --------- | ---------- |
|                   |     |             |     |                   |     |          | K-Means | clustering |     | has been | found | to assist | in identi- |
purchasingbehaviors,allowingformoretargetedmarketing
|     |     |     |     |     |     |     | fying targeted |     | customers | and | customers’ | buying | patterns, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | ---------- | ------ | --------- |
strategiesandenhancedcustomerengagement.
|     |     |     |     |     |     |     | enabling       | informed | decision-making |               | [13]. | Acknowledging |              |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --------------- | ------------- | ----- | ------------- | ------------ |
|     |     |     |     |     |     |     | the challenges |          | related to      | data quality, |       | outliers,     | and noise is |
C. K-MEANS,K-MEDOIDS,AGGLOMERATIVE,DBSCAN, important.Nevertheless,K-Meansclusteringoffersimproved
ANDFUZZYC-MEANSCLUSTERINGMETHODS
salesbenefits.Theresearchersfromstudy[14]haveempha-
Customer segmentation plays a vital role in e-marketing as sized the significance of K-Means clustering in identifying
segmentationenablescompaniestotargetspecificcustomer different customer groups and the unique characteristics,
segments and improve the marketing strategies accord- helpingcompaniestoresolvethechallengeofcustomergroup
| ingly [9]. | There    | are        | many | types of clustering |             | methods | classification. |         |             |     |             |      |            |
| ---------- | -------- | ---------- | ---- | ------------------- | ----------- | ------- | --------------- | ------- | ----------- | --- | ----------- | ---- | ---------- |
| such as    | K-Means, | K-Medoids, |      | Agglomerative       | clustering, |         |                 |         |             |     |             |      |            |
|            |          |            |      |                     |             |         | Using           | K-Means | clustering, |     | researchers | from | study [15] |
Density-BasedClusteringAlgorithms(DBSCAN)andFuzzy categorized e-marketing customers into two clusters based
C-Means. The clustering methods have been widely used on the RFM values. Out of the 102 customers, 63 belong
to effectively segment customers. This literature review to cluster 1 while 39 belong to cluster 2. This indicates
explores the findings and insights of numerous studies that that cluster 1 has a higher average RFM value compared to
use these clustering methods for customer segmentation in cluster2.Thestudy[15]notedthattheinitialstartingpoints
electronicmarketing. of the clusters as well as the number of clusters used can
K-Means is a commonly used clustering method known affect the results. Nonetheless, K-Means clustering enables
| for the effectiveness |     | in  | grouping | similar data | points. | This |           |     |          |       |           |           |         |
| --------------------- | --- | --- | -------- | ------------ | ------- | ---- | --------- | --- | -------- | ----- | --------- | --------- | ------- |
|                       |     |     |          |              |         |      | companies | to  | make the | right | decisions | regarding | market- |
techniqueinvolvesassigningdatapointstothenearestcluster ing strategies. The identification of denser clusters of users
center and iteratively adjusting the centers to minimize the through K-Means clustering has been linked to enhanced
differenceswithineachcluster.Bydoingso,K-Meansaims customerexperienceandincreasedbusinessprofits[16].The
to create clusters that contain data points with similar char- study’s results from [16] reveal that cluster 1 contains a
| acteristics, | allowing | for | meaningful | grouping | and | analysis |               |     |           |            |     |        |               |
| ------------ | -------- | --- | ---------- | -------- | --- | -------- | ------------- | --- | --------- | ---------- | --- | ------ | ------------- |
|              |          |     |            |          |     |          | larger number |     | of users, | indicating | a   | higher | concentration |
of the data. This method is commonly used for analyzing of users in that specific cluster. The limitation of the ini-
data and uncovering patterns in a straightforward manner. tial position of cluster centroids in K-Means clustering is
K-Meansclusteringhasbecomewidelyusedine-marketing acknowledged. Because K-Means is sensitive to the initial
forcustomersegmentation.InthestudybyMufarrohaetal. positionoftheclustercentroidandresultsinvariouscluster
| [10], researchers |     | found | that | the optimal number | of  | clusters |             |           |     |        |         |          |             |
| ----------------- | --- | ----- | ---- | ------------------ | --- | -------- | ----------- | --------- | --- | ------ | ------- | -------- | ----------- |
|                   |     |       |      |                    |     |          | assignments | depending |     | on the | initial | location | of the cen- |
using K-Means and K-Medoids clustering techniques was troids. However, clustering can help companies to enhance
4and6respectively,showingthatthedifferentmethodshave customer experience and increase business profits. In this
identifieddifferentpatternswithinthedata.However,noting current study, K-Means clustering is applied to effectively
that K-Means clustering is not suitable for datasets with segment e-marketing customers based on RFM values, pro-
| outliers is | important. |     | Nonetheless, | K-Means | clustering | has |                   |     |          |               |     |           |            |
| ----------- | ---------- | --- | ------------ | ------- | ---------- | --- | ----------------- | --- | -------- | ------------- | --- | --------- | ---------- |
|             |            |     |              |         |            |     | viding actionable |     | insights | for tailoring |     | marketing | strategies |
beenshowntobeefficientinmarketing. andimprovingoverallcustomerengagement.
Besides that, the combination of hierarchical clustering The results of study [17] indicate that the combined
withK-Meansclusteringhasbeensuggestedasamethodto weighted clustering method yields significantly improved
| 47420 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
clusteringoutcomesfore-marketingcustomerscomparedto clusteringalgorithmtoidentifycustomerbehaviorandmind-
traditional methods. These findings demonstrate the effec- set,enablingcompaniestoimproveproducts,technology,and
tiveness of utilizing K-Means clustering in improving the increasesales.
accuracy of customer segmentation. By employing this Besides K-Means, other clustering techniques have also
approach, businesses can develop more targeted marketing proven worth in customer analysis. The researchers from
strategies, optimize resource allocation, and foster stronger study[25]useFuzzyC-Meansclusteringtodeterminewhich
customer loyalty. The researchers from study [18] have customerclustersexhibitloyaltytoaparticularproduct.The
successfully demonstrated the value of K-Means clustering value of this approach lies in the ability to target marketing
in achieving these outcomes, emphasizing the potential for effortsmoreeffectively,savingtimeandresources.Similarly,
drivingbetterresultsine-marketinginitiatives.Determining the study by Gopal and Jacob [26] employs Agglomerative
suitablesegmentationscopesinK-Meansclusteringpresents clusteringtoenablefirmstogainadeeperunderstandingof
challenges that require careful consideration of numerous customerattitudesandimprovecustomersatisfaction.While
factors.Nonetheless,companiescanunderstandtheproduct this technique has limitations in terms of application accu-
typeandpaymentmethodthatispopularinthecompanyand racy and other performance metrics, still provides valuable
enables to retain customers by upgrading the quality of ser- insightsthatcanhelpeffectivelysolvebusinessproblems.
vices and products, improving communication, and gaining
a better understanding of customers. In this current study,
the application of clustering techniques allowed for a more D. K-MEANS++ANDMINIBATCHK-MEANS
detailedunderstandingofcustomerbehavior,facilitatingthe Customer analytics plays a vital role in understanding and
developmentofpersonalizedmarketingstrategies. meeting the needs of different customer segments, enabling
Anotherstudy[19]bytheseresearchersshowsthatusing businesses to formulate effective marketing strategies and
K-Meansclusteringcanclassifycustomersintothreedistinct increase profitability. Therefore, clustering algorithms are
clusters which are Silver, Gold, and Platinum. While this important to enterprises, such as K-Means++ and Mini
segmentationhasbeenshowntohelpimproveservicequality, Batch K-Means, which have been widely used in customer
companies can provide different services based on different analysis to group customers according to the similarity and
categories of clusters. The limitation of the study [19] is discovervaluableinsights.Manyresearchershavealsodone
that the analysis is based on data collected within a limited research on these algorithms to explore the effectiveness
two-year period only. The value gained from this clustering of these clustering techniques and the impact on customer
technique is the potential to increase sales and profits. The segmentation in various situations [5], [27], [28]. Overall,
study by Saini et al. [20] found that K-Means clustering these algorithms provide businesses with valuable tools to
enablesfirmstofocusonspecificcustomers,therebyenhanc- enhancethecustomersegmentationeffortsandimproveover-
ingcustomerexperienceduringtheproductpurchaseprocess. allmarketingeffectiveness.
However,alimitationofK-Meansclusteringisthatclusters TheK-Means++algorithmhasbeenstudiedincustomer
can have different shapes and sizes, which may reduce the analysis, and researchers [5] found that this method out-
effectiveness. However, the overall value of implementing performed other clustering methods. K-Means++ provides
K-Meansclusteringistomaximizefirmrevenue. greater separation between clusters and higher closeness
The researchers from study [21] highlighted the impor- within clusters, making an effective tool for customer seg-
tance of K-Means clustering in evaluating cluster models mentation. However, this approach should consider that
and determining customer distributions. The impact of this customervaluecanvarysignificantlywithinthesameindus-
approach is especially important for digital marketing com- tryduetofactorssuchasproducttype,customerpreferences,
panies and businesses looking to refine the strategies and and market conditions. Despite this limitation, using the
achieve better results. Furthermore, other researchers from K-Means++ algorithm can guide companies to implement
study[9]alsohighlightedK-Meansclusteringcanbeeasier differentiatedmarketingstrategiestoincreaseprofits.
to identify the customer characteristics, thereby improving AnotherclusteringtechniquecalledMiniBatchK-Means
customerrelationshipsandincreasingfirmrevenue. hasbeenappliedtocustomeranalysis,especiallyinthesector
However, the study by Bhatia et al. [22] pointed out of electronic marketing. The researchers from study [27]
the limitations of the K-Means clustering method, as the demonstrated that Mini Batch K-Means can effectively
method does not consistently produce practical and bene- dividee-marketingcustomersintomeaningfulsegmentsand
ficial results. Nonetheless, the result will show the various reveal the unique characteristics. However, both traditional
categories of clusters with distinct colors which can help K-MeansclusteringandMiniBatchK-Meansmayencounter
companies easily differentiate the customer category and challenges when dealing with large datasets, such as scal-
improvethemarketingplanbasedondifferentclusters.When ability and performance issues. Nevertheless, Mini Batch
successfullyapplied,K-Meansclusteringenablescompanies K-Means can help companies to improve the marketing
toformulatebettermarketingstrategiesandincreasesalesand strategy.
revenue of the company. Furthermore, these two studies by Furthermore, the researcher from study [28] compared
Aruletal. [23] and Gankidietal. [24] utilize the K-Means Mini Batch K-Means with other existing models, including
VOLUME13,2025 47421

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
K-Means, Agglomerative Clustering, and Mean-Shift, and variationswithincustomersegmentsmightbechallengingto
found that Mini Batch K-Means produced lesser errors in detect. Nevertheless, the study [32] emphasized the use of
clusteringcomparedtoexistingmodels.However,onelimi- K-Meansforsupportingcustomerrelationshipmanagement.
tationofthisapproachisthatdifficulttodeploypermanently, Theotherresearcher[8]comparedK-Means,Agglomerative
as customer habits and buying patterns change over time. Clustering, Spectral Clustering, Gaussian Mixture Model-
Nonetheless, implementing Mini Batch K-Means may lead based clustering, and DBSCAN Clustering methods. Based
tohigherearningsthroughimprovedmarketingefforts. on the analysis of the visualized results, the researchers
concluded that K-Means clustering was the most suitable
approach for the given dataset. The study from [8] further
E. COMPARISONBETWEENCLUSTERINGMETHODS highlighted the challenges associated with predefining the
Thissectionpresentsfindingsfromseveralstudies,highlight- numberofclustersandthesensitivityofresultstotheinitial-
ingtheresults,limitations,andvaluesofeachstudy.Various izationprocess.Indoingso,thecurrentstudyunderscoredthe
clusteringmethods,includingK-Means,DBSCAN,Agglom- significance of leveraging K-Means clustering in enhancing
erativeClustering,Mean-ShiftClustering,K-Medoids,Fuzzy marketing efficiency, facilitating budget allocation for mar-
C-Means, Spectral Clustering, Gaussian Mixture Model- ketingactivities,andidentifyingemergingmarketpotentials
based clustering, and Particle Swarm Clustering, have been andopportunities.
comparedacrossthesestudies[4],[8],[29],[30]todetermine Moreover,theauthor[30]comparedK-MeansClustering,
theeffectivenessincustomersegmentationfore-marketing. Fuzzy C-Means, and Particle Swarm Clustering algorithms.
Theresearcherfromthisstudy[7]comparedtheK-Means Theresultfoundthatallthreemethodsachievedsatisfactory
and DBSCAN algorithms and indicated that DBSCAN out- performance. The author emphasized that the application
performedK-Meansinidentifyingcustomerswhoexhibited of these methods resulted in an increase in the number
distinct spending behaviors, setting apart as a more effec- of clicks on websites. Lastly, researchers from study [33]
tiveapproach.However,thestudydidnotincludenecessary comparedK-Meansclustering,DBSCAN,andAffinityProp-
pre-processingstepsfordatapreparation.Despitethislimita- agation methods. The study observed that the sizes of the
tion,DBSCANwasconsideredusefulindetectingpotential DBSCANclustersshowedsignificantdifferences,whilethe
customers. The other researcher [29] compared K-Means Affinity Propagation clusters had more balanced sizes, like
Clustering, Agglomerative Clustering, Mean-Shift Cluster- the clusters generated by K-Means. The authors noted that
ing, and DBSCAN Clustering. The study concluded that wrong results could be produced, considering the possi-
DBSCAN and Mean-Shift performed better than K-Means bility of people learning and changing habits or spending
andAgglomerativeinidentifyingmeaningfulclusters.How- behavior. However, the study from [33] highlighted the
ever, K-Means and Agglomerative struggled to find mean- benefitoffocusingonmanagingeachidentifiedgroupeffec-
ingful data. The authors [29] emphasized that DBSCAN tively. In summary, the adaptability of clustering methods
andMean-Shiftcouldsignificantlyassistmarketingteamsin across different applications highlights the importance as
personalizingmarketcampaigns. essentialtoolsforeffectivecustomersegmentationandmar-
Besides that, the study by Maulina et al. [4] compared keting strategies. Table 1 presents the comparison between
K-Means,K-Medoids,andFuzzyC-Meansclusteringmeth- clusteringmethodsacrossdifferentstudies.
ods.TheresultdeterminedthatK-Meanswasthemosteffec-
tivealgorithmforclusteranalysis.However,theauthorsnoted
that the characteristics of company customers in business- III. METHODOLOGY
to-business (B2B) settings, which refer to transactions and A. DATASET
relationships between businesses rather than between busi- ThedatasetsthatareusedinthisreportarefromtheKaggle
nessesandconsumers,mayrequirefurtherimprovementfor website, which is a platform that allows users to find and
accurate segmentation. This highlights the value of using publishdatasets.Thedatasetsthatarechoseninthiscurrent
K-Meanstodevelopdifferentiatedstrategiesforspecificcus- studyareretailbusiness-related.Thefirstdatasetdetailsthe
tomergroups.Apartfromthis,theotherresearcher[31]also onlineretailtransactionsforaUK-basednon-storethattook
comparedK-Means,Agglomerative,andMean-Shiftcluster- place between 2010 and 2011 [34]. The second dataset is
ing methods, concluding that K-Means and Agglomerative about the comprehensive collection of sales, customer, and
performed better in clustering the data compared to Mean- product[35].BothdatasetsaredownloadedintoaCSVfile.
Shift. However, the authors acknowledged that K-Means The first dataset has 24,700 views and 4002 downloads,
clustering might not fully capture complex relationships consisting of 1,067,372 data and 8 columns attributes. The
betweenvariables,resultinginpoorgroupingoutcomes.This second dataset has 19,100 of views and 4,356 downloads,
underscores the importance of selecting the most suitable consistingof9,994dataand21columnsattributes.
clusteringalgorithmbasedonthedatasetcharacteristics. ThefirstdatasetdownloadedfromKaggleintheCSVfile
Furthermore, the researchers from study [32] compared consists of 1,067,372 data and 8 columns, which are the
K-Means and K-Medoids methods and concluded that following attributes: ‘‘Invoice’’, ‘‘Stock Code’’, ‘‘Descrip-
K-Means performed better. The authors noted that small tion’’, ‘‘Quantity’’, ‘‘Invoice Date’’, ‘‘Price’’, ‘‘Customer’’
47422 VOLUME13,2025

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE1. Comparisonbetweenclusteringmethods. TABLE3. Featuresindataset2withoutpre-processing.
TABLE2. Featuresindataset1withoutpre-processing.
|     |     |     |     | per unit using | Excel and                 | the formula     | (Sales/Quantity). | For     |
| --- | --- | --- | --- | -------------- | ------------------------- | --------------- | ----------------- | ------- |
|     |     |     |     | example,       | one record                | from the second | dataset shows     | an      |
|     |     |     |     | order with     | the ID ‘‘CA-2013-152156’’ |                 | where the         | product |
‘‘BushSomersetCollectionBookcase’’,ProductIDis‘‘FUR-
|     |     |     |     | BO-10001798’’ | was purchased. | The | order was placed | by a |
| --- | --- | --- | --- | ------------- | -------------- | --- | ---------------- | ---- |
customernamedClaireGutefromtheUnitedStates,withthe
orderdatebeing‘‘2013-09-11’’andtheshipdateon‘‘2013-
|     |     |     |     | 12-11’’.     | The order was | shipped via       | ‘‘Second Class’’   | with |
| --- | --- | --- | --- | ------------ | ------------- | ----------------- | ------------------ | ---- |
|     |     |     |     | a total sale | of $261.96    | for 2 units, each | priced at $130.98. |      |
and‘‘Country’’.Forexample,onerecordfromthefirstdataset
|            |                 |               |          | The order | had no discount, | resulting | in a profit of | $41.91. |
| ---------- | --------------- | ------------- | -------- | --------- | ---------------- | --------- | -------------- | ------- |
| shows that | an invoice with | ID ‘‘536365’’ | contains | the pur-  |                  |           |                |         |
chaseof‘‘WhiteHangingHeartT-LightHolder’’,stockcode Anadditional‘‘UnitPrice’’attributewasmanuallycalculated
|     |     |     |     | as $130.98 | by dividing | the sales by | the quantity. | Table 3 |
| --- | --- | --- | --- | ---------- | ----------- | ------------ | ------------- | ------- |
is‘‘85123A’’withaquantityof6,eachpricedat£2.55.The
customer is from the UK, and the invoice date is ‘‘2010- presentsthefeaturesindataset2withoutpreprocessing.
| 12-01’’. Table | 2 presents | the features | in dataset 1 | without              |     |     |     |     |
| -------------- | ---------- | ------------ | ------------ | -------------------- | --- | --- | --- | --- |
| preprocessing. |            |              |              | B. DATAPREPROCESSING |     |     |     |     |
The second dataset that downloaded consists of 9,994 This study uses Python to handle the missing values. After
data and 21 columns, which are the following attributes: loading the dataset into Jupiter Notebook. A comprehen-
‘‘RowID’’,‘‘OrderID’’,‘‘OrderDate’’,‘‘ShipDate’’,‘‘Ship sive check for missing values was conducted and the drop
Mode’’, ‘‘Customer ID’’, ‘‘Customer Name’’, ‘‘Segment’’, functionwasemployedtoeliminaterowscontaining‘‘Nan’’
‘‘Country’’, ‘‘City’’, ‘‘State’’, ‘‘Postal Code’’, ‘‘Region’’, values.Then,the‘‘InvoiceDate’’wasconvertedtodatetime
‘‘Product ID’’, ‘‘Category’’, ‘‘Sub-Category’’, ‘‘Product formatforconsistenttemporalanalysis.Additionally,filters
Name’’, ‘‘Sales’’, ‘‘Quantity’’, ‘‘Discount’’ and ‘‘Profit’’. were applied to exclude cancelled transactions and ensure
There is an additional attribute added manually, which is thenon-negativityof‘‘Quantity’’and‘‘Price’’[10].Figure1
‘‘Unit Price’’. This attribute calculates each product’s price shows the results of the missing values check for dataset 1.
| VOLUME13,2025 |     |     |     |     |     |     |     | 47423 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ----- |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
FIGURE1. Checkmissingvaluesfordataset1.
FIGURE4. RFMfordataset1.
FIGURE2. Removemissingvaluesfordataset1.
FIGURE5. RFMfordataset2.
recency,andmonetaryvaluebyconductingRFManalysison
thedataset.Secondly,RFMscoresshouldbeassignedtoeach
customerbasedonthebehavior,suchasrecentpurchasedate,
numberofpurchasesmadeandtotalspending.Thirdly,cus-
tomersshouldbeclusteredintodistinctgroupsusingtheRFM
scorestoidentifydifferentsegmentsbasedontheengagement
and value to the business. Finally, the characteristics and
behaviorsofeachRFMsegmentshouldbeanalyzedtogain
insight into customer preferences and identify opportunities
fortargetedmarketingstrategies.Figure4andFigure5below
showtheRFMresultsfordataset1anddataset2.
D. OUTLIERREMOVALANDNORMALIZATION
In this section, a robust function has been developed to
FIGURE3. Checkmissingvaluesfordataset2. identify and eliminate outliers based on the Interquartile
Range (IQR). The function is applied strategically to the
‘‘Recency’’,‘‘Frequency’’and‘‘Monetary’’columnswithin
Figure2presentstheresultsafterremovingthemissingval- the RFM dataset, ensuring the removal of data points that
ues from dataset 1, while Figure 3 shows the results of the may skew the analysis. Outliers are defined as data points
missingvaluescheckfordataset2. that fall outside the range of the first quartile (Q1) minus
1.5 times the IQR, or the third quartile (Q3) plus 1.5 times
C. RFMANALYSIS the IQR. The Interquartile Range (IQR) method provides
After the data pre-processing step, RFM analysis was con- a reliable mechanism for detecting outliers, enhancing the
ductedtogainvaluableinsightsintocustomerbehavior.The overallintegrityoftheRFMdataset[10].
Recency(R)scoreindicateshowrecentlyacustomermadea Additionally, the dataset undergoes min-max normaliza-
purchase,withmorerecentpurchasesreceivinghigherscores. tion,thisisacrucialstepinstandardizingthefeatureswhich
Frequency(F)measureshowoftenacustomerbuysfromthe are Recency, Frequency, and Monetary within a consistent
business, with more frequent buyers getting higher scores. rangeof[0,1].Thisnormalizationprocessisinstrumentalin
Monetary(M)reflectshowmuchmoneyacustomerspends, ensuring that each feature contributes proportionally to the
where higher spending results in a higher score. First, the subsequentanalyses,preventinganyundueinfluencedueto
consumer group should be divided according to frequency, differingscales.
47424 VOLUME13,2025

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
FIGURE6. Boxplotafteroutlierremovedfordataset1. FIGURE7. Boxplotafteroutlierremovedfordataset2.
| By systematically |          | removing | outliers  | and     | normalizing   | the |
| ----------------- | -------- | -------- | --------- | ------- | ------------- | --- |
| dataset, the      | analysis | is       | poised to | deliver | more accurate | and |
meaningfulresults,settingthestageforsubsequentstagesof
thestudy.Thismeticulousapproachenhancesthereliability
andinterpretabilityofRFMdata,providingasolidfoundation
fortheensuinganalysesandinsights.
| Figure           | 6 illustrates | a           | boxplot    | for Dataset | 1 after      | outlier |
| ---------------- | ------------- | ----------- | ---------- | ----------- | ------------ | ------- |
| removal. This    | visualization |             | provides   | a clear     | perspective  | on      |
| the distribution |               | of Recency, | Frequency, |             | and Monetary | val-    |
ues. The central box represents the main data points, with FIGURE8. Min-maxnormalizationfordataset1.
| a line indicating |     | the median. | Removing |     | the outliers | makes |
| ----------------- | --- | ----------- | -------- | --- | ------------ | ----- |
the plot more compact, simplifying the interpretation of the Figure8presentstheresultsofmin-maxnormalizationfor
data’srangeandspread.Overall,thisboxplotenhancesunder- Dataset1.ThisprocessadjuststheRecency,Frequency,and
standing of the dataset and prepares for the next analysis Monetaryvaluestoascalebetween0and1.Bystandardizing
steps. thedata,allmetricscanbecomparedmoreeasily.Thisstep
Figure 7 shows a similar boxplot for Dataset 2, also is vital for ensuring accurate analyses and interpretations,
reflecting the removal of outliers. This figure highlights the settingasolidfoundationforthenextphasesofthestudy.
distribution of Recency, Frequency, and Monetary metrics. Figure9displaystheresultsofmin-maxnormalizationfor
The elimination of outliers results in a more concentrated Dataset 2. Like Figure 8, this visualization shows how the
groupingofdatapoints,suggestingthatsomeextremevalues Recency,Frequency,andMonetaryvalueshavebeenadjusted
may have distorted the results. This clearer representation to fall within the 0 to 1 range. This normalization elimi-
boostsconfidenceinthedatasetandpavesthewayformore nates any differences in scale among the features, ensuring
accurateinsightsinfutureanalyses. each contributes equally to future analyses. This consistent
VOLUME13,2025 47425

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
FIGURE9. Min-maxnormalizationfordataset2.
approachimprovesthereliabilityoftheRFMdata,facilitating
thedrawingofmeaningfulconclusions.
| In conclusion, |              | the boxplots |               | provide | clearer       | distributions |     |     |     |     |     |
| -------------- | ------------ | ------------ | ------------- | ------- | ------------- | ------------- | --- | --- | --- | --- | --- |
| after outlier  | removal,     |              | while min-max |         | normalization | stan-         |     |     |     |     |     |
| dardizes       | the metrics. | These        | processes     |         | improve       | the accuracy  |     |     |     |     |     |
andreliabilityoftheupcominganalyses,establishingasolid
|     |     |     |     |     |     |     | FIGURE10. | ElbowmethodforK-Meansindataset1. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------------------------- | --- | --- | --- |
foundationformakinginformeddecisionsbasedontheRFM
model.
E. ELBOWMETHOD
| The optimal    | number | of            | clusters | (K) in | the clustering | algo-   |     |     |     |     |     |
| -------------- | ------ | ------------- | -------- | ------ | -------------- | ------- | --- | --- | --- | --- | --- |
| rithms K-Means |        | and K-Medoids |          | can    | be determined  | graphi- |     |     |     |     |     |
callyusingtheElbowMethod.Within-cluster-sum-of-square
| (WCSS)           | values            | are used  | in this    | method.    | These          | values are    |     |     |     |     |     |
| ---------------- | ----------------- | --------- | ---------- | ---------- | -------------- | ------------- | --- | --- | --- | --- | --- |
| the sum          | of squared        | distances |            | between    | data points    | and the       |     |     |     |     |     |
| cluster          | centers to        | which     | data       | have been  | assigned.      | The link      |     |     |     |     |     |
| between          | the corresponding |           | WCSS       | values     | on the         | y-axis and    |     |     |     |     |     |
| the number       | of clusters       |           | (K) on     | the x-axis | is represented | by            |     |     |     |     |     |
| the elbow        | graph.            | When      | additional | cluster    | addition       | does not      |     |     |     |     |     |
| significantly    | reduce            | WCSS,     | the        | graph      | displays       | an ‘‘elbow,’’ |     |     |     |     |     |
| or apparent      | bend,             | and       | this is    | the ideal  | K value        | [10]. This    |     |     |     |     |     |
| point represents |                   | a balance | between    |            | avoiding       | unnecessary   |     |     |     |     |     |
complexityandminimizingintra-clusterdistance.
Figure 10 illustrates the results of the Elbow Method FIGURE11. ElbowmethodforK-Meansindataset2.
appliedtoDataset1,displayingtherelationshipbetweenthe
numberofclusters(K)andinertia.Theplotincludesvalues
|     |     |     |     |     |     |     | Figure | 13 illustrates | the results | of the Elbow | Method |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | ----------- | ------------ | ------ |
forKrangingfrom2to10,withinertiaplottedonthey-axis.
|     |     |     |     |     |     |     | applied to | Dataset 2 | using K-Medoids, | depicting | the rela- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ---------------- | --------- | --------- |
Eachpointonthecurverepresentstheinertiacalculatedfora
specificnumberofclusters.Basedontheanalysis,avalueof tionshipbetweenthenumberofclusters(K)andinertia.The
K=4appearsoptimal,balancingsimplicityandaccuracyin analysis indicates that K = 7 is the optimal choice for this
segmentingthedataforK-MeansclusteringinDataset1. dataset, suggesting an effective balance for segmenting the
Figure11presentstheresultsoftheElbowMethodapplied datawiththeK-Medoidsalgorithm.
toDataset2,illustratingtherelationshipbetweenthenumber
ofclusters(K)andinertia.SimilartoDataset1,theanalysis F. SILHOUETTESCORE
revealsthatK=4isalsooptimalforthisdataset,indicatinga
|     |     |     |     |     |     |     | One measure | for evaluating | a clustering | technique’s | quality |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------------ | ----------- | ------- |
consistenttrendinclustersegmentationacrossbothdatasets. is the Silhouette Score. The degree of cluster separation is
Figure12displaystheresultsoftheElbowMethodapplied representedbyascalerangingfrom-1to1.AhigherSilhou-
to Dataset 1 using K-Medoids, illustrating the relationship etteScoreindicatesmoredefinedclusters.Eachdatapoint’s
betweenthenumberofclusters(K)andinertia.Theanalysis averagedistancefromotherpointsinthesamecluster(a)and
showsvaluesforKrangingfrom2to10,withinertiaplotted from the closest cluster to which the point does not belong
onthey-axis.Eachpointonthecurverepresentstheinertia (b)areconsideredwhencalculatingthescoreforthatpoint.
calculatedforthecorrespondingnumberofclusters.Basedon A cluster’s Silhouette Score is calculated as (b - a) / max
thisanalysis,avalueofK=6emergesasoptimal,suggesting (a,b).Theaverageoftheseratingsoveralldatapointsisthe
aneffectivebalanceforsegmentingthedatainDataset1using overall Silhouette Score. Higher Silhouette Scores indicate
| theK-Medoidsalgorithm. |     |     |     |     |     |     | betterclusterplacements. |     |     |               |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ------------- | --- |
| 47426                  |     |     |     |     |     |     |                          |     |     | VOLUME13,2025 |     |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
|     |     |     |     |     | TABLE4. | ResultsofsilhouettescoreandDaviesBouldinindexfor |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
k-means++.
| FIGURE12. | ElbowmethodforK-Medoidsindataset1. |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
behaviorandproductpreferences.Differentclusteringmeth-
|     |     |     |     |     | ods, including |     | K-Means++, |       | K-Medoids, |           | Gaussian | Mixture |
| --- | --- | --- | --- | --- | -------------- | --- | ---------- | ----- | ---------- | --------- | -------- | ------- |
|     |     |     |     |     | Model (GMM)    |     | and Mean   | Shift | are        | evaluated | using    | perfor- |
mancemetricsliketheSilhouetteScoreandDavies-Bouldin
Index.
|     |     |     |     |     | Based          | on           | the presented  |            | tables     | for            | each   | clustering |
| --- | --- | --- | --- | --- | -------------- | ------------ | -------------- | ---------- | ---------- | -------------- | ------ | ---------- |
|     |     |     |     |     | method,        | prioritizing |                | higher     | Silhouette | Scores         | and    | lower      |
|     |     |     |     |     | Davies-Bouldin |              | Index          | values     | indicates  | favorable      |        | choices.   |
|     |     |     |     |     | Consequently,  |              | the identified |            | optimal    | K              | values | are 4 for  |
|     |     |     |     |     | K-Means++,     |              | 7 for          | K-Medoids, |            | 8 for Gaussian |        | Mixture    |
Model(GMM)and5forMeanShift.ThesespecificKvalues
aredeemedsuitableforachievingwell-definedandcompact
|     |     |     |     |     | clusters, | aligning | with | the | objective | of effective |     | customer |
| --- | --- | --- | --- | --- | --------- | -------- | ---- | --- | --------- | ------------ | --- | -------- |
segmentationinthecontextofe-marketing.
ThetablegivesathoroughsummaryoftheDavies-Bouldin
K-Means++
|     |     |     |     |     | Index and | Silhouette |     | Score | for the |     |     | clustering |
| --- | --- | --- | --- | --- | --------- | ---------- | --- | ----- | ------- | --- | --- | ---------- |
algorithmforarangeofKvalues.TheDavies-BouldinIndex
|     |     |     |     |     | and Silhouette |     | Score | values | that correlate |     | to each | K value |
| --- | --- | --- | --- | --- | -------------- | --- | ----- | ------ | -------------- | --- | ------- | ------- |
FIGURE13. ElbowmethodforK-Medoidsindataset2. representthequalityofclusteringatvariouslevelsofcluster
granularity.
Table4presentstheperformancemetricsforK-Means++
G. DAVIES-BOULDININDEX
acrossdifferentclustervalues(K).TheSilhouetteScoreindi-
Another measure for evaluating the quality of clustering is cates how well-defined the clusters are, with higher values
theDavies-BouldinIndex.Thismethodevaluateshowclose
|     |     |     |     |     | suggesting | better | clustering. |     | The best | score | of 0.501 | occurs |
| --- | --- | --- | --- | --- | ---------- | ------ | ----------- | --- | -------- | ----- | -------- | ------ |
togetherandapartclustersare.AlowerDavies-BouldinIndex at K = 4, showing that this number of clusters provides
indicates better grouping. The average similarity between clear separation. The scores decrease with more clusters,
| each cluster | and the most | similar cluster | is found using | the |             |          |     |          |     |     |         |         |
| ------------ | ------------ | --------------- | -------------- | --- | ----------- | -------- | --- | -------- | --- | --- | ------- | ------- |
|              |              |                 |                |     | with values | dropping |     | to 0.401 | for | K = | 8,9 and | 10. The |
index.TheDavies-BouldinIndexistheaverageoftheseclus- Davies-BouldinIndexreflectsthequalityofclustering,with
| ter similarity | values across | all clusters. | Like the Silhouette |     |              |            |     |        |            |     |         |           |
| -------------- | ------------- | ------------- | ------------------- | --- | ------------ | ---------- | --- | ------ | ---------- | --- | ------- | --------- |
|                |               |               |                     |     | lower values | indicating |     | better | separation |     | between | clusters. |
Score,alowerDavies-BouldinIndexsignifiesbetter-defined The lowest value of 0.748 is also at K = 4, suggesting
clusterswithclearboundaries. effective clustering. As the k values increases, the index
rises,reaching0.896atK=10,indicatingpoorerseparation.
H. RESULTSOFSILHOUETTESCOREAND Insummary,K=4offersthebestclusteringperformanceand
| DAVIES-BOULDININDEXFOREACHCLUSTERING |     |     |     |     | balancing. |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
METHODINDATASET1 Inthefollowingsubsection,ananalysisoftheK-Medoids
Machinelearningisanessentialtoolfordataanalysis,where clustering method is presented. The exploration delves into
algorithms learn from data to identify patterns and make theSilhouetteScoreandDavies-BouldinIndexresultsacross
decisions. In this study, clustering algorithms are used to variousKvalues,offeringinsightsintotheclusteringefficacy
segment customer data based on features such as purchase andgranularityachievedthroughtheK-Medoidsalgorithm.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 47427 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE5. ResultsofsilhouettescoreandDaviesBouldinindexfor TABLE7. Resultsofsilhouettescoreanddaviesbouldinindexformean
| k-medoids. |     |     |     | shift.         |                |                        |            |               |
| ---------- | --- | --- | --- | -------------- | -------------- | ---------------------- | ---------- | ------------- |
|            |     |     |     | Table          | 7 displays the | results for the        | Mean Shift | clustering    |
|            |     |     |     | method         | at K = 5. A    | Silhouette Score       | of 0.403   | indicates     |
|            |     |     |     | decent cluster | separation,    | while a Davies-Bouldin |            | Index of      |
|            |     |     |     | 1.355 suggests | moderate       | compactness.           | These      | results imply |
thatK=5providesagoodbalancebetweenclusterseparation
TABLE6. ResultsofsilhouettescoreandDaviesBouldinindexfor andcompactness.
gaussianmixturemodel.
I. CLUSTERINGUSED
|     |     |     |     | Informed | by the literature | review | in Chapter | 2, various |
| --- | --- | --- | --- | -------- | ----------------- | ------ | ---------- | ---------- |
partition-basedanddensity-basedclusteringalgorithmshave
|     |     |     |     | been employed  | in previous | studies.       | For this study, | the cho-   |
| --- | --- | --- | --- | -------------- | ----------- | -------------- | --------------- | ---------- |
|     |     |     |     | sen clustering | approaches  | include        | K-Means,        | K-Means++, |
|     |     |     |     | K-Medoids,     | Gaussian    | Mixture Models | (GMM)           | and Mean   |
Shift.
|     |     |     |     | K-Means    | is a widely | used partition-based |                   | clustering |
| --- | --- | --- | --- | ---------- | ----------- | -------------------- | ----------------- | ---------- |
|     |     |     |     | algorithm, | is selected | for simplicity       | and effectiveness | [10].      |
Usingthisapproach,datapointsaredividedintoKclusters,
Table 5 summarizes the performance metrics for and each point is allocated to the cluster with the closest
K-MedoidsacrossdifferentvaluesofK.ThehighestSilhou- mean. The iterative refinement process continues until a
etteScoreof0.389occursatK=7,indicatingthebestcluster convergencecriterionismet.
separation. Although K = 8 has the lowest Davies-Bouldin K-Means++ is an improvement over the standard
Indexat0.908,K=7isselectedastheoptimalbalance,pro- K-Meansalgorithmintermsofinitializingclustercentroids.
vidingclearerclusteringwhileensuringsuitableseparation. Byemployingasmarterinitializationstrategy,K-Means++
In the subsequent subsection, the analysis shifts to the often converges faster and provides more robust clustering
| Gaussian Mixture | Model (GMM) | for clustering. | The evalu- | results[5]. |     |     |     |     |
| ---------------- | ----------- | --------------- | ---------- | ----------- | --- | --- | --- | --- |
ation encompasses the examination of Silhouette Score and Table 8 presents the K-Means++ clustering results for
Davies-BouldinIndexresultsacrossdifferentconfigurations Dataset 1, categorizing customers into four distinct groups
oftheGMM,sheddinglightontheeffectivenessincapturing based on their Recency, Frequency, and Monetary values.
underlyingpatternsandstructureswithinthedataset. Cluster 0 includes customers with low recency but high
Table 6 shows the performance metrics for the Gaussian frequency and monetary values, indicating that this group
MixtureModelatdifferentKvalues.ThehighestSilhouette tendstomakepurchasesfrequentlyanddemonstratesstrong
=
Score of 0.045 occurs at K 8, indicating the best cluster loyalty.Cluster1consistsofcustomerswhohavemaderecent
separation.TheDavies-BouldinIndexalsoreachesthelowest purchases but do not engage often, as shown by the high
point at K = 8 with a value of 2.639, suggesting clearer recencyandlowfrequencyandmonetaryscores.Cluster2is
clusters.Incomparison,bothK=9andK=10demonstrate made up of customers with low values across all metrics,
weakerseparation,makingK=8themostsuitablechoicefor suggesting that this group is inactive and might require tar-
thismodel. getedstrategiestoencourageareturn.Cluster3featureslow
Inthissubsection,attentionisdirectedtowardsMeanShift recency, high frequency, and high monetary values, repre-
clusteringanalysis.MeanShiftisdifferentbecausethisclus- sentinganothersegmentofloyalcustomerswhoconsistently
teringcaninherentlydetectthenumberofclustersbasedon makepurchases.
thedensityofdatapoints.MeanShiftoffersanon-parametric Table 9 displays the K-Means++ results for Dataset 2,
approachtoclustering,effectivelyidentifyingdenseregions which also includes four clusters. Cluster 0 stands out with
ofdatapointsinfeaturespace.Theevaluationentailsexamin- high recency, frequency, and monetary values, indicating
ingSilhouetteScoreandDavies-BouldinIndexresultsacross highly engaged customers who frequently purchase and
varyingbandwidthparameters,elucidatingMeanShift’sabil- spend well. Cluster 1 features customers with high recency
ity to adaptively determine cluster centers and capture data but low frequency and monetary values, suggesting that
distributioncharacteristics. whilethesecustomershaverecentlymadepurchases,butare
| 47428 |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------- |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE8. ResultsofK-Means++clusterfordataset1. TABLE10. ResultsofK-Medoidsclusterfordataset1.
TABLE9. ResultsofK-Means++clusterfordataset2.
Table 11 presents the K-Medoids clustering results for
Dataset 2, which identifies eight customer clusters. Clus-
ter 0 includes customers with low recency, low frequency,
and high monetary values, indicating a unique segment that
makes significant purchases infrequently. Cluster 1 features
customers characterized by low recency, high frequency,
not regular buyers. Cluster 2 highlights customers with low and high monetary values, representing a loyal group of
recencybuthighfrequencyandmonetaryvalues,showcasing customers who engage frequently. Cluster 2 also consists
aloyalgroupthatmakesconsistentpurchases.Lastly,Cluster of customers with low recency, high frequency, and high
3 exhibits low value across all metrics, indicating that this monetaryvalues,suggestingarobustsegmentofrepeatbuy-
group may need special marketing efforts to enhance the ers. Cluster 3 consists of customers with high recency, low
engagement. frequency, and low monetary values, indicating potential
K-Medoids is a partition-based clustering algorithm that, candidates for targeted marketing efforts to drive engage-
unlikeK-Means,utilizesdatapointsthemselvesasrepresen- ment. Cluster 4 includes customers with high recency, high
tatives of clusters [10]. This approach can be particularly frequency,andhighmonetaryvalues,highlightingactivecus-
useful in scenarios where the mean may not be a robust tomerswhoconsistentlymakesignificantpurchases.Cluster
representative. 5featurescustomerscharacterizedbylowrecency,highfre-
Table 10 shows the results of the K-Medoids clustering quency, and low monetary values, suggesting a group that
method applied to Dataset 1, revealing seven distinct cus- may require strategies to increase overall spending. Clus-
tomer clusters based on Recency, Frequency, and Monetary ter 6 includes customers with high recency, low frequency,
values.Cluster0consistsofcustomerswithlowrecency,high andlowmonetaryvalues,indicatinganeedforstrategiesto
frequency, and high monetary values, indicating a segment enhanceengagementandretention.Finally,Cluster7consists
ofloyalcustomerswhofrequentlyengageinsignificantpur- ofcustomerswithlowrecency,lowfrequency,andlowmon-
chases. Cluster 1 features customers characterized by high etaryvalues,suggestingasegmentatriskofbeinginactive.
recency,lowfrequency,andlowmonetaryvalues,represent- GaussianMixtureModels(GMM)isamodel-basedclus-
ing those who may have made recent purchases but lack tering technique assuming that data points come from a
ongoingengagement.Cluster2includescustomerswithhigh combination of different Gaussian distributions. GMM is
recency, high frequency, and high monetary values, sug- well-suitedforsituationswherethedatasetexhibitscomplex
gesting a group of active buyers that should be prioritized structures that cannot be adequately represented by simple
forretentionstrategies.Cluster3exhibitshighrecency,low geometricshapes[8].
frequency, and low monetary values, indicating a segment Table 12 presents the results of the Gaussian Mixture
thatmayneedtargetedmarketingeffortstoencouragerepeat Model clustering for Dataset 1, revealing eight distinct cus-
purchases. Cluster 4 also consists of customers with low tomersegmentsbasedonRecency,Frequency,andMonetary
recency,highfrequency,andhighmonetaryvalues,highlight- values. Cluster 0 includes customers with high recency,
ing another group of valuable customers. Cluster 5 features high frequency, and high monetary values, indicating active
customerscharacterizedbylowrecency,lowfrequency,and shoppers who frequently make significant purchases. Clus-
low monetary values, indicating a higher risk of churn. ter 1 shows customers with high recency, low frequency,
Finally,Cluster6includescustomerswithhighrecency,low and low monetary values, suggesting infrequent shoppers
frequency, and low monetary values, suggesting a need for who have recently made a purchase but may not contribute
strategiestoconvertrecentbuyersintoregularcustomers. muchtooverallrevenue.Cluster2ismadeupofcustomers
VOLUME13,2025 47429

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE11. ResultsofK-Medoidsclusterfordataset2. TABLE13. Resultsofgaussianmixturemodelclusterfordataset2.
TABLE14. Resultsofmeanshiftclusterfordataset1.
TABLE12. Resultsofgaussianmixturemodelclusterfordataset1.
MeanShiftisadensity-basedclusteringmethodthatiden-
tifiesclustersbylocatingmaximainthedatadensityfunction.
This approach is effective in situations where clusters have
irregularshapesanddensities[29].
Table14outlinestheMeanShiftclusteringforDataset1,
identifyingfivedistinctcustomergroupsbasedonRecency,
Frequency, and Monetary values. Cluster 0 represents cus-
tomers with low recency, low frequency, and low monetary
values,indicatingasegmentoflessengagedcustomerswho
rarely make purchases. Cluster 1 consists of highly active
and valuable shoppers, characterized by high recency, high
whoexhibitlowrecency,highfrequency,andlowmonetary frequency, and high monetary values. Cluster 2 captures
values, reflecting regular buyers who tend to make smaller customerswithlowrecency,highfrequency,andhighmon-
purchases. Clusters 3, 4 and 5 feature customers with low etary values, suggesting a loyal group that purchases often
recency, high frequency, and high monetary values, indicat- and significantly contributes to revenue. Cluster 3 reflects
ing multiple segments of loyal and valuable customers who similar characteristics to Cluster 1, with high recency, high
purchase often. Cluster 6 consists of customers with high frequency,andhighmonetaryvalues,forminganotherhighly
recency, low frequency, and low monetary values, pointing engagedgroup.Finally,Cluster4displayslowrecency,high
tothosewhorecentlyshoppedbutdonotengagefrequently. frequency,andhighmonetaryvalues,indicatingfrequentand
Finally,Cluster7representscustomerswithlowrecency,low valuableshoppers.
frequency,andlowmonetaryvalues,signalingagroupatrisk Table15illustratestheMeanShiftclusteringforDataset2,
ofdisengagement. identifying seven unique clusters. Cluster 0 represents cus-
Table13showstheresultsoftheGaussianMixtureModel tomers with low recency, low frequency, and low monetary
clustering for Dataset 2, identifying three distinct clusters. values, indicating a less engaged group. Cluster 1 shows
Cluster 0 contains customers with low recency, high fre- customerswithlowrecency,highfrequency,andhighmon-
quency,andlowmonetaryvalues,suggestingregularbuyers etary values, suggesting frequent and valuable shoppers.
who tend to spend less. Cluster 1 includes customers with Cluster 2 consists of customers with high recency, low fre-
highrecency,lowfrequency,andlowmonetaryvalues,indi- quency, and high monetary values, pointing to those who
catingshopperswhohaverecentlymadeapurchasebutdonot haverecentlymadeasignificantpurchasebutdonotengage
engage regularly. Cluster 2 highlights customers with high frequently. Cluster 3 includes customers with high recency,
recency,highfrequency,andhighmonetaryvalues,reflecting high frequency, and high monetary values, indicating active
an active and valuable segment of shoppers who frequently and high-spending customers. Cluster 4 with high recency,
makesignificantpurchases. low frequency, and high monetary values, forming another
47430 VOLUME13,2025

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE15. Resultsofmeanshiftclusterfordataset2. TABLE16. Resultsofrandomforestsandgradientboostingfor
K-Means++indataset1.
|     |     |     |     |     |     | proportionof | thevariationofthe |     |     | dependentvariablecanbe |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | ----------------- | --- | --- | ---------------------- | --- | --- |
expected.Consequently,greatermodel-datafitisindicatedby
segment of recent but infrequent shoppers. Cluster 5 repre- largerR-squaredvalues[36].
| sents customers |         | with low   | recency, | low frequency, | and high          |        |          |             |       |            |          |     |
| --------------- | ------- | ---------- | -------- | -------------- | ----------------- | ------ | -------- | ----------- | ----- | ---------- | -------- | --- |
|                 |         |            |          |                |                   | Moving | forward, | the current | study | implements | Gradient |     |
| monetary        | values, | suggesting | a        | small but      | valuable group of |        |          |             |       |            |          |     |
Boosting,apotentmachinelearningalgorithm,toenablethe
infrequent buyers. Cluster 6 features customers with low predictionofCustomerLifetimeValue(CLV).Thisensemble
recency,highfrequency,andhighmonetaryvalues,forming
learningmethodcombinesweaklearnersintoastrongpredic-
asegmentofloyalandhigh-valuecustomers.
|     |     |     |     |     |     | tive model | and | is effective | in capturing | complex | patterns | in  |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ------------ | ------------ | ------- | -------- | --- |
Theselectedclusteringmethodsareimplementedafterthe
customerbehavior.
| RFM analysis | and | a series | of  | preprocessing | steps, ensur- |                |     |        |          |         |          |        |
| ------------ | --- | -------- | --- | ------------- | ------------- | -------------- | --- | ------ | -------- | ------- | -------- | ------ |
|              |     |          |     |               |               | Next, applying |     | Random | Forests, | another | ensemble | learn- |
ing the data is well-prepared for accurate and meaningful ingalgorithm,knownforrobustnessandcapabilitytohandle
| segmentation. | The | determination |     | of the | optimal number of |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
diversedatapatterns,enhancespredictiveaccuracy.Random
| clusters is | conducted      |     | using the | elbow     | method, silhouette |             |         |          |     |             |       |        |
| ----------- | -------------- | --- | --------- | --------- | ------------------ | ----------- | ------- | -------- | --- | ----------- | ----- | ------ |
|             |                |     |           |           |                    | Forests can | provide | accurate | CLV | predictions | based | on the |
| score, and  | Davies-Bouldin |     | index,    | providing | a robust foun-     |             |         |          |     |             |       |        |
algorithm’sabilitytohandlehigh-dimensionaldatasets.
dationforsubsequentanalysis.Inconclusion,thoroughdata
Then,thiscurrentstudyenhancestheperformanceofboth
preparation, the use of effective clustering algorithms, and Gradient Boosting and Random Forests models by employ-
reliableevaluationmethodshavebeenessentialinproducing
|                   |     |           |         |     |                   | ing Hyperparameter      |     | Tuning, | which      | involves        | fine-tuning | the |
| ----------------- | --- | --------- | ------- | --- | ----------------- | ----------------------- | --- | ------- | ---------- | --------------- | ----------- | --- |
| accurate customer |     | segments, | leading | to  | improved customer |                         |     |         |            |                 |             |     |
|                   |     |           |         |     |                   | model’s hyperparameters |     |         | to enhance | the performance |             | and |
engagementandgreaterbusinesssuccess.
predictiveaccuracy.
|     |     |     |     |     |     | This subsection |     | focuses | on the | utilization | of  | Random |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------- | ------ | ----------- | --- | ------ |
J. CUSTOMERLIFETIMEVALUE(CLV)PREDICTION Forests and Gradient Boosting in conjunction with the
K-Means++
CustomerLifetimeValue(CLV)predictionisamethodused clustering method. The examination delves
to estimate the long-term value and profitability of a cus- intothepredictivecapabilitiesandmodelperformancewhen
appliedtotheclustersgeneratedbyK-Means++acrossthe
| tomer for | a business | [3]. | The prediction |     | involves analyzing |     |     |     |     |     |     |     |
| --------- | ---------- | ---- | -------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
historical customer data to study the potential revenue and specifieddatasets.
profitability in the future. This process includes collecting Table16presentstheresultsofRandomForestsandGradi-
entBoostingmodelsappliedtoDataset1usingK-Means++
| and pre-processing |     | customer |     | data, segmenting | customers |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | ---------------- | --------- | --- | --- | --- | --- | --- | --- | --- |
basedonbehaviorusingRFMsegmentsandclustermethod, clustering,bothbeforeandafterHyperparameterTuning.The
developing predictive models, validating the models, and performanceofthesemodelsismeasuredbyMeanAbsolute
applying the predictions to inform business strategies [10]. Error (MAE), Mean Squared Error (MSE), and R-squared
BusinessescanoptimizeoverallincomebyusingCLVpredic- values. Before tuning, Random Forests showed an MAE of
tiontoassistwithdecisionsregardingprice,marketing,client 2.3903, an MSE of 243.4673, and an R-squared value of
retention,andresourceallocation.CLVpredictionhelpsbusi- 0.9999, while Gradient Boosting had a significantly higher
nesses understand the value of each customer and optimize MAEof15.5569andanMSEof831.1362,withanR-squared
the strategies accordingly. The Mean Absolute Error calcu- of 0.9998. After Hyperparameter Tuning, Random Forests
lates the average absolute difference between the expected showed a slight improvement in MAE to 2.4558, while the
andactualvalues.Themodel’spredictionsaremoreaccurate R-squared value remained constant at 0.9999, while Gradi-
whentheMeanAbsoluteErrorvaluesarelower.Theaverage entBoostingshowedsubstantialimprovementwithanMAE
of the squares of the mistakes is measured by the Mean of 2.4212 and an MSE of 11.9509, maintaining a strong
SquaredError.Betterpredictionaccuracyfromthemodelis R-squaredof0.9999.
indicated bya lower mean squarederror number [3].Based Table 17 displays the results for Dataset 2, where similar
on the independent variable, the R-squared indicates what trends are observed. Before tuning, Random Forests had an
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 47431 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE17. Resultsofrandomforestsandgradientboostingfor TABLE19. Resultsofrandomforestsandgradientboostingfor
K-Means++indataset2. K-Medoidsindataset2.
TABLE18. Resultsofrandomforestsandgradientboostingfor Table 19 presents the results for Dataset 2. Before tun-
K-Medoidsindataset1.
ing, Random Forests had an MAE of 16.5303, an MSE
of 2349.6705, and an R-squared value of 0.9995. Gradient
BoostingshowedhighererrorswithanMAEof25.3454and
anMSE of2530.7474, resultingin anR-squared of0.9995.
After tuning, Random Forests improved with a reduced
MAE of 15.2979, an MSE of 1874.0583, and an R-squared
of 0.9996. Gradient Boosting achieved significant improve-
ments,loweringtheMAEto1.5649,theMSEto5.3597,and
reachinganR-squaredvalueof0.9999.
Within this subsection, the emphasis is on examining the
integration of Random Forests and Gradient Boosting with
theGaussianMixtureModel(GMM)clusteringmethod.The
evaluation seeks to elucidate the predictive capabilities and
MAEof15.5362,anMSEof2053.1072,andanR-squaredof model adaptability within the context of GMM-generated
0.9995,whileGradientBoostingproducedhighererrorswith clustersacrossthespecifieddatasets[37].
anMAEof25.3906andanMSEof2566.7146,resultingin Table 20 details the performance of the Random Forests
anR-squaredof0.9994.AfterHyperparameterTuning,Ran- andGradientBoostingmodelsonDataset1usingtheGaus-
domForestsdemonstratedimprovements,achievinganMAE sian Mixture Model, comparing results before and after
of 14.5254, an MSE of 1601.4375, and a slight enhance- HyperparameterTuning.Initially,RandomForestsachieved
ment in R-squared to 0.9996. Gradient Boosting showed a Mean Absolute Error (MAE) of 2.4879, a Mean Squared
remarkableimprovement,withanMAEof1.5592,anMSE Error(MSE)of316.0545,andanR-squaredvalueof0.9999.
of 5.0941, and an R-squared of 0.9999, indicating highly In contrast, Gradient Boosting reported a higher MAE of
accuratepredictionsaftertuning. 15.7106,anMSEof824.4635,andanR-squaredof0.9998.
Thissubsectionfocusesonevaluatingtheperformanceof AfterHyperparameterTuning,RandomForestsexperienced
Random Forests and Gradient Boosting in conjunction with a slight increase in MAE to 2.4965 and MSE to 322.9151,
theK-Medoidsclusteringmethod.Theanalysisaimstoassess whileR-squaredremainedstableat0.9999.GradientBoost-
the predictive accuracy and model robustness when applied ing demonstrated significant improvements, reducing the
to clusters generated by K-Medoids across the designated MAEto2.4581andloweringtheMSEto12.1213,withthe
datasets. R-squaredremainingat0.9999.
Table 18 showcases the results of Random Forests and Table 21 presents the outcomes for Dataset 2, where a
Gradient Boosting models on Dataset 1 using K-Medoids similar trend is observed. Before tuning, Random Forests
clustering,beforeandafterHyperparameterTuning.Initially, had an MAE of 16.1810, an MSE of 2107.2269, and an
Random Forests recorded an MAE of 2.3447, an MSE of R-squared of 0.9995, while Gradient Boosting produced a
196.6169, and an R-squared of 0.9999. Gradient Boosting, higherMAEof25.3100andanMSEof2569.4302,yielding
ontheotherhand,hadahigherMAEof15.4840,anMSEof anR-squaredof0.9994.AfterHyperparameterTuning,Ran-
800.6385,andanR-squaredof0.9998.Aftertuning,Random dom Forests improved the MAE to 15.9164, with an MSE
ForestsexperiencedaslightincreaseinbothMAEandMSE, of 2286.6050, while the R-squared remained unchanged at
reaching values of 2.4725 and 320.8613, while R-squared 0.9995.Incontrast,GradientBoostingdisplayedremarkable
remained stable at 0.9999. Gradient Boosting experienced improvement,reducingtheMAEto1.5741andloweringthe
substantial gains, reducing the MAE to 2.4222 and MSE to MSE to 5.5292, while achieving a higher R-squared value
11.9070,whilemaintainingastrongR-squaredof0.9999. of0.9999.
47432 VOLUME13,2025

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE20. Resultsofrandomforestsandgradientboostingforgaussian TABLE22. Resultsofrandomforestsandgradientboostingforgaussian
| mixturemodelindataset1. |     |     |     |     |     |     | mixturemodelindataset1. |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
TABLE23. Resultsofrandomforestsandgradientboostingforgaussian
TABLE21. Resultsofrandomforestsandgradientboostingforgaussian
mixturemodelindataset2.
mixturemodelindataset2.
|         |             |           |     |          |         |           | enhancements, | reducing | the MAE to 1.5776 | and MSE to |
| ------- | ----------- | --------- | --- | -------- | ------- | --------- | ------------- | -------- | ----------------- | ---------- |
| In this | subsection, | attention | is  | directed | towards | exploring |               |          |                   |            |
thecompatibilityofRandomForestsandGradientBoosting 5.4238,resultinginahigherR-squaredof0.9999.
Basedonthetablesabove,theGradientBoostingmethod
| with the | Mean Shift | clustering |     | method | [31]. The | analysis |     |     |     |     |
| -------- | ---------- | ---------- | --- | ------ | --------- | -------- | --- | --- | --- | --- |
significantlyoutperformsRandomForestsafterhyperparam-
| endeavors | to unveil | the | predictive | performance |     | and model |     |     |     |     |
| --------- | --------- | --- | ---------- | ----------- | --- | --------- | --- | --- | --- | --- |
etertuningforpredictingCustomerLifetimeValue.Gradient
| versatility | when | applied | to clusters | derived | through | Mean |          |                 |                    |             |
| ----------- | ---- | ------- | ----------- | ------- | ------- | ---- | -------- | --------------- | ------------------ | ----------- |
|             |      |         |             |         |         |      | Boosting | exhibits a much | lower Mean Squared | Error and a |
Shiftclusteringacrossthepredefineddatasets.
higherR-squaredvalueafterhyperparametertuning,making
| Table | 22 displays | the | performance | metrics |     | of Random |     |     |     |     |
| ----- | ----------- | --- | ----------- | ------- | --- | --------- | --- | --- | --- | --- |
thebetterchoiceforpredictingCustomerLifetimeValue.
| Forests | and Gradient | Boosting |     | models applied |            | to Dataset |     |     |     |     |
| ------- | ------------ | -------- | --- | -------------- | ---------- | ---------- | --- | --- | --- | --- |
| 1 using | the Gaussian | Mixture  |     | Model,         | presenting | results    |     |     |     |     |
K. CUSTOMERLIFETIMEVALUE(CLV)PREDICTIONUSING
bothbeforeandafterHyperparameterTuning.Initially,Ran-
BESTMODEL
| dom Forests | recorded | a   | Mean | Absolute | Error | (MAE) of |     |     |     |     |
| ----------- | -------- | --- | ---- | -------- | ----- | -------- | --- | --- | --- | --- |
2.4686, a Mean Squared Error (MSE) of 247.0451, and an After completing the hyperparameter tuning process, the
best-tunedGradientBoostingmodelisemployedforthefinal
| R-squared | value | of 0.9999. | In contrast, |     | Gradient | Boosting |     |     |     |     |
| --------- | ----- | ---------- | ------------ | --- | -------- | -------- | --- | --- | --- | --- |
hadahigherMAEof15.7106,withanMSEof824.4635and Customer Lifetime Value (CLV) prediction. Subsequently,
anR-squaredof0.9998.AfterHyperparameterTuning,Ran- ananalysisisconductedtocomparethepredictedCLVwith
theHistoricalCLV.IfthepredictedCLVislessthantheHis-
domForestsshowedaslightincreaseinMAEto2.4930and
MSEto333.5033,whiletheR-squaredremainedat0.9999. toricalCLV,theclusteriscategorizedas‘Low.’Conversely,
ifthepredictedCLVexceedstheHistoricalCLV,thecluster
| Meanwhile, | Gradient | Boosting | improved |     | the MAE | slightly |     |     |     |     |
| ---------- | -------- | -------- | -------- | --- | ------- | -------- | --- | --- | --- | --- |
to 2.4738 and significantly reduced the MSE to 12.4526, isdesignatedas‘High.’Thisstepensuresthatthepredictive
maintaininganR-squaredof0.9999. modelisnotonlyoptimizedforaccuracyandreliabilitybut
|               |             |              |          |          |          |           | also provides | actionable | insights into the | relative value of |
| ------------- | ----------- | ------------ | -------- | -------- | -------- | --------- | ------------- | ---------- | ----------------- | ----------------- |
| Table         | 23 presents | similar      | findings | for      | Dataset  | 2. Before |               |            |                   |                   |
| tuning,       | Random      | Forests      | had an   | MAE of   | 15.3888, | an MSE    | eachcluster.  |            |                   |                   |
| of 2125.6122, | and         | an R-squared |          | value of | 0.9995.  | Gradient  |               |            |                   |                   |
BoostingreportedahigherMAEof25.5233andanMSEof IV. RESULTSANDDISCUSSION
2608.9479,withanR-squaredof0.9994.Aftertuning,Ran- A. CONCEPTUALFRAMEWORK
dom Forests improved the MAE to 14.2419 and decreased The first step in the conceptual framework of the study
the MSE to 1814.0673, while the R-squared increased to is the preprocessing of data on selected datasets, such as
0.9996.Conversely,GradientBoostingachievedremarkable datasets 1 and 2. This crucial step ensures that the dataset
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     | 47433 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
| is cleaned | and | converted | to format |     | ready for | analysis. | After |     |     |     |     |     |
| ---------- | --- | --------- | --------- | --- | --------- | --------- | ----- | --- | --- | --- | --- | --- |
preprocessingthedata,performRFManalysistoinvestigate
| customer        | behavior      | patterns      |             | based      | on currency,   |                 | frequency,  |     |     |     |     |     |
| --------------- | ------------- | ------------- | ----------- | ---------- | -------------- | --------------- | ----------- | --- | --- | --- | --- | --- |
| and recency     | variables.    |               | Then,       | to improve |                | the consistency |             |     |     |     |     |     |
| and quality     | of            | the data,     | outlier     | removal,   |                | and             | normaliza-  |     |     |     |     |     |
| tion procedures |               | are utilized. |             | Next,      | the Elbow      | method          | was         |     |     |     |     |     |
| employed        | to determine  |               | the optimal |            | number         | of clusters     | for         |     |     |     |     |     |
| segmentation,   |               | and the       | clustering  | quality    |                | was then        | evalu-      |     |     |     |     |     |
| ated using      | the           | Silhouette    | Score       | and        | Davies-Bouldin |                 | Index.      |     |     |     |     |     |
| Figure 14       | presents      | the           | conceptual  | framework  |                | for             | this study. |     |     |     |     |     |
| The framework   |               | further       | explores    | various    |                | clustering      | meth-       |     |     |     |     |     |
| ods, including  |               | K-Means,      | K-Means++,  |            | K-Medoids,     |                 | GMM,        |     |     |     |     |     |
| and Mean        | Shift,        | aiming        | to          | identify   | better-defined |                 | clusters    |     |     |     |     |     |
| for enhanced    | segmentation. |               | From        | the        | results        | obtained        | from        |     |     |     |     |     |
thisstudy,better-definedclusterswereobservedforspecific
| clustering | methods:  | K-Means++     |                  |                  | with a       | Silhouette | score      |     |     |     |     |     |
| ---------- | --------- | ------------- | ---------------- | ---------------- | ------------ | ---------- | ---------- | --- | --- | --- | --- | --- |
| of 0.5011  | for       | four clusters | and              | a Davies-Bouldin |              |            | index of   |     |     |     |     |     |
| 0.7480;    | K-Medoids | with          | seven            | clusters         | showed       |            | a Silhou-  |     |     |     |     |     |
| ette score | of 0.3894 | and           | a Davies-Bouldin |                  |              | index      | of 0.9561; |     |     |     |     |     |
| GMM with   | eight     | clusters      | produced         |                  | a Silhouette |            | score of   |     |     |     |     |     |
0.0451andaDavies-Bouldinindexof2.6393;andMeanShift
| with five        | clusters | showed     | a          | Silhouette | score    | of 0.4026 | and   |     |     |     |     |     |
| ---------------- | -------- | ---------- | ---------- | ---------- | -------- | --------- | ----- | --- | --- | --- | --- | --- |
| a Davies-Bouldin |          | index      | of 1.3553. |            | Customer | lifetime  | value |     |     |     |     |     |
| (CLV) prediction |          | is carried | out        | using      | Random   | Forests   | and   |     |     |     |     |     |
Gradient Boosting techniques following cluster validation. FIGURE14. Conceptualframeworkforthisstudy.
| To maximize | model | performance, |     | hyperparameter |     |     | tuning is |     |     |     |     |     |
| ----------- | ----- | ------------ | --- | -------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
carriedoutusingtheRandomizedSearchCVmethod.After compactness and separation, displayed variability with dis-
hyperparameter optimization, the comparison output shows tinctKvalues.LowerDavies-BouldinIndexvaluesindicated
that the Gradient Boosting approach performs better than improvedclusteringsolutions[38].ImplementingtheElbow
Random Forests, especially in predicting CLV. To allow Method[10]andscrutinizingSilhouetteScoresandDavies-
robustcustomerbehavioranalyticsandpredictivemodelling, Bouldin Index, potential optimal K values were identified.
thisall-inclusiveframeworkcombinesdatapreparation,RFM A comprehensive summary table detailing K, Silhouette
analysis, outlier removal, normalization, cluster validation, Score,andDavies-BouldinIndexforeachattemptfacilitated
CLVprediction,andhyperparametertuning. a methodical comparison. The final selection of K involved
However, certain limitations exist within this framework. a nuanced assessment, integrating quantitative metrics with
Scalability could be an issue when applying these methods domainexpertise.Thismethodologicalapproachcontributed
to large datasets, as some clustering techniques, particu- to a thorough comprehension of cluster quality, leading to
larlyGMMandMeanShift,mayfacechallengesprocessing the selection of a suitable number of clusters for customer
| high-dimensional |     | or  | large-scale | data | efficiently. |     | The sen- | segmentation. |     |     |     |     |
| ---------------- | --- | --- | ----------- | ---- | ------------ | --- | -------- | ------------- | --- | --- | --- | --- |
sitivity to initial parameters also affects certain methods, Inevaluatingtheperformanceofdifferentclusteringmeth-
particularlyK-MeansandK-Means++,whereclusterquality
|     |     |     |     |     |     |     |     | ods on | the first dataset, | the following | observations | were |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------ | ------------- | ------------ | ---- |
can vary depending on initial cluster centroids. Lastly, the made. K-Means++ clustering method exhibits the highest
qualityofdatapreprocessingplaysacriticalroleintheoverall Silhouette Score and a low Davies-Bouldin Index, indicat-
performanceoftheframework.Inaccuratedatapreprocessing ing well-defined clusters and effective separation between
orpoorhandlingofnoiseandoutlierscanleadtosuboptimal them. K-Means++ with K = 4 emerges as a promising
clusteringresultsandpredictiveaccuracy. clusteringapproach.WhileK-Medoidsdemonstratesadecent
|     |     |     |     |     |     |     |     | Silhouette    | Score, the | higher Davies-Bouldin  |     | Index suggests |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ---------------------- | --- | -------------- |
|     |     |     |     |     |     |     |     | less distinct | clusters   | compared to K-Means++. |     | Neverthe-      |
B. COMPARISONOFCLUSTERINGMETHODS less,K-Medoidsstillperformswellinclustering.ForGMM,
Inassessingtheeffectivenessofclusteringmethods,twokey despite having a low Silhouette Score and a high Davies-
metricswereemployed:theSilhouetteScoreandtheDavies- BouldinIndex,providesinsightsintopotentialchallengesin
Bouldin Index. The Silhouette Score, illustrating cluster achieving clear cluster definitions with this method. Mean
cohesionandseparation,exhibitedadiscerniblerangeacross ShiftdemonstratesareasonableSilhouetteScoreandDavies-
differentKvalues.HigherSilhouetteScores,particularlyfor BouldinIndex,indicatingacceptableclusteringperformance.
specificKvalues,suggestedmorewell-definedclusters[38]. The dataset’s dimensionality and noise influenced clus-
Simultaneously,theDavies-BouldinIndex,assessingcluster tering performance. GMM struggled with high-dimensional
| 47434 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
data, while Mean Shift was affected by noise, which TABLE24. Resultsofcomparisonofclusteringmethods.
reduced effectiveness. K-Medoids performed reasonably
well, but clustering quality was less distinct compared
to K-Means++ due to the higher Davies-Bouldin Index.
In contrast, K-Means++ showed robustness despite these
challenges,maintaininghighperformanceandwell-separated
clusters. While K-Means++ provided the most consistent
results,methodslikeGMM,MeanShiftandK-Medoidsfaced
limitationsduetonoiseanddimensionality.
In comparison to the benchmark paper, which used
K-Means,K-Medoids,andtheElbowMethodforclustering
evaluation,thisstudyextendedtheanalysisbyincorporating
K-Means++, GMM and Mean Shift. While the bench- is consistency between K-Means and K-Means++ results,
mark relied on the Elbow Method for cluster selection, this slight variations occur in the output when the code is exe-
studyaddedtheSilhouetteScoreandDavies-BouldinIndex cuted multiple times for K-Means clustering. For getting
for a more comprehensive assessment of clustering qual- the best values using K-Means clustering, the trials need to
ity.ThesuperiorperformanceofK-Means++demonstrated repeat a few times [11]. Consequently, K-Means++, as an
by a higher Silhouette Score and a lower Davies-Bouldin enhancement of the original method, emerges as the pre-
Index, aligns with known advantages, such as better cluster ferred choice for stability and performance reliability [5].
separationandreducedsensitivitytoinitialization. In the case of K-Medoids clustering, Method 2 suggests
Table24presentstheresultsofthecomparisonofvarious optimal K values that outperform those recommended by
clustering methods used in the analysis. Each method is Method1,asevidencedbyhigherSilhouetteScoresandlower
evaluated based on the number of clusters (K values), the Davies-Bouldin Index values. The comprehensive compari-
Silhouettescore,andtheDavies-Bouldinindex.K-Means++ son underscores the robustness of Method 2, positioning a
achieves the highest Silhouette score of 0.5012 and the more effective approach for cluster analysis across diverse
lowest Davies-Bouldin index at 0.7481, indicating supe- datasets.
rior cluster separation. In contrast, the Gaussian Mixture The performance between K-Means and K-Means++
Model (GMM) performs poorly, with a Silhouette score of under both Method 1 and Method 2 across Dataset 1 and
0.0452 and a high Davies-Bouldin index of 2.6394, indi- Dataset 2. While the analysis meticulously examines the
cating weak clustering performance. K-Medoids and Mean clustering results, underscores that although both methods
Shift present intermediate results, with K-Medoids yielding exhibitcomparableperformanceincapturingmeaningfulpat-
a Silhouette score of 0.3894 and a Davies-Bouldin index of ternswithinthedatasets,K-Means++demonstratesgreater
0.9561,whileMeanShifthasaSilhouettescoreof0.4027and stability and consistency upon multiple executions of the
a Davies-Bouldin index of 1.3553. Based on this compre- code.ThissuggeststhatK-Means++offersbetterreliability
hensive analysis, K-Means++ with K = 4 stands out as inproducingconsistentclusteringoutcomes.
the most promising clustering method. This conclusion is Table 25 compares Method 1 (K-Means) and Method 2
drawnfromK-Means++’shighestSilhouetteScore(0.5012) (K-Means++)usingDataset1.Bothmethodsuse4clusters
whichindicateswell-definedandcohesiveclustersamongthe (K), as confirmed by the Elbow method. The Silhouette
comparedmethodsandalowDavies-BouldinIndex(0.7481) Score for both methods is about 0.5012, indicating that the
suggestingclearseparationbetweenclusterswhencompared clusters are reasonably well-defined. This score means that
to alternative approaches. The higher Silhouette Score of items within the same cluster are similar to each other. The
K-Means++impliesthattheclustersaremorecohesiveand Davies-Bouldin Index is also the same for both methods,
distinct,akeyfactorineffectivesegmentation.Additionally, around0.7481,suggestingthattheclustersarewellseparated.
thelowerDavies-BouldinIndexreinforcesthemethod’sabil- Overall, Table 23 shows that both methods perform equally
ity to create compact and well-separated clusters, providing wellintermsofclusteringforDataset1.
furtherevidenceofK-Means++’ssuperiorclusteringperfor- Table 26 compares Method 1 (K-Means) and Method 2
mance.Incomparisontoothermethods,thiscombinationof (K-Means++) using Dataset 2. Again, both methods use
highercohesionandbetterseparationmakesK-Means++the 4clusters,whichtheElbowmethodconfirms.ForDataset2,
mostreliableandefficientchoiceforcustomersegmentation. bothmethodshavethesameSilhouetteScoreofabout0.3394,
indicating that the clusters are less distinct compared to
C. COMPARISONBETWEENMETHOD1[10]AND Dataset1.Thismeanstheitemsinthesameclusterarenotas
METHOD2(PROPOSED)FORDATASET1ANDDATASET2 similar.TheDavies-BouldinIndexisalsosimilar,ataround
The comparative analysis between Method 1 [10] and 0.9948,showingthattheclustersarestillsomewhatseparated
Method2(Proposedmethod)acrossDataset1andDataset2, but not as well as in Dataset 1. In summary, both meth-
employing K-Means and K-Medoids clustering methods, ods yield consistent results for Dataset 2, but the clustering
elucidates distinct clustering characteristics. While there performanceisweakerthaninDataset1.
VOLUME13,2025 47435

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE25. Resultsofcomparisonofmethod1andmethod2indataset1. TABLE28. Resultsofcomparisonofmethod1andmethod2indataset2.
TABLE26. Resultsofcomparisonofmethod1andmethod2indataset2.
Table28presentstheresultsforDataset2.Again,Method2
shows better performance, achieving a Silhouette Score of
about0.242andaDavies-BouldinIndexof1.295.Thesemet-
ricssuggestthatMethod2ismoreeffectiveatformingclear
anddistinctclusters,eventhoughitincreasesthenumberof
clustersfrom7(Method1)to8(Method2).
D. COMPARISONOFCUSTOMERLIFETIMEVALUE(CLV)
PREDICTIONFORK-MEANS++ANDK-MEDOIDS
FOR2DATASETS
After a thorough comparison of the methods, method 2 has
demonstrated superior results, prompting the selection of
K-Means++ and K-Medoids for further exploration in the
TABLE27. Resultsofcomparisonofmethod1andmethod2indataset1.
Customer Lifetime Value (CLV) prediction phase. The sub-
sequent tables present the final CLV predictions for both
K-Means++ and K-Medoids applied to the two datasets.
These predictions will serve as valuable insights for under-
standing the long-term value and profitability of customers
intheidentifiedclusters.
This subsection focusses on the final CLV predic-
tions derived from the K-Means++ clustering method for
Dataset1andDataset2.Theanalysisevaluatestheaccuracy
andreliabilityoftheCLVpredictionsandexploresthepoten-
tialimpactonbusinessstrategiesandcustomermanagement
initiatives.
Thetables29,30,31and32displaythevaluesofRecency,
Frequency, Monetary, and CLV Prediction for each cluster
Next, the focus centers on the comparison of K-Medoids inboththeK-Means++andK-Medoidsmethodsusingtwo
clusteringunderMethod1andMethod2acrossDataset1and datasets. These results offer valuable insights into strategic
Dataset2.Notably,theanalysisrevealsthatMethod2outper- decision-making within the company. For instance, clusters
forms Method 1 for K-Medoids clustering, highlighting the with a High CLV Prediction present an opportunity for the
effectivenessingeneratingclustersthataccuratelyrepresent companytoenhancecustomerloyaltybyofferingfreegiftsto
theunderlyingstructureandcharacteristicsofthedata. customers within those clusters. On the other hand, clusters
Table 27 shows the results for Dataset 1, highlighting with a Low CLV Prediction suggest a potential for cus-
that Method 2 outperforms Method 1. Method 2 achieves tomerchurn,promptingthecompanytoimplementtargeted
a higher Silhouette Score of approximately 0.389 and a discount and promotion strategies to retain and re-engage
lower Davies-Bouldin Index of about 0.956. These num- customers. Additionally, the results provide the company
bers indicate that Method 2 creates clusters that are better withanopportunitytoobserveandanalyzecustomerbehav-
separated and more accurately reflect the data’s structure. ior,enablinginformedadjustmentstobusinessstrategiesand
WhileMethod1uses6clusters,Method2optsfor7clusters, marketingefforts.Thiscomprehensiveunderstandingofcus-
allowingforamoredetailedanalysis. tomer segments allows the company to tailor the approach,
47436 VOLUME13,2025

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE29. ResultsofK-Means++indataset1. TABLE31. ResultsofK-Medoidsindataset1.
TABLE30. ResultsofK-Means++indataset2.
and highlights the implications for strategic planning and
resourceallocation.
Table 31 summarizes the results of the K-Medoids clus-
teringmethodappliedtoDataset1.Atotalofsevendistinct
clusters are identified based on Recency, Frequency, Mone-
taryvalues,andCustomerLifetimeValue(CLV)prediction.
Cluster 0 features low recency, high frequency, and high
maximizingcustomersatisfactionandoverallbusinessprof- monetaryvalues,indicatingagroupofloyalandhigh-value
itability.Table29summarizestheresultsoftheK-Means++ customers.Cluster1showshighrecency,lowfrequency,and
clusteringmethodappliedtoDataset1.Fourdistinctclusters low monetary values, suggesting a segment of customers
are identified based on Recency, Frequency, Monetary, and who may not engage frequently but have recently made
CustomerLifetimeValue(CLV)prediction.Cluster0ischar- purchases. Cluster 2 exhibits high recency, high frequency,
acterizedbylowrecency,highfrequency,andhighmonetary andhighmonetaryvalues,pointingtoactivecustomerswho
values,indicatingasegmentofloyalandvaluablecustomers. require retention strategies. Cluster 3 consists of customers
In contrast, Cluster 1 displays high recency, low frequency, characterizedbyhighrecency,lowfrequency,andlowmon-
andlowmonetaryvalues,suggestingagroupoflessengaged etaryvalues,indicatinganeedfortargetedmarketingefforts.
customers.Cluster2consistsofcustomerswithlowrecency, Cluster 4 is the same as Cluster 0, with low recency, high
low frequency, and low monetary values, representing a frequency, and high monetary values, representing another
segment that may require re-engagement strategies. Finally, segmentofvaluablecustomers.Cluster5includescustomers
Cluster 3 mirrors the characteristics of Cluster 0, with low with low recency, low frequency, and low monetary values,
recency,highfrequency,andhighmonetaryvalues,indicating suggesting they may be at risk of churn. Finally, Cluster
anothergroupofloyalcustomers. 6 shows high recency, low frequency, and low monetary
Table30presentstheresultsoftheK-Means++clustering values, indicating a group that requires immediate attention
method applied to Dataset 2. This table also identifies four forengagement.
distinctclusters,butthecharacteristicsoftheseclustersdiffer Table32presentstheresultsoftheK-Medoidsclustering
fromthoseinDataset1.Cluster0featureshighrecency,high method applied to Dataset 2. Similar to Dataset 1, a total
frequency, and high monetary values, indicating customers of seven clusters are identified, each with distinct charac-
whohaverecentlypurchasedbutmaynotexhibitlong-term teristics. Cluster 0 features low recency, low frequency, and
loyalty.Cluster1showshighrecency,lowfrequency,andlow highmonetaryvalues,suggestingcustomerswhohavemade
monetaryvalues,suggestingagroupofcustomerswhomay significant purchases but may not engage frequently. Clus-
have made a recent purchase but do not engage regularly. ter 1 displays low recency and high frequency, indicating
Cluster 2 displays low recency, high frequency, and high valuable but less-engaged customers that may require dif-
monetaryvalues,representingloyalcustomers,whileCluster ferentiated marketing strategies. Cluster 2 also shows low
3 has low recency, low frequency, and low monetary val- recency and high frequency, reflecting another segment of
ues,indicatingcustomerswhomayneedtargetedmarketing loyal customers. Cluster 3 demonstrates high recency, low
effortstodrivere-engagement. frequency,andlowmonetaryvalues,representingcustomers
This discussion centers on the final CLV predictions who have recently interacted but contribute minimally to
obtainedfromtheK-MedoidsclusteringmethodforDataset revenue.Cluster4presentshighrecency,highfrequency,and
1andDataset2.Theanalysisexaminesthepredictiveperfor- high monetary values, indicating highly engaged customers
mance of K-Medoids in estimating customer lifetime value who may need continuous engagement to maintain loyalty.
VOLUME13,2025 47437

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
TABLE32. ResultsofK-Medoidsindataset2. includeleveragingK-Means++orK-Medoidsforimproved
segmentation,enablingmoreaccuratetargetingandtailored
|     |     |     |     |     |     |     |     | marketing | strategies.   | However, |          | acknowledging |       | the limita-   |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | -------- | -------- | ------------- | ----- | ------------- |
|     |     |     |     |     |     |     |     | tions of  | this research | is       | crucial. | The           | focus | was solely on |
K-Means,K-Means++,K-Medoids,GMM,andMeanShift
|     |     |     |     |     |     |     |     | clustering | methods, | limiting | the | exploration |     | of a broader |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | -------- | --- | ----------- | --- | ------------ |
rangeofclusteringtechniques.Futureresearchcouldaddress
theselimitationsbyincorporatingadditionalclusteringmeth-
ods,exploringscalabilityissues,andinvestigatingsensitivity
toinitialparametersordatapreprocessingquality.
|     |     |     |     |     |     |     |     | In comparison |             | to previous | studies,     |             | the superior | perfor-        |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | ----------- | ------------ | ----------- | ------------ | -------------- |
|     |     |     |     |     |     |     |     | mance of      | K-Means++   |             | consistently |             | demonstrates | strong         |
|     |     |     |     |     |     |     |     | clustering    | performance | and         | reduced      | sensitivity |              | to initializa- |
tion.Overall,thisresearchstudycontributestotheevolving
|     |     |     |     |     |     |     |     | field of online | marketing |     | by demonstrating |     | the | advantages |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | --- | ---------------- | --- | --- | ---------- |
ofmachinelearninginconsumersegmentationandoffering
|         |             |     |          |      |            |     |         | practical | insights | for marketers |     | to enhance |     | strategies and |
| ------- | ----------- | --- | -------- | ---- | ---------- | --- | ------- | --------- | -------- | ------------- | --- | ---------- | --- | -------------- |
| Cluster | 5 showcases | low | recency, | high | frequency, |     | and low |           |          |               |     |            |     |                |
drivebusinesssuccess.
monetaryvalues,whileCluster6displayshighrecency,low
frequency,andlowmonetaryvalues,suggestingbothgroups
ACKNOWLEDGMENT
requireurgentre-engagementefforts.
|     |     |     |     |     |     |     |     | The authors   | gratefully | acknowledge |     | the             | support | provided |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | ----------- | --- | --------------- | ------- | -------- |
|     |     |     |     |     |     |     |     | by Multimedia |            | University  | and | the Fundamental |         | Research |
V. CONCLUSION Grant Scheme (FRGS) (Project Number: FRGS/1/2024/
Insummary,thisstudyonconsumersegmentationstrategies SSI09/MMU/02/2). This support has been instrumental in
in online marketing concludes with the aim of uncovering facilitatingtheresearchandcontributingtothefindingspre-
the advantages of utilizing machine learning, particularly sentedinthisarticle.
unsupervisedclustering,toenhanceconsumerunderstanding
| andboostmarketingeffectiveness. |     |     |     |     |     |     |     | REFERENCES |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
The exploration begins by closely examining the chal- [1] Star.(Dec.11,2021).E-commerceContinuestoFlourishin2021|The
lengesfacedbybusinessesinunderstandingdiversecustomer Star.[Online].Available:https://www.thestar.com.my/business/business-
news/2021/12/11/e-commerce-continues-to-flourish-in-2021
preferencesinthefiercelycompetitiverealmofe-marketing. [2] N.Jalaliyoon,A.H.Taherdoost,K.Lumpur,andM.N.Jalaliyoon,‘‘Mar-
The absence of a systematic consumer segmentation plan keting vs E-marketing,’’ Int. J. Academic Res. Manag., vol. 3, no. 4,
pp.335–340,2014.
| underscores | the          | need | for an      | effective | strategy, | setting | the   |           |          |                |          |       |                 |               |
| ----------- | ------------ | ---- | ----------- | --------- | --------- | ------- | ----- | --------- | -------- | -------------- | -------- | ----- | --------------- | ------------- |
|             |              |      |             |           |           |         |       | [3] P. P. | Pramono, | I. Surjandari, | and E.   | Laoh, | ‘‘Estimating    | customer seg- |
| stage for   | the research |      | objectives. | The       | outlined  | study   | goals |           |          |                |          |       |                 |               |
|             |              |      |             |           |           |         |       | mentation | based    | on customer    | lifetime | value | using two-stage | clustering    |
provide a clear roadmap, emphasizing the development of method,’’inProc.16thInt.Conf.ServiceSyst.ServiceManage.(ICSSSM),
Shenzhen,China,Jul.2019,pp.1–5.
| a comprehensive     |     | understanding |     | of         | consumer | characteris- |         |                                                                |     |     |     |     |     |     |
| ------------------- | --- | ------------- | --- | ---------- | -------- | ------------ | ------- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                     |     |               |     |            |          |              |         | [4] N.R.Maulina,I.Surjandari,andA.M.M.Rus,‘‘Dataminingapproach |     |     |     |     |     |     |
| tics, a comparative |     | analysis      | of  | clustering | methods, |              | and the |                                                                |     |     |     |     |     |     |
forcustomersegmentationinB2Bsettingsusingcentroid-basedcluster-
enhancementofmarketingeffectiveness. ing,’’inProc.16thInt.Conf.ServiceSyst.ServiceManage.(ICSSSM),
Shenzhen,China,Jul.2019,pp.1–6.
| Section    | II Literature |          | Review     | delves | into    | various | research |             |        |                |     |            |          |              |
| ---------- | ------------- | -------- | ---------- | ------ | ------- | ------- | -------- | ----------- | ------ | -------------- | --- | ---------- | -------- | ------------ |
|            |               |          |            |        |         |         |          | [5] R. Zhao | and C. | Li, ‘‘Research | on  | e-commerce | customer | segmentation |
| materials, | laying        | a robust | foundation |        | through | an      | in-depth |             |        |                |     |            |          |              |
basedonRFACmodel,’’inProc.IEEEInt.Conf.Power,Intell.Comput.
studyofcustomersegmentationandvariousclusteringmeth- Syst.(ICPICS),Shenyang,China,Jul.2021,pp.439–444.
ods, focusing on the advantages and disadvantages relevant [6] W.R.Smith,‘‘Productdifferentiationandmarketsegmentationasalterna-
tivemarketingstrategies,’’J.Marketing,vol.21,no.1,pp.3–8,Jul.1956.
tothisstudy.SectionIIIdetailsthemethodology,emphasiz-
|     |     |     |     |     |     |     |     | [7] A.S.M.S.Hossain,‘‘Customersegmentationusingcentroidbasedand |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
ing critical steps like data preprocessing, RFM analysis and densitybasedclusteringalgorithms,’’inProc.3rdInt.Conf.Electr.Inf.
clustering,whichareessentialforaccuratecustomerlifetime Commun.Technol.(EICT),Khulna,Bangladesh,Dec.2017,pp.1–6.
|     |     |     |     |     |     |     |     | [8] S. R. | Regmi, | J. Meena, | U. Kanojia, | and | V. Kant, | ‘‘Customer mar- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --------- | ----------- | --- | -------- | --------------- |
value prediction. SectionIV delivers a critical evaluationof ket segmentation using machine learning algorithm,’’ in Proc. 6th Int.
clustering methods, comparing the effectiveness in segmen- Conf.TrendsElectron.Informat.(ICOEI),Tirunelveli,India,Apr.2022,
tation and examining the practical implications of customer pp.1348–1354.
|     |     |     |     |     |     |     |     | [9] M.R.K.IbrahimandR.Tyasnurita,‘‘LRFMmodelanalysisforcustomer |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
lifetimevaluepredictions.
segmentationusingK-meansclustering,’’inProc.Int.Conf.Electr.Inf.
The significance of this study lies in the ability to obtain Technol.(IEIT),Malang,Indonesia,Sep.2022,pp.383–391.
|                 |         |     |              |          |           |                |        | [10] F. A. | Mufarroha, | I. O. Suzanti, | B.        | D. Satoto, | M. Syarief, | Husni, and   |
| --------------- | ------- | --- | ------------ | -------- | --------- | -------------- | ------ | ---------- | ---------- | -------------- | --------- | ---------- | ----------- | ------------ |
| CLV predictions |         | for | each cluster | through  |           | the evaluation |        |            |            |                |           |            |             |              |
|                 |         |     |              |          |           |                |        | I. Yunita, | ‘‘K-means  | and            | K-medoids | clustering | methods     | for customer |
| results in      | Section | IV. | This         | empowers | companies |                | to use |            |            |                |           |            |             |              |
segmentationinonlineretaildatasets,’’inProc.IEEE8thInf.Technol.Int.
CLVpredictionsformoreinformedbusinessplanning.Addi-
Seminar(ITIS),Surabaya,Indonesia,Oct.2022,pp.223–228.
tionally, the comparison of clustering methods reveals that [11] Dedi,M.I.Dzulhaq,K.W.Sari,S.Ramdhan,R.Tullah,andSutarman,
‘‘CustomersegmentationbasedonRFMvalueusingK-meansalgorithm,’’
| K-Means++ | and | K-Medoids |     | are | more suitable |     | for the |     |     |     |     |     |     |     |
| --------- | --- | --------- | --- | --- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
inProc.4thInt.Conf.Informat.Comput.(ICIC),Semarang,Indonesia,
datasets in this study. Practical takeaways for businesses Oct.2019,pp.1–7.
| 47438 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

L.S.Ling,C.T.Weiling:EnhancingSegmentation:AComparativeStudyofClusteringMethods
[12] F.A.Bachtiar,‘‘Customersegmentationusingtwo-stepminingmethod [30] C.J.Santana,P.Aguiar,andC.J.A.Bastos-Filho,‘‘Customersegmen-
based on RFM model,’’ in Proc. Int. Conf. Sustain. Inf. Eng. Technol. tation in a travel agency dataset using clustering algorithms,’’ in Proc.
(SIET),Malang,Indonesia,Nov.2018,pp.10–15. IEEELatinAmer.Conf.Comput.Intell.(LA-CCI),Gudalajara,Mexico,
[13] R.Pradhan,‘‘Customersegmentationusingclusteringapproachbasedon Nov.2018,pp.1–6.
RFManalysis,’’inProc.5thInt.Conf.Inf.Syst.Comput.Netw.(ISCON), [31] T. Kansal, S. Bahuguna, V. Singh, and T. Choudhury, ‘‘Customer seg-
Mathura,India,Oct.2021,pp.1–5. mentationusingK-meansclustering,’’inProc.Int.Conf.Comput.Techn.,
[14] J.Bi,‘‘Researchforcustomersegmentationofmedicalinsurancebased Electron.Mech.Syst.(CTEMS),Belgaum,India,Dec.2018,pp.135–139.
onK-meansandC&Rtreealgorithms,’’inProc.6thInt.Conf.Semantics, [32] M.Aryuni,E.DidikMadyatmadja,andE.Miranda,‘‘Customersegmenta-
Knowl.Grids,Beijing,China,Nov.2010,pp.359–362. tioninXYZbankusingK-meansandK-medoidsclustering,’’inProc.Int.
[15] I. Maryani, D. Riana, R. D. Astuti, A. Ishaq, E. A. Pratama, and Conf.Inf.Manage.Technol.(ICIMTech),Jakarta,Indonesia,Sep.2018,
S.N.M.Jakarta,‘‘CustomersegmentationbasedonRFMmodelandclus- pp.412–416.
teringtechniqueswithK-meansalgorithm,’’inProc.3rdInt.Conf.Inform. [33] M.Pavithra,A.Prashar,andAbirami,‘‘Maximizingstrategyincustomer
Comput.(ICIC),Palembang,Indonesia,2018,pp.1–6. segmentationusingdifferentclusteringtechniques,’’inProc.IEEEInt.
[16] L.RajputandS.N.Singh,‘‘Customersegmentationofe-commercedata Conf.SignalProcess.,Informat.,Commun.EnergySyst.(SPICES),vol.1,
usingK-meansclusteringalgorithm,’’inProc.13thInt.Conf.CloudCom- Thiruvananthapuram,India,Mar.2022,pp.481–485.
put.,DataSci.Eng.(Confluence),Noida,India,Jan.2023,pp.658–664. [34] U.T.Pedersen.OnlineRetailDataset.Kaggle.Accessed:Nov.26,2023.
[17] P. Li, C. Wang, J. Wu, and R. Madlenák, ‘‘An e-commerce customer [Online].Available:https://www.kaggle.com/datasets/ulrikthygepedersen/
segmentationmethodbasedonRFMweightedK-means,’’inProc.Int. online-retail-dataset
Conf. Manage. Eng., Softw. Eng. Service Sci. (ICMSS), Wuhan, China, [35] I. Shrivastava. Superstore Sales. Kaggle. Accessed: Nov. 26, 2023.
Jan.2022,pp.61–68. [Online].Available:https://www.kaggle.com/datasets/ishanshrivastava28/
[18] R.Punhani,V.P.S.Arora,S.Sabitha,andV.K.Shukla,‘‘Applicationof superstore-sales/data
clusteringalgorithmforeffectivecustomersegmentationine-commerce,’’ [36] M. Heidari, S. Zad, and S. Rafatirad, ‘‘Ensemble of supervised and
in Proc. Int. Conf. Comput. Intell. Knowl. Economy (ICCIKE), Dubai, unsupervisedlearningmodelstopredictaprofitablebusinessdecision,’’
UnitedArabEmirates,Mar.2021,pp.149–154. in Proc. IEEE Int. IoT, Electron. Mechatronics Conf. (IEMTRONICS),
[19] A.SolichinandG.Wibowo,‘‘Customersegmentationbasedonrecency Toronto,ON,Canada,Apr.2021,pp.1–6.
frequencymonetary(RFM)andusereventtracking(UET)usingK-means [37] S. Kaur and Sarabjeet, ‘‘Customer segmentation using clustering
algorithm,’’inProc.IEEE8thInf.Technol.Int.Seminar(ITIS),Surabaya, algorithm,’’ in Proc. Int. Conf. Technological Advancements Innov.
Indonesia,Oct.2022,pp.257–262. (ICTAI),Tashkent,Uzbekistan,Nov.2021,pp.224–227.
[20] N.Saini,K.Sharma,P.K.Sarangi,G.Singh,andL.Rani,‘‘Customer [38] V.Mehta,R.Mehra,andS.S.Verma,‘‘Asurveyoncustomersegmentation
segmentation using K-means clustering,’’ in Proc. 10th Int. Conf. Rel., usingmachinelearningalgorithmstofindprospectiveclients,’’inProc.
Infocom Technol. Optim. (Trends Future Direction) (ICRITO), Noida, 9thInt.Conf.Rel.,InfocomTechnol.Optim.(TrendsFutureDirections)
India,Dec.2018,pp.1–5. (ICRITO),Noida,India,Sep.2021,pp.1–4.
[21] A.Agrawal,P.Kaur,andM.Singh,‘‘Customersegmentationmodelusing
K-meansclusteringone-commerce,’’inProc.Int.Conf.Sustain.Comput.
DataCommun.Syst.(ICSCDS),Erode,India,Mar.2023,pp.1–6.
[22] T.K.Bhatia,S.Gupta,andA.Sharma,‘‘Analysisofcustomersegmen-
tationmodelthroughK-meansclustering,’’inProc.10thInt.Conf.Rel.,
InfocomTechnol.Optim.(ICRITO),Noida,India,Oct.2022,pp.1–6.
[23] V.Arul,A.Kumar,andA.Agarwal,‘‘Segmentingmallcustomersdatato LEW SOOK LING (Senior Member, IEEE)
improvebusinessintohighertargetusingK-meansclustering,’’inProc. receivedthePh.D.degreefromMultimediaUni-
3rdInt.Conf.Adv.Comput.,Commun.ControlNetw.(ICAC3N),Greater versity (MMU), Malaysia, in 2013. Since 2001,
Noida,India,Dec.2021,pp.1602–1604. shehasbeenaLecturerwiththeFacultyofInfor-
[24] N. Gankidi, S. Gundu, M. V. Ahmed, T. Tanzeela, C. R. Prasad, and mationScienceandTechnology,MMU,whereshe
S.Yalabaka,‘‘Customersegmentationusingmachinelearning,’’inProc. iscurrentlyanAssociateProfessor.Herresearch
2ndInt.Conf.Intell.Technol.(CONIT),Hubli,India,2022,pp.1–6. interests include educational technology, busi-
[25] M. Husnah and R. A. Vinarti, ‘‘Customer segmentation analysis using ness analytics, image processing, and machine
LRFMbasedproductandbranddimensions,’’inProc.2ndInt.Conf.Innov. learning.
Technol.(INOCON),Bangalore,India,Mar.2023,pp.1–6.
[26] A.C.GopalandL.Jacob,‘‘Customerbehavioranalysisusingunsupervised
clusteringandprofiling:Amachinelearningapproach,’’inProc.2ndInt.
Conf.AdvanceComput.Innov.Technol.Eng.(ICACITE),GreaterNoida,
India,Apr.2022,pp.2075–2078.
[27] Y.-C. Chang, H. Yang, and S. Kong, ‘‘Based on mini batch K-means
CLAIRETA TANG WEILING receivedthebach-
clustering for customer segmentation in e-commerce,’’ in Proc. Int.
elor’sdegreeininformationtechnology,special-
Conf.CloudComput.,BigDataInternetThings(3CBIT),Wuhan,China,
Oct.2022,pp.60–66. izinginbusinessintelligenceandanalytics,from
[28] V.L.Narayana,S.Sirisha,G.Divya,N.L.S.Pooja,andSk.A.Nouf,‘‘Mall Multimedia University, where she is currently
customersegmentationusingmachinelearning,’’inProc.Int.Conf.Elec- pursuing the master’s degree in computing. Her
tron.Renew.Syst.(ICEARS),Tuticorin,India,Mar.2022,pp.1280–1288. researchinterestsincludecustomersegmentation,
[29] T. Mathesh, G. Sumathy, and A. Maheshwari, ‘‘A machine learning clusteringmethods,andpredictiveanalytics.
approach to segment the customers of online sales data for better and
efficientmarketingpurposes,’’inProc.Int.Conf.Artif.Intell.Knowl.Dis-
coveryConcurrentEng.(ICECONF),Chennai,India,Jan.2023,pp.1–9.
VOLUME13,2025 47439