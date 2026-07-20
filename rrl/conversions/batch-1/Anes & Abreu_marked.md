---
conversion_metadata:
  converted_at: "2026-07-20T14:36:07Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Anes & Abreu.pdf"
  source_pdf_sha256: "6cf9d628d50ee439a48b651c0f39ccb07de0c2caa9854540434b2b8bca38fc50"
  page_count: 21
  markdown_char_count: 74585
---

Article
Adaptive Cluster-Based Normalization for Robust TOPSIS in
Multicriteria Decision-Making
VitorAnes1,2,* andAntónioAbreu2,3
1 IDMEC,InstitutoSuperiordeEngenhariadeLisboa,InstitutoPolitécnicodeLisboa,1959-007Lisbon,Portugal
2 UnitforInnovationandResearchinEngineering,PolytechnicUniversityofLisbon,1959-007Lisbon,Portugal;
antonio.abreu@isel.pt
3 CenterofTechnologyandSystems(UNINOVA-CTS),AssociatedLabofIntelligentSystems(LASI),
2829-516Caparica,Portugal
* Correspondence:vitor.anes@isel.pt
Abstract: Inmulticriteriadecision-making(MCDM),methodssuchasTOPSISareessential
forevaluatingandcomparingalternativesacrossmultiplecriteria. However,traditional
normalizationtechniquesoftenstrugglewithdatasetscontainingoutliers,largevariances,
orheterogeneousmeasurementunits,whichcanleadtoskewedorbiasedrankings. To
addressthesechallenges,thispaperproposesanadaptive, cluster-basednormalization
approach,demonstratedthroughareal-worldlogisticscasestudyinvolvingtheselection
of a host city for an international event. The method groups alternatives into clusters
basedonsimilaritiesincriterionvaluesandapplieslogarithmicnormalizationwithineach
cluster. Thislocalizedstrategyreducestheinfluenceofoutliersandensuresthatscaling
adjustmentsreflectthespecificcharacteristicsofeachgroup.Inthecasestudy—wherecities
wereevaluatedbasedoncost,infrastructure,safety,andaccessibility—thecluster-based
normalizationmethodyieldedmorestableandbalancedrankings,eveninthepresence
ofsignificantdatavariability. Byreducingtheinfluenceofoutliersthroughlogarithmic
normalization and allowing predefined cluster profiles to reflect expert judgment, the
methodimprovesfairnessandadaptability. ThesefeaturesstrengthenTOPSIS’sabilityto
deliveraccurate,balanced,andcontext-awaredecisionsincomplex,real-worldscenarios.
Keywords: TOPSIS;logarithmicnormalization;cluster-basednormalization;multicriteria
decision-making;outliermitigation
AcademicEditor:YimingTang
Received:12February2025
Revised:26March2025
Accepted:2April2025 1. Introduction
Published:7April2025
Multi-criteriadecision-making(MCDM)methodsareessentialforaddressingcomplex
Citation: Anes,V.;Abreu,A.
problemsthatinvolvemultiple,oftenconflicting,factors. Amongthese,theTechniquefor
AdaptiveCluster-Based
OrderofPreferencebySimilaritytoIdealSolution(TOPSIS)iswidelyusedduetoitsability
NormalizationforRobustTOPSISin
toeffectivelyrankalternativesbasedontheirclosenesstoanidealsolution.
MulticriteriaDecision-Making.Appl.
Sci.2025,15,4044. https://doi.org/ ClusteringtechniquesareincreasinglyrelevantinTOPSIS-basedapplicationsbecause
10.3390/app15074044 theyenabledecision-makerstogroupalternativeswithsimilarcharacteristicsbeforeper-
formingtherankingprocedure. Thissegmentationenhancestheinterpretabilityofresults
Copyright:©2025bytheauthors.
LicenseeMDPI,Basel,Switzerland. andallowsformorecontext-sensitivecomparisons. Ratherthanapplyingaone-size-fits-all
Thisarticleisanopenaccessarticle rankingacrossadiversesetofalternatives,clusteringallowseachgrouptobeevaluated
distributedunderthetermsand against a tailored ideal profile, reflecting specific priorities or constraints. In this way,
conditionsoftheCreativeCommons
clusteringnotonlyincreasesadaptabilitytoreal-worldscenariosbutalsoimprovesthe
Attribution(CCBY)license
fairnessandclarityofthefinalrankings.
(https://creativecommons.org/
licenses/by/4.0/).
Appl.Sci.2025,15,4044 https://doi.org/10.3390/app15074044

Appl.Sci.2025,15,4044 2of21
However,despiteitsadvantages,certainchallengesremain—particularlyrelatedto
clusteringandnormalization. Traditionalclusteringmethodstendtoassignalternatives
to fixed categories, even when those alternatives share features with multiple groups.
Thisrigidclassificationcanleadtomisinterpretationandthelossofvaluableinformation,
especiallywhenthedatainvolvesuncertaintyoroverlappingcharacteristics. Likewise,
widelyusednormalizationtechniques—suchasMin–MaxandZ-score—oftenstruggleto
managelargedatavariations,skeweddistributions,andextremevalues,whichcandistort
rankingsandintroducebiasintodecision-making.
Toovercometheselimitations,thisstudyproposestwoinnovativemethodsdesigned
tomaketheTOPSISframeworkmoreflexible,reliable,anduser-friendly. ThefirstisClus-
teringUsingFuzzyNumbersandCentroid-BasedDistanceAllocation,anovelclustering
approachthatincorporatesfuzzynumberstorepresentuncertaintyintheevaluationof
alternatives. UnliketraditionalclusteringmethodssuchasK-Means—whereclustercen-
troidsaredeterminedbasedonthedataofexistingelements—ourapproachdefinesthe
centroidofeachclusterapriori,basedonexpertjudgmentandidealconditionsforeach
criterion. Alternativesarethenevaluatedusingfuzzynumberstoaccountforuncertainty,
andtheirdistancestothepredefinedclustercentroidsarecomputedusingcrispvalues
derived from these fuzzy assessments. This process avoids arbitrary assignments and
providesamorestructured,interpretableclassificationframeworkthatreflectsbothexpert
intentandtheinherentimprecisionofreal-worlddata.
ThesecondinnovationislogarithmicnormalizationinTOPSIS,atransformationtech-
niquethatsmoothsextremevariations,preservesproportionaldifferences,andprevents
anysinglecriterionfromdominatingthefinalrankings. Akeybenefitofthistechniqueis
that,whileitenhancesstabilityandaccuracy,itremainsasstraightforwardtoapplyastradi-
tionalmethodslikeMin–MaxorZ-scorenormalization,makingitapracticalenhancement
fordecision-makers.
By integrating these two methodological advancements, this study improves both
theclusteringandnormalizationcomponentsoftheTOPSISframework,addressingkey
limitationsintraditionalapproacheswhilemaintainingsimplicityandefficiency.
Unlike traditional data-driven clustering algorithms, the proposed method allows
decision-makerstodefineidealclusterprofilesindependentlyofthedataset. Thisdesign,
combinedwiththeuseoffuzzynumberstocaptureevaluationuncertainty,enablesasimple
yetrobustclassificationprocess. Thedeterministicassignmentofalternativesenhances
transparencyandinterpretability,makingtheapproachbothinnovativeandwell-suited
forreal-worlddecision-making.
Designedforbotheaseofimplementationandadaptability,themethodisapplicable
acrossawiderangeofdomains,includingfinance,environmentalassessment,andindus-
trialplanning. Byimprovingthegroupingofalternativesandenablingfairercomparisons
betweencriteria,theproposedapproachoffersamorebalanced,insightful,andscalable
solutionforcomplexdecision-makingproblems.
Thefollowingsectionsprovideadetailedexplanationoftheproposedmethods,their
theoreticalunderpinnings,andtheirpracticalimplementation.
Therestofthispaperisorganizedasfollows: Section2reviewstheexistingliterature
onclusteringandnormalizationinTOPSIS,highlightingtheirstrengthsandlimitations
andidentifyingthegapsthatthisstudyaimstoaddress. Section3outlinestheMaterials
andMethods,providingadetailedexplanationoftheproposedClusteringUsingFuzzy
NumbersandCentroid-BasedDistanceAllocationapproach, aswellasthelogarithmic
normalizationforTOPSIS,alongwiththeirtheoreticalfoundationsandimplementation
process. Section4presentsacasestudy,demonstratinghowthesemethodscanbeapplied
inareal-worlddecision-makingscenario. Section5analyzestheresults,comparingthe

Appl.Sci.2025,15,4044 3of21
proposed techniques with traditional methods to evaluate improvements in accuracy,
robustness,andefficiency. Finally,Section6offerstheconclusion,summarizingthekey
findings, discussing their broader implications, and suggesting possible directions for
futureresearch.
2. LiteratureReview
Multi-criteriadecision-making(MCDM)encompassesasetofmethodologiesusedto
evaluateandprioritizemultiple—oftenconflicting—factorsinthedecision-makingprocess.
Theseapproachesarecriticalinfieldssuchasenvironmentalmanagement,engineering,
andeconomics,wherecomplexdecisionsarefrequentlyencountered[1].
One of the most widely applied MCDM techniques is the Technique for Order of
PreferencebySimilaritytoIdealSolution(TOPSIS).Itscoreprincipleisstraightforward:the
optimalalternativeistheoneclosesttotheidealsolutionandfarthestfromtheworst-case
scenario. TOPSISisparticularlyvaluedforitssimplicityanditsabilitytoeffectivelyhandle
bothqualitativeandquantitativedata[2].
Likeanymethod,however,TOPSIShasitslimitations. Itcanstrugglewithdatasets
characterizedbyuncertainty,outliers,orhighvariance,whichmayaffecttheconsistency
and reliability of its rankings. In response, researchers have explored methods to link
inputuncertaintywithoutputuncertaintywithintheTOPSISframework,highlightingthe
challengesofinterpretinguncertaindatainreal-worlddecision-makingcontexts[3].
Refining these techniques can increase decision-makers’ confidence in the results,
therebyenhancingtheoverallvalueandapplicabilityofMCDMmethodsacrossvarious
industries[4].
ComparativestudieshaveexaminedTOPSISalongsideotherMCDMmethodssuch
as VIKOR, PROMETHEE, and AHP. For instance, one study evaluated four different
techniques—AHP,TOPSIS,ELECTREIII,andPROMETHEEII—inthecontextofgroup
decision-makingforsewernetworkprojects,offeringvaluableinsightsintotheirapplicabil-
ityandeffectiveness[5–7].
Traditionalclusteringmethods—suchasK-MeansandHierarchicalClustering—have
long served as fundamental tools for grouping similar data points in decision-making
models. Theirefficiencyandeaseofimplementationcontributetotheirwidespreaduse.
However,thesemethodshavenotablelimitations,especiallywhendealingwithuncertainty,
complex data distributions, or overlapping classifications. Because they rely on crisp
boundaries, each data point is strictly assigned to a single cluster, which can result in
inaccurate or overly simplistic groupings in real-world scenarios where data are often
ambiguousandmultidimensional[8].
To overcome these limitations, fuzzy clustering techniques—particularly Fuzzy C-
Means(FCM)—offeramoreflexiblealternative. Unliketraditionalclusteringmethods,
FCMallowsdatapointstobelongtomultipleclusterswithvaryingdegreesofmembership,
enablingmorenuancedandadaptableclassifications. Thisapproachisespeciallyvaluable
indomainssuchasmedicaldiagnosis,imagesegmentation,andcustomerprofiling,where
real-worlddatararelyconformstoclearlydefinedcategories[9].
Although FCM enhances clustering accuracy and adaptability, it also introduces
considerablecomputationalcomplexity. IncontrasttoK-Means,whichfollowsarelatively
simpleiterativeprocess,FCMrequiresmoreintensivecalculationsduetothecontinuous
updatingofmembershipprobabilitiesandtheoptimizationofanobjectivefunction. This
iterativeminimizationprocesscanbecomecomputationallyexpensive,particularlywhen
workingwithlarge,high-dimensionaldatasets. Asaresult,FCMincreasesprocessingtime
anddemandsgreatercomputationalresources[10].

Appl.Sci.2025,15,4044 4of21
Anothersignificantbarriertotheadoptionoffuzzyclusteringmethodsistheneedfor
programmingandalgorithmicexpertise. Implementingthesemethods—particularlyin
large-scaleapplications—requiresfamiliaritywithprogramminglanguagessuchasPython
v3,Rv4,orMATLABR2024a,aswellaswithspecializedlibrarieslikescikit-fuzzyorthe
FuzzyLogicToolbox. Unliketraditionalclusteringalgorithms,whichareoftenaccessible
throughbuilt-insoftwaretoolswithminimalcoding,FCMandsimilarapproachesdemand
manualparametertuning(e.g.,selectingtheoptimalfuzzinesscoefficientm)andcareful
datapreprocessingtoproducemeaningfulresults[11].
Additionally,FCMishighlysensitivetoinitialization—poorlyselectedinitialcentroids
canleadtosuboptimalclusteringoutcomes,oftenrequiringadvancedtechniquessuchas
geneticalgorithmsorparticleswarmoptimizationtoenhanceresults. Consequently,while
fuzzyclusteringoffersimprovedaccuracyandflexibility,itspracticalapplicationdemands
greaterexpertise,computationalresources,andalgorithmicfine-tuning[12].
Recentresearchhasfocusedonreducingthecomputationaloverheadassociatedwith
fuzzyclusteringbyexploringhybridmodelsthatcombinedeeplearningandoptimization
algorithms. These models aim to automate parameter selection and improve overall
performance. Suchadvancesseektomakefuzzyclusteringmoreaccessibleandscalable,
bridgingthegapbetweenitstheoreticalstrengthsandpracticalusabilityincomplex,real-
worlddecision-makingscenarios[13].
Normalizationisacriticalstepinmulti-criteriadecision-making(MCDM)processes,
asitensuresthatcriteriameasuredondifferentscalescanbecomparedmeaningfully[14].
Common normalization methods include Min–Max normalization: This method
rescalesdatatoafixedrange,typically[0,1],butissensitivetooutliers,whichcandistort
thenormalizedvalues. Z-Scorenormalization: Thistechniquestandardizesdatabasedon
meanandstandarddeviation,assuminganormaldistribution,whichmaynotholdtrue
foralldatasets. Vectornormalization: OftenusedinTOPSIS,thismethodnormalizesdata
bydividingeachcriterionvaluebytheEuclideannormofthevector. Whileeffective,it
maynotalwayspreserveproportionaldifferencesbetweencriteria.
Theseconventionalnormalizationtechniquesfacechallengeswhenappliedtohighly
skeweddata,extremevalues,ornon-lineardistributions,whichcancompromisethefair-
nessandaccuracyofdecision-makingoutcomes. Forexample,thechoiceofnormalization
methodcansignificantlyinfluencetherankingofalternativesinMCDMprocesses, un-
derscoringtheimportanceofselectinganappropriatetechniqueforeachspecificdecision
context[15,16].
Logarithmictransformationisamathematicaltechniqueusedtohandlenon-linear
data and compress large numerical ranges. By applying a logarithmic function, data
can be transformed to reduce skewness, manage outliers, and stabilize variance. This
transformationpreservesrelativedifferenceswhileminimizingtheinfluenceofextreme
values,makingitusefulinfieldssuchasstatistics,finance,andmachinelearning. Despite
theseadvantages,logarithmicnormalizationremainsunderutilizedinMCDMmethods
likeTOPSIS.IntegratingitintotheTOPSISframeworkcouldimproverankingstability
anddecisionaccuracy—especiallyindatasetscharacterizedbyhighvariance[17]. One
studyintroducedanovellogarithmicnormalizationmethodwithinthecontextofgame
theory,demonstratingitseffectivenessinseparatingnormalizedvaluesmoreefficiently
thanconventionalapproaches. Thesefindingssuggestpromisingapplicationsforsucha
methodinMCDMframeworksaswell[18].
The current literature reveals a lack of studies that combine fuzzy clustering with
centroid-based distance allocation within MCDM frameworks [19,20]. Furthermore, al-
thoughlogarithmicnormalizationoffersclearadvantagesforhandlinghigh-variancedata,
itsapplicationwithinTOPSISandotherMCDMmodelsremainslimited[21].

Appl.Sci.2025,15,4044 5of21
Addressingthesegapspresentsanopportunitytoimprovedecision-makingprocesses
bydevelopingaunifiedframeworkthatintegratesbothtechniques, therebyenhancing
clusteringprecisionandrankingaccuracywithinMCDMapplications[22].
RecentstudieshavealsoexploredtheintegrationofMCDMmethodswithuncertainty
modelinginemergingtechnologicalcontexts. Forinstance,Nabeehetal.[23]proposed
a hybrid model combining the Ordered Weighted Averaging (OWA) operator with the
TOPSISmethodtoevaluatekeyfactorsinfluencingtheproductionofdigitaltwinsbasedon
blockchaintechnology. Theirapproachleveragesneutrosophiclogictomanageuncertainty
inexpertjudgments,offeringastructuredyetflexibledecision-makingframework. While
theapplicationdomaindiffersfromthepresentstudy,bothapproachesshareacommon
goal: enhancing the reliability of TOPSIS in uncertain, multi-criteria environments. In
contrast to neutrosophic sets, our method uses fuzzy numbers exclusively to express
uncertaintyduringtheevaluationphase,followedbycrispclassificationbasedondistance
topredefinedidealcentroids. Thisallowsforimprovedinterpretabilityandcomputational
simplicitywhilemaintainingrobustnessindecisionsupport.
BeyondtheMCDM-andTOPSIS-focusedresearchreviewedhere,advancedstudies
inoptimization,machinelearning,andstatisticalmodelingmayinspirenovelextensions
to fuzzy clustering and logarithmic normalization approaches. Recent works on meta-
learningfornonconvexoptimization[24],few-shotidentificationforstochasticdynamical
systems[25],robustkernel-basedsurrogatemodeling[26],andGaussiankernelsimilar-
ity for multisource information fusion [27] illustrate how sophisticated algorithms can
handlehigh-dimensional,uncertaindata. Relatedeffortsaddressrobuststatisticaltests
forheavy-tailedtimeseries[28],supervisedlearningforcomplextracking[29],adaptive
opiniondynamics[30],andagent-baseddecisionmodelsleveragingdeepreinforcement
learning[31].
Althoughtheseadvancedmethodsofferimpressivecapabilities,theyoftencomewith
increasedcomputationalcomplexityanddemandahighleveloftechnicalexpertisefor
effectiveimplementation. Incontrast,ourgoalistoproposeamorestraightforwardand
practicalapproach,suitableforreal-worldscenarios,thatbalancestheneedtoaddressdata
variabilityanduncertaintywithsimplicityandusability. Nonetheless,thesesophisticated
techniqueshighlightpromisingdirectionsforfutureMCDMresearch,particularlyinthe
integrationofmeta-learning,robustmodeling,andadaptiveinformationfusiontofurther
improveclusteringandnormalizationstrategiesincomplexdecision-makingcontexts.
3. MaterialsandMethods
In this section, we introduce a new methodological approach that enhances both
clusteringandnormalizationwithintheTOPSISframeworkwhileensuringthattheprocess
remainsstraightforwardandeasytoimplement. Theproposedmethods,ClusteringUsing
FuzzyNumbersandCentroid-BasedDistanceAllocation,andtheintegrationoflogarithmic
normalizationinTOPSIS,addresskeylimitationsintraditionaltechniques. Byintroducing
amoreflexibleclusteringprocessandanadaptivenormalizationapproach,thesemethods
allowforamoreaccuraterepresentationofreal-worlddatavariability,improvingdecision-
makingoutcomes.
Oneofthefundamentalchallengesindecisionmodelsisthattraditionalclustering
methodstendtoassignalternativestorigidcategories,evenwhenthedatasuggestsamore
nuancedclassification. Thiscanleadtomisinterpretations,particularlywhendealingwith
uncertaintyoroverlappingdatapoints. Toovercomethislimitation,weproposeClustering
UsingFuzzyNumbersandCentroid-BasedDistanceAllocation,whichintroducesadegree
ofmembershipforeachalternativewithinaclusterinsteadofenforcingastrictassignment.

Appl.Sci.2025,15,4044 6of21
Thismethodacknowledgesthatalternativesmayexhibitcharacteristicsofmultipleclusters,
leadingtoamoreprecise,meaningful,andinterpretablegroupingofdata.
Similarly,conventionalnormalizationtechniquessuchasMin–MaxandZ-scoreoften
fail to handle datasets with large numerical variations, highly skewed distributions, or
extremeoutliers. TheseissuescandistortrankingsinTOPSIS,ascriteriawithsignificantly
largervaluesmaydisproportionatelyinfluencethefinalresults.Toaddressthis,wepropose
theintegrationoflogarithmicnormalizationinTOPSIS,whicheffectivelysmoothsextreme
variations,preservesrelativedifferences,andensuresamorebalancedinfluenceacross
criteria. Oneofitsmostcompellingadvantagesisthat,despiteitseffectivenessinhandling
complexdatadistributions,itremainsaseasytoapplyastraditionalnormalizationmethods,
makingitanaccessibleyetpowerfulenhancementfordecision-makers.
The strength of our proposed methodology lies in its ability to enhance accuracy,
robustness,andadaptabilitywhilemaintainingeaseofimplementation. Boththefuzzy
clusteringapproachandlogarithmicnormalizationaredesignedtoseamlesslyintegrate
intoexistingdecision-makingworkflowswithoutaddingcomputationalcomplexity. By
introducinggreaterflexibilityinclusteringandamoreadaptiveapproachtonormalization,
this study provides a scalable, practical, and efficient framework for improving multi-
criteriadecision-making. Thefollowingsectionsprovideanin-depthexplanationofhow
thesemethodsworkandtheirpracticalapplications.
3.1. ClusteringUsingFuzzyNumbersandCentroid-BasedDistanceAllocation
To group alternatives into meaningful clusters, we implement a fuzzy clustering
approach. Thismethodinvolvesthefollowingsteps:
Step1:Representationofalternativeswithfuzzynumbers—eachalternative’scriteria’s
valuesareconvertedintofuzzynumbers(a, b, c)representingthelowerbound, central
value, andupperbound, respectively. Thisallowsforamoreflexiblerepresentationof
uncertaintyinthedecision-makingprocess.
Step 2: In this step, the cluster centroids are determined qualitatively by the user,
identifyingtheoptimalrankingforeachcriterionwithinthecluster. Thisprocessemploys
fuzzynumbers,representedasvalues(a,b,c)rangingbetween0and1. Theseresultswill
allowustomeasurethedistancebetweentheclustercentroids,whichrepresenttheideal
positionforeachclusterbasedontheselectedcriteria—andthescoresofeachalternative.
Beyondthisprimarypurpose,theresultingcentroidsarealsousedtodeterminethecriterion
weights, which will later be applied in the TOPSIS method. Formula (1) calculates the
centroidrepresentingtheoptimalpositionwithinagivencluster.
(cid:18) a +b +c (cid:19)
C = w w w , (1)
cwj
3
j
wherea ,b ,c arethefuzzynumbercomponentsrepresentingtheoptimalpositionwithin
w w w
agivenclusterj.
Step3: Determinationofalternativecentroids—usingafuzzyclusteringapproach,
thecentroidsofeachalternativearedetermined. ThecentroidC foreachalternativeiis
Aij
computedasfollows:
(cid:18) a +b +c (cid:19)
C = i i i , (2)
Aij
3
j
wherea,b,c arethefuzzynumbercomponentsofalternativeiinthecriterionj.
i i i
Thisformulaisappliedtoallalternativesacrossallconsideredcriteriatoestablishthe
rankingofthealternatives.
Equations (1) and (2) define two distinct types of centroids within the proposed
method:clustercentroidsandalternativecentroids.Theclustercentroidrepresentstheideal

Appl.Sci.2025,15,4044 7of21
positionofagivenclusteracrossallcriteriaandiscomputedbasedonpredefinedfuzzy
valuesthatcharacterizethecluster’soptimalconditions. Thiscentroidremainsfixedforall
alternativeswithinthecluster,servingasareferencepointforcomparison. Incontrast,the
alternativecentroidiscalculatedbasedonthefuzzyscoresassignedtoaspecificalternative,
meaningitvariesfromonealternativetoanother. Whiletheclustercentroidreflectsthe
overallprofileofagroup,thealternativecentroidcapturestheindividualpositioningofan
alternativewithinthedecisionspace. Thisdistinctioniscrucialfortheclusteringprocess,
asitenablesamoreflexibleclassificationofalternativeswhilemaintainingastructured
evaluationframework.
Step4: Thenewdecisionmatrix,obtainedfromStep3,isnormalizedusingthecost
(lowerisbetter)andbenefit(higherisbetter)formulas(Formulas(2)and(3)).
max(X)−X
N = i , (3)
i max(X)−min(X)
X −max(X)
N = i , (4)
i max(X)−min(X)
whereN isthenormalizedvalueofthealternativei,X istheoriginalvalueofthealterna-
i i
tivei,max(X)isthemaximumvalueinthecriterion,andmin(X)istheminimumvaluein
thecriterion. Theseformulasscalethevaluesbetween0and1,ensuringafaircomparison
betweenalternativeswhilemaintainingthemeaningofcostandbenefitcriteria.
Step5: Calculationofdistancetoclustercentroids—thedistancebetweeneachalter-
nativecentroid(CAlternative)ineachcriterionj,andeachclustercentroid(CCluster)ineach
criterionj,iscalculatedusingtheEuclideandistanceformulaasfollows:
(cid:118)
D iw =
(cid:117)
(cid:117) (cid:116) ∑
m (cid:16)
C i A j lternative−C w Cl j uster
(cid:17)2
, (5)
j=1
whereD representsthedistancebetweenthecentroidofalternativeiandthecentroidof
iw
theoptimalpositionwithinclusterw,andmdenotesthenumberofcriteriaconsideredin
theMCDMproblemunderanalysis.
Step 4: Assignment of alternatives to clusters—each alternative is assigned to the
cluster with the smallest distance to its centroid. This process involves calculating the
distancebetweeneachalternativeandallclustercentroids. Thealternativeisthenassigned
to the cluster with the nearest centroid, ensuring it is grouped with the most similar
alternativesasdefinedinFormula(6).
C =argminD , (6)
i iw
w
where C is the cluster assigned to alternative i and argmin selects the cluster w that
i
w
minimizesthedistance.
3.2. LogarithmicNormalization: AnAdaptiveApproachforTOPSIS
Normalizationisafundamentalstepinmulti-criteriadecision-making(MCDM)meth-
odssuchasTOPSIS(TechniqueforOrderofPreferencebySimilaritytoIdealSolution). It
ensuresthatcriteriawithdifferentunitsandscalescanbemeaningfullycompared. Tra-
ditionalnormalizationmethods, suchasMin–MaxandZ-score, effectivelyrescaledata
butmaynotbesuitablefordatasetswithhighvariance,extremeoutliers,ornon-linear
distributions. Insuchcases,logarithmicnormalizationemergesasanalternativetechnique
thatdynamicallyadjuststodatadistributions,makingitparticularlyeffectiveforhandling
dataspanningmultipleordersofmagnitude. Bycompressinglargenumericalvariations

Appl.Sci.2025,15,4044 8of21
while amplifying smaller differences, this approach ensures a more balanced contribu-
tionofcriteriatothefinaldecision, preservingtherelativerankingamongalternatives.
LogarithmicnormalizationismathematicallyexpressedasshowninEquation(7),
log(X)−log(X )
X = min , (7)
log(X )−log(X )
max min
where X represents the normalized value, X is the original value, and X and X
min max
denotetheminimumandmaximumvalueswithinagivencriterion. Thistransformationis
particularlybeneficialindecision-makingscenarioswheresomecriteriaexhibitexponential
growthpatterns,suchasfinancialmetrics,environmentalindicators,andenergyconsump-
tion data. By using a logarithmic scale, the influence of extreme values is harmonized,
ensuringthatallcriteriacontributemeaningfullytothedecision-makingprocessinTOPSIS,
forinstance. Akeystrengthoflogarithmicnormalizationisitsadaptivenature. Unlike
fixedrangemethods,itautomaticallyadjuststovaryingdatamagnitudes,dynamically
scalingvaluestoensurefaircomparisonsacrosscriteria. Thismakesitparticularlyeffective
fordatasetswithhighlyskeweddistributionsorlargenumericaldifferences. Moreover,
itenhancesdecisionstability,reducingthedominanceofcriteriawithdisproportionately
largevalueswhileensuringthatsmallervaluesremaindistinguishable. Anotheradvantage
oflogarithmicnormalizationisitsabilitytoenhancedifferentiationamongalternatives.
Byredistributingvaluesinawaythatemphasizesproportionaldifferences,itensuresthat
the ranking process in TOPSIS remains representative and reliable, even when dealing
withhighlydisperseddatasets. Thisisparticularlybeneficialincaseswherecriteriaex-
hibitnon-linearrelationships,allowingforamoreaccuratereflectionofeachalternative’s
performance. TheimplicationsoflogarithmicnormalizationinTOPSISaresignificant. By
integratingthisapproach,rankingsbecomemorestableandreflectiveofreal-worldcondi-
tions,ensuringthatdecision-makingprocessesremainrobustandinterpretable. Givenits
abilitytobalancedifferencesacrosscriteriawithoutdistortingrankings,logarithmicnormal-
izationoffersanadvancedscalingtechniquethatalignswellwithdiversedecision-making
scenarios. Despiteitsmanyadvantages,logarithmicnormalizationhasyettobewidely
integratedintotheTOPSISframework,presentinganexcitingopportunityforinnovation.
Byintroducingthisapproach,wecancreateamoreadaptivewayofhandlingcriteriawith
highvariance,non-lineardistributions,andsensitivitytooutliers. Thisintegrationhelps
improverankingstability,ensuresfairercomparisonsbetweenalternatives,andstrengthens
theoveralldecision-makingprocess. Whatmakeslogarithmicnormalizationevenmore
appealingisitseaseofimplementation. Whileiteffectivelybalancesdatadistributionand
minimizestheimpactofextremevalues,itremainsjustassimpletoapplyasMin–Maxor
Z-scorenormalization. Thismeansthatdecision-makerscanbenefitfromitsadvantages
withoutfacingadditionalcomputationalcomplexityorimplementationchallenges.
Tofurtherclarifytheproposedmethod,Figure1providesastep-by-stepflowchart
illustrating the transformation of raw data into fuzzy values, the application of fuzzy
clustering,andthefinallogarithmicnormalization.
Theproposedmethodintroducesseveralmethodologicalinnovationsthatenhance
the flexibility, interpretability, and robustness of the TOPSIS framework. First, instead
ofrelyingondata-drivenclusteringtechniques,theapproachusesexpert-definedideal
clusterprofiles(step4),representedthroughfuzzynumbers,allowingforcontext-aware
classificationofalternatives. Second,alternativesareassignedtoclustersbasedontheir
Euclideandistancetotheseidealprofiles,enablingadeterministicandtransparentgrouping
process(steps7and8). Third,logarithmicnormalizationisappliedwithineachclusterto
reducetheinfluenceofoutliersandlargevariances,improvingthestabilityandfairnessof
therankings(step9). Finally,themethodderivestheweightsofcriteriadirectlyfromthe

Appl.Sci.2025,15,4044 9of21
idealclustercentroids,eliminatingtheneedforsubjectiveorcomplexweightingprocedures
Appl. Sci. 2025, 15, x FOR PEER REVIEW 9 of 21
(step10).Together,theseinnovationsofferapracticalandscalablesolutionformulti-criteria
decision-makinginreal-worldscenariosinvolvinguncertaintyandheterogeneousdata.
Figure1.Overviewoftheproposeddecision-makingworkflow,combiningfuzzyevaluation,cluster
Figure 1. Overview of the proposed decision-making workflow, combining fuzzy evaluation, clus-
assignment,andlogarithmicnormalizationwithintheTOPSISframework.Thedashedoutlineboxes
ter assignment, and logarithmic normalization within the TOPSIS framework. The dashed outline
representthecontributionsoftheproposedmethodology.
boxes represent the contributions of the proposed methodology.
4. CaseStudy
The proposed method introduces several methodological innovations that enhance
Thiscasestudyfocusesonselectingthemostsuitablecitytohostaninternationalevent
stchhee dfluelxeidbitloittya,k ienptelarpcereintatbwiloityye, aarns.dT rhoebduesctniseiosns oisf ctohme pTlOexP,SinISv oflrvaimngewthoerekv.a Fluirastti,o innstead of
orfeklyeiynfga cotno rdsastuac-hdraisvceons tcsl,ulsotgeirsitnicgs ,teactthenndiqeueeesx,p therei eanpcpe,roanadcho uveserasl lexevpeenrtt-idmepfiancet.dT iodeal clus-
ftaecri lpitraotefitlhese (psrtoecpe 4ss),, raedparteasseenttoefdp tohtreonutigahl hfousztzcyi tnieusmwbaesrasn, aallylozwedinagn dfogr rcoounpteedxti-natwoare clas-
csliufiscteartsiobna soefd aolnteercnoantoivmeisc. cSheacroanctder, iastlitcesr,ninaftrivasetsr uacrteu raesqsiuganlietyd, staof ectlyu,satnedrsa bccaessesdib iolinty t.heir Eu-
Table 1 presents an overview of the cities, each identified by a letter for clarity. These
clidean distance to these ideal profiles, enabling a deterministic and transparent grouping
citieswerethoroughlyassessed,withdescriptionshighlightingtheirindividualstrengths
process (steps 7 and 8). Third, logarithmic normalization is applied within each cluster to
andchallenges. Thisstructuredapproachprovidesvaluableinsights,supportingdecision-
reduce the influence of outliers and large variances, improving the stability and fairness
makersinidentifyingthebestlocationtoensuretheevent’ssuccess. Intotal,12citieswere
of the rankings (step 9). Finally, the method derives the weights of criteria directly from
evaluatedusingfourcriteria:cost,infrastructure,safety,andaccessibility.Thesealternatives
the ideal cluster centroids, eliminating the need for subjective or complex weighting pro-
wereselectedtoreflectarealisticshortlistingscenario,wheredecision-makerstypically
ncaerdrouwreds o(wstnepo p1t0io).n Tsobgaseethdeorn, tphreesliem iinnnaroyvsactrieoennsi nogff.eWr hai lpertahcetidcaatla asentdis smcaoldaebrlaet esoinlution for
smizeu,litti-ccarpittuerreias adedciviseirosen-rmanagkeionfgu irnb arneaplr-owfiolersldan sdcegneoagriroaps hinicvcoolnvtienxgts .uTnhceersttrauincttuyr eanofd hetero-
tgheendeaotau—s doragtaan. izedasfuzzyevaluationspercriterion—allowsfornuancedanalysisand
robustcomparisonacrossalternatives.
4. CTahseec iStietsuwdeyr e evaluated based on the following four key criteria, each playing a
crucialroleindeterminingtheirsuitabilitytohosttheinternationalevent:
This case study focuses on selecting the most suitable city to host an international
1. Cost(C1): Theestimatedtotalexpenseofhostingtheevent,measuredinmillionsof
event scheduled to take place in two years. The decision is complex, involving the evalu-
dollars. Thiscriterionreflectsthefinancialfeasibilityofeachcityanditspotential
ation of key factors such as costs, logistics, attendee experience, and overall event impact.
impactontheevent’sbudget.
To facilitate the process, a dataset of potential host cities was analyzed and grouped into
clusters based on economic characteristics, infrastructure quality, safety, and accessibility.
Table 1 presents an overview of the cities, each identified by a letter for clarity. These cities
were thoroughly assessed, with descriptions highlighting their individual strengths and
challenges. This structured approach provides valuable insights, supporting decision-
makers in identifying the best location to ensure the event’s success. In total, 12 cities were
evaluated using four criteria: cost, infrastructure, safety, and accessibility. These alterna-
tives were selected to reflect a realistic shortlisting scenario, where decision-makers typi-
cally narrow down options based on preliminary screening. While the dataset is moderate
in size, it captures a diverse range of urban profiles and geographic contexts. The structure

Appl.Sci.2025,15,4044
10of21
2. Infrastructure(C2): Ascorefrom1to10thatrepresentsthequalityofvenues,trans-
portationsystems,accommodations,andotherfacilitiesrequiredtohostalarge-scale
internationalevent.
3. Safety(C3): Anindex(1to10)measuringoverallsafetyinthecity,includingcrime
rates,politicalstability,andemergencypreparedness. Ahigherscoreindicatesasafer
environmentforattendees.
4. Accessibility(C4): Ascorefrom1to10reflectingthecity’sconnectivityandeaseof
access,includinginternational/domesticflightavailability,publictransit,androad
infrastructure.
Table1.Potentialcitiesforselectionashostsofaninternationalevent.
| City(Letter) | City | Description |
| ------------ | ---- | ----------- |
Low-costcitywithfunctionalinfrastructure,ideal
| CityA | Hanoi,Vietnam |     |
| ----- | ------------- | --- |
forregionalevents.
Highlyaffordablebutwithlimitedinfrastructure
| CityB | Kathmandu,Nepal |     |
| ----- | --------------- | --- |
andmoderatesafety.
Exceptionalinfrastructure,safety,andaccessibility;
| CityC | Tokyo,Japan |     |
| ----- | ----------- | --- |
high-costcity.
CityD Singapore,Singapore SimilarqualitytoTokyowithslightlylowercosts.
|     | KualaLumpur, | Balancedcitywithhighsafety,accessibility,and |
| --- | ------------ | -------------------------------------------- |
CityE
|     | Malaysia | moderatecosts. |
| --- | -------- | -------------- |
MoreaffordablethanKualaLumpur,withslightly
| CityF | Bangkok,Thailand |     |
| ----- | ---------------- | --- |
lowersafetyscores.
Affordablewithgrowinginfrastructureand
| CityG | Colombo,SriLanka |     |
| ----- | ---------------- | --- |
moderateaccessibility.
Slightlyhighercostwithchallengesininfrastructure
| CityH | Manila,Philippines |     |
| ----- | ------------------ | --- |
andsafety.
Highsafetyandgoodinfrastructure,thoughslightly
| CityI | Seoul,SouthKorea |     |
| ----- | ---------------- | --- |
lessaccessible.
Highlyaccessibleandsecure,withcostssimilar
| CityJ | HongKong,China |     |
| ----- | -------------- | --- |
toTokyo.
|     | HoChiMinhCity, | Goodsafetyandaccessibility,withmoderately |
| --- | -------------- | ----------------------------------------- |
CityK
|     | Vietnam | highercosts. |
| --- | ------- | ------------ |
Highaccessibilityandsafetywithbalanced,
| CityL | Jakarta,Indonesia |     |
| ----- | ----------------- | --- |
moderatecosts.
To streamline the decision-making process, the cities under consideration were
grouped into three clusters based on shared characteristics, including cost, infrastruc-
ture,safety,andaccessibility. Eachclusterrepresentsadistinctcategoryofcities,enabling
decision-makerstonarrowtheirfocusandevaluatealternativesmoreeffectivelyasfollows:
1. Cluster1: Cost-EffectiveCitieswithModerateInfrastructure. Thisclusterconsists
of budget-friendly cities, making them attractive options for events with tighter
financialconstraints. Theirlowercostsalloworganizerstoallocateresourcestoother
areas,suchasmarketingorimprovingtheattendeeexperience. Thesecitiesmayalso
attracthigherattendancefromlocalorregionalparticipantsduetotheiraffordability.
However, they present certain challenges. Infrastructure may require temporary
enhancementstomeettheneedsofaninternationalaudience,andtheirsafetyand
accessibilityscoresaregenerallymoderate—requiringcarefulplanningtoensurea
successfulevent.
Inthefollowing,thevaluespresentedforeachcriterionareanalyzedanddiscussed
usingfuzzynumbers, whichrepresenttheoptimalvaluesforeachcriterionwithinthis
cluster. These fuzzy values indicate the most desirable levels for cost, infrastructure,
safety, andaccessibility, providingadegreeofflexibilityratherthanrigid, fixedvalues.
Byapplyingfuzzylogic,thisapproachacknowledgesthatreal-worldcityclassifications

Appl.Sci.2025,15,4044 11of21
involvegradualtransitionsratherthanstrictcategorizations,allowingforamorenuanced
andadaptableevaluationofurbancharacteristicsasfollows:
1. Cost(C1):Thiscriterionrepresentsthefinancialaffordabilityofthecity.Sincethis
clusterfocusesoncost-effectivelocations,thecostshouldbeashighaspossible
(fuzzynumber(0.9,1,1)).Ahigherratingmeansthecityismorebudget-friendly
intermsoflivingexpenses,businessoperations,andoverallaffordability.
2. Infrastructure(C2): Thisreferstothequalityandavailabilityofpublicservices,
transportation, and essential facilities. Cities in this cluster should have a
moderatelevelofinfrastructure(fuzzynumber(0.5,0.6,0.7)). Thismeansthey
providebasicamenitiesbutmightrequireimprovementsinareaslikeroads,
publictransportation,healthcare,anddigitalconnectivity.
3. Safety(C3): Thiscriterionevaluateshowsecurethecityisforresidents,busi-
nesses, and visitors. These cities should have moderate safety levels (fuzzy
number (0.4, 0.5, 0.6)). While they are generally safe, they may have certain
areas that require extra precautions, such as higher crime rates or specific
securityconcerns.
4. Accessibility(C4): Thiscriterionassesseshowwell-connectedthecityisboth
regionallyandinternationally. Thecitiesinthisclustershouldhavemoderate
accessibility(fuzzynumber(0.4,0.5,0.6)). Theytypicallyhavegoodregional
connectivity through local transportation networks but might lack direct ac-
cesstoglobaltravelhubs,suchasmajorinternationalairportsorhigh-speed
raillinks.
2. Cluster2: High-InvestmentCitieswithWorld-ClassInfrastructure. Citiesinthisclus-
terarerenownedfortheirexceptionalinfrastructure,includingstate-of-the-artvenues,
premiumaccommodations,androbusttransportationnetworks. Thesecitiesareideal
foreventsthataimtoprojectprestigeorcatertohigh-profileattendees. Highsafety
andaccessibilityscoresfurtherensureasmoothandsecureexperienceforparticipants.
However,theseadvantagescomewithsignificantcosts,whichcanimpactprofitability
orrestrictparticipation. Carefulbudgetingandstrongjustificationstostakeholders
areessentialtoaddressthesechallenges. Thefollowinganalyzesanddiscussesthe
valuesforeachcriterioninCluster2usingfuzzynumbers,whichdefinetheoptimal
rangeforcost,infrastructure,safety,andaccessibilitywithinthiscategoryasfollows:
1. Cost (C1): Should be as low as possible (fuzzy number (0.05, 0.1, 0.12)) be-
cause these are expensive cities, making budget management a challenge.
The lower the rating, the higher the cost of living, business operations, and
generalexpenses.
2. Infrastructure(C2): Shouldbeashighaspossible(fuzzynumber(0.8,0.95,1))
to ensure world-classfacilities. Thisincludes cutting-edge public transporta-
tion, advancedhealthcaresystems, efficientdigitalconnectivity, andmodern
urbanplanning.
3. Safety(C3): Shouldbeashighaspossible(fuzzynumber(0.95,0.95,1))since
thesecitiesareknownfortheirstabilityandsecurity. Lowcrimerates,strong
lawenforcement,andasecureenvironmentmakethemattractiveforbusinesses
andresidentsalike.
4. Accessibility(C4): Shouldbeashighaspossible(fuzzynumber(0.7, 0.95, 1))
to ensure global connectivity. These cities have major international airports,
excellentpublictransitsystems,andstronginfrastructuretohostinternational
conferencesandbusinessevents.

Appl.Sci.2025,15,4044 12of21
3. Cluster3:BalancedCitieswithaMixofFeatures.Thisclusterincludescitiesthatstrike
astrongbalancebetweenaffordabilityandquality,offeringgoodinfrastructure,high
safetyratings,andexcellentaccessibilityatreasonablecosts. Theirversatilitymakes
them ideal for events that seek to combine cost-effectiveness with a high-quality
experience for attendees. While these cities may not be as affordable as those in
Cluster1orhaveinfrastructureasadvancedasthoseinCluster2,theiroverallbalance
makes them strong contenders for hosting successful events. Choosing between
similarlybalancedoptionsinthisclustermightrequireadditionalconsiderations,but
theirhighsafetyandaccessibilityscoresenhancetheexperienceforallparticipants.
ThefollowinganalyzesanddiscussesthevaluesforeachcriterioninCluster3using
fuzzynumbers,whichdefinetheoptimalrangeforcost,infrastructure,safety,and
accessibilitywithinthiscategory.
1. Cost(C1): Shouldbemoderate(fuzzynumber(0.5,0.6,0.7))becausethesecities
balancequalityandaffordability. Theyareneitherexcessivelyexpensivenor
extremelycheap,makingthemattractiveformiddle-incomeprofessionalsand
businesseslookingforcost-effectivebutwell-equippedlocations.
2. Infrastructure(C2): Shouldbegoodbutnotpremium(fuzzynumber(0.5,0.6,
0.7)). Thesecitiesprovidehigh-qualitypublicservices,efficienttransportation,
and modern urban planning, but they may lack the cutting-edge facilities of
world-classmetropolises.
3. Safety(C3): Shouldbehighbutnotextreme(fuzzynumber(0.5,0.6,0.7)). These
cities offer a safe environment with low to moderate crime rates, ensuring a
comfortablelivingandworkingatmospherewithoutreachingtheultra-secure
standardsofCluster2cities.
4. Accessibility(C4): Shouldbehighbutnotatthemaximumlevel(fuzzynumber
(0.5,0.6,0.7)). Thesecitieshavestrongregionalandinternationalconnectivity,
including well-developed airports and transport networks, but they do not
matchtheglobalreachofthetop-tierbusinesshubsinCluster2.
Table 2 provides a summary of the optimal scores for each cluster discussed in
this section, with the centroids of each cluster defined using fuzzy numbers for each
criterionconsidered.
Table2.Summaryofoptimalscoresforeachcluster—clustercentroids.
Cost(C1) Infrastructure(C2) Safety(C3) Accessibility(C4)
Cluster a b c a b c a b c a b c
1 0.9 1 1 0.5 0.6 0.7 0.4 0.5 0.6 0.4 0.5 0.6
2 0.05 0.1 0.12 0.8 0.95 1 0.95 0.95 1 0.7 0.95 1
3 0.5 0.6 0.7 0.5 0.6 0.7 0.5 0.6 0.7 0.5 0.6 0.7
The scores presented in Table 3 were developed through a collaborative process
involving a diverse panel of experts and analysts. This group combined professional
experience in event planning and logistics with insights drawn from tourist feedback
and reviews published in reputable travel and tourism journals. By integrating these
perspectives,theevaluationcapturednotonlythelogisticalandoperationaldimensionsof
hostinganinternationaleventbutalsotravelerperceptionsandexperiences.

Appl.Sci.2025,15,4044
13of21
Table3.Clustereddataofcitiesforeventhostinganalysis.
|       | Cost(C1)($K) |     | Infrastructure(C2) |     |     |     | Safety(C3) |     |     | Accessibility(C4) |      |
| ----- | ------------ | --- | ------------------ | --- | --- | --- | ---------- | --- | --- | ----------------- | ---- |
|       | a b          | c   | a                  | b   | c   |     | a          | b   | c   | a                 | b c  |
| CityA | 11 14        | 16  | 4                  | 5   | 6   |     | 6          | 7   | 8   | 5                 | 6 7  |
| CityB | 9 11         | 14  | 2                  | 3   | 4   |     | 3          | 4   | 5   | 3                 | 4 5  |
| CityC | 34 39        | 45  | 8                  | 9   | 10  |     | 8          | 9   | 10  | 8                 | 9 10 |
| CityD | 32 37        | 43  | 8                  | 9   | 10  |     | 8          | 9   | 10  | 8                 | 9 10 |
| CityE | 18 20        | 23  | 6                  | 7   | 8   |     | 6          | 7   | 8   | 7                 | 8 9  |
| CityF | 16 18        | 20  | 5                  | 6   | 7   |     | 5          | 6   | 7   | 7                 | 8 9  |
| CityG | 14 16        | 18  | 4                  | 5   | 6   |     | 4          | 5   | 6   | 5                 | 6 7  |
| CityH | 20 23        | 25  | 3                  | 4   | 5   |     | 3          | 4   | 5   | 6                 | 7 8  |
| CityI | 29 35        | 41  | 7                  | 8   | 9   |     | 7          | 8   | 9   | 7                 | 8 9  |
| CityJ | 32 37        | 43  | 8                  | 9   | 10  |     | 7          | 8   | 9   | 8                 | 9 10 |
| CityK | 14 16        | 18  | 5                  | 6   | 7   |     | 5          | 6   | 7   | 6                 | 7 8  |
| CityL | 18 20        | 23  | 4                  | 5   | 6   |     | 4          | 5   | 6   | 6                 | 7 8  |
Thiscomprehensiveapproachensuredthattheassessmentreflectedboththefunc-
tionalfeasibilityandthebroaderappealofeachcityasavibrantandwelcomingdestination.
Foreachcityandcriterion,expertsprovidedindividualscoresbasedontheirknowledge,
experience,andtrustedsourcessuchasgovernmentreports,travelerfeedback,andindus-
tryanalyses. Asexpected,theseevaluationsvaried,reflectingdifferingviewpointsand
prioritiesacrossthepanel.
To ensure fairness and consistency, final scores were calculated by averaging the
individualassessmentsforeachcriterionandcity.Theresultingvalueswerethenexpressed
asfuzzynumbers. Thismethodhelpsharmonizediverseopinionsandminimizespotential
bias,yieldingwell-roundedandobjectivescoresforamorebalancedevaluation.
5. ResultsandDiscussion
Inthissection,weapplytheproposedmodels,includingthenewclusteringapproach
andthelogarithmicnormalizationmethod—withintheTOPSISframeworkforthepre-
sentedcasestudy. Theresultsaredetailedstepbystep,thenanalyzedandcomparedwith
thoseobtainedusingtraditionalmethods.
Table4presentstheprocessingofthedatafromTable3. Usingthefuzzynumberof
eachalternativeforeachcriterion,thecorrespondingcentroidiscalculated(columns2to
5),usingEquation(2). ThesecentroidsarethennormalizedusingtheMin–Maxmethod
(columns6to9),usingEquations(3)and(4).
Table4.Normalizedcentroidsforthefourconsideredcriteriaacrossselectedcities.
|       |          |          |          |     |          |            | (C1) |            | (C1) | (C1)       | (C1)       |
| ----- | -------- | -------- | -------- | --- | -------- | ---------- | ---- | ---------- | ---- | ---------- | ---------- |
|       | (C1)     | (C2)     | (C3)     |     | (C4)     |            |      |            |      |            |            |
|       |          |          |          |     |          | Centroid   |      | Centroid   |      | Centroid   | Centroid   |
|       | Centroid | Centroid | Centroid |     | Centroid |            |      |            |      |            |            |
|       |          |          |          |     |          | Normalized |      | Normalized |      | Normalized | Normalized |
| CityA | 14       | 5        | 7        |     | 6        |            | 0.92 |            | 0.33 | 0.6        | 0.4        |
| CityB | 11       | 3        | 4        |     | 4        |            | 1.00 |            | 0.00 | 0          | 0          |
| CityC | 39       | 9        | 9        |     | 9        |            | 0.00 |            | 1.00 | 1          | 1          |
| CityD | 37       | 9        | 9        |     | 9        |            | 0.08 |            | 1.00 | 1          | 1          |
| CityE | 20       | 7        | 7        |     | 8        |            | 0.68 |            | 0.67 | 0.6        | 0.8        |
| CityF | 18       | 6        | 6        |     | 8        |            | 0.76 |            | 0.50 | 0.4        | 0.8        |
| CityG | 16       | 5        | 5        |     | 6        |            | 0.84 |            | 0.33 | 0.2        | 0.4        |
| CityH | 23       | 4        | 4        |     | 7        |            | 0.60 |            | 0.17 | 0          | 0.6        |
| CityI | 35       | 8        | 8        |     | 8        |            | 0.16 |            | 0.83 | 0.8        | 0.8        |
| CityJ | 37       | 9        | 8        |     | 9        |            | 0.08 |            | 1.00 | 0.8        | 1          |
| CityK | 16       | 6        | 6        |     | 7        |            | 0.84 |            | 0.50 | 0.4        | 0.6        |
| CityL | 20       | 5        | 5        |     | 7        |            | 0.68 |            | 0.33 | 0.2        | 0.6        |

Appl.Sci.2025,15,4044
14of21
Thecentroidscalculatedforeachalternativearethenusedtocomputetheirdistances
totheoptimalscoresdefinedforeachcluster,asoutlinedinTable2.
Table5presentsthesedistances,calculatedusingtheEuclideannorm,asspecified
inEquation(5). Asthetableshows,thedistancebetweeneachalternativeandtheideal
cluster values varies. To assign each alternative to a cluster, we select the one with the
minimumdistance,asdescribedinEquation(6). ThefinalcolumninTable5displaysthe
shortestdistanceforeachalternative,withtheassignedclusterhighlightedinbold.
Table5.Evaluationofdistancestothecentroidsofeachcluster.
|       | (C1)Distance | (C2)Distance |      | (C3)Distance |      |     | min  |
| ----- | ------------ | ------------ | ---- | ------------ | ---- | --- | ---- |
| CityA | 0.31         |              | 1.18 |              | 0.46 |     | 0.31 |
| CityB | 0.93         |              | 1.84 |              | 1.11 |     | 0.93 |
| CityC | 1.26         |              | 0.17 |              | 0.92 |     | 0.17 |
| CityD | 1.20         |              | 0.15 |              | 0.87 |     | 0.15 |
| CityE | 0.43         |              | 0.74 |              | 0.23 |     | 0.23 |
| CityF | 0.39         |              | 0.98 |              | 0.34 |     | 0.34 |
| CityG | 0.43         |              | 1.31 |              | 0.57 |     | 0.43 |
| CityH | 0.76         |              | 1.36 |              | 0.74 |     | 0.74 |
| CityI | 0.94         |              | 0.22 |              | 0.57 |     | 0.22 |
| CityJ | 1.13         |              | 0.22 |              | 0.79 |     | 0.22 |
| CityK | 0.21         |              | 1.07 |              | 0.33 |     | 0.21 |
| CityL | 0.50         |              | 1.16 |              | 0.49 |     | 0.49 |
Table6presentstheresultsaggregatedbycluster,revealingadistributionthataligns
wellwiththeintendeddefinitionsofeachgroup.
Table6.Resultofthedistributionofalternativesusingtheproposedclusteringmethod.
|     |     | (C1) |     | (C2) |     | (C3) | (C4) |
| --- | --- | ---- | --- | ---- | --- | ---- | ---- |
Cluster
|       |     | Centroid |     | Centroid |     | Centroid | Centroid |
| ----- | --- | -------- | --- | -------- | --- | -------- | -------- |
| CityA | 1   | 14       |     | 5        |     | 7        | 6        |
| CityB | 1   | 11       |     | 3        |     | 4        | 4        |
| CityG | 1   | 16       |     | 5        |     | 5        | 6        |
| CityK | 1   | 16       |     | 6        |     | 6        | 7        |
| CityC | 2   | 39       |     | 9        |     | 9        | 9        |
| CityD | 2   | 37       |     | 9        |     | 9        | 9        |
| CityI | 2   | 35       |     | 8        |     | 8        | 8        |
| CityJ | 2   | 37       |     | 9        |     | 8        | 9        |
| CityE | 3   | 20       |     | 7        |     | 7        | 8        |
| CityF | 3   | 18       |     | 6        |     | 6        | 8        |
| CityH | 3   | 23       |     | 4        |     | 4        | 7        |
| CityL | 3   | 20       |     | 5        |     | 5        | 7        |
Cluster1—Cost-EffectiveCitieswithModerateInfrastructure—includesalternatives
withthelowestcosts,whiletheothercriteriagenerallyexhibitmoderatevalues,confirming
thecoherenceoftheclassification.
Cluster2—High-InvestmentCitieswithWorld-ClassInfrastructure—comprisesalter-
nativesthatmatchtheprofileofhigh-costcitiesofferingtop-tierscoresininfrastructure,
safety,andaccessibility.
Cluster3—BalancedCitieswithaMixofFeatures—includesalternativeswithinter-
mediatecostlevelsandcriteriaratingsthatfallbetweenthoseofClusters1and2. This
consistencyreinforcesthevalidityoftheproposedclusteringmethod.

Appl.Sci.2025,15,4044
15of21
Basedontheseresults,wecanconcludethattheproposedmodelproducesoutcomes
consistentwithexpectations. Thismeansthatanalyzingthedistributionofalternatives
acrossthedifferentclustersconfirmsthattheresultsarelogicalandalignwiththeexpected
distributionofalternativeswithineachcluster.
Table7comparestheproposedclusteringmethodwiththeFuzzyK-Meansapproach,
revealing that the results are nearly identical—with one notable exception: City K is
assignedtoCluster1bytheproposedmethod,whereasFuzzyK-MeansplacesitinCluster
3. Althoughthisdifferencemayappearminor,ithighlightsanimportantdistinctionin
howeachmethodinterpretsdistancesandassignsalternativestoclusters. Overall, the
strongalignmentbetweenthetwomethodssupportstheeffectivenessandreliabilityofthe
proposedapproachasaviablealternativetotraditionalfuzzyclusteringtechniques.
Table7.ComparisonbetweentheproposedclusteringmethodandtheFuzzyK-Meansmethod,bold
numbershighlightdiscrepanciesbetweenthetwomethods.
| ProposedMethod | FuzzyK-Means |     |
| -------------- | ------------ | --- |
| CityA          | 1            | 1   |
| CityB          | 1            | 1   |
| CityG          | 1            | 1   |
| CityK          | 1            | 3   |
| CityC          | 2            | 2   |
| CityD          | 2            | 2   |
| CityI          | 2            | 2   |
| CityJ          | 2            | 2   |
| CityE          | 3            | 3   |
| CityF          | 3            | 3   |
| CityH          | 3            | 3   |
| CityL          | 3            | 3   |
More importantly, assigning City K to Cluster 1 appears to be a more appropriate
classification. Thecitysharesalow-costprofile,whichisadefiningcharacteristicofCluster
1. In fact, City K has the same cost value as City G, which was placed in Cluster 1 by
theFuzzyK-Meansmethod. Theonlydifferencesbetweenthetwoareminor,suchasa
one-pointvariationinothercriteria—makingthemhighlycomparable.Therefore,grouping
CityKwithCityGinCluster1ismoreconsistentwiththeunderlyinglogicoftheclustering
process. Thissupportstheconclusionthattheproposedmethodoffersamoreaccurateand
contextuallysoundclassification.
Anotherkeyadvantageoftheproposedmethodliesinitssimplicityandcomputa-
tionalefficiencywhencomparedtoFuzzyK-Means,whichdependsonmultipleiterative
calculationsandamorecomplexoptimizationprocess. Incontrast,theproposedmethod
usesadirectandintuitiveapproachbyassigningeachalternativetothenearestcentroid,
eliminating the need for repeated recalculations. Fuzzy K-Means, on the other hand,
involvescontinuousre-evaluationofcentroids,whichincreasescomputationaldemands—
particularly for larger datasets. Additionally, Fuzzy K-Means applies a soft clustering
strategy,wherealternativescanpartiallybelongtomultipleclusters,whereastheproposed
methoddeterministicallyassignseachalternativetoasinglecluster.
In contrast, the proposed method is deterministic, assigning each alternative to a
singleclusterwithoutambiguity. Italsosignificantlyreducescomputationaloverheadby
avoidingiterativeadjustments. Itseaseofimplementationmakesitespeciallypracticalin
contextswherespeedandefficiencyareessential. Consideringthattheoverallclustering
resultsarenearlyidentical—andthattheproposedmethodclassifiesCityKinawaythat

Appl.Sci.2025,15,4044
16of21
alignsmorelogicallywiththedata—itcanberegardedasnotonlysimplerbutalsomore
accurateandreliablethantheFuzzyK-Meansapproach.
In the next step, the rankings of each alternative within their respective clusters
werenormalizedusingtwomethods: logarithmicnormalization(Table8)andMin–Max
normalization(Table9).
Table8.Logarithmicnormalizationresults.
| City  | Cluster | C1   | C2   | C3   | C4   |
| ----- | ------- | ---- | ---- | ---- | ---- |
| CityA | 1       | 0.96 | 0.92 | 1.00 | 0.94 |
| CityB | 1       | 0.88 | 0.71 | 0.77 | 0.77 |
| CityG | 1       | 1.00 | 0.92 | 0.86 | 0.94 |
| CityK | 1       | 1.00 | 1.00 | 0.94 | 1.00 |
| CityC | 2       | 1.00 | 1.00 | 1.00 | 1.00 |
| CityD | 2       | 0.99 | 1.00 | 1.00 | 1.00 |
| CityI | 2       | 0.97 | 0.95 | 0.95 | 0.95 |
| CityJ | 2       | 0.99 | 1.00 | 0.95 | 1.00 |
| CityE | 3       | 0.96 | 1.00 | 1.00 | 1.00 |
| CityF | 3       | 0.93 | 0.94 | 0.94 | 1.00 |
| CityH | 3       | 1.00 | 0.77 | 0.77 | 0.95 |
| CityL | 3       | 0.96 | 0.86 | 0.86 | 0.95 |
Table9.Min–Maxnormalizationresults.
| City  | Cluster | C1   | C2   | C3   | C4   |
| ----- | ------- | ---- | ---- | ---- | ---- |
| CityA | 1       | 0.60 | 0.67 | 1.00 | 0.67 |
| CityB | 1       | 0.00 | 0.00 | 0.00 | 0.00 |
| CityG | 1       | 1.00 | 0.67 | 0.33 | 0.67 |
| CityK | 1       | 1.00 | 1.00 | 0.67 | 1.00 |
| CityC | 2       | 1.00 | 1.00 | 1.00 | 1.00 |
| CityD | 2       | 0.50 | 1.00 | 1.00 | 1.00 |
| CityI | 2       | 0.00 | 0.00 | 0.00 | 0.00 |
| CityJ | 2       | 0.50 | 1.00 | 0.00 | 1.00 |
| CityE | 3       | 0.40 | 1.00 | 1.00 | 1.00 |
| CityF | 3       | 0.00 | 0.67 | 0.67 | 1.00 |
| CityH | 3       | 1.00 | 0.00 | 0.00 | 0.00 |
| CityL | 3       | 0.40 | 0.33 | 0.33 | 0.00 |
AnanalysisofTables8and9showsthatlogarithmicnormalizationoffersclearad-
vantagesoverMin–Maxnormalization,particularlyinthewayitdistributesvaluesacross
clusters. In Cluster 2, where the cost criterion (C1) exhibits significantly higher values
thaninotherclusters,Min–Maxnormalizationexaggeratesthesedifferences,makingcost
variationsbetweencitiesappearmorepronounced. Incontrast, logarithmicnormaliza-
tioncompressesthescale,reducingthegapsbetweenalternativeswhilepreservingtheir
relativerankings.
A similar effect is observed in Cluster 3, where differences in cost (C1) and infras-
tructure(C2)aremoreevenlybalancedunderlogarithmictransformation. Thisprevents
extreme values from overshadowing smaller differences. As a result, logarithmic nor-
malizationdeliversamorebalancedrepresentation, ensuringthatnosinglehighvalue
disproportionatelyinfluencestheoutcome—thusproducingamorestableandinterpretable
rankingsystem.
The next step is the application of the TOPSIS method to the normalized tables
(Tables8and9),consideringtheweightsforeachcriterionandeachcluster,aspresentedin

Appl.Sci.2025,15,4044
17of21
Table10. Theseweightsarederivedfromtheoptimalvalueswithineachclusterandare
essentiallyobtainedbynormalizingthesevaluesusingtheMin–Maxmethod.
Table10.Criterionweightsforeachcluster.
|         | (C1)Cluster | (C2)Cluster | (C3)Cluster | (C4)Cluster |          |          |          |          |
| ------- | ----------- | ----------- | ----------- | ----------- | -------- | -------- | -------- | -------- |
| Cluster |             |             |             |             | WeightC1 | WeightC2 | WeightC3 | WeightC4 |
|         | Centroid    | Centroid    | Centroid    | Centroid    |          |          |          |          |
| 1       | 1.0         | 0.6         | 0.5         | 0.5         | 0.38     | 0.23     | 0.19     | 0.19     |
| 2       | 0.1         | 0.9         | 1.0         | 0.9         | 0.03     | 0.32     | 0.34     | 0.31     |
| 3       | 0.6         | 0.6         | 0.6         | 0.6         | 0.25     | 0.25     | 0.25     | 0.25     |
TheTOPSISmethodwasthenappliedusingtheweightsderivedforeachcluster(as
showninTable10)andthenormalizeddatafrombothapproaches. Table11presentsthe
results obtained using logarithmic normalization, ranking the alternatives within their
respectiveclusters. Table12showstheresultsusingMin–Maxnormalization,allowingfor
adirectcomparisonbetweenthetwonormalizationtechniques.
Table11.TOPSISresultsusinglogarithmicnormalization,boldnumbersindicatethebestalternative
withineachclusteridentifiedbythemethod.
| City  | Cluster | C1   | C2   | C3   | C4   | D+   | D-   | TOPSISScore |
| ----- | ------- | ---- | ---- | ---- | ---- | ---- | ---- | ----------- |
| CityA | 1       | 0.36 | 0.21 | 0.19 | 0.18 | 0.03 | 0.08 | 0.74        |
| CityB | 1       | 0.33 | 0.16 | 0.15 | 0.15 | 0.10 | 0.00 | 0.00        |
| CityG | 1       | 0.38 | 0.21 | 0.16 | 0.18 | 0.03 | 0.08 | 0.69        |
| CityK | 1       | 0.38 | 0.23 | 0.18 | 0.19 | 0.01 | 0.10 | 0.89        |
| CityC | 2       | 0.03 | 0.32 | 0.34 | 0.31 | 0.00 | 0.03 | 1.00        |
| CityD | 2       | 0.03 | 0.32 | 0.34 | 0.31 | 0.00 | 0.03 | 0.98        |
| CityI | 2       | 0.03 | 0.31 | 0.32 | 0.30 | 0.03 | 0.00 | 0.00        |
| CityJ | 2       | 0.03 | 0.32 | 0.32 | 0.31 | 0.02 | 0.02 | 0.57        |
| CityE | 3       | 0.24 | 0.25 | 0.25 | 0.25 | 0.01 | 0.08 | 0.89        |
| CityF | 3       | 0.23 | 0.23 | 0.23 | 0.25 | 0.03 | 0.06 | 0.67        |
| CityH | 3       | 0.25 | 0.19 | 0.19 | 0.24 | 0.08 | 0.02 | 0.18        |
| CityL | 3       | 0.24 | 0.22 | 0.22 | 0.24 | 0.05 | 0.03 | 0.38        |
Table12.TOPSISresultsusingMin–Maxnormalization,boldnumbersindicatethebestalternative
withineachclusteridentifiedbythemethod.
| City  | Cluster | C1   | C2   | C3   | C4   | D+   | D-   | TOPSISScore |
| ----- | ------- | ---- | ---- | ---- | ---- | ---- | ---- | ----------- |
| CityA | 1       | 0.23 | 0.15 | 0.19 | 0.13 | 0.18 | 0.36 | 0.66        |
| CityB | 1       | 0.00 | 0.00 | 0.00 | 0.00 | 0.52 | 0.00 | 0.00        |
| CityG | 1       | 0.38 | 0.15 | 0.06 | 0.13 | 0.16 | 0.43 | 0.73        |
| CityK | 1       | 0.38 | 0.23 | 0.13 | 0.19 | 0.06 | 0.50 | 0.89        |
| CityC | 2       | 0.03 | 0.32 | 0.34 | 0.31 | 0.00 | 0.56 | 1.00        |
| CityD | 2       | 0.02 | 0.32 | 0.34 | 0.31 | 0.02 | 0.56 | 0.97        |
| CityI | 2       | 0.00 | 0.00 | 0.00 | 0.00 | 0.56 | 0.00 | 0.00        |
| CityJ | 2       | 0.02 | 0.32 | 0.00 | 0.31 | 0.34 | 0.45 | 0.57        |
| CityE | 3       | 0.10 | 0.25 | 0.25 | 0.25 | 0.15 | 0.44 | 0.75        |
| CityF | 3       | 0.00 | 0.17 | 0.17 | 0.25 | 0.28 | 0.34 | 0.55        |
| CityH | 3       | 0.25 | 0.00 | 0.00 | 0.00 | 0.43 | 0.25 | 0.37        |
| CityL | 3       | 0.10 | 0.08 | 0.08 | 0.00 | 0.37 | 0.15 | 0.29        |
TheapplicationoftheTOPSISmethodusingbothMin–Maxandlogarithmicnormal-
ization identified the top-ranked cities within each cluster. The results show that City
K(Cluster1)andCityC(Cluster2)consistentlyachievedthehighestscoresacrossboth
normalizationmethods,whileCityE(Cluster3)exhibitedsomevariationdependingon
thetechniqueused.

Appl.Sci.2025,15,4044 18of21
InCluster1,CityKemergedasthebest-performingalternative,withaTOPSISscore
of approximately 0.887 in both cases. This indicates that City K offers a well-balanced
combinationofcost,infrastructure,safety,andaccessibility,makingitthemostsuitable
option within its group. Its consistent ranking across both normalization techniques
demonstratesstrongalignmentwiththecluster’sidealconditions.
InCluster2,CityCachievedaperfectTOPSISscoreof1.000underbothnormalization
methods, confirming its status as the most suitable alternative for this category. The
unchangedresult,regardlessofthenormalizationapplied,reinforcesCityC’sdominance
intermsofmeetingallweightedcriteria.
Incontrast,CityEledCluster3butshowednoticeablevariationbetweenmethods:
0.747usingMin–Maxand0.886withlogarithmicnormalization. Thisdifferencesuggests
thatthelogarithmicapproachwasmoreeffectiveinsmoothingextremevaluesandreducing
theinfluenceofoutliers. Asaresult,CityEappearedclosertotheidealsolutionunder
logarithmicnormalization.
Overall,theconsistencyofCityKandCityCastop-rankedalternativesreinforcesthe
robustnessofthemethodologyandconfirmsthatthechosencriteriaeffectivelydistinguish
the best-performing cities within each cluster. However, the variation in City E’s score
highlightshownormalizationcaninfluencerankingintensity,particularlyindatasetswhere
differencesbetweenvaluesaremorepronounced.
The results show that logarithmic and Min–Max normalizations produced nearly
identicaloutcomesintheTOPSISanalysis,indicatingthatwhentherearenosignificant
outliers,logarithmicnormalizationperformsjustaswellastheMin–Maxmethod.However,
inthepresenceofextremevalues,logarithmicnormalizationprovestobemoreeffective,as
itreducestheimpactofoutliersandpreventscriteriawithveryhighvaluesfromdistorting
thedistancecalculationsinTOPSIS.
Thus, it is observed that for datasets without outliers, logarithmic normalization
performsjustaswellasMin–Maxnormalization, withtheaddedadvantagethatwhen
outliersarepresent,logarithmicnormalizationdeliversbetterperformance. Ifthegoalis
toensurethatnormalizationhasameaningfuleffectonlyincaseswheredatavariationis
large,logarithmicnormalizationispreferableduetoitsabilitytosmoothextremevalues.
However,whenthedataarenaturallywell-distributed,Min–Maxnormalizationremainsa
validoption,asitpreservestheoriginalproportionswithoutinformationloss.
6. Conclusions
This study introduced two methodological innovations to enhance the TOPSIS
decision-makingframework: ClusteringUsingFuzzyNumbersandCentroid-BasedDis-
tance Allocation and logarithmic normalization. Together, these methods address key
limitationsintraditionalMCDMapproaches,particularlyinthehandlingofuncertainty,
outliers,andrigiddata-drivenclassifications.
The proposed clustering approach allows decision-makers to define ideal cluster
profilesindependentlyofthedataset,enablinggreaterstrategiccontrol. Fuzzynumbers
are used exclusively to model uncertainty in the evaluation of alternatives, which are
thenconvertedtocrispvaluestocalculateEuclideandistancesfrompredefinedcentroids.
This results in a robust yet transparent classification method, free from iterative opti-
mizationorprobabilisticmembershipfunctions. Unliketraditionalclusteringtechniques
suchasK-Means,whichderivecentroidsfromdata,ourapproachdecouplesclustering
fromdatadistributionandfocusesonalignmentwithidealizedprofiles—offeringgreater
interpretabilityandconsistency.
LogarithmicnormalizationfurtherenhancestherobustnessoftheTOPSISmethodby
smoothingextremevaluesandpreservingproportionaldifferencesacrosscriteria.Thisises-

Appl.Sci.2025,15,4044 19of21
peciallyusefulindatasetswithhighvarianceornon-lineardistributions,wheretraditional
normalizationtechniquesmaydistortrankings.
The case study results demonstrate that the proposed methodologies significantly
enhanceboththeaccuracyandstabilityofdecision-makingoutcomes. Thefuzzyclustering
approachenablesmorerealisticclassificationofalternatives,whilelogarithmicnormaliza-
tionimprovesthecomparabilityofcriteria—withoutaddingunnecessarycomplexity.Akey
advantageofbothmethodsistheircomputationalsimplicityandeaseofimplementation,
makingthemaccessibleforabroadrangeofpracticalapplications.
Beyond the context of city selection, the proposed methodology offers broader en-
hancementstodecision-makingbyimprovinghowalternativesaregroupedandcompared
inthepresenceofuncertaintyandvariability. Itsmodulardesign—combiningfuzzy-based
evaluation,predefinedclustercentroids,andadaptivenormalization—makesitsuitable
for various domains such as supply chain optimization, financial assessment, environ-
mentalplanning,andstrategicprojectprioritization. Themethodsupportsmorerobust,
context-aware,andscalabledecisionprocessesacrossdiversereal-worldapplications.
Although the results are promising, there remain several opportunities for further
explorationandvalidation.Alogicalnextstepistotesttheperformanceofthesetechniques
withinotherMCDMmodels—suchasVIKOR,PROMETHEE,andAHP—toassesstheir
adaptabilityacrossdifferentdecision-makingframeworks.Eachofthesemodelshasunique
characteristics,andapplyingtheproposedmethodswithinthemcouldofferdeeperinsights
intotheirgeneralizabilityandeffectiveness.
Despiteitspromisingresults,theproposedmethodologypresentssomelimitations.
The definition of ideal cluster centroids is currently based on expert judgment, which,
whileofferingflexibilityandinterpretability,mayintroduceadegreeofsubjectivity. Fu-
turerefinementscouldexplorehybridordata-assistedstrategiestosupportorvalidate
thesepredefinedprofiles. Additionally,whilethemethodiscomputationallysimpleand
effectiveinthecasestudy,itsperformanceinlarge-scaleorhigh-dimensionalproblems
remainstobetested. Moreover,althoughtheproposedapproachwasappliedwithinthe
TOPSIS framework, evaluating its integration with other MCDM models (e.g., VIKOR,
PROMETHEE,AHP)wouldhelpassessitsgeneralizability.
Finally,futureworkcouldinvolvebenchmarkingtheproposedmethodsagainstother
clusteringandnormalizationtechniques. Comparativeanalysesfocusedonclassification
accuracy,rankingstability,andcomputationalefficiencywouldfurthersupportmethod
refinementandfosterbroaderadoptionincomplexdecision-makingcontexts.
AuthorContributions:Conceptualization,V.A.andA.A.;methodology,V.A.;software,V.A.;vali-
dation,V.A.andA.A.;formalanalysis,V.A.;investigation,V.A.;resources,V.A.;datacuration,V.A.;
writing—originaldraftpreparation,V.A.;writing—reviewandediting,A.A.;visualization,A.A.;
supervision,V.A.;projectadministration,V.A.;fundingacquisition,A.A.Allauthorshavereadand
agreedtothepublishedversionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Theoriginalcontributionspresentedinthestudyareincludedinthe
article;furtherinquiriescanbedirectedtothecorrespondingauthors.
Acknowledgments: TheauthorsgratefullyacknowledgethesupportfromFCT–Fundaçãoparaa
CiênciaeTecnologia(PortugueseFoundationforScienceandTechnology),throughIDMEC,under
LAETABaseFunding(DOI:10.54499/UIDB/50022/2020).
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.

Appl.Sci.2025,15,4044 20of21
References
1. Štilic´,A.;Puška,A.IntegratingMulti-CriteriaDecision-MakingMethodswithSustainableEngineering:AComprehensiveReview
ofCurrentPractices.Eng2023,4,1536–1549.[CrossRef]
2. Hajduk,S.;Jelonek,D.ADecision-MakingApproachBasedonTOPSISMethodforRankingSmartCitiesintheContextofUrban
Energy.Energies2021,14,2691.[CrossRef]
3. Madi,E.N.;Zakaria,Z.A.;Sambas,A.;Sukono.TowardEffectiveUncertaintyManagementinDecision-MakingModelsBasedon
Type-2FuzzyTOPSIS.Mathematics2023,11,3512.[CrossRef]
4. Cai,M.;Hong,Y.ImprovedTOPSISMethodConsideringFuzzinessandRandomnessinMulti-AttributeGroupDecisionMaking.
Mathematics2022,10,4200.[CrossRef]
5. Sałabun,W.;Wa˛tróbski,J.;Shekhovtsov,A.AreMCDAMethodsBenchmarkable? AComparativeStudyofTOPSIS,VIKOR,
COPRAS,andPROMETHEEIIMethods.Symmetry2020,12,1549.[CrossRef]
6. Vakilipour,S.;Sadeghi-Niaraki,A.;Ghodousi,M.;Choi,S.-M.ComparisonbetweenMulti-CriteriaDecision-MakingMethods
andEvaluatingtheQualityofLifeatDifferentSpatialLevels.Sustainability2021,13,4067.[CrossRef]
7. Qureshi, A.M.; Rachid, A. Comparative Analysis of Multi-Criteria Decision-Making Techniques for Outdoor Heat Stress
Mitigation.Appl.Sci.2022,12,12308.[CrossRef]
8. Lim,Z.-Y.;Ong,L.-Y.;Leow,M.-C.AReviewonClusteringTechniques:CreatingBetterUserExperienceforOnlineRoadshow.
FutureInternet2021,13,233.[CrossRef]
9. Krasnov,D.;Davis,D.;Malott,K.;Chen,Y.;Shi,X.;Wong,A.FuzzyC-MeansClustering:AReviewofApplicationsinBreast
CancerDetection.Entropy2023,25,1021.[CrossRef]
10. Al-Augby,S.;Majewski,S.;Majewska,A.;Nermend,K.AComparisonOfK-MeansAndFuzzyC-MeansClusteringMethods
ForASampleOfGulfCooperationCouncilStockMarkets.FoliaOeconomicaStetin.2014,14,19–36.[CrossRef]
11. Ghadiri,N.;Ghaffari,M.;Nikbakht,M.A.BigFCM:Fast,PreciseandScalableFCMonHadoop. arXiv2016,arXiv:1605.03047.
[CrossRef]
12. Chen,Y.;Zhou,S.RevisitingPossibilisticFuzzyC-MeansClusteringUsingtheMajorization-MinimizationMethod.Entropy2024,
26,670.[CrossRef][PubMed]
13. Chan,K.Y.;Yiu,K.F.C.;Kim,D.;Abu-Siada,A.FuzzyClustering-BasedDeepLearningforShort-TermLoadForecastinginPower
GridSystemsUsingTime-VaryingandTime-InvariantFeatures.Sensors2024,24,1391.[CrossRef]
14. Vafaei,N.;Ribeiro,R.A.;Matos,L.M.C.DataNormalizationTechniquesinDecisionMaking:CaseStudywithTOPSISMethod.
IJIDS2018,10,19.[CrossRef]
15. Aytekin,A.ComparativeAnalysisoftheNormalizationTechniquesintheContextofMCDMProblems.Decis.Mak.Appl.Manag.
Eng.2021,4,1–25.[CrossRef]
16. Vafaei,N.;Ribeiro,R.A.;Camarinha-Matos,L.M.ComparisonofNormalizationTechniquesonDataSetswithOutliers. Int.
J.Decis.SupportSyst.Technol.2021,14,1–17.[CrossRef]
17. Vafaei,N.;Ribeiro,R.A.;Camarinha-Matos,L.M.NormalizationTechniquesforMulti-CriteriaDecisionMaking: Analytical
HierarchyProcessCaseStudy.InTechnologicalInnovationforCyber-PhysicalSystems;Camarinha-Matos,L.M.,Falcão,A.J.,Vafaei,
N.,Najdi,S.,Eds.;SpringerInternationalPublishing:Cham,Switzerland,2016;Volume470,pp.261–269;ISBN978-3-319-31164-7.
18. Zavadskas,E.K.;Turskis,Z.ANewLogarithmicNormalizationMethodinGamesTheory.Informatica2008,19,303–314.[CrossRef]
19. Sahu,S.K.AStudyofK-MeansandC-MeansClusteringAlgorithmsforIntrusionDetectionProductDevelopment.Int.J.Innov.
Manag.Technol.2014,5,207–213.[CrossRef]
20. Ikotun,A.M.;Ezugwu,A.E.;Abualigah,L.;Abuhaija,B.;Heming,J.K-MeansClusteringAlgorithms:AComprehensiveReview,
VariantsAnalysis,andAdvancesintheEraofBigData.Inf.Sci.2023,622,178–210.[CrossRef]
21. Zolfani,S.;Yazdani,M.;Pamucar,D.;Zaraté,P.AVIKORandTOPSISFocusedReanalysisoftheMADMMethodsBasedon
LogarithmicNormalization.arXiv2020,arXiv:2006.08150.[CrossRef]
22. Magableh,G.M.;Mistarihi,M.Z.AnIntegratedFuzzyMCDMMethodforAssessingCrisisRecoveryStrategiesintheSupply
Chain.Sustainability2024,16,2383.[CrossRef]
23. Nabeeh,N.A.;Abdel-Basset,M.;Gamal,A.;Chang,V.EvaluationofProductionofDigitalTwinsBasedonBlockchainTechnology.
Electronics2022,11,1268.[CrossRef]
24. Xia,J.-Y.;Li,S.;Huang,J.-J.;Yang,Z.;Jaimoukha,I.M.;Gündüz,D.Metalearning-BasedAlternatingMinimizationAlgorithmfor
NonconvexOptimization.IEEETrans.NeuralNetw.Learn.Syst.2023,34,5366–5380.[CrossRef]
25. An,X.-K.;Du,L.;Jiang,F.;Zhang,Y.-J.;Deng,Z.-C.;Kurths,J.AFew-ShotIdentificationMethodforStochasticDynamical
SystemsBasedonResidualMultipeaksAdaptiveSampling.ChaosInterdiscip.J.NonlinearSci.2024,34,073118.[CrossRef]
26. Fang,P.;Gao,Z.;Tsay,R.S.SupervisedKernelPrincipalComponentAnalysisforForecasting.Financ.Res.Lett.2023,58,104292.
[CrossRef]
27. Yang,R.-S.;Li,H.-B.;Huang,H.-Z.MultisourceInformationFusionConsideringtheWeightofFocalElement’sBeliefs:AGaussian
KernelSimilarityApproach.Meas.Sci.Technol.2024,35,025136.[CrossRef]

Appl.Sci.2025,15,4044 21of21
28. Jin,H.;Tian,S.;Hu,J.;Zhu,L.;Zhang,S.RobustRatio-TypedTestforLocationChangeunderStrongMixingHeavy-TailedTime
SeriesModel.Commun.Stat.-TheoryMethods2025,1–24.[CrossRef]
29. Zhou,M.;Zhao,X.;Luo,F.;Luo,J.;Pu,H.;Xiang,T.RobustRGB-TTrackingviaAdaptiveModalityWeightCorrelationFilters
andCross-ModalityLearning.ACMTrans.Multimed.Comput.Commun.Appl.2024,20,1–20.[CrossRef]
30. Peng,Y.; Zhao,Y.; Dong,J.; Hu,J.AdaptiveOpinionDynamicsoverCommunityNetworksWhenAgentsCannotExpress
OpinionsFreely.Neurocomputing2025,618,129123.[CrossRef]
31. Zhu,C.AnAdaptiveAgentDecisionModelBasedonDeepReinforcementLearningandAutonomousLearning.J.Logist.Inform.
Serv.Sci.2023,10,107–118.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.