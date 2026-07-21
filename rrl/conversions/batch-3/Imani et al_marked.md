---
conversion_metadata:
  converted_at: "2026-07-21T06:38:24Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Imani et al.pdf"
  source_pdf_sha256: "d589704ce61f2c3c6d92954fa606b0136a57f557d3cc99b5363b1d1ae423777e"
  page_count: 38
  markdown_char_count: 129436
---

SystematicReview
Customer Churn Prediction: A Systematic Review of Recent
Advances, Trends, and Challenges in Machine Learning and
Deep Learning
MehdiImani1,* ,MajidJoudaki2 ,AliBeikmohammadi1,* andHamidRezaArabnia3
1 DepartmentofComputerandSystemSciences,StockholmUniversity,SE-16455Stockholm,Sweden
2 DepartmentofComputerEngineering,FacultyofEngineering,AyatollahBoroujerdiUniversity,
Boroujerd69199-69737,Iran;m.joudaki@abru.ac.ir
3 SchoolofComputing,UniversityofGeorgia,Athens,GA30602,USA;hra@uga.edu
* Correspondence:m.imani@gmail.com(M.I.);beikmohammadi@dsv.su.se(A.B.)
Abstract
Background: Customerchurnsignificantlyimpactsbusinessrevenues. MachineLearning
(ML)andDeepLearning(DL)methodsareincreasinglyadoptedtopredictchurn,yeta
systematicsynthesisofrecentadvancementsislacking. Objectives: Thissystematicreview
evaluatesMLandDLapproachesforchurnprediction,identifyingtrends,challenges,and
research gaps from 2020 to 2024. Data Sources: Six databases (Springer, IEEE, Elsevier,
MDPI,ACM,Wiley)weresearchedviaLens.orgforstudiespublishedbetweenJanuary
2020 and December 2024. Study Eligibility Criteria: Peer-reviewed original studies ap-
plyingML/DLtechniquesforchurnpredictionwereincluded. Reviews,preprints,and
non-peer-reviewed works were excluded. Methods: Screening followed PRISMA 2020
guidelines. Atwo-phasestrategyidentified240studiesforbibliometricanalysisand61
fordetailedqualitativesynthesis. Results: Ensemblemethods(e.g.,XGBoost,LightGBM)
remaindominantinML,whileDLapproaches(e.g.,LSTM,CNN)areincreasinglyapplied
tocomplexdata. Challengesincludeclassimbalance,interpretability,conceptdrift,andlim-
AcademicEditors:OliverHinzand iteduseofprofit-orientedmetrics.ExplainableAIandadaptivelearningshowpotentialbut
AndreasHolzinger limitedreal-worldadoption. Limitations: Noformalriskofbiasorcertaintyassessments
Received:9July2025 wereconducted. Studyheterogeneitypreventedmeta-analysis. Conclusions: MLandDL
Revised:10September2025 methodshavematuredaskeytoolsforchurnprediction,yetgapsremainininterpretability,
Accepted:19September2025 real-worlddeployment,andbusiness-alignedevaluation. SystematicReviewRegistration:
Published:21September2025
RegisteredretrospectivelyinOSF.
Citation: Imani,M.;Joudaki,M.;
Beikmohammadi,A.;Arabnia,H.R. Keywords:customerchurnprediction;customerretention;deeplearning;literaturereview;
CustomerChurnPrediction:A
machinelearning
SystematicReviewofRecent
Advances,Trends,andChallengesin
MachineLearningandDeepLearning.
Mach.Learn.Knowl.Extr.2025,7,105.
1. Introduction
https://doi.org/10.3390/
make7030105 Customerretentionhasbecomeacriticalchallengeforbusinessesacrossvariousindus-
Copyright:©2025bytheauthors. tries,includingtelecommunications,retail,banking,insurance,healthcare,education,and
LicenseeMDPI,Basel,Switzerland. subscription-basedservices. Customerchurn—customersdiscontinuingtheirrelationship
Thisarticleisanopenaccessarticle withacompany—cansignificantlyimpactrevenues,withannualchurnratesrangingfrom
distributedunderthetermsand
20%to40%insomesectors[1]. Researchindicatesthatacquiringanewcustomerisfiveto
conditionsoftheCreativeCommons
twenty-fivetimesmoreexpensivethanretaininganexistingone,makingchurnprevention
Attribution(CCBY)license
astrategicpriorityforcompanies[2].
(https://creativecommons.org/
licenses/by/4.0/).
Mach.Learn.Knowl.Extr.2025,7,105 https://doi.org/10.3390/make7030105

Mach.Learn.Knowl.Extr.2025,7,105 2of38
Machine Learning and Deep Learning have emerged as powerful tools for churn
predictionduetotheirabilitytoanalyzelarge,high-dimensional,anddynamiccustomer
datasetseffectively. Traditionalchurnpredictionmethods,suchasrule-basedsystemsand
statisticalmodeling,oftenfailtocapturecustomerbehaviour’scomplexitiesadequately.
Conversely,MLapproacheslikeDecisionTrees(DTs),RandomForests(RFs),SupportVector
Machines (SVMs), and boosting algorithms (e.g., XGBoost, LightGBM, CatBoost) have
demonstratedstrongpredictivecapabilitieswithstructureddatasets[3–5]. Furthermore,
advancedDLarchitectures—includingArtificialNeuralNetworks(ANNs),Convolutional
NeuralNetworks(CNNs),LongShort-TermMemorynetworks(LSTMs),andTransformer-
basedmodels—providesignificantadvantagesformodelingsequentialandunstructured
data,suchascustomerinteractionhistoriesandtextualfeedback.
Despitethesetechnologicaladvancements,severalcriticalchallengesremaininchurn
prediction. Modelinterpretabilityremainsasignificantconcern,especiallywithcomplex
DL-based approaches often functioning as “black-box” models [6]. Data imbalance is
anotherprevalentissue,aschurndatasetstypicallyfeaturesignificantlyfewerchurners
thannon-churners,potentiallybiasingmodelpredictions[5]. Additionally,conceptdrift—
theevolvingnatureofcustomerbehaviourovertime—complicatesthesustainedaccuracy
ofpredictivemodels.
Thisliteraturereviewsystematicallyexploresadvancementsincustomerchurnpre-
diction by analyzing peer-reviewed research published between 2020 and 2024 across
diversedomainssuchastelecommunications,retail,banking,healthcare,education,and
insurance. ItaimstomapthecurrentlandscapeofMLandDLapproaches, evaluating
their strengths, limitations, and applicability to real-world scenarios. Given the broad
adoptionofpredictiveanalyticsacrossindustries,thisreviewseekstoclarifytheevolution
of these methodologies, the specific challenges they address, and the gaps that require
furtherresearch.
Akeyobjectiveofthisstudyistoidentifyandcategorizethemostfrequentlyemployed
MLandDLtechniquesusedinchurnprediction. Understandingtheevolutionofthese
methodsoverrecentyearsprovidesinsightsintohowbusinessesandresearchershavere-
finedapproachestoenhanceaccuracyandadaptability. Additionally,thisreviewevaluates
theperformanceandinterpretabilityofvariouspredictivemodels,focusingspecificallyon
theircapacitytomanageimbalanceddatasets,dynamiccustomerbehaviours,andpractical
deploymentconstraints. Consideringthatcustomerchurnresultsfrommultiplefactors—
suchastransactionhistories,engagementpatterns,andexternalmarketconditions—itis
crucialtoassesstheeffectivenessofmodelsincapturingthesecomplexities.
Anothercentralgoalishighlightingpersistentchallengesandlimitationswithinchurn
predictionresearch. Despitesubstantialprogress,issuessuchastheblack-boxnatureofDL
models,classimbalance,anddifficultyadaptingmodelstoevolvingcustomerbehaviours
impede real-world implementations. This review emphasizes these research gaps and
suggestspotentialareasforfutureinvestigation,includingimprovingmodeltransparency,
advancingfeatureengineeringtechniques,anddevelopingadaptivelearningmethodsto
addressshiftingcustomerpreferences.
Whilethisreviewsynthesizesabroadbodyofrecentliteratureoncustomerchurn
prediction,weintentionallyrefrainfrompresentingadirectcomparisonoftheirreported
performancemetrics(e.g.,accuracy,F1-score,AUC).Thisdecisionisbasedonthesubstan-
tialheterogeneityobservedacrossthestudiesregardingdatasetcharacteristics,imbalance
ratios,featuresets,modelingobjectives,andevaluationprotocols.
Specifically, models were trained and validated on various public and proprietary
datasetsdrawnfromdiverseindustries(e.g.,telecommunications,banking,e-commerce),
oftenwithdistinctdefinitionsofchurn,timewindows,andinputmodalities. Evaluation

Mach.Learn.Knowl.Extr.2025,7,105 3of38
metricsalsovariedwidely,withsomestudiesprioritisingbusiness-orientedoutcomesand
othersfocusingonstatisticalmeasures. Assuch,anyattempttoaggregateorcomparethese
resultsdirectlywouldriskintroducingmisleadinginterpretationsandovergeneralizations.
Instead,thisreviewfocusesonidentifyingmethodologicaltrends,thetaxonomyof
modeling strategies, and common challenges and innovations. Where appropriate, we
highlight representative studies that exemplify key methodological advances without
assertingquantitativesuperiority. Weencouragefuturebenchmarkstudiesusingstandard-
izeddatasetsandexperimentalprotocolstoconductrigorousperformancecomparisons,
ideallyincorporatingstatisticalsignificancetestingundercontrolledconditions.
Toaddresstheseobjectives,thisstudyisguidedbythreefundamentalresearchques-
tions:
RQ1: What are the predominant ML and DL approaches used in customer churn
prediction,andhowhavethesemethodologiesevolvedovertime?
RQ2: Howdodifferentpredictivemodelscompareaccuracy,adaptability,andinter-
pretabilitywhenappliedtochurnpredictionacrossvariousindustries?
RQ3: What are the significant challenges and limitations in existing churn predic-
tionresearch,andwhatfuturedirectionscanbeexploredtoenhancetheeffectivenessof
predictivemodels?
Thisreviewsynthesizescurrentresearchtoinformbothacademicandindustryprac-
tices. Thiswork’sspecificcontributionsandnovelaspectsareoutlinedinthefollowing
subsection.
ContributionsandNovelty
Thisstudyoffersseveraldistinctcontributionsthatdifferentiateitfrompriorreviews
oncustomerchurnprediction:
1. Most Recent and Comprehensive Scope: We systematically review peer-reviewed
researchpublishedbetweenJanuary2020andDecember2024,encompassingrecent
advancessuchasCNN-basedarchitectures,hybriddeeplearningframeworks,and
profit-drivenmodellingapproaches. Earlierreviewspredominantlyfocusonpre-2020
literatureandthereforedonotcapturetheseemergingtrends.
2. PRISMA-GuidedandReproducibleMethodology: Oursearchandselectionstrategy
adherestothePRISMA2020guidelines,ensuringmethodologicaltransparencyand
reproducibility.Weemployatwo-phasereviewprocess,aninitialbibliometricanalysis
of240studiesfollowedbyanin-depthsynthesisof61keypapers. Whereasexisting
reviewsoftenlacksuchastructuredandreplicableapproach.
3. NovelHierarchicalTaxonomy:Weintroduceanewhierarchicaltaxonomythatcatego-
rizesMLandDLapproachesintofine-grainedsubgroups(e.g.,profit-centricmodels,
optimization/metaheuristics,adaptivelearning,explainableAI).Thistaxonomypro-
videsasystematicframeworkformappingthemethodologicallandscape,afeature
absentinearlierworks.
4. IntegrationofBibliometricandMethodologicalInsights: Inadditiontomethodolog-
ical synthesis, we conduct a comprehensive bibliometric analysis, including pub-
lishertrends,citationdynamics,andopen-accesseffects,tocontextualizetheresearch
landscape. Previous reviews focus exclusively on models and do not incorporate
dissemination-orientedanalyses.
5. Identification of Emerging Challenges Supported by Evidence-Based Trends: We
identifychallengessuchasclassimbalance,conceptdrift,andthelimitedadoptionof
business-orientedevaluationmetrics,linkingthemtorepresentativestudiespublished
between2020and2024. Thisevidence-drivenmappingoftrendsprovidesamore

Mach.Learn.Knowl.Extr.2025,7,105 4of38
preciseandup-to-dateperspectivethanthegenericlimitationsdiscussedinearlier
surveys.
Byclearlydelineatingthesecontributions,thisreviewmakesitsnoveltyandvalue
explicit,offeringactionableinsightsforacademicresearchersandindustrypractitioners
engagedincustomerretentionanalytics.
2. PurposeoftheStudy
CustomerchurnpredictionisvitalinmodernCustomerRelationshipManagement
(CRM),helpingbusinessesproactivelyretainat-riskcustomersandmaximizecustomer
lifetime value. With high churn rates leading to substantial revenue losses, businesses
in subscription-based services, telecommunications [1,7], retail [8], banking [9], educa-
tion[10],healthcare[11],Insurance[12],andothersectorsincreasinglyrelyondata-driven
approachestoenhancecustomerretentionstrategies.
Whilebusinessescollectvastamountsofcustomerdata,extractingactionableinsights
fromthesedatasetsischallenging. Datamining,akeydisciplineinMLandartificialintelli-
gence,enablesorganizationstouncoverhiddenpatternsandtrendsinchurnbehaviours.
However,theeffectivenessofchurnpredictionmodelsvariessignificantlybasedonthe
choiceofmethodology,datasetcharacteristics,andindustry-specificfactors.
Thisstudysystematicallyreviews240researcharticlespublishedbetween2020and
2024,focusingonchurnpredictionusingMLandDLmethodologiesacrossvarioussectors.
Thereview:
• Examinesdifferentchurnpredictionapproachesacrossmultipleindustries.
• AssessesthecomparativeperformanceofMLandDLtechniquesinchurnprediction.
• Investigates common challenges, such as data imbalance, feature selection, inter-
pretability,andconceptdrift.
• Highlightsemergingtrendsinchurnprediction,includingprofit-drivenmodeling,
explainableAI(XAI),andadaptivelearningapproaches.
Churn prediction research is crucial for developing effective retention strategies,
allowingbusinessestoanticipatecustomerattrition,personalizemarketingefforts,and
allocateretentionbudgetsmoreefficiently. Studiessuggestthatbusinessesimplementing
advancedchurnpredictiontechniquescanimproveretentionratesby5–10%,leadingto
profitincreasesof25–95%[13].
Bysynthesizinginsightsfromrecentresearch,thispaperservesasavaluableresource
forresearchers,datascientists,andindustrypractitioners,helpingthemunderstandbest
practices,methodologicaladvancements,andfuturedirectionsinchurnprediction.
Formoreinformation,readerscanrefertoseveralcomprehensivereviewpapersthat
explorevariousaspectsofcustomerchurnprediction.ImaniandArabnia[3]provideacom-
parativeanalysisofhyperparameteroptimizationtechniquesanddatasamplingstrategies
inMLmodelsforchurnprediction,highlightingtheirimpactonpredictiveperformance.
Theauthorsin[5]extendthisanalysisbyevaluatingtheeffectivenessofSMOTE,ADASYN,
andGNUSupsamplingtechniquesinconjunctionwithRFandXGBoostunderdifferent
classimbalancelevels. Geileretal.[14]offerabroadsurveyofMLapproachesforchurn
prediction,discussingtheirstrengths,limitations,andpracticalapplications. Domingos
etal.[15]focusonhyperparametertuningforDL-basedchurnpredictionmodels,particu-
larlywithinthebankingsector,providinginsightsintooptimizingdeepneuralnetworks
for improved accuracy. These studies offer valuable perspectives on churn prediction
research’smethodologicaladvancementsandchallenges.

Mach.Learn.Knowl.Extr.2025,7,105 5of38
3. SearchStrategies
Asystematicliteraturesearchwasconductedacrosssixmajoracademicpublishers,
includingSpringer,IEEE,Elsevier,MDPI,ACM,andWiley,ensuringcomprehensivecover-
ageofrecentadvancementsincustomerchurnpredictionusingMLandDLtechniques.
ThesearchwasexecutedviaLens.org, ascholarlyresearchplatformofferingadvanced
filteringandindexingcapabilitiessuperiortogenericsearchengineslikeGoogleScholar.
Torefinethesearch,thequery“(churnpredictionANDmachinelearning)OR(churn
predictionANDdeeplearning)NOT(“survey”OR“review”)”wasapplied,focusingon
originalresearchcontributionsratherthansurveyorreviewarticles. Additionally,results
wererestrictedtojournalandconferenceproceedingsarticlespublishedbetween2020and
2024,ensuringrelevancetorecentdevelopments. TheKStem-basedstemmingapproach
wasutilizedtonormalizevariationsoftheterm“churn,”suchas“churned”and“churning,”
tocaptureabroaderrangeofrelevantstudies.Thefinalsearchwasconductedon15January
2025. VisualizationsandplotswereproducedusingPython3.13,employingthematplotlib
andseabornlibrariestoensureclarityandreproducibilityofgraphicalresults.
AsillustratedinFigure1,theinitialsearchretrieved837articles. Toensurerelevance
andquality,aseriesofrefinementstepswasapplied. First,filteringbydocumenttypetoin-
cludeonlyjournalandconferencearticleswhileexcludingpre-prints,technicalreports,and
othernon-peer-revieweddocumentsreducedthecountto679articles. Next,restrictingthe
selectiontohigh-qualitypublishers—aspreviouslyoutlined—furtherrefinedthedatasetto
368articles. Finally,adomain-specificreviewwasconductedtoeliminatepapersunrelated
tocustomerchurnpredictionorthosenotutilizingMLandDLtechniques. Thisresultedin
afinalselectionof240articlesforthefirstphase(shallowreviewphase). Thisexploratory
phaseanalyzedbroadresearchtrends,methodologicalpatterns,andkeydevelopmentsin
customerchurnpredictionusingMLandDLapproaches. Thisphasefocusedonhigh-level
bibliometricanalysis,includingpublicationtrendsacrossresearchdomains,thedistribu-
tionofMLandDLtechniques,theaveragecitationtrendsofpublishers(Crossrefcitation),
citationpatterns,andthepublicationssharedamongdifferentpublishersoverthepastfive
years(2020–2024). Byanalyzingthesebroadertrends,thisphaseprovidedafoundationfor
identifyingthemostinfluentialstudies,emergingresearchdirections,andmethodological
advancements.
Asecondphase(deepreviewphase)wasconductedtoensureamorefocusedand
rigorousexamination,inwhich61paperswereselectedbasedonrelevance,citationimpact,
methodologicalnovelty,andcontributiontothefield. Thisphasedelvedintothetechnical
depthoftheselectedstudies,focusingoncriticalaspectssuchasdatasetcharacteristics,
appliedMLandDLtechniques,evaluationmetrics,andthekeyoutcomesreportedinthe
studies. Byconductingthistwo-phasereviewstrategy,thestudycapturedbroadresearch
trendsandprovidedagranularunderstandingofmethodologicaladvancements,dataset
challenges,andperformancebenchmarks.Thisstructuredapproachenhancedtheliterature
review’scomprehensiveness,objectivity,anddepth,ensuringbothbreadthanddepthin
assessingthestate-of-the-artcustomerchurnpredictionresearch.
Theinclusioncriteriaareoutlinedbelow:
• ArticlesmustfocusonchurnpredictionusingMLorDLtechniques.
• Articlespublishedbetween2020and2024inpeer-reviewed,high-qualityjournals.
• Articlesmustbeoriginalresearchpapers.
• ArticlespublishedinEnglish.
Theexclusioncriteriaareoutlinedbelow:
• Articlesunrelatedtochurnprediction.
• ArticlesunrelatedtoMLorDL.

Mach.Learn.Knowl.Extr.2025,7,105 6of38
• Non-peer-reviewedworks(e.g.,lecturenotes,newsletters,dissertations).
• Low-qualitypublishers.
• Reviewpapers,preprints,books,etc.
• Non-Englishpublications.
Figure1.PRISMAFlowchart.
This systematic approach, grounded in a well-documented filtering process and
adherencetoPRISMAguidelines,ensuresthereproducibilityofthisliteraturereview. All
inclusioncriteria,searchstrings,andfilteringstepshavebeenexplicitlyoutlinedtofacilitate
replicationbyfutureresearchers.
Tworeviewers(MIandMJ)collaborativelyscreenedtitlesandabstractsforrelevance,
resolvingdisagreementsthroughdiscussion. Onereviewer(MI)extractedstudycharac-
teristics and methodological details for data collection, while the second reviewer (MJ)
cross-checkedforaccuracy. Noautomationtoolsorcontactwithstudyauthorswereused
duringtheseprocesses.
For each included study, data were extracted on the primary outcomes of interest:
ML/DL techniques employed, evaluation metrics (e.g., accuracy, F1-score, ROC-AUC,
PR-AUC),andkeyfindingsrelatedtomethodologicalchallengessuchasclassimbalance,
conceptdrift,andmodelinterpretability. Additionalvariablescollectedincludedpubli-
cationyear,applicationdomain(e.g.,telecommunications,banking,healthcare),dataset
characteristics (public, private, or synthetic), and study citation metrics. All data were
extracted as reported in the original publications; no imputation or conversions were
applied.
Studiesweregroupedforsynthesisusingatwo-phaseapproach: ashallowreview
phase (240 studies) to identify broad methodological trends and a deep review phase
(61 studies) for detailed analysis. Results were tabulated and visually displayed using
summarytablesandfigurestoillustratetrendsinML/DLtechniques,performancemetrics,

Mach.Learn.Knowl.Extr.2025,7,105 7of38
andapplicationdomains.Narrativesynthesiswasperformedtosummarizemethodological
patternsandchallenges,asameta-analysiswasnotfeasibleduetoheterogeneityinstudy
designs,datasets,andevaluationmetrics. Nosubgroupanalysesorsensitivityanalyses
wereconducted,giventhequalitativefocusofthisreview.
Wedidnotperformaformalriskofbiasassessmentorreportingbiasassessment,as
thereviewaimedtosynthesizemethodologicaltrendsratherthanevaluatethequalityof
individualstudies. Similarly,aformalcertaintyassessment(e.g.,usingGRADE)wasnot
applied. Futuresystematicreviewsconductingquantitativesynthesisormeta-analyses
shouldconsiderincorporatingtheseassessmentsusingstandardizedtoolssuchasROBIS,
AMSTAR2,orGRADE.ThissystematicreviewwasretrospectivelyregisteredintheOpen
ScienceFramework(OSF)underDOI:https://doi.org/10.17605/OSF.IO/PZ2H7.
4. TrendsinChurnPredictionResearch
Tocomprehensivelyinvestigatethestateofchurnpredictionresearch,wesystemati-
callyreviewed240publicationsspanningtheyears2020to2024. Thisfive-yearwindow
waschosentocapturecurrenttrendsandreflecttherapidadvancementsinMLandDL
applications. Thebroadscopeofthisinitialpoolenabledustoanalyzesignificanttrends
inpublisherdistribution,citationdynamics,averagecitationvariations,researchdomain
focus,andtheadoptionofvariousMLandDLtechniques. Allstudiesexcludedduring
thescreeningprocessfailedtomeetthepredefinedinclusioncriteria(e.g., theydidnot
employML/DLtechniques,didnotaddresschurnprediction,orwerenon-peer-reviewed).
Nostudiesthatinitiallyappearedtomeetinclusioncriteriawereexcludedduringfull-text
review.
Fromthismoreextensiveset,weselected61studiesfordeeperqualitativeexamination.
This subset was identified based on multiple criteria, including methodological rigor,
noveltyofapproach,domaindiversity,andoverallcontributiontothefield. Bycombining
awide-rangingquantitativeoverviewwithafocused,in-depthanalysisofkeystudies,our
methodologyensuresanexpansivemappingofchurnpredictionresearchandathorough
investigationofthemostinfluentialandinnovativework. Thisdual-levelstrategythus
providesreaderswitharobustunderstandingofcurrentpractices,emergingchallenges,
andfuturedirectionsinchurnpredictionusingMLandDLtechniques.
Figure2presentstheoveralldistributionofpublicationsbypublishers. Thepiechart
illustrates that IEEE accounts for the largest share, with 60.4% of the total publications.
SpringerandElsevierfollow,at12.9%and11.2%,respectively,whileMDPIcomprises7.1%
ofthedataset. ACMandWileycomprisetheremaining5.8%and2.5%,respectively. These
percentageshighlightthedominantpositionofIEEEamongthepublishersrepresentedin
thisstudy.
Figure 3 further explores the temporal dimension of these publications from 2020
through2024. IEEEexhibitsamarkedincreaseinpublishedpapers,peakingin2023. In
contrast, the other publishers remain relatively steady, though minor fluctuations can
beobservedfromyeartoyear. Notably,theapparentdeclineinpublicationsfor2024is
likelyattributabletoincompleteindexingduringdataextraction(January2025). Given
thatnotall2024publicationsmayhavebeenprocessedandincludedinourstudybythat
point, the downward trend for 2024 should be interpreted with caution. These figures
suggestthatIEEEconsistentlyleadsinpublicationoutput,whileotherpublishersmaintain
comparativelysmalleryetstablesharesovertheexaminedperiod.

Mach.Learn.Knowl.Extr.2025,7,105 8of38
Figure2.ShareofPublicationsbyPublishers.
Figure3.PublicationTrendsofPublishers.
Figures4and5illustratethenumberofcitationsandnormalizedimpactfactortrends
fortheselectedpublishers(Elsevier,IEEE,MDPI,Springer,Wiley,andACM)from2020to
2024. Figure4showsthatElsevierexhibitedthehighesttotalcitationsin2020,followed
byanoticeabledeclineinsubsequentyears. Otherpublishers,includingIEEEandMDPI,
displaysmallerbutstilldiscerniblepeaksinearlieryears,withatendencytowardreduced
citation counts in 2023 and 2024. These observations align with the typical pattern in
bibliometricanalyses,wherebyearlierpublicationshavealongerwindowtoaccumulate
citations.
Figure4.CitationsReceivedbyEachPublisher.

Mach.Learn.Knowl.Extr.2025,7,105 9of38
Figure5.NormalizedIFTrendsofPublishers.
Figure5illustratesthenormalizedimpactfactortrendsofthepublishersfrom2020
to 2024. To ensure a fair comparison of citation performance across publication years,
wecomputedanormalizedimpactfactor(IF)bydividingthetotalnumberofcitations
receivedbythenumberofpublishedpapersandthenumberofyearssincepublication.
Thisapproachaccountsforthevaryingtimewindowsavailableforpaperstoaccumulate
citations,thusmitigatingthebiasthatfavorsearlierpublications. Theformulausedisas
follows:
TotalCitations
Normalized IF =
Numberof Papers×YearsSincePublications
AsshowninFigure5,ElsevierandMDPIconsistentlyoutperformotherpublishersin
termsofnormalizedimpactacrossmostyears. Elsevierexhibitsstrongperformancein2020
(above10citationsperpaperperyear),dipsin2022,andthenpeaksagainin2023,suggest-
ingacombinationofhigh-impactpublicationsandefficientvisibility. MDPIdemonstrates
asteeprisein2021—reachingnearly10citationsperpaperperyear—andagradualdecline
inthefollowingyearsyetmaintainingarelativelystrongcitationperformancethrough2023.
Springershowsadownwardtrendfrom2020to2022butstabilizesaroundthreecitations
perpaperperyearby2023. Wileypeaksin2021,likeMDPI,followedbyamoderatebut
steadydecline. IEEEandACMdisplaylowerandmorestablecitationpatternsacrossthe
years,withvaluesremainingprimarilybelow2,indicatingmoreconsistentbutmodest
averagecitationrates.
Whilethenormalizedimpactfactoraccountsforthetimesincepublication,ageneral
declineisstillobservedin2024acrossmostpublishers. Thismayreflectseveralfactors,
includingrecentshiftsinpublicationstrategies,articletopics,qualitychanges,orearly-
stage visibility. Moreover, papers published in 2024 may not yet be fully indexed or
cited at the time of data extraction (January 2025), especially for journals with delayed
indexingpipelines. Assuch,citation-basedmetricsfromthemostrecentyearshouldbe
interpretedwithcaution,astheymayunderestimatetheeventuallong-termimpactofthese
publications.
Overall, the trends reveal significant year-to-year variation in normalized citation
performanceamongpublishers,underscoringtherolesofeditorialpolicy,topicalfocus,
and dissemination strategies. By adjusting for publication age, the normalized impact
factoroffersafairerandmoretime-independentcomparison,particularlywhenanalyzing
performanceacrossbothrecentandearlierpublicationyears.
Figure6illustratestheoveralldistributionofcitationcountsforthecollectedpublica-
tions,revealingahighlyskewedpattern. Mostpapersreceiveonlyafewcitations(fewer
than five), while a relatively small number of publications accumulate notably higher
citationcounts. Thisright-skeweddistributionistypicalinbibliometricanalyses,wherein

Mach.Learn.Knowl.Extr.2025,7,105 10of38
most publications garner modest attention, whereas a limited subset gains substantial
visibilityand,consequently,highercitationimpact.
Figure6.CitationCountDistribution.
Figure7presentsthenormalizedimpactfactortrends—theaveragenumberofcitations
perpaperperyear—forOpenAccess(OA)andNon-OpenAccess(non-OA)publications
from2020to2024. Acrossallyears,OApapersconsistentlyoutperformnon-OAarticlesin
termsofcitationimpact,withrobustperformancein2020and2021. Thistrendsupports
thenotionthatOApublishingmayenhancethevisibilityanddiscoverabilityofresearch,
therebyincreasingitscitationpotential. Whilethenormalizedmetricaccountsforthetime
since publication, a noticeable decline is observed for both OA and non-OA papers in
2024. Thismayreflectlimitedearly-stagevisibility,indexingdelays,orpublicationlagsthat
hindercitationaccumulation,particularlyforarticlespublishedclosetothedataextraction
date(January2025),whichmaynotyetbefullyindexedorcited,especiallyinjournalswith
slowerindexingpipelines. Assuch,thelowervaluesobservedforthemostrecentyear
shouldbeinterpretedcautiously,astheymaynotaccuratelyreflectthelong-terminfluence
ofthosepublications.
Figure7.NormalizedIFTrends:OAvs.non-OAPapers.
Figure8presentstheannualdistributionofpublicationsacrosssixresearchdomains—
Telecom,Retail,Banking,Education,Healthcare,andInsurance—from2020to2024. Across
mostdomains,theoveralltrendisgradualgrowthfrom2020through2023,followedbya
slightdeclinein2024. Telecomshowsapronouncedincreaseinpublicationsupto2023,
indicatingasustainedresearchfocusonchurnpredictionwithinthatsector.Healthcareand
Educationalsoexhibitsteadyupwardtrajectories,reflectingbroaderinterestinapplying
churn-related methodologies to patient retention and student engagement. Retail and
Bankingmaintainmoderatebutconsistentgrowth,whileInsuranceremainscomparatively

Mach.Learn.Knowl.Extr.2025,7,105 11of38
lower throughout the observed period. The apparent drop in 2024 publications for all
domains is likely influenced by the shorter window for indexing at the time of data
extraction(January2025),anditdoesnotnecessarilyindicateawaningresearchinterest.
Figure8.Publicationtrendsbyresearchdomains.
Figure9presentsthetimeseriestrendsofMLandDLtechniquesinchurnprediction
from2020to2024. MLmethodsexhibitasteadyupwardtrend,indicatingtheirwidespread
adoption. Incontrast,DLpublicationsremainrelativelylowbutshowgradualgrowth. The
apparentdeclinein2024shouldbeinterpretedcautiously,asmanypapersfromthisyear
maynotyetbefullyindexedorhavehadsufficienttimetogaincitationsandvisibility.
Figure9.Theusageofdifferentcategoriesoftechniquesinchurnpredictionresearch.
Figure10depictstheannualusageofsevenMLalgorithms—BoostingTechniques
(includingXGBoost,LightGBM,andCatBoost),K-NearestNeighbors,RF,DT,SVM,Naïve
Bayes,andLogisticRegression—between2020and2024. BoostingTechniques,RF,and
LogisticRegressionshownotablegrowththrough2022–2023,suggestingincreasedresearch
interestinensemble-basedmethodsandwidelyusedbaselinemodels. Whilemosttech-
niques experienced a slight dip in 2024, it is likely due to incomplete indexing and the
relativelyshorttimesincepublicationatthetimeofdataextraction(January2025).
Figure11focusesonDLapproaches—ANNs,LSTMs,CNNs,RecurrentNeuralNet-
works(RNNs),Transformers,andReinforcementLearning—overthesameperiod. ANNs
exhibitapronouncedsurgein2022,reflectingtheirbroadapplicabilityindiversedomains.
LSTMsandCNNsalsoshowmoderateyetconsistentusage,whileTransformersandRe-
inforcementLearningremainlessfrequentbutappeartohavegainedmodesttractionin
recentyears. LiketheMLtrends,thelowercountsfor2024likelydonotcapturethefull
extentofongoingresearchactivity,underscoringtheneedtointerprettheserecent-year
valuescautiously. Overall,thedatarevealacontinuedshifttowardadvancedMLandDL

Mach.Learn.Knowl.Extr.2025,7,105 12of38
techniques, albeit tempered by the time-dependent nature of publication and indexing
cycles.
Figure10.TheusageofdifferentconventionalMLtechniquesinchurnpredictionresearch.
Figure11.TheusageofdifferentDLtechniquesinchurnpredictionresearch.
Whiletheprimaryfocusofthisreviewisonmethodologicaladvancementsinchurn
prediction,analyzingwhereandhowresearchispublishedofferscomplementaryinsights
intothedisseminationandvisibilityofthefield. Thedistributionofpublicationsacross
major academic publishers and the temporal trends in citation activity help illustrate
the growing attention to churn prediction across domains such as telecommunications,
banking,andhealthcare. Forexample,thepredominanceofIEEEpublicationsmayreflect
historicalengagementwithmachinelearningapplicationsintelecommunicationsanda
concentrationofconference-stylecontributions. Whilecitationtrendsatthepublisherlevel
cannotbedirectlylinkedtospecificmethodsorstudies,theymaysuggestbroaderpatterns
inresearchvisibility,accessibility(e.g.,openaccessavailability),andperceivedrelevance.
Assuch,thesebibliometricobservationscontextualize,notevaluate,themethodological
developmentsreviewedinthisstudy.
5. Paper’sCategorizations
Inourreview,weproposeacomprehensivetaxonomythatsystematicallyorganizes
theliteratureonchurnpredictionintotwoprimarymethodologicalcategories: Machine
LearningApproachesandDeepLearningApproaches. Eachcategoryisfurthersubdivided
intospecificsubcategories,asillustratedinFigure12.

Mach.Learn.Knowl.Extr.2025,7,105 13of38
Figure12.TaxonomyofChurnPredictionApproaches.
TheMLApproachesencompassarangeoftechniques,includingprofit-centricmod-
els, which optimize retention strategies based on business impact, and ensemble and
hybridapproaches,whichcombinemultipleclassifierstoimprovepredictiveperformance.
Optimizationandmetaheuristicmethodsalsofocusonrefiningfeatureselectionandhyper-
parametertuning,whileadaptiveandresamplingtechniquesaddressdataimbalanceand
conceptdrift. Thereviewalsocoversexplainableandinterpretablemodels,whichenhance
transparencyinchurnprediction,data-centricandaugmentationstrategiesthatleverage
noveldatasourcesandsyntheticdatageneration,andtraditionalMLtechniques,which
continuetoplayafoundationalroleinchurnmodeling.
Ontheotherhand,DLapproachesleverageadvancedarchitecturestocapturecom-
plexpatternsincustomerbehaviour. Theseincludedeepreinforcementlearning,which
enablesadaptivedecision-making,andtemporalandsequentialmodels,suchasLSTMs,
whichcaptureevolvingchurnpatternsovertime. Thetaxonomyalsohighlightshybrid
and ensemble DL approaches, which integrate multiple DL frameworks for improved
generalization,andCNN-basedmodels,whichexcelinfeatureextraction. Furthermore,
feedforwarddeepneuralnetworks,NLP-basedmodelsfortext-basedchurnanalysis,and
representationandfeatureinteractiontechniques,whichenhancepredictiveperformance
bycapturinghigh-orderdependencies,areexplored.
AsnotedintheIntroduction,directcomparisonofreportedperformancemetricswas
avoidedduetosubstantialheterogeneityindatasets,evaluationprotocols,andmodeling
objectives across studies. Instead, a descriptive synthesis of individual study results is
presented.
Bystructuringtheexistingresearchintothishierarchicalframework,ourtaxonomy
providesaclearperspectiveontheevolutionofchurnpredictionmethodologies. Itunder-
scoreshowdifferentapproacheshavebeentailoredtoaddressthemultifacetedchallenges
ofchurnmodeling,fromenhancingpredictiveaccuracyandscalabilitytoimprovinginter-
pretabilityanddataefficiency.

Mach.Learn.Knowl.Extr.2025,7,105
14of38
6. MachineLearningApproaches
Machine learning methodologies have significantly enhanced churn prediction
through diverse approaches to address complex customer retention challenges across
various sectors. Recent research encompasses profit-driven models, ensemble learning
techniques,optimization-basedmethods,adaptiveresamplingstrategies,explainableartifi-
cialintelligence(XAI),andtraditionalalgorithms. Eachmethodologycontributesdistinct
advantagessuchasimprovedpredictiveaccuracy,enhancedinterpretability,computational
efficiency,andalignmentwithbusinessobjectives. Thissectionreviewstheseinnovative
approaches,outliningtheirmethodologies,datacharacteristics,andperformanceevalua-
tions,therebyprovidingvaluableguidanceforselectingsuitableMLtechniquesforspecific
churnpredictionapplications.
Table1brieflysummarizeseachstudybyindicatingthedatasettypesused(public,
private,orsynthetic),MLtechniquesemployed,andperformancemetricsevaluated.
Table1.ThesummaryofstudiesinthedomainofconventionalML.
| Category | Ref. Year | Dataset | TechniquesUsed | MetricsUsed |
| -------- | --------- | ------- | -------------- | ----------- |
AUC,Expected
MaximumProfitfor
|     | [16] 2020 | Public | DT,EvolutionaryAlgorithm |     |
| --- | --------- | ------ | ------------------------ | --- |
CustomerChurn
(EMPC)
Profit-centric
MinimaxProbabilityMachines(MPM),LASSO,
|     | [17] 2020 | Public |     | ProfitMaximization |
| --- | --------- | ------ | --- | ------------------ |
TikhonovRegularization
ExpectedMaximum
|     | [18] 2024 | Private | GradientBoosting |     |
| --- | --------- | ------- | ---------------- | --- |
ProfitforB2B(EMPB)
|     | [19] 2020 | Public | EnsembleLearning | Accuracy |
| --- | --------- | ------ | ---------------- | -------- |
Accuracy,ROCAUC,PR
[20] 2020 Private LogisticRegression,LogitBoost AUC,Precision,Recall,
MCC
|     |           |         | BoostedTreeAlgorithms(XGBoost,LightGBM, | Accuracy,AUC, |
| --- | --------- | ------- | --------------------------------------- | ------------- |
|     | [21] 2021 | Private |                                         |               |
CatBoost) Precision,Recall
StackingModel(XGBoost,LogisticRegression,DT,
|     | [22] 2021 | Private |     | Accuracy |
| --- | --------- | ------- | --- | -------- |
NaïveBayes)
Accuracy,Precision,
|     | [23] 2021 | Public | SVMs,BayesianClassifier,RF |     |
| --- | --------- | ------ | -------------------------- | --- |
Recall,F1-score
|     | [24] 2022 | Private | ArtificialNeuralNetworks,RF | Accuracy |
| --- | --------- | ------- | --------------------------- | -------- |
Ensembleand
|     | [25] 2022 | Public | DecisionForest,WeightedSoftVoting | Accuracy |
| --- | --------- | ------ | --------------------------------- | -------- |
HybridML
[26] 2022 Private MultilayerNeuralNetworks,AdaBoost,RF Accuracy,ROCAUC
[27] 2022 Private CatBoost,RecursiveFeatureElimination(RFE) Accuracy,F1-score
Clustering(k-means,k-medoids),Gradient
|     | [28] 2022 | Public | BoostingTrees,DT,RF,DeepLearning, | Accuracy |
| --- | --------- | ------ | --------------------------------- | -------- |
NaïveBayes
HybridEnsembleLearning,Two-Layer
|     | [29] 2022 | Public |     | Accuracy,F1-score |
| --- | --------- | ------ | --- | ----------------- |
FlexibleVoting
[30] 2023 Private EnsembleLearning,Nelder-MeadOptimization Accuracy
[31] 2023 Public WeightedEnsembleModel(XGBoost,RF) F1-score,ExecutionTime
[32] 2023 Private WeightedEnsembleModel,Powell’sOptimization Accuracy,F1-score
|     |           |                                           | QuantumSupportVectorMachine,Quantum | Accuracy,Precision, |
| --- | --------- | ----------------------------------------- | ----------------------------------- | ------------------- |
|     | [33] 2024 | Public                                    |                                     |                     |
|     |           | k-NearestNeighbors,andQuantumDecisionTree |                                     | Recall              |

Mach.Learn.Knowl.Extr.2025,7,105
15of38
Table1.Cont.
| Category | Ref. Year | Dataset |                                     | TechniquesUsed | MetricsUsed       |
| -------- | --------- | ------- | ----------------------------------- | -------------- | ----------------- |
|          |           |         | OptimalGeneticAlgorithm(OGA)withSVM |                | Accuracy,F-score, |
|          | [34] 2020 | Public  |                                     |                |                   |
|          |           |         | (OGA-SVM),Quantum-GeneticAlgorithm  |                | Sensitivity       |
SVMs,Multi-LayerPerceptron,RF,NaïveBayes,
|     | [35] 2021 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
FeatureSelection(InformationGain)
ImprovedSMOTE(ISMOTE)withanOptimal
WeightedExtremeLearningMachine(OWELM),
|     | [36] 2021 | Public |     |     | Accuracy,F-measure |
| --- | --------- | ------ | --- | --- | ------------------ |
Multi-objectiveRainOptimizationAlgorithm
(MOROA)
| Optimization |     |     | PrincipalComponentAnalysis(PCA), |     |     |
| ------------ | --- | --- | -------------------------------- | --- | --- |
AUC,MCC,F1-score,
| and | [37] 2022 | Public | Autoencoders,LinearDiscriminantAnalysis |     |     |
| --- | --------- | ------ | --------------------------------------- | --- | --- |
Kappa
Metaheuristic
(LDA),t-SNE,XGBoost,LightGBM
ML
AntColonyOptimizationwiththeReptileSearch
|     | [38] 2022 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
Algorithm(ACO-RSA)
SVMs,ParticleSwarmOptimization(PSO),
|     | [39] 2023 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
ArtificialEcosystemOptimization(AEO)
|     |           |        | PrincipalComponentAnalysis(PCA),GreyWolf |              | Accuracy,Recall,   |
| --- | --------- | ------ | ---------------------------------------- | ------------ | ------------------ |
|     | [40] 2023 | Public |                                          |              |                    |
|     |           |        | Optimization(GWO),SVMs                   |              | F1-score           |
|     | [41] 2023 | Public | ParticleSwarmOptimization,SVMs           |              | Accuracy           |
|     |           |        | ExtremeLearningMachine,GridSearch        |              | Accuracy,F1-score, |
|     | [42] 2023 | Public |                                          |              |                    |
|     |           |        |                                          | Optimization | ModifiedAccuracy   |
[43] 2022 Public AdaptiveChurnPrediction(OTCCD),SMOTE Accuracy
Precision,Recall,
|             | [44] 2023 | Public | NaiveBayes,EvolutionaryComputation |     |          |
| ----------- | --------- | ------ | ---------------------------------- | --- | -------- |
| Adaptiveand |           |        |                                    |     | F1-score |
Resampling [45] 2023 Public HybridStatisticalModelling Recall
Accuracy,Precision,
|     | [46] 2024 | Public | XGBoost,SMOTE-ENNResampling |     |     |
| --- | --------- | ------ | --------------------------- | --- | --- |
Recall,F1-score
[47] 2021 Public Spline-RuleEnsemble,SparseGroupLasso(SGL) AUC
| Explainable   |           |        | ShapleyAdditiveExplanations(SHAP)       |     |                   |
| ------------- | --------- | ------ | --------------------------------------- | --- | ----------------- |
|               | [48] 2022 | Public |                                         |     | Accuracy          |
| and           |           |        | ExplainableAI,CollaborativeFiltering    |     |                   |
| Interpretable |           |        |                                         |     | Interpretability, |
|               | [49] 2024 | Other  | ExplainableAI,SocialInteractionAnalysis |     |                   |
Decision-Making
[50] 2021 Private NaturalLanguageProcessing,InterpretableML Accuracy
|              |           |        | Entropy-basedMin-MaxSimilarity(E-MMSIM), |                     | F1-score,AUC, |
| ------------ | --------- | ------ | ---------------------------------------- | ------------------- | ------------- |
| Data-centric | [51] 2023 | Public |                                          |                     |               |
|              |           |        |                                          | TopicClassification | Accuracy      |
and
[52] 2023 Public SyntheticDataGeneration,Data-CentricAI Accuracy
Augmentation
Network-BasedFeatureEngineering,Gradient
|     | [53] 2024 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
Boosting
Accuracy,
|     | [54] 2020 | Public | CRISP-DM,LogisticRegression,RF |     |     |
| --- | --------- | ------ | ------------------------------ | --- | --- |
MisclassificationRate
[55] 2022 Public FisherDiscriminantAnalysis,LogisticRegression Accuracy
Accuracy,Precision,
|               | [56] 2023 | Private | LogisticRegressionwithMixedPenalty |     |        |
| ------------- | --------- | ------- | ---------------------------------- | --- | ------ |
| TraditionalML |           |         |                                    |     | Recall |
KNN,DTs,LogisticRegression,RF,SVM,
|     | [57] 2023 | Public |     |     | Accuracy |
| --- | --------- | ------ | --- | --- | -------- |
AdaBoost,GBM
|     | [58] 2024 | Private |     | RF       | F1-score,Recall |
| --- | --------- | ------- | --- | -------- | --------------- |
|     | [59] 2024 | Private |     | DTs,SVMs | Accuracy        |
6.1. Profit-CentricApproaches
Recent developments in churn prediction research reflect a growing emphasis on
aligningpredictivemodelswithbusinessobjectives,particularlyprofitability. Traditionally,
churn models have been optimized for accuracy-based metrics like AUC. Still, a shift
towardintegratingfinancialconsiderationsdirectlyintomodeltraininghasemergedas
criticalformoreimpactfulcustomerretentionstrategies.
Höppneretal.[16]exemplifythisshiftbyintroducingProfTree,aprofit-drivenDTtai-
loredexplicitlyforchurnprediction. Ratherthansolelyoptimizingclassificationaccuracy,

Mach.Learn.Knowl.Extr.2025,7,105 16of38
ProfTreeemploystheExpectedMaximumProfitforCustomerChurn(EMPC)metricto
constructDTsprioritisingprofitability. Themodelsystematicallyaccountsformisclassi-
ficationcostsandcustomer-specificeconomicvaluethroughanevolutionaryalgorithm.
ExperimentsontelecommunicationdatasetsdemonstratethatProfTreesignificantlyen-
hancesprofitcomparedtoconventionalaccuracy-centricapproaches, underscoringthe
importanceofprofit-centricpredictiveanalytics.
Buildingonsimilarprinciples,Maldonadoetal.[17]proposeaprofit-orientedchurn
predictionmodelutilizingMinimaxProbabilityMachines(MPM).Unliketraditionalmeth-
ods that often use profitability metrics only during post-model selection or threshold
adjustments, this approach directly integrates profit maximization into the classifier’s
trainingobjective. Theirframeworkincludesabaselinemodelandtworegularizedvari-
antsincorporatingLASSOandTikhonovregularizationtoensurerobustgeneralization.
Benchmarkevaluationsconfirmthattheseprofit-drivenMPMextensionsyieldsuperior
profitabilityoutcomesrelativetostandardbinaryclassifiers,emphasizingthenecessityof
embeddingbusinessobjectivesdirectlyintopredictivemodeling.
Extending this perspective into the business-to-business (B2B) domain, Janssens
etal.[18]introduceB2Boost, aninstance-dependentgradientboostingmodelexplicitly
designedforB2Bchurnscenarios. Recognizingcustomerheterogeneityinprofitability,they
proposetheExpectedMaximumProfitforB2Bchurn(EMPB)metrictoguidemodeltrain-
ing.B2Boostdirectlyoptimizescustomer-specificprofitratherthantraditionalclassification
accuracy,yieldingnotableprofitimprovementsoverstandardapproaches. Thesuccessful
applicationinB2Bcontextshighlightsthebroaderpotentialofprofit-centricmethodologies
beyondconsumermarkets.
Thesestudiesunderscorethenecessityofshiftingpredictivemodelingpracticesto-
ward profit-centric frameworks. By directly incorporating financial objectives, churn
predictionmodelsbecomemorealignedwithstrategicbusinessgoals,facilitatingmore
effectiveandeconomicallybeneficialcustomerretentionefforts.
6.2. EnsembleandHybridMLApproaches
Ensembleandhybridapproacheshaveemergedasrobustmethodologiesforenhanc-
ingcustomerchurnpredictionacrossvariousindustries. Byintegratingmultipleclassifiers,
clusteringtechniques,andadvancedfeatureengineeringmethods,theseapproacheshar-
ness the strengths of individual models to mitigate the limitations of single-algorithm
solutions. Thissectionprovidesacomprehensivereviewofkeystudiesthathavedemon-
stratedtheeffectivenessofensembleandhybridlearninginchurnprediction,highlighting
theircontributionstopredictiveaccuracy,modelrobustness,andreal-worldapplicability.
Whilebothhybridandensembleapproachescombinemultiplemodels,theirintegra-
tionstrategiesdiffer. Ensemblemethods,suchasbagging,boosting,andstacking,aimto
improvegeneralizationbyaggregatingthepredictionsofseveralbaselearners,typicallyof
thesameordifferenttypes,withoutalteringtheoriginalalgorithms. Incontrast,hybrid
methodsintegratedistinctalgorithmssequentiallyorinparallel,whereonemodel’soutput
or feature transformation becomes the input for another. For example, a hybrid model
mightuseclusteringforcustomersegmentation, followedbyclassificationwithineach
segment,orcombinefeatureengineeringviaCNNswithtemporalmodelingviaLSTMs.
Hybridsystemsaregenerallymorecustomizedandoftendomain-specific, whereasen-
semblemethodsfollowstandardizedcombiningruleslikemajorityvotingorweighted
averaging.
One notable study by Liu et al. [28] introduces a hybrid approach that integrates
clustering and classification algorithms to improve predictive accuracy in the telecom
sector. Their model employs k-means, k-medoids, and random clustering techniques

Mach.Learn.Knowl.Extr.2025,7,105 17of38
alongsideclassifierssuchasGradientBoostingTrees(GBT),DTs,RFs,DL,andNaïveBayes
(NB). The study reports significant performance improvements by leveraging stacking-
basedhybridization,with96%and93.6%accuracyontheOrangeandCell2Celldatasets.
Theseresultsemphasizethebenefitsofensemblelearningandclustering-basedfeature
enhancementinchurnprediction. Similarly,Rameshetal.[24]proposeahybridmodel
combiningANNsandRFstoenhancechurnpredictionintelecommunications. TheirANN
architecture,consistingoffourhiddenlayers,achieved90.34%accuracy,outperforming
standaloneRFandsimplerANNmodels. IntegratingANN’spredictivepowerwithRF’s
robustness effectively identifies churn factors, aiding telecom companies in proactive
customerretentionstrategies.
Using hybrid approaches, Usman-Hamza et al. [25] introduce Intelligent Decision
Forest (DF) models to address scalability issues and class imbalance in telecom churn
prediction. Theirapproachsignificantlyenhancesclassificationaccuracybyincorporating
LogisticModelTree(LMT),RF,andFunctionalTrees(FT)withinaweightedsoftvotingand
stackingframework.Thestudyunderscoresthepotentialofdecisionforest-basedmodelsin
handlingimbalanceddatasetsandimprovingchurndetectionacrosstelecommunications.
Saiasetal.[26]focusonchurnpredictionwithincloudserviceproviders,emphasizing
the importance of early detection in mitigating customer loss and optimizing resource
allocation. TheirMLframeworkevaluatesmultilayerneuralnetworks,AdaBoost,andRF
models,withRFemergingasthemosteffective,achievinganaccuracyof98.8%andan
AUCscoreof0.997. Thesefindingsreinforcetherelevanceofensemblelearningindynamic
serviceindustries.
Inthecontextofthewebcastingindustry,Fuetal.[30]employanensemblelearning-
basedchurnpredictionmodeloptimizedbytheNelder-Meadalgorithm. Theirapproach
extractshigh-dimensionalbehaviouralfeaturesfromtime-seriesdata,introducinganovel
churnindicatortoenhancelabelaccuracy. Thestudydemonstratessuperioroperational
efficiencyandoutperformanceoftraditionalensemblemodels,offeringactionableinsights
forcustomerretentionstrategies.
Optimizationtechniqueshavealsobeenexploredtorefineensemblemethods. Khoh
etal.[32]introduceanoptimizedweightedensemblemodeltailoredforthetelecommuni-
cationsindustry,integratingPowell’soptimizationalgorithmtoassigndifferentialweights
tobaselearnersbasedontheirpredictivestrength. Thismodelachievesanaccuracyof
84%andanF1-scoreof83.42%,surpassingconventionalMLapproaches. Yogeshetal.[29]
furthercontributetothisdomainbyproposingatwo-layerflexiblevotingensemble,demon-
stratingtheimpactofdatabalancingonimprovingclassificationperformance.
Boostedtreemodelshavegainedtractioninvariousindustriesfortheirefficiencyin
churnprediction.Marettaetal.[21]exploretheuseofXGBoost,LightGBM,andCatBoostin
bankingchurnprediction,findingLightGBMtobethemosteffectivewith91.4%accuracy,
94.8% AUC, and 87.7% recall. Similarly, Tianpei et al. [22] implement a stacking-based
ensemble framework combining XGBoost, Logistic Regression, DTs, and Naïve Bayes,
achieving98.09%accuracybyincorporatingfeaturegroupingtechniques.
A novel direction in ensemble learning is explored by Arshad et al. [33], who in-
troduce Q-Ensemble Learning, a quantum-enhanced ensemble approachincorporating
QuantumSupportVectorMachine(Q-SVM),Quantumk-NearestNeighbors(Q-kNN),and
QuantumDecisionTree(QDT).Byintegratingblockchaintechnologyfordatasecurityand
transparency,theirmodeloutperformsclassicalensemblemodels,achieving15%higher
accuracyand12%higherprecision,demonstratingthetransformativepotentialofquantum
computinginchurnprediction.
Ensemblemethodshavealsobeenappliedtoe-commercechurnprediction. Ishrat
etal.[27]presentanAI-drivenframeworkthatcombinesmodeltuning,featureselection,

Mach.Learn.Knowl.Extr.2025,7,105 18of38
andcomparativeanalysis,achieving100%accuracyandF1-scoreusingCatBoost. Manohar
etal.[23]investigateacollectivedataminingapproachintegratingSVMs,BayesianClas-
sifiers,andRF,highlightingthebenefitsofcombiningmultipleclassifiersforimproved
accuracyandrecall.
Otherstudieshavefocusedonrefiningtraditionalensembletechniques. Mahayasa
etal.[31]proposeaweightedaverageensemblecombiningXGBoostandRF,demonstrating
superiorpredictiveperformanceinthetelecomandinsurancesectors,withanF1-score
of0.850and0.947,respectively. Hemlataetal.[20]exploreLogisticRegressionandLogit
Boost for telecom churn prediction, confirming the efficacy of boosting techniques in
outperformingconventionalregressionmodels.
Finally,Wangetal.[19]provideacomparativeanalysisofwidelyusedclassification
algorithmsforchurnprediction,reinforcingtheimportanceofensemblelearninginenhanc-
ingmodelperformance. Theirbenchmarkingstudyoffersvaluableguidanceforbusinesses
seekingdata-drivenretentionstrategies.
Thesestudiesillustrateensembleandhybridapproaches’diverseandpracticalappli-
cationsincustomerchurnprediction. ByintegratingmultipleMLmodelsandleveraging
sophisticatedfeatureengineeringtechniques,thesemethodologiesproviderobust,scal-
able,andhigh-performingsolutionstothecomplexchallengeofcustomerretentionacross
variousindustries.
6.3. OptimizationandMetaheuristicApproaches
Optimizationandmetaheuristicapproacheshavegainedprominenceinchurnpre-
diction research as effective strategies for enhancing model performance and reducing
computationalcomplexity. Thesestudiesofferrobustframeworksthatimprovepredictive
accuracyandprovidegreaterinterpretabilityandactionableinsightsbyintegratingad-
vancedfeatureselectiontechniques,hyperparametertuning,andmetaheuristicalgorithms.
Thissectionreviewskeycontributionsthatemploythesetechniquestooptimizechurn
predictionmodelsacrossvariousdomains.
Feature selection plays a critical role in improving model efficiency and accuracy.
Saheed et al. [35] introduce an ML-based churn prediction framework for the telecom-
municationssector, leveragingInformationGainandRanker-basedfeatureselectionto
enhancemodelinterpretability. Theirapproach,whichincorporatesSVM,Multi-LayerPer-
ceptron(MLP),RF,andNaïveBayes,achievesa95.02%accuracyrate,surpassingthe92.92%
obtained without feature selection. These results highlight the importance of selecting
relevantchurn-relatedattributesforimprovedclassificationperformance.
Building on feature selection techniques, Al-Shourbaji et al. [38] propose a novel
hybridmethod, ACO-RSA,whichintegratesAntColonyOptimization(ACO)withthe
Reptile Search Algorithm (RSA) to enhance predictive performance. Evaluated across
multipleopen-sourcechurndatasets,ACO-RSAoutperformsParticleSwarmOptimization
(PSO),Multi-VerseOptimizer(MVO),andGreyWolfOptimizer(GWO),demonstrating
itseffectivenessinhandlinghigh-dimensionaltelecomdata. Thisstudyunderscoresthe
potential of metaheuristic approaches in refining feature selection for improved churn
detection.
Pustokhinaetal.[36]introducetheISMOTE-OWELMmodel,whichintegratesIm-
provedSMOTE(ISMOTE)fordatabalancingwithanOptimalWeightedExtremeLearning
Machine (OWELM) for classification. A Multi-objective Rain Optimization Algorithm
(MOROA)optimizessamplingratesandmodelparameters,yielding94%,92%,and90.9%
accuracyacrossthreetelecomdatasets,significantlysurpassingtraditionalapproaches. The
study emphasizes the effectiveness of ISMOTE-OWELM in improving churn detection

Mach.Learn.Knowl.Extr.2025,7,105 19of38
whilemaintainingcomputationalefficiency,makingitavaluabletoolfortelecomproviders
aimingtoenhancecustomerretentionefforts.
Incorporatinghyperparametertuningintofeatureselection,Mirabdolbaghietal.[37]
presentacomprehensivemodeloptimizationframeworkintegratingPrincipalComponent
Analysis(PCA),Autoencoders,LinearDiscriminantAnalysis(LDA),t-SNE,andXGBoost
forfeaturereduction. TheirapproachemploysBayesianandgeneticoptimizationtofine-
tuneLightGBMmodels,significantlyoutperformingAdaBoost,SVM,andDTclassifiers.
ThestudyalsoutilizesSHAPforfeatureimportanceinterpretationandintroducesaCus-
tomerLifetimeValue(CLV)rankingsystem,offeringactionableinsightsforprioritising
high-valuecustomersatriskofchurn.
Koçog˘luetal.[42]presentanExtremeLearningMachineapproachforcustomerchurn
prediction,optimizedusinggridsearchforhyperparametertuning. Thestudyutilizesa
churndatasetfromtheUCIMachineLearningRepositoryandcomparesELM’sperfor-
manceagainstNaïveBayes,k-NearestNeighbor,andSVMmodels.Theresultsdemonstrate
thatELMachievesthehighestaccuracyof93.1%,highlightingitsefficiencyinchurnpre-
dictionduetominimalparametertuningrequirementsandcompetitiveperformance. The
studyunderscoresELM’spotentialasarobustandeffectivetechniqueforchurnanalysis.
Metaheuristicoptimizationhasalsobeenexploredtoenhancegradientboostingtech-
niques. AlShourbajietal.[39]proposetheEnhancedGradientBoostingModel(EGBM),
whichintegratesanSVMRBFbaselearnerwithPSOandArtificialEcosystemOptimization
(AEO)forhyperparametertuning. Evaluatedonseventelecomdatasets,EGBMdemon-
strates superior predictive capabilities compared to traditional GBM and SVM models,
effectivelyaddressingprematureconvergenceandenhancingcustomerretentionstrategies.
Hybridoptimizationapproachesfurtherimprovechurnpredictionefficiency. Kurtcan
etal.[40]introducePCA-GWO-SVM,amodelcombiningPrincipalComponentAnalysis
(PCA)forfeatureselection,GreyWolfOptimizationforhyperparametertuning,andSVM
forclassification. Comparedtologisticregression,k-nearestneighbors,naïveBayes,and
DTs,PCA-GWO-SVMachieveshigheraccuracy,recall,andF1-score,reinforcingthevalue
ofcombiningoptimizationtechniqueswithclassificationframeworks.
Ponnusamyetal.[41]employaPSO-SVM-basedalgorithmtoenhancechurnpredic-
tion performance in the banking sector. By optimizing hyperparameters using Particle
SwarmOptimization,theirapproachsignificantlyoutperformstraditionalSVMmodels,
demonstratingtheeffectivenessofhybridoptimizationstrategiesforfinancialinstitutions
seekingtominimizecustomerattrition. Similarly,Venkateshetal.[34]proposeanOptimal
GeneticAlgorithm(OGA)withSVMforcloud-basedchurnprediction. Theirapproach
utilizes a double-chain quantum genetic algorithm to fine-tune SVM hyperparameters,
achievinghighsensitivity(94.50),accuracy(90.27),andanF-scoreof94.30. Thesefindings
underscoretheeffectivenessofgeneticoptimizationinenhancingpredictiveperformance,
makingitapromisingtechniqueforlarge-scalecloud-basedanalytics.
Thesestudiesillustratehowoptimizationandmetaheuristicapproachessignificantly
improvechurnpredictionmodels’accuracy,efficiency,andinterpretability. Byintegrat-
ingadvancedfeatureselection,hyperparametertuning,andmetaheuristicoptimization,
thesemethodologiesprovidescalableandhigh-performingsolutionsforindustriesgrap-
plingwithcomplexcustomerdata,ultimatelyenhancingretentionstrategiesandbusiness
decision-making.
6.4. AdaptiveandResamplingApproaches
In dynamic environments where customer behaviour and data distributions con-
tinuously evolve, addressing class imbalance and adapting to concept drift are critical
challengesinchurnprediction. Researchershaveincreasinglyturnedtoresamplingand

Mach.Learn.Knowl.Extr.2025,7,105 20of38
adaptivelearningstrategiestoenhancemodelperformanceinreal-timeapplications. This
sectionreviewskeystudiesthatemploythesetechniquestomitigateimbalancesandadapt
predictivemodelstochangingdatapatterns,ensuringmoreaccurateandreliablechurn
detection.
Ahmadetal.[43]introducetheOptimizedTwo-SidedCumulativeSumChurnDetec-
tor(OTCCD),anoveladaptivechurnpredictionframeworkfortelecomdatastreams. By
integratingtheSyntheticMinorityOver-samplingTechnique(SMOTE)fordatabalancing
andacumulativesumcontrolchartfordriftdetection,OTCCDefficientlyidentifiesshifts
incustomerbehaviourwithinaslidingwindowframework. Experimentalevaluations
on real-world telecom datasets, such as Call Detail Records, demonstrate that OTCCD
outperformstraditionalmethodsbyprovidinghigheraccuracyandfasterdriftdetection.
Thisstudyhighlightstheimportanceofreal-timeadaptabilityinchurnpredictionmodels,
offeringtelecomcompaniesarobusttoolforproactivecustomerretentionstrategies.
Adnanetal.[44]proposeanadaptivelearningapproachthatintegratesevolutionary
computationwithaNaïveBayesclassifiertoaddressclassimbalanceintelecommunications
churnprediction. Bydynamicallyadjustingmodelparametersbasedonincomingdata
patterns,thehybridmethodsignificantlyimprovesprecision,recall,andF1scorescompared
totraditionalapproaches. Evaluationsonreal-worldtelecomdatasetsconfirmthemodel’s
effectivenessinproactivelyidentifyingat-riskcustomers, underscoringthepotentialof
adaptivelearninginminimizingrevenuelossduetocustomerchurn.
Complementingadaptivemethodologies,Shimaaetal.[46]developahybridchurn
predictionframeworkthatcombinesXGBoostwithSMOTE-ENNresamplingtobalance
datasetsandimproveclassificationaccuracy. Thisintegrationenhancesprecision,recall,
andF1scores,outperformingconventionalMLtechniquesacrossthreetelecomdatasets.
Byeffectivelyaddressingclassimbalanceandleveragingensemblelearning,themodel
facilitatesproactiveretentionstrategies,reinforcingtheroleofresamplingtechniquesin
churnprediction.
Incorporating a more customer-centric approach, Lee et al. [45] propose a hybrid
churnpredictionframeworkthatdynamicallymodelschurnprobabilitybasedoncustomer
lifetimevalueratherthanfixedperiods. Bysegmentingcustomersintogroupssuchas
new,short-term,high-value,andchurn-proneusers,theirmethodologyappliestailored
MLmodelstoenhancepredictiveaccuracy. EvaluationsofdatasetsfromaU.K.giftseller
andPakistan’smostsignificante-commerceplatformshowrecallscoresrangingfrom0.56
to 0.72 in one case and 0.91 to 0.95 in another. The study highlights the advantages of
integratingstatisticalmodelingwithMLtechniquestorefinecustomerretentionstrategies
whilereducingdatarequirements.
Thesestudiesillustratehowadaptiveandresamplingapproacheseffectivelyaddress
class imbalance and concept drift, enabling more scalable and robust churn prediction
solutions. Byintegratingreal-timelearning,resamplingtechniques,andevolutionaryopti-
mization,thesemethodologiesprovidepowerfultoolsforbusinessesseekingtoenhance
customerretentionstrategiesinevolvingmarketconditions.
6.5. ExplainableandInterpretableApproaches
Understandingtheunderlyingdecisionprocessesincomplexpredictivetaskssuchas
churnpredictioniscrucialforgainingstakeholdertrustandfacilitatingactionableinsights.
Recentresearchhasincreasinglyfocusedonintegratinginterpretabilityandexplainable
AItechniquesintochurnpredictionmodels. Thissectionreviewskeycontributionsthat
enhancemodeltransparencythroughrule-basedformulations,SHAPanalyses,andother
XAImethodologies.

Mach.Learn.Knowl.Extr.2025,7,105 21of38
DeBocketal.[47]introduceSpline-RuleEnsembleclassifierswithStructuredSpar-
sityRegularization(SRE-SGL)asaninterpretableapproachtocustomerchurnprediction.
WhiletraditionalMLmodelsoftenprioritisepredictiveaccuracy,thisstudyemphasizesthe
needforexplainablemodelsthatprovideactionableinsightsintocustomerbehaviour. The
proposedspline-ruleensemblesintegratetree-basedensemblemethodswithregression
analysis, balancing model flexibility and simplicity. However, conventional rule-based
ensemblescanbecomeexcessivelycomplexduetoconflictingcomponents. Toaddressthis,
theauthorsincorporateSparseGroupLassoregularization,whichenhancesinterpretability
byenforcingstructuredsparsity. Evaluationsacrossfourteenreal-worlddatasetsdemon-
stratethatSRE-SGLoutperformsstandardruleensemblesinAUCandtopdecileliftwhile
maintainingcompetitivepredictiveperformance. Acasestudyinthetelecommunications
sectorfurtherillustratesthemodel’sinterpretability,reinforcingthevalueofstructured
regularizationinmakingchurnpredictionbotheffectiveandexplainable.
Extendinginterpretabilitytechniquestoworkforceanalytics,Mitravindaetal.[48]
investigateemployeeattritionpredictionusingMLmodelsandXAImethodologies. Their
study applies SHAP to identify key factors driving attrition and visualize their impact.
Additionally, the research introduces a recommendation system leveraging user-based
collaborativefilteringtoproposepersonalizedretentionstrategies.Bycombiningpredictive
modelingwithactionableinsights,thisstudydemonstrateshowXAItechniquescaninform
moreeffectiveemployeeretentionpolicies.
Indigitalentertainment,Wangetal.[49]addressthechallengeofplayerchurnpre-
dictioninonlinevideogames,whereunderstandingsocialinteractiondynamicsiscritical.
WhileMLmodelsarewidelyusedforplayerbehaviouranalysis,theirblack-boxnature
limitsadoptionbyproductmanagersandgamedesigners. Thestudyrestructuresmodel
inputsintoexplicitandimplicitfeaturestobridgethisgap,enhancingexpertinterpretabil-
ity. Furthermore, the research highlights the necessity of XAI techniques that explain
featurecontributionsandprovideactionablerecommendationsforreducingchurn. The
proposedapproachisvalidatedthroughtwocasestudiesinvolvingexpertfeedbackanda
within-subjectuserstudy,demonstratingitseffectivenessinimprovingdecision-making
forplayerretentionstrategies.
Together,thesestudiesillustratethecrucialroleofinterpretabilityinchurnprediction
models. ByintegratingadvancedXAItechniques,researchersbridgethegapbetweenhigh
predictive performance and the need for transparent, actionable insights. This integra-
tionsupportsmoreinformedandeffectiveretentionstrategiesacrossdiverseindustries,
reinforcingthevalueofexplainableAIinreal-worldpredictiveanalytics.
6.6. Data-CentricandAugmentationApproaches
Beyondrefiningpredictivemodels,recentresearchinchurnpredictionhasincreasingly
emphasizedenhancingthequalityanddiversityoftrainingdata. Data-centricandaugmen-
tationapproachesseektoenrichtraditionaldatasetsbyincorporatingnoveldatasources,
generatingsyntheticdata,andleveragingadvancedfeatureengineeringtechniques. These
strategiesarecrucialforimprovingmodelrobustness,addressingdataimbalances,and
achievinghigherpredictiveaccuracy. Thissectionreviewskeycontributionsthatexemplify
theseefforts.
Voetal.[50]exploreanovelchurnpredictionapproachthatintegratesunstructured
calllogdatawithtraditionalstructureddata. WhileexistingMLmodelsprimarilyrely
ondemographicandaccounthistorydata,thisstudyhighlightstheuntappedpotentialof
analyzingspokencontentfromcustomerinteractions. Usingnaturallanguageprocessing
techniques,theauthorsprocessalarge-scalecallcenterdatasetcontainingtwomillioncalls
fromover200,000customers. Theirfindingsdemonstratethatincorporatingunstructured

Mach.Learn.Knowl.Extr.2025,7,105 22of38
calldatasignificantlyenhancespredictionaccuracywhileprovidingdeeperinsightsinto
customerbehaviour. Additionally,interpretableMLtechniquesextractpersonalitytraits
andcustomersegmentationpatterns,facilitatingpersonalizedretentionstrategies. This
studyunderscorestheimportanceofcombiningstructuredandunstructureddatasources
to develop more comprehensive churn prediction frameworks in the financial services
industry.
Soumietal.[51]addressthechallengeofoptimizingtrainingdataqualitythrougha
representation-basedquerystrategyforchurnprediction. Givenmanualdataannotation’s
high cost and inefficiency, the authors propose Entropy-based Min-Max Similarity (E-
MMSIM),anactivelearningalgorithminspiredbyproteinsequencingtechniques. This
methodselectsthemostinformativeandrepresentativedatapointsforannotation,reducing
redundancyandimprovingmodelefficiency. Theapproachenhancestopicclassification
accuracyincustomerservicemessages,yieldingsignificantimprovementsinF1-score,AUC,
andoverallmodelperformance. Moreover,whenthesequalitativefeaturesareintegrated
withstructuredcustomerdata,churnpredictionmodelsachievea5%performancegain.
ThestudyhighlightsthecriticalroleofdataselectionstrategiesinoptimizingMLworkflows
forcustomerretentionmanagement.
Intherealmofsyntheticdatageneration,Wangetal.[52]exploretheimpactofdata-
centric AI on churn prediction. Unlike traditional model-centric AI, which focuses on
hyperparametertuningandalgorithmmodifications,data-centricAIenhancespredictive
performancebyimprovingtrainingdataqualityanddistribution. Thisresearchevaluates
variousdatasynthesisalgorithms,examiningtheireffectsondatabalancing,augmenta-
tion,andsubstitution. Thefindingsunderscorethepotentialofresamplingmethodsin
mitigatingclassimbalanceandimprovingmodelrobustness,providingvaluableinsights
forAI-drivenchurnpredictionframeworksacrossindustries.
Babaketal.[53]introduceasocialnetwork-basedchurnpredictionmodel,recognizing
thatsocialinteractionsandpeerbehaviourofteninfluencecustomerchurn.Thestudydevel-
opsafeatureengineeringapproachincorporatinginfluenceandconformityindicesderived
fromcallnetworkdata. Byintegratingsocialconnectivitymetrics,themodelsignificantly
enhancesthepredictivepowerofstandardMLclassifiers,particularlygradientboosting
models. Thisresearchdemonstratesthatchurnisnotsolelyanindividualdecisionbutis
shapedbybroadersocialdynamics. Thisperspectiveextendsbeyondtelecommunications
tovariousindustrieswherepeerinfluenceaffectscustomerbehaviour.
Collectively,thesestudiesillustratethetransformativeimpactofdataaugmentation
andqualityimprovementinchurnprediction. Researchersaredevelopingmorecompre-
hensiveandrobustpredictiveframeworksbyincorporatingnoveldatasources,employing
activelearningfordataselection,generatingsyntheticdata,andleveragingsocialnetwork
information. Theseadvancementsenhancemodelaccuracyandprovidedeeperinsights
intocustomerbehaviour,enablingmoreeffectiveandproactiveretentionstrategies.
6.7. TraditionalMLApproaches
Traditional machine learning approaches significantly influence churn prediction
byleveragingestablishedstatisticalandalgorithmictechniques. Thesemethodsrelyon
classicalmodelsandfeatureengineeringtoderiveactionableinsightsandachievehigh
predictiveaccuracy. Thissectionhighlightskeystudiesthatexemplifytheapplicationof
conventionalMLmethodologiesacrossdiversedomains.
Tianyuanetal.[55]presentadata-drivenapproachtocustomerchurnpredictionin
telecommunications,incorporatingcustomersegmentationtoenhancepredictiveaccuracy.
UsingFisherdiscriminantanalysisandlogisticregression,theirmodelachievesa93.94%
accuracy rate on telecom datasets, effectively identifying potential churners. Tailoring

Mach.Learn.Knowl.Extr.2025,7,105 23of38
predictions to specific customer groups enhances the precision of retention campaigns,
providingtelecomoperatorswithapowerfultooltoproactivelyreducechurnandimprove
profitability. The study underscores the significance of segmentation in refining churn
predictionmodels.
Expanding on customer relationship management (CRM) applications, Šimovic´
et al. [56] explore churn prediction using big data analytics to analyze heterogeneous
customer behaviours, such as self-care service usage, service duration, and responsive-
nesstomarketingefforts. Theirstudyintroducesanenhancedlogisticregressionmodel
withamixedpenaltytermtomitigateoverfittingandbalancefeatureselection. Empirical
evaluationonalargeCRMdatasetdemonstrateshighclassificationperformanceacross
standardmetrics,reinforcingthepotentialofpenalizedlogisticregressionasascalableand
computationallyefficientapproachtochurnmodelinginbigdataenvironments.
Jakobetal.[58]extendtraditionalMLtechniquestothedigitalhealthsector,investigat-
ingearlyuserchurninaweightlossapp. Byanalyzingengagementdatafrom1283users
and310,845eventlogs,thestudyemploysanRFmodeltopredictuserdropoutbasedon
dailylogincounts. AchievinganF1scoreof0.87onday7andidentifying93%ofchurned
users,thestudyhighlightshowchurnpredictioncanenablepersonalizedretentionstrate-
giesindigitalhealthinterventions,ultimatelyimprovinglong-termuserengagementand
healthoutcomes.
Returningtothetelecommunicationsindustry,Sikrietal.[59]developedanML-based
approachforimprovingcustomerretention. Byanalyzingcustomerdemographics,usage
patterns, and service details, the study applies DTs and SVM to identify customers at
riskofchurning. Theresultsdemonstratehighpredictiveaccuracy,empoweringtelecom
companiestoimplementtargetedretentionstrategieseffectively. Thisstudyreaffirmsthe
valueofconventionalMLtechniquesincustomerretentionefforts.
Expandingonreal-timepredictionapplications,Nyashadzasheetal.[54]developeda
churnpredictionmodeltailoredforthetelecommunicationsindustry,specificallyfocusing
onprepaidcustomerswhofrequentlyswitchproviders. UsingWatsonStudio,theirstudy
employs big data analytics within the CRISP-DM framework and evaluates three ML
algorithms—Logistic Regression, RF, and DT. While Logistic Regression exhibited the
lowest misclassification rate (2.2%), RF and DT achieved relatively high accuracy rates
(78.3%and79.2%,respectively)butsufferedfrommisclassificationratesabove20%. This
researchunderscoresthelimitationsofrelyingsolelyonaccuracymetricsandadvocates
for more comprehensive evaluation techniques to enhance real-time churn prediction
performance.
Beyond customer churn, AbdElminaam et al. [57] introduce EmpTurnoverML, an
AI-drivenapproachforpredictingemployeeturnoverandcustomerchurnusingMLalgo-
rithms. Thestudyevaluatesvariousclassificationtechniques,includingK-NearestNeigh-
bors,DTs,LogisticRegression,RF,SVM,AdaBoost,NaïveBayes,andGradientBoosted
Machines(GBM),usingan80-20train-testsplit. Byidentifyingkeypatternsassociatedwith
employeedepartures,thestudyhighlightshowAI-poweredpredictionmodelscanhelp
organizationsimplementproactiveretentionstrategies,reducinghiringandtrainingcosts
whileenhancingworkforcestability. Thefindingsdemonstratethebroaderapplicabilityof
churnpredictionmethodologiesinworkforceanalyticsandbusinessefficiency.
ThesestudiesillustratethecontinuedrelevanceofconventionalMLapproachesin
churnprediction. Throughrigorousmodeldevelopmentandstrategicfeatureengineering,
these methodologies provide potent tools for organizations seeking to mitigate churn,
improvecustomerandemployeeretention,anddrivesustainablebusinessgrowth. Overall,
traditional ML methods such as decision trees, logistic regression, and support vector
machinesremainvaluedfortheirinterpretability, computationalefficiency, andeaseof

Mach.Learn.Knowl.Extr.2025,7,105
24of38
deployment. However,theymaystrugglewithhigh-dimensionalorsequentialdata,and
theirperformanceisoftenlimitedcomparedtomoreadvancedensembleapproaches.
7. DeepLearningApproaches
Deeplearningtechniqueshavesignificantlyadvancedchurnpredictionbyofferingdi-
versemethodologiesthataddresscomplexuserbehaviourpatternsandindustryretention
challenges. Recentadvancementsincludedeepreinforcementlearning,sequentialmod-
elingwitharchitectureslikeLSTMs,hybridandensemblemethodsintegratingmultiple
DLparadigms,CNNstailoredforstructureddata,efficientfeedforwardneuralnetworks,
and innovative representation learning and feature interaction models. Each category
providesuniquestrengths,suchasimprovedaccuracy,enhancedinterpretability,orcom-
putationalefficiency,collectivelysupportingproactiveandeffectivechurnmanagement
strategies. Thissectionexploresthesedistinctapproaches,highlightingtheirapplications,
advantages,andcontributionstopredictiveanalytics. Table2highlightsthedatasetsused
(public,private,simulation-based),DLtechniquesimplemented,andperformancemetrics
evaluated.
Table2.ThesummaryofthestudiesinthedomainofDL.
| Category | Ref. Year | Dataset | TechniquesUsed |     | MetricsUsed |
| -------- | --------- | ------- | -------------- | --- | ----------- |
DeepReinforcement
|     | [60] 2020 | Simulation | DeepReinforcementLearning |     | Accuracy |
| --- | --------- | ---------- | ------------------------- | --- | -------- |
Learning
|     | [61] 2020 | Public | Trajectory-basedLSTM(TR-LSTM) |     | ROCAUC |
| --- | --------- | ------ | ----------------------------- | --- | ------ |
AUC,F1-Score,
|     | [62] 2020 | Public | LSTM-basedDynamicChurnModel |     | LogLoss,Lift, |
| --- | --------- | ------ | --------------------------- | --- | ------------- |
EMPC
| Temporaland |     |     | LSTMandGatedRecurrentUnit(GRU) |     |     |
| ----------- | --- | --- | ------------------------------ | --- | --- |
SequentialDL
[63] 2024 Private networks,LightGBM,SHAP,Explainable AUC,F1-score
BoostingMachines(EBM)
Accuracy,
|     | [64] 2024 | Public |     | LSTM | Precision,Recall, |
| --- | --------- | ------ | --- | ---- | ----------------- |
F1-score
AttentionalDLmodel(AttnBLSTM-CNN)
F1-score,ROC
|     | [65] 2022 | Private | integratedwithBidirectionalLSTMs |     |     |
| --- | --------- | ------- | -------------------------------- | --- | --- |
AUC
(BiLSTM)andCNNs
StackedBidirectionalLSTMs(SBLSTM)
andRNNswithanarithmeticoptimization
| Ensembleand | [66] 2023 | Private |     |     | Accuracy |
| ----------- | --------- | ------- | --- | --- | -------- |
algorithm(AOA),ImprovedGravitational
HybridDL
SearchOptimizationAlgorithm(IGSA)
[67] 2023 Public K-MeansClustering,Self-AttentionLSTM AUC,F1-score
Accuracy,
[68] 2024 Private StackedDNNs,LogisticRegression Precision,Recall,
F1-score
Accuracy,ROC
|     | [69] 2021 | Public | ComparativeCNNs,LSTMs |     |     |
| --- | --------- | ------ | --------------------- | --- | --- |
AUC,G-Mean
CNNs,ExtendedConvolutionalDecision
CNN–based
[70] 2022 Private Trees(ECDT)integratedwithGridSearch Accuracy
Optimization
|     | [71] 2024 | Public | 1DCNN,ResidualBlocks,Attention |     | Accuracy |
| --- | --------- | ------ | ------------------------------ | --- | -------- |
|     | [72] 2020 | Public | DNN,RF,XGBoost                 |     | Accuracy |
FeedforwardDeep
Multi-LayerPerceptron,RadialBasis
| NeuralNetwork | [73] 2024 | Public |     |     | Accuracy |
| ------------- | --------- | ------ | --- | --- | -------- |
Function(RBF)Networks
| NLP-basedDL | [74] 2021 | Private |                                | NLP,RNNs | F1-score |
| ----------- | --------- | ------- | ------------------------------ | -------- | -------- |
|             | [75] 2020 | Public  | FeatureInteractionNetwork(FIN) |          | Accuracy |
Representationand
FeatureInteraction [76] 2021 Public VectorEmbeddingsforChurn F1-score

Mach.Learn.Knowl.Extr.2025,7,105 25of38
7.1. DeepReinforcementLearningApproaches
Deepreinforcementlearningapproachesrepresentanemergingparadigminchurn
prediction,particularlywithindynamicenvironmentssuchasdigitalentertainment. These
methodsgobeyondtraditionalsupervisedlearningbyleveragingsimulation-basedtech-
niquestomodelcomplexuserbehavioursandengagementdynamics. Thissectionhigh-
lightsapioneeringstudythatexemplifiesthepotentialofdeepreinforcementlearningin
addressingchurnchallengesinmobilegaming.
Roohietal.[60]introduceanovelsimulation-basedmodelforpredictingchurnin
mobilegaming. UnliketraditionalsupervisedMLmodelsthatrelyonhistoricalplayer
data,thisworkintegratesDeepReinforcementLearningtosimulateAI-drivengameplay
behaviour, capturing in-game difficulty and player skill evolution. A key strength of
thisapproachisitsabilitytomodelplayerpersistenceandengagementdynamicswithout
requiringextensivereal-worldbehaviouraldata.Thestudydemonstratesthatincorporating
apopulation-levelsimulationofplayerheterogeneityimproveschurnpredictionaccuracy,
therebyreducingthedependencyonexpensiveretrainingofDRLagents. Thisframework
offers a promising direction for churn analysis in digital entertainment, where player
retentionstrategiesarecriticalforrevenuesustainability.
7.2. TemporalandSequentialDLApproaches
TemporalandsequentialDLapproacheshaveemergedasessentialtoolsforcapturing
thedynamicnatureofcustomerbehaviourinchurnprediction. Byleveragingtemporal
dependencies inherent in user engagement data, these models enable a more nuanced
understandingofchurnpatterns,ultimatelyleadingtomoreeffectiveretentionstrategies.
Thissectionreviewsrecentstudiesthatutilizedeepsequentialarchitectures,suchasLSTM
networks,toenhancechurnpredictionperformance.
Joyetal.[63]presentahybridDLapproachthatintegratessequentialmodelingwith
explainableAItoimprovechurnpredictioninstreamingservices.Theproposedframework
combinesLSTMandGatedRecurrentUnit(GRU)networkstocapturetemporaltrendsin
userengagement,complementedbyLightGBMtorefinepredictiveperformance. Akey
contributionofthisstudyisitsemphasisoninterpretability,employingShapleyAdditive
ExplanationsandExplainableBoostingMachines(EBM)toprovidetransparencyinfeature
importancerankings. Byensuringthatdecision-makersunderstandthereasoningbehind
churnpredictions,themodelenhancesactionableinsightsforbusinessapplications. The
studyreportsstate-of-the-artperformance,achievinga95.60%AUCanda90.09%F1score,
reinforcingtheeffectivenessofhybridarchitecturesinchurnanalysis.
ExpandingonsequentialDLtechniques,Zhuetal.[61]introduceatrajectory-based
LSTMframework(TR-LSTM)forchurnprediction,whichextractsthreetrajectory-based
featuresfromcustomermovementdata. Themodelsignificantlyoutperformstraditional
methods, demonstrating the utility of spatiotemporal behaviour analysis in predicting
churn. Similarly, Alboukaey et al. [62] emphasize the importance of daily behavioural
patternsbydevelopinganLSTM-baseddynamicchurnpredictionmodelformobiletelecom
customers. Unlike conventional monthly-based models, this approach captures short-
term fluctuations in customer activity, enhancing prediction accuracy and allowing for
more timely interventions. These findings underscore the superiority of LSTM-based
architectures in modeling evolving user engagement patterns, particularly in dynamic
serviceindustries.
FurthervalidatingtheeffectivenessofLSTMs,Beltozar-Clementeetal.[64]demon-
stratethatdeepsequentialnetworkscanovercomevanishinggradientissuesandeffectively
modellong-termdependenciesincustomerbehavioursequences.Theirstudyachieves95%

Mach.Learn.Knowl.Extr.2025,7,105 26of38
performanceacrossmultipleevaluationmetrics,highlightingthepotentialofLSTM-based
modelstorefinechurnpredictionbycapturingcomplexbehaviouraltrends.
Collectively,thesestudiesestablishsequentialandtemporalDLapproachesasrobust
toolsforchurnprediction. ByleveragingLSTM-basedarchitectures,thesemodelsoffer
enhanced predictive accuracy, more profound insights into user behaviour, and timely
interventions,makingtheminvaluablefordevelopingproactiveretentionstrategiesacross
variousindustries.
7.3. EnsembleandHybridDLApproaches
EnsembleandHybridDLapproacheshavegainedsignificanttractioninchurnpredic-
tionduetotheirabilitytocombinemultiplemodels’strengthsandovercomeindividual
architectures’limitations. Theseapproachesachieveenhancedpredictiveaccuracyand
improvedgeneralizationacrossdiverseapplicationdomainsbyintegratingDLtechniques,
suchasRNNs,CNNs,andattentionmechanisms,withensemblemethodsandoptimization
algorithms. Thissectionhighlightskeystudiesthatexemplifytheeffectivenessofhybrid
andensemblestrategiesinchurnprediction.
Jajametal.[66]introduceanensemblemodelthatintegratesStackedBidirectional
LSTMs(SBLSTM)andRNNswithanarithmeticoptimizationalgorithm(AOA).Theframe-
workisfine-tunedusinganimprovedGravitationalSearchOptimizationAlgorithm(IGSA),
achievingastate-of-the-artaccuracyof97.89%intheinsurancedomain. Theseresultshigh-
lightthepotentialofensemblearchitecturestoeffectivelymergemultipleDLtechniques,
improvinggeneralizationandperformanceinchurnpredictiontasks.
Similarly,Liuetal.[65]presentafusedattentionalDLmodel(AttnBLSTM-CNN)that
integratesBidirectionalLSTMs(BiLSTM)andCNNstoaddressthelimitationsofstandalone
RNNsandCNNs.Byincorporatinganattentionmechanism,themodelenhancesprediction
accuracy by prioritising critical customer behaviour patterns. The study demonstrates
thatintegratingattentionlayersintoDLpipelinesimproveschurndetectionaccuracyand
enhancesinterpretability,providingvaluableinsightsforfinancialinstitutions.
Expandingonhybridarchitecturesinthefinancialsector,Van-Hieuetal.[68]propose
aDLensemblemodelforcustomerchurnpredictioninbanking. Theapproachemploys
astackedDLarchitecturewhereLevel0integratesthreedistinctdeepneuralnetworks,
andLevel1utilizesalogisticregressionmodelforfinalprediction. TestedontheBank
Customer Churn Prediction dataset, the framework achieves 96.60% accuracy, 90.26%
precision,91.91%recall,andanF1-scoreof91.07%. Theseresultshighlighttherobustness
ofcombiningDLmodelswithlogisticregressiontoimprovechurnpredictionaccuracy,
reinforcingthevalueofensemblemethodologiesinfinancialcustomerretentionstrategies.
Zhaoetal.[67]furtherenhancechurnpredictionbyintegratingunsupervisedand
supervised learning techniques. Their hybrid model incorporates K-means clustering,
entropy-basedmethods,andcustomerportraitanalysisforsegmentingtelecomcustomers.
Amulti-headself-attention-basednestedLSTMclassifieristhenappliedtoevaluatecus-
tomerbehaviour.TestedonChina’stelecommarketdata,themodeloutperformstraditional
classificationmethodsbyimprovingtheaccuracyofcustomerbehaviourrecognition. Ad-
ditionally,iteffectivelydifferentiatesbetweenmedium-valueandhigh-valuecustomers,
providingcriticalinsightsforprecisionmarketingstrategiesandenablingtelecomcompa-
niestotailorserviceofferingsmoreeffectively.
Collectively,thesestudiesillustratethathybridandensembleDLapproachesenhance
predictiveaccuracyandimprovemodelinterpretabilityandgeneralizationacrosssectors.
Theirinnovativeintegrationofdiversemethodologiesofferspromisingavenuesfordevel-
opingrobust,scalablechurnpredictionsystemsthateffectivelysupporttargetedretention
strategies.

Mach.Learn.Knowl.Extr.2025,7,105 27of38
7.4. CNN–BasedApproaches
ConvolutionalNeuralNetworkshaveemergedasapowerfultoolinchurnprediction,
particularlyfortasksrequiringcomplexfeatureextractionandhierarchicaldatarepresen-
tation. Whiletraditionallyappliedtoimageandtextprocessing,CNN-basedapproaches
haveproveneffectiveinstructureddatascenarios,offeringimprovedpredictiveaccuracy
and addressing challenges such as class imbalance and information loss. This section
reviewskeystudiesthatleverageCNNs—oftenincombinationwithothertechniques—to
enhancechurnpredictionmodels.
Muhammad et al. [69] compare DL architectures on benchmark datasets such as
Cell2CellandKDDCupforchurnprediction. TheirfindingsidentifyCNNsasthemost
effectivemodelbasedonmultipleevaluationcriteria,outperformingtraditionalMLalgo-
rithmsandDLmodels. Theseresultsunderscoretheabilityofconvolutionalarchitectures
tocapturehierarchicalrelationshipswithincustomerdata,particularlyinscenarioswhere
featureextractionposessignificantchallenges.
Extending CNN applications to workforce analytics, Ebru et al. [70] introduce a
hybrid model (ECDT-GRID) for employee churn prediction. This approach integrates
ExtendedConvolutionalDecisionTrees(ECDT)withgridsearchoptimizationtoenhance
classificationaccuracy.UnlikeconventionalCNNapplicationsinimageandtextprocessing,
thisstudyadaptsCNNsforstructurednumericaldata,addressinginformationlossthrough
DT-basedlearning. TheECDT-GRIDmodeloutperformsCNN,ECDT,andtraditionalML
models,demonstratingtheimportanceofhyperparametertuninginimprovingpredictive
performance. ThestudyhighlightsthepotentialofDLinworkforceanalytics,particularly
inretail,whereemployeechurnimpactsoperationalstability. BycombiningCNNswith
DTstructures,thisapproachprovidesarobustpredictiveframework,showcasingtherole
ofDLinoptimizingemployeeretentionstrategies.
Sahaetal.[71]introduceChurnNet, anovelDL-basedchurnpredictionmodeltai-
loredforthetelecommunicationsindustry(TCI).Recognizingtheimportanceofcustomer
retentioninacompetitivemarket,thestudyaimstoenhancepredictiveaccuracybeyond
existing methods. ChurnNet integrates a 1D convolutional layer with residual blocks,
squeeze-and-excitationblocks,andaspatialattentionmodule,allowingthemodeltocap-
turecomplexfeaturedependencieswhilemitigatingthevanishinggradientproblem. The
model is evaluated using three public datasets, each exhibiting significant class imbal-
ance, which is addressed through SMOTE, SMOTEEN, and SMOTETomek resampling
techniques. Rigorousexperimentation,including10-foldcross-validation,demonstrates
thatChurnNetoutperformsstate-of-the-artmodels,achievingaccuracyscoresof95.59%,
96.94%,and97.52%acrossthethreedatasets. ThesefindingsemphasizethepotentialofDL
architectureswithattentionmechanismsinadvancingchurnpredictionmodels,making
themmoreeffectiveandinterpretablefortelecomserviceproviders.
These studies highlight the versatility and strength of CNN-based approaches in
churnprediction. Byaddressingchallengessuchasfeatureextraction,informationloss,
andclassimbalance,CNNsandtheirhybridvariantsproviderobustframeworksthatcan
beadaptedtovariousapplications—fromcustomerretentionintelecomtoemployeechurn
inretail—underscoringtheircriticalroleinmodernpredictiveanalytics.
7.5. FeedforwardDeepNeuralNetworkApproaches
Feedforwarddeepneuralnetworkapproachesremainwidelyusedinchurnprediction
becausetheycanlearncomplexnonlinearrelationshipsdirectlyfromdatawhilemaintain-
ingrelativelystraightforwardarchitectures. Thesemethods,includingExtremeLearning
Machines,Multi-LayerPerceptrons,andDeepNeuralNetworks,balancepredictiveperfor-

Mach.Learn.Knowl.Extr.2025,7,105 28of38
manceandcomputationalefficiency. Thissectionreviewskeystudiesthathaveleveraged
thesearchitecturestoachieverobustchurnpredictionoutcomes.
Małgorzataetal.[73]evaluateMulti-LayerPerceptronandRadialBasisFunction(RBF)
networksforchurnpredictioninmobiletelecommunications. Theirfindingssuggestthat
MLPsachievenear-perfectaccuracy(0.999),significantlyoutperformingtraditionalfuzzy
rule-basedandrough-setsystems. However,thestudyalsoacknowledgestheblack-box
natureofneuralnetworks,emphasizingtheneedforexplainabilityinDLmodelstosupport
real-worldadoption. Theseinsightshighlightthetrade-offbetweenmodelperformance
andinterpretability,anongoingchallengeindeployingDLsolutionsforchurnprediction.
Setyo[72]investigateschurnpredictioninthetelecommunicationssectorusingDeep
NeuralNetworks,comparingtheirperformanceagainstRFandXGBoost. Recognizingthe
criticalimpactofcustomerattritiononbusinessretention,thestudyincorporatesfeature
selection techniques and evaluates model efficiency using Google Colaboratory with a
TensorFlowbackend. TheresultsindicatethatDNNachieves80.62%accuracyinjust68s,
outperformingXGBoost(76.45%accuracy,175s)andRF(77.87%accuracy,529s). These
findingshighlightDNN’sabilitytobalanceaccuracyandcomputationalefficiency,making
itapromisingalternativeforreal-timechurnpredictionintelecommunications.
These studies underscore the potential of feedforward and standard deep neural
network approaches to provide robust and efficient churn prediction solutions. At the
sametime,theyhighlighttheongoingneedtoimprovemodelinterpretabilitytoenhance
adoptionandusabilityinpracticalbusinessapplications.
7.6. NLP–BasedDLApproaches
NLP-baseddeeplearningapproachesrepresentaninnovativefrontierinchurnpredic-
tionbyleveragingunstructuredtextualdatatocomplementtraditionalnumericalinputs.
These methods harness advanced language models and RNNs to extract meaningful
insights from customer communications, enriching predictive analytics and enhancing
retentionstrategies. Thissectionhighlightsakeystudythatexemplifiesthepotentialof
NLP-drivenchurnprediction.
Ozan[74]offersauniqueperspectivebyapplyingNLPtechniquestoCRMdatafor
churnprediction.UtilizingwordembeddingsalongsideRNNs,thestudydemonstratesthat
textdata—suchascustomerfeedbackandserviceinteractions—canbeeffectivelyharnessed
topredictchurn. Thisapproachcomplementstraditionalstructureddatamethodsand
providesdeeperinsightsintocustomersentimentandbehaviour. Thefindingssuggestthat
NLP-drivenchurnpredictionmodelscouldbeparticularlybeneficialinindustrieswhere
customercommunicationiscriticalinshapingretentionstrategies.
7.7. RepresentationandFeatureInteractionApproaches
Representationandfeatureinteractionapproacheshaveemergedaspromisingstrate-
giestoenhancechurnpredictionbycapturingcomplexrelationshipswithincustomerdata.
These methods address limitations in traditional deep neural networks, particularly in
handlinghigh-orderfeatureinteractionsandcategoricalvariables. Thissectionreviews
keystudiesthatleverageadvancedembeddingtechniquestoimprovepredictiveaccuracy
andinterpretabilityinchurnmodeling.
Tangetal.[75]introduceaFeatureInteractionNetwork(FIN)designedtoovercome
challengesstandarddeepneuralnetwork-basedchurnmodelsface. Traditionalmodels
oftenstruggletocapturehigh-orderfeatureinteractionsandeffectivelyhandleone-hot
encodedcategoricalfeatures. FINintegratestwokeycomponentstoaddressthis: anentity
embedding network to capture meaningful feature representations and a factorization
machine network with sliding windows to enhance feature interactions. Experimental

Mach.Learn.Knowl.Extr.2025,7,105 29of38
evaluations on four public datasets demonstrate that FIN outperforms state-of-the-art
models by effectively capturing complex dependencies in customer data. This study
underscorestheimportanceoffeatureinteractionmodelinginchurnprediction,offeringa
robustframeworkforleveragingstructuredcustomerdatainpredictiveanalytics.
Inacomplementaryapproach,Cenggoroetal.[76]developaDL-basedvectorembed-
dingmodeltailoredforchurnpredictioninthetelecommunicationsindustry. Thismodel
not onlyemphasizes predictive accuracybut alsoenhances interpretability. Themodel
enablesprecisedifferentiationbetweenloyalandchurn-pronecustomersbyleveraging
vector embeddings to represent customer behaviour in a discriminative feature space.
ExperimentalresultsindicatethatthemodelachievesanF1scoreof81.16%,demonstrat-
ing strong predictive performance. Additionally, cluster similarity analysis and t-SNE
visualizationsconfirmthatthelearnedrepresentationsarehighlyseparable,reinforcing
themodel’seffectiveness. Thisstudyhighlightsthepotentialofvectorembeddingsasa
powerfultoolforchurnmodeling,equippingtelecomproviderswithactionableinsights
forcustomerre-engagementandretention.
Thesestudiesillustratehowembeddingandfeatureinteractiontechniquescansignifi-
cantlyimprovechurnpredictionbycapturingnuancedrelationshipswithincustomerdata.
By enhancing both predictive performance and interpretability, these approaches offer
valuabletoolsfordevelopingproactiveandtargetedretentionstrategiesincompetitive
industries. DeeplearningarchitecturessuchasCNNs,RNNs,andattention-basedmodels
excelatcapturingtemporaldynamicsandcomplexfeatureinteractions,oftenachieving
superior predictive accuracy. Their main drawbacks are higher computational cost, re-
lianceonlargedatasets,andreducedinterpretability,whichcanlimitadoptioninbusiness
contextsrequiringtransparency.
In summary, machine learning and deep learning offer complementary strengths
forchurnprediction. MLtechniquesaregenerallyeasiertointerpret,fastertotrain,and
lessresource-intensive, makingthemsuitableforbusinesssettingswheretransparency
and efficiency are critical. In contrast, DL models are well-suited to high-dimensional,
sequential,andunstructureddata,wheretheirabilitytolearncomplexpatternscanleadto
superiorpredictiveaccuracy. Therefore,thechoicebetweenMLandDLdependsnotonly
ondatacharacteristicsbutalsoonpracticalrequirementssuchasinterpretability,scalability,
andcomputationalresources.
Theincludedstudies(n=61)weresynthesizednarrativelytohighlightmethodological
trends,datasetusage,andreportedperformancemetrics(seeTables1and2). Noformal
riskofbiasassessment,reportingbiasassessment,orcertaintyofevidenceassessment(e.g.,
usingGRADE)wasconducted,asthereviewfocusedonmethodologicalanalysisrather
thanquantitativesynthesis. Duetosubstantialheterogeneityinstudydesigns,datasets,
andevaluationprotocols,meta-analysiswasnotfeasible. Consequently,noinvestigations
ofheterogeneity,subgroupanalyses,sensitivityanalyses,orcertaintyassessmentswere
performed,andnoresultswerepresentedfortheseitems.
8. Discussion
8.1. LinkingFindingstoResearchQuestions
ToprovideadirectresponsetotheresearchquestionsoutlinedintheIntroduction,we
summariseourfindingsbelowabouteachquestion:
RQ1: What are the predominant ML and DL approaches used in customer churn
prediction, and how have these methodologies evolved over time? Our synthesis
(Sections6and7,Tables1and2)showsthatensemble-basedMLtechniques—particularly
boostingmethodssuchasXGBoost,LightGBM,andCatBoost—remainthemostwidely
adoptedacrossindustries,withdecisiontreesandrandomforestsalsofrequentlyusedas

Mach.Learn.Knowl.Extr.2025,7,105 30of38
interpretablebaselines. LSTMs,CNNs,andattention-basedarchitectureshavebeenwidely
adoptedintheDLdomain,particularlyforsequentialandunstructureddatasets. While
hybridapproachesexist,mostcombinealgorithmswithinthesameparadigm(ML–MLor
DL–DL)ratherthanintegratingMLwithDL.From2020to2024,therehasbeenanapparent
increaseintheadoptionofexplainableAItechniques,adaptivelearningstrategies,and
profit-driven evaluation metrics, reflecting a gradual shift toward models that balance
predictiveperformancewithinterpretabilityandbusinessrelevance.
RQ2: Howdodifferentpredictivemodelscompareintermsofaccuracy,adaptability,
andinterpretabilityacrossindustries? Duetotheheterogeneityofdatasets,churndefini-
tions,featuresets,andevaluationprotocols,directcross-studyperformancerankingisnot
feasible. Nonetheless,specifictrendsareevident. Boosting-basedMLmodelsconsistently
achievestrongpredictiveperformanceonstructureddatasetsbutmaybelesseffectiveat
modellingtemporaldependenciesthansequentialDLarchitectures. LSTMsandCNNsex-
celatcapturingbehaviouralandtemporalpatternsbutoftenrequiregreatercomputational
resources and exhibit reduced interpretability. Efforts to improve adaptability include
applyingonlinelearning,reinforcementlearning,andtransferlearning,althoughthese
remainlimitedinreal-worlddeployments. Regardinginterpretability,traditionalMLmeth-
odsofferinherenttransparency,whileDLmethodsbenefitfrompost-hocexplainability
toolssuchasSHAP,LIME,andattentionmechanisms.
RQ3: Whatarethesignificantchallengesandlimitationsinexistingchurnprediction
research,andwhatfuturedirectionscouldaddressthem? Ourreviewidentifieskeychal-
lenges, including class imbalance, reliance on static datasets, limited interpretability in
complexmodels,underutilisationofprofit-orientedmetrics,andalackofcross-domain
generalisability. Thesechallengesarecompoundedbydeploymentbarrierssuchasscala-
bilityandintegrationwithexistingCRMsystems. AsdiscussedinSection8.4,potential
solutionsincludeadvancedresamplingandcost-sensitivelearningtomitigateimbalance,
hybridmodelsthatcombineaccuracywithtransparency,adaptivedrift-awarelearning
methods,andembeddingbusiness-centricevaluationmetricsdirectlyintooptimisation
processes. Futureresearchshouldfocusondevelopingscalable,adaptive,andinterpretable
churnpredictionframeworksvalidatedonstandardisedbenchmarkdatasetstoensureboth
scientificrigourandreal-worldimpact.
8.2. ChallengesandLimitations
DespitesignificantadvancementsinMLandDLforchurnprediction,severalchal-
lengeshinderreal-worldimplementation. Oneofthemostpersistentissuesisclassim-
balance, where the number of churners in datasets is significantly smaller than that of
non-churners. This imbalance often biases models toward the majority class, reducing
theireffectivenessinidentifyingat-riskcustomers. Whileresamplingtechniquesandcost-
sensitivelearninghavebeenproposedassolutions,theycanleadtooverfittingorincreased
computationalcosts.
Anothermajorchallengeliesinfeatureengineeringanddatarepresentation. Many
modelsrelyonstructuredtransactionaldata, yetcustomerinteractionsinvolvediverse
data sources such as call logs, social media activity, and customer support interactions.
Integratingandextractingmeaningfulfeaturesfromsuchheterogeneousdataremainsa
complextask. DLmodelscanautomatefeatureextraction,butoftenrequireextensivedata
preprocessingandsignificantcomputationalresources.
Modelinterpretabilityisanothercriticalconcern,especiallywithDLmodels. While
traditionalMLtechniquessuchasDTsandlogisticregressionprovidehuman-readable
decisionrules,neuralnetworksandensemblemodelsfunctionasblackboxes,makingit
difficultforbusinessestotrusttheirpredictions. ExplainableAItechniques,suchasSHAP

Mach.Learn.Knowl.Extr.2025,7,105 31of38
andattentionmechanisms,havebeenintroducedtoaddressthisissue,buttheyarenotyet
widelyadoptedinreal-worldchurnpredictionsystems.
Furthermore, customerbehaviourisdynamic, andmanychurnpredictionmodels
struggletoadapttoevolvingpatternsovertime. Conceptdrift—wherecustomerprefer-
ences,engagementlevels,andchurnriskschange—challengesmodelstrainedonhistorical
data. Adaptivelearningtechniques,suchasonlinelearningandreinforcementlearning,
offerpotentialsolutionsbutrequirecontinuousretraining,makingthemresourceintensive.
Finally,thereisadisconnectbetweenacademicevaluationmetricsandbusinessimpact.
Many studies assess model performance using accuracy, F1-score, and AUC-ROC, but
thesedonotnecessarilytranslatetoactionablebusinessdecisions. Profit-drivenevaluation
metrics,whichfactorinthecostofretentioneffortsversuslostrevenuefromchurners,are
stillunderexploredinresearch. Bridgingthisgapisessentialfordevelopingmodelsthat
providetangiblebusinessvalue.
Addressingthesechallengeswillrequirefurtheradvancementsinadaptivemodeling,
explainabilitytechniques,andprofit-awarechurnprediction. Asbusinessescontinuetoin-
vestindata-drivenretentionstrategies,futureresearchshouldfocusondevelopingscalable,
interpretable,andbusiness-alignedsolutionstoimprovechurnpredictionoutcomes.
Beyond the methodological challenges discussed above, this review and the body
ofevidencesynthesizedhaveadditionallimitationsworthnoting. Thebodyofevidence
synthesizedinthisreviewmaybesubjecttoseverallimitations. First,theincludedstud-
iesexhibitedsubstantialheterogeneityindatasets,modelingobjectives,andevaluation
metrics,complicatingdirectcomparisonsacrossstudies. Second,manystudiesreliedon
proprietarydatasetswithlimitedtransparency,potentiallyrestrictingthegeneralizability
oftheirfindings. Third,publicationandreportingbiasesmaybepresent,asstudieswith
positiveresultsaremorelikelytobepublishedinpeer-reviewedoutlets. Finally,thelackof
standardizedevaluationprotocolsacrossstudieshinderstheestablishmentofconsistent
benchmarksforchurnpredictionperformance.
Moreover,thisreviewalsohasinherentlimitationsinitsprocesses. Thesearchstrategy
waslimitedtoEnglish-languagepeer-reviewedstudies,whichmayhaveexcludedrelevant
researchpublishedinotherlanguagesorgreyliterature. Althoughthereviewadheredto
PRISMAguidelinesandinvolvedtworeviewerscollaborativelyscreeningandextracting
data,noformalriskofbiasorcertaintyassessments(e.g.,ROBIS,GRADE)wereperformed,
astheprimaryfocuswasonmethodologicaltrendsratherthanquantitativeeffectestimates.
Additionally, using a narrative synthesis, while appropriate given the heterogeneity of
studies,maybelessrobustthanmeta-analyticapproachesforaggregatingevidence.
8.3. IdentifiedGapsinReviewedResearch
DespitetheextensiveadvancementsinMLandDLforcustomerchurnprediction,
severalgapspersistinthereviewedresearch,highlightingareasthatrequirefurtherexplo-
ration. Oneofthemostnotablegapsisthelimitedemphasisonreal-worlddeployment
challenges. Whilemanystudiesfocusonimprovingmodelaccuracyandrobustness,fewer
address the practical aspects of implementing these models in business environments.
Issuessuchasscalability,computationalefficiency,andintegrationwithexistingCRMsys-
temsremainunderexplored. Researchintolightweight,efficient,andreal-timedeployable
solutionsisessentialsincemanyorganizationslackthecomputationalinfrastructureto
supportcomplexDLmodels.
Anothersignificantgapisthelackoffocusonmodelinterpretabilityandexplainability.
WhileDLapproaches,particularlyRNNs,CNNs,andtransformers,haveshownimproved
predictiveperformance,theirblack-boxnaturelimitstheiradoptioninbusinesssettings
wheretransparencyiscrucial. AlthoughtechniqueslikeSHAPandLocalInterpretable

Mach.Learn.Knowl.Extr.2025,7,105 32of38
Model-AgnosticExplanations(LIME)havebeenintroduced,theyarenotwidelyintegrated
intochurnpredictionmodels. Futureresearchshouldprioritisethedevelopmentofinher-
entlyinterpretablemodelsorhybridapproachesthatbalanceaccuracywithtransparency
tofacilitatebetterdecision-makingincustomerretentionstrategies.
Additionally,mostexistingstudiesrelyonstaticdatasets,whichfailtoaccountfor
thedynamicnatureofcustomerbehaviour. Conceptdrift—wherecustomerengagement
patterns and churn drivers change over time—poses a significant challenge for model
generalization. Whilesomestudiesexploreadaptive, reinforcement, oronlinelearning
techniques, their practical adoption remains limited. Future research should focus on
developingadaptiveandself-learningmodelsthatcontinuouslyupdatebasedonevolving
customerdata,ensuringsustainedpredictiveperformanceovertime.
Anothergapisthelackofcross-domaingeneralizationinchurnpredictionmodels.
Manystudiesdevelopmodelstailoredtospecificindustries,suchastelecommunications
orbanking,butdonottesttheirapplicabilityacrossdifferentsectors. Giventhatcustomer
behaviour varies significantly across domains, future research should explore domain
adaptationtechniquesandtransferlearningtoimprovemodelgeneralizability. Thiswould
enablebusinessesindifferentsectorstoleveragechurnpredictionmethodologieswithout
extensiveretraining.
Afurthergapinthereviewedliteratureconcernsfairness,ethics,andbiasmitigation,
which remain largely absent from churn prediction research. Although fairness-aware
algorithms,biasauditing,andresponsibleAIframeworksareincreasinglydiscussedinthe
broadermachinelearningfield,veryfewstudiesapplytheseconsiderationstocustomer
churn. Thisomissionissignificantbecausebiasedmodelsmayunintentionallydisadvan-
tage certain customer groups, leading to unequal treatment in retention strategies and
exposingbusinessestoreputationalorregulatoryrisks. Futureresearchshouldtherefore
emphasize fairness-aware model design, transparent reporting of potential biases, and
theintegrationofbiasmitigationstrategies. Addressingtheseissueswouldensurethat
churnpredictionmodelsareaccurate,profitable,equitable,trustworthy,andalignedwith
emergingstandardsforresponsibleAI.
Finally,profit-drivenevaluationmetricsremainunderutilizedinthereviewedliter-
ature. While traditional metrics such as accuracy, F1-score, and AUC-ROC are widely
reported,theydonotfullycapturethebusinessimplicationsofchurnprediction. Fewstud-
iesincorporateprofit-basedmetricslikeExpectedMaximumProfitforCustomerChurn,
which consider the financial impact of retention strategies. Further research is needed
todevelopmodelsthatalignmorecloselywithbusinessgoals,optimizingforpredictive
performance,cost-effectiveness,andrevenuemaximization.
Addressing these gaps will require a multi-faceted research approach, integrating
interpretability,adaptivelearning,cross-domainvalidation,andbusiness-centricevaluation
intofuturechurnpredictionmodels. Bybridgingthesegaps,thefieldcanadvancetoward
more practical, transparent, and financially viable solutions for churn management in
real-worldapplications.
8.4. TrendDirections
Analyzingpublicationtrendsinchurnpredictionresearchover2020–2024revealsa
clearshifttowardmoreadvancedMLandDLtechniques. IEEEhasconsistentlyledinpub-
licationvolume,indicatingastrongresearchfocuswithinengineeringandcomputational
disciplines. WhiletraditionalMLtechniquessuchasDTsandlogisticregressionremain
widelyused,boostingmethodsandensemblelearninghavesteadilygrown,reflectingan
industrypreferenceforrobustandinterpretablemodels.

Mach.Learn.Knowl.Extr.2025,7,105 33of38
Inrecentyears,DLapproaches,particularlyRNNs,CNNs,andtransformers,have
gainedtraction,especiallyindomainsdealingwithcomplexsequentialandunstructured
data, such as telecommunications and banking. Adopting hybrid ML-DL models also
suggestsanincreasinginterestincombiningthestrengthsofmultipleparadigmstoimprove
predictiveaccuracy.
Another notable trend is the growing importance of explainability and business-
alignedevaluationmetrics. Whileearlystudiesprioritisedaccuracy-basedbenchmarks,
more recent research integrates profit-driven evaluation methods, addressing the gap
betweenacademicperformancemetricsandreal-worldapplicability.
Thefieldwilllikelyseefurtheradvancementsinadaptivelearningtechniques,rein-
forcementlearningforchurnmanagement,andintegrationofmulti-modaldatasources.
ThecontinuedevolutionofMLandDLforchurnpredictionindicatesashifttowardmodels
thataremoreaccurate,transparent,cost-effective,anddynamicallyadaptabletochanging
consumerbehaviours.
8.5. PotentialSolutiontotheCurrentChallenges
Our review identifies several persistent challenges in customer churn prediction,
eachofwhichhasbeenaddressedintheliteraturethroughvarioustechnicalapproaches.
One of the most prevalent is class imbalance, where the proportion of churners is far
smallerthanthatofnon-churners. Beyondconventionaloversamplingandundersampling
techniques, more advanced strategies such as Synthetic Minority Oversampling with
EditedNearestNeighbors(SMOTE-ENN)andAdaptiveSyntheticSampling(ADASYN)
have demonstrated improved representation of the minority class. Some studies have
combinedtheseresamplingmethodswithensemblelearning,whileothershaveadopted
cost-sensitivelearningframeworksthatincorporatemisclassificationcostsdirectlyintothe
model’soptimisationprocess. Thesecost-sensitiveapproachesensurethatmodeltraining
reflectstherealfinancialimplicationsofpredictionerrors,whichisparticularlyimportant
inretention-focusedapplications.
Modelinterpretabilityisanothermajorchallenge,especiallyasdeeplearningarchitec-
turesbecomeincreasinglycomplex. Severalstudieshaveappliedposthocexplainability
techniques such as Shapley Additive Explanations (SHAP), Local Interpretable Model-
agnosticExplanations(LIME),andcounterfactualexplanationmethodstoprovideaclearer
understandingofmodelbehaviour. Othershaveexploredinherentlyinterpretablealter-
natives, including sparse linear models and rule-based ensemble methods, which may
bettersuitdomainswheretransparencyiscriticalforregulatorycomplianceorbuilding
stakeholdertrust. Arecurringtrade-offinchurnpredictionresearchisthechoicebetween
interpretableMLmodelsandmorecomplexDLarchitectures. Interpretablemethodssuch
asdecisiontrees,logisticregression,andrule-basedensemblesremainhighlysuitablein
businesscontextswheretransparency,regulatorycompliance,andeaseofcommunication
withnon-technicalstakeholdersarecritical. Thesemodelsallowdecision-makerstotrace
predictionsbacktocustomerattributesanddesigntargetedretentionstrategies.Bycontrast,
DLmodels—includingLSTMs, CNNs, andTransformer-basedarchitectures—aremore
effectiveforhigh-dimensional,unstructured,orsequentialdata,wherepredictiveaccuracy
andcapturingcomplexbehaviouralpatternsoutweightheneedforinterpretability. Guid-
anceforpractitionersthereforedependsoncontext: interpretableMLispreferablewhen
accountabilityandactionableinsightsareparamount,whereasDLapproaches—including
LSTMs,CNNs,andTransformer-basedarchitectures—aremoreappropriatewhentherich-
nessandcomplexityofthedatademandadvancedrepresentationlearningandpredictive
accuracy.

Mach.Learn.Knowl.Extr.2025,7,105 34of38
The problem of concept drift, where customer behaviours and market conditions
evolveovertime,hasalsoreceivedgrowingattention. TheOptimisedTwo-SidedCumu-
lativeSumChurnDetector(OTCCD)integratesdriftdetectionwithadaptivelearningto
update models as data distributions change. Transfer learning and domain adaptation
techniqueshavelikewisebeenproposedtoenablemodelstoreuseknowledgefromearlier
datawhileadaptingtonewpatternswithminimalretraining. Thesestrategiesareparticu-
larlyrelevantinindustrieswherechurndeterminantsshiftrapidlyduetotechnologicalor
competitivechanges.
Finally,thelimitedadoptionofprofit-orientedevaluationmetricsremainsamissed
opportunityforaligningmodelperformancewithbusinessobjectives. Metricssuchasthe
ExpectedMaximumProfitforCustomerChurn(EMPC)andothercost–benefitframeworks
allowforadirectassessmentoftheeconomicimpactofretentionstrategies. Severalstudies
have shown that embedding these metrics into the optimisation process can produce
predictive and financially effective models rather than using them solely for post hoc
evaluation.
Thesesolutionsshowthatthechallengesinchurnpredictionarenotinsurmountable.
Manymethodologicaltoolsexisttoaddressimbalance,improveinterpretability,adaptto
shiftingdatadistributions,andincorporatebusinessvalueintoevaluation. Bydrawing
attentiontotheseapproaches,ourreviewaimstoencouragefutureworkthatadvancesthe
technicalstateoftheartandensuresthatchurnpredictionmodelsdeliveractionableand
economicallymeaningfuloutcomes.
9. ConclusionsandFutureResearchDirections
Customerchurnpredictionhasundergonerapidmethodologicalevolutioninrecent
years, with machine learning and deep learning techniques now central to identifying
at-riskcustomersandguidingretentionstrategies. Inthissystematicreview,weexamined
240peer-reviewedstudiespublishedbetweenJanuary2020andDecember2024,applyinga
PRISMA-guided,two-phasemethodology.Thefirstphaseprovidedabibliometricmapping
ofthefield, whiletheseconddeliveredadetailedsynthesisof61studiesmeetingstrict
novelty and contribution criteria. This dual approach enabled us to capture both the
breadthanddepthofrecentadvancesinchurnpredictionresearch.
Our findings reveal a strong preference for ensemble learning and advanced ML
techniquessuchasgradientboosting(XGBoost,LightGBM,CatBoost),decisiontrees,and
randomforests,alongsideagrowingadoptionofDLarchitectures,particularlyLSTMs,
CNNs,andattention-basedmodels. Thesemethodsareincreasinglyappliedtocapturecus-
tomerdata’stemporaldynamicsandbehaviouralpatterns. Hybridmodellingapproaches
arealsoexplored,thoughmostcombinedifferentalgorithmswithinthesameparadigm
(ML–MLorDL–DL)ratherthanintegratingMLwithDL.WhileDLmodelsoftenachieve
superiorpredictivepower,thiscomesattheexpenseofhighercomputationaldemandsand
reducedinterpretability;conversely,traditionalMLmodelstendtobemoreinterpretable
andcomputationallyefficientbutmayunderperformwithhigh-dimensionalorcomplex
datasets. Efforts to bridge this gap through explainable AI tools such as SHAP, LIME,
and attention mechanisms are promising but remain underrepresented in operational
deployments.
Severalpersistentchallengesemergedfromouranalysis. Classimbalancecontinues
tobiasmodelperformancetowardmajorityclasses,andmanymodelsaretrainedonstatic
datasets that do not reflect evolving customer behaviours, making them susceptible to
concept drift. Adaptive learning strategies and real-time model updating are still rare
in practice. Moreover, accuracy-oriented metrics dominate evaluation, with relatively
fewstudiesintegratingprofit-drivenmetricssuchastheEMPC,despitetheircloseralign-

Mach.Learn.Knowl.Extr.2025,7,105 35of38
mentwithbusinessobjectives. Inaddition,fairness,ethics,andbiasmitigationrepresent
importantbutunderexploredprioritiesinchurnpredictionresearch.Incorporatingfairness-
awaremodellingandtransparentreportingpracticeswillbeessentialtoensurethatfuture
solutionsarenotonlytechnicallyrobustandbusiness-alignedbutalsosociallyresponsible.
Addressingthesegapspresentscleardirectionsforfutureresearch. Thereisaneed
for adaptive churn prediction frameworks that can dynamically update to account for
behavioural and market changes, ideally incorporating automated drift detection and
incremental learning. Integrating inherently interpretable models and robust post hoc
explainabilitytechniquesshouldbeprioritisedtoimprovetransparencyandusertrust,
especiallyinregulatedindustries. Researchersshouldalsoexploremulti-modalapproaches
thatcombinestructured,unstructured,andnetwork-baseddatatocapturericherrepre-
sentationsofcustomerbehaviour. Finally,adoptingstandardisedbenchmarkdatasetsand
incorporatingbusiness-alignedperformancemetricsduringtrainingandevaluationwould
enablefairercomparisonsacrossstudiesandensurethatpredictivemodelsdelivertangible
valueinreal-worldretentionstrategies.
Bycombiningbibliometricinsightswithastructuredmethodologicalsynthesis,this
reviewprovidesacomprehensive,up-to-datemapofchurnpredictionresearch. Itoffers
concrete guidance for developing the next generation of adaptive, interpretable, and
business-alignedmodelsthatcanbedeployedeffectivelyinreal-worldcontexts.
AuthorContributions:M.I.:Conceptualization;Investigation;Methodology;Projectadministration;
Resources; Software; Validation; Visualization; Writing—originaldraft. M.J.: Conceptualization;
Investigation; Methodology;Resources; Validation. A.B.: Methodology; Supervision; Validation;
Writing—review&editing.H.R.A.:Supervision;Writing—review&editing.Allauthorshaveread
andagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenocompetinginterests.
References
1. Ahn,J.;Hana,S.-P.;Lee,Y.-S.Customerchurnanalysis:Churndeterminantsandmediationeffectsofpartialdefectioninthe
Koreanmobiletelecommunicationsserviceindustry.Telecommun.Policy2006,30,552–568.[CrossRef]
2. Xiaoling,S.;Ye,Y.KnowledgeDiscovery:Methodsfromdataminingandmachinelearning.Soc.Sci.Res.2023,110,102817.
3. Imani,M.;Arabnia,H.R.Hyperparameteroptimizationandcombineddatasamplingtechniquesinmachinelearningforcustomer
churnprediction:Acomparativeanalysis.Technologies2023,11,167.[CrossRef]
4. Imani,M.; Ghaderpour,Z.; Joudaki,M.; Beikmohammadi,A.TheImpactofSMOTEandADASYNonRandomForestand
AdvancedGradientBoostingTechniquesinTelecomCustomerChurnPrediction.InProceedingsofthe202410thInternational
ConferenceonWebResearch(ICWR),Tehran,Iran,24–25April2024.
5. Imani,M.;Beikmohammadi,A.;Arabnia,H.R.ComprehensiveAnalysisofRandomForestandXGBoostPerformancewith
SMOTE,ADASYN,andGNUSUnderVaryingImbalanceLevels.Technologies2025,13,88.[CrossRef]
6. Lemmens,A.;Gupta,S.Managingchurntomaximizeprofits.Mark.Sci.2020,39,956–973.[CrossRef]
7. Joudaki,M.;Imani,M.;Esmaeili,M.;Mahmoodi,M.;Mazhari,N.PresentingaNewApproachforPredictingandPreventing
Active/DeliberateCustomerChurninTelecommunicationIndustry.InProceedingsoftheInternationalConferenceonSecurity
andManagement(SAM).TheSteeringCommitteeoftheWorldCongressinComputerScience,ComputerEngineeringand
AppliedComputing(WorldComp),LasVegas,NV,USA,18–21July2011.
8. Kamil,M.;Kopczewska,K.Customerchurninretaile-commercebusiness:Spatialandmachinelearningapproach.J.Theor.Appl.
Electron.Commer.Res.2022,17,165–198.[CrossRef]
9. Al-Najjar,D.;Al-Rousan,N.;Al-Najjar,H.Machinelearningtodevelopcreditcardcustomerchurnprediction. J.Theor. Appl.
Electron.Commer.Res.2022,17,1529–1542.[CrossRef]
10. Christou,V.;Tsoulos,I.;Loupas,V.;Tzallas,A.T.;Gogos,C.;Karvelis,P.S.;Antoniadis,N.;Glavas,E.;Giannakeas,N.Performance
andearlydroppredictionforhighereducationstudentsusingmachinelearning.ExpertSyst.Appl.2023,225,120079.[CrossRef]

Mach.Learn.Knowl.Extr.2025,7,105 36of38
11. Ajegbile,M.D.;Olaboye,J.A.;Maha,C.C.;Igwama,G.T.;Abdul,S.Theroleofdata-driveninitiativesinenhancinghealthcare
deliveryandpatientretention.WorldJ.Biol.Pharm.HealthSci.2024,19,234–242.[CrossRef]
12. Ahn,J.;Hwang,J.;Kim,D.;Choi,H.;Kang,S.Asurveyonchurnanalysisinvariousbusinessdomains. IEEEAccess2020,8,
220816–220839.[CrossRef]
13. Reichheld,F.F.;Teal,T.LoyaltyEffect:TheHiddenForceBehindGrowth,Profits,andLasting;HarvardBusinessSchoolPublications:
Brighton,MA,USA,1996;pp.352–354.
14. Geiler,L.;Affeldt,S.;Nadif,M.Asurveyonmachinelearningmethodsforchurnprediction. Int. J.DataSci. Anal. 2022,14,
217–242.[CrossRef]
15. Edvaldo,D.;Ojeme,B.;Daramola,O.Experimentalanalysisofhyperparametersfordeeplearning-basedchurnpredictioninthe
bankingsector.Computation2021,9,34.[CrossRef]
16. Höppner,S.;Stripling,E.;Baesens,B.;vandenBroucke,S.;Verdonck,T.Profitdrivendecisiontreesforchurnprediction.Eur.J.
Oper.Res.2020,284,920–933.[CrossRef]
17. Maldonado,S.;López,J.;Vairetti,C.Profit-basedchurnpredictionbasedonminimaxprobabilitymachines. Eur. J.Oper. Res.
2020,284,273–284.[CrossRef]
18. Janssens,B.;Bogaert,M.;Bagué,A.;VandenPoel,D.B2Boost:Instance-dependentprofit-drivenmodellingofB2Bchurn.Ann.
Oper.Res.2024,341,267–293.[CrossRef]
19. Wang,X.;Nguyen,K.;Nguyen,B.P.Churnpredictionusingensemblelearning.InProceedingsofthe4thInternationalConference
onMachineLearningandSoftComputing,HaiphongCity,Vietnam,17–19January2020;AssociationforComputingMachinery:
NewYork,NY,USA,2020.
20. Hemlata,J.;Khunteta,A.;Srivastava,S.Churnpredictionintelecommunicationusinglogisticregressionandlogitboost.Procedia
Comput.Sci.2020,167,101–112.[CrossRef]
21. Maretta,S.N.T.;Permai,S.D.Enhancedchurnpredictionmodelwithboostedtreesalgorithmsinthebankingsector.InProceedings
ofthe2021InternationalConferenceonDataScienceandItsApplications(ICoDSA),Online,6–7October2021.
22. Tianpei,X.;Ma,Y.;Kim,K.Telecomchurnpredictionsystembasedonensemblelearningusingfeaturegrouping.Appl.Sci.2021,
11,4742.[CrossRef]
23. Manohar,E.;Jenifer,P.;Nisha,M.S.;Benita,B.Acollectivedataminingapproachtopredictcustomerbehaviour.InProceedings
ofthe2021ThirdInternationalConferenceonIntelligentCommunicationTechnologiesandVirtualMobileNetworks(ICICV),
Tirunelveli,India,4–6February2021.
24. Ramesh,P.;Emilyn,J.J.;Vijayakumar,V.Hybridartificialneuralnetworksusingcustomerchurnprediction.Wirel.Pers.Commun.
2022,142,1695–1709.[CrossRef]
25. Usman-Hamza,F.E.;Balogun,A.O.;Capretz,L.F.;Mojeed,H.A.;Mahamad,S.;Salihu,S.A.;Akintola,A.G.;Basri,S.;Amosa,R.T.;
Salahdeen,N.K.Intelligentdecisionforestmodelsforcustomerchurnprediction.Appl.Sci.2022,12,8270.[CrossRef]
26. Saias, J.; Rato, L.; Gonçalves, T. An approach to churn prediction for cloud services recommendation and user retention.
Information2022,13,227.[CrossRef]
27. Ishrat,J.;Sanam,T.F.AnImprovedMachineLearningBasedCustomerChurnPredictionforInsightandRecommendationin
E-commerce.InProceedingsofthe202225thInternationalConferenceonComputerandInformationTechnology(ICCIT),Cox’s
Bazar,Bangladesh,17–19December2022.
28. Liu,R.;Ali,S.;Bilal,S.F.;Sakhawat,Z.;Imran,A.;Almuhaimeed,A.;Alzahrani,A.;Sun,G.Anintelligenthybridschemefor
customerchurnpredictionintegratingclusteringandclassificationalgorithms.Appl.Sci.2022,12,9355.[CrossRef]
29. Yogesh,B.;Fokone,R.T.Hybridapproachusingmachinelearningalgorithmsforcustomers’churnpredictioninthetelecommu-
nicationsindustry.Concurr.Comput.Pract.Exp.2022,34,e6627.
30. Fu,K.;Zheng,G.;Xie,W.Customerchurnpredictionforawebcastplatformviaavoting-basedensemblelearningmodelwith
Nelder-Meadoptimizer.J.Intell.Inf.Syst.2023,61,859–879.[CrossRef]
31. Mahayasa, A.I.N.; Wanchai, P. Customer Churn Prediction Using Weight Average Ensemble Machine Learning Model. In
Proceedingsofthe202320thInternationalJointConferenceonComputerScienceandSoftwareEngineering(JCSSE),Phitsanulok,
Thailand,28June–1July2023.
32. Khoh,W.H.;Pang,Y.H.;Ooi,S.Y.;Wang,L.Y.K.;Poh,Q.W.Predictivechurnmodelingforsustainablebusinessinthetelecommu-
nicationindustry:Optimizedweightedensemblemachinelearning.Sustainability2023,15,8631.[CrossRef]
33. Arshad,U.;Khan,G.;KhaledAlarfaj,F.;Halim,Z.;Anwar,S.Q-ensemblelearningforcustomerchurnpredictionwithblockchain-
enableddatatransparency.Ann.Oper.Res.2024.[CrossRef]
34. Venkatesh, S.; Jeyakarthic, M.Anoptimalgeneticalgorithmwithsupportvectormachineforcloudbasedcustomerchurn
prediction.InProceedingsofthe2020InternationalConferenceonSystem,Computation,AutomationandNetworking(ICSCAN),
Pondicherry,India,3–4July2020.

Mach.Learn.Knowl.Extr.2025,7,105 37of38
35. Saheed,Y.K.;Hambali,M.A.Customerchurnpredictionintelecomsectorwithmachinelearningandinformationgainfilter
featureselectionalgorithms.InProceedingsofthe2021InternationalConferenceonDataAnalyticsforBusinessandIndustry
(ICDABI),Online,25–26October2021.
36. Pustokhina,I.V.;Pustokhin,D.A.;Nguyen,P.T.;Elhoseny,M.;Shankar,K.Multi-objectiverainoptimizationalgorithmwith
WELMmodelforcustomerchurnpredictionintelecommunicationsector.ComplexIntell.Syst.2023,9,3473–3485.[CrossRef]
37. Mirabdolbaghi,S.;Mohammad,S.;Amiri,B.Modeloptimizationanalysisofcustomerchurnpredictionusingmachinelearning
algorithmswithfocusonfeaturereductions.Discret.Dyn.Nat.Soc.2022,2022,5134356.[CrossRef]
38. Al-Shourbaji,I.;Helian,N.;Sun,Y.;Alshathri,S.;AbdElaziz,M.Boostingantcolonyoptimizationwithreptilesearchalgorithm
forchurnprediction.Mathematics2022,10,1031.[CrossRef]
39. AlShourbaji,I.;Helian,N.;Sun,Y.;Hussien,A.G.;Abualigah,L.;Elnaim,B.Anefficientchurnpredictionmodelusinggradient
boostingmachineandmetaheuristicoptimization.Sci.Rep.2023,13,14441.[CrossRef]
40. Kurtcan,D.B.;Ozcan,T.Predictingcustomerchurnusinggreywolfoptimization-basedsupportvectormachinewithprincipal
componentanalysis.J.Forecast.2023,42,1329–1340.[CrossRef]
41. Ponnusamy,R.R.A.;Rana,M.E.;Manickavasagam,S.A.;Hameed,V.A.PSO-SVMbasedalgorithmforcustomerchurnprediction
inthebankingindustry. InProceedingsofthe2023IEEE6thInternationalConferenceonBigDataandArtificialIntelligence
(BDAI),Jiaxing,China,8–9July2023.
42. Koçog˘lu,F.Ö.;Özcan,T.Agridsearchoptimizedextremelearningmachineapproachforcustomerchurnprediction.J.Eng.Res.
2023,11,103–112.[CrossRef]
43. Ahmad,T.A.;Usman,M.Adaptivetelecomchurnpredictionforconcept-sensitiveimbalancedatastreams.J.Supercomput.2022,
78,3746–3774.
44. Adnan,A.;Adnan,A.;Anwar,S.Anadaptivelearningapproachforcustomerchurnpredictioninthetelecommunicationindustry
usingevolutionarycomputationandNaïveBayes.Appl.SoftComput.2023,137,110103.[CrossRef]
45. Lee,N.T.;Lee,H.C.;Hsin,J.;Fang,S.H.Predictionofcustomerbehaviorchangingviaahybridapproach.IEEEOpenJ.Comput.
Soc.2023,5,27–38.[CrossRef]
46. Shimaa,O.;Mahmoud,K.T.;Abdel-Fattah,M.A.Aproposedhybridframeworktoimprovetheaccuracyofcustomerchurn
predictionintelecomindustry.J.BigData2024,11,70.[CrossRef]
47. DeBock,K.W.;DeCaigny,A.Spline-ruleensembleclassifierswithstructuredsparsityregularizationforinterpretablecustomer
churnmodeling.Decis.Support.Syst.2021,150,113523.[CrossRef]
48. Mitravinda,K.M.;Shetty,S.Employeeattrition:Predictionanalysisofcontributoryfactorsandrecommendationsforemployee
retention.InProceedingsofthe2022IEEEInternationalConferenceforWomeninInnovation,Technology&Entrepreneurship
(ICWITE),Bangalore,India,1–3December2022.
49. Wang,X.;Xie,L.;Wang,H.;Xing,X.;Wan,W.;Wu,Z.;Ma,X.;Li,Q.DecipheringExplicitandImplicitFeaturesforReliable,
Interpretable;ActionableUserChurnPredictioninOnlineVideoGames.IEEETrans.Vis.Comput.Graph.2024,31,5990–6007.
[CrossRef]
50. Vo,N.N.;Liu,S.;Li,X.;Xu,G.Leveragingunstructuredcalllogdataforcustomerchurnprediction.Knowl.-BasedSyst.2021,212,
106586.[CrossRef]
51. Soumi,D.;Prabu,P.ARepresentation-BasedQueryStrategytoDeriveQualitativeFeaturesforImprovedChurnPrediction.IEEE
Access2023,11,1213–1223.[CrossRef]
52. Wang,A.X.;Chukova,S.S.;Nguyen,B.P.Data-centricaitoimprovechurnpredictionwithsyntheticdata.InProceedingsofthe
20233rdInternationalConferenceonComputer,ControlandRobotics(ICCCR),Shanghai,China,24–26March2023.
53. Babak,A.;Hosseini,S.H.UnveilingthePowerofSocialInfluence:AMachineLearningFrameworkforChurnPredictionwith
NetworkAnalysis.IEEEAccess2024,12,71271–71285.[CrossRef]
54. Nyashadzashe,T.;Sibanda,K.Realtimecustomerchurnscoringmodelforthetelecommunicationsindustry.InProceedingsof
the20202ndInternationalMultidisciplinaryInformationTechnologyandEngineeringConference(IMITEC),Kimberley,South
Africa,25–27November2020.
55. Tianyuan,Z.;Moro,S.;Ramos,R.F.Adata-drivenapproachtoimprovecustomerchurnpredictionbasedontelecomcustomer
segmentation.FutureInternet2022,14,94.[CrossRef]
56. Šimovic´, P.P.; Chen, C.Y.T.; Sun, E.W.Classifyingthevarietyofcustomers’onlineengagementforchurnpredictionwitha
mixed-penaltylogisticregression.Comput.Econ.2023,61,451–485.[CrossRef]
57. AbdElminaam,D.S.;Maged,M.;Mousa,M.K.;Younis,A.O.;Abdelsalam,M.S.;Hisham,Y.;Talaat,T.EmpTurnoverML:An
EfficientModelforEmployeeTurnoverandCustomerChurnPredictionUsingMachineLearningAlgorithms.InProceedingsof
the2023InternationalMobile,Intelligent;UbiquitousComputingConference(MIUCC),Cairo,Egypt,27–28September2023.
58. Jakob, R.; Lepper, N.; Fleisch, E.; Kowatsch, T. Predicting early user churn in a public digital weight loss intervention. In
ProceedingsoftheCHI’24:Proceedingsofthe2024CHIConferenceonHumanFactorsinComputingSystems,Honolulu,HI,
USA,11–16May2024.

Mach.Learn.Knowl.Extr.2025,7,105 38of38
59. Sikri,A.;Jameel,R.;Idrees,S.M.;Kaur,H.Enhancingcustomerretentionintelecomindustrywithmachinelearningdrivenchurn
prediction.Sci.Rep.2024,14,13097.[CrossRef][PubMed]
60. Roohi, S.; Relas, A.; Takatalo, J.; Heiskanen, H.; Hämäläinen, P. Predicting game difficulty and churn without players. In
ProceedingsoftheCHIPLAY‘20:ProceedingsoftheAnnualSymposiumonComputer-HumanInteractioninPlay,Online,2–4
November2020.
61. Zhu,B.;Qian,C.;Pan,X.;Chen,H.Atrajectory-baseddeepsequentialmethodforcustomerchurnprediction.InProceedingsof
the20205thInternationalConferenceonMachineLearningTechnologies,Beijing,China,19–21June2020.
62. Alboukaey,N.;Joukhadar,A.;Ghneim,N.Dynamicbehaviorbasedchurnpredictioninmobiletelecom.ExpertSyst.Appl.2020,
162,113779.[CrossRef]
63. Joy,U.G.;Hoque,K.E.;Uddin,M.N.;Chowdhury,L.;Park,S.B.Abigdata-drivenhybridmodelforenhancingstreamingservice
customerretentionthroughchurnpredictionintegratedwithexplainableAI.IEEEAccess2024,12,69130–69150.[CrossRef]
64. Beltozar-Clemente,S.;Iparraguirre-Villanueva,O.;Pucuhuayla-Revatta,F.;Zapata-Paulini,J.;Cabanillas-Carbonell,M.Predicting
customerabandonmentinrecurrentneuralnetworksusingshort-termmemory.J.OpenInnov.Technol.Mark.Complex.2024,10,
100237.[CrossRef]
65. Liu,Y.;Shengdong,M.;Jijian,G.;Nedjah,N.Intelligentpredictionofcustomerchurnwithafusedattentionaldeeplearning
model.Mathematics2022,10,4733.[CrossRef]
66. Jajam,N.;Challa,N.P.;Prasanna,K.S.;Deepthi,C.V.S.ArithmeticoptimizationwithensembledeeplearningSBLSTM-RNN-IGSA
modelforcustomerchurnprediction.IEEEAccess2023,11,93111–93128.[CrossRef]
67. Zhao,Y.;Shao,Z.;Zhao,W.;Han,J.;Zheng,Q.;Jing,R.Combiningunsupervisedandsupervisedclassificationforcustomer
valuediscoveryinthetelecomindustry:Adeeplearningapproach.Computing2023,105,1395–1417.[CrossRef]
68. Van-Hieu,V.Predictcustomerchurnusingcombinationdeeplearningnetworksmodel.NeuralComput.Appl.2024,36,4867–4883.
69. Muhammad,U.;Ahmad,W.;Fong,A.Designandimplementationofasystemforcomparativeanalysisoflearningarchitectures
forChurnprediction.IEEECommun.Mag.2021,59,86–90.[CrossRef]
70. Ebru,P.O.;Ozcan,T.Anoveldeeplearningmodelbasedonconvolutionalneuralnetworksforemployeechurnprediction.J.
Forecast.2022,41,539–550.
71. Saha,S.;Saha,C.;Haque,M.M.;Alam,M.G.R.;Talukder,A.Churnnet:Deeplearningenhancedcustomerchurnpredictionin
telecommunicationindustry.IEEEAccess2024,12,4471–4484.[CrossRef]
72. Setyo,A.A.Telecommunicationservicesubscriberchurnlikelihoodpredictionanalysisusingdiversemachinelearningmodel.In
Proceedingsofthe20203rdInternationalConferenceonMechanical,Electronics,Computer;IndustrialTechnology(MECnIT),
Medan,Indonesia,25–27June2020.
73. Małgorzata,P.-K.;Marfo,K.F.;Sulikowski,P.Multi-LayerPerceptronandRadialBasisFunctionNetworksinPredictiveModeling
ofChurnforMobileTelecommunicationsBasedonUsagePatterns.Appl.Sci.2024,14,9226.[CrossRef]
74. Ozan,S¸.Casestudiesonusingnaturallanguageprocessingtechniquesincustomerrelationshipmanagementsoftware.J.Intell.
Inf.Syst.2021,56,233–253.[CrossRef]
75. Tang,Q.;Xia,G.;Zhang,X.;Li,Y.Afeatureinteractionnetworkforcustomerchurnprediction.InProceedingsofthe202012th
InternationalConferenceonMachineLearningandComputing,Shenzhen,China,15–17February2020.
76. Cenggoro,T.W.;Wirastari,R.A.;Rudianto,E.;Mohadi,M.I.;Ratj,D.;Pardamean,B.Deeplearningasavectorembeddingmodel
forcustomerchurn.ProcediaComput.Sci.2021,179,624–631.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.