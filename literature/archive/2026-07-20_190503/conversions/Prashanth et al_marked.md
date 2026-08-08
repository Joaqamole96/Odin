Received15September2025,accepted29September2025,
dateofpublication6October2025,dateofcurrentversion10October2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3616776
| Adaptive      | Buffering              | Strategies                  |                            | for Incremental |     |     |     |
| ------------- | ---------------------- | --------------------------- | -------------------------- | --------------- | --- | --- | --- |
| Learning      | Under                  | Concept                     | Drift                      | in Lifestyle    |     |     |     |
| Disease       | Modeling               |                             |                            |                 |     |     |     |
| B.S.PRASHANTH | 1,2,M.V.MANOJKUMAR     |                             | 1,2,3,(SeniorMember,IEEE), |                 |     |     |     |
| B.H.PUNEETHA  | 4,(SeniorMember,IEEE), |                             |                            |                 |     |     |     |
|               |                        | 5,(Member,IEEE),ARIFULHOQUE |                            |                 | 6,  |     |     |
NASSERABDOSAIFALMURAQAB
| IMMANUELAZAADMOONESAR |     | 3,ANDANANTHRAO |     | 3,7 |     |     |     |
| --------------------- | --- | -------------- | --- | --- | --- | --- | --- |
1DepartmentofInformationScienceandEngineering,NitteMeenakshiInstituteofTechnology(NMIT),Nitte(DeemedtobeUniversity),
Bengaluru560064,India
2VisvesvarayaTechnologicalUniversity,Belagavi590018,India
3MohammedBinRashidSchoolofGovernment,Dubai,UnitedArabEmirates
4DepartmentofComputerScienceandBusinessSystems,BapujiInstituteofEngineeringandTechnology,Davanagere,Karnataka577004,India
5InformationSystemsDepartment,DubaiBusinessSchool,UniversityofDubai,Dubai,UnitedArabEmirates
6MurdochUniversity,Murdoch,WA6150,Australia
7DubaiBusinessSchool,UniversityofDubai,Dubai,UnitedArabEmirates
Correspondingauthor:M.V.ManojKumar(manoj.kumar@nmit.ac.in)
ThisworkwassupportedbytheNitteMeenakshiInstituteofTechnology(NMIT),Nitte(DeemedtobeUniversity),Bengaluru,India.
ABSTRACT Lifestylediseasessuchasdiabetesmanifestthroughsubtleandnon-stationaryclinicalpatterns,
posingsignificantchallengesforreal-timepredictionandmonitoring.Conventionalmachinelearningmodels
often struggle to maintain performance under evolving data distributions due to concept drift. This study
proposesanadaptivedeeplearningframeworkdesignedtohandleconceptdriftthroughincrementallearning
in clinical data streams. The investigation centers on evaluating the effectiveness of various buffering
strategiesnamely,adaptivebuffering,FIFObuffering,andstreamingwithoutbufferingcombinedwithdrift
detection mechanisms for healthcare prediction. A balanced clinical dataset exhibiting evolving patterns
wasusedtobenchmarkmodelperformance.Deeplearningarchitectures,includingBiLSTM,GRU,LSTM,
andBayesianNeuralNetworkswereincrementallytrained,andtheirdrift(Abrupt,GradualandRecurring)
responsiveness was assessed using three categories of detectors: 1) statistical test-based, 2) error-rate-
based,and3)uncertainty-basedapproachesleveragingMonteCarloDropout.Resultsindicatedthatadaptive
buffering strategies consistently outperformed FIFO and no-buffer strategies, yielding higher accuracy,
precision,andrecall,especiallyunderabruptandlargedriftmagnitudes.Thehybriddriftdetectionmethod,
combined with Bi-LSTM, demonstrated the best performance in maintaining retention and minimizing
forgetting, even as the drift magnitude increased. Additionally, the drift magnitude study highlighted that
largerdriftshadasignificantimpactonmodelperformance,withadaptivebufferinganduncertainty-based
driftdetectionprovingtobemoreresilienttohighdriftintensities.Thisresearchunderscorestheimportance
ofcombiningrobustdriftdetectionmethodsandadaptivebufferingstrategiestoenhancetherobustnessof
modelsdealingwithconceptdriftinreal-worldapplications.
INDEXTERMS Adaptivebuffer,Bayesianneuralnetwork(BNN),bi-directionalLSTM(BiLSTM),centers
for disease control and prevention (CDC), concept drift detection and adaptation, first in first out (FIFO),
gated recurrent unit (GRU), incremental learning, long-short term memory (LSTM), national health and
nutritionexaminationsurvey(NHANES),uncertaintyestimation.
I. INTRODUCTION
| The associate editor                   | coordinating | the review of | this manuscript and |            |                    |                        |          |
| -------------------------------------- | ------------ | ------------- | ------------------- | ---------- | ------------------ | ---------------------- | -------- |
|                                        |              |               |                     | Over the   | past decade, there | has been a significant | shift in |
| approvingitforpublicationwasMu-YenChen |              | .             |                     |            |                    |                        |          |
|                                        |              |               |                     | the global | health landscape,  | with communicable      | diseases |

2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME13,2025 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 174001

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
giving way to non-communicable diseases (NCDs) that are Asaresultofitslongitudinalrichnessandmethodological
becoming increasingly prevalent as a result of lifestyle integrity,theNHANESisconsideredtobethegoldstandard
choices. According to the World Health Organization [1], forepidemiologicalandpredictivemodeling.Itcapturesreal-
non-communicable diseases are responsible for the deaths world patterns that span many years over a wide range of
ofaround41millionpeopleeachyear,whichcontributesto racial,ethnic,andsocioeconomicstrata,whichisakeyaspect
74% of all deaths that occur worldwide. When it comes to of researching the temporal evolution of risk factors for
these,theworldwidemortalityburdenisdominatedbymalig- chronicdiseases[3].
nancies, chronic respiratory illnesses (4.1 million), diabetes It is suitable for feature selection, deep learning,
(1.5 million), and cardiovascular diseases (17.9 million). and population-wide insights, and the NHANES offers
Several of these disorders have their origins in lifestyle researchersinmachinelearningaone-of-a-kindopportunity
variablesthatcanbealtered,suchasunhealthyeatinghabits, to model dynamic health hazards by utilizing thousands
a lack of physical activity, the use of tobacco products, the of characteristics. Because of its cross-cycle comparability,
abuse of alcohol, chronic stress, and sleep cycles that are it also makes it easier to research idea drift and adaptive
interrupted. learning.Inthesetypesofstudies,modelsthatweretrainedon
Emerging economies and cultures that are in the process earliercyclesarevalidatedonsubsequentcyclestoevaluate
of transitioning are experiencing an even more complicated theirgeneralizability.
burden. There are a number of factors that contribute to
lifestyledisruptionsthatappearaschronicmetabolicorvas-
B. THEROLEOFARTIFICIALINTELLIGENCEINTHE
culardisorders[2].Thesefactorsincludemigrationfromrural
TRANSITIONFROMGENERALIZEDRISKTO
to urban areas, fast industrialization, changing sociocultural
PERSONALIZEDPREDICTION
norms, and the combined hazards of under-nutrition and
Regression-based tools, such as the Framingham Risk
obesity. As a result of increased urbanization, even those
Score for cardiovascular diseases and the ADA (American
thathavehistoricallybeenconsideredtobeatalowriskare
Diabetes Association) risk test for diabetes, have been
experiencinganincreaseintheincidenceratesofdiabetesand
utilized extensively in traditional public health models for
hypertension.
the purpose of risk prediction. When it comes to offering
Inaddition,chronicdiseasesarenotmerelyclinicalissues
individualized,real-timeinsightsthattakeintoconsideration
butalsosignificanteconomicdisruptorwithincommunities,
the complex interconnections between variables such as
contributingtorisingdependencyratios,diminishedproduc-
age, ethnicity, comorbidities, behavior, and environmental
tivity,andincreasedfinancialstrainonbothhouseholdsand
exposure, these models are excellent at capturing average
healthcaresystems.Addressingthesechallengesnecessitates
trends; nevertheless, they fall short when it comes to
a paradigm shift toward proactive, personalized public
providingpersonalizedinsights.
healthapproachesfocusedonpreventionandearlydetection.
A new dimension has been introduced here by the
This section contextualizes the broader problem of lifestyle
application of AI and ML. The goal of machine learning
diseases,examinesthelimitationsofapplyingstaticmachine
algorithms is to discover non-linear relationships, manage
learning models to evolving health data, introduces the
high-dimensionaldata,andcontinuouslyimprovewithfresh
concept of concept drift, underscores the role of adaptive
inputs. Some examples of these algorithms are random
buffering techniques, and positions the study’s contribution
forests,supportvectormachines,gradientboosting,anddeep
within the wider pursuit of continuous and individualized
neural networks. Studies have demonstrated that machine
healthprediction—drawingfromrepresentativeclinicaldata
learning-based models perform better than traditional sta-
sourceswhereapplicable.
tistical techniques when it comes to predicting illnesses
such as diabetes, hypertension, stroke, and chronic kidney
disease when they are trained on big datasets such as the
A. THENATIONALHEALTHANDNUTRITION
NHANES[4],[5].
EXAMINATIONSURVEY(NHANES)ASTANDARDFOR
AImodelshavethepotentialtoadjustandcustomizerisk
MONITORINGTHEHEALTHOFTHEPOPULATION
estimates for specific patients, which is the primary advan-
One of the most extensive datasets for lifestyle and health
tage of using these algorithms. Using such models, doctors
behavior analytics is provided by the NHANES, which
andpublichealthofficialscaneffectivelyfocusinterventions
was first conducted in the early 1960s and has undergone
becausetheyareabletoincorporatepatient-specificfeatures
continuous development ever since. Structured interviews,
inreal-timethatprovideprecisionhealthtools.However,this
clinical evaluations, and laboratory investigations are the
capability comes with a catch: the majority of models that
methodsthatareutilizedbytheNHANES,whichiscarried
are currently available are static. They make the premise
out by the CDC of the United States of America. The
that there is a stable relationship between the inputs and
scopeofthisstudyencompassessocio-demographicfactors,
the outputs, an assumption that is becoming increasingly
anthropometricmeasurements,foodintake,physicalactivity,
problematicinthisdayandageofdynamichealthdata.
mentalhealth,medicationuse,andbiomarkersofdisease.
174002 VOLUME13,2025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
C. CONCEPTDRIFT:AHIDDENCHALLENGEINCHRONIC • No Buffer: This is the quickest but most forgetful
DISEASEMODELLING strategy;itjustupdatesthemodelwiththemostrecent
It is a problem that is inherent in health data due to batch
shiftingpopulationhabits,environmentalconditions,medical • First-in, first-out (FIFO) Buffer: This buffer keeps a
advancements, or policy changes [6]. Concept drift arises stationarywindowofrecentdata,whichfreesupsome
when the statistical correlations between predictors and RAM
outcomes experience a change over time. It is possible, for • AdaptiveBuffer:whichstoresonlythedriftedanomalies
instance, that a diabetes risk model that was established in forretraining
2010willnotfunctioneffectivelyin2025duetochangesin Indicatorssuchasuncertainty,driftmagnitude,orerrorrates
theaveragebodymassindex(BMI),dietarypatterns,physical are used to determine which data should be retained by the
activity,orevennewdiagnosticthresholdsputoutbyclinical adaptivebuffer.
recommendations. The detailed explanation of concept drift Adaptivebuffersmakeitpossibletobeflexibleinresponse
isdiscussedinsectionIII. tochangesinthehealthcareindustry,wheresomealterations
InlongitudinalandstreamingdatasetsliketheNHANES, are gradual (for example, dietary patterns) and others are
these alterations are not anomalies but typical behavior. abrupt (for example, pandemic effects). A sudden increase
The failure to take them into consideration results in the infastingglucoseisnoticedacrossallpatients;forexample,
degradationofthemodelovertime,areductioninaccuracy, themodelcanpreserverelevantbatchesandupdateweights
and the possibility of misclassification, which is especially accordingly, thus preserving accuracy without the need for
hazardousinclinicalsettings. constantfullretrainingeverytime.
InNHANES-basedmodeling,sinceeachcyclebringsnew
D. INCREMENTALLEARNING:TOWARDCONTINUAL sampling methods, variables, and social contexts, this is
ADAPTATION of greater significance than in other modeling approaches.
Incrementallearninghasdevelopedasafundamentalmethod The model can maintain its clinical validity and contextual
inthefieldofmachinelearningasameansofovercomingthe relevanceovertimeduetoadaptivebuffering.
limits of static models. In contrast to batch learning, which
necessitates doing a complete retraining of the model with F. ATESTBEDFORCONCEPTDRIFT
all of the data, incremental learning involves continuously Whenitcomestotheresearchofideadrift,thereareveryfew
updating the model with new data as it becomes available. datasetsthatareassuitableasNHANES.Itoffersaone-of-
Inthefieldofhealthcare,thisisespeciallyusefulinsituations a-kindplatformequippedwithcyclesthatspandecadesand
where data is collected over time, such as in the case of thousandsoffeatures,allowingusersto,
electronic health records (EHRs), wearable devices, mobile • Simulate non-stationary situations by comparing older
applications,orpublicsurveillanceapplications.Tomaintain cyclestomorerecentcycles
performance and scalability, incremental models can inte- • Evaluate the performance of artificial intelligence in
gratedevelopingtrendssuchasnewdiseasevariants,seasonal population-widediseasesurveillance
effects,orbehavioralshifts[7].Incrementalmodelscanalso • Explorebuffer-basedmodeladaptation
incorporatenoveldiseasevariations.Whenappliedtochronic • Benchmark drift detection techniques using real-world
diseases,incrementallearningenablesthefollowing: data
• Real-time,explainableforecastsfordecisionsupport Furthermore, the NHANES incorporates a wide range of
• Scalabilitytonewpopulationsorgeographicalareas subgroups on the basis of age, gender, ethnicity, education,
• Reducedcomputationalcostsincomparisontocompre- and income, which enables researchers to explore drift
hensiveretraining heterogeneity across populations. It is important to make
• Timelyupdateswhilepatientprofilesareevolving surethatmodelsdonotperpetuateprejudicesorinaccuracies
Despite this, the effectiveness of incremental learning is among underrepresented populations, which is in line with
contingent on successful data memory management, which theincreasedemphasisonhealthequity[8].
involvesfiguringouthowtokeeprelevantpreviousdatawhile
gettingridofnoiseandredundantinformation. G. RESEARCHOBJECTIVESANDSTUDYCONTRIBUTION
In light of this, the following are the objectives of the
E. ADAPTIVEBUFFERINGMEMORYMANAGEMENTFOR presentedresearch:
SMARTLEARNING 1) Create and test incremental learning algorithms that
Adaptive buffering is a system that saves a subset of arecapableofadjustingtonon-stationaryclinicaldata
historical data in order to guide model updates. This gets distributions
us to the concept of adjustable buffering. Imagine it as a 2) To develop and evaluate memory-efficient buffering
dynamicmemorybankthatassiststhemodelinremembering solutions (No Buffer, FIFO, and Adaptive Buffer)
pertinent information and forgetting irrelevant information. that strike a balance between learning plasticity and
Thefollowingaresomeexamplesofbufferingstrategies: maintainingstability
VOLUME13,2025 174003

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
3) Todemonstratetheefficacyofadaptivemodelupdating have been incorporated into the healthcare industry, which
in enhancing the early diagnosis of lifestyle-related has resulted in the opening of new doors for the prediction
diseasesandthecontinuousmonitoringsuchdiseases and management of these disorders. Providing complete
4) Toprovideaframeworkthatisscalableforproducing health and nutritional data that is typical of the population
real-time, drift-aware personalized health modeling of the United States. The purpose of this literature review
thathasclinicalandpublichealthapplications. is to investigate recent developments in machine learning
Not only does this study contribute to the creation of andartificialintelligenceapplicationsforpredictingchronic
algorithms, but it also contributes to the use of translational disease risk. The review focuses on works that have been
artificial intelligence in the healthcare industry. It provides publishedinScopusQ1journalssince2024.
| useful workflows, |     | evaluation |     | metrics, |     | and insights | for |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
incorporatingadaptivelearningintosurveillancesystems.
A. MACHINELEARNINGAPPLICATIONSINCHRONIC
| The mind | map | of the | presented |     | work, | which | will give a |     |     |     |     |     |     |     |
| -------- | --- | ------ | --------- | --- | ----- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
DISEASEPREDICTION
graphicaloverview,isshowninFigure1.Toguidethereader
1) HYPERTENSIONPREDICTION
throughthepresentedstudy,theremainderofthemanuscript
Topredicthypertension,[13]builtamodelbasedonmachine
| is structured | as         | follows.    | Section      | II        | reviews      | key       | literature |            |              |         |               |            |           |             |
| ------------- | ---------- | ----------- | ------------ | --------- | ------------ | --------- | ---------- | ---------- | ------------ | ------- | ------------- | ---------- | --------- | ----------- |
|               |            |             |              |           |              |           |            | learning   | by assessing |         | environmental | chemical   |           | exposures   |
| on concept    | drift,     | incremental |              | learning, | and          | buffering | mech-      |            |              |         |               |            |           |             |
|               |            |             |              |           |              |           |            | using data | from         | 2003    | to 2016.      | In order   | to handle | missing     |
| anisms in     | healthcare |             | and related  | domains.  |              | Section   | III and    |            |              |         |               |            |           |             |
|               |            |             |              |           |              |           |            | data, the  | study        | applied | multiple      | imputation |           | approaches. |
| section IV    | introduce  | the         | mathematical |           | formulations |           | under-     |            |              |         |               |            |           |             |
Additionally,thisstudyutilizedavarietyofmachinelearning
| pinning    | concept         | drift  | and        | incremental |         | model         | adaptation, |               |          |             |               |            |                  |             |
| ---------- | --------------- | ------ | ---------- | ----------- | ------- | ------------- | ----------- | ------------- | -------- | ----------- | ------------- | ---------- | ---------------- | ----------- |
|            |                 |        |            |             |         |               |             | algorithms    | in order | to evaluate |               | the impact | of environmental |             |
| providing  | the theoretical |        | foundation |             | for     | understanding | the         |               |          |             |               |            |                  |             |
|            |                 |        |            |             |         |               |             | chemicals     | on the   | risk of     | hypertension. | The        | findings         | proved      |
| presented  | research.       | In     | Section    | V, we       | detail  | three         | buffering   |               |          |             |               |            |                  |             |
|            |                 |        |            |             |         |               |             | the potential | of       | machine     | learning      | models     | in               | identifying |
| strategies | that            | are No | Buffer,    | FIFO        | Buffer, | and           | Adaptive    |               |          |             |               |            |                  |             |
individualswhoareatahighriskofdevelopinghypertension
| Buffer, and | analyze | their | implications |     | for | clinical | learning. |     |     |     |     |     |     |     |
| ----------- | ------- | ----- | ------------ | --- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
andbroughttolighttheroleofenvironmentalfactorsinthe
SectionVIpresentstheproposedframeworkfordrift-aware
developmentofhypertension.
lifestylediseasemanagement,integratingincrementallearn-
ingwithuncertainty-drivenbuffering.SectionVIIdescribes
2) CARDIOVASCULARANDALL-CAUSEMORTALITY
| the dataset;  | target           | variables  |        | and model  | configurations |       | used       |                  |             |       |           |              |        |            |
| ------------- | ---------------- | ---------- | ------ | ---------- | -------------- | ----- | ---------- | ---------------- | ----------- | ----- | --------- | ------------ | ------ | ---------- |
|               |                  |            |        |            |                |       |            | In a prospective |             | study | that was  | published    | in BMC | Public     |
| in this study | are              | summarized |        | in Section |                | VIII. | Section IX |                  |             |       |           |              |        |            |
|               |                  |            |        |            |                |       |            | Health [14],     | researchers |       | evaluated | the efficacy |        | of machine |
| outlines      | the experimental |            | setup, | including  |                | drift | simulation |                  |             |       |           |              |        |            |
techniques and evaluation protocols. Section X reports and learningmodelsinpredictingdeathfromcardiovascularand
|             |                 |     |     |             |          |                 |           | all-cause     | causes  | by using | data       | from 2007 | to 2010.  | During    |
| ----------- | --------------- | --- | --- | ----------- | -------- | --------------- | --------- | ------------- | ------- | -------- | ---------- | --------- | --------- | --------- |
| discusses   | the comparative |     |     | performance |          | of the          | buffering |               |         |          |            |           |           |           |
|             |                 |     |     |             |          |                 |           | the research, | various |          | techniques | were      | utilized, | including |
| strategies. | In Section      | XI, | we  | provide     | clinical | interpretations |           |               |         |          |            |           |           |           |
andcase-levelinsightsfromourresults.Finally,SectionXII supportvectormachines(SVM),randomforest,andextreme
gradientboosting.Theresultsshowedthatmachinelearning
| concludes | the paper | with | a   | summary | of  | key findings | and |     |     |     |     |     |     |     |
| --------- | --------- | ---- | --- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
outlinesfutureresearchdirections. modelsperformedbetterthantraditionalstatisticalmethods,
|     |     |     |     |     |     |     |     | with AUC  | values        | of  | 0.862      | and 0.836     | for cardiovascular |          |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ---------- | ------------- | ------------------ | -------- |
|     |     |     |     |     |     |     |     | mortality | and all-cause |     | mortality, | respectively. | The                | research |
II. BACKGROUNDANDRELATEDWORK
The growing adoption of AI-based predictive models in highlightedthesignificanceoflifestylechoicesinrelationto
mortalityrisk,aswellasthepotentialofmachinelearningin
| healthcare | brings | forth | the significant |     | challenge |     | of concept |     |     |     |     |     |     |     |
| ---------- | ------ | ----- | --------------- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
drift,wheremodelperformancedegradesasunderlyingdata relationtoriskstratification.
| distributions | shift | over | time | [9]. | This | phenomenon | is a |     |     |     |     |     |     |     |
| ------------- | ----- | ---- | ---- | ---- | ---- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
well-documentedissueinstreamingdataapplications,anda 3) METABOLICSYNDROMEPREDICTION
substantial body of research has been dedicated to methods To develop and validate machine learning-based models for
for its detection and adaptation [10]. While innovative the prediction of metabolic syndrome (MetS), international
approaches for drift adaptation, such as trust decay-based cohort validation research was conducted. The research
temporal learning, have been explored in other domains utilized a number of machine learning methods, such as
likerecommendersystems[11],thehealthcarefieldpresents multilayer perceptron (MLP) and XGBoost, to analyze
unique difficulties. A particularly critical problem is the the data obtained from the China Health and Retirement
prediction of performance drift in clinical settings where Longitudinal Study (CHARLS), the Korea National Health
groundtruthlabelsareoftendelayedorentirelyunavailable, and Nutrition Examination Survey (KNHANES), the UK
makingitessentialtodevelopmethodsthatcanensuremodel Biobank,andtheNHANES.Ahighlevelofpredictiveability
reliabilitywithoutimmediateoutcomedata[12]. wasexhibitedbytheMLPmodelacrossavarietyofcohorts,
Chronic illnesses, which include cardiovascular disease with an AUC of 0.9055 in the NHANES cohort. This work
(CVD), diabetes, and hypertension, continue to be among demonstrates that machine learning models can be applied
the leading causes of morbidity and mortality across the to a wide variety of populations for the purpose of MetS
| globe.Machinelearning(ML)andartificialintelligence(AI) |     |     |     |     |     |     |     | prediction. |     |     |     |     |     |               |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | ------------- |
| 174004                                                 |     |     |     |     |     |     |     |             |     |     |     |     |     | VOLUME13,2025 |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
FIGURE1. Mindmapoftheexperimentalframeworkforconceptdriftdetectioninlifestylediseaseprediction.
4) ATHEROSCLEROTICCARDIOVASCULARDISEASE(ASCVD) about the likelihood of problems associated with diabetes.
IDENTIFICATION Thepurposeofthestudywastoaddressethnicdisparitiesin
The primary objective of [15] was to construct an inter- healthoutcomesrelatedtodiabetes.Theresearchhighlighted
pretablemachinelearningmodelforthediagnosisofASCVD thepotentialofmergingmachinelearningwithadministrative
byutilizingdemographicfactorsanddietarypatternsderived datainordertoidentifyindividualswhoareathighriskandto
from data spanning the years 1999 to 2018. In addition usethisinformationtoinformtargetedinterventions,partic-
to demonstrating that the incorporation of dietary habits in ularlyincommunitiesthatarefacinghealthdisparities[16].
additiontodemographicparametersimprovedthepredictive
accuracy of ASCVD risk models, the study highlighted the
6) OSTEOPOROSISRISKASSESSMENT
significanceofmodelinterpretabilityinclinicalsettings.
AnMLmodelfordiagnosingosteoporosiswasbuiltby[17]
thatwaspublishedinBMCResearchNotes.Themodelwas
5) DIABETESCOMPLICATIONSPREDICTION developed using data from the data set. The performance
ResearchersinAotearoaNewZealandusedmachinelearning of the model was superior to that of conventional clinical
(ML) and social administrative data to make predictions assessment tools, and it highlighted the significance of
VOLUME13,2025 174005

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
interpretable AI techniques. In addition, the study empha- adaptationandknowledgeretention,PAGEmakesitpossible
sized the necessity of integrating various data sources, such to do generative replay without preserving data from previ-
asgeneticinformationandimaginginvestigations,inorderto ous domains. An expanded inductive conformal prediction
improvetherobustnessofpredictivemodels. method is incorporated into the model in order to provide
|     |     |     |     |     |     | confidence | scores | and | credibility |     | values, which |     | in turn |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ----------- | --- | ------------- | --- | ------- |
improvestheinterpretabilityofdiseasedetection.
7) CHRONICKIDNEYDISEASE(CKD)INABDOMINAL
OBESITY
Usingmachinelearningtechniques,[18]researchedtheiden-
11) BIASANDEQUITYINMACHINELEARNING
tificationandoptimizationofkeyfactorsforchronickidney APPLICATIONS
disease (CKD) in individuals who had abdominal obesity. Intheirscopingstudy,[14]investigatedthepresenceofbias
Throughtheutilizationofdataspanningfrom2005to2018, in machine learning systems that were designed to address
the research endeavor employed a number of machine non-communicablediseasesatthepopulationlevel.Toensure
| learning | techniques | to  | discover | critical predictors. | These |                 |     |         |            |     |                  |     |     |
| -------- | ---------- | --- | -------- | -------------------- | ----- | --------------- | --- | ------- | ---------- | --- | ---------------- | --- | --- |
|          |            |     |          |                      |       | that healthcare |     | results | are equal, | the | study emphasized |     | the |
predictors were triglyceride glucose, waist circumference, significanceofconsideringbiasesduringthedatacollection,
and the composite dietary antioxidant index. Machine modelbuilding,anddeploymentprocesses.Transparencyand
| Learning | was shown | to  | be helpful | in revealing | the intricate |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ---------- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
fairnesswereemphasizedasbeingequallyimportant.
| relationships | between |     | metabolic | variables | and the risk of |     |     |     |     |     |     |     |     |
| ------------- | ------- | --- | --------- | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
chronickidneydisease(CKD)bythefindings.
12) ADVANCEDMACHINELEARNINGTECHNIQUESIN
CHRONICDISEASEPREDICTION
8) ISCHEMICSTROKEANDHEAVYMETALEXPOSURE Withthehelpofdata,[23]investigatedtheuseofavarietyof
Usingdatafrom2003to2018,[19]utilizedmachinelearning supervisedmachinelearningalgorithmstomakepredictions
techniquestoinvestigatetheconnectionbetweenheavymetal
|     |     |     |     |     |     | about depressive |     | illnesses. | In  | this study, | a comparison |     | was |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --- | ----------- | ------------ | --- | --- |
exposure and ischemic stroke. The promise of machine madebetweenseveraldifferentstatisticalmethods,including
learninginenvironmentalhealthresearchwasdemonstrated
logisticregression,randomforest,NaïveBayes,supportvec-
by the study, which focused on identifying connections tor machines (SVM), eXtreme Gradient Boost (XGBoost),
betweenheavymetallevelsandstrokerisk.Thestudyutilized andLightGradientBoostedMachine(Light-GBM2).Shap-
logisticregressionandothermachinelearningtechniques.
|     |     |     |     |     |     | ley Additive     | Explanations |        | (SHAP)   | were | utilized   | to   | explain |
| --- | --- | --- | --- | --- | --- | ---------------- | ------------ | ------ | -------- | ---- | ---------- | ---- | ------- |
|     |     |     |     |     |     | the significance |              | of the | features | in   | the models | that | were    |
9) CONCEPTDRIFTANDINCREMENTALLEARNINGIN examined. The findings indicated that machine learning
HEALTHCARE modelswerecapableofaccuratelypredictingdepressivedis-
orders,withcertainalgorithmsexceedingstandardstatistical
Tolearnchangingdata,[20]presentedaneighbor-searching
discrepancy-baseddriftdetectionsystem.Realconceptdrift, methodsintermsofaccuracyandinterpretability.
whichreferstochangesinthecategorizationboundaryover Usingdatafrom2007to2016,[24]builtapredictivemodel
time, was the subject of the study, which addressed the for teenage metabolic syndrome (MetS). The researchers
difficulties associated with recognizing it. The proposed used LASSO (Least Absolute Shrinkage and Selection
method displayed a high level of accuracy in detecting Operator) regression to choose features and constructed
real concept drift while disregarding virtual drift. This numerous machine learning models, one of which was
provided useful insights for sustaining the performance of LightGBM, which produced the greatest performance with
machine learning models in healthcare environments that an area under the curve (AUC) of 0.969. Both of these
are constantly changing. CEL is a continual learning model models were used to pick features. In addition, the model
for disease outbreak prediction that was presented by [21]. was interpreted further by employing SHAP values, which
Thismodelmakesuseofdomainadaptabilitythroughelastic led to the identification of critical predictors such as the
weightconsolidation.Thepurposeofthemodelwastoreduce age-specific proportion of body mass index (BMI), weight,
|             |              |     |            |         |                 | and upper | arm | circumference. |     | In the | study, the | potential | of  |
| ----------- | ------------ | --- | ---------- | ------- | --------------- | --------- | --- | -------------- | --- | ------ | ---------- | --------- | --- |
| the risk of | catastrophic |     | forgetting | in deep | neural networks |           |     |                |     |        |            |           |     |
bypunishingchangestoparametersthatwereconsideredto machinelearningmodelsinearly,non-invasivescreeningfor
be relevant. During the evaluation of CEL’s performance, metabolicsyndromeinadolescentswashighlighted.
| diseases       | such as | measles,     | mpox, | and influenza  | were used    |     |     |     |     |     |     |     |     |
| -------------- | ------- | ------------ | ----- | -------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| to demonstrate | its     | adaptability |       | to incremental | data and its |     |     |     |     |     |     |     |     |
13) LIFESTYLEFACTORSANDOBESITY
potentialforproactivediseasecontrol. Utilizing pooled data from the China Health and Nutrition
|     |     |     |     |     |     | Survey | (CHNS) | and | the National |     | Health | and Nutrition |     |
| --- | --- | --- | --- | --- | --- | ------ | ------ | --- | ------------ | --- | ------ | ------------- | --- |
10) DOMAIN-INCREMENTALADAPTATION Examination Survey, research conducted by Guo et al. uti-
PAGE(PatientActivationinGenomicsandEngagement)isa lized interpretable machine learning techniques to evaluate
domain-incremental adaptation approach with past-agnostic the relative significance of lifestyle factors in predicting
generative replay that was introduced by [22] to offer overweight and obesity among people. The study utilized
intelligent healthcare. To strike a balance between domain decisiontree,randomforest,andgradient-boostingdecision
| 174006 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
tree models. The SHAP analysis revealed that sedentary resultsacrossawiderangeofpeopleshouldbetheprimary
behavior, alcohol consumption, and protein intake were interests of future study. Additionally, the development of
important predictors of overweight and obesity. The study standardized frameworks for model evaluation and drift
wasconductedintheUnitedStates.Basedonthesefindings, detection willbe vital for thecontinued success ofmachine
itappearsthatmachinelearningmodelshavethepotentialto learningapplicationsinchronicillnessriskmodeling.Thisis
offerdetailedinsightsintolifestyle-relatedhealthconcerns. becausetheseframeworkswillpreventdrift.
B. CONCEPTDRIFTDETECTIONANDINCREMENTAL D. SCOPEANDLIMITATIONOFTHEWORK
LEARNINGINHEALTHCARE This study explores the amalgamation of various temporal
Aninnovativeapproachtoidentifyingtrueideadriftinchang- and spatial deep learning models with adaptive buffering
ing data streams was presented by [13], with a particular mechanisms to detect and respond to concept drift in the
emphasisonchangesincategorizationboundaryregions.The contextoflifestylediseasemodeling.Usingthedataset,itsys-
neighbor-searchingdiscrepancy-baseddriftdetectionscheme tematicallybenchmarksthreedriftdetectionstrategies,such
that has been suggested is able to differentiate between real as error-based, statistical test-based, and uncertainty-based,
and virtual drift in an efficient manner, hence providing across multiple deep learning models, namely Bi-LSTM,
insights into the direction in which classification boundary GRU, LSTM, and Bayesian Neural Networks (BNNs). The
alterationsareoccurring.Throughtheaccurateidentification scopecanbeextendedto,
ofwhenmodelchangesarerequired,thisstrategyimproves • Assessing how streaming batch-based model updates
the adaptability of machine learning models in healthcare can be effectively supported with different buffer
environmentsthatareconstantlychanging. strategiestosustainpredictiveperformanceovertime
Reference [24] presented an overview of performance- • Examining the role of adaptive buffering in retaining
aware drift detectors and emphasized the significance of clinically relevant samples and improving responsive-
monitoring model performance degradation in order to nesstonon-stationaryhealthdata
identify concept drift. In the study, several drift detection • Comparativeunderstandingofhowdifferentdriftdetec-
methods were grouped according to their mathematical torsperformundernon-stationarydata,bothintermsof
definitions and tactics. This resulted in the creation of a sensitivityandclinicalinterpretability
consolidatedtaxonomythatcanbeusedtocomprehendand • Simulating synthetic concept drift within real-world
manageconceptdriftinpredictivesystems.Itispossiblefor health data streams to mirror clinically unexpected
datadistributionsinhealthcareapplicationstovaryovertime, behaviorchangesinpatientpopulations
and this framework helps to preserve the trustworthiness of • Emphasizing uncertainty-aware modeling with MC
machinelearningmodelsinthoseapplications. Dropout and BNNs for more explainable and stable
performanceindynamichealthcareenvironments
C. SUMMARYOFLITERATUREREVIEWANDFUTURE Thelimitationsofthepresentedresearchare,
DIRECTIONS • The study uses synthetically induced drift scenarios to
Incorporating machine learning and artificial intelligence evaluate detection mechanisms. Though the drift was
approaches into the analysis of data has resulted in major inducedinthecontrolledmanner,stillthefullessenceof
advancements in both the prediction and understanding of completenon-stationaritymaynothavebeencaptured
chronic diseases. Recent research has shown that various • Clinicallysignificantmodalitiessuchasimaging,wear-
machine learning models are effective in predicting condi- able sensors, or genomics that could influence drift
tionssuchashypertension,metabolicsyndrome,depression, dynamicsarenotmodeledinthisstudy,asthefocusis
and obesity. These models frequently beat classic statistical onthetabularnatureofdataset
methods in this regard. Furthermore, the creation of inter- • Live electronic health record (EHR) systems are not
pretablemodelsandtheuseofSHAPvalueshavecontributed usedintheexperimentation,butthedatasetisstilltaken
toanincreaseintheclinicalapplicabilityandtransparencyof asstreambatchestoemulatethestreamingenvironment,
thesepredictivetools. whichmightlimitthefullscopeofOnlinelearning
Concurrently, developments in concept drift detection • The study is based on U.S.-specific health survey
and incremental learning are addressing the issues that data, so adapting to the different demography requires
are posed by the ever-changing data distributions in the changes to the preprocessing phase of the learning
healthcareindustry.Whenitcomestopreservingtheaccuracy models
and dependability of machine learning models over time, • The use of complex architectures like BNNs with MC
it is essential to make use of innovative methods such Dropout introduces computational overhead that may
asneighbor-searchingdiscrepancy-baseddriftdetectionand limitthedeploymentinlow-resourceenvironments
performance-awaredriftdetectors.
The integration of these advanced machine learning III. CONCEPTDRIFT
approacheswithreal-timedatastreams,theenhancementof Lifestylediseasessuchasdiabetes,hypertension,andcardio-
model adaptability, and the guaranteeing of fair healthcare vascular disorders are not static conditions; they are shaped
VOLUME13,2025 174007

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
by continuously evolving behavioral, environmental, and systemsthatarebothresponsiveandadaptive.Thesediseases
socioeconomic factors. These dynamic influences introduce arecloselyrelatedtofactorsthatfluctuateovertime—dietary
non-stationarity in the learning environment, known as habits, physical activity levels, stress, and environmental
concept drift, into clinical and lifestyle datasets, where the influences—making the associated health data inherently
underlying data distributions change over time. Such drift dynamic. As patient behaviors shift, so too do the patterns
posesasignificantchallengetotraditionalpredictivemodels, within clinical datasets, creating a moving target for tradi-
whichoperateundertheassumptionofstaticdistributionsand tionalpredictivemodels.Capturingthistemporalvariability
arethereforepronetodegradationinaccuracyasreal-world is essential for accurate risk identification and timely inter-
conditionsevolve.Instreaminghealthcareenvironments,this vention. To address this challenge, the proposed framework
driftmanifeststhroughchangesinpatienthabits,healthcare employs an incremental learning approach designed to
access, seasonal effects, and public health interventions. adapt to these evolving data patterns. Figure 2 illustrates
Toaddressthis,incrementallearningprovidesapromising the proposed architecture for incremental learning under
solution by enabling models to update continuously as conceptdriftusingbufferedclinicaldatastreams.Streaming
new data becomes available. However, the efficacy of data, such as patient records arriving over time, are first
this approach heavily depends on how historical data is passed through a buffer mechanism that temporarily stores
managed. This motivates the incorporation of buffering incoming data in batches. These buffered batches enable
strategies such as FIFO (First In First Out) or adaptive bothshort-termmemoryandstatisticalanalysis.Thebuffered
memorymodulesthatselectivelyretainrelevantinformation data then undergo drift detection, which assesses whether
to support model adaptability and mitigate the effects of significant changes have occurred in the data distribution.
conceptdriftinpersonalizedlifestylediseaseriskprediction. When drift is detected, the model is updated incrementally
Themathematicalperspectiveoftheconceptdriftisdiscussed using the buffered data, thereby ensuring adaptability to
next. evolving clinical patterns. In parallel, the current buffered
| ∈   |     |     | ∈   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Let X X be the input space and Y Y be the output instanceisusedtogeneratereal-timepredictionsforclinical
space.Insupervisedlearning,thedataisassumedtofollowa decision support. A feedback loop ensures that the model
jointdistributionshowninequation1as, remains synchronized with observed data shifts, supporting
continuouslearningindynamichealthcareenvironments.
|     |     | D =P (X,Y) |     | (1) |       |       |                |       |         |                |     |
| --- | --- | ---------- | --- | --- | ----- | ----- | -------------- | ----- | ------- | -------------- | --- |
|     |     | t t        |     |     | Let D | = {(x | ,y )} the data | be at | time t. | In incremental |     |
|     |     |            |     |     |       | t     | t t            |       |         |                |     |
Concept drift occurs when the joint distribution changes learning, the model f t is updated over time as shown in
| overtimeasshowninequation2as, |     |              |       |     | equation3. |     |       |        |      |     |     |
| ----------------------------- | --- | ------------ | ----- | --- | ---------- | --- | ----- | ------ | ---- | --- | --- |
|                               |     |              |       |     |            |     | =A(f  | ,(x ,y |      |     |     |
|                               | ∃t  | ,t suchthatD | ̸=D   | (2) |            |     | f t+1 | t t    | t )) |     | (3) |
|                               | 1   | 2            | t1 t2 |     |            |     |       |        |      |     |     |
whereAdenotesthelearningalgorithmcapableofadapting
themodelincrementally.
Mathematicaltypesofconceptdrift.
TABLE1.
|     |     |     |     |     | V. BUFFERINGSTRATEGIESFORDRIFT-AWARECLINICAL |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
INCREMENTALLEARNING
|     |     |     |     |     | In streaming | healthcare | environments, |     | where | patient | data |
| --- | --- | --- | --- | --- | ------------ | ---------- | ------------- | --- | ----- | ------- | ---- |
arrivessequentiallyandmayundergodistributionalchanges
|     |     |     |     |     | over time.  | The         | ability of a    | model to | retain     | or discard   | past |
| --- | --- | --- | --- | --- | ----------- | ----------- | --------------- | -------- | ---------- | ------------ | ---- |
|     |     |     |     |     | information | is critical | for maintaining |          | predictive | reliability. |      |
Therearevarioustypesofdriftavailablebasedonwhatis Buffering strategies play a central role in managing this
changinginthedatadistributionsummarizedintable1.The temporal information by determining which data points
driftcanbe, are preserved for future learning updates. In this section,
1) Changes in the marginal distribution P(X) called as we explore three such strategies: No Buffer, FIFO Buffer,
covariatedrift. and Adaptive Buffer, each offering a distinct approach to
ChangesintheposteriordistributionP(Y|X)calledas
| 2)  |     |     |     |     | balancing | memory | efficiency, | responsiveness |     | to  | concept |
| --- | --- | --- | --- | --- | --------- | ------ | ----------- | -------------- | --- | --- | ------- |
realdrift. drift,andclinicalrelevance.Thesestrategiesareparticularly
3) ChangesinclasspriorsP(Y)calledaspriorprobabil- importantinthecontextoflifestylediseasemodeling,where
itydrift. patientbehaviorsandriskfactorsevolvegraduallyorabruptly
Thepresentedworkaimsatcapturingrealdriftinthedataset overtime.Weexamineeachofthesebufferstrategiesindetail
below.
usingincrementallearningwithbufferingstrategies.
|     |     |     |     |     | A. NOBUFFERSTRATEGY |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
IV. INCREMENTALLEARNINGFRAMEWORK
The rising prevalence of lifestyle-related diseases such The no-buffer strategy is the most memory-efficient incre-
as obesity, type 2 diabetes, and cardiovascular conditions mental learning setup, where the model is updated only on
highlights the quintessential need for predictive healthcare the most recent batch of data. This approach is suitable
| 174008 |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
FIGURE2. Generalarchitectureofincrementallearningwithbuffer-baseddriftadaptation.
for latency-sensitive or resource-constrained applications. wherehisthenumberoftrainableparameters.Thismethod
However, it lacks historical context, making it prone to ismemory-lightandfastbutlacksresiliencetolong-termor
catastrophicforgettingandoverfittingtoshort-termnoise. recurringdriftsduetotheabsenceofhistoricaldata.
LetB t denotetheincomingbatchattimet.Themodelfθ
| isupdatedasgivenbyequation4 |     |     |             |     |       |     | B. FIFOBUFFERSTRATEGY  |     |        |        |           |              |     |
| --------------------------- | --- | --- | ----------- | --- | ----- | --- | ---------------------- | --- | ------ | ------ | --------- | ------------ | --- |
|                             |     |     |             |     |       |     | The First-In-First-Out |     | (FIFO) | buffer | maintains | a fixed-size |     |
|                             | θ   | ←θ  | −η·∇θL(fθ(B |     | ),y ) | (4) |                        |     |        |        |           |              |     |
t+1 t t t window of the most recent data batches. When new data
|         |        |          |          |          |                |      | arrives and | the | buffer is | full, the | oldest | batch is discarded. |     |
| ------- | ------ | -------- | -------- | -------- | -------------- | ---- | ----------- | --- | --------- | --------- | ------ | ------------------- | --- |
| where η | is the | learning | rate and | L is the | loss function. | This |             |     |           |           |        |                     |     |
Thisbufferallowsshort-termmemory,reducingvarianceand
| formulation | can | lead to | unstable | updates | due to the | small |     |     |     |     |     |     |     |
| ----------- | --- | ------- | -------- | ------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
improvinggeneralization.
batchsizeandlackofmemory.
|     |     |     |     |     |     |     | For a buffer | of  | size K, | the active | memory | at time | t given |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ---------- | ------ | ------- | ------- |
TheNoBufferstrategyupdatesthemodelparametersusing
|          |         |          |       | Rn×d, |       |          | byequation8, |     |     |     |     |     |     |
| -------- | ------- | -------- | ----- | ----- | ----- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
| only the | current | incoming | batch | B ∈   | where | n is the |              |     |     |     |     |     |     |
t
| batchsizeandd |     | isthefeaturedimension.Themodelupdate |     |     |     |     |     |     |         |       | ,...,B |     |     |
| ------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | ----- | ------ | --- | --- |
|               |     |                                      |     |     |     |     |     |     | M t ={B | t−K+1 |        | t } | (8) |
isgivenbyequation5,
Modelupdateisthencarriedoutoverthisbuffergivenby9,
|     | θ   | ←θ  | −η·∇θL(fθ(B |     | ),y ) | (5) |     |     |                |     |     |       |     |
| --- | --- | --- | ----------- | --- | ----- | --- | --- | --- | -------------- | --- | --- | ----- | --- |
|     |     | t+1 | t           | t   | t     |     |     | θ   | ←θ −η·∇θL(fθ(M |     |     | ),y   |     |
|     |     |     |             |     |       |     |     | t+1 | t              |     |     | t t ) | (9) |
Theoverallspacecomplexityinducedbythisapproachis
|     |     |     |     |     |     |     | The FIFO | Buffer | strategy | maintains |     | a sliding window | of  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | --------- | --- | ---------------- | --- |
givenbyequation6,
|                             |               |     |            |     |         |         | themostrecentK |     | batchesgivenbyequation10 |         |        |        |          |
| --------------------------- | ------------- | --- | ---------- | --- | ------- | ------- | -------------- | --- | ------------------------ | ------- | ------ | ------ | -------- |
|                             |               |     | O(M )=O(n) |     |         | (6)     |                |     | ={B                      |         | ,...,B | }      |          |
|                             |               |     | t          |     |         |         |                |     | M t                      | t−K+1   |        | t      | (10)     |
| The overall                 | computational |     | complexity |     | induced | by this |                |     |                          |         |        |        |          |
|                             |               |     |            |     |         |         | The model      | is  | retrained                | on this | memory | buffer | given by |
| approachisgivenbyequation7, |               |     |            |     |         |         | equation11,    |     |                          |         |        |        |          |
|                             |               |     |            |     |         |         |                | θ   | ←θ −η·∇θL(fθ(M           |         |        | ),y    |          |
|                             |               | O(C | t )=O(n·d  | ·h) |         | (7)     |                | t+1 | t                        |         |        | t t )  | (11)     |
| VOLUME13,2025               |               |     |            |     |         |         |                |     |                          |         |        |        | 174009   |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
The overall space complexity induced by FIFO buffer The overall computational complexity induced by the
approachisgivenbytheequation12, FIFObufferapproachisgivenbyequation19,
|     |     | O(M | )=O(K | ·n) |     | (12) |     |     | O(C | )=O(m·n·d |     | ·h) |     | (19) |
| --- | --- | --- | ----- | --- | --- | ---- | --- | --- | --- | --------- | --- | --- | --- | ---- |
|     |     |     | t     |     |     |      |     |     |     | t         |     |     |     |      |
The overall computational complexity induced by the This strategy allows for dynamic, relevance-driven memory
|     |     |     |     |     |     |     | allocation, | making | it  | particularly | effective |     | for | handling |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | ------------ | --------- | --- | --- | -------- |
FIFObufferapproachisgivenbyequation13,
|     |     |       |     |          |     |      | abrupt and                                 | recurring                   | drifts. | The | aforementioned |     | strategies’ |        |
| --- | --- | ----- | --- | -------- | --- | ---- | ------------------------------------------ | --------------------------- | ------- | --- | -------------- | --- | ----------- | ------ |
|     |     | )=O(K |     | ·n·d ·h) |     |      |                                            |                             |         |     |                |     |             |        |
|     |     | O(C t |     |          |     | (13) | computationaldetailsaresummarizedintable2. |                             |         |     |                |     |             |        |
|     |     |       |     |          |     |      | Theorem1:                                  | [ConvergenceCondition]Let{D |         |     |                |     | }∞          | denote |
t t=1
| This buffer | allows      | short-term |     | memory      | and smoothing | but       |            |              |     |               |     |            |     |          |
| ----------- | ----------- | ---------- | --- | ----------- | ------------- | --------- | ---------- | ------------ | --- | ------------- | --- | ---------- | --- | -------- |
|             |             |            |     |             |               |           | a sequence | representing |     | the magnitude |     | of concept |     | drift at |
| does not    | distinguish | between    |     | informative | and           | redundant |            |              |     |               |     |            |     |          |
timet,andlettheAdaptiveReplayBufferhaveamaximum
samples.
|     |     |     |     |     |     |     | capacity              | of B adaptive | . Suppose | drift                   | detection |     | and retraining |      |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | ------------- | --------- | ----------------------- | --------- | --- | -------------- | ---- |
|     |     |     |     |     |     |     | aretriggeredwheneverD |               |           | > τ,forafixedthresholdτ |           |     |                | > 0. |
t
C. ADAPTIVEBUFFERSTRATEGY Iftheexpecteddriftmagnitudeisboundedsuchthat
| The adaptive |     | buffer dynamically |     | adjusts | its memory | based |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------ | --- | ------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ondriftseverityormodeluncertainty.UnlikeFIFO,itselec- lim E[D ]<τ, (20)
|                |     |           |         |       |       |              |     |     | t→∞ |     | t   |     |     |     |
| -------------- | --- | --------- | ------- | ----- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| tively retains |     | data from | batches | where | drift | is detected, |     |     |     |     |     |     |     |     |
thentheadaptivebufferstabilizes,andthesystemconverges
| allowing | focused | retraining | while | minimizing |     | redundancy. |     |     |     |     |     |     |     |     |
| -------- | ------- | ---------- | ----- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
In adaptive replay buffer strategies, the model dynamically toasteadystatewithboundedmemorygrowth.
|     |     |     |     |     |     |     | Proof: | The adaptive |     | replay | buffer | adds data | to  | memory |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ------ | ------ | --------- | --- | ------ |
retainsonlythosedatabatchesthatcorrespondtosignificant
|                                                         |     |              |     |             |         |           | only when | a drift      | is    | detected, | i.e., when | D         | >   | τ. Over  |
| ------------------------------------------------------- | --- | ------------ | --- | ----------- | ------- | --------- | --------- | ------------ | ----- | --------- | ---------- | --------- | --- | -------- |
| conceptdriftevents.Unlikefixed-sizebuffersthatstoredata |     |              |     |             |         |           |           |              |       |           |            |           | t   |          |
|                                                         |     |              |     |             |         |           | time, if  | the expected | drift | magnitude |            | satisfies | the | bound in |
| indiscriminately,                                       |     | the adaptive |     | buffer uses | a drift | detection |           |              |       |           |            |           |     |          |
Equation(20),thefrequencyofdriftdetectiondecreases.
| mechanism | typically | based | on  | uncertainty | estimates | such |     |     |     |     |     |     |     |     |
| --------- | --------- | ----- | --- | ----------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
as Monte Carlo dropout to determine whether the current ByMarkov’sinequalitygivenbyequation21,
E[D
| batchreflectsadistributionalshift.Whenadriftisdetected, |     |       |           |           |     |              |     |     |     |      |     | t ] |     |      |
| ------------------------------------------------------- | --- | ----- | --------- | --------- | --- | ------------ | --- | --- | --- | ---- | --- | --- | --- | ---- |
|                                                         |     |       |           |           |     |              |     |     | P(D | >τ)≤ |     |     |     | (21) |
| the corresponding                                       |     | batch | is stored | in memory |     | and used for |     |     |     | t    | τ   |     |     |      |
retraining.Batchesthatdonotshowanysignificantdeviation implying that the probability of drift detection becomes
from the previous distribution are discarded to conserve E[D →
|     |     |     |     |     |     |     | arbitrarily | small | as  | t ] | 0. As | a result, | fewer | new |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | --- | ----- | --------- | ----- | --- |
memory.Thisensuresthatthemodelselectivelylearnsfrom
|                                                         |     |           |           |        |               |      | samples      | are added | to      | the buffer,             | and | the update | frequency |     |
| ------------------------------------------------------- | --- | --------- | --------- | ------ | ------------- | ---- | ------------ | --------- | ------- | ----------------------- | --- | ---------- | --------- | --- |
| informativeinstanceswhileavoidingoverfittingtoredundant |     |           |           |        |               |      | diminishes.  |           |         |                         |     |            |           |     |
| or stationary                                           |     | data. The | following | figure | 3 illustrates | this |              |           |         |                         |     |            |           |     |
|                                                         |     |           |           |        |               |      | Thisbehavior |           | leadsto | eventualstabilizationof |     |            | thebuffer |     |
process. sizeandmodelparameters,assumingtheunderlyinglearning
| Let’s | U denote | model | uncertainty | at  | time | t. A drift is |                                                     |     |     |     |     |     |     |     |
| ----- | -------- | ----- | ----------- | --- | ---- | ------------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|       | t        |       |             |     |      |               | dynamicsalsohold.Hence,theadaptivesystemconvergesin |     |     |     |     |     |     |     |
detectedifitsatisfiestheequation14
|     |     |     |      |     |     |      | bothmemoryandpredictivestability. |     |     |     |     |     |     | □   |
| --- | --- | --- | ---- | --- | --- | ---- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | U   | >α·U |     |     | (14) |                                   |     |     |     |     |     |     |     |
|     |     |     | t    | t−1 |     |      |                                   |     |     |     |     |     |     |     |
VI. PROPOSEDFRAMEWORKFORLIFESTYLEDISEASE
whereα >1isasensitivitythreshold.Ifdriftisdetected,the MANAGEMENT
batchB t isaddedtothebufferA t ,andthemodelisupdated Figure 4 presents the proposed experimental workflow for
usingequation15 evaluating adaptive buffering strategies under concept drift
|     |     |     |             |     |       |      | using the | dataset. | The | process | begins | with | a data | prepro- |
| --- | --- | --- | ----------- | --- | ----- | ---- | --------- | -------- | --- | ------- | ------ | ---- | ------ | ------- |
|     | θ   | ←θ  | −η·∇θL(fθ(A |     | ),y ) | (15) |           |          |     |         |        |      |        |         |
t+1 t t t cessing pipeline that performs data cleaning, exploratory
|     |     |     |     |     |     |     | analysis, | and class | balancing | to  | ensure | model-ready |     | input. |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------- | --- | ------ | ----------- | --- | ------ |
TheAdaptiveBufferstoresonlythosebatchesidentifiedas
|     |     |     |     |     |     |     | To simulate | real-world |     | non-stationarity, |     | a   | drift induction |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ----------------- | --- | --- | --------------- | --- |
conceptuallynovelbasedonpredictiveuncertainty.Adriftis
|     |     |     |     |     |     |     | pipeline | introduces | abrupt | changes | by  | manipulating |     | class |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------ | ------- | --- | ------------ | --- | ----- |
declaredifequation16,
|     |     |      |     |        |     |     | labels, effectively |     | mimicking |     | shifts in | patient | behavior | or  |
| --- | --- | ---- | --- | ------ | --- | --- | ------------------- | --- | --------- | --- | --------- | ------- | -------- | --- |
|     |     | >α·U |     | , α >1 |     |     |                     |     |           |     |           |         |          |     |
U t t−1 (16) diagnosticcriteria.Thedataisthenstreamedinmini-batches
|     |     |     |     |     |     |     | to emulate | an online |     | learning | environment, |     | where | various |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | -------- | ------------ | --- | ----- | ------- |
⊆
HereU t isthemeanuncertaintyscoreattimet.Let’sA t deep learning architectures, including LSTM, GRU, Bi-
St
B denotethesetofbatchescorrespondingtodetected
| i=1 i |     |     |     |     |     |     | LSTM, | and Bayesian |     | Neural | Networks, | are | trained | using |
| ----- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | ------ | --------- | --- | ------- | ----- |
drifts.Themodelisupdatedusingequation17 one of three buffering strategies: No Buffer, FIFO Buffer,
θ ←θ −η·∇θL(fθ(A ),y orAdaptiveBuffer.Adriftdetectionandadaptationpipeline
|     |     | t+1 t |     |     | t t ) | (17) |          |       |          |       |             |     |        |        |
| --- | --- | ----- | --- | --- | ----- | ---- | -------- | ----- | -------- | ----- | ----------- | --- | ------ | ------ |
|     |     |       |     |     |       |      | monitors | model | behavior | using | statistical |     | tests, | hybrid |
TheoverallspacecomplexityinducedbytheFIFObuffer approach and uncertainty measures to detect drift points,
approachisgivenbytheequation18, after which the model is selectively retrained on relevant
|     |     |     |     |     |     |     | batches, | which | is highlighted |     | in the | dotted | red-lined | path. |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------------- | --- | ------ | ------ | --------- | ----- |
)=O(m·n),
|        |     | O(M t |     | m≤t |     | (18) |            |     |          |             |     |            |               |         |
| ------ | --- | ----- | --- | --- | --- | ---- | ---------- | --- | -------- | ----------- | --- | ---------- | ------------- | ------- |
|        |     |       |     |     |     |      | Throughout | the | process, | performance |     | parameters |               | such as |
| 174010 |     |       |     |     |     |      |            |     |          |             |     |            | VOLUME13,2025 |         |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
FIGURE3. Illustrationoftheadaptivereplaybuffer—Onlybatchesassociatedwithsignificantdrift(highlightedinred)areretainedinmemoryfor
retraining.Othernon-driftbatchesarediscarded,allowingthebuffertoadaptdynamicallytochangesindatadistribution.
TABLE2. Theoreticalcomplexitycomparisonofbufferstrategies.
accuracy values and uncertainty values are measured to 6) Replacingmissingvalueswithcolumn-wisemedians.
assesseachbufferingstrategy’seffectiveness.Thefinalstage 7) Filtering invalid diabetes responses and creating a
involves recording key performance metrics such as ROC, binaryclasslabelfordiabetesdiagnosis
AUC,F1-score,accuracy,andloss,allowingfortheselection
Thecumulatedprocesseddatasetcontains9,236recordsand
of the most robust and clinically relevant model. This 26 features, with the class label being the Boolean value
frameworkenablesacomprehensiveevaluationofdrift-aware
|     |     |     |     |     |     | of being diabetic | or  | not. The | features | selected | based | on  |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | -------- | -------- | ----- | --- |
learningsystemsforlifestylediseasemodelingandsupports
|     |     |     |     |     |     | relevance from | the different |     | survey files | of  | the dataset | are |
| --- | --- | --- | --- | --- | --- | -------------- | ------------- | --- | ------------ | --- | ----------- | --- |
anomalyreportingforimproveddecision-makingindynamic summarizedintable3.
healthcaresettings.
| As described |     | in Algorithm | 1, the | adaptive | buffering |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | ------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
A. CLASSBALANCING
| approach | is designed | to handle | evolving | data | distributions |                 |     |             |     |             |     |       |
| -------- | ----------- | --------- | -------- | ---- | ------------- | --------------- | --- | ----------- | --- | ----------- | --- | ----- |
|          |             |           |          |      |               | Upon performing | the | Exploratory | on  | the dataset | and | exam- |
throughdriftdetectionmechanisms,ensuringtherobustness
iningtheclassdistributionasshowninfigure5,itisevident
ofthemodelovertime.
theclasslabelsarenotbalanced,asthemajorityofthedataset
|     |     |     |     |     |     | consists of | non-diabetic | individuals. |     | To balance | this | data, |
| --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------------ | --- | ---------- | ---- | ----- |
VII. DATASETDESCRIPTIONANDPREPARATION we have applied SMOTE (synthetic minority oversampling
Thedatasetusedinthisexperimentationisderivedfrom[25] technique), which uses k-nearest neighbor to generate a
| which is | a nationally | representative, | cross-sectional |     | dataset |                    |        |     |          |        |        |        |
| -------- | ------------ | --------------- | --------------- | --- | ------- | ------------------ | ------ | --- | -------- | ------ | ------ | ------ |
|          |              |                 |                 |     |         | synthetic minority | sample |     | equating | to the | number | of the |
developedandmaintainedbytheNationalCenterforHealth majorityclasssamples.BMI(BMXBMI),age(RIDAGEYR),
Statistics(NCHS),adivisionoftheCDCintheUnitedStates. and glucose proxy (LBXGLU) show a moderate positive
| The original | dataset | between | the year | 2017-18 | was split |             |          |          |                 |     |         |       |
| ------------ | ------- | ------- | -------- | ------- | --------- | ----------- | -------- | -------- | --------------- | --- | ------- | ----- |
|              |         |         |          |         |           | correlation | with the | diabetes | label (DIQ010). |     | Certain | vari- |
across multiple CSV files, each covering a different aspect ables,likeHDLcholesterol(LBDHDD)andphysicalactivity
ofparticipantdata,suchasdemographics,laboratoryresults,
(PAQ605,PAQ620),shownegativecorrelationwithdiabetes,
dietaryintake,andmedicalquestionnaires.Thefollowingare suggesting protective associations. Sociodemographic fea-
thepreprocessingstepsdoneintheprocess, tures such as education level (DMDEDUC2) and income
1) Loading 6 data sources: Demographics, Examination, (INDFMPIR) show mild correlations, indicating possible
socialdeterminantsofdiabetes.
LabResults,Diet,Questionnaire,andMedical.
2) Selectingrelevantfeaturesbasedontheirsignificance
| tolifestylediseasemodeling. |     |     |     |     |     | B. DRIFTINDUCTION |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
3) Merging all datasets using the common identifier To evaluate the robustness of concept drift detection and
columnSEQN. adaptation methods, three types of drift, abrupt, gradual,
4) Handlingcategoricalfeaturesvialabelencoding. and recurring were synthetically injected into the balanced
5) Estimating glucose levels from HbA1c using the NHANESdataset.ThetargetvariableDIQ010,representing
formula:Glucose=(HbA1c×28.7)−46.7.
|               |     |     |     |     |     | the binary | class label, | was | manipulated | to  | simulate | drift  |
| ------------- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ----------- | --- | -------- | ------ |
| VOLUME13,2025 |     |     |     |     |     |            |              |     |             |     |          | 174011 |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
FIGURE4. Proposedmethodology:adaptiveincrementallearningpipelineforconceptdriftdetectioninlifestyle
diseasemodeling.
includingthechangeinthedistributionofeachfeatures(data
| drift), alongside | the class      | label(concept |               | drift)   | due to the    |
| ----------------- | -------------- | ------------- | ------------- | -------- | ------------- |
| measurement       | device failure | or            | any equipment |          | discrepancies |
| or due to         | an environment | anomalies     |               | that can | happen over   |
time.
1) ABRUPTDRIFTINJECTION
Abruptdriftsimulatesasuddenchangeinthedatadistribution
| at a specific | point in time. | To  | induce | abrupt drift, | a single |
| ------------- | -------------- | --- | ------ | ------------- | -------- |
FIGURE5. Classdistributionoftheoriginaldataset. contiguous region of the dataset is selected starting from
| a predefined | drift index. | Labels       | within   | this | region are   |
| ------------ | ------------ | ------------ | -------- | ---- | ------------ |
| flipped      | with a fixed | probability, | referred | to   | as the drift |
scenarios. Label flipping was applied probabilistically to magnitude. A higher drift magnitude implies a more severe
emulate real-world drift behavior while maintaining control labeltransition.
over the drift magnitude and region. The following sub- Letsbethedriftstartindex,wbethewindowsize,andp
sections describe the drift injection strategies implemented bethedriftmagnitude.Foreachinstancei ∈ [s,s+w),the
isflippedto1−y
in this study. More realistic drift setup up would be classlabely i i withprobabilityp.
174012 VOLUME13,2025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
Algorithm1AdaptiveBufferingforConceptDriftDetectioninLifestyleDiseasePrediction
|     | Input:NHANESDatasetD={(x |     |     |     | ,y  | )}T   |     |     |     |     |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
| 1:  |                          |     |     |     | t   | t t=1 |     |     |     |     |     |     |     |
2: Output:Driftdetectionandmodeladaptation
PerformDataPreprocessing:
3:
4: Cleanthedata:Removenoiseandmissingvalues
PerformExploratoryDataAnalysis(EDA)
5:
6: BalancetheclassesusingtechniqueslikeSMOTE
7: SimulateDrift:
Injectdriftintodataset:
8:
Forabruptdrift:y′
| 9:  |     |     |     | ←y t ⊕p,wherepisthedriftmagnitude |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
| 10: | Forgradualdrift:y′                           |     |     | ←f(p | ,y ),wherep | isthedriftovertime |          |     |     |     |     |     |     |
| --- | -------------------------------------------- | --- | --- | ---- | ----------- | ------------------ | -------- | --- | --- | --- | --- | --- | --- |
|     |                                              |     |     | t    | t t         | t                  |          |     |     |     |     |     |     |
|     | Forrecurringdrift:Applydriftperiodicallyat{t |     |     |      |             |                    | ,t ,...} |     |     |     |     |     |     |
| 11: |                                              |     |     |      |             |                    | 1 2      |     |     |     |     |     |     |
12: EmulateOnlineLearning:
|     | Setupstreamingenvironment:{(x |     |     |     |     | ,y )}T   |     |     |     |     |     |     |     |
| --- | ----------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 13: |                               |     |     |     | t   | t t=1    |     |     |     |     |     |     |     |
|     | Dividedataintomini-batches:{B |     |     |     | ,B  | ,...,B } |     |     |     |     |     |     |     |
| 14: |                               |     |     |     | 1   | 2 n      |     |     |     |     |     |     |     |
15: ModelTraining:
|     | Trainmodelsonmini-batches:fθ |     |     |     | ←Train(B | )fori=1,...,n |     |     |     |     |     |     |     |
| --- | ---------------------------- | --- | --- | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| 16: |                              |     |     |     |          | i             |     |     |     |     |     |     |     |
17: ApplyBufferStrategies:Adaptive,FIFO,No-buffer
MeasurePerformance:
18:
19: Evaluatemodelwithmetrics:Accuracy,Precision,Recall,F1-Score,AUC
20: Foreachbatch,calculateperformance:
|     | Performance= |     | 1   | Pn I[y | =yˆ ] |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| 21: |              |     |     | t=1 t  | t     |     |     |     |     |     |     |     |     |
n
22: DetectDrift:
ifDriftDetectedthen
23:
24: Identifydriftpointsusinguncertainty,KS-Test,Hybridmethods
25: Foruncertainty-baseddetection:
|     | Uncertainty(x |     | )=E[yˆ | |x ]−E[yˆ |     | |x ]    |     |     |     |     |     |     |     |
| --- | ------------- | --- | ------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| 26: |               |     | t      | t t       |     | t−1 t−1 |     |     |     |     |     |     |     |
27: ForKS-TestorT-Test:
|     | H   | :µ =µ |     | vs H | :µ ̸=µ |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| 28: |     | 0 t   | t−1 | A    | t      | t−1 |     |     |     |     |     |     |     |
29: Updatemodelondriftpoints:
| 30: | θ t+1                              | =θ −η∇θL(fθ |     | ,B )    |     |          |       |     |     |     |     |     |     |
| --- | ---------------------------------- | ----------- | --- | ------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
|     |                                    | t           |     | t drift |     |          |       |     |     |     |     |     |     |
|     | Re-trainthemodelwithdrifteddata:fθ |             |     |         |     | ←Train(B | )     |     |     |     |     |     |     |
| 31: |                                    |             |     |         |     |          | drift |     |     |     |     |     |     |
32: else
33: Recordperformanceparametersforfutureevaluation:
={Accuracy,Precision,Recall,F1-Score,...}
34: P record
35: endif
Output:BestperformingmodelanddriftreportR
36:
2) GRADUALDRIFTINJECTION Thisensuresasmoothtransitionfromnodrifttomaximum
driftacrossthewindow,morecloselyresemblingreal-world
Gradualdriftemulatesascenariowherethedatadistribution
changes progressively over time. To simulate this, a wider driftevolution.
| window | is  | chosen | and a | linearly or | non-linearly | increasing |     |     |     |     |     |     |     |
| ------ | --- | ------ | ----- | ----------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
3) RECURRINGDRIFTINJECTION
probabilityisusedtoflipthelabels.
|     |     |     |     |     |     |     |     | Recurring | drift | captures | patterns | where the same | or similar |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | -------- | -------- | -------------- | ---------- |
Thedriftprobabilityatpositioniinthewindowisdefined
as: drift recurs at multiple intervals. This is typical in seasonal
orcyclicsystems.Driftregionsareselectedatmultiple,pre-
 defined positions throughout the dataset, and label flipping
i
|     |  | Linear: |     | p·  |     |     |     |     |     |     |     |     |     |
| --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w i s p e r fo r m e d w i thineachregionusingaconstantorvariable
|     |     |     |     | (cid:18) i (cid:19)2 |     |     |     | d ri f t | m a g n it | ud e . |     |     |     |
| --- | --- | --- | --- | -------------------- | --- | --- | --- | -------- | ---------- | ------ | --- | --- | --- |
P(i)=
|     |     | Quadratic: |     | p·  |     |     |     |     | =   | {b ,b ,...,b | }   |                   |               |
| --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------------- | ------------- |
|     |     |            |     | w   |     |     |     | Let | B   | 1 2          | n   | denote the set of | batch indices |
Sigmoid:
1 w h e re d r if t re c u r s . F o r ea c h b ∈ B , a w i n d o w o f si z e w i s
|     |     |     |     | p·  | ,   | z ∈[−6,6] |     |     |     |     |     | j   |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
i d e fi n ed , a n d w it h i n t h at w i nd o w , e a ch la b e l i s fl i pp e d w it h
|     |     |     |     | 1 + e−zi |     |     |     |                                         |     |     |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
|     |     |     |     |          |     |     |     | probabilityp,whichmayvaryperrecurrence. |     | j   |     |     |     |
wherepisthemaximumdriftmagnitude,andwisthesizeof The summary of the induced drift points for Abrupt,
thedriftwindow. Gradual and Recurring drift are shown in table 4 with
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 174013 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
TABLE3. Descriptionofthecolumnsselectedforexperimentationfromdataset.
4statisticaltestsperformedtoconfirmthepresenceofdrift, inference, enabling it to estimate prediction uncertainty.
they are, KS-Test, Chi-Squared, T-Test, and Wasserstein This is particularly beneficial in drift-prone environments
Distance measures. The methodology employed to confirm wheredecisionconfidencevaries.TheGRUemploysaGated
the drift is if any two tests has p-value < 0.05, then drift is RecurrentUnit,whichiscomputationallyefficientcompared
flaggedandconfirmed. to LSTMs and captures sequential dependencies while
using fewer parameters. Lastly, the LSTM uses a standard
TABLE4. Driftdetectionsummaryusingstatisticaltests. unidirectionalLSTMlayertomodellong-termdependencies
in the input data. All models incorporate dropout and are
designedtooutputabinarypredictionindicatingthepresence
orabsenceofdiabetes,servingascorelearnersintheadaptive
bufferingframework.Thedescriptionsofeachofthemodels
aresummarizedintable5.
IX. EXPERIMENTALSETUPANDEVALUATIONCRITERIA
TheexperimentationisconductedonanAcerNitromachine
VIII. MODELDESCRIPTION with a Ryzen 7 and a CUDA-enabled Nvidia GPU with
The four deep learning models implemented in this study graphics3050with6GBgraphics.Toassessandvalidatethe
are BiLSTM, BNN, GRU, and LSTM which serve as presence of concept drift in the context of lifestyle disease
temporal learners for detecting lifestyle disease patterns modeling, we employed three complementary strategies for
under concept drift. The BiLSTM (Bidirectional LSTM) driftpointidentification.Eachstrategyisdesignedtocapture
model leverages both forward and backward temporal differentdimensionsofdistributionalandpredictiveshiftsin
dependencies, enhancing contextual learning by processing thedatastream.
input sequences from both directions. It uses dropout 1) Statistical Test-Based Detection (KS-Test and T-
regularization and a fully connected layer followed by a Test)
sigmoid activation to produce probabilistic outputs. The This method relies purely on statistical hypothesis
BNN is based on an LSTM architecture but distinguishes testing. The Kolmogorov-Smirnov (KS) test is used
itself by incorporating Monte Carlo (MC) dropout during todetectchangesintheempiricaldistributionsofkey
174014 VOLUME13,2025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
TABLE5. Summaryofdeeplearningarchitecturesusedfordrift-awarelearning.
features, while the two-sample T-test evaluates shifts A. HYBRIDDRIFTDETECTION
infeaturemeansbetweentwotemporalsegments(typ- The performance of 4 Deep learning models(Bi-LSTM,
| ically | pre-drift | and post-drift |     | batches). | A statistically |     |            |     |      |        |        |                      |     |
| ------ | --------- | -------------- | --- | --------- | --------------- | --- | ---------- | --- | ---- | ------ | ------ | -------------------- | --- |
|        |           |                |     |           |                 |     | BNN, LSTM, | and | GRU) | with 3 | buffer | strategies(Adaptive, |     |
significant change in either test quantified via low FIFO and No-Buffer) with 3 Drift types(Abrupt, Gradual
p-valuesandlargeteststatistics—indicatesapotential and Recurring) with Hybrid drift detection mechanism is
driftpoint. summarized in the table 10. In the case of Abrupt Drift,
2) AccuracyDipCombinedwithStatisticalEvidence the Adaptive Buffer Strategy yields BiLSTM detecting
| In  | this hybrid | method, | drift | points | are flagged | by  |                       |     |     |           |           |       |     |
| --- | ----------- | ------- | ----- | ------ | ----------- | --- | --------------------- | --- | --- | --------- | --------- | ----- | --- |
|     |             |         |       |        |             |     | 4 drift points(figure |     | 6)  | with 0.73 | accuracy, | while | BNN |
tracking sudden declines in the model’s prediction (figure 7 performs slightly worse, detecting 2 drift points
accuracyovertime.Whenanotabledropinaccuracyis with 0.73 accuracy. GRU and LSTM have the best runtime
observed(relativetoarollingbaseline),statisticaltests performance,butGRU(figure9)detectsnodriftpoints,while
(KS or T-Test) are applied to the surrounding batches LSTM(figure8)detects2driftpointswithsimilaraccuracy.
| to  | confirm | distributional | change. | This | approach | com- |             |          |       |     |        |           |         |
| --- | ------- | -------------- | ------- | ---- | -------- | ---- | ----------- | -------- | ----- | --- | ------ | --------- | ------- |
|     |         |                |         |      |          |      | FIFO Buffer | Strategy | leads | to  | BiLSTM | detecting | 3 drift |
bines model-centric performance degradation with pointswith0.73accuracy,andBNNmaintainingaccuracybut
data-centric evidence to avoid false positives and withalowerdriftdetectioncount.GRUandLSTMperform
improvedetectionreliability. better in runtime efficiency, but BiLSTM shows the highest
3) Uncertainty-BasedDriftDetection driftdetectionwithslowerruntime.TheNoBufferStrategy
Thismethodleveragesmodeluncertaintyasasignalfor
|     |     |     |     |     |     |     | exhibits | better efficiency |     | for all | models, | with | BiLSTM |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | ------- | ------- | ---- | ------ |
drift.UsingMonteCarlodropout.Aspikeinepistemic detecting 3 drift points and performing with 0.73 accuracy.
uncertainty indicates that the model is encountering BiLSTM incurs the highest runtime in all buffer strategies,
| data | it is | less confident | about, | often | due to | a shift |     |     |     |     |     |     |     |
| ---- | ----- | -------------- | ------ | ----- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
especiallyinFIFO(32.85seconds)andNoBuffer(30.01sec-
in the underlying data distribution. If the uncertainty onds). The BNN model exhibits consistently high runtimes,
increase exceeds a threshold, a drift is declared. This particularly in Adaptive Buffer (23.79 seconds), indicating
approach is particularly useful in dynamic settings its computational cost for Bayesian inference. GRU and
wheredistributionalchangeisgradualorsubtle. LSTMarefasterandcomputationallyefficient,withruntimes
rangingbetween15.09and24.29seconds,dependingonthe
| X. RESULTSANDDISCUSSION |     |     |     |     |     |     | drifttypeandbufferstrategy. |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
This section discusses the performance of deep learning For Gradual Drift, BiLSTM detects 0 drift points with
models (Bi-LSTM, BNN, LSTM, and GRU) across three 0.77accuracyinAdaptiveBuffer,whileBNNperformsbetter
driftdetectionstrategiesusingadaptive,FIFO,andno-buffer with1driftpointdetectedat0.77accuracy.GRUandLSTM
| incremental | learning | frameworks. |     | The evaluation |     | metrics |     |     |     |     |     |     |     |
| ----------- | -------- | ----------- | --- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
showbetterdriftdetectionwith1driftpointeach,achieving
include accuracy, precision, recall, F1-score, AUC, and 0.77accuracyand0.84AUCinAdaptiveBuffer.FIFOBuffer
the number of detected drift points, serving to quantify Strategyagainincreasescomplexity,withBiLSTMdetecting
bothpredictiveeffectivenessandadaptabilityunderdynamic 1 drift point and BNN detecting 1 with 0.77 accuracy.
clinical data streams. The experimentation is done in three LSTM and GRU show strong results with good accuracy.
driftdetectionverticals;theyare,
NoBufferStrategymaintainsconsistentperformanceacross
1) Hybrid Drift Detection: Combines error rate drops all models with 0.77 accuracy but achieves faster runtimes
withstatisticalvalidation. compared to the buffer strategies. BiLSTM experiences the
2) StatisticalTest-BasedDetection:UsesKS-TestandT- longest runtimes in FIFO (49.1 seconds) and No Buffer
Testtodetectdistributionalshifts. (32.68 seconds), while BNN shows higher runtimes in
3) Uncertainty-Based Detection: Leverages predictive both buffer strategies (233.02 seconds). GRU and LSTM
variancefromBayesianmodelsfordriftidentification. havebetterruntimeefficiency,particularlyintheNoBuffer
The subsections below examine each of these vertical Strategy, where GRU takes 22.92 seconds and LSTM takes
experimentationfindingsindetail. 25.92 seconds. The Adaptive Buffer Strategy results in
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 174015 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
moderateruntimes,withBiLSTMat22.45secondsandGRU
at15.28seconds.
| In the      | case  | of Recurring | Drift,           | BiLSTM | detects | 2 drift     |     |     |     |     |
| ----------- | ----- | ------------ | ---------------- | ------ | ------- | ----------- | --- | --- | --- | --- |
| points with | 0.80  | accuracy     | and              | 0.85   | AUC in  | Adaptive    |     |     |     |     |
| Buffer,     | while | BNN performs | similarly        |        | with 1  | drift point |     |     |     |     |
| detected.   | GRU   | shows        | high performance |        | with 1  | drift point |     |     |     |     |
and0.80accuracyinAdaptiveBuffer.FIFOBufferStrategy
| increases     | complexity, | with           | BiLSTM         | detecting | 2 drift        | points      |     |     |     |     |
| ------------- | ----------- | -------------- | -------------- | --------- | -------------- | ----------- | --- | --- | --- | --- |
| and achieving |             | 0.80 accuracy. | GRU            | and       | LSTM show      | strong      |     |     |     |     |
| performance,  |             | with LSTM      | achieving      | 0.80      | accuracy       | across      |     |     |     |     |
| all buffer    | types.      | No Buffer      | Strategy       |           | performs       | efficiently |     |     |     |     |
| with BiLSTM   |             | detecting      | 2 drift        | points    | and performing |             |     |     |     |     |
| with 0.80     | accuracy    | in             | 33.37 seconds. |           | BiLSTM         | and BNN     |     |     |     |     |
| continue      | to show     | high           | runtime        | costs     | in the FIFO    | Buffer      |     |     |     |     |
| Strategy,     | with        | BiLSTM         | taking         | 66.09     | seconds        | and BNN     |     |     |     |     |
taking246.15seconds.GRUandLSTMperformwithhigher
| efficiency | in the | FIFO | Buffer | Strategy, | with runtimes | of  |     |     |     |     |
| ---------- | ------ | ---- | ------ | --------- | ------------- | --- | --- | --- | --- | --- |
47.06secondsforGRUand56.12secondsforLSTM.InNo FIGURE7. PerformanceofBNNwithhybriddriftdetectionusingadaptive
Buffer,BiLSTMtakes33.37seconds,whileGRUandLSTM buffering:Accuracytrend(abrupt).
| have faster | runtimes | of  | 22.06 seconds |     | and 20.28 | seconds, |     |     |     |     |
| ----------- | -------- | --- | ------------- | --- | --------- | -------- | --- | --- | --- | --- |
respectively.
Acrossallthetypesofdrift,theAdaptiveBufferStrategy
| and FIFO | Buffer | Strategy | consistently |     | provide | better drift |     |     |     |     |
| -------- | ------ | -------- | ------------ | --- | ------- | ------------ | --- | --- | --- | --- |
detectionandaccuracy,particularlyforgradualandrecurring
drifts.TheNoBufferStrategyresultsinlowerperformance,
especiallyforabruptdrift,wheredriftdetectionandaccuracy
| are compromised. |     | BiLSTM | and | BNN | are the most | robust |     |     |     |     |
| ---------------- | --- | ------ | --- | --- | ------------ | ------ | --- | --- | --- | --- |
models,showingstableperformanceacrossalldrifttypesand
| strategies, | while | GRU | tends to | underperform, | especially | in  |     |     |     |     |
| ----------- | ----- | --- | -------- | ------------- | ---------- | --- | --- | --- | --- | --- |
detectingdrifts.
FIGURE8. PerformanceofLSTMwithhybriddriftdetectionusing
adaptivebuffering:Accuracytrend(abrupt).
andRecurring)withExternaldriftdetectionusingKS-testis
summarizedinthetable11.
IntheAbruptDriftscenario,theAdaptiveBufferStrategy
|     |     |     |     |     |     |     | yields the | best results, with | BiLSTM(figure | 10) detecting |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | ------------- | ------------- |
18driftpointsandachievinganaccuracyof0.73,maintaining
|     |     |     |     |     |     |     | good precision | and recall. | The GRU(figure | 13) model also |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- | -------------- | -------------- |
performswellwith18driftpointsdetectedandslightlyhigher
FIGURE6. PerformanceofBiLSTMwithhybriddriftdetectionusing accuracy (0.74). The BNN(figure 12) model detects fewer
adaptivebuffering:Accuracytrend(abrupt). driftpoints(15)andmaintainssimilaraccuracytoBiLSTM
|     |     |     |     |     |     |     | (0.73). LSTM(figure | 11) | performs slightly | worse, detecting |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ----------------- | ---------------- |
13driftpointswithanaccuracyof0.73.IntheFIFOBuffer
B. STATISTICALTEST-BASEDDRIFTDETECTION Strategy, drift detection is lower, with BiLSTM detecting
The performance of 4 Deep learning models(Bi-LSTM, 12 drift points and an accuracy of 0.72. The GRU model
BNN, LSTM, and GRU) with 3 buffer strategies(Adaptive, performssimilarly,detecting12driftpointsandmaintaining
FIFO and No-Buffer) with 3 Drift types(Abrupt, Gradual 0.73 accuracy, while LSTM detects 15 drift points with
| 174016 |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
ForRecurringDrift,theAdaptiveBufferStrategyprovides
|     |     |     |     |     |     |     |     | the highest | performance     | across | all models, | with           | BiLSTM |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------- | ------ | ----------- | -------------- | ------ |
|     |     |     |     |     |     |     |     | detecting   | 17 drift points | and    | achieving   | 0.80 accuracy. | The    |
BNNmodelperformssimilarly,detecting18driftpointsand
|     |     |     |     |     |     |     |     | achieving | the same accuracy |     | of 0.80. GRU | and | LSTM also |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | --- | ------------ | --- | --------- |
showstrongperformance,detecting14to16driftpointswith
0.80accuracy.IntheFIFOBufferStrategy,BiLSTMdetects
|     |     |     |     |     |     |     |     | 14 drift          | points with 0.80     | accuracy, | while           | BNN       | and LSTM      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | -------------------- | --------- | --------------- | --------- | ------------- |
|     |     |     |     |     |     |     |     | perform           | similarly, detecting |           | 15 drift points | and       | maintaining   |
|     |     |     |     |     |     |     |     | 0.81 accuracy.    | GRU                  | performs  | slightly        | worse,    | with 13 drift |
|     |     |     |     |     |     |     |     | points detected   | and 0.80             | accuracy. | The             | No Buffer | Strategy      |
|     |     |     |     |     |     |     |     | yields comparable | performance          |           | with 0.80       | accuracy  | across        |
allmodels.BiLSTM,BNN,andLSTMdetect14to16drift
points,whileGRUdetects17driftpointswithslightlylower
|     |     |     |     |     |     |     |     | performance     | in precision | and    | recall.         | BiLSTM | incurs the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | ------ | --------------- | ------ | ---------- |
|     |     |     |     |     |     |     |     | highest runtime | in FIFO      | Buffer | (84.7 seconds), |        | while BNN  |
andLSTMtake55.97and56.12seconds,respectively.GRU
FIGURE9. PerformanceofGRUwithhybriddriftdetectionusingadaptive performsbetter,with47.06secondsinFIFO.IntheNoBuffer
buffering:Accuracytrend(abrupt). Strategy,BiLSTMandBNNexhibitgoodruntimeefficiency
(55.59and35.4seconds),whileGRUandLSTMarefaster,
taking29.48and31.35seconds,respectively.
IncaseofStatisticaltestbaseddriftdetectionmechanism,
0.73accuracy.FortheNoBufferStrategy,BiLSTMperforms GRU and LSTM are the most computationally efficient
the best, detecting 22 drift points with 0.81 accuracy, while modelsacrossthedrifttypes,providingareasonablebalance
GRUandLSTMperformsimilarlybutwithfewerdriftpoints between accuracy and runtime. The No Buffer Strategy
detected. BNN incurs the highest runtime, particularly in offers the best runtime efficiency, especially with GRU and
the Adaptive Buffer strategy (27.67 seconds), while GRU LSTM, but at the expense of some drift detection accuracy
and LSTM have faster runtimes of 23.25 seconds and inGradualandRecurringdrifts.BiLSTMandBNNofferthe
19.96seconds,respectively.TheFIFOBufferstrategyleads highestaccuracy,especiallyformorecomplexdrifttypeslike
tolongerruntimes,especiallyforBiLSTM(35.28seconds). AbruptandRecurringbutincursignificantlyhigherruntimes,
NoBufferStrategyoffersthemostcomputationalefficiency, particularly with the FIFO Buffer strategy. FIFO Buffer
withBiLSTMtaking22secondsandGRUandLSTMtaking Strategy tends to increase runtime considerably, especially
lessthan15seconds. withBiLSTMandBNN,makingitlesssuitableforreal-time
For Gradual Drift, the Adaptive Buffer Strategy again applications but beneficial in scenarios where accuracy is
delivers good results. BiLSTM detects 15 drift points prioritizedoverspeed.TheAdaptiveBufferStrategyprovides
with an accuracy of 0.78, while BNN detects the same abalancebutstillrequiresmoderateruntime,withBiLSTM
number of drift points with accuracy remaining at 0.78. performingthebestinaccuracyanddriftdetection.
| GRU detects      | 18           | drift points |           | but performs |              | slightly      | worse |     |     |     |     |     |     |
| ---------------- | ------------ | ------------ | --------- | ------------ | ------------ | ------------- | ----- | --- | --- | --- | --- | --- | --- |
| in accuracy      | (0.76).      | LSTM         | shows     | similar      | performance  |               | to    |     |     |     |     |     |     |
| the other        | models,      | detecting    | 16        | drift        | points       | and achieving |       |     |     |     |     |     |     |
| 0.78 accuracy.   |              | In the FIFO  | Buffer    | Strategy,    |              | BiLSTM        | and   |     |     |     |     |     |     |
| BNN both         | achieve      | 0.78         | accuracy, | with         | BiLSTM       | detecting     |       |     |     |     |     |     |     |
| 15 drift         | points       | and BNN      | detecting |              | 18 drift     | points.       | The   |     |     |     |     |     |     |
| GRU model,       | in           | FIFO,        | detects   | fewer        | drift points | (13)          | but   |     |     |     |     |     |     |
| maintains        | accuracy     | at 0.78.     | LSTM      | also         | performs     | similarly     |       |     |     |     |     |     |     |
| with 15          | drift points | detected     | and       | 0.78         | accuracy.    | In the        | No    |     |     |     |     |     |     |
| Buffer Strategy, |              | all models   | perform   | well         | with         | an accuracy   |       |     |     |     |     |     |     |
| of 0.80.         | BiLSTM,      | BNN,         | and LSTM  | perform      |              | similarly     | with  |     |     |     |     |     |     |
| 14 to 16         | drift points | detected,    |           | while        | GRU detects  | 17            | drift |     |     |     |     |     |     |
pointsbutmaintains0.80accuracy.GRUshowstheshortest FIGURE10. PerformanceofBiLSTMwithKS-testbaseddriftdetection
usingadaptivebuffering:Accuracytrend(abrupt).
| runtime      | of 11.89  | seconds  | in the         | Adaptive | Buffer | Strategy, |        |     |     |     |     |     |     |
| ------------ | --------- | -------- | -------------- | -------- | ------ | --------- | ------ | --- | --- | --- | --- | --- | --- |
| while BiLSTM |           | takes    | 22.45          | seconds. | The    | FIFO      | Buffer |     |     |     |     |     |     |
| Strategy     | increases | runtimes | significantly, |          | with   | BiLSTM    | at     |     |     |     |     |     |     |
49.1 seconds and BNN at 28.14 seconds. The No Buffer C. UNCERTAINTYBASEDDRIFTDETECTION
Strategyprovidesagoodtrade-off,withGRUperformingin The performance of 4 Deep learning models(Bi-LSTM,
14-15secondsandLSTMtaking20.39seconds. BNN, LSTM, and GRU) with 3 buffer strategies(Adaptive,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 174017 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
accuracyof0.73buthasahigherruntimeof50.42seconds,
reflectingtheaddedcomplexityofmaintainingaFIFObuffer.
BNN continues to show high runtime (363.45 seconds),
confirming its computationally expensive nature. GRU and
LSTMshowlowerruntime,withGRUtaking26.21seconds
and LSTM 37.79 seconds, indicating that these models are
moreefficientinhandlingdriftdetectionwithabuffer.Inthe
No Buffer Strategy, BiLSTM detects 18 drift points with
0.73accuracyin36.26seconds,whileGRUandLSTMshow
fasterruntime(17.95and26.92seconds,respectively),with
GRU showing good performance despite fewer drift points
FIGURE11. PerformanceofLSTMwithKS-testbaseddriftdetectionusing
detected.
adaptivebuffering:Accuracytrend(abrupt).
For Gradual Drift, the Adaptive Buffer Strategy provides
good performance with BiLSTM detecting 17 drift points
with 0.78 accuracy and 0.76 F1-score. BNN, however,
detects fewer drift points (9) and has lower accuracy (0.69)
and runtime (233.02 seconds), indicating that Bayesian
models are less efficient for gradual drift detection. GRU
detects 15 drift points with 0.77 accuracy, while LSTM
shows slightly better performance with 20 drift points
detected and 0.77 accuracy. The FIFO Buffer Strategy
againresultsinlongerruntime,especiallyforBiLSTMwith
60.73 seconds, compared to BNN and GRU, which have
307.21 seconds and 358.51 seconds runtimes, respectively.
LSTM performs similarly to BiLSTM, with 20 drift points
FIGURE12. PerformanceofBNNwithKS-testbaseddriftdetectionusing
adaptivebuffering:Accuracytrend(abrupt). detected and 0.78 accuracy, but with a more reasonable
runtime (49.89 seconds). The No Buffer Strategy shows
betterefficiency,withBiLSTMdetecting17driftpointsand
achieving 0.77 accuracy in 33.93 seconds, while GRU and
LSTM show good performance with runtime of 17.95 and
26.92seconds,respectively.
For Recurring Drift, the Adaptive Buffer Strategy results
inBiLSTMdetecting19driftpointswith0.80accuracyand
0.86 AUC in 33.45 seconds, while BNN again shows lower
accuracy(0.69)andruntime(233.01seconds).GRUperforms
similarly, detecting 15 drift points with 0.80 accuracy and
0.85 AUC, and LSTM achieves 0.80 accuracy with 21 drift
points detected. The FIFO Buffer Strategy increases the
runtime significantly, especially for BiLSTM (66.09 sec-
FIGURE13. PerformanceofGRUwithKS-testbaseddriftdetectionusing
adaptivebuffering:Accuracytrend(abrupt). onds), BNN (246.15 seconds), and GRU (294.67 seconds).
LSTM continues to perform well with 20 drift points
detectedand0.81accuracyin46.95seconds.TheNoBuffer
FIFO and No-Buffer) with 3 Drift types(Abrupt, Gradual Strategy results in 0.80 accuracy across all models, with
and Recurring) with uncertainty based drift detection is BiLSTM detecting 17 drift points in 36.18 seconds. GRU
summarizedinthetable12. andLSTMcontinuetoshowfastruntime,withGRUtaking
IntheAbruptDriftscenario,theAdaptiveBufferStrategy 20.92secondsandLSTMat25.75seconds.
shows BiLSTM(figure 14) detecting 14 drift points with an The No Buffer Strategy offers the lowest computational
accuracy of 0.73, while GRU(figure 17) performs slightly overhead and quickest runtime, making it ideal for applica-
better, detecting 19 drift points and achieving an accuracy tions where speed is crucial, though it may sacrifice some
of 0.72. BNN(figure 15) performs worse, detecting 9 drift accuracyindriftdetection.TheAdaptiveBufferStrategypro-
pointsandhavinganaccuracyof0.7,withitscomputational videsagoodbalanceofdriftdetectionandruntime,withGRU
complexity reflected in a significantly higher runtime of andLSTMbeingmorecomputationallyefficientcomparedto
233.01 seconds. LSTM(figure 16) performs similarly to BiLSTMandBNN.BNN,whileaccurate,iscomputationally
BiLSTM, detecting 21 drift points with 0.73 accuracy, and expensive and should be used in environments where high
theruntimeismoderateat24.48seconds.IntheFIFOBuffer accuracy justifies the additional time complexity. The FIFO
Strategy, BiLSTM detects 17 drift points and maintains an Buffer Strategy, though useful for improved drift detection,
174018 VOLUME13,2025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
introducessignificantcomputationaloverhead,especiallyfor
| BiLSTM | and BNN, making | it less practical | for real-time |     |     |     |     |     |     |     |     |
| ------ | --------------- | ----------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
systems.
|     |     |     |     | FIGURE17. | PerformanceofGRUwithuncertaintybaseddriftdetection |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
usingadaptivebuffering:Accuracytrend(abrupt).
1) ABLATIONSTUDYONHYBRIDDRIFTDETECTIONWITH
FIGURE14. PerformanceofBiLSTMwithUncertaintybasedDrift ADAPTIVEBUFFERING
detectionusingadaptivebuffering:Accuracytrend(abrupt). ThefirststudyfocusesontheHybridDriftDetectionmethod
|     |     |     |     | combined           | with      | adaptive     | buffering.  | The             | goal | is to    | evaluate  |
| --- | --- | --- | --- | ------------------ | --------- | ------------ | ----------- | --------------- | ---- | -------- | --------- |
|     |     |     |     | how different      | aspects   |              | of the      | drift detection |      | process, | such      |
|     |     |     |     | as drift-triggered |           | buffering,   | retraining, |                 | and  | drift    | detection |
|     |     |     |     | mechanisms         | (KS-test, | error-rate), |             | affect          | the  | model’s  | ability   |
todetectandadapttodrift.
DescriptionofAblations:Thefollowingaretheablations
|     |     |     |     | taken for | study | and its | interpretation |     | as summarized |     | in the |
| --- | --- | --- | --- | --------- | ----- | ------- | -------------- | --- | ------------- | --- | ------ |
table6,
1) B1(BaseLine):Allfeaturesareenabled:drift-triggered
|     |     |     |     | buffering, |     | retraining, | and | the | use of | the KS-test | for |
| --- | --- | --- | --- | ---------- | --- | ----------- | --- | --- | ------ | ----------- | --- |
detectingdrift.
2) B2:Drift-triggeredbufferingisdisabled,meaningdrift
isaddedtothebufferonlywhendetected
| FIGURE15. | PerformanceofBNNwithuncertaintybaseddriftdetection |     |     |        |        |            |     |           |     |           |      |
| --------- | -------------------------------------------------- | --- | --- | ------ | ------ | ---------- | --- | --------- | --- | --------- | ---- |
|           |                                                    |     |     | 3) B3: | Buffer | retraining | is  | disabled, | and | the model | does |
usingadaptivebuffering:Accuracytrend(abrupt).
notretrainoncedriftisdetected
|     |     |     |     | 4) B4: | The KS-test |     | is disabled, | and | the model | uses | only |
| --- | --- | --- | --- | ------ | ----------- | --- | ------------ | --- | --------- | ---- | ---- |
error-ratemethodstodetectdrift
TheB1configurationisthereferencepointforcomparison,
|     |     |     |     | and we | observe | how | disabling | each | component |     | affects |
| --- | --- | --- | --- | ------ | ------- | --- | --------- | ---- | --------- | --- | ------- |
performance.
|     |     |     |     | Table          | 13 summarizes |               | the findings |          | of the       | 4 ablations | for     |
| --- | --- | --- | --- | -------------- | ------------- | ------------- | ------------ | -------- | ------------ | ----------- | ------- |
|     |     |     |     | hybrid drift   | detection     | for           | the          | adaptive | buffer       | strategy    | with    |
|     |     |     |     | Deep learners. |               | The following |              | are the  | key insights |             | learned |
throughthisablationstudyoneachdrifttype.
|     |     |     |     | • Abrupt | Drift:     | In             | the case | of       | Abrupt      | Drift, | the Base  |
| --- | --- | --- | --- | -------- | ---------- | -------------- | -------- | -------- | ----------- | ------ | --------- |
|     |     |     |     | Line     | (B1)       | configuration, |          | with all | components  |        | enabled,  |
|     |     |     |     | yielded  | consistent |                | results  | across   | all models, |        | including |
BiLSTM,BNN,GRU,andLSTM,withaccuracyaround
| FIGURE16. | PerformanceofLSTMwithUncertaintybaseddriftdetection |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
usingadaptivebuffering:Accuracytrend(abrupt).
|     |     |     |     | 0.73 | and AUC | at    | 0.78. The | runtime | varied, | with  | BiL-     |
| --- | --- | --- | --- | ---- | ------- | ----- | --------- | ------- | ------- | ----- | -------- |
|     |     |     |     | STM  | taking  | 24.29 | seconds,  | and     | LSTM    | being | slightly |
fasterat15.09seconds.WhenDrift-triggeredBuffering
D. ABLATIONSTUDYONDRIFTDETECTIONMETHODS wasdisabledinB2,theruntimeincreasedsignificantly
This section presents the ablation studies conducted for (e.g.,BiLSTMtook145.01seconds),buttheAccuracy
two different drift detection techniques used in our experi- and AUC improved to 0.82 and 0.87, respectively.
ments:Hybrid Drift Detection and Uncertainty-Based Drift DisablingBufferRetraining(B3)resultedinamoderate
Detection. These studies aim to isolate and evaluate the decreaseinaccuracy(0.81)butsignificantlyreducedthe
impactofdifferentcomponentsofthedriftdetectionmethods runtime(e.g.,BiLSTMat15.7seconds).Lastly,inB4,
on overall performance, accuracy, and computational effi- when KS-test was replaced with the error-rate method,
| ciency.       |     |     |     | themodelsexhibitedconsistentperformancesimilarto |     |     |     |     |     |     |        |
| ------------- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------ |
| VOLUME13,2025 |     |     |     |                                                  |     |     |     |     |     |     | 174019 |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
TABLE6. Ablationstudyonhybriddriftdetectionwithadaptivebuffering.
the baseline, with Accuracy around 0.81 and AUC at examineshowdifferentconfigurationsofMCDropout,buffer
0.86,whiletheruntimedecreasedincomparisontoB2. updates,andretrainingaffectthedriftdetectionprocess.
• Gradual Drift: For Gradual Drift, the Base Line (B1) DescriptionofAblations:Thefollowingaretheablations
configuration again provided strong performance, with for Uncertainty based drift detection with adaptive buffers
Accuracy ranging from 0.77 to 0.78 and AUC at taken for study and its interpretation as summarized in the
0.84. The runtime for models like GRU and LSTM table7,
rangedbetween15.28and16.12seconds.InB2,where 1) U1(BaseLine):Thisconfigurationservesasthebase,
Drift-triggered Buffering was disabled, the Accuracy with an uncertainty threshold of 20 samples. Buffer
improved slightly to 0.79, and AUC reached 0.85, but updates and retraining are performed only when drift
theruntimeincreasedsignificantly,withBiLSTMtaking is detected, ensuring that the model adapts when drift
77.42seconds.DisablingBufferRetraining(B3)ledto occursbutwithoutconstantretrainingorupdates.
aminorperformancedip,withaccuracyaround0.78for 2) U2(ContinuousUpdatesandRetraining):Inthissetup,
BiLSTM, and the runtime dropped to 17.85 seconds. there is no uncertainty threshold (disabled), and both
InB4,whenKS-testwasexcluded,Accuracydecreased buffer updates and retraining occur every batch. This
slightly to 0.79, and AUC maintained at 0.85, with configuration tests the impact of continuous updates
runtimeforBiLSTMdecreasingto23.87seconds. andretraining,whichmayresultinhighcomputational
• Recurring Drift: For Recurring Drift, the Base Line costs without necessarily improving the detection of
(B1) configuration provided high Accuracy at 0.8 and drift.
AUC at 0.85. Models like BiLSTM and GRU per- 3) U3 (Reduced Sensitivity): By setting the uncertainty
formed well, with runtime around 25.65 seconds for threshold to 1 sample, this configuration lowers the
BiLSTM and 15.51 seconds for LSTM. In B2, where sensitivity of drift detection. The buffer updates and
Drift-triggeredBufferingwasdisabled,theperformance retrainingstilloccurondriftdetection,butthereduced
decreased, particularly for BiLSTM, with Accuracy threshold may cause the model to miss subtle drifts,
dropping to 0.74, but the AUC remained at 0.78. leading to lower performance in detecting gradual
This configuration resulted in a significant runtime changes.
increase (e.g., BiLSTM at 79.67 seconds). B3, which 4) U4 (No Buffer Update and No Retraining): This con-
disabled Buffer Retraining, showed reduced runtime figurationusesanuncertaintythresholdof20samples
(e.g.,BiLSTMat28.15 seconds),buttheAccuracyfor for drift detection but disables both buffer updates
BiLSTMwasstilllower(0.73)thaninB1.Finally,inB4, and retraining. Without any adaptation mechanisms,
where KS-test was excluded, the models exhibited a the model may struggle to adjust to changing data
slight reduction in Accuracy and AUC (e.g., BiLSTM distributions, resulting in decreased drift detection
at 0.73 and 0.77, respectively), but still maintained effectiveness.
reasonable performance with runtime ranging from 5) U5 (Frequent Buffer Updates): Here, the uncertainty
24.29to44.2seconds. threshold remains at 20 samples, with buffer updates
ThisablationstudyonHybridDriftDetectionshowsthat occurring every batch. Retraining is only performed
Drift-triggeredBuffering(B2)significantlyimprovesAccu- on drift detection. This configuration examines the
racy but incurs a substantial computational cost, increasing impact of frequent buffer updates on performance
runtime. On the other hand, Buffer Retraining (B3) reduces whilerestrictingretrainingtodriftdetectionevents.
computationaltimebutleadstoaslightdropinperformance. Table 14 summarizes the findings of the 4 ablations for
Excluding the KS-test (B4) results in a modest reduction in uncertaintybaseddriftdetectionforadaptivebufferstrategy
accuracyandAUC,thoughitstilloffersatrade-offbetween with Deep learners. The following are the key insights
performanceandruntimeefficiency. learned through this ablation study on each drift type using
uncertaintybaseddriftdetectionmethod.
E. ABLATIONSTUDYONUNCERTAINTY-BASEDDRIFT • Abrupt Drift: In the Abrupt Drift scenario, the U1
DETECTION configuration (Uncertainty threshold with 20 samples,
The second study focuses on the Uncertainty-Based Drift bufferupdateandretrainingondrift)showedrelatively
Detection method, which relies on Monte Carlo (MC) consistent performance across models. BiLSTM and
Dropout for uncertainty estimation. The ablation study LSTM both achieved Accuracy values of 0.73, with
174020 VOLUME13,2025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
TABLE7. Ablationstudyonuncertainty-baseddriftdetection.
AUC at 0.78 and moderate runtime around 28.5 and runtime remaining low (e.g., 15.42 seconds for GRU).
24.48seconds,respectively.TheBNNmodel,however, The U4 configuration, with uncertainty-based updates
performedpoorlywithAccuracydroppingto0.7anda on drift and retraining, showed similar performance to
significantlyhigherruntimeof233.01seconds.TheU2 U3,maintainingAccuracyat0.73forBiLSTMandAUC
configuration,whereretrainingoccurredoneverybatch, at0.77,withruntimearound31.96secondsforBiLSTM.
yielded significant improvements in Accuracy (around Finally, in U5, when both batch updates and retraining
0.82)andAUC(0.86)acrossallmodels,withBiLSTM were enabled, performance was slightly lower (e.g.,
showing the highest runtime of 86.93 seconds. The AccuracyforBiLSTMat0.71)butstillacceptable,with
U3 configuration, with the uncertainty threshold and runtimebeingthehighestat43.2secondsforBiLSTM.
bufferupdateonlyondrift,displayedstableperformance This ablation study highlights the effects of different
withAccuracyaround0.81andlowerruntimeforGRU configurations in Uncertainty-based Drift Detection. The
(13.6seconds)andLSTM(11.59seconds).InU4,when best overall performance was observed in U2, where both
buffer retraining was disabled, performance remained the buffer update occurred on drift and retraining was
closetoU2,butruntimewassignificantlyreduced(e.g., performed, leading to high Accuracy and AUC for all
BiLSTMat39.57seconds).Finally,inU5,whereboth models.However,thiscameatthecostofincreasedruntime,
the buffer update occurred every batch and retraining particularly for BiLSTM. The U3 configuration, which
wasperformedondrift,theAccuracyremainedaround utilized uncertainty-based updates only on drift, achieved
0.81,buttheruntimeincreasedslightlyforBiLSTMto good performance with reduced runtime, especially for
63.84seconds. models like GRU and LSTM. Finally, the U4 and U5
• Gradual Drift: For Gradual Drift, U1 exhibited configurationsprovidedtrade-offsbetweenperformanceand
consistent performance across models, with BiLSTM computationalcost,withU4beingthemostbalancedoption
achieving Accuracy of 0.78 and AUC at 0.84, with intermsofruntimeandperformance.
moderateruntimerangingfrom22.45to25.84seconds.
U2(bufferupdateondrift)showedimprovedAccuracy F. DRIFTMAGNITUDESTUDY
(ranging from 0.79 to 0.80) and AUC (0.85) across In this section, we analyze the impact of varying drift
all models, but the runtime increased substantially for magnitudes (20%, 50%, 80%, and 100% flips) on different
BiLSTM(108seconds).U3sawaperformancedropin drift detection methods: Hybrid Approach, Uncertainty-
Accuracy for BNN to 0.79, but the runtime remained based Drift Detection, and KS-Test-based Drift Detection.
relatively low for GRU (8.26 seconds) and LSTM The goal is to observe how different models respond to the
(8.32seconds).InU4,theperformancewasstablewith severityoftheinduceddriftandhowtheseadjustmentsaffect
Accuracy remaining around 0.79, but the runtime was performancemetrics,includingAccuracy,Precision,Recall,
notablyreduced(e.g.,BiLSTMat24.98seconds).InU5, F1-Score,AUC,andCPUTime.
which had both batch-wise updates and retraining, The drift is introduced by flipping a certain percentage
the models showed slightly decreased Accuracy (e.g., of the dataset’s labels, and the models are evaluated under
0.75 for BiLSTM) but maintained AUC at 0.85, with these varying conditions. By comparing these performance
runtime ranging from 35.46 seconds for BiLSTM to metrics across different drift magnitudes, we can gauge
18.18secondsforGRU. the robustness and efficiency of each detection method in
• Recurring Drift: In the Recurring Drift scenario, U1 handling abrupt, gradual, and recurring concept drift types.
exhibited high Accuracy at 0.8 and AUC at 0.86, with Table15summarizesthefindingsofthedriftmagnitudestudy
GRU and LSTM showing reasonable runtime perfor- against the various drift detection methods using adaptive
mance(e.g.,24.12and27.06seconds,respectively).The bufferingstrategy.
U2configurationsawasignificantdecreaseinAccuracy • Abrupt Drift: For Abrupt Drift, the Hybrid Approach
(around 0.74) and AUC at 0.78, but the performance demonstratedthatBiLSTMisthemostefficientmodel,
was stable across models with runtime varying from achieving the highest Accuracy of 0.94 for a 20% flip
79.67secondsforBiLSTMto56.15secondsforLSTM. with a moderate CPU Time of 5.5 seconds. As the
In U3, performance was consistently maintained, with drift magnitude increased, the Accuracy decreased,
Accuracy for BiLSTM at 0.73 and AUC at 0.77, and reaching 0.81 for a 100% flip, but still maintaining
VOLUME13,2025 174021

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
solid performance. The GRU and LSTM models also TABLE8. Brierscoreanalysisandcalibrationofuncertaintyindeep
| exhibited     | similar          | patterns,   |      | where       | Accuracy | gradually     | learners. |     |     |     |     |     |     |
| ------------- | ---------------- | ----------- | ---- | ----------- | -------- | ------------- | --------- | --- | --- | --- | --- | --- | --- |
| dropped,      | but their        | Performance |      | remained    |          | competitive,  |           |     |     |     |     |     |     |
| with Accuracy |                  | ranging     | from | 0.74        | to 0.75  | in the worst  |           |     |     |     |     |     |     |
| case. These   | results          | highlight   |      | that the    | Hybrid   | Approach      |           |     |     |     |     |     |     |
| retains       | high performance |             |      | in handling |          | Abrupt Drift, |           |     |     |     |     |     |     |
withBiLSTMshowingthemostconsistentandreliable
| results               | across   | all levels | of    | drift.       | For    | Abrupt Drift, |     |     |     |     |     |     |     |
| --------------------- | -------- | ---------- | ----- | ------------ | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
| the Uncertainty-based |          |            | Drift | Detection    | method | showed        |     |     |     |     |     |     |     |
| that BiLSTM           | achieved |            | solid | performance, |        | maintaining   |     |     |     |     |     |     |     |
Accuracyat0.87fora20%flipanddroppingto0.80for
|     |     |     |     |     |     |     | effective | for Recurring |     | Drift, | the performance |     | of the |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | ------ | --------------- | --- | ------ |
a100%flip.However,BNNdemonstratedasubstantial
modelsdeclinesasthedriftmagnitudebecomessevere,
performance drop in Accuracy, starting from 0.9 at a although BiLSTM remains the most stable model.
20%flipanddecreasingto0.83at100%drift,coupled
|     |     |     |     |     |     |     | For Recurring |     | Drift, | BiLSTM | continued | to  | perform |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | ------ | --------- | --- | ------- |
with high CPU Time (around 220 seconds). The GRU consistentlywellacrossdifferentdriftmagnitudes,with
andLSTMmodelsshowedmorestableperformancein Accuracy starting at 0.86 and dropping to 0.73 for
termsofAccuracybutexperiencedmoderatedecreases
|     |     |     |     |     |     |     | the 100% | flip. | Similarly, | LSTM | performed |     | well at |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ---------- | ---- | --------- | --- | ------- |
as the drift magnitude increased. The CPU Time for 0.81 for 20% drift and slightly decreased to 0.73 at
| Uncertainty-based |     | Drift | Detection |     | was | significantly |      |        |         |       |           |             |     |
| ----------------- | --- | ----- | --------- | --- | --- | ------------- | ---- | ------ | ------- | ----- | --------- | ----------- | --- |
|                   |     |       |           |     |     |               | 100% | drift. | The BNN | model | exhibited | significant |     |
highercomparedtotheHybridApproach,especiallyfor
|      |     |     |     |     |     |     | deterioration                                   |     | in performance |     | as the drift | magnitude |     |
| ---- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | -------------- | --- | ------------ | --------- | --- |
| BNN. |     |     |     |     |     |     | increased,withAccuracydroppingfrom0.89at20%flip |     |                |     |              |           |     |
• GradualDrift:InthecaseofGradualDrift,theHybrid
|     |     |     |     |     |     |     | to 0.72 | at 100% | flip, | along with | increased | CPU | Time. |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----- | ---------- | --------- | --- | ----- |
Approach showed thatBiLSTM and BNN modelsper- GRU performed similarly to LSTM, with a moderate
formedconsistentlywell,althoughCPUTimeincreased
|                |          |     |          |     |           |          | drop in           | Accuracy | and   | consistent | CPU       | Time. | Overall, |
| -------------- | -------- | --- | -------- | --- | --------- | -------- | ----------------- | -------- | ----- | ---------- | --------- | ----- | -------- |
| significantly. | BiLSTM’s |     | Accuracy |     | decreased | slightly |                   |          |       |            |           |       |          |
|                |          |     |          |     |           |          | Uncertainty-based |          | Drift | Detection  | performed | well  | but      |
from 0.86 at a 20% flip to 0.78 at a 100% flip, while at the cost of higher computational time, especially
| BNN followed                                |        | a similar | trend,    | with       | Accuracy | ranging  |                       |       |       |           |                |     |        |
| ------------------------------------------- | ------ | --------- | --------- | ---------- | -------- | -------- | --------------------- | ----- | ----- | --------- | -------------- | --- | ------ |
|                                             |        |           |           |            |          |          | for BNN,              | which | was   | less      | efficient than | the | Hybrid |
| from0.81to0.77.TheCPUTimeforthesemodelsalso |        |           |           |            |          |          | Approach.             |       |       |           |                |     |        |
| escalated                                   | as the | drift     | magnitude | increased, |          | with BNN |                       |       |       |           |                |     |        |
|                                             |        |           |           |            |          |          | The Uncertainty-based |       | Drift | Detection | method         |     | showed |
requiringthelongestprocessingtime.GRUandLSTM
robustperformanceacrossalldrifttypes,buttheCPUTime
| models, | though | less | efficient | in  | terms | of Accuracy |     |     |     |     |     |     |     |
| ------- | ------ | ---- | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
wasmuchhigher,particularlyforBNN.WhileBiLSTMwas
| (around     | 0.78        | for higher |            | drift magnitudes), |           | showed         |                    |             |          |              |                      |            |     |
| ----------- | ----------- | ---------- | ---------- | ------------------ | --------- | -------------- | ------------------ | ----------- | -------- | ------------ | -------------------- | ---------- | --- |
|             |             |            |            |                    |           |                | the most efficient |             | in terms | of Accuracy, | models               | like       | BNN |
| more stable | performance |            | but        | still faced        | increased | CPU            |                    |             |          |              |                      |            |     |
|             |             |            |            |                    |           |                | faced substantial  | performance |          | degradation  | with                 | increasing |     |
| Time as     | the drift   | severity   | increased. |                    | For       | Gradual Drift, |                    |             |          |              |                      |            |     |
|             |             |            |            |                    |           |                | drift magnitude    | and         | high     | CPU          | Time. In comparison, |            | the |
BiLSTMmaintainedhighAccuracy(0.87)at20%drift
|             |     |      |     |      |            |           | Hybrid Approach | was | more | efficient | with balanced |     | perfor- |
| ----------- | --- | ---- | --- | ---- | ---------- | --------- | --------------- | --- | ---- | --------- | ------------- | --- | ------- |
| and dropped | to  | 0.77 | for | 100% | flip, with | a similar |                 |     |      |           |               |     |         |
manceintermsofbothAccuracyandCPUTime,especially
| trend observed |     | in LSTM. |     | The BNN | model | struggled |     |     |     |     |     |     |     |
| -------------- | --- | -------- | --- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
forAbruptDrift.
significantly,withAccuracystartingat0.9forthe20%
flipbutdroppingto0.77forthe100%flip,accompanied
by high CPU Time. GRU displayed more stability, G. CALIBRATIONSTUDYONUNCERTAINTYBASEDDRIFT
| though | its Accuracy |     | was lower | compared |     | to BiLSTM | DETECTION |     |     |     |     |     |     |
| ------ | ------------ | --- | --------- | -------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- |
and LSTM, starting at 0.86 for 20% flip and declining Calibrationplaysacriticalroleinensuringthatdeeplearning
to 0.78 for 100% flip. The increased CPU Time for models produce reliable predicted probabilities that align
BNN indicates that this model struggles under higher well with actual outcomes, especially when dealing with
drift magnitudes, making it less suitable for real-time uncertainty in concept drift detection. In this study, deep
applicationsinsuchscenarios. learning models such as BiLSTM, BNN, GRU, and LSTM
• Recurring Drift: For Recurring Drift, the Hybrid are utilized for uncertainty estimation, and their predicted
Approach showed that BiLSTM continued to outper- probabilitiesarecalibratedtoimprovedecision-makingunder
| formtheothermodels,withAccuracystartingat0.86for |     |     |     |     |     |     | driftconditions. |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
lower drift levels but dropping to 0.72 as the drift The calibration curve, also known as the reliability dia-
magnitudereached100%.TheGRUandLSTMmodels gram,providesavisualtooltoassesshowwellthepredicted
exhibited the most significant degradation in perfor- probabilities of a model match the observed outcomes.
mance,withAccuracydroppingtoaround0.74to0.76. For perfectly calibrated models, the predicted probabilities
DespitethedropinAccuracy,thesemodelsmaintained should match the observed proportion of positive samples.
similar CPU Time across the different drift levels. For example, for a predicted probability of 0.8, the actual
The results suggest that while the Hybrid Approach is proportionofpositivesamplesinthatbinshouldalsobe0.8.
| 174022 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
FIGURE18. Bi-LSTMcalibrationcurve. FIGURE21. GRUcalibrationcurve.
TABLE9. RetentionandforgettingscoresforBiLSTMacrossdifferentdrift
detectionmethods.
frequencyofpositiveoutcomesineachbinwiththepredicted
| probability. | The formula | used to | calculate the | observed |
| ------------ | ----------- | ------- | ------------- | -------- |
fractionofpositivesforagivenbinisasshowninequation22
as,
n
FIGURE19. BNNcalibrationcurve. 1X
I(y =1)
|     |     | i   |     | (22) |
| --- | --- | --- | --- | ---- |
n
i=1
| where:-nisthenumberofsamplesineachbin,-I(y |     |     |     | = 1) |
| ------------------------------------------ | --- | --- | --- | ---- |
i
| isanindicatorfunctionthatreturns1ifthetrueoutcomey |     |     |     | is  |
| -------------------------------------------------- | --- | --- | --- | --- |
i
positive(i.e.,1)and0otherwise.
Thecloserthecalibrationcurveistothediagonalline,the
moreaccurateandreliablethemodel’spredictedprobabilities
are.
1) BRIERSCORE
TheBrierscoreisacommonlyusedmetrictoquantifyhow
| well-calibrated | predicted | probabilities | are. It computes | the |
| --------------- | --------- | ------------- | ---------------- | --- |
meansquareddifferencebetweenthepredictedprobabilities
| and the | actual outcomes. | The Brier | score is calculated | as  |
| ------- | ---------------- | --------- | ------------------- | --- |
showninequation23
N
1 X
|     | BrierScore= |     | (yˆ −y)2 | (23) |
| --- | ----------- | --- | -------- | ---- |
i i
FIGURE20. LSTMcalibrationcurve. N
i=1
| where:-yˆ | i isthepredictedprobabilityforthei-thsample,- |     |     |     |
| --------- | --------------------------------------------- | --- | --- | --- |
The calibration curve is computed by grouping the y isthetrueoutcome(0or1)forthei-thsample,-N isthe
i
predictedprobabilitiesintobinsandcomparingtheobserved totalnumberofsamples.
VOLUME13,2025 174023

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
.pidycaruccadnatseT-SKgnisunoitcetedtfirddirbyhhtiwsrenraelpeedfosisylanaecnamrofreP
.01ELBAT
174024 VOLUME13,2025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
.ylnotseT-SKgnisunoitcetedtfirdlanretxehtiwsrenraelpeeDfosisylanaecnamrofreP
.11ELBAT
VOLUME13,2025 174025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
.noitcetedtfirddesabytniatrecnuhtiwsrenraelpeeDfosisylanaecnamrofreP
.21ELBAT
174026 VOLUME13,2025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
A lower Brier score indicates a more reliable model that learned.FMcanbecalculatedasequation24,
| accurately | predicts | the | likelihood | of  | an event. | Models | that |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ---------- | --- | --------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
N
exhibitlowerBrierscoresacrossdifferentdrifttypesdemon- 1 X (cid:16) (cid:17)
|     |     |     |     |     |     |     |     |     |     |     | =   | Amax−Afinal |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
strate better calibration, which is crucial when detecting FM (24)
|     |     |     |     |     |     |     |     |     |     |     | N   | i   | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i=1
| and responding |     | to concept    | drift. | The          | Brier | score measures |     |     |        |            |        |          |              |        |
| -------------- | --- | ------------- | ------ | ------------ | ----- | -------------- | --- | --- | ------ | ---------- | ------ | -------- | ------------ | ------ |
| the accuracy   | of  | probabilistic |        | predictions, |       | quantifying    | the |     |        |            |        |          |              |        |
|                |     |               |        |              |       |                |     |     | where: | - N is the | number | of tasks | (or batches) | in the |
meansquareddifferencebetweenpredictedprobabilitiesand
archive.-Amaxisthehighestaccuracyachievedontask
i
actual outcomes and table 8 summarizes the findings. The i.-Afinalistheaccuracyontaskiafterthefinaltraining.
| BiLSTM | model | outperforms |     | the other | models | by  | having |     | i   |     |     |     |     |     |
| ------ | ----- | ----------- | --- | --------- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
AlowFMvalueindicatesminimalforgetting,meaning
| the lowest | Brier | score | of 0.1743, | which | indicates |     | that it |     |     |     |     |     |     |     |
| ---------- | ----- | ----- | ---------- | ----- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
themodelretainsknowledgefromoldertasks.Ahigh
producesthemostreliablepredictedprobabilitiesamongthe
|              |     |     |      |      |        |           |       |     | FM value | indicates | catastrophic |     | forgetting, | where the |
| ------------ | --- | --- | ---- | ---- | ------ | --------- | ----- | --- | -------- | --------- | ------------ | --- | ----------- | --------- |
| four models. | BNN | and | LSTM | have | almost | identical | Brier |     |          |           |              |     |             |           |
model’sperformancedeterioratessignificantlyonolder
| scores (0.1744), |     | showing | that | their probabilistic |     | predictions |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ---- | ------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
tasksasitlearnsnewones.
| are similarly | calibrated. |     | The | GRU model |     | has the | highest |     |           |          |        |     |           |          |
| ------------- | ----------- | --- | --- | --------- | --- | ------- | ------- | --- | --------- | -------- | ------ | --- | --------- | -------- |
|               |             |     |     |           |     |         |         | 2)  | Retention | Accuracy | (ARA): |     | Retention | Accuracy |
Brierscoreof0.1757,thoughstillwithinareasonablerange,
(ARA)isametricusedtoquantifyhowwellthemodel
| suggesting | slightly | less | reliable | calibration | compared |     | to the |     |     |     |     |     |     |     |
| ---------- | -------- | ---- | -------- | ----------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
retainsperformanceonearliertasksasitisexposedto
othermodels.
newdata.Itistheaverageaccuracyontheoldertasks
| The calibration |     | curve | for | BNN as shown |     | in the figure | 19  |     |     |     |     |     |     |     |
| --------------- | --- | ----- | --- | ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
afterthemodelhasbeentrainedonnewertasks.
| that the | model | tends | to be | slightly | overconfident |     | at both |     |       |        |          |         |      |                |
| -------- | ----- | ----- | ----- | -------- | ------------- | --- | ------- | --- | ----- | ------ | -------- | ------- | ---- | -------------- |
|          |       |       |       |          |               |     |         |     | Let A | be the | accuracy | on task | t −k | after training |
low and high probabilities. It deviates from the perfectly t−k
|     |     |     |     |     |     |     |     |     | on task | t. The | Retention | Accuracy | (ARA) | for the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --------- | -------- | ----- | ------- |
calibratedline,especiallyatextremeends.TheBrierscorefor
|     |     |     |     |     |     |     |     |     | modelaftertrainingontaskt |     |     | isdefinedastheaverage |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --------------------- | --- | --- |
BNNwasthehighestamongthemodels,indicatingrelatively
|     |     |     |     |     |     |     |     |     | accuracy | on all | previous | tasks | t − k, where | k is the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ----- | ------------ | -------- |
poorcalibrationcomparedtoothers.ThecurveforBiLSTM
|             |          |           |            |               |            |     |        |     | numberofbatchesortasksbeforet |     |     |     | asequation25, |     |
| ----------- | -------- | --------- | ---------- | ------------- | ---------- | --- | ------ | --- | ----------------------------- | --- | --- | --- | ------------- | --- |
| is closer   | to the   | perfectly | calibrated | line,         | suggesting |     | better |     |                               |     |     |     |               |     |
| calibration | compared |           | to the     | other models. | BiLSTM’s   |     | Brier  |     |                               |     |     |     |               |     |
K
1 X
scoreasshowninfigure18wasoneofthelowest,indicating ARA = A (25)
|                                                          |     |     |     |     |     |     |     |     |     |     | t−k |     | t−k |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| abettercalibrationandmorereliableuncertaintypredictions. |     |     |     |     |     |     |     |     |     |     |     | K   |     |     |
i=1
| The calibration |     | curve | for GRU | shown | in 21 | also shows | a   |     |     |     |     |     |     |     |
| --------------- | --- | ----- | ------- | ----- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
istheaccuracyontaskt−kaftertraining
reasonablematchwiththeperfectlycalibratedline,thoughit where:-A t−k
isslightlymorespreadoutthanBiLSTM.GRU’sBrierscore up to task t. - K is the total number of previous tasks
wasslightlyhigherthanBiLSTM,indicatingthatitperforms (orbatches)toevaluate.
slightly worse in terms of calibration. LSTM’s calibration ARA measures how well the model continues to
performonprevioustasksafterlearningfromnewdata.
curveasshowninfigure20showsanear-perfectalignment
withtheidealline,indicatingthebestcalibrationamongthe A high ARA indicates that the model has retained
fourmodels.LSTMhadthelowestBrierscore,makingitthe knowledgeofprevioustasks,andthus,itislessprone
tocatastrophicforgetting.
bestintermsofcalibration.
|     |     |     |     |     |     |     |     | The table | 9 compares |            | the performance |     | of BiLSTM | (Bidi-       |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ---------- | --------------- | --- | --------- | ------------ |
|     |     |     |     |     |     |     |     | rectional | Long       | Short-Term | Memory)         |     | in terms  | of retention |
H. CATASTROPHICFORGETTINGANDRETENTION (ARA) and forgetting (F) across different drift detection
Catastrophic forgetting refers to the phenomenon where a methods and buffer strategies. The Hybrid Drift Detection
model, after being trained on new data, loses its ability to methodwiththeFIFObufferresultsinthehighestretention
perform well on previously learned tasks. In the context (ARA=0.7318)butalsothehighestforgettingrate(0.0350).
|            |        |      |                 |     |          |         |     | This suggests |     | that while | the FIFO | buffer | slightly | improves |
| ---------- | ------ | ---- | --------------- | --- | -------- | ------- | --- | ------------- | --- | ---------- | -------- | ------ | -------- | -------- |
| of concept | drift, | this | is particularly |     | relevant | because | the |               |     |            |          |        |          |          |
modelmayforgetitsknowledgeofearlierdatadistributions retention,italsoleadstomoreforgettingcomparedtoother
as it is exposed to new data distributions. This can result methods.TheUncertainty-basedDriftDetectionmethodand
in a significant drop in performance on earlier tasks. As a KS-test-based Drift Detection yield similar results, with no
casestudywehavetakenBiLSTMmodelwithvariousdrift significant change in retention and forgetting across buffer
strategies.However,adaptivebufferinghelpsinreducingthe
detectionmethods(Hybrid,UncertaintybasedandStatistical
test based) against the three buffers (Adaptive, FIFO, and forgetting rate compared to FIFO and no buffer scenarios.
No-buffer)andstudiedhowtheproposedmethodsavoidsthe Adaptive buffering generally reduces forgetting rates across
catastrophicforgettingduringitsruntime.Twomeasuresare all methods, but it also comes with slight decreases in
usedinthisstudy,theyare, retention, particularly in Uncertainty-based drift detection.
|     |     |     |     |     |     |     |     | BiLSTM | performs | reasonably |     | well with | the | Hybrid Drift |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | --- | --------- | --- | ------------ |
1) Catastrophic Forgetting (FM) is computed as the Detection method, especially with the FIFO buffer, but the
difference between the maximum accuracy on a task adaptive buffer seems to be the best in terms of minimizing
and the final accuracy after new tasks have been forgetting,thoughitslightlyaffectsretention.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 174027 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
TABLE13. Ablationsforhybriddriftdetectionusingdeeplearnerswithadaptivebufferstrategywithdifferentdrifttypes(Abrupt,GradualandRecurring).
XI. CLINICALINSIGHTSANDCASESTUDIES physical activity pattern—common precursors to metabolic
The integration of drift-aware incremental learning tech- dysregulation can be captured as concept drift. Such
niques with lifestyle disease prediction offers meaningful timely detection allows clinicians to intervene proactively,
insights for real-world clinical decision support. In this potentiallypreventingdiseaseprogression.
| section, we  | discuss practical | implications             | derived | from the     |     |     |     |     |     |     |
| ------------ | ----------------- | ------------------------ | ------- | ------------ | --- | --- | --- | --- | --- | --- |
| experimental | findings          | and potential case-based |         | applications |     |     |     |     |     |     |
B. EHR-INTEGRATEDLEARNINGSYSTEMS
| that align | with public | health surveillance | and | individual |                  |     |        |           |             |       |
| ---------- | ----------- | ------------------- | --- | ---------- | ---------------- | --- | ------ | --------- | ----------- | ----- |
|            |             |                     |     |            | The NHANES-based |     | models | simulated | a streaming | envi- |
patientcare.
|     |     |     |     |     | ronment analogous |               | to real-world | Electronic | Health | Records      |
| --- | --- | --- | --- | --- | ----------------- | ------------- | ------------- | ---------- | ------ | ------------ |
|     |     |     |     |     | (EHRs).           | In a clinical | deployment,   | the        | models | can continu- |
A. PERSONALIZEDMONITORINGANDEARLYDETECTION ously learn from patient-specific data and issue alerts when
The findings through presented experimentation sug- a patient’s risk profile deviates from historical patterns.
gest that adaptive buffering mechanisms combined with These alerts, supported by high model uncertainty, serve
uncertainty-awaredetectioncantracksubtlepatientbehavior as justifiable triggers for additional diagnostics or lifestyle
| changes | over time. For | example, a shift | in dietary | intake or | counseling. |     |     |     |     |               |
| ------- | -------------- | ---------------- | ---------- | --------- | ----------- | --- | --- | --- | --- | ------------- |
| 174028  |                |                  |            |           |             |     |     |     |     | VOLUME13,2025 |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
TABLE14. Ablationsforuncertaintybaseddriftdetectionusingdeeplearnerswithadaptivebufferstrategywithdifferentdrifttypes(Abrupt,Gradualand
Recurring).
C. PUBLICHEALTHSURVEILLANCE Forinstance,suddenincreasesindriftpointsacrossmultiple
On a population scale, the model’s ability to detect models may indicate community-wide behavioral changes
population-level drifts such as seasonal trends in hyperten- or environmental exposures, warranting targeted health
sion or glucose levels can support public health strategies. campaigns.
VOLUME13,2025 174029

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
.srenraelpeedsuoiravgnisuygetartsreffubevitpadahtiw)gnirrucerdnalaudarG,tpurbA(sepyttfirdsuoiravrofecnamrofrepnotcapmistidnaedutingamtfirdnoydutS
.51ELBAT
174030 VOLUME13,2025

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
D. CASEEXAMPLE:DRIFTINPHYSICALACTIVITYAND the study emphasizes the critical role of adaptive buffering
strategiesandadvanceddriftdetectiontechniquesinensuring
DIABETESONSET
Consider a middle-aged patient whose physical activity effectiveandaccurateincrementallearninginthepresenceof
| sharplydeclinesoverseveralweeks,ascapturedbywearable |         |       |      |          |           |         |     | conceptdrift. |     |     |     |     |     |     |
| ---------------------------------------------------- | ------- | ----- | ---- | -------- | --------- | ------- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| devices.                                             | The GRU | model | with | adaptive | buffering | detects | a   |               |     |     |     |     |     |     |
drift in the ‘PAQ605‘ (work-related activity) and ‘PAQ620‘ FUTURESCOPE
(recreational activity) features, correlated with rising BMI Thefollowingdirectionsareenvisionedtoextendtheutility
and fasting glucose levels. The system flags this shift with andscopeofthisframework:
highuncertainty,promptingthecliniciantoassesstheriskof Multi-modalLearning:Integrateimaging,sensor,and
•
diabetesonsetandrecommendbehavioralmodifications. genomicdatatoenhancefeaturespaceandincreasedrift
sensitivity.
E. TRUSTWORTHYAIINMEDICINE • Explainable Buffering: Design interpretable buffer
The use of Bayesian Neural Networks (BNNs) not only strategies to explain sample retention or replacement
improved drift detection but also introduced a quantifiable decisionsforclinicalauditability.
uncertaintymetric,anessentialfeatureinclinicalAIsystems. • Federated Deployment: Expand to privacy-aware
This uncertainty-aware modeling enhances trust, allowing federated learning settings across hospitals and demo-
clinicianstointerpretpredictionswithconfidencethresholds graphics, ensuring real-time drift tracking without data
| andavoidover-relianceonautomateddecisions. |     |     |     |     |     |     |     | centralization. |        |           |     |           |            |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | --------- | --- | --------- | ---------- | --- |
|                                            |     |     |     |     |     |     |     | • Dynamic       | Policy | Triggers: |     | Implement | real-time, |     |
F. RECOMMENDATIONSFORCLINICALDEPLOYMENT uncertainty-awaredriftalarmsandmodelre-calibration
• Employadaptivebuffer-basedlearnerstobalancehistor- triggerstailoredtodiseaseprogressionpatterns.
icalcontextandreal-timeupdates. Clinical Validation: Collaborate with healthcare
•
• Use uncertainty scores as a gating mechanism for providers to deploy and evaluate the framework in live
generatingclinicalalerts. electronic health record (EHR) environments for real-
• Integrate statistical drift logs into EHR systems for worldvalidation.
transparentauditingandexplainability.
| • Perform | periodic |     | model validation |     | to ensure | alignment |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | ---------------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ACKNOWLEDGMENT
withshiftingpopulationhealthdynamics. TheauthorsthankNitteMeenakshiInstituteofTechnology,
In summary, the proposed framework not only supports Bengaluru,andVisvesvarayaTechnologicalUniversity,Bela-
continuouslearningbutalsoalignswellwithprecisionhealth
gavi,forprovidingtheresearchinfrastructureandacademic
| goals, enabling |     | systems | that | evolve with | the | patient | and | support. |     |     |     |     |     |     |
| --------------- | --- | ------- | ---- | ----------- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
populationalike.
REFERENCES
XII. CONCLUSIONANDFUTURESCOPE
|     |     |     |     |     |     |     |     | [1] WorldHealthOrganization.(May2024).WhoResultsReport2023Shows |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
InthisstudyonAdaptiveBufferingStrategiesforIncremental Notable Health Achievements and Calls for Concerted Drive Toward
|     |     |     |     |     |     |     |     | Sustainable | Development | Goals. | Accessed: | May | 28, 2025. | [Online]. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------ | --------- | --- | --------- | --------- |
LearningUnderConceptDriftinLifestyleDiseaseModeling,
Available:https://shorturl.at/lyiCE
| four deep | learning | models: | Bi-LSTM, |     | LSTM, | BNN, | and |                                                                 |     |     |     |     |     |     |
| --------- | -------- | ------- | -------- | --- | ----- | ---- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|           |          |         |          |     |       |      |     | [2] R.Beaglehole,C.Bates,B.Youdan,andR.Bonita,‘‘Nicotinewithout |     |     |     |     |     |     |
GRU were evaluated for concept drift detection using three smoke: Fighting the tobacco epidemic with harm reduction,’’ Lancet,
vol.394,no.10200,pp.718–720,Aug.2019.
| distinct | buffering | strategies | (Adaptive |     | buffer, | FIFO buffer, |     |              |             |               |     |           |       |            |
| -------- | --------- | ---------- | --------- | --- | ------- | ------------ | --- | ------------ | ----------- | ------------- | --- | --------- | ----- | ---------- |
|          |           |            |           |     |         |              |     | [3] G. Zipf, | M. Chiappa, | K. S. Porter, | Y.  | Ostchega, | B. G. | Lewis, and |
andNo-buffer)andthreetypesofdriftdetectionmechanisms
J.Dostal,‘‘Healthandnutritionexaminationsurvey:Planandoperations,
(KS-test,Hybriddriftdetection,andUncertainty-baseddrift 1999–2010,’’inVitalandHealthStatistics,vol.56.Hyattsville,MD,USA:
detection). The analysis revealed that adaptive buffering U.S.DepartmentofHealthandHumanServices,1999.[Online].Available:
https://www.cdc.gov/nchs/data/series/sr01/sr01056.pdf
| strategies | consistently |     | outperformed | FIFO | and | No-buffer |     |                                                                  |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------------ | ---- | --- | --------- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |              |     |              |      |     |           |     | [4] A.M.AlaaandM.vanderSchaar,‘‘Prognosticationandriskfactorsfor |     |     |     |     |     |     |
strategies across all models, maintaining higher accuracy, cysticfibrosisviaautomatedmachinelearning,’’Sci.Rep.,vol.8,no.1,
precision,andrecall,particularlyunderAbrupt,Gradual,and p.11242,Jul.2018.
|     |     |     |     |     |     |     |     | [5] M.Zhang,O.Press,W.Merrill,A.Liu,andN.A.Smith,‘‘Howlanguage |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Recurring drifts. Hybrid drift detection provided the best modelhallucinationscansnowball,’’2023,arXiv:2305.13534.
overallperformance,withBi-LSTMshowingstrongretention [6] A.Tsymbal,‘‘Theproblemofconceptdrift:Definitionsandrelatedwork,’’
and minimal forgetting, especially in the face of high drift Comput.Sci.Dept.,TrinityCollegeDublin,vol.106,no.2,p.58,2004.
|             |     |       |           |       |              |     |      | [7] J.ArmstrongandD.A.Clifton,‘‘Continuallearningoflongitudinalhealth |     |     |     |     |     |     |
| ----------- | --- | ----- | --------- | ----- | ------------ | --- | ---- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| magnitudes. | The | drift | magnitude | study | demonstrated |     | that |                                                                       |     |     |     |     |     |     |
records,’’inProc.IEEE-EMBSInt.Conf.Biomed.HealthInformat.(BHI),
increasingtheintensityofdrift(from20%to100%)signifi-
Sep.2022,pp.01–06.
|     |     |     |     |     |     |     |     | [8] Z. Obermeyer, | B.  | Powers, | C. Vogeli, | and | S. Mullainathan, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ---------- | --- | ---------------- | --- |
cantlyimpactedmodelperformance,withmodelsemploying
|          |           |           |                   |       |         |           |     | ‘‘Dissecting | racial            | bias in  | an algorithm | used     | to manage         | the |
| -------- | --------- | --------- | ----------------- | ----- | ------- | --------- | --- | ------------ | ----------------- | -------- | ------------ | -------- | ----------------- | --- |
| adaptive | buffering | and       | uncertainty-based |       | drift   | detection |     |              |                   |          |              |          |                   |     |
|          |           |           |                   |       |         |           |     | health       | of populations,’’ | Science, | vol.         | 366, no. | 6464, pp.447–453, |     |
| proving  | more      | resilient | in handling       | large | drifts. | Notably,  |     |              |                   |          |              |          |                   |     |
Oct.2019.
BNN struggled with high drift magnitudes, underscoring [9] B. Saxena, M. Jain, and A. Sinha, ‘‘AI-based predictive models
|                |     |              |        |       |           |         |     | in healthcare,’’ |     | in Advancing | Biotechnology: |     | From      | Science |
| -------------- | --- | ------------ | ------ | ----- | --------- | ------- | --- | ---------------- | --- | ------------ | -------------- | --- | --------- | ------- |
| the importance |     | of combining | robust | drift | detection | methods |     |                  |     |              |                |     |           |         |
|                |     |              |        |       |           |         |     | To Therapeutics  |     | and. Cham,   | Switzerland:   |     | Springer, | 2025,   |
with effective adaptation strategies like retraining. Overall, pp.109–125.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 174031 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
[10] S. Arora, R. Rani, and N. Saxena, ‘‘A systematic review on detection learning.HehascontributedtofundedprojectsbyVGST,Karnataka,and
andadaptationofconceptdriftinstreamingdatausingmachinelearning received multiple best paper awards. His technical skills include Python,
techniques,’’ WIREs Data Mining Knowl. Discovery, vol. 14, no. 4, Java,andmachinelearningframeworks,suchasPyTorchandTensorFlow.
p.1536,Jul.2024. Hisresearchfocusesonadaptivesystemsandpredictiveaccuracyindynamic
| [11] Hartatik, | L. Heryawan, | and | R. Pulungan, | ‘‘Trust | decay-based temporal | environments. |     |     |     |     |
| -------------- | ------------ | --- | ------------ | ------- | -------------------- | ------------- | --- | --- | --- | --- |
learningfordynamicrecommendersystemswithconceptdriftadaptation,’’
IEEEAccess,vol.13,pp.110955–110971,2025.
[12] Y.Rotalinti,P.Myles,andA.Tucker,‘‘Predictingperformancedriftin
AImodelsofhealthcarewithoutgroundtruthlabels,’’inProc.Int.Symp.
Intell.DataAnal.,2024,pp.167–178.
[13] K.Guo,W.Ni,L.Du,Y.Zhou,L.Cheng,andH.Zhou,‘‘Environmental
chemicalexposuresandamachinelearning-basedmodelforpredicting
M.V.MANOJKUMAR(SeniorMember,IEEE)
hypertensioninNHANES2003–2016,’’BMCCardiovascularDisorders,
|     |     |     |     |     |     |     | received the | bachelor’s and | master’s | degrees |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | -------- | ------- |
vol.24,no.1,p.544,Oct.2024.
|               |                |            |          |              |                 |     | from VTU   | and the Ph.D.     | degree         | from NITK |
| ------------- | -------------- | ---------- | -------- | ------------ | --------------- | --- | ---------- | ----------------- | -------------- | --------- |
| [14] S. Birdi | et al., ‘‘Bias | in machine | learning | applications | to address non- |     |            |                   |                |           |
|               |                |            |          |              |                 |     | Surathkal. | He is a Professor | in information | sci-      |
communicablediseasesatapopulation-level:Ascopingreview,’’BMC
PublicHealth,vol.24,no.1,p.3599,Dec.2024. ence and engineering with the Nitte Meenakshi
[15] Q.Tang,Y.Wang,andY.Luo,‘‘Aninterpretablemachinelearningmodel Institute of Technology, Bengaluru. With over
withdemographicvariablesanddietarypatternsforASCVDidentification: 12yearsinacademia,hehasledresearchprojects
FromU.S.NHANES1999–2018,’’BMCMed.Informat.Decis.Making, funded by VGST, TEQIP, and DST; and four
vol.25,no.1,p.105,Mar.2025. international consultancy projects with Cybernet
[16] N. Nghiem, N. Wilson, J. Krebs, and T. Tran, ‘‘Predicting the risk of Infocom,USA.Hehasauthoredover60research
diabetescomplicationsusingmachinelearningandsocialadministrative articles,holdsfivepatents,andservesasanassociateeditorforFrontiers.
datainacountrywithethnicinequitiesinhealth:AotearoanewZealand,’’ Hefrequentlydeliversworkshopsandlecturesonthesetopicsinternationally.
BMCMed.Informat.Decis.Making,vol.24,no.1,p.274,Sep.2024. His research and teaching interests include process mining, data science,
[17] Z.Si,D.Zhang,H.Wang,andX.Zheng,‘‘PrOsteoporosis:Predicting machinelearning,andEDA.
osteoporosisriskusingNHANESdataandmachinelearningapproach,’’
BMCRes.Notes,vol.18,no.1,pp.1–10,Mar.2025.
[18] X.Deng,L.Ma,P.Li,M.He,R.Jin,Y.Tao,H.Cao,H.Gao,W.Zhou,
K.Lu,X.Chen,W.Li,andH.Zhou,‘‘Identificationandoptimizationof
relevantfactorsforchronickidneydiseaseinabdominalobesitypatientsby
machinelearningmethods:InsightsfromNHANES2005–2018,’’Lipids
HealthDisease,vol.23,no.1,p.390,Nov.2024.
|     |     |     |     |     |     |     | B. H. PUNEETHA | (Senior | Member, | IEEE) |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ------- | ----- |
[19] Y.Zibibula,G.Tayier,A.Maimaiti,T.Liu,andJ.Lu,‘‘Machinelearning
|     |     |     |     |     |     |     | received the | B.E. degree from | the GM | Institute |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------------- | ------ | --------- |
approachestoidentifythelinkbetweenheavymetalexposureandischemic
ofTechnologyandtheM.Tech.degreefromthe
strokeusingtheU.S.NHANESdatafrom2003to2018,’’FrontiersPublic
Health,vol.12,Sep.2024,Art.no.1388257. Bapuji Institute of Engineering and Technology.
[20] X.Guo,M.Ma,L.Zhao,J.Wu,Y.Lin,F.Fei,C.S.Tarimo,S.Wang, He is currently pursuing the Ph.D. degree in
J.Zhang, X.Cheng, and B. Ye, ‘‘The association of lifestyle with detecting and localizing model decay due to
cardiovascular and all-cause mortality based on machine learning: A conceptdriftinprocessmining.HeisaResearch
prospectivestudyfromtheNHANES,’’BMCPublicHealth,vol.25,no.1, ScholarwiththeDepartmentofInformationSci-
p.319,Jan.2025.
|     |     |     |     |     |     |     | ence and Engineering, | Nitte | Meenakshi | Institute |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | ----- | --------- | --------- |
[21] P.Kumari,J.Chauhan,A.Bozorgpour,B.Huang,R.Azad,andD.Merhof,
|     |     |     |     |     |     |     | of Technology, | Bengaluru. | He is an | Assistant |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | -------- | --------- |
‘‘Continuallearninginmedicalimageanalysis:Acomprehensivereview ProfessorwiththeDepartmentofComputerScienceandBusinessSystems,
ofrecentadvancementsandfutureprospects,’’2023,arXiv:2312.17004. BapujiInstituteofEngineeringandTechnology.
[22] C.-H.LiandN.K.Jha,‘‘PAGE:Domain-incrementaladaptationwithpast-
agnosticgenerativereplayforsmarthealthcare,’’2024,arXiv:2403.08197.
| [23] T. Vu, | R. Dawadi, | M. Yamamoto, | J. T. | Tay, N. | Watanabe, Y.Kuriya, |     |     |     |     |     |
| ----------- | ---------- | ------------ | ----- | ------- | ------------------- | --- | --- | --- | --- | --- |
A.Oya,P.N.H.Tran,andM.Araki,‘‘Predictionofdepressivedisorder
usingmachinelearningapproaches:FindingsfromtheNHANES,’’BMC
Med.Informat.Decis.Making,vol.25,no.1,pp.1–12,Feb.2025.
[24] Z.Li,W.Wu,andH.Kang,‘‘Machinelearning-drivenmetabolicsyndrome
prediction:Aninternationalcohortvalidationstudy,’’Healthcare,vol.12, NASSERABDOSAIFALMURAQAB(Member,
no.24,p.2527,Dec.2024. IEEE)receivedthebachelor’sdegreeinmanage-
|              |               |             |                |           |                  |     | ment information | systems       | from UAE | University |
| ------------ | ------------- | ----------- | -------------- | --------- | ---------------- | --- | ---------------- | ------------- | -------- | ---------- |
| [25] Centers | for Disease   | Control     | and Prevention | (CDC).    | (2024). National |     |                  |               |          |            |
|              |               |             |                |           |                  |     | (UAEU), the      | M.B.A. degree | from     | Abu Dhabi  |
| Health       | and Nutrition | Examination | Survey         | (NHANES). | Accessed:        |     |                  |               |          |            |
University(ADU),andthePh.D.degreeinbusi-
| May       | 24, 2025. [Online]. | Available: | https://www.cdc.gov/nchs/nhanes/ |     |     |     |                                            |     |     |     |
| --------- | ------------------- | ---------- | -------------------------------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- |
| index.htm |                     |            |                                  |     |     |     | nessadministrationfromDubaiBusinessSchool, |     |     |     |
UniversityofDubai(UD).Histhesisfocusedon
|     |     |     |     |     |     |     | smart government | services | adoption. | He is an |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | --------- | -------- |
AssociateProfessorinmanagementandaVPof
B. S. PRASHANTH received the B.E. degree operations with UD. He has published research
from the Jawaharlal Nehru National College of papersininternationaljournalsandconferences.Inaddition,hedelivered
Engineering and the M.Tech. degree from the keynotespeechesatinternationalevents.HehasextensiveITmanagement
Bapuji Institute of Engineering and Technology. experiencesincehehasbeenworkinginEtihadairways,RochesterInstitute
He is currently pursuing the Ph.D. degree in of Technology (RIT), Dubai, and joined UD as the Director of IT. He is
detecting and localizing model decay due to a Judge-Member with the Shikha Latifa Award, Ministry of Education
concept drift in deep neural networks. He is a Excellence Competition, and QS Reimagine Education Competition. His
ResearchScholarandanAssistantProfessorwith research interests include and not limited to technology adoption, smart
theInformationScienceandEngineeringDepart- cities, e-learning, emerging technologies and business, and management.
ment, Nitte Meenakshi Institute of Technology, Heservedasareviewerinseveralinternationalconferencesandjournals.
Bengaluru.Hehasauthoredseveralpublications,includingworksonIoT- HewasanEditorialBoardMemberofinternationaljournals,suchasPLOS
drivenautomation, COVID-19 data analysis, and advancements in deep OneandJournalofGlobalInformationManagement.
| 174032 |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

B.S.Prashanthetal.:AdaptiveBufferingStrategiesforIncrementalLearning
ARIFUL HOQUE received the Bachelor of Sci- thePresident(theChapterChair)andanExecutiveBoardMemberofthe
encedegreeincivilengineeringfromBangladesh AcademyofInternationalBusiness–MiddleEastNorthAfrica(AIB-MENA)
University of Engineering and Technology, and Chapter.HeisalsoaRegisteredDietitianandpossessesprofessionalcertifi-
the Ph.D. degree in financial engineering from cationsinNEBOSHOccupationalHealthandSafety,ProjectManagement:
Curtin University, Australia. He is currently a Certified Business Professional (CBP), Emotional Intelligence Assessor,
SeniorLecturerinfinanceandtheAcademicChair and Quality Management System Internal Auditors (ISO 9001:2008).
oftheMasterofBusinessAdministration(MBA) He has attained over $4.8 million USD in grants and published over
Global,CollegeofBusiness,MurdochUniversity. 265peer-reviewedjournalarticles,peer-reviewedinternationalconferences,
Previously,hewasaBusinessAnalyst,anOracle co-authoredbooks,andbookchapters.Hisresearchinterestsincludehealth
Programmer,andaSoftwareDeveloperforseveral systems, public policy, healthcare management and leadership, maternal
well-reputedorganizations,includingSt.GeorgeBank,Australia,andAir andchildhealth,healthpolicyandinnovation,nutrition,globalgovernance,
New Zealand, New Zealand. He was also a Civil Engineer for several internationalbusinesspolicy,socialpolicy,public-privatepartnerships,and
multinational construction companies in Bangladesh. He is the author of qualitymanagement.
InternationalFinancialManagement(Asia–Pacificedition),oneofthetop
textbooksininternationalfinance.Hehaspublishedhishigh-qualityresearch
worksinvariousScopusQ1-rankedjournals,includingEnergyEconomics,
International Review of Economics and Finance, Pacific-Basin Finance
Journal, Global Finance Journal, International Journal of Managerial ANANTH RAO received the M.S. degree in
Finance,EnergyPolicy,JournalofOpenInnovation:Technology,Market, appliedeconomics-bankingfromPurdueUniver-
and Complexity, Financial Innovation, International Review of Financial sity,USA,in1985,andthePh.D.degreeinapplied
Analysis,ResearchinInternationalBusinessandFinance,FinTech,Risks, economics-banking from the University of Min-
Economies, International Journal of Financial Studies, and Eurasian nesota,USA,in1991.HeisanEmeritusProfessor
BusinessReview.Hereceivedseveralgrantsandawardsforexcellencein of finance, the former Dean of Dubai Business
research. School, and a former Chief Academic Officer
(Provost)withtheUniversityofDubai(UD).Prior
to joining academics, in 1997, he was with the
StateBankofIndia—apremiercommercialbank
inIndia—invariousmanagerialrolesformorethan15years.Heisanactive
professional member of the Financial Management Association (FMA)
International,USA,andtheInstituteofManagementAccountants(IMA),
USA.Heisanactiveresearcherintheareasofenterpriseriskmanagement,
investments,bankmanagement,assetsandliabilitiesmanagement,corporate
finance, stabilityof emergingfinancial markets,derivatives, efficiencyof
financialservicesfirms,andartificialintelligenceinpublichealthrelated
areas.HehasexecutedseveralconsultancyprojectsforDubaiChamberof
IMMANUELAZAADMOONESARwasbornin Commerce and Industry, more than six companies in Dubai and United
TrinidadandTobago.HereceivedtheBachelorof ArabEmirates;andUSAIDprojectsforcapacitybuildingoftwobusiness
Science degree in human ecology: nutrition and schoolsinIraq.HewasinstrumentalinbuildingresearchcapacityofHEIs
dietetics from the University of the West Indies in India via international collaborations through competitive bidding of
(UWI), Trinidad and Tobago, the Postgraduate research projects through USAID /NIH/CDC/EU grants in data analysis,
Diploma degree (Hons.) from the Institutional finance,health,supplychainandlogistics,andICTdomains.Heiscurrently
CommunityNutritionandDietetics,themaster’s afreelanceConsultantadvisingNitteEducationTrustandRamaiahGroup
degree (Hons.) in quality management from the of Institutions, Bengaluru, India, in building research capacity through
UniversityofWollongong(UOW),Australia,and international collaborations. He was instrumental in leading the business
the Ph.D. degree (Hons.) in health services: schoolteamtoearnthecovetedAssociationtoAdvanceCollegiateSchools
leadershipfromWaldenUniversity,USA.HisPh.D.dissertationwastitled of Business (AACSB) international accreditation for the UD Business
‘‘The Role of UAE Health Professionals in Maternal and Child Health School,in2009,subsequentlymaintainingfrom2014to2019.AsanAACSB
Policy.’’Hiscareerexperienceincludesqualityassuranceandmanagement, OfficialVolunteer,heservedasaPRTmemberonvisitstomanybusiness
nutritionanddietetics,healthandsafety,teaching,andinstitutionalresearch. schoolsinIndia,Moscow,Kuwait,andUnitedArabEmiratesforAACSB
HeistheHealthPolicyandSystemsResearchProfessor(Full)withMBRSG, initial accreditation of the schools, besides serving as a mentor for few
theScientificPolicyAdvisorwiththeInternationalVaccineInstitute,andthe schools.
FormerAcademyofInternationalBusiness(MENA)President. He is also
VOLUME13,2025 174033