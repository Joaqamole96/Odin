Article
Evaluation of Cost-Sensitive Learning Models in Forecasting
Business Failure of Capital Market Firms
PejmanPeykani1,* ,MoslemPeymanyForoushany2,CristinaTanasescu3 ,MostafaSargolzaei2and
HamidrezaKamyabfar2
1 DepartmentofIndustrialEngineering,FacultyofEngineering,KhatamUniversity,Tehran1991633357,Iran
2 DepartmentofFinanceandBanking,FacultyofManagementandAccounting,AllamehTabataba’iUniversity,
Tehran1489684511,Iran;m.peymany@atu.ac.ir(M.P.F.);mostafa.sargolzaei@atu.ac.ir(M.S.);
h.kamyabfar@gmail.com(H.K.)
3 FacultyofEconomicSciences,LucianBlagaUniversityofSibiu,550324Sibiu,Romania;
cristina.tanasescu@ulbsibiu.ro
* Correspondence:p.peykani@khatam.ac.irorpejman.peykani@yahoo.com
Abstract: Classifyingimbalanceddataisawell-knownchallengeinmachinelearning. One
ofthefieldsinherentlyaffectedbyimbalanceddataiscreditdatasetsinfinance. Inthis
study,toaddressthischallenge,weemployedoneofthemostrecentmethodsdeveloped
forclassifyingimbalanceddata,CorrOV-CSEn. InadditiontotheoriginalCorrOV-CSEn
approach,whichusesAdaBoostasitsbaselearningmethod,wealsoappliedMulti-Layer
Perceptron(MLP),randomforest, gradientboostedtrees, XGBoost, andCatBoost. Our
dataset,sourcedfromtheIrancapitalmarketfrom2015to2022,utilizesthemoregeneral
andaccuratetermbusinessfailureinsteadofdefault. Modelperformancewasevaluated
usingsensitivity,precision,andF1score,whiletheiroverallperformancewascompared
usingtheFriedman–Nemenyitest. Theresultsindicatethehigheffectivenessofallmodels
inidentifyingfailingbusinesses(sensitivity),withCatBoostachievingasensitivityof0.909
onthetestdata. However,allmodelsexhibitedrelativelylowprecision.
Keywords: businessfailureforecasting;imbalanceddata;cost-sensitivelearning;machine
learning;Multi-LayerPerceptron(MLP);randomforest;gradientboostedtrees;XGBoost;
CatBoost;AdaBoost
AcademicEditor:RaymondLee
Received:18December2024
MSC:62M20;62P05;62P20;68T05;68T10;90C90;91B28
Revised:16January2025
Accepted:21January2025
Published:23January2025
Citation: Peykani,P.;Peymany 1. Introduction
Foroushany,M.;Tanasescu,C.;
Sargolzaei,M.;Kamyabfar,H. Inrecentdecades,withadvancementsinMLalgorithmsandcomputationaltools,their
EvaluationofCost-SensitiveLearning application has garnered significant attention among financial experts and
ModelsinForecastingBusinessFailure researchers [1–11]. One of the most critical fields in which they have been applied is
ofCapitalMarketFirms.Mathematics
riskmanagement,particularlycreditriskmanagement. ManystudieshaveusedMLmod-
2025,13,368. https://doi.org/
elstoidentifyfirmsorcustomerslikelytodefaultcomparedtoothers. Machinelearning
10.3390/math13030368
(ML)-basedmodelsofferspecificadvantages. Theyrequirefewerassumptionscompared
Copyright:©2025bytheauthors.
totraditionalmodelsandcanprocessawiderrangeofdata. Unliketraditionalmodels,
LicenseeMDPI,Basel,Switzerland.
whichtypicallyrelyonaccountingormarketdata[12],MLmodelsincorporateabroader
Thisarticleisanopenaccessarticle
setoffactors,suchascashflow,nationalgovernance,andcapitalstructure,makingthem
distributedunderthetermsand
conditionsoftheCreativeCommons moreeffectiveincreditassessment[13–16].
Attribution(CCBY)license Whiletheirperformanceoftensurpassesthatoftraditionalhuman-basedorstructural
(https://creativecommons.org/ models,theyencountersomechallenges[17–19]. Oneofthesechallengesisthestructureof
licenses/by/4.0/).
Mathematics2025,13,368 https://doi.org/10.3390/math13030368

Mathematics2025,13,368 2of29
datasets[20]. MLmodelsworkwithdataandareregularlydevelopedtohandlebalanced
data[21],whileinmanycreditdatasets,inherentimbalancesexist.
Thisislogicalbecausedefaultsarerareoccurrences. Asitisoftenstated, machine
learning models are typically designed for balanced datasets. However, in credit risk
management,itiscrucialtopredictdefaultersasaccuratelyaspossibleduetothehigh
costofmissingadefaulterinacreditsystem. Thisissimilartootherchallenges,suchas
disease detection, where misclassifying a member of the minority class is costlier than
misclassifyingamemberofthemajorityclass[22,23].
Insomestudies,toaddresstheperformancechallengesofMLmodels,thedatasetis
balancedbyselectinganequalnumberofdefaultersandnon-defaulters. However,this
approachisunrealisticandoftenresultsinmodelswithhighbiasduetotheartificially
balanced dataset. In other cases, this imbalance has simply been ignored, resulting in
modelsthatachievehighaccuracybutexhibitlowsensitivity.
Imbalanced data have an impact on the performance of models, although it may
notbevisibleinitially. Forinstance,inahypotheticalcreditdataset,anMLmodelmight
predictbothgoodandbadpayerswiththesamenumberofincorrectclassifications. In
thiscase,becauseofthelownumberofdefaulters,thewholenumberofpayersthattheir
labelpredictscorrectlyishigh,and,asaresult,themachinelearningmodelreachedhigh
accuracyorevenahighAUCscore.
However,thisunderminesthemodel’sabilitytoidentifydefaulterseffectivelybecause
evenaverysmallportionofnon-defaulterfirms,whichwedefinedasthenumberoffalsely
labeledfirmsinMLmodelperformance,canbeavastmajorityofdefaulterfirms,and,asa
result,themodelexhibitsapoorfunctioninfindingthedefaulterfirms.
Thisissueisparticularlyevidentinmetricslikesensitivity,whicharebasedondefining
defaultedborrowersaspositiveornegativeandmeasuretherateofidentifyingeachdata
labelcategory.
Asaresult,itisimportanttonotethatduetothehighnumberofgoodpayersand
theirbetteridentificationrate,generalmetricslikeaccuracyandAUCmayappearhigh
while sensitivity remains low. This discrepancy can lead to credit disasters, especially
consideringthehighcorrelationofdefaults.
Inresponsetothischallenge,severalsolutionshavebeenproposed. Somesolutions
focusonmodifyingthedatadistributionbycreatingartificialinstancesorreducingcertain
instances. Thesecondbrunchemphasizesdevelopingnewalgorithmsthatareexpertson
learningimbalancedata. Thethirdcategoryaimstoallocatedifferentweightstodifferent
classes. Thelastcategoryisreferredtoascost-sensitiveapproaches.
Cost-sensitiveapproachesareconstructedbasedonreal-worldoutcomes. Asamatter
offact,itisinevitablethatwhenadefaultoccursaftercreditriskmanagementpredictsthat
thefirmwillnotdefault(falsepositive),itismoreexpensivethanpreventingallocating
capitaltoafirmthatispredictedtodefaultalthoughitwillnot(falsenegative).
Manycost-sensitiveapproacheshavebeenintroducedinrecentyears;however,few
ofthemhavebeenstudiedtodetectdefaulterfirms. Inthisessay,wefirstreviewresearch
onimbalanceddatasetsandtheperformanceofnotablestudiesincreditpredictionusing
cost-sensitiveMLmodels. Then,weexploretheperformanceofnotablepapersincredit
predictionusingcost-sensitivemachinelearningmodels. Finally,weevaluatetheperfor-
manceofoneofthemostrecentcost-sensitivemodelsforimbalanceddatasets,asproposed
in work by Devi et al. [24], which combines several decision tree-based models for the
firsttime.
Inthispaper,forthefirsttime,Devietal.’s[24](CorrOV-CSEn)methodisusedin
businessfailureprediction. Additionally,weemployoneofthestate-of-the-artalgorithms
introducedinrecentyears,CatBoost,inconjunctionwithacost-sensitiveapproach. We

Mathematics2025,13,368 3of29
believethatCatBoost’sabilitytopreventoverfittingisexpectedtoenhanceourmodel’s
performance.OurthirdcontributionistheuseofIraniancapitalmarketfirmsasourdataset.
TheIraniancapitalmarketisoneoftheoldestintheMiddleEastandrecentlywasdescribed
byBloombergasoneofthemost“unfamiliar”largecapitalmarketsintheworld[25].
Theremainderofthispaperisorganizedasfollows: Section2providesabriefreview
ofmethodsdevelopedtoaddressimbalanceddatasetproblemsandtheirapplicationsin
credit risk management. Section 3 details the methodology employed in this study. In
Section4, thecasestudy—focusedonbusinessfailureintheIraniancapitalmarket—is
analyzed. Section5presentstheexperimentalresults,discussingtheperformanceofeach
machinelearningmodel. Finally,Section6concludesthepaperwithrecommendationsfor
futureresearch.
2. LiteratureReview
Our literature review is divided into two parts. The first part addresses previous
workonimbalanceddatasets,primarilythatdevelopedbycomputersciencescholars. The
second part explores the application of these models in finance, with a focus on credit
riskmanagement.
2.1. ImbalanceDatasetsSolution
Numerousmethodshavebeenproposedtoaddresstheissueofimbalanceddatasets.
Theseapproachesaregenerallycategorizedintothreetypes[26]: (A)data-level(orresam-
pling)methods,(B)algorithm-levelmethods,andC)cost-sensitivelearning,respectively.
Data-level(orresampling)methodsaddressimbalanceddatasetsbymodifyingthe
structure of the data. This can be achieved through under-sampling, oversampling, or
hybridresamplingmethods. Inunder-sampling,onlyasubsetofthemajorityclassisused
ofthemajorityclassaretrained. MethodssuchasTomeklinks[27],KubatandMatwin[28],
Japkowicz [29], Neighborhood Cleaning Rule (NCL) [30], Relevant Information-based
Under Sampling (RIUS) [31], Lee & Seo [32], and EUStack [33] are examples of under-
samplingapproaches.
Oversamplingmethods,ontheotherhand,involvecreatingadditionalcopiesofthe
minority class to balance the training set. Solberg and Solberg [34], WK-SMOTE [35],
MAHAKIL [36], GSMOTE-NFM [37], SMOTEFUN [38], SMOTE-tBPSO-SVM [39], and
Approx—SMOTE[40]areexamplesofsuchmethods.
Hybridresamplingmethodsusuallycombineoversamplingandunder-sampling. The
Synthetic Minority Oversampling Technique (SMOTE), introduced in 2002 by Chawla
etal.[41],isawidelyusedhybridresamplingapproach. Otherhybridresamplingmethods
includeLingandLi[42],RFMSE[43],RK-SVM[26],SA-CGAN[44],SMOTified-GAN[45],
andPuri&Gupta[46].
Algorithm-level methods focus on developing algorithms specifically designed to
classifyimbalanceddata.TheRUSBoostalgorithm[47],WeightedEnsemblewithOne-Class
ClassificationwithOversamplingandInstanceSelection(WECOI)[48],andLasso-Logistic
RegressionEnsemble[49]areexamplesofthesemethods.
Cost-Sensitive Learning addresses misclassification by assigning different costs to
errors. In traditional ML models, misclassifications—such as false negatives (FN) and
false positives (FP)—are often treated equally. However, in reality, the consequences
oftheseerrorscanvarysignificantly, especiallyindomainslikecreditclassification. In
this context, there is a loss function that considers four possible outcomes in a binary
classificationproblem,suchasdistinguishingbetweendefaultersandnon-defaulters(or

Mathematics2025,13,368 4of29
1and0). ThematrixbelowillustratesthecostmatrixusedinaregularMLalgorithmfor
creditclassification.
(cid:34) (cid:35)
C(1¸1) =0 C(1¸0) =1
(1)
C(0¸1) =1 C(0¸0) =0
Inthecostmatrix,C(i¸j)representsthecostoflabelinganinstanceX,withanactual
valueofjasi. Whentheinstanceiscorrectlylabeled,thereisnocost. However,forboth
typesofmislabeling(falsepositivesandfalsenegatives),thecostistypicallysetto1.
Cost-SensitiveLearningincorporatesthelossfunctionthroughtwomainapproaches:
directandindirect. Inthedirectapproach,thelossfunctioninfluencesthetrainingprocess
itselfbyadjustingthemodelbasedonmisclassificationcosts. Intheindirectapproach,the
lossfunctionisappliedaftertraining,eitherbymodifyingdecisionthresholdsorusinga
Bayesiandecisionframeworktominimizeexpectedcosts[50].
InCost-SensitiveLearning,differentmisclassificationcostsaretakenintoaccount. In
real-worldscenarios,thecostofafalsepositive(e.g.,incorrectlyclassifyinganunhealthy
firmashealthy)canbesignificantlydifferentfromthecostofafalsenegative. Misclassifica-
tioncostscanbeassignedusingvariousapproaches. Asaresult,whiletraditionalmachine
learningmethodsfocusonminimizingoverallmisclassificationandmaximizingaccuracy,
Cost-SensitiveLearningmethodsaimtominimizethetotalcostsassociatedwithdifferent
typesofmisclassificationerrors.
Oneofthemostpioneeringcost-sensitivemethodswasICET,introducedbyTurneyin
1995[51]. Itwasbuiltongeneticalgorithms. Othercost-sensitivemodelsbasedondecision
treeswereintroducedbyLingetal.[52]andDrummondandHolte[53].
Somecost-sensitivemethodsuseathresholdprobabilityforalgorithms,whichpro-
ducesprobabilitiesforeachinstanceclassification,suchasMetaCost[54],CostSensitive-
Classifier[55],Cost-sensitivenaïveBayes[56],andEmpiricalThresholding[57].
Khanetal.[58]proposedacost-sensitivemethodbasedonthedeepConvolutional
Neural Network that focuses on feature selection. They did not alter data distribution.
Unlikepreviousmodels,theysetclassdependentcostsautomaticallyduringthelearning
procedure. Theefficiencyoftheirmodelhasbeendemonstratedinsubsequentworks[59].
TheCost-sensitiveGeneralVectorMachine(CFGVM)wasproposedbyFengetal.,which
combinesfeatureselectionandGVM[60]. Devietal.[24],combinedAdaBoostensemble
learningwithcorrelation-basedoversamplingintheirproposedmodel.
2.2. ImbalancedLearninginFinance
Usingmachinelearningmethodsincreditriskassessmenthasalreadybeenextensively
exploredintheliterature. However,thevastmajorityofthesestudieshavenotconsidered
the imbalanced nature of datasets [22]. Among the notable works in utilizing machine
learningtoolsforpredictingdefaults,Khandanietal.[61]evaluatedmachinelearning-based
modelsforpredictingcreditcarddefaultrisk. Theyemployedfourclassifierthresholds
to classify the data, achieving sensitivity values of 65%, 78%, 83%, and 88% for each
threshold,respectively.
Barboza et al. [62] conducted a comprehensive study examining the credit risk of
NorthAmericancompaniesfrom1985to2013. Thedatasetincluded10,000companiesand
aimedtopredictdefaultsoneyearinadvance. Theyemployedvariousmodels,including
supportvectormachines,bagging,boosting,andrandomforestsandcomparedtheseto
statisticalmodelssuchasdiscriminantanalysis,logisticregression,andneuralnetworks.
Theirfindingsindicatedthatmachinelearningmodelsoutperformedtraditionalonesin
predictingcorporatedefaultsbyupto10%,asmeasuredbytheROCscore. Notably,the
randomforestmodeldemonstratedexceptionalaccuracy,achieving87%,whichsurpassed

Mathematics2025,13,368 5of29
othermodels. However,thesensitivityoftherandomforestremainedintherangeof0.76
to0.83.
Yildrim[63]conductedastudytodeveloptwomodelsforpredictingcorporatede-
faultsusingasampleof1millionTurkishcompaniesfrom2010to2018.Thestudyevaluated
logisticregression,decisiontree,randomforest,andgradientboostedtreemodels. The
averageAUCscoresforthesemodelswere0.76,0.80,0.82,and0.82,respectively. How-
ever, the sensitivity of the three tree-based models was notably low, at 0.15, 0.17, and
0.30,respectively.
Inasimilarstudyusingthesamedataset,Peykanietal.[64]employedtwomachine
learningmodels—randomforestandgradientboostedtrees—topredictbusinessfailure
in the Iranian capital market. Both models achieved exceptionally high ROC scores of
0.97. However,theirsensitivityfordefaultedfirmswas0.66forrandomforestand0.77for
gradientboostedtrees.
Chen&Ribeiro[65]combinedmultipleclassifiers,includingKNN,supportvector
machines, and decision trees, using a consensus approach for bankruptcy prediction.
The dataset consisted of 37 French firms, and the ensemble method aimed to improve
therobustnessandaccuracyofpredictionsbyintegratingresultsfromseveralmachine
learningtechniques.
Bahnsenetal.[66]presentedacost-sensitivedecisiontreealgorithmdesignedtoac-
countforthevaryingcostsassociatedwithdifferentinstancesbyincorporatingacost-based
impuritymeasure. Theyintroducedanewperformancemetriccalled“Saving”toevaluate
modelperformance. Thisalgorithm istestedon variousreal-world datasets, including
creditcardfrauddetectionandcreditscoring. Theresultsindicatethatitoutperformsother
methodsacrossalldatasets,achievingsignificantcostsavingsofupto71percentcompared
to32percentforthebenchmarkwhileconstructingsmallertreesthatarefastertobuild,
requiringonlyone-fifthofthetimeneededfortraditionaldecisiontrees.
ZakaryazadandDuman[67]addressedthechallengeofimbalanceddatabydevelop-
inganArtificialNeuralNetwork(ANN)modeloptimizedtomaximizeprofitratherthan
traditionalaccuracy. Theirprofit-orientedANNincorporatesacustomizedpenaltyfunc-
tionthatassignsvariablepenaltiesbasedonthefinancialimpactofcorrectlyorincorrectly
classifyingeachinstance,modifyingthetypicalsumofsquarederrors(SSE)functionto
weighmisclassificationsaccordingtoeachinstance’sprofitsignificance. Thefindingsfrom
datasetsinfrauddetectionandbankmarketingindicatethattheANNandNaïveBayes
classifieroutperformothermodels.
Xiaetal.[68]exploredpeer-to-peerlendingdatasetsusingacost-sensitiveweighted
XGBoostapproach. Theirstudyexaminedbothfinancialandnon-financialfactors,withthe
primaryevaluationmetricbeingtheannualizedrateofreturn(ARR).Themodelaimedto
enhanceloanevaluationbybalancingrisksandreturnsforlenders.
Fioreetal.[69]demonstratedthatgenerativeadversarialnetworks(GANs)canbe
employedasanalternativeresamplingtechniquetoenhancecreditcardfraudmodeling.
Notably,earlydefaulthasreceivedlessattentionintheliterature.
PapouskovaandHajek[70]proposedatwo-stageensemblelearningmodeltoevaluate
defaultriskinconsumercredit,particularlyinP2Plending.Inthefirststage,theyemployed
heterogeneousclassificationensemblemodelstopredictwhetheraP2Ploanwoulddefault.
Inthesecondstage,theyappliedheterogeneousregressionensemblemodelstoestimate
the exposure at default for loans that had defaulted. Their findings demonstrated that
thetwo-stagemethodoutperformedsingle-stageapproaches,withtheensemblemethod
achievinggreaterpredictiveaccuracycomparedtotraditionalcreditscoringmodels. They
employedadiverserangeofalgorithms,includingDecisionTree(C4.5),LogisticRegression,
SVM,randomforest,andAdaBoost.

Mathematics2025,13,368 6of29
DeBocketal.[71]addresseduncertaintyinmisclassificationcostsforbusinessfailure
predictionthroughaheterogeneousensembleframework. Themodelincorporatedbag-
ging,randomforests,andmulti-objectiveoptimizationandwasevaluatedon21datasets
spanningvariousindustries. Theresultshighlightedthemodel’sadaptabilitytoscenarios
involvingunknownordynamicmisclassificationcosts.
Houetal.[72]proposedaninnovativeapproachtoaddressingimbalanceddatain
creditscoring. Recognizingthelimitationsoftraditionalstaticensemblemethods,they
introducedadynamicensembleselection(DES)modelspecificallydesignedforimbalanced
classificationtasks. ThemodelfirstappliedSMOTE(SyntheticMinorityOver-Sampling
Technique)tobalancethedataset,therebycreatingamoreeffectivecandidateclassifierpool.
Additionally,theyintegratedDES-MI,aweightingmechanismthatprioritizesminorityin-
stancesduringtheevaluationofclassifiercompetence. Forfurtherrefinement,theyapplied
META-DESforacomprehensivemulti-criteriaassessmentandusedDES-KNNtobalance
classifiercompetencewithdiversity. Testingon15imbalanceddatasetsdemonstratedthat
theproposedmodeloutperformedotherDESapproachesintermsofAUCperformance.
Moreover, when evaluated on real P2P loan data, it achieved a lower Type I error rate
comparedtoXGBoostandLightGBM,highlightingitspotentialformoreaccuratecredit
riskpredictions. Thismodelisparticularlyvaluableforapplicationswherefalsepositives
carrysignificantfinancialconsequences.
Lietal.[73]appliedcreditscoringtoolstoidentifyhigh-riskborrowers, including
onlineloanfraudsters. UsingML-LightGBM,theyaimedtomoreeffectivelyidentifyearly
stagedefaulters. Toenhancepredictionaccuracy,theauthorsincorporatedacost-sensitive
framework into the loss function of the classification model. Tested on a dataset of 1.6
million online loans, their method demonstrated that the cost-sensitive ML-LightGBM
approach outperformed previous models in predictive performance, underscoring its
effectivenessforfrauddetectionandcreditscoring.
Barbagliaetal.[74]investigateddefaultbehaviorinEuropeanresidentialmortgages
leveragingadatasetof12millionloansacrossmultiplecountries. Theymodeledloande-
faultasafunctionofvariablessuchasborrowerprofiles,loancharacteristics,andregional
economicconditions. Bycomparingcost-sensitivemachinelearningalgorithmswithtradi-
tionallogisticregression,theydemonstratedthatmachinelearningmethodssignificantly
enhancedpredictionaccuracy. Theirmodelsincludedgradientboostedtrees,XGBoost,and
LogisticRegression. Theyemployedbothunder-samplingandover-samplingtechniques.
GramegnaandGiudici[75]evaluatedtheirmodelonreal-worlddatafromItaliansmall
and medium enterprises, employing XGBoost with an under-sampling approach. Zou
etal.[76]appliedXGBoostwithacostmatrixtopredictbusinessfailuresintheChinese
capitalmarket. Theyutilizedadiversesetof47financialratiosasfeaturesintheirdataset.
Themodelwascomparedtovariousotherstatisticalandmachinelearningmodels,andthe
resultsindicatedthatXGBoostwithacostmatrixexcelledinminimizingTypeIIerrors.
Chietal.[77]introducedanovelinstance-dependent,misclassificationcost-sensitive
algorithmfordefaultprediction. Thestudyproposedtwoclassifiers—misclassification
cost-sensitive Logistic Regression (MCSLR) and misclassification cost-sensitive Neural
Network(MCSNN)—andevaluatedtheirperformancebyminimizingTypeIandType
II errors, thus improving prediction accuracy in financial decision making. Wang and
Chi[78]utilizedacost-sensitivestackingensemblelearningmethodtopredictfinancial
distressamong3425Chinesecompaniesfrom2000to2020. Thestudyemployedstatistical
tests,includingT-testsandWilcoxonnon-parametrictests,tovalidatethesignificanceof
differencesinfinancialdistresspredictions,underscoringtheeffectivenessoftheensemble
method. Table1. providesasummaryofthediscussioninthissection.

Mathematics2025,13,368
7of29
Table1.Asummaryofthestudiesconducted.
Methodof
| Year | Research |     |     | MachineLearningModel |     | Dataset |
| ---- | -------- | --- | --- | -------------------- | --- | ------- |
ImbalancedData
KNN
2013 Chen&Ribeiro[65] Cost-sensitive SupportVectorMachines 37Frenchfirms
DecisionTrees
Creditcardtransactionsand
| 2015 | Bahnsen[79] |     | Cost-sensitive |     | DecisionTrees |     |
| ---- | ----------- | --- | -------------- | --- | ------------- | --- |
customerdata
Zakaryazadand
| 2016 |     |     | Cost-sensitive |     | ANN | Creditcardfrauddetection |
| ---- | --- | --- | -------------- | --- | --- | ------------------------ |
Duman[67]
Tworeal-worldP2Plending
| 2017 | Xiaetal. | [68] | Cost-sensitive |     | XGBoost |     |
| ---- | -------- | ---- | -------------- | --- | ------- | --- |
datasets
| 2017 | Fioreetal. | [69] | Resampling |     | GAN | creditcardfraud |
| ---- | ---------- | ---- | ---------- | --- | --- | --------------- |
DecisionTree(C4.5)Logistic
|      | Papouskovaand |     |                |     | regression | P2Plending    |
| ---- | ------------- | --- | -------------- | --- | ---------- | ------------- |
| 2019 |               |     | Cost-sensitive |     |            |               |
|      | Hajek[70]     |     |                |     | SVM        | consumerloans |
RandomforestAdaBoost
|      |             |      |                |               | Bagging | 21datasetsacrossvarious |
| ---- | ----------- | ---- | -------------- | ------------- | ------- | ----------------------- |
| 2020 | DeBocketal. | [71] | Cost-sensitive |               |         |                         |
|      |             |      |                | Randomforests |         | industries              |
XGBoost
| 2020 | Houetal. | [72] | Resampling |     |     | P2Ploan |
| ---- | -------- | ---- | ---------- | --- | --- | ------- |
LightGBM
2021 Lietal. [73] Cost-sensitive LightGBM 1.6milliononlineloans
XGBoost
2021 Barbagliaetal. [74] Cost-sensitive GradientBoostedtree 12millionloans
LogisticRegression
|      | Gramegnaand |     |            |     |         | Italiansmallandmedium |
| ---- | ----------- | --- | ---------- | --- | ------- | --------------------- |
| 2021 |             |     | Resampling |     | XGBoost |                       |
|      | Giudici[75] |     |            |     |         | enterprises           |
2022 Zouetal. [76] Cost-sensitive XGBoost Chinesecapitalmarket
LogisticRegression
| 2022 | Chietal. | [77] | Cost-sensitive |     |     |     |
| ---- | -------- | ---- | -------------- | --- | --- | --- |
NeuralNetwork
3425Chinesecompaniesfrom
| 2024 | WangandChi[78] |     | Cost-sensitive | Ensemblelearningmethod |     |     |
| ---- | -------------- | --- | -------------- | ---------------------- | --- | --- |
2000to2020
Randomforest
|     |     |     | Cost-sensitiveand | GradientBoostedtree |     |     |
| --- | --- | --- | ----------------- | ------------------- | --- | --- |
2024 OurResearch Resampling AdaBoost Iraniancapitalmarketfirms
|     |     |     | (CorrOV-CSEn) |     | XGBoost |     |
| --- | --- | --- | ------------- | --- | ------- | --- |
CatBoost
3. Methods
|     |     | 3.1. | CorrOV-CSEn |     |     |     |
| --- | --- | ---- | ----------- | --- | --- | --- |
In this study, we employed recently introduced Correlation-based Oversampling
AidedCost-SensitiveEnsemblelearning(CorrOV-CSEn)technique. CorrOV-CSEninte-
gratestwocomplementaryapproachesforhandlingimbalanceddatasets. First,itapplies
correlation-basedoversamplingtobetterpreparethedataset. Then,theprepareddataare
usedinacost-sensitiveensemblealgorithm,specificallyAdaboostinsomecases,butalso
incombinationwithotherensemblelearningmethods. TheprimarygoalsofCorrOV-CSEn
aretoreduceredundantdatageneration,preventoverfitting,andimprovetheclassification
accuracy of the minority class. Generally, CorrOV-CSEn follows a two-step process, as
detailedbelow. Figure1describesanoverviewoftheCorrOV-CSEnprocess.

MMatahtehmemataictisc2s 022052,51, 31,33, 6x8 FOR PEER REVIEW 88 ooff2 929
FiFgiugurere1 .1O. Ovverevrvieiwewo offt htheeC CororrOrOVV-C-CSESnEnp rporcoecsess.s.
3.31..11..1.C Coorrrerelalatitoionn-B-BaasesdedO Ovveresrasmampplilningg
TThhisiss tespteepn heannhcaensctehse ptheerf opremrfaonrcmeaonfctera doift iotrnaadliotivoenrasal mopvleirnsgammpetlhinogd smliketehSoMdsO TliEke
bSyMinOcoTrEp obrya itnincgorcpoorrrealtaintigo ncoirnrfeolramtioanti oinnfoinrtmoathtieonp rinoctoe stsh.eS ppreoccifiescsa.l lSyp,ewceifiecmalplylo, wyae eLminpelaory
Cao vLainrieaanrc eCMovaatrriiaxn(cLeC MMa)t[r8i0x] (tLoCdMet)e r[m80i]n teot hdeetoeprtmiminael ltehvee olopftiomvaelr slaemvepl loinf go.vTehresaLmCpMlinisg.
caTlhcue lLaCteMd uiss icnaglctuhleatfeodll ouwsiinngg tehqeu faotliloonw:ing equation:
∑ A = ∑ | 𝐴 NN =1 ( | X (cid:3015)(cid:3015) a (cid:2869) ( ) (cid:3025) |(cid:3276) ∑ )| ∑ X (cid:3025) ∈ ∈ N (cid:3015) N (cid:3015)( ( (cid:3025) X (cid:3276) a ) ) ((cid:0)𝑌 Y − − 𝑌(cid:3364) Y )(cid:1)((cid:0)𝑌 Y − − 𝑌(cid:3364) Y )(cid:3021) (cid:1) T (2 (2 ) )
where
w•h ere∑𝐴 represents the Linear Covariance Matrix (LCM);
• • ∑𝑋A(cid:3028) riesp ar emsiennotrsitthy eclLaisnse ianrstCanovcea;r ianceMatrix(LCM);
• • X𝑁
a
𝑁is(a𝑋 (cid:3028)m) indoernitoytecsl atshse ikn-sntaeanrcees;t neighbors (K-NN) of 𝑋
(cid:3028)
;
• • N𝑌N (isX t
a
h)ed menatortiexs otfh Ke-kN-Nn einarsetastncneesig ohf b𝑋or(cid:3028)s; (K-NN)ofX
a
;
• • Y𝑌(cid:3364) i sitsh tehme caetnritxrooifdK o-fN thNe iYn mstaatnrciexs. ofX ;
a
• YTihset hLeinceeanrt rCooidvaorfitahneceY Mmaattrriixx .(LCM) is utilized in two critical ways:
• Oversampling rate determination: Higher LCM values, particularly among the K-
TheLinearCovarianceMatrix(LCM)isutilizedintwocriticalways:
NN of the same minority class, indicate stronger correlation and guide a higher over-
• Oversampling rate determination: Higher LCM values, particularly among the K-
sampling rate. This strategy reduces variance and generates synthetic instances in
NN of the same minority class, indicate stronger correlation and guide a higher
regions with higher minority class correlations, especially near borderline instances.
• o O ve v r e sa rs m am pl p in l g in r g a t r e e . g T io h n is o s p tr t a im te i g z y at r i e o d n u : c F e o s r v e a a r c ia h n m ce in a o n r d it g y e i n n e s r t a a t n e c s e s , y o n v t e h r e s t a ic m i p n l s i t n a g n c i e s s p i e n r-
regionswithhigherminorityclasscorrelations,especiallynearborderlineinstances.
formed only if its LCM with respect to the K-NN of the same class label is greater
• Oversamplingregionoptimization: Foreachminorityinstance,oversamplingisper-
than its LCM with instances from other classes. This ensures that synthetic data are
formed only if its LCM with respect to the K-NN of the same class label is greater
generated in the most relevant regions, enhancing both model robustness and the
thanitsLCMwithinstancesfromotherclasses. Thisensuresthatsyntheticdataare
quality of the generated samples.
generated in the most relevant regions, enhancing both model robustness and the
qualityofthegeneratedsamples.
3.1.2. Cost-Sensitive Ensemble Learning
After applying correlation-based oversampling, the prepared data are fed into an en-
3.1.2. Cost-SensitiveEnsembleLearning
semble learning framework. While previous studies, such as those by Devi et al. [24], used
After applying correlation-based oversampling, the prepared data are fed into an
AdaBoost [81], this study, in addition to AdaBoost, explores a broader range of ensemble
ensemblelearningframework. Whilepreviousstudies,suchasthosebyDevietal.[24],
methods to assess their performance. These methods include Multi-Layer Perceptron
usedAdaBoost[81],thisstudy,inadditiontoAdaBoost,exploresabroaderrangeofensem-
(MLP), random forest [82], gradient boosted trees [83], XGBoost [84], and CatBoost [85].
Each of these ensemble models is adapted to be cost-sensitive, focusing on minimizing the

Mathematics2025,13,368 9of29
blemethodstoassesstheirperformance. ThesemethodsincludeMulti-LayerPerceptron
(MLP),randomforest[82],gradientboostedtrees[83],XGBoost[84],andCatBoost[85].
Eachoftheseensemblemodelsisadaptedtobecost-sensitive, focusingonminimizing
themisclassificationcostsassociatedwiththeminorityclass,whichiscrucialforhandling
imbalanceddatasets. Wedescribethesemethodsindetail.
Multi-LayerPerceptron(MLP)
TheMulti-LayerPerceptron(MLP)[86],atypeoffeedforwardartificialneuralnetwork,
iswidelyusedforbothclassificationandregressiontasksduetoitsflexibilityandabilityto
modelcomplex,non-linearrelationships. TheMLPconsistsofmultiplelayersofneurons,
whereeachneuronisconnectedtotheneuronsinthesubsequentlayerthroughweighted
connections. Thelearningprocessinvolvesadjustingtheseweightstominimizeprediction
error. Thealgorithm’sprocesscanbesummarizedasfollows[87]:
1. AnMLPconsistsofaninputlayer,oneormorehiddenlayers,andanoutputlayer.
Eachlayeriscomposedofseveralneurons(nodes). Ifthedatasetcontains Mfeatures,
theinputlayerwillhave Mneurons. Thenumberofneuronsinthehiddenlayers
canbechosenbasedonthecomplexityofthetask. Eachneuronappliesaweighted
sumofinputsfollowedbyanon-linearactivationfunctionsuchasReLUorsigmoid.
Mathematically,theoutputofaneuroncanbeexpressedas
M
∑
z = w x +b
i i
i=1
wherew aretheweightsoftheconnections,x aretheinputfeatures,andbisthebias
i i
term. Theneuronoutputafterapplyingtheactivationfunction f is
a = f(z)
2. Duringforwardpropagation,inputspassthroughthenetworkfromtheinputlayerto
theoutputlayer. Eachhiddenlayerneuronprocessestheweightedsumofinputsand
appliestheactivationfunction. Thefinaloutputlayerprovidespredictions,which
canbeeitherClassificationorRegression.
3. Thelossfunctionquantifiestheerrorbetweenthepredictedoutputandtheactual
target. Forregression,theMeanSquaredError(MSE)isoftenused.
4. BackpropagationandWeightUpdate: Thegradientofthelossfunctioniscalculated
usingthechainrule,andweightsareupdatedusinggradientdescent.
3.2. RandomForest
Therandomforestalgorithm,introducedbyLeoBreimanin2001[82],isamongthe
mostwidelyusedandaccuratemachinelearningtechniques, includingapplicationsin
creditriskmanagement[88–91]. Itconstructsanensembleofdecisiontreesbydrawing
randomsubsetsfromthedatasetandcombinespredictionsfrommultiple“weak”models
tocreatearobust“strong”model. BasedonCART(ClassificationandRegressionTrees),
eachtreeisindependentlytrainedonabootstrappedsample—arandomsubsetchosen
withreplacement. Thealgorithm’sprocesscanbesummarizedasfollows[92]:
1. BootstrapSampling: ForeachoftheTtreesintheforest,arandomsubsetofthedata
isdrawnwithreplacement. IfthereareNtotalsamples,theneachtreeisbuiltfrom
asubsetD ofNsamplesdrawnrandomlywithreplacement,resultingindifferent
t
trainingsetsforeachtree:
D = {x, y }wherei ∈ {1, 2, ..., N} (3)
t i i

Mathematics2025,13,368 10of29
2. Feature Selection: At each node of the decision tree, a random subset of features
is chosen, typically equal to the square root of the total number of features M in
√
classificationtasks(i.e., M). Thishelpsreducethecorrelationbetweentreesand
improvemodelvariance. Forregression,thenumberofselectedfeaturesisoftenM/3.
Thisfeaturesminimizescorrelationsamongthetrees[60].
3. SplittingCriterion: Fromtheselectedsubsetoffeaturesateachnode,thefeaturethat
bestsplitsthedataischosenusingasplittingcriterion,oftentheGiniindexorentropy.
Forexample,theGiniindexGforasplitcanbecalculatedas
G =1− ∑C p2 (4)
i=1 i
4. BuildingtheForest: Eachtreeisgrowntoitsfulldepthwithoutpruning,resulting
inacollectionofdeep,unprunedtrees. Bydefault,500treesarebuilt,thoughthis
numbercanbeadjustedforspecificapplications.
5. PredictionAggregation:Forclassificationtasks,thefinalpredictionforeachdatapoint
isdeterminedbymajorityvotingacrossalltrees. Leth (x)representthepredictionof
t
thet−thtreeforadatapointx. Then,thefinalpredictionH(x)isgivenby
H(x) = mode{h (x),h (x),..., h (x)} (5)
1 2 T
Forregressiontasks,thefinalpredictionistheaverageofalltreeoutputs:
1 ∑T
H(x) = h (x) (6)
T t=1 t
Random sampling and feature selection in random forest reduce the variance of
individualtreeswhileminimizingcorrelationsamongthem,producinganensemblewith
lowervarianceandhigheraccuracy. Eachtreeintheforestisuncorrelatedwiththeothers,
enhancingthemodel’srobustness.
3.3. GradientBoostedTrees
Gradientboostedtrees(GBT),introducedbyFriedmanin2000[83],extendtheboosting
concepttodecisiontreesbybuildingasequenceofmodelsthatiterativelyminimizeerrors.
Eachmodelfocusesoncorrectingtheerrorsofitspredecessor,creatingastronglearner
from a series of weak learners. Unlike bagging, which trains independent models on
randomsubsetsofdata(asusedinrandomforest),boostinginvolvessequentialtraining
whereeachmodelimprovesuponthepreviousone[93].
Boostingoperatesontheprinciplethatarobustlearningmodelcanbeconstructed
bycombiningmultiplecomplementaryweakmodels. Unlikebagging[94],boostingdoes
notdividethedatasetintorandomsubsets. Instead,itassignshigherweightstosamples
thatweremisclassifiedinpreviousiterations,refiningthemodelstep-by-step. Thisprocess
continuesuntilthemodelachievesadesiredlevelofaccuracyortheerrorisminimized[95].
InGBT,thefirstdecisiontreeT (x)istrainedontheoriginaltargetvaluesy. Subse-
1
quenttreesaretrainedontheresiduals(errors)oftheprecedingmodelstoprogressively
reducetheremainingerror. Forexample,ifyisthetargetvalue,theresidualsforthefirst
treearecalculatedas
r
(1)
= y −T (x ) (7)
i i 1 i
Ineachsuccessivestepm,anewtreeT (x)istrainedtopredicttheresidualsfromthe
m
priormodel. Themodelupdateprocesscanbesummarizedasfollows:

Mathematics2025,13,368
11of29
1. Initializethemodel: Startwithaninitialestimate,oftentakenasthemeanvalueof
thetargetvariableforregressiontasksorasingleweakclassifierforclassification.
∑N
|     |     | F   | (x) = argmin |     | γ   | L(y | γ)  | (8) |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
|     |     |     | 0            |     | i=1 | i,  |     |     |
where L is the loss function, such as squared error for regression or log-loss for
classification.
|                           |     | Foreachiterationm |     |     | =1, |         | M:  |     |
| ------------------------- | --- | ----------------- | --- | --- | --- | ------- | --- | --- |
| 2. IterativeModelUpdates: |     |                   |     |     |     | 2, ..., |     |     |
(m)
• ComputetheResiduals: Calculatetheresidualsr foreachsamplebasedon
i
| thecurrentmodelF |     |     | (x): |     |     |     |     |     |
| ---------------- | --- | --- | ---- | --- | --- | --- | --- | --- |
m−1
|     |     |     | (m) | ∂L(y | i , F | m−1 (x | i )) |     |
| --- | --- | --- | --- | ---- | ----- | ------ | ---- | --- |
|     |     |     | r   | = −  |       |        |      | (9) |
|     |     |     | i   |      | ∂F    | (x )   |      |     |
|     |     |     |     |      | m−1   | i      |      |     |
(m)
• FitaNewTree: TrainanewdecisiontreeT m (x)topredicttheresidualsr .
i
| •   |     |     |     |     |     |     |     | η   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Update the Model: Add the new tree to the model with a learning rate (to
controlthecontributionofeachtree),yieldinganupdatedmodel:
|     |     |     | F (x) | = F | (x)+ηT |     | (x) |      |
| --- | --- | --- | ----- | --- | ------ | --- | --- | ---- |
|     |     |     | m     | m−1 |        | m   |     | (10) |
(x)
3. Final Prediction: After M iterations, the final model F M is an ensemble of the
trees, each adjusted to reduce the error from prior steps. For regression, the final
predictionis
∑M
|     |     | Yˆ = | F (x) = | F (x)+ |     | ηT  | (x) | (11) |
| --- | --- | ---- | ------- | ------ | --- | --- | --- | ---- |
|     |     |      | M       | 0      |     | m=1 | m   |      |
The sequential nature of boosting, combined with gradient descent optimization,
allowsgradientboostedtreestoachievehighaccuracyandperformanceonvariousdatasets.
Thisalgorithmiswell-knownincreditriskprediction[89].
3.4. XGBoost
XGBoost,introducedbyTianqiChenin2016[84],isanoptimizedimplementationof
gradientboostedtrees(GBT)designedtobebothefficientandscalable. XGBoostenhances
traditionalgradientboostingbyaddingregularizationtechniques,treepruning,andad-
vancedhandlingofmissingdata,makingitwell-suitedforhigh-dimensionaldatasets[96].
TheseimprovementshelpXGBoostachievehighpredictiveaccuracyandrobustnesswhile
avoidingoverfitting[97].
OneofthekeydifferentiatorsofXGBoostfromotherGBTmethodsisitsuseofbothL1
(Lasso)andL2(Ridge)regularization. Theseregularizationtermspenalizethecomplexity
ofthemodel,ensuringthatthefinalmodelgeneralizeswellevenwithlargedatasets:
1. ObjectiveFunction:TheobjectiveofXGBoostistominimizearegularizedlossfunction
thatcombinesthetraditionallossfunctionwithregularizationtermsforcomplexity
control. ForTtrees,theobjectivefunctionObjisdefinedas
|     |     |     | = ∑N | L(y, | )+ ∑T | Ω(f | )   |      |
| --- | --- | --- | ---- | ---- | ----- | --- | --- | ---- |
|     |     | Obj |      | i    | yˆ i  |     | t   | (12) |
|     |     |     | i=1  |      |       | t=1 |     |      |
where
• L(y, yˆ )isthelossfunction,suchasmeansquarederrorforregressionorlog-loss
| i   | i   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
forclassification;
| • Ω(f | ) = YT+ | 1λ∑T | w2                                          |     |     |     |     |     |
| ----- | ------- | ---- | ------------------------------------------- | --- | --- | --- | --- | --- |
| t     |         | j=1  | istheregularizationtermwithparametersγandλ, |     |     |     |     |     |
|       |         | 2    | j                                           |     |     |     |     |     |
controllingthecomplexityofeachtree.

Mathematics2025,13,368 12of29
2. TreeStructureandGrowth: EachtreeinXGBoostisbuilttominimizetheresiduals
from the previous trees, following the same general structure as GBT. However,
XGBoostintroducesatree-pruningtechnique,wheretreesareprunedbasedontheir
impactontheobjectivefunctionratherthangrowingtofulldepth. Themax_depth
parameter controls the maximum depth of each tree, preventing the model from
overfittingbylimitingtreecomplexity.
3. UpdateProcess: Ineachiteration,thealgorithmcalculatesthebesttreestructureto
minimizetheresidualsofthepreviousensemble. Theupdatesarecomputedusing
second-ordergradients(Hessian)ofthelossfunction,makingitmoreefficient. The
modelupdateateachsteptisgivenby
yˆ
(t)
= yˆ
(t−1)
+ηf (x ) (13)
i i t i
whereηisthelearningrateand f (x )istheoutputofthet−thtree.
t i
4. HandlingMissingData: XGBoostautomaticallymanagesmissingdatabylearning
optimalpathsforinstanceswithmissingvaluesduringtraining. Itassignsmissing
valuestothemostsuitablebranch,improvingmodelaccuracywhendealingwith
incompletedatasets.
5. FinalPrediction: Thefinalpredictionisanaggregationofalltrees,representedas
∑T
yˆ = F(x ) = f (x ) (14)
i t=1 t i
where x representstheinputfeatures,and f (x )istheoutputfromthet−thtree.
i t i
Forclassification,thefinaloutputisoftendeterminedbyapplyingasoftmaxfunction
toconverttheaggregatedscoretoclassprobabilities.
Byintegratingtheseinnovations, XGBoostachievesahighdegreeofaccuracyand
efficiency,makingitparticularlyeffectiveforcomplextaskssuchashandlingimbalanced
datasetsandfinancialfailureprediction[88,89,98,99].
3.5. AdaBoost
Adaboost, short for Adaptive Boosting, is an ensemble learning method designed
tocreateastrongclassifierbycombiningmultipleweakclassifiers. Thecoreideabehind
Adaboost,likeBoosting,istoiterativelyadjusttheweightsofthetrainingsamples,placing
greater emphasis on those that were misclassified in previous rounds. This approach
enhancestheoverallmodel’saccuracybyforcingeachweakclassifiertofocusmoreon
challengingcases.
Initially,Adaboostassignsequalweightstoalltrainingsample. Ineachiteration,it
selectstheweakclassifierthatperformsbestonthecurrentweighteddatasetandupdates
thesampleweightsbasedonitsclassificationresults. Misclassifiedsamplesreceivehigher
weightsinthenextround,whilecorrectlyclassifiedsamplesareassignedlowerweights.
Thisensuresthatpreviouslymisclassifiedsamplesreceivemoreattentioninsubsequent
rounds,improvingthemodel’soverallaccuracy.
TheAdaboostprocesscanbeformalizedasfollows[81]:
1. Initializesampleweights: Eachsampleiinthetrainingsetreceivesaninitialweight:
w
(1)
=
1
(15)
i N
whereNisthenumberoftrainingsamples.

Mathematics2025,13,368
13of29
2. Train a weak classifier: In each round t, a weak classifier h (x) is trained on the
t
weightedsamples,anditserrorrateϵ t iscalculatedas
|     | ∑N  | (t)     |          |      |
| --- | --- | ------- | -------- | ---- |
| ϵ = | w   | .1(h (x | ) ̸= y ) | (16) |
| t   | i=1 | i t i   | i        |      |
3. Calculatetheclassifier’sweight:Theweightoftheweakclassifierisdeterminedbased
onitsaccuracy:
|     |     | (cid:18) 1−ϵ (cid:19) |     |     |
| --- | --- | --------------------- | --- | --- |
t
|     | a t =ln |     |     | (17) |
| --- | ------- | --- | --- | ---- |
ϵ
t
4. Updatesampleweights: Sampleweightsareupdatedtoreflecttheclassifier’sperfor-
mance,givingmoreweighttomisclassifiedsamples:
| (t+1) | (t)      |         |           |      |
| ----- | -------- | ------- | --------- | ---- |
| w =   | w .exp(a | .1(h (x | ) ̸= y )) | (18) |
| i     | i        | t t     | t i       |      |
5. Combineweakclassifiers: Thefinalstrongclassifier H(x)isaweightedsumofall
weakclassifiers:
|     |     | (cid:16) | (cid:17) |     |
| --- | --- | -------- | -------- | --- |
∑T
| H(x) | = sign | a .h  | (x) | (19) |
| ---- | ------ | ----- | --- | ---- |
|      |        | i=1 t | t   |      |
Throughtheseiterations,Adaboostcreatesarobustensemblemodelcapableofgeneral-
izingwellacrossvariousdatasets,improvingclassificationaccuracysignificantly,especially
forimbalanceddatasets.
3.6. CatBoost
CatBoost,introducedbyProkhorenkovaetal. in2018[100],isapowerfulandefficient
implementationofgradientboostedtrees(GBT)designedtoreduceoverfittingandim-
provepredictiveaccuracy,especiallywithcategoricalfeatures. Theprimaryinnovationin
CatBoostistheuseoforderedboosting,atechniquedevelopedbyDorogushetal.[101],to
addressthetargetleakageproblemthatoftenarisesinstandardboostingalgorithms. This
featuremakesCatBoostparticularlyeffectiveonsmall-tomedium-sizeddatasets,where
targetleakagecansignificantlyimpactmodelperformance.
CatBoostoffersseveraluniqueimprovementsovertraditionalGBTmethods[85]:
1. Ordered Boosting to Avoid Target Leakage: In standard GBT, future data points
mightunintentionallyinfluenceearlierpredictions,leadingtotargetleakage. Ordered
boostingsolvesthisbyusingapermutation-basedscheme,ensuringthatonlypast
informationinfluenceseachiteration. Thisorderedapproachisparticularlyusefulin
datasetswherefeature-targetrelationshipsarecomplexanddynamic,anditenhances
CatBoost’saccuracy.
2. HandlingofCategoricalVariables: CatBoostautomaticallyhandlescategoricalfea-
tureswithoutrequiringextensivepreprocessing. Itconvertscategoricalfeaturesinto
numeric representations through a series of random permutations, using them to
guidethesplittingcriteriaforeachdecisiontree.
3. ObjectiveFunction: CatBoostminimizesaregularizedlossfunctionsimilartoother
boostingmethods,butwithanemphasisonorderedboosting:
| ∑N    |        | ∑J  | Ω(cid:0) (cid:1) |      |
| ----- | ------ | --- | ---------------- | ---- |
| Obj = | L(y.yˆ | )+  | f )              | (20) |
|       | i=1    | i i | j=1 j            |      |
where
• L(y, yˆ ) is the loss function (e.g., cross-entropy or log-loss for classification
i i
tasks);
Ω(cid:0) (cid:1)
• f istheregularizationtermfortreecomplexity,helpingtocontroloverfitting.
j

Mathematics2025,13,368 14of29
4. TreeStructureandDecisionRule: CatBoostusesbinarydecisiontreesasbaselearners.
Foreachinputx,thedecisiontreeassignsittooneoftheleafregionsR basedona
i j
seriesofsplits. Thefunctionforeachtreecanberepresentedas
∑J
H(X i ) = j=1 C j .1 x∈Rj (21)
where
• H(X)representsthedecisionfunctionforeachsampleX;
i i
• R isthedisjointregioncorrespondingtoeachleafinthetree;
j
• C isthepredictedoutputvalueforregionR .
j j
5. FinalPrediction: Thefinalpredictionistheaggregationofallthetreesintheensemble.
ForadatasetwithTtrees,thefinaloutputZisgivenby
∑T
Z = F(X) = f (X) (22)
i t=1 t i
where f (X)istheoutputofthet−thtreeforagiveninputX. Forclassification,the
t i i
modeloftenappliesasigmoidorsoftmaxtransformationtoconverttheoutputinto
classprobabilities.
6. RegularizationandOverfittingPrevention:CatBoostusesrandompermutationswhen
selectingtreesplits,whichreducesoverfittingandenhancesmodelgeneralization.
This,combinedwithorderedboosting,allowsCatBoosttooutperformtraditionalGBT
methodsonmanycomplextasks.
CatBoost have been applied in several papers in order to financial failure predic-
tion[102,103], inthisarticle, weappliedadost-sensitiveapproachtowardthemforthe
firsttime.
By combining correlation-based oversampling with cost-sensitive ensemble learn-
ing, the CorrOV-CSEn approach minimizes overfitting and significantly enhances the
classificationaccuracyoftheminorityclasscomparedtotraditionalmethods.
3.7. BusinessFailure
In our study, we emphasize the concept of business failure rather than terms like
default or bankruptcy. Business failure refers to a situation where a firm faces signif-
icant challenges in continuing its operations. It is a broader concept than default and
bankruptcy. Afirmexperiencingbusinessfailureislikelytodefault,whichmayeventually
leadtobankruptcyifitreachesspecificlegalthresholdsandundergoesthelegalprocess
ofresolution.
In countries like Iran, where the government plays a significant role in the econ-
omy [104,105] and the operation of major companies, firms are often prevented from
defaultinganddeclaringbankruptcyinthecapitalanddebtmarkets. However,theconcept
ofbusinessfailureprovidesavaluableperspectiveforassessingcreditrisk. Businessfailure
hasbeenexaminedinotherstudies,particularlyinrelationtomacroeconomicconditions.
InIran’scapitalmarket,businessfailureiscloselyassociatedwith“Article141ofthe
AmendedCommercialCode.”ThisregulationrequirescompaniesthatfallunderArticle
141topresentadetailedrecoveryplan. ThecorrelationbetweenArticle141andbusiness
failureisevidentinitsfocusonbothfinanciallossesandtheproportionofthoselosses
relativetothecompany’scapital. AcompanyfallingunderArticle141hasaccumulated
lossesthatexceeditsequity,meaningitsassetshavedroppedbelowitsliabilities,which
signalspotentialinsolvency.
Figure2illustratesthepercentageoffirmsineachyearthatfailedunderArticle141as
aproportionofthetotalnumberoffirmsinthatyear.

Mathematics 2025, 13, x FOR PEER REVIEW 14 of 29
In our study, we emphasize the concept of business failure rather than terms like
default or bankruptcy. Business failure refers to a situation where a firm faces significant
challenges in continuing its operations. It is a broader concept than default and bank-
ruptcy. A firm experiencing business failure is likely to default, which may eventually
lead to bankruptcy if it reaches specific legal thresholds and undergoes the legal process
of resolution.
In countries like Iran, where the government plays a significant role in the economy
[104,105] and the operation of major companies, firms are often prevented from defaulting
and declaring bankruptcy in the capital and debt markets. However, the concept of busi-
ness failure provides a valuable perspective for assessing credit risk. Business failure has
been examined in other studies, particularly in relation to macroeconomic conditions.
In Iran’s capital market, business failure is closely associated with “Article 141 of the
Amended Commercial Code.” This regulation requires companies that fall under Article
141 to present a detailed recovery plan. The correlation between Article 141 and business
failure is evident in its focus on both financial losses and the proportion of those losses
relative to the company’s capital. A company falling under Article 141 has accumulated
losses that exceed its equity, meaning its assets have dropped below its liabilities, which
signals potential insolvency.
Mathematics2025,13,368 Figure 2 illustrates the percentage of firms in each year that failed under Arti1c5leo f12491
as a proportion of the total number of firms in that year.
16
14
12
10
8
6
4
2
0
2015 2016 2017 2018 2019 2020 2021 2022
FFigiguurere2 .2.P Peercrecnentataggeeo offfi firmrmssf afialiilninggu unnddererA Artritcilcele1 41141e aecahchy eyaerarf rformom2 0210515to to2 022022.2.
33.8.8..E EvvaaluluaatitninggM Metehthooddss
InIno ouurrr ereseseaarcrhch,,w weeu utitliilzizeeddr aratitoiossd deerirviveeddf rforommt htheee elelemmeenntstso offt htheec coonnffuussioionnm maattrrixix,,
wwhhicihcho offffeersrsv vaaluluaabblelei ninsisgighhtstsi nintotot htheeo ovverearallllp perefroformrmaannceceo offt htheem mooddele.l.T Thheec oconnfufusisoionn
mmaatrtirxixi sisc coommmmoonnlylyu useseddt otoa asssseesssst htheep peerfroformrmaanncceeo offb bininaaryryc clalassssifiificcaatitoionnm mooddeelsl,s,w whheerere
ththeea iamimis isto tod idffieffreernetniattieatbee btweteweneefna ifleadilecdo mcopmanpiaensi(epso (spitoivsieticvlea scsl)aasns)d ahneda lhtheyalcthoym cpoamnipesa-
(nneiegsa t(inveegcaltaivsse) .class).
(cid:34) (cid:35)
TP FN
FP
(cid:4674)
𝑇𝑃
TN
𝐹𝑁
(cid:4675)
(2(233))
𝐹𝑃 𝑇𝑁
In the confusion matrix, 𝑇𝑃 or true positive refers to instances that are actually pos-
Intheconfusionmatrix,TPortruepositivereferstoinstancesthatareactuallypositive
itive and were correctly identified by the model. 𝑇𝑁 or true negative indicates instances
andwerecorrectlyidentifiedbythemodel. TNortruenegativeindicatesinstancesthat
that are actually negative and correctly classified. 𝐹𝑃 or false positive represents in-
areactuallynegativeandcorrectlyclassified. FPorfalsepositiverepresentsinstancesthat
stances that were predicted as positive but are actually negative, while 𝐹𝑁 or false nega-
werepredictedaspositivebutareactuallynegative,whileFNorfalsenegativerefersto
tive refers to positive instances incorrectly classified as negative.
positiveinstancesincorrectlyclassifiedasnegative.
Basedontheconfusionmatrixelements,variousratiosareintroducedtoevaluatethe
performance of binary classification models. In this research, we used three key ratios:
recall,precision,andF1score,whichwillbeexplainedinorderoftheirsignificance.
Recallorsensitivity,calculatedusingFormula(3),measuresthemodel’ssuccessin
identifyingfailedcompanies. Thismetricisconsideredthemostimportant,asagoodcredit
modelshouldbeabletoidentifyallfailingcompaniesandpreventmisclassifyingthem
ashealthy.
TP
Sensitivity= (24)
TP+FN
Precision,calculatedusingFormula4,evaluatestheaccuracyofthemodelinidentify-
ingfailingcompanies. Inotherwords,itindicatesthelikelihoodthatacompanyidentified
asfailingbythemodelisindeedfailing.
TP
Precision= (25)
TP+FP
F1scoreisametricusedtoevaluatebinaryclassificationmodels,especiallyincases
wherethereisanimbalancebetweenthepositiveandnegativeclasses. TheF1scoreisthe
harmonicmeanofprecisionandrecall,calculatedusingthefollowingformula:
2∗Precision∗Sensitivity
F1Score = (26)
Precision+Sensitivity

Mathematics2025,13,368 16of29
Itbalancesthetwometrics,offeringacomprehensivemeasureofamodel’sperfor-
mancebyconsideringbothhowwellthemodelidentifiesfailedcompanies(recall)andthe
accuracyofthosepredictions(precision). Thisscoreisparticularlyimportantwhenboth
falsepositivesandfalsenegativescarrysignificantcosts.
3.9. StatisticalSignificanceTest
WeusetheFriedman–Nemenyitesttodetectsignificantdifferencesamongthemodels.
This approach is commonly employed in research involving machine learning models,
particularlythoserelatedtobusinessfailure. TheFriedmantestissuitableforcomparing
threeormoregroups,especiallywhentheassumptionofnormalityisviolated. Itextends
theWilcoxonsigned-ranktestbyincorporatinganadditionalassumptionofsphericity[106].
TheFriedmanstatisticiscalculatedasdescribedbyFriedman(1937)[107,108]:
X2 = 12 ∑ R2−3n(k+1) (27)
F nk(k+1) i
where
• nisthenumberofdatasets(blocks);
• k isthenumberofmodels(groups);
• R2isthesumofranksforeachmodel.
i
H isthatthereisnosignificancedifferencebetweenthetwomodelsthathavebeen
0
compared,andifX2 crossesthecriticalvalue,thenH isrejected. WhenH isrejected,then
F 0 0
theNemenyitestisused.
4. CaseStudy
ThestatisticalpopulationoftheresearchcomprisesallcompaniesintheIraniancapital
market from 2015 to 2022. Each instance represents a firm’s annual information, with
instanceslabeledaseither“defaulted”or“healthy.”InIran’seconomy,thegovernment
prohibitslargecompaniesfromdeclaringbankruptcyordefault. Consequently,similarto
mostcreditriskresearchinIran,defaultandbankruptcyaredefinedbasedonArticle141
oftheproposedamendmenttoasectionoftheCommercialCode. Accordingtothisarticle,
ifacompanylosesatleasthalfofitscapitalduetoincurredlosses,theboardofdirectors
mustpromptlyconveneanextraordinarygeneralmeetingofshareholderstodecideonthe
company’sdissolutionorsurvival. Article141effectivelyidentifiesconditionsindicativeof
financialdistress,andduetotheaccessibilityofthisinformation,itisusedbyresearchersin
theIraniancapitalmarket. Thefollowingsectionreviewsthemodelsemployed,detailing
theparametersandcalculationmethodsforeachmodel.
Wedividedoursampleintotrainingandtestdatasetsbasedontheyears. Instances
from2015to2021wereconsideredastrainingdatasets,andinstancesfrom2021to2022
werealsoconsideredastrainingdatasets.
Inthisresearch,asthefocusofourinvestigationinvolvescompanieswhoseshares
are traded in the capital market, we have made efforts to categorize variables into two
maingroups: financialstatement-basedvariablesandvariablesrelatedtothecompany’s
stockprice. Thesevariablesareconsideredthemostfundamentalinformationavailablefor
companiesinthecapitalmarket[109].
Barbozaetal.[62]conductedoneofthemostcomprehensivestudiesinvestigating
the default risk of companies in the North American capital market from 1985 to 2013.
Theyemployedtworesearchapproachestodeterminetheirdatasetvariables. Firstly,they
utilizedthevariablesoftheAltmanmodel[110],afundamentalmodeldesignedtoestimate
the default risk of companies. Secondly, they also incorporated the variables used by
Carton&Hofer[111],whicharebasedonthegrowthrateofsomefundamentalcompany

Mathematics2025,13,368
17of29
variables[62]. Ourfeaturesarederivedfromthebalancesheet,whichisessentialincredit
studies[112].
Itisessentialtomentionthatthecriterionusedinthisresearchfordefaultisnotthe
actualdefaultbuttheinclusioninArticle141,whichismeasuredbasedontheratioofthe
retainedearningstotheregisteredcapitalofthecompany. Oneofthevariablesusedby
Altman(variableX2),representingtheratioofretainedearningstoregisteredcapital,is
excludedfromthedatasetvariableslist. ThereasonforexcludingAltman’sX2isthatthe
defaultcriterioninthisstudyalreadyreliesonthesameratio,thusavoidingredundancy
andoverlappingmetrics. Additionally,oneoftheCarton&Hofervariables,GE,which
measuresthegrowthinthecompanyemployeecount, wasremovedduetothelackof
completeandreliabledata.
The variables of the training and test datasets are as follows, as shown in Table 2,
consideringtheaforementionedpoints.
Table2.Featuresofthedatasetandtheirrespectiveformulas.
|     |     | Variable |     |     |                                             | Formula                      |     |     |
| --- | --- | -------- | --- | --- | ------------------------------------------- | ---------------------------- | --- | --- |
|     |     | X1       |     |     | NetWorkingCapital/Totalassets               |                              |     |     |
|     |     | X3       |     |     | Earningsbeforeinterestandtaxes/Totalassets  |                              |     |     |
|     |     | X4       |     |     | Marketvalueofshare∗numberofshares/Totaldebt |                              |     |     |
|     |     | X5       |     |     |                                             | Sales/Totalassets            |     |     |
|     |     | OM       |     |     | Earningsbeforeintrestandtaxes/Sales         |                              |     |     |
|     |     | GA       |     |     | Totalassetst                                | −Totalassetst−1/Totalassetst |     |     |
|     |     | GS       |     |     |                                             | Salest−Salest−1/Salest−1     |     |     |
|     |     | CROE     |     |     |                                             | ROE t−ROE                    | t−1 |     |
|     |     | CPB      |     |     | Price−to−Book                               | t−Price−to−Book              |     |     |
t−1
Table 3 shows the statistical description of our training and test data. The table
providesastatisticalsummaryofthetrainingandtestdatasets,detailingkeyvariables(e.g.,
X1,X3,andX4). Metricssuchasthemean,standarddeviation,minimum,maximum,and
quartilesofferinsightsintothedistributionofeachvariable.X4andGSexhibitconsiderable
variability,withlargestandarddeviationsandextrememaximumvalues. Thetrainingset
showsmorestability,whilethetestsetincludesoutliers,particularlyforX4andGS.These
variationscouldimpactthemodel’spredictiveperformanceandgeneralizability.
Table3.Statisticaldescriptionofourtrainingandtestdata.
| TrainingSet | X1 X3     | X4   | X5   | OM   | GA   | GS   | CROE | CPB  |
| ----------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| count       | 2987 2987 | 2987 | 2987 | 2987 | 2987 | 2987 | 2987 | 2987 |
−2.688
| mean | 0.083 0.129 | 19.821 | 0.724 |     | 0.374 | 349.054 | 0.698 | 0.057 |
| ---- | ----------- | ------ | ----- | --- | ----- | ------- | ----- | ----- |
std 0.682 0.182 104.381 0.720 129.034 1.536 19,013.508 8.601 3.794
min −16.681 −2.109 0.002 −0.192 −6824.769 −0.786 −203.866 −181.728 −112.889
25% −0.046 0.026 1.339 0.219 0.061 0.038 −0.014 −0.266 −0.077
| 50% | 0.145 0.106 | 4.532  | 0.577 | 0.192 | 0.176 | 0.257 | 0.143 | 0.013 |
| --- | ----------- | ------ | ----- | ----- | ----- | ----- | ----- | ----- |
| 75% | 0.341 0.222 | 13.310 | 1.001 | 0.463 | 0.429 | 0.671 | 1.505 | 0.124 |
max 0.982 0.842 4133.761 7.780 230.176 68.611 1,039,154.000 190.281 125.772
| Testset | X1 X3     | X4   | X5   | OM   | GA   | GS   | CROE | CPB  |
| ------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| count   | 1240 1240 | 1240 | 1240 | 1240 | 1240 | 1240 | 1240 | 1240 |
mean 0.224 0.192 1407.757 0.805 0.463 0.581 0.970 −0.771 −0.111
std 0.365 0.187 18,561.378 0.787 4.646 1.882 11.161 4.969 4.079
min −3.494 −0.781 0.001 −0.579 −18.486 −0.637 −27.413 −99.452 −129.227

Mathematics2025,13,368
18of29
Table3.Cont.
| TrainingSet | X1 X3       | X4     | X5    | OM    | GA    | GS    | CROE   | CPB    |
| ----------- | ----------- | ------ | ----- | ----- | ----- | ----- | ------ | ------ |
| 25%         | 0.057 0.061 | 3.283  | 0.271 | 0.123 | 0.174 | 0.162 | −1.218 | −0.143 |
| 50%         | 0.232 0.179 | 7.290  | 0.633 | 0.286 | 0.366 | 0.479 | −0.173 | −0.013 |
| 75%         | 0.402 0.313 | 16.479 | 1.132 | 0.622 | 0.612 | 0.828 | 0.425  | 0.083  |
max 1.000 0.838 387,142.019 7.467 159.588 44.695 385.756 32.016 47.076
Table 4 presents skewness and kurtosis values for variables in both the training
andtestsets. Skewnessmeasuresasymmetry,withvaluesnearzeroindicatingsymmetric
distributions.Manyvariables,especiallyinthetrainingset(e.g.,X1:−10.814,OM:−50.328),
showhighpositiveornegativeskewness,indicatingsignificantasymmetry.
Table4.SkewnessandKurtosisvaluesforvariablesintotaldatasets.
|     |     |      |             | Skewness |         |             | Kurtosis |          |
| --- | --- | ---- | ----------- | -------- | ------- | ----------- | -------- | -------- |
|     |     |      | TrainingSet |          | TestSet | TrainingSet |          | TestSet  |
|     |     | X1   | −10.814     |          | −2.181  | 199.295     |          | 17.969   |
|     |     | X3   | −1.193      |          | −0.008  | 15.695      |          | 0.939    |
|     |     | X4   | 25.938      |          | 17.379  | 897.031     |          | 319.686  |
|     |     | X5   | 2.584       |          | 2.417   | 12.077      |          | 10.372   |
|     |     | OM   | −50.328     |          | 32.369  | 2629.754    |          | 1113.145 |
|     |     | GA   | 32.133      |          | 19.269  | 1337.749    |          | 426.320  |
|     |     | GS   | 54.653      |          | 33.171  | 2986.988    |          | 1142.797 |
|     |     | CROE | 1.569       |          | −7.078  | 172.100     |          | 136.141  |
|     |     | CPB  | 5.855       |          | −24.427 | 725.704     |          | 826.716  |
Kurtosis measures the “tailedness” of the distribution. High values, such as GS
(2986.988inthetrainingset),suggestextremeoutliers. Thetestsetgenerallyshowslower
kurtosis,indicatingmoremoderateoutlierscomparedtothetrainingset.
Table5showsthecorrelationmatrixamongfeaturesforboththetrainingandtestsets.
Table5.Correlationmatrixamongfeaturesinthetrainingandtestdatasets.
| TrainingSet | X1 X3       | X4     | X5     | OM    | GA     | GS     | CROE   | CPB   |
| ----------- | ----------- | ------ | ------ | ----- | ------ | ------ | ------ | ----- |
| X1          | 1.000 0.529 | 0.103  | 0.097  | 0.255 | 0.040  | −0.004 | −0.173 | 0.008 |
| X3          | 0.529 1.000 | 0.130  | 0.281  | 0.173 | 0.075  | −0.015 | −0.139 | 0.016 |
| X4          | 0.103 0.130 | 1.000  | −0.032 | 0.005 | 0.025  | −0.003 | 0.201  | 0.002 |
|             |             | −0.032 |        |       | −0.018 | −0.016 |        |       |
| X5          | 0.097 0.281 |        | 1.000  | 0.022 |        |        | 0.003  | 0.008 |
−0.013
| OM  | 0.255 0.173 | 0.005 | 0.022  | 1.000 | 0.013 | 0.000 |        | 0.001 |
| --- | ----------- | ----- | ------ | ----- | ----- | ----- | ------ | ----- |
| GA  | 0.040 0.075 | 0.025 | −0.018 | 0.013 | 1.000 | 0.003 | −0.242 | 0.005 |
GS −0.004 −0.015 −0.003 −0.016 0.000 0.003 1.000 −0.001 −0.003
CROE −0.173 −0.139 0.201 0.003 −0.013 −0.242 −0.001 1.000 0.001
| CPB     | 0.008 0.016 | 0.002  | 0.008 | 0.001  | 0.005  | −0.003 | 0.001  | 1.000 |
| ------- | ----------- | ------ | ----- | ------ | ------ | ------ | ------ | ----- |
| Testset | X1 X3       | X4     | X5    | OM     | GA     | GS     | CROE   | CPB   |
|         |             |        |       | −0.001 | −0.046 | −0.025 | −0.029 |       |
| X1      | 1.000 0.445 | 0.127  | 0.017 |        |        |        |        | 0.024 |
| X3      | 0.445 1.000 | −0.115 | 0.321 | 0.026  | −0.003 | 0.112  | −0.045 | 0.042 |
X4 0.127 −0.115 1.000 −0.086 0.009 −0.028 −0.016 0.012 −0.001
| X5  | 0.017 0.321 | −0.086 | 1.000 | −0.049 | −0.027 | 0.009 | 0.054 | 0.035 |
| --- | ----------- | ------ | ----- | ------ | ------ | ----- | ----- | ----- |
OM −0.001 0.026 0.009 −0.049 1.000 −0.007 −0.001 0.004 −0.008
GA −0.046 −0.003 −0.028 −0.027 −0.007 1.000 −0.001 −0.606 −0.023
GS −0.025 0.112 −0.016 0.009 −0.001 −0.001 1.000 −0.007 0.037
|      | −0.029 −0.045 |        |       |        | −0.606 | −0.007 |       |       |
| ---- | ------------- | ------ | ----- | ------ | ------ | ------ | ----- | ----- |
| CROE |               | 0.012  | 0.054 | 0.004  |        |        | 1.000 | 0.005 |
| CPB  | 0.024 0.042   | −0.001 | 0.035 | −0.008 | −0.023 | 0.037  | 0.005 | 1.000 |

Mathematics2025,13,368
19of29
5. ExperimentalDiscussion
5.1. EvaluationAmongModels
Table 6 shows the results of applying SMOTE and CorrOV-CSEn across different
machinelearningmethods. Wesummarizealltheresultshereandhighlightthebestresult
foreachaspectamongthemodelsinbold.
Table6.Performancemetricsfordifferentmachinelearningmodels.
| Model | Sensitivity | Precision | F1Score |
| ----- | ----------- | --------- | ------- |
CorrOV-CSEn
| Multi-LayerPerceptron(MLP) | 0.841 | 0.327 | 0.471 |
| -------------------------- | ----- | ----- | ----- |
| RandomForest               | 0.886 | 0.375 | 0.527 |
| GradientBoosting           | 0.795 | 0.443 | 0.569 |
| XGBoost                    | 0.795 | 0.393 | 0.526 |
| AdaBoost                   | 0.750 | 0.478 | 0.584 |
| CatBoost                   | 0.909 | 0.201 | 0.329 |
SMOTE
| Multi-LayerPerceptron(MLP) | 0.841 | 0.327 | 0.471 |
| -------------------------- | ----- | ----- | ----- |
| RandomForest               | 0.795 | 0.603 | 0.686 |
| GradientBoosting           | 0.727 | 0.603 | 0.660 |
| XGBoost                    | 0.772 | 0.554 | 0.645 |
| AdaBoost                   | 0.568 | 0.555 | 0.561 |
| CatBoost                   | 0.750 | 0.717 | 0.733 |
The performance evaluation of the Multi-Layer Perceptron (MLP), random forest,
gradientboosting,XGBoost,AdaBoost,andCatBoostmodelsrevealssignificantdifferences
intheirclassificationaccuracy. classification accuracy.
  CCoorrrrOOVV--CCSSEEnn RReessuullttss::
  • Multi-LayerPerceptron(MLP)showsgoodsensitivity(0.84). However,itstruggles
withprecision(0.33),meaningarelativelysmallproportionofthepredictedfailure
casesareactualfailures. ThisimbalanceresultsinamoderateF1scoreof0.47.
• Randomforestdemonstratesstrongsensitivity(0.89),meaningiteffectivelydetects
failure cases. However, it struggles with precision (0.38), indicating that only a
relativelysmallportionofthefirmspredictedasfailuresareactuallyfailures. This
resultsinamoderateF1scoreof(0.53). Ontheotherhand,whenusingSMOTE,it
records(0.80)forsensitivityandlosesmuchofitssuccessrateforidentifyingdefault
firms. However,precisiongotbetter((0.60)and(0.69)).
• Gradientboostingoffersbalancedperformance,withasensitivityof(0.80)andhigher
precision(0.44),resultinginanF1scoreof(0.57).Thisindicatesbetteroverallhandling
ofbothfalsepositivesandfalsenegatives.
• XGBoostperformssimilarlytogradientboosting,withthesamesensitivity(0.80)but
slightlylowerprecision(0.39),resultinginanF1scoreof(0.53). Whilestillrobust,itis
slightlyoutperformedbygradientboostingintermsofprecision.
• AdaBoosthasthelowestsensitivity(0.75)butthehighestprecision(0.48),resultingin
acompetitiveF1scoreof(0.58). Thisindicatesthatwhileitsfailurepredictionsare
moreaccurate,itmissessomefailurecases.
• CatBoostexhibitsthehighestsensitivity(0.91)butstrugglesthemostwithprecision
(0.20), leadingtotheweakestF1score(0.33). ThissuggeststhatwhileCatBoostis
highlyeffectiveatdetectingfailures,whichisourprimaryobjective,itproducesmore
cflaalssseifipcoastiitoivne asc.curacy.
  CSoMrrOOTVE-CRSesEunl tRs:esults:
  • Multi-LayerPerceptron(MLP)maintainsasimilarperformancepattern. Sensitivity
remainshighat0.84,effectivelycapturingfailurecases,whileprecisionstaysrelatively
lowat0.33,indicatingthatmanypredictedfailurecaseswerenotactualfailures.

Mathematics2025,13,368 20of29
• Random forest sensitivity drops to 0.80 while precision improves to 0.60, leading
to an F1 score of 0.69. However, the sensitivity reduction indicates some missed
failurecases.
• Gradientboostingshowslowersensitivity(0.73)withaslightprecisionincrease(0.60),
resultinginanF1scoreof0.66,suggestingamodesttrade-off.
• XGBoostseesaminordecreaseinsensitivity(0.77)andanincreaseinprecision(0.55),
withanF1scoreof0.65.
• AdaBoostunderSMOTEshowsasignificantdropinsensitivity(0.57)withminimal
gaininprecision(0.56),reducingitsF1scoreto0.56.
• CatBoostimprovesprecision(0.72)butitssensitivityremainslowerthanCorrOV-CSEn,
withanF1scoreof0.73,showingmorebalancedresultsbutstilllowersensitivity.
ThesefindingsrevealthatCatBoostreachedthehighestsensitivity,whichisfollowed
byrandomforest,Multi-LayerPerceptron(MLP),gradientboosting,XGBoost,andAd-
aBoost. On the other hand, CatBoost and random forest, despite their high sensitivity,
achieverelativelypoorprecisionandoveralleffectiveness.
WhentheSMOTEmethodisused,XGBoostrecordsthehighestsensitivity,followed
byrandomforest,gradientboosting,CatBoost,andAdaBoost. Meanwhile,CatBoosthas
thebestprecisionandF1score.
CatBoostemergesasthestrongestmodelintermsofsensitivitywhencombinedwith
CorrOV-CSEn. ThisisprimarilyduetothefeaturesofCorrOV-CSEn,wheretheaugmented
dataaregeneratedbasedoncorrelations,leadingtolessnoisydatabeingfedintothemodel.
Additionally,theminorityclassreceivesmoreweightautomatically,whichisessentialin
imbalanceddatasets. CatBoost,beinghighlyadaptabletoweighteddata,caneffectively
handletheimbalanceandemphasizetheminorityclass.
Furthermore,CatBoostusesagradientboostingframeworkwithdecisiontrees,lever-
agingthepowerfulcombinationofcategoricalfeatureprocessingandboostingtohandle
theweightdistributionsmoreefficiently. Forrecallspecifically,CorrOV-CSEngenerates
datathatclarifiestheboundarybetweenclasses, reducingoverlapandthusimproving
recall. This characteristic is particularly beneficial for models like CatBoost, which are
well-equippedtolearnfromcomplexrelationshipsinthedata,includingthosebetween
featuresthataremorestronglycorrelatedwithdefaultcases.
5.2. SignificanceDifferences
For a more detailed comparison of our models, we divided the dataset into four
subsets. Theperformanceacrossthesesubsetsrevealsnotablevariations,highlightingthe
models’differingstrengthsandweaknessesinhandlingimbalanceddata. Table7describes
theperformanceofmachinelearningmodelsacrossfourdatasets.
CatBoostachieveshighsensitivity,particularlyinDataset-I(1.00)andDataset-IV(1.00).
ItalsoperformsreasonablywellinDataset-II(0.86)andDataset-III(0.89),indicatingits
effectivenessinidentifyingpositivecases. GradientboostingandXGBoostdemonstratethe
highestandmostconsistentsensitivityacrossalldatasets,bothachievingperfectsensitivity
(1.00)inDataset-IandDataset-IV.However,theyexperiencemoderatedropsinDataset-II
(0.57and0.71,respectively)andDataset-III(0.56and0.67,respectively). Randomforest
showsvariedsensitivity,excellinginDataset-I(0.95)andDataset-IV(0.88)butdropping
significantlyinDataset-II(0.71)andDataset-III(0.67). TheperformanceofMulti-Layer
Perceptron (MLP), similar to random forest, varies significantly, ranging from 0.84 in
Dataset-II to 0.67 in Dataset-IV. AdaBoost struggles more with sensitivity, particularly
inDataset-II(0.43)andDataset-III(0.56),thoughitperformswellinDataset-I(0.80)and
Dataset-IV(0.88).

Mathematics2025,13,368
21of29
Table7.Performancecomparisonofmachinelearningmodelsacrossfourdatasets.
|     | Dataset-I |     |     |     | Dataset-II |     |
| --- | --------- | --- | --- | --- | ---------- | --- |
Model Sensitivity Precision F1Score Sensitivity Precision F1Score
Multi-LayerPerceptron(MLP) 0.693 0.455 0.550 0.844 0.371 0.516
| RandomForest     | 0.950       | 0.593 | 0.731 | 0.714 | 0.192      | 0.303 |
| ---------------- | ----------- | ----- | ----- | ----- | ---------- | ----- |
| GradientBoosting | 1.000       | 0.666 | 0.800 | 0.571 | 0.500      | 0.533 |
| XGBoost          | 1.000       | 0.606 | 0.755 | 0.714 | 0.385      | 0.500 |
| AdaBoost         | 0.800       | 0.640 | 0.711 | 0.429 | 0.429      | 0.429 |
| CatBoost         | 1.000       | 0.339 | 0.506 | 0.857 | 0.188      | 0.308 |
|                  | Dataset-III |       |       |       | Dataset-IV |       |
Model Sensitivity Precision F1Score Sensitivity Precision F1Score
Multi-LayerPerceptron(MLP) 0.773 0.370 0.500 0.670 0.451 0.540
| RandomForest | 0.666 | 0.240 | 0.353 | 0.875 | 0.368 | 0.519 |
| ------------ | ----- | ----- | ----- | ----- | ----- | ----- |
Gradient
|     | 0.556 | 0.227 | 0.323 | 1.000 | 0.444 | 0.615 |
| --- | ----- | ----- | ----- | ----- | ----- | ----- |
Boosting
| XGBoost  | 0.667 | 0.300 | 0.414 | 1.000 | 0.333 | 0.500 |
| -------- | ----- | ----- | ----- | ----- | ----- | ----- |
| AdaBoost | 0.556 | 0.313 | 0.4   | 0.875 | 0.389 | 0.538 |
| CatBoost | 0.889 | 0.138 | 0.239 | 1.000 | 0.116 | 0.208 |
Gradientboostingdeliverssolidprecisionacrossalldatasets,particularlyinDataset-I
(0.67)andDataset-IV(0.44). XGBoostalsoperformswellintermsofprecision,especiallyin
Dataset-I(0.61),butsuffersslightlyinDataset-II(0.38)andDataset-IV(0.33),indicatinga
highernumberoffalsepositivesinthesedatasets. Multi-LayerPerceptron(MLP)achieves
amorestableperformance,withscoresrangingfrom(0.37)to(0.45)acrossthefourdatasets.
Randomforestshowsawiderangeofprecision,performingstronglyinDataset-I(0.59)but
strugglingsignificantlyinDataset-II(0.19),Dataset-III(0.24),andDataset-IV(0.37). This
suggeststhatwhilerandomforestcapturespositivecaseswell,itispronetomisclassifying
negativecasesaspositive. CatBoostexhibitstheweakestprecisionacrossalldatasets,with
valuesof(0.34)inDataset-I,(0.19)inDataset-II,(0.14)inDataset-III,and(0.12)inDataset-IV,
indicating consistent difficulty in accurately classifying failure cases and a higher rate
of false positives. AdaBoost generally maintains moderate precision, performing best
inDataset-I(0.64)butfallingto(0.43)inDataset-II,withconsistentbutlowerresultsin
Dataset-IIIandDataset-IV.
GradientboostingachievesthehighestandmostconsistentF1scores,particularlyin
Dataset-I(0.80)andDataset-IV(0.62). XGBoostalsoperformswell,especiallyinDataset-I
(0.75), with solid F1 scores in Dataset-III (0.41) and Dataset-IV (0.50). However, its F1
score drops slightly in Dataset-II (0.50). Random forest delivers strong performance in
Dataset-I(0.73)andDataset-IV(0.52),butitslowerF1scoresinDataset-II(0.30)andDataset-
III (0.35) highlight its susceptibility to imbalanced class distributions, especially where
precision is low. The Multi-Layer Perceptron (MLP) achieves stable performance, with
scoresconsistentlyaround(0.50). AdaBoostperformsmoderatelywell,withpeakF1scores
inDataset-I(0.71)andDataset-IV(0.54),butfaceschallengesinDataset-II(0.43)andDataset-
III(0.40). Despiteitshighsensitivity,CatBoostsuffersthemostintermsofF1scoredueto
poorprecision,whichmayneedtuningforscenarioswhereprecisionismorecritical. ItsF1
scoresare(0.51)inDataset-I,(0.31)inDataset-II,and(0.21)inDataset-IV.
We also used the Friedman–Nemenyi test to detect significant differences among
the models. Table 8 shows the results of the Friedman–Nemenyi test for each of the
threescores.

Mathematics2025,13,368
22of29
Table8.Friedmantestresultsforcomparisonsamongmachinelearningmodels.
Precision
| FriedmanTestStatistic | 12.00   |     |     |     |     |     |
| --------------------- | ------- | --- | --- | --- | --- | --- |
| p-value               | 0.03479 |     |     |     |     |     |
Multi-Layer
|     | RandomForest |     | GradientBoosting | XGBoost | AdaBoost | CatBoost |
| --- | ------------ | --- | ---------------- | ------- | -------- | -------- |
Perceptron(MLP)
| RandomForest | -   | 0.854075 | 0.635776 | 0.900000 | 0.635776 | 0.744925 |
| ------------ | --- | -------- | -------- | -------- | -------- | -------- |
Multi-LayerPerceptron(MLP) 0.854075 - 0.900000 0.900000 0.900000 0.136905
GradientBoosting 0.635776 0.900000 - 0.900000 0.900000 0.052161
| XGBoost  | 0.900000 | 0.900000 | 0.900000 | -        | 0.900000 | 0.410222 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| AdaBoost | 0.635776 | 0.900000 | 0.900000 | 0.900000 | -        | 0.052161 |
| CatBoost | 0.744925 | 0.136905 | 0.052161 | 0.410222 | 0.052161 | -        |
Sensitivity
| FriedmanTestStatistic | 10.04 |     |     |     |     |     |
| --------------------- | ----- | --- | --- | --- | --- | --- |
p-value1
0.07413
NosignificantdifferencewasfoundbytheFriedmantestbecausethep-valueisgreaterthanthesignificancelevelof0.05.
F1Score
| FriedmanTestStatistic | 10.43   |     |     |     |     |     |
| --------------------- | ------- | --- | --- | --- | --- | --- |
| p-value2              | 0.06396 |     |     |     |     |     |
1,2NosignificantdifferencewasfoundbytheFriedmantestbecausethep-valueisgreaterthanthesignificance
levelof0.05.
Sincethep-valueislessthan0.05,theFriedmantestindicatesasignificantdifference
insensitivityandprecisionacrossthemodels:
• AdaBoost vs. CatBoost: This is the only comparison with a significant difference
(p-value=0.030),showingthatCatBoostperformssignificantlybetterthanAdaBoost
intermsofsensitivity.
•
Gradient boosting vs. CatBoost, AdaBoost vs. CatBoost, and MLP vs. CatBoost:
Allcomparisonsshowsignificantdifferenceswithp-valuesof0.030,indicatingthat
CatBoosthassignificantlylowerprecisioncomparedtogradientboosting,AdaBoost,
andMLP.
Allothercomparisonshavep-valuesabove0.05,indicatingnosignificantdifferences
insensitivityandprecisionbetweenthesemodels.
5.3. FeatureImportance
Inthefinalstage,wepresenttheimportanceofourfeaturesetacrossthemodelsused.
Figure3illustratesthefeatureimportanceinourmodels. ItisclearthatX1hasthehighest
importanceinallmodelsexpectMLP.Thiscontrastswithothercreditriskstudiesusingthe
samefeaturesetintheIraniancapitalmarket[64].

Mathematics 2025, 13, x FOR PEER REVIEW  22 of 29

Since the p-value is less than 0.05, the Friedman test indicates a significant difference
in sensitivity and precision across the models:
•
AdaBoost vs. CatBoost: This is the only comparison with a significant difference (p-
value = 0.030), showing that CatBoost performs significantly better than AdaBoost in
terms of sensitivity.
•  Gradient boosting vs. CatBoost, AdaBoost vs. CatBoost, and MLP vs. CatBoost: All
comparisons show significant differences with p-values of 0.030, indicating that Cat-
Boost has significantly lower precision compared to gradient boosting, AdaBoost,
and MLP.
All other comparisons have p-values above 0.05, indicating no significant differences
in sensitivity and precision between these models.
5.3. Feature Importance
In the final stage, we present the importance of our feature set across the models
used. Figure 3 illustrates the feature importance in our models. It is clear that X1 has the
Mathematics2025,13,368 highest importance in all models expect MLP. This contrasts with other credit r2i3skof s2t9udies
using the same feature set in the Iranian capital market [64].
|      | RandomForest |     |      |     | XGBoost  |     |     |
| ---- | ------------ | --- | ---- | --- | -------- | --- | --- |
| CPB  |              |     | CPB  |     |          |     |     |
| CROE |              |     | CROE |     |          |     |     |
| GS   |              |     |      | GS  |          |     |     |
| GA   |              |     |      | GA  |          |     |     |
| OM   |              |     |      | OM  |          |     |     |
| X5   |              |     |      | X5  |          |     |     |
| X4   |              |     |      | X4  |          |     |     |
| X3   |              |     |      | X3  |          |     |     |
| X1   |              |     |      | X1  |          |     |     |
| 0    | 0.1          | 0.2 | 0.3  | 0   | 0.1      | 0.2 | 0.3 |

|      | AdaBoost   |     |      |     | CatBoost    |     |     |
| ---- | ---------- | --- | ---- | --- | ----------- | --- | --- |
| CPB  |            |     | CPB  |     |             |     |     |
| CROE |            |     | CROE |     |             |     |     |
| GS   |            |     |      | GS  |             |     |     |
| GA   |            |     |      | GA  |             |     |     |
| OM   |            |     |      | OM  |             |     |     |
| X5   |            |     |      | X5  |             |     |     |
| X4   |            |     |      | X4  |             |     |     |
| X3   |            |     |      | X3  |             |     |     |
| X1   |            |     |      | X1  |             |     |     |
Mathematics 2025, 13, x FOR PEER REVIEW  23 of 29

| 0                | 0.05 0.1 | 0.15 | 0.2  | 0   | 10  | 20  | 30  |
| ---------------- | -------- | ---- | ---- | --- | --- | --- | --- |
|                  |          |      |      |     |     |     |     |
| GradientBoosting |          |      |      |     | MLP |     |     |
| CPB              |          |      | CPB  |     |     |     |     |
| CROE             |          |      | CROE |     |     |     |     |
| GS               |          |      |      | GS  |     |     |     |
| GA               |          |      |      | GA  |     |     |     |

| OM  |         |     | OM  |     |          |      |     |
| --- | ------- | --- | --- | --- | -------- | ---- | --- |
| X5  |         |     |     | X5  |          |      |     |
| X4  |         |     |     | X4  |          |      |     |
| X3  |         |     |     | X3  |          |      |     |
| X1  |         |     |     | X1  |          |      |     |
| 0   | 0.2 0.4 | 0.6 | 0.8 | 0   | 0.05 0.1 | 0.15 | 0.2 |
|     |         |     |     |     |          |      |     |
Figure3.Featureimportanceinourmachinelearningmodels.
Figure 3. Feature importance in our machine learning models.
6. Conclusions
In this study, we employed recently introduced cost-sensitive methods to predict
business failures in the Iranian capital market using five decision tree-based algorithms in
addition to MPL. Our findings demonstrate that all models achieved improved sensitivity
scores through this approach, with CatBoost outperforming the others.
While CatBoost showed clear superiority, there remains a tradeoff between extend-
ing credit to a broader range of customers to maximize revenue and minimizing the risk
of default. Future research could focus on developing models that optimize creditor prof-
its by balancing revenue generation with risk management rather than solely assessing
default risk.
Additionally, other decision tree-based methods, such as Mondrian Forest, could be
explored in this context. In addition to the models evaluated in this study, it is important
to consider the role of hyperparameter optimization in improving model performance.
While our current work focuses on assessing the effectiveness of various decision tree-
based models, incorporating optimization techniques such as grid search or Bayesian op-
timization could lead to even better-performing models.
From a data perspective, incorporating new types of data, including sentiment anal-
ysis, textual data, and political indices, could significantly enhance model performance.
This is especially relevant in countries like Iran, where political and economic conditions
play a crucial role in credit risk management.
Our research focused on the Iran capital market, and due to the unique economic and
political challenges facing the Iranian capital market, these findings might not exactly ap-
ply to other industries or nations, although many developing countries face similar chal-
lenges, like extensive governmental administration, challenges related to market effi-
ciency, and regulatory frameworks and political instability. It is recommended to consider
actual default instead of failure under Article 141 of the Amended Commercial Code.
Further, it is important to notice that the data analysis results may be affected by the
global economic meltdown caused by the pandemic during the window period. There-
fore, in the upcoming research, it is potential to conduct a sensitivity analysis to compare
the results with the exclusion of the COVID-19 period.
Lastly, there is considerable potential in applying these methods to emerging fields,
such as peer-to-peer (P2P) lending platforms, which have been growing rapidly in Iran in
recent years.

Mathematics2025,13,368 24of29
6. Conclusions
In this study, we employed recently introduced cost-sensitive methods to predict
businessfailuresintheIraniancapitalmarketusingfivedecisiontree-basedalgorithmsin
additiontoMPL.Ourfindingsdemonstratethatallmodelsachievedimprovedsensitivity
scoresthroughthisapproach,withCatBoostoutperformingtheothers.
WhileCatBoostshowedclearsuperiority,thereremainsatradeoffbetweenextending
credit to a broader range of customers to maximize revenue and minimizing the risk
of default. Future research could focus on developing models that optimize creditor
profitsbybalancingrevenuegenerationwithriskmanagementratherthansolelyassessing
defaultrisk.
Additionally,otherdecisiontree-basedmethods,suchasMondrianForest,couldbe
exploredinthiscontext. Inadditiontothemodelsevaluatedinthisstudy,itisimportant
to consider the role of hyperparameter optimization in improving model performance.
While our current work focuses on assessing the effectiveness of various decision tree-
based models, incorporating optimization techniques such as grid search or Bayesian
optimizationcouldleadtoevenbetter-performingmodels.
Fromadataperspective,incorporatingnewtypesofdata,includingsentimentanalysis,
textualdata,andpoliticalindices,couldsignificantlyenhancemodelperformance. Thisis
especiallyrelevantincountrieslikeIran,wherepoliticalandeconomicconditionsplaya
crucialroleincreditriskmanagement.
OurresearchfocusedontheIrancapitalmarket,andduetotheuniqueeconomicand
politicalchallengesfacingtheIraniancapitalmarket,thesefindingsmightnotexactlyapply
tootherindustriesornations,althoughmanydevelopingcountriesfacesimilarchallenges,
likeextensivegovernmentaladministration,challengesrelatedtomarketefficiency,and
regulatory frameworks and political instability. It is recommended to consider actual
defaultinsteadoffailureunderArticle141oftheAmendedCommercialCode.
Further,itisimportanttonoticethatthedataanalysisresultsmaybeaffectedbythe
globaleconomicmeltdowncausedbythepandemicduringthewindowperiod. Therefore,
intheupcomingresearch,itispotentialtoconductasensitivityanalysistocomparethe
resultswiththeexclusionoftheCOVID-19period.
Lastly,thereisconsiderablepotentialinapplyingthesemethodstoemergingfields,
suchaspeer-to-peer(P2P)lendingplatforms,whichhavebeengrowingrapidlyinIranin
recentyears.
AuthorContributions:Conceptualization,P.P.,M.P.F.,C.T.,M.S.andH.K.;methodology,P.P.,M.P.F.,
C.T.,M.S.andH.K.;software,P.P.andH.K.;validation,P.P.,M.P.F.,C.T.andH.K.;formalanalysis,P.P.,
C.T.,M.S.andH.K.;investigation,P.P.,M.P.F.,C.T.andM.S.;resources,P.P.,M.P.F.,C.T.andM.S.;data
curation,M.P.F.,M.S.andH.K.;writing—originaldraftpreparation,P.P.andH.K.;writing—review
andediting,P.P.,M.P.F.,C.T.,M.S.andH.K.;visualization,P.P.,M.S.andH.K.;supervision,P.P.,M.P.F.,
C.T.andM.S.;projectadministration,P.P.,C.T.andM.P.F.Allauthorshavereadandagreedtothe
publishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Dataarecontainedwithinthearticle.
Acknowledgments:Theauthorswouldliketothanktheanonymousreviewersandtheeditor-in-chief
fortheirconstructivecommentsandsuggestions.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.

Mathematics2025,13,368 25of29
References
1. Usmani,S.; Shamsi,J.A.LSTMbasedstockpredictionusingweightedandcategorizedfinancialnews. PLoSONE2023,18,
e0282234.[CrossRef][PubMed]
2. Zhang,Z.;Liu,X.;Niu,H.FinancialcrisisearlywarningofChineselistedcompaniesbasedonMD&Atext-linguisticfeature
indicators.PLoSONE2023,18,e0291818.[CrossRef]
3. Jezeie,F.V.;Sadjadi,S.J.;Makui,A.Constrainedportfoliooptimizationwithdiscretevariables:Analgorithmicmethodbasedon
dynamicprogramming.PLoSONE2022,17,e0271811.[CrossRef][PubMed]
4. Bi,W.;Zhang,Q.Forecastingmergersandacquisitionsfailurebasedonpartial-sigmoidneuralnetworkandfeatureselec-tion.
PLoSONE2021,16,e0259575.[CrossRef]
5. Li,M.FinancialinvestmentriskpredictionundertheapplicationofinformationinteractionFireflyAlgorithmcombinedwith
GraphConvolutionalNetwork.PLoSONE2023,18,e0291510.[CrossRef]
6. Dahal,K.R.;Pokhrel,N.R.;Gaire,S.;Mahatara,S.;Joshi,R.P.;Gupta,A.;Banjade,H.R.;Joshi,J.Acomparativestudyoneffectof
newssentimentonstockpricepredictionwithdeeplearningarchitecture.PLoSONE2023,18,e0284695.[CrossRef][PubMed]
7. Javid,I.;Ghazali,R.;Syed,I.;Zulqarnain,M.;Husaini,N.A.StudyonthePakistanstockmarketusinganewstockcrisisprediction
method.PLoSONE2022,17,e0275022.[CrossRef]
8. Cui, Y.; Liu, L.Investorsentiment-awarepredictionmodelforP2PlendingindicatorsbasedonLSTM.PLoSONE2022, 17,
e0262539.[CrossRef]
9. Zhu,C.;Liu,X.;Chen,D.Predictionofdigitaltransformationofmanufacturingindustrybasedoninterpretablemachinelearning.
PLoSONE2024,19,e0299147.[CrossRef][PubMed]
10. Khan,A.H.;Shah,A.;Ali,A.;Shahid,R.;Zahid,Z.U.;Sharif,M.U.;Jan,T.;Zafar,M.H.Aperformancecomparisonofmachine
learningmodelsforstockmarketpredictionwithnovelinvestmentstrategy.PLoSONE2023,18,e0286362.[CrossRef][PubMed]
11. Wei,X.;Ouyang,H.;Liu,M.StockindextrendpredictionbasedonTabNetfeatureselectionandlongshort-termmemory.PLoS
ONE2022,17,e0269195.[CrossRef][PubMed]
12. Tran,T.;Nguyen,N.H.;Le,B.T.;Vu,N.T.;Vo,D.H.ExaminingfinancialdistressoftheVietnameselistedfirmsusingaccounting-
basedmodels.PLoSONE2023,18,e0284451.[CrossRef][PubMed]
13. Laghari,F.;Ahmed,F.;LópezGarcía,M.D.L.N.Cashflowmanagementanditseffectonfirmperformance:Empiricalev-idence
onnon-financialfirmsofChina.PLoSONE2023,18,e0287135.[CrossRef][PubMed]
14. Almustafa,H.;Nguyen,Q.K.;Liu,J.;Dang,V.C.TheimpactofCOVID-19onfirmriskandperformanceinMENAcountries:
Doesnationalgovernancequalitymatter?PLoSONE2023,18,e0281148.[CrossRef][PubMed]
15. Tian,X.;Wang,Y.;Kohar,U.H.A.Capitalstructure,businessmodelinnovation,andfirmperformance:EvidencefromChinese
listedcorporatebasedonsystemGMMmodel.PLoSONE2024,19,e0306054.[CrossRef]
16. Samour,A.;AlGhazali,A.;Gadoiu,M.;Banuta,M.CapitalstructureandfinancialperformanceofChina’senergyindustry:What
canweinferfromCOVID-19?PLoSONE2024,19,e0300936.
17. Berloco,C.;Morales,G.D.F.;Frassineti,D.;Greco,G.;Kumarasinghe,H.;Lamieri,M.;Massaro,E.;Miola,A.;Yang,S.Predicting
corporatecreditrisk:Networkcontagionviatradecredit.PLoSONE2021,16,e0250115.[CrossRef][PubMed]
18. Hlongwane, R.; Ramaboa, K.K.K.M.; Mongwe, W. Enhancing credit scoring accuracy with a comprehensive evaluation of
alternativedata.PLoSONE2024,19,e0303566.[CrossRef][PubMed]
19. Ma,Z.;Hou,W.;Zhang,D.AcreditriskassessmentmodelofborrowersinP2PlendingbasedonBPneuralnetwork.PLoSONE
2021,16,e0255216.[CrossRef][PubMed]
20. Wang,H.;Liu,X.Undersamplingbankruptcyprediction:Taiwanbankruptcydata.PLoSONE2021,16,e0254030.[CrossRef]
[PubMed]
21. Japkowicz,N.Learningfromimbalanceddatasets: Acomparisonofvariousstrategies. InAAAIWorkshoponLearningfrom
ImbalancedDataSets;AAAIPress:MenloPark,CA,USA,2000.
22. Groccia,M.C.;Guido,R.;Conforti,D.;Pelaia,C.;Armentaro,G.;Toscani,A.F.;Miceli,S.;Succurro,E.;Hribal,M.L.;Sciacqua,A.
Cost-SensitiveModelstoPredictRiskofCardiovascularEventsinPatientswithChronicHeartFailure.Information2023,14,542.
[CrossRef]
23. Natha,P.;RajaRajeswari,P.AdvancingSkinCancerPredictionUsingEnsembleModels.Computers2024,13,157.[CrossRef]
24. Devi,D.;Biswas,S.K.;Purkayastha,B.Correlation-basedOversamplingaidedCostSensitiveEnsemblelearningtechniquefor
TreatmentofClassImbalance.J.Exp.Theor.Artif.Intell.2022,34,143–174.[CrossRef]
25. Alloway,B.T.;Weisenthal,J.What’sBeenHappeningwiththeIranianStockMarket;Bloomberg:NewYork,NY,USA,2023.
26. Rawat, S.S.; Mishra, A.K. Review of Methods for Handling Class-Imbalanced in Classification Problems. arXiv 2022,
arXiv:2211.05456.
27. Tomek,I.TwoModificationsofCNN.IEEETrans.Syst.ManCybern.1976,11,769–772.
28. Kubat,M.;Matwin,S.Addressingthecurseofimbalanceddatasets: One-sidedsampling. InProceedingsoftheFourteenth
InternationalConferenceonMachineLearning,Nashville,TN,USA,8–12July1997.

Mathematics2025,13,368 26of29
29. Japkowicz,N.Theclassimbalanceproblem: Significanceandstrategies. InProceedingsoftheInternationalConferenceon
ArtificialIntelligence,LasVegas,NV,USA,26–29June2000.
30. Laurikkala,J.Improvingidentificationofdifficultsmallclassesbybalancingclassdistribution.InProceedingsoftheArtificial
IntelligenceinMedicine:8thConferenceonArtificialIntelligenceinMedicineinEurope,AIME2001,Cascais,Portugal,1–4July
2001;Proceedings8.Springer:Berlin/Heidelberg,Germany,2001.
31. Hoyos-Osorio,J.;Alvarez-Meza,A.;Daza-Santacoloma,G.;Orozco-Gutierrez,A.;Castellanos-Dominguez,G.Relevantinforma-
tionundersamplingtosupportimbalanceddataclassification.Neurocomputing2021,436,136–146.[CrossRef]
32. Lee,W.;Seo,K.DownsamplingforBinaryClassificationwithaHighlyImbalancedDatasetUsingActiveLearning.BigDataRes.
2022,28,100314.[CrossRef]
33. Laveti,R.N.;Mane,A.A.;Pal,S.N.DynamicStackedEnsemblewithEntropybasedUndersamplingfortheDetectionofFraudulent
Transactions.InProceedingsofthe20216thInternationalConferenceforConvergenceinTechnology(I2CT),Maharashtra,India,
2–4April2021;pp.1–7.
34. Solberg, A.S.; Solberg, R. A large-scale evaluation of features for automatic detection of oil spills in ERS SAR images. In
ProceedingsoftheIGARSS’96.1996InternationalGeoscienceandRemoteSensingSymposium,Lincoln,NB,USA,21–26May
1996;pp.1484–1486.
35. Mathew,J.;Pang,C.K.;Luo,M.;Leong,W.H.ClassificationofImbalancedDatabyOversamplinginKernelSpaceofSupport
VectorMachines.IEEETrans.NeuralNetworksLearn.Syst.2017,29,4065–4076.[CrossRef][PubMed]
36. Bennin, K.E.; Keung, J.; Phannachitta, P.; Monden, A.; Mensah, S.MAHAKIL:DiversityBasedOversamplingApproachto
AlleviatetheClassImbalanceIssueinSoftwareDefectPrediction.IEEETrans.Softw.Eng.2017,44,534–550.[CrossRef]
37. Cheng, K.; Zhang, C.; Yu, H.; Yang, X.; Zou, H.; Gao, S.GroupedSMOTEWithNoiseFilteringMechanismforClassifying
ImbalancedData.IEEEAccess2019,7,170668–170681.[CrossRef]
38. Tarawneh,A.S.;Hassanat,A.B.A.;Almohammadi,K.;Chetverikov,D.;Bellinger,C.SMOTEFUNA:SyntheticMinorityOver-
SamplingTechniqueBasedonFurthestNeighbourAlgorithm.IEEEAccess2020,8,59069–59082.[CrossRef]
39. Almomani,I.;Qaddoura,R.;Habib,M.;Alsoghyer,S.;AlKhayer,A.;Aljarah,I.;Faris,H.Androidransomwaredetectionbased
onahybridevolutionaryapproachinthecontextofhighlyim-balanceddata.IEEEAccess2021,9,57674–57691.[CrossRef]
40. Juez-Gil,M.;Arnaiz-González,Á.;Rodríguez,J.J.;López-Nozal,C.;García-Osorio,C.Approx-SMOTE:FastSMOTEforBigData
onApacheSpark.Neurocomputing2021,464,432–437.[CrossRef]
41. Chawla,N.V.;Bowyer,K.W.;Hall,L.O.;Kegelmeyer,W.P.SMOTE:SyntheticMinorityOver-samplingTechnique.J.Artif.Intell.
Res.2002,16,321–357.[CrossRef]
42. Li,C.DataMiningforDirectMarketing:ProblemsandSolutions;NationalLibraryofCanada=BibliothèquenationaleduCanada:
Ottawa,ON,Canada,2000.
43. Xu,Z.;Shen,D.;Nie,T.;Kou,Y.AhybridsamplingalgorithmcombiningM-SMOTEandENNbasedonRandomforestfor
medicalimbalanceddata.J.Biomed.Informatics2020,107,103465.[CrossRef]
44. Dong;Xiao,H.;Dong,Y.SA-CGAN:AnoversamplingmethodbasedonsingleattributeguidedconditionalGANformulti-class
imbalancedlearning.Neurocomputing2022,472,326–337.[CrossRef]
45. Sharma,A.;Singh,P.K.;Chandra,R.SMOTified-GANforClassImbalancedPatternClassificationProblems.IEEEAccess2022,10,
30655–30665.[CrossRef]
46. Puri,A.;Gupta,M.K.ImprovedHybridBag-BoostEnsembleWithK-Means-SMOTE–ENNTechniqueforHandlingNoisyClass
ImbalancedData.Comput.J.2021,65,124–138.[CrossRef]
47. Seiffert,C.;Khoshgoftaar,T.M.;VanHulse,J.;Napolitano,A.RUSBoost:AHybridApproachtoAlleviatingClassImbalance.
IEEETrans.Syst.ManCybern.PartASyst.Hum.2009,40,185–197.[CrossRef]
48. Czarnowski,I.WeightedEnsemblewithone-classClassificationandOver-samplingandInstanceselection(WECOI):Anapproach
forlearningfromimbalanceddatastreams.J.Comput.Sci.2022,61,101614.[CrossRef]
49. Wang,H.;Xu,Q.;Zhou,L.LargeUnbalancedCreditScoringUsingLasso-LogisticRegressionEnsemble. PLoSONE2015,10,
e0117844.[CrossRef][PubMed]
50. Ariza-Garzón,M.-J.;Arroyo,J.;Segovia-Vargas,M.-J.;Caparrini,A.Profit-sensitivemachinelearningclassificationwithex-
planationsincreditrisk: Thecaseofsmallbusinessesinpeer-to-peerlending. Electron. Commer. Res. Appl. 2024,67,101428.
[CrossRef]
51. Turney,P.D.Cost-SensitiveClassification:EmpiricalEvaluationofaHybridGeneticDecisionTreeInductionAlgorithm.J.Artif.
Intell.Res.1994,2,369–409.[CrossRef]
52. Ling,C.X.;Yang,Q.;Wang,J.;Zhang,S.Decisiontreeswithminimalcosts. InProceedingsoftheTwenty-FirstInternational
ConferenceonMachineLearning,Banff,AB,Canada,4–8July2004.
53. Drummond,C.;Holte,R.C.Exploitingthecost(in)sensitivityofdecisiontreesplittingcriteria.InProceedingsoftheInternational
ConferenceonMachineLearning,Stanford,CA,USA,29June29–2July2000.

Mathematics2025,13,368 27of29
54. Domingos, P.Metacost: Ageneralmethodformakingclassifierscost-sensitive. InProceedingsoftheFifthACMSIGKDD
InternationalConferenceonKnowledgeDiscoveryandDataMining,SanDiego,CA,USA,15–18August1999.
55. Witten,I.H.;Frank,E.Datamining:PracticalmachinelearningtoolsandtechniqueswithJavaimplementations.AcmSigmodRec.
2002,31,76–77.[CrossRef]
56. Chai, X.; Deng, L.; Yang, Q.; Ling, C.X. Test-cost sensitive naive bayes classification. In Proceedings of the Fourth IEEE
InternationalConferenceonDataMining(ICDM’04),Brighton,UK,1–4November2004;IEEE:Piscataway,NJ,USA.
57. Sheng,V.S.;Ling,C.X.Thresholdingformakingclassifierscost-sensitive.InProceedingsoftheAssociationfortheAdvancement
ofArtificialIntelligence,Boston,MA,USA,16–20July2006.
58. Khan,S.H.;Hayat,M.;Bennamoun,M.;Sohel,F.A.;Togneri,R.Cost-SensitiveLearningofDeepFeatureRepresentationsFrom
ImbalancedData.IEEETrans.NeuralNetw.Learn.Syst.2017,29,3573–3587.[CrossRef][PubMed]
59. Lu,H.;Xu,Y.;Ye,M.;Yan,K.;Gao,Z.;Jin,Q.Learningmisclassificationcostsforimbalancedclassificationongeneexpression
data.BMCBioinform.2019,20,1–10.[CrossRef][PubMed]
60. Feng,F.; Li,K.C.; Shen,J.; Zhou,Q.; Yang,X.Usingcost-sensitivelearningandfeatureselectionalgorithmstoimprovethe
performanceofimbalancedclas-sification.IEEEAccess2020,8,69979–69996.[CrossRef]
61. Khandani,A.E.;Kim,A.J.;Lo,A.W.Consumercredit-riskmodelsviamachine-learningalgorithms. J.Bank. Financ. 2010,34,
2767–2787.[CrossRef]
62. Barboza,F.;Kimura,H.;Altman,E.Machinelearningmodelsandbankruptcyprediction.ExpertSyst.Appl.2017,83,405–417.
[CrossRef]
63. Yıldırım,M.;Okay,F.Y.;Özdemir,S.Bigdataanalyticsfordefaultpredictionusinggraphtheory.ExpertSyst.Appl.2021,176,
114840.[CrossRef]
64. Peykani,P.;Sargolzaei,M.;Sanadgol,N.;Takaloo,A.;Kamyabfar,H.Theapplicationofstructuralandmachinelearningmodels
topredictthedefaultriskoflistedcompaniesintheIraniancapitalmarket.PLoSONE2023,18,e0292081.[CrossRef][PubMed]
65. Chen, N.; Ribeiro, B. A consensus approach for combining multiple classifiers in cost-sensitive bankruptcy prediction. In
ProceedingsoftheAdaptiveandNaturalComputingAlgorithms:11thInternationalConference,ICANNGA2013,Lausanne,
Switzerland,4–6April2013;Proceedings11.Springer:Berlin/Heidelberg,Germany,2013.
66. Bahnsen,A.C.;Aouada,D.;Ottersten,B.Example-dependentcost-sensitivedecisiontrees.ExpertSyst.Appl.2015,42,6609–6619.
[CrossRef]
67. Zakaryazad,A.;Duman,E.Aprofit-drivenArtificialNeuralNetwork(ANN)withapplicationstofrauddetectionanddirect
marketing.Neurocomputing2016,175,121–131.[CrossRef]
68. Xia,Y.;Liu,C.;Liu,N.Cost-sensitiveboostedtreeforloanevaluationinpeer-to-peerlending.Electron.Commer.Res.Appl.2017,
24,30–49.[CrossRef]
69. Fiore,U.;DeSantis,A.;Perla,F.;Zanetti,P.;Palmieri,F.Usinggenerativeadversarialnetworksforimprovingclassification
effectivenessincreditcardfrauddetection.Inf.Sci.2017,479,448–455.[CrossRef]
70. Papouskova,M.;Hajek,P.Two-stageconsumercreditriskmodellingusingheterogeneousensemblelearning.Decis.SupportSyst.
2019,118,33–45.[CrossRef]
71. DeBock,K.W.;Coussement,K.;Lessmann,S.Cost-sensitivebusinessfailurepredictionwhenmisclassificationcostsareuncertain:
Aheterogeneousensembleselectionapproach.Eur.J.Oper.Res.2020,285,612–630.[CrossRef]
72. Hou,W.-H.;Wang,X.-K.;Zhang,H.-Y.;Wang,J.-Q.;Li,L.Anoveldynamicensembleselectionclassifierforanimbalanceddata
set:Anapplicationforcreditriskassessment.Knowl.-BasedSyst.2020,208,106462.[CrossRef]
73. Li,Z.;Zhang,J.;Yao,X.;Kou,G.Howtoidentifyearlydefaultsinonlinelending:Acost-sensitivemulti-layerlearningframework.
Knowl.-BasedSyst.2021,221,106963.[CrossRef]
74. Barbaglia,L.;Manzan,S.;Tosetti,E.ForecastingLoanDefaultinEuropewithMachineLearning.J.Financ.Econ.2021,21,569–596.
[CrossRef]
75. Gramegna,A.;Giudici,P.SHAPandLIME:AnEvaluationofDiscriminativePowerinCreditRisk.Front.Artif.Intell.2021,4,
752558.[CrossRef]
76. Zou,Y.;Gao,C.;Gao,H.BusinessFailurePredictionBasedonaCost-SensitiveExtremeGradientBoostingMachine.IEEEAccess
2022,10,42623–42639.[CrossRef]
77. Xing,J.;Chi,G.;Pan,A.Instance-dependentmisclassificationcost-sensitivelearningfordefaultprediction.Res.Int.Bus.Financ.
2024,69,102265.[CrossRef]
78. Wang,S.;Chi,G.Cost-sensitivestackingensemblelearningforcompanyfinancialdistressprediction.ExpertSyst.Appl.2024,255,
124525.[CrossRef]
79. CorreaBahnsen, A.; Aouada, D.; Ottersten, B.EnsembleofExample-DependentCost-SensitiveDecisionTrees. arXiv2015,
arXiv:1505.04637.
80. Pandove,D.;Rani,R.;Goel,S.Localgraphbasedcorrelationclustering.Knowl.-BasedSyst.2017,138,155–175.[CrossRef]

Mathematics2025,13,368 28of29
81. Freund,Y.;Schapire,R.E.ADecision-TheoreticGeneralizationofOn-LineLearningandanApplicationtoBoosting.J.Comput.
Syst.Sci.1997,55,119–139.[CrossRef]
82. Breiman,L.RandomForests.Mach.Learn.2001,45,5–32.[CrossRef]
83. Friedman,J.H.Greedyfunctionapproximation:Agradientboostingmachine.Ann.Stat.2001,29,1189–1232.[CrossRef]
84. Chen,T.; Guestrin,C.XGBoost: AScalableTreeBoostingSystem. InProceedingsofthe22ndACMSIGKDDInternational
ConferenceonKnowledgeDiscoveryandDataMining,SanFrancisco,CA,USA,13–17August2016;AssociationforComputing
Machinery:SanFrancisco,Ca,USA;pp.785–794.
85. Prokhorenkova,L.;Gusev,G.;Vorobev,A.;Dorogush,A.V.;Gulin,A.CatBoost:Unbiasedboostingwithcategoricalfeatures.In
Proceedingsofthe32ndInternationalCon-ferenceonNeuralInformationProcessingSystems,Montréal,Canada,3–8December
2018;CurranAssociatesInc.:Montréal,QC,Canada;pp.6639–6649.
86. Rumelhart,D.E.;Hinton,G.E.;Williams,R.J.Learningrepresentationsbyback-propagatingerrors.Nature1986,323,533–536.
[CrossRef]
87. Kumar,V.;Kedam,N.;Sharma,K.V.;Mehta,D.J.;Caloiero,T.AdvancedMachineLearningTechniquestoImproveHydrological
Prediction:AComparativeAnalysisofStreamflowPredictionModels.Water2023,15,2572.[CrossRef]
88. Charoenwong, B.; Reddy, P. Using forensic analytics and machine learning to detect bribe payments in regime-switching
environments:EvidencefromtheIndiademonetization.PLoSONE2022,17,e0268965.[CrossRef][PubMed]
89. Nandi,A.K.;Randhawa,K.K.;Chua,H.S.;Seera,M.;Lim,C.P.Creditcardfrauddetectionusingahierarchicalbehavior-knowledge
spacemodel.PLoSONE2022,17,e0260579.[CrossRef][PubMed]
90. Carbo-Valverde, S.; Cuadros-Solas, P.; Rodríguez-Fernández, F. A machine learning approach to the digitalization of bank
customers:Evidencefromrandomandcausalforests.PLoSONE2020,15,e0240362.[CrossRef]
91. Hlongwane,R.;Ramabao,K.;Mongwe,W.Anovelframeworkforenhancingtransparencyincreditscoring:LeveragingShapley
valuesforinterpretablecreditscorecards.PLoSONE2024,19,e0308718.[CrossRef]
92. Quach,A.C.AExtensionsandImprovementstoRandomForestsforClassification;UtahStateUniversity:Logan,Utah,2017.
93. Wyrobek,J.;Kluza,K.EfficiencyofGradientBoostingDecisionTreesTechniqueinPolishCompanies’BankruptcyPrediction.
In Proceedings of the Information Systems Architecture and Technology: Proceedings of 39th International Conference on
InformationSystemsArchitectureandTechnology–ISAT2018:PartIII,Wrocław,Poland,16–18September2019;pp.24–35.
94. Freund,Y.BoostingaWeakLearningAlgorithmbyMajority.Inf.Comput.1995,121,256–285.[CrossRef]
95. Breiman,L.Baggingpredictors.Mach.Learn.1996,24,123–140.[CrossRef]
96. Lu,M.;Hou,Q.;Qin,S.;Zhou,L.;Hua,D.;Wang,X.;Cheng,L.AStackingEnsembleModelofVariousMachineLearningModels
forDailyRunoffForecasting.Water2023,15,1265.[CrossRef]
97. Ainan, U.H.; Por, L.Y.; Chen, Y.-L.; Yang, J.; Ku, C.S. Advancing Bankruptcy Forecasting with Hybrid Machine Learning
Techniques:InsightsfromanUnbalancedPolishDataset.IEEEAccess2024,12,1.[CrossRef]
98. Aiken,J.M.;DeBin,R.;Hjorth-Jensen,M.;Caballero,M.D.PredictingtimetograduationatalargeenrollmentAmericanuniversity.
PLoSONE2020,15,e0242334.[CrossRef][PubMed]
99. Du, H.; Lv, L.; Wang, H.; Guo, A.Anovelmethodfordetectingcreditcardfraudproblems. PLoSONE2024, 19, e0294537.
[CrossRef]
100. Jabeur,S.B.;Gharib,C.;Mefteh-Wali,S.;Arfi,W.B.CatBoostmodelandartificialintelligencetechniquesforcorporatefailure
prediction.Technol.Fore-Cast.Soc.Chang.2021,166,120658.[CrossRef]
101. Dorogush,A.V.;Ershov,V.;Gulin,A.CatBoost:Gradientboostingwithcategoricalfeaturessupport.arXiv2018,arXiv:1810.11363.
102. Lu,H.;Hu,X.EnhancingFinancialRiskPredictionforListedCompanies:ACatboost-BasedEnsembleLearningApproach.J.
Knowl.Econ.2023,15,1–17.[CrossRef]
103. Enkhtuya,T.;Kang,D.K.BankruptcyPredictionwithExplainableArtificialIntelligenceforEarly-StageBusinessModels.Int.J.
InternetBroadcast.Commun.2023,15,58–65.
104. Peykani,P.;Sargolzaei,M.;Botshekan,M.H.;Oprean-Stan,C.;Takaloo,A.OptimizationofAssetandLiabilityManagementof
BankswithMinimumPossibleChanges.Mathematics2023,11,2761.[CrossRef]
105. Peykani,P.;Sargolzaei,M.;Takaloo,A.;Sanadgol,N.Investigatingthemonetarypolicyriskchannelbasedonthedynamic
stochasticgeneralequilibriummodel:EmpiricalevidencefromIran.PLoSONE2023,18,e0291934.[CrossRef][PubMed]
106. Marino,M.J.Chapter3—StatisticalAnalysisinPreclinicalBiomedicalResearch.InResearchintheBiomedicalSciences;Williams,M.,
Curtis,M.J.,Mullane,K.,Eds.;AcademicPress:Cambridge,MA,USA,2018;pp.107–144.
107. Riffenburgh,R.H.ChapterSummaries.InStatisticsinMedicine,2nded.;Riffenburgh,R.H.,Ed.;AcademicPress:Burlington,MA,
USA,2006;pp.533–580.
108. Friedman,M.TheUseofRankstoAvoidtheAssumptionofNormalityImplicitintheAnalysisofVariance.J.Am.Stat.Assoc.
1937,32,675–701.[CrossRef]
109. Hull,J.MachineLearninginBusiness:AnIntroductiontotheWorldofDataScience;AmazonDistribution:London,UK,2020.

Mathematics2025,13,368 29of29
110. Altman,E.I.Financialratios,discriminantanalysisandthepredictionofcorporatebankruptcy. J.Financ. 1968,23,589–609.
[CrossRef]
111. Carton,R.B.;Hofer,C.W.MeasuringOrganizationalPerformance:MetricsforEntrepreneurshipandStrategicManagementResearch;
EdwardElgarPublishing:Cheltenham,UK,2006.
112. Peykani,P.;Sargolzaei,M.;Takaloo,A.;Valizadeh,S.TheEffectsofMonetaryPolicyonMacroeconomicVariablesthroughCredit
andBalanceSheetChannels:ADynamicStochasticGeneralEquilibriumApproach.Sustainability2023,15,4409.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.