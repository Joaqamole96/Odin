Conv-FinRe: A Conversational and Longitudinal Benchmark for
Utility-Grounded Financial Recommendation
YanWang YiHan LingfeiQian∗ YueruHe XueqingPeng∗
TheFinAI GeorgiaInstituteof TheFinAI ColumbiaUniversity TheFinAI
USA Technology USA USA USA
wy2266336@gmail.com USA lingfei.qian@yale.edu xueqing.peng@yale.edu
DongjiFeng∗ ZhuohanXie VincentJim RosieGuo FengranMo
CaliforniaState MBZUAI Zhang TheFinAI UniversityofMontreal
University UAE TheFinAI USA Canada
USA USA
dfeng@csumb.edu
JiminHuang YankaiChen∗ Xue(Steve)Liu Jian-YunNie
TheUniversityof McGillUniversity McGillUniversity UniversityofMontreal
Manchester MBZUAI MBZUAI Canada
Manchester,United Canada Canada
yankaichan3@gmail.com
Kingdom
TheFinAI
USA
Abstract
canoverfitshort-termnoise.Thedatasetispubliclyreleasedon
Mostrecommendationbenchmarksevaluatehowwellamodelimi-
HuggingFace1,andthecodebaseisavailableonGitHub2.
tatesuserbehavior.Infinancialadvisory,however,observedactions
CCSConcepts
canbenoisyorshort-sightedundermarketvolatilityandmaycon-
flictwithauser’slong-termgoals.Treatingwhatuserschoseasthe •Informationsystems→Recommendersystems;Similarity
solegroundtruth,therefore,conflatesbehavioralimitationwith measures;Languagemodels;•Human-centeredcomputing
decisionquality.WeintroduceConv-FinRe,aconversationaland →Usercentereddesign;•Computingmethodologies→Nat-
longitudinalbenchmarkforstockrecommendationthatevaluates urallanguageprocessing.
LLMsbeyondbehaviormatching.Givenanonboardinginterview,
Keywords
step-wisemarketcontext,andadvisorydialogues,modelsmust
generaterankingsoverafixedinvestmenthorizon.Crucially,Conv- PersonalityStockRecommendation,ConversationalBenchmark,
FinReprovidesmulti-viewreferencesthatdistinguishdescriptive UtilityFunction,Rerank,LargeLanguageModels
behaviorfromnormativeutilitygroundedininvestor-specificrisk
ACMReferenceFormat:
preferences,enablingdiagnosisofwhetheranLLMfollowsrational
YanWang,YiHan,LingfeiQian,YueruHe,XueqingPeng,DongjiFeng,
analysis,mimicsusernoise,orisdrivenbymarketmomentum.
ZhuohanXie,VincentJimZhang,RosieGuo,FengranMo,JiminHuang,
We build the benchmark from real market data and human de-
YankaiChen,Xue(Steve)Liu,andJian-YunNie.2018.Conv-FinRe:ACon-
cisiontrajectories,instantiatecontrolledadvisoryconversations, versationalandLongitudinalBenchmarkforUtility-GroundedFinancial
andevaluateasuiteofstate-of-the-artLLMs.Resultsrevealaper- Recommendation.InProceedingsofMakesuretoenterthecorrectconference
sistenttensionbetweenrationaldecisionqualityandbehavioral titlefromyourrightsconfirmationemail(Conferenceacronym’XX).ACM,
alignment:modelsthatperformwellonutility-basedrankingoften NewYork,NY,USA,8pages.https://doi.org/XXXXXXX.XXXXXXX
failtomatchuserchoices,whereasbehaviorallyalignedmodels
1 Introduction
Largelanguagemodels(LLMs)haveachievedremarkableprogress
∗Correspondingauthors.
acrossdiverseapplicationdomains,demonstratingstrongperfor-
manceinlanguageunderstanding[24,43],reasoning[25,44],and
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor structuredproblem-solving[39,40].Thesecapabilitieshavemoti-
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed vatedtheiradoptionasassistantsfordecision-makingandrecom-
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe mendationtasks[7,9,15,18,19].Inmostrecommendationbench-
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or marks,personalizationisprimarilymeasuredbybehavioralimita-
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
tion:arecommendationisdeemedcorrectifitmatcheswhatauser
and/orafee.Requestpermissionsfrompermissions@acm.org.
Conferenceacronym’XX,Woodstock,NY wouldclick,rate,orchoose[6,14,16,28].Thisbehavior-centric
©2018Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ACMISBN978-1-4503-XXXX-X/2018/06 1https://huggingface.co/collections/TheFinAI/conv-finre
https://doi.org/XXXXXXX.XXXXXXX 2https://github.com/The-FinAI/Conv-FinRe
6202
yaM
71
]IA.sc[
2v09961.2062:viXra

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Yanetal.
Table 1: Comparison of representative user-centric
modelstendtooverfitnoisyuseractions,mistakingtransientbehav-
recommendation benchmarks. Dynamic indicates time- iorforstablepreferences.Together,theseresultsmotivateConv-
conditioned signals; Utility refers to relevance grounded FinReasabenchmarkformulti-view,utility-groundedevaluation.
inauser-dependentdecisionutility;Multi-view indicates
Wemakethefollowingcontributions:(1)WeintroduceConv-
multiple, potentially conflicting ranking views; Dialogue FinRe,aconversationalandlongitudinalbenchmarkforstockrec-
denotesaconversationalinteractivesetting.
ommendationthatevaluatesLLMsbeyondbehavioralimitationby
Work Domain Dynamic Utility Multi-view Dialogue groundingassessmentininvestor-specificutility.(2)Weformulate
REASONER[6] Video (cid:37) (cid:37) (cid:37) (cid:37) financialrecommendationevaluationasamulti-viewalignment
FairEval[28] Music (cid:37) (cid:37) (cid:37) (cid:37) problemandprovideadiagnosticframework,supportedbyinverse
PerFairX[27] Movie&Music (cid:37) (cid:37) (cid:37) (cid:37) optimization,thatdisentanglesbehavioralalignmentfromrational
CEREAL[14] Movie (cid:37) (cid:37) (cid:37) (cid:34) decisionquality.(3)Weconductasystematicevaluationofstate-
LLM-REDIAL[16] Movie (cid:37) (cid:37) (cid:37) (cid:34) of-the-artLLMsunderConv-FinRe,identifyingdistinctadvisory
RecBench[18] General (cid:37) (cid:37) (cid:37) (cid:37)
FAR-Trans[29] Finance (cid:34) (cid:37) (cid:37) (cid:37) behaviorpatternsundercompetingmarketsignalsandusernoise.
Ours Finance (cid:34) (cid:34) (cid:34) (cid:34) 2 RelatedWorks
paradigmiseffectiveinmanyconsumerdomains,wherefeedback Personalizedrecommendationbenchmarksarewellstudiedincon-
isareliableproxyforutility. sumerdomainssuchase-commerceandmedia,wherepersonal-
Financialrecommendationisdifferent.Investoractionsareoften izationistypicallymodeledfrominteractionhistoriesorcoarse
affectedbyshort-termmarketnoise,emotions,andshiftingcon- usertraitsandsupervisionreliesonasinglerelevancesignallike
straints,andmaydeviatefromstablerisktoleranceorlong-term ratingsorclicks[6,42].Recentworkenrichesthissettingbyintro-
objectives[1,22].Asaresult,matchinghistoricalchoicesalone ducingstructuredexplanations[6]andbyevaluatingLLMseither
cannottellwhetheranadvisorisprovidinggoodfinancialguidance. asrepresentationenhancersorasend-to-endrecommendersun-
Afaithfulmimicofnoisyactionsmaybemisalignedwiththeuser’s derpoint-wise,pair-wise,orlist-wiseprotocols[7,9,18,19],with
underlyinggoals,whileapurelyrationaladvisormayignoreuser furtheranalysisoffairness,bias,andsequentialalignment[17,28].
intentandpreferences. Incontrast,personalizedstockrecommendationposesadditional
Existingbenchmarks,assummarizedinTable1,thereforestrug- challenges due to non-stationary assets and investor objectives
glewiththreeissues:behavior-as-truth,utilityblindness,andsingle- constrainedbyrisktoleranceandreturn–risktrade-offs[29,34],
viewevaluation.Mostuser-centricbenchmarksrelyonrelevance withevidencethatriskpreferencesevolveandmustbeinferred
signals(clicks/ratings)[6,18]withoututilitygrounding,whilefi- frombehaviorratherthanstaticprofiles[5].Whileconversational
nancedatasetsoftenemphasizepredictionortradingobjectives andLLM-basedfinancialadvisorsenableiterativepreferenceelici-
ratherthanuser-specificdecisionquality[29].Consequently,they tation[10,23,30,33,35,36],existingbenchmarksrarelyevaluate
cannotdiagnosewhetheranLLMadvisorisreasoningaboutrisk- recommendationqualityusinginvestor-specificutilityasthecore
sensitiveutility,blindlychasingmarkettrends,orsimplyoverfitting supervision signal, limiting their ability to assess true decision
usernoise. alignment.
Toaddressthisgap,weintroduceConv-FinRe,thefirstcon-
3 Conv-FinRe
versationalandlongitudinalbenchmarkthatformulatesfinancial
recommendationasamulti-viewalignmentproblem.Ratherthan Figure1illustratestheoverallpipelineofConv-FinRe,fromdata
evaluatingwhetheranLLMsimplymatchesuserchoices,thebench- collectionanduserprofilingtomulti-viewconversationsimulation
markassessesmodelrankingsagainstfourcomplementaryrefer- andevaluation.Theframeworkmodelslongitudinaladvisoryinter-
enceviews,suchasuserchoice(𝑦 𝑢𝑠𝑒𝑟),rationalutility(𝑦 𝑢𝑡𝑖𝑙),market actionsbyintegratingmarketsignals,inferreduserpreferences,and
momentum(𝑦 𝑚𝑜𝑚),andrisksensitivity(𝑦 𝑠𝑎𝑓𝑒),enablingdiagnosis competingexpertrecommendations,enablingfine-grainedanalysis
ofwhetheramodelreliesonrationalanalysis,behavioralimitation, ofLLMalignmentinpersonalizedfinancialdecision-making.
orshort-termmarketsignals.Tosupportsuchevaluation,user-
specificriskpreferencesareinferredfromlongitudinaldecision 3.1 TaskFormulation
trajectoriesviainverseoptimizationandusedtoconstructutility-
WedefinetheMulti-viewLongitudinalStockRecommenda-
andrisk-basedreferencerankings,withoutexposingthelatentutil-
tiontask,whichsimulatesiterativeinteractionsbetweenaper-
ityfunctiontothemodel.Operationally,Conv-FinReinstantiates
sonalizedinvestmentadvisorandauseroverafixedinvestment
thetaskthroughonboardinginterviewsandstep-wiseadvisory
horizon𝑇.Unlikeconventionalrecommendationbenchmarksthat
dialogues,whereanLLMmustreconcilecompetingadvisoryprin-
relyonasingle"gold-standard"label,ourtaskevaluatesLLMalign-
ciplesovertime.
mentacrossfourcomplementaryreferenceviews:UserChoice
Weevaluateadiversesetofstate-of-the-artLLMsunderConv-
FinRe and reveal a fundamental tension between rational deci-
(𝑦
𝑢𝑠𝑒𝑟
),representingtheempiricalselectionsmadebythehuman
sionqualityandbehavioralalignment.Whilesomemodelsachieve
participant;RationalUtility(𝑦
𝑢𝑡𝑖𝑙
),anidealizedrankingderived
fromacalibratedutilityfunctionthatrepresentsthetheoretically
strongutility-basedrankings,theyoftenconflatelong-termrisk
optimalbalancebetweenreturnandrisk;MarketMomentum
withshort-termmarketmomentum;conversely,domain-specialized
(𝑦
𝑚𝑜𝑚
),aprofit-orientedrankingbasedpurelyonrecentcumulative
returns;andRiskSensitivity(𝑦
𝑠𝑎𝑓𝑒
),aconservativerankingthat

Conv-FinRe:AConversationalandLongitudinalBenchmarkforUtility-GroundedFinancialRecommendation Conferenceacronym’XX,June03–05,2018,Woodstock,NY
|     |     |     |     |     | 3.2 | LatentPreferenceGroundingviaInverse |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
Optimization
Thetaskitselfdoesnotassumeaccesstotheuser’strueutilityfunc-
tion.Instead,toenableprincipledanalysisofadvisorybehaviors,
weconstructalatentpreferencesignalthatservesasareference
representationofeachuser’sunderlyingriskattitude.Thisprefer-
encesignalisusedtocharacterizeadvisoryobjectiveswithinthe
benchmark,ratherthanbeingexposedtothemodel.
Weassumethatuser𝑖’sdecision-makingprocessisgoverned
byalatentutilityfunction𝑈(𝑠)
,whichbalancesexpectedreturn
𝑖,𝑡
againstvolatilityanddownsiderisk[20,26,38].Foruser𝑖andstock
|     |     |     |     |     | 𝑠   | atstep𝑡,theutilityisdefinedas: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
∈S𝑡
𝑠)
|     |     |     |     |     |                |     | 𝑈 (                  | =𝜇˜𝑠,𝑡 | −𝜆 𝜎˜𝑠 2 −𝛾 𝑖Draw˜down𝑠,𝑡       |     | ,   | (3) |
| --- | --- | --- | --- | --- | -------------- | --- | -------------------- | ------ | ------------------------------- | --- | --- | --- |
|     |     |     |     |     |                |     | 𝑖 ,𝑡                 |        | 𝑖 ,𝑡                            |     |     |     |
|     |     |     |     |     | where𝜇˜𝑠,𝑡,𝜎˜𝑠 |     | 2 ,𝑡,andDraw˜down𝑠,𝑡 |        | denotethecross-sectionallystan- |     |     |     |
Figure1:OverviewofConv-FinRebenchmark.
dardizedmeanreturn,variance,andmaximumdrawdownofstock
|     |     |     |     |     | 𝑠overa7-daywindowprecedingstep𝑡.(𝜆 |     |     |     |     | ,𝛾  |     |     |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
𝑖 𝑖)aretheuser-specific
isolatestheuser’sspecificrisk-avoidancecomponentbypenalizing
parameters,whichareassumedtobetime-invariantandcapture
volatilityanddownsideriskaccordingtotheirinferredsensitivity.
theuser’ssensitivitytovolatilityanddownsiderisk.
Inthissetting,theLLMactsasaPersonalizedInvestment
|                                                           |     |     |     |     |     | We estimate | (𝜆  | ,𝛾 𝑖) via | Inverse Optimization |     | [3, | 4] using the |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --------- | -------------------- | --- | --- | ------------ |
| Advisorwhoseobjectiveisnotexplicitlyspecified.Instead,the |     |     |     |     |     |             |     | 𝑖         |                      |     |     |              |
user’slongitudinalbehavioraltrajectory𝐻𝑖
1:𝑇 .Assumingaratio-
modelmustinfertheuser’slatentfinancialpreferencesovertime
nalchoicemodelwithGumbel-distributednoise,theprobability
andreconcileconflictingadvisoryprinciples.Ateachdecisionstep, thatuser𝑖 selectsstock𝑠∗ atstep𝑡
followsaMultinomialLogit
themodelispresentedwiththecurrentmarketcontext,historical
model[32]:
interactiontrajectory,andrecommendationsfromapanelofthree
specializedadvisorsgroundedin𝑦 𝑢𝑡𝑖𝑙,𝑦 𝑚𝑜𝑚,and𝑦 (cid:16) (cid:17)
|     |     |     | 𝑠𝑎𝑓𝑒.Thecore |     |     |     |     |     |     | 𝑈(𝑠∗) |     |     |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     |     |     |              |     |     |     |     |     | exp | 𝑖,𝑡   |     |     |
c ha l l en ge fo r t h e L L M i s to s y n t h e s iz e t h e s e h e te ro g e n e o u s si g n a ls 𝑃(𝑠∗ |𝜆 ,𝛾 ,M𝑡)= ,
|     |     |     |     |     |     |     |     | 𝑖   | 𝑖   |     | (cid:16) (cid:17) | (4) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |
to p r o du ce a fi n a l ra n ki n g th a t r e fl e c ts i t s i n fe r re d u n d e rs t a nd i n g o f (cid:205) 𝑈 ( 𝑠)
|     |     |     |     |     |     |     |     |     | 𝑠∈S𝑡 | exp | 𝑖 ,𝑡 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- |
theuser’sunderlyingfinancialobjectives.Thismulti-viewdesign
TheglobalparametersareobtainedbyminimizingtheRegular-
enablesustodiagnosewhetheranLLM’smisalignmentwithactual
izedNegativeLog-Likelihood[2,21]overtheinteractionhorizon:
userbehaviorstemsfromanover-relianceonmarketmomentum
oramiscalculationoftheuser’sspecificriskthresholds.
𝑇
Fo r m a l ly ,f o r t h e u s e r 𝑖 a t s t e p 𝑡 ,g i v e n a ca n d i d a t e s t o c k s e tS 𝑡 L𝑖(𝜆 ,𝛾 ∑︁ log𝑃(cid:0)𝑠 ∗ |𝜆 ,𝛾 ,M𝑡 (cid:1)
|     |     |     |     |     |     |     |     | 𝑖 𝑖)= | −   | 𝑖 ,𝑡 𝑖 | 𝑖   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------ | --- | --- |
and d e ci si o n c o n t ex t I 𝑖, t h e r e c o m m e n d a ti on p r o c e s s i s d e fi n e d as : (5)
|     | 𝑡        |        |     |     |     |     |     |     | 𝑡=1              |     |     |     |
| --- | -------- | ------ | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
|     |          |        |     |     |     |     |     |     | +𝛼∥(𝜆 ,𝛾 𝑖)∥2    | ,   |     |     |
|     |          |        |     |     |     |     |     |     | 𝑖                | 2   |     |     |
|     | 𝜋 =𝑓 𝜃(I | 𝑖,S𝑡), |     |     |     |     |     |     |                  |     |     |     |
|     | 𝑖,𝑡      | 𝑡      |     | (1) |     |     |     | (𝜆  | 𝑖 ,𝛾 𝑖)=argminL𝑖 | .   |     | (6) |
𝜆𝑖,𝛾𝑖
|                                               |     |     |                  |     | where𝑠 | ∗    | isthestockactuallychosenbyuser𝑖 |     |     |     | atstep𝑡,and𝛼 |     |
| --------------------------------------------- | --- | --- | ---------------- | --- | ------ | ---- | ------------------------------- | --- | --- | --- | ------------ | --- |
| where𝑓 𝜃denotestheevaluatedLLM-basedadvisor,𝜋 |     |     | 𝑖,𝑡isthereranked |     |        | 𝑖 ,𝑡 |                                 |     |     |     |              |     |
listfromtheS𝑡.Specifically,thedecisioncontextI 𝑖isshownbelow: controlsthestrengthofregularization.
𝑡
|     |     |     |     |     |     | Once (𝜆 | 𝑖 ,𝛾 𝑖) areestimated,weconstructthereferenceviews |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | ------------------------------------------------- | --- | --- | --- | --- | --- |
𝑖 =(cid:0)𝑃𝑖,H 𝑖 ,M𝑡(cid:1), f o r e v al u at io n . Sp e c ifi c a ll y, th e R a t io n al U t ili t y v i e w ( 𝑦 ) is
|         | I   |        |     | (2) |        |         |          |              |                  |      |           | 𝑢𝑡 𝑖𝑙       |
| ------- | --- | ------ | --- | --- | ------ | ------- | -------- | ------------ | ---------------- | ---- | --------- | ----------- |
|         | 𝑡   | 1 :𝑡−1 |     |     |        |         |          |              | 𝑈 (𝑠 )           | R is | k S e n s | i t ivi t y |
|         |     |        |     |     | r a nk | e d b y | t h e fu | ll u t ili t | y 𝑖,𝑡 , w h il e | t he |           | v i ew      |
| where𝑃𝑖 |     |        |     |     | (𝑦     |         |          |              |                  |      |           | 𝑅 ( 𝑠 ) =   |
denotestheonboardingdialogue,amulti-turnintroduc- 𝑠𝑎𝑓𝑒) is ranked by the personalized risk penalty term: 𝑖 , 𝑡
toryinteractionusedtoelicittheuser𝑖’sbackground,financial 𝜆 𝑖 𝜎˜𝑠 2 +𝛾 𝑖Draw˜down𝑠,𝑡.
,𝑡
| goals,andinitialrisktolerance.M𝑡 |     | = {v𝑠,𝑡 ,x𝑠,𝑡}𝑠∈S𝑡 | represents |     |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | ------------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thecurrentmarketstate.Here,v𝑠,𝑡 =(𝜇 ,𝜎 2,Drawdown𝑠)denotes 3.3 DataCollectionandConversation
𝑠 𝑠
Simulation
thevectorofrawperformancemetricsusedforpreferenceground-
| ing,whilex𝑠,𝑡 comprisestheverbalizedmarketsignals(e.g.,price |     |     |     |     |       |                 |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | ----- | --------------- | --- | --- | --- | --- | --- | --- |
|                                                              |     |     |     |     | 3.3.1 | DataCollection. |     |     |     |     |     |     |
trends,percentagereturns,andvolatility)presentedtotheLLM
advisor.ThetermH𝑖 encapsulatesthelongitudinalinteraction MarketData. WeconstructacompactstockuniversefromS&P500
1:𝑡−1
trajectory,consistingofmulti-turndialoguesbetweentheuserand constituents using stratified sampling to ensure coverage of all
thethreespecializedadvisors(RationalUtility,MarketMomentum, elevenGICSsectorsandbalancedexposuretosystematicrisk.Can-
andRiskSensitivity).Thishistoryprovidesthemodelwithboth didatestocksaregroupedbymarketbeta,computedfromfive-year
theuser’spreviousdecisionpatternsandtheconflictingadvisory monthlyreturns,intolow(𝛽 < 1),moderate(𝛽 ≈ 1),andhigh
signalspreviouslyencountered. (𝛽 >1)riskregimes,withapproximatelyequalrepresentationfrom

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Yanetal.
Table2:SummaryofthestockuniverseusedinConv-FinRe. Table3:StructuralstatisticsofConv-FinRebenchmark.To-
Stocksaregroupedbyvolatilitytierbasedonmarketbetato kencountsarecomputedusingthecl100k_basetokenizer.
ensurebalancedexposuretosystematicrisk.
Scale Dialogue
Ticker Company GICSSector Beta MarketCap Users 10 MinTurns/Instance 4
LowVolatility(𝛽<1) Steps/User 23 MaxTurns/Instance 26
PG Procter&Gamble ConsumerStaples 0.36 $353B TotalInstances 230 AvgTurns/Instance 15
MRK Merck&Co.,Inc. HealthCare 0.38 $274B
VZ VerizonCommunicationsInc. CommunicationServices 0.36 $188B TurnAccounting TokenStatus
ModerateVolatility(𝛽≈1) UniqueTurns 270 MinTokens/Instance 1,818
LIN Lindeplc Materials 0.95 $213B Prefix-ExpandedTurns 3,450 MaxTokens/Instance 7,252
XOM ExxonMobilCorporation Energy 0.95 $596B
HighVolatility(𝛽>1) AvgTokens/Instance 4,320.2
JPM JPMorganChase&Co. Financials 1.13 $841B
AMZN Amazon.com,Inc. InformationTechnology 1.31 $2.6T trajectoryintoacoherentmulti-turnadvisoryconversation,en-
MMM 3MCompany Industrials 1.10 $81B
ablingcontrolledandreproducibleevaluationofLLMs.Eachuser
SPG SimonPropertyGroup,Inc. RealEstate 1.53 $62B
TSLA Tesla,Inc. ConsumerDiscretionary 2.07 $1.4T trajectoryisorganizedintotwophases:anonboardinginterview
andalongitudinaladvisorydialogueoverafixedhorizon𝑇.
eachgroup.Theresultinguniversecomprisestenrepresentative Theonboardingphaseverbalizesthestaticuserprofileobtained
stocks(Table2),enablingcontrolledlongitudinalevaluation. fromthequestionnaire.Usingtheuser’ssurveyresponsesasground-
Foreachstock,wecollectdailyandintradaypricedataovera ingsignals,wegenerateafour-turnadvisor–userdialoguethat
30-dayhorizon(Aug.6–Sep.17,2025)viatheYahooFinanceAPI3,
capturestheuser’sfinancialbackground,constraints,investment
whichdefinesthemarketstateinthesimulationenvironment. goals,andemotionalreactionstorisk.Thegeneratedlanguageis
constrainedtomatchtheuser’sreportedfinancialliteracy,ensur-
UserInteractionData. Userinteractiondataarecollectedthrough
ingthatpreferencesignalsareconveyedimplicitlythroughnatural
atwo-stageprotocol.First,weobtainstaticuserprofilesfrom10
expressionratherthanexplicitfinancialterminology.Thisonboard-
participantsviaastructuredquestionnaire4capturinginvestorde-
ingdialogueservesastheconversationalrealizationof𝑃𝑖 inthe
m
att
o
i
g
tu
ra
d
p
e
h
s.
ic
T
s
h
,
e
fi
q
n
u
a
e
n
s
c
t
i
i
a
o
l
n
c
n
a
a
p
ir
a
e
ci
d
ty
e
,
si
i
g
n
n
ve
fo
st
l
m
lo
e
w
n
s
t
r
e
e
x
g
p
u
e
la
ri
t
e
o
n
ry
ce
s
,
u
a
i
n
ta
d
bi
r
l
i
i
s
ty
k decisioncontextI
𝑡
𝑖.
Followingonboarding,thelongitudinaladvisoryphasereflects
guidelines(MiFIDIIArticle255;FINRARule21116)andisinformed
theuser’ssequentialdecision-makingbehaviorobservedinthe
byBetterment’sapproach7oninvestorriskpreferencesandfinan-
assetsimulation.Ateachstep𝑡,theconversationconditionson
cialdecision-making;andindustryexamples,suchasJPMorgan thehistoricalinteractiontrajectoryH𝑖 andthecurrentmarket
FinancialHealthCheck8,CharlesSchwabInvestorRiskProfile9, 1:𝑡−1
VanguardInvestorFinancialProfile10,andFinancialGroupPlan11.
stateM𝑡,representedbya7-daymarketsnapshotderivedfrom
thesimulationenvironment.Apanelofthreespecializedadvisors
Second,wecollectlongitudinaldecisiontrajectoriesusingacus-
providesrecommendationsbasedontheheterogeneousprinciples
tomassetsimulationtool.Participantsinteractwithafixeduniverse
definedinourmulti-viewframework:Rational-Utility,Market-
oftenstocksovera30-dayhorizon,observingdailyandintraday
Momentum,andRisk-Sensitivitystrategies.Theuserthenfi-
pricemovements.Ateachstep,usersmakeincrementalbuyde-
nalizesachoice,potentiallydeviatingfromadvisorsuggestions
cisionsandreceiveportfolio-levelfeedback,includingrealizedre-
andprovidingasubjectivejustificationconsistentwiththeirob-
turnsandvolatility,whichisloggedtogetherwiththeiractionsto
servedbehaviorinthesimulation.Alladvisormessagesanduser
formatemporallyorderedinteractiontrace.Thesimulationtoolis
responsesareappendedtotheconversationhistory,yieldingatem-
publiclyreleasedforreproducibility12.
porallyordereddialoguealignedwiththeunderlyinginteraction
3.3.2 ConversationSimulation. trace.Overall,asshowninTable3,thebenchmarkcontains10
usersand230prefix-conditionedinstances.Dialoguecontextgrows
ConversationGeneration. Buildingonthecollecteduserinter- from4to26turns(15onaverage),yielding270uniqueturnsthat
actiondata,weconstructastructuredconversationsimulationto expandto3,450prefix-conditionedturns.Eachinstancecontains
instantiatetheproposedlongitudinaladvisorytaskinalanguage- 1,818–7,252tokens(4,320.2onaverage),highlightingthesubstantial
basedsetting.Ratherthancollectingfree-formdialoguesfrompar- longitudinalcontextcomplexityrequiredforevaluation.
ticipants,wetransformeachuser’sobservedprofileandbehavioral
ConversationQualityValidation. Wevalidatethequalityofthe
simulatedconversationsfrombothapreference-groundinganda
3https://pypi.org/project/yfinance/ conversationalrealismperspective.
4https://forms.gle/g7GnwqByq7mCoJgTA UserPreferenceConsistencyValidation:Foreachuser𝑖,the
5https://eur-lex.europa.eu/eli/dir/2014/65/oj/
6https://www.finra.org/rules-guidance/rulebooks/finra-rules/2111 inferredlatentparameters(𝜆 𝑖 ,𝛾 𝑖)representtheuser’ssensitivityto
7https://d-nb.info/116404222X volatilityanddownsiderisk.Toassesswhethertheseparameters
8https://am.jpmorgan.com/content/dam/jpm-am-aem/asiapacific/hk/en/literature/
meaningfullycapturetheuser’strueinvestmentpsychology,finan-
account-forms/healthcheck_corporate.pdf
9https://www.studocu.vn/vn/document/royal-melbourne-institute-of-technology- cialexpertstranslateeachparameterpairintoaconcisenatural-
vietnam/international-trade/charles-schwab-investor-risk-profile/100562992 languagesummaryoftheuser’srisktolerance.Usersarethenasked
10https://sustainableinvest.com/wp-content/uploads/Investor-Financial-Profile-
torate,ona0–9Likertscale(0=notatallaccurate,9=perfectly
Questionnaire.pdf
11https://financialgroup.com/risk-profile-bq accurate),howwellthesummaryreflectstheirownreasoningand
12https://huggingface.co/spaces/TheFinAI/LetYourProfitsRun emotionswhenmakingstockselectiondecisions.Acrossusers,the

Conv-FinRe:AConversationalandLongitudinalBenchmarkforUtility-GroundedFinancialRecommendation Conferenceacronym’XX,June03–05,2018,Woodstock,NY
summariesreceiveahighaverageagreementscoreof 7.8,with Table4:Overallperformanceonthelongitudinalstockadvi-
sorytask.TheRandombaselineiscomputedbyaveraging
lowinter-uservariance,indicatingthattheinferredpreferencesare
over1,000uniformrandompermutationsperinstance,serv-
largelyconsistentwithusers’decision-makingbehavior.
ConversationalPlausibilityValidation:Wefurtherassessthe ingasasanity-checklowerbound.
realismofthesimulatedadvisorydialogues.Toavoidover-counting Model uNDCG↑ MRR↑ HR@1↑ HR@3↑
highlycorrelatedinteractionswithinthesameusertrajectory,we Random 0.73±0.00 0.29±0.01 0.10±0.01 0.30±0.01
GPT-5.2 0.94±0.03 0.46±0.02 0.29±0.03 0.51±0.03
adoptauser-levelsamplingstrategy.Specifically,foreachofthe GPT-4o 0.94±0.00 0.56±0.03 0.42±0.03 0.60±0.03
10users,werandomlysampleonedecisionstepfromthe23-step DeepSeek-V3.2 0.92±0.00 0.51±0.03 0.37±0.03 0.55±0.03
longitudinalconversation,resultingin10representativedialogue Qwen3-235B-A22B-Instruct 0.94±0.00 0.47±0.02 0.30±0.03 0.52±0.03
Qwen2.5-72B-Instruct 0.92±0.01 0.63±0.03 0.50±0.03 0.69±0.03
instances.Eachsampledconversationisindependentlyevaluated
Llama-3.3-70B-Instruct 0.97±0.00 0.52±0.03 0.36±0.03 0.59±0.03
bythreedomainexpertswithbackgroundsinfinanceandconver- Llama3-XuanYuan3-70B-Chat 0.92±0.00 0.65±0.03 0.54±0.03 0.69±0.01
sationalsystems.Expertsrateeachdialogueona0–9Likertscale
3.5 EvaluationModels
alongfourdimensions:roleconsistency,linguisticnaturalness,be-
havioralplausibilityofuserresponses,andcross-turncoherence. Ourgoalistoassessthecapabilitiesandlimitationsofcontempo-
Thefinalplausibilityscoreforeachconversationiscomputedas raryLLMsinconversational,personality-groundedlongitudinalstock
theaverageacrossthefourdimensionsandacrossexperts.Overall, recommendationundertheConv-FinRebenchmark.Tothisend,we
thesimulateddialoguesachieveameanplausibilityscoreof 8.1, evaluateadiversesetofstate-of-the-artLLMs,coveringbothpropri-
indicatingthatthegeneratedconversationscloselyresemblerealis- etaryandopen-sourcefamilies.Specifically,weincludetwoclosed-
ticfinancialadvisoryinteractionsratherthanscriptedorartificial sourcegeneral-purposemodels,GPT-5.2[31]andGPT-4o[13].
exchanges. Wefurtherevaluatearangeofopen-sourcegeneralmodelswith
strongreasoningandinstruction-followingcapabilities,including
3.4 EvaluationMetrics
DeepSeek-V3.2[8],Qwen3-235B-A22B-Instruct[37],Qwen2.5-
Utility-basedNDCG(uNDCG):Wefirstevaluatewhethermodel- 72B-Instruct[41],andLlama-3.3-70B-Instruct[12],andonefi-
generatedrankingsalignwiththeuser’slatent,utility-grounded nancialdomainconversationalmodel:Llama3-XuanYuan3-70B-
preferencestructure.Foruser𝑖atstep𝑡,wecomputeuNDCGusing Chat13.AllmodelsareevaluatedusingtheLMEvaluationHar-
thecalibratedutility𝑈 𝑖 ( ,𝑡 𝑠) asrelevance.Givenaranking𝜋 𝑖,𝑡 over ness[11]underaunifiedinterface.Proprietarymodelsareaccessed
candidatesetS𝑡,thediscountedcumulativegainis: viaofficialAPIs,whileopen-sourcemodelsareexecutedlocally.
Acrossallexperiments,westandardizethemaximuminputcon-
|S𝑡| 𝑈(𝜋𝑖,𝑡[𝑘])
DCG𝑖,𝑡 = ∑︁
log
𝑖,𝑡
(𝑘+1)
, (7) t
le
e
n
xt
gt
l
h
en
t
g
o
t
1
h
2
t
6
o
to
8
k
,1
e
9
n
2
s,
to
en
ke
su
n
r
s
in
an
g
d
fa
c
ir
on
an
st
d
ra
c
i
o
n
n
t
s
h
is
e
te
m
n
a
t
x
c
i
o
m
m
u
p
m
ar
g
is
e
o
n
n
e
a
ra
cr
ti
o
o
s
n
s
𝑘=1 2
models.
andtheutility-basedNDCGisdefinedas:
uNDCG𝑖,𝑡 =
DCG𝑖,𝑡
, (8)
4 ExperimentsandResults
IDCG𝑖,𝑡 4.1 OverallPerformance
whereIDCG𝑖,𝑡 iscomputedfromtheutility-optimalranking.
MRRandHitRate:Toassessrecoveryoftheuser’sobserved Table4showsthatmostmodelsachievehighuNDCGscores(0.92–0.97),
choice,let𝑠∗ denotethestockselectedbyuser𝑖atstep𝑡,andlet indicatingastrongbaselineforrankingassetsaccordingtotheRa-
𝑖,𝑡
𝜋 𝑖,𝑡(𝑠
𝑖
∗
,𝑡
)beitspositionin𝜋 𝑖,𝑡.Thereciprocalrankis tionalUtility.However,highuNDCGdoesnotalwaystranslateinto
betterrecoveryoftheUserChoice.WhileLlama-3.3-70B-Instruct
RR𝑖,𝑡 =
𝜋 𝑖,𝑡(
1
𝑠 𝑖 ∗ ,𝑡 )
, (9) l
p
e
r
a
io
d
r
s
it
i
i
n
ze
u
s
N
a
D
n
C
"i
G
de
(
a
0
l
.
i
9
z
7
e
)
d
,
"
i
r
t
a
s
t
h
io
o
n
w
a
s
lr
l
e
o
c
w
o
e
m
r
m
H
e
i
n
t
d
R
a
a
t
t
i
e
o
s
n
,
t
s
h
u
a
g
t
g
b
e
a
st
la
in
n
g
ce
i
s
t
long-termriskandreturn.
withMeanReciprocalRank(MRR)obtainedbyaveragingacross
usersandsteps.WeadditionallyreportHitRateattop-𝐾: Incontrast,Qwen2.5-72B-InstructandLlama3-XuanYuan3-70B-
ChatexcelinMRRandHR@K,indicatingtheyaremoreeffective
HR@𝐾 𝑖,𝑡 =I(cid:2)𝜋 𝑖,𝑡(𝑠 𝑖 ∗ ,𝑡 )≤𝐾(cid:3), (10) atmimickingtheuser’srealized,andoftennoisy,decision-making
andfocuson𝐾 ∈{1,3},whereI[·]denotestheindicatorfunction. patterns.Thisgaprevealsafundamentaltrade-off:𝑦 𝑢𝑡𝑖𝑙 actsasafi-
ExpertAlignmentScore(EAS):Toanalyzehowmodelsresolve nanciallyrobustreferencetoalignwiththeuser’slatentpsychology,
competingadvisoryprinciples,wemeasurealignmentwiththree whereas𝑦 𝑢𝑠𝑒𝑟 capturestheempiricalbehaviorwhichmaydeviate
expertrankings:RationalUtility,MarketMomentum,andRisk frompurerationality.Theresultssuggestthatmodelsmust
Sensitivity.Formodel𝑚,wecomputestep-wisealignmentusing navigatethetensionbetweenprovidingthemostrational
Kendall’s𝜏: adviceandmaintainingempatheticbehavioralalignment.
EAS 𝑖 ( , 𝑒 𝑡 )(𝑚)=𝜏(cid:0)𝜋 𝑖 𝑚 ,𝑡 ,𝜋 𝑖 𝑒 ,𝑡 (cid:1), (11) 4.2 ExpertAlignmentAnalysis
where𝑒denotestheexperttype.Finalscoresareobtainedbyaver-
agingoverallusersandsteps: Table5revealshowmodelsresolvecompetingadvisoryprinciples.
𝑁 𝑇 AprominenttrendisthestrongcouplingbetweenRationalUtility
EAS (𝑒) (𝑚)= 1 ∑︁∑︁ EAS (𝑒)(𝑚). (12)
𝑁𝑇
𝑖=1 𝑡=1
𝑖,𝑡 13https://huggingface.co/Duxiaoman-DI/Llama3-XuanYuan3-70B-Chat

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Yanetal.
Table5:Alignmentofmodel-generatedrankingswithhet-
erogeneousadvisoryprinciples.
Model 𝜏(Utility)↑ 𝜏(Momentum)↑ 𝜏(Risk)↑
Random 0.00±0.01 0.00±0.01 0.00±0.01
GPT-5.2 0.59±0.02 0.56±0.02 0.28±0.02
GPT-4o 0.60±0.02 0.60±0.02 0.20±0.02
DeepSeek-V3.2 0.51±0.02 0.49±0.02 0.26±0.02
Qwen3-235B-A22B-Instruct 0.56±0.02 0.55±0.02 0.26±0.02
Qwen2.5-72B-Instruct 0.52±0.02 0.49±0.02 0.22±0.02
Llama-3.3-70B-Instruct 0.74±0.02 0.73±0.01 0.17±0.02
Llama3-XuanYuan3-70B-Chat 0.47±0.02 0.46±0.02 0.15±0.02
andMarketMomentumalignment,whichstemsfromthecontex-
tualcollinearityofthesesignalsduringtrendingmarketswhere Figure2:Step-wiseimprovementinutility-basedalignment
high-momentumassetsoftendominateutilitycalculations.Llama- fromconversationalhistory.
3.3-70B-Instructexemplifiesthistrendbyachievingthehighest
alignmentwithbothUtilityandMomentum,yetitssharpdecline Figure3providesafiner-graineddiagnosticbycomparingav-
inRiskalignmentprovesthatitstrugglestodecoupledownside erage utility alignment with and without longitudinal context.
protectionfromgrowth-orientedsignals. Basedontherelativeshiftsfromthediagonal,weidentifythree
Incontrast,DeepSeek-V3.2demonstratesthemostbalancedpro- archetypes.
fileacrossallevaluatedmodels.Bymaintainingastableandrel- Adaptive Advisors (GPT-5.2, DeepSeek-V3.2, Qwen3-235B)
ativelyhighalignmentwithSafetywhileavoidingextremebias showclearimprovementswhenhistoryisavailable,indicatingef-
toward return-driven metrics, DeepSeek-V3.2 shows a superior fectivecross-turnpreferenceintegrationandprogressivealignment
abilitytointegrateconflictingadvisorysignalsintoacompromise withtheuser’slatentriskprofile.
recommendation.TheGPTseriesalsoexhibitssimilarbalanced Transaction-drivenAnalysts(GPT-4o,Llama-3.3-70B)remain
characteristics,thoughwithslightlylessconsistencythanDeepSeek closetothediagonal,achievingstrongutilityrankingsbutexhibit-
inthesafetydimension. inglimitedgainsfromconversationalcontext,suggestingreliance
ThebehaviorofLlama3-XuanYuan3-70B-Chatisparticularly oncontemporaneousmarketsignalsratherthanpersonalization.
noteworthygivenitsbackgroundasadomain-specificLLMfine- BehavioralOverfitters(Qwen2.5-72B,Llama3-XuanYuan3)ex-
tuned on financial corpora. Despite its lower expert alignment periencedegradedutilityalignmentwhenhistoryisintroduced,
scores,itachieveshighbehavioralhitratesinTable4,suggesting implyingover-sensitivitytonoisyuseractionsandatendencyto
thatitsfinancialexpertisemanifestsasempatheticalignmentwith prioritizebehavioralmimicryoverstablepreferenceinference.
UserChoicesratherthanstrictadherencetoidealizedmathematical Theresultsrevealnon-uniformpreferencediscoveryandhigh-
formulas.XuanYuan3actsasaseasonedhumanconsultantwho lighttheneedtoseparatesurfaceimitationfromgenuinedecision-
prioritizesthepragmatic,albeitnoisy,preferencesofreal-world utilityalignment,asevidencedbyXuanYuan’sperformancedrop.
investorsoverrigidalgorithmicconsistency.
4.3 PreferenceDiscoveryDynamics
Figure2illustratesthestep-wisegain(ΔuNDCG)inutility-based
alignmentwhenconversationalhistoryisaccessible.Whilegains
areobservedforseveralmodels,thedynamicsarehighlyhetero-
geneous. Models like GPT-5.2 and DeepSeek-V3.2 show signifi-
cantpositiveimprovementsinearlytomiddlestages(steps1–10),
suggestingtheysuccessfullyextractinformativesignalsaboutthe
user’s latent risk preferences from initial interactions. The sub-
sequentfluctuationsandgeneralplateauingacrossmostmodels
indicatethatwhileLLMscanformacoarsepreferencerepresenta-
tionearlyon,theinherent"noise"inlongitudinalfinancialdecisions Figure3:Averageutilityalignmentwithandwithoutconver-
makesconsistent,long-termpreferencetrackingchallenging. sationalhistory.
Fromafinancialadvisoryperspective,thesegainssuggestthat
conversationhistoryallowsmodelstogaugebaselineinvestment
styles,identifyingwhetherauserisinherentlyrisk-averseorreturn-
sensitive.However,theplateauingsuggeststhatthemarginalutility
5 Conclusion
ofadditionalhistoricalcontextdiminishesonceastable"investor
persona"isestablished,atwhichpointrankingperformancebe- WeintroduceConv-FinRe,aconversationalandlongitudinalbench-
comesmorecontingentontheimmediatemarketcontextM𝑡 than markthatshiftsfinancialrecommendationfromsurface-levelbe-
onfurtherpreferencerefinement. havioralmatchingtoutility-groundeddecisionalignment.Through

Conv-FinRe:AConversationalandLongitudinalBenchmarkforUtility-GroundedFinancialRecommendation Conferenceacronym’XX,June03–05,2018,Woodstock,NY
inverseoptimizationoflatentriskpreferences,itsupportsmulti- [19] HanjiaLyu,SongJiang,HanqingZeng,YinglongXia,QifanWang,SiZhang,Ren
viewevaluationthatseparatesrationaldecisionqualityfromob- Chen,ChrisLeung,JiajieTang,andJieboLuo.2024.Llm-rec:Personalizedrecom-
mendationviapromptinglargelanguagemodels.InFindingsoftheAssociation
serveduserbehavior.Ourresultsrevealapersistenttensionbe-
forComputationalLinguistics:NAACL2024.583–612.
tween utility-based ranking and behavioral alignment: general- [20] MalikMagdon-IsmailandAmirFAtiya.2004. Maximumdrawdown. Risk
purposeLLMsoftenoptimizeutilitymoreeffectively,whiledomain- Magazine17,10(2004),99–102.
[21] DanielMcFadden.1972.Conditionallogitanalysisofqualitativechoicebehavior.
specificmodelstendtooverfittransientuseractions.Thesefind- (1972).
ingsexposethelimitsofbehavior-onlyevaluationandmotivate [22] KhalidMehrajandVinayKumar.2025. PsychologicalBiasesinInvestment
Decisions:ABehavioralFinanceApproach.(2025).
benchmarksthatdisentanglelong-terminvestorpreferencesfrom
[23] AndreasOehlerandMatthiasHorn.2024.DoesChatGPTprovidebetteradvice
short-termmarketnoise. thanrobo-advisors?FinanceResearchLetters60(2024),104898.
[24] XueqingPeng,LingfeiQian,YanWang,RuoyuXiang,YueruHe,YangRen,
References MingyangJiang,JeffZhao,HuanHe,YiHan,etal.2025.MultiFinBen:AMultilin-
gual,Multimodal,andDifficulty-AwareBenchmarkforFinancialLLMEvaluation.
[1] RArran.2023. Behavioralfinance:Thepsychologybehindfinancialdecision- arXivpreprintarXiv:2506.14028(2025).
making.BusinessStudiesJournal15,5(2023),1–2. [25] LingfeiQian,WeipengZhou,YanWang,XueqingPeng,HanYi,YilunZhao,
[2] MBertero.2006.Regularizationmethodsforlinearinverseproblems.InInverse JiminHuang,QianqianXie,andJianyunNie.2025. Fino1:OntheTransfer-
Problems:Lecturesgivenatthe1st1986SessionoftheCentroInternazionaleMatem- abilityofReasoning-EnhancedLLMsandReinforcementLearningtoFinance.
aticoEstivo(CIME)heldatMontecatiniTerme,Italy,May28–June5,1986.Springer, arXiv:2502.08127[cs.CL] https://arxiv.org/abs/2502.08127
52–112. [26] MarkRubinstein.2002.Markowitz’s"portfolioselection":Afifty-yearretrospec-
[3] DimitrisBertsimas,VishalGupta,andIoannisChPaschalidis.2012. Inverse tive.TheJournaloffinance57,3(2002),1041–1045.
optimization:AnewperspectiveontheBlack-Littermanmodel. Operations [27] ChandanKumarSahandXiaoliLian.2025.PerFairX:IsThereaBalanceBetween
research60,6(2012),1389–1403. FairnessandPersonalityinLargeLanguageModelRecommendations?.InPro-
[4] DimitrisBertsimas,VishalGupta,andIoannisChPaschalidis.2015.Data-driven ceedingsoftheIEEE/CVFInternationalConferenceonComputerVision.2750–2759.
estimationinequilibriumusinginverseoptimization.MathematicalProgramming [28] ChandanKumarSah,XiaoliLian,TonyXu,andLiZhang.2025.FairEval:Eval-
153,2(2015),595–633. uatingFairnessinLLM-BasedRecommendationswithPersonalityAwareness.
[5] AgostinoCapponiandZhaoyuZhang.2020.RiskPreferencesandEfficiencyof arXivpreprintarXiv:2504.07801(2025).
HouseholdPortfolios.arXivpreprintarXiv:2010.13928(2020). [29] JavierSanz-Cruzado,NikolaosDroukas,andRichardMcCreadie.2024.FAR-Trans:
[6] XuChen,JingsenZhang,LeiWang,QuanyuDai,ZhenhuaDong,RuimingTang, AnInvestmentDatasetforFinancialAssetRecommendation. arXivpreprint
RuiZhang,LiChen,XinZhao,andJi-RongWen.2023.REASONER:anexplainable arXiv:2407.08692(2024).
recommendationdatasetwithcomprehensivelabelinggroundtruths.Advances [30] SurajSharma,JosephBrennan,andJasonNurse.2021.StockBabble:Aconversa-
inNeuralInformationProcessingSystems36(2023),14497–14515. tionalfinancialagenttosupportstockmarketinvestors.InProceedingsofthe3rd
[7] SunhaoDai,NingluShao,HaiyuanZhao,WeijieYu,ZihuaSi,ChenXu,Zhongx- ConferenceonConversationalUserInterfaces.1–5.
iangSun,XiaoZhang,andJunXu.2023.Uncoveringchatgpt’scapabilitiesin [31] AadityaSingh,AdamFry,AdamPerelman,AdamTart,etal.2025.OpenAIGPT-5
recommendersystems.InProceedingsofthe17thACMConferenceonRecom- SystemCard.arXiv:2601.03267[cs.CL] https://arxiv.org/abs/2601.03267
menderSystems.1126–1132. [32] YingSoandWarrenFKuhfeld.1995. Multinomiallogitmodels.InSUGI20
[8] DeepSeek-AI.2025.DeepSeek-V3.2:PushingtheFrontierofOpenLargeLanguage conferenceproceedings,Vol.1995.1227–1234.
Models. [33] YuemingSunandYiZhang.2018.Conversationalrecommendersystem.InThe
[9] DarioDiPalma,GiovanniMariaBiancofiore,VitoWalterAnelli,FedelucioNar- 41stinternationalacmsigirconferenceonresearch&developmentininformation
ducci,TommasoDiNoia,andEugenioDiSciascio.2023.Evaluatingchatgptas retrieval.235–244.
arecommendersystem:Arigorousapproach.arXivpreprintarXiv:2309.03613 [34] TakehiroTakayanagi,Chung-ChiChen,andKiyoshiIzumi.2023.Personalizeddy-
(2023). namicrecommendersystemforinvestors.InProceedingsofthe46thInternational
[10] ChongmingGao,WenqiangLei,XiangnanHe,MaartenDeRijke,andTat-Seng ACMSIGIRConferenceonResearchandDevelopmentinInformationRetrieval.
Chua.2021.Advancesandchallengesinconversationalrecommendersystems: 2246–2250.
Asurvey.AIopen2(2021),100–126. [35] TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,
[11] LeoGao,JonathanTow,BaberAbbasi,StellaBiderman,SidBlack,AnthonyDiPofi, andIadhOunis.2025.AregenerativeAIagentseffectivepersonalizedfinancial
CharlesFoster,LaurenceGolding,JeffreyHsu,AlainLeNoac’h,HaonanLi,Kyle advisors?.InProceedingsofthe48thInternationalACMSIGIRConferenceon
McDonell,NiklasMuennighoff,ChrisOciepa,JasonPhang,LariaReynolds,Hailey ResearchandDevelopmentinInformationRetrieval.286–295.
Schoelkopf,AviyaSkowron,LintangSutawika,EricTang,AnishThite,BenWang, [36] TakehiroTakayanagi,MasahiroSuzuki,KiyoshiIzumi,JavierSanz-Cruzado,
KevinWang,andAndyZou.2024. TheLanguageModelEvaluationHarness. RichardMcCreadie,andIadhOunis.2025.FinPersona:AnLLM-DrivenConver-
doi:10.5281/zenodo.12608602 sationalAgentforPersonalizedFinancialAdvising.InEuropeanConferenceon
[12] AaronGrattafiori,AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,Abhishek InformationRetrieval.Springer,13–18.
Kadian,AhmadAl-Dahle,AieshaLetman,AkhilMathur,AlanSchelten,Alex [37] QwenTeam.2025. Qwen3TechnicalReport. arXiv:2505.09388[cs.CL] https:
Vaughan,etal.2024.Thellama3herdofmodels.arXivpreprintarXiv:2407.21783 //arxiv.org/abs/2505.09388
(2024). [38] AmosTverskyandDanielKahneman.1992.Advancesinprospecttheory:Cumu-
[13] AaronHurst,AdamLerer,AdamPGoucher,AdamPerelman,AdityaRamesh, lativerepresentationofuncertainty.JournalofRiskanduncertainty5,4(1992),
AidanClark,AJOstrow,AkilaWelihinda,AlanHayes,AlecRadford,etal.2024. 297–323.
Gpt-4osystemcard.arXivpreprintarXiv:2410.21276(2024). [39] YanWang,LingfeiQian,XueqingPeng,YangRen,KeyiWang,YiHan,Dongji
[14] JiyoonLee,JoonghoonKim,andPilsungKang.2026.CEREAL:personality-driven Feng, Fengran Mo, Shengyuan Lin, Qinchuan Zhang, Kaiwen He, Chenri
LLM-basedconversationalrecommendationdatasetwithcontextually-enriched Luo,JianxingChen,JunweiWu,ChenXu,ZiyangXu,JiminHuang,Guo-
andrealisticuserinteractions.MultimediaToolsandApplications85,2(2026),47. jun Xiong, Xiao-Yang Liu, Qianqian Xie, and Jian-Yun Nie. 2026. FinTag-
[15] HaohangLi,YupengCao,YangyangYu,ShashidharReddyJavaji,ZhiyangDeng, ging:BenchmarkingLLMsforExtractingandStructuringFinancialInformation.
YueruHe,YuechenJiang,ZiningZhu,KpSubbalakshmi,JiminHuang,etal. arXiv:2505.20650[cs.CL] https://arxiv.org/abs/2505.20650
2025. Investorbench:Abenchmarkforfinancialdecision-makingtaskswith [40] YanWang,KeyiWang,ShanshanYang,JaisalPatel,JeffZhao,FengranMo,
llm-basedagent.InProceedingsofthe63rdAnnualMeetingoftheAssociationfor XueqingPeng,LingfeiQian,JiminHuang,GuojunXiong,Xiao-YangLiu,andJian-
ComputationalLinguistics(Volume1:LongPapers).2509–2525. YunNie.2025.FinAuditing:AFinancialTaxonomy-StructuredMulti-Document
[16] TingtingLiang,ChenxinJin,LingzhiWang,WenqiFan,CongyingXia,KaiChen, BenchmarkforEvaluatingLLMs.arXiv:2510.08886[cs.CL] https://arxiv.org/abs/
andYuyuYin.2024. LLM-REDIAL:alarge-scaledatasetforconversational 2510.08886
recommendersystemscreatedfromuserbehaviorswithllms.InFindingsofthe [41] AnYang,BaosongYang,BinyuanHui,etal.2024.Qwen2TechnicalReport.arXiv
AssociationforComputationalLinguisticsACL2024.8926–8939. preprintarXiv:2407.10671(2024).
[17] JiayiLiao,SihangLi,ZhengyiYang,JiancanWu,YanchengYuan,andXiangWang. [42] Qi Yang, Sergey Nikolenko, Alfred Huang, and Aleksandr Farseev. 2022.
2023.Llara:Aligninglargelanguagemodelswithsequentialrecommenders.CoRR Personality-drivensocialmultimediacontentrecommendation.InProceedingsof
(2023). the30thACMInternationalConferenceonMultimedia.7290–7299.
[18] QijiongLiu,JiemingZhu,LuFan,KunWang,HengchangHu,WeiGuo,Yong [43] TongYu,YongchengJing,XikunZhang,WentaoJiang,WenjieWu,YingjieWang,
Liu,andXiao-MingWu.2025.BenchmarkingLLMsinRecommendationTasks: WenbinHu,BoDu,andDachengTao.2025.Benchmarkingreasoningrobustness
AComparativeEvaluationwithConventionalRecommenders.arXivpreprint inlargelanguagemodels.arXivpreprintarXiv:2503.04550(2025).
arXiv:2503.05493(2025).

Conferenceacronym’XX,June03–05,2018,Woodstock,NY Yanetal.
[44] YilunZhao,YitaoLong,HongjunLiu,RyoKamoi,LinyongNan,LyuhaoChen, SpecializedDocuments. arXiv:2311.09805[cs.CL] https://arxiv.org/abs/2311.
YixinLiu,XiangruTang,RuiZhang,andArmanCohan.2024.DocMath-Eval: 09805
EvaluatingMathReasoningCapabilitiesofLLMsinUnderstandingLongand