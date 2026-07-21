---
conversion_metadata:
  converted_at: "2026-07-21T05:35:35Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Bauer A. et al.pdf"
  source_pdf_sha256: "76b0e4e1f872fc64472573aa660235f606f99c868abae5e32d1306f15242bf7b"
  page_count: 103
  markdown_char_count: 420553
---

COMPREHENSIVE EXPLORATION OF SYNTHETIC DATA
GENERATION: A SURVEY
AndréBauer SimonTrapp,MichaelStenger,RobertLeppich,SamuelKounev
UniversityofChicago UniversityofWürzburg
Chicago,UnitedStatesofAmerica Würzburg,Germany
andrebauer@uchicago.edu {firstname}.{lastname}@uni-wuerzburg.de
MarkLeznik KyleChard,IanFoster
UniversityofUlm ArgonneNationalLaboratory
Ulm,Germany Lemont,UnitedStatesofAmerica
mark.leznik@uni-ulm.de {lastname}@anl.gov
ABSTRACT
RecentyearshavewitnessedasurgeinthepopularityofMachineLearning(ML),appliedacross
diversedomains. However,progressisimpededbythescarcityoftrainingdataduetoexpensive
acquisitionandprivacylegislation.Syntheticdataemergesasasolution,buttheabundanceofreleased
modelsandlimitedoverviewliteratureposechallengesfordecision-making. Thisworksurveys417
SyntheticDataGeneration(SDG)modelsoverthelastdecade,providingacomprehensiveoverview
of model types, functionality, and improvements. Common attributes are identified, leading to a
classificationandtrendanalysis. Thefindingsrevealincreasedmodelperformanceandcomplexity,
with neural network-based approaches prevailing, except for privacy-preserving data generation.
Computer vision dominates, with GANs as primary generative models, while diffusion models,
transformers, and RNNs compete. Implications from our performance evaluation highlight the
scarcityofcommonmetricsanddatasets,makingcomparisonschallenging. Additionally,theneglect
oftrainingandcomputationalcostsinliteraturenecessitatesattentioninfutureresearch. Thiswork
servesasaguideforSDGmodelselectionandidentifiescrucialareasforfutureexploration.
Keywords Survey·Synthesis·SyntheticDataGeneration
1 Introduction
Inrecentyears,ArtificialIntelligence(AI),particularlyinsubfieldslikeMachineLearning(ML)andDeepLearning
(DL),hasexperiencedsignificantgrowthandpopularity[1,2]. AsMLandDLmodelshaveevolvedincomplexityand
efficiency,apersistentchallengehasbeenthelimitedsizeoftrainingdatasets. Thislimitationstemsfromhighlabeling
costsandprivacyconcerns,hinderingthemodel’sabilitytogeneralizeeffectively. Toaddressthisissue,Synthetic
DataGeneration(SDG)emergesasaviablesolution,providingsubstantialamountsofartificialdataformodeltraining.
Thisartificialdataincludesnovel, diverse, andrealisticsamples, alleviatingtheconstraintsimposedbytraditional
datasets[2].
Broadlyspeaking,SDGinvolvesgeneratingartificialdataandlabels,aimingtoemulateauthenticsamplesclosely. This
processisautomatedbyutilizinggenerativemodelsthatestimatetheprobabilitydistributionoftheirtrainingdata. This
setsitapartfromdataaugmentation,whichmanipulatesexistingdata,asSDGgeneratesnewdatabysamplingfrom
learneddistributions. Theadvantagesofsyntheticdatagobeyondmerecostreduction,withitson-the-flygeneration
contributing to reduced computational time and addressing bias in data distribution. Synthetic data proves highly
valuablewhenrealdataisinsufficient,costlytolabel,orexhibitsbiaseddistributions.
Theconceptofsyntheticdatadatesbacktothe1960sandhasevolvedalongsidethebroaderAIlandscape. However,the
dynamicnatureofSDG,withnewapproachesemergingannually,posesachallengeforresearchers,especiallythose
4202
beF
1
]GL.sc[
2v42520.1042:viXra

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
newtothefield. ExistingliteratureonSDGoftenlacksacomprehensiveoverviewandclassificationofapproaches,
makingitdifficulttostaycurrentwithgenerativemodels,theirapplications,andtherelationshipsbetweenthem. Recent
studieshavesummarizedtheliteratureonspecificmodeltypessuchasGenerativeAdversarialNets(GANs)[3,4]
andcomputer-renderedvirtual3Denvironments[5,6]. Otherworksconcentrateondistinctdomains,includinggraph
generation [7], computer vision [8, 9], text generation [10], music [11], privacy [12], and molecular science [13].
Additionally, somerelatedliteraturehasundertakenthetaskofcompiling, comparing, orclassifyingvariousSDG
approachescomprehensively[14,15,16,17,2]. However,theseworkshavelimitationsinscope,oftenoverlooking
recentadvancementssuchasself-attention[18]. Theymayfocusexclusivelyonasingledomain,classifymodelsbased
ononlyafewaspects,orprovidecoarsecoverageofliteratureandmodelarchitecture.
Toaddressthesegapsintheexistingliterature,thisworkendeavorstoprovideacomprehensiveoverviewofSDG.
Moreprecisely,thecontributionsofthisworkinclude:
1. Surveying Literature: We conduct an extensive survey of the literature from the last decade, aiming to
comprehensivelycoverallmodeltypessuitableforSDG. Ourinvestigationinvolvesscrutinizing417models,
revealing20distinctmodeltypes,furthercategorizedinto42subtypes.
2. ExploringApplicationsandEnhancements: Withinthissurvey,wedelveintotheapplicationsandenhance-
mentsoftheidentifiedSDGmodeltypes,providinginsightsintotheirrespectivepracticalimplementations.
3. IntroducingClassificationCategories: Inadditiontomodelidentification,weintroducevariouscategories
forclassifyingthecollectedgenerativemodels. Thesecategoriesincludegenerateddatatypes,performance,
privacyconsiderations,andtrainingprocesses.
4. KnowledgeFoundation:Theacquiredknowledgefromthisexplorationservesasasolidfoundation,providing
acomprehensiveunderstandingofthediverselandscapeofSDGmodeltypes.
5. GuidelineDevelopment: Buildinguponthisfoundation,wedevelopapracticalguideline. Thisguidelineis
tailoredtofacilitatetheselectionofanappropriateSDGmodeltype,offeringvaluableinsightsforresearchers
andpractitionersinthefield.
Oursurveyof417SDGmodelsrevealsnotabletrends.Weclassifiedthesemodelsbasedonovertencriteria,demonstrat-
inganevidentincreaseincomplexityandperformanceovertheyears. Theevolutionismarkedbytheshiftfromsimpler
probabilisticmodelslikeMarkovchainsandBayesianNetworks(BNs)tomoresophisticatedneuralnetwork-based
approaches. Notably,intherealmofSDG,computervisionstandsoutasthemostpopularapplicationfield. GANs
anddiffusionmodelshaveemergedastopperformersinthisdomain. Forhandlingsequentialdata,suchasmusic
ortext,RecurrentNeuralNetworks(RNNs)dominate. Additionally,privacy-preservingdatagenerationcommonly
employsmodelslikeMarkovchains,BNs,andmoreadvancedGANs. Theworkalsohighlightschallengessuchas
non-standardizedevaluationmetricsanddatasets,offeringsolutionslikebuildinggraphsofpredecessorsbasedonthe
models’performanceevaluations[19].
Weareconvincedthatourworkcanserveasavaluableresourcefornewcomersandexperiencedresearchers,providing
anupdatedoverviewoftheSDGlandscapeandaidinginidentifyingsuitablemodelsanddatasetsforspecifictasks.
Furthermore,wepresentthefirstcomprehensiveclassificationofnumerousmodelimplementationsspanningmultiple
domains,facilitatingtheidentificationofstrengthsandweaknessesinthesemodels.
Theremainderofthisworkisstructuredasfollows: InSection2,weintroduce42differentSDGmodeltypesand
highlighttheirusageinliterature. InSection3,weclassifyandcomparethefoundgenerativemodelsaccordingto
differentcategoriesbeforediscussingaguidelineforchoosingwhichSDGmodeltypeissuitableforagivenscenario.
InSection4,reviewexistingsurveysanddistinguishthescopeofourstudyfromexistingsurveys. InSection5,we
concludeourpaper. InAppendixA,welistallusedacronyms.
2 OverviewofGenerativeModels
Various approaches exist to generate synthetic data, ranging from models based on graphs or simple probabilistic
assumptionstodeepneuralnetworks. Thefollowingsectionsdescribethedifferentavailablemodelarchitecturesin
generalandprovideachronologicaloverviewoftherecentliteratureregardingtheusageofthesemodelsforSDG. The
structureisinspiredbytheworkdonebyHarshvardhanetal.[16]andextendedfurthertoincludemissingmodels
andsomenovelandimportantimplementationswefound. Wefocusonapproachesreleasedinthelasttenyearsto
keepthisworkwithinviableandreasonablebounds. Wemainlyrestrictourselvestomodelsreferencedbytheworks
mentionedinSection4,extendedbysomeoftheiroften-citedliteratureandadditionalmaterialfromourresearchon
GoogleScholar.
2

| ComprehensiveExplorationofSyntheticDataGeneration: |     |     | ASurvey |     |     |
| -------------------------------------------------- | --- | --- | ------- | --- | --- |
2.1 GaussianMixtureModels
Gaussian Mixture Models (GMMs) are density estimation algorithms mostly used for data clustering but can also
beusedasagenerativeprobabilisticmodel. AGMMconsistsofN Gaussiandistributions(components),whichare
normal distributions that are continuous for a real-valued random variable and symmetric about their mean. Each
Gaussiancanbecharacterizedbyameanµ andavarianceρ andhasaprobability/weightπ inthemixturemodel
|     |     | i   | i   |     | i   |
| --- | --- | --- | --- | --- | --- |
(cid:80)N π =1. Forone-dimensionaldata,π andµ arenumbers,butintwo-dimensionalspace,π
| sothat | i   |     | i i |     | i isavector, |
| ------ | --- | --- | --- | --- | ------------ |
i=1
andµ i isacovariancematrix. TheprobabilityofadatapointdbelongingtotheclusterrepresentedbyGaussianiis
P(d=i)=π andtheobservationlikelihoodofdinGaussianiisP(d|d=i,µ ,ρ )=N(d|µ ,ρ )whereN(.)isthe
|     | i   |     |     | i i | i i |
| --- | --- | --- | --- | --- | --- |
normaldistributionfunction. [16]
(a) One-dimensional GMM with three components. (b)AGMMwith16componentsmappedtotwo-dimensional
| (Source:[16]) |                                                               |     | data.(Source:[20]) |     |     |
| ------------- | ------------------------------------------------------------- | --- | ------------------ | --- | --- |
|               | Figure1: IllustrationsofGMMsusedforoneandtwo-dimensionaldata. |     |                    |     |     |
TomapdatapointstoN clusters/componentsofaGMMduringtraining,anexpectation-maximization(EM)algorithm
isused:
| 1. Choose(random)locationsµ |     | andshapesρ | foreachcomponent |     |     |
| --------------------------- | --- | ---------- | ---------------- | --- | --- |
|                             |     | i          | i                |     |     |
2. Repeatuntilconvergence:
|     | (a) E-step: Foreachdatapoint,findπ |     | encodingthemembershipprobability |     |     |
| --- | ---------------------------------- | --- | -------------------------------- | --- | --- |
i
|     | (b) M-step: Foreachcluster,updateµ |     | ,ρ andπ basedonalldatapoints |     |     |
| --- | ---------------------------------- | --- | ---------------------------- | --- | --- |
|     |                                    | i   | i i                          |     |     |
MultipleGMMscanbeinitializedwithdifferentrandomvaluestoreducethechanceofmissingthegloballyoptimal
solution. [20].
VanderOord[21]proposeadeepGMM,whichcontainsmultiplelayersoflineartransformationsx=Az+bapplied
tothenormalvariablez ∼N(0,I ). Foreachsample,arandompaththroughthegraphistaken(seeFigure2),andthe
n
transformationsareconcatenated. Intheory,deepGMMscanberepresentedbynormalGMMs,buttrainingwouldbe
morecomplex,andthedeepmodelsgeneralizebetter. ThemodelistrainedwithanEMalgorithmandparallelizableby
design. Itscapabilitiesaredemonstratedbygeneratinglow-resolutiongreyscaleimages.
ZenandSenior[22]appliedmixturedensitynetworksforspeechsynthesistoenablemultimodalregressionandthe
predictionofvariances. Tothisend,theauthorsmodeltheconditionalprobabilitydistributionusingaGMM,with
parameterspredictedbyafullyconnectedmulti-layerneuralnetwork.
VanderPlas[20]demonstrateshowGMMscanbefittedwellontwo-dimensionaldata(seeFigure1b)bytryingdifferent
componentsizesN andsearchingforthemodelwiththeoptimalAkaikeinformationcriterion(AIC)orBayesian
informationcriterion(BIC). SyntheticdatacanbeobtainedfromthistrainedmodelbyrandomlyselectingaGaussian
according to probability π and sampling from its normal distribution. The author uses this approach on binary
i
black-and-whiteimagesofhandwrittendigitsandgeneratesauthenticartificialsamples.
3

| ComprehensiveExplorationofSyntheticDataGeneration: |        |     |     | ASurvey  |         |     |
| -------------------------------------------------- | ------ | --- | --- | -------- | ------- | --- |
|                                                    | N (0,I | )   |     | N (0,I ) | N(0,In) |     |
|                                                    | n      |     |     | n        |         |     |
A1,1 A1,2 A1,3
|     | A   |     | A   | A A | A2,1 A2,2 |     |
| --- | --- | --- | --- | --- | --------- | --- |
|     |     |     | 1   | 2 3 |           |     |
A3,1 A3,2 A3,3
|     | x           |     |     | x      | x          |     |
| --- | ----------- | --- | --- | ------ | ---------- | --- |
|     | (a)Gaussian |     |     | (b)GMM | (c)DeepGMM |     |
Figure 2: Comparison between a Gaussian, GMM and a deep GMM with transformation biases b not shown.
i,j
(Source:[21])
2.2 KernelDensityEstimators
KernelDensityEstimatorss(KDEs)aremodelsthatapproximatetheprobabilitydensityfunctionp(X =x)ofarandom
variableX inbetweenasetofobservations. Forobservationsx andanoptimizablesmoothingparameterh>0,the
i
densityestimationisdefinedas
n
|     |     |     |        | 1 (cid:88) |     |     |
| --- | --- | --- | ------ | ---------- | --- | --- |
|     |     |     | pˆ(x)= | K(x−x ,h)  |     | (1) |
n i
i=1
withapositivekernelfunctionK(y,h),forwhichvariousimplementationsexist. OnekerneloftenusedistheGaussian
kernelK(y,h)=exp(− y2 ),butmanyothersareavailabletomodeldifferentkindsofdata. [23]
2h2
Bhattacharyaetal. [23]synthesizePhotoplethysmograms(PPGs),whicharetimeseriesovervolumetricbloodflowin
thehumanbody,bydecomposingitintocomponents(pulselength,peakposition,amplitude,etc.),trainingaKDEfor
eachcomponentandsamplingfromtheresultingprobabilitydistributions,fromwhichnewPPGscanbeconstructed.
2.3 MarkovChainModels
OrdernMarkovchainsareprobabilisticmodelsforinfinitesequencesofsymbolswheretheprobabilityforeachsymbol
onlydependsonthepreviousnsymbols[11]. Forn=1,theycanbedrawnasagraphwiththestates(symbols)as
nodesandthetransitionprobabilitiesa =P(x =t|x =s)asedges(seeFigure3). Theprobabilityofawhole
|     |     | st  | i   | i−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- |
sequencecanbecomputedbyapplyingP(X,Y)=P(X|Y)P(Y)manytimes;thatis,theprobabilityofasequencex
(cid:81)L
| withlengthLisP(x)=P(x |     | ) a | . [24] |     |     |     |
| --------------------- | --- | --- | ------ | --- | --- | --- |
1 i=2 xi−1xi
A B
|     | A   | B   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
B E
C D
|     | C   | D   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
(a)Anorder1Markovchain. (b)Anorder1Markovchainwithstartandendstate.
Figure3:IllustrationsofgraphsofMarkovchainswithsymbolsasnodesandtransitionprobabilitiesasedges. (Adapted
from: [24])
4

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
TheadvantageofMarkovchainsistheirsimplicity. Theycanbeeasilyunderstoodbecausetheconditionalprobabilities
canbecomputedbycountingrelativesymbolappearances. Further, theycanbeinterpretedasautomataonwhich
additionalcontrolmechanismslikeMarkovconstraintsandfactorgraphscanbeimposed. Onthedownside,simple
order1modelscannotcapturelong-termtemporalstructures,andordernmodelstendtooverfit,requiresignificantly
biggeramountsoftrainingdata,andneedtocomputeexponentiallymoreconditionalprobabilitiesforlargen. [11,25]
Pachetetal. [26]introducetheContinuator,asystemforinteractivemusicgenerationintheuser’sstylewithouta
priorimusicalknowledge,allowingamusicianto“jam”inreal-timewiththecomputer. TheContinuatorispowered
byananalysismoduleandagenerator. Theanalysismodulefirstdetectstheendsofmusicalphrases,thenbuildsa
Markovianmodelofthesephrasesanddetectsglobalpropertiesliketempo,meter,andnotedensity. Thegeneratoruses
theMarkovmodelandthepropertiestogeneratemusicintheinputstyleandcontinueitnote-by-note.
2.3.1 HiddenMarkovModels
HiddenMarkovModels(HMMs)areextensionsofMarkovchainswheretheMarkovchainstatesequenceπishidden
and each hidden state k has emission probabilities e (b) = P(x = b|π = k) for the observable symbols x (see
k i i
Figure4a). ThismodelcandepictmanyissueswithreducedcomplexitycomparedtosimpleMarkovchains,butthe
inference of hidden states π for observation x with joint probability P(x,π) = a
(cid:81)L
e (x )a is more
0π1 i=1 πi i πiπi+1
complex(seeforexampleFigure4b). Themostprobablestatesequenceπ∗ =argmax P(x,π)foranobservationx
π
canberecursivelycomputedwiththeViterbialgorithm. [16,24]
(b)HMMofadishonestcasinoswitchingbetween
(a)ArchitectureofanHMM.(Source:[16]) fairandunfairdices.(Source:[24])
Figure4: IllustrationsofHMMs.
Durbinetal. [24]useHMMstomodelbiological(genetic)sequencesanddemonstratethelabelingofunannotated
andgenerationofnewdataforthistopic. Theyshowthatthesesimplemodelscanlearntruthfulmodelsevenfrom
observationswherethehiddenpathsareunknownusingtheBaum-WelchandViterbialgorithms. Theyalsodiscuss
differentmodeltopologiesfordifferentsequencelengthsandfindthecarefultopologyconstructionofaHMMvalidated
byhumanexpertstobeessentialforgoodmodelperformance.
Racyzn´skietal. [27]interpolateresultsusingmultiplelearnedsub-models(namely,abigramMarkovchainmodel
P(C |C ),atonalityrelationP(C |T ),andamelodyrelationmodelP(C |M ))tosequentiallygeneratechordsC
t t−1 t t t t i
asaccompanimentformusic.
Kaliakatsos-Papakostasetal. [28]proposetheconstrainedHMM(CHMM),whichallowsintermediatestatesofthe
sequencetobefixedtoaspecificvalue(anchorchords)withprobability1. Then,theViterbialgorithmisusedtofind
themostlikelypathbetweenthesecheckpoints. Themodelisusedtogenerateharmonicchordsequencesforamelody
bymappingthehiddennotestatesbetweentheanchorsdefinedbythemelodytochords.
5

| ComprehensiveExplorationofSyntheticDataGeneration: |     |     |     |     |     | ASurvey |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
BindschaedlerandShokri[29]useHMMstogenerateplausibleandprivatelocationtracesbyclusteringtheavailable
locations and synthesizing a sequence of locations from the same cluster label sequence as a real seed trace. The
generatedtraceisfurtherevaluatedusingaplausibilityandaprivacy(geographicsimilaritytotheseedtrace)test.
2.3.2 N-Grams
Then-gramisatupleofnvalues,forinstance,asequenceofnwordsofasentence(w ,...,w ).
1 n Theyareusuallyused
toefficientlymodeltheprobabilitiesofwordsbasedonthealreadywrittentext:
|     |     |     |        |        | count(X       |       | t−n+1 ,...,X | t )+1 |     |
| --- | --- | --- | ------ | ------ | ------------- | ----- | ------------ | ----- | --- |
|     |     |     | p(X |X | ,...,X | )=            |       |              |       | (2) |
|     |     |     | t t−1  |        | t−n+1 count(X |       | ,...,X       | )+V   |     |
|     |     |     |        |        |               | t−n+1 |              | t−1   |     |
undertheMarkovianassumptionp(X |X ,...,X )=p(X |X ,...,X ),thatis,theprobabilityofawordat
|     |     |     | t   | t−1 | 1   | t t−1 | t−n+1 |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
positiontonlydependsonthepreviousn−1words. AddingLaplacesmoothingwiththe+1inthenumeratorandthe
wordvocabularysizeV inthedenominatoralsoallowspreviouslyunseenwordcombinationstobecreatedwithlow
probability. N-gramsarenormallyusedforlanguagemodelingandsynthetictextgeneration. [30]
Bengioetal. [31]extendtheideaofn-gramswithaMultilayerPerceptron(MLP): First,eachwordX isencodedinto
k
a1-hotvector1(X ). Then,thevectorsarelinearlyembeddedusingmatrixW ,concatenated,andfedintotheMLP,
|     | k   |     |     |     |     |     |     | x   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichistrainedtopredictthenextwordprobability. Finally,asoftmaxfunctionSM isapplied,resultingintheneural
networklanguagemodel:
|     |     | p(X |X | ,...,X    | )=SM(MLP[W |     | 1(X | ),...,W | 1(W )]). | (3) |
| --- | --- | ------ | --------- | ---------- | --- | --- | ------- | -------- | --- |
|     |     | t      | t−1 t−n+1 |            |     | x   | t−1     | x t−n+1  |     |
Barbierietal. [32]implementMarkovconstraintstogeneratelyricsinagivenstyleandrhythmformusic. Theytraina
Markovprocessusingrelativefrequenciesofn-gramsoflyrics,forexample,ofaspecificauthorandthenrestructureit
asafinite-lengthsequenceofconstrainedvariableswithassignedprobabilityforeachvalue. Theconstraintsarerelated
torhyme,rhythm,syntax(part-of-speechtemplates),andsemantics(relationsbetweenwords).
Shortoverviewofotherusagesofn-grams:
| Approach | Description |     |     |     |     |     |     |     | Year |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | ---- |
[33] ExtensionoftheconstrainedMarkovmodelfrom[32]toallowaglobalmeterconstrainttobe 2013
efficientlyimplemented.
[34] Constructionofaprobabilisticfinitestateautomatfromn-gramsofpreprocessedMIDIfilesto 2013
harmonicallyaccompanyamelody.
[35] Avoidanceofplagiarismingeneratedsequencesinhigh-orderMarkovchainswithaMaxOrder 2014
globalMarkovconstraintthatpreventschunkslongerthanMaxOrderfrombeingreplicated
fromthetrainingdatabybuildingMarkovautomatonswithrestrictedmaximumpathlengths.
[36] FlowComposer: A web tool consisting of two collaborating constrained Markov models 2016
(melodyandchords)forgeneration,re-harmonization,andinteractivecompositionofmusic
leadsheets.
[37] A multiple viewpoint system consisting of Markov chains obtained from n-grams gener- 2016
ates music. The agents are responsible for different aspects of the music and are ordered
sequentiallyandhierarchically.
2.4 BayesianNetworks
[38])ABayesianNetwork(BN)isaDirectedAcyclicGraph(DAG),aspecialtypeofgraphicalmodelinwhichrandom
variablesarethenodesanddependenciesbetweenthesevariablesaretheedges. Thedirectededgesrunfromthe“cause”
orparentnodetothe“effect”orchildnodeanddefinetheconditionaldependencyofthenodes. Eachrandomvariable
hasacontinuousordiscreteprobabilitydistributionfunction. AnexampleforaBayesianNetworkcanbeseenin
Figure5. [39]
IfwedefineV={V :j ∈{1,...,N}}asthesetofrandomvariablesofaBayesiannetwork,theprobabilitydistribution
j
ofV asp(V |Pa )andPa asthesetofparentsofV ,thejointdistributionoverVisdefinedas[41]:
| j   | j j | j   |     |     | j   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:89) N
|     |     |     | p(V)=p(V |     | 1 ,...,V N | )=  | p(V j |Pa | j ). | (4) |
| --- | --- | --- | -------- | --- | ---------- | --- | --------- | ---- | --- |
j=1
6

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
C P(R)
T .80
F .20
Rain
P(C)=.50
Cloudy WetGrass
S R P(S)
Sprinkler
T T .10
T F .50
C P(S)
F T .90
T .10
F F .00
F .50
Figure5: ExampleofaBayesianNetworkwithdiscreterandomvariables. (Source: [40])
TherearemanyalgorithmstotrainBNsunderdifferentconditionswherethenetstructureisknownorunknownin
advance, and the reference data is fully or partially observable. In the context of synthetic data, we usually either
havethetrivialcaseofavailableexpertknowledge,fromwhichthestructureofaBNcanbeconstructed,oravailable
real-worlddata,butnoinformationaboutthestructureofaBNthatcorrespondswelltothedata. Forthelattercase,
twoproblemsneedtobesolved:
1. FindingametrictocomparepotentialstructuresofBNs.
2. SearchingforpotentialBNstructuresalgorithmically.
Asolutionforthefirstproblemisprovidedbythejointprobabilityp(D,Sh)forthedataDandahypotheticalstructure
ShofaBN:
logp(D,Sh)=logp(D|Sh)+logp(Sh). (5)
TheBayesianinformationcriterion(BIC)[42]canbeusedtocalculatelogp(D|Sh)whilethepriorprobabilityp(Sh)
ofastructurecanbedeterminedforexamplebyassigningprobabilitiestoapredefinedsetofpossiblestructuresor
definingapriornetworkandmeasuringthedeviationofShfromit. [39]
Thesecondproblem,searchingforstructures,isNP-hardifdoneforallpossiblecombinations,sodifferentgreedy
algorithmsareemployed. Ingeneral,thesealgorithmsincreasep(Sh)step-wisebyperformingactionsonthegraph
(adding,removing,orreversinganedge)untilamaximumisreached. [39]
In recent years, more sophisticated learning algorithms have been developed. They use dynamic programming
[43,44,45]tosplitthegloballearningproblemintosmallsubproblems. Othersdefinethelearningtaskasashortest
pathproblemandsolveitwithanA*algorithm[46].
Youngetal. [47]useBNstoanonymizeadatasetsoitcanbedisclosedtothepublic. Theylimittheirnetworksto
discretevariablesandmapcontinuousvalues(e.g.,age)todiscreteintervalstofacilitatethelearningprocess,which
consistsofmultiplesteps:
1. Theuserdefinesapriornetworkandconditionalprobabilitydistributionsforeachnode. Also,animaginary
databaseissuppliedtogenerateconfidenceinthepriorstructure.
2. Theprobabilitydistributionsofthenodesareupdatedusingthetrainingdata.
3. Agreedysearchalgorithm[48]startsthesearchfromthepriornetwork,createsallpossiblenetworkswithone
change(edgeaddition,removal,orreversion),andselectstheonewiththehighestBayesfactor(likelihoodof
themodelaccordingtothedata)asthenewbaselineuntilnofurtherimprovementoccurs.
ThetrainedBNisnowusedasanimputationmodel[49]togeneratesyntheticdatabyconsecutivelydrawingrandom
samplesfromthenodesinthehierarchy.
7

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Suzukietal. [50]generatefixed-sizefour-part(alto,tenor,bass,soprano)symbolicharmoniesbasedonthemelodyofa
sopranovoiceandexperimentwiththeconditioningonchordnodes. Thepitchesforeachvoiceareclassifiedjointly
basedonthepreviousvalue(Markovproperty)andthecurrentsopranoorchordvalue. Thesopranonetworkwithout
chordsproducessmootherresults.
Zhangetal. [51]proposePrivBayes,adifferentiallyprivate1methodtoreleasehigh-dimensionaldatasets. First,aBN
withsuccinctattributecorrelationsiscreated. Thennoiseisinjectedintothelow-dimensionalmarginaldistributionsof
theBN,andthenownoisyapproximateddatadistributionisusedtosampleaprivatesyntheticdataset.
Draghietal. [38]approachthebiasprobleminthetrainingdataofBNsbyidentifyingunder-representedcasesand
over-samplingthemwithsyntheticdata. TheystartbytrainingaBNonasubsetoftheoriginaldata,modifyingit,and
generatinganewbiaseddataset. Then,aBNistrainedonthisbiaseddataandgeneratesthedatasetD withthe
bias
samesizeastheoriginal. Next,aclassifieristrainedonD andtriestopredictvaluesfromavalidationset,whichis
bias
asubsetoftheoriginaldataandaddssampleswithanuncertainoutcome(lowprobability)toadatasetD . Finally,
unc
theBayesBoostisperformedbygeneratingmsimilarsamplesforeachsampleinD withaBNtrainedonD and
unc bias
addingtheresultstoD ,resultinginanewlessbiaseddataset.
bias
ShortoverviewofotherusagesofBNs:
Approach Description Year
[53] TrainingaBNonmotioncapturedatatoproducerealistichuman3Dposesthatarerendered 2016
withdifferenttextures(e.g.,clothes)toproducetrainingdataforhuman3Dposeestimation.
[54] DataSynthesizer: CreatingaBayesianNetworkfromdatawithaDataDescriber,injecting 2017
noiseintothedistributionsandsamplingfromitwiththeDataGenerator. TheModelInspector
comparesthepropertiesofthesyntheticdatatotherealone.
[55] Modelingheterogeneous(continuousanddiscretevariables)medicalpatientdataasaBNto 2020
beabletoincorporateexpertknowledgeandgenerateprivatedatasets. Theyexperimentwith
threewaystodealwithmissingvalues: Deletingtheentireentry,adding“missstates/nodes”
totheBN,andusingtheFCIalgorithm[56]toinferthemissingvariables. Usingprobabilistic
graphical modeling, the model produces high-fidelity results with a low risk of patient re-
identification(cloningoftrainingdata).
[38] Exploringthedatabiasproblemandunder-representationinunderlyinggroundtruthsamples. 2021
Specifically,itisanimportantprobleminmedicaldata,wheresyntheticdatagenerationisused
tomasksensitivepatientdata. Theauthorsproposeanapproachtoidentifyingunder-sampled
dataandimprovingdatasynthesistocorrectthisproblem.
2.5 GeneticAlgorithms
Genetic Algorithms (GAs) are ML algorithms that mimic the natural selection process over time. The population
consistsofacrowdofindividualsateachtimesteporgeneration. Tocreatethepopulationforthenextgeneration,
threeactionsareperformed:
Selection Selectionofsuitablecandidatesfromthepopulation,usingafitnessfunctiontoeliminateworsecandidates
andincreasethechanceofsurvivalofbetteronessotheycanpassontheirgoodproperties. Individualscanbe
selectedmultipletimestomaintainpopulationsize.
Crossover Informationexchangebetweencandidates.
Mutation Perturb the candidates’ information by randomly changing some properties, usually according to some
distribution.
Thisgenerationprocess(illustratedinFigure6)continuesuntilthesystemconverges(i.e.,allcandidatesareidentical)
orauser-definedcriterionismet. ThespeedoftheGAmodelismeasuredbythenumberofgenerationsneededtomeet
therequirements. [57]
LiuetTing[59]useaGAforpolyphonicaccompanimentgenerationgivenadominantmusicmelody. Theyremovethe
impracticalneedforahumanevaluationcriterionofpreviousapproachesbybuildingafitnessfunctionbasedonmusic
theory.
You et Liu [58] propose a GA that finds similar and suitable chord variations for a given target melody and some
examplechordprogressionsfromothersongsprovidedasMIDIfiles. Theinitialpopulationconsistsoftheexemplar
1Differentialprivacyintroducesrandomnesstothedataprovisionprocess,resultingin“plausibledeniabilityofanyoutcome”[52]
8

| ComprehensiveExplorationofSyntheticDataGeneration: |     |     | ASurvey    |     |         |     |
| -------------------------------------------------- | --- | --- | ---------- | --- | ------- | --- |
|                                                    |     | Yes |            |     | Initial |     |
|                                                    |     | End | Converged? |     |         |     |
population
No
|     | Fitness  |               | Crossover                    |     | Mutation |     |
| --- | -------- | ------------- | ---------------------------- | --- | -------- | --- |
|     | Figure6: | ProcessofaGA. | (Adaptedfrom[58]andmodified) |     |          |     |
chordpatternswithkeysshiftedtomatchthekeyofthetargetmelody. Thefitnessfunctionandcrossoverprocess
furtherincorporatemusictheorytoensurethattheevolvingchordpatternsharmonizewiththemelodyandconformto
basicrules.
Chenetal.[57]implementaGAforcategoricaltabulardatawithnon-hierarchicalvariables.Theystartbyindependently
computingtheunivariatedistributionsofallcolumnsoftheoriginaldata;then,theysampleauser-definedamountof
synthetictablesfromthesedistributions,whicharethepopulationofthefirstgeneration.TheGAprocessthenoptimizes
thestatisticsofthedatasetsiterativelyuntilthedesiredsimilaritytotheoriginaldataisreached. Thecomputational
workloadoftableGAsissignificantlyhigher,andtheyaremoreerror-pronethanGAsforstringdataduetotheincrease
invariablesandtheirrelationships.
2.6 BoltzmannMachines
A Boltzmann machine is an undirected network consisting of binary visible nodes v ∈ {0,1}D and hidden nodes
h∈{0,1}P. Themodelparametersθ ={W,L,J}arethevisible-to-hidden,visible-to-visibleandhidden-to-hidden
ThemodelparametersθofaBoltzmannmachine
symmetricinteractionterms(matrices)ofthegraph(seeFigure7).
aretrainedusinggradientascent. Theyassignprobabilitiestothevisibleunits,wherethetrainingdataisputin,based
| onthestatesofthehiddenunits. | [60] |     |     |     |     |     |
| ---------------------------- | ---- | --- | --- | --- | --- | --- |
J
| h   |     | h   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
h3
W3
h2
|     | W   |     |     | W   |     | W2  |
| --- | --- | --- | --- | --- | --- | --- |
h1
W1
| v   |     | v   |     |     | v   |     |
| --- | --- | --- | --- | --- | --- | --- |
L
(a)ArchitectureofaGeneralBoltzmann (b)ArchitectureofaRestrictedBoltz- (c)ArchitectureofaDeepBoltzmann
| Machine. |                                                   | mannMachine. |     |     | Machine.       |     |
| -------- | ------------------------------------------------- | ------------ | --- | --- | -------------- | --- |
| Figure7: | ArchitecturesofdifferentkindsofBoltzmannmachines. |              |     |     | (Source: [60]) |     |
2.6.1 RestrictedBoltzmannMachines
RestrictedBoltzmannMachines(RBMs)[61]areasubsetofgeneralBoltzmannmachines,whereonlyvisible-to-hidden
(W)connectionsareallowed,sobothJandLaresettozero. Thesemodelshavetheadvantagethatinferenceisexact,
andlearningissignificantlymoreefficient[60]. ThemethodusedtotrainaRBMisunsupervisedlearning,sothedata
isunlabeled. Eachtrainingsampleisprovidedasinputvandθismodifiedtoincreasethelikelihoodfunctionp(v,θ)
using,forexample,agradientmethodorContrastiveDivergence[62].
Leeetal. [63]extendtheRBMwithconvolutionfilterstoprocesstwo-dimensionalhigh-resolutionimages. Thevisible
inputunitsofsizeN ×N areprocessedbyK filterswithsizeN ×N toproduceK hiddenlayerswithsize
| V   | V   |     |     | W W |     |     |
| --- | --- | --- | --- | --- | --- | --- |
9

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
N ×N . EachhiddenlayeristhenpartitionedintoC×C blocksthatareeachconnectedtoexactlyonebinaryunit
H H
inthemax-poolinglayerP toshrinktherepresentation. ThearchitectureisdepictedinFigure8.
N
pk Pk (pooling layer)
P α
N H C hk i,j Hk (detection layer)
Wk
N V N W v V (visible layer)
Figure 8: The convolutional RBM architecture with only one of the K hidden and max-pooling layers shown for
readability. (Source: [63])
Lattneretal. [64]proposeamulti-componentmodeltogeneratemusicwithconsistentlocalandglobalstructural
properties. First,aconvolutionalRBM[63]learnsthelocalstructureofmusicalpiecesbasedontrainingdata. Then,
constrained sampling is applied to a randomly initialized “piano roll” music representation matrix v ∈ [0,1]T×P
consistingofprobabilitiesofactivepitches1<p<P overtimesteps1<t<T: Thesamplingprocessfirstapplies
20gradientdescentstepstovwithalossfunctioninvolvingself-similarity,tonalityandmeterconstraintsregarding
atemplatepiecex∈[0,1]T×P beforeperformingalternatingstepsofGibbssampling2withtheconvolutionalRBM
andonestepofgradientdescentwithlowerlearningratetov. Thisprocessisrepeateduntilthesolutionnolonger
improvesontheRBMandconstraintsjointly.
2.6.2 DeepBeliefNetworks
ADeepBeliefNetwork(DBN),similartoitssuccessorDeepBoltzmannMachine(DBM)(seeSection2.6.4),isa
combinationofmultipleRBMs,wherethehiddenlayerofoneRBMbecomestheinput(visiblelayer)ofthehigher-level
RBM,butonlythetoptwohiddenlayersareundirectedandformanassociativememorywhilethelowerlayersforma
DAG(seeFigure9). LiketheRBM,theDBNcanbeusedtolearnhigh-levelrepresentationsofunlabeleddataand
convertrepresentationsbacktovisibledata(e.g.,images),butitcanalsobeextendedtosupervisedlearningtasksby
appendingthelabelasaninputtothevisiblelayer. [65]
h3
W3
h2
W2
h1
W1
v
(a)ArchitectureofaDeepBeliefNet- (b)ArchitectureofaDeepBoltzmann
work. Machine.
Figure9: ComparisonofthearchitecturesofaDBNandaDBM. (Source: [60])
Thelayer-wisegreedylearningprocessstartsbytrainingthelowest-levelRBMwiththevisibleandfirsthiddenlayer
normally. Then,theoutputofthefirsthiddenlayerbecomestheinput(visiblelayer)ofthenextRBM,andnowthe
secondmodelistrained. Thiscontinuesuntilasufficientnumberoflayersarereached. Thesecondstepintroducesa
2GibbssamplingisaMarkovchainMonteCarlo(MCMC)algorithmusedforapproximatestatisticalinferencethatiteratively
samplesfromtheconditionalprobabilitydistributionofeachvariableinamultivariatedistributionwhileholdingtheothersfixed.
10

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
fine-tuningalgorithmwithabottom-upandatop-downpass. Now,the“recognition”weightsW⊤ and“generative”
x
weightsW aredecoupledandmodifiedindependently. Duringthebottom-uppass,fixedrecognitionweightsareused
x
tostochasticallydetermineallhiddenvaluesandupdatethegenerativeweightsonthedirectedconnectionsaccordingto
alikelihoodmetric. Thetop-downpassstartswithastateofthetop-levelassociativememoryandusesfixedgenerative
weightstodeterminethevisiblelayersonwhichtherecognitionweightsareupdatedsimilarly. [65]
Hinton et al. [65] use alternating Gibbs sampling [66] in the DBN’s associative memory “until the Markov chain
convergestotheequilibriumdistribution”. Then,imagesofdigitsaregeneratedintheDBNthatwastrainedonthe
MNIST dataset by drawing a sample from this distribution and passing it down the generative weights. By fixing
thelabelunits,certaindigitscanbesyntheticallygenerated,andwithrepeatediterationsofGibbssamplingbetween
down-passes,thedigitsbecomemorerealistic.
Leeetal. [63],whointroducedconvolutionalRBMs,stacktheseontopofoneanothertocreateconvolutionalDBNs.
Differentfrom[65],theyuseundirectedconnectionsbetweenalllayers,likeDBMs. Theexperimentalresultswitha
two-layerconvolutionalDBNontheKyotonaturalimagedatasetshowthatthefirstlayerlearnsedgefiltersandthe
secondfiltersforcontours,corners,angles,andsurfaceboundaries. Thehierarchicalrepresentationsobtainedfrom
theselayersimproveclassificationresultsontheCaltech-101objectandMNISTdigitclassificationtasks.
Bickermanetal. [67]applyDBNstocreatejazzmelodiesinanunsupervisedmanner. Theydivideeachbeatinto12
slots,eachconsistingof30bits(12chords,18melodies)thatencodethenotepitch,octave,andlength. Atwo-layer
DBN can produce short stylistically plausible jazz samples based on a random sequence input but cannot capture
regularitiesinmusic. OtherproblemsarethelargetrainingtimeandcomplicatedsamplingprocedureofDBNs.
Sun[68]employstwoDBNs(oneflipped)withpair-wisepre-trainedlayersasanautoencodertogeneraterandom
pianorollbarsofmusicfrombinarypianorollmatrices(rowsrepresentnotepitches,columnsa16thnoteofplaying
time)ofcompleteorincompletemusic. Onaverage,thenetworkcopies56,9%ofthenotesduringthereconstruction,
whichstillresultsinnoticeablydifferentworksbeingcreated.
2.6.3 TemporalRestrictedBoltzmannMachinesandRelatedModels
TheTemporalRestrictedBoltzmannMachine(TRBM)[69]isasequenceofRBMswherethebiasesofoneRBM
dependonthehiddenstateofthepreviousRBM(seeFigure10). TrainingthemodelworkssimilartoanormalRBM,
butonsequencesinsteadoffixed-sizesamples. AsignificantproblemofTRBMsisthatforcomputingprobabilities
duringinference,theevaluationofallpossiblestates(partitionfunctions)oftwoRBMsisrequired,makingaheuristic
approachnecessary[70].
Figure10: ArchitectureofaTRBM. (Source: [70])
RecurrentTemporalBoltzmannMachines(RTRBMs)[70]areslightlymodifiedTRBMswhichofferexactinference
andfeasiblegradientcomputation. RTRBMscanbeexpressedasaRNNwiththesameparametersastheRTRBMand
itslog-likelihoodasthecostfunction,sogradientscanbecomputedusingtheBackpropagationThroughTime(BPTT)
algorithm.
TheStructuredRecurrentTemporalBoltzmannMachine(SRTRBM)[71]learnsadependencystructurebetweenpairs
ofvisibleandhiddenunitsinsteadofusingfullconnectivityliketheRTRBM. Themodelencouragessparsegraphsand
canrevealthestructureoftheunderlyingtime-seriesdata.
Sutskeveretal. [69],theoriginalauthorsoftheTRBM,traintheirmodelon10,000videosequenceswith100frames
andachievegoodresultsonfutureframepredictionandonlinedenoising(removingartifacts). Intheirlaterworkon
RTRBMs[70],theyimproveonthevideogenerationtask.
Mittelmann et al. [71] compare their SRTRBM to the previously proposed models by Sutskever et al. [69, 70] by
predictingframesonsyntheticbouncingballvideos. Further,theyusetheSRTRBMtomakepredictionsonmotion
captureandweatherdata. Theyimproveontheperformanceofthepredecessorsinalltemporalmodelingtasks.
11

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
2.6.4 DeepBoltzmannMachines
ADBM[60]isacombinationofmultipleRBMswherethehiddenlayerofoneRBMbecomesthevisiblelayerofthe
nextone,resultinginamodelwithonevisibleandastackofmultiplehiddenlayers(seeFigure9). Usingagreedy
layer-wiselearningapproach,suchamulti-layermodelcanefficientlylearnhigh-levelrepresentationsfromunlabeled
data.
Salakhutdinovetal.[60]useaDBMtrainedontheMNISTdatasettogeneratesynthetichandwrittendigitsbyinitializing
themodelwithrandombinarystatesandrunningaGibbssamplerfor100,000steps. Further,theydemonstratethe
creationofgreyscaletoyimagesontheNORB[72]datasetandimprovetheresultsbyincreasingtheamountoftraining
datawithsimplepixeltranslations.
2.6.5 GatedBoltzmannMachines
A gated Boltzmann machine encodes transformations between two observations using its hidden layer. It can be
describedasaconditionalRBMwithavisibleinputx,ahiddentransformationrepresentationlayerhthatactsasa
gate(seeFigure11)andavisibleoutputlayery. Conditionalontheinput,theinferenceandlearningproceduresare
tractable[73]. Thetrainableparametersarestoredinathree-dimensionalparameter“tensor”Wandthecompatibility
betweenx,yandhiscomputedbyanenergyfunctionE(y,h;x)[74]:
(cid:88)
| E(y,h;x)=− | W x y h |     | (6) |
| ---------- | ------- | --- | --- |
|            | ijk i j | k   |     |
ijk
Thevaluesforyandhcanbecomputedinthesameway[74]:
1
| p(h |x,y)= | (cid:80) |       | (7) |
| ---------- | -------- | ----- | --- |
| k 1+exp(−  | W        | x y ) |     |
|            | ij ijk   | i j   |     |
1
| p(y |x,h)= |            | .     | (8) |
| ---------- | ---------- | ----- | --- |
| j 1+exp(−  | (cid:80) W | x h ) |     |
|            | ik ijk     | i k   |     |
(a)Hiddenlayeractingasagate. (b)Factorizationreducingthenumberofparameters.
| Figure11: GateapproachesinagatedBoltzmannmachine. |     | (Source: [73]) |     |
| ------------------------------------------------- | --- | -------------- | --- |
The model parameters W are trained with gradient-based optimization maximizing the average conditional log-
(cid:80)
likelihoodL= 1 logp(yα|xα)fortrainingpairs(xα,yα). Becausepartsofthegradientareintractable,Gibbs
N α
samplingisusedtoapproximatepartialresultswiththehelpoftheconditionaldistributionsdescribedinEquation7
andEquation8inaschemecalledcontrastivedivergence. [74]
Memisevicetal.[74]usethegatedBoltzmannmachinetolearntransformationrepresentationsonrandomlytransformed
8×8pixelimagesandpredictthenextimagesonvideopatchesofsize22×22pixels. Theynoticethatthemodel
becomesintractableforlargerimagesduetothecubicparameterspaceWandmodifyittomakeititerativelyapplicable
tosmallerimagepatches. Finally,themodel’sabilitiesaredemonstratedbyanalogymaking,whichmeansobtaininga
transformationfromasourceimageandapplyingthetransformationtoatargetimageusingthepatch-wiseapproach.
Memisevic et al. [75] tackle the problem of the rapidly expanding cubic parameter tensor W for large inputs by
approximatingtheresultsusingthreematriceswx,wy andwh,sow = (cid:80)F wx wy wh . Supposethenumberof
|     | ijk | f=1 if jf kf |     |
| --- | --- | ------------ | --- |
12

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
factorsF issimilartothenumberofhiddenandvisiblevariables. Inthatcase,themodelnowonlyrequiresO(N2)
insteadofO(N3)parameters(seeFigure11foracomparison). Like[74],themodellearnsfiltersastransformation
representationsonlarger40×40pixelimages. Also,theanalogyexperimentsarerepeated,andmotionextractionis
successfullyperformed.
Tayloretal. [73]proposethreekeypropertiesfortimeseriesmodels:
1. Distributed(i.e.,componential)hiddenstateinsteadofsamplingfromasinglecategorylikeHMMstoretain
highflexibilityandcapacity.
2. Undirected,bipartitegraphasthemodelstructuretomakeinferencesimpleandefficient.
3. Abilitytoformdeepnetworksbystackingmodelsandlearningonelayeratatimetocapturemoreabstract
datafeatures.
Guidedbytheseconstraints, theyintroduce theConditionalRestrictedBoltzmannMachine(CRBM), whichtakes
oneormorevisiblelayersfromprevioustimestepsasadditionalinputstoanormalRBM(seeFigure12a),andthe
ConditionalDeepBeliefNetwork(CDBN),whichstacksmultipleCRBMssimilartoaDBN,tobuildagenerative
model for time series initialized by real data (see Figure 12b). Further, the gated CRBM is introduced to enable
multiplicativeinteractionsbetweentimesteps,allowingthelearnedtransformationstobehighlynonlinear. Also,the
factorizationmethodfrom[75]isreintroducedtoreduceparameters,andpredefinedstylelabelsareaddedtothegate
process. ThemodelsaresuccessfullyevaluatedusingtheCMUmotiondatasetwheremotionsarecontinuedbythe
CRBMsornewmotionswithmixedorchangingstylesarecreated.
|     |       | ?           | ?       |           |         |     |
| --- | ----- | ----------- | ------- | --------- | ------- | --- |
|     |       | ?           | ?       |           |         |     |
|     |       | ? ?         |         |           |         |     |
|     |       | ?           | ?       | ?         |         |     |
|     | 1 2 3 | 4 5 6 1 2 3 | 4 5 6 1 | 2 3 4 5 6 | 1 2 3 4 | 5 6 |
(a)Anorder2CRBM. (b)ACDBNconsistingofanorder2andanorder3CRBMinitializedbyreal
datatogenerateanewsample.
| Figure12: ArchitectureofCRBMandthedeepversionCDBN. |     |     | (Source: | [73]) |     |     |
| -------------------------------------------------- | --- | --- | -------- | ----- | --- | --- |
2.7 Autoencoders
The basic autoencoder is a network that has as input a vector x ∈ [0,1]d and maps it to a hidden representation
y∈[0,1]d′ withafunctiony=f (x)=s(Wx+b). Wisaweightmatrixofsized′×d,babiasvectorandtogether
θ
1
theyaretheparametersθ = {W,b}off. s(x) = isthesigmoidfunction. Thehiddenrepresentationisthen
1+e−x
mappedbacktoavectorz∈[0,1]dwherez=g (y)=s(W’y+b’)withθ′ ={W’,b’}. Optionally,theconstraint
θ′
W’=W⊤canbeapplied.
[76]
During the unsupervised representation learning, the autoencoder adapts its parameters to minimize the average
reconstructionerrorfortrainingsamplesx(i)andcorrespondingy(i)andz(i):
|                | n                   |        | n        |              |     |     |
| -------------- | ------------------- | ------ | -------- | ------------ | --- | --- |
| 1              | (cid:88)            | 1      | (cid:88) |              |     |     |
| θ∗,θ′∗ =argmin | L(x(i),z(i))=argmin |        | L(x(i),g | (f (x(i)))). |     | (9) |
|                |                     |        | θ′       | θ            |     |     |
| θ,θ′ n         |                     | θ,θ′ n |          |              |     |     |
|                | i=1                 |        | i=1      |              |     |     |
∥x−z∥2.
ThelossfunctionLcanbeanythingcompatiblewiththedata,forexample, thesquarederror L(x,z) =
SimilartoDBNsandDBMs,thehiddenlayerofoneautoencodercanbecometheinputlayerofanotheronetolearn
higher-levelrepresentationsorpre-traintheweightstogenerateaneuralnetworkfromthemlater. [76]
RBMsandautoencodersareverysimilarinstructure(RBMsareundirected,whileautoencodersareusuallydirected
graphs),buttheydifferintrainingprocedureandhiddenrepresentation: Theautoencoderconsidersthereal-valued
13

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
mappingfromtheinputasitsrepresentation,whiletheBoltzmannmachinesamplesabinaryrepresentationfromthat
real-valuedmapping. Autoencoderscanalsobeseenasdeterministicfeedforwardneuralnetworks,whileRBMscanbe
definedasthegenerativestochasticvariant. [77,78]
Shortoverviewofotherusagesofautoencoders:
Approach Description Year
[79] DeepAutoregressiveNetwork(DARN):Adeepautoencoderwithamixtureofstochasticand 2014
deterministichiddenunitsthatincorporateautoregressiveconnectionsinthesamelayer,so
p(h)=
(cid:81)nh
p(h |h ). OutperformsRBMandNADEonimagelog-likelihood.
j=1 j 1:j−1
[78] Thefirstevaluationofoneandtwo-layerautoencodersonmusicaudiospectrograms. 2014
[80] AnhierarchicalLongShort-TermMemory(LSTM)autoencoderwithanattentionmechanism 2015
thatbuildsandreconstructsembeddingsofwords,sentences,andparagraphs. Themodelis
capableofcoherentmulti-sentencegeneration.
[81] Usingso-calledLadderNetworks,asemi-supervisedlearningmodelcombiningsupervisedand 2015
unsupervisedlearningindeepneuralnetworks. Itenhanceslearningbyaddingdenoisingtasks
ateachlevelofthemodel,fosteringmorerobustfeaturelearning. Themodel’seffectivenessis
demonstratedonseveralbenchmarkdatasets,whereitachievesstate-of-the-artperformancein
semi-supervisedlearningtasks.
[82] Extendingseveralstate-of-the-artnetworkarchitectureapproachesbyintroducingauxiliary 2016
variablestodeepgenerativemodels,whichimprovevariationaldistributionapproximation.
[83] DEFactor: Conditionalmoleculegenerationwithoptimalpropertiesusingagraphconvolu- 2018
tionalnetwork[84]asanencodertoproducealatentgraphrepresentation,aLSTMcreates
a sequence of node embeddings autoregressively, and a decoder determines the edge and
nodetypesusingasimilaritymeasureofthenodeembeddings. Additionally,anexistence
moduleMLPstopstheLSTMgeneratorwhenanon-informativeembeddingisencounteredto
generategraphsofarbitrarysize.
[85] AdversarialGenerator-EncoderNetwork(AGE):Ageneratorcreatesdatafromaspecified 2018
latentdistributionz ∼ p(z)andanadversarialencoderconvertsrealandgenerateddatato
latentvectors.TheAGElearnsbycomparingthedistributionsoftherealandfakelatentvectors
with p(z). The model is suitable for conditional and unconditional generation, converges
quickly,anddoesnotrequireadiscriminator.
[86] Augmentingtimeseriesdatathroughtime-warpedautoencoders. Theauthorsintroducetwo 2021
techniques - independent and dependent - and showcase their effectiveness in producing
syntheticdatasamples. Thismethodutilizesthecharacteristicsofauto-encoderstocreate
high-quality,realistictimeseriesdata.
2.7.1 HelmholtzMachines
TheHelmholtzmachine[87]isadirecteddeepgenerativemodel[88]withbinaryunits,biases,andgenerativeand
recognitionweightsfortherespectivedirection(seeFigure13).Theweightsaretrainedwiththe“wake-sleep”algorithm
[89]: Duringthe“wake”(recognition)phase,theinputvaluesarepropagatedbottom-upthroughthelayerstocreatea
representation. Thestates ofunitvwithbiasb andincomingweightsw isdefinedas
v v uv
1
p(s =1)= . (10)
v 1+exp(−b − (cid:80) s w )
v u u uv
Thenthegenerativeweightsofthehiddenstatessα betweenlayerskandj areupdatedwiththedeltarule∆w =
i kj
ϵsα(sα−pα)andlearningrateϵ.
k j j
The“sleep”phasegeneratesthestatesofthelowerlayersfromthehighestlayerinatop-downapproach. Itupdatesthe
recognitionweightsofallstateswithanotherdeltarule∆w =ϵs (s −q )whereq istheprobabilitythatunitkis
jk j k k k
activatedbytherecognitionweightsofthestatess ofthelowerlayer.
j
2.7.2 DenoisingAutoencoder
Denoising Autoencoders (DAEs) modify the training process of basic autoencoders by randomly corrupting the
input vector x (i.e., setting a fixed proportion of values to zero), resulting in ˜x, and then trying to restore it with
thetransformationsf andg (seeFigure14). Thedatacorruptionimprovesthemodel’sgeneralizationabilitiesand,
therefore,therepresentations’robustness. Also,theconstraintd′ <dofthebasicautoencodertopreventoverfittingcan
nowbeomitted. [76]
14

Extracting and Composing Robust Features with Denoising Autoencoders
2.3. The Denoising Autoencoder towards reconstructing the uncorrupted version from
the corrupted version. Note that in this way, the au-
To test our hypothesis and enforce robustness to par-
toencoder cannot learn the identity, unlike the basic
tially destroyed inputs we modify the basic autoen-
autoencoder, thus removing the constraint that d0 < d
coder we just described. We will now train it to recon-
or the need to regularize specifically to avoid such a
struct a clean “repaired” input from a corrupted, par-
trivial solution.
tially destroyed one. This is done by first corrupting
the initial input x to get a partially destroyed version
2.4. Layer-wise Initialization and Fine Tuning
x˜ by means of a stochastic mapping x˜ ∼ q (x˜|x). In
D
our experiments, we considered the following corrupt-
The basic autoencoder has been used as a building
ing process, parameterized by the desired proportion ν
block to train deep networks (Bengio et al., 2007), with
of “destruction”: for each input x, a fixed number νd
the representation of the k-th layer used as input for
of components are chosen at random, and their value
the (k + 1)-th, and the (k + 1)-th layer trained after
is forced to 0, while the others are left untouched. All
the k-th has been trained. After a few layers have been
information about the chosen components is thus re-
trained, the parameters are used as initialization for a
moved from that particuler input pattern, and the au-
network optimized with respect to a supervised train-
toencoder will be trained to “fill-in” these artificially
ing criterion. This greedy layer-wise procedure has
introduced “blanks”. Note that alternative corrupting
been shown to yield significantly better local minima
ComprehennsivoeiEsxepslorcatoionuolfdSybntheeticcoDnatasGideneerraetidon 1 : A. STurhveey corrupted input x˜ is
than random initialization of deep networks , achieving
then mapped, as with the basic autoencoder, to a hid-
better generalization on a number of tasks (Larochelle
den representation y = f (x˜) = s(Wx˜+b) from which
θ et al., 2007).
we reconstruct a z = g (y) = s(W0y + b0) (see figure
θ0
The procedure to train a deep network using the de-
1 for a schematic representation of the process). As
noising autoencoder is similar. The only difference is
before the parameters are trained to minimize the av-
how each layer is trained, i.e., to minimize the crite-
erage reconstruction error L (x,z) = IH(B kB ) over
IH x z
rion in eq. 5 instead of eq. 3. Note that the corrup-
a training set, i.e. to have z as close as possible to the
tion process q is only used during training, but not
uncorrupted input x. But the key difference is that z
D
is now a deterministic function of x˜ rather than x and for propagating representations from the raw input to
higher-level representations. Note also that when layer
thus the result of a stochastic mapping of x.
Figure13: ArchitectureofaHelmholtzmachinewiththreelayersK,L,andIandprobabilitiespforgenerationandq
k is trained, it receives as input the uncorrupted out-
forrecognition. (Source: [89])
put of the previous layers.
y
L (x,z)
f g θ0 H 3. Relationship to Other Approaches
θ
Our training procedure for the denoising autoencoder
q
D
involves learning to recover a clean input from a cor-
x˜ xx z
rupted version, a task known as denoising. The prob-
Figure14: TrainingprocessofaDenoisingAutoencoder. (Source: [76])
lem of image denoising, in particular, has been exten-
Figure 1. An example x is corrupted to x˜. The autoen-
Bengioetal. [90]proposeageneralizedprobabilisticinterpretationofDAEs,whereanobservedrandomvariableXsiivsely studied in the image processing community and
coder then maps it to y and attempts to reconstruct x.
corruptedusingaconditionaldistributionC(X|X)andtheDAEistrainedtoestimatethereverseconditionalP (X|X),
θ many recent developments rely on machine learning
whereθarethetrainableparameters. ThesamplingprocessfromthisDAEisrealizedusingaMarkovchainwhere
Let us define the joint distribution
X t ∼ P θ (X|X t−1 )andX t ∼ C(X|X t ), whichtheauthorsprovegeneratesthedata-generatingdistributionPa(Xp)proaches (see e.g. Roth and Black (2005); Elad and
withaproperlytrainedmodel. Theyintroducewalkbacktraining,wherethedefaultcorruptionprocessC isreplaced
withawalkbackprocessqC 0 ,(wXhic,hXgeen,erYates)o=neoqrm 0 o(rXebo)oqsted(“Xneega|tXive)exδamples”X(Y∗ fo)ratraini(n4gs)ampleXAbyharon (2006); Hammond and Simoncelli (2007)). A
D
goingarandom-lengthwalkthroughtheaforementionedMarkovchainwiththe
f
cuθr
(
re
Xent )
modelparameters. Thetraining
particular form of gated autoencoders has also been
withthesegreatlydivergentcorruptions,whichmaynotevenberepresentedbythetrainingdataorsimplecorruptions,
preventsthewDhAEerfreomδdev(iavtin)gtpooufatrsfrommtahespslau0siblwephreedinctiounran6=ge. vTh.eexTpehrimuesntsYonthiesMaNISTdataset
u used for denoising in Memisevic (2007). Denoising us-
(seeFigure15)showthattheresultsoftheMarkovchainofthewalkback-trainedmodellookmorenaturalthanthe
onesobtain d ed e fr t o e m r t m hem in od i e s l t tr i a c ine f d u w n ith c a t s i i o m n plec o or f rup X teion . pro q ce 0 ss ( . X,Xe,Y ) is param- ing autoencoders was actually introduced much ear-
eterized by θ. The objective function minimized by
lier (LeCun, 1987; Gallinari et al., 1987), as an alter-
stochastic gradient descent becomes:
native to Hopfield models (Hopfield, 1982). Our ob-
h (cid:16) (cid:17)i jective however is fundamentally different from that of
argminEE L X,g (f (Xe)) . (5)
q0(X,Xe) IH θ0 θ developing a competitive image denoising algorithm.
θ,θ0
We investigate explicit robustness to corrupting noise
So(a)fTrraoinmingwtithhseimppleocionrrutptioonf. view of the stoch(ba)sTrtaiincinggwritahdwailkebnactk.de-
as a novel criterion guiding the learning of suitable in-
Figure15: ComparisonoftheMNISTresultsofaDAEtrainednormallyorwithwalkback. (Source: [90])
scent algorithm, in addition to picking an input sam-
termediate representations to initialize a deep network.
ple from the training set, we will also produce a ran-
2.7.3 ContractiveAutoencoder Thus our corruption+denoising procedure is applied
dom corrupted version of it, and take a gradient step
The Contractive Autoencoder (CAE) uses the constraint W’ = W⊤ and improves the robustness of the hidndeont only on the input, but also recursively to interme-
representationybypenalizingsensitivitytotheinputxwiththeFrobeniusnormoftheJacobianmatrixJ (x),whichis
f
thesumofsquar1esTofhaellpaarptipalrdoeraivcathivewsoefthdeeesxtcrarcitbedefeaatnurdesyo = ur f(xa ) ncoanlcyersniisngitsheninoputtxsp[9e1,-92]: diate representations.
cific to a particular kind of corrupting noise.
15
1098

| ComprehensiveExplorationofSyntheticDataGeneration: |     |     |     |     |     |     | ASurvey |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
∂f(x)
|     |     |     |     |     |     | J        | (x)=        |     |     |     |     |     | (11) |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |          | f ∂x        |     |     |     |     |     |      |
|     |     |     |     |     |     |          | (cid:88) ∂f | (x) |     |     |     |     |      |
|     |     |     |     |     |     | ∥J (x)∥2 | = ( j       | )2. |     |     |     |     | (12) |
|     |     |     |     |     |     | f        | F           |     |     |     |     |     |      |
|     |     |     |     |     |     |          | ∂x          | i   |     |     |     |     |      |
ij
Inthecaseofthesigmoidactivationfunctionbeingused,thisresultsinthefollowing:
|     |     |     |     |     |          |     | d′       | d        |     |     |     |     |      |
| --- | --- | --- | --- | --- | -------- | --- | -------- | -------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |          |     | (cid:88) | (cid:88) | W2  |     |     |     |      |
|     |     |     |     |     | ∥J (x)∥2 | =   | (y (1−y  | ))2      | .   |     |     |     | (13) |
|     |     |     |     |     | f        | F   | i i      |          | ij  |     |     |     |      |
|     |     |     |     |     |          |     | i=1      | j=1      |     |     |     |     |      |
ThisobjectivefunctionisminimizedonthedataD , withhyperparameterλ ≥ 0, parametersθ = {W,b,b’}and
n
cross-entropylossL(x,z):
(cid:88)
|     |     |     |     |     | J (θ)= |     | (L(x,g(f(x)))+λ∥J |     | (x)∥2) |     |     |     | (14) |
| --- | --- | --- | --- | --- | ------ | --- | ----------------- | --- | ------ | --- | --- | --- | ---- |
|     |     |     |     |     | CAE    |     |                   |     | f      | F   |     |     |      |
x∈Dn
d
(cid:88)
|     |     |     |     |     | L(x,z)=− | x   | log(z )+(1−x | )log(1−z |     | )   |     |     | (15) |
| --- | --- | --- | --- | --- | -------- | --- | ------------ | -------- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |          |     | i i          | i        |     | i   |     |     |      |
i=1
Rifaietal. [92]proposeanalgorithm(seeAlgorithm1)togeneratesamplesfromapre-trainedCAEthatprovidesan
ergodicHarrischainwithastationarydistributionπundertheconditionthatJ J⊤isfullrank.
t t
| Algorithm1SamplingalgorithmforaCAE. |             |                              |     |         |          | (Source: | [92]) |     |     |     |     |     |     |
| ----------------------------------- | ----------- | ---------------------------- | --- | ------- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
| Require:                            |             | f,g,stepsizeσandchainlengthT |     |         |          |          |       |     |     |     |     |     |     |
| Ensure:                             |             | Sequence(x                   | ,y  | ),(x ,y | ),...,(x | ,y )     |       |     |     |     |     |     |     |
|                                     |             |                              | 1 1 | 2       | 2 T      | T        |       |     |     |     |     |     |     |
|                                     | Initializex | 0 arbitrarilyandy            |     | 0 =f(x  | 0 ).     |          |       |     |     |     |     |     |     |
|                                     | fort=0toT   |                              | do  |         |          |          |       |     |     |     |     |     |     |
∂f(xt).
|     | LetJacobianJ |     | =                        |     |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |              |     | t ∂xt                    |     |     |     |     |     |     |     |     |     |     |
|     | Letϵ∼N(0,σI  |     | )isotropicGaussiannoise. |     |     |     |     |     |     |     |     |     |     |
k
|     | Letperturbation∆y |      | =J       | J⊤ϵ. |      |     |     |     |     |     |     |     |     |
| --- | ----------------- | ---- | -------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |                   |      |          | t t  |      |     |     |     |     |     |     |     |     |
|     | Letx              | =g(y | +∆y)andy |      | =f(x | ).  |     |     |     |     |     |     |     |
|     |                   | t    | t−1      |      | t    | t   |     |     |     |     |     |     |     |
endfor
TheytesttheirtechniqueonaCAEwithtwo-layerstacksandcompareitagainsta2-layerDBN,resultinginslightly
better/worseperformanceontheTorontoFaceDatabase(TFD)/MNISTdatasetregardingthelog-likelihoodofthe
generatedsamplesbutsignificantlyreducedsensitivitytodeformationsofMNISTdigits.
Bengioetal. [93]hypothesizethatsamplingfromhigher-levelrepresentationsimprovesthequality(log-likelihood)and
classvariationofobtainedsamples. Theyprovetheirclaimsbysamplingfromhigh-levelrepresentationsgenerated
by a Markov chain processfrom variousdepths of multi-layer CAEs and DBNs and measuringthe log-likelihood.
Further,theytestthemixingofrepresentationsofdigitsatvariousdepthswithlinearinterpolation,whichalsogives
moreplausiblesamplesathigherlevels.
2.7.4 GenerativeStochasticNetwork
AGenerativeStochasticNetwork(GSN)[94]isageneralizedframeworkofadeepDAEthathasthestructureofa
Markovchainandcanbetrainedwithback-propagatedgradientsandwithoutlayer-wisepre-training. Thetransition
operatorP(x ,h |x ,h )isresponsibleforgeneratingthenextvisiblestateX andhiddenstateH oftheMarkov
|     |     | t t | t−1 t−1 |     |     |     |     |     |     | t   |     | t   |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
chain(seeFigure16).
Toenabletheback-propagationofthereconstructionlog-likelihoodlogP(X =x |H )intoalltheparametersofthe
|     |     |     |     |     |     |     |     |     | 1   | 0 1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
encodingfunctionf andreconstructionfunctiong ,adeterministicfunctionisusedtodefineH =f (X ,Z ,H )
|     |     |     | θ1  |     |     | θ2  |     |     |     |     | t+1 | θ1 t | t t |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- |
withZ beinganindependentnoisesourcesoX cannotbeexactlyrecoveredfromH . Thisresemblesthemasking
|     | t   |     |     |     |     | t   |     |     |     | t+1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofvaluesintheinputlayerofaDAE.
16

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
|           | H   |                                | H   |     | H   |                |     |
| --------- | --- | ------------------------------ | --- | --- | --- | -------------- | --- |
|           | 0   |                                | 1   |     | 2   |                |     |
|           |     | X                              |     | X   |     | X              |     |
|           |     | 0                              |     | 1   |     | 2              |     |
| Figure16: |     | TheMarkovchainstructureofaGSN. |     |     |     | (Source: [94]) |     |
Bengioetal. [94]usetheGSNframeworktoadapttheGibbssamplingprocessofaDBM(seeFigure17),butwiththe
abilitytousetheGSN’sbackpropagationateachlayer. ThechainstartswithatrainingsampleX =x 0 andencodes
and reconstructs intermediate samples x several times. The training of the model is realized using the sum of all
i
| log-likelihoodstothetargetX | =x  | ,inspiredbythewalkbackobjective(see[90]). |     |     |     |     |     |
| --------------------------- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
0
Figure17: AGSNinspiredbytheGibbssamplingprocessofaDBM. Thelightningsymbolsindicatethecorruptionof
| thesampleswithsalt-and-peppernoise. |     | (Source: | [94]) |     |     |     |     |
| ----------------------------------- | --- | -------- | ----- | --- | --- | --- | --- |
2.7.5 VariationalAutoencoder
Variational Autoencoders (VAEs) is an autoencoder with encoder E(.) and decoder D(.) whose hidden layer is
representedasaGaussiandistributionN(µ,σ2)withmeanvectorµandstandarddeviationvectorσthatareobtained
fromtheencoderµ,σ = E(x),wherex ∼ X. Thedecodersamplesfromthisdistributionandreconstructsthedata
xˆ = E [D(z)]. Additionally, the aggregated distribution of z over all data X is constrained to be N(0,I),
z∼N(µ,σ)
allowingrandomvectorstobesampledfromN(0,I)tobeusedfordatagenerationwiththedecoder.
[95]
TheVAEistrainedusingtheEvidenceLower-Bound(ELBO)loss
| L=E |     | [E        | [∥D(z)−x∥2]+KL(N(µ,σI)∥N(0,I))], |     |     |     | (16) |
| --- | --- | --------- | -------------------------------- | --- | --- | --- | ---- |
|     | x∼X | z∼N(µ,σI) |                                  | 2   |     |     |      |
wherethefirsttermencouragestheautoencodingpartwhilethesecondtermwiththeKullback-Leibler(KL)divergence
KL(p∥q)measuresthedifferencebetweentheprobabilitydistributionspandq. [95]
Kingmaetal. [96]appliedtheVAEasagenerativemodelwithMLPencoderanddecodertotheMNISTandFrey
Facedatasets. Theyachievefasterconvergenceandahighermarginallikelihoodthantheirreference,thewake-sleep
algorithm,describedinSection2.7.1.
Gregoretal. [97]introducetheDeepRecurrentAttentiveWriter(DRAW)forimagegeneration. Theauthorsfollowthe
humandrawingprocess,whereroughoutlinesareiterativelyrefineduntilarealisticpictureisgenerated. Similartoa
VAE,DRAWconsistsofanencoderthatlearnsarepresentationz∼p(z)oftheinputandadecoderthatreconstructsthe
inputfromz,butbothmodelsareLSTMsthatonlyhandleregionsofthefullinputdefinedbyanattentionmechanism
at each time step. For evaluation, the authors use MNIST, the Street View House Numbers (SVHN) data set, and
CIFAR-10,andtheyachievehighlyrealisticresultsonthefirsttwowhileoverfittingthelastdatasetduetoonly50,000
trainingsamples.
Rezendeetal. [98]proposetheclassofsequentialgenerativemodels,whichgenerateT groupsofklatentvariables
sequentiallyinsteadofgeneratingK =kT latentvariablesatonceandalsosequentiallyreconstructdatatoamodifiable
canvaswhileincorporatinginferenceandwritingattentionmechanisms. AtthecoreofthemodelareoneormoreRNNs
(bothLSTMsandGatedRecurrentUnits(GRUs))andattention-basedneuralnetworkslikespatialtransformers[99]to
writetheRNNoutputtothecanvas. Themodelperformswellonunconditionalsamplingandone-shotlearningtasks,
17

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
whereaconceptisonlyencounteredonceandcompellingvariationsoftheconceptshouldbegenerated,ormultiple
concepts(e.g.,lettersofanalphabet)areprovidedduringthesequentialinferenceprocess,andaplausiblenewcharacter
isgenerated.
Higginsetal. [100]proposeβ-VAE,areformulationoftheoriginalunsupervisedVAE(β = 1)withanadditional
hyperparameterβ thatencouragesthemodeltolearnbetter-disentangledrepresentationsofdata,meaningthatsingle
hiddenunitsencodesinglegenerativefactorswhilebeinginvarianttochangesinothers(e.g.,skincolorinfaceimages),
byenforcingmoreindependenceandlesscovarianceofthelatentvariablesandtheirdistributions. β-VAEoutperforms
the previous unsupervised state-of-the-art model InfoGAN [101] and semi-supervised DC-IGN [102] in terms of
disentanglementoffactorsqualitativelyandquantitatively.
Tomczaketal. [103]implementtheVAE’spriorasamixturedistribution(e.g.,aGMM)thatcanbetrainedwithpseudo
inputsandproposemultiplelayersofvariables. TheyevaluatetheirmodelonmultipleMNISTdatasets,OMNIGLOT,
Caltech101Silhouette,FreyFace,andHistopathologypatches,resultinginstate-of-the-artlog-likelihoodcomparedto
anormalVAEandavoidanceofitslocaloptimaproblem.
ShortoverviewofotherusagesofVAEs:
Approach Description Year
[104] Variational Recurrent Autoencoder (VRAE): A VAE with RNN encoder and decoder for 2014
modelingsequentialdata. ThemodelisusedforMIDImusicgenerationandcreates“medleys”
ofthetrainingdata.
[105] DenoisingVariationalAutoencoder(DVAE):Combinationofthenoiseinjectionattheinput 2015
likeaDAEandthenoiseinjectionatthehiddenlayerofaVAEimprovesaveragelog-likelihood
resultsonMNISTandFreyFacedatasets.
[106] Importance-weightedautoencoder(IWAE):AVAEwithatighterlog-likelihoodlowerbound 2015
onlogp(x)basedonimportanceweightingusingmultiplesamplesq(h |x),thatlearnsricher
i
representationsthanVAEs,outperformingthemonMNISTdensityestimation.
[107] AVAEwithsingle-layerLSTMencoderanddecoderforsentencegeneration. Interpolation 2015
betweenlatentvectorsoftwosentencesprovidesinterestingresults.
[102] DeepConvolutionalInverseGraphicsNetwork(DC-IGN):AVAEbuiltwithaconvolutional 2015
encoder and deconvolutional decoder. The model is further encouraged to assign certain
transformations(e.g.,lighting,rotation)inimagestodisentangledneurongroupsunsupervised
bytrainingwithmini-batchesoftransformedimages.
[108] CompositedspatiallytransformedVAE(CST-VAE):Layer-wisesequentialimagegeneration 2015
usingposeandcontentencoder-decoderpairsonthepartialresultsandaspatialtransformer
network[99]tooutputthenextimagelayerfronttoback.
[109] VAEtrainingwithanadditionalsimilaritylossobtainedfromajointlytrainedGANdiscrimi- 2016
natorforhigherimagequalityandbetterrepresentations.
[110] Attribute2Image: UsingaVAEtolearndisentangledlatentrepresentationsofattributes(e.g., 2016
color,gender,viewpoint)fromimagesandgeneratenewimagesconditionedonattributes.
[111] AVAEwithrecurrentencoderanddecoder(similarto[107])isusedtogenerateSMILES 2016
[112]textencodingsofnewvalidmoleculeswithdesirablepropertiesbyusinggradient-based
optimizationinthelatentspace.
[113] Proposalofthevariationallossyautoencoder(VLAE),whichallowstheusertocontrolwhat 2016
thelatentvariablecancontainbylimitingthereceptivefieldoftheautoregressiveencoder
anddecoder. Combinedwithanautoregressivemodelmodelingp(z),state-of-the-artresults
areachievedonMNIST,OMNIGLOT,andCaltech-101densityestimation(competitiveon
CIFAR-10).
[114] PixelVAE: Combination of a VAE with a PixelCNN-based [115] autoregressive decoder 2016
that iteratively refines the image result. It performs comparably to PixelCNN with fewer
autoregressivelayersandasmallerlatentvariablethananormalVAE.
[116] GrammarVAE:Tobettergeneratediscretedata,itisconvertedtoaparsetreeusingacontext- 2017
freegrammar,andtherulesusedbythetreearethenone-hotencodedinorder,formattedasa
matricandmappedtoalatentspacewithaConvolutionalNeuralNetwork(CNN). ARNN
decodesfromthislatentspacebacktovalidrules. Themodelgeneratesmoleculestructures
andarithmeticexpressions,outperformingtext-basedrepresentations.
Continuation...
18

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[117] RecurrenthierarchicalVAEwithBiLSTMencoderand3-layerLSTMdecoderforthecreative 2017
reconstructionofshortmusicalsequenceswithrandomsamplingorinterpolationinthelatent
space.
[118] AVAEwithLSTMencoderandCNNdecoderwithdilatedconvolutionsfortextmodeling 2017
andgeneration. Changesinthedilationconfigurationgivecontroloverthecontextsizefrom
previouswords,andtheconvolutionaldecoderislesspronetoignoreencoderinformation
becauseitscontextualcapacityislowerthananLSTM’s.
[119] Vector-QuantisedVAE(VQ-VAE):TheencoderCNNoutputszarediscretetoenforcemore 2017
efficientusageofthelatentspaceandprevent“posteriorcollapse”,whichisoftencausedby
decodersignoringz. Themodeliscombinedwithanautoregressivedecoder(PixelCNNfor
images,WaveNetforaudio)andprovidessimilarresultstocontinuousVAEs.
[120] Character-leveltextgenerationVAEwithconvolutionalencodercombinedwithadeconvo- 2017
lutional decoder with recurrent output layer. The CNNs make VAE training easier and an
additionalcostfunctionencouragesrelianceofthedecoderonthelatentvector. Experiments
onTwittertweetgenerationshowmorediverseandcoherentsamplesthanaLSTM-based
VAE.
[121] Sketch-RNN: Sketch-conditionalandunconditionalstroke-basedsketchgenerationwitha 2017
sequence-to-sequence VAE with bidirectional RNN encoder and RNN decoder. Possible
applicationsalsoincludelatentspaceinterpolationandsketchcompletion.
[122] First application of a recurrent VAE [107] to music generation, providing a good balance 2017
betweenlocalandglobalstructures.
[123] Training a GAN to generate and modify the latent code z of an unconditional VAE with 2017
z′ = G(z,y ) to satisfy specific properties enforced by D(z′,y ). Allows zero-shot
attr attr
conditionalgenerationandidentity-preservingtransformation(e.g.,samefacewithdifferent
haircolor)ofdatafromanunconditionalVAEmodel.
[124] Application of the grammar VAE [116] to molecule generation with desired properties by 2018
randomly sampling 106 samples from p(z) and iteratively encoding and decoding them
withtheautoencodermanytimesbeforefilteringtheresultswithneuralnetworkregression
functionstogetthebestsamplesforthedesiredproperty.
[125] GraphVAE(GVAE):Generationofprobabilisticfullyconnectedgraphsfromwhichcanbe 2018
sampled. TheconvolutionalencodergetsasinputagraphG = (A,E,F)andgraphlabel
vectory,whereAistheadjacencymatrix,E theedgeattributetensor,andF anodeattribute
matrix,andcomputesalatentrepresentationz. ThedeterministicdecoderMLPtakeszandy
andoutputsG˜ =(A˜,E˜,F˜),containingtheindependentnodeandedge,edgeclassandnode
classprobabilitiesrespectivelyforgraphswithafixedmaximumnumberofk nodes. The
modelisdemonstratedonmoleculegenerationtasksandisonlysuitableforslightlylarger
graphsthantheprovidedinput.
[126] MusicVAE: Recurrent VAE with two-layer bidirectional LSTM encoder and hierarchical 2018
RNN decoder, which consists of a two-layer unidirectional LSTM conductor that creates
subsequenceembeddingsfromthelatentvector,andatwo-layerLSTMdecoderRNNthat
producesthefinalsubsequenceoutputinsidetheseseparateembeddings. Themodelachieves
promisingresultsonMIDImusicreconstructiontasks.
[127] JunctiontreeVAE(JT-VAE):Encodinganddecodingmoleculesusingtworepresentations: A 2018
fine-grainedgraphconnectivityrepresentationobtainedfromamessage-passingnetwork[128]
andarepresentationofajunctiontree(alsofromamessagepassingnetwork),thatmodels
a molecule as a composition of valid subgraph components and avoids the node-by-node
generationofinvalidintermediaries.
[129] ConstrainedGraphVAE(CGVAE):Usinggatedgraphneuralnetworksasencoderanddecoder 2018
formoleculargraphgeneration. TheencodermapsagraphwithamaximumofN nodestoN
latentcodesz conformingtoaGaussiandistribution. ThedecoderinitializesagraphwithN
v
nodesanda“stopnode”fromthelatentcodes. Then,aloopstartswherenewedgesareadded
andlabeled,andnoderepresentationsareupdatedwithmessagesfromneighbors(see[128])
untilanedgetothestopnodeiscreated. Correctatomvalencyisalwaysenforcedtoguarantee
validmolecules.
Continuation...
19

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[130] Syntax-directedVAE(SD-VAE):Applyingsyntaxandsemanticconstraintstothedecoder 2018
ofagrammar-basedVAEsimilartoGrammarVAE[116]toenforcesyntacticallyvalidand
semanticallyreasonablereconstructionandoptimizationofmoleculestructuresandprogram
code.
[131] Differentially private autoencoder-based generative model (DP-AuGM) & variational 2018
autoencoder-based model (DP-VaeGM): Autoencoders are trained using stochastic gradi-
entdescentwithclippedgradientsandnoiseinjection[132]. ForDP-AuGM,onlytheencoder
makesconfidentialdata“private”. TheVAEversiontrainsonemodelforeachclass,samples
z fromeachmodel, andmergesthedecodedsamples,whichislessstablethantheformer
approach.
[133] IntroVAE: Integrating the concepts of VAE and GAN into a single model that is both a 2018
generatorandadiscriminator. Thismodelself-evaluatesthequalityofgeneratedimagesand
improvesitselfaccordingly,offeringstabletrainingandhigh-resolutionimagesynthesis. The
approachcombinestheadvantagesofVAEandGANwithoutneedingextradiscriminators,
simplifyingthearchitectureandimprovingtrainingefficiency.
[134] AmultilevelVAEarchitectureforgeneratingcoherentandlongtextsequences. Theencoder 2019
consistsofalowerandhigher-levelCNNproducingseparatelatentrepresentationswherethe
lowerlatentvectorisadditionallyconditionedontheupper. Thelowerrepresentationisthen
fedtoahierarchicalLSTMdecodernetworkwithasentence-levelandword-levelLSTM. The
modelperformswellonconditional(title-to-paragraph)andunconditionaltextgeneration.
[135] Topic-guidedVAE(TGVAE):ModelingthelatentspaceofaVAEusingaGMMpriordistribu- 2019
tionparametrizedbyaneuraltopicmodulethatispoweredbythebag-of-wordsrepresentation
ofthetext. AGRUencoderanddecoderprocessedthetextinputstooutputs. Themodelis
usedfortextgenerationandsummarization.
[136] A VAE for molecule generation that uses a graph-convolutional encoder, a MLP to cre- 2019
ate a “bag-of-atoms” (counts for certain atoms in the target reconstruction), and a graph-
convolutionaldecoderthattakesthelatentrepresentationandtheatombagtocreateanedge
probabilitymatrixfromwhichabeamsearchgeneratesadiscreteoutput.
[137] NeVAE:Generatingmoleculargraphswithvariablesizefromaconvolution-styleVAEwith 2020
variable-lengthlatentrepresentations(oneforeachnode). Inadditiontotheatoms’typesand
theirbonds,themodelalsopredictstheirpositions. Thedecodercanbefurtheroptimizedwith
agradient-basedalgorithmtomaximizespecificpropertiesofthegeneratedmolecules.
[138] Node-EdgeDisentangledVAE(NED-VAE):Usingthreeconvolutionalsub-encoders(node, 2020
edge,andgraph)andtwodeconvolutionalsub-decoders(nodeandedge),bothwithaccessto
thegraphrepresentation,toreconstructthenodeandedgeattributesfromwhichagraphcan
berecreated. Themodelalsoenforcesthedisentanglementoflatentfactorsofnodes,edges,
andjointpatterns.
[95] TabularVAE(TVAE):TabulardatagenerationwithaVAEusingprobabilitydistributionsto 2020
encodediscreteandcontinuousvalues.
[139] HI-VAE:AVAEthatcanhandleincomplete(missingvaluesatrandom)andheterogeneous 2020
(mixedcontinuousanddiscrete)databylearningtheinfluenceofinputvariablesonthelatent
codeindividually,usingspecialdistributionsfordiscretevariables,andonlyusingobserved
variablesforrecognition(i.e.,replacemissingwithzero).
[140] MessagePassingGraphVAE(MPGVAE):BuildingontopoftheGraphVAE[125],theauthors 2020
usemessagepassingneuralnetworks[128]forbothencoderanddecoder,whereedgeand
noderepresentationsarealternatinglyupdatedmultipletimesbasedonmessagesfromtheir
neighbors.
[95] Besides a conditional GAN, the authors introduce a tabular VAE for generating synthetic 2020
tabular data using . This method addresses challenges in modeling tabular data, which
oftencontainsamixofdiscreteandcontinuouscolumnsandmayexhibitimbalancesand
non-Gaussian distributions. It employs mode-specific normalization and reversible data
transformationstogeneratesyntheticdataeffectively.
[141] TreatingthemoleculeasasequenceofvalidSMILES-encoded[112]fragments/components, 2020
thisapproachusesGRUstoencodeamoleculetoalatentvectorwithGaussiandistribution
anddecodeitback. Thewholetrainingprocessincorporateslow-frequencymasking,which
masksrarelyencounteredfragmentswithamasktokenthatisreplacedduringsamplingby
anyofthesuitablemaskedfragmentswithuniformprobabilitytoimproveuniqueness.
20

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
2.7.6 DeepLatentGaussianModels
ADeepLatentGaussianModel(DLGM)isadeep,directedgenerativemodelpoweredbyGaussianlatentvariables. A
recognitionmodelwithLlayersencodesthetrainingobservationstoprovidethelayer-wiseparametersfortheGaussian
distributionsofthegenerationmodel. Thegenerativeprocessstartsatthetoplatentlayer(L)anddrawsmutually
independentGaussianvariablesE ∼N(E |0,I). Eachlayerh =T (h )+G E belowthetoplayerh =G E
l l l l l+1 l l L L L
dependsonthelayerabove,whereT areMLPtransformationsandG arematrices. Thevisibledatav=π(v|T (h ))
l l 0 1
isgeneratedfromadistributionπ. Themodelistrainedusingstochasticbackpropagation,i.e.,bycomputinggradients
throughrandomvariables. [142]
TheoriginalDLGMauthorsRezendeetal. [142]evaluatethegenerativeabilitiesofathree-layerDLGMonMNIST,
CIFAR-10,theFreyfacesdataset,andNORB.Theyalsoproposeanimputationusecase,wheretheGaussianmodel
fillsinmissingdataintheSVHN,Freyfaces,andMNISTdatasets. Theirexperimentsachieverealistic-lookingresults
comparabletoothercontemporaryapproachessuchastheRBMandDBN.
2.7.7 GatedAutoencoders
AGatedAutoencoder(GAE)isaconditionalbi-linearmodelthatlearnstorepresentalineartransformationencodedas
mappingunitsmbetweentwoobservationsx(1)andx(2)usingparametermatricesU,VandWwith
m=σ(W(Ux(1)·Vx(2))). (17)
Themappings,sincetheGAEisasymmentricmodel,canbeusedtoreconstructx(1)orx(2)respectivelybasedonthe
otherone[143]:
x˜(2) =VT(Ux(1)·WTm) (18)
x˜(1) =UT(Vx(2)·WTm). (19)
TrainingworkssimilarlytoaDAE: Inputpairsareindependentlycorruptedandconcatenated. Thenbackpropagation
andgradient-basedoptimizationareusedtominimizethelossfunction,forexample,thesymmetricreconstructionerror
[143,144]:
L=∥x(1)−x˜(1)∥2+∥x(2)−x˜(2)∥2 (20)
Michalskietal.[143]modelatimeseriesasasequenceoftransformationsappliedtoitselements. Duringthepredictive
training,apyramidofstackedGAEsisusedtolearnbasicandhigher-orderrepresentationsoftransformationsbetween
observationpairsandpredictfutureobservationsrecurrentlywithaconstanthighest-ordertransformation(seeFigure18).
Theautoencodersareinitializedbykseedframescorrespondingtotheklayersofthepyramidandoptimizedusing
backpropagationthroughtime.ThemodeliscomparedagainstaRNNandaRBMinthepredictionofchirps(sinusoidal
waveswithchangingfrequencies)andvideoframesofbouncingballsandobjectsoftheNORBdataset,outperforming
themintermsofmeansquarederror.
2.7.8 MaskedAutoencoders
Maskedautoencoderssetweightsintheirinput-to-hiddenorhidden-to-outputweightmatricestozero,meaningthereis
nocomputationalpathbetweencertaininputandoutputunits,whichisnecessary,forexample,forautoregressivetasks,
wherefutureinputsmustnotbeseen. Themaskingapproachalsodirectlyappliestodeeparchitectures(seeFigure19).
[145]
Germainetal. [145]proposethemaskedautoencoderfordistributionestimation(MADE),whichcomputesthejoint
probabilitydistributionp(x)ofdataxautoregressivelyasp(x)=
(cid:81)D
p(x |x )andthereforeneedstomaskthe
d=1 d <d
futureinputsx ,...,x fortherespectivesteps. Themodelcanalsobeusedforsamplingaccordingtothecalculated
d D
probabilitiesdemonstratedbygeneratingbinaryMNISTimages.
2.8 NeuralAutoregressiveDistributionEstimators
TheNeuralAutoregressiveDistributionEstimator(NADE)isinspiredbytheRBM,whosejointprobabilityestimation
of an observation is intractable and can also be interpreted as an autoencoder that assigns probabilities to binary
21

| ComprehensiveExplorationofSyntheticDataGeneration: |     |     |     |     |     | ASurvey |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A2-layerpyramidmodelisusedtopredictthenexttransformationmˆ(t:t+1) VT(U m(t−1:t)·
| Figure18: Left: |     |     |     |     |     |     |     |     |     | =   | 2   |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                 |     |     |     |     |     |     |     |     | 1   |     | 2   | 1   |     |     |     |     |     |     |
WTm(t−2:t))andtheresultingobservationxˆ(t+1) =VT(U x(t)·WTmˆ(t:t+1))withU,VandWbeingthefilter
| 2 2 |     |     |     |     | 1   | 1   | 1   | 1   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
matriceslearnedbytherespectiveautoencoders. Right: Multi-steppredictionwithconstanttop-layertransformationin
a3-layerpyramid. (Source: [143]) MADE:MaskedAutoencoderforDistributionEstimation
p(x x ,x ) p(x ) p(x x ) tobegreaterthanorequaltotheminimumconnectivityat
|     |     |     |     |     |     |     | 1| 2 | 3   | 2 3| 2 |                          |     |     |     |     |                  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------ | ------------------------ | --- | --- | --- | --- | ---------------- | --- | --- | --- |
|     | x   | x   | x   |     |     |     |      |     |        |                          |     |     |     |     | ml−1(k(cid:48)). |     |     |     |
|     |     | 1 2 | 3   |     |     |     |      |     |        | thepreviouslayer,i.e.min |     |     |     |     |                  |     |     |     |
k(cid:48)
|     |     |     |     |     |     |      |     | 3   | 1 2 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | !   | !   | !   |     |     |      |     |     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     | = MV |     |     |     |     |     |     |     |     |     |     |     |     |
4.2.Order-agnostictraining
V
1 2 2 1 So far, we’ve assumed that the conditionals modelled by
|     |     |     |     |     |     |       |     |     |     | MADE           |     | were | consistent                        | with | the natural | ordering |     | of the |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | -------------- | --- | ---- | --------------------------------- | ---- | ----------- | -------- | --- | ------ |
|     | W2  |     |     |     |     | = MW2 |     |     |     |                |     |      |                                   |      |             |          |     |        |
|     |     |     |     |     |     |       |     |     |     | dimensionsofx. |     |      | However,wemightbeinterestedinmod- |      |             |          |     |        |
|     |     |     |     |     |     |       | 2   | 1   | 2 2 |                |     |      |                                   |      |             |          |     |        |
ellingtheconditionalsassociatedwithanarbitraryordering
|     | W1  |     |     |     | =   | MW1 |     |     |     | oftheinput’sdimensions. |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
3 1 2 Specifically, Uria et al. (2014) have shown that training
x x x x x x anautoregressivemodelonallorderingscanbebeneficial.
|     |     | 1 2 | 3   |     |     |     |     | 1   | 2 3 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Autoencoder x Masks MADE Werefertothisapproachasorder-agnostictraining. Itcan
Figure19: Adeepmaskedautoencoderarchitecture. (Source: [145]) be achieved by sampling an ordering before each stochas-
|     |               |     |              |     |       |        |       |              |     | tic/minibatchgradientupdateofthemodel. |     |     |     |     |     |     | Therearetwo |     |
| --- | ------------- | --- | ------------ | --- | ----- | ------ | ----- | ------------ | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- |
|     | Figure1.Left: |     | Conventional |     | three | hidden | layer | autoencoder. |     |                                        |     |     |     |     |     |     |             |     |
Inputinthebottomispassedthroughfullyconnectedlayersand advantagesofthisapproach. Firstly,missingvaluesinpar-
observations. NADEmodelsaD-dimensionalobservationvectorxasaproductoftheone-dimensionalconditional
point-wisenonlinearities. Inthefinaltoplayer,areconstruction tiallyobservedinputvectorscanbeimputedefficiently: we
(cid:81)D
distributionsp(x)= is=p1ecifieid<ais p(x |x ). a Theprobabilityofx probability distribiution isconditionedonallpreviouslyseenobservationsx over inputs is produced. < i ,so
|                                   |         |              |     |         |     |           |         |     |              | invoke | an         | or dering | where | observed | dimensions |                  | are | all be- |
| --------------------------------- | ------- | ------------ | --- | ------- | --- | --------- | ------- | --- | ------------ | ------ | ---------- | --------- | ----- | -------- | ---------- | ---------------- | --- | ------- |
| theorderingofthevariablesmatters. |         | [146]        |     |         |     |           |         |     |              |        |            |           |       |          |            |                  |     |         |
|                                   | As this | distribution |     | depends | on  | the input | itself, | a   | standard au- |        |            |           |       |          |            |                  |     |         |
|                                   |         |              |     |         |     |           |         |     |              | fore   | unobserved |           | ones, | making   | inference  | straightforward. |     |         |
Eachprobabilityoutputxˆ =p(x =1|x )dependsonaH-dimensionalhiddenvectorh thatiscomputedrecursively
|     | toiencodeir | canno<ti | predict |     | or sample | new | data. | Right: | MAiDE. |                                                    |     |     |     |     |     |     |     |     |
| --- | ----------- | -------- | ------- | --- | --------- | --- | ----- | ------ | ------ | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| by  |             |          |         |     |           |     |       |        |        | Secondly,anensembleofautoregressivemodelscanbecon- |     |     |     |     |     |     |     |     |
Thenetworkhasthesamestructureastheautoencoder,butaset
structedonthefly,byexploitingthefactthattheconditionals
|     | of connections |     | is removed |     | such | that each | input | unit | is only pre- |             |     |     |                                           |     |     |     |     |     |
| --- | -------------- | --- | ---------- | --- | ---- | --------- | ----- | ---- | ------------ | ----------- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
|     |                |     |            |     |      |           |       |      |              | fortwodiffe |     | r   | e n torderingsarenotguaranteedtobeexactly |     |     |     |     |     |
dictedfromtheprpe(vxiio=us1o|xne<si,)u=siσng(Vm.,ui hltiip+licbai )tivebinarymasks ( 2 1 )
(MW1 ,MW2 consistent(andthustechnicallycorrespondtoslightlydif-
|     |            |      | ,MV).  | Inthisexample,theorderingoftheinput |           |        |       |           |         |        |          |      |     |          |         |        |          |     |
| --- | ---------- | ---- | ------ | ----------------------------------- | --------- | ------ | ----- | --------- | ------- | ------ | -------- | ---- | --- | -------- | ------- | ------ | -------- | --- |
|     |            |      |        |                                     |           |        |       |           |         | ferent | models). |      | An  | ensemble | is then | easily | obtained | by  |
|     | is changed | from | 1,2,3  | to 3,1,2.                           | This      | change | is    | explained | in sec- |        |          |      |     |          |         |        |          |     |
|     |            |      | h =σ(W |                                     | x +c)andh |        | =σ(c) |           |         |        |          | (22) |     |          |         |        |          |     |
tion4.2,butisn i otnecess . a ,< ry i f < or i understand 1 ingthebasicprinciple. samplingasetoforderings,computingtheprobabilityofx
T h e n u m be r s inVth∈eRhDid×dHen ,bun∈itRsDin dWica∈teRthHe×mD, a x im ucm∈nRuHm b e r u n d e r e a c h o r d eringandaveraging.
withσbeingthesigmo id f un c t ion a n d , a n d b e i ngthe p a ra m e t er s o f th e
Thiscorroefspinopnudstswointhweahcichhxˆthbeeikntghcuonmitpuotfeldaybyeralndeeupraelnndest.wTohrkeamndasakllsnaerueralnetworkshavingtied
NADEmodel.
|     |     |     | i   |     |     |     |     |     |     | Conveniently,inMADE,theorderingissimplyrepresented |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
weightsforeachobservcaotinonst.r[u1c4t6e]d based on these numbers (see Equations 12 and 13).
|     |     |     |     |     |     |     |     |     |     | by  | the vector |     | m0 = | [m0(1),...,m0(D)]. |     |     | Specifically, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | ------------------ | --- | --- | ------------- | --- |
NADEistrainedusingTghraedsieenmtadsekssceenntsounreththeaNtMegAatiDveELsoagti-sLfiiekseltihheooadut(oNreLgLr)esgsiviveenparotrpa-iningsetXwithsizeT
[146]: erty, allowing it to form a probabilistic model, in this example m0(d)correspondstothepositionoftheoriginaldth dimen-
p(x) = p(x )p(x |x )p(x |x ,x ). Connections in light gray sion of x in the product of conditionals. Thus, a random
|     |     | 2   | 3   | 2   | 1 2 | 3   |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
correspoTnd 1 to paths that depTendDonly 1 on 1 input, while the dark ordering can be obtained by randomly permuting the or-
|     |     | (cid:88) |     |     | (cid:88)(cid:88) |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
gray conne−ctiloongspd(xept )en=d on2input−s.logp(x |x )forx ∈X deredvector(2[13,)...,D]. Fromthesevaluesofeachm0,the
|     | T   |     |     | T   |     |     | i   | <i  | i   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t=1 t=1 i=1 firsthiddenlayermaskmatrixcanthenbecreated. During
order-agnostictraining,randomlypermutingthelastvalue
connectedtoatmostm2(k(cid:48))2i2nputs,i.e.thefirstlayerunits
ofm0 againissufficienttoobtainanewrandomordering.
|     | suchthatm1(k) |     |     | m2(k(cid:48)). |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
≤
Onecangeneralizethisruletoanylayerl,asfollows:
4.3.Connectivity-agnostictraining
1 if m l( k (cid:48) ) ml−1(k) O n e a dv a nt a g e o f o rd e r-a g n o sti c t r a in i ng is t ha t i te f f e c ti v e l y
W l
|     | M   | = 1 ml(k(cid:48))≥ml−1(k) |     |     | =   |     |     | ≥   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
k (cid:48),k 0 o th er w i s e. al lo w s u s t o t ra i n a s m a n y m o d e l s a s th er e a r e o r d e r i n g s ,
(cid:26)
|     |     |     |     |     |     |     |     |     | (12) | using | a   | common | set of | parameters. | This | can | be exploited |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | ------ | ------ | ----------- | ---- | --- | ------------ | --- |
Also, taking l = 0 to mean the input layer and defining bycreatingensemblesofmodelsattesttime.
|     | m0(d)=d | (which |     | is intuitive, |     | since | the | dth input | unit in- |     |     |     |     |     |     |     |     |     |
| --- | ------- | ------ | --- | ------------- | --- | ----- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
InMADE,inadditiontochoosinganordering,wealsohave
deedtakesitsvaluesfromthedfirstinputs),thisdefinition
tochooseeachhiddenunit’sconnectivityconstraintml(k).
|     | also applies |     | for the | first | hidden | layer | weights. |     | As for the |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------- | ----- | ------ | ----- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thus,wecouldimagingtrainingMADEtoalsobeagnostic
outputmask,wesimplyneedtoadaptitsdefinitionbyusing
theconnectivityconstraintsofthelasthiddenlayermL(k) oftheconnectivitypatterngeneratedbytheseconstraints. To
achievethis,insteadofsamplingthevaluesofml(k)forall
insteadofthefirst:
unitsandlayersonceandforallbeforetraining,weactually
mL(k)
|     |     |     |         |     |     | 1 ifd | >   |     |      | resamplethemforeachtrainingexampleorminibatch. |     |     |     |     |     |     |     | This |
| --- | --- | --- | ------- | --- | --- | ----- | --- | --- | ---- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     | MV  | =   | 1       |     | =   |       |     |     | (13) |                                                |     |     |     |     |     |     |     |      |
|     |     | d,k | d>mL(k) |     |     |       |     |     |      |                                                |     |     |     |     |     |     |     |      |
0 otherwise. isstillpractical,sincetheoperationofcreatingthemasksis
(cid:26)
|     |     |     |     |     |     |     |     |     |     | easy | to  | parallelize. | Denoting |     | ml = [ml(1),...,ml(Kl)], |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------------ | -------- | --- | ------------------------ | --- | --- | --- |
Likeforthesinglehiddenlayercase,thevaluesforml(k)
andassuminganelement-wiseandparallelimplementation
|     | foreachhiddenlayerl |     |     |     | 1,...,L   |                     | aresampleduniformly. |     |     |                 |     |     |     |                      |     |     |           |     |
| --- | ------------------- | --- | --- | --- | --------- | ------------------- | -------------------- | --- | --- | --------------- | --- | --- | --- | -------------------- | --- | --- | --------- | --- |
|     |                     |     |     | ∈   | {         | }                   |                      |     |     | oftheoperation1 |     |     |     | forvectors,suchthat1 |     |     | isamatrix |     |
|     | Toavoidunconnectedu |     |     | ni  | ts,theval | ueforml(k)issampled |                      |     |     |                 |     |     | a≥b |                      |     | a≥b |           |     |

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Hugo Larochelle, Iain Murray
To achieve this, one could consider the follow- ˆv ˆv ˆv ˆv
ing approach. To approximate the conditional 1 2 3 4
p(v |v ) under an RBM, we first find an approxima-
i <i
tion q(v ,v ,h|v ) for p(v ,v ,h|v ), such that
i >i <i i >i <i
q(v i |v <i ) can be easily obtained. Such a choice for ˆv 1 ˆv 2 ˆv 3 ˆv 4 h 1 h 2 h 3 h 4
q(v ,v ,h|v ) and a popular approach for RBMs in
i >i <i
generalisthemean-fielddistribution,whereafactorial
decomposition is assumed:
q(v
i
,v
>i
,h|v
<i
)=µ
i
(i)vi(1−µ
i
(i))1−vi
Y
µ
j
(i)vj(1−µ
j
(i))1−vj
v v v v v v v v
1 2 3 4 1 2 3 4
j>i
Y
τ
k
(i)hk(1−τ
k
(i))1−hk,
Fig
(
u
6
r
)
e20: NADFEVarScBhitNecture(bluelinesaretieNdwAeDighEts)withvinsteadofxnotation. (Source: [146])
k
where µ (i) is the marginal probability of observation
j Figure 1: (Left) Illustration of a fully visible sigmoid
v being equal to 1, given v . Similarly, τ (i) is the
j <i Urkia et al. [147]beplrioefponseetwreoarlk-.va(luReidghNtA)DIlElus(tRrNatAioDnEo)f, awhneeruerarelaaluo-utput values are computed using a GMM, so
marginal probability of hidden variable h being equal
kp(x |x )=p toreg(xres|θsiv)ewditihstθribbuetiinognthesetpimaraatmore.tervsoifsthueseGdMaMs a.
i <i GMM i i i bi
to1. Thedependenceonicomesfromconditioningon
shorthand for p(v = 1|v ). Arrows connected by a
v , i.e. for each value of i. The mean-fiIenld[1a4p8p]r,oUxir-iaetal. introduceaneifficient<piroceduretotrainNADEandRNADEmodelsforeachpossiblevariable
<i bluelinecorrespondtoconnectionswithsharedortied
mation then proceeds by finding the paraomredteerrisngµs(iim)ultaneouslybyusingsharedweightsandstochasticgradientdescenttooptimizethemeancostoverall
j parameters.
for j ≥i and τ (i) which minimize the KLorddievreirnggesn.cAefterthat,themostsuitablevariableorderingforthedatacanbedeterminedinconstanttime. Theyalso
k
between q(v ,v ,h|v ) and p(v ,v ,hi|nvtro)d.ucTehaedeepNADEwithmultiplehiddenlayersthatisefficienttotrainandoftenachievesbetterlog-likelihood
i >i <i i >i <i
most frequently used approach for doing trhesisulctosnosnistthsetesutpsewtitthhanposwinegrfluel-lfauynecrtimonosdteolsu.seinaBayesiannetwork
in setting the derivatives of the KL to 0, R yi a e i l k d o in e g t t a h l. e [149 a ] n p d ro m p o o d s e e l N th A e D c E on -kdi , t w io h n i a c l h s p c ( o v mip = ut 1 e | d v <thi ) e . densityofanoutputasthek-threcurrentpass-throughof
following equations (see Appendix for a d t e h ri e va in t p io u n t ) v : ⟨1⟩thFroourgihnsthtaennceeu,racolnnseitdweorrkthheidadpepnlilcaayteior,nsoofp(txhe=af1o|rxe- )=v⟨k⟩. Themodeloutperformsprevious
i obs i
 NADEapproachmese,nRtiBonMedsamnedanD-fiBeNldspinrodceendsuirteyfmorodonellyinogn,ealistoeroantiomna.skedinputs,andcangeneratebinaryMNIST
X X
τ k (i)=sigmc k + W kj µ j (i)+ Wdi k g j ivt j s  and(7C)altecWh-i1t0h1µs j i(lhi)ouineittteiasl.ized to 0 for j ≥ i, we can rewrite
this procedure as follows:
j≥i j<i In[150],Uriaetal. proposeConvNADE,whichreplacesthefullyconnectedhiddenlayerswithconvolutionallayers,
!
X
allowingexploitationof
p
t
(
h
v
es
=
pa
1
t
|
i
v
als
)
tr
=
uc
s
t
i
u
g
r
m
e,(cid:0)f
b
or
+
ex
(
a
W
m>p
)
le,
h
of(cid:1)2Dim
(9
a
)
ges. Theyalsocombinetheapproachwiththe
µ j (i)=sigm b j + W kj τ k (i) ∀j ≥Die.epNAD(8E)[148]architectu i re,wh < ic i husesmask i ingtoim i p ,· ro i vetheresultsofimagemodelingtasks.
h =sigm(c+W v ), (10)
k i ·,<i <i
The fixed point satisfying these equations is found
2.9 SparseCowdihnigch corresponds to a feed-forward neural network
by initializing µ (i) and τ (i) to 0 and alternating
j k with a single hidden layer, and tied weighted connec-
between applying Equations 7 and 8 from right to left.
Sparsecodingistuiosnusalglyoianngoipntiamndizaotuiotnopfrtohbelehmid,dwenhelraeyedra.taMisorreeocvoenrs,tructedbyaweightedlinearcombinationofas
This procedure is guaranteed to converge to a fixed
fewaspossiblebsainscisevtehcetroersis(soeneeFnieguurrael2n1etfwororaknfeoxraemapchlecaopnpdliitciaotnioanl). Thereconstructionandsparsitycostsofthe
point, which might not be a global optimum. Still,
linearcombinatiopn(vre=pre1s|evnti)n,gctohnendeacttaiohnasvearteoablesomtiineidmaizcerdo.ss[1t5h1e]se
i <i
the general principle of mean-field has been shown to
neural networks.
work well in practice for RBMs (Welling & Hinton,
2002;Salakhutdinov&Hinton,2009). Inthesettingof TLheeatrineedd croencneepcttivioen fsiecldasn be leveraged to speed up
convertinganRBMintoaBayesiannetwork,thevalue the computations of each conditional by sharing cal-
Outputs of sparse coding network
of µ (i) would be used as an estimate of p(v =1|v ). culations across neural networks. Indeed, the ith and
j i <i
(i+1)th hidden layer activations passed into the sig-
However, this mean-field procedure can be quite slow,
moid in Equation (10) are almost exactly the same.
with convergence often taking around 20 iterations.
The difference between the two is simply
Each iteration can be quite costly for large dimension-
alitiesofobservationsvorhiddenvectorsh. Moreover, (c+W v )−(c+W v )=W v
·,<i+1 <i+1 ·,<i <i ·,i+1 i+1 Pixelvalues
thesameprocedurewouldneedtobefollowedforeach
observation v , making it impractical. which can be computed in O(H), where H is the num-
i
ber of hidden units. Hence, the complete cost of com-
4 The Neural Autoregressive puting p(v) is O(HD), instead of the O(HD2) cost of
a naive procedure that doesn’t take advantage of the Image
Distribution Estimator
weight sharing across conditionals.
Whilenotdirectlyapplicable,themean-fieldprocedure WecalltheproposednewBayesiannetworkfordistribu-
Figure21: Exampleofanapplicationofsparsecodingtogenerateimages. (Source: [152])
ofthelastsectioncanserveasaninspirationforcoming tion estimation the Neural Autoregressive Distribution
Wangetal. [153]proposeusingsparserepresentationsofimagepatchesforsuper-resolution. Theyassumethata
31
low-resolution image patch and its closely related high-resolution pendant share the same sparse code α =
lowres
23

| ComprehensiveExplorationofSyntheticDataGeneration: |     | ASurvey |     |     |     |
| -------------------------------------------------- | --- | ------- | --- | --- | --- |
α =αgivenproperlydefinedreconstructiondictionariesD andD . Theyapplyfeedforwardneural
| highres |     |     | lowres | highres |     |
| ------- | --- | --- | ------ | ------- | --- |
networkstocomputeapproximatesparsecodes.
Tonolini et al. [151] propose Variational Sparse Coding, which incorporates sparse coding at the inputs of a VAE
recognitionmodeltoimprovefeaturedisentanglementinthelatentcode. ThemodelisevaluatedontheFashionMNIST,
celebA(celebrityfaces),andUCIHAR(accelerometerandgyroscopetime-seriesdataofhumanactivities)datasetsto
investigatethedisentanglementoffeaturesinthelatentspaceandprovidespromisingresultsandvisuals.
2.10 RecurrentNeuralNetworks
RecurrentNeuralNetworks(RNNs)areasupersetoffeedforwardneuralnetworkswhichincluderecurrentedgesthat
incorporatehiddenstatesofprevious,andinsomecasessubsequenttimesteps. Thisenablesthemodeltoprocess
sequentialdataofarbitrarylengthoneatatimewhilemaintainingamemoryofthepast. InthecontextofSDG,RNNs
areespeciallyusefulforspeechsynthesis,musicgeneration,ortimeseriesprediction. [154]
Figure22: Left: AsimpleRNNnetwork. Right: Depictionofthevanishinggradientproblem,wherethroughweights
lessthanone,theinfluenceofthefirstinputwilldiminishovertime. (Source: [154])
InasimpleRNN(seeFigure22,left)attimestept,thecurrenthiddenstateh(t)dependsonthecurrentinputexample
x(t)andthepreviousstateh(t−1),resultingin
|     | h(t) =σ(W | x(t)+W | h(t−1)+b | )   | (24) |
| --- | --------- | ------ | -------- | --- | ---- |
|     |           | hx     | hh       | h   |      |
withthesigmoidactivationfunctionσandtrainableweightmatricesW ,W andbiasb . Thepredictedoutputyˆ(t)
|     |     |     | hx  | hh h |     |
| --- | --- | --- | --- | ---- | --- |
isthencomputedfromh(t),so
|     | yˆ(t)      |     | h(t)+b |     |      |
| --- | ---------- | --- | ------ | --- | ---- |
|     | =softmax(W |     | yh y   | )   | (25) |
with bias b and trainable weight W . The weights are usually trained using BPTT, which can suffer from the
y yh
vanishing gradient problem (see Figure 22, right), which LSTMs, a special kind of RNN, and GRUs, a simplified
| versionofLSTMs[155],aimtosolve. | [154] |     |     |     |     |
| ------------------------------- | ----- | --- | --- | --- | --- |
Boulanger-Lewandowskiet al. [156] generalize RTRBMs and introducethe RNN-RBM, which combinesan RNN
withdistincthiddenunitswithanRBM,whosehiddenunitsarerelatedtotheRNN’sonesandvisibleunitsinfluence
thenexthiddenstateoftheRNN. TheRBM’sabilitytogeneratecomplexdistributionsforeachtimestepallowsthe
authorstomodelandgeneratepolyphonicmusicinabinarymatrixpiano-rollrepresentationbutnotobservelong-term
musicalstructure.
Gravesetal. [157]proposeadeepRNNwithN stackedrecurrentlyconnectedLSTMhiddenlayersthat,ateachstep,
computethepredictionprobabilityforthenextword. Thenetworkalwaysstartswithanullvectorasthefirstinput,
soalldataisgeneratedwithoutpriorinformation. First,theyevaluatetheirmodelonone-hot-encodeddiscretetext
dataandthenononlinehandwritingdata,asequenceofpentiplocations,togeneraterandomhandwrittencharacter
sequences. Next,theycombinethehandwritingapproachwithatargetcharactersequencetogeneratehandwritingfora
24

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
giventext. ThisworksbyprovidingaweightedwindowonthetargettextateachRNNtimesteptothehiddenlayers.
Theapproachiscapableofproducingrealisticresults.
Ranzatoetal. [30]introducerCNN,anunsupervisedrecurrentconvolutionalneuralnetwork,topredictthenextframe
ofavideo. Themodelsplitsthevideoframeinto8×8pixelpatchesandfeedsa9×9patchoftheirquantizedvalues
intoaRNNtocreateanembedding,whichisthenprocessedbytwoconvolutionallayerstopredictthecentralpatch.
The patch-wise convolutional processing allows the rCNN to process videos of arbitrary frame size. The authors
evaluatetheirmodelontheUCF-101sportclipdataset,resultinginbetterperformancethann-gramsandtheneuralnet
languagemodel[31].
Vinyalsetal. [158]generatecaptionsforimagesusinganend-to-endencoder-decoderarchitecture,fullytrainablewith
stochasticgradientdescent. TheNeuralImageCaption(NIC)modelencodesimagesusingthelasthiddenlayerofa
CNNpre-trainedforimageclassificationandfeedingittotheLSTMdecoder,whichaimstomaximizethelikelihood
ofthesentencebeingacorrecttranscriptionoftheimage. Themodelachievesstate-of-the-artBLEU,METEOR,and
CIDERscoresforthetime(2015)onthedescribedimagedatasetsPascalVOC2008,Flickr8k,Flickr30k,MSCOCO,
andSBU.
Donahueetal. [159]proposetheLong-termRecurrentConvolutionalNetwork(LRCN)forimageinterpretationtasks.
ImagesareprocessedbyasingleCNNtoextractvisualfeatures,andaLSTMencodercreatesatotalrepresentation
fromthesefeatures. ALSTMtakestheimagerepresentationandthepreviouswordasinputsandgeneratesadescription
wordbyword. Theauthorsextractentitiesandtheirrelationsfromvideosforvideodescription,andtheLSTMdecodes
theentitycollectionintoameaningfulsentence.
Srivastavaetal. [160]useLSTMstolearnrepresentationsofvideosequencesanddecodethemtopredictfutureframes
or reconstruct the input sequence. They also propose a composite model performing both tasks simultaneously to
overcometheirshortcomings. Thetrainingisconductedusingbackpropagation,andthemodelsareevaluatedonthe
UFC-101,HMDB-51,Sports-1M,andmovingMNISTdigitsdatasets. Thefuturepredictionresultsarequiteblurry,
buttherepresentationsworkwellforactionrecognitionwhenfedintoaclassifier.
Mansimovetal. [161]presentAlignDRAW,whichextendstheDRAWmodel[97]togenerateimagesgivenacaption.
ThecaptionisdefinedasasequenceofwordsandisencodedusingabidirectionalRNN,whichconsistsofaforward
andbackwardLSTMwhoserepresentationsateachtimestepareconcatenated. ThegenerativeRNNworkssimilarlyto
DRAWbyincludingtherespectivecaptionrepresentationateachtimestepanditerativelyimprovingthequalityofthe
existingimage. Themodelalsogeneratesplausibleresultsforpreviouslyunseentypesofcaptions.
Jaques et al. [162] adopt LSTMs to music generation by training them to predict the next note on a large training
corpus. TheythenuseReinforcementLearning(RL)tooptimizetheirNote-RNNbycombiningarewardfunctionbased
onrulesofmusicaltheorywiththeoutputofanotherfixedcopyNote-RNN.Theyachievemorecoherentresultsthat
complywithmusicaltheory,avoidingthesometimesoccurringrandomnessofRNNs. Theyalsodiscusstheapplication
ofRLtootherdomainssuchastextgeneration,whichcouldbeusedtoenforcecorrectgrammar.
VandenOordetal.[115]advancetwo-dimensionalRNNstosequentiallypredictpixels(morespecifically,theirdiscrete
RGBchannelvalues)alongthetwospatialdimensionswiththehelpoflearnedprobabilitydistributionsandasoftmax
function. Theyproposetwodeep(upto12layers)LSTMarchitectures(seeFigure23),alsocalledPixelRNNs: The
rowLSTM,whichprocessestheimagerowbyrowfromtoptobottom,andthediagonalBiLSTM,whichusestwo
LSTMsstartingateachtopcornerandcrossingtheimagediagonallytocapturemorecontext. ThediagonalBiLSTM
outperformstherowLSTMandothermodelslikePixelCNN,DRAW,andDLGMsinimagedensityestimationtasks.
Row LSTM Diagonal BiLSTM
Figure23: TherowLSTM(left)anddiagonalBiLSTM(right)PixelRNNs. (Source: [115])
Waite et al. [163] propose Lookback and Attention RNN, which try to improve the long-term structure modeling
capabilities of recurrent networks for music generation. The basic LSTM takes the one-hot encoded vector of the
25

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
previousmelodyeventasinput. LookbackRNNtakestwomorepreviouseventvectors,thecurrentpositioninthe
musicmeasure(e.g., 4),andwhetherthelasteventrepeatstheeventoftheprevioustwoevents. TheLSTMnowhas
4
tolabelnewvectorsas“repeat-1-bar-ago”,“repeat-2-bars-ago”,oranewmelodyevent. TheAttentionRNNusesan
attentionmechanismtolookattheweightedsumofthepreviousnoutputstogeneratethecurrentstepresult. The
modelcanbetrainedonMIDIfilestocreatesimilarmelodies.
Hadjeresetal. [164]introducetheAnticipation-RNN,whichenablestheinteractivegenerationofmusicbyallowing
user-definedpositionalconstraints. Becausetheincorporationoffutureconstraintsinasequentialprobabilisticmodel
wouldbecomputationallyexpensive,abackwardConstraint-RNN goingfromconstraintN to1isproposed,whose
step-wiseoutputsarecombinedwiththeinputstateoftheforwardTokenRNN,whichgeneratesthemusictokensfrom1
toN. ThemethodisgeneralandcanbeappliedtootherRNN-basedapproaches.
Oore et al. [165] train a LSTM on the Piano-e-Competition MIDI data set to generate natural-sounding piano
performancesintheMIDIeventspacewithvaryingdynamicsandvelocity. TheLSTMinputsareone-hotencodings
overtheMIDIeventvocabulary(variousNOTE-ON,NOTE-OFF,TIME-SHIFT,andVELOCITYevents),andthe
modelcomputesasoftmaxprobabilitydistributionfortheoutputeventconditionedontheinputeventsfromwhichit
samples. Themodelcangeneratemusicfromaninitialstartingsequenceorfromscratch(anemptysequence)that
comesclosetohumanimprovisation. Itdoesnotjustcopythetrainingsamplesbutcannotdecideonacoherentplay
style. Theauthorsprovethatpowerfulgenerativemodelsformusicarepossiblewithoutdefiningrulesorheuristicsat
allandwithoutobservinglong-termrelationshipsinthedata.
ShortoverviewofotherusagesofRNNs:
Approach Description Year
[166] RNN-NADE:CombiningRNNswithaNADE[146]tooutputmultivariatepredictions(prob- 2012
abilities)formusicdata.
[167] Experimentswithsubword-levellanguagemodels,resultinginsmallermodelsthancharacter 2012
orword-basedapproacheswithsimilarperformanceandnoout-of-vocabularypredictions.
[168] AreferencemelodyandchaoticunitsaregiventoaLSTMasinputtogeneratenewmelodies 2013
withapredefinedmelodiouness.
[169] Application of fast dropout to RNNs, which drops each incoming unit of a neuron with a 2013
certainprobability,resultinginarespectivezerovalueintheweightedsumfortheneuron
activation. ExperimentsonpolyphonicmusicgenerationindicatethatshallowRNNsperform
betterwithdropoutthroughbettergeneralization.
[170] ExperimentswithmultipledifferentdeepRNNsonlanguagemodelingandpolyphonicmusic 2013
generation tasks. They implement deep state transition and output functions and improve
overconventionalshallowmodels,exceptoneswithfastdropout[169]oroncharacter-wise
generation,wherethesubwordRNN[167]performsbetter.
[171] VideodescriptionbyextractingfeaturesfromeachframewithaCNN,applyingmeanpooling 2014
acrossallframeembeddingsandfeedingtheresulttoaLSTMwhichgeneratesthedescription.
[172] Chinesepoemgenerationfromuser-suppliedkeywords. Chinesesymbolsareone-hotencoded. 2014
Aconvolutionalsentencemodelcreateslineembeddingsfedtoarecurrentcontextmodelthat
forwardsacontextvectortotherecurrentgenerationmodelthatcreateswordafterwordfor
thecurrentline.
[173] Stochastic Recurrent Networks (STORNs): Two RNNs, the recognition (encoder) model 2014
q(z |x )fromwhichz issampled,andthegeneratingmodelp(x |z ),fromwhichx
t 1:t−1 t t 1:t t
isobtained,formanetworkeasilytrainablewithstochasticgradientdescentthatcanmodel
multiplevariablesateachtimestep. Additionally,thelatentrepresentationsz areconditioned
t
on a prior p(z) like a VAE. The model is evaluated on polyphonic music generation and
motion capture data continuation, where it outperforms previous RNN approaches except
RNN-NADE[166].
[174] ClockworkRNN:PartitionofhiddenlayersintoseparatemodulesiwitharbitraryperiodsT 2014
i
thatareactiveattimesteptonlyift mod T =0. Thisreducesthenumberofparameters
i
andincreasestheperformanceonsequencereconstructiontasks.
[175] LSTMtrainingwithresilientpropagation[176]insteadofBPTTforimprovedmusiccompo- 2014
sitionrepresentedas“binary”pianokeypresses.
[177] RNN-DBN: VerysimilartotheRNN-RBM[156],thismodelcombinesRNNsandDBNs, 2014
whichareRBMswithmultiplestackedhiddenlayers. Itisalsousedforpolyphonicmusic
generationandimprovesupontheRNN-RBMresults.
Continuation...
26

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[178] MultimodalRNN(m-RNN):ARNNthatmodelsthenextwordprobabilitydistributionbased 2014
onthepreviouswordandtheencodingofanimageprovidedbyaCNN.
[179] Recurrentimagedensityestimator(RIDE):CombiningspatialLSTMs[180]thatcomputethe 2015
hiddenstateh ofthenextpixelx basedonthetwoaxis-wiseprecedingstatesc and
ij ij i,j−1
c ,andmixturesofconditionalGaussianscalemixture[181]thatpredictthestateofthe
i−1,j
nextpixelp(x |h ).
ij ij
[182] BidirectionalRNNsasgapfillersinhigh-dimensionalcategoricalandbinarytimeseriesdata 2015
(e.g.,music),outperformingunidirectionalRNNsandbeingapplicableinmorescenarios.
[183] VariationalRNN(VRNN):ArecurrentVAEforhigh-dimensionalsequencegenerationusing 2015
thehiddenstateh ofaRNNastheparameterforthedistributionofthelatentrandomvariable
t
z oftheVAEateachstep. Themodeloutperformssimplerconfigurationsinunconditional
naturalspeechandhandwritinggeneration.
[184] Scheduledsampling: Tobridgethegapbetweentraining,whereusuallytheground-truthpre- 2015
vioustokenx istakenforthenextprediction,andinference(generationofnewsequences)
t−1
distributions,wherethemodelusesitspreviouspredictionxˆ ,itisrandomlydecidedduring
t−1
trainingforeachtokenprediction,whetherx orxˆ istaken. Improvedresultsonimage
t−1 t−1
captioning (CNNencoder) and speech recognition compared to a baseline LSTM without
scheduledsampling.
[185] Mind’sEye: Learningbi-directionalmappingsbetweenvisualfeaturesofimages(obtained 2015
fromaVGG[186])andtheirtextdescriptionswithRNNs. Themodelcanbeusedtogenerate
inbothdirectionsbyfirsttrainingaRNNtogeneratethetextfromthefeaturesandthena
secondRNNontoptoreconstructthevisualfeaturesfromthetext.
[187] Alignmentofvisual(objectdetectorCNN)andlanguage(bidirectionalLSTM)representations 2015
ofimageregionsforfull-frameandregion-levelimagedescriptionwithRNNdecoding.
[188] DBN-LSTM:ImprovedversionoftheRNN-DBN[177],wheretheRNNisreplacedwitha 2015
LSTMforbetterperformanceinpolyphonicmusicgeneration.
[189] LSTM-RTRBM: ReplacementofsomehiddenunitsofaRTRBMwithLSTMones,which 2015
increasesperformanceandlearningspeed.
[190] Imagecaptioningwithconvolutionalfeatureextractionandanattention-basedLSTMthat 2015
generatesthecaptionword-by-word.
[191] VideodescriptionwithCNN-encodedvideoframesasinputforatwo-layerLSTMthatstarts 2015
outputtingwordsafterthewholevideosequencehasbeenprocessedbythefirstLSTMlayer.
[192] Videodescriptionwitha3DCNNencoder(width×height×timestepsofvideo)andLSTM 2015
decoderwithtemporalattentionmechanism.
[193] A stochastic recurrent neural network (SRNN) with separate stochastic and deterministic 2016
layerspropagatesuncertaintyinlatentspacethroughthenetwork. Thehiddenrepresentation
z depends on a prior p(z |z ), similar to a VAE, parameterized by a neural network.
t z t−1
Achievesstate-of-the-artperformanceonspeechandpolyphonicmusicmodeling.
[194] Single-notemelodygenerationandcontinuationwithamulti-layerGRUtrainedonsequences 2016
ofcorrespondingpitchanddurationone-hotvectors.
[195] ImprovedLSTMtrainingformusiccomposition. Pitchesanddurationsofnotesareencoded 2016
together in one one-hot vector. Training is split into two parts, where first, the model is
trainedwithrealdata,andnewcompositionsaregenerated. Thesecreationsarefilteredbythe
grammarargumentedmethod,whichonlyallowssamplescomplyingwithdefinedmusical
rules to remain. These are then appended to the training data, and the model is retrained,
resultingintheactualgenerativemodel.
[196] TrainingofasequencepredictionRNNactor withasecondcriticnetworkthathasaccess 2016
to the ground-truth data and computes the expected task-specific score. The RL-inspired
actor-critictrainingapproachfitstrainingdatafasterthanmaximum-likelihoodlearning. It
providesmorecoherentandaccurateresultsontextpredictiontasks(i.e.,spellingcorrection
andmachinetranslation).
[197] ReviewNetwork: Anencoder-decoderframeworkwithreviewersinbetweenthatprovidea 2016
discriminativeloss. Additionally,anattentionmechanismbetweentheencoderandthereview
networksandthereviewnetworksandthedecoderisimplemented.TheencodercanbeaCNN
orRNN,whilethedecoderisaLSTM. Themodelisusedtocaptionimagesandgenerate
commentsforJavasourcecode.
Continuation...
27

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[198] ImagecaptioningbasedonCNNencoder,visualattributeprediction(i.e.,whathappensinthe 2016
picture),aLSTMforstateprogression,andtwodifferentattentionmechanismsforinputand
outputthatdeterminethenextwordfromthevocabulary.
[155] VideodescriptioninoneormultiplesentencesusingahierarchicalRNNswithasentenceand 2016
paragraphgenerator. ThenetworkisbasedonGRUsandusestemporalandspatialattention
mechanisms.Inputfeaturesofthevideoareobtainedfromapre-trainedconvolutionalextractor
[186].
[199] Two text-based LSTMs (word-RNN and char-RNN) learn chord progressions from text 2016
representationsofmusicforfullyautomaticmusiccomposition.
[200] Multi-trackpopmusicgenerationwithahierarchicalLSTMwhereeachlayerisresponsible 2016
forpredictingacertainaspectofthesongatatimestep: Thebottomlayerpredictsthepressed
key,thenextlayerthedurationofthepress,thethirdthechordandthefourthandlastlayer
thedrumbeat.
[201] Folk-RNN:Large-scalegenerationofCelticfolkmusictranscriptionswithLSTMstrained 2016
withavocabularyoftokensonsingletranscriptions. Evaluationisperformedonthelarge-
scaledistributionsofrealandgenerateddataandthesingletranscriptionlevel. TheLSTMs
automaticallylearntoconformtostructuralconstraintsoffolkmusic.
[202] BachBot: Athree-layerstackedLSTMwithoptimizedparametersgeneratesBachchorales 2016
ortransferstheirstyletoothermelodies. Itistrainedwithteacherforcing(alwayscontinue
predictionwiththecorrectprevioustoken)onframe-basedrepresentationsofthepolyphonic
pianorolldata.
[203] Two-layerLSTMfortoken-levelmusicgenerationfromashortseedsequence. EachMIDI 2016
messageorexistingnotecombinationfromapianorollrepresentationistreatedasaseparate
token. TheresultsarecomparabletoRNN-NADE[166].
[204] SampleRNN:Anunsupervisedandunconditionalend-to-endmodelforrawaudiowaveform 2016
synthesiswithhierarchicalRNNsthatcoverdifferenttemporalranges.
[205] Applicationofa(bidirectional)hierarchicalrecurrentencoder-decoder(HRED)todialogue 2016
generationbyutilizingquestion-answerpairsandpre-trainedwordembeddings. Themodel
consistsofaRNNencoder,whosefinalrepresentationisfedintoacontextRNN,whichmaps
therepresentationintothedialoguecontext. Thecontextstateisthenfedtoeachstepofthe
decoderRNN.
[206] The “Professor Forcing” algorithm is designed to align the behaviors of recurrent neural 2016
networksduringtrainingandsamplingphases,addressingacommonissueinRNNtraining.
Thismethodappliesadversarialdomainadaptation,wherethenetworkistrainedtomakeits
behaviorindistinguishablebetweenthesetwophasesunderthescrutinyofadiscriminator.
Thisapproachhelpsinproducingmorecoherentandstructuredoutputs. Thealgorithmserves
asaregularizationtechnique,enhancingthenetwork’sabilitytogeneralizefromitstraining
data,leadingtoimprovementsinperformanceonvarioustasksincludinglanguagemodeling
andimagesynthesis.
[207] Char2Wav: End-to-endspeechsynthesisfromtext. AbidirectionalRNNencodestext,anda 2017
RNNwithattentiondecodestherepresentationatdifferenttimestepstoproducefeaturesfora
vocoder. ThevocoderisaconditionalSampleRNN[204]thatproducesrawwaveformoutput
fromthevocoderfeatures.
[208] RecurrentHighwayNetwork: LSTMswithmultiplehighwaylayers[209]thatallowdeep 2017
step-to-steptransitionfunctionsthatareeasilytrainable. Themodeloutperformsprevious
RNNsincharacterpredictiontasksonWikipediatexts.
[210] DeepArtificialComposer(DAC):Extensionof[194]thatusesLSTMs(durationandpitch 2017
RNN)togeneratenotetransitionsandistrainedonacorpuswithtwodifferentmusicalstyles.
Italsoemphasizesanewnoveltymeasure(fractionoftransitionsfoundinadefinedcorpus)
thatisusedtoimprovethecreativityofthemodel.
[211] Improvementofimagecaptioningwithattention[190]bysupervisedtrainingoftheattention 2017
mechanismwithgroundtruthtextentity-imageregionmappingsobtainedfromhumans.
[212] SemanticCompositionNetwork(SCN):Imagecaptioninginmultipleparts: ACNNextracts 2017
afeaturevector,andaMLPcomputesprobabilitiesoftagsbasedonthemostusedwordsin
thetrainingdescriptions. ALSTMthengeneratesthedescriptionbasedonthefeaturevector
andthetagprobabilities.
Continuation...
28

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[213] DeepBach: GenerationorreharmonizationofBachchorales/MIDIdatausingdeepLSTMs 2017
workinginoppositedirectionsandneuralnetworksthatmergetheRNNresults. Sampling
fromthisdependencynetworkisperformedusingpseudo-Gibbssampling.
[214] Conditionaldrumrhythmgenerationwithacombinationofatwo-layerstackedLSTMthat 2017
learnsdrumsequencesandafeedforwardfullyconnectedlayerthatprocessesmetricalrhythm
andabasssequenceasconstraints. Theirpredictionsaremergedtopredictthenextdrum
event.
[215] Sequence Tutor: An improved fine-tuning approach for RNNs that first trains an RNN on 2017
datawithmaximum-likelihoodestimationandusesitsoutputasapolicy(originallyproposed
in [162]) for a second RNN trained with RL for a specific domain. The effectiveness is
demonstratedonmusicmelodyandmoleculegeneration(i.e.,SMILES[112]strings).
[216] ChordprogressiongenerationfrommonophonicmelodieswithBiLSTMs. 2017
[217] Latentvariablehierarchicalrecurrentencoder-decoder(VHRED):Astackofencoder,context, 2017
anddecoderRNNscombinedwithastochasticlatentvariableconditionedonallpreviously
observedtokensthatcancapturethedependenciesofsub-sequencesofsequentialdata. The
stochasticvariableallowsfordiverseandcoherentdialoguestobegenerated.
[218] Harmonic Improviser: A LSTM harmony agent trained on Jazz chord progressions and a 2017
rule-basedmelodyagentmanipulatingprovidedmelodiestaketurnsimprovisingmusicin
real-timeandarerewardedforharmonicconsistencyandmelodicflow.
[219] PerformanceRNN:MIDImusicgenerationwithaLSTMshowingtiminganddynamics,but 2017
lackinglong-termcoherence.
[220] TP-LSTM-NADE & BALSTM (biaxial LSTMs): Modification of an RNN-NADE [166] 2017
to model relative differences between nodes for transposition-invariant polyphonic music
generation.
[221] Combination of a biaxial LSTM [220] for symbolic music generation and a conditional 2018
WaveNet-basedaudiogeneratorforwaveformmusicgeneration.
[222] GraphNeuralNetworks(GNNs): Computinganditerativelyupdatingnodeandgraphem- 2018
beddings using fully connected neural networks, GRUs for nodes and LSTMs for edge
modifications. MLPsareusedtosequentiallycomputeprobabilitiesofaddingnewnodes(and
theirtype)andedgesbasedontheserepresentations. Themodelcanworkconditionallyand
unconditionallyandisdemonstratedonmoleculegeneration.
[223] WaveRNN:Asparsesingle-layerRNNmainlyfortext-to-speechsynthesiswherethemajority 2018
ofweightsareprunedandsubscalingisemployedtofoldlongsequencesintoabatch(matrix)
ofshortones,whichallowsgeneratingmultiplesamples(i.e.,overmultiplerows)atonestep.
ThisallowsthemodeltoproduceresultsinrealtimeonamobileCPU.
[224] RelationalRNN: ALSTMwithamulti-slotmemorymatrixinsteadofthehiddenstatevector. 2018
Inputisconcatenatedtothematrixasanewrow,andmulti-headdotproductattention[18]
isappliedtogeneratethenextmemorystate. Themodelachievesstate-of-the-artresultson
languagemodelingtasks(next-wordprobability).
[225] DeepJ:AmodelbuiltuponthebiaxialLSTM[220]structureandincorporatedynamics(i.e., 2018
relativenotevolume)innoteembeddingsandglobalstyleandcontext(e.g.,genre)conditioning
in the network. They train three outputs simultaneously (play and replay probability and
dynamics)forthepredictednotes.
[226] GraphRNN: Generate large variable-length graphs without node ordering by treating the 2018
problem as a sequence of node and edge additions. At each step i, the graph-level GRU
updates the graph state h and adds a new node. The edge-level RNN then creates the
i
adjacencyvectorforthenewnodetoalloldnodesortheend-of-sequencetokenfromh . The
i
modelistrainedondataobtainedusingbreadth-first-searchthroughanygraphpermutation
with a random starting point. The graphs are evaluated by computing a Maximum Mean
Discrepancy(MMD)scorebetweenthedegreeandclusteringcoefficientdistributionsand
orbitcountstatisticsbetweensetsofgraphs.
[227] Tacotron2: Arecurrentsequence-to-sequencetext-to-speechnetworkconsistingofmultiple 2018
LSTMsandCNNsthatmapscharacterembeddingstosimplifiedmelspectrogramsthatare
thenconvertedtowaveformaudiowithWaveNet[228].
Continuation...
29

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[229] GraphRecurrentAttentionNetwork(GRAN):ImprovementuponGraphRNN[226]usinga 2019
GNN[222]withattentionateachsteptogenerateablockofnewnodesandedgesbasedon
thealreadyexistinggraph. Further,theyproposetrainingonadjacencymatricesconforming
tofamiliesofnodeorderings(e.g.,nodessortedbynodedegree,breadth/depth-first-search
orderingfromlargestdegreenode,originaldataorder)toimprovemodelunderstanding.
[230] Generatingundirected,fullyconnectedgraphswithoutself-loopsasanorderededgesequence 2019
usingGRUs. ThefirstGRUpredictsthesequenceofthefirstnodesoftheedgepairs. The
secondGRUoutputstheprobabilitiesforthesecondnodeoftheedge. Thegraphnodesare
assignedafixedorderinadvanceandtheRNNsaretrainedtomaximizethenodeprobabilities
observedinthetrainingdata. ThissimplemodelperformssimilarlytotheGraphRNN[226].
[231] MolecularRNN:ExtensionofGraphRNN[226]thatusesaNodeRNN tocomputethenext 2019
atomtypeandanEdgeRNN tocomputethebondtypestothepreviousatoms. Themodel
enforcesvalidper-atomvalency. Itisfirsttrainedtoreconstructthetrainingdataandthen
fine-tunedusingaRLcriticthatrewardsmoleculeswithcertainproperties.
[232] DeepGraphDistributionLearning(DeepGDL):Decomposingagraphintodenselyconnected 2019
componentswithsparseconnectionsbetweenthesecommunities. AGRUisthentrainedto
learn the distribution of nodes and edges in these communities based on earlier node and
edgeobservations. Syntheticcommunitiesaresampledfromthesepredicteddistributionsand
probabilisticallyconnectedtoproducenewlargegraphs(syntheticpowergrids)withsimilar
propertiestotherealdata.
[233] Generationofbiomedicalsignals(electrocardiogram,etc.) forpatientsorspecificeventsusing 2020
bidirectionalRNNsthataretrainedwithrealpatientdata. Inthefirstoptionalstage,noiseis
injectedintotherealsignals,andthenthesignalissegmentedaccordingtocertaineventsor
classes. Finally,theBiRNNgeneratesnewsimilardatabasedontheinput,andastatistical
stageevaluatesthedataquality.
[234] GraphGen: Adomain-agnosticandscalablelabeledgraphgenerationmethodusingaLSTM 2020
to sequentially append tuples containing the sequence and types of nodes and edges in a
depth-firstsearchorder. OthermodelslikeGraphRNN[226]areoutperformedinalmostevery
evaluatedcriterion.
[235] Scramble: MusicgenerationwithpitchtransitionsgeneratedbyaMarkovchainandaLSTM 2022
thatimposesalearnedstyle(velocity,rhythm,andbeatsperminute)onthepitchsequence,
whichtheusercanalsotweak.
2.11 ConvolutionalNeuralNetworks
ConvolutionalNeuralNetworks(CNNs)areartificialneuralnetworksbasedonmatrixoperationsthatcanhandledata
oflargesizeslikeimagesorspeechwithsignificantlyfewerparameterstotrainthanafullyconnectedneuralnetwork.
Themodelcancontaindifferenttypesoflayers[236]:
Convolution A kernel or filter, which is a lower-size matrix consisting of trainable weights, is applied to parts of
the input matrix to extract local features, for example, to detect edges in an image. The kernel is moved
overtheinputleft-to-right,andtop-to-bottombyastride,whichdefinesthenumberofunitsshiftedateach
step,tocomputetheoutputvalueatthiskernelpositionthroughmatrixmultiplicationoftheweightswiththe
respectivevaluesintheinputatthekernel’sposition(seeFigure24a).
Padding Topreventlossofinformationattheborderoftheinputortopreservetheinputsize,azero-paddingcanbe
addedaroundthematrix.
Non-linearity Afteraconvolutionlayer,anon-linearfunctionisusedtomodifyorcutofftheoutput. Typically,the
rectifiedlinearunit(ReLU)functionReLU(x)=max(0,x)isused.
Pooling Apoolinglayerdownsizesitsinputtoreducecomplexityforlatermodellayers. Popularimplementationsare
max-poolingoraverage-pooling,whichreturnaregion’smaximumvalueoraverage,respectively. Theyare
appliedinthesamemannerasakernel.
Fullyconnectedlayer Finally,acomputationallyexpensivefullyconnectedlayerisappliedtothesignificantlysmaller
inputto,forexample,classifyanimageorperformanothertask. AnillustrationofsuchaCNNarchitectureis
providedinFigure24b.
Lotter et al. [237] predict future frames of image sequences by first learning a representation of each single input
imagewithaCNN. Then,aLSTMprocessestheimagessequentiallyinorderbeforethefinaloutputisforwardedtoa
30

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
(a)Applicationofkernelsorpoolingfunctionstoaninputmatrixwithstride1.(Source:[236])
Convolutions (filter) ReLu Pooling (subsampling) Fully connected NN
Filter of feature
Concatenate
Yes
No
Input Data
Feature maps Feature maps Feature maps
(b)ExampleCNNarchitectureforanimageclassificationtask.(Source:[17])
Figure24: IllustrationsofthestructureofaCNN.
deconvolutional(i.e.,reversed)CNN,whichproducesanimagefromtheRNNprediction. Theytrainthemodelusing
meansquarederrorbutalsoexperimentwithadversarialloss[238]realizedbyasimilarCNN-LSTMdiscriminator
whosefinalpredictiontogetherwithanencodingofthegenerator’sresultimageortherealnextframeispassedtoa
MLP. Themodelcanpredictmovementsandrotationsinvideoswell,whichsupportstheideathatpredictionmay
enablethedevelopmentoftransformation-tolerantobjectrepresentations.
Brunaetal. [239]proposeCNNsforhigh-dimensionalstructuredpredictionproblemssuchasimagesuper-resolution.
Theymodeltheconditionaldistributionp(y|x)asaGibbsdensityp(y|x)∝exp(−∥Φ(x)−Ψ(y)∥2),whereΦ:RN →
RP andΨ:RM →RP arehighly-informativenon-linearmappings(sufficientstatistics)obtainedfromdeepCNNsthat
“minimizetheuncertaintyofygivenx”. Themodelcanprovidesolutionswithspatialcoherence. Still,theinferenceis
computationallycostlycomparedtoGANs,andatrade-offbetweensharpnessandstabilitymustalwaysbemade.
VandenOordetal. [115]proposethePixelCNN,whichconsistsofmultipleresolution-preservingconvolutionallayers
withmasks(seeFigure25)toignorefuturepixels. LikethePixelRNNs,asoftmaxfunctionisusedtocomputethe
discreteRGBvaluesofpixelssequentiallyforimagegenerationandcompletiontasks. TheadvantageofthePixelCNN
overthePixelRNNisthepossibilityofparallelizationduringtrainingandevaluationoftestimages,buttheperformance
isworse. Themodelhasbeensuccessfullyadaptedtovideocontinuationasadecoder[240].
VandenOordetal. [228]introduceWaveNet,whichoperatesontherawaudiowaveformandissimilartoPixelCNN
[115]inthatitmodelstheconditionalprobabilitydistributionp(x |x ,...,x )withastackofconvolutionallayers. It
t 1 t−1
usesdilatedcausalconvolutions(seeFigure26)topreserveorderingandprocessanarealargerthantheconvolution
lengthbyskippingvaluesbyastep. Themodelcanbetrainedinparallelbutgeneratesnewaudiosequentially. The
modelcanalsoeasilybetransformedtoincorporateadditionalinput(e.g.,textandspeakeridentityfortext-to-speech)
byappendingittotheconditionaldistribution,resultinginaconditionalWaveNet. WaveNetachievesstate-of-the-art
resultsintext-to-speechtasksandallowsconditioningondifferentspeakers. Further,themodelcangeneratenoveland
realisticmusicalfragments.
Gatys et al. [242] propose to use a deep CNN [186] to separate style (texture) and content (object recognition)
representationsofanimageforstyletransfer. Thestyletransferworksbyextractingmultiplelayersofstyleandcontent
representationsfromstyleandcontentreferenceimages,respectively. Then,awhitenoiseimage⃗xisinitializedand
iterativelyoptimizedusinggradientdescentwithrespecttothepixelvaluesbasedonthecombinedstyleandcontent
losses,whicharethesumofsquarederrorsbetweentherespectiverepresentations(styleimageand⃗x,⃗xandcontent
image).
Kimetal. [243]usearecursiveCNNforimagesuper-resolution. First, anembeddingnetwork, similartoaMLP,
encodesanimageasasetoffeaturemaps. ThentherecursiveCNNappliesthesameconvolutionfollowedbyaReLU
31

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
^
X
t
^
X
t-1
Output layer
Hidden layer
Hidden layer
Input layer
X X X
t-6 t-1 t
Figure25: Auto-regressive1DsignalmodelingwithamaskedCNN. (Source: [241])
Output Output
Dilation = 8
Hidden Layer Hidden Layer
Dilation = 4
Hidden Layer Hidden Layer
Dilation = 2
Hidden Layer Hidden Layer
Dilation = 1
Input Input
(a)Causalconvolution:Amaskedconvolutionwhereonlyprevi- (b)Dilatedcausalconvolution:Onlytimestepswithacertainstep
oustimestepsareconsidered. betweenthemareconsidered.
Figure26: Illustrationsofacausalanddilatedconvolution. (Source: [228])
totheembeddingtoincreasetheobservedrangebeforeareconstructionnetwork,alsosimilartoaMLP,createsthe
finaloutput. Tosolvetheproblemsofvanishing/explodinggradientsandfindingtheoptimalamountofrecursions
duringtraining,eachrecursivelayerisreconstructed,andaweightedaverageofallpredictionsproducesthefinaloutput
(recursivesupervision). Askipconnectionbetweentheinputimageandthereconstructionnetworkisestablishedto
improveresultsfurther. ThemethodoutperformsSRCNN[244,245]andprovidesclearerimages.
Salimans et al. [246] accelerate PixelCNN training and generate state-of-the-art results on class-conditional and
unconditional image generation task CIFAR-10 with their improved implementation called PixelCNN++. They
computetheRGBvaluesofpixelsassuminglineardependenceandusingcontinuousdistributionsthatarerounded
insteadof256-waysoftmaxtoreducetrainingcost. Further,theyintroducedownsamplingandshortcutconnections
betweenlayerstobettercapturetheinputstructureandusedropoutregularizationtopreventoverfitting.
ShortoverviewofotherusagesofCNNs:
Approach Description Year
[244] SRCNN:AdeepCNNlearnsanend-to-endmappingfromlowtohigh-resolutionimagesfor 2014
super-resolution. Thefirstlayerextractsfeaturemapsfromoverlappingpatches,thesecond
mapsthesefeaturemapstohigher-resolutionmaps,andthethirdcombinesthepredictionsin
aneighboringareaforthefinalresult.
[247,248] DeepDream: AnimageclassificationCNNthatisreversedto(iteratively)amplifyhigh-level 2015
featuresinrandomnoiseorrealimages, oftenresultingindream-likeover-interpretations.
Thisapproachallowsausertovisuallyinspectwhatamodelhaslearnedaboutobjectsor
conceptsandcanbeusedtocreateart-likeimages.
[245] ImprovementofSRCNN[244]forsimultaneous3-channelcolorhandling. Further,different 2015
modelarchitectures(largerfiltersandmorelayers)andparametersareexplored.
Continuation...
32

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[249] Gated PixelCNN: Improved image quality over the original PixelCNN by utilizing gated 2016
convolutional layers, matching the PixelRNN. The model is suitable for class-conditional
imagegenerationandasapowerfuldecoderforanautoencoder.
[241] ProposalofthegatedconditionalPixelCNNwithtext(GRUencoder),segmentationmap,and 2016
keypoint(i.e.,annotatedlocationsofcertainhuman/birdbodypartsintheimage)conditioning
forimagegeneration.
[250] Image super-resolution and style transfer like [242], but three orders of magnitude faster 2016
withqualitativelysimilarresultsbyusingaperceptuallossobtainedfromapre-trainedVGG
network[186]insteadofaper-pixelloss.
[251] ESPCN:Imageandvideosuper-resolutionwithsub-pixelCNNlearningupscalingfiltersfrom 2016
low-resolutionfeaturemapsintohigh-resolutionoutput.
[252] DeepVoice3: Afully-convolutionalencoder-decodermodelwithposition-augmentedatten- 2017
tionmechanismfortext-to-speechsynthesis. Themodelcanproducedifferentparametersfor
variouswaveformsynthesismodels(e.g.,WaveNet[228])andincorporateaspeakerrepresen-
tationtocapturedifferentspeechstyles. Themodelachievesstate-of-the-artqualityinhuman
meanopinionscoreevaluations.
[253] PixelSNAIL:ApplicationofSNAIL[254],ageneralpurposeautoregressivemeta-learning 2017
modelusingcausalconvolutionsandself-attentiontomaximizeitscontextsize,tosequen-
tial image generation, resulting in state-of-the-art likelihood, but slow density estimation
performance.
[255] SubscalePixelNetwork(SPN):ImagesofsizeN ×N aresplitintoslicesofsize N × N 2018
S S
thatareinterleaved. Thenetworkconsistsofaconvolutionalencoderthatembedspreviously
processedslicesandaconvolutionaldecoderwithmaskedconvolutionandself-attentionthat
predictsthenextslicegiventheembedding. Themodelisespeciallysuitableforupscaling
andgeneratescoherentandexactsamples.
[256] JointtrainingofanensembleofshallowanddeepCNNstogeneratesuper-resolutionimages 2019
end-to-end. Optimization during training is alleviated by letting the shallow CNN restore
themainstructureoftheimageandthedeepCNNfillinthedetails. ThedeepCNNextracts
features,upscalesthemtothetargetfactor,andusesmulti-scalereconstructiontocapturethe
contextbetterandproducetheoutputpixels.
2.12 Transformers
Transformers(seeFigure27c)aresequence-to-sequencetransductionmodelswithanencoder-decoderstructure. They
advancepreviousrecurrentandconvolutionalencoder-decoderarchitecturesbecausetheyallowformoreparallelization
andmodelingofdependencieswitharbitrarydistanceintheinputandoutputsequenceswithaconstantnumberof
sequentialoperations. Forthat,thetransformerutilizesamulti-headedself-attentionmechanism(seeFigure27aand
Figure27b)insteadofrecurrentlayers. Originally,thetransformerwasusedforlanguagetranslationtasks,wherethe
originalsentencewasfirstencoded,andthedecoderusedattentiontotheencoderembeddingsandthealreadygenerated
outputinthetargetlanguagetocomputetheprobabilitiesofthenexttoken. [18]
Liu et al. [257] generate English Wikipedia articles by providing the target article title and summarizing multiple
non-Wikipediareferencedocuments. ThetrainingdataconsistsofWikipediaarticles,theircitations,andthetop10
websearchresultsforeacharticlesectiontitle. Theparagraphsofallreferencedocumentsarerankedbyimportance
accordingtothetargetarticletitle. Then,thefirstLtokensoftheserankedparagraphsareusedastheinputforthe
generativemodel. Thegenerativemodelisatransformerwithoutanencoderthatconcatenatestheinputsequenceand
thedesiredoutputsequenceintoasinglevectorforthedecoderinputandistrainedtopredictthenexttokenbased
onthepreviousones. Theauthorsalsomodifytheattentionmechanismbysplittingthetokensintoblocksonwhich
attentionisindependentlyappliedandperformingconvolutiononthekey-valuepairstoreducememoryrequirements
onlonginputsequences. Theresultsshowthatthemodelcansplitarticlesintoreasonablesectionsandfillinfactual
informationfrommanydifferentreferences.
Parmaretal. [258]proposetheImageTransformer conditionedonafewclassembeddings(decoderonly)orlow-
resolution pictures (encoder-decoder architecture) to generate high-resolution images. The generation process is
formulatedasasequencemodelingproblem,wheretheRGBchannelvaluesofthenextpixelarepredictedbasedon
theotherpixels’valuesinthelocalneighborhoodtoallowforlargerimagesizes. Theauthorsproposetwodifferent
attentionmechanisms,1Dand2Dlocalattention(seeFigure28). ExperimentsonCIFAR-10,ImageNet,andcelebA
33

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
(a)Thescaleddot-productattentionmapsweightstovaluesof
key-valuepairs(K,V)accordingtothecorrespondencebetween
aqueryQandthekey.
(b)Multi-headattentionusesmultipleattentionlayersandconcate- (c)Encoder-decoderarchitectureofthetransformer.Both
natestheresults.
partsconsistofN =6layers.
Figure27: Structureofthetransformeritselfandessentialparts. (Source: [18])
datasetsshowthatthetransformerarchitectureoutperformspreviousstate-of-the-artarchitectureslikeRNNs,CNNs,
andGANsintermsofprocessibleimagesizeandquality.
Local 1D Attention Local 2D Attention
Memory Block
MMeemmoorryy BBlloocckk
q q
Query Block
Query Block
Figure 28: Illustration of the 1D and 2D local attention mechanisms of the Image Transformer. The 2D attention
performsslightlybetterintermsofperceptualimagequalityevaluatedbyhumans. (Source: [258])
Huangetal. [259]useatransformertogeneratesymbolicmusicrepresentedasasequenceofdiscretetokens. Since
piecesoftenrepeatandmodifypreviousmotifsorsections,relationsbetweensuchsectionsareexplicitlymodeled.
Therefore,theauthorsadoptarelation-awareself-attention[260]thatcreatesrelativepositionembeddingsandoptimizes
thememoryconsumptiontoallowlongsequencestobeautoregressivelymodeled.TheyachievethebestNLLscoresand
mostwininahuman“musicality”comparisontestwhencomparedagainstthePerformanceRNNandLookBackRNN
[163]LSTMmodelsandabaselinetransformerwhencontinuingamusicsequencetheywereinitializedon.
Childetal. [261]introducethesparsetransformer,whichusessparsefactorizationsoftheattentionmatrixtoreduce
√
thetimeandmemoryrequirementsfromO(n2)toO(n n)forthesequencelengthnwithoutperformanceloss. This
works by splitting the attention operation into multiple faster operations that only access a subset of all previous
positionsandcombiningtheirresultstoapproximatethefullattention. Themodelcangeneratelargeunconditional
sequencesamplesinvariousdomainssuchasnaturalimages(CIFAR-10,ImageNet64)andrawaudiodataofclassical
musicandachievesstate-of-the-artresultsindensitymodelingtaskscomparedtocontemporarymodels.
Sun et al. [262] build VideoBERT, a joint visual-linguistic model in the style of BERT [263], which uses masked
languagemodelandnextsentencepredictiontaskstotrainthelanguageunderstandingofatransformer. VideoBERT
34

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
VideoBERT: A Joint Model for Video and Language Representation Learning
pairsrepresentationsofvideos,consistingofspatiotemporalfeaturesextractedwithpre-trainedvideoclassification
modelsandtheirtextdescription,obtainedthroughanautomaticspeechrecognitionsystem,andtrainsthetransformer
onfillinginmaskedtokensinbothdatatypes(representationsofframes,notrawimagedata)ordecidingwhetherthe
ChenSun,AustinMyers,CarlVondrick,KevinMurphy,andCordeliaSchmid
textmatchesthevideofeatures. Thetrainedmodelisthenusedforactionclassification,videocaptioning,futurevideo
tokenforecasting,andpredictionofvideotokensfortextdescriptions(seeFigure29),achievingcoherentresultsand
GoogleResearch
state-of-the-artcaptions.
Season the steak with Carefully place the steak Flip the steak to the Now let it rest and enjoy
input text
salt and pepper. to the pan. other side. the delicious steak.
VideoBERT
output video
output
input
video
video
futures
VideoBERT
FigFuirgeu2re9:1:TeVxitd-teoo-BvEidReTottoexkte-ntog-veindeeroatgioennearnatdiofnutaunredtfoukteunrepfroerdeiccatisotinngw.it(hAVboidveeo)BGEivRenT.sTomheeirmecaigpeestedxetpdicivteiddedfroinmtothe
traisneinntgendcaetsa,yha=veyt1h:Te,mwoesgtesnimerailtaeratosekqeunenreceproefsevnidteaotiotonketonsthxe=prxed1:iTctbioync.o(mSpouutrincge:x[∗ t26=2]a)rgmaxkp(xt = k|y)using
VideoBERT.(Below)Givenavideotoken,weshowthetopthreefuturetokensforecastedbyVideoBERTatdifferenttime
Liusceatleasl..I[n2t6h4is]cparsoe,pVosideeoaBgErRaTphprterdainctssfothramtearbothwaltorfeflpolaucreasndthceoceodagpeo-woduetprumtanyebtewboarkkedofinthaneoGveranp,ahnRdNmNay[b2e2c6o]mweiatha
tranbsrfoowrnmieerordceucpocdaekrew.Withevsieslufa-alitzteenvtiidoenoltaoykeenrssuasnidngatthteenitmioangelsayfreormsrtehfeetrrraiinngintgostehteclhoisdedstetnogcreanptrhoisdtsatienfoefattuhreensopadcee.RNN.
TheresultsarecompetitiveorbetterthanGraphRNNonavarietyofmetrics.
Abstract 1.Introduction
2.13 GenerativeAdversarialNetworks
Self-supervisedlearninghasbecomeincreasinglyimpor- Deep learning can benefit a lot from labeled data [24],
GentaenrtattioveleAvedrvaegresathriealaNbuentdsa(nGceANofs)unalraebferlaedmedwatoarkasvaciol-nsistibnugtothfiasigsehnaerrdattooracGqucirreeaattinscgasley.nCthoentsiecqduaetnatlyfrothmererahnadsom
noiasbeleanodnapdlaitsfcorrimmsinliakteorYoDuTduebtee.rmWinhienregaswhmeotshteerxaistpinrogvidedbeseanmaplleotcoafmreecfernotmintGereosrttihne“strealfinsiunpgerdvaistead. lTeharenianugt”h,ors
approaches learn low-level representations, we propose a wherewetrainamodelonvarious“proxytasks”,whichwe
describetheirsystemasa“minimaxtwo-playergame”[238],wherethegeneratortriestodeceivethediscriminator.
joint visual-linguistic model to learn high-level features hopewillresultinthediscoveryoffeaturesorrepresenta-
[265]
without any explicit supervision. In particular, inspired tionsthatcanbeusedindownstreamtasks. Awidevariety
byitsrecentsuccessinlanguagemodeling,webuilXdupon of such proxy tasks have been proposed in the image and
the BERT model toRleeaalr ndabitdairectional joint distributions videodomains. However,mostofthesemethodsfocuson
oversequencesofvisualandlinguistictokens,derivedfrom lowlevelfeatures(e.g.,textures)andshorttemporalscales
vector quantization of video data and off-the-shelf speech Disc(er.igm.,imnoattioonrpatternsthatlastaRseeaclo/nFdaokreless). Wearein-
recognitionoutputs,respectively.WeuseVideoBERTinnu- terestedindiscoveringhigh-levelsemanticfeatureswhich
G(z)
meroustaNskos,iisnecludingactionclassificationandvideocap- correspond to actions and events that unfold over longer
tioning. We(zs)how that it canGbeenapeprlaietdordirectly to open- timescales(e.g.minutes),sincesuchrepresentationswould
vocabulary classification, and confirm that large amounts beusefulforvariousvideounderstandingtasks.
oftrainingdataandcross-modalinformationarecriticalto In this paper, we exploit the key insight that human
performance.Furthermore,weoutperformthestate-of-the- languagehasevolvedwordstodescribehigh-levelobjects
artonvideocaptioning,andquantitativeresultsverifythat and events, B an a d ck th p u r s o p p r a o g vi a d t e i s on a natural source of “self”
themodellearnshigh-levelsemanticfeatures. supervision. In particular, we present a simple way to
Figure30: TheoriginalGANimplementation. (Source: [265])
modeltherelationshipbetweenthevisualdomainandthe
AsseeninFigure30,bothD andG,originallyimplementedasMLPstoprovideanetworkmodelwithnon-linear
mapping, are learning from the results of D. G learns th 17e46p4robability distribution of the real data p (x) and D
data
thedistributionoftherandomnoisep (z). ThegoaloftheoptimizationprocessinAlgorithm2isreachingtheNash
z
equilibriumbetweenDandG,sobothdistributionsbecomeindistinguishableandtheprobabilityofDclassifyinga
sampleaseitherfakeorrealapproaches50%. [265]
Inpractice, minimizing thecostof thediscriminatorand generatorjointly isdifficultand oftenleadsto instability
becauseminimizingonecostfunctionoftenmeansincreasingtheother. AGANmayfailtoconverge. Further,GANs
oftenlackdiversityduetothemodecollapseprobleminducedbytheeffortofthegeneratortodeceivethediscriminator,
notrepresentarealisticdatadistribution. Thisoftenleadstoonlycertain“easy”datatypesbeinggeneratedandrepeated.
[4]
35

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Algorithm2TrainingalgorithmforGANs. θ andθ aretheparametersoftherespectiveMLPsD andGthatare
d g
updated. Intheoriginalexperiments,k = 1isused,butahigherk isrecommendedtokeepDclosetotheoptimal
solutionandpreventGfromoverfitting. (Source: [238])
fornumberoftrainingiterationsdo
forkstepsdo
Sampleminibatchofmnoisesamples{z(1),...,z(m)}fromp (z).
z
Sampleminibatchofmexamples{x(1),...,x(m)}fromp (x).
data
Updatethediscriminatorbyascendingitsstochasticgradient:
∇ 1 (cid:80)m [logD(x(i))+log(1−D(G(z(i))))].
θdm i=1
endfor
Sampleminibatchofmnoisesamples{z(1),...,z(m)}fromp (z).
z
Updatethegeneratorbydescendingitsstochasticgradient:
∇ 1 (cid:80)m log(1−D(G(z(i)))).
θgm i=1
endfor
Thegradient-basedupdatescanuseanystandardgradient-basedlearningrule. Weusedmomentuminourexperi-
ments.
TheauthorsoftheoriginalGANframework,Goodfellowetal. [238],trainasetupoftwoMLPsonthreedatasets:
MNIST,TFDandCIFAR-10. Theyachievefirstandsecond-placeresultsontheMNISTandTFDdatasets,respectively,
whencomparedagainstaDBN,adeepGSN,andastackedCAEintermsoflog-likelihoodestimates[266].
Radford et al. [267] develop the Deep Convolutional GAN (DCGAN) architecture, which aims to adopt CNNs to
unsupervisedlearningtasksbyusingtheGANframework. DCGANsreplacethepoolingfunctionsofCNNswith
striddenconvolutionsforthediscriminatorandfractional-striddenconvolutionsforthegeneratorandremovefully
connectedlayersentirely. Further,theneuralnetworksnowutilizeReLUactivationfunctionsandbatchnormalization
forallparts. AnexampleofaDCGANarchitectureforimagemodelingisdepictedinFigure31. Frid-Adaretal. [268]
applytheDCGANtogeneratelabeledliverlesionimages.
Figure31: TheDCGANgeneratorarchitectureusedtogeneratebedroomsceneimagestrainedontheLSUNdataset.
(Source: [267])
Metzetal. [269]unrolltheparametersofGANdiscriminatorsθ0 =θ forK futuresteps
D D
df(θ ,θk)
θk+1 =θk +ηk G D (26)
D D dθk
D
andupdatethegeneratorparameters
df(θ ,θK)
θ ←θ −η G D (27)
G G dθ
G
withlearningrateηandobjectivefunctionf,accordinglytostabilizethetrainingofthegeneratorattheexpenseof
increasedcomputationalcostduringtraining. Bylettingthegenerator“seeintothefuture”,thenextdiscriminatorstep
becomeslesseffective,whichbalancesthetwomodelsbetterandimprovesconvergence.
Elgammal et al. [270] train a DCGAN [267] to produce art images. They achieve this by changing the training
objectivesofboththegeneratoranddiscriminatortoencouragelearningaboutstylesandartseparately. TheCreative
36

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Adversarial Network (CAN) generator aims to deviate as much as possible from learned styles while keeping the
learnedartaspects. Thediscriminator,ontheotherhand,decideswhetheraninputimageisartornotandclassifiesthe
artstyle. Duringtraining,thediscriminatoristrainedwithartimageswithstylelabelstorefinethedecisionsandstyle
classifications. Thegeneratorreceivestheart/notartdecisionandthestyleambiguityofthediscriminatorasaloss. An
evaluationwithhumansubjectsindicatesthatgeneratedartisindistinguishablefromrealart.
Donahueetal. [271]introduceWaveGAN,whichsynthesizesone-secondclipsofraw-waveformaudiounsupervised.
WaveGANcangeneratewords,birdchirping,andinstrumentsbycapturingperiodicpatternsinthesampledwaveforms
withconvolutions. TheapproachisbasedonDCGAN[267]buthasamodifiedone-dimensionalconvolutionkernel
withahigherstride. Further,phaseshuffleisusedtoshifttheactivationsofeachlayer’sactivationsbyarandominteger
∈ [−n,n]topreventthediscriminatorfromlearningtrivialpolicies. TheycompareWaveGANtoanotheroftheir
modelsbasedonDCGAN,SpecGAN,whichworksonspectrograms,andfindthatSpecGANhasahigherInception
Score(IS)andlabelaccuracythroughhumans,butWaveGANproducessamplesofhighersoundquality.
ShortoverviewofotherusagesofGANs:
Approach Description Year
[272] GenerativeMulti-AdversarialNetworks(GMANs): ThefirstintroductionofDCGAN[267] 2016
with multiple discriminators demonstrated on image generation tasks, resulting in higher-
qualityimagesandrobustnesstomodecollapse.
[273] Mode regularized GANs for stable training and reduced risk of mode collapse: Train an 2016
encoderE(x) : X → Z togetherwithgeneratorG(z) : Z → X andaddasimilarityloss
distance(x,G(E(x))) for stable training gradients. Further, a mode regularizer objective
D (G(E(x)))onthetrainingdataxisemployedtoforcethegeneratortocoverthewhole
1
dataspace. Aftertrainingwithx,aseconddiscriminatorD discriminatesG(z)andG(E(x))
2
tobringbothdistributionstothesamemanifoldefficiently.
[274] 3D-GAN:ACNNgeneratorcreatesobjectsin3Dvoxelspacefromarandomvector, and 2016
the discriminator, which is a reversed generator, judges whether the objects are real. The
modellearnsmappingsbetweenlow-dimensionallatentvectorsand3Dobjects,whichcan
beused,apartfromgenerativepurposes,forobjectrecognitionanddescription. Theyfurther
introduce3D-VAE-GAN,whichconsistsofaconvolutionalimageencoderandallowsone-shot
image-conditional3Dmodelgeneration.
[275] TextGAN:TextgenerationwithaLSTMgeneratorandaCNNdiscriminator/encoder. Instead 2016
ofthestandardGANobjective,thegeneratoristrainedtominimizethecovariancematrices
of the real and synthetic sentence feature vectors obtained from the CNN encoder. The
discriminator is trained with the standard adversarial loss, latent code reconstruction loss,
andgeneratorloss. Thegeneratorispre-trainedinanautoencoderLSTMsetting,whilethe
discriminatorispre-trainedtoclassifysentenceswithswappedwordsfromtruesentences. In
[276],theygointofurtherdetailandexploreaMMD-basedfeaturematchinglossinsteadof
covariance.
[277] CoupledGAN(CoGAN):Multiplegenerator-discriminatorpairswithsharedweightsinthe 2016
higherabstractionlayersallowlearningofimagerelationswithouttuplesofcorresponding
images. Themodellearnstogeneratecorrespondingimagesfordifferentdomainsfromthe
samenoisevectorz,makingthemodelsuitableforunsuperviseddomainadaptationandimage
transformation(e.g.,learningtherelationshipbetweendepthandcolorinRGBDimages).
[278] Energy-basedGAN(EBGAN):Definingthediscriminatorasanenergyfunction[279]that 2016
assignslowenergiestodatapointsnearthedatamanifoldandviceversa. Thediscriminatoris
implementedasanautoencoder,andthereconstructionerroristheenergyfunction. During
training,theEBGANismorestablethanregularGANsandgenerateshigh-resolutionimages.
[280] C-RNN-GAN:AmodelwithdeepLSTMgeneratoranddiscriminatortocreatecontinuous 2016
sequentialdatawithoneormorevaluesateachstep.Theadversariallytrainedmodelgenerates
polyphonicmusicwithasenseoftimingandvariationbutisdistinguishablefromrealmusic.
[281] Introspective adversarial network (IAN): A hybrid of a VAE for representation learning 2016
andreconstructionandaGANtoimproveVAEperformance. ThenetworkcombinesGAN
discriminator and VAE encoder and GAN generator and VAE decoder. Used for realistic
photoediting/interpolation.
[101] InfoGAN: An unsupervised GAN that learns disentangled representations with a mutual 2016
informationobjectiveonlatentvariablesubsets. Themodelcanseparatewritingstylesfrom
digitsonMNISTandhairstyles,emotions,andeyeglassesfromfacesontheCelebAdataset.
Continuation...
37

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[282] f-GAN:Trainingofgenerativeneuralsamplers(probabilisticfeedforwardneuralnetworks), 2016
whichefficientlyconvertarandominputvectortoasample,usinganauxiliarydiscriminative
neuralnetworkorotherf-divergences(e.g.,Kullback-Leibler,Jensen-Shannon). Results,also
withDCGAN[267],showthatthediscriminatorapproachdoesnotnecessarilyperformbetter.
[283] Generative Recurrent Adversarial Network (GRAN): A recurrent attention-based genera- 2016
tor/decoderappliessequentialchangestoacanvasbasedontheprevioushiddenstateand
randomnoiseateachtimestep,whileanattention-basedencoder/discriminatorprovidesa
feature-based loss. An evaluation method involving a “battle” between separately trained
generatorsanddiscriminatorsisproposed,whereGRANoutperformsDRAW[97]andthe
denoisingVAE[105].
[284] OfferingasuiteofmethodologiesforimprovedtrainingofGANs. Thesetechniques,suchas 2016
featurematching,minibatchdiscrimination,andhistoricalaveraging,addressthechallenges
ofGANtraining,particularlyinachievingconvergence. Theauthorsfurthercontributedto
stabilizingGANtrainingandproposedanovelevaluationmetricnowwidelyusedforGAN
performanceevaluation,theIS,toassesssamplequality.
[285] WassersteinGAN(WGAN):Replacementofthediscriminatorwithacriticthatapproximates 2017
theEarth-Moverdistance(Wasserstein-1)betweentherealdatadistributionandthegenerator
data distribution. Since the Wasserstein distance is continuous and differentiable under
mostcircumstances,thegeneratorcanbetrainedwithgradientdescent,solvingthetraining
instabilityandmodecollapseproblemsofGANsandprovidingmeaningfullearningcurves,
asdemonstratedonimagegenerationtasks. In[286],thetrainingisimprovedwithagradient
penaltywithrespecttothecriticinput.
[287] BoundaryEquilibriumGAN(BEGAN):SimilartoEBGAN[278],anautoencoderisusedasa 2017
discriminator,butinsteadofusingthereconstructionlossofsamplesdirectly,theWasserstein
distancebetweenerrordistributionsofrealandgeneratedsamplesiscomputed. Further,the
equilibriumconditionbetweentheexpectederrorsofgeneratedandrealsamplesisrelaxed
withahyperparameterγ ∈[0,1]thatinfluencesthediversityofthegeneratedimages.BEGAN
outperformspreviousmodelsinimagequalityathigherresolutions.
[288] Least Squares GAN (LSGAN): Using the least squares loss for the discriminator instead 2017
ofthesigmoidcross-entropyloss,resultinginhigherqualityimagesgeneratedandamore
stabletrainingprocedurecomparedtoregularGANs. Thenewlosspenalizescorrectdecisions
farbeyondthedecisionboundary(i.e.,toomuchcertaintybythediscriminator)toprevent
vanishinggradientsandmovethegeneratortowardsthedecisionboundary,whichconverges
totherealdatamanifold.
[289] RankGAN: Instead of binary judgments of individual data samples by the discriminator, 2017
generatoroutputsaremixedwithrealdataandrankedbythediscriminatoraccordingtoa
reference. Themoredetailedfeedbackallowsthegeneratortolearnbetterwhatmakesdata
realistic. Themodelgeneratesnaturallanguagesentencesbutcouldbeextendedforimage
generationandcaptioning.
[290] Chekhov GAN: Treating GAN training as a zero-sum game that can be solved by finding 2017
a mixed strategy. Using ideas from online learning, where a player aims to minimize a
sequentially-revealedcumulativelossfunction,ano-regretstrategyforbothgeneratorand
discriminatorthatincorporatesthehistoryofthemodel’sactionsisemployed. Themodel
improvesstabilityandmodecollapseproblemsandisguaranteedtoconvergetoequilibrium
for specific GAN architectures. The model is evaluated on image generation and density
estimationtasks.
[291] AdversariallyRegularizedAutoencoder(ARAE):AframeworkthattrainsaWassersteinGAN 2017
[285]toproducelatentcodesofasimultaneouslytrainedautoencodertocreateaGANfor
discretedata(e.g.,images,text).
[292] MeanandcovariancefeaturematchingGAN(McGAN):TrainingGANsbymatchingstatistics 2017
(e.g.,embeddedmeanorcovarianceoffeatures)ofrealandfakedatainsteadofclassifying
individualsamples. TheapproachisadaptedtoDCGAN[267]andusedtogenerateimages.
[293] FisherGAN:InsteadofpenalizingthegradientsoftheWassersteinGANdiscriminator[286], 2017
aconstraintisimposedonitssecond-ordermoments, inspiredbytheFisherDiscriminant
Analysismethod. TheapproachisappliedtoaDCGAN[267]architecture,outperforming
othermodelsinunconditionalimagegeneration.
Continuation...
38

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[294] α-GAN: Combining an autoencoder with a GAN, where the GAN generator is trained to 2017
reconstructlatentrepresentationsofanencoderandthelatentspaceisencouragedtoconform
to a Gaussian distribution. Further, a discriminator is used to evaluate the realism of the
generatedorreconstructedsamples. ThecombinationofautoencodersandGANs(DCGAN
[267]inparticular)solvesblurrinessandmodecollapseissuesforimagegeneration.
[295] SeqGAN: Application of the GAN architecture to the generation of sequences of discrete 2017
tokens. SincethedefaultGANgeneratorgeneratescontinuousvaluesandreceivesinstant
feedbackfromthediscriminator,andthediscriminatorcanonlyevaluatecompletesequences,
the authors model the generator as a LSTM and RL agent with a stochastic policy whose
intermediateactionsarerewardedafterthecompletesequencehasbeenjudgedbytheCNN
discriminator. Leeetal.[296]appliedSeqGANtopolyphonicmusicgenerationusingefficient
representationsofpolyphonicMIDIfiles.
[297] Temporal GAN (TGAN): The video generator consists of a temporal generator CNN that 2017
generatesT latentvariableszt frominitialnoisez andanimagegeneratorthatgenerates
1 0
T video frames from z and the respective zt. The discriminator receives all frames and
0 1
evaluates,withmultipleconvolutionallayers,whetherthevideoisrealorgenerated. Image
generatoranddiscriminatorareverysimilartoDCGAN[267],andtrainingalsoincorporates
theWGAN[285]objective.
[298] VEEGAN:UsingareconstructornetworkF(x)tomapthetruedatadistributionp(x)back 2017
totheGaussiandistributionp(z)ofthegeneratorG(z)’slatentcode. TheKullback-Leibler
divergenceservesasanexpressivelossfunctionbetweendistributionsF(G(p(z)))andp(z)
becausetheyshouldbeidentical. Thisautoencoder-styledstructureaimstosolvethemode
collapseproblemofGANsbycheckingifthiswholedistributioniscovered. Themodelis
demonstratedondensityestimationandimagegenerationtasks,whereitislesspronetomode
collapseissuesthanotherGANapproaches.
[299] Boundary-seekingGAN(BGAN):Usingtheestimateddifferencemeasureofadiscriminator 2017
asadifferentiablepolicygradientforthegeneratortoallowGANstogeneratediscretedata.
Theapproachisalsosuitableforcontinuousdataandisdemonstratedinnaturallanguageand
imagegeneration.
[300] medGAN:GenerationofsyntheticElectronicHealthRecords(EHRs)forprivacy-preserving 2017
datasharingformedicalresearch. Anautoencoderprovidesdiscreterealdataxordiscrete
datafromnoiseztoadiscriminatorDintheformDec(Enc(x))orDec(G(z))respectively,
wheregeneratorGandDarefeedforwardneuralnetworks.
[301] MidiNet: AgeneratorCNNcreatessymbolicMIDImelodiesfromrandomnoiseandprior 2017
knowledge(e.g.,chordprogression,previousbars,primingmelody)fromaconditionerCNN
withtransposedconvolutions[302]andadiscriminatorCNNpredictswhetheraninputscore
isrealorfake.
[303] ProgressiveGAN:AcceleratingandstabilizingGANtrainingbyprogressivelyaddingconvolu- 2017
tionallayerstothegeneratoranddiscriminator,increasingtheresolutionforimagegeneration
iteratively.
[304] DRAGAN:TreatingGANtrainingasazero-sumgamesolvedusingaregretminimization 2017
technique. Modecollapseisinterpretedasaproblemcausedbylocalequilibriainthetraining
“game”. ThemodelisstableandoutperformsWassersteinGAN[285,286]significantly.
[305] GangofGANs(GoGAN):ImprovementoverWassersteinGAN[285]byusingamargin-based 2017
discriminatorlossthatenforcesacertaindistanceϵbetweendiscriminatorscoresoffakeand
realsamplesandprogressivelytrainingmultipleGANsthatareevaluatedagainsteachother
withamaximummarginrankinglossthatensuresthatlaterGANsperformsignificantlybetter
thanearlierones. Themodelisusedforimagecompletion.
[306] LeakGAN:TheCNNdiscriminatorleaksitshigh-levelabstractedfeaturesofthecurrently 2017
evaluatedsentencetotheLSTMgeneratorthattakestheadditionalinputasguidancefornext
wordgenerationforatext.
[307] CombiningaclassicGANarchitecturewithaninferencenetwork. Thisallowsthediscrimina- 2017
tortodistinguishbetweenjointlatent/data-spacesamplesfromthegenerativenetworkand
jointsamplesfromtheinferencenetwork(whichreceivesadatasampleasinputandoutputs
syntheticdata). Thesetupenhancestheperformanceofstate-of-the-arttasks.
Continuation...
39

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[308] LR-GAN:Generatingimagesbycreatingbackgroundsandforegroundsseparatelyandthen 2017
stitchingthemtogether. Itemploysarecursiveapproachwhereeachlayer(backgroundor
foreground)isgeneratedstep-by-step,eachwithitsownshapeandpose. Thismethodallows
foracontextuallyrelevantcompositionofimages,leadingtomorenaturalandrealisticimage
generation.
[309] Enhancing GANs using denoising feature matching. This technique guides the generator 2017
towards more probable configurations of abstract discriminator features, generating more
object-likesamples. Theapproachusesadenoisingauto-encodertoestimateandtrackthe
distributionofthesefeaturesderivedfromrealdata. ThisiscombinedwiththeoriginalGAN
loss,andtheaugmentedtrainingprocedureisshowntoimproveitsstability.
[286] ApplyingWassersteinGANfordatageneration,usingagradientpenaltytoenforceaLipschitz 2017
constraintonthediscriminator. Thisaddressesthetraininginstabilityassociatedwithweight
clipping in Wasserstein GAN. The method enables stable training across various GAN
architectures,significantlyreducingtheneedforhyperparametertuning.
[310] IncontrasttoGANtrainingtraining,theauthorsupdatethediscriminatorandgeneratorat 2017
differentrates. Thismethodfacilitatesmorestableconvergenceandenablesthenetworks
toreachalocalNashequilibriumeffectively. Additionally,theintroductionoftheFréchet
InceptionDistance(FID)providesamorereliableandsensitivemetricforGANperformance
evaluation when compared to the IS. The effectiveness was validated using several GAN
architectures,improvingstabilityandimagequalityinthegeneratedsamples.
[311] MotionandcontentdecomposedGAN(MoCoGAN):Videogenerationusingafixedcontent 2018
vectorandasequenceofmotionvectorsthatareconvertedtoastateusingaRNN. Animage
generator CNN then creates a frame from both vectors, and CNN-based video and image
discriminatorsprovidefeedback.
[312] MuseGAN:AWGAN[285]utilizingdeepCNNsthatgeneratemulti-trackmusicsequences 2018
withpiano-rollrepresentations. Itcombinesajammingmodelthatimprovisesonetrackwith
a composer model that creates multiple accompanying tracks at once, so multiple hybrid
generatorswithinter-trackrandomvectorzandintra-trackrandomvectorsz arepairedwith
i
onediscriminator.
[313] CapsuleGAN:ReplacestheCNNdiscriminatorinaDCGAN[267]withacapsulenetwork 2018
(CapsNet)[314]classifiertoimproveaccuracyandgeneratorperformance.
[315] MolGAN:TrainingaMLPgeneratortoproduceadjacencyandnodeannotationmatricesfor 2018
smallmoleculeswithagraph-convolutionaldiscriminatorandrewardnetwork. Thereward
network,likeinRL,learnstoscorenon-differentiablemetrics(e.g.,solubilityinwater)with
thehelpofexternalsoftwareandtoguidethemoleculegenerationtowardsaspecifictarget.
[316] NetGAN:Generatinggraphsasasetofrandomwalks(nodesequences)withaLSTMgenerator 2018
outputtingvertexaftervertexofthesequenceandadiscriminatorLSTMthatjudgeswhether
the sequence belongs to the real graph or is fake. Training samples (random walks) are
obtainedfromarealgraph,andsyntheticgraphsareobtainedbymergingtherandomwalks.
[317] table-GAN:ApplicationoftheDCGAN[267]architecturetothegenerationofprivateand 2018
usefultabulardata. Originaltableentriesarefedassquarezero-paddedmatricestotheGAN
fortraining,withaneuralnetworkclassifierC besidesthegeneratoranddiscriminatorthat
enforcesdataconsistencylearnedfromtheoriginaltable.
[318] corrGAN:Generationofcorrelateddiscretedata(e.g.,tableentries,binaryimages)withan 2018
autoencoderthatlearnsmappingsbetweendiscreteinput/outputandcontinuouslatentspace
whileconsideringthecorrelationsbetweensubsetsofthediscretevariables. Thedecoderthen
servesastheoutputlayerofaGANgeneratormodelingthecontinuouslatentspace.
[319] Tabular GAN (TGAN): A LSTM generates discrete and continuous values encoded with 2018
probabilitydistributionscolumnbycolumnforeachentry,andaMLPdiscriminatorscores
thelikelihoodanddiversityofthedata.
[320] ConsistencyTerm(CT)GAN:ImprovedtrainingofimprovedWassersteinGANs[285,286]by 2018
additionallytrainingthediscriminatorononceandtwiceperturbedrealdataandevaluatingthe
responses. Combinedwithothersmalloptimizations,thisapproachachievesstate-of-the-art
generativeresultsandisbettersuitableforsemi-supervisedlearningthanotherGANs.
Continuation...
40

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[321] AmbientGAN: Training a GAN on lossy measurements by passing the generator output 2018
throughasimulatedrandommeasurementfunctionthatcorruptsit. Thediscriminatorthen
triestodistinguishthelossyrealandfakemeasurements. Themodelcansuccessfullyinpaint
lossyimages.
[322] Proteinstructuregenerationandcompletionbyencodingthemaspair-wisedistancesbetween 2018
α-carbons in a matrix using a DCGAN [267] and recovering the 3D structure using the
“alternatingdirectionalmethodofmultipliers”(ADMM)algorithm.
[323] Humantrajectorygenerationasasequenceofstayswithalocation(x,y),astarttimet,and 2018
adurationd. AGANmadeofCNNscreatesandevaluates“maps”withtheaforementioned
timesascoordinatevalues.
[324] MGAN: Tackling the mode collapse in GANs by using multiple generators. This method 2018
employsamixtureofgeneratorswithasharedclassifieranddiscriminator,aimingtoproduce
diverseoutputsthatcoverdifferentdatamodes. Theauthorsdemonstratethattheirapproach
effectivelyminimizestheJensen-ShannonDivergencebetweenthemixedgeneratordistribu-
tionsandtherealdatadistribution. Empiricalresultsshowedthemodel’sabilitytogenerate
diverseandrecognizableimages,indicatingasignificantimprovementoversingle-generator
GAN.
[325] RelGAN:Textgenerationwithaconfigurabletrade-offbetweensamplequalityanddiversity. 2018
Therecurrentgeneratorincorporatesrelationalmemory[224](multiplememoryslotswith
self-attention[18])tomodellong-rangedependencies, andtheCNNdiscriminatorcreates
multiplerepresentationsforeachsentencetoevaluatethesentencefromdifferentaspectsand
providebetterfeedback.
[326] Dist-GAN:AGANenhancedwithdistanceconstraints. ItaddressestwokeyissuesinGAN 2018
training: gradientvanishingandmodecollapse. Thenovelapproachincludesintegratingan
autoencoderwiththegeneratorandimplementingtwodistanceconstraints,oneinthelatent
space and another based on discriminator scores. This stabilizes the GAN training while
retainingcompetitivescoresinclassificationtasks.
[327] Introducingspectralnormalization,atechniqueforstabilizingGANtraining. Itnormalizes 2018
thespectralnormoftheweightmatricesinthediscriminator,usingaLipschitzconstantas
theonlyhyper-parametertobetuned. Thismethodissimple,computationallyefficient,and
stabilizesGANperformance,particularlyinimagegenerationtasksondatasets.
[328] BayesianmodelingisemployedtotacklemodecollapseinGANs,awell-documentedand 2018
activelyresearchedproblem. Theauthorsproposelearningthedistributionsofgenerators,asit
mirrorsacommonapproachoftrainingaGANwithmultiplegeneratorstoalleviatethemode
collapse.
[329] Using the Sinkhorn divergence to train generative models based on regularized optimal 2018
transportwithanentropypenalty. Thismethodaddressesthecomputationalandstatistical
challengesofusingoptimaltransportmetricsintraininggenerativemodels. TheSinkhorn
divergenceinterpolatesbetweenWassersteinandMMDlosses,leveragingthegeometrical
propertiesoftheoptimumtransportandthefavorablehigh-dimensionalsamplecomplexityof
MMD.
[330] StyleGAN:Astyle-transferrelatedprogressiveGAN[303]capableofunsupervisedlearning 2019
of disentangled high-level attributes of images in latent space and generation of realistic
imagesfromthatlatentspaceandrandomnoise. Themodelcanalsointerpolate(stylemixing)
inthelatentspace.
[331] PATE-GAN:DifferentiallyprivatedatagenerationwiththeoriginalGANutilizingtheprivate 2019
aggregationofteacherensembles(PATE)[332]frameworkwhichallowstoboundtheinfluence
ofindividualsamplesonthegenerator. Asetofteacher discriminatorsistrainedonequal
amountsofgeneratoroutputanddisjointtrainingdata. Astudentdiscriminatoristrainedon
theoutputlabelsoftheteachers,andthegeneratoristrainedonthestudent’soutput.
[333] ImprovedtextgenerationwithGANsbysegmentingsentencesintosub-sequencesandpro- 2019
viding simultaneous discriminator feedback for all sub-sequences and the entire sentence
instead of the sentence alone. Applying this approach to previous state-of-the-art GANs
[295,306,325]significantlyimprovestheirresults.
Continuation...
41

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[334] SemGAN:Generationofpixel-levelsemanticimagesfromlatentvectorswithpriordistribution 2019
to speed up convergence. Class probabilities for each pixel are forwarded as a softmax
distribution to the discriminator, allowing for detailed feedback. The SemGAN produces
significantlycleanerresultsthanadefaultGANworkingwithRGBsemanticmappings. Using
the image-to-image GAN from [335], the creation of natural images from these artificial
semanticimagesisdemonstrated.
[336] MedicalWassersteinGAN(medWGAN)&MedicalBoundary-seekingGAN(medBGAN): 2019
ModifiedversionsofmedGAN[300]withbetterperformance. medBGANoutperformsall
otherapproachesonsyntheticEHRgeneration.
[337] UsingadefaultGANtogenerateimagesofskincancer,adomainforwhichonlyafewlabeled 2019
samplesareavailable.Thesyntheticdataisusedtoboosttheperformanceofacancerdetection
CNN.
[338] AutoGAN:Anautomatedapproachofsolvingneuralarchitecturesearchspecificallytailored 2019
toGANarchitectures. Todoso,anadditionalRNNcontrollerisincorporatedforthesearch
process,whiletheISisusedasthesuccessrewardofthereinforcement.
[339] DoppelGANger: Agenerativemodelforcreatingsynthetictimeseriesdatatacklingseveral 2019
issuesaboutGANsanddataprivacy. Thismodeleffectivelycapturesandgeneratescomplex
correlationsbetweentimeseriesanditsattributeswhileaddressingchallengessuchasmode
collapseandvariabledatalengths.
[340] TimeGAN: Generating realistic time-series data by combining supervised and adversarial 2019
training,addressingthechallengeofpreservingtemporaldynamicsingeneratedsequences. It
featuresanembeddingnetworkfordimensionalreduction,enhancingthegenerativemodel’s
learningoftemporalrelationships.
[341] StyleGAN2: ImprovementofStyleGAN[330]bysimplifyingandrestructuringthegenerator 2020
architecture. Theyfurtheremploylazyregularizationandremovetheprogressivegrowing
infavorofskipconnectionsbetweenup-anddownsamplinglayers. Theyalsodevelopeda
methodtoprojectimagesbacktolatentspacewherestylecouldbechanged/interpolated.
[342] HealthGAN:AfeedforwardneuralnetworkbasedGANthatcombinesideasfrommedGAN 2020
[300]withtheWassersteinGANgradientpenalty[286]anddatatransformationstoenable
the use of continuous and categorical data. The model is purposefully small to prevent
memorizationandusedtogenerateprivateEHRrecords.
[343] UsingaprogressivelygrowingGAN(similarto[303])withWassersteingradientpenaltyloss 2020
[286]togeneratemagneticresonanceimagingofbrainsthatcanbeusedforAttentionDeficit
HyperactivityDisorderprediction.
[344] UsingDCGAN[267]togeneratepositronemissiontomographybrainimagesforthreestages 2020
ofAlzheimer’sdiseasetobuildanautomateddiagnosismodel.
[345] SynSigGAN:Generationoffixed-lengthlabeledbiomedicalsignals(electrocardiogramand 2020
othertimeseriesdata)usingabidirectionalgridLSTMandaCNNdiscriminatorwithasmall
amountoftrainingdata. Thedatacanbeusedforautomaticalmedicaldiagnosisortraining
medicalstudentsandachievesstate-of-the-artperformancewhenusedastrainingdatafora
classifier.
[346] By analyzing the loss of the generator and the discriminator during the training process, 2020
overarchingcalculationssuchasISorFIDcanbeeliminated.Thisreducesthecomputingtime
greatlyandoptimizesthenetworkatthesametime,especiallycomparedtoeitheramanual
GANconfigurationorsimilarautomatedapproachesbasedontheISoderFID.
[347] COT-GAN:Agenerativemodelforsequentialdataemployingcausaloptimaltransportfor 2020
training implicit generative models, integrating classic optimal transport methods with a
temporal causality constraint. The COT-GAN framework is adept at generating low- and
high-dimensionaltimeseriesdata.
[348] Using differentiable augmentations applied to real and fake samples during training, this 2020
approacheffectivelypreventsoverfittinginGANandreducesthetrainingsize. Themethod
showsnotableimprovementsacrossvariousGANarchitecturesandachievesstate-of-the-art
resultswhilenotablyonlyusing20%ofthetrainingdata.
[349] UsingDCGAN[267]toboosttheamountoftrainingdatafortrafficsignrecognition,resulting 2021
inincreasedaccuracyandreduceddetectiontime.
Continuation...
42

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[350] Combining the boundary-seeking GAN [299] with noise addition directly on the data to 2021
generatedifferentiallyprivatesmarthealthcaredatasetsofpopulationsformedicalresearch.
TrainingdataisobtainedfromFitbitsmartwatches.
[351] IntroducingamethodforgeneratingsyntheticElectrocardiograms(ECGs)usingGANsto 2021
addressprivacyconcernsinmedicaldatasharing. TheauthorspresentedtwoGANmodels,
WaveGAN and Pulse2Pulse, trained on real normal ECGs to produce synthetic, plausible
ECGs. Thepresentedapproachallowsforgeneratinganarbitraryamountofnormallyvery
sensitivepatientdataandopen-sourcestheover100,000normalECGs.
[352] TTS-GAN:Generatingsynthetictime-seriesdatausingtransformerarchitecture. Itemploys 2022
transformerencodersinbothgeneratoranddiscriminatornetworks,overcominglimitations
of RNN-based GAN in handling long sequences. It showcases improved performance in
generatingrealisticsequencesacrossmultipledatasets.
2.13.1 ConditionalGANs
NormalGANshavenocontroloverthetypeofdatathegeneratoroutputs. ConditionalGANssolvethisproblemby
conditioninggeneratoranddiscriminatoronadditionalinformationy,whichcouldbeclasslabels,forexample,thatare
providedattheinputlayer(seeFigure32). TheobjectivefunctionoftheGANismodifiedasfollows[353]:
minmaxV(D,G)=E [logD(x|y)]+E [log(1−D(G(z|y)))]. (28)
G D
x∼pdata(x) z∼pz(z)
Figure32: AconditionalGANconditionedonadditionalinputy. (Source: [353])
Mathieuetal. [354]adopttheGANarchitecturetopredictthenextvideosequenceframesandintroducealossfunction
thatimprovesthesharpnessoftheimagepredictions. Thegeneratoranddiscriminatorusemulti-scalenetworks,which
areCNNsthatup-ordown-scaletheresolutionofapredictionmultipletimes,respectively,untilthetargetimagesize
orasinglescalaroutputisreached. Themodelistrainedbyprovidingasequenceofvideoframestobothmodelsand
therealorgeneratedadditionalframestothediscriminator. Themodelparametersareupdatedusingstochasticgradient
descent. Theyachievestate-of-the-artsharpnessandsimilarityonacollectionofsportsclipsfromtheSports1mand
UCF-101datasets.
Zhuetal. [355]proposeusingtheDCGAN[267]architecturetolearntheapproximatenaturalimagemanifoldby
trainingthegeneratortoproducerealisticimagesgivena100-dimensionalrandomvectorz. Then,realimagesare
projectedtosuchalatentrepresentationz ,andmanipulatingoperations(coloring,sketching,orwarpingexecutedwith
0
brushtools)areappliedtothatvector,resultinginz . ThechangesintheartificiallygeneratedimagesG(z )arethen
i i
sequentiallytransferredtotheoriginalphotousingopticalflowmethodstomaintainimagequality. Besidesinteractive
imagemanipulation,theiGAN modelcanalsogenerateobjectsfromdrawnsketches.
43

| ComprehensiveExplorationofSyntheticDataGeneration: |     |     |     |     | ASurvey |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Reedetal. [356]generateimagesfromtextualdescriptions(sentences)usingaDCGAN[267]architecture. First,atext
embeddingencodermodel(hybridcharacter-levelconvolutionalrecurrentneuralnetwork)ispre-trainedbycomparing
itsembeddingstotheonesencodedbyacorrespondingimageencoder(deepCNN). TheGANconsistsofadeep
convolutionalgeneratorthattakesasinputthetextembeddingandrandomnoiseandadeepconvolutionaldiscriminator
thatdecideswhethertheimageisrealorfakebasedonthetextembeddingandaprovidedimage. Theyalsotesta
modifieddiscriminatorwithadditionalrealtrainingsampleswithmismatchedtexttoconditionthemodelonmatching
textsinadditiontoimagerealism. Afurtheradditiontothegeneratortrainingobjectiveistheinterpolationoftext
representationstoensurethatgapsinthetrainingdataalsocorrespondtothedatamanifold:
E
|     |     |             | [log(1−D(G(z,βt |     |     | +(1−β)t |     | )))] |     |     | (29) |
| --- | --- | ----------- | --------------- | --- | --- | ------- | --- | ---- | --- | --- | ---- |
|     |     | t1,t2∼pdata |                 |     |     | 1       |     | 2    |     |     |      |
with noise sample z, text embeddings t and t and β = 0.5, which works well as long as the discriminator can
|     |     |     | 1 2 |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recognizethematchingimageandtextpairs. Further,theauthordevelopedastyleencoder,which,incombinationwith
thetrainedgenerator,allowsthemtocombinethestyleofoneimageandadescriptiontogenerateasame-styleimage
withpropertiesmatchingthetext(e.g.,animageofaneaglewiththedescriptionofaredbirdresultsinaredeagle).
In[357],Reedetal. introducetheGenerativeAdversarialWhat-WhereNetwork(GAWWN)asanextensionof[356],
thatallowsspecificationoflocations(bounding-boxes)ofobjectsandtheirparts(keypoints)fortext-to-imagesynthesis.
Theypresenttwomodels,thebounding-box-conditionalandthekeypoint-conditionaltext-to-imagemodel,andapply
aGANarchitecturetogeneratemissingkeypointsgivensomeuser-definedkeypointsandthetextdescriptionortext
alone,whichtheydemonstratealsoworks.
Isolaetal.[335]performimage-to-imagetranslationusingaconditionalDCGAN[267]withageneratorG:{x,z}→y
andadiscriminatorD :{x,y}→[real,fake],wherexisthe“concept”ofanimage(e.g.,anedgedrawingorblueprint),
yistherealorgeneratedimageandzisrandomnoise,whichislaterreplacedbydropoutonseverallayersbecauseG
tendstoignorez. ThegeneratorisadeepCNNwhichfirstdown-andthenup-samplesxtoobtainessentialfeatures
andcreateafittingimageinthetarget“style”. ThediscriminatorPatchGAN isaconvolutionalmodelthatclassifiesif
eachN ×N patchofanimageisrealorfakeandaveragesalloutputs. Thelossfunctioncombinesthediscriminator
outputandtheL1loss(meanabsoluteerror)ofthegeneratedimageandthegroundtruth. Themodelisthentrained
usingalternatinggradientdescentstepsonDandG.
Choietal. [358]introduceStarGAN basedon[359]formulti-domainimage-to-imagetranslationusingonegenerator
andmultiplediscriminators,oneforeverypairofimagedomains(seeFigure33a). ThisallowsStarGANtobetrained
onmultipledatasetswithdifferentlabelssimultaneouslyandcombinetheinformationlearnedintoonegenerative
model.
|     |     | (a)Training the discriminator |     |     | (b) Original-to-target domain |     |     | (c)Target-to-original domain | (d)Fooling the discriminator |     |     |
| --- | --- | ----------------------------- | --- | --- | ----------------------------- | --- | --- | ---------------------------- | ---------------------------- | --- | --- |
Depth-wise concatenation
1
O ri gi n a l
|     |     |     | Real image | Fake image |     | Fake image |     | Fake image |     | Fake image |     |
| --- | --- | --- | ---------- | ---------- | --- | ---------- | --- | ---------- | --- | ---------- | --- |
do m a i n
|                          |     |             | (1) | (2)                   |                          |     |             |              |       |             |                       |
| ------------------------ | --- | ----------- | --- | --------------------- | ------------------------ | --- | ----------- | ------------ | ----- | ----------- | --------------------- |
| 5                        | 2   |             |     |                       |                          |     |             |              |       |             |                       |
|                          |     |             |     | D                     |                          |     | G           |              | G     |             | D                     |
|                          |     | (1), (2)    |     | (1)                   |                          |     |             |              |       |             |                       |
| 4                        | 3   |             |     |                       |                          |     |             | Reco ns t ru | cted  |             | D o m a i n           |
|                          |     | Real / Fake |     | D o m a i n           | Target domain            |     | Input image |              |       | Real / Fake |                       |
|                          |     |             |     | cla ss if ic a t io n |                          |     |             | im a g e     |       |             | cla ss if ic a t io n |
| (a) Overall architecture | of  |             |     |                       | Depth-wise concatenation |     |             |              |       |             |                       |
StarGANwithonegenerator (b)Right:Discriminatortraining.Left:Generatortrainingwithreconstructionloss(c)
| andmultiplediscriminators. |     | andadversariallossbythediscriminator(d). |                                 |     |     |     |     |        |     |     |     |
| -------------------------- | --- | ---------------------------------------- | ------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- |
|                            |     | Figure33:                                | IllustrationsofStarGAN.(Source: |     |     |     |     | [358]) |     |     |     |
[360]proposeCausalGAN
Kocaogluetal. (Figure34a),whosegeneratorisstructuredaccordingtoagivencausal
graph,similartoaBN(seeFigure34b). Givenbinarylabelsandsomerealobservationsforthediscriminator,themodel
canbeconditionedtogeneratedata,forexample,faceimages,accordingtothelabels(e.g.,sex,haircolor). First,the
causalcontroller,implementedasaWassersteinGAN[285],generatesthelabels. Then,thegeneratorproducesdata
accordingtothelabelsandnoise. Finally,thegeneratorcompeteswiththreeadversariestoproducerealisticsamples
(discriminator)withcorrectlabels(labeler)whileavoidingeasy-to-labelunrealisticimagedistributions(anti-labeler).
44

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Anti- Label
Labeler Estimate
Causal
Controller
LG
X
N Generator G(Z,LG) Discriminator ℙ(Real)
N
X Feed Forward NN
Z
Z
Dataset X Labeler Es L t a im be a l t e N Z Feed Forward NN
Y
N
LR Y Feed Forward NN
(a)OverallarchitectureofCausalGAN. (b)TheBN-likegeneratorofCausalGAN.
Figure34: IllustrationsofCausalGAN.(Source: [360])
Zhangetal. [361]developtheself-attentionGAN(SAGAN)tocombinethecomputationalandstatisticalefficiencyof
aconvolutionalGANforclass-conditionalimagegenerationwiththelong-rangedependencymodelingcapabilityof
self-attentionmechanisms(seeSection2.12). SAGANsignificantlyoutperformspreviousstate-of-the-artmodels[362]
byincreasingtheISfrom36.8to52.52anddecreasingtheFIDfrom27.62to18.65.
Krishnaetal. [363]proposeaconditionalGANtomergethestyleofoneComputedTomography(CT)imagewith
thecontentofanothertosolvetheproblemofscarcityandprivacyissuesinclinicaltrainingdata. Theyintroducea
convolutionalencoder-decodergeneratortrainedtomapthestyleofaCTimagetothesegmentationmapofother
imagesperorganinfluencedbyrandomnoise. Thetrainingrequiresonlyasmalldatasetandcombinesstyleand
contentlosstoguidethegeneratorandtheconvolutionaldiscriminator.
Alonsoetal. [364]extendaGANtogenerateimagesofhandwrittenwords. Theyusea4-layerbidirectionalLSTM
tocreateanembeddingofthetargetcharactersequencefedtothegenerator. Further,anauxiliarytextrecognition
networkconsistingofaCNNencoderandLSTMdecoderevaluatesthegeneratedimageinadditiontothediscriminator
toencouragefaithfulrecreationofthetargetword. TheresultingGANproducesrealisticimagesofFrenchandArabic
wordsthatimprovetextrecognitionresultsofaneuralnetworkwhenusedasadditionaltrainingdata.
Brocketal. [365]builduponSAGAN[361],increasethebatchsizebyfactor8andthewidthofeachlayerby50%,
doublingthenumberofparametersinthegeneratorandthediscriminator. TheirBigGAN achievesnewstate-of-the-art
resultsinclass-conditionalimagesynthesiswithhighresolutionsupto512×512andacontrollabletrade-offbetween
detailandvariety.
Lucˇic´ et al. [366] aim to train the BigGAN [365] with unlabeled data for conditional image generation. They
experimentwithunsupervisedclusteringandlinearclassifiers(pre-trainedorco-trainedwiththediscriminator)ontop
ofrepresentationsoftheimagestosubstitutelargepartsofthelabels(upto90%),achievingsimilarorbetterinception
andFIDscorescomparedtothenormalBigGAN.
Fengetal. [265]introduceCA-GAN,asymmetricandconvolutionalGANthatimplementscollaborativelearning
betweenthegeneratoranddiscriminatortoproviderealsampleinformationtothegeneratorandanattentionmechanism
forthegeneratortoremovespuriousfeatures. Thegeneratoranddiscriminatorinteractatmultipleconvolutionsteps
withtheattentionmechanism. CA-GANisusedtogeneratelabel-conditionalhigh-qualityHyperspectralImages(HSIs),
whicharepictureswithmultiplelayersoffeaturesperpixel,withthehelpofalimitedsamplesetandclassifythem.
ShortoverviewofotherusagesofconditionalGANs:
Approach Description Year
[353] FirstintroductionofconditionalGANsonMNISTdigitandimagetagsgeneration. 2014
[367] Conditional face image generation with the conditional GAN [353] architecture with de- 2014
convolutionalgeneratorandconvolutionaldiscriminator. Theconditionalvectorallowsage
specificationandotherattributesfoundinthetrainingdata. Toavoidthereproductionofthe
trainingdatabythegenerator,theconditionalvectorsarenotdirectlyusedbutaresampled
fromakerneldensityestimateofthetrainingdata.
Continuation...
45

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[368] Utilizinganobjectivefunctionbalancingmutualinformationbetweenobservedexamplesand 2015
predictedclassdistributionsagainsttherobustnesstoanGAN. Thisapproachextendsthe
regularizedinformationmaximizationtorobustclassificationagainstanoptimaladversary.
The study includes empirical evaluations of synthetic data and image classification tasks,
demonstratingtherobustnessoflearnedclassifiersandthefidelityofsamplesgeneratedbythe
adversarialgenerator.
[369] InvertibleconditionalGAN(IcGAN):Usingtwoencoderstocreateaninversemappingfrom 2016
imagestoalatentrepresentationzandconditionalattributes,allowingmodificationsofimages
withaconditionalDCGAN[267]whosegeneratoralsofunctionsasthedecoder. Themodel
isevaluatedwithdifferentconfigurations,enablingrealisticandcompleximagemodifications.
[370] Attribute-LayoutConditionedGAN(AL-CGAN):Generatingimagesofoutdoorscenesfrom 2016
semanticlayoutsandsceneattributes(e.g.,weather)withaDCGAN[267].
[371] GANforvideo(VGAN):Aspatio-temporalDCGAN[267]architectureforunconditionaland 2016
conditionalvideogeneration(e.g.,futurepredictionfromstaticimages)withmovingobjects
andastaticcamera. Generatesone-second-longvideosthatresemblerealvideoswithseparate
foregroundandbackgroundgenerators.
[372] SimGAN:UseaGANtorefinesyntheticdatafromasimulatorandmakeitrealisticwhile 2017
preservingthesimulator’sannotations. Anadditionallossisemployedtominimizetheapplied
per-pixeldifferenceoftheCNNrefiner.
[373] SeGAN:Segmentationandpaintingofoccludedpartsofanimage. AsegmentationCNN 2017
createsthecompletesegmentmaskfromapartialmaskobtainedbyanotherpre-trainedmodel
[374]andtheRGBimage. AconditionalGAN(similarto[335])thenpaintstheinvisible
partsoftheobjectbasedonthemasksandtheimage.
[375] TrainingaGANgeneratortolearnapixel-levelimagetransformationfromonedomainto 2017
another(e.g.,depthforanRGBimage)usingconvolutionsandfullyconnectedlayers. The
discriminatorisstructuredsimilarlyandoutputstheprobabilitythatanimagewassampled
fromthetargetdomain. Forsometasks,thegeneratorisfurtherconditionedusingacontent
similaritylossthatpenalizeslargedifferencesbetweentheinputandoutputofthegenerator.
[376] SegAN:TrainingaCNNtoproducesegmentationmasksformedicalimages(CTimages)and 2017
anadversarialcriticnetworkcomparesthegeneratedmasktothegroundtruthbyevaluating
featuresextractedwithaCNN.
[377] DualGAN:TrainingtwoconvolutionalGANs[335]totranslateimagesbetweentwodomains 2017
inbothdirectionsfromunpaireddata. Also,sincebothdirections’modelsareavailable,a
reconstructionlossisemployedtoimprovetraining. Insteadofadedicatednoisevectorz,
dropoutisusedinmultiplelayers.
[378] SteganographicGAN: UsingaDCGAN[267]generatortoencodeencryptedmessagesin 2017
natural-lookingimages,adiscriminatortoensuredatarealism,andasteganalyzernetworkto
retrievethemessageusingasharedkey.
[379] SRGAN:Generatoranddiscriminatorconsistingofmultipleconvolutionallayersgenerate 2017
super-resolution(factor4×)images. TheGANisadditionallytrainedonaperceptualloss
obtainedfromfeaturemapsofaVGGnetwork[186],adeepCNNforimageclassification.
[380] VariationalautoencodingWassersteinGAN(VAW-GAN):Voiceconversionwithaconditional 2017
VAE encoding phonetic content from speech parameters (spectral frames) and decoding
it depending on speaker identity. The VAE decoder is then treated as the generator of a
WassersteinGAN[285]andtrainedtogenerateclearerspeech.
[381] Triple-GAN:Jointlytrainagenerator,discriminator,andclassifierforsemi-supervisedlearn- 2017
ing,resultinginstate-of-the-artclassificationresultsandsmoothclass-conditionalgeneration
andinterpolationinthelatentspace.
[382] RecurrentGAN(RGAN)andRecurrentConditionalGAN(RCGAN)forreal-valued(medical) 2017
timeseriesgeneration. Theconditionalversionhasadditionalinputsbesidesnoiseanddata
forthegeneratoranddiscriminatorLSTMs,respectively. Themodelsareevaluatedusingan
evaluationscheme,trainedonsyntheticdata,andevaluatedonrealdata.
[383] Multi-AgentDiverseGAN(MAD-GAN):Usingmultiplegeneratorsandonediscriminator 2017
thatalsohastoidentifythegeneratorthatcreatedthesampletogenerateimageswithdifferent
classesinaconditionalandunconditionalsetting. Thediscriminatorpushescertaingenerators
todifferentclasses(modes)andimprovestheoverallperformance.
Continuation...
46

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[384] Variational InfoGAN (ViGAN): Combining VAEs with InfoGAN [101], using the VAE 2017
encodertogeneratealatentrepresentationz ofanobservationthatcombinedwithasetof
interpretablevariablescallowstogenerate/decodemodifiedimagesx˜ ∼ P(x|z,c). These
imagesarethenevaluatedbyadiscriminatorandarecognizerthatreconstructsc.
[362] AuxiliaryClassifierGAN(AC-GAN):Aclass-conditionaldeconvolutionalgeneratorproduces 2017
images,andtheconvolutionaldiscriminatoroutputsthereal/fakeprobabilitiesandaprobability
distributionoverallclassesforinputimages. Theobjectivefunctionencouragesbothmodels
tomaximizetheclasslikelihood,whilethegeneratoraimstominimizethecorrectreal/fake
judgments that the discriminator tries to maximize. The model works better on higher-
resolutionimagesandachievesastate-of-the-artISonCIFAR-10.
[385] StructureCorrectingAdversarialNetwork(SCAN):ACNNgeneratorlearnssegmentation 2017
masksofchestx-rays,andacriticnetwork(CNNandfullyconnectednetworkforclassifica-
tion)learnstodiscriminatebetweenrealandgeneratedmasksforanimage. Tomitigatemode
collapse,thegeneratorispre-trainedwithpixel-wiseloss.
[386] ImagemanipulationwithtextdescriptionsusingageneratorthatconsistsofaCNNimage 2017
encoder,apre-trainedRNNtextencoder,aresidualtransformationunitthatjointlyencodes
textandimageembeddingsfurtherandadecoderthatreconstructstheimagewithupscaling
layers. ACNNdiscriminatorevaluatestheprobabilitiesofthegeneratedimageandthetext
descriptionmatching.
[359] CycleGAN: Unpaired image-to-image translation (i.e., two unrelated sets of images with 2017
norelationinformationprovided)bylearningmappingG : X → Y andinversemapping
F : Y → X and adding a cycle consistency loss F(G(X)) ≈ X next to the adversarial
loss G(X) ≈ Y. The model is implemented as CNNs and used for style transfer, object
transfiguration,seasontransfer,andphotoenhancement.
[387] BicycleGAN:Imagetranslation(e.g.,night-to-dayimageconversion)withinvertiblelatent 2017
codes to prevent many-to-one mappings (i.e., mode collapse). For that purpose, a genera-
tor/decoderisconditionedonaninputimageandalatentvectortoproduceasuitableoutput
image,andaVAEencoderistrainedtomaptheoutputbacktothesamelatentcodeanda
predefineddistribution.
[388] Unsupervisedimage-to-imagetranslationwithcoupledGANsutilizingasharedlatentspace 2017
assumption. TwoencodersE andE translateimagesfromtwodomainstothesamelatent
1 2
spacez. ThegeneratorsG andG serveasdecodersofaVAEandrecreateimagesfrom
1 2
z suitable for the domain. Their performance is evaluated by discriminators D and D
1 2
respectively. Thehigh-levelconnectionweightsbetweentheencodersandthegeneratorsare
tiedtoaccountforthesharedlatentspaceassumption.
[389] ConditionalCycleGAN:ExtendingCycleGAN[359]withanadditionalattributeconditionvec- 2017
tor(e.g.,haircolor,gender,smiling)forfaceimagesuper-resolutionandattribute-conditional
translation.
[390] ShowcasingthatGANscanproducehigherqualitysamplesbyusingaconditionalsetup,more 2017
precisely,whenclasslabelsareprovided. Theapproachproposedaugmentsclasslabelsby
clusteringtherepresentationspacelearnedbythemodelitself. Themethodis,however,based
onthemorecomputationallycostlyWassersteinGANapproach.
[391] Usingthepix2pix[335]approachtogenerateinfraredimagesandvideoswithtrackinglabels 2018
forentitiesfromlabeledRGBvideoframes.
[392] PerceptualAdversarialNetwork(PAN):Animage-to-imagetransformationCNNT learns 2018
mappingsbetweendomainsandadiscriminatorCNNDtriestofinddiscrepanciesbetween
transformedimagesandgroundtruth.
[393] Text-adaptiveGAN(TAGAN):AGANthatallowsthemodificationofimagesusingnatural 2018
language descriptions while preserving text-irrelevant features of the original image, for
example, the form of an object. The generator is an encoder-decoder architecture derived
from[386]thatcombinestheimageembeddingwiththetextrepresentationobtainedfrom
abidirectionalGRUworkingonpre-trainedfastText[394]wordvectors. Thetext-adaptive
discriminatorclassifieseachattributeindependentlyusingword-leveldiscriminators.
Continuation...
47

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[395] vid2vid: Video-to-videosynthesisfromsegmentationmasksorothersourcestophotorealistic 2018
outputwithGANsandaspatiotemporaladversarialobjective. Arecursivelyappliedfeedfor-
wardneuralnetworkgeneratesthenextframebasedonthecurrentsourceframeandthepast
sourceandgeneratedframes. Aconditionalimagediscriminatorcomparesthecurrentsource
andthegeneratedimage. Additionally,aconditionalvideodiscriminatorestimatestheoptical
flowofthegeneratedsequencetoensureplausibletemporaldynamics.
[396] TrainingaprogressiveGAN[303]toproducefaceimagesconditionedontheidentityem- 2018
beddingofaperson. Theidentityisbuiltwithdiscretelabelsandconvertedtoacontinuous
representationthatfollowsasimpledistribution. Themodelcanbeusedforconditionaland
unconditionalimagegenerationandimprovesandalleviatesthetrainingoffacerecognition
modelsbyboostingthetrainingdatasizewithinterpolatedimagereconstructions.
[397] Produceidentity-preservingphotorealisticfaceimagesfromrenderingsofa3Dmorphable 2018
modelshowingdifferentposes,expressions,andilluminationswithaconditionalGAN. The
GANusessemi-supervisedlearning,soittrainswithafewpairsofrealandrenderedface
imagesandhasalargeamountofunpaireddataavailable.
[398] Graph-translationGAN(GT-GAN):AGANconsistingofa(de)convolutionalgraphtranslator 2018
withanencoder-decoderstructurepittedagainstaconditionalgraphdiscriminatorthattakes
the translated/real graph pairs as input and uses the same CNN as the encoder to classify
whethertheyarerealorfake.
[399] MaskGAN:TrainingaGANfortextgeneration. ThegeneratorconsistsofaLSTMencoder 2018
thatgeneratesacontextrepresentationoftextwithmaskedtokensandaLSTMdecoderthat
takesthecontextandthemaskedtexttoautoregressivelyfillinthegapsandreconstructthe
sequenceprobabilistically. ThediscriminatorisaLSTMsimilartothedecoderandoutputs
the probability of a token in the sequence to be real. On top of the discriminator, a critic
networkcomputesarewardfunctionbasedonthepredictedtokenlikelihoodsusedtotrain
thegenerator. Themodelisalsousedforunconditionaltextgenerationbymaskingtheentire
input.
[400] Usingthepix2pix[335]GANapproachtogenerateimagesandsegmentationmapsofbrains 2018
andtumors.
[401] MakingtheimprovedWassersteinGANwithgradientpenalty[286]differentiallyprivateby 2018
addingGaussiannoisetotheactivationsofthesecond-to-lastlayerofthediscriminator. The
modelisusedtoproducelabel-conditionedimages.
[402] GANsynth: High-fidelity and locally-coherent audio (music notes) synthesis using high- 2019
resolution frequency spectrograms, several orders of magnitude faster than autoregressive
models. Thegeneratorisadditionallyconditionedonaone-hotpitchlabelthatthediscrimina-
tortriestopredictwithanauxiliaryclassifier.
[403] Labeled-GraphGAN(LGGAN):AnimprovedWassersteinGAN[320]approachthatuses 2019
a MLP generator to produce adjacency and one-hot node label matrices for graphs and a
graphconvolutionalnetwork[84]withresidualconnections[374]asthediscriminator. Both
conditionalandunconditionalconfigurationsarepresented.
[404] DP-CGAN:DifferentiallyprivatedatagenerationusingaconditionalGANthatinjectsGaus- 2019
sian noise and clips the discriminator gradients to limit the amount of information from
thetrainingdatatransferredtothegenerator. Themodelistraineduntiltheprivacybudget
monitoredbyaRényidifferentialprivacyaccountant[405]isspent. Themodelimproveson
differentiallyprivateresultsonMNISToverasimplerbaselineconditionalGANmodel.
[406] Misc-GAN:Translatinggraphsfromasourcetoatargetdomain(e.g.,foranonymization)by 2019
extractingcoarse(partial)structuresfromrealgraphsusingclusteringmethods,permutating
them,generatingnewcoarsegraphsfromthesetemplates,andcombiningthegeneratedcoarse
graphstoproduceafullsyntheticgraph.
[407] COCO-GAN:AconditionalGANonlytrainedusingso-calledmicropatchesofimagedatasets. 2019
The generator and discriminator learn only parts of the image via conditional formatting;
however,theycangeneratefullimagesduringtheinferencephase.
[95] ConditionalTabularGAN(CTGAN):AGANtoeffectivelygeneratetabulardatawithmixed 2020
discreteandcontinuouscolumns.Thegeneratorisconditionedonaone-hotvectordetermining
arandomlyselectedcategoryandsamplesarow(eachcolumnindependently)fromthelearned
marginaldistributions. Thecriticthenscoresthegeneratedsampleagainstarandomsample
fromthetrainingdatamatchingthesamecriterion.
Continuation...
48

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[408] MedGAN:Image-to-imagetranslationinthemedicaldomainusingaCasNetgeneratorthat 2020
progressivelyrefinestheimageviaencoder-decoderpairs. Thisfeature-extractingdiscrimina-
torevaluatesthepresenceofdesiredmodalitiesandnon-adversariallossesthatevaluatethe
generatedimage’sstyle(e.g.,structureandtextureapplication).
[409] Mol-CycleGAN:UsingCycleGAN[359]toenablethebidirectionaltranslationofmolecule 2020
embeddingsbetweenmoleculeswithandwithoutanoptimizedproperty. TheGANoperates
inthelatentspaceofajunctiontreeVAE[127],simplifyingtrainingbecausethesimilarity
measureusedforthismoleculerepresentationisdifferentiable.
[410] SMOOTH-GAN:EHRgenerationconditionedondiagnosiscodes(binaryvectorofpresent 2020
diseases)builtupontheconditionalGAN[353]withtheWassersteinGANgradientpenalty
loss[285,286].
[411] WG2GAN:Image-to-imagetranslationtogeneratewoundsfromsegmentationmapswitha 2021
conditionalGAN.
[412] UsingamodifiedDCGAN[267]togeneratelungCTimagesforCOVID-19classification. 2021
2.13.2 Deep/StackedGANs
DeepGANscontainmultiplelayersofgeneratorsanddiscriminatorsorsharepartialresults(e.g.,imagesatdifferent
resolutionsandtherespectivediscriminativefeedback)atspecificstepswitheachother. Thisallowsthediscriminator(s)
toevaluatethefinalproduct,assesshigher-orderfeatures,andprovidemoredetailedfeedbacktothegenerator(s),often
resultinginbetterresults.
Dentonetal. [413]introduceLAPGAN,aLaplacianpyramidframeworkhavingconditionalCNNstrainedwithGANs
ateachlayertogeneratecoarse-to-fineimages. Forthispurpose,thegeneratorupsamplestheimagefromtheprevious
stagetodoublethewidthandheightandthenappliesaconvolutionbasedontheupscaledimageandrandomnoise.
During the training process, a high-resolution image I is downscaled, blurred, and upscaled again. This modified
versionlisthenusedtoeithergeneratearealhigh-passimageh=I−lorsyntheticsampleG(z,l)thatisgivento
thediscriminatortogetherwithltodeterminewhetheritisrealorgenerated. Log-likelihoodevaluationwithParzen
windowestimatesandhumanevaluationshowthatLAPGANproducesmorerealisticresultsthanastandardGAN.
Zhangetal. [414]proposeStackGAN,wherethetext-to-imagetaskisdividedintotwostages. ThefirststageGAN
drawstheshapeandcoloroftheobjectdescribedbythetext. Instagetwo,asecondGANrefinesthesketchgiventhe
textdescriptiontoproducephoto-realisticimages. StackGANoutperformspreviousstate-of-the-artconditionalGAN
modelsGAN-INT-CLS[356]andGAWWN[357]intermsofresolution(256×256pixels)andrealism.
Shortoverviewofotherusagesofdeep/stackedGANs:
Approach Description Year
[415] StackedGANs: Astackofsymmetricencoder-decoderlayerswithlayer-wiserepresentation 2017
pair discriminators and a Q-Net that evaluates the diversity of the output of the genera-
tor/decoderateachlayer. Eachgeneratorlayerhasitsindependentnoiseinputandprevious
layer input, which allows conditioning on the output of the encoder. The resulting label-
conditionedimagesareofhigherqualitythancomparedshallowGANs.
[416] Atwo-stageGANapproachforretinaimages. InthefirststageGAN,vesseltreesegmentation 2017
masks are generated with the help of a small human data set. In stage two, a conditional
DCGAN[267]learnstocreatethecorrespondingretinafundusimageforthevesseltree.
[417] TransGAN:AdeepGANconsistingofapurelytransformer-basedarchitecture,excluding 2021
conventional convolutional layers. TransGAN consists of a memory-friendly transformer-
basedgeneratorthatprogressivelyincreasesfeatureresolutionandamulti-scalediscriminator
thatcapturesbothsemanticcontextsandlow-leveltextures. Thestudyincludesanewgrid
self-attentionmoduleforhigh-resolutionimagegenerationandauniquetrainingprocedureto
addresstheinstabilityissuesassociatedwithTransGAN.
2.13.3 BidirectionalGANs
A Bidirectional GAN (BiGAN) [418], also introduced as Adversarially Learned Inference (ALI) [419], lets the
discriminatorevaluatedata-representationpairs(x,z)ofeitherageneratorx=G(z)creatingdatafromarepresentation
oranencoderz =E(x)inverselygeneratingrepresentationsfordataanddecide,whetherxisrealorfake(seeFigure35).
Theresultisamodelthatlearnsmeaningfuldatarepresentationsfordetectionorclassificationtasksdespitetheencoder
49

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
andgeneratorbeingunabletocommunicate.Itcanalsobeusedsimilarlytoanautoencoderx˜=G(E(x))forgenerative
tasks,forexample,imagegeneration. [418]
features data
z G G(z)
G(z),z
D P(y)
x,E(x)
E(x) E x
Figure35: TheBiGANarchitecture. (Source: [418])
Donahueetal. [420]proposeBigBiGAN,whichcombinestheBigGAN[365]withtheencoderofaBiGAN.They
furthermodifytheBigGANdiscriminatortocomputeascoreforxandz,respectively,andajointscore. BigBiGAN
achieves state-of-the-art results in unsupervised representation learning and unconditional image generation tasks,
outperformingBiGANandBigGAN,respectively.
2.13.4 AdversarialAutoencoders
The Adversarial Autoencoder (AAE) is a probabilistic autoencoder whose latent representations z ∼ q(z) of the
encodeddataareforwardedtoadiscriminatorwhotriestodistinguishthesamplesq(z)fromonesofaprioruser-defined
distributionp(z)andprovidesanadversarialloss,asseeninFigure36. Byusingthevariationalinferencetechnique
similartoaVAE(seeSection2.7.5),theautoencoderlearnstomapdatatoandgeneratemeaningfulsamplesfromthe
wholespacedefinedbythepriorp(z),whichisconfigurablebytheuserandallowslearningofpowerfulrepresentations
(see Figure 37 for example) for classification, disentangling of style and content, unsupervised clustering or data
visualization. [421]
Figure36: ArchitectureofanAdversarialAutoencoder. (Source: [421])
Makhzani et al. [421] demonstrate the generative capabilities of the AAE on MNIST, SVHN and TFD, achieving
state-of-the-artlog-likelihoodonthetestdatacomparedtothestandardGAN[238],GenerativeMomentMatching
Network(GMMN)[422],DBN[65]andGSN[94]andallowingthecombinationofdisentangledstyles(writingstyle
orfont)andcontents(numbers)onMNISTandTFD.
Tolstikhinetal. [423]proposetheWassersteinAutoencoder(WAE)asageneralizationoftheAAE,inspiredbythe
WassersteinGAN[285]adversarythatusestheprobabilitydistributiondiscrepancybetweenrealandgenerateddata
astheadversarialloss. Twoapproachestocomputethediscrepancybetweenqandparepresented: TheWAE-GAN
incorporatesanadversarythatapproximatestheJensen-Shannon(JS)divergenceaslossandistrainedtogetherwiththe
autoencoder,whiletheWAE-MMDusedanadversary-freeMMD-basedloss,similartoGMMNs(seeSection2.14).
WAE-GANislessstablebutgenerateshigherqualitysamplesthanWAE-MMDandanormalVAE.
50

| ComprehensiveExplorationofSyntheticDataGeneration: |     |     |     | ASurvey |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- |
B
A
|     | C   |     | D   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure37: ByforcingthelatentspacedistributionofanAdversarialAutoencoderintospecificregions,forexample,
toseparatedifferentnumbersofMNIST,thequalityandinterpretabilityofrepresentationscanbegreatlyimproved.
(Source: [421])
ShortoverviewofotherusagesofAAEs:
| Approach | Description |     |     |     |     |     |     | Year |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | ---- |
[424] AnAAEisusedtogeneratesuitablemoleculefingerprintsforcancertreatment(trainedon 2017
6252samples),andtheseprobabilisticfingerprintsareusedtosearchforsimilarrealmolecules
inthePubChemdatabasewith72millionentries.
[425] druGAN:AnimprovedAAEtrainedonlargerdatasetsthanKadurinetal.[424]thatdemon- 2017
stratessuperiorreconstructionresultsoveracomparableVAEwiththesamesamplingvariabil-
ity(i.e.,coverage),whichtheyidentifyisatrade-offnecessaryforgenerativeautoencoders.
[426] End-to-endretinalimagegenerationwithanAAEgeneratingthevesselnetworkandacondi- 2017
tionalGANcreatingthecorrespondingfundusimage. TheGANdiscriminatorthenevaluates
thevessel-funduspairsintermsofrealism.
[427] AnAAEwithanadditionalclassificationstepforbiomedicaltimeseriesgeneration. This 2021
allowstheauthorstogeneratelabeledtimeseriesdatausingasemi-supervisedapproach. A
dimensionalityreductionisfurtherintroduced,transformingthree-dimensionalbiomedical
breathingdataintoone-dimensionaltimeseriesandback.
2.14 GenerativeMomentMatchingNetworks
GenerativeMomentMatchingNetworks(GMMNs)useaneuralnetworktolearndeterministicmappingsfroman
easy-to-sample data distribution to the real data distribution, similar to a GAN generator. The model starts with a
top hidden layer h ∈ RH whose elements are usually independently sampled from a uniform distribution so that
(cid:81)H
p(h)= U(h ). Then,hispassedthroughmultipleneuralnetworklayersuntilthefinaloutputisreturnedasa
|             | j=1 j |     |     |     |     |     |     |     |
| ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| datasample. | [422] |     |     |     |     |     |     |     |
TheGMMNistrained,unlikeaGANgenerator,minimizingtheMMDcriterioninsteadofadversarialtrainingwitha
| discriminator. | TheMMDcriterionisdefinedas |                  |              |                  |           |                  |             |      |
| -------------- | -------------------------- | ---------------- | ------------ | ---------------- | --------- | ---------------- | ----------- | ---- |
|                |                            | 1 N              | N            | 2 N              | M         | 1 M              | M           |      |
|                |                            | (cid:88)(cid:88) |              | (cid:88)(cid:88) |           | (cid:88)(cid:88) |             |      |
|                | L                          | =                | k(x ,x i′ )− |                  | k(x ,y )+ |                  | k(y ,k j′ ) | (30) |
|                | MMD2                       | N2               | i            | NM               | i j       | M2               | j           |      |
|                |                            | i=1i′=1          |              | i=1j=1           |           | j=1j′=1          |             |      |
andcomputes,whetherthegeneratingdistributionsfortwosetsofsamplesX = {x }N andY = {y }M arethe
|     |     |     |     |     |     | i   | i=1 j | j=1 |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
sameusingaGaussiankernelk(x,x′)=exp(− 1 |x−x′|2)withσbeingthebandwidthparameter. Thegradientis
2σ
differentiable;thatis,thegradientcanbebackpropagatedtoupdatetheparametersoftheneuralnetwork. Thelargerthe
dimensionalityofthedata,themoretrainingdataisrequiredtoestimatethedatadistribution. [422]
51

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Lietal. [422]useaGMMNwithfourintermediatenon-linearReLUlayersandalogisticsigmoidoutputlayerto
modeltheMNISTandTFDdatadistribution. Further,theyimprovetheirgenerativemodelbytrainingtheirGMMNon
topofthelatentrepresentationofanautoencodertoreducethedatadimensionalityand,consequently,theamountof
trainingdataneeded.
Lietal. [428]proposeMMDGAN,whichreplacestheGaussiankernelofaGMMNwithanadversarialkernellearning
techniquetoreducetheamountofrequiredtrainingdataandimprovethemodelaccuracyandefficiency. TheGaussian
kernel is modified with injective functions f with optimizable parameters ϕ, resulting in the new kernel function
ϕ
k˜(x,x′)=exp(−∥f (x)−f (x′)∥2). TheGMMNmodel(generator)parametersθandMMD(discriminator)kernel
ϕ ϕ
parametersϕarethenadversariallyoptimizedinaminimaxgamemin max L (X,Y ),likeinaGAN,minimizing
θ ϕ ϕ θ
thegeneratorlossfortheworstpossiblediscriminatorresult.
ShortoverviewofotherusagesofGMMNs:
Approach Description Year
[429] MMDnets: Proposaloftraining/initializinggenerativeneuralnetworkswiththeinexpensive 2015
MMDstatisticinsteadofaGANdiscriminatoratthesametimeasLietal.[422].
[430] ConditionalGMMN: Feedingasampledrawnfromasimpledistributionandtheconditional 2016
variablestothenetworkthatgeneratesthetargetsample. AconditionalMMDcriterionis
developedtolearntheparameters. ThemodelisusedforconditionalgenerationofMNIST
andfaceimages,combinedwithanautoencoderlikeLietal.[422].
[431] SpeechsynthesisbysamplingspeechparametersfromaGMMN-learneddistributiontoinduce 2017
variationinthegeneratedspeechandmakeitmorenatural.
[432] IntroducingarepulsivelossfunctiontoaddressthelimitationsofexistingMMDlossfunctions 2018
thatmayhinderlearningfinedetailsindata. Therepulsivelossfunctionenhanceslearningby
emphasizingdifferencesamongrealdatasamples. Additionally,thestudyproposesabounded
GaussiankerneltostabilizeMMD-GANtraining. Themethodsareappliedtounsupervised
imagegenerationtasksondatasets, showingsignificantimprovementsoverthetraditional
MMDlosswithoutadditionalcomputationalcosts. Thepaperalsoexploresregularization
techniquesforMMDandthediscriminator,contributingtothestabilityandeffectivenessof
thetrainingprocess.
[433] Generationofhigh-dimensionalloadcurves(cooling,heating,power)ofintegratedenergy 2022
systemswithaCNNgeneratorandtransformationofrealandgeneratedsamplestolatent
spacewithanautoencoderwherethedistributionsarecomparedusinganMMDloss.
2.15 Plug&PlayGenerativeNetworks
Plug&PlayGenerativeNetworks(PPGNs)consistofapre-trainedgeneratornetworkGwithlatentvariablespace,
usuallyobtainedfromaGAN,andareplaceable(“plugandplay”)pre-trainedconditionnetworkC,whichcanbea
classifierorimagecaptioningnetworkforexampleand“tellsthegeneratorwhattodraw”. Theclassprobabilitiesofthe
classifierareusedtoperformgradientascentonthelatentspaceofthegenerator,iterativelyimprovingthegenerated
results. GandC canevenbetrainedondifferentdatasetsordomains,allowingforatleastalimitedformofdomain
transfer. [434,435]
Nguyenetal. [434]introducethedeepgeneratornetworkwithactivationmaximization,shortDGN-AM(seeFigure38),
whichistheoriginofPPGNs. Itaimstosynthesizedatafromapre-trainedgenerator,whichmaximizestheactivation
ofaspecificneuronofaclassifier. Thearchitectureproducesimagesofstate-of-the-artqualitybutlittlediversity[435].
Inanotherwork[435],Nguyenetal. improveuponthelackofdiversityofDGN-AMbylearningapriordistribution
forthelatentvariableofthegeneratorusingaDAE,whichservesasanadditionaloptimizationcriterion. Theyfurther
definethegeneralizedclassofPPGNsandexperimentwithotherbuildingblockslikeimagecaptioningnetworksfor
theconditionnetwork. TheyachievehighersamplequalityanddiversitythanDGN-AM.
2.16 Copulas
AcopulaC modelsanddecomposesthejointprobabilitydistributionofacontinuousrandomvectorXintoaproduct
ofthemarginaldistributionsandarepresentationofthemarginalvariables’dependencestructure. [436]
Thecreationofacopulamodelreliesheavilyonestimation: First,themarginalcumulativedistributionfunctionsF for
i
individualrandomvariablesX areapproximatedwiththehelpoftrainingdataandconvertedtoauniformdistribution
i
usingprobabilityintegraltransform. Then,thevariables’dependenciesandcorrelationscanbeestimatedinvarious
52

| ComprehensiveExplorationofSyntheticDataGeneration: |     |     |     |     | ASurvey |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
Image
Code
Forward  and  backward  passes
..
candle
banana
...
...
|     |     | u9  | u2  |     | c2 c3 | c4 c5 |     |     |     |
| --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- |
convertible
|     |     |     |     | u1 c1 |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
...
|     | fc6 |                 |     |     |               |     | fc8     |     |     |
| --- | --- | --------------- | --- | --- | ------------- | --- | ------- | --- | --- |
|     |     | upconvolutional |     |     | convolutional |     |         |     |     |
|     |     |                 |     |     |               |     | fc6 fc7 |     |     |
Deep  generator  network
|     |     | (prior)   |                                          |     | DNN  being  visualized |     |        |     |     |
| --- | --- | --------- | ---------------------------------------- | --- | ---------------------- | --- | ------ | --- | --- |
|     |     | Figure38: | ExampleofthefirstPPGN,theDGN-AM.(Source: |     |                        |     | [434]) |     |     |
Figure2: Tosynthesizeapreferredinputforatargetneuronh(e.g. the“candle”classoutputneuron),
weoptimizethehiddencodeinput(redbar)ofadeepimagegeneratornetwork(DGN)toproduce
animagethathighlyactivatesh. Intheexampleshown,theDGNisanetworktrainedtoinvertthe
ways, forexample, nonparametricallyviakernelestimation[437,436]ordecompositionintotreesofpair-copulas
cafleleadtuvrienerse[p4r3e6s]e.ntationsoflayerfc6ofCaffeNet. ThetargetDNNbeingvisualizedcanbeadifferent
network (with a different architecture and or trained on different data). The gradient information
Lietal. [438]introduceDPCopula,atechniquetosynthesizedifferentiallyprivatemulti-dimensionaldatawithcopula
(blue-dashedline)flowsfromthelayercontaininghinthetargetDNN(here,layerfc8)alltheway
functions efficiently. They propose two metrics, maximum likelihood estimation, and Kendall’s τ correlation, to
throughtheimagebacktotheinputcodelayeroftheDGN.NotethatboththeDGNandtargetDNN
estimatetheparametersoftheGaussiancopulafunction. Bothmethodsareanalyzedintermsofprivacyguaranteesand
cobmepinugtatvioisnuaallciozmedplhexaivtyeofinxceednspuasrdaamtaesteetrss,,oauntpdeorfpotrimminizgaptrioevnioounslsytacteh-aonf-gthees-athrteaDppGroNachinepsulitkecoPdrieva(treeSdp).atial
Decomposition(PSD)andP-HP(lossycompression),especiallyonhigh-dimensionaldatasets.
Ktuhlkeanrneiuertoanl.o[4f3i7n]teurseesvtin(eFicgo.pu2l)a.sOtouitrermateivtheloydgerensetrraitcetmsothbeilistyeatrracjhecttoorioens,lywhthicehsaeretdoeffiinmedagasesattehmatpocraanlly
orbdeerdedrasweqnuebnycethTe=pr⟨i(olr1,,wt )h,i.c..h,(pl nro,tvni)d⟩ewsiathsltorcoantigonbsial is(ecseltloIwDas)rdanrdeatilmisetsitcamvipssutail.iTzahteiyofinnsd. Btheactathuesceoopuulras
1
maoldgeolroibthsemrveudsestsataisdtiecaelpagndenseemraatnotricn/geetowgorarpkhticospimeriflaorrimtiesapcatirvtiactuiloanrlymwaexllimatiazafrtaioctnio,nwoeftchaellcoitmDpuGtaNti-oAnaMlc.ost
ofneuralnetworkapproacheswhilealsoincorporatinglong-rangedependencies. LessaccuratemodelslikeRNNsand
GANsperformbetterintheirprivacytests.
Tagaskova 2 Methods et al. [436] propose Vine Copula Autoencoder (VCAE), which utilize a CNN autoencoder based on
DCGAN[267]toextractlower-dimensionalrepresentationsfromdataandfitanonparametricvinecopulatolearnthe
representations’distribution. Bysamplingfromthetrainedcopula,thedecoderoftheautoencodercanbeusedasa
ge ne r a tiv e m od el . Th e V C A E i s te s teWdoendthermeeorneaslt-rwatoerldouimravgiesudaatlaizsaettsioinntmermetshoofdMoMnDasvcaorreieatnydoCfladsisfiffieerreTnwto
| N e t w o | rk s th a t w | e v i su a | l iz e . |     |     |     |     |     |     |
| --------- | ------------- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
SampleTest(C2ST)accuracy: MNIST,SVHN,andCelebA.VCAEperformssimilartoDCGANandoutperformsthe
networks. For reproducibility, we use pretrained models freely available in Caffe or the Caffe
VAE.
ModelZoo[20]: CaffeNet[20],GoogleNet[21],andResNet[22]. Theyrepresentdifferentconvnet
architecturestrainedonthe 1.3-million-image2012ImageNetdataset[23,19]. OurdefaultDNNis
2.17 NormalizingFlowModel∼s
CaffeNet[20],aminorvariantofthecommonAlexNetarchitecture[24]withsimilarperformance
[20]. Thelastthreefullyconnectedlayersofthe8-layerCaffeNetarecalledfc6,fc7andfc8(Fig.2).
Normalizingflowsaredeterministicinvertibletransformationsf :E →Zwithparametersθbetweenabasedistribution
Ef(ce8.g.i,sGthaueslsaiasntdlaisytreirbu(tpioren)saonfdtmobasxe)rvaantidonhaalssp1a0ce00Zo. Tuthpeuttrsa,nsofnoremfaotrioenaccahnIbmeuasgeedNtoetcacllcauslsa.tetheexactdensity
(probability) of an observation by using f−1 : Z → E or sample new observations by sampling from the simpler
|                 |                                      |          | We denote | the DNN | we want | to visualize | by Φ. Instead | of previous |     |
| --------------- | ------------------------------------ | -------- | --------- | ------- | ------- | ------------ | ------------- | ----------- | --- |
| Image           | generator                            | network. |           |         |         |              |               |             |     |
| distributionϵ∈E | andtransformingittoobservationspacez |          |           |         | ∈Z.     | [439]        |               |             |     |
works,whichdirectlyoptimizedanimagesothatithighlyactivatesaneuronhinΦandoptionally
∈RD
AutoregressiveFlows(AFs)areavariantofnormalizingflowsthatmodelsanobservationz satisfies hand-designed priors embedded in the cost function [5, 7, 9, 6], here we optimize as in the
inputcodeofanimagegeneratornetworkGsuchthatGoutputsanimagethathighlyactivatesh.
)2),withµ
|     | p(z | |z  | )=N(z |µ | ,(α | =g  | (z ;θ),α | =g (z ;θ), |     | (31) |
| --- | --- | --- | -------- | --- | --- | -------- | ---------- | --- | ---- |
ForGweusenetwdor1k:ds−m1 adepubdlicdlyavdailablebyd[11]µtha1t:dh−a1vebeedntraαined1:dw−1iththeprinciplesof
GANs [17] to reconstruct images from hidden-layer feature representations within CaffeNet [20].
whereg andg
HowµG trαained areunconstrainedpositivescalarfunctions,usuallyimplementedasneuralnetworks,thatcomputethe
is includes important differences from the original GAN configuration [17]. Here
| meananddeviationforanormaldistributionN. |     |     |     | Thetransformationsaredefinedas |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
wecanonlybrieflysummarizethetrainingprocedure;pleasesee[11]formoredetails. Thetraining
process involves four convolutional networks: 1) a fixed encoder network E to be inverted, 2) a
z −µ
generatornetworkG,3)affi(xϵe)d=“czom=pµara+toαr”·nϵet;wfo−r1k(zC)a=ndϵ4=)ad d iscri d m. inatorD. Gistrained(t3o2)
|                                                                                     |     |     | θ d d | d   | d d θ d | d   |     |     |     |
| ----------------------------------------------------------------------------------- | --- | --- | ----- | --- | ------- | --- | --- | --- | --- |
| invertafeaturerepresentationextractedbythenetworkE,andhastosdatisfythreeobjectives: |     |     |       |     |         | α   |     |     |     |
1)for
a f e a tu re v e c to r y = E ( x )R,t he s y n t h e s i z e d im a g e G ( y ) h a s t o b e c l o se to th e o r ig in al im a g e x ;
To s a m p le z fr o m a n AiF ,fir st ϵ ∈i D is s a m p l e d , t h en z i s co m p utie d u s in g E q ua t i on 32 . F in al ly , ea ch su bs eq u e ntiz
|     |     |     |     |     | 1   |     |     |     | d   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
canbecomputedusingEquation31. 2)thefeaturesoftheoutputimageC(G(y [439] ))havetobeclosetothoseoftherealimageC(x );3)
|     |     |     |     | i   |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D shouldbeunabletodistinguishG(y )fromrealimages. TheobjectiveforD istodiscriminate
i
betweensyntheticimagesG(y )andrealimagesx asintheoriginalGAN[17].
|     |     |     | i   |     | 53 i |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
Inthispaper,theencoderE isCaffeNettruncatedatdifferentlayers. WedenoteCaffeNettruncated
atlayerl byE ,andthenetworktrainedtoinvertE byG . The“comparator”C isCaffeNetupto
|     | l   |     |     |     | l   | l   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
layerpool5. D isaconvolutionalnetworkwith5convolutionaland2fullyconnectedlayers. Gisan
upconvolutional(akadeconvolutional)architecture[15]with9upconvolutionaland3fullyconnected
| layers. | Detailedarchitecturesareprovidedin[11]. |     |     |     |     |     |     |     |     |
| ------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
3

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Shi et al. [439] propose GraphAF for graph-based molecule generation with parallel training, which uses AFs to
generategraphssequentially. Ateachstep,thetypeofthenextnode(madecontinuouswithadequantizationtechnique)
ispredictedbeforealledgestoexistingnodesaredetermined. Thenodeandedgedistributionparametersrespectively
µX andαX andµAandαAarecomputedwithMLPsthatareconditionedonthenodeembeddingsH thatareobtained
i i i i i
fromarelationalgraphconvolutionalnetwork[440]. Theauthorsadditionallyemployvalencychecking[231]toreject
invalidedgesandimplementaRLapproachforgoal-directedmoleculegeneration.
Shortoverviewofotherusagesofnormalizingflowmodels:
Approach Description Year
[441] Non-linearindependentcomponentsestimation(NICE):Learningofanon-lineardeterministic 2014
andeasilyinvertibletransformation(deepneuralnetwork)f thatmapsaninputxtoahidden
representationh = f(x)andback,sox = f−1(h). Thetrainingcriterionistheexactlog-
likelihood. Sincethetransformationsaredeterministic,noiseisinjectedathforgeneration.
Resultsinimagegenerationachievehighlog-likelihoodbutoftendonotlookrealistic.
[442] Real-valuednon-volumepreserving(realNVP)transformations: Efficientinvertiblemapping 2016
ofimagestolatentvariables.
[443] Glow: Usinganinvertible1×1convolutiontogeneraterealisticandlargeimages. 2018
[444] NeuralOrdinaryDifferentialEquation(ODE): Acontinuous-timemappingz(t)fromlatent 2018
variablestodatadefinedbyODEs,alsocalledcontinuousnormalflow[445]. Themodelis
usedtoaccuratelymodelandextrapolatetimeseriesorreplacediscretehiddenlayersofa
neuralnetwork.
[445] FFJORD:Combiningthecontinuousnormalflowprocedurefrom[444]withanestimatorof 2018
thelogdensityfortraininginsteadofusingmaximumlikelihood. Thissignificantlyreduces
thecomputationalcostandallowsunrestrictedarchitectures. Themodeloutperformsprevious
flow-basedmethodsondensityestimationandalsoimagegeneration.
[446] GraphNVP: The first flow-based invertible graph generation model that can handle fixed- 2019
size node type assignments and adjacency matrices together. The model maps the node
featureandannotationmatricestolatentrepresentations,whichcanalsoberandomlysampled
for generative purposes. They also train a simple linear regressor on the latent space for
property-targetedmoleculegeneration.
[447] Fourier Flows: This approach operates in the frequency domain, using discrete Fourier 2021
transformationtohandlevariable-lengthtime-serieswithvaryingsamplingratesandleveraging
the more computationally efficient convolutions in the frequency domain. Fourier Flows
appliesdata-dependentspectralfilterstothefrequency-transformeddata,enablingefficient
Jacobiandeterminantsandinversemappingcomputation. Thismethodshowscompetitive
performancecomparedtostate-of-the-artmodels.
2.18 ReinforcementLearning
In Reinforcement Learning (RL), an agent starts in a state s ∈ S within its environment and obtains an initial
0
observationω ∈Ω. Theagentthenhastodecideonanactiona ∈Aateachtimestept. Afterperformingtheaction,
0 t
theagentreceivesarewardr ∈R,thestatetransitionstos ∈S andtheagentgetsanewobservationω ∈Ω,as
t t+1 t+1
seeninFigure39. ThegoalofRListolearnandoptimizeapolicyπsothattheactionstakenmaximizethecumulative
reward. Therefore,theagentusesavaluefunctionV topredicttherewardforanaction. Thepolicycanbedeterministic,
soitcanbedefinedasπ(s):S →A,orstochastic,assigningaprobabilityπ(s,a):S×A→[0,1]toeachaction. A
significantadvantageofRListhattheagentdoesnotneedcompleteknowledgeorcontroloftheenvironment,which
oftenmakesitmorecomputationallyefficientthanclassicsupervisedandunsupervisedMLmethods. [448]
Agent
a ω r
t t+1 t
Environment
s → s
t t+1
Figure39: Agent-environmentinteractioninRL. (Source: [448])
54

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Ohetal. [449]predictthenextframesofAtarivideogamesconditionedonpreviousframesandplayeractions. Input
framesareencodedwithaCNN(andoptionallyaRNN)toextractspatio-temporalfeaturesandthencombinedwitha
1-hotencodedactionvariableinatransformationlayertoobtainahigh-levelpredictionofthenextframe. ACNNtakes
thispredictionandusesupsamplingtogenerateafull-sizeframe. Themodelistrainedonemulatorrecordingswiththe
correspondinguserinputsusingstochasticgradientdescentwithbackpropagationthroughtime. Thetrainedmodelcan
generatefutureframesforarbitraryinputsequences. Theevaluationshowsrealistic100-stepfutureframesforavariety
ofAtarigames.
Jiaetal. [450]trainapaintingagent’spolicywithRLtobrushstrokesstep-by-steponacanvasguidedbyareference
image. ThepaintingprocessofPaintbotconsistsofmultiplesteps:
1. Arandomstrokestartingpointponthecanvasisselected.
2. Imagepatchescenteredaroundpfromthereferenceimageandthecanvasactastheobservationo.
3. WhilethepredictedrewardV (o)ispositive,actions(strokes)areperformed,consistingofcontinuousvalues
π
forangle,length,color,andwidth,thecanvasisupdated,andpandoarebothupdatedtothenewposition.
Thisprocessisrepeateduntilaspecifiedsimilaritythresholdbetweenthereferenceimageandpaintingisreached. The
trainingprocessconsistsofanadditionallossfunctionusedtotrainthedeepneuralnetworkforrewardpredictionV
(seeFigure40).
(a)Duringtraining. (b)Aftertraining.
Figure40: ThePaintbotpaintingprocessduringandaftertraining. (Source: [450])
Krishnaetal. [451]useaRLapproachtosynthesizefull-resolutionCTimages. Theycreateanatomicallycorrect
semanticmasksandusetheirexistingconditionalGANstyletransfernetwork[363]tofillthegeneratedmaskedareas
withcorrecttextures. Semanticmasksarerepresentedasvectorsviab-splinesandprincipalcomponentanalysisfor
which the agent learns a policy. An image classifier CNN is used as the reward predictor and trained with human
feedbackontheagent’sgeneratedmasksthroughaninterface.
ShortoverviewofotherusagesofRL:
Approach Description Year
[452] Dialoguetextgenerationwithtwoagents,whichareencoder-decoderLSTMs. Agentsare 2016
rewardedfordisplayingthreeconversationalproperties: Informativity,coherence,andeaseof
answering.
[453] Extendingtheideafrom[452]fordialoguegeneration,butusinganadversarialdiscriminator 2017
todistinguishbetweenhuman-generatedandsyntheticdialoguesandusingtheprobabilities
putoutbythediscriminatorastherewardfunction.
[454] ORGAN:CombinationofaSeqGAN[295]withRLwheretheGANgeneratoristrainedwith 2017
a tunable reward function consisting of the discriminator classification result, a repetition
penalty,anddomain-specificobjectivefunctions. ThenetworkisevaluatedonSMILES[112]
moleculeandmusicalmelodygeneration.
[455] GenerationofSMILES[112]representationsofmoleculeswithspecificpropertiesusinga 2017
priorRNNtrainedonaSMILESdatabaseandauser-definedscoringfunctionasrewardsfor
anRLagentRNNinitializedbythepriorRNN.
[456] ApplicationofinverseRLtotextgeneration,wherearewardfunctionisalternatinglylearned 2018
ontrainingdataandanagentlearnsanoptimalpolicytomaximizethetotalreward. Inthe
implementation, a reward approximator MLP aims to maximize the log-likelihood of the
training set samples, and the text generator LSTM is trained with a policy gradient [457]
techniquebasedontherewardandentropyregularizationtoencouragemorediverseresults.
Continuation...
55

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
... Continuation
[458] Goal-directedmoleculargraphgenerationwithagraphconvolutionalpolicynetwork(GCPN): 2018
MoleculegenerationasaMarkovdecisionprocesswherethenextgraphstateonlydepends
onthepreviousone. Ateachstep,anewsubgraph,inthiscase,predefinedasallsingle-node
graphsofallallowedatomtypes,isconnectedtoanexistingnode,ortwoexistingnodesare
connectedbytheGCPN.TheGCPNisrewardedbyasumofdomain-specificandadversarial
rewardstoensurethemolecule’sutility,realism,andvalidity.
[459] Amadeus: Train a LSTM on a representation of multiple monophonic note streams that 2019
provideapolyphonicpieceofmusictosimplifythelearningprocess. ThenRLisappliedto
selecthigh-levelLSTMconfigurationsthatproducethedesiredoutputsinsteadofmodifying
weightsoroutputs.
[460] Addressingthecompoundingerrorsinsequentialgenerationbycombiningcontrastiveimita- 2021
tionandanenergymodel. Themodelaimstocaptureboththestep-wisetransitionsandthe
overalltrajectorydistribution,balancingthelocalandglobalpropertiesoftime-seriesdata.
2.19 DiffusionModels
DiffusionmodelsareMarkovchainsthatiterativelyaddGaussiannoisetodatax inaforwardprocessoverT stepsand
0
alsolearnthereverseprocessthatiterativelymapsthenoiseinputbacktothedatadistribution(seeFigure41). [461]
p (x x )
✓ t 1 t
x x <latexit sha1_base64="XVzP503G8Ma8Lkwk3KKGZcZJbZ0=">AAACEnicbVC7SgNBFJ2Nrxhfq5Y2g0FICsNuFEwZsLGMYB6QLMvsZDYZMvtg5q4Y1nyDjb9iY6GIrZWdf+Mk2SImHrhwOOde7r3HiwVXYFk/Rm5tfWNzK79d2Nnd2z8wD49aKkokZU0aiUh2PKKY4CFrAgfBOrFkJPAEa3uj66nfvmdS8Si8g3HMnIAMQu5zSkBLrlmO3R4MGZBSLyAw9Pz0YeKmcG5P8CNekKDsmkWrYs2AV4mdkSLK0HDN714/oknAQqCCKNW1rRiclEjgVLBJoZcoFhM6IgPW1TQkAVNOOntpgs+00sd+JHWFgGfq4kRKAqXGgac7p0eqZW8q/ud1E/BrTsrDOAEW0vkiPxEYIjzNB/e5ZBTEWBNCJde3YjokklDQKRZ0CPbyy6ukVa3YF5Xq7WWxXsviyKMTdIpKyEZXqI5uUAM1EUVP6AW9oXfj2Xg1PozPeWvOyGaO0R8YX7+bCp4F</latexit>   | x
T t ! x t 1 0
 ! ···  !       !    ! ···  !
<latexit sha1_base64="l4LvSgM7PR7I/kkuy5soikK4gpU=">AAAEoXictVLditNAFE7XqGv92a5eejOYLexKLU0VFKRQ9EYvhCrb3YUklOlk2g6dnzBzYrcb8zK+lU/gazhJK6atuiB4YODM+T/n+8YJZwY6nW+1vRvuzVu39+/U7967/+CgcfjwzKhUEzokiit9McaGcibpEBhwepFoisWY0/Px/G3hP/9MtWFKnsIyoZHAU8kmjGCwplHjeygwzAjThNM4Kz/jSXaZj05zFHIlp5pNZ4C1VgsUkliB2TX/oQLYCpe/4rJwZhJM6NPMJyLPt9IM0SwBA0tOUaVGBs/8/J8mWVRH6eSjhtdpd0pBu4q/VjxnLYPR4d7XMFYkFVQC4diYwO8kEGVYA7P183qYGmr3meMpDawqsaAmykpEctS0lhhNlLZPAiqt1YwMC2OWYmwjiynNtq8w/s4XpDB5FWVMJilQSVaNJilHoFABL4qZpgT40irYntTOisgMa0zAkqC+0QbY/MquIfCcYssbsBH1UNIFUUJgGVePGfhR1qyj1YETXAaH/SqAnp836/lGftUfdNcFiqbBT8L2jouQdvE9iVAoVUyDWONFa5XVYlJSjezEPT+BlmCSiVQgw65or2vBaE0Y5z1e4D/VeBmhstwJyo5C0YeZ53vdo/z19lhVjly71+K6xRb/ZbO/rbLCS8HMwmVZ7W9zeFc567b95+3uxxde/82a3/vOY+eJc+z4zkun77xzBs7QIbUPNVP7Ustdz33vDtxPq9C92jrnkbMhbvAD81mObw==</latexit>
>tixetal/<=o5kGOXA8nPw+jg58xpF0iV+df+Fc65c4dlh4JDBJAKNtMMqLdIwOTQ4OGxReUn+Vexdrd1nq3qVS+6LLjfIyWlZGbSFISWRvZGKYWSswTsoY2QALRDSIPOKiWMkUNDNJSYwXREzdn3/JuZ26ZIbTsDaJdcrTIoY7pfugK8WqgEoZY1pF5zHZCTdCBnKa1eMCLjYam2lpm20EGWlCCmmX67utOGhwg6SkA5NreffakjAkeu4VB6c6taxut/HlsiBHuYFIW6x56m+V2ogxYxCcIRDpY8bxlkmVNg98zc3csTaInUxVkk2wxMNanAnmGbCVvkkkodEMt8ShFs7Lb/92Z3lupC3Y/9WYN1tejn2nlShmbWG9OOwBXPte0up3wv3p0vXiMYxi/l0UvKJW2kmbYXayKV7BsfBjVM6xiuKdXJPRA2ljWNd+V7Xt2JExMwSNBVbciH+BAAA>"=g/Sbcz2lT7cvIVd5PuyPY0nrFy7"=46esab_1ahs tixetal<
q(x x )
t t 1
<latexit sha1_base64="eAZ87UuTmAQoJ4u19RGH5tA+bCI=">AAACC3icbVC7TgJBFJ31ifhatbSZQEywkOyiiZQkNpaYyCMBspkdZmHC7MOZu0ay0tv4KzYWGmPrD9j5N87CFgieZJIz59ybe+9xI8EVWNaPsbK6tr6xmdvKb+/s7u2bB4dNFcaSsgYNRSjbLlFM8IA1gINg7Ugy4ruCtdzRVeq37plUPAxuYRyxnk8GAfc4JaAlxyzclbo+gaHrJQ8TB/AjnvsmcGZPTh2zaJWtKfAysTNSRBnqjvnd7Yc09lkAVBClOrYVQS8hEjgVbJLvxopFhI7IgHU0DYjPVC+Z3jLBJ1rpYy+U+gWAp+p8R0J8pca+qyvTRdWil4r/eZ0YvGov4UEUAwvobJAXCwwhToPBfS4ZBTHWhFDJ9a6YDokkFHR8eR2CvXjyMmlWyvZ5uXJzUaxVszhy6BgVUAnZ6BLV0DWqowai6Am9oDf0bjwbr8aH8TkrXTGyniP0B8bXL+1hmu8=</latexit> |  
FigFiugruere24:1:TDhieffduisrieocntfeodrwgarradpahnicdarlevmerosdeeplrcoocensssiedse.r(eSdouirncet:hi[s46w1o])rk.
ThiTshpeafoprewrarpdreprsoecnestssipsrdoegfinreedssasin diffusion probabilistic models [53]. A diffusion probabilistic model
(which we will call a “diffusion model” for brevity) is a parameterized Markov chain trained using
variational inference to produce s(cid:89)aTmples matching the data afte(cid:112)r finite time. Transitions of this chain
q(x |x )= q(x |x ),q(x |x )=N(x ; 1−β x ,β I), (33)
are learned to reverse a 1d:Tiffu0sion procetsst,−w1 hichtist−a1Markovtchain thtatt−g1ratdually adds noise to the
t=1
data in the opposite direction of sampling until signal is destroyed. When the diffusion consists of
smawlhlearemthoeuvnatrsianocfeGscahuedsuslieaβn1n,.o..i,sβeT,ciatnisbesucofnfisctainetnotrtloeasrneetdthhyepesrapmarapmlientegrsc.hTahienretvrearnsesiptrioocnessstiosdceofinnedditaisonal
Gaussians too, allowing for a particularly simple neural network parameterization.
T
(cid:89)
Diffusion modelspa(rxe str)a=igph(txfor)warpd(txo de|fixn)e,pan(xd ef|fixc)ie=ntNto(xtrai;nµ, b(xut,tto),tΣhe(xbe,st)t)o,f our know(3le4d)ge,
θ 0:T T θ t−1 t θ t−1 t t−1 θ t θ t
there has been no demonstratiot=n1that they are capable of generating high quality samples. We
show that diffusion models actually are capable of generating high quality samples, sometimes
whereµ (x ,t)andΣ (x ,t)arefunctionsthatprovidethemeanandcovariancefortheGaussianandaredefined
θ t θ t
betutesirngthMaLnPtsh.e[4p62u,b4l6i1s]hed results on other types of generative models (Section 4). In addition, we
show that a certain parameterization of diffusion models reveals an equivalence with denoising
ThemodelistrainedbymaximizingthevariationallowerboundontheNLL(likeaVAE)
score matching over multiple noise levels during training and with annealed Langevin dynamics
during sampling (Section 3.2) [55, 61]. We obtainedpo(xur b)est sample quality results using this
E[−logp (x )]≤E [−log θ 0:T ]=L, (35)
parameterization(Section4.2),sowecoθnsi0derthqisequiqv(axlenc|xet)obeoneofourprimarycontributions.
1:T 0
Deswphiitcehtishdeoirnesabymopplteimqizuinaglitthye,aofuorremmeondtioenlseddMoLnPost. [h4a6v2,e4c6o1]mpetitive log likelihoods compared to other
likelihood-basedmodels(ourmodelsdo,however, haveloglikelihoodsbetterthanthelargeestimates
Sohl-Dicksteinetal. [462]providethefirstimplementationofdiffusionmodelsandapplyittothegenerationand
anninepaaliendtinigmopfiomratagnescaendsabminaprylinsegquhenacsesb,epeernforrmepinogrtweodrsetothpanroGdAuNcse,bfuotrbeetnteerrtghaynbDaBsNesd,GmSoNdseanlsdCanAdEssicnore
mattecrhmisnogfl[o1g1-l,ik5e5lih])o.odW. e find that the majority of our models’ lossless codelengths are consumed
to dHeosectraibl.e[4i6m1]pperorcpeospetithbeleDeimnoaisginegdDeiftfauislison(SPreocbtaiboinlis4tic.3M).odWele(DpDrPeMse)n,wt haicmhosirmeplriefifiesntehdetaraninailnygspisroocefssthis
pheonfo[4m62e]nboynreipnlatchineglΣanθ (gxut ,atg)ewiothfulontsrsaiynecdotmimpe-rdeespseinodne,ntacnodnswtanetssσh
t
2oIwintthheatretvheersesapmrocpelsisnagndptrroaicneindguarne of
estimatorϵ (x ,t)topredictthenoiseϵaddedtox insteadofpredictingthemeanµ (x ,t). Thevariationallower
diffusion moθdetls is a type of progressive decotding that resembles autoregθrestsive decoding along a bit
boundissimplifiedtooptimizethedifferencebetweenactualandpredictederror. Fortheestimatorϵ ,PixelCNN++
ordering that vastly generalizes what is normally possible with autoregressive modelθs.
[246]isadoptedwithself-attentionatthesmallfeaturemaps.
2 Background 56
(cid:82)
Diffusion models [53] are latent variable models of the form p (x ) := p (x )dx , where
θ 0 θ 0:T 1:T
x ,...,x are latents of the same dimensionality as the data x q(x ). The joint distribution
1 T 0 0
∼
p (x ) is called the reverse process, and it is defined as a Markov chain with learned Gaussian
θ 0:T
transitions starting at p(x ) = (x ;0,I):
T T
N
T
(cid:89)
p (x ) := p(x ) p (x x ), p (x x ) := (x ;µ (x ,t),Σ (x ,t)) (1)
θ 0:T T θ t 1 t θ t 1 t t 1 θ t θ t
− | − | N −
t=1
Whatdistinguishesdiffusionmodelsfromothertypesoflatentvariablemodelsisthattheapproximate
posterior q(x x ), called the forward process or diffusion process, is fixed to a Markov chain that
1:T 0
|
gradually adds Gaussian noise to the data according to a variance schedule β ,...,β :
1 T
T
(cid:89) (cid:112)
q(x x ) := q(x x ), q(x x ) := (x ; 1 β x ,β I) (2)
1:T 0 t t 1 t t 1 t t t 1 t
| | − | − N − −
t=1
Training is performed by optimizing the usual variational bound on negative log likelihood:
(cid:20) (cid:21) (cid:20) (cid:21)
p (x ) (cid:88) p (x x )
E [ logp θ (x 0 )] E q log θ 0:T = E q logp(x T ) log θ t − 1 | t =: L (3)
− ≤ − q(x x ) − − q(x x )
1:T 0 t t 1
| t 1 | −
≥
The forward process variances β can be learned by reparameterization [33] or held constant as
t
hyperparameters, and expressiveness of the reverse process is ensured in part by the choice of
Gaussian conditionals in p (x x ), because both processes have the same functional form when
θ t 1 t
β are small [53]. A notable p−ro | perty of the forward process is that it admits sampling x at an
t t
(cid:81)t
arbitrary timestep t in closed form: using the notation α := 1 β and α¯ := α , we have
t − t t s=1 s
q(x x ) = (x ;√α¯ x ,(1 α¯ )I) (4)
t 0 t t 0 t
| N −
2

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Nichol et al. [463] introduce the improved DDPM for better log-likelihood results. It reintroduces Σ (x ,t) as a
θ t
trainablemodelandreplacesthelinearnoisescheduleforβ withacosineschedule,whichspreadsthenoiseaddition
t
intheforwardprocessmoreevenly. Theyalsoreducethenumberofdiffusionstepstoimprovesamplingspeedwith
verylittlequalitylossbyscalingthescheduleparameters,andincreasingthemodelsizealsoincreasesperformance.
Dhariwaletal. [464]proposetheablateddiffusionmodel(ADM)withclassifierguidance(ADM-G),whichimproves
upon[463]byusingmoreattentionatdifferentscales,classconditioning,adeepermodelarchitecture,andaclassifier
toguidethegenerationprocessmoreprecisely.
Rameshetal. [465]addtextembeddingsproducedbyadecoder-onlytransformertotheexistingtimestepembedding
ofadiffusionmodeltoproducetext-conditionalimages. Imagescanbemanipulatedbasedontextbyreconstructing
imagesfromx withthediffusionmodelconditionedonnew/interpolatedtextembeddings.
T
2.20 VirtualEnvironments
Virtualenvironmentsarecomputer-simulated“graphicandreal-likemodelsofreal-lifeobjects”[5]thataresimpleto
annotatebynaturesinceobjectlocations,classes,andotherpropertiesareapparentinthesimulationsoftware. More
realisticdepictionsofvirtualobjectshavebecomepossiblebecauseoftheincreasingcomputationalprocessingpowerof
GraphicsProcessingUnits(GPUs)inrecentyears. Theyallowedvirtualenvironmentstobeadoptedforvarioustasks,
suchasautonomousdrivingorgesturerecognition. Basedon[5],wederivethreecategoriesforvirtualenvironment
usages:
GraphicModels Inthissimplescenario,single3DComputerAidedDesign(CAD)modelsorcompositionsareused
toalleviateMLmodeltrainingfor,e.g.,gesturerecognitionandobjectrecognitionfromdifferentviewpoints
orbuilding3Dmodelsfromimages.
VirtualWorlds These models are computer-simulated and emulate a complex real-world environment. They are
populatedwithmanyobjectsthatcansometimesmoveorinteractwiththeworldoreachother. Theyare
especiallypopularforgeneratingannotatedtrainingdataforautonomousdrivingsystems.
InteractiveEnvironments Theseinteractivevirtualworlds,usuallyvideogamesorsimulatorswithaninherentgoal
andwell-definedrules,areespeciallysuitableforthetrainingandbenchmarking/competitionofRLagents
becausetheyallowuserinputsanddirectlypresentaresult. Theadvantagesaretheirhighavailabilityfor
variousscenarios(e.g.,drivingsimulations,open-world,andstrategygames)andtheiroftensimpleadaptability
toresearchtasksthroughmodsupportandeditorsoftware.
Foroptimalresultswithrenderedsyntheticdataforcomputervisiontasks,Mayeretal. [466]presentseveralfindings:
Multistagetrainingondifferentdatasetsworksbetterthanmixingortrainingononedatasetalone,complexandmore
realisticlightingdoesnotnecessarilyhelp,andincorporatingflawsofarealcameraduringtrainingimprovesmodel
performance.
2.20.1 GraphicModels
Butleretal. [467]introduceMPI-Sintel,anoptimizedversionoftheopen-source3DanimatedshortfilmSintel[468]
foropticalflowevaluation. Asgroundtruth, motionvectorsforeachpixelarecomputedusingamodifiedversion
ofBlender’s[469]motionblurpipeline. Theadvantagesoverotherdatasetsforopticalflowevaluationarethelong
sequencesandmotionsandtheabilitytorenderthefilmwithvariouseffectslikemotionblur,specularreflections,and
atmosphericeffectsenabledordisabled.
Handaetal. [470]createthefirstRGB-D(RGBplusdepth)imagecollectionwithcameratrajectoryandfull3Dscene
groundtruthattachedtoeachframe. Theyprovideraytracedrenderingsoftworooms,theofficeroomandtheliving
room,viathePOVRay[471]raytracingsoftware. TheyalsoseparatelyapplyartificialnoisetotheRGBanddepth
valuestomaketheimagesmorerealistic. Thedatasetisthenusedtobenchmarkalgorithmsforvisualodometry,3D
reconstruction,andSimultaneousLocalizationandMapping(SLAM).
Suetal. [472]utilize3DmodelsrenderedontopofrealbackgroundimagestotrainCNNsforviewpointestimation.
The models are rotated and inserted at different positions in the picture for that purpose. Their “render for CNN”
approachachievesstate-of-the-artperformanceonabenchmarkdatasetatnegligiblehumancostusingexisting3D
modelrepositories.
Pengetal. [473]traindeepCNNobjectdetectorswithsyntheticimagesrenderedfromnon-photorealistic3DCAD
modelsthatarefreelyavailableontheInternettodetectnovelobjectcategoriesnotavailableintherealtrainingdata.
Theyevaluatethemodelsonrealimages,showingbetterdetectionperformancethanmodelstrainedonrealdatafroma
differentdomain.
57

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Handa et al. [474] introduce a framework to randomly generate realistic and automatically annotated 3D indoor
environmentsusing3Dobjectsfrompublicdatabases. TheSceneNetusesahierarchicalscenegeneratorthatlearns
relationships(co-occurrencefrequency)betweenobjectsfrompriorindoorscenedatasets. Inanotherwork[475],they
demonstratetheirmodel’sutilitybyusingitsrenderingsfromrandomperspectiveswithaddednoisetotrainadeep
modelfordepth-basedsemanticper-pixelsegmentation.
Shortoverviewofotherusagesofgraphicalmodels:
Approach Description Year
[476] CreationoftheTsukubaCGStereodataset,whichisacollectionofphoto-realisticrenderings 2012
of the head and lamp scene under varying conditions and camera perspectives for stereo
matchingtasktrainingandevaluation.
[477] Kinematic hand model with random initial global rotation is used to render hand gesture 2014
sequencesforhuman-computerinterfaces.
[478] Trainingofobjectdetectorswith3Dmodelrenderingscombinedwithdomainadaptationusing 2014
discriminativedecorrelationperformscomparablytomodelstrainedonrealdata(ImageNet).
[479] (Re-)Synthesisofnaturalimagesfromdifferentviewpointsaidedbystructuralinformation 2014
from3Dmodelsofthesameobjectclassalignedtoanimage.
[480] Simultaneousclass,pose,andlocationpredictionofpossibleobjectsusingadeepCNNtrained 2015
onRGB-Drenderingsofrandomlygenerated3Droomsbuiltwithintersectiondetectionand
plausibilitychecks(e.g.,sofasareusuallynearwalls).
[481] AcollectionofFlyingChairsimagesequencescombiningnaturalbackgroundimageswith 2015
renderingsof3DchairmodelsisusedtotraintheFlowNetCNNforopticalflowestimation.
[482] Usinga3Dmorphablefacemodeltocreatesynthetictrainingdataforfacerecognitionsystems 2018
reducestheamountofrealdataneededsignificantlyandimprovesperformance.
[483] Rendering video sequences of neurosurgical instrument movements from a microscope’s 2021
perspectiveinBlender[469]foropticalflowestimationbenchmarksinthisdomain.
[484] UsingBlender[469]torendersteelpieceswithdefects(e.g.,cracksinthesurfacetexture)and 2021
masksforasteeldefectdetectiontask.
2.20.2 VirtualWorlds
Sky
Building
Road
Sidewalk
Fence
Vegetation
Pole
Marking
Car
Sign
Pedestrian
Cyclist
Figure 42: The SYNTHIA data set: Image rendered from the virtual world (left), ground truth segmentation map
(middle),andcityoverview(right). (Source: [485])
Haltakovetal. [486]proposeaframeworkbuiltontopoftheopen-sourcedrivingsimulatorVDrift[487]. Themodified
softwareallowsthemtorenderrealisticsyntheticimageswithpixel-wiseobjectannotations,depth,andopticalflow
maps(movements)invariousscenarios,perspectives,anddrivingstyles. Theframeworkisthenappliedtocreatea
largeimagetrainingsetforamulti-classimagesegmentationtask.
Richteretal. [488]utilizethedetouringtechniquetogeneratesemanticlabelmapsforimagesfromclosed-source
moderncomputergames. Theyevaluatethecommunicationbetweenthegameandgraphicshardwareusingagraphics
APIwrapperlibrary,hashingrenderingresourcesliketexturesorgeometryandcreatingpersistentobjectsignaturesto
whichlabelsforurbansceneunderstandingareapplied. Thegametrainingdata,obtainedfromGrandTheftAutoV,
booststheaccuracyofsegmentationmodelsandreducestheneedforexpensivelabeledreal-worldimages.
Johnson-Robertsonetal. [489]useopen-sourcepluginsandGPUbufferdatatoextractannotatedandrealisticimages
fromGrandTheftAutoV forvehicledetectiontasks. Theyachievestate-of-the-artperformanceonrealdatawitha
modeltrainedonlyonsimulatedimages.
Rosetal. [485]introducetheSYNTHIAdataset(seeFigure42),whichprovidesasemanticallysegmentedcollection
ofimagesofurbanscenesobtainedfromtheUnitygameengine[490]. SinceSYNTHIAisintendedforautonomous
58

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
drivingtasks,itnotonlycontainsimagesfromvariousperspectivesinthevirtualworldbutalsofourvideosequences
ofavirtualcardrivingthroughtheurbansimulatedlandscape,oneforeachseason. Thevirtualcarconsistsoftwo
multi-cameras0.8metersapart,eachconsistingoffourmonocularcameraswithdepthsensors,acommoncenter,and
90-degreerotationbetweenthem. Incombinationwithrealdata,SYNTHIAcansignificantlyimprovesegmentation
modelaccuracy.
Shortoverviewofotherusagesofvirtualworlds:
Approach Description Year
[491] Assessmentoftheeffectivenessofmodelstrainedwithcomputergamesonreal-worlddatain 2016
imagesegmentationanddepthestimationtasks.Theresultsshowsimilarorbetterperformance
thanmodelstrainedonrealdata.
[492] VirtualKITTI:Alabeledvideodatasetcontainingcomputer-renderedsequencesofdriving 2016
throughrealisticvirtualworldsobtainedfromtheUnity[490]gameengine. Thevirtualworlds
arecreatedwithpositionalinformationfromtheoriginalKITTI[493]datasetandhuman
optimization.
[494] Visual perception benchmark (VIPER): More than 250,000 high-resolution video frames 2017
withannotations,forinstance,segmentation,opticalflow,objectdetection,tracking,visual
odometry,andobject-level3Dscenelayouttasksobtainedbymovingthroughtheworldofthe
videogameGrandTheftAutoV.
[495] Meta-Sim:Usingprobabilisticscenegrammarstocreateandrendervalidvirtualenvironments. 2019
Performanceimprovementsofthemethodaredemonstratedbytrainingatasknetworkonthe
syntheticdataandcomparingittoamodeltrainedonrealdata.
2.20.3 InteractiveEnvironments
Bellemareetal. [496]buildtheArcadeLearningEnvironment(ALE)ontopofanAtari2600emulatortoevaluateAI
techniqueslikeRLandplanningalgorithmsonarbitraryAtarigames,whichareusuallysplitintoatrainingandtesting
set. ALEprovidesaninterfacetothegamecontrols,screeninformation,RAM,andregistersforanAIagenttocontrol
orread. Therewardfunctionforanagentisdefinedpergamebasedonthescoredifferencebetweenframes.
Kempkaetal. [497]buildupontheideaof[496],where2DAtari2600gamesareusedasanevaluationplatformfor
RLagents,andproposeVizDoom,amorerealistic3Dgamebasedonthefirst-personshooterDoom,asaresearch
platformforvisualreinforcementlearning. TheytraincompetentbotsusingconvolutionaldeepneuralnetworksandRL
onvarioustasksandscenarios.
Sadeghi et al. [498] make deep reinforcement learning applicable to safety-critical domains such as autonomous
flightsbytraininginvirtualenvironmentsbuiltentirelywithCADmodels. TheCAD2RLmethodtrainsaRLagent
(deepCNN)onRGBimagesofamonocularcameramountedtoadroneinthevirtualenvironmenttooutputvelocity
commandsthatavoidcollisions. Theauthorsfindthatbyusinghighlyrandomizedrenderingsettings,theagent’spolicy
canbetrainedtogeneralizewelltoreal-worldapplications,whichtheydemonstratebylettingthetrainedagentflya
realdronethroughindoorenvironments.
Vinyalsetal.[499]introducetheStarCraftIILearningEnvironment(SC2LE),whichcombinesaPython-basedinterface
forthegameenginewithspecificationsforpossibleobservations,actions,andrewards. Asacomplexmulti-agent
problemwithincompleteinformation,long-termstrategies,andlargeactionspace,StarCraftprovidesadifficultclassof
problemstoevaluateRLmodelson. Theauthorstestagentsonvariousmini-games,resultinginagentbehaviorsimilar
toanoviceplayerandonthemaingame,wheretheagentscannotprogressnoticeably.
Shortoverviewofotherusagesofinteractiveenvironments:
Approach Description Year
[500] DeepMindLab: First-person3DgameframeworkbasedontheQuakeIII gameenginefor 2016
easytaskandAIdesign.
[501] TorchCraft: ProvidinganinterfacebetweentheTorchMLframeworkandreal-timestrategy 2016
game“StarCraft: BroodWar”.
[502] ProjectMalmo: AnAIexperimentationplatformforcomplexnavigation,survival,collabora- 2016
tion,andproblem-solvingtasksbuiltontopofMinecraft,apopulargamemimickingthereal
worldasacollectionofblocksandfriendlyandhostileentities(e.g.,animals,zombies).
59

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
3 ClassificationofGenerativeModels
Inthissection,weclassifythemodelswepresentedinSection2bycriteriapresentedinSection3.1. InSection3.2,we
performatrendanalysisbeforefinallypresentingaguidelineformodelselectioninSection3.13.
3.1 CriteriaforClassification
Foreachmodelpresentedinthiswork,wecollectcertaininformationwefindtobecomparableandusefulforourtrend
analysisandguidelines:
Metadata Wecollectname,releaseyear,model(sub-)category(accordingtoSection2)andcitations(accordingto
Googlescholar). Optionalentriesarepredecessors(othermodelsthatarethefoundationforthismodel)and
combinations,whichdescribethecategoriesaproposedmodelcombines(e.g.,aGANcancombineaCNN
generatorwithaRNNdiscriminator).
DataStructure Determinesifthesize/amountofsamplesofthedatageneratedbythemodelislimited,forexample,
animagewithastaticresolutionorafixed-lengthvideo,or(theoretically)infinite,whichisoftenrequiredfor
processingarbitrarily-sizedsequences.
DataType Typeofthedatageneratedbythemodel,forexample,naturallanguagetext,timeseries,music,orimages.
SamplingRequirements Thedatagenerationprocessofamodelcanbeunconditionalorconditional,whichmeans
aninputisrequiredbasedonwhichsyntheticdataisgenerated,orboth(seeFigure43). Ifaninputisaccepted,
wealsocapturethetypesofinputthatthemodelaccepts.
SamplingProcess Describeswhetherasampleisgeneratedin“onego”oriterativelyrefinedbythemodel.
TrainingProcess Describeshowthegenerativemodelistrainedandisdescribedbytwoaspects,inspiredby[503]:
LossType Thelossfunction(s)thatis/areusedtooptimizethemodel.
Optimization Additionalpenalizationofthemodelormodificationofthelossfunctiontoimproveresults.
DataSets Thedatasetsusedtotrainandevaluatethemodels.
ModelPerformance Comparingdifferentmodelsiscomplicatedbecausenocommonlyusedperformancemeasure
exists, andmanyproposedmeasuresonlyworkforspecificdatatypesordomains(e.g., musiccannotbe
evaluated in the same way as natural language). To work around this issue, we collect the performance
predecessors,thatis,thelistofoutperformedmodels,fromtheevaluationsectionoftherespectivepaper,if
available.
Privacy Showswhetherthegenerateddataisconsidereddifferentiallyprivateorprivatebyanothercriteriondefinedby
therespectiveauthors.
this small bird has a pink this magnificent fellow is
breast and crown, and black almost all black with a red
primaries and secondaries. crest, and white cheek patch.
(a)Image-to-imagetranslation(Source:[335]) (b)Text-to-imagetranslation(Source:[3])
Figure43: ExamplesofGANsbeingappliedtotranslativetasks.
3.2 DataEvaluationandTrendAnalysis
ThissectionpresentsthefindingsfromoursurveyofexistingSDGliterature. Inthefollowingsubsectionsthatbuildon
oneanother,weinvestigatethecriteriaproposedinSection3.1beforeconcluding.
3.3 Metadata
First,welookatthemetadatafromour417models. InFigure44,weshowthenumberofpapersgroupedbymodel
categoryweevaluatedforeachyear. Wefocusprimarilyonmodelsproposedinthelasttenyears,sothedatastartingin
60

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Autoencoder DiffusionM. KDE RL
BayesianNetw. GAN MarkovChain RNN
BoltzmannM. GMM NADE SparseCoding
CNN GMMN Norm.Flow Transformer
Copula GeneticAlg. PPGN VirtualEnv.
50
0
8991 0002 4002 6002 7002 8002 9002 0102 1102 2102 3102 4102 5102 6102 7102 8102 9102 0202 1202 2202
1.0
0.5
0.0
Figure44: Total(top)andnormalized(bottom)amountofmodelswepresentinourworkgroupedbyyearandmodel
category.
2012isprimarilyrelevant. GANs,RNNs,autoencoders(especiallyVAEs),virtualenvironments,andCNNsexperience
highusagethroughouttheyearsintheliteratureweevaluated,withGANsquicklysurpassingtheotherapproaches
sincetheirfirstproposalin2014[238]. TheusageofMarkovchainmodelsandBoltzmannmachinesdeclinedoverthe
years,whileRLanddiffusionmodelsslightlygainedpopularity.
Next,inFigure45,weevaluatetheamountofGoogleScholarcitationspermodelcategory. Comparedtoothermodels
coveredbyourwork,GANshavereceivedthehighestamountofcitationsoverthelasttenyears. Inaddition,RNNs,
CNNs,andautoencodersoftenreceivecomparableattention.
InFigure46,weevaluatewhicharchitecturesandconceptsourmodelsborrowfromothermodeltypes. Themodels
oftenusedassubmodelsaccordingtoFigure46aareCNNs,followedbyRNNsandautoencoders. InFigure46b,we
alsoshowthatsomeapparentassumptionsareconfirmed:
• GANsandtheverysimilarGMMNsoftenuseautoencoders,especiallytheirdecoders,asgenerativenetworks.
• 70%ofourRLmodelsuseRNNs,whicharesuitableforguidancebyrewardfunctionsduetotheirsequential
datagenerationprocess. RLisalsoappliedtoGANandCNNtraining.
• AutoencodersoftenincorporateRNNsandCNNsastheirencodersanddecoders.
• Diffusionmodels,GANsandnormalizingflowmodelsheavilyutilizeCNNs. ThisisbecausemanyGAN
models are based on the CNN-based DCGAN [267], and diffusion models are also mostly related to the
CNN-basedDDPM[461],whichisillustratedinFigure47.
Finally,wediscussthepredecessorsclassofourmetadata. InFigure47,webuildagraphofallpredecessorconnections
fornotablemodelcategories.WeobservethatespeciallyGANsandRNNsarestronglyinterconnected.Forautoencoders,
weonlyfoundstrongrelationsbetweenVAEmodels. Fourofthefivediffusionmodelswepresentedsignificantly
dependoneachother,whilethefifthmodelisextendedfortext-conditionaltasksand,therefore,considerablychanged.
3.4 DataStructure
InFigure48,wediscussthedatamodelingcapabilitiesofdifferentmodeltypes. Asexpected,sequence-basedmodels
suchasMarkovchains,RNNs,andtransformersaremainlyappliedtogeneratearbitrarily-sizeddata. Autoencodersand
61

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Autoencoder DiffusionM. KDE RL
BayesianNetw. GAN MarkovChain RNN
BoltzmannM. GMM NADE SparseCoding
CNN GMMN Norm.Flow Transformer
Copula GeneticAlg. PPGN VirtualEnv.
104
103
102
101
100
2012 2014 2016 2018 2020 2022
Figure45: GoogleScholarcitationsfordifferentmodelcategoriesoverthelasttenyearsonalogarithmicscale. For
betterreadability,weapplya[−0.4,0.4]offsettothepoints’yearvalueintheorderoftheirlegendappearance(topto
bottom,lefttoright). ThenumberswerelastobtainedDate.
GANsarebasedinitiallyonneuralnetworkarchitectureswithfixedinputandoutputsizesbutcanprocesssequences
byadoptingRNNs. ThesecorrelationsareeasytoobservebycomparingtheRNNconnectionsinFigure46btoour
findingsinthissection. RL,whichalsoheavilyreliesonRNNs,workswellforunlimiteddatalengthsaswell,alsodue
totherewardfunctionbeingapowerfultooltolearnandimproveduringthegenerationprocess. ModernBoltzmann
machinesliketheTRBMarealsostronglyrelatedtoRNNs,makingthemnoticeableinourdatastructureevaluation.
3.5 DataTypes
Weidentifyseveraldatatypesinourresearch,ofwhichmultipleareoftenusedbyasinglemodel. Wecategorizethem
asfollows:
Audio Representsrawwaveformaudio. Duetothehighsamplingraterequiredtoproducenatural-soundingaudio,
thisdatatypeusuallyrequirescomplexmodelsandthoroughtrainingtoproducegoodresults. Wefurther
differentiate between music and speech generation due to their difference in complexity (e.g., note and
instrumentvs. text,speaker,andcharactertransitions).
Image Describesclassictwo-dimensionalbitmaps,usuallywithRGBorgrayscalepixelvaluestowhichwereferas
naturalimages. Binaryimagesaresimplifiedversionswherepixelscaneitherbeonoroff(blackandwhite).
Segmentationmasksdescribeimageswherepixelsareofaparticularclassinsteadofcolor. Imageswithmore
informationencapsulateotherpixelvaluesbesidescolor,forexample,depthinRGB-DimagesorHSIs.
Text Thisclassdescribesasequenceofcharacters. Wedifferentiatebetweennaturallanguage,asspokenbyhumans,
andtextrepresentationsthatencodeotherdatatypes,forexample,SMILESstrings[112]formolecules.
TimeSeries Sequencesofone(univariate)ormore(multivariate)variablevaluesthathavetobedeterminedforeach
step. Themorepotentiallyinterdependentvariableshavetobespecified,themorecomplexthetaskbecomes.
Weadditionallydefinesymbolicmusicasanadditionalcategorybecauseoftheconsiderableinterestinthe
topicandthecomplexconstraintsprovidedbymusictheorythatmustbeconsidered. Dependingonthetask
definition,symbolicmusiccanberegardedasaunivariateormultivariatetimeseries.
62

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
| RNN | RL NADE | GAN | CNN BoltzmannM. | Autoencoder |     |
| --- | ------- | --- | --------------- | ----------- | --- |
1
|     |     | 4   | 0   |     | 4   |
| --- | --- | --- | --- | --- | --- |
|     | 3   |     | 9   |     |     |
4
3
| 20  | 3   |     |     | 26  |     |
| --- | --- | --- | --- | --- | --- |
5
35 3
4
15
|     |     |     | 2 5 |     |     |
| --- | --- | --- | --- | --- | --- |
|     |     | 4   |     |     | 8   |
1
3 8
| Autoencoder | CNN | DiffusionM. | GAN GMMN | Norm. | Flow RL RNN |
| ----------- | --- | ----------- | -------- | ----- | ----------- |
(a)Totalamountbottommodelsborrowedfromupperones.
| RNN | RL NADE | GAN | CNN BoltzmannM. | Autoencoder |     |
| --- | ------- | --- | --------------- | ----------- | --- |
|     |         | 7   | 7               |             | 5   |
|     | 2       |     | 35              |             |     |
0
27
| 35  | 1 7 |     |     | 17    |     |
| --- | --- | --- | --- | ----- | --- |
|     |     | 6   |     | 3 745 |     |
3
5
26
0 1
|     |     | 8   | 6   |     | 7 2 |
| --- | --- | --- | --- | --- | --- |
3 2
7 3
| Autoencoder | CNN | DiffusionM. | GAN GMMN | Norm. | Flow RL RNN |
| ----------- | --- | ----------- | -------- | ----- | ----------- |
(b)Normalized(in%,roundeddown)bythenumberofmodelsofbottommodelcategoriesthatusetheuppermodels.
Figure46: Weighteddependencygraphformodelcompositions. Thebottommodelsrelyonsubmodels(e.g.,encoders
anddecoders)fromtheuppercategories. Theedges’sizeandlabelsdenotetheamountorpercentageofmodelsthatuse
therespectivesubmodel. Weomittededgeswithlessthanthreetotalusagesforreadability.
GraphsandMolecules Graphsarecollectionsofnodeswithconnections(edges)betweenthem. Nodesandedgescan
haveadditionalpropertiesandvaluesassignedtothem. Theyareusuallyrepresentedbyadjacencymatrices
ortimeseriesofnodeandedgecreations. Manypresentedworksconsidermoleculesasasubsetofgraphs,
whereatomsarethenodesconnectedinaspecificway,andtheyareoftenrepresentedasSMILES[112]text
representationsinadditiontotherepresentationabovetypes.
TabularData We consider tabular data to be tuples, sequences of tuples, or matrices containing categorical and
numericalvalues. Besidesgeneratingtables,itisoftenusedtoprovideadditionalinformationtoanotherdata
type. Virtualenvironmentsuseittoprovide,forexample,emulatororgameinformation.
Video Asequenceofimagesasdefinedabove.
Figure49showsthatnaturalimagegenerationisthedatatypeofmostoverallimportance. RNNsarepredominantly
appliedtosequentialarbitrary-lengthdomainslikenaturallanguagetextandsymbolicmusic. Duetotheirflexible
architecture,autoencodersandGANsareappliedtoalmostalldatatypes.
Figure50illustratesthatsomemodeltypesarelimitedtospecificdatatypes: Boltzmannmachinesareexclusively
appliedtotimeseries,video,andimagedata. CNNsmainlyfocusonimagesandotherhigh-dimensionalformatslike
waveformaudio. Virtualenvironmentsareexclusivelyappliedtovisualdataandprovideadditionalinformation. RL
putsitselfforwardfordomainssuitedforsequentialgeneration.
3.6 SamplingRequirements
InFigure51,wecomparethemodels’relianceonadditionalinformation. Geneticalgorithms,PPGNs,sparsecoding
models, and CNNs that we covered can always be conditioned on additional information to guide the generation
process. Boltzmannmachines,RNNs,transformers,RL,Markovchains,diffusionmodels,GANs,andautoencoders
63

| ComprehensiveExplorationofSyntheticDataGeneration: |                 |       |     |     |     | ASurvey |     |     |     |     |
| -------------------------------------------------- | --------------- | ----- | --- | --- | --- | ------- | --- | --- | --- | --- |
| 2014 [                                             | 35 3 ] [ 2 38 ] | [367] |     |     |     |         |     |     |     |     |
c G A N G A N
| 2015 [ A 4 | A 21 E ] D [ C 2 G 67 A ] | N Ca [3 tG 68 A ] N |              |                    |                              |                           |      |              |     |     |
| ---------- | ------------------------- | ------------------- | ------------ | ------------------ | ---------------------------- | ------------------------- | ---- | ------------ | --- | --- |
| [3         | 6 9 ] [3 7                | 0 ] [ 27 2]         | [ 35 5 ]     | [3 57 ] [ 2 7 7]   | [ 2 8 4 ]                    | M [ 2 o 7 d 3 e ]         |      |              |     |     |
| 2016 Ic    | G A N A L                 | G M A N             | i G A N      | GA W W N C o G A N | [356] Im p r o v             | ed R e g .                |      |              |     |     |
|            | C G A                     | N                   |              |                    | G A N                        | G A N                     |      |              |     |     |
| [3         | 7 1 ] [ 4 1 8]            | [ 1 0 1 ]           |              |                    |                              |                           |      |              |     |     |
| 2016 V     | G A N B i G A             | N In f o G A N      |              |                    |                              |                           |      |              |     |     |
| 2017       | [ 3 58 ] [ 4              | 25 ] [ 2 70 ]       | [ 3 0 1 ]    | [ 3 7 3] [309]     | Im [ p 2 r 8 o 6 v ] ed [3 6 | 2 ] P [ 3 r o 0 g 3 r ] . |      | [1 6 6 ]     |     |     |
| St         | a rG A N dr u             | G A N C A N         | M i d i N et | S e G A N          | W G A N AC - G               | A N G A N                 | 2012 | RNN - N A DE |     |     |
[ 3 8 7 ] [ 3 5 9 ]
| 2017      | [ 2 98 ] B i c    | y c le C y c le        | [3 0 0 ]    | [ 3 7 7 ] [      | 3 8 4] [388]           |       | 2013 | [157]      |             |     |
| --------- | ----------------- | ---------------------- | ----------- | ---------------- | ---------------------- | ----- | ---- | ---------- | ----------- | --- |
| Ve        | e G A N G         | A N G A N              | me d G A N  | Du a l G A N V   | i G A N                |       |      |            |             |     |
|           | [ 2 97            | ]                      | [           | 4 23 ] [ 3 3 5 ] |                        |       |      |            |             |     |
| 2017 B [2 | G 9 A 9 N ] T e m | p . G [ o 3 G 0 A 5] N | [386] W     | A E p i x 2 p ix | A [2 R 9 A 1 E ] [424] |       | 2014 | [ 17 7]    |             |     |
|           | G A               | N                      | G           | A N              |                        |       |      | RN N -D BN |             |     |
|           | [ 2 9 3 ] [ 3     | 9 0 ] [ 3 7 8 ]        | [ 2 92 ]    | [ 2 8 8] [2      | 8 5] [ 3 6 0 ]         |       |      | [ 1 6 1 ]  | [ 1 8 8 ]   |     |
| 2017 F    | is h e r Sp li    | tt in g S t e g a n    | . M c G A N | L S G A N W      | G A N C a u s a l      | [416] | 2015 | a li g n   | [190] D B N |     |
|           | G A N G           | A N G A N              |             |                  | G A N                  |       |      | D R A W    | L S T M     |     |
[389]
|      | C o n d . [426] |     |           |                  |             |     |      | [ 2 04 ]   | [ 1 6 2]                 |     |
| ---- | --------------- | --- | --------- | ---------------- | ----------- | --- | ---- | ---------- | ------------------------ | --- |
| 2017 | C y c l e       |     |           |                  |             |     | 2016 | S a m p le | [194] No t e -R NN [206] |     |
|      | G A N           |     |           |                  |             |     |      | R N N      |                          |     |
|      |                 |     | [ 3 1 2 ] | [ 2 7 1 ] [3 9 6 | ] [ 3 1 7 ] |     |      | [ 2 2 0 ]  |                          |     |
2018 [3 9 3] [401] [3 2 4] M u s e W a v e G A N C o n d . t a b l e [391] [ 3 2 9 ] T P - L S T M - [ 2 1 5 ] [ 2 0 7 ] [ 2 10 ]
TA G A N M G A N G A N Sp e c G A N P G G A N G A N Sink h o r n GAN 2017 N A D E Se T q u u t e o n r ce Ch a r 2 W av D A C [211]
B A L S T M
[ 3 1 3 ]
2018 [3 20 ] [3 27 ] [322] C a p s u le 2018 [221] [ 2 22 ] [2 2 5 ] [ 2 2 6] Ta [ c 2 o 2 t 7 r ] on
| CT      | -G A N SN -G | A N            | G A N     |               |                    |                |      | G N N          | D e e p J Gra p h R NN | 2   |
| ------- | ------------ | -------------- | --------- | ------------- | ------------------ | -------------- | ---- | -------------- | ---------------------- | --- |
|         | [4 03 ] [ 3  | 3 6 ] [ 4 2 0] | [ 3 3 0 ] | [ 4 0 2 ] [ 3 | 65 ] [ 3 3 8 ]     | [3 61 ]        |      | [ 2 3 1 ]      |                        |     |
| 2019 LG | G A N m      | e d B i g      | S t y l e | G A N Bi g    | G A N Au t o G A N | [366] SA G A N | 2019 | Mo l e c u lar | [2 2 9 ]               |     |
|         | W G          | A N B i G A N  | G A N     | s y n t h     |                    |                |      | R N N          | G R A N                |     |
|         | [4 0 7 ]     |                |           |               |                    |                |      |                | (b)RNNs.               |     |
2019 COC O - G AN
[ 4 0 9 ]
| 2020  | [ 3 4 6 ]     | [348] [ 3 4 | 7 ] [344] | [343] [ S 3 t 4 y 1 le ] | M o l H   | [ 3 e 4 a 2 l t ] h |     |     |     |     |
| ----- | ------------- | ----------- | --------- | ------------------------ | --------- | ------------------- | --- | --- | --- | --- |
| Adver | s a r ia lNAS | CO T - G    | A N       | G A N 2                  | C y c l e | G A N               |     |     |     |     |
G A N
| 2021 [412] | [ 3 5 1 ]        | [350] | [ 4 1 7]     |     |     |     |     |     |     |     |
| ---------- | ---------------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|            | Pul s e 2 P ulse |       | Tra n s G AN |     |     |     |     |     |     |     |
2022 TT [ S 3 - 5 G 2 A ] N
(a)GANs.
2013 [9 6 ]
V A E
2015 [107]
|     |     |            |     |     |     |     |      | [                 | 1 0 0]                  |       |
| --- | --- | ---------- | --- | --- | --- | --- | ---- | ----------------- | ----------------------- | ----- |
|     |     | 2015 [462] |     |     |     |     | 2016 | [111] β           | - V A E                 |       |
|     |     | 2020 [4 6  | 1 ] |     |     |     |      | [ 1 16 ]          | [ 1 2 1 ]               |       |
|     |     | D D P      | M   |     |     |     | 2017 | Gr V a m A E m ar | [117] S R k N e t N c h | [122] |
[ 4 6 3 ]
|     |     | 2021 Im p | r o v ed [4 | 6 4 ]  |     |     | 2018 | [124] | [1 2 5 ] [ 1 2 6 ]     |     |
| --- | --- | --------- | ----------- | ------ | --- | --- | ---- | ----- | ---------------------- | --- |
|     |     | D D       | P M AD M    | - G /U |     |     |      | Gra   | p h V AE Mu s i c V AE |     |
(c)Diffusionmodels.
2019 [ 1 35 ]
T G V A E
2020 MP [1 G 4 V 0 A ] E
(d)Autoencoders.
Figure47: Inheritancegraphsofthemodeltypesforwhichweacquiredasignificantamountofdatainthepredecessors
sectionofthemetadata. Weomitmodelswithoutdocumentededges,andsomeyearsarespreadacrossmultiplerowsto
accommodatewidthlimitations.
64

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
| Arbitrarysize |     |     |     |     |     | Limitedsize |
| ------------- | --- | --- | --- | --- | --- | ----------- |
1.0
0.8
0.6
0.4
0.2
0.0
|                           | NNC                | NAG         | MMG              |                      | LR        |                              |
| ------------------------- | ------------------ | ----------- | ---------------- | -------------------- | --------- | ---------------------------- |
| redocneotuA .wteNnaiseyaB | .MnnamztloB alupoC | .MnoisuffiD | NMMG .glAciteneG | EDK niahCvokraM EDAN | wolF NGPP | NNR gnidoCesrapS remrofsnarT |
.vnElautriV
.mroN
| Figure48:     | Fractionofdatastructuresdifferenttypesofmodelsputout. |     |     |     |                          |     |
| ------------- | ----------------------------------------------------- | --- | --- | --- | ------------------------ | --- |
| Audio(Music)  |                                                       |     |     |     | Text(NaturalLanguage)    |     |
| Audio(Speech) |                                                       |     |     |     | Text(Representation)     |     |
| Graph         |                                                       |     |     |     | TimeSeries(Univariate)   |     |
| Image(Binary) |                                                       |     |     |     | TimeSeries(Multivariate) |     |
Image(MoreInformation)
TimeSeries(SymbolicMusic)
| Image(Natural)          |     |     |     |     | TabularData |     |
| ----------------------- | --- | --- | --- | --- | ----------- | --- |
| Image(SegmentationMask) |     |     |     |     | Video       |     |
Molecule
1.00
0.75
0.50
0.25
0.00
| redocneotuA   | NNC alupoC  | .MnoisuffiD NAG | MMG NMMG .glAciteneG | EDK EDAN    | wolF NGPP LR | NNR remrofsnarT          |
| ------------- | ----------- | --------------- | -------------------- | ----------- | ------------ | ------------------------ |
| .wteNnaiseyaB | .MnnamztloB |                 |                      | niahCvokraM |              | gnidoCesrapS .vnElautriV |
.mroN
Figure49: Fractionofdatatypeusagespermodelcategory.
arealsoveryflexibleandoftensupportconditionalgeneration. Theothermodeltypesaremainlyusedforunconditional
generation;theyonlyrequirerandomnoiseasinputorduringthegenerationprocess.
65

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
redocneotuA .wteNnaiseyaB .MnnamztloB NNC alupoC .MnoisuffiD NAG MMG NMMG .glAciteneG EDK niahCvokraM EDAN wolF.mroN NGPP LR NNR gnidoCesrapS remrofsnarT .vnElautriV
100
Audio(Music) 2 0 0 6 0 0 1 0 0 0 0 0 0 0 0 0 4 0 17 0
Audio(Speech) 4 0 0 12 0 0 1 33 12 0 0 0 25 0 0 0 8 0 0 0
Graph 14 0 0 0 0 0 4 0 0 0 0 0 0 25 0 9 9 0 17 0
80
Image(Binary) 14 0 17 0 0 0 3 0 0 0 0 0 75 0 0 0 1 0 0 0
Image(MoreInformation) 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 28
Image(Natural) 42 0 67 88 33 100 62 67 75 0 0 0 25 50 100 18 9 100 33 76
60
Image(SegmentationMask) 0 0 0 0 0 0 6 0 0 0 0 0 0 0 0 9 0 0 0 34
Molecule 11 0 0 0 0 0 4 0 0 0 0 0 0 12 0 27 5 0 0 0
Text(NaturalLanguage) 11 0 0 0 0 0 5 0 0 0 0 25 0 0 0 27 32 0 50 0
40
Text(Representation) 11 0 0 0 0 0 2 0 0 0 0 0 0 0 0 18 3 0 0 0
TimeSeries(Univariate) 0 0 0 0 0 20 0 0 0 0 100 17 0 12 0 0 3 0 0 0
TimeSeries(Multivariate) 12 0 25 0 33 0 7 0 12 0 0 0 0 12 0 9 6 50 0 0 20
TimeSeries(SymbolicMusic) 9 14 25 0 0 0 3 0 0 67 0 58 0 0 0 18 41 0 17 0
TabularData 16 86 0 0 33 0 11 0 12 33 0 0 50 0 0 0 0 0 0 24
Video 4 0 42 6 0 0 3 0 0 0 0 0 0 0 0 0 3 0 0 31 0
Proportionofworksprovidingdatatype[in%]
Figure50: Heatmapshowcasingthedataoutputprovidedbydifferenttypesofmodels.
redocneotuA .wteNnaiseyaB .MnnamztloB NNC alupoC .MnoisuffiD NAG MMG NMMG .glAciteneG EDK niahCvokraM EDAN wolF
.mroN
NGPP LR NNR gnidoCesrapS remrofsnarT
both conditional unconditional
1.0
0.8
0.6
0.4
0.2
0.0
Figure51: Fractionofmodelsconditionedoninputdatapermodelcategory.
InFigure52,weprovideamoredetailedoverviewoftherelianceofspecificmodeltypesoncertainconditioninginput
types. WeextendthedatatypesproposedinSection3.5withthreenewentries:
ModelConstraints Constraintsimposedonthemodelbytheuser,forexample,staticgenerationrulesfrommusic
theoryorpositionalconstraintsthatrequireaspecificstepinasequencetohaveaparticularvalue.
ClassLabels Aone-hotvectororembeddingthatspecifiescertainaspectsthegenerateddatashouldhave. Thiscould
behairorskincolorforhumanfaceimagegeneration.
66

| ComprehensiveExplorationofSyntheticDataGeneration: |               |             |     |       |     | ASurvey |     |       |     |     |
| -------------------------------------------------- | ------------- | ----------- | --- | ----- | --- | ------- | --- | ----- | --- | --- |
|                                                    | Audio(Speech) |             | 3   | 0 0 0 | 0 0 | 1 0 0   | 0 0 | 0 0 0 | 0 4 | 0 0 |
|                                                    |               | Coordinates | 0   | 0 0 0 | 0 0 | 1 0 0   | 0 0 | 0 0 0 | 0 0 | 0 0 |
Proportionofworksacceptingdatatype[in%]
|     |     | Graph | 0   | 0 0 0 | 0 0 | 3 0 0 | 0 0 | 0 0 0 | 0 0 | 0 0 |
| --- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | --- |
100
|                         | Image(Natural)   |          | 38  | 0 10 71 | 0 75 | 41 0 0  | 0 0  | 100 0 0 | 25 24 | 100 25 |
| ----------------------- | ---------------- | -------- | --- | ------- | ---- | ------- | ---- | ------- | ----- | ------ |
| Image(SegmentationMask) |                  |          | 0   | 0 0 6   | 0 0  | 13 0 0  | 0 0  | 0 0 0   | 0 0   | 0 0    |
|                         | ModelConstraints |          |     |         |      |         |      |         |       | 80     |
|                         |                  |          | 3   | 0 0 0   | 0 0  | 0 0 0   | 0 40 | 0 0 0   | 0 7   | 0 0    |
|                         |                  | Molecule | 6   | 0 0 0   | 0 0  | 2 0 0   | 0 0  | 0 0 0   | 12 0  | 0 0    |
| Text(NaturalLanguage)   |                  |          | 9   | 0 0 18  | 0 25 | 9 100 0 | 0 20 | 0 0 50  | 25 22 | 0 25   |
60
|                          | Text(Representation) |     | 3   | 0 0 0  | 0 0 | 0 0 0 | 0 0  | 0 0 0  | 0 2 | 0 0 |
| ------------------------ | -------------------- | --- | --- | ------ | --- | ----- | ---- | ------ | --- | --- |
| TimeSeries(Univariate)   |                      |     | 0   | 0 0 0  | 0 0 | 0 0 0 | 0 0  | 0 0 0  | 0 2 | 0 0 |
| TimeSeries(Multivariate) |                      |     |     |        |     |       |      |        |     | 40  |
|                          |                      |     | 0   | 0 10 0 | 0 0 | 0 0 0 | 0 10 | 0 33 0 | 0 6 | 0 0 |
TimeSeries(SymbolicMusic) 0 50 20 0 0 0 2 0 0 67 40 0 0 0 0 35 0 25
|     |     | TabularData | 6   | 0 0 6 | 0 0 | 3 0 0 | 33 0 | 0 0 0 | 0 2 | 0 0 |
| --- | --- | ----------- | --- | ----- | --- | ----- | ---- | ----- | --- | --- |
20
|     |     | Video | 3   | 0 50 12 | 0 0 | 3 0 0 | 0 0 | 0 0 0 | 0 15 | 0 25 |
| --- | --- | ----- | --- | ------- | --- | ----- | --- | ----- | ---- | ---- |
|     |     | Any   | 0   | 0 0 0   | 0 0 | 1 0 0 | 0 0 | 0 0 0 | 0 0  | 0 0  |
0
|     |                 | ClassLabels | 56  | 50 20 29 | 100 25 | 45 0 100 | 0 0 | 0 33 100 | 12 9 | 0 25 |
| --- | --------------- | ----------- | --- | -------- | ------ | -------- | --- | -------- | ---- | ---- |
|     | RewardFunctions |             | 0   | 0 0 0    | 0 0    | 0 0 0    | 0 0 | 0 33 0   | 50 0 | 0 0  |
Staticfeatures
|     |     |     | 0           | 0 0 0                     | 0 0                | 1 0 0        | 0 0                     | 0 0 0     | 0 0    | 0 0                      |
| --- | --- | --- | ----------- | ------------------------- | ------------------ | ------------ | ----------------------- | --------- | ------ | ------------------------ |
|     |     |     |             | NNC                       | alupoC .MnoisuffiD | NAG MMG NMMG |                         | EDAN NGPP | LR NNR |                          |
|     |     |     | redocneotuA | .wteNnaiseyaB .MnnamztloB |                    |              | .glAciteneG niahCvokraM | wolF.mroN |        | gnidoCesrapS remrofsnarT |
Figure52: Heatmapshowcasingthedatatypesacceptedbydifferenttypesofmodels.
RewardFunctions User-definedfunctionsthatprovideaspecificvaluetobeoptimizedbythemodelinadditiontoits
defaulttargets. Forexample,ageneratedmoleculeshouldhaveaparticularchemicalproperty.
Themostoftenusedsamplingrequirementsacrossallmodeltypesareimagesandclasslabels,followedbynatural
languagetextandmusic. Duetotheirsimplestructure,Markovchainsaresuitableforapplyingmodelconstraints. In
contrast,RLmodelsarepredestinedforusingrewardfunctionsduetotheirflexiblepolicylearningarchitecture. In
thepresentedliterature,wefindsegmentationmaskstobeexclusivelyusedbyCNNsandGANs,whichalsooftenuse
CNNsasgenerators(seeSection3.3).
3.7 SamplingProcess
Wefoundtwotypesofsamplingprocessestoberelevant:Determiningthevaluesofasampleorsequenceofsamples“in
onego”(oneshot)anditerativelyrefiningthesamplevaluesaspecificnumberofstepsoruntilacriterionisreached. We
presentourfindingsinFigure53,whereweshowthatmostmodelsuseone-shotsampling. PPGNs,geneticalgorithms
anddiffusionmodelsalwaysiterativelysampledatabecauseoftheirarchitecture. Othermodelslikeautoencoders,
CNNs,Markovchains(especiallyHMMs),NADEs,RL,andRNNsarealsosuitabletobeappliedmultipletimesoras
deeparchitecturesconsistingofmultiplesubmodelstothedatatorefinetheresults,butlessoftenusedinthatway.
3.8 TrainingProcess
InFigure54,weprovideacombinedoverviewofdifferentlossesandoptimizationtechniquesusedtotrainandimprove
generativemodels:
MMDLoss/DataDistributionMatching Comparisonofoveralldatastatisticsbetweensetsofrealandgenerated
samples. GMMNsusetheMMDmetricastheirmaintrainingobjective. ManyGANsusetheWasserstein
distanceinadditiontotheadversariallosstopreventmodecollapse.
AdversarialLoss/ClassificationError/AuxiliaryClassifier Describesthecompetitionofagenerativemodelagainst
aclassifiermodelthatjudgeswhetheritsinputisrealorfake(adversarialloss,thefoundationofGANs)or
67

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
redocneotuA .wteNnaiseyaB .MnnamztloB NNC alupoC .MnoisuffiD NAG MMG NMMG .glAciteneG EDK niahCvokraM EDAN wolF
.mroN
NGPP LR NNR gnidoCesrapS remrofsnarT .vnElautriV
Iterative OneShot
1.0
0.8
0.6
0.4
0.2
0.0
Figure53: Fractionofmodelsutilizingaspecificsamplingprocess.
theprobabilitiesthattheinputbelongstoaspecificclass. Classifiersareoftenusedbesidesotherlosstypes
(auxiliary)orinPPGNsastheprimarytrainingobjective,whichcanbeconsideredamorepowerfulGAN
discriminator.
DataLikelihood Asimplisticevaluationapproachofthemodelperformanceisoftenusedbyoldermodels,lettingthe
modelassignagenerationprobabilitytorealtestdata.
ReconstructionError/CycleConsistencyLoss Reconstructionerroristhefoundationofautoencoders,Boltzmann
machines, andthemoregeneralsparsecodingmodelthattakesdataasinput, convertsittoasmallrepre-
sentation,andthenaimstoreconstructthedataasaccuratelyaspossible. Theaccuracyismeasuredbythe
errormetric,whichisoftenameanabsoluteormeansquarederror. Cycleconsistencyloss,introducedby
CycleGAN[359],allowsaGANtotrainbasedonreconstructionlossbytrainingconditionalgeneratorsand
discriminatorsforbothdirectionsinanunpairedimagetranslationtask.
Reward/ScoreFunctionandContentFeatureEvaluation Evaluationofspecificaspectsofthegenerateddatafor
modeltrainingandguidance. Thisisespeciallyrelevantforpolicy-learningmodelslikeRL.
Rule-BasedLoss Hardconstraintsimposedonthegenerateddataandmodel,implementedbyhumans. Itisusedto
forceRNNstocomplywiththebasicrulesofmusictheory.
LimitationsandAdaptation The training process of many models is significantly modified. Model training with
gradientdescentisoftenimprovedandacceleratedbyusingadynamicallyadaptedlearningrateorrestricting
the gradient itself (e.g., gradient clipping, normalization, penalization). A model’s network weights or
parameterscanalsobeheavilyrestrictedbynormalization,freezing,decay,clipping,orconnectionofsomeof
them(i.e.,weightsharing). Modelsthatworkwithlatentcodesrepresentingdata(mostlyautoencoders)also
oftenimposedistributionconstraintsonthem,usuallytosimplifythesamplingofnewdata.
RankingofSamples Arankingoffakesamplesamongrealonesprovidesmoredetailedfeedbacktothegenerative
model.
Dropout Setarandomfractionofneuronsofaneuralnetworktozeroateachtrainingsteptopreventneuronsfrom
learningthesamefeatures.
EarlyStopping Stopoptimizationonthetrainingdatawhenmodelperformancestopsincreasingontheevaluation
datatopreventoverfitting.
ModeRegularization Offeringanincentivetothemodelorpenalizingitforitscoverageofdataclassesorthedata
distribution. MakesmodelsmoreresilienttoimbalanceddatasetsormodecollapseinthecaseofGANs.
NoiseInjection Addingnoisetothedataoratspecificlayersinaneuralnetwork. Forcesthemodeltogeneralizemore.
68

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
redocneotuA .wteNnaiseyaB .MnnamztloB NNC alupoC .MnoisuffiD NAG MMG NMMG .glAciteneG EDK niahCvokraM EDAN wolF.mroN NGPP LR NNR gnidoCesrapS remrofsnarT
GradientPenalty 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
MMDLoss 0 0 0 0 0 0 0 0 100 0 0 0 0 0 0 0 0 0 0
MMDloss 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
Spatialconsistencyloss 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
AdversarialLoss 2 0 0 12 0 0 98 0 25 0 0 0 0 0 0 27 3 0 0
ClassificationError 2 0 0 0 0 0 2 0 0 0 0 0 0 0 100 0 0 0 0
classificationloss 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
CycleConsistencyLoss 0 0 0 0 0 0 4 0 0 0 0 0 0 0 0 0 0 0 0
EnergyFunction 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 0 0 0
hingloss 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
hingeloss 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0
DataLikelihood 4 100 0 65100100 5 100 0 0 100100100100 0 55 92 0 100 100
policyoptimization 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 0 0 0
ReconstructionError 95 0 92 35 33 0 21 0 25 0 0 0 0 0 50 0 9 100 0
reconstructionerroradversarial 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 80
Reward/ScoreFunction 2 0 0 0 0 0 2 0 0 0 0 0 0 12 0 73 5 0 0
Rule-BasedLoss 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 4 0 0
Augmentation 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 60
DataAugmentation 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
DataDistributionMatching 0 0 0 0 0 0 19 0 0 0 0 0 0 0 0 9 0 0 0
EarlyStopping 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 0 0 0 40
EntropyRegularization 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 9 0 0 0
GradientLimitations 5 0 0 0 0 0 13 0 0 0 0 0 0 0 0 9 6 0 17
LatentCodeLimitations 75 0 0 0 0 0 7 0 0 0 0 0 0 38 50 0 5 50 0
20
LearningRateAdaptation 2 0 0 6 33 0 30 33 12 0 0 0 0 62 0 18 5 0 50
LearningRateAdaption 2 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 1 0 0
NoiseInjection 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
ProfessorForcing 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
Weight/ParameterLimitations 4 0 0 0 0 0 13 0 25 0 0 8 25 0 0 9 0 0 17
AuxiliaryClassifier 5 14 0 0 0 20 11 0 0 0 0 0 0 0 50 0 0 0 0
RankingofSamples 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
Dropout 4 0 0 12 0 0 11 0 12 0 0 0 0 0 0 9 10 0 67
EarlyStopping 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 17
ContentFeatureEvaluation 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0
gradient-clipping 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
ModeRegularization 2 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
NoiseInjection 5 14 0 0 0 0 4 0 0 0 0 0 0 0 0 0 1 0 0
PrivacyBudget 0 14 0 0 33 0 1 0 0 0 0 0 0 0 0 0 0 0 0
TeacherForcing 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 5 0 0
Proportionofworksusingloss/regularization[in%]
Figure54: Loss(above)andadditionaloptimization(belowblackline)heatmapfordifferentmodeltypes.
PrivacyBudget Usedtopreventdifferentially-privatemodelsfromdisclosingtoomuchinformationfromtheoriginal
data.
TeacherForcing AppliedtoRNNstoavoiderrorpropagationbyfeedingthecorrecttokenoftherealdatainsteadof
thefaultypredictedtokentothenextrecurrentstep.
3.9 DataSets
Commondatasetsareessentialformodeltrainingandevaluation. Theyallowresearcherstocomparetheirmodels
againstothersinameaningfulmanner. Thesedatasetsmustbecommonlyavailabletotheresearchcommunityforthat
purpose. InFigure55,weinvestigateifthegenerativemodelspresentedinthissurveyusepublicorprivatedatasets.
Wefindthat355outof388models(excludingvirtualenvironments)useatleastonepubliclyavailabledatasetfor
theirevaluation,while33donotdisclosetheirdata,ofwhichonlyfivemodelsareusedforprivacypreservation,where
restrictionsoftenapply(e.g.,healthcare). Additionally,47modelsutilizebothprivateandpublicdatasetsfortheir
evaluations. Eachpaperpresenteduses1.74datasetsonaverage.
Wefurtherpresentthemostoftenusedpublicdatasetsusedinoursurvey: MNIST[504],CIFAR-10[505],celebA
[506], ImageNet [507], LSUN (Bedrooms) [508], MS COCO [509] and SVHN [510] are collections of labeled or
69

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
cilbuP1≥ etavirPylnO ycavirP&etavirP TSINM 01-RAFIC Abelec teNegamI selarohChcaB CNIZ NUSL NHVS OCOCSM ataDesuM
332
300
200
100
76
56 58
44
33
5 19 19 19 16 15 11
0
Figure55: Amountofmodels(excludingvirtualenvironments)usingatleastonepublic,onlyprivate,andonlyprivate
datasetswhileneedingtoenforceprivacyconstraints. Additionally,wecoverthemostpopulardatasetswithmorethan
tenoccurrences.
unlabeledimages, whichalsoarethemostpopularapplicationareaofSDGasweidentifiedinSection3.5. Other
domainswherecommonlyuseddatasetsexistaremusicwiththeBachChorales[511]andMuseData3datasets,and
graphs/molecules,whereZINC[512]ispopular.
3.10 ModelPerformance
InFigure56,wevisualizethemodelsandtheirrelationshipstootherapproachesthattheyclaimtooutperformintheir
respectiveevaluations. Wecanseethatalmostallarrowsrunfromthetoptothebottom,meaningthatnewermodels
tendtooutperformolderones. Mostmodelsonlyevaluateagainstasmallnumberofotherworks(onaverage0.65ofthe
presentedapproaches),leadingtoasmallin-degreeandusuallyalsoout-degree. SomeapproacheslikeDCGAN[267]
and[111]arepopulartocompareagainst,asshownbytheirlargeout-degree. GANsareoverallmostoftencompared
against(83times),followedbyautoencoders(62times),RNNs(44times),CNNs(25times),normalizingflowmodels
(12times),Boltzmannmachines(7times),RLapproaches(7times),diffusionmodels(5times),NADEs(3times),
transformers(3times),GMMNs(2times),andPPGNs(1time).
GANs and transformers tend to outperform other model types like CNNs and autoencoders. In graph/molecule
generation domain, RNNs also hold up well. Since the resurgence of diffusion models in 2020 [461], they also
outperformGANsinunconditionalandtext-conditionalimagegeneration.
Wealsoinvestigatetheevaluationmetricsusedbythepresentedmodels: Theoverallmostcommonlyusedmetricisthe
NegativeLog-Likelihood(NLL),whichdescribestheprobabilitiesassignedtotheobservedgroundtruthbythemodel.
AsBorji[19]pointsout,alowNLLscoredoesnotnecessarilyresultinhighdataquality,andthemetricisdifficult
tocomputeforhigh-dimensionaldata. OthercommonmetricsforimagedataandGANsinparticularareInception
Score(IS)andFréchetInceptionDistance(FID),whichuseapre-trainedimageclassifiertocomparetherealandfake
datadistributions[19]. WealsooftenencounterevaluationsbyhumansusingaMOS!(MOS!)onascalefromoneto
fiveoronetotentorateseveralfeaturesoftheproduceddata. Acomprehensiveevaluationbasedonthesemetricsis
notpossible,duetomostworksusingdifferentmetricsspecializedfortheirtask,andevenifthesamemetricisused,
thedatasets(seeSection3.9)areoftendifferent.
3.11 Privacy
ManymodernapplicationsofMLareinareassuchasthehealthcaresector,wheresensitivedataofrealpersonshasto
beprocessed. Thisleadstotheproblemthatlargeamountsofdatafortrainingandevaluationofmodelsarerequired
3www.musedata.org
70

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
201 GAN [3 - 1 T 0 T ] UR
2006 D [6 B 5 N ]
2007 G [7 B 4 M ] T [ R 6 B 9] M
2008 RT [ R 70 B ] M
2009 D [6 B 0 M ]
2010 [75]
2012 C [9 A 2 E ] RNN [1 - 6 N 6 A ] DE RN [ N 15 -R 6] BM
2013 [93] [90] V [9 A 6 E ] [157] R [ N 1 A 47 D ] E FD [1 -R 69 N ] N R [ D 1 N e 7 e N 0 p ] s
2014 c [ G 35 A 3 N ] SR [2 C 4 N 4] N N [4 I 4 C 1 E ] D [ A 79 R ] N m [ - 1 R 7 N 8] N O N A [1 A / 4 d D 8 e ] E ep D [1 L 4 G 2 M ] G [9 S 4 N ] NA [1 D 49 E ] -k G D [ M 2 e 1 e M ] p [171] SRT [7 R 1 B ] M S [ T 1 O 7 R 3] N [ G 2 A 38 N ]
2014 RN [ N 17 -D 7] BN rC [3 N 0] N
2015 D [ a R 1 li 6 A g 1 n W ] [192] D [ R 9 A 7] W [185] [239] D [1 V 0 A 5 E ] [462] LA [4 P 1 G 3 A ] N [ N 15 IC 8] [190] [ A 4 A 21 E ] CS [ T 1 - 0 V 8 A ] E D [ C 2 G 67 A ] N L [ D 1 S B 8 T 8 N M ]
2015 M [4 N M 2 e 9 t D ] D [ C 1 - 0 I 2 G ] N [237] G [ M 42 M 2] N I [ W 10 A 6 E ] N L e [ a t 8 d w 1 d o ] e r r k [354] R [1 I 7 D 9 E ] [187] I S m R [ p 2 C r 4 o N 5 v ] N ed L [1 R 5 C 9 N ] Ca [3 tG 68 A ] N
2015 M [1 A 4 D 5] E
2016 [ N R 4 V 4 ea 2 P l ] [ I 2 A 8 N 1] G [2 R 8 A 3 N ] Pix [ e 1 l 1 C 5 N ] N β [ - 1 V 0 A 0] E [111] [203] [452] G [ M 27 A 2] N W [ a 2 v 2 e 8 N ] et EB [2 G 78 A ] N [242] [250] U [ G n 2 r A 6 o 9 l N l ] ed
2016 Pix [ e 1 l 1 R 5 N ] N E [ S 2 P 5 C 1] N S [ R a 2 m N 04 p N ] le D [2 R 4 C 3 N ] N R [ e e 1 t v w 9 i 7 e o ] w rk GA [3 W 57 W ] N L A o t [ R o t 1 e k N 6 n b 3 t N a i ] o ck n / C-RN [2 N 80 -G ] AN V [1 L 1 A 3 E ] Pix [1 e 1 lV 4 A ] E C [ o 2 G 7 A 7] N [356]
2016 [155] Im [ G p 2 A r 8 o 4 N v ] ed M G [ R 2 A o e 7 g d 3 N . e ] DG [4 N 3 - 4 A ] M A [ D 8 G 2] M Pix G [ e 2 a l 4 C t 9 e N d ] N [198] V [3 G 7 A 1 N ] [206] B [ i 4 G 1 A 8] N [109] In [ f 1 o 0 G 1 A ] N
2017 St [ a 3 rG 58 A ] N M [ i 3 d 0 i 1 N ] et Se [ q 2 G 95 A ] N S [ e 3 G 7 A 3] N MA [ D 38 - 3 G ] AN [309] Perf [ R o 2 N r 1 m 9 N a ] nce Si [ m 3 G 72 A ] N Im W [ p 2 G r 8 o A 6 v ] N ed AC [3 - 6 G 2 A ] N Ra [ n 2 k 8 G 9 A ] N P [4 P 3 G 5 N ] P [ G 3 r A o 0 g 3 N r ] . Ve [ e 2 G 98 A ] N
2017 B [ G i 3 c A 8 y 7 c N ] le [211] C [ G 3 y A 5 c 9 N le ] me [3 d 0 G 0 A ] N Du [ a 3 l 7 G 7 A ] N Sta [ c 4 k 1 G 4] AN [388] O [ R 4 G 54 A ] N T B P A N - [ L 2 A L 2 S S D 0 T T ] E M M - Gr [ V a 1 m A 16 E m ] ar T [ G 2 e A m 97 N p ] . Pixe [ l 2 C 4 N 6] N++
2017 DR [3 A 0 G 4 A ] N G [ o 3 G 05 A ] N [386] B [ E 2 G 87 A ] N R( [ C 3 ) 8 G 2 A ] N p [ i 3 x 3 2 5 p ] ix LR [3 -G 08 A ] N [ S 2 C 12 N ] F [ G 2 is A 9 h 3 N e ] r [453] Sp [ G 3 li A 9 tt 0 N in ] g Pixe [2 lS 5 N 3] AIL M [ c 2 G 92 A ] N
2017 L [ S 2 G 8 A 8] N [ A 30 L 7 I ] Le [ a 3 k 0 G 6 A ] N T [ G 3 r A i 8 p 1 N l ] e SR [3 G 79 A ] N M [ G 4 M A 28 N D ] W [2 G 8 A 5] N S [ G t 4 a A c 1 k 5 N e ] d
2018 co [ r 3 rG 18 A ] N T I [ m r 2 a 5 a n 8 g s ] e f. G [4 C 5 P 8 N ] Ne [3 tG 16 A ] N [437] D [2 e 2 e 5 p ] J Gra [ p 2 h 2 R 6] NN TA [3 G 9 A 3] N M [3 G 2 A 4] N JT [1 -V 2 A 7] E T M [ r 2 a u 5 n s 9 s i ] c f. [64] M [ o 3 l 1 G 5 A ] N W Sp a [ e v 2 c e 7 G G 1 A A ] N N
2018 Mo [ C 3 o 1 G 1] AN M I M m [ p 4 D r 3 - o 2 G v ] e A d N GT [3 -G 98 A ] N Ma [ s 3 k 9 G 9] AN Dis [3 t- 2 G 6 A ] N Ba [ G 3 y A 2 es 8 N i ] an Int [ r 1 o 3 V 3 A ] E [391] G [4 l 4 o 3 w ] [ S 2 P 5 N 5] Sink [ h 3 o 2 r 9 n ] GAN SD [1 - 3 V 0 A ] E
2018 Gra [1 p 2 h 5 V ] AE [ I 4 R 5 L 6] [ P 3 A 9 N 2] CT [3 -G 20 A ] N SN [3 -G 27 A ] N C [ G 1 V 29 A ] E DE [ F 8 a 3 c ] tor [257] A [8 G 5 E ] [ G 2 N 22 N ] C [ G a 3 p A 1 s 3 N u ] le FF [4 JO 45 R ] D
2019 Tim [3 e 4 G 0 A ] N Mo [ R 2 l N e 3 c 1 N u ] lar LG [4 G 03 A ] N W [ m 3 G 3 e A 6 d ] N G [2 R 2 A 9 N ] E [2 E 5 D 6 S ] T S [ r p 2 a a 6 n r 1 s s ] f e . T G [ r 2 r a 6 a n p 4 s h ] f. mu [ V 1 lt A 3 il 4 E e ] vel Mi [ s 4 c 0 -G 6] AN B [ i 4 B G 2 i A g 0] N [ G S 3 t A 3 y 0 l N e ] s [ G 4 y A 0 n 2 t N h ] Bi [ g 3 G 65 A ] N
2019 Au [ t 3 o 3 G 8 A ] N [366] SA [3 G 61 A ] N Gra [ p 4 h 4 N 6] VP Dopp [ e 3 l 3 G 9 A ] Nger COC [4 O 0 - 7 G ] AN
2020 Adver [ s 3 a 4 r 6 ia ] lNAS Gr [ a 2 p 3 h 4 G ] en [348] N [ e 1 V 3 A 7] E CO [ T 3 - 4 G 7 A ] N SM [ G 4 O A 1 O 0 N ] TH D [4 D 6 P 1 M ] [343] Me [4 d 0 G 8 A ] N Gr [ a 4 p 3 h 9 A ] F NE [ D 13 -V 8] AE G [ S 3 A t 4 y N 1 le ] 2 [141]
2021 AD [4 M 6 - 4 G ] /U Ti [ m 4 e 6 C 0] GI S [4 A 2 A 7 E ] Im D [ p 4 D r 6 P o 3 v M ] ed Four [ i 4 e 4 r 7 F ] lows Tra [ n 4 s 1 G 7] AN T [ i 8 G 6 A ]
2022 TT [ S 3 - 5 G 2 A ] N
0 5 10 15 20 25 30
Numberoftimesthem71odelwasoutperformed
Figure56: Therelationshipsbetweenmodelsandtheirperformancepredecessors. Thefillcolorindicatesthemodel
categoryasinFigure44whilethebordercolorshowshowoftenothermodelshaveoutperformedamodel.

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
redocneotuA .wteNnaiseyaB .MnnamztloB NNC alupoC .MnoisuffiD NAG MMG NMMG .glAciteneG EDK niahCvokraM EDAN wolF
.mroN
NGPP LR NNR gnidoCesrapS remrofsnarT
NoPrivacy Privacy
1.0
0.8
0.6
0.4
0.2
0.0
Figure57: Amountofmodelswithprivacyconsiderationspermodelcategoryabsolute(top)andnormalized(bottom).
)cisuM(oiduA )hceepS(oiduA hparG )yraniB(egamI )noitamrofnIeroM(egamI )larutaN(egamI )ksaMnoitatnemgeS(egamI eluceloM )egaugnaLlarutaN(txeT )noitatneserpeR(txeT )etairavinU(seireSemiT )etairavitluM(seireSemiT )cisuMcilobmyS(seireSemiT ataDralubaT oediV
NoPrivacy Privacy
1.0
0.5
0.0
Figure58: Privacyconsiderationsperoutputdatatypeabsolute(top)andnormalized(bottom).
butcannotbedisclosed. SDGcanbeasensiblesolutiontothisproblem[95],butprovingthatnosensitiveinformation
isleakedbytheSDGmodelrequiresspecialtechniquessuchasdifferentialprivacy[52].
In Figure 57, we look at our surveyed models grouped by category and evaluate whether they provide a privacy
guarantee. Usually,simplisticmodelswithlimitedlearningcapabilities,suchasBNs,Markovchains,andcopulas,are
usedtogenerateprivatedata. Thesemodelshavetheadvantagethattheycanbeinspectedandmodifiedbyhumansand
withsimpledistributionmodificationsornoiseinjection. Thus,itbecomesdifficulttodetermineandextractinformation
fromrealorpersonaldata. Morecomplexneuralnetworkmodelsareseldomused,whichislikelybecausetheylackthe
advantagesaboveandlearnlotsofdetailsabouttheirtrainingdata. Thatis,tomakemodelsmoreprivacy-preserving,
therealismand,ultimately,theutilityofthedataisreduced[317]. GANs,however,areanexception: Theyhavethe
72

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
advantagethattheirgeneratorneverseestherealtrainingdata,anditisdemonstratedthatwiththoughtfuldesignofthe
lossfunctionandthemodelarchitecture,privacyguaranteesforthesemodelscanbegiven[317].
InFigure58,weevaluatethetypesofprivatedataprovidedbyourpresentedmodels. Themostuseddatatypeistabular
data,whichencapsulatesEHRsandmostotherpersonalinformationoftenencounteredintherealworld. Theonlyother
datatypesweencounteredweregraphsandtimeseries,whichcanbeusedtostoremobilitytrajectoriesofpersonsor
othermedicaldata(e.g.,anelectrocardiogram). WedidnotencounterprivateSDGofhigher-dimensionaldatalike
audio,images,video,ortext.
3.12 Summary
Intheearliersections,wetookalookatvariousaspectsofSDGmodelsthatwenowsummarize: Themostpopular
modeltypeistheGAN,whichisflexibleand,bydesign,cancreatelargeamountsofdatabecauseitdoesnotdirectly
train on the training data. RNNs and CNNs are used as standalone models but also serve as building blocks for
GANs,RLapproaches,diffusionmodels,andautoencoders. Theyaresuitableforgeneratingsequencesofsamplesand
high-dimensionaldata(e.g.,audio,images)respectively.
Wefindvisualdatageneration,thatis,imagesandvideos,tobebyfarthemostessentialusecaseforSDG. Virtual
environmentsareexclusivelyappliedtothisdomain. Atthesametime,GANsandautoencodersareflexiblyemployed,
andRNNsarepreferablyusedforsequentialdatasuchastimeseriesandtext. Mostmodelssamplethedata“inone
go”. Incontrast,iterativesamplerefinementwaslesspopulardespiteachievingsimilarresultsuntilrecently,when
diffusionmodelsquicklybecamecompetitiveagainstGANsforimagegeneration.
Ourperformanceevaluationfoundthatnewermodelsusuallyoutperformolderones. EspeciallyGANs,transformers,
diffusionmodels, andRNNs, sometimescombinedwithRL, oftencomeoutontop. Butwealsoencounteredtwo
significantproblems: First,nocommonstandardizedevaluationmetricforSDGmodelsexists. FID,IS,NLL,and
humanevaluationarefrequentlyusedbutarenotsuitedforalltasks. Thesecondproblemistheevaluationdata,which
isalsonotstandardized. Weidentifiedseveralcommondatasetsfordifferentdomains,butdirectcomparisonofmodels
wasoftenimpossibleduetodifferentmetricanddatasetcombinations. Anotheraspectofmodelperformancethatwas
seldommentionedisthecomputationalcomplexityofmodels,meaningthetrainingandsamplingresourcesandtime
andtheamountoftrainingdatarequiredtoachievethequalityofthepresentedresults. Amoresystematicevaluation
approachcouldsolvethecomparabilityproblem: Tomeasurethequalityofgeneratedimages,forexample,amodel
authorcouldcompareagainstafixedsetofotherpopularmodels(e.g.,DCGAN[267]),onalargersetofcommondata
sets(e.g.,celebA,MNIST,CIFAR-10)usingpredeterminedmetrics(e.g.,FID,IS). Thiscommonfoundationwould
allowforamoreprecisecomparisonofapproaches.
Accordingtoourfindingsandalsotheresearchofothers[513],privacy-preservingdatagenerationisstillintheearly
stagesofdevelopment. Itislimitedtolow-dimensionaldataliketableentriesortimeseriesandisusuallyperformed
withsimplemodelsobservablebyhumanslikeMarkovchainsorBayesiannetworks. Theonlymorecomplexmodel
thatseemstobesuitableforthistaskistheGAN,whosegeneratorneverseestheactualdata. Themainchallengealso
identifiedbyothers[513]isthetrade-offbetweendatautilityandprivacy,whichmeansthatthemodificationsrequired
tomakethedatamoreprivatereducetherepresentativeness. Anotherproblemisthatthemorecomplexandpowerful
neural-network-basedapproachesareknown[514]tocovertlyencodeindividualsamplesfromthetrainingdataintheir
parametersthatcanbereconstructed.
3.13 GuidelineforSyntheticDataGeneration
AfterclassifyingalargeamountofSDGmodelsandpresentingourfindingsinwrittenandvisualform,wefinally
provideaguidelineformodelselectionforvarioususecases. Weexplainoursuggestionsinwrittenformandfinally
illustratethemasadecisiontreeinFigure59:
• Userecentandup-to-datemodels. Morepowerfulmodelsareusuallymoreexpensivetotrain.
• Forimagegenerationandrelatedpurposes, diffusionmodelsandGANsarethebestoptionsquality-wise.
GANsarebetterforsituationswherelesstrainingdataisavailable. Autoencodersarealesspowerfulbutalso
alessresource-demandingalternative.
• Generationofsequentialdatalikesymbolicmusic, timeseries, mostgraph/moleculerepresentations, and
textisasuitabletaskfortransformersandRNNs. Markovchainsarealesspowerfulbutsimpleandefficient
alternativethathumanscaninspect.
• Autoencoders,especiallyVAEs,aregoodunsupervisedfeaturelearnersthatcandisentangleandrecombine
featuresfromtrainingdatatoproducenewdatawithdesiredproperties.
73

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
• CNNsareacommonbuildingblockofmodelstomakethemsuitabletoprocesshigh-dimensionaldatalike
large-resolutionimagesandaudiowaveforms,whosesizesotherwisesignificantlyslowdownthetraining
processorincreasemodelsizebeyondaprocessablepoint.
• For the guidance of SDG models towards producing data with specific properties (e.g., molecular proper-
ties/validity), twoapproacheshaveproventobesimpleyetpowerful: RL, especiallyincombinationwith
RNNs,allowsuserstodefinerewardsforSDGmodelstoproducethedesiredoutput. ModelslikePPGNspair
atrainedGANgeneratorwithaclassifiertofine-tuneforaspecifictask. Suchapproachescangreatlyreduce
therequiredtrainingdata.
• Forprivatedatageneration,MarkovchainsorBayesiannetworkswithmodifiedprobabilitiesornoiseinjection
inthesamplingprocesscanbeused. GANsareamodernandmorecomplexsolutiontoprivatedatageneration
whenappliedcorrectly[317].
• Whenvisualdatawithhighlyaccuratelabelsandhighconfigurabilityisrequired,virtualenvironmentsarea
goodoption,buttheyoftenrequireaconsiderableamountofhumaninteractiontobuildandconfigure.
FixedSize
DataStructure? VAEs,CNNs
G M r o a l p e h c s u , les S equ.
Text,Music, VerySimple:Markovchains
TimeSeries,Video Simple:RNNs
DataType?
WithGuidance:RNNs&RL
Images
Complex:Transformers
No
BestQuality:DiffusionModels
Faster:GANs
Privacy?
DisentangledFeatures:VAEs
AccurateLabels:VirtualEnvironments
Yes
complex
GAN
TaskComplexity?
simple
BayesianNetwork
MarkovChain
Figure59: Asimpledecisiontreeformodelselection. (Sequ. =Sequential)
4 RelatedWork
This section presents prior papers that compare or classify generative models for synthetic data. In Section 4.1,
weprovideanoverviewofpreviousworksthatselectivelycompriseandcomparemodelsinspecificdomainslike
healthcareprivacyorgraphgeneration. InSection4.2,wefocusonliteraturethataimstoorganizeapproachesforSDG
comprehensivelybyspecificaspectstoprovideanovervieworguidancetonoviceusers.
4.1 Domain-orModel-SpecificOverviewsandComparisons
Fernández and Vico [515] summarize the research done in the field of algorithmic music composition to provide
a comprehensive survey of various generation approaches: Grammars, knowledge-based systems, Markov chains,
artificialneuralnetworks,evolutionary(genetic)algorithms,andcellularautomata.
Goodfellowetal. [3]createatutorialonGANs. Theyshowhowthesemodelsworkandhowtheycanbeimprovedfor
specifictasks. Further,differentspecializedapplicationsofGANsinliteratureareshownandexplained. GANsarealso
comparedtootherapproaches,suchasbeliefnetworks,autoencoders,andBoltzmannmachines,regardinghowthe
likelihoodofgeneratedsamplescanbecomputed.
Briot et al. [11] issue a large-scale survey on music generation via deep learning. They cover different types of
musicalcontent(melody,polyphony,performedbyhumans/machines),representations(Formats: MIDI,pianoroll,text.
74

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Encodings: Scalar,one-hot,many-hot),strategies(single-step/iterativefeed-forward,sampling,etc.),challenges(e.g.,
variability,interactivity,originality)anddeepneuralnetworkarchitectures. Inthiswork,standardfeed-forwardand
recurrentneuralnetworks,autoencoders,andRBMarchitecturesarecoveredandcomparedwiththefivecriteriaabove.
Heetal. [516]provideanoverviewofdifferentmodelsandbenchmarksforimagecaptioning. Theycaptureend-to-end
encoder-decoderframeworkslikeCNN-RNNcombinationsandalsocoveranattentionmechanismappliedtosubregions
of the image to improve the decoding. Other approaches are compositional frameworks that generate and arrange
tagstogeneratecaptions,GANs,autoencoders,andRL. Theauthorsaimtohighlighttheimportanceofimage-to-text
generationandencouragenewcomerstocontributetothistopic.
Jørgensenetal. [13]reviewtheVAEasanalternativetoquantum-mechanicalcomputationswithlowercomputational
costtogeneratenewmolecularstructuresandpredicttheirproperties. Theyalsodiscussapproachestoimprovethe
realismofgenerateddatabyusinggrammar-basedinsteadofcharacter-basedencodersanddecodersandproposeother
modelslikeGANsandRLagents.
Korakakisetal. [5]provideanoverviewofvirtualenvironmentsandtheirusageinliterature. Theyillustratehow
syntheticdataobtainedfromCADrendersandvideogamescanbeusedtoimproveobjectdetectionorclassification
modelsortrainRLagents. Theauthorsidentifyatrendofsteadilyincreasingusageofvirtualenvironmentsforcheap
yeteffectivemodellearning,especiallyforcomputervisiontasks.
Gaidonetal. [8]presentninepapersexploringnovelwaysofgeneratingandusingsyntheticdataforcomputervision
tasks. Theysummarizethesenineworksandalsocoversomeoftheproblemsencounteredbytheliterature,suchas
generationchallengesorthe“sim2real”domaingap,whichdescribestheproblemoffittingmodelstrainedonsynthetic
datatorealapplicationsdespitethegenerateddataoftenbeingdifferentinsomeway(e.g., lackofphoto-realism).
Nevertheless,moreandhigher-qualitysyntheticdatamighthelpovercomethelimitationsofcurrentcomputervision
algorithms,accordingtotheauthors.
Kulkarnietal. [437]evaluatetheperformanceofRNNs,GANs,andcopulasonthegenerationofsynthetichumanmo-
bilitytrajectoriesintermsofprivacypreservation,long-rangedependencies,thestatisticalsimilarityofthedistributions,
trainingandgenerationtime,circadianrhythms,andsemanticandgeographicsimilarity. Theyconcludethatcopulas
havepreferablestatisticalandsemanticpropertiesovertheneuralnetworkmodels,whichalsoconsumemoretime
andarelesscomputationallyefficient. Further,theyassessthatautilitymetrictomeasureandmaximizeprivacyand
statisticalsimilarityjointlycouldimprovetheusabilityofsynthetictrajectories,butisnotyetavailable.
Hongetal.[4]giveadetailedintroductiontoGANsandvariousrecentlyproposedobjectivefunctionsforthem.Further,
thecombinationofaGANwithanautoencoderisdiscussed. Finally,multipleapplicationsofGANsindifferenttasks
andfieldsarecovered,andtheprosandconsofthismodeltype,suchasconvergencetowardsanoptimalsolution,are
highlighted.
Yietal. [517]reviewGANsandtheirapplicationsinmedicalimaging. TheycollectliteratureusingGANsformedical
purposessuchasimagesynthesis,segmentation,andreconstruction/repairandclassifythemaccordingtoGANmethod
(e.g.,pix2pix[335]),adversariallosstypeandquantitativemeasures(e.g.,Wassersteindistance[285])used.
Iqbaletal. [10]surveydeeplearningtextgenerationmodelsandtheprogressmadefrom2015onwards. Theyfocus
onRNNssuchasLSTMs,GRUsandbidirectionalRNNs,CNNs,VAEs,andGANsincombinationwithRL. Various
representations(Word2Vec,Glove,FastText),optimizationtechniques(stochasticgradientdescent,RMSProp,AdaGrad,
Adam),activationfunctions(Sigmoid,ReLu),andevaluationmethods(Rouge,BLEU)fortextgenerationmodelsare
alsointroduced.
Tsirikoglouetal. [9]collectandcomparedifferentimagesynthesisandaugmentationmethods. Theyidentifythatthe
visualdatagenerationpipelineconsistsoftwoparts: Content/scenegeneration,whichmeansgeneratingthefeaturesof
thevirtualenvironment,andrendering,whichsimulatesthelighttransportandperceptionofsensors. Further,synthetic
visualtrainingdatahasfourrequirementstobeuseful: Featurevariationandcoverage,domainrealism,automatic
generationofannotationsandmeta-data,andscalabilitytolargenumbersofdatapoints. Over40generativemodels
fromrecentliteraturearecategorizedbytheirmodelingandrenderingapproachandcomparedregardingimagequality
andwhattaskstheyareappliedto.
Guo et al. [7] extensively cover and analyze the recent literature of deep generative models for graph generation,
includingBNs,VAEs,GANs,RNNs,flow-basedlearningandRL. Theyprovidetaxonomiesofmodelsforconditional
andunconditionalgraphgenerationanddescribetheevaluationmetricsapplicableinthisdomain.Finally,theapplication
fieldsofdeepgraphgeneration,suchastheanalysisofinteractiondynamicsinsocialnetworks,thecreationofmolecules,
oranomalydetection,arediscussed.
75

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Seibetal. [6]discussdifferenttechniquestoimproveneuralnetworktrainingresultsoncomputervisiontasksinurban
and traffic environments without acquiring additional real-world data. The topics explored are data augmentation,
transferlearning,whichdescribesthefine-tuningofpre-trainedmodelsforanothertaskwithfewdatasamples,and
approachestogeneratingsyntheticdata. Different3Dengines(UnrealEngineandUnity)andvideogames(GTAV)and
theirusageinliteraturearecovered. AfutureoutlooktowardsGANsandtheirimage-to-imagetranslationcapabilities
isalsoprovided.
Abufaddaetal. [518]examineandsummarizerelatedworksaboutSDGinthehealthcaredomain,especiallypresenting
many GAN approaches. For each paper, they highlight the research field, used methods and results, and indicate,
whetherthemodelsaresuitablefortheirtask. Theauthorsconcludethatgeneralizedsolutionsforutilityandefficiency
evaluationswouldimprovethemodelselectionprocess.
Dankaretal. [12]proposeanoverallutilityscoreformaskedsyntheticdatasets,wherefeaturesoftheoriginaldata
havetobekeptsecret. Forthat,availablemetricsarecategorizedbythemeasuretheyaimtopreserve,andfromeachof
thefourcategories(attribute,bivariate,population,andapplicationfidelity),onesuitablemetricischosentodetermine
thefinalutilityofagenerativemodel. Theutilitymeasurementapproachisevaluatedonfourrecentmodelsand19data
setswithdifferentsizesandfeatures. Theyconcludethateachprivacy-enhancingtechnologydecreasesdatautility,and
theacceptableornecessarydecreasetoachieveprivacyisunknown.
All the literature above provides useful insight into specific application fields of synthetic data and model types.
However, the scope of the individual works is usually limited to one domain and a small selection of models and
architectures,makingthemratherunsuitableasacomprehensiveintroductiontoSDG.
4.2 ComprehensiveReviews
Turhanetal. [14]conductacomprehensivereviewofgenerativemodels,especiallyfocussingondeeplearningmodels
likeGANsandautoencodersforimagegeneration. Theyhighlightusecasesforthesemodelsandclassifytheminto
fivecategories: Unsupervisedfundamentalmodels(RBM,DBNandDBM),autoencoder-basedmodels,autoregressive
models(CNNsandRNNs),GAN-basedmodelsandautoencoder-GANhybridmodels. Further,arelationdiagramof
allpresentedmodelsiscompiledthatisparticularlyusefultobeginnersinthistopic.
Oussidietal. [15]consolidatepromisingtypesofgenerativemodelslikeRBMs,DBNs,DBMs,VAEsandGANsand
describethethreemodelsPixelRNN[115],DRAW[97]andNADE[146]indetail. Theyalsoputgenerativemodels
intotwocategories:
Costfunction-basedmodels Modelsthatoptimizeparametersbasedoncost/loss,likeautoencodersandGANs.
Energy-basedmodels Thejointprobabilityisdefinedbyanenergyfunction,whichmeasuresthecompatibilityof
variableconfigurations[279]. ThisapproachisusedbyBoltzmannmachinesandtheirderivatives.
Theystudytheiradvantages,limitations,andpotentialforthefuture. Theyfindthatenergy-basedmodelsaremore
complextocombinethandirectedgraphicalmodelslikefeed-forwardneuralnetworks,anddeepnetworksoftensuffer
fromvanishingorexplodinggradientsduringtraining. Hence,thebottomlayersbarelylearnanything,whilethetop
layersquicklyreachanoptimalstate.
Wangetal. [503]proposeanarchitecture-andloss-basedtaxonomyforGANsandhighlightthesignificantadvances
madewiththeminrecentyearsinthefieldofcomputervision. Theyfurtherdiscussthechallengesinthesetasks,such
asimagequality,diversity,andtrainingstability,butalsotherisksinvolvedinbeingabletogeneratehigh-qualityfake
data,suchasfakeevidenceofcrimesorevents.
Harshvardhanetal.[16]compileacomprehensivesurveyofgenerativemodels,highlightsomenoteworthycontributions
fromliterature,andimplementandevaluateeachpresentedmodeltohelpthereaderspickthebestsolutionfortheiruse
case. Theirhigh-levelreviewincorporatesGMMs,HMMs,LatentDirichletAllocation(LDA),Boltzmannmachines,
VAEsandGANs. Further,themodelsarealsoclassifiedbytheirlearningtype(un-/semi-andsupervisedlearning)and
theirmodelarchitecture(machinelearningorsubsetdeeplearning).
Eigenschinketal. [17]presentadata-drivenframeworkthatevaluatessyntheticdatagenerationmodelsindependently
oftheirinternalworkings. Theauthorsexclusivelycovermodelsforsyntheticsequentialdatatocomplementprevious
reviewsthatonlyfocusedonparticulardata(e.g.,time-series,videos,text)ormodel(e.g.,GANs)types. Themodels
comparedinthisworkareRNNs,CNNs,transformers,autoencoders,autoregressiveneuralnetworks,andGANs. They
arecomparedintermsof
Representativeness Howwellthesyntheticdatacapturesdistributionsanddependenciesbetweenthedistributions,
forinstance,haircolorsandeyedistancesinafaceimagedataset.
76

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
Novelty Donewsamplesresemblesamplesfromtheoriginaldataset,oraretheynewobservationsfromthelatent
distribution? This is especially important for use cases concerned with privacy, like healthcare, because
originalsamplesmustnotbeleaked.
Realism SimilartoRepresentativeness,astatisticalmeasure,butonaper-samplelevel: Often,humanjudgmentis
usedtodeterminewhethersyntheticsamplesarerealistic.
Diversity Measureofsimilaritybetweenindividualsyntheticdatapoints,forexample,theaverageEuclideandistance
totheirnearestneighbors[271].
Coherence Often implicitly evaluated with realism, coherence describes whether the internal structure of single
syntheticdatapointsisconsistent. VaryingNotesinmusic,forexample,arenaturalandnecessary,butrandom
genrechangesarenotandindicatebadcoherence.
Further,theimportanceofindividualcriteriaisevaluatedindifferentdomainssuchasNaturalLanguageProcessing
(NLP),audioprocessing,oranonymizationofhealthcaredata,concludingthatrepresentativenessandrealismaremost
importantforNLP. Speech,music,andvideotasksmostlyrelyonrealismandcoherence,privatesyntheticEHRsin
healthcareapplicationsneedrepresentativeness,novelty,andrealism,andmobilitytrajectoriesadditionallyrequire
coherence.
Nikolenko[2]releasedabookaboutsyntheticdataandhowitiscurrentlyusedforML. Thebookmainlycoversthe
computervisiontopic,especiallythecollaborationofdeeplearningmodelsforclassificationandGANsassynthetic
datagenerators,andalsoprovidesahistoricalperspectiveonit,butotherapplicationfieldslikecomputersecurity,
bioinformaticsandNLPalsomakeanappearance. Commonproblemsofgenerativemodels,suchasprivacyconcerns
andthechallengeofdomainshift,arealsotreatedinseparatesections,andpotentialsolutionsarediscussed. Finally,an
outlookonpotentialfutureimprovementsforSDGisgivenintheformofRLortheincorporationofdomainknowledge
ingenerativemodels.
The works presented here have a more comprehensive view on SDG methods, some even providing a historical
perspective[2]. Eventhoughthesesurveysandreviewsareallrecent,releasedin2018orlater,newapproacheslike
transformers[18]areoftenmissedentirely,andmanyofthemfocusprimarilyonGANsorautoencoders. Also,essential
domainslikemusic,whichcouldplayanimportantfutureroleinthefilmandvideogameindustry,areoftenforgotten.
Anotherimportantuseofacomprehensiveoverviewisthecomparisonofapproachesandguidanceofuserstoselect
anappropriatemodelfortheirusecase,whichisonlyprovidedextensivelyby[16]andcoarselyby[17]. Themain
differencebetweenourworkandthepresentedworksislistedinTable1.
Approach DataType(s) Model(s) #Works InvestigatedAspects
[515] Music 6 267 Creativity
[11] Music 7 12 Creativity,Modelcapabilities
[10] Text 5 30 Similaritytorealdata
[14] Image 2 45 Modelrelationships
[15] Image 5 13 Limitations/Advantages
[503] Image 1 36 Performance,Architecture
[16] Comprehensive 6 20-30 Lim./Adv.,Perf.,Implementation
[17] SequentialData 6 17 Creativity,DataQuality
Thisarticle 8types(15sub-types) 20(42sub-types) 417 9(seeSection3.1)
Table1: Comparisonofthissurveytoothers.
5 Conclusion
ThesurgeinapplicationsinMLhastransformedvariousfields,butlimitedtrainingdata,expensiveacquisition,and
privacylawshinderMLmodelefficacy. SDGemergesasasolution,yetthediverseandrapidlyevolvinglandscapeof
SDGmodels,spanningdecadesofdevelopment,posesachallengefordecision-makers. Tothisend,weconducteda
comprehensivesurveyof417SDGmodelpapers,resultinginthecategorizationofthesemodelsinto20distincttypes
(42sub-types). Theclassificationwasperformedbasedoncriteriaextractedfromrelatedworkandidentifiedduringour
survey. Thekeyfindingsfromourcomprehensiveclassificationareasfollows:
• Computervisionisthemostpopularapplicationfield,andGANsarethemostpopularSDGmodels.
• Differentdatatypesrequiredifferentmodeltypes. RNNsandtransformersaremoresuitableforsequential
data,whileCNNs,GANsorautoencodersaremostlyusedfordatawithstaticsize.
77

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
• Wealsoobservedatrendofcombiningdifferentmodeltypes. GANsandautoencodersoftenactasframeworks
with RNNs or CNNs as building blocks. RNNs are often combined with RL components to guide the
generationprocess.
• Ouranalysisrevealedchallengesinperformanceevaluation,citingtheabsenceofstandardizedmetricsand
datasets. Thatis,acommonsetofmetrics,datasets,andreferencemodelsisneededtoenhancecomparability
amongSDGmodels.
• We identified a nascent stage in the development of privacy-preserving data generation, where simplistic
modelslikeMarkovchains,BN,andgeneticalgorithmsareprevalent,withGANbeingtheonlymorecomplex
neuralnetwork-basedmodel.
Weareconvincedthatourworkprovidesavaluableresourceforresearchersenteringthefield,aidingtheminselecting
suitableapproachesfortheirspecificpurposes. Furthermore,itiscrucialtounderscorethenecessityforfutureresearch
to(i)delveintothetrainingandsamplingcostsofSDGmodelsforamorecomprehensiveclassificationand(ii)establish
asystematicevaluationapproachthatenhancestheoverallunderstanding,theusability,andthecomparabilityamong
SDGmodels.
References
[1] KonstantinosStathoulopoulos,JoelKlinger,andJuanMateos-Garcia. Isaieatingsoftware? ananalysisofai/ml
researchtrendsusingscientificpre-prints. Apr2018. Accessed: 2022-05-24.
[2] SergeyINikolenkoetal. Syntheticdatafordeeplearning. Springer,2021.
[3] IanGoodfellow. Nips2016tutorial: Generativeadversarialnetworks. arXivpreprintarXiv:1701.00160,2016.
[4] YongjunHong,UiwonHwang,JaeyoonYoo,andSungrohYoon. Howgenerativeadversarialnetworksandtheir
variantswork: Anoverview. ACMComputingSurveys(CSUR),52(1):1–43,2019.
[5] MichalisKorakakis,PhivosMylonas,andEvaggelosSpyrou. Ashortsurveyonmodernvirtualenvironments
thatutilizeaiandsyntheticdata. InMCIS,page34,2018.
[6] Viktor Seib, Benjamin Lange, and Stefan Wirtz. Mixing real and synthetic data to enhance neural network
training–areviewofcurrentapproaches. arXivpreprintarXiv:2007.08781,2020.
[7] Xiaojie Guo and Liang Zhao. A systematic survey on deep generative models for graph generation. arXiv
preprintarXiv:2007.06686,2020.
[8] AdrienGaidon,AntonioLopez,andFlorentPerronnin. Thereasonableeffectivenessofsyntheticvisualdata.
InternationalJournalofComputerVision,126(9):899–901,Sep2018.
[9] ApostoliaTsirikoglou, GabrielEilertsen, andJonasUnger. Asurveyofimagesynthesismethodsforvisual
machinelearning. InComputerGraphicsForum,volume39,pages426–451.WileyOnlineLibrary,2020.
[10] TouseefIqbalandShaimaQureshi. Thesurvey: Textgenerationmodelsindeeplearning. JournalofKingSaud
University-ComputerandInformationSciences,2020.
[11] Jean-PierreBriot,GaëtanHadjeres,andFrançois-DavidPachet. Deeplearningtechniquesformusicgeneration–a
survey. arXivpreprintarXiv:1709.01620,2017.
[12] Fida K Dankar, Mahmoud K Ibrahim, and Leila Ismail. A multi-dimensional evaluation of synthetic data
generators. IEEEAccess,10:11147–11158,2022.
[13] Peter B Jørgensen, Mikkel N Schmidt, and Ole Winther. Deep generative models for molecular science.
Molecularinformatics,37(1-2):1700133,2018.
[14] CerenGüzelTurhanandHasanSakirBilge. Recenttrendsindeepgenerativemodels: areview. In20183rd
InternationalConferenceonComputerScienceandEngineering(UBMK),pages574–579,2018.
[15] AchrafOussidiandAzeddineElhassouny. Deepgenerativemodels: Survey. In2018InternationalConference
onIntelligentSystemsandComputerVision(ISCV),pages1–8.IEEE,2018.
[16] GM Harshvardhan, Mahendra Kumar Gourisaria, Manjusha Pandey, and Siddharth Swarup Rautaray. A
comprehensive survey and analysis of generative models in machine learning. Computer Science Review,
38:100285,2020.
[17] PeterEigenschink,StefanVamosi,RalfVamosi,ChangSun,ThomasReutterer,andKlaudiusKalcher. Deep
generativemodelsforsyntheticdata. ACMComputingSurveys,2021.
78

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[18] AshishVaswani,NoamShazeer,NikiParmar,JakobUszkoreit,LlionJones,AidanNGomez,ŁukaszKaiser,
andIlliaPolosukhin. Attentionisallyouneed. Advancesinneuralinformationprocessingsystems,30,2017.
[19] Ali Borji. Pros and cons of gan evaluation measures: New developments. Computer Vision and Image
Understanding,215:103329,2022.
[20] JakeVanderPlas. Pythondatasciencehandbook: Essentialtoolsforworkingwithdata. O’ReillyMedia,Inc.,
2016.
[21] Aaron Van den Oord and Benjamin Schrauwen. Factoring variations in natural images with deep gaussian
mixturemodels. Advancesinneuralinformationprocessingsystems,27,2014.
[22] HeigaZenandAndrewSenior. Deepmixturedensitynetworksforacousticmodelinginstatisticalparametric
speechsynthesis. In2014IEEEinternationalconferenceonacoustics,speechandsignalprocessing(ICASSP),
pages3844–3848.IEEE,2014.
[23] SakyajitBhattacharya,OisheeMazumder,DibyenduRoy,AniruddhaSinha,andAvikGhose. Syntheticdata
generationthroughstatisticalexplosion: Improvingclassificationaccuracyofcoronaryarterydiseaseusingppg.
InICASSP2020-2020IEEEInternationalConferenceonAcoustics,SpeechandSignalProcessing(ICASSP),
pages1165–1169.IEEE,2020.
[24] RichardDurbin,SeanREddy,AndersKrogh,andGraemeMitchison.Biologicalsequenceanalysis:probabilistic
modelsofproteinsandnucleicacids. Cambridgeuniversitypress,1998.
[25] JoséLuisTriviño-RodriguezandRafaelMorales-Bueno. Usingmultiattributepredictionsuffixgraphstopredict
andgeneratemusic. ComputerMusicJournal,25(3):62–79,2001.
[26] FrançoisPachet.Beyondthecyberneticjamfantasy:Thecontinuator.IEEEComputerGraphicsandApplications,
24(1):31–35,2004.
[27] StanisławARaczyn´ski,SatoruFukayama,andEmmanuelVincent. Melodyharmonizationwithinterpolated
probabilisticmodels. JournalofNewMusicResearch,42(3):223–235,2013.
[28] MaximosKaliakatsos-PapakostasandEmiliosCambouropoulos. Probabilisticharmonizationwithfixedinterme-
diatechordconstraints. InICMC,2014.
[29] VincentBindschaedlerandRezaShokri. Synthesizingplausibleprivacy-preservinglocationtraces. In2016
IEEESymposiumonSecurityandPrivacy(SP),pages546–563.IEEE,2016.
[30] MarcAurelioRanzato,ArthurSzlam,JoanBruna,MichaelMathieu,RonanCollobert,andSumitChopra. Video
(language)modeling: abaselineforgenerativemodelsofnaturalvideos. arXivpreprintarXiv:1412.6604,2014.
[31] YoshuaBengio,RéjeanDucharme,andPascalVincent. Aneuralprobabilisticlanguagemodel. Advancesin
NeuralInformationProcessingSystems,13,2000.
[32] GabrieleBarbieri,FrançoisPachet,PierreRoy,andMirkoDegliEsposti. Markovconstraintsforgenerating
lyricswithstyle. InEcai,volume242,pages115–120,2012.
[33] PierreRoyandFrançoisPachet. Enforcingmeterinfinite-lengthmarkovsequences. InTwenty-SeventhAAAI
ConferenceonArtificialIntelligence,2013.
[34] JonathanPForsythandJuanPBello. Generatingmusicalaccompanimentusingfinitestatetransducers. In16th
InternationalConferenceonDigitalAudioEffects(DAFx-13),pages1–7,2013.
[35] AlexandrePapadopoulos,PierreRoy,andFrançoisPachet. Avoidingplagiarisminmarkovsequencegeneration.
InProceedingsoftheAAAIConferenceonArtificialIntelligence,volume28,2014.
[36] AlexandrePapadopoulos,PierreRoy,andFrançoisPachet. Assistedleadsheetcompositionusingflowcomposer.
InInternationalConferenceonPrinciplesandPracticeofConstraintProgramming,pages769–785.Springer,
2016.
[37] RaymondPWhorleyandDarrellConklin. Musicgenerationfromstatisticalmodelsofharmony. JournalofNew
MusicResearch,45(2):160–183,2016.
[38] BarbaraDraghi,ZhenchenWang,PujaMyles,andAllanTucker. Bayesboost: Identifyingandhandlingbias
usingsyntheticdatagenerators. InThirdInternationalWorkshoponLearningwithImbalancedDomains:Theory
andApplications,pages49–62.PMLR,2021.
[39] ToddAndrewStephenson. Anintroductiontobayesiannetworktheoryandusage. Technicalreport,Idiap,2000.
[40] Haipeng Guo and William Hsu. A survey of algorithms for real-time bayesian network inference. In Join
WorkshoponRealTimeDecisionSupportandDiagnosisSystems,2002.
79

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[41] DiederikPKingma. Fastgradient-basedinferencewithcontinuouslatentvariablemodelsinauxiliaryform.
arXivpreprintarXiv:1306.0733,2013.
[42] GideonSchwarz. Estimatingthedimensionofamodel. Theannalsofstatistics,pages461–464,1978.
[43] MikkoKoivistoandKismatSood. Exactbayesianstructurediscoveryinbayesiannetworks. TheJournalof
MachineLearningResearch,5:549–573,2004.
[44] Tomi Silander and Petri Myllymaki. A simple approach for finding the globally optimal bayesian network
structure. arXivpreprintarXiv:1206.6875,2012.
[45] AjitPSinghandAndrewWMoore. FindingoptimalBayesiannetworksbydynamicprogramming. Citeseer,
2005.
[46] ChangheYuan,BrandonMalone,andXiaojianWu. Learningoptimalbayesiannetworksusinga*search. In
Twenty-SecondInternationalJointConferenceonArtificialIntelligence,2011.
[47] JimYoung,PatrickGraham,andRichardPenny. Usingbayesiannetworkstocreatesyntheticdata. Journalof
OfficialStatistics,25(4):549,2009.
[48] SusanneGBøttcherandClausDethlefsen. deal: Apackageforlearningbayesiannetworks. Journalofstatistical
software,8:1–40,2003.
[49] PatrickGraham,JimYoung,andRichardPenny. Multiplyimputedsyntheticdata: Evaluationofhierarchical
bayesianimputationmodels. JournalofOfficialStatistics,25(2):245,2009.
[50] Syunpei Suzuki and Tetsuro Kitahara. Four-part harmonization using bayesian networks: pros and cons of
introducingchordnodes. JournalofNewMusicResearch,43(3):331–353,2014.
[51] JunZhang,GrahamCormode,CeciliaMProcopiuc,DiveshSrivastava,andXiaokuiXiao. Privbayes: Private
datareleaseviabayesiannetworks. ACMTransactionsonDatabaseSystems(TODS),42(4):1–41,2017.
[52] CynthiaDwork,AaronRoth,etal. Thealgorithmicfoundationsofdifferentialprivacy. FoundationsandTrends®
inTheoreticalComputerScience,9(3–4):211–407,2014.
[53] Wenzheng Chen, Huan Wang, Yangyan Li, Hao Su, Zhenhua Wang, Changhe Tu, Dani Lischinski, Daniel
Cohen-Or,andBaoquanChen. Synthesizingtrainingimagesforboostinghuman3dposeestimation. In2016
FourthInternationalConferenceon3DVision(3DV),pages479–488.IEEE,2016.
[54] HaoyuePing,JuliaStoyanovich,andBillHowe. Datasynthesizer: Privacy-preservingsyntheticdatasets. In
Proceedingsofthe29thInternationalConferenceonScientificandStatisticalDatabaseManagement,pages1–5,
2017.
[55] AllanTucker,ZhenchenWang,YleniaRotalinti,andPujaMyles. Generatinghigh-fidelitysyntheticpatientdata
forassessingmachinelearninghealthcaresoftware. NPJdigitalmedicine,3(1):1–13,2020.
[56] PeterSpirtes,ClarkNGlymour,RichardScheines,andDavidHeckerman. Causation,prediction,andsearch.
MITpress,2000.
[57] YingruiChen,MarkElliot,andJosephSakshaug. Geneticalgorithmsinmatrixrepresentationanditsapplication
insyntheticdata. InUNECEWorksessiononStatisticalConfidentiality2017.2017.
[58] ShingchernDYouandPo-ShengLiu. Automaticchordgenerationsystemusingbasicmusictheoryandgenetic
algorithm. In2016IEEEInternationalConferenceonConsumerElectronics-Taiwan(ICCE-TW),pages1–2.
IEEE,2016.
[59] Chien-HungLiuandChuan-KangTing. Polyphonicaccompanimentusinggeneticalgorithmwithmusictheory.
In2012IEEECongressonEvolutionaryComputation,pages1–7.IEEE,2012.
[60] RuslanSalakhutdinovandGeoffreyHinton. Deepboltzmannmachines. InDavidvanDykandMaxWelling,
editors,ProceedingsoftheTwelthInternationalConferenceonArtificialIntelligenceandStatistics,volume5of
ProceedingsofMachineLearningResearch,pages448–455,HiltonClearwaterBeachResort,ClearwaterBeach,
FloridaUSA,16–18Apr2009.PMLR.
[61] PaulSmolensky. Informationprocessingindynamicalsystems: Foundationsofharmonytheory. Technical
report,ColoradoUnivatBoulderDeptofComputerScience,1986.
[62] YumingHua,JunhaiGuo,andHuaZhao. Deepbeliefnetworksanddeeplearning. InProceedingsof2015
InternationalConferenceonIntelligentComputingandInternetofThings,pages1–4.IEEE,2015.
[63] HonglakLee,RogerGrosse,RajeshRanganath,andAndrewYNg. Convolutionaldeepbeliefnetworksfor
scalableunsupervisedlearningofhierarchicalrepresentations. InProceedingsofthe26thannualinternational
conferenceonmachinelearning,pages609–616,2009.
80

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[64] StefanLattner,MaartenGrachten,andGerhardWidmer. Imposinghigher-levelstructureinpolyphonicmusic
generationusingconvolutionalrestrictedboltzmannmachinesandconstraints.JournalofCreativeMusicSystems,
2:1–31,2018.
[65] GeoffreyEHinton,SimonOsindero,andYee-WhyeTeh. Afastlearningalgorithmfordeepbeliefnets. Neural
computation,18(7):1527–1554,2006.
[66] ChristopherTosh. Mixingratesforthealternatinggibbssampleroverrestrictedboltzmannmachinesandfriends.
InInternationalConferenceonMachineLearning,pages840–849.PMLR,2016.
[67] GregBickerman,SamBosley,PeterSwire,andRobertMKeller. Learningtocreatejazzmelodiesusingdeep
beliefnets. InICCC,pages228–237,2010.
[68] FelixSun. Deephear–composingandharmonizingmusicwithneuralnetworks. https://fephsun.github.
io/2015/09/01/neural-music.html,2015. Accessed: 2022-07-29.
[69] Ilya Sutskever and Geoffrey Hinton. Learning multilevel distributed representations for high-dimensional
sequences. InArtificialintelligenceandstatistics,pages548–555.PMLR,2007.
[70] IlyaSutskever,GeoffreyEHinton,andGrahamWTaylor. Therecurrenttemporalrestrictedboltzmannmachine.
Advancesinneuralinformationprocessingsystems,21,2008.
[71] RoniMittelman,BenjaminKuipers,SilvioSavarese,andHonglakLee. Structuredrecurrenttemporalrestricted
boltzmannmachines. InInternationalConferenceonMachineLearning,pages1647–1655.PMLR,2014.
[72] YannLeCun,FuJieHuang,andLeonBottou. Learningmethodsforgenericobjectrecognitionwithinvariance
toposeandlighting. InProceedingsofthe2004IEEEComputerSocietyConferenceonComputerVisionand
PatternRecognition,2004.CVPR2004.,volume2,pagesII–104.IEEE,2004.
[73] Graham W Taylor, Geoffrey E Hinton, and Sam T Roweis. Two distributed-state models for generating
high-dimensionaltimeseries. JournalofMachineLearningResearch,12(3),2011.
[74] Roland Memisevic and Geoffrey Hinton. Unsupervised learning of image transformations. In 2007 IEEE
ConferenceonComputerVisionandPatternRecognition,pages1–8.IEEE,2007.
[75] RolandMemisevicandGeoffreyEHinton. Learningtorepresentspatialtransformationswithfactoredhigher-
orderboltzmannmachines. Neuralcomputation,22(6):1473–1492,2010.
[76] PascalVincent,HugoLarochelle,YoshuaBengio,andPierre-AntoineManzagol. Extractingandcomposing
robustfeatureswithdenoisingautoencoders. InProceedingsofthe25thinternationalconferenceonMachine
learning,pages1096–1103,2008.
[77] PascalVincent,HugoLarochelle,IsabelleLajoie,YoshuaBengio,Pierre-AntoineManzagol,andLéonBottou.
Stacked denoising autoencoders: Learning useful representations in a deep network with a local denoising
criterion. Journalofmachinelearningresearch,11(12),2010.
[78] AndySarroffandMichaelACasey. Musicalaudiosynthesisusingautoencodingneuralnets. InProceedingsof
theInternationalSocietyforMusicInformationRetrievalConference(ISMIR2014).InternationalSocietyfor
MusicInformationRetrieval,2014.
[79] KarolGregor,IvoDanihelka,AndriyMnih,CharlesBlundell,andDaanWierstra. Deepautoregressivenetworks.
InInternationalConferenceonMachineLearning,pages1242–1250.PMLR,2014.
[80] JiweiLi,Minh-ThangLuong,andDanJurafsky.Ahierarchicalneuralautoencoderforparagraphsanddocuments.
arXivpreprintarXiv:1506.01057,2015.
[81] AnttiRasmus,MathiasBerglund,MikkoHonkala,HarriValpola,andTapaniRaiko. Semi-supervisedlearning
withladdernetworks. InC.Cortes,N.Lawrence,D.Lee,M.Sugiyama,andR.Garnett,editors,Advancesin
NeuralInformationProcessingSystems,volume28.CurranAssociates,Inc.,2015.
[82] LarsMaaløe,CasperKaaeSønderby,SørenKaaeSønderby,andOleWinther. Auxiliarydeepgenerativemodels.
InInternationalconferenceonmachinelearning,pages1445–1453.PMLR,2016.
[83] RimAssouel,MohamedAhmed,MarwinHSegler,AmirSaffari,andYoshuaBengio. Defactor: Differentiable
edgefactorization-basedprobabilisticgraphgeneration. arXivpreprintarXiv:1811.09766,2018.
[84] ThomasNKipfandMaxWelling. Semi-supervisedclassificationwithgraphconvolutionalnetworks. arXiv
preprintarXiv:1609.02907,2016.
[85] DmitryUlyanov,AndreaVedaldi,andVictorLempitsky. Ittakes(only)two: Adversarialgenerator-encoder
networks. InProceedingsoftheAAAIConferenceonArtificialIntelligence,volume32,2018.
81

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[86] ShainShahidChowdhury,SoukaïnaFilaliBoubrahimi,andShahMuhammadHamdi. Timeseriesdataaugmen-
tationusingtime-warpedauto-encoders. In202120thIEEEInternationalConferenceonMachineLearningand
Applications(ICMLA),pages467–470,2021.
[87] Peter Dayan, Geoffrey E Hinton, Radford M Neal, and Richard S Zemel. The helmholtz machine. Neural
computation,7(5):889–904,1995.
[88] Yifeng Li and Xiaodan Zhu. Exploring helmholtz machine and deep belief net in the exponential family
perspective. InICML2018WorkshoponTheoreticalFoundationsandApplicationsofDeepGenerativeModels,
2018.
[89] Geoffrey E Hinton, Peter Dayan, Brendan J Frey, and Radford M Neal. The" wake-sleep" algorithm for
unsupervisedneuralnetworks. Science,268(5214):1158–1161,1995.
[90] YoshuaBengio,LiYao,GuillaumeAlain,andPascalVincent. Generalizeddenoisingauto-encodersasgenerative
models,2013.
[91] Salah Rifai, Pascal Vincent, Xavier Muller, Xavier Glorot, and Yoshua Bengio. Contractive auto-encoders:
Explicitinvarianceduringfeatureextraction. InIcml,2011.
[92] SalahRifai,YoshuaBengio,YannDauphin,andPascalVincent. Agenerativeprocessforsamplingcontractive
auto-encoders. arXivpreprintarXiv:1206.6434,2012.
[93] YoshuaBengio,GrégoireMesnil,YannDauphin,andSalahRifai. Bettermixingviadeeprepresentations. In
Internationalconferenceonmachinelearning,pages552–560.PMLR,2013.
[94] YoshuaBengio,EricLaufer,GuillaumeAlain,andJasonYosinski. Deepgenerativestochasticnetworkstrainable
bybackprop. InInternationalConferenceonMachineLearning,pages226–234.PMLR,2014.
[95] LeiXuetal.SynthesizingtabulardatausingconditionalGAN.PhDthesis,MassachusettsInstituteofTechnology,
2020.
[96] DiederikPKingmaandMaxWelling. Auto-encodingvariationalbayes. arXivpreprintarXiv:1312.6114,2013.
[97] Karol Gregor, Ivo Danihelka, Alex Graves, Danilo Rezende, and Daan Wierstra. Draw: A recurrent neural
networkforimagegeneration. InInternationalConferenceonMachineLearning,pages1462–1471.PMLR,
2015.
[98] DaniloRezende,IvoDanihelka,KarolGregor,DaanWierstra,etal. One-shotgeneralizationindeepgenerative
models. InInternationalconferenceonmachinelearning,pages1521–1529.PMLR,2016.
[99] MaxJaderberg,KarenSimonyan,AndrewZisserman,etal. Spatialtransformernetworks. Advancesinneural
informationprocessingsystems,28,2015.
[100] IrinaHiggins,LoicMatthey,ArkaPal,ChristopherBurgess,XavierGlorot,MatthewBotvinick,ShakirMohamed,
andAlexanderLerchner. beta-vae: Learningbasicvisualconceptswithaconstrainedvariationalframework.
2016.
[101] XiChen,YanDuan,ReinHouthooft,JohnSchulman,IlyaSutskever,andPieterAbbeel. Infogan: Interpretable
representationlearningbyinformationmaximizinggenerativeadversarialnets. Advancesinneuralinformation
processingsystems,29,2016.
[102] Tejas D Kulkarni, William F Whitney, Pushmeet Kohli, and Josh Tenenbaum. Deep convolutional inverse
graphicsnetwork. Advancesinneuralinformationprocessingsystems,28,2015.
[103] JakubTomczakandMaxWelling. Vaewithavampprior. InInternationalConferenceonArtificialIntelligence
andStatistics,pages1214–1223.PMLR,2018.
[104] OttoFabiusandJoostRVanAmersfoort. Variationalrecurrentauto-encoders. arXivpreprintarXiv:1412.6581,
2014.
[105] DanielJiwoongIm,SungjinAhn,RolandMemisevic,andYoshuaBengio. Denoisingcriterionforvariational
auto-encodingframework. arXivpreprintarXiv:1511.06406,2015.
[106] Yuri Burda, Roger Grosse, and Ruslan Salakhutdinov. Importance weighted autoencoders. arXiv preprint
arXiv:1509.00519,2015.
[107] SamuelRBowman,LukeVilnis,OriolVinyals,AndrewMDai,RafalJozefowicz,andSamyBengio. Generating
sentencesfromacontinuousspace. arXivpreprintarXiv:1511.06349,2015.
[108] JonathanHuangandKevinMurphy. Efficientinferenceinocclusion-awaregenerativemodelsofimages. arXiv
preprintarXiv:1511.06362,2015.
82

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[109] AndersBoesenLindboLarsen,SørenKaaeSønderby,HugoLarochelle,andOleWinther. Autoencodingbeyond
pixelsusingalearnedsimilaritymetric. InInternationalconferenceonmachinelearning,pages1558–1566.
PMLR,2016.
[110] XinchenYan,JimeiYang,KihyukSohn,andHonglakLee. Attribute2image: Conditionalimagegenerationfrom
visualattributes. InEuropeanconferenceoncomputervision,pages776–791.Springer,2016.
[111] RafaelGómez-Bombarelli,JenniferNWei,DavidDuvenaud,JoséMiguelHernández-Lobato,BenjamínSánchez-
Lengeling,DennisSheberla,JorgeAguilera-Iparraguirre,TimothyDHirzel,RyanPAdams,andAlánAspuru-
Guzik. Automaticchemicaldesignusingadata-drivencontinuousrepresentationofmolecules. arXivpreprint
arXiv:1610.02415,2016.
[112] DavidWeininger. Smiles,achemicallanguageandinformationsystem.1.introductiontomethodologyand
encodingrules. Journalofchemicalinformationandcomputersciences,28(1):31–36,1988.
[113] XiChen,DiederikPKingma,TimSalimans,YanDuan,PrafullaDhariwal,JohnSchulman,IlyaSutskever,and
PieterAbbeel. Variationallossyautoencoder. arXivpreprintarXiv:1611.02731,2016.
[114] IshaanGulrajani,KundanKumar,FarukAhmed,AdrienAliTaiga,FrancescoVisin,DavidVazquez,andAaron
Courville. Pixelvae: Alatentvariablemodelfornaturalimages. arXivpreprintarXiv:1611.05013,2016.
[115] AaronVanOord,NalKalchbrenner,andKorayKavukcuoglu. Pixelrecurrentneuralnetworks. InInternational
conferenceonmachinelearning,pages1747–1756.PMLR,2016.
[116] Matt J Kusner, Brooks Paige, and José Miguel Hernández-Lobato. Grammar variational autoencoder. In
Internationalconferenceonmachinelearning,pages1945–1954.PMLR,2017.
[117] Adam Roberts, Jesse Engel, and Douglas Eck. Hierarchical variational autoencoders for music. In NIPS
WorkshoponMachineLearningforCreativityandDesign,volume3,2017.
[118] ZichaoYang,ZhitingHu,RuslanSalakhutdinov,andTaylorBerg-Kirkpatrick.Improvedvariationalautoencoders
fortextmodelingusingdilatedconvolutions. InInternationalconferenceonmachinelearning,pages3881–3890.
PMLR,2017.
[119] AaronVanDenOord,OriolVinyals,etal.Neuraldiscreterepresentationlearning.Advancesinneuralinformation
processingsystems,30,2017.
[120] StanislauSemeniuta,AliakseiSeveryn,andErhardtBarth. Ahybridconvolutionalvariationalautoencoderfor
textgeneration. arXivpreprintarXiv:1702.02390,2017.
[121] DavidHaandDouglasEck. Aneuralrepresentationofsketchdrawings. arXivpreprintarXiv:1704.03477,2017.
[122] AlexeyTikhonov,IvanPYamshchikov,etal. Musicgenerationwithvariationalrecurrentautoencodersupported
byhistory. arXivpreprintarXiv:1705.05458,2017.
[123] JesseEngel,MatthewHoffman,andAdamRoberts. Latentconstraints: Learningtogenerateconditionallyfrom
unconditionalgenerativemodels. arXivpreprintarXiv:1711.05772,2017.
[124] PeterBjørnJørgensen,MuratMesta,SuranjanShil,JuanMariaGarcíaLastra,KarstenWedelJacobsen,Kris-
tianSommerThygesen,andMikkelNSchmidt. Machinelearning-basedscreeningofcomplexmoleculesfor
polymersolarcells. TheJournalofchemicalphysics,148(24):241735,2018.
[125] MartinSimonovskyandNikosKomodakis. Graphvae: Towardsgenerationofsmallgraphsusingvariational
autoencoders. InInternationalconferenceonartificialneuralnetworks,pages412–422.Springer,2018.
[126] AdamRoberts,JesseEngel,ColinRaffel,CurtisHawthorne,andDouglasEck.Ahierarchicallatentvectormodel
forlearninglong-termstructureinmusic. InInternationalconferenceonmachinelearning,pages4364–4373.
PMLR,2018.
[127] WengongJin,ReginaBarzilay,andTommiJaakkola. Junctiontreevariationalautoencoderformoleculargraph
generation. InInternationalconferenceonmachinelearning,pages2323–2332.PMLR,2018.
[128] JustinGilmer,SamuelSSchoenholz,PatrickFRiley,OriolVinyals,andGeorgeEDahl. Neuralmessagepassing
forquantumchemistry. InInternationalconferenceonmachinelearning,pages1263–1272.PMLR,2017.
[129] QiLiu,MiltiadisAllamanis,MarcBrockschmidt,andAlexanderGaunt. Constrainedgraphvariationalautoen-
codersformoleculedesign. Advancesinneuralinformationprocessingsystems,31,2018.
[130] HanjunDai,YingtaoTian,BoDai,StevenSkiena,andLeSong. Syntax-directedvariationalautoencoderfor
structureddata. arXivpreprintarXiv:1802.08786,2018.
[131] QingrongChen,ChongXiang,MinhuiXue,BoLi,NikitaBorisov,DaliKaarfar,andHaojinZhu. Differentially
privatedatagenerativemodels. arXivpreprintarXiv:1812.02274,2018.
83

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[132] MartinAbadi,AndyChu,IanGoodfellow,HBrendanMcMahan,IlyaMironov,KunalTalwar,andLiZhang.
Deeplearningwithdifferentialprivacy. InProceedingsofthe2016ACMSIGSACconferenceoncomputerand
communicationssecurity,pages308–318,2016.
[133] HuaiboHuang,zhihangli,RanHe,ZhenanSun,andTieniuTan. Introvae: Introspectivevariationalautoencoders
forphotographicimagesynthesis. InS.Bengio,H.Wallach,H.Larochelle,K.Grauman,N.Cesa-Bianchi,and
R.Garnett,editors,AdvancesinNeuralInformationProcessingSystems,volume31.CurranAssociates,Inc.,
2018.
[134] DinghanShen,AsliCelikyilmaz,YizheZhang,LiqunChen,XinWang,JianfengGao,andLawrenceCarin. To-
wardsgeneratinglongandcoherenttextwithmulti-levellatentvariablemodels.arXivpreprintarXiv:1902.00154,
2019.
[135] Wenlin Wang, Zhe Gan, Hongteng Xu, Ruiyi Zhang, Guoyin Wang, Dinghan Shen, Changyou Chen, and
LawrenceCarin. Topic-guidedvariationalautoencodersfortextgeneration. arXivpreprintarXiv:1903.07137,
2019.
[136] XavierBressonandThomasLaurent. Atwo-stepgraphconvolutionaldecoderformoleculegeneration. arXiv
preprintarXiv:1906.03412,2019.
[137] BidishaSamanta,AbirDe,GourhariJana,VicençGómez,PratimKumarChattaraj,NiloyGanguly,andManuel
Gomez-Rodriguez. Nevae: Adeepgenerativemodelformoleculargraphs. Journalofmachinelearningresearch.
2020Apr;21(114): 1-33,2020.
[138] XiaojieGuo,LiangZhao,ZhaoQin,LingfeiWu,AmardaShehu,andYanfangYe. Interpretabledeepgraph
generation with node-edge co-disentanglement. In Proceedings of the 26th ACM SIGKDD international
conferenceonknowledgediscovery&datamining,pages1697–1707,2020.
[139] AlfredoNazabal,PabloMOlmos,ZoubinGhahramani,andIsabelValera. Handlingincompleteheterogeneous
datausingvaes. PatternRecognition,107:107501,2020.
[140] DanielFlam-Shepherd,TonyWu,andAlanAspuru-Guzik. Graphdeconvolutionalgeneration. arXivpreprint
arXiv:2002.07087,2020.
[141] Marco Podda, Davide Bacciu, and Alessio Micheli. A deep generative model for fragment-based molecule
generation. InInternationalConferenceonArtificialIntelligenceandStatistics,pages2240–2250.PMLR,2020.
[142] DaniloJimenezRezende,ShakirMohamed,andDaanWierstra. Stochasticbackpropagationandapproximate
inferenceindeepgenerativemodels. InInternationalconferenceonmachinelearning,pages1278–1286.PMLR,
2014.
[143] VincentMichalski,RolandMemisevic,andKishoreKonda.Modelingdeeptemporaldependencieswithrecurrent
grammarcells"". Advancesinneuralinformationprocessingsystems,27,2014.
[144] RolandMemisevic. Gradient-basedlearningofhigher-orderimagefeatures. In2011InternationalConference
onComputerVision,pages1591–1598.IEEE,2011.
[145] MathieuGermain,KarolGregor,IainMurray,andHugoLarochelle. Made: Maskedautoencoderfordistribution
estimation. InInternationalconferenceonmachinelearning,pages881–889.PMLR,2015.
[146] Hugo Larochelle and Iain Murray. The neural autoregressive distribution estimator. In Proceedings of the
fourteenthinternationalconferenceonartificialintelligenceandstatistics,pages29–37.JMLRWorkshopand
ConferenceProceedings,2011.
[147] BenignoUria,IainMurray,andHugoLarochelle.Rnade:Thereal-valuedneuralautoregressivedensity-estimator.
AdvancesinNeuralInformationProcessingSystems,26,2013.
[148] Benigno Uria, Iain Murray, and Hugo Larochelle. A deep and tractable density estimator. In International
ConferenceonMachineLearning,pages467–475.PMLR,2014.
[149] TapaniRaiko,YaoLi,KyunghyunCho,andYoshuaBengio. Iterativeneuralautoregressivedistributionestimator
nade-k. Advancesinneuralinformationprocessingsystems,27,2014.
[150] BenignoUria,Marc-AlexandreCôté,KarolGregor,IainMurray,andHugoLarochelle. Neuralautoregressive
distributionestimation. TheJournalofMachineLearningResearch,17(1):7184–7220,2016.
[151] FrancescoTonolini,BjørnSandJensen,andRoderickMurray-Smith. Variationalsparsecoding. InUncertainty
inArtificialIntelligence,pages690–700.PMLR,2020.
[152] BrunoAOlshausenandDavidJField. Sparsecodingofsensoryinputs. CurrentOpinioninNeurobiology,
14(4):481–487,2004.
84

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[153] Zhaowen Wang, Ding Liu, Jianchao Yang, Wei Han, and Thomas Huang. Deep networks for image super-
resolutionwithsparseprior. InProceedingsoftheIEEEinternationalconferenceoncomputervision,pages
370–378,2015.
[154] ZacharyLipton. Acriticalreviewofrecurrentneuralnetworksforsequencelearning. 052015.
[155] HaonanYu,JiangWang,ZhihengHuang,YiYang,andWeiXu. Videoparagraphcaptioningusinghierarchical
recurrentneuralnetworks. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,
pages4584–4593,2016.
[156] NicolasBoulanger-Lewandowski,YoshuaBengio, andPascalVincent. Modelingtemporaldependenciesin
high-dimensional sequences: Application topolyphonic music generation andtranscription. arXiv preprint
arXiv:1206.6392,2012.
[157] AlexGraves. Generatingsequenceswithrecurrentneuralnetworks. arXivpreprintarXiv:1308.0850,2013.
[158] OriolVinyals,AlexanderToshev,SamyBengio,andDumitruErhan. Showandtell: Aneuralimagecaption
generator. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages3156–3164,
2015.
[159] JeffreyDonahue,LisaAnneHendricks,SergioGuadarrama,MarcusRohrbach,SubhashiniVenugopalan,Kate
Saenko,andTrevorDarrell. Long-termrecurrentconvolutionalnetworksforvisualrecognitionanddescription.
InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages2625–2634,2015.
[160] NitishSrivastava,ElmanMansimov,andRuslanSalakhudinov. Unsupervisedlearningofvideorepresentations
usinglstms. InInternationalconferenceonmachinelearning,pages843–852.PMLR,2015.
[161] ElmanMansimov,EmilioParisotto,JimmyLeiBa,andRuslanSalakhutdinov. Generatingimagesfromcaptions
withattention. arXivpreprintarXiv:1511.02793,2015.
[162] Natasha Jaques, Shixiang Gu, Richard E Turner, and Douglas Eck. Tuning recurrent neural networks with
re-inforcementlearning. arXivpreprintarXiv:1611.02796,2016.
[163] ElliotWaiteetal. Generatinglong-termstructureinsongsandstories. Webblogpost.Magenta,15(4),2016.
Accessed: 2022-05-13.
[164] GaëtanHadjeresandFrankNielsen. Interactivemusicgenerationwithpositionalconstraintsusinganticipation-
rnns. arXivpreprintarXiv:1709.06404,2017.
[165] SageevOore,IanSimon,SanderDieleman,DouglasEck,andKarenSimonyan. Thistimewithfeeling:Learning
expressivemusicalperformance. NeuralComputingandApplications,32(4):955–967,2020.
[166] Yoshua Bengio, Nicolas Boulanger-Lewandowski, and Razvan Pascanu. Advances in optimizing recurrent
networks. arXivpreprintarXiv:1212.0901,2012.
[167] TomášMikolov,IlyaSutskever,AnoopDeoras,Hai-SonLe,StefanKombrink,andJanCernocky. Subword
languagemodelingwithneuralnetworks. preprint(http://www.fit.vutbr.cz/imikolov/rnnlm/char.pdf),8(67),
2012.
[168] AndrésECoca,DéboraCCorrêa,andLiangZhao. Computer-aidedmusiccompositionwithlstmneuralnetwork
andchaoticinspiration. InIJCNN,pages1–7,2013.
[169] JustinBayer,ChristianOsendorfer,DanielaKorhammer,NutanChen,SebastianUrban,andPatrickvander
Smagt. Onfastdropoutanditsapplicabilitytorecurrentnetworks. arXivpreprintarXiv:1311.0701,2013.
[170] RazvanPascanu,CaglarGulcehre,KyunghyunCho,andYoshuaBengio. Howtoconstructdeeprecurrentneural
networks. arXivpreprintarXiv:1312.6026,2013.
[171] SubhashiniVenugopalan,HuijuanXu,JeffDonahue,MarcusRohrbach,RaymondMooney,andKateSaenko.
Translatingvideostonaturallanguageusingdeeprecurrentneuralnetworks. arXivpreprintarXiv:1412.4729,
2014.
[172] XingxingZhangandMirellaLapata. Chinesepoetrygenerationwithrecurrentneuralnetworks. InProceedings
ofthe2014ConferenceonEmpiricalMethodsinNaturalLanguageProcessing(EMNLP),pages670–680,2014.
[173] JustinBayerandChristianOsendorfer. Learningstochasticrecurrentnetworks. arXivpreprintarXiv:1411.7610,
2014.
[174] Jan Koutnik, Klaus Greff, Faustino Gomez, and Juergen Schmidhuber. A clockwork rnn. In International
ConferenceonMachineLearning,pages1863–1871.PMLR,2014.
[175] ILiu,BhikshaRamakrishnan,etal. Bachin2014: Musiccompositionwithrecurrentneuralnetwork. arXiv
preprintarXiv:1412.3191,2014.
85

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[176] MartinRiedmillerandIRprop. Rprop-descriptionandimplementationdetails. 1994.
[177] KratarthGoel,RaunaqVohra,andJajatiKeshariSahoo. Polyphonicmusicgenerationbymodelingtemporal
dependencies using a rnn-dbn. In International Conference on Artificial Neural Networks, pages 217–224.
Springer,2014.
[178] JunhuaMao,WeiXu,YiYang,JiangWang,ZhihengHuang,andAlanYuille. Deepcaptioningwithmultimodal
recurrentneuralnetworks(m-rnn). arXivpreprintarXiv:1412.6632,2014.
[179] LucasTheisandMatthiasBethge.Generativeimagemodelingusingspatiallstms.Advancesinneuralinformation
processingsystems,28,2015.
[180] AlexGravesandJürgenSchmidhuber. Offlinehandwritingrecognitionwithmultidimensionalrecurrentneural
networks. Advancesinneuralinformationprocessingsystems,21,2008.
[181] LucasTheis,ReshadHosseini,andMatthiasBethge. Mixturesofconditionalgaussianscalemixturesappliedto
multiscaleimagerepresentations. 2012.
[182] MathiasBerglund,TapaniRaiko,MikkoHonkala,LeoKärkkäinen,AkosVetek,andJuhaTKarhunen. Bidirec-
tionalrecurrentneuralnetworksasgenerativemodels. Advancesinneuralinformationprocessingsystems,28,
2015.
[183] Junyoung Chung, Kyle Kastner, Laurent Dinh, Kratarth Goel, Aaron C Courville, and Yoshua Bengio. A
recurrentlatentvariablemodelforsequentialdata. Advancesinneuralinformationprocessingsystems,28,2015.
[184] SamyBengio,OriolVinyals,NavdeepJaitly,andNoamShazeer. Scheduledsamplingforsequenceprediction
withrecurrentneuralnetworks. Advancesinneuralinformationprocessingsystems,28,2015.
[185] XinleiChenandCLawrenceZitnick. Mind’seye:Arecurrentvisualrepresentationforimagecaptiongeneration.
InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages2422–2431,2015.
[186] KarenSimonyanandAndrewZisserman. Verydeepconvolutionalnetworksforlarge-scaleimagerecognition.
arXivpreprintarXiv:1409.1556,2014.
[187] Andrej Karpathy and Li Fei-Fei. Deep visual-semantic alignments for generating image descriptions. In
ProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages3128–3137,2015.
[188] Raunaq Vohra, Kratarth Goel, and Jajati Keshari Sahoo. Modeling temporal dependencies in data using a
dbn-lstm. In2015IEEEInternationalConferenceonDataScienceandAdvancedAnalytics(DSAA),pages1–4.
IEEE,2015.
[189] Qi Lyu, Zhiyong Wu, Jun Zhu, and Helen Meng. Modelling high-dimensional sequences with lstm-rtrbm:
Application to polyphonic music generation. In Twenty-Fourth International Joint Conference on Artificial
Intelligence,2015.
[190] KelvinXu,JimmyBa,RyanKiros,KyunghyunCho,AaronCourville,RuslanSalakhudinov,RichZemel,and
YoshuaBengio. Show,attendandtell: Neuralimagecaptiongenerationwithvisualattention. InInternational
conferenceonmachinelearning,pages2048–2057.PMLR,2015.
[191] Subhashini Venugopalan, Marcus Rohrbach, Jeffrey Donahue, Raymond Mooney, Trevor Darrell, and Kate
Saenko. Sequencetosequence-videototext. InProceedingsoftheIEEEinternationalconferenceoncomputer
vision,pages4534–4542,2015.
[192] LiYao,AtousaTorabi,KyunghyunCho,NicolasBallas,ChristopherPal,HugoLarochelle,andAaronCourville.
Describingvideosbyexploitingtemporalstructure. InProceedingsoftheIEEEinternationalconferenceon
computervision,pages4507–4515,2015.
[193] MarcoFraccaro,SørenKaaeSønderby,UlrichPaquet,andOleWinther. Sequentialneuralmodelswithstochastic
layers. Advancesinneuralinformationprocessingsystems,29,2016.
[194] FlorianColombo,SamuelPMuscinelli,AlexanderSeeholzer,JohanniBrea,andWulframGerstner. Algorithmic
compositionofmelodieswithdeeprecurrentneuralnetworks. arXivpreprintarXiv:1606.07251,2016.
[195] ZhengSun,JiaqiLiu,ZewangZhang,JingwenChen,ZhaoHuo,ChingHuaLee,andXiaoZhang. Composing
musicwithgrammarargumentedneuralnetworksandnote-levelencoding. arXivpreprintarXiv:1611.05416,
2016.
[196] DzmitryBahdanau,PhilemonBrakel,KelvinXu,AnirudhGoyal,RyanLowe,JoellePineau,AaronCourville,
andYoshuaBengio. Anactor-criticalgorithmforsequenceprediction. arXivpreprintarXiv:1607.07086,2016.
[197] ZhilinYang,YeYuan,YuexinWu,WilliamWCohen,andRussRSalakhutdinov. Reviewnetworksforcaption
generation. Advancesinneuralinformationprocessingsystems,29,2016.
86

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[198] QuanzengYou,HailinJin,ZhaowenWang,ChenFang,andJieboLuo. Imagecaptioningwithsemanticattention.
InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages4651–4659,2016.
[199] KeunwooChoi,GeorgeFazekas,andMarkSandler. Text-basedlstmnetworksforautomaticmusiccomposition.
arXivpreprintarXiv:1604.05358,2016.
[200] Hang Chu, Raquel Urtasun, and Sanja Fidler. Song from pi: A musically plausible network for pop music
generation. arXivpreprintarXiv:1611.03477,2016.
[201] BobLSturm,JoaoFelipeSantos,OdedBen-Tal,andIrynaKorshunova. Musictranscriptionmodellingand
compositionusingdeeplearning. arXivpreprintarXiv:1604.08723,2016.
[202] Feynman Liang. Bachbot: Automatic composition in the style of bach chorales. University of Cambridge,
8:19–48,2016.
[203] AllenHuangandRaymondWu. Deeplearningformusic. arXivpreprintarXiv:1606.04930,2016.
[204] SoroushMehri,KundanKumar,IshaanGulrajani,RitheshKumar,ShubhamJain,JoseSotelo,AaronCourville,
andYoshuaBengio. Samplernn: Anunconditionalend-to-endneuralaudiogenerationmodel. arXivpreprint
arXiv:1612.07837,2016.
[205] IulianSerban,AlessandroSordoni,YoshuaBengio,AaronCourville,andJoellePineau. Buildingend-to-end
dialoguesystemsusinggenerativehierarchicalneuralnetworkmodels. InProceedingsoftheAAAIConference
onArtificialIntelligence,volume30,2016.
[206] Alex M Lamb, Anirudh Goyal ALIAS PARTH GOYAL, Ying Zhang, Saizheng Zhang, Aaron C Courville,
andYoshuaBengio. Professorforcing: Anewalgorithmfortrainingrecurrentnetworks. Advancesinneural
informationprocessingsystems,29,2016.
[207] JoseSotelo,SoroushMehri,KundanKumar,JoaoFelipeSantos,KyleKastner,AaronCourville,andYoshua
Bengio. Char2wav: End-to-endspeechsynthesis. 2017.
[208] Julian Georg Zilly, Rupesh Kumar Srivastava, Jan Koutnık, and Jürgen Schmidhuber. Recurrent highway
networks. InInternationalconferenceonmachinelearning,pages4189–4198.PMLR,2017.
[209] RupeshKSrivastava,KlausGreff,andJürgenSchmidhuber. Trainingverydeepnetworks. Advancesinneural
informationprocessingsystems,28,2015.
[210] FlorianColombo,AlexanderSeeholzer,andWulframGerstner. Deepartificialcomposer: Acreativeneural
networkmodelforautomatedmelodygeneration. InInternationalConferenceonEvolutionaryandBiologically
InspiredMusicandArt,pages81–96.Springer,2017.
[211] Chenxi Liu, Junhua Mao, Fei Sha, and Alan Yuille. Attention correctness in neural image captioning. In
Thirty-firstAAAIconferenceonartificialintelligence,2017.
[212] ZheGan,ChuangGan,XiaodongHe,YunchenPu,KennethTran,JianfengGao,LawrenceCarin,andLiDeng.
Semanticcompositionalnetworksforvisualcaptioning. InProceedingsoftheIEEEconferenceoncomputer
visionandpatternrecognition,pages5630–5639,2017.
[213] GaëtanHadjeres,FrançoisPachet,andFrankNielsen. Deepbach: asteerablemodelforbachchoralesgeneration.
InInternationalConferenceonMachineLearning,pages1362–1371.PMLR,2017.
[214] DimosMakris,MaximosKaliakatsos-Papakostas,IoannisKarydis,andKatiaLidaKermanidis. Combining
lstmandfeedforwardneuralnetworksforconditionalrhythmcomposition. InInternationalconferenceon
engineeringapplicationsofneuralnetworks,pages570–582.Springer,2017.
[215] Natasha Jaques, Shixiang Gu, Dzmitry Bahdanau, José Miguel Hernández-Lobato, Richard E Turner, and
Douglas Eck. Sequence tutor: Conservative fine-tuning of sequence generation models with kl-control. In
InternationalConferenceonMachineLearning,pages1645–1654.PMLR,2017.
[216] HyunguiLim,SeungyeonRhyu,andKyoguLee. Chordgenerationfromsymbolicmelodyusingblstmnetworks.
arXivpreprintarXiv:1712.01011,2017.
[217] IulianSerban,AlessandroSordoni,RyanLowe,LaurentCharlin,JoellePineau,AaronCourville,andYoshua
Bengio. Ahierarchicallatentvariableencoder-decodermodelforgeneratingdialogues. InProceedingsofthe
AAAIConferenceonArtificialIntelligence,volume31,2017.
[218] PatrickHutchingsandJonMcCormack. Usingautonomousagentstoimprovisemusiccompositionsinreal-time.
InInternationalconferenceonevolutionaryandbiologicallyinspiredmusicandart,pages114–127.Springer,
2017.
[219] Ian Simon and Sageev Oore. Performance rnn: Generating music with expressive timing and dynamics.
https://magenta.tensorflow.org/performance-rnn,2017.
87

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[220] DanielDJohnson. Generatingpolyphonicmusicusingtiedparallelnetworks. InInternationalconferenceon
evolutionaryandbiologicallyinspiredmusicandart,pages128–143.Springer,2017.
[221] RachelManzelli, VijayThakkar, AliSiahkamari, andBrianKulis. Conditioningdeepgenerativerawaudio
modelsforstructuredautomaticmusic. arXivpreprintarXiv:1806.09905,2018.
[222] YujiaLi,OriolVinyals,ChrisDyer,RazvanPascanu,andPeterBattaglia. Learningdeepgenerativemodelsof
graphs. arXivpreprintarXiv:1803.03324,2018.
[223] NalKalchbrenner,ErichElsen,KarenSimonyan,SebNoury,NormanCasagrande,EdwardLockhart,Florian
Stimberg, Aaron Oord, Sander Dieleman, and Koray Kavukcuoglu. Efficient neural audio synthesis. In
InternationalConferenceonMachineLearning,pages2410–2419.PMLR,2018.
[224] AdamSantoro,RyanFaulkner,DavidRaposo,JackRae,MikeChrzanowski,TheophaneWeber,DaanWierstra,
OriolVinyals,RazvanPascanu,andTimothyLillicrap. Relationalrecurrentneuralnetworks. Advancesinneural
informationprocessingsystems,31,2018.
[225] HuanruHenryMao,TaylorShin,andGarrisonCottrell. Deepj: Style-specificmusicgeneration. In2018IEEE
12thInternationalConferenceonSemanticComputing(ICSC),pages377–382.IEEE,2018.
[226] Jiaxuan You, Rex Ying, Xiang Ren, William Hamilton, and Jure Leskovec. Graphrnn: Generating realistic
graphswithdeepauto-regressivemodels. InInternationalconferenceonmachinelearning,pages5708–5717.
PMLR,2018.
[227] JonathanShen,RuomingPang,RonJWeiss,MikeSchuster,NavdeepJaitly,ZonghengYang,ZhifengChen,
YuZhang,YuxuanWang,RjSkerrv-Ryan,etal.Naturalttssynthesisbyconditioningwavenetonmelspectrogram
predictions. In2018IEEEinternationalconferenceonacoustics,speechandsignalprocessing(ICASSP),pages
4779–4783.IEEE,2018.
[228] AaronvandenOord,SanderDieleman,HeigaZen,KarenSimonyan,OriolVinyals,AlexGraves,NalKalch-
brenner,AndrewSenior,andKorayKavukcuoglu. Wavenet: Agenerativemodelforrawaudio. arXivpreprint
arXiv:1609.03499,2016.
[229] Renjie Liao, Yujia Li, Yang Song, Shenlong Wang, Will Hamilton, David K Duvenaud, Raquel Urtasun,
andRichardZemel. Efficientgraphgenerationwithgraphrecurrentattentionnetworks. Advancesinneural
informationprocessingsystems,32,2019.
[230] DavideBacciu,AlessioMicheli,andMarcoPodda. Graphgenerationbysequentialedgeprediction. In27th
EuropeanSymposiumonArtificialNeuralNetworks,ComputationalIntelligenceandMachineLearning,ESANN
2019,pages95–100.ESANN(i6doc.com),2019.
[231] Mariya Popova, Mykhailo Shvets, Junier Oliva, and Olexandr Isayev. Molecularrnn: Generating realistic
moleculargraphswithoptimizedproperties. arXivpreprintarXiv:1905.13372,2019.
[232] MahdiKhodayar,JianhuiWang,andZhaoyuWang. Deepgenerativegraphdistributionlearningforsynthetic
powergrids. arXivpreprintarXiv:1901.09674,2019.
[233] AndresHernandez-Matamoros,HamidoFujita,andHectorPerez-Meana. Anovelapproachtocreatesynthetic
biomedicalsignalsusingbirnn. InformationSciences,541:218–241,2020.
[234] NikhilGoyal,HarshVardhanJain,andSayanRanu. Graphgen: ascalableapproachtodomain-agnosticlabeled
graphgeneration. InProceedingsofTheWebConference2020,pages1253–1263,2020.
[235] NicolaPrivato, OmarRampado, andAlbertoNovello. Acreativetoolforthemusiciancombininglstmand
markovchainsinmax/msp. InInternationalConferenceonComputationalIntelligenceinMusic,Sound,Artand
Design(PartofEvoStar),pages228–242.Springer,2022.
[236] SaadAlbawi,TareqAbedMohammed,andSaadAl-Zawi. Understandingofaconvolutionalneuralnetwork. In
2017internationalconferenceonengineeringandtechnology(ICET),pages1–6.Ieee,2017.
[237] WilliamLotter,GabrielKreiman,andDavidCox. Unsupervisedlearningofvisualstructureusingpredictive
generativenetworks. arXivpreprintarXiv:1511.06380,2015.
[238] IanGoodfellow,JeanPouget-Abadie,MehdiMirza,BingXu,DavidWarde-Farley,SherjilOzair,AaronCourville,
andYoshuaBengio. Generativeadversarialnets. Advancesinneuralinformationprocessingsystems,27,2014.
[239] JoanBruna,PabloSprechmann,andYannLeCun. Super-resolutionwithdeepconvolutionalsufficientstatistics.
arXivpreprintarXiv:1511.05666,2015.
[240] Nal Kalchbrenner, Aäron Oord, Karen Simonyan, Ivo Danihelka, Oriol Vinyals, Alex Graves, and Koray
Kavukcuoglu. Videopixelnetworks. InInternationalConferenceonMachineLearning, pages1771–1779.
PMLR,2017.
88

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[241] Scott Reed, Aäron van den Oord, Nal Kalchbrenner, Victor Bapst, Matt Botvinick, and Nando De Freitas.
Generatinginterpretableimageswithcontrollablestructure. 2016.
[242] LeonAGatys,AlexanderSEcker,andMatthiasBethge.Imagestyletransferusingconvolutionalneuralnetworks.
InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages2414–2423,2016.
[243] JiwonKim,JungKwonLee,andKyoungMuLee. Deeply-recursiveconvolutionalnetworkforimagesuper-
resolution. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages1637–1645,
2016.
[244] ChaoDong,ChenChangeLoy,KaimingHe,andXiaoouTang. Learningadeepconvolutionalnetworkforimage
super-resolution. InEuropeanconferenceoncomputervision,pages184–199.Springer,2014.
[245] ChaoDong,ChenChangeLoy,KaimingHe,andXiaoouTang. Imagesuper-resolutionusingdeepconvolutional
networks. IEEEtransactionsonpatternanalysisandmachineintelligence,38(2):295–307,2015.
[246] TimSalimans,AndrejKarpathy,XiChen,andDiederikPKingma. Pixelcnn++: Improvingthepixelcnnwith
discretizedlogisticmixturelikelihoodandothermodifications. arXivpreprintarXiv:1701.05517,2017.
[247] AlexanderMordvintsev,ChristopherOlah,andMikeTyka. Deepdream-acodeexampleforvisualizingneural
networks. GoogleResearch,2(5),2015.
[248] AlexanderMordvintsev,ChristopherOlah,andMikeTyka. Inceptionism: Goingdeeperintoneuralnetworks.
2015.
[249] AaronVandenOord,NalKalchbrenner,LasseEspeholt,OriolVinyals,AlexGraves,etal. Conditionalimage
generationwithpixelcnndecoders. Advancesinneuralinformationprocessingsystems,29,2016.
[250] JustinJohnson,AlexandreAlahi,andLiFei-Fei.Perceptuallossesforreal-timestyletransferandsuper-resolution.
InEuropeanconferenceoncomputervision,pages694–711.Springer,2016.
[251] WenzheShi,JoseCaballero,FerencHuszár,JohannesTotz,AndrewPAitken,RobBishop,DanielRueckert,and
ZehanWang. Real-timesingleimageandvideosuper-resolutionusinganefficientsub-pixelconvolutionalneural
network. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages1874–1883,
2016.
[252] WeiPing,KainanPeng,AndrewGibiansky,SercanÖmerArik,AjayKannan,SharanNarang,JonathanRaiman,
andJohnMiller. Deepvoice3: 2000-speakerneuraltext-to-speech. 2017.
[253] Xi Chen, Nikhil Mishra, Mostafa Rohaninejad, and Pieter Abbeel. Pixelsnail: An improved autoregressive
generativemodel. arXivpreprintarXiv:1712.09763,2017.
[254] NikhilMishra,MostafaRohaninejad,XiChen,andPieterAbbeel. Asimpleneuralattentivemeta-learner. arXiv
preprintarXiv:1707.03141,2017.
[255] Jacob Menick and Nal Kalchbrenner. Generating high fidelity images with subscale pixel networks and
multidimensionalupscaling. arXivpreprintarXiv:1812.01608,2018.
[256] YifanWang,LijunWang,HongyuWang,andPeihuaLi. End-to-endimagesuper-resolutionviadeepandshallow
convolutionalnetworks. IEEEAccess,7:31959–31970,2019.
[257] PeterJLiu,MohammadSaleh,EtiennePot,BenGoodrich,RyanSepassi,LukaszKaiser,andNoamShazeer.
Generatingwikipediabysummarizinglongsequences. arXivpreprintarXiv:1801.10198,2018.
[258] NikiParmar,AshishVaswani,JakobUszkoreit,LukaszKaiser,NoamShazeer,AlexanderKu,andDustinTran.
Imagetransformer. InInternationalConferenceonMachineLearning,pages4055–4064.PMLR,2018.
[259] Cheng-Zhi Anna Huang, Ashish Vaswani, Jakob Uszkoreit, Noam Shazeer, Ian Simon, Curtis Hawthorne,
AndrewMDai,MatthewDHoffman,MonicaDinculescu,andDouglasEck. Musictransformer. arXivpreprint
arXiv:1809.04281,2018.
[260] PeterShaw,JakobUszkoreit,andAshishVaswani. Self-attentionwithrelativepositionrepresentations. arXiv
preprintarXiv:1803.02155,2018.
[261] RewonChild,ScottGray,AlecRadford,andIlyaSutskever. Generatinglongsequenceswithsparsetransformers.
arXivpreprintarXiv:1904.10509,2019.
[262] ChenSun,AustinMyers,CarlVondrick,KevinMurphy,andCordeliaSchmid. Videobert: Ajointmodelfor
video and language representation learning. In Proceedings of the IEEE/CVF International Conference on
ComputerVision,pages7464–7473,2019.
[263] JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. Bert: Pre-trainingofdeepbidirectional
transformersforlanguageunderstanding. arXivpreprintarXiv:1810.04805,2018.
89

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[264] Chia-ChengLiu,HarrisChan,KevinLuk,andAIBorealis. Auto-regressivegraphgenerationmodelingwith
improved evaluation methods. In 33rd Conference on Neural Information Processing Systems. Vancouver,
Canada,2019.
[265] JieFeng,XueliangFeng,JiantongChen,XianghaiCao,XiangrongZhang,LichengJiao,andTaoYu. Gener-
ativeadversarialnetworksbasedoncollaborativelearningandattentionmechanismforhyperspectralimage
classification. RemoteSensing,12:1149,042020.
[266] Olivier Breuleux, Yoshua Bengio, and Pascal Vincent. Quickly generating representative samples from an
rbm-derivedprocess. Neuralcomputation,23(8):2058–2073,2011.
[267] AlecRadford,LukeMetz,andSoumithChintala. Unsupervisedrepresentationlearningwithdeepconvolutional
generativeadversarialnetworks. arXivpreprintarXiv:1511.06434,2015.
[268] Maayan Frid-Adar, Eyal Klang, Michal Amitai, Jacob Goldberger, and Hayit Greenspan. Synthetic data
augmentationusingganforimprovedliverlesionclassification. In2018IEEE15thinternationalsymposiumon
biomedicalimaging(ISBI2018),pages289–293.IEEE,2018.
[269] LukeMetz,BenPoole,DavidPfau,andJaschaSohl-Dickstein. Unrolledgenerativeadversarialnetworks. arXiv
preprintarXiv:1611.02163,2016.
[270] AhmedElgammal,BingchenLiu,MohamedElhoseiny,andMarianMazzone.Can:Creativeadversarialnetworks,
generating"art"bylearningaboutstylesanddeviatingfromstylenorms. arXivpreprintarXiv:1706.07068,2017.
[271] Chris Donahue, Julian McAuley, and Miller Puckette. Adversarial audio synthesis. arXiv preprint
arXiv:1802.04208,2018.
[272] IshanDurugkar,IanGemp,andSridharMahadevan. Generativemulti-adversarialnetworks. arXivpreprint
arXiv:1611.01673,2016.
[273] TongChe,YanranLi,AthulPaulJacob,YoshuaBengio,andWenjieLi. Moderegularizedgenerativeadversarial
networks. arXivpreprintarXiv:1612.02136,2016.
[274] JiajunWu,ChengkaiZhang,TianfanXue,BillFreeman,andJoshTenenbaum. Learningaprobabilisticlatent
space of object shapes via 3d generative-adversarial modeling. Advances in neural information processing
systems,29,2016.
[275] YizheZhang,ZheGan,andLawrenceCarin. Generatingtextviaadversarialtraining. InNIPSworkshopon
AdversarialTraining,volume21,pages21–32,2016.
[276] YizheZhang,ZheGan,KaiFan,ZhiChen,RicardoHenao,DinghanShen,andLawrenceCarin. Adversarial
feature matching for text generation. In International Conference on Machine Learning, pages 4006–4015.
PMLR,2017.
[277] Ming-Yu Liu and Oncel Tuzel. Coupled generative adversarial networks. Advances in neural information
processingsystems,29,2016.
[278] JunboZhao,MichaelMathieu,andYannLeCun. Energy-basedgenerativeadversarialnetwork. arXivpreprint
arXiv:1609.03126,2016.
[279] Yann LeCun, Sumit Chopra, Raia Hadsell, M Ranzato, and F Huang. A tutorial on energy-based learning.
Predictingstructureddata,1(0),2006.
[280] Olof Mogren. C-rnn-gan: Continuous recurrent neural networks with adversarial training. arXiv preprint
arXiv:1611.09904,2016.
[281] AndrewBrock,TheodoreLim,JamesMRitchie,andNickWeston. Neuralphotoeditingwithintrospective
adversarialnetworks. arXivpreprintarXiv:1609.07093,2016.
[282] Sebastian Nowozin, Botond Cseke, and Ryota Tomioka. f-gan: Training generative neural samplers using
variationaldivergenceminimization. Advancesinneuralinformationprocessingsystems,29,2016.
[283] DanielJiwoongIm,ChrisDongjooKim,HuiJiang,andRolandMemisevic. Generatingimageswithrecurrent
adversarialnetworks. arXivpreprintarXiv:1602.05110,2016.
[284] Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, Xi Chen, and Xi Chen.
Improvedtechniquesfortraininggans. InD.Lee,M.Sugiyama,U.Luxburg,I.Guyon,andR.Garnett,editors,
AdvancesinNeuralInformationProcessingSystems,volume29.CurranAssociates,Inc.,2016.
[285] MartinArjovsky,SoumithChintala,andLéonBottou. Wassersteingenerativeadversarialnetworks. InInterna-
tionalconferenceonmachinelearning,pages214–223.PMLR,2017.
[286] IshaanGulrajani,FarukAhmed,MartinArjovsky,VincentDumoulin,andAaronCCourville. Improvedtraining
ofwassersteingans. Advancesinneuralinformationprocessingsystems,30,2017.
90

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[287] David Berthelot, Thomas Schumm, and Luke Metz. Began: Boundary equilibrium generative adversarial
networks. arXivpreprintarXiv:1703.10717,2017.
[288] XudongMao,QingLi,HaoranXie,RaymondYKLau,ZhenWang,andStephenPaulSmolley. Leastsquares
generativeadversarialnetworks. InProceedingsoftheIEEEinternationalconferenceoncomputervision,pages
2794–2802,2017.
[289] KevinLin,DianqiLi,XiaodongHe,ZhengyouZhang,andMing-TingSun. Adversarialrankingforlanguage
generation. Advancesinneuralinformationprocessingsystems,30,2017.
[290] PaulinaGrnarova,KfirYLevy,AurelienLucchi,ThomasHofmann,andAndreasKrause. Anonlinelearning
approachtogenerativeadversarialnetworks. arXivpreprintarXiv:1706.03269,2017.
[291] YoonKim,KellyZhang,AlexanderMRush,YannLeCun,etal. Adversariallyregularizedautoencodersfor
generatingdiscretestructures. arXivpreprintarXiv:1706.04223,2:12,2017.
[292] Youssef Mroueh, Tom Sercu, and Vaibhava Goel. Mcgan: Mean and covariance feature matching gan. In
Internationalconferenceonmachinelearning,pages2527–2535.PMLR,2017.
[293] YoussefMrouehandTomSercu. Fishergan. AdvancesinNeuralInformationProcessingSystems,30,2017.
[294] MihaelaRosca,BalajiLakshminarayanan,DavidWarde-Farley,andShakirMohamed. Variationalapproaches
forauto-encodinggenerativeadversarialnetworks. arXivpreprintarXiv:1706.04987,2017.
[295] LantaoYu,WeinanZhang,JunWang,andYongYu. Seqgan: Sequencegenerativeadversarialnetswithpolicy
gradient. InProceedingsoftheAAAIconferenceonartificialintelligence,volume31,2017.
[296] Sang-gilLee,UiwonHwang,SeonwooMin,andSungrohYoon. Aseqganforpolyphonicmusicgeneration.
2017.
[297] MasakiSaito,EiichiMatsumoto,andShuntaSaito. Temporalgenerativeadversarialnetswithsingularvalue
clipping. InProceedingsoftheIEEEinternationalconferenceoncomputervision,pages2830–2839,2017.
[298] AkashSrivastava,LazarValkov,ChrisRussell,MichaelUGutmann,andCharlesSutton. Veegan: Reducing
modecollapseingansusingimplicitvariationallearning. Advancesinneuralinformationprocessingsystems,
30,2017.
[299] RDevonHjelm,AthulPaulJacob,TongChe,AdamTrischler,KyunghyunCho,andYoshuaBengio. Boundary-
seekinggenerativeadversarialnetworks. arXivpreprintarXiv:1702.08431,2017.
[300] Edward Choi, Siddharth Biswal, Bradley Malin, Jon Duke, Walter F Stewart, and Jimeng Sun. Generating
multi-labeldiscretepatientrecordsusinggenerativeadversarialnetworks. InMachinelearningforhealthcare
conference,pages286–305.PMLR,2017.
[301] Li-ChiaYang,Szu-YuChou,andYi-HsuanYang. Midinet: Aconvolutionalgenerativeadversarialnetworkfor
symbolic-domainmusicgeneration. arXivpreprintarXiv:1703.10847,2017.
[302] VincentDumoulinandFrancescoVisin. Aguidetoconvolutionarithmeticfordeeplearning. arXivpreprint
arXiv:1603.07285,2016.
[303] TeroKarras,TimoAila,SamuliLaine,andJaakkoLehtinen. Progressivegrowingofgansforimprovedquality,
stability,andvariation. arXivpreprintarXiv:1710.10196,2017.
[304] Naveen Kodali, Jacob Abernethy, James Hays, and Zsolt Kira. How to train your dragan. arXiv preprint
arXiv:1705.07215,2(4),2017.
[305] FelixJuefei-Xu,VishnuNareshBoddeti,andMariosSavvides. Gangofgans: Generativeadversarialnetworks
withmaximummarginranking. arXivpreprintarXiv:1704.04865,2017.
[306] JiaxianGuo,SidiLu,HanCai,WeinanZhang,YongYu,andJunWang. Longtextgenerationviaadversarial
trainingwithleakedinformation. arXivpreprintarXiv:1709.08624,2017.
[307] VincentDumoulin,IshmaelBelghazi,BenPoole,OlivierMastropietro,AlexLamb,MartinArjovsky,andAaron
Courville. Adversariallylearnedinference. arXivpreprintarXiv:1606.00704,2016.
[308] JianweiYang,AnithaKannan,DhruvBatra,andDeviParikh. Lr-gan: Layeredrecursivegenerativeadversarial
networksforimagegeneration. arXivpreprintarXiv:1703.01560,2017.
[309] DavidWarde-FarleyandYoshuaBengio. Improvinggenerativeadversarialnetworkswithdenoisingfeature
matching. InInternationalConferenceonLearningRepresentations,2017.
[310] MartinHeusel,HubertRamsauer,ThomasUnterthiner,BernhardNessler,andSeppHochreiter. Ganstrained
byatwotime-scaleupdateruleconvergetoalocalnashequilibrium. InI.Guyon,U.VonLuxburg,S.Bengio,
H.Wallach,R.Fergus,S.Vishwanathan,andR.Garnett,editors,AdvancesinNeuralInformationProcessing
Systems,volume30.CurranAssociates,Inc.,2017.
91

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[311] SergeyTulyakov,Ming-YuLiu,XiaodongYang,andJanKautz. Mocogan: Decomposingmotionandcontentfor
videogeneration. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages
1526–1535,2018.
[312] Hao-WenDong,Wen-YiHsiao,Li-ChiaYang,andYi-HsuanYang. Musegan: Multi-tracksequentialgenerative
adversarialnetworksforsymbolicmusicgenerationandaccompaniment. InProceedingsoftheAAAIConference
onArtificialIntelligence,volume32,2018.
[313] AyushJaiswal,WaelAbdAlmageed,YueWu,andPremkumarNatarajan. Capsulegan: Generativeadversarial
capsulenetwork. InProceedingsoftheEuropeanconferenceoncomputervision(ECCV)workshops,pages0–0,
2018.
[314] SaraSabour,NicholasFrosst,andGeoffreyEHinton. Dynamicroutingbetweencapsules. Advancesinneural
informationprocessingsystems,30,2017.
[315] NicolaDeCaoandThomasKipf. Molgan: Animplicitgenerativemodelforsmallmoleculargraphs. arXiv
preprintarXiv:1805.11973,2018.
[316] AleksandarBojchevski,OleksandrShchur,DanielZügner,andStephanGünnemann. Netgan: Generatinggraphs
viarandomwalks. InInternationalconferenceonmachinelearning,pages610–619.PMLR,2018.
[317] NoseongPark,MahmoudMohammadi,KshitijGorde,SushilJajodia,HongkyuPark,andYoungminKim. Data
synthesisbasedongenerativeadversarialnetworks. arXivpreprintarXiv:1806.03384,2018.
[318] ShreyasPatel,AshutoshKakadiya,MaitreyMehta,RajDerasari,RahulPatel,andRatnikGandhi. Correlated
discretedatagenerationusingadversarialtraining. arXivpreprintarXiv:1804.00925,2018.
[319] LeiXuandKalyanVeeramachaneni. Synthesizingtabulardatausinggenerativeadversarialnetworks. arXiv
preprintarXiv:1811.11264,2018.
[320] XiangWei,BoqingGong,ZixiaLiu,WeiLu,andLiqiangWang. Improvingtheimprovedtrainingofwasserstein
gans: Aconsistencytermanditsdualeffect. arXivpreprintarXiv:1803.01541,2018.
[321] AshishBora,EricPrice,andAlexandrosGDimakis. Ambientgan: Generativemodelsfromlossymeasurements.
InInternationalconferenceonlearningrepresentations,2018.
[322] NamrataAnandandPossuHuang. Generativemodelingforproteinstructures. Advancesinneuralinformation
processingsystems,31,2018.
[323] KunOuyang,RezaShokri,DavidSRosenblum,andWenzhuoYang. Anon-parametricgenerativemodelfor
humantrajectories. InIJCAI,volume18,pages3812–3817,2018.
[324] QuanHoang,TuDinhNguyen,TrungLe,andDinhPhung. MGAN:Traininggenerativeadversarialnetswith
multiplegenerators. InInternationalConferenceonLearningRepresentations,2018.
[325] Weili Nie, Nina Narodytska, and Ankit Patel. Relgan: Relational generative adversarial networks for text
generation. InInternationalconferenceonlearningrepresentations,2018.
[326] Ngoc-TrungTran,Tuan-AnhBui,andNgai-ManCheung. Dist-gan: Animprovedganusingdistanceconstraints.
InProceedingsoftheEuropeanConferenceonComputerVision(ECCV),September2018.
[327] TakeruMiyato,ToshikiKataoka,MasanoriKoyama,andYuichiYoshida. Spectralnormalizationforgenerative
adversarialnetworks. arXivpreprintarXiv:1802.05957,2018.
[328] HaoHe,HaoWang,Guang-HeLee,andYonglongTian. Bayesianmodellingandmontecarloinferencefor
GAN. InInternationalConferenceonLearningRepresentations,2019.
[329] AudeGenevay,GabrielPeyre,andMarcoCuturi. Learninggenerativemodelswithsinkhorndivergences. In
AmosStorkeyandFernandoPerez-Cruz,editors,ProceedingsoftheTwenty-FirstInternationalConferenceon
ArtificialIntelligenceandStatistics,volume84ofProceedingsofMachineLearningResearch,pages1608–1617.
PMLR,09–11Apr2018.
[330] Tero Karras, Samuli Laine, and Timo Aila. A style-based generator architecture for generative adversarial
networks. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages
4401–4410,2019.
[331] JamesJordon,JinsungYoon,andMihaelaVanDerSchaar. Pate-gan: Generatingsyntheticdatawithdifferential
privacyguarantees. InInternationalconferenceonlearningrepresentations,2018.
[332] Nicolas Papernot, Shuang Song, Ilya Mironov, Ananth Raghunathan, Kunal Talwar, and Úlfar Erlingsson.
Scalableprivatelearningwithpate. arXivpreprintarXiv:1802.08908,2018.
[333] XingyuanChen, YanzheLi, PengJin, JiuhuaZhang, XinyuDai, JiajunChen, andGangSong. Adversarial
sub-sequencefortextgeneration. arXivpreprintarXiv:1905.12835,2019.
92

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[334] EmanueleGhelfi,PaoloGaleone,MicheleDeSimoni,andFedericoDiMattia. Adversarialpixel-levelgeneration
ofsemanticimages. arXivpreprintarXiv:1906.12195,2019.
[335] PhillipIsola,Jun-YanZhu,TinghuiZhou,andAlexeiAEfros. Image-to-imagetranslationwithconditional
adversarialnetworks. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages
1125–1134,2017.
[336] MrinalKantiBaowaly,Chia-ChingLin,Chao-LinLiu,andKuan-TaChen.Synthesizingelectronichealthrecords
usingimprovedgenerativeadversarialnetworks. JournaloftheAmericanMedicalInformaticsAssociation,
26(3):228–241,2019.
[337] PooyanSedigh,RasoulSadeghian,andMehdiTaleMasouleh. Generatingsyntheticmedicalimagesbyusing
gantoimprovecnnperformanceinskincancerclassification. In20197thInternationalConferenceonRobotics
andMechatronics(ICRoM),pages497–502.IEEE,2019.
[338] Xinyu Gong, Shiyu Chang, Yifan Jiang, and Zhangyang Wang. Autogan: Neural architecture search for
generativeadversarialnetworks. InProceedingsoftheIEEE/CVFInternationalConferenceonComputerVision
(ICCV),October2019.
[339] ZinanLin,AlankarJain,ChenWang,GiuliaC.Fanti,andVyasSekar. Generatinghigh-fidelity,synthetictime
seriesdatasetswithdoppelganger. arXivpreprint,September2019.
[340] Jinsung Yoon, Daniel Jarrett, and Mihaela van der Schaar. Time-series generative adversarial networks. In
H.Wallach,H.Larochelle,A.Beygelzimer,F.d'Alché-Buc,E.Fox,andR.Garnett,editors,AdvancesinNeural
InformationProcessingSystems,volume32.CurranAssociates,Inc.,2019.
[341] TeroKarras, SamuliLaine, MiikaAittala, JanneHellsten, JaakkoLehtinen, andTimoAila. Analyzingand
improvingtheimagequalityofstylegan. InProceedingsoftheIEEE/CVFconferenceoncomputervisionand
patternrecognition,pages8110–8119,2020.
[342] AndrewYale,SaloniDash,RitikDutta,IsabelleGuyon,AdrienPavao,andKristinPBennett. Generationand
evaluationofprivacypreservingsynthetichealthdata. Neurocomputing,416:244–255,2020.
[343] SaadiaBinteAlam,MoazzemHossain,andSyojiKobashi. Syntheticbrainimagegenerationforadhdprediction
basedonprogressivegrowinggenerativeadversarialnetwork. InInternationalSymposiumonAffectiveScience
andEngineeringISASE2020,pages1–5.JapanSocietyofKanseiEngineering,2020.
[344] JyotiIslamandYanqingZhang. Gan-basedsyntheticbrainpetimagegeneration. Braininformatics,7(1):1–12,
2020.
[345] DebapriyaHazraandYung-CheolByun. Synsiggan: Generativeadversarialnetworksforsyntheticbiomedical
signalgeneration. Biology,9(12):441,2020.
[346] ChenGao, YunpengChen, SiLiu, ZhenxiongTan, andShuichengYan. Adversarialnas: Adversarialneural
architecturesearchforgans. InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern
Recognition(CVPR),June2020.
[347] TianlinXu,LiKevinWenliang,MichaelMunn,andBeatriceAcciaio. Cot-gan: Generatingsequentialdatavia
causaloptimaltransport. InH.Larochelle,M.Ranzato,R.Hadsell,M.F.Balcan,andH.Lin,editors,Advances
inNeuralInformationProcessingSystems,volume33,pages8798–8809.CurranAssociates,Inc.,2020.
[348] ShengyuZhao,ZhijianLiu,JiLin,Jun-YanZhu,andSongHan. Differentiableaugmentationfordata-efficient
gantraining. InH.Larochelle,M.Ranzato,R.Hadsell,M.F.Balcan,andH.Lin,editors,AdvancesinNeural
InformationProcessingSystems,volume33,pages7559–7570.CurranAssociates,Inc.,2020.
[349] ChristineDewi,Rung-ChingChen,Yan-TingLiu,andShao-KuoTai. Syntheticdatagenerationusingdcganfor
improvedtrafficsignrecognition. NeuralComputingandApplications,pages1–16,2021.
[350] SanaImtiaz,MuhammadArsalan,VladimirVlassov,andRaminSadre. Syntheticandprivatesmarthealthcare
datagenerationusinggans. In2021InternationalConferenceonComputerCommunicationsandNetworks
(ICCCN),pages1–7.IEEE,2021.
[351] VajiraThambawita,JonasLIsaksen,StevenAHicks,JonasGhouse,GustavAhlberg,AllanLinneberg,Niels
Grarup,ChristinaEllervik,MortenSallingOlesen,TorbenHansen,etal. Deepfakeelectrocardiogramsusing
generativeadversarialnetworksarethebeginningoftheendforprivacyissuesinmedicine. Scientificreports,
11(1):1–8,2021.
[352] XiaominLi,VangelisMetsis,HuangyingruiWang,andAnneHeeHiongNgu. Tts-gan: Atransformer-based
time-seriesgenerativeadversarialnetwork. InMartinMichalowski,SyedSibteRazaAbidi,andSaminaAbidi,
editors,ArtificialIntelligenceinMedicine,pages133–143,Cham,2022.SpringerInternationalPublishing.
93

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[353] MehdiMirzaandSimonOsindero. Conditionalgenerativeadversarialnets. arXivpreprintarXiv:1411.1784,
2014.
[354] MichaelMathieu,CamilleCouprie,andYannLeCun. Deepmulti-scalevideopredictionbeyondmeansquare
error. arXivpreprintarXiv:1511.05440,2015.
[355] Jun-YanZhu,PhilippKrähenbühl,EliShechtman,andAlexeiAEfros. Generativevisualmanipulationonthe
naturalimagemanifold. InEuropeanconferenceoncomputervision,pages597–613.Springer,2016.
[356] ScottReed,ZeynepAkata,XinchenYan,LajanugenLogeswaran,BerntSchiele,andHonglakLee. Generative
adversarialtexttoimagesynthesis. InInternationalconferenceonmachinelearning,pages1060–1069.PMLR,
2016.
[357] ScottEReed,ZeynepAkata,SantoshMohan,SamuelTenka,BerntSchiele,andHonglakLee. Learningwhat
andwheretodraw. Advancesinneuralinformationprocessingsystems,29,2016.
[358] YunjeyChoi,MinjeChoi,MunyoungKim,Jung-WooHa,SunghunKim,andJaegulChoo. Stargan: Unified
generativeadversarialnetworksformulti-domainimage-to-imagetranslation. arXivpreprintarXiv:1711.09020,
2017.
[359] Jun-Yan Zhu, Taesung Park, Phillip Isola, and Alexei A Efros. Unpaired image-to-image translation using
cycle-consistentadversarialnetworks. InProceedingsoftheIEEEinternationalconferenceoncomputervision,
pages2223–2232,2017.
[360] MuratKocaoglu,ChristopherSnyder,AlexandrosGDimakis,andSriramVishwanath. Causalgan: Learning
causalimplicitgenerativemodelswithadversarialtraining. arXivpreprintarXiv:1709.02023,2017.
[361] Han Zhang, Ian Goodfellow, Dimitris Metaxas, and Augustus Odena. Self-attention generative adversarial
networks. InInternationalconferenceonmachinelearning,pages7354–7363.PMLR,2019.
[362] AugustusOdena,ChristopherOlah,andJonathonShlens. Conditionalimagesynthesiswithauxiliaryclassifier
gans. InInternationalconferenceonmachinelearning,pages2642–2651.PMLR,2017.
[363] ArjunKrishnaandKlausMueller. Medical(ct)imagegenerationwithstyle. In15thInternationalMeeting
onFullyThree-DimensionalImageReconstructioninRadiologyandNuclearMedicine,volume11072,page
1107234.InternationalSocietyforOpticsandPhotonics,2019.
[364] Eloi Alonso, Bastien Moysset, and Ronaldo Messina. Adversarial generation of handwritten text images
conditionedonsequences. In2019internationalconferenceondocumentanalysisandrecognition(ICDAR),
pages481–486.IEEE,2019.
[365] AndrewBrock,JeffDonahue,andKarenSimonyan. Largescalegantrainingforhighfidelitynaturalimage
synthesis. arXivpreprintarXiv:1809.11096,2019.
[366] MarioLucˇic´,MichaelTschannen,MarvinRitter,XiaohuaZhai,OlivierBachem,andSylvainGelly. High-fidelity
imagegenerationwithfewerlabels. InInternationalconferenceonmachinelearning,pages4183–4192.PMLR,
2019.
[367] JonGauthier.Conditionalgenerativeadversarialnetsforconvolutionalfacegeneration.ClassprojectforStanford
CS231N:convolutionalneuralnetworksforvisualrecognition,Wintersemester,2014(5):2,2014.
[368] JostTobiasSpringenberg. Unsupervisedandsemi-supervisedlearningwithcategoricalgenerativeadversarial
networks. arXivpreprintarXiv:1511.06390,2015.
[369] GuimPerarnau,JoostVanDeWeijer,BogdanRaducanu,andJoseMÁlvarez. Invertibleconditionalgansfor
imageediting. arXivpreprintarXiv:1611.06355,2016.
[370] LeventKaracan,ZeynepAkata,AykutErdem,andErkutErdem. Learningtogenerateimagesofoutdoorscenes
fromattributesandsemanticlayouts. arXivpreprintarXiv:1612.00215,2016.
[371] CarlVondrick,HamedPirsiavash,andAntonioTorralba. Generatingvideoswithscenedynamics. Advancesin
neuralinformationprocessingsystems,29,2016.
[372] AshishShrivastava,TomasPfister,OncelTuzel,JoshuaSusskind,WendaWang,andRussellWebb. Learning
fromsimulatedandunsupervisedimagesthroughadversarialtraining. InProceedingsoftheIEEEconferenceon
computervisionandpatternrecognition,pages2107–2116,2017.
[373] KianaEhsani, RoozbehMottaghi, andAliFarhadi. Segan: Segmentingandgeneratingtheinvisible. arXiv
preprintarXiv:1703.10239,2017.
[374] KaimingHe,XiangyuZhang,ShaoqingRen,andJianSun. Deepresiduallearningforimagerecognition. In
ProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages770–778,2016.
94

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[375] KonstantinosBousmalis,NathanSilberman,DavidDohan,DumitruErhan,andDilipKrishnan. Unsupervised
pixel-leveldomainadaptationwithgenerativeadversarialnetworks. InProceedingsoftheIEEEconferenceon
computervisionandpatternrecognition,pages3722–3731,2017.
[376] YuanXue,TaoXu,HanZhang,RodneyLong,andXiaoleiHuang. Segan: Adversarialnetworkwithmulti-scale
l_1lossformedicalimagesegmentation. arXivpreprintarXiv:1706.01805,2017.
[377] ZiliYi,HaoZhang,PingTan,andMinglunGong. Dualgan: Unsupervisedduallearningforimage-to-image
translation. InProceedingsoftheIEEEinternationalconferenceoncomputervision,pages2849–2857,2017.
[378] DenisVolkhonskiy,IvanNazarov,andEvgenyBurnaev. Steganographicgenerativeadversarialnetworks. arXiv
preprintarXiv:1703.05502,2017.
[379] ChristianLedig,LucasTheis,FerencHuszár,JoseCaballero,AndrewCunningham,AlejandroAcosta,Andrew
Aitken,AlykhanTejani,JohannesTotz,ZehanWang,etal. Photo-realisticsingleimagesuper-resolutionusing
a generative adversarial network. In Proceedings of the IEEE conference on computer vision and pattern
recognition,pages4681–4690,2017.
[380] Chin-Cheng Hsu, Hsin-Te Hwang, Yi-Chiao Wu, Yu Tsao, and Hsin-Min Wang. Voice conversion from
unalignedcorporausingvariationalautoencodingwassersteingenerativeadversarialnetworks. arXivpreprint
arXiv:1704.00849,2017.
[381] Chongxuan Li, Taufik Xu, Jun Zhu, and Bo Zhang. Triple generative adversarial nets. Advances in neural
informationprocessingsystems,30,2017.
[382] CristóbalEsteban,StephanieLHyland,andGunnarRätsch. Real-valued(medical)timeseriesgenerationwith
recurrentconditionalgans. arXivpreprintarXiv:1706.02633,2017.
[383] ArnabGhosh,VivekaKulharia,VinayNamboodiri,PhilipHSTorr,andPuneetKDokania. Multi-agentdiverse
generativeadversarialnetworks. arXivpreprintarXiv:1704.02906,2017.
[384] Mahesh Gorijala and Ambedkar Dukkipati. Image generation and editing with variational info generative
adversarialnetworks. arXivpreprintarXiv:1701.04568,2017.
[385] WDai,JDoyle,XLiang,HZhang,NDong,YLi,andEPXing. Scan: Structurecorrectingadversarialnetwork
forchestx-raysorgansegmentation. arXivpreprintarXiv:1703.08770,2017.
[386] Hao Dong, Simiao Yu, Chao Wu, and Yike Guo. Semantic image synthesis via adversarial learning. In
ProceedingsoftheIEEEinternationalconferenceoncomputervision,pages5706–5714,2017.
[387] Jun-YanZhu,RichardZhang,DeepakPathak,TrevorDarrell,AlexeiAEfros,OliverWang,andEliShechtman.
Towardmultimodalimage-to-imagetranslation. Advancesinneuralinformationprocessingsystems,30,2017.
[388] Ming-YuLiu,ThomasBreuel,andJanKautz. Unsupervisedimage-to-imagetranslationnetworks. Advancesin
neuralinformationprocessingsystems,30,2017.
[389] YongyiLu,Yu-WingTai,andChi-KeungTang. Conditionalcycleganforattributeguidedfaceimagegeneration.
arXivpreprintarXiv:1705.09966,2,2017.
[390] GuillermoLGrinblat,LucasCUzal,andPabloMGranitto. Class-splittinggenerativeadversarialnetworks.
arXivpreprintarXiv:1709.07359,2017.
[391] Lichao Zhang, Abel Gonzalez-Garcia, Joost Van De Weijer, Martin Danelljan, and Fahad Shahbaz Khan.
Syntheticdatagenerationforend-to-endthermalinfraredtracking. IEEETransactionsonImageProcessing,
28(4):1837–1850,2018.
[392] ChaoyueWang,ChangXu,ChaohuiWang,andDachengTao. Perceptualadversarialnetworksforimage-to-
imagetransformation. IEEETransactionsonImageProcessing,27(8):4066–4079,2018.
[393] SeonghyeonNam,YunjiKim,andSeonJooKim. Text-adaptivegenerativeadversarialnetworks: manipulating
imageswithnaturallanguage. Advancesinneuralinformationprocessingsystems,31,2018.
[394] PiotrBojanowski,EdouardGrave,ArmandJoulin,andTomasMikolov. Enrichingwordvectorswithsubword
information. Transactionsoftheassociationforcomputationallinguistics,5:135–146,2017.
[395] Ting-Chun Wang, Ming-Yu Liu, Jun-Yan Zhu, Guilin Liu, Andrew Tao, Jan Kautz, and Bryan Catanzaro.
Video-to-videosynthesis. arXivpreprintarXiv:1808.06601,2018.
[396] DanielSáezTrigueros,LiMeng,andMargaretHartnett. Generatingphoto-realistictrainingdatatoimproveface
recognitionaccuracy. arXivpreprintarXiv:1811.00112,2018.
[397] BarisGecer,BinodBhattarai,JosefKittler,andTae-KyunKim. Semi-supervisedadversariallearningtogenerate
photorealisticfaceimagesofnewidentitiesfrom3dmorphablemodel.InProceedingsoftheEuropeanconference
oncomputervision(ECCV),pages217–234,2018.
95

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[398] XiaojieGuo,LingfeiWu,andLiangZhao. Deepgraphtranslation. arXivpreprintarXiv:1805.09980,2018.
[399] WilliamFedus,IanGoodfellow,andAndrewMDai. Maskgan: bettertextgenerationviafillinginthe_. arXiv
preprintarXiv:1801.07736,2018.
[400] Hoo-ChangShin,NeilATenenholtz,JamesonKRogers,ChristopherGSchwarz,MatthewLSenjem,JeffreyL
Gunter, Katherine P Andriole, and Mark Michalski. Medical image synthesis for data augmentation and
anonymizationusinggenerativeadversarialnetworks. InInternationalworkshoponsimulationandsynthesisin
medicalimaging,pages1–11.Springer,2018.
[401] Aleksei Triastcyn and Boi Faltings. Generating artificial data for private deep learning. arXiv preprint
arXiv:1803.03148,2018.
[402] Jesse Engel, Kumar Krishna Agrawal, Shuo Chen, Ishaan Gulrajani, Chris Donahue, and Adam Roberts.
Gansynth: Adversarialneuralaudiosynthesis. arXivpreprintarXiv:1902.08710,2019.
[403] ShuangfeiFanandBertHuang.Labeledgraphgenerativeadversarialnetworks.arXivpreprintarXiv:1906.03220,
2019.
[404] ReihanehTorkzadehmahani,PeterKairouz,andBenedictPaten. Dp-cgan: Differentiallyprivatesyntheticdata
andlabelgeneration. InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition
Workshops,pages0–0,2019.
[405] IlyaMironov. Rényidifferentialprivacy. In2017IEEE30thcomputersecurityfoundationssymposium(CSF),
pages263–275.IEEE,2017.
[406] DaweiZhou,LechengZheng,JiejunXu,andJingruiHe. Misc-gan: Amulti-scalegenerativemodelforgraphs.
FrontiersinbigData,2:3,2019.
[407] Chieh Hubert Lin, Chia-Che Chang, Yu-Sheng Chen, Da-Cheng Juan, Wei Wei, and Hwann-Tzong Chen.
Coco-gan: Generationbypartsviaconditionalcoordinating. InProceedingsoftheIEEE/CVFInternational
ConferenceonComputerVision(ICCV),October2019.
[408] KarimArmanious,ChenmingJiang,MarcFischer,ThomasKüstner,TobiasHepp,KonstantinNikolaou,Sergios
Gatidis,andBinYang. Medgan: Medicalimagetranslationusinggans. Computerizedmedicalimagingand
graphics,79,2020.
[409] ŁukaszMaziarka,AgnieszkaPocha,JanKaczmarczyk,KrzysztofRataj,TomaszDanel,andMichałWarchoł.
Mol-cyclegan: agenerativemodelformolecularoptimization. JournalofCheminformatics,12(1):1–18,2020.
[410] SinaRashidian,FushengWang,RichardMoffitt,VictorGarcia,AnuragDutt,WeiChang,VishwamPandya,
JanosHajagos,MarySaltz,andJoelSaltz. Smooth-gan: towardssharpandsmoothsyntheticehrdatageneration.
InInternationalConferenceonArtificialIntelligenceinMedicine,pages37–48.Springer,2020.
[411] SalihSarp,MuratKuzlu,EmmanuelWilson,andOzgurGuler. Wg2an: Syntheticwoundimagegenerationusing
generativeadversarialnetwork. TheJournalofEngineering,2021(5):286–294,2021.
[412] JavariaAmin,MuhammadSharif,NadiaGul,SeifedineKadry,andChinmayChakraborty. Quantummachine
learningarchitectureforcovid-19classificationbasedonsyntheticdatagenerationusingconditionaladversarial
neuralnetwork. CognitiveComputation,pages1–12,2021.
[413] EmilyLDenton,SoumithChintala,RobFergus,etal. Deepgenerativeimagemodelsusingalaplacianpyramid
ofadversarialnetworks. Advancesinneuralinformationprocessingsystems,28,2015.
[414] HanZhang,TaoXu,HongshengLi,ShaotingZhang,XiaogangWang,XiaoleiHuang,andDimitrisNMetaxas.
Stackgan: Texttophoto-realisticimagesynthesiswithstackedgenerativeadversarialnetworks. InProceedings
oftheIEEEinternationalconferenceoncomputervision,pages5907–5915,2017.
[415] XunHuang,YixuanLi,OmidPoursaeed,JohnHopcroft,andSergeBelongie. Stackedgenerativeadversarial
networks. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages5077–5086,
2017.
[416] John T Guibas, Tejpal S Virdi, and Peter S Li. Synthetic medical images from dual generative adversarial
networks. arXivpreprintarXiv:1709.01872,2017.
[417] YifanJiang,ShiyuChang,andZhangyangWang. Transgan: Twopuretransformerscanmakeonestronggan,
andthatcanscaleup. InM.Ranzato,A.Beygelzimer,Y.Dauphin,P.S.Liang,andJ.WortmanVaughan,editors,
AdvancesinNeuralInformationProcessingSystems,volume34,pages14745–14758.CurranAssociates,Inc.,
2021.
[418] Jeff Donahue, Philipp Krähenbühl, and Trevor Darrell. Adversarial feature learning. arXiv preprint
arXiv:1605.09782,2016.
96

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[419] VincentDumoulin,IshmaelBelghazi,BenPoole,OlivierMastropietro,AlexLamb,MartinArjovsky,andAaron
Courville. Adversariallylearnedinference. arXivpreprintarXiv:1606.00704,2016.
[420] Jeff Donahue and Karen Simonyan. Large scale adversarial representation learning. Advances in neural
informationprocessingsystems,32,2019.
[421] AlirezaMakhzani,JonathonShlens,NavdeepJaitly,IanGoodfellow,andBrendanFrey.Adversarialautoencoders.
arXivpreprintarXiv:1511.05644,2015.
[422] YujiaLi,KevinSwersky,andRichZemel. Generativemomentmatchingnetworks. InInternationalconference
onmachinelearning,pages1718–1727.PMLR,2015.
[423] IlyaTolstikhin,OlivierBousquet,SylvainGelly,andBernhardSchoelkopf. Wassersteinauto-encoders. arXiv
preprintarXiv:1711.01558,2017.
[424] ArturKadurin,AlexanderAliper,AndreyKazennov,PolinaMamoshina,QuentinVanhaelen,KuzmaKhrabrov,
andAlexZhavoronkov. Thecornucopiaofmeaningfulleads: Applyingdeepadversarialautoencodersfornew
moleculedevelopmentinoncology. Oncotarget,8(7):10883,2017.
[425] ArturKadurin,SergeyNikolenko,KuzmaKhrabrov,AlexAliper,andAlexZhavoronkov. drugan: anadvanced
generative adversarial autoencoder model for de novo generation of new molecules with desired molecular
propertiesinsilico. Molecularpharmaceutics,14(9):3098–3104,2017.
[426] PedroCosta,AdrianGaldran,MariaInesMeyer,MeindertNiemeijer,MichaelAbràmoff,AnaMariaMendonça,
andAurélioCampilho. End-to-endadversarialretinalimagesynthesis. IEEEtransactionsonmedicalimaging,
37(3):781–791,2017.
[427] OscarPastor-Serrano,DannyLathouwers,andZoltánPerkó. Asemi-supervisedautoencoderframeworkforjoint
generationandclassificationofbreathing. ComputerMethodsandProgramsinBiomedicine,209:106312,2021.
[428] Chun-LiangLi,Wei-ChengChang,YuCheng,YimingYang,andBarnabásPóczos. Mmdgan: Towardsdeeper
understandingofmomentmatchingnetwork. Advancesinneuralinformationprocessingsystems,30,2017.
[429] GintareKarolinaDziugaite,DanielMRoy,andZoubinGhahramani. Traininggenerativeneuralnetworksvia
maximummeandiscrepancyoptimization. arXivpreprintarXiv:1505.03906,2015.
[430] YongRen,JunZhu,JialianLi,andYucenLuo. Conditionalgenerativemoment-matchingnetworks. Advancesin
NeuralInformationProcessingSystems,29,2016.
[431] ShinnosukeTakamichi,TomokiKoriyama,andHiroshiSaruwatari. Sampling-basedspeechparametergeneration
usingmoment-matchingnetworks. arXivpreprintarXiv:1704.03626,2017.
[432] WeiWang,YuanSun,andSamanHalgamuge. Improvingmmd-gantrainingwithrepulsivelossfunction. arXiv
preprintarXiv:1812.09916,2018.
[433] Wenlong Liao, Yusen Wang, Yuelong Wang, Kody Powell, Qi Liu, and Zhe Yang. Scenario generation for
cooling,heating,andpowerloadsusinggenerativemomentmatchingnetworks. CSEEJournalofPowerand
EnergySystems,2022.
[434] AnhNguyen,AlexeyDosovitskiy,JasonYosinski,ThomasBrox,andJeffClune. Synthesizingthepreferred
inputsforneuronsinneuralnetworksviadeepgeneratornetworks. Advancesinneuralinformationprocessing
systems,29,2016.
[435] Anh Nguyen, Jeff Clune, Yoshua Bengio, Alexey Dosovitskiy, and Jason Yosinski. Plug & play generative
networks: Conditionaliterativegenerationofimagesinlatentspace. InProceedingsoftheIEEEconferenceon
computervisionandpatternrecognition,pages4467–4477,2017.
[436] NatasaTagasovska,DamienAckerer,andThibaultVatter. Copulasashigh-dimensionalgenerativemodels: Vine
copulaautoencoders. Advancesinneuralinformationprocessingsystems,32,2019.
[437] VaibhavKulkarni,NatasaTagasovska,ThibaultVatter,andBenoitGarbinato. Generativemodelsforsimulating
mobilitytrajectories. arXivpreprintarXiv:1811.12801,2018.
[438] HaoranLi,LiXiong,andXiaoqianJiang. Differentiallyprivatesynthesizationofmulti-dimensionaldatausing
copulafunctions. InAdvancesindatabasetechnology: proceedings.Internationalconferenceonextending
databasetechnology,volume2014,page475.NIHPublicAccess,2014.
[439] ChenceShi,MinkaiXu,ZhaochengZhu,WeinanZhang,MingZhang,andJianTang. Graphaf: aflow-based
autoregressivemodelformoleculargraphgeneration. arXivpreprintarXiv:2001.09382,2020.
[440] Michael Schlichtkrull, Thomas N Kipf, Peter Bloem, Rianne van den Berg, Ivan Titov, and Max Welling.
Modeling relational data with graph convolutional networks. In European semantic web conference, pages
593–607.Springer,2018.
97

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[441] LaurentDinh,DavidKrueger,andYoshuaBengio. Nice: Non-linearindependentcomponentsestimation. arXiv
preprintarXiv:1410.8516,2014.
[442] LaurentDinh, JaschaSohl-Dickstein, andSamyBengio. Densityestimationusingrealnvp. arXivpreprint
arXiv:1605.08803,2016.
[443] DurkPKingmaandPrafullaDhariwal. Glow: Generativeflowwithinvertible1x1convolutions. Advancesin
neuralinformationprocessingsystems,31,2018.
[444] Ricky TQ Chen, Yulia Rubanova, Jesse Bettencourt, and David K Duvenaud. Neural ordinary differential
equations. Advancesinneuralinformationprocessingsystems,31,2018.
[445] WillGrathwohl,RickyTQChen,JesseBettencourt,IlyaSutskever,andDavidDuvenaud. Ffjord: Free-form
continuousdynamicsforscalablereversiblegenerativemodels. arXivpreprintarXiv:1810.01367,2018.
[446] KaushalyaMadhawa,KatushikoIshiguro,KosukeNakago,andMotokiAbe. Graphnvp: Aninvertibleflow
modelforgeneratingmoleculargraphs. arXivpreprintarXiv:1905.11600,2019.
[447] AhmedAlaa,AlexJamesChan,andMihaelavanderSchaar. Generativetime-seriesmodelingwithfourierflows.
InInternationalConferenceonLearningRepresentations,2021.
[448] VincentFrançois-Lavet,PeterHenderson,RiashatIslam,MarcGBellemare,andJoellePineau. Anintroduction
todeepreinforcementlearning. arXivpreprintarXiv:1811.12560,2018.
[449] Junhyuk Oh, Xiaoxiao Guo, Honglak Lee, Richard L Lewis, and Satinder Singh. Action-conditional video
predictionusingdeepnetworksinatarigames. Advancesinneuralinformationprocessingsystems,28,2015.
[450] BiaoJia, ChenFang, JonathanBrandt, ByungmoonKim, andDineshManocha. Paintbot: Areinforcement
learningapproachfornaturalmediapainting. arXivpreprintarXiv:1904.02201,2019.
[451] ArjunKrishna,KedarBartake,ChuangNiu,GeWang,YoufangLai,XunJia,andKlausMueller. Imagesynthesis
fordataaugmentationinmedicalctusingdeepreinforcementlearning. arXivpreprintarXiv:2103.10493,2021.
[452] JiweiLi,WillMonroe,AlanRitter,MichelGalley,JianfengGao,andDanJurafsky. Deepreinforcementlearning
fordialoguegeneration. arXivpreprintarXiv:1606.01541,2016.
[453] JiweiLi, WillMonroe, TianlinShi, SébastienJean, AlanRitter, andDanJurafsky. Adversariallearningfor
neuraldialoguegeneration. arXivpreprintarXiv:1701.06547,2017.
[454] GabrielLimaGuimaraes,BenjaminSanchez-Lengeling,CarlosOuteiral,PedroLuisCunhaFarias,andAlán
Aspuru-Guzik. Objective-reinforcedgenerativeadversarialnetworks(organ)forsequencegenerationmodels.
arXivpreprintarXiv:1705.10843,2017.
[455] MarcusOlivecrona,ThomasBlaschke,OlaEngkvist,andHongmingChen. Molecularde-novodesignthrough
deepreinforcementlearning. Journalofcheminformatics,9(1):1–14,2017.
[456] Zhan Shi, Xinchi Chen, Xipeng Qiu, and Xuanjing Huang. Toward diverse text generation with inverse
reinforcementlearning. arXivpreprintarXiv:1804.11258,2018.
[457] RonaldJWilliams. Simplestatisticalgradient-followingalgorithmsforconnectionistreinforcementlearning.
Machinelearning,8(3):229–256,1992.
[458] JiaxuanYou,BowenLiu,ZhitaoYing,VijayPande,andJureLeskovec. Graphconvolutionalpolicynetworkfor
goal-directedmoleculargraphgeneration. Advancesinneuralinformationprocessingsystems,31,2018.
[459] Harish Kumar and Balaraman Ravindran. Polyphonic music composition with lstm neural networks and
reinforcementlearning. arXivpreprintarXiv:1902.01973,2019.
[460] DanielJarrett, IoanaBica, andMihaelavanderSchaar. Time-seriesgenerationbycontrastiveimitation. In
M.Ranzato,A.Beygelzimer,Y.Dauphin,P.S.Liang,andJ.WortmanVaughan,editors,AdvancesinNeural
InformationProcessingSystems,volume34,pages28968–28982.CurranAssociates,Inc.,2021.
[461] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. Advances in Neural
InformationProcessingSystems,33:6840–6851,2020.
[462] JaschaSohl-Dickstein,EricWeiss,NiruMaheswaranathan,andSuryaGanguli. Deepunsupervisedlearning
usingnonequilibriumthermodynamics. InInternationalConferenceonMachineLearning,pages2256–2265.
PMLR,2015.
[463] AlexanderQuinnNicholandPrafullaDhariwal. Improveddenoisingdiffusionprobabilisticmodels. InInterna-
tionalConferenceonMachineLearning,pages8162–8171.PMLR,2021.
[464] PrafullaDhariwalandAlexanderNichol. Diffusionmodelsbeatgansonimagesynthesis. AdvancesinNeural
InformationProcessingSystems,34:8780–8794,2021.
98

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[465] AdityaRamesh,PrafullaDhariwal,AlexNichol,CaseyChu,andMarkChen. Hierarchicaltext-conditional
imagegenerationwithcliplatents. arXivpreprintarXiv:2204.06125,2022.
[466] NikolausMayer,EddyIlg,PhilippFischer,CanerHazirbas,DanielCremers,AlexeyDosovitskiy,andThomas
Brox. Whatmakesgoodsynthetictrainingdataforlearningdisparityandopticalflowestimation? International
JournalofComputerVision,126(9):942–960,2018.
[467] DanielJButler, JonasWulff, GarrettBStanley, andMichaelJBlack. Anaturalisticopensourcemoviefor
opticalflowevaluation. InEuropeanconferenceoncomputervision,pages611–625.Springer,2012.
[468] TonRoosendaal. Sintel. 2010. Accessed: 2022-07-18.
[469] Blender-freeandopen3dcreationsoftware. https://www.blender.org/. Accessed: 2022-07-18.
[470] AnkurHanda,ThomasWhelan,JohnMcDonald,andAndrewJDavison.Abenchmarkforrgb-dvisualodometry,
3dreconstructionandslam. In2014IEEEinternationalconferenceonRoboticsandautomation(ICRA),pages
1524–1531.IEEE,2014.
[471] Thepersistenceofvisionraytracer. https://www.povray.org/. Accessed: 2022-07-18.
[472] HaoSu,CharlesRQi,YangyanLi,andLeonidasJGuibas. Renderforcnn: Viewpointestimationinimages
using cnns trained with rendered 3d model views. In Proceedings of the IEEE international conference on
computervision,pages2686–2694,2015.
[473] XingchaoPeng,BaochenSun,KarimAli,andKateSaenko. Learningdeepobjectdetectorsfrom3dmodels. In
ProceedingsoftheIEEEinternationalconferenceoncomputervision,pages1278–1286,2015.
[474] AnkurHanda,VioricaPa˘tra˘ucean,SimonStent,andRobertoCipolla. Scenenet: Anannotatedmodelgenerator
forindoorsceneunderstanding. In2016IEEEInternationalConferenceonRoboticsandAutomation(ICRA),
pages5737–5743.IEEE,2016.
[475] AnkurHanda,VioricaPatraucean,VijayBadrinarayanan,SimonStent,andRobertoCipolla. Understandingreal
worldindoorsceneswithsyntheticdata. InProceedingsoftheIEEEconferenceoncomputervisionandpattern
recognition,pages4077–4085,2016.
[476] MartinPeris,SaraMartull,AtsutoMaki,YasuhiroOhkawa,andKazuhiroFukui. Towardsasimulationdriven
stereovisionsystem. InProceedingsofthe21stInternationalConferenceonPatternRecognition(ICPR2012),
pages1038–1042.IEEE,2012.
[477] JavierMolina,JoséAPajuelo,MarcosEscudero-Viñolo,JesúsBescós,andJoséMMartínez. Anaturaland
synthetic corpus for benchmarking of hand gesture recognition systems. Machine Vision and Applications,
25(4):943–954,2014.
[478] BaochenSunandKateSaenko. Fromvirtualtoreality:Fastadaptationofvirtualobjectdetectorstorealdomains.
InBMVC,volume1,page3,2014.
[479] Konstantinos Rematas, Tobias Ritschel, Mario Fritz, and Tinne Tuytelaars. Image-based synthesis and re-
synthesisofviewpointsguidedby3dmodels. InProceedingsoftheIEEEConferenceonComputerVisionand
PatternRecognition,pages3898–3905,2014.
[480] Jeremie Papon and Markus Schoeler. Semantic pose using deep networks trained on synthetic rgb-d. In
ProceedingsoftheIEEEInternationalConferenceonComputerVision,pages774–782,2015.
[481] PhilippFischer,AlexeyDosovitskiy,EddyIlg,PhilipHäusser,CanerHazırbas¸,VladimirGolkov,PatrickVander
Smagt,DanielCremers,andThomasBrox. Flownet: Learningopticalflowwithconvolutionalnetworks. arXiv
preprintarXiv:1504.06852,2015.
[482] AdamKortylewski,AndreasSchneider,ThomasGerig,BernhardEgger,AndreasMorel-Forster,andThomas
Vetter. Trainingdeepfacerecognitionsystemswithsyntheticdata. arXivpreprintarXiv:1802.05891,2018.
[483] Markus Philipp, Neal Bacher, Jonas Nienhaus, Lars Hauptmann, Laura Lang, Anna Alperovich, Marielena
Gutt-Will,AndreaMathis,StefanSaur,AndreasRaabe,etal.Syntheticdatagenerationforopticalflowevaluation
intheneurosurgicaldomain. Currentdirectionsinbiomedicalengineering,7(1):67–71,2021.
[484] AlekseiBoikov,VladimirPayor,RomanSavelev,andAlexandrKolesnikov. Syntheticdatagenerationforsteel
defectdetectionandclassificationusingdeeplearning. Symmetry,13(7):1176,2021.
[485] GermanRos,LauraSellart,JoannaMaterzynska,DavidVazquez,andAntonioMLopez. Thesynthiadataset:
Alargecollectionofsyntheticimagesforsemanticsegmentationofurbanscenes. InProceedingsoftheIEEE
conferenceoncomputervisionandpatternrecognition,pages3234–3243,2016.
[486] VladimirHaltakov,ChristianUnger,andSlobodanIlic. Frameworkforgenerationofsyntheticgroundtruthdata
fordriverassistanceapplications. InGermanconferenceonpatternrecognition,pages323–332.Springer,2013.
99

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[487] Vdrift-open-sourcedrivingsimulation. https://vdrift.net/. Accessed: 2022-07-18.
[488] Stephan R Richter, Vibhav Vineet, Stefan Roth, and Vladlen Koltun. Playing for data: Ground truth from
computergames. InEuropeanconferenceoncomputervision,pages102–118.Springer,2016.
[489] Matthew Johnson-Roberson, Charles Barto, Rounak Mehta, Sharath Nittur Sridhar, Karl Rosaen, and Ram
Vasudevan. Drivinginthematrix: Canvirtualworldsreplacehuman-generatedannotationsforrealworldtasks?
arXivpreprintarXiv:1610.01983,2016.
[490] Unityreal-timedevelopmentplatform. https://unity.com/. Accessed: 2022-07-18.
[491] AlirezaShafaei,JamesJLittle,andMarkSchmidt. Playandlearn: Usingvideogamestotraincomputervision
models. arXivpreprintarXiv:1608.01745,2016.
[492] AdrienGaidon,QiaoWang,YohannCabon,andEleonoraVig. Virtualworldsasproxyformulti-objecttracking
analysis. InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,pages4340–4349,
2016.
[493] Andreas Geiger, Philip Lenz, and Raquel Urtasun. Are we ready for autonomous driving? the kitti vision
benchmarksuite. In2012IEEEconferenceoncomputervisionandpatternrecognition,pages3354–3361.IEEE,
2012.
[494] StephanRRichter,ZeeshanHayder,andVladlenKoltun. Playingforbenchmarks. InProceedingsoftheIEEE
InternationalConferenceonComputerVision,pages2213–2222,2017.
[495] AmlanKar,AayushPrakash,Ming-YuLiu,EricCameracci,JustinYuan,MattRusiniak,DavidAcuna,Antonio
Torralba,andSanjaFidler. Meta-sim: Learningtogeneratesyntheticdatasets. InProceedingsoftheIEEE/CVF
InternationalConferenceonComputerVision,pages4551–4560,2019.
[496] MarcGBellemare,YavarNaddaf,JoelVeness,andMichaelBowling. Thearcadelearningenvironment: An
evaluationplatformforgeneralagents. JournalofArtificialIntelligenceResearch,47:253–279,2012.
[497] Michał Kempka, Marek Wydmuch, Grzegorz Runc, Jakub Toczek, and Wojciech Jas´kowski. Vizdoom: A
doom-basedairesearchplatformforvisualreinforcementlearning. In2016IEEEconferenceoncomputational
intelligenceandgames(CIG),pages1–8.IEEE,2016.
[498] Fereshteh Sadeghi and Sergey Levine. Cad2rl: Real single-image flight without a single real image. arXiv
preprintarXiv:1611.04201,2016.
[499] OriolVinyals,TimoEwalds,SergeyBartunov,PetkoGeorgiev,AlexanderSashaVezhnevets,MichelleYeo,
AlirezaMakhzani,HeinrichKüttler,JohnAgapiou,JulianSchrittwieser,etal. Starcraftii: Anewchallengefor
reinforcementlearning. arXivpreprintarXiv:1708.04782,2017.
[500] CharlesBeattie,JoelZLeibo,DenisTeplyashin,TomWard,MarcusWainwright,HeinrichKüttler,Andrew
Lefrancq,SimonGreen,VíctorValdés,AmirSadik,etal. Deepmindlab. arXivpreprintarXiv:1612.03801,
2016.
[501] GabrielSynnaeve,NantasNardelli,AlexAuvolat,SoumithChintala,TimothéeLacroix,ZemingLin,Florian
Richoux,andNicolasUsunier. Torchcraft: alibraryformachinelearningresearchonreal-timestrategygames.
arXivpreprintarXiv:1611.00625,2016.
[502] MatthewJohnson,KatjaHofmann,TimHutton,andDavidBignell. Themalmoplatformforartificialintelligence
experimentation. InIjcai,pages4246–4247.Citeseer,2016.
[503] ZhengweiWang,QiShe,andTomasEWard. Generativeadversarialnetworksincomputervision: Asurveyand
taxonomy. arXivpreprintarXiv:1906.01529,2019.
[504] YannLeCun,LéonBottou,YoshuaBengio,andPatrickHaffner. Gradient-basedlearningappliedtodocument
recognition. ProceedingsoftheIEEE,86(11):2278–2324,1998.
[505] AlexKrizhevsky,GeoffreyHinton,etal. Learningmultiplelayersoffeaturesfromtinyimages. 2009.
[506] ZiweiLiu,PingLuo,XiaogangWang,andXiaoouTang.Deeplearningfaceattributesinthewild.InProceedings
ofInternationalConferenceonComputerVision(ICCV),December2015.
[507] JiaDeng,WeiDong,RichardSocher,Li-JiaLi,KaiLi,andLiFei-Fei. Imagenet: Alarge-scalehierarchical
imagedatabase. In2009IEEEconferenceoncomputervisionandpatternrecognition,pages248–255.Ieee,
2009.
[508] FisherYu,AriSeff,YindaZhang,ShuranSong,ThomasFunkhouser,andJianxiongXiao. Lsun: Constructionof
alarge-scaleimagedatasetusingdeeplearningwithhumansintheloop. arXivpreprintarXiv:1506.03365,2015.
100

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
[509] Tsung-YiLin,MichaelMaire,SergeBelongie,JamesHays,PietroPerona,DevaRamanan,PiotrDollár,and
CLawrenceZitnick. Microsoftcoco: Commonobjectsincontext. InEuropeanconferenceoncomputervision,
pages740–755.Springer,2014.
[510] YuvalNetzer,TaoWang,AdamCoates,AlessandroBissacco,BoWu,andAndrewYNg. Readingdigitsin
naturalimageswithunsupervisedfeaturelearning. 2011.
[511] DarrellConklin. BachChorales. UCIMachineLearningRepository.
[512] TeagueSterlingandJohnJ.Irwin. Zinc15–liganddiscoveryforeveryone. JournalofChemicalInformation
andModeling,55(11):2324–2337,2015. PMID:26479676.
[513] FidaKDankarandMahmoudIbrahim. Fakeittillyoumakeit: Guidelinesforeffectivesyntheticdatageneration.
AppliedSciences,11(5):2158,2021.
[514] ShanChangandChaoLi. Privacyinneuralnetworklearning: Threatsandcountermeasures. IEEENetwork,
32(4):61–67,2018.
[515] JoseDFernándezandFranciscoVico. Aimethodsinalgorithmiccomposition:Acomprehensivesurvey. Journal
ofArtificialIntelligenceResearch,48:513–582,2013.
[516] XiaodongHeandLiDeng. Deeplearningforimage-to-textgeneration: Atechnicaloverview. IEEESignal
ProcessingMagazine,34(6):109–116,2017.
[517] XinYi,EktaWalia,andPaulBabyn. Generativeadversarialnetworkinmedicalimaging: Areview. Medical
imageanalysis,58:101552,2019.
[518] MohammadAbufaddaandKhalidMansour. Asurveyofsyntheticdatagenerationformachinelearning. In2021
22ndInternationalArabConferenceonInformationTechnology(ACIT),pages1–7.IEEE,2021.
101

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
A Acronyms
AAE AdversarialAutoencoder
AF AutoregressiveFlow
AI ArtificialIntelligence
AIC Akaikeinformationcriterion
ALI AdversariallyLearnedInference
BIC Bayesianinformationcriterion
BN BayesianNetwork
BPTT BackpropagationThroughTime
BiGAN BidirectionalGAN
C2ST ClassifierTwoSampleTest
CAD ComputerAidedDesign
CAE ContractiveAutoencoder
CAN CreativeAdversarialNetwork
CDBN ConditionalDeepBeliefNetwork
CNN ConvolutionalNeuralNetwork
CRBM ConditionalRestrictedBoltzmannMachine
CT ComputedTomography
DAE DenoisingAutoencoder
DAG DirectedAcyclicGraph
DL DeepLearning
DBM DeepBoltzmannMachine
DBN DeepBeliefNetwork
DCGAN DeepConvolutionalGAN
DDPM DenoisingDiffusionProbabilisticModel
DLGM DeepLatentGaussianModel
ECG Electrocardiogram
EHR ElectronicHealthRecord
ELBO EvidenceLower-Bound
FID FréchetInceptionDistance
GA GeneticAlgorithm
GAE GatedAutoencoder
GAN GenerativeAdversarialNet
GMM GaussianMixtureModel
GMMN GenerativeMomentMatchingNetwork
GNN GraphNeuralNetwork
GPU GraphicsProcessingUnit
GRU GatedRecurrentUnit
GSN GenerativeStochasticNetwork
HMM HiddenMarkovModel
HSI HyperspectralImage
IS InceptionScore
KDE KernelDensityEstimators
102

ComprehensiveExplorationofSyntheticDataGeneration: ASurvey
LDA LatentDirichletAllocation
LRCN Long-termRecurrentConvolutionalNetwork
LSTM LongShort-TermMemory
MCMC MarkovchainMonteCarlo
ML MachineLearning
MLP MultilayerPerceptron
MMD MaximumMeanDiscrepancy
NADE NeuralAutoregressiveDistributionEstimator
NLL NegativeLog-Likelihood
NLP NaturalLanguageProcessing
ODE OrdinaryDifferentialEquation
PPG Photoplethysmogram
PPGN Plug&PlayGenerativeNetwork
PSD PrivateSpatialDecomposition
RBM RestrictedBoltzmannMachine
RL ReinforcementLearning
RNN RecurrentNeuralNetwork
RTRBM RecurrentTemporalBoltzmannMachine
ReLU rectifiedlinearunit
SDG SyntheticDataGeneration
SLAM SimultaneousLocalizationandMapping
SRTRBM StructuredRecurrentTemporalBoltzmannMachine
SVHN StreetViewHouseNumbers
TFD TorontoFaceDatabase
TRBM TemporalRestrictedBoltzmannMachine
VAE VariationalAutoencoder
VCAE VineCopulaAutoencoder
WAE WassersteinAutoencoder
103