---
conversion_metadata:
  converted_at: "2026-07-21T07:07:34Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Li & Gautam.pdf"
  source_pdf_sha256: "83a6beaee34cac57acd8b0474ddd752943a540a202932839f9f9f09751a7b918"
  page_count: 10
  markdown_char_count: 45550
---

Segmented Confidence Sequences and Multi-Scale Adaptive
Confidence Segments for Anomaly Detection in Nonstationary
Time Series
MuyanAnnaLi AditiGautam
NVIDIA NVIDIA
SantaClara,USA SantaClara,USA
annali@nvidia.com adgautam@nvidia.com
Abstract forpreventingfaults,reducingrisk,andensuringoperationalrelia-
Astimeseriesdatabecomeincreasinglyprevalentindomainssuch bility[7].Unlikestaticdatasets,timeseriesoftenexhibitevolving
asmanufacturing,IT,andinfrastructuremonitoring,anomalyde- behavior,includingtrends,seasonality,andabruptregimeshifts,
tectionmustadapttononstationaryenvironmentswherestatistical makinganomalydetectionaparticularlychallengingproblem.
propertiesshiftovertime.Traditionalstaticthresholdsareeasily Inrecentyears,researchershavedevelopedadvancedtechniques
renderedobsoletebyregimeshifts,conceptdrift,ormulti-scale thatgobeyondsimplestaticthresholds.Approachessuchasro-
changes.Toaddressthesechallenges,weintroduceandempirically bustmovingwindows,onlinequantileestimation,andconfidence
evaluatetwonoveladaptivethresholdingframeworks:Segmented sequencetheoryhaveemergedtoprovidemoreadaptiveandsta-
ConfidenceSequences(SCS)andMulti-ScaleAdaptiveConfidence tisticallyprincipledanomalydetection[9,13].Thesemethodsaim
Segments(MACS).Bothleveragestatisticalonlinelearningand to balance computational efficiency with real-time adaptability,
segmentationprinciplesforlocal,contextuallysensitiveadaptation, enablingdetectionsystemstorespondtochangingdatadynamics.
maintainingguaranteesonfalsealarmratesevenunderevolving However,existingadaptivethresholdingmethodsoftenstruggle
distributions.Ourexperimentsacrosssixpublicbenchmarkdatasets whendataexhibitmultipletemporalscalesorsuddenregimeshifts.
showsignificantF1-scoreimprovementcomparedtotraditional Fixed-windoworglobalpercentile-basedstrategiesmayeitherfail
percentileandrollingquantileapproaches.Thisworkdemonstrates tocapturelocalvariations,leadingtomissedanomalies,orproduce
thatrobust,statisticallyprincipledadaptivethresholdsenablere- excessivefalsepositiveswhenthebaselinedrifts[4].Thishighlights
liable, interpretable, and timely detection of diverse real-world theneedforathresholdingframeworkthatcansimultaneously
anomalies. adapttobothabruptandgradualchangesindatadistribution.
Toaddressthesechallenges,wecontributetwonovelframeworks
CCSConcepts foradaptivethresholding.
•Computingmethodologies→Machinelearning;Anomaly
• SegmentedConfidenceSequences(SCS)segmentstimeseries
detection;•Informationsystems→Dataanalytics.
byregime,maintainingdistinctconfidence-basedboundsper
segment,andadaptstolocalratherthanglobalstatistics.
Keywords
• Multi-ScaleAdaptiveConfidenceSegments(MACS)isan
AnomalyDetection,AdaptiveThresholding,ConfidenceSequences, approachthatadaptsdetectionsimultaneouslyatmultiple
Multi-ScaleAnalysis,NonstationaryTimeSeries windowlengths,enablingthedetectionofbothrapidbursts
andslowregimechanges.
ACMReferenceFormat:
MuyanAnnaLiandAditiGautam.2025.SegmentedConfidenceSequences • Comprehensiveexperimentalevaluationsupportingstatisti-
andMulti-ScaleAdaptiveConfidenceSegmentsforAnomalyDetectionin callysignificantimprovementsovertraditionalpercentileor
NonstationaryTimeSeries.In20255thInternationalConferenceonArtificial fixedadaptivethresholds.
IntelligenceandApplicationTechnologies(AIAT2025),December04–06,2025,
Kyoto,Japan.ACM,NewYork,NY,USA,10pages.https://doi.org/10.1145/
3787120.3787130 2 RelatedWork
2.1 StaticandTraditionalThresholding
1 Introduction
Earlyapproachesreliedonfixedglobalthresholds–oftenprescribed
Timeseriesdataareubiquitousacrossmodernapplications,fromin- asmean±𝑘𝜎orastaticquantile–assumingstationarityandi.i.d.
dustrialprocessmonitoringandpredictivemaintenancetofinancial
observations[7].Althougheasytoimplement,thesemethodsfail
marketsandsensor-drivensystems.Detectinganomalies—unusual
underconceptdriftordynamicvarianceandarepronetofalse
patternsorbehaviorsthatdeviatefromexpectedtrends—iscrucial
positivesinpracticalsystems[5].
Percentile-basedapproaches,suchasthe99thpercentilethresh-
old,adjustforheavytailsbutstillfalterunderpersistentdistribu-
ThisworkislicensedunderaCreativeCommonsAttribution4.0InternationalLicense. tionaldriftornonstationarity,asshowninbenchmarkstudies[8].
AIAT2025,Kyoto,Japan MethodsbasedonExtremeValueTheory(EVT)andthePeak-Over-
©2025Copyrightheldbytheowner/author(s).
Threshold(POT)modeltheempiricaltailbeyondahighthreshold
ACMISBN979-8-4007-2290-5/25/12
https://doi.org/10.1145/3787120.3787130 butstillassumethethresholdregimeisquasi-stationary[8].
6

AIAT2025,December04–06,2025,Kyoto,Japan LiandGautam
2.2 SlidingWindows,RollingStatistics,and confidencesequenceismaintainedforanomalyscorethresholds,us-
MovingQuantiles ingHoeffding’sinequalityfornon-parametricbounds[9].Segment-
specificanomalyflagsaretriggeredifnewscoresexceedtheupper
Adaptivemethodsusingslidingwindowsrecalculatethresholds
confidenceboundorfallbelowthelowerconfidencebound.
overarecentwindow–updatingthemean,standarddeviation,
or quantile in an online manner [1]. The exponential weighted
movingaverage(EWMA)improvesrapidadaptationtotrendsor
regimeswitches,butwindowsizedeterminessensitivityandis
oftenhardtotune[5].Non-parametricdynamicmodelsfurther
reducerelianceondistributionalassumptionsandaresuperiorin
recall[11].
2.3 Model-BasedandMachineLearning
Approaches
Forecasting-model-baseddetectionfitsmodelssuchasARIMAor
seasonaldecomposition,thentestsforoutliersinthemodelresid-
uals[6].Moreadvancedapproachesleverageautoencoders,deep
neuralnetworks,orreinforcementlearningagentstolearncontext-
sensitiveanomalyscoresordirectlyoptimizedetectionperformance
Figure1:IllustrationoftheSCSflow.
[3,4,14].However,thesemethodseitherlackexplicitstatistical
errorguaranteesorrequireconsiderablelabeledanomalydata.
SCSbeginsbypartitioningthetimeseriesintolocallystationary
2.4 ConfidenceSequencesforOnline segments,usingeitherAdaptivePiecewiseConstantApproximation
Adaptation (APCA)orfeature-basedK-meansclustering[2].APCAoperates
byiterativelyidentifyingoptimalsplitpointsthatminimizetotal
Confidencesequences(CS)–time-uniformintervalsguaranteeing
reconstructionerror,definedasthesumofsquareddeviationsfrom
correctcoverageatalltimes–areafoundationforrigorousthresh-
themeanwithineachsegment.Specifically,foraproposedsplit,
olding in nonstationary data, allowing error rate control under
thereconstructionerroriscalculatedas:
arbitrarystopping[9].Recentalgorithmscanmaintainconfidence
boundsforquantilesormeans,enablingadaptiveanomalyscor- total_error=left_error+right_error (1)
ingrobusttodrift,heavytails,oroutliers[13].ApplyingCS-based ∑︁
thresholdselectiontostreaminganomalydetectionisapromising left_error= (𝑥 𝑖 −𝑥¯ left )2 (2)
andnewlyemergingdirection[9,12]. right_error= ∑︁ (𝑥 𝑗 −𝑥¯ right )2 (3)
2.5 Segmentation-BasedLocalThresholding Thisprocesscontinuesrecursivelyuntilsegmentsfallbelowamin-
imumlengthconstraintornofurtherimprovementisobserved
Segmentingtimeseriesintolocallystationaryregimes–viaAPCA
accordingtoaspecifiedthreshold.Forflatregionsofthetimese-
orclustering–bringsstatisticalhomogeneitytothresholdestima-
ries,identifiedbyacoefficientofvariationbelow0.1,APCAdefaults
tion,allowingeachregimetohavealocallyfitted,adaptiverule
tofixed-lengthsegmentation,wheresegmentsizeissetto:
[2,10].Recentapproachesuseclustering(e.g.,k-means)onsum-
(cid:106)𝑛 (cid:107)
maryfeaturestocaptureregimechange,butstatisticaldecision max(200, ) (4)
boundarieswithineachsegmentremainunderexplored. 15
Formorevariabledata,acandidatesplitisacceptedonlyifthe
3 Methods minimizedreconstructionerrorsatisfies:
Wefocusontwonovel,unsupervisedadaptivethresholdingstrate- min_error<no_split_error×
(5)
giesforstreamingtimeseries:SegmentedConfidenceSequences improvement_threshold
(SCS)andMulti-ScaleAdaptiveConfidenceSegments(MACS).Both
aredesignedforpracticalanomalydetectionpipelines(seeFigure1 Theimprovementthresholdissetto0.7forhigh-varianceseries
andFigure2). and0.5formoderate-varianceseries.
Alternatively,SCSsupportsaK-meanssegmentationapproach
thatclustersslidingwindowrepresentationsofthetimeseriesbased
3.1 SegmentedConfidenceSequences(SCS)
on statistical features. For each window, features including the
SCS first performs time series segmentation using either Adap-
mean,standarddeviation,median,andskewnessareextracted,and
tivePiecewiseConstantApproximation(APCA)-whichiteratively
theresultingfeaturevectorsarenormalizedusingStandardScaler.
splits at points that minimize reconstruction error - or feature-
Formulti-dimensionaltimeseriesdata,thedimensionalityisre-
basedK-meansclusteringusingsliding-windowstatistics[2].Each
ducedbyaveragingacrossthefeaturedimensionssuchthat:
segmentisassumedtobelocallystationary,allowingforregime-
specificanomalydetection.Withineachsegment,anindependent data_1d=mean(𝑋,axis=1) if𝑋 ∈R𝑛×𝑑,𝑑 >1 (6)
7

SegmentedConfidenceSequencesandMulti-ScaleAdaptiveConfidenceSegments
forAnomalyDetectioninNonstationaryTimeSeries AIAT2025,December04–06,2025,Kyoto,Japan
Incaseswheretheclusteringprocessfailsduetoinsufficientvari-
abilityordegeneratedistributions,theentiresequenceistreatedas
asinglesegmenttopreservestability.
Withineachresultingsegment,regardlessofthesegmentation
method,SCSmaintainsanindependentconfidencesequencefor
thresholdinganomalyscores.TheseboundsarederivedusingHoeffding-
styleinequalities[9]andareparameterizedbythelocalstandard
deviation of the segment’s scores. The width of the confidence
boundisinitiallysetas:
bound_width=1.5×std_score (7)
Itisthenscaledbyafactorthatreflectsthedesiredconfidence
level.Specifically,iftheconfidencelevelexceeds95%,theboundis
widenedbyafactorof1.2;ifitisbelow90%,theboundisnarrowed
to0.8.Thefinalconfidenceintervalforeachscoreisgivenby:
lower_bound=𝑥¯−bound_width (8)
Figure2:IllustrationoftheMACSflow.
upper_bound=𝑥¯+bound_width (9)
Toensurerobustnessandavoidfalsepositivesfromlocalfluctua- Specifically,ittracksshort(e.g.,50steps),medium(e.g.,100steps),
tions,SCSusesacompositedetectioncriterion:apointisflagged andlong(e.g.,500steps)timescales,eachofwhichindependently
asanomalousonlyifitviolatesboththeconfidenceboundsand maintainsaconfidencesequence[5].ThisstructureenablesMACS
aglobalpercentilethreshold.Formally,anintermediateanomaly todetectabroadspectrumofanomalies,fromshort-termburststo
indicatoriscomputedas: slow-movingregimeshifts.Tofurtherenhanceadaptability,MACS
anomalies=(𝑥 <lower_bound)∨ incorporatesanattentionmechanismthatdynamicallyweighsthe
(𝑥 >upper_bound) (10) importanceofeachtemporalscalebasedonlocalvariancepatterns
inthedata.
Thefinalanomalydecisionismadevia: Eachtemporalscalemaintainsitsownconfidencebounds,com-
final_anomalies=anomalies∧ putedusingthesegment’slocalstatistics.Foragivenwindow,the
(11) widthoftheconfidenceboundisinitializedas:
percentile_filter
bound_width=1.5×std_score (12)
Tosummarize,thealgorithmflowisoutlinedbelow:
Itisthenscaledaccordingtothedesiredconfidencelevel.Specif-
• SegmentationPhase:ApplyAPCAorK-meanstoidentify
ically,theboundwidthisincreasedby20%forhigh-confidence
regimeboundaries
settings(>95%)anddecreasedby20%forlow-confidencesettings
• BoundCalculation:Computeconfidenceboundsforeach
(<90%).Thefinalupperandlowerboundsateachscalearethen
segmentindependently
computedas:
• PointAssignment:Dynamicallyassignincomingpointsto
theircorrespondingsegment lower_bound=𝑥¯−bound_width (13)
• AnomalyDetection:Compareeachpointtosegment-specific upper_bound=𝑥¯+bound_width (14)
thresholds
Tointegratethesemultiplescales,MACSusesanattentionmech-
• Filtering:Applypercentile-basedfilteringforconservative-
anismthatadjuststherelativeimportanceofeachscalebasedon
ness
thelocalvarianceofthescores.Localvarianceisestimatedusinga
(ThepseudocodeofthealgorithmflowisinAppendixA.)
rollingvariancewindow,definedas:
Incomingdatapointsaredynamicallyassignedtotheircorre-
window=min(short_window,⌊𝑛/10⌋) (15)
spondingsegment,andanomaliesaredetectedbycomparingeach
pointtothesegment-specific,adaptivelyupdatedthreshold.This Basedontheleveloflocalvariance,differentattentionweightsare
approachensuresthatanomalydetectionislocallycalibratedto assigned:
thecurrentregime,providingrobustdetectionevenasthedata • Highvariance(>0.7):[0.6,0.3,0.1]
distributionshiftsovertime.Themethodisunsupervised,requires • Mediumvariance(>0.3):[0.2,0.6,0.2]
nolabeledanomalies,andissuitableforbothbatchandstreaming • Lowvariance(≤0.3):[0.1,0.3,0.6]
data.
MACScombinesthreetemporalviews-short,medium,long-to
staysensitivetobothbriefspikesandslowdriftswithouthand-
3.2 Multi-ScaleAdaptiveConfidenceSegments
retuningperdataset.Theweightingshould(i)favorthescalethat
(MACS)
is most informative for the current regime and (ii) remain sta-
MACSisdesignedtocaptureanomaliesoccurringatdifferenttem- bleenoughtoavoidthrashingorsingle-scaledomination.Short-
poralresolutionsbymaintainingmultiplerollingwindowsofvary- windowvariancerisesduringbursty,transientanomalies;long-
inglengthsinparallel. windowvariance/sloperiseduringgradualdriftsorlevelshifts.
8

AIAT2025,December04–06,2025,Kyoto,Japan LiandGautam
Therefore,inhigh-variancebursts,shortgetsmoremass(catches • AttentionCalculation:Computelocalvarianceanddeter-
spikes),andinlow-variancebuttrendingperiods,longgetsmore mineattentionweights
mass(capturesdrifts).Whenneitherextremedominates,medium • BoundCombination:Applyattentionmechanismtocom-
arbitrates(reducesfalsepositivesfromover-reactiveshortandiner- binemulti-scalebounds
tiafromlong).Theseweightscanbefinetunedbasedonthemodel • RegimeDetection:Identifystatisticalregimechangesusing
andthedataset.Inaddition,theweightsareusedtocomputea CUSUM-likelogic
combinedconfidenceboundasaweightedsumacrossscales: • DualDetection:Applyboththresholdviolationcounting
andattention-weightedbounds
3
combined_bound= ∑︁ weight𝑖 ·bound𝑖 (16) • Regime-AwareDecision:Combinedetectionmethodsbased
𝑖=1 onregimestate
• Filtering:Applypercentile-basedfilteringforconservative-
Inadditiontoconfidencesequences,MACSperformsregimechange
ness
detectionusingaCUSUM-likeprocedurebasedonrollingstatistics.
Ittracksboththerollingmeanandstandarddeviationoverthelong (ThepseudocodeofthealgorithmflowisinAppendixB.)
window.Aregimechangeisflaggedifthenormalizedchangein
3.3 ImplementationandPipeline
meanexceeds2.0,orifthechangeinstandarddeviationexceeds
1.5,definedrespectivelyas: Botharchitecturesprocessthetimeseriesasfollows:
mean_change=
𝑥¯current −𝑥¯
historical (17)
• Preprocessing:Removeapparentseasonalityorfitbasic
std +10−8 modeltocomputeresiduals(ifneeded)[6].
historical
std −std • Computeanomalyscores:Ascoringfunction(e.g.,abso-
std_change= s c t u d rrent + h 1 i 0 st − or 8 ical (18) lutechanges,reconstructionerrorsfromanautoencoder[3])
historical
isstreamed.
Whenaregimechangeisdetected,MACSappliesaconservative • Segmentation(SCSonly):SegmentincomingdatabyAPCA
thresholdingpolicythatrequiresagreementbetweentwoindepen-
orK-means.
dentdetectionmechanisms. • Adaptivethresholding:
ThedualdetectionapproachinMACSenhancesrobustnessby
– Updatesegment-orscale-specificconfidencesequences.
combiningtwocomplementarystrategies.First,athresholdviola-
– Optionallyapplyadditionalpercentileormixturemodel
tioncountingmechanismflagsapointasanomalousifitexceeds
filtering[11].
atleasttwooutofthreeindividualscale-specificthresholds: • Decisionlayer:Flaganomaliesusingcompositerules.
3
∑︁
violation= scale_anomalies𝑖 ≥2 (19) 4 ExperimentalResults
𝑖=1
WeevaluatedbothSCSandMACSagainsttraditionalandstate-
Second,MACSusestheattention-weightedcombinedbounds of-the-artadaptivemethodsonpublicdatasetscontainingground-
todetectdeviationsfromthecontextuallyprioritizedenvelope.A truthanomalylabels.Metricsincludetheconfusionmatrix,change
pointisflaggedasanomalousifitsscoreliesoutsidethiscombined inaccuracy,precision,recall,andF1-scorecomparedtobaseline.
range: TheexperimentsrunfromJuly5th,2025,toJuly31st,2025,overa
attention_anomalies=(𝑥 <combined_lower)∨ month.
(20)
(𝑥 >combined_upper)
4.1 ExperimentandDatasetDescription
Thefinaldecisionruleisregime-aware.Undernormaloperating 4.1.1 Baseline:TraditionalPercentileThresholding. Ourreference
conditions,anomaliesareflaggedsolelybasedontheattention- methodfollowstheclassicp-percentilerule.
weightedbounds.However,duringregimechanges,boththethresh-
(1) Reconstruction-errorvector
oldviolationandtheattentionanomalyconditionsmustbesatis- Let𝑥
𝑡
′betheoutputofthediffusionauto-encoderattime𝑡
fiedsimultaneously.Finally,MACSappliesanadditionalpercentile-
and𝑥 𝑡 theoriginalserieswindow.Wecomputethepoint-
basedfiltertoavoidover-detection.Thisstepdiscardslow-magnitude
wiseL2residual:
outliersbyrequiringanomalyscorestoexceedaglobalpercentile
threshold.Thefinalanomalymaskisobtainedas: 𝑟 𝑡 =∥𝑥 𝑡 −𝑥 𝑡 ′∥ 2 (22)
final_anomalies=anomalies∧ (2) Thresholdselection
percentile_filter (21) Aglobalcut-offischosenasthe99thpercentileoftheresidual
distributiononthetrainingsplit:
Thislayeredstructure–combiningmulti-scalebounds,adaptiveat-
tention,regimeawareness,andstatisticalfiltering–enablesMACS 𝜃 =Percentile 0.99 ({𝑟 𝑡} train ) (23)
tobalancesensitivityandprecisionindiversestreamingenviron- (3) Decisionrule
mentseffectively. Atimestampislabelledanomalousiff𝑟 𝑡 >𝜃.
Tosummarize,thealgorithmflowisoutlinedbelow: Althoughcomputationallytrivial,thisfixed-quantilerulecannot
• Multi-ScaleAnalysis:Calculateconfidenceboundsatthree adapttoregimeshiftsorchangesinerrorvariance–motivating
temporalscales theadaptiveapproachesstudiedintheremainderofthepaper.
9

SegmentedConfidenceSequencesandMulti-ScaleAdaptiveConfidenceSegments
forAnomalyDetectioninNonstationaryTimeSeries AIAT2025,December04–06,2025,Kyoto,Japan
Table1:Overviewofevaluateddatasets Table2:Cross-DatasetF1-ScoreDelta(vs.Baseline)
Name of Source&Scope AnomalyLabels Dataset SCSAPCA SCSKMEANS MACS
Dataset
|               |                       |          |           |          | WaferManufacturing |     | 1.91/2.13 | 0.93/1.41 | 2.17/2.23 |
| ------------- | --------------------- | -------- | --------- | -------- | ------------------ | --- | --------- | --------- | --------- |
| WaferManufac- | 151 inline            | process- | Pass/fail | ground   |                    |     |           |           |           |
|               |                       |          |           |          | CalIt2             |     | 0.46/0.42 | 0.70/0.24 | 0.46/0.42 |
| turing        | controltracesrecorded |          | truth     | from fab |                    |     |           |           |           |
by semiconductor test lines (≈10% GCP 4.84/7.94 1.60/3.58 4.84/7.94
|     |                |       |            |     | MSL |     | 4.30/5.01 | 0.33/1.61 | 4.30/4.98 |
| --- | -------------- | ----- | ---------- | --- | --- | --- | --------- | --------- | --------- |
|     | sensors during | wafer | defective) |     |     |     |           |           |           |
|     |                |       |            |     | SMD |     | 3.59/4.43 | 1.93/3.25 | 3.45/4.31 |
fabrication
|              |                       |        |                   |               | CPU-KPI |     | 1.15/1.73 | -0.18/0.28 | 1.05/1.69 |
| ------------ | --------------------- | ------ | ----------------- | ------------- | ------- | --- | --------- | ---------- | --------- |
| CalIt2       | People-count          | sensor | Event             | file with pe- |         |     |           |            |           |
|              | at UC-Irvine’s        | CalIt2 | riodsofabnormally |               |         |     |           |            |           |
|              | building (15          | weeks, | 48 high footfall  | (e.g.,        |         |     |           |            |           |
|              | half-hourslotsperday) |        | conferences)      |               |         |     |           |            |           |
| Google Cloud | 30 service-category   |        | Manually          | curated       |         |     |           |            |           |
Platform(GCP) KPIs collected from incidenttickets Table3:PerformancedeltaonWaferManufacturingdataset
|     | NVIDIA’s  | internal |     |     |     |     |                      |         |           |
| --- | --------- | -------- | --- | --- | --- | --- | -------------------- | ------- | --------- |
|     | DGX-Cloud | deploy-  |     |     |     |     |                      |         |           |
|     |           |          |     |     |     |     | ΔAccuracy ΔPrecision | ΔRecall | ΔF1-Score |
Method
ments
SCSAPCA
| Mars Science | NASA Mars            | Science | 73729         | test points |           |     |         |                |        |
| ------------ | -------------------- | ------- | ------------- | ----------- | --------- | --- | ------- | -------------- | ------ |
|              |                      |         |               |             | (𝛼=0.99)  |     | -0.0422 | -0.3282 3.9952 | 1.9074 |
| Laboratory   | Laboratory–55teleme- |         | with labelled | off-        |           |     |         |                |        |
| (MSL)        | try channels         | from    | nominal       | events      | SCSKMEANS |     |         |                |        |
(𝛼=0.99)
|     |                |     |                  |     |     |     | -0.0260 | -0.3999 1.6643 | 0.9262 |
| --- | -------------- | --- | ---------------- | --- | --- | --- | ------- | -------------- | ------ |
|     | Curiosityrover |     | (10.7%anomalous) |     |     |     |         |                |        |
MACSMulti-Scale
| ServerMachine | 5-week trace | from     | 28 Point-level      | labels |          |     |         |                |        |
| ------------- | ------------ | -------- | ------------------- | ------ | -------- | --- | ------- | -------------- | ------ |
|               |              |          |                     |        | (𝛼=0.99) |     | -0.0279 | -0.1890 3.9952 | 2.1705 |
| Dataset(SMD)  | production   | servers, | 38 (4.2%anomaly)and |        |          |     |         |                |        |
|               | KPIseach     |          | attributionmasks    |        | SCSAPCA  |     |         |                |        |
(𝛼=0.95)
CPU-KPI Seasonal CPU- Partialpointlabels -0.0830 -0.4290 6.1595 2.1289
SCSKMEANS
|     | utilisationKPIreleased |         | from           | capacity- |                 |     |         |                |        |
| --- | ---------------------- | ------- | -------------- | --------- | --------------- | --- | ------- | -------------- | ------ |
|     |                        |         |                |           | (𝛼=0.95)        |     | -0.0545 | -0.4656 3.3286 | 1.4148 |
|     | with Donut             | (public | planningalerts |           |                 |     |         |                |        |
|     | AIOpsbenchmark)        |         |                |           | MACSMulti-Scale |     |         |                |        |
(𝛼=0.95)
|                 |                                               |     |     |     |     |     | -0.0638 | -0.3651 5.6595 | 2.2349 |
| --------------- | --------------------------------------------- | --- | --- | --- | --- | --- | ------- | -------------- | ------ |
| 4.1.2 Datasets. | Detailsforalldatasetdistributionsarepresented |     |     |     |     |     |         |                |        |
inAppendixD.
4.1.3 Hyper-parametersandVariants.
| • Confidencelevel1−𝛼 |     | foradaptiveconfidencesequences: |     |     |     |     |     |     |     |
| -------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Table4:Anomalycountcomparison
{0.05,0.01}.
•
SegmentationforSCS:AdaptivePiecewiseConstantApprox-
|     |     |     |     |     | Method |     |     | TP TN | FP FN |
| --- | --- | --- | --- | --- | ------ | --- | --- | ----- | ----- |
imation(APCA)vs.k-meansonresidualvariance.
|     |     |     |     |     | TraditionalPercentile(99thpercentile) |     |     | 6 1608 | 12 137 |
| --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | ------ | ------ |
• Baseline:fixed99%percentileruledescribedabove.
|                           |                           |     |     |     | SCSAPCA(𝛼   | =0.99) |     | 30 1516 | 104 113 |
| ------------------------- | ------------------------- | --- | --- | --- | ----------- | ------ | --- | ------- | ------- |
| 4.1.4 EvaluationProtocol. | Foreverydatasetwecompute: |     |     |     |             |        |     |         |         |
|                           |                           |     |     |     | SCSKMEANS(𝛼 | =0.99) |     |         |         |
|                           |                           |     |     |     |             |        |     | 16 1556 | 64 127  |
• Confusion-matrixcounts(TP,FP,TN,FN)
|     |     |     |     |     | MACSMulti-Scale(𝛼 |     | =0.99) | 30 1539 | 81 113 |
| --- | --- | --- | --- | --- | ----------------- | --- | ------ | ------- | ------ |
• ChangeinAccuracy,Precision,Recall,F1comparedtobase-
| line |     |     |     |     | SCSAPCA(𝛼 | =0.95) |     | 43 1437 | 183 100 |
| ---- | --- | --- | --- | --- | --------- | ------ | --- | ------- | ------- |
• Proportionalimprovementoverthebaseline,calculatedas: SCSKMEANS(𝛼 =0.95)
|     |     |     |     |     |     |     |     | 26 1500 | 120 117 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- |
new_method−traditional_method MACSMulti-Scale(𝛼 =0.95) 40 1471 149 103
(24)
traditional_method
4.2 QuantitativeComparison
Toprovideabalancedassessmentandaddressgeneralizability,we
evaluatedSCS(APCAandK-means)andMACSacrosssixdiverse
publicbenchmarkdatasets:WaferManufacturing,CalIt2,Google
CloudPlatform(GCP),MarsScienceLaboratory(MSL),ServerMa- Acrossalldatasets,SCSandMACSsubstantiallyboostrecall
chineDataset(SMD),andCPU-KPI(Donut).Themainresultssum- andF1-scoreoverthetraditionalstaticpercentilebaseline.Notably,
marize the F1-score delta over the percentile baseline for each improvementsarestrongestondatasetswithpronouncedregime
approach;detailedresultsforallmetricsanddatasetsappearin shiftsormultiscaleanomalies(Wafer,SMD,GCP,MSL),whilethe
AppendixD. gains are less pronounced but still positive on noisier or more
stationarydata(CalIt2,CPU-KPI).Precisionconsistentlydeclines
inexchangeforincreasedrecall,reflectingtheenhancedsensitivity
ofadaptivethresholds.
Keyresults(WaferManufacturingdataset):
10

AIAT2025,December04–06,2025,Kyoto,Japan LiandGautam
filtering,whichisafivefoldincreaseoverthetraditionalmethod
(whichdetectsonlysixtruepositiveanomalies).
Indatasetswithmorecomplextemporaldynamics–suchas
sudden spikes, short bursts, or overlapping regimes – MACS is
expectedtooutperformduetoitsabilitytoattendtofine-grained
andcoarse-graineddeviationssimultaneously.Incontrast,SCSmay
bemoreeffectivewhenanomaliesarealignedwithpersistentstruc-
turalshifts,asitexplicitlyisolatesandmonitorsregime-specific
statistics.
Thesuccessofbothapproachesliesintheirabilitytolocalize
statisticalestimation.SCSadaptsquicklytochangesbysegmenting
thetimeseriesintoregionswithapproximatelystationarybehavior,
whichallowsfortightconfidenceboundswithineachregion.MACS,
ontheotherhand,incorporatestemporaldiversitythroughrolling
Figure3:ResultsforWaferManufacturingdataset𝛼 =0.99
windowsatmultipleresolutionsandadaptiveattentionweighting,
enablingittorespondtoanomaliesthatmanifestatdifferenttime
scales.Together,thesetechniquesrepresentaprincipledmovebe-
yondstaticglobalthresholdsandallowforamoreinterpretable,
robust,andtimelyanomalydetectioninreal-worldsettings.
Finally,whileremovingthepercentilefiltermaximizesrecall
andF1-score,thissettingmaynotalwaysbeoptimalinpractice.In
noisyenvironmentsorwhenfalsepositivescarrysignificantcost,
reintroducingpercentilefilteringmaybedesirabletobalanceinter-
pretabilitywithoperationalreliability.Thus,bothSCSandMACS
offerflexiblecontroloverthistrade-offdependingondeployment
constraints.
5 Discussion
Ourempiricalfindingsreinforcetheknownlimitationsofstatic
thresholdingtechniquessuchasglobalpercentilesandrollingquan-
tileswhenappliedtononstationarytimeseriesdata.Thesetradi-
Figure4:ResultsforWaferManufacturingdataset𝛼 =0.95
tionalapproachesfailtoaccountfordynamicdistributionalshifts,
leadingtopoorrecallandunder-detectionofrelevantanomalies
4.3 DetailedAnalysis [9].Incontrast,theproposedSCSandMACSmethodssubstan-
tiallyimproveperformancebyincorporatingstructuralandtem-
BothSegmentedConfidenceSequences(SCS)andMulti-ScaleAdap-
poral adaptivity. Specifically, they address evolving data behav-
tiveConfidenceSegments(MACS)showsignificantperformance
iorthroughsegmentation(SCS)andmulti-scaletemporalanalysis
improvementsoverthetraditionalstaticpercentilethresholding
(MACS),yieldingsignificantF1-scoregainswithonlymodestre-
approachacrossallevaluationmetrics.Mostnotably,theF1-score
ductionsinprecision.
ofbothSCSandMACSwithaconfidencelevelof𝛼 =0.99increases
approximatelytwicecomparedtothebaseline,highlightingthe
benefitofadaptive,context-awarethresholds.Whentheconfidence
levelisfurtherreducedto𝛼 =0.95,recallimprovessubstantially,
leadingtoanovertwotimesincreaseinF1-scorerelativetothe
baseline,evenatthecostofamoderatedeclineinprecision.
Thistrade-offbetweenrecallandprecisionreflectsatypicalpat-
terninadaptivedetection:loweringtheconfidencethresholdleads
tomoreaggressiveanomalydetection,capturingalargerpropor-
tionoftruepositivesattheriskofincludingmorefalsepositives.
SCS/MACSshrinklocaluncertaintywhenaregimeisstableand
widen/shiftboundsquicklyafterdrift.Thisincreasesthechance
ofcatchingweak,briefanomalies(higherrecall).However,during
highlyvolatileintervals,short-windowboundsreactaggressively
andmayflagnoiseoutliers(lowerprecision).Interestingly,this
behaviorisespeciallypronouncedwhenthepercentilefilterisdis-
abled.Asshownintheanomalycountcomparison,bothSCSand
MACSidentify30truepositiveanomaliesunder𝛼 =0.99withno Figure5:Illustrationofdifferentthresholdingstrategy
11

SegmentedConfidenceSequencesandMulti-ScaleAdaptiveConfidenceSegments
forAnomalyDetectioninNonstationaryTimeSeries AIAT2025,December04–06,2025,Kyoto,Japan
SCSisparticularlywell-suitedtosettingscharacterizedbyabrupt percentilefiltering,whilemaintainingrobustnessinunsupervised
regimeshiftsandpiecewisestationarity,wherelocaladaptation settings.
viasegmentationcapturesthechangingstatisticalpropertiesofthe Lookingahead,futureworkwillexploreextensionstomulti-
signal.Itsregime-specificconfidencesequencesofferinterpretable variate time series, correlated or structured input streams, and
boundsandfastdetectionofcontextualoutliers.MACS,ontheother integrationwithinference-basedanomalyscoringmethods.These
hand,ismoreflexibleacrossawiderrangeoftemporalpatterns.By directionsaimtoenhancefurthertheexpressiveness,generalizabil-
leveragingmultiplerollingwindowsandvariance-sensitiveatten- ity,anddeploymentreadinessofadaptivethresholdingstrategies
tionmechanisms,MACSgeneralizesacrossbothfasttransientsand forreal-worldanomalydetection.
slowdrifts.Thismakesitespeciallyeffectiveinenvironmentswith
layeredormulti-scaleanomalybehavior,suchasburstynetwork Acknowledgments
activityorgradualprocessdegradation[13].
ThisworkwassupportedbyDGXCAppliedAILab,NVIDIA.The
Akeyadvantageofbothapproachesliesintheirmodel-free,
authorsthankAaronErickson,SairaQureshi,SenaEkizandAIAT
unsupervisednature.Unlikemanymachinelearning-basedanom-
2025reviewersfortheirvaluablefeedbackwhichledtoimportant
alydetectors,whichoftenrelyonlabeledanomalyinstancesfor
improvements,includingexpandeddatasetanalysisandmethod-
trainingandhyperparametertuning,SCSandMACSoperatewith-
ologicaltransparency.
outsupervisionandretainexplicitcontroloverfalsealarmrates
throughstatisticallyprincipledconfidencesequences.Thisiscru- References
cialinhigh-stakesdomainssuchasmanufacturing,infrastructure
[1] CharuC.Aggarwal.2015.OutlierAnalysis(2nded.).Springer.
monitoring,orcybersecurity,whereexcessivefalsepositivescan [2] SeyedAminAghabozorgi,AliSeyedShirkhorshidi,andTehYingWah.2015.
desensitizeoperatorsanddegradetrustinautomatedsystems[3,7]. Time-seriesclustering–Adecadereview.InformationSystems53(2015),16–38.
[3] SubutaiAhmad,AlexanderLavin,ScottPurdy,andZuhaAgha.2017.Unsuper-
Despitetheseadvantages,ourworkalsohighlightssomesignifi-
visedreal-timeanomalydetectionforstreamingdata.Neurocomputing262(2017),
cantlimitationsandopenchallenges.TheperformanceofSCS,in 134–147.
particular,issensitivetothestructureofthetimeseries.Indatasets [4] KonstantinosBenidis,YoshuaBengio,MarcBlais,etal.2022.Machinelearning
fortimeseriesforecasting:challengesandopportunities.Proc.IEEE110,5(2022),
thatarehighlystationaryorexhibitnoisy,unstructuredbehavior, 656–678.
segmentationmayfailtoproducemeaningfulpartitions.Poorly [5] A.Blázquez-García,A.Conde,U.Mori,andJ.A.Lozano.2021. Areviewon
outlier/anomalydetectionintimeseriesdata.Comput.Surveys54,3(2021),1–33.
definedsegmentscanblurstatisticaldistinctionsandreducedetec-
[6] PeterJ.BrockwellandRichardA.Davis.2016.TimeSeries:TheoryandMethods
tionquality.Similarly,whileMACSbenefitsfromitsmulti-scale (2nded.).Springer.
architecture,itseffectivenesshingesontheappropriatecalibration [7] V.Chandola,A.Banerjee,andV.Kumar.2009. Anomalydetection:Asurvey.
Comput.Surveys41,3(2009),1–58.
ofattentionweightsandconfidencelevels–parametersthatmay
[8] MarcG.Genton,YuguoChen,andWilliamKleiber.2021. Statisticalmethods
needtuningdependingonthedomainandnoiseprofile. foroutlierdetection. AnnualReviewofStatisticsandItsApplication8(2021),
Animportantdirectionforfutureworkisthedevelopmentof 297–321.
[9] StevenR.Howard,AadityaRamdas,JasjeetSekhon,etal.2021.Time-uniform
robustonlinesegmentationalgorithmscapableofoperatingunder Chernoffboundsvianonnegativesupermartingales.ProbabilitySurveys18(2021),
adversarialconditionsorextremenonstationarity.Thisincludes 1–45.
[10] EamonnKeogh,KaushikChakrabarti,MichaelPazzani,andSharadMehrotra.
detectinglatentregimetransitionsthataresubtle,overlapping,or
2001.Locallyadaptivedimensionalityreductionforindexinglargetimeseries
inducedbyexternalinterventions.Additionally,whilethisstudy databases.InProceedingsofthe2001ACMSIGMODInternationalConferenceon
usedfixedwindowsizesforMACS,thereispotentialinexploring ManagementofData.151–162.
[11] PeterJ.Rousseeuw,MiaHubert,andWesleySchmitt.2020.Robuststatisticsfor
adaptive window scaling or learned attention mechanisms that
outlierdetection.WileyInterdisciplinaryReviews:DataMiningandKnowledge
adjustovertimebasedonpredictiveuncertaintyorperformance Discovery10,5(2020),e1380.
feedback. [12] SophiaSun,AadityaRamdas,andJingLei.2024. OnlineAdaptiveAnomaly
ThresholdingwithConfidenceSequences.InProceedingsofthe41stInternational
ConferenceonMachineLearning(ICML).
[13] JinlinWang,AadityaRamdas,andJingLei.2023.Robustandadaptiveconfidence
6 Conclusion sequencesforheavy-taileddata.J.Amer.Statist.Assoc.(2023). Toappear.
[14] YaoXue,LingfeiWu,Pin-YuChen,andBoLi.2023.ADT:Agent-basedDynamic
Adaptivethresholdingisacriticalcomponentofreliableanomaly ThresholdingforAnomalyDetection.InProceedingsoftheAdaptiveandLearning
detectioninnonstationarytimeseries,wherestaticbaselinesoften AgentsWorkshop(ALA2023).
failtocaptureevolvingdatabehavior.Inthiswork,weintroduced
andsystematicallyevaluatedtwonovelframeworks–Segmented Appendix
ConfidenceSequences(SCS)andMulti-ScaleAdaptiveConfidence A.PseudocodeforSegmentedConfidence
Segments(MACS)–thatintegrateonlineconfidencesequencethe-
Sequences(SCS)
orywithlocalizedstatisticaladaptation.Bytailoringthresholding
tothestructureandscaleofthedata,bothmethodsdeliversta- # Pseudocode for SCS adaptive thresholding
tisticallyprincipled,interpretable,andhigh-performinganomaly
# Input:
detection.
# time_series, window_size, confidence_level,
OurexperimentalresultsonbenchmarkWaferManufacturing
# n_segments, segmentation_method
datasetsdemonstratethatSCSandMACSsignificantlyoutperform
traditionalpercentile-basedandrollingquantilemethods,particu- # Step 1: Segment the time series
larlyintermsofrecallandF1-score.Bothframeworksofferflexible if segmentation_method == "APCA":
precision-recalltrade-offsthroughtunableconfidencelevelsand segments = APCA_segment(time_series,
12

| AIAT2025,December04–06,2025,Kyoto,Japan |               |     |                    |     | LiandGautam |
| --------------------------------------- | ------------- | --- | ------------------ | --- | ----------- |
| n_segments)                             |               |     | D.FullResultsTable |     |             |
| elif segmentation_method                | == "k-means": |     |                    |     |             |
WaferManufacturingdatasetdistribution
| segments | = kmeans_segment(time_series, |     |     |     |     |
| -------- | ----------------------------- | --- | --- | --- | --- |
n_segments)
| # Step 2: | Initialize confidence | sequence per |     |     |     |
| --------- | --------------------- | ------------ | --- | --- | --- |
segment
| for segment              | in segments:                      |                   |     |     |     |
| ------------------------ | --------------------------------- | ----------------- | --- | --- | --- |
| scores                   | = compute_anomaly_scores(segment) |                   |     |     |     |
| conf_bounds              | = init_confidence_sequence        |                   |     |     |     |
| (scores,                 | confidence_level)...              |                   |     |     |     |
| # Step                   | 3: Online update and              | anomaly detection |     |     |     |
| for new_point            | in stream:                        |                   |     |     |     |
| assigned_segment         | = assign_to_segment               |                   |     |     |     |
| (new_point,              | segments)                         |                   |     |     |     |
| update(assigned_segment, | new_point)                        |                   |     |     |     |
if is_anomalous
| (new_point, | assigned_segment.conf_bounds): |     |     |     |     |
| ----------- | ------------------------------ | --- | --- | --- | --- |
flag_anomaly(new_point)
B.PseudocodeforMulti-ScaleAdaptive WaferManufacturingdatasetresult
ConfidenceSegments(MACS)
| # Pseudocode          | for MACS         |                |          |                      |                   |
| --------------------- | ---------------- | -------------- | -------- | -------------------- | ----------------- |
|                       |                  |                |          | ΔAccuracy ΔPrecision | ΔRecall ΔF1-Score |
| # Input: time_series, | short_window,    | medium_window, | Method   |                      |                   |
| # long_window,        | confidence_level |                | SCSAPCA  |                      |                   |
|                       |                  |                | (𝛼=0.99) | -0.0422 -0.3282      | 3.9952 1.9074     |
# Step 1:
SCSKMEANS
| # Maintain              | sliding windows at multiple | scales       | (𝛼=0.99) |                 |               |
| ----------------------- | --------------------------- | ------------ | -------- | --------------- | ------------- |
|                         |                             |              |          | -0.0260 -0.3999 | 1.6643 0.9262 |
| scales = [short_window, | medium_window,              | long_window] |          |                 |               |
MACSMulti-Scale
| for scale            | in scales:                 |     |          |                 |               |
| -------------------- | -------------------------- | --- | -------- | --------------- | ------------- |
|                      |                            |     | (𝛼=0.99) | -0.0279 -0.1890 | 3.9952 2.1705 |
| window_scores[scale] | = initialize_window(scale) |     |          |                 |               |
| conf_bounds[scale]   | = init_confidence_sequence |     | SCSAPCA  |                 |               |
(𝛼=0.95)
(window_scores[scale], confidence_level) -0.0830 -0.4290 6.1595 2.1289
SCSKMEANS
# Step 2: Online anomaly detection (𝛼=0.95) -0.0545 -0.4656 3.3286 1.4148
| for new_point | in stream: |     |     |     |     |
| ------------- | ---------- | --- | --- | --- | --- |
MACSMulti-Scale
| for scale | in scales: |     | (𝛼=0.95) |                 |               |
| --------- | ---------- | --- | -------- | --------------- | ------------- |
|           |            |     |          | -0.0638 -0.3651 | 5.6595 2.2349 |
window_scores[scale].add(new_point)
update_confidence_sequence
(window_scores[scale],
confidence_level)
| # Composite         | decision rule                 |            | Calitdatasetdistribution |     |     |
| ------------------- | ----------------------------- | ---------- | ------------------------ | --- | --- |
| violation_count     | = sum(is_anomalous(new_point, |            |                          |     |     |
| conf_bounds[scale]) | for scale                     | in scales) |                          |     |     |
| if violation_count  | >= threshold:                 |            |                          |     |     |
flag_anomaly(new_point)
C.PipelineDiagram(SuggestedStructure)
(1) Input:TimeSeriesData
(2) Preprocessing:Removeseasonality/trendifneeded
(3) SegmentationModule:
• APCAork-meanssegmentation(SCS)
• Multi-scalerollingwindows(MACS)
(4) AdaptiveThresholding:
• Segment-specific/confidencesequenceupdate(SCS)
•
Multi-scaleonlinebounds(MACS)
(5) CompositeDetectionLayer:
• Dualfiltering:confidenceviolationandglobalpercentile
| • Anomalydecisionbasedonacompositerule |     |     | Calitdatasetresult |     |     |
| -------------------------------------- | --- | --- | ------------------ | --- | --- |
13

SegmentedConfidenceSequencesandMulti-ScaleAdaptiveConfidenceSegments
forAnomalyDetectioninNonstationaryTimeSeries AIAT2025,December04–06,2025,Kyoto,Japan
|     | ΔAccuracy ΔPrecision | ΔRecall ΔF1-Score |     |     |     |
| --- | -------------------- | ----------------- | --- | --- | --- |
Method
SCSAPCA
| (𝛼=0.99) | -0.0542 -0.4799 | 3.0000 0.4600 |     |     |     |
| -------- | --------------- | ------------- | --- | --- | --- |
SCSKMEANS
(𝛼=0.99)
|     | -0.0518 -0.3990 | 3.7135 0.6957 |     |     |     |
| --- | --------------- | ------------- | --- | --- | --- |
MACSMulti-Scale
| (𝛼=0.99) | -0.0542 -0.4799 | 3.0000 0.4600 |     |     |     |
| -------- | --------------- | ------------- | --- | --- | --- |
SCSAPCA
(𝛼=0.95)
|     | -0.0772 -0.5286 | 3.8573 0.4200 |     |     |     |
| --- | --------------- | ------------- | --- | --- | --- |
SCSKMEANS
| (𝛼=0.95) | -0.0933 -0.5981 | 3.7135 0.2436 |     |     |     |
| -------- | --------------- | ------------- | --- | --- | --- |
MACSMulti-Scale
(𝛼=0.95)
|     | -0.0772 -0.5286 | 3.8573 0.4200 |     |     |     |
| --- | --------------- | ------------- | --- | --- | --- |
MSLdatasetresult
GCPdatasetdistribution
|     |     |     | Method | ΔAccuracy ΔPrecision | ΔRecall ΔF1-Score |
| --- | --- | --- | ------ | -------------------- | ----------------- |
SCSAPCA
|     |     |     | (𝛼=0.99) | -0.0710 -0.0070 | 8.0741 4.2980 |
| --- | --- | --- | -------- | --------------- | ------------- |
SCSKMEANS
(𝛼=0.99)
|     |     |     |     | 0.0005 0.2847 | 0.3333 0.3283 |
| --- | --- | --- | --- | ------------- | ------------- |
MACSMulti-Scale
|     |     |     | (𝛼=0.99) | -0.0710 -0.0070 | 8.0741 4.2980 |
| --- | --- | --- | -------- | --------------- | ------------- |
SCSAPCA
(𝛼=0.95)
|     |     |     |     | -0.1109 -0.0685 | 11.5556 5.0101 |
| --- | --- | --- | --- | --------------- | -------------- |
SCSKMEANS
|     |     |     | (𝛼=0.95) | -0.0106 0.2276 | 1.9352 1.6061 |
| --- | --- | --- | -------- | -------------- | ------------- |
MACSMulti-Scale
(𝛼=0.95)
|     |     |     |     | -0.1084 -0.0633 | 11.3611 4.9848 |
| --- | --- | --- | --- | --------------- | -------------- |
GCPdatasetresult
SMDdatasetdistribution
| Method | ΔAccuracy ΔPrecision | ΔRecall ΔF1-Score |     |     |     |
| ------ | -------------------- | ----------------- | --- | --- | --- |
SCSAPCA
(𝛼=0.99)
|     | -0.0463 0.0585 | 6.5054 4.8418 |     |     |     |
| --- | -------------- | ------------- | --- | --- | --- |
SCSKMEANS
| (𝛼=0.99) | -0.0073 0.2319 | 1.7527 1.6045 |     |     |     |
| -------- | -------------- | ------------- | --- | --- | --- |
MACSMulti-Scale
(𝛼=0.99)
|     | -0.0463 0.0585 | 6.5054 4.8418 |     |     |     |
| --- | -------------- | ------------- | --- | --- | --- |
SCSAPCA
| (𝛼=0.95) | -0.0923 0.0654 | 13.0645 7.9435 |     |     |     |
| -------- | -------------- | -------------- | --- | --- | --- |
SCSKMEANS
(𝛼=0.95)
|     | -0.0193 0.2723 | 4.2473 3.5819 |     |     |     |
| --- | -------------- | ------------- | --- | --- | --- |
MACSMulti-Scale
| (𝛼=0.95)               | -0.0923 0.0654 | 13.0645 7.9435 |                  |     |     |
| ---------------------- | -------------- | -------------- | ---------------- | --- | --- |
| MSLdatasetdistribution |                |                | SMDdatasetresult |     |     |
14

AIAT2025,December04–06,2025,Kyoto,Japan LiandGautam
Method ΔAccuracy ΔPrecision ΔRecall ΔF1-Score CPUdatasetresult
SCSAPCA
(𝛼=0.99) -0.0594 0.4030 9.2152 3.5938 Method ΔAccuracy ΔPrecision ΔRecall ΔF1-Score
SCSKMEANS SCSAPCA
(𝛼=0.99) -0.0146 0.4848 2.8481 1.9297 (𝛼=0.99) -0.0538 -0.4667 2.5971 1.1456
MACSMulti-Scale SCSKMEANS
(𝛼=0.99) -0.0596 0.3576 8.8734 3.4453 (𝛼=0.99) -0.0110 -0.5353 -0.0777 -0.1758
SCSAPCA MACSMulti-Scale
(𝛼=0.95) -0.1199 0.3758 17.7342 4.4297 (𝛼=0.99) -0.0522 -0.4796 2.3932 1.0549
SCSKMEANS SCSAPCA
(𝛼=0.95) -0.0376 0.5091 6.5823 3.2500 (𝛼=0.95) -0.1084 -0.4867 5.4903 1.7335
MACSMulti-Scale SCSKMEANS
(𝛼=0.95) -0.1198 0.3455 17.2785 4.3125 (𝛼=0.95) -0.0279 -0.5495 0.7039 0.2802
MACSMulti-Scale
CPUdatasetdistribution (𝛼=0.95) -0.1064 -0.4913 5.3155 1.6923
15