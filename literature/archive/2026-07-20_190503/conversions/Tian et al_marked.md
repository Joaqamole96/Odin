|     |     |     |     |     |     |     |     | TYPE OriginalResearch |               |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | ------------- | --- |
|     |     |     |     |     |     |     |     | PUBLISHED             | 27January2026 |     |
10.3389/frai.2026.1726900
DOI
Marketing-AutoM3L:
|     | domain-aware |     |     |     |     | automated |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
OPENACCESS
| EDITEDBY | machine |     |     | learning |     | for | financial |     |     |     |
| -------- | ------- | --- | --- | -------- | --- | --- | --------- | --- | --- | --- |
ZhilinZhang,
LumosAlpha,UnitedStates
|     | customer |     |     | analytics |     |     |     |     |     |     |
| --- | -------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
REVIEWEDBY
WisnuUriawan,
StateIslamicUniversitySunanGunungDjati,
Indonesia
| YiqingShen, | YeTian1,WenqianShao2* |     |     |     | andZihanDeng3 |     |     |     |     |     |
| ----------- | --------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
JohnsHopkinsUniversity,UnitedStates
Md.MortuzaAhmmed, 1EngageElement,Albany,NY,UnitedStates,2NewBeginningsCreatorNetwork,Monrovia,CA,
AmericanInternationalUniversityBangladesh, UnitedStates,3HarbinInstituteofTechnology,Harbin,China
Bangladesh
JingWan,
Verizon,UnitedStates
|     | Financial | customer | analytics |     | requires | specialized | machine |     | learning | pipelines |
| --- | --------- | -------- | --------- | --- | -------- | ----------- | ------- | --- | -------- | --------- |
*CORRESPONDENCE thatincorporatedomain-specificunderstandingofcustomerbehavior.Existing
WenqianShao
|     | automated | ML  | approaches |     | often | lack the | capacity | to effectively |     | construct |
| --- | --------- | --- | ---------- | --- | ----- | -------- | -------- | -------------- | --- | --------- |
wenqianshao72@gmail.com
marketing-relevantfeaturesandthatmanualconstructionofpredictivemodels
RECEIVED17October2025
REVISED03January2026 demandsspecializedexpertisethatisdifficultformanyinstitutionstoconsistently
ACCEPTED05January2026 secureandmaintain.Toaddressthisgap,weproposeanautomatedframework
PUBLISHED27January2026 for generating end-to-end machine learning pipelines tailored to financial
CITATION customer analytics tasks. The system processes raw customer datasets
TianY,ShaoWandDengZ(2026)
|     | alongside | natural | language |     | instructions, | and | autonomously |     | performs | data |
| --- | --------- | ------- | -------- | --- | ------------- | --- | ------------ | --- | -------- | ---- |
Marketing-AutoM3L:domain-aware
|     | modality | recognition, |     | domain-aware |     | feature | engineering, |     | model | selection, |
| --- | -------- | ------------ | --- | ------------ | --- | ------- | ------------ | --- | ----- | ---------- |
automatedmachinelearningforfinancial
customeranalytics.
|     | andpipeline | assembly. |     | The | frameworkautonomouslyperformsdomain-aware |     |     |     |     |     |
| --- | ----------- | --------- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
Front.Artif.Intell.9:1726900.
|     | feature | engineering |     | by automatically |     | computing |     | key marketing |     | indicators |
| --- | ------- | ----------- | --- | ---------------- | --- | --------- | --- | ------------- | --- | ---------- |
doi:10.3389/frai.2026.1726900
(RFMmetrics,CLV,engagementscores)—capabilitiesabsentingenericAutoML
COPYRIGHT
systems.Experimentalvalidationshowing1.4%to5.4%accuracyimprovements
©2026 Tian,ShaoandDeng.Thisisan
open-accessarticledistributedunderthe over existing automated ML techniques while reducing development time by
termsoftheCreativeCommonsAttribution
|     | nearly sevenfold. |     | Natural | language |     | interface | enabling | business | stakeholders | to  |
| --- | ----------------- | --- | ------- | -------- | --- | --------- | -------- | -------- | ------------ | --- |
License(CCBY).Theuse,distributionor
configurepipelineswithoutmachinelearningexpertise.
reproductioninotherforumsispermitted,
providedtheoriginalauthor(s)andthe
copyrightowner(s)arecreditedandthatthe
| originalpublicationinthisjournaliscited,in | KEYWORDS |     |     |     |     |     |     |     |     |     |
| ------------------------------------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accordancewithacceptedacademicpractice. automatedmachinelearning,domain-specificfeatureengineering,financialcustomer
Nouse,distributionorreproductionis analytics,largelanguagemodels,multimodallearning
permittedwhichdoesnotcomplywiththese
terms.
1 Introduction
|     | Financial      | institutions       |                 | increasingly  |                 | face the formidable   |           | dual challenge   |          | of predicting |
| --- | -------------- | ------------------ | --------------- | ------------- | --------------- | --------------------- | --------- | ---------------- | -------- | ------------- |
|     | nuanced        | customer           | behavior        | and           | proactively     | mitigating            | churn,    | as               | market   | competition   |
|     | intensifies    | and                | customer        | acquisition   |                 | costs soar—reportedly |           | being            | five     | times higher  |
|     | than the       | cost of            | retaining       | existing      | customers       | (Capponi              |           | et al., 2021).   | In       | this climate, |
|     | advanced       | customer           | analytics       | has           | become          | indispensable,        |           | driving          | critical | strategies in |
|     | customer       | retention,         | revenue         | optimization, |                 | and targeted          | marketing |                  | across   | the banking   |
|     | (Ogbuonyalu    | et                 | al., 2025;      | Mokoena,      |                 | 2025), insurance      |           | (Islayem         | et al.,  | 2025; Baro    |
|     | et al., 2025), | telecommunications |                 |               | (Yuan           | et al., 2025;         | Zou       | et al.,          | 2025),   | and financial |
|     | services       | sectors            | (Mokoena,       | 2025;         | Boinpally,      | 2025;                 | Shen      | et al.,          | 2025f;   | Han et al.,   |
|     | 2025). Despite |                    | its importance, |               | the traditional |                       | paradigm  | for constructing |          | predictive    |
modelsremainspredominantlymanual(KashyapandSinha,2024).Datascientistsmust
|     | painstakingly | engineer |     | domain-specific |     | features (such | as  | those derived | from | Recency- |
| --- | ------------- | -------- | --- | --------------- | --- | -------------- | --- | ------------- | ---- | -------- |
Frequency-Monetaryanalysis),selectappropriatemodelarchitectures,anditerativelytune
|     | hyperparameters. |     | This | labor-intensive |     | process not | only creates | significant |     | bottlenecks |
| --- | ---------------- | --- | ---- | --------------- | --- | ----------- | ------------ | ----------- | --- | ----------- |
thatconstrainorganizationalscalabilitybutalsodemandsaconcentrationofspecialized
| FrontiersinArtificialIntelligence |     |     | 01  |     |     |     |     |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

Tianetal. 10.3389/frai.2026.1726900
expertisethatisdifficultformanyinstitutionstoconsistentlysecure demandbothmarketingexpertiseandtechnicalskill(Borleetal.,
and maintain (Shen et al., 2022a,b). The resulting inefficiencies 2008).
underscore an urgent need for more automated, intelligent, and Rule-based automation systems are often too rigid to
accessibleanalyticalframeworks(Zhaoetal.,2025). accommodate the varied data formats and business contexts
Current automated machine learning (AutoML) systems are encountered in real-world financial settings (Sheikh and Conlon,
predominantlydesignedforgenerictabulardataandexhibitlimited 2012). Meanwhile, generic machine learning frameworks cannot
capacitytocapturedomain-specificconceptsessentialtofinancial readilyincorporatedomainknowledgewithoutsubstantialmanual
customer analytics (Lin et al., 2011; Qiao and Beling, 2016; configuration—underminingthegoalofautomation(Webb,1996).
Shen et al., 2025e; Lin et al., 2025). Specifically, these systems Furthermore, the steep learning curve of these systems prevents
fail to automatically identify critical marketing constructs—such businessstakeholdersfromdirectlyarticulatingtheirrequirements
as recency-frequency-monetary (RFM) relationships (Qi et al., totechnicalpipelines(GeethaandKrishna,2025).Thus,thereisa
2023), customer lifetime value (CLV) trajectories, and behavioral clearneedforsolutionsthatintegrateautomation,embeddomain
engagement sequences—that form the foundation of accurate expertise,andofferintuitivenaturallanguageinterfacestoenable
prediction in marketing contexts (Donepudi, 2019; Zhang et al., non-technicaluserstoguidethepipelinedesignprocess(Luoetal.,
2025). Consequently, significant manual intervention is still 2025;Zengetal.,2023).
required across multiple stages, including the identification of To address these challenges, we introduce an automated
relevant data modalities, the engineering of marketing-specific pipeline construction framework tailored for financial customer
features, and the configuration of model training pipelines analytics. Our focus is on practical method design and system
alignedwithbusinessobjectives.Thisdisconnectbetweenbusiness implementation rather than theoretical analysis, providing
requirementsandtechnicalimplementationpresentspractitioners practitioners with an immediately deployable solution for
with a persistent trade-off: accepting suboptimal performance automating domain-specific machine learning workflows. The
from generic AutoML solutions (Zhu et al., 2025) or dedicating systemtakesasinputrawcustomerdatasetsandnaturallanguage
considerable resources to manual customization (Bonidia et al., directives, and autonomously generates executable training
2022). pipelines optimized for marketing objectives. It performs several
Recent advances in large language models (LLMs) have keystepsautomatically:
unlocked new potential for automating end-to-end machine Thecoreprocessingstepsoftheframeworkincludemodality
learningworkflows(Fastowskietal.,2025).Thesemodelsexhibit recognitiontoidentifyattributetypeswithinthedataset,domain-
strongreasoningcapacities(Shenetal.,2025a;ShenandUnberath, awarefeatureengineeringtoderivemarketing-relevantindicators,
2025;Shenetal.,2025d),codegenerationproficiency(Luoetal., as well as model selection based on data characteristics, the
2024a),andnaturallanguageunderstanding(Shenetal.,2025b,c; assembly of multimodal pipelines that integrate heterogeneous
ShiandShen,2025),facilitatingnovelparadigmsfororchestrating data sources, and the optimization of training configurations—
complextechnicalprocesses(Liuetal.,2024;Shenetal.,2024b,a). including hyperparameter tuning. At each stage, LLMs act as
Specifically, LLMs can infer data semantics from metadata such intelligent controllers, making contextual decisions according to
ascolumnnamesandsamplevalues,interpretbusinessdirectives dataproperties,businessgoals,andcomputationalconstraints.
conveyed in natural language, and generate executable code that Our framework incorporates established marketing analytics
incorporates appropriate preprocessing and modeling strategies methodsforcustomerbehaviorprediction,includingRFManalysis
(Novikovaetal.,2025).Thiscapabilityoffersapromisingpathway for segmentation based on recency, frequency, and monetary
tobridgethegapbetweenbusinessstakeholders—whopossessdeep value; customer lifetime value modeling for revenue projection
customeranalyticsexpertise—andthetechnicalsystemsrequiredto and retention prioritization; and behavioral engagement scoring
buildpredictivemodels. to quantify cross-channel customer involvement. The system
Financial customer data typically integrates multiple also recognizes financial-domain patterns such as transaction
heterogeneous sources, including transaction histories, sequences, account relationships, and service usage histories.
demographic profiles, interaction logs, and communication Through natural language directives, business intents are
records. Each data modality demands specialized preprocessing translatedintotechnicalimplementations.Forinstance,agoalto
andmodelingtechniquestoextractpredictivesignals(Zhouetal., “maximize customer retention” guides the system to construct
2025). Domain knowledge is critical for designing informative features reflecting engagement trends and relationship duration,
features that capture customer behavior and value patterns (Luo while a focus on “deployment speed” leads to more efficient
et al., 2023). Established frameworks such as recency-frequency- model architectures. This process enables business experts
monetary (RFM) analysis enable customer segmentation based to directly shape pipeline design without requiring machine
ontransactionalbehavior,whileengagementscoringconsolidates learningexpertise.
diverseinteractionsignalsintounifiedmetricspredictiveoffuture Themaincontributionsofthisstudyareasfollows:Firstly,it
activity (Rajendran, 2025). Similarly, customer lifetime value proposes an end-to-end framework that automates ML pipeline
(CLV)modelingprojectsthetotalvalueacustomerwillgenerate construction for financial customer analytics, which generates
throughout their relationship with the organization. Current executable training code from natural language directives and
automatedtools,however,oftenforceatrade-off:usersmusteither raw data without manual coding. This addresses the critical
acceptgenericfeatureengineeringthatoverlooksdomain-specific gap where business stakeholders possess deep customer analytics
patterns,orresorttomanual,time-intensivetransformationsthat expertise but lack technical programming skills to implement
FrontiersinArtificialIntelligence 02 frontiersin.org

| Tianetal. |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- |
predictive models. Secondly, it incorporates domain-specific Team, 2022). Recent work has extended AutoML capabilities
feature engineering components that automatically compute to specialized domains, with applications in medical diagnosis
marketing-relevant indicators such as RFM scores, customer achieving detection accuracies of 84.4% using no-code platforms
lifetime value, and engagement metrics. Unlike generic AutoML like Teachable Machine (Arora et al., 2024; Liu et al., 2025;
systems that apply only standard preprocessing operations, our Gao et al., 2025). The integration of meta-learning approaches
frameworkembedsestablishedmarketinganalyticsmethodologies allowssystemstoleverageknowledgefrompreviousexperiments
directly into the automation process, eliminating the need to improve performance on new datasets (Gomaa et al., 2024).
for manual feature design. Additionally, it realizes automated Evaluation studies across diverse datasets spanning tabular data,
modelselectionandhyperparameteroptimizationguidedbydata time series, and image classification reveal that proprietary
characteristicsandbusinessobjectives,reducingdevelopmenttime cloud-based tools often outperform open-source alternatives in
by nearly sevenfold while maintaining predictive performance. terms of computational efficiency and scalability, while open-
This intelligent optimization eliminates the extensive manual sourceplatformsprovidegreatermodelinterpretability(Gancheva
experimentationtypicallyrequiredinhyperparametertuningwhile et al., 2024). However, persistent challenges include lack of
ensuring models remain aligned with business priorities such as transparencyinadvancedneuralarchitecturesearchmechanisms,
interpretability or deployment constraints. Finally, it conducts computational scalability for large datasets, and the need for
experimental validation across five customer analytics datasets better bias mitigation strategies (IEEE Standards Committee,
spanning telecommunications, banking, e-commerce, insurance, 2024). Contemporary research focuses on developing domain-
andmarketingcampaigns,demonstratingaccuracyimprovements specific AutoML frameworks that balance automation with
of1.4%to5.4%overexistingautomatedandmanualapproaches. humanoversight,particularlyinregulatedindustrieswheremodel
The remainder of this paper is structured as follows. Section explainabilityisparamount(Narayanaetal.,2024).
| 2 reviews | related | work. | Section | 3 introduces | our proposed |     |     |     |     |     |     |
| --------- | ------- | ----- | ------- | ------------ | ------------ | --- | --- | --- | --- | --- | --- |
Marketing-AutoM3LFrameworkanditsimplementation.Section
| 4 presents | the experimental |     | results, | followed | by analysis | and          |     |           |     |       |     |
| ---------- | ---------------- | --- | -------- | -------- | ----------- | ------------ | --- | --------- | --- | ----- | --- |
|            |                  |     |          |          |             | 2.2 Customer |     | analytics | and | churn |     |
discussion.Finally,Section5concludesthepaper.
|           |      |     |     |     |     | prediction  | methods    |            |               |         |             |
| --------- | ---- | --- | --- | --- | --- | ----------- | ---------- | ---------- | ------------- | ------- | ----------- |
| 2 Related | work |     |     |     |     |             |            |            |               |         |             |
|           |      |     |     |     |     | Customer    | churn      | prediction | has evolved   | from    | traditional |
|           |      |     |     |     |     | statistical | approaches | to         | sophisticated | machine | learning    |
This section focuses on practical AutoML systems and methodologies that capture complex behavioral patterns in
appliedmethodologiesratherthantheoreticalfoundations,asour
|     |     |     |     |     |     | customer data | (Jain | et al., | 2023). Early | approaches | relied on |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | ------- | ------------ | ---------- | --------- |
contributionliesinAIsystemdesignandempiricalvalidationfor logistic regression models due to their interpretability and ease
domain-specificapplications. of implementation, providing probability estimates for churn
eventswhileenablingstraightforwardfeatureimportanceanalysis
|               |     |         |     |          |         | (Boozary et | al., 2025). | Ensemble | methods, | particularly | Random |
| ------------- | --- | ------- | --- | -------- | ------- | ----------- | ----------- | -------- | -------- | ------------ | ------ |
| 2.1 Automated |     | machine |     | learning | systems |             |             |          |          |              |        |
ForestandGradientBoostingMachines,havegainedprominence
and frameworks
fortheirabilitytohandlenon-linearrelationshipsandinteractions
|     |     |     |     |     |     | between customer | attributes |     | without requiring | extensive | feature |
| --- | --- | --- | --- | --- | --- | ---------------- | ---------- | --- | ----------------- | --------- | ------- |
Thegrowingcomplexityandexpertiserequiredintraditional preprocessing(Akteretal.,2025).
machine learning workflows have spurred the development Deeplearningarchitectureshaveshownpromiseincapturing
of Automated Machine Learning (AutoML), which aims to sequentialdependenciesincustomerbehavior,withhybridmodels
democratize access to advanced data analytics across various likeBiLSTM-CNNachievingsuperiorperformancebycombining
domains (Mumuni and Mumuni, 2024). Early AutoML systems, bidirectional context modeling with spatial feature extraction
such as TPOT, leveraged genetic programming to automatically (Jainet al.,2023). RFManalysis(Recency,Frequency,Monetary)
evolve machine learning pipelines. In contrast, modern cloud- has become a cornerstone methodology in customer analytics,
based platforms like Google Cloud AutoML and Amazon providing an intuitive framework for customer segmentation
SageMaker Autopilot represent the current state of the art, based on transactional behavior (GeeksforGeeks, 2021). Modern
demonstrating superior scalability by harnessing distributed implementationsextendtraditionalRFMmetricswithautomated
computing resources (TechAhead, 2024). A common thread feature engineering techniques that generate customer lifetime
among these systems is the automation of core pipeline stages— valueprojectionsandengagementscoringmechanisms(Optimove,
| includingdatapreprocessing,modelselection,andhyperparameter |     |     |     |     |     | 2023). |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
optimization—primarily through techniques like Bayesian Machine learning applications in customer analytics
optimizationandneuralarchitecturesearch.Persistentchallenges demonstrate measurable business impact, including 20%
includelackoftransparencyinadvancedneuralarchitecturesearch improvements in customer engagement rates and significant
mechanisms, computational scalability for large datasets, and the reductions in churn prediction false positive rates (Nelson
needforbetterbiasmitigationstrategies. et al., 2025). Feature engineering remains critical for model
Featuretoolsrepresentsanotableadvancementinautomated performance, with domain-specific transformations capturing
featureengineering,enablingthegenerationofcomplextemporal marketing-relevantpatternssuchasseasonalpurchasingbehavior
andrelationalfeaturesthroughdeepfeaturesynthesis(Hopsworks and cross-product affinity (Sica et al., 2025). Recent advances
| FrontiersinArtificialIntelligence |     |     |     |     |     | 03  |     |     |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Tianetal.      |          |              |          |            |             |          |         |              |     |        |                   | 10.3389/frai.2026.1726900 |     |     |
| -------------- | -------- | ------------ | -------- | ---------- | ----------- | -------- | ------- | ------------ | --- | ------ | ----------------- | ------------------------- | --- | --- |
| incorporate    | ensemble |              | learning | approaches |             | that     | combine | 3 Methods    |     |        |                   |                           |     |     |
| multiple       | model    | predictions, |          | leading    | to more     | robust   | churn   |              |     |        |                   |                           |     |     |
|                |          |              |          |            |             |          |         | 3.1 Overview |     | of the | Marketing-AutoM3L |                           |     |     |
| identification | systems  | that         | can      | adapt      | to changing | customer |         |              |     |        |                   |                           |     |     |
framework
| behavior   | patterns   | (Jain | et al., | 2023).   | The       | field continues |       |     |     |     |     |     |     |     |
| ---------- | ---------- | ----- | ------- | -------- | --------- | --------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| to address | challenges |       | related | to class | imbalance | in              | churn |     |     |     |     |     |     |     |
datasets, temporal drift in customer preferences, and the The Marketing-AutoM3L framework presents an end-
integration of unstructured data sources such as customer to-end solution for automating machine learning pipeline
communications and social media interactions (Ahmad et al., construction in customer analytics. It takes raw customer
2019). data and natural language directives as dual inputs to
|                |     |         |     |          |     |     |     | generate       | executable  | training | pipelines | for          | marketing         | tasks |
| -------------- | --- | ------- | --- | -------- | --- | --- | --- | -------------- | ----------- | -------- | --------- | ------------ | ----------------- | ----- |
|                |     |         |     |          |     |     |     | like churn     | prediction, | customer |           | lifetime     | value estimation, |       |
|                |     |         |     |          |     |     |     | and engagement |             | scoring. | The       | architecture | comprises         | five  |
| 2.3 Multimodal |     | machine |     | learning |     | and |     |                |             |          |           |              |                   |       |
interconnectedstages:datamodalityrecognition,domain-specific
| LLM-based |     | automation |     |     |     |     |     |                      |               |       |              |               |               |     |
| --------- | --- | ---------- | --- | --- | --- | --- | --- | -------------------- | ------------- | ----- | ------------ | ------------- | ------------- | --- |
|           |     |            |     |     |     |     |     | feature engineering, |               | model | architecture | selection,    | multimodal    |     |
|           |     |            |     |     |     |     |     | pipeline             | construction, | and   | training     | configuration | optimization. |     |
The integration of Large Language Models with automated Large language models (LLMs) act as intelligent controllers
| machine | learning | has opened |     | new possibilities |     | for intelligent |     |              |         |           |      |      |                 |     |
| ------- | -------- | ---------- | --- | ----------------- | --- | --------------- | --- | ------------ | ------- | --------- | ---- | ---- | --------------- | --- |
|         |          |            |     |                   |     |                 |     | across these | stages, | utilizing | both | data | characteristics | and |
pipeline construction and natural language-driven model natural language business objectives to make context-aware
development(Luoetal.,2024a).AutoM3Lrepresentsapioneering
|     |     |     |     |     |     |     |     | decisions. | This LLM-driven |     | orchestration | allows | the framework |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------------- | ------ | ------------- | --- |
approach that employs LLMs as controllers to automatically to adapt preprocessing, feature engineering, model selection,
constructmultimodaltrainingpipelines,addressinglimitationsof and training procedures, bridging marketing expertise with
| traditional | rule-based | AutoML |     | systems | through | natural | language |     |     |     |     |     |     |     |
| ----------- | ---------- | ------ | --- | ------- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
technicalexecutionwhileensuringscalabilityandinterpretability.
interaction (Luo et al., 2024b). This framework demonstrates Figure1 presents the overall architecture of the proposed
| the ability | to  | process | heterogeneous |     | data | types including |     |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ------------- | --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Marketing-AutoM3Lframework.
tabular, text, and temporal modalities through specialized Our research methodology proceeds through five sequential
model architectures and late fusion strategies (OpenReview, phases,eachaddressingaspecifictechnicalchallengeinautomated
2024).
pipelineconstruction.Phase1involvesdatamodalityrecognition
LLM-driven automation extends beyond simple code to identify attribute types and their semantic meanings.
| generation | to encompass |     | intelligent | decision-making |     | throughout |     |         |            |              |     |         |             |     |
| ---------- | ------------ | --- | ----------- | --------------- | --- | ---------- | --- | ------- | ---------- | ------------ | --- | ------- | ----------- | --- |
|            |              |     |             |                 |     |            |     | Phase 2 | implements | domain-aware |     | feature | engineering | to  |
the machine learning workflow, from data preprocessing to generate marketing-relevant indicators. Phase 3 performs
modeldeployment(Sampleetal.,2024).Multi-agentframeworks model architecture selection based on data characteristics and
| like AutoML-Agent |     | introduce |     | retrieval-augmented |     |     | planning |          |               |       |              |            |            |     |
| ----------------- | --- | --------- | --- | ------------------- | --- | --- | -------- | -------- | ------------- | ----- | ------------ | ---------- | ---------- | --- |
|                   |     |           |     |                     |     |     |          | business | requirements. | Phase | 4 constructs | integrated | multimodal |     |
strategies that enhance exploration in the model search space, pipelines through late fusion strategies. Phase 5 optimizes
decomposingcomplexMLtasksintospecializedsub-taskshandled
|     |     |     |     |     |     |     |     | training | configurations | including |     | hyperparameter | tuning | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --------- | --- | -------------- | ------ | --- |
by domain-specific agents (Trirat et al., 2025). These systems computationalresourceallocation.
| leverage   | case-based    | reasoning | to          | structure | iterative    | improvement |         |          |              |     |     |                |     |     |
| ---------- | ------------- | --------- | ----------- | --------- | ------------ | ----------- | ------- | -------- | ------------ | --- | --- | -------------- | --- | --- |
| pipelines, | incorporating |           | expert      | knowledge | from         | platforms   | like    |          |              |     |     |                |     |     |
| Kaggle to  | guide         | model     | development |           | decisions    | (Guo        | et al., |          |              |     |     |                |     |     |
| 2024).     |               |           |             |           |              |             |         | 3.2 Data | organization |     | and | representation |     |     |
| Multimodal | data          | fusion    | strategies  |           | have evolved | to          | address |          |              |     |     |                |     |     |
alignment challenges across different data types, with early Marketingdatasetstypicallyoriginatefromdisparatesources:
fusion approaches combining raw features at the input level customerrelationshipmanagementsystems,transactiondatabases,
while late fusion methods integrate model predictions from web analytics platforms, and interaction logs. We organize this
modality-specificarchitectures(EducativeTeam,2023).Advanced heterogeneous information into structured tables where each
fusiontechniquesemployattentionmechanismsandtransformer row represents a customer or interaction event, and columns
architectures to model cross-modal interactions, particularly capture various attributes. This tabular representation preserves
beneficial for tasks requiring joint understanding of textual and relationships between different data types while providing a
visual information. Contemporary research addresses missing format that LLM can analyze effectively (Luo et al., 2024a; Qian
modality scenarios through graceful degradation mechanisms and Shen, 2025; Wen et al., 2024). The framework preserves
and cross-modal knowledge transfer (Qian and Shen, 2025; the chronological order of temporal data, such as transaction
Sun et al., 2025; Ye et al., 2025; Gao et al., 2025), essential sequences, using a structured tabular format. Each transaction is
for robust deployment in real-world environments where recordedwithmetadatacontainingtimestamps,amounts,product
data availability varies (LabelYourData Team, 2024). The categories,andcontextualattributes.Theseorderedsequencesare
field faces ongoing challenges in computational complexity thenprocessedtoextractbehavioralpatterns,trends,andrecurring
management, temporal and spatial alignment of multimodal motifs,whichformthebasisforpredictingcustomerbehavior.This
streams,andthedevelopmentofinterpretablefusionmechanisms temporalstructureenablestheidentificationofcriticalindicators—
that can explain cross-modal reasoning processes (Wu et al., includingpurchaseperiodicity,spendingtrends,andengagement
2025). trajectories—essentialforaccuratebehavioralforecasting.
| FrontiersinArtificialIntelligence |     |     |     |     |     |     |     | 04  |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Tianetal. |     |     |     |     |     | 10.3389/frai.2026.1726900 |
| --------- | --- | --- | --- | --- | --- | ------------------------- |
FIGURE1
TheframeworkofMarketing-AutoM3Lshowingthedual-modulearchitectureforautomatedpipelineconstruction.TheIntelligentProcessing
Module(left)receivesuserqueriesaboutfinancialdecisionsandexecutesafour-stagestrategy:datamodalityrecognitiontoidentifyfeaturetypes
fromtimeseriesandfinancialdata,domainfeatureengineeringtoconstructmarketing-specificindicators,modelarchitectureselectionbasedon
datacharacteristics,andmultimodalpipelineassembly.TheKnowledgeSupplementationModule(right)providesdomainexpertisethrough
marketingknowledgerepositoriesandcompletechain-of-thoughtreasoning.TheframeworkincludesanIndicatorTrendSummarycomponentthat
analyzestemporalpatternsfromfinancialnews(e.g.,USdollarindexfluctuations,Bitcoinpricemovements,crudeoiltrends)andgenerates
executabletrainingpipelinesthroughproactiveconsultation.Theexamplequerydemonstrateshownaturallanguageinstructionsaretransformed
intoautomatedpipelineconfigurationswithappropriatestatisticaltestsanddatatransformations(ShenandZhang,2025).
3.3 Data modality recognition modules. This approach offers greater adaptability than rule-
|     |     |     |     | based heuristics, | handling domain-specific | naming conventions |
| --- | --- | --- | --- | ----------------- | ------------------------ | ------------------ |
Accurate identification of data types is essential for applying and irregular data formats. For example, a column labeled
appropriate preprocessing and modeling techniques (Luo et al., “customer_value_tier”mayrepresentencodednumericalvaluesin
2024a). The problem of accurate data type identification is one dataset and categorical labels in another. The LLM resolves
essential because incorrect classification leads to inappropriate suchambiguitiesbyanalyzingboththesemanticsofcolumnnames
preprocessing,suchastreatingcategoricalidentifiersasnumerical and the distribution of data values, and can incorporate user
features. Our solution employs LLM-based analysis of three instructionsthatprovideessentialbusinesscontext.
| information | sources: attribute | names, sample | values, and user- |     |     |     |
| ----------- | ------------------ | ------------- | ----------------- | --- | --- | --- |
providedcontext.Themodalityrecognitionmoduleanalyzeseach
| attribute in       | the customer dataset | to determine  | its fundamental |                     |         |             |
| ------------------ | -------------------- | ------------- | --------------- | ------------------- | ------- | ----------- |
|                    |                      |               |                 | 3.4 Domain-specific | feature | engineering |
| nature. The        | framework examines   | three sources | of information  |                     |         |             |
| via LLM: attribute | names, which         | often contain | semantic        | cues                |         |             |
aboutthedatatype;samplevaluesfromthedataset,whichreveal Marketing analytics benefits from specialized feature
distributional properties and formats; and user-provided context engineering that captures customer value, engagement
aboutthebusinessproblemanddatasources.TheLLMprocesses patterns, and behavioral trends. The framework implements
a structured prompt containing example attribute classifications two complementary components: feature filtering and feature
from diverse marketing datasets. These examples illustrate the construction. The filtering component identifies and removes
distinctionbetweenkeydatatypes:numericalmeasurements(e.g., attributesthatareunlikelytocontributetopredictivevalue,suchas
purchaseamounts,engagementscores),categoricalvariables(e.g., uniqueidentifiers,redundantencodingsofthesameinformation,
customersegments,productcategories),temporalsequences(e.g., or fields with excessive missing values. The construction
transaction histories), and text fields (e.g., customer feedback, component generates derived features that encode marketing-
communication logs). The model then outputs its classifications relevant concepts. The core problem in marketing analytics is
in a structured format for direct consumption by downstream that raw transactional data does not directly capture customer
| FrontiersinArtificialIntelligence |     |     |     | 05  |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --------------- |

| Tianetal. |     |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
value patterns and behavioral trends. Our solution implements 3.4.2 Customerlifetimevalueprojection
specialized construction components that automatically compute Theframeworkcalculatescustomerlifetimevalueprojections
RFMmetrics,customerlifetimevalueprojections,andengagement whensufficienthistoricaldataexists.Thismetricestimatesthetotal
scores without manual intervention. All domain features are value a customer will generate over their relationship with the
computed relative to a prediction reference time t that business.Weimplementthreecomplementaryapproachesselected
pred
represents the temporal point at which predictions are made in automaticallybasedondatacharacteristicsandavailability.
practice. For model training and evaluation, we establish t pred The historical averaging method is suitable for datasets with
for each customer based on their observation window, ensuring stablecustomerbehaviorpatternsandcomputesCLVas:
| that only | historical | information |     | available | before | t pred is | used for |     |     |     |     |     |     |     |     |
| --------- | ---------- | ----------- | --- | --------- | ------ | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
feature computation. For churn prediction tasks, t typically CLVh ist=AOVi ×PFi ×CLi (3)
|     |     |     |     |     |     | pred |     |     |     | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
representstheendofthecustomer’shistoricalobservationperiod,
andthepredictiontarget(churnstatus)isobservedinasubsequent whereAOVi =Mi /Fiistheaverageordervalue,PFi =Fi /Tiisthe
evaluation window (typically 30–90 days after t ). This strict purchase frequency (transactions per unit time with Ti being the
pred
temporalseparationpreventsanyformofdataleakagewherefuture customerrelationshipduration),andCLiistheprojectedcustomer
informationcouldcontaminatethefeaturesusedforprediction. lifespanestimatedfromtheaveragerelationshipdurationofsimilar
customersinthesameRFMsegment.
|     |     |     |     |     |     |     |     | The probabilistic |     | model | incorporates |     | customer | retention |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ----- | ------------ | --- | -------- | --------- | --- |
3.4.1 RFManalysisandscoring probability estimated from historical churn patterns, providing
| The       | feature   | construction |     | process               | focuses  | on established |          |                    |     |             |     |            |      |             |     |
| --------- | --------- | ------------ | --- | --------------------- | -------- | -------------- | -------- | ------------------ | --- | ----------- | --- | ---------- | ---- | ----------- | --- |
|           |           |              |     |                       |          |                |          | more accurate      |     | projections | for | businesses | with | significant |     |
| marketing | analytics | frameworks.  |     | For transaction-based |          |                | customer | customerattrition: |     |             |     |            |      |             |     |
| data, the | framework | implements   |     | RFM                   | analysis | by computing   |          |                    |     |             |     |            |      |             |     |
(cid:2)T
t h r ee me t ri c s f o r ea c h c u s t om e r : R e c e n cy , d e fi n e d a s th e ti m e AOV × P F ×r t
|     |     |     |     |     |     |     |     |     | CLV | p rob= |     | i   | i i |     | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
e la p sed si n c e t h e m o s t r e c e n t t r a n sa c t io n ; F re q u e n cy , m e asu r ed i +
|     |     |     |     |     |     |     |     |     |     |     |     | ( 1 | d ) t |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
as the number of transactions within a specified time window; t=1
andMonetaryvalue,calculatedasthetotaloraveragetransaction
whereriistheretentionprobabilityforcustomeriestimatedusing
amount.Thesethreedimensionsprovideacompactrepresentation
logisticregressiononhistoricalchurneventswithRFMscoresas
ofcustomerengagementandvalue.Formally,forcustomeriwith
{t1,t2,...,tn } {s1,s2,...,sn } predictors, d is the discount rate (typically set to the business’s
| transactions         |     |              | occurring | at  | times |     | with |                  |            |             |         |           |             |               |          |
| -------------------- | --- | ------------ | --------- | --- | ----- | --- | ---- | ---------------- | ---------- | ----------- | ------- | --------- | ----------- | ------------- | -------- |
|                      |     |              |           |     |       |     |      | cost of capital, | defaulting |             | to 0.10 | if not    | specified), | and           | T is the |
| amounts{a1,a2,...,an |     | },wecompute: |           |     |       |     |      |                  |            |             |         |           |             |               |          |
|                      |     |              |           |     |       |     |      | projection       | horizon    | (defaulting | to      | 36 months | for         | subscription- |          |
(cid:2)n
basedbusinessesand12monthsfortransactionalbusinesses).The
| =tcurrent | −max(s1,s2,...,sn), |     |     |     | =n, | =   |     |     |     |     |     |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ri Fi Mi aj (1) retention probability is computed as ri = σ(β + β RSR(i) +
0
|     |     |     |     |     |     | j=1 |     | β +    | β       |       | σ(·) |             |          |     | β   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ----- | ---- | ----------- | -------- | --- | --- |
|     |     |     |     |     |     |     |     | FSF(i) | MSM(i)) | where | is   | the sigmoid | function |     | and |
coefficientsareestimatedfromhistoricaldatathroughmaximum
wheretcurrentrepresentstheanalysisreferencetime.
likelihoodestimation.Topreventtargetleakageintheprobabilistic
| To  | ensure | RFM metrics |     | have | consistent | interpretable |     |     |     |     |     |     |     |     |     |
| --- | ------ | ----------- | --- | ---- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ranges suitable for machine learning models, the framework CLV model, retention probabilities ri are estimated using only
historicalchurneventsthatoccurredstrictlybeforetheobservation
| applies percentile-based |     |     | scoring | that transforms |     | raw values | into |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ------- | --------------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
standardized scores. For each metric dimension X ∈ {R,F,M}, cutoff time T. Specifically, we fit the logistic regression model
usingacohortofcustomerswhoseobservationwindowsendedat
| the scoring | function | maps | the | raw value | Xi to | a discrete | score |     |     |     |     |     |     |     |     |
| ----------- | -------- | ---- | --- | --------- | ----- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
SX(i)∈{1,2,3,4,5}basedonquintilethresholds: least H days before time T (where H is the prediction horizon),
|     |     | ⎧   |     |     |     |     |     | ensuringthattheirsubsequentchurnoutcomesarefullyobserved |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
⎪⎪⎪⎪⎪⎪⎪⎨ 5 i f X ≥ P 0(X ) w it h o ut o v e rl a p pin g w i th t h e c u r r e n t p r ed i c t i o n pe ri o d . T h i s
|     |     |     | i   | 8   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4 i f P6 (X ) ≤ X <P80(X) sta g e d est i m a t io n ap pr o a ch g u ar a n t e e s th a t r e t e n t ion p r o b ab il it y
|     |     |     |     | 0   | i   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SX(i)= p a r a m e t er s a r e d e r iv e d f r o m g e n u i n e ly h i s t or i c a l d a t a a n d c o n ta in
|     |     | 3   | i f P | ( X ) ≤ X | < P | ( X ) | (2) |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
⎪⎪⎪⎪⎪⎪⎪⎩ 4 0 i 6 0 n o i n f o r m a t i o n a b o u t ta r g e t o u t c o m e s in t h e p re d i c t i o n h or i z o n .
|     |     |     |         | ≤         | <       |       |     |         |               |          |                 |          |           |            |           |
| --- | --- | --- | ------- | --------- | ------- | ----- | --- | ------- | ------------- | -------- | --------------- | -------- | --------- | ---------- | --------- |
|     |     | 2   | i f P 2 | 0 ( X ) X | i P 4 0 | ( X ) |     |         |               |          |                 |          |           |            |           |
|     |     |     |         |           |         |       |     | T h e c | o h o r t - b | a se d m | e t h o d o l o | g y se g | m e n t s | c u s to m | e r s b y |
<P20(X)
1 ifXi acquisitionperiodandmodelslifetimevaluetrajectoriesspecificto
eachcohort,capturingtemporaltrendsincustomerbehavior:
| where P k | (X) denotes | the           | k-th | percentile | of the   | distribution | of       |     |     |     |     |     |     |     |     |
| --------- | ----------- | ------------- | ---- | ---------- | -------- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| metric X  | across      | all customers |      | in the     | dataset. | Note         | that for |     |     |     |     |     |     |     |     |
(cid:2)T
m ×r
recency, lower values indicate more recent transactions and thus CLVcohort= c(i),t c(i),t (5)
|     |     |     |     |     |     |     |     |     |     | i   |     | (1+d)t |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
receive higher scores, so the framework reverses the scoring t=1
| direction: | SR(i) = | 6−S | R(cid:5)(i) where | S R(cid:5)(i) | is computed |     | using the |     |     |     |     |     |     |     |     |
| ---------- | ------- | --- | ----------------- | ------------- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
standardscoringfunction.ThefinalRFMcompositescorecanbe wherec(i)denotesthecohorttowhichcustomeribelongs(defined
represented as a three-digit concatenation (SR(i),SF(i),SM(i)) or by acquisition month), mc,t is the average monthly revenue per
|     |     |     | =   | wRSR(i)+wFSF(i)+wMSM(i) |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as a weighted aggregate RFMi customer in cohort c at time t since acquisition, and rc,t is
where weights (wR,wF,wM) are determined based on univariate the cohort-specific retention rate at time t. Parameters mc,t and
correlationwiththepredictiontarget,withtheconstraintwR +wF + rc,t(cid:7)are estimated empirically from historical cohorts: mc,t =
| =1.                               |     |     |     |     |     |     |     | 1              |     |          | =   | A c t i v e       |       | C               |        |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | ----------------- | ----- | --------------- | ------ |
| wM                                |     |     |     |     |     |     |     | j∈C Revenuej,t |     | and rc,t |     | c ,t              | where | c is the        | set of |
|                                   |     |     |     |     |     |     |     | N c c          |     |          | A   | ct i v e c ,t − 1 |       |                 |        |
| FrontiersinArtificialIntelligence |     |     |     |     |     |     |     | 06             |     |          |     |                   |       | frontiersin.org |        |

| Tianetal. |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
customersincohortc,Nc = |C |,andActivec,t isthenumberof InadditiontotherawengagementscoreEi(t),theframework
c
activecustomersfromcohortcattimet. computes engagement trend features that capture temporal
The framework automatically selects among these three dynamicsincustomerbehavior:
| approaches | based | on data availability |     | and business |     | context. | The |     |             |     |     |         |     |              |
| ---------- | ----- | -------------------- | --- | ------------ | --- | -------- | --- | --- | ----------- | --- | --- | ------- | --- | ------------ |
|            |       |                      |     |              |     |          |     | −   | − (cid:7)t) |     |     | Ei(t)−E |     | (t−(cid:7)t) |
h is to ri c a l a v e ra g i ng m eth o d is s el e c ted w h e n c oh o rt s a m p l e s i z e s (cid:7)Ei = Ei(t) E i(t ∇Ei = dE i (t) ≈ i
,
ar e in s u ffi c ie n t ( N < 3 0 ) o r w h e n cu st o m e r b eh av i o r e x h i b i t s E i(t − (cid:7) t) d t (cid:7) t
c
| highstability(coefficientofvariationinmonthlyrevenue< |     |     |     |     |     |     |     |     |     |     |     |     |     | (8) |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.3).
|                   |     |                    |     |                 |     |       | where(cid:7)Ei | representstherelativechangeinengagement(growth |     |     |     |     |     |     |
| ----------------- | --- | ------------------ | --- | --------------- | --- | ----- | -------------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
| The probabilistic |     | model is preferred |     | when historical |     | churn | data           |                                                |     |     |     |     |     |     |
rate)and∇Eirepresentstheengagementvelocity(rateofchange).
(>
| is available | and | churn rates | are substantial |     | 15% | annually). |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thesederivativefeaturescapturewhethercustomerengagementis
Thecohort-basedmethodologyisemployedwhensufficientcohort
history exists (at least 12 cohorts with minimum 6 months of increasing,stable,ordeclining,whichisparticularlypredictivefor
|             |     |             |      |          |        |             | churn identification |     | where | declining | engagement |     | often | precedes |
| ----------- | --- | ----------- | ---- | -------- | ------ | ----------- | -------------------- | --- | ----- | --------- | ---------- | --- | ----- | -------- |
| observation | per | cohort) and | when | temporal | trends | in customer |                      |     |       |           |            |     |       |          |
customerattrition.Thetimedifference(cid:7)tistypicallysetto30days
behavioraredetected(significanttrendcoefficientsinregressionof
| cohortmetricsoncohortage,p<0.05). |     |     |     |     |     |     | formonthlytrendanalysis. |              |            |                |     |         |          |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | ------------ | ---------- | -------------- | --- | ------- | -------- | --- |
|                                   |     |     |     |     |     |     | These                    | mathematical |            | formulations   |     | for RFM | scoring, | CLV |
|                                   |     |     |     |     |     |     | projection,              | and          | engagement | quantification |     | are     | grounded | in  |
3.4.3 Engagementscoring established marketing analytics literature. The probabilistic CLV
|                |           |                 |           |             |         |            | model builds  | upon     | the seminal     |           | work of     | Fader | and Hardie       | on        |
| -------------- | --------- | --------------- | --------- | ----------- | ------- | ---------- | ------------- | -------- | --------------- | --------- | ----------- | ----- | ---------------- | --------- |
| For behavioral |           | data, the       | framework | constructs  |         | engagement |               |          |                 |           |             |       |                  |           |
|                |           |                 |           |             |         |            | probabilistic | customer | base            | analysis, |             | while | the cohort-based |           |
| scores that    | aggregate | multiple        |           | interaction | signals | such       | as            |          |                 |           |             |       |                  |           |
|                |           |                 |           |             |         |            | approach      | follows  | the methodology |           | established |       | in               | retention |
| email opens,   |           | website visits, | content   | downloads,  |         | support    |               |          |                 |           |             |       |                  |           |
ticket submissions, and social media interactions into unified cohortanalysis.Theengagementscoringframeworkincorporates
|             |                |        |          |         |            |            | principles | from     | multi-channel | attribution |            | models           | and behavioral |      |
| ----------- | -------------- | ------ | -------- | ------- | ---------- | ---------- | ---------- | -------- | ------------- | ----------- | ---------- | ---------------- | -------------- | ---- |
| metrics.    | The engagement |        | scoring  | model   | quantifies | customer   |            |          |               |             |            |                  |                |      |
|             |                |        |          |         |            |            | economics  | research | on recency    |             | effects in | decision-making. |                | This |
| interaction | intensity      | across | channels | through |            | a weighted |            |          |               |             |            |                  |                |      |
theoreticalfoundationensuresourautomatedfeatureengineering
temporalaggregation:
|     |     |     |     |     |     |     | procedures | capture | marketing-relevant |     |     | patterns |     | validated |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------------ | --- | --- | -------- | --- | --------- |
(cid:2)K (cid:2)W through decades of empirical research rather than implementing
|                                                     | Ei(t)= |     |       | (t−τ)·e | −λτ |     |                                                     |           |            |            |            |               |             |     |
| --------------------------------------------------- | ------ | --- | ----- | ------- | --- | --- | --------------------------------------------------- | --------- | ---------- | ---------- | ---------- | ------------- | ----------- | --- |
|                                                     |        | w   | I     |         |     |     | (6) ad-hocheuristics.                               |           |            |            |            |               |             |     |
|                                                     |        |     | k i,k |         |     |     |                                                     |           |            |            |            |               |             |     |
|                                                     |        | k=1 | τ=0   |         |     |     | TheLLMdetermineswhichfeatureengineeringoperationsto |           |            |            |            |               |             |     |
|                                                     |        |     |       |         |     |     | apply based                                         | on        | available  | data types | and        | the specified | prediction  |     |
| whereEi(t)istheengagementscoreforcustomeriattimet,K |        |     |       |         |     |     | is                                                  |           |            |            |            |               |             |     |
|                                                     |        |     |       |         |     |     | objective.                                          | For churn | prediction |            | tasks, the | framework     | prioritizes |     |
(t−τ)isanindicatorfunction
| thenumberofinteractiontypes,I |     |     | i,k |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
featuresthatcaptureengagementtrendsandrelationshipduration.
equalto1ifcustomerihadaninteractionoftypekattimet−τand
Forcampaignresponsemodeling,itemphasizesrecentbehavioral
| 0otherwise,W | isthetemporalwindowlength(typically90days), |     |     |     |     |     |          |                |          |     |          |         |            |      |
| ------------ | ------------------------------------------- | --- | --- | --- | --- | --- | -------- | -------------- | -------- | --- | -------- | ------- | ---------- | ---- |
|              |                                             |     |     |     |     |     | patterns | and historical | response |     | rates to | similar | campaigns. | This |
λ
| is the | temporal | decay rate | parameter, | and | w is the | weight | for                                                          |     |     |     |     |     |     |     |
| ------ | -------- | ---------- | ---------- | --- | -------- | ------ | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|        |          |            |            |     | k        |        | contextualadaptationensuresthatgeneratedfeaturesalignwiththe |     |     |     |     |     |     |     |
interactiontypek.
underlyingbusinessproblem.
| The | interaction | type weights |     | w k are estimated |     | based | on  |     |     |     |     |     |     |     |
| --- | ----------- | ------------ | --- | ----------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
univariatecorrelationwiththepredictiontarget,normalizedtosum
tounity:
|     |     |     |     |     |     |     | 3.5 Model |     | architecture |     | selection |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------ | --- | --------- | --- | --- | --- |
|ρ |
|     |     | w = | (cid:7) | k   |     |     | (7)      |            |             |     |            |        |          |           |
| --- | --- | --- | ------- | --- | --- | --- | -------- | ---------- | ----------- | --- | ---------- | ------ | -------- | --------- |
|     |     | k   | K       | |ρ| |     |     |          |            |             |     |            |        |          |           |
|     |     |     | j=1     | j   |     |     | The      | selection  | of machine  |     | learning   | models | for      | customer  |
|     |     |     |         |     |     |     | behavior | prediction | is informed |     | by several | key    | factors: | available |
(cid:7)
where ρ = corr( W I (t −τ),yi) is the Pearson correlation datatypes,thespecificpredictiontask,computationalconstraints,
| k   |     | τ=0 i,k |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
coefficient between the count of type-k interactions within the and interpretability needs. Our framework maintains a model
temporal window and the binary prediction target yi (e.g., repository indexed by compatible data modalities and task
churnindicator).Thisdata-drivenweightingschemeensuresthat types. Each model is characterized by a performance profile,
interaction types most predictive of customer behavior receive computationaldemands,andrecommendedapplicationscenarios.
appropriateemphasisinthecompositeengagementmetric. When selecting models, the framework employs a two-stage
λ
The temporal decay parameter controls how rapidly process. First, it filters the repository to identify architectures
the influence of past interactions diminishes. The framework compatible with the available data modalities and prediction
automaticallycalibratesλbyestimatingthemediantimebetween
|     |     |     |     |     |     |     | task. For | instance, | if the | dataset | contains | both | tabular | customer |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ------ | ------- | -------- | ---- | ------- | -------- |
consecutive interactions across all customers: λ = ln(2) where attributes and text fields from customer communications, the
t1 / 2
t1/2 = mediani,τ(si,τ+1 − si,τ) is the median inter-e v e nt time system retrieves models capable of processing these modality
computedfromthesortedsequenceofinteractiontimestampsfor combinations.Second,itanalyzesthefilteredcandidatestoselect
eachcustomer.Thiscalibrationensuresthehalf-lifeofinteraction the most appropriate architecture based on user directives and
influencealignswiththetypicalcustomerengagementcyclelength data characteristics. For tabular customer data, the repository
in the specific business context, preventing over-weighting of includes gradient boosting models well-suited to capturing
stale historical interactions or under-weighting of informative complex nonlinear relationships, neural architectures that can
recentpatterns. learn representations from high-dimensional features, and linear
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 07  |     |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Tianetal. |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |
| --------- | --- | --- | --- | --- | --- | ------------------------- | --- |
models that offer interpretability when business stakeholders 3.7 Training configuration optimization
| need to understand | factor | contributions. | For text data | such |     |     |     |
| ------------------ | ------ | -------------- | ------------- | ---- | --- | --- | --- |
as customer reviews or support tickets, the system accesses The final stage determines training hyperparameters and
pre-trained LLMs that can encode semantic content into optimization procedures. Rather than requiring users to specify
numerical representations. For temporal transaction sequences, learning rates, batch sizes, regularization strengths, and other
it includes recurrent architectures and temporal convolutional technicalparameters,theframeworkautomaticallyconfiguresthese
models that capture sequential dependencies. User directives settingsbasedondatasetcharacteristicsandmodelrequirements.
shape model selection through three primary channels. A The LLM analyzes the training configuration to pinpoint
directive for model interpretability, driven by compliance or hyperparameters that impact model performance. For neural
stakeholder needs, prioritizes architectures with transparent architectures, these include the learning rate, which governs
decision processes. A requirement for real-time prediction in optimizationstepsize;batchsize,whichinfluencestrainingstability
customer-facing applications selects computationally efficient and efficiency; and regularization parameters for overfitting
models. A specification of deployment targets, such as mobile or mitigation. For gradient boosting models, key hyperparameters
edgecomputingplatforms,guidesthechoicetowardarchitectures are tree depth, learning rate, and the number of estimators. For
withcompatibleresourceprofiles.Theselectionprocessgeneratesa each identified hyperparameter, the system defines appropriate
structuredconfigurationspecifyingthechosenmodelarchitecture, search ranges informed by the model architecture and dataset
its initialization parameters, and preprocessing requirements. scale.Theserangesareconstructedtoincludedefaultvalueswhile
This configuration serves as input to subsequent pipeline exploringvariationslikelytoimproveperformance.Theframework
constructionstages. canleverageexternaloptimizationlibrariestoconductautomated
hyperparametersearchwhencomputationalresourcespermit.
| 3.6 Pipeline | construction |     | and integration |         |                 |        |     |
| ------------ | ------------ | --- | --------------- | ------- | --------------- | ------ | --- |
|              |              |     |                 | 3.8 LLM | integration and | prompt |     |
engineering
| After selecting | appropriate    | models | for each data   | type,    |     |     |     |
| --------------- | -------------- | ------ | --------------- | -------- | --- | --- | --- |
| the framework   | must integrate | them   | into a cohesive | training |     |     |     |
pipeline. For datasets with multiple modalities, we employ a Large language models serve as intelligent controllers
late fusion strategy where specialized models process each data throughout the Marketing-AutoM3L framework, orchestrating
type independently before combining their outputs for final decisionsateachstageofpipelineconstructionthroughcarefully
predictions. Formally, let xi denote input data of modality i, and engineered prompt templates. This subsection documents the
modeli represent the selected architecture for that modality. The LLM integration architecture and prompt engineering strategies
framework first computes modality-specific representations fi = to ensure full reproducibility. The framework employs GPT-4
adapter (modeli(xi)),whereadapter projectstheoutputofmodeli accessed through the OpenAI API with temperature set to 0.1
| i   |     | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
intoacommondimensionalspace.Theserepresentationsarethen for deterministic outputs, maximum token limit of 2,048, and
concatenatedandprocessedbyfusioncomponents: exponential backoff retry logic (maximum three attempts) for
|                          |     |                |          | rate limiting. | Response validation    | mechanisms | verify outputs     |
| ------------------------ | --- | -------------- | -------- | -------------- | ---------------------- | ---------- | ------------------ |
|                          |     |                |          | conform        | to expected structured | formats,   | with clarification |
| =concat(f1,f2,...,fm),yˆ |     | =head(fusion(f |          |                |                        |            |                    |
| f combined               |     |                | combined | )). (9)        |                        |            |                    |
protocolsthatrequestadditionaldetailwhenambiguityisdetected
|     |     |     |     | (limited | to three clarification | rounds before | falling back to |
| --- | --- | --- | --- | -------- | ---------------------- | ------------- | --------------- |
The fusion component learns to combine information from conservativedefaults).Thedatamodalityrecognitionstageusesa
different modalities, while the head component produces final three-component prompt structure comprising system message,
predictions appropriate for the task, such as churn probabilities structuredinputdata,andoutputformatspecification.Thesystem
or estimated customer lifetime values. The pipeline construction messageestablishestheLLMasanexpertdataanalystspecializing
modulegeneratesexecutablecodeimplementingthisarchitecture. inmarketinganalytics.Theinputpresentscolumnnames,sample
TheLLMreceivesspecificationsforeachselectedmodelalongwith values,statisticalsummaries,anduser-providedbusinesscontext.
preprocessing requirements, then produces code that instantiates The output specification requires JSON-formatted responses
models, defines data flow, implements the fusion strategy, and mapping each column to a modality classification (numerical,
configures training procedures. This code generation approach categorical,temporal,text,oridentifier)withjustification.Figure2
providesflexibilitytoaccommodatevaryingnumbersofmodalities presents the complete prompt template, incorporating few-shot
and different model combinations without requiring predefined learning examples that demonstrate correct classification for
templatesforeverypossibleconfiguration.Thegeneratedpipeline attributeswithambiguousnamesorunconventionalformats.
includes data preprocessing components that apply appropriate The feature engineering stage integrates domain knowledge
transformations to each modality. Numerical features undergo anduserdirectivestoguidetransformationdecisions.Theprompt
normalizationorstandardizationasneeded.Categoricalvariables establishes the LLM as a marketing analytics expert familiar
areencodedusingtechniquessuitablefortheselectedmodel.Text with RFM analysis, customer lifetime value modeling, and
fieldsaretokenizedandprocessedthroughappropriateembedding engagementscoring.Theinputprovidesclassifieddatamodalities,
layers. The pipeline ensures that data flows correctly through all predictionobjectivesinnaturallanguage,anddomainknowledge
stagesfromrawinputstofinalpredictions. retrievedfromtheKnowledgeSupplementationModuleincluding
| FrontiersinArtificialIntelligence |     |     |     | 08  |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --------------- |

Tianetal. 10.3389/frai.2026.1726900
SystemMessage:Youareanexpertdataanalystspecializinginmarketinganalyticsandcustomerbehavior
datasets.Yourtaskistoanalyzedatasetattributesandclassifytheirdatatypesaccurately.
UserMessage:
Analyzethefollowingcustomerdatasetandclassifyeachattribute’sdatatype.
DatasetMetadata:
- Column Names: [CustomerID, Age, Gender, TotalSpend, LastPurchaseDate, NumTransactions,
PreferredCategory,EmailEngagement,ChurnLabel]
-SampleValues:
CustomerID:[C001,C002,C003,C004,C005]
Age:[34,45,28,52,39]
Gender:[M,F,F,M,F]
TotalSpend:[1250.50,890.20,2340.75,670.00,1890.40]
LastPurchaseDate:[2024-11-15,2024-10-22,2024-12-01,2024-09-18,2024-11-30]
NumTransactions:[12,8,24,5,15]
PreferredCategory:[Electronics,Clothing,Home,Electronics,Clothing]
EmailEngagement:[High,Low,Medium,Low,High]
ChurnLabel:[0,1,0,1,0]
BusinessContext:Thisdatasetisusedforpredictingcustomerchurninane-commerceplatform.
RequiredOutputFormat:ReturnaJSONobjectwiththefollowingstructure:
{”classifications”:[
{”column”:”columnname”,”type”:”modalitytype”,”justification”:”briefexplanation”},
...
]}
AvailableTypes:numerical,categorical,temporal,text,identifier
FIGURE2
Completeprompttemplatefordatamodalityrecognition,includingsystemmessage,structuredinputformat,andoutputspecification.
metric definitions, mathematical formulations, and task-specific approach ensures systematic consideration of all relevant factors
guidelines.Theoutputrequiresastructuredplandetailingfeatures whilereducingprematureconvergenceonsuboptimalchoices.
to construct, specific transformations, and executable Python Validation mechanisms ensure logical consistency across
code. Figure3 illustrates this template with a customer retention pipeline stages through schema checking for JSON structure
objective,wheretheLLMprioritizesrecency-basedfeatures,CLV compliance, semantic validation verifying transformations
projections, and engagement derivatives, providing mathematical reference existing columns, and consistency checking confirming
formulasandimplementationcodeforeachtransformation. stage compatibility. When inconsistencies are detected, the
Model selection prompts match data characteristics and validation-and-revision loop requests LLM corrections until all
business requirements to appropriate architectures. The componentsaremutuallycompatible.
prompt provides available modalities, dataset dimensions, All prompt templates, knowledge graph content, and
computational constraints, and business requirements such reasoning templates are maintained in a version-controlled
as interpretability needs or deployment constraints. The repository with comprehensive documentation of development
LLM evaluates candidates from the architecture repository decisions, A/B testing results, and extension guidelines for new
based on compatibility with these factors, returning selected domains. This infrastructure enables precise reproduction of our
architectures with initialization parameters, preprocessing experimental setup and understanding of how large language
requirements,andjustificationaddressingallspecifiedconstraints. modelscontributetoautomatedpipelineconstructionthroughout
The Knowledge Supplementation Module provides domain theMarketing-AutoM3Lframework.
expertise through a hierarchical knowledge graph containing
approximately 150 nodes organized into customer segmentation
methodologies, behavioral prediction frameworks, feature
4 Experiments
engineering techniques, model architecture families, and
evaluation metrics. When domain knowledge is required, a
retrievalmechanismusingsentenceembeddings(all-MiniLM-L6- The experimental evaluation is designed to validate our
v2model)measurescosinesimilaritybetweendecisioncontextand framework’s three primary contributions: first, that domain-
node descriptions, selecting the top five most relevant nodes for specific feature engineering significantly improves prediction
promptinclusion. accuracy over generic AutoML approaches; second, that LLM-
The module implements chain-of-thought reasoning through driven pipeline automation substantially reduces development
structured templates that decompose complex decisions into time while maintaining or improving model performance;
sequential sub-problems with clear evaluation criteria. Figure4 and third, that natural language interfaces enable practical
presentsthemodelselectionreasoningtemplate,whichbreaksthe deployment for business stakeholders without machine learning
decisionintofivesteps:datacharacteristicanalysis,computational expertise. Our experiments evaluate each contribution through
resource assessment, business requirement analysis, architecture comparative studies, ablation analyses, and computational
repository filtering, and candidate ranking. This structured efficiencymeasurements.
FrontiersinArtificialIntelligence 09 frontiersin.org

Tianetal. 10.3389/frai.2026.1726900
SystemMessage:Youareanexpertinmarketinganalyticsfeatureengineering,specializingincustomer
behaviorprediction.YouarefamiliarwithRFManalysis,customerlifetimevaluemodeling,engagement
scoring,andotherdomain-specificmethodologies.
UserMessage:
Designdomain-specificfeaturesforthefollowingcustomeranalyticstask.
DataModalitiesIdentified:
-Numerical:Age,TotalSpend,NumTransactions
-Categorical:Gender,PreferredCategory,EmailEngagement
-Temporal:LastPurchaseDate
-Target:ChurnLabel
PredictionObjective:Maximizeaccuracyforcustomerchurnpredictionwithemphasisonearlyidentification
ofat-riskcustomers.
DomainKnowledge:
-RFMAnalysis:ComputeRecency(dayssincelastpurchase),Frequency(transactioncount),andMonetary
value(totaloraveragespend)
-CustomerLifetimeValue:Projectfuturevaluebasedonhistoricalpatterns:CLV=(AverageOrderValue)×
(PurchaseFrequency)×(CustomerLifespan)
-EngagementTrends:Calculaterateofchangeinengagementmetricsovertimewindows
RequiredOutput:ReturnaJSONobjectspecifying:
1.Featurestoconstructwithjustification
2.Transformationdetailsincludingformulas
3.Pythoncodesnippetsforimplementation
OutputFormat:
{”featureengineeringplan”:[
{”featurename”:”name”,”type”:”RFM—CLV—engagement—aggregation”,
”justification”:”whythisfeaturehelpswiththeobjective”,
”formula”:”mathematicaldefinition”,
”requiredcolumns”:[”col1”,”col2”],
”code”:”executablePythoncode”},
...
]}
FIGURE3
Prompttemplatefordomain-awarefeatureengineering,showinghowuserobjectivesanddomainknowledgeguidetransformationdecisions.
Chain-of-ThoughtReasoningTemplateforModelSelection
Step1-DataCharacteristicAnalysis:
Questions:Whatdatamodalitiesarepresent?Whatisthedatasetsize?Arethereclassimbalanceissues?Is
theretemporaldependency?
Output:Structuredsummaryofdatacharacteristicsconstrainingmodelchoices.
Step2-ComputationalResourceAssessment:
Questions: Whatcomputationalresourcesareavailablefortraining? Whatarelatencyrequirementsfor
inference?Aretherememoryconstraints?
Output:Resourceconstraintspecification.
Step3-BusinessRequirementAnalysis:
Questions:Ismodelinterpretabilityrequired?Whatisthetoleranceforfalsepositivesversusfalsenegatives?
Aretheredeploymentconstraints?
Output:Businessrequirementspecificationwithpriorityordering.
Step4-ArchitectureRepositoryFiltering:
Action: Filtermodelrepositorytoarchitecturescompatiblewithdatacharacteristicsandcomputational
constraints.
Output:Listofcandidatearchitectureswithcompatibilityjustification.
Step5-CandidateRankingandSelection:
Action: Rankcandidatesbasedonexpectedperformance, businessrequirementalignment, andtraining
efficiency.
Output:Selectedarchitecturewithdetailedjustification.
FIGURE4
Chain-of-thoughtreasoningtemplateformodelselection,showingstructureddecisiondecompositionguidingLLMreasoning.
4.1 Implementation details our experimental evaluation employed high-end NVIDIA A100
GPUs and Apache Spark distributed computing infrastructure
The Marketing-AutoM3L framework was implemented using to efficiently process the largest datasets in our benchmark suite,
Python 3.8 with PyTorch 1.12 as the deep learning backend. these resources are not requirements for framework deployment
The system operates on a distributed computing cluster with in typical business environments. To assess infrastructure
NVIDIA A100 GPUs for model training and CPU-based Intel scalabilityandpracticaldeploymentcosts,weconductedadditional
Xeonprocessorsfordatapreprocessingtasks.TheLLMcomponent experimentsrunningtheframeworkonstandardcloudcomputing
utilizes GPT-4 through OpenAI’s API with temperature set to instances with consumer-grade GPUs (NVIDIA T4 and RTX
0.1 for consistent decision-making across experiments. While 4000).Theseexperimentsdemonstratedthatpipelineconstruction
FrontiersinArtificialIntelligence 10 frontiersin.org

Tianetal. 10.3389/frai.2026.1726900
timesincreasedbyonlythirtypercentcomparedtoourA100-based areconsistentacrossmethodstoevaluatepracticalapplicabilityin
setup, resulting in average completion times of approximately businessenvironments.
thirty minutes rather than twenty-three minutes. This modest
performance degradation maintains substantial efficiency
advantages over manual approaches while dramatically reducing 4.3 Datasets
infrastructure costs. Cloud-based execution on medium-tier
GPU instances costs approximately two dollars per pipeline in Our experimental evaluation uses five diverse customer
compute time, bringing total per-pipeline costs including GPT-4 analyticsdatasetsrepresentingdifferentbusinessscenariosanddata
API usage to approximately ten dollars while maintaining net characteristics,asdetailedinTable1.
savings exceeding three hundred dollars compared to manual The Telco Customer Churn dataset1 originates from IBM’s
development requiring 156.9 minutes of data scientist time. sample datasets and is available through Kaggle, representing
Organizations without access to high-end GPU infrastructure a telecommunications provider serving over 7,000 customers
can therefore deploy the framework effectively on commodity in California. Features include service usage patterns, contract
hardwareoraffordablecloudinstances,acceptingminorincreases details,billinginformation,andcustomersupportinteractions.The
inexecutiontimetominimizecapitalinvestmentwhilepreserving datasetcontainsmixedmodalitieswithnumericalservicemetrics
the core automation benefits. Data preprocessing pipelines are andcategoricalservicetypes.BankCustomerChurn2 represents
parallelizedusingApacheSpark3.2tohandlelarge-scalecustomer a European financial institution with approximately 10,000
datasets.Theframeworkincorporatesautomatedhyperparameter customer records. This dataset captures customer demographics,
optimization through Bayesian optimization with 50 iterations account balances, product usage, and transaction histories.
maximum per model. Feature engineering operations are cached The relatively low churn rate reflects typical banking industry
to reduce computational overhead in repeated experiments. retention patterns. E-commerce Customer data3 comes from an
The modality recognition component processes tabular data, online retail platform tracking customer purchasing behavior,
text fields, and temporal sequences using specialized encoders. website interactions, and product preferences. The dataset
Text processing employs BERT-base-uncased for semantic comprises 5,634 customer records with 20 attributes including
understanding,whilenumericalfeaturesundergostandardization tenure, preferred login device, city tier, warehouse-to-home
and categorical variables receive target encoding. Temporal distance,satisfactionscore,andorderpatterns.Thehigherchurn
sequencesareprocessedusingslidingwindowswithconfigurable rateindicatesthecompetitivenatureofe-commerceenvironments
time steps. Model selection considers computational constraints wherecustomersfrequentlyswitchbetweenplatforms.Insurance
with a maximum training time of 2 h per experiment. The Churn4 encompasses customer data from an insurance services
frameworkmaintainsaregistryof15basearchitecturesincluding company, including policy details, claims history, and customer
gradient boosting variants, neural networks, and ensemble service interactions. The dataset contains 9,134 records with 16
methods.PipelineconstructiongeneratesexecutablePythoncode distinguishing factors designed specifically for churn prediction
thatisvalidatedthroughstaticanalysisbeforeexecution. modelingintheinsuranceindustry.Thedatasetprovidesinsights
intolong-termcustomerrelationshipstypicalininsurancemarkets.
Marketing Campaign Response5 represents the largest dataset
with over 41,000 records from direct marketing initiatives
conducted by a Portuguese banking institution. This dataset
4.2 Compared methods
combines demographic information, campaign exposure history,
andresponsepatternsacrossmultiplechannelsandtimeperiods.
We compare Marketing-AutoM3L against several state-
We employed stratified random splitting to maintain class
of-the-art AutoML frameworks and traditional approaches.
distributionacrossallsplits,whichisparticularlyimportantgiven
AutoM3Lservesasourprimarybaseline,representingthegeneral-
the class imbalance present in churn prediction datasets (churn
purposemultimodalAutoMLframeworkwithoutdomain-specific
rates ranging from 11.3% to 32.1% across our five datasets).
customizations for marketing analytics. TPOT (Tree-based
Specifically,weallocated70%ofeachdatasetfortraining,15%for
Pipeline Optimization Tool) provides automated pipeline
validation (used for hyperparameter tuning and early stopping),
construction using genetic programming to evolve machine
and 15% for final testing, with stratification based on the binary
learningpipelines.AutoGluonfromAmazonWebServicesoffers
churnlabeltoensureproportionalrepresentationofbothchurned
tabularpredictioncapabilitieswithautomaticmodelstackingand
ensemblegeneration.GoogleAutoMLthroughVertexAIprovides
cloud-basedautomatedmachinelearningwithneuralarchitecture 1 https://www.kaggle.com/datasets/blastchar/telco-customer-churn
search capabilities. The Manual ML Pipeline baseline represents 2 https://www.kaggle.com/datasets/murilozangari/customer-churn-
traditional data science workflows where practitioners manually from-a-bank and https://mavenanalytics.io/data-playground/bank-
designfeatures,selectmodels,andtunehyperparametersbasedon customer-churn
domainknowledge. 3 https://www.kaggle.com/datasets/samuelsemaya/e-commerce-
Each baseline method receives identical preprocessed customer-churn
datasets to ensure fair comparison. We disable method-specific 4 https://www.kaggle.com/datasets/k123vinod/insurance-churn-
optimizationsthatcouldprovideunfairadvantagesandstandardize prediction-weekend-hackathon
evaluationproceduresacrossallapproaches.Trainingtimelimits 5 https://archive.ics.uci.edu/dataset/222/bank+marketing
FrontiersinArtificialIntelligence 11 frontiersin.org

| Tianetal. |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
TABLE1 Datasetcharacteristicsandbusinesscontextsforexperimentalevaluation.
Dataset Samples Features Churnrate Modalities Businesscontext
Telcocustomerchurn 7,043 21 26.5% Tabular,text Telecommunicationsserviceprovider
Bankcustomerchurn 10,000 14 20.4% Tabular,demographics Europeanbankinginstitution
E-commercecustomer 5,634 18 32.1% Tabular,behavioral Onlineretailplatform
Insurancechurn 9,134 16 15.7% Tabular,claims Insuranceservicescompany
Marketingcampaignresponse 41,188 23 11.3% Tabular,text,temporal Directmarketingcampaigns
and non-churned customers in each subset. We fixed random model’s sensitivityto churn events. F1-Scoreprovides abalanced
seeds(seed=42)acrossallexperimentstoensurereproducibility assessment by combining precision and recall into a single
andenablefaircomparisonacrossdifferentmethods.Fordatasets metric.Accuracyrepresentsoverallpredictioncorrectnessacrossall
withtemporaldependencies(TelcoCustomerChurn,E-commerce customerclassifications.
Customer,InsuranceChurn,andMarketingCampaignResponse), Beyond traditional metrics, we evaluate computational
we implement chronological train-test splits where the training efficiency through execution time measurements and model
set comprises customer observations from the earliest 70% of complexity analysis. Business impact assessment considers false
the temporal range and the test set contains observations from positivecostsassociatedwithunnecessaryretentioninterventions
the most recent 30%, maintaining strict temporal ordering to and false negative costs from missed churn events. We report
preventinformationleakage.Foralltemporalfeatureengineering confidenceintervalsusingbootstrapsamplingwith1,000iterations
operations, we enforce temporal constraints ensuring that toassessstatisticalsignificanceofperformancedifferences.
| RFM recency        | calculations, | CLV             | projections |               | based on           | historical |             |          |               |     |             |     |             |
| ------------------ | ------------- | --------------- | ----------- | ------------- | ------------------ | ---------- | ----------- | -------- | ------------- | --- | ----------- | --- | ----------- |
| transaction        | patterns,     | and             | engagement  |               | score computations |            |             |          |               |     |             |     |             |
| only utilize       | data          | from periods    | strictly    | before        | each               | customer’s |             |          |               |     |             |     |             |
| prediction         | timestamp.    | The             | framework’s |               | automated          | pipeline   |             |          |               |     |             |     |             |
|                    |               |                 |             |               |                    |            | 4.5 Results |          |               |     |             |     |             |
| generation         | includes      | temporal        | validation  | checks        | that               | verify no  |             |          |               |     |             |     |             |
| future information |               | is incorporated |             | into training | features,          | with       |             |          |               |     |             |     |             |
|                    |               |                 |             |               |                    |            | Table2      | presents | comprehensive |     | performance |     | comparisons |
theseconstraintsautomaticallyenforcedthroughtheLLM-driven
code generation process that produces temporally-aware data acrossalldatasetsandmethods.Marketing-AutoM3Ldemonstrates
preprocessingpipelines. consistent superiority over baseline approaches, achieving the
|                |     |              |          |            |          |     | highest ROC-AUC |     | scores | on all | five datasets | with | improvements |
| -------------- | --- | ------------ | -------- | ---------- | -------- | --- | --------------- | --- | ------ | ------ | ------------- | ---- | ------------ |
| All prediction |     | tasks employ | explicit | prediction | horizons | to  |                 |     |        |        |               |      |              |
define the target variable: churn labels are defined as customer rangingfrom1.4%to5.4%overthestrongestbaseline.
TheBankCustomerChurndatasetyieldsthehighestabsolute
| attrition occurring |     | within 90 | days | after the | observation | cutoff |     |     |     |     |     |     |     |
| ------------------- | --- | --------- | ---- | --------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
date for Telco and Bank datasets, 60 days for E-commerce and performance across all methods, with Marketing-AutoM3L
Insurancedatasets,and30daysforMarketingCampaignResponse. achieving 0.941 ROC-AUC. This superior performance stems
|                     |     |         |          |     |                    |     | from the | dataset’s | well-structured |     | customer | attributes | and clear |
| ------------------- | --- | ------- | -------- | --- | ------------------ | --- | -------- | --------- | --------------- | --- | -------- | ---------- | --------- |
| Feature computation |     | windows | strictly | end | at the observation |     |          |           |                 |     |          |            |           |
cutoff date, ensuring a temporal gap between the last feature behavioral patterns that the domain-specific feature engineering
|     |     |     |     |     |     |     | effectively | captures. | Conversely, |     | E-commerce | Customer | data |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ----------- | --- | ---------- | -------- | ---- |
observationandtheearliestpossibletargetevent.Forexample,if
the observation cutoff is day T, all features (RFM metrics, CLV presents the most challenging prediction task due to the highly
projections,andengagementscores)arecomputedusingonlydata dynamic nature of online customer behavior and shorter
|     |     |     |     |     |     |     | engagement | cycles. | The | experimental | results | demonstrate | the |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --- | ------------ | ------- | ----------- | --- |
fromperiodsendingatorbeforedayT,whilechurnlabelsindicate
events occurring between day T+1 and day T+H where H is the effectiveness of our proposed framework across all evaluation
|     |     |     |     |     |     |     | metrics. As | shown | in Figure5, |     | Marketing-AutoM3L |     | consistently |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----------- | --- | ----------------- | --- | ------------ |
predictionhorizon.
|     |     |     |     |     |     |     | outperforms | baseline | methods | in  | terms of | ROC-AUC, | F1-Score, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ------- | --- | -------- | -------- | --------- |
Precision,andRecallacrossallfivedatasets.Statisticalsignificance
|                |     |         |     |     |     |     | testing using | paired | t-tests           | confirms | that            | Marketing-AutoM3L’s |             |
| -------------- | --- | ------- | --- | --- | --- | --- | ------------- | ------ | ----------------- | -------- | --------------- | ------------------- | ----------- |
| 4.4 Evaluation |     | metrics |     |     |     |     |               |        |                   |          |                 |                     |             |
|                |     |         |     |     |     |     | improvements  | over   | baseline          | methods  | exceed          | random              | variation   |
|                |     |         |     |     |     |     | (p < 0.05     | for    | all comparisons). |          | The framework’s |                     | performance |
We employ standard classification metrics to assess model gains are most pronounced on datasets with diverse feature
performanceacrossdifferentaspectsofpredictionquality.Receiver types, demonstrating the effectiveness of multimodal processing
OperatingCharacteristicAreaUnderCurve(ROC-AUC)servesas capabilities. The practical implications of these performance
our primary evaluation metric, measuring the model’s ability to differences merit careful consideration. The 5.4% improvement
distinguishbetweenchurningandnon-churningcustomersacross on the E-commerce Customer dataset translates to identifying
allclassificationthresholds.Precisionquantifiestheproportionof approximately 380 additional at-risk customers in a base of
predictedchurnerswhoactuallychurn,directlyrelatingtoresource 10,000, enabling proactive retention interventions that could
allocation efficiency in retention campaigns. Recall measures the preventsubstantialrevenueloss.FortheBankingdataset,the1.6%
fraction of actual churners correctly identified, indicating the improvement over the next-best automated method (AutoM3L)
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 12  |     |     |     |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Tianetal. |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |
| --------- | --- | --- | --- | --- | --- | ------------------------- | --- |
TABLE2 MainexperimentalresultscomparingMarketing-AutoM3Lagainstbaselinemethods,includingcomprehensiveperformancemetricsand
statisticalsignificance.
|        | Telcocustomerchurn |            | Bankcustomerchurn |            | E-commercecustomer |       |      |
| ------ | ------------------ | ---------- | ----------------- | ---------- | ------------------ | ----- | ---- |
| Method | AUC F1             | Prec. Rec. | AUC F1            | Prec. Rec. | AUC F1             | Prec. | Rec. |
Marketing-AutoM3L 0.923∗∗∗ 0.847 0.862 0.833 0.941∗∗∗ 0.863 0.879 0.848 0.867∗∗∗ 0.791 0.805 0.778
AutoM3L 0.908 0.832 0.847 0.818 0.925 0.849 0.864 0.835 0.851 0.776 0.789 0.764
TPOT 0.895 0.819 0.834 0.805 0.912 0.836 0.851 0.822 0.843 0.761 0.781 0.743
AutoGluon 0.901 0.826 0.843 0.810 0.918 0.842 0.857 0.828 0.847 0.765 0.785 0.746
GoogleAutoML 0.889 0.811 0.826 0.797 0.904 0.828 0.843 0.814 0.834 0.752 0.773 0.732
ManualMLpipeline 0.876 0.798 0.813 0.784 0.891 0.815 0.830 0.801 0.821 0.738 0.758 0.719
|     | Insurancechurn |     | Marketingcampaign |     | Avg.improvement |     |     |
| --- | -------------- | --- | ----------------- | --- | --------------- | --- | --- |
(cid:7)AUC (cid:7)F1
| Method | AUC F1 | Prec. Rec. | AUC F1 | Prec. Rec. |     | Time(min) | Speedup |
| ------ | ------ | ---------- | ------ | ---------- | --- | --------- | ------- |
Marketing-AutoM3L 0.912∗∗∗ 0.834 0.849 0.820 0.889∗∗∗ 0.813 0.827 0.800 – – 23.4 6.7×
AutoM3L 0.897 0.819 0.834 0.805 0.873 0.797 0.811 0.784 +1.6% +1.7% 31.7 4.9×
TPOT 0.884 0.806 0.821 0.792 0.861 0.785 0.799 0.772 +2.9% +3.1% 89.2 1.8×
3.4×
AutoGluon 0.888 0.810 0.827 0.794 0.865 0.789 0.803 0.776 +2.3% +2.5% 45.6
2.3×
GoogleAutoML 0.875 0.797 0.813 0.782 0.852 0.776 0.790 0.763 +3.6% +3.8% 67.3
ManualMLPipeline 0.863 0.785 0.800 0.771 0.839 0.763 0.777 0.750 +4.9% +5.2% 156.9 –
∗∗∗p<0.001comparedtobestbaseline(pairedt-test).Avg.Improvementshowsmeangainsovereachbaselinemethod.
Timemeasurementsrepresentaveragepipelineconstructionandtrainingtime.SpeedupcalculatedrelativetoManualMLPipeline.Theboldvaluesrepresentthebestperformanceofeach
metric.
FIGURE5
PerformancecomparisonacrossdatasetsandmethodsshowingROC-AUC,F1-Score,Precision,andRecallmetrics.
| FrontiersinArtificialIntelligence |     |     | 13  |     |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --------------- |

Tianetal. 10.3389/frai.2026.1726900
TABLE3 Performancewhenbaselinemethodsreceivepre-computeddomainfeatures.
Method Inputconfiguration Telco Bank E-comm Insurance Marketing
ROC-AUC ROC-AUC ROC-AUC ROC-AUC ROC-AUC
Baselinemethodswithpre-computeddomainfeatures
AutoM3L+features Raw+RFM+CLV+Eng 0.915 0.933 0.859 0.904 0.881
TPOT+features Raw+RFM+CLV+Eng 0.906 0.922 0.853 0.896 0.873
AutoGluon+features Raw+RFM+CLV+Eng 0.911 0.928 0.856 0.899 0.877
GoogleAutoML+features Raw+RFM+CLV+Eng 0.902 0.918 0.847 0.891 0.868
ManualML+features Raw+RFM+CLV+Eng 0.897 0.913 0.841 0.885 0.862
Marketing-AutoM3L(autonomousfeaturegeneration)
Marketing-AutoM3L Rawdataonly 0.923 0.941 0.867 0.912 0.889
Performanceadvantageofmarketing-AutoM3L
vs.AutoM3L+features (cid:7)ROC-AUC +0.008(+0.9%) +0.008(+0.9%) +0.008(+0.9%) +0.008(+0.9%) +0.008(+0.9%)
vs.TPOT+features (cid:7)ROC-AUC +0.017(+1.9%) +0.019(+2.1%) +0.014(+1.6%) +0.016(+1.8%) +0.016(+1.8%)
vs.AutoGluon+features (cid:7)ROC-AUC +0.012(+1.3%) +0.013(+1.4%) +0.011(+1.3%) +0.013(+1.4%) +0.012(+1.4%)
vs.GoogleAutoML+features (cid:7)ROC-AUC +0.021(+2.3%) +0.023(+2.5%) +0.020(+2.4%) +0.021(+2.4%) +0.021(+2.4%)
vs.ManualML+features (cid:7)ROC-AUC +0.026(+2.9%) +0.028(+3.1%) +0.026(+3.1%) +0.027(+3.1%) +0.027(+3.1%)
AllbaselinesreceiverawdataPLUSpre-computedRFMscores,CLVprojections,andengagementmetricsasadditionalinputcolumns.Marketing-AutoM3Lgeneratesthesefeatures
autonomously.Resultsdemonstratethatourframework’sintelligentpipelineconstructionprovidesvaluebeyondfeatureengineeringalone.
Pre-computedfeaturesprovidedtobaselines:RFM_Recency,RFM_Frequency,RFM_Monetary,RFM_Score.
CLV_Projection,Engagement_Score,Engagement_Trend.Performanceadvantagesrangefrom0.8%to2.1%.
demonstratingthatMarketing-AutoM3L’sintelligentpipelineconstructionprovidesvaluebeyondfeatureengineering.Theboldvaluesrepresentthebestperformanceofeachmetric.
representsapproximately160customersper10,000,whichinhigh- that AutoM3L augmented with pre-computed features achieves
value banking contexts can correspond to millions of dollars in 0.915 ROC-AUC on the Telco dataset compared to Marketing-
retainedcustomerlifetimevalue.Theconsistencyofimprovements AutoM3L’s 0.923 is particularly revealing—despite having
across diverse business contexts—telecommunications, banking, access to identical domain features, the generic multimodal
e-commerce,insurance,andmarketingcampaigns—demonstrates frameworkcannotmatchourdomain-awarepipelineconstruction,
the generalizability of our domain-aware automation approach confirming that intelligent integration of marketing knowledge
ratherthanperformancegainslimitedtospecificindustryverticals. throughouttheautomationprocessprovidesgenuinevaluebeyond
To address potential concerns that our performance gains featureavailability.
mightderivesolelyfromthepresenceofdomain-specificfeatures Table4 provides comprehensive metric analysis across all
rather than intelligent pipeline construction, we conducted a datasets, revealing that Marketing-AutoM3L maintains balanced
comparison where all baseline methods receive pre-computed performance across precision and recall while achieving the
domain features (RFM scores, CLV projections, and engagement highestF1-scores.
metrics) as additional input columns alongside raw customer Computational efficiency analysis reveals that Marketing-
data, while Marketing-AutoM3L continues to generate these AutoM3Lrequiresanaverageof23.4minutesforcompletepipeline
features autonomously. Table3 presents the results of this constructionandtraining,representinga6.7×speedupcompared
configuration, which tests whether baseline AutoML systems can to manual approaches and 2.9× improvement over generic
effectivelyexploitdomainfeatureswhenprovided,orwhetherour AutoML methods. This efficiency stems from the framework’s
framework’s LLM-driven integration provides additional value intelligentcachingmechanismsanddomain-specificoptimizations
beyond feature engineering alone. The results demonstrate that that reduce the search space for hyperparameter optimization.
even when baseline methods have direct access to pre-computed The ROC-AUC performance comparison, presented in Figure6,
domain features, Marketing-AutoM3L maintains statistically demonstratesMarketing-AutoM3L’ssuperiorpredictivecapability
significant performance advantages ranging from 0.8% to 2.1% acrossallcustomeranalyticsdatasets.Ourframeworkconsistently
in ROC-AUC across all datasets (p < 0.01 for all comparisons). achieves higher AUC scores compared to baseline methods,
Thesepersistentperformancegainsindicatethatourframework’s indicatingbetteroverallclassificationperformance.
value extends beyond simply computing marketing-relevant Therelationshipbetweenmodelcomplexityandperformance,
features to encompass intelligent model selection that matches illustratedinthecomplexityanalysis,demonstratesthatMarketing-
architectures to data characteristics, sophisticated multimodal AutoM3Lachievesoptimalperformancewithmoderateparameter
fusion strategies that optimally combine heterogeneous feature counts. This efficiency indicates that domain-specific feature
types, and contextual hyperparameter optimization guided by engineeringreducestheneedforcomplexmodelarchitecturesto
business objectives specified in natural language. The finding capturerelevantpatterns.
FrontiersinArtificialIntelligence 14 frontiersin.org

| Tianetal. |     |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |
| --------- | --- | --- | --- | --- | --- | --- | ------------------------- | --- |
TABLE4 DetailedperformancemetricsforMarketing-AutoM3Lacrossalldatasets.
| Dataset |     | ROC-AUC | F1-score |     | Precision | Recall | Accuracy | 95%CI |
| ------- | --- | ------- | -------- | --- | --------- | ------ | -------- | ----- |
Telcocustomerchurn 0.923 0.847 0.862 0.833 0.891 [0.917,0.929]
Bankcustomerchurn 0.941 0.863 0.879 0.848 0.905 [0.935,0.947]
E-commercecustomer 0.867 0.791 0.805 0.778 0.834 [0.859,0.875]
| Insurancechurn |     | 0.912 |     | 0.834 | 0.849 | 0.820 | 0.878 | [0.905,0.919] |
| -------------- | --- | ----- | --- | ----- | ----- | ----- | ----- | ------------- |
Marketingcampaignresponse 0.889 0.813 0.827 0.800 0.856 [0.882,0.896]
FIGURE6
ROC-AUCperformancecomparisonshowingMarketing-AutoM3L’ssuperiorperformanceacrossdifferentcustomeranalyticsdatasets.
Feature importance analysis reveals that RFM (Recency, essential for achieving superior predictive accuracy in customer
| Frequency,  | and Monetary)         | features             | dominate     | prediction      | analyticstasks. |     |     |     |
| ----------- | --------------------- | -------------------- | ------------ | --------------- | --------------- | --- | --- | --- |
| performance | across all            | datasets, validating |              | the framework’s |                 |     |     |     |
| emphasis    | on marketing-specific | feature              | engineering. | Recency         |                 |     |     |     |
measuresconsistentlyrankasthemostpredictivefeatures,followed
|     |     |     |     |     | 4.6 Ablation | study |     |     |
| --- | --- | --- | --- | --- | ------------ | ----- | --- | --- |
bymonetaryvaluecalculationsandtransactionfrequencypatterns.
| The computational | efficiency | of our | framework | is evaluated |     |     |     |     |
| ----------------- | ---------- | ------ | --------- | ------------ | --- | --- | --- | --- |
through execution time analysis. As demonstrated in Figure7, We conduct comprehensive ablation studies to quantify the
Marketing-AutoM3L achieves significant speed improvements contribution of each framework component. Table5 presents the
compared to traditional manual pipeline development and progressiveperformanceimprovementsascomponentsareadded
other automated methods, while maintaining competitive toabaselineimplementation.
predictiveperformance. Data Recognition contributes substantial improvements
These results directly validate the core premise of our (3.6%–4.5% ROC-AUC increase) by correctly identifying feature
title: that domain-aware automation specifically designed for types and applying appropriate preprocessing. This component
financial customer analytics outperforms generic approaches. prevents common errors such as treating categorical identifiers
Theconsistentperformancegainsacrossalldatasetsdemonstrate as numerical features or failing to recognize temporal patterns
that incorporating marketing domain knowledge—through in transaction data. Feature Engineering provides the largest
RFM analysis, CLV calculations, and engagement scoring—is individualcontribution(3.3%–3.6%improvement),confirmingthe
| FrontiersinArtificialIntelligence |     |     |     |     | 15  |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Tianetal. |     |     |     |     |     | 10.3389/frai.2026.1726900 |
| --------- | --- | --- | --- | --- | --- | ------------------------- |
FIGURE7
ExecutiontimecomparisonshowingMarketing-AutoM3L’scomputationalefficiencyrelativetobaselinemethods.
TABLE5 Ablationstudyresultsshowingindividualcomponentcontributionstooverallperformance.
| Configuration          |     | Telco | Bank  | E-commerce | Insurance | Marketing |
| ---------------------- | --- | ----- | ----- | ---------- | --------- | --------- |
| Baseline(nocomponents) |     | 0.798 | 0.812 | 0.745      | 0.787     | 0.763     |
| Datarecognition        |     | 0.834 | 0.849 | 0.781      | 0.823     | 0.798     |
| Featureengineering     |     | 0.867 | 0.882 | 0.814      | 0.856     | 0.831     |
| Modelselection         |     | 0.891 | 0.906 | 0.838      | 0.880     | 0.855     |
| Pipelineconstruction   |     | 0.908 | 0.925 | 0.852      | 0.897     | 0.872     |
| Fullframework          |     | 0.923 | 0.941 | 0.867      | 0.912     | 0.889     |
Theboldvaluesrepresentthebestperformanceofeachmetric.
importanceofdomain-specifictransformations.RFMcalculations, Marketing-AutoM3L consistently identifies an optimal operating
customer lifetime value estimations, and engagement scoring point, achieving high accuracy without unnecessary complexity,
createpredictivefeaturesthatcapturemarketing-relevantpatterns unlike baseline methods which tend toward either underfitting
| not apparent | in raw data. | Model Selection | adds 2.4%–2.8% | oroverfitting. |     |     |
| ------------ | ------------ | --------------- | -------------- | -------------- | --- | --- |
improvement by choosing architectures appropriate for each Multimodal integration provides consistent improvements
modality and prediction task. The LLM-based selection process over single-modality approaches, with gains ranging from
considers data characteristics, computational constraints, and 1.1% to 3.6% ROC-AUC. Text modalities contribute
user requirements to identify optimal modeling approaches. particularly valuable insights for telecommunications and
Pipeline Construction contributes 1.7%–1.9% through effective marketing datasets where customer communications provide
multimodal fusion strategies and automated code generation. sentiment and intent signals. Temporal patterns prove
Late fusion approaches allow specialized processing for each essential for e-commerce and marketing scenarios where
modality while maintaining coherent integration for final seasonal effects and purchasing cycles influence churn
predictions. Table6 examines the impact of different data behavior. To validate the consistency of our complexity-
modalities on prediction performance, demonstrating that performance optimization, we conducted additional ablation
multimodal approaches consistently outperform single-modality studies. As corroborated by Figure9, Marketing-AutoM3L
baselines. Figure8 analyzes the critical trade-off between maintains its ability to identify the optimal trade-off point
model complexity and predictive performance. It shows that even under varying dataset conditions and architectural
| FrontiersinArtificialIntelligence |     |     |     | 16  |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --------------- |

| Tianetal. |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
TABLE6 Modalityablationstudyshowingthecontributionofdifferent like Llama 3.1 70B demonstrate feasible migration paths
datatypes.
|          |       |      |            |           | with accuracy |     | decreases   | limited         | to  | one | to two       | percent. |
| -------- | ----- | ---- | ---------- | --------- | ------------- | --- | ----------- | --------------- | --- | --- | ------------ | -------- |
|          |       |      |            |           | Organizations |     | with strong | reproducibility |     |     | requirements | can      |
| Modality | Telco | Bank | E-commerce | Marketing |               |     |             |                 |     |     |              |          |
combination
|             |       |       |       |       | deploy open-source |              | language    | models       |     | locally,    | accepting    | modest |
| ----------- | ----- | ----- | ----- | ----- | ------------------ | ------------ | ----------- | ------------ | --- | ----------- | ------------ | ------ |
|             |       |       |       |       | performance        | trade-offs   |             | to eliminate |     | proprietary | dependencies |        |
| Tabularonly | 0.887 | 0.923 | 0.841 | 0.862 |                    |              |             |              |     |             |              |        |
|             |       |       |       |       | while maintaining  |              | substantial | efficiency   |     | advantages  | over         | manual |
| Textonly    | 0.756 | N/A   | N/A   | 0.734 |                    |              |             |              |     |             |              |        |
|             |       |       |       |       | pipeline           | development. |             | For typical  |     | enterprise  | deployments  |        |
Temporalonly N/A N/A 0.798 0.823 constructing multiple pipelines annually, the cumulative labor
Tabular+text 0.912 N/A N/A 0.874 savings substantially exceed computational costs across all
|          |     |     |       |       | infrastructure | configurations |         | we                | evaluated, |     | confirming | clear |
| -------- | --- | --- | ----- | ----- | -------------- | -------------- | ------- | ----------------- | ---------- | --- | ---------- | ----- |
| Tabular+ | N/A | N/A | 0.856 | 0.881 |                |                |         |                   |            |     |            |       |
|          |     |     |       |       | economic       | value          | despite | the computational |            |     | overhead.  | These |
temporal
|               |       |       |       |       | findings             | demonstrate |     | that while    | infrastructure |          | dependencies |          |
| ------------- | ----- | ----- | ----- | ----- | -------------------- | ----------- | --- | ------------- | -------------- | -------- | ------------ | -------- |
| Allmodalities | 0.923 | 0.941 | 0.867 | 0.889 |                      |             |     |               |                |          |              |          |
|               |       |       |       |       | merit consideration, |             |     | the framework |                | delivers | net          | positive |
Theboldvaluesrepresentthebestperformanceofeachmetric.
|     |     |     |     |     | economic    | returns    | for | practical | deployment | scenarios               |     | spanning |
| --- | --- | --- | --- | --- | ----------- | ---------- | --- | --------- | ---------- | ----------------------- | --- | -------- |
|     |     |     |     |     | high-volume | enterprise |     | use       | cases      | to resource-constrained |     |          |
researchenvironments.
| configurations, | demonstrating | the robustness | of  | our automated |     |     |     |     |     |     |     |     |
| --------------- | ------------- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
selectionmechanism.
Theablationanalysisconfirmsthateachframeworkcomponent
contributes meaningful performance improvements, with 5 Discussion
| domain-specific | feature | engineering | providing | the largest |     |     |     |     |     |     |     |     |
| --------------- | ------- | ----------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
gains. The cumulative effect of all components results in This work presents Marketing-AutoM3L, an automated
| substantial | improvements  | over       | baseline approaches | while       |               |          |                    |     |          |              |              |           |
| ----------- | ------------- | ---------- | ------------------- | ----------- | ------------- | -------- | ------------------ | --- | -------- | ------------ | ------------ | --------- |
|             |               |            |                     |             | machine       | learning | framework          |     | that     | successfully |              | addresses |
| maintaining | computational | efficiency | through             | intelligent |               |          |                    |     |          |              |              |           |
|             |               |            |                     |             | the challenge |          | of domain-specific |     | pipeline |              | construction | for       |
optimizationstrategies.
|                   |     |           |     |     | financial      | customer | analytics. |              | Our  | experimental |              | evaluation |
| ----------------- | --- | --------- | --- | --- | -------------- | -------- | ---------- | ------------ | ---- | ------------ | ------------ | ---------- |
|                   |     |           |     |     | across five    | diverse  | datasets   | demonstrates |      | that         | the          | framework  |
|                   |     |           |     |     | achieves       | 1.4%     | to 5.4%    | improvements |      | in           | ROC-AUC      | scores     |
| 4.7 Computational |     | economics | and |     |                |          |            |              |      |              |              |            |
|                   |     |           |     |     | while reducing |          | pipeline   | development  | time | by           | 6.7 compared | to         |
infrastructure trade-offs manual approaches. The ablation studies confirm that domain-
|     |     |     |     |     | specific | feature | engineering | provides |     | the | largest | individual |
| --- | --- | --- | --- | --- | -------- | ------- | ----------- | -------- | --- | --- | ------- | ---------- |
While our framework demonstrates substantial reductions contribution to model performance, validating our architectural
in human development time, the reliance on proprietary GPT-4 design decisions. The ablation study in Figure10 quantifies
API and high-end infrastructure introduces computational the incremental contribution of each framework component to
costs that warrant careful economic analysis. GPT-4 API costs overall performance. Results demonstrate that domain-aware
for complete pipeline construction average approximately feature engineering provides the most significant performance
eight dollars per pipeline across our experimental datasets, boost, followed by data modality recognition and LLM-driven
ranging from five dollars for smaller datasets to twelve model selection, validating the importance of our integrated
dollars for larger ones based on token consumption across all architectural design. By incorporating domain-specific feature
decision stages. Using conservative estimates of data scientist engineering operations such as RFM analysis and customer
labor costs at one hundred fifty dollars per hour, the 6.7- lifetime value calculations, the framework addresses the
fold reduction in development time from 156.9 minutes unique requirements of marketing prediction tasks while
to 23.4 min saves approximately 2.2 h of human labor per maintaining the flexibility of general-purpose AutoML systems.
pipeline, corresponding to three hundred thirty dollars in Experimental evaluation across five diverse customer datasets
labor cost savings. This yields net savings of approximately demonstrates consistent performance gains over both traditional
330 dollars per pipeline even after accounting for API manual approaches and existing AutoML frameworks, with
costs, representing a return on investment exceeding forty improvements ranging from 1.4% to 5.4% in ROC-AUC scores.
times the computational expense. Regarding infrastructure The ablation studies confirm that domain-specific feature
requirements, our experimental setup utilized NVIDIA A100 engineering provides the largest individual contribution to
GPUs and Apache Spark primarily to handle the largest model performance, validating the importance of incorporating
datasets efficiently, but additional experiments on standard marketing domain knowledge into automated pipelines. The
cloud instances with consumer-grade GPUs demonstrated framework achieves these improvements while reducing pipeline
only 30 percent increases in execution time while reducing development time by 6.7× compared to manual approaches,
infrastructure costs from negligible to approximately two demonstrating practical applicability in business environments
dollars per pipeline. The dependence on proprietary GPT- where rapid model deployment is essential. Natural language
4 introduces legitimate reproducibility concerns, as model directives enable business stakeholders without extensive
updates or access changes could affect framework behavior, technical expertise to specify requirements and constraints,
though our comprehensive logging of all prompt-response pairs bridging the gap between marketing objectives and machine
and preliminary experiments with open-source alternatives learningimplementation.
| FrontiersinArtificialIntelligence |     |     |     |     | 17  |     |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Tianetal. |     |     | 10.3389/frai.2026.1726900 |     |
| --------- | --- | --- | ------------------------- | --- |
FIGURE8
Modelcomplexityvs.performancetrade-offanalysisshowingMarketing-AutoM3Lachievesoptimalbalance.
FIGURE9
Modelcomplexityvs.performancetrade-offanalysisshowingMarketing-AutoM3Lachievesoptimalbalance.
6 Conclusion
|     | engineering   | capabilities essential | for financial customer | analytics.      |
| --- | ------------- | ---------------------- | ---------------------- | --------------- |
|     | While generic | AutoML frameworks      | automate               | model selection |
This work addresses the fundamental problem that existing and hyperparameter tuning, they cannot automatically identify
automatedmachinelearningsystemslackdomain-specificfeature andconstructmarketing-relevantindicatorssuchasRFMmetrics,
| FrontiersinArtificialIntelligence | 18  |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --------------- |

| Tianetal. |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1726900 |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- |
FIGURE10
Ablationstudyshowingtheincrementalcontributionofeachframeworkcomponenttooverallperformance.
customer lifetime value, and engagement scores. Marketing- frameworks, specifically translating feature importance scores
AutoM3L solves this problem by integrating domain knowledge intobusinessrecommendationssuchas’prioritizecustomerswith
directly into the automation process through LLM-driven decliningengagementscoresinthepast30days.
| intelligent        | controllers | that       | recognize     | data      | modalities,  | generate     |                   |           |     |     |
| ------------------ | ----------- | ---------- | ------------- | --------- | ------------ | ------------ | ----------------- | --------- | --- | --- |
| marketing-specific |             | features,  | and construct |           | optimized    | pipelines    |                   |           |     |     |
|                    |             |            |               |           |              |              | Data availability | statement |     |     |
| tailored           | to customer | behavior   | prediction    |           | tasks.       | Our specific |                   |           |     |     |
| contributions      | are         | threefold. | First, we     | developed | domain-aware |              |                   |           |     |     |
featureengineeringcomponentsthatautomaticallycomputeRFM Theoriginalcontributionspresentedinthestudyareincluded
scores, CLV projections, and engagement metrics, eliminating in the article/supplementary material, further inquiries can be
manual feature design—ablation studies show this component directedtothecorrespondingauthor.
alonecontributes3.3%–3.6%performanceimprovement.Second,
| we implemented |     | LLM-based | pipeline | automation |     | that reduces |     |     |     |     |
| -------------- | --- | --------- | -------- | ---------- | --- | ------------ | --- | --- | --- | --- |
Author contributions
developmenttimefrom156.9min(manualapproach)to23.4min,
achieving6.7speedupwhileimprovingaccuracy.Third,weenabled
|                  |     |               |            |     |            |          | YT: Conceptualization, | Data | curation, | Formal analysis, |
| ---------------- | --- | ------------- | ---------- | --- | ---------- | -------- | ---------------------- | ---- | --------- | ---------------- |
| natural language |     | configuration | interfaces |     | that allow | business |                        |      |           |                  |
stakeholders to specify requirements without programming Funding acquisition, Investigation, Methodology, Project
expertise, democratizing access to advanced customer analytics administration, Resources, Software, Supervision, Validation,
capabilities. Future research directions include three specific Visualization,Writing–originaldraft,Writing–review&editing.
extensions.First,incorporatingsentimentanalysisfromcustomer WS: Conceptualization, Data curation, Formal analysis, Funding
|               |          |          |      |       |        |              | acquisition, Investigation, | Methodology, | Project | administration, |
| ------------- | -------- | -------- | ---- | ----- | ------ | ------------ | --------------------------- | ------------ | ------- | --------------- |
| communication | channels | (emails, | chat | logs, | social | media) using |                             |              |         |                 |
transformer-based language models to capture attitudinal signals Resources, Software, Supervision, Validation, Visualization,
beyondbehavioraldata—preliminaryexperimentssuggest2%–3% Writing–originaldraft,Writing–review&editing.ZD:Writing
accuracy improvements are achievable. Second, implementing –originaldraft,Writing–review&editing.
| causal inference |     | techniques | such as | doubly | robust   | estimation |     |     |     |     |
| ---------------- | --- | ---------- | ------- | ------ | -------- | ---------- | --- | --- | --- | --- |
| and instrumental |     | variable   | methods | to     | identify | actionable |     |     |     |     |
Funding
retentioninterventionsratherthanmerelypredictivecorrelations,
| enabling | prescriptive | rather | than | descriptive | analytics. | Third, |     |     |     |     |
| -------- | ------------ | ------ | ---- | ----------- | ---------- | ------ | --- | --- | --- | --- |
developingautomatedmodelinterpretationmodulesthatgenerate Theauthor(s)declaredthatfinancialsupportwasnotreceived
natural language explanations aligned with marketing decision forthisworkand/oritspublication.
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 19  |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Tianetal. |     |          |     |     |     |     |           |               |              |           |           | 10.3389/frai.2026.1726900 |         |        |
| --------- | --- | -------- | --- | --- | --- | --- | --------- | ------------- | ------------ | --------- | --------- | ------------------------- | ------- | ------ |
| Conflict  | of  | interest |     |     |     |     |           |               |              |           |           |                           |         |        |
|           |     |          |     |     |     |     | support   | of artificial | intelligence |           | and       | reasonable                | efforts | have   |
|           |     |          |     |     |     |     | been made | to            | ensure       | accuracy, | including |                           | review  | by the |
YTwasemployedatEngageElement.WSwasemployedatNew authors wherever possible. If you identify any issues, please
| BeginningsCreatorNetwork. |     |     |     |     |     |     | contactus. |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
Theremainingauthordeclaresthatthisworkwasconductedin
theabsenceofanycommercialorfinancialrelationshipsthatcould
|     |     |     |     |     |     |     | Publisher’s |     | note |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- |
beconstruedasapotentialconflictofinterest.
|            |     |              |     |     |     |     | All              | claims | expressed      | in  | this article | are       | solely | those      |
| ---------- | --- | ------------ | --- | --- | --- | --- | ---------------- | ------ | -------------- | --- | ------------ | --------- | ------ | ---------- |
| Generative |     | AI statement |     |     |     |     |                  |        |                |     |              |           |        |            |
|            |     |              |     |     |     |     | of the authors   |        | and do         | not | necessarily  | represent |        | those of   |
|            |     |              |     |     |     |     | their affiliated |        | organizations, |     | or those     | of        | the    | publisher, |
|            |     |              |     |     |     |     | the editors      | and    | the reviewers. |     | Any          | product   | that   | may be     |
Theauthor(s)declaredthatgenerativeAIwasnotusedinthe
creationofthismanuscript. evaluated in this article, or claim that may be made by
Any alternative text (alt text) provided alongside figures its manufacturer, is not guaranteed or endorsed by the
| in this | article | has been | generated |     | by Frontiers | with | the publisher. |     |     |     |     |     |     |     |
| ------- | ------- | -------- | --------- | --- | ------------ | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
References
Ahmad, A. K., Jafar, A., and Aljoumaa, K. (2019). Customer churn prediction Gomaa,I.,Mokhtar,H.M.O.,El-Tazi,N.,andZidane,A.(2024).Sml-automl:a
in telecom using machine learning in big data platform. J. Big Data 6:28. smartmeta-learningautomatedmachinelearningframework.Adv.Artif.Intell.Mach.
doi:10.1186/s40537-019-0191-6 Learn.4,3074–3089.doi:10.54364/AAIML.2024.44176
Akter,J.,Roy,A.,Rahman,S.,Mohona,S.,andAra,J.(2025).Artificialintelligence- Guo, S., Deng, C., Wen, Y., Chen, H., Chang, Y., and Wang, J. (2024). Ds-
drivencustomerlifetimevalue(clv)forecasting:Integratingrfmanalysiswithmachine agent:automateddatasciencebyempoweringlargelanguagemodelswithcase-based
learningforstrategiccustomerretention.J.Comput.Sci.Technol.Stud.7,249–257. reasoning.arXivpreprintarXiv:2402.17453.
doi:10.32996/jcsts.2025.7.1.18 Han, S., Zhang, J., Shen, Y., Yan, K., and Li, H. (2025). Finsphere: a real-
Arora,K.,Potluru,V.,Sangle,S.R.,Kulkarni,P.A.,Chauhan,P.S.,Barjatiya, time stock analysis agent with instruction-tuned large language models and
S., et al. (2024). Automated machine learning (automl) for the diagnosis of domain-specific tool integration. Front. Inf. Technol. Electr. Eng. 26, 1822–1831.
melanoma skin lesions from consumer-grade camera photos. Cureus 16:e67559. doi:10.1631/FITEE.2500414
doi:10.7759/cureus.67559
HopsworksTeam(2022).AutomatedFeatureEngineeringwithFeaturetools:Deep
Baro,E.F.,Oliveira,L.S.,andBritto,A.d.S.(2025).Predictinghospitalization FeatureSynthesisforMachineLearning.HopsworksBlog.Blogpost.
| with llms from | health | insurance | data. | Med. Biol. | Eng. Comput. | 63, 1215–1226. |     |     |     |     |     |     |     |     |
| -------------- | ------ | --------- | ----- | ---------- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
doi:10.1007/s11517-024-03251-4 IEEE Standards Committee (2024). IEEE standard for algorithmic bias
considerations.TechnicalReportIEEEStd7003–2024,IEEE.
Boinpally,D.(2025).Transformingfinancialservicesthroughawsbedrock:anew
eraofllmintegration.J.Eng.Comput.Sci.4,250–257. Islayem, R., Gebreab, S., AlKhader, W., Musamih, A., Salah, K., Jayaraman,
|     |     |     |     |     |     |     | R., et al. | (2025). Using | large | language | models | for enhanced | fraud | analysis |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | ----- | -------- | ------ | ------------ | ----- | -------- |
Bonidia, R. P., Santos, A. P. A., de Almeida, B. L., Stadler, P. F., da Rocha, and detection in blockchain based health insurance claims. Sci. Rep. 15:29763.
U.N.,Sanches,D.S.,etal.(2022).Bioautoml:automatedfeatureengineeringand doi:10.1038/s41598-025-15676-4
metalearningtopredictnoncodingRNASinbacteria.Brief.Bioinform.23:bbac218.
Jain,H.,Khera,A.K.,etal.(2023).Customerchurnpredictionusingcomposite
doi:10.1093/bib/bbac218 deeplearningtechnique.Sci.Rep.13:17295.doi:10.1038/s41598-023-44396-w
| Boozary, | P., Sheykhan, | S., | GhorbanTanhaei, |     | H., and Magazzino, | C. (2025). |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------------- | --- | ------------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Kashyap,Y.,andSinha,A.(2024).LLMisallyouneed:howdoLLMSperform
Enhancing customer retention with machine learning: a comparative analysis of onpredictionandclassificationusinghistoricaldata.Int.J.Multidisc.Res.6,1–10.
| ensemble models | for | accurate churn | prediction. | Int. | J. Inf. | Manag. Data Insights |     |     |     |     |     |     |     |     |
| --------------- | --- | -------------- | ----------- | ---- | ------- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
doi:10.36948/ijfmr.2024.v06i03.23438
5:100331.doi:10.1016/j.jjimei.2025.100331
LabelYourDataTeam(2024).Multimodaldatafusion:Handlingmissingmodalities
Borle,S.,Singh,S.S.,andJain,D.C.(2008).Customerlifetimevaluemeasurement.
inmachinelearning.LabelYourDataBlog.Blogpost.
Manage.Sci.54,100–112.doi:10.1287/mnsc.1070.0746
|          |                |     |              |            |              |         | Lin, W.-Y.,        | Hu, Y.-H., | and     | Tsai, C.-F. | (2011). | Machine    | learning | in financial |
| -------- | -------------- | --- | ------------ | ---------- | ------------ | ------- | ------------------ | ---------- | ------- | ----------- | ------- | ---------- | -------- | ------------ |
| Capponi, | G., Corrocher, | N., | and Zirulia, | L. (2021). | Personalized | pricing | for                |            |         |             |         |            |          |              |
|          |                |     |              |            |              |         | crisis prediction: | a          | survey. | IEEE Trans. | Syst.   | Man Cyber. | C 42,    | 421–436.     |
customerretention:Theoryandevidencefrommobilecommunication.Telecomm. doi:10.1109/TSMCC.2011.2170420
Policy45:102069.doi:10.1016/j.telpol.2020.102069
Lin,Z.,Shen,Y.,Cai,Q.,Sun,H.,Zhou,J.,andXiao,M.(2025).Autop2c:anLLM-
Donepudi,P.K.(2019).Automationandmachinelearningintransformingthe
financialindustry.AsianBus.Rev.9,129–138.doi:10.18034/abr.v9i3.494 basedagentframeworkforcoderepositorygenerationfrommultimodalcontentin
academicpapers.arXivpreprintarXiv:2504.20115.
EducativeTeam(2023).MultimodalMachineLearning:EarlyFusionvsLateFusion.
Educative.io.Blogpost. Liu, Y., Chen, Z., Wang, Y., and Shen, Y. (2025). “Autoproteinengine: a
|     |     |     |     |     |     |     | large language | model | driven agent | framework | for | multimodal | autoML | in protein |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ----- | ------------ | --------- | --- | ---------- | ------ | ---------- |
Fastowski,A.,Prenkaj,B.,andKasneci,G.(2025).Fromconfidencetocollapsein engineering,”inProceedingsofthe31stInternationalConferenceonComputational
llmfactualrobustness.arXivpreprintarXiv:2508.16267.
|                                                                      |     |     |     |     |     |     | Linguistics:          | Industry | Track (Abu | Dhabi, | UAE: Association |     | for Computational |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------------- | -------- | ---------- | ------ | ---------------- | --- | ----------------- | --- |
| Gancheva,V.,Stoyanova,P.,andPetrov,P.(2024).“Evaluationofcloud-based |     |     |     |     |     |     | Linguistics),422–430. |          |            |        |                  |     |                   |     |
automlplatformsandopen-sourcealternatives,”inInformationandCommunication
|     |     |     |     |     |     |     | Liu, Y., | Chen, Z., | Wang, Y. | G., and | Shen, Y. | (2024). | “Toursynbio-search: | a   |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | -------- | ------- | -------- | ------- | ------------------- | --- |
TechnologiesinBusinessandEducation(ICTBE2024),63–70.
largelanguagemodeldrivenagentframeworkforunifiedsearchmethodforprotein
Gao,Z.,Chen,D.,andShen,Y.(2025).Amissingmultimodalimputationdiffusion engineering,”in2024IEEEInternationalConferenceonBioinformaticsandBiomedicine
modelfor2Dx-rayand3DCTinCOVID-19diagnosis.ExpertSyst.Appl.279:127367. (BIBM)(IEEE),5395–5400.doi:10.1109/BIBM62325.2024.10822318
doi:10.1016/j.eswa.2025.127367
|     |     |     |     |     |     |     | Luo, D., | Feng, C., | Nong, Y., | and Shen, | Y. (2024a). | “Autom3l: | an  | automated |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --------- | --------- | ----------- | --------- | --- | --------- |
GeeksforGeeks(2021).RfmAnalysisforCustomerSegmentation.GeeksforGeeks. multimodalmachinelearningframeworkwithlargelanguagemodels,”inProceedings
Tutorial. of the 32nd ACM International Conference on Multimedia (ACM), 6654–6665.
doi:10.1145/3664647.3680665
| Geetha, | N., and Krishna, | U.  | G. (2025). | “The | role of artificial | intelligence | and |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | ---------- | ---- | ------------------ | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
machinelearninginenhancingstakeholderengagementforsustainablefinanceinthe Luo, D., Feng, C., Nong, Y., and Shen, Y. (2024b). Autom3l: an automated
SMEsector,”inTheFutureofSmallBusinessinIndustry5.0(IGIGlobalScientific multimodalmachinelearningframeworkwithlargelanguagemodels.arXivpreprint
| Publishing),331–346.doi:10.4018/979-8-3693-7362-0.ch013 |     |     |     |     |     |     | arXiv:2408.00665. |     |     |     |     |     |                 |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --------------- | --- |
| FrontiersinArtificialIntelligence                       |     |     |     |     |     |     | 20                |     |     |     |     |     | frontiersin.org |     |

Tianetal. 10.3389/frai.2026.1726900
Luo,D.,Liao,W.,Li,S.,Cheng,X.,andYan,R.(2023).“Causality-guidedmulti- with partial personalized attention mechanism,” in 2022 IEEE International
memoryinteractionnetworkformultivariatestockpricemovementprediction,”in Conference on Bioinformatics and Biomedicine (BIBM) (IEEE), 1706–1709.
Proceedingsofthe61stAnnualMeetingoftheAssociationforComputationalLinguistics doi:10.1109/BIBM55620.2022.9995355
(Volume1:LongPapers),12164–12176.doi:10.18653/v1/2023.acl-long.679
Shen, Y., Sowmya, A., Luo, Y., Liang, X., Shen, D., and Ke, J. (2022b).
Luo,Y.,Feng,Y.,Xu,J.,Tasca,P.,andLiu,Y.(2025).Llm-poweredmulti-agent A federated learning system for histopathology image analysis with an
systemforautomatedcryptoportfoliomanagement.arXivpreprintarXiv:2501.00826. orchestral stain-normalization GAN. IEEE Trans. Med. Imaging 42, 1969–1981.
doi:10.1109/TMI.2022.3221724
Mokoena,P.B.(2025).Harnessingartificialintelligencebyembeddingadvanced
analyticsandmodellingtechniquesintoriskmanagementprocesses.RiskManag.Insur. Shen, Y., and Unberath, M. (2025). Constructing and interpreting digital twin
Rev.28,207–231.doi:10.1111/rmir.70006 representations for visual reasoning via reinforcement learning. arXiv preprint
arXiv:2511.12365.
Mumuni, A., and Mumuni, F. (2024). Automated data processing and feature
engineeringfordeeplearningandbigdataapplications:asurvey.J.Inf.Intell.2,1–37. Shen,Y.,Wang,C.,andKe,J.(2025e).Autopathml:Automatedmachinelearning
doi:10.1016/j.jiixd.2024.01.002 forhistologyimagesvialargelanguagemodelandmulti-agent.Artif.Intell.Eng.1,
Narayana,M.S.,Mohan,C.,Ranjan,R.,Kumari,A.,Singh,S.,Sharma,P.,etal. 32–43.doi:10.1049/aie2.12005
(2024). Automated machine learning in dentistry: a narrative review of current Shen, Y., and Zhang, D. (2025). A survey of language-guided video
applicationsandfutureperspectives.J.Clin.Med.13,1–25. object segmentation: from referring to reasoning. Vicinagearth 2, 1–20.
Nelson, J., Pavlidis, M., Fish, A., Polatidis, N., and Manolopoulos, Y. (2025). doi:10.1007/s44336-025-00018-9
Leveraging ethical narratives to enhance llm-automl generated machine learning Shen,Y.,Zhang,J.,Chen,F.,Yan,K.,andLi,H.(2025f).“Finsearch:atemporal-
models.ExpertSyst.42:e70072.doi:10.1111/exsy.70072 awaresearchagentframeworkforreal-timefinancialinformationretrievalwithlarge
Novikova,J.,Anderson,C.,Blili-Hamelin,B.,Rosati,D.,andMajumdar,S.(2025). languagemodels,”inProceedingsofthe6thACMInternationalConferenceonAIin
Consistencyinlanguagemodels:Currentlandscape,challenges,andfuturedirections. Finance(ACM),10–17.doi:10.1145/3768292.3770382
arXivpreprintarXiv:2505.00268. Shi, W., and Shen, Y. (2025). Reinforcement fine-tuning for reasoning
Ogbuonyalu,U.O.,Abiodun,K.,Dzamefe,S.,Vera,E.,Oyinlola,A.,andIgba,E. towards multi-step multi-source search in large language models. arXiv preprint
(2025).Beyondthecreditscore:Theuntappedpowerofllmsinbankingriskmodels. arXiv:2506.08352.
FinanceAccount.Res.J.7,351–366.doi:10.51594/farj.v7i4.1905 Sica,E.T.,Barboza,L.F.R.,Beneted,J.V.R.,deLima,K.V.P.,Albani,V.V.L.,
OpenReview (2024). Multimodal data fusion strategies for machine learning. Santos,E.,etal.(2025).Bigdataanalysisanddimensionalityreductionforpredictprice
OpenReviewForum.Discussionforum. trendsintheBrazilianelectricitymarketconsideringinterdisciplinaryphenomena.
IEEELatinAm.Trans.23,812–821.doi:10.1109/TLA.2025.11119488
Optimove (2023). Modern RFM analysis: Automated feature engineering for
customerlifetimevalue.OptimoveResources.Resourcecenterarticle. Sun,X.,Wang,Y.G.,andShen,Y.(2025).Amultimodaldeeplearningframework
forenzymeturnoverpredictionwithmissingmodality.Comput.Biol.Med.193:110348.
Qi,Y.,Lai,F.,Chen,G.,andGan,W.(2023).F-rfm-miner:anefficientalgorithm doi:10.1016/j.compbiomed.2025.110348
forminingfuzzypatternsusingtherecency-frequency-monetarymodel.Appl.Intell.
53,27892–27911.doi:10.1007/s10489-023-04990-x TechAhead(2024).Democratizingmachinelearningusingautoml.TechAheadBlog.
Blogpost.
Qian,Y.,andShen,Y.(2025).“Feature-awaresequencemodelsfortabulardata
processing with missing values,” in International Conference on Artificial Neural Trirat,P.,Jeong,W.,andHwang,S.J.(2025).Amulti-agentLLMframeworkfor
Networks(Springer),114–126.doi:10.1007/978-3-032-04549-2_10 full-pipelineautoML.arXivpreprintarXiv:2410.02958.
Qiao, Q., and Beling, P. A. (2016). Decision analytics and machine Webb, G. I. (1996). Integrating machine learning with knowledge acquisition
learning in economic and financial systems. Environ. Syst. Decis. 36, 109–113. through direct interaction with domain experts. Knowl.-Based Syst. 9, 253–266.
doi:10.1007/s10669-016-9601-x doi:10.1016/0950-7051(96)01033-7
Rajendran,N.(2025).EnhancingCustomerSegmentationandBehaviourAnalysis Wen, Y., Wang, Y., Yi, K., Ke, J., and Shen, Y. (2024). “Diffimpute:
withRFMClustering:AMachineLearningApproach.PhDthesis,NationalCollegeof tabular data imputation with denoising diffusion probabilistic model,” in 2024
Ireland,Dublin. IEEE International Conference on Multimedia and Expo (ICME) (IEEE), 1–6.
doi:10.1109/ICME57554.2024.10687685
Sample,C.,Zhu,Y.,Liu,T.,Ye,J.,Feng,C.,andShen,Y.(2024).Evaluationoflarge
languagemodel-drivenAutoMLindataandhuman-computerinteraction.Front.Artif. Wu,S.,Fei,H.,Pan,L.,Wang,W.Y.,Yan,S.,andChua,T.-S.(2025).“Combating
Intell.8:1590105.doi:10.3389/frai.2025.1590105 multimodalLLMhallucinationviabottom-upholisticreasoning,”inProceedingsofthe
AAAIConferenceonArtificialIntelligence,8460–8468.doi:10.1609/aaai.v39i8.32913
Sheikh, M., and Conlon, S. (2012). A rule-based system to extract financial
information.J.Comput.Inf.Syst.52,10–19.doi:10.1080/08874417.2012.11645572 Ye,W.,Guo,Z.,Ren,Y.,Tian,Y.,Shen,Y.,Chen,Z.,etal.(2025).Diffm4RI:alatent
diffusionmodelwithmodalityinpaintingforsynthesizingmissingmodalitiesinMRI
Shen,Y.,Chen,Z.,Mamalakis,M.,He,L.,Xia,H.,Li,T.,etal.(2024a).“Afine- analysis.IEEEJ.Biomed.HealthInform.2025,1–13.doi:10.1109/JBHI.2025.3580510
tuningdatasetandbenchmarkforlargelanguagemodelsforproteinunderstanding,”in
2024IEEEInternationalConferenceonBioinformaticsandBiomedicine(BIBM)(IEEE), Yuan,Y.,Wu,H.,Zhou,H.,Liu,X.,Chen,H.,Xin,Y.,etal.(2025).Understanding
2390–2395.doi:10.1109/BIBM62325.2024.10821894 6Gthroughlanguagemodels:acasestudyonllm-aidedstructuredentityextractionin
telecomdomain.arXivpreprintarXiv:2505.14906.
Shen,Y.,Chen,Z.,Mamalakis,M.,Liu,Y.,Li,T.,Su,Y.,etal.(2024b).“Toursynbio:
amulti-modallargemodelandagentframeworktobridgetextandproteinsequences Zeng, Z., Watson, W., Cho, N., Rahimi, S., Reynolds, S., Balch, T., et al.
forproteinengineering,”in2024IEEEInternationalConferenceonBioinformaticsand (2023). “Flowmind: automatic workflow generation with LLMS,” in Proceedings
Biomedicine(BIBM)(IEEE),2382–2389.doi:10.1109/BIBM62325.2024.10822695 of the Fourth ACM International Conference on AI in Finance (ACM), 73–81.
doi:10.1145/3604237.3626908
Shen,Y.,Fan,C.,Li,C.,andUnberath,M.(2025a).Reasoningtext-to-videoretrieval
via digital twin video representations and large language models. arXiv preprint Zhang,Z.,Liu,S.,Liu,Z.,Zhong,R.,Cai,Q.,Zhao,X.,etal.(2025).“LLM-powered
arXiv:2511.12371. usersimulatorforrecommendersystem,”inProceedingsoftheAAAIConferenceon
ArtificialIntelligence,13339–13347.doi:10.1609/aaai.v39i12.33456
Shen,Y.,Li,C.,Fan,C.,andUnberath,M.(2025b).“Temporally-constrainedvideo
reasoning segmentation and automated benchmark construction,” in International Zhao,Z.,Birke,R.,andChen,L.Y.(2025).“Tabula:harnessinglanguagemodelsfor
Workshop on Foundation Models for General Medical AI (Springer), 150–158. tabulardatasynthesis,”inPacific-AsiaConferenceonKnowledgeDiscoveryandData
doi:10.1007/978-3-032-07845-2_15 Mining(Springer),247–259.doi:10.1007/978-981-96-8186-0_20
Shen, Y., Li, C., Liu, B., Li, C.-Y., Porras, T., and Unberath, M. (2025c). Zhou,L.,Zhang,Y.,Yu,J.,Wang,G.,Liu,Z.,Yongchareon,S.,etal.(2025).LLM-
“Operatingroomworkflowanalysisviareasoningsegmentationoverdigitaltwins,” augmentedlineartransformer-cnnforenhancedstockpriceprediction.Mathematics
in International Conference on Medical Image Computing and Computer-Assisted 13:487.doi:10.3390/math13030487
Intervention(Springer),415–424.doi:10.1007/978-3-032-05114-1_40 Zhu,Q.,Cao,J.,Lu,Y.,Lin,H.,Han,X.,Sun,L.,etal.(2025).“Domaineval:anauto-
Shen, Y., Li, C., and Unberath, M. (2025d). Text-driven reasoning video constructedbenchmarkformulti-domaincodegeneration,”inProceedingsoftheAAAI
editing via reinforcement learning on digital twin representations. arXiv preprint ConferenceonArtificialIntelligence,26148–26156.doi:10.1609/aaai.v39i24.34811
arXiv:2511.14100. Zou, H., Zhao, Q., Tian, Y., Bariah, L., Bader, F., Lestable, T., et al. (2025).
Shen, Y., Liu, B., Yu, R., Wang, Y., Wang, S., Wu, J., et al. (2022a). Telecomgpt:aframeworktobuildtelecom-specificlargelanguagemodels.IEEETrans.
“Federated learning for chronic obstructive pulmonary disease classification Mach.Learn.Commun.Netw.3,948–975.doi:10.1109/TMLCN.2025.3593184
FrontiersinArtificialIntelligence 21 frontiersin.org