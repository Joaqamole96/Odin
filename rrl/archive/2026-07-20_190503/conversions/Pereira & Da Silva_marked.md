Received6February2025,accepted30March2025,dateofpublication2April2025,dateofcurrentversion11April2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3557229
A Comparison of Approaches for Handling
Concept Drifts in Data Processed
With Machine Learning
EMANUELVALÉRIOPEREIRA ,(Member,IEEE),ANDWENDLEYSOUZADASILVA
ComputerEngineeringDepartment,FederalUniversityofCeará,Sobral60020-181,Brazil
Correspondingauthor:EmanuelValérioPereira(emanuelvalerio@alu.ufc.br)
ThisworkwassupportedbytheArticleProcessingChargefundedbytheCoordenaçãodeAperfeiçoamentodePessoaldeNívelSuperior
(CAPES)underGrant00x0ma614.
ABSTRACT In the realm of machine learning models, the pursuit of achieving favorable metrics is
undeniably significant. However, these models confront phenomena that can diminish their effectiveness
ifleftunaddressed–notably,thephenomenonofconceptdrift.Conceptdriftmaterializeswhenunforeseen
alterations in the statistical properties of the target variable transpire over time. This article introduces a
comprehensiveanalysisofclassicaltreatmentmethods,examiningthebehaviorofmachinelearningmodels
across diverse datasets. Various concept drift detection algorithms are employed, facilitating a holistic
assessment.Thestudyencompassesacomparativeexplorationofdifferentclassificationalgorithmswithin
thescikit-multiflowframework.Thesealgorithmsintegrateadaptivestrategiestocontendwithconceptdrifts.
Through this generalized analysis, the performance of distinct classification algorithms is contrasted. The
overarching aim is to facilitate the selection of optimal classification methods aligned with specific types
ofconceptdrift.Ultimately,thisstudyprovidesapivotaltoolkitforthejudiciousselectionofclassification
methods,enhancingmodeladaptabilityinthepresenceofconceptdrifts.Inadditiontosheddinglightonthe
behaviorofmachinelearningmodelsunderconceptdrift,thefindingsempowerpractitionersandresearchers
tomakeinformeddecisionstooptimizemodelrobustness.
INDEXTERMS Classifiers,conceptdrift,datastream,evaluation,machinelearning.
I. INTRODUCTION government data, and industries. In such contexts, the
With the continuous advancement of machine learning accuracyandreliabilityofmodelsarevitaltomakingaccurate
technology, it is essential to understand and address the and impactful decisions. Adopting models that are outdated
recurringchallengeinmachinelearningsystemsisessential: oraffectedbyconceptdriftcanleadtoinaccuratepredictions,
conceptdrift.Conceptdriftreferstothephenomenonwhere misdiagnoses,andpotentiallysevereconsequences.
the statistical properties of the target variable, which the Furthermore,datagenerationandcollectionhavebecome
model is trying to predict, change over time in unforeseen even more diverse and voluminous with the increasing use
ways [1]. This poses a critical factor that can negatively ofInternetofThings(IoT)devices[2].IoTdevicesareinte-
impacttheperformanceofmachinelearningmodelstrained grated into various spheres of modern life, including home
onhistoricaldata. automation, transportation, healthcare, and environmental
Theneedtokeepmachinelearningmodelsup-to-dateand monitoring. In this scenario, analyzing data processed by
free from data drift is particularly crucial in areas dealing machine learning is key to deriving valuable and actionable
with critical and high-risk information, such as healthcare, insights from this information. However, the presence of
concept drift in the data collected by IoT devices can affect
The associate editor coordinating the review of this manuscript and the accuracy of models and consequently compromise the
effectivenessofapplicationsandservices.
approvingitforpublicationwasDominikStrzalka .
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME13,2025 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 61109

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
IntherealmofSupervisedlearning-basedmachinelearn- In this regard, it is necessary to add to this scheme of
ing systems, which is the focus of this article, the general building a machine learning model three new, important
approach involves extracting features from the observed methods for building more robust models. These new
system. These features are used to construct data that methods are drift detection (whether drifts occur), drift
ideallydistinguishesdifferentcomponentsofthesystem.The understanding (when, how, and where it occurs), and drift
betterthisdatacandifferentiatebetweenthesecomponents, adaptation(howtoreactifdriftoccurs).
the higher the expected performance of the model during Concept drift covers a variety of scenarios, including
training. During the training process, this data is presented gradual changes, abrupt changes, and even the presence of
to the model, and metrics such as accuracy are analyzed new concepts not previously observed in the training data.
toassessthesystem’sperformance.Accuracyquantifiesthe From this perspective, this article uses different methods of
numberofcorrectpredictionsmadebythemodeloutofthe detectingconceptdriftbecauseitisacomplextasktoidentify
totalnumberofsamples. thedifferentvarietiesofscenariosofchangesinthedatabase
However, the performance of these systems, specifically accurately.Thus,itaimstovarythedetectionmethodssothat
thedataquality,issubjecttosuchstatisticalvariationsdefined results that reflect the different scenarios of changes in the
earlier as concept drift. A practical example experienced dataareobtainedinarealway.
through the concept drift phenomenon, based on its defini- Throughout this article, the need for systems with rea-
tion,wasthecoronavirusdisease2019(COVID-19).Changes sonable accuracies that remain in line with the dynamic
ingloballifestylepatternswereradicallyaltered,andmodels behavior of the data will be emphasized. The comparative
trained pre-pandemic might no longer correspond to the analysis will provide valuable insights for developers and
moment during the pandemic. The data generation during researchers interested in improving their concept drift
this period was a complex process undergoing substantial handling approaches to ensure their models’ continued
changes[3]. performance and reliability. In sum, this paper seeks
Assumingthatthesamplefunctionrepresentsthebuyer’s to contribute to the field of concept drift handling in
behavior for each month over a year, we can model this machine learning-processed data by offering a compre-
system as a stochastic process. From this, we can define a hensive overview of available approaches and identifying
stochasticprocessasstationary,whereinamachinelearning best practices to mitigate the negative impacts of concept
modeltrainedataspecifictimeoftheyearwouldbecapable drift on models. The understanding and application of
of predicting customer behavior throughout the analysis these strategies are essential to ensure the effectiveness of
period. In other words, the statistical characteristics of the machinelearningapplicationsinrealandconstantlyevolving
random process remain unchanged over time. On the other scenarios.
hand, concept drift, in this sense, can be classified as a
non-stationary process. The statistical characteristics of the II. PROBLEMDESCRIPTION
sampledprocessatagiventime,t ,nolongermaintainthose This section will discuss more specific content definitions
1
characteristicsattimet +τ.Therefore,thesecharacteristics of concept drift, the different types of concept drift will
1
change over time. Based on this definition, it becomes be treated, once the different types of concept drift are
necessarytodevelopmachinelearningmodelsthatarerobust defined, classical algorithms for detection of concept drift
to concept drift, enabling the model to maintain its metrics will be presented, and finally, the problem formulation will
overtime. bediscussed.
In our paper, we will discuss different techniques that
can be used to make machine learning models adaptable A. CONCEPTDRIFTDEFINITION
to the changing statistical characteristics of the underlying Concept drift is a phenomenon that occurs when changes
process.Theideaistoensurethattheperformanceanalysis in statistical properties occur with the target variable over
metrics for models trained on data streams are not only a period of time [1]. In a more general sense, one can
based on traditional metrics like accuracy and F1 score understand a machine learning model trained on historical
but also take into account the occurrence of concept drift. data by modeling the underlying system as a stochastic
Systems should be capable of detecting when concept drift process. This is akin to associating a sample function of
occurs,whereitoccurs,andwhatactionstotaketomaintain the stochastic process with the features extracted during
model performance, making the model adaptable to this specifictimeintervals.Eachsamplefunctionthatcomposes
phenomenon. thestochasticprocesscanrepresentthecharacteristicsofthe
Thepresentstudyseekstoevaluatetheimpactsofconcept model. According to the theory of stochastic processes, for
drift on machine learning models trained in stream data, agiventimeinstant,t,thereisarandomvariablethatmaps
as well as strategies to mitigate these effects. Different theprocessbysamplingitattimet.Therefore,thisrandom
methodsofhandlingconceptdriftwillbeinvestigated,such variable corresponds to points from the sample functions,
as retraining the model with new data and using detection meaningthefeaturesextractedattimet.
algorithms to identify and remove data affected by concept Stochastic processes have a specific classification known
drift. as stationary stochastic processes, and this definition arises
61110 VOLUME13,2025

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
from the fact that the statistical properties do not change occurrences.Itisfromthisdynamicthatdetectionalgorithms
over time. In contrast, the concept drift phenomenon can are designed and, ultimately, methods for adapting to these
be classified as a non-stationary process [4]. Its definition shifts.Thus,itisunderstoodthatsomealgorithmswillexhibit
lies in the fact that the statistical properties of a target distinctperformanceswhenencounteringdatawhoseconcept
variable, in this context, a given random variable X (i.e., drift occurrences differ from those for which the algorithm
a stochastic process sampled at time t), have different wasdesignedtohandle.
statistical characteristics for the same process sampled at In general, there are four types, namely, abrupt, where
a time t , in other words, the statistical characteristics of variations in the temporal domain related to joint prob-
2
the random variable or target variable vary with time. This abilities occur within a very short period and maintain
approach, in terms of a stochastic process, assumes that this new configuration during subsequent times; gradual
amongthesamplefunctionsthatcomposeit,onerepresents concept drift occurs over short periods, returning to old
theclass,andtheotherscanbeunderstoodasfeaturevectors. statistical properties until it persists during subsequent time
This modeling is only at the level of problem visualization. instants. On the other hand, incremental concept drift,
Mathematically, concept drift is defined as a relation of as suggested by its name, involves subtle variations related
conditionalandmarginalprobabilitiesviaBayes’theorem. to statistical properties, taking a time window to truly
According to paper [1], concept drift can be modeled in perceive this variation. Finally, recurrent concept drift can
termsofBayes’theorem.Inotherwords,itinvolvesrelating be seen as abrupt but returns to past metrics and recurs
the joint probability of two random variables to conditional temporally[5].
probability and marginal probability. With that said, let the
time period be [0, t], and consider a set of samples denoted C. MOTIVATIONS
as S 0,t = {d 0 ,...,d t }, where d i = (X i ,y i ) represents an Severalworksinthescientificliteraturehavebeendedicated
observationofthesamples,withX asthefeaturevectorand to robustly addressing different proposals for concept drift
i
y asthetargetvariable.Hence,thejointprobabilityofthese detection methods and robust algorithms to deal with these
i
observationsX andydenotestheconceptdriftphenomenon dynamicscenarios.However,uponconductingameticulous
ifandonlyif: bibliographic review, a gap is evident in the literature
concerning the comprehensive comparison of these classi-
p t (X,y)̸=p t+1 (X,y). (1) fication algorithms, especially those implementing concept
In this way, the joint probability can be decomposed drifttreatmentmethods.
into the conditional and marginal probability functions. Whilesomestudies,suchasthe[6]paper,haveapproached
Therefore,letp (X,y)=p (y|X)·p (X). theanalysisoftreatmentmethodsusingspecificmodelslike
t t t
Based on this, concept drift can be sliced into three SVM (Support Vector Machine), these analyses often limit
mathematical models of occurrence. The first follows the themselves to a few methods and a single algorithm. The
expression p t (X) ̸= p t+1 (X), while the conditional prob- study [1] explores various concepts related to concept drift,
ability does not vary with time, classifying it as virtual making it a significant contribution by addressing multiple
concept drift. This is because if p (X) does not affect the aspects, such as answering questions like when, where,
t
model’s decision, based on the fact that the probability and how concept drift impacts a dataset. Furthermore, the
of the class being y given that X occurred is temporally paper also investigates some potential adaptation strategies
invariant. for concept drift. However, it lacks results that broadly and
Anothersourceofoccurrenceisifthemarginalprobability comprehensively analyze the impact of different adaptation
is temporally invariant, p t (X) = p t+1 (X), while temporal techniques for handling concept drift. The article [7]
variationoccursinthejointprobabilityp t (y|X)̸=p t+1 (y|X). presents a performance analysis of several concept drift
Inthiscase,imprecisionisobservedinthecorrectclassifica- detection algorithms. The study [8] proposes algorithms for
tionofaclassygiventhepresentedsetoffeaturesX,leading addressingconceptdriftspecificallyinthecontextofGlobal
to imprecision in the decision boundary and, consequently, Forecasting Models. However, its scope is limited, as the
adecreaseinmodelaccuracymetrics. proposed methods are exclusively tailored to this particular
Finally, the combination of the other two cases of occur- scenario. However, it does not include any examination of
rence,wherebothconditionalandmarginalprobabilitiesvary the different methods for handling concept drifts or how
withtime;inotherwords,conceptdriftfocusesonthechange these methods relate to the results obtained. The study [9]
inbothP t (y|X)andP t (X). highlights the importance of addressing concept drift by
applyingtechniquessuchasmodelretraining,demonstrating
B. TYPESOFCONCEPTDRIFT significantaccuracyimprovementswhentreatmentstrategies
Throughout the process discussed in this work concerning are implemented. However, the study is limited in several
detection algorithms and the treatment methods analyzed, aspects,includingtherangeoftreatmenttechniquesexplored,
their precision metrics in model analyses depend on the thenumberofdatasetsanalyzed,andthevarietyofdetection
nature of the data. This involves the intrinsic characteristics algorithmsevaluated.Additionally,whilethestudyprovides
of each database, with a focus on the types of concept drift valuable insights, its focus is primarily confined to the
VOLUME13,2025 61111

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
domainofBusinessProcessMining.Thework[10]provides a comprehensive perspective on the interplay between
a comprehensive overview of various treatment methods, concept drift and machine learning models. The results
algorithms, and datasets—both real and synthetic—within contribute to the informed selection of optimal classifiers,
the scope of its subject matter. Its primary focus is to optimizing their performance under diverse concept drift
| document | and               | summarize |          | these       | aspects as   | presented in | scenarios. |     |     |     |     |     |     |
| -------- | ----------------- | --------- | -------- | ----------- | ------------ | ------------ | ---------- | --- | --- | --- | --- | --- | --- |
| various  | studies           | from      | the      | literature, | offering     | significant  |            |     |     |     |     |     |     |
| insights | and observations. |           | However, |             | it should be | noted that   |            |     |     |     |     |     |     |
A. METHODOLOGY
the study does not include a comparative analysis of these In this subsection, the methodology employed for the
methodsordatasets.
comparisonofconceptdrifttreatmentmethodsinthisstudy
Unlikealltheworkscited,thisisthefirststudytocompare will be outlined. We will elaborate on the classification
| the performance |     | of different |     | concept | drift treatment | tech- |            |           |     |         |     |          |           |
| --------------- | --- | ------------ | --- | ------- | --------------- | ----- | ---------- | --------- | --- | ------- | --- | -------- | --------- |
|                 |     |              |     |         |                 |       | algorithms | utilized, | as  | well as | the | datasets | employed. |
niquesinageneralizedmanner,encompassingadiverserange
|     |     |     |     |     |     |     | Furthermore, | we  | shall present | the | parameters |     | selected for |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | ---------- | --- | ------------ |
ofbothartificialandreal-worlddatasetsaffectedbyvarious the machine learning methods and explain the evaluation
| types of | concept | drift | occurrences. |     | It also | incorporates |     |     |     |     |     |     |     |
| -------- | ------- | ----- | ------------ | --- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
metricsemployed.Thiscomprehensivedescriptionservesto
different detection algorithms and analyzes classification establishasolidfoundationforthesubsequentanalysesand
algorithmsinconjunctionwithtreatmentmethods.Moreover,
findings.
| it highlights | the | critical | importance |     | of these | treatment |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ---------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
techniquesinacomprehensivemanner.
1) DATASET
Thisarticle’sproposalgoesbeyond,aimingforathorough
Eightdistinctdatasetswereemployedtoconductacompre-
evaluationoftreatmentmethodsondiversedatasets,consid-
hensiveanalysisencompassingvariousscenariosofconcept
| ering a       | variety | of classification |           | algorithms. | Understanding  |              |                   |              |               |          |          |                    |            |
| ------------- | ------- | ----------------- | --------- | ----------- | -------------- | ------------ | ----------------- | ------------ | ------------- | -------- | -------- | ------------------ | ---------- |
|               |         |                   |           |             |                |              | drift occurrence. |              | This approach |          | aims not | only to            | scrutinize |
| the behavior  | of      | machine           | learning  | models      | in varied      | scenar-      |                   |              |               |          |          |                    |            |
|               |         |                   |           |             |                |              | the behavior      | of           | classifiers   | in the   | presence | of concept         | drift      |
| ios regarding |         | datasets,         | detection | algorithms, | classification |              |                   |              |               |          |          |                    |            |
|               |         |                   |           |             |                |              | but, more         | importantly, | to            | evaluate | the      | classifiers        | that best  |
| algorithms,   | and     | treatment         | methods   |             | motivates      | this work to |                   |              |               |          |          |                    |            |
|               |         |                   |           |             |                |              | accommodate       | different    | types         | of       | concept  | drift occurrences. |            |
| contribute    | to the  | field             | of data   | drift       | by providing   | extensive    |                   |              |               |          |          |                    |            |
Bydoingso,theobjectiveistopresentoutcomesthatcould
informationaboutthesecomparisons.
provevaluableacrossdiversesituations.
| The distinctive |     | aspect | of  | this | work lies | not only in |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --- | ---- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Airlines:
comparing concept drift treatment methods but also in • Real-world data containing information from
proposing innovative approaches and ensemble strategies. scheduled departures of commercial flights within the
These methods are applied across various concept drift US.Theobjectiveistopredictifaflightwillbedelayed
| scenarios,broadeningtheunderstandingoftheireffectiveness |     |     |     |     |     |     | [11]. |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
in different contexts and with diverse algorithms. This • Covertype: This data set contains data collected over
|     |     |     |     |     |     |     | time | by the | US Forest | Service. | Classes | correspond | to  |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --------- | -------- | ------- | ---------- | --- |
significantlycontributestoadvancingknowledgeinconcept
drift treatment, addressing a gap identified in the existing covertypeinaforestonsquaresof30×30meters[12].
literature. By adopting a comprehensive and comparative • Electricity Market: Data from the Australian New
approach, this study aims to provide valuable insights for SouthWaleselectricitymarketwherepricesarenotfixed
researchers,practitioners,andmachinelearningenthusiasts. but change based on offer and demand. The 2 target
|     |     |     |     |     |     |     | classes | represent | changes | in  | the price | (1 = | up or 0 = |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------- | --- | --------- | ---- | --------- |
Itoffersadeeperunderstandingofhowmodelsbehaveinthe
faceofdynamicchangesindata,therebydrivingprogressin down)[13].
theapplicationofthesetechniquestoreal-worldscenarios. • SEA-abrupt and SEA-gradual: A data stream with
|     |     |     |     |     |     |     | three | numerical | features | where | only | two attributes | are |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | -------- | ----- | ---- | -------------- | --- |
III. EVALUATIONOFTREATMENTMETHODS related to the target class. Created using the SEA
Thissectioninitiallyanalyzesclassicalmethodsfortreating generator. Three abrupt drifts are simulated for SEAa
concept drift individually. Subsequently, the behavior of a andthreegradualdriftsforSEAg[11].
machine learning model is examined using two classifiers: • Hyperplane-fast: A data stream with fast incremen-
one without concept drift adaptation and another that tal drifts where a d-dimensional hyperplane changes
performs concept drift detection and adaptation. Further- position and orientation. Created with the random
more, a broader comparison is conducted by contrasting hyperplanegenerator[11].
differentclassifiersincorporatingconceptdriftdetectionand • MovingSquares:Fourequidistantlyseparated,squared
adaptation. uniform distributions are moving in the horizontal
Acrossalltheaforementionedcomparisons,acomprehen- directionwithconstantspeed.Thedirectionisinverted
sive and generalized analysis is undertaken, encompassing whenever the leading square reaches a predefined
variations in diverse datasets, concept drift detection algo- boundary.Eachsquarerepresentsadifferentclass.The
rithms, and classifiers. This approach ensures a conclusive addedvalueofthisdatasetisthepredefinedtimehorizon
evaluation. Through these examinations, insights into the of 120 examples before old instances start to overlap
efficacyofdistincttreatmentstrategiesaregarnered,offering withcurrentones.Thisisespeciallyusefulfordynamic
| 61112 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
slidingwindowapproaches,allowingtotestwhetherthe employadaptationtechniquesforhandlingconceptdrift.Itis
| sizeisadjustedaccordingly[14]. |      |          |         |              |           |           |     | atree-basedalgorithm.         |     |     |     |     |     |
| ------------------------------ | ---- | -------- | ------- | ------------ | --------- | --------- | --- | ----------------------------- | --- | --- | --- | --- | --- |
| • Weather:                     |      | Contains | weather | information  |           | collected |     |                               |     |     |     |     |     |
| between                        | 1949 | and      | 1999    | in Bellevue, | Nebraska. |           | The |                               |     |     |     |     |     |
|                                |      |          |         |              |           |           |     | b: HOEFFDINGADAPTIVETREE(HAT) |     |     |     |     |     |
objective is to predict if it will rain or not on a given Contrasting with the HT algorithm, the HAT algorithm
date[15]. employs the concept drift detection algorithm ADWIN to
Thetable1summarizesthecharacteristicsofthedatabases monitor performance within the decision tree branches.
Iftheevaluatedclassificationmetricsundergoaperformance
usedintheexperiments:
degradationstemmingfromfactorssuchasconceptdrift,the
|     |     |     |     |     |     |     |     | algorithm | implements | a treatment | technique | by substituting |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ----------- | --------- | --------------- | --- |
2) FRAMEWORKDESCRIPTION
|            |             |       |              |                  |           |               |        | the old  | branches | with new ones,  | provided | that    | these new  |
| ---------- | ----------- | ----- | ------------ | ---------------- | --------- | ------------- | ------ | -------- | -------- | --------------- | -------- | ------- | ---------- |
| It is well | known       | that  | data streams | are              | generated | at            | a con- |          |          |                 |          |         |            |
|            |             |       |              |                  |           |               |        | branches | exhibit  | better accuracy | [22].    | It is a | tree-based |
| siderably  | high speed, | which |              | poses challenges |           | in processing |        |          |          |                 |          |         |            |
algorithm.
| and, for         | instance, | storing | this           | data. | This is     | due    | to the |                                    |        |                |           |       |       |
| ---------------- | --------- | ------- | -------------- | ----- | ----------- | ------ | ------ | ---------------------------------- | ------ | -------------- | --------- | ----- | ----- |
| rapid generation |           | speed,  | coupled        | with  | substantial | memory |        |                                    |        |                |           |       |       |
|                  |           |         |                |       |             |        |        | c: EXTREMELYFASTDECISIONTREE(EFDT) |        |                |           |       |       |
| consumption,     | making    |         | it impractical |       | to store    | and    | apply  |                                    |        |                |           |       |       |
|                  |           |         |                |       |             |        |        | EFDT is                            | also a | classification | algorithm | based | on an |
machinelearningapproachestohistoricaldata.Furthermore,
incrementaldecisiontreestructure.Thealgorithmpossesses
| many companies |     | and | governmental | entities | adopt | a   | hybrid |     |     |     |     |     |     |
| -------------- | --- | --- | ------------ | -------- | ----- | --- | ------ | --- | --- | --- | --- | --- | --- |
model, where new data, to be analyzed using a pre-trained the capability of swift learning for a given set of stationary
data.Consequently,duetoitsrelianceonastationarydataset,
| model, needs | to  | be integrated. |     | As mentioned |     | earlier, | these |               |          |               |           |     |            |
| ------------ | --- | -------------- | --- | ------------ | --- | -------- | ----- | ------------- | -------- | ------------- | --------- | --- | ---------- |
|              |     |                |     |              |     |          |       | the algorithm | refrains | from applying | treatment |     | methods in |
scenariosbringaboutcertainchallengesandcomplexities.
|     |     |     |     |     |     |     |     | the event | of concept | drift occurrences. |     | The EFDT | aims to |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ------------------ | --- | -------- | ------- |
Inotherwords,thesealgorithmsmustbemodifiedtocater
identifytheoptimalsplitduringthemodeltrainingprocess.
| to limitations | in  | resources | and | challenges | stemming |     | from |     |     |     |     |     |     |
| -------------- | --- | --------- | --- | ---------- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- |
factors such as single-pass processing, memory constraints, Ifaparticularsplitisdeemedbeneficial,thealgorithmrevisits
thechoicetopursueanevenmoreadvantageousdivision[23].
| rapid data | access, | and | the occurrence |     | of concept | drift. | This |     |     |     |     |     |     |
| ---------- | ------- | --- | -------------- | --- | ---------- | ------ | ---- | --- | --- | --- | --- | --- | --- |
Itisalsoatree-basedalgorithm.
| adaptation | is essential |     | due to | the dynamic | characteristics |     | of  |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------ | ----------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
datastreamsastheyevolveovertime.
Inthiscontext,thisarticlereliesontheanalysesconducted d: K-NEARESTNEIGHBORSADAPTIVEWINDOWING
| within the | framework |     | of the | scikit-multiflow |     | library. | scikit- | (KNNADW) |     |     |     |     |     |
| ---------- | --------- | --- | ------ | ---------------- | --- | -------- | ------- | -------- | --- | --- | --- | --- | --- |
KNNADWisaclassificationalgorithmbasedontheclassical
multiflowrepresentsanopen-sourcemachinelearningtoolkit
adapted to deal with streaming data. It expands on existing KNN (K-Nearest Neighbors) classifier. KNNADW is a
Python scientific tools, catering to scenarios where data is versionofKNNdesignedforlearningenvironmentssubject
generated continuously and requires real-time processing to concept drift occurrences. In other words, the distinction
and analysis. Unlike traditional approaches, this framework lies in its utilization of concept drift treatment methods.
Toachievethis,theconceptdriftdetectionalgorithmADWIN
| does not | store | data samples |     | and instead | exposes | learning |     |     |     |     |     |     |     |
| -------- | ----- | ------------ | --- | ----------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
techniquestonewdatainstancesonlyonce[16]. is incorporated. Once a drift occurrence is identified, the
The inherent infinite nature of data streams introduces algorithm discards or removes the samples, adjusting the
additional complexities. Although the flow of data is windowsize.ItisaK-NearestNeighbor-basedalgorithm.
limitless,resourcessuchasmemoryandtimeremainlimited,
issuesdiscussedearlierwhichforcestreamlearningmethods e: ACCURACYWEIGHTEDENSEMBLECLASSIFIER(AWEC)
to be efficient. Furthermore, the dynamic nature of the AWEC is a classification algorithm based on ensembles,
environmentmeansthatdatacharacteristicscanevolveover
whichmeansit’sacollectionofclassificationmodelswhere
time.Inthescikit-multiflowlibrary,itispossibletoworkwith each model’s classification accuracy in a continuous data
different methods for detecting concept drift and providing stream environment determines its weighting. Depending
varioustypesofclassifiersandregressors,thusprovidingthe on their individual performance, the models are weighted
essentialtoolsforthestudycoveredinthisarticle. accordingly.Thisensembleensuresrobustnessandefficiency
TheTable2providesadetaileddescriptionoftheconcept
inscenariosinvolvingconceptdriftoccurrences.Forinstance,
driftdetectionalgorithmsutilizedinthisstudy. the learning models used in the ensemble can incorporate
On the other hand, the descriptions of the classification conceptdrifthandlingtechniques[24].
algorithmsevaluatedareasfollows.
f: ADAPTIVERANDOMFORESTCLASSIFIER(ARFC)
a: HOEFFDINGTREE(HT) ARFC is a classification algorithm based on the random
HT is a classification algorithm based on incremental forest approach, and one of its important features is the
decision trees capable of learning from a substantial stream utilization of concept drift detection algorithms for each
ofdata.Itassumesthatthedistributionofexamplesremains decision tree that comprises the classifier. This allows
unchanged over time; therefore, the algorithm does not for selective reinitialization in response to concept drift
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 61113 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
TABLE1. Datasetdescription.
occurrences.Additionally,itdistinguishesitselfbyensuring parameter values. By adhering to these default configura-
diversityinthemodelconstructionprocess.Thisisachieved tions, we ensure that the observed performance differences
through both the random selection of subsets for node areprimarilyattributedtotheconceptdrifthandlingstrategies
splittingindecisiontreesandtheresamplingprocess[11]. rather than being influenced by parameter optimization.
This approach reflects our commitment to maintaining the
g: VERYFASTDECISIONRULESCLASSIFIER(VFDRC) integrityandvalidityofthecomparativeanalysis.
The VFDRC is an incremental classifier that shares some In summary, our methodology encompasses the selection
similarities with the HT classifier. Unlike a decision tree- ofdiversedatasets,theincorporationofconceptdriftdetec-
based classifier, it employs a collection of rules during the tion algorithms, the utilization of classification algorithms
model training process, called an incremental rule-learning with default parameter values, and a rationale prioritizing
algorithm.Thealgorithmishighlyinterpretable,likedecision rigorous and unbiased comparison. These methodological
trees in its model construction methodology. However, the considerations collectively form the foundation of our
algorithm does not implement adaptation techniques for investigationintotheeffectivenessofconceptdrifthandling
scenariosinvolvingconceptdriftoccurrences[25]. strategiesincontinuousdatastreams.
Importantly, parameter tuning to achieve better accuracy
h: ADDITIVEEXPERTENSEMBLECLASSIFIER(AEEC)OR wasintentionallyavoided,asthefocusofthisanalysisliesin
ALSO(ADDEXP) examiningtheperformanceofclassificationalgorithmsunder
AEECisanensemble-basedclassificationalgorithm,which thepresenceofconceptdriftratherthanaimingforthehighest
isageneralmethodappliedtoanyonlinelearningproblem. possible accuracy. This is in contrast to another analysis,
The classifier is designed to handle concept drift, making it detailed in the Results section, where specific concept drift
an essential tool for working with continuous data streams handling methods are evaluated on two distinct classifiers.
subjecttoconceptdriftoccurrences[26]. In this scenario, one of the classifiers employed is KNN,
configured with the following parameters: The number of
i: BATCHINCREMENTALENSEMBLECLASSIFIER(BIC) nearest neighbors was set to 8, the maximum size of the
TheBICisanincrementalensembleclassifier.Theclassifier window for storing the last observed samples was set to
incrementally constructs a set of model samples in batches 2,000 and the maximum number of samples that can be
for training. The algorithm uses a sample window to train stored in a leaf node, which determines the point at which
a model, and in this process, new batches are added to the thealgorithmswitchestoabrute-forceapproach,wassetto
ensemble.Inacontinuousdatastreamenvironment,toensure 40.Thisdual-levelanalysishighlightstheadaptabilityofthe
limitedmemoryconsumption,amaximumnumberofmodels proposedmethodsandoffersinsightsintotheirperformance
comprise the ensemble. When this number of models is acrossdiverseconfigurations.
exceeded, the algorithm removes the older training models, The results presented in this work are divided into
keepingthemup-to-datewiththemostrecentmodels. three stages. The first stage involves the implementation
of concept drift handling techniques separately from the
B. RESULTS employed classification algorithms. In other words, for
To analyze the performance of different classification and a given classifier, a concept drift detection algorithm is
detection algorithms implemented in this work, the use of employed. If this algorithm detects any suspicious change,
default parameter values was motivated by the objective of atechniqueisapplied,whichisdescribedasfollows:
ensuring a fair and impartial comparison among classifiers.
During training, the default parameters for classification • Ignore: If a concept drift is identified by the detection
algorithms were used, considering a batch size of 10,000 algorithms,noactionwillbetaken.
and a pretrain size of 1,000. Furthermore, for all datasets • Delete: Samples identified with concept drift by the
analyzed,thedetectionalgorithmsalsoutilizedtheirdefault detectionalgorithmswillbeexcluded.
61114 VOLUME13,2025

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
TABLE2. Conceptdriftdetectionalgorithms.
• Retrain: In case concept drift is identified, the system with algorithms that do not implement this treatment
willberetrainedwithallthesamples. approach. Finally, the third stage of results presents com-
• Batch Training: Training is performed based on a parisonsbetweenvariousclassifiersthatimplementconcept
packageofsamples,asubsetofthetotalsamples,aiming drift handling techniques. Some of these classifiers may
toadapttotheconceptdrift. not necessarily have techniques explicitly stated in their
The second stage utilizes classification algorithms that formulationbutarebasedonrobusttrainingtoconceptdrift
internally implement techniques for detecting and adapting deviations.Thisanalysisaimstoobservethebestalgorithms
toconceptdrifts.Itcomparestheseclassificationalgorithms in terms of performance by examining the algorithms and
VOLUME13,2025 61115

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
TABLE3. AccuracyofthemodelswhenperformingdifferenttreatmentmethodsontheSEA-abruptdataset.
TABLE4. AccuracyofthemodelswhenperformingdifferenttreatmentmethodsontheSEA-gradualdataset.
TABLE5. AccuracyofthemodelswhenperformingdifferenttreatmentmethodsontheElectricityMarketdataset.
TABLE6. AccuracyofthemodelswhenperformingdifferenttreatmentmethodsontheSEA-abruptdataset(KNN).
the data distribution. It may provide insights to identify observed based on the classifier model used. It is important
the best algorithms depending on data distribution, data to note that in this analytical phase, the classifiers do
sampling/collectingperiods,forexample. not incorporate concept drift treatment techniques. This
Forthisanalysis,diversedatasetswereemployed,incorpo- deliberate choice ensures the reliability of the evaluated
rating various concept drift detection algorithms. To ensure methods’outcomes.
a more comprehensive analysis, the experimentation was Naturally, a model that does not implement concept drift
extended to two distinct classifiers that do not incorporate treatmenttechniques,effectivelyignoringthem,shouldhave
techniques for addressing or adapting to concept drift itscomparativeanalysisinthetablesbasedonthemetricsof
occurrences. the (Ignore) treatment method. This approach allows for an
Tables 3, 4, and 5 exhibit the behavior of the machine assessmentoftheimpactofothertechniques.Asindicatedin
learning model when applying different concept drift treat- alltables,batchtrainingemergesasarobusttrainingmethod
menttechniquesupontheiridentification.InTables3to5,the inscenariosaffectedbyconceptdrift.
analysisemploystheHTclassifier,andtheutilizeddatasets Thereferencemetricsemployedintheanalysisarederived
are SEA-abrupt, SEA-gradual, and the Electricity Market, fromthemethodthatdisregardsconceptdrift,therebyestab-
respectively. lishingabenchmark againstwhichothertreatmentmethods
The subsequent Tables 6, 7, and 8 adhere to the same are compared. This provides a discernible framework to
analytical approach, altering the datasets to SEA-abrupt, assesstheefficacyofthealternativeapproaches.
SEA-gradual, and the Electricity Market, respectively. The Notably, in none of the instances did the exclusion of
only distinction lies in the classifier employed, where the samples significantly influence the model’s performance.
KNN(K-NearestNeighbors)classifierisused. This consistency indicates that removing samples does not
This classifier variation aims to assess whether different necessarily yield discernible benefits or detriments to the
outcomes in concept drift treatment methods could be model’sstability.
61116 VOLUME13,2025

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
TABLE7. AccuracyofthemodelswhenperformingdifferenttreatmentmethodsontheSEA-gradualdataset(KNN).
TABLE8. AccuracyofthemodelswhenperformingdifferenttreatmentmethodsontheElectricityMarketdataset(KNN).
Regarding the model retraining strategy, it is observed equippedwithconceptdrifthandlingtechniques.Theresults
that the outcomes exhibit a degree of variability. This is an ofthisassessmentareencapsulatedinFigure1.
anticipatedoutcomegiventhedynamicnatureofconceptdrift This endeavor arises from the recognition that a com-
and its varying impact on the model based on the evolving prehensive evaluation of model performance necessitates
datapatterns. considering a spectrum of potential scenarios encompass-
Therecurringinstancesofaccuracyimprovementresulting ing various concept drift manifestations. The contrasting
from batch training are noteworthy. This underscores the approaches of models that accommodate concept drift and
potency of processing larger data volumes in segments, thosethatdonotprovidevaluableinsightsintotheutilityof
allowing the model to adapt more adeptly to changing data suchadaptationmechanisms.
distributions. Enhancing the previous analysis of methods for handling
The exploration of combining these methods within concept drift and broadening the scope to encompass
ensembles is particularly intriguing. While the impact of classifiers integrating concept drift adaptation techniques,
individual techniques may not be markedly pronounced, the outcomes presented in Figure 1 underscore the superior
the amalgamation of diverse strategies could potentially performanceofclassifiersemployingconceptdrifthandling
overcome their individual limitations, leading to a more methods.
robust and consistently performing approach. This aligns Giventhesusceptibilityofthedatasetstoconceptdrift,the
withtherecognitionthatthesynergyofmethodsinensembles algorithm yielded results as anticipated, achieving elevated
might offer a valuable avenue for effective concept drift metrics including accuracy and precision, in contrast to
management. modelsdisregardingtheeffectsofdrift.
The comprehensive analysis of concept drift treatment Notably, in just one of the assessed datasets, the HAT
methods elucidates how distinct strategies influence model algorithmexhibitedslightlyinferiormetrics.Thishighlights
accuracy. Moreover, the exploration of ensembles hints thenotionthattheselectionofaclassificationalgorithmcan
at a promising avenue for future investigations. This leadtovariedbehaviors.
enriched understanding of effectively addressing concept Consequently,thesubsequentanalyticalphasewillencom-
drift within continuous data streams is a pivotal con- pass the evaluation of diverse classifier types, to unveil
tribution to advancing the domain of stream learning distinctbehaviorswithintheseclassifiercategories.Ournext
methodologies. experiment shown in Figure 2 illustrates the comparison
Given the imperative to comprehensively evaluate more of the effectiveness of various classification algorithms
comprehensive treatment models that intrinsically offer a implementing concept drift treatment techniques across
synthesis of the individually analyzed methods, the second differentdatasets.
segment of this analysis aims to assess the performance Analyzing the metrics obtained for the batch training
of machine learning models–one devoid of concept drift methodpresentedfromthetable3to8,itisevidentthat,inall
adaptation techniques, and the other endowed with such results,itwasthesuperiormethodintermsofaccuracy.Itis
mechanisms. importanttonotethat,dependingonthetypeofconceptdrift,
This investigation spans across eight distinct datasets, thismethodmaynotbethemostsuitable.
ensuringacomprehensiveexaminationofanarrayofconcept Considering batch training and analyzing the results
drift occurrences. The classifiers under scrutiny encompass presented in Figure 2, the BIC classification algorithm
HT, HAT, and EFDT, with HAT being the sole classifier stands out as an example of a method based on batch
VOLUME13,2025 61117

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
FIGURE1. Comparisonofclassificationmodelsindatastreamswithandwithoutconceptdrifthandlingacrossmultipledatasets.
training. According to the data presented in the tables, it is training plays a crucial role in this performance. To further
evident that this algorithm consistently achieved one of the substantiate this observation, we can analyze the AEEC
best performances across all test datasets, regardless of the algorithm, which is based on an ensemble but shows
type of concept drift affecting the data. Although it was highlyvariableperformance.Specifically,itdidnotperform
not the top-performing algorithm among those analyzed, well in scenarios involving gradual concept drift, while
it consistently demonstrated excellent metrics, highlighting it demonstrated good performance in abrupt concept drift.
its robustness and reliability. According to [10], ensemble This contrasts with the complementary nature of batch
training is one of the most used approaches. As a result of training combined with ensemble training (BIC), which
thiswork,itisobservedthatthecombinationofthisensemble performs favorably regardless of the type of concept drift
method with batch training (BIC) algorithm achieved good analyzed.
performance across all analyzed datasets under different Otheralgorithms,leveragingclassificationtechniquesand
typesofconceptdrift. treatments more tailored to the types of concept drift and
Althoughensemblelearningiswidelyused[10],itcannot data distribution, have demonstrated superiority. However,
be guaranteed that its superiority is specifically due to irrespective of this, algorithms based on batch training
being an ensemble. In the analysis presented here, the consistentlyexhibitedcommendablemetrics.
superiority is indeed attributed to the ensemble; however, A more in-depth analysis of the results about the SEA-A
when comparing it to the methods analyzed individually, dataset in Figure 2a, characterized by abrupt concept drifts,
as shown in the tables, it can be concluded that batch revealsthatdecisiontree-basedalgorithmsexhibitedsuperior
61118 VOLUME13,2025

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
FIGURE2. Comparisonoftheperformanceamongdifferentclassificationalgorithmsfordataaffectedbyconceptdrift.
performance.AsdetailedinthedefinitionofHATalgorithm, because, with this treatment approach, in the case of abrupt
the operation involves applying concept drift detection at concept drifts, the affected branch is promptly addressed
eachbranchofthedecisiontree.Naturally,wecaninferthat without impacting other branches, thus avoiding training
themodelcanadaptmoreswiftly,achievinghigherefficacy, delays.
VOLUME13,2025 61119

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
This analysis is consistent when examining the extending these methods, emphasizing their pivotal role in
SEA-Gradual dataset shown in Figure 2b, characterized creatingresilientmachinelearningsystemsforever-evolving
by gradual concept drifts and a longer window for data real-worlddataenvironments.
| observation. | Algorithms |     | such | as KNNADW, |     | with | a more |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | ---- | ---------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
extended window, allow for more accurate identification V. FUTUREWORKS
of this type of deviation when compared to decision tree- Ourstudyconductedanin-depthanalysisofthebehaviorof
basedalgorithms.Thisisduetotheanalysisineachbranch variousapproachestohandlingconceptdriftusingdifferent
beingmoretime-consumingbeforethedeviationisaccurately classifiers. One potential direction for future work is to
identified. extend this analysis to regression problems, which would
AnothernoteworthyalgorithmisVFDRC,whichisbased expand the scope of our findings and their applicability
on decision trees and does not implement methods to to a broader range of scenarios. Furthermore, evaluating
circumvent concept drifts once identified. However, it is additional classification algorithms not covered in this
an incremental training algorithm that naturally adapts the study could provide further insights and contribute to a
model to new incoming data. Once again, depending on morecomprehensiveunderstandingofconceptdrifthandling
| the type | of concept | drift | occurrence, |     | it may | not deliver | the | techniques. |     |     |     |     |     |     |
| -------- | ---------- | ----- | ----------- | --- | ------ | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
best performance. Nevertheless, upon analyzing the results Building on the analyses and observations made in this
obtained in Figure 2, it demonstrated remarkable metrics in study,anotherpromisingavenueforfutureresearchliesinthe
alltheanalyzeddatasets. developmentofspecializedalgorithmsforhandlingconcept
|     |     |     |     |     |     |     |     | drift. These        | algorithms | could      | be     | designed | to         | generalize |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | ---------- | ---------- | ------ | -------- | ---------- | ---------- |
|     |     |     |     |     |     |     |     | their effectiveness |            | regardless | of the | type     | of concept | drift      |
IV. CONCLUSION
This study conducted a comprehensive evaluation of clas- encountered, thereby addressing the limitations observed
sification algorithms implementing concept drift treatment, and contributing to advancements in the field. Additionally,
analyzing their performance across various datasets and futureworkcouldexplorehowthesemethodsperformwhen
scenarios.Bysystematicallyapplyingdifferentconceptdrift extendedtohandleconceptdriftindeeplearningmodelsand
detectionalgorithmsandexploringdiverseformsofdrift,this howtheyadapttodynamicenvironments,furtherenhancing
workprovidesanempiricalbenchmarkthathighlightscritical theirapplicabilityinreal-worldscenarios.
insightsforpractitionersandresearchers.
One significant finding is the effectiveness of a training ACKNOWLEDGMENT
method that employs a sliding data window, leading to For open access purposes, the authors have assigned the
notableperformanceimprovementswithoutalteringthedata. creativecommonsCCBYlicensetoanyacceptedversionof
| This approach |      | was consistent |               | across | various   | classification |     | thearticle. |     |     |     |     |     |     |
| ------------- | ---- | -------------- | ------------- | ------ | --------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| and detection |      | methods,       | offering      | a      | versatile | solution       | for |             |     |     |     |     |     |     |
| dynamic       | data | environments.  | Additionally, |        | while     | exclusion      |     | REFERENCES  |     |     |     |     |     |     |
techniquesdidnotenhanceaccuracy,theydemonstratedthe [1] J.Lu,A.Liu,F.Dong,F.Gu,J.Gama,andG.Zhang,‘‘Learningunder
potentialforreducingstorageandcomputationalcostswith- conceptdrift:Areview,’’IEEETrans.Knowl.DataEng.,vol.31,no.12,
pp.2346–2363,Dec.2019.
| out compromising |     | performance–an |     | essential |     | consideration |     |                                                           |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | --------- | --- | ------------- | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                  |     |                |     |           |     |               |     | [2] E.Ahmed,I.Yaqoob,M.Hashem,I.Khan,A.I.A.Ahmed,M.Imran, |     |     |     |     |     |     |
forresource-constrainedsystems.
andA.V.Vasilakos,‘‘TheroleofbigdataanalyticsinInternetofThings,’’
Comput.Netw.,vol.129,pp.459–471,Jun.2017.
| The study       | also | revealed   | that | combining   |     | these strategies |     |                                                                     |     |     |     |     |     |     |
| --------------- | ---- | ---------- | ---- | ----------- | --- | ---------------- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                 |      |            |      |             |     |                  |     | [3] J.Tetteroo,M.Baratchi,andH.H.Hoos,‘‘Automatedmachinelearningfor |     |     |     |     |     |     |
| within ensemble |      | frameworks |      | can amplify |     | their strengths, |     |                                                                     |     |     |     |     |     |     |
COVID-19forecasting,’’IEEEAccess,vol.10,pp.94718–94737,2022.
| yielding | higher | adaptability |     | and robustness |     | in dynamic |     |                                                                |     |     |     |     |     |     |
| -------- | ------ | ------------ | --- | -------------- | --- | ---------- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|          |        |              |     |                |     |            |     | [4] T.Escovedo,A.Koshiyama,A.A.daCruz,andM.Vellasco,‘‘DetectA: |     |     |     |     |     |     |
settings. These results underscore the practical implications Abruptconceptdriftdetectioninnon-stationaryenvironments,’’Appl.Soft
Comput.,vol.62,pp.119–133,Jan.2018.
| of choosing | appropriate |     | concept | drift | handling | techniques |     |              |                |           |                 |     |     |               |
| ----------- | ----------- | --- | ------- | ----- | -------- | ---------- | --- | ------------ | -------------- | --------- | --------------- | --- | --- | ------------- |
|             |             |     |         |       |          |            |     | [5] J. Gama, | I. Žliobaite˙, | A. Bifet, | M. Pechenizkiy, |     | and | A.Bouchachia, |
basedonspecificapplicationneeds.
‘‘Asurveyonconceptdriftadaptation,’’ACMComput.Surv.,vol.46,no.4,
This comparative analysis not only sheds light on the pp.1–37,Apr.2014.
nuances of existing methods but also bridges the gap [6] N. A. Syed, H. Liu, and K. K. Sung, ‘‘Handling concept drifts
|     |     |     |     |     |     |     |     | in incremental |     | learning with | support vector | machines,’’ |     | in Proc. 5th |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | -------------- | ----------- | --- | ------------ |
betweentheoreticaladvancementsandpracticalapplications. ACM SIGKDD Int. Conf. Knowl. Discovery Data mining, Aug. 1999,
Byprovidingadetailedexplorationofalgorithmperformance pp.317–321.
andtrade-offs,thestudyequipspractitionerswithactionable [7] S. Wares, J. Isaacs, and E. Elyan, ‘‘Data stream mining: Methods and
|          |          |                 |     |            |     |          |        | challenges | for | handling concept | drift,’’ | Social Netw. | Appl. | Sci., vol. 1, |
| -------- | -------- | --------------- | --- | ---------- | --- | -------- | ------ | ---------- | --- | ---------------- | -------- | ------------ | ----- | ------------- |
| insights | to guide | their selection |     | of methods |     | tailored | to the |            |     |                  |          |              |       |               |
no.11,pp.1–19,Nov.2019.
natureoftheirdatasetsanddriftscenarios. [8] Z.Liu,R.Godahewa,K.Bandara,andC.Bergmeir,‘‘Handlingconcept
|             |     |          |          |     |          |            |     | drift in | global | time series | forecasting,’’ | in Forecasting |     | With Artificial |
| ----------- | --- | -------- | -------- | --- | -------- | ---------- | --- | -------- | ------ | ----------- | -------------- | -------------- | --- | --------------- |
| Ultimately, | the | findings | reaffirm | the | critical | importance |     |          |        |             |                |                |     |                 |
Intelligence:TheoryandApplications.Cham,Switzerland:Springer,2023,
| of addressing |     | concept | drift in | machine | learning. |     | Models |     |     |     |     |     |     |     |
| ------------- | --- | ------- | -------- | ------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
pp.163–189.
| that incorporate |            | effective | drift         | management | techniques |     | con-    |                                                                      |         |           |               |      |       |                |
| ---------------- | ---------- | --------- | ------------- | ---------- | ---------- | --- | ------- | -------------------------------------------------------------------- | ------- | --------- | ------------- | ---- | ----- | -------------- |
|                  |            |           |               |            |            |     |         | [9] L.Baier,J.Reimold,andN.Kühl,‘‘Handlingconceptdriftforpredictions |         |           |               |      |       |                |
|                  |            |           |               |            |            |     |         | in business                                                          | process | mining,’’ | in Proc. IEEE | 22nd | Conf. | Bus. Informat. |
| sistently        | outperform | static    | counterparts, |            | achieving  |     | greater |                                                                      |         |           |               |      |       |                |
(CBI),vol.1,Jun.2020,pp.76–83.
| accuracy | and | adaptability | over | time. | This | work | lays a |                                                                    |     |     |     |     |     |     |
| -------- | --- | ------------ | ---- | ----- | ---- | ---- | ------ | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|          |     |              |      |       |      |      |        | [10] A.S.IwashitaandJ.P.Papa,‘‘Anoverviewonconceptdriftlearning,’’ |     |     |     |     |     |     |
foundation for future research aimed at optimizing and IEEEAccess,vol.7,pp.1532–1547,2019.
| 61120 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

E.V.Pereira,W.S.daSilva:ComparisonofApproachesforHandlingConceptDrifts
[11] H. M. Gomes, A. Bifet, J. Read, J. P. Barddal, F. Enembreck, EMANUELVALÉRIOPEREIRA(Member,IEEE)
B.Pfharinger,G.Holmes,andT.Abdessalem,‘‘Adaptiverandomforests receivedthebachelor’sdegreeincomputerengi-
forevolvingdatastreamclassification,’’Mach.Learn.,vol.106,nos.9–10, neering from the Federal University of Ceará
pp.1469–1495,Oct.2017. (UFC),whereheiscurrentlypursuingtheGrad-
[12] J. A. Blackard and D. J. Dean, ‘‘Comparative accuracies of artificial uate degree with the Electrical and Computer
neuralnetworksanddiscriminantanalysisinpredictingforestcovertypes
EngineeringProgram.Hehasconductedresearch
fromcartographicvariables,’’Comput.Electron.Agricult.,vol.24,no.3,
inthefieldofimageprocessingandiscurrently
pp.131–151,Dec.1999.
|     |     |     |     |     |     |     |     | focused | on investigating | data | drift and | resource |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | ---- | --------- | -------- |
[13] M.Harries,‘‘Splice-2comparativeevaluation:Electricitypricing,’’School
|     |     |     |     |     |     |     |     | allocation | for | mobile communication |     | systems. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------------- | --- | -------- |
Comput.Sci.Eng.,Univ.NewSouthWales,Sydney,NSW,Australia,Tech.
Rep.,1999.[Online].Available:https://nla.gov.au/nla.cat-vn3513275 Additionally,heholdsatechnicalqualificationin
computernetworks.
| [14] V. Losing, | B.  | Hammer, | and H. | Wersing, ‘‘KNN | classifier | with self |     |     |     |     |     |     |
| --------------- | --- | ------- | ------ | -------------- | ---------- | --------- | --- | --- | --- | --- | --- | --- |
adjustingmemoryforheterogeneousconceptdrift,’’inProc.IEEE16th
Int.Conf.DataMining(ICDM),Dec.2016,pp.291–300.
| [15] R. Elwell | and | R. Polikar, | ‘‘Incremental | learning | of concept | drift in |     |     |     |     |     |     |
| -------------- | --- | ----------- | ------------- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
nonstationaryenvironments,’’IEEETrans.NeuralNetw.,vol.22,no.10,
pp.1517–1531,Oct.2011.
| [16] J. Montiel, | J.  | Read, A. | Bifet, and | T. Abdessalem, | ‘‘Scikit-multiflow: |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | ---------- | -------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
Amulti-outputstreamingframework,’’J.Mach.Learn.Res.,vol.19,no.1,
pp.2914–2915,2018.
| [17] A. Bifet | and | R. Gavaldà, | ‘‘Learning | from | time-changing | data with |     |     |     |     |     |     |
| ------------- | --- | ----------- | ---------- | ---- | ------------- | --------- | --- | --- | --- | --- | --- | --- |
adaptivewindowing,’’inProc.SIAMInt.Conf.DataMining,Apr.2007,
|     |     |     |     |     |     |     |     | WENDLEY |     | SOUZA DA | SILVA received | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | -------------- | --- |
pp.443–448.
|     |     |     |     |     |     |     |     | bachelor’s | degree | in telematics, | with a | focus on |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | -------------- | ------ | -------- |
[18] J.Gama,P.Medas,G.Castillo,andP.P.Rodrigues,‘‘Learningwithdrift
informaticsfromIFCE,in2006,thedegreeinedu-
detection,’’inProc.17thBrazilianSymp.Artif.Intell.Cham,Switzerland:
cationfromSenac-RJ,in2007,themaster’sdegree
Springer,Jan.2004,pp.286–295.
[19] M.Baena-Garcıa,J.D.Campo-Ávila,R.Fidalgo,A.Bifet,R.Gavaldà, in teleinformatics engineering from the Federal
andR.Morales-Bueno,‘‘Earlydriftdetectionmethod,’’inProc.4thInt. UniversityofCeará(UFC),Sobral,in2010,and
WorkshopKnowl.DiscoveryDataStreams,vol.6,2006,pp.77–86. thePh.D.degreeincomputersciencefromUFMG,
[20] I. Frías-Blanco, J. del Campo-Ávila, G. Ramos-Jiménez, in2020.
R.Morales-Bueno, A. Ortiz-Díaz, and Y. Caballero-Mota, ‘‘Online Hecompletedhispostdoctoralfellowshipwith
and non-parametric drift detection methods based on hoeffdingâăźs the Department of Computing, MDCC, UFC,
bounds,’’ IEEE Trans. Knowl. Data Eng., vol. 27, no. 3, pp.810–823, in 2022, where he has been an Associate Professor 4, teaching in the
Mar.2015. computerengineeringcourses,since2007.Hisacademicjourneyismarked
[21] E.S.Page,‘‘Continuousinspectionschemes,’’Biometrika,vol.41,no.1, bysignificantachievements,includingthePh.D.degreeandhispostdoctoral
pp.100–115,Jun.1954. fellowshipwithMDCC,UFC,wherehiscurrentpositionasanAssociate
[22] A. Bifet and R. Gavaldà, ‘‘Adaptive learning from evolving data Professor.Specializinginthefieldofcomputerscience,hiscurrentresearch
streams,’’inProc.8thInt.Symp.Intell.DataAnal.,Lyon,France.Cham,
|     |     |     |     |     |     |     | interests include | the Internet | of Things, | 5G, e-Health, | applications | of  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------ | ---------- | ------------- | ------------ | --- |
Switzerland:Springer,Jan.2009,pp.249–260.
machinelearning,andcloudcomputing.
[23] C.Manapragada,G.I.Webb,andM.Salehi,‘‘Extremelyfastdecision
|         |          |          |        |            |        |                | Dr. da Silva          | has made | substantial | contributions | to academia, | with      |
| ------- | -------- | -------- | ------ | ---------- | ------ | -------------- | --------------------- | -------- | ----------- | ------------- | ------------ | --------- |
| tree,’’ | in Proc. | 24th ACM | SIGKDD | Int. Conf. | Knowl. | Discovery Data |                       |          |             |               |              |           |
|         |          |          |        |            |        |                | a notable publication | record   | in esteemed | conferences   | and          | journals. |
Mining,Jul.2018,pp.1953–1962.
[24] Z.Ouyang,M.Zhou,T.Wang,andQ.Wu,‘‘Miningconcept-driftingand Throughouthiscareer,hehasservedasanevaluator/reviewerfornumerous
conferences,includingInternationalConferenceonSystemsandNetworks
noisydatastreamsusingensembleclassifiers,’’inProc.Int.Conf.Artif.
|     |     |     |     |     |     |     | Communications | (ICSNC), | International | Conference | on Network | and |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ------------- | ---------- | ---------- | --- |
Intell.Comput.Intell.,vol.4,Nov.2009,pp.360–364.
ServiceManagement(CNSM),Halifax,Canada,InternationalConference
[25] P.KosinaandJ.Gama,‘‘Veryfastdecisionrulesforclassificationindata
onNetworksoftheFuture(NoF),IEEELatinAmerica,EATIS,Wireless
| streams,’’ | Data | Mining Knowl. | Discovery, | vol. | 29, no. | 1, pp.168–202, |     |     |     |     |     |     |
| ---------- | ---- | ------------- | ---------- | ---- | ------- | -------------- | --- | --- | --- | --- | --- | --- |
Jan.2015. Communications and Networking Conference (WCNC), CA, USA, and
[26] J. Z. Kolter and M. A. Maloof, ‘‘Using additive expert ensembles to IEEEConsumerCommunicationsandNetworkingConference(CCNC),Las
| copewithconceptdrift,’’inProc.22ndInt.Conf.Mach.Learn.,2005, |     |     |     |     |     |     | Vegas,USA. |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
pp.449–456.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 61121 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |