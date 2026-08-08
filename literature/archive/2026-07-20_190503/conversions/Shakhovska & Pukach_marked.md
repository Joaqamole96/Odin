AI
Article
Severity-Aware Drift Adaptation for Cost-Efficient
Model Maintenance
KhrystynaShakhovska1 andPetroPukach2,*
1 ArtificialIntelligenceDepartment,LvivPolytechnicNationalUniversity,12BanderaStr.,79013Lviv,Ukraine;
khrystyna.r.shakhovska@lpnu.ua
2 DepartmentofComputationalMathematicsandProgramming,InstituteofAppliedMathematicsand
FundamentalSciences,LvivPolytechnicNationalUniversity,12BanderaStr.,79013Lviv,Ukraine
* Correspondence:petro.y.pukach@lpnu.ua
Abstract
Objectives: Thispaperintroducesanadaptivelearningframeworkforhandlingconcept
driftindatabydynamicallyadjustingmodelupdatesbasedontheseverityofdetected
drift. Methods: The proposed method combines multiple statistical measures to quan-
tify distributional changes between recent and historical data windows. The resulting
severity score drives a three-tier adaptation policy: minor drift is ignored, moderate
drifttriggersincrementalmodelupdates,andseveredriftinitiatesfullmodelretraining.
Results: Thisapproachbalancesstabilityandadaptability,reducingunnecessarycomputa-
tionwhilepreservingmodelaccuracy. Theframeworkisapplicabletobothsingle-model
andensemble-basedsystems,offeringaflexibleandefficientsolutionforreal-timedrift
management. Also,differenttransformationmethodswerereviewed,andquantiletrans-
formationwastested. Byapplyingaquantiletransformation,theKolmogorov–Smirnov
(KS)statisticdecreasedfrom0.0559to0.0072,demonstratingeffectivedriftadaptation.
Keywords: driftdetection;severityscore;incrementalmodelupdate;quantiletransforma-
tion;severity-awareadaptationmechanism;datatransformationstrategies
1. Introduction
AcademicEditors:Wai-keungFung
andJinzhuGao Inreal-worldsystems,datadistributionsrarelyremainstable. Datadrift,orcovariate
shift[1],occurswheninputstatisticschangeovertime,threateningthereliabilityofmodels
Received:13August2025
Revised:16October2025 trainedundertheassumptionofstabledistributions. Tomanagesuchevolvingdata,it
Accepted:22October2025 isimportanttorecognizethatdatacanbestoredinmultipleformatssuchasstructured,
Published:23October2025 semi-structured,andunstructured,dependingontheapplicationandtherequirementsfor
Citation: Shakhovska,K.;Pukach,P. processingandanalysis[2].
Severity-AwareDriftAdaptationfor Undetecteddriftdegradesaccuracyanddecisionquality,whichiscriticalindomains
Cost-EfficientModelMaintenance.AI
like finance, healthcare, and autonomous systems where outputs directly affect safety
2025,6,279. https://doi.org/
andoutcomes. Forinstance, acreditscoringmodeltrainedonpre-pandemicdatamay
10.3390/ai6110279
performinadequatelyduringeconomicshiftsunlesschangesindatapatternsareidentified
Copyright:©2025bytheauthors.
andaddressed[3].
LicenseeMDPI,Basel,Switzerland.
DetectingandquantifyingdriftisnowcentraltorobustMLlifecyclemanagement.
Thisarticleisanopenaccessarticle
distributedunderthetermsand Statisticalandmonitoringapproaches[4]enableproactiveretrainingoradaptation,helping
conditionsoftheCreativeCommons preservelong-termperformanceandreliability. Datadriftcanmanifestinseveraldistinct
Attribution(CCBY)license forms, each with different implications for machine learning model performance. The
(https://creativecommons.org/
primarytypesofdriftaregenerallycategorizedascovariatedrift,priorprobabilitydrift,
licenses/by/4.0/).
AI2025,6,279 https://doi.org/10.3390/ai6110279

AI2025,6,279 2of24
andconceptdrift. Thesedriftsmayoccurindependentlyorincombination,dependingon
changesinthedata-generatingprocess.
Covariatedrift,alsoknownasinputdrift,occurswhenthedistributionoftheinput
featuresP(X)changesovertime,whiletherelationshipbetweeninputsandoutputsP(Y|X)
remainsstable. Thistypeofdriftiscommonlyencounteredinreal-worldscenarioswhere
externalfactorsinfluencetheinputspace. Forexample,inane-commercerecommendation
system,seasonalvariationinuserbehaviormayresultinashiftinfeaturedistributions,
suchasproductviewsorclickpatterns,withoutalteringtheuserpreferencesthemselves[5].
Priorprobabilitydrift[6]referstoachangeinthemarginaldistributionofthetarget
variableP(Y)overtime. ThisoccurseveniftheconditionaldistributionP(X|Y)remains
unchanged. For instance, in medical diagnostics, the prevalence of certain conditions
may change due to epidemiological factors, leading to a shift in label distributions [7].
If unaccounted for, this drift can introduce bias in model predictions and compromise
decisionaccuracy.
Conceptdrift[8]ariseswhentheinput–outputrelationshipP(Y|X)changes,shifting
decisionboundariesandreducingpredictivepower. Forinstance,fraudstersmayadapt
behaviorstoevadedetection[9]. Conceptdriftisconsideredthemostdisruptiveform,asit
indicatesafundamentalchangeinthetaskthemodelisattemptingtolearn.
In this paper, an adaptive framework was proposed for handling concept drift in
streamingdataenvironments,focusingondynamicmodeladaptationbasedonquantified
driftseverity. Thecoreideaistointegrateadriftdetectionmechanismthatcontinuously
monitorschangesindatadistributionusingmultiplestatisticalmeasureslikeKolmogorov–
Smirnov,Wasserstein,andJensen-Shannondivergence. Thesemetricsareaggregatedinto
aunifiedseverityscorethatreflectstheextentofdistributionalshiftbetweenshort-term
andlong-termdatawindows. Unlikemethodsthatretrainaftereverydrift,ourframework
is severity-aware: minor drift is ignored, moderate drift triggers lightweight updates,
andonlyseveredriftrequiresfullretraining. Thisadaptivepolicyreducesunnecessary
computational overhead while maintaining high model performance over time. The
frameworkcanbeimplementedforbothsingle-modelandensemble-basedarchitectures
and is designed to be modular, interpretable, and compatible with real-time learning
systems. Quantiletransformationwasreviewedforupdatinglowdriftdetecteddata.
The ROSE [10] algorithm proposes a robust ensemble learning framework specifi-
cally designed for online, imbalanced, and concept-drifting data streams. The method
employs an ensemble of classifiers trained incrementally on random feature subsets to
promote diversity and adaptability. Concept drift is addressed through an integrated
onlinedetectionmechanismthattriggersthecreationofabackgroundensemble,enabling
rapidadaptationwhenchangesaredetected. Tomanageclassimbalance,ROSEmaintains
separate sliding windows for each class, ensuring sufficient representation of minority
classinstancesduringtraining. Additionally,thealgorithmincorporatesaself-adjusting
bagging strategy that dynamically increases the sampling rate for difficult or minority
classinstances. Throughthecombinationofthesetechniques,ROSEeffectivelyhandles
challengesrelatedtoevolvingdatadistributions,achievingabalancebetweenpredictive
performance,computationalefficiency,andmemoryusageinnon-stationaryenvironments.
TheDAMSIDmethod[11]presentsadynamicensemblelearningstrategytailored
forimbalanceddatastreamsaffectedbyconceptdrift. Themethodologyisstructuredin
threestages: ensemblelearning,conceptdriftdetection,andconceptdriftadaptation. In
theensemblelearningstage,classifiersaresequentiallytrainedonincomingdatachunks
andselectivelymaintainedbasedonperformanceevaluations,withaparticularfocuson
preserving high accuracy on minority classes. For drift detection, DAMSID employs a
dynamicweightedperformancemonitoringmechanism,separatelytrackingclassification

AI2025,6,279 3of24
performanceforminorityandmajorityclassesandadjustingdetectionsensitivityaccording
to the current class distribution. Upon detecting drift, the method initiates ensemble
adaptation by discarding underperforming classifiers and reconstructing the ensemble
usingmorerecentdata. Thismulti-stageprocessenablesDAMSIDtomaintainrobustness
andpredictiveaccuracyindynamic,highlyimbalancedstreamingenvironmentswhere
bothclassdistributionsanddecisionboundariesmayshiftovertime.
TheproposedSelf-AdaptiveEnsemble(SA-Ensemble)framework[12]isdesignedto
effectivelyhandleuserinterestdriftindatastreams,structuredaroundthreeinterconnected
components: topic-baseddriftdetection(T-IDDM),adaptiveweightedensemblelearning,
and dynamic voting strategy selection. First, the T-IDDM component employs topic
modeling(e.g.,viaLDA)todetectandquantifydriftinuserinterestbycomparingtopic
distributionsacrossconsecutivedatachunksusingstatisticaltwo-sampletesting,enabling
differentiation between real and virtual drift. Upon drift detection, the SA-Ensemble
moduleadaptstheensemble: poorlyperformingbaselearnersarepruned,andnewones
aretrainedonthelatestdata,whileresilientmodelsareretained;itincorporatesanadaptive
weightedvotingstrategyinwhichalightweightsub-modelpredictslabelsbasedontopic
contexttoestimatethecurrentaccuracyofensemblemembers,therebyweightingvotes
accordingly. Lastly,robustnessisenhancedthroughadynamicvotingstrategyselection
mechanism that evaluates predictions from majority voting, adaptive weighted voting,
andthesub-modelitself,selectingthemostaccuratestrategyonaper-instancebasis. This
integratedprocessmaintainshighperformanceandresilienceinthefaceofevolvinguser
interestdistributions.
TheproposedDynamicEnsembleLearning(DEL)framework[13]addressespredic-
tivechallengesinevolvingdatastreamsbyintegratingheterogeneousmodels,dynamic
adaptationmechanisms,andconceptdrifthandlingtechniques. Theframeworkbegins
withtheconstructionofanensemblecomprisingdiversebaselearners,eachofferingdis-
tinctperspectivesontheunderlyingdatadistribution. Adynamicweightingmechanism
continuously adjusts the influence of each model based on real-time performance and
sensitivitytoconceptdrift. Baselearnersareincrementallyupdatedusingonlinelearning
techniques, such as stochastic gradient descent and online boosting, enabling continu-
ousadaptationtonewdata. Conceptdriftisdetectedusingstatisticalchangedetection
methods,whichtriggerrecalibrationoftheensemblethroughreweightingandadaptive
retraining. TheDELframeworkisevaluatedthroughextensiveexperimentsonbenchmark
datasetswithsimulateddrift,usingstandardmetricssuchasaccuracy,precision,recall,and
F1-score. Furthermore,real-worldcasestudiesinfinance,healthcare,andenvironmental
monitoringdemonstratethepracticalapplicabilityofDELinsupportingrobust,real-time
decision-makingindynamicenvironments.
TheFastAdaptingEnsemble(FAE)algorithm[14]addressesbothabruptandgradual
concept drift, with specific capability to handle recurring concepts in streaming data.
Data are processed in fixed-size blocks, yet adaptation mechanisms are triggered even
beforeabatchisfullyreceivedtoensurerapidresponsetodrift. Explicitdriftdetection
is implemented via a drift detector (e.g., DDM), which monitors the data stream and
signalswhensignificantdistributionalchangesoccur. Tomanagerecurringconcepts,FAE
maintainsarepositoryofinactiveclassifiersrepresentingpreviouslyobservedconcepts;
theseclassifierscanbereactivatedimmediatelywhentheirassociatedconceptsreemerge.
Thealgorithm’sperformanceisrigorouslyevaluatedagainstestablishedlearningmethods
usingbenchmarkdatasetsundervariousdriftscenarios,demonstratingrobustadaptability,
highaccuracy,andcompetitiveruntimeperformance.
ThechallengeofconceptdriftinIoTdatastreamshasbeenwidelyaddressedthrough
ensemblelearningmethods. Forexample,Yangetal.[15]proposedanlightweightframe-

AI2025,6,279
4of24
workthatintegratesofflineclassifierswithadaptiveupdatingmechanismstocopewith
both abrupt and gradual drift in highly imbalanced industrial IoT data. Their method
leveragesmultiplelearnerstocapturediversedriftpatterns,whiledynamicallyadjusting
theensembletomaintainpredictiveaccuracyasnewdataarrives.
Whiletheaboveapproachesprovidevaluablestrategiesforhandlingdatadrift,many
relyonfrequentorfullretrainingofmodelsoncedriftisdetected. Thiscreatessignificant
computationalandoperationaloverhead,particularlyinreal-timeorresource-constrained
settings. What remains underexplored is a principled way of distinguishing between
differentlevelsofdriftseverityandtailoringthemodel’sresponseaccordingly. Proposed
frameworkaddressesthisgapbyintroducingaunifiedseverityscorethatenablesselective
adaptation: instead of retraining at every drift event, the system applies lightweight
transformationswhendriftisminorormoderate,andonlyescalatestofullretrainingunder
severedrift. Thisseverity-awarestrategypreservespredictiveaccuracywhilereducing
unnecessaryupdates,offeringamorecost-efficientandpracticalalternativetotraditional
drifthandlingtechniques.
2. MaterialsandMethods
Continuousdatashiftsaffectmodelaccuracy,butretrainingaftereverydriftisineffi-
cient. Proposedapproachquantifiesdriftseveritywithmultiplestatisticalmeasuresand
respondsproportionally,maintainingaccuracywhileavoidingunnecessarycosts.
Inputs:
| • StreamingdataD arrivingovertime. |     |     |     |
| ---------------------------------- | --- | --- | --- |
t
| • Short-termwindowsizeW         | ,long-termwindowsizeW. |     |     |
| ------------------------------- | ---------------------- | --- | --- |
|                                 | s                      | l   |     |
| • Thresholdsθ ,θ 2 forseverity. |                        |     |     |
1
•
CurrentmodelM.
Outputs:
| • Adaptiveaction: NoAction,PartialRetrain,FullRetrain. |     |     |     |
| ------------------------------------------------------ | --- | --- | --- |
Procedure:
1. UpdateWindows:
| Maintainashort-termwindowX         |     | ,Y ofthemostrecentW |            |
| ---------------------------------- | --- | ------------------- | ---------- |
|                                    |     | s s                 | s samples. |
| (cid:35) Maintainalong-termwindowX |     | ,Y ofhistoricalW    | samples.   |
|                                    |     | l l                 | l          |
(cid:35)
2. ComputeDriftSeverity:
Foreachdistributionalmetricm∈{KS,Wasserstein,Jensen–Shannon}:
(cid:35)
d = m(P,P), (1)
|             |                                 | m s l |        |
| ----------- | ------------------------------- | ----- | ------ |
| whereP andP | aretheempiricaldistributionsofX |       | andX . |
| s           | l                               |       | s l    |
Aggregateintoasingleseverityscore:
(cid:35)
S = α×d_ks+β×d_w+γ×d_jss, (2)
withα,β,γasweightingcoefficients.
3. SelectActionBasedonSeverity:
| Lowseverity: | S < θ |     |     |
| ------------ | ----- | --- | --- |
1
| (cid:35) ■ Action=Noupdate;continuemonitoring. |         |     |     |
| ---------------------------------------------- | ------- | --- | --- |
| Moderateseverity:                              | θ ≤ S < | θ 2 |     |
1
(cid:35) ■ Action=IncrementalUpdate: fine-tuneMonX ,Y usingsmalllearn-
s s
ingrateoronlineupdatestep.

AI2025,6,279 5of24
Highseverity: S ≥ θ
2
(cid:35) ■ Action=FullRetrain: discardMandtrainanewmodelonX ∪X
s l
Whilethedriftseverityscoreisdistributionalinnature,itsthresholdsweredesigned
with downstream model performance in mind. In preliminary sensitivity tests, scores
belowθ (<0.05)didnotyieldmeasurableaccuracyloss,whereasscoresbetweenθ andθ
1 1 2
(0.05–0.1)typicallycoincidedwithminorbutaccumulatingdegradation(<2–3%accuracy
droponbenchmarktasks). Scoresaboveθ (≥0.1)alignedwithsharpdeclinesinpredictive
2
stability,motivatingfullretraining.Thus,severitycategoriesserveasoperationalproxiesfor
acceptableversusunacceptableperformanceloss,providingaprincipledbasisforretraining
decisions. While current study emphasizes demonstrating the framework rather than
exhaustivebenchmarking,thesemappingsillustratehowthresholdscanbeoperationalized
inpractice.
4. LogandAdapt:
Record(S,action)forfuturethresholdtuning.
(cid:35) Optionallyupdateθ ,θ dynamicallyusinghistoricalSvalues.
1 2
(cid:35)
Toquantifydistributionaldrift,multiplestatisticalmetricscanbeemployeddepending
onthespecificrequirementsoftheanalysis.
Figure1summarizestheworkflow,highlightingthestagesofwindowmaintenance,
driftquantification,aggregation,andadaptiveaction.
Figure1.Methodologyworkflow.
Initially,evaluationofthedriftusingtheKolmogorov–Smirnov(KS)statistic,Kullback–
Leibler (KL) divergence, and the Anderson–Darling statistic was tested. However, this
combinationexhibitedcertaindrawbacks: theAnderson–Darlingstatisticprovedhighly
sensitivetosamplesize,oftenexaggeratingdriftinlargedatasets,whileKLdivergence
sufferedfromasymmetryandinstabilityinthepresenceofzero-probabilitybins.Toaddress
theseissues,theAnderson–DarlingstatisticwasreplacedwiththeWassersteindistance,

AI2025,6,279 6of24
whichismoreinterpretableintermsof“averagedisplacement”betweendistributionsand
lessaffectedbydifferencesinsamplesize. Furthermore,KLdivergencewassubstituted
withtheJensen–Shannon(JS)divergence,asymmetricandboundedmeasurethatavoids
zero-probabilityissues,providingamorerobustandinterpretabledriftscore. TableA1
presentsdetailedmetricscomparison.
Asingledriftscorein[0,1]wasobtainedbycombiningnormalizedKS,Wasserstein,
andJensen–Shannonmeasuresviaaweightedaverage. Eachmetricwasfirstscaledvia
min–max normalization based on historical drift observations to ensure comparability
despite differing units and ranges. The weights were selected to balance sensitivity to
bothshapeandlocationchangesinthedistribution, whileavoidingdominancebyany
singlemetric. Thisaggregatedscoreenablesaconsistentinterpretationofdriftmagnitude,
facilitating threshold-based categorization into “no drift,” “low drift,” and “significant
drift”levelsforoperationaldecision-making.
Afterquantifyingseverity,weevaluatedtransformationmethodstoalignnewdata
withthehistoricalbaseline,aimingtoreducediscrepanciesbeforeinferencewithoutfullre-
training. Severalapproacheswereconsidered: (i)feature-wiseimportancereweighting[16],
wheresampleweightsareadjustedbasedonestimateddensityratiosbetweenhistorical
andcurrentfeaturedistributions;(ii)featuremappingthroughdomainadaptationlayers,
whichlearnatransformationthatminimizesdistributionshiftviastatisticalmeasuressuch
asMaximumMeanDiscrepancy(MMD)[17]oradversarialtraining;(iii)residualcorrection
models [18], which adaptively adjust predictions based on recent residual errors; and
(iv)calibrationlayers,whichpost-processoutputprobabilitiestobettermatchobserved
frequenciesinthenewdata.
Afterreviewingtheseoptions,thequantiletransformationmethod[19]wasselected
forempiricaltesting. ThemathematicalformulationsareprovidedinAppendixA.3. This
approachnon-parametricallymapstheempiricalcumulativedistributionfunction(CDF)
ofthenewdatatothatofthereferencedistribution,ensuringthateachfeature’smarginal
distributionmatchesthebaselinewhilepreservingtherankorderofobservations. Unlike
reweighting,itadjuststhefeaturespacedirectly;unlikedomainadaptation,itrequiresno
extramodel. Themethodislightweight,deterministic,androbusttosample-sizevariation,
makingitsuitableforrapidalignmentwhenretrainingiscostly.
Thistransformationpreservestherelativeranksofthenewdatawhilereshapingits
distributiontoresemblethehistorical(reference)one.
Forimplementationdetails,thepseudocodeisincludedinAppendixA.2.
3. Results
3.1. DataExploration
Indataanalysisandmachinelearning, trackinghowvariablesevolveovertimeis
keytomaintainingrelevantinsights. Thejobmarketisonesuchdomain,wheresalaries,
demand,andskillsshiftwithtechnology,economics,andorganizationalneeds.
Inthisstudy,driftisexaminedwithinthecontextofadatasetondatasciencesalaries,
focusingonhowcompensationlevelsvaryacrosstimeandbetweendifferentexperience
levels.Theobserveddriftreflectsbothcovariatedrift—changesininputssuchasexperience
level,jobtitle,orcompanysize—andpriorprobabilitydrift,wherecategoryfrequencies
shift. Conceptdriftmayalsoariseifexternalfactors(e.g.,marketsaturationornewtools)
altertherelationshipbetweenexperienceandsalary.
Thiscasestudyinvestigatestemporaltrendsandstructuralchangesinthesalarydata,
withparticularattentionpaidtohowdistributionsevolveacrosstimeandroleseniority. By
identifyingandquantifyingsuchdrift,actionableinsightscanbederivedtosupportmore
informedandadaptivedecision-makinginarapidlychanginglabormarket.

AI2025,6,279 7of24
Fortheempiricalstudy,theDataScienceJobSalariesdatasetpublishedonKagglewas
used. Thedatasetcontains38,376recordscoveringsalariesofdata-relatedrolesbetween
2020and2024. Eachrecordincludesattributessuchasthereportedsalaryinlocalcurrency,
thestandardizedsalaryinUSD,theworkyear,employmenttype,jobtitle,companysize,
and locationinformation. Importantly, this dataset isnot a single-source collectionbut
ratheranaggregationofsixindependentsalarysurveys,whichimprovesitsdiversitywhile
alsointroducingpotentialinconsistenciesacrosssources.
Thetemporaldistributionofrecordsisskewedtowardrecentyears,with20,548entries
in2024,13,319in2023,andsubstantiallyfewerobservationsinearlieryears(e.g.,213in
2020). Thisimbalancereflectsthedataset’scrowdsourcednatureandtherapidgrowthof
thetechnologysectorinrecentyears.
Salary values exhibit substantial variation: the average reported salary is approxi-
mately$148,762USD,withastandarddeviationofabout$75,034USD.Themaximumsalary
exceeds$800,000USD,whiletheminimumentriesincludezeros,whichlikelycorrespond
toerroneousorincompletesubmissions. Thesecharacteristicshighlighttheheterogeneity
ofthedatasetandtheimportanceofapplyingnormalizationandrobustnesschecksinthe
driftanalysis.
Thisdatasetwasselectedforthreereasons:
• Accessibilityandsize—itprovidesarelativelylargesamplethatispubliclyavailable
andreproducible.
• Temporalcoverage—thedatasetspansmultipleconsecutiveyears,enablingyear-over-
yeardriftanalysis.
• Heterogeneity—itcapturesawiderangeofsalariesandjobcontexts,whichallows
testingdriftdetectionacrossdiversedistributions.
Whilethisdatasetisnotfullyrepresentativeofallenvironmentswheredriftadaptation
iscritical(e.g.,high-frequencysensordata,streamingapplications),itoffersapracticaland
transparentbenchmarkforevaluatingourseverity-baseddriftscoringapproach.
InFigure2,thetrendofdatascientistsalariesovertimeisdepicted,showingaclear
temporalshift. Theobservedpatternindicatesdrift,suggestingthatthesalarydistribution
changesnotablyacrossperiods.
Figure2.Salarytrendoverthetimewithshaded95%CI.
InFigure3,boxplotsillustratethesalarydistributionbyyearandrolelevel,revealing
that the magnitude and direction of drift vary across levels. This indicates that salary
dynamicsarenotuniformbutdependoncareerstage.

AI2025,6,279 8of24
Figure3.Boxplotofsalarydistributionbyyearandexperiencelevel.
To statistically confirm the observed drift, the Kolmogorov–Smirnov (KS) test [20]
wasappliedtosalarydistributionsfrom2023and2024. ThetestyieldedaKSstatisticof
0.0559(p<0.0001),indicatingasmallbutstatisticallysignificantdifferenceindistribution
shape,confirmingmeasurabledriftbetweenthetwoyears.
TheKolmogorov–Smirnov(KS)testwasalsoappliedseparatelyforeachrolelevelto
assesswhethersalarydriftdiffersacrosscareerstages. Table1summarizestheresultsfor
allconsecutiveyearcomparisons.
Table1.KStestp-valuesforsalarydistributiondriftbyrolelevel.
YearsCompared EN EX MI SE
2020vs. 2021 0.0011 0.0082 0.0764 0.0025
2021vs. 2022 0.0008 0.0145 0.0000 0.0076
2022vs. 2023 0.0003 0.2729 0.0000 0.0000
2023vs. 2024 0.0000 0.0084 0.0000 0.0000
Acrossmostyear-to-yearcomparisons,p-values<0.05indicatestatisticallysignificant
distributionalchanges,confirmingsalarydrift. However,theextentofdriftisnotuniform:
• Entry(EN)rolesshowconsistent,significantdriftinallcomparisons.
• Executive (EX) roles exhibit significant drift in most years, but not between 2022
and2023.
• Mid-level(MI)salariesarestableonlybetween2020and2021, withstrongdriftin
laterperiods.
• Senior(SE)rolesshowsignificantdriftinallbutthe2020–2021comparison.
Thisconfirmsthatsalarydynamicsevolvedifferentlybyrolelevel,withentryand
mid-levelpositionsexperiencingthemostpersistentdistributionalshifts.
Another way to detect drift is using Empirical CDFs [21]. Figure 4 displays the
EmpiricalCumulativeDistributionFunctions(ECDFs)ofsalariescomparing2023and2024
fortheoveralldataandFigure5brokendownbyexperiencelevels(EN,EX,MI,SE).The
ECDFplotsvisualizethecumulativeprobabilitythatasalaryislessthanorequaltoagiven
value,highlightingdifferencesinthesalarydistributionsovertime.

AI2025,6,279 9of24
Figure4.EmpiricalCDFofSalaries.
(a) (b)
(c) (d)
Figure5. EmpiricalCDFbyexperiencelevel: (a)EntryLevel;(b)MiddleLevel;(c)SeniorLevel;
(d)ExpertLevel.
TheoverallECDF(topplot)showsasmallbutnoticeableshiftbetween2023(blue)
and2024(red)salaries,withaKSstatisticof0.0559,indicatingsomedrift.
Byexperiencelevel,theECDFsrevealvaryingdegreesofdistributionalchange:
• Entry(EN)levelshowsasubstantialshiftwithaKSstatisticof0.1782,indicatinga
significantincreaseinsalarydistributionbetweenyears.
• Executive(EX)levelshowsmoderatedriftwithaKSstatisticof0.0976,confirming
statisticallysignificantbutsmallerchanges.
• Mid-level (MI) also exhibits a pronounced shift (KS = 0.1488), reflecting notable
salaryadjustments.
• Senior(SE)levelshowsthesmallestshift(KS=0.0531),indicatingrelativelystable
salarydistributionscomparedtootherlevels.

AI2025,6,279
10of24
Across all levels, p-values of 0.0000 or near zero confirm that these distributional
differencesbetween2023and2024arestatisticallysignificant. ThevaryingKSstatistics
visuallyandquantitativelydemonstratethatsalarydriftdiffersbyroleseniority,withthe
largestchangesobservedinEntryandMid-levelpositions.
Inadditiontotheprimaryanalysis,twoadditionalstatisticalmetricswereusedto
assessthedistributionaldifferencesinsalarydatabetween2023and2024acrossthefour
groups (EN, EX, MI, SE): the Kullback–Leibler [22] (KL) divergence and the Anderson-
Darling(AD)teststatistic.
The KL divergence, which measures the relative entropy or difference between
two probability distributions, yielded the following values: EN = 0.2311, EX = 0.0645,
MI=0.1428,andSE=0.0393. TheoverallKLdivergenceacrossallgroupswasfoundtobe
0.0412,indicatingarelativelysmalldivergencebetweenthesalarydistributionsofthetwo
yearsonaggregate.
TheAnderson-Darlingtest[23],anon-parametrictestusedtoevaluatewhethertwo
samplescomefromthesamedistribution,producedstatisticallysignificantresultsforall
groups. TheADstatisticswere: EN=88.5902,EX=9.1434,MI=203.8717,andSE=58.5065,
allwithp-valuesequalto0.0010.
TheoverallAnderson-Darlingstatisticwas73.6193witha
p-valueof0.0010,stronglyrejectingthenullhypothesisofidenticaldistributionsbetween
the2023and2024salarydata.
TheseresultscollectivelysuggestthatwhiletheoveralldivergencemeasuredbyKL
divergence is relatively low, the Anderson-Darling test detects statistically significant
differencesinthedistributionsacrossallgroups,reflectingchangesintheunderlyingsalary
distributionsbetweenthetwoyears.
Toinvestigatetemporalchangesinthesalarydistributions,thedataacrossmultiple
yearsusingthreestatisticalmetricswascompared: theKolmogorov–Smirnov(KS)statistic,
theKullback–Leibler(KL)divergence,andtheAnderson-Darling(AD)teststatistic. The
samplesizesandresultsforeachyearcomparisonagainst2024aresummarizedinTable2:
Table2.Datadriftcomparison.
YearsCompared
| Comparingdistributionsfor2023vs. |                  | 2024:  |
| -------------------------------- | ---------------- | ------ |
| Samples:                         | 13,214vs.        | 20,318 |
| KSstatistic:                     | 0.0559,p-value:  | 0.0000 |
| KLDivergence(2023vs.             | 2024):           | 0.0412 |
| Anderson–Darlingstatistic:       | 73.6193,p-value: | 0.0010 |
| Comparingdistributionsfor2022vs. |                  | 2024:  |
| Samples:                         | 2993vs. 20,318   |        |
| KSstatistic:                     | 0.1093,p-value:  | 0.0000 |
| KLDivergence(2022vs.             | 2024):           | 0.1421 |
153.0022,p-value:
| Anderson–Darlingstatistic:       |                  | 0.0010 |
| -------------------------------- | ---------------- | ------ |
| Comparingdistributionsfor2021vs. |                  | 2024:  |
| Samples:                         | 1219vs. 20,318   |        |
| KSstatistic:                     | 0.1737,p-value:  | 0.0000 |
| KLDivergence(2021vs.             | 2024):           | 0.4136 |
| Anderson–Darlingstatistic:       | 92.9645,p-value: | 0.0010 |
Basedontheseresults,thedistributionalshiftscanbecategorizedasfollowstosimu-
latedifferentlevelsofdrift:
1. No Drift—represented by the 2023 vs. 2024 comparison, where the KS statis-
tic and KL divergence are relatively low, indicating minimal change between the
salarydistributions.

AI2025,6,279 11of24
2. LowDrift—representedbythe2022vs.2024comparison,showingmoderateincreases
inKSstatisticandKLdivergence,suggestingnoticeablebutnotdrasticchanges.
3. Strong Drift—represented by the 2021 vs. 2024 comparison, with the highest KS
statisticandKLdivergencevalues,indicatingasubstantialchangeinthedistribution.
Thesecategoriesallowmodelingofdriftseverityintemporalsalarydata,usefulfor
evaluatingrobustnessofstatisticalmethodsormachinelearningmodelstochangingdata
distributionsovertime.
3.2. WeightedDriftAnalysis
To obtain a single composite measure of distributional change, a Combined Drift
ScorebyweightingtheKSstatistic(50%),KLdivergence(30%),andtheAnderson–Darling
statisticnormalizedbythelogarithmofthecombinedsamplesize(20%)wascomputed.
TheKSstatisticissensitivetothelargestdifferencesbetweencumulativedistribution
functions(CDFs),theKLdivergencequantifiestheoverall(asymmetrical)shiftbetween
distributions,andtheAnderson-Darlingstatisticisparticularlysensitivetodifferencesin
thetailsofthedistributions.
DriftseveritywasclassifiedasNodrift(<0.05),Lowdrift(<0.15),orSignificantdrift
(≥0.15). ThecombinedscoreresultsareshowninTable3.
Table3.Combinedscoreresultscomparison.
Comparison KS KL AD CombinedScore DriftLevel
2023vs.2024 0.0559 0.0412 73.6193 1.4533 Significant
2022vs.2023 0.0793 0.0808 58.5182 1.2713 Significant
2021vs.2022 0.0821 0.1023 8.9058 0.2851 Significant
Allyear-to-yearcomparisonsexceededthethresholdforSignificantdrift,indicating
substantialchangesintheunderlyingsalarydistributionsacrossconsecutiveyears. The
largestdriftwasobservedbetween2023and2024(score=1.4533),drivenprimarilybya
highnormalizedAnderson–Darlingstatistic,whilethesmallest—butstillsignificant—drift
occurredbetween2021and2022(score=0.2851),wheretheAnderson–Darlingcontribution
wascomparativelylow.Whilethisconfirmsdistributionalchangesovertime,theuniformly
significantresultslimittheabilitytodiscriminatebetweendifferentdriftlevelsincurrent
experimentalsetup,whichrequiresdistinguishingamongnodrift,lowdrift,andstrong
driftconditions.
To better capture and differentiate these levels, adjustment of the set of metrics
wasproposed:
• KeepKStestforasimplequickcheck.
• Replace Anderson–Darling with Wasserstein distance [24]—interpretable and less
sample-sizedependent.
• Use Jensen-Shannon divergence [25] instead of KL to avoid asymmetry and zero-
probabilityissues.
ThesummaryofchangesareshowninTable4.
Usingtherevisedmetrics—KSstatistic,Wassersteindistance,andJensen-Shannon
divergence—thecombineddriftscoreswasrecalculatedfortheyearlysalarydistribution
comparisons. TheresultsaresummarizedinTable5:

AI2025,6,279
12of24
Table4.Combinedscoremetricdecision.
|     |     | MetrictoKeep | MetrictoReplacewith |     |                        | Why? |
| --- | --- | ------------ | ------------------- | --- | ---------------------- | ---- |
|     |     | KS           |                     | -   | Simpleandinterpretable |      |
Anderson–Darling Wassersteindistance Morestablewithsamplesize
|     |     | KLdivergence | Jensen-Shannondivergence |     | Symmetric,morestable |     |
| --- | --- | ------------ | ------------------------ | --- | -------------------- | --- |
Table5.Updatedcombinedscoreresultscomparison.
Comparison KSStatistic WassersteinDistance Jensen-ShannonDivergence CombinedDriftScore DriftLevel
| 2023vs.2024 | 0.0559 | 7943.26   | 0.0148 |     | 2383.01 | Significant |
| ----------- | ------ | --------- | ------ | --- | ------- | ----------- |
| 2022vs.2024 | 0.1093 | 21,564.75 | 0.0518 |     | 6469.49 | Significant |
| 2021vs.2024 | 0.1737 | 24,353.06 | 0.1502 |     | 7306.03 | Significant |
While the updated metrics produce a wider and more distributed range of drift
scores—reflectinggradationsindistributionalchanges—theabsolutevaluesofthecom-
binedscoresvarygreatlyinmagnitude. Thiswidescalecomplicatesdirectinterpretation
andcomparison.
Therefore,tofacilitateconsistentclassificationandimproveinterpretability,thecom-
bineddriftscorerequiresnormalizationtoaboundedrange,suchas[0,1]. Normalizing
thescoreswillenablestraightforwardthresholdingandclearerdistinctionbetweennodrift,
lowdrift,andstrongdriftcategories,therebyimprovingpracticalusabilityinmonitoring
andexperimentalevaluation.
|     | 3.3. | NormalizationofDriftMetricsandResults |     |     |     |     |
| --- | ---- | ------------------------------------- | --- | --- | --- | --- |
Toensurecomparabilityandinterpretabilityofdriftscoresacrossdifferentyear-to-year
salarydistributioncomparisons,normalizationwasappliedtotheindividualmetricsprior
tocombiningthem.
•
Wassersteindistancenormalization: TherawWassersteindistancewasdividedbythe
rangeofcombinedsalaryvalues(max–min)frombothsamples. Thisscalingbounds
theWassersteinmetricapproximatelybetween0and1,makingitinvarianttoabsolute
salaryscaledifferences.
• Jensen-Shannondivergence: ComputedonhistogramswithFreedman–Diaconisbin-
ning and smoothed with a small epsilon to avoid zeros, then squared to maintain
valuesstrictlybetween0and1.
• KSstatistic: Remainsnaturallybetween0and1andisretainedwithoutmodification.
• ThecombineddriftscoreiscalculatedasaweightedsumofthenormalizedKSstatistic
(weight0.4),scaledWassersteindistance(weight0.3),andJensen-Shannondivergence
(weight0.3). Thisweightedaggregationensurestheoverallscorerangesfrom0to1.
Thedriftscoreisinterpretedwiththresholds:
•
Nodrift: score<0.05.
|     | •   | Lowdrift: 0.05≤score<0.1.    |     |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --- | --- |
|     | •   | Significantdrift: score≥0.1. |     |     |     |     |
ThecombinedscoreresultswithnormalizedmetricsareshowninTable6.
Table6.Normalizedmetricscombinedscoreresultscomparison.
Comparison KSStatistic Wasserstein(Scaled) Jensen-Shannon CombinedScore DriftLevel
| 2023vs.2024 | 0.0559 | 0.0183 | 0.0148 |     | 0.0323 | Nodrift          |
| ----------- | ------ | ------ | ------ | --- | ------ | ---------------- |
| 2022vs.2024 | 0.1093 | 0.0496 | 0.0518 |     | 0.0742 | Lowdrift         |
| 2021vs.2024 | 0.1737 | 0.0560 | 0.1502 |     | 0.1313 | Significantdrift |

AI2025,6,279 13of24
Thenormalizedcombinedscoresrevealaclearergradationofdriftintensity,withthe
2023vs. 2024comparisonfallingintothenodriftcategory,2022vs. 2024showinglowdrift,
and2021vs. 2024exhibitingsignificantdrift.
As a complementary case study, experiments were conducted on the Housing in
London dataset, originally published by the London Datastore. The dataset spans the
periodfromJanuary1995toJanuary2020, offeringalong-termviewofhousingtrends
acrossLondonboroughs.
Thedatasetcontains13,549recordswiththefollowingmainattributes:
• average_price—averagepropertypricesinGBP;
• houses_sold—numberofresidentialpropertytransactions;
• no_of_crimes—recordedcrimecounts;
• borough_flag—binaryindicatordistinguishingLondonboroughsfromotheradminis-
trativeareas.
Descriptivestatisticsrevealconsiderablevariationacrossthesemeasures. Themean
averagepropertypriceisapproximately£263,520withastandarddeviationof£187,618,
while the maximum recorded value reaches over £1.46 million. The number of houses
sold varies widely (mean ≈3894, max >132,000), reflecting the dynamic nature of the
housing market. Crime counts average around 2158 incidents per period with notable
dispersion(standarddeviation≈902). Theborough_flagdistribution(mean≈0.73)reflects
thedataset’smixofborough-levelandnon-borough-levelentries.
Thisdatasetwasselectedbecause:
• Longitudinal coverage—it spans 25 years, allowing drift detection to be tested on
long-termsocio-economicprocesses.
• Multivariatestructure—itincludeseconomic(prices,transactions)andsocial(crime
rates) indicators, enabling analysis of how different feature types drift jointly
overtime.
• Publicprovenance—sourcedfromanofficialopen-dataportal,ensuringtransparency
andreproducibility.
This dataset complements the salary dataset by providing a structurally different
domain: structuredtemporal-economicdatawithgeographicgranularity,incontrastto
individual-levelsurveydata. Together,thetwocasesillustratetheflexibilityofproposed
driftseverityscoringapproachacrossdiversecontexts.
Onechallengewithhousingdataisthatadjacentyearscanshownoisydifferencesdue
tochangesinthemixofpropertiessold(e.g.,regionaldistributionorpropertytype). To
addressthis,weanchorcomparisonsinafixedyearandthenmeasuredriftatincreasing
horizons. This approach highlights the cumulative effect of distributional change over
time. AsshowninTable7,thedriftseverityincreasesconsistentlywiththetimehorizon:
one-yearcomparisonsremainintheNodriftcategory,mediumhorizonsshowLowdrift,
andlongerhorizonsreachSignificantdrift. Thisillustratesthatproposedseverityscore
scalesmeaningfullywithtemporaldistance,eveninnoisyreal-worlddatasets.
Table7.Driftseverityinhousingdatasetwith2010asanchoryear.Thresholds:Nodrift(<0.05),Low
drift(0.05–0.15),Significantdrift(≥0.15).
Comparison KSStatistic Wasserstein(Scaled) Jensen-Shannon CombinedScore DriftLevel
2010vs.2011 0.0704 0.0105 0.0531 0.0472 Nodrift
2010vs.2012 0.1463 0.0237 0.0790 0.0893 Lowdrift
2010vs.2015 0.4611 0.1083 0.2012 0.2773 Significantdrift

AI2025,6,279 14of24
Whencomparinghousingpricesbetween2010and2011,pooledanalysissuggested
Nodrift(combinedscore=0.0472). However,whenthesamecomparisonwasperformed
separatelyforeacharea,almosteveryregionshowedSignificantdrift(44outof45),with
onlyoneareashowingLowdrift. Table8highlightsthetop-3strongestandweakestcases.
Table8.By-areadriftseverityfor2010vs.2011(average_price).
Area CombinedScore DriftLevel
YorksandtheHumber 0.735 Significantdrift
RichmonduponThames 0.731 Significantdrift
NorthEast 0.715 Significantdrift
Havering 0.147 Significantdrift
Bexley 0.146 Significantdrift
Enfield 0.097 Lowdrift
Thisdiscrepancyshowsthataggregatedanalysiscanobscureimportantlocalchanges:
whensubgroupsshiftindifferentways,theoveralldistributionmayappearstableeven
thoughstrongdriftoccurswithinsubpopulations.
Driftassessmentismostinformativewhenperformedatthelevelofdetailthatmatches
themodel’sscope. Forglobalmodels,aggregated(pooled)driftscoresprovideauseful
overview,whileforregion-orsubgroup-specificmodels,stratifieddetectionoffersmore
relevant insights. The proposed framework accommodates both approaches, allowing
practitioners to compute severity scores for any subgroup of interest (e.g., by region,
demographic,ordevicetype)andalignmonitoringwiththeintendedapplication.
As a direction for future work, it would be valuable to design summary statistics
thatintegratebothglobalandsubgroupperspectives. Suchmeasurescouldcaptureover-
alldistributionalshiftswhilealsoreflectingvariationacrosssubpopulations,enablinga
morebalancedassessmentinsettingswherebothglobalaccuracyandsubgroupstability
arecritical.
Totestproposedapproachinahigh-dimensional,non-economicdomain,weused
the Gas Sensor Array Drift Dataset at Different Concentrations, published by the UCI
MachineLearningRepository. ThisdatasetwasoriginallycollectedbyVergaraetal. as
partofresearchonsensordriftphenomena,makingithighlyrelevantforevaluatingdrift
detectionmethods.
Thedatasetconsistsof13,910measurementsofchemicalgasconcentrationscollected
over10batches. Eachrecordincludes:
• batch—indicatingthemeasurementbatch(1–10);
• class_id—thegastypeidentifier(6classesofvolatileorganiccompounds);
• concentration—concentrationlevel(1–1000ppm);
• f1–f128—128 continuous features representing the raw responses of an array of
16chemicalsensorsacrossmultiplefeatureextractionmethods.
The data distribution is heterogeneous. Concentration values range from 1 ppm
to1000ppm, whilethesensorfeaturesspanwidenumericscales. Forinstance, feature
values(e.g.,f1,f121)canrangefromhighlynegativevalues(e.g.,−16,000)tolargepositive
magnitudes (up to >670,000). The dataset thus reflects both the physical variability of
sensoroutputsandthechallengesintroducedbysensordrift. Sensorfeaturesexhibitlarge
standarddeviations(e.g.,f1std≈69,845),skewness,andextremeoutliers. Measurements
covermultiplegasesacrossbatches,providingnaturalpartitionsfordriftanalysis.
Thisdatasetwaschosenbecause:
• Direct relevance—it was explicitly designed to study sensor drift, making it a
naturalbenchmark.

AI2025,6,279
15of24
• Highdimensionality—with128features,itenablestestingscalabilityandrobustness
ofdriftscoring.
•
Temporalbatching—thedivisionintobatchesallowsforevaluatingdriftbothsequen-
tiallyandcumulatively.
Thisdatasetcomplementsthesalaryandhousingdatasetsbyrepresentingareal-world
sensorscenariowheredriftisaknownandcriticalchallenge. Itallowsustodemonstrate
that our severity-based scoring approach is not limited to socio-economic data but can
generalizecomplexindustrialandIoTsettings.
Analysiswasconductedinthreesteps:
1. Feature-leveldriftdetection: Eachsensorfeaturewascomparedacrosstimewindows
using the same statistical tests (KS, Wasserstein, Jensen–Shannon). Features were
assigned a severity level (No drift, Low drift, Significant drift). This provides a
fine-grainedviewofwhichsensorsshowthestrongestdistributionalchanges.
2. Window-levelaggregation: Foreachtimewindow,weaggregatedacrossfeaturesand
computedthepercentageoffeaturesineachdriftcategory. Thisallowsustoobserve
whetherdriftissporadicorsystemicacrossthesensorarray.
3. Stackedtrendvisualization: Finally,thedriftdynamicsovertimeusingastackedbar
plotwaspresented,showingtheevolutionofNo/Low/Significantdriftcategories
acrosswindows. Thishighlightsnotonlywhichfeaturesdrift,butalsowhendrift
isconcentrated.
Keyobservation:
Thegasdatasetshowedpervasivedrift—with93%offeaturesflaggedasSignificant
drift. Onlyasmallfraction(7%)wascategorizedasLowdrift,andnoneasNodrift. Thisis
consistentwiththestackedplot,wherealmosteverywindowisdominatedbysignificant
drift. At the same time, the framework identifies both the most unstable features (e.g.,
f121,f105,f113)andtherelativelymorestableones(f32,f24,f10),demonstratinghowit
canpinpointthewhereandwhenofchanges,evenincomplexsensordata. Resultsare
displayedonTable9.
Table9.Top5mostdriftedandstablefeatures.
| Feature | CombinedScore | DriftLevel       |
| ------- | ------------- | ---------------- |
| f121    | 0.314         | Significantdrift |
| f105    | 0.313         | Significantdrift |
| f113    | 0.307         | Significantdrift |
| f57     | 0.298         | Significantdrift |
| f49     | 0.298         | Significantdrift |
| f32     | 0.056         | Lowdrift         |
| f24     | 0.059         | Lowdrift         |
| f10     | 0.067         | Lowdrift         |
| f56     | 0.081         | Lowdrift         |
| f96     | 0.081         | Lowdrift         |
Table10reportsdriftseverityacrossdifferenttargetwindowsinthegassensordataset.
Thedatasetisorganizedintobatches, whereeachbatchcorrespondstoacontrolledex-
perimental run collected under fixed conditions (e.g., a particular time period and gas
concentration setting). A target window in this analysis is defined as a single batch
(window size = 1 batch). Thus, Window (1,) refers to the first batch after the baseline,
Window(2,)tothesecondbatch,andsoon.

AI2025,6,279 16of24
Table10.Mostandleastdrift-affectedfeaturesinthegasdataset.
TargetWindow LowDrift NoDrift SignificantDrift
(1,) 0.0% 38.3% 61.7%
(2,) 1.6% 47.7% 50.8%
(3,) 0.0% 0.8% 99.2%
(4,) 0.0% 4.7% 95.3%
(5,) 0.0% 2.3% 97.7%
Foreachtargetwindow,driftseveritywasmeasuredbycomparingthefeaturedistri-
butionsinthatbatchagainstthebaselinedistribution. Theproportionsoffeaturesfalling
intoNodrift,Lowdrift,andSignificantdriftcategoriesarereported.
Theresultshighlightastrongtemporalprogression:
• Intheearliestwindows((1,)and(2,)),38–48%offeaturesremainstable(nodrift),while
roughlyhalfalreadyexhibitsignificantdrift.
• StartingfromWindow(3,),significantdriftdominates,exceeding95%offeaturesin
laterwindows((3,)–(5,)).
• Low drift is rarely observed, suggesting that feature distributions tend to change
abruptlyratherthangradually.
Thisconfirmsthatgassensorresponsesdegradeorshiftsystematicallyacrossbatches,
withlaterexperimentalrunsshowingpronounceddivergencefromthebaseline.
ThestackedbarchartpresentedonFigure6showstheproportionoffeaturescatego-
rizedasnodrift,lowdrift,andsignificantdriftacrosssequentialbatches(B1–B10). While
earlybatchescontainamixofdriftseverities,significantdriftquicklybecomesdominant,
exceeding90%offeaturesinmostlaterbatches. AbriefstabilizationisobservedinB2,but
thiseffectdoesnotpersist. Overall, thecharthighlightsthepervasiveandaccelerating
natureofdriftingassensordata,withonlytransientwindowsofstability.
Figure6.Driftanalysisacrossbatchesinthegasdataset.
3.4. LimitationsandFutureDirections
Theprimarycontributionofthisworkisaframeworkthatenablesrapiddetection
of data drift and its severity, providing a cost-efficient alternative to continuous model
retraining. Theexperimentalevaluationacrossdiversedatasets(salary,housingprices,and
gassensors)highlightsboththestrengthsandthecurrentlimitationsoftheapproach.
First,datarepresentativenessremainsachallenge: somedatasets(e.g.,salarysurveys)
maynotfullyreflectreal-worlddistributions,whileothers(e.g.,housingorsensordata)
exhibitimbalancedorlimitedsamplesthataffectmetricstability.Second,thereisatrade-off
in granularity: pooled analysis may suggest stability, whereas subgroup-level analysis

AI2025,6,279 17of24
(e.g.,byregioninhousingdata)revealssubstantialdrift. Third,themethodissensitive
to temporal windowing, where small windows can produce noise and large windows
canobscureshort-termshifts. Fourth,small-sampleeffectsoccasionallyyieldunreliable
statisticaloutputs(e.g.,NaNvalues),leadingtoanoverestimationofdriftseverity. Finally,
the current implementation is restricted to continuous variables, and categorical drift
detectionhasnotyetbeenincorporated.
Theselimitationssuggestseveralpromisingdirectionsforfutureresearch. Expanding
dataset diversity will help validate robustness across domains. Adaptive windowing
strategies could automatically adjust temporal granularity, reducing reliance on fixed
parameters. Hierarchicalanalysisatbothglobalandsubgrouplevelswouldprovideamore
nuancedunderstandingofdrift. EnhancingrobustnesstosparsedatathroughBayesian
inference,bootstrapping,orresamplingwouldmitigateinstabilityinlow-sampleregimes.
Extendingtheframeworktocategoricaldistributionsrepresentsanimportantnextstepto
improvecoverage. Finally,explicitlylinkingdriftseverityscorestomodelperformance
degradationwouldstrengthentheirutilityinguidingretrainingpolicies.
3.5. ParameterSelectionandJustification
The construction of the Combined Drift Score required two key design decisions:
theweightingofindividualstatisticalmetricsandthethresholdsusedtocategorizedrift
severity. Bothwereguidedbyempiricalexperimentationanddomain.
Weightingofmetrics. TheKolmogorov–Smirnov(KS)statisticwasinitiallyassigned
thelargestweight(50%)becauseitisawidelyestablishedtestfordistributionaldifferences
anddirectlycapturesthemaximumdeviationbetweencumulativedistributions. Kullback–
Leibler(KL)divergencereceivedamoderateweight(30%)toemphasizesensitivitytoshifts
indistributionalmasswhilemitigatinginstabilityinsparseregionsofthedistribution. The
Anderson–Darling(AD)statistic,normalizedbythelogarithmofthecombinedsample
size to reduce sensitivity to sample size, was weighted lower (20%) to complement KS
andKLbyfocusingontailbehavior. Thesecoefficientswerecalibratedthroughrepeated
experimentstoreflectwhichmetricsmostconsistentlyalignedwithobservedandexpert-
validateddistributionalchanges. Theweightingschemethereforebalancedrobustness,
interpretability,andcoverageofdifferentdistributionalaspects.
Followingfurtherevaluationandrefinement,thefinalCombinedDriftScoreiscal-
culatedasaweightedsumofthenormalizedKSstatistic(40%), thescaledWasserstein
distance(30%),andtheJensen–Shannon(JS)divergence(30%).TheKSstatisticsretainedthe
largestshare(40%)duetoitsestablishedroleasanon-parametrictestfordetectingdistribu-
tionaldifferences,particularlyitssensitivitytomaximumdeviationsbetweendistributions.
Wassersteindistancewasassignedamoderateweight(30%)foritsinterpretabilityasthe
“averageshift”betweendistributions,makingitespeciallysuitableforquantifyingpractical,
real-worlddifferences. JSdivergencewasalsogivenamoderateweight(30%)becauseofits
stability,boundedrange(0–1),andsymmetrictreatmentofdistributions,complementing
thedirectionalsensitivityofKLdivergenceusedearlier.Together,theseweightsweretuned
through empirical testing to maximize robustness and consistency with observed drift
phenomena,whileensuringthatthecombinedscoreremainsinterpretableonanormalized
[0,1]scale. Thisschemeintegratescomplementaryperspectives—maximumdiscrepancy,
averageshift,andsymmetricdivergence—yieldingabalancedandreliableindicatorof
driftseverity.
Thresholdsforseveritylevels. Tocategorizethecombinedscoreintointerpretable
severitylevels,weconductedexperimentsacrossmultipledatasets(salary,housing,and
gassensordata). Resultsindicatedthatevenrelativelysmalldeviationsinthescore(≥0.05)
alreadysignaledpracticallymeaningfulchangesinthedatadistributions,withpotential

AI2025,6,279 18of24
downstreameffectsonmodelperformance. Onthisbasis,thresholdswereconservatively
defined as: no drift (score < 0.05), low drift (0.05 ≤ score < 0.1), and significant drift
(score≥0.1). Thisconservativedesignreflectstheprinciplethatearlydetectionofsubtle
driftisoftenmorevaluablethanoverlookinggradualshiftsthatmayaccumulateovertime.
Whilealternativethresholdscouldbeadopteddependingonapplicationrequirements,the
chosenvaluesprovidedaconsistentandinterpretableframeworkforourexperiments.
Together,theweightingschemeandthresholddefinitionsformacoherentapproachto
quantifyingandcategorizingdistributionalchange. TheyensurethattheCombinedDrift
Scoreremainsbothsensitivetodifferenttypesofdriftandpracticallyusefulforguiding
decisionsaboutmodelretrainingortransformation.
3.6. DataTransformation
Several approaches exist for mitigating the impact of distributional drift in input
data,includingz-scorenormalization,covariatereweighting,anddomain-invariantrep-
resentationlearning. Amongthese,weemployedthequantiletransformationmethodas
astatisticallygroundedandnon-parametricapproachthatdoesnotrelyonfixeddistri-
butional assumptions. It preserves the rank structure of features while mapping them
to a predefined target distribution (uniform or normal), thereby stabilizing feature be-
havior under non-linear, skewed, or multimodal shifts. Compared to standard scaling,
quantile transformation adapts dynamically to the empirical distribution of incoming
data,makingitparticularlyeffectiveforlong-termorgradualdriftscenarios. Itsrobust-
ness and computational efficiency also make it suitable for both streaming and batch
adaptationpipelines.
Thistransformationmapsfeaturevaluestoauniformornormaldistributionbasedon
theirempiricalquantiles,effectivelynormalizingfeaturedistributionswithoutmodifying
theunderlyingmodel. Thismethodpossesbothadvantagesanddisadvantages,further
detailscanbefoundinTable11.
Table11.Reviewofquantiletransformationmethod.
Advantages Limitations
Univariateoperation: Thetransformationisapplied
independentlytoeachfeatureanddoesnotcaptureor
preservedependenciesorcorrelationsbetween
Model-agnostic: Thetransformationoperatesattheinput
multiplefeatures.
level,requiringnochangesorretrainingoftheexisting
Monotonicityconstraint: Whileitpreservestheorderof
predictivemodel.
featurevalues,applyingquantiletransformsblindly
Noretrainingneeded: Becausethemodelprocesses
acrosscorrelatedfeaturesmaydistorttheir
transformedinputsseamlessly,thisapproachavoidscostly
relationships,potentiallyaffectingmodel
retrainingcycles.
interpretabilityorperformance.
Non-parametric: Itmakesnoassumptionsaboutthe
Samplesizesensitivity: Accuratequantileestimation
underlyingdatadistribution(e.g.,Gaussian),adapting
requiressufficientlylargeandrepresentativesamples;
flexiblytovariousfeatureshapes.
smallsamplewindowsmayleadtonoisyor
Effectiveforcovariatedrift: Particularlyusefulwhenthe
unstabletransformations.
inputfeaturedistributionsshiftovertime,helpingstabilize
Doesnotaddressconceptdrift: Changesinthe
modelperformanceinthepresenceofcovariatedrift.
relationshipbetweeninputsandoutputs(labelor
conceptdrift)arenotmitigatedbythismethodalone
andrequireadditionalstrategies.
QuantileTransformationalgorithm
• MaptheempiricalCDFofthenewdatatotheempiricalCDFofolddatafeature-wise.

AI2025,6,279 19of24
• Foreachfeatureortarget:
x = F −1(F (x )) (3)
new_transformed old new new
whereF andF
−1areempiricalCDFsofthefeatureinnewandolddata,respectively.
new old
This“warps”thenewdatadistributiontolookliketheold.
Thequantiletransformationmethodwastestedbymappingthe2024salarydistribu-
tionontothe2023distribution,aimingtoreducedistributionaldifferenceswhilepreserving
the overall data structure. The transformation aligns the quantiles of the 2024 salaries
withthoseof2023,effectivelynormalizingfordistributionalshifts. Theeffectofquantile
transformationisshowninTable12.
Table12.Resultsbeforeandafterquantiletransformation.
Metric BeforeTransformation AfterTransformation
KSStatistic 0.0559 0.0072
WassersteinDistance 7943.26 170.93
TheKolmogorov–Smirnov(KS)statisticdecreasedsubstantiallyfrom0.0559to0.0072,
indicatingadramaticreductioninthemaximumdifferencebetweentheempiricalcumula-
tivedistributionsofthetwoyears.
Similarly,theWassersteindistancedroppedsharplyfrom7943.26to170.93,reflecting
amuchsmalleraverageshiftinsalaryvaluesafterthetransformation.
These results demonstrate that quantile transformation can effectively align distri-
butionsacrossyears,mitigatingcovariatedriftandhelpingmaintainmodelrobustness
withoutretraining.
3.7. TimeandMemoryComplexityAnalysis
Ateachtimestep,wemaintaintwoper-featureslidingwindowsovertheincoming
stream—ashortwindowofsizew andalongwindowofsizew (total w = w + w )—and
s l s l
compute a severity score by aggregating three divergences between the two windows:
two-sampleKolmogorov–Smirnov(KS),1-Wasserstein(W1),andJensen–Shannon(JS).For
exactcomputationfromraw1-Dsamples,perfeaturewesorttheconcatenatedsamples
toobtainempiricalCDFsandcumulativesums;KSandW1arethenobtainedbyasingle
linearscan,whileJSiscomputedfromhistogramswithbbins. Thisyieldsaper-steptime
ofO(wlogw+b)(equivalentlyO(w logw +w logw +b))andmemoryO(w+b)tohold
s s l l
(sorted)windowsandcounts.
Across d features, the detection cost is therefore T = O(d(wlogw+b)) with
detect
memoryO(d(w+b)). Toreducerecomputation,wealsoreportastreamingvariantthat
maintainsper-featuresummaries: rollinghistogramsforJSandfixed-sizequantilesketches
forKS/W1withsummarysizeqindependentofw. Eachnewobservationtriggersconstant-
timeamortizedupdates(insertingthenewitemandexpiringtheoldest),andthescore
is evaluated from the summaries in O(q+b) time per feature. Consequently, stream-
ing detection costs T = O(d(q+b)) with O(1) amortized updates per arrival and
detect
memoryO(O(d(q+b)). Theaggregateddivergencesarefinallycombinedintoaunified
severityscore.
Theproposedseverityscoreisadaptivebydesign,allowingthesystemtorespond
proportionallytothedetectedlevelofdriftratherthantriggeringfullmodelretraining
immediately.Byintegratingquantiletransformation,themethodnormalizesheterogeneous
featuredistributions,ensuringrobustnessofdriftdetectionacrossvaryingdatascales. This

AI2025,6,279 20of24
adaptivemechanismenablesincrementalupdatesundermoderatedriftandreservesfull
retrainingonlyforseverecases,therebyoptimizingcomputationalefficiency.
ThequantiletransformationstepcontributesatimecomplexityofO(nlogn)—dominated
bysortingoperations—andamemorycomplexityofO(n),asthetransformedcumulative
distributionmustberetainedforsubsequentmetriccomputation. Thesepropertiesensure
thattheadaptiveseverityscoreremainscomputationallyfeasiblewhilepreservingsensitivity
todistributionalchangesacrosstime.
Incontrast, theROSEframeworkexhibitsasignificantlyhighercomputationalburden.
Its worst-case time complexity is O(2kλ|S|), where k is the number of base classifiers, λ is
theensembleupdaterate, and|S|isthestreamsize. ThememorycomplexityofROSEis
O((2krvlc)+(|w|f)),incorporatingr-dimensionalrandomsubspaceprojections,treestructures,
andper-classslidingwindows.Therefore,thecombinedcostofdetection+quantiletransforma-
tionismarkedlylowerthanROSE’sensemble-basedoverhead,underscoringtheefficiencyand
scalabilityoftheproposedadaptivescoringmechanismforonlineenvironments.
Naturally, purely statistical transformations such as quantile-based normalization
cannotmatchthepredictiveaccuracyoffullmodelretrainingoradaptiveensembleup-
dates in all situations. However, their role is not to replace these mechanisms but to
delay or reduce their frequency in cases where drift severity remains low or moderate.
Byrelyingonlightweightdistributionaladjustments,thesystempreservesstabilityand
acceptableaccuracylevelswhilesubstantiallyreducingcomputationalandmemorycosts.
Inpractice, thistrade-offyieldsconsiderableefficiencygains: minordriftscanoftenbe
mitigatedthroughtransformationalone,whereasonlytherare,severedriftsnecessitate
fulladaptation. Thus,theframeworkachievesabalancedcompromisebetweenaccuracy
preservationandresourceoptimization,makingitparticularlyeffectiveforstreamingor
real-timedeploymentcontexts.
4. Discussion
Concept drift remains one of the most critical challenges in maintaining reliable
machinelearningmodelsindynamicenvironments. Leftunaddressed,driftcanleadto
gradualorsuddendegradationinpredictiveperformance,whichinturnimpactsdecision
quality, user trust, and operational efficiency. The framework proposed in this work
directlyaddressesthischallengebyintroducingaseverity-awareadaptationmechanism.
Byaggregatingmultiplecomplementarystatisticalmetricsintoaunifiedseverityscore,the
methodenablesdata-drivendecisionsaboutwhenandhowtoadaptthemodel. Selective
adaptation—minor,moderate,orsevere—triggersupdatesonlywhenneeded,reducing
costswithoutsacrificingaccuracy.
Theapproachnotonlyoptimizesresourceusagebutalsoenhancesoperationalstability.
Forexample,inreal-worldscenarioswheremodelretrainingincurshighfinancialortime
costs,theabilitytodeferupdatesfornegligibledriftcanyieldsignificantefficiencygains.
At the same time, the system remains vigilant against severe drift events, where rapid
interventionisessentialtopreventsubstantialperformanceloss. Theadaptabilityofthe
thresholds,whichmaybeeitherfixedorstatisticallytunedovertime,furtherstrengthens
therobustnessoftheframeworkacrossdifferentapplicationdomains.
An additional contribution of this work is the exploration of data transformation
strategies to mitigate the effects of drift before triggering model adaptation. Different
transformationscanalterthefeaturespaceinwaysthatreducetheapparentseverityor
impactofdrift,potentiallypostponingoreveneliminatingtheneedforcostlyretraining. In
particular,quantiletransformationreducedtheKSstatisticfrom0.0559to0.0072,normaliz-
ingdistributionsandmitigatingdriftbeforeadaptation. Suchtransformationscansmooth

AI2025,6,279 21of24
distributionalshifts—especiallyforskewedorheavy-tailedfeatures—therebyenhancing
resiliencetogradualdriftandpotentiallydelayingtheneedforcostlyretraining.
While the current method focuses on the severity dimension of drift, future work
canexpandthisdecisionprocesstoincorporatedrifttypeaswell. Notalldriftiscreated
equal—covariateshift, priorprobabilityshift, andconditionaldistributionchangemay
requiredistinctadaptationstrategies. Ahybriddecisionmechanismthatconsidersboththe
magnitudeandthenatureofdriftcouldfurtherrefineupdatepolicies,enablingevenmore
precisetrade-offsbetweenadaptationcostandperformancestability. Suchanextension
wouldopenthedoortotrulyintelligent,context-awaredriftmanagementsystemsthatcan
operateeffectivelyacrossawidevarietyofdynamicdatastreams.
5. Conclusions
Insummary,thisstudyshowsthatcareful,severity-drivenadaptationoffersaprac-
ticalandcost-effectivewaytokeepmodelsperformingwellunderdrift. Theframework
updatesmodelsonlywhenthebenefitsareexpectedtooutweighthecostsandtriessimple
adjustments,likethequantiletransformation,beforemakingbiggerchanges. Thismakes
theapproachsmarterandmoreefficientformachinelearninginchangingenvironments.
ThesignificantdropintheKSstatisticafterapplyingthequantiletransformationhighlights
thevalueoftargetedpreprocessinginreducingdrifteffects. Inthefuture,animportant
extensionwillbetoadaptnotonlytotheseveritybutalsotothetypeofdrift—suchas
covariate shift, prior probability shift, or concept shift—allowing for more precise and
context-awaremodelupdates. Thiscouldmaketheframeworkevenmoreefficientand
robustacrossawiderangeofreal-worldscenarios.
AuthorContributions:Conceptualization,K.S.;methodology,K.S.;software,K.S.;validation,P.P.;
formalanalysis,P.P.;investigation,P.P.;resources,K.S.;datacuration,K.S.;writing—originaldraft
preparation,K.S.andP.P.;writing—reviewandediting,K.S.andP.P.;visualization,K.S.;supervision,
P.P.;projectadministration,P.P.;fundingacquisition,P.P.Allauthorshavereadandagreedtothe
publishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Therawdatausedinthisstudyareavailableatthefollowingopen-
sourcelink:https://www.kaggle.com/code/fahadrehman07/data-science-job-salary-prediction-
glassdoor/input,accessedon13August2025.
Acknowledgments:Duringthepreparationofthismanuscript,theauthorusedChatGPT(GPT-3.5,
OpenAI)forthepurposesofsearchingforrelevantliteraturerelatedtothetopicandvalidatingthe
clarityandconsistencyofthetext.Theauthorshavereviewedandeditedtheoutputandtakesfull
responsibilityforthecontentofthispublication.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
EN Entry-levelroles
EX Executiveroles
MI Mid-levelroles
SE Seniorroles
LDA LinearDiscriminantAnalysis
KS Kolmogorov–Smirnov

AI2025,6,279
22of24
|     |     |     | AD  | Anderson–Darling           |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
|     |     |     | KL  | Kullback–LeiblerDivergence |     |     |     |     |     |
|     |     |     | JS  | Jensen–ShannonDivergence   |     |     |     |     |     |
|     |     |     | PSI | PopulationStabilityIndex   |     |     |     |     |     |
|     |     |     | MMD | MaximumMeanDiscrepancy     |     |     |     |     |     |
AppendixA
|     |     |     | AppendixA.1. MetricsJustification |     |     |     |     |     |     |
| --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
TableA1.Driftmetricscomparison.
|                    | Metric | WhatitMeasures   |     |                   | Pros |                     | Cons        |     | UseCase           |
| ------------------ | ------ | ---------------- | --- | ----------------- | ---- | ------------------- | ----------- | --- | ----------------- |
| Kolmogorov–Smirnov |        |                  |     |                   |      | Lesssensitivetotail |             |     | Quickgeneraldrift |
|                    |        | MaxCDFdifference |     | Simple,well-known |      |                     |             |     |                   |
|                    | (KS)   |                  |     |                   |      |                     | differences |     | check             |
Highlysensitiveto
|                  |      |                       | WeightedCDF | MoresensitivethanKS |                   |                   |                | Detectingsubtletail |                |
| ---------------- | ---- | --------------------- | ----------- | ------------------- | ----------------- | ----------------- | -------------- | ------------------- | -------------- |
| Anderson–Darling |      |                       |             |                     |                   |                   | samplesize,can |                     |                |
|                  |      | difference(emphasizes |             |                     | todifferencesin   |                   |                | changes,whensample  |                |
|                  | (AD) |                       |             |                     |                   | exaggeratedriftin |                |                     |                |
|                  |      |                       | tails)      |                     | distributiontails |                   |                |                     | sizeismoderate |
largedatasets
Wassersteindistance
Averagedistance Intuitivedistance Computationally Goodforquantifying
(EarthMover’s
|     |     | betweendistributions |     |     | measure |     | heavier |     | practicaldifference |
| --- | --- | -------------------- | --- | --- | ------- | --- | ------- | --- | ------------------- |
Distance)
|     |                | Howmuchonedist     |              |                      |       | Asymmetric,undefined |                | Usefulifdistributions |         |
| --- | -------------- | ------------------ | ------------ | -------------------- | ----- | -------------------- | -------------- | --------------------- | ------- |
|     | KLdivergence   |                    |              | Informationtheoretic |       |                      |                |                       |         |
|     |                | differsfromanother |              |                      |       |                      | ifzerobins     |                       | arePDFs |
|     | Jensen-Shannon | Symmetricversionof |              | Symmetric,bounded    |       |                      |                |                       |         |
|     |                |                    |              |                      |       |                      | StillneedsPDFs | MorestablethanKL      |         |
|     | divergence     |                    | KLdivergence |                      | (0–1) |                      |                |                       |         |
PopulationStability Measurespopulation Popularincredit Needsbinningandcare
Usedforscorecarddrift
|     | Index(PSI) | changesinbins |     | risk/modelmonitoring |     |     | withbinedges |     |     |
| --- | ---------- | ------------- | --- | -------------------- | --- | --- | ------------ | --- | --- |
Energy
| distance/Maximum |     |     | Kernel-based |     | Powerful, |     |     | Goodformultivariate |     |
| ---------------- | --- | --- | ------------ | --- | --------- | --- | --- | ------------------- | --- |
Morecomplex
| MeanDiscrepancy |     | distributiondistance |     |     | non-parametric |     |     |     | data |
| --------------- | --- | -------------------- | --- | --- | -------------- | --- | --- | --- | ---- |
(MMD)
|     |     |     | AppendixA.2. Pseudocode |     |     |     |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
foreachtimestept:
updateshort_term_window(X_s,y_s)
updatelong_term_window(X_l,y_l)
d_KS=KS_distance(X_s,X_l)
d_W=Wasserstein_distance(X_s,X_l)
d_JS=JS_divergence(X_s,X_l)
S=alpha*d_KS+beta*d_W+gamma*d_JS
#CompareseverityscoreSwiththresholds(θ1,θ2)
#todecidetheadaptationstrategy.
ifS<theta1:
action=“none”#negligibledrift→noupdate
elifS<theta2:
action=“incremental_update”#moderatedrift→smallupdate
M=update_model(M,X_s,y_s,lr=small)
else:
action=“full_retrain”#severedrift→fullretraining
M=train_new_model(X_s,y_s)
log(S,action)
Summary. Thispseudocodeformalizestheseverity-awareadaptationstrategy: the
combineddriftscoreSiscontinuouslyevaluatedagainsttwothresholds(θ 1 ,θ 2 ). Ifdrift
|     |     |     | (S  |     |     |     |     | ≤ S |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
is negligible < θ 1 ), no update is performed; if moderate (θ 1 < θ 2 ), the model is

AI2025,6,279 23of24
incrementallyupdatedwithasmalllearningrate;andifsevere(S≥θ ),afullretrainingis
2
triggered. Thisensuresthatcomputationallyexpensiveretrainingisreservedonlyforcases
wherepredictiveperformancewouldotherwisedegradesubstantially.
AppendixA.3. QuantileTransformation
LetX betheincoming(drifting)dataandX bethereference(baseline)data. The
new ref
methodinvolvesthefollowingsteps:
1. Rank-basedquantileestimation:
Eachsamplex ∈ X isassignedaquantilerankq basedonitspositioninthesorted
i new i
distributionofX :
new
rank(x )
q = i , (A1)
i
n
wherenisthenumberofsamplesinX .
new
2. Inversemappingtoreferencespace:
Thevaluecorrespondingtothesamequantileq islookedupinthereferencedistribu-
i
tionX ,resultinginthetransformedsample:
ref
x’ = F −1(q ). (A2)
i ref i
whereF
−1istheinverseempiricalCDFofthereferencedata.
ref
References
1. Castle,S.;Schwarzenberg,R.;Pourvali,M.Detectingcovariatedriftwithexplanations.InProceedingsoftheCCFInternational
ConferenceonNaturalLanguageProcessingandChineseComputing,Qingdao,China,13–17October2021;SpringerInternational
Publishing:Cham,Switzerland,2021;pp.317–322.[CrossRef]
2. Shvorob,I.NewApproachforSavingSemistructuredMedicalData.InProceedingsoftheAdvancesinIntelligentSystemsand
Computing:SelectedPapersfromtheInternationalConferenceonComputerScienceandInformationTechnologies,CSIT2016,
Lviv,Ukraine,6–10September2016;SpringerInternationalPublishing:Cham,Switzerland,2016;pp.29–40.[CrossRef]
3. Chikoore, R.; Kogeda, O.P.; Ojo, S.O. Recent Approaches to Drift Effects in Credit Rating Models. In Proceedings of the
InternationalConferenceone-Infrastructureande-ServicesforDevelopingCountries,Online,2–4December2020;Springer
InternationalPublishing:Cham,Switzerland,2020;pp.237–253.[CrossRef]
4. Arora,S.;Rani,R.;Saxena,N.Asystematicreviewondetectionandadaptationofconceptdriftinstreamingdatausingmachine
learningtechniques.WileyInterdiscip.Rev.DataMin.Knowl.Discov.2024,14,e1536.[CrossRef]
5. Dritsas,E.;Trigka,M.MachineLearningine-Commerce: Trends,Applications,andFutureChallenges. IEEEAccess2025,13,
99048–99067.[CrossRef]
6. Kang,M.;Kim,S.;Jin,K.H.;Adeli,E.;Pohl,K.M.;Park,S.H.FedNN:Federatedlearningonconceptdriftdatausingweightand
adaptivegroupnormalizations.PatternRecognit.2024,149,110230.[CrossRef]
7. Prathapan,S.;Samala,R.K.;Hadjiyski,N.;D’hAese,P.-F.;Maldonado,F.;Nguyen,P.;Yesha,Y.;Sahiner,B.Quantifyinginput
datadriftinmedicalmachinelearningmodelsbydetectingchange-pointsintime-seriesdata. InProceedingsoftheMedical
Imaging 2024: Computer-Aided Diagnosis, SPIE, San Diego, CA, USA, 18–22 February 2024; pp. 66–75. Available online:
https://ui.adsabs.harvard.edu/abs/2024SPIE12927E..0EP(accessedon12August2025).
8. Gama,J.;Žliobaite˙,I.;Bifet,A.;Pechenizkiy,M.;Bouchachia,A.Asurveyonconceptdriftadaptation.ACMComput.Surv.2014,
46,1–37.[CrossRef]
9. Darwish, S.M.; Salama, A.I.; Elzoghabi, A.A. Intelligent approach to detecting online fraudulent trading with solution for
imbalanceddatainfintechforensics.Sci.Rep.2025,15,17983.[CrossRef][PubMed]
10. Cano,A.;Krawczyk,B.ROSE:Robustonlineself-adjustingensembleforcontinuallearningonimbalanceddriftingdatastreams.
Mach.Learn.2022,111,2561–2599.[CrossRef]
11. Lin,C.-C.;Deng,D.-J.;Kuo,C.-H.;Chen,L.ConceptdriftdetectionandadaptioninbigimbalanceindustrialIoTdatausingan
ensemblelearningmethodofofflineclassifiers.IEEEAccess2019,7,56198–56207.[CrossRef]
12. Wang,K.;Xiong,L.;Liu,A.;Zhang,G.;Lu,J.Aself-adaptiveensembleforuserinterestdriftlearning.Neurocomputing2024,577,
127308.[CrossRef]

AI2025,6,279 24of24
13. Du,K.-L.;Zhang,R.;Jiang,B.;Zeng,J.;Lu,J.FoundationsandInnovationsinDataFusionandEnsembleLearningforEffective
Consensus.Mathematics2025,13,587.[CrossRef]
14. Díaz,A.O.;delCampo-Ávila,J.;Ramos-Jiménez,G.;Blanco,I.F.;Mota,Y.C.;Hechavarría,A.M.;Morales-Bueno,R.Fastadapting
ensemble:Anewalgorithmforminingdatastreamswithconceptdrift.Sci.WorldJ.2015,2015,235810.[CrossRef][PubMed]
15. Yang,L.;Shami,A.AlightweightconceptdriftdetectionandadaptationframeworkforIoTdatastreams.IEEEInternetThings
Mag.2021,4,96–101.[CrossRef]
16. Yan,J.;Zhai,D.;Jiang,J.;Liu,X.Target-guidedadaptivebaseclassreweightingforfew-shotlearning.InProceedingsofthe29th
ACMInternationalConferenceonMultimedia,Chengdu,China,20–24October2021;pp.5335–5343.[CrossRef]
17. Wang,W.;Li,H.;Ding,Z.;Nie,F.;Chen,J.;Dong,X.;Wang,Z.Rethinkingmaximummeandiscrepancyforvisualdomain
adaptation.IEEETrans.NeuralNetw.Learn.Syst.2021,34,264–277.[CrossRef][PubMed]
18. Brüggemann,R.;Lütkepohl,H.;Saikkonen,P.Residualautocorrelationtestingforvectorerrorcorrectionmodels.J.Econom.2006,
134,579–604.[CrossRef]
19. Bogner,K.;Pappenberger,F.;Cloke,H.L.Thenormalquantiletransformationanditsapplicationinafloodforecastingsystem.
Hydrol.EarthSyst.Sci.2012,16,1085–1094.[CrossRef]
20. Massey,F.J.,Jr.TheKolmogorov-Smirnovtestforgoodnessoffit.J.Am.Stat.Assoc.1951,46,68–78.[CrossRef]
21. Hoadley,A.B.OntheProbabilityofLargeDeviationsofFunctionsofSeveralEmpiricalCDF’S.Ann.Math.Stat.1967,38,360–381.
[CrossRef]
22. vanErven,T.;Harremos,P.RényidivergenceandKullback-Leiblerdivergence. IEEETrans. Inf. Theory2014,60,3797–3820.
[CrossRef]
23. Scholz,F.W.;Stephens,M.A.K-sampleAnderson–Darlingtests.J.Am.Stat.Assoc.1987,82,918–924.[CrossRef]
24. Panaretos,V.M.;Zemel,Y.StatisticalaspectsofWassersteindistances.Annu.Rev.Stat.ItsAppl.2019,6,405–431.[CrossRef]
25. Menéndez,M.;Pardo,J.;Pardo,L.;Pardo,M.TheJensen-Shannondivergence.J.Frankl.Inst.1997,334,307–318.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.