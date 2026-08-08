TechScience Press
DOI:10.32604/cmc.2024.055192
ARTICLE
Data-Driven Decision-Making for Bank Target Marketing Using Supervised
Learning Classifiers on Imbalanced Big Data
FahimNasir1,AbdulghaniAliAhmed1,*,MehmetSabirKiraz1,IrynaYevseyeva1andMubarakSaif2
1SchoolofComputerScienceandInformatics,DeMontfortUniversity,Leicester,LE19BH,UK
2FacultyofComputerScienceandInformationTechnology,UniversitiTunHusseinOnnMalaysia,Johor,86400,Malaysia
*CorrespondingAuthor:AbdulghaniAliAhmed.Email:aa.ahmed@dmu.ac.uk
Received:20June2024 Accepted:26August2024 Published:15October2024
ABSTRACT
Integratingmachinelearninganddataminingiscrucialforprocessingbigdataandextractingvaluableinsights
to enhance decision-making. However, imbalanced target variables within big data present technical challenges
that hinder the performance of supervised learning classifiers on key evaluation metrics, limiting their overall
effectiveness. This study presents a comprehensive review of both common and recently developed Supervised
LearningClassifiers(SLCs)andevaluatestheirperformanceindata-drivendecision-making.Theevaluationuses
various metrics, with a particular focus on the Harmonic Mean Score (F-1 score) on an imbalanced real-world
banktargetmarketingdataset.Thefindingsindicatethatgrid-searchrandomforestandrandom-searchrandom
forestexcelinPrecisionandareaunderthecurve,whileExtremeGradientBoosting(XGBoost)outperformsother
traditional classifiers in terms of F-1 score. Employing oversampling methods to address the imbalanced data
showssignificantperformanceimprovementinXGBoost,deliveringsuperiorresultsacrossallmetrics,particularly
when using the SMOTE variant known as the BorderlineSMOTE2 technique. The study concludes several key
factors for effectively addressing the challenges of supervised learning with imbalanced datasets. These factors
include the importance of selecting appropriate datasets for training and testing, choosing the right classifiers,
employingeffectivetechniquesforprocessingandhandlingimbalanceddatasets,andidentifyingsuitablemetrics
forperformanceevaluation.Additionally,factorsalsoentailtheutilisationofeffectiveexploratorydataanalysisin
conjunctionwithvisualisationtechniquestoyieldinsightsconducivetodata-drivendecision-making.
KEYWORDS
Big data; machine learning; data mining; data visualization; label encoding; imbalanced dataset; sampling
techniques
Nomenclature
AdaBoost AdaptiveBoosting
AdaSynSMOTE AdaptiveSynthetic(variantofSMOTE)
BD BigData/bigdata
BorderlineSMOTE2 VariantofSMOTE
Class Classification
Copyright©2024TheAuthors.PublishedbyTechSciencePress.
This work is licensed under a Creative Commons Attribution 4.0 International License, which permits
unrestricteduse,distribution,andreproductioninanymedium,providedtheoriginalworkisproperlycited.

1704 CMC,2024,vol.81,no.1
DT DecisionTree
EDA ExploratoryDataAnalysis
ENN EditedNearestNeighbour
F-1 Performancemetric/HarmonicMean
GS-RF Grid-SearchRandomForest
LR LogisticRegression
ML MachineLeaning
NN NeuralNetwork
RF RandomForest
ROS RandomOver-Sampling
ROC-AUC ReceiverOperatingCharacteristic-AreaUnderCurve
RS-RF Random-SearchRandomForest
RUS RandomUnder-Sampling
SLC SupervisedLearningClassifiers
SLR SystematicLiteratureReview
SMOTE SyntheticMinorityOversamplingTechnique
SVM SupportVectorMachine
XGBoost ExtremeGradientBoosting
χ NotStated
1 Introduction
The integration of big data (BD) [1], machine learning (ML) [2], and data mining (DM) [3]
creates a dynamic trio that propels innovation, boosts efficiency, and enhances decision-making in
our data-driven world. Leveraging the power of these technologies has transformative effects with
extensive impacts across various industries and research fields. BD [1], characterized by its volume,
velocity, and variety, provides a vast reservoir for information extraction that has helped to set the
stage for transformative technologies. The ability to analyse and utilise complex datasets, which
grow exponentially in today’s interconnected world, offers organizations and industries unparalleled
opportunitiestogainvaluableinsights,makedata-drivendecisions,anduncoverpreviouslyunknown
patterns.Frompredictiveanalyticstoreal-timeprocessing,bigdataanalysishasbecomeanessential
tooldrivinginnovationandefficiencyacrossvarioussectors.Italsoaidsindatapreparation,business
understanding,datamodelling,andexploratoryanalysistoextracthiddeninsightsandidentifytrends
toderivemeaningfulinformation.Unearthingthewealthofknowledgewithindatanecessitatestheuse
of data mining technologies to uncover compelling, significant, and reliable patterns. Real-world big
datacanbecategorisedasstructured,unstructured,semi-structured,andimbalanced.Thesignificance
ofmajorityandminorityclassesinanimbalanceddatasetdependsontheresearchproblem.
DM[3]offersarangeofinnovativetechnologiesthatrevealpreviouslyhiddenpatterns,opening
new avenues for innovation and the formulation of novel theories. This has a transformative impact
on theoretical development across various fields. By extracting valuable insights from vast datasets,
data mining enhances understanding of customer behaviours, optimises business processes, and
supports strategic planning. As a crucial component of the data analytics toolkit, data mining
extracts actionable intelligence from the immense information generated in our digital world. With
the availability of big data, machine learning provides an essential enhanced processing platformfor
datamining,exploratoryanalysis,andbuildingmodelstoaddressrelatedproblems.

CMC,2024,vol.81,no.1 1705
Asasubfieldofartificialintelligence(AI),ML[4]enhancesbigdataanddataminingparadigmsby
providingthenecessaryalgorithmsandmodelsforpredictive,descriptive,andprescriptiveanalyticsof
vastandcomplexdatasets,includingimbalanceddata.Throughiterativelearningfromdata,machines
can improve their performance and make decisions without explicit programming. This adaptability
empowersMLapproachestomanagediversetasks,fromimagerecognitionandnaturallanguagepro-
cessing (NLP) to recommendation systems and autonomous vehicles. The interconnections between
big data, data mining, and ML represent a transformative force, unlocking the true potential of
data-driven technologies. Moreover, ML aids in outcome prediction and encompasses three types of
learning:‘supervised’,‘unsupervised’,and‘reinforcementlearning’[2].Classification[4]referstothe
processofpredictingthetargetclasscategoriesbyclassifyingtheinputvariables.Classificationliesin
supervised learning that requires labelled data to train an algorithm. Classification has applications
inseveraldomains,suchasmedicaldiagnosis,spamdetection,creditapproval,targetmarketing,and
salesforecasting.
Businessesgravitatetowardsdecision-makingbasedonhistoricaldata[5].Giventhatcorporations
emphasizing data-driven strategies regard their data as valuable corporate assets, they proactively
exploreavenuestoutiliseitforacompetitiveadvantageovertheircompetitors.Duringtheepochofbig
dataandML,majorcorporationsindifferentfields,suchasmanufacturing,informationtechnology,
marketing, logistics, finance, banking, and online sales sectors are increasingly turning toward
statistically informed analytics as the way forward. Their focus is on understanding and defining
consumer behaviour to increase returns on investment (ROI) [5]. Target marketing is fundamentally
important in the banking sector, as it acts as a strategic channel for personalized communication
with clients [6]. At the same time, target marketing and customer forecasting are important aspects
of business success and require a real dataset. Real-world data could have any form and may even
haveimbalancedtargetvariables[7,8].
Banksneeddatatounderstandcustomerforecasting,predicting,andbuyingbehaviourfortarget
marketing.Priortoextendingloansorothercreditproducts,bankmanagementwouldpredictthata
loanwouldeitherbepaidbackordefaulted.Anotherscenariowhethercustomermightbeinterested
in new product during a marketing campaign. In this case, there are two possible outcomes for
the target variable (“yes” or “no”). The bank can use ML algorithms and techniques to identify
the category by training on some historical data to predict or forecast the next outcome [9]. In
addition to that, there could be multiple scenarios for marketing campaigns that need prediction
based on skewed or imbalanced historic datasets of customers or previous marketing campaigns.
Furthermore, data analysis results and supervised learning algorithms enable executives to target
differentsegmentstopitchnewproductsorofferanextendedloan.However,therestrictedavailability
of real-world datasets and the presence of imbalanced target variables for classification accentuate
researchdeficiencies[10,11].
Classificationofimbalancedmarket-baseddatasetsreliesondeterminingthesignificanceofeither
the majority or the minority class. An imbalanced dataset exhibits a pronounced skewness in class
distribution, with two or more classes containing fewer instances compared to others. Within the
realm of automated machine learning, this disproportion presents hurdles during model training
and evaluation, possibly leading to biased predictions and reduced effectiveness on minority classes.
Although there is no standard definition to distinguish between imbalanced and balanced datasets,
a general rule of thumb states that if the class distribution is 50:50, it is a balanced dataset. If it is
51:49,itistermedanimbalanceddataset.Fortheimbalanceddataset,themajorityclassandminority
class, or sometimes minority classes, are categorised based on specific thresholds. Less than 25% is
categorised as moderate imbalance, less than 15% as highly imbalanced, equal to or less than 5%

1706 CMC,2024,vol.81,no.1
as extremely imbalanced, and less than 1% as imbalanced with rare instances of the minority class
[10,11]. Multiple domains could face problem statements with the involvement of an imbalanced
dataset.Theimportanceofmajorityandminorityclassesdependsontheresearchproblemstatement.
It is possible that the minority class could be treated as noise leading to biased training and testing
of the classification model towards the majority class resulting in more false positives with fewer
True Positives [11]. Sampling techniques offer a solution to treat imbalanced datasets in the pre-
processing of data. Sampling techniques are classified into three distinct approaches: over sampling,
undersampling,andhybridsampling[8].Undersamplingapproachreducesthenumberofmajority
class instances, whereas in over sampling, the number of minority class instances is increased due to
generatingnewinstances[8].Fig.1showshowsamplingtechniqueshandleimbalanceddatasets.
Figure1:Samplingofimbalanceddataset
The ability to analyse trends and patterns aids decision-makers in strategising and making
informed choices [1]. This research rigorously followed research methodologies, starting with the
selection of related research based on search string keywords. These include data analysis, data
pre-processing techniques, sampling techniques, imbalanced datasets, and classifier implementation.
The present era, characterised by technological advancements and pervasive presence of BD, DM,
and ML, has transformed the way in which information is generated, processed, and utilised. This
transformation offers remarkable advantages and helps researchers to achieve their goals and aims.
This study contributes in several ways. Firstly, it offers a critical review of related studies. Secondly,
it conducts data analysis and data transformation, including data cleaning, on an imbalanced bank
marketing dataset [12]. This step supports the necessary data pre-processing to understand and
preparethedatasetforimplementingtherecommendedclassifier.Additionally,thestudyincludesthe
implementationoftwofine-tunedhyper-parameterclassifiers.Lastly,itconductsacriticalevaluation
oftheresultsbasedonfiverelevantmetrics.Inourwork,theevaluationfocusesontheHarmonicMean
Score(F-1score)andAreaUndertheCurve(AUC),consideringtheimportanceoftheminorityclass.
We then assess the performance of the classifiers by comparing their results when implemented on
animbalanceddatasettotheresultsobtainedwhenimplementingthesameclassifierswithsampling
techniques[13].
Thispaperisstructuredasfollows.Section2presentsthemethodologyofourresearch.Therelated
works are reviewed in Section3. Then, we discuss our experiment setup with different conditions or
parameters for implementation and results in Section4. Section5 concludes the paper and provides
directionsforfuturework.

CMC,2024,vol.81,no.1 1707
2 Methodology
The methodology of this study consists of two main components: the first part focuses on the
selectedSystematicLiteratureReview(SLR),whilethesecondcomponentdescribesthemethodology
flowchart.TheliteraturereviewinthisstudyfollowstheKitchenhamandChartersSLRapproach[14],
asdepictedinFig.2.Thisapproachconsistsofthreephases:planning,conducting,andreporting.
Figure2:KitchenhamandChartersSLRapproach
In the planning phase, we define the review’s purpose, specify research questions, and develop a
reviewprotocol.Thepurposeofthereviewinthisstudyistoidentifytheoptimalmodelforclassifying
imbalanceddata.Toachievethis,asystematicliteraturereviewisconductedonexistingrelatedstudies,
and various recommended techniques and classification models are implemented for performance
evaluation. This helps in identifying the optimal model as a solution to the research problem. Our
researchquestionsareformulatedbasedondataanalysistechniques,datapre-processingtechniques,
classifiers, and performance evaluation metrics. The aim is to provide an ideal solution by utilising
the finest data analysis and data pre-processing techniques to identify the best-performing classifier
forimbalanceddatasets.Thereviewprotocolincludestheidentificationofpotentiallyrelevantstudies
from search results based on a search string. The conducting phase entails the selection of relevant
studies, conducting quality assessments of these studies, and extracting valuable data from them.
Screening is performed based on inclusion and exclusion criteria. We then thoroughly analyse the
remaining articles selected after detailed screening of the studies. In the third phase, the report is
prepared,andthekeyhighlightsofthereviewedSLRareevaluated.
In this paper, our methodology involves the classification of an imbalanced bank marketing
dataset with data analysis and pre-processing to facilitate data-driven decision-making. We utilised
a public dataset from the University of California, Irvine (UCI), an online data repository [12],
comprising sixteen input variables and one target variable. We performed exploratory data analysis
(EDA) and data visualisation to uncover the data patterns and insights. EDA involves examining
andunderstandingdatato extractinsights,identify patterns,andrelationshipsamongvariables,and
highlight key characteristics. For graphical EDA, we used visualisation techniques to create plots,
charts,andmapsusingPythonlibrariessuchasMatplotlib,Seaborn,andPlotlyinJupyterNotebook.
Once the nuances and key issues in the dataset are understood through EDA, data pre-processing
preparesthedatasettobeusedinthemodel.Datapre-processingincludesthecleaningofthedatasetby
removingtheoutliersandmissingvalues.Furthermore,weemployedBinningandLabelencodingto
categorisevariablestoengineerourutiliseddataset.Wethenperformedbinningonvariableslike‘age’,

1708 CMC,2024,vol.81,no.1
‘balance’,‘job’,‘day’,‘month’,‘duration’,‘campaign’,‘pdays’,and‘previous’inourdatasettogroupdata
intodiscreteintervals.Afterward,weappliedlabelencodingtoassignauniqueintegertoeachcategory
tofacilitatetheclassifier’simplementation.Datasamplingisthenemployedtohandletheimbalancein
thedistributionofclasses.Weperformedundersampling,andoversamplingtoaddresstheimbalance
inthetargetvariable.Finally,weappliedmultipleclassifierstothepre-processeddatasetandevaluated
theresultsonfivedifferentperformancemetricsofAccuracy,Precision,F-1score,AUC,andRecall.
Fig.3showstheflowchartoftheimplementationmethodology.
Figure3:Methodologyflowchart
3 RelatedLiterature
ThissectionpresentsthesearchstrategyaccordingtotheKitchenhamSLRapproachforrelated
literature, including papers filtering criteria, and a discussion on relevant research selected in sub-
sections:Reviewofpublishedliterature,includingSLRpapersandcasestudies.Werefinedoursearch
string by starting from examining the best classifiers, data analysis and processing, and literature
about imbalanced datasets used in recent academic research to address various gaps across different
domains.Wealsoexploredstudiesconcerningbigdataanalyticsinbusinessandindustries,concluding
withtheselectionofrelevantliteraturebasedonitsstrengthsandlimitationsthroughthelensofour
search string, inclusion, and exclusion criteria. An online search engine (Google Scholar) served as
ourprimarytoolforsourcingscholarlymaterial.Oursearch stringincluded keywordssuchas“data
analytics used in different fields,”AND “top classifiers with their strengths and limitations,”AND
“handling Imbalance datasets”AND “case studies of classifier’s implementation on datasets.”This
is further explained in Table1, which comprises keywords with Boolean “OR”and “AND”for our
searchstring.
The strategy for reviewing related literature encompassed digital libraries including; Institute of
Electrical and Electronics Engineers (IEEE), ScienceDirect, Scopus, Springer Link. These are well-
knownresearchsourceswithmulti-disciplinaryfieldsofresearch[11].About16,500researcharticles
werefoundin0.14sonGoogleScholarsearchengineinitiallywhilefollowingourbasicsearchstring.
Thefilteringprocesswascarriedoutontheexclusioncriteriawhichcomprised:Thestudyisnotwritten
inEnglish;Somekeywordsmatchbuttheoverallcontextwasnotsupportiveoftheresearchpurpose;
The full text of the study is not accessible; and the study is a short research article. Inclusion criteria
limit the year of publication to within the last decade (2014–2024). After excluding duplicates, we
identified over 1270 research publications in the online libraries that were pertinent to our research
contextandsearchstring.

CMC,2024,vol.81,no.1 1709
Table1: Searchstring
Keywords Searchstrategy
Dataanalysis (DataAnalyticsORDataAnalysisORBigDataAnalysisORbig-data
Analysis.)
AND
Dataprocessing (DataPre-processingORDataProcessingORFeatureEngineeringOR
FeatureAnalysisORDataModelling.)
AND
Machinelearning (MachineLearningORSupervisedLearningORClassificationORClassifiers.)
AND
Imbalanceddataset (ImbalanceDatasetORImbalanceDatadistributionORMajorityClassOR
MinorityClassORClassImbalance.)
Sampling AND
(ClassBalancingTechniquesORBalancingClassDistributionOROver
SamplingORUnderSamplingORhybridSamplingtechniques.)
AND
Evaluativemetrics (PerformanceEvaluativeMetricsORmetricsforsupervisedlearning.)
Our search results revealed numerous manuscripts, which partially answer or entirely support
our research purpose while offering novel insights about using established algorithms for classifying
different datasets in diverse fields, with feature engineering techniques and systematic summaries of
past related literature. Some research studies pertinent to our related literature were selected from
recent years after applying a systematic search strategy and filtering process. These studies fall into
three categories. Firstly, reviewed published studies having academic papers other than case studies
(Lit. Review). Secondly, case studies of the classifier’s implementation (Class. Case studies), and
thirdly,casestudiesoftheclassifier’simplementationonimbalanceddatasets(Class.Casestudieswith
Imbalanced data). We identified appropriate implementation methodologies and evaluation metrics
from related works. We carefully examined all selected studies to choose classifiers and sampling
techniquesforourstudy.Fig.4displaysachartdepictingtheselectedstudiesforreviewingthestate-
of-the-art.
3.1 ReviewofPublishedLiterature
We reviewed and summarized some academic studies, including systematic mapping studies,
published in different journals and conferences to understand the concepts of ‘Supervised learning’,
‘Imbalanced dataset’, ‘Classification’, and the strengths and limitations of different classifiers with
their basic principles and pseudocodes. Study [1] illustrated the impact of big data analytics in the
banking industry. The purpose of this case study was to help enterprises gain valuable knowledge
aboutbig data implementation in practice and improve their informationmanagement ability. Thus,
astheyaccumulateexperience,theycanreuseoradapttheproposedmethodtoachieveasustainable
competitiveadvantage.Referringtothetheoriesoftechnologicalframesofreferenceandtransaction
costtheory,thatstudyalsoproposedaframeworktoaddressanoverarchingresearchquestion:“How

1710 CMC,2024,vol.81,no.1
can big data analytics be effectively adopted to help the banking industry improve performance in
termsofcustomersegmentationandproductaffinityprediction?”.
Figure4:Showsthereviewedstudiesinthestateoftheart[1,4–6,8–11,13–27]
Anotherstudy[5]systematicallyreviewedstudiesonpredictiveanalyticsandDecisionTree(DT)in
businessresearch.Theauthorsselected24publishedstudiesonpredictiveanalyticsbasedoncustomer
relationship management, healthcare, fraud detection, underwriting, education, and manufacturing.
The paper also investigated the predictive tools used (methodology or algorithms) in the studies and
identifiedthekeytakeawaysoftheselectedstudiespublishedfrom2018to2021.Anotherpartofthe
reviewisbasedonDT,aknownclassifierinsupervisedlearning.Inthispartofthereview,theauthors
selected20studiesandexaminedtheirdomainsofstudy,thealgorithmsormethodologiestheyused,
andthekeyoutcomesofthestudiespublishedfrom2019to2021.
Inthestudy[11],theauthorsprovidedanSLRusingasystematicmappingmethodologyaccording
to guidelines proposed by Peterson et al in 2015. Through the systematic mapping methodology, the
authorsassessed9927researchpapersfrom7digitallibrariesrelatingtosamplingtechniquesforML
andselected35suchpaperspublishedfrom2013to2020relatedtodomainslikehealth,finance,and
engineering after the filtering process. The study concluded that oversampling techniques used with
classicMLmodelsarethemostcommon,butsamplingsolutionswithNeuralNetworks(NN)orwith
ensembleMLmodelsarethebestperformers.Theauthorsindicatedthathybridsamplingtechniques
havethepotentialtoperformbetter.TheyalsotermedSimulation-basedsyntheticoversamplingasa
futurepre-processingsolution.
Study [14] performed SLR according to Kitchenham and charter’s guidelines and provided
insights into AI techniques used in financial trading after analysing the selected 143 research papers

CMC,2024,vol.81,no.1 1711
published between 2015 and 2023. The authors tried to answer four research questions while high-
lightingandidentifyingeightfinancialmarkets,commonlystudiedwithafocusonstockmarkets,the
FOREX market, and cryptocurrency trading. Machine learning, deep learning, and reinforcement
learning were utilised as AI techniques in the reviewed literature, with a higher number of research
papers focused on deep learning, and only 10% of research papers being related to classification.
During and after the pandemic of Corona Virus (COVID-19) stock market crash, many research
workswerepublishedonthetopicoffintechwithafocusonfundamentaltradinganalysis,technical
analysis, and trading strategies. The study listed forty AI techniques (traditional and hybrid) with
multipleevaluationmetricsfollowingasystematicmappingreview.Theauthorsrecommendedfuture
research aiming to develop an automated financial trading system that predicts the market after
technical and fundamental analysis. To achieve this aim, researchers should focus on developing
modelswithmaximumriskcontrolbehaviourandbuildingadditionalcrisisdetectorsforriskanalysis.
Furthermore,thisstudysuggestsresearchpathwayofdevelopingapproachfordeterminationofbest
automatedmodelandfintechsystem.
In a comparative study on business intelligence (BI) and AI conducted through the lens of big
data analytics [15], the authors reviewed the literature and highlighted the scope, importance, usage,
software and hardware resources, and the role of BI, AI, and ML in data analytics. Study [16] also
systematicallyreviewedtheliteratureonsupervisedlearningtechniquesandalgorithms.Theresearch
questionsformulatedforthisreviewaimedtofigureoutthetypesofapproachesoralgorithmsused,
which performance evaluation metrics were employed, and the strengths and limitations of each
study on supervised learning. The authors selected digital libraries like IEEE, the Association for
ComputingMachinery(ACM),andScienceDirectwhensearchingforarticlespublishedfromJanuary
2011toAugust2021.Theyendedupwith57studiesafterimplementinginclusiveandexclusivesearch
strategies for review. This study found classifiers such as Logistic Regression (LR), Support Vector
Machine(SVM),DT,AdaptiveBoosting(AdaBoost),ExtremeGradientBoosting(XGBoost),Naïve
Bayes(NB),K-nearestneighbours(KNN),andRandomForest(RF),arethewidelyusedsupervised
learning algorithms. The authors also identified Accuracy, Precision, Recall, F-1 score, AUC, and
Mean Absolute Error (MAE) as widely used evaluation metrics. Furthermore, about 60% of the
selectedstudieswererelatedtothemedicalfield.
Study[17]presentedanextensivereviewofpublishedliteraturebetween2019and2021onhybrid
techniques based on optimisation and machine learning models. The authors reviewed 479, 200 and
450 research publications from Scopus, IEEE, and Web of Science, respectively. According to the
authors, there is a notable surge in research towards the advancement of bio-inspired algorithms
accompanied by fusion or diverse methodologies of machine learning. A discernible conclusion pro-
posessubstantialfutureresearchinbio-inspiredstrategies,particularlyrootedinSwarmOptimisation
or Genetic algorithms to enhance ML models. This paper contributes to knowledge discovery by
conducting a comparative analysis of the performance and adaptability of hybrid techniques based
onoptimisationandMLacrossdifferentdomains.
In the literature review, most of the selected research papers are published as SLR that contain
reviewsofpapersonclassification,dataanalyticswithfeatureengineering,andsamplingtechniques,
which provide a brief understanding of historic research work and proposed research gaps related
to our problem statement published between 2014 and 2024 [5,14,17]. All of these studies describe
the importance and impact of AI and ML models along with pre-processing techniques in different
domains including medical and financial fields. We also reviewed some case studies, which are
subdividedanddistinguishedbasedonthedatasetdistributionratiofromdifferentdomains.

1712 CMC,2024,vol.81,no.1
3.2 CaseStudiesofClassifiersImplementation
This section includes a scholarly examination of studies that implemented different classifiers
to address their respective research questions. This section includes case studies with structured,
unstructured, or semi-structured datasets; excluding case studies with imbalanced datasets. For
example, the study [18] investigated credit card fraud detection using the RF algorithm on a dataset
based on customer behaviour. The study assessed Accuracy and Precision by using DT, RF, LR,
and AdaBoost as classifiers and found that RF outperformed others with a 94.40% accuracy score.
Anotherstudy[19]assessedclassifierperformanceusingadatasetofabstractsfetchedfromdifferent
existingresearch.Thedatasetconsistsof107researchabstracts,with36relatedtoScienceandSocial
Sciences and 35 from Business. They used DT, SVM, KNN, and NB to classify research abstracts
into classes of Science, Business, and Social Sciences based on ‘term frequency-inverse document
frequency’and‘bagofwords’,whileevaluatingtheirperformanceonaccuracy,precision,recall,andF-
1score.SVMagainoutperformsotherclassifiersincomparativeresults.Datapre-processinginvolves
tokenisation,textcleaning,stop-wordremoval,stemming,andfeatureextraction.
In research work [20], analysis and classification were performed on diabetes data using the
Waikato Environment for Knowledge Analysis (WEKA) tool with SVM, RF, and NB classifiers.
Onceagain,SVMdemonstratedsuperiorperformancecomparedwiththeotherclassifiers,particularly
under a binary target variable. However, the study also noted that RF performed well in terms
of Accuracy, Precision, and MAE under the binary target variable. Meanwhile, the authors in the
study [21] discussed various probabilistic and linear classifiers under supervised learning, including
Boosting, DT, RF, SVM, NN classifiers, LR, NB, and the maximum entropy classifier. Study [22]
utilised ML classifiers to analyse and predict real estate pricing using a multi-attribute dataset. The
studyimplementedKohonenmaps,NN,andDTonarealestatedatasetfromtheonlineplatformfor
machinelearning(Kaggle);subsidiaryofGoogleLLC.Despiteseverallimitations,theauthorsfound
thatDTperformedwellintermsofAccuracy,whichwasthesolemetricusedforevaluation.InStudy
[23], the author named NB and RF as the two best-performing models for predicting bank money
launderingtransactionscomparedwithLRandCategoricalBoosting(CatBoost).Furthermore,they
verified through the results that the Artificial Neural Network (ANN) model slightly outperformed
allaforementionedclassicMLmodels.
TheconcludingresultsofthereviewedexistingworksarepresentedintermsofAccuracy,Recall,
Precision,andF-1score.Table2presentstheresultsforthecomparativeevaluationofreviewedcase
studies with classifier implementations on different datasets. (χ represents ‘Not Stated’ in Tables2
and3asdefinedintheNomenclatureofthedraft).
To summarise Table2, the studies listed in the table utilise diverse types of datasets and focus
onvariousresearchareas,demonstratingtheversatilityandeffectivenessofmachinelearningmodels
across different domains. These studies employed conventional classifiers, yielding diverse results on
performance metrics, which supports the statement that “the performance of classification depends
not only on the selection of the algorithm but also on the quality and form of the input dataset”
[14]. This also reiterates that traditional classifiers, with fine-tuned hyper parameters, can produce
acceptableresultsforclassificationproblems.Thisunderscoresthenecessityofresearchoncombining
multiple techniques and algorithms with optimised hyperparameter tuning to achieve robust results.
Most of the studies used and recommend Accuracy, Precision, Recall, and F-1 score as relevant
performancemetrics.

CMC,2024,vol.81,no.1 1713
Table2: CasestudiesofClassifiersimplementationondifferentdatasets
| Study |     | Comparisonmetrics |     |     |
| ----- | --- | ----------------- | --- | --- |
Classifiers Datasets Accuracy Sensitivity/Recall Precision F-1score
| DT             |                       | 0.86 | χ    | 0.94 χ    |
| -------------- | --------------------- | ---- | ---- | --------- |
| RF             |                       | 0.94 | χ    | 0.94 χ    |
| [18] LR        | Credit-carddataset    | 0.93 | χ    | 0.93 χ    |
| AdaBoost       |                       | 0.93 | χ    | 0.93 χ    |
| MajorityVoting |                       | 0.93 | χ    | 0.93 χ    |
| DT             |                       | 0.63 | 0.64 | 0.64 0.69 |
| SVM            |                       | 0.88 | 0.89 | 0.89 0.89 |
| [19]           | Researchpapersdataset |      |      |           |
| KNN            |                       | 0.86 | 0.85 | 0.85 0.85 |
| NB             |                       | 0.83 | 0.82 | 0.82 0.84 |
| SVM            |                       | 0.77 | χ    | 0.74 χ    |
| NB             |                       | 0.76 | χ    | 0.67 χ    |
| [20]           | Diabetesdataset       |      |      |           |
| DT             |                       | 0.73 | χ    | 0.63 χ    |
| RF             |                       | 0.74 | χ    | 0.65 χ    |
Moneylaundering
| ANN |     | 0.80 | 0.72 | 0.87 χ |
| --- | --- | ---- | ---- | ------ |
[23]
dataset
Table3: Casestudiesofclassifiersimplementationonimbalanceddatasets
Comparisonmetrics
Study Classifiers Datasets Accuracy Sensitivity/ Precision AUC F-1 Targetclass
Recall score distribution
| LR      |     | 0.99 0.61 | 0.90 χ | 0.73 |
| ------- | --- | --------- | ------ | ---- |
| DT      |     | 0.99 0.75 | 0.88 χ | 0.81 |
| XGBoost |     | 0.99 0.80 | 0.91 χ | 0.85 |
Credit-cardfraud
| [4] ANN |     | 0.99 0.83 | 0.87 χ | 0.85 99.83:0.17 |
| ------- | --- | --------- | ------ | --------------- |
detectiondataset
| ROS+XGBoost |     | 0.99 1.0 | 0.99 χ | 0.99 |
| ----------- | --- | -------- | ------ | ---- |
RUS+XGBoost
|                |     | 0.92 0.90 | 0.95 χ | 0.92 |
| -------------- | --- | --------- | ------ | ---- |
| SMOTE+XGBoost  |     | 0.99 0.98 | 0.99 χ | 0.99 |
| SGD(Stochastic |     | 0.44 0.39 | 0.86 χ | 0.17 |
GradientDescent)
| KNN | Bankmarketing | 0.82 0.97 | 0.84 χ | 0.28 |
| --- | ------------- | --------- | ------ | ---- |
88:11.69
| [6] LR | dataset | 0.85 0.99 | 0.85 χ | 0.75 |
| ------ | ------- | --------- | ------ | ---- |
| GNB    |         | 0.85 0.92 | 0.89 χ | 0.53 |
| DT     |         | 0.85 0.94 | 0.89 χ | 0.56 |
| RF     |         | 0.87 0.98 | 0.87 χ | 0.81 |
(Continued)

| 1714 |     |     |     | CMC,2024,vol.81,no.1 |
| ---- | --- | --- | --- | -------------------- |
Table3 (continued)
Comparisonmetrics
Study Classifiers Datasets Accuracy Sensitivity/ Precision AUC F-1 Targetclass
Recall score distribution
| AdaBoost      |              | χ 1.0     | 0.66 χ    | 0.80             |
| ------------- | ------------ | --------- | --------- | ---------------- |
| XGBoost       | Glassdataset | χ 1.0     | 1.0 χ     | 1.0 95:05        |
| LR            |              | χ 1.0     | 0.66 χ    | 0.80             |
| [9] AdaBoost  |              | χ 0.80    | 0.72 χ    | 0.76             |
| XGBoost       | Ecolidataset | χ 0.80    | 0.57 χ    | 0.66 90:10       |
| LR            |              | χ 0.70    | 0.63 χ    | 0.66             |
| AdaBoost      |              | χ 0.98    | 0.98 χ    | 0.98             |
| XGBoost       | Wi-Fidataset | χ 0.99    | 0.98 χ    | 0.98 75:25       |
| LR            |              | χ 0.75    | 0.86 χ    | 0.81             |
| Grid-searchRF | MIED         | 0.73 0.88 | 0.77 0.76 | 0.82 76.30:23.70 |
| Grid-searchRF | EIED         | 0.88 0.19 | 0.66 0.80 | 0.29 93.4:6.6    |
| Grid-searchRF | MIED         | 0.87 0.81 | 0.92 0.96 | 0.87 76.30:23.70 |
withROS
| Grid-searchRF | EIED | 0.98 0.99 | 0.97 0.99 | 0.98 93.4:6.6 |
| ------------- | ---- | --------- | --------- | ------------- |
withROS
| [10] Grid-searchRF | MIED | 0.70 0.66 | 0.72 0.76 | 0.69 76.30:23.70 |
| ------------------ | ---- | --------- | --------- | ---------------- |
withRUS
| Grid-searchRF | EIED | 0.73 0.72 | 0.73 0.80 | 0.72 93.4:6.6 |
| ------------- | ---- | --------- | --------- | ------------- |
withRUS
| Grid-searchRF | MIED | 0.77 0.74 | 0.79 0.86 | 0.77 76.30:23.70 |
| ------------- | ---- | --------- | --------- | ---------------- |
withSMOTE-
NC+RUS
| Grid-searchRF | EIED | 0.90 0.89 | 0.91 0.96 | 0.90 93.4:6.6 |
| ------------- | ---- | --------- | --------- | ------------- |
withSMOTE-
NC+RUS
Logisticregression Bankmarketing 0.80 0.80/0.77 χ 0.89 0.88/0.47
88.31:11.69
| [24] SVM | dataset | 0.89 1.00/0.00 | χ 0.89 | 0.94/0.00 |
| -------- | ------- | -------------- | ------ | --------- |
randomforest
| [25] Neuralnetwork |     |     | 0.80 | χ   |
| ------------------ | --- | --- | ---- | --- |
Bankmarketing
| Decisiontree |     | χ χ | χ 0.75 | χ 87.62:12.38 |
| ------------ | --- | --- | ------ | ------------- |
dataset
| Supportvector |     |     | 0.76 | χ   |
| ------------- | --- | --- | ---- | --- |
machine
3.3 CaseStudiesofClassifiersImplementationonImbalancedDataset
This section includes the revision of academic case studies on classifiers applied to imbalanced
datasets. One of the objectives of these studies was the critical evaluation of classifiers on real-world
imbalanced datasets. While recapitulating the study [4], the authors offered significant insights into
how imbalanced data can affect the performance of ML models in detecting credit card fraud.
Furthermore, the research proposes techniques, such as Random Oversampling (ROC), Random

CMC,2024,vol.81,no.1 1715
Undersampling (RUS), and Synthetic Minority Oversampling Technique (SMOTE) to balance the
dataset and improve the performance of XGBoost, thereby enhancing the overall accuracy of fraud
detection systems. ROS performed better than the other two techniques. Among basic classifiers,
XGBoost gives better results than LR, DT, and ANN in terms of Accuracy, Precision, Recall, and
F-1score.AfterapplyingROS,theXGBoostclassifierachievedanF-1scoreof0.99.
Meanwhile, the problem statement of the study [6] is to explore the use of predictive analytics
and ML in direct marketing using a bank marketing dataset. The objectives of this case study were
topredictpotentialcustomersandassesstheperformanceofdifferentclassifiersoncustomer-related
datasets. To achieve their research objectives, the authors implemented KNN, LR, Gaussian Naïve
Bayes (GNB), DT, and RF while assessing performance based on Accuracy, Sensitivity, Specificity,
PositivePredictiveValue,NegativePredictiveValue,andF-1score.RFclassifierappearedasthebest-
performingmodelintermsofpredictivepowercomparedwiththeotherclassifiersinthisstudy.
Study [8] conducted a comparative evaluation by assessing and ranking 66 distinct variations of
minorityoversamplingtechniquesforhandlingimbalanceddatausingPositionalVotingRules(Borda
Count Score) and Non-Parametric Test (Kruskal-Wallis Test Score). They selected 50 datasets from
online data repositories like UCI and Open Platform for Machine Learning (OpenML) with the
distributionof20and30setsofdata,respectively.TheyrankedMinorityCloningTechnique,Cluster-
Based Synthetic Oversampling, SMOTE with Iterative Partitioning Filter, and Proximity Weighted
Synthetic Oversampling as the top 4 imbalanced data handling techniques on the F-measure and
Kruskal-Wallis Test Score for selected implementation on 30 OpenML datasets with DT, RF, and
XGBoost as baseline classifiers. They also evaluated the execution time of these four best balancing
techniques,includingSMOTE,onthe20UCIrepositorydatasets.Theempiricalresultsconcludedthat
Minority Cloning Technique, Cluster-Based Synthetic Oversampling, and SMOTE with Polynomial
Fitting were the top three in terms of execution time and F-measure among the imbalanced data
handlingmethodsusedinthestudy.
Study [9] evaluated the performance of AdaBoost, XGBoost, and LR on imbalanced data
by implementing these classifiers on three UCI repository datasets with 5% (Glass dataset), 10%
(Ecoli dataset), and 25% (Wi-Fi dataset) imbalance rates (Minority class distribution). The authors
concluded that all three classifiers performed worst on 5% imbalanced data, slightly better on 10%
imbalanced, and much better on the 25% imbalanced data. Furthermore, the increase in sample size
andthedecreaseinthepercentageofminorityclassesimpliedthattheclassifiersfailedtopredictthe
minoritycaseseffectively,treatingthemasnoise.Additionally,allthreemethodsexhibitedoverfitting
issues.ThestudyalsorevealedthatLRyieldedbetterresultsforthe5%imbalanceddataset,XGBoost
performed well on the 10% imbalanced dataset, while AdaBoost had the best results on the 25%
imbalanceddataset.
Thestudy[10]aimedtoinformEducationDataMining(EDM)researchersabouttheoperation,
advantages,andlimitationsofselectedresamplingtechniques,includingROS,RUS,andSMOTE.The
studyprimarilyfocusedonRadomForestwithhyperparametertuningongridsearch(GS-RF)asthe
chosen model for performance evaluation on imbalance dataset for learning. The authors selected
Accuracy,Precision,Recall,AUC,andF-1scoreastheevaluationmetrics.Italsoincludedtwotypes
ofdatasetstakenfromtheNationalCentreforEducationStatistics(NCES);moderateimbalancewith
23.7% minority class and extreme imbalance with 6.6% minority class. The authors acknowledged
the limitations of this study, such as the use of a single dataset and the challenge of finding the
optimalhyperparametervalues.Furthermore,theyrecommendedexploringdifferentcombinationsof
resamplingtechniquesandclassificationalgorithmsinthecontextofeducationdataminingforfuture

1716 CMC,2024,vol.81,no.1
research.TheyalsoproposedtheuseofROSformoderatelyimbalanceddataandhybridresampling
forextremelyimbalanceddatatoproducethebestresultsinthecontextofEDM.
Study [13] highlighted the need for efficient sampling techniques to address bias in prediction
when dealing with BD. The authors presented a novel resampling method named SMOTENN; a
fusion comprised of RUS, SMOTE, and Edited Nearest Neighbour (ENN) under the MapReduce
framework.Theauthorsstatethattheproposedresamplingmethodcomplementstheneighbourhood
of the minority class with efficient implementation and performance on small, medium, and large
datasets.TheyalsostudiedENNalongsidetwootherSMOTEvariantsknownasBorderlineSMOTE
and Safe Level SMOTE, for resampling. The experimentation utilised DT and RF as baseline
classifiers on large datasets after processing with ENN, SMOTE, ENN+SMOTE, and SMOTENN
whileusingGeometricmeanmeasureasthePerformancemetric.Theauthorssuggestedtheneedfor
State-of-the-artapproachforimbalancedBDclassificationwithhigh-dimensionaldatasets.
Authors [24] performed basic data analysis and classification on a real bank marketing dataset
[12]. This paper included the implementation of SVM, ANN, LR, and RF as classifiers and one-
hotencodingonallfeaturesduringfeatureengineering.Thepaperconcludedthatthe‘job’;aninput
variable, did not affect the target variable. Furthermore, the RF classifier demonstrated the best
performance among all the classifiers in handling the imbalanced target variable. In another study
[25], data analysis was performed based on the ‘contacts’ and ‘duration’ of calls for the marketing
campaign. The authors analysed a dataset with 150 features and carried out semi-automatic feature
selectionduringthemodellingphasetoreducethenumberoffeatures.Theyusedintuitiveknowledge
and adapted the forward selection method to reduce the features to 22 during the feature selection
phase.TheauthorsalsoperformedthedatasetclassificationusingSVM,NN,andDT.Overall,theNN
classifierperformedbettercomparedtotheotherclassifiersonAUCandAreaoftheLIFTcumulative
cure(ALIFT),whichwerethemetricsusedforcomparison.NNachievedthebestresultsbygiving0.8
onAUCand0.7onALIFTundertherollingwindowscheme.Study[26]performeddataanalysisand
usedone-hotencodingindataprocessing.TheauthorsalsoimplementedKNN,Linearregression,and
LR as classifiers, with fine-tuning to form different models. Their results showed that KNN model
3 performed better in terms of Accuracy, Precision, Sensitivity, and Specificity than other models
presentedinthestudy.
In [27], the authors used two ensemble models and one hybrid ensemble learning model namely
random subspace, multi-boosting, and random subspace multi-boosting respectively, to build a
prediction model that could further improve the success of telemarketing in the banking industry.
Inthisstudy,theauthorsselectedindependentinputvariablesthroughapartialdependenceplotand
described their impact on the target variable. They implemented SMOTE to handle the imbalanced
nature of the dataset. They found that hybrid ensemble learner random subspace-multi-boosting
had the best prediction performance with the selected independent variables. Results for the hybrid
ensemblelearnershowed0.94fortheF-1scoreand0.98fortheAUConthebankmarketingdataset.
TheresultsofthereviewedexistingworksintermsofAccuracy,AUC,Recall,Precision,F-1score,
andtargetclassdistributionareshowninTable3.Thistablepresentstheoutcomesafteracomparative
evaluationofreviewedcasestudieswithclassifierimplementationonimbalanceddatasets.
Different case studies on the implementation of classifiers for imbalanced datasets conclude
that the classifier’s performance depends on the target class distribution and the results of feature
engineering.Sometimes,simpleclassifiersyieldreasonableresults,butwhencombinedwithsampling
techniques, their performance improves significantly. To illustrate this, we evaluate the outcomes of
different studies. For example, the study [24,25] applied multiple different classifiers on the same

CMC,2024,vol.81,no.1 1717
banking dataset with imbalanced target class distribution, using fewer evaluative metrics under
differentconditions.Althoughinthestudy[6],RFgivesabetterF-1scorebutmissestheAUCscorefor
betteranalysisofclassifiersperformanceintermsofunderfittingoroverfitting.Inthestudy[25],the
F-1scoreismissingthroughwhichwecouldanalysetheclassifier’sperformanceonthemajorityclass
orontheminorityclassofthetargetvariable.Study[24]showedbetterperformanceonthemajority
classofthetargetvariablebutperformedpoorlyontheminorityclass,suggestingthattheclassifiers
mighttreattheminorityclassasnoise.Study[9]implementedmultipleclassifiersondifferentdatasets
with varying class distributions of the target variable and provided satisfactory results on the F-1
score.However,itlackedaccuracyandAUCscores,whichareimportantforresultanalysis.Study[4],
demonstrated the implementation of sampling techniques alongside the XGBoost classifier, yielding
quite reliable results for a highly imbalanced target variable with only 492 instances of the minority
class. Study [10] implemented GS-RF, alongside different sampling techniques on education related
dataset with different class distributions in the target variable. This study recommended that GS-
RFwithROSprovidesbetterresultsonmoderatelyimbalancedandextremelyimbalancededucation
datasets. Authors extensively evaluated the performance of RF as a baseline classifier on education
relatedimbalanceddatasetsbeforeandaftersamplingtechniques,providingaconceptualfoundation
forclassifyingimbalancedbankingbigdata.
Based on the reviewed studies, RF, DT, AdaBoost, and XGBoost classifiers have demonstrated
their effectiveness under various conditions and datasets. Consequently, we chose to utilise these
classifiers in our analysis. Additionally, the study [10] recommended illustrating the performance of
thehyperparameterrandomforestmodel.Therefore,weincludedRadomForestwithhyperparameter
tuning on grid search (GS-RF) and random forest with hyperparameter tuning on Random Search
(RS-RF)forimplementationandperformanceevaluationonahighlyimbalancedmarketingdataset.
Paststudies[4,10]suggestedtheuseofaccuracy,precision,recall,AUC,andF-1scoreasperformance
evaluation metrics. Moreover, Wu [24] highlighted that one-hot encoding introduced a curse of
dimensionality issue, leading to the selection of label encoding for feature engineering. The initial
selection criteria for sampling techniques were based on the basic advantages and limitations of the
selected sampling techniques. As RUS and ROS are traditional sampling techniques, the rest of the
samplingtechniquesarebuiltonboth,suchasSMOTE,whichisaminorityoversamplingtechnique.
TheprocessofgeneratingredundantsyntheticvaluesintheminorityclassisnamedSMOTE.Asthe
inclusionofredundantinstancesorvariablescannegativelyaffecttheperformanceoftheresampling
strategy [13], we sought out SMOTE variants. Adaptive Synthetic SMOTE (AdaSyn SMOTE) only
generatesvariableswhenandwhereclassificationisdifficult,therebyimprovingaccuracy[8].RUShas
thelimitationofdealingwithnoiseandcouldpossiblycausethelossofusefulinstancesandvariables
fromthefeaturespace,soweoptedforBorderlineSMOTE2;avariantofSMOTEwheredatavalues
aregeneratedforoversamplingbasedonthevaluesneartheminorityclassborderline.Accordingtoa
study[13],mostpublicationshaveadoptedSMOTEanditsvariantsforoversamplinglargeimbalanced
dataset.WechooseSMOTE,AdaSynSMOTE,andBorderlineSMOTE2alongwithROS,andRUS
for performance evaluation on our dataset as sampling techniques. The performance of classifiers,
however, depends not only on the selected algorithms but also on the quality of input data [13]. In
this study, we selected multiple variants of sampling techniques for implementation to evaluate the
performance of classifiers both before and after applying the sampling techniques, setting the best-
performingclassifierasthebaseline[8,11,13].

1718 CMC,2024,vol.81,no.1
4 ExperimentalResults
In the current experiment, we used Jupyter Notebook with Python language, implementing
libraries like scikit-learn (Sklearn) and imbalance-learn (Imblearn) under various random states and
conditions of the machine, sampling techniques, and classifiers for a comprehensive implementation
of classifiers with sampling techniques and subsequent performance evaluation. The following sub-
sectionsdescribetheexperimentsettings,dataanalysiswithlabelencoding,andclassificationresults
before and after sampling techniques with the discussion of the findings. For this experiment, we
used the Portuguese bank marketing dataset [12] which consists of 45,211 instances or values with
17 variables, including “y”as the target variable. The Portuguese bank dataset contains data related
to marketing campaigns. The target variable ‘y’ indicates “yes”and “no”for the current marketing
campaign. The target variable in our dataset is highly imbalanced, where “yes” values are only of
11.69% while the rest are “no”values in the target variable. We conducted EDA, feature engineering
using label encoding and applied sampling techniques in Jupyter Notebook using Python libraries,
alongwithimplementingMLclassifiers.
After EDA and feature engineering, we split our dataset into training and testing data for the
implementationandperformanceevaluationofclassifiersundersupervisedlearning.Forthispurpose,
weimportedthetrain-testsplitfunctionfromthemodelselectionmoduleoftheScikit-LearnLibrary.
Wesplitthedataintoa70:30proportion,where70%ofthedatawasusedfortraining,and30%was
used for testing under a random state of machine on 100. After splitting, the training dataset had
31,647instancesorvalueswith16inputvariablesorfeaturesand“y”astheoutputvariableortarget
variable. For testing, we had 13,564 instances with the same input and output variables. Given that
the experiment test bed conditions and system parameters, such as the random state and classifier
parameters, can affect the results. Therefore, we conducted multiple iterations of experimentation
using different classifiers and sampling techniques with varying parameters and the random state
of the machine to obtain optimal results. Table4 displays the random state of the machine and
experiment parameters for each classifier or sampling technique that yielded the best results in our
implementation.
Table4: Experimentationparametersofeachclassifier
Model Description
Decisiontree WeimportedtheDecisionTreeclassifierfrom‘tree’moduleofthescikit-learn
library,settingthe‘maxdepth’equalsto3,‘criterion’equalstoGini,andthe
‘randomstate’equalsto25.
Randomforest WeimportedRandomForestclassifierfromensembleofthescikit-learnlibrary
andsetthe‘randomstate’ofmachineequalsto100.
Grid WeimportedGridSearchCrossvalidationfrommodelselectionofscikit-learn
search-random library,whilesettingparameterofn-estimatorat{9,12,15,18,21,24,27},max
forest depthequals5to15andmini-samples-leafequated1to4,‘CrossValidation’
equalsto5,scoringequalstoaccuracyandn-jobsequalsto4.
Wegotthebestestimatorwith‘max-depth’equalsto14,min-samplesleafequals
to4,n-estimatorequalsto24andrandomstateequalsto1withmin-sample-split
equalsto2,maxfeaturesequaltoautoand‘criterion’equalstoGini.So,we
implementedthebestestimatorofgridsearchcrossvalidationrandomforeston
trainingandtestingdatasettogettheresults.
(Continued)

CMC,2024,vol.81,no.1 1719
Table4 (continued)
Model Description
Random WeimportedRandomizedSearchCrossvalidationfrommodelselectionofthe
search-random scikit-learnlibrarywhilesettingparameterof‘n-estimator’startsfrom10andends
forest at1000,‘max-depth’equals10to110,‘n-iterations’equals50,‘CrossValidation’
equalsto5,verboseequalsto2,min-sample-splitequalsto{2,5,10}withrandom
stateequalsto100.Aftergettingrandombestestimatorbymachine,weapplied
thattotrainingandtestingdatasetwiththebestestimateparameterstogetthe
results.
AdaBoost WeimportedAdaBoostclassifiersfromensembleofscikit-learnlibrarywith
randomstateequalsto100andimplementedthemontrainingandtestingdata.
XGBoost WeimportedXGBoostclassifiersfrommachinelearninglibrary,wesettheseed
sizeat25,‘n-thread’equalsto1andrandomstateat100forimplementing
XGBoostontrainingandtestingdata.
ROS+XGBoost WeimportedRandomOverSamplerfromImblearnlibraryandappliedondataset
withrandomstateofmachineequalsto0.SameconditionsforXGBoost
mentionedaboveinthistable.
RUS+XGBoost WeimportedRandomUnderSamplerfromImblearnlibraryandappliedon
datasetwithrandomstateofmachineequalsto0.SameconditionsforXGBoost
mentionedabove.
SMOTE+ WeimportedSMOTEfromImblearnlibraryandappliedondatasetwithrandom
XGBoost stateofmachineequalsto0.SameconditionsforXGBoostmentionedabove.
AdaSyn+ WeimportedAdaSynfromImblearnlibraryandappliedondatasetwithrandom
XGBoost stateofmachineequalsto0.SameconditionsforXGBoostmentionedabove.
Borderline WeimportedBorderlineSMOTE2fromImblearnlibraryandappliedondataset
SMOTE2 withrandomstateofmachineequalsto0.SameconditionsforXGBoost
+XGBoost mentionedabove.
Label encoding was used for feature engineering as our dataset does not have high cardinality,
which could lead to overfitting. Label encoding makes it easier for algorithms to interpret and
understandcategoricaldatawithinadistinctnumberofcategories.Byapplyinglabelencoding,each
category is represented by a unique integer, sometimes ordinal in nature [28]. In our dataset [12]
‘Marital’ had three distinct values of “married”, “single”, and “divorced”, which were changed to
0, 1, and 2 after label encoding to simplify the classifier’s task. We also used a fundamental set of
data categorisation techniques in data analysis and data engineering for classifier implementation.
Forclassificationpurpose,thedatacategorisationprocessinvolvesorganisingandgroupingdatainto
meaningfulcategoriesorclassesbasedoncertaincriteriaorclassattributepatterns.Datacategorising
entailstrainingamodeltoforecastthecategoryorclasstowhichnewdatapointspertain[28].
Fig.5 and Table5 show the confusion matrix, which plays a crucial role in classifier evaluation
[10]. After reading the related work and considering the highly imbalanced target variable, DT, RF,
GS-RF,RS-RF,AdaBoost,andXGBoostwerechosenasinitialclassifiersforimplementation,while
Precision,Recall,Accuracy,F-1score,andAUCwereselectedasmetricsforperformanceevaluation.

1720 CMC,2024,vol.81,no.1
Figure5:Confusionmatrixofaclassifier
Table5: Performanceevaluativemetricsfortheclassification
Metrics Formulae
Precision TP/(TP+FP)
Recall TP/(TP+FN)
Accuracy (TP+TN)/(TP+TN+FP+FN)
F-1score 2TP/(2TP+FP+FN)
4.1 DataAnalysiswithLabelEncoding
Ourresultsaredividedintotwoparts.Firstly,wepresentthedataanalysisresults,whichinclude
EDA, visualisation, and feature engineering. The second part holds classification results and their
evaluation based on different metrics. The data analysis involved EDA and data visualisation to
understand the emerging dataset patterns. In a basic exploratory analysis, we used different data-
frame methods and functions [24,25] to gain a fundamental understanding of each column’s data
values commonly called instances, including the target variable. The exploratory analysis reveals
that our dataset has 45,211 instances and 17 variables or features. The “y” column is our target
variable, andthe other16 arethe inputvariables.Itis necessaryfor classification undera supervised
learning environment to have labelled dataset. The results indicate that there are no missing values,
with different data types. In the ‘age’column, the minimum and maximum ages are 18 and 95 years,
respectively,howevershowsrightskewnessamonginstances.Theresultsshowthat2085countsofage
32appearintheagecolumn,whichisthehighest.Minutecountsofageabove75yearsinourdataset.
Meanwhile, there are 12 unique categories in the ‘job’input variable, with the highest counts of
the blue-collar category. Three unique categories appear in the ‘marital’ column, with most of the
instancesindicatingamarriedstatus.Ourtargetvariablehastwouniquecategories,with5289counts
of“yes”and39,922countsof“no”,indicatingahighlyimbalanceddistributioninthetargetvariable.
The percentage proportion reveals that less than 12% of individuals have a “yes” value, making
this group crucial for devising future strategies for target marketing or offering new products. The
visualisationanalysisincludesplotsofvariousinputvariables,bothindividuallyandinrelationtothe
target variable. Some plots show counts, while others display the percentage proportion of values in
thedataset,whichcanhelpustounderstandhiddentrendsandoverallpatterns.Selectedvisualisation
resultsareshowninFig.6a,bforreference.

CMC,2024,vol.81,no.1 1721
Figure 6: (a) Visualisation of right-skewed “Age”variable. (b) Visualization result of “Job”variable
withcountsof“y”variable
After EDA and data visualisation, we transformed the dataset through feature engineering (i.e.,
binningandlabelencoding).Thefinaldataset,afterlabelencoding,hasalldatacolumnsrepresenting
featurevaluesintheformof0,1,2,3,4,and5,asshowninFig.7andTable6.
4.2 ClassificationResults
Using the post-analysis processed dataset, we evaluated the performance of the implemented
classicclassifiersintermsofAccuracy,Precision,Recall,F-1score,andAUCscore.Accordingtothe
confusionmatrix,theaccuraciesofallclassifiersaregood;however,inourcase,theF-1scoreisamore
importantmetric,whereXGBoostandRS-RFperformedwellonahighlyimbalancedtargetvariable

| 1722 |     | CMC,2024,vol.81,no.1 |     |
| ---- | --- | -------------------- | --- |
dataset.Furthermore,thevaluesofPrecision,Recall,andF-1scoreforpredictinga“yes”targetvalue
arenotasgoodacrossalltheclassifiersused,comparedwiththe“no”targetvalueoftargetvariable.
AUC score is good for all classifiers, but XGBoost shows better results on the F-1 score in our case.
TheAUCscoreforGS-RF,RS-RF,andXGBoostisapproximately90%whichisexceptionallygood.
Once again features ‘durationcat’and ‘contact’have proved to be the most prominent feature in our
implementationresultsasshowninFig.9[25].Table7andFigs.8and9showthecompleteresultsfor
evaluation.
Figure7:DatacategorisationandLabelEncodingresults
Table6: Datasetforclassifiersimplementationafterlabelencoding
| Variables | Datatype | Instancevalues | Labelencoding |
| --------- | -------- | -------------- | ------------- |
| Y         | Binary   | No,yes         | 0and1         |
Agecat Categorical Young,middle-aged,aged-adults,old-age,senior 0–4
citizen
| Marital   | Categorical | Married,Unmarried                  | 0and1 |
| --------- | ----------- | ---------------------------------- | ----- |
| Education | Categorical | Unknown,Secondary,Tertiary,Primary | 0–4   |
| Default   | Binary      | No,yes                             | 0and1 |
| Housing   | Binary      | No,yes                             | 0and1 |
| Loan      | Binary      | No,yes                             | 0and1 |
| Contact   | Categorical | Cellular,Telephone,Unknown         | 0–2   |
| Poutcome  | Categorical | Unknown,Failure,Other,Success      | 0–3   |
Balcat Categorical -8019–0,1–1000,1001–10000,10001–25000, 0–4
25000+(avg.balineuro)
| Daycat | Categorical | 1–7,8–14,15–21,22–28,29–31 | 0–4 |
| ------ | ----------- | -------------------------- | --- |
Monthcat Categorical Aug.–Oct.,Nov.–Jan.,Feb.–Apr.,May–Jul. 0–3
1–2,3–4,5–6,7–8,9–10,10+(inminutes)
| Durationcat | Categorical |     | 0–5 |
| ----------- | ----------- | --- | --- |
1–5,6–10,11–15,16–20,21–25,25+
| Compaigncat | Categorical |     | 0–5 |
| ----------- | ----------- | --- | --- |
1–100,101–200,201–300,301+,nocontact
| Pdayscat | Categorical |     | 0–4 |
| -------- | ----------- | --- | --- |
Previouscat Categorical 0,1–50,51–100,101–150,151–200,200–275 0–5
Jobcat Categorical Unknown,Dependent,Blue-collar,White-collar, 0–5
Business-owner,Retired

CMC,2024,vol.81,no.1 1723
Givenourhighlyimbalancedtargetvariable,predictingpositiveoutcomesaccuratelyisimportant.
TheF-1scoresofallimplementedclassifiersfellshort;however,XGBoostyieldedbetterresultsthan
theotherclassifiers.Therefore,weusedXGBoostasthebaselineclassifierwiththeimplementationof
samplingtechniquesontheimbalanceddataset.
|              | Table7:  | Resultsofclassifiersperformance |        |           |          |
| ------------ | -------- | ------------------------------- | ------ | --------- | -------- |
| Classifier   | Accuracy | Precision                       | Recall | AUC-Score | F-1score |
| Decisiontree | 0.88     | 0.51                            | 0.26   | 0.79      | 0.35     |
| Randomforest | 0.89     | 0.54                            | 0.37   | 0.85      | 0.44     |
| RS-RF        | 0.90     | 0.61                            | 0.36   | 0.91      | 0.46     |
| GS-RF        | 0.90     | 0.65                            | 0.30   | 0.91      | 0.41     |
| AdaBoost     | 0.89     | 0.59                            | 0.59   | 0.89      | 0.41     |
| XGBoost      | 0.90     | 0.59                            | 0.43   | 0.91      | 0.50     |
Figure8:ResultofXGBoostclassifier
Figure9:Featureimportancegraphresult

1724 CMC,2024,vol.81,no.1
4.3 ClassificationResultswithSamplingTechniques
Imbalanced big data classification has been acknowledged as a machine learning problem [13].
As shown in Table7, while XGBoost outperformed the others in terms of the F-1 score, it still fell
short of expectations. Therefore, we implemented XGBoost as a baseline classifier on the dataset
processedwithdifferentsamplingtechniquestohandletheimbalanceddataset.Ourimplementation
resultsshowthattheperformanceofXGBoostasabaselineclassifierincreasedonthedatasettreated
withtheBorderlineSMOTE2samplingtechnique.TheAUCscoreandRecallvaluesalsoshowedan
improvement. The feature ‘durationcat’; after feature engineering proved to be the most important
among feature space. Table8 and Figs.9–11 show the complete result for evaluation of Borderline
SMOTE2+XGBoostperformance.Fig.11showsthefeatureimportancescorederivedbythemodel.
Table8: Resultsofclassifiersperformance
| Classifier | Accuracy | Precision | Recall AUC-score | F-1score |
| ---------- | -------- | --------- | ---------------- | -------- |
ROS+XGBoost
|     | 0.83 | 0.84 | 0.79 0.90 | 0.82 |
| --- | ---- | ---- | --------- | ---- |
RUS+XGBoost
|     | 0.84 | 0.83 | 0.85 0.90 | 0.84 |
| --- | ---- | ---- | --------- | ---- |
SMOTE+XGBoost
|                          | 0.85 | 0.86 | 0.84 0.92 | 0.85 |
| ------------------------ | ---- | ---- | --------- | ---- |
| AdaSyn+XGBoost           | 0.84 | 0.85 | 0.83 0.92 | 0.84 |
| BorderlineSMOTE2+XGBoost | 0.87 | 0.87 | 0.87 0.94 | 0.87 |
Figure10:ResultofXGBoostclassifier
After applying different sampling techniques to the dataset, the performance of the XGBoost
classifier significantly improved across all performance metrics. The bank marketing dataset was
classified using XGBoost after applying BorderlineSMOTE2, and it performed well on all selected
metrics.Ascoreof0.94onAUCand0.87onF-1scoredemonstratestheimprovementinXGBoost’s
performance. Previously, the F-1 score of XGBoost was 0.51 on imbalanced dataset without the

CMC,2024,vol.81,no.1 1725
implementationofanysamplingtechniques.Thefeature‘durationcat’provedtobethemostimportant
featureamongthedatasets.
Figure11:Featureimportancegraphresult
5 Conclusion
Keyinsightsobtainedfrombankmarketingdataafterdataanalysishelpindecision-makingand
formulation of marketing strategies. Data-driven decision-making helps the bank stay ahead of its
competitorsandplanforboththeshortandlongtermwhilemakinginformeddecisions.Italsohelps
to identify key features and hidden patterns for formulating an effective marketing strategy, which
couldbeawin-winpropositionforboththebankandthecustomer.Ourresultshighlightthekeyand
notablefeaturesofthebankmarketingdata,whicharecriticalfordata-drivendecision-making.The
data features ‘durationcat’, ‘housing’, and ‘loan’ are critical and prominent in deciding the decision-
makingstrategyfortargetedmarketing.
This study addressed the research questions by reviewing multiple data analysis techniques to
highlightpatternsandhiddeninsightsfromaquantitativedataset.Analysismethodsareimplemented
toidentifythecorrelationamongvariablesofthedataset.Exploratorydataanalysisresultshighlighted
thepresenceofhighlyimbalancedtargetvariableswith88.30%of‘no’valuesand11.70%of‘yes’values.
For data pre-processing, we implemented data cleaning, feature engineering, and label encoding to
transform the data for classifiers implementation. Furthermore, we implemented classifiers recom-
mended by the recent literature, selecting after SLR. Moreover, we treated the imbalanced data with
samplingtechniquestohandletheimbalancephenomenon.BorderlineSMOTE2samplingtechnique

1726 CMC,2024,vol.81,no.1
enhancedtheperformanceofXGBoostfrom0.51to0.87ontheF-1scoreand0.94from0.91onthe
AUCscore.
Whilefindingsofimplementedclassifiers,recommendedinstudies[4,10]showedgoodaccuracy,
their recall and precision values fell short in predicting the minority class (1 or “yes” target value)
beforetheimplementationofsamplingtechniques.TheAUCscoreforGS-RF,RS-RF,andXGBoost
wasapproximately90%,indicatingexcellentperformance.Givenourhighlyimbalancedtargetvariable
with only 11.69% representing the minority class, F-1 score becomes a crucial performance metric,
where XGBoost performs positively compared to other classic classifiers used. Upon applying
BorderlineSMOTE2, the performance of the XGBoost experienced a significant enhancement when
usingthesampleddataset.TheF-1scoresurgedfrom0.51to0.87andtheAUCscoreenhancedto0.94
from0.91.ThecombinationofBorderlineSMOTE2withXGBoostyieldedpositiveresults,exhibiting
minimaloverfittingandreduceddataloss.Mostofourfindingsalignwithpriorresearchdocumented
inreviewedstudies[4,10,11].
Inourfutureresearch,wewilladdressthechallengeimposedbythelimitedavailabilityofbanking
datasets, primarily due to concerns about security and privacy. Our approach will involve exploring
alternative methodologies and strategies to acquire larger-scale datasets from the banking industry,
which will encompass an increased number of features and instances. This expansion will enable us
to conduct a more comprehensive evaluation of the performance exhibited by supervised learning
models. Furthermore, our future work will focus on the development of novel models that integrate
optimisationtechniques,samplingmethods,andmachinelearningmodelsspecificallytailoredtothe
unique characteristics of banking big data. By seamlessly combining these components, we aim to
contributesignificantlytotheclassificationofimbalanceddatasetsprevalentinthebankingdomain.
Ultimately, this research direction will facilitate and enhance data-driven decision-making processes
withinthebankingindustry.
Acknowledgement:TheauthorswouldliketoextendtheirgratitudetotheKimberlinLibraryAdmin-
istration and the Faculty of Computing, Engineering, and Media at De Montfort University for
providingthespaceandresourcesessentialtocompletingthisresearchstudy.
FundingStatement:ThisresearchreceivedsupportfromtheCyberTechnologyInstitute(CTI)atthe
SchoolofComputerScienceandInformatics,DeMontfortUniversity,UnitedKingdom,alongwith
financial assistance from Universiti Tun Hussein Onn Malaysia and the UTHM Publisher’s office
throughpublicationfundE15216.
Author Contributions: Study, conception, design, interpretation of results, manuscript preparations:
Fahim Nasir. Conception, design, resources, writing review & editing: Abdulghani Ali Ahmed.
Visualisation,fundingacquisition:MehmetSabirKiraz.Reviewedtheimplementationandconcluding
resultswhileadministratingthisproject:IrynaYevseyeva.Resources,writingreview&editing,funding
acquisition: Mubarak Saif. All authors reviewed the results and approved the final version of the
manuscript.
AvailabilityofDataandMaterials:AbankmarketingdatasetispubliclyavailableforuseonUniversity
ofCalifornia,Irvine(UCI)repository[12]andrecommendedforclassificationstudies.
EthicsApproval:Notapplicable.

CMC,2024,vol.81,no.1 1727
ConflictsofInterest:Theauthorsdeclarethattheyhavenoconflictsofinteresttoreportregardingthe
presentstudy.
References
[1] H. Wu, J. L. Hung, and L. Liu, “Impact of big data analytics on banking: A case study,”J. Enterp. Inf.
Manag.,vol.36,no.2,pp.459–479,Mar.2023.
[2] S. B. Kotsiantis, I. Zaharakis, and P. Pintelas, “Supervised machine learning: A review of classification
techniques,”Emerg.Artif.Intell.Appl.Comput.Eng.,vol.160,no.1,pp.3–24,Apr.2007.
[3] X.ShuandY.Ye,“Knowledgediscovery:Methodsfromdataminingandmachinelearning,”Soc.Sci.Res.,
vol.110,Feb.2023,Art.no.102817.doi:10.1016/j.ssresearch.2022.102817.
[4] P.Gupta,A.Varshney,M.R.Khan,R.Ahmed,M.ShuaibandS.Alam,“Unbalancedcreditcardfraud
detectiondata:Amachinelearning-orientedcomparativestudyofbalancingtechniques,”ProcediaComput.
Sci.,vol.218,no.1,pp.2575–2584,Jan.2023.doi:10.1016/j.procs.2023.01.231.
[5] C.S.Lee,P.Y.S.Cheang,andM.Moslehpour,“Predictiveanalyticsinbusinessanalytics:Decisiontree,”
Adv.Decis.Sci.,vol.26,no.1,pp.1–29,Sep.2022.
[6] A.M.Zaki,N.Khodadadi,W.H.Lim,andS.K.Towfek,“Predictiveanalyticsandmachinelearningin
directmarketingforanticipatingbanktermdepositsubscriptions,”Am.J.Bus.Oper.Res.,vol.11,no.1,
pp.79–88,Jan.2024.doi:10.54216/AJBOR.110110.
[7] M. Binjubeir, A. A. Ahmed, M. A. B. Ismail, A. S. Sadiq, and M. K. Khan, “Comprehensive survey
on big data privacy protection,” IEEE Access, vol. 8, pp. 20067–20079, Mar. 2019. doi: 10.1109/AC-
CESS.2019.2962368.
[8] T.Watthaisong,K.Sunat,andN.Muangkote,“Comparativeevaluationofimbalanceddatamanagement
techniquesforsolvingclassificationproblemsonimbalanceddatasets,”Stat.Optim.Inf.Comput.,vol.12,
no.2,pp.547–570,Jan.2024.doi:10.19139/soic-2310-5070-1890.
[9] S. B. S. Lai, N. H. N. B. M. Shahri, M. B. Rahman, and A. B. Rambli, “Comparing the performance of
AdaBoost,XGBoost,andlogisticregressionforimbalanceddata,”Math.Stat.,vol.9,no.3,pp.379–385,
Nov.2021.doi:10.13189/ms.2021.090320.
[10] T. Wongvorachan, S. He, and O. Bulut, “A comparison of undersampling, oversampling, and SMOTE
methodsfordealingwithimbalancedclassificationineducationaldatamining,”Information,vol.14,no.
1,Jan.2023,Art.no.54.doi:10.3390/info14010054.
[11] V.WernerdeVargas,J.A.SchneiderAranda,R.DosSantosCosta,P.R.DaSilvaPereira,andJ.L.Victória
Barbosa,“Imbalanceddatapreprocessingtechniquesformachinelearning:Asystematicmappingstudy,”
Knowl.Inf.Syst.,vol.65,no.1,pp.31–57,2023.doi:10.1007/s10115-022-01772-8.
[12] S. Moro, P. Rita, and P. Cortez, “Bank marketing,” in UCI Machine Learning Repository, 2014. doi:
10.24432/C5K306.
[13] C.Vairetti,J.L.Assadi,andS.Maldonado,“Efficienthybridoversamplingandintelligentundersampling
forimbalancedbigdataclassification,”Expert.Syst.Appl.,vol.246,pp.123–149,Jul.2024.
[14] F.Dakalbab,M.A.Talib,Q.Nassir,andT.Ishak,“Artificialintelligencetechniquesinfinancialtrading:
Asystematicliteraturereview,”J.KingSaudUniv.—Comput.Inf.Sci.,vol.36,no.3,Mar.2024,Art.no.
102015.doi:10.1016/j.jksuci.2024.102015.
[15] J. P. Bharadiya, “A comparative study of business intelligence and artificial intelligence with big data
analytics,”Am.J.Artif.Intell.,vol.7,no.1,p.24,Jun.2023.
[16] S.Dridi,“Supervisedlearning–Asystematicliteraturereview,”Dec.2021.doi:10.31219/osf.io/tysr4.
[17] B. F. Azevedo, A. M. A. Rocha, and A. I. Pereira, “Hybrid approaches to optimization and machine
learningmethods:Asystematicliteraturereview,”Mach.Learn.,vol.113,no.7,pp.4055–4097,Jan.2024.
doi:10.1007/s10994-023-06467-x.
[18] N.Kumar,K.Tomar,T.Sharma,P.Jyala,D.MalikandI.Dawar,“Customerbehaviour-basedfrauddetec-
tionofcreditcardusingarandomforestalgorithm,”in2023Int.Conf.Artif.Intell.Appl.(ICAIA)Alliance
Technol.Conf.(ATCON-1),Bangalore,India,Apr.21–22,2023,pp.1–5.doi:10.1109/ICAIA57370.2023.

1728 CMC,2024,vol.81,no.1
[19] S. Chowdhury and M. P. Schoen, “Research paper classification using supervised machine learning
techniques,” in 2020 Intermountain Eng., Technol. Comput. (IETC), Orem, UT, USA, IEEE, Oct. 2–3,
2020,pp.1–6.
[20] F.Y.Osisanwo,J.E.T.Akinsola,O.Awodele,J.O.Hinmikaiye,O.OlakanmiandJ.Akinjobi,“Supervised
machine learning algorithms: Classification and comparison,”Int. J. Comput. Trends Technol. (IJCTT),
vol.48,no.3,pp.128–138,Jun.2017.doi:10.14445/22312803/IJCTT-V48P126.
[21] R.SaravananandP.Sujatha,“Astateofarttechniquesonmachinelearningalgorithms:Aperspectiveof
supervised learning approaches in data classification,”in 2018 Second Int. Conf. Intell. Comput. Control
Syst.(ICICCS),Madurai,India,IEEE,Jun.14–15,2018,pp.945–949.
[22] A. Borodulin, A. Gladkov, A. Gantimurov, V. Kukartsev, and D. Evsyukov, “Using machine learning
algorithms to solve data classification problems using multi-attribute dataset,”BIO Web Conf., vol. 84,
Jan.2024,Art.no.02001.doi:10.1051/bioconf/20248402001.
[23] M. E. Lokanan, “Predicting money laundering using machine learning and artificial neural net-
works algorithms in banks,” J. Appl. Secur. Res., vol. 19, no. 1, pp. 20–44, Aug. 2022. doi:
10.1080/19361610.2022.2114744.
[24] Y.Wu,“Bigdataproject-bankmarketingcampaign,”Rev.Appl.Socio-Econ.Res.,vol.21,no.1,pp.99–110,
2021.
[25] S.Moro,R.Laureano,andP.Cortez,“Adatadrivenapproachtopredictthesuccessofbanktelemarket-
ing,”Decis.SupportSyst.,vol.62,no.3,pp.22–31,Jun.2014.doi:10.1016/j.dss.2014.03.001.
[26] K. Wlodarczyk and K. S. Ikani, “Data analysis of a Portuguese marketing campaign using bank
marketing dataset,” 2020, Accessed: Aug. 10, 2023. [Online]. Available: https://www.researchgate.net/
publication/339988208
[27] C.Xie,J.L.Zhang,Y.Zhu,B.Xiong,andG.J.Wang,“Howtoimprovethesuccessofbanktelemarketing?
Prediction and interpretability analysis based on machine learning,”Comput. Indus. Eng., vol. 175, Jan.
2023,Art.no.108874.doi:10.1016/j.cie.2022.108874.
[28] S.Suthaharan,“Machinelearningmodelsandalgorithmsforbigdataclassification,”IntegrSer.Inf.Syst.,
vol.36,pp.1–12,2016.doi:10.1007/978-1-4899-7641-3.

© 2024. This work is licensed under
https://creativecommons.org/licenses/by/4.0/ (the “License”). Notwithstanding
the ProQuest Terms and Conditions, you may use this content in accordance
with the terms of the License.