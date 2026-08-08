Incremental Data Drifting: Evaluation Metrics, Data
Generation, and Approach Comparison
YU-TUNGPAI,CSIE,NationalTaiwanUniversity,Taipei,Taiwan
NIEN-ENSUN,CSIE,NationalTaiwanUniversity,Taipei,Taiwan
CHENG-TE LI, Department of Computer Science and Information Engineering, National Cheng Kung
University,Tainan,Taiwan
SHOU-DELIN,CSIE,NationalTaiwanUniversity,Taipei,Taiwan
Incremental data drifting is a common problem when employing a machine-learning model in industrial
applications.Theunderlyingdatadistributionevolvesgradually,e.g.,userschangetheirbuyingpreferences
onanE-commercewebsiteovertime.Theproblemneedstobeaddressedtoobtainhighperformance.Right
now,studiesregardingincrementaldatadriftingsufferfromseveralissues.Foronething,thereisalackof
clear-definedincrementaldriftdatasetsforexamination.Existingeffortsuseeithercollectedrealdatasetsor
syntheticdatasetsthatshowtwoobviouslimitations.Oneisinparticularwhenandofwhichtypeofdrifts
thedistributionundergoesisunknown,andtheotheristhatasimplesynthesizeddatasetcannotreflectthe
complexrepresentationwewouldnormallyfaceintherealworld.Foranother,therelacksawell-defined
protocoltoevaluatealearner’sknowledgetransfercapabilityonanincrementaldriftdataset.Toprovidea
holisticdiscussionontheseissues,wecreateapproachestogeneratedatasetswithspecificdrifttypes,and
defineanovelprotocolforevaluation.Besides,weinvestigaterecentadvancesinthetransferlearningfield,
including Domain Adaptation and Lifelong Learning, and examine how they perform in the presence of
incrementaldatadrifting.Theresultsunfoldtherelationshipsamongdrifttypes,knowledgepreservation,
andlearningapproaches.
CCS Concepts: • Information systems → Data mining; • Computing methodologies → Knowledge
representationandreasoning;
AdditionalKeyWordsandPhrases:Conceptdrift,incrementaldatadrift,datageneration
ACMReferenceFormat:
Yu-TungPai,Nien-EnSun,Cheng-TeLi,andShou-deLin.2024.IncrementalDataDrifting:EvaluationMetrics,
DataGeneration,andApproachComparison.ACMTrans.Intell.Syst.Technol.15,4,Article71(July2024),
26pages.https://doi.org/10.1145/3655630
ThisworkissupportedbytheNationalScienceandTechnologyCouncil(NSTC)ofTaiwanundergrants110-2221-E-006-
136-MY3,111-2221-E-002-146-MY3,112-2628-E-006-012-MY3,111-2221-E-006-001,and112-2634-F-002-006.
Authors’ContactInformation:Yu-TungPai,CSIE,NationalTaiwanUniversity,Taipei,Taiwan;e-mail:r08944012@csie.ntu.
edu.tw;Nien-EnSun,CSIE,NationalTaiwanUniversity,Taipei,Taiwan;e-mail:r09922019@csie.ntu.edu.tw;Cheng-TeLi,
DepartmentofComputerScienceandInformationEngineering,NationalChengKungUniversity,Tainan,Taiwan;e-mail:
reliefli@gmail.com;Shou-deLin,CSIE,NationalTaiwanUniversity,Taipei,Taiwan;e-mail:sdlin@csie.ntu.edu.tw.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbe
honored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,
requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2024Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ACM2157-6904/2024/07-ART71
https://doi.org/10.1145/3655630
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:2 Y.-T.Paietal.
1 INTRODUCTION
Machinelearning(ML)hasachievedtremendoussuccessinsolvingvariousindustrialproblems
includingclassification,recommendation,andrecognition.Inastandardsupervisedlearningsce-
nario, two assumptions are usually held: (1) training data comes all at once; (2) training data is
ofthesamedistributionastestingdata.Therefore,asimpletrain-then-fixprocessfordeploying
amodelcanachievedecentperformance.However,real-worldapplications,suchasE-commerce
recommendations, introduce complexities due to the sheer volume of data, such as user clicks
andpurchasehistories,generatedpersecondandtheevolvingnatureofuserbehaviorsovertime.
This dynamism and voluminous influx of data make the static model application infeasible and
introducethecriticalconsiderationof“ConceptDrift.”
ConceptDrift,asarticulatedby[49],signifiesthephenomenonwhereindatadistributionsex-
periencenon-static,underlyingshiftsovertime.Thedefinitiontypicallyhingesonthejointdistri-
butionP t (X,y)betweenfeaturesX andlabelsyataparticulartimestampt [14,30,33].Tobemore
specific,givenadataset,inwhichdataarrivesatdifferenttimestamps,theconceptdrifthappens
if∃t : P t (X,y) (cid:2) P t+1 (X,y).Conceptdriftattimet canbedefinedasthechangeofjointproba-
bilityofX andy attimet.SincethejointprobabilityP
t
(X,y)canbedecomposedintotwoparts:
P
t
(X,y)=P
t
(X)∗P
t
(y|X),threetypesofdatadriftingcanbedefinedasbelow,alsoasillustrated
inFigure1.
—CovariateDrift[14]comeswhenP(X)changeswhileP(y|X)remainsunchanged,i.e.,P
t
(X)(cid:2)
P
t+1
(X)andP
t
(y|X)=P
t+1
(y|X).Thishappenswhen,duetosomeartifacts,thesampleddata
ineachbatchvarieswhereasthedecisionboundariesdonot.
—ActualDrift [14]happenswhen,giventwotimestamps,P(y|X)driftswhileP(X)staysthe
same,i.e.,P
t
(X)=P
t+1
(X)andP
t
(y|X)(cid:2)P
t+1
(y|X).Anexampleisasituationwhere,when
buildingamovierecommendationsystem,viewersmaychangetheircriteriatorateacom-
edyhighastheywatchmorecomedies.
—ConceptDrift [14]indicatesthatwherethechangesofbothP(X)andP(y|X)happenatthe
same time in two consecutive timestamps, i.e., P t (X) (cid:2) P t+1 (X) and P t (y|X) (cid:2) P t+1 (y|X).
Eitherchangeoccursinthefeaturespaceorthemappingbetweenfeaturesandlabelscan
deterioratetheperformance.
Thisworkendeavorstofacilitatelearningamidsttheaforementionedthreetypesofdatadrift-
inginanincrementalmanner.Incrementaldatadrifting[14]isindicativeofthescenariowherethe
datadistributiongraduallytransitionsoveraspecificduration.Suchinstancesarenotrareinreal-
worldapplications.Considerascenarioinamovierecommendationsystem:ausermightgradually
shift their preferences from action genres to documentaries as they explore various social and
environmentalissues.Inasimilarvein,envisionthegradualincreaseindemandforelectriccarsas
globalawarenessandadvancementsinsustainabletechnologiesrise.Neitherofthesereal-world
evolutionsoccurredabruptlyorwithoutacertaintrajectory.Rather,theyunfoldedprogressively,
highlightingtheimperativeofaddressingincrementaldatadriftinpracticalapplications.Existing
work on learning with concept drifts struggles to adequately accommodate incremental data
driftingduetoseveralreasons.First,thereisanotablechallengeinhandlingincrementaldrifting
effectively for sequential data batches, as opposed to processing an instance-by-instance data
stream. Second, a significant issue arises regarding how to precisely evaluate a model’s perfor-
manceamidthenuancesofincrementaldatadrifting.Third,thegenerationofincrementaldrifting
datasets, which encompass covariate, actual, and concept types for astute model evaluation,
presents a notable conundrum. Last, identifying the most effective approach to learning amidst
incrementaldatadriftingremainsanunresolvedinquiry.Belowwediscusssuchfourreasonsin
moredetail.
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:3
Fig.1. Illustrationsofthreedatadriftingtypes.
—Batch-wise Data. Most of the methods tackling concept drift assume data arrives in the
formofadatastream,wheresamplesareexaminedonebyoneorinsmallchunks[30].There-
fore,thesealgorithms[10,17]typicallymaintainaslidingwindoworapoolofpreviousmod-
els,andapplymajorityvotingormonitorunderlyingdriftthroughdetection.However,we
holdthatthissettingispotentiallyimpracticalinreal-worldapplicationsfortworeasons.For
onething,sinceusersarecontinuallygeneratingdata,theamountofdataisincreasingexpo-
nentiallynowadays,whichmakeshandlingtheminstancebyinstancetooslow.Foranother,
collectingdatawithexacttimestampsisexpensive.Oftentimes,datacomeswithoutsignif-
icant element-wise consequences but simply represents an overall outcome in a period of
time,likebuyingpreferences,ortrends.Asaresult,werequireanincrementaldriftlearning
frameworkthatsimulatesarealML-Pipelinewheredataarrivesinbatchesofgreatamount.
—Model Evaluation. An effective learning model for incremental data drifting is expected
to meet two requirements. One is not forgetting the data distribution it has seen so far.
The other is being able to adapt to unseen data concerning incremental changes involved.
BackwardTransferandForwardTransfer[29]aretwowell-knownmetricstoevaluatemodel
learningoveracontinuumofdata.Wearguethatsuchtwometricscannotpreciselyestimate
the capability of transferring knowledge between incremental drifting data batches. The
memorizationofolddatashouldbemaintainedthroughouthistoricaltime,insteadofonly
theoldesttimeorthelatesttime.Besides,botharenotcomparablewithoneanothernorat
the same scale because the performance scores at the time of random model initialization
areingenerallow.Weneedproperevaluationmetrics.
—Data Generation. Existing studies on concept drift suffer from a lack of clear-defined
datasetsforexaminations.Waresetal.[48]pointoutashortfallintheavailabilityofpublic
benchmarkconceptdriftdatasets.Besides,Luetal.[30]alsorevealthelimitationsofcurrent
conceptdriftdatasets.Inparticular,forthosereal-worlddatasetsthatinvolvedrifts,typically
when and of which types the drifts happen are unclear. Without this information, evalua-
tionsarehardtomaketoconcludewhetherornotanalgorithmcaneffectivelyhandledrifts.
On the other hand, for those synthetic concept-drift datasets, such as SINE [11], Rotation
Hyperplane[46],andSEA[43],whereinstancesaregeneratedbyartificiallydefinedrules
andsettings,theyarehighlydependentonuser-specifiedparameters.Differentparameters
lead to various results, which make direct comparisons difficult. In addition, being low in
dimensionandpureinshape,syntheticdatasetscannotrevealrealdatapatternswewillface
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:4 Y.-T.Paietal.
in industrial conditions, such as image recognition and fraud detection. For example, SEA
dataset[43]isdesignedwiththreeattributeswhereonlytwoarerelevanttodrifts.Ifthesum
ofthetwoattributesexceedsathreshold,aninstanceislabeled0,andviceversa.Driftsare
createdbychangingthethresholdthroughtime.Weaimtogenerateconceptdriftdatasets
ofdifferenttypesinanincrementalfashionthatrepresentsreal-worldscenariosbetter.
—Learning Approach. Given the scenario that incremental drifting data arrives in a
batch-wise manner, it is impracticable to learn based on existing approaches that handle
datastreamwithconceptdrift[10,17].Nevertheless,ifweconsiderbatcheswithdifferent
datadistributionsasdifferentdomains,domainadaptationtechniques[7]canbeused.The
incrementaldistributionchangesinbatchesovertimealsofitthescenariooflifelonglearn-
ing[8].DomainAdaptationdealswithdomainshiftbyaligninglatentspacestogetherwhile
Lifelong Learning puts emphasis on not forgetting previously seen concepts. Although
Domain Adaptation and Lifelong Learning target different schemas, they both embody
solutions to handling discrepancies in data. To the best of our knowledge, none of past
workhasdiscussedmethodsinthesefieldsonconceptdrift.
Notethataddressingdatamanagementinthecontextoflargevolumes,thisworkjuxtaposesthe
conceptof“batch-wisedata,”entailingthehandlingofextensivedatasetspotentiallyinthetens
of thousands of data points, with the utilization of a “small chunk” of data, often limited to a
few hundred points [20, 31]. Our focus leans towards batch-wise data approaches, given their
alignmentwithpracticallarge-scaledatamanagementandcomputationalefficiencyinreal-world
scenarios.Whileemployingsmallchunksformodelupdatesoffersanimbleapproach,itmayfalter
inscalabilityandrobustness,especiallyinmaintainingpacewiththerapidinfluxofextensivedata
batches,potentiallycompromisingthemodel’scapabilitytoswiftlyadapttovariedpatternsand
comprehensiveinformationencapsulatedinlargerdatasets.
Inthiswork,wehighlightthelearningproblemofdatadriftingfromtwoaspects:incremental
fashionandbatch-wisedatasequence,whichareessential,andpractical,buthardlydiscussedin
theliterature.Wetermsuchkindoftaskasincrementaldatadrifting,whichistightlycoupledwith
covariate,actual,andconceptdrifts.Todealwiththeissuesmentionedabove,wefirstpresenttwo
newmetrics,OldTransferandNewTransfer,whichcanproperlyevaluatehowamodelmemorizes
thehistoricaldatadistributions,andhowamodeladaptstofuturedatawithincrementalchanges,
respectively.Second,wegeneratesyntheticimageandtabulardatasetswithexplicittypesofincre-
mentaldrifting,i.e.,covariate,actual,andconcept,inabatch-wisesetting.Third,weinvestigate
how recent advances in domain adaptation and lifelong learning can be utilized to learn in the
contextofincrementaldatadrifting.
Belowwesummarizethecontributionsofthiswork.
—Welearnwithincrementaldatadriftinginaholisticview,includingthebatch-wisesequence
data,definingevaluationmetrics,generatingthedatasets,andexaminingvariouslearning
approaches.Tothebestofourknowledge,thisisthefirstworkthatcomprehensivelylooks
intoincrementaldatadrifting.
—Weproposetwonovelevaluationmetrics,OldTransferandNewTransfer,toquantifythe
goodnessofalearningmodeldesignedforincrementaldatadrifting.Suchtwometricsquan-
tifyhowwell-driftingknowledgecanbememorizedbynewmodelsandsimultaneouslybe
adaptedfromoldmodels.
—Wegeneratesyntheticincrementaldriftingdatasets1withexplicitdrifttypes(i.e.,covariate,
actual,andconcept)fromexistingimageandtabulardatasets.Thedatagenerationprocess
1Datasetsareavailableathttps://github.com/cealia/drift_dataset
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:5
itself,basedonfeaturevaluesandgenerativeadversarialmodels,canbeappliedtomorereal
datasetswithsimilarproperties.
—Weidentifythattheapproachesofdomainadaptationandlifelonglearningproperlyfitand
tackle incremental data drifting. Extensive experiments conducted on both the generated
and the real datasets deliver insights that unfold the relationships among drifting types,
knowledgepreservation,andlearningapproaches.
We organize this paper as follows. Section 2 reviews relevant studies. We present how to ro-
bustlyevaluateamodelthatdealswithincrementaldatadriftinginSection3,anddescribehow
to generate synthetic incremental drifting datasets in Section 4. We give three approaches that
canhandlethelearningwithincrementaldatadriftinginSection5.Theexperimentalresultsare
reportedinSection6.WeconcludethisworkinSection7.
2 RELATEDWORK
Wereviewtherelevantstudiesfromfouraspects.Wefirstdescribethetypicalmethodsforlearning
withconceptdrifts,thendiscussexistingconcept-driftdatasets.Wealsodiscussrecentadvances
indomainadaptation,lifelonglearning,andout-of-distributiongeneralizationthatcandealwith
knowledgetransferbetweendomainswithdifferentdatadistributions.
Solutions to Concept Drift. The Drift Detection Method (DDM) [13] keeps track of the
onlineerrorratewithinthetimewindow,alongwithapre-definedwarninglevelandadriftlevel.
Iftheerrorincreasesreachingthewarninglevel,whichimpliestheconceptdrifthappens,anew
model is built to learn the subsequent instances. If the error increases reaching the drift level,
theoldmodelisreplacedbythenewmodelforpredictions.TheEarlyDriftDetectionMethod
(EDDM) [2] improves DDM using the distance between classification errors to detect concept
drifts. Although these methods can adapt to the newest concepts, they may forget old concepts
thatarestillconsistentwithnewdata.Learn++.NSE[10]constructsapoolofensembleclassifiers
trainedondifferentdatabatches.Weightedmajorityvotingisappliedtoproducethefinalpredic-
tion.KappaUpdatedEnsemble(KUE)[5]isalsoanensemble-basedapproachthatusesdynamic
weightingandselectionofbaseclassifiers.Anewclassifierisaddedtotheensembleonlywhenit
hasapositivecontributiontoimprovingtheperformance.
Addressingincrementaldatadriftingdemandsastrategythatbalancesadaptingtonewconcepts
andpreservinghistoricalknowledge,afeatnotfullyrealizedbydiscussedmethods.Thesepredom-
inantlyemploybinary,threshold-drivendecisionsformodelretentionorreplacement,potentially
sacrificing insights from older models and data. Incremental drifts, which may not significantly
impacterrorratesormodelperformanceimmediately,couldtherebyescapedetectionandinter-
ventionbysuchapproaches.Whilethesemethodsexhibitacommendablerapidadaptationtonew
concepts, they often lack sturdy mechanisms for retaining valuable knowledge from historical
data, presenting an ongoing challenge in learning amidst concept drift, particularly in the sub-
tletiesofincrementaldatadrifting.Theentwiningoffreshandestablishedknowledge,embodying
bothlearningstabilityandplasticity,standsasacrucialareawarrantingfurtherexplorationand
innovationinthisdomain.
Concept Drift Datasets. Several synthetic datasets and real-world datasets are widely used
to evaluate the performance of an algorithm dealing with concept drift. Synthetic datasets such
asSINE[11],RotationHyperplane[46],andSEA[43]aregeneratedbyuser-specifiedparameters.
Instances in these datasets are usually low in dimension, making it hard to reflect the concept
driftphenomenainrealindustries.Althoughmanyreal-worlddatasets,suchasEmail_data[23],
Spam_data[23],andGasSensorArrayDriftDataset[45],havebeencreatedtotackletheabove-
mentionedissues,itisstilluncleartoknowwhichtypesofdriftshappen.Withoutthisinformation,
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:6 Y.-T.Paietal.
onecannotconcludeifanalgorithmiseffectivetoovercomeacertaintypeofconceptdrift.Inthis
work,weaimatgeneratingnewconceptdriftdatasetsthathavethebenefitsofbothexistingsyn-
theticandreal-worlddatasets.Ourcompileddatasetscanreflectreal-worldscenariosduetothe
highdimensionalityoffeatures,havedriftingbehaviorsthathappenedinanincrementalfashion,
andcanbeutilizedtomeasuretheperformanceofaspecificdrifttypeforagivenmethod.
DomainAdaptation.Giventwodatadomains(i.e.,sourceandtarget)drawnfromdifferentdis-
tributions,domainadaptationaimsateffectivelyadaptingthelearningtotargetdatabyusingonly
labeledsourcedataandunlabeledtargetdata.Mostoftheexistingmethodsaretoalignthedistri-
butionsofsourceandtargetdomainsthroughafeatureextractor.DANN[16]createsanadditional
domaindiscriminatorandagradientreversallayertoforcethefeatureextractortoalignbothdo-
mains. MCD [36] considers not only the alignment between domains, but also the task-specific
decisionboundariesbetweenclasses.DIRT-T[40]combinesDANNwiththeclusterassumption,
whichmeansthatthetargetdatashouldbefarfromthedecisionboundary.AdaptiveRiskMin-
imization(ARM)[51]isintroducedinthecontextofdomaingeneralization,wheretrainingdata
is structured into domains, and there might be multiple test-time shifts corresponding to new
domainsordomaindistributions.Whiletraditionalapproachesfocusonlearningasinglerobust
modelorinvariantfeaturespacethatperformswellacrossalldomains,ARMtakesadifferentap-
proach.Itaimstolearnmodelsthatcanadaptduringtesttimetodomainshiftsusingunlabeled
testpoints.ThecentralideabehindARMistooptimizemodelsforeffectiveadaptationtoshiftsby
learningtoadaptbasedonthetrainingdomains.SequentialModelAdaptationUsingInternal
distribution(SMAUI)[35]isanalgorithmthatfocusesonthelearningofaparametricinternal
distribution,derivedfromthesourcedomain,allwithinaunifiedembeddingspace.Byharnessing
thepowerofthisinternallysculpteddistribution,SMAUIfacilitatesthealignmentofsourceand
targetdomaindistributions.Theadaptationtoperformoptimallyinthetargetdomainisachieved
bysamplingfromthiscalculatedinternaldistributionandcompellingthetargetdomaintoadhere
toasimilardistributionintheembeddingspace.Thisisimplementedthroughtheminimization
ofthedistancebetweentherespectivedistributions,ensuringasmoothandeffectiveadaptation
ofthemodelacrossvariousdomains.
ExistingdomainadaptationmethodslikeDANN,MCD,andSMAUIhaveshownproficiencyin
reconciling discrepancies between distinct data domains, yet their efficacy dwindles when con-
fronted with the subtle and persistent nature of incremental data drifting. The core limitations
stemfromtheiroftenstaticandinstantaneousadaptationmechanisms,which,whileaptlymanag-
ingabruptordiscretedomainshifts,inadequatelyaddresstheslow,continuousevolutioninherent
toincrementaldrifts.Specifically,thesemethodstendtoprioritizeimmediateadaptationandalign-
ment between source and target distributions, potentially overlooking the cumulative impact of
minute,ongoingchangesindatadistributions.Furthermore,theirlimitedcapacitytoretainand
utilize knowledge across varying phases of data evolution curtails their ability to generate pre-
dictionsthatarecogentlyawareoftheentiretyofdata’stemporaltrajectory.Therefore,thereisa
pronouncedneedforapproachesthatnotonlyadeptlyadapttoimmediatedistributionaldisparities
butalsopreserveandleveragehistoricaldataknowledge,ensuringnuanced,temporally-informed
predictiveperformanceamidstthegradualundulationsofincrementaldatadrifting.Nevertheless,
weconsidersomedomainadaptationmethodsusefulwhenhandlingfeaturediscrepanciesinnew-
comingdata(i.e.,newconceptswithcovariatedrift),andwillhavethemexperimentallycompared
tootherapproaches.
LifelongLearning.Lifelonglearningaimstomitigatethecatastrophicforgettingofalearner,
which means forgetting the knowledge learned from previous tasks after training on a new
task with different data distribution. Various approaches are proposed: regularization-based
approach, data rehearsal, generative rehearsal, and additional neural resource allocation. The
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:7
regularization-basedapproach[25]penalizesmoreonimportantparameterstrainedonprevious
tasks, and penalizes less on unimportant parameters meaning that they can be updated more
easilywhentrainingonafuturetask.Thedatarehearsalapproach[34]storesalimitedamount
of historical data utilized in old tasks, and adaptively reintroduces them at the training phase
of new tasks. The generative rehearsal approach [39] trains a generator to produce old data
instead of storing them. Gradient-based Coreset Selection (GCR) [44] is a replay-based
continuallearningframework.GCRemploysgradientapproximationasastrategicoptimization
criterionforcoresetselection,astutelyamalgamatingrecentprogresswithinsupervisedlearning
environments. Ingeniously interwoven into the continual learning process, GCR prioritizes the
selectionandupdatingofreplaybuffersforensuingtrainingphases.Moreover,GCRjudiciously
incorporates a supervised representation learning loss into the continual learning objective,
thereby enriching the representations learned throughout the model’s lifecycle, and fostering a
morerobustandadaptivelearningparadigm.TrustRegionGradientProjection(TRGP)[28]
navigatesforwardknowledgetransferwithanastute,layer-wiseapproach,introducinga’trustre-
gion’tosingularlyselectrelevantoldtasksfornewonesusinggradientprojectionnormsmapped
onto input subspaces. Recycling frozen weights from selected old tasks via a layer-wise scaling
matrix, and concurrently optimizing scaling matrices and the model in directions orthogonal to
old task subspaces, TRGP adeptly facilitates knowledge transfer while sidestepping forgetting,
therebyjudiciouslybalancingrecallandadaptabilityincontinuallearningscenarios.
Whilecurrentlifelonglearningstrategieslikeregularization-based,datarehearsal,andgener-
ative rehearsal approaches, alongside models like GCR and TRGP, offer innovative solutions to
the catastrophic forgetting dilemma, their application in scenarios of incremental data drifting
presentsnotablechallenges.Onesuchchallengestemsfromthemeticulousbalancethesemodels
strivetomaintainbetweenretainingknowledgefrompriortasksandadaptingtonewones.Given
thesubtletyandgradualprogressionofincrementaldrifts,existingmethodsmightstruggletodis-
cern and adequately respond to slowly morphing data distributions, potentially misjudging the
relevance and applicability of historical data and knowledge. Notably, the slow, nuanced nature
ofincrementaldatadriftingmightnotsufficientlytriggeradaptiveresponsesinthesemodels,as
thegradualshiftsmaynotintroduceabrupt,discernibleperformancedeteriorations.Furthermore,
themodelsmightnotbeabletodifferentiatebetweenthenecessitytoretainpreviouslylearned
knowledgeandtheimperativetoadapttominoralterationsindataproperties.Thisintricacybe-
comesespeciallypertinentwhenpastconceptscontinuetoholdrelevance.Sincewecanconsider
learningfromhistoricaldataasoldtasksandpredictionofnewdataasthenewtask,alongwith
differentdatadistribution,respectively,lifelonglearningmethodscanbeutilizedtomodelincre-
mental drifting between data batches. We will incorporate typical lifelong learning methods to
examinehowtheyperforminthecontextofincrementaldatadrifting.
Out-of-distribution Generalization. Out-of-distribution (OOD) generalization refers to
amodel’sabilitytoperformaccuratelyondatathatmaycomefromadistributiondifferentfrom
thetrainingdata.Thisconceptispivotalinapplicationswheremodelsaredeployedindynamic
and diverse real-world scenarios. Invariant Risk Minimization (IRM) [1] is a paradigm that
seeks to identify and leverage invariant correlations across various training distributions to
facilitateOODgeneralization.Themethodaimstolearnadatarepresentationwheretheoptimal
classifierisconsistentacrossalltrainingdistributions,linkinglearnedinvariancestounderlying
causal structures. Risk Extrapolation (REx) [26] addresses distributional shifts by assuming
variations across training domains are indicative of potential test-time variations, even those of
moreextrememagnitudes.RExanditsvariantsexhibitacapacitytorecovercausalmechanisms
andproviderobustnessagainstinputdistributionchanges,offeringabalancebetweenrobustness
to causally induced distributional shifts and covariate shift. Guo et al. [19] critically evaluate
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:8 Y.-T.Paietal.
Fig.2. Batchesofdriftdataarrivesequentially.Yellowandorangeblocksareatthecurrentandhistorical
timesteps,respectively.Greenonesarethenextbatchestobepredicted.
IRM,particularlyunderconditionsofstrongspuriousness,whereittendstofailduetotherobust
spurious correlations. A solution is proposed by combining IRM with conditional distribution
matching, mitigating specific types of spurious correlations under strong spuriousness. EIIL [6]
is a framework for domain-invariant learning that infers partitions maximally informative for
downstreamInvariantLearningwithoutexplicitdomainlabels,establishingaconnectionbetween
domain-invariantlearningandalgorithmicfairness.
TherelationshipbetweenOODgeneralizationandincrementaldatadriftingisnuanced.While
OODgeneralizationfocusesonensuringmodelperformanceacrossdiverse,unseendistributions,
incrementaldatadriftingpertainstothegradual,oftensubtle,shiftindatadistributionsovertime.
MethodsdevelopedforOODgeneralization,suchasIRM[1]orREx[26],primarilyaimtoensure
robustnessagainststark,potentiallyabruptdistributionalshiftsandmaynotbedirectlyapplica-
ble to scenarios of incremental data drifting due to their design and assumptions. Incremental
datadriftingrequiresmodelstocontinuouslyadaptandlearnfromtheslowlychangingdatadis-
tribution,which isinherently adifferent problem from ensuring generalization acrossdistinctly
different distributions. Thus, while OOD generalization methods provide valuable insights into
managingdistributionshifts,theymaynotinherentlycatertothesubtletiesandcontinuousadap-
tationrequiredtohandleincrementaldatadriftingeffectively.
3 EVALUATIONFRAMEWORK
Weconsiderapracticaltrainingprotocol:(1)Alargeamountofdata,whichwerefertoasabatch,
arrivesatatime.(2)Dataindifferentbatchesdriftsincrementally.(3)Alearnercanperformseveral
passes over instances in a single batch. Figure 2 illustrates the logic of how batches of data are
observedbyalearnerovertime.Giventhebatchofthecurrenttimestep(yellow)andthehistorical
batches(orange)formodeltraining,thegoalistomakepredictionsonthedataatthenexttime
step(green).
Under this training protocol, there are two metrics that are critical to evaluating a learner’s
performance.ThefirstisOldTransfer:theextenttowhichalearneriscapableofnotforgetting
the data distribution it has seen so far. The second is New Transfer: how well the learner can
adapt to unseen data concerning incremental changes involved. Regarding accessing a learner’s
abilitytotransferknowledge,Lopez-PazandRanzato[29]havedefinedtwotypesofevaluation
metrics,BackwardTransfer andForwardTransfer,toevaluatemodelslearningoveracontinuum
of data. Backward transfer is calculated only once after all data is observed. The calculation of
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

| IncrementalDataDrifting |     |     |     |     | 71:9 |
| ----------------------- | --- | --- | --- | --- | ---- |
Fig.3. AnillustrationofOldTransfermetric.
Forward transfer includes the performance at the time of model weights’ random initialization.
Wearguethatsuchtwometricshaveissueswithnotpreciselyestimatingthecapabilityoftrans-
ferringknowledge.Foronething,thememorizationofolddatashouldbemaintainedthroughout
historical time, instead of only the oldest time or the latest time. For the other, Backward trans-
ferandForwardtransferarenotcomparablewithoneanothernoratthesamescalebecausethe
performance scores at the time of random model initialization are in general low, which makes
forwardtransferexceptionallyhighwhenamodeldoesperformforwardtransferonnewdata.
For better generalization and robust evaluation of knowledge transfer in the context of vari-
ousdatadrifting,weextendthemetricsofbackwardandforwardtransferinthefollowingways.
TheevaluationofthecapabilityofknowledgetransferindatadriftingrequirestheproposedOld
thei-th
Transfer and New Transfer to compare two learners. After a learner is fully trained on
batchdata (abbrev. D i), we measure the performance scores P on test sets of every batch of
|        | i        |         |             | i,j                      |       |
| ------ | -------- | ------- | ----------- | ------------------------ | ----- |
| i.e.,D | ,D ...,D | obtainP | 1,i,P ...,P | whereP                   | dataD |
| data,  | 1 2 ,    | k, and  | 2,i, k,i,   | i,j is the performanceon | i     |
afterobservingdataD j.Givenanovellearnerandabaselinelearner,werefertotheperformance
oftheformerasP i,j,andthatofthelatterasP ∗ .Assumetherearek batchesofdataarrivingat
i ,j
time,t =0,t =1,...,tillt =k,wedefineoldtransferandnewtransfer:
(cid:2) (cid:6)
|     |     |             | (cid:3)k−1 (cid:3)k−1 | (cid:4) (cid:5) |     |
| --- | --- | ----------- | --------------------- | --------------- | --- |
|     |     | OldTransfer | =avд                  | P −P∗ ,         |     |
i,j i,j
|     |     |     | i=1 j=i+1 |     |     |
| --- | --- | --- | --------- | --- | --- |
(cid:2) (cid:6)
|     |     |             | (cid:3)k−1 | (cid:3)k−1 (cid:4) (cid:5) |     |
| --- | --- | ----------- | ---------- | -------------------------- | --- |
|     |     | NewTransfer | =avд       | P −P∗ .                    |     |
i,j i,j
|     |     |     | i=2 j=i−1 |     |     |
| --- | --- | --- | --------- | --- | --- |
WecreateFigures3and4toelaboratehowOldTransferandNewTransferareobtained,respectively.
Old transfer is to quantify to what extent old data be forgotten by a model. Hence, for every
pair of data batches D i and D j andi < j, we calculate the performance. In other words,i < j
meansthatamodelistrainedonnewdataD andistestedonolddataD i.Onthecontrary,new
j
transferestimatesthedegreeofamodel’sadaptiontonewdata.ForeachpairofdatabatchesD
i
and D and i = j + 1, we calculate P i,j, indicating the performance that a model is trained on
j
| batchD |     |     | batchD |     |     |
| ------ | --- | --- | ------ | --- | --- |
a j and tested on its immediate next j+1 . By obtaining scores of old transfer and
newtransferbetweenabaselinelearnerandanovellearner,onewouldfinditpracticaltojustify
thenovellearner’seffectivenessintransferringknowledgeindatadrifting.Thelargerthescores,
thebetteranovellearneroutperformsitsbaselinecounterpart.Notethat,forclearlypresenting
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:10 Y.-T.Paietal.
Fig.4. AnillustrationofNewTransfermetric.
Table1. Differencesbetween“OldTransfer”and“BackwardTransfer”
Aspect OldTransfer(Proposed) BackwardTransfer(Existing)
(cid:7) (cid:7) (cid:7)
Equation avg( k i= − 1 1 k j= − i 1 +1 (P i,j −P i ∗ ,j )) avg( k i= − 1 1P k,i −P i,i )
Throughoutlearning,comparing
Onlycalculatedonce,afteralldatahas
CalculationPeriod performanceonpreviousbatchesbefore
beenobserved
andafterobservingeachsubsequentbatch
Compareperformanceofanovellearnerto
Compareperformanceonearlierbatches
ComparisonBase abaselineonolddatafollowingthe
beforeandaftertheentiretrainingprocess
observationofeachsubsequentbatch
Takeintoaccountthevariabilitybetweena
novellearnerandabaselinelearner, Onlyconsidertheperformanceofasingle
LearnerVariability
consideringboththeirperformanceson modelonolddataafterobservingalldata
olderdataafterobservingnewdata
BackwardTransferneglectsthegradualprogressionofhowolddataisremembered
orforgottenthroughoutthelearningjourneybyevaluatingonlyafteralldataisob-
Criticism
served,potentiallyconcealingperiodsofforgettingandrelearningduringthelearn-
ingprocess.
thedifferencesamongthesemetrics,wecreateTables1and2,inwhichtheequationsofmetrics
areprovided,toconcretelycomparetheproposedoldtransferandtheexistingbackwardtransfer,
andtocomparetheproposednewtransferandtheexistingforwardtransfer,respectively.Inthese
twotables,thecomparisonsareonvariousaspects,includingcalculationperiod,comparisonbase,
learnervariability,andcriticism.
Discussion.Oneconcernaboutthesetwoproposedmetricsisthattheyrequireatestsetfor
each time step (probably also a validation set for each time step), which may not be the case
in real-world applications. First, regarding forward transfer, it appears there might be a slight
misunderstanding.Thismetricdoesnotnecessitatestoringatestsetforeverytimestep.Rather,it
involvesapplyingthemodeltrainedattimestepttothetestsetfromtimestept+1.Thisprocedure
doesnotentailretainingmultipletestsetsacrossalltimestepsandtherebyisnothinderedbythe
issuesraised.However,forbackwardtransfer,ourinitialmethodologyrequirestheavailabilityof
atestsetforeachtimestep,whichcouldimposestoragechallenges.Yet,therearepragmaticways
to navigate this, such as storing a modestly-sized test set for each time step that is adequately
representative, hence maintaining a balance between storage efficiency and experimental rigor.
Alternatively,backwardtransfercouldbemodifiedtoinvolveinferenceusingthemodelfromtime
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:11
Table2. Differencesbetween“NewTransfer”and“ForwardTransfer”,inwhichb¯isthe
VectorofTestAccuraciesforEachBatchatRandomInitialization
Aspect NewTransfer(Proposed) (cid:7) (cid:7) ForwardTransfer(Existing)
|     |     | k − k − | ∗   |     | (cid:7) k |     |
| --- | --- | ------- | --- | --- | --------- | --- |
Equation avg( i= 1 j= i 1 −1 (P i,j −P )) avg( P i−1,i −b¯ i )
|     |     | 2                            | i ,j |     | i=2                             |     |
| --- | --- | ---------------------------- | ---- | --- | ------------------------------- | --- |
|     |     | Throughoutlearning,comparing |      |     | Includethemodelperformanceatthe |     |
CalculationPeriod performanceonnewdataafterobserving timeofweights’randominitialization,
|     |     | eachpreviousbatch |     |     | andcalculatedthroughouttraining |     |
| --- | --- | ----------------- | --- | --- | ------------------------------- | --- |
Compareperformanceofanovellearnertoa Compareperformanceonsubsequent
ComparisonBase baselineonnewdata,giventheexperiences batchestothemodel’sperformanceat
|     |     | fromobservingpreviousbatches |     |     | randominitialization |     |
| --- | --- | ---------------------------- | --- | --- | -------------------- | --- |
Considerthedifferentialperformance
betweenanovellearnerandabaseline Onlycontemplatethesinglemodel’s
LearnerVariability learneronnewdata,accommodatingan adaptivecapacitieswithreferencetoits
|     |     | understandingofadaptivecapabilitiesfrom |     |     | initial,untrainedstate |     |
| --- | --- | --------------------------------------- | --- | --- | ---------------------- | --- |
observingpreviousdata
Forward Transfer is criticized for the inclusion of initial untrained performance,
whichistypicallylowandthusresultsinseeminglyhighadaptabilityscores.Fur-
Criticism thermore,theinclusionintroducesanon-comparabilityandscalingdiscrepancywith
Backward Transfer, limiting their joint utility in holistically evaluating a model’s
adaptivelearningperformance.
|     | Table3. | SummaryoftheFourGeneratedIncrementalDriftDatasets |     |     |     |     |
| --- | ------- | ------------------------------------------------- | --- | --- | --- | --- |
Datasetname drifttype #ofbatch item#perbatch train:val:test inputformat tasktarget
|     | Aging Covariate | 5   | 2276  | 8:1:1 | 64-64image | genderclassification |
| --- | --------------- | --- | ----- | ----- | ---------- | -------------------- |
|     | Pose Covariate  | 5   | 23708 | 8:1:1 | 64-64image | genderclassification |
AmazonReviewA Actual 4 3175 8:1:1 tabular semanticclassification
AmazonReviewC Concept 4 3175 8:1:1 tabular semanticclassification
steptonlyonthetestsetsfromthemostrecentmtimesteps,i.e.,fromt−mtot−1.Thisapproach
wouldalleviatethenecessityforextensivestoragewhilestillprovidingarelevantandinsightful
evaluationofthemodel’sabilitytogeneralizefromitsaccumulatedknowledgetoprevioustasks.
4 INCREMENTALDRIFTDATAGENERATION
Wegeneratesyntheticdatasetswithincrementalcovariatedrift,incrementalactualdrift,andin-
cremental concept drift. In each generated dataset, instances are divided into multiple batches
| B ,...,B | ,...,B | B = {(x | ,y )}n ,k |     |     | andn |
| -------- | ------ | ------- | --------- | --- | --- | ---- |
0 i k, where i j j j=1 is the number of batches, is the number of
instancesineachbatchB i.Atrainingmodelwillobserve,batchbybatch,atdifferenttimestamps,
i.e.,t ,t ,...,t ,...,t k. The drifting behaviors in the synthesized data happen incrementally be-
|     | 0 1 i |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- |
tween every two consecutive batches over time. We summarize the four generated incremental
driftdatasetsinTable3.
4.1 CovariateDriftData
Incovariatedatadrifting,giventwotimestampst andt ,werequireP(X) (cid:2)P(X)
|     |     |     | 0   | 1   |     | t t whilemain- |
| --- | --- | --- | --- | --- | --- | -------------- |
tainingP(y|X) =P(y|X) .TocreateP(X)driftsincrementallybetweenbatchesofdata,wepro- 0 1
|     | t   | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | 0   | 1   |     |     |     |     |
videtwoapproaches.Oneisafeature-based approach,andtheotherisagenerativeadversarial
network(GAN)basedapproach.Inthemeanwhile,byfixingtheclassificationgoalamongalldata
batches,wecanensureP(y|X)remains.
o
4.1.1 Feature-based Approach. We leverage an ordinal feature in the original dataset. By
groupingfeaturevaluesofo intomultipledisjointsetsinascendingorder,datainstanceswhose
valuesoffeatureobelongtothesamesetareassignedtothesamebatchB
i.Hence,amodeltrained
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:12 Y.-T.Paietal.
Fig.5. AnillustrationofAgingdataset withincrementalcovariatedrift.Differentshapes(e.g.,circles,trian-
gles,rectangles)representfaceswithdifferentageintervals.
batchbybatchwillexperienceanincrementalcovariatedriftwithrespecttofeatureo.Belowwe
introduce the Aging Dataset based on a feature-based approach. Note that any existing dataset
withanordinalfeaturecanusethesamewaytocreateadatasetwithincrementalcovariatedrift.
WeutilizetheUTKFace2[52]datasettocreatetheAgingDataset.TheUTKFacedatasetcontains
roughly20,000humanfaceimagesrangingfrom0to116yearsold.Weusetheagefeature,asan
ordinalfeature,todividethefaceimagesintofivebatches,i.e.,B ,B ,...,B ,eachofwhichcon-
0 1 4
tainsimagesagedbetween3-17,18-25,26-35,36-55,and56up,respectively.Ontheotherhand,the
targettaskistodogenderclassification.ThisguaranteesP(y|X)tobeconsistentamongallbatches.
Figure5isanillustrationofhowagespanschangeamongbatchesoverdifferenttimestamps,in
whichthegenderdistributionismaintained,toconstructtheincrementalcovariatedriftdata.
4.1.2 GAN-based Approach. Even though Feature-based obtains success in generating incre-
mental P(X) drifts, we cannot always expect every dataset contains proper ordinal or continu-
ous features, like age, to create covariate drift data. Therefore, we propose to use the semantic
interpolation capability of generative adversarial networks (GAN) [18] to match such incremen-
tal changes from scratch. GAN has demonstrated its great effectiveness in generating realistic
images[4,21,22].Notonlydoesthemodelgeneratehigh-qualityimagesbutitslatentspacealso
showsinterpretability.Recentstudies[37,38]haveworkedonlatentsemanticinterpretation.They
aimatfindingmeaningfuldirectionsinthelatentspaceineitherasupervisedoranunsupervised
manner.Bymovingthelatentcodeinacertaindirection,oneisabletotakecontrolofthetraitsof
outputimages,effectsofwhichincludeagradualchangeinlightingconditioninscenesynthesis,
ortheextentofasmileonfaces.
WeuseSeFa3[38],thestate-of-the-artunsupervisedmethodofGAN-basedsemanticinterpola-
tion,tocreatethePoseDataset withincrementalcovariatedrift.WefirstapplyaStyleGAN[22]
2https://susanqq.github.io/UTKFace/
3https://github.com/genforce/sefa
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:13
Fig.6. AnillustrationofPosedatasetwithincrementalcovariatedrift.Differentshapes(e.g.,circles,triangles,
rectangles)representfaceswithdifferentturnings.
modeltrainedontheFlickr-Faces-HQDataset(FFHQ)4totheSeFadataset.Byfactoringthe0-1
layerofthegenerator,wesegmentitinto20fragments.Finally,weretrievethe1,6,9,13,19steps
ofimagesasthefivebatchesofimages,i.e.,B ,B ,...,B ,inthePosedataset.Eachbatchcontains
0 1 4
8,278 images. Likewise, P(y|X) remains consistent as the goal among all data batches is gender
classification.Figure6showsanillustrationofthecompiledPosedataset.Incrementalchangesin
faceturningsbatchbybatchcanbeobservedwhilethegenderdistributioniskept.
Notethat,asidefromimagedata,GANcanbeusedtogeneratetabulardata[50].Therefore,we
highlightthepotentialofgeneralizingGAN’ssemanticinterpolationtogenerateincrementalP(X)
driftsinfuturework.Byrevealingtheunderlyingsemanticvectorofapre-trainedGAN,onecan
createincrementalP(X)drifts.
4.2 ActualDriftData
TocreateP(y|X)driftsincrementallybetweenconsecutivedatabatches,weadoptthefeature-based
approach.Givenadatasetwithanordinallabelo,athresholdτ canbeusedtoconvertthetaskto
beabinaryclassification,wherelabel=0ifo ≤τ whilelabel=1ifo >τ.Bychangingthethreshold
τ fromsmalltolargebetweenconsecutivebatches,incrementalP(y|X)driftscanbecreated.Inthe
meanwhile,P(X)remainsfixedbyrandomlydispensingdatainstancesintobatches.Notethatany
existingdatasetwithanordinallabelcanbeusedinthesamewaytocreateanewdatasetwith
incrementalactualdrift.
We create the Amazon Review Actual Drift dataset (Amazon Review A) from the Amazon Re-
viewdataset5 [32].Toletthedatabetterfitourgoal,weretrieveproductreviewsfromonlyfour
categories:ArtCraft,DigitalMusic,Lawn&Garden,andSoftware.Eachdatainstancecontainsa
textreviewandascorerangingfrom1to5.Wedrawanequalnumberof2,540reviewsforeach
4https://github.com/NVlabs/ffhq-dataset
5https://nijianmo.github.io/amazon/
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:14 Y.-T.Paietal.
Fig.7. AnillustrationonAmazonReviewAdatasetwithincrementalactualdrift.
category.Weencodeeachtextreviewintoa768-dimensionalembeddingbyapre-trainedBERT6
[9].Asforthe1–5scores,wedividethemintotwoclasses:likeanddislikebasedonathreshold
τ. Scores lower than the threshold go to the dislike class whereas scores above the threshold
gotothelikeclass.Byadjustingthethresholdsfrom2to4,wecangeneratefourdatabatches
B ,B ,B ,B thatmaptheincrementalactualdriftsinP(y|X).Inthemeanwhile,P(X)remainsthe
0 1 2 3
same since all reviews are equally sampled from the four productcategories. Figure7 showsan
illustrationofhowActualDrifthappensonreviewembeddingsamongdatabatchesatdifferent
timestamps.
Notethatwestrategicallydefinethethreshold,τ,withreviewsscoringbelowitdesignatedas
“dislike”andthoseaboveas“like”,therebyconvertingtheproblemintoabinaryclassificationtask.
Theprogressionofτ overvarioustimepointsaimstosimulateactualdriftbygraduallyescalating
this threshold. It is crucial to elucidate that this design choice is primarily a hypothesis devised
to generate an incremental actual drift dataset, while also offering a framework of design that
canbereferencedinsimilarexperimentalcontexts.AslongastheprobabilitydistributionP(y|X)
shifts,alternativehypotheses,suchasassigningdifferentthresholdsfordifferentproducts,could
beequivalentlyformulatedandtested.Theconcretechoiceofthresholdandlabelingstrategywas
shapedwiththeintentionofprovidingaclear,comprehensible,andreproduciblemethodologyfor
simulatingactualdriftinawidelyrecognizeddataset,therebyfacilitatingarobustevaluationof
theproposedmethodsunderconsistentandtransparentconditions.
4.3 ConceptDriftData
Wecompiletheincrementalconceptdriftdatasetbasedonthefeature-basedapproach.Theobjec-
tiveistosimultaneouslycreatethedriftsofP(X)andP(y|X)incrementallybetweenconsecutive
databatches.Givenadatasetwithacategoricalfeaturec andanordinallabelo,athresholdτ can
6https://huggingface.co/bert-base-uncased
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:15
Fig.8. AnillustrationonAmazonReviewCdatasetwithincrementalconceptdrift.
be created to convert the task to binary classification, where label= 0 ifo ≤ τ while label= 1 if
o >τ.Bychangingthethresholdτ fromsmalltolargebetweenconsecutivebatches,datainstances
withincrementalP(y|X)driftscanbegenerated.Inthemeanwhile,sincedatainstanceswithvar-
ious values of a certain categorical feature tend to exhibit different distributions,P(X) drifts on
instancescanbeproducedthroughthecategoricalfeaturec.Weconfineeachdatabatchtocon-
tain data instances belonging to a specific value of categorical featurec. Note that any existing
datasetwithacategoricalfeatureandanordinallabelcanbeusedinthesamewaytocreateanew
datasetwithincrementalconceptdrift.
Similarly, we create the Amazon Review Concept Drift dataset (Amazon Review C) from the
Amazon Review Dataset [32]. In addition to adjusting the thresholdτ between data batches to
createP(y|X)drifts,wecreateP(X)driftsbychangingthereviewcategories,i.e.,ArtCraft,Digital
Music,LawnandGarden,andSoftwareindifferentbatches.Datainstanceswithdifferentreview
categoriesareassignedtodifferentbatches.Eventually,wecanproducefourbatchesB ,B ,B ,B
0 1 2 3
forthedriftofP(X),andeachofwhichhasitsownthresholdτ thatdeterminesthedriftofP(y|X).
Figure8providesanillustrationofhowincrementalconceptdrifthappensonreviewembeddings
amongdatabatchesatdifferenttimestamps.
4.4 EvaluationonIncrementalDrift
We aim at examining whether or not the four generated datasets do contain incremental drifts.
Weexpectthatifthedatacontainsincrementaldrifts,alearner’spredictionperformancewillbe
diminishedwhenshiftingfromonebatchtoanother.Toconstructtheevaluation,wefinetunea
baseneuralnetworkmodelthatistrainedoneachtrainingbatchoverafixednumberofepochs
(50forthefirstdataset,and30fortheremainingthreedatasets).Wheneachtrainingepochisdone,
thelearneristestedonthetestsetofthatbatch.Notethatthedetailedmodelconfigurationand
experimentalsettingsarepresentedinSection6.1.Theperformancescoresintermsofclassifica-
tionaccuracyoverallepochsinthefourgenerateddatasetsarereportedinFigure9.Wecansee
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:16 Y.-T.Paietal.
Fig.9. Finetuningaccuracy(y-axis)vs.thetrainingepochnumber(x-axis)onthefourdatasets(fromtopto
down):Agingdataset(50),Posedataset(30),AmazonReviewA(30),andAmazonReviewC(30),wherethe
numberinthebracketisthenumberofepochsperbatch.Inthelegend,thenumberfrom0to3or4refers
tobatchesB 0,B 1,...,B 3orB 4.Forexample,theredcurveshowstheaccuracyvaluesreportedfromtraining
onthefirstbatchB 0overepochs.
thatoncethelearnermovesfromonebatchtothenextone,ineverydataset,theaccuracyvalues
show significant drops. It is becausethe learner moves to train on the next batch with a drifted
concept,causingthegradualforgettingofthepreviousbatch’sconcept.Suchresultsindicatethat
incrementaldriftsexistamongbatchesinthefourgenerateddatasets.
Note that our intention behind employing GANs to synthesize datasets was to create a con-
trolledexperimentalenvironmentwherewecouldmeticulouslymodulatethedriftcharacteristics,
therebyfacilitatinganuancedexplorationofthealgorithmsunderdistinctincrementaldriftsce-
narios.Itisalsopertinenttonotethatwhileourproposeddatasetsdemonstrateevidentshiftsand
complexities,theperennialchallengeremainsthatnosyntheticdatasetcanwhollyencapsulatethe
multifacetednatureofreal-worlddrifts.Consequently,whilewearguethatourdatasets,generated
with considered applications of GANs, present a significant step forward in approximating real-
worldcomplexities,weconcedeandunderscorethattheyarenotanexhaustiverepresentationof
allpossiblereal-worldscenarios.Nonetheless,wepositthattheyserveasavaluabletoolinbridg-
ingthegapbetweenconventionalsyntheticdatasetsandtheunpredictableintricaciesobservedin
real-worldapplications.
5 MODELCOMPARISON
Givenadatasetwithincrementaldatadrifts,weaimtoinvestigatehowrecentadvancesinknowl-
edge transfer between domains/tasks can be adopted for the predictions. We find that Domain
Adaptation[47]andLifelongLearning[8]arethetwomostrelevantapproachestomodelincremen-
taldatadrifting.Bothapproachescandealwithlearningknowledgefromatask/domainandhav-
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:17
Fig. 10. Elaboration of domain adaptation and lifelong learning for incremental data drifting. Domain-
adaptationmethodstrainonbothlabeleddatainbatchk−1andunlabeleddatainbatchk,andpredicton
unlabeleddatainbatchk.Lifelonglearningtrainsonallpreviouslylabeleddatainbatches0,1,...,k −1
andpredictonunlabeleddatainbatchk.
ingittransferredtoanothertask/domain,andwecantreatthepredictionsonthedriftedbatches
assequentialtaskswithdomainshifts.WealsostudyhowwellcanthemethodsonConceptDrift
Adaption[15]beutilizedtomakepredictionsonincrementaldatadrifting.
5.1 DomainAdaptation
Domain adaptation deals with the prediction task, in which datasets are collected from two do-
mainswithdifferentdistributions,i.e.,thesourcedomainandthetargetdomain.Itaimsattransfer-
ringknowledgelearnedfromthesourcedomaintothetargetdomainthroughadversarialtraining.
AsshowninFigure10(a),alearneristrainedandadaptedtoanunlabeledtargetdomainleverag-
ingbothlabeleddatainthesourcedomainandunlabeleddatainthetargetdomain.Sincedomain
adaptationiscapableofhandlingfeaturediscrepancies,itprovidessomepotentialtodealwithnew
conceptswithincrementalcovariatedrifts.Bytreatingsourceandtargetdomainsasconsecutive
batchesB k−1 andB k,weareallowedtoseamlesslyexploitdomainadaptationmethodstotackle
incrementaldatadrifting.Belowwecomparethreetypicalmethodsofdomainadaptation.
—DANN: Domain-Adversarial Neural Network (DANN)7 [16] achieves domain adapta-
tionbygeneratingfeaturesthatcannotbetoldfromsourcetotargetdomain.Inadditionto
minimizingthelabelpredictionlossforsource-domaindata,DANNminimizesthedomain
classificationlossforallinstancesandproducesdomain-invariantfeaturesbyagradientre-
versallayer,whichensuresthatthefeaturedistributionsovertwodomainsaremadesimilar.
—MCD: Maximum Classifier Discrepancy (MCD)8 [36] is an unsupervised domain
adaptationalgorithmthatconsiderstask-specificdecisionboundariesbetweenclasses.The
adversarialtrainingmodelconsistsofafeaturegeneratorandtwolabelclassifiers.Bymax-
imizingthediscrepancybetweentwoclassifiersontarget-domainsamples,andgenerating
latentfeaturesthatminimizethediscrepancy,MCDalignssource-andtarget-domaindata
distributions.
—GST: Gradual Self-Training (GST)9 [27] focuses on data that the domain shift happens
gradually. The goal is to adopt an initial classifier trained on the labeled source domain
7https://github.com/fungtion/DANN
8https://github.com/mil-tokyo/MCD_DA
9https://github.com/p-lambda/gradual_domain_adaptation
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:18 Y.-T.Paietal.
given unlabeled intermediate domains that shift gradually in distribution towards an
unlabeled target domain. GST utilizes self-training to model gradual shift. The classifier
first generates pseudo-labels for the successive domain. High-confident pseudo-labeled
samplesareconsideredtotrainaregularizedsupervisedclassifier.Byiteratingthisprocess
whenintermediate-domaindataarrives,GSTcangraduallyadapttothefinaltargetdomain.
HereweapplyGSTeverytimeanewdatabatcharrives.
—ARM:AdaptiveRiskMinimization(ARM)10[51]offersanovelapproachinthedomain
generalization problem setting, where training data is categorized into domains, and
potential test-time shifts into new domains or domain distributions are anticipated. ARM
createsmodelsthatcanadaptduringtesttimetodomainshifts,usingunlabeledtestpoints.
ARM aims to optimize the model to proficiently utilize the unlabeled adaptation phase to
managedomainshiftsbymeta-learninganadaptablemodelfromasetoftrainingdomains
that correspond to training batches in our setting. Similarly, we apply ARM every time a
newdatabatcharrives.
5.2 LifelongLearning
Lifelonglearningisperformedonasequenceoftaskswhosedatadistributionschangedarepre-
sentedchronologically.AsillustratedinFigure10(b),alifelonglearnerneedstodoaccuratepre-
dictionsonthenewtask(ondatabatchB k)whilelearningandmaintainingtheperformanceon
historicaltasks(onB 0 ,...,B k−1 ),giventhatonlyalimitedamountofpreviouslyseendatabatches
andmodelscanbesaved.Anextremedecreaseinperformanceonoldtasksiscalledcatastrophic
forgetting.Sincelifelonglearningcaneffectivelymitigatecatastrophicforgetting,itisexpectedto
memorize all historical knowledge with covariate drifts. By regarding tasks with historically la-
beleddataassequentialtrainingbatches,andthenexttaskasthetargetbatchB k beingpredicted,
lifelonglearningcanbeaproperapproachtodealwithincrementaldatadrifting.Weexperimen-
tallycomparetwotypicallifelonglearningmethods.
—EWC:ElasticWeightConsolidation(EWC)11[25]preventscatastrophicforgettinginthe
settingoflifelonglearningbyflexiblydecreasingthelearningoncertainweightsaccording
tohowtheypositivelycontributetohistoricaltasks.EWCdevisesanovelregularizationterm
thatcanreflecttheimportanceofeverysinglemodelparameterlearnedfromhistoricaltasks,
andpenalizetheweightupdatesthatattempttomodifyimportantparameters.PuttingEWC
tothelearningwithincrementaldriftdataisexpectedtoeffectivelymaintaintheknowledge
learnedfromobservedbatches.
—GEM:GradientEpisodicMemory(GEM)12[29]mitigatescatastrophicforgettingbymain-
taining an episodic memory that stores a subset of the observed instances from historical
data. By computing the inner product between the loss gradient vector of the data in the
memoryandthecurrentupdatederivedfromnewdata,GEMcandiagnosewhethertheloss
athistoricaltasksisincreased.Ifitis,GEMfindsanalternativegradientwhoseparameter
updateisunlikelytohurttheperformanceonpasttasks,leadingtomaintainingpastlearned
knowledge.
5.3 ConceptDriftAdaptation
The adaptive approach to handling concept drifts is a kind of incremental learning that is able
toadapttotheevolutionofthedatagenerationprocessovertime.Thepredictivemodelsupdate
10https://github.com/henrikmarklund/arm
11https://github.com/ariseff/overcoming-catastrophic
12https://github.com/facebookresearch/GradientEpisodicMemory
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:19
onlineduringtheiroperationstoreacttoconceptdrifts.Whentostarttheadaptiveprocessand
how to deal with the changes are two essential issues. For the first issue, one can blindly and
regularlytriggertheadaptiveprocesswithoutknowingwhentheconceptdrifthappens[42],e.g.,
re-trainingthemodeleveryday.Anothermethodistostarttheadaptiveprocesswhentheconcept
driftisdetectedbythedriftdetectionsystem[41].Asforthesecondissue,astraightforwardway
is to retrain a new model with the newest data. The model ensemble is also a popular method
tomitigateperformancedecaycausedbyconceptdrift.Anewmodelistrainedandaddedtothe
ensemble,andtheoldmodelwiththeworstperformanceonthenewestdataisremoved[10].Given
thatourdatasettingisbatch-wiseandrequiresnodriftdetection,weconsiderthefollowingtypical
conceptdriftadaptationmethod.
—Learn ++ .NSE:Learn ++ .NSE(LNSE)13[10]isamodelensemblemethod,inwhichclassifiers
aretrainedondifferentdatabatches.Anewclassifieristrainedonthelatestdatabatchif
theerrorrateofthepreviousclassifierintheensembleexceeds0.5.Inaddition,dynamically
weighted majority voting is applied based on the performance of the latest data of each
classifier.
6 EXPERIMENTALEVALUATION
Weanswersixquestions.(1)Whichapproachesamongdomainadaptation,lifelonglearning,and
conceptdriftadaptationperformbetter?(2)Candomainadaptationmethodsperformwellwhen
new data arrives? (3) Will domain adaptation methods decrease their performance on Old data
whentheytrytoaligndomaindrifts?(4)Canlifelonglearningmethodsperformwellonhistorical
data?(5)Willlifelonglearningmethodsperformbettergiventhattheycanalleviatecatastrophic
forgetting?(6)Howdodifferentapproachesperformonrealconceptdriftdatasets?
6.1 ExperimentalSettings
Baselines.Weconsiderthreebaselinesthatdonothandledrifting.
—Finetune: The model is sequentially trained on the immediately previous data batch and
fine-tuned on the current batch without any advanced knowledge-transfer techniques ap-
plied. Methods belonging to either domain adaptation or lifelong learning can have such
finetuningversions.
—Joint: The model is trained using a part of historical data instances stored before the pre-
dictionbatch.Forafaircomparison,weusethesameamountofdataasthememorysizein
GEM[29]tocreatetheJointmodel.
—Joint-full: The model is trained on all of historical data instances. All instances in past
batchesareusedsimultaneouslytotrainthemodel.Therefore,Joint-fullcanbeseenasan
upperbound forLifelongLearningmethods.
Notethatonemayquestionhowbatch-wisedataissignificantlydifferentfromadatastream.
Anaivesolutionthroughupdatingthemodelwiththemeanofthegradientofthebatchshould
workforbatch-wisedata.Infact,suchanaivesolutionisanalogizedwiththe“Finetune”baseline
thatweincludedforcomparisonanddiscussion.ThisFinetuneapproachwasadoptedtoensurea
balancedandrigorousanalysis,accountingforbothconventionalandalternativemethodologies
inmanagingbatch-wisedataamidstconceptdrift.
DatasetsandSplittings.Weusethefourgenerateddatasets,Aging,Pose,AmazonReviewA,
andAmazonReviewC,aspresentedinTable3.Tounderstandhowwelldifferentapproachescan
beutilizedtoreal-worldconceptdrifts,wefurtherruntheexperimentsontworealdatasets,Gas
13https://github.com/gditzler/IncrementalLearning
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:20 Y.-T.Paietal.
Table4. SummaryoftheTwoRealDatasets
#data #feature #Class #batch #dataperbatch train:val:test
GasSensorArray 13,910 128 6 10 variantbytime 8:1:1
ForestCovertype 581,012 54 7 7 83000 8:1:1
SensorArrayDriftdataset14 [12]andForestCovertypedataset15 [3],whosestatisticsisprovided
in Table 4. In the generation of each synthetic dataset and in the experiments, each data batch
containsnotonlyavalidationset,whichisusedformodelselection,butalsoatestsettodisplay
finalperformance.Theideabehindsuchkindofdatasplittingistodividethedataineachdistri-
butionintovalidationandtest,assumingtheaccesstoasmallvalidationsetthatsharesthesame
distributionwiththetest.Thisapproachallowsforrobustmodeltraining,hyperparametertuning,
andeventualevaluationofthemodel’sgeneralizationperformanceofincrementaldatadrifting.
Base Learner Settings. For a fair comparison, the same neural network architecture is used
asthebaselearnerforallcomparedmethodsrunningunderthesamedataset.Iftheinputdatais
the image, a typical 4-layer convolutional neural network channeled 3-32-64-128 is used. As for
tabular data, we employ a multi-layer perceptron with 4 hidden layers of 64 neurons each. We
adddropoutwith0.2probabilitytoeachlayer.TheactivationfunctionReLUisusedinallhidden
layers.WeuseAdam[24]tooptimizeallmodels.Allmethodsusethestandardcross-entropyloss
fortheclassificationtasks.
Model Selection. The ways to tune hyperparameters of all comparing methods in domain
adaptation(DA),lifelonglearning(LL),andconceptdriftadaptation(CDA)followthere-
spective studies unless further specification. We perform model selection with hyperparameter
tuningusingthevalidationsetwithineachdatabatch.InDANN,Thedomainadaptationparam-
eterλ (the trade-off between the prediction loss and the negative of the domain loss) is defined
asfollows:λ p = 1+e 2 −10p −1,wherep isthetrainingsteplinearlychangingfrom0to1.InMCD,
the number of times to repeat the process of minimizing the discrepancy loss is tuned within
{1,3,5,7}.InEWC,thescalingfactor,whichreflectstheimportanceoftheoldtask,tohavebet-
ter performance, is tuned within {800,1200,1800,2400,...,4800}. For GEM and Joint, a subset
of instances in each historical batch is randomly sampled and stored with a ratio α. We tune
α = {0.025,0.05,0.075,0.1}. Note that the number of instances per batch varies in Gas Sensor
ArrayDriftdatasetbecausebatchesaredeterminedaccordingtofixedtimeperiods.Wedefinen
s
as the size of the smallest data batch, and the actual number of instances to be stored for each
batchisn
s
×α.
EvaluationMetrics.WeutilizethemetricsdescribedinSection3,includingOldTransferand
NewTransfer.Sincebothrequirebaselinestohaverelativeperformancescores,hereweconsider
Finetuneasthebaselinelearner.Notethatthisiswhythescoresofsuchtwocriteriain“finetune”
rowsintheresultanttablesshow0acrossalldatasets.Wereporttheaverageresultsonthetest
setsovertendifferentseeds,alongwiththestandarddeviation.
6.2 ResultsandDiscussion
Covariate Drift. The results for incremental covariate drift on the generated Aging and Post
datasets are shown in Tables 5 and 6. We find out that when covariate drift happens, lifelong
learning-based algorithms succeed in preserving the knowledge in old data. Therefore, they
are proven to be effective when handling situations where old concepts reoccur in the future.
14https://archive.ics.uci.edu/ml/datasets/gas+sensor+array+drift+dataset
15https://archive.ics.uci.edu/ml/datasets/covertype
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:21
Table5. ResultsontheAgingDataset
|                   | Old         | New          |
| ----------------- | ----------- | ------------ |
| Baseline finetune | 0.0000±0.00 | 0.0000±0.00  |
| joint             | 0.0310±0.03 | 0.0018±0.01  |
|                   | 0.0908±0.08 | −0.0227±0.02 |
joint-full
| LL GEM | 0.0370±0.03 | −0.0078±0.02 |
| ------ | ----------- | ------------ |
|        | 0.0231±0.04 | −0.0168±0.03 |
EWC
| DA MCD | −0.0147±0.03 | 0.0220±0.01 |
| ------ | ------------ | ----------- |
|        | 0.0025±0.03  | 0.0038±0.02 |
DANN
|     | −0.0185±0.01 | 0.0033±0.02 |
| --- | ------------ | ----------- |
GST
| ARM      | 0.0032±0.02  | 0.0079±0.02  |
| -------- | ------------ | ------------ |
|          | −0.1763±0.08 | −0.2309±0.04 |
| CDA LNSE |              |              |
Table6. ResultsonthePoseDataset
|                   | Old          | New          |
| ----------------- | ------------ | ------------ |
| Baseline finetune | 0.0000±0.000 | 0.0000±0.000 |
|                   | 0.0099±0.013 | 0.0043±0.009 |
joint
| joint-full | 0.0212±0.017 | −0.0057±0.013 |
| ---------- | ------------ | ------------- |
|            | 0.0126±0.009 | 0.0058±0.010  |
| LL GEM     |              |               |
|            | 0.0107±0.011 | −0.0061±0.008 |
EWC
| DA MCD | −0.0377±0.026 | 0.0199±0.009 |
| ------ | ------------- | ------------ |
|        | −0.0175±0.015 | 0.0208±0.010 |
DANN
| GST | −0.0063±0.010 | 0.0012±0.009 |
| --- | ------------- | ------------ |
|     | 0.0002±0.012  | 0.0314±0.008 |
ARM
| CD LNSE | −0.3054±0.044 | −0.2271±0.051 |
| ------- | ------------- | ------------- |
Furthermore,GEMconsistentlyoutperformsjointtraininginOldTransfer,giventhattheyboth
storethesameamountofolddata.However,bothGEMandEWChaveverylimitedimprovements
incovariatedriftinNewTransfer.EWCaggravatesmorewhenintransigencehappens.Thereason
forthisdifferenceisbecauseoftheinnateshiftoffeaturespaceincovariatedriftingdata;asdata
keepexploringnewspaceswithoutoverlaps,theburdensofmitigatingdatadiscrepanciesbymod-
elsincrease.Suchaweakadaptationtounseencovariatedriftdataisespeciallyobviousforlifelong
learningmodelsbecausetheycannotutilizeanyunlabeleddatainthebatchbeingpredicted.
On the other hand, all domain adaptation methods perform well on New Transfer measured
forincrementalcovariatedrift,asexhibitedinTables5and6.Theysucceedinaligningunlabeled
datashiftinginthefeaturedomain.Tobemorespecific,MCDisslightlybetterthanDANNand
ARM since it not only aligns the feature spaces but also considers the potential differences in
decisionboundariesbetweendomains/batches.AlthoughGSTandARMalsoperformbetterthan
lifelonglearning-basedmethodsonNewTransfermostly,ithaslimitedeffectcomparedwithother
domainadaptationmethodsbecausethedegreeofgradualdriftisnotlargeenoughinthegenerated
datasets.Inotherwords,GSTandARMonlyperformwellondatathatdriftveryslowly.Wealso
find out that all domain adaptation-based methods suffer from performance degradation in Old
Transfer. A possible reason for this is that when feature spaces are continually adapted, models
areguidedawayfromtheoldconceptswhileinmeanwhilemodelspaymuchattentiontonewer
conceptsandunlabeleddatainthebatchbeingpredicted.
ActualDrift.WereporttheresultsonincrementalactualdriftusingthegeneratedAmazonRe-
viewAdatasetinTable7.Wecanfindthatonlifelonglearningmethods,GEMperformswellwhile
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:22 Y.-T.Paietal.
Table7. ResultsontheAmazonActualDriftDataset
|                   | Old          | New           |
| ----------------- | ------------ | ------------- |
| Baseline finetune | 0.0000±0.000 | 0.0000±0.000  |
| joint             | 0.0264±0.014 | −0.0028±0.011 |
|                   | 0.0950±0.042 | −0.0618±0.058 |
joint-full
| LL GEM | 0.0283±0.020 | −0.0049±0.013 |
| ------ | ------------ | ------------- |
|        | 0.0069±0.014 | 0.0047±0.008  |
EWC
| DA MCD | 0.0180±0.009 | −0.0005±0.011 |
| ------ | ------------ | ------------- |
|        | 0.0013±0.018 | 0.0025±0.014  |
DANN
|     | −0.0202±0.020 | 0.0133±0.020 |
| --- | ------------- | ------------ |
GST
| ARM | 0.0057±0.017  | 0.0097±0.014  |
| --- | ------------- | ------------- |
|     | −0.0216±0.094 | −0.2005±0.088 |
CDA LNSE
EWCshowsanobviousdecline.InthecomparisonbetweenGEMandjointtraining,GEMstillob-
tains better performance given that they both use the same amount of storage to store old data.
ThishelpsuscometotheinsightthatGEMisbetteratpreservingoldconceptswhenincremental
actualdrifthappens.Ontheotherhand,alldomainadaptationmethodsfailintacklingincremental
actualdriftexceptgradualself-training.Consistentwiththeinnatedesignofthesemethods,they
showed no improvement when drifts only happened in decision boundaries rather than the fea-
turespaces.Thishighlightsthelimitationsofthedomainadaptationmethods:althoughalltypes
ofdatadriftingcauseperformancedecline,theycomeintoeffectonlywhenthedriftshappenon
P(X).Interestingly,GSTandARMobtainthebestperformanceintacklingincrementalactualdrift.
Wethinkdatalyinginthedriftregionmaybefilteredoutbecauseofthelowpredictionconfidence.
Therefore,itmaybefeasibletoobtainabetterdecisionboundaryafterretrainingontheremaining
pseudo-labeledsamples,bringingbetterperformanceinpredictingthenextconcepts.
Concept Drift. Table 8 exhibits the results of evaluating incremental concept drift based on
the generated Amazon Concept Drift dataset. We can find that lifelong learning-based methods,
in particular GEM, can successfully preserve old concepts. However, it also causes serious per-
formancedegradationinNewTransfer.Wespeculatethatthisisbecauseofthecontradictionin
decisionboundariesbetweendatabatches.Lifelonglearningapproachesarehardtoforeseeand
adapttothedrifteddecisionboundariesinthetestingbatch.Also,thebetteralifelonglearning-
based method is in Old Transfer, the worse it is in New Transfer. On the other hand, domain
adaptation-based methods, again, fail in New Transfer. Moreover, MCD and ARM decline even
more in incremental concept drift, compared to incremental actual drift. We consider this hap-
peningduetothefalsedecisionboundariesMCDandARMlearnedwhiletryingtoalignfeature
spaces. Gradual self-training also fails because the drift of the data feature space is not gradual
enough.
Real Data Drift. We present the results on real-world incremental data drifting in Tables 9
and10.Wefindthatlifelonglearning-basedmethodsleadtopromisingperformanceonbothold
andnewtransfers.InthecaseofGasSensordata,GEMnearlyreachestheperformance’supper
bound(i.e.,joint-full).Ontheotherhand,whileMCDhassomesuccessinForestCovertypedata,
theimprovementsthatlifelonglearningmethodsmakearemoresignificant.Thisisbecausethat
new data come in a mixture of old data. Therefore, having old data memorized helps a learner
to perform well when it recurs. This also highlights the importance of generating incremental
datasets with different specific drift types. Only the old transfer and new transfer evaluated on
incrementalchangeddatacanrevealalearner’strueabilitiestopreventforgettingandbeingable
toadaptforwardatthesametime.
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:23
Table8. ResultsontheAmazonConceptDriftDataset
|                   | Old          | New           |
| ----------------- | ------------ | ------------- |
| Baseline finetune | 0.0000±0.000 | 0.0000±0.000  |
| joint             | 0.0611±0.034 | −0.0498±0.054 |
|                   | 0.0864±0.063 | −0.0660±0.057 |
joint-full
| LL GEM | 0.0630±0.045  | −0.0579±0.048 |
| ------ | ------------- | ------------- |
|        | −0.0011±0.012 | −0.0069±0.014 |
EWC
| DA MCD | 0.0456±0.077 | −0.0860±0.122 |
| ------ | ------------ | ------------- |
|        | 0.0318±0.040 | −0.0071±0.042 |
DANN
|     | −0.0609±0.024 | −0.0193±0.026 |
| --- | ------------- | ------------- |
GST
| ARM                                         | 0.0494±0.028  | −0.0037±0.025 |
| ------------------------------------------- | ------------- | ------------- |
|                                             | −0.1271±0.159 | −0.2184±0.059 |
| CDA LNSE                                    |               |               |
| Table9. ResultsonGasSensorArrayDriftDataset |               |               |
|                                             | Old           | New           |
| Baseline finetune                           | 0.0000±0.000  | 0.0000±0.000  |
|                                             | 0.1413±0.113  | 0.0428±0.091  |
joint
| joint-full | 0.1882±0.130 | 0.0478±0.100 |
| ---------- | ------------ | ------------ |
|            | 0.1675±0.097 | 0.0362±0.085 |
| LL GEM     |              |              |
|            | 0.0580±0.077 | 0.0044±0.061 |
EWC
| DA MCD | −0.0241±0.088 | 0.0047±0.084  |
| ------ | ------------- | ------------- |
|        | −0.0135±0.060 | −0.0123±0.120 |
DANN
| GST | −0.0101±0.067 | −0.0438±0.079 |
| --- | ------------- | ------------- |
|     | −0.0076±0.057 | −0.0070±0.076 |
ARM
| CDA LNSE                                 | −0.4270±0.181 | −0.4290±0.143 |
| ---------------------------------------- | ------------- | ------------- |
| Table10. ResultsonForestCovertypeDataset |               |               |
|                                          | Old           | New           |
| Baseline finetune                        | 0.0000±0.000  | 0.0000±0.000  |
|                                          | 0.1586±0.098  | −0.0019±0.024 |
joint
| joint-full | 0.3855±0.090  | 0.1008±0.055  |
| ---------- | ------------- | ------------- |
|            | 0.1785±0.086  | −0.0042±0.023 |
| LL GEM     |               |               |
| EWC        | 0.1131±0.073  | 0.0358±0.020  |
|            | −0.1098±0.091 | 0.0117±0.023  |
| DA MCD     |               |               |
|            | −0.1280±0.100 | −0.0652±0.033 |
DANN
| GST | −0.0363±0.098 | 0.0299±0.027 |
| --- | ------------- | ------------ |
|     | −0.0193±0.093 | 0.0160±0.022 |
ARM
| CDA LNSE | −0.1114±0.146 | −0.0664±0.045 |
| -------- | ------------- | ------------- |
7 CONCLUSIONSANDDISCUSSION
In this work, we highlight and tackle the problem of incremental data drifting under covariate,
actual,andconcepttypes.Whileexistingstudiestargetinstance-wisedatastreams,cannotprop-
erlyevaluatemodelsonknowledgetransfer,donotworkonspecificdriftingdatasets,andhave
notinvestigatedadvancedlearningapproaches,weprovidethefirstholisticattemptforlearning
withincrementaldriftinginthebatch-wisedatasetting.Weproposetwonovelmetrics,oldand
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:24 Y.-T.Paietal.
new transfer, to properly and robustly reflect the goodness of knowledge transfer between data
batches.Wealsoproposefeature-basedandGAN-basedmechanismstogeneratesyntheticincre-
mentaldriftingtabularandimagedatasetswithexplicitdrifttypes.Byproperlyaligningthetasks
betweenthetechniquesfordomainadaptationandlifelonglearninginthescopeofincremental
data drifting, we experimentally compare their performance. We obtain insights that depict the
underlyingrelationshipsamongdriftingtypes,knowledgepreservation,andlearningapproaches.
First,thelifelonglearningapproach,especiallyGEM,isgoodatpreservingoldknowledgeinall
kinds of datasets and across drift types, but fails in adapting to unseen new data. Second, the
domainadaptationapproachworkswellonadaptingconceptshifttothenextdatabatchinincre-
mentalcovariatedrift,buthurtstheperformanceinallotherdrifttypesasitalignsonlyfeature
spaces based on unlabeled data. Third, adapting to unseen data with incremental concept drift
is the most challenging because both feature and label spaces are shifted, and thus none of do-
mainadaptationandlifelonglearningmethodscanworkwell.Fourth,whenfacingconceptdrift
inrealdata,thelifelonglearningapproachisabetterchoiceforbothpreservingoldknowledge
andadaptingtonewknowledge.
In this work, we only evaluate the performance of domain adaptation and lifelong learning
methods in the presence of incremental data drifting. There is the potential to devise a novel
method to tackle the issue of incremental data drifting. Indeed, the conundrum of incremental
datadriftingposesaninterestingchallengeindynamiclearningenvironments.Incrementaldata
drift typically exhibits a certain regularity and exploring this regularity can potentially forge a
path towards proactively predicting future data concepts, thereby offering a viable strategy to
navigatethroughtheissuesposedbyincrementaldatadrifting.Takingactualdriftasanexample,
thisregularitycanbediscernedbyunderstandingthevariationsintheclassdistributionofeach
data point across previous time instances. This suggests that for a data batch arriving at timet,
wemighttrainamodelusingtheclassdistributionsfromthepastm timepoints(t −m tot −1)
asinput,andtheclassdistributionatthecurrenttimepointt asthelabel.Bydoingso,duringthe
inferencestage,wecouldshifttheinputwindowbyonetimeunittoconsiderclassdistributions
fromt−m+1tot,enablingthemodeltopredicttheinstance’sclassdistributionattimet+1and,
potentially,estimatetheconceptatt +1.
Obtainingtheclassdistributionofaparticularinstanceatvarioustimepointsmightbeachieved
byperforminginferenceusingclassifierstrainedateachrespectivetimepoint.Thiscreatesaloop
ofcontinuousadaptationandlearning,whereinthemodelnotonlylearnsfromthedriftingdata
butalsopredictssubsequentdrifts,therebypreparingitselftoadjusttofutureshifts.Thissystem-
aticmethodensuresthatthemodelisnotonlyreactivebutalsoproactiveinitsapproachtowards
handling incremental data drifting, potentially reducing the lag between the occurrence of drift
and the model’s adaptation to it, and thus maintaining a robust predictive performance despite
thedynamicdatalandscape.It’sworthnotingthatthisproposedmethodwouldnecessitatethor-
oughempiricalvalidationtoascertainitseffectivenessandapplicabilityacrossdiversedatadrift
scenarios.Andcertainly,thisexplorationcanfurtherenrichthediscourseintherealmofhandling
incrementaldatadrift.
REFERENCES
[1] Martin Arjovsky, Léon Bottou, Ishaan Gulrajani, and David Lopez-Paz. 2019. Invariant risk minimization. arXiv
preprintarXiv:1907.02893(2019).
[2] ManuelBaena-García,JoséCampo-Ávila,RaúlFidalgo-Merino,AlbertBifet,RicardGavald,andRafaelMorales-Bueno.
2006.Earlydriftdetectionmethod.(012006).
[3] J. Blackard and D. Dean. 1999. Comparative accuracies of artificial neural networks and discriminant analysis
in predicting forest cover types from cartographic variables. Computers and Electronics in Agriculture 24 (1999),
131–151.
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

IncrementalDataDrifting 71:25
[4] AndrewBrock,JeffDonahue,andKarenSimonyan.2019.LargescaleGANtrainingforhighfidelitynaturalimage
synthesis.InInternationalConferenceonLearningRepresentations(ICLR’19).
[5] AlbertoCanoandBartoszKrawczyk.2020.Kappaupdatedensemblefordriftingdatastreammining.MachineLearning
109(012020),175–218.
[6] ElliotCreager,Jörn-HenrikJacobsen,andRichardZemel.2021.Environmentinferenceforinvariantlearning.InIn-
ternationalConferenceonMachineLearning.PMLR,2189–2200.
[7] GabrielaCsurka.2017.DomainAdaptationinComputerVisionApplications.Springer.
[8] MatthiasDeLange,RahafAljundi,MarcMasana,SarahParisot,XuJia,AlesLeonardis,GregorySlabaugh,andTinne
Tuytelaars.2022.Acontinuallearningsurvey:Defyingforgettinginclassificationtasks.IEEETransactionsonPattern
AnalysisandMachineIntelligence44,7(2022),3366–3385.
[9] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova.2019.BERT:Pre-trainingofdeepbidirectional
transformersforlanguageunderstanding.InProceedingsofthe2019ConferenceoftheNorthAmericanChapterofthe
AssociationforComputationalLinguistics:HumanLanguageTechnologies.4171–4186.
[10] RyanElwellandRobiPolikar.2011.Incrementallearningofconceptdriftinnonstationaryenvironments.IEEETrans.
NeuralNetworks22,10(2011),1517–1531.
[11] WeiFan.2004.Systematicdataselectiontomineconcept-driftingdatastreams.InProceedingsoftheTenthACM
SIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.128–137.
[12] JordiFonollosa,IreneRodríguez-Luján,andRamónHuerta.2015.Chemicalgassensorarraydataset.DatainBrief 3
(2015),85–89.
[13] JoãoGama,PedroMedas,GladysCastillo,andPedroRodrigues.2004.Learningwithdriftdetection.IntelligentData
Analysis8,286–295.
[14] JoáoGama,Indre˙Žliobaite˙,AlbertBifet,MykolaPechenizkiy,andAbdelhamidBouchachia.2014.Asurveyonconcept
driftadaptation.ACMComput.Surv.46,4(2014),1–37.
[15] JoãoGama,IndrundefinedŽliobaitundefined,AlbertBifet,MykolaPechenizkiy,andAbdelhamidBouchachia.2014.A
surveyonconceptdriftadaptation.ACMComput.Surv.46,4,Article44(2014).
[16] YaroslavGanin,E.Ustinova,HanaAjakan,PascalGermain,H.Larochelle,FrançoisLaviolette,M.Marchand,and
V.Lempitsky.2016.Domain-adversarialtrainingofneuralnetworks.J.Mach.Learn.Res.17(2016),59:1–59:35.
[17] HeitorMuriloGomes,JeanPaulBarddal,FabrícioEnembreck,andAlbertBifet.2017.Asurveyonensemblelearning
fordatastreamclassification.ACMComput.Surv.50,2(Mar.2017),1–36.
[18] Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville,
andYoshuaBengio.2014.GenerativeadversarialNetworks.InAdvancesinNeuralInformationProcessingSystems
(NeurIPS’14).
[19] RuochengGuo,PengchuanZhang,HaoLiu,andEmreKiciman.2021.Out-of-distributionpredictionwithinvariant
riskminimization:Thelimitationandaneffectivefix.arXivpreprintarXiv:2101.07732(2021).
[20] XianyanJia,ShutaoSong,WeiHe,YangzihaoWang,HaidongRong,FeihuZhou,LiqiangXie,ZhenyuGuo,Yuanzhou
Yang,LiweiYu,TiegangChen,GuangxiaoHu,ShaohuaiShi,andXiaowenChu.2018.Highlyscalabledeeplearning
trainingsystemwithmixed-precision:TrainingImageNetinfourminutes.arXivpreprintarXiv:1807.11205(2018).
[21] TeroKarras,TimoAila,SamuliLaine,andJaakkoLehtinen.2018.ProgressivegrowingofGANsforimprovedquality,
stability,andvariation.InInternationalConferenceonLearningRepresentations(ICLR’18).
[22] TeroKarras,S.Laine,andTimoAila.2019.Astyle-basedgeneratorarchitectureforgenerativeadversarialnetworks.
2019IEEE/CVFConferenceonComputerVisionandPatternRecognition(CVPR)(2019),4396–4405.
[23] IoannisKatakis,GrigoriosTsoumakas,andI.Vlahavas.2010.Trackingrecurringcontextsusingensembleclassifiers:
Anapplicationtoemailfiltering.KnowledgeandInformationSystems22(032010),371–391.
[24] DiederikP.KingmaandJimmyBa.2015.Adam:Amethodforstochasticoptimization.InInternationalConferenceon
LearningRepresentations(ICLR’15).
[25] JamesKirkpatrick,RazvanPascanu,NeilRabinowitz,JoelVeness,GuillaumeDesjardins,AndreiA.Rusu,KieranMilan,
JohnQuan,TiagoRamalho,AgnieszkaGrabska-Barwinska,DemisHassabis,ClaudiaClopath,DharshanKumaran,
andRaiaHadsell.2017.Overcomingcatastrophicforgettinginneuralnetworks.ProceedingsoftheNationalAcademy
ofSciences114,13(2017),3521–3526.
[26] DavidKrueger,EthanCaballero,Joern-HenrikJacobsen,AmyZhang,JonathanBinas,DinghuaiZhang,RemiLePriol,
andAaronCourville.2021.Out-of-distributiongeneralizationviariskextrapolation(rex).InInternationalConference
onMachineLearning.PMLR,5815–5826.
[27] AnanyaKumar,TengyuMa,andPercyLiang.2020.Understandingself-trainingforgradualdomainadaptation.In
Proceedingsofthe37thInternationalConferenceonMachineLearning.5468–5479.
[28] SenLin,LiYang,DeliangFan,andJunshanZhang.2022.TRGP:Trustregiongradientprojectionforcontinuallearning.
InInternationalConferenceonLearningRepresentations.
[29] DavidLopez-PazandMarc'AurelioRanzato.2017.Gradientepisodicmemoryforcontinuallearning.InAdvancesin
NeuralInformationProcessingSystems.
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.

71:26 Y.-T.Paietal.
[30] JieLu,AnjinLiu,FanDong,FengGu,JoáoGama,andGuangquanZhang.2018.Learningunderconceptdrift:A
review.IEEETrans.Knowl.DataEng.31,12(Oct.2018),2346–2363.
[31] DominicMastersandCarloLuschi.2018.Revisitingsmallbatchtrainingfordeepneuralnetworks.arXivpreprint
arXiv:1804.07612(2018).
[32] JianmoNi,JiachengLi,andJulianMcAuley.2019.Justifyingrecommendationsusingdistantly-labeledreviewsand
fine-grained aspects. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing
(EMNLP’19).188–197.
[33] VishalM.Patel,RaghuramanGopalan,RuonanLi,andRamaChellappa.2015.Visualdomainadaptation:Asurveyof
recentadvances.IEEESignalProcess.Mag.32,3(Apr.2015),53–69.
[34] AmandaRiosandLaurentItti.2019.Closed-loopmemoryGANforcontinuallearning.3332–3338.
[35] MohammadRostamiandAramGalstyan.2023.Overcomingconceptshiftindomain-awaresettingsthroughconsoli-
datedinternaldistributions.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.37.9623–9631.
[36] KuniakiSaito,KoheiWatanabe,Y.Ushiku,andT.Harada.2018.Maximumclassifierdiscrepancyforunsupervised
domainadaptation.2018IEEE/CVFConferenceonComputerVisionandPatternRecognition(2018),3723–3732.
[37] YujunShen,CeyuanYang,XiaoouTang,andBoleiZhou.2020.InterFaceGAN:Interpretingthedisentangledface
representationlearnedbyGANs.IEEETransactionsonPatternAnalysisandMachineIntelligencePP(2020).
[38] YujunShenandBoleiZhou.2021.Closed-formfactorizationoflatentsemanticsinGANs.In2021IEEE/CVFConference
onComputerVisionandPatternRecognition(CVPR’21).
[39] HanulShin,JungLee,JaehongKim,andJiwonKim.2017.Continuallearningwithdeepgenerativereplay.(052017).
[40] RuiShu,HungBui,HirokazuNarui,andStefanoErmon.2018.ADIRT-Tapproachtounsuperviseddomainadaptation.
(022018).
[41] YiliaoSong,JieLu,AnjinLiu,HaiyanLu,andGuangquanZhang.2021.Asegment-baseddriftadaptationmethodfor
datastreams.IEEETransactionsonNeuralNetworksandLearningSystems(2021).
[42] YiliaoSong,JieLu,HaiyanLu,andGuangquanZhang.2021.Learningdatastreamswithchangingdistributionsand
temporaldependency.IEEETransactionsonNeuralNetworksandLearningSystems(2021).
[43] W.NickStreetandYongSeogKim.2001.Astreamingensemblealgorithm(SEA)forlarge-scaleclassification.InPro-
ceedingsoftheSeventhACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.377–382.
[44] RishabhTiwari,KrishnatejaKillamsetty,RishabhIyer,andPradeepShenoy.2022.GCR:Gradientcoresetbasedreplay
bufferselectionforcontinuallearning.InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern
Recognition.99–108.
[45] AlexanderVergara,ShankarVembu,TubaAyhan,MargaretA.Ryan,MargieL.Homer,andRamónHuerta.2012.
Chemicalgassensordriftcompensationusingclassifierensembles.SensorsandActuatorsB:Chemical166-167(2012),
320–329.
[46] HaixunWang,WeiFan,PhilipS.Yu,andJiaweiHan.2003.Miningconcept-driftingdatastreamsusingensemble
classifiers.InProceedingsoftheNinthACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandDataMining.
226–235.
[47] MeiWangandWeihongDeng.2018.Deepvisualdomainadaptation:Asurvey.Neurocomputing312(2018),135–153.
[48] ScottWares,JohnIsaacs,andEyadElyan.2019.Datastreammining:Methodsandchallengesforhandlingconcept
drift.SNAppl.Sci.1,11(2019),1–19.
[49] GerhardWidmerandMiroslavKubat.1996.Learninginthepresenceofconceptdriftandhiddencontexts.Mach.
Learn.23,1(Apr.1996),69–101.
[50] LeiXu,MariaSkoularidou,AlfredoCuesta-Infante,andKalyanVeeramachaneni.2019.Modelingtabulardatausing
conditionalGAN.InAdvancesinNeuralInformationProcessingSystems(NeurIPS’19).
[51] MarvinMengxinZhang,HenrikMarklund,NikitaDhawan,AbhishekGupta,SergeyLevine,andChelseaFinn.2021.
Adaptiveriskminimization:Learningtoadapttodomainshift.InAdvancesinNeuralInformationProcessingSystems.
[52] ZhifeiZhang,YangSong,andHairongQi.2017.Ageprogression/regressionbyconditionaladversarialautoencoder.
InIEEEConferenceonComputerVisionandPatternRecognition(CVPR’17).
Received18April2023;revised23January2024;accepted28February2024
ACMTrans.Intell.Syst.Technol.,Vol.15,No.4,Article71.Publicationdate:July2024.