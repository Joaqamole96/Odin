Multi-Class Imbalanced Data Handling with Concept Drift in
Fog Computing: A Taxonomy, Review, and Future Directions
FARHANASHARIEF,DepartmentofSoftwareEngineering,UniversityofSargodha,Sargodha,Pakistan
HUMAIRAIJAZ,ComputerScience&IT,UniversityofSargodha,Sargodha,Pakistan
MOHAMMADSHOJAFAR,5G&6GInstituteforCommunicationSystems,UniversityofSurrey,Guild-
ford,UnitedKingdomofGreatBritainandNorthernIreland
MUHAMMADASIFNAEEM,DepartmentofComputerScience,NationalUniversityofComputerand
EmergingSciences,Islamabad,Pakistan
Anetworkofactualphysicalobjectsor“IoTcomponents”linkedtotheinternetandequippedwithsensors,
electronics,software,andnetworkconnectivityisknownastheInternetofThings(IoT).Thisabilityofthe
IoTcomponentstogatherandsharedataismadepossiblebythisnetworkconnectivity.ManyIoTdevicesare
currentlyoperating,whichgeneratealotofdata.WhentheseIoTdevicesstartedcollectingdata,thecloud
wastheonlyplacetoanalyze,filter,pre-process,andaggregateit.However,whenitcomestoIoT,thecloud
hasrestrictionsregardinglatencyandamorecentralizedmethodofdistributingprograms.Anewformof
computingcalledFogcomputinghasbeenproposedtoaddresstheshortcomingsofcurrentcloudcomputing.
InanIoTcontext,sensorsregularlycommunicatesignalinformation,andedgedevicesprocessthedataob-
tainedfromthesesensorsusingFogcomputing.Thesensors’internalorexternalproblems,securitybreaches,
ortheintegrationofheterogeneousequipmentcontributetotheimbalanceddata,i.e.,comparativelyspeak-
ing,oneclasshasmoreinstancesthantheother.Asaresultofthisdata,thepatternextractionisimbalanced.
Recentattemptshaveconcentratedheavilyonbinary-classimbalancedconcernswithexactlytwoclasses.
However,theclassificationofmulti-classimbalanceddataisanissuethatneedstobefixedinFogcomputing,
evenifitiswidespreadinotherfields,includingtextcategorization,humanactivitydetection,andmedical
diagnosis.Thestudyintendstodealwiththisproblem.Itpresentsasystematic,thorough,andin-depthcom-
parativeanalysisofseveralbinary-classandmulti-classimbalanceddatahandlingstrategiesforbatchand
streamingdatainIoTnetworksandFogcomputing.Therearefivemajorobjectivesinthisstudy.First,re-
viewingtheFogcomputingconcept.Second,outliningtheoptimizationmetricusedinFogcomputing.Third,
focusingonbinaryandmulti-classbatchdatahandlingforIoTnetworksandFogcomputing.Fourth,review-
ingandcomparingthecurrentimbalanceddatahandlingmethodologiesformulti-classdatastreams.Fifth,
explaininghowtocopewiththeconceptdrift,includingnovelandrecurringclasses,targetedoptimization
measures,andevaluationtools.Finally,thebestperformancemetricsandtoolsforconceptdrift,binary-class
(batchandstream)data,andmulti-class(batchandstream)dataarehighlighted.
ThisworkispartlysupportedbyEUHORIZON-TMA-MSCA-SEprojectTRACE-V2XundergrantNo.101131204.
Authors’ContactInformation:FarhanaSharief,DepartmentofSoftwareEngineering,UniversityofSargodha,Sargodha,
Punjab, Pakistan; e-mail: farhana.shareef@uos.edu.pk; Humaira Ijaz, Computer Science & IT, University of Sargodha,
Sargodha, Pakistan; e-mail: humaira.bilalrasul@uos.edu.pk; Mohammad Shojafar, 5G & 6G Institute for Communica-
tion Systems, University of Surrey, Guildford, Surrey, United Kingdom of Great Britain and Northern Ireland; e-mail:
m.shojafar@surrey.ac.uk;MuhammadAsifNaeem,DepartmentofComputerScience,NationalUniversityofComputer
andEmergingSciences,Islamabad,Pakistan;e-mail:asif.naeem@nu.edu.pk.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbe
honored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,
requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ACM0360-0300/2024/10-ART16
https://doi.org/10.1145/3689627
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:2 F.Shariefetal.
CCSConcepts:•Computingmethodologies→Supervisedlearningbyclassification;Artificialintel-
ligence;•Generalandreference→Surveysandoverviews;•Informationsystems→Datastreams;
AdditionalKeyWordsandPhrases:Cloudcomputing,fogcomputing,InternetofThings(IoT),multi-class
imbalanceddatastream,conceptdrift
ACMReferenceFormat:
FarhanaSharief,HumairaIjaz,MohammadShojafar,andMuhammadAsifNaeem.2024.Multi-ClassImbal-
ancedDataHandlingwithConceptDriftinFogComputing:ATaxonomy,Review,andFutureDirections.
ACMComput.Surv.57,1,Article16(October2024),48pages.https://doi.org/10.1145/3689627
1 Introduction
TheInternetofThings(IoT)isavastandheterogeneouslandscapebeingemergedasthenext
computingparadigmthatwillundoubtedlyrevolutionizehowweinteractandconductbusinessby
connectingbillionsofdevices,objects,andlivingthingstotheInternet.Thisnetworkhaswidely
dispersed, intelligent, tiny, self-configurable devices with limited processing and storage capaci-
ties,whichcancauseproblemswithperformance,security,privacy,andreliability[1].Itbenefits
various application sectors, including smart buildings, healthcare, manufacturing, and many
more.TheseinterconnectedIoTcomponentsgenerateawiderangeandmassiveamountsofdata.
TheIoTcomponentsgenerateover2.5quintillionbytesofdatadaily.[2].Estimatessuggest45.41
billionconnectedIoTcomponentswillbeconnectedby2023,[3],risingto1.2trillionby2030[4].
1.1 IoTDataTypes
A wide variety of applications and environment that IoT components operate in is reflected in
diversespectrumofdatatypesthatthesedevicescreate.Itiscrucialtounderstandthesedatatypes
forfullyutilizingIoTtechnology.Therefore,theseIoTdevicesgeneratedataaboutthefollowing
features[5]:
(1) StatusData:IoTstatusdataisthemostprevalentandfundamentaltypeofdata.Itserves
asastartingpointformorecomplexinvestigations,suchasdeterminingwhetheracertain
unit component is functioning. Almost anything will generate data like this. Therefore, it
servesasabaseline.
(2) LocationData:Itistheinformationaboutadevice’sorotherasset’suniquegeographical
whereabouts that is gathered and tracked by GPS satellites in a specific network. It is an
extensionofGPSbecause,inmanycongestedareas,GPSdoesnotwork.
(3) AutomationData:Itisunavoidableandisusedtochangethecurrentstateofthesystem.
Manufacturersofsmartlights,forexample,usesensordatatodirectthestoremanagersin
theopeningofcheckoutlines.
(4) ActionableData:Itissimilartostatusinformationwithafollow-upstrategy.Adashboard
alertindicatingserverdowntime,accompaniedbyarecommendedrebootproceduretore-
storeservice.
(5) FeedbackLoopwithIoTData:Itisestablishingafeedbackloopfromtheclienttothede-
velopertoassessreal-worldbehaviorwhilepreservingappropriatelevelsofprivacy,security,
andanonymity.
1.2 Analytics-drivenIntelligenceintheInternetofThings
ThisdiverseandenormousIoTdatasetisanalyzedusingIoTanalytics,whichoffersinsightfuldata.
IoT analytics adds value to this data by fetching, combining, and evaluating it. This procedure
encouragesinnovationacrossarangeofindustries,enhancesfunctionalperformance,andallows
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:3
Fig.1. Analyticstaxonomy.
for better informed decision-making. Among the many tasks carried out by IoT analytics are
the anticipatory maintenance of equipment, the efficient use of resources, enhanced customer
experiences, and the creation of new products. Moreover, real-time responses to dynamic
conditions are provided via IoT data analytics. To put it simply, IoT data analytics is essential
torealizingthefullpotentialofIoTtechnologyandtransformingdataintoastrategicassetthat
can advance both enterprises and society. Furthermore, individuals and businesses may benefit
from data analytics. The taxonomy of data analytics is shown in Figure 1 with the following
categories:
(1) Descriptiveanalysisisusedtoexaminehistoricaldata.It,forexample,employsdata-mining
techniquestofindpatternsandestablishconnections.
(2) Diagnostic analysis is used to identify the causes of events as well as potential issues and
failures,forexample.
(3) Predictiveanalysisemployspreviousdatatoforecastdatapatterns.Intheproductionpro-
cess,forexample,consumerbehaviorforecastsarecrucial.
(4) Prescriptiveanalysistakesalltheothertypes’resultsandappliesthemtomakingthebest
judgmentspossibletoobtainapredictableoutcome.
1.3 Cloud-basedProcessingandAnalytics
Inthebeginning,theIoTanalyticsperformedbyacentralizedcloud-basedarchitectureisknown
as CIoT [6]. In this paradigm, the IoT can benefit from the cloud’s resources and limitless capa-
bilities. This architecture has only two tiers. The first tier is the end-user devices that are using
cloud services. The second tier is the cloud. A business model called cloud computing provides
essentialnetworkconnectivityinseveralforms,includingstorage,services,andnetworks.Italso
has virtually infinite processing and storage capacity. Although the CIoT has been a successful
platformformanyIoTapplications,theunlimitedincreaseinIoTapplicationsgeneratesanendless
stormofdatathatCloudserverscannotprocessalone.Furthermore,theseIoTapplicationsnow
alsoneedlocationawareness,lowlatency,geo-distribution,andmobility,[7]duetotechnological
advancements and a new wave of internet deployment adding more to data generated by these
IoTapplications.Transferringthissheeramountofdatatodistantcloudserversconsumesheavy
bandwidth but causes delays that are not tolerable by many real-time applications. There are
restrictionsonhowmuchdatacanbetransferredtothecloud[8].
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:4 F.Shariefetal.
Theemergingtechnologiestohandlethesechallengesinthecloudincludevolunteercomputing,
software-definedcomputing,mobilecomputing,andFogandedgecomputing.Accordingtoasur-
vey[9],FogcomputingisthemostcommonparadigmforanalyzingIoTdataandgivingnetwork
devicescloudfunctionalities.
1.4 FogComputingParadigm
A distributed computing technique known as Fog computing emerges as a solution to the
bandwidthandlatencyissuesthatcloud-centricIoTsystemsbringabout.Thistechniqueusesthe
cloudasalinktoconnecttodevicesattheedge.Retainingcontentclosertotheedgeimprovesthe
capabilitiesofcloud-basedservices.Byofferingdecentralizedcomputingservices,Fogcomputing
enables local data processing, lowers latency and bandwidth consumption, which improves pro-
ductivityandservicequality.Thisapproachworkswellfortime-sensitiveapplicationsthatrequire
immediateanalysisandactions.Itisthereforeamoreeffectiveandresponsivecomputingmodel
thatreducesdependencyoncentralizeddatacenters.Smarthealthmanagement,smartbuildings,
smartgrids,andsmartmanufacturingareafewofthemostpopularusesofFogcomputing.
1.5 FogDataLifeCycle
CombiningIoTdataanalyticswithFogcomputingallowsefficientprocessingandanalysisofthe
largeIoTdataset.Fogcomputingleveragesdataanalysistoenablereal-timeinsightsanddecision-
making withoutthe latency associatedwith cloud computing, which entails processingmassive
amountsofdatacreatedbyIoTdevicesatorneartheedgeofthenetwork.TheFogdataanalysis
lifecycleisthesequenceofeventsthatdatagoesthroughintheFogcomputingarchitecture,in-
cludingthedata’sinitialgenerationbyIoTdevices,processingandanalysisattheedge,andfinal
usefordecision-makingoradditionalaggregationforcloudstorageorin-depthanalysis.
Fogcomputing,improvingdecision-making. TheFogdataanalysiscomprisesthreelayers.There
arethreelayersofFogdataanalysis.Inthefirstlayer,thedataisgatheredfromIoTcomponents
and sensors before being sent to the Fog layer. This layer contains actuators for command
execution coming from the above layer. The subsequent Fog layer comes after that. It consists
oftwosub-layers.Thefirstsub-layer,theFog-deviceFogsub-layer,handlesthephysicaldevices’
routines,protocolinterpretation,signalde-noising,authentication,anddatastorage.Additionally,
thislayerconductslocaldecision-makingandlightanalysis.TheFog-cloudsub-layeristheother
Fogsub-layer.Thissub-layerhandlescompressionanddecompressionaswellasencryptionand
decryption. The third layer is the cloud layer, which transfers aggregated data. It stores data
permanentlyandmakesglobaldecisions.Afterprocessingandanalyzingtheincomingquery,it
generates feedback and sends it to the Fog layer. A detailed Fog Data Analysis (FDA) model
proposed by Reference [10] addresses various challenges such as heterogeneous Fog network,
qualityofservice,programmingmodelandinterface,resourcemanagement,security,andprivacy.
Figure2showsthebasicstructureofFDA.
However,theoccurrenceofimbalanceddataisamajorchallenge,especiallyinsettingswhere
timely and accurate insights from data are crucial for decision-making in Fog data analytics,
particularly in IoT and Fog computing environments. When there is an uneven distribution of
data among various classes, some types of data predominate over others, which results in this
condition. Analytics models may be negatively impacted by thisimbalance, which can lead to a
biasinfavorofthemorecommonlyrepresentedclassesand,asaresult,reducetheirabilitytopre-
dictimportantbutrareevents.Suchbiasedanalyticshaveafargreaternegativeimpactthanjust
inaccurate analysis: They fundamentally compromise the quality of decision-making processes.
Similar to how unbalanced data prevents systems from detecting threats in security systems,
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:5
Fig.2. Fogdatalifecycle.
unbalanced data prevents scenarios needing predictive maintenance for system integrity from
detectingearlysignsofsystemmalfunction.Furthermore,excessivecautionoroverstretchingin
areasthatdonotrequireimmediateattentioncanresultfromthisimbalance,whichcanleadto
inefficientresourceallocation.Moreover,thechallengeofdataimbalanceinfoganalyticsextends
to the optimization of the fog computing infrastructure itself. It can hinder the system’s ability
to effectively manage load distribution, energy consumption, and bandwidth usage, affecting
the overall performance and sustainability of the fog computing environment. Therefore, it is
crucialtoaddressdataimbalancetoenhancethereliabilityofFog analytics.Syntheticdatagen-
eration,dataaugmentation,andafewadvancedmachinelearningtechniqueshandleimbalanced
data. Resolving this imbalance is essential to guaranteeing that data analytics in fog environ-
ments can produce trustworthy, actionable insights that facilitate prompt and well-informed
decision-making.
1.6 ReasonsofImbalancedDatainIoT,FogComputing,andWSN
Technical, environmental, and operational issues could cause data imbalance. We elaborate on
thesecausesbelow,offeringathoroughrundownoftheelementscausingdataimbalancesinFog
computing:
—HeterogeneityofDevices
EachheterogeneousIoTcomponentgeneratesdataatvaryingratesandformats,leadingto
imbalanceddatadistribution.Inasmartcity,forinstance,trafficcamerasmaycontinuously
collectdata,butenvironmentalsensorsmayonlycollectwithincertainconditionsleading
toimbalanceddata.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:6 F.Shariefetal.
—RarenessofEvent
Detecting rare but critical events leads to datasets where the number of such occurrences
is much greater than that of typical events. For instance, because irregular heart rates are
uncommonrelativetonormalheartrates,healthmonitoringsystemsmayhavetroublede-
tectingthem.
—ConstantlyChangingNetworkTopology
Frequent connection and disconnection of devices in IoT environments cause network
instability. The energy constraints arising from limited battery life of devices, mobility of
wearable devices introducing variability in data capture and network connectivity, and
other environmental factors like temperature fluctuations, cause the network topology to
changeconstantly.Thisdynamicnatureisespeciallyprevalentinvariousapplicationssuch
as healthcare monitoring, smart cities, and industrial IoT, where it leads to variable data
ratesandpatterns,causingimbalanceddatasetsthatchallengedataprocessingandmachine
learningmodels.
—TemporalandSpatialDifferences
ThegeographicallydistributedIoTcomponentsandtemporalfactorsaffectdatacollection,
leadingtoimbalances.Forinstance,variationsinthetimeofdayorseason.
—LimitedResources
The processing of selected data due to limited computational resources causes the data to
beimbalanced.
—SpecificTransmissionandFiltration
To preserve bandwidth and storage, the Fog nodes broadcast and filter data selectively,
resultinginanunbalanceddataset.Environmentalmonitoringdevices,forinstance,might
onlysenddatawhenvaluesdeviatefromexpectedranges.
—DelayinDataProcessing
Temporalimbalancesindataavailabilitycausedbyvariationsinprocessinglatenciesmight
impact real-time analytics. For instance, outdated data utilized in decision-making may
arisefromadelayindataprocessingcausedbycomputationaloverload.
—Lossofdata
Data imbalance can result from gaps in datasets caused by data loss during transmission.
Forinstance,thelossofvitalpatientdatamayresultinanunderrepresentationofspecific
medicalconditions.
—Userinteractions
DataimbalanceisintroducedbythewayconsumersinteractwithIoTcomponentschanging
overtime.Inparticular,IoTapplicationsfocusedoncustomers.
—EnvironmentalFactors
External conditions have the potential to impact the data generated by Internet of Things
components,resultingindataimbalancescausedbysituationalorseasonalcauses.
—AdvancementinCapabilitiesofIoTComponents
With the advancement of IoT technology, newer IoT devices generate more frequent data
than older devices, leading to data imbalance. For example, the machinery upgraded with
moresensorsgeneratemoredata.
—DataQuality
Imbalanced data is the result of changes in data quality, such as errors, missing numbers,
andnoise.Forinstance,duringharshweather,sensorsinweathermonitoringsystemsthat
relyonoutdoorsensorsmaymalfunctionandprovidedistorteddata,whichwouldreduce
thereliabilityofthedatasetasawhole.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:7
—LimitationsonEnergy
Energylimitationsmaycauseselectivedatatransmission,whichcouldprovidedatathatis
imbalanced. Trackers may lower data transmission frequency in remote wildlife tracking
applicationstosaveenergy,whichcouldresultingapsinthetrackingdata.
—GrowingData
Theavailabilityofhistoricalandpresentdatamaybecomeimbalancedovertimeasnewer
datareplacesorbecomeslessrelevantforpreviousdata.Forinstance,datalossmayoccur
whenoutdatedclientinformationisarchivedtomakewayformorerecentinformation.
1.7 MotivationandGoaloftheArticle
The inspiration for the article and its objective are as follows: A few research studies have
beenconductedonhandlingimbalanceddatainFogcomputing,butitisstillinitsinfancy.The
previous studies provided a basis for the Fog computing architecture and a brief overview of
differenttechniquestohandlebinary-classandmulti-classimbalanceddataforbatchandstream
dataprocessingproblems.However,asFogcomputingdevicesareresource-constrainedtohandle
imbalanced data, a lightweight technique is required for multi-class imbalanced data stream
problems.Thisanalysishasledustoanopenissuefordrivingmulti-classimbalanceddatastreams
intheFog.AsnoisyandincompleteIoTstreamscancreateuncertainty,thereisaneedtodefine
amechanismforresource-constraineddevicesattheedgetohandleimbalancedstreamdatathat
continuouslyupdatesinstancesandpredictsnovelandrecurringclassesthatappearafteralong
time. So, it is necessary to thoroughly assess the literature on these imbalanced data handling
techniquesforbatchandstreamdata.ItisalsoessentialtodescribethearchitectureofFogcom-
putinganditsunresolvedchallenges,particularlyinhandlingmulti-classimbalancedstreamdata
in Fog computing. We give a complete evaluation, covering all the paths to connect these holes.
ThefoundationofFogcomputing,numerousimbalanceddatahandlingtechniques,andafullas-
sessmentoftheapproachesuseduptonowforhandlingimbalanceddatainFogcomputingareall
presentedinthiscompletesurvey,whichfocusesonmulti-classdynamicimbalancedstreamdata.
1.8 Contributions
Thefollowingarethemajorcontributionsofthepresentstudy:
—The study classifies and thoroughly examines the existing imbalanced data handling tech-
niques, concentrating on imbalanced multi-class stream data handling techniques based
on sampling, algorithmic, cost-sensitive, and ensemble approaches and examining their
strengthsandweaknesses.
—Itgivesathoroughexplanationofthefoundationofimbalanceddataanditsvariousforms,
includingbatch(binary-classandmulti-class)andstream(binary-classandmulti-class)im-
balanced data. Moreover, it delves into a comprehensive evaluation of the Fog computing
paradigmforimbalanceddata.
—Thisresearchdescribesthevariousperformancemetricsusedintheliterature.Themetrics
used for the evaluation of existing imbalanced data handling techniques are categorized
intobothbinary-class(Accuracy,Kappa,MCC,Precision,Recall/Sensitivity,Specificity,F1-
measure,G-measure,G-mean,andAUC)andmulti-class(AveAcc,AveragePrecision,Mean
Accuracy,MeanF-measure,MAUC,KappaandProbabilisticAUC)metrics.Forbinary-class
data,accuracywasthoughttobethemostpopularmetric,whereasMAUCwasthoughtto
bepopularformulti-classdata.
—In a non-stationary environment, concept drift occurs when the data and target concept
evolvesovertime.Whenitcoexistswithclassimbalanced,itaffectspredictiveperformance,
andonlyafewapproachesaddressthisproblem.Inthissurvey,conceptdriftidentification
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:8 F.Shariefetal.
Fig.3. Organizationofthearticle.
inimbalancedstreamdataindifferentnetworksisthoroughlyexaminedforthefirsttime,
focusingontheFognetwork.
—Thestudyalsoshowsaresearchgapintheareaofmulti-classimbalanceddatastreamswith
conceptdriftsinFogcomputing,whichhastobefilled.
1.9 ArticleStructure
Thearticlestructure,asdescribed,outlinestheorganizationoftheresearchcontent,startingwith
the discussion of solutions for handling imbalanced data are detailed in Section 2, specifically
in Section 2.1 and Section 2.2 gives the performance metrics to evaluate the effectiveness of
various solutions. Section 3 elaborates on a comparison of existing surveys. The applications
of imbalanced data handling techniques is presented in Section 4, which is further divided
into subsections. WSN and IoT network methodologies for dealing with binary and multi-class
imbalanced batch and stream data and concept drift handling are covered in Section 4.1 and
Fog computing in Section 4.2. Section 5 presents the analytical discussion about the surveyed
techniques,andthelessonslearnedfromthissurveyreportarepresentedinSection6.InSection7,
wehighlightthechallengesandrefertofuturevisionaryresearch.Section8concludesthesurvey.
Figure3displaysthestructureofthearticle.
1.10 Methodology
ThiscomprehensivesurveyreportimplementsPRISMAsystemtoensuremulti-classimbalanced
data and concept drift while maintaining transparency, consistency, and repeatability in the
screening stage of the review procedure. The following sequential steps are used to describe
themethodology.IntegratingthePRISMAstructurewiththearticle’sorganizationenhancesthe
systematic and rigorous approach to reviewing and presenting the findings on imbalanced data
handlinginFogcomputing.
—Identification
Acomprehensivesearchstudywasdesignedtofindthemostimportantpapersonthepredic-
tionofmulticlassimbalanceddatawithconceptdrift.Academicdatabases,GoogleScholar,
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:9
IEEE Xplore, ACM Digital Library, ScienceDirect were searched using key terms such as
“IoT,”“cloud,”“imbalanceddata,”“conceptdrift,”“Fogcomputing.”Thisyielded150records
fromGoogleScholar,whichwereaddedtoreferencesoftwareafterduplicateremoval.
—Screening
Following the removal of duplicates, 130 distinct files were left for more review. Then,
for finding the relevance of each document, the title and abstract of each document were
studiedandirrelevantdocumentswereexcludedinthisphase.Amorepreciselistofstudies
thatareeligibleisproducedbythescreeningprocess.
—EligibilityandExclusion
Afterscreening,130paperswerereviewed.Uponfull-textreview,27wereexcluded,leaving
103articlesthatmettherequirements.
—Inclusion
Finally, 103 studies met the predefined parameters and were included in the systematic
reviewonMulti-classimbalanceddatahandlinginFogcomputingwithconceptdrift.
2 ImbalancedDataSolutionsandPerformanceMetrics
Thissectionpresentssolutionsforaddressingimbalanceddataanddiscussesrelevantperformance
metricstoevaluatemodeleffectiveness.
2.1 GeneralApproachestoHandleImbalancedData
This section focuses on exploring fundamental strategies for addressing imbalanced datasets. It
delvesintobothdata-levelandalgorithm-levelsolutionsthatplayacrucialroleinmitigatingthe
challengesposedbyimbalanceddatainvariousdomains.
—Data-levelSolutions:Totacklethechallengeofimbalanceddata,asamplingprocedurecan
beemployed.Itisapreprocessingtechnique.Byrepeatingtheobservations,minorityclass
instancesaremultipliedinoversampling.Incontrast,majorityclassinstancessignificantly
decrease in undersampling to maintain an equal number of occurrences in two different
classes.Inhybridsampling,bothsamplingtechniquesarecombined.Severalideasemerged
underthesecategories,withnon-heuristicpreprocessingtechniquessuchasrandomunder-
samplingandrandomoversamplingbeingthesimplest.
—Algorithm-levelSolutions:Itisanalternativesolutionfordatapreprocessingtodealwith
imbalanceddata.Itisaclassifiertrainingprocedureinsteadofmodifyingthetrainingset.The
imbalanceinthetrainingdatasamplescanbecorrectedthroughtheweighteddistancefunc-
tionwithoutaffectingtheclassdistribution[11].Thealgorithmsthatareusedforhandling
theimbalanceddataareSVMbias,NaïveBayes,andNeuralNetwork.
—Ensemble-levelSolutions:Ensemblelearningandensembleclassificationrelyonseveral
classifiers’votestoevaluatetheactualclasslabelofsamples.Thisprocedurebuildsdifferent
classifiers, each focusing on a unique set of characteristics or examples. The diversity of
the training sets of classifiers causes the system to be varied. This heterogeneity between
classifiersdevelopsanensemble-basedsystemandhelpstoincreaseitsrobustnessagainst
noise.Becausenoneoftheclassifiersusestheentiredataset,therefore,itperformsbetteron
datathathasnotbeenpreviouslyseen.
—Cost-sensitive-level Solutions: This approach generates classification algorithms for
each class with a different misclassification cost. It necessitates understanding the cost of
misclassification, which varies with every dataset and is sometimes not able to be known
orchallengingtocompute.Furthermore,thealgorithmsmustcomputethemisclassification
cost for each class or instance while optimizing. There are two primary sub-categories
of cost-sensitive learning algorithms: The first sub-category directly incorporates the
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:10 F.Shariefetal.
Table1. GeneralApproachesforImbalancedDataHandling
Category Strength Weakness
Resampling
—Balanceclassdistributionthrough —Overfitting[14]
resampling —Loseimportantinformation
—Applicabilitytoanylearning —Highlearningtime[15]
algorithm[12]
—Modifyoriginaltrainingdataset
—Externalapproach[13]
—Independentfromtheclassifier
Algorithmic
—Providegoodprediction —Ittakesintoaccounttheerrorrate
accuracies[16] ratherthandatadistribution
—Modifyexistingclassification —Fixedtothepre-determinedlearning
method algorithm
—Internalapproach —Cost-sensitivetowardsminorityclass
Ensemble-level
—Overcomeimbalancedbyforming —Themoreunder-fit/over-fitmodels
sub-samples amongthetotalensemblemodels,the
—Overcomecomputationalload moreadverselyitaffectsthe
—Preventperformancedegradation well-learnedclassifier
Cost-sensitive
—Focusondifferent —Sensitivetonoiseandoutliers
misclassificationcostsof
classifiersfordifferentclasses
cost of misclassification into the training procedure. The second sub-category is called
meta-learning and it modifies the outputs of the classifier or the training data but not the
training process. Meta-learning-based solutions can be used in two separate stages of the
classificationprocess,forexample,preprocessingandpostprocessing.
Table 1 summarizes the strength and the weaknesses of various imbalance data handling
techniques.
Numerousreal-worldapplicationsaremoreconcernedaboutthecategorizationofimbalanced
datasets. Binary-classification problems, where one class greatly outnumbers the second, have
receivedthemajorityofattentionintheliteratureonimbalancedclassification.Inadditiontothat,
skewedclassdistributionscanalsocausemulti-classdifficultiesthatinvolvemoreclasses,andone
of them contains more instances than all other classes. We have grouped general approaches to
addressingimbalanceddatainthissection.Thesetechniquesarefurtherdividedintostreamand
batchdata,havingbothbinaryandmulti-classes,asmentionedbelow:
2.1.1 Batch Data Handling for Binary Classes. As far as binary-class data processing is con-
cerned, both batch data processing and real-time processing are included. Batch processing re-
quires processing a significant volume of previously stored data, whereas real-time processing
entailsprocessingstreamdata.Streamprocessingconsistsofaninfinitenumberoftinybatches.
Inthecaseofbatchprocessing,thedatafacesafewproblems.Oneofthemisthedata-imbalance
problem.Variousapproacheshavebeenusedtoovercomethisprobleminbinary-classdatasets.A
fewofthemaregivenbelow:
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:11
Table2. ComparisonofData-levelSolutionsforImbalancedDataHandlingTechniques
Technique R-Type Acc G-meanF1-m A R P Cov MI Co-CMSDBal DS Ref
Heuristicoversamplingbased OS × × × × × × × × UCI,KEEL,MEDELON [17]
onK-meanandSMOTE
KMFOS OS × × × × × × × × × × ProjectfromNASA,softlab [18]
MTDF OS × × × × × × “LINKSOFCOMPARING -
OVERSAMPLING”
Empiricalcomparison OS × × × × × × × × Keel [19]
Comparisonofoversampling OS × × × × × × × × 7-yearfreshmenstudents [20]
andundersampling data
ECO-ensembleframework OS × × × × × × × × × × UCI [21]
SMOTEvariants-A OS × × × × × × × × × × × Libras [22]
comparison
=metricsfocusedintechnique;×=metricsignored;R–Type=ResamplingType;OS=Oversampling;
US=Undersampling;Acc=Accuracy;F1-m=F1-measure;P=Precision;Cov=Coverage;MI=MutualInformation;
Co-C=CorrelationCoefficient;MSD=Meanstandarddeviation;Bal=Balance;DS=Datasets;Ref=Reference.
—Resampling
Class-imbalanced datasets are prevalent in different domains, including health, security,
banking, and others. A typical supervised learning algorithm tends to be biased towards
themajorityclasswhendealingwithimbalanceddatasets.Thesolutionproposedtosolve
theclass-imbalanceproblemisdataresampling.Thedata-levelsolutionformallyknownas
resamplingprovidesameanstomodifydatadistributionandyieldsarevisedsetwithbal-
anceddatadistribution.
(1) Oversampling
Even though the accuracy is good, the correct specification rate for the minority class
suffers in an imbalanced dataset situation. To remedy the problem, the oversampling
approach was applied without regard to the loss of accuracy. Furthermore, an arbitrary
oversampling strategy may result in bias. Oversampling tacticswere proposedby many
researchersinvariousformats,someofwhicharelistedbelow:
—Reference[17]coupledthek-meansclusteringmethodwithSMOTEtoproducehigher
classification results than training with unmodified, imbalanced data. This technique
solvedboththebetween-classandwithin-classimbalancesbyinflatingscarceminority
regions.
—Reference [18] provided a cluster-based oversampling with noise filtering (KMFOS)
approach for handling the problem of class imbalanced Software Defect Prediction
(SDP). KMFOS first divided faulty instances into K clusters and then interpolated
betweeninstancesofeachofthetwoclusterstogeneratenewdefectiveexamples.The
researcherthenimprovedthiscluster-basedoversamplingwiththeClosestListNoise
Identification (CLNI) to clear the noise occurrences. In Table 2, the tick marks (
) indicate theintendedcriteria, whilethecrosses(×) showthemetrics ignored by the
researchers.
—Undersampling
Differentresearcherspresentedundersamplingstrategiesinvariousforms,someofwhich
aregivenbelow:
—Many academics have suggested informative undersampling procedures to prevent the
loss of useful information. Unlike K-specific clusters, the cluster-based undersampling
strategy based on distance-based instance concepts proved beneficial for dataspace that
washighlyclusterable.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:12 F.Shariefetal.
Table3. ApproachesforUndersamplingandHybridSampling
Technique Dataset Tool Parameters Ref
Boosting-driven Breastcancer,Diabetes,German MATLAB Recall,Precision, [15]
cluster-basedundersampling creditcard,Ionosphere,Blood G-mean,F1-measure,
(undersampling+clustering) transfusion,Spambase Specificity
Clustering-based 44small-scaledatasetsusedby − Accuracy [14]
undersamplingin Glaretal.aswellastwo
class-imbalanceddata large-scaledatasets,namely,the
(undersampling+clustering) breastcancerandprotein
homologyprediction
Neighborhood-based 66datasetsfromUCIandKEEL − Sensitivity,G-mean, [12]
undersamplingframework Precision,F1-score
TPHM Uremiadataset − Accuracy [24]
SUNDO Asyntheticdatasetof134samples − Accuracy [13]
andreal-worlddatasetsfromthe
metalindustry
Undersampling+ensemble Datasetfromsteelmanufacturing Python G-mean,F1-score, [25]
plant Recall,Precision
—Bycombiningtheundersamplingofmajorityoccurrenceswithclassifierlearning,anadap-
tiveundersamplingstrategywassuggestedinReference[15].
—Undersamplingwasdoneiterativelyinsideanensemblelearningframeworkthatisused
tocontrolthetrainingflowforfutureiterations.TheAdaBoostensemblemodelwasused
fortheclassifiertrainingalongwiththedecisiontreeC4.5astheweaklearner[23].
—Reference[14]introducedtwoundersamplingstrategies.Thefirststrategyusestheclus-
tercenterstorepresentthemajorityclass,whereasthesecondstrategyusesthenearest
neighborsoftheclustercenters.Itcanreducetheriskofremovingusefuldatafromthe
majorityclass.
—Neighborhood-based undersampling framework [12] identified and eliminated majority
classinstancesfromtheoverlappingregion.First,itmaximizesthevisibilityofminority
classinstances.Second,itpreventsexcessiveeliminationsandminimizesinformationloss.
—Reference[24]proposedahybridimbalanced-classdecision-treeroughsetmodeltointe-
grate the knowledge of experts. The accuracy of the hybrid sampling and oversampling
methodswasveryclose.
—InReference[13],anewresamplingmethodwaspresented,combininganoversampling
and an undersampling technique. It outperformed the widely adopted combination of
SMOTEoversamplingandrandomundersampling.
—The researcher suggested an ensemble learning-based undersampling technique using
Extreme Gradient Boosting (XGBoost) and SVM [25]. For producing the training
set for this ensemble method, the patterns were generated randomly after sampling on
the majority set. This methodology helps in improving the classification tasks. Table 3
summarizestheinformation.
—Ensemble
Multipleclassifiersystems,alsoknownasensemble-basedclassifiers,havebeenshowntoim-
proveasingleclassifier’sperformancebyintegratingvariousbaseclassifiersthatcollectively
performbetterthaneachoneusedalone.Classifierensembleshavebecomemorecommon
as a solution to the class-imbalance problem. Probably, 218 publications out of the 527 re-
viewedpapersinasurveyreport[26]presentednewensemblemodelstoaddressreal-world
problems.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:13
Table4. Ensemble-levelApproachesforDataHandling
Technique Dataset Tool Parameters Ref
BalancedBoost UNIBSdataset −C4.5asbaseclassifier Precision,Recall, [27]
F-measure,Accuracy,
RandomBalance HDDT,KEEL Weka(J48asbaseclassifier) AUC,f-measure [28]
GradientBoosting Ivshina,Wang,Sotiriou,EM −CARTasbase G-mean,AUC [29]
EPRENNID 35datasetsfromUCIandKEEL −1NN AUC,G-mean [30]
SwitchingNED 33datasetsfromUCIandKEEL DecisionTreeC4.5 AverageAUC [31]
In “BalancedBoost,” proposed by Reference [27], RUSBoost was modified and resampling
tookplaceusingAdaBoost.M2algorithmweight.Inanothertechnique,givenbyReference
[28], an amalgam of RUSBoost and SMOTEBoost was called “RandomBalance Boosting.”
The Adaboost.M2 method was paired with random balanced sampling to produce an
ensemble capable of handling imbalanced classes. In Reference [29], the optimization of
an arbitrary differentiable loss function was allowed by the gradient-boosted trees. An
ensemble approach proposed by Reference [30] for classifiers specifically focused on data
preprocessing was called EPRENNID (Evolutionary Prototype Reduction based En-
semble for Nearest Neighbor Classification of Imbalanced Data). The hybridization
ofprototypeselectionandprototypegenerationforensemblebuildingresultsinthedistinct
reference sets of a K-NN. Both systems were created using evolutionary algorithms, and
both methods adjust for imbalanced class, primarily done by taking relevant performance
measurementsintothefitnessfunction.AccordingtoReference[31],theundersampling
SwitchingNearestEnemyDistancewasknownasUSwitchingNED.Itrandomlyswaps
the labels of instances of the majority class to achieve diversity. Table 4 outlines a few
ensemble-levelsolutionapproachesforimbalanceddatahandling.
—Cost-sensitive
As opposed to the resampling strategy, cost-sensitive learning is more computationally
effective,makingitabetterchoiceforBigdatastreams.Itisfarlesscommonthanresam-
plingmethods,asevidencedbythesurveyreportthatfoundjust39oftheexaminedpapers
employedit[26].
Reference [32] improved classification accuracy along with the consideration of variable
misclassifcationcost.TheapproachpresentedbyReference[33]automaticallylearnedthe
representationsoffeaturesforbothunderrepresentative(minority)andoverrepresentative
(majority) classes. Reference [34] directly incorporated a cost-sensitive function into the
classification paradigm and employed differentiable evolution for the optimization of
the cost matrix. The research proposed by Reference [35] used an adaptive differential
evolutiontotackleoptimizingthemisclassificationcost.Itwasaneffectivesolutiontotackle
unknown misclassification costs. Reference [36] has combined the cost-sensitive method
withathresholdstrategytoincreasetheaccuracyoftheminorityclass,andforthispurpose,
it used a cost-sensitive factor for assigning larger weights to the underrepresentative
(minority) classes and punishing the overrepresentative (majority) classes. A few of the
worksonthisstrategyaregiveninTable5.
—Algorithmic
Traditionally, classification algorithms have been unable to deal with the problems of
imbalanced data, since they are biased against the dominant class. As a result, algorithms
havebecomeunabletoclassifythemostdemandingminorityclass.
TheproposedmodelofReference[37]entaileddevelopinganapproachtogeneticprogram-
mingthatemployedhierarchicallinguisticvariables.ItsuggestedcombiningSMOTEwith
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:14 F.Shariefetal.
Table5. Cost-sensitive-levelApproachesforDataHandling
| Technique | Dataset | Tool | Parameters | Ref |
| --------- | ------- | ---- | ---------- | --- |
AdaC-TANBN Heart,ILPD,Dermatology, R3.5mathematical Accc,Sensitivity, [32]
|          | CCRF             | developmentenvironment | Specificity,AUC,ROC |      |
| -------- | ---------------- | ---------------------- | ------------------- | ---- |
| CoSenCNN | MINST,CIFAR-100, | −                      | F-measure,G-mean    | [33] |
Caltech-101,MIT-67,DIL,MLC
−
| CSDBN-DE | 42datasetsfromKEEL |        | Accuracy,ErrorRate | [34] |
| -------- | ------------------ | ------ | ------------------ | ---- |
| ECS-DBN  | 58datasetsfromKEEL | Python | Acc,G-mean,AUC,    | [35] |
Precision,F1-score
| CSHCIC | proteindataset(DD,F194),SUN | −   | ACC,F1Hierarchical | [36] |
| ------ | --------------------------- | --- | ------------------ | ---- |
measure
Table6. Algorithmic-levelApproachesforDataHandling
| Technique | Dataset |     | Tools Parameters | Ref |
| --------- | ------- | --- | ---------------- | --- |
− −
| HFRBCS | 44datasetsfromKEEL |     |     | [37] |
| ------ | ------------------ | --- | --- | ---- |
−
Compactevolutionary BI,BC,WSI,FESI,DT,AL,SL,ARB,FD, G-mean [16]
| IVFRBCS | Len,LA |     |     |     |
| ------- | ------ | --- | --- | --- |
FuzzyKNN IonosphereandNew-ThyroidfromUCI, − Precision,Recall, [38]
|     | Wisconsiin,Phoneme,Vehicle0,and |     | F-measure,AUC,G-mean |     |
| --- | ------------------------------- | --- | -------------------- | --- |
Glass2fromKEEL
−
ImprovedFuzzyKNN Ionosphere,Pima,Transfusion, F-measure,AUC,G-mean [39]
Spectfheart,WinequalityfromUCI,
Phoneme,Vehicle0andEcoli1,
Yeast-2-vs-4,Ecoli4
−
IndustrialIoT(IIoT) Realbuiltdataset Accuracy,FalseAlarm [40]
| testbed |     |     | Rate,Undetectedrate, |     |
| ------- | --- | --- | -------------------- | --- |
Sensitivity,MCC
algorithmic alterations, such as using a hierarchical knowledge base. For the purpose of
balancing the weights of the fuzzy rules that are linked with different classes, Reference
[16]employedarescalingmechanism.InthetechniqueofFuzzyKNN[38],thebenefitsof
theneighbor-weightedKNNapproachweremergedwithfuzzylogic.Itsresultswerebetter
thanNWKNNandAdpt-NWKNN.AnimprovedFuzzyKNNgivenbyReference[39]wasan
adaptiveK-nearestneighborstrategytohandletheimbalanceproblems.Besides,forthepur-
poseofgettingthetestinstancemembershipsfromimbalanceddata,itwasjoinedtofuzzy
K-nearest neighbors. The fuzzy memberships of data instances using adaptive KNN were
more accurate than simple fuzzy KNN. Another study, Reference [40], described a testbed
and created an intrusion detection system (IDS) that is based on machine learning.
Table6outlinesafewalgorithmic-levelsolutionapproachesforimbalanceddatahandling.
2.1.2 Batch Data Handling for Multi-classes. In recent years, the researchers spent much ef-
fort on the situations of data imbalanced in binary-class, which has only two classes. Various
real-worldapplicationsaresufferingfrommulti-classimbalancedclassificationissuesduetothe
widelydisparatedistributionofdataclasses.Itisfrequentlyemployedinnumerousfields,including
textcategorization,humanactivitydetection,andmedicaldiagnosis.Learningfrommanyclasses
makesdata-miningtechniquesmorechallengingwhenconsideringoverlappingacrossclasses[41],
adearthofrepresentativedata,andmixedtypesofdata[42].Unfortunately,applyingthesolutions
thataresuggestedforthebinary-classproblemstomulti-classimbalancedissuescanbeinvalid,
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:15
andsometechniquesareimpossibletobeapplieddirectlytotheimbalancedsituationsofmulti-
classes[43].Itisproposedthat,todealwiththeclassificationofmulti-classproblems,decomposi-
tionstrategiesarepreferablyused.Binary-classimbalanceddatatechniqueshavegeneratedmore
interestintheresearchcommunity.Thesetechniquesallowyoutobreakdownmulti-classprob-
lemsintosmallersub-problemsofthebinary-classesthatcanbeeasilysolved.Thissectiongives
twoofthemostcommonlyusedbinarydecompositiontechniques:
(1) One-vs.-One
—The concentration on one-vs.-one does not affect the positive and negative class
distributions.
—Itreducesthecomputationaltime.
—Thedecisionboundariesofeachbinary-classproblemcouldbeeasiertodeterminethan
the“one-vs.-all”transformation.
(2) One-vs.-All
—Simpler
—Notreliable,becausewhensamplesfromclassesthatarenot“small”enougharecrowded
intooneclass,thedistributionbecomesextremelyimbalanced,especiallyifthesurviving
classisminor[44].
Variousapproacheshavebeendevelopedforaddressingthemajorproblemofmulti-classimbal-
ancedclassdistribution.Thesestrategiescanbeclassifiedintofourlevels:datalevel,algorithmic,
cost-sensitive, and ensemble level. Table 7 summarizes general approaches for handling multi-
classimbalanceddata.
2.1.3 StreamDataHandlingforBinaryClasses. TheIoTcomponentscontainsensorsofvarious
typesthatcollectorgeneratevariousdatathroughouttimefornumeroussectorsandapplications
intheInternetofThings(IoT)era.TheseIoTcomponentscanproducemassiveorquick(real-
time)datastreamswhilerelyingonthenatureoftheapplication.ThedatafromIoTcomponents
canbeconstantlygatheredortransmittedtocreateahugedatasource.Datacreatedorretrieved
inabrieftimeintervaliscalled“streamingdata.”Itworkstogainquickunderstandingand/orto
makerapiddecisions.“Bigdata”includeslargedatasetsthataretoolargefortraditionaltechnology
andsoftwareplatformstostore,manage,process,oranalyze.Becausetheirneedsforananalytic
responsearenotthesame,thesetwotechniquesshouldbeconsidereddifferently.Bigdataanalytics
insightscanbesuppliedwithinafewdaysofdatacollection,buttheanalyticsofstreamingdata
insightsmustbeavailableimmediately.
Applyinganalyticstothesedatastreamstoextractnewknowledge,foreseefuturedisclosures,
andmakejudgmentsinrealtimeisessential.ItidentifiestheIoTasatechnologythatenhances
thequalityoflife.Large-scalestreamingdata,heterogeneity,timeandspatialcorrelation,andhigh
noisearepropertiesofIoTdatathatsetitapartfromordinarybigdata.
2.1.4 Stream Data Handling for Multi-classes. In the case of stream data, new data samples
are continuously created, and their properties evolve when they exist. On the contrary, when
the issue appears, it becomes non-stationary. Therefore, the classifiers must exhibit great speed,
lowcomputingcost,accuracy,andtheabilitytoaccommodatenewexamplescontinuously.Some
data stream applications are more class-imbalanced, i.e., one of the classes is underrepresented.
Thiscausesgreatlearningdifficulties,becausetraditionalmachinelearnersignoreoroverfitthe
minorityclass.Asanimbalancedratio(IR)evolves,afixedIRcannotbeused,theproblemmay
become balanced, classes may switch roles, and overlapping with other classes are a few such
difficulties.Multi-classimbalancedlearningsuffersfrommoredifficultiesthantwo-classproblems
eveninthecaseofofflinelearning.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:16 F.Shariefetal.
Table7. GeneralApproachesforMulti-classImbalancedDataHandling
Technique Method Parameters Highlights Ref
Oversampling ItcombinedtheNeighborCleaningRule(NCL) Recall Whencomparedtoindividual [45]
and toremovetheoutlierswiththeSMOTEto procedures,therecallrateis
Undersampling increasethesamples. higher.
FH-GBMLbased Inthefirststep,one-vs.-onebinarizationandin Probabilistic Itoutperformedthebasicand [41]
onOVO thesecondstep,theSMOTEalgorithmwas AUC pairedlearningmulti-classifier
appliedtoagainbalancethedatabeforethe approaches.
processofpairwiselearning.
Ensemble Binaryensemblelearningmethodologieswere AvgAcc Itdemonstratedhowwell [43]
usedtosupporttheone-to-onescheme.Then, decompositiontechniquesand
theresultswerecombinedusingthevote ensemblelearninginteract.
aggregationstrategytorecreatetheoriginal
multi-classchallenge.
AMDO GSVD(GeneralizedSingularValue P-min, Ithindersperformancewhen [42]
Decomposition)isintroducedforthemixed-type P-avg, dealingwithlow-dimensional
ofdatabyAMDO,whichpartiallydevelopsthe AUCm datasets.
strategyofbalancedresamplingandalso
optimizesthesamplesynthesis.
SMOTE Initially,Kclosestneighborsfromtheminority AUC Theclasscovariancestructure [46]
classarechosen,andtheirdifferenceis isnotpreserved.Overlaps
computed.Then,thefreshsamplesarecreated betweenclassesandmessesup
withintherangeofdifferences. classboundaries.
Oversampling Theoversamplingapproachisdependentonthe - Enhancesaccuracywhile [47]
jointprobabilitydistributionofdataattributes. preservingcovariance
structure.
MDO Thisdistance-basedoversamplingconsidersthe MAUC Effectiveinamulti-class [48]
classwiththemostsamplesasmajority,while imbalancedsituationwith
theremainingclassesbecomesminorities. overlappingclasses.The
Additionalsamplesforeachminorityclassare structureofclassco-varianceis
generatedinproportiontothenumberof preserved.
examplesinthemajorityclass.
Clustering-based Thistechniqueisusedtoincreasethe MI’s Clustering-based [49]
undersampling classificationaccuracyoftheclasswithasmaller F-measure undersamplingproducesbetter
numberofinstances. resultsthanother
undersampling.
Oversampling ImprovedSMOTE(ISMOTE)asanoversampling AUCand Itproducedbetteroutcomes [50]
and techniqueispairedwithdistance-based G-mean thanoversamplingor
undersampling undersampling(DUS). undersampling.
Spectral OVOdecompositionisapplied,followedby P-min, Itshowsbestperformancein [44]
clustering spectralclusteringtoseparateminorityclasses P-avg, comparisontomulti-class
intosubspaces,whicharethenoversampled MAUC imbalancedlearning.
basedondatafeatures
Feature Newfeaturesareextractedusingmulti-intra MFM, ThehighestaverageofMAcc, [51]
extractionwith clusterstocontrolredundancyinmulti-class MAUC, MFM,andMAUCshowsthe
random imbalancedclassification,selectingfeatureswith MAcc potentialofthismethod.
sampling highestsimilarity.Then,aresamplingtechnique
isapplied.
Self-inspected The“visible”nearestneighborsarefoundusing F1score Recommendedwhenthereare [52]
adaptiveSMOTE thenearestneighboralgorithm,whichproduces alotofnearbyneighborsand
(SASMOTE) samplesthatarelikelytobelongtotheminority optimalaverageperformance
class.Theproducedsamplesthatareextremely requiresfine-tuningthe
ambiguousandinseparablefromthemajority uncertaintyscorethreshold.
classarethenseparatedusingaself-inspection
techniqueforuncertaintyelimination.
Thedynamic Allsamplesarefedintothedeepneuralnetwork AUC Deeplearningalgorithm [53]
sampling forthecurrentiteration,andtheperformance outperformedtheother
metricsarecalculatedfortheneuralnetwork algorithmsthatwerechosen
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:17
Intheofflineversionofdata,theclassifierdetectsminorityandmajorityclassesbeforethelearn-
ingbegins.However,onlinelearninghastwoimportantcharacteristics.Thefirstistheunderrep-
resentationofminoritiesinclasssamples,andthesecondistheincrementalarrivalofsamplesin
thelearner.Thiscancauseafewoftheseproblems.
—First,itisimpossibletodeterminetheminorityclassaheadoftime,becausethelearnerlacks
acomprehensivepictureofthedata.
—Second,thestatusoftheminorityclasscanalterovertime.Sincetherearefewersamples
fromminorityclassesthanfrommajorityclasses,updatingthelearnerwithcorrectlycate-
gorizedexamplesmayencourageoverfittingtowardsamplesfromthemajorityclass.
Therefore,theworkpresentedinReference[54]updatedthebaseclassifierafterreceivingeach
samplethatthelearnercorrectlycategorized,insteadofupdatingthelearner.Thisworkallowed
itsclassifiertomisclassifysamplesuptoanacceptableleveltoavoiderroneousupdates.However,
itdidnothaveanymethodforcopingwithconceptdriftandevolvingclassproperties.
Classdecompositionsimplifiesmulti-classimbalanceddatastreams,butitcausesafewproblems
whencombiningbinaryclassifiers.Thenumberofclassesandtheclassifierscouldevolvejustlike
withdatastreams,soitbecomesdifficulttocombinemultiplebinaryclassifiers.Moreover,binary
classifiersaretrainedwithoutfullknowledge,whichleadstoclassificationambiguity.Thework
of Reference [55] dealt with MOOB and MUOB, which processed multi-classes directly without
usingthedecompositionofclasses.
Further, some of the studies, like Reference [56], have focused on recurring classes. A class
becomes a recurrent class when it returns from a prolonged absence from the stream. The
technique that has been used in the study is CLAM, a class-based approach rather than a
chunk-based approach, because a chunk-based approach keeps a fixed-size ensemble. In the
chunk-basedapproach,whenaclassvanishes,allmodelsdevelopedwiththatclassarediscarded,
and no model can recognize the class when it reappears. As opposed to recurring classes being
mistakenlyidentifiedasnovelclasses,theCLAMtechniquediscoversnovelclasses.Iteventually
increasestheaccuracyoftheclassifiers.
Toaddresstheemergenceanddisappearanceofconceptsinadatastream,theworkofReference
[57] offered a method that employed continuous and active learning. AnyNovel detected both
normal(driving)andabnormal(suddenfall)novelconcepts.AnyNovelhastheabilitytoadaptto
changesbyrecognizingrecurringnovelconceptsaswellasabandoned(forgetting)concepts.
2.1.5 ConceptDriftHandling. Astreamofdataisaconstantflowofdatathatarrivesatahigh
rate. In a dynamic streaming environment, the data continuously changes over time along with
theevolutionofthestream.Thechangingnatureofdataresultsintheemergenceofafewunique
characteristics, one of which is the concept drift that occurs with the continuous change in the
concept of the data. These innovative concepts could be examples of fraud detection, network
intrusiondetection,orsuddendropdetection.Itwouldbeaninnovativeconceptthatthesystem
hasneverheardoforbeentaughtabout.
Thestreamdataiscategorizedintothreetypes[58].Thefirsttypeofclassificationtechniqueis
basedonasinglemodel.Itupdatesthesingleclassificationmodelincrementally,anditrespondsto
drifteffectively.Thesecondtypeofclassificationtechniqueisanensemble-basedtechnique,which
maintainsanumberofclassificationmodels.Somenewclassificationmodelsaregraduallyreplac-
ingtheoldonesinthiscategory.Andinthethirdtype(hybrid),singleandensembleapproaches
arecombined.
Whenthestatisticalfeaturesofdatainadynamicstreamenvironmentchangeatdifferenttime
intervals,theproblemofconceptdriftarises.Thisconceptdriftcanbevirtualaswellasreal.Most
often,itischaracterizedonthefollowingbasis[59]:
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:18 F.Shariefetal.
First, it can be categorized on the basis of speed of drift, where it can be abrupt, in which
changes suddenly occur from one concept to another, or gradual, in which transformations
happen gradually over time. Second characteristic is the severity of drift, which can be local
as well as global. Third is the reccurency in which the concept drift can be seen in two ways:
Either it can be a new concept (Novel Concept) or an old concept (Recurrent Concept). The
conceptdriftmayintroducemanysignificantchallengesformachinelearning(ML)models.For
example,thechangeinclasslabelinginvarioustimestepsmaydecreaseaccuracy.Thisproblem
arises in the context of online learning, where patterns shift over time. As a result, machine
learning models must react quickly to changes to preserve the accuracy of their findings. The
machinelearningmodellearnsintwomodes[60],retrainingaswellasincremental.Inthecase
of retraining, the model is trained on the first batch of data, but once drift is detected, the old
model is rejected and the newly predicted model is developed; this is then applied to each new
instanceofdata.Onthecontrary,theincrementallearningworksbyupdatingthepredictedmodel
regularly.
Another challenge to dealing with drift is the recurrence and adjustment of the new concept.
Driftrecurrenceismoredifficultthanthenovelconcept,becauseitismorechallengingtokeep
trackofpreviousconcepts.Thebuyer’spurchasebehaviortobuytheitemsisagoodillustrationof
recurrentdrift.Forexample,everysummer,thewholeactivityofbuyingclothesisrepeated.The
followingfundamentalapproachesareusedtodealwithconceptdrifts[61]:
—Thefirstisinstanceselection,whichaimstoidentifyinstancesrelevanttopresentconcepts.
—Thesecondtechniqueisinstanceweighting,whichusestheabilityoflearningalgorithms
tointerprettheweightedinstance.
—Thethirdmethodisensemblelearning,whichkeepstrackofaseriesofconceptdescriptions,
thepredictionsofwhicharecombinedbyusingavotingsystem,orahighlyrelevantdescrip-
tion is chosen. Finally, the activity of combining the base classifiers is performed through
static(voting,weighted-voting,CVM)ordynamic(DS,DV,DVS)techniques.
When the environment is non-stationary, the distribution of classes is mostly imbalanced. The
otherprobleminthisimbalanceddatastreamisconceptdrift,wherethetargetclasskeepsdrift-
ing all the time. The work performed by Reference [62] accommodated the inclusion of a small
numberofminoritycasesthathadpreviouslybeenapprovedinthetrainingphase.Inaccordance
withthecurrentmajoritycollectionsize,thenumberofacceptablepriorminoritycasesincreases.
TheMahalanobisdistancewasusedtodeterminetheprioritylevelofacceptance.Thisalgorithm
improvedthepredictionaccuracyfortheminorityclass.Thisworkwasnotstrictlyincremental
andwassuitablewhenearlierobserveddatawaskeptandlaterused.
An Online-MC-Queue (OMCQ) algorithm that learns multi-class imbalanced setting was
proposedbyReference[63].Itutilizedaqueue-basedresamplingmethodthatcreatedaninstance
queue for each class. This algorithm was able to dynamically adapt to changes using DDM
algorithmwhilesimultaneouslydealingwithmulti-classimbalanceddata.
A systematic study [64] dealing with class imbalance and concept drift is presented. A
summary of several approaches was provided in Table 8, including DDM-OCI, LFR, PAUC-PH,
RLSACP/ONN,ESOS-ELM,OOB/UOBusingCID.Theseapproacheswerenotappliedtomultiple
classes. According to this study, the performances of RLSACP and ESOS-ELM were not good.
LFR and DDM-OCI were sensitive to concept drift. To detect change, the researcher employed
an adaptive class imbalance technique (OOB). The best strategy overall was determined to be
thecombinationofPAUC-PHandOOBbasedontheobservationsmaderegardingminority-class
recall and G-mean. Researchers have recently focused a lot of attention on this issue, because
many learning problems need to be resolved. To achieve that, this study comprises some open
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:19
Table8. AlgorithmsHandlingConceptDriftandClassImbalanceProblem
Algorithm Detection Advantage Limitation
LinearFour ConceptDrift Thedetectionofdatachange Highrateoffalsediscovery
Rates(LFR) overtime comparedtohybridconceptdrift
PAUC ConceptDrift Fastconceptdriftdetection Thetimedependencebetween
instancesisnottakenintoaccount
RLSACP Conceptdriftand Detectingconceptdriftover Inaccuratefordatasetsthatare
imbalanceddatadistribution imbalanceddataclasses nonlinearand/ornonseparable
MWMOTE Distributionofimbalanced Solvingmulti-classissue Forcertainkindsofdatasets,
data oversamplingisinsufficient
WOS-ELM Distributionofimbalanced Notrequiredtokeeppreviously Itisassumedthattheclassesdonot
data acquiredinformation changewiththepassageoftime
challengesandanexperimentalinvestigation.Thedevelopmentofamoreefficienttechniqueto
detectconceptdriftinimbalanceddatastreamsisoneofthem.
Anotherreviewofacombinedproblemofconceptdriftwithclassimbalancehasbeenpresented
byReference[65].Thisworkgaveacomparativestudyofdifferentclassifiersontheclassimbal-
ance dataset with concept drift. Single learner and ensemble classifiers were used in this study
andtestedonavarietyofdatasets,includingreal-worlddatasetsandsyntheticdatastreamslike
SEA,electrical,andKDDdatasets.Itwasobservedthatclassdistributionhadahighimpactonthe
classificationprocess.Itwasalsonotedthatanensemble-basedalgorithmprovidedbetterresults
whencomparedwithasingleclassifierwhendealingwithconceptdrift.Inthefuture,deeplearn-
ingapproachescanbeusedtodealwithconceptdriftinclass-imbalanceddatastreams.Thiswork
presentedafewalgorithmsandtheirlimitationsusedforconceptdriftwithclassimbalanceissues.
Table9summarizesvariousapproachesforconceptdrifthandling.
Reference [77] presented two major ensemble-based techniques for the detection of concept
driftfromimbalanceddata.SMOTEandLearn++.NSEwereusedtogetherasthefirsttechnique.In
thesecondtechnique,asub-ensembletooktheplaceofSMOTEandLearn++.NSE.Moreover,the
algorithm was compelled to balance accuracy across all classes because of its class-independent
errorweightingschemeandpenaltyrestrictions.ThisworkprovedthatLearn++.NSEshouldbe
usedforconceptdriftindataforthebalancedclasses.Learn++.NIEisapreferredalgorithmina
situationwherebothmajorityandminorityclassesandconceptdriftrequirestrongbalanceper-
formance.Bysettingtheensemblesize,itmaybecreatedconsiderablymorequickly.Learn++.NIE
gains knowledge from new data without needing access to data that has already been observed.
For the proposal of a general framework of concept drift data streams with imbalanced data
distribution, Reference [78] presented a new method for mining data streams that involves
generatingtrustworthyposteriorprobabilitieswithanensembleofmodelstofitthedistribution
acrossnegativeundersamplesandpositiverepeatedsamples.
2.2 PerformanceMetrics
Itisessentialtoemployappropriateperformancemetricstoevaluatetheeffectivenessofvarious
solutionsforhandlingimbalanceddataindifferentdomainssuchasFogcomputing,wirelesssen-
sornetworks(WSNs),andIoT.Theperformanceoflearningalgorithmsontestdataiscommonly
usedtoassesstheirquality.Forthispurpose,thepredictionsofthetrainedclassifiersarecompared
tothetrueclassesofthetestdataandvariousperformanceindicatorsaregenerated.Weexamine
thesemetricsinbothbinaryandmulti-classissues.
2.2.1 Binary-classMetrics. Therearethreedifferentscenariosdependingonhowweinterpret
the classifiers’ output or the amount of information they supply: nominal class predictions,
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

| 16:20 |     |     |     | F.Shariefetal. |     |
| ----- | --- | --- | --- | -------------- | --- |
Table9. ApproachesforConceptDriftHandling
Technique Imbalanced Datasets Tools Baseclassifiers Parameters Ref
Keypoints
RDDM No Itremovedtheearlierinstances48artificialand3 MOA NaiveBayes Accuracy [66]
|     | oftheconceptsfordetecting | real-world |     |     |     |
| --- | ------------------------- | ---------- | --- | --- | --- |
driftsandboostingfinal
accuracy
Comparative Yes Thefinestconceptdrift Artificial MOA NaiveBayesand Precision,Recall,[67]
| analysis | detectorsmustdetectall |     | HoeffdingTree | MCC,Accuracy |     |
| -------- | ---------------------- | --- | ------------- | ------------ | --- |
existingconceptdriftsclosest
totheirrightplaces
Dynamic - Itoutperformsthebest Vitek-60bacterial Weka3.4.2 NaiveBayes, Accuracy [61]
| ensembles’  | stationarybatchlearning  | analyzer | C4.5DT,KNN        |          |      |
| ----------- | ------------------------ | -------- | ----------------- | -------- | ---- |
| integration | technique                |          |                   |          |      |
| Drift       | No Itshowsthevarious     | -        | Python NB,NN,SVM, | Accuracy | [60] |
| handlingfor | alternativesforselecting |          | DT                |          |      |
| prediction  | trainingdataforMLmodels  |          |                   |          |      |
| process     | thatneedtoberetrained    |          |                   |          |      |
Predict- Yes Itdealswithadversarialdrifts, Synthetic,CAPTCHA, - LinearSVM Accuracy [68]
| Detect    | e.g.,datadistributionchanges, | phishinganddigits08 |     |     |     |
| --------- | ----------------------------- | ------------------- | --- | --- | --- |
| framework | thatalterthefeaturesof        |                     |     |     |     |
specificclasssamples
Integrating Yes Momentum-basedstochastic 9syntheticand3real - Hoeffding Accuracy [69]
| Adadeltaand | gradientdescenttechniques |     | AdaptiveTree |     |     |
| ----------- | ------------------------- | --- | ------------ | --- | --- |
| Adamax      | dealswithconceptdrift     |     |              |     |     |
passively
ACNNELM No Itprovidesimprovedaccuracy, MINSTandnot-MINST DeepLearn - Accuracy, [70]
|     | computingscalability,and |     | Toolbox | Cohen’sKappa |     |
| --- | ------------------------ | --- | ------- | ------------ | --- |
conceptdriftadaptability
ISTM No ISTMchangesthemodelafter CityPulsedata - Linear MSEaccuracy [71]
|     | readingtheintermediarydata |     | regression |     |     |
| --- | -------------------------- | --- | ---------- | --- | --- |
matrixagainwhennewdata
arrives
Comparative Yes ThecombinationofPAUC-PH Artificial(SINE1and - Multilayer Recall,G-mean [64]
| analysis | and(OOB)wasfoundtobethe | SEA),Real-world | perceptron |     |     |
| -------- | ----------------------- | --------------- | ---------- | --- | --- |
|          | bestoutofalltheother    | dataset(Tweet,  |            |     |     |
|          | approachestestedfor     | Weather,PAKDD)  |            |     |     |
imbalanceddatawithconcept
drift
| AUC        | YEs EWAUCPHandGM-PH        | -   | - - | G-mean,   | [72] |
| ---------- | -------------------------- | --- | --- | --------- | ---- |
| estimation | demonstrateahighertrue     |     |     | EWAUC-PH, |      |
|            | detectionratethanother     |     |     | PMAUC,    |      |
|            | conceptdriftdetectorsinthe |     |     | EWAUC     |      |
PH-test(TDR)
RBM-IM Yes Itprovidesataxonomyforthe 12Real-worldand12 MOA Adaptive pmAUCand [73]
|     | difficultieswithmulti-class | Artificial | Cost-sensitive | pmGM |     |
| --- | --------------------------- | ---------- | -------------- | ---- | --- |
|     | datawithnovelconceptdrift   |            | Perceptron     |      |     |
HIDC Yes Itusesresamplingfor Citypulseweather - - Precision,Recall,[74]
|     | imbalanceddataandfor        | dataset |     | G-meanand |     |
| --- | --------------------------- | ------- | --- | --------- | --- |
|     | conceptdriftweightingscheme |         |     | delay     |     |
replacestheworstclassifier
DUE Yes Itpreserveslimitedclassifiers, Syntheticandreal MOA VFDT Recall,Precision,[75]
|     | emphasizesmisclassified   | datasets |     | F-measure, |     |
| --- | ------------------------- | -------- | --- | ---------- | --- |
|     | samples,learnsonechunkata |          |     | G-mean     |     |
time,andmanagesvarious
formsofdrift
Imbalanced Yes Localdatapropertiesandlocal Syntheticandrealdata MOA OOB,UOB, G-mean,Recall [76]
| dataanalysis | driftweretakenintoaccount | streams | ESOS,VFDT,OB |     |     |
| ------------ | ------------------------- | ------- | ------------ | --- | --- |
| withdrift    | insteadofglobalfactors    |         |              |     |     |
OMCQ Yes Itfunctionsindependentlyofa Covertype Python, Hoeffding F-measure, [63]
baseclassifier,keepsqueuesfor Scikit-LearnAdaptiveTree, G-mean,Cohen
|     | everyclass,andimplicitly |     | SAM,KNN | Kstatistic |     |
| --- | ------------------------ | --- | ------- | ---------- | --- |
balancesthedatawithout
requiringresampling
Systematic Yes Athoroughreviewand SINE1,SEA,Python,R, - - G-mean [64]
| study | experimentalstudyfor       | Java,scikit-learn,Weka, |     |     |     |
| ----- | -------------------------- | ----------------------- | --- | --- | --- |
|       | handlingimbalanceddatawith | TensorFlow              |     |     |     |
conceptdrift
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:21
numerical scoring predictions, and probabilistic predictions. Now, we will look at each of these
scenariosintermsofbinaryclasses.
(1) Nominal Class Predictions: To assess the model, nominal class predictions compare the
labelsofthepredictedclasstotheactualtrueclassvalues.Theconfusionmatrixisacross-
tabulation of actual and anticipated classes used to summarize how well classifiers per-
form. Depending upon the confusion matrix, many performance measurements may be
constructed.Afewofthemarelistedbelow.
—Accuracy
An accuracy measure is a type of performance metric that is commonly used to assess
classificationperformance.Itisthepercentageofeventsthatwerecorrectlycategorized.
Accuracyanderrorratecalculationsarewidelyusedbuttheyhaveafewlimitationswhen
dealing with imbalanced data. Low error rates or high accuracy can be easily achieved,
anditisalsoassumedthaterrorsarecomputedcostly.Intheconfusionmatrix,accuracy
is represented by the diagonal elements and is calculated using Equation (1) and error
usingEquation(2)givenbelow:
TP +TN
Acc = , (1)
N
Error =1−Acc. (2)
—Kappa
The predicted accuracy is removed from the accuracy in the kappa metric. After that,
1−Acc isusedtonormalizethevalue.Thekappavaluespansfrom−1to1,andvalues
e
less than zero imply that the classifier performs worse than random guessing. The
Equation(3)forCohen’skappaisgivenbelow:
Acc −Acc
k = 0 e. (3)
1−Acce
—Matthew’sCorrelationCoefficient(MCC)
It is a metric that considers all confusion matrix values as well as mistakes and proper
classificationinbothminorityandmajorityclasses.Equation(4)showstheMCCformula.
MCCisascalethatspansfrom −1to+1,with+1reflectingthebestpossibleforecast,0
representingnobetterthanchance,and−1representingtheworstpossibleprediction.
TP.TN +FP.FN
MCC = √ (4)
POS.NEG.PPOS.PNEG
—Precision
Thefractionofcorrectlycategorizedeventsamongthoselabeledaspositiveismeasured
byprecision.Itisametricfordetermininghowaccurateamodelis.Itsformulaisgiven
inEquation(5).
TP
Precision = (5)
TP +FP
—Recall/Sensitivity
The fraction of all positive events accurately labeled as positive is known as recall. The
classifier’s sensitivity to the positive/minority class determines how successful it is. Its
formulaisgiveninEquation(6).
TP
Recall = (6)
TP +FN
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:22 F.Shariefetal.
—Specificity
Theclassifier’sefficacyonthenegative/majorityclassismeasuredbyspecificity[79].Its
formulaisgiveninEquation(7).
TN
Specificity = (7)
TN +FP
—F-measure
TheF-measureemploys aweightedharmonicmean ofthepositivepredictivevalueand
truepositiveratealsoknownasaccuracyandrecall.ItsformulaisgiveninEquation(8).
Precision.Recall
F −measure =2. (8)
Precision+Recall
—G-measure
G-MeasureisavariantofF-Measurethattradesprecisionforrecallbyusingthegeometric
meanratherthantheharmonicmean.Equation(9)showsitsformula.
√
G−measure = Precision.Recall (9)
—G-mean
It is another geometric mean-based measure that incorporates data from both minority
andmajorityclasses.Evenifthenegativeinstancesareaccuratelyidentified,poorperfor-
mance in predicting the positive cases will result in a low G-mean score. This metric is
identical to conventional accuracy when the classes are evenly balanced. Equation (10)
showsitsformula.
(cid:2)
G−mean = Sensitivity.Specificity (10)
(2) NumericalScoringPredictions:Toranktheinstances,themethodsusescore-basedordering
combinedwithpredictionstoawardagradetotestsamplesbasedonhowlikelytheyareto
belongtoacertainclass.Thefollowingisanexampleofnumericalscoringpredictions:
—Receiver Operating Characteristic (ROC) Charts/Area under the curve (AUC):
The ROC curve determines both specificity and sensitivity for a variety of thresholds.
Findingtheidealratioofsensitivitytospecificitycanbedoneusingthecurve.Thearea
under the ROC curve is called the AUC. An ideal model contains an area of 1, whereas
theareaofaworthlessmodelis0.5.
(3) Probabilistic Predictions: The numerical outputs linked with probabilistic predictions are
examples of class probability. The Brier Score is commonly used to evaluate probabilistic
scores.Thefundamentalideaistocomputethemeansquarederror(MSE),withpositive
classes being represented as 1 and negative classes being coded as 0. This computation
involves predicted probability scores and the real class indication. The Brier Score in its
mostpopularformisshowninEquation(11).
(cid:3)N
1
BS = (p −o )2 (11)
i i
N
i=1
2.2.2 Multi-classMetrics. Theaccuracyishelpfulforbinarydatasetclassification,butitdoes
not provide a holistic view of how well our prediction model works. A few other metrics are
requiredforthehandlingofmulti-classimbalanceddata.
—AveAcc
Eachclassisgivenequalweightbytheaverageaccuracy.Theaccuracyrateofeachclassis
determinedseparately,andtheaverageresultisusedforthefinalcomputation.Thefollow-
ingistheformulaforcalculatingtheaverageaccuracygiveninEquation(12).
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:23
(cid:3)m
|     |        | =   | 1   |     |     |      |
| --- | ------ | --- | --- | --- | --- | ---- |
|     | AveAcc |     | TRP |     |     | (12) |
|     |        | m   |     | i   |     |      |
i=1
—AveragePrecision
Itrepresentstheoverallaccuracyofallclasses,anditsformulaisgiveninEquation(13).
(cid:3)c
1
=
|     |     | P a vд | P   | i   |     | (13) |
| --- | --- | ------ | --- | --- | --- | ---- |
c
i=1
—MeanAccuracy(MAcc)
TheMAcciscalculatedbyaveragingtheaccuracyratesofeachclassseparately.Theformula
giveninEquation(14)definesit.
(cid:4)
n MAcc
|     |      | =   | i=1 | i   |     |      |
| --- | ---- | --- | --- | --- | --- | ---- |
|     | MAcc |     |     |     |     | (14) |
r
—MeanF-Measure(MFM)
It calculates the f-measure of each class and then uses the average to calculate the final
results.ItsformulaisgiveninEquation(15).
(cid:4)
r (FM)
|     |     | =   | i=1 | i   |     |      |
| --- | --- | --- | --- | --- | --- | ---- |
|     | MFM |     |     |     |     | (15) |
r
—MeanoftheareaundertheROCcurve(MAUC)
ItistheaveragepairwiseAUCvalueofallthepairsofclasses.Itcananalyzetheefficacyof
imbalancedlearningalgorithmsmoreaccurately.ItsformulaisgiveninEquation(17).
(cid:3)
2
|      | =   |         | (AUC(C |      | ))  |      |
| ---- | --- | ------- | ------ | ---- | --- | ---- |
| MAUC |     | r(r −1) |        | i ,C | j   | (16) |
i<j
(cid:3)
2
| MAUC | =   |     | [A(C ,C | )+A(C | ,C )] | (17) |
| ---- | --- | --- | ------- | ----- | ----- | ---- |
|      | r(r | −1) | i       | j     | j i   |      |
i<j
—Kappa
Although the accuracy metric is effective for binary dataset classification, the distribution
offilledandemptyclassesinourtrainingcontextualizeddatatuplesisuneven.Therefore,
accuracyandtheKappameasurecooperatetopreventinaccuratelypredictedoutcomes[80].
ItsformulaisgiveninEquation(18).
−p
p
|     |     | k = O | E   |     |     | (18) |
| --- | --- | ----- | --- | --- | --- | ---- |
1−p
E
—ProbabilisticAUC
Because accuracy can lead to erroneous results, the more accurate metric AUC is used in-
steadofaccuracy.Weneedtoupdatetheconceptofthismeasureformulti-classsituations,
becauseitwasfirstproposedforbinary-classimbalanceddatasets.So,theKappameasure
and accuracy work together to prevent inaccurately predicted outcomes. For each pair of
classes,asinglevalueiscomputed,includingonepositive(minority)andtheotherasaneg-
ative (majority). Following that, the result’s average is calculated. Its formula is given in
Equation(19).
(cid:3)C (cid:3)C
1
|      | =   |        |     | AUC(j,k) |     |      |
| ---- | --- | ------ | --- | -------- | --- | ---- |
| PAUC |     | C(C−1) |     |          |     | (19) |
j=1k!=j
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:24 F.Shariefetal.
3 ComparisonwithExistingSurveys
In this section, various approaches and results from previous research attempts in imbalanced
datahandlingtechniquesarecriticallyexaminedandsummarized,withafocusonhowtohandle
multi-classimbalanceddataandconceptdriftissuesinthecontextoffogcomputing.Throughan
examinationofcurrentsurveys,thissectionseekstopinpointimportantfindings,knowledgegaps,
andprospectsforfuturedevelopmentsinthefield.Afewofthemarediscussedasfollows:
Mercedes E. Paoletti [81] presented a thorough experimental analysis for imbalanced data in
classificationofhyperspectraldata.Thestudyhadtwogoals:First,itreviewedoversamplingtech-
niquesthatweremoreappropriateforHSdataand,second,itprovidedamorethoroughexperi-
mentalanalysisandcomparison.Thecomparisonofoversamplingmethodsinthepaperwasdone
based on several key criteria: (how the new synthetic samples are generated using the SMOTE
algorithm,consideringtheproximityofminorityclassneighbors);selectionofgeneratorsamples
(howsampleswerechosenfromthedatasettoactasthebasisforgeneratingnewsyntheticdata);
use of classifiers (role of classifiers in identifying which samples or clusters should be used to
generate synthetic samples); sample generation method (specific techniques used to create new
samplesfromtheselectedgeneratorsamples);andlocationofnewsyntheticsamples(wherethese
newsyntheticsamplesarepositionedwithinthefeaturespaceaftertheyaregenerated,whichcan
impacttheeffectivenessoftheoversamplingtechnique).Thisworkgivesthreeexperiments.First
performsacomparisonusingseveralmachinelearningmodels(MLR,SVM,andshallowandDeep
multi-layerperceptron(MLPandDMLP)).Differentdeep-learningmodelswerecomparedin
thesecondexperiment.Thethirdexperimentevaluatedtheimpactoftheclassimbalanceproblem
on the models of semantic segmentation that are trained with different loss functions i.e, focal
loss(FL),cyclicalfocalloss(C-FL),asymmetricfocalloss(A-FL),andcross-entropy(CE).
IthighlightedthelimitationsofADASYNandK-meansSMOTEwithrestrictiveconstraintsonthe
minimumnumberofsamplesperclass.Italsohighlightedtheneedtogenerateafewmoredeep
networkmechanisms.First,itwasnotedthatimbalanceddatasetscausetheclassiccross-entropy
lossfunctiontoperformpoorlyforminorityclasses.Thishasemphasizedhowcrucialitistoad-
dress the class imbalance by utilizing balance-aware loss functions. Ultimately, the research has
demonstrated that mIoU is a more appropriate metric for assessing performance on imbalanced
datasets than overall accuracy. The author suggested expanding this work to include undersam-
plingandoversamplinginthefuture.
D. Devi [82] provided a review of undersampling techniques, then compared and contrasted
afewmethodsofpureundersamplingtechniques,cluster-basedundersamplingtechniques,and,
finally, a comparative study of a few different hybrid undersampling techniques was provided.
Thisstudyproducedalistofafewpointsthatfutureresearcherscanusetohelptheminvestigate
the problem and come up with fresh ideas. The significance of a pattern was highly related to
its neural networks (NNs) and their distribution properties. Combining an informative under-
sampling technique with an efficient clustering algorithm was very effective. Undersampling
with ensemble learning and evolutionary algorithms can be used to achieve a tradeoff between
accuracyandtrainingtime.
AsurveyonsoftwarefaultpredictionforimbalanceddatawasconductedbyS.Pandey[83].The
trainingphaseofadatasetdeterminedthemodel’saccuracy.Therefore,iftherewasadatasetfault,
then it could result in issues with class overlapping, null values, or imbalanced classes. Because
modelsbuiltonfaultydatacouldproduceinaccuratepredictions,softwarefaultpredictionfocused
ondataquality.Thus,themostrecentfaultpredictionalgorithmsinmachinelearning,deeplearn-
ing,andensemblelearningwerecoveredinthissurvey.SMOTE,adatasamplingtechniquebased
ontheliterature,waswidelyusedforsoftwarefaultprediction.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:25
Table10. ComparisonwithExistingSurveys
Ref. Imbalanced Conceptdrift Limitation
[81] Yes No Thissurveyprimarilyfocusesonoversamplingtechniques,and
otherimbalancecorrectionstrategiessuchascost-sensitiveor
algorithmicapproachesarenotdiscussed.
[82] Yes No Computationalcostofundersamplingtechniqueisnotdiscussed.
Certainundersamplingtechniquesmaybecomeineffectivein
practicalapplicationsforlargedatasetsbecauseoftheirhigh
dimensioncosts.
[83] Yes No Thissurveyreportfocusesonspecificmethods(SMOTE)limiting
exploringalternativeorcomplementaryapproachestoaddressing
classimbalanceissues.
[84] Yes No Thissurveycomparesthetechniquesthatonlyusef-measureand
donotprovideacomprehensiveevaluationofothermetrics.
[85] Yes No Thereisnotenoughnoveltyorcomparativeanalysisinthiswork.
[86] No Yes Itdoesnotdelvedeeplyintothespecificmethodologies,their
strengths,weaknesses,orcomparativeperformance.
[87] No Yes Itmightmakeitmoredifficulttodirectlycomparestrategies,
sinceitlacksaconsistentevaluationmetricforevaluatingthe
efficacyofvariousconceptdrifthandlingtechniques.
A.Sharma[84]presentedasurveyreport.Themethodsforhandlingimbalanceddatathatwere
proposedbydifferentresearcherswerelistedinthissurveyinthefollowingcategories:data-level,
algorithmic,hybrid,kernel-based,andcost-sensitive.Usingacommondatasetandsetofclassifiers,
theapproachespresentedinthissurveywerecomparedusingF-measurevalues.Theanalysisof
theseapproachesledtotheconclusionthatSMOTEovercamethelimitationsofRUSandROS.
A review of17researchpaperspublishedbetween2018and 2021wasgiven bySJ Basha[85].
To address the issue of class imbalance, this survey offered the following imbalanced dataset
classification methods: KNN, updated KNN with feature selection, Distributed deep learning,
GAN,Gradientboosting,iterativeexpansionalgorithm,KSAMOTE,IAdaBoost,RandomOversam-
pling,RCT,Labelenhancementtechnique,andoversamplingwithDLapproach.Thesestrategies
addressedtheproblemofclassifyingimbalanceddatasets.
Thissurveyaimstoaddresslimitationsbydiscussingvariousimbalanceddatahandlingstrate-
giesbeyondoversampling,includingcost-sensitiveandalgorithmicapproaches,whilealsoaddress-
ingconceptdriftchallenges.Itplanstoexplorealternativemethodstotackleclassimbalanceand
conceptdrifteffectively,evaluatingtechniquesusingdiversemetricsforacomprehensiveassess-
ment.Furthermore,thesurveyseekstoimproveunderstandinginthefieldbyenhancingitsanaly-
siswithmorenovelty,comparativestudies,andathoroughinvestigationofmethodologiesinthe
contextofmulti-classimbalancedstreamdatainFogcomputing.
4 ApplicationsofImbalancedDataHandlingTechniques
The term “imbalanced class distribution” refers to the tendency of a dataset collected through-
outtheprocesstohavemoreobservationinstancesrelatedtooneclassthantotheotherclasses,
and a dataset with such a property is known as “imbalanced data.” The imbalanced data prob-
lemfrequentlyarisesduringdataprocessinginIoTapplications.Undernormalcircumstances,it
ischallengingtocollectenoughsamplesofunusualconditions,andcreatingunusualconditions
wouldbeprohibitivelyexpensiveordangerous.Imbalancedlearningisapressingsubjectthathas
beencoveredbynumerousscholars,andherewediscussitinvarioussections.
ImbalanceddatahandlinginvariousnetworksisexploredinSection4.1.Section4.1.1presents
binaryandmulti-classimbalanceddatasethandlinginawirelesssensornetwork.ForIoTnetworks,
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:26 F.Shariefetal.
Fig.4. Taxonomyofimbalanceddatawithconceptdrift.
theprogressfortheimbalancedIoTdatasethandlingisdividedintobinary-classandmulti-class
batchdata.Forstreamingdata,theimbalanceddatastreamhandlingforbinary-classesandwork
forimbalancedmulti-classdatastreamsintheIoTnetworkisfurtherelaboratedoninSection4.1.2.
ThelatestresearchonimbalancedbatchandstreamdatahandlinginFogcomputingisdiscussed
inSection4.2.TohandleconceptdriftalongwithimbalanceddataintheFogcomputingenviron-
ment,differenttechniquesarealsoexploredinthissection.Figure4showsthetaxonomyofthe
imbalanceddatawithconceptdrift.
4.1 ImbalancedDatainNetworks
Manysmall-andlarge-scaleenterprisesthatemploynetworkservicestocarryouttheireveryday
activitieshaverecentlybenefitedfromtechnologicaladvancementsintermsofcomfortandoppor-
tunities.Itallowsforexploringandexploitingseveralattacksbyintrudersorattackers.Today’s
escalatingcyberattacksonnetworksleadtoanimbalanceddistributionofclasses.Theseproblems
havebeenaddressedusingavarietyofapproaches.Thefollowingdescribesafewofthese.
4.1.1 ImbalancedDataHandlinginWSN. Awirelesssensornetwork(WSN)ismadeupofa
largenumberoflow-power,battery-powered,andlow-costsensornodes.Asthesesensornodes
are non-rechargeable and have minimal energy resources, they must be properly controlled to
extendthenetwork’slifespan[88].Whensensorscreatedata,thereisapotentialthatthedatawill
bediscontinuous,resultinginsparsedatathatisimbalanced.ImbalanceddataprocessingforWSN
iscoveredinseveralcircumstancesgivenbelow:
—ActivityRecognition
Someactionsoccurmoreoftenthanothersinactivityrecognitiondatasets,resultinginan
imbalanced dataset. The goal of Reference [89] was to solve class imbalance problems in
automatedactivityidentificationfrompatternsofbinarysensorsinasmarthome.Initially,
publicly available datasets from three different households were used. The activities of an
individual residing in an apartment were monitored using a wireless sensor network in
which each sensor was connected to a node. A base station gathered the data, which was
then labeled using a wireless Bluetooth headset and a software for voice recognition, as
well as a handwritten journal or a PDA. The model recognized the activities based on the
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:27
binarysensoroutputs.Insteadofrepresentingrawvaluesofsensors,theauthoremployed
the “change point” representation (which assigns the value one (1) when the reading of
sensor changes from one (1) to zero (0) or zero (0) to one (1)) and “Last” representation
(which assigns one (1) to the “last” sensor that changes state until a new sensor changes
state).Allcoursesthatlastedlonger(idleandsleeping)wereclassifiedasmajorityclasses,
while others were classified as minority classes. In the trials, the SVM hyper-parameters
(σ,C)weretuned.Severalbinaryclassifiersweretrainedusingamulti-classCSVM.Finally,
a learning approach combining multi-class SMOTE-CSVM and OS-CSVM was presented,
with results showing that resampling methods were more efficient than CSVM, CRF, and
CS-SVMinclassifyingmulti-classsensorydata.
—ManufacturingProcess
Incomplete and missing values can be found in data obtained from semiconductor man-
ufacturing processes in a real-world setting. This incomplete and imbalanced data gives
biasedresults.So,Reference[90],usedtwostepstoovercomethisproblem.Initially,KNN
performedthemissingvalueimputation.Then,usinganAdaptiveSyntheticSamplingtech-
niqueanda2-layerFeed-forwardNeuralNetworkasaclassifier,theysolvedtheimbalance
problem by artificially introducing additional minority class samples and forecasting the
faulty items. Although the suggested approach did not perform well with an incomplete
dataset,itdidobtainahighandtolerableidentificationperformancewithnobias.
— EnergyConsumption
The sensors’ energy consumption may become imbalanced and cause particular local
nodestodepleteprematurely.Inthisscenario,typicalclassificationmethodsarefrequently
foundtobeerroneousandoptimized.[91],suggestedanoveltechniquethatextendedthe
streamclassificationalgorithmtotheanalysisofWSNtolessenthenegativeimpactofthe
imbalancedclassofdata.Thistechniquewaslowonresourcesanddidnotnecessitateany
preprocessing,whichwouldhaverequiredgoingthroughtheentiredatabase.Itemployed
naive Bayes predictors at the leaf nodes of the decision tree to limit the influence of
imbalancedclasses.Astreamclassifierwasusedinsteadofastandardclassifierinthisstudy.
—Cluster-basedRouting
Inacluster-basedwirelesssensornetwork,non-uniformnodedistributionproducesuneven
energy consumption across nodes. It is a critical issue impacting network services. As a
result, [88], presented a cluster-based routing protocol for WSNs with non-uniform node
distribution to address this issue. This protocol included the energy-aware clustering
algorithmEADC,whichbuiltclustersofevensizes,andthecluster-basedroutingalgorithm,
which adjusted the intra-cluster and inter-cluster energy consumption of cluster heads
to balance the energy consumption among cluster heads. By compelling cluster heads to
acceptnodeswithgreatenergyandfewernodesasnexthops,loadbalancingamongcluster
heads is achieved, resulting in an even distribution of energy consumption across nodes
and a rise in the number of nodes. According to a review report presented by [92], a few
piecesofworkhaveconcentratedonimbalanceddatahandlinginWSN.Thispieceofwork
provided suggestions for extending traditional imbalanced data handling approaches to a
WSN, especially K-fold cross-validation, ensemble resampling datasets, assigning weights
toattributes,cost-sensitivelearning,andcombinedclassmethods.
—IntrusionDetectionSystem
Anintrusiondetectionsystemmonitorsnetworktrafficinrealtimetodistinguishbetween
maliciousattacksandnormaltraffic.Becauseitmustproperlydetectallthreats,eveninthe
presenceofatinypercentageofintrusiondata,[93]focusedonanimbalanceprobleminthe
intrusiondataset.Thestudyusedfourprominentclassificationapproachestoexaminethe
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

| 16:28 |     |     |     | F.Shariefetal. |     |
| ----- | --- | --- | --- | -------------- | --- |
Table11. ComparisonofImbalancedDataHandlingTechniquesinWSNforBatchandStreamData
Technique Strategy Class Conceptdrift Dataset Tools Parameters Ref
SoftMargin Sampling Multi(Batch) No Datasetsof3Houses Matlab Accuracy [89]
SVM
KNN- Algorithm Binary(Batch) No Secom,Secom1, - Recall,Precision, [90]
| ADASYN- |     | Secom2 |     | F1-measure |     |
| ------- | --- | ------ | --- | ---------- | --- |
FNN
OVFDT+FL Algorithm Multi No LED24,Connect-4, MOA Accuracy,ROC, [91]
|     | (streams) | Waveform21,RBF, | simulator | compactDTsize |     |
| --- | --------- | --------------- | --------- | ------------- | --- |
RT,COVTYPE
Cluster Algorithm Binary(Batch) No NS-2simulator No Sensorfield,BS [88]
| basedinter- (Clustering) |     |     |     | location,theinitial |     |
| ------------------------ | --- | --- | --- | ------------------- | --- |
| cluster                  |     |     |     | energyofnodes,#     |     |
| algorithm                |     |     |     | ofnodes,data        |     |
packetsize
| Dataset Survey | Multi(Batch) | No NSL-KDD | Weka | Accuracy | [93] |
| -------------- | ------------ | ---------- | ---- | -------- | ---- |
evaluation Report
Correlation- Feature Multiand No SatimageBreast Weka,NS-2 Accuracy [94]
| based selection | Binary(Batch) | Wisconsin,Glass, | simulator |     |     |
| --------------- | ------------- | ---------------- | --------- | --- | --- |
| scheme and      |               | Yeast,Phoneme    |           |     |     |
Clustering
WSVM Algorithm Binaryand No Datasetof3Houses MATLAB, Accuracy,class [95]
|     | Multi(Batch) |     | LibSVM | accuracy |     |
| --- | ------------ | --- | ------ | -------- | --- |
Table12. ConceptDriftinWSN
| Technique KeyPoints |     | Dataset Tools | Parameters |     | Ref |
| ------------------- | --- | ------------- | ---------- | --- | --- |
FedConD Itaddressesconceptdriftonlocal AirQuality, FedConD Regularizationparameterofthe [96]
devicesandusesacommunication extrasen- framework objectivefunctiononeachlocal
| strategyontheserversidetoselect |     | sory | device |     |     |
| ------------------------------- | --- | ---- | ------ | --- | --- |
localupdates.
Angle Projectvarianceandprojection Synthetic AOGEand Projectionvarianceandprojection [97]
Optimized anglesareusedtoanalyzethe dataset PCA angle,constraintparameterfor
Global principalcomponents,andthe (Circle,Sine, determiningtheoccurrenceof
Embedding changeinsubspaceisusedtodetect andLine) conceptdrift
| (AOGE) theoccurrenceofconceptdrift. |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- |
HybridBatch GAHSusesanonlinemachine AirQuality - Pearsoncorrelationcoefficient, [98]
determinationcoefficient(R2),root
| Online learningcalibrationfunctionor |     | Low-Cost |     |     |     |
| ------------------------------------ | --- | -------- | --- | --- | --- |
Stacking functionsthatareupdatedona Sensor meansquarederror(RMSE),mean
Ensembles regularbasisfortheentirenetwork Network absoluteerror(MAE),relative
integrated inadditiontobatchmachine (AQLCSN) expandeduncertainty(REU)
| withGA learningalgorithms. |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- |
NSL-KDDdatasetanddiscoveredthatseverelyimbalancedclasseswerenotsuccessfullycat-
egorized.RandomForest,whichisanensemble-basedclassifier,performedwellforafewmi-
noritiesandtheremainingmajorityclassesbutstruggledwithseverelyimbalancedclasses.
Table11showsacomparisonofimbalanceddatahandlingtechniquesinWSN
NumerousstudiesonconceptdriftinWSNenhancethepredictionaccuracyandadaptabilityof
WSNsystemsindynamicenvironments.Belowaresomeofthem.
4.1.2 ImbalancedDataHandlinginIoTNetwork. TheIoTisthenetworkofcomputing-capable
and Internet-connected devices that are typically not thought of as computers. Because of the
maximumuseofthesesmartdevicesacrossnumerousnetworks(home,business,military,etc.),a
numberofproblemshaveemerged,andoneofthemisdataimbalance.Therehasbeenextensive
researchontheimbalanceddataintheIoT,whichhasbeendividedintobinaryandmulti-classdata.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:29
Table13. ImbalancedBatchDatainIoTNetworkforBinaryClasses
Technique Strategy Datasets Tools Parameters Ref
Anomaly-based Resampling CIDDS-001 Weka,MATLAB, Accuracy [103]
IDS Keras
DeL-IoT Ensemble,Feature Testbeddataaswell - F1-measure,MCC [3]
Extraction asBenchmarkdata
CSSAE Cost-sensitive KDDCUP99and DARPA’sevaluation Accuracy,Recall,Precision, [100]
NSL-KDD program F-measure,FalseAlarmRate
Imbal-OL Resampling CIFAR-10AND IoTboard(Google AcceleratedRaspberryPi4, [101]
CIFAR-100 CoralDevboard, andNVIDIAJetsonNano)
IntelMovidiusNCS)
Frameworkfor Ensemble - Keras,PySpark Accuracy [102]
handlingIoT
datasets
Deeplearningmodelsaretrainedprogressivelyovertime.Theyreducetheirstatictrainingwithall
ofthedata.Todealwithimbalanceddata,combiningclass-incrementallearningwiththeIoTisa
newlyintroducednotionthatisstillintheearlystagesofdevelopment.ThemainfeatureofRefer-
ence[99]’sdatasamplingalgorithmwasthecapabilityofsamplingdatafromnovelclasseswithout
usinghyperparametersbyautomaticallychoosingthenumberofsamplesrequiredperincremental
trainingsession.AfewstudiesforhandlingimbalanceddataintheIoTarementionedbelow:
(1) Binary-classBatchDataHandling:
In the case of IoT data, the security risks have sharply increased recently, and the attack
methods used by the attackers are frequently changing and improving. Additionally, the
frequency and complexity of imbalanced class distributions in most datasets point to the
necessityforadditionalresearch.Asfarasbinary-classimbalanceddatainIoTnetworksis
concerned,Table13givesvariousresearchapproaches.TheDeL-IoTtechnique,proposedby
Reference[3],wasintroducedtodetectSDN-basedIoTanomalies.Italsoaddressedtheissue
ofmulti-classaswellasbinary-classdatabeingimbalanced.Inanothertechniqueof cost-
sensitive stacked auto-encoder (CSSAE) [100], stacked autoencoder with the Sigmoid
function employed in the initial stage. The SAE of the second phase, however, used Tanh
asanactivationfunction.ThetwoSAEs’learnedfeaturesweremerged.Thistechniquewas
used for both binary and multi-classes. The technique of Reference [101] was suggested
as an OL (Online Machine Learning) plugin that would process actual IoT streams and
after that send them to the learner. After the whole process, the local on-device model is
updated.Itworkedondatastreams.AframeworkforhandlingIoTdatasets[102]adopted
Adamoptimization,anextensionof stochasticgradientdescent(SGD),whichhaslately
gained wider recognition for deep learning and IoT applications. It also worked for batch
andstreamdata.AccordingtoReference[103],itwasobservedthatdatasetcharacteristics
matter,butclassdistributionhadlittleeffectontheclassificationissue.
(2) Multi-classBatchDataHandling:
Amulti-classimbalanceddatasetisconsideredanimbalanceddatasetwhentherearemore
occurrencesofafewoftheclassesinthetrainingsetthanthereareofotherclasses.Itaf-
fectshoweffectivemachinelearningalgorithmswork.Incomparisontothealgorithmsof
ML,deeplearningtechniquesperformwellwhenlearningfromhugevolumesofdata,but
theirperformancesuffersdramaticallywhenlearningfromimbalanceddata.Formeasuring
theperformanceofmulti-classdatasets,macrometricsareusedtoindependentlycalculate
the metrics for each class, and after that, it takes the average for multi-class imbalanced
data.Variousmodelshavebeensuggestedformulti-classbatchdata.Forinstance,themodel
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:30 F.Shariefetal.
Table14. ImbalancedBatchDatainIoTNetworkforMulti-classes
Technique Strategy Datasets Tools/frameworks Parameters Ref
RITIDS Algorithmic CICIDS2017,BoT-IoT Weka,MySQLRDBMS Accuracy,Detection [104]
rate,FalseAlarmRate,
TimeOverhead
GANModel Generative CICIDS2017 Python,TensorFlow, RecallorF1-Score [105]
Adversarial Scikit-learn
Nets
CSSAE Cost-sensitive KDDCUP99and DARPA’sevaluation Accuracy,Recall, [100]
NSL-KDD program Precision,F-measure,
andFalseAlarm
DAMSID Ensemble SEA - Accuracy [106]
Comparative Resampling KDD99,UNSW.NB15, SparkMLib Macroprecision,Macro [107]
analysis UNSW-NB17, recall,MacroF1-score
UNSW-NB18
Adaptive Ensemble NSL-KDD,Synthetic, PythonAnaconda,Spyder Sensitivity,F1-score, [108]
boosting-based KDDCUP99,DS2OS IDE,Pandas,Imblearn, ROC-AUC
model Numpy,Matplotlib
GWO–PSO–RF Feature KDDCUP99,NSL-KDD, Python,Anaconda Accuracy [109]
NIDS Extractionand CICIDS-2017 Navigator
Resampling
proposed by Reference [104], was made up of three classifiers, two of which run simulta-
neously and feed the third. Evaluation results revealed that this hierarchical model beats
various popular and contemporary machine learning algorithms. Reference [105] displays
that“whenRandomForestwasusedtoclassifydataafterGANresampledit,itsperformance
outperformed that of a single RF alone.” The model of Reference [100] recommended that
theissueofclassimbalanceinIDScouldbesolvedbyacost-sensitivestackingauto-encoder.
Itwasusedbothforbinaryaswellasmulti-classes.Theissuesofclassificationwithconcept
driftsandimbalanceddataweresimultaneouslyaddressedinReference[106].Todetermine
the most effective methods for handling imbalanced data, six separate datasets were sub-
jectedtofivedifferentresamplingtechniquesinReference[107].Reference[108]presented
anensemblelearning-basedapproachwiththeSMOTE.Itsuccessfullyhandledboththeim-
balancednatureofthedataandtheanomalypredictionintheIoTnetworkdataDS2OS.To
achievemaximumattackdetectionaccuracy,themethodwassuggestedbyReference[109],
usingParticleSwarmOptimization(PSO)andGreyWolfOptimization(GWO)forex-
tracting meaningful IoT network features that were then given to a random forest (RF)
classifier.Itworkedforboththebinaryandmulti-class.
Table14summarizestheserecentapproachesforimbalanceddatainIoTformulti-classes.
(3) Binary-classStreamDataHandlingwithConceptDrift:
Thecontinuousarrivalofdatathatmustbeanalyzedatonceoneachscancauseschallenges
for stream data mining. Moreover, a number of challenges have to be taken into account
whiledealingwithstreamsofimbalanceddata.Theconceptdriftisoneofthesechallenges.
Theresearchersoffereddifferenttechniquestohandlethesechallenges.Thetechniquemen-
tioned in Reference [110] processed the fixed-size chunks twice: once using oversampling
andonceusinganensembleofpredictionmodels.Itperformedbetterwithashortertime
delay and can be employed with dynamically imbalanced data streams. According to the
technique proposed by Reference [111], to a large extent, CtRUSBoost surpassed all of its
competitorsindetectingtransactionsasnormalorfraudulent.Thetechniquepresentedin
Reference [112] did not take as much time as other evaluated algorithms. It employed a
resamplingmethodthatconcurrentlytookconceptdriftintoaccountandfollowedthatwith
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:31
Table15. ImbalancedDataStreamsalongwithConceptDriftinIoTNetworkforBinaryClasses
Technique Strategy ConceptDatasets language/Tools/ Parameters Ref
Drift frameworks
ICMS Resampling Yes Syntheticdata(staticand MOA, Accuracyscore,G-mean [110]
dynamicImbalancedRatio) Stream-learn, score
Scikit-multiflow
CtRUSBoost Ensemble No 3datasetsofcreditcard - Sensitivity,specificity, [111]
fraudfromKaggle precision,F1-score
GRE Ensemble Yes SEA,Radialbasisfunction, JAVA,MOA Accuracy,Recall, [112]
Hyperplane,Electricity F-measure,G-mean,AUC
pricing(Elec)
PWIDB Automated No (ECC)dataset,UCIAdult - AUC-ROC,F1-score [113]
datare- dataset
balancing
PWPAE Ensemble Yes IoTID20,CICIDS2017 Python, Accuracy,Precision, [114]
Scikit-Multiflow Recall,F1-score
Two-layer Feature No Adultcensusdataset,Bank ApacheSpark Accuracy [115]
ensemble selection marketingdataset
Kohonennets
anensembleupdatemechanismandadetailedanalysisofboththereal-worldandsynthetic
datasets.TheframeworkproposedbyReference[113]usedabatch-incrementalprocessto
handlethedemandsofdealingwithimbalanceddatastreamsdynamically.Anotherframe-
workproposedbyReference[114]wasadrift-adaptiveframeworkforfindinganomaliesin
theIoT.Itwasbuiltbyusinganensembleofcutting-edgedriftadaptationtechniques.The
technique given in Reference [115] was more concerned with identifying and separating
areaswheretheminorityclasswasconcentrated.AccordingtoasurveyreportbyReference
[116],themajorityofsolutionswereproposedfordatasetswithbinary-classesandnotwith
multi-classes. However, before inclusion, multi-class datasets need to be transformed into
binary-classes. Table 15 summarizes these techniques for imbalanced data streams having
conceptdriftinIoTforbinary-classes.
(4) Multi-classStreamDataHandlingwithConceptDrift:
Attacksmakedatastreamsimbalancedandmakeitpossiblefortheconceptofadatastream
to change over time. To deal with this problem, a few researchers have presented their
work. For example, a survey report given by Reference [117] assessed both imbalanced
datastrategies’effectivenessanddemonstratedhowmachinelearningalgorithmsmanage
streams of network traffic. A method in Reference [118] was suggested to change the
low-weighted data in the contextual information while keeping the weighted data in the
acquisition of contextual information, as opposed to applying uniform oversampling or
undersampling. Reference [119] expanded the concept drift procedure into imbalanced
class circumstances by creating an adaptable learning algorithm with a Windows-based
methodology. Reference [120] took two steps. First, cost-sensitive learning was employed
in the process of feature selection. Then, a cost-sensitive weighting schema was designed
toupdatetheweightofthelatestdatablock.Table16summarizesdifferentapproachesfor
dealingwithimbalanceddatastreamsandconceptdriftintheIoTformulti-classes.
4.2 ImbalancedDataHandlinginFogComputing
Thecloudservicesarepushedtothenetwork’sedgethroughadistributedcomputingmodelcalled
Fog. Fog computing techniques have been proposed to reduce latency and computing load. The
pieces of work presented by different researchers for batch and stream data handling show the
importanceofthisfield.Afewoftheseresearchworksaregivenbelow:
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:32 F.Shariefetal.
Table16. ImbalancedDataStreamalongwithConceptDriftinIoTNetworkforMulti-classes
Technique Strategy Concept Datasets language/Tools/ Parameters Ref
Drift frameworks
Surveyon Tree-based Yes UNSW-NB15, Scikit-multi- Accuracy, [117]
networktraffic algorithm, NSL-KDD,UNSW2018 flow,Python Kappa,Cohen’s
streamanalysis Ensemble package Kappa
Smart Data-level No Datareportedby Smart - [118]
switchboard sensors switchboard
imbalanceddata
FP-EStream Algorithmic Yes 3entriesfromparking MOA,NetLogo Speed [119]
lotofUniversityof
Essex
(1) BatchDataHandlinginFogComputing:
At present, a few works have been done in imbalanced data handling in Fog computing.
One of the key contributions of this research is to present the work done for imbalanced
batch data handling in Fog computing. For example, a Fog-based unsupervised machine
learning prototype for a large volume of data analysis was developed in Reference [121],
whichreplacedtheinitialdeploymentofmachinelearningmodulesandsignalprocessorsin
the cloud for processing physiological data. The Parkinson’s disease patients wore smart-
watches that collected speech data to assess their speech impairments. The speech data
was sent from a smartphone or tablet to a Fog computer. K-means clustering was utilized
toprocesssomefeaturesontheFogcomputer.Reference[122]presentedacomparisonof
cloudandFogcomputing,somechallenges,andopenissuesinFogcomputing.Thisresearch
alsoanalyzedFogcomputingdeploymentinintelligentlogisticcentersandprovedthatde-
ploymentofFogcomputingimprovesenergyefficiency,reduceslatency/costs,andsupports
mobility.
Anotherstudydiscusseshowmachinelearningcanbeusedtoperformmoreaccuratefault
detectionwhencollectingdata.Real-timefaultdetectionhasafewissues.Oneoftheissues
is an imbalanced class, which causes extreme difficulty in using machine learning models
inreal-worldsettings.Inthecaseofanimbalancedclass,wherethenumberofinstancesof
oneclassisgreaterthanthatofanother,themachinelearningmodelisoverfittedtowards
numerousexamplesandcausesperformancedegradation.Becausethefaultdoesnotoccur
frequently,mostdataoccurinanormalstate,makingitaserioussituation.Toovercomethe
classimbalance,themethodologiesthatareadoptedbyReference[123]arethecomputing
architecturesolutionmethodandthealgorithmsolutionmethod.Table17summarizesdata
handlinginFogcomputing.
(2) StreamDataHandlinginFogComputing:
DatastreamprocessingandanalyticsareusedinmanyFogapplications.Thesearewidely
used in the cloud but have yet to be thoroughly examined in the context of Fog architec-
ture.Byexaminingthecommonaspectsofnumeroustypicalapplications,Reference[132]
describedthemainprinciplesandarchitectureofFogdatastreaming.
DatastreamsintheIoTenvironmentaremadeaccessibleinunlimitedflows,continuously
producedathighspeed,andtheirbehaviorchangesovertimeratherthanremainstationary.
These qualities of the data make it known as “real-time big data” and give it several Vs
(volume,velocity,variety,andveracity).Thesecharacteristicsarerelatedtothehugevolume
ofcontinuouslygenerateddata,thehighspeedatwhichseveraldevicesgenerateIoTdata,
the variety of devices and data sources, and the effect of data by environment and noise
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:33
Table17. ImbalancedBatchDatainFog
| Objective                      | ImbalancedFogNodes | Privacy/Security | QoS/QoE    | Ref   |
| ------------------------------ | ------------------ | ---------------- | ---------- | ----- |
| ItexploredmachinelearningonFog | No Edisonand       | -                | Resource   | [121] |
| deviceswithlimitedresources    | RaspberryPi        |                  | Management |       |
Ranking-basedjobschedulingsystem No AnyFog Usersatisfaction,MatLab [124]
| fromthemostsuitableFognodesto | provider | Energy,Latency |     |     |
| ----------------------------- | -------- | -------------- | --- | --- |
theleastsuitableones
Adynamicmulti-goalapproach No LocalCentral - EnergyEfficiency [125]
managestheenergyofIoT-based device,Gateway
wearablesystems device
| Anomalydetectionusingdata-driven | No - | Accuracy,Low | -   | [126] |
| -------------------------------- | ---- | ------------ | --- | ----- |
| networkintelligence              |      | latency      |     |       |
TheuseofFogcomputinginthe No Gatewaysand - Mobility,Energy [122]
| logisticssystem | Fogdevices |     | Efficiency,Reduce |     |
| --------------- | ---------- | --- | ----------------- | --- |
latency,cost
InaFogcomputing(FC)scenario,this No Gateway - Latency,Network [127]
| intelligentanalyticalmodelwasused |     |     | usage,Ram        |     |
| --------------------------------- | --- | --- | ---------------- | --- |
| toallocateandselecthealthcareIoT  |     |     | consumption(MB), |     |
| datapackets                       |     |     | (Net-Beansand    |     |
Spyder)
| Itprovideda3-tierArchitecturefor | No Gateway | -   | Latency | [128] |
| -------------------------------- | ---------- | --- | ------- | ----- |
reducingnetworklatencyin
HealthcareIoT
| DevelopedthreeIoTnetwork      | No Gateways | -   | Lowpower       | [129] |
| ----------------------------- | ----------- | --- | -------------- | ----- |
| architecturaldesignsforthe    |             |     | consumptionand |       |
| LoRaWANcloudarchitecture,then |             |     | Location       |       |
| optimalisselected.            |             |     | awareness      |       |
IoT,Fog,andCloudintegration(iIFC) No Gateway Security Energy,Transport [130]
| enablesoptimizedapplication |     |     | health,etc. |     |
| --------------------------- | --- | --- | ----------- | --- |
performance
Analgorithmsolutionmethodanda Yes Fogclusterfor Reduces F-measure,G-mean[123]
| computingarchitecturesolution | eachgroupof | performance    |     |     |
| ----------------------------- | ----------- | -------------- | --- | --- |
| methodwereusedtoovercomethe   | sensors     | degradationand |     |     |
| classimbalanceproblems.       |             | computational  |     |     |
load
Todevelopalightweightanomaly Yes Fogdevices Security Precision,Recall [131]
| detectionmodelfordeploymenton |     |     | andF1-score |     |
| ----------------------------- | --- | --- | ----------- | --- |
Fognodes
transmission. The important characteristics of mining data streams are the use of short-
termmemoryasaqueuetostoresubsetsofdataandtheuseofalimitedamountofmemory.
Othercharacteristicsincludemaintaininglinearspatialandtemporalcomplexitytooperate
withintheexecutiontimeandprovidingasolutionwhenrequired.
Reference[128]offerstheFogcomputing3-tierarchitecturethatconsistsoffuzzylogicand
reinforcementlearning.Thisarchitectureminimizedlatencybyutilizingmachinelearning
and virtualization approaches. The first layer was the IoT layer, which contained sensor
devicesthatproduceddata.Theclassificationofthedatawasdoneusingafuzzyinference
technique. The classified data was sent as streams in a Fog computing environment to a
real-timeanalyzerlikeApacheSPARK.ThesecondwastheFoglayer,whichuseddistributed
reinforcementlearningtoselectthatdatafromtheclassifieddatathatismosttime-sensitive.
Afterthat,itperformedthevirtualizationoftheFogserverfordataallocation.AniFogsim
andaSpydereditortoolbasedonPythonwereusedforsimulatingtheFogcomputing-based
architecture and analytical models and for analyzing the performance of the architecture
andthealgorithm.Intheend,thethirdlayerwasthecloudthatcontaineddataforfutureuse.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:34 F.Shariefetal.
Reference [133] presents a new hybrid security strategy (HS2) that is merging the
strengths of steganography with cryptography to create a method for protecting the Fog.
The first contribution of HS2 is a new encryption technique that depends on n-blocks of
linear feedback shift registers (LFSRs) merged with a subtractor or adder for creating
the strong key for each and every block. Then, all the blocks were combined to generate
afinalkey.Thesecondcontributionisthesteganographymethodologybasedonupgraded
discrete wavelet packet transform (DWPT) that is used for embedding the encrypted
secret image into a cover video. The findings show that this strategy outperformed the
recentsecuritystrategy.
ToimplementtheproposedapproachinReference[134],platformsmaybeusedassensor
nodes, and one of them is the Raspberry Pi. Compared to traditional sensor nodes, these
sensornodesprovidebettercomputationalpower.Thesesensornodescreatetheencrypted
XMLdocumentsbyapplyingthesuggestedalgorithmofencryption.Thealgorithmapplied
for encrypting the contents and features of the specified XML elements must be executed
by the sensor nodes to produce the encrypted XML documents. To do this, they need to
use a secret channel to obtain common parameters, encryption functions, and secret keys
from the server. In this study, Fog computing is used. Fog nodes can execute lightweight
computationalserviceslikeaggregations.XMLfilteringprocessestheXMLstreams,butit
concentratesononestreamatatimeandinfrequentlyhandlesseveralstreamsatonce.More-
over,itproposedamodelthatexpandedtheXMLencryptionstandardtoincludedatastored
insensorsasstringsandnumerictypes.Itefficientlyfilteredthematchedstreamingdataand
performedsummationatFognodes.Italsoperformedfiltrationoperationswithoutdecryp-
tionatFognodes.ThismodelrapidlyprocessednumerousencryptedXMLstreamsproduced
in parallel by sensors without disclosing private information to the subscriber. In another
technique,XMLstreamsweregeneratedbysensors.Toevaluatetheproposedapproach,the
PCenvironmentorRasberryPiplatformwasusedtoimplementtheFognode.Ascompared
toaPC,theRaspberryPicarrieslesscomputingpower,but,still,itsexecutiontimeremains
satisfactory. However, the maximum use of the concurrent XML filters, because of the
limitedcomputationresourcesoftheRaspberryPi,alwaysresultsinresourcecompetition.
TheefficiencywasobtainedbyincreasingthenumberofconcurrentXMLfilters.
Fog computing supports large amounts of stream data generated in IoT scenarios. A new
FOTplatformisintroducedbyReference[135]forhandlingstreamdatainFogcomputing.
It is used in Fog to process and analyze real-time stream data from the IoT. Its main
benefit was to reduce internet usage. Through the detection of changes in data behavior
and the reduction of a huge amount of data transmission over a network infrastructure,
online data modeling can be made possible. The occurrence of such unpredictable and
unexpectedchangesmotivatesthedesignoftheconceptdriftdetectionmethod.Amethod
named Cumulative Sum (CUSUM) is adopted in this study due to its low complexity
computationsandisconsideredtobememoryless.
Reference [136] proposes a five-tier architecture in which the stream data initiating from
variousIoTdevicesismovedtoIoTgatewaysusingvariousprotocols(MQTT,CoAP,Zigbee,
WiMax, etc.) of communication. These gateways perform aggregation of data, and then,
for further processing, they publish it to Fog nodes. A modern and frequently adopted
distributed messaging system called Apache Kafka and a stream processing engine called
ApacheStormarethecomponentsoftheFognodes.
Forsuccessfuldeliveryofmultimediabroadcasts,reliablecontentdelivery,scalability,and
video-streamqualitymustbeensured.Theimprovementsinroutingprotocolsandtopolo-
gies improve reliability, scalability, and the quality of sharing information experiences.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:35
Reference [137] proposes a collaborative routing protocol for video streaming ad hoc
network that is dependent upon cluster architecture, and it uses Fog storage services to
minimizecontentsharing.Thismodelperformsthecalculationofacollaborativegateway
to rank each vehicle with respect to the Gateway Quality Indicator (GQI). Based upon
the values of GQI, a routing table is defined that is built for each vehicle in the cluster
of V2V communication. The vehicle collaboration is executed in the cluster for reducing
the irrelevant data exchange. It is not necessary for all vehicles in a cluster to share the
same live video, because irrelevant information will affect network performance. So, the
algorithm,throughclusterformation,findsthevehiclethathasthebestGQI,andthesame
vehiclebecomesthecollaborativegatewaythatstreamsthevideoviaVehicle-to-Vehicle-
Infrastructure(V2I)communication.Table18summarizesvariousapproachesforstream
datahandlinginFogcomputing.
(3) ConceptDriftHandlinginFogComputing
Machinelearningmodelsthataretrainedonhistoricaldataandbecomeoutofdatefordata
fromtherealworldarereferredtoasexperiencing“drift,”whichisashiftinthestatistical
characteristics of the data. This means that the machine learning models that have been
trainedgraduallydeteriorateandlosetheirabilitytoutilizepatternstomakepredictionsin
thefuture.Thetermdriftcanbeusedasdatadrift,whichisthechangeindatadistribution;
oritcanbeusedasconceptdrift,whichisthechangeintheobjectiveorgoal.Conceptdrift
involves changes over time, requiring models to adapt to maintain accuracy continuously.
The concept drift can be detected using concept drift detectors, sliding windows, online
learners, and ensemble learners. The approaches listed below in Table 19 for managing
conceptdriftareproactive,providingvaluableinsightsthroughadvancedmachinelearning
techniques and optimization strategies. These methods demonstrate effective handling of
concept drift, ensuring models remain accurate and adaptive in dynamic environments.
Reference [147] uses LSTM models for detecting sudden and gradual concept drift in the
clouddomainusingagenetichyper-tuningdriftdetector,leadingtoimprovedperformance
and more efficient resource allocation. Reference [148] handles concept drift within
non-stationary spatiotemporal data streams. BOASWIN, adaptive XGBoost-based model
with the BO-TPE hyperparameter optimization strategy, has become a powerful tool for
spatiotemporal data analytics. This model improves classification accuracy and remains
responsive to continuous and predictable changes in data distribution by dynamically
adjusting window size based on detected drift. Reference [149] proposes a framework for
dynamicstreamingdataanalytics.Inthiswork,patternchangesinthedatastreamsduring
incremental learning are adapted using an optimized adaptive and sliding window
(OASW)thatefficientlymanagesmemoryandtimeconstraints.
ConceptdriftinFogcomputing,causedbydynamicnetworkconditionsandsystemupdates,
alters data distributions over time. This requires models to adapt for accurate predictions.
To present a detailed evaluation of different machine learning and AI models used in Fog
computing to mitigate concept drift, Table 20 highlights the design, implementation, and
critical analysis of each model, emphasizing proactive approaches. This comprehensive
comparisonensuresaclearunderstandingofthestrengthsandlimitationsofeachmethod,
therebyfacilitatingmoreinformeddecisionsintheapplicationofFogcomputingtechnolo-
gies. In the given below different concept drift handling techniques in Fog computing are
mentioned. In Reference [150], Fog-computing-based concept drift detection is combined
with cloud-computing-based process mining. The proposed work actively detects and
responds to concept drift, preprocesses the data locally, and maintains multi-version
processmodels,whichresultsinefficientandtimelyprocessminingformobileapplications.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

| 16:36 |     |     | F.Shariefetal. |     |
| ----- | --- | --- | -------------- | --- |
Table18. StreamDataHandlinginFogComputing
| Technique | ImbalancedKeyPoints | Tools | Parameters | Ref |
| --------- | ------------------- | ----- | ---------- | --- |
Aggregationand No ItprovidesasolutionforFog RaspberryPi Privacy [134]
| filteringmodelon | computingapplicationswhere    | Platform |     |     |
| ---------------- | ----------------------------- | -------- | --- | --- |
| XMLstreams       | maintainingtheprivacyofsensor |          |     |     |
dataisamajorconcern
3-Tierarchitecture No Itminimizeslatency iFogsim,Spyder Latency [128]
| forlatency |     | Editor |     |     |
| ---------- | --- | ------ | --- | --- |
reduction
HS2forreliable No Lowlatency,Lownetwork ApacheFlink, Lowlatency,low [135]
videoStreaming utilization,andnoneedforconstant Spark,H2O networkutilization
internetconnection
Low-power No Thesuggestedmethodenabled Python2.7and Time [138]
| portable       | instantaneousdataanalysisand | Karaken |     |     |
| -------------- | ---------------------------- | ------- | --- | --- |
| metagenomics   | sequencemappingassoonasthe   |         |     |     |
| deviceanalysis | resultswereavailable         |         |     |     |
Architecturefor No Itshowsbetterbehaviorthanits Dockercontainer Time [139]
| trafficmodeling | predecessors,evenwhen     |     |     |     |
| --------------- | ------------------------- | --- | --- | --- |
| andprediction   | connectivityconcernsarose |     |     |     |
services
Anomalydetection No Latency-sensitiveapplicationsmightMicrosoftAzure Timeinuserandkernel [140]
| framework | considerablybenefitfroma         |     | mode,bytesreadand   |     |
| --------- | -------------------------------- | --- | ------------------- | --- |
|           | lightweightframeworkcapableof    |     | writetodisk,iowait, |     |
|           | continuallyandonlineidentifying  |     | bytesread,andwrite  |     |
|           | irregularitiesintheperformanceof |     | likesystemcall      |     |
variousactivities
T3-Scheduler No Theaveragethroughputincreased ApacheStorm Throughput,resource [141]
|     | by25%and12%,respectively,as |     | utilization |     |
| --- | --------------------------- | --- | ----------- | --- |
comparedtothedefaultand
resource-awarescheduling
strategies
Nornira No Itisflexibletoimplementdifferent PARSEC Throughput,latency, [142]
| C++-based | algorithmswithoutexplicitly |     | completiontime,power |     |
| --------- | --------------------------- | --- | -------------------- | --- |
| framework | interactingwithapplications |     | consumption,energy   |     |
Viper No AcommunicationmoduleconnectedApacheStorm Throughput,latency, [143]
|     | withthestreamprocessingengine’s |     | andenergyefficiency |     |
| --- | ------------------------------- | --- | ------------------- | --- |
communicationlayerimproves
parallelthreadcoordinationduring
dataanalysis
Hierarchical No Unlikethreshold-basedtechnique, ApacheStorm ResponseTime [144]
| distributed     | theRL-basedsolutionmayaccount   |     |     |     |
| --------------- | ------------------------------- | --- | --- | --- |
| architecturefor | forvariousQoSmetricsallowingthe |     |     |     |
| elasticDSP      | usertoweightherelativerelevance |     |     |     |
| application     | ofeachmeasure                   |     |     |     |
PiCo:newC++API No ComparedtoSparkandFlink,this ApacheSpark, Throughput,execution [145]
| withafluent | newframeworkcanachieve          | ApacheFlink | time |     |
| ----------- | ------------------------------- | ----------- | ---- | --- |
| interface   | superiorexecutiontimewhileusing |             |      |     |
lessmemory,makingitidealfor
resource-limiteddevices
Edge-Fog-Cloud No Ifeachedge-Fog-cloudresourceis RabitMQ,Cisco - [80]
| Architecture | consideredseparately,thenitwillbeKinetic, |     |     |     |
| ------------ | ----------------------------------------- | --- | --- | --- |
unabletomanagethedatalifecyclesScikit-Multiflow,
|     | ofIoTapplicationswithout | Python, |     |     |
| --- | ------------------------ | ------- | --- | --- |
sacrificingfunctionalityor
performance
Tracingframework No Presentedsolutionswerecapableof ApacheSpark Throughput,processing [146]
|     | tracingwithlesscodingand |     | time |     |
| --- | ------------------------ | --- | ---- | --- |
executiontime
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:37
Table19. ConceptDrift
| AIModel | DesignandImplementation | CriticalAnalysis | Ref |
| ------- | ----------------------- | ---------------- | --- |
LSTMDDisfocusedoncloud Thismodelincorporates Itscomputationalintensityand [147]
ratherthanFogcomputing.It mechanismstohandle therequirementforsufficient
presentsaproactiveapproach non-Gaussiandistributedcloud historicaldatatotrain
tohandlingconceptdriftin dataefficiently.Itisoptimizedto effectivelymightpose
dynamicenvironmentsusing improveperformancein challengesinrapidlychanging
| advancedMLtechniquesand | detectinganomaliesthat     | environments. |     |
| ----------------------- | -------------------------- | ------------- | --- |
| optimizedLSTMmodels.    | manifestasgradualandsudden |               |     |
drifts.
BOASWIN-XGBoost(Bayesian Itusesanoptimizedversionof Thismodeleffectivelyhandles [148]
OptimizedAdaptiveSliding XGBoostforclassification,where sudden,gradual,andrecurring
WindowandXGBoost) theparametersofXGBoostare drifts.Itshowsimproved
proactivelypreparestodetect fine-tunedusingBayesian performanceinclassifying
andhandledriftsbutreactsby Optimizationwitha streamingdatabyadaptingthe
adjustingandretrainingwhen Tree-structuredParzenEstimator windowsizedynamicallybased
| actualchangesaredetected. | (BO-TPE). | onthedriftdetected. |     |
| ------------------------- | --------- | ------------------- | --- |
OptimizedDeeplearningmodel Itallowslowerlatencyindata Benefitofrapidresponseand [149]
andAdaptingslidingwindow processingandquicker localizeddataprocessing,
| technique | adaptationtochangesindata   | limitedcomputational      |     |
| --------- | --------------------------- | ------------------------- | --- |
|           | streams.Thealgorithmdetects | resources.Managingwindow  |     |
|           | changesbycontrollingthesize | sizeandshiftparametersmay |     |
|           | andshiftofthewindow.        | requirefine-tuning        |     |
Table20. ConceptDriftinFog
| AIModel | DesignandImplementation | CriticalAnalysis | Ref |
| ------- | ----------------------- | ---------------- | --- |
A concept drift adapting algo-Conceptdriftdetection Thisintegrationallowsfor [150]
rithm is used to Integrate Fog methodsareusedinthecloud efficientpreprocessingcloseto
computing for accurate log pre-computinglayertohandle thedatasource(fog)androbust,
processing with lower overhead transitionsfromoneversion scalableprocessinginthecloud.
andcloudcomputingforprocess-ofamobileapplicationto Theconceptdriftadaptive
| ingminedlog.                 | another. | algorithmenablesreal-time    |     |
| ---------------------------- | -------- | ---------------------------- | --- |
| Thisapproachactivelyadaptsto |          | updatestoprocessmodels,      |     |
| changes,specifically,concept |          | capturingtheevolvingnatureof |     |
| driftsduetotheevolutionof    |          | mobileappusageand            |     |
| mobileapplications.          |          | operations.                  |     |
ThisapproachusesWavelet Implementedinthe Itreducestheamountofdata [135]
Transformfordata FoT-Streamplatform,which transferredoverthenetworkby
decomposition,allowingthe processesandanalyzesdata focusingonlyonsignificant
captureofessentialfeatures streamsfromIoTdevicesin changes,whichoptimizesboth
whilereducingdataredundancy. real-timewithinthefog computationalresourcesand
Conceptdriftdetectionmethods computinglayer. networkbandwidth.
adapttochangesandoptimize
theuseofnetworkand
computationalresources.
Fog-DeepStreamoffersan ItusesWaveletTransformfor Theeffectivenessandscalability [151]
incrementalapproachto datareduction,ConceptDrift ofthisapproachmayrequire
efficientlymodeldatastreamsin detectionformodelupdates, furthervalidationacrossdiverse
FogComputingenvironments. andintegratingDeepNeural IoTapplicationstoassessits
Thisapproachdetectsand Networksforenhanced practicalutilityandperformance
| adaptstochangesinthedata | systembehavior | incomplexscenarios. |     |
| ------------------------ | -------------- | ------------------- | --- |
| stream,allowingfortimely | understanding. |                     |     |
modelupdatesandpredictions
ofevolvingpatterns.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:38 F.Shariefetal.
Table21. ImbalancedDataStreamalongwithConceptDriftinFogComputing
Technique Imbalanced Keypoints Datasets Parameters Ref
Attentive No InsingleandmultipleFogdrift FGtracedata MeanAbsolute [152]
FederatedLearning scenarios,themodelreducedmean collectedfromIrish Error(MAE)
absoluteerrorsbyroughly20% mobileoperatorin
comparedtothebaselinefederated 2020
averagingapproach.
Fog-computing- No Itsolveslogincompleteness Twogenerated Precision,Recall, [150]
basedconceptdrift problemsandprovidesprocess datasets F1-measure
adaptiveprocess modelevolutionanalysisinthe
mobileapplications.
Conceptdrift No Thereviewandimplementationof ELEC2,Fingrid Meanabsolute [153]
adaptation themostrecentconceptdrift(CD) percentageerror
techniquein detectionmethodswereperformed (MAPE)
distributed fortime-seriesanalysisina
environment distributedenvironment.
DSPLE No TomanageadynamicIoTsystem,it - Accuracy,Kappa [154]
dealswithachangeinstreamdata
behavior.
TabTransformer Yes ThisapproachusesacustomTab UNSW-NB15 Precision,Recall, [131]
Transformerforaddressing F1Score,Support
multi-classimbalanceandachieves
highaccuracy.
Reference [135] reduces the amount of data transmitted on the network, which allows
onlinedatamodelingbydetectingchangesinbehaviorandreductionofinternetusage.The
frameworkproposedinReference[151]continuouslymonitorsdata,efficientlymanagesit,
performs incremental learning, and processes data faster by handling data near its origin
(suchasattheedgeofthenetwork),whichfacilitatestimelyanalyticsanddecision-making.
TheconceptdriftinFogcomputinghasreceivedlittleattention,yetitisstillnecessaryto
address multi-class imbalanced data with concept drift in the future. A few examples of
conceptdriftinFogcomputingaregiveninTable21.
Whiletheresearchonconceptdriftinfogcomputingdoesnotexplicitlyfocusonimbalanced
data,itimplicitlyhandlesimbalanceddatathroughmethodsforadaptingtoconceptdrift.These
approachesoftenaccountforthechangingnatureofdatastreams,whichcanincludeshiftsinclass
distributions,therebyaddressingimbalanceddataindirectly.
Figure5givesanarchitecturediagramthatshowstheoveralldataflowandprocessingstages
involvedinhandlingimbalanceddataacrossIoT,Fog,andcloud.Theprocessesincludedatacol-
lection,preprocessing,detectionofimbalanceddata,conceptdriftdetectionandadaptation,data
transmission,andsubsequentanalysisandvisualization.
5 AnalyticalDiscussion
The researcher suggests using different imbalance correction approaches based on specific sce-
narios in Fog computing environments. It is imperative to customize the choice of solution to
thecharacteristicsofthedataset,theavailablecomputationalresources,andtheobjectivesofthe
application. For instance, undersampling techniques may be more suitable to address the class
imbalance effectively in situations where the dataset is heavily imbalanced with limited compu-
tational resources. However, in scenarios where preserving information from the minority class
iscrucial,oversamplingmethodslikeSMOTEcouldbemorebeneficial.Cost-sensitivetechniques
provevaluablewhenmisclassificationcostsvarybetweenclasses,allowingforamorecustomized
approachtohandlingimbalanceddata.Ensemblemethods,suchascombiningmultipleclassifiers,
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:39
Fig.5. Architecturediagram.
Fig.6. Metricsformulti-class Fig.7. Metricsusedformulti-class Fig. 8. Streamprocessingtoolsin
generalformofdata. datainIoT. fog.
can be effective in scenarios wherea combination of techniquesis neededto improve classifica-
tionperformance.Bycarefullyassessingthespecificneedsofeachscenarioandunderstandingthe
capabilitiesofvariousimbalancecorrectionapproaches,practitionerscanmakewell-informedde-
cisions when selecting the most suitable solution to enhance data processing in Fog computing
environments. The data is primarily categorized into batch and stream data. Theresearcherhas
analyzedthecurrentbinaryandmulti-classimbalanceddatahandlingapproachesforthesetwo
typesofdata.Theimbalanceddataprocessingcategoriesalongwithconceptdrift,theircontribu-
tions,thetoolsused,andthemetricsemployedinthesestudiesprovidethebasisfortheanalytical
investigation.Figure5displaystheevaluationmetricsthatareadoptedinafewrecentpiecesof
researchonmulti-classimbalancedbatchdata.ThemostpopularmetricMAUCisusedin23%of
the study; 12% P-min, 12% P-avg, 11% AUC, 6% MFM, 6% MAcc, 6% G-mean, 6% F-measure, 6%
Recall,6%AvgAcc,and6%probabilisticAUC.
Figure 6 shows that the accuracy is 22% in the metrics that are used in multi-class IoT. Other
metricsincluderecall9%,falsealarmrate9%,f1-measure9%,Precision4%,f-measure4%,G-mean
4%,Kappa4%,Macroprecision4%,macrorecall4%,macro-f1-score4%,ROC-AUC4%,sensitivity
4%,speed4%,andtimeoverhead4%.
Figure 7 displays an Apache Storm that covers up to 17% of the area. The other tools include
ApacheSpark(11%),Python(11%),andC++-basedframeworks(11%).Theremainingtoolsinclude
Microsoft Azure (6%), Occam (6%), Python (6%), RabitMQ (6%), RaspberryPi (6%), Spyder editor
(6%), Apache Flink (5%), Docker container (5%), H2O (5%), and iFogsim (5%). For the measures
listedinFigure8thatareusedforconceptdrifthandling,accuracyis24%.G-meanis15%,recallis
13%,precisionis11%,f-measureis11%,PMAUCis4%,andeachonefromtheremainingmetrics
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:40 F.Shariefetal.
Fig.9. Metricsusedforconceptdrifthandling. Fig.10. Softwaretoolsusedforconceptdrifthandling.
occupies2%area,accordingtotheliterature.Additionally,36%ofconceptdrifthandlingwasdone
usingtheMOAsimulator,18%wasdonebyusingScikit,14%byusingJava,14%byusingPython,
5%byusingWeka3.4.2,5%byusingNetlogo,4%byusingtheDeepLearningToolbox,and4%was
donebyusingApacheStorm,asshowninFigure9.
6 LessonsLearnedfromSurvey
Followingarethelessonslearnedfromthesurveythatismentionedabove:AMDOtechniqueis
thebettersolutionformulti-classhybridimbalanceddatasets.Thecombinedapproachgenerates
betterresultsthantheindividualoversamplingorundersamplingtechniques.
Theimbalancedclassproblemisnottheonlyaspectaffectingtheperformanceoftheprediction
model.Duetotheirhighprocessingcost,high-dimensionalitydatasetshaveanimpactonperfor-
manceprediction.Byremovingtheuselessfeatures,afewfeaturereduction-basedclassification
modelshavebeenpresented[51].
Inconceptdriftissues,thedynamicintegrationhasalwaysbeensuperiortothebestbaseclas-
sifierandweightedvoting,despitewindowshiftorwindowsize,andthelearningalgorithm.
Naive Bayes is mostly used as a prediction algorithm in retraining a model because of two
reasons[60]:
—First,incrementallearningisused,allowingthepredictionmodeltobeupdatedincremen-
tally.
—Second, the computational complexity of Naive Bayes is rather low against the other
methodsofmachinelearning.
Onlinealgorithmsorincrementallearningarethemostappropriateandpreferablemethodsfor
learningfrommassiveamountsofdatathatarebeingprocessedinsequentialsteps[155].
Althoughincrementallearningreducescomplexitybysimplifyingtheoverallprocessthrough
updatingthemodelwithnewdatawithoutretrainingfromscratch,onlyafewmachinelearning
methods (Naive Bayes, Neural Networks, and Hoeffding Trees) are capable of performing these
incrementalupdates.Moreover,theseincrementalupdatesofmodelsareunabletoreacttorapid
changesthathappenduringtheconceptdrifts.
Thebulkofstreamingdataclassificationalgorithmsiseitherrules-basedortree-basedtoclassify
data.Ensemble,nearestneighbor,andstatisticaltechniquesareusedinthedevelopmentofvery
fewalgorithms.Thesefindingsshowthatthereisstillspaceforresearchinthisfield,astheper-
formanceofprobabilityandmachinelearning–basedcategorizationalgorithmsonstreamingdata
remainsanopenresearchsubject[156].Thissurveydiscussescomputationalscalabilityinthecon-
textofFogcomputingforhandlingimbalanceddatastreams.Itexploresthechallengesrelatedto
computationalscalabilityandemphasizestheneedforlightweighttechniquestoaddresstheseis-
sueseffectively.Specifically,thesurveymentionstheimportanceofcombiningretraininglearning
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:41
with incremental learning in Fog nodes using lightweight techniquesto enhance computational
scalability.Additionally,thesurveyhighlightstheconstraintsonmemory,power,communication,
and processing in Fog nodes, underscoring the significance of developing mechanisms that can
handleimbalanceddatastreamsefficientlywhileensuringcomputationalscalability.
7 ChallengesandFutureDirections
The major factors that are covered in this section are open questions, upcoming difficulties,
and future research prospects for handling imbalanced data in Fog computing. The handling of
multi-class imbalanced data streams on Fog nodes is a challenge due to constraints in memory,
power,communication,andprocessing.Alotoftimeisrequiredforthecomputationsperformed
by resource-constrained devices at the edge. It is necessary to have a mechanism for handling
imbalanced data streams that frequently update instances and forecasts unique as well as recur-
ring classes. Investigating deep reinforcement learning and generative adversarial networks
(GANs), developing real-time lightweight and Automated Machine Learning (AutoML)
systems for streaming data are required for handling concept drift and imbalanced data in Fog
computing environments. Additionally, federated learning techniques, in which models are
trained locally and then aggregated on a regular basis, may be used to create a robust global
modelthatcanadapttonewdataandconceptdriftefficiently.Optimizetheperformanceoffog
computing systems by integrating edge AI and federated learning techniques to minimize data
transferandenhancelocalprocessingcapabilities.Transferlearningandcross-domainadaptation
needtobehandled,ensuringthatmodelstrainedinonedomaincanbeusedinanother,especially
whentherearepatternsorfeaturessharedbydatastreamsfromdifferentdomain.Explorehybrid
approaches that combine data-level techniques with algorithm-level solutions to improve the
robustness and accuracy of models in Fog computing. Implement hybrid Edge-Fog-Cloud archi-
tecturesthatleveragethestrengthsofeachlayerforoptimizeddataprocessingandconceptdrift
management.
Tohandlemulti-classimbalanceddataandconceptdriftinFognodes,developalgorithmsthat
detectoutliersandminimizetheirimpact.Useprivacy-preservingtechniquestomanagedatawith-
outcompromisingconfidentiality.Combineincrementallearning,whichupdatesmodelsquickly,
withretrainingtoadapttosuddenconceptdrift.Thisapproachoptimizesperformancedespitelim-
itedresources.Addressingthesechallengescollectivelywillimprovedataprocessinganddecision-
makinginFogenvironments.
8 Conclusion
AFogcomputingandIoTnetwork’sperformancecanbeconsiderablyenhancedbyeffectivebatch
andstreamdataprocessingapproaches.NostudyhasbeenidentifiedinFogcomputingonhowto
handleunevendatastreams,butasignificantamountofworkhasalreadybeendonewithbatch
data. In this article, the researchers investigated the recent imbalanced data handling methods
for processing batch and stream data in WSN, IoT networks, and Fog computing. Binary and
multi-classimbalanceddataarefurthersubcategoriesofbothtypes(batchandstreamdata)ofdata.
Resampling, algorithmic, cost-sensitive, and ensemble are the four broad categories into which
the various approaches are divided to treat imbalanced data. The present study has described
the methodologies, their contributions, performance metrics, and tools of every approach. The
analysisshowsthat,althoughensemblelearningisthepreferredstrategy,mostresearchershave
used resampling strategies. The research results show that in 23% of the study, the MAUC was
usedasapopularmetricforhandlingmulti-classimbalanceddata.InthecaseofIoTnetwork,22%
ofthestudiesusedtheaccuracymetricforhandlingmulti-classimbalanceddata,andtheresearch
related to the assessment environment for concept drift reveals that accuracy was employed as
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:42 F.Shariefetal.
acommonperformancemetricforconceptdrifthandlingin24%ofthestudies,while36%ofthe
studiesusedtheMOAasanoptimizationtoolforconceptdrifthandling.Moreover,thecommonly
usedtoolforstreamprocessinginFogwasApacheStorm,whichcovered17%ofthearea.These
findingscanbeusedforfurtherresearchworks.
References
[1] ShaikMasthanBabu,A.JayaLakshmi,andB.ThirumalaRao.2015.AstudyoncloudbasedInternetofThings:
CloudIoT.InGlobalConferenceonCommunicationTechnologies(GCCT’15).IEEE,60–65.
[2] BushraJamil,HumairaIjaz,MohammadShojafar,KashifMunir,andRajkumarBuyya.2022.Resourceallocation
andtaskschedulinginfogcomputingandinternetofeverythingenvironments:Ataxonomy,review,andfuture
directions.ACMComputingSurveys(CSUR)54,11s(2022),1–38.
[3] EnkhturTsogbaatar,MonowarH.Bhuyan,YuzoTaenaka,DoudouFall,KhishigjargalGonchigsumlaa,ErikElmroth,
andYoukiKadobayashi.2021.DeL-IoT:AdeepensemblelearningapproachtouncoveranomaliesinIoT.Internet
Things14(2021),100391.
[4] A.Jaokar.2016.DataScienceforInternetofThings(IoT):TenDifferencesFromTraditionalDataScience.KDnuggets.
[5] D.Friedman.2015.DataScienceforInternetofThings(IoT):TenDifferencesFromTraditionalDataScience.ReadWrite.
https://readwrite.com/five-types-data-internet-of-things/
[6] AlessioBotta,WalterDeDonato,ValerioPersico,andAntonioPescapé.2016.Integrationofcloudcomputingand
InternetofThings:Asurvey.Fut.Gen.Comput.Syst.56(2016),684–700.
[7] FlavioBonomi,RodolfoMilito,JiangZhu,andSateeshAddepalli.2012.FogcomputinganditsroleintheInternetof
Things.In1stEditionoftheMCCWorkshoponMobileCloudComputing.13–16.
[8] P.PunithaIlayaraniandM.MariaDominic.2019.Anatomizationoffogcomputingandedgecomputing.InIEEE
InternationalConferenceonElectrical,ComputerandCommunicationTechnologies(ICECCT’19).IEEE,1–6.
[9] SwatiMalikandKamaliGupta.2019.Resourceschedulinginfog:Taxonomyandrelatedaspects.J.Comput.Theoret.
Nanosci.16,10(2019),4313–4319.
[10] AparnaKumari,SudeepTanwar,SudhanshuTyagi,NeerajKumar,RezaM.Parizi,andKim-KwangRaymondChoo.
2019.Fogdataanalytics:Ataxonomyandprocessmodel.J.Netw.Comput.Applic.128(2019),90–104.
[11] RicardoBarandela,JoséSalvadorSánchez,VicenteGarcıa,andEdgarRangel.2003.Strategiesforlearninginclass
imbalanceproblems.PatternRecog.36,3(2003),849–851.
[12] PattaramonVuttipittayamongkolandEyadElyan.2020.Neighbourhood-basedundersamplingapproachforhan-
dlingimbalancedandoverlappeddata.Inf.Sci.509(2020),47–70.
[13] SilviaCateni,ValentinaColla,andMarcoVannucci.2014.Amethodforresamplingimbalanceddatasetsinbinary
classificationtasksforreal-worldproblems.Neurocomputing135(2014),32–41.
[14] Wei-ChaoLin,Chih-FongTsai,Ya-HanHu,andJing-ShangJhang.2017.Clustering-basedundersamplinginclass-
imbalanceddata.Inf.Sci.409(2017),17–26.
[15] DebashreeDevi,SuyelNamasudra,andSeifedineKadry.2020.Aboosting-aidedadaptivecluster-basedundersam-
plingapproachfortreatmentofclassimbalanceproblem.Int.J.DataWarehous.Min.16,3(2020),60–86.
[16] JoséAntonioSanz,DarioBernardo,FranciscoHerrera,HumbertoBustince,andHaniHagras.2014.Acompactevolu-
tionaryinterval-valuedfuzzyrule-basedclassificationsystemforthemodelingandpredictionofreal-worldfinancial
applicationswithimbalanceddata.IEEETrans.FuzzySyst.23,4(2014),973–990.
[17] GeorgiosDouzas,FernandoBacao,andFelixLast.2018.Improvingimbalancedlearningthroughaheuristicover-
samplingmethodbasedonk-meansandSMOTE.Inf.Sci.465(2018),1–20.
[18] LinaGong,ShujuanJiang,andLiJiang.2019.Tacklingclassimbalanceprobleminsoftwaredefectpredictionthrough
cluster-basedover-samplingwithfiltering.IEEEAccess7(2019),145725–145737.
[19] GyörgyKovács.2019.Anempiricalcomparisonandevaluationofminorityoversamplingtechniquesonalarge
numberofimbalanceddatasets.Appl.SoftComput.83(2019),105662.
[20] DechThammasiri,DursunDelen,PhayungMeesad,andNihatKasap.2014.Acriticalassessmentofimbalanced
class distribution problem: The case of predicting freshmen student attrition. Expert Syst. Applic. 41, 2 (2014),
321–330.
[21] PinLim,ChiKeongGoh,andKayChenTan.2016.Evolutionarycluster-basedsyntheticoversamplingensemble
(eco-ensemble)forimbalancelearning.IEEETrans.Cybern.47,9(2016),2850–2861.
[22] GyörgyKovács.2019.Smote-variants:APythonimplementationof85minorityoversamplingtechniques.Neuro-
computing366(2019),352–354.
[23] Dong-ShengCao,Qing-SongXu,Yi-ZengLiang,Liang-XiaoZhang,andHong-DongLi.2010.Theboosting:Anew
ideaofbuildingmodels.Chemomet.Intell.Lab.Syst.100,1(2010),1–11.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:43
[24] You-ShyangChen.2016.Anempiricalstudyofahybridimbalanced-classDT-RSTclassificationproceduretoeluci-
datetherapeuticeffectsinuremiapatients.Med.Biol.Eng.Comput.54,6(2016),983–1001.
[25] SobhanSarkar,NikhilKhatedi,AnimaPramanik,andJ.Maiti.2020.Anensemblelearning-basedundersampling
techniqueforhandlingclass-imbalanceproblem.InInternationalConferenceonEmergingTrendsinInformationTech-
nology(ICETIT’19).Springer,586–595.
[26] GuoHaixiang,LiYijing,JenniferShang,GuMingyun,HuangYuanyue,andGongBing.2017.Learningfromclass-
imbalanceddata:Reviewofmethodsandapplications.ExpertSyst.Applic.73(2017),220–239.
[27] HengyiWei,BaochengSun,andMingmingJing.2014.BalancedBoost:Ahybridapproachforreal-timenetwork
trafficclassification.In23rdInternationalConferenceonComputerCommunicationandNetworks(ICCCN’14).IEEE,
1–6.
[28] José F. Díez-Pastor, Juan J. Rodríguez, Cesar Garcia-Osorio, and Ludmila I. Kuncheva. 2015. Random balance:
Ensemblesofvariablepriorsclassifiersforimbalanceddata.Knowl.-basedSyst.85(2015),96–111.
[29] LaraLusaandothers.2017.Gradientboostingforhigh-dimensionalpredictionofrareevents.ComputationalStatistics
&DataAnalysis113(2017),19–37.
[30] SarahVluymans,IsaacTriguero,ChrisCornelis,andYvanSaeys.2016.EPRENNID:Anevolutionaryprototypere-
ductionbasedensemblefornearestneighborclassificationofimbalanceddata.Neurocomputing216(2016),596–610.
[31] SergioGónzalez,SalvadorGarcía,MarcelinoLázaro,AníbalR.Figueiras-Vidal,andFranciscoHerrera.2017.Class
switchingaccordingtonearestenemydistanceforlearningfromhighlyimbalanceddata-sets.PatternRecog.70
(2017),12–24.
[32] DanGan,JiangShen,BangAn,ManXu,andNaLiu.2020.IntegratingTANBNwithcostsensitiveclassification
algorithmforimbalanceddatainmedicaldiagnosis.Comput.Industr.Eng.140(2020),106266.
[33] SalmanH.Khan,MunawarHayat,MohammedBennamoun,FerdousA.Sohel,andRobertoTogneri.2017.Cost-
sensitivelearningofdeepfeaturerepresentationsfromimbalanceddata.IEEETrans.NeuralNetw.Learn.Syst.29,8
(2017),3573–3587.
[34] ChongZhang,KayChenTan,andRuoxuRen.2016.Trainingcost-sensitivedeepbeliefnetworksonimbalancedata
problems.InInternationalJointConferenceonNeuralNetworks(IJCNN’16).IEEE,4362–4367.
[35] ChongZhang,KayChenTan,HaizhouLi,andGeokSoonHong.2018.Acost-sensitivedeepbeliefnetworkfor
imbalancedclassification.IEEETrans.NeuralNetw.Learn.Syst.30,1(2018),109–122.
[36] WeijieZhengandHongZhao.2020.Cost-sensitivehierarchicalclassificationforimbalanceclasses.Appl.Intell.50,
8(2020),2328–2338.
[37] VictoriaLópez,AlbertoFernández,MaríaJoséDelJesus,andFranciscoHerrera.2013.Ahierarchicalgeneticfuzzy
systembasedongeneticprogrammingforaddressingclassificationwithhighlyimbalancedandborderlinedata-sets.
Knowl.-basedSyst.38(2013),85–104.
[38] Harshita Patel and Ghanshyam Singh Thakur. 2017. Classification of imbalanced data using a modified fuzzy-
neighborweightedapproach.Int.J.Intell.Eng.Syst.10,1(2017),56–64.
[39] HarshitaPatelandG.S.Thakur.2019.Animprovedfuzzyk-nearestneighboralgorithmforimbalanceddatausing
adaptiveapproach.IETEJ.Res.65,6(2019),780–789.
[40] MaedeZolanvari,MarcioA.Teixeira,andRajJain.2018.EffectofimbalanceddatasetsonsecurityofindustrialIoT
usingmachinelearning.InIEEEInternationalConferenceonIntelligenceandSecurityInformatics(ISI’18).IEEE,112–
117.
[41] AlbertoFernández,MaríaJoséDelJesus,andFranciscoHerrera.2010.Multi-classimbalanceddata-setswithlinguis-
ticfuzzyrulebasedclassificationsystemsbasedonpairwiselearning.InInternationalConferenceonInformation
ProcessingandManagementofUncertaintyinKnowledge-basedSystems.Springer,89–98.
[42] XuebingYang,QiumingKuang,WenshengZhang,andGuopingZhang.2017.AMDO:Anover-samplingtechnique
formulti-classimbalancedproblems.IEEETrans.Knowl.DataEng.30,9(2017),1672–1685.
[43] ZhongliangZhang,BartoszKrawczyk,SalvadorGarcia,AlejandroRosales-Pérez,andFranciscoHerrera.2016.Em-
poweringone-vs-onedecompositionwithensemblelearningformulti-classimbalanceddata.Knowl.-basedSyst.106
(2016),251–263.
[44] QianmuLi,YanjunSong,JingZhang,andVictorS.Sheng.2020.Multiclassimbalancedlearningwithone-versus-one
decompositionandspectralclustering.ExpertSyst.Applic.147(2020),113152.
[45] NutthapornJunsomboonandTanasaneePhienthrakul.2017.Combiningover-samplingandunder-samplingtech-
niquesforimbalancedataset.In9thInternationalConferenceonMachineLearningandComputing.243–247.
[46] NiteshV.Chawla,KevinW.Bowyer,LawrenceO.Hall,andW.PhilipKegelmeyer.2002.SMOTE:Syntheticminority
over-samplingtechnique.J.Arti.Intell.Res.16(2002),321–357.
[47] BarnanDas,NarayananC.Krishnan,andDianeJ.Cook.2014.RACOGandwRACOG:Twoprobabilisticoversam-
plingtechniques.IEEETrans.Knowl.DataEng.27,1(2014),222–234.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:44 F.Shariefetal.
[48] LidaAbdiandSattarHashemi.2015.Tocombatmulti-classimbalancedproblemsbymeansofover-samplingtech-
niques.IEEETrans.Knowl.DataEng.28,1(2015),238–251.
[49] Show-JaneYenandYue-ShiLee.2009.Cluster-basedunder-samplingapproachesforimbalanceddatadistributions.
ExpertSyst.Applic.36,3(2009),5718–5727.
[50] HuLi,PengZou,XiangWang,andRongzeXia.2013.Anewcombinationsamplingmethodforimbalanceddata.In
ChineseIntelligentAutomationConference.Springer,547–554.
[51] AliArshad,SamanRiaz,andLichengJiao.2019.Semi-superviseddeepfuzzyC-meanclusteringforimbalancedmulti-
classclassification.IEEEAccess7(2019),28100–28112.
[52] TanapolKosolwattana,ChenangLiu,RenjieHu,ShizhongHan,HuaChen,andYingLin.2023.Aself-inspected
adaptiveSMOTEalgorithm(SASMOTE)forhighlyimbalanceddataclassificationinhealthcare.BioDataMin.16,1
(2023),15.
[53] MasoumehSoleimaniandAkramSadatMirshahzadeh.2023.Multi-classclassificationofimbalancedintelligentdata
usingdeepneuralnetwork.EAIEndors.Trans.AIRobot.2(2023).
[54] SukarnaBarua,MdMonirulIslam,andKazuyukiMurase.2015.GOS-IL:Ageneralizedover-samplingbasedonline
imbalancedlearningframework.InNeuralInformationProcessing:22ndInternationalConference,ICONIP2015,Istan-
bul,Turkey,November9-12,2015,Proceedings,PartI22.Springer,680–687.
[55] ShuoWang,LeandroL.Minku,andXinYao.2016.Dealingwithmultipleclassesinonlineclassimbalancelearning.
InInternationalJointConferenceonArtificialIntelligence(IJCAI’16).2118–2124.
[56] TahseenAl-Khateeb,MohammadM.Masud,KhaledM.Al-Naami,SadiEvrenSeker,AhmadM.Mustafa,Latifur
Khan,ZouheirTrabelsi,CharuAggarwal,andJiaweiHan.2015.Recurringandnovelclassdetectionusingclass-
basedensembleforevolvingdatastream.IEEETrans.Knowl.DataEng.28,10(2015),2752–2764.
[57] ZahraaS.Abdallah,MohamedMedhatGaber,BalaSrinivasan,andShonaliKrishnaswamy.2016.AnyNovel:Detec-
tionofnovelconceptsinevolvingdatastreams.Evolv.Syst.7,2(2016),73–93.
[58] AhmadM.Mustafa,GbadeboAyoade,KhaledAl-Naami,LatifurKhan,KevinW.Hamlen,BhavaniThuraisingham,
andFredericoAraujo.2017.Unsuperviseddeepembeddingfornovelclassdetectionoverdatastream.InIEEEInter-
nationalConferenceonBigData(BigData’17).IEEE,1830–1839.
[59] ImenKhamassi,MoamarSayed-Mouchaweh,MoezHammami,andKhaledGhédira.2018.Discussionandreviewon
evolvingdatastreamsandconceptdriftadapting.Evolv.Syst.9,1(2018),1–23.
[60] LucasBaier,JosuaReimold,andNiklasKühl.2020.Handlingconceptdriftforpredictionsinbusinessprocessmining.
InIEEE22ndConferenceonBusinessInformatics(CBI’20).IEEE,76–83.
[61] ManzoorAhmedHashmani,SyedMuslimJameel,MobasharRehman,andAtsushiInoue.2020.Conceptdriftevo-
lutioninmachinelearningapproaches:Asystematicliteraturereview.Int.J.SmartSens.Intell.Syst.13,1(2020),
1.
[62] ShengChenandHaiboHe.2009.SERA:Selectivelyrecursiveapproachtowardsnonstationaryimbalancedstream
datamining.InInternationalJointConferenceonNeuralNetworks.IEEE,522–529.
[63] FarnazSadeghiandHernaL.Viktor.2021.Online-MC-queue:Learningfromimbalancedmulti-classstreams.In3rd
InternationalWorkshoponLearningwithImbalancedDomains:TheoryandApplications.PMLR,21–34.
[64] ShuoWang,LeandroL.Minku,andXinYao.2018.Asystematicstudyofonlineclassimbalancelearningwithconcept
drift.IEEETrans.NeuralNetw.Learn.Syst.29,10(2018),4802–4821.
[65] S.PriyaandR.AnnieUthra.2021.RETRACTEDARTICLE:Comprehensiveanalysisforclassimbalancedatawith
conceptdriftusingensemblebasedclassification.J.Amb.Intell.Human.Comput.12,5(2021),4943–4956.
[66] RobertoS.M.Barros,DaniloR.L.Cabral,PauloM.GonçalvesJr,andSilasG.T.C.Santos.2017.RDDM:Reactive
driftdetectionmethod.ExpertSyst.Applic.90(2017),344–355.
[67] RobertoSoutoMaiorBarrosandSilasGarridoT.CarvalhoSantos.2018.Alarge-scalecomparisonofconceptdrift
detectors.Inf.Sci.451(2018),348–370.
[68] TegjyotSinghSethiandMehmedKantardzic.2018.Handlingadversarialconceptdriftinstreamingdata.ExpertSyst.
Applic.97(2018),18–40.
[69] MoritzHeusinger,ChristophRaab,andFrank-MichaelSchleif.2022.Passiveconceptdrifthandlingviavariationsof
learningvectorquantization.NeuralComputingandApplications34,1(2022),89–100.
[70] ArifBudiman,MohamadIvanFanany,andChanBasaruddin.2016.AdaptiveconvolutionalELMforconceptdrift
handlinginonlinestreamdata.arXivpreprintarXiv:1610.02348(2016).
[71] TaoPeng,SanaSellami,andOmarBoucelma.2019.IoTdataimputationwithincrementalmultiplelinearregression.
OpenJ.InternetThings5,1(2019),69–79.
[72] ShuoWangandLeandroL.Minku.2020.AUCestimationandconceptdriftdetectionforimbalanceddatastreams
withmultipleclasses.InInternationalJointConferenceonNeuralNetworks(IJCNN’20).IEEE,1–8.
[73] ŁukaszKoryckiandBartoszKrawczyk.2021.Conceptdriftdetectionfrommulti-classimbalanceddatastreams.In
IEEE37thInternationalConferenceonDataEngineering(ICDE’21).IEEE,1068–1079.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:45
[74] S.AncyandD.Paulraj.2020.Handlingimbalanceddatawithconceptdriftbyapplyingdynamicsamplinganden-
sembleclassificationmodel.ComputerCommunications153(2020),553–560.
[75] ZengLi,WenchaoHuang,YanXiong,SiqiRen,andTuanfeiZhu.2020.Incrementallearningimbalanceddatastreams
withconceptdrift:Thedynamicupdatedensemblealgorithm.Knowl.-basedSyst.195(2020),105694.
[76] DariuszBrzezinski,LeandroL.Minku,TomaszPewinski,JerzyStefanowski,andArturSzumaczuk.2021.Theimpact
ofdatadifficultyfactorsonclassificationofimbalancedandconceptdriftingdatastreams.Knowl.Inf.Syst.63,6
(2021),1429–1469.
[77] GregoryDitzlerandRobiPolikar.2012.Incrementallearningofconceptdriftfromstreamingimbalanceddata.IEEE
Trans.Knowl.DataEng.25,10(2012),2283–2301.
[78] JingGao,WeiFan,JiaweiHan,andPhilipS.Yu.2007.Ageneralframeworkforminingconcept-driftingdatastreams
withskeweddistributions.InSiamInternationalConferenceonDataMining.SIAM,3–14.
[79] JosephineAkosa.2017.Predictiveaccuracy:Amisleadingperformancemeasureforhighlyimbalanceddata.InSAS
GlobalForum.
[80] HungCaoandMonicaWachowicz.2019.Anedge-fog-cloudarchitectureofstreaminganalyticsforInternetofThings
applications.Sensors19,16(2019),3594.
[81] MercedesE.Paoletti,OscarMogollon-Gutierrez,SergioMoreno-Álvarez,JoseCarlosSancho,andJuanM.Haut.
2023.Acomprehensivesurveyofimbalancecorrectiontechniquesforhyperspectraldataclassification.IEEEJournal
ofSelectedTopicsinAppliedEarthObservationsandRemoteSensing16(2023),5297–5314.
[82] DebashreeDevi,SarojK.Biswas,andBiswajitPurkayastha.2020.Areviewonsolutiontoclassimbalanceproblem:
Undersamplingapproaches.InInternationalConferenceonComputationalPerformanceEvaluation(ComPE’20).IEEE,
626–631.
[83] SanchitaPandeyandKuldeepKumar.2023.Softwarefaultpredictionforimbalanceddata:Asurveyonrecentdevel-
opments.Proced.Comput.Sci.218(2023),1815–1824.
[84] AbhisarSharma,AnuradhaPurohit,andHimaniMishra.2021.Asurveyonimbalanceddatahandlingtechniques
forclassification.Int.J.Emerg.TrendsEng.Res.9,10(2021).
[85] ShaikJohnyBasha,SrinivasaRaoMadala,KollaVivek,EedupalliSaiKumar,andTammininaAmmannamma.2022.A
reviewonimbalanceddataclassificationtechniques.InInternationalConferenceonAdvancedComputingTechnologies
andApplications(ICACTA’22).IEEE,1–6.
[86] MeghaAshokPatil,SunilKumar,SandeepKumar,andMuskanGarg.2021.Conceptdriftdetectionforsocialme-
dia:Asurvey.In3rdInternationalConferenceonAdvancesinComputing,CommunicationControlandNetworking
(ICAC3N’21).IEEE,12–16.
[87] MengHan,ZhiqiangChen,MuhangLi,HongxinWu,andXilongZhang.2022.Asurveyofactiveandpassiveconcept
drifthandlingmethods.Comput.Intell.38,4(2022),1492–1535.
[88] JiguoYu,YingyingQi,GuanghuiWang,andXinGu.2012.Acluster-basedroutingprotocolforwirelesssensor
networkswithnonuniformnodedistribution.AEU-Int.J.Electron.Commun.66,1(2012),54–61.
[89] NawelYala,BelkacemFergani,LaurentClavier,andothers.2014.SoftmarginSVMmodelingforhandlingimbalanced
humanactivitydatasetsinmultiplehomes.In2014InternationalConferenceonMultimediaComputingandSystems
(ICMCS).IEEE,421–426.
[90] HongZhouandKun-MingYu.2017.Imbalanceddataclassificationfordefectiveproductpredictionbasedonin-
dustrialwirelesssensornetwork.In6thInternationalConferenceonFutureGenerationCommunicationTechnologies
(FGCT’17).IEEE,1–6.
[91] HangYang,SimonFong,RaymondWong,andGuangminSun.2013.Optimizingclassificationdecisiontreesbyusing
weightednaïveBayespredictorstoreducetheimbalancedclassprobleminwirelesssensornetwork.Int.J.Distrib.
SensorNetw.9,1(2013),460641.
[92] HarshitaPatel,DharmendraSinghRajput,G.ThippaReddy,CelestineIwendi,AliKashifBashir,andOhyunJo.2020.
Areviewonclassificationofimbalanceddataforwirelesssensornetworks.Int.J.Distrib.SensorNetw.16,4(2020),
1550147720916404.
[93] SireeshaRoddaandUmaShankarRaoErothi.2016.Classimbalanceprobleminthenetworkintrusiondetection
systems.InInternationalConferenceonElectrical,Electronics,andOptimizationTechniques(ICEEOT’16).IEEE,2685–
2688.
[94] SitaramAsurandSrinivasanParthasarathy.2007.Correlation-basedfeaturepartitioningforrareeventdetectionin
wirelesssensornetworks.In1stInternationalWorkshoponKnowledgeDiscoveryfromSensorData(Sensor-KDD’07).
[95] B.AbidineM’hamedandBelkacemFergani.2014.Anewmulti-classWSVMclassificationtoimbalancedhuman
activitydataset.J.Comput.9,7(2014),1560–1565.
[96] YujingChen,ZhengChai,YueCheng,andHuzefaRangwala.2021.Asynchronousfederatedlearningforsensordata
withconceptdrift.InIEEEInternationalConferenceonBigData(BigData’21).IEEE,4822–4831.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:46 F.Shariefetal.
[97] ShenglanLiu,LinFeng,JunWu,GangHou,andGuangjieHan.2017.Conceptdriftdetectionfordatastreamlearning
basedonangleoptimizedglobalembeddingandprincipalcomponentanalysisinsensornetworks.Comput.Electric.
Eng.58(2017),327–336.
[98] EvangelosBagkis,TheodosiosKassandros,andKostasKaratzas.2022.Learningcalibrationfunctionsonthefly:Hy-
bridbatchonlinestackingensemblesforthecalibrationoflow-costairqualitysensornetworksinthepresenceof
conceptdrift.Atmosphere13,3(2022),416.
[99] Swaraj Dube, Wong Yee Wan, and Hermawan Nugroho. 2021. A novel approach of IoT stream sampling and
modelupdateontheIoTedgedeviceforclassincrementallearninginanedge-cloudsystem.IEEEAccess9(2021),
29180–29199.
[100] AkbarTelikaniandAmirH.Gandomi.2021.Cost-sensitivestackedauto-encodersforintrusiondetectioninthe
InternetofThings.InternetThings14(2021),100122.
[101] BharathSudharsan,JohnG.Breslin,andMuhammadIntizarAli.2021.Imbal-OL:Onlinemachinelearningfrom
imbalanced data streams in real-world IoT. In IEEE International Conference on Big Data (Big Data’21). IEEE,
4974–4978.
[102] GauravMohindru,KoushikMondal,andHaiderBanka.2021.Differenthybridmachineintelligencetechniquesfor
handlingIoT-basedimbalanceddata.CAAITrans.Intell.Technol.6,4(2021),405–416.
[103] RazanAbdulhammed,MiadFaezipour,AbdelshakourAbuzneid,andArafatAbuMallouh.2018.Deepandmachine
learningapproachesforanomaly-basedintrusiondetectionofimbalancednetworktraffic.IEEESensorsLett.3,1
(2018),1–4.
[104] MohamedAmineFerrag,LeandrosMaglaras,AhmedAhmim,MakhloufDerdour,andHelgeJanicke.2020.RDTIDS:
Rules and decision tree-based intrusion detection system for internet-of-things networks. Fut. Internet 12, 3
(2020),44.
[105] JooHwaLeeandKeeHyunPark.2021.GAN-basedimbalanceddataintrusiondetectionsystem.Person.Ubiq.Comput.
25,1(2021),121–128.
[106] Chun-ChengLin,Der-JiunnDeng,Chin-HungKuo,andLinnanChen.2019.Conceptdriftdetectionandadaption
inbigimbalanceindustrialIoTdatausinganensemblelearningmethodofofflineclassifiers.IEEEAccess7(2019),
56198–56207.
[107] SikhaBaguiandKunqiLi.2021.Resamplingimbalanceddatafornetworkintrusiondetectiondatasets.J.BigData8,
1(2021),1–41.
[108] PanditByomakeshaDash,JanmenjoyNayak,BighnarajNaik,EtuariOram,andS.K.HafizulIslam.2020.Model
basedIoTsecurityframeworkusingmulticlassadaptiveboostingwithSMOTE.Secur.Privac.3,5(2020),e112.
[109] PankajKumarKeserwani,MaheshChandraGovil,EmmanuelS.Pilli,andPrajjvalGovil.2021.Asmartanomaly-
basedintrusiondetectionsystemfortheInternetofThings(IoT)networkusingGWO–PSO–RFmodel.J.Reliab.
Intell.Environ.7,1(2021),3–21.
[110] MashaalA.AlfhaidandManalA.Abdullah.2022.ICSM:Imbalancedchunk-basedstreammodel.Int.J.Innov.,Creativ.
Change16(2022).
[111] VinayArora,RohanSinghLeekha,KyungroulLee,andAmanKataria.2020.Facilitatinguserauthorizationfrom
imbalanceddatalogsofcreditcardsusingartificialintelligence.MobileInformationSystems2020,1(2020),8885269.
[112] SiqiRen,BoLiao,WenZhu,ZengLi,WeiLiu,andKeqinLi.2018.Thegradualresamplingensembleformining
imbalanceddatastreamswithconceptdrift.Neurocomputing286(2018),150–166.
[113] RafiqAhmedMohammed,Kok-WaiWong,MohdFairuzShiratuddin,andXuequnWang.2020.PWIDB:Aframework
forlearningtoclassifyimbalanceddatastreamswithincrementaldatare-balancingtechnique.Proced.Comput.Sci.
176(2020),818–827.
[114] LiYang,DimitriosMichaelManias,andAbdallahShami.2021.PWPAE:Anensembleframeworkforconceptdrift
adaptationinIoTdatastreams.InIEEEGlobalCommunicationsConference(GLOBECOM’21).IEEE,01–06.
[115] AsimRoy.2016.Two-layeredensembleKohonennetsforimbalancedstreamingdata.InIEEECongressonEvolution-
aryComputation(CEC’16).IEEE,5215–5221.
[116] SebaSusanandAmiteshKumar.2021.Thebalancingtrick:Optimizedsamplingofimbalanceddatasets–Abrief
surveyoftherecentstateoftheart.Eng.Rep.3,4(2021),e12298.
[117] AminShahraki,MahmoudAbbasi,AmirTaherkordi,andAncaDeliaJurcut.2022.Acomparativestudyononline
machinelearningtechniquesfornetworktrafficstreamsanalysis.Comput.Netw.207(2022),108836.
[118] HongleDu,YanZhang,KeGang,LinZhang,andYeh-ChengChen.2021.Onlineensemblelearningalgorithmfor
imbalanceddatastream.AppliedSoftComputing107(2021),107378.DOI:https://doi.org/10.1016/j.asoc.2021.107378
[119] ManalAlmuammarandMariaFasli.2018.Learningpatternsfromimbalancedevolvingdatastreams.InIEEEInter-
nationalConferenceonBigData(BigData’18).IEEE,2048–2057.
[120] YangeSun,YiSun,andHonghuaDai.2020.Two-stagecost-sensitivelearningfordatastreamswithconceptdrift
andclassimbalance.IEEEAccess8(2020),191942–191955.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

Multi-ClassImbalancedDataHandlingwithConceptDriftinFogComputing 16:47
[121] DebanjanBorthakur,HarishchandraDubey,NicholasConstant,LeslieMahler,andKunalMankodiya.2017.Smart
fog:FogcomputingframeworkforunsupervisedclusteringanalyticsinwearableInternetofThings.InIEEEGlobal
ConferenceonSignalandInformationProcessing(GlobalSIP’17).IEEE,472–476.
[122] BrankaMikavicaandAleksandraKostić-Ljubisavljević.2019.FogComputinginLogisticsSystems.Logic.
[123] YohanJoo,JaehyeongLee,andJongpilJeong.2020.Ensemblefogcomputingarchitectureforunstablestatedetection
ofhydraulicsystem.Proced.Comput.Sci.175(2020),230–236.
[124] MohammedAnisBenblidia,BouzianeBrik,LeilaMerghem-Boulahia,andMoezEsseghir.2019.Rankingfognodesfor
tasksschedulinginfog-cloudenvironments:Afuzzylogicapproach.In15thInternationalWirelessCommunications
&MobileComputingConference(IWCMC’19).IEEE,1451–1457.
[125] ArmanAnzanpour,HumayunRashid,AmirM.Rahmani,AxelJantsch,NikilDutt,andPasiLiljeberg.2019.Energy-
efficientandreliablewearableInternet-of-Thingsthroughfog-assisteddynamicgoalmanagement.Proced.Comput.
Sci.151(2019),493–500.
[126] ShengjieXu,YiQian,andRoseQingyangHu.2019.Asemi-supervisedlearningapproachfornetworkanomaly
detectioninfogcomputing.InIEEEInternationalConferenceonCommunications(ICC’19).IEEE,1–6.
[127] SaurabhShukla,MohdFadzilHassan,MuhammadKhalidKhan,LowTangJung,andAzlanAwang.2019.Ananalyt-
icalmodeltominimizethelatencyinhealthcareinternet-of-thingsinfogcomputingenvironment.PLoSOne14,11
(2019),e0224934.
[128] SaurabhShukla,MohdFadzilHassan,LowTangJung,AzlanAwang,andMuhammadKhalidKhan.2019.A3-tierar-
chitecturefornetworklatencyreductioninhealthcareinternet-of-thingsusingfogcomputingandmachinelearning.
In8thInternationalConferenceonSoftwareandComputerApplications.522–528.
[129] JakubJalowiczor,JanRozhon,andMiroslavVoznak.2021.Studyoftheefficiencyoffogcomputinginanoptimized
LoRaWANcloudarchitecture.Sensors21,9(2021),3159.
[130] NaderMohamed,JameelaAl-Jaroodi,SanjaLazarova-Molnar,andImadJawhar.2021.Applicationsofintegrated
IoT-fog-cloudsystemstosmartcities:Asurvey.Electronics10,23(2021),2918.
[131] AIAAlzahrani,A.Al-Rasheed,A.Ksibi,M.Ayadi,M.M.Asiri,andM.Zakariah.2022.Anomalydetectioninfog
computingarchitecturesusingcustomtabtransformerforinternetofthings.Electronics11,23(2022),4017.
[132] ShusenYang.2017.IoTstreamprocessingandanalyticsinthefog.IEEECommun.Mag.55,8(2017),21–27.
[133] ShaimaaA.Hussein,AhmedI.Saleh,HossamEl-DinMostafa,andMarwaI.Obay.2021.AHybridSecurityStrategy
(HS2)forReliableVideoStreaminginFogComputing(RetractionofVol51,artno102412,2020).ElsevierRadarweg29,
1043NXAmsterdam,Netherlands.
[134] Jyun-YaoHuang,Wei-ChihHong,Po-ShinTsai,andI-EnLiao.2017.Amodelforaggregationandfilteringonen-
cryptedXMLstreamsinfogcomputing.Int.J.Distrib.SensorNetw.13,5(2017),1550147717704158.
[135] BrennoM.Alencar,RicardoA.Rios,CleberSantana,andCássioPrazeres.2020.FoT-Stream:Afogplatformfordata
streamanalyticsinIoT.Comput.Commun.164(2020),77–87.
[136] ElarbiBadidiandKarimaMoumane.2019.Enhancingtheprocessingofhealthcaredatastreamsusingfogcomputing.
InIEEESymposiumonComputersandCommunications(ISCC’19).IEEE,1113–1118.
[137] PauloBezerra,AdalbertoMelo,AllanDouglas,HugoSantos,DenisRosário,andEduardoCerqueira.2019.Acollab-
orativeroutingprotocolforvideostreamingwithfogcomputinginvehicularadhocnetworks.Int.J.Distrib.Sensor
Netw.15,3(2019),1550147719832839.
[138] IvanMerelli,LuciaMorganti,ElenaCorni,CarmeloPellegrino,DanieleCesini,LucaRoverelli,GabrieleZereik,and
DanieleD’Agostino.2018.Low-powerportabledevicesformetagenomicsanalysis:Fogcomputingmakesbioinfor-
maticsreadyfortheInternetofThings.Fut.Gen.Comput.Syst.88(2018),467–478.
[139] JuanLuisPérez,AlbertoGutierrez-Torre,JosepLluísBerral,andDavidCarrera.2018.Aresilientanddistributednear
real-timetrafficforecastingapplicationforFogcomputingenvironments.Fut.Gen.Comput.Syst.87(2018),198–212.
[140] MariaA.Rodriguez,RamamohanaraoKotagiri,andRajkumarBuyya.2018.Detectingperformanceanomaliesin
scientificworkflowsusinghierarchicaltemporalmemory.Fut.Gen.Comput.Syst.88(2018),624–635.
[141] AsifMuhammadandMuhammadAleem.2021.A3-Storm:Topology-,traffic-,andresource-awarestormscheduler
forheterogeneousclusters.J.Supercomput.77,2(2021),1059–1093.
[142] DanieleDeSensi,TizianoDeMatteis,andMarcoDanelutto.2018.Simplifyingself-adaptiveandpower-awarecom-
putingwithNornir.Fut.Gen.Comput.Syst.87(2018),136–151.
[143] IvanWalulya,DimitrisPalyvos-Giannas,YiannisNikolakopoulos,VincenzoGulisano,MarinaPapatriantafilou,and
PhilippasTsigas.2018.Viper:Amoduleforcommunication-layerdeterminismandscalinginlow-latencystream
processing.Fut.Gen.Comput.Syst.88(2018),297–308.
[144] Valeria Cardellini, Francesco Lo Presti, Matteo Nardelli, and Gabriele Russo Russo. 2018. Decentralized self-
adaptationforelasticdatastreamprocessing.Fut.Gen.Comput.Syst.87(2018),171–185.
[145] Claudia Misale, Maurizio Drocco, Guy Tremblay, Alberto R. Martinelli, and Marco Aldinucci. 2018. PiCo: High-
performancedataanalyticspipelinesinmodernC++.Fut.Gen.Comput.Syst.87(2018),392–403.
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.

16:48 F.Shariefetal.
[146] ZoltánZvara,PéterG.N.Szabó,BarnabásBalázs,andAndrásBenczúr.2019.Optimizingdistributeddatastream
processingbytracing.Fut.Gen.Comput.Syst.90(2019),578–591.
[147] ArvindKumarGangwarandSandeepKumar.2023.Conceptdriftinsoftwaredefectprediction:Amethodfordetect-
ingandhandlingthedrift.ACMTrans.InternetTechnol.23,2(2023),1–28.
[148] AtureAngberaandHuahYongChan.2024.AnadaptiveXGBoost-basedoptimizedslidingwindowforconceptdrift
handlinginnon-stationaryspatiotemporaldatastreamsclassifications.J.Supercomput.80,6(2024),7781–7811.
[149] KetanSanjayDesaleandSwatiV.Shinde.2023.Conceptdriftdetectionandadaptionframeworkusingoptimized
deeplearningandadaptiveslidingwindowapproach.ExpertSyst.40,9(2023),e13394.
[150] TaoHuang,BoyiXu,HongmingCai,JiaweiDu,Kuo-MingChao,andChengxiHuang.2018.Afogcomputingbased
conceptdriftadaptiveprocessminingframeworkformobileAPPs.Fut.Gen.Comput.Syst.89(2018),670–684.
[151] BrennoM.Alencar,JoãoPauloCanário,RuivaldoLobãoNeto,CássioPrazeres,AbertBifet,andRicardoA.Rios.2023.
Fog-DeepStream:AnewapproachcombiningLSTMandconceptdriftfordatastreamanalyticsonFogcomputing.
InternetThings22(2023),100731.
[152] Amir Hossein Estiri and Muthucumaru Maheswaran. 2021. Attentive federated learning for concept drift in
distributed5Gedgenetworks.arXivpreprintarXiv:2111.07457(2021).
[153] HassanMehmood,PanosKostakos,MartaCortes,TheodorosAnagnostopoulos,SusannaPirttikangas,andEkaterina
Gilman.2021.Conceptdriftadaptationtechniquesindistributedenvironmentforreal-worlddatastreams.Smart
Cities4,1(2021),349–371.
[154] I.MadeMurwantaraandPujiantoYugopuspito.2021.AnadaptiveIoTarchitectureusingcombinationofconcept-
driftanddynamicsoftwareproductlineengineering.TELKOMNIKA(Telecommun.Comput.Electron.Contr.)19,4
(2021),1226–1233.
[155] PallaviKulkarniandRoshaniAde.2014.Incrementallearningfromunbalanceddatawithconceptclass,conceptdrift
andmissingfeatures:Areview.Int.J.DataMin.Knowl.Manag.Process4,6(2014),15.
[156] ShikhaMehtaandothers.2017.Conceptdriftinstreamingdataclassification:algorithms,platformsandissues.Pro-
cediaComputerScience122(2017),804–811.
Received28January2023;revised13July2024;accepted6August2024
ACMComput.Surv.,Vol.57,No.1,Article16.Publicationdate:October2024.