Article
A Reinforcement Learning Framework for Fraud Detection in
Highly Imbalanced Financial Data
AlkisPapanastassiou1,2,* ,BenedettaCamaiani1,2 ,PiergiulioLenzi1,2 andRiccardoCrupi3
1 IstitutoNazionalediFisicaNucleare(INFN),SezionediFirenze,50019SestoFiorentino,Italy;
benedetta.camaiani@unifi.it(B.C.);piergiulio.lenzi@unifi.it(P.L.)
2 DipartimentodiFisicaeAstronomia,UniversitàdegliStudidiFirenze(UNIFI),50019SestoFiorentino,Italy
3 DataArtificialIntelligenceOffice,IntesaSanpaoloS.p.A.,10138Torino,Italy;
riccardo.crupi@intesasanpaolo.com
* Correspondence:alkis.papanastassiou@unifi.it
Abstract
Anomalydetectioninfinancialtransactionsisachallengingtask,primarilyduetosevere
classimbalanceandtheadaptivebehavioroffraudulentactivities. Thispaperpresents
areinforcementlearningframeworkforfrauddetection(RLFD)toaddressthisproblem.
WetrainadeepQ-network(DQN)agentwithalongshort-termmemory(LSTM)encoder
toprocesssequencesoffinancialeventsandidentifyanomalies. Onaproprietary,highly
imbalanceddataset,10-foldcross-validationhighlightsadistincttrade-offinperformance.
Whileagradientboostedtrees(GBT)baselinedemonstratessuperiorglobalrankingca-
pabilities (higher ROC and PR AUC), the RLFD agent successfully learns a high-recall
policydirectlyfromtherewardsignal,meetingoperationalneedsforrareeventdetection.
Importantly,adynamicorthogonalityanalysisprovesthatthetwomodelsdetectdistinct
subsetsoffraudulentactivity. TheRLFDagentconsistentlyidentifiesuniquefraudulent
transactionsthatthetree-basedmodelmisses,regardlessofthedecisionthreshold. Evenat
high-confidenceoperatingpoints,theRLFDagentaccountsfornearly30%ofthedetected
anomalies. These results suggest that while tree-based models offer high precision for
staticpatterns,RL-basedagentscapturesequentialanomaliesthatareotherwisemissed,
supportingforahybrid,paralleldeploymentstrategy.
Keywords: frauddetection;reinforcementlearning;deepq-network;anomalydetection;
imbalanceddata;sequentialdata;data-drivenfinance
1. Introduction
Thedetectionoffraudulentactivitiesinfinancialdatarepresentsacriticalandpersis-
tentchallenge,primarilyduetothesevereclassimbalanceofdatasetsandthedynamic,
AcademicEditor:RuiAraújo adaptivenatureoffraudulentactivities,asoutlinedincomprehensivereviewssuchasCom-
Received:24November2025 pagninoetal. (2025)[1],HernandezArosetal. (2024)[2],Alietal. (2022)[3],Al-Hashedi
Revised:15December2025 andMagalingam(2021)[4],andothers[5–8]. Financialfraudismultifaceted,encompassing
Accepted:24December2025
schemes from credit card and insurance fraud to sophisticated money laundering and
Published:26December2025
emergingtypologieslikeauthorizedpushpayment(APP)fraud[1]. Manyoftheseschemes
Copyright:©2025bytheauthors.
arenotisolatedeventsbutarecomposedofsequencesofactionsdesignedtoappearlegiti-
LicenseeMDPI,Basel,Switzerland.
mate. Forexample,moneymulinginvolveschainsoftransactionsacrossmultipleaccounts
Thisarticleisanopenaccessarticle
distributedunderthetermsand toobscuretheoriginoffunds,whileaccounttakeover(ATO)fraudmaybeprecededbya
conditionsoftheCreativeCommons seriesofunusualloginactivities.
Attribution(CCBY)license.
Appl.Sci.2026,16,252 https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 2of16
Traditionalmachinelearningmodels,suchasGradientBoostedTrees(GBTs)orRan-
domForests,typicallytreattransactionsasindependenttabulardatapoints.Whileeffective
forstaticclassification,thisindependenceassumptionrenderstheminherentlyblindto
thetemporalcorrelationsandsequentialpatternscharacteristicofsophisticatedfraud. As
recentempiricalstudieshavedemonstrated[1],thislimitationoftenresultsinlowdetection
ratesforrarefraudulentevents,necessitatingtheexplorationoffundamentallydifferent
paradigmssuchasReinforcementLearning(RL).
In this work, we present the Reinforcement Learning for Fraud Detection (RLFD)
framework. Wepositionthiscontributionnotasanoveldeeplearningarchitecture,butas
adomain-specificadaptationoftheexistingRLADframework(ReinforcementLearningfor
AnomalyDetection)[9],specificallyengineeredfortheconstraintsofbankingtransaction
streams. Theinnovationofthisstudyliesintheadaptationoftheexistingformulation,
specificallytheclient-centricstatewindowingandasymmetricrewardshaping,toaddress
thesevereclassimbalanceandoperationalcostsoffinancialfraud. Wehypothesizethat
thistargetedadaptationenablestheagenttocapturesequentialbehavioralpatternsthat
remaininvisibletothestaticclassifierscurrentlydominatingtheindustry.
Toinvestigatethishypothesisandassesstheoperationalvalueoftheframework,this
studyaddressesthefollowingresearchquestions:
• Can a sequential reinforcement learning agent, trained with asymmetric rewards,
achievesuperiordetectionrates(recall)forrarefraudulenteventscomparedtotradi-
tionalstaticbaselinesinhighlyimbalancedfinancialdatasets?
• Does the RLFD framework detect a distinct subset of fraudulent activities com-
paredtotree-basedmodels,therebyprovidingorthogonalandcomplementaryopera-
tionalvalue?
• To what extent does the sequential RL approach generalize to standard public
benchmarks that lack strong temporal dependencies, compared to state-of-the-art
staticclassifiers?
2. TheoreticalBackgroundandLiteratureReview
Theapplicationofmachinelearningtofinancialfrauddetectionhasevolvedsignif-
icantly,transitioningfromrule-basedexpertsystemstosophisticatedstatisticallearning
algorithms. This section reviews the existing scholarship regarding static classification
methods,thechallengesofimbalancedsequentialdata,andtheemergenceofreinforcement
learningasaviablealternativeforanomalydetection.
2.1. SupervisedLearningandClassImbalance
Traditionalsupervisedlearningalgorithms,particularlyensemblemethodssuchas
RandomForestsandGradientBoostedTrees(GBTs),representthecurrentindustrialstan-
dardforfrauddetection[1,10]. Thesemodelsexcelatcapturingnon-linearinteractions
betweenfeaturesintabulardata. However, theirstandardformulationreliesonthein-
dependentandidenticallydistributed(i.i.d.) assumption,treatingeachtransactionasan
isolatedevent. Thislimitationisrelevantinfinancialcontexts,wherefraudulentbehavior
oftenmanifestsasasequenceofactionsratherthanasingleanomalousdatapoint[5].
Furthermore, the extreme class imbalance characterizing financial datasets
(typically< 5%fraudrate)posesaseveretheoreticalchallenge. Standardobjectivefunc-
tionstendtobiasthemodeltowardsthemajorityclasstomaximizeglobalaccuracy[3,4].
AsdemonstratedbyCompagninoetal. (2025)[1]onthesameproprietarybankingdataset
usedinthisstudy,ensemblemethodsoftenstruggletoachievehighrecallwithoutgenerat-
ingexcessivefalsepositives;intheirbenchmark,aRandomForestmodelachievedafraud
recallofonly0.36,highlightingtheneedforalternativeapproaches.
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 3of16
2.2. DeepLearningandSequenceModeling
Toaddressthetemporallimitationsofstaticmodels,DeepLearningarchitecturessuch
asRecurrentNeuralNetworks(RNNs)andLongShort-TermMemory(LSTM)networks
have been adopted to model transaction sequences [11]. LSTMs are theoretically well-
suitedforthisdomainbecausetheymaintainaninternalstatethatcancapturelong-term
dependencies. However,inapurelysupervisedsetting,LSTMsaretypicallyoptimizedto
minimizeaclassificationlossfunction(e.g.,cross-entropy). Thisobjectivedoesnotalways
alignwiththeoperationalgoaloffrauddetection,whichistomaximizethecumulative
financialsavingsofcorrectlyblockingfraudwhileminimizingcustomerfriction.
2.3. ReinforcementLearningforAnomalyDetection
ReinforcementLearning(RL)reframestheclassificationproblemasaMarkovDecision
Process(MDP).Unlikesupervisedlearning,whichprovidesastaticlabelforeveryinput,
RLinvolvesanagentthatinteractswithanenvironment(thestreamoftransactions)and
receives a reward signal based on its actions [12]. This paradigm allows for the direct
optimizationofnon-differentiablebusinessmetricsthroughrewardshaping.
RecentliteraturehasbeguntoexploreRLforanomalydetection. TheRLADframe-
workproposedbyWuandOrtiz[9]demonstratedthataDeepQ-Network(DQN)could
effectively learn to identify anomalies in time-series data by treating the classification
decisionasanactioninanMDP.Bydecouplingthelearningprocessfromstaticlossmini-
mization,RLagentscanlearnaggressivepoliciesthatprioritizerareeventsifthereward
structureincentivizesit. Thisstudybuildsuponthesetheoreticalfoundationstoanswer
theresearchquestionsposedinSection1.
2.4. MappingFinancialFraudtoRL
Tobridgethegapbetweenfinancialanomalydetectionandreinforcementlearning
theory,weformalizethefrauddetectionproblemnotasastaticclassificationtask,butasa
sequentialinteractionbetweenamonitor (theagent)andaclientprofile(theenvironment).
Thisconceptualmodelisbasedonthreetheoreticallinks:
1. Sequentialityoffraud: Unlikestaticanomalies,financialfraudoftenevolvesthrough
atrajectoryofevents(e.g.,aninitialphaseoflow-risk,apparentlylegitimatetransac-
tionsfollowedbyasuddenescalationintoillicitactivity). TheRLframeworkcaptures
this via the state representation (s ), which is not a single point but a history win-
t
dow, allowing the agent to detect patterns based on temporal context rather than
instantaneousfeaturevalues.
2. Action-consequencefeedback: Inabankingcontext,everydecisionhasanimmediate
operationalconsequence. Blockingalegitimateuser(FalsePositive)incursa“cus-
tomerfriction”cost,whileallowingafraud(FalseNegative)incursadirectfinancialli-
ability. ThisalignsnaturallywiththeRLrewardsignal(r ),whicheffectivelytranslates
t
theasymmetriccostmatrixofthebusinessdirectlyintotheoptimizationobjective.
3. Adaptivedecisionboundary: Traditionalclassifiersoptimizeafixeddecisionbound-
arybasedonatrainingsetdistribution. Incontrast,anRLagentoptimizesapolicy
π(s )tomaximizelong-termrewards. Thistheoreticallyallowsthesystemtoadapt
t
itssensitivitybasedonthestateoftheclient(e.g.,becomingmoreaggressiveifthe
recent sequence shows rising entropy), rather than applying a global threshold to
allusers.
Byframingtheproblemthroughthisconceptuallens,wejustifytheselectionofaDQN
with LSTM encoders as the appropriate methodological vehicle to answer the research
questionsposedinSection1.
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 4of16
3. MaterialsandMethods
OurstudyutilizestwodistinctdatasetstoevaluatetheRLFDframework,selectedto
assessperformanceinbothacomplex,real-worldbankingscenarioandastandardized
publicenvironment.
3.1. ProprietaryTransactionDataset
Theprimarydatasetemployedinthisstudyisaproprietarycollectionoffinancial
transactions provided by Intesa Sanpaolo (ISP), comprising 90,314 bank transfers from
anonymizedusers. Thedatasetishighlyimbalanced,containing3285fraudulenttransac-
tions,whichrepresentapproximately3.6%ofthetotal. Toensureprivacyandregulatory
compliance,alldatawereencryptedandanonymized: categoricalandtextualvariables
werehashedusingtheSecureHashAlgorithm256-bit(SHA-256)[13]priortobeingtrans-
formedintonumericalrepresentationsformachinelearningmodels.
Afeatureengineeringprocesswascarriedouttoconstructarichandstructuredsetof
variablesforeachtransaction,organizedintothefollowingcategories:
• Temporal: Hour,day,dayoftheweek,andaweekendindicator.
• Spatial: Latitudeandlongitudeofthetransactionorigin,alongwithaclient-specific
distancefromspatialmedianfeature. Specifically,foreachclient,themedianlatitude
and longitude across all transactions are computed, and the Euclidean distance of
eachtransactionfromthisspatialmedianiscalculated,providingameasureofgeo-
graphicdeviation.
• Financial: Transactionamount,currencycode,divisibilityflags(e.g.,by2,5,or10),
anddecimalpatterns(e.g.,0.00,0.50).
• Contextualandtechnical: BankIdentifierCode(BIC),bankcodes,clienttype,mobile
carrier,anddecomposed/encryptedIPaddressoctets. Semanticinformationfromthe
transactiondescriptionfieldiscapturedusinga10-dimensionalWord2Vecembedding.
• Securityandauthentication: Flagsindicatingsecureappusage,fingerprintauthentica-
tion,instantpayment,anddigitalsignatures.
TherawdataundergoapreprocessingproceduretoprepareitfortheRLFDagent:
1. Chronologicalsorting: TransactionsarefirstgroupedbyclientIDandthensorted
chronologicallybytimestamptopreservetemporaldependencies.
2. Categoricalfeatureselection: Tomanagethehighdimensionalityofcategoricalvari-
ables, a two-stage selection process is applied. First, features are ranked by their
MutualInformation(MI)scorewithrespecttothefraudlabel,andthetop-Nfeatures
areretained. Then,foreachselectedfeature,onlythetop-Mmostfrequentvaluesare
preserved,withallothersaggregatedintoasingle“Other”category.
3. Encodingandscaling: Theselectedcategoricalfeaturesareone-hotencoded,whileall
numericalvariablesarenormalizedtothe[0,1]rangeusingMin–Maxscaling.
Finally,wenotethatsyntheticoversamplingtechniques(e.g.,SMOTE)wereexplicitly
excludedfromthepipeline. Insequentialdomains,generatingsynthetictransactionvectors
candisruptthetemporalcoherenceofclienthistories, introducinglook-aheadbiasand
invalidatingtheMarkovpropertyrequiredfortheRLagent.
3.2. UCICreditCardDefaultBenchmark
Toassessthegeneralizabilityofourframework,wealsoemploythepublic“Defaultof
CreditCardClients”datasetfromtheUCIMachineLearningRepository[14]. Thisdataset,
whichcontainsrecordsfor30,000uniqueclients,isastandardbenchmarkforclassification
tasks. Ithasbeenusedinnumerousstudies,includingarecentcomparativeanalysisof
various machine learning models for fraud detection by Seera et al. [10]. The dataset
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252
5of16
includesdemographicdataandasix-monthhistoryofbillamounts,paymentamounts,and
repaymentstatuses. Thetargetlabelindicateswhetheraclientdefaultedontheirpayment
inthesubsequentmonth,withadefaultrateofapproximately0.22.
Whilethedatasetcontainsasix-monthhistory,itisnotprimarilyknownforstrong,
long-termtemporalcorrelationsandistreatedintheliteratureasastatic,tabularproblem.
Thismakesitaparticularlychallengingbenchmarkforoursequentialmodel.Bytestingour
frameworkhere,weevaluateitsperformanceinascenariowhereitisnotinherentlyfavored
overtabular-optimizedmethodslikeGBT,whichcanprocessallfeaturessimultaneously.
Thisservesasatestofourmodel’sabilitytogeneralizeitsfeature-extractionanddecision-
makingcapabilitiestodifferentproblemstructures.
Sincethisdatasetisinawideformat(onerowperclient),aspecificpreprocessingstep
isrequiredtoadaptitforoursequentialmodel. Wetransformthedataintoalongformat,
creating a sequence of six time-steps for each client. Each time-step contains the client’s
staticdemographicfeaturescombinedwiththeirmonthlypayment/billingvariablesforthat
specificmonth.Thefinalclientlabel(defaultornot)ispropagatedtoallsixtime-stepsforthat
client.Theresultingfeaturesarethenone-hotencodedwhereappropriateandscaled.
3.3. Windowing
Forbothdatasets,theprocessedtime-seriesdataforeachclientaretransformedinto
overlappingslidingwindowsofafixedlengthwindow_size(w).Eachwindowservesasthe
staterepresentationfortheagent. Forclientswithfewerthanwtransactions,thesequences
areleft-paddedwithadistinctplaceholdervalue(−10),andabinarymaskisgeneratedto
differentiaterealobservationsfrompadding. Wewillrefertow(window_size)throughout.
3.4. RLFDFrameworkasaMarkovDecisionProcess(MDP)
We formulate the fraud detection task as an MDP [12] defined by the tuple
(S,A,R,P,γ):
• State (S): a state at time t, denoted s , is a window of w preprocessed transaction
t
∈Rw×d,wheredisthenumberoffeatures.
vectorsandisrepresentedasamatrixs
t
• hlAction (A): the agent takes one of two discrete actions at each time: a t ∈ {0,1},
|        | =0denotesclassifyingthetransactionasnormalanda |     |     |     | =1asfraudulent. |     |
| ------ | ---------------------------------------------- | --- | --- | --- | --------------- | --- |
| wherea | t                                              |     |     |     | t               |     |
• Reward (R): the reward r is asymmetric to reflect the higher cost of missing a
t
| fraudulenttransaction. |     | Giventhetruelabely |     | ∈ {0,1}, |     |     |
| ---------------------- | --- | ------------------ | --- | -------- | --- | --- |
t

|     |         | +           | =           | =                    |                         |     |
| --- | ------- | ----------- | ----------- | -------------------- | ----------------------- | --- |
|     |         | − r 1 | i f a t 1 a | n d y t 1 ( T r u e  | P o s it iv e , T P ) , |     |
|     |         | r           | i f a = 0 a | n d y = 1 ( F a ls e | N e g a ti v e , F N ), |     |
|     | r (a ,y | ) = 1       | t           | t                    |                         | (1) |
t t t
|     |     |  + r | i f a = 0 a | n d y = 0 ( T r u e  | N e g a t i v e , T N ), |     |
| --- | --- | ---------- | ----------- | -------------------- | ------------------------ | --- |
|     |     | 2          | t           | t                    |                          |     |
|     |     | −          | =           | =                    |                          |     |
|     |     | r 2        | i f a t 1 a | n d y t 0 ( F a ls e | P o si t i v e , F P ),  |     |
>r >0. Inconfigurationfilesthesearedenotedr1andr2.
| wherer | 1 2 |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
• TransitionKernel(P): statetransitionsaredeterministicwithinaclient’stransaction
history: the next state s is the subsequent overlapping window from the same
t+1
client’ssequence.
∈ [0,1)
• Discount Factor (γ): a scalar γ balancing immediate and future rewards
| (configurationkey: |     | gamma). |     |     |     |     |
| ------------------ | --- | ------- | --- | --- | --- | --- |
3.5. ModelArchitectureandTrainingStrategy
OuragentutilizesaDeepQ-Network(DQN)[15]withaLongShort-TermMemory
(LSTM)[16]encodertomodelsequentialdependencies. Whilethefundamentalnetwork
topologyisadoptedfromtheRLADframework[9],wedistinguishourapproachbyre-
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 6of16
engineeringtheinteractionloopforthefinancialdomain.Unlikegenericanomalydetection
tasks where errors may be symmetric, we implement an asymmetric reward structure
andastrictlychronologicalclient-centricwindowingmechanism. Thisensurestheagent
isoptimizednotjustforpatternrecognition,butforthespecificoperationalobjectiveof
maximizingfraudrecallunderimbalance. ThearchitectureisdepictedinFigure1.
PaddingMask InputStatest
w×d
LSTM
controls Selectlastvalid
w×H
hiddenstatehw
FullyConnected
Layer
Q(st,0) Q(st,1)
at
(ϵ-greedy)
at
gradients
rt
rt
NextStates t+1
TDLoss&Backprop
Transition(st,at,rt,s
t+1
)
sample
Replay
Mini-batch
Buffer
Figure1.Expandedagentarchitectureandtrainingloop.ThenetworkoutputsQ-valuesfornormal
andfraud;anϵ-greedyselectorchoosesat,leadingthroughtheenvironmenttortands t+1 .Thetransi-
tion(st,at,rt,s
t+1
)isappendedtothereplaybuffer(maxsize:replay_buffer_size).Mini-batches
from the buffer drive temporal-difference (TD) loss (model updated every target_update_freq
episodes)andbackpropagation(dashedarrows).Here,wisthewindowlength(window_size)andd
isthefeaturecount.
Theinputstates ispassedtotheLSTM,whichoutputsasequenceofhiddenstates.
t
Weextractthelastvalidhiddenstateh (usingthepaddingmask)asacompressedrepre-
w
sentationandsetz := h . Alinearlayerthencomputestheaction–valuevector:
w
Q(s ;θ) =Wz+b ∈R2, Q(s ,a;θ) = [Q(s ;θ)] , (2)
t t t a
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 7of16
whereθrepresentsthenetworkweights. Followingbestpractices[9],theLSTM’sforget-
gatebiasisinitializedto1.0.
TrainingisstabilizedusingtworelevantDQNmechanisms[15]:
• ExperienceReplay: Alltransitions (s t ,a t ,r t ,s t+1 ) arestoredinareplaybuffer. The
agentlearnsbysamplingmini-batchesfromthisbuffer. Themaximumreplaybuffer
size (replay_buffer_size) is treated as a hyperparameter and has been tuned to
balancesamplediversityandmemoryefficiency.
• TargetNetwork: Aseparate,fixedtargetnetworkQ′ isusedtogeneratethetemporal-
difference(TD)target,reducinginstabilitybydecouplingthetargetfromtheonline
network. TheTDtargety is
t
y t =r t +γmaxQ ′(s t+1 ,a ′ ;θ ′). (3)
a′
Theonlinenetworkparametersθareupdatedbyminimizingthemeansquarederror.
Thetargetnetworkparametersareupdatedduringtrainingwithafixedfrequency
(target_update_freq),whichisalsotunedasahyperparameter.
Training is structured into episodes, where each episode corresponds to the full
transactionhistoryofasingleclient. Anϵ-greedystrategyisusedforactionselection.
3.6. EvaluationStrategy
Ourevaluationstrategydiffersbetweenthetwodatasetstoadheretobestpractices
foreach.
• ProprietaryDataset: Weemployatwo-stageevaluation. First,forinitialdevelopment
andhyperparametertuning,weuseasingle,stratifiedholdoutsplit: training(0.64),
validation(0.16),andtesting(0.20). Duringthisstage,wesavethe“BestValidation
Model”thatmaximizesfraudrecallwhilemaintainingnormal-classrecallabovea
highthreshold(e.g.,0.90). Thisspecificselectioncriterionwasdrivenbythebank’s
operationalrequirements,whichmandatedaminimumfraudrecallof≈65%dueto
thehighimbalanceandthepatternoffraudulentbehavior. Consequently,ourtuning
process prioritized pushing the recall for the fraud class to reach this limit, rather
than solely optimizing global metrics like the Area Under the Receiver Operating
CharacteristicCurve(ROCAUC)ortheAreaUnderthePrecision–RecallCurve(PR
AUC)whichcanyieldlowdetectionratesinhighlyimbalancedscenarios. Second,for
amorerobustandunbiasedperformanceassessment,weconducta10-foldstratified
cross-validation. Thisallowsforadirectcomparisonagainstgradientboostedtrees
(GBT)baselines,whichwereevaluatedusingtheidenticalcross-validationscheme
anddatapreprocessing.
• UCIBenchmarkDataset: Forthisstandardbenchmark,weemploya10-foldstratified
cross-validationasinSeeraetal.[10].Ineachfold,thedataaresplitinto8foldsfortraining,
1forvalidation,and1fortesting. Afreshmodelistrainedforeachofthe10folds,and
itsbestperformance(basedonitsvalidationset)isevaluatedonthetestfold. Thefinal
reportedmetricsareaggregatedfromtheout-of-foldpredictionsfromall10runs.
3.7. PerformanceMetrics
Evaluatingtheperformanceoffrauddetectionmodelsrequiresasetofmetricsthat
handlesevereclassimbalanceandasymmetricmisclassificationcosts[1]. Throughout,we
definethepositiveclassasy =1(fraudfortheproprietarydatasetanddefaultfortheUCI
dataset). Theconfusion-matrixentriesTP,TN,FP,andFNarewithrespecttoy =1.
Accuracy:theoverallproportionofcorrectlyclassifiedinstancesrelativetoalltransactions:
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 8of16
TP+TN
Accuracy= . (4)
TP+TN+FP+FN
Whilecommonlyreported,Accuracycanbemisleadingunderextremeimbalance[17].
PrecisionandRecall: precision(PositivePredictiveValue)measurestheproportionof
correctlyidentifiedpositivesamongallpredictedpositives:
TP
Precision= . (5)
TP+FP
Recall (Sensitivity, True Positive Rate) measures the proportion of actual positives that
weredetected:
TP
Recall= . (6)
TP+FN
HighrecallreducesTypeIIerror(missedpositives),whereashighprecisionreducesTypeI
error(falsealarms)[18].
F1-Score: theharmonicmeanofPrecisionandRecall:
Precision·Recall
F1-Score=2· . (7)
Precision+Recall
Threshold-Independent Metrics: to assess ranking performance across thresholds,
wereporttheROCAUCandthePRAUC,thelatterbeingoftenmoreinformativeunder
imbalance[19].
4. Results
4.1. ProprietaryDatasetPerformanceonHoldoutSet
Themodelwasfirsttrainedonourproprietarydatasetusingtheholdoutsplitmethod-
ology. The specific hyperparameters, detailed in Table 1, were selected through a grid
search optimization process on the validation set. The rationale for the key parameter
choicesisasfollows:
• Reward Ratio (r1/r2 = 4): The positive reward for catching fraud (r1) is set four
times higher than the reward for correct normal classification (r2). This asymme-
tryisnecessarytocounteractthesevereclassimbalance(3.6%fraud),ensuringthe
agentfindsitmathematicallyadvantageoustopursuerarefraudeventsratherthan
convergingtoatrivial“alwaysnormal”policy.
• Exploration(epsilon_min=0.22): UnlikestandardRLtaskswhereϵoftendecaysto
0.01,wemaintainahigherminimumexplorationrate. ThispreventstheQ-network
fromoverfittingtothemajorityclassandencouragestheagenttocontinuouslytest
thedecisionboundaryaroundrareevents.
• FeatureThresholds(N=10,M=10): Theseparametersweretreatedashyperparame-
terswithintheoptimizationloop. Preliminarysensitivityanalysisonthevalidation
setindicatedthisconfigurationofferedtheoptimaltrade-off;increasingdimensions
beyondthispointintroducedstatesparsitythatdestabilizedtheDQNconvergence
withoutimprovingrecall,whilelowervaluesdiscardedpredictivesignal.
• replay_buffer (80): A constrained buffer size was chosen to ensure the agent
learns from relatively fresh, on-policy experiences, which is beneficial given the
non-stationarynatureofusertransactionpatterns.
• window_size(18): Empiricallydeterminedtobalancethecaptureofsufficienttempo-
ralcontextagainsttheinclusionofirrelevanthistoricalnoise.
TheperformanceinTable2indicatesthattheBestValidationModelissuperiorfor
frauddetection,achievingafraudrecallof0.67.Thisperformancereflectsadeliberatetrade-
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252
9of16
offdrivenbyourvalidationstrategy: themodelidentifiesmostfraudswhilemaintaining
arecallof0.90fornormaltransactions. Itisimportanttonotethattheachievedrecallof
0.67satisfiestheexplicitrequirementtopushfraudrecallabove65%,thussacrificingsome
accuracy. ThisdemonstratesthattheRLFDagentcanbeeffectivelytunedtomeetstrict
operationalthresholdsthatprioritizedetectingrareevents,acapabilityoftencompromised
whenoptimizingsolelyforstandardaggregatedmetrics.
Table 1. Hyperparameter configuration and training parameters for the RLFD Agent (propri-
etarydataset).
|     | Hyperparameter |     |     | Value |     |
| --- | -------------- | --- | --- | ----- | --- |
Preprocessing&ModelArchitecture
window_size
18
|     | hidden_size(LSTM) |     |     | 64  |     |
| --- | ----------------- | --- | --- | --- | --- |
|     | Top-NFeaturesN    |     |     | 10  |     |
|     | Top-MCategoriesM  |     |     | 10  |     |
Training
|     | learning_rate            |     |     | 0.001 |     |
| --- | ------------------------ | --- | --- | ----- | --- |
|     | gamma                    |     |     | 0.95  |     |
|     | batch_size               |     |     | 8     |     |
|     | replay_buffer_size       |     |     | 80    |     |
|     | inner_epochs             |     |     | 200   |     |
|     | target_update_freq       |     |     | 40    |     |
|     | epsilon_min              |     |     | 0.22  |     |
|     | r1(Positive-classreward) |     |     | 4.0   |     |
r2(Negative-classreward)
1.0
Table2.Performanceontheproprietarydatasettestset(holdoutsplit).Allmetricsareproportions
in[0,1].Thebestrecallforthefraudclass,obtainedwiththeBestValidationModel,isinbold.
Class-WisePerformance
| Model |     |     |     | OverallAccuracy |     |
| ----- | --- | --- | --- | --------------- | --- |
Precision(Normal) Recall(Normal) Precision(Fraud) Recall(Fraud)
| FinalModel          | 0.98 | 0.93 | 0.21 | 0.53 | 0.9160 |
| ------------------- | ---- | ---- | ---- | ---- | ------ |
| BestValidationModel | 0.99 | 0.90 | 0.19 | 0.67 | 0.8903 |
4.2. Cross-ValidationBenchmarkonProprietaryDataset
Toprovideamorerobustevaluation,weconducteda10-foldcross-validationonthe
proprietarydataset,comparingourRLFDframeworkagainstGBTbaselines. Theresults,
averagedacrossthe10folds,arereportedinTable3.
ThestandardGBTmodeldemonstratesstrongstatisticalcapabilities,achievingthe
highestoverallROCAUC(0.886)andPRAUC(0.443),asevidencedinFigure2. Thisindi-
catesthatthetree-basedmodelishighlyeffectiveatrankingtransactionsanddistinguishing
classeswhenthedecisionthresholdisoptimizedglobally. However,atthedefaultdecision
±
threshold of 0.5, the GBT yields a low recall for the fraud class (0.226 0.042), heavily
favoringprecision. Applyingclassweighting(GBTWeighted)improvestherecallto0.450,
butstillfallsshortoftheRLFDagentinpuresensitivity. Infact,theRLFDframework,while
achievingloweraggregaterankingmetrics(ROCAUC0.773,PRAUC0.222),successfully
learnsanaggressivepolicyfromtheasymmetricrewardsignal. Itachievesthehighest
fraudrecallof0.549±0.062,directlymeetingtheoperationalrequirementtoprioritizethe
detectionofrareevents. Toassessstatisticalsignificance,werelyonthestandarddeviation
across the 10 folds as a proxy for confidence intervals. The RLFD fraud recall presents
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 10of16
a distribution that is strictly superior to the standard GBT with no overlap in the ±1σ
intervals,confirmingthesignificanceofthesensitivityimprovement.
ThediscrepancybetweenthehighrecallandlowerAUCsuggeststhatwhiletheRLFD
agent is less precise globally, it is particularly effective at flagging a specific subset of
suspiciousactivitiesthatalignwiththehigh-rewardcriteria.
Table3.10-foldcross-validationperformanceontheproprietarydataset.Valuesaremean±std.dev.
across10folds.
Model Accuracy ROCAUC PRAUC Recall(Normal) Recall(Fraud) Precision(Fraud) F1(Fraud)
GBT 0.969±0.002 0.886±0.010 0.443±0.030 0.997±0.001 0.226±0.042 0.726±0.066 0.343±0.051
GBT(Weighted) 0.962±0.002 0.891±0.012 0.445±0.030 0.981±0.001 0.450±0.029 0.474±0.030 0.462±0.029
RLFD 0.906±0.012 0.773±0.041 0.222±0.042 0.919±0.012 0.549±0.062 0.197±0.028 0.289±0.036
(a) (b)
(c) (d)
Figure2. AggregatedROCandPrecision–Recallcurvesfromthe10-foldcross-validationonthe
proprietarydataset,comparingtheRLFD(DQN-based)frameworkandtheGBTmodel.(a)RLFD
GlobalROCCurve.(b)RLFDGlobalPrecision–RecallCurve.(c)GBTGlobalROCCurve.(d)GBT
GlobalPrecision–RecallCurve.IntheROCplots(a,c),thebluedasheddiagonallinerepresentsthe
performanceofarandomclassifier(AUC=0.5).
4.3. OrthogonalityandComplementaryDetection
TobetterunderstandtheoperationalvalueoftheRLFDframeworkbeyondaggre-
gate metrics, we performed a dynamic orthogonality analysis. Instead of relying on a
singleoverlapsnapshot,weexaminedtheintersectionofdetectedfraudsacrossdifferent
operatingpointsontheholdoutset.
Figure 3a displays the overlap composition as a function of the target fraud recall.
Whilethesymmetrybetweentheuniquesetsismathematicallyenforcedbyequatingthe
recallofbothmodels,themagnitudeoftheseuniquesetsisrelevant. Ifthemodelsrelied
on similar decision boundaries, the “Common” area would dominate and the unique
bandswouldbenegligible. Instead,thepersistentwidthofthe“UniquetoRLFD”band
demonstratesthatforanygivensensitivitylevel,theRLFDagentcapturesasubstantial
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 11of16
volumeoffraudthattheGBTinherentlymisses, provingthattheagentisnotmerelya
redundantclassifierbutasourceoforthogonalinformation.
Figure 3b visualizes the overlap as a function of the decision threshold, moving
fromstrict(highprobability)toloose(lowprobability)classifiers. Atverystrictthresholds
(e.g.,>0.8),theRLFDagentisnotablymoreeffective,capturingthevastmajorityofdetected
frauds. EvenasthethresholdisloweredandtheGBTbecomesmoreeffective,theRLFD
agentcontinuestocontributeadistinctsetofuniquedetections,comprisingapproximately
30%ofthetotalunionofdetectedfraudsatthreshold0.4,andover40%uniquecasesat
threshold0.5,thatarenevercapturedbythetree-basedmodel.Thispersistentorthogonality
confirmsthatthetwomodelsrelyonfundamentallydifferentdecisionboundaries: the
GBTexploitsfeatureinteractionsintabularspace,whiletheRLagentleveragestemporal
transitionstocatchsequentialanomalies.
(a)Overlapvs.TargetRecall
(b)Overlapvs.DecisionThreshold
Figure3.DynamicorthogonalityanalysisbetweentheRLFDagentandtheGBTbaseline.(a)Evolu-
tionoffraudoverlapasafunctionoftargetfraudrecall(sensitivity).(b)Evolutionoffraudoverlap
asafunctionofthedecisionthreshold(probabilitycut-off),orderedfromstrict(1.0)toloose(0.0).In
bothviews,theblueareahighlightstheuniquecontributionoftheRLFDagent,whichpersistsacross
alloperatingpoints.
4.4. UCIBenchmarkPerformance
Toaddressourthirdresearchquestionregardinggeneralizability,weevaluatedthe
frameworkontheUCICreditCardDefaultdataset. Thisenvironmentdiffersfundamen-
tallyfromtheproprietarybankdataset: thesequencesareshort(only6time-steps),the
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252
12of16
granularity is coarse (monthly aggregates vs. timestamps), and the class imbalance is
moderate(22%vs. 3.6%).
Consequently,theagent’shyperparametersrequiredlogicaladaptation,asdetailed
in Table 4. The window_size was reduced to 4 to accommodate the limited six-month
history available per client. Furthermore, the positive reward scalar (r1) was lowered
from4.0to3.0;becausethedefaultclassislessrarethanbankingfraud,theagentrequires
lessaggressiveincentivizationtolearntheminorityclassdistribution.
Table4.KeyhyperparametersfortheUCIbenchmarkexperiment.
| Hyperparameter           | Value |     |
| ------------------------ | ----- | --- |
| window_size              |       | 4   |
| hidden_size(LSTM)        |       | 32  |
| r1(Positive-classreward) |       | 3.0 |
r2(Negative-classreward)
1.0
| learning_rate | 0.001 |     |
| ------------- | ----- | --- |
The comparative results are presented in Table 5. Our RLFD framework achieves
an Accuracy of 0.802 and a ROC AUC of 0.696. When compared to the suite of static
classifiersevaluatedbySeeraetal.[10],theRLagentperformscompetitivelywithstandard
distance-basedmethods(e.g.,k-NN)buttrailsbehindensembletreemethodslikeGBT
(Accuracy0.821,ROCAUC0.778).
This result provides a relevant boundary condition for our research questions. It
suggeststhattheRLFDframework’sadvantageisheavilydependentonthepresenceof
high-frequencysequentialsignals. IntheUCIdataset,wheretemporalresolutionislow
(monthly snapshots) and feature interactions are largely static, the GBT leverage their
superiorabilitytopartitiontabularspace. However,thefactthattheRLagentmaintainsro-
bustperformance(within2%Accuracyofthestate-of-the-art)despitebeingarchitecturally
optimizedforsequentialtasksconfirmsitsflexibilityacrossdifferentfinancialdomains.
Table 5. Comparison of RLFD performance on the UCI benchmark against results reported by
Seeraetal.[10]. BoldvaluesindicatetheperformanceoftheproposedRLFDframework. Source
resultsfromFengetal.[20]andJadhavetal.[21]. Accuracyisreportedasaproportionin[0,1].
Acronyms: k-NN,k-nearestneighbours;NB,NaïveBayes;SVM,supportvectormachine;BagDT,
baggeddecisiontrees;BagNN,baggedneuralnetworks;BagSVM,baggedsupportvectormachines.
| Model             | Accuracy | ROCAUC |
| ----------------- | -------- | ------ |
| k-NN[21]          | 0.8080   | 0.627  |
| NB[21]            | 0.7136   | 0.699  |
| SVM[20]           | 0.8200   | 0.643  |
| RandomForest[20]  | 0.8200   | 0.625  |
| BagDT[20]         | 0.8200   | 0.665  |
| BagNN[20]         | 0.8200   | 0.660  |
| BagSVM[20]        | 0.8100   | 0.620  |
| NeuralNetwork[20] | 0.8205   | 0.660  |
| GBT[10]           | 0.8206   | 0.778  |
| RLFD              | 0.8016   | 0.696  |
5. Discussion
This study aimed to evaluate the efficacy of reinforcement learning for financial
frauddetection,specificallyaddressingthecapabilityofsequentialagentstoidentifyrare
eventsinhighlyimbalanceddomains. Interpretingourfindingsthroughthelensofthe
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 13of16
primaryresearchquestionsrevealsadistincttrade-offbetweenstatisticalrankingpower
andoperationalcoverage.
Regardingthefirstresearchquestionondetectionefficacy,theempiricalresultson
the proprietary dataset affirm that the RLFD agent can achieve superior recall for rare
eventscomparedtostaticbaselines. WhilethestandardGBTmodelprioritizedprecision,
resultinginalowfraudrecallof0.226,theRLFDagentleveragedtheasymmetricreward
signal(r /r =4)toachieveafraudrecallof0.549. Thisdemonstratesthatinoperational
1 2
contextswherethefinancialliabilityofafalsenegativevastlyoutweighsthefrictioncostof
afalsepositive,theRLframeworkoffersamoretunableandeffectiveoptimizationobjec-
tivethanstandardcross-entropylossminimization. Regardingcomputationalefficiency,
theRLFDframeworkrequiressignificantlyhighertrainingresourcescomparedtoGBT
(approximately2×wall-clocktimeinourexperiments)duetotheepisodicnatureofthe
interactionloop. However,inferencelatencyremainscomparable,asthetrainedQ-network
processessequencewindowsinconstanttime.
Themostrelevantfinding,however,addressestheoperationalorthogonalityofthe
models.ThedynamicorthogonalityanalysispresentedinFigure3providesstrongevidence
thattheRLFDframeworkdetectsadistinctsubsetoffraudulentactivities. Thepersistence
ofthe“UniquetoRLFD”detectionbandacrosstheentirethresholdspectrumindicates
thattheagentisnotmerelyactingasanoisierclassifier,butissensitivetofundamentally
differentpatternsthatareinvisibletothetree-basedmodel. Notably,athigh-confidence
thresholds,theRLagentcontributedover30%oftheuniquedetections. Thisconfirmsits
valueasacomplementarysafetynetthatcapturestemporalcorrelationsmissedbythe
independenceassumptionofstaticclassifiers.
Todefinetheboundaryconditionsofthisapproach,weexaminedtheframework’s
performance on the UCI benchmark, which lacks high-frequency temporal data. The
resultsshowthatwhileRLFDiscompetitive(Accuracy0.802),itdoesnotoutperformthe
GBT(Accuracy0.821)inpurelytabularenvironments. Thisestablishesaclearlimitation:
theRLFDframeworkprovidesmaximumvalueindomainswithrichsequentialsignals
(e.g.,timestampedbankinglogs)andoffersdiminishingreturnsinstaticclassificationtasks
wherefeatureinteractionsdominate.
These findings have both theoretical and practical implications. Theoretically, the
studyreinforcesthedistinctionbetweenclassificationerrorminimizationandoperational
utilitymaximization.ByframingfrauddetectionasaMarkovDecisionProcess,thedecision
boundaryisallowedtoevolvebasedonthesequentialstateoftheclient,contrastingwith
thefixedhyperplaneapproachesofsupervisedlearning. Methodologically,ouranalysis
highlights the danger of relying solely on global metrics like ROC AUC or Accuracy
in highly imbalanced settings, a choice made on the UCI benchmark to align with the
comparativeanalysisbySeeraetal.[10]. AsshowninTable3,amodelcanachievesuperior
ROC AUC (0.886 vs. 0.773) while failing the primary business objective of detecting
fraud(Recall0.22vs. 0.55). Consequently,futurecomparisonsshouldprioritizethreshold-
dependentmetricsanddynamicoverlapanalyses.Fromapracticalstandpoint,thefindings
speak against a “winner-takes-all” model selection. The optimal strategy for financial
institutions is possibly an hybrid parallel deployment: using GBTs as a primary high-
precisionfilter,whiledeployingRLagentsinparalleltointerceptthesignificantfractionof
complex,sequentialattacksthatbypassstaticrules.
6. Conclusions
We adapted and evaluated a Reinforcement Learning for Fraud Detection (RLFD)
framework alongside a Gradient Boosted Trees (GBTs) baseline on both a proprietary,
real-world financial dataset and a public credit default benchmark. The investigation
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 14of16
revealsthatstatisticalsuperiority(asmeasuredbyAreaUndertheCurve,AUC)doesnot
necessarilyimplyoperationalcompleteness. WhiletheGBTbaselineprovidesarobust
primaryfilterwithhighprecision,ourdynamicorthogonalityanalysisprovesitremains
blind to specific anomalies across the entire decision spectrum. The RLFD framework,
employinganepisodictrainingloop,asymmetricrewardshaping,andLSTM-basedstate
encoding, successfullycapturestheseelusivepatterns. Ontheproprietarydataset, this
approachconsistentlyidentifiesauniquesetoffraudulenttransactionsthattheGBTmisses;
conversely, on the static public benchmark, the sequential advantage diminishes. We
thereforecautionthatthemagnitudeofthecomplementaryeffectobservedhere(e.g.,the
≈30%uniquedetections)islikelydataset-dependentandcontingentontheprevalenceof
high-frequencysequentialpatternsinthetargetfinancialstream.
We conclude that the optimal deployment strategy for financial fraud detection is
notamonolithicchoicebetweenstaticorsequentialmodels,butratherahybridparallel
architecture. In such a system, the RLFD agent serves as a specialized “safety net” for
complex,sequence-dependentfraudscenariosthatevadetraditionaltree-basedclassifiers,
therebysignificantlyenhancingthetotalfraudcoverageofthebankingsystem. Future
evolutionofthisframeworkwillfocusontheintegrationofExplainableAI(XAI)methods
to bridge the gap between the high sensitivity of Deep RL agents and the regulatory
requirementforinterpretabilityinthefinancialsector.
AuthorContributions:Conceptualization,A.P.;Methodology,A.P.;Software,A.P.;Validation,A.P.;
Formalanalysis,A.P.;Investigation,A.P.;Writing—originaldraft,A.P.;Writing—review&editing,
A.P.,B.C.,P.L.andR.C.;Visualization,A.P.andP.L.;Supervision,P.L.andR.C.Allauthorshaveread
andagreedtothepublishedversionofthemanuscript.
Funding:ThisresearchwasfundedbytheEuropeanUnion—NextGenerationEUundertheNational
RecoveryandResiliencePlan(PNRR)—Missione4“IstruzioneeRicerca”—Componente2“Dalla
Ricercaall’Impresa”—Investimento1.4“CampioninazionalidiR&S”,Project“NationalCentrefor
HPC,BigDataandQuantumComputing”—CN1(Spoke2)“Simulazioni,calcoloeanalisideidatiad
alteprestazioni”,CUP:B83C22002830001.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Theproprietarydatasetusedinthisstudyconsistsofbanktransactions
protectedbylegalandcontractualrestrictions;rawdatacannotbeshared. Thepublicbenchmark
datasetisavailableattheUCIMachineLearningRepositoryathttps://archive.ics.uci.edu/dataset/
350/default+of+credit+card+clients(accessedon21December2025).
Acknowledgments:WethankIntesaSanpaoloforprovidingtheanonymizeddatasetforthisresearch.
Theviewsandopinionsexpressedarethoseoftheauthorsanddonotnecessarilyreflecttheviewsof
IntesaSanpaolo,itsaffiliates,oritsemployees.
ConflictsofInterest:AuthorRiccardoCrupiwasemployedbythecompanyIntesaSanpaoloS.p.A.
Theremainingauthorsdeclarethattheresearchwasconductedintheabsenceofanycommercialor
financialrelationshipsthatcouldbeconstruedasapotentialconflictofinterest.
Abbreviations
Thefollowingabbreviationsareusedinthismanuscript:
APP AuthorizedPushPayment
ATO AccountTakeover
AUC AreaUndertheCurve
BagDT BaggedDecisionTrees
BagNN BaggedNeuralNetworks
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 15of16
BagSVM BaggedSupportVectorMachines
BIC BankIdentifierCode
DQN DeepQ-Network
GBT GradientBoostedTrees
ISP IntesaSanpaolo
k-NN k-NearestNeighbours
LSTM LongShort-TermMemory
MDP MarkovDecisionProcess
MI MutualInformation
NB NaïveBayes
PR Precision–Recall
RL ReinforcementLearning
RLAD ReinforcementLearningforAnomalyDetection
RLFD ReinforcementLearningforFraudDetection
ROC ReceiverOperatingCharacteristic
SHA-256 SecureHashAlgorithm256-bit
SVM SupportVectorMachine
TD TemporalDifference
UCI UniversityofCaliforniaIrvine(Repository)
XAI ExplainableArtificialIntelligence
References
1. Compagnino,A.A.;Maruccia,Y.;Cavuoti,S.;Riccio,G.;Tutone,A.;Crupi,R.;Pagliaro,A. Anintroductiontomachinelearning
methodsforfrauddetection. Appl.Sci.2025,15,11787.[CrossRef]
2. HernandezAros,L.;BustamanteMolano,L.X.;Gutierrez-Portela,F.;MorenoHernandez,J.J.;RodríguezBarrero,M.S. Financial
frauddetectionthroughtheapplicationofmachinelearningtechniques:Aliteraturereview. Humanit.Soc.Sci.Commun.2024,
11,1130.[CrossRef]
3. Ali,A.;AbdRazak,S.;Othman,S.H.;Eisa,T.A.E.;Al-Dhaqm,A.;Nasser,M.;Elhassan,T.;Saif,A. Financialfrauddetectionbased
onmachinelearning:Asystematicliteraturereview. Appl.Sci.2022,12,9637.[CrossRef]
4. Al-Hashedi,K.G.;Magalingam,P. Financialfrauddetectionapplyingdataminingtechniques:Acomprehensivereviewfrom
2009to2019. Comput.Sci.Rev.2021,40,100402.[CrossRef]
5. West, J.; Bhattacharya, M. Intelligent financial fraud detection: A comprehensive review. Comput. Secur. 2016, 57, 47–66.
[CrossRef]
6. Abdallah,A.;Maarof,M.A.;Zainal,A. Frauddetectionsystem:Asurvey. J.Netw.Comput.Appl.2016,68,90–113.[CrossRef]
7. Ngai,E.W.T.;Hu,Y.;Wong,Y.h.;Chen,Y.;Sun,X. Theapplicationofdataminingtechniquesinfinancialfrauddetection: A
classificationframeworkandanacademicreviewofliterature. Decis.SupportSyst.2011,50,559–569.[CrossRef]
8. Bolton,R.J.;Hand,D.J. Statisticalfrauddetection:Areview. Stat.Sci.2002,17,235–255.[CrossRef]
9. Wu,T.;Ortiz,J. RLAD:Timeseriesanomalydetectionthroughreinforcementlearningandactivelearning. InProceedings
ofthe7thACMSIGKDDWorkshoponMiningandLearningfromTimeSeries(MiLeTS’21),VirtualEvent,Singapore,14–18
August 2021.
10. Seera,M.;Lim,C.P.;Kumar,A.;Dhamotharan,L.;Tan,K.H. Anintelligentpaymentcardfrauddetectionsystem. Ann.Oper.Res.
2024,334,445–467.[CrossRef][PubMed]
11. Jurgovsky, J.; Granitzer, M.; Ziegler, K.; Calabretto, S.; Portier, P.E.; He-Guelton, L.; Caelen, O. Sequence classification for
credit-cardfrauddetection. ExpertSyst.Appl.2018,100,234–245.[CrossRef]
12. Sutton,R.S.;Barto,A.G. ReinforcementLearning:AnIntroduction,2nded.;MITPress:Cambridge,MA,USA,2018.
13. Penard,W.;VanWerkhoven,T. Onthesecurehashalgorithmfamily. InCryptographyinContext;Wiley:Hoboken,NJ,USA,2008;
pp.1–18. Availableonline:https://blog.infocruncher.com/resources/ethereum-whitepaper-annotated/On%20the%20Secure%
20Hash%20Algorithm%20family%20%282008%29.pdf(accessedon21December2025).
14. Dua, D.; Graff, C. UCIMachineLearningRepository. 2019. Availableonline: http://archive.ics.uci.edu/ml (accessedon
10November2025).
15. Mnih, V.; Kavukcuoglu, K.; Silver, D.; Rusu, A.A.; Veness, J.; Bellemare, M.G.; Graves, A.; Riedmiller, M.; Fidjeland, A.K.;
Ostrovski,G.;etal. Human-levelcontrolthroughdeepreinforcementlearning. Nature2015,518,529–533.[CrossRef][PubMed]
16. Hochreiter,S.;Schmidhuber,J. Longshort-termmemory. NeuralComput.1997,9,1735–1780.[CrossRef]
https://doi.org/10.3390/app16010252

Appl.Sci.2026,16,252 16of16
17. Ramírez-Alpízar,A.;Jenkins,M.;Martínez,A.;Quesada-López,C. Useofdataminingandmachinelearningtechniquesforfraud
detectioninfinancialstatements:Asystematicmappingstudy. RISTI—Iber. J.Inf. Syst. Technol. 2020,E28,97–109. Available
online:https://www.risti.xyz/issues/ristie28.pdf(accessedon21December2025).
18. Bakumenko,A.;Elragal,A. Detectinganomaliesinfinancialdatausingmachinelearningalgorithms. Systems2022,10,130.
[CrossRef]
19. Saito,T.;Rehmsmeier,M. Theprecision–recallplotismoreinformativethantheROCplotwhenevaluatingbinaryclassifierson
imbalanceddatasets. PLoSONE2015,10,e0118432.[CrossRef][PubMed]
20. Feng,X.;Xiao,Z.;Zhong,B.;Qiu,J.;Dong,Y. Dynamicensembleclassificationforcreditscoringusingsoftprobability. Appl.Soft
Comput.2018,65,139–151.[CrossRef]
21. Jadhav,S.;He,H.;Jenkins,K. Informationgaindirectedgeneticalgorithmwrapperfeatureselectionforcreditrating. Appl.Soft
Comput.2018,69,541–553.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/app16010252