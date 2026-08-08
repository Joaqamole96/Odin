AppliedSoftComputing134(2023)110020
ContentslistsavailableatScienceDirect
AppliedSoftComputing
journalhomepage:www.elsevier.com/locate/asoc
Weightedkappameasuresforordinalmulti-classclassification
performance
AyferEzgiYilmaza,HaydarDemirhanb,∗
aDepartmentofStatistics,HacettepeUniversity,Ankara,Turkey
bMathematicalSciencesDiscipline,SchoolofScience,RMITUniversity,Melbourne,Australia
a r t i c l e i n f o a b s t r a c t
Articlehistory: Assessing the classification performance of ordinal classifiers is a challenging problem under imbal-
Received10March2022 anced data compositions. Considering the critical impact of the metrics on the choice of classifiers,
Receivedinrevisedform18December2022 employing a metric with the highest performance is crucial. Although Cohen’s kappa measure is
Accepted5January2023 used for performance assessment, there are better-performing agreement measures under different
Availableonline13January2023
formationsofordinalconfusionmatrices.Thisresearchimplementsweightedagreementmeasuresas
Keywords: evaluationmetricsforordinalclassifiers.Theapplicabilityofagreementandmainstreamperformance
Accuracy metrics to various practice fields under challenging data compositions is assessed. The sensitivity
Agreementmeasures of the metrics in detecting subtle distinctions between ordinal classifiers is analyzed. Five kappa-
Evaluationmetric like agreement measures with six weighting schemes are employed as evaluation metrics. Their
Matthewscorrelationcoefficient reliability/usefulness is compared to the mainstream and recently proposed metrics, including F1,
Performancemetric Matthews correlation coefficient, and informational agreement. The performance of 37 metrics is
Ordinalclassifier
analyzedintwoextensivenumericalstudies,includingsyntheticconfusionmatricesandrealdatasets.
Ordinallabels
Promisingmetricsunderpracticalcircumstancesareidentified,andrecommendationsaboutthebest
metrictoevaluateordinalclassifiersunderdifferentconditionsaremade.Overall,theweightedScott’s
pi-measureisfounduseful,sensitivetosmalldifferencesintheclassificationperformance,andreliable
undergeneralconditions.
©2023TheAuthor(s).PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBY-NC-ND
license(http://creativecommons.org/licenses/by-nc-nd/4.0/).
1. Introduction the performance of ordinal classifiers with the highest possible
accuracy.
Classifying subjects into multiple ordinal classes, namely or- The evaluation of ordinal classifiers’ performance is directly
dinal multi-class classification or ordinal classification, is one of related to the used evaluation metric and the characteristics of
themostfrequentexercisesofautomaticclassificationsystemsin the training or test dataset, which we call ‘‘the composition of
patternrecognition,machinelearning,anddeeplearningsystems. thedataset’’throughoutthemanuscript.Whenthedistributionof
Theproblemconsideredhereistoassigneachobjectinasample subjects into ordinal classes is imbalanced, mainstream metrics
to one of the ordered classes of a categorical response variable such as accuracy, precision, and recall are negatively impacted;
using an ordinal classifier. In pattern recognition, ordinal multi- hence,theydonotpreciselyassessclassifiers’performance[5,6].
class classification is used in the classification of different types Therefore,theuseofothermeasuressuchasF1score[7],Cohen’s
ofimagessuchashyperspectralimages[1],data-likeimages[2], (weighted)κ (kappa)-measure[8]andMatthewscorrelationco-
radar images [3], or images from medical diagnosis systems [4]. efficient (MCC) [9] is proposed. MCC is observed to perform
Accurate evaluation of ordinal classifiers’ performance is a chal- better than the F1 score and κ-measure for binary classifica-
lenge under different circumstances of data. Therefore, many tion[10,11].Formulti-classclassification,Ráczetal.[6]identify
metricshavebeenproposedtoevaluateclassifiers.Thequalityof better performance for F1 score than MCC and find that MCC is
training a model or network is related to the preciseness of the more sensitive to the data composition. Although Rácz et al. [6]
classifier against true classes in a labeled dataset [4]. A metric
includeCohen’sunweightedκintheirstudy,theydonotgiveany
can also be used as a loss function to optimize in an image specific inference about the comparison of Cohen’s unweighted
classification system [4]. In this sense, it is crucial to evaluate
κ-measuretoF1scoreandMCCforordinalclassifiers.Theuseof
Cohen’slinearorquadraticweightedandunweightedκ-measures
∗ is found suitable for assessing the performance of multi-class
Correspondingauthor.
classifiers [8]. However, Czodrowski [8] do not distinguish or-
E-mailaddresses: ezgiyilmaz@hacettepe.edu.tr(A.E.Yilmaz),
haydar.demirhan@rmit.edu.au(H.Demirhan). dinal classifiers. Cohen’s unweighted κ-measure is compared to
https://doi.org/10.1016/j.asoc.2023.110020
1568-4946/©2023TheAuthor(s). PublishedbyElsevierB.V.ThisisanopenaccessarticleundertheCCBY-NC-NDlicense(http://creativecommons.org/licenses/by-
nc-nd/4.0/).

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
a bunch of metrics, including the F1 score in the accuracy of research are to (i) explore the precision/usefulness of weighted
assessing the performance of binary and multi-class classifiers agreement measures as evaluation metrics for ordinal classi-
for balanced and imbalanced data compositions by Ferri et al. fiers, (ii) compare the versatility of agreement metrics and the
[5], without specifically accounting for ordinal classifiers. It is mainstreammetricsunderchallengingcompositionsofconfusion
observed that the unweighted κ-measure shows similar per- matrices in different fields of practice for ordinal classification,
formance as the metric called accuracy for multi-class classi- and (iii) identify the promising metrics under practical circum-
fiers in general. However, it shows similar performance with stancesandmakerecommendationsaboutthebestmetrictouse
the F1 score for large datasets with more than 1000 observa- fortheevaluationofordinalclassifiers.
tions[5].Seriousconcernshavealsobeenraisedagainsttheuse To fulfill the aims, our objectives are to (i) implement the
of Cohen’s κ-measure in assessing the performance of multi- weightedagreementmeasuresfortheevaluationofordinalclas-
class classifiers. There is a strong correlation between Cohen’s sifiers for balanced and imbalanced data compositions, (ii) con-
unweightedκ-measureandMCC,andhighκ valuesareobserved ductanumericalstudywithsyntheticconfusionmatricestosee
forpoorlyperformingclassifierswithimbalanceddatawhileMCC thequalityofthemetricsundercontestingcompositionsofcon-
was insensitive to this case [12]. Specifically, mean absolute er- fusion matrices, and (iii) run a second numerical study with the
ror (MAE), its variations, and mean squared error (MSE) are outputsofordinalclassifierswithrealdatafromavastvarietyof
considered for the evaluation of ordinal classification perfor- thefieldstoassessthesensitivityofmetricstosmalldifferences
manceunderimbalanceddatacompositions[13,14].Cardosoand between ordinal classifiers. Under these objectives, we consider
Sousa[15]proposeanordinalclassificationindex(OCI),consider weighted versions of κ, π, α, BP and AC2 metrics and compare
Misclassification Error Rate (MER) for ordinal classification per- their performance against the mainstream metrics accuracy, re-
formance,andcompareMERwithMAEandMSE.However,they call, precision, F1, MCC and the recently proposed informational
do not consider mainstream and (weighted) agreement metrics agreementthroughtwoextensivenumericalstudies.Intotal,we
consider 37 metrics and assess them under artificially created
forordinalclassificationperformance.
In image classification studies, Cohen’s κ-measure is found scenarioscomposedofthetrueperformanceoftheclassifier,the
degree of imbalance in the data (the composition of data), and
useful for assessing multi-class classifiers’ performance. Some
differentmisclassificationscenariosfortheclassesoftheordinal
performance comparisons among well-known metrics, F1 score
and Cohen’s κ are reported. The grounds for using kappa-like dependent feature in the first numerical study. This numerical
studyrevealsthemetrics’performance/usefulnessundervarious
agreementmeasurestoassessmulti-classclassifiers’performance
confusion matrix formations. In the second numerical study, we
is that the confusion matrix is essentially a cross table showing
compare the metrics in terms of their sensitivity in distinguish-
the agreement between two raters, represented by the obser-
ing two classifiers with similar classification performance using
vations and estimations. In this case, the confusion matrix is
40 real datasets, including balanced, imbalanced, and extremely
taken as an ‘‘agreement table’’ that shows the classification of
imbalanced data compositions from social science, life sciences,
tworatersintomultipleclassesofanoutcomevariable.Then,the
engineering, and other areas of practice. This numerical study
levelofagreementbetweentworatersisequivalenttothelevelof
is important to observe the ability of metrics to perceive even
goodnessofclassification.Inthissense,allkappa-likeagreement
smalldifferencesinclassificationperformance,whichisahighly
measures can be considered as an evaluation metric for ordinal
classifiers. However, Cohen’s κ-measure is proposed to be used desiredqualityforanevaluationmetric.Thecontributionsofthis
study are that (i) we explore the performance of a wide range
when there is no ordering among the classes of the variable of
of unweighted and weighted agreement measures as metrics
interest (nominal type classes). Thus, it does not consider the
forordinalmulti-classclassifiers,(ii)comparativelyexaminethe
degree of deviance from the main diagonal of the classification.
performanceofthemainstreammetrics,and(iii)identifyametric
For example, in classifying objects in images into the classes
thatissuperiortothemainstreammetricsthatcanbeusedunder
‘‘bicycle’’,‘‘car’’,‘‘airplane’’,threeclassesareofnominaltypesince
different data compositions and areas of practice as a generic
there is no hierarchy among them. When there is a hierarchy
metric.
amongtheclasses(ordinaltypeclasses),weneedtoconsiderthis
Section2outlinestherelatedworksintheliterature.Section3
hierarchy in the analysis. For example, diabetic retinopathy is a
describes the metrics considered in this study. Sections 4 and 5
serious disease that may lead to visual impairment and can be
presentthenumericalstudieswithsyntheticconfusionmatrices
prevented if detected early. For the detection, lesions related to
and real data. Section 6 is devoted to the general recommenda-
thediseasearescreenedinretinalimages,andaclassificationis
tionsanddiscussions.
donebasedontheseverityofstagesusingautomaticimageclas-
sificationtechniques[4].Duetothenaturalhierarchyamongthe 2. Relatedworks
severitystages,wedealwithanordinalmulti-classclassification
problem.Inthiscase,theweightedversionofCohen’sκ-measure, The use of weighted κ and MCC as a loss function in deep
whichincludestheimpactofthedistancefromthemaindiagonal, learning models for image classification is considered by
is available for use. Since Cohen’s (weighted) κ-measure has de La Torre et al. [4] for general image classification and Kook
some drawbacks [16,17], other measures such as Gwet’s AC2, et al. [2] for the classification of complex data like images into
Scott’sπ(pi),Brennan–Prediger’sBP,andKrippendorff’sα(alpha)
ordinal classes. However, they only consider quadratic weights
are proposed in the agreement studies [18]. However, they are andCohen’sκ whiletherearebetter-performingalternatives.For
not considered as an evaluation metric for ordinal classifiers hyperspectral image classification, both Deng et al. [1] and Sel-
in the literature. When we consider ordinal classes, there are lami and Tabbone [19] employ accuracy and unweighted κ to
other weighting schemes besides linear and quadratic weights, evaluatetheirproposedmethodsformulti-classclassification.
such as ordinal, radical, ratio, circular, and bipolar weights to Ben-David[20]focusontheexpertsystemsforcost-sensitive
be used with weighted versions of the agreement measures to applications and propose a new strategy based on weighted κ-
accountfortheordinalityoftheclasses[18].Duetotheinterac- measuretoassesstheperformanceofmulti-classclassifiers.They
tion between the assumptions behind agreement measures and only consider unweighted, linear and quadratic weighted Co-
weighting schemes, each weighted agreement measure would hen’s κ-measure without distinguishing imbalance in data and
performsatisfactorilyinmeasuringaclassifier’sperformanceun- comparing the accuracy of κ-measure to others such as accu-
der a different data composition. Therefore, the aims of this racy, precision, recall, and F1 score. García et al. [21] consider
2

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Cohen’sunweightedκ-measureandclassificationrateformulti- composition and observe that AUC and MCC have consistent
classclassifiersforgenetics-basedmachinelearningimplementa- performance across different classifiers with imbalanced data
tions.Thisstudyshowsthattheprecisionofmetricscanvaryfor composition. Rácz et al. [6] conduct a statistical analysis on
classificationproblemsindifferentfieldsofapplication. the performance of 28 metrics, including unweighted κ, MCC,
Ferri et al. [5] conduct an extensive experimental study to F1 score, accuracy, diagnostic odds ratio, and AUC by taking
assessthereliabilityof18metricsinclassificationproblems.They data composition (imbalanced/balanced), level of classification
presentverydetailedbackgroundinformationaboutthedifferent (binary/multi-class), and the performance of metric as factors
types of metrics, including their taxonomy. They only consider againstthesumofrankingdifferencesoverthreedatasets.They
theunweightedversionofκ-measureanddonotincludeMCCin observethatmostofthemetricsaresensitivetothecomposition
thecomparisonstudy.SomesimilaritiesbetweentheF1scoreand ofthedatasetandtheF1scoreandthediagnosticoddsratioare
κ-measure,andaccuracyandκ-measureareobservedfordiffer- theleastsensitiveones.Wardhanietal.[24]focusonimbalanced
entcompositionsofdatabyFerrietal.[5].Czodrowski[8]studies datacompositionandcomparethereliabilityofF1score,g-mean,
theadvantagesanddisadvantagesofCohen’sunweightedκ asa MCC,unweightedκ,andAUCmetricsoveranempiricalstudyon
metric of performance for the classification problem in machine the cabbage image classification. They observe that accuracy, F1
learning and cheminformatics. He creates various data compo- score, g-mean, MCC, and κ provide similar results for different
sitions to compare the reaction of precision, recall, accuracy, κ, confusionmatriceswhileAUCissensitivetothechanges.When
prevalence, and bias and observes that κ-measure is a useful the degree of imbalance is high, Wardhani et al. [24] suggest
metric within this set of metrics. Saito and Rehmsmeier [22] not to use MCC and unweighted κ-measure to avoid misleading
compare the performance of precision/recall plots to Receiver results.
OperatingCharacteristics(ROC)plotsinassessingthebinaryclas- Inrecentstudies,Casagrandeetal.[25]proposeanewmetric
sifiers on imbalanced data. They consider the metrics computed calledinformationalagreement(IA)tomeasurethestrengthbe-
tweentwoassessorsforbinaryandmulti-classlabelstoavoidthe
usingtheinformationintheconfusionmatrix,suchasaccuracy,
disadvantagesofκ-measure.TheytestIAunderthecaseswhere
F1 score, MCC, and precision and observe that performance of
theκ-measuregivesproblematicresultsbytakingtwodiagnostic
precision/recallplotsissuperiortoROCplots.Korotcovetal.[23]
classifiersasassessors.DelgadoandTibau[12]focusonthesim-
compare the performance of deep neural networks to that of
ilaritiesanddifferencesbetweenCohen’sunweightedκ-measure
mainstream machine learning methods by using AUC, F1 score,
Cohen’s unweighted κ and MCC. They observe similar κ and andMCCundervariouscompositionsoftheconfusionmatrixfor
binaryandmulti-classclassifiers.Theytheoreticallyandnumeri-
MCCvaluesforimplementingdeeplearningandmachinelearn-
callystudytheequivalencebetweenMCCandunweightedκ and
ing methods with pharmaceutical data. Since we work with the
figureouttheformationsofconfusionmatrixwhereunweighted
metrics relying on the qualitative understanding of error that
κ should be avoided. Chicco and Jurman [11] consider MCC and
take the number of false classifications into account [5] in this
observeitsadvantagesovertheF1scoreandaccuracyforbinary
study, we do not consider either ROC or AUC. The metrics, such
classification. They conclude that MCC is a more reliable metric
as logarithmic loss, require prediction probabilities. However,
for assessing performance for binary classifiers and should be
we directly work with the confusion matrices for better gener-
preferredoveraccuracyandF1score.
alizability instead of working with a specific model. Therefore, There is a close theoretical relationship between κ-measure
metrics requiring prediction probabilities are not considered in
and MCC [12,26] when the confusion matrix is symmetric. Del-
thisstudy. gado and Tibau [12] also observe that κ-measure differs from
Forordinalmulti-classclassification,itisessentialtoaccount
MCC and is not reliable under imbalanced compositions of data.
for the severity of the error. In that sense, the use of metrics
This result motivates us to explore other alternatives of
that do not count for the magnitude of the error, such as ac- κ-measure to identify a better metric for assessing the perfor-
curacy metric, is not suitable [13,15]. Gaudette and Japkowicz
mance of multi-class classifiers with imbalanced datasets. Dif-
[13] consider MAE and MSE to capture the magnitude of the
ferent to the existing studies, we consider four alternatives of
errorandfindthatMAEandMSEperformbetterthanthemetric the κ-measure with six weighting schemes under different data
accuracyforimbalanceddatasets.Baccianellaetal.[14]propose
compositionsinthisstudy.
macro-averaged versions of MAE for imbalanced datasets but
In general, different studies in different areas have produced
do not compare them with the mainstream metrics. When the
contradictory conclusions on the suitability of MCC and Cohen’s
number of ordinal levels increases, it is appropriate to use MAE κ-measure. Although the characteristics of different areas are
and MSE based on the approximation to the continuous scale.
influentialinthiscontradiction,thesestudiesarelimitedtotheir
However, when the number of levels is not large enough to
simulationornumericalexperimentationspaces.Thisisanother
support such an approximation, it is essential to identify the
motivationforconductingextensivenumericalstudieswithsyn-
promisingmetricsthatcapturethemagnitudeoferrorforordinal thetic and real data from different fields to explore the preci-
classification. Cardoso and Sousa [15] define OCI directly using sion/usefulnessofotherweightedagreementmeasuresasmetrics
the confusion matrix and consider the relative ordering of true formulti-classclassifiersforordinallabels.
andpredictedclasses(concordantanddiscordantpairs)andtheir
deviation from the main diagonal of the confusion matrix. The 3. Performancemetricsformulti-classclassifiers
weighted agreement metrics considered in this study capture
concordanceanddiscordanceintheconfusionmatrixandaccount Evaluationmetricsdifferaccordingtothewaytheyhandlethe
for the magnitude of discrepancy between the observed and error. The measures based on the qualitative understanding of
predictedclassificationofthelabels,inadditiontothedegreeof errortakeintoaccountthenumberoffalseclassifications.Those
similarity between them. Thus, figuring out the usefulness and regarding the probabilistic understanding of error are based on
efficiencyoftheweightedagreementmetricsintheevaluationof the distance from the true probability and are mostly used in
ordinalclassificationperformanceisanimportantcontribution. reliabilitystudies.Themetricsrelatedtotherankingaccuracyof
Boughorbel et al. [9] propose optimizing the metrics to han- the model are used when the classifiers are evaluated on how
dle the imbalance in data and develop a new binary classifier well they select a given number of best labels/subjects from a
based on the optimization of MCC for imbalanced data. They datasetsuchasrecommendersystems[5].Inthisarticle,wefocus
compare MCC, AUC, Accuracy, and F1 under imbalanced data onthemetricsrelyingonthequalitativeunderstandingoferror.
3

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Table1 classmembershipsoflabelsusingthecellcountsofthecon-
Theconfusionmatrixforaclassifier. fusionmatrix.Ittakesvaluesin[−1,1]where−1represents
Predictedclass Row thepoorest,and1showsperfectclassificationperformance:
Actualclass 1 2 . . . 1 n n . . . 1 2 1 1 2 n n . . . 1 2 2 2 . . . .. . . . . . . . n R n . . . 1 2 R R n n . . . m 1 2 a . . rgin MCC = √ (n2 n − ∑ ∑ R i=1 R i= n 1 ii n − 2 i.)( ∑ n2 R i= − 1 n ∑ i.n R i= .i 1 n2 .i ) . (6)
R nR1 nR2 ... nRR nR. • Informational agreement has recently been proposed by
Columnmargin n.1 n.2 ... n.R n Casagrande et al. [25] and is based on the amount of in-
formation (entropy) exchanged between the raters in the
agreementcontext.Intheclassificationperformanceassess-
ment, the higher the agreement between a classifier and
3.1. Mainstreammetrics theactualdistributionoflabels,thehighertheclassification
performanceoftheclassifier.Itiscomputedas
The confusion matrix for a multi-class classifier assigning n
labelsintoRclassesisshowninTable1.Therowsoftheconfusion MI(X,Y) ∑ R ( p )
matrix represent the actual classes, and the columns show the IA= , MI(X,Y)= p log ij ,
predicted classes. In Table 1, n ij denotes the number of labels
min{H(X),H(Y)}
i,j=1
ij R p i.p.i
that are actually in class i and predicted to be in class j, where
i,j = 1,2,...,R. The corresponding cell probability is p = (7)
ij
n ij /n. The row and column totals are shown as row and column ∑ R ∑ R
m
ar
a
e
rg
p
i
i
n
.
s,
=
re
n
sp
i. /
e
n
cti
a
v
n
e
d
ly.
p.
M
j
a
=
rgin
n
a
.j
l
/n
r
,
ow
res
a
p
n
e
d
ctiv
co
e
l
l
u
y.
m
S
n
in
p
ce
ro
t
b
h
a
e
bi
r
li
o
ti
w
es
-
H(X)=−
i=1
p i.log
R
(p i.), andH(Y)=−
i=1
p.i log
R
(p.i ).
totals of the confusion matrix are fixed by the frequencies in
the dataset, the sampling scheme we are working with is the 3.2. Weightedagreementcoefficients
product-multinomialsampling[27].
UsingtheconfusionmatrixinTable1,themainstreammetrics The weighted agreement coefficients are essentially used to
consideredinthisarticlearecalculatedasfollows: evaluate the level of agreement between two raters who clas-
sified the subjects into ordered categories. The general form for
• Accuracyisthemostcommonmetricdefinedastheratioof
agreementcoefficients(A)isdefinedasfollows:
correctlypredictedlabelstothetotalnumberoflabels.
Acc = ∑R i= n 1 n ii. (1) A= P 1 o − − P P e e ( ( A A ) ) , P o = i ∑ ,j R =1 w ij p ij , (8)
• Macro-average recall is also called balanced accuracy and where P is the observed agreement, P is the proportion agree-
o e
computedasthearithmeticmeanofrecallsforallclasses. ment expected by chance, w shows the weight assigned to cell
ij
M.Recall= ∑R i=1 R recall i, and recall i = ∑ R n ii /n i. . (2) ( c i o , e j T ) ff h i o c e f ie t g n h e t e n a e c n r o d a n l f i u s fo s c i r a o m l n c u u m l l a a t a t i t e o r d n ix a , o s a f g n K i d v r e i P p n e p i d e n e n p T d a e o b n r l f d e f s ’s 2 o . α n t m he ea a s g u r r e e em is en as t
i=1
follows[18]:
Themacro-averagerecalliscalled‘‘recall’’intherestofthe
• p a M r r a t e i c c c r i l o s e i - . o a n v s er o a v g e e r p R re c c l i a si s o s n es i . sdefinedasthearithmeticmeanof α w = ( 1− n 1 r¯ ) 1 p − a0 ∑ + R k n , 1 r l ¯ = − 1 w ∑ kl π R k, k l= π 1 k w kl π k π k, (9)
where
M.precision=
∑R
i=1 p R recision i, and precision i = ∑ i=
R
1 n ii /n.i . p a0 = 1 n ∑ n ∑ R r i r k ¯ ( ( r r ¯ ik − . − 1 1 ) ) , r¯ ik. = ∑ R w kl r il , and
(3)
i=1 k=1 i l=1
(10)
n
1∑
Macro-average precision is called ‘‘precision’’ in the rest of π k = r ik r¯.
n
thearticle. i=1
• Mean F1-score is calculated as the arithmetic mean of F1- WhilecomputingKrippendorff’sαforaconfusionmatrix,r =
ik
scoresoverRclasses. 2andr =r¯ =2·RinEqs.(9)and(10).
i
∑R F1 ( precision ×recall ) The critical distinction between agreement metrics is the as-
MeanF1= i=1 i, and F1 =2× i i . sumption about the marginal distributions of assessors, which
R i precision i +recall i corresponds to the confusion matrix’s margins in the classifica-
(4) tion performance context. One of the margins of the confusion
matrix is fixed by the total class frequencies in the data. There-
• MacroF1-scoreiscomputedastheharmonicmeanofmacro-
fore, the agreement coefficients calculated assuming that one of
averaged precision and macro-averaged recall, defined in
themarginsisfixedareexpectedtoperformbetterintheclassifi-
Eqs.(2)and(3),respectively.
cationperformanceevaluation.However,noneoftheagreement
( M.precision×M.recall ) coefficientshasthisassumptionstraightforwardly.Scott’sπ w as-
M.F1=2× M.precision+M.recall . (5) sumesthehomogeneityofmargins[28];hence,itisexpectedto
be a precise metric when the margins of the confusion matrix
• Matthewscorrelationcoefficient [9]giveninEq.(6)measures get closer. Krippendorff’s α does not require the margins of the
thedegreeofcorrelationbetweenthepredictedandactual confusionmatrixtobehomogeneous.Itinsteadcountswherethe
4

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
Table2
Thecalculationoftheproportionagreementexpectedbychance.
|     | Coefficient |     | Symbol | Pe  |     |     |     |     |     |     |     |
| --- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
∑R
|     |               |     | κ   | w             |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|     | Weightedkappa |     | w   | Pe = ijpi.p.j |     |     |     |     |     |     |     |
i,j=1
|     |           |     |     | ∑R        |      | (pi.+     |     |       |      |     |     |
| --- | --------- | --- | --- | --------- | ---- | --------- | --- | ----- | ---- | --- | --- |
|     |           |     | π   | = w       | ,    | = p.i)    |     |       |      |     |     |
|     | Scott’spi |     | w   | Pe ijpipj | pi   |           |     |       |      |     |     |
|     |           |     |     | i,j=1     |      | 2         |     |       |      |     |     |
|     |           |     |     | 1         | ( ∑R | ) ∑R      |     | (pi.+ | p.i) |     |     |
|     | Gwet      |     | AC2 | Pe =      | w    | pi(1−pi), |     | pi =  |      |     |     |
|     |           |     |     | R(R −1)   |      | ij        |     |       | 2    |     |     |
i,j=1 i=1
∑R
1 w
|     | Brennan–Prediger |     | BPw | Pe = | ij  |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
R 2
i,j=1
classifier matches with the data in classifying the labels. There- patternaslinearweightsbutwithhighervaluesofweights.They
α get closer to quadratic weights toward the end of scale [18]. In
| fore, is expected | to be highly | sensitive | to misclassifications. |     |     |     |     |     |     |     |     |
| ----------------- | ------------ | --------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
κ-measure
Brennan–Prediger’sBPassumesthatthemarginaldistributionsof terms of the relationship between Cohen’s with no
the confusion matrix are uniform. Thus, BP is expected to work weight, linear, and quadratic weights, Warrens [26] shows that
|     |     |     |     |     |     | κ   | <   |     |     | κ   | <   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
well with balanced data compositions. Since Gwet’s AC2 adjusts ‘‘Cohen’s unweighted Cohen’s linear weighted Cohen’s
κ’’.
uniformityregardingthevariationineachclass,itcanhandlethe quadratic weighted The selection of weights is discussed in
unbalanceddatacompositionstoproducepreciseresults[29]. thelatersections.
The weighting schemes (w ) considered in this article are To implement the agreement coefficients as evaluation met-
ij
computed as given in Eqs. (11)–(15), where w = 1 when i = j rics, any agreement coefficient in Table 2 is calculated with one
ij
fori,j=1,2,...,R[18]. of the weighting schemes described in Eqs. (11)–(15) using the
|     |     |     |     | counts in | the | confusion | table | given | in Table | 1. Since | this cal- |
| --- | --- | --- | --- | --------- | --- | --------- | ----- | ----- | -------- | -------- | --------- |
• Unweighted:w =1. culation is straightforward and does not require any iterative
ij
• Linearweights: algorithms,thereisnodifferencebetweenthecomputationalcost
oftheagreementandthemainstreamevaluationmetrics.
|i−j|
| w =1− | .   |     |      |     |     |     |     |     |     |     |     |
| ----- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| ij    |     |     | (11) |     |     |     |     |     |     |     |     |
R−1
4. Numericalexperimentswithsyntheticconfusionmatrices
• Quadraticweights:
4.1. Experimentspaceanddatageneration
(i−j)2
| w =1− | .      |     |      |                                                       |     |     |     |     |     |     |     |
| ----- | ------ | --- | ---- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| ij    |        |     | (12) |                                                       |     |     |     |     |     |     |     |
|       | (R−1)2 |     |      | Inthisnumericalstudy,wecreatesyntheticconfusionmatri- |     |     |     |     |     |     |     |
cestoexaminethebehavioroftheevaluationmetricsmentioned
• Ordinalweights:
inSection3againstdifferentformationsoftheconfusionmatrix
|     |     |     |     | for a classification |     | task | into three | ordinal | classes. | We  | generate |
| --- | --- | --- | --- | -------------------- | --- | ---- | ---------- | ------- | -------- | --- | -------- |
M ij
w =1− , M =max(i,j)−min(i,j)+1 and confusionmatriceswithdifferentcharacteristicsforagiventrue
| ij  | M ij |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
max classificationperformance,calculateevaluationmetrics,andcom-
=max(M ).
M max ij pareevaluationmetricswiththetrueclassificationperformance.
|     |     |     |     | The generation |     | of confusion | matrices, |     | independent | of  | a specific |
| --- | --- | --- | --- | -------------- | --- | ------------ | --------- | --- | ----------- | --- | ---------- |
(13)
|     |     |     |     | model and | classifier, | allows | us  | to examine | a wide | range | of con- |
| --- | --- | --- | --- | --------- | ----------- | ------ | --- | ---------- | ------ | ----- | ------- |
• Radicalweights:
|     |     |     |     | fusion matrix |     | formations | that | can be | observed | in real | practice; |
| --- | --- | --- | --- | ------------- | --- | ---------- | ---- | ------ | -------- | ------- | --------- |
√
|       | |i−j| |     |     | hence,itprovidessufficientgeneralizability. |     |     |     |     |     |     |     |
| ----- | ----- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| w =1− | √ .   |     |     |                                             |     |     |     |     |     |     |     |
ij (14) The generated scenarios include high (0.8), moderate (0.5),
|R−1|
|     |     |     |     | and low | (0.2) | levels of | true accuracy |     | for a classifier | which | also |
| --- | --- | --- | --- | ------- | ----- | --------- | ------------- | --- | ---------------- | ----- | ---- |
• Bipolarweights: translate into high, moderate, and low performance in practice.
Here,thetrueaccuracy/performance(TA)isdefinedastheratioof
(i−j)2
w , correctlyclassifiedlabelstothenumberoflabelsineachclassin
| =1− |     |     | (15) |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
ij M(i+j−2)(2R−i−j) thedata(eithertestortrainingset).Therefore,themetriccalled
|     |     | (   | )   | accuracyisexpectedtogivesimilarvaluestoTAsubjecttosome |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
i− 2
whereM isthemaximumvalueof ( j) overthe randomvariationfromreplicatingtheexperiments.Inthissense,
|     |     | (i+j− | 2 )(2 R −i−j) |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
pairsof(i,j). accuracy will be used as a control metric to assess if the data
|                 |                    |                 |                    | generation   | approach | is         | sufficient | to  | generate        | the desired | levels   |
| --------------- | ------------------ | --------------- | ------------------ | ------------ | -------- | ---------- | ---------- | --- | --------------- | ----------- | -------- |
| Linear weights  | are proportional   | to the          | degree of misclas- |              |          |            |            |     |                 |             |          |
|                 |                    |                 |                    | of accuracy, | and      | the metric | accuracy   |     | is not compared |             | to other |
| sification made | by the classifier. | If a classifier | assigns a label    |              |          |            |            |     |                 |             |          |
metrics.
farther away from its true class, the penalty applied by linear Since one of the main factors impacting the metrics is the
weightsincreases.Thedegreeofpenaltyduetomisclassification balancednessofthedistributionoflabelsintothetargetclasses,
increases quadratically with the quadratic weights, while the balanced, imbalanced, and extremely imbalanced structures are
radicalweightspenalizemisclassificationatadegreebetweenthe created in combination with the true accuracy. This factor is
linear and quadratic weights. Since the ordinal weights account calledthestructureofthetable(ST)intherestofthemanuscript.
fortheranksofassignmentsdonebytheclassifier,onlytheranks Basedontheclassifier’sperformanceandtheareaofinterest,the
are reflected in the weights. Bipolar weights produce a similar accuracyofclassificationmaydifferacrosstheordinalclasses.To
5

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
accountforthis,thefollowingcasesarecreatedbyusingdifferent get worse in accurately capturing true accuracy. For high and
p settings: moderate true accuracy, Cohen’s κ and Scott’s π with ordinal
ij
weightsmeasuretheclassificationperformanceaccuratelyforall
1. Labelsbelongingtoall3classesareclassifiedwithanaccu- cases. When the true accuracy is low, unweighted or quadratic
racyclosetothetrueaccuracy. weightedAC2performsbetterthanothermeasuresforallcases.
2. Labels belonging to 2 out of 3 classes are classified with We observe that mainstream metrics have a slightly better or
anaccuracyclosetothetrueaccuracy,andthelastoneis similar performance for balanced situations with high true ac-
classifiedwithlowaccuracy. curacythanordinalweightedCohen’sκ andScott’sπ measures.
3. Labelsbelongingtoonlyoneof3classesareclassifiedwith However, if the true accuracy is at lower levels and the classi-
an accuracy close to the true accuracy, and the remaining fication accuracy is not distributed evenly as in Cases 2 and 3,
onesareclassifiedwithlowaccuracy. ordinalweightedCohen’sκ andScott’sπ andquadraticweighted
AC2performbetterforbalanceddatacompositions.Followingthe
Thisfactorisnamed‘‘Case’’inthenumericalstudyanddenoted
theoreticalresultsofDelgadoandTibau[12],Cohen’sunweighted
asCase1,2,and3throughoutthemanuscript.Case1isthebest κproducessimilarvaluestoMCCinallthescenariosforbalanced
scenariowheretheclassifierperformsequallywellforallclasses. data composition. There are small deviations between Cohen’s
Thus,weexpectametricvalueclosetothegiventrueaccuracy. unweightedκ andMCCforCases2and3.Asexpected,MAEand
In Cases 2 and 3, the classifier fails to work sufficiently for at RMSEvaluesgetslightlysmallerasthesamplesizeincreasesfor
leastoneofthethreeclasses.So,evenforhightrueaccuracy,the allmetrics.
classifier’sperformanceispoorforCase2andpoorerforCase3. The results for imbalanced data compositions are generally
Sincetheclassifierdoesnotperformwell,weexpectlowervalues similar to those observed for balanced datasets. MCC and IA
thanthegiventrueaccuracyinCases2and3. produce high error values for high and moderate levels of TA.
The confusion matrices are generated using the product- Mainstream metrics perform well when the classifier’s perfor-
multinomial sampling scheme for the sample sizes of 50, 100, mance is homogeneous across the ordinal levels and the true
200, and 500 for each combination of ST, TA, and Case. Each accuracyishighormoderate.ThemeanF1isthebest-performing
scenario is replicated 1000 times. The p ij values are created to mainstream classifier. Cohen’s κ and Scott’s π with quadratic
reflect the ordinal classes, and the combinations of ST, TA, and weights have very similar MAE and RMSE values to mainstream
CaseareusedasinputsoftherTable.RxC()functionofrTableICC metrics except for MCC and IA for these scenarios. However,
package of R software [27]. We arbitrarily distort the given true whentheTAisreduced,andtheclassifier’sperformanceisbetter
accuracy in Cases 2 and 3 to create situations that can occur forsomeclassesandworsefortheotherclasses(Cases2and3),
in real practice. The resulting synthetic confusion matrices are quadraticorordinalweightedCohen’sκ andScott’sπ producea
showninTableA.1ofAppendixA.Togenerateordinalclasses,we promising performance that is better than mainstream metrics
followtheapproachexplainedbyTranetal.[17,seep.996–997]. for most of the scenarios. For low TA under imbalanced data
We use mean absolute error (MAE) and root mean squared composition, AC2, BP, and Krippendorff’s α perform better than
error(RMSE)giveninEq.(16)tocomparethemetricsundereach the mainstream and other agreement metrics when only one of
simulationscenario. theclassesiscapturedwithanaccuracycloseto0.2.Weobserve

r  r slight decreases in MAE and RMSE for increasing sample sizes
MAE = 1∑ |X−X ˆ| and RMSE =  √ 1∑ (X−X ˆ )2, (16) withimbalanceddatacomposition.
i i
r r Whenthedatacompositionisextremelyimbalanced,MAEand
i=1 i=1
RMSE values of the mainstream metrics considerably increase if
where r is the number of replications, X is the true value of ac- theclassifierdoesnotperformequallywellinallclasses.Forhet-
ˆ
curacy,andX i istheperformanceorweightedagreementmetric erogeneous classifier performance across the classes, quadratic
estimationintheithreplication. weighted Cohen’s κ and Scott’s π generate better performance
estimatesthanmainstreammetricsforallsamplesizes.Forlower
4.2. Results TA,theunweightedAC2isthebestmetricamongtheagreement
metrics for all cases. It performs better than the mainstream
The mainstream metrics’ RMSE and MAE values for all sam- metricsforsamplesizesgreaterthan50.
ple sizes, balanced, imbalanced, and extremely imbalanced data
compositionsaregiveninTableA.2,A.4,...,A.12ofAppendixA. 4.3. Conclusions
ThosefortheweightedagreementmetricsaregiveninTableA.3,
A.5,...,A.13ofAppendixA.Inthissection,‘‘mainstreammetrics’’ Among the mainstream metrics, MCC and IA produce no-
refer to the metrics described in Section 3.1 except accuracy. tably larger MAE and RMSE values than most of the metrics in
Since we use the definition of accuracy to generate confusion most scenarios. The mainstream metrics, except for MCC and
matrices, we exclude it from the inferences in this section. For IA, successfully identify the performance of classifiers when the
a full picture of comparisons between the mainstream and the data composition is balanced, and all three ordinal classes are
weighted agreement metrics, the reader should refer to pairs of capturedequallysuccessfully.Forthescenariosthatdeviatefrom
Table A.2 and A.3, A.4 and A.5, and so on. The inferences in this theseidealconditions,errormarginsincreaseforthemainstream
sectionarealsomadebyconsideringthesepairsoftables. metrics.
TheresultsinAppendixAshowthataccuracyisverycloseto For the agreement measures, we observe the theoretical re-
TA, as expected in all the scenarios considered. When the data lationshipbetweenMCCandCohen’sκ demonstratedby[12,26]
compositionisbalanced,mainstreammetricsexceptforMCCand in practice through the synthetic datasets when all the classes
IAandmostagreementmetricsproduceaccuratemeasurements are assigned with similar success by the classifier and the data
ofclassifierperformanceforCase1foralllevelsofTAandsample composition is balanced. However, this theoretical relationship
sizes. MCC and IA produce large MAEs and RMSEs, in general. is not observed under the deviations from this well-balanced
Astheclassifier’sperformancebecomesheterogeneousacrossthe scenario.
classes(movingfromCase1to2and3)andTAreducestolower For the rest of the weighted agreement measures, a wide
levels (the classification task gets harder), mainstream metrics range of different values are observed, implying that agreement
6

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
measures are sensitive to different data compositions and true We aim to create 10 folds of data from each dataset if it has
accuracy levels and have the potential to be used as reliable, more than 100 labels. Since the confusion matrix becomes very
useful metrics for multi-class classifiers. Specifically, Cohen’s κ sparse for the datasets with less than 100 labels, we create 2
and Scott’s π with quadratic weights show the best MAE and foldsforlsci2,lsci4,lsci13,eng1,other2,andother7datasets.We
RMSE performance for high and moderate true agreement, data run the computations separately for the full dataset, balanced,
| composition | scenarios,      |     | and classification |         | cases.   | Since   | Scott’s π |              |           |       |                |      |           |        |          |
| ----------- | --------------- | --- | ------------------ | ------- | -------- | ------- | --------- | ------------ | --------- | ----- | -------------- | ---- | --------- | ------ | -------- |
|             |                 |     |                    |         |          |         |           | imbalanced,  | extremely |       | imbalanced,    | life | sciences, | social | science, |
| assumes     | the homogeneity |     | of                 | margins | [28], it | returns | low error |              |           |       |                |      |           |        |          |
|             |                 |     |                    |         |          |         |           | engineering, | and       | other | areas datasets |      | for each  | fold.  | Since we |
valueswhenthemarginsoftheconfusionmatrixgetcloser(the
|     |     |     |     |     |     |     |     | cannot | create | 10 folds | for every | dataset, | we  | have | a different |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ | -------- | --------- | -------- | --- | ---- | ----------- |
true agreement is moderate or high under all cases). However, number of replications for each run composed of datasets and
whenthetrueagreementislow,wedeviatefromthiscase;hence, their folds, as given in Table 3. For example, for the run with
otheragreementmeasuresperformbetter.Whenthetrueagree- ‘‘All datasets’’, we have 10 folds for 34 datasets and 2 folds for
ment is low, and data composition is imbalanced or extremely 6 datasets; in total, we run 352 replications for all datasets. For
imbalanced,weobservethatAC2giveslowMAEandRMSEvalues therunwith‘‘OnlyENG’’datasets,thereare10foldsfor3outof4
with different weights. The reason for Gwet’s AC2 to perform datasetsand2foldsfor1dataset,resultingin32replications.We
betteristhatAC2adjustsuniformityduetothevariationcreated utilizetherunsforthefoldsasreplicationstoconductstatistical
bythelowtrueagreementandimbalanceinthedata[29]. hypothesistests.
| All the | considered | mainstream |     | and | agreement |     | metrics are |        |                 |     |           |     |          |             |        |
| ------- | ---------- | ---------- | --- | --- | --------- | --- | ----------- | ------ | --------------- | --- | --------- | --- | -------- | ----------- | ------ |
|         |            |            |     |     |           |     |             | In the | implementation, |     | we employ |     | pairs of | classifiers | devel- |
sensitivetothesamplesize.WegetsmallerMAEandRMSEvalues
opedforordinaldata.Theclassifiersareselectedbyconsidering
| as the sample | increases. |     | The | benefit | of increasing |     | sample size |     |     |     |     |     |     |     |     |
| ------------- | ---------- | --- | --- | ------- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
thattheyhavesimilaroverallclassificationperformances.Weas-
| on MAE | and RMSE | becomes | notable |     | when the | true | accuracy is |     |     |     |     |     |     |     |     |
| ------ | -------- | ------- | ------- | --- | -------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
sessifthemetricsareabletodifferentiatebetweentheclassifiers.
| high or   | moderate  | with | balanced | data | composition.   |     | When the  |                |     |         |            |              |     |                |     |
| --------- | --------- | ---- | -------- | ---- | -------------- | --- | --------- | -------------- | --- | ------- | ---------- | ------------ | --- | -------------- | --- |
|           |           |      |          |      |                |     |           | The difference |     | between | the actual | performances |     | of classifiers | is  |
| imbalance | increases | and  | one or   | two  | of the classes | are | correctly |                |     |         |            |              |     |                |     |
animportantconsiderationinassessingtheprecision/usefulness
classified(Case2and3),increasingthesamplesizedoesnothelp
|     |     |     |     |     |     |     |     | of the metrics. |     | Conceivably, | in  | real practice, |     | the precision | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | -------------- | --- | ------------- | --- |
reducethevaluesofMAEandRMSEbyaconsiderablemargin. metrics is not a very important issue if one of the classifiers is
Overall,whenthedatacompositionisimbalancedforthesyn- performingfarbetterthantheother.Thesuccessofametriclies
thetic confusion matrices, the agreement measures mostly with initsabilitytodistinguishtheclassifierswhentheirperformances
ordinal weights produce lower error measures than the main- are close to each other. Therefore, to create two classifiers with
| stream metrics |     | and IA | for most | cases. | They | are more | sensitive |     |     |     |     |     |     |     |     |
| -------------- | --- | ------ | -------- | ------ | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
similarperformance,weusetwoclassifiersfromthesameclassi-
thanMCCagainstunsuccessfulclassificationinatleastoneofthe
|          |          |             |     |       |                    |     |           | fication    | method  | with slight | changes         | in  | their | parameter | settings.  |
| -------- | -------- | ----------- | --- | ----- | ------------------ | --- | --------- | ----------- | ------- | ----------- | --------------- | --- | ----- | --------- | ---------- |
| classes. | However, | we need     | to  | study | the response       | of  | agreement |             |         |             |                 |     |       |           |            |
|          |          |             |     |       |                    |     |           | We consider | support |             | vector machines |     | with  | ordered   | partitions |
| metrics  | to the   | composition | of  | data  | in a generalizable |     | setting   |             |         |             |                 |     |       |           |            |
(SVMOP),whichisdevelopedforclassificationintoordinalclasses
| to identify | which | agreement |                 | measure | and        | weighting | scheme     |                      |     |              |          |           |     |               |         |
| ----------- | ----- | --------- | --------------- | ------- | ---------- | --------- | ---------- | -------------------- | --- | ------------ | -------- | --------- | --- | ------------- | ------- |
|             |       |           |                 |         |            |           |            | by Waegeman          |     | et al. [30], | weighted | K-nearest |     | neighbors     | for or- |
| combination | can   | be used   | for performance |         | assessment |           | of ordinal |                      |     |              |          |           |     |               |         |
|             |       |           |                 |         |            |           |            | dinal classification |     | (WKNNOR)     |          | proposed  | by  | Hechenbichler | and     |
multi-classclassifiersandhowtheirusageiscomparedtothatof
Schliep[31],andkerneldiscriminantlearningforordinalregres-
themainstreammetrics,MCCandtherecentlyintroducedmetric
|              |          |     |         |     |           |           |       | sion (KDLOR) |            | proposed     | by Sun   | et al. | [32]. There | can    | be other |
| ------------ | -------- | --- | ------- | --- | --------- | --------- | ----- | ------------ | ---------- | ------------ | -------- | ------ | ----------- | ------ | -------- |
| IA. For this | purpose, | we  | conduct | an  | extensive | numerical | study |              |            |              |          |        |             |        |          |
|              |          |     |         |     |           |           |       | choices      | of ordinal | classifiers. | However, |        | since       | we are | not com- |
withrealdatasetsinthenextsection.
|     |     |     |     |     |     |     |     | paring the | performance |     | of actual | classifiers/classification |     |     | meth- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --------- | -------------------------- | --- | --- | ----- |
5. Numericalexperimentswithrealdata ods and need to get just confusion matrices out of classifiers,
|     |     |     |     |     |     |     |     | the choice | of SVMOP, |     | WKNNOR, | and KDLOR |     | classifiers | does not |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ------- | --------- | --- | ----------- | -------- |
poseanyproblemwiththegeneralizabilityoftheresultsonthe
5.1. Datasetsandclassifiers
performanceofthemetrics.
Theparametersγ
|         |            |       |          |                   |           |             |         |              |       | andcost | impacttheperformanceofSVMOP |        |       |        |           |
| ------- | ---------- | ----- | -------- | ----------------- | --------- | ----------- | ------- | ------------ | ----- | ------- | --------------------------- | ------ | ----- | ------ | --------- |
| In the  | numerical  | study | with     | real              | data, the | sensitivity | of 37   |              |       |         |                             |        |       |        |           |
|         |            |       |          |                   |           |             |         | classifiers, | which | use     | the Gaussian                | radial | basis | kernel | function. |
| metrics | of Section | 3 is  | assessed | in distinguishing |           | ordinal     | classi- |              |       |         |                             |        |       |        |           |
Theγ parameteradjuststhescaleoftheGaussiankernel.Alarge
fiers.Sincethereisnouniquemetrictobeusedasthegoldstan-
|     |     |     |     |     |     |     |     | scale γ | for a | given cost | creates | wide | classification |     | boundaries. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ---------- | ------- | ---- | -------------- | --- | ----------- |
dardfordeterminingthesuperiorityofonemetricoveranother,
Forsmallerscales,under-fittingoccursifclassificationboundaries
| we focus | on the | sensitivity | of  | metrics | to the | slight | difference |     |     |     |     |     |     |     |     |
| -------- | ------ | ----------- | --- | ------- | ------ | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
becomemorefocusedunderlimitedregionsofthespace[33,see
betweentheperformanceoftwoclassifiers.Itisadesiredquality
p.347–348].Anincreasedunder-fittingreducestheclassification
forametrictodistinguishsubtledifferencesintheclassification
performance. performance with the test set. We set the cost value for both
γ
Weuse40realdatasetshavingdependentfeatureswithmul- SVMOPs to 1 and use the parameter to create classifiers that
tiple ordinal classes. For the generalizability of the results, we have similar overall performance but make mistakes on ordinal
γ =
gather datasets from the main areas of practice: social sciences classes. We set the SVMOP classifiers to use with 1 and 10
(16), life sciences (13), engineering (4) and other areas (7). withcost =1forSVMOP andSVMOP ,respectively.
|     |     |     |     |     |     |     |     |     |     |     | 1   | 2   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Datasets and their web links are given in Table B.1 of Appendix For WKNNOR classifiers, we use the Euclidean distance and
B.SummaryinformationaboutthedatasetsisgiveninTableB.2 Gaussiankernelforbothclassifiersandsetthenumberofneigh-
|             |     |            |      |         |         |     |             | bors differently |     | to create | two          | classifiers | with | slightly     | different |
| ----------- | --- | ---------- | ---- | ------- | ------- | --- | ----------- | ---------------- | --- | --------- | ------------ | ----------- | ---- | ------------ | --------- |
| of Appendix | B.  | The sample | size | of each | dataset | is  | given under |                  |     |           |              |             |      |              |           |
|             |     |            |      |         |         |     |             | performances.    |     | A KNN     | with a small | number      |      | of neighbors | tends     |
the‘‘#Labels’’columnofTableB.2.Forthedatasetshavingmore
toover-fit,butalargevalueofthenumberofneighborshasthe
| than 5000 | labels, | a sub-sample |     | of size | 1000 | is taken | randomly. |     |     |     |     |     |     |     |     |
| --------- | ------- | ------------ | --- | ------- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
potentialtocreateunder-fit[33,seep.160and352].Wesetthe
| Data composition |     | for each | dataset | is  | qualified | based | on the bal- |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | ------- | --- | --------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ancednessofmarginalprobabilities.Overall,wehave6balanced, number of neighbors to 20 for WKNNOR 1 and 5 for WKNNOR 2
8 imbalanced, and 26 extremely imbalanced datasets. We have to create a small discrepancy between the performances of the
sufficient coverage of the number of features ranging from 3 classifiersthatweexpecttheevaluationmetricstodistinguish.
to 56 and the number of ordinal classes from 3 to 11 among For KDLOR classifiers, we use the Gaussian kernel with dif-
the datasets. There are very small samples as well as very large ferent scales to create KDLOR and KDLOR classifiers. We set
|     |     |     |     |     |     |     |     |     |     |     | 1   |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
samples from a wide range of areas of practice included in this the scale of the Gaussian kernel to 1 and 5 for KDLOR and
1
numericalstudy. KDLOR , respectively. Since KDLOR is a kernel-based method,
2
7

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Table3
Runs,datasets,andthecorrespondingnumberofreplications.
Runswith Numberofdatasets Datasetnumber Replications
Alldatasets 40 1to40 352
Onlybalanced 6 3,9,12,17,20,39 52
Onlyimbalanced 8 2,4,5,6,11,14,38,40 72
Onlyextremely 26 1,7,8,10,13,15,16, 228
Imbalanced 18,19,21to37
OnlySSCI 16 14to29 160
OnlyENG 4 30to33 32
OnlyLSCI 13 1to13 106
OnlyOTHER 7 34to40 138
Fig.1. Flowdiagramofthenumericalstudywithrealdata.Here,nshowsthenumberofdatasetsineachparticularrunasgiveninthesecondcolumnofTable3,
k=2,10,andthevaluesofmareshowninthelastcolumnofTable3foreachrun.
its performance is characterized by the kernel. The scale of the 5.2.1. Visualinspection
Gaussian kernel specifies the boundaries of the regions created The means of metrics, calculated by aggregating over 40
forclassification,similartoSVMOPs. datasets and folds, are given in Figs. 2, 3, and 4 for SVMOP,
Itshouldbenotedthatthesesettingsdonotensurethateither WKNNOR,andKDLORclassifiers,respectively,alongwithandthe
Classifier orClassifier undereachordinalclassificationmethod ± standard error limits. Note that the statistical significance of
1 2
will have superior performance. The superiority issue is outside differences is thoroughly discussed in the parts following these
thefocusofthisnumericalstudysinceweonlyneedtohaveone figures. In Figs. 2, 3, and 4, we see different behaviors for each
oftheclassifiersperformslightlydifferently.
groupofmetrics,namely,mainstream,Cohen’sκ,Scott’sπ,AC2,
BPandKrippendorff’sαforalltheordinalclassificationmethods.
We employ svmofit(), wknnor(), and kdlortrain() functions
There is no clear distinction between the values of metrics with
from OCAPIS R package [34] for the implementation of SVMOP,
differentweights.Forallthemainclassificationmethods,SVMOP,
WKNNOR, and KDLOR classifiers, respectively. The flow diagram
ofimplementationisgiveninFig.1.Wecreatek-folds,k=2,10 WKNNOR,andKDLOR,almostallmetricsshowthatClassifier 1 has
slightlybetterperformancethanClassifier .
of each dataset and implement k-fold cross-validation without For SVMOP classifiers (Fig. 2), weighte 2 d π metrics have no-
aggregatingtheresultscomingoutofthefolds. tably different behavior than all the other metrics. Weighted κ
and α metrics show similar results, while weighted AC2 and BP
5.2. Results metrics indicate a similar level of performance to each other.
However, AC2 and BP metrics do not distinguish SVMOP and
1
SVMOP ,whichisnotthedesiredresult.Inthissense,weighted
Results are composed of the values of 37 metrics observed 2
π metrics show the highest difference between the classifiers.
over 2 sub-classifiers under each of 3 main classification meth-
Among the mainstream metrics, macro recall, macro precision,
ods, 40 real datasets, and replications from k-folds. The real
and macro F1 are close to each other, while IA and accuracy
datasetsarealsodividedintocategoriesbasedontheirbalanced-
showasimilarperformance.MCCistheonlymainstreammetric
ness and the field of application. We follow Demšar [35] to
that shows a slight difference between the classifiers. Overall,
provide statistical evidence on the significance of the difference weighted π metrics are able to distinguish the classifiers as
betweenmetricsacrossthefactorsusedforcomparisons.Weuse
desired, while none of the mainstream metrics is capable of for
multi-way analysis of variance (ANOVA) and Tukey’s pairwise
theSVMOPmethod.
comparisontesttoidentifythemetricsthatproducesignificantly
ForWKNNORclassifiers(Fig.3),weightedAC2andBPindicate
different values between classifiers under each main classifica-
considerably higher performance for both classifiers than the
tion method. In this way, we identify the sensitive metrics to othermetrics.Thefirstclassifierisfoundtobeslightlybetterby
separate the classification performance of two similar classifiers all the agreement measures. Since the mean metric values have
from each other. The normality and homogeneity of variances the lowest standard errors for the WKNNOR classifiers, distin-
assumptions of ANOVA [35] need to be ensured to get valid guishingbetweentwoclassifiersbecomesevenmorechallenging.
inferences from ANOVA. For this aim, the Kolmogorov–Smirnov The mainstream metrics, except accuracy and IA, are insensitive
normalitytestandLenevetestforthehomogeneityofvariances to the difference between WKNNOR and WKNNOR . BP is the
1 2
are implemented using notest [36] and car [37] R packages, most sensitive metric to the difference between two WKNNOR
respectively. classifiers. Weights have no impact on the α metric and little
8

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Fig.2. MeanofmetricsfortheSVMOPclassifiers.Themeaniscalculatedover40datasetsandfolds.Barsshowthelimitsofmean±standarderror.
Fig.3. MeanofmetricsfortheWKNNORclassifiers.Themeaniscalculatedover40datasetsandfolds.Barsshowthelimitsofmean±standarderror.
impact on κ and BP metrics. Overall, while most mainstream classifiers, all agreement measures show some degree of differ-
metricsareinsensitivetotheslightdifferencebetweenWKNNOR encebetweentheperformancesofWKNNOR andWKNNOR .BP
1 2
9

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
MeanofmetricsfortheKDLORclassifiers.Themeaniscalculatedover40datasetsandfolds.Barsshowthelimitsofmean±standarderror.
Fig.4.
showsthebestsensitivitywhenthemetricvaluesareveryclose classification method and the application field for each ordinal
toeachother(verysmallstandarderrors). classification method. However, Figs. 5 and 6 demonstrate that
For KDLOR classifiers (Fig. 4), we observe higher standard we need to consider each data composition for each ordinal
errorsamongthevaluesofmetricsthatincreasethesensitivityof classificationmethod.
| themetricstotheslightdifferencebetweenKDLOR |     |     |     |     |     | andKDLOR |     |     |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                             |     |     |     |     |     | 1        | 2   |     |     |     |     |     |     |     |     |
classifiers.Allthemetricsaresensitivetothedifferencebetween
|                  |     |          |        |          |     |             |     | 5.2.2. | Statisticaltests |         |          |              |              |     |          |
| ---------------- | --- | -------- | ------ | -------- | --- | ----------- | --- | ------ | ---------------- | ------- | -------- | ------------ | ------------ | --- | -------- |
| the classifiers. | The | α metric | is not | impacted | by  | the weights | for |        |                  |         |          |              |              |     |          |
|                  |     |          |        |          |     |             |     | In     | order            | to give | detailed | significance | test results | for | the dif- |
KDLORclassifierstoo.Theπ
metricsshowthehighestsensitivity, ference between two sub-classifiers, we first apply ANOVA with
and the weights do not influence the degree of their sensitivity. metricsandsub-classifiers,ensurethenormalityandhomogene-
AlthoughMCChasthehighestsensitivityamongthemainstream
|     |     |     |     |     |     |     |     | ity of | variances | assumptions |     | of ANOVA, | and then | apply | Tukey’s |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | ----------- | --- | --------- | -------- | ----- | ------- |
metrics,itisconsiderablylowerthanthedifferenceindicatedby
theπ metric.Overall,MCC,κ,andπ pairwise comparison tests to identify the metrics for which the
metricsshowsimilarlevels
π sub-classifiers are giving different results. The results of these
| of performance, | while | distinguishes |     | KDLOR |     | and KDLOR | as  |     |     |     |     |     |     |     |     |
| --------------- | ----- | ------------- | --- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1 2 tests are given in Table B.3 of Appendix B. Suppose we refer to
desired.
Tukey’spairwisecomparisontestresultforthemetricMCC.The
| When | the standard | errors | of metric | values |     | are high, | the π |      |           |         |       |                  |            |     |         |
| ---- | ------------ | ------ | --------- | ------ | --- | --------- | ----- | ---- | --------- | ------- | ----- | ---------------- | ---------- | --- | ------- |
|      |              |        |           |        |     |           |       | test | indicates | whether | there | is a significant | difference |     | between |
metricisabletodistinguishclassifierswithsimilarperformance
|                                                   |     |     |     |     |     |     |     | MCC | values | computed | for Classifier |     | and Classifier | . If | there is |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------------- | --- | -------------- | ---- | -------- |
| asseenforSVMOPandKDLORmethods.However,whenthemet- |     |     |     |     |     |     |     |     |        |          |                |     | 1              | 2    |          |
ric values are less variable, BP indicates the difference between a significant difference, we can conclude that MCC is able to
WKNNORclassifiersbetterthanπ.Regardingthelevelofdiffer- distinguish the performance difference between Classifier 1 and
|               |        |          |     |           |        |      |     | Classifier | as  | desired. | In this | way, we | gather statistical |     | evidence |
| ------------- | ------ | -------- | --- | --------- | ------ | ---- | --- | ---------- | --- | -------- | ------- | ------- | ------------------ | --- | -------- |
| ence captured | by the | metrics, | the | weighting | scheme | does | not |            | 2   |          |         |         |                    |     |          |
π to identify the metrics that perform as desired in distinguishing
| have a notable | influence | on  | both | and BP | metrics. | However, | it  |     |     |     |     |     |     |     |     |
| -------------- | --------- | --- | ---- | ------ | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
twoclassifierswithsimilarperformance.Ifapairwisecomparison
impactstheclassificationperformanceindicatedbythesemetrics.
|               |          |             |               |           |         |             |          | of two | metrics      | is  | insignificant, | we  | conclude that | both   | metrics  |
| ------------- | -------- | ----------- | ------------- | --------- | ------- | ----------- | -------- | ------ | ------------ | --- | -------------- | --- | ------------- | ------ | -------- |
| Since the     | data     | composition | and           | the field | of      | application | are      |        |              |     |                |     |               |        |          |
|               |          |             |               |           |         |             |          | are    | unsuccessful | in  | distinguishing |     | classifiers;  | hence, | they are |
| two important | features | of          | the datasets, |           | we need | to          | consider |        |              |     |                |     |               |        |          |
these factors for the inferences. Figs. 5 and 6 show the mean insensitivetothedifferencebetweenthem.
metric values and their standard error limits aggregated over For SVMOP classifiers, the p-values of Tukey’s pairwise com-
all the classifiers and the ordinal classification methods. From parisontestsaregiveninFig.7inthebreakdownofdatacompo-
these plots, we observe that both the data composition and the sitions.Forbalanceddatasets,pairwisecomparisonsofallmain-
application field considerably impact the mean metric values stream metrics except MCC and IA are insignificant, implying
|     |     |     |     |     |     |     |     | that | they are | insensitive | to  | the difference | between | SVMOP | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ----------- | --- | -------------- | ------- | ----- | --- |
generated for the classifiers since the metrics react differently 1
|                                                        |     |     |     |     |     |     |     | SVMOP | classifiers. |     | All weighted | κ   | and π metrics | and | some |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | ------------ | --- | ------------- | --- | ---- |
| toeachofbalanced,imbalanced,andextremelyimbalanceddata |     |     |     |     |     |     |     |       | 2            |     |              |     |               |     |      |
compositions and datasets from different fields. Note that since weighted AC2 metrics are significantly different from the main-
α
the aggregation is done over very different ordinal classification stream metrics, while BP and some metrics are not. All the
π
methods for Figs. 5 and 6, it is not appropriate to interpret weighted metrics are significantly different from the other
the differences between the data compositions and application mainstream and agreement metrics. When the composition of
fieldswithoutlookingintothedatacompositionforeachordinal data becomes imbalanced, mean F1, MCC, and IA metrics give
10

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
Fig.5. Meanofmetricsaccordingtothedatacomposition.Themeaniscalculatedoverallclassifiersandfolds.Barsshowthelimitsofmean±standarderror.
Fig. 6. Mean of metrics according to the application fields of the datasets. The mean is calculated over all classifiers and folds. Bars show the limits of mean ±
standarderror.
significantlydifferentvaluesbetweenSVMOP andSVMOP clas- inferences given for imbalanced data composition, we see mean
1 2
sifiers among the mainstream metrics. κ and α metrics are not F1 becomes significantly different from other mainstream and
significantlydifferentfromMCC,whileallotheragreementmet- agreementmetrics.
ricsaresignificantlydifferentfromMCCandallothermainstream Thep-valuesofTukey’spairwisecomparisontestsformetrics
metrics. For extremely imbalanced datasets, in addition to the are given in Fig. 8 in the breakdown of the field of application
11

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- |
Fig. 7. The p-values of Tukey’s pairwise comparison tests for SVMOP classifiers in the breakdown of data composition. The axes of the plots show the metrics
| calculatedforSVMOP1 |     | andSVMOP2 | classifiers. |     |     |     |     |     |     |     |     |
| ------------------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
for SVMOP classifiers. We get different patterns of the pairwise accuracyisalsosensitivetothedifferencebetweenSVMOP and
1
| comparisons’ | p-values | across | the application |     | fields; | hence, the |     |     |     |     |     |
| ------------ | -------- | ------ | --------------- | --- | ------- | ---------- | --- | --- | --- | --- | --- |
SVMOP 2 classifiers.Forengineeringdatasets,themetricaccuracy
application field makes a difference in the usefulness of the significantlydiffersfromallothermainstreammetrics,κ,π,and
α
metrics.Amongthemainstreammetrics,onlyMCCissignificantly metrics. There is no significant difference between accuracy
differentacrosstwoSVMOPclassifiersforsocialsciencesdatasets. and weighted AC2 and BP metrics. Consistently, weighted ver-
|     | κ, π, | α   |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Since all and metrics are significantly different from the sions of AC2 and BP metrics are significantly different from the
| mainstream | metrics, | their | behavior | against | two similar | SVMOP |     |     |     |     |     |
| ---------- | -------- | ----- | -------- | ------- | ----------- | ----- | --- | --- | --- | --- | --- |
mainstreammetricsexceptforaccuracy.
| classifiers  | differs. | Also, there | are significant |          | differences | between |                                                       |     |     |     |     |
| ------------ | -------- | ----------- | --------------- | -------- | ----------- | ------- | ----------------------------------------------------- | --- | --- | --- | --- |
|              | κ        | π           |                 |          | α           |         | ForWKNNORclassifiers,thep-valuesofTukey’spairwisecom- |     |     |     |     |
| all weighted | and      | metrics.    | All             | weighted | metrics     | are not |                                                       |     |     |     |     |
significantlydifferentfromκ parisontestsaregiveninFigureB.1ofAppendixBinthebreak-
butshowthedifferencefortherest
|     |     |     |     |     |     |     | down of data | compositions | and Figure | B.3 of Appendix | B in |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | ---------- | --------------- | ---- |
oftheagreementmeasures.SomeweightedAC2andBPmetrics
|           |           |         |            |      |         |             | the breakdown | of application | fields. We | get similar results | for |
| --------- | --------- | ------- | ---------- | ---- | ------- | ----------- | ------------- | -------------- | ---------- | ------------------- | --- |
| also show | a similar | result. | We observe | very | similar | results for |               |                |            |                     |     |
life sciences datasets. In addition to MCC, the only difference is balanced and imbalanced datasets. For both data compositions,
that mean F1 and IA metrics also show significant differences all the agreement metrics are significantly different from each
among the mainstream metrics. The results of datasets catego- other and mainstream metrics. Among the mainstream metrics,
rized in other application fields are similar to life sciences, but mean F1, MCC, and IA are sensitive to the differences between
12

| A.E.YilmazandH.Demirhan |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |
| ----------------------- | --- | --- | --- | --- | ----------------------------------- | --- | --- |
Fig.8. Thep-valuesofTukey’spairwisecomparisontestsforSVMOPclassifiersinthebreakdownofthefieldofapplication.Theaxesoftheplotsshowthemetrics
| calculatedforSVMOP1 andSVMOP2 | classifiers. |     |     |     |     |     |     |
| ----------------------------- | ------------ | --- | --- | --- | --- | --- | --- |
WKNNOR andWKNNOR classifiers.Onlyaccuracyshowsasig- aresensitivetothedifferencebetweenWKNNOR andWKNNOR
| 1                                                       | 2   |     |              |     |     | 1   | 2   |
| ------------------------------------------------------- | --- | --- | ------------ | --- | --- | --- | --- |
| nificantdifferenceamongthemainstreammetricsforextremely |     |     | classifiers. |     |     |     |     |
imbalanceddatasets.Someofκ,mostofπ,andallAC2,BP,and For KDLOR classifiers, the p-values of Tukey’s tests are given
α metricsaresensitivetothedifferencebetweentwoWKNNOR inFigureB.2andB.4ofAppendixBintermsofdatacompositions
classifiers.Scott’sπ metricsarenotsignificantlydifferentfromκ andapplicationfields,respectively.Forbalanceddatasets,MCCis
and α metrics. We observe different patterns of p-values across theonlysensitivemetrictothedifferencebetweenKDLOR and
1
the fields of application in Figure B.3 of Appendix B. For social KDLOR classifiers.Whileκ,π,andαmetricsarenotsignificantly
2
science datasets, κ metrics are not significantly different from different from MCC, AC2 and BP metrics are different. π and
|     |     | π   | α   |     |     |     | κ   |
| --- | --- | --- | --- | --- | --- | --- | --- |
the mainstream metrics except for accuracy. Scott’s and Krip- show significant differences from all other metrics except
pendorff’sαmetricsshowsensitivitytothediscrepancybetween
|     |     |     | for balanced | datasets. | For imbalanced datasets, | mean F1, | MCC, |
| --- | --- | --- | ------------ | --------- | ------------------------ | -------- | ---- |
the classifiers compared to mainstream metrics. AC2 and BP IA,andallagreementmetricsdiffersignificantlyfromthemain-
α
metricsaresignificantlydifferentfromthemainstreamandother stream metrics. The metric shows different behavior than the
agreementmetrics.Whenitcomestoengineeringdatasets,only other agreement metrics. When the data composition becomes
|     |     |     |     |     | κ, π, α |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |
accuracy, AC2, and BP metrics are significantly sensitive to the extremely imbalanced, MCC, and metrics are sensitive
α
difference between WKNNOR and WKNNOR classifiers, and to the difference between KDLOR classifiers, and the difference
|     | 1 2 | π   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
shows significant differences from these metrics. Scott’s and betweenthisgroupofmetricsandAC2andBPissignificant.For
κ
Cohen’s metrics are insensitive for engineering datasets. For the application fields, we observe different patterns of p-values
life sciences and other datasets, we see similar patterns of p- for social sciences, engineering, and life sciences datasets, while
values. All the metrics except macro recall and macro precision datasets from other application areas produce a similar pattern
13

A.E.YilmazandH.Demirhan AppliedSoftComputing134(2023)110020
as the life sciences datasets. MCC, π, and α metrics produce SVMOPandWKNNORclassifiersforengineeringdatasets.Forall
significantly different results for KDLOR and KDLOR classifiers theothercategoriesofdatasets,κ,π,andαmetricsaresensitive
1 2
forsocialsciencesdatasets.AC2andBPmetricsaresignificantly tothedifferencebetweenclassifiers.Fromthesetofmainstream
different from the rest of the agreement and mainstream met- metrics,onlyMCCisconsistentlysensitiveacrossdifferentfields
rics.Forengineeringdatasets,interestingly,onlyunweightedand ofapplication.
radical weighted versions of the π metrics show a significant Themainstreammetricsaregenerallyinsensitivetothediffer-
difference for the KDLOR classifiers in addition to AC2 and BP ence between the classifiers, except for MCC. The mean F1 and
metrics.Noneofthemainstreamandκ metricsissensitivetothe MCC show sensitivity against the slight difference between the
differencebetweenKDLOR andKDLOR .Mostmetricsaresensi- classifiersforsomeordinalclassifiersandapplicationfields.
1 2
tivetothedifferencebetweenKDLORclassifiersforlifesciences The number of features has no impact on the ability of both
andotherdatasets.Onlyaccuracy,macrorecallandmacroF1are mainstream and weighted agreement metrics to distinguish the
insensitive. multi-classclassificationperformanceofclassifiers.Thesensitiv-
ity of the metrics is highly related to the characteristics of the
5.2.3. Impactofthenumberoffeatures datasetsasinvestigatedinSections5.2.1and5.2.2.
To further investigate the sensitivity of the metrics against
different numbers of features, we worked with datasets ssci15, 6. Discussion
ssci14,other3,eng2,ssci13,ssci11,lsci4,lsci5,lsci11fromTable
B.2 of Appendix B. The numbers of features of ssci15 and ssci11 Assessing the performance of classifiers in supervised ma-
arereducedto2and7,respectively,tohavef =2,3,...,10fea- chine/deeplearningiscrucialtochoosingtheclassifiertoemploy.
turesintheconsidereddatasets.TheprocedureoutlinedinFig.1 This problem gets challenging when the classification task is a
isimplementedwithSVMOP,WKNNOR,andKDLORclassifiersfor multi-class classification with ordinal classes. In this work, we
eachdataset.Thetwo-samplet-testisusedtoassessifthereisa focusedonthemetricsusedtoassesstheperformanceofordinal
significant difference between Classifier and Classifier . The p- multi-class classifiers based on the qualitative understanding of
1 2
valuesofthetestsaregiveninTableB.4,B.5andB.6ofAppendix error.Cohen’sκ-measurehasbeenusedinapplicationsasoneof
BforSVMOP,WKNNOR,andKDLORclassifiers,respectively. the promising metrics for classifiers without distinguishing the
In Table B.4, B.5 and B.6 of Appendix B, cells with bold font type of multi-class categorical responses as ordinal or nominal.
show the metrics that produce a significant difference between Manyotheragreementmeasuresandtheirweightedversionsfor
the two classifiers; hence, they are sensitive to the slight dif- ordinal data are proposed in the literature. Furthermore, from
ferencebetweentheclassificationperformanceofclassifiers.For the previous works, it is known that there are better perform-
all classification methods of SVMOP, WKNNOR, and KDLOR, the ing measures than Cohen’s κ in the area of agreement studies.
sensitivity of all the metrics is not impacted by the increasing Consideringthese,weconductedtwoextensivenumericalstudies
number of features. For SVMOP, the mainstream metrics are with 37 metrics composed of the mainstream and agreement
insensitive for all the considered number of features. Weighted metricstoinvestigatethereliability/usefulnessoftheagreement
κ and π metrics detect the difference just for the dataset with measuresasevaluationmetricsforordinalmulti-classclassifiers.
seven features. Metrics are more sensitive to the difference be- WeidentifiedScott’sweightedπ-measureasastrongalternative
tween WKNNOR classifiers. While the mainstream metrics are toCohen’sweightedκ.
sensitive to the difference between WKNNOR classifiers with 6 In the first numerical study, the ability of metrics to capture
features, weighted agreement metrics are sensitive for multiple the classification performance as close as the true accuracy is
numbersoffeatures.Thebestsensitivityresultsareseenforthe analyzed through randomly generated synthetic confusion ma-
weightedBPmetric,whichdetectsthedifferencefor2,5,6,and trices under different data compositions and different levels of
7 features. For KDLOR classifiers, the weighted κ and π metrics accuracy in the classification performance. Ordinal multi-class
showsensitivity,withthedatasetshaving5and7features. classification processes are not perfect. Thus, they are prone to
the composition of ordinal response and sample size. We show
5.3. Conclusions thatthecompositionofdataconsiderablyinfluencestheaccuracy
ofmetrics.Themainstreammetrics,exceptMCC,areobservedto
Underdifferentdatacompositions,Scott’sπ metricsarecon- be insensitive to capture different types of misclassification. In
sistently sensitive to the difference between classifiers for all contrast, the metrics based on agreement measures react better
ordinalclassificationmethods,whilemainstreammetrics,except tomisclassificationinindividualclassesofthedependentfeature.
MCC and IA are not, in general. Other agreement metrics are Sincethemainstreammetricshavethemaindiagonalofthecon-
as consistent as Scott’s π in distinguishing classifiers under dif- fusionmatrixandoneofitsmarginsintheirformulations,theydo
ferent data compositions. Specifically, metrics have difficulty in not capture the misclassification that occurs in the off-diagonal
separating the performance of classifiers for extremely imbal- cells.OnlyMCCtakesbothmarginsintoaccountandshowsbetter
anced datasets where Scott’s π metric works best. Among the sensitivitythantheothermainstreammetrics.Ontheotherhand,
agreement metrics, while κ, π, and α generally have similar (weighted)agreementmetricsconsiderdiagonalandoff-diagonal
behavior, AC2 and BP have similar responses to the slight dif- cellsandmargins(rowandcolumntotals)oftheconfusiontable
ference between the classifiers. All the metrics perform better to capture the correct classifications as well as the magnitude
in distinguishing the classifiers for the SVMOP method and the of divergence from the correct classifications. The level of true
worstperformancefortheKDLORclassifiers. accuracyisanotherimportantfactorontheperformanceofmet-
Engineeringdatasetsproducenotablydifferentpairwisecom- rics.Whenthetrueaccuracyislow,themetrics’marginoferror
parison results for all ordinal classification methods than the toevaluatetheclassificationperformanceincreases,mainstream
other fields of application. The results for the datasets catego- metrics become highly insensitive to misclassification, and the
rized as other fields of application or life sciences are generally rangeofagreementmeasuresincreases.Therefore,thereliability
similar. Among the agreement metrics, π and κ metrics do not ofallmetricsishigherwhentheyindicatehighperformance.The
work as desired for engineering datasets, while AC2 and BP are casewithalowtrueaccuracyischallengingbecauseitpushesthe
mostly sensitive to the differences between the classifiers. For cellcountstooff-diagonalcellsoftheconfusiontable.Themetrics
themainstreammetrics,onlytheaccuracymetricissensitivefor that do not incorporate off-diagonal cells of the confusion table
14

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
Scott’sunweightedπ
in their formulation got more negatively impacted in detecting producesclosevaluestoMCCundersome
a low level of accuracy. Cohen’s κ and Scott’s π with quadratic scenarios. Besides, Gwet’s unweighted AC2, Brennan–Prediger’s
weightsperformbetterthanalltheconsideredmainstreammet- unweightedBP,andKrippendorff’sα metricsproduceveryclose
rics and agreement measures under the most challenging data valuestoIAwhenthetrueagreementishighand,insomecasesof
compositions. lowandmoderateagreement.Atheoreticalinvestigationofthese
The second numerical study uses 40 real datasets, including resultsisafuturedirection.
AnotherfuturedirectionisusingScott’squadraticweightedπ
| balanced, | imbalanced, | and | extremely | imbalanced |     | data composi- |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | --------- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tions from social sciences, life sciences, engineering, and other asalossfunctionforordinalimageclassificationandregression.
κ
areas, to create replications via cross-validation. In this study, Cohen’s weighted showed improved generalization ability for
we examined the sensitivity of metrics to small differences be- imageclassification[4]whenusedasalossfunction.Inthissense,
tweentwosimilarclassifiersfromthesameordinalclassification theuseofScott’squadraticweightedπ asalossfunctionwould
method. A useful metric is expected to be sensitive enough to providefurtherimprovement.
| distinguish | such | classifiers. | We  | observed | that MCC | successfully |     |     |     |     |     |     |     |     |
| ----------- | ---- | ------------ | --- | -------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
discriminatestwoclassifierswithsimilarperformance.However,
CRediTauthorshipcontributionstatement
itgenerateshighmarginsoferrorwhenthedatacompositionis
imbalancedorextremelyimbalanced.Scott’squadraticweighted
|     |     |     |     |     |     |     | Ayfer | Ezgi | Yilmaz: | Conceptualization, |     | Methodology, |     | Soft- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ------- | ------------------ | --- | ------------ | --- | ----- |
| π   |     |     |     | κ   |     |     |       |      |         |                    |     |              |     |       |
and Cohen’s quadratic weighted metrics show promising ware, Data curation, Writing – original draft, Review. Haydar
sensitivityforchallengingcases,includingextremelyimbalanced Demirhan: Conceptualization, Methodology, Software, Data
| datacompositions. |     |     |     |     |     |     | curation,Writing–originaldraft,Review. |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Thequadraticweightspenalizemisclassificationquadratically;
hence,theagreementmetricswithquadraticweightsarehighly Declarationofcompetinginterest
sensitivetomisclassification.Scott’sπ
doesnothaveauniformity
assumptionontherowandcolumntotalsoftheconfusiontable.
|     |     |     |     |     |     |     | The authors |     | declare | that they | have | no known | competing |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | --------- | ---- | -------- | --------- | --- |
Instead,itassumesthehomogeneityofmargins.Ifthemarginsof
|             |       |                  |     |                  |     |            | financial | interests | or  | personal | relationships | that | could | have |
| ----------- | ----- | ---------------- | --- | ---------------- | --- | ---------- | --------- | --------- | --- | -------- | ------------- | ---- | ----- | ---- |
| a confusion | table | are considerably |     | non-homogeneous, |     | it implies |           |           |     |          |               |      |       |      |
appearedtoinfluencetheworkreportedinthispaper.
thattheclassifierassignsobjectstothewronglabelsatanotably
| high rate. | This translates |     | into very | poor | performance, | and the |     |     |     |     |     |     |     |     |
| ---------- | --------------- | --- | --------- | ---- | ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Dataavailability
metricscancapturethiscasestraightforwardly.Thus,ingeneral,
π
| Scott’s          | is not       | impacted    | by the      | composition    | of                | data. Cohen’s |                                   |     |       |         |             |           |     |       |
| ---------------- | ------------ | ----------- | ----------- | -------------- | ----------------- | ------------- | --------------------------------- | --- | ----- | ------- | ----------- | --------- | --- | ----- |
| κ                |              |             |             |                |                   |               | Datawillbemadeavailableonrequest. |     |       |         |             |           |     |       |
| does not         | have         | restrictive | assumptions | on             | the margins       | of the        |                                   |     |       |         |             |           |     |       |
| confusion        | table        | as well.    | Therefore,  | Scott’s        | quadratic         | weighted      |                                   |     |       |         |             |           |     |       |
| π                | κ            |             |             |                |                   |               | Acknowledgments                   |     |       |         |             |           |     |       |
| and Cohen’s      |              | generally   | show        | satisfactory   | preciseness.      | How-          |                                   |     |       |         |             |           |     |       |
| ever, the        | assumptions, | such        | as          | the uniformity | of                | the margins   |                                   |     |       |         |             |           |     |       |
|                  |              |             |             |                |                   |               | The authors                       |     | would | like to | thank three | reviewers | for | their |
| of the confusion |              | table BP    | or AC2,     | limits         | their preciseness | for           |                                   |     |       |         |             |           |     |       |
commentsthatconsiderablyimprovedtheclarityofthearticle.
imbalanceddatacompositions.Duetothetheoreticalrelationship
| between Cohen’s |     | κ and | MCC for | symmetric | confusion | matri- |     |     |     |     |     |     |     |     |
| --------------- | --- | ----- | ------- | --------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ces, MCC also show satisfactory preciseness when the confusion AppendixA. Supplementarydata
matrixisnear-symmetric.
|          |     |            |      |           |          | π           | Supplementary |     | material | related | to this | article | can be | found |
| -------- | --- | ---------- | ---- | --------- | -------- | ----------- | ------------- | --- | -------- | ------- | ------- | ------- | ------ | ----- |
| Based on | the | results of | both | numerical | studies, | Scott’s and |               |     |          |         |         |         |        |       |
κ online at https://doi.org/10.1016/j.asoc.2023.110020. Tables A.1
| Cohen’s | metrics | with quadratic |     | weights | are both | sensitive to |          |        |         |          |         |            |           |     |
| ------- | ------- | -------------- | --- | ------- | -------- | ------------ | -------- | ------ | ------- | -------- | ------- | ---------- | --------- | --- |
|         |         |                |     |         |          |              | to A.14, | Tables | B.15 to | B.17 and | Figures | B.1 to B.3 | are given | in  |
thesmalldifferencesbetweenclassifiersandproduceclosevalues
theSupplementaryMaterial.
| to the true           | level | of accuracy     | in  | most of the  | considered | scenar-         |            |     |     |     |     |     |     |     |
| --------------------- | ----- | --------------- | --- | ------------ | ---------- | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| ios. Therefore,       | they  | are recommended |     | to be        | used       | in practice, in |            |     |     |     |     |     |     |     |
| general. Specifically |       | for engineering |     | applications |            | and low true    | References |     |     |     |     |     |     |     |
performance,theuseofquadraticweightedAC2metricisrecom-
mended.Werecommendavoidingaccuracy,recall,precision,and [1] C. Deng, X. Liu, C. Li, D. Tao, Active multi-kernel domain adaptation for
hyperspectralimageclassification,PatternRecognit.77(2018)306–315.
macroF1forextremelyimbalanceddatasets.MeanF1hasabetter
|     |     |     |     |     |     |     | [2] L. Kook, | L. Herzog, | T.  | Hothorn, | O. Dürr, B. | Sick, Deep | and interpretable |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | -------- | ----------- | ---------- | ----------------- | --- |
performancethanmacroF1butisnotasgoodasScott’sweighted
|     |     |     |     |     |     |     | regression | models | for | ordinal outcomes, |     | Pattern Recognit. | 122 | (2022) |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ----------------- | --- | ----------------- | --- | ------ |
π.Insomecases,therecentlyproposedmetric,IA,isusefulinthe
108263.
performanceassessmentofordinalclassifiers.However,itisnot [3] L. Li, L. Ma, L. Jiao, F. Liu, Q. Sun, J. Zhao, Complex contourlet-CNN for
polarimetricSARimageclassification,PatternRecognit.100(2020)107110.
recommendedforgeneraluse.
|     |     |     |     |     |     |     | [4] J. de | La Torre, | D. Puig, | A. Valls, | Weighted | kappa loss function | for | multi- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | -------- | --------- | -------- | ------------------- | --- | ------ |
Thisstudyfocusesonaperformanceanalysisoftheevaluation
classclassificationofordinaldataindeeplearning,PatternRecognit.Lett.
| metrics readily | computed |     | using | a given confusion |     | matrix. The |     |     |     |     |     |     |     |     |
| --------------- | -------- | --- | ----- | ----------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
105(2018)144–154.
computation of all the evaluation metrics requires straightfor- [5] C. Ferri, J. Hernández-Orallo, R. Modroiu, An experimental comparison
ward analytical calculations without any iterative method, done of performance measures for classification, Pattern Recognit. Lett. 30 (1)
inmillisecondswithoutconsuminganoticeablecomputermem- (2009)27–38.
ory.Therefore,thespaceandtimecomplexityofcalculatingeval- [6] A.Rácz,D.Bajusz,K.Héberger,Multi-levelcomparisonofmachinelearning
uationmetricsisoutsidethefocusofourstudy.Themainlimita- classifiersandtheirperformancemetrics,Molecules24(15)(2019)2811.
[7] Y.Sasaki,R.Fellow,TheTruthoftheF-Measure,UniversityofManchester:
tionsofourstudyincludethesimulationspaceofsyntheticdata
MIB-SchoolofComputerScience,2007.
study and the number of datasets and replications of the real- [8] P.Czodrowski,Countonkappa,J.Comput.AidedMol.Des.28(11)(2014)
| data study. | Although | we cover | many | scenarios | of  | true accuracy, | 1049–1055. |     |     |     |     |     |     |     |
| ----------- | -------- | -------- | ---- | --------- | --- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
data composition, misclassification, and application areas, there [9] S. Boughorbel, F. Jarray, M. El-Anbari, Optimal classifier for imbalanced
datausingMatthewsCorrelationCoefficientmetric,PLoSOne12(6)(2017)
canstillbeotherapplication-specificcharacteristicstoinfluence
e0177678.
theperformanceofmetrics.
|             |     |                 |     |            |                |        | [10] D. Chicco, | M.J. | Warrens, | G. Jurman, | The Matthews | correlation | coefficient |     |
| ----------- | --- | --------------- | --- | ---------- | -------------- | ------ | --------------- | ---- | -------- | ---------- | ------------ | ----------- | ----------- | --- |
| In addition | to  | the theoretical |     | results on | the similarity | of un- |                 |      |          |            |              |             |             |     |
(MCC)ismoreinformativethanCohen’sKappaandBrierscoreinbinary
weighted Cohen’s κ and MCC, we numerically observed that classificationassessment,IEEEAccess(2021).
15

| A.E.YilmazandH.Demirhan |     |     |     |     |     |     |     |     | AppliedSoftComputing134(2023)110020 |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- |
[11] D.Chicco,G.Jurman,TheadvantagesoftheMatthewscorrelationcoeffi- [24] N.W.S.Wardhani,M.Y.Rochayani,A.Iriany,A.D.Sulistyono,P.Lestantyo,
cient(MCC)overF1scoreandaccuracyinbinaryclassificationevaluation, Cross-validation metrics for evaluating classification performance on im-
BMCGenomics21(1)(2020)6. balanced data, in: 2019 International Conference on Computer, Control,
InformaticsandItsApplications(IC3INA),IEEE,2019,pp.14–18.
| [12] R. Delgado, | X.-A. | Tibau, | Why Cohen’s | Kappa | should | be avoided as |     |     |     |     |
| ---------------- | ----- | ------ | ----------- | ----- | ------ | ------------- | --- | --- | --- | --- |
performancemeasureinclassification,PLoSOne14(9)(2019)e0222916. [25] A. Casagrande, F. Fabris, R. Girometti, Beyond kappa: an informa-
[13] L. Gaudette, N. Japkowicz, Evaluation methods for ordinal classification, tional index for diagnostic agreement in dichotomous and multivalue
in:Y.Gao,N.Japkowicz(Eds.),AdvancesinArtificialIntelligence,Springer ordered-categorical ratings, Med. Biol. Eng. Comput. 58 (12) (2020)
3089–3099.
BerlinHeidelberg,Berlin,Heidelberg,2009,pp.207–210.
[14] S. Baccianella, A. Esuli, F. Sebastiani, Evaluation measures for ordinal [26] M.J.Warrens,AcomparisonofCohen’skappaandagreementcoefficients
regression,in:2009NinthInternationalConferenceonIntelligentSystems byCorradoGini,Int.J.Res.Rev.Appl.Sci.16(2013)345–351.
|     |     |     |     |     |     |     | [27] H. Demirhan, | rTableICC: | An R package for | random generation of 2x2xK |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------- | ---------------- | -------------------------- |
DesignandApplications,IEEE,2009,pp.283–287.
andRxCcontingencytables,RJ.8(1)(2016)48–63.
[15] J.S.Cardoso,R.Sousa,Measuringtheperformanceofordinalclassification,
Int.J.PatternRecognit.Artif.Intell.25(08)(2011)1173–1195. [28] R.Artstein,M.Poesio,Inter-coderagreementforcomputationallinguistics,
[16] A.E. Yilmaz, T. Saracbasi, Assessing agreement between raters from the Comput.Linguist.34(4)(2008)555–596.
[29] K.L.Gwet,Computinginter-raterreliabilityanditsvarianceinthepresence
pointofcoefficientsandlog-linearmodels,J.DataSci.15(1)(2017)1–24.
ofhighagreement,Br.J.Math.Stat.Psychol.61(1)(2008)29–48.
[17] D.Tran,A.Dolgun,H.Demirhan,Weightedinter-rateragreementmeasures
[30] W.Waegeman,L.Boullart,etal.,Anensembleofweightedsupportvector
for ordinal outcomes, Comm. Statist. Simulation Comput. 49 (4) (2020) machinesforordinalregression,Int.J.Comput.Syst.Sci.Eng.3(1)(2009)
989–1003.
47–51.
| [18] K.L. Gwet, | Handbook | of Inter-Rater | Reliability: |     | The Definitive | Guide To |     |     |     |     |
| --------------- | -------- | -------------- | ------------ | --- | -------------- | -------- | --- | --- | --- | --- |
[31] K.Hechenbichler,K.Schliep,WeightedK-Nearest-NeighborTechniquesand
| Measuring | the Extent | of Agreement | Among | Raters, | Advanced | Analytics, |     |     |     |     |
| --------- | ---------- | ------------ | ----- | ------- | -------- | ---------- | --- | --- | --- | --- |
OrdinalClassification,CollaborativeResearchCenter386,DiscussionPaper
| LLC,2014. |     |     |     |     |     |     | 399,2004,http://dx.doi.org/10.5282/ubm/epub.1769. |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- |
[19] A.Sellami,S.Tabbone,Deepneuralnetworks-basedrelevantlatentrepre-
|     |     |     |     |     |     |     | [32] B.-Y. | Sun, J. Li, D.D. | Wu, X.-M. Zhang, W.-B. | Li, Kernel discriminant |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | ---------------------- | ----------------------- |
sentationlearningforhyperspectralimageclassification,PatternRecognit.
learningforordinalregression,IEEETrans.Knowl.DataEng.22(6)(2010)
| 121(2022)108224. |     |     |     |     |     |     | 906–910. |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- |
[20] A. Ben-David, Comparison of classification accuracy using Cohen’s [33] M.Kuhn,K.Johnson,etal.,AppliedPredictiveModeling,Vol.26,Springer,
WeightedKappa,ExpertSyst.Appl.34(2)(2008)825–832.
2013.
| [21] S. García, | A. Fernández, | J. Luengo, | F. Herrera, | A   | study of | statistical tech- |     |     |     |     |
| --------------- | ------------- | ---------- | ----------- | --- | -------- | ----------------- | --- | --- | --- | --- |
[34] M.C.Heredia-Gómez,S.García,P.A.Gutiérrez,F.Herrera,Ocapis:Rpackage
niques and performance measures for genetics-based machine learning: forordinalclassificationandpreprocessinginscala,Prog.Artif.Intell.8(3)
| accuracyandinterpretability,SoftComput.13(10)(2009)959. |     |     |     |     |     |     | (2019)287–292. |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- |
[22] T.Saito,M.Rehmsmeier,Theprecision-recallplotismoreinformativethan
[35] J.Demšar,Statisticalcomparisonsofclassifiersovermultipledatasets,J.
the ROC plot when evaluating binary classifiers on imbalanced datasets, Mach.Learn.Res.7(2006)1–30.
PLoSOne10(3)(2015)e0118432. [36] J.Gross,U.Ligges,nortest:Testsfornormality,2015,URL: https://CRAN.R-
[23] A. Korotcov, V. Tkachenko, D.P. Russo, S. Ekins, Comparison of deep project.org/package=nortest,Rpackageversion1.0-4.
| learning | with multiple | machine | learning | methods | and | metrics using |     |     |     |     |
| -------- | ------------- | ------- | -------- | ------- | --- | ------------- | --- | --- | --- | --- |
[37] J.Fox,S.Weisberg,AnRCompanionToAppliedRegression,thirded.,Sage,
diversedrugdiscoverydatasets,Mol.Pharm.14(12)(2017)4462–4475. ThousandOaksCA,2019.
16