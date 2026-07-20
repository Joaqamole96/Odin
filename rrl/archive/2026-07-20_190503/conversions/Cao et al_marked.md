PublishedasaconferencepaperatICLR2024
| TEMPO:      |     | PROMPT-BASED |     |     | GENERATIVE |        |             | PRE-TRAINED |     |
| ----------- | --- | ------------ | --- | --- | ---------- | ------ | ----------- | ----------- | --- |
| TRANSFORMER |     |              |     |     | TIME       | SERIES | FORECASTING |             |     |
FOR
DefuCao1,FurongJia1,SercanO¨.Arık2,TomasPfister2,YixiangZheng1,WenYe1,YanLiu1
1UniversityofSouthernCalifornia
2GoogleCloudAIResearch
| {defucao, |     | florajia,             | yixiangzheng, |     | yewen, | yanliu.cs}@usc.edu |     |     |     |
| --------- | --- | --------------------- | ------------- | --- | ------ | ------------------ | --- | --- | --- |
| {soarik,  |     | tpfister}@google.com, |               |     |        |                    |     |     |     |
ABSTRACT
Thepastdecadehaswitnessedsignificantadvancesintimeseriesmodelingwith
|     | deep                                               | learning. | While | achieving | state-of-the-art |     | results, | the best-performing  | ar- |
| --- | -------------------------------------------------- | --------- | ----- | --------- | ---------------- | --- | -------- | -------------------- | --- |
|     | chitecturesvaryhighlyacrossapplicationsanddomains. |           |       |           |                  |     |          | Meanwhile,fornatural |     |
languageprocessing,theGenerativePre-trainedTransformer(GPT)hasdemon-
|     | strated | impressive | performance    |          | via training      | one        | general-purpose | model              | across |
| --- | ------- | ---------- | -------------- | -------- | ----------------- | ---------- | --------------- | ------------------ | ------ |
|     | various | textual    | datasets.      | It       | is intriguing     | to explore | whether         | GPT-type architec- |        |
|     | tures   | can be     | effective      | for time | series, capturing |            | the intrinsic   | dynamic attributes |        |
|     | and     | leading    | to significant | accuracy | improvements.     |            | In this         | paper, we propose  | a      |
novelframework,TEMPO,thatcaneffectivelylearntimeseriesrepresentations.
|     | We focus           | on  | utilizing                                            | two essential | inductive | biases | of  | the time series | task for |
| --- | ------------------ | --- | ---------------------------------------------------- | ------------- | --------- | ------ | --- | --------------- | -------- |
|     | pre-trainedmodels: |     | (i)decompositionofthecomplexinteractionbetweentrend, |               |           |        |     |                 |          |
seasonalandresidualcomponents;and(ii)introducingthedesignofpromptsto
|     | facilitatedistributionadaptationindifferenttypesoftimeseries. |     |     |     |     |     |     | TEMPOexpands |     |
| --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- |
thecapabilityfordynamicallymodelingreal-worldtemporalphenomenafromdata
|     | withindiversedomains. |     |     | Ourexperimentsdemonstratethesuperiorperformanceof |     |     |     |     |     |
| --- | --------------------- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
TEMPOoverstate-of-the-artmethodsonzeroshotsettingforanumberoftime
|     | seriesbenchmarkdatasets. |     |     | Thisperformancegainisobservednotonlyinscenarios |     |     |     |     |     |
| --- | ------------------------ | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
involvingpreviouslyunseendatasetsbutalsoinscenarioswithmulti-modalinputs.
ThiscompellingfindinghighlightsTEMPO’spotentialtoconstituteafoundational
model-buildingframework.
1 INTRODUCTION
Timeseriesforecasting,i.e.,predictingfuturedatabasedonhistoricalobservations,hasbroadreal-
worldapplications,suchashealth,transportation,financeandsoon. Inthepastdecade,numerous
deepneuralnetworkarchitectureshavebeenappliedtotimeseriesmodeling,includingconvolutional
neuralnetworks(CNN)(Baietal.,2018),recurrentneuralnetworks(RNN)(Siami-Naminietal.,
2018),graphneuralnetworks(GNN)(Lietal.,2018;Caoetal.,2021),andTransformers(Liuetal.,
2021;Zhouetal.,2021;Wuetal.,2023;Zhouetal.,2022;Wooetal.,2022;Kitaevetal.,2020;Nie
etal.,2023),leadingtostate-of-the-artsresults.Whileachievingstrongpredictionperformance,some
ofthepreviousworksontimeseriesmostlybenefitfromtheadvanceinsequencemodeling(from
RNNandGNN,totransformers)thatcapturestemporaldependenciesbuthavenotfullycapitalized
onthebenefitsofintricatepatternswithintimeseriesdata,suchasseasonality,trend,andresidual.
These components are the key differentiating factors of time series from classical sequence data
(Fildesetal.,1991). Asaresult,recentstudiessuggestthatdeeplearning-basedarchitecturesmight
notbeasrobustaspreviouslythoughtandmightevenbeoutperformedbyshallowneuralnetworks
orevenlinearmodelsonsomebenchmarks (Zengetal.,2023;Zhangetal.,2022b;Wuetal.,2023;
Ekambarametal.,2023;Fanetal.,2022). Despitethenotablesuccessofdeeplearningforecasters,
thevastmajorityofthemstillfollowaconventionaltrainingmechanism, trainingandpredicting
usingthesamedatasets.
Meanwhile,theriseoffoundationmodelsinnaturallanguageprocessing(NLP)andcomputervision
(CV), such as LLaMA (Touvron et al., 2023), CLIP (Radford et al., 2021) and ChatGPT, marks
1

PublishedasaconferencepaperatICLR2024
majormilestonesoneffectiverepresentationlearning. Itisextremelyintriguingtoexploreapre-
trainedpathforfoundationtimeseriesmodelswithvastamountsofdata,facilitatingperformance
improvementindownstreamtasks. Somerecentworksshedlightintothepossibilityofbuilding
general transformers for time series (Zhou et al., 2023; Sun et al., 2023; Goswami et al., 2024;
Dasetal.,2023b;Rasuletal.,2023). However,thetheoreticalandpracticalunderstandingofsuch
modelshasnotreachedtheconsensusobservedinotherdomainswheregenerativemodelshavebeen
widelyacknowledged(Garza&Mergenthaler-Canseco,2023). Inaddition,promptingtechniquesin
LLM(suchasInstructGPT(Ouyangetal.,2022))provideawaytoleveragethemodel’sexisting
representationsduringpre-traininginsteadofrequiringlearningfromscratch. However,existing
backbonestructuresandprompttechniquesinlanguagemodelsdonotfullycapturetheevolutionof
temporalpatternsasinN-BEATS(Oreshkinetal.,2019)andAutoFormer(Wuetal.,2021),which
arefundamentalfortimeseriesmodeling.
Inthispaper,wemakeanattempttoaddressthetimelychallengesofadaptinglargepre-trainedmodels
fortimeseriesforecastingtasksanddevelopingaprompt-basedgenerativepre-trainingtransformer
fortimeseries,namelyTEMPO.TEMPOconsistsoftwokeyanalyticalcomponentsforeffectivetime
seriesrepresentationlearning: onefocusesonmodelingspecifictimeseriespatterns,suchastrends
andseasonality,andtheotherconcentratesonobtainingmoreuniversalandtransferrableinsights
fromtheinherentpropertiesofdatathroughaprompt-basedapproach. Specifically,TEMPOfirstly
decomposestimeseriesinputintothreeadditivecomponents,i.e.,trend,seasonality,andresiduals
vialocallyweightedscatterplotsmoothing(Clevelandetal.,1990). Eachofthesetemporalinputsis
subsequentlymappedtoitscorrespondinghiddenspacetoconstructthetimeseriesinputembedding
ofthegenerativepre-trainedtransformer(GPT).Weconductaformalanalysis,bridgingthetime
seriesdomainwiththefrequencydomain,tohighlightthenecessityofdecomposingsuchcomponents
fortimeseriesanalysis. Inaddition,wetheoreticallyrevealthattheattentionmechanismishard
toachievethedecompositionautomatically. Second,TEMPOutilizesasoftprompttoefficiently
tunetheGPT (Radfordetal.,2019)forforecastingtasksbyguidingthereuseofacollectionof
learnablecontinuousvectorrepresentationsthatencodetemporalknowledgeoftrendandseasonality.
Inaddition,weleveragethethreekeyadditivecomponentsoftimeseriesdata—trend,seasonality,
andresiduals—toprovideaninterpretableframeworkforcomprehendingtheinteractionsamong
inputcomponents(Hastie,2017). Experimentresultsonzeroshotsettingandmultimodalsettingof
TEMPOpavethepathtofoundationalmodelsfortimeseries. Besides,wedemonstratethestable
predictivepowerofourmodelonunseensampleswithtextualinformationontwomultimodaldatasets
includingTETS(TextforTimeSeries)dataset,whichisfirstintroducedinthisworktofosterfurther
researchtopicsofpre-trainedtimeseriesmodels.
Insummary,themaincontributionsofourpaperinclude: (1)Weintroduceaninterpretableprompt-
tuning-based generative transformer, TEMPO, for time series representation learning. It further
drives a paradigm shift in time series forecasting - from conventional deep learning methods to
pre-trainedfoundationalmodels. (2)Weadaptpre-trainedmodelsfortimeseriesbyfocusingon
two fundamental inductive biases: First, we utilize decomposed trend, seasonality, and residual
information. Second, we explore the soft prompt strategies to accommodate time series data’s
dynamicnature. (3)Throughextensiveexperimentationonbenchmarkdatasetsandtwomultimodal
datasets,ourmodeldemonstratessuperiorperformance.Notably,ourrobustresultstowardshighlights
thepotentialoffoundationalmodelsintherealmoftimeseriesforecasting.
2 RELATED WORKS
Pre-trainedLargeLanguageModelsforTimeSeries. TherecentdevelopmentofLargeLanguage
Models (LLMs) has opened up new possibilities for time-series modeling. LLMs, such as T5
(Raffeletal.,2020),GPT(Radfordetal.,2018),GPT-2(Radfordetal.,2019),GPT-3(Brownetal.,
2020),GPT-4(OpenAI,2023),LLaMA(Touvronetal.,2023),havedemonstratedastrongabilityto
understandcomplexdependenciesofheterogeneoustextualdataandprovidereasonablegenerations.
Recently,thereisgrowinginterestinapplyinglanguagemodelstotimeseriestasks(Jinetal.,2024a;
Gruveretal.,2024). Forexample,Xue&Salimnaivelyconverttimeseriesdatatotextsequence
inputsandachievesencouragingresults. Sunetal. proposetextprototype-alignedembeddingto
enableLLMstohandletimeseriesdata. Inaddition,Yuetal. presentaninnovativeapproachtowards
leveragingLLMsforexplainablefinancialtimeseriesforecasting. Theworksin(Zhouetal.,2023)
and(Changetal.,2023)arethemostrelevantonestoourwork,astheybothintroduceapproachesfor
2

PublishedasaconferencepaperatICLR2024
Prompt Module

Add & Norm
|     |                            |              |  ...Trend ...   | Val |                      | Attention   |          |     |
| --- | -------------------------- | ------------ | --------------- | --- | -------------------- | ----------- | -------- | --- |
|     | Trainable Blocks           |              | ...Seasonal ... | Val | Feed Forward Layer   |             |          |     |
|     |                            |              |                 |     |                      | Q           | K V      |     |
|     | Frozen Blocks              |              | ...Residual ... | Val | 6 x Add & Norm       |             |          |     |
|     |                            |              |                 |     |                      | L o RA      | L o R A  |     |
|     | Pr e -t ra in e d  P a r a | m et e r s
 |                 |     | Multi-head Attention |             |          |     |
|     | f ro m  G e n e ra t i v   | e P r e -    |                 |     |                      | Hi d d en S | t a t es |     |
trained Transformer
Prompt
|     |       | Normalize |          | Embedding |             |        |              |     |
| --- | ----- | --------- | -------- | --------- | ----------- | ------ | ------------ | --- |
|     |       |           |          |           | Tra n s f o | r mer  | De-Normalize |     |
|     | Trend |           | Patching |           | B l o c     | k s    |              |     |
Prompt
|                   |          | Normalize |          | Embedding |     |     | De-Normalize | Prediction |
| ----------------- | -------- | --------- | -------- | --------- | --- | --- | ------------ | ---------- |
| time series input | Seasonal |           | Patching |           |     |     |              |            |
Positional
Embedding
Prompt
De-Normalize
|     |          | Normalize |          | Embedding |     |     |     |     |
| --- | -------- | --------- | -------- | --------- | --- | --- | --- | --- |
|     | Residual |           | Patching |           |     |     |     |     |
Linear Output Layer
Figure1:ThearchitectureofproposedTEMPO-GPT.ThetrendX ,seasonalX andresidualX components
|     |     |     |     |     |     | T S | R   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
aretreatedasdifferentsemanticinductivebiasestofeedintothepre-trainedtransformer.
time-seriesanalysisbystrategicallyleveragingandfine-tuningLLMs. However,thesestudiesdirectly
employ time series data to construct embeddings, without adequately capturing the inherent and
unqiuecharacteristicsoftimeseriesdatawhichischallengingtodecouplesuchinformationwithin
theLLMs(Shinetal.,2020). Inaddition,thereisstillverylimitedworkonLLMformultimodal
datawithtimeseries. METS(Lietal.,2023)isoneoftheearlyworkspursuingthisdirection. While
theexperimentresultsareencouraging,itisdifficulttoextendMETStoothermodalitiessincethe
embeddingalignmentbetweentimeseriesandtextsarespecific. Pleaserefertothesuverypapers
(Jinetal.,2023;2024b)forfurtherreferencesoftimeseriesmeetingLLMs.
Prompttuning. Prompttuningisanefficient,low-costwayofadaptingapre-trainedfoundation
modeltonewdownstreamtaskswhichhasbeenadaptedtodownstreamtasksacrossvariousdomains.
InNLPdomain,softpromptswithtrainablerepresentationareusedthroughprompt-tuning(Lester
etal.,2021)orprefix-tuning(Li&Liang,2021).PromptingtechniqueshavealsobeenextendedtoCV
taskslikeobjectdetection(Lietal.,2022)andimagecaptioning(Zhangetal.,2022a),etcandother
domainssuchasmisinformation(Zhangetal.,2024). Multimodalworks,suchasCLIP(Radford
etal.,2021),usetextualpromptstoperformimageclassificationandachieveSOTAperformance. In
addition,L2P(Wangetal.,2022b)demonstratesthepotentialoflearnablepromptsstoredinashared
pool to enable continual learning without rehearsal buffer, and Dualprompt (Wang et al., 2022a)
introduces a dual-space prompt architecture, maintaining separate prompt encodings for general
knowledgeandexpertinformation,etc. Ourresearchbuildsupontheseconceptsbyexploringthe
useofpromptdesignfromindicativebiasspecificallyfortemporalreasoningandknowledgesharing
acrosstimeseriesforecastingproblems.
3 METHODOLOGY
Inourwork,weadoptahybridapproachthatincorporatestherobustnessofstatisticaltimeseries
analysiswiththeadaptabilityofdata-drivenmethods. AsshowninFigure1,weproposeanovel
integrationofseasonalandtrenddecompositionfromSTL(Clevelandetal.,1990)intothepre-trained
transformers. Thisstrategyallowsustoexploittheuniquestrengthsofbothstatisticalandmachine
learningmethods,enhancingourmodel’scapacitytohandletimeseriesdataefficiently. Moreover,a
semi-softpromptingapproachisintroducedtoenhancetheadaptabilityofpre-trainedmodelsfor
handlingtimeseriesdata. Thisinnovativeapproachenablesthemodelstomergetheirextensive
learnedknowledgewiththeuniquerequirementsintrinsictotimeseriesanalysis.
3.1 PROBLEMDEFINITION
GivenobservedvaluesofpreviousK timestamps,thetaskofmultivariatetime-seriesforecasting
| aimstopredictthevaluesforthenextH |     |     |             | timestamps. | Thatis, |        |     |     |
| --------------------------------- | --- | --- | ----------- | ----------- | ------- | ------ | --- | --- |
|                                   |     |     | xˆi,...,xˆi | =F(xi       | ,...,xi | ;Vi;Φ) |     | (1) |
|                                   |     |     | t t+H−1     |             | t−K     | t−1    |     |     |
3

PublishedasaconferencepaperatICLR2024
wherexˆi,...,xˆi isthevectorofH-stepestimationfromtimestamptofchannelicorresponding
|     | t t+H−1 |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
tothei-thfeature. Giventhehistoricalvaluesxi ,...,xi ,itcanbeinferredbymodelF with
|     |     |     |     |     | t−K | t−1 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
parameter Φ and prompt Vi. In anticipation of the foundational model’s strong generalization
capabilitiesacrossunseendatasets,wedefaulttoazero-shotlearningconfigurationintheabsenceof
specificindications. Thisapproachentailsthatthemodelisnotprivytothetargetdataset’shistory
valueandhorizonvalueduringthetrainingprocess.
3.2 TIMESERIESINPUTREPRESENTATION
Fortimeseriesdata,representingthecomplexinputbydecomposingitintomeaningfulcomponents,
suchastrendandseasoncomponents,canhelpextractinformationoptimally. Inthispaper,given
theinputX ∈Rn×L,wherenisthefeature(channel)sizeandLitthelengthofthetimeseries,the
additiveSTLdecomposition(Clevelandetal.,1990)canberepresentedas:
|     |     |     |     | Xi =Xi | +Xi | +Xi. |     |     | (2) |
| --- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- |
|     |     |     |     |        | T   | S R  |     |     |     |
Here,iisthechannelindex(correspondingtoacertaincovariate)formultivariatetimeseriesinput,
and the trend X ∈ Rn×L = 1 (cid:80)k X captures the underlying long-term pattern in the
|     |     | T   |     | j=−k | t+j |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
m
data,wherem = 2k+1andk istheaveragingstepsize. TheseasonalcomponentX ∈ Rn×L
S
encapsulates the repeating short-term cycles, which can be estimated after removing the trend
|     |     |     |     | X   | ∈ Rn×L |     |     |     |     |
| --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
component. The residual component R represents the remainder of the data after the
trendandseasonalityhavebeenextracted. Notethat,inpractice,itissuggestedtoleverageasmuch
information as possible to achieve a more precise decomposition. However, in consideration of
computational efficiency, we opt not to use the STL decomposition on the largest possible data
windowoneachinstance. Instead,weperformlocaldecompositionwithineachinstanceusingafixed
windowsize. InspiredbyN-BEATs(Oreshkinetal.,2019),weintroducelearnableparametersfor
estimatingthevariouslocaldecompositioncomponents. Samefortheothers. Thisprincipleapplies
toothercomponentsofthemodelaswell. InAppendixG,weestablishaconnectionbetweentime
seriesforecastingandfrequencydomainprediction,whereourfindingsindicatethatdecomposition
significantlysimplifiesthepredictionprocess. Notethatsuchdecompositionisofmoreimportance
incurrenttransformer-basedmethodsastheattentionmechanism,intheory,maynotdisentanglethe
disorthogonaltrendandseasonsignalsautomatically:
Theorem3.1 SupposethatwehavetimeseriessignalX = X +X +X ,t ∈ [t ,t ]. Let
|     |     |     |     |     |     |     | Tt St | Rt  | 1 n |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
E ={e ,e ,...,e }denoteasetoforthogonalbases. LetE ⊆E denotethesubsetofE onwhich
|     | 1 2 | n   |     |     |     |     | S   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X has non-zero eigenvalues and E ⊆ E denote the subset of E on which X has non-zero
| St  |     |     |     | T   |     |     |     | Tt  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
eigenvalues. IfX andX arenotorthogonal,i.e. (cid:80)n Xi Xi ̸=0,thenE ∩E ̸=∅,i.e. E
|     |     | St  | Tt  |     |     | i=1 | Tt St | T   | S   |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
cannotdisentanglethetwosignalsontotwodisjointsetsofbases.
TheproofcanbefoundinAppendixG.Theorem 3.1statesthatiftrendandseasonalcomponents
of a time series are non-orthogonal, they cannot be fully disentangled and separated by any set
oforthogonalbases. Accordingto (Zhouetal.,2023),theself-attentionlayernaturallylearnsan
orthogonaltransformation,akintoPCA’sdecompositionintoorthogonalprincipalcomponents. Thus,
applyingattentiondirectlytoarawtimeserieswouldbeineffectiveatdisentanglingnon-orthogonal
trendandseasonalcomponents. Fortheremainderofthemethodologysection,wewillutilizethe
trendcomponentX astheexemplarycase. Wefirstapplyreverseinstancenormalization(Kimetal.,
T
2022)oneachglobalcomponentandlocalinputrespectivelytofacilitateknowledgetransferand
minimizelossesintroducedbydistributionshifts. Thatis,foreachsamplex fromX ’s-thchannel
|     |     |          |     |           |     |          |     | Tt T |                 |
| --- | --- | -------- | --- | --------- | --- | -------- | --- | ---- | --------------- |
|     |     | (cid:16) |     | (cid:112) |     | (cid:17) |     |      | (cid:2) (cid:3) |
oftimet,xˆ = γ x −E [x ]/ Var[x ]+ϵ +β ,whereE [x ]andVar xi are
|     | Tt  | T Tt | t   | Tt  | Tt  | T   | T   | t Tt | Tt  |
| --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- |
theinstance-specificmeanandstandarddeviation;γ andβ aretrainableaffineparametervectors
|     |     |     |     |     |     | T   | T   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
for trend component. In addition, we implement a mean square error (MSE) reconstruction loss
functiontoensurethatthelocaldecompositionalignswiththeglobalSTLdecompositionobserved
inthetrainingdata. Thedecompositionlossfunction,denotedasL =f (X,θ )−Xˆg,where
|     |     |     |     |     |     |     | Dec | T T | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f isthefunctionwithlearnablevariablesθ formappinglocaldecompositiontobealignedwith
| T   |     |     |     |     | T   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theglobaldecompositionafternormalizationXˆg.
|     |     |     |     |     |     | Then,following | (Nieetal.,2023),wecombine |     |     |
| --- | --- | --- | --- | --- | --- | -------------- | ------------------------- | --- | --- |
T
time-series patching with temporal encoding to extract local semantics by aggregating adjacent
time steps into tokens, significantly increasing the historical horizon while reducing redundancy.
Specifically,wegetthepatchedtokenforthei-thnormalizedtrendcomponentforf (Xi,θ )with
|     |     |     |     |     |     |     |     | T   | T   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4

PublishedasaconferencepaperatICLR2024
(cid:106) (cid:107)
P
T
i ∈RLP×N,whereL
P
isthepatchlength,N = (L−
S
LP) +2isthenumberofpatchesandS is
thestride. WegetpatchedtokensPi andPi inthesameway. Then,wefeedthepatchedtimeseries
S R
tokenstotheembeddinglayerf togettherepresentationPi =f(Pi)∈RP×LE forthelanguage
T T
modelarchitecturetotransferitslanguagecapabilitiestothenovelsequentialmodalityeffectively,
whereL istheembeddingsize.
E
3.3 PROMPTDESIGN
Promptingtechniqueshavedemonstratedremarkableeffectivenessacrossawiderangeofapplications
byleveragingthepoweroftask-specificknowledgeencodedwithincarefullycraftedprompts. This
successcanbeattributedtotheprompts’abilitytoprovideastructuredframeworkthatalignsthe
model’soutputswiththedesiredobjectives,resultinginenhancedaccuracy,coherence,andoverall
qualityofthegeneratedcontent. Previousworksmostlyfocusonutilizingafixedprompttoboostthe
pre-trainedmodels’performancethroughfine-tuning(Brownetal.,2020). Inpursuitofleveraging
the rich semantic information encapsulated within various time series components, our research
introducesasemi-softpromptingstrategy. Thisapproachinvolvesthegenerationofdistinctprompts
correspondingtoeachprimarytimeseriescomponent: trend,seasonality,andresiduals. ‘Predict
thefuturetimestepgiventhe[trend,season,residual]’servesasthetemplatefromwhichwederive
ourcomponent-specificprompts. Thesearesubsequentlyconcatenatedwiththerelevantcomponent
data,therebyenablingamorerefinedmodelingapproachthatacknowledgesthemultifacetednature
oftimeseriesdata. Specifically,commencebytranslatingthetrend-specificpromptsintotheword
embeddingspace,followedbyalineartransformationtoderivethelearnabletrendpromptvectorV .
t
Thisso-called‘semi-soft’promptdesignthusstrikesabalancebetweentheinterpretabilityandinitial
guidanceofa‘hard’promptandtheadaptabilityofa‘soft’prompt. Thecombinedembeddingofthis
promptwiththetimeseriesrepresentationisencapsulatedby:
x =[V ;P ] (3)
T t T
Here, x denotes the aggregation of embeddings along the temporal axis. This concatenation
T
procedureismirroredfortheseasonalityandresidualcomponents,yieldingx andx ,respectively.
S R
Thisframeworkallowsforaninstancetobeassociatedwithspecificpromptsastheinductivebias,
jointly encoding critical information relevant to the forecasting task, such as recurring patterns,
overarchingtrends,andinherentseasonalityeffects. Itisofnotethatourpromptdesignmaintainsa
highdegreeofadaptability,ensuringcompatibilitywithabroadspectrumoftimeseriesanalyses. In
particular,similarwith (Wangetal.,2022a),weintroducepromptpoolasanextensionofourdesign
ofsoftpromptinAppendix D,aimedataccommodatingthecharacteristicallynon-stationarynature
ofreal-worldtimeseriesdataandtheassociateddistributionalshifts(Huangetal.,2020;Fanetal.,
2023). Thisadaptabilityunderscoresthepotentialofourpromptingstrategytoevolveincongruence
withthecomplexitiespresentedbydiversetimeseriesdatasets.
3.4 GENERATIVEPRE-TRAINEDTRANSFORMERARCHITECTURE
Weusethedecoder-basedgenerativepre-trainedtransformer(GPT)asthebackbonetobuildthe
basis for the time-series representations. To utilize the decomposed semantic information in a
data-efficientway,wechoosetoconcatenatethepromptanddifferentcomponentstogetherandput
themintotheGPTblock. Specifically,theinputofourtimeseriesembeddingcanbeformulated
as: x = x ⊕x ⊕x ,where⊕correspondstoconcatenateoperationandx canbetreatedas
T S R ∗
differentsentences. Notethat, anotheralternativewayistobuildseparateGPTblockstohandle
differenttypesoftimeseriescomponents. InsidetheGPTblock,weadoptthestrategyusedin(Zhou
etal.,2023)andopttoupdatethegradientsofthepositionembeddinglayerandlayernormalization
layers. Inaddition,weemployLORA(Low-RankAdaptation)(Huetal.,2021)toadapttovarying
timeseriesdistributionsefficientlyasitperformsadaptationwithsignificantlyfewerparameters.
Theoverallforecastingresultshouldbeanadditivecombinationoftheindividualcomponentpre-
dictions. Finally,theoutputsZ ofnfeaturesfromtheGPTblockcanbesplitintoZ ,Z ,Z ∈
T S R
Rn×P×LE (output corresponding to trend, seasonality, and residual) based on their positions in
theinputorder. EachZ componentisthenfedintofullyconnectedlayerstogeneratepredictions
Y
∗
∈Rn×LH,whereL
H
isthepredictionlength. Theforecastresultscanbeformulatedasfollows:
Yˆ =Yˆ +Yˆ +Yˆ . Afterthat,wede-normalizeY accordingtothecorrespondingstatisticsusedin
T S R
5

PublishedasaconferencepaperatICLR2024
thenormalizationstep: Yˆ t i = (cid:113) Var (cid:2) xi t (cid:3) +ϵ· (cid:16) Y t i γ −β (cid:17) +E t (cid:2) xi t (cid:3) . Byrecombiningtheseadditive
elements,ourapproachaimstoreconstructthefulltemporaltrajectorymostrepresentativeofthe
underlyingdynamicsacrossvariedtimescalescapturedbythedecomposedinputrepresentation.
Inordertoachieveinterpretability,weexplorebothlinearandnonlinearinteractionsamongtrend,
seasonal,andresidualcomponentsintheircontributiontothefinaloutput. Thereforeweconstructan
interpretablegeneralizedadditivemodel(GAM)(Hastie,2017)basedonGPT’soutputtolearnhow
(cid:80) (cid:80)
thethreecomponentsinteractwitheachother,whichis: g(Y)=F + F (x )+ F (x ),
∅ i i i t It It
whereF isanormalizingconstant, thefootnoteicorrespondstothetrend, season, andresidual
∅
component. {I }isofasetofmultipleinteractcomponents. Then,wecancalculatethefirst-order
t
sensitivityindex (Sobol’,1990)orSHAP(SHapleyAdditiveexPlanations)value(Lundberg&Lee,
2017)tomeasurethesensitivityofeachcomponent.
4 EXPERIMENTS
Ourexperimentsareconductedusingwidely-recognizedtimeseriesbenchmarkdatasets,suchas
thosedetailedin(Zhouetal.,2021),alongsidetheGDELTdataset(Jiaetal.,2024)andourproposed
TETSdataset. Thesecomprehensivedatasetsencompassadiversearrayofdomains,including,but
notlimitedto,electricity(ETTh1,ETTh2,ETTm1,ETTm2,Electricity),traffic(Traffic),climate
(Weather),news(GDELT),andfinance(TETS),withdatasamplingfrequenciesrangingfromminutes,
hours to days and quarters. The inclusion of such varied datasets ensures a thorough evaluation
of our experimental setups across multiple dimensions of time series data. Due to the absence
of a standard test split for zero-shot comparison, we adopt a uniform training methodology to
ensurefairperformanceassessmentacrossdatasetsunseenduringmodeltraining. Specifically,to
advancetheparadigmoffoundationmodelswithinthedomainoftransferlearning,weinvestigate
azero-shotsettingforourexperiments,whichisthe‘many-to-one’scenario: trainingonmultiple
sourcedatasetsfollowedbyzero-shotforecastingonadistinct,unseentargetdataset. Forinstance,
whenevaluatingperformanceona‘weather’dataset,ourmodelispre-trainedondiversedatasets
including‘ETTm1,ETTm2,ETTh1,ETTh2,Electricity,andTraffic’withoutexposuretothetarget
weatherdata. This’many-to-one’approachdiffersfundamentallyfrom‘one-to-one’or‘one-to-many’
configurations(Zhangetal.,2022c)byusingdiversepre-trainingdatasetsfromvarieddomains,like
trafficandweatherdata. Thisdiversity,whilerich,introducescomplexity,asthemodelmustidentify
patternsacrosspotentiallymisalignedsamples,complicatinglearningcomparedtomodelstrained
andtestedonindistributiondatasets.
WeuseGPT-2(Radfordetal.,2019)asourbackbonetobuildTEMPO1 asshowninFigure1. To
comprehensivelydemonstratetheperformanceofourmodel,wecompareTEMPO withthefollowing
baselinesoverlong-termforecastingandshort-termforecasting: (1)Thepre-trainedLLM-based
models,includingBert(Devlinetal.,2019),GPT2(Radfordetal.,2019;Zhouetal.,2023),T5(Raffel
etal.,2020),andLLaMA(Touvronetal.,2023). (2)TheTransformer-basedmodels,includingthe
PatchTST (Nie et al., 2023), FEDformer (Zhou et al., 2022), ETSformer (Woo et al., 2022) and
Informer(Zhouetal.,2021). (3)ThevariantofLinear-basedmodels,DLinear(Zengetal.,2023)
model.(4)General2D-variationmodel,TimesNet(Wuetal.,2023).Followingtraditionalforecasting
works,wereporttheMeanSquaredError(MSE)andMeanAbsoluteError(MAE)resultsinthis
section. PleaserefertotheAppendixBandFforthedetailedexperimentsettingandbaselines.
4.1 ZEROSHOTLONG-TERMFORECASTINGRESULTS
Table 1presentstheperformanceofmultipletimeseriesforecastingmodelsonMSEandMAEmetrics
acrossdifferentpredictionlengthsunderthe‘many-to-one’setting,withlowerscoresindicatingmore
accurateforecasts. Ourproposedmodel,TEMPO,surpassedexistingbaselinesonaverageoverall
predictionhorizonsacrossalldatasets,highlightingthebroadapplicabilityofTEMPO.Ourmodel
achievesthehighestaverageperformancescores. Specifically,itimprovestheweatherandETTm1
datasetsbyaround6.5%and19.1%,respectivelyinMAEcomparedtothepreviousstate-of-the-art
model,PatchTST.Italsosecuresthelowesterrorratesacrossnumerousindividualdataset-prediction
lengthconfigurations. Comparedtootherpre-trainedmodelsforforecasting,TEMPO consistently
deliversthebestresultsacrossdifferenttimeseriesdatasets. Theseresultssuggestthatincorporating
1TEMPO’ssourcecodecanbefoundat:https://github.com/DC-research/TEMPO
6

PublishedasaconferencepaperatICLR2024
Table1: Transferlearningoflong-termforecastingresultsontimeseriesbenchmarkdatasets. Weuse
predictionlengthO ∈{96,192,336,720}.
|     |     |     | AlowerMSEindicatesbetterperformance. |     |     |     | Hereafter, |
| --- | --- | --- | ------------------------------------ | --- | --- | --- | ---------- |
forthetables,thebestresultsaremarkedinboldandthesecondoptimalinunderlined,respectively
withMSE/MAE.
|     | ECL | Traffic | Weather | Ettm1 | Ettm2 | Etth1 | Etth2 |
| --- | --- | ------- | ------- | ----- | ----- | ----- | ----- |
Horizon Model
|          | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     |
| -------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| TEMPO    | 0.178/0.276 | 0.476/0.343 | 0.211/0.254 | 0.438/0.424 | 0.185/0.267 | 0.400/0.406 | 0.301/0.353 |
| GPT2     | 0.193/0.288 | 0.522/0.380 | 0.226/0.274 | 0.486/0.438 | 0.193/0.273 | 0.400/0.416 | 0.320/0.363 |
| T5       | 0.185/0.282 | 0.508/0.366 | 0.217/0.271 | 0.529/0.464 | 0.190/0.268 | 0.400/0.409 | 0.328/0.366 |
| PatchTST | 0.489/0.546 | 1.023/0.641 | 0.247/0.301 | 0.733/0.554 | 0.273/0.345 | 0.57/0.518  | 0.379/0.412 |
96 Timesnet 0.293/0.369 0.585/0.401 0.247/0.295 0.518/0.470 0.202/0.290 0.407/0.423 0.315/0.362
| FEDformer | 0.300/0.399 | 0.835/0.564 | 0.292/0.346 | 0.698/0.553 | 0.665/0.634 | 0.509/0.502 | 0.385/0.426 |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.707/0.638 | 1.419/0.795 | 0.453/0.416 | 1.117/0.678 | 0.353/0.404 | 0.469/0.457 | 0.405/0.428 |
| Informer  | 0.512/0.531 | 1.400/0.830 | 0.837/0.711 | 0.880/0.657 | 0.263/0.360 | 0.642/0.562 | 0.704/0.651 |
| DLinear   | 0.195/0.292 | 0.609/0.424 | 0.212/0.275 | 0.624/0.522 | 0.264/0.352 | 0.414/0.421 | 0.334/0.389 |
| TEMPO     | 0.198/0.293 | 0.496/0.355 | 0.254/0.298 | 0.461/0.432 | 0.243/0.304 | 0.426/0.421 | 0.355/0.389 |
| GPT2      | 0.207/0.300 | 0.533/0.387 | 0.273/0.312 | 0.516/0.461 | 0.254/0.312 | 0.441/0.433 | 0.381/0.402 |
| T5        | 0.205/0.302 | 0.524/0.374 | 0.277/0.321 | 0.523/0.454 | 0.246/0.306 | 0.428/0.426 | 0.413/0.410 |
| PatchTST  | 0.465/0.535 | 0.992/0.633 | 0.277/0.324 | 0.739/0.563 | 0.299/0.355 | 0.580/0.528 | 0.387/0.417 |
192 Timesnet 0.283/0.366 0.64/0.431 0.316/0.342 0.55/0.490 0.261/0.318 0.439/0.439 0.394/0.406
| FEDformer | 0.390/0.468 | 0.869/0.579 | 0.372/0.426 | 0.819/0.608 | 0.358/0.416 | 0.683/0.596 | 0.921/0.748 |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.721/0.645 | 0.995/0.658 | 0.545/0.466 | 1.598/0.803 | 0.390/0.416 | 0.548/0.503 | 0.476/0.468 |
| Informer  | 0.625/0.619 | 0.872/0.506 | 0.431/0.455 | 1.461/0.892 | 0.494/0.516 | 0.798/0.632 | 0.455/0.883 |
| DLinear   | 0.204/0.300 | 0.595/0.412 | 0.259/0.308 | 0.599/0.511 | 0.292/0.365 | 0.439/0.437 | 0.381/0.415 |
| TEMPO     | 0.209/0.309 | 0.503/0.356 | 0.292/0.332 | 0.515/0.467 | 0.309/0.345 | 0.441/0.430 | 0.379/0.408 |
| GPT2      | 0.231/0.324 | 0.566/0.421 | 0.441/0.379 | 0.571/0.502 | 0.315/0.35  | 0.449/0.440 | 0.394/0.416 |
| T5        | 0.229/0.321 | 0.550/0.391 | 0.330/0.330 | 0.572/0.504 | 0.316/0.346 | 0.442/0.438 | 0.416/0.427 |
| PatchTST  | 0.531/0.569 | 0.987/0.626 | 0.317/0.347 | 0.755/0.576 | 0.342/0.382 | 0.677/0.573 | 0.386/0.425 |
336 Timesnet 0.733/0.633 1.609/0.864 0.359/0.372 0.638/0.532 0.38/0.392 0.555/0.503 0.384/0.413
| FEDformer | 0.317/0.406 | 1.006/0.640 | 0.639/0.600 | 0.785/0.624 | 0.372/0.424 | 0.582/0.542 | -/5.755     |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.862/0.707 | 0.940/0.621 | 0.487/0.444 | 1.154/0.682 | 0.409/0.428 | 0.728/0.585 | 0.446/0.451 |
| Informer  | 1.222/0.863 | 0.978/0.507 | 0.370/0.412 | 0.949/0.631 | 0.788/0.622 | 1.125/0.810 | 1.389/0.848 |
| DLinear   | 0.231/0.325 | 0.624/0.427 | 0.304/0.342 | 0.622/0.534 | 0.361/0.411 | 0.463/0.464 | 0.471/0.482 |
| TEMPO     | 0.279/0.355 | 0.538/0.376 | 0.370/0.379 | 0.591/0.509 | 0.386/0.395 | 0.443/0.451 | 0.409/0.440 |
| GPT2      | 0.262/0.347 | 0.596/0.399 | 0.484/0.422 | 0.646/0.54  | 0.394/0.397 | 0.445/0.454 | 0.434/0.448 |
| T5        | 0.266/0.351 | 0.578/0.404 | 0.528/0.451 | 0.694/0.568 | 0.394/0.397 | 0.443/0.458 | 0.425/0.440 |
| PatchTST  | 0.475/0.532 | 1.152/0.706 | 0.375/0.388 | 0.739/0.57  | 0.421/0.421 | 0.540/0.521 | 0.425/0.448 |
720 Timesnet 1.166/0.859 1.974/0.971 0.423/0.405 0.723/0.577 0.399/0.409 0.438/0.461 0.394/0.431
| FEDformer | 0.423/0.48  | 0.965/0.652 | 0.409/0.425 | 0.816/0.614 | 0.455/0.462 | 0.688/0.618 | 0.427/0.452 |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.666/0.640 | 0.798/0.518 | 0.592/0.506 | 1.038/0.665 | 0.444/0.438 | 0.615/0.561 | 0.446/0.466 |
| Informer  | 0.881/0.778 | 1.532/0.800 | 1.133/0.842 | 0.779/0.616 | 1.075/0.725 | 0.836/0.687 | 1.330/0.866 |
| DLinear   | 0.259/0.352 | 0.623/0.42  | 0.363/0.389 | 0.639/0.559 | 0.515/0.490 | 0.467/0.481 | 0.639/0.559 |
| TEMPO     | 0.216/0.308 | 0.503/0.358 | 0.282/0.316 | 0.501/0.458 | 0.280/0.328 | 0.428/0.427 | 0.361/0.398 |
| GPT2      | 0.223/0.315 | 0.554/0.397 | 0.356/0.347 | 0.555/0.485 | 0.289/0.333 | 0.436/0.436 | 0.382/0.407 |
| T5        | 0.221/0.314 | 0.540/0.384 | 0.338/0.343 | 0.58/0.498  | 0.287/0.329 | 0.428/0.433 | 0.396/0.411 |
| PatchTST  | 0.49/0.545  | 1.039/0.652 | 0.304/0.340 | 0.741/0.566 | 0.334/0.376 | 0.592/0.535 | 0.394/0.425 |
Avg Timesnet 0.619/0.557 1.202/0.667 0.336/0.354 0.607/0.517 0.311/0.352 0.460/0.457 0.372/0.403
| FEDformer | 0.358/0.439 | 0.919/0.609 | 0.428/0.449 | 0.780/0.600 | 0.463/0.484 | 0.616/0.565 | -/1.845     |
| --------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| ETSformer | 0.750/0.664 | 1.038/0.648 | 0.519/0.458 | 1.227/0.707 | 0.399/0.422 | 0.590/0.527 | 0.443/0.453 |
| Informer  | 0.810/0.698 | 1.196/0.661 | 0.693/0.605 | 1.017/0.699 | 0.655/0.556 | 0.850/0.673 | 0.970/0.812 |
| DLinear   | 0.222/0.317 | 0.613/0.421 | 0.284/0.329 | 0.621/0.531 | 0.358/0.405 | 0.446/0.451 | 0.456/0.461 |
LLMwiththewell-designedpromptandimplementingtimeseriesdecompositioncancontribute
significantlytoenhancingtheaccuracyandstabilityofzero-shottimeseriesforecasting.
4.2 SHORT-TERMFORECASTINGWITHCONTEXTUALINFORMATION
Datasetandmetrics. Inthissection,weintroduceTETS,anewbenchmarkdatasetbuiltuponS&P
500datasetcombiningcontextualinformationandtimeseries,tothecommunity. Following (Cao
etal.,2023),wechoosethesymmetricmeanabsolutepercentageerror(SMAPE)asourmetricin
thissection. Moreover,theGDELTisalsousedtoverifytheeffectivenesstheourproposedmethod.
PleaserefertoAppendixB.2andAppendixB.3forthedetaileddatasetsettingofTETSandGDELT;
7

PublishedasaconferencepaperatICLR2024
Table 2: SMAPE results of EBITDA from TETS and GDELT. The result of EBITDA includes
outliersremovedwhereSMAPEexceeds0.8/0.9. Thebestresultsaremarkedinboldandthesecond
optimalinunderlinedrespectivelywith0.8&0.9. (Sectors: CC:ConsumerCyclical;CD:Consumer
Defensive;Ind: Industrials;RE:RealEstate;Events: 11: Disapprove;17: Coerce;19:Fight.)
EBITDADataset
Sectors TEMPO LLaMA GPT2 Bert T5 Informer PatchTST Reformer DLinear
CC 32.27/33.48 33.13/34.31 33.77/35.37 33.42/35.33 32.65/33.83 41.12/43.17 41.44/43.18 37.23/39.09 33.53/35.65
CD 25.9/26.25 26.34/26.62 26.86/27.15 27.34/28.3 26.44/26.79 35.65/36.08 31.6/31.98 29.93/30.36 27.01/28.04
Ind 26.7/27.42 27.17/27.98 27.9/28.63 27.89/28.95 27.3/28.12 34.83/35.87 33.84/34.87 30.23/31.28 27.59/28.84
RE 29.46/30.11 29.63/30.48 30.62/31.21 30.62/31.66 30.1/30.64 36.4/37.22 37.63/38.31 31.23/31.69 29.95/30.92
GDELTDataset
11 38.77 40.23 39.03 38.89 39.04 42.00 40.45 46.72 40.14
17 41.02 42.50 41.20 41.10 41.24 44.44 42.72 48.08 42.45
19 44.03 45.49 44.17 44.09 44.29 47.45 45.49 48.30 45.40
AppendixHfortheproposedpipelineofcollectingTETSdatasetwithbothtimeseriesandtextual
information.
Contextual Information. In order to incorporate the contextual information into our proposed
TEMPO,weleveragethebuilt-intokenizationcapabilitiesofthegenerativepre-trainedtransformerto
deriveembeddingsofinputtext. Then,weutilizethesetextembeddingscorrespondingtoeachtime
seriesinstance,Text,toconstructsoftpromptswithlearnableparametersandconcatenatethematthe
beginningoftheinputembedding,thatis,x=Text⊕x ⊕x ⊕x . Wherethex forEBITDA
T S R ∗
is conducted with semi-soft prompt. This method is not strictly confined to our proposed model
butcanbefeasiblyappliedinsimilarworkstoenhancetheircapabilityofhandlingandbenefiting
fromcontextualinformation. Comparisonswithotherdesignstrategiesofcontextualinformationare
providedintheAppendixD.4forfurtherreference.
Results. Fromthetransferlearningperspective,wechoosetoreportthesettingof‘many-to-many’,
whichmeanswetrainamodelusingin-domainsectorsdataanddirectlydothezero-shottestonall
cross-domainsectors. TheSMAPEresultsofusingdifferentbaselinemodelsandourmodelonthe
TETSdatasetandGDELTdatasetarelistedinTable2whichisalsozero-shotsettingasdatasamples
fromthosesectorsarenotseenduringthetrainingstage. Examiningtheresultsacrossallsectors,our
proposedmodel,whichcombinestimeseriesdatawithsupplementarysummary(contextual)data,
outperformsallthebaselinemethodsincross-domainsectors. Besides,weobservethattransformer-
based architectures training from scratch, specifically tailored for time series analysis—such as
PatchTST,Informer,andReformer(Kitaevetal.,2020)—tendtounderperformincomparisonto
transformers pre-trained on linguistic datasets. This performance discrepancy indicates that the
parameterinitializationderivedfrompre-trainedlanguagemodelsconfersasuperiorstartingpoint
formodeloptimization. Consequently,thesepre-trainedmodelsexhibitenhancedcapabilitiesand
adaptabilitywithinzero-shotlearningcontexts. Furthermore,ininstanceswherethetimeseriesdata
exhibitsastrongcorrelationtoothermodalities,suchastextualinformation,devisinganeffective
strategytoamalgamatethesedistinctmodalitiescouldleadtoenhancedperformancegains.
5 ANALYSIS
5.1 ABLATIONSTUDY
The provided ablation study, Table 3, offers critical insights into the impact of the prompt and
decompositioncomponentsontheperformanceofourmodel. Inthistable,theMSEandMAEon
variousdatasetsarereportedforfourscenarios: theoriginalmodelconfiguration(‘TEMPO’);the
modelwithoutthepromptdesignandwithoutdecomposition,whichisthesettingof‘w/oDec’;the
modelwithoutpromptdesign(‘w/oPro’)andthemodelwithoutthedecompositionlossalignment
(’w/o Dec Loss’). Averagely, the exclusion of the prompt component leads to a deterioration in
themodel’spredictiveaccuracy,indicatingthepromptcanbeanimportantfactorinenhancingthe
model’s overall performance. The omission of decomposition loss typically results in a decline
inmodelperformance. Decompositionlossfacilitatestheuseofaricherhistoricaldataset,which
8

PublishedasaconferencepaperatICLR2024
| TEMPO | w/oDec w/oPro | w/oDecLoss |     |     |     |
| ----- | ------------- | ---------- | --- | --- | --- |
1.0
| MSE/MAE         | MSE/MAE MSE/MAE         | MSE/MAE     |     |     |     |
| --------------- | ----------------------- | ----------- | --- | --- | --- |
| 96 0.178/0.276  | 0.195/0.294 0.185/0.281 | 0.191/0.293 | 0.8 |     |     |
| 192 0.198/0.293 | 0.210/0.301 0.196/0.295 | 0.205/0.305 |     |     |     |
egatnecreP tnenopmoC
| ECL 336 0.209/0.309 | 0.237/0.328 0.225/0.318 | 0.243/0.337 | 0.6 |     |     |
| ------------------- | ----------------------- | ----------- | --- | --- | --- |
| 720 0.279/0.355     | 0.271/0.351 0.269/0.359 | 0.262/0.353 |     |     |     |
| Avg 0.216/0.308     | 0.228/0.319 0.219/0.313 | 0.225/0.322 | 0.4 |     |     |
| 96 0.438/0.424      | 0.516/0.447 0.452/0.431 | 0.428/0.425 |     |     |     |
| 192 0.461/0.432     | 0.518/0.462 0.47/0.45   | 0.494/0.463 | 0.2 |     |     |
Trend Seasonality
| Ettm1 336 0.515/0.467 | 0.622/0.515 0.519/0.474 | 0.544/0.492 | Residual |     |     |
| --------------------- | ----------------------- | ----------- | -------- | --- | --- |
Error
| 720 0.591/0.509 | 0.644/0.50 0.582/0.51 | 0.594/0.521 | 0.0 96 | 192 336 | 720 |
| --------------- | --------------------- | ----------- | ------ | ------- | --- |
Prediction Length
| Avg 0.501/0.458 | 0.575/0.481 0.506/0.466 | 0.515/0.475 |     |     |     |
| --------------- | ----------------------- | ----------- | --- | --- | --- |
Figure2:TheSHAPvaluesofdecomposedcom-
| Table3: | AblationstudyonTEMPO. |     | ponentsofTEMPOforETTm1. |     |     |
| ------- | --------------------- | --- | ----------------------- | --- | --- |
enhances the quality of individual decomposition components. This improvement in component
qualityisimportantforthemodel’sforecastingaccuracy. Notethatemployingthepromptdesign
inisolation,withoutthesupportofdecomposition,candetrimentallyimpactthebackbonemodel’s
performanceinmostcases. Thiscanbeduetothedifficultiesineffectivelypromptingtimeseries
datafromitsrawformwithlimitedsemanticinformation. Thesefindingsunderscoretheessential
natureofbothpromptanddecompositionelementsinachievingrobustforecastingcapabilitiesunder
thezero-shotsetting.
5.2 INTERPRETINGMODELPREDICTIONS
SHAP(SHapleyAdditiveexPlanations)valuesserveasacomprehensivemeasureoffeatureimpor-
tance,quantifyingtheaveragecontributionofeachfeaturetothepredictionoutputacrossallpossible
featurecombinations. AsshowninFigure2,whenappliedtoourseasonalandtrenddecomposition,
theSHAPvaluesfromthegeneralizedadditivemodel(GAM)suggestadominantinfluenceofthe
seasonalcomponentonthemodel’spredictions, implyingasignificantdependencyofthemodel
ontheoverallrecurringpatternswithinthedata. WhilethedirectionalshiftsofETTm1dataset’s
contribution is relatively stable. The escalating values in the ’Error’ column, which denote the
discrepancybetweenthemodel’spredictionsandthegroundtruth,indicateapotentialdeclinein
themodel’saccuracyasthepredictionlengthincreaseswhichisindeedobservedinmostexperi-
mentsrun. Inthiscontext,theSTLdecompositionprovesinvaluableasitenablesustoidentifyand
quantifytheindividualcontributionsofeachcomponenttotheoverallpredictions,asdemonstrated
bytheSHAPvalues. Thisdetailedunderstandingcanyieldcriticalinsightsinhowthepre-trained
transformerisinterpretingandleveragingthedecomposingpre-processingstep,therebyprovidinga
robustfoundationformodeloptimizationandenhancement. SHAPvaluesforweatherdatasetcanbe
foundatFigure14.
6 CONCLUSION
Thispaperproposesasoftpromptbasedgenerativetransformer,TEMPO,whichachievesstate-of-the-
artperformanceinzero-shottimeseriesforecasting.Weintroducethenovelintegrationofpromptsand
seasonaltrenddecompositiontogetherwithinapre-trainedTransformer-basedbackbonetoallowthe
modeltofocusonappropriatelyutilizingknowledgefromdifferenttemporalsemanticscomponents.
Moreover,wedemonstratetheeffectivenessofTEMPOwithmultimodelinput,effectivelyleveraging
contextualinformationintimeseriesforecasting. Lastly,withextensiveexperiments,wehighlight
thesuperiorityofTEMPOinaccuracy,andgeneralizability. Onepotentiallimitationworthfurther
investigationisthatsuperiorLLMswithbetternumericalreasoningcapabilitiesmightyieldbetter
results. Inaddition,theencouragingresultsofTEMPOonthezero-shotexperimentsshedlightinto
effectivefoundationalmodelsfortimeseries.
9

PublishedasaconferencepaperatICLR2024
ACKNOWLEDGEMENT
ThisworkispartiallysupportedbytheNSFAward#2125142andNSFAward#2226087.Thefunding
fromthesesourceshasbeenacornerstoneinenablingustobringourprojecttofruition. Wewould
liketoextendourthankstoYizhouZhang,JamesEnouen,QiangHuang,ChuizhengMeng,andHao
Niufortheirinvaluablediscussionsandinsightsinshapingthedirectionandexecutionofourwork.
Wearealsodeeplygratefultotheanonymousreviewersfortheirrigorousreviewprocess. Their
detailedcommentsandconstructivesuggestionshavesignificantlycontributedtotheimprovementof
thispaper. Thetimeandefforttheyinvestedinprovidingfeedbackhavebeeninvaluableandhave
greatlyassistedusinrefiningourwork.
REFERENCES
ShaojieBai,JZicoKolter,andVladlenKoltun. Anempiricalevaluationofgenericconvolutionaland
recurrentnetworksforsequencemodeling. arXivpreprintarXiv:1803.01271,2018.
TomB.Brown,BenjaminMann,NickRyder,MelanieSubbiah,JaredKaplan,PrafullaDhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel
Herbert-Voss,GretchenKrueger,T.J.Henighan,RewonChild,AdityaRamesh,DanielM.Ziegler,
JeffWu,ClemensWinter,ChristopherHesse,MarkChen,EricSigler,MateuszLitwin,ScottGray,
BenjaminChess,JackClark,ChristopherBerner,SamMcCandlish,AlecRadford,IlyaSutskever,
and Dario Amodei. Language models are few-shot learners. Advances in neural information
processingsystems,abs/2005.14165,2020.
DefuCao,YujingWang,JuanyongDuan,CeZhang,XiaZhu,ConguriHuang,YunhaiTong,Bixiong
Xu,JingBai,JieTong,etal. Spectraltemporalgraphneuralnetworkformultivariatetime-series
forecasting. Advancesinneuralinformationprocessingsystems,2021.
DefuCao,YixiangZheng,ParisaHassanzadeh,SimranLamba,XiaomoLiu,andYanLiu. Large
scalefinancialtimeseriesforecastingwithmulti-facetedmodel. InProceedingsoftheFourthACM
InternationalConferenceonAIinFinance,pp.472–480,2023.
CristianChallu, KinGOlivares, BorisNOreshkin, FedericoGarzaRamirez, MaxMergenthaler
Canseco,andArturDubrawski. Nhits: Neuralhierarchicalinterpolationfortimeseriesforecasting.
InProceedingsoftheAAAIConferenceonArtificialIntelligence,volume37,pp.6989–6997,2023.
ChingChang,Wen-ChihPeng,andTien-FuChen. Llm4ts: Two-stagefine-tuningfortime-series
forecastingwithpre-trainedllms. arXivpreprintarXiv:2308.08469,2023.
RobertBCleveland,WilliamSCleveland,JeanEMcRae,andIrmaTerpenning.Stl:Aseasonal-trend
decomposition. J.Off.Stat,6(1):3–73,1990.
AbhimanyuDas,WeihaoKong,AndrewLeach,RajatSen,andRoseYu. Long-termforecastingwith
tide: Time-seriesdenseencoder. arXivpreprintarXiv:2304.08424,2023a.
AbhimanyuDas,WeihaoKong,RajatSen,andYichenZhou. Adecoder-onlyfoundationmodelfor
time-seriesforecasting. arXivpreprintarXiv:2310.10688,2023b.
JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. BERT:pre-trainingofdeep
bidirectionaltransformersforlanguageunderstanding. InProceedingsofthe2019Conferenceof
theNorthAmericanChapteroftheAssociationforComputationalLinguistics: HumanLanguage
Technologies(NAACL-HLT),Minneapolis,MN,USA,June2-7,2019,pp.4171–4186,2019.
Vijay Ekambaram, Arindam Jati, Nam Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam.
Tsmixer: Lightweight mlp-mixer model for multivariate time series forecasting. In Proceed-
ings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD
’23, pp. 459–469, New York, NY, USA, 2023. Association for Computing Machinery. ISBN
9798400701030. doi: 10.1145/3580305.3599533. URL https://doi.org/10.1145/
3580305.3599533.
WeiFan,ShunZheng,XiaohanYi,WeiCao,YanjieFu,JiangBian,andTie-YanLiu. DEPTS:Deep
expansionlearningforperiodictimeseriesforecasting. InInternationalConferenceonLearning
Representations,2022.
10

PublishedasaconferencepaperatICLR2024
WeiFan,PengyangWang,DongkunWang,DongjieWang,YuanchunZhou,andYanjieFu. Dish-ts:
ageneralparadigmforalleviatingdistributionshiftintimeseriesforecasting. InProceedingsof
theAAAIConferenceonArtificialIntelligence,volume37,pp.7522–7529,2023.
RobertFildes,AndrewHarvey,MikeWest,andJeffHarrison. Forecasting,structuraltimeseries
modelsandthekalmanfilter. TheJournaloftheOperationalResearchSociety,42:1031,111991.
doi: 10.2307/2583225.
AzulGarzaandMaxMergenthaler-Canseco. Timegpt-1. arXivpreprintarXiv:2310.03589,2023.
Mononito Goswami, Konrad Szafer, Arjun Choudhry, Yifu Cai, Shuo Li, and Artur Dubrawski.
Moment: A family of open time-series foundation models. arXiv preprint arXiv:2402.03885,
2024.
NateGruver,MarcFinzi,ShikaiQiu,andAndrewGWilson. Largelanguagemodelsarezero-shot
timeseriesforecasters. AdvancesinNeuralInformationProcessingSystems,36,2024.
TrevorJHastie. Generalizedadditivemodels. InStatisticalmodelsinS,pp.249–307.Routledge,
2017.
EdwardJHu,YelongShen,PhillipWallis,ZeyuanAllen-Zhu,YuanzhiLi,SheanWang,LuWang,
and Weizhu Chen. Lora: Low-rank adaptation of large language models. arXiv preprint
arXiv:2106.09685,2021.
BiweiHuang,KunZhang,JijiZhang,JosephRamsey,RubenSanchez-Romero,ClarkGlymour,and
BernhardScho¨lkopf. Causaldiscoveryfromheterogeneous/nonstationarydata. TheJournalof
MachineLearningResearch,21(1):3482–3534,2020.
RobJHyndmanandYeasminKhandakar. Automatictimeseriesforecasting: theforecastpackage
forr. Journalofstatisticalsoftware,27:1–22,2008.
FurongJia,KevinWang,YixiangZheng,DefuCao,andYanLiu. Gpt4mts: Prompt-basedlarge
languagemodelformultimodaltime-seriesforecasting. InThe14thSymposiumonEducational
AdvancesinArtificialIntelligence(EAAI-24),2024.
Ming Jin, Qingsong Wen, Yuxuan Liang, Chaoli Zhang, Siqiao Xue, Xue Wang, James Zhang,
YiWang,HaifengChen,XiaoliLi,etal. Largemodelsfortimeseriesandspatio-temporaldata: A
surveyandoutlook. arXivpreprintarXiv:2310.10196,2023.
Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y. Zhang, Xiaoming Shi, Pin-Yu Chen,
YuxuanLiang,Yuan-FangLi,ShiruiPan,andQingsongWen. Time-LLM:Timeseriesforecasting
byreprogramminglargelanguagemodels. InTheTwelfthInternationalConferenceonLearning
Representations,2024a. URLhttps://openreview.net/forum?id=Unb5CVPtae.
MingJin,YifanZhang,WeiChen,KexinZhang,YuxuanLiang,BinYang,JindongWang,Shirui
Pan,andQingsongWen. Positionpaper: Whatcanlargelanguagemodelstellusabouttimeseries
analysis. arXivpreprintarXiv:2402.02713,2024b.
Taesung Kim, Jinhee Kim, Yunwon Tae, Cheonbok Park, Jang-Ho Choi, and Jaegul Choo. Re-
versibleinstancenormalizationforaccuratetime-seriesforecastingagainstdistributionshift. In
InternationalConferenceonLearningRepresentations,2022.
NikitaKitaev,LukaszKaiser,andAnselmLevskaya. Reformer: Theefficienttransformer. In8th
InternationalConferenceonLearningRepresentations(ICLR),AddisAbaba,Ethiopia,April26-30,
2020,2020.
BrianLester,RamiAl-Rfou,andNoahConstant. Thepowerofscaleforparameter-efficientprompt
tuning. arXivpreprintarXiv:2104.08691,2021.
JunLi,CheLiu,SiboCheng,RossellaArcucci,andShendaHong. Frozenlanguagemodelhelpsecg
zero-shotlearning,2023.
11

PublishedasaconferencepaperatICLR2024
LiunianHaroldLi,PengchuanZhang,HaotianZhang,JianweiYang,ChunyuanLi,YiwuZhong,
LijuanWang,LuYuan,LeiZhang,Jenq-NengHwang,etal.Groundedlanguage-imagepre-training.
InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,pp.
10965–10975,2022.
XiangLisaLiandPercyLiang. Prefix-tuning: Optimizingcontinuouspromptsforgeneration. arXiv
preprintarXiv:2101.00190,2021.
YaguangLi,RoseYu,CyrusShahabi,andYanLiu. Diffusionconvolutionalrecurrentneuralnetwork:
Data-driventrafficforecasting. InInternationalConferenceonLearningRepresentations(ICLR
’18),2018.
MinhaoLiu,AilingZeng,MuxiChen,ZhijianXu,QiuxiaLai,LingnaMa,andQiangXu. Scinet:
Timeseriesmodelingandforecastingwithsampleconvolutionandinteraction. AdvancesinNeural
InformationProcessingSystems,35:5816–5828,2022.
Shizhan Liu, Hang Yu, Cong Liao, Jianguo Li, Weiyao Lin, Alex X Liu, and Schahram Dust-
dar. Pyraformer: Low-complexitypyramidalattentionforlong-rangetimeseriesmodelingand
forecasting. InInternationalconferenceonlearningrepresentations,2021.
YongLiu,TenggeHu,HaoranZhang,HaixuWu,ShiyuWang,LintaoMa,andMingshengLong.
itransformer: Inverted transformers are effective for time series forecasting. arXiv preprint
arXiv:2310.06625,2023.
ScottMLundbergandSu-InLee. Aunifiedapproachtointerpretingmodelpredictions. Advancesin
neuralinformationprocessingsystems,30,2017.
YuqiNie,NamH.Nguyen,PhanwadeeSinthong,andJayantKalagnanam. Atimeseriesisworth
64words: Long-termforecastingwithtransformers. InInternationalConferenceonLearning
Representations(ICLR’23),2023.
OpenAI. Gpt-4technicalreport,2023.
BorisNOreshkin,DmitriCarpov,NicolasChapados,andYoshuaBengio. N-beats: Neuralbasis
expansionanalysisforinterpretabletimeseriesforecasting. arXivpreprintarXiv:1905.10437,
2019.
LongOuyang,JeffWu,XuJiang,DiogoAlmeida,CarrollL.Wainwright,PamelaMishkin,Chong
Zhang,SandhiniAgarwal,KatarinaSlama,AlexRay,JohnSchulman,JacobHilton,FraserKelton,
LukeE.Miller, MaddieSimens, AmandaAskell, PeterWelinder, PaulFrancisChristiano, Jan
Leike,andRyanJ.Lowe. Traininglanguagemodelstofollowinstructionswithhumanfeedback.
ArXiv,abs/2203.02155,2022. URLhttps://api.semanticscholar.org/CorpusID:
246426909.
AntonyPapadimitriou,UrjitkumarPatel,LisaKim,GraceBang,AzadehNematzadeh,andXiaomo
Liu. Amulti-facetedapproachtolargescalefinancialforecasting. InProceedingsoftheFirstACM
InternationalConferenceonAIinFinance,pp.1–8,2020.
Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya Sutskever, et al. Improving language
understandingbygenerativepre-training. 2018.
AlecRadford,JeffreyWu,RewonChild,DavidLuan,DarioAmodei,IlyaSutskever,etal. Language
modelsareunsupervisedmultitasklearners. OpenAIblog,1(8):9,2019.
AlecRadford, JongWookKim, ChrisHallacy, AdityaRamesh, GabrielGoh, SandhiniAgarwal,
GirishSastry,AmandaAskell,PamelaMishkin,JackClark,etal. Learningtransferablevisual
modelsfromnaturallanguagesupervision. InInternationalConferenceonMachineLearning,pp.
8748–8763.PMLR,2021.
ColinRaffel,NoamShazeer,AdamRoberts,KatherineLee,SharanNarang,MichaelMatena,Yanqi
Zhou,WeiLi,andPeterJLiu. Exploringthelimitsoftransferlearningwithaunifiedtext-to-text
transformer. TheJournalofMachineLearningResearch,21(1):5485–5551,2020.
12

PublishedasaconferencepaperatICLR2024
Kashif Rasul, Arjun Ashok, Andrew Robert Williams, Arian Khorasani, George Adamopoulos,
Rishika Bhagwatkar, Marin Bilosˇ, Hena Ghonia, Nadhir Vincent Hassen, Anderson Schnei-
der, et al. Lag-llama: Towards foundation models for time series forecasting. arXiv preprint
arXiv:2310.08278,2023.
TaylorShin,YasamanRazeghi,RobertLLoganIV,EricWallace,andSameerSingh. Autoprompt:
Elicitingknowledgefromlanguagemodelswithautomaticallygeneratedprompts. InProceedings
ofthe2020ConferenceonEmpiricalMethodsinNaturalLanguageProcessing(EMNLP),pp.
4222–4235,2020.
SimaSiami-Namini,NedaTavakoli,andAkbarSiamiNamin. Acomparisonofarimaandlstmin
forecastingtimeseries. In201817thIEEEinternationalconferenceonmachinelearningand
applications(ICMLA),pp.1394–1401.IEEE,2018.
Il’yaMeerovichSobol’. Onsensitivityestimationfornonlinearmathematicalmodels. Matematich-
eskoemodelirovanie,2(1):112–118,1990.
ChenxiSun,YaliangLi,HongyanLi,andShendaHong. Test: Textprototypealignedembeddingto
activatellm’sabilityfortimeseries. arXivpreprintarXiv:2308.08241,2023.
HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,Timothe´e
Lacroix,BaptisteRozie`re,NamanGoyal,EricHambro,FaisalAzhar,AurelienRodriguez,Armand
Joulin,EdouardGrave,andGuillaumeLample. Llama: Openandefficientfoundationlanguage
models. ArXiv, abs/2302.13971, 2023. URL https://api.semanticscholar.org/
CorpusID:257219404.
ZifengWang,ZizhaoZhang,SaynaEbrahimi,RuoxiSun,HanZhang,Chen-YuLee,XiaoqiRen,
Guolong Su, Vincent Perot, Jennifer Dy, et al. Dualprompt: Complementary prompting for
rehearsal-free continual learning. In European Conference on Computer Vision, pp. 631–648.
Springer,2022a.
ZifengWang,ZizhaoZhang,Chen-YuLee,HanZhang,RuoxiSun,XiaoqiRen,GuolongSu,Vincent
Perot,JenniferDy,andTomasPfister. Learningtopromptforcontinuallearning. InProceedings
oftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,pp.139–149,2022b.
GeraldWoo,ChenghaoLiu,DoyenSahoo,AkshatKumar,andStevenHoi. Etsformer: Exponential
smoothingtransformersfortime-seriesforecasting. arXivpreprintarXiv:2202.01381,2022.
GeraldWoo, Chenghao Liu, AkshatKumar, Caiming Xiong, Silvio Savarese, andDoyen Sahoo.
Unifiedtrainingofuniversaltimeseriesforecastingtransformers.arXivpreprintarXiv:2402.02592,
2024.
HaixuWu,JiehuiXu,JianminWang,andMingshengLong. Autoformer: Decompositiontransform-
ers with auto-correlation for long-term series forecasting. In Advances in Neural Information
ProcessingSystems(NeurIPS),pp.101–112,2021.
Haixu Wu, Tengge Hu, Yong Liu, Hang Zhou, Jianmin Wang, and Mingsheng Long. Timesnet:
Temporal2d-variationmodelingforgeneraltimeseriesanalysis. InTheEleventhInternational
ConferenceonLearningRepresentations,2023. URLhttps://openreview.net/forum?
id=ju_Uqw384Oq.
HaoXueandFloraDSalim. Promptcast: Anewprompt-basedlearningparadigmfortimeseries
forecasting. IEEETransactionsonKnowledgeandDataEngineering,2023.
XinliYu,ZhengChen,YuanLing,ShujingDong,ZongyiLiu,andYanbinLu. Temporaldatameets
llm–explainablefinancialtimeseriesforecasting. arXivpreprintarXiv:2306.11025,2023.
Ailing Zeng, Muxi Chen, Lei Zhang, and Qiang Xu. Are transformers effective for time series
forecasting? InProceedingsoftheAAAIConferenceonArtificialIntelligence,2023.
HaotianZhang,PengchuanZhang,XiaoweiHu,Yen-ChunChen,LiunianLi,XiyangDai,Lijuan
Wang,LuYuan,Jenq-NengHwang,andJianfengGao. Glipv2: Unifyinglocalizationandvision-
languageunderstanding. AdvancesinNeuralInformationProcessingSystems,35:36067–36080,
2022a.
13

PublishedasaconferencepaperatICLR2024
TianpingZhang,YizhuoZhang,WeiCao,JiangBian,XiaohanYi,ShunZheng,andJianLi. Lessis
more: Fastmultivariatetimeseriesforecastingwithlightsampling-orientedmlpstructures. arXiv
preprintarXiv:2207.01186,2022b.
XiangZhang,ZiyuanZhao,TheodorosTsiligkaridis,andMarinkaZitnik. Self-supervisedcontrastive
pre-training for time series via time-frequency consistency. Advances in Neural Information
ProcessingSystems,35:3988–4003,2022c.
YizhouZhang,LunDu,DefuCao,QiangFu,andYanLiu. Guidinglargelanguagemodelswith
divide-and-conquerprogramfordiscerningproblemsolving. arXivpreprintarXiv:2402.05359,
2024.
YunhaoZhangandJunchiYan. Crossformer: Transformerutilizingcross-dimensiondependency
formultivariatetimeseriesforecasting. InTheEleventhInternationalConferenceonLearning
Representations,2022.
HaoyiZhou,ShanghangZhang,JieqiPeng,ShuaiZhang,JianxinLi,HuiXiong,andWancaiZhang.
Informer: Beyondefficienttransformerforlongsequencetime-seriesforecasting. InProceedings
ofAAAI,2021.
TianZhou,ZiqingMa,QingsongWen,XueWang,LiangSun,andRongJin. FEDformer: Frequency
enhanceddecomposedtransformerforlong-termseriesforecasting. InProc.39thInternational
ConferenceonMachineLearning(ICML2022),2022.
TianZhou,PeisongNiu,XueWang,LiangSun,andRongJin. Onefitsall: Powergeneraltimeseries
analysisbypretrainedlm. Advancesinneuralinformationprocessingsystems,2023.
14

PublishedasaconferencepaperatICLR2024
A SHOWCASES
A.1 COMPAREWITHGPT4TS
InFigure3,4,5,6,7,weplotthecomparisonofthepredictedvaluefromourmodelandGPT4TS
modelgivenalook-backwindow. Asshowninthedatasets,weareabletopredictclosetotheground
truth,whichisalsoshownthroughoursuperiorperformanceoverothermodelsintable1. Weselect
time series with different characteristics under different prediction lengths O ∈ {96,192}: time
serieswithhighvariability(Figure5a),periodic(Figure3a,Figure3b,4a,4b),non-periodicwith
achangeintrend(Figure6a,Figure6b)
| 1                        |       |     | 1                         |                   |             |
| ------------------------ | ----- | --- | ------------------------- | ----------------- | ----------- |
| 0                        |       |     | 0                         |                   |             |
| 1                        |       |     | 1                         |                   |             |
| 2                        |       |     | 2                         |                   |             |
| 3                        |       |     | 3                         |                   |             |
| GroundTruth              |       |     |                           | GroundTruth       |             |
| 4                        |       |     | 4                         |                   |             |
| GPT4TS Prediction        |       |     |                           | GPT4TS Prediction |             |
| Ours Prediction          |       |     |                           | Ours Prediction   |             |
| 0 20                     | 40 60 | 80  | 0 25 50                   | 75 100 125        | 150 175 200 |
| (a) predictionlengthO=96 |       |     | (b) predictionlengthO=192 |                   |             |
Figure3: Visualizationoflong-termforecastingresults. ComparedbetweenourmodelTEMPOand
GPT4TSonETTh1dataset
| 1.0 |     |     | 0.50 |     |     |
| --- | --- | --- | ---- | --- | --- |
| 0.5 |     |     | 0.25 |     |     |
0.00
0.0
0.25
0.5
0.50
1.0
|     |     |     | 0.75 |     | GroundTruth |
| --- | --- | --- | ---- | --- | ----------- |
1.5 GroundTruth
| GPT4TS Prediction |     |     |      |     | GPT4TS Prediction |
| ----------------- | --- | --- | ---- | --- | ----------------- |
|                   |     |     | 1.00 |     | Ours Prediction   |
Ours Prediction
| 0 20 | 40 60 | 80  | 0 25 | 50 75 100 | 125 150 175 200 |
| ---- | ----- | --- | ---- | --------- | --------------- |
(b) predictionlengthO=192
(a) predictionlengthO=96
Figure4: Visualizationoflong-termforecastingresults. ComparedbetweenourmodelTEMPOand
GPT4TSonETTh2dataset
A.2 COMPAREWITHTIMEGPT
We also compare our results with TimeGPT (Garza & Mergenthaler-Canseco, 2023), which is
capableofgeneratingaccuratepredictionsforadiverserangeofdatasetsnotseenduringtraining,
demonstratingsuperiorperformanceinzero-shotinferencecomparedtotraditionalstatistical,machine
learning,anddeeplearningmethods. AccesstoTimeGPT-1(Beta)isprovidedthroughaPython
SDKandaRESTAPI.ThisaccessibilityallowsustoexploreTimeGPT’sforecastingcapabilitieson
ourdatasets. AsshowninFigure8andFigure9,despiteitsdesignforvariousdownstreamtasks,it
15

PublishedasaconferencepaperatICLR2024
2
2
1
1
0
0
1
1
2
2
| GroundTruth       |       |     | GroundTruth       |        |                 |
| ----------------- | ----- | --- | ----------------- | ------ | --------------- |
| 3                 |       |     | 3                 |        |                 |
| GPT4TS Prediction |       |     | GPT4TS Prediction |        |                 |
| Ours Prediction   |       |     | Ours Prediction   |        |                 |
| 0 20              | 40 60 | 80  | 0 25 50           | 75 100 | 125 150 175 200 |
(b) predictionlengthO=192
| (a) predictionlengthO=96 |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- |
Figure5: Visualizationoflong-termforecastingresults. ComparedbetweenourmodelTEMPOand
GPT4TSonETTm1dataset
0.4
GroundTruth
0.2
| 0.2 |     |     | GPT4TS Prediction |     |     |
| --- | --- | --- | ----------------- | --- | --- |
Ours Prediction
| 0.0 |     |     | 0.4 |     |     |
| --- | --- | --- | --- | --- | --- |
| 0.2 |     |     | 0.6 |     |     |
0.4
0.8
0.6
1.0
0.8
1.2
1.0
GroundTruth
| 1.2 GPT4TS Prediction |     |     | 1.4 |     |     |
| --------------------- | --- | --- | --- | --- | --- |
Ours Prediction
|                          |       |     | 0 25                      | 50 75 100 | 125 150 175 200 |
| ------------------------ | ----- | --- | ------------------------- | --------- | --------------- |
| 0 20                     | 40 60 | 80  |                           |           |                 |
| (a) predictionlengthO=96 |       |     | (b) predictionlengthO=192 |           |                 |
Figure6: Visualizationoflong-termforecastingresults. ComparedbetweenourmodelTEMPOand
GPT4TSonETTm2dataset
| 0.375 |     |     | 1.2 |     | GroundTruth |
| ----- | --- | --- | --- | --- | ----------- |
GPT4TS Prediction
| 0.400 |     |     |     |     | Ours Prediction |
| ----- | --- | --- | --- | --- | --------------- |
1.0
0.425
| 0.450 |     |     | 0.8 |     |     |
| ----- | --- | --- | --- | --- | --- |
0.475
0.6
0.500
| 0.525 |     |     | 0.4 |     |     |
| ----- | --- | --- | --- | --- | --- |
GroundTruth
0.550 GPT4TS Prediction
| Ours Prediction |     |     | 0.2 |     |     |
| --------------- | --- | --- | --- | --- | --- |
0.575
| 0 20                     | 40 60 | 80  | 0 25 50 | 75 100 | 125 150 175 200 |
| ------------------------ | ----- | --- | ------- | ------ | --------------- |
| (a) predictionlengthO=96 |       |     |         |        |                 |
(b) predictionlengthO=192
Figure7: Visualizationoflong-termforecastingresultsonweatherdataset. Comparedbetweenour
modelTEMPOandGPT4TSonweatherdataset
16

PublishedasaconferencepaperatICLR2024
GroundTruth 2
| 2   |     |     | TimeGPT Prediction |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
GPT4TS Prediction 1
| 1   |     |     | Ours Prediction |     |     |     |     |     |     |
| --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |                 | 0   |     |     |     |     |     |
| 1   |     |     |                 | 1   |     |     |     |     |     |
| 2   |     |     |                 | 2   |     |     |     |     |     |
GroundTruth
|     |     |     |     | T i | m e G P T  P re d i c t io n |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
| 3   |     |     |     | 3 G | P T 4 T S  P re d ic t i o n |     |     |     |     |
Ours Prediction
0 0 3 0 0 0 3 0 0 0 3 0 0 0 3 0 0 0 3 0 0 0 3 0 0 0 3 0 0 0 -08 14:30 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -09 13:00
02-07 16: -07 17: -07 19: -07 20: -07 22: -07 23: -08 01: -08 02: -08 04: -08 05: -08 07: -08 08: -08 10: -08 11: -08 13: 02-07 16: -07 19: -07 22: -08 01: -08 04: -08 07: -08 10: -08 13: -08 16: -08 19: -08 22: -09 01: -09 04: -09 07: -09 10:
| 2 2 | 2 2 2 2 2                | 2 2 2 2 2 | 2 2 2 | 2   | 2 2 2 | 2 2                   | 2 2 2 | 2 2   | 2 2 2 2 |
| --- | ------------------------ | --------- | ----- | --- | ----- | --------------------- | ----- | ----- | ------- |
| 0 0 | 0 0 0 0 0                | 0 0 0 0 0 | 0 0 0 | 0   | 0 0 0 | 0 0                   | 0 0 0 | 0 0 0 | 0 0 0   |
|     | (a) predictionlengthO=96 |           |       |     | (b)   | predictionlengthO=192 |       |       |         |
Figure8: Visualizationoflong-termforecastingresultsonETTm1dataset. Comparedbetweenour
modelTEMPOandTimeGPTonweatherdataset
| 1.0 GroundTruth     |                 |     |     |     | GroundTruth                    |     |     |     |     |
| ------------------- | --------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
| T i m e G P T  P    | re d i c t io n |     |     | 0.5 | T i m e G P T  P re d i c t io | n   |     |     |     |
| G P T 4 T S  P re   | d ic t i o n    |     |     |     | G P T 4 T S  P re d ic t i o n |     |     |     |     |
| 0.5 Ours Prediction |                 |     |     |     | Ours Prediction                |     |     |     |     |
0.0
0.0
0.5
0.5
1.0
1.0
1.5
11-25 14: 3 0 -25 16: 0 0 -25 17: 3 0 -25 19: 0 0 -25 20: 3 0 -25 22: 0 0 -25 23: 3 0 -26 01: 0 0 -26 02: 3 0 -26 04: 0 0 -26 05: 3 0 -26 07: 0 0 -26 08: 3 0 -26 10: 0 0 -26 11: 3 0 -26 13:00 12-01 14: 3 0 -01 17: 3 0 -01 20: 3 0 -01 23: 3 0 -02 02: 3 0 -02 05: 3 0 -02 08: 3 0 -02 11: 3 0 -02 14: 3 0 -02 17: 3 0 -02 20: 3 0 -02 23: 3 0 -03 02: 3 0 -03 05: 3 0 -03 08: 3 0 -03 11:30
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
|     | (a) predictionlengthO=96 |     |     |     | (b) | predictionlengthO=192 |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --------------------- | --- | --- | --- |
Figure9: Visualizationoflong-termforecastingresultsonETTm2dataset. Comparedbetweenour
modelTEMPOandTimeGPTonweatherdataset
isimportanttonotethatTimeGPTmaynotperformaswellinlong-termforecastingscenarios. In
contrast,ourproposedmodelexcelsinzero-shotsettings,includinglong-termforecasting,illustrating
theneedforfoundationmodelsthatcanadapttoboththebreadthoftimeseriesapplicationsandthe
depthofforecastinghorizons.
| B EXPERIMENT | SETTING |     |     |     |     |     |     |     |     |
| ------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
B.1 TOWARDSFOUNDATIONMODELEXPERIMENTSDETAILS
|     |     |     |     |     | It  | has been | well-established |     | that |
| --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ---- |
channel-independenceworkswellfor
| Table4: | Datasetdetailsofbenchmarkdataset. |     |     |     |     |     |     |     |     |
| ------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
timeseriesdatasets,sowetreateach
multivariatetimeseriesasmultiplein-
|             |        |            |                |     | dependentunivariatetimeseries. |         |          |        | We           |
| ----------- | ------ | ---------- | -------------- | --- | ------------------------------ | ------- | -------- | ------ | ------------ |
| Dataset     | Length | Covariates | SamplingPeriod |     |                                |         |          |        |              |
|             |        |            |                |     | use                            | popular | time     | series | benchmark    |
| ETTh        | 17420  | 7          | 1hour          |     | datasets(Zhouetal.,2021):      |         |          |        | ETTm1,       |
| ETTm        | 69680  | 7          | 15min          |     | ETTm2,                         | ETTh1,  |          | ETTh2, | Weather,     |
| Weather     | 52696  | 22         | 10min          |     |                                |         |          |        |              |
|             |        |            |                |     | Electricity,                   |         | Traffic, | ILI    | and exchnge. |
| Electricity | 26304  | 321        | 1hour          |     |                                |         |          |        |              |
|             |        |            |                |     | 1)ETTm1,                       |         | ETTm2,   | ETTh1, | ETTh2        |
| Traffic     | 17544  | 862        | 1hour          |     |                                |         |          |        |              |
containelectricityloadfromtwoelec-
tricitystationsat15minutesleveland
hourlylevel. 2)Weatherdatasetcontains21meteorologicalindicatorsofGermanywithin1year;3)
Electricitydatasetcontainselectricityconsumption;4)Trafficdatasetcontainstheoccupationrate
ofthefreewaysystemacrosstheStateofCalifornia. ThelookbackwindowLisfollowing (Zhou
etal.,2023),andthepredictionlengthOissetto{96,192,336,720}. Inthisexperimentpart,our
experimentswereconductedusingsingleNVIDIAA100GPU,withabatchsizesetto256, and
focused on long-term forecasting by employing a Mean Squared Error (MSE) loss function. To
17

PublishedasaconferencepaperatICLR2024
ensurethereliabilityofourresults,weperformedthreeiterativeloopsandcalculatedtheaverageof
theoutcomes. Ourexplorationcovered[3,6]GPTlayersandtestedvariousweights,[0.001,0.01,
and1],fortheMSElossfunctionappliedtothereconstructedcomponentsofthetimeseries. We
havedocumentedtheoptimalresultsobtainedfromthissearch. Acomprehensiveanalysisofthe
impactthatthenumberofGPTlayershasontheperformancewillbeaddressedinfutureresearch.
TowardsFoundationModel’sZeroShotSetting Foreachpredictionlength,wetrainamodelon
amixtureoftrainingdatafromdifferentdomainsandtestthemodelonthetargetunseendomain’s
data. Weconstructthecombinedtrainingdatasetbypoolingthetrainingdataandfullyshufflinge
them. Topreventunduebiasandensurefairrepresentationofdatafromeachdomaininthecombined
training data, we select an equal number of training examples from each domain’s training data.
We noted that the number of training samples that ETTh1 and ETTh2 has is on a much smaller
magnitudecomparedtotheotherthreetrainingdatasets(ETTm1,Weather,Electricity),soselecting
theminimumnumberoftrainingsamplesamongallothertrainingdatasetswouldresultintoomuch
datalossfromETTm1,Weather,andElectricity,etc. Therefore,weincludedalltrainingexamples
fromETTh1andETTh2inthecombinedtrainingdataset. Similartotraditionalexperimentalsettings,
eachtimeseries(ETTh1,ETTh2,ETTm1,Weather,Electricity,ETTm2,Traffic)issplitintothree
parts: trainingdata,validationdata,andtestdatafollowingin7:1:2ratioin (Zhouetal.,2022),and
weonlymergethetrainingandvalidationdata. ForETTm1,ETTm2,WeatherandElectricitydata,
thenumberofexamplessampledtobepooledintothecombinedtrainingdatasetischosentobethe
minimumnumberoftrainingexamplesamongthesetrainingdatasets.
B.2 PROPOSEDTETSDATASETSETTING
Prompt:
Suppose you are living in {Year: 2000}, can you help me summarize the news and reports in {Year:
2000}’s {quarter: second quarter} for {company name: Company A}, which is an {company sector:
Technology} company. Please directly give me the answer limited to 2 sentences without apology.
GPT Response:
Description:

In the second quarter of 2000, Company A reported a net profit of $233 million, up from $123 million
in the same quarter of the previous year, driven by strong sales of its X computers and Products Y.
However, the company's stock price dropped after warning that its third-quarter profits would be
below expectations due to slower sales.
Figure10: ExamplefordesigningpromptsusingOPENAIChatGPT-3.5API.
DataCollection Ourtimeseriesdataforfinancialanalysisandforecastingarederivedprimarily
fromthefinancialstatementsofcompaniesincludingbalancesheets,incomestatements,andcash
flowstatements. Specifically,weutilizedatafromthe500largestU.S.companiesacross11sectorsas
listedintheStandard&Poor’s500Index(S&P500),whichwedivideintotwoparts: thefirstseven
sectorsfortrainingandevaluation,andtheremainingfourforzero-shotforecastingtaskstotestthe
model’sabilitytopredictinunseendomains. Whilecollectingcorrespondingcontextualinformation
fromtheabundanceofdigitalnewssourcesischallenging,OpenAI’sChatGPTAPIoffersasolution
togatherandcondenserelevantnewsefficiently. ByinputtingkeydetailsintotheAPIandlimiting
theresponseto110tokens,asshowninFigure10,wecanswiftlyextractpertinentcontextualdatato
improveouranalysis. PleaserefertoSectionHforfurtherdetailsofcreatingTETSdataset.
Predictionobjective TheprimaryobjectiveofourexperimentistoforecasttheEarningsBefore
Interest, Taxes, Depreciation and Amortization(EBITDA) for companies listed in S&P500, and
ourdatarangefrom2000to2022. Followingthemultivariatetimeseriesframeworkpresentedin
(Papadimitriouetal.,2020),weselectfoundationalfinancialmetricsfromtheincomestatementsas
inputfeatures: costofgoodssold(COGS),selling,generalandadministrativeexpenses(SG&A),RD
expenses(RD EXP),EBITDA,andRevenue. Comparingwithothermetrics,theselectedmetrics
containinformationmorerelevanttoourpredictionobjective. ForLargeLanguagebasedmodels,
18

PublishedasaconferencepaperatICLR2024
includingourmodelTEMPO,GPT4TS,andT5,weapplychannel-independencestrategytoperform
univariatetimeseriesforecastingtasks. Allfivefeaturesareusedfortraining(predictingitsfuture
valuebasedonitspastvalue), whileonlyEBITDAisaccessibleduringthetrainingstage. Other
modelsfollowthemultivariatetimeseriesforecastingsetting,treatingthefivefeaturesasmultivariate
inputandpredictingthetarget,EBITDA,bothinthetrainingandtestingstages.
WepredictquarterlyEBITDAbasedonthepast20quarters’data. Thispredictedvalueisthenused
toforecastthenextquarter’sEBITDA,iterativelyfourtimes,leadingtoayearlyprediction. Inorder
tomeasuretheaccuracyofthesepredictionsbasedonthecumulativeyearlyvalue(sumof4quarters),
weemploythesymmetricmeanabsolutepercentageerror(SMAPE)astheevaluationmetricaswell
astheforecastinglossfunctioninthisexperimentalpart.
Data Split For companies under each sector, we employ the windowing method to generate
cohesivetrainingandtestinginstances. Underthechannel-independencesettingwhereweseparate
eachfeaturetoobtainunivariatetimeseries,weget80,600samplesfromthesevenin-domainsectors,
and 9,199 samples from the four zero-shot sectors(also known as cross-domain sectors), five as
muchaswegetinthechanneldependentsetting. Thesectorssplittingiselaboratedin H.Inour
experimentsshownintable2,Weuse70%ofin-domaindatafortraining,10%ofin-domaindatafor
evaluation,andallzero-shotdataforunseentesting.
SymmetricMeanAbsolutePercentageError Inreality,themagnitudeoffinancialmetricscan
varysignificantlyamongdifferentcompanies.So,wechoosethesymmetricmeanabsolutepercentage
error(SMAPE),apercentage-basedaccuracymeasure,asourevaluationmetric. ForEBITDA,there
aremanynegativeresultsthatmayinfluencethefinalSMAPE.WeusetheformofSMAPE-Abs
SMAPE:
n
AbsSMAPE=
200%(cid:88) |F
t
−A
t
|
, (4)
n |F |+|A |
t t
t=1
Here,F representsthetruevalue,A representsthepredictedvalueinoursystem,andnrepresents
t t
thetotaltimestepsweneedtoforecast.
SMAPEcanbeparticularlysensitivetooutliers. Specifically,whenthetruedataandpredictionhave
oppositesigns,theresultingerrormaybeupto200%,seriouslydistortingthefinalresults. Following
theapproachin(Papadimitriouetal.,2020),wefilteroutdatapointsatthe80%and90%thresholds
andfindmostoftheoutliersarerelatedtosignificantfinancialshiftsduetomergers&acquisitions
(M&A).
B.3 GDELTDATASETSETTING
We utilized the GDELT dataset (Jia et al., 2024), which focuses on predicting the respective
mentions and mentions in the news media. We utilized the data collected from the 55 regions
under the US and the national data for the US and divided the 10 event root types in the dataset
into unseen and seen sets, as demonstrated in Table 5. We focused on predicting the three key
variablesNumMentions,NumArticles,NumSourcesrelatedtotheparticulareventtypewithinagiven
timeframeandgeographicalregion. Weapplychannel-independencestrategytoperformunivariate
timeseriesforecastingtsksforallbaselinemodelsandourmodel. Allthreefeaturesareusedfor
trainingandevaluation(predictingitsfuturevaluebasedonitspastvalue).
Wepredictthefuture7daysbasedonthepast15days’datadirectly. Inothertomeasuretheaccuracy
of the predicitions, we use mean square error (MSE) and mean absolute error (MAE). For each
region,weemploythewindowingmethodtogeneratecohesivetrainingandtestinginstancesfor
eacheventroottype. Underourchannel-independencesetting,weget122,008samplesfromthe
sevenin-domainsectors(seensectors)fortraining,and76,048samplesforevaluatingunderthethree
zero-shotsectors(unseensectors). Inourexperiments,weuse70%ofin-domaindatafortraining,
10%forevaluationandallzero-shotdataforunseentesting.
19

PublishedasaconferencepaperatICLR2024
| EventNumber   | EventTypeName               |         |
| ------------- | --------------------------- | ------- |
|               | 01 MakePublicStatement      |         |
|               | 02                          | Appeal  |
|               | 03 ExpressIntenttoCooperate |         |
| TrainingEvent | 04                          | Consult |
05 EngageinDiplomaticCooperation
|           | 07  | ProvideAid |
| --------- | --- | ---------- |
|           | 08  | Yield      |
|           | 11  | Disapprove |
| TestEvent | 17  | Coerce     |
|           | 19  | Fight      |
Table5: EventnumbertoeventtypeNametable
C FURTHER RESULTS
C.1 SELF-SUPERVISEDREPRESENTATIONLEARNING
Ourproposedmodelarchitecturecanbedesignedtosupportself-supervisedlearningandthusfurther
embracefoundationmodelsfortimeseries. Following (Nieetal.,2023),wemaskarandomsubset
ofpatchesbyreplacingthemwithzeros,wherethepatchesaredividedintonon-overlappingpatches
forsimplicityandtoavoidmaskedpatchesinfluencingpredictions. Thepredictionheadisremoved
andreplacedwithalinearlayertoreconstructthemaskedpatches. Themodelistrainedtominimize
theMSEbetweenthepredictedandtruemaskedpatches. Tohandlemultivariatetimeserieswith
varyingnumbersoffeatures,weapplychannelindependence(Zengetal.,2023)tomodeleachtime
seriesindependently.
WiththestrongperformanceTEMPOshowedundertheexperiment’many-to-one’zero-shotsetting,
fromtheperspectiveofaself-supervisedcross-domainfoundationalmodel,wefurtherinvestigateif
usingaTEMPOmodeltrainedondatasetsacrossdomainscanstillachievecomparableperformance
onunseendomains. Here,westillusethe’many-to-one’settingbutthemodelistrainedinaself-
supervisedmanner. Specifically,wefirstuseallotherdomain’sdatatotrainarepresentationmodel
thenonlyuse5%dataofthetrainingdatatofineturnthetotalmodelwiththepredictionlayerasa
forecastingdownstreamtask. Table6providesacomprehensivecomparisonofourmodelagainst
otherbaselinemodelsonthreemultivariatetimeseriesdatasetsthatareunseenbythemodelsduring
training,namelyelectricityandtrafficandweather.Alltheseselected3datasetsareentirelydissimilar
toanydatathemodelhasencounteredbefore. TEMPOoutperformsbaselinemodels,achievingthe
lowest MSE and MAE in most cases. Note that TEMPO’s average MSE and MAE is 7.3% and
4.6%lessthanthebest-performingbaselinemodel(GPT2)fortheweatherdataset,respectively. This
findingshedlightonthestronggeneralizabilityofTEMPOandindicateditspotentialofservingasa
foundationaltimeseriesforecastingmodel,maintainingrobustperformanceforunseendomains.
C.2 COMPARINGWITHFULL-SHOTSTATE-OF-THE-ARTSBASELINES
Towardsfoundationmodeltrainingdifferssignificantlyfromtheone-to-one/manyscenarios,where
pre-traininginvolvesahomogenousdataset,oftenwithconsistentseasonpatterns,samplingrates,
andtemporalscales. Thishomogeneityfacilitatespatternlearningtransferabletofine-tuneddatasets.
Incontrast,towardsfoundationmodeltraininginvolvespre-trainingonhighlydiversedatasets,such
as merging traffic and weather data, which may hinder the model’s ability to discern underlying
patterns. InTable7,weprovidefurtherresultsonETTh1andETTh2datasets,demonstratingthat
theperformanceofTEMPO(zero-shotsetting)surpassesthatofstate-of-the-artmodelsspecifically
designedforthesetargetdatasetswithfull-shotsettings. TheresultsinTable7areobtainedfrom
(Liuetal.,2023),includingbutnotlimitedtoiTransformer(Liuetal.,2023),Crossformer(Zhang&
Yan,2022),TiDE(Dasetal.,2023a)andSCINet(Liuetal.,2022),whicharealsoreportedinour
contemporaneouswork,MOIRAI(Wooetal.,2024).
20

PublishedasaconferencepaperatICLR2024
Table6: Self-supervisedrepresentationlearningresultsarefine-tunedon5%in-domaindatasets. We
usepredictionlengthO ∈{96,192,336,720}. AlowerMSEindicatesbetterperformance,andthe
bestresultsareinbold.
|         | TEMPO           | GPT4TS      | T54TS       | Bert4TS     | PatchTST    |
| ------- | --------------- | ----------- | ----------- | ----------- | ----------- |
|         | MSE/MAE         | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     |
|         | 96 0.19/0.29    | 0.202/0.301 | 0.199/0.293 | 0.202/0.298 | 0.21/0.308  |
|         | 192 0.211/0.31  | 0.217/0.313 | 0.238/0.337 | 0.227/0.321 | 0.223/0.312 |
| ECL     | 336 0.229/0.323 | 0.258/0.353 | 0.273/0.364 | 0.256/0.345 | 0.282/0.357 |
|         | 720 0.375/0.444 | 0.43/0.475  | 0.455/0.49  | 0.442/0.479 | 0.606/0.561 |
|         | Avg 0.251/0.342 | 0.277/0.361 | 0.291/0.371 | 0.282/0.361 | 0.33/0.385  |
|         | 96 0.56/0.411   | 0.607/0.417 | 0.543/0.408 | 0.591/0.423 | 0.577/0.403 |
|         | 192 0.575/0.419 | 0.603/0.421 | 0.594/0.431 | 0.613/0.432 | 0.596/0.411 |
| Traffic | 336 0.597/0.433 | 0.63/0.435  | 0.659/0.458 | 0.639/0.445 | 0.665/0.454 |
|         | 720 0.65/0.452  | 0.643/0.439 | 0.69/0.49   | 0.744/0.496 | 0.802/0.501 |
|         | Avg 0.595/0.429 | 0.621/0.428 | 0.622/0.447 | 0.647/0.449 | 0.66/0.442  |
|         | 96 0.217/0.268  | 0.288/0.31  | 0.252/0.288 | 0.237/0.288 | 0.249/0.285 |
|         | 192 0.265/0.302 | 0.305/0.331 | 0.322/0.336 | 0.291/0.323 | 0.277/0.314 |
| Weather | 336 0.322/0.342 | 0.338/0.353 | 0.346/0.358 | 0.335/0.354 | 0.311/0.341 |
|         | 720 0.41/0.397  | 0.381/0.377 | 0.444/0.42  | 0.466/0.436 | 0.385/0.386 |
|         | Avg 0.304/0.327 | 0.328/0.343 | 0.341/0.351 | 0.332/0.35  | 0.305/0.331 |
Table7: ResultsoflongtermforecastingexperimentsonETTh1andETTh2. Thebestresultsare
markedinboldandthesecondoptimalinunderlined,respectivelywithMSE/MAE.Notethatthe
TEMPOisunderzero-shotsettingandothermodelsareunderfull-shotsetting.
TEMPO iTransformer TimesNet PatchTST Crossformer TiDE DLinear SCINet FEDformer
MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE
96 0.400/0.406 0.386/0.405 0.384/0.402 0.414/0.419 0.423/0.448 0.479/0.464 0.386/0.400 0.654/0.599 0.376/0.419
192 0.426/0.421 0.441/0.436 0.436/0.429 0.460/0.445 0.471/0.474 0.525/0.492 0.437/0.432 0.719/0.631 0.420/0.448
1hTTE
336 0.441/0.430 0.487/0.458 0.491/0.469 0.501/0.466 0.570/0.546 0.565/0.515 0.481/0.459 0.778/0.659 0.459/0.465
720 0.443/0.451 0.503/0.491 0.521/0.500 0.500/0.488 0.653/0.621 0.594/0.558 0.519/0.516 0.836/0.699 0.506/0.507
Avg. 0.428/0.427 0.454/0.447 0.458/0.450 0.469/0.454 0.529/0.522 0.541/0.507 0.456/0.452 0.747/0.647 0.440/0.460
96 0.301/0.351 0.297/0.349 0.340/0.374 0.302/0.348 0.745/0.584 0.400/0.440 0.333/0.387 0.707/0.621 0.358/0.397
192 0.355/0.389 0.380/0.400 0.402/0.414 0.388/0.400 0.877/0.656 0.528/0.509 0.477/0.476 0.860/0.689 0.429/0.439
2hTTE
336 0.379/0.408 0.428/0.432 0.452/0.541 0.426/0.433 1.043/0.731 0.643/0.571 0.594/0.541 1.000/0.744 0.496/0.487
0.409/0.440
720 0.427/0.445 0.462/0.657 0.431/0.446 1.104/0.763 0.874/0.679 0.831/0.657 1.249/0.838 0.463/0.474
Avg. 0.361/0.398 0.383/0.407 0.414/0.427 0.387/0.407 0.942/0.684 0.611/0.550 0.559/0.515 0.954/0.723 0.437/0.449
21

PublishedasaconferencepaperatICLR2024
Table8: ComparetheresultswithARIMA.
ECL Traffic Weather Ettm2
TEMPO ARIMA TEMPO ARIMA TEMPO ARIMA TEMPO ARIMA
MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE MSE/MAE
96 0.178/0.276 1.220/0.814 0.476/0.343 1.997/0.924 0.211/0.254 0.217/0.258 0.185/0.267 0.225/0.301
192 0.198/0.293 1.264/0.842 0.496/0.355 2.044/0.944 0.254/0.298 0.263/0.299 0.243/0.304 0.298/0.345
336 0.209/0.309 1.311/0.866 0.503/0.356 2.096/0.960 0.292/0.332 0.330/0.347 0.309/0.345 0.370/0.386
720 0.279/0.355 1.364/0.891 0.538/0.376 2.138/0.971 0.393/0.387 0.425/0.405 0.386/0.395 0.478/0.445
Avg. 0.216/0.308 1.290/0.853 0.503/0.357 2.069/0.950 0.287/0.318 0.309/0.327 0.280/0.328 0.343/0.369
C.3 COMPARINGWITHARIMA
Asapioneeringfoundationmodel,TEMPOisengineeredtoforecastfuturevaluesdirectly,eliminating
thenecessityforretrainingwitheachnewdatainstance. Itsunderlyingframeworkcapturesintricate
temporalpatterns,grantingittheversatilitytogeneralizeacrossvarioustimeseries. Inthisstudy,we
compareTEMPO’sforecastingprowesswiththatoftheARIMAmodel(Hyndman&Khandakar,
2008), which is renowned for its capacity to make accurate predictions within a specific time
seriesoncetheinitialmodelparametershavebeenset. WhileARIMAmodelsexcelincontinuing
predictionswithintheseriestheyareconfiguredfor,theydonotinherentlypossessthefacultyto
forecastacrossdisparatetimeserieswithoutrecalibration. WeobtaintheARIMA’sforecastingresults
from (Challuetal.,2023). AsshowninTable8,theresultshighlightthesuperioradaptabilityof
our‘towardsfoundationmodel’–TEMPO–whichretainsitspredictiveaccuracyevenwhenapplied
totimeseriesbeyonditstrainingscope, therebyillustratingthefeasibilityofmoreuniversaland
resilientforecastingmethodologies.
D FURTHER ANALYSIS
D.1 DESIGNOFPROMPTPOOL
Inthissection,weproposeanotherpotentialpromptdesignforaddressingnon-stationarynatureof
real-worldtimeseriesdatawithdistributionalshifts(Huangetal.,2020). Specifically,weintroduce
asharedpoolofpromptsstoredasdistinctkey-valuepairs. Ideally,wewantthemodeltoleverage
relatedpastexperiences,wheresimilarinputtimeseriestendtoretrievethesamegroupofprompts
from the pool (Wang et al., 2022b). This would allow the model to selectively recall the most
representativepromptsatthelevelofindividualtimeseriesinstanceinput. Inaddition,thisapproach
can enhance the modeling efficiency and predictive performance, as the model would be better
equippedtorecognizeandapplylearnedpatternsacrossdiversedatasetsviaasharedrepresentation
pool. Promptsinthepoolcouldencodetemporaldependencies,trends,orseasonalityeffectsrelevant
todifferenttimeperiods. Specifically,thepoolofpromptkey-valuepairsisdefinedas:
V ={(k ,V ),(k ,V ),··· ,(k ,V )}, (5)
K 1 1 2 2 M M
where M is length of prompt pool, V
m
∈ RLp×LE is a single prompt with token length L
p
and the same embedding size L
E
as P
T
i and k
m
∈ K = {k
m
}M
m=1
with the shape of RLE.
The score-matching process can be formulated with the score-matching function γ (cid:0) Pi,k (cid:1) =
T m
P
T
i ·k
m
/∥P
T
i∥∥k
m
∥,whereγ : RLE ×RLE → R. Themodelistrainedinanend-to-endwayto
optimizepredictionswiththeprompts. ThequeryPi thatisusedtoretrievethetop-Kcorresponding
T
valuecomesfromthepatchedtimeseriesinput. Therefore,similartimeseriescanbeassignedto
similarprompts. Denoting{s }K asasubsetofKindicesfortheselectedtop-Kprompts,ourinput
j j=1
embeddingoftrendisasfollows:
x =[V ;··· ;V ;P ], 1≤K≤M, (6)
T s1 sK T
where we concatenate all the tokens along the temporal length dimension, so as x ,x . Each
S R
instance can be assigned to multiple prompts, which can jointly encode knowledge pertinent to
the forecasting task- such as periodic patterns exhibited by the time series, prevailing trends, or
seasonalityeffects.
22

PublishedasaconferencepaperatICLR2024
Table9: ComparethedifferentpromptdesignsontheETTm2dataset.
Semi-soft Soft Hard Pool Poolmaskall
mse/mae mse/mae mse/mae mse/mae mse/mae
96 0.182/0.263 0.189/0.271 0.182/0.267 0.185/0.267 0.1952/0.274
192 0.243/0.304 0.252/0.307 0.243/0.302 0.242/0.304 0.2739/0.324
336 0.309/0.344 0.306/0.348 0.299/0.340 0.289/0.336 0.3131/0.354
720 0.384/0.392 0.386/0.394 0.380/0.392 0.373/0.386 0.3794/0.390
Avg. 0.280/0.326 0.283/0.330 0.276/0.325 0.273/0.323 0.290/0.335
D.2 RESULTSONDIFFERENTPROMPTDESIGN
Inthissection,weexaminetheimpactofvariouspromptdesignsonmodelperformance. Weutilize
the‘semi-soft’promptasoutlinedinSection3.3,wherethepromptvectorsareinitializedsemi-softly;
the soft prompt, which entails the random initialization of vectors of identical dimensions to the
‘semi-soft’prompt;andthehardprompt,whichissemanticallymeaningfulandremainsfixedpost-
tokenization. Additionally,weexplorethepromptpool,asdescribedinSection D.1,andemploya
similarleave-one-outapproachtomaskallpromptswithinthepooltoinvestigateitseffectiveness.
Thefindings,presentedinTable 9,revealthat,intheETTm2dataset,thepromptpooloutperforms
the‘semi-soft’promptinthreeoutoffourscenarios,underscoringthepotentialofpromptstoenhance
modelcapacityandadaptabilitytoshiftsindatadistribution. Furthermore,weobservethatprompts
withexplicitsemanticcontent(Semi-softandHard)surpasstheperformanceofsimplesoftprompts.
This suggests that incorporating semantic information as discrete indicators within a pre-trained
modelcanmoreeffectivelyorchestratedomainknowledge. Thisunderstandinginformsthedesignof
promptsforefficientinteractionwithlanguagemodels,especiallyinapplicationswhereprecision
andrelevanceoftheoutputarecrucial.
D.3 ANALYSISONPROMPTPOOL
Hereisasummaryofhowthepromptsareinitializedandtrainedinourwork:
• Initialization: Thepromptembeddingsinthepoolarerandomlyinitializedfromanormal
distribution,asisstandardpracticefortrainableparametersinneuralnetworks.
• Training: Theprompts’valueandallothermodelparametersaretrainedinanend-to-end
mannertooptimizetheforecastingobjective. Thisallowsthepromptstobecontinuously
updatedtoencoderelevanttemporalknowledge.
Thenumberofpromptsandembeddingdimensionsaretreatedashyperparametersandtunedfor
goodperformance. Differentpoolsettings,includingpoolsize,topknumber,andpromptlength,
willleadtodifferentresults. Toexplorethis,weconductatotalof27experiments,setting3distinct
valuesforeachofthe3settings: (1)poolsizeof10,20,and30. (2)topknumbersof1,2,and3. (3)
promptlengthsof1,2,and3. WechoosethecombinationwiththebestresultsforTEMPO settings.
Forthelong-termandshort-termforecastingexperiments,wechooseapoolsizewithM =30and
K=3andpromptlengthis3. Detaileddesignanalysisprovidesinsightsintopromptsimilarityand
selection. Notethat,thepromptpool’skeyin (Wangetal.,2022b)istrainablewhichallowsusto
maintainconsistentanddistinctcharacteristicsoftimeseriesdataforanalysis. Ourworkoffersan
initialexplorationintoprompt-basedtuningfortimeseriesforecasting,butsubstantialroomremains
foradvancingpromptpooldesign.
D.3.1 PROMPTSELECTIONDISTRIBUTION
Toelucidatethemechanicsbehindpromptselection,wehavevisualizedthedistributionhistograms
for chosen prompts corresponding to the trend, seasonal, and residual elements of the ETTm2
datasetinFigure11. Inourexperimentalframework,eachdatapointispermittedtoselectmultiple
prompts—withthreepromptsbeingchosenpercomponent. Consequently,thefrequencyisdeter-
minedbythenumberoftimesaparticularpromptisselectedacrossthedataset. Thehistograms
revealpronounceddiscrepanciesinpromptpreferencesbetweenperiodicandseasonalcomponents.
23

PublishedasaconferencepaperatICLR2024
1.0
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0.0
01234567891011121314151617181920212223242526272829
Prompt ID
ycneuqerF
Trend
Season
Noise
Figure11: PromptDistributionforpromptpoolselection.
For instance, within the ETTm2 dataset, prompts 11, 20, and 24 are predominantly selected for
capturingtrends,whereasprompts8,10,and29areprimarilychosenforseasonalfluctuations. This
observationsubstantiatesthepremisethatthepromptpoolisadeptatfurnishingspecializedprompts
tailoredtodiscretecharacteristicsoftimeseriesdata.
D.4 ANALYSISONDESIGNSOFINJECTINGCONTEXTUALINFORMATION
Table10: SMAPEresultsofGEBDITdatasetwithdifferenttextualinformationinjection.
Event Sum+TP SumP+TP Sum⊕TP SumP⊕TP Sum+Semi SumP+Semi Sum⊕Semi SumP⊕Semi
EPAMS 11 38.77 38.77 38.75 38.90 38.91 38.82 39.04 38.79
17 41.02 41.03 40.95 41.05 41.24 41.08 41.38 41.08
19 44.03 44.02 44.06 44.10 44.41 44.19 44.73 44.24
Inthissection,weinvestigatetheinfluenceofvariousconfigurationsoftextualinjectionandoriginal
prompt design from multi-modality perspective. As depicted in Table 10, eight distinct prompt
designs were formulated. ’Sum’ denotes the utilization of a direct summary of textual data as a
prompt,while’SumP’signifiestheuseoftextualinformationasaquerywithinthepromptpool. The
symbols’+’and’⊕’representsummationandconcatenationoperations,respectively. ’TP’stands
for’timeseriespromptpool,’and’Semi’indicatesa’semi-softprompt’wherewemanuallydesign
theprompt,withtrainableparameters,referredtoas”Predictthefuturetimestepgiventhe{time
seriesdatatype}”for3differenttimeseries(Trend,Season,Residual)afterdecomposition. Each
designchoiceexertsadistinctimpactontheperformancemetrics. Thedirectincorporationoftextual
informationalongwiththepromptpoolyieldsthemostoptimalandnear-optimaloutcomes. Infuture
work,weaimtodelvedeeperintotheanalysisofmultimodalsolutiondesignstrategiesfortimeseries
forecasting.
D.5 HIDDENREPRESENTATION
Figure12demonstratesthedifferencebetweentherepresentationoftheoutputhiddenspacefrom
thepre-trainedlangaugemodel. WhiletherepresentationoftimeserieslearnedfromGPT4TSis
centeredasawhole,therepresentationofthedecomposedcomponentfromTEMPOimpliesacertain
softboundarybetweenthethreecomponents. ThisisademonstrationofhowTEMPOisabletolearn
therepresentationoftrend,seasonality,residualpartsrespectively,whichcontributestothesuperior
performanceofourmodelTEMPO.
24

PublishedasaconferencepaperatICLR2024
|     | Trend | 100 |     | Original Time Series |
| --- | ----- | --- | --- | -------------------- |
Seasonality
| 100 | Residual | 75  |     |     |
| --- | -------- | --- | --- | --- |
50
50
| 2 noisnemid ENS-t |     | 2 noisnemid ENS-t 25 |     |     |
| ----------------- | --- | -------------------- | --- | --- |
| 0                 |     | 0                    |     |     |
25
50
50
75
100
| 100 50 t-SNE dim0ension 1 | 50 100 | 100 100 | 50 t-SNE dim0ension 1 | 50 100               |
| ------------------------- | ------ | ------- | --------------------- | -------------------- |
| (a) TEMPO-ETTh1           |        | (b)     | GPT4TS-ETTh1          |                      |
|                           | Trend  |         |                       | Original Time Series |
Seasonality
| 100 | Residual | 75  |     |     |
| --- | -------- | --- | --- | --- |
50
50
| 2 noisnemid ENS-t |     | 2 noisnemid ENS-t 25 |     |     |
| ----------------- | --- | -------------------- | --- | --- |
| 0                 |     | 0                    |     |     |
25
50
50
| 100 |     | 75  |     |     |
| --- | --- | --- | --- | --- |
100
| 100 50 t-SNE dime0nsion 1 | 50 100 | 100 75 | 50 25t-SNE di0mension 125 | 50 75 100            |
| ------------------------- | ------ | ------ | ------------------------- | -------------------- |
| (c) TEMPO-ETTh2           |        | (d)    | GPT4TS-ETTh2              |                      |
|                           | Trend  | 100    |                           | Original Time Series |
Seasonality
| 100               | Residual | 75                |     |     |
| ----------------- | -------- | ----------------- | --- | --- |
| 50                |          | 50                |     |     |
| 2 noisnemid ENS-t |          | 2 noisnemid ENS-t |     |     |
25
| 0   |     | 0   |     |     |
| --- | --- | --- | --- | --- |
25
50
50
| 100                       |                 | 75     |                           |                      |
| ------------------------- | --------------- | ------ | ------------------------- | -------------------- |
| 100 50 t-SNE dime0nsion 1 | 50 100          | 100 75 | 50 25t-SNE dim0ension 125 | 50 75 100            |
| (e) TEMPO-ETTm1           |                 | (f)    | GPT4TS-ETTm1              |                      |
|                           | T r e n d       |        |                           | Original Time Series |
|                           | S e a s onality | 100    |                           |                      |
| 100                       | Residual        |        |                           |                      |
75
| 50                |     | 50                |     |     |
| ----------------- | --- | ----------------- | --- | --- |
| 2 noisnemid ENS-t |     | 2 noisnemid ENS-t |     |     |
25
| 0   |     | 0   |     |     |
| --- | --- | --- | --- | --- |
25
50
50
75
100
100
| 100 50 t-SNE0 dimension 1 | 50 100 | 75 50 | 25 t-SNE d0imension 125 | 50 75 100 |
| ------------------------- | ------ | ----- | ----------------------- | --------- |
| (g) TEMPO-ETTm2           |        | (h)   | GPT4TS-ETTm2            |           |
Figure12: ComparisonofGPT4TSrepresentationwithTEMPOrepresentationforpredictionlength
O =96usingTSNE.Trendinred,seasonalityinblue,residualingreen.
25

PublishedasaconferencepaperatICLR2024
D.6 MODELTRAININGTIMECOMPARISON
Figure 13illustratesthetrainingtimeofotherbaselinemodelsincomparisontoourmodelTEMPO.
Toensurefairness,wecalculatedthepercentageofruntimeformodelsoperatingonidenticalmachines
andutilizingequivalentcomputationalresources. Eachmodel’strainingtimeispresentedasaratio
relativetoTEMPO’strainingtime. Avaluelessthan1indicatesthatthemodeltrainsfasterthan
TEMPO, while a value greater than 1 suggests the opposite. We use horizontal bars to visually
representeachmodel’srelativetrainingtime,withthebarsextendingtotheleftorrightofthecentral
verticallinebasedonwhethertheyarefasterorslowerthanourmodelTEMPO,respectively.
Figure13: VisualComparisononrelativetrainingtimeofothermodelsandourproposedmodel
TEMPO underchannelindependentsetting.
BERT 0.32
LLAMA 4.62
TimesNet 5.70
DLinear 0.02
LightTS 0.03
PatchTST 0.20
FEDformer 3.45
ETSformer 0.77
T5 0.43
GPT4TS 0.24
TEMPO 1.00
0 1 2 3 4 5 6
E THE ROLES OF GENERALIZED ADDITIVE MODELS (GAM) AND SHAPLEY
ADDITIVE EXPLANATIONS (SHAP)
Inourpaper,GAMandSHAPserveasinstrumentaltools,notonlyforaffirminganticipatedfindings
butalsoforyieldingdeeperinsightsandexplanationsintotheinnerworkingsofintricatemodels.
• RoleofGAM:GAMinherentlymodelstheeffectsofdifferentfeaturesasadditivecompo-
nents. ThischaracteristicofGAMprovidesintrinsicinterpretabilitytoTEMPO.It’snot
merelyatoolforconfirmingtheabsenceofpatternsinresiduals;italsohelpsusunderstand
howeachfeaturecontributestothefinalprediction.
• RoleofSHAP:SHAPhelpsinattributingfeatureeffectspost-hoctoexplainthepredictions
madebycomplexmodels,whichmayotherwisebeopaque.
TheutilityofGAMandSHAPinouranalysiscanbedetailedasfollows:
• ConfirmationofAssumptions: theanalysesquantitativelyconfirmassumptionsaboutmodel
behaviorwithdata-drivenevidence,ratherthanjustintuition. Thissubstantiationincreases
thetrustandtransparencyinthemodel’spredictions;
• DetectingUnexpectedBehaviors: thecomponentattributioncouldrevealunexpectedbe-
haviorsifpresent. Forexample,residualimpactbeinghigherthanexpectedcouldindicate
overfittingnoise.
• ProvidingNuancedInsights: SHAPprovidesnuancebeyondhigh-levelexpectations,like
showingtheincreasingerrorofseasonalcomponentsinlongerforecasts.
26

PublishedasaconferencepaperatICLR2024
1.0
0.8
0.6
0.4
0.2
0.0
96 192 336 720
Prediction Length
egatnecreP
tnenopmoC
Trend
Seasonality
Residual
Error
Figure 14: The SHAP (SHapley Additive exPlanations) values of decomposed components of
TEMPOforweatherdataset.
Inourpaper,weusetheETTm1andweatherdatasetsasdetailedexamples. Thefullresultsused
tocalculatetheSHAPvaluecanbefoundatTable11. Indatasetsexhibitingstrongseasonality,the
seasonalcomponentmaydisplaymuchlargervariationsthantheresidualcomponent. Conversely,
indatasetswithminimalseasonality,thevariationsbetweenthesetwocomponentsshouldbemore
comparable. Wecancalculatethestrengthofseasonalityvia:
(cid:18) (cid:19)
Var(R )
S=max 0,1− t (7)
Var(S )+Var(R )
t t
Whenwecomparetheseasonalitystrengthsofdifferentdatasets,wefindthatETTm1(asshownin
Figure2,withaseasonalitystrengthof0.99)constitutesstronglyseasonaldata,whereastheweather
dataset(depictedinFigure14withaseasonalitystrengthof0.476)exhibitslessseasonalityanda
morepronouncedtrend. ThesefindingsalignwiththeconclusionsdrawnfromtheSHAPvalues.
TheperformancedegradationofETTm1,whenthepredictionlengthisincreased,canbeprimarily
attributedtoinaccuraciesinthepredictionofseasonalterms. Insummary,SHAPprovidespivotal
descriptivepowerformodeltransparency,movingbeyondintuition. Theabilitytodiscernhowmuch
andwherecomponentscontributeenablestargetedimprovements. Theseinsightscanguideusin
betterleveraginginductivebiastoenhancebothefficiencyandeffectivenessintheeraofpre-training
models. Oneoftheinterestingfutureworksisthatwecanadaptivelyandselectivelyoptimizespecific
componentsbasedontheGAMstructureandSHAPscoresduringthetrainingprocess.Thisapproach
wouldallowustofocusourcomputationalresourcesandeffortsonthemostinfluentialcomponents,
therebyimprovingtheoveralleffectivenessofthemodel.
F BASELINE MODEL EXPLANATIONS
Wedemonstratethebaselinemodelswecomparedwithinourexperimentsinthefollowing:
• DLinear(Zengetal.,2023): DLinearcombinesadecompositionschemefromAutoformer
andFEDformerwithlinearlayerstopredicttimeseriesdatabymodelingtrendandseasonal
componentsseparatelyandsummingtheirfeaturesforenhancedperformanceintrend-rich
datasets.
• PatchTST(Nieetal.,2023): PatchTSTisaTransformer-basedmodelformultivariatetime
seriesforecastingthatsegmentsdataintosubseriespatchesandusesachannel-independent
design to efficiently reduce computational costs while enhancing long-term prediction
accuracy.
27

PublishedasaconferencepaperatICLR2024
Table11: SHAPoriginalvaluesforeachcomponent
| w/otrend        | w/oseason   | w/oresidual | trend       | season      | residual emptyset       | completeset |
| --------------- | ----------- | ----------- | ----------- | ----------- | ----------------------- | ----------- |
| MSE/MAE         | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE     | MSE/MAE MSE/MAE         | MSE/MAE     |
| 96 0.437/0.432  | 0.670/0.526 | 0.457/0.441 | 0.663/0.541 | 0.472/0.455 | 0.680/0.535 1.104/0.790 | 0.438/0.424 |
| 192 0.466/0.447 | 0.646/0.518 | 0.488/0.455 | 0.682/0.529 | 0.483/0.455 | 0.666/0.526 1.101/0.789 | 0.461/0.432 |
ETTm1 336 0.505/0.466 0.672/0.530 0.526/0.476 0.680/0.531 0.524/0.475 0.707/0.543 1.102/0.790 0.515/0.467
| 720 0.579/0.507 | 0.678/0.549 | 0.586/0.508 | 0.684/0.548 | 0.592/0.509 | 0.709/0.558 1.105/0.794 | 0.591/0.509 |
| --------------- | ----------- | ----------- | ----------- | ----------- | ----------------------- | ----------- |
| Avg 0.497/0.463 | 0.666/0.531 | 0.514/0.470 | 0.677/0.537 | 0.518/0.474 | 0.691/0.540 1.103/0.791 | 0.501/0.458 |
| 96 0.213/0.267  | 0.202/0.261 | 0.205/0.264 | 0.223/0.289 | 0.234/0.293 | 0.220/0.284 0.637/0.608 | 0.211/0.254 |
| 192 0.266/0.317 | 0.251/0.297 | 0.256/0.306 | 0.254/0.304 | 0.290/0.335 | 0.262/0.316 0.638/0.608 | 0.254/0.298 |
Weather 336 0.317/0.356 0.290/0.333 0.295/0.331 0.293/0.331 0.328/0.357 0.313/0.356 0.640/0.609 0.292/0.332
| 720 0.402/0.401 | 0.371/0.383 | 0.377/0.380 | 0.364/0.378 | 0.389/0.393 | 0.385/0.398 0.638/0.610 | 0.370/0.379 |
| --------------- | ----------- | ----------- | ----------- | ----------- | ----------------------- | ----------- |
| Avg 0.300/0.335 | 0.279/0.318 | 0.283/0.320 | 0.283/0.325 | 0.310/0.345 | 0.295/0.339 0.638/0.609 | 0.282/0.316 |
• FEDformer (Zhouetal.,2022): FEDformercombinesseasonal-trenddecompositionwith
Transformersfortimeseriesforecasting,leveragingfrequencyinsightsforefficiencyand
accuracy,outperformingstate-of-the-artmethods.
• Informer (Zhouetal.,2021): Informerisatransformer-basedmodeloptimizedforlong
sequencetime-seriesforecasting,leveragingProbSparseself-attentionforefficiency,self-
attentiondistillingforhandlinglonginputs,andagenerativedecoderforrapidpredictions.
• ETSformer (Wooetal.,2022): ETSformerisanovelTransformerarchitecturefortime-
series forecasting that integrates exponential smoothing principles, replacing traditional
self-attention with exponential smoothing attention and frequency attention, to enhance
accuracy,efficiency,andinterpretability.
• TimesNet(Wuetal.,2023): TimesNettransforms1Dtimeseriesinto2Dtensorscapturing
intra-andinter-periodvariationsandusesTimesBlockwithaninceptionblocktoextract
complextemporalpatterns,excellinginmultipletimeseriestasks.
• GPT-2 (Radford et al., 2019): GPT-2 is a decoder-based language model developed by
OpenAI,designedtogeneratecoherentanddiversetextualcontentfromagivenprompt. In
ourwork,weusetheGPT-2with6layersasthebackbone,whichisadaptedfromGPT4TS
(Zhouetal.,2023).
• BERT (Devlinetal.,2019): BERT(BidirectionalEncoderRepresentationsfromTrans-
formers)isanencoder-baseddeeplearningmodelutilizingtheTransformerarchitecture
designed by Google to understand the context of words in a sentence by analyzing text
bi-directionally.
• T5 (Raffeletal.,2020): T5(Text-to-TextTransferTransformer)isastate-of-the-artneural
networkmodelwithencoder-decoderbasedarchitecturedesignedbyGooglethatconverts
everylanguageproblemintoatext-to-textformat.
• LLaMA (Touvronetal.,2023):LLaMA(LargeLangaugeModelMetaAI)isacollectionof
state-of-the-artfoundationlanguagemodelsrangingfrom7Bto65Bparametersdelivering
exceptionalperformance,whilesignificantlyreducingtheneededcomputationalpowerand
resources. Inourwork,weusethefirst6layersof7BLLaMA.
G THEORICAL
ANALYSIS
| G.1 PROOFOFTHEOREM | 3.1 |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- |
TheoremG.1 Suppose that we have time series signal Y(t) = S(t)+T(t)+R(t),t ∈ [t ,t ],
1 n
whereS(t)istheseasonalsignal(periodical),T(t)isthetrendsignal(non-periodical)andR(t)is
theresidualsignal. LetE ={e ,e ,...,e }denoteasetoforthogonalbases. LetE ⊆E denote
|     |     | 1 2 | n   |     |     | S   |
| --- | --- | --- | --- | --- | --- | --- |
thesubsetofE onwhichS(t)hasnon-zeroeigenvaluesandE ⊆ E denotethesubsetofE on
|     |     |     |     |     | T (cid:80)n |     |
| --- | --- | --- | --- | --- | ----------- | --- |
whichT(t)hasnon-zeroeigenvalues. IfS(t)andT(t)arenotorthogonal,i.e. S(t )T(t )̸=0,
i=1 i i
thenE ∩E ̸=∅,i.e. E cannotdisentanglethetwosignalsontotwodisjointsetsofbases.
T S
28

PublishedasaconferencepaperatICLR2024
|     |     |     |     |     |     |     |     |     | (cid:80) |     | (cid:80) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- |
Proof1 WedecomposeS(t)andT(t)ontoE andacquirethatS(t)= a e andT(t)= b e .
|     |     |     |     |     |     |     |     |     |     | i i | i i |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thenitisobviousthate ∈E ⇐⇒ a ̸=0ande ∈E ⇐⇒ b ̸=0. Now,letusconsiderthe
|     |     |     | i   | S   | i   |     | i T |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
innerproductofS(t)andT(t):
n
|     |     | (cid:88) |      |               |     | (cid:88) |         | (cid:88) | (cid:88) |         |     |
| --- | --- | -------- | ---- | ------------- | --- | -------- | ------- | -------- | -------- | ------- | --- |
|     |     | S(t      | )T(t | )=S(t)·T(t)=( |     |          | a e )·( | b e      | )=       | a b e e | (8) |
|     |     |          | i    | i             |     |          | i i     | i        | i        | i j i j |     |
|     |     | i=1      |      |               |     |          |         |          |          | i,j     |     |
NotethatthecomponentsfoundbyPCAisasetoforthogonalbasis. Thus,foranyi̸=j,wehave
| e e | =0. Thus,wehave: |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i j
n
|     |     | (cid:88) |        |                 |     | (cid:88) | (cid:88)    |       | (cid:88) | ||2           |     |
| --- | --- | -------- | ------ | --------------- | --- | -------- | ----------- | ----- | -------- | ------------- | --- |
|     |     | S(t      | i )T(t | i )=S(t)·T(t)=( |     |          | a i e i )·( | b i e | i )=     | a i b i ||e i | (9) |
2
|     |     | i=1 |     |     |     |     |     |     |     | i   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:80)n
Notethat S(t )T(t )=0. Thus,theremustbeatleastoneisuchthata ̸=0andb ̸=0. Thus,
|      |      | i=1 | i i             |     |     |     |      |     |     | i i |     |
| ---- | ---- | --- | --------------- | --- | --- | --- | ---- | --- | --- | --- | --- |
| e ∈E | ande | ∈E  | ,inotherwords,E |     |     | ∩E  | ̸=∅. |     |     |     |     |
| i    | S    | i   | T               |     | T   | S   |      |     |     |     |     |
TheabovetheoremprovesthatifT(t)andS(t)arenotorthogonal,thentheredoesnotexistaset
oforthogonalbasesthatdisentangleS(t)andT(t)ontotwodisjointsetsofbases. Notethatitis
common that a periodical signal is not orthogonal with a non-periodical signal. This is because
thespectrumofaperiodicalsignalisdiscreteandthespectrumofaperiodicalsignaliscontinuous.
Thus,itisverylikelythatthereexistoverlapsonthosenon-zerofrequenciesoftheperiodicalsignal.
NotethatPCAalsoaimsatlearningasetoforthogonalbasesonthedata. Wecanquicklyacquire
a corollary that PCA can not disentangle the two signals into two disjoint sets of bases. Based
on (Zhouetal.,2023)’sTheorem1,wecanrevealthatself-attentioninpre-trainedlargemodels
learnstoperformafunctioncloselyrelatedtoPCA.Therefore,theself-attentionmechanismcannot
automaticallydecomposethetimeseriesintoitstrendandseasonalcomponentsunlesswemanually
performthisoperation.
G.2 INTERPRETINGMODELPREDICTIONSFROMFREQUENCYDOMAIN
InadditiontoSection5.2,whichgivesanexperimentalperspectiveonwhydecompositioncanaid
forecastingresults,weprovideatheoreticalanalysisfromthespectraldomain. Specifically,time
seriessignalscanberepresentedasacombinationofdifferentfrequenciesinthespectraldomain.
Forecastingischallengingbecausereal-worldseriescomprisesconvolutedmixturesofvariations
with overlapping periodicities. However, by shifting our view to the frequency domain, we can
identifydistinctcomponentsviaSTLdecompositioncontainingisolatedfrequenciesthatstandout
clearlyfromtherestofthespectrum. Thisseparationofdominantperiodicpatternsiscrucialbecause
forecastingfuturevaluesequatestopredictinghowtheseunderlyingfrequenciesevolveovertime:
PropositionG.2(Equivalenceoftimedomainforecastingandfrequencydomainforecasting)
Assumex ,x ,...,x andxˆ ,xˆ ...,xˆ ,xˆ aretheinputandoutputsequencesofthefrequency
|     | 0   | 1   | N−1 | 0   | 1 N−1 | N   |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
model. Then,xˆ transferredfromthefrequencydomainisthepredictedvalueattimestampN.
N
Giveninputsequence{x |t = 0,1,...,N −1},whereN isthenumberofdiscretetimestamps,in
t
thetimedomain,theDiscreteFourierTransform(DFT,F)andinverseDiscreteFourierTransform
(iDFT,f)operationtoobtainthefrequencydomaincanbedefinedas:
N−1
|     |     |     |       | 1   | (cid:88) | −i2πux |              |     |     |     |      |
| --- | --- | --- | ----- | --- | -------- | ------ | ------------ | --- | --- | --- | ---- |
|     |     |     | F(u)= |     | f(x)e    |        | ,u=0,1,...,N |     | −1, |     | (10) |
|     |     |     |       | N   |          |        | N            |     |     |     |      |
x=0
N−1
(cid:88)
|     |     |     |     | f(x)= | F(u)ei2π |     | ux,x=0,1,...,N |     | −1. |     | (11) |
| --- | --- | --- | --- | ----- | -------- | --- | -------------- | --- | --- | --- | ---- |
N
u=0
AccordingtoPropositionG.2, assumingthatthenextvalueofF(u), canbepredictedasF′(N),
otherunknownvariablesinthetimeandfrequencydomains,includingthe(N +1)thdiscretesample
f(N)andthenewDFT’sresultF′(u),u=0,1,2,...,N −1aredeterminedbythegivenF′(N).
29

PublishedasaconferencepaperatICLR2024
Proof2 Let
|     |     |     | N −1     | e−i2π ux | e−i 2π u x |     |      |
| --- | --- | --- | -------- | -------- | ---------- | --- | ---- |
|     |     |     | (cid:88) | N        | N + 1      |     |      |
|     |     | A=  | f(x)(    |          | − ),       |     | (12) |
|     |     |     |          | N        | N +1       |     |      |
x=0
N−1
|     |     |     | 1   | (cid:88) f(x)e−i2 | π N x, |     |      |
| --- | --- | --- | --- | ----------------- | ------ | --- | ---- |
|     |     |     | B = |                   | N + 1  |     | (13) |
N +1
x=0
thenwehave:
2
|     |     | f(N)=(N            | +1)(F′(N)−B)e−i2 |     | π N ,          |     |      |
| --- | --- | ------------------ | ---------------- | --- | -------------- | --- | ---- |
|     |     |                    |                  |     | N + 1          |     | (14) |
|     |     | F′(u)=A+(F′(N)−B)e |                  |     | i2π( N − u)N . |     | (15) |
N + 1
| Foru=0,1,2,...,N | −1,thevalueofF′(u)−F(u)canberepresentedas: |               |     |     |                 |     |      |
| ---------------- | ------------------------------------------ | ------------- | --- | --- | --------------- | --- | ---- |
|                  |                                            |               |     | 1   | f(N)e−i2 π u N. |     |      |
|                  |                                            | F′(u)−F(u)=A+ |     |     | N + 1           |     | (16) |
N +1
Foru=N,thevalueofF′(N)canberepresentedas
|     |     |     |          | 1        | 2   |     |      |
| --- | --- | --- | -------- | -------- | --- | --- | ---- |
|     |     |     | F′(N)=B+ | f(N)e−i2 | π N |     | (17) |
N + 1
N +1
.
GivenF′(N),wecaninferenceF′(u)by:
i2π( N − u)N
|     | F′(u)=A+(F′(N)−B)e |     |     | N + 1 | ,u=0,1,2,...,N | −1. | (18) |
| --- | ------------------ | --- | --- | ----- | -------------- | --- | ---- |
andf(N)by:
|     |     |         | +1)(F′(N)−B)e−i2 |     | π N 2   |     |      |
| --- | --- | ------- | ---------------- | --- | ------- | --- | ---- |
|     |     | f(N)=(N |                  |     | N + 1 , |     | (19) |
Thus,theonlyvariablethatneedstobepredictedisF′(N).
Thispropositionrevealsthatifitiseasytopredictpatternsinthefrequencydomain,wecanmore
easily predict the time series’ future values. Forecasting equates to predicting the evolution of
theunderlyingfrequenciesthatmakeupthetimeseriessignal. STLdecompositionsignificantly
aidsthistaskbyseparatingcomponentswithdistinctdominantperiodicpatterns. WithSTL,each
componentpresentsfarfewerintertwiningperiodicinfluencestodisentangle,whichnotablysimplifies
the prediction problem. For instance, the trend component may exhibit a lone annual cycle that
clearlydominatesitsspectrum. Atargetedpredictivemodelfocusingsolelyonaccuratelyestimating
theprogressionofthisisolatedfrequencycangenerateaccurateforecasts. Likewise,theseasonal
elementneatlyisolatesrecurringdailyorweeklyfrequencies. Modelstailoredspecificallyforthese
knownperiodicitiesallowforhighlypredictableextrapolations. Incontrast,directlymodelingthe
rawdata’scondensedspectrumwithnumerousblendedperiodiccomponentsyieldsunsatisfactory
approximations. Theoverlappingfrequenciesaredifficulttodistinguishandpredictindependently.
ConceptualizingforecastingthroughafrequencydomainlensrevealshowSTLdecomposescomplex
spectralmixturesintodistinguishablefrequency-basedsub-problems. Thisallowsimplementation
optimizedpredictivestrategiestouncoverpatternsineachcomponentformarkedlyimprovedtime
seriespredictions. Inessence,STLfacilitatesaccuratefuturepredictionsbydisentanglingthespectral
contentintosimplerpredictableforms.
| H DETAIL | OF THE | TETS | DATASET |     |     |     |     |
| -------- | ------ | ---- | ------- | --- | --- | --- | --- |
Time series data Analyzing and forecasting a company’s future profitability and viability are
essential for its development and investment strategies. Financial assessment and prediction are
data-driven,mostlyrelyingonthecombinationofdiversedatatypesincludingcompanyreports,etc.
Inthisproject,ourprimarysourcesarethecompany’sfinancialstatements: balancedsheet,income
statements,andcashflowstatements.
The Standard & Poor’s 500 Index (S&P 500) represents a stock market index that measures the
stockperformanceofthe500largestcompaniesintheU.S.11sectorsintheS&P500areincluded
30

PublishedasaconferencepaperatICLR2024
inourdataset: BasicMaterials(21companies),CommunicationServices(26companies),Energy
(22 companies), Financial Services (69 companies), Healthcare (65 companies), Technology (71
companies),Utilities(30companies),ConsumerCyclical(58companies),ConsumerDefensive(36
companies),Industrials(73companies),RealEstate(32companies). Intermsofdatasetdivision,we
separatethesectorsinourdatasettoachievebothin-domaintasksettingandzero-shottasksetting.
Thefirstsevensectorsaretreatedastrainingandevaluationsectors,whilethelastfoursectorsare
reservedasunseensectorsforzero-shotforecastingtask.
ToaddressmissingnumericalinformationforcompaniesintheS&P500thatlackdatapriorto2010,
weapplylinearinterpolationafterexperimentingwithvariousmethods. Linearinterpolationisa
techniquethatestimatesavaluewithinarangeusingtwoknownend-pointvalues. Formissingvalues
inresearchanddevelopmentexpenses,weadoptedazero-fillingstrategy. Thisisbecausenullentries
inthesestatementstypicallyindicatethatthecompanydidnotmakeanyinvestmentinthatarea.
Contextual data collection This rise of Large-scale pre-trained models (LLMs) in the field of
NaturalLangaugeProcessinghasprovidednewpossibilitiesfortheirapplicationintimeserisanalysis.
LLMshaveprovenusefulforanalyzingandlearningcomplicatedrelationshipsandmakinginferences
acrossdifferenttimeseriessequences. However,mostexistingapproachesprimarilyconverttime
seriesdatatodirectinputintoLLMs,overlookingthefactthattheLLMsarepre-trainedspecifically
fornaturallanguageandthusneglectingtheincorporationofcontextualdata.
Further,theinformationcontainedintimeseriesdataislimited,especiallyinthefinancialfield. Time
seriesdatainthefinancialfield,suchascompanystatements,primarilyreflectthefinancialnumeric
changesbasedonthecompany’shistoricalstrategyandbroadermacroeconomicshifts. Thesedata
containthecompany’sinternalhistoricalinformation. However,thebroadermarketenvironment,
referredtoasexternalinformation,alsoplaysanimportantroleinthecompany’sfuturedevelopment.
Forexample,medicineandhealthcarecompaniesexperiencedsteadygrowthbeforetheoutbreakof
COVID-19. Butbetween2019and2020,aftertheoutbreakofthepandemic,thefinancialstatements
ofsuchcompanieswereimpactedsignificantly. Asaresult,werecognizethevalueofintegrating
news and reports as external data sources to complement internal information contained in time
seriesdata. Theinformationcontainedintheexternaldatamainlyincludes3parts: (i). Policyshifts
acrossregions(ii). Significanteventsoccurringglobally(iii). Publicreactiontocompanies’products.
Together,theseelementsprovidesupplementaryinformationmissingintimeseriesdata(internal
data),thereforeenhancingourforecastingcapabilities.
Extracting contextual data, such as news and reports, from varied sources presents a significant
challenge. Intoday’sdigitalage,numerousnewswebsitesandappsdeliverawiderangeofworld
news,spanningfrominfluentialnewsaffectingentireindustriestotrivial,minorreports. Thus,itis
crucialtofilterandsummarizetheinformation,distinguishingbetweenpivotalandlesssignificant
news. Fortunately,therecentlyreleasedChatGPTAPI2byOpenAIoffersthecapabilityofcollecting
andsummarizingnewsandreportsforaspecifiedduration.
Throughconsolidatingallrelevantdetails–query, quarter, yearlycontext, companyinformation,
andspecificrequirements–intousermessageandsettingacapat110tokensforresponse,wecan
efficientlyobtainthedesiredcontextualinformationfromChatGPTAPI.Forillustration,Figure 10
displaysanexamplefromcompanyA,showcasingdesignedpromptsandcorrespondingresponses
fromChatGPT3.5.Ifthecontextualinformationcannotbegenerated,theAPIoftenreturnsmessages
withkeywordssuchas’unfortunately’and’sorry’. Wedetectandreplacethemwiththeterm’None’,
representingneutralcontextualinformation. Additionally,Figure 15and 17provideaillustrationof
ourdataset,encompassingbothtimeseriesdataandthecorrespondingcontextualtexts. Adetailed
viewofthecontextualtextscanbeseeninFigure 16and 18.
2https://platform.openai.com/docs/guides/gpt
31

PublishedasaconferencepaperatICLR2024
Figure15: EBITDAforCompanyAwithcontextualinformation
Company A reported a net profit of $32 million, its highest third-quarter profit in four 1
years, and released its new Product M.
2002 third quarter
In the second quarter of 2005, Company A's profits rose 425%, with Product P sales 2
accounting for most of the increase. The company also announced plans to start using I
technique in their computers. 2005 second quarter
3
In the fourth quarter of 2007, Company A announced record-breaking sales of over 2
million Product S, and also launched their revamped line of Product N.
2007 fourth quarter
In the first quarter of 2009, Company A reported a 1% decline in sales and a 17% drop in
4
profits compared to the same period in the previous year, citing the global economic
downturn as a contributing factor. The company also announced the release of the U
technique software and the new Product IS. 2008 first quarter
Figure16: ExampleofgeneratedcontextualinformationforCompanyAmarkedinFigure15
Figure17: EBITDAforCompanyBwithcontextualinformatino
32

PublishedasaconferencepaperatICLR2024
Company B reported fourth-quarter earnings of $189 million, supported by continued  1
growth in its electronics unit. The company also announced plans to acquire the
company C for $143 million
2006 fourth quarter
Company B reported a net income of $0.95 per share for Q4 of 2008, down from $1.21  2
per share in the same quarter of the previous year. The company also experienced a
decrease in sales due to the economic recession. 2008 fourth quarter
In 2012's third quarter, Company B reported weaker-than-expected earnings due to a
3
decline in its business, but it still projected higher sales and profits for the year. The
company also announced plans to expand its production facilities D in Russia. 2012 third quarter
In 4Q 2012, Company B reported a net income of $138.7 million, down from $289.3  4
million in the same quarter of 2011; the company's revenue also decreased by 6.2% to
$2.56 billion. 2012 fourth quarter
Figure18: ExampleofgeneratedcontextualinformationforCompanyBmarkedinFigure17
| Table12: | TableofMainNotationonTEMPO |     |
| -------- | -------------------------- | --- |
Notation Description
| xˆi | ithchannelpredictionattimestept |     |
| --- | ------------------------------- | --- |
t
| xi  | ithchannellookbackwindow/historicalvaluesattimestept |     |
| --- | ---------------------------------------------------- | --- |
t
Φ modelparameter
V promptvaluefrompromptpool
| X   | inputdatawhichcanbedecomposedintoX | X X |
| --- | ---------------------------------- | --- |
T S R
| X ,X ,X | trend,season,residualcomponentsetintimet |     |
| ------- | ---------------------------------------- | --- |
Tt St Rt
xi ithchanneltthtimestepofxi
| Tt  |     | T   |
| --- | --- | --- |
xˆi
| Tt  | predictvalueoftrendcomponent |     |
| --- | ---------------------------- | --- |
P patchofinputdata
mthkeyinpromptpool
k m
mthvalueinpromptpool
V m
V promptpool
k
| K   | hyperparameter,numberofpromptstochoose |     |
| --- | -------------------------------------- | --- |
| M   | hyperparameter,lengthofpromptpool      |     |
| Z∗  | GPToutputfor*(trend,seasonal,residual) |     |
L predictionlength
H
L embeddingvectorlength
E
| Y   | finalpredictvaluebeforede-normalization |     |
| --- | --------------------------------------- | --- |
∗
Yˆ finalpredictvalue
∗
33