A Framework for Evaluating and Benchmarking Concept Drift
Detection Methods
VitorCerqueira HeitorMuriloGomes MarcoHeyden
UniversityofCoimbra VictoriaUniversityofWellington Commerzbank
Coimbra,Portugal Wellington,NewZealand Frankfurt,Germany
vitorc@dei.uc.pt heitor.gomes@vuw.ac.nz heydenmarco48@gmail.com
BernhardPfahringer AlbertBifet
UniversityofWaikato AIInstitute,UniversityofWaikato
Waikato,NewZealand Waikato,NewZealand
bernhard@cs.waikato.ac.nz albert.bifet@telecom-paris.fr
Abstract ConferenceonKnowledgeDiscoveryandDataMiningV.2(KDD’26),Au-
Datastreamminingisfundamentallychallengedbyconceptdrift, gust09–13,2026,JejuIsland,RepublicofKorea.ACM,NewYork,NY,USA,
12pages.https://doi.org/10.1145/3770855.3819070
wheredistributionalchangescandegrademodelperformance.De-
spitetheproliferationofdriftdetectionmethods,progressinthe
fieldishinderedbyinconsistentevaluationpractices:studiesrely 1 Introduction
onoversimplifiedsyntheticdatagenerators,adoptincompatible
Machinelearningmodelstypicallyrelyontheassumptionthatthe
metrics,andlacktransparencyinhyperparameterselection,mak-
dataencounteredduringinferencefollowsthesamedistribution
ingfaircomparisonsdifficult.Weaddressthisgapwithanovel
asthetrainingdata.However,whenthisdistributionshifts,aphe-
benchmarkingframeworkcomprisingthreecontributions:(1)adrift
nomenonknownasconceptdrift,modelperformancecandegrade
simulationmethodthatinjectscontrolleddistributionalchanges
significantly,leadingtoinaccuratepredictions.Therefore,reliably
into real-world datasets via Monte Carlo trials, enabling super-
detectingandadaptingtoconceptdriftiscrucialformaintaining
visedevaluationwhilepreservingreal-worlddatacomplexity;(2)
theeffectivenessandreliabilityofmachinelearningsystems.
anevaluationprotocolfordriftdetectionwithtiming-awarecrite-
Detectingconceptdrifthaslongbeenrecognizedasacritical
ria,includingthederivationofnewmetrics(e.g.,F1detectionscore,
challengeinmachinelearning,motivatingthedevelopmentofnu-
normalizeddetection time)that arecomparable acrossstreams;
merousdriftdetectionalgorithmsovertheyears.Notableexam-
and(3)weadvocateforaleave-one-dataset-outhyperparameter
plesincludesequentialanalysismethodssuchasCUSUMandthe
optimizationprotocolfordriftdetectionmethodsthatpromotes
Page-Hinkley test [26], control chart-based approaches such as
configurationrobustnessacrossheterogeneousstreamdynamics.
DDM[15]andEDDM[1],andadaptivewindowingmethodssuch
Webenchmark14widelyuseddriftdetectionmethodson7real-
asADWIN[5].Yet,despiteextensiveresearchondriftdetection,
worlddatasetsacross4drifttypes(classprior,labelswap,feature
thereisstillalackofunifiedevaluationpracticesandreproducible
permutation,featurefiltering),eachunderbothabruptandgrad-
baselinesinthefield.Weidentifytwokeysourcesofinconsistency:
ualtransitions.Ourexperimentalresultsprovideinsightsintothe
strengthsandweaknessesofcurrentdriftdetectionapproaches I1. Methodology:Existingstudiesareinconsistentw.r.t.evalu-
whileestablishingbaselineperformancemetricsforfutureresearch ationmetricsandprotocols,hyperparameterselectionstrate-
inthisarea.Allcodeandexperimentsarepubliclyavailable. gies,datasets,anddrifttypes.
I2. Availability of labeled data: Drift points—the times at
CCSConcepts whichconceptdriftsoccurred—aretypicallyunknownin
real-worlddata.Hence,evaluatingadetectoronreal-world
•Computingmethodologies→Onlinelearningsettings;Su-
pervisedlearning.
data must happen unsupervised. This has led to an over-
relianceonsyntheticdataforevaluation.Insyntheticdata,
Keywords
driftpointsareknown,andthusallowforasupervisedeval-
uation.However,syntheticdataandconceptdriftsareoften
ConceptDrift,DataStreams,Benchmarking,Evaluation
unrealistic.Itisthusnotclearwhethertheobtainedresults
ACMReferenceFormat: holdtrueinthereal-world[33,36].This,inturn,callsforan
VitorCerqueira,HeitorMuriloGomes,MarcoHeyden,BernhardPfahringer, evaluationonreal-worlddata.
andAlbertBifet.2026.AFrameworkforEvaluatingandBenchmarking
ConceptDriftDetectionMethods.InProceedingsofthe32ndACMSIGKDD
Theseissuesgiverisetotheresearchquestion:Howcanwereliably
evaluateandcompareconceptdriftdetectionmethodsintheabsence
ofgroundtruthacrossmultipledatastreams?Wetacklethisquestion
andthelimitationsabovewiththefollowingcontributions:
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense.
KDD’26,JejuIsland,RepublicofKorea (1) Adriftsimulationframeworkthatallowsforcontrolled
©2026Copyrightheldbytheowner/author(s). experimentswithdiversetypesofdriftinreal-worlddatasets,
ACMISBN979-8-4007-2259-2/2026/08
https://doi.org/10.1145/3770855.3819070 enablingresearchersandpractitionerstobetterunderstand
6202
nuJ
5
]GL.sc[
1v98770.6062:viXra

KDD’26,August09–13,2026,JejuIsland,RepublicofKorea Cerqueiraetal.
detectorbehaviorindifferentscenarios.Theapproachfol- Conceptdriftscanbecategorizedbydifferenttypesofchange
lowsaMonteCarlosimulationapproachwhereateachrun inthedistribution.Changesin𝑝(𝑋),termedvirtualdrift(e.g.[38]),
predefineddistributionchangesareintroducedintothedata affecttheinputdistributionbutnotnecessarilytherelationshipbe-
streamatarandompoint.Thisenablesasupervisedevalua- tween𝑋 and𝑦;suchdriftscanbedetectedwithoutlabels.Changes
tionofdriftdetectionmethodswhilepreservingthenatural in𝑝(𝑦|𝑋),usuallyreferredtoasrealdrift,altertheinput-output
characteristicsandinherentchallengesofreal-worlddata, relationshipandtypicallyrequirelabeleddatatodetect.Changes
addressingI2. mayalsooccurintheclassprior𝑝(𝑦)orintheclass-conditional
(2) Asetofnewdriftdetectionevaluationmetrics,including featuredistribution𝑝(𝑋|𝑦).Thesecategoriesarenotmutuallyex-
F1detectionscore,driftrecall,andfalsealarmrate,basedona clusive;forinstance,ashiftin𝑝(𝑋|𝑦)willoftenalsomanifestasa
versatiledefinitionofcorrectandincorrectdetections. changein𝑝(𝑋).
Thisenablesastandardizedandobjectivecomparisonofdrift Driftscanalsobecategorizedbyhowtheyevolveovertime[17].
detectionmethodsacrossdifferentdatasetsanddrifttypes, Inabrupt(orsudden)drifts,thedistributionshiftsinstantaneously
addressingI1. fromoneconcepttoanother.Ingradualdrifts,twodistinctconcepts
(3) Apracticalstandardizedprotocolforoptimizingde- coexistduringatransitionperiod,withobservationsincreasingly
tectorsbasedonleave-one-dataset-outcross-validation:To drawnfromthenewconcept.Inincrementaldrifts,asingleconcept
alsoaddressI1,weproposetooptimizehyperparametersof evolvescontinuouslyovertimewithoutdistinctbefore-and-after
conceptdriftdetectorsonallbutonedatasetandusethe states.Forsuddenorabruptdrifts,𝑑
𝑠
=𝑑
𝑒
andthus𝑤 =0,while
held-outdatasetforevaluation.Wehypothesizethatthis gradualandincrementaldriftsarecharacterizedby𝑑 < 𝑑 and
𝑠 𝑒
approachencouragestheoptimizationprocesstofindconfig- 𝑤 >0.Whileincrementaldriftsarerelevant,ourframeworkfocuses
urationsthataremorerobusttodistinctstructuraldynamics. onabruptandgradualdrifts.
Whileleave-one-group-outisastandardvalidationapproach,
toourknowledge,ithasnotpreviouslybeenappliedtodrift
detectionmethods. 2.2 DetectionMethods
Weapplytheproposedframeworktobenchmarkasetofstate- Several methods have been proposed to detect concept drift in
of-the-artandwidelyuseddriftdetectionmethodsinadatastream datastreams.Mostofthesehavebeendesignedtotracktheperfor-
classificationscenario.Weuse7commonlyusedreal-worlddata mance(e.g.errorrate)ofapredictivemodelanddetectwheneverit
streamsandintroducefourdifferentkindsofdrift,namelyclass worsenssignificantly.Suchmethodstypicallyfollowanapproach
priordrift,classlabelswapdrift,featurepermutationdrift,and basedoneithersequentialanalysis,controlcharts,ordistribution
featurefilteringdrift,eachsimulatedwithbothabruptandgradual monitoring.Sequentialanalysisapproachesworkbyaccumulating
transitions. statisticsovertimeandcomparingthemtoathreshold.CUSUMor
Our results reveal that SEED [23], STEPD [25], and ABCD [22] Page-Hinkley[26]methodsaretwoprominentexamplesfollowing
consistentlyoutperformotherdetectorsacrossdistinctdrifttypes, thisapproach.Controlchartsleveragethebinomialdistribution
establishing new baseline benchmarks for the field. We further todefineconfidenceintervalsfortheerrorrate,withDDM[15]
demonstratethathyperparameteroptimizationusingourproposed orHDDM[14]beingtwowell-knownmethods.Distributionmon-
approachsignificantlyimprovesdetectionperformanceoverde- itoringapproachesworkbycomparingthecurrentdistribution
faultconfigurations.Ourimplementation1isbuiltontheCapyMOA toareferencedistribution.ADWIN[5],whichdetectssignificant
Pythonlibrary[19],andallcodeandexperimentdetailsareavail- changesinadistribution’smean,isawell-knownmethodfollowing
ableforreproducibility. thisapproach.WerefertotheseminalsurveybyGamaetal.[17]
foracomprehensivereviewontheseapproaches.
Indomainswithconsiderableverificationdelay(thetimeittakes
2 Background
toobtainalabelforagiveninstance),monitoringperformanceis
2.1 DataStreamsandConceptDrift
impractical.Ineffect,otherapproachestrackindicatorsthatcan
Adatastreamisaninfinitesequenceofobservationsgenerated hinttoapossibleperformancedegradationandcanbemonitored
over time according to some unknown underlying distribution. unsupervised.Examplesofsuchindicatorsarethedistributionof
Formally, we consider a data stream S as a sequence of tuples features(e.g.[11,22]),thedistributionofpredictions[27],oran
{(𝑋 1 ,𝑦 1),(𝑋 2 ,𝑦 2),...},whereeach𝑋 𝑡 isaninput(e.g.,afeature auxiliarycompressionloss[8].Theassumptionunderlyingthese
vector)and𝑦 𝑡 isalabel.2Attime𝑡,thetuple(𝑋 𝑡 ,𝑦 𝑡)isdrawnfrom methods is that drift in the feature space or the distribution of
adistribution𝑝 𝑡(𝑋,𝑦),referredtoastheconcept.Aconceptdrift predictionsindicateapotentialperformancedegradation.
hasoccurredifthisdistributionchanges:
Definition2.1(Conceptdriftanddriftpoint). Wedefineaconcept 2.3 EvaluatingDriftDetectionMethods
driftasatuple(𝑑
𝑠
,𝑑 𝑒)suchthat𝑝
𝑑𝑠
(𝑋,𝑦)≠𝑝
𝑑𝑒
(𝑋,𝑦)and𝑑
𝑠
≤𝑑
𝑒
.
Reliablyevaluatingandcomparingconceptdriftdetectorsrequires
I.e.,𝑑 isthestartingposition(pointoftheinstancewheredrift
𝑠 solvingthreeinterrelatedsub-problems:(1)obtaininggroundtruth
begins)and𝑑 istheendingposition(pointwheredriftcompletes).
𝑒 driftpointsinrealisticdata,(2)measuringperformanceinaway
Thewidthofthedriftisgivenby𝑤 =𝑑 𝑒−𝑑
𝑠
.
thatiscomparableacrossdatasets,and(3)selectinghyperparame-
terswithoutoverfittingtoasinglestream.Weorganizetherelated
1https://github.com/vcerqueira/experiments-drift_evaluation
2W.l.o.g.,wefocusoncategoricallabelsinthiswork. workaroundthesechallenges.

AFrameworkforEvaluatingandBenchmarkingConceptDriftDetectionMethods KDD’26,August09–13,2026,JejuIsland,RepublicofKorea
Driftpointgroundtruth. Evaluatingwhetheradetectorcorrectly
identifiesdriftpointsrequiresknowingwhendriftsoccurred.Two
P
A
r
c
e
c
c
e
e
p
d
ta
e
b
n
l
c
e
e
paradigmshaveemergedinresponse.Inproxyevaluation,detectors Drift Max 2nd Drift
areassessedindirectlybymeasuringwhetherretrainingamodel onset delay onset
upon detection improves predictive performance [8, 11]. While
practical,thisconflatesdetectorqualitywithmodeladaptability
anddoesnotrevealdetectionaccuracyortiming.Supervisedevalu-
ationinsteadreliesonknowndriftpoints,typicallyobtainedfrom
Time
syntheticdatageneratorsthatswitchbetweenpredefinedconcepts
atfixedtimes[4,20,30].Becausegroundtruthisavailablebycon-
struction,onecandirectlymeasuredetectionaccuracy,delay,and Alarm Alarm Alarm
(FP) (TP) (FP)
falsealarmrates.However,syntheticstreamsofteninvolvesimpli-
fieddistributionsandunrealisticdriftdynamics,leavingitunclear
whetherconclusionstransfertoreal-worldsettings[33,36].No Figure1:Driftdetectionevaluationcriteria.Theacceptable
priorworkprovidesaprincipledwaytoperformsupervisedeval- detectionwindowisdefinedastheinterval[𝑑 𝑠−𝛿 𝑝𝑟𝑒 ,𝑑 𝑒+𝛿 𝑚𝑎𝑥].
uationonreal-worlddata—agapourdriftsimulationframework Anydetectionfallingwithinthiswindowisconsideredatrue
addresses. positive,whiledetectionsoutsidethiswindowarecounted
asfalsepositives.
Comparabilityofevaluationmetrics. Evenwhengroundtruth
isavailable,existingmetricshinderfaircross-datasetcomparison.
Bifet[4]proposedthreewidelyusedmetricsforsupervisedevalua-
hyperparameterprotocol(I1).Ourworkisthefirsttojointlyaddress
tion:
allthreechallengeswithinaunifiedframework.
• MeanTimebetweenFalseAlarms(MTFA):theaveragetime
spanbetweenconsecutivefalsealarmsbeforethetruechange
3 DriftDetectionEvaluationFramework
point.
Thissectionintroducesasystematicframeworkforevaluatingcon-
• MeanDetectionTime(MDT):theaveragedelaybetweena
ceptdriftdetectionmethods,includingdefinitionsofdetectioncor-
driftanditsdetection.
rectness,asetofevaluationmetricsderivedfromthesedefinitions,
• MissedDetectionRatio(MDR):theproportionofdriftsthat
andanapproachforhyperparametertuningofdetectors.
goundetected.
These can be averaged over multiple runs for more robust esti-
3.1 EvaluationCriteria
mates[7,12].However,MTFAandMDTarehighlydependenton
Westartbyestablishingclearcriteriaforwhatconstitutesacorrect
streamlengthanddriftspacing,causingtheirvaluestofluctuate
detection,whichisakeyaspectforevaluatingdetectorsinsuper-
acrossdatasetsandprecludingmeaningfulcross-datasetcompari-
visedsettings.RecallourdefinitionofconceptinDefinition2.1:An
son.Otherworks[12,30]haveappliedsimilarmetricsunderdif-
idealdriftdetectorwoulddetectdatadistributionchangesaccu-
ferentterminology,furtherevidencingthelackofstandardization.
ratelyandwithzerodetectiondelay.Inpractice,however,adetector
Tomitigatedatasetdependence,Heydenetal.[22]proposedan
typicallyneedstofirstobserveacertainamountofdatabeforeac-
F1scorefordriftdetection,definingtruepositives,falsenegatives,
curatedriftdetectionispossible.Ingeneral,themoredataadrift
andfalsepositivesbasedonwhetheradriftwasdetectedbeforethe
detectorobserves,themoreaccurateitshouldbe.Atthesametime,
nextchangeoccurred.WhileF1improvescross-datasetcompara-
however,thiswillleadtoalargerdetectiondelay.Optimizingthis
bility,itsformulationignoresthetemporalaspect:adetectorwith
tradeoffisnon-trivialandapplication-dependent.
unacceptabledelaycanstillachieveperfectF1.Ourtiming-aware
Toaccountforthistrade-off,weintroduceanevaluationcriteria
metricsaddressthisgapbynormalizingforstreamcharacteristics
whereadetectionisonlyconsideredaccurateifitoccurswithin
whilepenalizingdetectiondelay.
areasonabletimewindowaroundtheactualdriftpoint.Let𝛿
𝑚𝑎𝑥
Configurationofdriftdetectors. Beyondmetrics,thehyperpa- denotethemaximumacceptabledelayparameter,representingthe
rameter configuration of drift detectors poses a reproducibility maximumnumberofinstancesafter𝑑 withinwhichadetection
𝑒
challenge.Mostworksreportspecificconfigurationswithoutclear mustoccurbeforethedriftisconsideredmissed.Similarly,let𝛿
𝑝𝑟𝑒
guidelinesonhowtheywereobtained,oftenrelyingontacitexpert denotetheacceptableprecedenceparameter,representingthemax-
knowledgeortuningonthesamedatasetusedforevaluation[20]. imumnumberofinstancesbefore𝑑 whereanearlydetectioncan
𝑠
This risks overfitting to specific stream dynamics and prevents beconsideredvalid.Thisprecedenceparameteraccountsforcases
faircomparisonacrossstudies.Ourleave-one-dataset-outcross- wheredetectablechangesinthedatastreammayprecedethefor-
validationprotocoladdressesthisbyoptimizinghyperparameters maldriftpoint.Forinstance,someexternaleventmaycauseand
on held-out datasets, preventing data leakage and encouraging precedeachangeinthedatadistributionandleadtoperformance
configurationsthatgeneralizeacrossdiversestreams. degradation.Whilethedatadistributionchangedefinestheconcept
Previousbenchmarks[12,20,30]eachsufferfromoneormore drift,theprecedingeventisakeyfactorforitsdetection.
oftheabovesub-problems:theyrelyonsyntheticdataforground Wethereforedefinetheacceptabledetectionwindowasaninter-
truth(I2),usedataset-dependentmetrics(I1),orlackaprincipled val[𝑑 𝑠−𝛿
𝑝𝑟𝑒
,𝑑 𝑒+𝛿 𝑚𝑎𝑥],illustratedinFigure1.Anydetectionfalling

KDD’26,August09–13,2026,JejuIsland,RepublicofKorea Cerqueiraetal.
withinthiswindowisconsideredatruepositive,whiledetections negativesarenotcoveredinthismetrictoavoidarbitrarily
outsidethiswindowarecountedasfalsepositives. largepenalties(i.e.values>>1);
For gradual drifts (𝑑 𝑠 < 𝑑 𝑒 ), we anchor the acceptable delay • AlarmRate(AR):Thetotalnumberofalarmstriggeredper
at𝑑
𝑒
ratherthan𝑑
𝑠
.Thischoiceensuresthattheentiregradual unitoftime,calculatedas
T
T
ot
o
a
t
l
a
i
l
n
a
s
l
t
a
a
r
n
m
c
s
es
·𝐹.Bydefault,weuse𝐹
transitionfallswithintheacceptablewindow,andthat𝛿 hasa instancesastheunitoftime.Thismeasureshowfrequently
𝑚𝑎𝑥
consistentinterpretation,i.e.maximumdelayafterdriftcompletion, the detector signals drifts, regardless of correctness. The
regardlessofdriftwidth.Notethatdetectionsoccurringduringthe factor𝐹 dependsonthevelocityofthedatastream.
gradualtransition(between𝑑 𝑠 and𝑑 𝑒 )areinherentlyvalid,asthey • False Alarm Rate (FAR): The number of false positive
fallwithintheacceptablewindow. alarmsperunitoftime,calculatedas FP ·𝐹.Thisis
Totalinstances
Ineffect,thecriteriaare: particularlyimportantasfrequentfalsealarmscanleadto
unnecessarymodelupdatesandreducedsystemefficiency
• TP(TruePositive):Aconceptdriftoccurredandwasde-
andtrust.
tectedwithintheacceptabledetectionwindow[𝑑 𝑠−𝛿 𝑝𝑟𝑒 ,𝑑 𝑒+
𝛿 𝑚𝑎𝑥]. Overall,thesemetricsprovideacomplementaryviewondriftde-
• FN (False Negative): A concept drift occurred but was tectorperformance.Forexample,NDTquantifiesdetectionlatency
notdetectedwithintheacceptabledetectionwindow[𝑑 𝑠− onlyforsuccessfullydetecteddriftepisodes;itdoesnotpenalize
𝛿
𝑝𝑟𝑒
,𝑑 𝑒+𝛿 𝑚𝑎𝑥]). misseddetections.Forthisreason,NDTshouldalwaysbeinter-
• FP(FalsePositive):Analarmwastriggeredoutsideany pretedalongsideEpisodeRecall,whichcapturestheproportionof
acceptabledetectionwindow[𝑑 𝑠−𝛿 𝑝𝑟𝑒 ,𝑑 𝑒+𝛿 𝑚𝑎𝑥] driftepisodesthatweredetectedwithintheacceptablewindow.
Remark(TrueNegative). Theconceptoftruenegative(TN)isnot 3.3 HyperparameterOptimization
welldefinedinthecontextofdriftdetection,duetothecontinuityof
Defaulthyperparametersfordriftdetectorsareoftentunedw.r.t.
thedatastreamandthefactthatthereareinfinitelymanypossible
thespecificdatasetsusedintheoriginalpublications.However,
momentswheredriftdoesnotoccur[13].
usingthesamedatasetforoptimizingandevaluatingthedetector
cancauseoverfittingandleadtooverlyoptimisticperformance
Remark(PrecedenceParameter). Thevalueoftheprecedencepa-
estimates reported in the respective papers. To solve this issue,
rameter𝛿 issituational.Forexample,whenintroducingsynthetic
𝑝𝑟𝑒 weproposealeave-one-dataset-outcross-validationapproachfor
driftpoints,thedistributionchangescanonlybedetectedafterthe
optimizingthehyperparametersofdriftdetectors.
driftonset,so𝛿 shouldbe0insuchcases.
𝑝𝑟𝑒 Foreachdatasetheldoutforevaluation,theremainingdatasets
serveastheoptimizationset.Asearchoverthedetector’shyperpa-
3.2 EvaluationMetrics rameterspaceisconducted,selectingtheconfigurationthatmaxi-
Buildingupontheevaluationcriteriadefinedabove,weestablish mizesachosenperformancemetric(e.g.,F1detectionscore)aver-
severalmetricstoassessdriftdetectorperformancefromvarious agedacrossallscenariosintheoptimizationset.Thedetectoristhen
perspectives:accuracy,timeliness,andreliability: evaluatedontheheld-outdatasetusingtheselectedconfiguration.
Leave-one-dataset-outcross-validationensuresthatdetectorpa-
• Precision: The proportion of detected alarms that were
rametersareoptimizedondatadifferentfromtheevaluationdata,
correct(𝑇𝑃/(𝑇𝑃+𝐹𝑃)).Thismetricindicateshowreliablethe
leadingtomorereliableperformanceestimateswhileatthesame
detector’salarmsare.Higherprecisionmeansmostalarms
timegettingthemostoutofdetectorsperformance.Theapproach
correspondtoactualdriftsratherthanfalsepositives.
canbecoupledwithanysearchstrategy,suchasrandomsearch[3].
• Recall:Theproportionofactualdriftsthatwerecorrectly
identified(𝑇𝑃/(𝑇𝑃+𝐹𝑁)).Thismeasurequantifieshowwell
4 DriftSimulationFramework
thedetectorcapturesactualdriftevents.
• Episode Recall: The proportion of actual drift episodes Wenowintroduceourmethodforinjectingsystematicallycontrol-
thatwerecorrectlyidentified.Bydefinition,recallcounts lableconceptdriftintoreal-worlddata.
multipledetectionswithintheacceptabledetectionwindow
asmultipleTPs.EpisodeRecalladdressesthislimitationby 4.1 SimulatingDrifts
countingmultiplealarmswithinthesamedetectionwindow Ourapproachadoptsasemi-syntheticmethodology:givenareal-
asasingledetection.Itprovidesamorerealisticmeasureof worlddatastream,ourapproachinjectssyntheticconceptdriftat
driftdetectioncoverage. specifiedpoints.
• F1Score:Theharmonicmeanofprecisionandrecall.
• NormalizedDetectionTime(NDT):Theaveragenumber 4.1.1 SimulationProcess. Ourdriftsimulationframeworkfollows
ofinstancesbetweenthestartofadrift(𝑑 )anditsdetection, theprequentiallearningparadigm[16]andconsistsoffoursteps:
𝑠
normalizedbythemaximumacceptabledelay𝛿
𝑚𝑎𝑥
.This (1) Randomshuffling:Real-worlddatastreams,denotedS,may
metricexpressesdetectiondelayasaproportionoftheac- alreadycontainunknownconceptdrifts,whichcouldcon-
ceptablewindow,enablingcomparisonsacrossdatasetswith foundtheresultsofcontrolledexperiments.Tominimize
different𝛿
𝑚𝑎𝑥
values.NDTiscomputedonlyoverdetected thisrisk,werandomlyshuffletheobservationsinS,produc-
drifts(misseddriftsareexcluded),sovaluesrangefrom0 ingapermutedstreamS𝜋 .Thisstepremovespre-existing
(immediatedetection)to1(detectionatthedeadline).False temporaldependencies(e.g.,seasonality)bydesign,bringing

AFrameworkforEvaluatingandBenchmarkingConceptDriftDetectionMethods KDD’26,August09–13,2026,JejuIsland,RepublicofKorea
itclosertoi.i.d.,andlayingthegroundforcontrolleddrift tothenextobservation.Zliobaite[38]evaluatedthisdrifttypein
injectionwithknownchangepoints. thecontextofchangedetectionwithdelayedlabeling,thoughina
(2) Randomizeddriftonset:Ineachprequentialevaluationrun, non-randomizedsetting(e.g.fixingtheproportionsoftheclasses
weselectasingledriftonsetpoint𝑑 atrandom,subject onspecificdatasets,predefineddriftonset),whilewecreateamore
𝑠
totwobufferregions.Thefirstbuffer,atthebeginningof generalframeworkwithrandomizedparameters.
S𝜋 ,ensurestheclassifierhassufficienttrainingdataand
4.2.2 ClassLabelSwapDrift(Algorithm3). Classlabelswapdrift
enoughpre-driftsamplesforevaluatingfalsealarms.The
simulatesachangeintheclassificationfunctionbyrelabelingin-
secondbuffer,attheendofthestream,providesamplepost-
stancesofaspecificclass.Afterthedriftonset,anyinstanceorigi-
driftsamplesforassessingdetectionperformance.Once𝑑 is
𝑠 nallybelongingtoaselectedlabel𝑦 hasitstruelabelchanged
established,allsubsequentinstancesaretransformedusing 𝑠𝑒𝑙
toadifferenttargetlabel𝑦 ,whileitsfeaturevectorremains
adesignateddriftfunction(asdetailedinSection4.2). 𝑠𝑤𝑎𝑝
unchanged.Thisrepresentsascenariowheretheunderlyingclassi-
(3) MonteCarlotrials:Theaboveprocess(shuffling,selecting
ficationrulechanges,withthesameinputnowcorrespondingtoa
arandomizeddriftpoint,andapplyingdrift)isrepeated𝑘
differentoutput.
times. This repetition allows for robust statistical assess-
mentofdetectorperformanceacrossmultiplerunsofthe 4.2.3 FeaturePermutationDrift(Algorithm4). Featurepermutation
prequentialworkflow. driftintroducesastructuralchangeinthefeaturespacebyreorder-
(4) Abruptvs.gradualdrift:Forabruptdrifts(𝑤 =0),thedrift ingtheinputfeatures.Afterthedriftonset,thefeatureswithineach
transformationisappliedtoallinstancesfromthedriftonset instance’svector𝑥 arerearrangedaccordingtoafixed,randomly
onwards.Forgradualdrifts(𝑤 > 0),thetransformationis generatedpermutation𝜎.Theclasslabelremainsunchanged.This
appliedprobabilistically:theprobabilitythataninstanceat simulatesscenarioswheretherelativeimportanceororderingof
time𝑡 isdrawnfromthetransformeddistributionincreases featuresshifts.Zliobaite[38]alsoevaluatedthisdriftinaclass-
linearlyfrom0at𝑑 𝑠 to1at𝑑 𝑒 ,computedas𝑝(𝑡) = 𝑡− 𝑤 𝑑𝑠. conditionalsetting(permutationoffeatureswithinaspecificclass),
After𝑑 ,allinstancesaretransformed. withtheclassandthepermutationoffeaturesbeinghand-picked
𝑒
foreachdataset.
4.1.2 Instancetransformationandevaluation. Beyondtheworkflow
describedabove,thecoremechanismforsimulatingdriftisthe 4.2.4 FeatureFilteringDrift(Algorithm5). Featurefilteringdrift
transformationandevaluationofdatainstancesafterthedriftonset. simulates a change in the marginal distribution of a feature by
Figure2illustratesthisprocess.Let𝑀denoteapredictivemodel conditionallyfilteringinstances.Afterthedriftonset,instancesare
(here,aclassifier),𝑔thedriftsimulationfunctionthatappliesthe checkedagainstathresholdcondition:ifthevalueofarandomly
selecteddriftpattern,and𝐼 =(𝑋,𝑦)aninstancefromS𝜋 . selectednumericfeatureexceedsapredefinedthreshold𝜏,thein-
Foreachincominginstance𝐼 = (𝑋,𝑦),theframeworkdeter- stanceisdroppedfromthestream;otherwise,itpassesthrough
mineswhetherdriftshouldbeappliedbasedonthecurrentposi- unchanged.Whenaninstanceisdropped,theprequentialworkflow
tionrelativetothedriftonset𝑑 .Before𝑑 ,instancespassthrough skipsitentirelyandproceedstothenextobservation.Thissim-
𝑠 𝑠
unchanged.After𝑑 ,thedriftsimulationfunctiontransforms𝐼 into ulatesscenarioswhere,duetopolicychanges,sensorlimitations,
𝑠
𝐼′ =𝑔(𝐼)accordingtothespecifieddriftpattern.Themodel𝑀then ordatacollectionconstraints,certainfeaturevaluesarenolonger
generatesaprediction𝑦ˆforthe(possiblytransformed)instance. observed.Inthiswork,weconsider𝜏tobethemedianofthefeature
Mostofthedriftdetectorsthenmonitor𝑀’spredictionerrorover valuesobservedbeforethedriftonset.
time.However,otherinputsarepossible,suchasthefeaturevec- 4.2.5 Discussion. Thefourdrifttypesdescribedaboverepresent
tors[22],oranauxiliarycompressionerror[8].Afterinference, commoncategoriesofdistributionchangethatcanoccurinreal-
themodel𝑀 istrainedontheinstance𝐼,orthetransformedin- worlddatastreams.Theyarenotintendedtobeexhaustive;many
stance𝐼′.Thecompletedriftsimulationframeworkisillustratedin otherformsofdriftexist,suchasnoiseinjection,heteroskedas-
Algorithm1inappendix. ticity,ortemporaldependencies[37].Additionally,incremental
drifts,wherethedistributionshiftscontinuouslyoveranextended
4.2 DriftTypes period[34],arealsorelevantbutnotconsideredinthiswork.Our
Thepreviouslyintroducedsimulationframeworkusesageneralized selectionfocusesondistinct,interpretabledriftpatternsthatallow
driftfunction𝑔.Thisallowsmodelingdifferenttypesofdistribution forcontrolledexperimentation.
changes.Wenowprovideconcreteexamplesof𝑔,illustratinghow Eachdrifttypeinvolvesrandomparameterchoices(e.g.,which
togeneratethetypesmentionedinSection2.1.SeeAppendixA.2 classtoaffect,whichfeaturetofilter).Thisvariabilitymeansthata
fortherespectivepseudocode. singlerunmaynotfullycharacterizedetectorperformance.The
MonteCarloapproachdescribedearlieraddressesthisbyrepeating
4.2.1 ClassPriorDrift(Algorithm2). Classpriordriftsimulates theevaluationacrossmultiplerunswithdifferentrandomconfigura-
achangeintheclassdistributionbyalteringthefrequencyofa tions,leadingtomorerobustperformanceestimates.Forsimplicity,
specifictargetclass.Afterthedriftonset,instancesbelongingtoa eachMonteCarloruncontainsasingledrift,whereasreal-world
pre-selectedlabel𝑦 arerandomlydroppedfromthestreamwith streamsmayexhibitmultipleones.Thesescenarioscanbeframed
𝑠𝑒𝑙
probability𝑝 ,effectivelyreducingtheoccurrenceofthatclass. asdifferentepisodesofdrifteventsasillustratedinFigure1.
𝑠𝑘𝑖𝑝
Whenaninstanceisdropped,theprequentialworkflowskipsit Finally,becauseeachdrifttypetransformsinstancesfrom𝐼 to𝐼′
entirely(i.e.notrainingorinferenceisperformedonit),proceeding (orfiltersthem),allfourcanbeappliedineitherabruptorgradual

KDD’26,August09–13,2026,JejuIsland,RepublicofKorea Cerqueiraetal.
M
Change
Detected?
I
No
|     |     |     | N e w      |     |     | Sim u l a te  |     |           |     | Co m p | u te |     |     |     |
| --- | --- | --- | ---------- | --- | --- | ------------- | --- | --------- | --- | ------ | ---- | --- | --- | --- |
|     |     |     | in st a nc | e   | I   | Dr if t ?     |     | Inference |     | E rr   | o r  | D   |     |     |
Yes
I'
Figure2:Inferencestageoftheprequentialworkflowwithsimulateddrifts(usingerrortrackingasexample).
modeasdescribedinSection4.Thisflexibilityallowstheframework Treeduetoitscomputationalefficiency.Weusedefaulthyperpa-
tosimulateawiderangeofdriftdynamics. rametersonHoeffdingTreeclassifieracrossallexperiments4.
|     |     |     |     |     |     |     |     | HyperparameterOptimization. |     |     | Regardinghyperparameteropti- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ---------------------------- | --- | --- | --- |
5 Experiments
mization,weconducttheleave-one-dataset-outapproachdescribed
5.1 ExperimentalSetup inSection3.3.Whenevaluatingthedetectorsoneachdataset,we
usetheremainingdatasetsforoptimizingitshyperparametersbased
| Datasets. |     | Weevaluateourapproachonsevenwidelyusedreal- |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
world datasets from the USP Data Stream Repository [32]: As- ontheF1detectionscore.Theoptimizationisconductedusing30
fault [31], Electricity [21], Covertype [6], GasSensorArray [35], iterationsofrandomsearch.Eachconfigurationisalsoevaluted
NOAA[9],Posture[11],andRialto[24].Detaileddescriptionsof using the Monte Carlo procedure described in Section 3.3. The
eachdatasetareavailableintherepository3. configurationspaceforeachdetectorispresentedinTable4in
appendix.
Tocreatecontrolledevaluationsettings,wesystematicallygen-
eratesemi-syntheticdatastreamsbyinjectingknownconceptdrift
| pointsintothesedatasetsusingtheproposeddriftsimulationframe- |     |     |     |     |     |     |     | 5.2 Results |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
work.Foreachdatasetanddrifttype,weperform50MonteCarlo MostoftheresultspresentedbelowarebasedonF1score.The
trials.Ineachtrial,thedriftonsettimeisrandomlysampledbe- scoresontheremainingmetrics(includingexecutiontime),other
tween50%and80%ofthetotaldatasetlength.Driftwidthand classifiers and synthetic data streams, are available in the Ap-
maximumdelayparametersaredataset-specific.Thesewerese- pendixB.2.Inalltables,bold(underlined)scoresdenotethebest
lectedbasedondatasetlengthandaresummarizedinTable3.The (second-best)detectorintherespectivescenario.
| p r e c | ed e n c e   | p a r am e t   | e r i s fi x e | d a t z e r   | o ( 𝛿         | 0 ) f o r a     | ll d a ta s e t s |                      |     |                                    |     |     |     |     |
| ------- | ------------ | -------------- | -------------- | ------------- | ------------- | --------------- | ----------------- | -------------------- | --- | ---------------------------------- | --- | --- | --- | --- |
|         |              |                |                |               | 𝑝 𝑟 𝑒         | =               |                   |                      |     |                                    |     |     |     |     |
|         |              |                |                |               |               |                 |                   | 5.2.1 Overallscores. |     | Tables1and2showtheaveragerankbased |     |     |     |     |
| si n c  | e sy n t h e | ti c d rif t s | c a n n o t    | b e n o t a n | ti c i p a te | db e f o r e th | e ir o n s e t .  |                      |     |                                    |     |     |     |     |
onF1detectionscoreforeachdriftdetectionmethodacrossdiffer-
Webenchmarkatotalof14changedetectionmethods:ADWIN[5],
entdriftscenarios,forabruptandgradualdriftsrespectively.The
| CUSUM | [26], | DDM [15], | EDDM [1], | EWMA | [29], GMA | [28], HDDMA | [14], |     |     |     |     |     |     |     |
| ----- | ----- | --------- | --------- | ---- | --------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
averagerankofadetectordenotesitsrelativepositionaccording
| HDDMW | [14], | PH [26], | RDDM [2], | SEED | [23], STEPD | [25], | ABCD and |     |     |     |     |     |     |     |
| ----- | ----- | -------- | --------- | ---- | ----------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
toperformance;lowervaluesindicatebetterperformance.
|         | [22], | and   | [8]. | Most of | these | are based | on track- |     |     |     |     |     |     |     |
| ------- | ----- | ----- | ---- | ------- | ----- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| ABCD(X) |       | STUDD |      |         |       |           |           |     |     |     |     |     |     |     |
Theresultsrevealdistincttiersofdetectorperformance.SEED
ingtheperformanceofaclassifier,namelytheinstance-wiseerror
|     |     |     |     |     |     |     |     | and STEPD exhibit | consistently |     | competitive |     | F1 scores across | all |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------ | --- | ----------- | --- | ---------------- | --- |
rate,exceptforABCD(X)[22],whichmonitorsthefeaturespaceand
drifttypesandabruptnessconditions,rankingamongthetopthree
STUDD,whichmonitorsanauxiliarycompressionloss[8].Mostof
performersinmostscenarios.
thesemethodsfollowadistributionmonitoring,controlchart,or
|     |     |     |     |     |     |     |     | Several detectors | perform |     | well under | specific | conditions | but |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | --- | ---------- | -------- | ---------- | --- |
sequentialanalysisapproach.TheexceptionisSTUDD,which,being
ameta-detector,canbecoupledwithanyoftheothermethods.In struggleinothers.Amongperformance-trackingmethods,ADWIN
excelsatfeaturefilteringandclasspriordriftsbutunderperforms
thiswork,STUDDiscoupledwithADWIN.WealsonotethatABCD
onfeaturepermutation.ABCDachievestop-tierranksonfeature
canbeappliedbothtotheerrorrateandthefeaturespace.We
permutationandclassswapswhileshowingweakerperformance
denotethelatterasABCD(X).Wenotethatourmainobjectiveisto
onfeaturefiltering.DDMshowsmoderateresultsoverall,perform-
establishastandardizedevaluationprotocolratherthantoidentify
thebestperformingdetector.Thus,wefocusonwell-established ingbestonclasspriorundergradualconditions.GMAdemonstrates
particularstrengthonfeaturefilteringingradualsettings,achiev-
detectionmethodswhoseperformancecharacteristicsarealready
ingthebestaveragerankforthatscenario.HDDMWshowsstable
wellunderstood.
middle-tierperformance(averageranksaround5to7)acrossmost
| We  | select | the Hoeffding |     | Tree [10] | as the | classifier | in the ex- |     |     |     |     |     |     |     |
| --- | ------ | ------------- | --- | --------- | ------ | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
conditions.
periments,awell-establishedalgorithminthestreamingmachine
learningliterature.WhileensemblesofHoeffdingTrees(e.g.[18]) Theunsuperviseddetectors,ABCD(X)andSTUDD,exhibitachar-
acteristicpattern:reasonableorstrongperformanceonfeature-
havebeenshowntobemoreaccurate,wefocusontheHoeffding
spacedriftsbutpoorresultsonlabel-basedchanges.ABCD(X)achieves
3https://sites.google.com/view/uspdsrepository 4https://capymoa.org/api/modules/capymoa.classifier.HoeffdingTree.html

AFrameworkforEvaluatingandBenchmarkingConceptDriftDetectionMethods KDD’26,August09–13,2026,JejuIsland,RepublicofKorea
| Table 1: Average | rank of | drift detectors | across | different |     |     |     |     |        |         |     |
| ---------------- | ------- | --------------- | ------ | --------- | --- | --- | --- | --- | ------ | ------- | --- |
|                  |         |                 |        |           |     |     |     |     | ABRUPT | GRADUAL |     |
datasetsforabruptdrifts
1.00
| Detector | Feature Feat.Per- |     | Class | Class |     |     |     |     |     |     |     |
| -------- | ----------------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
0.75
|         | Filtering mutation |     | Prior | Swap |     |      |     |     |     |     |     |
| ------- | ------------------ | --- | ----- | ---- | --- | ---- | --- | --- | --- | --- | --- |
| ABCD    | 8.1                | 3.9 | 8.0   | 3.6  | 1F  | 0.50 |     |     |     |     |     |
|         | 12.7               |     | 13.1  | 13.1 |     |      |     |     |     |     |     |
| ABCD(X) |                    | 1.0 |       |      |     |      |     |     |     |     |     |
|         | 4.1                | 7.6 | 4.1   | 7.1  |     | 0.25 |     |     |     |     |     |
ADWIN
| CUSUM | 5.6 | 11.9 | 6.1 | 9.2 |     |     |     |     |     |     |     |
| ----- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.00
D D M 7 . 3 1 1 . 4 6 . 0 9 . 9 ABCD ABCD(X ) DWIN CUSUM DDM EWMA GMA HDDMA HDDMWPH RDDM SEED STEPD STUDD
| E W MA | 9 . 7 | 1 2 . 9 | 9 . 4 | 1 0 . 9 |        |     | A            |     |              |        |        |
| ------ | ----- | ------- | ----- | ------- | ------ | --- | ------------ | --- | ------------ | ------ | ------ |
| GMA    | 9.0   | 7.7     | 8.7   | 7.3     |        |     |              |     |              |        |        |
|        | 7.4   | 5.6     | 6.3   | 5.4     |        |     |              |     |              |        |        |
| HDDMA  |       |         |       |         | Figure | 3:  | Distribution | of  | F1 detection | scores | across |
HDDMW 7.1 6.9 5.8 6.0 dataset/drift-typepairsforeachdetector,comparingabrupt
| PH   | 13.1 | 12.9 | 11.6 | 10.1 | andgradualdriftconditions. |     |     |     |     |     |     |
| ---- | ---- | ---- | ---- | ---- | -------------------------- | --- | --- | --- | --- | --- | --- |
| RDDM | 6.6  | 10.2 | 7.9  | 9.1  |                            |     |     |     |     |     |     |
| SEED | 4.4  | 2.7  | 3.9  | 1.1  |                            |     |     |     |     |     |     |
|      |      | 3.7  | 4.3  | 2.4  |                            |     |     |     |     |     |     |
STEPD 3.4 Asexpected,abruptdriftsaregenerallyeasiertodetect:most
|     | 6.4 | 6.8 | 9.9 | 9.6 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
STUDD detectorsexhibithighermedianF1scoresandgreaterupwardvari-
|     |     |     |     |     | ance | for abrupt | conditions. | SEED | and | STEPD maintain | the high- |
| --- | --- | --- | --- | --- | ---- | ---------- | ----------- | ---- | --- | -------------- | --------- |
estmediansinbothconditions,thoughwithnotableperformance
near-perfectrelativedetectionoffeaturepermutationdrifts(rank
degradationundergradualdrifts.
1.0forabrupt,3.3forgradual)butfailsonclasspriorandclassswap
drifts.STUDDrankssecondonfeaturefilteringforgradualdriftsbut 5.2.3 F1vsFAR. Figure4visualizesthetrade-offbetweendetec-
islesseffectiveforlabel-basedscenarios.Thisbehaviorisexpected, tionaccuracy(F1averagerank)andreliability(FARaveragerank),
asthesemethodscannotobservechangesthatonlyaffectthetarget with detection timing (MDT average rank) encoded as dot size.
variable.Finally,PHandEWMAconsistentlyrankamongtheworst Lowervaluesindicatebetterperformanceonallthreeaxes;anideal
detectorwouldappearinthebottom-leftcornerwithasmalldot.
performersacrossnearlyallscenarios,withaveragerankstypically
exceeding10.
Table 2: Average rank of drift detectors across different Avg. Rank (MDT) 3 6 9
datasetsforgradualdrifts
|     |     |     |     |     |     | 12.5 PH |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
EWMA
| Detector | Feature Feat.Per- |     | Class | Class |     |     |     |     |     |     |     |
| -------- | ----------------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
ABCD(X)
|     | Filtering mutation |     | Prior | Swap |     | 10.0 |     |     |     |     |     |
| --- | ------------------ | --- | ----- | ---- | --- | ---- | --- | --- | --- | --- | --- |
DDM
RDDM
| ABCD    | 11.7 | 4.1 | 9.8  | 5.1  |     | )1F( knaR .gvA |     | CUSUM |     | STUDD | GMA |
| ------- | ---- | --- | ---- | ---- | --- | -------------- | --- | ----- | --- | ----- | --- |
| ABCD(X) | 13.0 | 3.3 | 13.0 | 13.1 |     |                |     |       |     |       |     |
7.5
| ADWIN | 6.0  | 11.2 | 6.8  | 7.9  |     |     |     |      |                 | HDDMW |     |
| ----- | ---- | ---- | ---- | ---- | --- | --- | --- | ---- | --------------- | ----- | --- |
|       |      |      |      |      |     |     |     | ABCD | HDDMA           |       |     |
| CUSUM | 6.3  | 11.9 | 7.3  | 9.7  |     |     |     |      |                 | ADWIN |     |
|       | 6.1  | 9.4  |      | 8.1  |     |     |     |      |                 |       |     |
| DDM   |      |      | 4.7  |      |     | 5.0 |     |      |                 |       |     |
|       | 11.7 | 12.4 | 10.6 | 12.0 |     |     |     |      |                 |       |     |
| EWMA  |      |      |      |      |     |     |     |      | STEPD           |       |     |
| GMA   | 3.9  | 6.6  | 6.1  | 4.7  |     |     |     | SEED |                 |       |     |
| HDDMA | 9.7  | 7.9  | 7.8  | 10.5 |     |     |     |      |                 |       |     |
|       |      |      |      |      |     |     |     | 5    |                 | 10    |     |
| HDDMW | 5.5  | 6.3  | 5.2  | 5.4  |     |     |     |      | Avg. Rank (FAR) |       |     |
| PH    | 10.9 | 12.4 | 9.7  | 11.1 |     |     |     |      |                 |       |     |
Figure4:Trade-offbetweenF1averagerank(y-axis,lower
|     | 4.7 | 6.4 | 6.6 | 5.3 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RDDM
|      | 5.9 |     | 5.0 |     | isbetter)andFARaveragerank(x-axis,lowerisbetter).Dot |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| SEED |     | 2.7 |     | 1.9 |                                                      |     |     |     |     |     |     |
sizeencodesMDTaveragerank(smallerisfasterdetection).
| STEPD | 5.4 | 2.8 | 5.2 | 2.0 |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| STUDD | 4.2 | 7.6 | 7.1 | 8.1 |     |     |     |     |     |     |     |
SEEDachievesthebestF1rankwhilemaintainingamoderate
FAR,makingitthemostbalancedchoiceoverall.STEPDfollows
Figure3comparesabruptversusgradual closelywithsimilarcharacteristics.ABCDoffersacompellingalter-
5.2.2 AbruptvsGradual.
scenariosbyshowingtheF1scoredistributionforeachdetector. nativewhenminimizingfalsealarmsisapriority;itachievesthe
Eachboxplotaggregates4×7=28datapoints(4drifttypes×7 bestFARrankamongdetectorswithcompetitiveF1scores,though
| datasets). |     |     |     |     | withslightlylowerF1performancethanSEEDandSTEPD. |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |

KDD’26,August09–13,2026,JejuIsland,RepublicofKorea Cerqueiraetal.
1.00
0.75
0.50
0.25
0.00
1.00
0.75
0.50
0.25
0.00
ABCD ABCD(X
A
) DWIN CUSUM DDM EWMA GMA HDDMA HDDMWPH RDDM SEED STEPD STUDD
1F
toeffectivetuning.PHandEWMAremainineffectiveregardless
Default Optimized
ofconfiguration,suggestingfundamentallimitationsrather
ABRUPT thansuboptimaldefaults.
Thesefindingsofferpracticalguidanceforpractitioners:SEED
andSTEPDarerobustdefaultswhendriftcharacteristicsareun-
known,whilespecializeddetectorsmaybepreferredwhenthedrift
typeorfalsealarmtoleranceisconstrained.
GRADUAL Limitationsandfuturework. Whiletheexperimentsprovidevalu-
ableinsights,therearesomelimitationsandpotentialfuturework.
First,theexperimentsarelimitedtooneclassifier(Hoeffdingtree)
andfourdrifttypessimulatedin7real-worlddatasets.Nonethe-
less,theproposeddriftsimulationframeworkisgenericandcanbe
extendedwithadditionaldriftdefinitions,ormixturesofthem.An-
otherlimitationisthattheprequentialworkflowissimplifiedinthe
sensethatitassumesimmediatefeedback,withlabelsbeingreadily
availableateachstepafterinference.Inpractice,thisisoftennot
thecase[8].Finally,inourdriftsimulationprocedure,werandomly
shuffletheoriginaldatastreamtoeliminateanypre-existingdrifts
Figure 5: Distribution of F1 scores across different
thatmightconfoundtheevaluation.Thisapproachpreservesthe
dataset/drifttypepairsforeachdetectionmethodcontrol-
real-worldfeature-levelcomplexityofthedata;however,italso
lingforhyperparameteroptimizationapproachanddrift
removesanyinherenttemporalstructure.Preservingtemporalde-
abruptness.
pendenciesinfutureextensionsoftheframeworkwouldenablea
morecomprehensiveandrealisticassessmentofdetectorperfor-
5.2.4 Detectorhyperparameteroptimization. Finally,weanalyse mance.
theimpactofthehyperparameteroptimizationdescribedinSec-
tion3.3.Theresultsreportedsofarshowthescoresofeachdetector
6 Conclusion
afterapplyinghyperparameteroptimization.Figure5showsthe
Thisworkcontributeswithaunifiedframeworkforevaluating
distributionofF1scoresacrossdifferentdataset/drifttypepairsfor
and comparing change detection methods in data streams. The
eachdetectionmethodcontrollingforhyperparameteroptimization
noveltyoftheframeworksettlesonthreemaincontributions:(1)
approach:optimizedanddefaultparameters.Theresultsshowthat
a flexible drift simulation framework that allows for controlled
mostapproachesimprovetheirmedianF1scorewhenoptimized,
experimentswithvarioustypesofdrift,enablingpractitionersto
apartfromSEED.
betterunderstanddetectorbehaviorunderdifferentdriftcondi-
tions;(2)asystematicevaluationcriteriatocomparedriftdetection
5.3 Discussion
methods,includingnewevaluationmetricsbasedondetectionpre-
Mainfindings. Theexperimentsrevealdistinctpatternsindetec- cisionandrecall,withthegoalofbuildingacommongroundfor
torperformance.Wehighlightthefollowingmainfindings:
theevaluationofdriftdetectionmethods;(3)anapproachforhy-
(1) SEEDandSTEPDexhibitthemostconsistentperformance perparameteroptimizationofdriftdetectionmethods,basedona
across all drift types and abruptness conditions, ranking leave-one-dataset-outscheme.
amongthetopthreeinmostscenarios.Whenminimizing Weappliedtheproposedframeworktobenchmarkstate-of-the-
falsealarmsisapriority,ABCDoffersacompellingalternative artandwidelyuseddriftdetectionmethodsonsyntheticandreal-
withthebestFARrankamongaccuratedetectors,though worlddatasets.Theexperimentsrevealinterestingpatternsinthe
withslightlylowerF1thanSEEDandSTEPD. performanceofthedetectors.Whilethereisanoticeablevariability
(2) Gradualdriftsaresystematicallyhardertodetectthanabrupt inrelativeperformanceacrossdifferentconditions,wehighlight
ones.MostdetectorsshowlowermedianF1scoresandre- thatSEED,STEPDandABCDshowthebestoverallperformanceacross
ducedvarianceundergradualconditions,withtheperfor- alldatasetsanddrifttypes.
mancegapparticularlypronouncedformethodslikeABCD
andABCD(X).
(3) Unsuperviseddetectors(ABCD(X)andSTUDD)performbetter Acknowledgements
onfeature-spacedrifts(featurepermutation,featurefiltering) ThisworkisfundedbynationalfundsthroughFCT–Foundationfor
thanonlabel-basedchanges(classprior,classswaps),as ScienceandTechnology,I.P.,withinthescopeoftheresearchunit
expectedsincetheycannotobservetargetvariableshifts. UID/00326-CentreforInformaticsandSystemsoftheUniversityof
(4) Hyperparameteroptimizationyieldsimprovementsformost Coimbra,https://doi.org/10.54499/UID/00326/2025.HeitorMurilo
detectors, with gains more pronounced for abrupt drifts. GomesacknowledgesthefinancialsupportoftheMarsdenFund
Notably,STEPD’sstrongperformanceislargelyattributable underawardnumberVUW2213.

AFrameworkforEvaluatingandBenchmarkingConceptDriftDetectionMethods KDD’26,August09–13,2026,JejuIsland,RepublicofKorea
References Table3:Datasetsummaryanddriftparameters
[1] ManuelBaena-Garcıa,JosédelCampo-Ávila,RaulFidalgo,AlbertBifet,Ricard
Gavalda,andRafaelMorales-Bueno.2006.Earlydriftdetectionmethod.InFourth #Samples #Features #Classes MaxDelay DriftWidth
internationalworkshoponknowledgediscoveryfromdatastreams,Vol.6.77–86.
[2] RobertoSMBarros,DaniloRLCabral,PauloMGonçalvesJr,andSilasGTCSantos. Asfault 8563 62 5 500 500
2017.RDDM:Reactivedriftdetectionmethod.ExpertSystemswithApplications Covtype 100000 54 7 2500 2500
90(2017),344–355. Electricity 45312 8 2 2500 2500
[3] JamesBergstraandYoshuaBengio.2012.Randomsearchforhyper-parameter GasSensor 13910 128 6 1500 1500
optimization.Thejournalofmachinelearningresearch13,1(2012),281–305. NOAA 18159 8 2 1500 1500
[4] AlbertBifet.2017.Classifierconceptdriftdetectionandtheillusionofprogress. Posture 100000 3 8 2500 2500
InInternationalconferenceonartificialintelligenceandsoftcomputing.Springer,
Rialto 82250 27 10 2500 2500
715–725.
[5] AlbertBifetandRicardGavalda.2007.Learningfromtime-changingdatawith
adaptivewindowing.InProceedingsofthe2007SIAMinternationalconferenceon
datamining.SIAM,443–448.
[6] JockABlackardandDenisJDean.1999. Comparativeaccuraciesofartificial
neuralnetworksanddiscriminantanalysisinpredictingforestcovertypesfrom [25] KyosukeNishidaandKoichiroYamauchi.2007. Detectingconceptdriftusing
cartographicvariables. Computersandelectronicsinagriculture24,3(1999), statisticaltesting.InInternationalconferenceondiscoveryscience.Springer,264–
131–151. 269.
[7] VitorCerqueira,HeitorMuriloGomes,andAlbertBifet.2020.Unsupervisedcon- [26] EwanSPage.1954.Continuousinspectionschemes.Biometrika41,1/2(1954),
ceptdriftdetectionusingastudent–teacherapproach.InInternationalconference 100–115.
ondiscoveryscience.Springer,190–204. [27] FábioPinto,MarcoOPSampaio,andPedroBizarro.2019. Automaticmodel
[8] VitorCerqueira,HeitorMuriloGomes,AlbertBifet,andLuisTorgo.2023.STUDD: monitoringfordatastreams.arXivpreprintarXiv:1908.04240(2019).
Astudent–teachermethodforunsupervisedconceptdriftdetection.Machine [28] StuartWRoberts.2000.Controlcharttestsbasedongeometricmovingaverages.
Learning112,11(2023),4351–4378. Technometrics42,1(2000),97–101.
[9] GregoryDitzlerandRobiPolikar.2012.Incrementallearningofconceptdriftfrom [29] GordonJRoss,NiallMAdams,DimitrisKTasoulis,andDavidJHand.2012.
streamingimbalanceddata.IEEEtransactionsonknowledgeanddataengineering Exponentiallyweightedmovingaveragechartsfordetectingconceptdrift.Pattern
25,10(2012),2283–2301. recognitionletters33,2(2012),191–198.
[10] PedroDomingosandGeoffHulten.2000.Mininghigh-speeddatastreams.In [30] RaquelSebastiaoandJoaoGama.2009.Astudyonchangedetectionmethods.In
ProceedingsofthesixthACMSIGKDDinternationalconferenceonKnowledge Progressinartificialintelligence,14thPortugueseconferenceonartificialintelligence,
discoveryanddatamining.71–80. EPIA,Vol.2009.
[11] DenisMoreiraDosReis,PeterFlach,StanMatwin,andGustavoBatista.2016.Fast [31] ViniciusMASouza.2018. Asphaltpavementclassificationusingsmartphone
unsupervisedonlinedriftdetectionusingincrementalkolmogorov-smirnovtest. accelerometerandcomplexityinvariantdistance. EngineeringApplicationsof
InProceedingsofthe22ndACMSIGKDDinternationalconferenceonknowledge ArtificialIntelligence74(2018),198–211.
discoveryanddatamining.1545–1554. [32] V.M.A.Souza,D.M.Reis,A.G.Maletzke,andG.E.A.P.A.Batista.2020.
[12] WilliamJFaithfull,JuanJRodríguez,andLudmilaIKuncheva.2019.Combin- ChallengesinBenchmarkingStreamLearningAlgorithmswithReal-worldData.
ingunivariateapproachesforensemblechangedetectioninmultivariatedata. DataMiningandKnowledgeDiscovery34(2020),1805–1858.doi:10.1007/s10618-
InformationFusion45(2019),202–214. 020-00698-5
[13] TomFawcettandFosterProvost.1999.Activitymonitoring:Noticinginterest- [33] WNickStreetandYongSeogKim.2001.Astreamingensemblealgorithm(SEA)
ingchangesinbehavior.InProceedingsofthefifthACMSIGKDDinternational forlarge-scaleclassification.InProceedingsoftheseventhACMSIGKDDinterna-
conferenceonKnowledgediscoveryanddatamining.53–62. tionalconferenceonKnowledgediscoveryanddatamining.377–382.
[14] IsvaniFrias-Blanco,JosédelCampo-Ávila,GonzaloRamos-Jimenez,Rafael [34] YibinSun,HeitorMuriloGomes,BernhardPfahringer,andAlbertBifet.2025.
Morales-Bueno,AgustinOrtiz-Diaz,andYailéCaballero-Mota.2014. Online EvaluationforRegressionAnalysesonEvolvingDataStreams.arXivpreprint
andnon-parametricdriftdetectionmethodsbasedonHoeffding’sbounds.IEEE arXiv:2502.07213(2025).
TransactionsonKnowledgeandDataEngineering27,3(2014),810–823. [35] AlexanderVergara,ShankarVembu,TubaAyhan,MargaretARyan,MargieL
[15] JoaoGama,PedroMedas,GladysCastillo,andPedroRodrigues.2004.Learning Homer,andRamónHuerta.2012.Chemicalgassensordriftcompensationusing
withdriftdetection.InBraziliansymposiumonartificialintelligence.Springer, classifierensembles.SensorsandActuatorsB:Chemical166(2012),320–329.
286–295. [36] GerhardWidmerandMiroslavKubat.1996.Learninginthepresenceofconcept
[16] JoaoGama,RaquelSebastiao,andPedroPereiraRodrigues.2013.Onevaluating driftandhiddencontexts.Machinelearning23,1(1996),69–101.
streamlearningalgorithms.Machinelearning90,3(2013),317–346. [37] GiacomoZiffer,FedericoGiannini,andEmanueleDellaValle.2024.Tenet:Bench-
[17] JoãoGama,Indre˙Žliobaite˙,AlbertBifet,MykolaPechenizkiy,andAbdelhamid markingDataStreamClassifiersinPresenceofTemporalDependence.In2024
Bouchachia.2014.Asurveyonconceptdriftadaptation.ACMcomputingsurveys IEEEInternationalConferenceonBigData(BigData).IEEE,1187–1196.
(CSUR)46,4(2014),1–37. [38] IndreŽliobaite.2010.Changewithdelayedlabeling:Whenisitdetectable?.In
[18] HeitorMGomes,AlbertBifet,JesseRead,JeanPaulBarddal,FabrícioEnembreck, 2010IEEEinternationalconferenceondataminingworkshops.IEEE,843–850.
BernhardPfharinger,GeoffHolmes,andTalelAbdessalem.2017. Adaptive
randomforestsforevolvingdatastreamclassification.MachineLearning106,9
(2017),1469–1495.
[19] Heitor Murilo Gomes, Anton Lee, Nuwan Gunasekara, Yibin Sun, Guil- A DriftSimulation
hermeWeigertCassales,JustinLiu,MarcoHeyden,VitorCerqueira,Maroua
Bahri,YunSingKoh,etal.2025.CapyMOA:efficientmachinelearningfordata A.1 SimulationFramework
streamsinpython.arXivpreprintarXiv:2502.07432(2025).
Algorithm1describestheprocedureforsimulatingdriftonreal-
[20] PauloMGonçalvesJr,SilasGTdeCarvalhoSantos,RobertoSMBarros,and
DaviCLVieira.2014.Acomparativestudyonconceptdriftdetectors.Expert worlddatastreamsbasedonMonteCarlotrials.
SystemswithApplications41,18(2014),8144–8156.
[21] MichaelHarries,NewSouthWales,etal.1999.Splice-2comparativeevaluation:
Electricitypricing.(1999). A.2 DriftTypes
[22] MarcoHeyden,EdouardFouché,VadimArzamasov,TanjaFenn,FlorianKalinke,
and Klemens Böhm. 2024. Adaptive Bernstein change detector for high- Algorithms2,3,4,and5describethespecificdrifttypesappliedin
dimensionaldatastreams.DataMiningandKnowledgeDiscovery38,3(2024), ourworkusingtheproposedsimulationframework.
1334–1363.
[23] DavidTseJungHuang,YunSingKoh,GillianDobbie,andRusselPears.2014.
Detectingvolatilityshiftindatastreams.In2014IEEEInternationalConference B Experiments
onDataMining.IEEE,863–868.
[24] ViktorLosing,BarbaraHammer,andHeikoWersing.2016.KNNclassifierwith B.1 ExperimentalSetup
selfadjustingmemoryforheterogeneousconceptdrift.In2016IEEE16thinter-
nationalconferenceondatamining(ICDM).IEEE,291–300. Tables3and4summarisethekeyparametersandconfiguration
poolconsideredfortheexperiments.

KDD’26,August09–13,2026,JejuIsland,RepublicofKorea Cerqueiraetal.
Algorithm1DriftSimulationFramework Algorithm3ClassLabelSwapDriftSimulation
Require: Data stream S, Drift function𝑔, Predictive model𝑀, Require: Instance𝐼 =(𝑥,𝑦),Selectedlabel𝑦 𝑠𝑒𝑙 ,Swaplabel𝑦 𝑠𝑤𝑎𝑝
| Changedetector𝐷 |                                          |     |     |     |       |     | Ensure: | Transformedinstance𝐼′ |          |     |     |     |
| --------------- | ---------------------------------------- | --- | --- | --- | ----- | --- | ------- | --------------------- | -------- | --- | --- | --- |
|                 | Numberoftrials𝑘,Driftwidth𝑤,Buffersizes𝑏 |     |     |     |       | ,𝑏  | 1:      | if𝐼.𝑦=𝑦               |          |     |     |     |
| Require:        |                                          |     |     |     | 𝑠𝑡𝑎𝑟𝑡 | 𝑒𝑛𝑑 |         |                       | 𝑠𝑒𝑙 then |     |     |     |
Detectionresultsforeachtrial 𝐼′ =(𝐼.𝑥,𝑦 ⊲Createinstancewithswappedlabel
| Ensure: |                |     |     |                    |     |     | 2:  |          | 𝑠𝑤𝑎𝑝) |     |     |     |
| ------- | -------------- | --- | --- | ------------------ | --- | --- | --- | -------- | ----- | --- | --- | --- |
| for𝑗    | =1to𝑘do        |     |     | ⊲MonteCarlotrials  |     |     |     | return𝐼′ |       |     |     |     |
| 1:      |                |     |     |                    |     |     | 3:  |          |       |     |     |     |
| 2:      | S𝜋 ←Shuffle(S) |     |     | ⊲Randompermutation |     |     | 4:  | endif    |       |     |     |     |
3: 𝑑 ←RandomInt(𝑏 ,|S𝜋|−𝑏 𝑒𝑛𝑑) ⊲Randomdrift 5: return𝐼 ⊲Instanceremainsunchanged
|     | 𝑠   |     | 𝑠𝑡𝑎𝑟𝑡 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
onset
|     | 𝑑 ←𝑑 | 𝑠+𝑤 |     | ⊲Driftendposition |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
4: 𝑒
Reset(𝑀,𝐷) ⊲Initializemodelanddetector Algorithm4FeaturePermutationDriftSimulation
5:
| 6:  | for𝑖 =1to|S𝜋|do |     |     |     |     |     |     | Instance𝐼 |     | =(𝑥,𝑦),Permutationindexvector𝜎 |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------------------------ | --- | --- |
Require:
| 7:  | 𝐼 ←S𝜋[𝑖] |     |     | ⊲Getinstance(𝑋,𝑦) |     |     |     | Transformedinstance𝐼′ |     |     |     |     |
| --- | -------- | --- | --- | ----------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
Ensure:
| 8:  | if𝑖 | <𝑑 then |     | ⊲Beforedriftonset |     |     |     |          |     |     |                              |     |
| --- | --- | ------- | --- | ----------------- | --- | --- | --- | -------- | --- | --- | ---------------------------- | --- |
|     |     | 𝑠       |     |                   |     |     | 1:  | 𝑥′ ←𝑥[𝜎] |     |     | ⊲Reorderfeaturesaccordingto𝜎 |     |
𝐼′ ←𝐼
| 9:  |         |          |        |                      |     |     | 2:  | 𝐼′ =(𝑥′,𝐼.𝑦) |     | ⊲Createinstancewithpermutedfeatures |     |     |
| --- | ------- | -------- | ------ | -------------------- | --- | --- | --- | ------------ | --- | ----------------------------------- | --- | --- |
|     | elseif𝑖 | ≥𝑑       |        | ⊲Afterdriftcompletes |     |     |     |              |     |                                     |     |     |
| 10: |         |          | 𝑒 then |                      |     |     | 3:  | return𝐼′     |     |                                     |     |     |
| 11: |         | 𝐼′ ←𝑔(𝐼) |        |                      |     |     |     |              |     |                                     |     |     |
| 12: | else    |          |        | ⊲Gradualdriftregion  |     |     |     |              |     |                                     |     |     |
13: 𝑝 ←(𝑖−𝑑 𝑠)/𝑤 Algorithm5FeatureDistributionDriftSimulation
|     |                    | 𝐼′ ←𝑔(𝐼)withprobability𝑝,else𝐼′ |     |     | ←𝐼         |     |          |           |      |                                 |     |     |
| --- | ------------------ | ------------------------------- | --- | --- | ---------- | --- | -------- | --------- | ---- | ------------------------------- | --- | --- |
| 14: |                    |                                 |     |     |            |     | Require: | Instance𝐼 |      | =(𝑥,𝑦),Featureindex𝑗,Threshold𝜏 |     |     |
| 15: | endif              |                                 |     |     |            |     | Ensure:  | Instance𝐼 |      | orNull(iffiltered)              |     |     |
| 16: | 𝑦ˆ←𝑀.Predict(𝐼′.𝑋) |                                 |     |     | ⊲Inference |     |          | if𝐼.𝑥[𝑗]  | >𝜏   |                                 |     |     |
|     |                    |                                 |     |     |            |     | 1:       |           | then |                                 |     |     |
17: 𝑒 ←Error(𝑦ˆ,𝐼′.𝑦) ⊲Computeerror returnNull ⊲Instanceisdropped
2:
| 18: | 𝐷.Update(𝑒) |     |     |     | ⊲Feeddetector |     |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
3: endif
if𝐷.Alarm()then
| 19: |     |     |     |     |     |     | 4:  | return𝐼 |     |     | ⊲Instanceiskeptunchanged |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | ------------------------ | --- |
Recorddetectionatposition𝑖
20:
| 21: | endif       |     |     |     |              |     |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| 22: | 𝑀.Train(𝐼′) |     |     |     | ⊲Updatemodel |     |     |     |     |     |     |     |
gradualdriftscenarios,respectively.Table11showstheF1score
23: endfor
24: Storeresultsfortrial𝑗 onsyntheticdatastreams,andTable12reportstheF1scoreacross
differentclassifiers.Below,weprovideadetailedanalysisofeach
25: endfor
setofresults.
DecomposingtheF1scoresintoprecisionandrecall(Tables??–
Algorithm2ClassPriorDriftSimulation 10)revealsdifferentprofilesacrossdetectorsandclarifieshowsome
methodsachievesimilarF1scoresthroughdifferentbehaviors.For
|          | Instance𝐼 | =(𝑥,𝑦),Selectedlabel𝑦 |     | ,Skipprobability |     |     |     |     |     |     |     |     |
| -------- | --------- | --------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Require: |           |                       |     | 𝑠𝑒𝑙              |     |     |     |     |     |     |     |     |
𝑝 example,GMAexhibitsarecall-dominatedprofile:itachievesnear-
𝑠𝑘𝑖𝑝
perfectrecall(0.97–1.0acrossalldrifttypesandabruptnesscondi-
| Ensure: | Instance𝐼 | orNull(ifskipped) |     |     |     |     |     |     |     |     |     |     |
| ------- | --------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tions),meaningitdetectsalmosteverydrift.However,itsprecision
| 1: if𝐼.𝑦=𝑦 |     | then |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝑠𝑒𝑙 isamongthelowest(0.05–0.08),indicatingthatthemajorityofits
| 2:  | Generaterandomvalue𝑟 |     | ∼Uniform(0,1) |     |     |     |     |     |     |     |     |     |
| --- | -------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alarmsarefalsepositives.Thispatternsuggeststhatthismethodis
|     | if𝑟 <𝑝 |           |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3:  |        | 𝑠𝑘𝑖𝑝 then |     |     |     |     |     |     |     |     |     |     |
returnNull ⊲Instanceisdropped overlysensitive,triggeringalarmsfrequentlyregardlessofwhether
4:
|     |     |     |     |     |     |     | a genuine |     | drift has | occurred. | In practice, however, | this kind of |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------- | --------- | --------------------- | ------------ |
5: endif
behaviorleadstoexcessiveandunnecessarymodelretraining,un-
6: endif
derminingtrustinthedetectionsystem.Otherdetectorssuchas
| 7: return𝐼 |     |     | ⊲Instanceiskeptunchanged |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RDDMexhibitasimilarprofile,achievinghighrecallbutlowpreci-
sion.SEED,ABCD,andSTEPDshowarelativelybalancedprecision
andrecalltrade-offacrossallscenarios.Finally,undergradualdrift
B.2 Results conditions,overallscoresarelowerthanforabruptdrifts,butthe
Thissectionpresentsthecompleteexperimentalresultsobtained relativeperformanceofdetectorsislargelypreserved.
fromevaluatingthedriftdetectionmethodsacrossalldatasetsand Figure6displaystheaverageexecutiontime(inminutes)for
driftscenarios.Similarlytothemaincontent,inalltables,bold eachdriftdetectionmethod,aggregatedacrossalldatasets.The
valuesindicatethebestperformingmethodforeachdrifttype,while executiontimeencompassesthecompletedetectionpipeline.This
underlinedvaluesdenotethesecond-bestperformance.Tables5 metric complements the main results by providing insight into
and??reporttheaverageF1detectionscoresforabruptandgradual the computational overhead associated with each detector. The
driftscenarios,respectively.Tables??and8presenttheaverage computationalcostvariesacrossmethods.Mostmethodsshowa
precisionscoresforabruptandgradualdriftscenarios,respectively. similarcost,exceptforABCD,ABCD(X),andSTUDDwhicharemore
| Tables | 9 and | 10 report | the average recall | scores | for abrupt | and | expensive. |     |     |     |     |     |
| ------ | ----- | --------- | ------------------ | ------ | ---------- | --- | ---------- | --- | --- | --- | --- | --- |

AFrameworkforEvaluatingandBenchmarkingConceptDriftDetectionMethods KDD’26,August09–13,2026,JejuIsland,RepublicofKorea
Table4:DetectorParameterSearchSpace (e.g.,0.82forSEED,0.78forSTEPDandHDDMA),whileotherstendto
producelowerscores.
| Detector Parameter | Values                       |     |       |     |     |     |
| ------------------ | ---------------------------- | --- | ----- | --- | --- | --- |
| ABCD delta_drift   | 0.001,0.002,0.0001,0.01,0.02 |     |       |     |     |     |
| delta_warn         | 0.1,0.01                     |     | STEPD |     |     |     |
| encoding_factor    | 0.3,0.5,0.7                  |     |       |     |     |     |
| model_id           | kpca,ae                      |     | SEED  |     |     |     |
| num_splits         | 20,50,100                    |     |       |     |     |     |
DDM
| ABCD(X) delta_drift | 0.001,0.002,0.0001,0.01,0.02 |     | CUSUM |     |     |     |
| ------------------- | ---------------------------- | --- | ----- | --- | --- | --- |
| delta_warn          | 0.1,0.01                     |     |       |     |     |     |
| encoding_factor     | 0.3,0.5,0.7                  |     | PH    |     |     |     |
| model_id            | kpca,ae                      |     |       |     |     |     |
EWMA
| num_splits | 20,50,100 |     |     |     |     |     |
| ---------- | --------- | --- | --- | --- | --- | --- |
rotceteD
| ADWIN delta           | 0.001,0.002,0.005,0.01,0.0005,0.0001 | HDDMA |       |     |     |     |
| --------------------- | ------------------------------------ | ----- | ----- | --- | --- | --- |
| CUSUM min_n_instances | 30,50,100,300,500,1000,2000          |       | GMA   |     |     |     |
| delta                 | 0.001,0.002,0.005,0.0001,0.01        |       |       |     |     |     |
| lambda_               | 50,100,150,300,500,1000,2000         |       | ADWIN |     |     |     |
RDDM
| DDM min_n_instances | 30,50,100,300,500,1000,2000    |     |     |     |     |     |
| ------------------- | ------------------------------ | --- | --- | --- | --- | --- |
| out_control_level   | 1.75,2,2.5,3.0,2.25,2.75,3.5,4 |     |     |     |     |     |
HDDMW
| EWMA min_n_instances | 50,100,300,500,1000,2000,3000,5000,10000 |     |     |     |     |     |
| -------------------- | ---------------------------------------- | --- | --- | --- | --- | --- |
STUDD
| lambda_                | 0.9,0.01,0.001,0.1,0.005,0.002,0.0001 |         |      |     |     |     |
| ---------------------- | ------------------------------------- | ------- | ---- | --- | --- | --- |
| GMA min_n_instances    | 30,50,100,300,500,1000,2000           |         | ABCD |     |     |     |
| lambda_                | 0.001,0.002,0.01,0.1,0.5,1,2,3,5      |         |      |     |     |     |
| alpha                  | 0.99,0.995,0.9,0.8,0.7,0.5,0.1,0.01   | ABCD(X) |      |     |     |     |
|                        |                                       |         | 0 5  | 10  | 15  | 20  |
| HDDMA drift_confidence | 0.001,0.002,0.005,0.01,0.0001         |         |      |     |     |     |
CPU Time (minutes)
| test_type              | Two-sided,One-sided           |     |     |     |     |     |
| ---------------------- | ----------------------------- | --- | --- | --- | --- | --- |
| HDDMW drift_confidence | 0.001,0.002,0.005,0.01,0.0001 |     |     |     |     |     |
test_type Two-sided,One-sided Figure 6: Average execution time of each drift detection
| lambda_            | 0.05,0.001,0.1,0.01,0.0001        | methodacrossalldatasets |     |     |     |     |
| ------------------ | --------------------------------- | ----------------------- | --- | --- | --- | --- |
| PH min_n_instances | 30,50,100,300,500,1000,2000       |                         |     |     |     |     |
| delta              | 0.001,0.002,0.005,0.01,0.0001,0.1 |                         |     |     |     |     |
| lambda_            | 30,50,100,300,500,1000,2000       |                         |     |     |     |     |
alpha 0.99,0.999,0.995,0.9,0.8,0.5 Table5:AverageF1detectionscoreofdriftdetectorsacross
differentdatasetsforabruptdrifts
| RDDM min_n_instances | 30,50,100,300,500,1000,2000   |     |     |     |     |     |
| -------------------- | ----------------------------- | --- | --- | --- | --- | --- |
| drift_level          | 1.9,2,2.1,2.25,2.5,3,1.5,1.75 |     |     |     |     |     |
SEED delta 0.0001,0.001,0.01,0.05,0.1 Detector Feature Feat.Per- Class Class
epsilon_prime 0.0025,0.01,0.005,0.0075 Filtering mutation Prior Swap
| block_size        | 32,50,100,150,256                |         |      |      |      |      |
| ----------------- | -------------------------------- | ------- | ---- | ---- | ---- | ---- |
| alpha             | 0.2,0.3,0.4,0.5,0.6,0.7,0.8      | ABCD    | 0.11 | 0.51 | 0.16 | 0.25 |
|                   |                                  |         | 0.02 |      | 0.0  | 0.0  |
| STEPD window_size | 30,50,100,300,500,1000           | ABCD(X) |      | 0.98 |      |      |
|                   |                                  |         | 0.24 | 0.27 |      | 0.16 |
| alpha_drift       | 0.001,0.002,0.003,0.005,0.01,0.1 | ADWIN   |      |      | 0.31 |      |
STUDD min_n_instances 500,1000,2000,5000 CUSUM 0.19 0.01 0.22 0.1
|     |     | DDM  | 0.16 | 0.02 | 0.19 | 0.09 |
| --- | --- | ---- | ---- | ---- | ---- | ---- |
|     |     | EWMA | 0.09 | 0.0  | 0.06 | 0.03 |
|     |     | GMA  | 0.1  | 0.13 | 0.12 | 0.15 |
Table11reportsF1scoresonthreesyntheticdatastreamgenera-
|                                                              |     |       | 0.17 | 0.36 | 0.2  | 0.24 |
| ------------------------------------------------------------ | --- | ----- | ---- | ---- | ---- | ---- |
| tors(Agrawal,SEA,STAGGER),eachcomposedofeitherabruptor       |     | HDDMA |      |      |      |      |
|                                                              |     |       | 0.18 | 0.25 | 0.19 | 0.21 |
| gradualdrifts,usingonlytheerror-trackingdetectors.Theoverall |     | HDDMW |      |      |      |      |
rankingof detectorsonsynthetic streamsbroadly corroborates PH 0.02 0.0 0.06 0.09
|     |     | RDDM | 0.2 | 0.04 | 0.15 | 0.1 |
| --- | --- | ---- | --- | ---- | ---- | --- |
thefindingsonreal-worlddata:SEED,ABCD,andSTEPDachievethe
|     |     | SEED | 0.24 | 0.61 | 0.3 | 0.37 |
| --- | --- | ---- | ---- | ---- | --- | ---- |
highestF1scoresacrossmostsyntheticscenarios.
|                                                         |     | STEPD |      | 0.53 | 0.28 | 0.33 |
| ------------------------------------------------------- | --- | ----- | ---- | ---- | ---- | ---- |
| Table12reportsF1scoresforfiveclassifiers—AdaptiveRandom |     |       | 0.26 |      |      |      |
|                                                         |     |       | 0.17 | 0.27 | 0.1  | 0.11 |
| Forest(ARF),HoeffdingTree,NaiveBayes,OnlineBagging,and  |     | STUDD |      |      |      |      |
OzaBoost—ontheElectricitydatasetusingthelabelswapdrifttype.
Thisexperimentassesseswhethertherelativeperformanceofdetec-
torsissensitivetotheunderlyinglearningalgorithm.Therelative
rankingofdetectorsislargelypreservedacrossclassifiers.Thissta-
bilitysuggeststhatthefindingsfromourmainexperiments,which
usetheHoeffdingTree,arenotaresultofaparticularlearner’ser-
rordynamics.AbsoluteF1scores,however,varynoticeablyacross
classifiers.OzaBoostconsistentlyyieldsthehighestdetectionscores

KDD’26,August09–13,2026,JejuIsland,RepublicofKorea Cerqueiraetal.
Table8:Averageprecisionscoreofdriftdetectorsacrossdif- Table10:Averagerecallscoreofdriftdetectorsacrossdiffer-
| ferentdatasetsforgradualdrifts |     |     |     |     | entdatasetsforgradualdrifts |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- |
Detector Feature Feat.Per- Class Class Detector Feature Feat.Per- Class Class
|         | Filtering | mutation | Prior | Swap |         | Filtering | mutation | Prior | Swap |
| ------- | --------- | -------- | ----- | ---- | ------- | --------- | -------- | ----- | ---- |
| ABCD    | 0.03      | 0.26     | 0.08  | 0.17 | ABCD    | 0.04      | 0.5      | 0.08  | 0.28 |
|         | 0.0       |          | 0.0   | 0.0  |         | 0.0       | 0.76     | 0.0   | 0.0  |
| ABCD(X) |           | 0.66     |       |      | ABCD(X) |           |          |       |      |
|         | 0.07      | 0.03     | 0.1   | 0.05 |         | 0.24      | 0.1      | 0.34  | 0.27 |
| ADWIN   |           |          |       |      | ADWIN   |           |          |       |      |
| CUSUM   | 0.1       | 0.02     | 0.13  | 0.08 | CUSUM   | 0.14      | 0.02     | 0.17  | 0.11 |
| DDM     | 0.07      | 0.04     | 0.08  | 0.06 | DDM     | 0.89      | 0.69     | 0.89  | 0.78 |
| EWMA    | 0.05      | 0.0      | 0.05  | 0.04 | EWMA    | 0.06      | 0.01     | 0.06  | 0.03 |
| GMA     | 0.07      | 0.07     | 0.07  | 0.08 | GMA     |           |          |       |      |
|         |           |          |       |      |         | 1.0       | 1.0      | 1.0   | 1.0  |
|         | 0.06      | 0.09     | 0.13  | 0.05 |         | 0.09      | 0.17     | 0.15  | 0.11 |
| HDDMA   |           |          |       |      | HDDMA   |           |          |       |      |
| HDDMW   | 0.07      | 0.08     | 0.07  | 0.09 | HDDMW   | 0.65      | 0.78     | 0.66  | 0.81 |
| PH      | 0.06      | 0.01     | 0.12  | 0.05 | PH      | 0.05      | 0.01     | 0.09  | 0.05 |
| RDDM    | 0.07      | 0.07     | 0.07  | 0.08 | RDDM    | 1.0       | 0.99     | 1.0   | 1.0  |
| SEED    | 0.09      | 0.33     | 0.13  | 0.23 | SEED    | 0.19      | 0.87     | 0.27  | 0.59 |
|         |           | 0.33     |       |      |         | 0.19      | 0.84     | 0.28  | 0.54 |
| STEPD   | 0.11      |          | 0.16  | 0.23 | STEPD   |           |          |       |      |
|         | 0.09      | 0.1      | 0.09  | 0.06 |         | 0.43      | 0.61     | 0.37  | 0.41 |
| STUDD   |           |          |       |      | STUDD   |           |          |       |      |
Table9:Averagerecallscoreofdriftdetectorsacrossdifferent Table11:F1scoresonsyntheticdatastreams(Agrawal,SEA,
datasetsforabruptdrifts STAGGER)composedofabruptorgradualdrifts.
| Detector | Feature | Feat.Per- | Class | Class | Mode | ABRUPT |     | GRADUAL |     |
| -------- | ------- | --------- | ----- | ----- | ---- | ------ | --- | ------- | --- |
Filtering mutation Prior Swap Stream Agrawal SEA STAGGER Agrawal SEA STAGGER
|         |      |      |      |      |       | 0.57 0.07 |      | 0.60 0.33 | 0.44 |
| ------- | ---- | ---- | ---- | ---- | ----- | --------- | ---- | --------- | ---- |
|         | 0.14 | 0.7  | 0.17 | 0.37 | ABCD  |           | 0.40 |           |      |
| ABCD    |      |      |      |      |       | 0.26 0.04 | 0.04 | 0.54 0.54 | 0.08 |
|         | 0.01 | 0.96 | 0.0  | 0.0  | ADWIN |           |      |           |      |
| ABCD(X) |      |      |      |      |       | 0.12 0.00 | 0.04 | 0.17 0.22 | 0.03 |
CUSUM
| ADWIN | 0.4  | 0.55 | 0.51 | 0.47 | DDM   | 0.10 0.00 | 0.04 | 0.34 0.36 | 0.11 |
| ----- | ---- | ---- | ---- | ---- | ----- | --------- | ---- | --------- | ---- |
| CUSUM | 0.23 | 0.02 | 0.26 | 0.18 | EWMA  | 0.00 0.00 | 0.00 | 0.00 0.00 | 0.00 |
| DDM   | 0.23 | 0.04 | 0.29 | 0.21 | GMA   | 0.18 0.19 | 0.16 | 0.40 0.39 | 0.45 |
| EWMA  | 0.1  | 0.0  | 0.08 | 0.05 | HDDMA | 0.22 0.05 | 0.12 | 0.32 0.26 | 0.16 |
|       |      |      |      |      | HDDMW | 0.16 0.09 | 0.05 | 0.45 0.39 | 0.50 |
| GMA   | 0.97 | 1.0  | 1.0  | 1.0  |       | 0.06 0.00 | 0.00 | 0.14 0.07 | 0.03 |
|       | 0.23 | 0.66 | 0.3  | 0.45 | PH    |           |      |           |      |
| HDDMA |      |      |      |      |       | 0.15 0.08 | 0.04 | 0.40 0.43 | 0.41 |
RDDM
| HDDMW | 0.33 | 0.67 | 0.45 | 0.54 | SEED  | 0.46      | 0.35 |           | 0.47 |
| ----- | ---- | ---- | ---- | ---- | ----- | --------- | ---- | --------- | ---- |
|       |      |      |      |      |       | 0.58      |      | 0.61 0.63 |      |
| PH    | 0.02 | 0.0  | 0.04 | 0.07 | STEPD | 0.49 0.49 | 0.29 | 0.61 0.61 | 0.42 |
| RDDM  | 0.33 | 0.11 | 0.32 | 0.29 |       |           |      |           |      |
SEED 0.29 0.93 0.36 0.58 Table12:F1scoresofeachdetectorfordifferentclassifiers
|       | 0.36 | 0.92 | 0.39 | 0.58 |                                                       |                   |            |               |          |
| ----- | ---- | ---- | ---- | ---- | ----------------------------------------------------- | ----------------- | ---------- | ------------- | -------- |
| STEPD |      |      |      |      | usingtheElectricitydatastreamandthelabelswappingdrift |                   |            |               |          |
| STUDD | 0.48 | 0.75 | 0.38 | 0.41 | type.                                                 |                   |            |               |          |
|       |      |      |      |      | Learner                                               | ARF HoeffdingTree | NaiveBayes | OnlineBagging | OzaBoost |
|       |      |      |      |      | ABCD                                                  | 0.51 0.33         |            | 0.35          | 0.52     |
0.53
|     |     |     |     |     | ADWIN | 0.23 0.19 | 0.44 | 0.22 | 0.68 |
| --- | --- | --- | --- | --- | ----- | --------- | ---- | ---- | ---- |
|     |     |     |     |     | CUSUM | 0.0 0.1   | 0.37 | 0.01 | 0.6  |
|     |     |     |     |     | DDM   | 0.03 0.06 | 0.25 | 0.06 | 0.4  |
|     |     |     |     |     | EWMA  | 0.0 0.0   | 0.0  | 0.0  | 0.0  |
|     |     |     |     |     | GMA   | 0.2 0.18  | 0.15 | 0.2  | 0.17 |
|     |     |     |     |     | HDDMA | 0.56 0.51 | 0.41 | 0.47 | 0.78 |
|     |     |     |     |     | HDDMW | 0.62 0.42 | 0.22 | 0.46 | 0.63 |
|     |     |     |     |     |       | 0.0 0.02  | 0.06 | 0.0  | 0.78 |
PH
|     |     |     |     |     |     | 0.06 0.12 | 0.18 | 0.08 | 0.3 |
| --- | --- | --- | --- | --- | --- | --------- | ---- | ---- | --- |
RDDM
|     |     |     |     |     |       | 0.51 | 0.5  | 0.53 |      |
| --- | --- | --- | --- | --- | ----- | ---- | ---- | ---- | ---- |
|     |     |     |     |     | SEED  | 0.54 |      |      | 0.82 |
|     |     |     |     |     | STEPD | 0.57 | 0.46 |      | 0.78 |
|     |     |     |     |     |       | 0.54 |      | 0.56 |      |