---
conversion_metadata:
  converted_at: "2026-07-21T07:27:20Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Martin J. et al.pdf"
  source_pdf_sha256: "9dc1183d421b561686c5dd4b940a1c514f77177443e379cb5dcfa4b2d1136427"
  page_count: 26
  markdown_char_count: 71966
---

AnnalsofOperationsResearch
https://doi.org/10.1007/s10479-025-06514-x
ORIGINAL RESEARCH
Anovelfinancialperformancemetrictominimize
misclassificationcostsinmodelselection
John Martin1·Mali Abdollahian1·Sona Taheri1 ·David Akman1
Received:3January2023/Accepted:28January2025
©TheAuthor(s)2025
Abstract
Anovelfinancialperformancemetric(FPM)isintroducedseekingtominimisethemisclas-
sificationcostarisingfromfalsepositivesandfalsenegativesincreditriskassessment.Using
theGermanCreditDataset(GCD),importantfinancialvariablesaresimulatedaccordingto
fourdifferentassetclassestoenableamoreaccurateandreliable,multidimensionalmodel
selection.ThemisclassificationcostarisingfromFPMiscomparedwithcommonlyusedsta-
tisticalmetricsandthecreditscoringexampledependentcostmatrix(CSEDCM)metric.The
resultsshowthatCSEDCMunderestimatesfalsepredictioncostsbyasmuchas99%com-
paredtotheFPM.Arangeofhigh-performancemachinelearningmethodswascompared
usingFPMandstatisticalmetrics.TheMulti-LayerPerceptronoutperformedothermethods
onstatisticalmetricsandoverallonfinancialcosts,whileamixofalgorithmsworkedbest
oneithersideofthedecisionthreshold.TheresultsconfirmedthattheproposedFPMwould
provideasignificantfinancialbenefittoorganisations.
Keywords Creditscorecard·Financialperformancemetric·Machinelearning·German
credit
1 Introduction
Acreditdefaultisanegativeeventforbothborrowersandlenders,butcanalsoimpactthe
broadereconomy.Becausecreditisakeydriveroftheeconomy,essentialforthestability
andgrowthoftheglobalfinancialsystem,noeconomy,irrespectiveofhowadvanceditmay
be,candevelopinitsabsence(Banu,2013).Astheglobalfinancialcrisisandmorerecent
eventssuchastheCOVID-19pandemichavedemonstrated,creditlossesrelatedtoloanscan
haveasignificantdetrimentalimpactonthebroadereconomy(Cantrelletal.,2014).
B
SonaTaheri
sona.taheri@rmit.edu.au
JohnMartin
S3801949@student.rmit.edu.au
MaliAbdollahian
mali.abdollahian@rmit.edu.au
DavidAkman
david.akman@rmit.edu.au
1 SchoolofScience,RMITUniversity,Melbourne,VIC,Australia
123

AnnalsofOperationsResearch
Toprotectagainstlosses,lendersseektomaintainrobustlendingpracticesthroughopti-
mising credit risk assessment. Indeed, the centrality of credit to the monetary economy
throughout the economic cycle underscores the importance of accurate credit assessment.
Historically,creditworthinesswasevaluatedusinghumanjudgement.However,thescaleof
lendinghasincreasedovertimesuchthatcontemporaneously,mostlendersdeployclassifi-
cationmodelstoperformthistaskatscale.
Scorecardmodelsareoneofthemainapplicationsofclassificationmodelsincreditrisk.
Used to assess creditworthiness, scorecard models associate historical characteristics like
priorloanperformancewithdefaulttoestimatetheprobabilityofdefault.Oncethishashas
beenderiveditisthencomparedtocut-offthresholdstodeterminetheoutcome:approvalor
rejection.
Agreatdealofpriorresearchhasbeenpublisheddetailingthecomparativeperformance
of various statistical and machine learning algorithms. Martin et al. (2024) compared a
widerangeofindividualandensemblealgorithmsforcreditscoring.Theyshowedthatthe
bestindividualperformerwasaGeneralisedAdditiveModelandthebestoverallperformer
was a Random Forest and K-Nearest Neighbour ensemble. Similarly, hybrid models have
performed well on public datasets such as German credit. Tripathi et al. (2020) used an
Extrememachinelearningapproach.Mahbobietal.(2023)foundthattheSupportVector
MachinealgorithmperformedbestunderaK-NearestNeighboursamplingapproach.
Weconsidermethodswhichhaverecentlybeenshowntooutperformotherapproachesin
creditriskmodellingresearchincludingRandomForest(RF),GradientBoostingMachine
(GBM),ArtificialNeuralNetworks,specificallytheMulti-LayerPerceptron(MLP),Decision
Trees(DTR)andSupportVectorMachine(SVM).Wecomparetheperformanceofthesefive
algorithmswiththatofthegoldstandardusedinindustry,LogisticRegression(LR),using
thestatisticalandcostperformancecriteriadiscussedinthenextsections.
Maincontributionsofthispaperare:
1. IntroducinganewFinancialPerformanceMetric(FPM)toestimatethetruecostsarising
frombothfalsepositivesandfalsenegatives;
2. Providinginsightsoncostdynamicsasaconsiderationinthemodelselection,andopti-
misingtheselectionbycombiningstatisticalmethodswiththedevelopedFPM;
3. EvaluatingthesuitabilityofapubliclyavailableGermanCreditDataset(GCD)forcredit
riskmodelling,andsimulatingimportantfinancialvariableswhichareoftennotavailable
inpublicdatasets;
4. ComparingtheproposedFPMwithanexistingmetric,creditscoringexampledependent
costmatrix(CSEDCM)metric,aswellascommonlyusedstatisticalcriteria;
5. Comparingcostdynamicsacrossfoursimulatedassetclassesobservedatlargebanksto
understandtheimpactofdefaultandopportunitycostacrossdifferentloanvalues;
6. ComparingtheperformanceofLogisticRegressionwithaselectionofhigh-performance
machine learning algorithms utilizing the commonly used statistical criteria and the
proposedFPM,anddeterminingwhichalgorithmoutperformsinestimatingcostsarising
frombothfalsepositivesandfalsenegatives.
The rest of the paper is organised as follows. First, we provide a brief introduction on
theresearchworkinSect.1.InSect.2,wepresentanoverviewofcommonlyusedstatistical
measuresofperformance.Section3presentsanoverviewoncostperformancemeasuresand
introducesanewapproach.InSect.4,themachinelearningmethodsusedareprovided.The
datasetandnumericalresultsaredescribedinSect.5.Thediscussion,conclusionandsome
futuredirectionareprovidedinSect.6.
123

AnnalsofOperationsResearch
2 Statisticalperformance
Traditionallythefocusincreditriskmodellingresearchhasbeentooptimisetheidentification
of true positives, that is, optimizing alignment between the prediction and observation of
default, with scant regard for ‘non-defaults’. Researchers and industry practitioners alike
havemainlyreliedontheuseofstatisticalmetricstomeasuremodelperformanceandselect
thestrongestmodel.
Conceptually,theunderlyinglogictothispracticeisthatbyselectingthemodelwiththe
strongestmetricsmodellerscanidentifythemodelwhichismostfitforpurpose.Inindustry
and academia alike, classical statistical performance criteria including the Area under the
ReceiverOperatingCurve(AUC),Accuracy(ACC)andSomers’Delta(Gini)areamongst
themostwidelyusedmodelmetricsreportedandusedformodelselection.
However,priorresearchhasidentifiedsomeproblematicfeaturesofAUC,ACCandGini,
whichsuggesttheirusecanleadtoincorrectconclusions(see,forexample,Verbrakenetal.,
2014).TheGinistatistichasalinearrelationshipwithAUC,yetbotharecommonlyreported
despite the obvious redundancy of reporting directly related performance metrics. Gini is
definedas
n(cid:2)+m(cid:3)(cid:4) (cid:5)
Gini =1− F m.BADk −F m.BADk−1
(cid:4)
k=2
(cid:5)(cid:6)
× F n.GOODk −F n.GOODk−1 ,
where F m.BADk (F n.GOODk ) is the kth vector value of the empirical distribution function
of bad (good) applicants, while m and n are the number of elements of the bad and good
distributions,respectively.Furtherdetailscanbefound,forexampleinThomasetal.(2002).
Hand(2009)statesthatGinimaynotbesuitableasameasureofperformanceofapplication
scorecardssinceit(aswellassomeothercommonlyusedmetricsincludingtheKolmogorov–
Smirnov (KS) statistic and Information Value (IV)) uses irrelevant information. It fails to
measureinformationonthebadrateamongacceptswhichistheaspectofperformancewe
areactuallyinterestedin.
The Receiver Operating Curve (ROC) is a graphical tool used to visualise the trade-
off between sensitivity and specificity, while the AUC is a scalar measure of aggregate
performance which summarises the ROC into a single value. In Anagnostopoulos et al.
(2019),theAUCiscriticisedforhowithandlesthetrade-offbetweenfalsepositivesandfalse
negativeswherebytherelativeseveritiesofmisclassificationsaretreateddifferentlybetween
differentclassifiers.Moreover,Marzban(2004)showedthatAUCdiscriminateswellbetween
‘good’and‘bad’models,butnotbetweengoodmodels.HandandAnagnostopoulos(2013)
dismissAUCasaportmanteaumeasure,equivalenttointegratingoverarangeofpossible
values,concludingthattheROCisanincoherentperformancemeasure.TheAUCisdefined
as
1
AUC = ×(Sensitivity+Specificity),
2
wheresensitivityistheTruePositiveRate(TPR)andspecificityistheTrueNegativeRate
(TNR),withSensitivity(TPR)=TruePositives/TotalPositives×100,whereasSpecificity
(TNR)=TrueNegatives/TotalNegatives×100.
Asstatedabove,thereisalinearrelationshipbetweenAUCandGini,andeachcanbe
easilycalculatedfromtheotherusingthefollowingequation,suggestingredundancyinthe
123

AnnalsofOperationsResearch
commonpracticeofpresentingbothmeasuresformodelevaluationand/orselection:
Gini +1
AUC = .
2
Ontheotherhand,ACCworksbyeffectivelysummingaccurateclassificationsasaproportion
ofallclassifications,whichisproblematicinscenarioscharacterisedbyseverelyimbalanced
target variables typical in credit modelling research. For example, for an observeddefault
rateof0.05amodelmaypredictall observationsasnon-defaults,yetstillreceiveanACC
of 0.95. While a common solution is to perform sampling to increase the minority class
representation. This rarely fully deals with the class imbalance bias in real-situations and
createsfurthercomplicationsdownstreamintermsofmodelmonitoring.TheACCisdefined
as
TP+TN
ACC = ,
TP+TN +FP+FN
whereTPisequaltoTruePositive,TNequalsTrueNegative,FPequalsFalsePositiveand
FNequalsFalseNegative.
3 Costperformance
Asdiscussedintheprevioussection,themostcommonlyusedstatisticalmetricshavesome
seriousdrawbackswhichraisesquestionsaroundtheirvalueinmodelselection,particularly
inrelationtocommercialapplicationssuchascreditrisk.Moreover,focusingonlyonthis
aspectofperformanceignoressomeveryimportantpracticalconsiderations.Inclassification
researchthecorrectselectionofperformancemetricsisoneofthemostimportantissuesin
evaluating a classifier’s performance (Liu et al., 2014). Indeed, a vast array of alternative
metricsareavailableandoptimizingthewrongmetricdirectlytranslatesintolostrevenue
(Dmitriev&Wu,2016).
Themostimportantobjectiveinbankingisprofit,andthereforeonceamodelhasbeen
determined as functional the comparative costs must be considered. Selecting the optimal
approach is not possible using standard classification metrics because they treat the costs
of misclassifications the same, which is not true in real credit risk management (see, for
example, Fiore et al., 2017). Credit risk is particularly well aligned to the use of profit-
basedorfinancialloss-relatedmeasures(Maldonadoetal.,2017),whichseektooptimisea
commercialoutcomeasopposedtoastatisticalmetric.
Costsensitivelearningseekstooptimisedecision-makingwheremisclassificationcosts
incur different penalties. While a valid application of cost sensitive learning can assume
thesamemisclassificationcost,Elkan(2001)suggestedthatamorerealisticproblemexists
wheremisclassificationcostsareexample-dependent,inthesensethatthecostsvaryamong
examplesandnotonlyamongclasses.Thisisparticularlysoforcreditrisk,wheremisclas-
sificationcostsvarybothwithinandbetweenresponseclasses.
Indeed,researchershavelongbeenawareoftheprofitmotiveasacentraldrivingfactor
inmodelselectionincreditriskyetonlyahandfulhavesoughttofindwaystoincorporate
this perspective into model selection. One of the biggest obstacles has been the dearth of
availabledatasetscontainingthenecessaryfinancialinformationtocompareperformanceon
cost(Aodha&Brostow,2013),leadingtoavarietyofapproachestoovercomethisshortfall.
Forexample,Xiaetal.(2017)simplyassumedthatthecostsofmisclassifyingadefaulting
borrowerarelargerthanthatofmisclassifyingagoodone.SchebeschandStecking(2005)
123

AnnalsofOperationsResearch
Table1 CSEDCMmodel,giveninEq.(1)
|                   |     | Actualpositiveyi |     | =1      | Actualnegativeyi | =0      |     |
| ----------------- | --- | ---------------- | --- | ------- | ---------------- | ------- | --- |
| Predictedpositive |     |                  |     | CTPi =0 | CFPi             | =ri +Ca |     |
FP
ci =1
| Predictednegative |     | CFNi | =Cli | ·LGD |     | CTPi =0 |     |
| ----------------- | --- | ---- | ---- | ---- | --- | ------- | --- |
ci =0
simplifiedthisproblembyassumingthatthemisclassificationcostsofabadborrowerasa
goodborrowerasfivetimesmorecostlythanmisclassificationofagoodborrowerasabad
borrower,yetwithoutdataneitherpaperwasabletoempiricallyevaluatethisassumption.
Other researchers with access to data containing financial performance variables have
constructedcostmetricsusingavarietyofdifferentapproaches.Forinstance,Zhangetal.
(2018)appliedtheMultipleInstanceLearningmethod,proposingacostsensitiveoptimiza-
tion approach which sought to minimise misclassification costs. In this work, instead of
quantifyingdifferencesinmisclassificationcosts,theauthorsweightedmisclassificationsby
similarityaccordingtodemographicfeaturesandtransactionalbehaviour.
3.1 Existingcostmetrics
Wangetal.(2021)proposedanapproachtoestimatecostsassociatedwithriskbasedpricing,
wherebysimilargroupsofexposureswereassignedincreasinglevelsofinterestrelativeto
theirriskinpeer-to-peerlending.Theyassignedacostmatrixtopooledrisksfordifferential
pricing,whichsoughttoassigndifferential misclassification costmatrices, withthelower
triangular C1 assigned the economic costs with a predicted ‘good defaulting’, and C2 the
additivecostofmisclassifyinganapplicanttothewrongpoolandtheopportunitycostof
lostbusiness.Nevertheless,theuncertaintyarisingfromnewbusinessinopportunitycosts
wasnotconsideredinthiswork.
Bycontrast,Bahnsenetal.(2015)andVerbrakenetal.(2014)bothsoughttoassignacost
matrixwithdifferentialcostsaccordingtoeachoutcome.Bahsenetal.(2015)f(cid:7)ocusedon
(x ,y )∈
misclassificationonly,(cid:8)wheretruepredictionswereassumedtocostnothing.Let
i i
Rn×R,i =1,...,N beasetofpredictor(explanatory)variablesxandresponse(indicator)
variable y.TheBahnsenetal.(2014,2015)creditscoringexampledependentcostmatrix
(CSEDCM)metricisgivenbelow:
|     |     | (cid:4) | (cid:5) | (cid:9) | (cid:10) |     |     |
| --- | --- | ------- | ------- | ------- | -------- | --- | --- |
∗)
|            | Cost | f(x | = y   | c C +(1−c | )C       |          |     |
| ---------- | ---- | --- | ----- | --------- | -------- | -------- | --- |
|            |      | i   | i     | i TP      | i FN     |          |     |
|            |      |     |       | (cid:9)   |          | (cid:10) |     |
|            |      |     | +(1−y | ) c C     | +(1−c )C | ,        | (1) |
|            |      |     |       | i i FP    | i        | TN       |     |
| , =1,...,N |      |     |       |           | ,C       | ,C ,C    |     |
wherec i i arepredictedlabels,andvaluesC TP TN FN FP indicatethe
costsoftruepositive,truenegative,falsenegative,andfalsepositive,respectively.Notethat
C =C =0asthetruepredictiondonotaccrueanymisclassicationcost.C shows
| TP TN |     |     |     |     |     | FN  |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
lossesifthecustomeri defaultstobeproportionaltohiscreditline,whereasC FP isminus
profitplustheexpectedlossifthecustomerdoesnotdefault.
Table 1 sets out the CSEDCM approach according to the four outcomes for a binary
classificationmodel.
123

AnnalsofOperationsResearch
Here,r isthelossinprofitbyrejectingwhatwouldhavebeenagoodcustomer,yetthis
i
value must be present valued. The term Ca is minus the profit of an average alternative
FP
customer (r¯) times the probability they will not default (π ), plus the average credit line
0
(C ¯ l) times Loss Given Default (LGD) times the probability they will default (π ), that is
1
Ca =−r¯·π +C ¯ l·LGD·π .
FP 0 1
Takingaslightlydifferentroute,Verbrakenetal.(2014)soughttoestimatecostscompared
to a model where all applicants are approved, that is where no credit scoring takes place.
Morespecifically,theyproposedtheExpectedMaximumProfit(EMP)modelassigninga
benefitincorrectlyidentifyingadefaulter,b ,whichisthefractionoftheloanamountwhich
0
islostafterdefaultas
LGD×EAD
b = ,
0
A
where EAD is Exposure at Default, and A is Principal Exposure. By contrast, the costs
associated with misclassifying a good applicant as a defaulter are equal to the Return on
Investment(ROI)oftheloan,definedasfollows:
rM
ROI = −1,
1−(1+r)−M
wherer istheInterestRate,andM isMaturity.
Further,Verbrakenetal.(2014)proposedthatLGDfollowsauniformdistribution,and
theEMPmetricisgivenbelow:
(cid:11)
1
EMP = P(T(θ);b ,ROI)×π F (t)−h(b )db ,
0 0 0 0 0
0
wheret isthedefinedcutoffthresholdvalue,T istheoptimalcutoffvalueunderthegiven
circumstances, θ is the cost-benefit ratio, π F (t) is a true positive case, h(b )db is the
0 0 0 0
probabilitydistributionassociatedwithcorrectlyidentifyingadefaulter,and
P(t;b ,ROI)=b ×π F (t)−ROI ×π F (t),
0 0 0 0 1 1
withπ F (t)indicatingafalsepositivecase.
1 1
3.2 Proposedfinancialperformancemetric
Inthissection,weintroduceamorerealisticestimateofthemisclassificationcostsarising
fromcreditrisk,thefinancialperformancemetric(FPM).WeformulatetheFPMbasedon
thepriorresearch,inparticularthecontributionsofBahnsenetal.(2015)andVerbrakenet
al. (2014).The FPMseeks to incorporate elements which have hitherto been omitted. We
summariseourapproachbelowandhighlightdifferenceswiththeexistingapproaches.
Loss estimation in credit risk has matured significantly thanks to advancesrequired by
regulatoryregimessuchasIFRS9,publishedin2014(IASB,2014).IFRS9wastheinterna-
tionalaccountingstandardboard’sresponsetothefinancialcrisis,aimedatimprovingthe
accounting and reporting of financial assets and liabilities (Gea-Carrasco, 2015). We note
thatwhilelostinterestissometimesrecognisedinsomeformulationsofrealisedLGD,we
haveseparatedoutthiscomponenttomakeitmoreexplicit.
WhileweagreethatLGDmustbeincorporatedintocostestimatestoobtainatrueviewof
thepotentialloss,Bahnsen’sCSEDCMmetricusesmaximumcreditlineinallestimatesof
losses,yetitisclearthatEADmustbeevaluatedsinceEADistheactualamountthelender
hasatrisk.Moreover,theCSEDCMapproachignorestheinterestlostfromadefaultwhich
123

AnnalsofOperationsResearch
isanimportantconsideration,notingtheprofitcomponentasakeymotivationforbeingin
thebusinessoflending.
Furthermore, in estimating the cost of a false positive, there is some debate on how
to incorporate the portfolio level uncertainty for the alternative customer (the cost of the
‘nextcustomer’whothemodeldeemsthecreditworthy).Wehavechosentoincorporatean
amendedversionoftheaverageexpectedlossfortheportfoliousingtheexpectedlossfor-
mula,asthesecostscanreasonablybeexpectedovertimeandhaveincorporatedameasureof
theuncertaintyoffutureprofits.Intheresultssectionwedescribeacomparisonbetweenthe
proposedapproachandtheCSEDCMapproachtodemonstratethemodelselectionimplica-
tions.
Similarly, Verbraken’s model presents some opportunity for refinement to improve the
estimationofexpectedcosts.Forexample,ROIcannotpossiblybeassimpleasmultiplying
theinterestrateagainsttheprinciplefortheloanterm.Thefactthatthereisadefaultrate
means that a proportion of the portfolio will never reach its contractually agreed maturity
term.Thusremainingmonthsonbookmustbeconsideredtoaccuratelyassessthetruevalue
lost.Whileaveragesaresometimesunavoidablewherespecificinformationisn’tavailable,
thegrossvalueofinterestrevenuelostfromamortgagecustomerwhodefaultsattwomonths
isvastlydifferentfromonewhodefaultsatthe320thmonth.Moreover,thefinancialprofiles
oftheunderlyingcustomerswhoformthesetwodisparatescenarioswillbeverydifferent.
Therefore,ignoringtheremainingmonthsonbookwouldsystematicallyunderpredictcosts
foridentifiablecustomergroups.
In addition, since credit decisions that result in default and opportunity costs (that is,
positiveandnegativemisclassifications)occursimultaneously,theyshouldbesummedrather
than subtracted. Finally, it is unrealistic to assume a starting position of the no credit risk
modelasevenpriortothewide-scaleadoptionofclassificationmodelsexpertjudgmentwas
usedtoscoreapplicants.
OurproposedFPMadvancescost-sensitivelearningasitappliestocreditscorecardsby
developingamorerealisticevaluationofthefinancialcostsarisingfromeachmisclassifica-
tion.Thesedifferencescanbepotentiallyhugewhenconsideredataportfoliolevelthatmight
comprisehundredsofthousandsofcustomers.Splittingcostsoneithersideofthedecision
boundaryalsoimpartspositivebenefits.Itprovidesthecapabilitytooptimisethethresholdby
minimisingcost.Anysystematicweaknessinachosenmodelcouldbeidentifiedandindeed
overcomebypotentiallyaddingvariablesoreven‘beefingup’thepredictivecapabilityby
combiningmodels.Thus,thecostofafalsenegative,misclassifyingabadcustomerasgood,
isequalto
(cid:2)N
FNC = P(yˆ <t | y =1)×LGD×EAD+PV(ROI ×RMOB),
i i
i=1
where y is the observed outcome (actual output), yˆ is the estimated outcome (modeled
i i
output),and P(yˆ < t | y = 1)arethefalsenegativecases,thefunction PV isapresent
i i
valuewhichdependson ROI and RMOB,with RMOB beingtheremainingmonthson
book, a measure of the number of months remaining on the repayment terms of the loan
agreement.
123

AnnalsofOperationsResearch
Ontheotherhandthecostofafalsepositive,misclassifyingagoodcustomerasbad,is
equalto
(cid:2)N
|     | = P(yˆ | >t | =0)×PV(ROI)−(ROI |     | +y¯×EAD×LGD), |     |
| --- | ------ | --------------------- | --- | ------------- | --- |
| FPC |        | i y i                 |     |               |     |
i=1
| P(yˆ  | > |     | = 0)arethefalsepositivecases, |     |                             |     |
| ----- | ------- | ----------------------------- | --- | --------------------------- | --- |
| where | i t y i |                               | ROI | istheaverageinterestrevenue |     |
fortheportfolio, y¯ istheaveragedefaultratefortheportfolio, y = (y ,...,y ), EAD is
|     |     |     |     |     | 1 N |
| --- | --- | --- | --- | --- | --- |
theaverageEADandLGDistheaverageLGD.
Notethatourproposedapproachallowsustosplitfalseestimatesaboveandbelowthe
decisionthresholdwhichprovidesadditionalinsightsonmodelperformance.Inaddition,it
considersbothintermsofmakingjudgementsonmodelselectionaswellastheoverallview.
TheproposedFinancialPerformanceMetric(FPM)forcalculatesthemisclassificationcost
by:
= FNC+FPC.
FPM (2)
4 Methodsused
Weutilisesixwidelyusedmachinelearningalgorithmsofvaryingcomplexityonapublicly
availabledataset(GCD)toevaluatewhichperformsbestaccordingtoourproposedFPM.
The methods compared include: Logistic Regression, Random Forest, Gradient Boosting
Machine,DecisionTrees,SupportVectorMachineandArtificialNeuralNetworkMultilayer
Perceptron.Next,wegiveabriefdescriptionofeachalgorithmandrefertothereferences
providedformoredetails.
4.1 Logisticregression
Logistic Regression (LR) is the gold standard in credit risk modelling in industry and is
typicallythebaselinemodelincreditscoringmodelcomparisonstudies(Yhip&Alaghe-
band, 2017). However, it has received criticism for its inability to detect non-linear or
non-monotonic relationships. The LR is an extension of linear regression, using a logit
functiontomakethedistancebetweentwobinarypointscontinuous.Thelogitfunctionisa
transformationbetweenthelinearmodelandtheprobabilityofthebinaryoutcome.TheLR
isformulatedas
|     |     | ln(p/1− p)=β | +β +....β | ,     |     |
| --- | --- | ------------ | --------- | ----- | --- |
|     |     |              | 0 1 x 1   | n x n |     |
pistheprobabilityoftheeventoccurring,β isthey-intercept,andβ , =1,...,n
| where                                      |     |     | 0   |     | i i |
| ------------------------------------------ | --- | --- | --- | --- | --- |
| arethecoefficientoftheindependentvariablex |     |     | i . |     |     |
4.2 Decisiontree
DecisionTrees(DTRs)utiliseaflowchartortree-likedecisionmakingapproachthatiseasily
visualisedfromlefttorightandiscomposedof“burst”nodessplitintodifferentpaths.The
threetypesofnodesincludeRootnodes,whichcompiletheentiresampleandarethendivided
123

AnnalsofOperationsResearch
intomultiplesets;Decisionnodes,whicharetypicallyrepresentedbysquares,representsub-
nodesthatdivergefurtherintofurtherpossibilities;andTerminalnodes,whichrepresentthe
outcomethatcannotbecategorizedfurther.Thetreestructureisbuiltfromthetopdownby
selectingthebestdecisionnodetosplitfirst,andthenafter,basedonMeasuresofentropy
andinformationgainareusedtoselectthebestdecisiontonodefirstandthensubsequent
decisions.Weightsarecalculatedforeachchancenodebyestimatingtheconditional(joint)
probabilities.DTRsandvariantsthereofhavebeenshowntobehighlyeffectiveforcredit
riskmodelling(Dumitrescuetal.,2022;Tianetal.,2020).DTRsareformulatedas
(X,y)=(x ,x ,x ,...x ,Y),
1 2 3 n
wherex ,x ,x ,...x aretheindependentvariables,andY isthetargetvariable.
1 2 3 n
4.3 Randomforests
RandomForest(RF)(Breiman,2001)isamorecomplexbaggingimplementationofDTRs.
ItgrowsandcombinesmultipleDTRstocreatea“forest”.TheRFhasdemonstratedsupe-
riormodelperformancewhenappliedtocreditmodellingresearch(Lessmanetal.,2015).
Formally,anRFisapredictorconsistingofacollectionofrandomisedbaseregressiontrees,
asgivenbelow:
r
n
(X,D
n
)= Eθ [r
n
(X,θ
m
,D
n
)],
where Eθ represents the expectation taken with respect to the random parameter θ, con-
ditioned on X and the dataset D . The parameters (θ ,θ ,...,θ ) are independent and
n 1 2 m
identically distributed (i.i.d.) realizations of the randomizing variable θ. Each tree is built
independently by randomizing over subsets of the data or features, and the final output
r (X,D )aggregatespredictionsacrosstheensemble.
n n
4.4 Gradientboostingmachine
GradientBoostingMachine(GBM)isanimplementationofboosting,aniterativetechnique
whichadjuststheweightofanobservationbasedonthelastclassification(Friedman,2001).
GBManditsvariantssuchasExtremeGradientBoostinghavealsoperformedstronglyinthe
comparativeclassificationliterature(Odegua,2020).ThemainideaofGBMistoaddnew
modelstotheensemblesequentially.Ateachparticulariteration,anewweak,base-learner
modelistrainedwithrespecttotheerrorofthewholeensemblesofar.Onecanarbitrarily
specifyboththelossfunctionandthebase-learnermodelsondemand.Thegeneralupdate
ruleinGBMcanbeexpressedas
F m (x)= F m−1 (x)+γ m h m (x), m =1,2,...,M,
wherewhere F (x)isthemodelpredictionaftermiterations(ortrees),and
m
(cid:2)n
F (x)=argmin L(y ,γ),
0 γ i
i=1
anddecisiontreeh (x)isfittedtotheresidualsby
m
h (x)≈r (m).
m i
123

AnnalsofOperationsResearch
Here,thepseudo-residualsiscomputedusing
(cid:12) (cid:13)
r (m) =−
∂L(y
i
,yˆ
i
(m−1))
,
i ∂yˆ(m−1)
i
wherey
istheactualclasslabelofthei-thdatapoint,yˆ(m)
isthepredictedprobabilityofthe
i i
i-thdatapointbelongingtothepositiveclassafterm iterations, x isthei-thinputfeature
i
vector,γ istheweightorlearningrateforthem-thtreeandcontrolsthestepsizeateach
m
iteration,andL isthelossfunction.
4.5 Supportvectormachine
SupportVectorMachines(SVMs)aresupervisedlearningmodelswhichworkbyconstructing
hyperplanesinamultidimensionalspacetoseparatescasesofdifferentclasslabels(Vapnik,
1996).Thesamplesthatlieonboundariesofdifferentclassesarereferredtoassupportvectors.
TheunderlyingprinciplebehindSVM-basedclassificationistomaximizethemarginbetween
thesupportvectorsusingkernelfunctions.SVMshaveachievedsuperiorperformanceinboth
retail(Obare&Muraya,2018)andnon-retailcreditriskassessment(Telesetal.,2021).The
SVMisformulatedas
(cid:2)P
f(x)= a K(x,x ),
i i
i=1
where P is the number of support vectors, a is an element of the parameter vector, x is
i i
a vector of regressors, K is a function referred to as the kernel and a is the number of
i
parameters. The kernel can be a Radial Basis Function, polynomial or a two-layer neural
network.
4.6 Multilayerperceptron
Multilayer Perceptron (MLP) is an Artificial Neural Network characterised by a back-
propagation algorithm which uses a special class of feedforward networks (Baum, 1988).
MLPhasmorethanonehiddenlayerandthenetworkmovesonlyintheforwarddirection,
with no loopback. These neural networks are good for both classification and prediction.
MLP has been successfully deployed in credit risk modelling research achieving superior
performance.MLPcomposesthefinaloutputfunctionofanetworkusing
f (x) = f (a (x)).
k k k
The function is applied to an input activation function consisting of a (x). The input fre-
k
quentlycomprisesacomputationoftheform
a(x) = Wh(x) + b,
wherexistheinputvector,bisthebiasvector,W istheweightmatrixandhistheactivation
functionoutput.Thefunctiona(x)takesavectorargumentandreturnsavectorasaresult,
notethata (x)isjustoneoftheelementsofa(x).
k
123

AnnalsofOperationsResearch
5 Datsetsandnumericalresults
Inthissection,wedescribeGCDandHomeCreditDataset(HCD),thesamplingprocedure,
thedatamodellingandthesimulationprocess.Thisisfollowedbypresentingtheresultsof
ournumericalexperiments.
5.1 Datasetandsampling
ThepubliclyavailableGermanCreditDataset(GCD)(Hofmann,1994)isusedinourexper-
iments.Itcontains1000observationsacross20predictorvariablesandaresponsevariable,
indicating goods (i.e. negatives) and bads (i.e. positives). Due to confidentiality which is
characteristicoffinancialdatamostresearchiscarriedoutusingpubliclyavailabledatasets
suchastheGCD,whichisamongthemostwidelyusedpublicdatasetsforcreditriskresearch
(see for examples, Beque et al., 2017; Due & Graff, 2019; Khashman, 2010; Dong et al.,
2010).
AccordingtoRamezanetal.(2021),thesizeofthetrainingdatasetisamajordetermi-
nantintheclassificationperformance.Theauthorscomparedtheerrorofpredictionacross
differentsamplesizesforavarietyofalgorithmsincludingRF,GBMandMLP.Theyfound
thatallthesealgorithmsachievedmorethan95%accuracywithatrainingsampleof625.
Alametal.(2010)developedanapproachforpowerestimationinLRtodeterminewhether
aparameterissignificantlydifferenttozero,combiningthepriorworkofWhittemore(1981)
andHsiehetal.(1998).Theirresultsshowthatasamplesizeof655isneededtoachievea
statisticalpowerof0.9630.
These studies suggest that using a training sample of at least 655 will achieve strong
accuracyformachinelearningmodelsandadequatestatisticalpowerformodelsincorporating
hypothesistestingasperLR.Thus,thetrainingsampleof712usedshouldbelargeenough
to minimise the error of prediction and to determine the real significance of one or more
parameters.
5.2 Modellingdata
Inthissection,wedescribemodellingtheGCD.Predictorsinthisdatainclude:•Statusof
existingcheckingaccount•Durationinmonth•Credithistory•Purpose•Creditamount•
Savingsaccount•Presentemploymentsince•Installmentrateinpercentageofdisposable
income•Personalstatusandsex•Otherdebtors•Presentresidencesince•Property•Age
inyears•Otherinstallmentplans•Housing•Numberofexistingcreditsatthisbank•Job
•Numberofdependents•Telephone•Foreignworker.
Priortomodelling,allpredictorvariablesaretransformedaccordingtotheWeightsofEvi-
dence(WoE)discretizationapproachwhichiswidelyusedinindustry.WhileLRistheonly
approachutilisedthatrequiresthemonotonicityprovidedbyWoEtransformation,discretiza-
tionwasperformedtoensurethatdataalignedtoindustrypracticeasmuchaspossible.Note
thatmakingexplanatoryvariableseitherstrictlyincreasingorstrictlydecreasing(i.e.mono-
tonic)isacriticalrequirementforscorecardmodels;asindicatorsforriskinesseachretained
variablemustbelinearlyrelatedtodefaultforfacevalidityincreditprovisionenvironments.
TheformulaforWoEdiscretizationisgivenbelow:
(cid:14) (cid:15)
%of y =0,wherex =i
WoE =ln .
xi %of y =1,wherex =i
123

AnnalsofOperationsResearch
Table2 Gammaparametersfor
Assetclass Shape Scale
simulatedEAD
CC 3 5000
SL 3 50,000
Mo 3 400,000
LL/SME 3 1,000,000
5.3 Simulationofdata
Next, we discuss the simulation of the GCD. Due to the lack of information necessary to
evaluatecostparameters,simulatedvariablesrepresentingfourdifferentassetclasseswere
incorporatedintotheGCD.Importantly,onlythe20originalpredictorsandthetargetdefault
variablewereaccessibletothemodel.Thisensuredthatallmodelsoperatedwithidentical
defaultclassinformationwithineachcondition,whethertrainingortesting.Thesimulated
variableswereusedexclusivelyforcostcalculations,whichinformedmodelselectiondeci-
sions.TobuildontheGCD,wesimulatedthekeymissingvariablesrequiredforcostanalysis
acrossthe1000observationsthatcomprisetheunderlyingdataset.
Furthermore,wesimulateEADvaluesaccordingtoaGammadistribution(see,forexam-
plesJimenez&Mencia,2007;Assadsolimani&Chetalova,2017)givenbelow:
za−1e −bz ba
f(z) = , z >0, a, b>0,
(cid:7)(a)
where(cid:7)(a)isthegammafunction,aistheshapeparameter,andbdenotestherateparameter.
WeusetheGammadistributiontosimulatefourdifferentEADrangesrepresentingtyp-
icalmagnitudesofexposureobservedinaselectionofdifferenteconomies.Ourreviewof
lendingstatisticsfromjurisdictionssuchasAustralia(AustralianBureauofStatistics,2024),
theUK(BankofEngland,2024),andtheUSA(Ostrowski,2024)revealedsignificantdis-
paritiesbothbetweenandwithintheseregions.Forinstance,intheUSA,averagemortgage
lending exposures in California are over three times higher than those in Indiana. Further
complicatinggeneralizationsacrossjurisdictionsarefactorssuchasvariationsinexposure
pricing, exchange rates, regulatory practices, and the risk appetites of individual lenders.
Toensurerepresentativeassetclasses,weselectedscale-appropriaterangesthatencompass
typicalportfoliosobservedinAustralia,theUK,andtheUSA.
The primary objective in evaluating these portfolios was to examine the influence of
modelmetrics,includingFPM,betweenportfoliosofvaryingsizes.Specifically,wesought
to determine whether larger interest payments influenced model selection decisions. The
simulated ranges across different portfolio scales provided meaningful differentiation to
supportthisanalysis.
By modelling different exposures according to a Credit Card (CC), Small Loan (SL),
Mortgage (Mo) and Large Loan/Small to Medium Enterprise Loan (LL/SME), we seek
to observe the impact of different default and opportunity cost ranges. This follows from
Lessmanetal.(2015)whofoundthattheimpactoffailingtoconsiderthebiastowardstrue
positiveswasmagnifiedthelargerthecostofafalsepositive.
Aftersettingtheseedtoensurevaluesarereproducible,EADdistributionsweresimulated
usingtheparametersgiveninTable2.
123

AnnalsofOperationsResearch
Table3 Descriptivestatisticsof
|     | Assetclass |     | Mean | Median |     | Standarddeviation |     |
| --- | ---------- | --- | ---- | ------ | --- | ----------------- | --- |
simulatedassets(GCD)
|     | CC  |     | $12,039  | $10,419  |     | $7134   |     |
| --- | --- | --- | -------- | -------- | --- | ------- | --- |
|     |     |     | $152,263 | $139,396 |     | $86,212 |     |
SL
|     | Mo  |     | $1,185,477 | $1,034,473 |     | $698,810   |     |
| --- | --- | --- | ---------- | ---------- | --- | ---------- | --- |
|     |     |     | $2,996,111 | $2,679,932 |     | $1,723,469 |     |
LL/SME
Table4 Observedcountsand
|     | Dataset |     | Good | Bad | Total |     | Default(%) |
| --- | ------- | --- | ---- | --- | ----- | --- | ---------- |
defaultrate(GCD)
|     | Training |     | 502 | 210 | 712 |     | 29.49 |
| --- | -------- | --- | --- | --- | --- | --- | ----- |
|     | Test     |     | 198 | 90  | 288 |     | 31.25 |
Theproportionof the loan alreadypaid (usedto calculate Loanprincipal) is simulated
accordingtoaBetadistribution,thatis:
1
| f(z) | =   | za−1(1−z)b−1, |     | 0≤z | ≤1, |     |     |
| ---- | --- | ------------- | --- | --- | --- | --- | --- |
β(a,b)
where β(a,b) is the beta function, a > 0 and b > 0 are shape parameters. The Beta
distributionwassimulatedwithbothshapeparametersequaltoone.Intheasymptoticsample
this translates to a roughly uniform distribution between zero and one with some random
variation.
Monthly payment (Pmt) amounts are calculated according to the payment equation
detailedinFinlay(2009)as
|     |     | × r/12 | ×(1 + | r/12)12t |     |     |     |
| --- | --- | ------ | ----- | -------- | --- | --- | --- |
P r
| Pmt | =   |     |            |     | ,   |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- |
|     |     | (1  | + r/12)12t | −   |     |     |     |
1
where P =Principal,r=Annualinterestandt=Termoftheloaninyears.
r
Wealsokeeptheunderlyingdataasrealisticaspossibleaccordingtotheaforementioned
hypotheticalassetclasses,basingdistributionsonrealportfoliosobservedatAustralianand
Europeanbanks.Despitetheseefforts,somedifferencesarestillapparentinthedata.The
relativelyhighdefaultrateobservedintheGCDclearlysetsitapartfromdatasetsobservedin
industry.However,givenwell-knownconstraintswithclassificationmodellingitiscommon
practicetoperformsamplingoncreditriskdatasuchthattheminorityclass(iedefaults)is
markedly increased. Therefore, we can simply view the larger than normal minority class
asbeingtheresultofpriorsamplingtoaddresstheclassimbalance.InTable3,weprovide
descriptivestatisticsforthefoursimulatedassetclasses;CC,SL,MoandLL/SME.
InTable4,weprovidethesplitbetweenthetrainingandtestdatasets.Itincludescounts
of good (non-defaulting) and bad (defaulting) observations as well as the percent of each
outcome condition. Random sampling between the training and test datasets led to slight
variationsindefaultingproportions.Initialtestingrevealednosignificantdifferencesinresults
betweenequallysampledclassesandrandomlysampledones.Therefore,tomaintainrealistic
conditions,weoptedfortherandomlysampledapproach,whichiscommonlyusedinindustry
practices.
Afinalpotentialdeviationfromrealityrelatestothecreditcardassetclass,wherebyit
wastreatedlikeaone-offloanheldforasetnumberofmonths.Thisisnotrealisticsinceon
averagecreditcardcustomerstendtodrawdowncreditcontinuously,implyingthatwemay
123

AnnalsofOperationsResearch
Table5 DescriptivestatisticsofHomeCreditDataset(HCD)
Assetclass Mean Median Standarddeviation
Variousproducttypes $1,203,458 $1,069,602 $697,163
Table6 Observedcountsand
Dataset Good Bad Total Default(%)
defaultrate(HCD)
Training 197,910 17,448 215,258 8.10
Test 84,876 7377 92,253 7.99
haveunderrepresentedtheinterestwhichmightnormallybecollectedoverthelifeofthis
assetclass.
TofurtherdemonstratetherobustnessoftheproposedFPM,weappliedittotheHCDalso
usedinotherstudies,suchasWangetal.(2020).Thisdata,availableonKaggle(Montoya
etal.,2018),highlightsHomeCreditstrivestoexpandfinancialinclusionfortheunbanked
population, featuring a distinct loss structure unlike typical lending portfolios. Since the
HCD encompasses various lending products with different loss dynamics, this introduces
somenoiseintopredictions.However,itcontainsinformationsimilartotheGCD,covering
alargerdatasetof307,501rowsinthefullylabelledsubset.
Forthecomparisonpurpose,weanalysedasingleportfolioconsistingofvariousproduct
typesintheHCDratherthanmultiplesingleassetclasses,usingthesamesimulationapproach
aswiththeGCD.InTable5,weprovidedescriptivestatisticsforthenon-specificportfolio
fromtheHCD.
Table6displaysinformationonthecountsofgood(non-defaulting)andbad(defaulting)
observations,thepercentageofeachoutcomeconditionandtherateofdefaultinthetraining
andtestsplitsoftheHCD.
5.4 Implementation
Thefinaldecisionpriortomodellingwastoeitheroptimisethresholdsaccordingtospecific
modelswhichwouldhaveenhancedrealismyetreducedcomparability,ortoholdthethresh-
old constant at t = 0.5 to focus on the differential capabilities of each algorithm and the
performancemetrics;weoptedforthelatter.Furthermore,whilepreliminarymodeltuning
producedsomesmallincreasesinmodelstatisticalperformance,itcameatthecostofover-
fittingtothetrainingdataset.Thus,asallsixmodelsachievedacceptablystrongperformance
accordingtothestatisticalmetricsonlyminormodeltuningwasperformed.Statisticalmet-
rics were calculated first using automated outputs from R software and then recalculated
manuallyaccordingtotherelevantequations.
5.5 Results
Inthissection,wepresenttheresultsofournumericalexperiments.Westartbycomparing
theperformanceofourproposedcostmetricwiththatofthecommonlyusedapproachby
Bahnsen et al., and noting differences and similarities in model ranking between the two
approaches.
123

AnnalsofOperationsResearch
Table7 FalsepredictioncostsusingBahnsen’sapproach(CSEDCM)asapercentageofproposedcostmetric
(FPM),Eq.(3)
| Threshold(cost) | Methods | CC(%) | SL(%) | Mo(%) | LL/SME(%) |
| --------------- | ------- | ----- | ----- | ----- | --------- |
| Default         | MLP     | 1.04  | 7.67  | 7.10  | 8.09      |
|                 |         | 1.29  | 8.20  | 8.50  | 11.34     |
| Default         | DTR     |       |       |       |           |
| Default         | GBM     | 1.02  | 7.05  | 7.63  | 9.14      |
|                 |         | 1.21  | 9.77  | 7.20  | 10.76     |
| Default         | LR      |       |       |       |           |
| Default         | RF      | 1.20  | 8.98  | 8.21  | 13.87     |
|                 |         | 1.28  | 5.74  | 11.22 | 15.51     |
| Default         | SVM     |       |       |       |           |
| Opportunity     | MLP     | 30.72 | 43.43 | 38.09 | 40.50     |
| Opportunity     | DTR     | 41.15 | 43.50 | 33.34 | 35.01     |
| Opportunity     | GBM     | 25.56 | 45.47 | 31.16 | 38.96     |
| Opportunity     | LR      | 30.91 | 49.62 | 44.61 | 46.39     |
|                 |         | 31.74 | 44.61 | 39.45 | 22.33     |
| Opportunity     | RF      |       |       |       |           |
| Opportunity     | SVM     | 29.88 | 14.06 | 29.94 | 45.09     |
|                 |         | 17.30 | 33.63 | 29.61 | 30.87     |
| Overall         | MLP     |       |       |       |           |
| Overall         | DTR     | 19.26 | 27.54 | 21.59 | 24.11     |
| Overall         | GBM     | 13.48 | 33.08 | 22.40 | 27.65     |
| Overall         | LR      | 13.62 | 35.54 | 30.01 | 32.63     |
| Overall         | RF      | 11.70 | 26.39 | 22.56 | 17.21     |
|                 |         | 21.51 | 10.95 | 24.61 | 39.91     |
| Overall         | SVM     |       |       |       |           |
We calculated the cost of false predictions using both the proposed FPM and that put
forwardbytheCSEDCM.NotingthatallofCSEDCM’scostestimatesweresmallerthan
theFPM,wethencalculatedthepercentageforeachmodelandthresholdpositionusingthe
followingequation:
CSEDCM
|     | Cost%= |     | ×100. |     |     |
| --- | ------ | --- | ----- | --- | --- |
(3)
FPM
InTable7,wereporttheresultsobtainedusingthisequation.Thefirsttwocolumnsin
this table are the cost types and the six algorithms used in our comparison, and the last
four columns are the simulated asset classes. The results show that Bahnsen’s approach
routinelyunderestimatesthetruecostsoffalsepredictions,withunderpredictionsometimes
asdifferentasonehundredthoftheproposedFPM.Forexample,inestimatingthedefault
costoffalsepredictionfortheGBM,Bahnsen’sestimatewasjust1.02%oftheFPM.
The huge disparity in false prediction costs drastically increases the likelihood for
inadvertentlyselectingthewrongmodelunderthebeliefitpresentsthelowestcostofmisclas-
sification.We’vefurtherenhancedthemodelselectionprocessbydemonstratingperformance
measurementdifferentialsoneithersidesofthedecisionboundary,whereasmostindustry
practitionersaswellasresearchersconsideronlytheoverallview,andthatisusuallydone
comparing averaged statistical metrics such as Gini and AUC. Based on the cost of false
predictionestimatedbytheCSEDCMcomparedtothecostoffalsepredictionestimatedby
theFPMfromthistable,wewillutiliseourproposedcostmetricFPMforfurtheranalysis.
IftheproposedFPMisutilizedtoestimatethecostoffalseprediction(theresultspresented
in Table 8), the MLP demonstrates the lowest misclassification costs across all four asset
classes(CC,$17.4m;SL,$42.2m;Mo,$260.7m;LL/SME,$488.7m),andisthereforethe
123

AnnalsofOperationsResearch
bestperformingmodel.Bycontrast,iftheCSEDCMwasusedformodelselection,theRF
wouldbeselectedfortheCC($2.6m)andLL/SME($91.8m)assetclassesandtheSVMfor
smallloans($5.1m)andDTRformortgages($72.1m).Interestingly,whenwepeelbackthe
covertoexamineperformanceoneithersideofthedecisionboundary,bothcostapproaches
favortheMLPfordefaultcost,andRFperformsbestforopportunitycost,yettheconsiderable
differencesinthemagnitudeoffalsepredictioncostsresultindifferencesattheaggregate
level across the decision boundary, which is the level at which the CSEDCM approach
operatesat.
Now,wediscussthecomparisonbetweeneachrespectivemethodaccordingtothefinancial
cost of losses calculated on false predictions. The losses associated with false negatives
(applicantsthemodelpredictsasgoodbutwholaterdefault;thedefaultcost),aswellasfalse
positives(applicantsthemodelpredictsasbadyetwhodonotdefault;theopportunitycostand
mostlycomprisetheinterestrevenueforegonebyrejectinganotherwisegoodapplicant),are
included.Separatingobservationsintofalsepositivesversusfalsenegativesrequiredsplitting
thesampleaboveandbelowthethresholdwhichenhancedcomparisonswiththestatistical
metrics.
Thecomparisonresults,thecostsassociatedwithindividualcomponentsandtheoverall
FPM,areprovidedinTable8.The‘Above’columnrepresentsfalsepositivemisclassifica-
tioncosts,incurredwhenthemodelincorrectlyclassifiesindividualsasdefaulterswhodid
not default. The ‘Below’ column captures false negative misclassification costs, summing
the losses from applicants classified as low risk but who ultimately defaulted. Finally, the
‘Overall’columnrepresentsthetotalmisclassificationcosts,combiningbothfalsepositives
andfalsenegatives,comprisingtheproposedmetric.
Next, we provide the results of the classical statistical performance metrics in Table 9,
wherethefirsttwocolumnsshowthesixmethodsusedandthethresholdsplit,andthelast
threecolumnsarethestatisticalmetrics.Typicallytheseareonlypresentedattheoveralllevel,
which is effectively an average across all observations, however we additionally estimate
performancemeasuresaboveandbelowthethreshold.Splittingtheperformancemetricsin
thismannerprovidesfurtherinsightintoeachmethodandhowtheyperformoneitherside
ofthedecisionthresholdaswellasthemeasurementsthemselves.
TheresultsfromTable9showthatwhenwerankeachalgorithmbystatisticalperformance
seeking to identify the best method, we see that the method rankings are very different
comparingeithersideofthethresholdwithoverall.Forexample,GinishowsthattheGBM
performedbestabovethethresholdwhiletheLRwassuperiorbelow,yetitwastheMLP
thatcameoutontopaccordingtothismetric.
Further, the Gini and AUC result in identical rankings, reinforcing the notion that the
practiseofpresentingbothmetricstogetherisredundant.Bycontrast,theaccuracyofmethods
almostalwaysranksmethodsdifferentlytoGini/AUC,reflectingthedifferentphilosophyin
takingtheproportionoftruepredictionsfromallpredictions,versusdiscriminatingbetween
goodsandbadsusingthenumberofconcordantpairs.
The routine use of these statistical metrics in isolation is problematic because as has
already been established, while they may be useful in distinguishing between a good and
a bad model, they are not useful for making selections between good models. Moreover,
theydonotprovideinsightontherealparameterofinterestwhichisminimisingthefalse
predictions,inparticulartheircostinacreditscoringenvironment.Furthermore,‘overall’
estimateseffectivelyaverageacrossthedecisionboundarythusobscuringimportantdetails
ofmodelperformance.
Wenotethatwhenusedinthetraditionalmannerassessingstatisticalperformanceoverall,
theMLPwastheclearwinneroverall,yetonlymarginallystrongerthantheLR.Themarginal
123

AnnalsofOperationsResearch
Table8 Financialcostmetrics
|     | Method Assets | Above | Below | Overall |
| --- | ------------- | ----- | ----- | ------- |
(per$1000)bymethods,asset
| classandthresholdusingtest | DTR CC | $11,233 | $13,686 | $24,919 |
| -------------------------- | ------ | ------- | ------- | ------- |
dataset(GCD)
|     |     | $10,656 | $10,335 | $20,991 |
| --- | --- | ------- | ------- | ------- |
GBM CC
|     | LR CC | $8134 | $11,337 | $19,471 |
| --- | ----- | ----- | ------- | ------- |
$17,423
|     | MLP CC | $9541   | $7882   |         |
| --- | ------ | ------- | ------- | ------- |
|     | RF CC  | $7749   | $14,784 | $22,533 |
|     | SVM CC | $13,662 | $5652   | $19,314 |
|     |        | $30,664 | $25,311 | $55,975 |
DTR SL
|     | GBM SL | $38,119 | $18,163 | $56,283 |
| --- | ------ | ------- | ------- | ------- |
|     |        | $29,245 | $15,973 | $45,218 |
LR SL
|     | MLP SL | $30,607 | $11,557 | $42,164 |
| --- | ------ | ------- | ------- | ------- |
|     |        | $25,031 | $26,199 | $51,230 |
RF SL
|     | SVM SL | $29,145  | $17,368  | $46,513  |
| --- | ------ | -------- | -------- | -------- |
|     | DTR Mo | $176,080 | $158,013 | $334,093 |
|     | GBM Mo | $204,541 | $121,299 | $325,840 |
|     | LR Mo  | $180,241 | $115,443 | $295,684 |
|     |        | $189,427 | $71,316  | $260,743 |
MLP Mo
|     | RF Mo | $155,153 | $182,587 | $337,741 |
| --- | ----- | -------- | -------- | -------- |
|     |       | $242,131 | $96,377  | $338,508 |
SVM Mo
|     | DTR LL/SME | $314,838 | $268,673 | $583,511 |
| --- | ---------- | -------- | -------- | -------- |
|     |            | $402,095 | $245,552 | $647,647 |
GBM LL/SME
|     | LR LL/SME  | $324,782 | $204,305 | $529,087 |
| --- | ---------- | -------- | -------- | -------- |
|     | MLP LL/SME | $343,546 | $145,248 | $488,795 |
|     | RF LL/SME  | $210,919 | $322,532 | $533,451 |
|     | SVM LL/SME | $537,818 | $114,113 | $651,931 |
statisticalimprovementobtainedfromtheMLPwouldusuallybediscardedinfavourofthe
simplerandmoreeasilyimplementedandunderstoodLR.Indeed,whenusedinconjunction
withtheFPM,thetruecostofselectiondecisionscanbeeasilyunderstood.
In addition, the differential performance on either side of the threshold provides some
insightintohoweachalgorithmworks,and,whereeachperformsstrongest.Forinstance,it
isnotablethataccordingtoACCtheSVMperformedamongstthebestbelowthethreshold,
yet it was also the worst above the threshold. The observed variation in method ranking
betweenmodelmetricsunderscoresthenotionthatusingtraditionalperformancemeasures
blindlyresultsinsuboptimalmethodselections.Certainlyaveragingmetricsacrossthedeci-
sionboundaryobscuresimportantdetailsonperformance.Thus,thetraditionalperformance
measurespresentchallengesformethodselectionandmustbeusedwithcaution.
Fromtheresults,anotableobservationsupportsthefindingsbyVerbrakenetal.(2015),
whereby the larger the magnitude of the principal loan amount, the more important that
opportunity costs become. Given the scale of the largest asset class we simulated and the
consequentmagnitudeofinterestrevenuethatwouldbelost,ourfindingsshowthatforthese
dataopportunitycostsarelargerthandefaultcosts.Thedisparitybetweenopportunityand
defaultcostislargestwheretheinitialexposureissmallest,inthecreditcardassetclass,and
diminishesastheaveragesizeoftheassetclassincreases.Thissuggeststhatthelargerthe
123

AnnalsofOperationsResearch
Table9 Statisticalmetricsby
|     | Method | Threshold | Gini ACC | AUC |
| --- | ------ | --------- | -------- | --- |
thresholdandmethodsusingtest
| dataset(GCD) | MLP | Above   | 0.3273 0.7835 | 0.6636 |
| ------------ | --- | ------- | ------------- | ------ |
|              |     |         | 0.3906 0.7619 | 0.6953 |
|              | DTR | Above   |               |        |
|              | GBM | Above   | 0.4131 0.7553 | 0.7065 |
|              |     |         | 0.3681 0.8046 | 0.684  |
|              | LR  | Above   |               |        |
|              | RF  | Above   | 0.3279 0.7922 | 0.6639 |
|              | SVM | Above   | 0.3628 0.71   | 0.6814 |
|              |     |         | 0.8358 0.9319 | 0.9179 |
|              | MLP | Below   |               |        |
|              | DTR | Below   | 0.8224 0.8725 | 0.9112 |
|              |     |         | 0.8224 0.8969 | 0.9112 |
|              | GBM | Below   |               |        |
|              | LR  | Below   | 0.8558 0.9005 | 0.9279 |
|              |     |         | 0.8014 0.8863 | 0.9007 |
|              | RF  | Below   |               |        |
|              | SVM | Below   | 0.7682 0.9198 | 0.8841 |
|              | MLP | Overall | 0.8914 0.8819 | 0.9457 |
|              | DTR | Overall | 0.8517 0.8403 | 0.9259 |
|              | GBM | Overall | 0.8561 0.8507 | 0.9281 |
|              |     |         | 0.8903 0.8715 | 0.9452 |
|              | LR  | Overall |               |        |
|              | RF  | Overall | 0.8523 0.8611 | 0.9262 |
|              |     |         | 0.8392 0.8467 | 0.9196 |
|              | SVM | Overall |               |        |
creditcontract,themorecarefullendersmustbetoavoidmisclassifyingagoodcreditrisk
asbad.
However,thisisinalimitedsampleof1000customers,whereasinarealcreditportfo-
lio products like CC and SL customers may number in their millions. While our findings
supportthenotionthatopportunitycostsbecomeincreasinglyimportantthelargertheprin-
ciple.However,giventhevolumeoflowvaluelendingproductslikeCCthismaynothold,
particularlyinunsecuredlendinginwhichtheLGDtendstobesignificantlyhigher.
From a method selection perspective, the algorithm resulting in the smallest loss was
thewinner,inlinewiththeprofit-basedmotivewhichcharacterisescommercialenterprise.
Results show that the RF posed the lowest misclassification cost across all asset classes
relatedtofalsepositives,thatisforapplicantsthatthemodelhasscoredabovethedecision
thresholdwhodonotdefault.Bycontrast,theSVMposedthelowestmisclassificationcosts
fortwoassetclasses(CCandLL).TheMLPmisclassificationcostwaslowestforSLand
Moforapplicantswhothemethodapproves,thatisapplicantswhoscorebelowthedecision
threshold,yetwholaterdefault.Overall,theMLPperformedthebestacrossallfourasset
classes.
We conclude by discussing the power curve that is used to empirically determine the
statisticalpowerinourtrainingsample.Moreprecisely,thecurveisproducedtodetermine
whethertheGCDprovidesadequatestatisticalpowerwithwhichtomakeinferencesabout
modelperformance.Whilehypothesistestingisonlyafeatureofstatisticalmodelling,and
therefore,onlyrelatestotheLRalgorithm,itisinstructiveforcomparisonpurposeswiththe
othermethodsinvestigated.Notethatthestatisticalpowerwascalculatedusingtwoassumed
target variable probabilities, the required inputs for this calculation. However, under both
probabilityassumptions,thestatisticalpowerapproached100%priortothetrainingsample
reaching700.Thus,thepowercurvedemonstratesthatthetrainingsampleselectedatrandom
123

AnnalsofOperationsResearch
Fig.1 Samplesizepowercurveforclassification
from the GCD was sufficiently large to provide adequate statistical power with which to
estimateoneormoreparametersusingLR.Figure1depictstheresultsofthepoweranalysis.
Furthermore,asmachinelearningalgorithmsdonotformallyperformhypothesistesting
asstatisticalmodelsdo,truepoweranalysisisnotpossible.Instead,wecalculatetheerror
ofpredictionoverarangeoftrainingsamplesizestotestwhetherthesamplesizeusedwas
largeenough.Thedeterminationoftheadequacyofthesizewasmadebyobservingwhether
theerrorratewasstilldecliningasthetrainingsamplegrew,orwhetheritflattenedout.Each
modelwastestedoneachofninetrainingsamplesextractedfromtheGCDranginginsize
from100to900.Aftereachsubsetwasextractedtoformthetrainingdata,theremaining
proportioncomprisedthetestdata.Thus,wherethetrainingdatasetwas100,thetestdataset
was900;wherethetrainingdatasetwas200,thetestdatasetwas800,andsoonuntilthe
maximum split whereby the training dataset was 900 and the test dataset was 100. The
samplesizeversuserrorratechartsforallsixmethodsareshowninFigs.2,3,4,5,6and7,
respectively.NotethatinFig.1,thepowergreaterthan0.8isgenerallyconsideredacceptable,
whileforFigs.2,3,4,5,6and7thelowertheerrorratethebetterqualitythemethod.
Inearlymethodtesting,modeltuningappearedtoimprovethefittothetrainingdataset
yetreducedperformanceonthetestdata.Thus,tominimiseoverfittingtothetrainingdataset
onlybasicmodeltuningwasperformed.Thesamplesizebyerrorplotsforeachrespective
modelrevealsthatthetrainingandtestdatasetsachievedsimilarperformanceirrespective
ofsamplesize,withonlythesmallesttrainingsamplesizeof100(test=900)resultingina
maximumerrorofpredictionapproaching0.2.
ThetwomethodswhichshowedelevatederrorratesweretheGBMandtheSVM.Contrary
totheconvergingperformancebetweentrainingandtestdatasetsobservedfortheotherfour
methods,theerrorofpredictionforthesemethodsweresubstantiallylargerforthetestdataset
irrespectiveofitsrelativesizeincomparisontothetrainingdata.Forexample,fortheGBM
there is at least a 10% difference in performance even when the training data was at its
maximumof900.
Whileperformanceneverconvergesacrossanysamplesizeitisnoteworthythattheerror
rateinthetestdataisgenerallydecliningforboththeGBMandtheSVMasthesizeofthe
123

AnnalsofOperationsResearch
Fig.2 LRsamplesizeversuserrorrate
Fig.3 RFsamplesizeversuserrorrate
trainingdatasetincreases,andrelativelyflatfortheotherfourmethods.Whileperformance
may have continued to improve if the training sample was even larger, it implies that the
GBMandtheSVMmayrequirelargertrainingdatasetstocontroltheerrorintestdata.An
alternativeinterpretationisthattheGBMandtheSVMformulationsdidnotgeneraliseto
thisspecificdatasetaswellastheotheralgorithms.
Similar levels of the performance for both test and training datasets were observed for
LR,RF,MLPandDTR,yetfortheGBMtheactualmagnitudeofdifferenceinerrorwas
onlyaround0.1bythetimetrainingdatawasaround700,androughly0.06fortheSVM.
Takentogethertheseresultssupportthenotionthatthetrainingdatasetwassufficientlylarge
toproducereliableresultsforallalgorithmstested.
123

AnnalsofOperationsResearch
Fig.4 GBMsamplesizeversuserrorrate
Fig.5 MLPsamplesizeversuserrorrate
Asmentionedearlier,weusedtheHCDwithasingleportfolioofvariousproducttypes
tofurtherdemonstratetherobustnessoftheFPM.
Table10presentsmodelperformanceontheHCDincludingastatisticalaccuracymetric
andthedifferencefromtheLRalgorithmforreference.Usingaclassicalstatisticalperfor-
manceapproach,SVMwouldtypicallybechosen.However,theaccuracydifferencesamong
the six algorithms are trivial. In contrast, the financial losses from false predictions in the
FPMrevealssignificantdifferencesacrossalgorithms.Thisisconsistentwiththeobserva-
tionsfortheGCD.TheFPMidentifiedRFasthebest-performingmodel,closelyfollowedby
theMLP.TheresultsalsoindicatethatutilizingtheFPMwouldachieveasignificantsaving
ofapproximately$321millionand$297millionovertheLR,respectively.
123

AnnalsofOperationsResearch
Fig.6 DTRsamplesizeversuserrorrate
Fig.7 SVMsamplesizeversuserrorrate
Table10 Financialcostmetrics(per$1000)bymethodsusingtestdatasetHCD
| Method | Accuracy | Above    | Below    | Overall  | DifferfromLR |
| ------ | -------- | -------- | -------- | -------- | ------------ |
| DTR    | 0.9197   | $353,830 | $635,740 | $989,570 | −$198,240    |
−$17,970
| GBM | 0.9201 | $310,680 | $498,620 | $809,300 |          |
| --- | ------ | -------- | -------- | -------- | -------- |
| LR  | 0.9200 | $318,150 | $473,180 | $791,330 | –        |
| MLP | 0.9200 | $204,900 | $289,330 | $494,230 | $297,100 |
| RF  | 0.9200 | $138,990 | $330,380 | $469,370 | $321,960 |
| SVM | 0.9155 | $185,810 | $316,250 | $502,060 | $289,270 |
123

AnnalsofOperationsResearch
6 Discussionandconclusion
In this section, we provide discussion on the results presented in this paper and conclude
withfutureresearchdirections.
Publiclyavailabledatasetsenableindustrypractitionerstoemulatetheresultsachieved
inpublishedliteraturemoreeasily,thusexpeditingtheuptakeofnewresearch.Thisstudy
showsthatevenrelativelysmall,publiclyavailabledatasetsliketheGCDandtheHCDare
not only large enough to provide sufficient statistical power with which to train statistical
modelsbutalsotominimisetheerrorofpredictionarisingfromtheapplicationofmachine
learningalgorithmsontrainingsamplesanywhereabove100observations.
Moreover,wedemonstratedthatwherenecessaryfinancialinformationisnotavailable,it
canbesimulatedtoprovideinsightsoncostdynamicsasaconsiderationinmodelselection
particularlywherethesearecalibratedtoreallendingportfolios.Whileourcostdynamicsare
estimatedonsimulateddata,theresultsfromtestsonstatisticalpoweranderrorofprediction
show that these samples are sufficiently large to avoid sampling bias and therefore, make
inferencesonfinanciallosses.
Furthermore, by splitting results on either side of the decision threshold, we showed
howmodelperformancediffersaccordingtowhichalgorithmhasbeenused,thusproviding
additionalinsightsintoalgorithmselectionandperformancemetricsalike.Themodelranking
accordingtotheclassicalperformancemetricsvariedgreatlywhensplitinthismanner.
Thepresentstudyhasfocusedonindividualalgorithms.However,asmodelperformance
andrankingwerehighlyvariableoneithersideofthedecisionboundary,astackingapproach
maywelloutperformsinglealgorithms.Bycombiningthestrengthsofalgorithmsoneither
sideofthethresholditmaybepossibletoeliminateoratleastmitigatetheirweaknessesto
developastrongeroverallpredictionsystem.
Inaddition,buildingonpreviousresearch,wehavesoughttoproposethemostrealistic
estimatesoffalsepredictioncostsyet.Althoughweutilisedrelativelysmalldatasetsoffew
observations,theproposedFPMcouldbeextendedandappliedtolargerlendingportfolios
whichcouldpotentiallyprovideasignificantfinancialbenefittoorganizations.
Taking the example of the mortgage asset class, the best performing algorithm overall
was,forexample,theMLPintheGCD,andselectingthatoverthenextbestalgorithm(LR)
resultedinabenefitofapproximately35milliononadatasetof<300applicants.Whilethis
is a large enough difference to be meaningful in selecting the most fit-for-purpose model,
areal-lifemortgageportfoliocouldeasilybeathousandtimeslarger.Applyingtheratioof
1:1000putsthevalueofselectingMLPoverLRat$35Billion,amassivefinancialbenefit
foreventhelargestcorporationstradingonaglobalscale.
Furthermore,wehavenotedtheextantissueswiththethreemostpopularperformance
metrics, AUC, Gini, and ACC. Prior research suggests these measures are unsuitable for
modelselection.Forexample,althoughAUCmaybeabletodifferentiateagoodmodelfrom
abadoneitisunabletodistinguishbetweengoodones.Whileitiscoherentatseparatingclass
membership,itisalsoincoherentonthecostsofthoseclasses,andtheactuallossresulting
from false predictions. Although these incoherent approaches may be useful as a hurdle
todifferentiatebetweengoodandbadcandidatemodels,thefinanciallossshouldbeused
foridentifyingthebestperformer.Therefore,weproposeanoptimalsystemwherebyonce
candidate models achieve a minimum performance threshold, the financial loss measures
shouldbeusedtoselectthebest-performingmodel.
UsingtheproposedFinancialPerformanceMetric(FPM)enablesindustrypractitioners
toselectmodelswhichbestalignwiththeirmotivesforusingthemodelsinthefirstplacefor
123

AnnalsofOperationsResearch
profit.Asitisdemonstratedhereinforcreditscorecards,thesameprinciplescanbeapplied
to any commercial application of classification models in which the loss function is more
nuancedthansimplyseparatinggoodsandbads.
Mostofthepublishedcreditmodellingresearchfocusesonapplicationscorecards,never-
theless,theyarenotthemostmaterialmodelsusedbybanksglobally.Futureresearchshould
deeplyexaminebehavioralmodelswhichmeasuretheongoingriskonceapplicantsbecome
customers.Bothpointintime,aswellasthroughtheeconomiccyclemodelsareimportant
considerationsrequiredbyprudentialauthorities.Thesemodelshaveahugeimpactonnot
onlyretainedsolvencycapital,butalsotheoverallhealthofthefinancialsystem.Wetested
ourfindingsonacomparisondataset,butfurthertestingincludingreplacingsimulatedvari-
ableswithreal-timemeasurementsmayservetounderscorethevalueofusingthefinancial
performance metric. Lastly, there is a dearth of published research on optimal monitoring
solutionsforcreditmodelsovertime,whichisanurgentpriorityforindustry.
Funding OpenAccessfundingenabledandorganizedbyCAULanditsMemberInstitutionsThisresearch
receivednoexternalfunding.
Declarations
Conflictofinterest Theauthorsdeclarethattheyhavenoknowncompetingfinancialinterestsorpersonal
relationshipsthatcouldhaveappearedtoinfluencetheworkreportedinthispaper.
Ethicalapproval Thisarticledoesnotcontainanystudieswithhumanparticipantsoranimalsperformedby
anyoftheauthors.
OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permitsuse,sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicence,
andindicateifchangesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincludedinthe
article’sCreativeCommonslicence,unlessindicatedotherwiseinacreditlinetothematerial.Ifmaterialis
notincludedinthearticle’sCreativeCommonslicenceandyourintendeduseisnotpermittedbystatutory
regulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfromthecopyrightholder.
Toviewacopyofthislicence,visithttp://creativecommons.org/licenses/by/4.0/.
References
Aodha,O.M.,&Brostow,G.J.(2013).Revisitingexampledependentcostsensitivelearningwithdecision
trees.In2013IEEEinternationalconferenceoncomputervision(pp.193–200).Washington,DC,USA.
Assadsolimani,M.&Chetalova,D.(2017).EstimatingVaRincreditrisk:Aggregatevssinglelossdistribution.
AustralianBureauofStatistics.(September2024).LendingIndicators,ABSWebsite.Accessed10December
2024.
Bahnsen,A.C.,Aouada,D.,&Ottersten,B.(2014).Example-dependentcost-sensitivelogisticregressionfor
creditscoring.In13thinternationalconferenceonmachinelearningandapplications(pp.263–269).
https://doi.org/10.1109/ICMLA.2014.48
Bahnsen,A.C.,Aouada,D.,&Ottersten,B.(2015).Example-dependentcost-sensitivedecisiontrees.Expert
SystemswithApplications,42(19),6609–6619.https://doi.org/10.1016/j.eswa.2015.04.042
BankofEngland.(November2024).MoneyandLending,BankofEnglandwebsite.Accessed10December
2024.
Banu,I.M.(2013).Theimpactofcreditoneconomicgrowthintheglobalcrisiscontext.ProcediaEconomics
andFinance,6,25–30.
Baum,E.(1988).Onthecapacityofmultilayerperceptron.JournalofComplexity,4,193–215.
Bequé,A.,Coussement,K.,Gayler,R.,&Lessmann,S.(2017).Approachesforcreditscorecardcalibration:
Anempiricalanalysis.Knowledge-BasedSystems,134,213–227.
Breiman,L.(2001).Randomforests.MachineLearning,45,5–32.https://doi.org/10.1023/A:1010933404324
123

AnnalsofOperationsResearch
Cantrell,B.W.,McInnis,J.M.,&Yust,C.G.(2014).Predictingcreditlosses:Loanfairvaluesversushistorical
costs.TheAccountingReview,89(1),147–176.https://doi.org/10.2308/accr-50593
Dmitriev,P.,&Wu,X.(2016).Measuringmetrics.InProceedingsofthe25thACMinternationalonconference
oninformationandknowledgemanagement(CIKM’16).AssociationforComputingMachinery,New
York,NY,USA(pp.429–437).https://doi.org/10.1145/2983323.2983356
Dong,G.,Lai,K.K.,&Yen,J.(2010).Creditscorecardbasedonlogisticregressionwithrandomcoefficients.
ProcediaComputerScience,1(1),2463–2468.
Dua,D.,&Graff,C.(2019).UCImachinelearningrepository.SchoolofInformationandComputerScience,
UniversityofCalifornia,Irvine,CA.https://archive.ics.uci.edu/ml/datasets
Dumitrescu,E.,Hué,S.,Hurlin,C.,&Tokpavi,S.(2022).Machinelearningforcreditscoring:Improving
logisticregressionwithnon-lineardecision-treeeffects.EuropeanJournalofOperationalResearch,
297(3),1178–1192.https://doi.org/10.1016/j.ejor.2021.06.053
Elkan,C.(2001).Thefoundationsofcost-sensitivelearning.InSeventeenthinternationaljointconferenceon
artificialintelligence(pp.973-978).
Finlay,S.(2009).Consumercreditfundamentals(2nded.).PalgraveMacMillan.
Fiore,U.,DeSantis,A.,Perla,F.,Zanetti,P.,&Palmieri,F.(2017).Usinggenerativeadversarialnetworksfor
improvingclassificationeffectivenessincreditcardfrauddetection.InformationSciences,479,448–455.
https://doi.org/10.1016/j.ins.2017.12.030
Friedman,J.H.(2001).Greedyfunctionapproximation:Agradientboostingmachine.AnnalsofStatistics,
29(5),1189–1232.
Gea-Carrasco, C. (2015). IFRS 9 will significantly impact banks’ provisions and financial statements. In
Moody’sanalyticsriskperspectives(Vol.V).
Hand,D.J.(2009).Measuringclassifierperformance:AcoherentalternativetotheareaundertheROCcurve.
MachineLearning,77,103–123.https://doi.org/10.1007/s10994-009-5119-5
Hofmann,H.(1994).Statlog(GermanCreditData)[Dataset].UCImachinelearningrepository.https://doi.
org/10.24432/C5NC77
IASB.(2014).IFRSstandard9:Financialinstruments,InternationalAccountingStandardsBoard.
Khashman,A.(2010).Neuralnetworksforcreditriskevaluation:Investigationofdifferentneuralmodelsand
learningschemes.ExpertSystemswithApplications,37(9),6233–6239.
Lessmann,S.,Baesens,B.,Seow,H.V.,&Thomas,L.C.(2015).Benchmarkingstate-of-the-artclassification
algorithmsforcreditscoring:Anupdateofresearch.EuropeanJournalofOperationalResearch,247(1),
124–136.https://doi.org/10.1016/j.ejor.2015.05.030
Liu,Y.,Zhou,Y.,Wen,S.,&Tang,C.(2014).Astrategyonselectingperformancemetricsforclassifier
evaluation. International Journal of Mobile Computing and Multimedia Communications, 6, 20–35.
https://doi.org/10.4018/IJMCMC.2014100102
Mahbobi,M.,Kimiagari,S.,&Vasudevan,M.(2023).Creditriskclassification:Anintegratedpredictive
accuracyalgorithmusingartificialanddeepneuralnetworks.AnnalsofOperationsResearch,330(1),
609–37.
Maldonado,S.,Bravo,C.,López,J.,&Pérez,J.(2017).Integratedframeworkforprofit-basedfeatureselection
andSVMclassificationincreditscoring.DecisionSupportSystems,104,113–121.
Martin,J.,Taheri,S.,&Abdollahian,M.(2024).Optimizingensemblelearningtoreducemisclassification
costsincreditriskscorecards.Mathematics,12(6),855.https://doi.org/10.3390/math12060855
Marzban,C.(2004).TheROCcurveandtheareaunderitasperformancemeasures.WeatherandForecasting,
19(6),1106–1114.
Mencia,J.,&Jimenez,G.(2007).Modelingthedistributionofcreditlosseswithobservableandlatentfactors
(April18,2007).InBancodeEspañaResearchPapers.AvailableatSSRN.https://doi.org/10.2139/ssrn.
981109
Montoya,A.,Odintsov,K.,&Kotek.M.(2018).HomeCreditDefaultRisk.https://kaggle.com/competitions/
home-credit-default-risk,Kaggle
Obare,D.M.,&Muraya,M.M.(2018).Comparisonofaccuracyofsupportvectormachinemodelandlogistic
regressionmodelinpredictingindividualloandefaults.AmericanJournalofAppliedMathematicsand
Statistics,6(6),266–271.https://doi.org/10.12691/ajams-6-6-8
Odegua,R.(2020).Predictingbankloandefaultwithextremegradientboosting.
Ostrowski,J.(2024).Averagemortgagedebtin2024,Bankratewebsite.Accessedon10December2024.
Ramezan,C.A.,Warner,T.A.,Maxwell,A.E.,&Price,B.S.(2021).Effectsoftrainingsetsizeonsupervised
machine-learningland-coverclassificationoflarge-areahigh-resolutionremotelysenseddata.Remote
Sensing,13,368.https://doi.org/10.3390/rs13030368
Schebesch,K.,&Stecking,R.(2005).Supportvectormachinesforclassifyinganddescribingcreditapplicants:
Detectingtypicalandcriticalregions.JournalofTheOperationalResearchSociety,56,1082–1088.
https://doi.org/10.1057/palgrave.jors.2602023
123

AnnalsofOperationsResearch
Tripathi,D.,Edla,D.R.,Kuppili,V.,&Bablani,A.(2020).Evolutionaryextremelearningmachinewithnovel
activationfunctionforcreditscoring.EngineeringApplicationsofArtificialIntelligence,96,103980.
Teles,G.,Rodrigues,J.J.P.C.,Rabêlo,R.A.L.,&Kozlov,S.A.(2021).Comparativestudyofsupportvector
machinesandrandomforestsmachinelearningalgorithmsoncreditoperation.Software:Practiceand
Experience,51,2492–2500.https://doi.org/10.1002/spe.2842
Thomas,L.C.,Edelman,D.B.,&Crook,J.N.(2002).Creditscoringanditsapplications.Philadelphia:
SIAMMonographsonMathematicalModelingandComputation.
Tian,Z.,Xiao,J.,Feng,H.,&Wei,Y.(2020).Creditriskassessmentbasedongradientboostingdecisiontree.
ProcediaComputerScience,174,150–160.https://doi.org/10.1016/j.procs.2020.06.070
Vapnik,V.(1996).Thenatureofstatisticallearningtheory.Springer.
Verbraken,T.,Bravo,C.,Weber,R.,&Baesens,B.(2014).Developmentandapplicationofconsumercredit
scoringmodelsusingprofit-basedclassificationmeasures.EuropeanJournalofOperationalResearch,
238(2),505–513.https://doi.org/10.1016/j.ejor.2014.04.001
Wang,C.,Deng,C.,&Wang,S.(2020).Imbalance-XGBoost:Leveragingweightedandfocallossesforbinary
label-imbalancedclassificationwithXGBoost.PatternRecognitionLetters,136,190–197.https://doi.
org/10.1016/j.patrec.2020.05.035
Wang,H.,Kou,G.,&Peng,Y.(2021).Multi-classmisclassificationcostmatrixforcreditratingsinpeer-
to-peerlending.JournaloftheOperationalResearchSociety,72(4),923–934.https://doi.org/10.1080/
01605682.2019.1705193
Xia,Y.,Liu,C.,&Liu,N.(2017).Cost-sensitiveboostedtreeforloanevaluationinpeer-to-peerlending.
ElectronicCommerceResearchandApplications,24,30–49.https://doi.org/10.1016/j.elerap.2017.06.
004
Yhip,T.M.,&Alagheband,B.M.D.(2017).Thepracticeoflending.PalgraveMacmillan.https://doi.org/
10.1007/978-3-030-32197-0
Zhang,T.,Zhang,W.,Xu,W.,&Hao,H.(2018).Multipleinstancelearningforcreditriskassessmentwith
transactiondata.Knowledge-BasedSystems.https://doi.org/10.1016/j.knosys.2018.07.030
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmapsand
institutionalaffiliations.
123