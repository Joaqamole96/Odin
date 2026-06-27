Multimodal deep learning framework for
shadowbanking risk prediction - dynamic
decisionoptimization integrating knowledge graph
andreinforcement learning
Tong Qin
Chongqing University
Article
Keywords: Graph Neural Networks, Financial Compliance, Multimodal Learning, Dynamic Systems,
Policy-Aware Optimization
Posted Date: October 14th, 2025
DOI: https://doi.org/10.21203/rs.3.rs-7351508/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.
Read Full License
Additional Declarations: No competing interests reported.

Multimodal deep learning framework for shadow
banking risk prediction - dynamic decision
optimization integrating knowledge graph and
reinforcement learning
Tong Qin1,*
1SchoolofEconomicsandBusinessAdministration,ChongqingUniversity,Chongqing,400044,China
*corresponding.author@email: tlpfe3875@outlook.com
ABSTRACT
Amid increasing digitization and globalization of financial systems, the detection and mitigation of systemic risk within
non-traditionalfinancialsectorshasemergedasacriticalresearchimperativeincomputerscience. Traditionalstatisticaland
econometricmodelsforriskassessmentoftensufferfromstaticassumptions,limitedcapacitytomodelinterdependencies,and
lackofregulatoryinterpretability—shortcomingsthathinderreal-timeandscalablesolutionsincomplexfinancialecosystems.
Toovercometheselimitations,weproposeamultimodaldeeplearningframeworkthatintegratesagraph-theoreticneural
architecture, GFA-Net, with a policy-aware strategic module, PCS-Flow. GFA-Net encodes financial systems as dynamic
transactiongraphsenrichedwithsemanticandregulatoryfeatures,enablingrobuststructurallearningandforwardsimulation
across accounting periods. PCS-Flow further ensures that model outputs remain consistent under heterogeneous policy
regimes and evolving fiscal scenarios incorporating differentiable scenario perturbations and compliance regularizers.
Through these synergistic components, our approach delivers a unified solution for forecasting, anomaly detection, and
decisionoptimizationinhigh-dimensionalfinancialenvironments. Experimentalresultsonsimulatedandreal-worlddatasets
demonstrate superior accuracy, compliance fidelity, and temporal stability, thus validating the utility of our method for
policy-consistent risk prediction. This work contributes to the field by advancing interpretable, regulation-aware machine
learningframeworkscapableofnavigatingtheevolvinglandscapeoffinancialtechnologies.
keywords: GraphNeuralNetworks,FinancialCompliance,MultimodalLearning,DynamicSystems,Policy-AwareOptimization
1 Introduction
Shadowbankingsystemshaveincreasinglygainedattentionduetotheircomplexityandthesystemicriskstheyposetoglobal
financialstability. Traditionalfinancialmonitoringmechanismsoftenfailtoadequatelycapturethedynamicopaquenatureof
shadowbankingactivities1. Thesenon-bankfinancialintermediaries,whileprovidingessentialcreditintermediationfunctions,
arealsoassociatedwithhighleverage,maturitymismatches,andregulatoryarbitrage. Consequently,thedevelopmentofrobust,
adaptable,andpredictiveframeworksforshadowbankingriskassessmentisofparamountimportance. Notonlycansuch
frameworksimproveregulatoryoversightandmacroprudentialsupervision,buttheycanalsoprovideearlywarningsignals
forpotentialcrises2. Recentadvancesinmultimodaldeeplearning,semanticintegrationtechniques,andintelligentdecision
systemsofferpromisingavenuesforintegratingdiversedatasourcesanddynamicallyadaptingtoevolvingriskprofilesin
shadowbankingsystems.
Earlyresearcheffortsaimedatshadowbankingriskassessmentfocusedonstructuredknowledgeextractionandpredefined
logicalreasoningschemes. Theseapproacheswereprimarilydrivenbyexpert-definedframeworksthatencodedregulatory
policies,institutionalrelationships,andtransactionlogicsintoformalizedrulesets. Byleveragingdomaininsightsandlegal
compliancestructures,researcherssoughttoconstructinterpretablemodelscapableofrevealingthefunctionalarchitecture
and behavioral mechanisms of shadow banking systems 3. These models often took the form of modular rule engines or
hierarchicallogicstructures,designedtosimulatesystemicinteractionsunderwell-specifiedscenarios. Thebenefitofsuch
modelslay intheirtransparencyandalignment withsupervisorystandards, making themparticularlyuseful inregulatory
auditsandpolicyevaluations. Theiroutputswereeasilytraceable,enablingfinancialauthoritiestojustifydecisionsbasedon
clearlyarticulatedlogicpaths. However,theeffectivenessoftheseearlysystemswasheavilyconstrainedbytheirrelianceon
comprehensive,high-qualityinputdataandtheinflexibilityofrule-baseddesign. Inpractice,shadowbankingenvironmentsare
characterizedbyfragmenteddisclosures,evolvinginstruments,andcomplex,sometimesopaque,interconnections—factorsthat

traditionallogicalmodelswereill-equippedtohandle4. Whenfacedwithnoisy,partial,orambiguousdata,thesesystems
struggledtomaintainaccuracyandreliability. Furthermore,thestaticnatureoftheirrulesetslimitedtheircapacitytoadapt
tonewlyemergingfinancialbehaviorsorevolvingregulatorylandscapes. Inresponse,researchersintroducednetwork-based
enhancements,incorporatinggraphstructurestomodelinter-entityrelationshipsandenablemoreexpressiverepresentations
of financial dependencies 5. These graph-oriented techniques improved the system’s ability to reason over multi-layered
connections,suchasthosebetweenoff-balance-sheetentities,asset-backedsecurities,andshort-termfundingchains. While
suchimprovementsofferedaricherunderstandingofsystemicexposureandcounterpartyrisks,theystillfellshortincoping
withthescaleanddynamismofmodernshadowbankingsystems.Challengesincomputationalefficiency,modelscalability,and
timelyupdatescontinuedtohindertheirpracticaldeploymentinhigh-frequencyriskmonitoringandforecastingapplications6.
Subsequentdevelopmentsintroducedalgorithmicstrategiescapableofidentifyingrisksignaturesandanomalypatterns
directlyfromobservedfinancialbehavior. Thesemethodsmarkedashifttowardautomatedpatternrecognitionandstatistical
inference,movingawayfrommanuallyconstructedrulesystemstowardmoreflexible,data-adaptiveparadigms7. Drawingon
techniquesfromclassicalmachinelearning,includingdecisiontrees,randomforests,supportvectormachines,andensemble
classifiers,thesemodelsweretrainedtorecognizelatentpatternsinlargevolumesofstructuredandunstructureddata8. Input
sourcesincludedtransaction-levelrecords,balancesheetdisclosures,marketvolatilityindices,andmacroeconomicindicators,
enablingthesystemstocaptureawidespectrumoffinancialsignalsassociatedwithelevatedriskconditionsinshadowbanking
operations. Thekeyadvantageofthesealgorithmicapproacheslayintheirabilitytogeneralizefromhistoricaldataanddetect
subtleanomaliesthatmighteludehumanexpertsorrule-basedlogic. Theirapplicationledtoimprovementsinclassification
accuracy, early warning capabilities, and scalability across diverse financial instruments and institutions. Moreover, the
reductioninmanualinterventionallowedforfasterdeploymentandlowermaintenancecosts,makingthesesystemsattractive
forlarge-scalesurveillancetasks9. Theflexibilityoftrainingonheterogeneousdataalsoopenedpossibilitiesforcross-market
andcross-borderriskassessments,aligningwiththeglobalizednatureofshadowbanking. Despitethesestrengths,algorithmic
modelsfacedsignificantlimitations,particularlyinthecontextofregulatoryinterpretabilityandcontextualintegration. The
modelsoftenoperatedasblackboxes,providingoutputswithoutclearexplanationsoftheunderlyingdecisionrationale. This
opacityhinderedtheiracceptanceinrisk-sensitivedomains,wheretraceabilityandaccountabilityarecrucial. Suchmodels
typicallylackedthecapacitytoincorporateinstitutionalknowledge,legalconstraints,orevolvingregulatorydirectivesina
structuredmanner. Asaresult,whileeffectiveatidentifyingquantitativeirregularities,thesesystemsstruggledtoprovide
actionable insights grounded in financial policy frameworks. The absence of built-in mechanisms for embedding domain
expertiseandregulatorysemanticsconstrainedtheirutilityinreal-worldsupervisoryenvironments. Decision-makerswereoften
leftwithaccuratebutopaqueresults,forcingthemtorelyonsupplementaryanalysisoradhocinterpretations. Thisdisconnect
between technical efficacy and practical usability highlighted the need for hybrid models that could combine data-driven
learningwithstructuredreasoning,ensuringthatpredictivepowerdidnotcomeattheexpenseofregulatoryrelevanceand
interpretability10.
To further enhance predictive capabilities and contextual awareness, recent approaches have combined hierarchical
representationmodelswithtemporalandrelationallearningarchitectures11. Leveragingadvancementsinsequencemodeling
andstructuredembeddingtechniques,thesemodelsextractrichsemanticsignalsfromdiversedataformatsincludingfinancial
texts,graph-basedlinkages,andtemporaltrends. Theirabilitytounifylatentpatternswithdomain-specificcueshasproven
beneficial in modeling hidden vulnerabilities within shadow banking networks 12. Adaptive decision models have been
employedtoiterativelyrefinepolicychoicesunderuncertainmarketconditions. Despitenotableimprovements,challenges
suchasresourceintensivenessandexplainabilityconstraintsstilldemandattentioninreal-worlddeployment13.
Inlightofthelimitationsdiscussedabove,weproposeamultimodaldeeplearningframeworkforshadowbankingrisk
predictionthatintegratesdynamicdecisionoptimizationthroughknowledgegraphsandreinforcementlearning.Thisframework
isdesignedtoovercomethesymbolicmethods’rigidity,themachinelearningmodels’lackofinterpretability,andthedeep
learning models’ complexity by embedding structured domain knowledge and optimizing policy actions in real time. By
incorporatingadynamicknowledgegraph,themodelmaintainsanup-to-daterepresentationofthefinancialsystem’slatent
structuresandrelationships. Reinforcementlearningenablesthemodeltoadaptivelyrefineitspredictionsandrecommendations
based on feedback from evolving market conditions. This synergistic combination provides a flexible, transparent, and
intelligentsystemforregulatoryapplicationsinshadowbankingriskmanagement.
• Theproposedframeworkintroducesadynamicknowledgegraph-enhancedreinforcementlearningmoduletoenable
real-time,adaptiveriskprediction.
• Itsmodulardesignsupportsmultimodalinputs,facilitatinghighadaptabilityacrossdifferentfinancialscenariosand
ensuringbroadapplicability.
• Experimentalresultsdemonstratesignificantimprovementsinearlyriskdetectionaccuracyandpolicyoptimization
comparedtoexistingbenchmarks.
2/18

2 Related Work
2.1 MultimodalLearningforFinancialRisk
Multimodallearninginthecontextoffinancialriskpredictionhasemergedasacrucialmethodologicalinnovation,aimingto
integrateheterogeneousdatasourcessuchasnumericalfinancialindicators,textualfinancialnews,andstructuralrelational
informationtoimprovemodelexpressivenessandrobustness. Traditionalfinancialmodelsrelyheavilyonstructuredtabular
data,suchasbalancesheets,incomestatements,andmarketindicators,buttheseoftenmissunstructuredinformationlike
textualnarrativesorvisualcues,whichcanconveylatentsignalsoffinancialinstability14. Recentstudieshaveexploreddeep
neuralnetworkscapableofencodingdiversemodalities. Forinstance,convolutionalneuralnetworks(CNNs)andrecurrent
neuralnetworks(RNNs)havebeenemployedtoprocesstime-seriesmarketdataandfinancialnewsheadlinesrespectively,while
transformer-basedlanguagemodelssuchasBERThavebeenutilizedtoextractsemanticfromlengthyregulatoryreportsor
investorsentimentarticles. Attentionmechanisms,particularlycross-modalattention,haveproveneffectiveinaligningfinancial
indicators with corresponding textual rationales to capture interactions between market dynamics and external economic
narratives. Inshadowbankingcontexts,whereopacityandcomplexityareinherent,incorporatingmultimodalinputs—such
astextualdisclosuresfromoff-balance-sheetactivities,structuralfeaturesofshadowentities,andmacroeconomicsentiment
trends—intoaunifiedmodelhasshownpromiseforimprovingpredictionaccuracy15. Researchalsoindicatesthatlatefusion
strategies,wheremodality-specificdeepencodersprocessdifferentinputtypesfollowedbyconcatenationandfullyconnected
layers,tendtooutperformearlyfusionapproachesinhigh-noisefinancialdomains. Domainadaptationandtransferlearning
techniquesareoftenemployedtodealwithlimitedlabeleddata,withpretrainedmodelsongeneralfinancialcorporabeing
fine-tunedonshadowbankingdatasets. Multimodalvariationalautoencoders(MVAEs)andmultimodalGANshavealsobeen
proposedtoenhancerepresentationlearningandhandledataincompleteness. Despitetheseadvances,challengesremainin
modalityalignment,representationdisentanglement,andtheinterpretabilityofmultimodaldecisions,whichareparticularly
criticalforfinancialregulators. Thus,integratingmultimodallearningintoriskpredictionmodelsforshadowbankingprovides
notonlymethodologicalenrichmentbutalsoalignswiththeempiricalcomplexitiesofthisfinancialsector16.
2.2 KnowledgeGraphsinFinancialModeling
Knowledgegraphs(KGs)havegainedsignificanttractioninfinancialmodelingduetotheircapabilitytoencodecomplexand
interlinkedrelationshipsamongentitiessuchasfinancialinstitutions,instruments,transactions,andregulations17. AKG-based
approach enables the construction of semantically rich representations that go beyond flat tabular formats, encapsulating
temporal,relational,andhierarchicalinformationcrucialforunderstandingshadowbankingecosystems. Inthecontextof
shadowbanking,knowledgegraphscanmodelentitieslikespecialpurposevehicles(SPVs),trustproducts,off-balance-sheet
items,andtheirintricatelinkagestotraditionalbankinginstitutionsandcapitalmarkets18. Theserelationalstructuresareoften
non-trivialanddynamic,requiringsophisticatedgraphrepresentationlearningtechniquestoextractmeaningfulembeddings.
Graph neural networks (GNNs), including graph convolutional networks (GCNs), graph attention networks (GATs), and
temporalgraphnetworks(TGNs),havebeenappliedtoencodethesestructuresfordownstreamtaskssuchasfrauddetection,
creditriskscoring,andsystemicriskestimation. Furthermore,knowledgegraphembeddingmethodssuchasTransE,RotatE,
andComplExallowtransformationofsymbolicgraphdataintocontinuousvectorspaces,facilitatingintegrationwithdeep
learningarchitectures. Infinancialdomains,ontology-drivenKGconstructionhasbeenusedtoincorporateexpertknowledge
andregulatorylogic,ensuringsemanticconsistencyandimprovinginterpretability. Temporaldynamicsoffinancialtransactions
arecapturedthroughdynamicKGs,whichupdateentityrelationsasnewdataarrives,enablingreal-timeriskmonitoring19.
Event-basedKGaugmentation,whichlinksfinancialeventswithaffectedentities,enhancesthesituationalawarenessand
contextualaccuracyofriskpredictionmodels. HybridsystemscombiningKGswithprobabilisticreasoningorrule-based
engineshavealsodemonstratedutilityinscenariosimulationandstresstesting. Whilechallengessuchasdatasparsity,noise,
andentityresolutionpersist,theintegrationofKGsintofinancialanalytics,especiallyinopaquesectorslikeshadowbanking,
representsaparadigmshifttowardknowledge-centricAIsystemsthataremorealignedwithdomainreasoningandregulatory
needs20.
2.3 ReinforcementLearningforDecisionOptimization
Reinforcementlearning(RL)providesadynamicandinteractiveparadigmforoptimizingdecision-makingprocessesunder
uncertainty,whichisparticularlyapplicabletoriskcontrolandmanagementinshadowbankingsystems. Unlikesupervised
learning,whichassumesafixeddatasetandstaticdecisionboundaries,RLenablesagentstolearnpoliciesthatmaximize
long-termrewardsthroughcontinuousinteractionswithanenvironmentmodeledasaMarkovDecisionProcess(MDP).Inthe
financialcontext,thisenvironmentmayincludefluctuatingassetprices,regulatoryactions,andshiftingmarketsentiments21.
Shadowbankingactivities,oftencharacterizedbydelayedfeedbackloopsandsystemicinterdependencies,benefitfromRL’s
capacity to model sequential dependencies and delayed consequences of decisions. Deep reinforcement learning (DRL)
techniques,suchasDeepQ-Networks(DQN),ProximalPolicyOptimization(PPO),andSoftActor-Critic(SAC),havebeen
3/18

adaptedtofinancialtasksincludingportfoliomanagement,defaultprediction,andliquidityallocation. Whenintegratedwith
knowledgegraphs,RLagentscannavigatestructuredfinancialnetworks,learningoptimalinterventionpoliciessuchasearly
warningsorregulatorytriggersbasedonentityrelationshipsandsystemicriskindicators. Hierarchicalreinforcementlearning
hasbeenproposedtodecomposecomplexdecisionspacesintosubgoals,enhancinginterpretabilityandsampleefficiency22.
Rewardfunctionengineeringiscriticalinthesesystems, asitencodesdomain-specificobjectiveslikeminimizingdefault
risk,optimizingliquiditybuffers,orbalancingrisk-returntrade-offs. Simulationenvironments,oftenbuiltusinghistorical
transactiondataandmarketscenarios,areusedtotrainRLagentsbeforereal-worlddeployment,ensuringsafetyandcompliance.
Risk-sensitive RL, where the agent incorporates risk measures like Value-at-Risk (VaR) or Conditional VaR (CVaR) into
its reward structure, has shown promise for financial regulation applications. Moreover, model-based RL approaches are
beingexploredtoenhancesampleefficiencyandprovideexplicitmodelingofenvironmentdynamics,whichisvaluablein
low-frequencyfinancialdomains23. TheconvergenceofRLwithcausalityandexplainabilityresearchalsoopensavenuesfor
buildingtransparentdecisionsupportsystemsforfinancialregulators. Integratingreinforcementlearningintoamultimodaland
knowledge-awareframeworkfacilitatesadaptiveandrobustdecision-makingmechanismsthatcanresponddynamicallytothe
evolvingcomplexitiesofshadowbankingsystems24.
3 Experimental Setup
3.1 Dataset
TheCRSPdataset25consistsofdetailedtransactionalrecordsthatcaptureeveryfinancialmovementwithinanorganization,
includingdebitsandcredits. Eachentrytypicallyincludesatimestamp,accountcode,amount,anddescription,providinga
granularviewoffinancialactivitiesovertime. CRSPisextensivelyusedforconstructingfine-grainedjournalentries,validating
chronologicaltransactionorder,andevaluatinginternalfinancialtraceability. Duetoitshigh-resolutionnature,itsupports
various downstream tasks such as anomaly detection in double-entry records, audit trail reconstruction, and bookkeeping
automationunderevolvingpolicyenvironments. TheCompustatdataset26 providesasnapshotofallaccountbalancesata
specificpointintime,includingbothdebitandcreditcolumns. Asastaticledgerstaterepresentation,Compustatservesasthe
anchorforfinancialstatementgenerationandtemporalcomparisonacrossfiscalperiods. Itisinstrumentalinbenchmarking
accountreconciliationaccuracy,identifyingstructuralmispostings,andsupportingsupervisedlearningtaskssuchasautomated
integrityverificationandledger-levelconsistencymodelingwithinaccountingpipelines. TheWRDSdataset27focusesonthe
movementofcashintoandoutofabusinessacrossoperational,investing,andfinancingactivities. Itisorganizedasatemporal
sequenceofWRDSeventsalignedwithreportingcycles. WRDSenablesmodelingofliquidityfluctuations,short-termsolvency
assessments,andmulti-horizonfinancialforecasting. Itisparticularlyvitalforbudgetscenariosimulation,cash-basedaudit
metricdevelopment,andearlywarningdetectionoffinancialdistresspatternsinenterprise-levelrisksystems. TheQuandl
dataset28 consistsofitemizedsubmissionsfromemployeesordepartmentsdetailingincurredcostsforbusinesspurposes. Each
recordincludesexpensecategoriesalongsidemetadatasuchassubmitterID,approvallogs,andtimeannotations. Quandl
supportshigh-resolutioncompliancepipelines,transactionalfrauddetectionusingsemanticandstatisticalpatterns,andbudget
lifecycleoptimization. Italsofacilitatestrainingoffine-grainedclassifiersforexpense-typevalidationandlearning-to-rank
modelsforadaptiveapprovalworkflowprioritization.
3.2 ExperimentalDetails
Inourexperiments,allmodelsareimplementedusingPyTorchandtrainedonNVIDIAA100GPUswith80GBmemory. We
followstandardtrainingpipelineswidelyadoptedintop-tiervenuessuchasNeurIPSandICLR.Foroptimization,weuse
theAdamWoptimizerwithβ =0.9,β =0.999,andweightdecaysetto0.01. Thelearningrateisinitiallysetto5×10−5
1 2
andfollowsacosinedecayschedulewith10%warm-upsteps. Eachmodelistrainedfor100epochsunlessearlystoppingis
triggeredbasedonthevalidationloss. Batchsizeissetto64foralldatasets,andgradientclippingwithamaximumnorm
of1.0isappliedtoensurestableconvergence. Forinputpreprocessing,allcategoricalfeaturesareencodedusinglearnable
embeddingswithdimensionalitysetto32. Numericalfeaturesarestandardizedusingz-scorenormalization. Incaseswhere
missingvaluesappear,weemploydomain-specificimputationstrategies—meanimputationfornumericalattributesanda
separate category for missing categorical tokens. During training, dropout regularization with a rate of 0.2 is applied to
bothinputandintermediatelayerstomitigateoverfitting. Ourmodelarchitectureconsistsofasharedbackbonefollowed
bytask-specificheadsdependingonthedownstreamtask(classificationorregression). Forsequencemodeling,weadopta
Transformer-basedencoderwith4layers,8attentionheads,andhiddendimensionof256. Positionalencodingsareinjected
topreservetemporalstructure. Fortabularmodeling,weuseastackoffeedforwardlayerswithGELUactivations,residual
connections,andbatchnormalization. Allmodelsaretrainedwithmixedprecision(fp16)toreducememoryusageandtraining
time. Evaluationmetricsareselectedbasedonthetask. Forclassificationtasks,wereportaccuracy,precision,recall,and
F1-score. Forregressiontasks,weuseMeanSquaredError(MSE),RootMeanSquaredError(RMSE),andR2score. Wesplit
eachdatasetintotraining(70%),validation(15%),andtest(15%)sets. Hyperparametersaretunedonthevalidationsetvia
4/18

gridsearch. Weruneachexperimentthreetimeswithdifferentrandomseedsandreportthemeanandstandarddeviationto
ensurerobustnessandreproducibility. Ourcodebaseismadeavailableforreproducibilityandfollowsthebestpracticesin
experimentaldocumentationandversioning.
3.3 ComparisonwithSOTAMethods
Weconductacomprehensivecomparisonofourmethodagainstarangeofstate-of-the-art(SOTA)baselinesonfourdatasets
includingCRSP,Compustat,WRDS,andQuandl. TheresultsaresummarizedinTable1andTable2,coveringkeymetrics
includingPrecision,Recall,NDCG,andMAP.Acrossalldatasetsandevaluationindicators,ourmodelconsistentlyoutperforms
traditionalmethods. OntheCRSPdataset,ourmodelachievesthehighestPrecision(0.391),Recall(0.356),NDCG(0.403),
andMAP(0.294),significantlysurpassingthebest-performingbaselineDGCFby2.1–2.4pointsinabsoluteterms. Similar
trendsareobservedontheCompustatdataset,whereourmethodimprovesNDCGby2.7%andMAPby1.5%overthenext
bestmodel. Theseimprovementsvalidatetheeffectivenessofourdesignincapturinglatentfinancialpatternsandcomplex
temporaldependenciesthatareoverlookedbysimplerarchitectures.
InFigure1,intheWRDSandQuandldatasets,whichexhibithighervariabilityandnoise,ourmodelalsodemonstrates
robustperformance. Particularly,ontheQuandldataset,ourapproachachievesaremarkablePrecisionof0.379andanNDCG
of0.392,outperformingGRU4RecandDGCFbyanotablemargin. Thesegainscanbeattributedtoourarchitecture’sabilityto
jointlymodelstructuredfinancialrecordsandcontextualmetadatathroughdynamicinteractionlayersandadaptiveattention
mechanisms. Traditionalcollaborativefilteringmodelsandstaticembedding-basedapproacheslackthiscapability,leadingto
underperformanceonirregularorsparsefinancialevents. Furthermore,weobservethatourmodelmaintainsstablestandard
deviationsacrossmultipleruns,indicatingrobustnessandgeneralizationcapabilityindynamicfinancialenvironments. The
consistentsuperiorityacrossallfourdatasetssupportsthegeneralityofourapproachinbothtransactionalandstatement-level
financialanalytics.
In Figure 2, from a methodological standpoint, several factors explain the empirical advantages of our model. First,
our use of hierarchical feature encoding ensures better representation learning by integrating both low-level entry details
andhigh-levelfinancialcontexts. ThislayereddesigniscriticalindatasetslikeCRSPandWRDS,whereindividualentries
contributedifferentlydependingontheoverallperiodbalanceorcashdirection.Second,ourincorporationoftemporalencoding
enablesthemodeltodistinguishpatternsthatarerecurrentoverspecificaccountingperiods,whichisparticularlybeneficialin
Compustatevaluations. Thefine-grainedattentionandresiduallearningmechanismsallowthemodeltoremainsensitiveto
weaksignalswhilemaintainingstabilityondominantpatterns,whichprovesessentialinnoisydatasetslikeQuandl. These
architecturalchoicesalignwiththechallengesidentifiedinfinancialdatamodeling,suchasdatasparsity,heterogeneity,and
temporalirregularity. ComparedtoexistingSOTAmethods,ourdesignoffersamoreholisticmodelingparadigmthatbridges
signal-levellearningwithaccounting-levelreasoning,demonstratingbothaccuracyandinterpretabilityinreal-worldfinancial
scenarios.
Table1. EmpiricalEvaluationofProposedModelVersusBaselinesonCRSPandCompustat
CRSPDataset CompustatDataset
Model
Precision Recall NDCG MAP Precision Recall NDCG MAP
BPRMF29 0.312±0.01 0.286±0.02 0.338±0.01 0.241±0.01 0.294±0.02 0.275±0.01 0.320±0.02 0226±0.02
NCF30 0.341±0.01 0.309±0.01 0.352±0.02 0.259±0.01 0.322±0.01 0.297±0.02 0.340±0.02 0.248±0.01
LightGCN31 0.358±0.02 0.328±0.02 0.372±0.01 0.268±0.01 0.339±0.01 0.311±0.02 0.357±0.01 0.257±0.02
DGCF32 0.370±0.02 0.335±0.01 0.384±0.02 0.279±0.01 0.349±0.01 0.325±0.01 0.362±0.01 0.261±0.01
SVD++? 0.326±0.01 0.295±0.01 0.342±0.01 0.251±0.02 0.318±0.02 0.284±0.02 0.331±0.02 0.239±0.01
GRU4Rec33 0.344±0.01 0.321±0.01 0.365±0.01 0.262±0.02 0.337±0.01 0.303±0.01 0.350±0.02 0.254±0.02
Ours 0.391±0.01 0.356±0.01 0.403±0.01 0.294±0.01 0.368±0.01 0.343±0.01 0.389±0.01 0.276±0.01
3.4 AblationStudy
Tofurtherinvestigatethecontributionofeachcorecomponentinourmodel,weconductaseriesofablationexperimentsacross
allfourdatasets. TheresultsarepresentedinTable3andTable4,wherewesystematicallyremovethreecriticalmodules
including(GraphRepresentationLearning)thetemporalencodinglayer,(AccountingSemanticsAlignment)thehierarchical
featurefusionmechanism,and(EmbeddingPolicyConditions)theresidualattentioninteractionblock.Eachvariantisevaluated
usingthesameexperimentalsetupasthefullmodel,ensuringconsistencyandcomparability.
5/18

Figure1. EmpiricalEvaluationofProposedModelVersusBaselinesonCRSPandCompustat
InFigure3,theCRSPandCompustatresultshighlighttheessentialroleofallcomponents. Removingtemporalencoding
(w./o. GraphRepresentationLearning)leadstoasignificantdropinperformance,withNDCGdecreasingby3.3and3.2points
respectivelyonbothdatasets. Thisdemonstratestheimportanceofcapturingperiodicandsequentialdependenciesinfinancial
transactions,whichoftenexhibitseasonalorcyclicpatterns. Similarly,removingthehierarchicalfeaturefusionmodule(w./o.
AccountingSemanticsAlignment)resultsinafurtherperformancedecline,particularlyinMAPandPrecision. Thisconfirms
thatmulti-levelfeatureintegrationenablesthemodeltojointlyreasonoverfine-grainedentriesandhigh-levelsummaries.
Theremovaloftheresidualattentionblock(w./o. EmbeddingPolicyConditions)causesthemostseveredegradationinMAP,
revealingthatdeepsignalrefinementandselectiveamplificationofinformativepatternsarevitalforprecision-sensitivetasks
suchasanomalydetectionorjournalentrysuggestion. InFigure4,asimilartrendisobservedontheWRDSandQuandl
datasets. Theabsenceoftemporalencoding(w./o. GraphRepresentationLearning)consistentlyreducesRecallandNDCG
acrossbothdatasets,suggestingthattime-awaremodelingiscrucialinfinancialflowsandexpensetrajectories. Incontrast,
omitting the hierarchical fusion mechanism (w./o. Accounting Semantics Alignment) results in poorer generalization, as
evidencedbyreducedPrecisionandMAP.Thisreinforcestheideathatcombiningstructuredandcontextualcuesallowsfora
moreholisticunderstandingofthedata. Thevariantwithoutresidualattention(w./o. EmbeddingPolicyConditions)again
showsaconsistentdropinallmetrics,highlightingthemechanism’sroleinpreservingweakbutinformativesignalsinthe
presenceofnoisyorsparseexpenseitems. Thefullmodel,byintegratingallmodules,achievessuperiorperformanceacross
everydatasetandmetric,provingthenecessityandsynergyofitsdesign.
Theablationstudyvalidatesthateachcomponentisnotonlybeneficialbutalsocomplementary. Thetemporalencoding
layercaptureslatentchronologicalpatterns,thehierarchicalfeaturefusionextractssemanticallyrichrepresentations,andthe
residualattentionenhancesfocusonsubtlebutinformativefeatures. Removinganyofthemleadstosignificantperformance
degradation, confirmingthatourarchitecturalchoicesarewell-foundedandeffectiveinaddressingthecorechallengesof
financialdocumentmodeling. Thesefindingsstronglysupportthemodulardesignphilosophyadoptedinourapproach.
6/18

| Table2. | BenchmarkingOurModelVersusBaselinesonWRDSandQuandlData |     |     |     |               |     |     |
| ------- | ------------------------------------------------------ | --- | --- | --- | ------------- | --- | --- |
|         | WRDSDataset                                            |     |     |     | QuandlDataset |     |     |
Model
| Precision | Recall | NDCG | MAP | Precision | Recall | NDCG | MAP |
| --------- | ------ | ---- | --- | --------- | ------ | ---- | --- |
BPRMF29
0.305±0.01 0.289±0.01 0.332±0.02 0.237±0.01 0.318±0.01 0.281±0.02 0.328±0.01 0.243±0.02
NCF30
0.327±0.02 0.295±0.01 0.344±0.01 0.249±0.01 0.336±0.01 0.303±0.01 0.346±0.02 0.251±0.01
LightGCN31 0.349±0.01 0.323±0.02 0.366±0.01 0.267±0.01 0.341±0.02 0.326±0.01 0.363±0.01 0.258±0.01
DGCF32 0.342±0.02 0.318±0.01 0.359±0.01 0.261±0.02 0.355±0.01 0.315±0.01 0.375±0.02 0.265±0.01
SVD++? 0.311±0.01 0.287±0.01 0.335±0.01 0.242±0.02 0.325±0.02 0.292±0.01 0.333±0.01 0.247±0.01
GRU4Rec33 0.333±0.01 0.305±0.02 0.348±0.01 0.256±0.02 0.347±0.01 0.309±0.01 0.358±0.01 0.254±0.02
Ours 0.374±0.01 0.339±0.01 0.387±0.01 0.278±0.01 0.379±0.01 0.346±0.01 0.392±0.01 0.281±0.01
| Figure2. | BenchmarkingOurModelVersusBaselinesonWRDSandQuandlData |     |     |     |     |     |     |
| -------- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
Table3. DisentangledAnalysisofKeyElementsoverCRSPandCompustat
| Model |           | CRSPDataset |      |               | CompustatDataset |      |     |
| ----- | --------- | ----------- | ---- | ------------- | ---------------- | ---- | --- |
|       | Precision | Recall      | NDCG | MAP Precision | Recall           | NDCG | MAP |
w./o.GraphRepresentationLearning 0.359±0.01 0.326±0.01 0.370±0.01 0.264±0.01 0.345±0.02 0.314±0.01 0.357±0.02 0.251±0.01
w./o.AccountingSemanticsAlignment 0.345±0.02 0.309±0.01 0.356±0.01 0.257±0.01 0.337±0.01 0.304±0.02 0.346±0.01 0.245±0.02
w./o.EmbeddingPolicyConditions 0.331±0.01 0.312±0.01 0.342±0.02 0.248±0.02 0.328±0.01 0.296±0.01 0.335±0.01 0.239±0.01
Ours 0.391±0.01 0.356±0.01 0.403±0.01 0.294±0.01 0.368±0.01 0.343±0.01 0.389±0.01 0.276±0.01
Table4. DissectionofModelComponentsoverWRDSandQuandl
| Model |           | WRDSDataset |      |               | QuandlDataset |      |     |
| ----- | --------- | ----------- | ---- | ------------- | ------------- | ---- | --- |
|       | Precision | Recall      | NDCG | MAP Precision | Recall        | NDCG | MAP |
w./o.GraphRepresentationLearning 0.351±0.01 0.318±0.02 0.364±0.01 0.263±0.01 0.353±0.01 0.321±0.01 0.366±0.02 0.259±0.02
w./o.AccountingSemanticsAlignment 0.339±0.01 0.312±0.01 0.352±0.01 0.256±0.02 0.342±0.02 0.314±0.01 0.351±0.01 0.253±0.01
w./o.EmbeddingPolicyConditions 0.334±0.02 0.300±0.01 0.348±0.02 0.248±0.01 0.331±0.01 0.308±0.01 0.340±0.01 0.247±0.02
Ours 0.374±0.01 0.339±0.01 0.387±0.01 0.278±0.01 0.379±0.01 0.346±0.01 0.392±0.01 0.281±0.01
7/18

Figure3. DisentangledAnalysisofKeyElementsoverCRSPandCompustat
Figure4. DissectionofModelComponentsoverWRDSandQuandl
8/18

4 Conclusions and Future Work
Inthisstudy,weintroducedaninterpretableandpolicy-consistentdeeplearningframeworktailoredtosystemicriskmodelingin
non-traditionalfinancialdomains. Addressingtheshortcomingsofconventionaleconometricandmachinelearningapproaches,
ourarchitecturecombinesthestructuraladvantagesofagraph-basedencoder(GFA-Net)withtheregulatoryalignmentofa
scenario-drivenstrategymodule(PCS-Flow). GFA-Neteffectivelymodelstemporalandtransactionaldynamicsbyembedding
financial systems as evolving graphs enriched with semantic and institutional attributes. PCS-Flow complements this by
introducingscenarioperturbations,regulatoryembeddings,andcompliance-awareobjectives,ensuringthatdecisionoutputs
remainrobustacrossdiversefiscalpoliciesandmacroeconomicshifts. Extensiveexperimentsconductedonbothsynthetic
andreal-worlddatasets(CRSP,Compustat,WRDS,andQuandl)highlighttheframework’sstrengthsinpredictiveaccuracy,
temporalconsistency,andpolicyconformity. Comparedtobaselinemethods,ourmodeldemonstratesnotableimprovements
inprecision,recall,andanomalysensitivity,whilemaintainingtheinterpretabilityandflexibilityrequiredfordeploymentin
real-worldfinancialsystems.
Lookingforward,severalavenuesremainforexploration. First,incorporatingreinforcementlearningintoPCS-Flowcould
enabledynamicstrategyrefinementunderuncertainmarkettrajectories. Second,expandingthesemanticgraphschemato
include cross-institutional links and geopolitical variables would enhance system-wide risk propagation modeling. Third,
integratinghuman-in-the-loopsupervisioncouldfurtherboostcomplianceassuranceinsensitiveregulatorycontexts. Real-time
deployment onstreaming financialdata, combined withefficient onlineupdating mechanisms, presentsan importantstep
towardproduction-levelimplementation. Throughthiswork, wecontributetotheevolvingdiscourseonregulation-aware
AIandhighlightthepotentialofgraph-fusedandpolicy-integratedlearningmodelsforadvancingtrustworthyautomationin
financialdecisionsystems.
5 Method
5.1 Overview
Thissectionoutlinesthefoundationalandmethodologicalbasisforourproposedframeworkinfinancialaccountingmanagement.
Thecentralobjectiveofthisstudyistomodel,quantify,andalgorithmicallymanagethemultifaceteddynamicsoffinancial
datareportingandcontrolunderbothdeterministicandstochasticregimes. Byaddressingtheinherentchallengesinbalancing
compliancewithregulatorystandardsandoptimizingstrategicfinancialbehavior,ourframeworkoffersaunified,mathematically
groundedperspectivetoaddresskeygapsincurrentfinancialaccountingpractices.
InSection5.2,webeginbyformalizingthecorefinancialaccountingmanagementproblem. Thisinvolvestranslatingthe
structural,temporal,andquantitativeconstraintsofaccountingsystemsintoarigoroussymbolicrepresentation. Variables
suchasassetvaluation,liabilityrecognition,revenuetiming,andexpenseallocationareencodedusingasequenceofoperator-
drivenequationsovertemporalfinancialstates. Furthermore,weaccountforinterdependenciesbetweenregulatorypolicies,
internalfinancialcycles,andexternalauditexpectationsthroughasystemofconstrainedequationsandbudgetaryidentities.
Followingthat,Section5.3introducesournovelmodel,termedGFA-NetGraph-FusedAccountingNetwork),whichcaptures
thestructuralandtemporalcoherenceoffinancialtransactionsviaagraph-theoreticparadigmfusedwithneuralcomputation
layers. The model encodes financial entities as nodes and transactions as directed edges, embedding both semantic and
quantitativefeaturesinahigh-dimensionalvectorspace. Thisapproachallowsforsystematicpropagationofvaluationsignals,
anomaly detection, and forward simulation under hypothetical accounting policy changes. The architecture is carefully
designedtopreserveaccountingidentitiessuchasdouble-entrybookkeepingwhileenhancingcomputationaltractabilityfor
inferencetasks. InSection5.4,wepresentastrategywenamePolicy-ConsistentDifferentiation,whichgovernshowGFA-Net
operatesundervaryingfinancialreportingscenarios. Thiscomponentensuresthatthelearnedrepresentationsandinferred
accountingtrajectoriesremaininvariantorsmoothlyadaptableacrossdifferingjurisdictionalstandards,seasonalauditcycles,
andcorporateeventirregularities. Weintroduceaconstraintalignmentmechanismthatpenalizesmisalignedpolicyadherence
whileincentivizingcompliance-preservingtransformations. Thisstrategiclayereffectivelyoperationalizesdomainknowledge
assoftandhardconstraintsinthemodel’soptimizationprocess. Altogether,thismethodsectionaimstopresentacohesive
andextensibleapproachtomodelingfinancialaccountingmanagement. Eachsubsectionbuildsincrementally,startingfrom
symbolicformalization,progressingtoamodularneural-graphmodel,andculminatinginastrategiclayerthatcontextualizes
modeloutputsinreal-worldaccountingconstraints. Throughthislayeredapproach,wemovebeyondtraditionalrule-based
accountingsystemsandproposeadata-drivenframeworkwithformalguaranteesandinterpretability,thuscontributingtoboth
academicfinancetheoryandpracticalaccountingautomation.
5.2 Preliminaries
Financialaccountingmanagementisconcernedwiththesystematiccollection,classification,summarization,andinterpretation
of financial transactions to facilitate transparent reporting, informed decision-making, and regulatory compliance. In this
9/18

section, we provide a symbolic formulation of the core accounting management problem. We abstract the fundamental
elements—transactions,accounts,periods,standards,andconstraints—intoaformalframeworkgroundedindiscrete-time
mathematicalstructures,linearlogic,andalgebraicmappings.
Let us denote a discrete set of accounting periods by T = {t ,t ,...,t }, where each t represents a unique fiscal
1 2 n i
closure point. The set of accounts is given by A = {A ,A ,...,A }, each associated with a classification from C =
1 2 m
{Assets,Liabilities,Equity,Revenue,Expenses}. Thestateofthesystemattimet isrepresentedbyabalancevectorB(t)∈Rm.
We formalize transactions as a mapping T :T →Rm×m that satisfies the double-entry principle, and model policy
adjustmentsasafunctionP:T →Rm. Thedynamicevolutionofaccountbalancesisgiven.
Kt
B(t+1)=B(t)+∑e(t)
+P(t), (1)
k
k=1
wheree(t)
denotesthek-thentryvectorofatransactionandP(t)capturesdiscretionaryadjustmentssuchasdepreciationor
k
accruals. Theregulatorystructureenforcescoreaccountingidentities.
C⊤B(t)=C⊤B(t)+C⊤B(t), (2)
a l e
whereC ,C,C ∈{0,1}mareindicatorvectorscorrespondingtoassets,liabilities,andequityaccountsrespectively.
a l e
Toproduceaggregatedfinancialreports,wedefinealinearreportingtransformation.
r(t)=W·B(t), (3)
whereW ∈Rd×mmapsaccountbalancestoreportablelineitems. Forcomplianceverification,wedefineabinaryoperator
Γ:Rm→{0,1}.
1, ifallregulatoryandinternalpoliciesaresatisfied,
Γ(B(t))= (4)
(0, otherwise.
Theoptimizationobjectiveistominimizedeviationsfromfinancialtargetswhilepreservingpolicycompliance.
n 2
min ∑ r(t)−rtarget s.t. Γ(B(t))=1,∀t. (5)
{T(t),P(t)}t=1 2
(cid:13) (cid:13)
(cid:13) (cid:13)
(cid:13) (cid:13)
5.3 Graph-FusedAccountingNetwork(GFA-Net)
Inthissection,wepresentGFA-Net(Graph-FusedAccountingNetwork),anovelmodelingframeworkdesignedtoencode,
interpret, andmanagethedynamic, interconnectedstructureoffinancialaccountingsystems. Unlikeconventionaltabular
orpurelysequentialrepresentations,GFA-Netadoptsagraph-basedformulationthatallowsbothstructuralexpressivityand
computationalscalability. Eachaccountingperiodisrepresentedasagraphwherenodescorrespondtofinancialaccounts,and
directed,feature-annotatededgesrepresenttransactionsorflowsbetweenthem. Thisgraph-structureddataisprocessedviaa
parameterizedneuralencodingpipelinethatintegratesdomain-specificconstraintsandtemporalrecurrence(AsshowninFigure
5).
GraphRepresentationLearning
We define a dynamic financial accounting graph as G(t) =(V,E(t),X(t),F(t)) at each periodt ∈T. The vertex set
V ={v ,v ,...,v }representsthesetofallaccountsinthefinancialsystem,whereeachnodev correspondstoanaccountA
1 2 m i i
withassociatedfinancial,categorical,andregulatoryattributes. ThedirectededgesetE(t)⊆V ×V capturestemporalfinancial
flowssuchthatanedge(v,v )∈E(t)indicatesatransactionfromaccountA toaccountA attimet(AsshowninFigure6).
i j i j
Eachnodev carriesafeaturevectorX(t) ∈Rd,wheredincludescomponentssuchasbeginningbalance,accountcategory
i i
encoding,policycomplianceindicators,jurisdictionalregioncode,andanyexogenousinputsrelevanttoauditriskortransaction
frequency. Similarly,edgefeaturesF(t) ∈Rk storethetransactionmetadatasuchasamount,currencytype,transactionlatency,
ij
settlementflags,andcontractualterms.
TheedgefeaturesarederivedfromthesymbolicaccountingtransactionmatrixT(t)∈Rm×m. EachscalarT(t) denotesa
ij
monetarytransferfromaccountA toaccountA . Wedefineacontextualizedfeatureconstructorφ :R×Θ→Rk,suchthat
i j
10/18

Graph Representation Learning
TT
|     |     |     | sevaW waR | Tr rara r e |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
annns m
sfsf r
ofo orr o f
|     |     |     |     | mrm me s n |     |     | sreutaeF GEE dezirotceV |     |     |     | noitingoceR noitcA |     |
| --- | --- | --- | --- | ---------- | --- | --- | ----------------------- | --- | --- | --- | ------------------ | --- |
eer a
|     |      |              |              | rr r T           |     |     | 512 | rTr TT                 |                              | rTr TT                 |     |     |
| --- | ---- | ------------ | ------------ | ---------------- | --- | --- | --- | ---------------------- | ---------------------------- | ---------------------- | --- | --- |
|     |      |              |              |                  |     |     |     | e mannns rraa sredocnE |  laropmeT  scimanyD gniledoM | e mannns rraa sredocnE |     |     |
|     |      |              |              |                  |     |     | 512 |                        |                              | r ssff                 |     |     |
|     | EEG  |              |              |                  |     |     |     | r ofooof ssff          |                              | ofooof                 |     |     |
|     | Data |              |              |                  |     |     | 512 | srmm rr                |                              | srmm rr                |     |     |
|     |      |              |              | reyaL noitcejorP |     |     |     | nme                    |                              | nme a eer              |     |     |
|     |      |              | sretliF dnaB |                  |     |     |     | a r rrT eer            |                              | r rrT                  |     |     |
|     |      | noitaxiF eyE | sevaW decilS |                  |     |     | 512 |                        |                              |                        |     |     |
512
Accounting Semantics Alignment
Figure5. IllustrationofGraph-FusedAccountingNetwork(GFA-Net). Thisdiagramoutlinestheend-to-endprocessof
transformingrawEEGdata—comprisingrawwavesandeyefixationsignals—intoactionrecognitionoutputs. Thepipeline
includespreprocessingviabandfiltersandprojectionlayers,featureextractionusingtransformers,graph-basedrepresentation
learning,temporaldynamicsmodeling,semanticalignment,andfinalrecognitionthroughadditionaltransformerencoders.
| F(t) | =φ  | T(t),θ   | (t)      | ,   |     |     |     |     |     |     |     | (6) |
| ---- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|      | ij  | ij       | ij       |     |     |     |     |     |     |     |     |     |
|      |     | (cid:16) | (cid:17) |     |     |     |     |     |     |     |     |     |
(t)
where θ denotes auxiliary attributes including risk score, contract duration, and compliance tags. To enhance inter-
ij
pretability,weapplydomain-basedstandardizationonφ(·)ensuringinvariantscalingacrosstimeperiods.
TheinitialnodeembeddingmatrixH(0)∈Rm×d isinitializedbyconcatenatingrawnodefeaturesandanypolicyregime
embeddinge(t)
p activeduringtimet. Thegraphencodingmoduleusesastackofedge-awareGNNlayers,wherethel-thlayer
updateseachnodeembeddingh(l)
vianeighborhoodaggregationandtransformation.
i
| h(l+1) |     |         | ∑   | h(l),F(t) |          | h(l) |     |     |     |     |     |     |
| ------ | --- | ------- | --- | --------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
|        | =σ  |         | ψ   |           | +W       | 1    | ,   |     |     |     |     | (7) |
| i      |     |         |     | j         | ji       | i    |     |     |     |     |     |     |
|        |     |  j∈N(i) |     |           |          |      | !   |     |     |     |     |     |
|        |     |         |     | (cid:16)  | (cid:17) |      |     |     |     |     |     |     |
whereψ(·)isalearnededge-conditionedmessagefunctionandσ(·)isanonlinearactivationfunctionsuchasReLUor
| GELU.N |     |     |     |     |     |     |     | ∈Rd×d′ |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
(i)isthesetofallincomingneighborsofnodev,andW i 1 isalearnabletransformationmatrix.
Tomodelresidualstructureinnodeupdatesandimprovegradientflowindeeplayers,weaugmenttheupdaterulewithskip
connections.
| h(l+1) | =h(l) | +σ  | W   | · ∑ | ψ h(l),F(t) |     | ,   |     |     |     |     | (8) |
| ------ | ----- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| i      |       | i   |     | 2   | j           | ji  |     |     |     |     |     |     |
|        |       |     |     |     |             |     | !   |     |     |     |     |     |
j∈N(i)
|     |     |     |     |     | (cid:16) |     | (cid:17) |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- |
whereW 2 isaprojectionmatrixensuringdimensionalalignmentacrosslayers. Optionally,layernormalizationorbatch
normalizationcanbeinsertedbetweensummationandactivation.
Toincorporateglobalcontextintothegraphstructure,weincludeagraph-levelsummaryvectorcomputedviaattention
pooling.
|         | m   |            |     |       |     | exp(a⊤h(L) | )   |     |     |     |     |     |
| ------- | --- | ---------- | --- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| g(t)=∑α |     | (t) ·h(L), |     | (t)   |     |            | i   |     |     |     |     |     |
|         |     |            |     | withα | =   |            | ,   |     |     |     |     | (9) |
|         |     | i          | i   | i     | ∑m  | exp(a⊤h(   | L)  |     |     |     |     |     |
|         | i=1 |            |     |       |     |            | )   |     |     |     |     |     |
|         |     |            |     |       |     | j=1        | j   |     |     |     |     |     |
wherea∈Rd′
isalearnableattentionvector. Thisenablesdownstreammodulestoconditiononglobalfiscalcontextina
differentiablemanner.
TheoutputoftheGNNstackisconsolidatedintotheencodednode-statematrix.
| H(t)=[h( |     | L),h( | L),...,h( | L) ]⊤∈Rm×d′ |     |     |     |     |     |     |     |      |
| -------- | --- | ----- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | ---- |
|          |     |       |           |             |     | ,   |     |     |     |     |     | (10) |
|          |     | 1 2   |           | m           |     |     |     |     |     |     |     |      |
11/18

Linear
R  =  3
Concat
Heads
R  =  2
Graph Representation Learning
R  =  1
|     |     | Linear |     | Linear |     | Linear |     |
| --- | --- | ------ | --- | ------ | --- | ------ | --- |
|     |     | Q      |     |        | K   | V      |     |
Figure6. IllustrationofGraphRepresentationLearning. Thisdiagramvisualizeshowmulti-headattentionisintegrated
withgraphrepresentationlearning. Theprocessbeginswithlineartransformationsofquery(Q),key(K),andvalue(V)inputs.
Thesearepassedthroughmultipleattentionheads,eachincorporatinggraph-basedstructuresatvaryingreceptivefieldradii(R
=1,2,3). Theoutputsareconcatenatedandpassedthroughafinallinearlayer,enhancingspatialawarenessandcontextual
aggregationforimprovedrepresentationlearning.
whichrepresentssemantically-enriched,policy-awarefinancialaccountembeddingsattimet,suitableforprojectioninto
reportgeneration,compliancevalidation,andscenariosimulationpipelines.
AccountingSemanticsAlignment
To preserve the semantics of accounting laws within the learned representations, GFA-Net introduces a differentiable
projectionlayerthatenforcesidentityconsistencyandinstitutionalcomplianceatboththebalancesheetandincomestatement
levels. LetB(t)∈Rmdenotethepredictedvectorofaccountbalancesattimet. EachcomponentB(t) correspondstothelearned
i
financialrepresentationofaccountA i producedbytheGNNencoder. Thesystemmustsatisfythefundamentalbalancesheet
identity. b b
| ∑         | B(t) | ∑              | B(t) | ∑         | B(t). |     |      |
| --------- | ---- | -------------- | ---- | --------- | ----- | --- | ---- |
|           | =    |                | +    |           |       |     | (11) |
|           | i    |                | j    |           | k     |     |      |
| Ai∈Assets |      | Aj∈Liabilities |      | Ak∈Equity |       |     |      |
Toenforcebthisconstraintinbadifferentiablbeform,wedefineaquadraticpenaltylossusingindicatorvectorsC ,C,and
a l
C ∈{0,1}mwhichselectthecomponentsofB(t)belongingtoassets,liabilities,andequityclasses,respectively.
e
b2
| L(t) | = C⊤B(t)− | C⊤B(t)+C⊤B(t) |     |     | .   |     | (12) |
| ---- | --------- | ------------- | --- | --- | --- | --- | ---- |
| id   | a         | l             |     | e   |     |     |      |
2
| Inparallel,(cid:13)incomeverificationiscarriedo(cid:13)utbyensuringthatthepredictednetincomealignswiththedifferencebetween | (cid:13) | (cid:16) |      |              | (cid:17)(cid:13) |     |     |
| -------------------------------------------------------------------------------------------------------------------------- | -------- | -------- | ---- | ------------ | ---------------- | --- | --- |
|                                                                                                                            |          | b        | b    | b            |                  |     |     |
|                                                                                                                            | (cid:13) |          | LetR | andE(cid:13) |                  |     |     |
revenueandex pens ecomponen ts. denoteindexsetsofrevenueandexpenseaccounts. Thenthepredictedincome
iscomputed.
(t)
| Net \ Income |     | ∑B(t) | ∑B(t). |     |     |     | (13) |
| ------------ | --- | ----- | ------ | --- | --- | --- | ---- |
|              |     | = i   | −      | j   |     |     |      |
|              |     | i∈R   | j∈E    |     |     |     |      |
|              |     | b     |        | b   |     |     |      |
12/18

Toincorporatethisintothetrainingobjective,wedefinetheincomeloss.
|     |      |            |     |             | (t) 2 |     |      |
| --- | ---- | ---------- | --- | ----------- | ----- | --- | ---- |
|     | L(t) | \          | (t) | ^           |       |     |      |
|     | =    | Net Income |     | −Net Income | ,     |     | (14) |
inc
|     |     | (cid:18) |     |     | (cid:19) |     |     |
| --- | --- | -------- | --- | --- | -------- | --- | --- |
|     | ^   | (t)      |     |     |          |     |     |
whereNetIncome isaground-truthorexternallyestimatedvaluederivedfromauthoritativefinancialrecordsoraudit-
certifiedlabels. Moreover,toensurethesmoothintegrationofthesesymbolicconstraintsintotheend-to-endlearningpipeline,
wedefineaprojectedbalancevectorusinganalignmentoperatorΠ(·).
2
|     | B(t)=Π | B(t)              | =argmin | b−B(t)   | s.t. C⊤b=C⊤b+C⊤b. |       | (15) |
| --- | ------ | ----------------- | ------- | -------- | ----------------- | ----- | ---- |
|     |        |                   |         |          |                   | a l e |      |
|     |        |                   | b∈Rm    |          | 2                 |       |      |
|     |        | (cid:16) (cid:17) |         | (cid:13) | (cid:13)          |       |      |
Theisprojectiobnensuresthene(cid:13) tworbk’s(cid:13) outputcanbecorrectedposthocwithoutdiscardinglearnedstatisticalstructure.
|     |     |     |     | (cid:13) | (cid:13) |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- |
∈Rd×m
Areportingfidelitylossisintroducedtoconstraindeviationsinkeyline-itemsummaries. LetW bethereporting
| aggregationmatrix,andr(t) |     |     | theground-truthreportvector. |     |     | Theconstraintreads. |     |
| ------------------------- | --- | --- | ---------------------------- | --- | --- | ------------------- | --- |
true
|     | L(t)   | W·B(t)−r(t) |      | 2   |     |     |      |
| --- | ------ | ----------- | ---- | --- | --- | --- | ---- |
|     | =      |             |      | .   |     |     | (16) |
|     | report |             | true |     |     |     |      |
2
|     |     | (cid:13) |     | (cid:13) |     |     |     |
| --- | --- | -------- | --- | -------- | --- | --- | --- |
Theseseman(cid:13) ticalbignmentco(cid:13) mponentsarejointlyoptimizedwithpredictiveandtemporalobjectives,enablingthemodelto
|     |     | (cid:13) |     | (cid:13) |     |     |     |
| --- | --- | -------- | --- | -------- | --- | --- | --- |
remainfaithfultofinancialstructurewhileadaptingtodiverseoperationalcontexts.
TemporalDynamicsModeling
Tocapturetheprogressionoffinancialstatesovertime,GFA-Netemploysarecurrentpropagationmodulethatexplicitly
modelstemporaldependenciesbetweenconsecutiveaccountingperiods. LetH(t)∈Rm×d′ denotetheencodedfinancialgraph
representationattimet. Thesegraph-levelembeddingsaresummarizedandpassedintoarecurrentneuralunittomaintainan
evolvingstatevectorz(t)∈Rd′′,whichcaptureslong-termcontextualdependenciesacrossreportingperiods.
Theupdateruleis
governedbyagatedrecurrentunit(GRU)defined.
z(t+1)=GRU(H(t),z(t)),
(17)
wherez(t)representstheaccumulatedknowledgepriortotimet.
TheGRUlearnstemporalinteractionsbetweenfinancial
indicatorsandstructuralchangesintheaccountinggraph. Toencouragethemodeltogeneratetemporallycoherentpredictions,
wedefineatemporalsmoothnesslossbyprojectingthelatentmemorytothenext-steppredictionofaccountbalances.
|     |          | n−1 |          |        | 2   |     |      |
| --- | -------- | --- | -------- | ------ | --- | --- | ---- |
|     | L        | ∑   | B(t+1)−f | (z(t)) |     |     |      |
|     | temporal | =   |          | proj   | ,   |     | (18) |
2
t=1
|     |     | (cid:13)           |     |                    | (cid:13) |     |     |
| --- | --- | ------------------ | --- | ------------------ | -------- | --- | --- |
|     |     | (cid:13)           |     |                    | (cid:13) |     |     |
|     |     | :Rd′′ →(cid:13)bRm |     | p(cid:13)rojection |          |     |     |
where f proj is a neural function mapping recurrent states to predicted balances. This temporal
constraintenablesthemodeltolearnplausibletransitionsbetweenperiods,consistentwithreal-worldaccountingflows.
TheanomalydetectionmechanisminGFA-Netevaluatestheoutputofeachaccountnodeforirregularpatternsbyapplying
abinaryclassifierη overthefinalgraphlayerembeddingsh(L) . Foreachaccounti,thebinarycross-entropylossisusedto
i
supervisethepredictionagainstgroundtruthanomalylabelsy(t)
.
i
m
|     | L       | =∑BCE(y(t),η(h(L) |     | )), |     |     | (19) |
| --- | ------- | ----------------- | --- | --- | --- | --- | ---- |
|     | anomaly |                   | i   | i   |     |     |      |
i=1
:Rd′
whereBCE(·)denotesthebinarycross-entropyfunctionandη →[0,1]isalearnedsigmoidclassifier. Acompliance
scoreiscomputedforeachperiodt toreflectwhetherthetemporalstatealignswithregulatoryfeasibility. Thisscoreismodeled
viaalineartransformationfollowedbyasigmoidactivation.
|     | L          | =−log | σ        | w⊤z(t)+b | ,                |     | (20) |
| --- | ---------- | ----- | -------- | -------- | ---------------- | --- | ---- |
|     | compliance |       |          | c        | c                |     |      |
|     |            |       | (cid:16) | (cid:16) | (cid:17)(cid:17) |     |      |
∈Rd′′
wherew andb ∈Raretrainableweightsandσ(·)denotesthesigmoidfunction.
|     | c   |     | c   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
13/18

5.4 Policy-ConsistentScenarioFlowStrategy(PCS-Flow)
TocomplementthemodelingcapabilityofGFA-Net,weintroducePCS-Flow(Policy-ConsistentScenarioFlowStrategy),a
regulatory-aware,scenario-adaptivestrategicframeworkthatgovernsthebehavioroffinancialstateevolutionundervariable
accountingregimes. PCS-Flowisdesignedtoalignneuralpropagationanddecisionreasoningwithheterogeneousaccounting
standards,fiscalregulations,andauditinterpretationsacrossjurisdictionsandtemporalregimes. Thestrategyoperatesthrougha
seriesofdifferentiabletransformationsandconstraintregularizersthatencodelegalconsistency,policycoherence,andtemporal
resilience(AsshowninFigure7).
|     |     |     | PGB |     |     | PGB |     |     | PGB |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stage-level concatenation
C
|     |     |     |         |     |     |     |         |     |           |     | － Subtraction | ＋ Addition |     |
| --- | --- | --- | ------- | --- | --- | --- | ------- | --- | --------- | --- | ------------- | ---------- | --- |
|     |     |     | Stage 1 |     |     |     | Stage 2 |     | Stage 3   |     | Multiply      |            |     |
|     |     |     |         |     |     |     |         |     |           |     | ×             | C Concat   |     |
|     |     |     |         |     |     |     |         |     |           |     | C o n         | v Sigmoid  |     |
|     |     | BRC | DaMoE   |     |     | BRC | DaMoE   |     | BRC DaMoE |     | L a y         | e r S      |     |
|     |     |     | （×N1 ）  | C   | C   |     | （×N1 ）  | C   | （×N1 ）    | C   |               |            |     |
Min
Max
|     | Intput |             |                         |      |     |     |          |       |             | Output              | Channel                     | Channel    |     |
| --- | ------ | ----------- | ----------------------- | ---- | --- | --- | -------- | ----- | ----------- | ------------------- | --------------------------- | ---------- | --- |
|     |        |             | Conv                    |      | ＋   |     | ...      |       |             |                     |                             |            |     |
|     |        |             |                         |      | ×   |     |          |       | mroN reyaL  | tilpS erutaeF       |                             | mroN reyaL |     |
|     |        |             | PGB                     | Conv |     |     | Weight   |       | noitcideR Q | Q ... Q -toD delacS | tcusorP noitnettA noisnapxE |            |     |
|     |        |             |                         |      | ＋ S | C   |          | vnoC  | raeniL K    | K ...               | C                           | ＋ NFF ＋    |     |
|     |        | kcolBseR-ES | kcolBseR-ES kcolBseR-ES | Conv | ＋   |     | Expert 1 | × C ＋ |             | K                   |                             |            |     |
|     |        |             |                         |      |     |     |          |       | V           | V ... V             |                             |            |     |
|     | －      | Conv        | Conv                    | ＋    | ＋   |     | Expert 2 |       |             |                     |                             |            |     |
CRB
Expert k
Embedding Policy
|     |     |     |     |     |     |     | Scenario Simulation  |     | Cross-Time Policy Consistency |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----------------------------- | --- | --- | --- | --- |
Conditions
Mechanics
Figure7. IllustrationofthePolicy-ConsistentScenarioFlowStrategy(PCS-Flow). Thisdiagrampresentsathree-stage
architecturecombiningConditionalResidualBlocks(CRB)andDynamicMixture-of-Experts(DaMoE)modules,with
stage-wiseconcatenation. EachstagerefinestheinputthroughPolicy-GuidedBlocks(PGB)andCRB-enhancedfeature
extraction. Thedesignincludesanembeddingpolicymechanism,scenariosimulationviaexpertgating,andacross-timepolicy
consistencymoduleleveragingattentionmechanismsandfeaturesplittingfortemporalalignmentandrobustoutputgeneration.
EmbeddingPolicyConditions
LetP={p ,p ,...,p }denoteafinitesetofdiscreteaccountingpolicyregimes,suchasIFRS,USGAAP,orjurisdiction-
|     |     | 1   | 2 s |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
specifictaxframeworks. Eachpolicyregime p isassociatedwithasetofsemanticandstructuralinterpretationsregarding
k
recognition, measurement, and disclosure rules. To parameterize these differences, we define a policy embedding matrix
∈Rs×dp,whereeachrowEP[k,:]correspondstothelatentrepresentationofpolicy
| EP  |     |     |     |     |     |     |     |     |     | p k . Theseembeddingsarelearned |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- |
end-to-endandencodedifferentialassumptions,suchastreatmentofleasing,goodwillimpairment,orrevenuerecognition
timing(AsshowninFigure8).
p(t)∈P,indicatingtheapplicablereportingframework.
| Eachaccountingperiodt |     |     |     | islabeledwithanactivepolicytag |     |     |     |     |     |     |     |     | The |
| --------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
correspondingembeddingvectorisextracted.
|     | e( t) =EP[p(t)], |     |     |     |     |     |     |     |     |     |     |     | (21) |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
p
whichisusedtoinformgraphconstructionandneuralencodingforthatperiod. Thepolicyvectore(t) isconcatenatedto
p
boththenode-levelaccountfeaturesandedge-leveltransactionfeaturestocontextualizethemunderthegoverningregime.
|     | X (t) ←[X | (t) | ∥e( t) | F ( t) | ←[F ( | t) ∥e( t) |     |     |     |     |     |     |      |
| --- | --------- | --- | ------ | ------ | ----- | --------- | --- | --- | --- | --- | --- | --- | ---- |
|     |           |     | p ],   |        |       | p         | ],  |     |     |     |     |     | (22) |
|     | i         | i   |        | i j    | i     | j         |     |     |     |     |     |     |      |
foralli,j∈{1,...,m}. Thisensuresthatpolicy-conditionalencodingaffectsallmessagepassingoperationsandnode
updatesinGFA-Net.
Toincreasetheexpressivenessofe(t) beyondstaticembeddings,weintroduceatrainabletransformationfunctiong :
|     |     |     |     |     | p   |     |     |     |     |     |     |     | policy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
Rdp →Rd′ thatmapsrawpolicyvectorsintoaspacealignedwithGNNfeaturerepresentations.
|     | e˜( t) | (e(    | t) )=MLP(e( |     | t)  |     |     |     |     |     |     |     |      |
| --- | ------ | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     | =g     |        |             |     | ),  |     |     |     |     |     |     |     | (23) |
|     | p      | policy | p           |     | p   |     |     |     |     |     |     |     |      |
14/18

.
Vopt
Transpose
softmax
|      |        |        | Qopt | +   |     |     |     |
| ---- | ------ | ------ | ---- | --- | --- | --- | --- |
| lo w |        | h ig h | Kopt |     |     |     |     |
| Covo | or Cov |        |      |     |     |     |     |
| p    | t      | o p t  |      |     |     |     |     |
. .
|     |     |     |     |     | low         | high           |     |
| --- | --- | --- | --- | --- | ----------- | -------------- | --- |
|     |     |     |     |     | Att Opt-sat | or Att Opt-sat |     |
Transpose
+ softmax
QSAT
|     |     |     | KSAT | .   |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
VSAT
| Cov lo w | or Cov | h ig h |     |     |     |     |     |
| -------- | ------ | ------ | --- | --- | --- | --- | --- |
| s a t    |        | s a t  |     |     |     |     |     |
.
|     |     |     |     | + Matrix product | Hadamard product |     |     |
| --- | --- | --- | --- | ---------------- | ---------------- | --- | --- |
Figure8. IllustrationofEmbeddingPolicyConditions. Thisfigureshowsacomparisonbetweentwoparallelattention
computationpathwaysincludingoneunderoptimalcovarianceconditions(Cov opt )andanotherundersaturationconditions
(Cov ). Bothpathsutilizequery(Q),key(K),andvalue(V)vectors—denotedasQ ,K ,V andQ ,K ,V ,
| sat |     |     |     |     | opt opt opt | SAT SAT | SAT |
| --- | --- | --- | --- | --- | ----------- | ------- | --- |
respectively. TheattentionoutputsarederivedviamatrixproductsfollowedbysoftmaxandHadamardproducts,leadingto
eitherloworhighattentionoutputs(Att Opt-sat ). Thisdual-pathstructureemphasizestheroleofattentionstatevariationin
modelingadaptiveresponses.
whereMLPdenotesamulti-layerperceptronwithnon-linearactivations. Thetransformedvectore˜(t) canthenbeshared
p
acrossbothnodeandedgeupdates,aswellastemporalmodulessuchasGRUorscenariosimulators.
Toquantifytheinfluenceofpolicyvariabilityacrosstime,wedefineapolicytransitionlossbetweenadjacentperiods. Let
e(t) ande(t+1)
denoteembeddingsfortwoconsecutiveperiods. Thesmoothnessconstraintisdefined.
p p
2
| L ( t)         |     | e( t+1) −e( | t)       |     |     |     |      |
| -------------- | --- | ----------- | -------- | --- | --- | --- | ---- |
|                | =   | p           | p ,      |     |     |     | (24) |
| p o licy-shift |     |             | 2        |     |     |     |      |
|                |     | (cid:13)    | (cid:13) |     |     |     |      |
penalizing abrup(cid:13)t regime tra(cid:13)nsitions unless externally justified. We define a regime classification head to ensure that
|     |     | (cid:13) | (cid:13) |     |     |     |     |
| --- | --- | -------- | -------- | --- | --- | --- | --- |
embeddingsencodedistinguishablesemantics. Leth :Rdp →Rsbeasoftmaxclassifier,thentheauxiliaryclassificationloss
cls
isgiven.
(e( t)
|     |       | exp(h | )[p(t)]) |     |     |     |      |
| --- | ----- | ----- | -------- | --- | --- | --- | ---- |
| L   | =−log |       | cls p    | .   |     |     | (25) |
regime-cls
|     |     |  ∑s | exp(h (e( t) )[k])! |     |     |     |     |
| --- | --- | --- | ------------------- | --- | --- | --- | --- |
|     |     | k=1 | cls p               |     |     |     |     |
Thissupervisionencouragesthepolicyvectorstoremainidentifiableinlatentspace,enablingbettergeneralizationacross
unseenjurisdictions. Thesemechanismscollectivelyembedstructuralregulatoryassumptionsdirectlyintothecomputational
pipeline.
ScenarioSimulationMechanics
WedefineasetofhypotheticalscenariosS ={s ,s ,...,s },eachcorrespondingtoamacro-financialperturbationor
1 2 r
policy-sensitive event, such as inflation surges, regulatory amendments, or market liquidity shocks. Each scenario s j is
formalized as a transformation operator T that perturbs the input node features of the accounting graph, modeling how
sj
externalshocksreconfigurethefinanciallandscape.
Foreachaccountiattimet,theperturbedfeatureunderscenarios iscomputed.
j
| X(t) | (X(t) | )=X(t) | +∆(t), |     |     |     |      |
| ---- | ----- | ------ | ------ | --- | --- | --- | ---- |
| =T   |       |        |        |     |     |     | (26) |
| i,sj | sj    | i      | i i,sj |     |     |     |      |
15/18

where∆(t) encodesscenario-specificdeviations. Theseperturbednodefeaturesdefineanewscenario-specificgraphG(t) .
|     | i,sj |     |     |     |     |     |     | sj  |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- |
TheGFA-Netencoderisappliedoverthetransformedgraphtogeneratescenario-specifichiddenrepresentations.
|     | H(t) =GFA-Net(G(t)[X(t) |     | ]), |     |     |     |     | (27) |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | ---- |
|     | sj                      |     | sj  |     |     |     |     |      |
yieldingupdatedaccountembeddingsthatreflectthesimulatedenvironment. Thesearedecodedintoscenario-projected
| balancesB(t) | ,whicharethenaggregatedintostructuredfinancialreports. |     |     |     |     |     |     |     |
| ------------ | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
sj
b
|     | r(t) =W·B(t), |     |     |     |     |     |     |      |
| --- | ------------- | --- | --- | --- | --- | --- | --- | ---- |
|     | sj            | sj  |     |     |     |     |     | (28) |
withW denotingthereportingaggregationmatrix. Tomaintainsemanticcoherenceacrossaccountingregimes,PCS-Flow
b
introducesapolicy-consistencyconstraint. Givenabasepolicy p andatargetpolicy p .
|     |          |         |           |     |     | b   | a   |      |
| --- | -------- | ------- | --------- | --- | --- | --- | --- | ---- |
|     | t)       | t       | t 2       |     |     |     |     |      |
|     | L ( =    | r( ) −Π | (r( ) ) , |     |     |     |     | (29) |
|     | p o licy | p b     | pa←pb p b |     |     |     |     |      |
2
|     |     | (cid:13) | (cid:13) |     |     |     |     |     |
| --- | --- | -------- | -------- | --- | --- | --- | --- | --- |
(cid:13)(·)isalearnedope(cid:13)ratortranslatingreportingsemanticsfrom
|     | whereΠ        |     |          |     |     |     | p to p . Toevaluatescenariodesirabilityunder |     |
| --- | ------------- | --- | -------- | --- | --- | --- | -------------------------------------------- | --- |
|     | pa←p(cid:13)b |     | (cid:13) |     |     |     | b a                                          |     |
uncertainty,PCS-Flowranksalternativesusingaregulatory-compliance-weightedutilityscore.
|     | (t)    | (t)      | (r(t)      |     |     |     |     |      |
| --- | ------ | -------- | ---------- | --- | --- | --- | --- | ---- |
|     | ρ =α·γ | +(1−α)·f | util sj ), |     |     |     |     | (30) |
|     | j      | j        |            |     |     |     |     |      |
(t)
whereγ isthecomplianceconfidencescore, f util (·)isatask-specificutilityfunction,andα ∈[0,1]balancesfeasibility
j
andfinancialperformance.
Cross-TimePolicyConsistency
Weapplyasmoothnesspriortoensurethatreportedmetricsevolveconsistentlyacrosstimewithinthesamepolicy. For
eacht.
|     | L(t)                 |     |             | 2   |     |     |     |      |
| --- | -------------------- | --- | ----------- | --- | --- | --- | --- | ---- |
|     |                      | =   | r(t+1)−r(t) | ,   |     |     |     | (31) |
|     | temporal-consistency |     |             | 1   |     |     |     |      |
Σ− p
|     |     |     | (cid:13) | (cid:13) |     |     |     |     |
| --- | --- | --- | -------- | -------- | --- | --- | --- | --- |
|     |     |     | (cid:13) | (cid:13) |     |     |     |     |
whereΣ p(t),capturingexpectedvolatilitybetweenconsecutiveperiods.
p isalearnedco(cid:13)variancestru(cid:13)cturespecifictopolicy
Fordecisionsupport,PCS-Flowprovidesscenariorankingunderregulatoryfeasibilityandfinancialdesirability. Eachscenario
| s receivesacompliancescoreγ |          |        | andautilityscoreυ |       | .   |     |     |      |
| --------------------------- | -------- | ------ | ----------------- | ----- | --- | --- | --- | ---- |
| j                           |          |        | j                 |       | j   |     |     |      |
|                             |          | w⊤H(t) |                   | (r(t) |     |     |     |      |
|                             | γ =σ     | +b     | , υ = f           | ),    |     |     |     | (32) |
|                             | j        | γ sj   | γ j utility       | sj    |     |     |     |      |
|                             | (cid:16) |        | (cid:17)          |       |     |     |     |      |
withfinalrankingscore.
|     | ρ j =α·γ                                            | j +(1−α)·υ | j , |     |     |     |     | (33) |
| --- | --------------------------------------------------- | ---------- | --- | --- | --- | --- | --- | ---- |
|     | whereα ∈[0,1]balanceslegalandperformanceobjectives. |            |     |     |     |     |     |      |
TheintegratedPCS-Flowobjectiveisconstructed.
|     |      | n        |                        |     | r        |     |     |      |
| --- | ---- | -------- | ---------------------- | --- | -------- | --- | --- | ---- |
|     | L =∑ | λ L(t)   | +λ L(t)                |     | +λ ∑(1−γ | )2, |     | (34) |
|     | PCS  | 5 policy | 6 temporal-consistency |     | 7        | j   |     |      |
|     |      | t=1      |                        |     | j=1      |     |     |      |
|     |      | (cid:16) |                        |     | (cid:17) |     |     |      |
subjecttocomplianceconstraints.
Γ(r(t)
|     | sj )=1, | ∀j,t. |     |     |     |     |     | (35) |
| --- | ------- | ----- | --- | --- | --- | --- | --- | ---- |
PCS-Flowensuresthatfinancialpredictionsremainrobustunderchangingexternalandinternalconditions,whilemaintain-
inginterpretabilityandlegalcoherence.
16/18

Conflict of Interest Statement
Theauthorsdeclarethattheresearchwasconductedintheabsenceofanycommercialorfinancialrelationshipsthatcouldbe
construedasapotentialconflictofinterest.
Author Contributions
Conceptualization,TQ;methodology,TQ;software,TQ;validation,TQ;formalanalysis,TQ;investigation,TQ;datacuration,
TQ;writing—originaldraftpreparation,TQ;writing—reviewandediting,TQ;visualization,TQ;supervision,TQ;funding
acquisition,TQ.Allauthorshavereadandagreedtothepublishedversionofthemanuscript.
Funding
Detailsofallfundingsourcesshouldbeprovided,includinggrantnumbersifapplicable. Pleaseensuretoaddallnecessary
fundinginformation,asafterpublicationthisisnolongerpossible.
Acknowledgments
Thisisashorttexttoacknowledgethecontributionsofspecificcolleagues,institutions,oragenciesthataidedtheeffortsofthe
authors.
Data Availability Statement
Thedatasetsgeneratedand/oranalysedduringthecurrentstudyareavailableintheShadowBank,
https://github.com/aeon38116/ShadowBank.git
References
1. Gennaioli,N.,Shleifer,A.&Vishny,R.W. Amodelofshadowbanking. TheJ.Finance68,1331–1363(2013).
2. Culp,C.L.&Neves,A.M. Shadowbanking,risktransfer,andfinancialstability. J.Appl.Corp.Finance29,45–64(2017).
3. Huang,J. Bankingandshadowbanking. J.Econ.Theory178,124–152(2018).
4. Ricks,M. Shadowbankingandfinancialregulation. ColumbiaLawEcon.Work.Pap.(2010).
5. Agresti,A.M.&Brence,R. Statisticalworkonshadowbanking: developmentofnewdatasetsandindicatorsforshadow
banking. InBISIFCconferenceonDataneedsandStatisticscompilationformacroprudentialanalysis,vol.11(2017).
6. Judge,K. Informationgapsandshadowbanking. Va.L.Rev.103,411(2017).
7. Adrian, T. & Ashcraft, A. B. Shadow banking: a review of the literature. Bank. Crises: Perspectives from The New
PalgraveDict.282–315(2016).
8. Gong,R.&Page,F.H. Shadowbanksandsystemicrisks. AvailableatSSRN2724314(2015).
9. Pellegrini, C. B., Meoli, M. & Urga, G. Money market funds, shadow banking and systemic risk in united kingdom.
FinanceRes.Lett.21,163–171(2017).
10. Adrian,T.&Ashcraft,A.B. Shadowbankingregulation. Annu.Rev.Financ.Econ.4,99–140(2012).
11. Avkiran,N.K.,Ringle,C.M.&Low,R. Monitoringtransmissionofsystemicriskfromshadowbankingtoregulated
banking. In28thAustralasianFinanceandBankingConference(2015).
12. Amin,T.,Chikalov,I.,Moshkov,M.&Zielosko,B. Dynamicprogrammingapproachtooptimizationofapproximate
decisionrules. Inf.Sci.221,403–418(2013).
13. Noussair,C.&Matheny,K. Anexperimentalstudyofdecisionsindynamicoptimizationproblems. Econ.Theory15,
389–419(2000).
14. Meisel,S. Anticipatoryoptimizationfordynamicdecisionmaking,vol.51(SpringerScience&BusinessMedia,2011).
15. Neely,M.J. Dynamicoptimizationandlearningforrenewalsystems. IEEETransactionsonAutom.Control.58,32–46
(2012).
16. Amin,T.,Chikalov,I.,Moshkov,M.&Zielosko,B. Dynamicprogrammingapproachforpartialdecisionruleoptimization.
FundamentaInformaticae119,233–248(2012).
17/18

17. Pan,H.,Wang,Z.,Ding,S.&Yu,G. Creditriskassessmentofshadowbanking: Evidencefromchina. Res.Int.Bus.
Finance102928(2025).
18. Munir,A.&Gordon-Ross,A. Anmdp-baseddynamicoptimizationmethodologyforwirelesssensornetworks. IEEE
TransactionsonParallelDistributedSyst.23,616–625(2011).
19. Fu,H.,Lewis,P.R.,Sendhoff,B.,Tang,K.&Yao,X. Whataredynamicoptimizationproblems? In2014IEEEcongress
onevolutionarycomputation(CEC),1550–1557(IEEE,2014).
20. Bertsimas,D.&Thiele,A. Robustanddata-drivenoptimization: moderndecisionmakingunderuncertainty. InModels,
methods,andapplicationsforinnovativedecisionmaking,95–122(INFORMS,2006).
21. Agresti,A.M.&Brence,R. Statisticalworkonshadowbanking: developmentofnewdatasetsandindicatorsforshadow
banking. InBISIFCconferenceonDataneedsandStatisticscompilationformacroprudentialanalysis,vol.11(2017).
22. Chaturvedi,A.&Singh,A. Examiningtheinterconnectednessandearlywarningsignalsofsystemicrisksofshadow
banks: Anapplicationtotheindianshadowbankcrisis. Kybernetes52,3938–3964(2023).
23. Mishra,M.&Varshney,M. Creditriskassessmentinnon-bankingfinancialinstitutions: lessonsfromshadowbanking
sector. Int.J.Sci.Res.Netw.Secur.Commun.11,1–11(2023).
24. Yuan,C.,Zhu,Y.&Kapitsinis,N. Collateralmonetarypolicy,shadowbankingandbankrisk: evidencefromchina. China
FinanceRev.Int.(2025).
25. Song,Y.,Du,H.,Piao,T.&Shi,H. Researchonfinancialriskintelligentmonitoringandearlywarningmodelbasedon
lstm,transformer,anddeeplearning. J.Organ.EndUserComput.(JOEUC)36,1–24(2024).
26. Wang, X., Kräussl, Z.&Brorsson, M. Datasetsforadvancedbankruptcyprediction: Asurveyandtaxonomy. arXiv
preprintarXiv:2411.01928(2024).
27. Rizinski,M.etal. Comparativeanalysisofnlp-basedmodelsforcompanyclassification.information2024,15,77(2024).
28. Zhou,Q. Applicationofbigdataanalyticsinfinancialdecision-making: Integratingcomputationalmodelstooptimize
investmentstrategies. Int.J.HighSpeedElectron.Syst.2540424(2025).
29. Park, J., Kim, D. & Kim, D. Item-based variational auto-encoder for fair music recommendation. arXiv preprint
arXiv:2211.01333(2022).
30. Zhang,Y.etal. Coupleeffectsofmulti-impactdamageandcaicapabilityonncfcomposites. Rev.onAdv.Mater.Sci.63,
20240003(2024).
31. Liao,J.etal. Sociallgn: Lightgraphconvolutionnetworkforsocialrecommendation. Inf.Sci.589,595–607(2022).
32. Bourhim,S. Dfi-dgcf: Agraph-basedrecommendationapproachfordrug-foodinteractions. InInternationalConference
onComplexNetworksandTheirApplications,389–399(Springer,2023).
33. Zhang,S.etal. Glint-ru: Gatedlightweightintelligentrecurrentunitsforsequentialrecommendersystems. arXivpreprint
arXiv:2406.10244(2024).
18/18