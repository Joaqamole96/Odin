future internet
Article
Beyond Firewall: Leveraging Machine Learning for Real-Time
Insider Threats Identification and User Profiling
SaifAl-DeanQawasmeh1 andAliAbdullahS.AlQahtani2,*
1 DepartmentofAppliedScienceandTechnology,NorthCarolinaAgriculturalandTechnicalStateUniversity,
Greensboro,NC27411,USA;qawasmeh.saif1@gmail.com
2 DepartmentofSoftwareEngineering(CybersecurityTrack),PrinceSultanUniversity,
Riyadh12435,SaudiArabia
* Correspondence:aaalqahtani@psu.edu.sa
Abstract: Insiderthreatsposeasignificantchallengetoorganizationalcybersecurity,often
leading to catastrophic financial and reputational damages. Traditional tools such as
firewallsandantivirussystemslackthesophisticationneededtodetectandmitigatethese
threatsinrealtime. Thispaperintroducesamachinelearning-basedsystemthatintegrates
real-time anomaly detection with dynamic user profiling, enabling the classification of
employeesintocategoriesoflow,medium,andhighrisk. Thesystemwasvalidatedusing
asyntheticdataset,achievingexceptionalaccuracyacrossmachinelearningmodels,with
XGBoostemergingasthemosteffective.
Keywords:insiderthreats;machinelearning;real-timedetection;userbehaviorclassification;
riskassessment;anomalydetection;dynamicprofiling
1. Introduction
In today’s digital transformation era, organizations are increasingly vulnerable to
insider cyber threats. Insider attacks often exhibit subtle and complex behaviors that
makethemdifficulttodetectinrealtime,leadingtoseveredatabreaches,financiallosses,
anddamagetoreputations. Accordingtothe2024DataBreachInvestigationsReportby
Verizon,insidersaccountfor31%ofdatabreachesinthefinancialandinsurancesectors[1].
Received:1January2025 Additionally,the2024IBMCostofaDataBreachReportrevealedthatmaliciousinsider
Revised:23January2025 attacks resulted in the highest average costs, at USD 4.99 million [2]. Employees and
Accepted:24January2025
internaluserswithprivilegedaccesstosensitivesystemsposesignificantrisks,particularly
Published:18February2025
as they possess knowledge of how to evade detection [3]. This complicates efforts to
Citation: Qawasmeh,S.A.-D.;
identifyandmitigateinsiderthreatsusingtraditionalsecuritymeasuressuchasantivirus
AlQahtani,A.A.S.BeyondFirewall:
andfirewalls,whichremaininadequatefordetectingmaliciousinsiders[4]. Conventional
LeveragingMachineLearningfor
insiderthreatdetectiontoolssuchasIntrusionDetectionSystems(IDS)primarilyfocuson
Real-TimeInsiderThreats
IdentificationandUserProfiling. identifyingknownthreats. Althoughthisapproachisusefulwhentheattacksignaturesare
FutureInternet2025,17,93. https:// previouslyknown,itmaybeinsufficienttodetectnovelorpreviouslyunknowninsider
doi.org/10.3390/fi17020093 threatssuchaszero-dayattacks[5,6]. Anomaly-basedIDSmayovercomethisdrawbackby
Copyright:©2025bytheauthors. analyzinguserbehaviorandcheckingwhetheritdeviatessignificantlyfromtheestablished
LicenseeMDPI,Basel,Switzerland. baseline. However,amajorchallengeisthepossibilityofadversariesgraduallymodifying
Thisarticleisanopenaccessarticle theirbehaviortoavoiddetection,effectively“tricking”thesystemandincreasingtherate
distributedunderthetermsand
offalsenegatives[7].
conditionsoftheCreativeCommons
Machine learning (ML) has emerged as a critical tool in enhancing insider threat
Attribution(CCBY)license
detection. ML algorithms can identify abnormal behaviors (e.g., clicking unsafe links,
(https://creativecommons.org/
licenses/by/4.0/). logginginduringnon-businesshours)innear-realtime. Thesemodelscontinuouslylearn
FutureInternet2025,17,93 https://doi.org/10.3390/fi17020093

FutureInternet2025,17,93 2of26
fromnewdata,allowingthemtoanalyzelargevolumesofinformation,improvedetection
accuracy, and reduce false positives. However, current ML-based detection tools often
lackkeycapabilitiessuchasreal-timedataanalysisanddynamicclassificationofusers
basedontheirbehavior. Addressingthesegapsiscrucialforbuildingmoreeffectivethreat
detectionsystems.
ThispaperintroducesaninnovativeMLtoolthatintegratesreal-timedataanalysis
withdynamicuserbehaviorclassificationtoenhancethedetectionofabnormalemployee
behavior. Thetoolleveragescontinuouslearningtoadapttoevolvinguserbehaviorpat-
terns,enablingproactiveidentificationofpotentiallyconcerningactivities. Toaddressthe
challengesassociatedwithreal-worlddata,theproposedtoolutilizesasyntheticdataset
thateffectivelymimicsrealisticorganizationalenvironments. Byreplicatingkeycharacter-
isticsofreal-worlduserbehaviorsuchasaccesspatternsandnetworktrafficwhileallowing
for controlled introduction of simulated anomalous activities, this approach mitigates
privacyconcernsandfacilitatesrigorousexperimentation. Thisresearchdemonstratesthe
potentialofsyntheticdataandadvancedMLtechniquesinimprovingtheaccuracyand
effectivenessofsystemsfordetectingabnormalemployeebehavior.
Thispaperaddressesthefollowingkeyquestionsinthefieldofcybersecuritybehavior
detectionandclassification:
1. HowcanMLbeleveragedtoimprovethereal-timedetectionandidentificationof
insiderthreatsinorganizationalenvironments? AnsweredinSection3.1.
2. Whatlimitationsofexistingsecuritytoolscanbeaddressedthroughreal-timedata
analysisanddynamicuserprofilingusingML?AnsweredinSection2.
3. HowcanMLmodelseffectivelyclassifyusersbasedontheirbehaviorandassignrisk
levelstodetectandmitigateinsiderthreatsinreal-time? AnsweredinSection5.
4. WhatuniquecapabilitiesdoestheproposedMLtoolprovideovertraditionalsecurity
measures,especiallyintermsofautomatingreal-timethreatdetectionanduserrisk
profiling? AnsweredinSection3.2.
The remainder of this paper is structured as follows: Section 2 describes the back-
groundandrationaleofthestudy;Section3providesanoverviewoftheproposedtool;
Section4explainsthestepstakentoacquire,clean,andvisualizethedata;Section5presents
thefindingsofthestudy;finally,Section6concludeswithasummaryoftheproposedtool
andourfindings.
2. RelatedWork
Effective monitoring of insider threats is crucial for organizational cybersecurity,
includingidentifyingriskyemployeebehavior,ensuringaccountability,andmitigating
potential impacts. This section reviews both traditional and ML-based approaches for
insiderthreatdetection,highlightingtheiradvantagesandlimitations.
2.1. Traditional-Based
Traditionalinsiderthreatdetectionreliesonpredefinedrulesandstaticpolicies,often
employingmethodssuchaslogactivitymonitoring,rule-basedIDS,andEndpointDetec-
tionandResponseSolutions(EDR)[8–10]. AnomalydetectiontoolssuchasXABA[11]and
scoring-basedactivityloganalysis[12]usepredefinedkeywordsandscoringmechanisms;
however, their dependence on manual thresholds and analyst intervention introduces
performancebottlenecksandlimitsadaptabilitytonovelthreats.
Signature-basedIDS,suchasSNORT,Suricata,andZeekrelyonmatchingknownma-
liciouspatterns,butarevulnerabletozero-dayattacks[13–19].TheseIDStoolshavelimited
capabilitiesagainstpreviouslyunseenthreats,astheyrelyonafixeddatabaseofknown

FutureInternet2025,17,93 3of26
signatures. WhilecombiningIDStoolswithothernetworkanalysistoolssuchasWireshark
canenhancedetectionefficiency,relianceonpredefinedruleslimitsadaptability[20].
ApproachessuchasCorporateInsiderThreatDetection(CITD)[21]andtree-structured
activityprofiling[22]aimtoreducefalsepositivesbyincorporatinganalystfeedback. How-
ever,manualinterventionintroduceschallengesaroundscalingandreducestheefficacy
of real-time analysis. Adversarial Risk Analysis (ARA) models [23,24] provide a struc-
turedapproachforinsiderthreatdetection;however,theirstaticnaturelimitsadaptability.
Methodsbasedonrecordinguserinputs,suchaskeyloggers[25],faceprivacyconcerns
andreducedefficiency. Thetwo-stepinsiderdetectionapproachproposedby[26]further
illustratesthechallengesofbalancingaccuracyandadaptabilityintraditionalmethods.
Overall,traditionalmethodssufferfromhighfalsepositives,staticadaptability,and
dependenceonhumanintervention,makingthemlesseffectivefordynamicandevolv-
ingthreats.
2.2. ML-Based
ML has emerged as a potent tool for insider threat detection, enabling early-stage
identificationofanomalousbehavior,scalability,andpredictiveanalysis[27,28]. ML-based
IDSenhancesdetectionthroughmodelsthatcanidentifynovelattackpatterns.Forexample,
RandomForest(RF)andNaiveBayesclassifiershavebeenusedinanomalydetectionand
demonstratedgoodaccuracy,althoughtheyarelimitedbyalackofadaptivefeatures[29].
StudiesemployingsupervisedlearningmodelssuchasRF,SupportVectorMachine
(SVM),andDecisionTree(DT)haveshownpromisingresultsfordetectinginsiderthreats
usinglogdata[30–32]. However,challengesincluderelianceonmanualthresholdsanda
lackofreal-timeanalysiscapabilities.Theintegrationofdatapreprocessingtechniquessuch
asSMOTEcanimproveaccuracy,butintroduceadditionalcomputationaloverhead[33].
EnsemblelearningmethodssuchasGradientBoostingandIsolationForest(IF)have
demonstrated improved detection rates; however, their higher computational require-
ments limit real-time performance [34–36]. Hybrid approaches such as combining su-
pervised and unsupervised algorithms [37] have shown improved anomaly detection
scores,buttheirrelianceonbatchanalysisofhistoricaldatalimitstheireffectivenessfor
continuousmonitoring.
Recent research has emphasized human behavior analysis for insider threat detec-
tion. Tools combining RF, XGBoost, and other ensemble methods [38,39] have shown
high detection accuracy. However, issues persist with real-time adaptability and user
behavior analysis. Studies integrating behavior profiling approaches such as K-means
clustering[40,41]havebeenabletoclassifyemployeesbasedonsessiondata,butoftenfail
toincorporateriskseverityandcontinuousanalysis. SeveralstudieshaveexploredML
techniquesfordetectinginsiderthreatsandabnormalbehaviorinusers. Nandinietal.[42]
employedXGBoostwiththeCostGradientBoostingAlgorithm(CGBA)toclassifyusers
basedontheiractivities,outperformingothermethodssuchasDTandIF.LiandSu[43]
focusedonauniversitywebsite’slogdata,usinglogparsingandclusteringtechniquesfor
anomalydetection,thoughtheyfacedchallengeswithfalsepositivesduetotheirreliance
onthreshold-baseddistances.
SureshandMadhavu[44]improvedtheefficiencyofRFbyusingtheRandomized
WeightedMajorityAlgorithm(RWMA)andFuzzyFeatureAggregation(FFA)toclassify
riskyusers. Otherstudies,suchas[45],havedemonstratedthatIFisthemosteffectiveal-
gorithmwhenappliedtolargedatasets. Real-timedetectionmethodssuchasRADISH[46]
utilizeKNNtodetectinsiderthreats,althoughongoingsessionanalysisremainsmissing.
Vermaetal.[47]appliedK-NearestNeighbours(KNN)andK-meansforclassifying
networktrafficintofivecategories,withKNNshowingsuperioraccuracy. Amultilayered

FutureInternet2025,17,93 4of26
detectionframeworkincorporatingsupervisedandunsupervisedclassifiers(KNN,DT,
RF,andBootstrapAggregating)wasproposedin[48],withKNNachievingthehighest
truepositiverateandRFshowingzerofalsepositives. Beglietal.[49]usedSVMtoclassify
network traffic in healthcare organizations, revealing that detecting sensitive data was
morechallenging.
Kimetal.[50]proposedananomalydetectionsystemusingstatisticalmethodsand
K-means,achievinggooddetectionratesforabnormaluserbehavior,althoughtheirsystem
lackedreal-timecapability. AnevaluationofthreeMLalgorithms(LogisticRegression(LR),
RFandXGBoost)showedthatRFoutperformedtheothersindetectinginsideractivities[51].
Similarly, AI-baseddistancemeasurementtechniquessuchastheLevenshteindistance
wereevaluatedfordetectingIoTsensor-basedinsiderthreatsin[52].
Further,XGBoostcombinedwiththeSMOTEandRandomUndersampling(RUS)data
adjustmenttechniquesachievedhighaccuracyinanomalydetectiontasksontheCERT
dataset[53]. Studiessuchas[54]alsotestedmultiplealgorithms(AdaBoost,NaiveBayes,
andothers)forclassifyinganomalousemails, althoughthedatasetsizewaslimited. In
theIoTdomain,Shaveretal.[55]comparedMLalgorithms,findingRFtobeeffectivefor
anomalydetectiondespiteitshighcomputationaloverhead.
Abhaleetal.[56]exploredabroadersetofsupervisedmodels(RF,SVM,DT,Light
Gradient Boosting Machine (LGBM), ExtraTrees, Gradient Boosting, Ada Boost, KNN,
Multi-LayerPerceptron(MLP),GaussianNaiveBayes,andLR),withSVMachievingthe
highestaccuracy. Anotherstudy[57]usedRFanddeeplearningmodelstoclassifynetwork
attacksintofivetypes,althoughreal-timeadaptationwasnotaddressed. Al-Shehariand
Alsowail[58]employeddifferentdataprocessingtechniques(LabelEncoding,One-Hot
Encoding,SMOTE)toenhanceML-baseddetectionofdataleakageincidents,showingthat
RFandDTperformedbestontheCERTdataset.
Almomanietal.[59]comparedclassifiersforintrusiondetection,withRFandGra-
dientBoostbothperformingwell. Taghavi-Rashidizadehetal.[60]combinedPrincipal
ComponentAnalysis(PCA)andXGBoostforanomalydetectionandachievedhighaccu-
racyontheUNSW-NB15dataset, althoughcontinuousmonitoringwasnotconsidered.
Lastly,Manoharanetal.[61]evaluatedRF,KNN,andDTusingbalanceddatasets,withRF
achievingthehighestaccuracy,althoughinstantaneousdataanalysiswasmissing. Inuwa
andDas[62]comparedMLmodelssuchasSVM,DT,andKNNfordetectingIoTnetwork
anomalies,achievingreal-timedetection;however,theirstudylackeduserbehavioranal-
ysis. Finally, a number of studies have reported exceptionally high detection accuracy.
However,itisimportanttonotethattheseresultswerederivedfromofflinedatasetsrather
thanfromreal-timeinstantaneousdata[63–66]. Overall,ML-basedapproachesimprove
upontraditionalmethodsbyofferingbetterpredictivecapabilitiesandreducedfalseposi-
tives. However,theyoftenrequiresignificantcomputationalresourcesandlackeffective
real-timeclassificationfeatures.
2.3. LimitationsandGaps
Theliteratureindicatesthatwhileextensiveresearchhasbeenconductedoninsider
threatdetectiontools,themajorityoftheseapproachesfailtoprovidebothreal-timeanalysis
andcomprehensiveuserriskclassification. Previoustoolsoftenrelyonofflinedatasets
orhistoricallogfiles, resultingindelayeddetectionandresponse. Thus, thereremains
acriticalneedfortoolsthatcandynamicallyanalyzeuserbehaviorusingcontinuously
updateddata.
The proposed tool aims to bridge this gap by integrating real-time analysis with
dynamicclassificationfeatures,offeringasignificantimprovementoverexistingsolutions.

FutureInternet2025,17,93 5of26
Aqualitativeandquantitativecomparisonofthistoolwithrelatedworksispresentedin
VersionJanuary23,2025submittedtoFutureInternet Sections3.2and5.4. 5of6
3. TheProposedTool
3. TheProposedTool
178
Thissectionoutlinestheproposedtool’sworkflowandprovidesaqualitativecompar-
Thissectionoutlinestheproposedtool’sworkflowandprovidesaqualitativecompar-
isontotherelatedworksdiscussedinSection2. 179
isontotherelatedworksdiscussedinSection2.
180
3.1. Workflow
3.1.Workflow
181
Theproposedtoolcombinesreal-timeanalysiscapabilitiestodetectabnormalitiesand
Theproposedtoolcombinesreal-timeanalysiscapabilitiestodetectabnormalities
182
classifyemployeerisklevels,allbasedonemployees’dailyactivities. Figure1illustrates
andclassifyemployeerisklevels,allbasedonantheemployees’dailyactivities.Figure1
183
theworkflowoftheproposedtool.
illustratestheproposedtoolworkflow.
184
Start
Continuous Activ-
ities Monitoring
Abnormality
Identification
Immediate Alert
Generation
Risk Score
Calculation
Dynamic Em-
ployee Profiling
Classification
of Employees
Administration
Notification
Recurrence
looTsisylanAemit-laeR
looTnoitacfiissalCksiReeyolpmE
Figure1.SystemWorkflowDiagram.
Figure1.Systemworkflowdiagram.
3.1.1. Real-TimeAnalysisTool
3.1.1.Real-timeAnalysisTool
185
1. ContinuousActivitiesMonitoring:
1. ContinuousActivitiesMonitoring:Theproposedtoolprovidescontinuoussurveil-
186
The proposed tool provides continuous surveillance of an organization’s network,
lanceofanorganization’snetwork,capturingreal-timedatathatshowstheorganiza-
187
tion’semployees’dailyaccatpivtuitrieins.greal-timedatathatshowthedailyactivitiesoftheorganization’semployees.
188
2. Abnormality Identification: The system utilizes ML to identify abnormalities by
2. Abnormality Identification: Utilizing ML, the system identifies abnormalities by
189
examininganomalousdailyactivitiesofemployeesontheorganization’snetwork.
examiningtheanomalousdailyactivitiesofemployeesonanorganization’snetwork.
190
3. Immediate Alert Generation: Upon identifying abnormalities, the proposed tool
3. Immediate Alert Generpartoiomnp:tUlypoisnsuideesndtiefytainilgedabanloerrmtsatloitieths,ethceybperrospeocsuerditytootelam191for immediate action.
promptlyissuesdetailedalertstothecybersecurityteamforimmediateaction.Figure
Figure2showsanexampleofageneratedalert. 192
2showsanexampleofthegeneratedalert.
193

FutureInternet2025,17,93 6of26
Figure2.Alertgeneration.
3.1.2. EmployeeRiskClassificationTool
1. RiskScoreCalculation:
Eachemployeeisassignedariskscoredeterminedbytheirdailyactivitieswithinthe
organization’snetwork. TheriskscoreiscalculatedaccordingtoEquation(1):
n
RiskScore = ∑ W ·⊮ (1)
j i
i=1
where:
• RiskScore istheRiskScoreforthe j-threcord.
i
• Thesummation ∑n indicates that we are summing over all features from 1
i=1
ton.
• W istheweightassociatedwiththei-thfeature.
i
⊮
• istheindicatorfunction,whichequals1ifthei-thfeatureF forthej-threcord
ij
is1(indicatingfirst-timeabnormaldailyactivity)and0otherwise(indicatingno
abnormalactivity).
2. DynamicEmployeeProfiling: Followingstep1,employeesaredynamicallyprofiled,
with their profiles undergoing continuous updates to reflect their behavior within
theorganization’snetworksalongwiththeircalculatedriskscores. Inreal-lifesitu-
ations,eachemployee’sprofilewoulddynamicallyevolve,continuouslyrecording
observedabnormalbehaviorsandtheirassociatedriskscores. Forexample,instances
oflogginginoutsidebusinesshourswouldberecordedwithintheemployee’sprofile,
includingtheoccurrencetimeandthecalculatedriskscore. Anyadditionalbehavior
wouldalsobeadded,alongwiththecumulativeriskscoreneededforthesubsequent
classificationstep.
3. ClassificationofEmployees:UtilizingML,eachemployeeisclassifiedintooneofthree
risklevels(low,moderate,orhigh)basedontheupdateddataobtainedinstep2.
4. AdministrationNotification: Employeesidentifiedasmoderateorhighriskarere-
portedtoadministrationfornecessaryinterventions,whichmayincludeadditional
trainingorenhancedmonitoring.
3.1.3. Continuous
1. Recurrence: Theproposedtoolrestartsitsmonitoringprocess,ensuringcontinuous
adaptationandup-to-datesecuritymaintenance.

FutureInternet2025,17,93
7of26
Inatypicalscenario,thetoolcontinuouslymonitorsemployeeactivitiesbytracking
actionssuchaslogintimesandfileaccessandusestheseactionstoestablishabaseline
oftheirnormalbehavior. Iftheemployeelogsinoutsidebusinesshours(weightedat4)
andaccessessensitivefilesunrelatedtotheircurrentproject(weightedat7),thesystem
recognizesthesedeviationsfromthenorm. Analertisgeneratedforthecybersecurityteam
andariskscoreiscalculatedbysummingtheweightsoftheabnormalbehaviors,resulting
inascoreof11. Thisscoreclassifiestheemployeeinthemediumriskcategory,prompting
thecybersecurityteamtoincreasemonitoringoftheemployee’sactivities. Theemployee’s
profileisupdatedwiththesebehaviorsandthesystemresumesitscontinuousmonitoring,
ensuringthattheriskassessmentremainscurrent.
3.2. QualitativeComparisonwiththeDiscussedWorks
AnanalysisoftherelatedworksdiscussedinSection2revealsthateachofthereviewed
papersfacesatleastonelimitationinapplyingMLtoinsiderthreatdetection. Common
challengesincludelackofinstantaneousdatausage,lackofreal-timeanalysis,lackofreal-
timeclassification,non-interactivity,non-continuity,andabsenceofadjustability. Table1
highlightstheseshortcomingsandprovidesaqualitativecomparisonbetweentheproposed
methodandexistingapproachesintheliterature.
Table1.Comparisonwithdiscussedworks,where✓:FeatureSupported,✗:FeatureNotSupported,
N/D:FeatureNotDiscussed.
Study Instantaneous Real-Time Real-TimeUser Non- Continuous Adjustability Detection Classification
|      | Data | Analysis | Classification | Interactive |     |     | Time | Time |
| ---- | ---- | -------- | -------------- | ----------- | --- | --- | ---- | ---- |
|      |      | ✓        | ✗              | ✓           | ✗   | ✗   | ✗    | ✗    |
| [29] | N/D  |          |                |             |     |     |      |      |
|      | ✗    | ✗        | ✗              | ✓           | ✓   | ✗   | ✓    | ✗    |
[30]
| [31] | ✓   | ✓   | ✗   | N/D | ✓   | ✓   | ✗   | ✗   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| [32] | ✓   | ✓   | ✗   | ✗   | ✗   | ✓   | ✓   | ✗   |
|      | ✓   | ✓   | ✗   | ✓   | ✓   | ✗   | ✗   | ✗   |
[33]
| [34] | ✗   | ✓   | ✗   | ✗   | ✓   | ✓   | ✗   | ✗   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| [35] | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✓   | ✗   |
| [36] | ✓   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   |
|      | ✗   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   |
[37]
| [38] | ✓   | ✓   | ✗   | N/D | ✗   | ✓   | ✗   | ✗   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| [39] | ✓   | ✓   | ✗   | N/D | N/D | N/D | ✗   | ✗   |
|      | ✓   | ✓   | ✗   | ✗   | ✓   |     | ✗   | ✗   |
| [40] |     |     |     |     |     | N/D |     |     |
|      | ✓   | ✓   | ✗   | ✗   |     | ✗   | ✗   | ✗   |
| [41] |     |     |     |     | N/D |     |     |     |
| [42] | N/D | ✗   | ✗   | ✓   | N/D | N/D | ✗   | ✗   |
| [43] | ✓   | ✓   | ✗   | ✗   | ✓   | ✗   | ✗   | ✗   |
|      |     | ✓   | ✗   | ✓   |     |     | ✓   | ✗   |
| [44] | N/D |     |     |     | N/D | N/D |     |     |
| [45] | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   |
| [46] | ✓   | ✗   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   |
| [47] | ✗   | ✓   | ✗   |     |     |     | ✗   | ✗   |
|      |     |     |     | N/D | N/D | N/D |     |     |

FutureInternet2025,17,93
8of26
Table1.Cont.
Instantaneous Real-Time Real-TimeUser Non- Detection Classification
| Study |      |          |                |             | Continuous | Adjustability |      |      |
| ----- | ---- | -------- | -------------- | ----------- | ---------- | ------------- | ---- | ---- |
|       | Data | Analysis | Classification | Interactive |            |               | Time | Time |
|       | ✓    | ✓        | ✗              | ✓           | ✓          | ✗             | ✗    | ✗    |
[48]
| [49] | ✓   | ✓   | ✗   | ✓   | ✓   | ✗   | ✓   | ✗   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| [50] | ✓   | ✗   | ✗   | ✓   | ✓   | N/D | ✗   | ✗   |
|      | ✓   | ✓   | ✗   | ✗   | ✓   | ✗   | ✓   | ✗   |
[51]
|     | ✗   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
[52]
| [53] | ✓   | ✗   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| [54] | ✓   | ✓   | ✗   | ✓   | ✗   | N/D | ✗   | ✗   |
|      | ✓   | ✓   | ✗   |     |     | ✓   | ✓   | ✗   |
| [55] |     |     |     | N/D | N/D |     |     |     |
| [56] | ✓   | ✓   | ✗   | ✓   | ✗   | ✗   | ✗   | ✗   |
| [57] | ✓   | ✓   | ✗   | N/D | ✓   | ✗   | ✗   | ✗   |
|      | ✓   | ✗   | ✗   |     | ✓   | ✓   | ✗   | ✗   |
| [58] |     |     |     | N/D |     |     |     |     |
|      | ✓   |     | ✗   | ✓   |     | ✗   | ✗   | ✗   |
| [59] |     | N/D |     |     | N/D |     |     |     |
| [60] | ✗   | ✓   | ✗   | N/D | N/D | ✓   | ✗   | ✗   |
| [61] | ✗   | ✓   | ✗   | ✓   | ✓   | ✓   | ✗   | ✗   |
|      | ✓   | ✓   | ✗   | ✓   |     | ✓   | ✗   | ✗   |
| [62] |     |     |     |     | N/D |     |     |     |
|      | ✗   | ✓   | ✗   |     |     | ✗   | ✓   | ✗   |
| [63] |     |     |     | N/D | N/D |     |     |     |
| [64] | ✗   | ✗   | ✗   | ✓   | N/D | N/D | ✗   | ✗   |
| [65] | ✗   | ✓   | ✗   | N/D | N/D | ✓   | ✓   | ✗   |
|      | ✗   | ✓   | ✗   |     |     |     | ✗   | ✗   |
| [66] |     |     |     | N/D | N/D | N/D |     |     |
| Ours | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   | ✓   |
4. Dataset
Thedatasetformsthecornerstoneofourstudy,providingthebasisforouranalysis
and findings. This section details the data acquisition process along with the method-
ologies used for data preprocessing and validation, feature engineering, data privacy
considerations,andfeatureselection.
4.1. DataAcquisition
Weutilizedasyntheticdatasetspecificallycraftedtomimicreal-worldinsiderthreat
scenarios,allowingforadjustmentsalignedwithvariousorganizationalcybersecurityob-
jectives. Generatingsyntheticdataaddressesthesecurityandprivacyconcernsthatmake
itchallengingtoaccessrealorganizationaldatasets. Thedatasetcomprises10,000records
representing the activities of 500 employees over 4 weeks (expanded to 23,483 after re-
sampling) with 22 features, including Personally Identifiable Information (PII) such as
users’names,emailaddresses,SocialSecurityNumbers(SSNs),DatesofBirth(DoB),and
employeenumbers,aswellas17distinctanomalousactivitytypesdetailedinTable2.
Toensurethatthesyntheticdatasetcanaccuratelyreflectreal-worldscenarios, we
incorporatedseveralkeycharacteristics. First,thedatasetpredominantlycomprisesnormal
employeebehaviors,mirroringthetypicaldistributionobservedinreal-worldorganiza-
tions. Additionally,time-relatedfeatureswereincludedinordertocapturethetemporal
dynamicsofemployeeactivities,specificallythetimingofthemostcommonabnormalbe-
haviors.Furthermore,thedistributionofabnormalbehaviorsinthedatasetwasconstructed
toavoidbeingskewedtowardspecifictypesofanomalies,ensuringarepresentativerange

FutureInternet2025,17,93
9of26
of potential threats. Finally, the dataset contains a sufficient amount of data points to
effectivelycapturethecomplexityofemployeebehaviorpatterns.
Table2.Abnormalbehaviorsdescription.
| ActivityType |     | Description | Features | Weight |
| ------------ | --- | ----------- | -------- | ------ |
Logintime,numberoffailedattempts,
| LoginAttempts | Logginginoutsidethenormalbusinesshours |     |     | 4   |
| ------------- | -------------------------------------- | --- | --- | --- |
loginlocation,anddevicetype
Accesstime,filetype,accesslocation,and
| SensitiveFilesAccess | Unauthorizedentryintoconfidentialdata |     |     | 7   |
| -------------------- | ------------------------------------- | --- | --- | --- |
userprivilege
Installationoruseofunapprovedsoftware Installationtime,userpermission,and
| UnauthorizedSoftware |     |                      |          | 9   |
| -------------------- | --- | -------------------- | -------- | --- |
|                      |     | withinanorganization | location |     |
Unauthorizedorunmonitoredtransferof
DataTransfer sensitiveorconfidentialdatawithinan Transfertime,filesize,anddestination 6
organization
Unauthorizedaccessorfrequentvisitationof Visittime,websitecategory,andvisit
| Non-WorkWebsitesVisited |                               |     |           | 5   |
| ----------------------- | ----------------------------- | --- | --------- | --- |
|                         | websitesunrelatedtoworkduties |     | frequency |     |
Unauthorizedentryoraccesstorestricted Entrytime,locationaccessed,andbadge
| PhysicalAccess | areas,equipment,orsensitiveinformation |     | type | 8   |
| -------------- | -------------------------------------- | --- | ---- | --- |
Deceiveindividualsintodivulging
SocialEngineeringAttacks confidentialinformationorperformingactions Attacktype,responsetime,andsensitivity 8
thatcompromisesecurityprotocols
Pastsecuritybreaches,dataleaks,or
Incidenttype,incidentdate,user
| PreviousIncidents | unauthorizedactivitieswithinan |     |     | 10  |
| ----------------- | ------------------------------ | --- | --- | --- |
involvement,andincidentseverity
organization’sinformationsystems
Disclosingsensitiveorconfidential Sharingtime,informationtype,and
| PublicInfoShared |                              |     |                  | 5   |
| ---------------- | ---------------------------- | --- | ---------------- | --- |
|                  | informationtothepublicdomain |     | platformlocation |     |
InteractionWithMalicious Engagingwithfraudulentorcompromised Interactiontime,maliciousflag,anduser
8
| Accounts |     | onlineentities | reaction |     |
| -------- | --- | -------------- | -------- | --- |
Significantalterationsinanindividual’s
Changetype,frequency,timeofchange,
| BehaviorChange | actionsorhabits,oftensignalingpotential |     |     | 6   |
| -------------- | --------------------------------------- | --- | --- | --- |
andusermotivation
securityconcerns
Illegalengagementandcommunication
NetworkInteraction activitiesthatoccurwithinanetworked Protocoltype,datavolume,andfrequency 7
environment
Inadequateorcarelessinformationsecurity Practicetype,frequency,userawareness,
| PoorInfoSecPractices |     |           |             | 9   |
| -------------------- | --- | --------- | ----------- | --- |
|                      |     | practices | andseverity |     |
Uploadtime,filetype,encryptionstatus,and Uploadtime,filetype,encryptionstatus,
| UploadSensitiveInformation |     |               |                  | 8   |
| -------------------------- | --- | ------------- | ---------------- | --- |
|                            |     | userprivilege | anduserprivilege |     |
Transmittingconfidentialorproprietarydata
SendSensitiveInformation Sendtime,filetype,anduserprivilege 8
throughvariouscommunicationchannels
Unauthorizedorsuspiciousinsertionof
externalstoragedevices,suchasUSBthumb
AttemptedThumbDriveInsertion Inserttime,devicetype,andlocation 10
drives,intocomputersystemsornetwork
devices
Printingdocumentswithoutadequate
Printtime,documenttype,location,and
| SecurePrinting | safeguardstoprotecttheconfidentialityand |     |     | 6   |
| -------------- | ---------------------------------------- | --- | --- | --- |
userprivilege
integrityoftheprintedinformation
Weights were assigned to each anomalous activity type based on its severity. To
ensureameaningfulandmanageablescaleforassessingtherelativeriskassociatedwith
different types of anomalous activities, weights were assigned on a scale from 4 to 10.
Higher weights were assigned to activities with a greater potential impact on security,
ensuringthatthesystemeffectivelyreflectsorganizationalpriorities.Forexample,previous
incidentsofsecurityviolationswereassignedaweightof10,assuchincidentsstrongly
suggest severe abnormal behavior. In contrast, logging in outside business hours was

FutureInternet2025,17,93 10of26
assignedalowerweightof4.Whilethisbehaviormayraiseconcerns,itoftenhaslegitimate
explanations, such as remote work or urgent deadlines, and as such is considered less
criticalinisolation. Thisweightassignmentschemeenablesthesystemtomoreeffectively
identifyconcerningbehavioralpatterns. Anemployeelogginginoutsidebusinesshours
andvisitingnon-workwebsitesmightstillbeclassifiedaslowriskduetotherelatively
benignnatureoftheseactivities. However,ifthesameemployeeinsertedanunauthorized
thumbdrivealongwithvisitingnon-workwebsites,thecombinedweightoftheseactivities
wouldelevatetheiroverallriskscoretomedium,indicatinganeedforimmediateactionby
thecybersecurityteam.
Theseweightsweredeterminedbyourexpertise,andcanbeadjustedtomeetorgani-
zationalneeds. Eachactivityconsistsofseveralfeaturesthatdeterminewhethertheactivity
isanomalous. AdescriptionofthesefeaturesisshowninTable2,andtheencodedfeatures’
valuesareshowninTable3. Thepurposeofthefeaturesistocreatepatternsofemployee
behaviorinordertoprovideapatternfortheMLratherthanrelyingonpredefinedrules.
Thefeaturesweredeterminedbasedondomainknowledge.
Table3.Listofencodedvalues.
Variable EncodedValues
LoginTime WorkingHours(0),Non-WorkingHours(1)
LoginLocation Office(0),Remote(1)
DeviceType Desktop(0),Laptop(1),Mobile(2)
AccessTime WorkingHours(0),Non-WorkingHours(1)
AccessLocation Office(0),Remote(1)
UserPrivilege Normal(0),Admin(1)
FileType Document(0),Media(1),Executable(2)
InstallationTime WorkingHours(0),Non-WorkingHours(1)
UserPermission Normal(0),Admin(1)
Location Office(0),Remote(1)
TransferTime WorkingHours(0),Non-WorkingHours(1)
FileSize Small(0),Medium(1),Large(2)
Destination Internal(0),ExternalTrusted(1),ExternalUntrusted(2)
VisitTime WorkingHours(0),Non-WorkingHours(1)
WebsiteCategory SocialMedia(0),Shopping(1),News(2),Gaming(3)
EntryTime WorkingHours(0),Non-WorkingHours(1)
LocationAccessed Office(0),Remote(1)
BadgeType Visitor(0),Employee(1),Contractor(2)
AttackType Phishing(0),Baiting(1),Pretexting(2)
ResponseTime WorkingHours(0),Non-WorkingHours(1)
Sensitivity NoResponse(0),MinimalDisclosure(1),SensitiveDisclosure(2)
IncidentType LowRisk(0),MediumRisk(1),HighRisk(2)
UserInvolvement None(0),Indirect(1),Direct(2)
IncidentSeverity Low(0),Medium(1),High(2)

FutureInternet2025,17,93
11of26
Table3.Cont.
| Variable        |                                          | EncodedValues |     |
| --------------- | ---------------------------------------- | ------------- | --- |
| SharingTime     | WorkingHours(0),Non-WorkingHours(1)      |               |     |
| InformationType | Personal(0),Professional(1),Sensitive(2) |               |     |
PlatformLocation Internal(0),ExternalPublic(1),ExternalPrivate(2)
| InteractionTime | WorkingHours(0),Non-WorkingHours(1)        |     |     |
| --------------- | ------------------------------------------ | --- | --- |
| MaliciousFlag   | NotMalicious(0),Malicious(1)               |     |     |
| UserReaction    | None(0),Minimal(1),Full(2)                 |     |     |
| ChangeType      | Behavioral(0),Habitual(1),Sudden(2)        |     |     |
| TimeofChange    | WorkingHours(0),Non-WorkingHours(1)        |     |     |
| UserMotivation  | WorkRelated(0),Personal(1),Suspicious(2)   |     |     |
| ProtocolType    | HTTP(0),HTTPS(1),FTP(2),SMTP(3)            |     |     |
| UserAwareness   | FullyAware(0),PartiallyAware(1),Unaware(2) |     |     |
PracticeType WeakPasswords(0),SharingCredentials(1),LackofUpdates(2)
| Severity         | Low(0),Medium(1),High(2)                |     |     |
| ---------------- | --------------------------------------- | --- | --- |
| UploadTime       | WorkingHours(0),Non-WorkingHours(1)     |     |     |
| EncryptionStatus | NotEncrypted(0),Encrypted(1)            |     |     |
| SendTime         | WorkingHours(0),Non-WorkingHours(1)     |     |     |
| InsertTime       | WorkingHours(0),Non-WorkingHours(1)     |     |     |
| PrintTime        | WorkingHours(0),Non-WorkingHours(1)     |     |     |
| DocumentType     | Personal(0),Official(1),Confidential(2) |     |     |
TheprocessforgeneratingthisdatasetisoutlinedinAlgorithm1.
Algorithm1DataGeneration
InitializeFakerobjectfordatageneration
Setnumberofemployees,n_employees=500
Initializedatastructure:
data←{Name,Emails,SSN,DoB,EmpID,
Behaviors,Features}
foreach employee from 1 to
n_employeesdo
| GenerateandassignrandomName, | Email Address, | SSN, DoB, | and Emp ID |
| ---------------------------- | -------------- | --------- | ---------- |
endfor
Initializeanomalousbehaviorweights:
anomalous_weights←{
LoginAttempts:4,
SensitiveFilesAccess:7,
UnauthorizedSoftware:9,
DataTransfer:6,
NonWorkWebsitesVisited:5,
PhysicalAccess:8,
SocialEngineeringAttacks:8,
PreviousIncidents:10,
PublicInfoShared:5,
InteractionWithMaliciousAccounts:8,
BehaviorChange:6,
NetworkInteraction:7,

FutureInternet2025,17,93 12of26
Algorithm1Cont.
PoorInfoSecPractices:9,
UploadSensitiveInformation:8,
SendSensitiveInformation:8,
AttemptedThumbDriveInsertion:10,
SecurePrinting:6}
Addfeaturesforeachanomalousbehaviorandassignvalues:
foreach feature in anomalous_weightsdo
Assignvaluestofeaturesbasedonpre-definedbehaviorcriteria
endfor
Generatefeaturevalues:
foreach feature and corresponding weight in anomalous_weightsdo
Assignbinaryvalue(0or1)tofeatureforeachemployee,basedonthecorrespondingfeature
values
endfor
InitializeRiskScoreto0foreachemployee
return Data with synthesized employee details and features
4.2. FeatureEngineering
VersionJanuary23,2025submittedtoFutureInternet 12of6
Toenhanceriskassessment,weintroducedacompositeRiskScorefeaturecalculated
usingEquation(1),whichincorporatesbothactivityfrequencyandriskweight. Thescore
4.2.FeatureEngineering 285
isbasedonthefirstoccurrenceofanabnormalactivitymultipliedbythecorresponding
Toenhanceriskassessment,weintroducedacompositefeature,RiskScore,calculated
286
usingEquation(1),whichinaccotrivpoitryat’esswboethigahctti.viUtysfererqsuaernecythanednrilsakbweleeigdhta.cTchoersdcoinreg to their RiskScore as low risk (0–10),
287
isbasedonthefirstoccurremnceedoifuamnarbinsokrm(1a0l–ac2t5iv)i,tyo,rmhuiltgiphlierdisbky(tahbeocovrere2sp5o).ndTinhgese288thresholds are designed to detect
activity’sweight. Usersarreistkhyenulasbeerlsedatacecoarrdlyingsttaogtehse.irORirskgSacnoriez:aLtoiownrsiscka(n0-1m0)o,di2f89y these ranges according to their
Mediumrisk(10-25),andHighrisk(above25). Thesethresholdsaredesignedtodetect
specificrequirements. 290
riskyusersatearlystages;however,organizationscanmodifytheserangesaccordingto
291
theirspecificrequirements.
4.3. DataValidation 292
4.3.DataValidation Ensuringdataqualityandreliabilityisessential. W293eperformedseveralpreprocessing
Ensuringdataqualityasntedprselitaobiclilteyainsetshseendtiaalt.aW,wepheircfohrmareedislelvuesrtarlaptreedprionceFssiignugre2394andsummarizedasfollows:
stepstocleanthedata,summarizedasfollowsandillustratedinFigure3
295
Start
LoadRawData
HandleMissingValues
(Imputewith1)
DetectandTreatOutliers
(Adjustto1ifoutside{0,1})
AddressDatasetImbalance
(ApplySMOTEENN)
CleanedData
ReadyforAnalysis
End
Figure3.DataCleaningandPreprocessingWorkflow
Figure3.Datacleaningandpreprocessingworkflow.
1. HandlingMissingValues:Missingvalueswereimputedwith1,aligningwiththe
296
goalofdetectingthefirstinstanceofanomalousactivity.Thisconservativeapproach
297
minimizestheriskoffalsenegativesbyassumingthatmissingvaluesmayindicate
298
potentialanomalousactivity.
299
2. OutlierDetectionandTreatment: Frequencyvaluesoutsidethe{0,1}rangewere 300
adjustedto1,treatingtheseanomaliesasindicatorsofpotentiallyriskybehavior.Our
301
datasetdidnotexhibitoutliersoutsidethisrange.
302
3. AddressingDatasetImbalance:WeemployedtheSyntheticMinorityOver-sampling
303
TechniquecombinedwithEditedNearestNeighbors(SMOTEENN)tobalancethe
304
representationacrossanomalousbehaviors,whichiscrucialforeffectivemodeltrain-
305
ing.
306
TheprocessfordatavalidationisshowninAlgorithm2.
307

FutureInternet2025,17,93 13of26
1. HandlingMissingValues: Missingvalueswereimputedas1,aligningwiththegoal
of detecting the first instance of anomalous activity. This conservative approach
minimizestheriskoffalsenegativesbyassumingthatmissingvaluesmayindicate
potentialanomalousactivities.
2. Outlier Detection and Treatment: Frequency values outside the {0, 1} range were
adjustedto1,treatingtheseanomaliesasindicatorsofpotentiallyriskybehavior. Our
datasetdidnotexhibitoutliersoutsidethisrange.
3. AddressingDatasetImbalance: WeemployedtheSyntheticMinorityOversampling
TechniquecombinedwithEditedNearestNeighbors(SMOTEENN)tobalancetherep-
resentationacrossanomalousbehaviors,whichiscrucialforeffectivemodeltraining.
TheprocessfordatavalidationisshowninAlgorithm2.
Algorithm2DataValidation
1: Define feature columns as features related to different abnormal behaviors
2: featureCols←{Features of different abnormal behaviors}
3: Define target columns representing the anomalous behaviors
4: targetCols←{All anomalous behavior indicators}
5: Initialize SMOTEENN resampling
6: smote_enn←SMOTEENN()
7: Balancedataforeachanomalousbehavior:
8: foreach targetCol in targetColsdo
9: X_resampled, y_resampled ← smote_enn.fit_resample(data[featureCols],
data[targetCol])
10: Update data with resampled X and y for current targetCol
11: endfor
12: HandlingMissingValues:
13: Impute missing values with 1 across resampled dataset
14: This conservative imputation treats missing values as potential indicators of
anomalous activity
15: OutlierDetectionandTreatment:
16: foreach feature in featureColsdo
17: Check if values are outside the range {0, 1}
18: If a value is outside the range, set it to 1 to indicate potentially risky
behavior
19: endfor
20:
21: return Resampled, imputed, and outlier-adjusted dataset
4.4. DataPrivacy
Toensuretheethicaluseofdataandaddressprivacyconcerns,weimplementedthe
followingmeasures:
1. PseudonymizedAlerts:Usersremainpseudonymizedduringthealertandmonitoring
phase, allowing for risk assessment without revealing sensitive information (see
Figure2).
2. ControlledAccessforDe-anonymization: Whencorrectiveactionisnecessary,full
identificationisrestrictedtoauthorizedpersonnel,maintainingprivacyuntilinterven-
tionisrequired.
5. ToolValidation
Thissectionevaluatestheproposedtoolusingreal-timesimulationstotesttheexperi-
mentalsetupandprocessaswellasacomparisonwithdifferentMLmodelsintermsof
differentmetricsforassessingperformance. Finally,itexaminesdetectionandclassification
timestodemonstratethetool’sreal-timecapabilities.

FutureInternet2025,17,93 14of26
5.1. Real-TimeSimulation
Totesttheabilityoftheproposedtooltodetect,analyze,andclassifyemployeerisk
levelsinrealtime,asimulatorwascreatedwiththefollowingcomponents:
1. ThesystemusedforthisresearchwasaWindows11Pro64-bitHPlaptopequipped
withanIntel(R)Core(TM)i5-10210UCPUandoperatingatabasespeedof1.60GHz
withamaximumclockspeedof2.11GHz. Thelaptopfeatured8GBofRAManda
64-bitoperatingsystemrunningonanx64-basedprocessor. Thisconfigurationwas
sufficientforconductingtheexperimentsinthisstudy.
2. ThelaptopwasequippedwithIntel(R)UHDGraphicsprovidedbyIntelCorporation,
featuring an internal DAC type. It offered a total memory of 4147 MB, including
128MBofdedicatedVRAM.Thedisplayoperatedataresolutionof1366×768with
32-bitcolordepthanda60Hzrefreshrate.
3. Anacondawasutilizedastheprimaryenvironmentmanagertoenabletheinstalla-
tionandmanagementoftherequiredPythonlibraries. Pythonservedasthemain
programming language, with key libraries such as Pandas and NumPy used for
datamanipulation,Scikit-learnforimplementingMLmodels(RandomForest,Logis-
ticRegression,andSVM),andXGBoostforadvancedgradientboosting. TheFaker
librarywasemployedtogeneratesyntheticemployeedatasuchasnames,emails,and
behaviorstosimulatevariousanomalousactivities.
4. FlaskwasusedtosetupaRESTAPIforsimulatingtheinjectionofemployeebehaviors.
POSTMANwastheAPItestingplatformusedtoinjectbehaviorsintothesimulation
andretrieveresults.
Thesimulationinvolvedpushingthedatasetintothesystemtoevaluatehowdifferent
MLalgorithmsdetectandclassifyemployeesbasedonanomalousbehaviors.
Algorithm3showsthereal-timemonitoringandabnormalitydetectionprocess. The
simulation begins by capturing ongoing activities as the system remains active. The
algorithmcontinuouslygathersreal-timedatafromtheadjusteddatasetandupdatesa
monitoringdashboardwiththelatestactivities. Afterthedatahavebeencollected, the
algorithmsplitsthemintotraining,validation,andtestingsetsina70:15:15ratio. Itthen
initializesandtrainstheRF,LR,XGBoost,andSVMmachinelearningmodelsusingthe
trainingdataset.
Aseachactivityisrecorded,thealgorithmevaluatesitagainsteachtrainedmodelto
detectanyabnormalbehavior. Ifananomalyisidentified,thesystemlogstheincidentfor
furtherinvestigation,notifiesthesecurityteam,andgeneratesanalertcontainingcritical
informationsuchastheemployee’sname,ID,behaviortype,andtimeofoccurrence. This
alertisthensenttothecybersecurityteamforimmediateaction. Thealgorithmultimately
returnsalistofidentifiedabnormalactivities,demonstratingtheeffectivenessofreal-time
detectioninmonitoringmultipleemployeessimultaneously. Thisproactiveapproachaims
tomitigatepotentialanomalousbehaviorsbyidentifyingandaddressinganyirregularities
in employee behavior during the simulation. The time taken to detect the anomalous
behavioriscalculatedduringthisstep.
Algorithm4outlinestheprocessforcalculatingtheriskscorebasedoninstancesof
abnormal behaviors. Depending on their calculated risk score, users are classified into
oneofthreemainriskcategories: low,medium,orhigh. Additionally,eachuserprofileis
dynamicallyadjustedinresponsetoanyfutureabnormalactivities,ensuringthattherisk
classificationsremaincurrentandreflectiveofusers’behavior. Thetimetakentocalculate
theriskscoreandclassifyusersiscalculatedduringthisstep.

FutureInternet2025,17,93 15of26
Algorithm5outlinestheprocessfornotifyingadministrationaboutemployeesidenti-
fiedasmoderateorhighriskbasedontheiranomalousbehaviors. Thealgorithmcreates
detailednotificationsthatincludetheemployee’sname,ID,risklevel,abnormalbehaviors,
andtimeofoccurrence. Afternotificationsaresent,thealgorithminitiatesacontinuous
monitoringprocessthatcapturesnewreal-timedatafromtheorganization’snetwork. This
ensuresongoingadaptationandsecuritymaintenance, allowingthesystemtorespond
promptlytoanyemergingrisks.
Algorithm3ContinuousActivities,Identification,andAlert
1: Initialize data structure to capture real-time activities
2: whilesystem is activedo
3: Capture real-time data from the adjusted dataset
4: Append captured data to data structure
5: Update monitoring dashboard with latest activities
6: endwhile
7:
8: return Captured activities data
9: activitiesData←Call ContinuousMonitoring(adjustedDataset)
10: Split activitiesData into training, validation, and test sets with 70-15-15
ratio
11: trainingData, validationData, testData←split(activitiesData, 0.7, 0.15, 0.15)
12: behaviorTypes←Identify distinct abnormal behavior types in activitiesData
13: foreach behaviorType in behaviorTypesdo
14: correspondingFeatures←Extract features specific to behaviorType
15: models←Initialize [RF, LR, XGBoost, SVM]
16: foreach model in modelsdo
17: Fit model using correspondingFeatures
18: model.fit(trainingData[
correspondingFeatures])
19: endfor
20: endfor
21: foreach activity in activitiesDatado
22: foreach behaviorType in behaviorTypesdo
23: correspondingFeatures←Extract features specific to behaviorType
24: foreach model in modelsdo
25: prediction←model.predict(activity[
correspondingFeatures])
26: ifprediction indicates abnormalitythen
27: Log abnormal activity for further analysis
28: Notify security team about abnormal activity
29: Generate alert with details:
30: alert ← Create alert with employee name, ID, behavior type, and time of
occurrence
31: Send alert to cybersecurity team
32: Calculate the detection time
33: endif
34: endfor
35: endfor
36: endfor
37:
38: return List of identified abnormal activities

FutureInternet2025,17,93 16of26
Algorithm4EmployeeRiskClassificationandDynamicProfiling
1: Input:Employeeactivitiesdata
2: foreach employee in activitiesDatado
3: riskScore←0
4: foreach feature in featuresdo
5: iffeature value for employee is 1then
6: riskScore←riskScore+Weight[feature]
7: AddGaussiannoisetoRiskScoretosimulatevariability
8: endif
9: endfor
10: employee[’riskScore’]←riskScore
11: endfor
12: foreach employee in activitiesDatado
13: Update employee profile with latest behaviors and riskScore
14: endfor
15: foreach employee in activitiesDatado
16: ifriskScorelessthanlowThresholdthen
17: employee[’riskLabel’]←low
18: elseifriskScorelessthanmediumThresholdthen
19: employee[’riskLabel’]←moderate
20: else
21: employee[’riskLabel’]←high
22: Calculate the scoring and classification time
23: endif
24: endfor
25:
26: return Updated employee profiles with riskScores and riskLabels
Algorithm5AdministrationNotificationandRecurrence
1: Initialize data structure for notifications
2: foreach employee in activitiesDatado
3: ifemployee[’RiskLabel’]isModerateorHighthen
4: notification←Create notification with details:
5: notification[’Employee Name’]←employee[’Name’]
6: notification[’Employee ID’]←employee[’ID’]
7: notification[’Risk Level’]←employee[’RiskLabel’]
8: notification[’Abnormal Behaviors’]←Get abnormal behaviors for employee
9: notification[’Time of Occurrence’]←Get time of occurrence
10: Send notification to administration
11: endif
12: endfor
13: Log notifications for review
14: Return notifications sent to administration
15: Reinitialize monitoring process
16: whilesystem is activedo
17: Capture new real-time data from the organization’s network
18: Append captured data to activitiesData
19: Update monitoring dashboard with latest activities
20: endwhile
5.2. MLModels
Aspartoftheevaluationprocess,severalMLmodelswereselectedinordertoassess
theirabilitytodetectanomalousbehaviorandclassifyuserriskbasedontheirbehavior.
Themodelswechosearewell-suitedforclassificationtasksandhaveshowneffectivenessin
cybersecuritydomains,especiallywhendealingwithlargedatasetsandmultiplefeatures.
Thefollowingmodelswereevaluated:
1. RandomForest(RF):Arobustensemblelearningmethodthatbuildsmultipledecision
treesandaggregatestheirresults. RFwellsuitedforthissystemduetoitsabilityto

FutureInternet2025,17,93 17of26
handlelargedatasetswithamixtureoffeaturestypesanditsstrengthinestimating
featureimportance.
2. XGBoost: SimilartoRF,XGBoostisanensemblemethod;however,itusesagradient
boostingframeworkinwhichitbuildstreessequentiallytoimprovemodelaccuracy.
Itisknownforitshighperformance,speed,andabilitytohandlecomplexpatterns,
whichiscrucialforaccuratelyclassifyinguserrisk.
3. SupportVectorMachine(SVM):Apowerfulmodelforclassificationproblems,par-
ticularly when data points are not linearly separable, SVM works well in high-
dimensional spaces, making it effective for identifying risky behavior based on a
varietyofinputfeatures.
4. LogisticRegression(LR):Aninterpretablemodelthatprovidesclearprobabilitiesfor
classification. Givenitssimplicityandeaseofimplementation, itservesasagood
baselineforcomparisonwithmorecomplexmodelssuchasRFandXGBoost.
5.3. EvaluationMetrics
To assess the performance of the ML models, we employed several key metrics,
including the accuracy, precision, recall, F1-score, and confusion matrix. Each of these
metricsprovidesinsightintodifferentaspectsofamodel’sclassificationability.
Accuracyisageneralmeasureofhowwellthemodelclassifiesallinstances,definedas
theratioofcorrectlypredictedcases(truepositivesandtruenegatives)tothetotalnumber
ofpredictions. Mathematically,accuracycanbeexpressedasfollows:
TP+TN
Accuracy=
TP+TN+FP+FN
whereTPdenotestruepositives, TN denotestruenegatives, FPdenotesfalsepositives,
andFNdenotesfalsenegatives.
Precisionfocusesonthereliabilityofpositivepredictions,measuringtheproportion
oftruepositivesamongallpredictedpositives. Thismetricisparticularlyimportantwhen
thecostoffalsepositivesishigh. Precisionisprovidedby
TP
Precision= .
TP+FP
Recall,alsoknownassensitivity,quantifiesamodel’sabilitytocaptureallrelevant
instanceswithinaparticularclass.Itistheratiooftruepositivestothesumoftruepositives
andfalsenegatives,andcanbeformulatedasfollows:
TP
Recall= .
TP+FN
TheF1-scorebalancesprecisionandrecallbycomputingtheirharmonicmean,offering
asinglemetricthatconsidersbothfalsepositivesandfalsenegatives. Thisisparticularly
usefulwhenthereisanunevenclassdistribution. TheF1-scoreisrepresentedasfollows:
Precision×Recall
F1-Score=2×
Precision+Recall
Finally,theconfusionmatrixprovidesacomprehensiveviewofamodel’sperformance
by displaying the average distribution of true positives, false positives, true negatives,
andfalsenegativesacrossallanomalousbehaviors. Thismatrixenablesamoregranular
understandingofthemodel’sbehaviorindetectingdifferentbehaviors.
5.4. MLResults
Inthisstudy,thedatasetwasdividedintotraining(70%),validation(15%),andtesting
(15%) sets to ensure robust model evaluation, prevent overfitting, and provide reliable

FutureInternet2025,17,93 18of26
results. Thetrainingset,comprising70%ofthedata,wasallocatedalargerproportionto
ensurethatthemachinelearningmodelshadsufficientdatatoeffectivelylearnpatternsand
relationships. Alargetrainingsetiscrucialformodelstogeneralizewelltounseendata,as
itallowsthemtocapturecomplexbehaviorsandreducesthelikelihoodofunderfitting.
Thevalidationset,accountingfor15%ofthedata,wasusedtotunethemodelparam-
etersandselectthebest-performingmodelduringthetrainingprocess. Thisproportion
strikesabalancebetweenhavingsufficientdataforreliableparameteroptimizationand
retainingaseparateportionfortesting. Importantly,thevalidationsethelpstoprevent
overfittingbyensuringthatthemodel’sperformanceisevaluatedondatathatarenotdi-
rectlyusedfortraining,providinganearlyindicationofhowwellthemodelcangeneralize
tonewdata.
The test set, also accounting for 15%, was reserved exclusively for evaluating the
model’s final performance on unseen data. This percentage provides a sufficient sam-
plesizetoobtainstatisticallysignificantresultsandensuresareliableassessmentofthe
model’sgeneralizationability. Usingequalproportionsforvalidationandtestingmain-
tainsconsistencyandavoidsskewedevaluations,asbothsetsarederivedfromthesame
datadistribution.
WeevaluatedtheperformanceoffourMLmodels(LR,RF,XGBoost,andSVM)using
keyevaluationmetrics,includingtheaccuracy,precision,recall,andF1-score. Table4and
Figure4presenttheaveragedetectionperformanceofthesemodels. Figure5illustratesthe
models’confusionmatrices.
Figure4.PerformanceresultsforthedifferentMLmodels.
Precision,ameasureoftheproportionoftruepositivesamongallpositivepredictions,
wassimilarlyhighacrossallmodels. XGBachievedaperfectprecisionscoreof1.00,while
LRandSVMfollowedcloselywithscoresof0.996andRFachievedascoreof0.986. These
results reflect the models’ reliability in minimizing false positives when predicting the
positiveclass.
Recall,whichquantifiestheabilityofamodeltoidentifyalltruepositiveinstances,
paralleledtheprecisionresults. XGBandSVMbothachievedperfectrecallof1.00,whereas
LRandRFscoredslightlylowerat0.996and0.986,respectively. Thisdemonstratesthatthe
modelswereequallyadeptatminimizingfalsenegatives.
TheF1-scores,whichbalanceprecisionandrecall,alsounderscorethemodels’robust
performance. XGBandSVMachievedperfectscoresof1.00,indicatinganoptimaltradeoff
betweenprecisionandrecall. LRandRF,withF1-scoresof0.996and0.986,respectively,
demonstratedslightlylowerbutstillexcellentperformance.

FutureInternet2025,17,93
19of26
(a) (b)
(c) (d)
Figure5.Confusionmatricesforthedifferentmodels:(a)RandomForest(RF),(b)LogisticRegression
(LR),(c)XGBoost,(d)SupportVectorMachine(SVM).
Table4.Modelperformance.
|           | Logistic       | RandomForest |         | SupportVector |
| --------- | -------------- | ------------ | ------- | ------------- |
| Metric    |                |              | XGBoost |               |
|           | Regression(LR) | (RF)         |         | Machine(SVM)  |
| Accuracy  | 0.99           | 0.99         | 1.00    | 0.99          |
| Precision | 0.996          | 0.986        | 1.00    | 0.996         |
| Recall    | 0.996          | 0.986        | 1.00    | 0.996         |
| F1-score  | 0.996          | 0.986        | 1.00    | 1.00          |
Table 5 quantitatively compares the proposed tool with recently developed tools
discussedinSection2whichutilizethesameMLalgorithms. Comparingtheseresultswith
previousstudies,ourimplementationsofLR,XGBoost,andSVMnotablyoutperformed
the benchmarks in terms of classification accuracy and precision [38,55,60]. RF scored
similarlytoexistingresults,whileXGBconsistentlyachievedsuperiorperformanceacross
allmetrics. Becauseourproposedtoolworkswithonlinedatainsteadofrelyingonstatic
offlinedata,webelievethatourapproachcanalsoenhancesimilarmodelsproposedin
otherstudies[63–66].
Given the uniformly high performance of the models, selecting which one to use
fordeploymentmaydependonfactorssuchascomputationalefficiency,interpretability,

FutureInternet2025,17,93
20of26
and application-specific requirements. For example, the simplicity and interpretability
ofLRmakeitasuitablechoicewhenmodeltransparencyiscrucial. Conversely,XGB’s
unmatchedaccuracymakesitidealforhigh-stakesenvironmentswherepredictiveprecision
isparamount.
Table5.Quantitativecomparisonwithrecentstudies,includingdetectionandclassificationtimes
(N/D:NotDiscussed).
| Study      |                  | LogisticRegression(LR)    |              |                   | StudyDate |
| ---------- | ---------------- | ------------------------- | ------------ | ----------------- | --------- |
| Accuracy   | Recall Precision | F1-Score                  | Detection(s) | Classification(s) |           |
| [32] 0.97  | 0.97             | 0.98 0.97                 | N/D          | N/D               | 2021      |
| [38] 0.93  | 0.961            | 0.912 0.936               | N/D          | N/D               | 2024      |
| [39] 0.90  | 0.25             | 0.24 0.24                 | N/D          | N/D               | 2023      |
| [55] 0.913 | 0.91             | 0.91 0.90                 | N/D          | N/D               | 2020      |
| [56] 0.80  | 0.86             | 0.81 0.83                 | N/D          | N/D               | 2020      |
| [59] 0.70  | N/D              | 0.90 0.54                 | N/D          | N/D               | 2021      |
| [60] 0.946 | 0.973            | 0.969 0.971               | N/D          | N/D               | 2022      |
| Ours 0.99  | 0.996            | 0.996 0.996               | 0.014        | 0.071             | N/A       |
| Study      |                  | RandomForest(RF)          |              |                   |           |
| [32] 0.99  | 0.99             | 0.99 0.99                 | N/D          | N/D               | 2021      |
| [38] 0.993 | 0.996            | 0.992 0.994               | N/D          | N/D               | 2024      |
| [39] 0.99  | 0.97             | 0.97 0.97                 | N/D          | N/D               | 2023      |
| [55] 0.996 | 1.00             | 1.00 1.00                 | N/D          | N/D               | 2020      |
| [56] 0.83  | 0.91             | 0.81 0.86                 | N/D          | N/D               | 2020      |
| [59] 0.87  | N/D              | 0.98 0.84                 | N/D          | N/D               | 2021      |
| [60] N/D   | N/D              | N/D N/D                   | N/D          | N/D               | 2022      |
| Ours 0.99  | 0.986            | 0.986 0.986               | 0.15         | 0.34              | N/A       |
| Study      |                  | XGBoost                   |              |                   |           |
| [32] N/D   | N/D              | N/D N/D                   | N/D          | N/D               | 2021      |
| [38] 0.993 | 0.995            | 0.992 0.994               | N/D          | N/D               | 2024      |
| [39] N/D   | N/D              | N/D N/D                   | N/D          | N/D               | 2023      |
| [55] 0.992 | 0.99             | 0.99 0.99                 | N/D          | N/D               | 2020      |
| [56] N/D   | N/D              | N/D N/D                   | N/D          | N/D               | 2020      |
| [59] N/D   | N/D              | N/D N/D                   | N/D          | N/D               | 2021      |
| [60] 0.999 | 0.999            | 0.999 0.999               | N/D          | N/D               | 2022      |
| Ours 1.00  | 1.00             | 1.00 1.00                 | 0.056        | 0.102             | N/A       |
| Study      |                  | SupportVectorMachine(SVM) |              |                   |           |
| [32] 0.97  | 0.97             | 0.98 0.98                 | N/D          | N/D               | 2021      |
| [38] 0.969 | 0.982            | 0.96 0.971                | N/D          | N/D               | 2024      |
| [39] 0.70  | 0.14             | 0.14 0.14                 | N/D          | N/D               | 2023      |
| [55] 0.874 | 0.87             | 0.76 0.82                 | N/D          | N/D               | 2020      |
| [56] 0.84  | 0.86             | 0.87 0.87                 | N/D          | N/D               | 2020      |
| [59] N/D   | N/D              | N/D N/D                   | N/D          | N/D               | 2021      |
| [60] 0.786 | 0.896            | 0.722 0.80                | N/D          | N/D               | 2022      |
| Ours 0.99  | 0.996            | 0.996 1.00                | 0.046        | 0.1051            | N/A       |
5.5. DetectionandClassificationTimeEvaluation
Thisexperimentevaluatedtheaveragedetectionandclassificationtimesofthepro-
posedtoolusingfourMLalgorithms: LR,RF,XGBoost,andSVM.Thesemetricshighlight

FutureInternet2025,17,93 21of26
thetool’sreal-timecapabilityanditssuitabilityforcontinuousmonitoringanddynamic
profilinginhigh-securityenvironments.
5.5.1. DetectionTime
Detection time refers to the time required by the system to identify anomalies in
employee activities, and is recorded based on the steps in Algorithm 3. This metric is
crucialforensuringtimelyinterventionsandmitigatingpotentialrisks. Table6presents
theaveragedetectiontimesforthedifferentalgorithms.
Table6.Averagedetectionandclassificationtime.
Logistic RandomForest SupportVector
Metric XGBoost
Regression(LR) (RF) Machine(SVM)
Detection(s) 0.014 0.15 0.056 0.046
Classification(s) 0.071 0.34 0.102 0.1051
5.5.2. ClassificationTime
Theclassificationtimerepresentsthetimerequiredtoassignariskscoretoemployees
based on identified anomalies, as described in Algorithm 4, which outlines the steps
involvedincalculatingandassigningtheriskscores. Efficientclassificationensuresthat
high-riskemployeesarepromptlyflaggedforadministrativereview. Theresultsareshown
inTable6andFigure6.
Figure6.Detectionandclassificationtimes.
AscanbeseeninTable6, theexperimentalresultsdemonstratethatXGBoostwas
themostefficientamongthetestedmodelsintermsofbothdetectionandclassification
times,affirmingitssuitabilityforreal-timeapplications. Inthecontextofdetectinginsider
abnormalbehavior,XGBoost’ssuperiorperformancecanlikelybeattributedtoitsabilityto
effectivelycapturecomplexpatternsandrelationshipswithinuseractivitydata. XGBoost
leverages ensemble learning, combining multiple decision trees to improve predictive
accuracy. Furthermore,itemploysgradientboosting,wheresubsequenttreesaretrained
tocorrecttheerrorsofpreviousones,leadingtoamorerobustandaccuratemodel. This
combinationoftechniquesallowsXGBoosttoidentifysubtleandcomplexpatternsinuser
activitydatathatmayindicatemaliciousintent,makingitapowerfultoolforinsiderthreat
detection. Thesefindingsunderscoretheproposedtool’spotentialforproactiveanomaly
detectionandriskassessmentinorganizationalenvironments.

FutureInternet2025,17,93 22of26
6. Conclusions
Thispaperunderscoresthecriticalroleofreal-timethreatdetectionandclassification
systemsinmitigatinginsiderthreats,apersistentchallengeinorganizationalcybersecurity.
ByleveragingML,theproposedtooldynamicallycategorizesemployeebehaviorsinto
low,medium,andhighlevelsofrisk,therebyenhancingorganizationalresilienceagainst
maliciousactivities. SimulationtestingoftheproposedtoolconductedusingthePostman
APIplatformeffectivelydemonstratedthesystem’sabilitytodetectanomalousactions,cal-
culateriskscores,andclassifyusersbasedontheirbehaviors.Amongtheevaluatedmodels,
XGBoostemergedasthemosteffective,achievingsuperioraccuracyandexcellinginthe
identificationofmaliciousbehaviors. Theseresultsvalidatetheproposedtool’spotential
asarobustsolutionforreal-timedecision-makingandproactivethreatmanagement.
Thecontributionsofthisworkhighlightseveralkeyadvancements.First,theproposed
toolintroducesamachinelearningsystemthatcontinuouslymonitorsemployeeactivities
inreal-time,enablingtherapiddetectionofinsiderthreats. Italsoimplementsdynamic
userprofiling,classifyingindividualsintooneofthreeriskcategoriesbasedontheirbehav-
ior,ensuringaccurateidentificationofriskyusers. Thetoolfurtherautomatesimmediate
alertgeneration,reducingresponsetimesbynotifyingcybersecurityteamspromptlywhen
abnormalactivitiesaredetected. Byoperatingasafullyautomatednon-interactivesystem,
iteliminatestheneedformanualintervention,therebyenhancingefficiency. Moreover,the
toolprovidescustomizableconfigurations,allowingorganizationstoadjustparameters
suchasfeatureweightsandriskthresholdsinordertomeetspecificsecurityneeds. Ulti-
mately,bycombiningreal-timedetectionanduserclassificationintoaunifiedsolution,the
proposedtooladdressestheshortcomingsoftraditionalsystemsthatlackthesecapabilities.
OurfindingsemphasizethetransformativeimpactofMLinautomatinginsiderthreat
detection,enablingsecurityteamstofocusonhigher-prioritytaskswhilereducingresponse
times. Moreover, the proposed tool’s design and real-time analytics provide a scalable
frameworkthatcanbetailoredtovariousorganizationalcontexts,includingcriticalsectors
suchashealthcare, finance, andgovernment. Inhealthcare, forinstance, wherepatient
dataprivacyandregulatorycompliancearecrucial,ourtoolcanbecustomizedtoidentify
behaviorsthatmaysuggestnegligenceorlapsesinsecuritypractices,suchasimproper
accesstoconfidentialdata. Infinance,ourtoolcandetectbehaviorsindicativeofcareless
handling of sensitive financial information or violations of internal policies, ensuring
compliancewithregulations. Similarly,ingovernmentsettingswheresensitiveinformation
andpublictrustareatstake,theproposedsystemcanbescaledtomonitoremployeeactions
inordertoidentifyrisksarisingfromcarelessnessorviolationsofconduct.Thisadaptability
ensuresthattheproposedtoolcanbeeffectivelyintegratedintodiverseorganizational
frameworks,providingacomprehensivesolutionthataddressesbothsector-specificrisks
andbroaderorganizationalchallenges.
Despiteitsstrengths,thisstudyprimarilyreliedonsyntheticdataduetothelimited
availabilityofreal-worlddatasets. Whileeffectiveforinitialdevelopment,syntheticdata
maynotfullycapturethecomplexitiesofreal-worldscenariosandabnormalemployee
behaviors.Furthermore,thispaper’sfocusontechnicalindicatorsmaynotfullyaccountfor
psychologicalandcontextualfactorssuchasstresslevelsthatcaninfluenceabnormalem-
ployeebehavior. Futureresearchshouldaimtoincorporatereal-worlddataandintegrate
humanfactorsforamorecomprehensiveandaccurateassessmentofabnormalbehavior.
For instance, data such as the number of emails, projects, phone calls, or approaching
deadlinescouldbeusedtomeasurestresslevelsinemployees,whichmayinturn,helpto
explaincertainanomalousbehaviors. Additionally,factorssuchasjobsatisfactionlevels
couldprovidevaluableinsightsintowhyanemployeeisengaginginspecificbehaviors,
suchasattemptingtoaccesssensitivefiles. Byconsideringthesepsychologicalandcontex-

FutureInternet2025,17,93 23of26
tualelements,thesystemcouldofferamorenuancedunderstandingofemployeebehavior,
helpingittodistinguishbetweengenuinesecurityrisksandactionsdrivenbyexternal
pressuresordissatisfaction.
Future research should explore federated learning or decentralized data sharing
approachesasameanstopreserveprivacywhileleveragingreal-worlddataforanalysis.
Federatedlearningenablesorganizationstotrainmodelslocally,sharingonlyaggregated
updates rather than sensitive raw data, thereby maintaining confidentiality. Similarly,
decentralized data sharing techniques that rely on anonymized or partially processed
datasetscanhelptoensureprivacy. Collaboratingwithindustrypartnerstoaccesssuch
anonymizeddatasetswouldenhancetheseeffortsbyprovidingadiverseandrepresentative
poolofreal-worlddata. Thiscollaborationwouldensurethatthesystembenefitsfrom
practicalreal-worldscenarioswhilemaintainingtheethicalstandardsrequiredforhandling
sensitiveemployeeinformation.
Expandingtheproposedtool’sscalabilityandinteroperabilitywithexistingsecurity
systems,suchasSIEMplatformsoridentitymanagementtools,couldincreaseitsadoption
in real-world scenarios. To integrate our tool with current cybersecurity setups, this
wouldinvolveestablishingcommunicationchannelsbetweenthetoolandSIEMsystems
to share relevant employee activity data such as login attempts and access logs. This
wouldallowthetooltoleveragereal-timedatastreamsfromtheSIEMplatformstomore
accuratelydetectandclassifyanomalousbehaviors. Additionally,integrationwithidentity
management software could enable the tool to assess access patterns, user roles, and
permissions, improving its ability to identify risky behavior based on unauthorized or
abnormal access attempts. Such integration would ensure that the tool complements
existingcybersecurityinfrastructureandenhancesoverallthreatdetectioncapabilities.
Finally,theproposedtoolprovidesasignificantstepforwardinaddressinginsider
threats, offering an innovative and practical approach that bridges the gaps in existing
methods. Thisresearchpavesthewayformoreeffective,scalable,andinterdisciplinary
solutions,helpingtoensureenhancedsecurityinanincreasinglycomplexdigitallandscape.
AuthorContributions: Conceptualization, S.A.-D.Q.andA.A.S.A.; methodology, S.A.-D.Q.and
A.A.S.A.;software,S.A.-D.Q.andA.A.S.A.;validation,S.A.-D.Q.andA.A.S.A.;formalanalysis,S.A.-
D.Q.andA.A.S.A.;resources,S.A.-D.Q.andA.A.S.A.;datacuration,S.A.-D.Q.;writing—originaldraft
preparation,A.A.S.A.;writing—reviewandediting,S.A.-D.Q.;visualization,S.A.-D.Q.;supervision,
A.A.S.A.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
DataAvailabilityStatement:Thedatasetpresentedinthisstudyisavailableonrequest.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
References
1. Verizon. 2024DataBreachInvestigationsReport; TechnicalReport;Verizon:NewYork,NY,USA,2024.
2. IBM. CostofaDataBreachReport2024; TechnicalReport;IBM:Armonk,NY,USA,2024.
3. Le,D.C.;Zincir-Heywood,N. Exploringanomalousbehaviourdetectionandclassificationforinsiderthreatidentification. Int.J.
Netw.Manag.2021,31,e2109.[CrossRef]
4. Al-Shehari,T.;Rosaci,D.;Al-Razgan,M.;Alfakih,T.;Kadrie,M.;Afzal,H.;Nawaz,R. EnhancingInsiderThreatDetectionin
ImbalancedCybersecuritySettingsUsingtheDensity-BasedLocalOutlierFactorAlgorithm. IEEEAccess2024,12,34820–34834.
[CrossRef]
5. Neupane,S.;Ables,J.;Anderson,W.;Mittal,S.;Rahimi,S.;Banicescu,I.;Seale,M. Explainableintrusiondetectionsystems(x-ids):
Asurveyofcurrentmethods,challenges,andopportunities. IEEEAccess2022,10,112392–112415.[CrossRef]
6. Hajj,S.;ElSibai,R.;BouAbdo,J.;Demerjian,J.;Makhoul,A.;Guyeux,C. Anomaly-basedintrusiondetectionsystems: The
requirements,methods,measurements,anddatasets. Trans.Emerg.Telecommun.Technol.2021,32,e4240.[CrossRef]

FutureInternet2025,17,93 24of26
7. Ozkan-Okay,M.;Samet,R.;Aslan,Ö.;Gupta,D. Acomprehensivesystematicliteraturereviewonintrusiondetectionsystems.
IEEEAccess2021,9,157727–157760.[CrossRef]
8. Chaabouni,N.; Mosbah,M.; Zemmari,A.; Sauvignac,C.; Faruki,P. NetworkintrusiondetectionforIoTsecuritybasedon
learningtechniques. IEEECommun.Surv.Tutorials2019,21,2671–2701.[CrossRef]
9. Khraisat,A.;Gondal,I.;Vamplew,P.;Kamruzzaman,J.Surveyofintrusiondetectionsystems:Techniques,datasetsandchallenges.
Cybersecurity2019,2,1–22.[CrossRef]
10. Chandel,S.;Yu,S.;Yitian,T.;Zhili,Z.;Yusheng,H. Endpointprotection:Measuringtheeffectivenessofremediationtechnologies
and methodologies for insider threat. In Proceedings of the 2019 International Conference on Cyber-Enabled Distributed
ComputingandKnowledgeDiscovery(Cyberc),Guilin,China,17–19October2019;pp.81–89.
11. Zargar,A.;Nowroozi,A.;Jalili,R. XABA:Azero-knowledgeanomaly-basedbehavioralanalysismethodtodetectinsiderthreats.
InProceedingsofthe201613thInternationalIranianSocietyofCryptologyConferenceonInformationSecurityandCryptology
(ISCISC),Tehran,Iran,7–8September2016;pp.26–31.
12. Fujii,S.;Kurima,I.;Isobe,Y. ScoringMethodforDetectingPotentialInsiderThreatbasedonSuspiciousUserBehaviorusing
EndpointLogs. InProceedingsoftheInternationalConferenceonArtificialIntelligence(ICAI).TheSteeringCommitteeofThe
WorldCongressinComputerScience,ComputerEngineeringandAppliedComputing(WorldComp),LasVegas,NV,USA,29
July–1August2019;pp.291–297.
13. Pramudya,P.B.;Alamsyah,A. Implementationofsignature-basedintrusiondetectionsystemusingSNORTtopreventthreatsin
networkservers. J.SoftComput.Explor.2022,3,93–98.
14. Díaz-Verdejo, J.; Muñoz-Calle, J.; Estepa Alonso, A.; Estepa Alonso, R.; Madinabeitia, G. On the detection capabilities of
signature-basedintrusiondetectionsystemsinthecontextofwebattacks. Appl.Sci.2022,12,852.[CrossRef]
15. Asad, H.; Adhikari, S.; Gashi, I. Aperspective–retrospectiveanalysisofdiversityinsignature-basedopen-sourcenetwork
intrusiondetectionsystems. Int.J.Inf.Secur.2023,23,1331–1346[CrossRef]
16. Gupta, A.; Sharma, L.S. Performance evaluation of snort and Suricata intrusion detection systems on ubuntu server. In
ProceedingsoftheICRIC2019:RecentInnovationsinComputing,Jammu,India,9March2019;Springer:Berlin/Heidelberg,
Germany,2020;pp.811–821.
17. Kumar,A.;Tanwar,A.;Malhotra,V. Acomparativeanalysisofdifferentintrusiondetectionsystems. Int.Res.J.Mod.Eng.Technol.
Sci.2023,5,34–45.
18. Guo,Y. AreviewofMachineLearning-basedzero-dayattackdetection:Challengesandfuturedirections. Comput.Commun.
2023,198,175–185.[CrossRef][PubMed]
19. Singh,U.K.;Joshi,C.;Kanellopoulos,D. Aframeworkforzero-dayvulnerabilitiesdetectionandprioritization. J.Inf.Secur.Appl.
2019,46,164–172.[CrossRef]
20. Alsharabi,N.;Alqunun,M.;Murshed,B.A.H. DetectingUnusualActivitiesinLocalNetworkUsingSnortandWiresharkTools. J.
Adv.Inf.Technol.2023,14,616–624.[CrossRef]
21. Legg,P.A.;Buckley,O.;Goldsmith,M.;Creese,S. Caughtintheactofaninsiderattack: Detectionandassessmentofinsider
threat. InProceedingsofthe2015IEEEInternationalSymposiumonTechnologiesforHomelandSecurity(HST),Waltham,MA,
USA,14–16April2015;pp.1–6. [CrossRef]
22. Legg,P.;Buckley,O.;Goldsmith,M.;Creese,S. AutomatedInsiderThreatDetectionSystemUsingUserandRole-BasedProfile
Assessment. IEEESyst.J.2017,11,503–512. [CrossRef]
23. Joshi,C.;Aliaga,J.R.;Insua,D.R. InsiderThreatModeling:AnAdversarialRiskAnalysisApproach. IEEETrans.Inf.Forensics
Secur.2021,16,1131–1142. [CrossRef]
24. RiosInsua,D.;Couce-Vieira,A.;Rubio,J.A.;Pieters,W.;Labunets,K.;Rasines,D.G. Anadversarialriskanalysisframeworkfor
cybersecurity. RiskAnal.2021,41,16–36.[CrossRef]
25. Kaushik,K. Asystematicapproachtodevelopanadvancedinsiderattacksdetectionmodule. J.Eng. Appl. Sci. 2021,8,33.
[CrossRef]
26. Mehnaz,S.;Bertino,E. AFine-GrainedApproachforAnomalyDetectioninFileSystemAccessesWithEnhancedTemporalUser
Profiles. IEEETrans.DependableSecur.Comput.2021,18,2535–2550. [CrossRef]
27. Pham,N.;Guo,J.;Wang,Z.AbnormalityDetectioninNetworkTrafficbyClassificationandGraphDataAnalysis. InProceedings
ofthe2022IEEE13thAnnualInformationTechnology,ElectronicsandMobileCommunicationConference(IEMCON),Vancouver,
BC,Canada,12–15October2022;pp.0041–0047. [CrossRef]
28. Teymourlouei,H.; Harris,V.E. PreventingDataBreaches: UtilizingLogAnalysisandMachineLearningforInsiderAttack
Detection. InProceedingsofthe2022InternationalConferenceonComputationalScienceandComputationalIntelligence(CSCI),
LasVegas,NV,USA,14–16December2022;pp.1022–1027. [CrossRef]
29. Abdulhammed,R.;Faezipour,M.;Abuzneid,A.;AbuMallouh,A. Deepandmachinelearningapproachesforanomaly-based
intrusiondetectionofimbalancednetworktraffic. IEEESens.Lett.2018,3,7101404.[CrossRef]

FutureInternet2025,17,93 25of26
30. Le,D.C.;Zincir-Heywood,A.N. Evaluatinginsiderthreatdetectionworkflowusingsupervisedandunsupervisedlearning. In
Proceedingsofthe2018IEEESecurityandPrivacyWorkshops(SPW),SanFrancisco,CA,USA,24May2018;pp.270–275.
31. Park,H.;Kim,K.;Shin,D.;Shin,D. BGPDataset-BasedMaliciousUserActivityDetectionUsingMachineLearning. Information
2023,14,501.[CrossRef]
32. Alshamy,R.;Ghurab,M.;Othman,S.;Alshami,F. IntrusiondetectionmodelforimbalanceddatasetusingSMOTEandrandom
forestalgorithm. InAdvancesinCyberSecuritymProceedingsoftheThirdInternationalConference,ACeS2021,Penang,
Malaysia,24–25August2021;RevisedSelectedPapers3;Springer:Berlin/Heidelberg,Germany,2021;pp.361–378.
33. Padmavathi,G.;Shanmugapriya,D.;Asha,S. Aframeworktodetectthemaliciousinsiderthreatincloudenvironmentusing
supervisedlearningmethods. InProceedingsofthe20229thInternationalConferenceonComputingforSustainableGlobal
Development(INDIACom),NewDelhi,India,23–25March2022;pp.354–358.
34. Le,D.C.;Zincir-Heywood,N. AnomalyDetectionforInsiderThreatsUsingUnsupervisedEnsembles. IEEETrans.Netw.Serv.
Manag.2021,18,1152–1164. [CrossRef]
35. Ahmadi-Assalemi, G.; Al-Khateeb, H.; Epiphaniou, G.; Aggoun, A. Super Learner Ensemble for Anomaly Detection and
Cyber-RiskQuantificationinIndustrialControlSystems. IEEEInternetThingsJ.2022,9,13279–13297. [CrossRef]
36. Diop,A.;Emad,N.;Winter,T.;Hilia,M. Designofanensemblelearningbehavioranomalydetectionframework. Int.J.Comput.
Inf.Eng.2019,13,547–555.
37. Yi,J.;Tian,Y. InsiderThreatDetectionModelEnhancementUsingHybridAlgorithmsbetweenUnsupervisedandSupervised
Learning. Electronics2024,13,973.[CrossRef]
38. Alshuaibi,F.;Alshamsi,F.;Saeed,A.;Kaddoura,S. MachineLearning-BasedClassificationApproachforNetworkIntrusion
DetectionSystem. InProceedingsofthe202415thAnnualUndergraduateResearchConferenceonAppliedComputing(URC),
Dubai,UnitedArabEmirates,24–25April2024;pp.1–6.
39. AlLail,M.;Garcia,A.;Olivo,S. Machinelearningfornetworkintrusiondetection—Acomparativestudy. FutureInternet2023,
15,243.[CrossRef]
40. Nikiforova, O.; Romanovs, A.; Zabiniako, V.; Kornienko, J. DetectingandIdentifyingInsiderThreatsBasedonAdvanced
ClusteringMethods. IEEEAccess2024,12,30242–30253. [CrossRef]
41. Mehmood,M.;Amin,R.;Muslam,M.M.A.;Xie,J.;Aldabbas,H. PrivilegeEscalationAttackDetectionandMitigationinCloud
UsingMachineLearning. IEEEAccess2023,11,46561–46576. [CrossRef]
42. Nandini,K.;Girisha,G.;Reddy,S. CGBA:AEfficientInsiderAttackerDetectionTechniqueinMachineLearning. InProceedings
ofthe2024InternationalConferenceonAdvancesinComputing,CommunicationandAppliedInformatics(ACCAI),Chennai,
India,9–10May2024;pp.1–8.
43. Li,Y.;Su,Y. TheInsiderThreatDetectionMethodofUniversityWebsiteClustersBasedonMachineLearning. InProceedings
ofthe20236thInternationalConferenceonArtificialIntelligenceandBigData(ICAIBD),Chengdu,China,26–29May2023;
pp.560–565. [CrossRef]
44. Suresh,P.V.;Madhavu,M.L. Insiderattack:Internalcyberattackdetectionusingmachinelearning. InProceedingsofthe2021
12thInternationalConferenceonComputingCommunicationandNetworkingTechnologies(ICCCNT),Kharagpur,India,6–8
July2021;pp.1–7.
45. Peccatiello,R.B.;Gondim,J.J.C.;Garcia,L.P.F. ApplyingOne-ClassAlgorithmsforDataStream-BasedInsiderThreatDetection.
IEEEAccess2023,11,70560–70573. [CrossRef]
46. Böse,B.;Avasarala,B.;Tirthapura,S.;Chung,Y.Y.;Steiner,D. DetectingInsiderThreatsUsingRADISH:ASystemforReal-Time
AnomalyDetectioninHeterogeneousDataStreams. IEEESyst.J.2017,11,471–482. [CrossRef]
47. Verma,A.;Ranga,V. StatisticalanalysisofCIDDS-001datasetforNetworkIntrusionDetectionSystemsusingDistance-based
MachineLearning. ProcediaComput.Sci.2018,125,709–716. [CrossRef]
48. Zhang,F.;Kodituwakku,H.A.D.E.;Hines,J.W.;Coble,J. MultilayerData-DrivenCyber-AttackDetectionSystemforIndustrial
ControlSystemsBasedonNetwork,System,andProcessData. IEEETrans.Ind.Inform.2019,15,4362–4369. [CrossRef]
49. Begli,M.;Derakhshan,F.;Karimipour,H. Alayeredintrusiondetectionsystemforcriticalinfrastructureusingmachinelearning.
InProceedingsofthe2019IEEE7thInternationalConferenceonSmartEnergyGridEngineering(SEGE),Oshawa,ON,Canada,
12–14August2019;pp.120–124.
50. Kim,J.;Park,M.;Kim,H.;Cho,S.;Kang,P. Insiderthreatdetectionbasedonuserbehaviormodelingandanomalydetection
algorithms. Appl.Sci.2019,9,4018.[CrossRef]
51. Le,D.C.;Zincir-Heywood,N.;Heywood,M.I. AnalyzingDataGranularityLevelsforInsiderThreatDetectionUsingMachine
Learning. IEEETrans.Netw.Serv.Manag.2020,17,30–44. [CrossRef]
52. Khan,A.Y.;Latif,R.;Latif,S.;Tahir,S.;Batool,G.;Saba,T. MaliciousInsiderAttackDetectioninIoTsUsingDataAnalytics. IEEE
Access2020,8,11743–11753. [CrossRef]
53. Zou,S.;Sun,H.;Xu,G.;Quan,R. EnsembleStrategyforInsiderThreatDetectionfromUserActivityLogs. Comput.Mater.Contin.
2020,65,1321–1334. [CrossRef]

FutureInternet2025,17,93 26of26
54. Janjua,F.;Masood,A.;Abbas,H.;Rashid,I. Handlinginsiderthreatthroughsupervisedmachinelearningtechniques. Procedia
Comput.Sci.2020,177,64–71.[CrossRef]
55. Shaver,A.;Liu,Z.;Thapa,N.;Roy,K.;Gokaraju,B.;Yuan,X. Anomalybasedintrusiondetectionforiotwithmachinelearning.
InProceedingsofthe2020IEEEAppliedImageryPatternRecognitionWorkshop(AIPR),Washington,DC,USA,13–15October
2020;pp.1–6.
56. Abhale,A.B.;Manivannan,S. Supervisedmachinelearningclassificationalgorithmicapproachforfindinganomalytypeof
intrusiondetectioninwirelesssensornetwork. Opt.Mem.NeuralNetw.2020,29,244–256.[CrossRef]
57. Oliveira,N.;Praça,I.;Maia,E.;Sousa,O. IntelligentCyberAttackDetectionandClassificationforNetwork-BasedIntrusion
DetectionSystems. Appl.Sci.2021,11,1674. [CrossRef]
58. Al-Shehari,T.;Alsowail,R.A. Aninsiderdataleakagedetectionusingone-hotencoding,syntheticminorityoversamplingand
machinelearningtechniques. Entropy2021,23,1258.[CrossRef]
59. Almomani,O.;Almaiah,M.A.;Alsaaidah,A.;Smadi,S.;Mohammad,A.H.;Althunibat,A. Machinelearningclassifiersfor
networkintrusiondetectionsystem:Comparativestudy. InProceedingsofthe2021InternationalConferenceonInformation
Technology(ICIT),Amman,Jordan,14–15July2021;pp.440–445.
60. Taghavirashidizadeh, A.; Zavvar, M.; Moghadaspour, M.; Jafari, M.; Garoosi, H.; Zavvar, M.H. AnomalyDetectionInIoT
NetworksUsingHybridMethodBasedOnPCA-XGBoost. InProceedingsofthe20228thIranianConferenceonSignalProcessing
andIntelligentSystems(ICSPIS),Behshahr,Iran,28–29December2022;pp.1–5.
61. Manoharan,P.; Yin,J.; Wang,H.; Zhang,Y.; Ye,W. Insiderthreatdetectionusingsupervisedmachinelearningalgorithms.
Telecommun.Syst.2023,87,899–915.[CrossRef]
62. Inuwa,M.M.;Das,R. AcomparativeanalysisofvariousmachinelearningmethodsforanomalydetectionincyberattacksonIoT
networks. InternetThings2024,26,101162.[CrossRef]
63. Faysal,J.A.;Mostafa,S.T.;Tamanna,J.S.;Mumenin,K.M.;Arifin,M.M.;Awal,M.A.;Shome,A.;Mostafa,S.S. XGB-RF:Ahybrid
machinelearningapproachforIoTintrusiondetection. Telecom2022,3,52–69.[CrossRef]
64. Oyelakin,A.M. ALearningApproachforTheIdentificationofNetworkIntrusionsBasedonEnsembleXGBoostClassifier.
Indones.J.DataSci.2023,4,190–197.[CrossRef]
65. Khan,N.;Mohmand,M.I.;Rehman,S.u.;Ullah,Z.;Khan,Z.;Boulila,W. Advancementsinintrusiondetection:Alightweight
hybridRNN-RFmodel. PLoSONE2024,19,e0299666.[CrossRef]
66. Onyebueke,A.E.;David,A.A.;Munu,S. NetworkIntrusionDetectionSystemUsingXGBoostandRandomForestAlgorithms.
AsianJ.PureAppl.Math.2023,5,321–335.
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.