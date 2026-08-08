Rethinking Time Encoding via Learnable Transformation Functions
XiChen1 YatengTang2 JiarongXu3 JiaweiZhang4 SiweiZhang1 SijiaPeng1 XuehaoZheng2 YunXiong1
|     | Abstract |     |     |     | vationsinweatherforecasting(Muratetal.,2018;Neumann |          |     |             |        |     |         |
| --- | -------- | --- | --- | --- | --------------------------------------------------- | -------- | --- | ----------- | ------ | --- | ------- |
|     |          |     |     |     | et al., 2024).                                      | Adopting |     | time series | models | and | dynamic |
Effectivelymodelingtimeinformationandincor-
graphmodelstohandletime-relateddataaretwocommon
5202 yaM 41  ]GL.sc[  2v78800.5052:viXra poratingitintoapplicationsormodelsinvolving
|                                          |     |     |     |       | approaches(Wuetal.,2023;Yuetal.,2023). |     |     |     |     | Inbothcases, |     |
| ---------------------------------------- | --- | --- | --- | ----- | -------------------------------------- | --- | --- | --- | --- | ------------ | --- |
| chronologicallyoccurringeventsiscrucial. |     |     |     | Real- |                                        |     |     |     |     |              |     |
effectivelyincorporatingtimeinformationiscrucialformak-
worldscenariosofteninvolvediverseandcomplex
|     |     |     |     |     | ingaccuratepredictions. |     |     | Toachievethis,existingresearch |     |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------------------ | --- | --- | --- |
timepatterns,whichposesignificantchallenges
workstypicallyemploytimeencodingmethodstocapture
| fortimeencodingmethods. |     | Whilepreviousmeth- |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andrepresenttimeinformation,withtheresultingtimeem-
odsfocusoncapturingtimepatterns,manyrely
|     |     |     |     |     | bedding | being treated | as  | an independent |     | feature | in time |
| --- | --- | --- | --- | --- | ------- | ------------- | --- | -------------- | --- | ------- | ------- |
onspecificinductivebiases,suchasusingtrigono-
seriesforecastinganddynamicgraphrepresentationlearn-
| metricfunctionstomodelperiodicity. |     |     | Thisnar- |     |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingmodels.
rowfocusonsingle-patternmodelingmakesthem
lesseffectiveinhandlingthediversityandcom- Earlystudiesrepresenttimebyusinghand-craftedtemporal
plexitiesofreal-worldtimepatterns. Inthispa- featuresdesignedspecificallyfordownstreamtasks(Choi
per,weinvestigatetoimprovetheexistingcom- et al., 2016; Baytas et al., 2017; Kwon et al., 2018). A
monlyusedtimeencodingmethodsandintroduce prominentexampleisthetimeencodingmethodillustrated
LearnableTransformation-basedGeneralized in Figure 1 (a), which is widely used in existing time se-
TimeEncoding(LeTE).Weproposeusingdeep riesprocessingwork(Wangetal.,2023;Wuetal.,2023).
functionlearningtechniquestoparameterizenon- Such methods typically involve manually splitting times-
lineartransformationsintimeencoding,making tampsintocomponents(e.g.,month,day,etc.),assigning
themlearnableandcapableofmodelinggeneral- aembeddingtoeachcomponent,andaddingtheseembed-
izedtimepatterns,includingdiverseandcomplex
|     |     |     |     |     | dings to | form the | final | time embedding. |     | However, | these |
| --- | --- | --- | --- | --- | -------- | -------- | ----- | --------------- | --- | -------- | ----- |
temporaldynamics. Byenablinglearnabletrans- methods are resource-intensive andoften rely on domain
formations,LeTEencompassespreviousmethods expertise, which may limit their abilities to capture only
asspecificcasesandallowsseamlessintegration specificpre-definedtimepatterns(Kazemietal.,2019).
| into | a wide range of tasks. | Through | extensive |     |     |     |     |     |     |     |     |
| ---- | ---------------------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Withtherapiddevelopmentofattentionmechanisms,which
experimentsacrossdiversedomains,wedemon-
offeradvantagessuchasbetterhandlingoflong-rangede-
stratetheversatilityandeffectivenessofLeTE.
|     |     |     |     |     | pendencies | and        | adaptive | weighting | of time-related |     | infor-  |
| --- | --- | --- | --- | --- | ---------- | ---------- | -------- | --------- | --------------- | --- | ------- |
|     |     |     |     |     | mation,    | subsequent | research | on        | time series     | and | dynamic |
graphshasincreasinglyleveragedthesemechanisms(Xu
1.Introduction
|     |     |     |     |     | et al., 2020; | Yu  | et al., 2023; | Liu | et al., | 2023). | To better |
| --- | --- | --- | --- | --- | ------------- | --- | ------------- | --- | ------- | ------ | --------- |
Time-relateddataarecommonlyobservedinreal-worldap- modeltimeandensurecompatibilitybetweentimeencod-
|     |     |     |     |     | ing methods | and | self-attention, |     | Functional | Time | Encod- |
| --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | ---------- | ---- | ------ |
plications,suchasusertransactiondatainfinancialinstitu-
ing(FTE)methodswereproposed,withtworepresentative
tions(Kazemietal.,2020;Lezmi&Xu,2023),purchasebe-
haviorsequencesine-commerce(Kang&McAuley,2018; works: Functional Time Representation (Xu et al., 2019)
andTime2Vec(Kazemietal.,2019),asillustratedinFigure
Rossietal.,2020;Skardingetal.,2021),andclimateobser-
1(b). Nearlyallsubsequentdynamicgraphrepresentation
1ShanghaiKeyLaboratoryofDataScience,SchoolofCom-
|     |     |     |     |     | learning | research | employs | these | methods | to encode | time |
| --- | --- | --- | --- | --- | -------- | -------- | ------- | ----- | ------- | --------- | ---- |
2Tencent
puter Science, Fudan University, Shanghai, China (Yu et al., 2023). These techniques transform time input
3School
| Weixin Group,   | Shenzhen, China         |      | of Management, | Fu-       |                                                   |                 |     |          |     |             |      |
| --------------- | ----------------------- | ---- | -------------- | --------- | ------------------------------------------------- | --------------- | --- | -------- | --- | ----------- | ---- |
|                 |                         | 4IFM |                |           | intomulti-dimensionaltimeembeddingsbyapplyingmul- |                 |     |          |     |             |      |
| dan University, | Shanghai, China         | Lab, | University     | of Cal-   |                                                   |                 |     |          |     |             |      |
|                 |                         |      |                |           | tiple linear                                      | transformations |     | followed | by  | pre-defined | non- |
| ifornia, Davis, | CA, USA. Correspondence |      | to:            | Yun Xiong |                                                   |                 |     |          |     |             |      |
<yunx@fudan.edu.cn>. lineartransformationfunctions. Duetotheirrelianceonpre-
definednon-lineartransformations—suchastrigonometric
Proceedingsofthe42nd
InternationalConferenceonMachine functionstocaptureperiodicpatterns—thesemethodsare
Learning,Vancouver,Canada.PMLR267,2025.Copyright2025
inherentlylimitedtocapturingfixed,specifictimepatterns.
bytheauthor(s).
1

RethinkingTimeEncodingviaLearnableTransformationFunctions
Time Encoding Hand-Crafted Time Encoding (HCTE) Functional Time Encoding (FTE) LeTE (Ours)
Patterns
|     |     |     | Pre-defined |     |     | Pre-defined |     |     |     |     | Diverse |     |     |
| --- | --- | --- | ----------- | --- | --- | ----------- | --- | --- | --- | --- | ------- | --- | --- |
Capturing
|         | TE(t )[ | i] = E m o n th (t m o | n th ) [i ]+ E d a y | ( td a y ) [ i ] + |           | s i n ( ω t + | φ )   or ω t+φ | i, i f   i = 1 , |            |     |               |     |             |
| ------- | ------- | ---------------------- | -------------------- | ------------------ | --------- | ------------- | -------------- | ---------------- | ---------- | --- | ------------- | --- | ----------- |
| Formula |         |                        |                      |                    | TE(t)[i]= | i             | i i            |                  | TE(t)[i]=s |     | i⋅LayerNorm(ϕ |     | i(ω t+φ i)) |
E w ee kd a y( t w ee k d ay ) [i ] + Eh o u r (t h o u r ) [ i ] +Emin(tmin)[i] { s i n ( ω t + φ ) , i f   2 ≤ i ≤d i
i i
|     | (a) |                |     |     | (b) |                |     |     | (c) |     |                |     |     |
| --- | --- | -------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | -------------- | --- | --- |
|     |     | Time Embedding |     |     |     | Time Embedding |     |     |     |     | Time Embedding |     |     |
Fixed Non-linear
|     |     |     |     |     |     |     |     | Transformation |     |     | LayerNorm and Scaling |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --------------------- | --- | --- |
Em b e dd i n g  a n d     sin(ωit+φi) Lea r n a b l e  N o n - l in ear
Architecture Elem en t- w is e   A d d it i on T r a n s f o rm a t i o n
ϕi(ωit+φi)
|     |     | [tmonth,tday,tweekday,thour,tminute] |     |     | (ωit+φi) |     |     |     | (ωit+φi) |     |     |     |     |
| --- | --- | ------------------------------------ | --- | --- | -------- | --- | --- | --- | -------- | --- | --- | --- | --- |
Extract Features
|     |     |          | t                                                        |     |                       |     | t   |     |                       |     |     | t   |     |
| --- | --- | -------- | -------------------------------------------------------- | --- | --------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
|     |     |          |                                                          |     | Linear Transformation |     |     |     | Linear Transformation |     |     |     |     |
|     |     | Figure1. | AcomparisonofprevioustimeencodingmethodsandproposedLeTE. |     |                       |     |     |     |                       |     |     |     |     |
Asaresult,theyoftenstruggletorepresentmorecomplex, To better encode time information and simultaneously
non-linear temporal dynamics (Kazemi et al., 2019; Wu capture diverse time patterns, we propose Learnable
etal.,2023)andrequireadditionaldimensionstoaccount Transformation-basedGeneralizedTimeEncoding,ab-
for diverse periodic components (Xu et al., 2020; Rossi breviatedasLeTE—asimpleyeteffectivetimeencoding
etal.,2020;Zengetal.,2024). Furthermore,theseencoding method. Insteadofhand-craftingtimeencodingorrelying
methodsfrequentlylackthecapacitytoeffectivelymodel onpre-definednon-lineartransformations,wedrawinspira-
non-periodicpatterns,suchastrends,irregularities. tionfromdeepfunctionlearning,whichisknownforitsgen-
eralizability,interpretability,andreusability(Zhang,2024;
Weobservethatprevioustimeencodingmethods—whether
|              |     |                      |     |           |          | Liuetal.,2025),                 |     |     | andproposetouselearnablenon-linear |     |                        |     |     |
| ------------ | --- | -------------------- | --- | --------- | -------- | ------------------------------- | --- | --- | ---------------------------------- | --- | ---------------------- | --- | --- |
| hand-crafted | or  | functional—primarily |     | introduce | a strong |                                 |     |     |                                    |     |                        |     |     |
|              |     |                      |     |           |          | transformationsfortimeencoding. |     |     |                                    |     | Specifically,weparame- |     |     |
inductivebiasrootedintheperiodicnatureofhumanbehav-
terizenon-lineartransformationfunctionsusingtechniques
iorandnaturalphenomena(Lietal.,2017;Xuetal.,2019;
|                    |     |                                |     |     |     | derivedfromdeepfunctionlearning. |     |     |     |     | Thisparameterization |     |     |
| ------------------ | --- | ------------------------------ | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- |
| Kazemietal.,2019). |     | Theymainlyfocusoncapturingpre- |     |     |     |                                  |     |     |     |     |                      |     |     |
makesthetransformationslearnableandjointlyoptimizable
definedperiodicpatterns,oftenstrugglingtocapturemore
withthemodel’sparametersundersupervisionfromdown-
complexones,suchasnon-periodicandmixedpatterns.
streamtasks,allowingthemtoflexiblyadapttobothlinear
However,inreal-worldscenarios,dataoftenexhibitsacom- andarbitrarynon-linearforms. Withlearnabletransforma-
plexinterplayofmixedpatterns,makingaccuratemodeling tions,LeTEadaptivelymodelstimeinformation,enabling
more challenging. For instance, in financial risk control, differentdimensionsoftimeencodingtocapturecomplex
periodicpatterns—suchasdailytransactionpeaks,weekly timepatterns—suchasirregulartrends,abruptchanges,and
spending habits, and seasonal trends around holidays or overlappingperiodicities—thatarecommonlyencountered
salarypayments—offervaluableinsightsintopredictable inreal-worldscenariosandbeyondthecapabilitiesofpre-
behaviors. Ontheotherhand,non-periodicevents,suchas viousmethods. Thisgeneralizationalsoallowsourmethod
suddenspikesintransactionscausedbymarketfluctuations, to encompass previous approaches as specific cases. An
regulatorychanges,orpotentialfraudulentactivities,neces- illustrationofLeTEisinFigure1(c).
| sitateflexibleandadaptivemodelingtechniques. |          |                |     |              | Moreover,  |       |      |        |           |            |           |              |          |
| -------------------------------------------- | -------- | -------------- | --- | ------------ | ---------- | ----- | ---- | ------ | --------- | ---------- | --------- | ------------ | -------- |
|                                              |          |                |     |              |            | LeTE  | also | offers | following | advantages |           | (cf. Section | 3.2).    |
| different                                    | patterns | often coexist. |     | For example, | fraudsters |       |      |        |           |            |           |              |          |
|                                              |          |                |     |              |            | Since | time | can be | measured  | on         | different | scales,      | its rep- |
mayblendregularperiodictransactionswithabnormalnon-
resentationshouldbeinvarianttotimerescaling(Kazemi
| periodicactivitiestoevadethedetectionbyregulators. |     |     |     |     |     | To  |             |     |       |           |           |      |          |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --------- | --------- | ---- | -------- |
|                                                    |     |     |     |     |     | et  | al., 2019). | We  | prove | that LeTE | satisfies | this | property |
illustratethepresenceofcomplexmixedtimepatternsin
|     |     |     |     |     |     | (cf. | AppendixC.3). |     | Furthermore,weprovethatLeTEisa |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ------------- | --- | ------------------------------ | --- | --- | --- | --- |
real-worlddata,weconductextensiveinvestigationsinthis
generalizedversionofpreviousmethodsandcanintegrate
paper,withpartialresultsinAppendixG.1.
|     |     |     |     |     |     | seamlesslywithvariousmodels(cf. |     |     |     |     | Section3.2). |     | Byem- |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ------------ | --- | ----- |
Thismotivatesustorethinkthedesignoftimeencodings. ployinganinterpretabledeepfunctionlearningapproach,
We argue that an effective time encoding method should LeTE achieves a high degree of interpretability (cf. Ap-
adheretoakeyprincipletoenablecomprehensiveandaccu- pendixG.3). Additionally,experimentalresultsdemonstrate
rateanalysis: Capacityformodelingdiverseandcomplex thatLeTEachievessuperiorresultswithfewerdimensions
time patterns, i.e., the method should be capable of cap- thanprevioustimeencodings,asthelearnabletransforma-
turing a wide range of time patterns, including periodic, tionscapturepartofthecomplexitythatwouldotherwise
non-periodic,andmixedpatterns. requirehigher-dimensionalembeddings(cf. Section4.5).
2

RethinkingTimeEncodingviaLearnableTransformationFunctions
Wehighlightourcontributionsasfollows: 2.2.DeepFunctionLearning
|     |     |     |     |     |     |     | Deep | Function | Learning | refers | to the approach | of  | learn- |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | -------- | ------ | --------------- | --- | ------ |
• Wereinvestigatethedesignoftheexistingtimeencod-
ingtargetfunctionsbyoptimizingparameterizedfunctions,
ingmethods,highlightingtheirlimitationsinhandling
|     |     |     |     |     |     |     | suchaspolynomials,sinusoidalfunctions,orsplines. |     |     |     |     |     | This |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | ---- |
real-worlddataandproposeLeTE,ageneralizedtime
methodleveragestheflexibilityofparameterizedfunctions
encodingmethodthatallowstheentireencodingpro-
andoptimizestheirparametersusingdeeplearningframe-
cess,includingbothlinearandnon-lineartransforma-
workstoapproximatecomplexfunctions(Zhang,2024).
tions,fullyparameterizedandlearnable.
|     |     |     |     |     |     |     | FourierSeriesExpansion: |     |     | TheFourierseriesexpresses |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------------- | --- | --- | --- |
• LeTEhasthecapacitytomodeldiverseandcomplex
atargetfunctionf(x)asacombinationofsineandcosine
timepatterns,anditoffersadditionalbenefits,includ-
functions:
inginvariancetotimerescaling,plug-and-playfunc-
| tionality, | enhanced | interpretability |     | and | improved | di- |     |     | N   |     |     |     |     |
| ---------- | -------- | ---------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|                      |     |     |     |     |     |     |     | f(x)=a | + (a | cos(nωx)+b |     | sin(nωx)) | (4) |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ---------- | --- | --------- | --- |
| mensionalefficiency. |     |     |     |     |     |     |     |        | 0    | n          | n   |           |     |
n=1
| • Through                                        | extensive | experiments |     | across | diverse         | do- |                    |      |                                        |     |     |               |     |
| ------------------------------------------------ | --------- | ----------- | --- | ------ | --------------- | --- | ------------------ | ---- | -------------------------------------- | --- | --- | ------------- | --- |
|                                                  |           |             |     |        |                 |     | Here,a             | andb | arelearnablecoefficients,andωisthefun- |     |     |               |     |
| mains—including                                  |           | event-based |     | image  | classification, |     |                    | n    | n                                      |     |     |               |     |
|                                                  |           |             |     |        |                 |     | damentalfrequency. |      | Byoptimizinga                          |     | ,a  | andb througha |     |
| timeseriesforecasting,dynamicgraphrepresentation |           |             |     |        |                 |     |                    |      |                                        |     | 0 n | n             |     |
learningprocess,thefunctionf(x)canapproximatecom-
learningandreal-worldapplications-wedemonstrate
|     |     |     |     |     |     |     | plexpatterns(cf. |     | AppendixB.1fordetails). |     |     | Unlikefixed |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------------------- | --- | --- | ----------- | --- |
theeffectivenessandversatilityofLeTE.
sinefunctions,parameterizedfunctionsadjusttheirampli-
tude,frequency,andphasethroughdownstreamsupervisory
2.Preliminaries signals,enablingthemtoeffectivelymodelawiderrangeof
patterns.
2.1.FunctionalTimeEncodings
|     |     |     |     |     |     |     | SplineFunctions: |     | Splinefunctionsapproximateatarget |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------------------------- | --- | --- | --- | --- |
FunctionalTimeEncoding(FTE)methodscanbeviewedas
functionf(x)usingasumofpiecewisepolynomialbasis
featuremappingsfrom1-dimensionalinputtimetoahigh-
functions:
| dimensional | time embedding: |     | Φ   | : t ∈ R1 | → TE | ∈ Rd, |     |     |     | n   |     |     |     |
| ----------- | --------------- | --- | --- | -------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|                                                  |                                    |     |     |     |     |     |     |     | f(x)= | c   | B (x) |     |     |
| ------------------------------------------------ | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | --- |
| wheret∈[0,t                                      | max ]isfromthevaluerangeboundedbyt |     |     |     |     | max | .   |     |       | i   | i     |     | (5) |
| TworepresentativeworksofFTEareFunctionalTimeRep- |                                    |     |     |     |     |     |     |     |       | i=1 |       |     |     |
resentation(FTR)(Xuetal.,2019)andTime2Vec(T2V)
|     |     |     |     |     |     |     | Here,c | i arecontrolpoints,andB |     |     | i (t)arethebasisfunctions |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------------------- | --- | --- | ------------------------- | --- | --- |
(Kazemietal.,2019). Althoughthesemethodsconstruct (e.g., B-splines). By learning and optimizing the control
timeencodingsfromdifferentperspectives,theyaremath- points,knotpositions,andweights(cf. AppendixB.2for
ematically nearly identical (the only difference is that a details), splines provide a smooth and accurate represen-
separate dimension that undergoes only a linear transfor- tationofdiversefunctions. Theirpiecewiseandlocalized
| mation is | used by T2V | to  | capture | non-periodic | patterns). |     |     |     |     |     |     |     |     |
| --------- | ----------- | --- | ------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
structuremakesthemhighlyadaptableforcomplexfunction
| Westatethefollowingproposition,withdetailsofthetwo |     |     |     |     |     |     | modeling. |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
methodsandtheproofprovidedinAppendixC.1.
| Proposition2.1. | Mathematically,withselectedvaluesfor |     |     |     |     |     | 3.Methods |     |     |     |     |     |     |
| --------------- | ------------------------------------ | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
ω i andφ i ,theaforementionedFTRandT2Vcanbeunified
| intothefollowingforms: |     |     |     |     |     |     | 3.1.LeTE |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Includingthefirstdimension: To address the limitations of previous time encod-
(cid:40) ings—specifically,theirrestrictedcapacitytomodelfixed
sin(ω i t+φ i )orω i t+φ i , ifi=1, or pre-defined time patterns—we propose Learnable
TE(t)[i]=
sin(ω i t+φ i ), if2≤i≤d. Transformation-basedGeneralizedTimeEncoding(re-
|     |     |     |     |     |     | (1) | ferredtoasLeTE).Tocapturediverseandcomplexpatterns |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
Orexcludingthefirstdimension: intime-relateddata,weproposetechniquesthatmakenon-
|     |                |     |     |        |     |     | lineartransformationslearnable.                    |     |     |     | Thisapproachallowsthe |           |     |
| --- | -------------- | --- | --- | ------ | --- | --- | -------------------------------------------------- | --- | --- | --- | --------------------- | --------- | --- |
|     | TE(t)[i]=sin(ω |     |     | t+φ ), |     | (2) |                                                    |     |     |     |                       |           |     |
|     |                |     | i   | i      |     |     | modeltodynamicallyadaptitstransformations,enabling |     |     |     |                       |           |     |
|     |                |     |     |        |     |     | morepreciserepresentationsoftimepatterns.          |     |     |     |                       | Toachieve |     |
or
|     |     |     |     |     |     |     | this, | we employ | two distinct | approaches |     | for constructing |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | ------------ | ---------- | --- | ---------------- | --- |
TE(t)=[sin(ω t+φ ),··· ,sin(ω t+φ )] (3) learnable transformation functions: Fourier series expan-
|     |     | 1   | 1   | d   | d   |     |                         |     |     |                              |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ---------------------------- | --- | --- | --- |
|     |     |     |     |     |     |     | sionandSplinefunctions. |     |     | Bothmethodssharetheabilityto |     |     |     |
Forsimplicity,weuseFunctionalTimeEncoding(FTE)to effectivelycaptureandmodelcomplex,non-lineartemporal
refertoboththeFTRandT2Vthroughoutthepaper. patterns while maintaining flexibility in handling various
3

RethinkingTimeEncodingviaLearnableTransformationFunctions
|     |     |     |               | K    |             |                   | Combined LeTE |           |     |     |                     |             |     |     |
| --- | --- | --- | ------------- | ---- | ----------- | ----------------- | ------------- | --------- | --- | --- | ------------------- | ----------- | --- | --- |
|     |     |     | ϕ 1(x 1)=a    | 0+∑  |             |                   |               |           |     |     | M                   |             |     |     |
|     |     |     |               |      |             |                   |               |           |     | ϕ   | d(x                 | c B j(x     |     |     |
|     |     |     |               | k=1  |             |                   |               |           |     |     | d)=∑                | j d)        |     |     |
|     |     |     | (a kcos(kx    | 1)+b | ksin(kx 1)) |                   |               |           |     |     | j=1                 |             |     |     |
|     |     |     |               |      |             | [s i]⋅LayerNorm[ϕ |               | i(ω i t+φ | i)] |     |                     |             |     |     |
|     |     |     |               |      |             |                   |               |           |     |     | B 1(x)B 2(x)B 3(x)B | 4(x) B 5(x) |     |     |
|     |     |     | Fourier-based |      |             |                   |               |           |     |     | Spline-based        |             |     |     |
|     |     |     |               |      |             | x i=ω t+φ         |               | t         |     |     |                     |             |     |     |
|     |     |     |               |      |             | i                 | i             |           |     |     |                     |             |     |     |
Figure2.AnillustrationofCombinedLeTE:thefirstdimensionisparameterizedbyFourierseriesexpansionandthelastdimensionis
parameterizedbyB-Splines.
timedynamics. Basedonthesemethods,weproposethree where M is the number of B-spline basis functions, and
variationsofLeTE.First,weconstructthelearnabletransfor- B (x)isthej-thB-splinebasisfunction. LeTEcanthenbe
j
| mationfunctionsusingthesetwoapproaches,categorizing |                  |     |      |                  |     |        |     | expressedas: |     |     |     |     |     |     |
| --------------------------------------------------- | ---------------- | --- | ---- | ---------------- | --- | ------ | --- | ------------ | --- | --- | --- | --- | --- | --- |
| them                                                | as Fourier-based |     | LeTE | and Spline-based |     | LeTE   | ac- |              |     |     |     |     |     |     |
| cordingtotheirrespectiveconstructionmethods.        |                  |     |      |                  |     | Wethen |     |              |     |     | M   |     |     |     |
(cid:88)
|     |     |     |     |     |     |     |     |     |     | LeTE(t)[i]= | c   | B (ω | t+φ ). | (10) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | ------ | ---- |
integratethesetwovariationstodevelopamoregeneralized i,j j i i
| version,referredtoasCombinedLeTE,whichleveragesthe |     |     |     |     |     |     |     |     |     |     | j=1 |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
strengthsofbothapproaches. Comparingthesetwoapproachesforconstructingϕ ,the
i
For a scalar timestamp input t, LeTE for t, denoted as FourierseriesexpansioninLeTEenforcesperiodicityinϕ ,
i
whiletheB-splineapproachprovidesflexibilitytomodel
LeTE(t),isad-dimensionaltimeembeddingvector:
|     |     |              |     |        |     |     |     | more                  | complex | ϕ i functions, | including |     | both periodic | and |
| --- | --- | ------------ | --- | ------ | --- | --- | --- | --------------------- | ------- | -------------- | --------- | --- | ------------- | --- |
|     |     | LeTE(t)[i]=ϕ |     | (ω t+φ | ),  |     | (6) | non-periodicpatterns. |         |                |           |     |               |     |
|     |     |              |     | i i    | i   |     |     |                       |         |                |           |     |               |     |
Recallthatweneglectthefirstdimensionofthelineartrans-
| whereω | i andφ | i arelearnableparameters,andϕ |     |     |     | i arelearn- |     |     |     |     |     |     |     |     |
| ------ | ------ | ----------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
formationoftimeinEquations(2)and(3),whichmodels
ablefunctionsthatcanbeparameterizedbyeitherFourier
|     |     |     |     |     |     |     |     | thenon-periodicpatternsforTime2Vec. |     |     |     |     | However,inLeTE, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --------------- | --- |
seriesexpansionorB-splines.
|     |     |     |     |     |     |     |     | byallowingϕ |     | tobelearnable,differentϕ |     |     | atdifferentdi- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------------------ | --- | --- | -------------- | --- |
|     |     |     |     |     |     |     |     |             |     | i                        |     |     | i              |     |
Fourier-based LeTE: This method assumes that ϕ are mensionscancapturemorecomplexnon-periodicpatterns
i
parameterizedbyFourierseriesexpansion:
basedonthesupervisionsignalsfromdownstreamtasks.
|     |     |     |     |     |     |     |     | Combined |     | LeTE: To | enhance | the capability | of  | the time |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------- | -------------- | --- | -------- |
K
(cid:88)
ϕ (x)=a + (a cos(kx)+b sin(kx)), (7) encodingtocapturediverseandcomplextimepatternsand
|     | i   | 0   |     | k   | k   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tobuildamoregeneralizedversionofLeTE,wefurtherpro-
k=1
|        |     |       |                                  |     |     |     |     | poseastraightforwardextension: |      |            |          | applyingFourier-based |            |     |
| ------ | --- | ----- | -------------------------------- | --- | --- | --- | --- | ------------------------------ | ---- | ---------- | -------- | --------------------- | ---------- | --- |
| wherea | ,a  | ,andb | aretheparameterstobelearned,andK |     |     |     |     |                                |      |            |          |                       |            |     |
|        | 0   | k     | k                                |     |     |     |     | LeTE                           | to a | portion of | the time | encoding              | dimensions | and |
representsthenumberoftermsintheexpansion. LeTEcan Spline-basedLeTEtotheremainingdimensions. Thepro-
thenbeexpressedas: portionofFourier-basedLeTEandSpline-basedLeTEused
|     |     |     |     |     |     |     |     | can | be controlled | by  | a hyperparameter |     | p. To address | po- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------------- | --- | ------------- | --- |
K
(cid:88)(cid:16) tentialdifferencesintheoutputscalesofFourier-basedand
|     | LeTE(t)[i]=a |     | +   | a cos(k(ω |     | t+φ )) |     |              |     |          |           |         |               |     |
| --- | ------------ | --- | --- | --------- | --- | ------ | --- | ------------ | --- | -------- | --------- | ------- | ------------- | --- |
|     |              |     | i,0 | i,k       | i   | i      |     |              |     |          |           |         |               |     |
|     |              |     |     |           |     |        |     | Spline-based |     | LeTE, we | introduce | a Layer | Normalization |     |
k=1
|     |     |     |            |     |          |     | (8) | layer     | followed                               | by a learnable |     | scaling | weight for | the time |
| --- | --- | --- | ---------- | --- | -------- | --- | --- | --------- | -------------------------------------- | -------------- | --- | ------- | ---------- | -------- |
|     |     |     |            |     | (cid:17) |     |     | encoding. | Forad-dimensionalLeTE,thetimeembedding |                |     |         |            |          |
|     |     |     | +b sin(k(ω | t+φ | ))       |     |     |           |                                        |                |     |         |            |          |
|     |     |     | i,k        | i   | i        |     |     |           |                                        |                |     |         |            |          |
isformulatedas:
|                                         |     |     |     |     |     |     |        |     | LeTE(t)[i]=s | ·LayerNorm(ϕ |     |     | (ω t+φ )), | (11) |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | ------------ | ------------ | --- | --- | ---------- | ---- |
|                                         |     |     |     |     |     |     |        |     |              | i            |     | i   | i i        |      |
| Spline-basedLeTE:Thismethodassumesthatϕ |     |     |     |     |     |     | arepa- |     |              |              |     |     |            |      |
i
rameterizedbyB-splines:
|     |     |     |     |     |     |     |     | where[s | i ]isad-lengthlearnablescalingweightvector,and |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------------------------------------- | --- | --- | --- | --- | --- |
(cid:40)
(cid:88) M
|     |     |     |          |         |      |     |     |     |     | Equation(7), |     | if  | i≤⌊p·d⌋, |      |
| --- | --- | --- | -------- | ------- | ---- | --- | --- | --- | --- | ------------ | --- | --- | -------- | ---- |
|     |     |     | ϕ i (x)= | c j B j | (x), |     | (9) |     | ϕ   | (x)=         |     |     |          | (12) |
|     |     |     |          |         |      |     |     |     | i   | Equation(9), |     | if  | i>⌊p·d⌋. |      |
j=1
4

RethinkingTimeEncodingviaLearnableTransformationFunctions
When p = 1, the method corresponds to Fourier-based sitionwithitscorrespondingprooftodemonstratethis.
| LeTE, and | when p | = 0, it corresponds | to  | Spline-based |                 |                                    |     |     |
| --------- | ------ | ------------------- | --- | ------------ | --------------- | ---------------------------------- | --- | --- |
|           |        |                     |     |              | Proposition3.1. | Foranarbitraryinputt,thenetworkcan |     |     |
LeTE. For the remainder of this paper, unless otherwise learnasetofparameterssuchthatLeTEcanreplicatethe
specified,LeTEwillrefertotheCombinedLeTE,wherep
|             |                                       |     |     |     | effects of | previous time | encodings, making | previous time |
| ----------- | ------------------------------------- | --- | --- | --- | ---------- | ------------- | ----------------- | ------------- |
| issetto0.5. | AnillustrationofLeTEisshowninFigure2, |     |     |     |            |               |                   |               |
encodingsspecificcasesofLeTE.
andtheimplementationdetailsareprovidedinAppendixD.
Proof. ForEquations(8)and(10),weonlyneedtofinda
3.2.PropertiesofLeTE
setofcoefficientsforEquations(7)and(9)toapproximate
Inthissubsection,wepresentthepropertiesofourmethod thesinefunction,respectively.ByselectingK =1,a i,0 =0,
from the perspective of theoretical analysis. Specifically, a =0,andb =1,Equation(8)becomes:
|     |     |     |     |     | i,1 | i,1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
wediscussthestrengthsofFourier-basedLeTEandSpline-
|     |     |     |     |     |     |     | (cid:16) (cid:0) | (cid:1) |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- |
basedLeTEindividually. SinceCombinedLeTEintegrates LeTE(t)[i]=0+ 0·cos 1·(ω t+φ )
i i
| these two | variations, | it naturally | inherits their | respective |     |     |     |     |
| --------- | ----------- | ------------ | -------------- | ---------- | --- | --- | --- | --- |
(cid:1)(cid:17)
|             |     |     |     |     |     |        | (cid:0)    | (13) |
| ----------- | --- | --- | --- | --- | --- | ------ | ---------- | ---- |
| properties. |     |     |     |     |     | +1·sin | 1·(ω i t+φ | i )  |
Generalizability: Comparedwithpreviousmethods,which =sin(ω t+φ ).
i i
canonlycapturepre-definedtimepatterns—usuallyperiodic
ones—ourmethodoffersgreatergeneralizability,enabling Thus, sin(ω t+φ ) is indeed a special case of the more
i i
ittocaptureawiderrangeofdiverseandcomplexpatterns, general formula in Equation (8). The proof continues in
includingperiodic,non-periodicandmixedones. Naturally, Appendix C.2, which demonstrates that sin(ω i t+φ i ) is
Fourier-basedLeTE(asformulatedinEquation(8),theϕ alsoaspecialcaseofEquation(10).
i
functionsareparameterizedbyFourierseriesexpansion)can
modelperiodicity,asitresemblesaFourierseriesexpansion
Moreover,sinceXuetal.claimthatabsolutepositionencod-
withweightedsumsofsineandcosinetermsatdifferentfre-
ingisaspecialcaseoffunctionaltimerepresentation(Xu
quenciesandphases. Bylearningappropriatevaluesforω i etal.,2019;2020),itisstraightforwardtoseethatabsolute
andincorporatingdifferentharmonicsk,thefunctioncanap-
positionencodingisalsoaspecialcaseofourLeTE.
proximatecomplexperiodicpatternsandcapturerepeating
|                   |                         |     |     |          | Invariance | to Time Rescaling: | Since time | can be repre- |
| ----------------- | ----------------------- | --- | --- | -------- | ---------- | ------------------ | ---------- | ------------- |
| structuresintime. | Thelearnableparametersω |     |     | andφ en- |            |                    |            |               |
|                   |                         |     |     | i i      |            |                    |            |               |
ablethemodeltoadapttovariousperiodiccharacteristicsin sentedonvariousscales(suchasdays,hours,orseconds),a
keycharacteristicofatimerepresentationisitsinvariance
thedata. AlthoughtheFourierseriesisinherentlyperiodic,
torescaling(Kazemietal.,2019;Tallec&Ollivier,2018).
| non-periodic | patterns | can also be | modeled: | the learnable |     |     |     |     |
| ------------ | -------- | ----------- | -------- | ------------- | --- | --- | --- | --- |
parametersa ,a ,b ,ω ,andφ provideflexibilityto SimilartoFTE,ourproposedtimeencodingisalsoinvariant
|     | i,0 i,k | i,k i | i   |     |     |     |     |     |
| --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
totimerescaling,asshowninthefollowingpropositionwith
| approximatenon-periodicbehaviors. |     |     | Byusingverysmall |     |     |     |     |     |
| --------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
orlargevaluesforω ,themodelcanfitsignalswithlong proofprovidedinAppendixC.3.
i
orslow-varyingcycles,effectivelycreatingnon-repeating
|                              |     |                             |     |     | Proposition3.2. | LeTEisinvarianttotimerescaling. |     |     |
| ---------------------------- | --- | --------------------------- | --- | --- | --------------- | ------------------------------- | --- | --- |
| patternsoverafiniteinterval. |     | Additionally,thecombination |     |     |                 |                                 |     |     |
oflearnedfrequencies,phases,andamplitudescanproduce
|     |     |     |     |     | Plug-and-Play: | LeTEisdesignedinaplug-and-playman- |     |     |
| --- | --- | --- | --- | --- | -------------- | ---------------------------------- | --- | --- |
complexpatternsthatdonotrepeatovertheobservedrange,
ner,ensuringseamlesscompatibilitywithvariousmodels
| thereby approximating |     | non-periodic | signals. | For similar |     |     |     |     |
| --------------------- | --- | ------------ | -------- | ----------- | --- | --- | --- | --- |
reasons, and given the generality of functions formed by andarchitectures. Byproducingad-dimensionaltimeem-
beddingvectorsimilartoprevioustimeencodings,itcanbe
| splines,Spline-basedLeTE(Equation(10),theϕ |     |     |     | arepa- |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | ------ | --- | --- | --- | --- |
i
rameterizedbyB-splines)canalsomodelbothperiodicand easilyintegratedwithoutrequiringsignificantmodifications
|                       |     |                                    |     |     | toexistingframeworks. |     | Unlikepriormethodsthatrelyon |     |
| --------------------- | --- | ---------------------------------- | --- | --- | --------------------- | --- | ---------------------------- | --- |
| non-periodicpatterns. |     | Naturally,throughmulti-dimensional |     |     |                       |     |                              |     |
fixednon-lineartransformationfunctions,LeTEemploys
encoding,bothFourier-basedandSpline-basedLeTEare
capableofcapturingmixedtimepatterns. AlthoughFourier- parameterizedandlearnabletransformations,enablingitto
|     |     |     |     |     | captureadditionalinformationandcomplexity. |     |     | Thisdesign |
| --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | ---------- |
basedLeTEcancapturenon-periodicpatterns,itsinherent
periodicitymakesitparticularlyeffectiveatmodelingthe allows LeTE to achieve superior performance even with
lower-dimensionaltimeencodingscomparedtotraditional
| periodicityoftime. |     | Conversely,whileSpline-basedLeTEis |     |     |     |     |     |     |
| ------------------ | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
methods(seeSection4.5forexperimentalresults).
| also capable                                | of capturing | periodic | patterns, | it exhibits a |                   |                                     |     |     |
| ------------------------------------------- | ------------ | -------- | --------- | ------------- | ----------------- | ----------------------------------- | --- | --- |
| strongerabilitytomodelnon-periodicpatterns. |              |          |           | Therefore,    |                   |                                     |     |     |
|                                             |              |          |           |               | Interpretability: | Previoustimeencodingsexhibitnatural |     |     |
bycombiningFourier-basedLeTEandSpline-basedLeTE, interpretabilitybecausetheyuseafixednon-linearactiva-
theresultingCombinedLeTEachievesenhancedcapability
|     |     |     |     |     | tion function, | i.e., the sine | function, which | has obvious |
| --- | --- | --- | --- | --- | -------------- | -------------- | --------------- | ----------- |
tocapturediversepatterns. Intuitively,thepreviousFTEs periodicity. Ourproposedtimeencodingusesalearnable
arespecialcasesofLeTE;wepresentthefollowingpropo- non-lineartransformationfunction. However,byexamining
5

RethinkingTimeEncodingviaLearnableTransformationFunctions
thelearnedparameters,wecanreconstructthesetransforma- WethenapplyanLSTMwitha32-dimensionallearnable
tionfunctions,enablingourmethodtoalsoachievestrong embedding for the time input and compare it to models
interpretability. Avisualizationofourproposedtimeencod- wheretheFTEorourLeTEisusedforencodingtime. The
ingisprovidedinAppendixG.3. results,showninFigure3,indicatethattheFTEachieves
|     |     |     | testing accuracy | comparable | to that of | the LSTM with- |
| --- | --- | --- | ---------------- | ---------- | ---------- | -------------- |
3.3.UseofTimeEncoding out any time encoding method applied. However, our
LeTEachievessignificantlyhigherimageclassificationac-
Intimeseriesforecastingresearch,timeembeddingscalcu-
|     |     |     | curacy. ThissimpleexperimentdemonstratesthatLeTEcan |     |     |     |
| --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
latedbytimeencodingmodulesareusuallydirectlyadded
|     |     |     | efficientlyencodetimeinformationformodels. |     |     | Next,we |
| --- | --- | --- | ------------------------------------------ | --- | --- | ------- |
tofeatureembeddingsandfedintotheattentionmechanism present experiments applying LeTE to time series tasks,
| orTransformer(Vaswanietal.,2017). |     | Asaresult,theytypi- |     |     |     |     |
| --------------------------------- | --- | ------------------- | --- | --- | --- | --- |
dynamicgraphtasks,andreal-worldapplications.
callysharethesamedimensionsasthefeatureembeddings:
4.2.ExperimentsonTimeSeriesTasks
|     | x=TokenEncode(x)+TE(t)∈Rd. |     | (14) |     |     |     |
| --- | -------------------------- | --- | ---- | --- | --- | --- |
Fortimeseriesforecastingtasks,weselect5baselinemod-
Here,xrepresentstheinput,TokenEncodedenotesatoken elswherewecandirectlyreplacethetimeencodingmeth-
encoding function, TE denotes the time encoding, and d odswithLeTE:vanillaTransformer(Vaswanietal.,2017),
representsthedimensionofbothfeatureembeddingsand Pyraformer(Liuetal.,2021),Non-stationaryTransformer
timeembeddings. (Liuetal.,2022),MICN(Wangetal.,2023),andTimesNet
|            |                          |                    | (Wuetal.,2023).                      | Weconductlong-termforecastingtasks |     |              |
| ---------- | ------------------------ | ------------------ | ------------------------------------ | ---------------------------------- | --- | ------------ |
| In dynamic | graph representation     | learning research, | time                                 |                                    |     |              |
|            |                          |                    | onthesebaselinemodelsusing4datasets: |                                    |     | ETT,Weather, |
| embeddings | are usually concatenated | with node          | features                             |                                    |     |              |
Exchange(Laietal.,2018),andElectricity,coveringvarious
| andedgefeaturesaspartoftheinput. |     | Thisallowsformore |                      |                                   |     |     |
| -------------------------------- | --- | ----------------- | -------------------- | --------------------------------- | --- | --- |
|                                  |     |                   | real-worldscenarios. | Implementationdetailsandintroduc- |     |     |
flexibilityinthechoiceoftimeembeddingdimensions:
tionstobaselinesanddatasetsareprovidedinAppendixE.2.
WeapplyLeTEandadjustthehyperparameterpinallex-
x=NodeFeatures∥EdgeFeatures∥TE(t)∈Rdn+de+d.
perimentstocapturemorecomprehensivetimeinformation.
(15)
Wereporttheresultsinthemultivariatesetting,asshown
| Here,∥denotestheconcatenationoperation,whiled |     |     | ,d , |     |     |     |
| --------------------------------------------- | --- | --- | ---- | --- | --- | --- |
n e
|     |     |     | inTable1and5. | Becausethetimeembeddingsneedtobe |     |     |
| --- | --- | --- | ------------- | -------------------------------- | --- | --- |
anddrepresentthedimensionsofnodefeatures,edgefea-
addedtothefeatureembeddings,theymusthavethesame
tures,andtimeembeddings,respectively.
|     |     |     | dimensions | as the feature | embeddings. | Baseline models |
| --- | --- | --- | ---------- | -------------- | ----------- | --------------- |
commonlyapplyhand-craftedtimeencoding(HCTE)with
| 4.Experiments |     |     | Date-TimeFormatinputs(e.g.,ISO8601format,YYYY- |                 |     |               |
| ------------- | --- | --- | ---------------------------------------------- | --------------- | --- | ------------- |
|               |     |     | MM-DDHH:mm:ss).                                | Sinceourmethod, |     | likeFTE,takes |
4.1.TimeastheOnlyInput
UNIXtimestampsasinput,weincludeFTEinourexperi-
|     |     |     | mentsforcomparison. | Inourapproach,wetransformthe |     |     |
| --- | --- | --- | ------------------- | ---------------------------- | --- | --- |
Toevaluatetheperformanceofthetimeencodingmethodin
scenarioswheretheonlyinputistime,andtocomparedif- Date-TimeFormattimestampsintoUNIXtimestamps,en-
ferenttimerepresentationswhileminimizingtheinfluence codethemwithourproposedLeTE,andfeedtheresulting
ofextraneousvariables,wefollow(Kazemietal.,2019)and time embeddings into the models in the same manner as
create a sequential (event-based) MNIST dataset (Fatahi the baselines. In this context, the input consists of abso-
etal.,2016;Camposetal.,2018;Bellecetal.,2018)and lute timestamps, and the time encoding can therefore be
conductimageclassificationtask(moredetailsareshown regardedasanabsolutetimeencoding.
inAppendixE.1).
|     |     |     | Fromtheexperimentalresults,weobservethat: |     |     | (1)When |
| --- | --- | --- | ----------------------------------------- | --- | --- | ------- |
applyingdifferenttimeencodingmethodstobaselinemod-
| 1.0 |     |     | elsfortimeseriesforecasting,LeTEoutperformsthebench- |     |     |     |
| --- | --- | --- | ---------------------------------------------------- | --- | --- | --- |
|     |     | 1.4 | LSTM                                                 |     |     |     |
0.9 1.2 L S T M + F T E markinmostcases,achievinganaveragewinrateof98%
L S T M + L eT E
1.0
| ycaruccA 0.8 |     |     | onMAE(MeanAbsoluteError)and95%onMSE(Mean |     |     |     |
| ------------ | --- | --- | ---------------------------------------- | --- | --- | --- |
ssoL 0.8
SquaredError)acrossallbaseline,dataset,andprediction
| 0.7 |     | 0.6 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0.4
0.6 LSTM lengthcombinations,highlightingtheeffectivenessofthe
|     | LSTM+FTE | 0.2 |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- |
LSTM+LeTE proposedtimeencoding. Thisdemonstratesthatourmethod
| 0.5 |     | 0.0 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
0 50 100 150 200 0 50 100 150 200 canbeseamlesslytransferredtotimeseriesmodels,reliably
|     | Epoch | Epoch |     |     |     |     |
| --- | ----- | ----- | --- | --- | --- | --- |
(a)TestingAccuracy (b)TestingLoss achieving strong performance. (2) The improvements on
|     |     |     | baselinesareconsiderable. |     | Forinstance,applyingLeTEto |     |
| --- | --- | --- | ------------------------- | --- | -------------------------- | --- |
Figure3.Timeastheonlyinput:Comparisonoftimeencodings theTransformermodelreducestheaverageMAEandMSE
onsequentialMNIST. acrossalldatasetsby25.1%and46.5%,respectively. This
6

RethinkingTimeEncodingviaLearnableTransformationFunctions
Table1.Timeseriesprediction:multivariatelong-termforecastingtask.Thepastsequencelengthissetto96,whilethepredictionlengths
are{96,192,336,720}.TheresultsarereportedintermsofMAE,wherelowervaluesindicatebetterperformance.HCTE(Hand-Crafted
TimeEncoding)isamethodwidelyadoptedintimeseriesresearch.FTEstandsforFunctionalTimeEncoding.Thewinraterepresents
thepercentageofcaseswhereLeTEoutperformstheHCTE.Thebestresultsforeachbaseline,datasetandpredictionlengthcombinations
areinbold.ETTconsistsof4subsets.Here,wepresenttheaverageresultsacrossthesesubsets,withthefullresultsprovidedinTable7.
MAE Transformer Pyraformer NSTrans. MINC TimesNet Win
TE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE Rate
96 0.797 0.803 0.550 0.642 0.720 0.583 0.405 0.435 0.377 0.405 0.367 0.350 0.355 0.362 0.352
192 1.139 0.916 0.712 0.899 0.924 0.738 0.445 0.478 0.414 0.445 0.423 0.395 0.385 0.400 0.388
336 1.119 0.938 0.821 1.043 1.038 0.863 0.478 0.539 0.449 0.478 0.486 0.448 0.421 0.424 0.413
TTE 95%
720 1.070 1.146 0.878 1.196 1.189 0.959 0.526 0.557 0.490 0.526 0.561 0.505 0.455 0.455 0.429
96 0.357 0.375 0.347 0.376 0.375 0.365 0.273 0.275 0.265 0.269 0.263 0.254 0.272 0.272 0.267
192 0.367 0.402 0.353 0.391 0.385 0.372 0.286 0.292 0.278 0.285 0.278 0.271 0.289 0.281 0.277
336 0.370 0.425 0.357 0.399 0.401 0.369 0.304 0.300 0.293 0.304 0.298 0.294 0.300 0.308 0.291
yticirtcelE
100%
720 0.374 0.453 0.363 0.390 0.394 0.380 0.321 0.330 0.317 0.321 0.330 0.317 0.320 0.363 0.316
96 0.575 0.705 0.547 0.570 0.641 0.624 0.237 0.261 0.237 0.235 0.233 0.203 0.234 0.237 0.230
192 0.747 0.791 0.744 0.803 0.815 0.786 0.335 0.369 0.319 0.316 0.332 0.289 0.344 0.339 0.332
336 0.945 1.123 0.879 0.903 0.991 0.859 0.476 0.501 0.439 0.407 0.472 0.402 0.448 0.472 0.446
egnahcxE
95%
720 1.329 1.147 1.066 1.075 1.046 0.938 0.769 0.901 0.612 0.658 0.710 0.622 0.746 0.756 0.751
96 0.422 0.257 0.245 0.303 0.296 0.267 0.223 0.222 0.221 0.229 0.258 0.225 0.220 0.221 0.215
192 0.523 0.308 0.295 0.336 0.317 0.311 0.285 0.271 0.260 0.281 0.306 0.261 0.261 0.263 0.253
336 0.607 0.355 0.365 0.403 0.377 0.349 0.338 0.321 0.308 0.331 0.335 0.295 0.306 0.302 0.299
rehtaeW
100%
720 0.690 0.459 0.429 0.434 0.417 0.415 0.410 0.357 0.349 0.356 0.387 0.339 0.359 0.350 0.348
WinRate 100% 94% 100% 100% 94% 98%
Table2.Dynamicgraphlinkpredictiontask:TheresultsarereportedinAP,wherehighervaluesindicatebetterperformance.Thebetter
resultsareinbold.Here,wepresentthetop-performingresultsacrossvariationsofLeTE,withthefullresultsprovidedinTable9.FTE
representsFunctionalTimeEncodingwhichiscommonlyusedindynamicgraphresearch.
AP Wikipedia Reddit MOOC LastFM
TE Transductive Inductive Transductive Inductive Transductive Inductive Transductive Inductive
FTE 96.95±0.24 96.33±0.26 98.53±0.04 97.01±0.05 85.34±0.19 84.94±0.04 72.73±0.11 77.78±0.13
TGAT
LeTE 97.82±0.09 97.34±0.08 98.56±0.01 97.05±0.06 88.31±0.10 88.37±0.12 76.22±0.25 81.32±0.14
FTE 98.45±0.06 97.83±0.04 98.63±0.06 97.50±0.07 89.15±1.60 89.04±1.17 77.07±3.97 81.45±4.29
TGN
LeTE 98.78±0.07 98.19±0.09 98.74±0.00 97.65±0.04 91.41±0.55 90.87±0.83 83.64±2.00 87.55±1.88
FTE 96.47±0.16 96.22±0.17 97.53±0.02 94.09±0.07 82.38±0.24 80.60±0.22 67.27±2.16 73.53±1.66
TCL
LeTE 98.19±0.04 97.89±0.03 97.78±0.03 94.99±0.07 84.24±0.10 82.72±0.12 76.08±0.79 80.68±0.70
DyG- FTE 99.03±0.02 98.59±0.03 99.22±0.01 98.84±0.02 87.52±0.49 86.96±0.43 93.00±0.12 94.23±0.09
Former LeTE 99.13±0.02 98.73±0.00 99.24±0.01 98.86±0.01 88.70±0.21 88.39±0.15 93.64±0.10 94.69±0.12
illustratesthatourmethodcanbeappliedtovarioustimese- baseline methods and datasets are in Appendix E.3. The
riesforecastingmodels,consistentlyachievingstrongperfor- resultsarereportedinbothtransductiveandinductiveset-
mance. (3)FTEcanoccasionallyoutperformbenchmarks; tings,asshowninTables2and6. Inthiscontext,thetime
however,italsofailsinmanycases,whereasLeTEsteadily encodingmoduletakestherelativetimedifferencebetween
outperforms benchmarks in such situations. This demon- thecurrentedgeandthemostrecentpreviousedge,andcan
stratesourmethod’scapabilitytomodeldiversetimepat- thereforeberegardedasarelativetimeencoding.
terns, including periodic, non-periodic, and mixed, high-
As shown in the experimental results, our proposed
lightingitsgeneralizabilityacrossdifferentmodelsanddata.
LeTEsurpassesthebenchmarkresultsonallcombinations
ofbaselinesanddatasets,regardlessoftransductiveorinduc-
4.3.ExperimentsonDynamicGraphTasks
tivesettings,achievingstate-of-the-art(SOTA)performance.
FTEsarewidelyusedindynamicgraphrepresentationlearn- Thisstronglydemonstratestheeffectivenessofourproposed
ingmodels. RepresentativeworksincludeTGAT(Xuetal., timeencodingandhighlightsitspotentialforimprovingthe
2020),TGN(Rossietal.,2020),TCL(Wangetal.,2021), representationlearningofdynamicgraphs. Thedimensions
and DyGFormer (Yu et al., 2023). Thus, we apply these forthemainexperimentsaresetto100,followingtheorigi-
modelsasbaselinesandreplacetheirtimeencodingswith nalsettingsinpreviouswork(Rossietal.,2020;Yuetal.,
ourLeTE.Weconductlinkpredictionexperimentson4real- 2023). However,sincetimeembeddingsareconcatenated
world datasets: Wikipedia, Reddit, MOOC, and LastFM withnodeandedgefeaturesindynamicgraphmodels,this
(Kumar et al., 2019). The details of the implementation, providessignificantflexibilityinsettingtheirdimensions.
7

RethinkingTimeEncodingviaLearnableTransformationFunctions
67.0 200 25 99.00 92.00
w.o. Time Encoding
66.5 F L T eT E E (Ours) 192 24.21 98.30 90.40
190 24
66.0 65.81 97.60 88.80
182
65.5 65.26 180 23 22.95 96.90 87.20
65.0 64.75 175 22.06 96.20 L F L L F L TT e e e e T T T T EE E E E E TT T I T I rr nn aa rr dd nn aa uu nn ss.. cc ss. . . . 85.60 L F L L F L TT e e e e T T T T EE E E E E TT T I T I rr nn aa rr dd nn aa uu nn ss.. cc ss. . . .
64.5 170 22 95.50 FFTTEE IInndduucc.. 84.00 FFTTEE IInndduucc..
2 8 16 32 64 100 2 8 16 32 64 100
64.0
160 21 (a)Wikipedia/TGN (b)MOOC/TGN
63.5
63.0 150 20
AUC-ROC(%) TP10 Recall@10(%) Figure5.Average Precision results comparing different dimen-
sionsoftheFTEandSpline-basedLeTEonWikipedia/TGNand
Figure4.ResultsevaluatedbyAUC-ROC,TP10andRecall@10 MOOC/TGN.
onrealbusinessdatasets.
4.5.DimensionsofTimeEncoding
Wecomparetheeffectsoftimeembeddingswithdifferent
ComparedtothepreviousFTEmethods, ourLeTEtakes
dimensionsinSection4.5. Acomparisonandanalysisof
a step forward by making the non-linear transformation
thevariationsofLeTEarealsoprovidedinAppendixG.2.
learnable, thereby generalizing the time encoding. Since
part of the information from the data is captured by the
4.4.ExperimentsonReal-WorldApplication
learnablenon-lineartransformation,wehypothesizethatus-
Timeinformationplaysacrucialroleinmanyreal-world inglower-dimensionalLeTEmaystilloutperformtheFTE
fields. WeapplyourproposedLeTEinareal-worldfinan- (whichreliesonafixednon-lineartransformation). There-
cial risk control scenario to demonstrate its effectiveness fore,weconductexperimentswithlower-dimensionaltime
inpracticalapplications. Infinancialriskcontrol,auser’s encodings. Since the dimensionality of time encoding in
historicaltransactiondataistypicallyusedtopredicttheir dynamic graph tasks is more flexible, we conduct exper-
creditrisk,whichcanbeframedasaclassificationproblem iments on dynamic graph link prediction tasks, with the
based on historical transaction information. However, in results presented in Figures 5, 6, and 7. As illustrated in
this scenario, users’ transaction behaviors often exhibit a the results, models using the FTE suffer from severe per-
combinationofcomplexperiodicandnon-periodicpatterns. formancedegradationasthedimensiondecreases,whereas
Forinstance,usersmayregularlyreceivesalarydepositsand modelswithLeTEdemonstratemorestableperformance
purchasedailynecessities,whereaspeer-to-peertransfers andconsistentlyoutperformthoseusingtheFTE,evenat
may lack strong periodicity. Using financial risk control lowerdimensions. Notably,modelsusingLeTEwithsig-
datafromTencentMobilePayment1,weconductcompar- nificantly lower dimensions (e.g., 2, 8 or 16) outperform
ativeexperimentswithouttimeinformation,withtheFTE, modelswiththe100-dimensionalFTE.Thisdemonstrates
andwithLeTEtoencodetimeinformation. Thebackbone theeffectivenessandgeneralizabilityofourmethod.
modeltreatsthetimeembeddingasafeature,concatenates
itwiththeuser’srawfeatures,andtakestheconcatenated 4.6.AdditionalExperiments
featuresasinput. Theobjectiveistouseusers’historical
We provide the complete experimental results for the ex-
transactiondatatopredictwhethertheyhavedefaultrisk.
perimentsmentionedinthemaintextinAppendixF.Ad-
DetailsofthedatasetareprovidedinAppendixE.4. The
ditionally, weconductfurtherexperimentstoanalyzethe
resultsarepresentedinFigure4. Theresultsindicatethat
complex time patterns in real-world data (cf. Appendix
themodelwithouttimeencodingperformstheworst,asit
G.1); compare different variants of LeTE (cf. Appendix
completelyignorestimeinformation. WithFTE,theperi-
G.2);illustratetheinterpretabilityofLeTE(cf. Appendix
odicityofuserbehavioratdifferentfrequenciesiscaptured,
G.3); demonstrate LeTE’s ability to simultaneously cap-
resulting in improved performance compared to the case
turediversetimepatterns,includingperiodic,non-periodic,
withouttimeinformation. UsingLeTEyieldsthebestper-
and mixed ones (cf. Appendix G.4); and assess LeTE’s
formance,asourtimeencodingeffectivelymodelsperiodic,
capabilitytofitvariousfunctions(cf. AppendixG.5).
non-periodicandmixedpatternsinamoregeneralmanner.
1The data used in these experiments are properly sampled
5.Conclusion
only for testing purposes and does not imply any commercial
information. Allusers’privateinformationisremovedfromthe
In this paper, we propose a effective time encod-
dataset. Moreover, the experiments were conducted locally on
Tencent’sserverbyformalemployeeswhostrictlyfolloweddata ingmethod—LearnableTransformation-basedGeneralized
protectionregulations. TimeEncoding(LeTE)—designedtoacceptbothabsolute
8

RethinkingTimeEncodingviaLearnableTransformationFunctions
timestampsandrelativetimedifferencesasinputs,depend- neuralnetworks. InTheSixthInternationalConference
ing on the specific requirements of different models, en- onLearningRepresentations,2018.
ablingittofunctionaseitheranabsoluteorarelativetime
Chen,X.,Liao,Y.,Xiong,Y.,Zhang,Y.,Zhang,S.,Zhang,
| encoding | method. Through | comprehensive | analysis, we |     |     |     |     |     |     |     |
| -------- | --------------- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
demonstratethatourproposedLeTEiscapableofmodel- J.,andSun,Y. Speed: Streamingpartitionandparallel
accelerationfortemporalinteractiongraphembedding.
ingdiverseandcomplextimepatterns,includingperiodic,
arXivpreprintarXiv:2308.14129,2023.
| non-periodic, | and mixed patterns. | It is | invariant to time |     |     |     |     |     |     |     |
| ------------- | ------------------- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
rescaling, sufficiently simple for integration with various Chen,X.,Xiong,Y.,Zhang,S.,Zhang,J.,Zhang,Y.,Zhou,
backbonemodels,andexhibitsgoodinterpretabilityanddi-
|                      |                                   |     |     | S.,Wu,X.,Zhang,M.,Liu,T.,andWang,W. |     |     |     |     |     | Dtformer: |
| -------------------- | --------------------------------- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --------- |
| mensionalefficiency. | Extensiveexperimentsonevent-based |     |     |                                     |     |     |     |     |     |           |
Atransformer-basedmethodfordiscrete-timedynamic
imageclassification,time-seriesforecastingtasks,dynamic
|     |     |     |     | graph | representation |     | learning. | In  | Proceedings | of the |
| --- | --- | --- | --- | ----- | -------------- | --- | --------- | --- | ----------- | ------ |
graphlinkpredictiontasks,andreal-worldfinancialriskcon-
33rdACMInternationalConferenceonInformationand
trolapplicationsdemonstratethesuperiorperformanceand KnowledgeManagement,pp.301–311,2024a.
| generalizability | of our method | across various | application |     |     |     |     |     |     |     |
| ---------------- | ------------- | -------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
scenarios. Chen, X., Zhang, S., Xiong, Y., Wu, X., Zhang, J., Sun,
|     |     |     |     | X., Zhang, | Y.,      | Zhao,       | F., and | Kang,   | Y. Prompt | learn-   |
| --- | --- | --- | --- | ---------- | -------- | ----------- | ------- | ------- | --------- | -------- |
|     |     |     |     | ing on     | temporal | interaction |         | graphs. | arXiv     | preprint |
Acknowledgements
arXiv:2402.06326,2024b.
ThisworkispartiallysupportedbytheNoncommunicable
ChronicDiseases-NationalScienceandTechnologyMajor Cho,K. Learningphraserepresentationsusingrnnencoder-
|     |     |     |     | decoderforstatisticalmachinetranslation. |     |     |     |     | InProceed- |     |
| --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | ---------- | --- |
Project(NO.2024ZD0532400andNO.2024ZD0532403).
|     |     |     |     | ings of | the 2014 | Conference |     | on Empirical | Methods | in  |
| --- | --- | --- | --- | ------- | -------- | ---------- | --- | ------------ | ------- | --- |
ThisworkissponsoredbytheTencentRhino-BirdFocused
ResearchProgram. ThisworkispartiallysupportedbyNSF NaturalLanguageProcessing,pp.1724–1734,2014.
throughgrantIIS-2106972.
Choi,E.,Bahadori,M.T.,Schuetz,A.,Stewart,W.F.,and
|     |     |     |     | Sun,J. | Doctorai: | Predictingclinicaleventsviarecurrent |     |     |     |     |
| --- | --- | --- | --- | ------ | --------- | ------------------------------------ | --- | --- | --- | --- |
ImpactStatement neural networks. In Machine learning for Healthcare
Conference,pp.301–318.PMLR,2016.
Thispaperpresentsworkwhosegoalistoadvancethefield
of Machine Learning. There are many potential societal Fatahi,M.,Ahmadi,M.,Shahsavari,M.,Ahmadi,A.,and
consequences of our work, none which we feel must be Devienne, P. evt mnist: A spike based version of tra-
specificallyhighlightedhere. ditionalmnist. In1stInternationalConferenceonNew
ResearchAchievementsinElectricalandComputerEngi-
neering,2016.
References
Gehring,J.,Auli,M.,Grangier,D.,Yarats,D.,andDauphin,
Baytas,I.M.,Xiao,C.,Zhang,X.,Wang,F.,Jain,A.K.,and
Zhou,J. Patientsubtypingviatime-awarelstmnetworks. Y.N. Convolutionalsequencetosequencelearning. In
InternationalConferenceonMachineLearning,pp.1243–
InProceedingsofthe23rdACMSIGKDDInternational
| ConferenceonKnowledgeDiscoveryandDataMining, |     |     |     | 1252.PMLR,2017. |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
pp.65–74,2017.
|     |     |     |     | Graves,A.andGraves,A. |     |     | Longshort-termmemory. |     |     | Su- |
| --- | --- | --- | --- | --------------------- | --- | --- | --------------------- | --- | --- | --- |
Bellec,G.,Salaj,D.,Subramoney,A.,Legenstein,R.,and pervisedSequenceLabellingwithRecurrentNeuralNet-
works,pp.37–45,2012.
| Maass,                           | W. Long short-term | memory           | and learning-to- |             |     |          |     |                |     |            |
| -------------------------------- | ------------------ | ---------------- | ---------------- | ----------- | --- | -------- | --- | -------------- | --- | ---------- |
| learninnetworksofspikingneurons. |                    | AdvancesinNeural |                  |             |     |          |     |                |     |            |
|                                  |                    |                  |                  | Kang, W.-C. | and | McAuley, | J.  | Self-attentive |     | sequential |
InformationProcessingSystems,31,2018.
recommendation.In2018IEEEInternationalConference
Bengio,Y.,Courville,A.,andVincent,P. Representation onDataMining,pp.197–206.IEEE,2018.
| learning: | Areviewandnewperspectives. |     | IEEETransac- |         |        |       |              |     |          |         |
| --------- | -------------------------- | --- | ------------ | ------- | ------ | ----- | ------------ | --- | -------- | ------- |
|           |                            |     |              | Kazemi, | S. M., | Goel, | R., Eghbali, | S., | Ramanan, | J., Sa- |
tionsonPatternAnalysisandMachineIntelligence,35
hota,J.,Thakur,S.,Wu,S.,Smyth,C.,Poupart,P.,and
(8):1798–1828,2013.
Brubaker,M.Time2vec:Learningavectorrepresentation
Braun,J.andGriebel,M. Onaconstructiveproofofkol- oftime. arXivpreprintarXiv:1907.05321,2019.
| mogorov’ssuperpositiontheorem. |     | Constructiveapproxi- |     |         |       |       |           |              |     |            |
| ------------------------------ | --- | -------------------- | --- | ------- | ----- | ----- | --------- | ------------ | --- | ---------- |
|                                |     |                      |     | Kazemi, | S.M., | Goel, | R., Jain, | K., Kobyzev, | I., | Sethi, A., |
mation,30:653–675,2009.
|     |     |     |     | Forsyth,P.,andPoupart,P. |     |     | Representationlearningfor |     |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --- | ------------------------- | --- | --- | --- |
Campos,V.,Jou,B.,Giro´-iNieto,X.,Torres,J.,andChang, dynamicgraphs: Asurvey. JournalofMachineLearning
S.-F. Skiprnn: Learningtoskipstateupdatesinrecurrent Research,21(70):1–73,2020.
9

RethinkingTimeEncodingviaLearnableTransformationFunctions
Kolmogorov, A. N. On the representation of continuous Misra,D. Mish: Aselfregularizednon-monotonicactiva-
functionsofmanyvariablesbysuperpositionofcontin- tionfunction. arXivpreprintarXiv:1908.08681,2019.
| uous functions | of  | one variable | and | addition. | In Dok- |            |             |     |          |         |             |     |
| -------------- | --- | ------------ | --- | --------- | ------- | ---------- | ----------- | --- | -------- | ------- | ----------- | --- |
|                |     |              |     |           |         | Murat, M., | Malinowska, |     | I., Gos, | M., and | Krzyszczak, | J.  |
ladyAkademiiNauk,volume114,pp.953–956.Russian
Forecastingdailymeteorologicaltimeseriesusingarima
AcademyofSciences,1957.
|             |       |        |                |     |            | andregressionmodels. |     |     | InternationalAgrophysics,32(2), |     |     |     |
| ----------- | ----- | ------ | -------------- | --- | ---------- | -------------------- | --- | --- | ------------------------------- | --- | --- | --- |
| Kolmogorov, | A. N. | On the | representation | of  | continuous | 2018.                |     |     |                                 |     |     |     |
functionsofseveralvariablesbysuperpositionsofcontin-
|                                           |     |     |     |     |        | Neumann, | O., Beichter, |     | M., Heidrich, | B., | Friederich, | N., |
| ----------------------------------------- | --- | --- | --- | --- | ------ | -------- | ------------- | --- | ------------- | --- | ----------- | --- |
| uousfunctionsofasmallernumberofvariables. |     |     |     |     | Ameri- |          |               |     |               |     |             |     |
canMathematicalSociety,1961. Hagenmeyer, V., and Mikut, R. Intrinsic explainable
artificialintelligenceusingtrainablespatialweightson
Kumar,S.,Zhang,X.,andLeskovec,J. Predictingdynamic numericalweatherpredictions.InProceedingsofthe15th
embeddingtrajectoryintemporalinteractionnetworks. ACMInternationalConferenceonFutureandSustainable
InProceedingsofthe25thACMSIGKDDInternational EnergySystems,pp.551–559,2024.
ConferenceonKnowledgeDiscoveryandDataMining,
|     |     |     |     |     |     | Pennebaker,J.W. |     | Linguisticinquiryandwordcount: |     |     |     | Liwc |
| --- | --- | --- | --- | --- | --- | --------------- | --- | ------------------------------ | --- | --- | --- | ---- |
pp.1269–1278,2019.
2001,2001.
Kwon,B.C.,Choi,M.-J.,Kim,J.T.,Choi,E.,Kim,Y.B.,
|       |              |          |               |     |            | Radford,           | A., Wu, | J., Child,                    | R., | Luan, | D., Amodei, | D., |
| ----- | ------------ | -------- | ------------- | --- | ---------- | ------------------ | ------- | ----------------------------- | --- | ----- | ----------- | --- |
| Kwon, | S., Sun, J., | andChoo, | J. Retainvis: |     | Visualana- |                    |         |                               |     |       |             |     |
|       |              |          |               |     |            | Sutskever,I.,etal. |         | Languagemodelsareunsupervised |     |       |             |     |
lyticswithinterpretableandinteractiverecurrentneural
|                                     |               |     |          |              |        | multitasklearners. |     | OpenAIblog,1(8):9,2019. |     |     |     |     |
| ----------------------------------- | ------------- | --- | -------- | ------------ | ------ | ------------------ | --- | ----------------------- | --- | --- | --- | --- |
| networksonelectronicmedicalrecords. |               |     |          | IEEETransac- |        |                    |     |                         |     |     |     |     |
| tions on                            | Visualization | and | Computer | Graphics,    | 25(1): |                    |     |                         |     |     |     |     |
Rossi,E.,Chamberlain,B.,Frasca,F.,Eynard,D.,Monti,
299–309,2018. F., and Bronstein, M. Temporal graph networks for
|                                      |     |     |     |               |     | deep learning |     | on dynamic | graphs. |     | arXiv | preprint |
| ------------------------------------ | --- | --- | --- | ------------- | --- | ------------- | --- | ---------- | ------- | --- | ----- | -------- |
| Lai,G.,Chang,W.-C.,Yang,Y.,andLiu,H. |     |     |     | Modelinglong- |     |               |     |            |         |     |       |          |
arXiv:2006.10637,2020.
| and short-term | temporal |     | patterns | with deep | neural net- |     |     |     |     |     |     |     |
| -------------- | -------- | --- | -------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
InThe41stInternationalACMSIGIRConference
| works. |     |     |     |     |     | Shannon,C.E. | Amathematicaltheoryofcommunication. |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | ------------ | ----------------------------------- | --- | --- | --- | --- | --- |
onResearch&DevelopmentinInformationRetrieval,pp. TheBellSystemTechnicalJournal,27(3):379–423,1948.
95–104,2018.
|           |            |      |                    |     |             | Skarding,J.,Gabrys,B.,andMusial,K. |     |     |     |     | Foundationsand |     |
| --------- | ---------- | ---- | ------------------ | --- | ----------- | ---------------------------------- | --- | --- | --- | --- | -------------- | --- |
| Lezmi, E. | and Xu, J. | Time | series forecasting |     | with trans- |                                    |     |     |     |     |                |     |
modelingofdynamicnetworksusingdynamicgraphneu-
former models and application to asset management. ralnetworks: Asurvey. IEEEAccess,9:79143–79168,
| AvailableatSSRN4375798,2023. |     |     |     |     |     | 2021. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Li,Y.,Du,N.,andBengio,S. Time-dependentrepresenta- Tallec,C.andOllivier,Y. Canrecurrentneuralnetworks
tionforneuraleventsequenceprediction. arXivpreprint The Sixth International Conference on
|                        |     |     |     |     |     | warp time?                    | In  |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
| arXiv:1708.00065,2017. |     |     |     |     |     | LearningRepresentations,2018. |     |     |     |     |     |     |
Liu,S.,Yu,H.,Liao,C.,Li,J.,Lin,W.,Liu,A.X.,andDust- Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,
dar,S. Pyraformer: Low-complexitypyramidalattention L.,Gomez,A.N.,Kaiser,Ł.,andPolosukhin,I. Atten-
| forlong-rangetimeseriesmodelingandforecasting. |     |     |     |     | In  |         |         |       |          |           |             |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | ------- | ------- | ----- | -------- | --------- | ----------- | --- |
|                                                |     |     |     |     |     | tion is | all you | need. | Advances | in Neural | Information |     |
TheNinthInternationalConferenceonLearningRepre- ProcessingSystems,30,2017.
sentations,2021.
Wang,H.,Peng,J.,Huang,F.,Wang,J.,Chen,J.,andXiao,
Liu, Y., Wu, H., Wang, J., and Long, M. Non-stationary Y. Micn: Multi-scale local and global context model-
| transformers: | Exploring |     | the stationarity | in  | time series |         |           |        |              |     |        |          |
| ------------- | --------- | --- | ---------------- | --- | ----------- | ------- | --------- | ------ | ------------ | --- | ------ | -------- |
|               |           |     |                  |     |             | ing for | long-term | series | forecasting. |     | In The | Eleventh |
forecasting. AdvancesinNeuralInformationProcessing InternationalConferenceonLearningRepresentations,
| Systems,35:9881–9893,2022. |     |     |     |     |     | 2023. |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Liu, Y., Hu, T., Zhang, H., Wu, H., Wang, S., Ma, L., Wang,L.,Chang,X.,Li,S.,Chu,Y.,Li,H.,Zhang,W.,He,
and Long, M. itransformer: Inverted transformers are X.,Song,L.,Zhou,J.,andYang,H. Tcl: Transformer-
effectivefortimeseriesforecasting. InTheTwelfthInter- baseddynamicgraphmodellingviacontrastivelearning.
nationalConferenceonLearningRepresentations,2023. arXivpreprintarXiv:2105.07944,2021.
Liu, Z., Wang, Y., Vaidya, S., Ruehle, F., Halverson, Wu, H., Hu, T., Liu, Y., Zhou, H., Wang, J., and Long,
J., Soljacˇic´, M., Hou, T. Y., and Tegmark, M. Kan: M. Timesnet: Temporal2d-variationmodelingforgen-
Kolmogorov-arnoldnetworks. InTheThirteenthInterna- eraltimeseriesanalysis. InTheEleventhInternational
tionalConferenceonLearningRepresentations,2025. ConferenceonLearningRepresentations,2023.
10

RethinkingTimeEncodingviaLearnableTransformationFunctions
| Xu, D., Ruan,     | C.,      | Korpeoglu, | E.,        | Kumar,      | S., and        | Achan, |
| ----------------- | -------- | ---------- | ---------- | ----------- | -------------- | ------ |
| K. Self-attention |          | with       | functional | time        | representation |        |
| learning.         | Advances | in         | Neural     | Information | Processing     |        |
Systems,32,2019.
Xu,D.,Ruan,C.,Korpeoglu,E.,Kumar,S.,andAchan,K.
| Inductiverepresentationlearningontemporalgraphs. |     |     |     |     |     | In  |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
TheEighthInternationalConferenceonLearningRepre-
sentations,2020.
| Yu,L.,Sun,L.,Du,B.,andLv,W. |        |                                   |     | Towardsbetterdynamic |          |     |
| --------------------------- | ------ | --------------------------------- | --- | -------------------- | -------- | --- |
| graphlearning:              |        | Newarchitectureandunifiedlibrary. |     |                      |          | Ad- |
| vances in                   | Neural | Information                       |     | Processing           | Systems, | 36: |
67686–67700,2023.
| Zeng, C., | Tian, | Y., Zheng, | G., and | Gao, | Y. How | much |
| --------- | ----- | ---------- | ------- | ---- | ------ | ---- |
cantime-relatedfeaturesenhancetimeseriesforecasting?
arXivpreprintarXiv:2412.01557,2024.
| Zhang, J.                          | Rpn: | Reconciled | polynomial | network |               | towards |
| ---------------------------------- | ---- | ---------- | ---------- | ------- | ------------- | ------- |
| unifyingpgms,kernelsvms,mlpandkan. |      |            |            |         | arXivpreprint |         |
arXiv:2407.04819,2024.
| Zhang, S.,                     | Xiong,  | Y., Zhang, | Y.,     | Sun, Y.,           | Chen, X.,      | Jiao, |
| ------------------------------ | ------- | ---------- | ------- | ------------------ | -------------- | ----- |
| Y., and                        | Zhu, Y. | Rdgsl:     | Dynamic | graph              | representation |       |
| learningwithstructurelearning. |         |            |         | InProceedingsofthe |                |       |
32ndACMInternationalConferenceonInformationand
KnowledgeManagement,pp.3174–3183,2023a.
Zhang,S.,Chen,X.,Xiong,Y.,Wu,X.,Zhang,Y.,Fu,Y.,
| Zhao,Y.,andZhang,J.                           |     |     | Towardsadaptiveneighborhood |     |     |     |
| --------------------------------------------- | --- | --- | --------------------------- | --- | --- | --- |
| foradvancingtemporalinteractiongraphmodeling. |     |     |                             |     |     | In  |
Proceedingsofthe30thACMSIGKDDConferenceon
KnowledgeDiscoveryandDataMining,pp.4290–4301,
2024.
Zhang,S.,Xiong,Y.,Tang,Y.,Chen,X.,Jia,Z.,Gu,Z.,Xu,
| J.,andZhang,J. |     | Unifyingtextsemanticsandgraphstruc- |     |     |     |     |
| -------------- | --- | ----------------------------------- | --- | --- | --- | --- |
turesfortemporaltext-attributedgraphswithlargelan-
arXivpreprintarXiv:2503.14411,2025.
guagemodels.
Zhang,Y.,Xiong,Y.,Liao,Y.,Sun,Y.,Jin,Y.,Zheng,X.,
andZhu,Y.Tiger:Temporalinteractiongraphembedding
| withrestarts. | InProceedingsoftheACMWebConference |     |     |     |     |     |
| ------------- | ---------------------------------- | --- | --- | --- | --- | --- |
2023,pp.478–488,2023b.
11

RethinkingTimeEncodingviaLearnableTransformationFunctions
A.RelatedWork
Currently,commonlyusedtimeencodingmethodsorstrategiesformodelingtemporalinformationcanbebroadlycategorized
intotwotypes: Hand-CraftedTimeEncodings(HCTE)andFunctionalTimeEncodings(FTE).
HCTEinvolvesmanuallydesignedtemporalencodingstailoredtospecificdownstreamtasks. Thesemethodsrelyonspecific
designchoicesandincorporatevariousinductivebiasestocapturefixedperiodicpatterns,constructinghand-craftedtemporal
features. ThesefeaturesaretypicallyfedintomodelssuchasRNNs(Cho,2014)orsequentialarchitectures(Liuetal.,2021;
2022;Wangetal.,2023;Wuetal.,2023)tomeetspecificmodelingrequirements(Choietal.,2016;Baytasetal.,2017;
Kwonetal.,2018),asillustratedinFigure1(a). Suchapproachesareoftenemployedtoaddressparticularchallengesin
timeseriestasks.
Additionally,somemethodsinthiscategoryintegratetimeencodingdirectlywithattentionmechanisms(Vaswanietal.,
2017),simplifyingtemporalmodelingbyadoptingpositionencodingstrategies(Gehringetal.,2017). Othersembeddiscrete
eventsintoacontinuousvectorspacetobettercaptureeventcontextsinattention-basedmodels(Bengioetal.,2013;Li
etal.,2017). Thesemethods,whileeffective,areoftenlimitedtorepresentingfixedornarrowlydefinedtemporalpatterns.
FTErepresentsanadvancedandgeneralizedversionoftimeencoding,designedtoovercomepartofthelimitationsof
Hand-CraftedTimeEncodings. Tworepresentativeworksinthiscategoryarefunctionaltimerepresentation,proposedby
(Xuetal.,2019),andTime2Vec,proposedby(Kazemietal.,2019),asshowninFigure1(b). Importantly,thepreviously
mentionedpositionencodingmethodsintegratedwithattentionmechanismscanbeconsideredasimplifiedversionofFTE.
BothfunctionaltimerepresentationandTime2Vecadoptsimilarimplementationmethods,whichresembleaone-dimensional-
to-d-dimensionalMLPwithaspeciallydesignedtrigonometricnon-linearactivationfunction. InTime2Vec,experiments
comparingdifferentnon-linearactivationfunctionsdemonstratethatthesinefunctionperformsbestacrossvariousdown-
streamtasks. Despitelimitationsinmodelingrestrictedaspectsoftime,FTEiswidelyadoptedindynamicgraphrepresenta-
tionlearningduetoitseaseofapplicationandeffectiveness(Rossietal.,2020;Zhangetal.,2023b;a;Chenetal.,2023;Yu
etal.,2023;Chenetal.,2024b;Zhangetal.,2024;Chenetal.,2024a;Zhangetal.,2025).
Time encodings can be directly applied to sequential models such as RNNs and LSTMs (Graves & Graves, 2012), or
easily integrated into attention-based architectures. In time series forecasting, for instance, many models now employ
transformer-basedstructures(Vaswanietal.,2017),wheretimeencodingisoftentreatedsimilarlytopositionencoding.
Thisisusuallyachievedbyaddingittotheinputoftheattentionmechanism(Liuetal.,2021;2022;Wuetal.,2023).
Dynamicgraphrepresentationlearningmodelsalsorequireprecisetemporalmodeling. Forexample,TGAT(Xuetal.,
2020)directlyreplacespositionencodingwithfunctionaltimerepresentationwithinitsattentionmechanism. Subsequent
methods,suchasTGNandTIGER(Rossietal.,2020;Zhangetal.,2023b),haveadoptedsimilarapproaches. DyGFormer
(Yuetal.,2023),whichappliesaTransformertodynamicgraphrepresentationlearning,usesthesameencodingmethodby
concatenatingitwithnodeandedgefeaturesbeforeprocessingthemwithaTransformer-basedmodel.
B.MethodsofParameterizeContinuousFunctions
B.1.FourierSeriesExpansion
Afunctionf(x)thatisperiodicwithperiodT andsatisfiescertainconditions(Dirichletconditions)canberepresentedasa
FourierSeries. Thisseriesrepresentsf(x)asaninfinitesumofsinesandcosines(or,equivalently,complexexponentials)
withspecificcoefficients. Theseriestakestheform:
∞ (cid:18) (cid:19)
(cid:88) 2πnx 2πnx
f(x)=a + a cos +b sin . (16)
0 n T n T
n=1
Here,a istheaveragevalueofthefunctionoveroneperiod,anda andb areFouriercoefficientsthatcanbecalculated
0 n n
byintegratingf(x)overtheinterval[0,T].
Thesecoefficientsaregivenby:
2 (cid:90) T 2πnx
a = f(x)cos dx, (17)
n T T
0
2 (cid:90) T 2πnx
b = f(x)sin dx. (18)
n T T
0
12

RethinkingTimeEncodingviaLearnableTransformationFunctions
Undertheseconditions,theFourierSeriesconvergestof(x)atallpointswheref iscontinuousandconvergestotheaverage
oftheleft-handandright-handlimitsatpointsofdiscontinuity.
B.2.KANandSplineFunctions
The Kolmogorov–Arnold Theorem (Kolmogorov, 1961; 1957; Braun & Griebel, 2009) states that for any continuous
multivariatefunctionf(x ,x ,...,x )ontheunitcube[0,1]n,thereexistcontinuousfunctionsϕ andψ suchthat:
1 2 n i ij
|     |     |    |    |     |     |
| --- | --- | --- | --- | --- | --- |
2n+1 (cid:88) (cid:88) n
| f(x 1 ,x | 2 ,...,x n )= | ϕ i | ψ ij (x j ), |     | (19) |
| -------- | ------------- | ---- | ------------- | --- | ---- |
i=1 j=1
whereϕ i arecontinuousfunctionsofasinglevariable,enablingdimensionalityreduction,andψ ij arecontinuousfunctions
mappingeachinputvariablex toasingleoutput,contributingtothesuperpositionstructure. Thistheoremimpliesthat
j
everycontinuousfunctionofmultiplevariablescanberepresentedasasumofcompositionsofunivariatefunctions.
BuildingontheKolmogorov–ArnoldTheoremandtheadvantagesofsplinesforfunctionfitting,Liuetal. proposeusing
splinestoconstructlearnablenon-linearactivationfunctionsforneuralnetworks(Liuetal.,2025). Webrieflyintroduce
B-splines here. Given a knot vector T = t 0 ,t 1 ,...,t m with non-decreasing values, the basis functions N i,p (x) for a
B-splineofdegreeparedefinedrecursivelyasfollows: Fordegreep=0:
(cid:40)
|     |            | 1 ift ≤x<t   |     |     |      |
| --- | ---------- | ------------ | --- | --- | ---- |
|     |            | i            | i+1 |     |      |
|     | N i,0 (x)= |              |     |     | (20) |
|     |            | 0 otherwise. |     |     |      |
Forhigherdegreesp>0:
| x−t    |       | t          | −x      |      |      |
| ------ | ----- | ---------- | ------- | ---- | ---- |
| N (x)= | i N   | (x)+ i+p+1 | N       | (x). | (21) |
| i,p    | i,p−1 |            | i+1,p−1 |      |      |
| t      | −t    | t          | −t      |      |      |
| i+p    | i     | i+p+1      | i+1     |      |      |
TheB-splinecurveC(x)ofdegreepwithcontrolpoints{P ,P ,...,P }isgivenby:
|     |     | 0 1 | n   |     |     |
| --- | --- | --- | --- | --- | --- |
n
(cid:88)
|     | C(x)= | N i,p (x)P | i . |     | (22) |
| --- | ----- | ---------- | --- | --- | ---- |
i=0
Here,N (x)aretheB-splinebasisfunctionsofdegreep,andP arethecontrolpointsthatinfluencetheshapeofthe
i,p i
curve.
C.Proofs
C.1.ProofofProposition2.1
C.1.1.DETAILSOFFUNCTIONALTIMEREPRESENTATIONANDTIME2VEC
FTRisdesignedtousethetimedifferencet=t i −t j ,where0≤t j ≤t i ≤t ,asinput. Fortheinputtimedifference,a
max
learnablefrequencyparameterisfirstapplied. Next,anon-lineartransformationisapplied,usingthecosinefunctiononthe
odddimensionsandthesinefunctionontheevendimensions. Thismethodismathematicallyrepresentedasfollows:
(cid:40)
|           | cos(ω | i t), if | iisodd,  |     |      |
| --------- | ----- | -------- | -------- | --- | ---- |
| TE(t)[i]= |       |          |          |     | (23) |
|           | sin(ω | t), if   | iiseven, |     |      |
i
wheredisthedimensionofthetimeencoding,1≤i≤d,andω arelearnableparametersrepresentingthefrequencyof
i
thetrigonometricfunctions. Sincethistimeencodingusestimedifferencesasinput,itcanbeconsideredasarelativetime
encoding.
T2Visdesignedtousetimestampstasinput.Alineartransformationisappliedtothefirstdimensiontocapturenon-periodic
timepatterns. Fortheremainingdimensions,alineartransformationisfollowedbyasine-basednon-lineartransformation
tomodelperiodictimepatterns: Mathematically,thismethodisrepresentedasfollows:
(cid:40)
|           | ω i t+φ | i ,    | if i=1,   |     |      |
| --------- | ------- | ------ | --------- | --- | ---- |
| TE(t)[i]= |         |        |           |     | (24) |
|           | sin(ω   | t+φ ), | if 2≤i≤d, |     |      |
i i
13

RethinkingTimeEncodingviaLearnableTransformationFunctions
whereTE(t)[i]istheithelementofthetimeencoding,andω andφ arelearnableparametersrepresentingfrequencyand
i i
phase-shiftofthesinefunction,respectively. Sincethistimeencodingtakestimestampsasinput,itcanbeconsideredasan
absolutetimeencoding.
C.1.2.PROOFOFPROPOSITION2.1
Proof. Since Equation (23) can be written as TE(t) = [cos(ω t),sin(ω t),...,cos(ω t),sin(ω t)], we show that the
|     |     |     |     |     |     | 1   | 1   | d   | d   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vector[cos(ω t),sin(ω t),...,cos(ω t),sin(ω t)]canbeexpressedintheformsin(ω t+φ )withsuitablephaseshifts
| 1   | 1   |     | d   |     | d   |     |     | i   | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
φ . Recallthetrigonometricidentity:
i (cid:16) π(cid:17)
|     |     |     |     |     | cos(θ)=sin | θ+  | .   |     |     | (25) |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ---- |
2
Applyingthisidentity,eachcosineterminthevectorcanberewrittenas:
|     |     |     |       |          | (cid:16) π(cid:17) |     |                  |     |     |      |
| --- | --- | --- | ----- | -------- | ------------------ | --- | ---------------- | --- | --- | ---- |
|     |     |     | cos(ω | i t)=sin | ω i t+             | ,   | for i=1,2,...,d. |     |     | (26) |
2
Thesinetermsarealreadyinthedesiredformwithazerophaseshift:
|     |     |     | sin(ω | t)=sin(ω | t+0), | for | i=1,2,...,d. |     |     | (27) |
| --- | --- | --- | ----- | -------- | ----- | --- | ------------ | --- | --- | ---- |
|     |     |     |       | i        | i     |     |              |     |     |      |
Withthesetransformations,theoriginalvectorbecomes:
|     |        | (cid:104) | (cid:16) | π(cid:17) |                     |     | (cid:16) π(cid:17) |             | (cid:105) |      |
| --- | ------ | --------- | -------- | --------- | ------------------- | --- | ------------------ | ----------- | --------- | ---- |
|     | TE(t)= | sin       | ω        | t+        | ,sin(ω t+0),...,sin |     | ω t+               | ,sin(ω t+0) | ,         | (28) |
|     |        |           | 1        | 2         | 1                   |     | d 2                | d           |           |      |
orequivalently,
|     |     |     |     |     | TE(t)=[sin(ω | t+φ | )]2d , |     |     | (29) |
| --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | --- | ---- |
i i i=1
wherethephaseshiftsφ aredefinedasfollows:
i
(cid:40)
π,
ifiisodd
|     |     |     |     |     | φ = 2 |            |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- |
|     |     |     |     |     | i 0,  | ifiiseven. |     |     |     |     |
C.2.ContinuedProofofProposition3.1
Thefunctionsin(θ)iscontinuousandinfinitelydifferentiable(i.e.,C∞)onR.
Proof. Thus,itiscontinuousonanyclosed
interval[a,b].
B-splinebasisfunctionsofdegreekformabasisforthespaceofpiecewisepolynomialfunctionsofdegreekwithcontinuity
Ck−1 at the knots. By the Weierstrass Approximation Theorem, any continuous function on a closed interval can be
uniformlyapproximatedbypolynomialstoanydesireddegreeofaccuracy.
SinceB-splinesarepiecewisepolynomials,theycanuniformlyapproximateanycontinuousfunctionon[a,b]. Specifically,
foranyϵ>0,thereexistsalinearcombinationofB-splinebasisfunctionsthatapproximatessin(θ)withinϵover[a,b].
To build the approximation of sin(ω t + φ ) using B-spline basis functions, we first select a knot vector T =
|     |     |     |     | i   | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{t ,t ,...,t }thatpartitionstheinterval[a,b]appropriately. Thechoiceoftheknotvectordeterminestheplacement
0 1 n+k+1
andspacingoftheknots,whichinturnaffecttheflexibilityandlocalsupportoftheB-splinebasisfunctions.
Next,wechoosethedegreekoftheB-splinebasisfunctionsbasedonthedesiredsmoothnessandapproximationquality.
A higher degree allows for smoother basis functions, potentially improving the approximation at the cost of increased
computationalcomplexity.
(θ)}M
Withtheknotvectoranddegreespecified,wegeneratetheB-splinebasisfunctions{B j ofdegreekusingstandard
j=1
recursivedefinitions. Thesebasisfunctionspossesslocalsupportandsatisfythepartitionofunityproperty,makingthem
suitableforapproximatingfunctionsover[a,b].
Todeterminethecoefficientsc thatyieldthebestapproximationofsin(ω t+φ ),weformulateanoptimizationproblem.
|     |     | ij  |     |     |     |     | i i |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Specifically,wesetupaminimizationproblemthatseekstominimizethesquareddifferencebetweenthesinefunctionand
14

RethinkingTimeEncodingviaLearnableTransformationFunctions
theweightedsumofB-splinebasisfunctionsovertheinterval[a,b]:
|     |          |    |     |     |     |     | 2  |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- |
|     | (cid:90) | b   |     | M   |     |     |     |     |
(cid:88)
| min                |     | sin(ω | t+φ )− | c   | B (ω | t+φ | ) dt. | (30) |
| ------------------ | --- | ------ | ------ | --- | ---- | --- | ------ | ---- |
|                    |     | i      | i      | i,j | j    | i   | i      |      |
| ci,1,ci,2,...,ci,M |     | a      |        |     |      |     |        |      |
j=1
This minimization problem is a standard least squares problem, where the objective is to find the coefficients c that
i,j
minimizetheintegralofthesquarederror. Solvingthisproblemcanbeaccomplishedusingnumericalmethodssuchasthe
normalequationsorsingularvaluedecomposition,leadingtotheoptimalcoefficientsfortheapproximation.
ByleveragingthepropertiesofB-splinebasisfunctionsandtheWeierstrassApproximationTheorem,wecanassertthat,for
anyϵ>0,thereexistsasufficientlylargeM andappropriatecoefficientsc i,j suchthat:
|     | (cid:12) |     |          |     |     | (cid:12) |     |     |
| --- | -------- | --- | -------- | --- | --- | -------- | --- | --- |
|     | (cid:12) |     | M        |     |     | (cid:12) |     |     |
|     | (cid:12) |     | (cid:88) |     |     | (cid:12) |     |     |
sup (cid:12)sin(ω i t+φ i )− c i,j B j (ω i t+φ i )(cid:12)<ϵ. (31)
|                 | (cid:12) |     |     |     |     | (cid:12) |     |     |
| --------------- | -------- | --- | --- | --- | --- | -------- | --- | --- |
| t∈[a,b](cid:12) |          |     |     |     |     | (cid:12) |     |     |
j=1
ThisinequalityindicatesthatthemaximumdeviationbetweenthesinefunctionanditsB-splineapproximationover[a,b]is
lessthanϵ,satisfyingtheconditionofuniformapproximation.
Sinceϵ>0isarbitrary,wecanmaketheapproximationasaccurateasdesiredbyincreasingM andchoosingappropriate
coefficientsc . Therefore,thesinefunctionsin(ω t+φ )canberepresentedasasumofB-splinebasisfunctions,making
| i,j |     | i   | i   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
itaspecialcaseofEquation(10)inthelimitasM →∞.
C.3.ProofofProposition3.2
AclassC ofmodelsisconsideredinvarianttotimerescalingif,foranymodelM ∈C andanyscalarα>0,thereexistsa
1
modelM ∈C thatrespondstoαt(wheretisscaledbyα)inthesamewaythatM respondstotheoriginaltvalues. We
2 1
providethefollowingprooftoshowthatLeTEisinvarianttotimerescaling.
Proof. ConsidertimeencodingM ,mappedbyLeTE:
1
|     |     | LeTE(t)[i]=ϕ | i (ω | i t+φ | i ). |     |     | (32) |
| --- | --- | ------------ | ---- | ----- | ---- | --- | --- | ---- |
Ifwereplacetwithα·t(whereα>0),thetimeencodingupdatesasfollows:
|     | LeTE(α·t)[i]=ϕ |     | i (ω i | (α·t)+φ | i ). |     |     | (33) |
| --- | -------------- | --- | ------ | ------- | ---- | --- | --- | ---- |
TopreservethebehavioroftheoriginalmodelM undertimerescaling,consideranewtimeencodingM withadjusted
1 2
′ ω
frequenciesω = i. Withthisfrequencyadjustment,M 2 behavesidenticallytoM 1 onα·t,demonstratingthatLeTEis
i α
invarianttotimerescaling.
D.ImplementationDetailsofLeTE
PreviousimplementationsofFTEscanbesummarizedasinputtingatimestamportimedifferencebetweeneventsintoa
single-layerMLPwithafixedtrigonometricfunctionasthenon-linearactivationfunction. Inspiredbythis,ourmethodcan
beviewedasmakingthefixedactivationfunctionlearnablebyparameterizingitwithaFourierseriesexpansionorB-spline
functions. FollowingKAN(Liuetal.,2025),whichmakesactivationfunctionsindeeplearningmodelstrainable,weusea
similarimplementationmethod.
D.1.Fourier-basedLeTE
TheimplementationofFourier-basedLeTEisstraightforwardandisgivenby:
D K
|        | (cid:88) (cid:88)(cid:0) |              |                |       |     |     |              |      |
| ------ | ------------------------ | ------------ | -------------- | ----- | --- | --- | ------------ | ---- |
| ϕ (x)= |                          | W(cos)cos(mx | )+W(sin)sin(mx |       |     | )   | (cid:1) +b , | (34) |
| j      |                          | j,i,m        | i              | j,i,m |     | i   | j            |      |
i=1m=1
wherei = 1,2,...,Dindexestheinputdimension,j = 1,2,...,M indexestheoutputdimension(withD = M inour
method),andm=1,2,...,K indexestheFourierfrequencies. Here,K isahyper-parameterthatdeterminesthegridsize.
TheparametersW(cos) ∈RM×D×K,W(sin) ∈RM×D×K,andb∈RM arelearnableweightsandbiases.
15

RethinkingTimeEncodingviaLearnableTransformationFunctions
D.2.Spline-basedLeTE
ByusingB-splinefunctions,wemaketheϕ functionsinEquation(6)learnableasfollows:
i
ϕ (x)=b (x)+spline (x), (35)
i i i
sinh(x) ex−e−x
b(x)=Tanh(x)= = , (36)
cosh(x) ex+e−x
(cid:88)
spline (x)= c B (x), (37)
i ij j
j
wherec arelearnable. UnliketheoriginalKAN,weuseTanhasthebasisfunctionhere,aswefounditperformsbetterin
ij
practice.
E.MoreDetailsforExperimentalSetting
E.1.Detailsfor“TimeastheOnlyInput”Experiments
Following(Kazemietal.,2019),Wegenerateasequentialevent-basedversionofMNISTbyflatteningtheimagesand
recordingthepositionsofpixelswithintensitiesgreaterthanathreshold(0.9inourexperiment). Afterthistransformation,
eachimageisrepresentedasanarrayofincreasingnumbers,suchas[t ,t ,t ,...,t ]. Thesevaluesaretreatedasevent
1 2 3 m
timesandcanbeusedforimageclassificationtask. Thebackbonemodelweusedisa128-dimensionalLSTM,withabatch
sizeof512,alignedwiththesettingsin(Kazemietal.,2019).
E.2.TimeSeriesBaselinesandDatasets
E.2.1.EXPERIMENTIMPLEMENTATIONDETAILS
Ourexperimentssettingontimeseriestasksalignswiththedefinitionoflong-termforecasting. Thebaselineresultsfor
TransformerandPyraformerarebasedonourimplementation,whiletheresultsfortheotherbaselinesaretakenfromtheir
originalpapers. Baselinemodelstypicallyuseahand-craftedtimeencodingmethodthatappliesdateandtimestampsto
representvarioustimefeatures—includingminutes,hours,weekdays,days,andmonths. Themappedvectorsarethenadded
togetherandaddedtothefeatureembeddingsandfedintothemodels. TheresultsareevaluatedusingMAE(MeanAbsolute
Error)(Table1)andMSE(MeanSquaredError)(Table5),bothofwhicharewidelyusedmetricsintimeseriesforecasting
research.
E.2.2.BASELINES
Weselect5commonlyusedtimeseriespredictionbaselines—Transformer(Vaswanietal.,2017),Pyraformer(Liuetal.,
2021),Non-stationaryTransformer(Liuetal.,2022),MICN(Wangetal.,2023),andTimesNet(Wuetal.,2023)—and
replacetheiroriginalhand-craftedtimeencodingswithourproposedLeTEtodemonstratethatLeTEcanbeeffectively
appliedtotimeseriespredictionmodelsandimprovetheperformanceofdownstreamtasks. Abriefintroductiontothese
baselinemodelsisprovidedbelow:
• Transformer (Vaswani et al., 2017) leverages the self-attention mechanism to model long-range dependencies in
sequences,makingitapowerfultoolfortimeseriesforecasting,especiallyincaseswithcomplextimepatterns. Its
globalcontextmodelingcapabilityenablesittocaptureintricaterelationshipsbetweentimestepseffectively.
• Pyraformer(Liuetal.,2021)introducesapyramidattentionmechanismthathierarchicallyreducesthecomputational
burdenwhilepreservingtheabilitytomodelbothlocalandglobaldependencies. Thisdesignmakesitparticularly
well-suitedforhandlinglongtimeserieswithimprovedefficiencyandscalability.
• Non-stationaryTransformer(Liuetal.,2022): addresseschallengesinforecastingnon-stationarytimeseriesby
incorporatingdynamicfeatureadjustmentsandcontext-awareattentionmechanisms. Thisallowsthemodeltoadaptto
evolvingdatadistributions,ensuringrobustandaccuratepredictionsindynamicenvironments.
• MICN (Wang et al., 2023) integrates multi-scale architectures to capture both short-term patterns and long-term
dependencies in time series data. By combining localconvolutionaloperations and global attention, it provides a
balancedapproachtohandlingdiversetemporalcharacteristics.
16

RethinkingTimeEncodingviaLearnableTransformationFunctions
• TimesNet(Wuetal.,2023)innovativelymodelstimeseriesdatainthefrequencydomain,leveragingdiscreteFourier
transformations to capture periodicity and trends. This approach enhances its ability to predict time series with
prominentseasonalandcyclicalbehaviorsefficiently.
E.2.3.DATASETS
Weutilize4real-worlddatasetstoevaluatetheeffectivenessofourmethodontimeseriespredictiontasks,encompassing
variousreal-worldscenarios. ThedatasetstatisticsarepresentedinTable3,withdetaileddescriptionsprovidedbelow.
Table3.TimeSeriesDatasetStatistics:Thedatasetsizeisorganizedin(Train,Validation,Test).Pleasereferto(Wuetal.,2023)forthe
originaltable.
Dataset Dim SeriesLength DatasetSize Information(Frequency)
ETTm1,ETTm2 7 {96,192,336,720} (34465,11521,11521) Electricity(15mins)
ETTh1,ETTh2 7 {96,192,336,720} (8545,2881,2881) Electricity(15mins)
Electricity 321 {96,192,336,720} (18317,2633,5261) Electricity(Hourly)
Exchange 8 {96,192,336,720} (5120,665,1422) Exchangerate(Daily)
Weather 21 {96,192,336,720} (36792,5271,10540) Weather(10mins)
• ETT2datasetincludestimeseriesdataforoiltemperatureandpowerloadmeasurementsfromelectricitytransformers,
collectedbetweenJuly2016andJuly2018. Specifically,thesubsetsETTm1andETTm2aresampledat15-minute
intervals,whileETTh1andETTh2arerecordedhourly.
• Electricity3 datasetprovideshourlyelectricityconsumptiondatafor321clients,spanningtheperiodfrom2012to
2014.
• Exchange(Laietal.,2018)datasetoffersdailypaneldataonexchangeratesfromeightcountries,coveringtheyears
1990to2016.
• Weather4datasetcontainsmeteorologicaltimeseriesdata,comprising21weatherindicatorsrecordedat10-minute
intervalsin2020bytheWeatherStationoftheMaxPlanckBiogeochemistryInstitute.
E.3.DynamicGraphBaselinesandDatasets
E.3.1.EXPERIMENTIMPLEMENTATIONDETAILS
Thehyper-parametersarebasedonthebestconfigurationsreportedinthepapers,andwekeepthemunchangedacross
differentexperimentsforeachbaselinemodeltoensureafaircomparison. WererunthebaselinemodelsTGATwithbatch
size100andreusethebaselineresultsreportedintheDyGFormerpaperforotherbaselines. Theresultsareevaluatedusing
AveragePrecision,i.e.,AP(Table2)andAreaUndertheReceiverOperatingCharacteristicCurve,i.e.,AUC-ROC(Table6),
bothofwhicharewidelyusedmetricsindynamicgraphrepresentationlearningresearch.
E.3.2.BASELINES
Weselect4commonlyusedcontinuousdynamicgraphrepresentationlearningbaselines—TGAT(Xuetal.,2020),TGN
(Rossietal.,2020),TCL(Wangetal.,2021),andDyGFormer(Yuetal.,2023)—andreplacetheFunctionalTimeEncoding
methods(Kazemietal.,2019;Xuetal.,2019)withLeTEtodemonstrateitsoptimalperformanceonthedynamicgraphlink
predictiontask. Abriefintroductiontothesebaselinemodelsisprovidedbelow:
• TGAT(Xuetal.,2020)introducesatemporalattentionmechanismtoaggregateinformationfromtemporal-topological
neighbors,therebygeneratingtemporalnoderepresentationsintemporalgraphs. Additionally,itproposesatrainable
2https://github.com/zhouhaoyi/ETDataset
3https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
4https://www.bgc-jena.mpg.de/wetter/
17

RethinkingTimeEncodingviaLearnableTransformationFunctions
timeencodingfunctiontocapturedistinguishabletemporalinformation,whichhasbeenwidelyadoptedinsubsequent
dynamicgraphnetworkarchitectures.
• TGN(Rossietal.,2020)integrateskeyideasfrompreviousmodelsandintroducesamemorymodulethatmaintainsa
statevectorforeachnode.Thememoryisupdateddynamicallywhenevernodesparticipateininteractions.Additionally,
TGNincorporatesamessage-passingmodule,amemoryupdatemodule,andatemporalembeddingmoduletogenerate
effectivetemporalrepresentationsfornodeswithintemporalgraphs.
• TCL(Wangetal.,2021)utilizesabreadth-firstsearchalgorithmtoconstructatemporaldependencyinteractionsub-
graph,extractinginteractionsequences. ItemploysaTransformerencoderthatintegratesbothtopologicalandtemporal
informationtolearnrepresentationsofcentralnodes. Additionally,TCLintroducesacross-attentionmechanismwithin
theTransformertomodeltheinter-dependenciesbetweeninteractingnodepairs.
• DyGFormer(Yuetal.,2023)leverages1-hopneighborinformationforlearningtemporalgraphrepresentations. It
employsaTransformerencoderenhancedwithapatchingtechniquetoeffectivelycapturelong-termdependencies
amongnodesintemporalgraphs. Furthermore,DyGFormerincorporatesaNeighborCo-occurrenceFeaturetopreserve
thecorrelationinformationbetweensourceandtargetnodes.
E.3.3.DATASETS
We utilize 4 real-world datasets (Kumar et al., 2019) to evaluate the effectiveness of our method on dynamic graph
representationlearningtasks,encompassingvariousreal-worldscenarios. ThedatasetstatisticsarepresentedinTable4,
withdetaileddescriptionsprovidedbelow.
Table4.DynamicGraphDatasetStatistics:DimnandDimerepresentthedimensionsofnodefeaturesandedgefeatures,respectively.For
non-attributedgraphs,wefollowpreviousstudies(Xuetal.,2020;Rossietal.,2020)anduse172-dimensionalzerovectorsaspadding.
Dataset Dim Dim #Nodes #Edges Information Duration TimeGranularity
n e
Wikipedia - 172 9,227 157,474 Social 1month Unixtimestamps
Reddit - 172 10,984 672,447 Social 1month Unixtimestamps
MOOC - 4 7,144 411,749 Interaction 17months Unixtimestamps
LastFM - - 1,980 1,293,103 Interaction 1month Unixtimestamps
• WikipediarecordseditingactivitiesonWikipediapagesoveraone-monthtimeframe. Nodesinthisgraphrepresent
usersorpages,andtemporallinkswithtimestampscapturetheedits. Eachlinkisassociatedwitha172-dimensional
featurevectorbasedonLIWC(LinguisticInquiryandWordCount)(Pennebaker,2001).
• Redditcapturesuseractivityacrosssubredditsoveraone-monthperiod. Inthisdataset, nodesrepresentusersor
subreddits,whiletimestampedlinksdenotepostingactions. Eachlinkisfurthercharacterizedbya172-dimensional
featurevectorderivedfromLIWC.
• MOOCcapturestheinteractionsofusersonawidelyusedMOOCplatform,structuredasadirected,temporalnetwork.
Inthisrepresentation,nodescorrespondtousersandcourseactivities(referredtoastargets),whileedgesdenotethe
actionsperformedbyusersonthesetargets
• LastFMrecordsinteractiondatawhereuserslistentosongsoveramonth. InLastFM,nodescorrespondtousersand
songs,andthelinksrepresentlisteningactivitiesperformedbyusers.
E.4.Real-WorldApplicationDataset
Thedatasetusedforreal-worldapplicationexperimentsisafinancialriskcontroldataset,containingrecordsof483,379
users’transactionbehavioratvariousmerchantsovera60-dayperiod. Itincludesatotalof26,850,000transactions. Each
userisrepresentedbya585-dimensionalfeature,eachmerchantbya128-dimensionalfeature,andeachtransactionbya
202-dimensionalfeature,withalltransactionslabeledwithUNIXtimestamps. Theratioofpositiveusers(withdefaultrisk)
tonegativeusers(withoutdefaultrisk)is1:9.92inthetrainingdatasetand1:20.25inthetestdataset. Thebackbonemodel
18

RethinkingTimeEncodingviaLearnableTransformationFunctions
employsaspeciallydesignedTransformer-basedarchitecturetoaggregateusers’historicaltransactionfeatures,merchant
features,userfeatures,andanoptionaltimeembeddingintouserembeddings,whicharethenusedtopredictwhetherthe
userhasdefaultrisk.
F.AdditionalExperimentalResults
Here,weprovidethecompleteresultsoftheexperimentsdiscussedinthemaintext.
F.1.Resultsofmultivariatetimeserieslong-termforecastingtaskevaluatedusingMSE
Theresultsofthemultivariatetimeserieslong-termforecastingtask,evaluatedusingMSE,arepresentedinTable5. These
resultsareorganizedinthesamemannerasthoseinTable1.
Table5.Timeseriesprediction:multivariatelong-termforecastingtask.Thepastsequencelengthissetto96,whilethepredictionlengths
are{96,192,336,720}.TheresultsarereportedintermsofMSE,wherelowervaluesindicatebetterperformance.HCTE(Hand-Crafted
TimeEncoding)isamethodwidelyadoptedintimeseriesresearch.FTEstandsforFunctionalTimeEncoding.Thewinraterepresents
thepercentageofcaseswhereLeTEoutperformstheHCTE.Thebestresultsforeachbaseline,datasetandpredictionlengthcombinations
areinbold.ETTconsistsof4subsets.Here,wepresenttheaverageresultsacrossthesesubsets,withthefullresultsprovidedinTable8.
MSE Transformer Pyraformer NSTrans. MICN TimesNet Win
TE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE Rate
96 1.219 1.204 0.568 0.794 0.960 0.650 0.392 0.486 0.347 0.392 0.310 0.296 0.312 0.322 0.305
192 2.601 1.643 0.959 1.667 1.812 1.058 0.446 0.548 0.410 0.446 0.396 0.357 0.365 0.390 0.368
336 2.438 1.557 1.192 1.981 1.962 1.297 0.492 0.651 0.467 0.492 0.487 0.430 0.419 0.422 0.404
TTE 95%
720 1.998 2.217 1.313 2.589 2.442 1.612 0.552 0.660 0.531 0.552 0.630 0.517 0.467 0.468 0.441
96 0.258 0.280 0.252 0.285 0.281 0.267 0.169 0.171 0.163 0.164 0.156 0.150 0.168 0.168 0.164
192 0.266 0.310 0.259 0.298 0.288 0.274 0.182 0.192 0.178 0.177 0.170 0.166 0.184 0.179 0.179
336 0.275 0.339 0.265 0.307 0.306 0.274 0.200 0.201 0.190 0.193 0.189 0.184 0.198 0.210 0.193
yticirtcelE
95%
720 0.288 0.395 0.276 0.304 0.304 0.293 0.222 0.237 0.226 0.212 0.228 0.208 0.220 0.287 0.220
96 0.545 0.788 0.464 0.505 0.616 0.584 0.111 0.137 0.102 0.102 0.098 0.080 0.107 0.108 0.103
192 0.950 1.028 0.903 1.015 0.983 0.904 0.219 0.273 0.193 0.172 0.186 0.152 0.226 0.217 0.211
336 1.462 1.866 1.114 1.263 1.420 1.056 0.421 0.463 0.342 0.272 0.356 0.265 0.367 0.413 0.367
egnahcxE
95%
720 2.569 2.002 1.736 1.762 1.714 1.316 1.092 1.546 0.682 0.714 0.833 0.636 0.964 0.989 0.958
96 0.393 0.184 0.172 0.225 0.207 0.181 0.173 0.172 0.168 0.161 0.198 0.166 0.172 0.172 0.166
192 0.547 0.249 0.220 0.252 0.238 0.230 0.245 0.224 0.215 0.220 0.243 0.209 0.219 0.221 0.212
336 0.678 0.328 0.309 0.362 0.324 0.284 0.321 0.295 0.277 0.278 0.285 0.251 0.280 0.278 0.274
rehtaeW
95%
720 0.844 0.480 0.425 0.411 0.394 0.383 0.414 0.350 0.338 0.311 0.350 0.303 0.365 0.354 0.352
WinRate 100% 94% 94% 94% 94% 95%
F.2.ResultsofdynamicgraphlinkpredictiontaskevaluatedusingAUC-ROC
Theresultsofthedynamicgraphlinkpredictiontask,evaluatedusingAUC-ROC,arepresentedinTable6.
Table6.Dynamicgraphlinkpredictiontask:TheresultsarereportedinAUC-ROC,wherehighervaluesindicatebetterperformance.The
betterresultsareinbold.Here,wepresentthetop-performingresultsacrossvariationsofLeTE,withthefullresultsprovidedinTable10.
FTErepresentsFunctionalTimeEncodingwhichiscommonlyusedindynamicgraphresearch.
AUC Wikipedia Reddit MOOC LastFM
TE Transductive Inductive Transductive Inductive Transductive Inductive Transductive Inductive
FTE 96.69±0.26 95.95±0.33 98.48±0.04 96.90±0.07 86.44±0.24 86.04±0.19 70.89±0.10 76.11±0.11
TGAT
LeTE 97.63±0.11 97.07±0.10 98.51±0.01 96.96±0.05 89.46±0.08 89.50±0.05 74.24±0.28 79.63±0.14
FTE 98.37±0.07 97.72±0.03 98.60±0.06 97.39±0.07 91.21±1.15 91.24±0.99 78.47±2.94 82.61±3.15
TGN
LeTE 98.73±0.07 98.11±0.10 98.72±0.00 97.55±0.05 92.68±0.37 92.41±0.73 83.94±1.85 87.74±1.75
FTE 95.84±0.18 95.57±0.20 97.42±0.02 93.80±0.07 83.12±0.18 81.43±0.19 64.06±1.16 70.84±0.85
TCL
LeTE 97.84±0.06 97.56±0.02 97.68±0.03 94.63±0.05 84.73±0.13 83.25±0.23 70.17±0.47 75.86±0.44
DyG- FTE 98.91±0.02 98.48±0.03 99.15±0.01 98.71±0.01 87.91±0.58 87.62±0.51 93.05±0.10 94.08±0.08
Former LeTE 99.04±0.01 98.67±0.02 99.17±0.00 98.74±0.01 89.18±0.21 89.16±0.30 93.65±0.07 94.52±0.08
19

RethinkingTimeEncodingviaLearnableTransformationFunctions
F.3.Fullresultsofthemultivariatelong-termforecastingtaskon4ETTsubsets
Wepresentthefullresultsofthemultivariatelong-termforecastingtaskonthe4ETTsubsetsinTables7and8,asTables1
and5reporttheaverageresults.
Table7.Timeseriesprediction:multivariatelong-termforecastingtaskon4subsetsofETT.Thepastsequencelengthissetto96,while
thepredictionlengthsare{96,192,336,720}.TheresultsarereportedintermsofMAE.Thebestresultsforeachbaseline,datasetand
predictionlengthcombinationsareinbold.
MAE Transformer Pyraformer NSTrans. MINC TimesNet
TE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE
1mTTE
96 0.621 0.601 0.507 0.581 0.522 0.521 0.398 0.409 0.389 0.398 0.376 0.372 0.375 0.389 0.378
192 0.703 0.550 0.526 0.577 0.547 0.531 0.444 0.427 0.417 0.444 0.393 0.399 0.387 0.418 0.404
336 0.795 0.755 0.596 0.675 0.637 0.610 0.464 0.496 0.439 0.464 0.425 0.426 0.411 0.418 0.418
720 0.798 0.782 0.663 0.760 0.700 0.645 0.516 0.498 0.470 0.516 0.467 0.465 0.450 0.456 0.454
2mTTE
96 0.506 0.451 0.420 0.458 0.756 0.411 0.274 0.304 0.278 0.274 0.287 0.271 0.267 0.268 0.262
192 0.908 0.700 0.558 0.649 0.611 0.625 0.339 0.379 0.325 0.339 0.349 0.321 0.309 0.306 0.302
336 0.796 0.806 0.753 0.811 0.902 0.775 0.361 0.400 0.353 0.361 0.439 0.364 0.351 0.351 0.342
720 1.192 1.301 0.851 1.416 1.491 1.137 0.413 0.446 0.420 0.413 0.506 0.432 0.403 0.409 0.399
1hTTE
96 0.739 0.814 0.524 0.637 0.613 0.593 0.491 0.616 0.452 0.491 0.413 0.409 0.402 0.425 0.408
192 0.762 0.815 0.632 0.738 0.778 0.647 0.504 0.631 0.483 0.504 0.465 0.452 0.429 0.457 0.439
336 0.772 0.786 0.679 0.794 0.758 0.736 0.535 0.730 0.541 0.535 0.511 0.502 0.469 0.469 0.453
720 0.800 0.878 0.724 0.776 0.804 0.782 0.616 0.792 0.610 0.616 0.598 0.565 0.500 0.490 0.421
2hTTE
96 1.323 1.349 0.752 0.892 0.989 0.806 0.458 0.413 0.390 0.458 0.392 0.349 0.374 0.367 0.359
192 2.184 1.599 1.133 1.632 1.760 1.150 0.493 0.475 0.434 0.493 0.485 0.408 0.414 0.418 0.406
336 2.113 1.405 1.256 1.893 1.856 1.330 0.551 0.528 0.463 0.551 0.569 0.500 0.452 0.458 0.438
720 1.488 1.623 1.276 1.832 1.761 1.274 0.560 0.492 0.460 0.560 0.673 0.558 0.468 0.466 0.443
Table8.Timeseriesprediction:multivariatelong-termforecastingtaskon4subsetsofETT.Thepastsequencelengthissetto96,while
thepredictionlengthsare{96,192,336,720}.TheresultsarereportedintermsofMSE.Thebestresultsforeachbaseline,datasetand
predictionlengthcombinationsareinbold.
MSE Transformer Pyraformer NSTrans. MINC TimesNet
TE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE HCTE FTE LeTE
1mTTE
96 0.713 0.667 0.511 0.708 0.581 0.584 0.386 0.430 0.370 0.386 0.329 0.325 0.338 0.365 0.339
192 0.866 0.592 0.573 0.693 0.621 0.560 0.459 0.464 0.418 0.459 0.364 0.373 0.374 0.430 0.392
336 1.063 1.035 0.692 0.848 0.754 0.689 0.495 0.651 0.451 0.495 0.403 0.396 0.410 0.412 0.412
720 1.075 1.062 0.788 1.009 0.855 0.777 0.585 0.584 0.510 0.585 0.469 0.463 0.478 0.482 0.477
2mTTE
96 0.486 0.354 0.327 0.384 1.047 0.310 0.192 0.246 0.195 0.192 0.190 0.187 0.187 0.191 0.182
192 1.499 0.834 0.522 0.730 0.653 0.672 0.280 0.378 0.266 0.280 0.271 0.241 0.249 0.253 0.248
336 1.107 1.113 0.949 1.144 1.377 1.023 0.334 0.387 0.315 0.334 0.398 0.307 0.321 0.327 0.310
720 2.609 2.931 1.104 3.624 3.708 2.195 0.417 0.491 0.431 0.417 0.525 0.414 0.408 0.427 0.408
1hTTE
96 0.876 1.032 0.535 0.727 0.664 0.632 0.513 0.841 0.470 0.513 0.381 0.379 0.384 0.412 0.387
192 0.919 1.083 0.710 0.903 0.949 0.734 0.534 0.786 0.522 0.534 0.452 0.434 0.436 0.461 0.433
336 0.960 1.003 0.805 1.011 0.931 0.887 0.588 0.941 0.638 0.588 0.520 0.501 0.491 0.483 0.470
720 1.030 1.183 0.856 0.992 1.012 0.961 0.643 1.052 0.735 0.643 0.646 0.578 0.521 0.509 0.455
2hTTE
96 2.802 2.762 0.897 1.357 1.548 1.074 0.476 0.427 0.355 0.476 0.339 0.294 0.340 0.319 0.313
192 7.123 4.066 2.030 4.342 5.025 2.268 0.512 0.563 0.436 0.512 0.495 0.380 0.402 0.416 0.398
336 6.621 3.078 2.322 4.922 4.786 2.589 0.552 0.625 0.466 0.552 0.625 0.516 0.452 0.464 0.422
720 3.279 3.695 2.502 4.733 4.191 2.516 0.562 0.513 0.448 0.562 0.880 0.615 0.462 0.456 0.426
F.4.DimensionsofTimeEmbedding
WepresenttheAUC-ROCresultsforWikipedia/TGNandMOOC/TGNwithdifferenttimeembeddingdimensions(for
bothFTEandLeTE)inFigure6. Tocoverabroaderrangeofscenarios,wealsoincludetheresultsforDyGFormeronthe
WikipediadatasetinFigure7.
G.MoreExperiments
G.1.StatisticAnalysisoftheComplexTimePatternsinData
Time-relateddataoftencontainsmixedandcomplexpatterns, whichcanprimarilybecategorizedasperiodicandnon-
periodic. To investigate the periodic and non-periodic patterns in the data, we analyze four dynamic graph datasets
20

RethinkingTimeEncodingviaLearnableTransformationFunctions
|     | 99.00            |       |                        | 94.00       |       |                        |     |
| --- | ---------------- | ----- | ---------------------- | ----------- | ----- | ---------------------- | --- |
|     | 98.30            |       |                        | 92.50       |       |                        |     |
|     | 97.60            |       |                        | 91.00       |       |                        |     |
|     | 96.90            |       |                        | 89.50       |       |                        |     |
|     |                  |       | LLeeTTEE  TTrraannss.. |             |       | LLeeTTEE  TTrraannss.. |     |
|     | 96.20            |       | FFTTEE  TTrraannss..   | 88.00       |       | FFTTEE  TTrraannss..   |     |
|     |                  |       | LLeeTTEE  IInndduucc.. |             |       | LLeeTTEE  IInndduucc.. |     |
|     |                  |       | FFTTEE  IInndduucc..   |             |       | FFTTEE  IInndduucc..   |     |
|     | 95.50            |       |                        | 86.50       |       |                        |     |
|     | 2 8 16           | 32 64 | 100                    | 2 8 16      | 32 64 | 100                    |     |
|     | (a)Wikipedia/TGN |       |                        | (b)MOOC/TGN |       |                        |     |
Figure6.AUC-ROCresultscomparingdifferentdimensionsoftheFTEandSpline-basedLeTEonWikipedia/TGNandMOOC/TGN.
|     | 99.30  |       |                        | 99.20      |       |                        |     |
| --- | ------ | ----- | ---------------------- | ---------- | ----- | ---------------------- | --- |
|     | 99.04  |       |                        | 98.96      |       |                        |     |
|     | 98.78  |       |                        | 98.72      |       |                        |     |
|     | 98.52  |       |                        | 98.48      |       |                        |     |
|     |        |       | LLeeTTEE  TTrraannss.. |            |       | LLeeTTEE  TTrraannss.. |     |
|     |        |       | FFTTEE  TTrraannss..   |            |       | FFTTEE  TTrraannss..   |     |
|     | 98.26  |       |                        | 98.24      |       |                        |     |
|     |        |       | LLeeTTEE  IInndduucc.. |            |       | LLeeTTEE  IInndduucc.. |     |
|     |        |       | FFTTEE  IInndduucc..   |            |       | FFTTEE  IInndduucc..   |     |
|     | 98.00  |       |                        | 98.00      |       |                        |     |
|     | 2 8 16 | 32 64 | 100                    | 2 8 16     | 32 64 | 100                    |     |
|     |        | (a)AP |                        | (b)AUC-ROC |       |                        |     |
Figure7.APandAUC-ROCresultscomparingdifferentdimensionsoftheFTEandSpline-basedLeTEonWikipedia/DyGFormer.
usingspectralentropy(Shannon,1948). First,wenormalizethetimeortimedifferences(sincepreviousdynamicgraph
representationlearningmethodstypicallyusetimedifferencesasinputstothetimeencoding,weincludethisanalysishere
aswell)foreachnodewithmorethanfiveinteractions,mappingthevaluestotherange[0,1]. Wethentreateachnode’s
interactiontimesasasignalsequence. Thespectralentropyforeachnodeiscomputedasfollows: Webeginbyapplying
theFastFourierTransform(FFT)tothenormalizedsignalsequences: X(f)=FFT(t norm ),whereX(f)isthefrequency-
domain representation of the signal. Next, we calculate the magnitude of the frequency components M(f) = |X(f)|.
M(f)
Themagnitudesarethennormalizedtoformaprobabilitydistribution: P(f) = (cid:80) . Finally,thespectralentropy
M(f)
|     | (cid:80) |     |     |     | f   |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- |
iscomputedas: H(P) = − P(f)logP(f),whichmeasurestheuniformityofthefrequencycomponents. Alower
f
entropyvalueindicatesperiodicity,whileahigherentropyvaluesuggestsrandomness.
WepresentthedensityplotsofthespectralentropyinFigure8. Asshowninthefigures,onlyasmallportionofthenodes
exhibitstrongperiodicityintheirinteractiontimesortimedifferences,whilemostnodesshowhighentropy,indicating
non-periodicbehavior. Thissuggeststhatcapturingperiodicpatternsaloneisinsufficient;itisalsoimportanttomodel
non-periodicpatternstoenhancetheefficiencyandexpressivenessofthetimeencoding.
Density Plot of Spectral Entropy (Timestamp of Interactions) Density Plot of Spectral Entropy (Time Difference between Interactions)
| 1.2         |                  |                                                       | Wikipedia | 1.2         |                  |        | Wikipedia |
| ----------- | ---------------- | ----------------------------------------------------- | --------- | ----------- | ---------------- | ------ | --------- |
|             |                  |                                                       | Reddit    |             |                  |        | Reddit    |
| 1.0         |                  |                                                       | Mooc      | 1.0         |                  |        | Mooc      |
| ytisneD 0.8 |                  |                                                       | Lastfm    | ytisneD 0.8 |                  |        | Lastfm    |
| 0.6         |                  |                                                       |           | 0.6         |                  |        |           |
| 0.4         |                  |                                                       |           | 0.4         |                  |        |           |
| 0.2         |                  |                                                       |           | 0.2         |                  |        |           |
| 0.0         |                  |                                                       |           | 0.0         |                  |        |           |
| 0           | 2 4 6            | 8                                                     | 10 12     | 0 2         | 4                | 6 8 10 | 12        |
|             | Spectral Entropy |                                                       |           |             | Spectral Entropy |        |           |
|             | Figure8.         | Densityplotsofspectralentropyfordynamicgraphdatasets. |           |             |                  |        |           |
21

RethinkingTimeEncodingviaLearnableTransformationFunctions
G.2.ComparativeAnalysisofDifferentVariantsofLeTE
Weconductedasetofadditionalexperimentsondynamicgraphlinkpredictiontasks,applyingdifferentvariantsofLeTEand
comparingtheirdownstreamtaskperformance,evaluatedbyAPandAUC-ROC.Theresults,presentedinTables9and10,
indicatethat,inmostcases,CombinedLeTEachievesthebestperformanceamongthethreevariantsofLeTE.Thisoutcome
isintuitive,asCombinedLeTEleveragesthestrengthsofbothFourier-basedLeTEandSpline-basedLeTE,enablingitto
effectivelymodeldiversetimepatterns.
Duetodifferencesintheperiodicityandnon-periodicityofnodeinteractionsacrossdatasets,theeffectivenessofFourier-
basedLeTEandSpline-basedLeTEvaries. Nonetheless,inmostcases,bothmethodsoutperformthebenchmark. This
demonstratesthatevenwhenusingonlyFourier-basedLeTEorSpline-basedLeTE,theycaneffectivelymodeldifferent
patterns,includingperiodic,non-periodicandmixedpatterns,inthedata.
Table9.ComparingFunctionalTimeEncoding(FTE),Fourier-basedLeTE(F-LeTE),Spline-basedLeTE(S-LeTE)andCombined
LeTE(C-LeTE):DynamicgraphlinkpredictionresultsinAP.Thebestresultsareinbold.
AP Wikipedia Reddit MOOC LastFM
TE Transductive Inductive Transductive Inductive Transductive Inductive Transductive Inductive
FTE 96.95±0.24 96.33±0.26 98.53±0.04 97.01±0.05 85.34±0.19 84.94±0.04 72.73±0.11 77.78±0.13
F-LeTE 96.82±0.16 96.31±0.13 98.54±0.03 97.03±0.02 85.25±0.29 85.08±0.29 72.31±0.30 77.19±0.38
TGAT
S-LeTE 97.54±0.06 97.06±0.05 98.56±0.01 97.05±0.06 88.31±0.10 88.13±0.28 75.68±0.55 80.61±0.42
C-LeTE 97.82±0.09 97.34±0.08 98.56±0.01 96.99±0.06 88.30±0.05 88.37±0.12 76.22±0.25 81.32±0.14
FTE 98.45±0.06 97.83±0.04 98.63±0.06 97.50±0.07 89.15±1.60 89.04±1.17 77.07±3.97 81.45±4.29
F-LeTE 98.57±0.09 97.94±0.08 98.66±0.01 97.39±0.07 90.04±0.67 89.94±0.49 77.58±5.22 82.82±6.53
TGN
S-LeTE 98.55±0.06 97.98±0.08 98.74±0.00 97.65±0.04 91.09±0.20 90.87±0.83 82.26±2.27 86.46±0.77
C-LeTE 98.78±0.07 98.19±0.09 98.74±0.01 97.52±0.12 91.41±0.55 90.17±0.69 83.64±2.00 87.55±1.88
FTE 96.47±0.16 96.22±0.17 97.53±0.02 94.09±0.07 82.38±0.24 80.60±0.22 67.27±2.16 73.53±1.66
F-LeTE 97.83±0.05 97.58±0.10 97.74±0.03 94.75±0.20 83.40±1.32 81.75±1.43 76.08±0.79 80.68±0.70
TCL
S-LeTE 97.33±0.06 97.05±0.13 97.78±0.03 94.99±0.07 83.87±0.30 82.34±0.31 69.92±0.46 76.44±0.42
C-LeTE 98.19±0.04 97.89±0.03 97.75±0.09 94.83±0.20 84.24±0.10 82.72±0.12 72.76±4.64 78.70±3.67
FTE 99.03±0.02 98.59±0.03 99.22±0.01 98.84±0.02 87.52±0.49 86.96±0.43 93.00±0.12 94.23±0.09
DyG- F-LeTE 99.04±0.01 98.66±0.05 99.22±0.01 98.85±0.02 87.60±0.26 87.15±0.22 93.06±0.05 94.11±0.09
Former S-LeTE 99.12±0.01 98.72±0.03 99.17±0.10 98.78±0.13 88.66±0.20 88.37±0.25 93.50±0.12 94.57±0.15
C-LeTE 99.13±0.02 98.73±0.00 99.24±0.01 98.86±0.01 88.70±0.21 88.39±0.15 93.64±0.10 94.69±0.12
Table10.ComparingFunctionalTimeEncoding(FTE),Fourier-basedLeTE(F-LeTE),Spline-basedLeTE(S-LeTE)andCombined
LeTE(C-LeTE):DynamicgraphlinkpredictionresultsinAUC-ROC.Thebestresultsareinbold.
AUC Wikipedia Reddit MOOC LastFM
TE Transductive Inductive Transductive Inductive Transductive Inductive Transductive Inductive
FTE 96.69±0.26 95.95±0.33 98.48±0.04 96.90±0.07 86.44±0.24 86.04±0.19 70.89±0.10 76.11±0.11
F-LeTE 96.53±0.17 95.94±0.20 98.48±0.03 96.91±0.03 86.36±0.29 86.18±0.33 70.53±0.18 75.61±0.22
TGAT
S-LeTE 97.33±0.07 96.76±0.06 98.51±0.02 96.96±0.05 89.38±0.14 89.14±0.24 73.89±0.51 79.17±0.44
C-LeTE 97.63±0.11 97.07±0.10 98.51±0.01 96.88±0.05 89.46±0.08 89.50±0.05 74.24±0.28 79.63±0.14
FTE 98.37±0.07 97.72±0.03 98.60±0.06 97.39±0.07 91.21±1.15 91.24±0.99 78.47±2.94 82.61±3.15
F-LeTE 98.50±0.10 97.86±0.09 98.63±0.02 97.27±0.10 91.71±0.65 91.53±0.33 78.24±4.86 83.16±6.28
TGN
S-LeTE 98.47±0.06 97.86±0.06 98.72±0.00 97.55±0.05 92.68±0.37 92.41±0.73 82.48±2.17 86.49±0.62
C-LeTE 98.73±0.07 98.11±0.10 98.72±0.02 97.43±0.11 92.65±0.48 91.27±0.85 83.94±1.85 87.74±1.75
FTE 95.84±0.18 95.57±0.20 97.42±0.02 93.80±0.07 83.12±0.18 81.43±0.19 64.06±1.16 70.84±0.85
F-LeTE 97.35±0.07 97.14±0.13 97.62±0.03 94.42±0.22 83.73±0.92 82.11±0.98 70.17±0.47 75.86±0.44
TCL
S-LeTE 96.90±0.08 96.62±0.15 97.68±0.03 94.63±0.05 84.50±0.20 83.02±0.23 67.32±0.50 74.37±0.51
C-LeTE 97.84±0.06 97.56±0.02 97.64±0.08 94.49±0.17 84.73±0.13 83.25±0.23 69.16±3.21 75.85±2.64
FTE 98.91±0.02 98.48±0.03 99.15±0.01 98.71±0.01 87.91±0.58 87.62±0.51 93.05±0.10 94.08±0.08
DyG- F-LeTE 98.94±0.02 98.55±0.03 99.16±0.01 98.72±0.03 88.09±0.16 87.89±0.14 93.09±0.03 94.00±0.04
Former S-LeTE 99.04±0.01 98.67±0.02 99.08±0.13 98.61±0.19 89.18±0.21 89.16±0.30 93.56±0.06 94.46±0.06
C-LeTE 99.04±0.02 98.65±0.01 99.17±0.00 98.74±0.01 89.17±0.20 89.14±0.09 93.65±0.07 94.52±0.08
G.3.VisualizationandInterpretability
AsmentionedinSection3.2,thelearnedparametersofourproposedmethodcanbeusedtoreconstructthetimeembedding
feature map or the non-linear transformations. Since the previous time encoding method (FTE) uses fixed non-linear
transformationfunctions,wepresentanexampleofitsfeaturemapandcompareitwiththeFourier-basedLeTEinFigure9.
22

RethinkingTimeEncodingviaLearnableTransformationFunctions
Larger input range
(a) Functional Time Encoding (FTE)
Larger input range
(b) Fourier-Based LeTE (Ours)
Figure9.ExampleoffeaturemapfortheFTEandFourier-basedLeTEatdifferentdimensions(thetotaldimensionis8,theparameters
weightarebasedonalearnedTGNmodelonWikipediadataset).
Dim 0
0.75
Dim 4
N 0.50
on-Linear
Transform
0
0
.
.
2
0
5
0
Dim 7
Dim 6
Dim 1
ed
Value
-0.25
Dim 3Dim 2
-0.50
Dim 5
-0.75 0
1
-4
L
-
i
2
near Transfor 0
med Value 2
4 7
6 T
5 ime Em
4 bedd
3
ing
D
2 imension
Figure10. Exampleofnon-lineartransformationforSpline-basedLeTEatdifferentdimensions.
23

RethinkingTimeEncodingviaLearnableTransformationFunctions
(cid:17)(cid:16)(cid:26)(cid:25)(cid:18)(cid:19)(cid:23)(cid:20)(cid:13) (cid:10) (cid:15)(cid:17)(cid:24)(cid:18)(cid:22)(cid:16)(cid:12)(cid:9) (cid:17)(cid:16)(cid:26)(cid:25)(cid:18)(cid:19)(cid:23)(cid:20)(cid:13) (cid:10) (cid:15)(cid:17)(cid:24)(cid:18)(cid:22)(cid:16)(cid:12)(cid:11) (cid:21)(cid:20)(cid:31)(cid:30)(cid:23)(cid:24)(cid:28)(cid:25)(cid:14) (cid:11) (cid:15)(cid:18)(cid:28)(cid:28)(cid:21)(cid:26)(cid:23)(cid:26)(cid:22)(cid:3)(cid:17)(cid:29)(cid:27)(cid:19)(cid:13)(cid:6)(cid:4)(cid:10) (cid:21)(cid:20)(cid:31)(cid:30)(cid:23)(cid:24)(cid:28)(cid:25)(cid:14) (cid:11) (cid:15)(cid:18)(cid:28)(cid:28)(cid:21)(cid:26)(cid:23)(cid:26)(cid:22)(cid:3)(cid:17)(cid:29)(cid:27)(cid:19)(cid:13)(cid:6)(cid:4)(cid:6)(cid:5) (cid:29)(cid:28)(cid:39)(cid:38)(cid:31) (cid:36)(cid:33)(cid:17) (cid:14) (cid:20)(cid:25)(cid:36)(cid:36)(cid:29)(cid:34)(cid:31)(cid:34)(cid:30)(cid:3)(cid:23)(cid:37)(cid:35)(cid:26)(cid:16)(cid:10)(cid:8)(cid:13) (cid:29)(cid:28)(cid:39)(cid:38)(cid:31) (cid:36)(cid:33)(cid:17) (cid:14) (cid:20)(cid:25)(cid:36)(cid:36)(cid:29)(cid:34)(cid:31)(cid:34)(cid:30)(cid:3)(cid:23)(cid:37)(cid:35)(cid:26)(cid:16)(cid:10)(cid:8)(cid:10)(cid:9) (cid:29)(cid:28)(cid:39)(cid:38)(cid:31) (cid:36)(cid:33)(cid:17) (cid:14) (cid:23)(cid:29)(cid:37)(cid:31)(cid:35)(cid:28)(cid:16)(cid:15)
| (cid:8) | (cid:8) | (cid:9) | (cid:9) | (cid:12) | (cid:12) | (cid:12) |
| ------- | ------- | ------- | ------- | -------- | -------- | -------- |
(cid:6) (cid:4) (cid:6) (cid:4) (cid:7) (cid:5) (cid:7) (cid:5) (cid:11) (cid:9)(cid:9) (cid:11) (cid:9)(cid:9) (cid:11) (cid:9)(cid:9)
(cid:4) (cid:6)(cid:9) (cid:9)(cid:4) (cid:11)(cid:9) (cid:14)(cid:21)(cid:5)(cid:16)(cid:4)(cid:17)(cid:4)(cid:27) (cid:5)(cid:6)(cid:9) (cid:5)(cid:9)(cid:4) (cid:5)(cid:11)(cid:9) (cid:6)(cid:4)(cid:4) (cid:4) (cid:6)(cid:9) (cid:9)(cid:4) (cid:11)(cid:9) (cid:14)(cid:21)(cid:5)(cid:16)(cid:4)(cid:17)(cid:4)(cid:27) (cid:5)(cid:6)(cid:9) (cid:5)(cid:9)(cid:4) (cid:5)(cid:11)(cid:9) (cid:6)(cid:4)(cid:4) (cid:5) (cid:7)(cid:10) (cid:10)(cid:5) (cid:12)(cid:10) (cid:16)(cid:26)(cid:6)(cid:20)(cid:5)(cid:21)(cid:5)  (cid:6)(cid:7)(cid:10) (cid:6)(cid:10)(cid:5) (cid:6)(cid:12)(cid:10) (cid:7)(cid:5)(cid:5) (cid:5) (cid:7)(cid:10) (cid:10)(cid:5) (cid:12)(cid:10) (cid:16)(cid:26)(cid:6)(cid:20)(cid:5)(cid:21)(cid:5)  (cid:6)(cid:7)(cid:10) (cid:6)(cid:10)(cid:5) (cid:6)(cid:12)(cid:10) (cid:7)(cid:5)(cid:5) (cid:11)(cid:13) (cid:13)(cid:9) (cid:15)(cid:13)(cid:21)(cid:34)(cid:10)(cid:28)(cid:9)(cid:29)(cid:9)((cid:10)(cid:11)(cid:13) (cid:10)(cid:13)(cid:9) (cid:10)(cid:15)(cid:13) (cid:11)(cid:9)(cid:9) (cid:11)(cid:13) (cid:13)(cid:9) (cid:15)(cid:13)(cid:21)(cid:34)(cid:10)(cid:28)(cid:9)(cid:29)(cid:9)((cid:10)(cid:11)(cid:13) (cid:10)(cid:13)(cid:9) (cid:10)(cid:15)(cid:13) (cid:11)(cid:9)(cid:9) (cid:11)(cid:13) (cid:13)(cid:9) (cid:15)(cid:13)(cid:21)(cid:34)(cid:10)(cid:28)(cid:9)(cid:29)(cid:9)((cid:10)(cid:11)(cid:13) (cid:10)(cid:13)(cid:9) (cid:10)(cid:15)(cid:13) (cid:11)(cid:9)(cid:9)
(cid:17)(cid:16)(cid:26)(cid:25)(cid:18)(cid:19)(cid:23)(cid:20)(cid:13) (cid:10) (cid:15)(cid:17)(cid:24)(cid:18)(cid:22)(cid:16)(cid:12)(cid:5)(cid:8) (cid:17)(cid:16)(cid:26)(cid:25)(cid:18)(cid:19)(cid:23)(cid:20)(cid:13) (cid:10) (cid:15)(cid:17)(cid:24)(cid:18)(cid:22)(cid:16)(cid:12)(cid:7)(cid:4) (cid:21)(cid:20)(cid:31)(cid:30)(cid:23)(cid:24)(cid:28)(cid:25)(cid:14) (cid:11) (cid:15)(cid:18)(cid:28)(cid:28)(cid:21)(cid:26)(cid:23)(cid:26)(cid:22)(cid:3)(cid:17)(cid:29)(cid:27)(cid:19)(cid:13)(cid:6)(cid:4)(cid:7)(cid:5) (cid:21)(cid:20)(cid:31)(cid:30)(cid:23)(cid:24)(cid:28)(cid:25)(cid:14) (cid:11) (cid:15)(cid:18)(cid:28)(cid:28)(cid:21)(cid:26)(cid:23)(cid:26)(cid:22)(cid:3)(cid:17)(cid:29)(cid:27)(cid:19)(cid:13)(cid:6)(cid:4)(cid:8)(cid:5) (cid:29)(cid:28)(cid:39)(cid:38)(cid:31) (cid:36)(cid:33)(cid:17) (cid:14) (cid:23)(cid:29)(cid:37)(cid:31)(cid:35)(cid:28)(cid:16)(cid:10)(cid:12) (cid:29)(cid:28)(cid:39)(cid:38)(cid:31) (cid:36)(cid:33)(cid:17) (cid:14) (cid:22)(cid:35)(cid:34)(cid:6) (cid:31)(cid:34)(cid:29)(cid:25)(cid:37)(cid:3)(cid:4)(cid:21)(cid:34)(cid:27)(cid:7)(cid:3)(cid:19)((cid:36)(cid:35)(cid:34)(cid:29)(cid:34)(cid:38)(cid:31)(cid:25)  )(cid:5) (cid:29)(cid:28)(cid:39)(cid:38)(cid:31) (cid:36)(cid:33)(cid:17) (cid:14) (cid:22)(cid:35)(cid:34)(cid:6) (cid:31)(cid:34)(cid:29)(cid:25)(cid:37)(cid:3)(cid:4)(cid:21)(cid:34)(cid:27)(cid:7)(cid:3)(cid:35)(cid:37)(cid:3)(cid:18)(cid:29)(cid:27)(cid:7)(cid:3)(cid:24)(cid:39)(cid:25)(cid:28)(cid:37)(cid:25)(cid:38)(cid:31)(cid:27)(cid:25)  )(cid:5)
| (cid:8) | (cid:8) | (cid:9) | (cid:9) | (cid:12) | (cid:12) | (cid:12) |
| ------- | ------- | ------- | ------- | -------- | -------- | -------- |
(cid:6) (cid:4) (cid:6) (cid:4) (cid:7) (cid:5) (cid:7) (cid:5) (cid:11) (cid:9)(cid:9) (cid:11) (cid:9)(cid:9) (cid:11) (cid:9)(cid:9)
(cid:4) (cid:6)(cid:9) (cid:9)(cid:4) (cid:11)(cid:9) (cid:14)(cid:21)(cid:5)(cid:16)(cid:4)(cid:17)(cid:4)(cid:27) (cid:5)(cid:6)(cid:9) (cid:5)(cid:9)(cid:4) (cid:5)(cid:11)(cid:9) (cid:6)(cid:4)(cid:4) (cid:4) (cid:6)(cid:9) (cid:9)(cid:4) (cid:11)(cid:9) (cid:14)(cid:21)(cid:5)(cid:16)(cid:4)(cid:17)(cid:4)(cid:27) (cid:5)(cid:6)(cid:9) (cid:5)(cid:9)(cid:4) (cid:5)(cid:11)(cid:9) (cid:6)(cid:4)(cid:4) (cid:5) (cid:7)(cid:10) (cid:10)(cid:5) (cid:12)(cid:10) (cid:16)(cid:26)(cid:6)(cid:20)(cid:5)(cid:21)(cid:5)  (cid:6)(cid:7)(cid:10) (cid:6)(cid:10)(cid:5) (cid:6)(cid:12)(cid:10) (cid:7)(cid:5)(cid:5) (cid:5) (cid:7)(cid:10) (cid:10)(cid:5) (cid:12)(cid:10) (cid:16)(cid:26)(cid:6)(cid:20)(cid:5)(cid:21)(cid:5)  (cid:6)(cid:7)(cid:10) (cid:6)(cid:10)(cid:5) (cid:6)(cid:12)(cid:10) (cid:7)(cid:5)(cid:5) (cid:11)(cid:13) (cid:13)(cid:9) (cid:15)(cid:13)(cid:21)(cid:34)(cid:10)(cid:28)(cid:9)(cid:29)(cid:9)((cid:10)(cid:11)(cid:13) (cid:10)(cid:13)(cid:9) (cid:10)(cid:15)(cid:13) (cid:11)(cid:9)(cid:9) (cid:11)(cid:13) (cid:13)(cid:9) (cid:15)(cid:13)(cid:21)(cid:34)(cid:10)(cid:28)(cid:9)(cid:29)(cid:9)((cid:10)(cid:11)(cid:13) (cid:10)(cid:13)(cid:9) (cid:10)(cid:15)(cid:13) (cid:11)(cid:9)(cid:9) (cid:11)(cid:13) (cid:13)(cid:9) (cid:15)(cid:13)(cid:21)(cid:34)(cid:10)(cid:28)(cid:9)(cid:29)(cid:9)((cid:10)(cid:11)(cid:13) (cid:10)(cid:13)(cid:9) (cid:10)(cid:15)(cid:13) (cid:11)(cid:9)(cid:9)
(cid:13)(cid:27)(cid:25)(cid:18)(cid:23)(cid:26)(cid:21)(cid:20)(cid:3)(cid:17)(cid:21)(cid:29)(cid:23)(cid:27)(cid:20)(cid:23)(cid:19)(cid:3)(cid:14)(cid:33)(cid:21)(cid:26)(cid:31)(cid:30)(cid:3)(cid:34)(cid:23)(cid:31)(cid:22)(cid:3)(cid:16)(cid:27)(cid:23)(cid:30)(cid:21) (cid:13)(cid:27)(cid:25)(cid:19)(cid:23)(cid:26)(cid:21)(cid:20)(cid:3)(cid:17)(cid:18)(cid:26)(cid:20)(cid:27)(cid:25)(cid:3)(cid:14) (cid:21)(cid:26)(cid:30)(cid:29)(cid:3)(cid:33)(cid:23)(cid:30)(cid:22)(cid:3)(cid:16)(cid:27)(cid:23)(cid:29)(cid:21) (cid:13)(cid:26)(cid:24)(cid:18)(cid:22)(cid:25)(cid:20)(cid:19)(cid:3)(cid:16)(cid:22)(cid:33)(cid:20)(cid:19)(cid:3)(cid:14)(cid:31)(cid:20)(cid:25)(cid:29)(cid:28)(cid:3) (cid:22)(cid:29)(cid:21)(cid:3)(cid:17)(cid:26)(cid:22)(cid:28)(cid:20)
| (cid:5)(cid:7)                                                                   |     | (cid:11)                                                                         |     | (cid:5)(cid:6)                                                                    |     |     |
| -------------------------------------------------------------------------------- | --- | -------------------------------------------------------------------------------- | --- | --------------------------------------------------------------------------------- | --- | --- |
| (cid:5)(cid:6)                                                                   |     |                                                                                  |     | (cid:5)(cid:4)                                                                    |     |     |
| (cid:21)(cid:20) (cid:31)(cid:23)(cid:24)(cid:28)(cid:25)(cid:12) (cid:5)(cid:4) |     | (cid:21)(cid:20)(cid:31)(cid:30)(cid:23)(cid:24)(cid:28)(cid:25)(cid:12) (cid:9) |     | (cid:20)(cid:19)(cid:30)(cid:29)(cid:22)(cid:23)(cid:27)(cid:24)(cid:12) (cid:11) |     |     |
| (cid:11)                                                                         |     |                                                                                  |     | (cid:9)                                                                           |     |     |
| (cid:9)                                                                          |     | (cid:7)                                                                          |     |                                                                                   |     |     |
| (cid:7)                                                                          |     | (cid:6)                                                                          |     | (cid:7)                                                                           |     |     |
| (cid:6)                                                                          |     |                                                                                  |     | (cid:6)                                                                           |     |     |
| (cid:4)                                                                          |     | (cid:4)                                                                          |     | (cid:4)                                                                           |     |     |
(cid:4) (cid:6)(cid:8) (cid:8)(cid:4) (cid:10)(cid:8) (cid:15)(cid:26)(cid:20)(cid:5)(cid:4)(cid:21)(cid:4)(cid:35) (cid:5)(cid:6)(cid:8) (cid:5)(cid:8)(cid:4) (cid:5)(cid:10)(cid:8) (cid:6)(cid:4)(cid:4) (cid:4) (cid:6)(cid:8) (cid:8)(cid:4) (cid:10)(cid:8) (cid:15)(cid:26)(cid:20)(cid:5)(cid:4)(cid:21)(cid:4)(cid:34) (cid:5)(cid:6)(cid:8) (cid:5)(cid:8)(cid:4) (cid:5)(cid:10)(cid:8) (cid:6)(cid:4)(cid:4) (cid:4) (cid:6)(cid:8) (cid:8)(cid:4) (cid:10)(cid:8) (cid:15)(cid:25)(cid:19)(cid:5)(cid:4)(cid:20)(cid:4)(cid:33) (cid:5)(cid:6)(cid:8) (cid:5)(cid:8)(cid:4) (cid:5)(cid:10)(cid:8) (cid:6)(cid:4)(cid:4)
(cid:18))(cid:39)(cid:42)(cid:29),(cid:37)(cid:45))((cid:3))(cid:34)(cid:3)(cid:25),(cid:37)(cid:35)(cid:37)((cid:29)(cid:38)(cid:3)(cid:29)( (cid:3)(cid:26)(cid:33)(cid:31))((cid:45)(cid:46),/(cid:31)(cid:46)(cid:33) (cid:3)(cid:27)(cid:33)(cid:43)/(cid:33)((cid:31)(cid:33)(cid:45)(cid:3)(cid:4)(cid:27)(cid:39)))(cid:46)(cid:36)(cid:33) (cid:3)(cid:30)1(cid:3)(cid:22)(cid:29)/(cid:45)(cid:45)(cid:37)(cid:29)((cid:3)(cid:21)(cid:37)(cid:38)(cid:46)(cid:33),(cid:6)(cid:3)2(cid:16)(cid:10)(cid:5) (cid:16)(cid:35)(cid:33)(cid:36)(cid:23)(cid:38)(cid:31)(cid:39)(cid:35)(cid:34)(cid:3)(cid:35)(cid:28)(cid:3)(cid:20)(cid:38)(cid:31)(cid:29)(cid:31)(cid:34)(cid:23) (cid:3)(cid:23)(cid:34)(cid:26)(cid:3)(cid:21)(cid:27)(cid:25)(cid:35)(cid:34)(cid:39)((cid:38))(cid:25)((cid:27)(cid:26)(cid:3)(cid:22)(cid:27)(cid:37))(cid:27)(cid:34)(cid:25)(cid:27)(cid:39)(cid:3)(cid:4)(cid:22)(cid:33)(cid:35)(cid:35)((cid:30)(cid:27)(cid:26)(cid:3)(cid:24)(cid:43)(cid:3)(cid:18)(cid:23))(cid:39)(cid:39)(cid:31)(cid:23)(cid:34)(cid:3)(cid:17)(cid:31) ((cid:27)(cid:38)(cid:6)(cid:3),(cid:14)(cid:9)(cid:5) (cid:17)(cid:36)(cid:34)(cid:37)(cid:24)(cid:39) ((cid:36)(cid:35)(cid:3)(cid:36)(cid:29)(cid:3)(cid:21)(cid:39) (cid:30) (cid:35)(cid:24)(cid:33)(cid:3)(cid:24)(cid:35)(cid:27)(cid:3)(cid:22)(cid:28)(cid:26)(cid:36)(cid:35)()(cid:39)(cid:42)(cid:26))(cid:28)(cid:27)(cid:3)(cid:23)(cid:28)(cid:38)(cid:42)(cid:28)(cid:35)(cid:26)(cid:28)((cid:3)(cid:4)(cid:23)(cid:34)(cid:36)(cid:36))(cid:31)(cid:28)(cid:27)(cid:3)(cid:25),(cid:3)(cid:19)(cid:24)(cid:42)(( (cid:24)(cid:35)(cid:3)(cid:18) (cid:33))(cid:28)(cid:39)(cid:6)(cid:3)(cid:45)(cid:15)(cid:9)(cid:5)
(cid:27)1((cid:46)(cid:36)(cid:33)(cid:46)(cid:37)(cid:31)(cid:3)(cid:19)(cid:29)(cid:46)(cid:29)
| (cid:15) (cid:24)(cid:33)(cid:28)(cid:20)(cid:3)(cid:26)(cid:33)(cid:31))((cid:45)(cid:46),/(cid:31)(cid:46)(cid:33)                                                                                            |     | (cid:12)                                                     |     | (cid:13)                                                            |     |     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------ | --- | ------------------------------------------------------------------- | --- | --- |
| (cid:14) (cid:21)(cid:28)(cid:20)(cid:3)(cid:26)(cid:33)(cid:31))((cid:45)(cid:46),/(cid:31)(cid:46)(cid:33)  (cid:24)(cid:33)(cid:28)(cid:20)(cid:3)(cid:26)(cid:33)(cid:45)(cid:37) /(cid:29)(cid:38)(cid:45) |     | (cid:11)                                                     |     | (cid:12)                                                            |     |     |
| (cid:33) /(cid:46)(cid:37)(cid:38)(cid:42)(cid:39)(cid:17) (cid:13) (cid:21)(cid:28)(cid:20)(cid:3)(cid:26)(cid:33)(cid:45)(cid:37) /(cid:29)(cid:38)(cid:45)                                                   |     | (cid:27)(cid:26))((cid:31) (cid:36)(cid:33)(cid:15) (cid:10) |     | (cid:28)(cid:27)(cid:42)) (cid:33)(cid:37)(cid:34)(cid:16) (cid:11) |     |     |
| (cid:12) (cid:28),(cid:29)(cid:37)((cid:7)(cid:28)(cid:33)(cid:45)(cid:46)(cid:3)(cid:27)(cid:42)(cid:38)(cid:37)(cid:46)                                                                                       |     |                                                              |     | (cid:10)                                                            |     |     |
| (cid:11)                                                                                                                                                                                                        |     | (cid:9)                                                      |     | (cid:9)                                                             |     |     |
| (cid:10)                                                                                                                                                                                                        |     | (cid:8)                                                      |     | (cid:8)                                                             |     |     |
| (cid:9)                                                                                                                                                                                                         |     |                                                              |     | (cid:7)                                                             |     |     |
(cid:8) (cid:8) (cid:10)(cid:13) (cid:13)(cid:8) (cid:15)(cid:13) (cid:23)((cid:9) (cid:8)(cid:8)(cid:33)0 (cid:9)(cid:10)(cid:13) (cid:9)(cid:13)(cid:8) (cid:9)(cid:15)(cid:13) (cid:10)(cid:8)(cid:8) (cid:7) (cid:7) (cid:9)(cid:12) (cid:12)(cid:7) (cid:13)(cid:12) (cid:19)(cid:34)(cid:8)(cid:26)(cid:7)(cid:7)(cid:27)(cid:42) (cid:8)(cid:9)(cid:12) (cid:8)(cid:12)(cid:7) (cid:8)(cid:13)(cid:12) (cid:9)(cid:7)(cid:7) (cid:7) (cid:9)(cid:12) (cid:12)(cid:7) (cid:14)(cid:12) (cid:20)(cid:35)(cid:8)(cid:27)(cid:7)(cid:7)(cid:28)(cid:43) (cid:8)(cid:9)(cid:12) (cid:8)(cid:12)(cid:7) (cid:8)(cid:14)(cid:12) (cid:9)(cid:7)(cid:7)
Synthetic Periodic Data Synthetic Non-Periodic Data Synthetic “Mixed” Data
|     | Figure11. Capturingperiodic,non-periodicandmixedpatternsinsyntheticdata. |     |     |     |     |     |
| --- | ------------------------------------------------------------------------ | --- | --- | --- | --- | --- |
(cid:14)(cid:37)(cid:35)(cid:38)(cid:25)((cid:33))(cid:37)(cid:36)(cid:3)(cid:37)(cid:30)(cid:3)(cid:21)((cid:33)(cid:31)(cid:33)(cid:36)(cid:25)(cid:34)(cid:3)(cid:25)(cid:36)(cid:28)(cid:3)(cid:22)(cid:29)(cid:27)(cid:37)(cid:36))(cid:42)((cid:43)(cid:27)(cid:42)(cid:29)(cid:28)(cid:3)(cid:24)(cid:33)(cid:35)(cid:29)(cid:3)(cid:23)(cid:29)(cid:39)(cid:43)(cid:29)(cid:36)(cid:27)(cid:29))(cid:3)(cid:4)(cid:23)(cid:35)(cid:37)(cid:37)(cid:42) (cid:29)(cid:28)(cid:3)(cid:26)(cid:45)(cid:3)(cid:17)(cid:25)(cid:43)))(cid:33)(cid:25)(cid:36)(cid:3)(cid:16)(cid:33)(cid:34)(cid:42)(cid:29)((cid:6)(cid:3)(cid:46)(cid:13)(cid:10)(cid:5) (cid:15)(cid:21)(cid:18)(cid:19)(cid:3)(cid:6) (cid:17)((cid:38))(cid:28)(cid:43)(cid:36),((cid:39)(cid:3)((cid:33)(cid:3)(cid:24)(cid:43)(cid:36)(cid:34)(cid:36)(cid:39)(cid:28)(cid:37)(cid:3)(cid:28)(cid:39)(cid:31)(cid:3)(cid:25) (cid:30)((cid:39),(cid:45)(cid:43)(cid:46)(cid:30)(cid:45) (cid:31)(cid:3)(cid:27)(cid:36)(cid:38) (cid:3)(cid:26) (cid:42)(cid:46) (cid:39)(cid:30) ,(cid:3)(cid:4)(cid:26)(cid:38)(((cid:45)(cid:35) (cid:31)(cid:3)(cid:29)0(cid:3)(cid:20)(cid:28)(cid:46),,(cid:36)(cid:28)(cid:39)(cid:3)(cid:19)(cid:36)(cid:37)(cid:45) (cid:43)(cid:6)(cid:3)1(cid:16)(cid:10)(cid:5) (cid:13)(cid:19)(cid:16)(cid:17)(cid:3)(cid:6)(cid:4)(cid:4)
(cid:20)(cid:37)(cid:28)(cid:29)(cid:3)(cid:9) (cid:5)(cid:8)(cid:4)(cid:4)(cid:4)(cid:4) (cid:14)(cid:19)(cid:16)(cid:12) (cid:15)(cid:7)(cid:7) (cid:23)((cid:31) (cid:3)(cid:9)(cid:7)(cid:7) (cid:12)(cid:17)(cid:14)(cid:10)
(cid:11)(cid:7)(cid:7) (cid:19)(cid:29)(cid:24)(cid:15)(cid:3)(cid:22)(cid:29)(cid:27)(cid:37)(cid:36))(cid:42)((cid:43)(cid:27)(cid:42)(cid:29)(cid:28) (cid:16)(cid:24)(cid:15)(cid:3)(cid:22)(cid:29)(cid:27)(cid:37)(cid:36))(cid:42)((cid:43)(cid:27)(cid:42)(cid:29)(cid:28) (cid:5)(cid:6)(cid:4)(cid:4)(cid:4)(cid:4) (cid:13)(cid:16)(cid:12) (cid:14)(cid:7)(cid:7) (cid:22) (cid:27)(cid:18)(cid:3)(cid:25) (cid:30)((cid:39),(cid:45)(cid:43)(cid:46)(cid:30)(cid:45) (cid:31) (cid:19)(cid:27)(cid:18)(cid:3)(cid:25) (cid:30)((cid:39),(cid:45)(cid:43)(cid:46)(cid:30)(cid:45) (cid:31) (cid:8)(cid:4)(cid:4)(cid:4)(cid:4)(cid:4) (cid:11)(cid:14)(cid:10)
|     |     | (cid:5)(cid:4)(cid:4)(cid:4)(cid:4)(cid:4) | (cid:13)(cid:7)(cid:7) |     |     | (cid:7)(cid:4)(cid:4)(cid:4)(cid:4)(cid:4) |
| --- | --- | ------------------------------------------ | ---------------------- | --- | --- | ------------------------------------------ |
(cid:29)(cid:35)(cid:33)(cid:24) (cid:10)(cid:7)(cid:7) (cid:23)(cid:23)(cid:21)(cid:14) (cid:11)(cid:4)(cid:4)(cid:4)(cid:4)  (cid:38)(cid:36)(cid:27) (cid:12)(cid:7)(cid:7) (cid:21)(cid:21)(cid:19)(cid:12)
|                       |     | (cid:10)(cid:4)(cid:4)(cid:4)(cid:4) |                        |     |     | (cid:6)(cid:4)(cid:4)(cid:4)(cid:4)(cid:4) |
| --------------------- | --- | ------------------------------------ | ---------------------- | --- | --- | ------------------------------------------ |
| (cid:9)(cid:7)(cid:7) |     | (cid:8)(cid:4)(cid:4)(cid:4)(cid:4)  | (cid:11)(cid:7)(cid:7) |     |     |                                            |
(cid:8)(cid:7)(cid:7) (cid:6)(cid:4)(cid:4)(cid:4)(cid:4) (cid:10)(cid:7)(cid:7) (cid:5)(cid:4)(cid:4)(cid:4)(cid:4)(cid:4)
|     |     | (cid:4) | (cid:9)(cid:7)(cid:7) |     |     | (cid:4) |
| --- | --- | ------- | --------------------- | --- | --- | ------- |
(cid:7) (cid:12)(cid:7) (cid:8)(cid:7)(cid:7) (cid:18)(cid:36)(cid:42)(cid:29)((cid:25)(cid:27)(cid:42)(cid:33)(cid:37)(cid:36)(cid:8)(cid:3)(cid:12)(cid:18)(cid:7)(cid:36)(cid:28)(cid:29), (cid:9)(cid:7)(cid:7) (cid:9)(cid:12)(cid:7) (cid:4) (cid:5)(cid:4)(cid:4)(cid:4) (cid:6)(cid:4)(cid:4)(cid:4)(cid:12)(cid:22)(cid:21)(cid:17)(cid:20)(cid:7)(cid:4)(cid:4)(cid:4) (cid:8)(cid:4)(cid:4)(cid:4) (cid:9)(cid:4)(cid:4)(cid:4) (cid:7) (cid:9)(cid:7) (cid:11)(cid:7) (cid:21)(cid:39)(cid:45) (cid:43)(cid:28)(cid:30)(cid:45)(cid:36)((cid:13)(cid:39)(cid:7)(cid:3)(cid:21)(cid:39)(cid:31) (cid:47) (cid:15)(cid:7) (cid:8)(cid:7)(cid:7) (cid:8)(cid:9)(cid:7) (cid:4) (cid:5)(cid:4)(cid:4)(cid:4) (cid:6)(cid:4)(cid:4)(cid:4)(cid:10)(cid:20)(cid:19)(cid:15)(cid:18)(cid:7)(cid:4)(cid:4)(cid:4) (cid:8)(cid:4)(cid:4)(cid:4) (cid:9)(cid:4)(cid:4)(cid:4)
(cid:17)((cid:38))(cid:28)(cid:43)(cid:36),((cid:39)(cid:3)((cid:33)(cid:3)(cid:24)(cid:43)(cid:36)(cid:34)(cid:36)(cid:39)(cid:28)(cid:37)(cid:3)(cid:28)(cid:39)(cid:31)(cid:3)(cid:25) (cid:30)((cid:39),(cid:45)(cid:43)(cid:46)(cid:30)(cid:45) (cid:31)(cid:3)(cid:27)(cid:36)(cid:38) (cid:3)(cid:26) (cid:42)(cid:46) (cid:39)(cid:30) ,(cid:3)(cid:4)(cid:26)(cid:38)(((cid:45)(cid:35) (cid:31)(cid:3)(cid:29)0(cid:3)(cid:20)(cid:28)(cid:46),,(cid:36)(cid:28)(cid:39)(cid:3)(cid:19)(cid:36)(cid:37)(cid:45) (cid:43)(cid:6)(cid:3)1(cid:16)(cid:10)(cid:5) (cid:6)(cid:4)(cid:4)(cid:4)(cid:4)(cid:4) (cid:14)(cid:20)(cid:17)(cid:18)(cid:3)(cid:8) (cid:16)(cid:39)(cid:37)((cid:27)(cid:42)(cid:35)(cid:43)(cid:39)(cid:38)(cid:3)(cid:39) (cid:3)(cid:23)(cid:42)(cid:35)(cid:33)(cid:35)(cid:38)(cid:27)(cid:36)(cid:3)(cid:27)(cid:38)(cid:30)(cid:3)(cid:24)(cid:31)(cid:29)(cid:39)(cid:38)(cid:43),(cid:42)(cid:45)(cid:29),(cid:31)(cid:30)(cid:3)(cid:26)(cid:35)(cid:37)(cid:31)(cid:3)(cid:25)(cid:31))(cid:45)(cid:31)(cid:38)(cid:29)(cid:31)(cid:43)(cid:3)(cid:4)(cid:25)(cid:37)(cid:39)(cid:39),(cid:34)(cid:31)(cid:30)(cid:3)(cid:28)(cid:47)(cid:3)(cid:19)(cid:27)(cid:45)(cid:43)(cid:43)(cid:35)(cid:27)(cid:38)(cid:3)(cid:18)(cid:35)(cid:36),(cid:31)(cid:42)(cid:6)(cid:3)0(cid:15)(cid:10)(cid:5) (cid:14)(cid:20)(cid:17)(cid:18)(cid:3)(cid:9)(cid:5)(cid:6)(cid:9)
(cid:15) (cid:7) (cid:7) (cid:23)((cid:31) (cid:3)(cid:11) (cid:22) (cid:27)(cid:18)(cid:3)(cid:25) (cid:30)((cid:39),(cid:45)(cid:43)(cid:46)(cid:30)(cid:45) (cid:31) (cid:5)(cid:10)(cid:9)(cid:4)(cid:4)(cid:4) (cid:13) (cid:12)(cid:15) (cid:18)(cid:15) (cid:11) (cid:11) (cid:13)(cid:7)(cid:7) (cid:22) (cid:21)(cid:31) (cid:39) (cid:26) (cid:30) (cid:17) (cid:31)(cid:3) (cid:3) (cid:12) (cid:24) (cid:8) (cid:31) (cid:9) (cid:29) (cid:12) (cid:39)(cid:38)(cid:43),(cid:42)(cid:45)(cid:29),(cid:31)(cid:30) (cid:5)(cid:9)(cid:4)(cid:4)(cid:4)(cid:4) (cid:13)(cid:18)(cid:15)(cid:11) (cid:12)(cid:15)(cid:11)
(cid:14) (cid:7) (cid:7) (cid:19)(cid:27)(cid:18)(cid:3)(cid:25) (cid:30)((cid:39),(cid:45)(cid:43)(cid:46)(cid:30)(cid:45) (cid:31) (cid:5)(cid:9)(cid:4)(cid:4)(cid:4)(cid:4) (cid:12)(cid:7)(cid:7) (cid:18)(cid:26)(cid:17)(cid:3)(cid:24)(cid:31)(cid:29)(cid:39)(cid:38)(cid:43),(cid:42)(cid:45)(cid:29),(cid:31)(cid:30) (cid:5)(cid:6)(cid:9)(cid:4)(cid:4)(cid:4)
(cid:13)(cid:7)(cid:7) (cid:5)(cid:6)(cid:9)(cid:4)(cid:4)(cid:4) (cid:11)(cid:7)(cid:7) (cid:5)(cid:4)(cid:4)(cid:4)(cid:4)(cid:4)
 (cid:38)(cid:36)(cid:27) (cid:12)(cid:7)(cid:7) (cid:22)(cid:22)(cid:20)(cid:13) (cid:5)(cid:4)(cid:4)(cid:4)(cid:4)(cid:4) (cid:31)(cid:37)(cid:35)(cid:26) (cid:22)(cid:22)(cid:20)(cid:13)
(cid:11)(cid:7)(cid:7) (cid:10)(cid:9)(cid:4)(cid:4)(cid:4) (cid:10)(cid:7)(cid:7) (cid:10)(cid:9)(cid:4)(cid:4)(cid:4)
(cid:10)(cid:7)(cid:7) (cid:9)(cid:4)(cid:4)(cid:4)(cid:4) (cid:9)(cid:7)(cid:7) (cid:9)(cid:4)(cid:4)(cid:4)(cid:4)
(cid:9)(cid:7)(cid:7) (cid:6)(cid:9)(cid:4)(cid:4)(cid:4) (cid:8)(cid:7)(cid:7) (cid:6)(cid:9)(cid:4)(cid:4)(cid:4)
| (cid:8)(cid:7)(cid:7) |     | (cid:4) |     |     |     | (cid:4) |
| --------------------- | --- | ------- | --- | --- | --- | ------- |
(cid:7) (cid:9)(cid:12) (cid:12)(cid:7) (cid:14)(cid:12) (cid:21)(cid:39)(cid:45) (cid:43)(cid:28)(cid:30)(cid:45)(cid:36)((cid:39)(cid:8)(cid:3)(cid:21)(cid:7)(cid:39)(cid:7)(cid:31) (cid:47) (cid:8)(cid:9)(cid:12) (cid:8)(cid:12)(cid:7) (cid:8)(cid:14)(cid:12) (cid:4) (cid:5)(cid:4)(cid:4)(cid:4) (cid:6)(cid:4)(cid:4)(cid:4)(cid:11)(cid:21)(cid:20)(cid:16)(cid:19)(cid:7)(cid:4)(cid:4)(cid:4) (cid:8)(cid:4)(cid:4)(cid:4) (cid:9)(cid:4)(cid:4)(cid:4) (cid:7) (cid:9)(cid:12) (cid:12)(cid:7) (cid:14)(cid:12) (cid:20)(cid:38),(cid:31)(cid:42)(cid:27)(cid:29)(cid:8),(cid:7)(cid:35)(cid:7)(cid:39)(cid:38)(cid:3)(cid:20)(cid:38)(cid:30)(cid:31)(cid:46) (cid:8)(cid:9)(cid:12) (cid:8)(cid:12)(cid:7) (cid:8)(cid:14)(cid:12) (cid:9)(cid:7)(cid:7) (cid:4) (cid:5)(cid:4)(cid:4)(cid:4) (cid:6)(cid:4)(cid:4)(cid:4)(cid:11)(cid:21)(cid:20)(cid:16)(cid:19)(cid:7)(cid:4)(cid:4)(cid:4) (cid:8)(cid:4)(cid:4)(cid:4) (cid:9)(cid:4)(cid:4)(cid:4)
|     | Figure12. | Capturingperiodic,non-periodicandmixedpatternsinrealdata. |     |     |     |     |
| --- | --------- | --------------------------------------------------------- | --- | --- | --- | --- |
Wecomparethelocalandglobalmappingsofthetwotimeencodingmethods. Asshowninthefigure,ourmethodcaptures
richerandmoredetailedtimepatternsindifferentdimensionsofthetimeencodingforlocalmappings. Bycontrast,the
FTEmethodexhibitsperiodicityinonlyonedimension. Thisoccursbecausethelearnedfrequencyparametersinother
dimensionsaretoosmalltocapturesufficientperiodicitylocally. Similarly,forglobalmappings,strongperiodicityisstill
observedinthefeaturemapofourmethod,alongsidevaryingdegreesofnon-periodicity. TheFTEcontinuestoexhibit
periodicityinonlyonedimension. Inotherdimensions,thesimilarfrequencyparametersresultininsufficientperiodicity
modelingandalackofnon-periodicpatternrepresentation.
Wealsopresentthenon-lineartransformationsketchesofSpline-basedLeTEinFigure10. Thefigureshowsthatthelearned
non-linearactivationfunctionsvaryacrossdimensions,significantlyenhancingthemodel’sexpressiveness. Additionally,
it demonstrates the modeling of both periodic and non-periodic patterns at local and global scales. Since Combined
LeTEisacombinationofFourier-basedLeTEandSpline-basedLeTE,itisintuitivethatCombinedLeTEinheritsthesame
interpretabilityasitscomponents. Furthermore,asourmethodsupportsthereconstructionofnon-linearactivationfunctions,
itretainsstronginterpretability.
G.4.CapturingPeriodic,Non-PeriodicandMixedPatternsinData
Complexperiodicandnon-periodicpatternsoftencoexistinreal-worlddata,formingmixedtimepatterns. Todemonstrate
thatourmethodsurpassespreviousmethodsinmodelingsuchpatterns,wedesignaminireconstructiontaskusingboth
syntheticdataandrealdatafromtheWikipediadataset. Specifically,weconstructanencoder-decodermodeltoreconstruct
thedata. Theencoderiseither(d-dimensional)ourLeTEortheFTE,whilethedecoderisasimplelinearlayermappinga
d-dimensionalvectortoa1-dimensionaloutput. ThereconstructionobjectiveminimizestheMSEloss,whichalsoquantifies
themodelingcapabilityofthetimeencodings. Additionally,thereconstructedtimesequenceplotsvisuallyindicatethe
models’abilitytofitthedata.
Toisolateperiodicandnon-periodicpatterns,wefirstgeneratesyntheticdatacontainingpurelyperiodicsignals,purely
24

RethinkingTimeEncodingviaLearnableTransformationFunctions
x
|     | y sin(x)              | y (1+sin(x))sin(2x)   | y log(1+ex |     | y =      |
| --- | --------------------- | --------------------- | ---------- | --- | -------- |
|     | =                     | =                     | =          | )   | 1+e−x    |
|     | (cid:6)(cid:4)(cid:5) | (cid:6)(cid:4)(cid:9) | (cid:10)   |     | (cid:10) |
(cid:9)
|     | (cid:5)(cid:4)(cid:9) | (cid:6)(cid:4)(cid:5) | (cid:9) |     |         |
| --- | --------------------- | --------------------- | ------- | --- | ------- |
|     |                       | (cid:5)(cid:4)(cid:9) | (cid:8) |     | (cid:8) |
FTE
|     | (cid:5)(cid:4)(cid:5) | (cid:5)(cid:4)(cid:5)         | (cid:7) |     | (cid:7) |
| --- | --------------------- | ----------------------------- | ------- | --- | ------- |
|     |                       | (cid:11)(cid:5)(cid:4)(cid:9) | (cid:6) |     | (cid:6) |
(cid:11)(cid:5)(cid:4)(cid:9)
|     |                               | (cid:11)(cid:6)(cid:4)(cid:5) | (cid:5) |     | (cid:5) |
| --- | ----------------------------- | ----------------------------- | ------- | --- | ------- |
|     |                               | (cid:11)(cid:6)(cid:4)(cid:9) |         |     | (cid:4) |
|     | (cid:11)(cid:6)(cid:4)(cid:5) |                               | (cid:4) |     |         |
(cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:7) (cid:5) (cid:7) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:7) (cid:5) (cid:7) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:6) (cid:4) (cid:6) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:6) (cid:4) (cid:6) (cid:8) (cid:10)
|                | (cid:6)(cid:4)(cid:5) | (cid:6)(cid:4)(cid:9) | (cid:10) |     | (cid:10) |
| -------------- | --------------------- | --------------------- | -------- | --- | -------- |
|                | (cid:5)(cid:4)(cid:9) | (cid:6)(cid:4)(cid:5) | (cid:9)  |     | (cid:9)  |
| Fourier-based  |                       | (cid:5)(cid:4)(cid:9) | (cid:8)  |     | (cid:8)  |
LeTE (cid:5)(cid:4)(cid:5) (cid:5)(cid:4)(cid:5) (cid:7) (cid:7)
(cid:11)(cid:5)(cid:4)(cid:9)
|     |                               |                               | (cid:6) |     | (cid:6) |
| --- | ----------------------------- | ----------------------------- | ------- | --- | ------- |
|     | (cid:11)(cid:5)(cid:4)(cid:9) | (cid:11)(cid:6)(cid:4)(cid:5) | (cid:5) |     | (cid:5) |
(cid:11)(cid:6)(cid:4)(cid:9)
|     | (cid:11)(cid:6)(cid:4)(cid:5) |     | (cid:4) |     | (cid:4) |
| --- | ----------------------------- | --- | ------- | --- | ------- |
(cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:7) (cid:5) (cid:7) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:7) (cid:5) (cid:7) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:6) (cid:4) (cid:6) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:6) (cid:4) (cid:6) (cid:8) (cid:10)
|     | (cid:6)(cid:4)(cid:5) |     | (cid:10) |     | (cid:10) |
| --- | --------------------- | --- | -------- | --- | -------- |
(cid:6)(cid:4)(cid:9)
|               | (cid:5)(cid:4)(cid:9) | (cid:6) (cid:4) (cid:5) | (cid:9) |     | (cid:9) |
| ------------- | --------------------- | ----------------------- | ------- | --- | ------- |
| Spline-based  |                       |                         |         |     | (cid:8) |
|               |                       | (cid:5) (cid:4) (cid:9) | (cid:8) |     |         |
LeTE (cid:5)(cid:4)(cid:5) (cid:5)(cid:4)(cid:5) (cid:7) (cid:7)
|     |                               | (cid:11)(cid:5)(cid:4)(cid:9) | (cid:6) |     | (cid:6) |
| --- | ----------------------------- | ----------------------------- | ------- | --- | ------- |
|     | (cid:11)(cid:5)(cid:4)(cid:9) | (cid:11)(cid:6)(cid:4)(cid:5) |         |     | (cid:5) |
|     |                               | (cid:11)(cid:6)(cid:4)(cid:9) | (cid:5) |     |         |
|     | (cid:11)(cid:6)(cid:4)(cid:5) |                               | (cid:4) |     | (cid:4) |
(cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:7) (cid:5) (cid:7) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:7) (cid:5) (cid:7) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:6) (cid:4) (cid:6) (cid:8) (cid:10) (cid:11)(cid:10) (cid:11)(cid:8) (cid:11)(cid:6) (cid:4) (cid:6) (cid:8) (cid:10)
Target Function
} Learned Function
Figure13. FTE,Fourier-basedLeTEandSpline-basedLeTEfittingdifferentfunctions.
non-periodicsignals,andmixedsignals. Thesedataisusedtoevaluatetheperformanceofdifferentencoders(LeTEorFTE).
ThegroundtruthandreconstructedsequencesareshowninFigure11. Asillustrated,theFTEmethodperformsreasonably
wellonperiodicdatabutstruggleswithnon-periodicandmixeddata. Incontrast,ourmethodconsistentlyoutperformsFTE,
demonstratingitscapabilitytomodelbothperiodicandnon-periodicpatternseffectively.
Real-worlddataoftenexhibitcomplexcombinationsofperiodicandnon-periodicpatterns,i.e.,mixedpatterns. Tofurther
evaluateourmethod,werandomlyselect4nodes’interactionsequencesfromtheWikipediadatasetandperformthesame
reconstructionexperiments. TheresultsarepresentedinFigure12,wherethetimesequencesaresmoothedusinga1D
Gaussianfilterforclarity. Asshown,thetimesequencesreconstructedusingourLeTEalignmorecloselywiththeoriginal
datacomparedtothosereconstructedusingFTE.Additionally,thelossofourLeTEissignificantlylowerthanthatofFTE,
furthervalidatingourmethod’sabilitytocapturecomplexperiodicandnon-periodicpatternsinreal-worlddata.
Theexperimentalresultsshowthat,regardlessofwhetherthesequenceisperiodicornon-periodic,ourmethodconsistently
outperformsbetter. Thisisprimarilyduetotheincorporationoflearnablenon-lineartransformationsintoourtimeencoding
approach.
G.5.FittingAbility
We conduct a simple toy experiment to further demonstrate that both Fourier-based LeTE and Spline-based LeTE are
capableofcapturingdifferentpatterns. Consequently,CombinedLeTEinheritsthisabilityaswell. Toillustratethis,we
generateasetoftrainingdatausing4differentnon-lineartransformationfunctions. Twoofthesefunctionsareperiodic: the
sinefunctiony = sin(x),andamorecomplexperiodicfunctiony = (1+sin(x))sin(2x). Theothertwofunctionsare
=log(1+ex)(Misra,2019),andtheSwishactivationfunctiony x
| non-periodic: | theSoftplusactivationfunctiony |     |     |     | =   |
| ------------- | ------------------------------ | --- | --- | --- | --- |
1+e−x
(Radfordetal.,2019).
Wefitthedatausingsimple1-dimensionalFTE,Fourier-basedLeTEandSpline-basedLeTE,evaluatingtheirabilityto
capturecomplexpatterns,includingbothperiodicandnon-periodic. Thelearnednon-lineartransformationfunctionsare
plottedinFigure13. Asshowninthefigure,bothFourier-basedLeTEandSpline-basedLeTEsuccessfullycapturediverse
25

RethinkingTimeEncodingviaLearnableTransformationFunctions
patterns. WealsocompareourmethodwithFTE.Duetothefixednon-lineartransformationfunctionsusedinFTE,itfails
tocapturethecomplexperiodicandnon-periodicpatternspresentinthedata. Theseresultsdemonstratethatourproposed
LeTEhasthecapabilitytomodelcomplexpatternsindataeffectivelyandismoregeneralthanprevioustimeencoding
methods.
H.MoreExplanationsandExamplesaboutInterpretability
Wechoosetousea4-dimensionalCombinedLeTEtopresentouranalysisrelatedtointerpretabilityofLeTE.Theexperiments
areconductedontheWikipediaandMOOCdatasets,withTGNandDyGFormerasbackbonemodels. Thetrainingprocess
andsettingsareconsistentwiththoseusedinthemainexperiments. Wewilldemonstratetheinterpretabilityofourmodel
fromthefollowingperspectives:
1. Reconstructing the learned non-linear transformation functions and plotting them to provide a clear and intuitive
analysis.
2. Analyzingeachdimensiontounderstandwhatinformationitrepresents. Specifically,thefirsttwodimensionsofthe
timeencodingareFourier-based,whilethelasttwodimensionsareSpline-based.
3. Comparingdifferentdatasetsunderthesamebackbonemodel.
4. Comparingdifferentbackbonemodels’LeTEunderthesamedataset.
5. Comparingtheplotsoflow-vs. high-dimensionalLeTEtoassesstheimpactofdimensionalityoninterpretability.
H.1.Reconstructing
Aspreviouslydiscussed,theprevioustimeencodingmethodsexhibitadegreeofinterpretabilitybyusingfixedsinusoidal
functions,whichinherentlyreflectperiodicpatterns. However,thisstronginductivebiasalsolimitstheirexpressivenessand
generalizationtocomplexornon-periodicity.
In contrast, our proposed LeTE is a fully learnable time encoding, and the learnable non-linear functions can still be
reconstructedandvisualizedfromlearnedparameters,allowingforinterpretabilityanalysisthroughfunctioninspection.
Wedemonstratethisinterpretabilityusinga4-dimensionalCombinedLeTE,trainedontheWikipedia/TGN.Figure14
showsthelearnedtransformationfunctionsforeachdimension. ThefirsttwodimensionsareFourier-based,andthelasttwo
areSpline-based.
H.2.AnalyzingEachDimension
Fourier-based: The Fourier coefficients explicitly encode frequency components, offering a clear, intuitive view of
the captured periodicity. Compared to fixed sinusoidal functions, our learnable Fourier-based time encoding captures
periodicpatternswithfinergranularityandgreaterflexibility,enablingtherepresentationofbothperiodicsignalsandsubtle
non-periodicitieswithinspecificranges.
Forasingledimension,low-frequencycomponentscapturelong-termtrends,whilehigh-frequencycomponentsfocuson
short-termfluctuations. Thisallowsthemodeltoencodebothlong-termdynamicsandshort-termvariationssimultaneously.
Asanexample,weapplythistotheWikipediadataset,whichrecordseditingactivities,wherenodesrepresentusersor
pages,andedgeswithtimestampscaptureeditingevents(frequencymagnitudespectrumisshowninFigure15,notethatthe
inputsaretimedifferencesinthiscase).
Specifically,Dim0showsastronghigh-frequencyresponse. Thelearnedcoefficientsincludecos(3x′):+0.29,cos(4x′):
−0.16,cos(5x′):−0.42. ThissuggeststhatDim0issensitivetoshort-termrepetitiveedits,i.e.,high-frequencyediting
behavior.
Dim 1 captures low- to mid-frequency patterns, with large coefficients: sin(1x′) : +0.96, sin(4x′) : +0.61, cos(4x′) :
+0.29. Thesereflectlonger-termperiodicbehaviors. Forexample,frequency-1maycorrespondtodailyorweeklyediting
cycles,whilefrequency-4maycapturesub-dailyrepeatedinteractions. Thisdimensionmayreflectuserhabitsorregular
communityeditingpatterns. Thus,LeTE’sFourier-baseddimensionsnotonlyretaintheperiodicinterpretabilityofsine
26

RethinkingTimeEncodingviaLearnableTransformationFunctions
Dim 0 (Fourier-based)
-0.4
-0.6
Dim 1 (Fourier-based)
1
0
Dim 2 (Spline-based)
0.5
0.0
Dim 3 (Spline-based)
-0.36
-0.38
|     |     | -4  |     | -2  |     | 0   |     | 2   |     | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time
Figure14.Plotsofthefourdimensionsofthenon-lineartransformationfunctionsofa4-dimensionalLeTEtrainedonWikipedia/TGN.
Wefurtherpresentthefourfunctionshere,theparametersarelearnedandreadfromthetrainedmodel:
|     |     |     | x′) |     | x′) |     | x′) |     |     | x′) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f 0 (x) = −0.0444 · cos(1 · 0 + 0.0758 · sin(1 · 0 + 0.0875 · cos(2 · 0 + 0.0704 · sin(2 · 0 + 0.0712 · cos(3 ·
x′)−0.0327·sin(3·x′)+0.0040·cos(4·x′)−0.0340·sin(4·x′)+0.0150·cos(5·x′)−0.0220·sin(5·x′)+0.0710·cos(1·
| 0   |     | 0   |     | 0   |     | 0   |     | 0   |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+0.1506·sin(1·x′)−0.1483·cos(2·x′)+0.2502·sin(2·x′)+0.2938·cos(3·x′)+0.0878·sin(3·x′)−0.1641·cos(4·
| 1   |     | 1   |     | 1   |     | 1   |     | 1   |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+0.0640·sin(4·x′)−0.4155·cos(5·x′)+0.0395·sin(5·x′)−0.0762,
| 1   |     | 1   |     | 1   |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | x′) |     | x′) |     | x′) |     |     | x′) |
f 1 (x) = +0.1860 · cos(1 · 0 + 0.0267 · sin(1 · 0 + 0.1971 · cos(2 · 0 − 0.0510 · sin(2 · 0 − 0.0225 · cos(3 ·
x′)−0.0909·sin(3·x′)−0.0501·cos(4·x′)+0.1460·sin(4·x′)+0.0952·cos(5·x′)+0.2974·sin(5·x′)−0.1604·cos(1·
| 0   |     | 0   |     | 0   |     | 0   |     | 0   |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+0.9609·sin(1·x′)+0.2323·cos(2·x′)−0.3430·sin(2·x′)−0.0441·cos(3·x′)−0.1428·sin(3·x′)+0.2930·cos(4·
| 1   |     | 1   |     | 1   |     | 1   |     | 1   |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+0.6073·sin(4·x′)+0.0330·cos(5·x′)−0.1345·sin(5·x′)−0.0130,
| 1             |     | 1       |                              | 1   |     | 1                 |     |     |     |     |
| ------------- | --- | ------- | ---------------------------- | --- | --- | ----------------- | --- | --- | --- | --- |
| here,forbothf |     | (x)andf | (x),x′ =1.0069·x+0.0069andx′ |     |     | =0.0054·x+0.0108. |     |     |     |     |
|               | 0   | 1       | 0                            |     |     | 1                 |     |     |     |     |
f (x)=+0.0013·B (x)(support:[-2.20,-1.80])+0.0047·B (x)(support:[-1.80,-1.40])−0.0353·B (x)(support:[-1.40,-1.00])−
| 2   |     | 0   |     |     |     | 1   |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0321·B (x)(support:[-1.00,-0.60])−0.0455·B (x)(support:[-0.60,-0.20])−0.0273·B (x)(support:[-0.20,0.20])+0.0211·
|                                     | 3   |     |     |                                          | 4   |     |     | 5   |     |     |
| ----------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| B (x)(support:[0.20,0.60])+0.0248·B |     |     |     | (x)(support:[0.60,1.00])+0.4133·Tanh(x), |     |     |     |     |     |     |
| 6                                   |     |     |     | 7                                        |     |     |     |     |     |     |
f 3 (x)=−0.0008·B 0 (x)(support:[-2.20,-1.80])−0.0072·B 1 (x)(support:[-1.80,-1.40])−0.0040·B 2 (x)(support:[-1.40,-1.00])+
0.0227·B (x)(support:[-1.00,-0.60])−0.0067·B (x)(support:[-0.60,-0.20])+0.0248·B (x)(support:[-0.20,0.20])+0.0165·
|                                     | 3   |     |     |                                          | 4   |     |     | 5   |     |     |
| ----------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| B (x)(support:[0.20,0.60])+0.0078·B |     |     |     | (x)(support:[0.60,1.00])+0.0100·Tanh(x). |     |     |     |     |     |     |
| 6                                   |     |     |     | 7                                        |     |     |     |     |     |     |
27

RethinkingTimeEncodingviaLearnableTransformationFunctions
0.40
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0.00
1 2 3 4 5
Frequency (k)
edutingaM
Frequency Magnitude Spectrum (Dim 0)
1.0
Magnitude (x'_0)
Magnitude (x'_1)
0.8
0.6
0.4
0.2
0.0
1 2 3 4 5
Frequency (k)
(a)Dim0(Fourier-based)
edutingaM
Frequency Magnitude Spectrum (Dim 1)
Magnitude (x'_0)
Magnitude (x'_1)
(b)Dim1(Fourier-based)
Figure15.FrequencyMagnitudeSpectrumforthefirsttwodimensionsofthenon-lineartransformationfunctionsofLeTEtrainedon
Wikipedia/TGN.ThesetwodimensionsareFourier-based.
functionsbutalsoexhibitricherfrequencycomposition,allowingittosimultaneouslycapturebothshort-termburstsand
long-termrhythms.
Inaddition,thisapproachcouldbeextendedtoanalyzemorecomplexpatterns. However,asourgoalhereistopresentthe
underlyingidea,wewillnotgodeeperhere.
Spline-based: TheSpline-basedfunctionsoffercomplementaryadvantages,particularlyfornon-periodicity.
Inourspline-baseddimensions,whereweappliedabasisfunction(Tanh),iftheweightofthebasisfunctionishigher,
itmaydominateaspecificdimension—suchasDim2inFigure14. However,thereareotherdimensionswheresplines
dominate,suchasDim3. Tofurtherclarifythis,wecombinethespecificWikipediadatasetandexplain:
Dim2: Theoutputincreasesmonotonicallywithtimedifference,indicatingatime-decay-likeeffect—thelongerthetime
sincelastedit,thestrongertheencodingresponse. Thismaysuggestthetimeencodinghaslearnedthatre-activationafter
longinactivityisasignificanteventinthisspecificcase.
Dim 3: The function exhibits sharp peaks and local bumps, indicating that the model assigns particular importance to
certaintimeintervals. Thesemaycorrespondtoknownactiveeditingwindowsorreactiondelays. Thesharpnessofsome
coefficientssuggeststhemodelhascapturedrarebutimportanttemporalphenomena,suchasone-offcampaignsoranomaly
spikes.
TheSplinecoefficientsinherentlycapturelocaltemporalfeatures,indicatingspecifictimeintervalsthatthemodelconsiders
criticaloractive. Sharppeakscoefficientswithinthesecurvessuggesttheoccurrenceofsuddeneventsoranomalies. This
localcharacteristicisadvantageousforidentifyingrarephenomena.
H.3.DifferentDatasets
Wereconstructedandplottedthefournon-linearfunctionsfora4-dimensionalLeTEtrainedonMOOC/TGN(shownin
Figure16). BycomparingtheseresultstothosefromtheWikipedia(Figure14),itcanbeseenthattheDim0exhibita
lackofperiodicity. FromthereconstructedequationsofDim0,thehigher-frequencytermsdohavecoefficientswithsome
magnitude,buttheyaregenerallysmall. Forinstance,thecoefficientsofcos(5x′)andsin(5x′)arerelativelysmall(e.g.,
−0.0134and−0.0136),suggestingthattheircontributionisminimalandinsufficienttogeneratesignificantfluctuations. As
aresult,theoverallfunctionprimarilyexhibitsslowoscillations,makingtheplotappeartobepredominantlynon-periodic
withinacertaininputwindow.
ThisobservationalignswiththefindingsinAppendixG.1andFigure8,wherethespectralentropystatisticsalsoshowthat
theWikipediaexhibitsstrongerperiodicitycomparedtotheMOOC.
Thus,bycomparingthenon-linearfunctionsofLeTEacrossdifferentdatasets,wecanindirectlyexploretheperiodicor
non-periodicnatureofthedatapresent.
28

RethinkingTimeEncodingviaLearnableTransformationFunctions
Dim 0 (Fourier-based)
0.2
0.0
-0.2
Dim 1 (Fourier-based)
0.0
-0.2
-0.4
Dim 2 (Spline-based)
0.25
0.00
Dim 3 (Spline-based)
0.0
-0.2
|     |     | -4  |     |     | -2  |     |     | 0   |     | 2   |     | 4   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time
Figure16.Plotsofthefourdimensionsofthenon-lineartransformationfunctionsofa4-dimensionalLeTEtrainedonMOOC/TGN.We
furtherpresentthefourfunctionshere,theparametersarelearnedandreadfromthetrainedmodel:
|     |     |     | x′) |     |     | x′) |     |     | x′) |     | x′) |     | x′) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f 0 (x) = −0.0186 · cos(1 · 0 − 0.0131 · sin(1 · 0 − 0.0173 · cos(2 · 0 + 0.0039 · sin(2 · 0 + 0.0019 · cos(3 · 0 +
0.0013·sin(3·x′)+0.0032·cos(4·x′)−0.0096·sin(4·x′)−0.0134·cos(5·x′)−0.0136·sin(5·x′)+0.3140·cos(1·x′)+
|     |     | 0   |     | 0   |     |     | 0   |     | 0   |     | 0   |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.5998·sin(1·x′)−0.2781·cos(2·x′)+0.4591·sin(2·x′)+0.1376·cos(3·x′)+0.2296·sin(3·x′)−0.0880·cos(4·x′)−
|     |     | 1   |     | 1   |     |     | 1   |     | 1   |     | 1   |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0198·sin(4·x′)−0.2621·cos(5·x′)+0.0030·sin(5·x′)+0.0016,
|     |     | 1   |     | 1   |     |     | 1   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | x′) |     |     |     | x′) |     | x′) |     |     | x′) |     |
f 1 (x) = +0.0816 · cos(1 · 0 + 0.0362 · sin(1 · 0 + 0.0588 · cos(2 · 0 − 0.0046 · sin(2 · 0 − 0.0199 · cos(3 ·
x′)−0.0082·sin(3·x′)−0.0121·cos(4·x′)+0.0325·sin(4·x′)+0.0591·cos(5·x′)+0.0609·sin(5·x′)−0.4787·cos(1·
| 0   |     | 0   |     |     | 0   |     |     | 0   |     | 0   |     | 0   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+1.1011·sin(1·x′)+0.0467·cos(2·x′)−0.4438·sin(2·x′)−0.1300·cos(3·x′)−0.2972·sin(3·x′)+0.3344·cos(4·
| 1   |     | 1   |     |     | 1   |     |     | 1   |     | 1   |     | 1   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+0.1396·sin(4·x′)+0.0593·cos(5·x′)−0.0841·sin(5·x′)+0.1166,
| 1             |     | 1       |        |                       | 1   |     |     | 1                  |     |     |     |     |     |
| ------------- | --- | ------- | ------ | --------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
| here,forbothf |     | (x)andf | (x),x′ | =0.9857·x+0.0971andx′ |     |     |     | =−0.0187·x+0.0885. |     |     |     |     |     |
|               |     | 0       | 1 0    |                       |     |     | 1   |                    |     |     |     |     |     |
f (x)=+0.0020·B (x)(support:[-2.20,-1.80])+0.0071·B (x)(support:[-1.80,-1.40])−0.0979·B (x)(support:[-1.40,-1.00])−
| 2   |     | 0   |     |     |     |     | 1   |     |     |     | 2   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0916·B (x)(support:[-1.00,-0.60])−0.1039·B (x)(support:[-0.60,-0.20])−0.3442·B (x)(support:[-0.20,0.20])−0.3597·
|                                     | 3   |     |     |     |                                          | 4   |     |     |     | 5   |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| B (x)(support:[0.20,0.60])−0.3093·B |     |     |     |     | (x)(support:[0.60,1.00])+0.2827·Tanh(x), |     |     |     |     |     |     |     |     |
| 6                                   |     |     |     |     | 7                                        |     |     |     |     |     |     |     |     |
f 3 (x)=−0.0011·B 0 (x)(support:[-2.20,-1.80])−0.0099·B 1 (x)(support:[-1.80,-1.40])+0.0364·B 2 (x)(support:[-1.40,-1.00])+
0.0712·B (x)(support:[-1.00,-0.60])+0.0169·B (x)(support:[-0.60,-0.20])+0.2372·B (x)(support:[-0.20,0.20])+0.2886·
|                                     | 3   |     |     |     |                                          | 4   |     |     |     | 5   |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| B (x)(support:[0.20,0.60])+0.2155·B |     |     |     |     | (x)(support:[0.60,1.00])+0.0947·Tanh(x). |     |     |     |     |     |     |     |     |
| 6                                   |     |     |     |     | 7                                        |     |     |     |     |     |     |     |     |
29

RethinkingTimeEncodingviaLearnableTransformationFunctions
Dim 0 (Fourier-based)
0
-1
Dim 1 (Fourier-based)
1
0
-1
Dim 2 (Spline-based)
1
0
-1
Dim 3 (Spline-based)
0.5
0.0
-0.5
-4 -2 0 2 4
Time
Figure17.Plotsofthefourdimensionsofthenon-lineartransformationfunctionsofa4-dimensionalLeTEtrainedonWikipedia/TGN.
They-axeshavebeenscaledtothesamelevelas18tofacilitateadirectcomparison.Thereconstructedfunctionsarethesameasinthe
Figure14.
H.4.DifferentBackbones
WeprovideplotsofthesamedatasettrainedwithTGNandDyGFormer,showninFigure17andFigure18,withthey-axes
settothesamelevelforeachbackbonetofacilitateadirectcomparison). Asthefiguresdemonstrate,despiteusingdifferent
backbonemodels,thelearnedfunctionsexhibitsimilartrendsandshapesforeachdimension. Thisillustratesthestabilityof
ourmethodandmakestheinterpretabilityprocessmorereliable.
Ofcourse,theremaybesomedetaileddifferencesbetweenLeTEstrainedondifferentbackbones. Thisisintuitivelydueto
thepresenceofvariousinfluencingfactors,suchasthemodelarchitecture,theinteractionofLeTEwithothermodules,the
optimizationprocessandetc. However,wecanvalidatetheideabyinspectingtheplotinasimplifiedmanner.
H.5.ComparingLower-andHigher-dimensionalLeTE
Wefurthercomparethelower-andhigher-dimensionalLeTEbyreconstructingthenon-linearfunctionsandplottingthem
(please refer to and compare Figure 14 and 19). Intuitively, the higher-dimensional representation will provide more
information. Asseenfromtheplots,Dim2inFigure19isdominatedbythebasisfunction,partiallylosingtheinformation
capturedbyDim3inFigure14.
Fromtheperspectiveofthereconstructedfunctions,fortheFourier-baseddimensions,theLeTEwithonlyoneFourier-based
dimensionhasasingleinputtransformation,x′ ,andallfrequencycomponentsarecomputedbasedonthistransformation.
0
ThismeanstheLeTEencodesonabroadertimescale(reminder: weusedtheWikipediadataset)andmodelsthetime
differencevariationsofeditingactivitieswithoutdistinguishingpatternsatdifferentscales. SincethereisonlyoneFourier-
baseddimension,allfrequencycomponentsarecontrolledbythesameinputtransformation,makingitharderforthemodel
tointerpreteditingpatternsatdifferenttimescales. Incontrast,fortheLeTEwithtwoFourier-baseddimensions,each
dimensionhasdifferentinputtransformations(x′ andx′ ),enablingthemodeltocapturemoredetailededitingbehaviors
0 1
at different scales. For example, Dim 0 might rely more on x′ (with a larger scaling factor), focusing on short-term
0
fluctuations(high-frequencycomponents),whileDim1mightrelymoreonx′ (withasmallerscalingfactor),focusing
1
30

RethinkingTimeEncodingviaLearnableTransformationFunctions
Dim 0 (Fourier-based)
0
-1
Dim 1 (Fourier-based)
1
0
-1
Dim 2 (Spline-based)
1
0
-1
Dim 3 (Spline-based)
0.5
0.0
-0.5
|     |     | -4  |     | -2  |     | 0   |     | 2   |     | 4   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Time
Figure18.Plotsofthefourdimensionsofthenon-lineartransformationfunctionsofa4-dimensionalLeTEtrainedonWikipedia/TGN.
They-axeshavebeenscaledtothesamelevelas17tofacilitateadirectcomparison. Wefurtherpresentthefourfunctionshere,the
parametersarelearnedandreadfromthetrainedmodel:
|     |     |     | x′) |     | x′) |     | x′) |     |     | x′) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f 0 (x) = −0.0727 · cos(1 · 0 + 0.0704 · sin(1 · 0 + 0.1529 · cos(2 · 0 + 0.1720 · sin(2 · 0 + 0.1554 · cos(3 ·
x′)−0.0320·sin(3·x′)−0.0385·cos(4·x′)−0.0220·sin(4·x′)−0.0086·cos(5·x′)−0.1107·sin(5·x′)+0.0758·cos(1·
| 0   |     | 0   |     | 0   |     | 0   |     | 0   |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+0.2909·sin(1·x′)−0.2430·cos(2·x′)+0.3166·sin(2·x′)+0.2097·cos(3·x′)+0.0334·sin(3·x′)−0.3308·cos(4·
| 1   |     | 1   |     | 1   |     | 1   |     | 1   |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)−0.0664·sin(4·x′)−0.4329·cos(5·x′)−0.1351·sin(5·x′)−0.0009,
| 1   |     | 1   |     | 1   |     | 1   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | x′) |     | x′) |     | x′) |     |     | x′) |
f 1 (x) = +0.2232 · cos(1 · 0 + 0.1531 · sin(1 · 0 + 0.2963 · cos(2 · 0 − 0.0852 · sin(2 · 0 − 0.0409 · cos(3 ·
x′)−0.1263·sin(3·x′)−0.0938·cos(4·x′)+0.1772·sin(4·x′)+0.1431·cos(5·x′)+0.3435·sin(5·x′)−0.2795·cos(1·
| 0   |     | 0   |     | 0   |     | 0   |     | 0   |     | 0   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+1.0935·sin(1·x′)+0.1297·cos(2·x′)−0.4577·sin(2·x′)−0.0711·cos(3·x′)−0.3519·sin(3·x′)+0.4151·cos(4·
| 1   |     | 1   |     | 1   |     | 1   |     | 1   |     | 1   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
x′)+0.5552·sin(4·x′)+0.0696·cos(5·x′)−0.1653·sin(5·x′)−0.0245,
| 1             |     | 1         |                              | 1   |     | 1                   |     |     |     |     |
| ------------- | --- | --------- | ---------------------------- | --- | --- | ------------------- | --- | --- | --- | --- |
|               |     |           | (x),x′ =0.9936·x−0.0016andx′ |     |     |                     |     |     |     |     |
| here,forbothf | 0   | (x)andf 1 | 0                            |     |     | 1 =0.0009·x−0.0678. |     |     |     |     |
f (x)=+0.0012·B (x)(support:[-2.20,-1.80])+0.0043·B (x)(support:[-1.80,-1.40])−0.0096·B (x)(support:[-1.40,-1.00])−
| 2   |     | 0   |     |     | 1   |     |     |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.0071·B (x)(support:[-1.00,-0.60])−0.0197·B (x)(support:[-0.60,-0.20])−0.0075·B (x)(support:[-0.20,0.20])+0.0045·
|                                     | 3   |     |     |                                          | 4   |     |     | 5   |     |     |
| ----------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| B (x)(support:[0.20,0.60])+0.0038·B |     |     |     | (x)(support:[0.60,1.00])+0.4794·Tanh(x), |     |     |     |     |     |     |
| 6                                   |     |     |     | 7                                        |     |     |     |     |     |     |
f 3 (x)=−0.0008·B 0 (x)(support:[-2.20,-1.80])−0.0074·B 1 (x)(support:[-1.80,-1.40])+0.0026·B 2 (x)(support:[-1.40,-1.00])+
0.0294·B (x)(support:[-1.00,-0.60])−0.0009·B (x)(support:[-0.60,-0.20])+0.0179·B (x)(support:[-0.20,0.20])+0.0037·
|                                     | 3   |     |     |                                          | 4   |     |     | 5   |     |     |
| ----------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| B (x)(support:[0.20,0.60])+0.0031·B |     |     |     | (x)(support:[0.60,1.00])−0.0395·Tanh(x). |     |     |     |     |     |     |
| 6                                   |     |     |     | 7                                        |     |     |     |     |     |     |
31

RethinkingTimeEncodingviaLearnableTransformationFunctions
Dim 0 (Fourier-based)
2
0
Dim 1 (Spline-based)
0.2
0.0
-0.2
-4 -2 0 2 4
Time
Figure19.Plotsofthetwodimensionsofthenon-lineartransformationfunctionsofa2-dimensionalLeTEtrainedonWikipedia/TGN.
Wefurtherpresentthefourfunctionshere,theparametersarelearnedandreadfromthetrainedmodel:
f (x) = −0.9560 · cos(1 · (x′)) + 0.3821 · sin(1 · (x′)) + 0.2430 · cos(2 · (x′)) − 0.3138 · sin(2 · (x′)) − 0.4807 · cos(3 ·
0
(x′))−0.1918·sin(3·(x′))−0.6372·cos(4·(x′))−0.2811·sin(4·(x′))+0.1555·cos(5·(x′))+0.0840·sin(5·(x′))+0.0334,
here,x′ =0.9963·x−0.0092.
f (x)=−0.0020·B (x)(support:[-2.20,-1.80])−0.0022·B (x)(support:[-1.80,-1.40])+0.0097·B (x)(support:[-1.40,-1.00])−
1 0 1 2
0.0636·B (x)(support:[-1.00,-0.60])−0.0556·B (x)(support:[-0.60,-0.20])−0.0123·B (x)(support:[-0.20,0.20])−0.0054·
3 4 5
B (x)(support:[0.20,0.60])−0.0011·B (x)(support:[0.60,1.00])−0.1945·Tanh(x).
6 7
moreonlong-termtrends(low-frequencycomponents).Thus,higherdimensionsallowthemodeltohandleeditingbehaviors
atdifferenttimescales,providinghigherinterpretability.
Similarly,fortheLeTEwithonlyoneSpline-baseddimension,itprimarilyfocusesonadjustingasinglelevel,potentially
describinghowtimeaffectseditingbehaviors. However,relyingonjustoneSpline-baseddimensionmaymakeitdifficultto
capturerelativelycomplextimedynamics. FortheLeTEwithtwoSpline-baseddimensions,theweightsofthecoefficients
aremoredistributed,grantingtheoverallLeTEstrongerlocaladjustmentcapabilities. Moreover,sinceadimensionmaybe
dominatedbybasisfunctionorSplinefunctions,higherdimensionsnaturallyhavestrongerexpressivepower.
Althoughhigher-dimensionalLeTEsofferstrongerperformanceandbetterexplaintheinformationcapturedbythemodel,
theinterpretabilityanalysisofsuchhigher-dimensionalLeTEsbecomesmorecomplexandmayrequireadimension-by-
dimensionanalysis.
I.LimitationandFutureWork
Inthispaper,weintroduceLeTE,ageneraltimeencodingmethod. Generally,CombinedLeTEoffersbetterperformanceas
itleveragesthestrengthsofbothFourier-basedLeTEandSpline-basedLeTE,enablingittoeffectivelycaptureboththe
periodicityandnon-periodicityoftime. However,inpracticalscenarios,thechoiceofthehyperparameterporamongthe
threevariantsmaydependonthecharacteristicsofthedataandthespecifictaskrequirements.
We also explore the impact of the time encoding dimension on downstream task performance. Similarly, selecting an
appropriatetimeencodingdimensionmayvarydependingonthedataandtasks. Notably,weobservethatevenwithasmall
dimension,LeTEcanachieveacceptableresultsindownstreamtasks.
Additionally,wementionthatcertainpositionencodingmethodscanbeconsideredspecialcasesofourapproach. However,
aspositionencodingisnottheprimaryfocusofthispaper,wedidnotprovideformalproofs. Webelievethatextendingthe
ideasproposedinthispapertomodelsthatusepositionencodingcouldyieldimprovedresults,makingthisapromising
directionforfutureresearch.
J.CodeImplementation
ThecodesareavailableataGitHubRepository.
32