---
conversion_metadata:
  converted_at: "2026-07-20T15:11:19Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Charizanis et al.pdf"
  source_pdf_sha256: "cc32ae917790db26ddde679156cd53fa5144a2a31a4c22a3bc50c26dbee2599a"
  page_count: 35
  markdown_char_count: 123936
---

Review
Data-Driven Decision Support in SaaS Cloud-Based
Service Models
GerasimosCharizanis,EfthimiaMavridou,EleniVrochidou ,TheofanisKalampokasandGeorgeA.Papakostas*
MLVResearchGroup,DepartmentofInformatics,DemocritusUniversityofThrace,65404Kavala,Greece;
gecsari@cs.duth.gr(G.C.);emavridou@cs.duth.gr(E.M.);evrochid@cs.duth.gr(E.V.);tkalampo@cs.duth.gr(T.K.)
* Correspondence:gpapak@cs.duth.gr;Tel.:+30-2510-462321
Abstract: Software as a service (SaaS) is a major service model for delivering software
to end users through the cloud. SaaS platforms provide their users with cost-efficient,
flexibleandscalableservicesthatcanbeavailableondemand,anytime,andanywhere.
Moreover,SaaSempowerssoftwareproviderstoestablishrecurringrevenueandcreate
profitablebusinesses. However,SaaScanendurehighcustomerturnoverduetoreasons
suchasservingawiderangeofcustomers, intensecompetitionandrapidevolutionof
technology. Maintainingaregularcustomerbaseandkeepingusersengagediscrucialfor
thesurvivalofaSaaSbusiness. Thus,itiscrucialforSaaSproviderstoidentifyboththe
reasonsbehindusers’engagementandchurnoftheirapptowardstakingproperactionsto
retaintheminthelongterm. SaaSdataregardinguserbehavior,subscriptionsandsystem
performance can be utilized for deriving insights and identifying patterns to support
decision-makingforSaaSproviders. Tothisend,theaimofthissurveyistoreviewresearch
indata-drivendecisionsupportsystemsinSaaS,identifyingcurrentgapsandchallenges
andhighlightingdirectionsforfutureimprovementstowardsthedevelopmentofmore
efficientandintelligentsystems.
Keywords: softwareasaservice;churnprediction;userengagement;machinelearning;
usagemining
AcademicEditor:Miguel
García-Pineda
1. Introduction
Received:2May2025
Cloud computing is the dominant model for providing software and technology
Revised:29May2025
Accepted:6June2025 infrastructures nowadays. This approach enables access to computing resources and
Published:10June2025 applications without the need for hardware setup and maintenance. The main cloud
Citation: Charizanis,G.;Mavridou, service models are infrastructure as a service (IaaS), platform as a service (PaaS) and
E.;Vrochidou,E.;Kalampokas,T.; softwareasaservice(SaaS)[1].
Papakostas,G.A.Data-Driven TheIaaSmodelprovidesinfrastructureresourcesthroughthecloudsuchasstorage
DecisionSupportinSaaSCloud-Based
andcomputationalpower. Usersdonothavetoupdateandmaintaintheinfrastructure,yet
ServiceModels.Appl.Sci.2025,15,
theyareinchargeofsettingupoperatingsystems,softwareanddata[2]. Onthecontrary,
6508. https://doi.org/10.3390/
thePaaS modelalsoprovides thesoftware resources forcreating softwarein thecloud.
app15126508
Usersdonotmaintainthesoftwaredevelopmentenvironment,buttheyhavetowritetheir
Copyright:©2025bytheauthors.
owncode. Finally,theSaaSmodelprovidesready-to-usesoftwaresolutions[3],meaning
LicenseeMDPI,Basel,Switzerland.
thattheuserscanstartusingthesoftwarewithoutinstallation. Therefore,IaaSandPaaS
Thisarticleisanopenaccessarticle
distributedunderthetermsand usersaremainlydevelopersandITprofessionals,whileSaaSuserscanvarydependingon
conditionsoftheCreativeCommons thesolutionprovidedbytheSaaS.Forexample,aSaaSthatprovidesinvoicingsoftware
Attribution(CCBY)license mayhaveusersrangingfromvariousprofessions,e.g.,engineers,lawyers,etc. TheSaaS
(https://creativecommons.org/
modelistheleadingcloudcomputingmodelfordeliveringsoftwarenowadayssinceit
licenses/by/4.0/).
Appl.Sci.2025,15,6508 https://doi.org/10.3390/app15126508

Appl.Sci.2025,15,6508 2of35
enables software distribution without the need for installation and hardware setup [4].
Thus,userscanusethemeasilyandquickly,whilegenerallypayingbysubscriptioninstead
ofalargeamountupfront.
TheSaaSmodelenablessoftwareproviderstocreateprofitablebusinessesallowing
softwaredistributionthroughthecloudtomanyusers,simultaneously[5]. Moreover,the
subscription-basedbusinessmodelprovidesopportunitiesforstableincomestreams. Thus,
thesuccessofaSaaSmodelasabusinessheavilydependsonwhetheritmaintainsacore
userbase. Whenusersexperiencemeaningfulbenefitsfromasoftwaresolution,theyuseit
regularlyandforalongtime. EngagedusersarethesuperpowerofSaaSsincetheytendto
useitinthelongtermandwithminimumsupport,whiletheycouldpossiblysuggestitto
otherusers. Thecostofobtainingnewusersisgenerallymuchhigherthanretainingthe
onesthatalreadyexist[6]. Thus,SaaSbusinessesstrivetoincreaseuserengagementand
reduceuserchurn,i.e.,thepercentageofusersthatcanceltheirsubscriptions.
Recentindustryreportspointtoseveralgrowingchallengesthatmakestrong,data-
drivendecisionsupportsystemsmoreimportantthaneverforSaaScompanies. Onemajor
issueisthehighrateofcustomerchurn,shortlyaftercustomerssignup,whichiscommonly
observedwithnewartificialintelligence(AI)-poweredtools(https://www.paddle.com/
blog/saas-market-report-q1-2025,assessedon1June2025). Thisisparticularlyaproblem
intheB2Cmarket, whereuserbehaviorchangesquicklyandishardtopredict. Atthe
sametime,manySaaSbusinessesdonotpayenoughattentiontohowtheyadjusttheir
prices,eventhoughpricingcanhaveabigimpactonuserretention(https://www.omnius.
so/blog/saas-industry-report-2024, assessedon1June2025). Anotherchallengeisthe
riseofmulti-cloudandhybridsystems,wherecompaniesruntheirsoftwareacrossseveral
cloud platforms. This makes it harder to gather and analyze all of their data in one
place(https://www.fortunebusinessinsights.com/software-as-a-service-saas-market-10
2222, assessed on 1 June 2025). The growing use of AI in SaaS platforms introduces
new benefits, like automation and personalization. However, this also leads to higher
infrastructurecostsduetoexpensivecomputingresourceslikeGPUs,high-volumedata
usage, and the need for highly skilled professionals to build and maintain AI systems
(https://www.paddle.com/blog/saas-market-report-q1-2025,assessedon1June2025).
ThesetrendsintheSaaSindustryindicatethatSaaSprovidersfaceincreasinglycomplex
decisions. Asaresult,theroleofdata-drivendecisionsupportsystemsbecomescriticalin
helpingSaaSvendorsmakeinformed,timely,andcost-effectivechoices.
AtthecoreofmodernSaaSecosystems,vastamountsofdataaregenerated,regarding
userbehavior,subscriptionsandsystemperformance[7]. SaaSdatacanbeleveragedfor
derivinginsightsandidentifyingpatternstosupportdecision-makingforSaaSproviders.
Forexample,machinelearning(ML)algorithmscanbeemployedtocreatechurnprediction
modelsforuserchurnprediction[8]. Giventhatinformation,SaaSproviderscanactwitha
specificincentivetoreengagethoseusers. Tothisend,theaimofthissurveyistoreview
researchindata-drivendecisionsupportinSaaSapplications. Inparticular,thegoalofthis
workistoidentifyresearchthatutilizesdatatosupportSaaSvendorstowardsreducing
churnandincreasinguserengagement,satisfactionandloyalty.
Althoughrelatedworksarealreadypresentintheliterature[9–11],thisstudystands
outbyofferingacomprehensiveperspectiveonleveragingSaaSdatatosupportdecision-
makingforSaaSvendorstosustainuserloyaltyandsatisfaction. Unlikepriorresearchthat
oftenfocusesnarrowlyonspecifictaskssuchaschurnprediction,thisworkprovidesa
holisticexaminationofstrategiestomaintainastableuserbase. Specifically,thediverse
objectivesofexistingapproachesareanalyzed,asthevarietyofemployeddatasources,
and the comparative effectiveness of different machine learning methods on multiple
occasions.Moreover,thewaystheoutputsoftheseapproaches,rangingfromvisualizations

Appl.Sci.2025,15,6508 3of35
toactionableinsights,arepresentedtoSaaSvendorstofacilitatespot-ondecision-making,
arealsodiscussed.
Therestofthepaperisstructuredasfollows: Section2presentsrelatedworksand
highlightsthecontributionsofthispaper. Section3summarizestheresearchmethodol-
ogy, while Section 4 presents the results. Discussions and conclusions are provided in
Sections5and6,respectively.
2. RelatedWork
ThecurrentworkconstitutesascopingreviewofresearchtoassistSaaSvendorsin
decision-makingbasedonthedatathatSaaSbusinessesgenerate. Therefore,theaimisto
identifyresearcheffortsthatperformliteraturereviewsonthesamesubject. Tothebest
ofourknowledge,thereisnoexacttypeofreviewfoundintheliterature. However,there
areliteraturereviewsthatarerelatedtothesubject,yetwithdifferentfocus. Forexample,
theauthorsin[9]performedareviewonmachinelearningmethodsforchurnprediction
coveringtheyearsbetween2015and2023. Althoughtheirworkprovidedinsightsonthe
useofMLforchurnpredictionhighlightingthetrade-offsofdifferentMLmethods,the
focuswasonlyonchurnprediction,anditdidnotaddressotherusecasessuchasuser
segmentationorcustomerlifetimevaluepredictionwhicharecriticaltosupportbusiness
ownersondecision-making. Moreover,thereviewfocusedontelecommunications,finance
and online gaming industries, regardless of the type of businesses and the adoption of
cloud-based models and SaaS specifically. To this end, our work constitutes a review
tailoredtosupportbusinessesthatoperatebasedontheSaaScloudmodelprovidinga
moreholisticapproachbycoveringawiderangeofusecases,importanttoretainastrong
customerbase.
Similarly, the authors in [10] conducted a general review of decision analytics ap-
proachesforcloudcomputing. It’salsoworthnotingthattheirworkwaspublishedmore
than10yearsago, in2014, andthereforeitdoesnotcovercurrentresearchefforts. The
authorsfocusedondecisionsupportforcloudcomputingforproblemslikeserviceselection
andpricing,ratherthandiscussingdecisionsupportforuserretentionandengagement.
Moreover,therewasnodescriptionofthesystematicreviewresearchmethodologyandno
informationorstatisticsregardingthenumberofpapersincludedintheirreview.Moreover,
the authors considered papers with methods that were not data-driven, like heuristics
or ontology-based. The review presented in [11] addressed a broad range of different
topicsAI,ML,BusinessIntelligence(BI)andSaaSatahighlevelwithoutgoingintodetail.
Regardinguserbehavior,authorsdiscussedpredictionstrategiesandpersonalizationof
userexperience,however,withoutgoingintospecificinsightsandrecommendations. A
systematicreviewmethodologywasalsomissing.
Anotherpaper[5]publishedinthesameyear(2014)coveredthetechnicalchallenges
andperspectivesforSaaSsuchasmulti-tenancyandscalability. Thatreviewalsolackeda
researchmethodologyanddidnotmentionhowthereviewedapproacheswereselected.
Performance comparisons were not included, and only a qualitative analysis was per-
formed.Lastly,therewasnofocusonuserinteractionsubjectslikeuserretentionandchurn.
Finally,theresearchpresentedin[11]addressedAIadoptionforBIinSaaS.Althoughit
wasmentionedthataliteraturereviewwasconducted, only8paperswereincludedin
theiranalysis.
Tothisend,comparedtotheexistingbibliography,thecurrentwork:
• Presentsasystematicreviewprocess.
• Includesonlydata-drivenmethods.
• Presentsofperformancecomparisontosupportmodelselection.

Appl.Sci.2025,15,6508 4of35
• DiscussesofchallengestheSaaSvendorsfaceregardingmaintainingacoreuserbase
likechurn,userengagementanduserretention.
Moreover, the contributions of this work can be summarized in the following
distinctpoints:
• Acomprehensivereviewofresearchinitiativesaimingtosupportdecision-making
for SaaS providers, expanding beyond single-task approaches to address broader
strategicgoals.
• Anoverviewofvariousdatainputsutilizedacrossstudies,identifyingfrequentlyused
datasourcesandhighlightingcaseswheremultiplekindsofdatawereintegratedfor
morerobustinsights.
• Acomparativeevaluationofemployedmachinelearningtechniques,analyzingtheir
relativestrengths,weaknesses,andperformanceindifferentSaaSdecision-makingcontexts.
• Anoverviewofuser-facedoutputtypesproposedbyresearcherstohelpSaaSproviders
takeeffective,data-drivenactions.
• Asynthesisofbestpracticesandkeytakeawaysfromtheliterature,offeringactionable
recommendationsforenhancinguserretentionandensuringthelong-termsustain-
abilityofSaaSbusinessmodels.
3. ResearchMethodology
Theresearchquestionsthatweaimtoanswerinthissurveyarethefollowing:
RQ1: What is the main focus of the papers in the area of data-driven methods for
supportingdecision-makinginSaaS?
RQ2: Whatkindofdataisutilized?
RQ3: Aremachinelearningmethodsemployedandhoweffectivearethey?
RQ4: HowaretheresultspresentedtoSaaSproviderstosupportdecision-making?
ThesurveywasconductedfollowingthePRISMA-ScRmethodology.Theresearchwas
conductedusingtheScopusandScholarbibliographicdatabasesthatcontainpapersfrom
librarieslikeSpringer,Elsevier,IEEE,etc. Thefollowingquerywasposedon5March2025
toScopus:
(“webusagemining”OR“customersegmentation”OR“loganalysis”OR“churn”
OR“userengagement”OR“customerlifetimevalue”OR“userlifetimevalue”OR“user
segmentation”)AND“SaaS”ANDPUBYEAR>2013ANDPUBYEAR<2026.
Thisqueryreturned426results. Screeningwasperformedbyreadingthetitleand
abstract in order to identify the completely irrelevant ones. This process resulted in
147papers. Thesepapersweresearchedandretrievedinordertoreadthemthoroughly.
Duringthissecondscreeningphase,therewereexcludedallpapersthatwerenotrelevant
tooursubject. Relevancywasbasedonthreemainrules: papersshouldbeaboutSaaS,
decision-supportandbasedondata. Thus,theexcludedpapersofthesecondphasefall
intooneofthethreecategories:
• NotrelatedtoSaaS;
• AlthoughrelatedtoSaaStheywerenotaboutsupportingdecisions;
• Notdata-driven,theoretical.
Thisprocessresultedin22papersthatwereincludedinoursurvey. Asupplementary
search was conducted in Google Scholar using keywords like “churn prediction SaaS”,
“userengagementSaaS”and“userlifetimevalueSaaS”resultingin6morepapers. Thus,a
finallistof28paperswasformedthatwasanalyzedfurther.Figure1illustratestheresearch
processfollowed.

Appl.Sci.2025,15,6508 5of35
Figure1.PRISMAflowdiagram.
At this stage, it is important to acknowledge the limitations of this research. The
research was limited from 2014 to 2025, so as to cover a full range of 10 years, as well
as due to the fact that SaaS adoption began to rise mainly after 2014, where the main
volumeofliteraturewaslocated. However,thelatterdidnotaffectourresearchfindings,
since the main volume of the research was located after 2014 and especially from 2020
onwards. Moreover, the database coverage was limited to Scopus and Google Scholar.
Whileotherdatabasesalsoexist,suchasWebofScienceorPubMed,theuseofbothScopus
andGoogleScholarcouldimprovecoverageandreliability,astheybothcoverawiderange
ofpeer-reviewedsources.
4. Data-DrivenDecisionSupportinSaaS
4.1. MainFocus
TheSaaSmodelismainlyofferedbysubscriptionwhichisthemainsourceforrevenue
generationforsuch businesses. Havinga stronguser baseiscrucial fortheviabilityof
SaaSbusinesses. Therefore,itisveryimportantforSaaStomaintainasmallpercentageof
usersthatcanceltheirsubscriptions(churn). ForSaaSbusinesses,evenasmallreductionin
churncanleadtosignificantprofitgrowthandahealthierandlong-termbusiness. Forthis
reason,manyresearchersfocusonpredictingchurninSaaSbusinessesandonidentifying
thebestperformingmachinelearningalgorithmsforeachcase.
Figure2summarizestheresultsregardingRQ1. AscanbeseeninFigure1,mostof
thereviewedpapers(53.57%)focusedonchurnprediction. Thiscomesasnosurprisesince
highchurnratescannotsustainaSaaSbusinessmodel. Thechurnrateisthenumberof
usersthatleavetheSaaSdividedbythetotalnumberofusers. Churnpredictionrefersto
predictingifauserisabouttochurn.Theauthorsin[12,13]focusedonapplyingandtesting

Appl.Sci.2025,15,6508 6of35
variousalgorithmsfedwithusagedatatoevaluatetheirperformanceinchurnprediction,
inthecontextofSaaS,whileresearchpresentedin[8,14–17]followedthesameprinciple
butshiftedtheirfocustowardstheBusinesstoBusiness(B2B)SaaSbusinessmodel. All
thosestudiesaimedtopointoutkeyfeaturesthatchurningcustomerspossessandoffer
SaaSprovidersactionableinsightsforimprovingtheircustomerretentionstrategies.
Figure2.Mainfocusofthereviewedpapers(RQ1).
Further research on this topic included in [18,19] focused on comparing multiple
machine learning algorithms to figure out which one was best performing for churn
predictionintheSaaScloudservicemodel.Theauthorsin[18]developedachurnprediction
systemtopredictcustomerattritionforcloud-basedserviceproviders(CSPs),attempting
anearlyidentificationofcustomersatriskofcancelingsubscriptions. Churnpredictionin
CustomerRelationshipManagementsystems(CRM)usinghybridmachinelearningmodels
wasaddressedin[19]. Apartfromthecomparisonbetweenmachinelearningmethods,the
authorsin[20]chosetousemachinelearningtoanalyzeandmonitorcustomersatisfaction
from support tickets and predict whether a client is going to renew their cloud service
subscription. Accordingly,theresearchpresentedin[21]experimentedwiththecreation
andapplicationofahybridmachinelearningframeworkdesignedforreal-timeprediction
ofusereventsinSaaSproductssuchassubscriptioncancellation,userinteractions,and
taskabandonmentduringusersessions.
Severalresearcheffortsdealtwithpredictingchurnandimprovingretentionspecif-
icallyforonlinegamesbasedontheSaaSmodel. Thestrategyemployedin[22]aimed
toidentifychurnersinearlierstagesofamobilefreemiumgame,evenafterthetutorial
phase,usingminimalearly-stageuserdata,featuringaTransformer-basedarchitecture(FT-
Transformer)tailoredfortabulardata. Theresearchpresentedin[23]focusedonpredicting
playerchurnanddisengagementwithina14-daywindowinafreemiumonlinestrategy
gameusingmachinelearning. Specifically,itaimedtoidentifythemosteffectivemachine
learningtechniquesandlabelingapproachesforearlydetectionofplayersatriskofleav-
ingthegame, enablingproactiveretentionstrategies. In[23]theauthorsdistinguished
betweenchurn(permanentdeparture)anddisengagement(reducedactivity),providinga
comprehensivecomparisonofmethodstailoredtothegamingindustry. Theauthorsof[24]
extendedtheirresearchtoalargertimespan,focusingonimprovingchurnpredictionin
casualfreemiumgamesbycombiningsequential(temporal)andaggregated(static)data
usingdifferentneuralnetworkarchitectures. Theirstudyinvestigatedhowintegrating
these two types of data can enhance prediction accuracy compared to models that rely
solelyonsequentialoraggregateddatawhilealsoaddressingthechallengeofpredicting

Appl.Sci.2025,15,6508 7of35
churn in non-contractual contexts (for example in mobile games), where players could
leavewithoutexplicitsignals.
Additionally,theresearchconductedin[25]focusedonenhancingretentionanalysis
in freemium role-playing games (RPGs) by modeling players’ motivation, progression,
and churn. Particularly, it aimed to understand how in-game behaviors (engagement,
collaboration,andachievement)atdifferentlevelsinfluencedropoutrates,andhowthese
interdependencies could be leveraged to predict player retention more accurately. As
playerretentioninthevideogameindustryisthekeytoitsongoingprosperity,workin[26]
exploredhowvideogameoperatorscanretainplayersinsubscription-basedgamesby
dynamicallyadjustingthequalityofthegameovertime. Thestudydevelopedadynamic
programming model that considered players’ memory of past service experiences and
networkexternalities(thephenomenonwherethevalueorutilityofaproductorservice
increasesasmorepeopleuseit)todeterminetheoptimaldata-drivendecisionstomaximize
long-termprofits.
Inordertobetterunderstandandadapttoclients’needsinSaaSservicesitisimpor-
tanttocategorizethemintogroupstobeabletoprovidethempersonalizedattention. An
iterativemixed-methodapproachforcreatinguserpersonasinthecontextofB2BSaaS
productswaspresentedin[27]. Thatworkalsoaimedtodemonstratehowthegenerated
userpersonascouldbepracticallyappliedasanindicatortoimprovethedesign,develop-
ment,andprioritizationoffeaturesinaB2BSaaSproduct. Anotherresearchoncustomer
segmentationwaspresentedin[28],particularlyexploringhowbehavioralcustomerseg-
mentationandappusageanalysiscanbeleveragedtopredictcustomerinterestinpremium
subscriptionsandidentifykeyinfluencingfactorstoimprovesubscriptionconversionrates
formobileapps. Userconversionfromfreetrialstopaidsubscriptionswasthemainfocus
of[29],examininghowmarketinginteractions(ads,messages,emails,etc.) andtheirtype
ofcontentalongwithfree-trialusagebehaviorscouldinfluenceusers’decisions. Further
insightsregardingfreetrialswereshowcasedin[30]. Thestudyhighlightedtheimportance
of free trials as a customer acquisition strategy in the SaaS industry and analyzed how
customeracquisition,retentionandprofitabilitywereaffectedbythedurationoffreetrials
todiscovertheiroptimaldesign.
Establishingalong-termrelationshipwithcustomersrequireskeepingthemengaged
andsatisfiedwiththeservicestheyaregetting. Theauthorsin[31]examinedhowvisual
andfunctionalaspectsofuserinterface(UI)designcouldinfluenceuserexperience(UX).
Advancingfurtheronthesubjectofcustomerloyalty,theauthorsin[32]followedadata-
drivenapproachtodiscoveringthedeterminantsofcustomerloyaltyintheB2BSaaSindus-
try. Thatstudyexploredhowtransactionalandbehavioraldata(likeplatformengagement,
andcommunicationfrequency)couldbeleveragedtopredictcustomerloyaltywithout
relyingontraditionalsurveys. Theresearchpresentedin[33]proposedthedesignofan
adaptivenegotiationmechanismtoallowproviderstointeractwithclientsanddynamically
manageservicequality,usersatisfaction,andresourcecostsincloudenvironments.
Averyimpactfulfactorinkeepingcustomersfromchurningiswhethertheseindi-
vidualsdiscoverthe“ahamoment”andacknowledgethereturnontheirinvestmentin
SaaS services. The “aha moment” refers to the point when users understand the value
ofthesoftwareproduct,whichiscrucialforenablingcustomeractivationandretention.
Theauthorsof[34]focusedonidentifyingthe“ahamoment”ofB2BSaaScustomersusing
process mining techniques. Specifically, this study investigated how customers switch
fromtheactivationphasetotheretentionphaseintheAARRR(Acquisition,Activation,
Retention,Revenue,Referral)modelbyidentifyingandexaminingbehaviorpatternsof
clients. Inordertoprovidevaluetotheircustomers,customerfeedbackmustbetakeninto
consideration,sothatproviderscanofferamorepersonalizedexperienceandcatertotheir

Appl.Sci.2025,15,6508 8of35
clients’needs. Theresearchpresentedin[35]exploredstructuredapproachesforcollecting
andintegratingcustomerfeedbackinSaaScompaniesoperatingintheB2Bmarketand
waysofintegratingcustomerknowledgeintosoftwaredevelopmentprocesses.
SaaS pricing also takes its toll on user satisfaction as it affects SaaS users directly.
Thestudypresentedin[36], however, showcasedadata-drivenframeworkintegrating
real-timeusagetracking,machinelearningfordemandprediction,andcustomer-centric
billingadjustmentstooptimizerevenueforproviderswhileenhancinguserexperienceand
customerloyalty. AdditionalfactorsinfluencingusagecontinuanceinSaaSapplications,
particularlyaftertheinitialadoptionphaseweredemonstratedin[37],inanattemptto
improveuserretentionandreducechurnbyenhancingusagepenetration(thenumberof
usersactivelyengagingwiththesoftware).
Finally,anotherproblemthattheresearchaddressedwastheCustomerLifetimeValue
(CLV)prediction. CLVpredictionmodelspredictthefuturerevenuethatcustomersmay
generate. Theauthorsin[38]proposedanovelmachinelearningframeworkforpredicting
CLVinthecontextofB2BSaaScompaniesanddescribedseveralbusinessapplications
whereCLVpredictionswereusedtoenhancemarketingexpenditures,improveReturn
onInvestment(ROI),andprovideessentialinsightsformanagementdecision-makingin
thiscontext.
4.2. DataSources
InordertocompareandevaluatealgorithmsforpredictingchurninSaaSbusinesses,
researchers chose to utilize various types of data sources for their experiments. As per
theresearchquestionRQ2,themostcommoncategoryamongstudies[8,12–19]isusage
behavior data. All those studies incorporate some form of user interaction or system
activity logs like logins, sessions, file uploads, application usage, number of users and
actionsperformed.
Anothercommontypeofdatausedin[8,12–14,16,17]istransactionalandbusiness
metricsincludingmonetaryvalues(monthlycharges,totalexpenses,amountspent),sub-
scription status and billing information. Additionally, temporal data, contractual data
andcustomerlifecycleindicatorsappearedin[12,13,15,17–19]concerningcustomertenure,
daystoexpiry,subscriptionageandmonthlysnapshotsorobservationwindowswhilein
studies[8,16–19]customerdemographicsandattributeswerealsoutilized(companysize,
region,industry,onboardingstatusorbusinessage).
Theauthorsin[18]alsousedbillingandloyaltyprogramdatalikeloyaltyprogram
status and billing cycles. At last, customer support interaction data were used in [15]
(supporttickets,resolutiontimes)and[16](supportcaselogs)whilecustomersatisfaction
metricssuchasNetPromoterScore(NPS)andcallqualitywerespecificallyincludedin[17].
Furthermore,regardingchurnprediction,theapproachfollowedin[20]usedsupportand
subscriptionmetadatawhilethestudy[21]focusedonclickstreamdatacombinedwith
dynamicuserprofiles(subscriptionstatus,tenure,demographics).
Studiesthatfocusedonpredictingchurningamesfeaturingasubscriptionmodelas
in[22–24],sharedastrongemphasisoneventlogs,sessiondata,andgameplaybehavior
andchosetoutilizebehavioraldata(gameplayactions,tutorialengagement,sessionmetrics,
clicks,purchases,logins)todesigntheirchurnpredictingmodels.
Focusingonimprovingretentionoffreemiumonlinegames,thestudy[25]conducted
itsresearchbyutilizingplayerbehavioraldata(engagement,achievements,collaboration,
progress,dropouts),demographicandcontextualdata(genderofgamecharacters,geo-
graphiclocation,timeofplay),andsomegame-specificmetrics. Moreover,thedataused
in[26]wasderivedfromasimulateddatasetcontainingsyntheticdata(simulatedquality
levels,utilityfunctions,andcoststructures).

Appl.Sci.2025,15,6508
9of35
Datain[27]arederivedfromsurveys,interviewsandwebbehavioraldata(timespent
perpage,clicksperfeature,aggregatedovertime)andareusedincustomersegmentation
algorithms. Onthesamepage,work[28]useddemographicfeatures(age,gender,state),
behavioral features (engagement level, time spent, number of screens viewed, clicks,
sessions)andtransactionalfeatures(maximumbudget,maximumreturnoninvestment,
numberofpurchases)forcustomersegmentation.
Forthepurposeofdiscoveringdriversofuserloyaltyandimprovingusersatisfaction
andengagement,studies[29–32,34,37]leveragedmainlybehavioralandusagedata(login
frequency, feature usage, interaction patterns to understand user engagement, product
adoptionovertime). However,in[35,37]interviewandsurveydatawereused,providing
contextonuserperceptions,satisfaction,anddemographiccharacteristics.Instudies[34,35],
systemlogsandeventdatawereusedandspecificallyin[35]logsareusedalongsidedirect
feedbacklikesurveysandsupporttickets. Marketing,freetrial,andtransactionaldata(ad
impressions,messagetypes,marketingvariablesandtrialdurationvariations)areutilized
byresearchersin[30,33]whilein[36]simulateddatawereemployed(transactionvolumes,
volatility,user-centricmetrics,userprofiles,negotiationdynamics)toexplorehypothetical
userbehaviorsandnegotiationdynamicsinscalable,controlledenvironments. Last,stud-
ies[32,35]utilizedrich,multi-sourcedataintegrations,combiningCRM,financial,usage,
andexternalfirmographicdatainordertobettermodelloyaltyandcustomerrelationships.
Finally,research[38],whichfocusedonpredictingCLV,employedvarioustypesof
datatoachieveitsgoal. Thosedataincludedrevenuedata(monthlyrecurringrevenue,
historicalbillingdata),productlicensedata(producttypes,acquisitionchannels,license
terms), product usage data (feature adoption, user activity logs, engagement metrics),
firmographic data (company size, industry, geography, employee count) and customer
segments based on behavior. Table 1 summarizes the types of input data used in the
reviewedapproaches.
Table1.Typesofdatasourcesusedbythereviewedapproaches(RQ2).
Transactional/
| Usage    |          | Customer | Financial | Customer | Satisfaction |                  |           |
| -------- | -------- | -------- | --------- | -------- | ------------ | ---------------- | --------- |
| Ref.     | Business |          |           |          |              | Survey/Interview | Marketing |
| Behavior |          | Profile  | Data      | Support  | (e.g.,NPS)   |                  |           |
Metrics
| ✓   |     | ✓   | ✓   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[18]
✓
[24]
| [12] ✓ | ✓   | ✓   |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| [14] ✓ | ✓   |     |     |     |     |     |     |
✓
[22]
✓ ✓
[19]
✓ ✓
[25]
| [13] ✓ | ✓   | ✓   |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| [20]   |     |     |     | ✓   |     |     |     |
| ✓      |     | ✓   |     | ✓   |     |     |     |
[15]
| ✓   | ✓   | ✓   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[8]
✓
[23]
| [21] ✓ |     | ✓   |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| [38] ✓ | ✓   | ✓   | ✓   |     |     |     |     |
| [29]   |     |     |     |     |     |     | ✓   |
| ✓      |     |     |     |     |     | ✓   | ✓   |
[30]
| ✓   |     | ✓   |     |     |     | ✓   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[31]
|     |     | ✓   |     |     | ✓   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[26]
| [33] ✓ |     |     |     |     | ✓   |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
[32] ✓
✓ ✓
[27]
| ✓   |     | ✓   |     |     |     | ✓   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
[37]

Appl.Sci.2025,15,6508 10of35
Table1.Cont.
Transactional/
Usage Customer Financial Customer Satisfaction
Ref. Business Survey/Interview Marketing
Behavior Profile Data Support (e.g.,NPS)
Metrics
[16] ✓ ✓ ✓ ✓
[28] ✓ ✓
[35] ✓ ✓ ✓ ✓
[17] ✓ ✓ ✓ ✓
[36] ✓ ✓
[34] ✓ ✓ ✓
4.3. MachineLearningMethods
Regarding RQ3, most of the studies relied solely on machine learning methods to
conducttheirresearchandgeneratetheirexpectedresults. Amongthepapersfocusedon
churnprediction,RandomForest(RF)[39–41]wasoneofthemostwidelyusedmethods,
appearinginstudies[8,13–19,23,24]. Inthestudy[18],RFwith64estimatorsachievedan
excellentperformanceof98.8%accuracy,0.997AreaUndertheCurve(AUC),andstrong
F-measures(0.989non-churn,0.981churn). Instudies[8,14],RFalsostoodoutwith87%
testing accuracy, while being resistant to noise and overfitting. A study [13] reported
exceptionallystrongRFresultsaswell,withF1-scoreof92.6%andrecallof91.6%,whilea
study[15]foundthatRFhadthehighestprecision(0.80)amongthemodelstested,though
recalllaggedbehindXGBoost. Onthecontrary,RFunderperformedinthestudy[12],with
anAUCof~0.5,andaddingPCA(PrincipalComponentAnalysis)didnothaveanyimpact
ontheresults. Inwork[23],RFachievedAUC>0.99and97%accuracy,outperformingall
othermodelsacrossvariouslabelingschemeslikeslidingwindowsandactivityquartiles
whileinthestudy[24]RFwasusedasabaselinecombiningsequentialandaggregateddata,
whereitachievedanAUCof0.72,whichwasnotablylowerthanthehybridLongShort-
TermMemory(LSTM)models,indicatingitslimitationsinmodelingtemporaldynamics
insequentialdata. Inthestudy[17],RFshowedonlymoderatesuccesswithAUC-ROC
~0.65,thoughitsperformanceimprovedslightlywhenpairedwithSMOTE-Tomekforclass
imbalancehandling. Figure3presentsthenumberofpapersthatsuccessfullyemployed
specificmachinelearningalgorithms. Thus,itcontainsthenumberofpaperstowhichthe
specificmachinelearningalgorithmnotedthebestresults. RFwassuccessfullyusedin
moreworksthananyothermachinelearningalgorithm.
ExtremeGradientBoosting(XGBoost)[42]wastestedinstudies[12,15,16],consistently
deliveringtop-tierresults. Inresearch[12],XGBoostachievedthehighestAUC(0.7941)
and,afterthresholdtuning,improvedsensitivityto74%. Study[15]reportedROCAUC
of0.86,recallof0.85andF1-scoreof0.82,outperformingothermodelssuchasRandom
Forests andLogistic Regressionand identifiedticket resolution timeandlicense ageas
key features. Study [16] found XGBoost and Logistic Regression achieved comparable
AUC(~60%),butXGBoostwaslessprofitablethanlogisticregressionwhenmeasuredby
ExpectedMaximumProfit. XGBoostandGradientBoostingDecisionTrees(GBDT),were
alsousedin[22]withXGBoostemergingasthebest-performingmodelwith98.8%AUC,
whileGBDTfollowedwith93.4%AUC.
Decision Trees (DT) were used in studies [8,13,14,16,19]. In work [13], DT was the
bestperformerusingChi-squared-selectedfeatures,with88.2%F1-scoreand94.4%recall.
In contrast, studies [8,14] revealed DT’s tendency to overfit, achieving perfect training
accuracybutonly76%ontestdata. DTalsoservedasabaselinein[16,19],withmoderate
performancecomparedtoensembleandhybridmodels.

Appl.Sci.2025,15,6508 11of35
Figure3.Machinelearningmethodsproposedtousebythereviewedpapers.
LogisticRegression(LR)[43]wasappliedinstudies[8,12,13,15–17],mostlyasabase-
line due to its interpretability. Its AUC ranged from 0.71 to 0.74 in studies [8,12], and
it consistently offered stable, if lower, performance. In work [16], LR delivered strong
profit-basedperformance,leadinginExpectedMaximumProfitandTopDecileLiftwhen
pairedwithusage-basedfeatures. Intheresearch[17],LRinitiallyhad97%accuracybut
0% recall until SMOTE-Tomek was applied, improving recall to 57% (but at the cost of
reducedprecision).
Support Vector Machines (SVM) featured in studies [8,13,14,16,19]. SVMs often
struggled—studies[8,14]reported100%trainingaccuracybutjust63%testaccuracy,indi-
catingsevereoverfitting. However,thestudy[19]successfullyemployedahybridmodel
combiningSVMwithNaiveBayes,achieving95.67%accuracy,94.3%precision,and95.65%
recall, outperformingotherclassifiers. Inwork[16], SVMdeliveredstrongprofitability
metrics,rivalingLRinExpectedMaximumProfit.
NeuralNetworks(NN)(includingMLPsanddeeplearning)appearedin[8,14,15,18,20,23,24].
A study [18] reported 96.5% accuracy for a Multilayer Perceptron (MLP), which, while
lowerthanRFandAdaBoost,stillofferedvaluablecomparativeinsights. Inworks[8,14],
deepneuralnetworks(includingTensorFlowmodels)achievedaround82%testaccuracy,
withonemodelidentifyingsubtlechurnsignalslikelowsessionfrequencyandhighpricing.
MLPwasagaintestedin[15],performingadequatelybuttrailingensemblemethodslike
XGBoostandGradientBoostingMachine(GBM).In[24],anon-sequentialNNusingonly
aggregated features yielded lower performance (AUC not specified), underperforming
compared to LSTM-based hybrids. In research [20], sentiment modeling with LSTM
networks produced learned sentiment features from support ticket data, which when
combinedwithmetadatafeatures, ledtoanoticeable+5%increaseinaccuracyandthe
highestrecall,criticalforpredictingsubscriptionrenewals. Single-layerneuralnetworks
wereemployedin[23]achievingAUC=0.987,thoughtheirperformancedegradedover
timeduetostaleness,makingthemlessidealforevolvinguserbehavior.
AdaBoost [44] and other boosting techniques such as GBM [45] were included in
studies[15,18]. AdaBoostin[18]wasthesecond-bestperformerwith98.4%accuracyand
0.995AUC,whilein[15],boostingmethods(especiallyXGBoost)consistentlyoutperformed
simplerclassifiersacrossrecall,AUC,andF1-score.

Appl.Sci.2025,15,6508 12of35
NaiveBayes[46],thoughrarelyatopperformer,wasevaluatedin[8,14,19]. Itper-
formedpoorlywhenusedalonein[8,14](accuracy~69–71%),butin[19],itformedpartof
thehigh-performinghybridmodelwithSVM.
Transformer-basedmodels[47]wereexploredinthestudy[22]. TheFT-Transformer,
builtfortabulardatawithembeddedcategoricalandnumericalfeatures,achieved86.79%
accuracy,88.75%recall,and94.9%AUC—astrongimprovementoverolderworks(AUC
~71–77%),thoughitwasstilloutperformedbyXGBoost(AUC98.8%,F194.81%,accuracy
94.8%)inthesamestudy.
HybridModelswereexploredin[19],whereanSVM-NaiveBayescombinationledto
superiorperformanceacrossallkeymetrics,indicatingthestrengthofensemblelearning
strategies,especiallyinreducingfalsepositives/negativesforCRMapplications. Addi-
tionally,ensembleandhybridarchitectureswerecoreinstudies[20,21,24]. HybridLSTM
architecturescombiningsequentialandstaticaggregateddataoutperformedsingle-source
models [24]. Study [21] introduced the BBE-LSWCM ensemble, integrating LightGBM,
BiLSTM,andLRtoachieve60%betterdecilelift(DL1=3.197)and25%higherAUROC
thanstandaloneBiLSTM,whilemaintainingreasonablelatency.AmodularfusionofLSTM-
learnedsentimentfeaturesandhandcraftedmetadatayieldedthehighestaccuracyand
recall,demonstratingthevalueofcombiningdeeplearningwithtraditionalfeatures[20].
Theresearchersin[26]employedadynamicprogrammingmodeltooptimizeplayer
retention over time alongside a Q-learning algorithm [48] to simulate offline decision-
makingandidentifyconvergencepathsforbothactualandperceivedquality. Theresults
indicatedthatbothgamequalityandperceivedqualitystabilizedathighlevelsregardless
of initial quality. However, the speed of convergence depended on starting conditions,
withlowerinitialquality(x =0.4)taking20periodstoconvergecomparedto14periods
0
forx =0.6. Interestingly,whenplayersinitiallyoverestimatedquality,perceivedquality
0
followeda“high-low-high”trajectory.
Theauthorsof[27]employedaniterativeclusteringapproachstartingwithPCAfor
dimensionalityreductionandK-meansclustering,laterswitchingtoUniformManifold
ApproximationandProjection(UMAP)andHierarchicalDensity-BasedSpatialClustering
ofApplicationswithNoise(HDBSCAN)formoreeffectivehandlingofsparseandnon-
normaldatadistributions. Afterfouriterations,thefinalmodelidentifiedsixmeaningful
personas(e.g.,Uploaders,TVBuilders),whichwerevalidatedthroughinterview-based
triangulation.Earlierclusteringfailedduetooverlappingbehaviorsandsparsedata,butthe
refinedmethodsucceededindifferentiatingusertypesbycombiningbehavioraldatawith
qualitativeinsights. Atlast,inthestudy[28]amoretraditionalmachinelearningapproach
was adopted for behavioral customer segmentation to predict subscription conversion
by evaluating several classifiers, including Decision Tree, K-Nearest Neighbors (KNN),
Naive Bayes, RF, LR, SVC, and XGBoost. Among these, XGBoost achieved the highest
performance,withanaccuracyof79%,precisionof80%,recallof76%,andanF1-scoreof
78%. Cross-validationfurtherconfirmedthegeneralizabilityofthemodelwithamean
scoreof78.5%. However,themodelexhibitedaslightlyhigherrateoffalsenegativesthan
falsepositives,arelevanttrade-offwhenconsideringconversionsensitivity.
Studies[30,32,36]utilizedmachinelearningandstatisticalmodelingtopersonalize
user experience and predict outcomes. Study [30] employed Lasso regression [49] to
personalizefreetriallengths,showinga6.8%subscriptionincreasecomparedtoa30-day
baseline. Simpler uniform policies like a 7-day trial still yielded a 5.59% gain. Among
alternatives, Lasso outperformed random forests and causal forests, which struggled
with overfitting and poor personalization. Similarly, a study [36] implemented logistic
regression, random forest, and gradient boosting for dynamic pricing in usage-based
models. Whilelogisticregressionachievedperfectaccuracyonsimulateddata,real-world

Appl.Sci.2025,15,6508 13of35
applicabilityfavoredgradientboostingandrandomforest,withaccuraciesaround0.77
and0.75,respectively. Study[32]leveragedhierarchicallogisticregressionwithintheCross
IndustryStandardProcessforDataMining(CRISP-DM)frameworktopredictcustomer
retention and cross-buying. Retention prediction reached 93.7% accuracy (F1: 94.38%),
whilecross-buyingwaslesspredictable(accuracy: 78.9%,F1: 20.60%).
Finally,intheworkpresentedin[38],theauthorsusedahierarchicalensembledma-
chinelearningframeworkforpredictingCLVinB2BSaaScompanies. TheCLVprediction
wasframedasalumpsumregressiontaskratherthanatraditionaltime-seriesforecasting
problem,enablingtheuseofrichsupervisedlearningmodelslikeLightGBM,XGBoost,
LASSOregression,KNN,andAutoARIMA.Tohandlelimitedanddriftinghistoricaldata,
atwo-stephierarchicalmodelwasbuilt: firstpredictingoverashorttimehorizon,then
mappingittoalongerhorizon. Theyalsoadoptedanensembleapproach, segmenting
customersbasedonkeyfeatures(likesize)andfittingdifferentmodelsfordifferentgroups
(LightGBMforsmallercustomers,LASSOforenterprises). Inperformancetests,thelump
sumregressionmodelsoutperformedtraditionaltime-seriesmodelsby2to5timesacross
metricslikeRootMeanSquareError(RMSE),MeanAbsoluteError(MAE),andsymmetric
meanabsolutepercentageerror(SMAPE),withLightGBMgivingthebestresults.
Few researchers, however, opted to utilize several methods that rely on statistical,
econometricorheuristicmodels. Indetail,study[34]deployedProcessMining[50],specifi-
callyHeuristicMinerandFuzzyMiner,totrackuserbehaviorsleadingto“Aha! moments”.
Through data cleaning and retention clustering, it identified key activation actions by
reducingmodelcomplexityby62%. However,manualdataprocessingwastime-intensive.
Linear Mixed Models (LMMs) were utilized in [37] to evaluate usage continuance.
It accounted for repeated measures and individual client variability through fixed and
random effects. For existing clients, the model achieved an RMSE of 5.23, though it
struggledwithnewclients(RMSE:13.93),indicatingagapingeneralization. Activation
measures(banners)significantlyincreasedusage(+5.2%).
PLS-SEM(PartialLeastSquaresStructuralEquationModeling)wasemployedin[31]
tovalidatetheeffectofUIdesignonsatisfactionandloyalty. Theresultsshowedstrong
modelreliability(Cronbach’salpha: 0.837–0.860)andhighexplanatorypower(R2~0.50).
Allhypotheses(UIdesign→Satisfaction→Loyalty)werestatisticallysupported.
Focusing on the topic of customer segmentation, the study [25] introduced a joint
modelingframeworkthatcombinedGeneralizedLinearMixedModels(GLMMs)[51]to
trackplayers’in-gamebehavioralpatternswithaSharedParameterModel(SPM)[52]that
linkedthesebehavioralgroupstotheprobabilityofdropout. Thisintegratedapproach
significantlyoutperformedtraditionalmodelslikeCoxregression,improvingretention
predictionby63.2%athigherplayerlevelsandreducingRMSEforlifetimeengagement
by25.5%.
Authorsin[29]tookamoreeconometricroute,applyingaDynamicProbitModel[53]
with copula-based corrections for endogeneity. It incorporated exponentially decaying
goodwillstockstomodelusertouchpointsandusageeffects. Inthisstudyregularization
viaLasso/Ridgeregressionwasalsoutilized,addressingmulticollinearityandimprov-
ing model stability. The study achieved a 9.3% error reduction in predictions and key
findingsemphasizedthatconsumer-initiatedtouchpointsandpersuasivecontentboosted
conversionstopremiumusers,whilefirm-initiatedadshadnegativeeffects.
Study[33]introducedtheAQUAMannegotiationmechanism,combiningquantile
estimation,opponentmodeling,andsurplusredistributiontomanageserviceacceptability.
Underbothnormalandextremeloads(upto2500users/min),itmaintainedhighaccept-
abilityrates(95%+and93.3%,respectively)whilekeepingcostsandoverheadmanageable.

Appl.Sci.2025,15,6508
14of35
Atlast,study[35]outlinedarangeofqualitative(interviews,questionnaires,incident
reports)andquantitative(A/Btesting,in-productsurveysandonlineads,crowdfunding
and crowdsourcing platforms, click-based user data collection) methods deployed for
collectingandintegratingcustomerfeedback,aswellasinsightsintotheirperformance
acrossseveralcompanies. Thisstudyconcludedthatthere’snosingleperfectapproachand
thatthechoiceandsuccessofmethodsdependheavilyonthecompany’ssize,thestructure
oftheproductoffering(customvs. SaaS),thetypeofcustomers(B2Bvs. B2C),thestageof
developmentandtheinternalcommunicationanddataintegrationstructure.
Table2summarizestheresultsregardingtheuseofmachinelearninginthereviewed
approachesforSaaS.
Specifically, Table 2 includes the proposed ML algorithm for the reviewed papers
alongwith the comparedmethods. Resultsaresplit intotwo categories, indicatingthe
mostcommonlyusedmetricsandmiscellaneousacrossthereviewedpapers. Additionally,
informationabouttheuseddatasetsandemployedvalidationmethodsisincluded.
Table2.MachinelearningmethodsusedfordecisionsupportinSaaS(RQ3).
EvaluationResults
| Proposed | Compared |               |               | Validation |         |
| -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref.     |          |               | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
RandomForest:0.997AUC,
0.988Accuracy,
0.989F-measurefor
|     |     | Non-ChurnClassand |     |     | Datasetfroma      |
| --- | --- | ----------------- | --- | --- | ----------------- |
|     |     | 0.981forChurn     |     |     | partnercompany    |
|     |     | NeuralNetworks:   |     |     | associatedwiththe |
Training(64%),
|     | Neural | 0.968AUC,0.965Accuracy, |     |     | Universityof |
| --- | ------ | ----------------------- | --- | --- | ------------ |
Random validation
| [18] | Networks, | 0.975F-measurefor | -   |     | Évora,containing |
| ---- | --------- | ----------------- | --- | --- | ---------------- |
Forest (16%),andtest
|     | AdaBoost | Non-ChurnClassand |     |     | 196,977instances |
| --- | -------- | ----------------- | --- | --- | ---------------- |
(20%)sets
|     |     | 0.946forChurn      |     |     | correspondingto |
| --- | --- | ------------------ | --- | --- | --------------- |
|     |     | AdaBoost:0.995AUC, |     |     | 26,418service   |
|     |     | 0.984Accuracy,     |     |     | subscriptions   |
0.989F-measurefor
Non-ChurnClassand
0.974forChurn
|                 |             | HybridModels:0.8741AUC, |     |               | Datasetfromplayer  |
| --------------- | ----------- | ----------------------- | --- | ------------- | ------------------ |
|                 |             | 0.6953F1-score,         |     |               | logsofafreemium    |
|                 |             | 0.8023Accuracy          |     |               | mobilegame         |
| Hybrid          |             | LSTM:0.8592AUC,         |     |               | developedby        |
|                 | Random      |                         |     | 10-foldcross- |                    |
| [24] Model(LSTM |             | 0.6795F1-score,         | -   |               | TactileGames       |
|                 | Forest,LSTM |                         |     | validation    |                    |
| HiddenState)    |             | 0.7900Accuracy          |     |               | including          |
|                 |             | RandomForest:0.8405AUC, |     |               | 2,284,238recordsof |
|                 |             | 0.6414F1-score,         |     |               | 814,822unique      |
|                 |             | 0.7749Accuracy          |     |               | players            |
Datasetfroma
|     | Logistic | XGBoost:0.7526AUC |     |     | clientSaaS |
| --- | -------- | ----------------- | --- | --- | ---------- |
Regression, RandomForest:~0.5AUC 10-foldcross- companyincluding
| [12] XGBoost |         |                     | -   |            |                    |
| ------------ | ------- | ------------------- | --- | ---------- | ------------------ |
|              | Random  | LogisticRegression: |     | validation | 76,668observations |
|              | Forests | 0.7257AUC           |     |            | of20predictor      |
variables

Appl.Sci.2025,15,6508
15of35
Table2.Cont.
EvaluationResults
| Proposed | Compared |               |               | Validation |         |
| -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref.     |          |               | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
Randomforest:
0.88TrainingAccuracy,
0.87TestAccuracy
DecisionTrees:1.00
Decision
|     |     | (overfitting)Training |     |     | AB2BSaaS |
| --- | --- | --------------------- | --- | --- | -------- |
Trees,
|     |     | Accuracy,0.76TestAccuracy |     |     | subscriptions |
| --- | --- | ------------------------- | --- | --- | ------------- |
Support
|     |     | SupportVectorMachine: |     |     | dataset(source |
| --- | --- | --------------------- | --- | --- | -------------- |
Vector
|     |     | 1.00(overfitting)Training |     | train-testsplit | notmentioned) |
| --- | --- | ------------------------- | --- | --------------- | ------------- |
Random Machine,
| [14] |     | Accuracy,0.63TestAccuracy | -   | (percentagenot | including |
| ---- | --- | ------------------------- | --- | -------------- | --------- |
Forest Neural
|     |     | NeuralNetworks: |     | mentioned) | 7044examplesof |
| --- | --- | --------------- | --- | ---------- | -------------- |
Networks,
|     |     | 0.85TrainingAccuracy, |     |     | B2BSaaS |
| --- | --- | --------------------- | --- | --- | ------- |
NaïveBayes,
|     |     | 0.82TestAccuracy |     |     | subscriptionsand |
| --- | --- | ---------------- | --- | --- | ---------------- |
Logistic
|     |     | NaïveBayes:0.71Training |     |     | 21variables |
| --- | --- | ----------------------- | --- | --- | ----------- |
Regression
Accuracy,0.69TestAccuracy
LogisticRegression:
0.73TrainingAccuracy,
0.71TestAccuracy
XGBoost:0.948Accuracy,
0.9545Precision,
0.9418Recall,
0.9481F1-Score,0.988AUC
|     | Transformer- | Transformer-basedmodels: |     |                 | Datasetfroma   |
| --- | ------------ | ------------------------ | --- | --------------- | -------------- |
|     | basedmodels  | 0.8679Accuracy,          |     | train-testsplit | mobilefreemium |
[22] XGBoost (FT- 0.8477Precision, - (percentagenot gameincludesdata
|     | transformer), | 0.8875Recall,           |     | mentioned) | fromover     |
| --- | ------------- | ----------------------- | --- | ---------- | ------------ |
|     | GBDT          | 0.8671F1-Score,0.949AUC |     |            | 268,370users |
GBDT:0.8561Accuracy,
0.8755Precision,
0.8328Recall,
0.8536F1-Score,0.934AUC
HybridModel:
0.9567Accuracy,
0.943Precision,
0.9565Recall,0.943F1-Score
ANN:0.789Accuracy,
0.8403Precision,
0.8824Recall,
Datasetfrom
0.8608F1-Score
|                 | KNN,         |                            |     |                 | Kagglecontaining    |
| --------------- | ------------ | -------------------------- | --- | --------------- | ------------------- |
| Hybrid          |              | RandomForest:              |     | train-testsplit |                     |
|                 | Random       |                            |     |                 | subscriptiondetails |
| [19] Model(SVM+ |              | 0.8Accuracy,0.79Precision, | -   | (80%            |                     |
|                 | Forest,ANN,  |                            |     |                 | on7044customers     |
| NaïveBayes)     |              | 0.80Recall,0.79F1-Score    |     | train—20%test)  |                     |
|                 | Decisiontree |                            |     |                 | ofafictional        |
KNN:0.839Accuracy,
SaaScompany
0.826Precision,0.829Recall,
0.781F1-Score
DecisionTree:
0.9097Accuracy,
0.9242Precision,
0.9242Recall,
0.9242F1-Score

Appl.Sci.2025,15,6508
16of35
Table2.Cont.
EvaluationResults
|      | Proposed | Compared |               |               | Validation |         |
| ---- | -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref. |          |          |               | Miscellaneous |            | Dataset |
|      | Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
RandomForest:0.916Recall,
0.926F1-Score,
0.92Accuracy,
0.939Precision
|     |     |               | DecisionTree:0.945Recall, |     |     | Datasetextracted  |
| --- | --- | ------------- | ------------------------- | --- | --- | ----------------- |
|     |     | DecisionTree, | 0.871F1-Score,            |     |     | fromthecase-study |
train-testsplit
|     |     | Logistic | 0.845Accuracy, |     |     | company’s |
| --- | --- | -------- | -------------- | --- | --- | --------- |
(80%
|      | Random | Regression, | 0.809Precision      |     |           | databasesystem |
| ---- | ------ | ----------- | ------------------- | --- | --------- | -------------- |
| [13] |        |             |                     | -   | train—20% |                |
|      | Forest | Support     | LogisticRegression: |     |           | containing     |
test),10-fold
|     |     | Vector | 0.868Recall,0.902F1-Score, |     |     | 1788observations |
| --- | --- | ------ | -------------------------- | --- | --- | ---------------- |
crossvalidation
|     |     | Machine | 0.896Accuracy, |     |     | ofchurnand       |
| --- | --- | ------- | -------------- | --- | --- | ---------------- |
|     |     |         | 0.939Precision |     |     | non-churnsamples |
SupportVectorMachine:
0.881Recall,0.839F1-Score,
0.814Accuracy,
0.803Precision
Datasetcollected
fromacloud
serviceprovider
including
NeuralNetworks:
approximately
|      | Neural   |     | 0.9694Accuracy,  |     |             |           |
| ---- | -------- | --- | ---------------- | --- | ----------- | --------- |
| [11] |          | -   |                  | -   | Notprovided | 700unique |
|      | Networks |     | 0.9651Precision, |     |             |           |
cloudservice
0.9540Recall
offering-customer
pairsandaround
90,000associated
supporttickets
XGBoost:0.7956Accuracy,
0.7916Precision,
0.8507Recall,
0.8201F1-Score,
0.86ROCAUC
RandomForest:
0.7877Accuracy,
0.8042Precision,
0.8096Recall,
|     |     | Random | 0.8069F1-Score, |     |     |     |
| --- | --- | ------ | --------------- | --- | --- | --- |
Twodatasets
|     |     | Forest, | 0.85ROCAUC |     |     |     |
| --- | --- | ------- | ---------- | --- | --- | --- |
providedbya
|     |     | Logistic | LogisticRegression: |     |     |     |
| --- | --- | -------- | ------------------- | --- | --- | --- |
Portuguese
|      |         | Regression, | 0.7757Accuracy,  |     |                 |                 |
| ---- | ------- | ----------- | ---------------- | --- | --------------- | --------------- |
|      |         |             |                  |     | train-testsplit | softwarehouse   |
|      |         | Neural      | 0.7986Precision, |     |                 |                 |
| [15] | XGBoost |             |                  | -   | (80%            | withthefinal    |
|      |         | Networks,   | 0.7895Recall,    |     |                 |                 |
|      |         |             |                  |     | train—20%test)  | datasetincluded |
|      |         | AdaBoost,   | 0.7940F1-Score,  |     |                 |                 |
9539observations
|     |     | Gradient | 0.84ROCAUC |     |     |     |
| --- | --- | -------- | ---------- | --- | --- | --- |
fromthetwo
|     |     | Boosting | NeuralNetworks: |     |     |     |
| --- | --- | -------- | --------------- | --- | --- | --- |
datasetscombined
|     |     | Machine | 0.7835Accuracy, |     |     |     |
| --- | --- | ------- | --------------- | --- | --- | --- |
0.7910Precision,
0.8220Recall,
0.8062F1-Score,
0.84ROCAUC
AdaBoost:0.7867Accuracy,
0.7970Precision,
0.8191Recall,
0.8079F1-Score,
0.86ROCAUC

Appl.Sci.2025,15,6508
17of35
Table2.Cont.
EvaluationResults
| Proposed | Compared |               |     |               | Validation |         |
| -------- | -------- | ------------- | --- | ------------- | ---------- | ------- |
| Ref.     |          |               |     | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |     |               | Method     |         |
Metrics
GradientBoostingMachine:
0.7935Accuracy,
0.7946Precision,
0.8402Recall,
0.8167F1-Score,
0.86ROCAUC
RandomForest:
0.88TrainingAccuracy,
0.87TestAccuracy
NeuralNetworks:
|     | Neural    | 0.85TrainingAccuracy, |     |     |     |     |
| --- | --------- | --------------------- | --- | --- | --- | --- |
|     | Networks, | 0.82TestAccuracy      |     |     |     |     |
|     | Decision  | DecisionTree:1.00     |     |     |     |     |
Useractivity
|     | Trees,Logistic | (overfitting)Training |     |     | train-testsplit |     |
| --- | -------------- | --------------------- | --- | --- | --------------- | --- |
Random datasets(source
| [8] | Regression, | Accuracy,0.76TestAccuracy |     | -   | (percentagenot |     |
| --- | ----------- | ------------------------- | --- | --- | -------------- | --- |
Forest andnumberofdata
|     | Support | LogisticRegression: |     |     | mentioned) |     |
| --- | ------- | ------------------- | --- | --- | ---------- | --- |
notmentioned)
|     | Vector     | 0.73TrainingAccuracy, |     |     |     |     |
| --- | ---------- | --------------------- | --- | --- | --- | --- |
|     | Machine,   | 0.71TestAccuracy      |     |     |     |     |
|     | NaïveBayes | SupportVectorMachine: |     |     |     |     |
1.00(overfitting)Training
Accuracy,0.63TestAccuracy
NaiveBayes:0.71Training
Accuracy,0.69TestAccuracy
|     | Neural    | RandomForest:0.997AUC |     |     |     |                 |
| --- | --------- | --------------------- | --- | --- | --- | --------------- |
|     | Networks, | Decisiontree:0.987AUC |     |     |     |                 |
|     | Decision  | NeuralNetworks:       |     |     |     | Datasetfrom“The |
train-test-
|     | Trees,Logistic |     | 0.994AUC |     |     | SettlersOnline |
| --- | -------------- | --- | -------- | --- | --- | -------------- |
validationsplit
|     | Regression, | GradientBoosting: |     |     |     | (TSO)”,afreemium |
| --- | ----------- | ----------------- | --- | --- | --- | ---------------- |
(percentagenot
| Random | Support |                     | 0.984AUC |     |             | onlinestrategy |
| ------ | ------- | ------------------- | -------- | --- | ----------- | -------------- |
| [23]   |         |                     |          | -   | mentioned), |                |
| Forest | Vector  | LogisticRegression: |          |     |             | game,including |
crossvalidation
|     | Machine, |     | 0.967AUC |     |     | 7439usersand |
| --- | -------- | --- | -------- | --- | --- | ------------ |
(foldsnot
|     | NaïveBayes, | SupportVectorMachine: |     |     |     | 113,643observed |
| --- | ----------- | --------------------- | --- | --- | --- | --------------- |
mentioned)
|     | Gradient  |                    | 0.990AUC |     |     | events. |
| --- | --------- | ------------------ | -------- | --- | --- | ------- |
|     | Boosting, | KNN:0.840AUC       |          |     |     |         |
|     | KNN       | NaïveBayes0.887AUC |          |     |     |         |
Datasetfrom
|     | Hybrid |     |     |     |     | QuickBooksOnline |
| --- | ------ | --- | --- | --- | --- | ---------------- |
LightGBM:0.690AUROC,
|     | Models |     |     |     | train-testsplit | (QBO)users, |
| --- | ------ | --- | --- | --- | --------------- | ----------- |
~30minTrainingTime
|               | (Neural     |               |     |     | (500,000 | including           |
| ------------- | ----------- | ------------- | --- | --- | -------- | ------------------- |
| [21] LightGBM |             | HybridModels: |     | -   |          |                     |
|               | Networkwith |               |     |     | records– | 700,000combinations |
0.591AUROC,
|     | BiLSTM |     |     |     | 200,000records) | ofusersand |
| --- | ------ | --- | --- | --- | --------------- | ---------- |
~2hTrainingTime
|     | layers) |     |     |     |     | reference |
| --- | ------- | --- | --- | --- | --- | --------- |
timestamps.
Performance
indexedto
|     | XGBoost, |     |     | LIghtGBM= |     |     |
| --- | -------- | --- | --- | --------- | --- | --- |
1.0×
Gradient
Datasetcollected
|     | boosting, |     |     | LightGBM: |     |     |
| --- | --------- | --- | --- | --------- | --- | --- |
fromawell-known
|               | LASSO       |     |     | 1SMAPE, |             |                |
| ------------- | ----------- | --- | --- | ------- | ----------- | -------------- |
| [38] LightGBM |             |     | -   |         | Notprovided | B2BSaaScompany |
|               | Regression, |     |     | 1RMSE,  |             |                |
(numberofdata
|     | K-nearest- |     |     | 1MAE |     |     |
| --- | ---------- | --- | --- | ---- | --- | --- |
notmentioned)
|     | neighbors, |     |     | XGBoost:    |     |     |
| --- | ---------- | --- | --- | ----------- | --- | --- |
|     | AUTO-Arima |     |     | ~1.10SMAPE, |     |     |
~1RMSE,
~1.1MAE

Appl.Sci.2025,15,6508
18of35
Table2.Cont.
EvaluationResults
| Proposed | Compared |               |               | Validation |         |
| -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref.     |          |               | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
Gradient
Boosting:
~1.2SMAPE,
~1.1RMSE,
~1.2MAE
KNN:
~1.25SMAPE,
~1.2RMSE,
~1.25MAE
LASSO
Regression:
~1.25SMAPE,
~1.1RMSE,
~1.2MAE
AUTO-
Arima:
~1.75SMAPE,
~5RMSE,
~2.5MAE
LASSO
Regression
|     |     |     | reducedMSE |     | Datasetfroma  |
| --- | --- | --- | ---------- | --- | ------------- |
|     |     |     | to0.122    |     | U.S.-based    |
|     |     |     | Dynamic    |     | multinational |
LASSO
|     |     |     | probitmodel |     | computersoftware |
| --- | --- | --- | ----------- | --- | ---------------- |
Regression,
|     |     |     | withcopula |     | companyoperating |
| --- | --- | --- | ---------- | --- | ---------------- |
Dynamic
| [29] | -   | -   | corrections: | Notprovided | onaSoftware-as-a- |
| ---- | --- | --- | ------------ | ----------- | ----------------- |
probitmodel
|     |     |     | −3841 |     | Servicebusiness |
| --- | --- | --- | ----- | --- | --------------- |
withcopula
|     |     |     | Log-Marginal |     | modelincludinga |
| --- | --- | --- | ------------ | --- | --------------- |
corrections
|     |     |     | Density, |     | sampleof     |
| --- | --- | --- | -------- | --- | ------------ |
|     |     |     | 7808.5   |     | 14,989unique |
|     |     |     | Deviance |     | consumers    |
Information
Criterion
LASSO
Regression:
+6.8%
subscriptions
XGBoost:
Datasetfromafully
+6.17%
|            | Random        |     |               |                 | randomized         |
| ---------- | ------------- | --- | ------------- | --------------- | ------------------ |
|            |               |     | subscriptions | train-testsplit |                    |
| LASSO      | Forest,causal |     |               |                 | experiment         |
| [30]       |               | -   | Random        | (70%            |                    |
| Regression | forest,       |     |               |                 | involving          |
|            |               |     | Forests:Poor  | train—30%test)  |                    |
|            | XGBoost       |     |               |                 | 337,724unconnected |
(overfitted
usersglobally
trainingdata)
Causal
Forests:Poor
(minimalper-
sonalization)

Appl.Sci.2025,15,6508
19of35
Table2.Cont.
EvaluationResults
|      | Proposed | Compared |               |               | Validation |         |
| ---- | -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref. |          |          |               | Miscellaneous |            | Dataset |
|      | Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
Logistic
Regression:
1.682TDL,
21,209EMPB
(EUR)
Support
Vector
Machine:
|     |     | Random |     | 1.590TDL, |     |     |
| --- | --- | ------ | --- | --------- | --- | --- |
LogisticRegression:
|      |            | Forest,  |                       | 22,566EMPB |            |                   |
| ---- | ---------- | -------- | --------------------- | ---------- | ---------- | ----------------- |
|      |            |          | 0.604AUC              |            |            | Datasetfroma      |
|      |            | XGBoost, |                       | (EUR)      | cross-     |                   |
|      |            |          | SupportVectorMachine: |            |            | Europeansoftware  |
|      | Logistic   | Decision |                       | Random     | validation |                   |
| [16] |            |          | 0.603AUC              |            |            | serviceprovider   |
|      | Regression | Trees,   |                       | Forest:    | (foldsnot  |                   |
|      |            |          | RandomForest:0.594AUC |            |            | including         |
|      |            | Support  |                       | 11.482TDL, | mentioned) |                   |
|      |            |          | XGBoost:0.599AUC      |            |            | 3959subscriptions |
|      |            | Vector   |                       | 15,106EMPB |            |                   |
DecisionTree:0.523AUC
|     |     | Machine |     | (EUR) |     |     |
| --- | --- | ------- | --- | ----- | --- | --- |
XGBoost:
1.360TDL,
14,351EMPB
(EUR)
DecisionTree:
0.856TDL,
5809EMPB
(EUR)
Random
Forest,
|     |     | Decision | XGBoost:0.79Accuracy, |     |     |     |
| --- | --- | -------- | --------------------- | --- | --- | --- |
Datasetfrom
|     |     | Trees,Logistic | 0.8Precision,0.76Recall, |     |     |     |
| --- | --- | -------------- | ------------------------ | --- | --- | --- |
Kaggle
|     |     | Regression, | 0.78F1-Score |     | train-testsplit |     |
| --- | --- | ----------- | ------------ | --- | --------------- | --- |
(fineTech_appData)
| [28] | XGBoost | Support | Alltheothermethodswhere | -   | (80% |     |
| ---- | ------- | ------- | ----------------------- | --- | ---- | --- |
including
|     |     | Vector | outperformedbuttheir |     | train—20%test) |     |
| --- | --- | ------ | -------------------- | --- | -------------- | --- |
50,000rowsofuser
|     |     | Machine, | specificresultswerenot |     |     |     |
| --- | --- | -------- | ---------------------- | --- | --- | --- |
information
|     |     | K-nearest- | provided |     |     |     |
| --- | --- | ---------- | -------- | --- | --- | --- |
neighbors,
NaïveBayes
RandomForest:
0.09Precision,0.11Recall,
|     |     |     | 0.10F1-Score        |     |     | Datasetfrom       |
| --- | --- | --- | ------------------- | --- | --- | ----------------- |
|     |     |     | LogisticRegression: |     |     | Aircall,aSoftware |
crossvalidation
|      | Random | Logistic   | 0.05Precision,0.57Recall, |     |           | asaService       |
| ---- | ------ | ---------- | ------------------------- | --- | --------- | ---------------- |
| [17] |        |            |                           | -   | (foldsnot |                  |
|      | Forest | Regression | 0.19F1-Score              |     |           | companyincluding |
mentioned)
|     |     |     | Theproposedmodelwas     |     |     | datafromabout |
| --- | --- | --- | ----------------------- | --- | --- | ------------- |
|     |     |     | betteratexplainingchurn |     |     | 5000customers |
drivers(featureimportance)
thanpreciseprediction.
LogisticRegression:
|     |     |     | 1.00Accuracy,            |     |     | Asimulation        |
| --- | --- | --- | ------------------------ | --- | --- | ------------------ |
|     |     |     | 1.00Precision,1.00Recall |     |     | datasetreplicating |
Random
|      |          |            | (duetodatasetsimplicity)   |     |                 | real-world    |
| ---- | -------- | ---------- | -------------------------- | --- | --------------- | ------------- |
|      | Forest,  |            |                            |     | train-testsplit |               |
|      |          | Logistic   | RandomForest:              |     |                 | Softwareasa   |
| [36] | Gradient |            |                            | -   | (80%            |               |
|      |          | Regression | 0.75Accuracy,              |     |                 | Service(SaaS) |
|      | Boosting |            |                            |     | train—20%test)  |               |
|      |          |            | 0.714Precision,0.789Recall |     |                 | usagepatterns |
Machine
|     |     |     | GradientBoostingMachine: |     |     | (numberofdata |
| --- | --- | --- | ------------------------ | --- | --- | ------------- |
|     |     |     | 0.77Accuracy,            |     |     | notmentioned) |
0.753Precision,0.768Recall

Appl.Sci.2025,15,6508
20of35
Table2.Cont.
EvaluationResults
| Proposed | Compared |               |               | Validation |         |
| -------- | -------- | ------------- | ------------- | ---------- | ------- |
| Ref.     |          |               | Miscellaneous |            | Dataset |
| Method   | Methods  | CommonMetrics |               | Method     |         |
Metrics
Datasetscollected
fromfour
|     |     | LogisticRegression: |     |     | databasesat    |
| --- | --- | ------------------- | --- | --- | -------------- |
|     |     | 0.9372Accuracy,     |     |     | Digidata,aSaaS |
Logistic
| [32] | -   | 0.9549Precision, | -   | Notprovided | companywherethe |
| ---- | --- | ---------------- | --- | ----------- | --------------- |
Regression
|     |     | 0.9330Recall,           |     |     | projectwascarried |
| --- | --- | ----------------------- | --- | --- | ----------------- |
|     |     | 0.9438F1-Score,0.999AUC |     |     | out(numberof      |
datanot
mentioned)
4.4. FormofOutputsPresentedtoSaaSProviders
ConcerningRQ4,researcherschoseawidevarietyofmethodstopresenttheirresults
toSaaSprovidersinordertosupportdecision-making. Aslistedbelow,thecategoriesof
thosemethodsinclude:
1. Visualizations
Asignificantnumberofpapersutilizedvisualrepresentationslikeconfusionmatrices,
ReceiverOperatingCharacteristic(ROC)curves,featureimportanceplots,retentioncurves,
sentimentplots,time-seriesgraphsandprocessmaps. Thesevisualshelpnon-technical
stakeholdersquicklygrasppatterns,modelstrengths,andkeyinsights. Theyalsosupport
internalpresentationsandstakeholderalignmentaroundkeymetricsandstrategies.Table3
presentsthevisualizationtechniquesdeployedbythereviewedapproaches.
Table3.Visualizationsfordecision-making(RQ4).
|     | Ref. |     | Visualizations |     |     |
| --- | ---- | --- | -------------- | --- | --- |
[14] Accuracycurvestoshowtheimpactoftreecountsinrandomforests
|     | [22] | AUC-ROCcurvesandconfusionmatricestovalidaterobustness |     |     |     |
| --- | ---- | ----------------------------------------------------- | --- | --- | --- |
[25] Hazardratecurvesandpredictiveintervalsforretentionstatistics
|     | [13] | Featureimportance(e.g.,prevPeriodTrans)viabarcharts |     |     |     |
| --- | ---- | --------------------------------------------------- | --- | --- | --- |
|     | [20] | Temporalsentimentplotstracksatisfactiontrajectories |     |     |     |
[23] ROCcurvesandfeatureplotsthathighlight“misseddays”astoppredictors
[21] (BBE-LSWCM)usesdecileliftchartstoshowa30%churnreductioninA/Btests
|     | [31] | PathanalysisdiagramstomapUIdesigntoloyalty |     |     |     |
| --- | ---- | ------------------------------------------ | --- | --- | --- |
[33] Time-seriesgraphstocompareadaptivevs. non-adaptivenegotiationmodes
[34] Processmapsthatrevealkeyactivationmoment
[37] Trajectoryplotsthatshowactivationimpacts
|     | [16] | Coefficientplotstoillustrateusagedata’simpactonchurn |     |     |     |
| --- | ---- | ---------------------------------------------------- | --- | --- | --- |
[35] Dashboardstoautomatefeedbacksummariesandissueprioritization
[36] Comparativeplotsthatguidemodelselectionviaaccuracy/recallmetrics
2. Simulation/What-IfAnalysis
Simulationtoolsmodelhypotheticalscenarios(e.g.,pricingchanges,triallengths),
enabling SaaS providers to test retention strategies and forecast revenue impact before
implementation, supporting data-driven decision-making. Study [18] enabled “what-
if” scenarios to test the impact of retention strategies like loyalty extensions, helping
providersoptimizeinterventionswhiletheworkpresentedin[25]simulatedpromotional
campaigns, showing a 20% engagement boost from aggressive incentives, and models
premiumpurchasevaluesforrevenueforecasting. Additionally,work[29]testedtiming
strategies,revealingpeakconversionwindows(e.g.,post-trialexpiration)andwarning

Appl.Sci.2025,15,6508 21of35
againstoverusingpersuasivemessagingandstudy[30]comparedtriallengths(7-dayvs.
30-daytrial)throughsimulations,findingshortertrialsoptimalforbeginnersbutlonger
trialsbetterforexperts. Atlast,in[26],theauthorsmodeledplayerretentionunderquality
adjustments, showing that initial quality investments reduced attrition and study [36]
simulateddynamicpricingstrategies,suchasoutcome-basedbilling,toaligncostswith
customervalue.
3. SegmentationandPersonaModeling
Studies[23,28,32,38]usedclusteringandbehavioralanalysistosegmentusersorcreate
personas. These help SaaS providers tailor features, marketing, and support strategies
todistinctusergroupsforbetterengagement. Table4includesthesegmentationgroups
used in those studies. Authors in [25] categorized users based on demographics and
engagementlevels,inthestudy[23]theauthorschosetocategorizetheirusersbytheir
activitypatternswhile[38]chosetogroupusersbyCLV.Additionally, theworkin[27]
createdB2Buserpersonaswhilein[28]theauthorscreatedbehavioralclusters. Finally,the
study[32]segmentedusersbyrelationshiplengthandcross-sellingdependency.
Table4.Segmentationandpersonamodeling(RQ4).
Ref. SegmentationGroups Description
Demographics(gender,geography)and Groupspeopleaccordingtodemographicsand
[25]
engagementlevels engagementlevels
Classifiesplayersbyactivitypatterns,usingloyalty
[23] Activitypatterns(e.g.,“economyoverviewusage”)
markerstotargetinterventions
SegmentscustomersbyCLV,focusingonprioritizing
[38] CustomerLifetimeValue(CLV)
enterpriseclientsforretention
Createsuserpersonaswithpainpointsandworkflow
[27] B2Buserpersonas(e.g.,“DataSellers”)
metricstoguideproductdevelopment
Identifiesbehavioralclusters,suchas
[28] Behavioralclusters(e.g.,education-focusedusers)
education-focusedusers,fortargetedmarketing
[32] Relationshiplengthandcross-sellingdependency Segmentsbyrelationshiplength
4. BusinessImpactMetrics
Metrics like CLV, MRR and ROI can be used to quantify churn effects. This en-
ablesproviderstounderstandthefinancialimplicationsofretentioneffortsandprioritize
high-value customer segments. For instance, study [18] reported cost savings per re-
tainedcustomerandrevenueprotectionthroughchurnreduction,whiletheworkin[14]
demonstratedROIimprovementsviadynamicpricingstrategies. Earlychurndetection
andassociatedacquisitioncostreductionswerehighlightedinstudy[19]andstudy[25]
showcasedarevenueboostfromcollaboration-drivenmonetizationmodels. Furthermore,
studiessuchas[8,21]focusedonreducingnegativeMRRchurnandincreasingintervention
acceptancethroughA/Btesting,respectively. ThepredictionofCLVandtheapplication
ofmarginalROIformulaswereaddressedinthework[38],whereasthestudy[30]illus-
tratedhowoptimizedfreetrialstrategiescouldenhancebothretentionandrevenue. In
addition,study[26]linkedqualityinvestmentcoststogainsinnetwork-drivenretention,
and study [16] evaluated predictive accuracy in relation to carbon emissions. Studies
like[36]connectedusage-basedbillingmodelstoamarkedincreaseincustomersatisfac-
tion,while[32]quantifiedretentiondifferencesacrosscountries,providingfurtherinsights
into localization strategies. Table 5 summarizes the business metrics employed by the
reviewedapproaches.

Appl.Sci.2025,15,6508 22of35
Table5.Businessimpactmetrics(RQ4).
Ref. BusinessMetrics
[18] Costsavingsperretainedcustomer,revenueprotectionfromchurnreduction
[14] DynamicpricingROI
[19] Churnratesfromearlydetection,acquisitioncostreduction
[25] Revenueboostfromcollaboration-basedmonetization
[8] NegativeMRRchurnandCLV
[21] ChurnreductionandinterventionacceptanceinA/Btests.
[38] MarginalROIformulas
[30] Improvedretentionandrevenue
[26] Qualityinvestmentcostsagainstnetwork-drivenretentiongains.
[16] Predictiveaccuracyagainstcarbonemissions
[36] Customersatisfaction
[32] Country-specificretentiondifferences
5. ModelDeploymentandIntegration
Model deployment integrates predictive models into SaaS platforms via APIs or
cloudpipelines,enablingautomatedchurnpredictionandalignmentwithCRMfeatures.
Buildingonthis,CRMandmarketingtoolsusetheseinsightstopersonalizecampaigns
basedonchurnriskoruserbehavior. Additionally,toolkitsandinteractivesystemssup-
portscenariotestingandonboardinganalysis,helpingteamsrefinestrategiesandmake
data-drivendecisions.
For instance, the work in [30] integrated RESTful APIs and the CBAR platform to
deliverJSON-formattedreal-timeriskscores,enhancingboththespeedandaccuracyof
predictions. Centralized Bank Account Register (CBAR) not only ranked subscriptions
by risk and value but also enabled targeted actions based on live insights. Similarly,
study[12]proposedastandaloneappthatsupporteddynamicthresholdingandfeedback
loops,allowingcontinuousmodelrefinement,andintroducedatoolofferinglivechurn
predictions for real-time decision-making. This study also highlighted declining login
activityasanearlywarningsignandrecommendsdynamicthresholdadjustmentbasedon
marketingcapacity.
Severalotherstudiesproposedadditionalenhancements. Asshownin[21]anAWS
SageMakerpipelinewasutilizedtosupportbothbatchandreal-timefeaturization,enabling
flexibledataprocessing, andtriggeredchatpop-upsforhigh-riskuserstofosterimme-
diate engagement. Study [16] recommended leveraging cloud storage and algorithmic
optimizationstoreduceenvironmentalimpact,whilework[36]providedpseudocodefor
integratingreal-timedatastreamswithbillingsystems.
Moreover,theworkin[24]alignedpredictivemodelswithtargetedre-engagement
strategiesforat-riskusers,while[19]fine-tunedretentioncampaignsbybalancingpreci-
sionandrecall,anddesignedhybridmodelstoensurescalabilityforclouddeployment.
Study[29]optimizedconversionratesthroughstrategicadplacementsandprecisetiming
ofmessaging. Study[17]ensuredthatkeyfeatureusagedataissyncedwithCRMsystems
andflagslow-usageaccountsforproactivecustomersuccessoutreach.
Dashboardsandinteractivesystemsalsoplayacriticalsupportingrole. Study[15]pre-
sentedadashboardthatvisualizeschurnriskmetricsandintegratesreal-timealertsdirectly
intoCRMdashboards,ensuringthatteamscanactswiftlyoncriticalissues. Study[15]
offeredaprocessminingtoolkitthatuncovers“Aha!”momentsduringonboarding,en-
hancinguseractivationefforts. Finally,authorsin[35]proposedanautomatedfeedback
systemthatprioritizescriticaluserissuesandprovidesdashboardsthatvisualizefeedback
trends,helpingteamsmonitorusersentimentandbehaviorpatternsovertime.

Appl.Sci.2025,15,6508 23of35
5. Discussion
InresponsetoRQ1,theanalysisrevealedthatchurnpredictionisthemostfrequently
pursuedobjectiveindecisionsupportsystemsinSaaSsettings. Studiesconsistentlyempha-
sizedtheimportanceofidentifyingearlyat-riskusersinordertointerferewithdata-driven
strategies,thereforeimprovingsubscriptioncontinuanceandreducingrevenueloss. Be-
yondchurn,researchersalsocontributedsignificantlythroughusersegmentation,which
enablesthegroupingofcustomersintomeaningfulbehavioralordemographicclusters.
Thissupportspersonalizedproductdevelopment,targetedmarketing,andmoreresponsive
customerservice. Otherstudiesfocusedonimprovinguserengagementandpredicting
CLV,whicharekeyindicatorsforlong-termbusinesssustainability. Additionally,strategic
decisionsaroundpricingoptimization,freetrialpolicies,andonboardingpracticeswere
offeredsothatSaaSprovidersareaidedinaligningservicedesignwithactualuserbehavior
andexpectations.
Regarding RQ2, this survey revealed that for the effectiveness of decision-making
in SaaS environments, diverse and rich datasets must be used. In most studies, behav-
ioral data, such as clickstream logs, feature usage, and session frequency, emerged as
foundational. These were often combined with transactional and subscription-related
information,includingbillinghistoryandaccounttenure, toprovideafullerpictureof
userengagement. Studiesalsomadeuseofdemographicandfirmographiccharacteristics,
allowingforsegmentationbyindustry,companysize,orgeographiclocation.Insomecases,
sentiment data from support tickets or survey responses were incorporated to capture
users’subjectiveexperiences. Afewstudiesemployedsyntheticorsimulateddatatotest
hypotheticalscenariosandoptimizeinterventionstrategiesbeforedeployment. Altogether,
theresultsunderscoretheimportanceofintegratingbothquantitativesystemusagemetrics
andqualitativefeedbackforcomprehensivedecisionsupport.
AddressingRQ3,itwasfoundthatmachinelearningtechniquesplayacentralrolein
nearlyalltheexaminedimplementations. RFandXGBoostwerethemostcommonlyused
algorithms,andtheyconsistentlydeliveredstrongperformanceacrossvariousevaluation
metrics such as AUC, precision, recall, and F1-score. These models were particularly
effectiveinhandlinghigh-dimensional,tabulardatasetsandofferedabalanceofaccuracy
andinterpretability. Inmorecomplexscenariosrequiringtemporalmodelingorbehavioral
pattern recognition, hybrid and ensemble models outperformed traditional classifiers.
For example, combinations of LSTM networks with LightGBM or structured metadata
inputscapturedsequentialuserbehaviormoreeffectivelythanstaticmodelsalone. While
simplermodelslikeLRandDTprovidedusefulbaselines,theirperformancewasoften
eclipsedbyensembleordeeplearningapproaches. Notably,somestudiesconsideredthe
environmentalimpactandscalabilityofdifferentalgorithms,highlightingtherelevance
ofcomputationalefficiencyandcarbonfootprintinmodelselection. Overall,thechoice
ofmethodwasshowntodependonspecifictaskrequirements,datacharacteristics,and
operationalconstraintssuchaslatencyormodeltransparency.
Finally,inresponsetoRQ4,awidevarietyofoutputtypeswerepresentedtoinform
andguideSaaSproviders. Theimportanceofvisualanalyticswashighlighted,including
ROCcurves, featureimportancerankings, anduserbehaviormaps, whichhelpednon-
technicalstakeholdersinterpretmodeloutcomes. Business-orientedmetricssuchasCLV,
MRR,andROIlinkedpredictionstofinancialoutcomeswhilesimulationtoolsallowed
providerstoexperimentwithtrialdurationsorpricingadjustmentsbeforeactualimple-
mentation, enhancing the strategic value of the DSSs. Furthermore, user segmentation
andpersonamodelingenabledmoredetailedtargetingofuserengagementandmarketing
strategies,whileprocessminingtechniquesuncoveredcriticalactivationpatternssuchas
thediscoveryofan“ahamoment”.

Appl.Sci.2025,15,6508
24of35
Somestudiesalsofocusedonmodeldeploymentstrategies,emphasizingcloudinte-
grationandscalability. Bybridgingpredictiveanalyticswithtangiblebusinessinsightsand
strategictools,DSSoutputswereshowntohaveadirectimpactonoperationalefficiency,
customersatisfaction,andlong-termprofitability. Moreover,deployingsuchmodelsas
churnpredictiononesthroughthecloudoffersthepossibilityofprovidingMachineLearn-
ingasService(MLaaS)modelsspecializedforsupportingdecision-makinginSaaS.On
thesamepage,research[54]presentedanMLaaSsolutionformarketingthatcontaineda
churnpredictionmodeltestedinretailande-commercesettings.
Tosynthesizethefindingsdiscussedinthisreviewandprovideaclearerunderstand-
ingoftheresearchlandscape,Table6presentsthemaininsightsandfindingscorresponding
toeachresearchquestion(RQ1–RQ4)addressedinthisstudy. Table6offersacompact
overviewofthefocusareas,typesofdataused,appliedmachinelearningmethods,and
thenatureofdecisionsupportoutputsinSaaSenvironments.
Table6.Cumulativetable,findingsofRQ1–RQ4.
| Ref. | Focus | Data | ProposedMethod | Output |
| ---- | ----- | ---- | -------------- | ------ |
Simulation/What-If
Analysis,BusinessImpact
Usagebehavior,customer
| [18] Churnprediction |     |     | RandomForest | Metrics,Model |
| -------------------- | --- | --- | ------------ | ------------- |
profile,financial
Deploymentand
Integration
|                      |     |               | HybridModel       | ModelDeployment |
| -------------------- | --- | ------------- | ----------------- | --------------- |
| [24] Churnprediction |     | Usagebehavior |                   |                 |
|                      |     |               | (LSTMHiddenState) | andIntegration  |
Usagebehavior,
|                      |     | customerprofile,       |         | ModelDeployment |
| -------------------- | --- | ---------------------- | ------- | --------------- |
| [12] Churnprediction |     |                        | XGBoost |                 |
|                      |     | transactional/business |         | andIntegration  |
metrics
Usagebehavior,
Visualizations,Business
| [14] Churnprediction |     | transactional/business | RandomForest |     |
| -------------------- | --- | ---------------------- | ------------ | --- |
ImpactMetrics
metrics
| [22] Churnprediction |     | Usagebehavior | XGBoost | Visualizations |
| -------------------- | --- | ------------- | ------- | -------------- |
BusinessImpactMetrics,
|                      |     | Usagebehavior,  | HybridModel(SVM |                 |
| -------------------- | --- | --------------- | --------------- | --------------- |
| [19] Churnprediction |     |                 |                 | ModelDeployment |
|                      |     | customerprofile | +NaïveBayes)    |                 |
andIntegration
Visualizations,
Simulation/What-If
Usagebehavior,
| [25] Churnprediction |     |     | CoxRegression | Analysis,Segmentation |
| -------------------- | --- | --- | ------------- | --------------------- |
customerprofile
andPersonaModeling,
BusinessImpactMetrics
Usagebehavior,
customerprofile,
| [13] Churnprediction |     |     | DecisionTrees | Visualizations |
| -------------------- | --- | --- | ------------- | -------------- |
transactional/business
metrics
[20] Churnprediction Customersupport NeuralNetworks Visualizations
|                      |     | Usagebehavior,customer  |         | ModelDeployment |
| -------------------- | --- | ----------------------- | ------- | --------------- |
| [15] Churnprediction |     |                         | XGBoost |                 |
|                      |     | profile,customersupport |         | andIntegration  |
Usagebehavior,
[8] Churnprediction transactional/business NeuralNetworks BusinessImpactMetrics
metrics,customerprofile

Appl.Sci.2025,15,6508
25of35
Table6.Cont.
| Ref. | Focus | Data | ProposedMethod | Output |
| ---- | ----- | ---- | -------------- | ------ |
Visualizations,
[23] Churnprediction Usagebehavior RandomForest Segmentationand
PersonaModeling
Visualizations,Business
|      |                 | UsageBehavior,  |          | ImpactMetrics,Model |
| ---- | --------------- | --------------- | -------- | ------------------- |
| [21] | Churnprediction |                 | LightGBM |                     |
|      |                 | customerprofile |          | Deploymentand       |
Integration
|      |                 | Usagebehavior,           |                    | Visualizations,Business |
| ---- | --------------- | ------------------------ | ------------------ | ----------------------- |
|      |                 | transactional/business   |                    | ImpactMetrics,Model     |
| [16] | Churnprediction |                          | LogisticRegression |                         |
|      |                 | metrics,customerprofile, |                    | Deploymentand           |
|      |                 | customersupport          |                    | Integration             |
Usagebehavior,
|      |                 | transactional/business |              | ModelDeployment |
| ---- | --------------- | ---------------------- | ------------ | --------------- |
| [17] | Churnprediction |                        | RandomForest |                 |
|      |                 | metrics,customer       |              | andIntegration  |
profile,satisfaction
Usagebehavior,
Segmentationand
|      | Customerlifetime | transactional/business |          |                  |
| ---- | ---------------- | ---------------------- | -------- | ---------------- |
| [38] |                  |                        | LightGBM | PersonaModeling, |
|      | value            | metrics,customer       |          |                  |
BusinessImpactMetrics
profile,financial
Visualizations,
Simulation/What-If
Customerlifetime Transactional/business Analysis,BusinessImpact
| [36] |       |                   | RandomForest |               |
| ---- | ----- | ----------------- | ------------ | ------------- |
|      | value | metrics,financial |              | Metrics,Model |
Deploymentand
Integration
Simulation/What-If
Analysis,Model
| [29] | Userengagement | marketing/trials | LASSORegression |     |
| ---- | -------------- | ---------------- | --------------- | --- |
Deploymentand
Integration
Visualizations,Model
Heuristicand
| [34] | Userengagement | Usagebehavior |     | Deploymentand |
| ---- | -------------- | ------------- | --- | ------------- |
FuzzyMining
Integration
Simulation/What-If
Usagebehavior,
| [30] | Userretention |     | LASSORegression | Analysis,Business |
| ---- | ------------- | --- | --------------- | ----------------- |
survey/interview,marketing
ImpactMetrics
Simulation/What-If
Reinforcement
[26] Userretention Customerprofile,satisfaction Analysis,Business
learning
ImpactMetrics
Usagebehavior,customer
| [37] | Userretention |     | LinearMixedModels | Visualizations |
| ---- | ------------- | --- | ----------------- | -------------- |
profile,survey/interview
PLS-SEM(Partial
User
|      |                   | Usagebehavior,customer   | LeastSquares       |                |
| ---- | ----------------- | ------------------------ | ------------------ | -------------- |
| [31] | satisfaction/user |                          |                    | Visualizations |
|      |                   | profile,survey/interview | StructuralEquation |                |
loyalty
Modeling)
|     | User |     | AQUAman |     |
| --- | ---- | --- | ------- | --- |
[33] satisfaction/user Usagebehavior,satisfaction negotiation Visualizations
|     | loyalty |     | mechanism |     |
| --- | ------- | --- | --------- | --- |

Appl.Sci.2025,15,6508 26of35
Table6.Cont.
Ref. Focus Data ProposedMethod Output
User Usagebehavior,customer Visualizations,Model
Comparative
[35] satisfaction/user support,satisfaction, Deploymentand
analysis
loyalty survey/interview Integration
User Usagebehavior, Segmentationand
[32] satisfaction/user transactional/business LogisticRegression PersonaModeling,
loyalty metrics,marketing BusinessImpactMetrics
Usagebehavior, UMAPand Segmentationand
[27] Usersegmentation
survey/interview HDBSCAN PersonaModeling
Usagebehavior,
Segmentationand
[28] Usersegmentation transactional/business XGBoost
PersonaModeling
metrics
5.1. InsightsandStrategicRecommendations
From many of the reviewed systems derived various actionable predictions and
recommendations, such as identifying customers at high risk of churning, estimating
potentialrevenueloss,oradvisingonoptimalpricingstrategies. Oneofthemostconsistent
themesacrossresearchwastheuseofmachinelearningtoflagcustomerslikelytochurn.
Studiessuchas[14]concludedthatnewerB2Bcustomersareparticularlyvulnerableto
churn,whilethosewithlowmonthlypaymentsoftenexhibithigherloyalty,suggesting
thatrandomforestsarewell-suitedforB2BSaaSduetotheirinterpretabilityandscalability.
Pricingstrategiesalsoplayapivotalroleinuserretention. Forinstance,research[36]
concludedthatasignificantpercentageofusersprefertransparentbillingandproposeda
dynamicpricingformulathatfactorsinbaserates,usagemetrics,andriskadjustments.The
studyrecommendedgradientboostingforcomplexpricingenvironmentswheretraditional
modelsmayfallshort. Additionally,research[32]revealedthatmulti-productsubscrip-
tionsimprovedretentionbutcautionedagainstover-relianceonbundling,notingregional
variationsinloyalty. Furthersupportingpricingadjustments,research[8]identifiedthat
highfeescombinedwithlowsessionactivitystronglycorrelatewithchurn,suggestingthat
SaaSprovidersshouldconsiderflexiblepricingforlow-engagementusers.
Additionally,otherresearchersproposedbest-practicepolicies,liketrialdurations,
onboardingflows,andpricingtactics,tohelpSaaSprovidersalignproductdecisionswith
userbehaviorandretentiontrends. Study[30]recommendeddefaultingto7-daytrials
unlesssegmentationsuggestslongerones,whileauthorsof[31]highlightedthatintuitive
UI design can boost satisfaction and increase loyalty by 41%. Additionally, work [26]
advisedgradualqualityadjustmentstobettermatchuserperceptions,andwork[33]set
performancebenchmarkssuchas90%acceptabilityratesinnegotiationsystems. Onboard-
ing strategies, according to [34], should center around key activation points, while the
workpresentedin[37]encouragedCRM-styleengagement,includingintranetbanners,to
maintainuserinvolvement.
In[22]theauthorsdemonstratedthatearlyonboardingmetricsarestrongpredictors
oflong-termretention. Thestudyachievedan88.75%recallrateinpredictingpost-tutorial
churn,underscoringtheimportanceofmonitoringearlyuserbehavior. Similarly,thework
presented in [20] linked negative sentiment in support tickets to churn, advocating for
sentimentanalysisalongsideusagelogstocreateariskassessmentframework. Inanother
study[19],theauthorsfoundthatlowAPIorintegrationusageandinfrequentsupport
interactions are reliable churn signals, making these metrics essential for prioritizing
retentionefforts.

Appl.Sci.2025,15,6508 27of35
Otherresearch[13,23]highlightedthatselectingtherightmachinelearningmodel
iscrucialforeffectivechurnpredictionhighlightingthetrade-offsbetweendifferentap-
proaches. Forexample,theauthorsin[13]compareddecisiontreesandrandomforests,
findingthatdecisiontreesexcelinrecall,makingthemidealforminimizingmissedchurn
risks,whilerandomforestsofferbetterF1-scores,whichmaybepreferablewhenbalancing
precision and recall. Meanwhile, research [23] achieved near-perfect predictive perfor-
mancewithanAUCofapproximately0.99butwarnedagainstneuralnetworksdueto
theirtendencytodegradeovertimewithoutfrequentretraining. Ontheoperationalside,
authors in [16] highlighted the computational cost of XGBoost, noting that it produces
335%higheremissionsthanlogisticregression,andrecommendedcloud-basedsolutions
forscalabilityandefficiency.
Measuring the financial impact of churn ensures that retention efforts align with
businessobjectives. Theworkpresentedin[38]demonstratedhowCLVpredictionscan
optimizebudgetallocation,ensuringmarketingspendingtargetshigh-valueusers.Another
key insight comes from [29], which found that organic search ads outperformed email
campaignsindrivingconversions,cautioningagainstoverlyaggressiveretentiontactics
thatmayalienateusers.
Finally,theimportanceofaddressingcomputationaldemandsandsustainabilityin
SaaSsystemswashighlightedbystudies[14,16,19,36]. Keyrecommendationsincluded
optimizing models for cloud deployment, minimizing carbon footprints, and ensuring
scalableinfrastructureforreal-time,high-volumeapplications. Forinstance, study[14]
pointedoutthesignificantcomputationalrequirementsofdeeplearningmodels,particu-
larlyforlargefirms. Inaddition,theauthorsin[19]focusedondesigningmodelssuitedfor
cloud-basedSaaSenvironments,whileinstudy[16]theauthorsevaluatedtheenvironmen-
talimpact,specificallythecarboncost,ofmodeltraining. Tosupportscalability,authors
in[36]recommendedhybridcomputingapproaches,especiallyforhigh-demandsystems
likebilling.
5.2. SelectionofOptimalMachineLearningModelforDecision-Making
Selectingtheoptimalmachinelearningmodeldependsonthespecificusecase. The
initialdecisionforaSaaSprovideristodeterminetheprimarybusinessobjectivedriving
the need for machine learning. If the goal is the churn prediction, which is the most
frequentlycitedusecase,theprovidershouldassesswhethertheirdatasetconsistsprimarily
of structured behavioral and transactional data. If the data is rich in clickstream logs,
usersessions,orsubscriptiondata,ensemblemodelssuchasRandomForestorXGBoost
standoutduetotheirstrongperformanceinpredictiveaccuracyandfeatureimportance
insights. Thesemodelsareparticularlyeffectivewheninterpretabilityandscalabilityare
important,especiallyinBusiness-to-Business(B2B)contextswhereclearjustificationfor
churnpredictionsisessential.
However,inusecaseswhereuserbehaviorevolvesovertime,forinstance,infreemium
gamesorSaaSproductswithhighsessionvariability[23],hybridarchitecturesthatintegrate
static and time-dependent features into LSTM networks (such as subscription age or
paymenthistory)shouldbeconsidered. Thesemodelsbettercapturetemporaldynamics
and early disengagement signals but at the cost of increased complexity and training
resources. ForSaaSvendorsrequiringreal-timedeploymentorlow-latencypredictions,
LightGBMoffersacompellingbalancebetweenperformanceandcomputationalefficiency
andisespeciallysuitableforstreamingcontextsorintegrationintocloud-basedplatforms.
Forusecasesfocusingonusersegmentation,wherethegoalistogroupusersinto
interpretablepersonasorstrategicmarketinggroups,thenatureoftheinputdataplays
apivotalrole. Ifthedataincludesdemographic,firmographic,andbehavioralattributes,

Appl.Sci.2025,15,6508 28of35
thentraditionalclusteringmethodslikeK-meansarepreferredforidentifyingmeaningful
segments,especiallywhenenhancedwithdimensionalityreductiontechniquessuchas
UMAPorHDBSCANtohandlesparsedatasets[26]. Theseapproachessupportexploratory
analysisandarevaluablewhenstrategicalignmentwithqualitativeinsightsfromsurveys
orinterviewsisrequired.
ForpredictingCLVinB2Benvironments,wherehistoricalbillingdata,engagement
metrics,andfirmographicfeaturessuchascompanysizeorindustryplayacriticalrole,
hierarchicalensemblemodelssuchasLightGBMwereparticularlyeffective. Thesemodels
deliverstrongpredictiveaccuracyandcanbepairedwithtime-seriestechniqueslikeAuto
ARIMAtocapturerevenuetrendsacrossdifferentcustomersegments[37]. Additionally,
LASSOregressionwasappliedinthiscontexttoenhancemodelinterpretabilityandstability
byselectingkeypredictivefeaturesinhigh-dimensionaldatasets. Thisapproachallows
SaaSproviderstoidentifyandprioritizehigh-valueaccounts,allocatemarketingresources
moreefficiently,andoptimizelong-termrevenuestrategies.
Ifthefocusisonuserengagement,satisfaction,orloyalty,thedecisionisagainbased
on the type of available data. For use cases involving UI/UX feedback, support ticket
sentiment,oronboardingflows,vendorsshouldconsiderdeeplearningmodels(likeMLP
orsentiment-enhancedLSTM)onlyiftheyhavelargedatasetsandneedtoidentifysubtle
trends. Forsmallerdatasetsorwhenmodelexplainabilityisprioritized,logisticregression
orPLS-SEMmodelsprovideinterpretableinsightsandcanbeusedtoconnectinterface
designorfeatureadoptiontoengagementmetrics.
Whenthebusinessobjectiverevolvesarounddynamicpricingortrialoptimization,
wherescenariotestingandprofitabilityforecastingarekey,modelsmustsupportwhat-if
simulations and business impact metrics. In these cases, gradient boosting techniques
(XGBoost,GBM),orLASSOregressionareoptimalduetotheirabilitytomodelnonlinear
relationshipsandprovidestablecoefficientsforstrategicleversliketrialdurationorusage-
basedpricing. SaaSplatformsfeaturingdynamicpricingmodelsmayalsobenefitfrom
reinforcementlearningtoadjustpricesinresponsetouserbehaviorandnetworkeffects
overtime.
Finally,forthechoiceoftheappropriatemachinelearningmodel,deploymentand
sustainabilityconstraintsshouldbeconsidered. ForSaaSvendorswithlimitedengineering
capacity or requiring real-time predictions integrated into CRM systems, models like
RandomForest,XGBoost,orLightGBMcanbedeployedviaRESTAPIsorembeddedin
cloudMLpipelines(asinAWSSageMaker).Additionally,inenergy-sensitiveenvironments,
vendorsshouldprefercomputationallylightweightmodelsandmonitorcarbonemissions,
asstudiesshowedlargeenvironmentalvariancesbetweenarchitectures.
Although the primary focus of the reviewed papers was on the performance and
utility of data-driven decision support systems in SaaS, interpretability was also a key
considerationinseveraloftheexaminedstudies.Forinstance,paper[15]employedLogistic
Regression, a model valued for its transparency, and visualized its coefficients to help
stakeholdersunderstandhowdifferentusagefactorsaffectchurnpredictions. Likewise,
the paper [16] emphasized explainability by analyzing feature importance in Random
ForestandLogisticRegressionmodelstorevealkeychurndrivers,evenwhenpredictive
performancewasmodest. Otherstudiessuchas[12,13,22]alsousedinterpretablemodels
(such as Decision Trees) or feature importance plots to support decision-making with
understandableinsights.
Figure4illustratestherecommendedactionsforselectingtheoptimalMLmodelbased
onthespecificusecaseandcontextasderivedfromtheresultsofthereviewedpapers.

Appl.Sci.2025,15,6508 29of35
Figure4.TaxonomyforMLalgorithmsselectionforSaaSproviders.
However, explainability techniques such as SHAP (SHapley Additive exPlana-
tions)[55]orLIME(LocalInterpretableModel-agnosticExplanations)[56]werenotem-
ployed by the reviewed papers. SHAP is a method used to explain the output of any
machinelearningmodelbyquantifyingthecontributionofeachinputfeaturetoaspecific
prediction. ItutilizestheconceptofShapleyvaluesfromgametheorytodeterminethe
importanceofeachfeature. LIMEisaninterpretationtechniqueusedtoexplainthepredic-
tionsofanyblackboxmachinelearningmodel. LIMEapproximatesacomplexmodel’s
predictionwithasimpler,interpretablemodel,focusingonindividualpredictionsrather
thanthemodelasawhole. ThechoicebetweenSHAPandLIMEdependsonthespecific
needsofthetask. SHAPisidealwhenaccuracy,consistency,andfairnessarepriorities,
especially in regulated settings or with tree-based models like XGBoost. LIME, on the
other hand, is useful for quick, model-agnostic explanations during development, and
works well with various data types. Its simplicity makes it great for explaining results
to non-technical users. Ultimately, the adoption of such techniques could significantly
improvestakeholderconfidenceinautomateddecisionsandsupporterrordiagnosis,bias
detection,andregulatorycompliance.
Moreover,explicitconsiderationsofalgorithmicfairness,privacyprotection,orethical
implications seem to be largely absent. Future research should address those gaps by
incorporatingsuchexplainabilitytechniquesintomachinelearningmodelsandconsider
theincorporationofprivacy-preservingtechniquessuchasdifferentialprivacy[57],feder-
atedlearning[58]andsecuremulti-partycomputation,whichcanenablemodeltraining
on sensitive user data without compromising user confidentiality. Additionally, incor-
poratingalgorithmicfairnessassessmentsintothedevelopmentpipelinecouldprevent
discriminatoryoutcomessuchasbiasedchurnpredictions. AsSaaSsolutionsincreasingly
influencestrategicdecisionslikemarketing,pricing,orretentioninvestments,itiscritical
to ensure that automated recommendations do not reinforce inequalities or introduce
unfairtreatment.
Even though carbon footprint should be taken into consideration, only two stud-
ies [13,15] measured how machine learning model selection affects carbon emissions.
Study[15]examinedtheenvironmentalimpactofmachinelearninginB2Bchurnpredic-

Appl.Sci.2025,15,6508 30of35
tion,analyzingthetrade-offsbetweenmodelaccuracyandcarbonemissions. Usingan
AMDEPYC7763processor(280W)andEuropeanemissionsdata(296.96gCO /kWh),
2
theresearchquantifiedCO eqemissionsinrelatableterms. Theresultsrevealedthateven
2
basicpreprocessing,suchasfeaturecreation,emits86.379gCO eq,whilemodeltraining
2
introducedfargreatercosts. Theinclusionofmultipleusagefeaturesresultinginahigh
dimensionaldataset,significantlyaffectedthecarbonfootprintproducedbythereviewed
machine learning methods. Specifically, Decision Trees and Random Forests showed a
~200%riseinemissions(DT:2.349gCO eqto4.044g;RF:1.350gto4.044g). XGBoost’s
2
emissions rose by 335% (21.29 g CO eq), and SVM increased by 50% (40.99 g CO eq),
2 2
whereasLogisticRegressionremainedefficient(2.349gCO eq).
2
However,themoststrikingenvironmentalcostsseemedtoderivefromdeeplearn-
ingandcomplexensemblemethods. Instudy[13],aDeepNeuralNetwork(DNN)with
twohidden layers (32/64 neurons) achieved a high accuracy percentage but at a high
computationalexpense,scalingconsiderablyasmodelcomplexionincreased. Similarly,
RandomForestprovedresource-intensive,withcostsgrowingalongsidetreedepthand
featurecomplexity. BothDNNandRFrequiredparallelcomputationtotrainefficiently
andusedupalloftheavailableprocessorsindicatingtheirhighresourceconsumptionin
comparisonwiththerestofthereviewedmodels. Althoughadvancedmodelsseemedto
improveprediction,theirenergydemandsmakethemunsustainableforfirmswithoutop-
timizedinfrastructure. Thestudyconcludedthatbusinesses,especiallysmallerenterprises,
should prioritize energy-efficient algorithms (like Logistic Regression) or cloud-based
solutionstoreduceenvironmentalimpact.
Although several of the reviewed studies experimented with deployment aspects,
suchasstandalonereal-timeapplications[5],CRM-integrateddashboardsfordecisionsup-
port[14],cloud-basedpredictionAPIs[29],andreal-timedatastreamingusingplatforms
like AWS SageMaker [20], these efforts primarily emphasize centralized, cloud-centric
architectures. Anemergingdirectionforreal-worlddeploymentofdecisionsupportsys-
tems in SaaS would involve combining centralized model training with decentralized
inferencethroughedgecomputing[59],particularlyinsettingsinvolvingIoTdevicesor
localclients. Followingthis,machinelearningmodelsaretrainedinthecloud,oftenvia
MLaaSplatformsthatprovidescalablecomputingresources,versioningandmonitoring,
andthendeployedtoedgedevicesforlocalinference. Thisapproachcouldpotentiallyoffer
keybenefitssuchasreducedlatency,improvedbandwidthefficiency,offlinefunctionality,
andenhancedprivacy,aspredictionscanbemadewithouttransmittingsensitivedataback
tothecloud.
6. ConclusionsandFutureWork
Thisworkprovidedascopingreviewofdata-drivendecisionsupportsystems(DSSs)
withinSaaSenvironments,highlightingcurrentadvances,practices,andgaps. Through
anextensiveanalysisofrecentliterature,ithasbecomeclearthatearlychurnprediction,
customersegmentation,andpersonalizedengagementstrategiesarecriticalforsustaining
growthandprofitabilityinSaaSbusinesses. Churnreductionemergesasthepredominant
researchobjective,withstudiesfocusingontheidentificationofat-riskusersandproposing
targeted, data-driven interventions. From a methodological perspective, it was found
thatRandomForestandXGBoostalgorithmsconsistentlyoutperformedothermachine
learningmodelsinchurnpredictiontasks,particularlywhendealingwithtabularbehav-
ioralandtransactionaldata. Additionally,hybridmodelscombiningstaticandsequential
featureshaveshownsuperiorpredictiveperformance,suggestingthatintegratingdiverse
datasourcescanenhancemodelrobustness. However,simplermodelslikeLogisticRe-

Appl.Sci.2025,15,6508 31of35
gressionremainvaluablefortheirinterpretability,particularlyinresource-constrainedor
real-timeapplications.
Beyondpredictivemodeling,researchemphasizedtheimportanceofusersegmenta-
tionandpersonamodelingforcreatingpersonalizedengagementstrategies. Keydriversof
long-termretentionidentifiedacrossstudiesincludeUI/UXquality,effectiveonboarding
(suchas“ahamoments”),flexiblepricingstrategies,andproactivesupportinterventions.
Moreover, linking predictive outputs to business impact metrics such as CLV, Monthly
RecurringRevenue(MRR),andretention-relatedROIhaveprovenessentialforbridging
analyticswithexecutivedecision-making.
Intermsofpracticalapplications,manystudiesadvocatedforreal-timedeployment
ofpredictivemodelsthroughCRMintegrations,APIs,anddashboardvisualizations. This
operationalizationensuresthatinsightsleadtoimmediateactions,supportingdynamic
marketing, retention, and customer success initiatives. Moreover, choosing the right
machinelearningmodelforaSaaSproviderdependsonthebusinessgoalanddatatype.
For churn prediction, ensemble models like Random Forest and XGBoost are ideal for
structured behavioral data, offering accuracy and interpretability. When user behavior
changes over time, LSTM-based models are better suited, though more complex. For
real-timeuse,LightGBMbalancesspeedandperformance. Inusersegmentationusecases,
modelslikeK-meansworkwellwhencombinedwithdimensionalityreductiontechniques,
especiallywithdiverseuserdata. ForCLVpredictions,LightGBMandLASSOregression
provide accurate and interpretable insights, particularly when paired with time-series
models. Regardinguserengagementandsatisfactionanalysis,deeplearningmodelsare
usefulforlargedatasets,whilelogisticregressionorPLS-SEMofferclaritywithsmaller
ones. Indynamicpricing, XGBoostorreinforcementlearningsupportsstrategytesting
andadaptivepricing. Finally,deploymentrequirementsandenergyefficiencyarecritical
considerations. Models such as LightGBM, XGBoost, and Random Forest are not only
knownfortheirstrongperformancebutarealsorelativelystraightforwardtodeployvia
RESTAPIsorintegrateintocloud-basedmachinelearningpipelines. However,inresource-
constrainedorenergy-sensitivesettings,wherecomputationalloadandsustainabilityare
priorities,lighter-weightmodels,suchaslogisticregressionordecisiontreesshouldbe
prioritized to reduce infrastructure costs and minimize environmental impact without
sacrificingessentialperformance.
However,despitetheconsiderableprogressinresearch,severalchallengesandopen
researchdirectionspersist. Machinelearningmodelsmayexhibitperformancedegradation
overtimeorstruggletoadapttoevolvinguserbehavior,highlightingtheneedfordynamic
modelmonitoringandcontinuallearningmechanisms. Inordertoensurethatdeveloped
DSSsremaineffective,monitoringmechanismsshouldbeestablished. Ensuringtraining
dataisuptodateandmachinelearningmodelsmaintaingoodaccuracylevelsiscrucial.
Batchtrainingofmachinelearningmodelsmaybeagoodstartingpointbutwillnotbe
sustainable in the long term as data volume increases. To this end, periodically batch
trainingofthemodelsand/orreal-timetrainingincrementallyupdatingthemodelscould
beexploredinordertoensuredataintegrity. Therefore,MLaaSsolutions[60]specifically
designedforsupportingdecision-makinginSaaSareofgreatimportancesincetheycan
providemonitoringandupdatingmechanismsreadytouseassuringtheefficiencyofDSSs.
Meanwhile,theenvironmentalimpactofmachinelearningimplementationsemerged
asanothercriticalconsideration. Comparativeanalysisrevealedthatcomplexensemble
methodsanddeepneuralnetworkscanincurhighercomputationalcostsandcarbonemis-
sionsthansimplermodelalternatives,underscoringtheimportanceofbalancingpredictive
performance with sustainability, particularly for SaaS companies managing significant
computationalworkloads. Futureresearch,exceptforseekinggreenerarchitectures,could

Appl.Sci.2025,15,6508 32of35
alsoemphasizeclearlyexplainingthetrade-offsbetweenaccuracymetricsandenviron-
mentalfootprint. Informingusersofenergyconsumptionandcarbonemissionscancreate
awarenessandleadtomoreenvironmentallyfriendlymodelselectiondecisionslikesmaller
architecturesandtheuseoftechniqueslikeearlystoppingandtransferlearning.
Asdecision-makingincreasinglyreliesonautomatedsystems,ensuringtheexplain-
ability,fairness,andtransparencyofpredictions,particularlyinchurnriskassessments,
will be critical. SaaS vendors need to have a clear view of what is happening in their
businessatanytimeandacttowardsimprovinguserexperienceandultimatelyincreas-
ingKPIsthatarevitalfortheirbusiness. Therefore,it’simportantthatDSSsjustifytheir
recommendeddecisionsandprovideclearguidanceonwhatactionsshouldbetaken. To-
wardsthisdirection,DSSscanutilizeinterpretablemachinelearningmodelstojustifytheir
decision-makingprocesses. Posthocmethodsfornon-interpretablemodelssuchasSHAP
values [55] and LIME [56] can be used to provide explanations on models’ predictions
allowing vendors to understand what influences the decisions. While both SHAP and
LIMEoffervaluableinsights,theyservedistinctpurposes. ForSaaSproviders,SHAPmay
bepreferableforstrategicdecision-makingandbiasdetection,whileLIMEcouldbetter
supportcustomer-facingteamsneedingimmediate,case-specificexplanations.
NaturallanguageUIcouldalsobeexploredtoprovideaneasierandfriendlierwayto
provideguidancetoSaaSvendors. LargeLanguageModels(LLMs)couldbeemployed
tounderstanduser’sintentandexplainrecommendedactions,forexampleforreducing
churnorincreasinguserengagement. ComplicatedtoolsandUIsarenotthebestchoicefor
supportingSaaSprofessionals. Theyneedtostayaheadofthecompetitionandactfastand
efficiently. Providingclearexplanationsinnaturallanguageandsuggestingasetofactions
toperformcouldadjustbettertobusyschedulesandofferclarity.
Additionally,futuresystemsmaybenefitfromrefinedpersonalizationstrategiesdriven
bycontext-awarerecommendations,dynamicallyadaptingtoeachuser’slifecyclestageand
dynamicprofile. Inparticular,theDSSswouldrecommendapersonalizedcourseofactions
tailoredtoeachuser’sholisticprofilewhichwillbedynamicallyupdated. Ultimately,the
developmentofintelligent,adaptive,andsustainabledecisionsupportsystemswillbea
keydifferentiatorforSaaSprovidersseekingtobuildresilient,customer-centricbusinesses
inanincreasinglycompetitiveanddynamicmarketplace.
AuthorContributions:Conceptualization,E.M.;methodology,E.M.;formalanalysis,E.M.andG.C.;
investigation,G.C.;resources,G.C.;datacuration,E.M.andG.C.;writing—originaldraftpreparation,
E.M.andG.C.;writing—reviewandediting,E.V.,T.K.andG.A.P.;visualization,E.M.;supervision,
G.A.P.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Bokhari,M.U.;Shallal,Q.M.;Tamandani,Y.K.CloudComputingServiceModels: AComparativeStudy. InProceedingsof
the20163rdInternationalConferenceonComputingforSustainableGlobalDevelopment(INDIACom),NewDelhi,India,
16–18March2016;pp.890–895.
2. Mohammed,C.M.;Zeebaree,S.R.M.SufficientComparisonAmongCloudComputingServices:IaaS,PaaS,andSaaS:AReview.
Int.J.Sci.Bus.2021,5,17–30.
3. Cusumano,M.CloudComputingandSaaSasNewComputingPlatforms.Commun.ACM2010,53,27–29.[CrossRef]
4. Kumar,K.V.K.M.Softwareasaserviceforefficientcloudcomputing.Int.J.Res.Eng.Technol.2014,3,178–181.[CrossRef]
5. Tsai,W.;Bai,X.;Huang,Y.Software-as-a-Service(SaaS):PerspectivesandChallenges.Sci.ChinaInf.Sci.2014,57,1–15.[CrossRef]
6. Berger,P.D.;Nasr,N.I.CustomerLifetimeValue:MarketingModelsandApplications.J.Interact.Mark.1998,12,17–30.[CrossRef]

Appl.Sci.2025,15,6508 33of35
7. Wang,R.;Ying,S.;Jia,X.LogDataModelingandAcquisitioninSupportingSaaSSoftwarePerformanceIssueDiagnosis.Int.J.
Softw.Eng.Knowl.Eng.2019,29,1245–1277.[CrossRef]
8. Morozov,V.;Mezentseva,O.;Kolomiiets,A.;Proskurin,M.PredictingCustomerChurnUsingMachineLearninginITStartups.
InLectureNotesinComputationalIntelligenceandDecisionMaking,2021InternationalScientificConference“IntellectualSystemsof
Decision-makingandProblemsofComputationalIntelligence”;Springer:Berlin/Heidelberg,Germany,2022;pp.645–664.
9. Manzoor,A.;AtifQureshi,M.;Kidney,E.;Longo,L.AReviewonMachineLearningMethodsforCustomerChurnPrediction
andRecommendationsforBusinessPractitioners.IEEEAccess2024,12,70434–70463.[CrossRef]
10. Heilig,L.;Voß,S.DecisionAnalyticsforCloudComputing:AClassificationandLiteratureReview.InBridgingDataandDecisions;
INFORMS:Catonsville,MD,USA,2014;pp.1–26.[CrossRef]
11. Arora,S.;Thota,S.R.;Gupta,S.ArtificialIntelligence-DrivenBigDataAnalyticsforBusinessIntelligenceinSaaSProducts.In
Proceedingsofthe2024FirstInternationalConferenceonPioneeringDevelopmentsinComputerScience&DigitalTechnologies
(IC2SDT),Delhi,India,2–4August2024;IEEE:NewYork,NY,USA,2024;pp.164–169.
12. Ge,Y.;He,S.;Xiong,J.;Brown,D.E.CustomerChurnAnalysisforaSoftware-as-a-ServiceCompany.InProceedingsofthe2017
SystemsandInformationEngineeringDesignSymposium(SIEDS),Charlottesville,VA,USA,28April2017;IEEE:NewYork,NY,
USA,2017;pp.106–111.
13. Phumchusri,N.;Amornvetchayakul,P.MachineLearningModelsforPredictingCustomerChurn:ACaseStudyinaSoftware-
as-a-ServiceInventoryManagementCompany.Int.J.Bus.Intell.DataMin.2024,24,74–106.[CrossRef]
14. Mezentseva,O.V.;Kolesnikova,K.;Kolomiiets,A.CustomerChurnPredictionintheSoftwarebySubscriptionModelsITBusiness
UsingMachineLearningMethods.InProceedingsoftheInternationalWorkshoponInformationTechnologies:Theoreticaland
AppliedProblems,Ternopil,Ukraine,16–18November2021.
15. Dias,J.R.;Antonio,N.PredictingCustomerChurnUsingMachineLearning:ACaseStudyintheSoftwareIndustry.J.Mark.Anal.
2025,13,111–127.[CrossRef]
16. SanchezRamirez,J.;Coussement,K.;DeCaigny,A.;Benoit,D.F.;Guliyev,E.IncorporatingUsageDataforB2BChurnPrediction
Modeling.Ind.Mark.Manag.2024,120,191–205.[CrossRef]
17. Sergue,M.CustomerChurnAnalysisandPredictionUsingMachineLearningforaB2BSaaSCompany.Master’sThesis,KTH
RoyalInstituteofTechnology,Stockholm,Sweden,2020.
18. Saias,J.;Rato,L.;Gonçalves,T.AnApproachtoChurnPredictionforCloudServicesRecommendationandUserRetention.
Information2022,13,227.[CrossRef]
19. Thota,S.R.;Arora,S.;Gupta,S.HybridMachineLearningModelsforPredictiveMaintenanceinCloud-BasedInfrastructurefor
SaaSApplications.InProceedingsofthe2024InternationalConferenceonDataScienceandNetworkSecurity(ICDSNS),Tiptur,
India,26–27July2024;IEEE:NewYork,NY,USA,2024;pp.1–6.
20. Gajananan,K.;Loyola,P.;Katsuno,Y.;Munawar,A.;Trent,S.;Satoh,F.ModelingSentimentPolarityinSupportTicketDatafor
PredictingCloudServiceSubscriptionRenewal.InProceedingsofthe2018IEEEInternationalConferenceonServicesComputing
(SCC),SanFrancisco,CA,USA,2–7July2018;IEEE:NewYork,NY,USA,2018;pp.49–56.
21. Chakraborty,A.;Raturi,V.;Harsola,S.BBE-LSWCM:ABootstrappedEnsembleofLongandShortWindowClickstreamModels.
InProceedingsofthe7thJointInternationalConferenceonDataScience&ManagementofData(11thACMIKDDCODSand
29thCOMAD),Bangalore,India,4–7January2024;ACM:NewYork,NY,USA,2024;pp.350–358.
22. Hoang,H.D.;Cam,N.T.EarlyChurnPredictioninFreemiumGameMobileUsingTransformer-BasedArchitectureforTabular
Data. InProceedingsofthe2024IEEE3rdWorldConferenceonAppliedIntelligenceandComputing(AIC),Gwalior,India,
27–28July2024;IEEE:NewYork,NY,USA,2024;pp.568–573.
23. Rothmeier,K.;Pflanzl,N.;Hullmann,J.A.;Preuss,M.PredictionofPlayerChurnandDisengagementBasedonUserActivity
DataofaFreemiumOnlineStrategyGame.IEEETrans.Games2021,13,78–88.[CrossRef]
24. Kristensen,J.T.;Burelli,P.CombiningSequentialandAggregatedDataforChurnPredictioninCasualFreemiumGames. In
Proceedingsofthe2019IEEEConferenceonGames(CoG),London,UK,20–23August2019;IEEE:NewYork,NY,USA,2019;
pp.1–8.
25. Karmakar,B.;Liu,P.;Mukherjee,G.;Che,H.;Dutta,S.ImprovedRetentionAnalysisinFreemiumRole-PlayingGamesbyJointly
ModellingPlayers’Motivation,ProgressionandChurn.J.R.Stat.Soc.Ser.AStat.Soc.2022,185,102–133.[CrossRef]
26. Pang,L.;Hu,Z.;Liu,Y.HowtoRetainPlayersthroughDynamicQualityAdjustmentinVideoGames.InProceedingsofthe
2021IEEE5thAdvancedInformationTechnology,ElectronicandAutomationControlConference(IAEAC),ChongqingChina,
12–14March2021;IEEE:NewYork,NY,USA,2021;pp.154–160.
27. Boyle,R.E.;Pledger,R.;Brown,H.-F.IterativeMixedMethodApproachtoB2BSaaSUserPersonas.Proc.ACMHum.Comput.Interact.
2022,6,1–44.[CrossRef]
28. Mali,M.;Mangaonkar,N.BehavioralCustomerSegmentationForSubscription.InProceedingsofthe20233rdAsianConference
onInnovationinTechnology(ASIANCON),Pune,India,25–27August2023;IEEE:NewYork,NY,USA,2023;pp.1–6.

Appl.Sci.2025,15,6508 34of35
29. Li,H.(Alice)ConvertingFreeUserstoPaidSubscribersintheSaaSContext:TheImpactofMarketingTouchpoints,Message
Content,andUsage.Prod.Oper.Manag.2022,31,2185–2203.[CrossRef]
30. Yoganarasimhan,H.;Barzegary,E.;Pani,A.DesignandEvaluationofPersonalizedFreeTrials. arXiv2020,arXiv:2006.13420.
[CrossRef]
31. Harahap,E.P.;Hermawan,P.;Kusumawardhani,D.A.R.;Rahayu,N.;Komara,M.A.;Agustian,H.UserInterfaceDesign’sImpact
onCustomerSatisfactionandLoyaltyinSaaSE-Commerce.InProceedingsofthe20243rdInternationalConferenceonCreative
CommunicationandInnovativeTechnology(ICCIT),Tangerang,Indonesia,7–8August2024;IEEE:NewYork,NY,USA,2024;
pp.1–6.
32. vanBelle,E.P.J.Data-DrivenDriversofCustomerLoyaltyinaBusiness-to-BusinessEnvironmentfortheSoftwareasaService
Industry.Master’sThesis,EindhovenUniversityofTechnology,Eindhoven,TheNetherlands,2022.
33. Najjar,A.;Boissier,O.;Picard,G.Elastic&Load-SpikeProofOne-to-ManyNegotiationtoImprovetheServiceAcceptabilityofan
OpenSaaSProvider.InAutonomousAgentsandMultiagentSystems,ProceedingsoftheAAMAS2017Workshops,BestPapers,São
Paulo,Brazil,8–12May2017,RevisedSelectedPapers;Springer:Berlin/Heidelberg,Germany,2017;pp.1–20.
34. Chiang,W.-H.;Ahmad,U.;Wang,S.;Bukhsh,F.InvestigatingAhaMomentThroughProcessMining.InProceedingsofthe25th
InternationalConferenceonEnterpriseInformationSystems,Prague,CzechRepublic,24–26April2023;SCITEPRESS—Science
andTechnologyPublications:Setúbal,Portugal,2023;pp.164–172.
35. Ahlgren,O.;Dalentoft,J.CollectingandIntegratingCustomerFeedback:ACaseStudyofSaaSCompaniesWorkingB2B.Master’s
Thesis,LundUniversity,Lund,Sweden,2020.
36. Kumar,G.S.C.;Dhanalaxmi,B.LeveragingUsage-BasedSaaSModels:OptimizingRevenueandUserExperience.Knowl.Trans.
Appl.Mach.Learn.2025,3,12–17.[CrossRef]
37. Baumann,E.;Kern,J.;Lessmann,S.UsageContinuanceinSoftware-as-a-Service.Inf.Syst.Front.2022,24,149–176.[CrossRef]
38. Curiskis,S.;Dong,X.;Jiang,F.;Scarr,M.ANovelApproachtoPredictingCustomerLifetimeValueinB2BSaaSCompanies.
J.Mark.Anal.2023,11,587–601.[CrossRef]
39. Breiman,L.RandomForests.Mach.Learn.2001,45,5–32.[CrossRef]
40. Ishwaran,H.;Kogalur,U.B.;Blackstone,E.H.;Lauer,M.S.RandomSurvivalForests.Ann.Appl.Stat.2008,2,841–860.[CrossRef]
41. Liaw,A.;Wiener,M.ClassificationandRegressionbyRandomForest.R.News2002,2,18–22.
42. Chen,T.;Guestrin,C.XGBoost.InProceedingsofthe22ndACMSIGKDDInternationalConferenceonKnowledgeDiscovery
andDataMining,SanFrancisco,CA,USA,13–17August2016;ACM:NewYork,NY,USA,2016;pp.785–794.
43. Dreiseitl,S.;Ohno-Machado,L.LogisticRegressionandArtificialNeuralNetworkClassificationModels:AMethodologyReview.
J.Biomed.Inf.2002,35,352–359.[CrossRef]
44. Hastie,T.;Rosset,S.;Zhu,J.;Zou,H.Multi-ClassAdaBoost.Stat.Interface2009,2,349–360.[CrossRef]
45. AlShourbaji,I.;Helian,N.;Sun,Y.;Hussien,A.G.;Abualigah,L.;Elnaim,B.AnEfficientChurnPredictionModelUsingGradient
BoostingMachineandMetaheuristicOptimization.Sci.Rep.2023,13,14441.[CrossRef][PubMed]
46. Rouder,J.N.;Morey,R.D.TeachingBayes’Theorem:StrengthofEvidenceasPredictiveAccuracy.Am.Stat.2019,73,186–190.
[CrossRef]
47. Huang, X.; Khetan, A.; Cvitkovic, M.; Karnin, Z. TabTransformer: Tabular Data Modeling Using Contextual Embeddings.
arXiv2020,arXiv:2012.06678.
48. Ren,J.;Pang,L.;Cheng,Y.DynamicPricingSchemeforIaaSCloudPlatformBasedonLoadBalancing:AQ-LearningApproach.
InProceedingsofthe20178thIEEEInternationalConferenceonSoftwareEngineeringandServiceScience(ICSESS),Beijing,
China,24–26November2017;IEEE:NewYork,NY,USA,2017;pp.806–810.
49. Tibshirani,R.RegressionShrinkageandSelectionviatheLasso.J.R.Stat.Soc.Ser.BStat.Methodol.1996,58,267–288.[CrossRef]
50. vanderAalst,W.ProcessMining;Springer:Berlin/Heidelberg,Germany,2016;ISBN978-3-662-49850-7.
51. Jiang, J.; Nguyen, T.LinearandGeneralizedLinearMixedModelsandTheirApplications; Springer: NewYork, NY,USA,2021;
ISBN978-1-0716-1281-1.
52. Rizopoulos,D.;Verbeke,G.;Molenberghs,G.SharedParameterModelsunderRandomEffectsMisspecification.Biometrika2008,
95,63–74.[CrossRef]
53. Park,S.;Gupta,S.HandlingEndogenousRegressorsbyJointEstimationUsingCopulas.Mark.Sci.2012,31,567–586.[CrossRef]
54. Pereira,I.;Madureira,A.;Bettencourt,N.;Coelho,D.;Rebelo,M.Â.;Araújo,C.;deOliveira,D.A.AMachineLearningasaService
(MLaaS)ApproachtoImproveMarketingSuccess.Informatics2024,11,19.[CrossRef]
55. Lundberg, S.M.; Lee, S.-I. A Unified Approach to Interpreting Model Predictions. In Proceedings of the 31st International
ConferenceonNeuralInformationProcessingSystems,LongBeach,CA,USA,4–9December2017; CurranAssociatesInc.:
RedHook,NY,USA,2017;pp.4768–4777.
56. Ribeiro, M.T.; Singh, S.; Guestrin, C.“WhyShouldITrustYou?”: ExplainingthePredictionsofAnyClassifier. arXiv2016,
arXiv:1602.04938.

Appl.Sci.2025,15,6508 35of35
57. Dwork,C.DifferentialPrivacy. InInternationalColloquiumonAutomata,Languages,andProgramming;Bugliesi,M.,Preneel,B.,
Sassone,V.,Wegener,I.,Eds.;Springer:Berlin/Heidelberg,Germany,2006;pp.1–12.
58. Konecˇn\‘y, J.; McMahan, H.B.; Yu, F.X.; Richtárik, P.; Suresh, A.T.; Bacon, D.FederatedLearning: StrategiesforImproving
CommunicationEfficiency.arXiv2016,arXiv:1610.05492.
59. Shi, W.; Cao, J.; Zhang, Q.; Li, Y.; Xu, L.EdgeComputing: VisionandChallenges. IEEEInternetThingsJ.2016, 3, 637–646.
[CrossRef]
60. GrigoriadisIoannisandVrochidou,E.andT.I.andP.G.A.MachineLearningasaService(MLaaS)—AnEnterprisePerspective.In
ProceedingsoftheInternationalConferenceonDataScienceandApplications,Jaipur,India,14–15July2023;Nanda,S.J.,Yadav,
R.P.,Gandomi,A.H.,Saraswat,M.,Eds.;Springer:Singapore,2023;pp.261–273.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.