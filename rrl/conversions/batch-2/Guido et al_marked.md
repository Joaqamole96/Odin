---
conversion_metadata:
  converted_at: "2026-07-21T06:17:16Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Guido et al.pdf"
  source_pdf_sha256: "dad8c3b45acb2a76d1cc90ea36160db578f42bd49525a2da41ad9ad5cb022ade"
  page_count: 19
  markdown_char_count: 93672
---

SoftComputing(2023)27:12863–12881
https://doi.org/10.1007/s00500-022-06768-8
FOCUS
A hyper-parameter tuning approach for cost-sensitive support vector
machine classifiers
Rosita Guido1 ·Maria Carmela Groccia1·Domenico Conforti1
Accepted:10January2022/Publishedonline:2February2022
©TheAuthor(s)2022
Abstract
Inmachinelearning,hyperparametertuningisstronglyusefultoimprovemodelperformance.Inourresearch,weconcentrate
ourattentiononclassifyingimbalanceddatabycost-sensitivesupportvectormachines.Weproposeamulti-objectiveapproach
that optimizes model’s hyper-parameters. The approach is devised for imbalanced data. Three SVM model’s performance
measuresareoptimized.Wepresentthealgorithminabasicversionbasedongeneticalgorithms,andasanimprovedversion
based on genetic algorithms combined with decision trees. We tested the basic and the improved approach on benchmark
datasetseitherasserialandparallelversion.Theimprovedversionstronglyreducesthecomputationaltimeneededforfinding
optimizedhyper-parameters.Theresultsempiricallyshowthatsuitableevaluationmeasuresshouldbeusedinassessingthe
classificationperformanceofclassificationmodelswithimbalanceddata.
Keywords Multi-objectiveoptimization·Supportvectormachine·Hyper-parameteroptimization·Imbalanceddatasets·
Geneticalgorithms
1 Introduction can significantly affect the resulting model’s performance.
Generally,hyper-parametersareadjustedforeachmodelin
Classification problems may be encountered in different order to find a hyper-parameter setting that maximizes the
domains.Oneoftheseisthediseasediagnosis,whichestab- model performances and so that the ML model can predict
lishesthepresenceorabsenceofagivendiseaseaccording unknowndataaccurately.Thegoalofhyper-parameteropti-
toreferredsymptomsandresultsofmedicalexams.Machine mizationistofindasetofvaluesthatminimizesapredefined
learning approaches can be employed to support experts in lossfunction.
diseases diagnosis. Many researches aim to propose new Usually, a good set of hyper-parameters are determined
methods to improve or enhance the outcomes of existing by a grid search. The grid search strategy is based on
ones. testingallhyper-parametercombinationsspecifiedinamulti-
Support vector machines (SVM) are one of the best dimensional grid. During the search, the hyper-parameters
machine learning (ML) models for solving several real-life arevaried,withfixedstep-size,inagivenrangeofvalues.The
classificationproblems(Vapnik1998;CristianiniandShawe- performanceofacombinationofhyperparametersisevalu-
Taylor2000).Thechoiceofhyper-parametersofaMLmodel atedusingaperformancemetric.Theconfigurationwiththe
bestperformanceisselectedandusedtotraintheMLmodel
CommunicatedbyDarioPacciarelli. on the whole dataset. However, this kind of search is very
B timeconsuminganditissuitablefortheadjustmentoffew
RositaGuido
hyper-parameters.
rosita.guido@unical.it
Another big challenge in data mining that is attracting
MariaCarmelaGroccia
increasing interest of researchers is dealing with imbal-
mariacarmela.groccia@unical.it
anceddatasets(JapkowiczandStephen2002).Adatasetis
DomenicoConforti
imbalancedwhenoneormoreclasseshaveverylowpropor-
domenico.conforti@unical.it
tions in the data as compared to the other classes. The first
1 DepartmentofMechanical,EnergyandManagement class is called as minority class with respect to the major-
Engineering,UniversityofCalabria,PontePietroBucci, ity class(ess). The main interest is in correctly classifying
87036Rende,Cosenza,Italy
123

12864 R.Guidoetal.
theminorityclass.Theexistingmethodsforclassificationof tormachinesanddecisiontreesinSect.3,anddiscusssome
imbalanceddatacanbecategorizedasalgorithm-levelcate- metrics commonly used to evaluate model performance. In
gory,data-levelcategory,andcost-sensitivemethodsthatlie Sect. 4, we introduce multi-objective optimization prob-
between the above two categories (Galar et al. 2012). The lems and the Non-dominated Sorting Genetic Algorithm-II
firstcategoryincludesmethodsmodifiedordesignedtohan- (NSGA-II). In Sect. 5, we detail our approach that com-
dleimbalanceddata;thesecondcategoryincludesmethods bines genetic algorithms and a heuristic procedure based
that try to transform data in order to balance classes and on decision tree in order to find optimal hyper-parameters.
usethenstandardclassificationalgorithms.Down-sampling Threeobjectivefunctionsareoptimized.Weperformseveral
approaches,whichreducethemajorityclassinthetraining computationalexperimentsaimedatfindingthebesthyper-
subset, and over-sampling approaches, which increase the parametertuningforsixbenchmarkdatasets.Thebestresults
size of the minority class in the training subset, belong to alongwithadiscussionandcomparisonwithotherresultsof
this category. Finally, the third category includes methods theliteraturearereportedinSect.6.Finally,theconclusions
designedforweightingdifferentlytheclassesbyintroducing aregiveninSect.7.
misclassificationcosts.
Itisimportanttopointoutthatthemostcommonlyused
modelevaluationmetricistheaccuracy.However,itcanbe 2 Relatedworkonimbalanceddata
verymisleadingwhendataareimbalanced.Insuchcases,dif- classificationandcost-sensitivelearning
ferentevaluationmetricsshouldbeconsidered.Wetestedin problems
(Guidoetal.2021)twoevaluationmodelmetrics,i.e.,accu-
racy and G-Mean, on two imbalanced benchmark datasets LetD ={(x ,y ),(x ,y ),...,(x ,y)},beadatasetwhere
1 1 2 2 l l
byoptimizinghyper-parametersofsupportvectormachines x ∈ (cid:3)L is a pattern (even called example) drawn from a
i
by genetic algorithms (GAs). Comparing the results, we domainX andy ∈Y isitsrelatedclasslabel.Anexampleis
i
observedempiricallythatG-Meanismoresuitablethanaccu- thusavector.Inabinaryclassificationdomain,anexample
racy to evaluate model performance in case of imbalanced canbeeitherpositive,denotedbyalabely =1,ornegative,
data, especially when data refers to medical domains, like denotedbyy =−1.Generally,thegoalofabinaryclassifier
diagnosis. The results encouraged us to continue exploring is to map feature vectors x ∈ X to class labels y ∈ {±1}.
thisresearchfield. In terms of functions, a classifier can be written as h(x) =
This research paper addresses the optimal hyper- sign[p(x)],wherethefunction p : X → Risdenotedasthe
parameters problem as a multi-objective problem. It has a classifierpredictor.
twofoldcontribution: Classifiers generally perform poorly on imbalanced
datasets and, as a consequence, often they classify almost
1. The main goal is to investigate methods for improving all instances as negative. In recent years, imbalanced data
hyper-parameter tuning of SVM. We propose a novel classificationhasbeenstudiedbymanyresearcherswithdif-
approach for optimal hyper-parameter tuning that con- ferentmethods(JoandJapkowicz2004;Galaretal.2012).
sists of a genetic algorithm combined with a decision These methods can be distinguished into two categories
tree.Thebasicideaisthatsomechromosomesaresimilar basedondataandalgorithms.Data-basedmethodsfocuson
among them and they have thus the same fitness value. datapre-processingtoreduceimbalanceddata.Forinstance,
A decision tree (DT), trained in a suitable manner, is up-samplingandunder-samplingaretwomethodsthatmod-
exploitedtoreducethenumberofk-foldcross-validation ifyinstancedistribution.Up-samplingmethodsincreasethe
tobeperformedandthustheoverallcomputationaltime. minoritysamples,whereasunder-samplingmethodsreduce
As we will see, GAs were chosen even because they the majority samples. Synthetic Minority Oversampling
allowforaneasyparallelizationoftheproblem,whichis Techniqueisanoversamplingmethodthatbalancesdataby
tremendouslyhelpful.TheapproachthatcombinesGAs generatingnewsamplessimilartotheminoritysamplesand
andDTstronglyreducestheoverallcomputationaltime, theirneighbors(Chawlaetal.2002).
asdescribedinSect. 5. Hereafter,apositiveinstancebelongstotheminorityclass,
2. It focuses on testing and optimizing, at the same time, whereas a negative instance to the majority class. In many
more suitable performance measures in addition to the real-world applications, misclassifications may have differ-
accuracy. This is important for application domains entcosts,suchasforinstancediseasediagnosisandbusiness
whereonedataclassisofmoreinterestthanothers. decision making. The related classification problem, called
cost-sensitivelearningproblem,aimsatminimizingthetotal
Thepaperisstructuredasfollows.Ashortreviewofthe misclassificationcosts.Theissueofclassifyingimbalanced
state-of-the-artoftheliteraturefocusingonimbalanceddata databyanSVMwasaddressedin(Veropoulosetal.1999)by
setsisinSect. 2.Wegiveashortdescriptionofsupportvec- abiased-SVM.Thismethodusestwopenaltycoefficientsfor
123

Ahyper-parametertuningapproach... 12865
misclassifiedpositiveinstancesandnegativeinstances.Since ing kernel allows better discrimination in the feature space
the positive instances usually belong to the minority class, thanthatofasingleRBFkernel.
theusedpenaltycoefficientforthisclassisbiggerthanthe Oneofthefirstresearchpapersoncost-sensitiveapproach
penaltycoefficientassociatedwiththemajorityclass.Inthis tackledwithanevolutionaryprocessisduetoTurney(1995).
way, the SVM classifier aims at reducing misclassification Recently,Noiaetal.(2020)appliedSVM,k-NearestNeigh-
rateoftheminorityclass. bors and k-means as clustering techniques to predict the
The performance of an SVM model even depends, for probabilityofcontractingagivendiseasestartingfromboth
instance,ontheusedkernelfunction,whichmapsinstances- workplace-related(usingAtecoandIstatcodes)andworker-
vectorsfromtheoriginalinputspacetohigherdimensional related characteristics (i.e., age at hiring, age at disease
spacestodealwithnonlinearlyseparabledata(Scholkopfand certification,gender,employmentduration).TheyusedaGA
Smola2001).Accordingly,twoparametersofSVM,i.e.,C to find the best values of the used methods. Misclassifica-
andthekernelparameterwerefoundbyanexhaustivesearch tionerrorrateisusedasfitnessfunction.However,sincethe
approachin(Mehrbakhshetal.2019).Iranmehretal.(2019) classeswerenotevenlydistributedamongtheinstances,they
extended the SVM with cost-sensitive learning consider- usedasecondfitnessfunctionthatreducesthemisclassifica-
ingexampledependentcosts.Theyperformedexperimental tionerrorrateoftheminorityclass.
analysis on class imbalance, cost-sensitive learning with Anexhaustive searchofpapers addressingevaluation of
a given class and example costs and showed that their ML algorithms on classification is due to Sokolova et al.
proposedalgorithmprovidessuperiorgeneralizationperfor- (2006). These authors showed that the clear “leaders” are
mance compared to conventional methods. Qi et al. (2013) thosepapersinwhichevaluationisperformedondatafrom
proposedanewCost-SensitiveLaplacianSVMandtestedits the UCI repository, in biomedical and medical sciences,
effectivenessviaexperimentsonpublicdatasets.Theyeval- visual and text classification, and language applications.
uate the algorithms performance by the Average Cost. Tao Themostusedevaluationmeasuresareaccuracy,precision,
et al. (2019) developed a novel self-adaptive cost weights- recall, F-score, and the Receiver Operating Characteristic
| basedSVMcost-sensitiveensembleforimbalanceddatasets |        |     |          |            |              | (ROC). |     |     |     |
| --------------------------------------------------- | ------ | --- | -------- | ---------- | ------------ | ------ | --- | --- | --- |
| classification                                      | tasks. | The | approach | was tested | on synthetic |        |     |     |     |
datasetsandonpublicdatasetsshowinghigherclassification
3 Learningmodelclassifiers
| accuracy | than | the other | existing | imbalanced | classification |     |     |     |     |
| -------- | ---- | --------- | -------- | ---------- | -------------- | --- | --- | --- | --- |
methodsintermsofG-MeanandF-Measure.
Weoptimizehyper-parametersofSVMclassifierswithGaus-
Evolutionaryalgorithmsareflexibleandcommonlyused
siankernelinordertocorrectlycompareourresultsfoundon
| for a plethora |     | of machine | learning | problems | and tasks |     |     |     |     |
| -------------- | --- | ---------- | -------- | -------- | --------- | --- | --- | --- | --- |
publicandwell-knowndatasetswiththosereportedinthelit-
| (Bergstra | et al. | 2011; Goldberg | and | Holland | 1988). Evolu- |     |     |     |     |
| --------- | ------ | -------------- | --- | ------- | ------------- | --- | --- | --- | --- |
erature.Ourapproach,asitisbetterdetailedinSect.5,trains
tionaryoptimization-basedtechniquessolvethefilterdesign
|         |                 |     |          |      |                   | and uses random | trees to reduce | the | overall computational |
| ------- | --------------- | --- | -------- | ---- | ----------------- | --------------- | --------------- | --- | --------------------- |
| task as | an optimization |     | problem. | They | are used success- |                 |                 |     |                       |
time.
| fully in  | different | real-world | optimization |     | problems related |                  |            |           |                  |
| --------- | --------- | ---------- | ------------ | --- | ---------------- | ---------------- | ---------- | --------- | ---------------- |
|           |           |            |              |     |                  | In this section, | we briefly | introduce | SVM and decision |
| to Finite | Impulse   | Response   | (FIR)        | and | Infinite Impulse |                  |            |           |                  |
trees.Thus,wereportthemostusedperformancemetricsofa
Response(IIR)digitalfiltersdesign.Thegoalistominimize
MLmodelanddiscusstheirsuitabilityincaseofimbalanced
anerrorfunctionthatquantifiesdeviationbetweenafilterand
datasets.
adesiredresponse.Thiserrorisreducedbyupdatingitera-
tivelyasetoffiltercoefficientssuchthatgivenspecifications 3.1 Supportvectormachine
| are met. | Dwivedi | et al. | (2018) provided |     | a comprehensive |     |     |     |     |
| -------- | ------- | ------ | --------------- | --- | --------------- | --- | --- | --- | --- |
reviewofthevariousevolutionaryoptimization-basedtech- TheSVMwasintroducedbyCortesandVapnik(1995)and
niquesforFIRfilterdesign.ApproachestodesignIIRfilters isbasedonstatisticallearningtheory(Vapnik1998).SVMs
basedonevolutionarytechniqueswereproposedin(Agrawal are a class of algorithms for classification, regression and
et al. 2018, 2017). Evolutionary algorithms are even used otherapplications(CristianiniandShawe-Taylor2000)and
to automatically tune several parameters. Lessmann et al. theyareamongthemostusedMLtechniques.
|     |     |     |     |     |     |     |     |     | = (x ,...,x ), |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- |
(2005)usedaGAinordertotuneSVMs.Phienthrakuland Let X, be a dataset with L instances X 1 L
Kijsirikul(2010)improvedtheaccuracyofSVMbyanon- where x ∈ (cid:3)m, denotes an instance with m features, and
i
|                                                   |     |     |     |     |     | ∈ {±1}itslabel,i | = 1,...,L.Inabinaryclassification |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ---------------- | --------------------------------- | --- | --- |
| linearcombinationofmultipleRBFkernelstoobtainmore |     |     |     |     |     | y i              |                                   |     |     |
flexible kernel functions. The hyperparameters are chosen problem, an SVM basically searches for an optimal hyper-
byanevolutionarystrategywheretheobjectivefunctionsare planethatseparatespatternsofthetwoclassesbymaximizing
basedontrainingaccuracy,boundingofgeneralizationerror, themarginw ∈(cid:3)m.Findingtheoptimalhyperplanemeans
andsubsetcross-validationontrainingaccuracy.Theresult- solvingthequadraticprogrammingmodel(1)-(3),whichis
knownassoft-marginSVM
123

| 12866        |          |     |     |     |     |      |          |     |          | R.Guidoetal. |     |
| ------------ | -------- | --- | --- | --- | --- | ---- | -------- | --- | -------- | ------------ | --- |
|              | (cid:2)L |     |     |     |     | (wTx | +b)≥1−ξ  |     | =1,...,L |              |     |
| 1            |          |     |     |     |     | y i  |          |     | i i      |              | (5) |
| min ||w||2+C |          | ξ   |     | (1) |     |      |          |     |          |              |     |
|              |          | i   |     |     |     | ξ ≥0 | =1,...,L |     |          |              |     |
| 2            |          |     |     |     |     | i    | i        |     |          |              | (6) |
1
| (wTφ(x )+b)−1+ξ |     | ≥0  | =1,...,L |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| y i i           |     | i   | i        | (2) |     |     |     |     |     |     |     |
Observethatthecostmatriceshasthediagonalelements
ξ ≥0 =1,...,L
| i i |     |     |     | (3) |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aszero—becauseoftheassumptionthatacorrectclassifica-
tionhasnocost—andtheoff-diagonalelementsarepositive
| where C, named | penalty | parameter, | is a trade-off | between |          |          |     |       |                  |     |        |
| -------------- | ------- | ---------- | -------------- | ------- | -------- | -------- | --- | ----- | ---------------- | --- | ------ |
|                |         |            |                |         | numbers. | However, | the | range | of possibilities | for | CS-SVM |
thesizeofthemarginofseparationwandthetrainingerrors
hyper-parametercanbehuge.
ξ;b isthebiasanditindicatestheoffsetofthehyperplane
|     |     |     |     |     | Datta | and | Das (2015) | proposes | a Near-Bayesian |     | Sup- |
| --- | --- | --- | --- | --- | ----- | --- | ---------- | -------- | --------------- | --- | ---- |
from the origin. Constraints (2) state that when a training portVectorMachine(NBSVM)forimbalancedclassification
| example x | lies on the | wrong side | of the hyperplane, | the |                                                    |     |     |     |     |     |     |
| --------- | ----------- | ---------- | ------------------ | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| i         |             |            |                    |     | problemsbycombiningdecisionboundaryshiftandunequal |     |     |     |     |     |     |
correspondingslackvariableξ
i isgreaterthan1.Smallvalues regularization costs. Extensive comparison with standard
ofCincreasethetrainingerrors,whereaslargervaluesbring
|     |     |     |     |     | SVM | and some | state-of-the-art |     | methods | is furnished | as a |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------- | ------------ | ---- |
it closer to the hard-margin SVM. In case of nonlinearly proofoftheabilityoftheNBSVMtoperformcompetitively
| separable datasets, | the | SVM basically | maps | input vectors |     |     |     |     |     |     |     |
| ------------------- | --- | ------------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
onimbalanceddatasets.
intohigh-dimensionalfeaturespacesbytheso-calledkernel
functions(Hofm(cid:3)annetal.200(cid:4)8).Akernelfunction,denoted
3.2 Decisiontree
| asK(x ,x )= | φ(x | ),φ(x ),isaninnerproductinafeature |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| i j         | i   | j                                  |     |     |     |     |     |     |     |     |     |
spacewhereitmeasuressimilaritybetweenanypairofinputs
Adecisiontreeisasupervisedlearningalgorithmforregres-
x i and x j .Akernelfunctioncantakemanydifferentforms
sionandclassificationproblems(Breimanetal.1984)andis
(Hofmannetal.2008),suchas
themostpopularformofrule-basedclassifiers(Wittenand
Frank2005).Ithasasetofelementscallednodesandisbuilt
| •   | K(x | ,x )=(xTx | )d  |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Linearkernel i j j top-down from a root node. Each node represents a single
i
| • Polynomialkernel |     | K(x ,x )=(xTx | +a)d |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
i j i j inputattribute:leafnodescontainanoutputattribute,which
| •   |     |     | K(x | ,x ) = |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Radial Basis Function (RBF) kernel i j isusedtomakeaprediction;theothernodesaresplitpoints
| exp(−γ(cid:6)x | −x  | (cid:6)2) |     |     |                                                       |            |                   |     |              |         |       |
| -------------- | --- | --------- | --- | --- | ----------------------------------------------------- | ---------- | ----------------- | --- | ------------ | ------- | ----- |
|                | i j |           |     |     | ofanattribute.Thedataispartitionedintohomogeneoussub- |            |                   |     |              |         |       |
|                |     |           |     |     | sets,                                                 | i.e., they | contain instances |     | with similar | values. | Given |
The decision function, i.e., the classifier, is specified by a a new input, the tree is traversed by evaluating the specific
subset of training instances, the so-called support vectors, inputstartedattherootnodeofthetree.
thataretheonlyvectorsthat“support”theoptimalseparating
hyperplane.
3.3 Performanceevaluationandsomelimitations
| It is well | known that | the performance | of most | machine |     |     |     |     |     |     |     |
| ---------- | ---------- | --------------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
learningalgorithmsonagivendatasetdependsonwell-tuned
|     |     |     |     |     | To estimate |     | the generalization |     | performance | of  | an SVM |
| --- | --- | --- | --- | --- | ----------- | --- | ------------------ | --- | ----------- | --- | ------ |
hyper-parameter.InsettingupanSVMmodel,forinstance, model, generally one evaluates accuracy measure on data
twoproblemsareencountered:(1)howtoselectthekernel
notusedfortrainingthemodel.Thek-foldcross-validation
function,and(2)howtoselectitshyper-parameter.AnSVM (k-CV)isthemostusedprocedure.Itconsistsonpartitioning
withpolynomialkernelhasthreeparametersthatneedtobe
dataintokdisjointsetsofapproximatelyequalsize.AnSVM
optimized:theregularizationparameterC,theparametera, isthustrainedktimes:atthei−thiteration,allthedisjoint
| andthedegreed.Theoptimizationofthesethreeparameters |     |     |     |     |      |          |             |            |       | −th  |          |
| --------------------------------------------------- | --- | --- | --- | --- | ---- | -------- | ----------- | ---------- | ----- | ---- | -------- |
|                                                     |     |     |     |     | sets | are used | as training | set except | the i | set, | which is |
if50stepsshouldbeperformed,requiresanamountoftime used to evaluate the performance of the model. The errors
| totestthetotal503 | =125000combinations.Thegreaterthe |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observedinthisprocessareaveragedyieldingthek-foldCV
numberofparameterstobeset,thegreateristhenumberof
error.
combinations.
Beforeintroducingthemostusedevaluationmeasures,it
| The cost-sensitive |     | SVM (CS-SVM) | uses | two penalty |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
isusefultorevisetheconfusionmatrixofbinaryclassification
| weightsforthetwoclasses.LetC |     |     | ,bethecostofafalsenega- |     |                                                      |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ----------------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                              |     |     | 1                       |     | problems.AgeneralconfusionmatrixisillustratedinTable |     |     |     |     |     |     |
tive.Itpenalizesmisclassificationofinstancesoftheminority
1.Thetwocolumnsrefertothepredictedclasses,whereasthe
| class.Analogously,letC−1 |     | ,bethecostofafalsepositive.It |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tworowsrefertotheactualclasses.TruePositives(TP)isthe
penalizesmisclassificationofinstancesofthemajorityclass.
|     |     |     |     |     | number | of positive | instances | correctly | classified |     | and False |
| --- | --- | --- | --- | --- | ------ | ----------- | --------- | --------- | ---------- | --- | --------- |
TheoptimizationmodelCS-SVMis(4)-(6).
|     |     |     |     |     | Negatives | (FN) | is the number |     | of positive | instances | incor- |
| --- | --- | --- | --- | --- | --------- | ---- | ------------- | --- | ----------- | --------- | ------ |
rectlyclassifiedasnegative.Thesetwonumbersrefertothe
|     |     | (cid:2) | (cid:2) |     |     |     |     |     |     |     |     |
| --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
argmin (cid:6)w(cid:6)2+C[C ]ξ +C−1 ξ ] (4) minorityclass.Similarly,TrueNegatives(TN)isthenumber
|     |     | 1   | i   | i   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w,b,ξ 2 ofnegativeinstancescorrectlyclassified,andFalsePositives
|     |     | i|yi =1 | i|yi =−1 |     |     |     |     |     |     |     |     |
| --- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
123

| Ahyper-parametertuningapproach... |     |     |     |     |     |     |     |     |     |     |     |     |     | 12867 |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Table1 Confusionmatrixforabinaryproblem classificationevaluationmeasuresthatallowtobalancefalse
positiverateandfalsenegativerate.Here,amongthesemea-
Predicted
sures,weevaluateevenF-Measure,theGeometricMean,the
positiveclass negativeclass averagecost,theYouden’sindex,andthebalancedaccuracy.
| Actual | positiveclass |     |     | TP  |     | FN  |     | Theyaredefinedasfollows. |     |     |     |     |     |     |
| ------ | ------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
negativeclass FP TN F-Measureintegratessensitivityandprecisionintoanaver-
agebyaharmonicmean
| (FP) is the | number | of  | negative | instances | incorrectly |     | classi- |     |     |               |     |           |     |     |
| ----------- | ------ | --- | -------- | --------- | ----------- | --- | ------- | --- | --- | ------------- | --- | --------- | --- | --- |
|             |        |     |          |           |             |     |         |     |     | 2Sensitivity× |     | Precision |     |     |
−Measure=
| fiedaspositiveclass.Thesetwonumbersrefertothemajority |     |     |     |     |     |     |     | F   |     |              |     |           |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | --- |
|                                                       |     |     |     |     |     |     |     |     |     | Sensitivity+ |     | Precision |     |     |
class.Observethat,incaseofdatarelatedtopatients,afalse
negativemeansthatpatienthasthediseasebutthediagnosis
Theharmonicmeanoftwonumberstendstobeclosertothe
resultsaysthatitdoesnothave.
|     |             |     |            |          |     |          |        | smaller number. |     | A high | F-Measure | value | means | that both |
| --- | ----------- | --- | ---------- | -------- | --- | -------- | ------ | --------------- | --- | ------ | --------- | ----- | ----- | --------- |
| The | most common |     | evaluation | measures |     | used are | listed |                 |     |        |           |       |       |           |
SensitivityandPrecisionarehigh.
below.
GeometricMean(G-Mean)issuggestedasthebalancedper-
| Accuracy | defined | as  | the ratio | between |     | the number | of  |     |     |     |     |     |     |     |
| -------- | ------- | --- | --------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
formancebetweenthetwoclasses.Itisintrinsicallydefined
instancescorrectlyclassifiedandthetotalnumberofinstances.
|     |     |     |     |     |     |     |     | as the geometric |     | mean of | sensitivity | and | specificity. | If the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ----------- | --- | ------------ | ------ |
Itassessestheoveralleffectivenessofthemodelbyshowing
|     |     |     |     |     |     |     |     | G-Mean value | is  | high, both | Sensitivity |     | and Specificity | are |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ----------- | --- | --------------- | --- |
theprobabilityofthetruevalueoftheclasslabel
expectedtobehighsimultaneously
|     |     |     | +TN |     |     |     |     |     | (cid:5) |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
TP
| Accuracy | =   |     |        |     |     |     |     | G−Mean | =   | Sensitivity×Specificity |     |     |     |     |
| -------- | --- | --- | ------ | --- | --- | --- | --- | ------ | --- | ----------------------- | --- | --- | --- | --- |
|          |     | +FP | +Tn+FN |     |     |     |     |        |     |                         |     |     |     |     |
TP
Othertwomeasuresthatseparatelyestimateaclassifier’sper- AverageCost(AC)isexpressedas
formanceondifferentclassesaresensitivityandspecificity.
|     |     |     |     |     |     |     |     |     |     | C ×FN | +C−1 | ×FP |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---- | --- | --- | --- |
Theyareoftenemployedinmedicalandbio-medicalappli- AverageCost = 1
| cations. |     |     |     |     |     |     |     |     |     | TP +TN | +FP | +FN |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
Sensitivity(truepositiverate)isdefinedastheratiobetween where C and C−1 are the two costs used in the objective
1
thenumberofpositiveinstancescorrectlyclassifiedassuch
functionofCS-SVM.
andthenumberofpositiveinstances
|             |     |     |     |     |     |     |     | Youden’s index                       | Y   | equally | weights | the | algorithm’s | perfor- |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | ------- | ------- | --- | ----------- | ------- |
|             |     | TP  |     |     |     |     |     | manceonpositiveandnegativeinstances: |     |         |         |     |             |         |
| Sensitivity | =   |     |     |     |     |     |     |                                      |     |         |         |     |             |         |
+FN
TP
Y =sensitivity+specificity−1
Specificity(truenegativerate)isdefinedastheratiobetween
thenumberofnegativeinstancescorrectlyclassifiedassuch Balanced accuracy(BA) is the average of sensitivity and
andthenumberofnegativeinstances
specificity:
|             |            | T N |           |       |        |        |        |          |          |     | sensitivity+ | specificity |     |     |
| ----------- | ---------- | --- | --------- | ----- | ------ | ------ | ------ | -------- | -------- | --- | ------------ | ----------- | --- | --- |
| Specificity | =          |     |           |       |        |        |        |          |          | =   |              |             |     |     |
|             |            | +   |           |       |        |        |        | Balanced | accuracy |     |              |             |     |     |
|             |            | TN  | FP        |       |        |        |        |          |          |     |              | 2           |     |     |
| Precision   | is defined | as  | the ratio | of TP | to the | number | of all |          |          |     |              |             |     |     |
instancespredictedaspositive
4 Multi-objectiveoptimizationproblems
andGeneticalgorithms
TP
=
Precision
TP +FP
Multi-objectiveoptimizationproblemsconsistofmorethan
Asreportedespeciallyrecentlyinsomepapers(e.g.,Tao onecriterion,oftenconflicting,forwhichanysolutionexist-
et al. 2019), the accuracy-based evaluation measure is not ing on the Pareto front of criterion trade-offs is considered
| suitableforclassificationofimbalanceddataastheminority |     |     |     |     |     |     |     | optimal. |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
class has very little effect on the accuracy compared to the Inthissection,weintroducemulti-objectiveoptimization
majority class. For imbalanced classification problems, the problemsandthecornerstoneconceptofParetooptimality.
correctclassificationofinstancesoftheminorityclassisusu- Amulti-objectiveproblemconsistsofminimizingand/or
allythemostimportantmeasure.Therearefurtherinteresting maximizing two or more objective functions subject to
123

12868 R.Guidoetal.
inequality and/or equality constraints. The objective func- lems. This algorithm was called non-dominated sorting
tionsareconflictingamongthemandasolutionisatrade-off genetic-algorithm (NSGA). Deb et al. (2002) improved it
intheobjectivefunctionspace. by proposing NSGA-II. The key features of NSGA-II are
elitism, diversity-preserving mechanisms, and emphasis on
Definition1 A solution is defined Pareto optimal if there
non-dominatedsolutions.InNSGA-II,the N offspringsare
doesnotexistanyothersolutionintheobjectivespacewhich
createdfromtheNparentsusingstandardgeneticalgorithms.
improvesthevalueofanyofitsobjectivefunctionswithout
Thenewpopulationatthenextgenerationisgivenbyselect-
deterioratingatleastoneotherobjectivefunctionvalue.
ingthenon-dominatedsolutionsfortheParetofrontwiththe
Inotherwords,anon-dominatedsolutionprovidesasuit- highestdiversitywhilediscardingtherestofthesolutions.
able compromise between all objectives without degrading
Tournament selection This is a procedure that imitates sur-
any of them. The multi-objective optimization process is
vivalofthefittestinnature.Indeed,eachindividualcompetes
looking for a set of alternative solutions that represent the
intwotournamentswithrandomlyselectedindividuals.The
Paretooptimalsolution.Asetofnon-dominatedindividuals
crowded tournament selection is based on ranking and dis-
formaPareto-optimalfront.
tance:ifasolutionhasabetterrankthananotherone,itwill
From the mathematical point of view, the definition of
beselected;iftheranksarethesamebutthecrowdingdis-
thedominancebetweentwosolutionsx andx isthatx is
1 2 1 tance is not, the solution with better crowding distance is
noworsethan x inallobjectives f ,i ∈ {1,...,m}ofthe
2 i selected.
problem.Thisconceptcanbeexpressedasx dominatesx
1 2
if f (x ) ≤ f (x )∀i ∈ {1,...,m}and ∃ j ∈ {1,...,m} : CrowdingdistanceThecrowdingdistancemetricofanindi-
i 1 i 2
f (x )≤ f (x ). vidual proposed by Deb and Goel (2001) aims to select
j 1 j 2
ThegeneticalgorithmsweredevelopedbyHollandandhis potential individuals to construct a new population. It is
collaborators (Holland 1975) as a model based on Charles essentially based on the cardinality of a solution sets and
Darwin’s theory of natural selection. They are heuristic their distance to solution boundaries. More specifically, it
searchtechniques,successfullyappliedtodifferentdomains is defined as the perimeter of the rectangle with its nearest
(e.g., Guido and Conforti 2017; Bao-De et al. 2021). Fur- neighbors at diagonally opposite corners. Two individuals
thermore, they demonstrated a large amount of inherent with a same rank are better if they have a larger crowding
parallelism that makes them attractive mainly for solving distance.
problems defined in large feature spaces, as that one here
Crossover and mutation Crossover and mutation are
addressed. The evolutionary process usually starts from a
employedtoobtaintheoffspringpopulation.
populationofrandomlygeneratedindividuals,whicharethe
Algorithm1showstheframeworkofNSGA-II.Themain
chromosomes.Itisaniterativeprocess.Oneiterationisone
stepsofNSGA-IIcanbesummarizedasfollows:
generation.Ineachgeneration,thefitnessofeveryindividual
inthepopulationisevaluated.Thefitnessvalueofachromo-
Step1 Create a new population by combining parents and
someisameasureofitsgoodness.Thefitnessisusuallythe
offspringsandapplynon-dominatedsorting
valueoftheobjectivefunctionintheoptimizationproblem
Step2 Identifydifferentfronts
beingsolved.Usually,operatorssuchasselection,crossover,
Step3 Generatethenewpopulationbyexploitingthefronts
mutation and recombination are applied during the evolu-
givenatthepreviousstepuntilsize N
tionaryprocessoverthegeneratedpopulationstofindbetter
Step4 Usethecrowddistancetocarryoutacrowdingsort
chromosomes,whichoptimizethefitnessfunctiontillater-
appliedtothefronts
minationconditionisreached.Theoffspringsinapopulation
Step5 Generatenewoffspringfromthecurrentpopulation
act like independent agents so that they explore the search
via the genetic operators crossover, mutation, and
spaceinmanydirections.
selection
Aswellknown,geneticalgorithmshavesomedisadvan-
tages mainly due to the choice of parameters such as the
mutation rate and crossover rate that should be carried out
carefully.Thecrossoveroperatorisoneofthemostimpor-
tantoperatorsbecauseitdeterminestheglobalconvergence 5 Proposedapproach
ofthegeneticalgorithm.
In this section, is firstly introduced a basic approach for
4.1 NSGA-II hyper-parameter optimization. Then, a novel algorithm for
hyper-parameterstuningbasedonGAandDTisproposed.
Srinivas and Deb (1994) proposed an algorithm based The core of the algorithm is a fitness function evaluation
on non-dominated sorting for solving multiobjective prob- procedurealongwithasimilarityprocedure.
123

| Ahyper-parametertuningapproach... |     |     |     |     |     |     |     | 12869 |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- |
Algorithm1NSGA-II
Require:
RandompopulationP0;achildpopulationQ0isgeneratedfromthe
| populationofparents | P0usinggeneticoperatorssuchascrossover |     |     |     |     |     |     |     |
| ------------------- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
andmutation
1: whileanystoppingcriterionisnotreacheddo
| 2: Rt = | Pt ∪Qt |     |     |     |     |     |     |     |
| ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
3: fast-non-dominated-sort(Rt)
| 4: Pt+1       | =∅;i =1;     |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| 5: while|Pt+1 | |+|Fi |<N do |     |     |     |     |     |     |     |
6: Applycrowding-distance-assignmentFi
| 7: Pt+1 | ← Pt+1 ∪Fi |     |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
8: i ←i+1
9: endwhile
| 10: Sort(Fi | ,<N)                 |       |     |     |     |     |     |     |
| ----------- | -------------------- | ----- | --- | --- | --- | --- | --- | --- |
| 11: Pt+1    | ← Pt+1 ∪Fi [1:(N−|Pt | +1|)] |     |     |     |     |     |     |
| 12: Qt+1    | ←createNewPopPt+1    |       |     |     |     |     |     |     |
13: t ←t+1
14: endwhile
Fig.2 Frameworkoftheimprovedhyper-parametersalgorithm
|     |     |     |     | out is 4800 | and the computational |     | time may | be extremely |
| --- | --- | --- | --- | ----------- | --------------------- | --- | -------- | ------------ |
high.
|     |     |     |     | There | are two main | issues: the | first one | is related to the |
| --- | --- | --- | --- | ----- | ------------ | ----------- | --------- | ----------------- |
timeneededtocarryoutk-foldCV;thesecondone,isrelated
tothefactthatoftenachromosomeisslightlydifferentfrom
|     |     |     |     | another         | one already evaluated | and        | with equal     | fitness. We    |
| --- | --- | --- | --- | --------------- | --------------------- | ---------- | -------------- | -------------- |
|     |     |     |     | try to overcome | these                 | two issues | by introducing | a proce-       |
|     |     |     |     | dure in the     | NSGA-II               | algorithm  | that exploits  | a suitable and |
Fig.1 MainstepsofNSGA-II trainedDT.Theproposedalgorithm,describedinthefollow-
|     |     |     |     | ing, reduces | considerably | the overall | number | of performed |
| --- | --- | --- | --- | ------------ | ------------ | ----------- | ------ | ------------ |
k-foldCVbycombiningNSGA-IIwithaDT.Thegoalisto
5.1 Basicapproach
evaluateonlyasmallsetofchromosomesateachgeneration
byak-foldCV.Thisproceduredoesnotaffectconvergenceof
ThebasicapproachconsistsonusingNSGA-IIalgorithmfor
thealgorithmandstronglyreducestheoverallcomputational
solvingamulti-objectivehyper-parametertuningproblem.A
time.
| set of hyper-parameter | codified | as a chromosome | is evalu- |     |     |     |     |     |
| ---------------------- | -------- | --------------- | --------- | --- | --- | --- | --- | --- |
atedbyak-foldCVapproach.Afitnessfunctionevaluation
isthusperformedateachgeneration,i.e.,eachchromosome 5.2 Improvedhyper-parametersalgorithm
hasitsfitnessfunctionsevaluated.However,thisapproachis
quitetimeconsuming.Indeed,letN,bethenumberofchro- The above basic approach has been modified in order to
mosomesofapopulation,andGthenumberofgenerations. evaluate the fitness function only of some individuals of a
Ateachgeneration,thenumberofcarriedoutk-foldCVis population by a k-fold CV. Figure 2 provides an intuitive
N, one per each chromosome. The overall number of per- understandingoftheproposedalgorithmframework.
|     |     | ×G.Forexample,if | =   |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
formedk-foldCVisthus N N 24 Each chromosome consists of a number of genes that
andG =200,theoverallnumberofk-foldCVtobecarried representthehyper-parameters ofCS-SVM.Thealgorithm
123

12870 R.Guidoetal.
startsfromaninitialpopulation Pop .Itconsistsofthefol-
0
lowingfivemainsteps.
Algorithm2Proposedhyper-parametersalgorithm
1: Step1Initialization
2: Step1.1DefineGenSetasasetofnumbersofgenerations
3: Step1.2CreateaninitialpopulationPop0
4: Step 2 (Fitness function evaluation) Evaluate the fitness value of
eachchromosomeinthecurrentpopulation.
5: ifthecurrentgenerationGen∈GenSetthengotoStep2.1
6: elsegotoStep2.2
7: endif
8: Step2.1Performak-CV
9: Step2.2(Similarityprocedure)Compareeachchromosomewith
theonesofthepreviouspopulation
10: if Similarity=Truethenassignafitnessvaluetoitbythetrained
DT
11: elsegotoStep2.1
12: endif
13: Step3Terminationcriteria.Ifatleastoneofthestoppingconditions
ismeet,thealgorithmstops
14: Step4TrainDecisionTree.Thecurrentpopulationisusedtotrain
aDecisionTree.
15: Step 5 Reproduce a new population. The operators of selection,
crossoverandmutationareappliedoverthegeneratedpopulationto
findbetterchromosomes.
ThecoreofAlgorithm2isthefitnessevaluationprocedure
atStep2,explainedinthefollowing.
Step2: Fitness evaluation procedure The aim of the fitness
Fig.3 Fitnessevaluationprocedure
evaluation step is to provide a procedure that reduces the
numberoffitnessevaluationsandconsequentlythenumber
of carried out k-fold CV. To this purpose, a DT is trained is found, a cost-sensitive learning classifier SVM-based is
at each generation and used to predict the fitness value of builtandthefitnessvalueisevaluatedbyk-foldCV.
somechromosomes,asexplainedbelow.Indeed,thefitness Similaritybetweentwochromosomescanbeestimatedby
of a chromosome in a population is evaluated or assigned: various distance measurement methods. Here, we designed
Awholepopulationisevaluatedbyk-foldCVonlyatthose a procedure that evaluates similarity between two chromo-
generationswell-definedinthesetGenSet.Thismeansthat somesasfollows.Letchr 1 andchr 2 ,betwochromosomes
thecost-sensitivelearningclassifierSVM-basedisbuiltusing representedasvectors.Theprocedurecompareseachcorre-
thehyper-parameterscodifiedaschromosomesofthepopula- sponding couple of genes of chr 1 and chr 2 , as detailed in
tion;foreverychromosomes,ak-foldCVisusedtoestimate Algorithm 3. More specifically, the difference between the
thegeneralizationabilityoftherelatedbuildmodel.Theset i−thgeneofchr 1 andthecorrespondinggeneofchr 2 iscom-
GenSet hasatleasttwoelements,i.e.,thefirstandthelast puted.Ifthisdifferenceislessthanagiventhresholdt i ,the
generation.AprocedurebasedonalearnedDTtakesplace nextcoupleofgenesofthetwochromosomesarecompared;
atthosegenerationsnotinthesetGenSet. otherwise,theprocedurestopsandthetwochromosomesare
ThefitnessevaluationprocedureisdepictedinFig.3.To notsimilar.
reducetheoverallcomputationaltime,theprocedureverifies Figure 4 depicts an example of DT trained to predict a
if each chromosome has already a fitness value (because it givenfitnessfunction.
hasbeenevaluatedpreviously).Ifso,theprocedureanalyzes
nextchromosome;otherwise,thechromosomeiscompared,
at Step 2.2, with the chromosomes of the previous popu- 6 Experimentalresultsandanalysis
lation in order to discover similarity. If the chromosome is
similar at least to one chromosome, the DT trained on the In this study, we test the proposed Algorithm 2 for on six
previous population predicts its fitness value; this value is benchmarkimbalanceddatasetsbinaryclassificationtaskto
thusassignedaspredictedvalue.Otherwise,ifnosimilarity comparetheperformanceofdifferentclassificationmethods
123

| Ahyper-parametertuningapproach... |     |     |     |     |     |     |     |     |     |     | 12871 |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |
Fig.4 Anexampleoftrained
decisiontree
Algorithm3Similarityprocedure investigatedandtunedoverarereportedinSect.6.2.Exper-
| Require: |     |     |                        |              | imentalresultsarelistedinSect.6.3. |     |     |     |     |     |     |
| -------- | --- | --- | ---------------------- | ------------ | ---------------------------------- | --- | --- | --- | --- | --- | --- |
|          |     |     | ,chr2 ∈ Rk.Thresholdti | ,i =1,...,k. |                                    |     |     |     |     |     |     |
Twochromosomeschr1
=1;similarity←true
1: i
≤kdo
2: whilei
| if|chri1 | −chri2 | |<ti |      |     | 6.1 Benchmarkdatasets |     |     |     |     |     |     |
| -------- | ------ | ---- | ---- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
| 3:       |        |      | then |     |                       |     |     |     |     |     |     |
←i+1
4: i
5: else The datasets are from the University of California Irvine
←k
| 6:  | i   |     |     |     | (UCI) | Repository |     | of Machine |     | Learning | Databases |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | ---------- | --- | -------- | --------- |
similarity←
| 7:  |     | false |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(https://archive.ics.uci.edu/ml/datasets.php).Theyhavediver-
8: endif
|     |     |     |     |     | sity in the | number | of  | attributes | and | imbalance | ratio. More- |
| --- | --- | --- | --- | --- | ----------- | ------ | --- | ---------- | --- | --------- | ------------ |
9: endwhile
10: returnsimilarity over, the datasets have both continuous and categorical
attributes,andsomeofthemhavemissingvalues.
|     |     |     |     |     | Appendicitis |     | dataset | consists | of  | 106 | instances and 8 |
| --- | --- | --- | --- | --- | ------------ | --- | ------- | -------- | --- | --- | --------------- |
intheliteraturewithourresults.Theyarerelatedtomedical attributes.Theattributesareresultsoflaboratorytest.
diagnosisrepresentedasbinaryclassificationproblemsand
|     |     |     |     |     | Haberman |     | datasetdescribesthefive-yearorgreatersur- |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | ----------------------------------------- | --- | --- | --- | --- |
have different sample sizes, attributes, and imbalance ratio vival of breast cancer patients. The study was conducted
| (IR), defined | as  | m/M | (Amin et al. 2016), | where m is the |         |      |          |     |                |     |              |
| ------------- | --- | --- | ------------------- | -------------- | ------- | ---- | -------- | --- | -------------- | --- | ------------ |
|               |     |     |                     |                | between | 1958 | and 1970 | at  | the University |     | of Chicago’s |
number of the minority instances and M is the number of BillingsHospital.Thedatasetconsistsof306instancesand
majorityinstances.
|              |     |             |           |               | 4 attributes.  | The | outcome | is  | patient | survival. | There are no |
| ------------ | --- | ----------- | --------- | ------------- | -------------- | --- | ------- | --- | ------- | --------- | ------------ |
| We conducted |     | experiments | to answer | the following | missingvalues. |     |         |     |         |           |              |
researchquestionsempirically:
|     |     |     |     |     | Hepatitis | datasetisusedtoclassifypatientswithhepati- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | ------------------------------------------ | --- | --- | --- | --- | --- |
tisinthetwoclasses,liveordie.Itconsistsof155instances
1. Doesmulti-objectiveoptimizationfindmuchsparsersolu-
|     |     |     |     |     | and 19 attributes, |     | 14 nominal |     | attributes | and | 6 multi-valued |
| --- | --- | --- | --- | --- | ------------------ | --- | ---------- | --- | ---------- | --- | -------------- |
tions without a major loss in predictive performance attributes. It requires the determination of whether patients
comparedtosingle-objectiveoptimization?
withhepatitiswilleitherliveordie.Theproblemaimstopre-
2. Aretherealternativemetricstotheaccuracy? dictthepresenceorabsenceofhepatitisbyusingtheresults
| 3. May | the computational |     | time be reduced | by a machine |     |     |     |     |     |     |     |
| ------ | ----------------- | --- | --------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
ofvariousmedicaltestscarriedoutonapatient.Thedataset
| learningtechnique? |     |     |     |     | hasmissingvalues. |        |          |         |     |         |                 |
| ------------------ | --- | --- | --- | --- | ----------------- | ------ | -------- | ------- | --- | ------- | --------------- |
|                    |     |     |     |     | Pima              | Indian | Diabetes | dataset | is  | used to | predict whether |
AbriefdescriptionofthedatasetsisinSect.6.1.Detailson ornotapatienthasdiabetes.Allpatientsarefemale,areat
the algorithms embedded in our approach and the hyper- least21yearsold,andareofPimaIndianheritage.Ithas8
parameter spaces of the several CS-SVM that are being laboratoryfeatures.
123

| 12872 |     |     |     |     |     |     |     |     |     |     |     |     | R.Guidoetal. |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |
Table2 Datasetsandtheirmaincharacteristicsintermsofnumberof
attributes(No.A),numberoftheminorityinstances(m),numberofthe
majorityinstances(M),indexratioIR=m/M
| Dataset |     | No.A |     | m   | M   | IR  |     |     |     |     |     |     |     |
| ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Fig.5 Representationofachromosome
| Appendicitis |     | 8   |     | 21  | 85  | 0.25 |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| Haberman     |     | 4   |     | 81  | 225 | 0.36 |     |     |     |     |     |     |     |
Hepatitis 19 70 85 0.82 ments were run on a PC Intel Xeon E5 1620 CPUs with 4
| Pima |     | 9   |     | 268 | 500 | 0.53 | coresat3.50GHzand32GBRAM.               |     |     |     |     |     |         |
| ---- | --- | --- | --- | --- | --- | ---- | --------------------------------------- | --- | --- | --- | --- | --- | ------- |
| WDBC |     | 10  |     | 241 | 458 | 0.53 |                                         |     |     |     |     |     |         |
| WPBC |     | 32  |     | 47  | 151 | 0.33 | 6.2.1 Parametersetting                  |     |     |     |     |     |         |
|      |     |     |     |     |     |      | Algorithm2startsfromaninitialpopulation |     |     |     |     | Pop | ofchro- |
0
|           |     |            |        |        |        |         | mosomes | randomly     | generated. |                 | Each chromosome |            | has four |
| --------- | --- | ---------- | ------ | ------ | ------ | ------- | ------- | ------------ | ---------- | --------------- | --------------- | ---------- | -------- |
| Wisconsin |     | Diagnostic | Breast | Cancer | (WDBC) | dataset |         |              |            |                 |                 |            |          |
|           |     |            |        |        |        |         | genes   | representing | the        | hyper-parameter |                 | of CS-SVM, | as       |
consistsof30featurescomputedbydigitizedimageoffine
|     |     |     |     |     |     |     | depicted | in Fig. | 5. All | experiments | have | the same | random |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ------ | ----------- | ---- | -------- | ------ |
needleaspirateofabreastmassindex.Theproblemaimsto
initialpopulation;thenumberofgenerationsistheonlyone
predictwhetherornotthepatienthasbreastcancer.
stoppingcriterion.
WisconsinPrognosticBreastCancer(WPBC)datasethas
Table3liststhesearchpopulationsize,crossoverprobabil-
198instancesthatrepresentfollow-updataforonebreastcan-
|     |     |     |     |     |     |     | ity p ,genemutationprobability |     |     |     | p ,numberofgenerations |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ---------------------- | --- | --- |
cer case, only those cases exhibiting invasive breast cancer c m
|     |     |     |     |     |     |     | along | with the | design | parameters | (decision | variables) | and |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ------ | ---------- | --------- | ---------- | --- |
andnoevidenceofdistantmetastasesatthetimeofdiagno-
therangeoftheirvariations.Wetestedtwopopulationsizes
sis.Itisusedinthispapertoclassifypatientsasrecurrences
andcreatedtheinitialparentpopulationrandomlybyselect-
before24months(positiveclass)ornon-recurrencebeyond
|     |     |     |     |     |     |     | ing solutions | from | the | ranges | defined | for the | parameters |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --- | ------ | ------- | ------- | ---------- |
24months(negativeclass).Weremovedthefeaturenamed
C,C ,C ,γ,whereC
|                                                     |     |     |     |     |     |     |     |     |     | andC | arethecostsoftheminority |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------ | --- | --- |
| “Time”fromthedatasetbecauseitistherecurrencetimefor |     |     |     |     |     |     | 1   | 2   | 1   | 2    |                          |     |     |
classandmajorityclass,respectively.
| instances | in the | positive | class | and | the disease-free | time for |     |     |     |     |     |     |     |
| --------- | ------ | -------- | ----- | --- | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
theinstancesofthenegativeclass. The multi-objective problem that we formulated and
solvedhasthreefitnessfunctions(7–9),givenbyaccuracy,
| Table | 2 summarizes, |     | per | each | dataset, the | number of |     |     |     |     |     |     |     |
| ----- | ------------- | --- | --- | ---- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
attributes,thenumberofminorityinstances(diseasedexam- G-mean,andAverageCost,respectively:
| ples), the                  | number | of  | the majority |     | instances (non-diseased |     |      |        |        |     |     |     |     |
| --------------------------- | ------ | --- | ------------ | --- | ----------------------- | --- | ---- | ------ | ------ | --- | --- | --- | --- |
|                             |        |     |              |     |                         |     |      |        | TP +TN |     |     |     |     |
| examples),andtheindexratio. |        |     |              |     |                         |     | =max |        |        |     |     |     |     |
|                             |        |     |              |     |                         |     | f 1  |        |        |     |     |     | (7) |
|                             |        |     |              |     |                         |     |      | TP +FP | +TN    | +FN |     |     |     |
(cid:5)
|     |     |     |     |     |     |     | f =max | Sensitivity×Specificity |     |     |     |     | (8) |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------------------- | --- | --- | --- | --- | --- |
2
| 6.2 Learningalgorithmsandhyperparameters |     |     |     |     |     |     |        | C ×FN | +C  | ×FP |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- | --- | --- |
|                                          |     |     |     |     |     |     | f =min | 1     |     | 2   |     |     | (9) |
| optimization                             |     |     |     |     |     |     | 3      | +TN   | +FP | +FN |     |     |     |
TP
WeconsideredseveralmodelclassifiersCS-SVMwithGaus- Alltheexperimentsareconductedby10-foldcross-validation.
| sian kernel | tuned | by  | the optimization |     | algorithm | proposed. |     |     |     |     |     |     |     |
| ----------- | ----- | --- | ---------------- | --- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
The experiments were performed by the ML algorithms of 6.3 Computationalresults
| Waikato | Environment |     | for Knowledge |     | Analysis | (WEKA). |     |     |     |     |     |     |     |
| ------- | ----------- | --- | ------------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
WEKA isanopen-source collection of MLalgorithms and Toassessourapproach,weperformedbothAlgorithm1and
dataprocessingtools.WeusedSequentialminimaloptimiza- Algorithm 2 on the six datasets and compared the results.
tion algorithm for SVM and Random Tree algorithm for The computational experiments were carried out using the
DT. For that concerning NSGA-II algorithm, we used the JCLECsequentialalgorithmanditsparallelizedversion.The
frameworknamedJavaClassLibraryforEvolutionaryCom- only difference we noticed was the reduced computational
putation (JCLEC) Ramírez et al. (2015, 2019), which is a timeoftheparallelizedversionwithrespecttothesequential
Javasuiteforsolvingmulti-objectiveoptimizationproblems algorithm.Wereportinthissectiononlytheresultsfoundby
| usingevolutionaryalgorithms. |     |     |     |     |     |     | theparallelversion. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
Algorithm 2 has been coded in Java using the NSGA Table 4 reports the best fitness values per each dataset.
II algorithm of the JCLEC framework. We executed both From the second to the fourth column there is the value of
thesequentialandtheparallelversionoftheNSGA-II.The accuracy,G-Mean,andaveragecost,respectively.Wecom-
parallel version is more efficient since it performs function pareinthistableourresultswiththebestonesoftheliterature
evaluations of different individuals in parallel. The experi- byselectingthosepapersthatoptimizedhyper-parameterof
123

Ahyper-parametertuningapproach... 12873
Table3 NSGA-IIparameters
|     | NSGA-IIparameters |     |     |     | CS-SVMhyper-parameterspace |     |     |
| --- | ----------------- | --- | --- | --- | -------------------------- | --- | --- |
andhyper-parametersspacesof
| CS-SVMwithRBFkernel | Popsize | pc  | pm   | NumGen | Cost      |     | γ         |
| ------------------- | ------- | --- | ---- | ------ | --------- | --- | --------- |
|                     | 24      | 0.8 | 0.25 | 100    | C ∈{1−50} |     | {0.001−1} |
∈{1−20}
|     | 48  |     |     | 200  | C1         |     |     |
| --- | --- | --- | --- | ---- | ---------- | --- | --- |
|     |     |     |     | 1000 | C2 ∈{1−10} |     |     |
Table4 Bestmetricvaluesby
|     | Dataset | Accuracy | G-Mean | AC  | Acc AC | G-Meana | G-Meanb |
| --- | ------- | -------- | ------ | --- | ------ | ------- | ------- |
theoptimizedhyper-parameters
|     |     |     |     |     | [1] [2] | [3] | [3] |
| --- | --- | --- | --- | --- | ------- | --- | --- |
comparedtothebestresultsof
theliterature.[1](YuandWang
|     | Appendicitis | 89.62 | 82.54 | 0.11 | – – |     |     |
| --- | ------------ | ----- | ----- | ---- | --- | --- | --- |
2017);[2](Qietal.2013);
|                          |          |       |       |      |     | 60.77±3.89 | 66.71±1.67 |
| ------------------------ | -------- | ----- | ----- | ---- | --- | ---------- | ---------- |
| [3](Taoetal.2019).Hyphen | Haberman | 76.14 | 67.70 | 0.26 | – – |            |            |
meansthattheauthorsdidnot Hepatitis 87.10 84.06 0.14 83.22 0.208
testthatdataset
|     | Pima | 78.13 | 76.54 | 0.22 | 76.27 0.457 | 64.60±3.16  | 75.13±1.67 |
| --- | ---- | ----- | ----- | ---- | ----------- | ----------- | ---------- |
|     |      |       |       |      |             | 92.41±2.44  | 96.91±1.79 |
|     | WDBC | 97.42 | 97.73 | 0.03 | – –         |             |            |
|     | WPBC | 77.78 | 61.54 | 0.22 | 81.28 –     | 27.38±11.69 | 67.53±3.71 |
Boldindicatesthebestaccuracyvalues
SVMwithRBFkernel.Undertheseconditions,experimen- G-meanvalue.SimilarcasesareontheHepatitisandWPBC
| talevidenceshowsthatouralgorithmfindssimilarresultsor |     |     | datasets. |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --------- | --- | --- | --- | --- |
outperformstheotheralgorithmsproposedintheliterature. Tables 5 and 6 show the results found by Algorithm 1
ThebestresultsintermsofaccuracyonHepatitis,Pima,and on the six datasets along with the related optimized hyper-
WPBCdatasetsarefoundin(YuandWang2017)byoptimiz- parameter configuration. For the Appendicitis dataset, for
ingtheparametersoftheSVMwithRBFkernelbyanovel instance,thebestaccuracyinTable5is f =89.62;thebest
1
ensembledifferentialevolutionapproachthattheyproposed. G-Mean is f = 82.54, and the best average cost is f =
2 3
Severalapproachesweretestedin(Taoetal.2019)andthe 0.11. As expected, the improvement of a fitness function
results were reported in terms of G-Mean. In Table 4, we implies a worsening in the other two. We observe that the
denoted with G-Meana and G-Meanb the values found by singleoptimalfitnessvaluesarefoundwithdifferenthyper-
CS-SVMandtheirself-adaptivecostweights-basedsupport parameter tuning. Moreover, the best results are found in
vector machine cost-sensitive ensemble approach, respec- all the experiments even if number of population size and
tively.Itishelpfultonoticethattheyreportedtheseresults generationnumberisincreased.
onthedatasetsbymodifyingimbalanceddataratioof10:1. Tables 7 and 8 show the results found by Algorithm 2
Tables5,6,7,8listonlysomeofthefoundnon-dominated on the six datasets along with the related optimized hyper-
solutions of the Pareto front of our experimental results. parameter configuration. These results were found in very
These results refer to the experiments carried out with the contracted computational time if compared to the previous
relatedparallelizedversionofAlgorithms1and2.Thefirst ones. Observe that there has been a reduction over 70%
andsecondcolumnofthesetablesreportthepopulationsize in some experiments. These results show that the proposed
and the number of carried out generations; the next three Algorithm2isefficient.
columns show the fitness function values associated with Theresultsevidencedthat:(1)bothalgorithmsconverge
theoptimalhyper-parameterconfiguration,whichisreported andfindthesamebestvaluesforthethreefitnessfunctions;
in thenext four columns. The eleventh and twelfthcolumn (2) the number of optimal non-dominated solutions of the
reportsthesensitivityandspecificityvalues,whereasthenext ParetofrontfoundbyAlgorithm1isgreaterthanthenum-
four columns report the ROC area, the F-Measure, the bal- berfoundbyAlgorithm2.Tobetterunderstandourfinding,
ancedaccuracy,andtheYouden’sindex,respectively.Finally, we illustrate in Figs. 6 and 7 the Pareto points of Tables 7
the last column shows the average computational time, in and 8pereachdatasetwiththesixperformancemeasures.
minutes. The Pareto points are shown considering decreasing Sen-
Asalreadyobservedintheliterature,theaccuracyisnot sitivity.Asdepictedinthesetwofigures,generallybalance
asuitablemeasureforimbalanceddata.Indeed,wenoticed accuracydecreasesasSensitivitydecreaseswhileSensitivity
thatintheHabermandataset,forinstance,thereisahyper- increases.ThebestParetopointsrelatedtomedicaldatasets,
parameterconfigurationthatallowstohaveagoodaccuracy asthosetestedinthispaper,shouldbethepointswithhigh
equal to 75.53%, but the specificity is zero as well as the balanceaccuracyorhighsensitivityvalues.
123

12874 R.Guidoetal.
stesatadsititapeHdna,namrebaH,siticidneppAnostluserlatnemirepxE:1mhtiroglA
5elbaT
emiT
scirtemecnamrofreP
rap-repyHdezimitpO
snoitcnufssentiF
.marap.neG
tesataD
Y
AB
M-F
aeraCOR
cepS
sneS
2C
1C
γ
C
3f
2f
1f
neG
ezispoP
67.0
485.0
297.0
7.0
297.0
569.0
916.0
2
1
10.0
33
81.0
82.77
26.98
001
42
siticidneppA
656.0
828.0
7.0
828.0
498.0
267.0
4
1
83.0
9
72.0
45.28
97.68
635.0
867.0
76.0
867.0
569.0
175.0
1
1
81.0
54
11.0
52.47
86.88
24.1
485.0
297.0
7.0
297.0
569.0
916.0
2
1
81.0
2
81.0
82.77
26.98
002
656.0
828.0
7.0
828.0
498.0
267.0
4
1
83.0
9
72.0
45.28
97.68
635.0
867.0
76.0
867.0
569.0
175.0
1
1
83.0
01
11.0
52.47
86.88
90.7
485.0
297.0
7.0
297.0
569.0
916.0
2
1
81.0
2
81.0
82.77
26.98
0001
656.0
828.0
7.0
828.0
498.0
267.0
4
1
83.0
9
72.0
45.28
97.68
635.0
867.0
76.0
867.0
569.0
175.0
1
1
83.0
51
11.0
52.47
86.88
44.1
485.0
297.0
7.0
297.0
569.0
916.0
2
1
10.0
93
81.0
82.77
26.98
001
84
745.0
377.0
96.0
477.0
679.0
175.0
1
1
21.0
93
1.0
7.47
26.98
656.0
828.0
7.0
828.0
498.0
267.0
4
1
4.0
01
72.0
45.28
97.68
346.0
5128.0
17.0
228.0
929.0
417.0
81
5
10.0
3
3.1
84.18
86.88
38.2
485.0
297.0
7.0
297.0
569.0
916.0
2
1
10.0
62
81.0
82.77
26.98
002
745.0
377.0
96.0
477.0
679.0
175.0
1
1
21.0
93
1.0
7.47
26.98
31.41
485.0
297.0
7.0
297.0
569.0
916.0
2
1
10.0
62
81.0
82.77
26.98
0001
745.0
377.0
96.0
477.0
679.0
175.0
1
1
21.0
93
1.0
7.47
26.98
656.0
828.0
7.0
828.0
498.0
267.0
4
1
4.0
11
72.0
45.28
97.68
14.4
513.0
756.0
94.0
856.0
178.0
444.0
2
1
68.0
94
93.0
22.26
28.57
001
42
namrebaH
823.0
466.0
15.0
466.0
67.0
865.0
31
4
35.0
94
91.2
7.56
29.07
380.0
145.0
2.0
245.0
69.0
321.0
1
1
47.0
84
62.0
34.43
68.37
20.9
513.0
756.0
94.0
856.0
178.0
444.0
2
1
68.0
64
93.0
22.26
28.57
002
233.0
666.0
15.0
666.0
467.0
865.0
31
4
35.0
83
81.2
98.56
42.17
380.0
145.0
2.0
245.0
69.0
321.0
1
1
47.0
92
62.0
34.43
68.37
69.73
513.0
756.0
94.0
856.0
178.0
444.0
2
1
68.0
64
93.0
22.26
28.57
0001
943.0
476.0
25.0
476.0
657.0
395.0
31
4
68.0
31
21.2
19.66
42.17
780.0
5345.0
2.0
445.0
469.0
321.0
1
1
68.0
32
62.0
15.43
81.47
123

Ahyper-parametertuningapproach... 12875
|      |      | 53.31 | 29.66 |           |      |      |      | 68.61 |
| ---- | ---- | ----- | ----- | --------- | ---- | ---- | ---- | ----- |
| emiT | 87.6 |       |       | 49.0 87.1 | 30.9 | 28.1 | 54.3 |       |
353.0 990.0 353.0 990.0 663.0 990.0 126.0 956.0 445.0 126.0 956.0 445.0 186.0 445.0 576.0 125.0 576.0 445.0 186.0 445.0
|     | 23.0 | 23.0 | 80.0 23.0 |     | 36.0 | 36.0 | 36.0 | 36.0 |
| --- | ---- | ---- | --------- | --- | ---- | ---- | ---- | ---- |
Y
5048.0
676.0 945.0 676.0 945.0 386.0 945.0 018.0 928.0 277.0 018.0 928.0 277.0 518.0 048.0 277.0 518.0 738.0 067.0 518.0 738.0 277.0 518.0 277.0
|     | 66.0 | 66.0 | 45.0 66.0 |     |     |     |     |     |
| --- | ---- | ---- | --------- | --- | --- | --- | --- | --- |
AB
M-F 35.0 32.0 35.0 32.0 91.0 35.0 32.0 96.0 86.0 56.0 96.0 86.0 56.0 86.0 56.0 96.0 36.0 96.0 56.0 86.0 56.0
|     | 5.0 | 5.0 | 5.0 |     | 7.0 | 7.0 | 7.0 | 7.0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
aeraCOR
66.0 776.0 55.0 66.0 776.0 55.0 45.0 66.0 386.0 55.0 118.0 928.0 277.0 118.0 928.0 277.0 518.0 148.0 277.0 518.0 738.0 67.0 518.0 738.0 277.0 518.0 148.0 277.0
scirtemecnamrofreP
678.0 117.0 159.0 678.0 117.0 159.0 969.0 678.0 377.0 159.0 209.0 648.0 919.0 209.0 648.0 919.0 119.0 738.0 919.0 119.0 268.0 729.0 119.0 268.0 919.0 119.0 738.0 919.0
cepS
sneS 444.0 246.0 841.0 444.0 246.0 841.0 111.0 444.0 395.0 841.0 917.0 318.0 526.0 917.0 318.0 526.0 917.0 448.0 526.0 917.0 318.0 495.0 917.0 318.0 526.0 917.0 448.0 526.0
2C
|     | 2 7 | 1 2 7 | 1 1 2 31 | 1 2 2 1 2 2 | 1 2 1 | 1 2 2 | 1 2 2 | 1 2 1 1 |
| --- | --- | ----- | -------- | ----------- | ----- | ----- | ----- | ------- |
rap-repyHdezimitpO 1C
|     | 1 2 | 1 1 2 | 1 1 1 4 | 1 3 9 1 3 9 | 1 3 5 | 1 3 7 | 1 3 7 | 1 3 5 1 |
| --- | --- | ----- | ------- | ----------- | ----- | ----- | ----- | ------- |
49.0 24.0 49.0 49.0 24.0 49.0 25.0 49.0 49.0 49.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 10.0 23.0 10.0 10.0 10.0 10.0 10.0 10.0
γ
C 94 93 94 94 93 94 74 94 2 94 04 8 74 93 8 74 53 8 74 23 01 01 23 01 74 23 8 74
93.0 90.1 62.0 93.0 90.1 62.0 62.0 93.0 70.2 62.0 33.0 95.0 41.0 33.0 95.0 41.0 23.0 92.0 41.0 23.0 94.0 41.0 23.0 94.0 41.0 23.0 92.0 41.0
3f
snoitcnufssentiF 83.26 75.76 45.73 83.26 75.76 45.73 18.23 83.26 45.73 45.08 88.28 87.57 45.08 88.28 87.57 60.48 87.57 86.38 81.47 86.38 87.57 60.48 87.57
|     |     |     | 7.76 |     | 9.08 | 9.08 | 9.08 | 9.08 |
| --- | --- | --- | ---- | --- | ---- | ---- | ---- | ---- |
2f
41.67 82.96 68.37 41.67 82.96 68.37 81.47 41.67 55.27 68.37 54.68 78.38 18.58 54.68 78.38 18.58 78.38 18.58 61.58 18.58 61.58 18.58 78.38 18.58
|     |     |     |     |     | 1.78 | 1.78 | 1.78 | 1.78 |
| --- | --- | --- | --- | --- | ---- | ---- | ---- | ---- |
1f
|     |         |     | 0001 |         | 0001 |     |     | 0001 |
| --- | ------- | --- | ---- | ------- | ---- | --- | --- | ---- |
|     | neG 001 | 002 |      | 001 002 |      | 001 | 002 |      |
.marap.neG
ezispoP
deunitnoc
|     | 84  |     |     | 42  |     | 84  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
sititapeH
5elbaT tesataD
123

| 12876 |     |     |     |     |     | R.Guidoetal. |
| ----- | --- | --- | --- | --- | --- | ------------ |
Table6 Algorithm1:ExperimentalresultsonthedatasetsPima,WDBC,andWPBC
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
|             | f1 f2 | f3 γ | C1 C2 |           |             |      |
| ----------- | ----- | ---- | ----- | --------- | ----------- | ---- |
| Popsize Gen |       | C    |       | Sens Spec | ROCarea F-M | BA Y |
Pima 24 100 77.99 72.69 1.46 5 0.24 7 6 0.604 0.874 0.739 0.66 0.739 0.478 10.19
|     | 77.99 70.9  | 0.22 4 0.53 | 1 1 | 0.56 0.898 | 0.729 0.64 | 0.729 0.458 |
| --- | ----------- | ----------- | --- | ---------- | ---------- | ----------- |
|     | 74.35 76.28 | 0.68 5 0.53 | 5 2 | 0.843 0.69 | 0.767 0.7  | 0.766 0.533 |
77.6 71.12 0.22 10 0.53 1 1 0.571 0.886 0.728 0.64 0.728 0.457
200 77.99 72.69 1.46 5 0.24 7 6 0.604 0.874 0.739 0.66 0.739 0.478 20.31
|     | 77.99 70.9  | 0.22 4 0.53 | 1 1 | 0.56 0.898 | 0.729 0.64 | 0.729 0.458 |
| --- | ----------- | ----------- | --- | ---------- | ---------- | ----------- |
|     | 74.35 76.28 | 0.68 5 0.53 | 5 2 | 0.843 0.69 | 0.767 0.7  | 0.766 0.533 |
77.6 71.12 0.22 10 0.53 1 1 0.571 0.886 0.728 0.64 0.728 0.457
1000 77.99 72.69 1.46 5 0.24 7 6 0.604 0.874 0.739 0.66 0.739 0.478 100.99
|     | 77.99 70.9 | 0.22 4 0.53 | 1 1 | 0.56 0.898 | 0.729 0.64 | 0.729 0.458 |
| --- | ---------- | ----------- | --- | ---------- | ---------- | ----------- |
74.87 76.54 0.99 4 0.53 7 3 0.832 0.704 0.768 0.7 0.768 0.536
77.86 71.28 0.22 15 0.53 1 1 0.571 0.89 0.73 0.64 0.730 0.461
48 100 78.13 70.82 0.22 4 0.47 1 1 0.556 0.902 0.729 0.64 0.729 0.458 21.26
74.87 76.54 0.99 4 0.47 7 3 0.832 0.704 0.768 0.7 0.768 0.536
77.86 71.28 0.22 19 0.47 1 1 0.571 0.89 0.73 0.64 0.730 0.461
200 78.13 70.82 0.22 4 0.47 1 1 0.556 0.902 0.729 0.64 0.729 0.458 41.87
74.87 76.54 0.99 4 0.47 7 3 0.832 0.704 0.768 0.7 0.768 0.536
77.86 71.28 0.22 19 0.47 1 1 0.571 0.89 0.73 0.64 0.730 0.461
1000 78.13 70.82 0.22 4 0.47 1 1 0.556 0.902 0.729 0.64 0.729 0.458 210.71
78.13 72.34 2.11 4 0.47 10 9 0.593 0.882 0.738 0.65 0.737 0.475
74.87 76.54 0.99 4 0.47 7 3 0.832 0.704 0.768 0.7 0.768 0.536
77.99 71.51 0.22 18 0.47 1 1 0.575 0.89 0.732 0.65 0.732 0.465
WDBC 24 100 97.42 97.73 0.06 10 0.42 2 5 0.988 0.967 0.977 0.96 0.9775 0.955 2.26
97.14 97.7 0.03 6 0.42 1 5 0.996 0.959 0.977 0.96 0.9775 0.955
200 97.42 97.73 0.06 10 0.42 2 5 0.988 0.967 0.977 0.96 0.9775 0.955 7.49
97.14 97.7 0.03 6 0.42 1 5 0.996 0.959 0.977 0.96 0.9775 0.955
1000 97.42 97.73 0.06 8 0.42 2 5 0.988 0.967 0.977 0.96 0.9775 0.955 30.76
97.28 97.53 0.03 5 0.42 1 2 0.983 0.967 0.975 0.96 0.975 0.95
48 100 97.42 97.73 0.03 8 0.09 1 3 0.988 0.967 0.977 0.96 0.9775 0.955 9.44
200 97.42 97.73 0.03 8 0.09 1 3 0.988 0.967 0.977 0.96 0.9775 0.955 11.8
1000 97.42 97.73 0.03 8 0.09 1 3 0.988 0.967 0.977 0.96 0.9775 0.955 50.86
WPBC 24 100 77.78 29.08 0.24 38 0.24 1 4 0.085 0.993 0.539 0.15 0.539 0.078 1.65
69.7 61.05 0.55 1 0.24 3 1 0.489 0.762 0.625 0.43 0.6255 0.251
|     | 76.77 14.59 | 0.23 38 0.24 | 1 5 | 0.021 1 | 0.511 0.04 | 0.5105 0.021 |
| --- | ----------- | ------------ | --- | ------- | ---------- | ------------ |
200 77.78 29.08 0.24 44 0.24 1 4 0.085 0.993 0.539 0.15 0.539 0.078 3.25
|     | 77.78 25.26 | 0.22 32 0.42 | 1 8 | 0.064 1 | 0.532 0.12 | 0.532 0.064 |
| --- | ----------- | ------------ | --- | ------- | ---------- | ----------- |
69.7 61.05 0.55 1 0.24 3 1 0.489 0.762 0.625 0.43 0.6255 0.251
1000 77.78 29.08 0.24 18 0.42 1 4 0.085 0.993 150 0.15 0.539 0.078 16.17
|     | 77.78 25.26 | 0.22 32 0.42 | 1 8 | 0.064 1     | 151 0.12 | 0.532 0.064  |
| --- | ----------- | ------------ | --- | ----------- | -------- | ------------ |
|     | 69.7 61.05  | 0.55 1 0.24  | 3 1 | 0.489 0.762 | 115 0.43 | 0.6255 0.251 |
123

Ahyper-parametertuningapproach... 12877
Table6 continued
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
Popsize Gen f1 f2 f3 C γ C1 C2 Sens Spec ROCarea F-M BA Y
48 100 77.78 25.26 0.22 47 0.33 1 9 0.064 1 0.532 0.12 0.532 0.064 3.15
77.78 29.08 0.24 32 0.32 1 5 0.085 0.993 0.539 0.15 0.539 0.078
68.69 61.54 1.75 46 0.01 10 3 0.511 0.742 0.626 0.44 0.6265 0.253
200 77.78 29.08 0.24 33 0.32 1 5 0.085 0.993 0.539 0.15 0.539 0.078 6.34
77.78 25.26 0.22 33 0.32 1 6 0.064 1 0.532 0.12 0.532 0.064
68.69 61.54 1.75 44 0.01 10 3 0.511 0.742 0.626 0.44 0.6265 0.253
1000 77.78 29.08 0.23 21 0.32 1 3 0.085 0.993 0.539 0.15 0.539 0.078 31.85
77.78 25.26 0.22 33 0.32 1 6 0.064 1 0.532 0.12 0.532 0.064
68.69 61.54 1.75 48 0.01 10 3 0.511 0.742 0.626 0.44 0.6265 0.253
Table7 Algorithm2:ExperimentalresultsonthedatasetsAppendicitis,Haberman,andHepatitis
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
Popsize Gen f1 f2 f3 C γ C1 C2 Sens Spec ROCarea F-M BA Y
Appendicitis 24 100 89.62 77.28 0.18 23 0.01 1 2 0.619 0.965 0.792 0.7 0.792 0.584 0.37
86.79 80.44 0.3 10 0.01 1 4 0.714 0.906 0.81 0.68 0.81 0.62
84.91 60.62 0.15 24 0.01 1 1 0.381 0.965 0.673 0.5 0.673 0.346
200 89.62 77.28 0.36 35 0.01 2 4 0.619 0.965 0.792 0.7 0.792 0.584 0.55
86.79 82.54 0.32 28 0.13 1 5 0.762 0.894 0.828 0.7 0.828 0.656
1000 89.62 77.28 0.18 38 0.01 1 2 0.619 0.965 0.792 0.7 0.792 0.584 1.94
87.74 80.96 0.29 8 0.01 1 4 0.714 0.918 0.816 0.7 0.816 0.632
48 100 89.62 77.28 0.36 29 0.01 2 4 0.619 0.965 0.792 0.7 0.792 0.584 0.61
87.74 80.96 0.29 29 0.01 1 4 0.714 0.918 0.816 0.7 0.816 0.632
86.79 67.78 0.13 36 0.01 1 1 0.476 0.965 0.72 0.59 0.720 0.441
200 89.62 77.28 0.18 11 0.01 1 2 0.619 0.965 0.792 0.7 0.792 0.584 0.91
86.79 82.54 1.19 9 0.47 4 18 0.762 0.894 0.828 0.7 0.828 0.656
1000 89.62 77.28 0.18 18 0.01 1 2 0.619 0.965 0.792 0.7 0.792 0.584 3.07
87.74 80.96 0.29 8 0.01 1 4 0.714 0.918 0.816 0.7 0.816 0.632
84.91 57.05 0.15 22 0.01 1 1 0.333 0.976 0.655 0.47 0.654 0.309
Haberman 24 100 76.14 62.38 0.39 42 1 1 2 0.444 0.876 0.66 0.5 0.66 0.32 1.82
68.3 66.49 1.12 11 1 2 7 0.63 0.702 0.666 0.51 0.666 0.332
73.53 0 0.26 23 0.94 2 1 0 1 0.5 0 0.5 0
200 76.14 57.81 1.38 29 0.12 3 7 0.37 0.902 0.636 0.45 0.636 0.272 3.8
67.32 66.29 1.13 3 0.94 2 7 0.642 0.684 0.663 0.51 0.663 0.326
75.82 62.22 0.39 42 0.94 1 2 0.444 0.871 0.658 0.49 0.657 0.315
1000 76.14 62.38 0.39 35 0.94 1 2 0.444 0.876 0.66 0.5 0.66 0.32 19.47
70.92 67.21 1.6 11 0.94 3 10 0.605 0.747 0.676 0.52 0.676 0.352
73.86 37.54 0.26 49 0.94 1 1 0.148 0.951 0.55 0.23 0.549 0.099
48 100 76.14 62.38 0.39 49 0.94 1 2 0.444 0.876 0.66 0.5 0.66 0.32 4.29
68.95 67.35 1.09 15 0.63 2 7 0.642 0.707 0.674 0.52 0.674 0.349
73.86 37.54 0.26 49 0.94 1 1 0.148 0.951 0.55 0.23 0.549 0.099
200 76.14 62.38 0.39 49 0.94 1 2 0.444 0.876 0.66 0.5 0.66 0.32 6.74
69.28 67.57 1.09 24 0.63 2 7 0.642 0.711 0.677 0.53 0.676 0.353
73.86 34.43 0.26 49 0.56 1 1 0.123 0.96 0.542 0.2 0.541 0.083
123

| 12878 |     |     |     |     |     | R.Guidoetal. |
| ----- | --- | --- | --- | --- | --- | ------------ |
Table7 continued
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
| Popsize Gen | f1 f2 | f3 C γ | C1 C2 | Sens Spec | ROCarea F-M | BA Y |
| ----------- | ----- | ------ | ----- | --------- | ----------- | ---- |
1000 76.14 62.38 0.39 34 0.94 1 2 0.444 0.876 0.66 0.5 0.66 0.32 27.73
|     | 69.61 67.33 | 2.7 9 1      | 5 17 | 0.63 0.72 | 0.675 0.52 | 0.675 0.35 |
| --- | ----------- | ------------ | ---- | --------- | ---------- | ---------- |
|     | 73.53 0     | 0.26 10 0.94 | 7 1  | 0 1       | 0.5 0      | 0.5 0      |
Hepatitis 24 100 87.1 79.47 0.45 28 0.01 4 3 0.688 0.919 0.803 0.69 0.803 0.607 0.4
83.23 82.49 0.61 6 0.01 9 2 0.813 0.837 0.825 0.67 0.825 0.65
83.23 67.78 0.17 28 0.01 1 1 0.5 0.919 0.709 0.55 0.709 0.419
200 87.1 80.9 0.32 32 0.01 3 2 0.719 0.911 0.815 0.7 0.815 0.63 0.58
83.23 82.49 0.61 6 0.01 9 2 0.813 0.837 0.825 0.67 0.825 0.65
84.52 71.89 0.15 32 0.01 1 1 0.563 0.919 0.741 0.6 0.741 0.482
1000 87.1 80.9 0.32 35 0.01 3 2 0.719 0.911 0.815 0.7 0.815 0.63 1.9
83.87 84.06 0.29 8 0.01 5 1 0.844 0.837 0.841 0.68 0.840 0.681
|     | 79.35 0 | 0.21 8 0.01 | 1 3 | 0 1 | 0.5 0 | 0.5 0 |
| --- | ------- | ----------- | --- | --- | ----- | ----- |
48 100 86.45 80.54 0.33 13 0.02 3 2 0.719 0.902 0.811 0.69 0.810 0.621 0.74
83.23 83.65 0.59 7 0.01 10 2 0.844 0.829 0.837 0.68 0.836 0.673
85.81 74.18 0.14 26 0.02 1 1 0.594 0.927 0.76 0.63 0.760 0.521
200 87.1 80.9 0.32 35 0.01 3 2 0.719 0.911 0.815 0.7 0.815 0.63 1.1
81.94 81.68 0.71 15 0.01 11 2 0.813 0.821 0.817 0.65 0.817 0.634
84.52 71.89 0.15 34 0.01 1 1 0.563 0.919 0.741 0.6 0.741 0.482
1000 87.1 80.9 0.32 32 0.01 3 2 0.719 0.911 0.815 0.7 0.815 0.63 4.03
83.87 84.06 0.29 8 0.01 5 1 0.844 0.837 0.841 0.68 0.840 0.681
84.52 71.89 0.15 34 0.01 1 1 0.563 0.919 0.741 0.6 0.741 0.482
Table8 Algorithm2:ExperimentalresultsonthedatasetsPima,WDBC,andWPBC
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
γ
| Popsize Gen | f1 f2 | f3 C | C1 C2 | Sens Spec | ROCarea F-M | BA Y |
| ----------- | ----- | ---- | ----- | --------- | ----------- | ---- |
Pima 24 100 77.73 73.2 1.02 5 0.24 5 4 0.623 0.86 0.742 0.66 0.741 0.483 7.8
|     | 74.35 76.28 | 0.68 5 0.53 | 5 2 | 0.843 0.69 | 0.767 0.7 | 0.766 0.533 |
| --- | ----------- | ----------- | --- | ---------- | --------- | ----------- |
77.08 70.34 0.23 23 0.32 1 1 0.56 0.884 0.722 0.63 0.722 0.444
77.47 70.26 0.23 23 0.24 1 1 0.552 0.894 0.723 0.63 0.723 0.446
200 77.99 70.9 0.44 4 0.53 2 2 0.56 0.898 0.729 0.64 0.729 0.458 12.41
|     | 74.35 76.28 | 0.68 5 0.53 | 5 2 | 0.843 0.69 | 0.767 0.7 | 0.766 0.533 |
| --- | ----------- | ----------- | --- | ---------- | --------- | ----------- |
74.74 58.03 0.28 5 0.53 1 2 0.351 0.96 0.655 0.49 0.655 0.311
1000 77.47 70.89 0.45 48 0.24 2 2 0.567 0.886 0.727 0.64 0.726 0.453 52.83
77.47 70.1 0.23 12 0.24 1 1 0.549 0.896 0.722 0.63 0.722 0.445
74.48 76.33 0.68 48 0.13 5 2 0.84 0.694 0.767 0.7 0.767 0.534
48 100 78.13 71.13 0.22 3 0.63 1 1 0.563 0.898 0.731 0.64 0.730 0.461 9.86
|     | 74.35 76.28 | 0.68 3 0.58 | 5 2 | 0.843 0.69 | 0.767 0.7 | 0.766 0.533 |
| --- | ----------- | ----------- | --- | ---------- | --------- | ----------- |
200 78.13 71.13 0.22 3 0.63 1 1 0.563 0.898 0.731 0.64 0.730 0.461 15.34
75.13 75.44 0.33 10 0.42 2 1 0.765 0.744 0.754 0.68 0.754 0.509
|     | 74.35 76.22 | 0.68 2 0.63 | 5 2 | 0.84 0.692 | 0.766 0.7 | 0.766 0.532 |
| --- | ----------- | ----------- | --- | ---------- | --------- | ----------- |
1000 78.13 71.13 0.22 3 0.63 1 1 0.563 0.898 0.731 0.64 0.730 0.461 62.73
78.13 72.34 2.11 1 0.63 10 9 0.593 0.882 0.738 0.65 0.737 0.475
74.22 75.93 0.7 3 0.42 5 2 0.828 0.696 0.762 0.69 0.762 0.524
123

Ahyper-parametertuningapproach... 12879
Table8 continued
Dataset Gen.param. Fitnessfunctions OptimizedHyper-par Performancemetrics Time
Popsize Gen f1 f2 f3 C γ C1 C2 Sens Spec ROCarea F-M BA Y
WDBC 24 100 97.42 97.73 0.09 19 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 0.87
97.14 97.7 0.04 4 0.18 1 7 0.996 0.959 0.977 0.96 0.977 0.955
200 97.42 97.73 0.09 19 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 2.59
97.28 97.43 0.04 4 0.01 1 3 0.979 0.969 0.974 0.96 0.974 0.948
97.14 97.7 0.04 4 0.18 1 7 0.996 0.959 0.977 0.96 0.977 0.955
1000 97.42 97.73 0.09 14 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 13.77
97.14 97.7 0.03 14 0.24 1 4 0.996 0.959 0.977 0.96 0.977 0.955
48 100 97.42 97.73 0.09 19 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 2.52
97.28 97.43 0.04 4 0.01 1 3 0.979 0.969 0.974 0.96 0.974 0.948
97.14 97.7 0.04 4 0.18 1 7 0.996 0.959 0.977 0.96 0.977 0.955
200 97.42 97.73 0.09 19 0.24 3 7 0.988 0.967 0.977 0.96 0.977 0.955 5.37
97.28 97.43 0.04 4 0.01 1 3 0.979 0.969 0.974 0.96 0.974 0.948
97.14 97.7 0.04 4 0.18 1 7 0.996 0.959 0.977 0.96 0.977 0.955
1000 97.42 97.73 0.16 16 0.27 5 12 0.988 0.967 0.977 0.96 0.977 0.955 25.72
97.14 97.13 0.03 4 0.27 1 1 0.971 0.972 0.971 0.96 0.971 0.943
WPBC 24 100 76.26 0 0.24 49 0.01 1 1 0 1 0.5 0 0.5 0 0.96
69.19 60.78 0.55 1 0.18 3 1 0.489 0.755 0.622 0.43 0.622 0.244
200 77.27 48.83 3.36 9 0.01 17 7 0.255 0.934 0.595 0.35 0.594 0.189 1.61
65.15 62.29 2.95 5 0.01 17 5 0.574 0.675 0.625 0.44 0.624 0.249
76.26 0 0.24 42 0.01 1 7 0 1 0.5 0 0.5 0
1000 77.27 48.83 3.36 9 0.01 17 7 0.255 0.934 0.595 0.35 0.594 0.189 4.47
65.15 62.29 2.95 5 0.01 17 5 0.574 0.675 0.625 0.44 0.624 0.249
76.26 0 0.24 5 0.01 1 9 0 1 0.5 0 0.5 0
48 100 76.26 0 0.24 41 0.09 1 2 0 1 0.5 0 0.5 0 1.77
76.26 55.17 0.39 14 0.09 2 1 0.34 0.894 0.617 0.41 0.617 0.234
200 77.78 29.08 0.25 49 0.27 1 6 0.085 0.993 0.539 0.15 0.539 0.078 2.64
77.78 25.26 0.22 48 0.27 1 7 0.064 1 0.532 0.12 0.532 0.064
67.17 60.71 3.04 47 0.01 17 5 0.511 0.722 0.616 0.42 0.616 0.233
1000 76.26 0 0.24 28 0.01 1 7 0 1 0.5 0 0.5 0 8.55
65.15 59.59 3.25 37 0.01 18 5 0.511 0.695 0.603 0.41 0.603 0.206
7 Conclusion or equivalent to other algorithms proposed in the literature
forCS-SVMhyper-parametersoptimization.Overall,taking
SupportvectormachinesareoneofthebestMLmodelsfor intoaccountthreepredictivemetrics,i.e.,accuracy,G-Mean,
solvingseveralreal-lifeclassificationproblems.However,as and average cost,thebest hyper-parameter configuration is
inotherMLtechniques,theirperformancedependsonhyper- foundinshortcomputationaltime,mainlyifcomparedwith
parameters. gridsearchapproach.Hence,thisapproachcanbeconsidered
In this paper, we have investigated and proposed an asagoodsolutionforaddressingimbalanceddatasetclassi-
approachthatcombinesgeneticalgorithmsanddecisiontrees ficationandhyper-parametertuning,astheyarechallenging
tooptimizehyper-parametersofC-SVMs.Theoptimumval- problemsinclassificationresearch.
uesoftheregularizationparameter,costsofclassesandthe We suggest evaluating the performance of classifiers on
parametersoftheRBFkernelfunctionaresearchedforSVM. medicaldatabysuitablemeasuresotherthanaccuracy.Our
Wetestedthealgorithmonsixbenchmarkdatasets,which future work is to extend and assess the proposed approach
areimbalanced.Weevaluatedtheperformanceofthemod- to investigate hyper-parameter tuning of different machine
elsbyseveralperformancemetrics.Theframeworkisbetter learningmethods.
123

12880 R.Guidoetal.
Fig.6 ValuesofthesixperformancemeasuresoftheParetopointsfoundforAppendicitis,Haberman,Hepatitis,andPimadatasets
Fig.7 ValuesofthesixperformancemeasuresoftheParetopointsfoundforWDBCandWPBCdatasets
Acknowledgements Theresearchhasbeenpartiallysupportedbythe professionalrelationships,affiliations,knowledgeorbeliefs)inthesub-
researchprojectSI.F.I.PA.CRO.DE.Sviluppoeindustrializzazionefar- jectmatterormaterialsdiscussedinthismanuscript.
maci innovativi per terapia molecolare personalizzata PA.CRO.DE.
(PON ARS01_00568, CUP: B29C20000360005, CONCESSIONE Open Access This article is licensed under a Creative Commons
RNA-COR: 4646672), Italian Ministry of University and Research, Attribution4.0InternationalLicense,whichpermitsuse,sharing,adap-
2021. tation, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the
Declaration source, provide a link to the Creative Commons licence, and indi-
cateifchangesweremade.Theimagesorotherthirdpartymaterial
inthisarticleareincludedinthearticle’sCreativeCommonslicence,
Conflictofinterest Theauthorsofthemanuscriptdeclarethattheyhave
unlessindicatedotherwiseinacreditlinetothematerial.Ifmaterial
noaffiliationswithorinvolvementinanyorganizationorentitywith
is not included in the article’s Creative Commons licence and your
any financial interest (such as honoraria; educational grants; partici-
intended use is not permitted by statutory regulation or exceeds the
pationinspeakers’bureaus;membership,employment,consultancies,
permitteduse,youwillneedtoobtainpermissiondirectlyfromthecopy-
stockownership,orotherequityinterest;andexperttestimonyorpatent-
rightholder.Toviewacopyofthislicence,visithttp://creativecomm
licensingarrangements),ornon-financialinterest(suchaspersonalor
ons.org/licenses/by/4.0/.
123

Ahyper-parametertuningapproach... 12881
References LessmannS,StahlbockR,CroneR(2005)Optimizinghyperparameters
ofsupportvectormachinesbygeneticalgorithms.In:IC-AIpp
AgrawalN,KumarA,BajajV(2017)Anewdesignmethodforstable 74–82
IIRfilterswithnearlylinear-phaseresponsebasedonfractional MehrbakhshN,HosseinA,LeilaSetal(2019)Apredictivemethodfor
derivativeandswarmintelligence.IEEETransactionsonEmerging hepatitisdiseasediagnosisusingensemblesofneuro-fuzzytech-
TopicsinComputationalIntelligence1(6):464–477 nique.JInfectPublicHealth12(1):13–20
AgrawalN,KumarA,BajajV(2018)DesignofdigitalIIRfilterwith NoiaA,MartinoA,MontanariPetal(2020)Supervisedmachinelearn-
lowquantizationerrorusinghybridoptimizationtechnique.Soft ingtechniquesandgeneticoptimizationforoccupationaldiseases
Comput22(9):2953–2971 riskprediction.SoftComput24:4393–4406
AminA,AnwarS,AeaAdnan(2016)Comparingoversamplingtech- PhienthrakulT,KijsirikulB(2010)Evolutionarystrategiesforhyper-
niquestohandletheclassimbalanceproblem:acustomerchurn parametersofsupportvectormachinesbasedonmulti-scaleradial
predictioncasestudy.IEEEAccess4:7940–7957 basisfunctionkernels.SoftComput14:681–699
Bao-DeL,Xin-YangZ,MeiZetal(2021)Improvedgeneticalgorithm- QiZ,TianaY,ShiaYetal(2013)Cost-sensitivesupportvectormachine
based research on optimization of least square support vec- forsemi-supervisedlearning.ProcediaComputSci18:1684–1689
tor machines: an application of load forecasting. Soft Comput RamírezA,RomeroJR,VenturaS(2015)AnextensibleJCLEC-based
10(1007):5674–9 solution for the implementation of multi-objective evolutionary
BergstraJ,BardenetR,BengioY,etal(2011)Algorithmsforhyper- algorithms.In:proceedingsofthecompanionpublicationofthe
parameteroptimization.In:andCAI(ed)Proceedingsofthe24th 2015annualconferenceongeneticandevolutionarycomputation,
international conference on neural information processing sys- pp1085–1092
tems.USA,pp2546–2554 RamírezA,RomeroJR,García-MartínezCetal(2019)JCLEC-MO:
BreimanL,FriedmanJH,OlshenR,etal(1984)R.A.andStone,C.J. ajavasuiteforsolvingmany-objectiveoptimizationengineering
Classificationandregressiontrees.CRCpress problems.EngApplArtifIntell81:14–28
ChawlaN,BowyerK,LeaHall(2002)Smote:Syntheticminorityover- ScholkopfB,SmolaAJ(2001)LearningwithKernels:SupportVector
samplingtechnique.JArtifIntellRes16:321–357 Machines,Regularization,Optimization,andBeyond.MITPress,
Cortes C, Vapnik V (1995) Support-vector network. Mach Learn Cambridge,MA,USA
20:273–297 Sokolova M, Japkowicz N, Szpakowicz S (2006) Beyond accuracy,
CristianiniN,Shawe-TaylorJ(2000)AnIntroductiontoSupportVector F-score and ROC: A family of discriminant measures for per-
Machines and other kernel-based learning methods. Cambridge formance evaluation. In: Sattar A, Kang B (eds) Advances in
UniversityPress Artificial Intelligence. Lecture Notes in Computer Science, vol
DattaS,DasS(2015)Near-bayesiansupportvectormachinesforimbal- 4304.Springer,Berlin,Heidelberg
anceddataclassificationwithequalorunequalmisclassification SrinivasN,DebK(1994)Multiobjectiveoptimizationusingnondomi-
costs.NeuralNetw70:39–52 natedsortingingeneticalgorithms.EvolComput2(3):221–248
DebK,GoelT(2001)Controlledelitistnon-dominatedsortinggenetic Tao X, Li Q, Guo W et al (2019) Self-adaptive cost weights-based
algorithms for better convergence. In: Lothar T, Kalyanmoy D, support vector machine cost-sensitive ensemble for imbalanced
CoelloCetal(eds)ZitzlerEckart.EvolutionaryMulti-Criterion dataclassification.InfSci487:31–56
Optimization,Springer,BerlinHeidelberg,pp67–81 TurneyPD(1995)Cost-sensitiveclassification:empiricalevaluationof
DebK,PratapA,AgarwalSetal(2002)Afastandelitistmultiobjective ahybridgeneticdecisiontreeinductionalgorithm.JArtifIntRes
geneticalgorithm:NSGA-II.IEEETransEvolComput6:182–197 2:369–409
Dwivedi AK, Ghosh S, Londhe ND (2018) Review and analysis of VapnikV(1998)StatisticalLearningTheory.Wiley,JohnSonsInc
evolutionary optimization-based techniques for fir filter design. Veropoulos K, Campbell C, Cristianini N (1999) Controlling the
CircuitsSystSignalProcess37(10):4409–4430 sensitivityofsupportvectormachines.In:proceedingsoftheinter-
GalarM,FernandezA,BarrenecheaEetal(2012)Areviewonensem- nationaljointconferenceonAL,pp55–60
bles for the class imbalance problem: Bagging, boosting, and WittenI,FrankE(2005)DataMiningPracticalMachineLearningTools
hybrid-basedapproaches,systems,man,andcybernetics,partc: andTechniques.MorganKaufmannPublishers,CA
Applicationsandreviews.IEEETrans42(4):463–484 YuX,WangX(2017)Anovelhybridclassificationframeworkusing
GoldbergDE,HollandJ(1988)Geneticalgorithmsandmachinelearn- svmanddifferentialevolution.SoftComput21:4029–4044
ing.MachLearn3(2):95–99
GuidoR,ConfortiD(2017)Hybridgeneticapproachforsolvingan
Publisher’sNote SpringerNatureremainsneutralwithregardtojuris-
integratedmulti-objectiveoperatingroomplanningandscheduling
dictionalclaimsinpublishedmapsandinstitutionalaffiliations.
problem.ComputOperRes87:270–282
GuidoR,GrocciaMC,ConfortiD(2021)Hyper-ParameterOptimiza-
tion in Support Vector Machine on unbalanced datasets using
GeneticAlgorithms.In:OptimizationinArtificialIntelligenceand
DataSciences,AIROSpringerSeries(inpress)
HofmannT,ScholkopfB,SmolaAJ(2008)Kernelmethodsinmachine
learning.AnnStatistpp1171–1220
Holland JH (1975) Adaptation in natural and artificial systems: An
introductory analysis with applications to biology, control, and
artificialintelligence.MichiganPress
IranmehrA,Masnadi-ShiraziH,VasconcelosN(2019)Cost-sensitive
supportvectormachines.Neurocomputing343:50–64
JapkowiczN,StephenS(2002)Theclassimbalanceproblem:asys-
tematicstudy.IntellDataAnal6:429–449
JoT,JapkowiczN(2004)Classimbalancesversussmalldisjuncts.ACM
SIGKDDExplorationsNewslett6:40–49
123