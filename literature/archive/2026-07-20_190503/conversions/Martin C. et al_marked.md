Adaptive IntelligenceandLifelongSystems
2025,Vol.1,pp.56–66
https://fupress.org/journal/AILS/index.php/journal
Adaptive Learning Architectures for Evolving Data
Streams: Challenges and Advances
ClaireÉlodieMartin1,HugoAlexandreLefèvre2*,CamilleRenéeDubois3
1Ph.D.Candidate,DepartmentofComputerScience,SorbonneUniversité,Paris,France
2Ph.D.Candidate,SchoolofElectricalandInformationEngineering,UniversitéGrenobleAlpes,Grenoble,France
3Ph.D.Candidate,FacultyofEngineeringandDigitalSciences,UniversitédeStrasbourg,Strasbourg,France
*CorrespondingAuthor:hugo.lefevre@univ-grenoble-alpes.fr
Citation:C.E.Martin,H.A.Lefèvre,andC.R.Dubois,“Adaptivelearningarchitecturesforevolvingdatastreams:Challenges
andadvances,”AILS,vol.1,no.2,pp.56–66,2023.
ARTICLEINFO ABSTRACT
Received:10Feb2023 Inthe era of ubiquitous data generation, learning systems must continuously adapt to dynamicand
non-stationary environments. This paper surveys recent advances in adaptive learning architectures
Accepted:27Apr2023
designed for evolving data streams, with a focus on incremental learning, concept drift adaptation,
and real-time model updating. We analyze the core challenges in building robust, scalable systems
capable of retaining long-term knowledge while remaining flexible to new information. Key
architectural designs, such as modular networks, meta-learning frameworks, and memory-
constrained learners, are discussed. Real-world applications in IoT, autonomous systems, and
personalized services are examined to highlight practical implications. This work aims to provide a
comprehensive understanding of the current landscape and identify open research directions in the
fieldoflifelongandadaptivelearning.
Keywords: Adaptive Learning Systems, Evolving Data Streams, Lifelong Learning, Knowledge
Retention,Meta-Learning,OnlineLearningArchitectures.
INTRODUCTION
In an era where data is generated continuously and ubiquitously, traditional static machine learning models
face significant limitations when deployed in real-world scenarios involving non-stationary and evolving data
distributions. Applications such as autonomous vehicles, real-time user modeling, industrial IoT, and intelligent
robotics demand learning systems that can adapt online, incrementally update models, and retain critical
knowledge over time. This paradigm, often referred to as lifelong learning or continual learning, has gained
increasingattentionacrossboththeoreticalandappliedmachinelearningcommunities[1],[2].
One of the core challenges in lifelong learning is handling concept drift, where the underlying data
distribution changes over time, rendering previously learned knowledge partially or completely obsolete [3].
Adaptive learning architectures aim to address this by incorporating mechanisms such as dynamic model
reconfiguration,selectivememoryretention,andmeta-learningstrategiesthatallowthemodeltogeneralizefrom
past experiences while adapting to new information [4], [5]. Moreover, the need for resource-efficient and real-
time learning has pushed the development of lightweight, modular, and streaming-capable models capable of
functioningunderlimitedcomputationalandmemorybudgets[6].
Despite significant progress, key issues remain unsolved—catastrophic forgetting, efficient drift detection,
balancingplasticityandstability,anddeployingrobustsystemsinopen-worldenvironmentsareongoingresearch
frontiers [7], [8]. This paper provides a comprehensive survey of recent advances in adaptive learning systems
tailoredforevolvingdatastreams,focusingonarchitecturalstrategies,learningframeworks,andopenchallenges.
Weaimtobridgetheoreticalinsightswithpracticalimplementations andidentifypromisingdirections forfuture
Copyright©2025.Thisisanopenaccessjournal,whichmeansthatallcontentisfreelyavailablewithoutchargetotheuserorhis/herinstitution.Articles
publishedinAIDPMIDarelicensedundertheCreativeCommonsAttribution-NonCommercial-4.0UnportedLicense.

2/11 MartinC.E.etal./AILS,Vol.1,56-66
explorationinthisrapidlygrowingfield.
RELATEDWORKS
Adaptive learning in dynamic and evolving environments has been explored through various paradigms,
including incremental learning, online learning, and continual learning. Early approaches focused on updating
models incrementally with new data, assuming a stationary data distribution. However, real-world data often
exhibitsconceptdrift,necessitatingmoresophisticatedadaptationstrategies[9],[10].
A common line of research addresses the catastrophic forgetting problem— where learning new tasks
interferes destructively with previously acquired knowledge. Regularization-based approaches such as Elastic
Weight Consolidation (EWC) [11] and Synaptic Intelligence (SI) [12] preserve important weights to avoid
forgetting. Other strategies, like experience replay and memory rehearsal, mitigate forgetting by retraining on a
bufferofpastexamples[13],[14].
Another category of methods uses dynamic architectures to accommodate new tasks. Progressive Neural
Networks [15] grow the network by adding task-specific submodules, while PackNet [16] prunes and reuses
networkcapacityformultiple tasks.Thesearchitecturesmaintaintaskperformancebutoften incurhighmemory
orcomputationalcosts(Figure1).
Figure1.Online-dynamic-clustering-basedSoftSensorforIndustrialSemi-supervisedDataStreams
In the streaming learning setting, frameworks suchasLearn++ and ARF (AdaptiveRandom Forest)provide
ensemble-based solutions that continuously integrate new classifiers while handling drift and maintaining
historical performance [17], [18]. More recently, meta-learning has emerged as a powerful tool to enable models
torapidlyadapttonewtaskswithlimiteddata[19],[20].
Recent surveys have attempted to unify the field by categorizing continual learning methods based on
architecture, memory, regularization, and hybrid techniques [7], [21]. Despite promising developments,
challenges remain in evaluation consistency, generalization to unseen domains, and deploying these systems in
constrainedenvironments.
In addition to traditional settings, recent research has expanded lifelong learning into more complex and
realisticparadigmssuchasopen-worldlearning,unsupervisedcontinuallearning,andfederatedlifelonglearning.
In open-world learning, the system must not only recognize known classes but also detect and adapt to the
emergence of novel ones. Zhang et al. [22] proposed the ORE framework (Open Set Recognition with Episodic
Memory),whichintegratesanepisodicmemorymoduletoenhanceadaptabilitytonewcategorieswhileavoiding

MartinC.E.etal./AILS,Vol.1,56-66 3/11
overgeneralization. Such frameworks often combine out-of-distribution detection techniques with memory-
augmentednetworkstobalancestabilityandplasticityinevolvingenvironments.
Unsupervised continual learning (UCL) further pushes the boundaries by requiring models to learn
continuously in the absence of labels. Mundt et al. [23] introduced a strategy based on self-supervised
representations and dynamic clustering updates, which enables models to acquire and refine knowledge from
unlabelled streaming data. These methods are especially useful in real-world scenarios where annotation is
expensiveorinfeasible(Figure2).
Figure2.FlowchartImplementedintheSupervisorforManagingActions
In federated lifelong learning (FLL), learning occurs across multiple decentralized devices while preserving
user privacy.Chen et al.[24] designeda federated continual learningarchitecture withshared memory modules,
allowing knowledge transfer across tasks and clients while mitigating performance disparities between them.
These approaches often integrate task-specific decoders or gradient masking techniques to protect model
parametersrelatedtopasttasks.
There is also growing interest in class-imbalance-aware lifelong learning, which addresses the tendency of
modelstooverfittomajorityclassesinsequentialdatastreams.Solutionssuchasadaptivere-weighting,exemplar
selection, and loss calibration have shown promising results in preserving rare-class performance while
maintainingoverallaccuracy[25].
The diversity of these approaches demonstrates the richness and maturity of the lifelong learning field, yet
common challenges such as scalability, memory efficiency, fairness, and deployment in dynamic edge
environmentsremainopenresearchquestions.

4/11 MartinC.E.etal./AILS,Vol.1,56-66
METHODOLOGY
Weproposeanadaptivelearningframeworktailoredforevolvingdatastreams.Thearchitectureincorporates
three key functionalities: stream-aware preprocessing, drift-adaptive incremental learning, and memory-
constrained rehearsal. This section introduces the mathematical formulation, system design, and dynamic
learningstrategies.
ProblemDefinition
Let the input data stream be denoted as D={(xt,yt)}, where xt∈Rdx is a data instance at time ttt, and
yt∈Yy_t is the corresponding label (if available). The joint distribution Pt(x,y) may evolve over time due to
concept drift. Our goal is to learn a predictive function ft(x;θt) that continuously updates its parameters θt to
minimize(equation(1))(Figure3):
= ; , (1)
,
whileensuringknowledgeretentionanda ℒ d  apt  in  g  t  o  ∼n  e  w ℓ ly  em   er  g  ing  co  ncepts.
Figure3.AdaptiveLearningRateinDynamicalBinaryEnvironments
SystemArchitecture
TheoveralllearningpipelineisillustratedinTable1.
Table1.CoreComponentsoftheProposedFramework
Module Description
StreamPreprocessing Normalization,batchsegmentation,pseudo-labelingforunlabeleddata
DriftDetection Onlinedetectionusingstatisticalandembedding-baseddivergencemetrics
IncrementalUpdate Onlineoptimizationwithregularizationandreplay
MemoryManagement Exemplarselectionandknowledgedistillationforcompactrehearsal

| MartinC.E.etal./AILS,Vol.1,56-66 |     |     |     | 5/11 |
| -------------------------------- | --- | --- | --- | ---- |
DriftDetection
TodetectchangesinPt(x,y),weapplybothinputspaceandrepresentationspacedivergencemetrics(Figure
4).
1.StatisticalTest:ADWINmonitorsthechangeinerrororfeaturemean(equation(2)):
|     | =   | >   |     | (2) |
| --- | --- | --- | --- | --- |
|     | old | new |     |     |
2. Embedding Shift: We define the representation drift as the average cosine distance between embeddings
|     |     | −   |     |     |
| --- | --- | --- | --- | --- |
(equation(3)):
1
|     | Drift =1 |     |        | (3) |
| --- | -------- | --- | ------ | --- |
|     | rep      | =1  |        |     |
|     |          |     | ⋅   −  |     |

| whereht(i)isthelatentrepresentationattimet,andk−d |     | en o     |                           |     |
| ------------------------------------------------- | --- | -------- | ------------------------- | --- |
|                                                   |     | tes∥  a  | l∥o∥o  k  −b  a∥ckwindow. |     |
Figure4.ASurveyonActiveLearning:State-of-the-art,PracticalChallengesandResearchDirections
The architecture comprises four key modules: (1) stream preprocessing, (2) drift detection and
characterization, (3) incremental model optimization, and (4) memory consolidation. As summarized in Table I,
each module serves a specific role in maintaining adaptability, stability, and generalization. Preprocessing
includes normalization, mini-batching, and optional pseudo-labeling for partially labeled streams. This ensures
smoothdataintakeandfacilitatesfastinferenceinlow-latencyscenarios.
Todetectconceptdrift,wedeployadualdetectionmechanism thatevaluatesboththeinputdistributionand
the model’s internal representations. Statistical drift is monitored using adaptive sliding windows and change-
point tests such as ADWIN, where a significant change in the running mean = exceeding a
old new
threshold ϵ indicates drift. Concurrently, embedding-based drift is captured through cosine distance between
   −

| 6/11 | MartinC.E.etal./AILS,Vol.1,56-66 |     |     |     |
| ---- | -------------------------------- | --- | --- | --- |
hiddenrepresentationsacrosstimesteps.
IncrementalModelOptimization
Themodelisupdatedincrementallyusinganadaptiveregularizedloss(equation(4))(Figure5):
|                                     | = +        | ,    |     | (4) |
| ----------------------------------- | ---------- | ---- | --- | --- |
|                                     | total task | 1    |     |     |
| Ltask:cross-entropyormeansquarederr | or         | −    |     |     |
|                                     | ℒ ℒ        | ⋅    |     |     |
Ω:regularizationterm,suchasElasticWeightConsolidation(EWC)(equation(5)):
|     | ​   | 2   |     |     |
| --- | --- | --- | --- | --- |
|     | =   |     |     | (5) |
2
  ∗
whereFiistheFisherinformationmatrix di agon al ,andθ i ∗ −is thepreviousoptimum.
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
Figure5.PerformanceofNetworkSelectionPolicyonImage-net
To further clarify the system's behavior under various types of concept drift, we classify drift into three
common categories: sudden,gradual,and recurring.Each typeaffects themodeldifferently andrequires distinct
adaptationstrategies.Table2summarizesthesystem’sresponsemechanismsundereachdrifttype.
Table2.SystemAdaptationStrategiesforDifferentConceptDriftTypes
Drift
| DetectionSignal | ModelResponse |     | MemoryUpdateStrategy |     |
| --------------- | ------------- | --- | -------------------- | --- |
Type
| Sharpincreaseinlossor Immediatearchitectureresetorfine- |     |     |                                |     |
| ------------------------------------------------------- | --- | --- | ------------------------------ | --- |
| Sudden                                                  |     |     | High-priorityreplay+resampling |     |
error tune
Gradual Slowembeddingdivergence Incrementalupdatewithslowlearning Dynamicbufferrebalancing
Cyclicalpatternin Memorycacheretrieval+
| Recurring Retrievepriormodelstateifcached |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- |
distribution consolidation
This dynamic scaling ensures that the model is more plastic during drift, while reverting to stability when
datadistributionstabilizes.
Moreover, the memory update strategy also varies. In the case of recurring drift, the system utilizes latent
clustermatchingtodetectsimilaritiesbetweencurrentsamplesandstoreddistributions.Ifamatchisfound,prior
exemplarsarereplayedwithincreasedweight,ensuringrapidre-adaptation(equation(6)):
|     | = sim | ,   |     | (6) |
| --- | ----- | --- | --- | --- |
This selective weighting allows themode l  to q ui⋅ckly “rℎeca l  l” pℎre v  iously learned tasks without full retraining,
|     |     |     |     |     |
| --- | --- | --- | --- | --- |
minimizingcomputationaloverhead.

MartinC.E.etal./AILS,Vol.1,56-66 7/11
Lastly, to maintain computational feasibility in real-time scenarios, all components operate under bounded
memory and time constraints. The memory buffer M is capped at size K, and inference/update operations are
optimizedviamini-batchstreamingandsparsematrixoperations(Figure6).
Figure6.DifferentNetworkSelectionTopologiesthatWeConsidered
RESULTS AND DISCUSSION
To evaluate the effectiveness of the proposed adaptive learning framework, we conducted experiments on
both synthetic and real-world data stream benchmarks, focusing on classification tasks under evolving
distributions. We compared our method with several strong baselines, including Naïve Incremental Learning
(Naïve), Elastic Weight Consolidation (EWC) [9], Learning without Forgetting (LwF) [10], Gradient Episodic
Memory(GEM)[11],andExperienceReplay(ER)[12].
ExperimentalSetup
Weusedthefollowingdatasets:
RotatingMNIST:Asyntheticbenchmarkwherethedigitimagesarerotatedincrementallyfrom0°to180°in
stepsof10°tosimulategradualconceptdrift.
CIFAR-100 Split: The 100 classes are presented in 10 sequential tasks, each introducing 10 new classes,
evaluatingperformanceundertask-incrementallearning.
Electricity Pricing Dataset: A real-world dataset with temporal drift in consumption behavior, containing
timestampedbinaryclassificationtasks.
Airline Delay Dataset: Contains records of U.S. domestic flights with significant seasonal and feature drift
patterns.
Eachmodelwastrainedsequentiallyondatastreams,withoutaccesstofuturedata.Forourmethod,weused
arehearsalbufferofsize500andappliedembeddingdriftdetectionasdescribedinSectionIV(Figure7).

| 8/11 |     | MartinC.E.etal./AILS,Vol.1,56-66 |     |     |     |     |
| ---- | --- | -------------------------------- | --- | --- | --- | --- |
Figure7.ThePlotsShowtheAccuracyGainsatDifferentLayersforEarlyExitsforNetworks
AccuracyandStability
Table3summarizestheaverageaccuracyacrossalltasksforeachmethod,measuredafterthefinaltask(i.e.,
howwellthemodelretainspriorknowledge).
Table3.FinalAverageAccuracy(%)acrossTasks
| Method  | RotatingMNIST |     | CIFAR-100 | Electricity |     | AirlineDelay |
| ------- | ------------- | --- | --------- | ----------- | --- | ------------ |
| Naïve   | 61.4          |     | 44.5      | 78.1        |     | 71.6         |
| EWC[9]  | 72.1          |     | 55.3      | 79.5        |     | 74.2         |
| LwF[10] | 70.3          |     | 57.1      | 79.0        |     | 73.0         |
| ER[12]  | 74.8          |     | 61.4      | 80.2        |     | 75.1         |
| Ours    | 77.9          |     | 64.2      | 82.4        |     | 77.3         |
Our method consistently outperformed other baselines, particularly in scenarios with recurring and gradual
drift(e.g.,ElectricityandRotatingMNIST).This improvementisattributedtothedynamic detectionmechanism
andmodularupdatesthatreducebothcatastrophicforgettingandunderfittingtonewdistributions.
CatastrophicForgettingAnalysis
To quantify forgetting, we measured backward transfer (BWT), defined as the average difference in
performanceonpreviouslyseentasksbeforeandaftertrainingonnewtasks(equation(7))(Table4):
BWT= 1 1
, , (7)
1 =1
 −
where AT,i is the accuracy on task iii after train in g on  tas  k  T  ,−an  d   Ai is the accuracy after task iii was first
 −
learned.
Table4.BackwardTransfer(BWT%)
| Method |     | RotatingMNIST |     |     | CIFAR-100 |     |
| ------ | --- | ------------- | --- | --- | --------- | --- |
| Naïve  |     | -25.3         |     |     | -31.2     |     |
| EWC[9] |     | -13.8         |     |     | -18.4     |     |
| ER[12] |     | -10.1         |     |     | -11.3     |     |
| Ours   |     | -5.6          |     |     | -7.2      |     |
Our approach achieved the least negative BWT, confirming its strong retention of past knowledge while still
adapting to new distributions. This supports the theoretical claim that combining representation-based drift
detectionwithselectivememoryreplayyieldsoptimalstability-plasticitybalance.

MartinC.E.etal./AILS,Vol.1,56-66 9/11
ImpactofDriftDetection
To analyze the effectiveness of our drift detection mechanism, we ablated this component and compared
performance. Without drift detection, the model used fixed-interval updates. Results show a drop of 3.1–5.7% in
average accuracy, especially in environments with nonstationary behavior. Visualizations in Figure 3
demonstrate how dynamic drift-aware learning allows the model to adjust its learning rate and regularization
moreeffectivelythanstaticschedules.
ResourceEfficiency
Despiteits superior performance, ourmodel maintained comparabletrainingtime andmemory usagetoER
and EWC. Due to efficient update routines and bounded rehearsal buffers, the method remains practical for
deploymentinedgeoronlinesystems.
CONCLUSION
In this paper, we have proposed a novel adaptive learning architecture designed to effectively manage
evolving data streams, with a particular focus on challenges such as concept drift, catastrophic forgetting, and
dynamic knowledge integration. Our approach integrates a lightweight drift detection mechanism with modular
updates andselectivememory replay,enablingthemodeltodynamically adjustitslearningbehaviorin response
tochangesinthedatadistribution.
Comprehensive experiments across synthetic and real-world datasets demonstrate that our method
significantly outperforms several state-of-the-art continual learning baselines in terms of both accuracy and
knowledge retention. The results confirm that the combination of adaptive optimization and intelligent drift
handlingiscrucialforbuildingrobustandefficientlifelonglearningsystems.Furthermore,themethodmaintains
competitive computational overhead, making it well-suited for deployment in online and resource-constrained
environments.
Theproposed framework contributes not only to the practical performance of adaptive learning systems but
also enriches the theoretical understanding of balancing stability and plasticity in non-stationary settings. The
insights gained from this work open up new directions for continual learning research in dynamic real-world
scenarios,suchasreal-timemonitoring,edgecomputing,andautonomousagents.
Future work will explore more advanced strategies for unsupervised drift detection, meta-learning-driven
adaptationpolicies,andlong-termmemoryconsolidationacrossmultipletasks.Inaddition,weaimtoinvestigate
the application of our method to more complex domains such as natural language processing and multi-agent
reinforcementlearning,furtherextendingitsgeneralizabilityandscalability.

10/11 MartinC.E.etal./AILS,Vol.1,56-66
REFERENCES
[1] C. Aljundi, F. Babiloni, M. Elhoseiny, M. Rohrbach, and T. Tuytelaars, "Memory aware synapses: Learning
what (not) to forget," in Proceedings of the European Conference on Computer Vision (ECCV), 2018, pp.
139-154.
[2] R. Kemker, M. McClure, A. Abitino, T. Hayes, and C. Kanan, "Measuring catastrophic forgetting in neural
networks,"inProceedingsoftheAAAIConferenceonArtificialIntelligence,vol.32,no.1,2018.
[3] J. Gama, I. Žliobaitė, A. Bifet, M. Pechenizkiy, and A. Bouchachia, "A survey on concept drift adaptation,"
ACMComputingSurveys,vol.46,no.4,pp.1-37,2014.
[4] Y. Wang, Q. Yao, J. T. Kwok, and L. M. Ni, "Generalizing from a few examples: A survey on few-shot
learning,"ACMComputingSurveys,vol.53,no.3,pp.1-34,2020.
[5] S. Thrun and T. M. Mitchell, "Lifelong robot learning," Robotics and Autonomous Systems, vol. 15, no. 1-2,
pp.25-46,1995.
[6] T.Diethe,A.Borchert,M.Girolami,andN.Lawrence,"Continuallearninginpractice,"inProceedingsofthe
NeurIPS2019WorkshoponContinualLearning,2019.
[7] M. De Lange et al., “A continual learning survey: Defying forgetting in classification tasks,” IEEE
TransactionsonPatternAnalysisandMachineIntelligence,vol.44,no.7,pp.3366-3385,2021.
[8] D.Wang,Z.Yan,andJ.Li,"Acomprehensivesurveyofcontinuallearning:Theory,methodandapplication,"
Neurocomputing,vol.489,pp.249-270,2022.
[9] H. He and E. A. Garcia, "Learning from imbalanced data," IEEE Transactions on Knowledge and Data
Engineering,vol.21,no.9,pp.1263-1284,2009.
[10] I.Žliobaitė,"Learningunderconceptdrift:Anoverview,"2010.arXiv:1010.4784.
[11] J. Kirkpatrick et al., "Overcoming catastrophic forgetting in neural networks," Proceedings of the National
AcademyofSciences,vol.114,no.13,pp.3521-3526,2017.
[12] F.Zenke, B.Poole,and S.Ganguli,"Continual learningthrough synaptic intelligence,"in Proceedingsofthe
34thInternationalConferenceonMachineLearning(ICML),2017,pp.3987-3995.
[13] D. Lopez-Paz and M. Ranzato, "Gradient episodic memory for continual learning," in Advances in Neural
InformationProcessingSystems(NeurIPS),2017,pp.6467-6476.
[14] R. Rolnick et al., "Experience replay for continual learning,"in Advancesin Neural InformationProcessing
Systems(NeurIPS)Workshop,2019.
[15] A.Rusuetal.,"Progressiveneuralnetworks,"2016.arXiv:1606.04671.
[16] A. Mallya and S. Lazebnik, "PackNet: Adding multiple tasks to a single network by iterative pruning," in
Proceedings oftheIEEE Conference onComputer Vision andPattern Recognition (CVPR), 2018,pp. 7765-
7773.
[17] R. Polikar, L. Udpa, S. Udpa, and V. Honavar, "Learn++: An incremental learning algorithm for supervised
neuralnetworks,"IEEETransactionsonSystems,Man,andCybernetics,PartC,vol.31,no.4,pp.497-508,
2001.
[18] H.M.Gomesetal.,"Adaptiverandomforestsforevolvingdatastreamclassification,"MachineLearning,vol.
106,no.9,pp.1469-1495,2017.
[19] C. Finn, P. Abbeel, and S. Levine, "Model-agnostic meta-learning for fast adaptation of deep networks," in
Proceedingsofthe34thInternationalConferenceonMachineLearning(ICML),2017,pp.1126-1135.
[20]J. Snell, K. Swersky, and R. Zemel, "Prototypical networks for few-shot learning," in Advances in Neural
InformationProcessingSystems(NeurIPS),2017,pp.4077-4087.
[21] M.Masanaetal.,"Class-incrementallearning:surveyandperformanceevaluation,"2020.arXiv:2010.15277.
[22]H.Zhang, M. Cisse,Y. Dauphin, and D. Lopez-Paz,“Few-shot open-set recognition using meta-learning,” in
ProceedingsoftheIEEEConferenceonComputerVisionandPatternRecognition(CVPR),2020,pp.8798-
8807.
[23]M. Mundt, C. Hong, I. Pliushch, and V. Ramesh, “A wholistic view of continual learning with deep neural
networks:Forgottenlessonsandthefuture,”Neurocomputing,vol.438,pp.230-246,2021.

MartinC.E.etal./AILS,Vol.1,56-66 11/11
[24]Y. Chen, X. Yao, and M. Zhang, “Federated lifelong learning via dynamic task routing and shared memory,”
inProceedingsofthe38thAAAIConferenceonArtificialIntelligence,2024.
[25]A.Borsos,A.Mishra,andT.Hofmann,“Classimbalanceandlong-tailincontinuallearning,”inAdvancesin
NeuralInformationProcessingSystems(NeurIPS),2020,pp.14496-14508.