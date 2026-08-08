|     | Synthesizing    |     | Behaviorally-Grounded |           |     |              | Reasoning |         | Chains: |      | A   |     |
| --- | --------------- | --- | --------------------- | --------- | --- | ------------ | --------- | ------- | ------- | ---- | --- | --- |
|     | Data-Generation |     |                       | Framework |     | for Personal |           | Finance |         | LLMs |     |     |
AkhilTheerthala
PerfiosSoftwareSolutions
|     |     | Abstract |     |     |     | et al., | 2024; | Luo et | al., 2025; | Takayanagi |     | et al., |
| --- | --- | -------- | --- | --- | --- | ------- | ----- | ------ | ---------- | ---------- | --- | ------- |
2023)
Personalizedfinancialadvicerequiresconsid-
|         |         |        |              |      |        | Recent | advances |     | in large | language |     | models |
| ------- | ------- | ------ | ------------ | ---- | ------ | ------ | -------- | --- | -------- | -------- | --- | ------ |
| eration | of user | goals, | constraints, | risk | toler- |        |          |     |          |          |     |        |
ance, and jurisdiction. Prior LLM work has (LLMs)haveshowneffectiveperformanceinact-
focusedonsupportsystemsforinvestorsandfi- ing as decision support systems for investors
nancialplanners. Simultaneously,numerousre- (Gupta,2023)andfinancialplanners(Huangetal.,
centstudiesexaminebroaderpersonalfinance
2024). Thecoreadvantageofnaturallanguagegen-
tasks,includingbudgeting,debtmanagement, erationpresentstheseautomatedsupportsystems
retirement,andestateplanning,throughagen-
|     |     |     |     |     |     | withaunique |     | advantagethat |     | wasneveravailable |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | ----------------- | --- | --- |
ticpipelinesthatincurhighmaintenancecosts,
|     |     |     |     |     |     | in previous | applications. |     |     | This advantage |     | has re- |
| --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | --- | -------------- | --- | ------- |
yieldinglessthan25%oftheirexpectedfinan-
cialreturns. Inthisstudy,weintroduceanovel peatedly shown itspower inlinguistic tasks such
asstreamliningcomplexfinancialnarrativesfrom
andreproducibleframeworkthatintegratesrel-
evantfinancialcontextwithbehavioralfinance extensivedocuments, corporatediscourses, news
studiestoconstructsupervisiondataforend-to-
sources,andsocialmedia.(Guetaetal.,2025;Lee
endadvisors. Usingthisframework,wecreate and Lay-Ki, 2024) The utility of these models is
a19ksamplereasoningdatasetandconducta
|     |     |     |     |     |     | also | being explored |     | in Time | series | (Liu | and Jia, |
| --- | --- | --- | --- | --- | --- | ---- | -------------- | --- | ------- | ------ | ---- | -------- |
comprehensivefine-tuningoftheQwen-3-8B
|                                      |     |     |                      |     |     | 2025)        | and Financial |     | reasoning |     | applications | (Liu |
| ------------------------------------ | --- | --- | -------------------- | --- | --- | ------------ | ------------- | --- | --------- | --- | ------------ | ---- |
| modelonthedataset.                   |     |     | Throughaheld-outtest |     |     |              |               |     |           |     |              |      |
| splitandablindLLM-jurystudy,wedemon- |     |     |                      |     |     | etal.,2025). |               |     |           |     |              |      |
Notwithstandingthiscapability,recentresearch
| strate | that through |     | careful data | curation | and |     |     |     |     |     |     |     |
| ------ | ------------ | --- | ------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
behavioralintegration,our8Bmodelachieves indicatesthatnomodelexcelsacrossallfinancial
performancecomparabletosignificantlylarger
taskcategories,whichincludetextsummarization,
baselines (14-32B parameters) across factual sentiment analysis, causal analysis, forecasting,
accuracy,fluency,andpersonalizationmetrics
|     |     |     |     |     |     | and text | classification |     | (Matlin |     | et al., | 2025). It |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------- | --- | ------- | --------- |
whileincurring80%lowercoststhanthelarger
|     |     |     |     |     |     | has been | demonstrated |     | that | attaining |     | robust per- |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | ---- | --------- | --- | ----------- |
counterparts.
formancefrequentlynecessitatestheutilizationof
| Keywords: |     | Financial | Datasets; | Personal | Fi- |     |     |     |     |     |     |     |
| --------- | --- | --------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
large,expensivemodels,therebyconstrainingthe
| nance; | Reasoning |     | Models; | Large Language |     |              |     |       |            |     |        |           |
| ------ | --------- | --- | ------- | -------------- | --- | ------------ | --- | ----- | ---------- | --- | ------ | --------- |
| Models |           |     |         |                |     | practicality | of  | these | solutions. |     | Due to | these in- |
herentlimitationsandthecomplexityoffinancial
1 Introduction
advisory,manystudiesfocusingonbroaderfinan-
Legal counseling, healthcare, and finance are cial decision systems have preferred an agentic
amongthenumeroushigh-stakesdomainsinwhich approach over training financial domain-specific
personalizedadviceisessential. However,thede- languagemodels. (Okpalaetal.,2025;Joshi,2025;
velopment of this personalized advice is fraught Takayanagietal.,2025a)
with obstacles, requiring substantial investments Althoughtheinitialagenticframeworksfocused
andyearsofhumanexpertise. Recentresearchef- on answering simple inquiries,(Lakkaraju et al.,
fortshavethoroughlyinvestigatedautomateddeci- 2023) recent studies have accelerated the devel-
sionsupportsystemsinvariousareas,emphasizing opmentofthesesystemstoprovidepracticaland
their cost-effectiveness. In the financial sector, a actionableadvicetotheenduser(Takayanagietal.,
varietyofsupportsystemshavebeeninvestigated, 2025b;Okpalaetal.,2025). Theseagentscannow
withaparticularemphasisonassetrecommenda- dynamically interact with users and can assist in
tions and investment predictions. (Sanz-Cruzado varioustaskssuchasrecommendation,questionan-
167
Proceedings of The 10th Workshop on Financial Technology and Natural Language. EMNLP-2025, Suzhou, China

swering,search,andcustomerprofiling. (Lietal., itly modelling this psychological dimension, our
2024;Takayanagietal.,2025a;Hanetal.,2024) frameworkensuresthatpersonalisationandempa-
Althoughagenticsystemsdemonstratepotential theticframingareintrinsictothemodel’sreasoning
inprovidingtailoredfinancialadvice,theirefficacy process,leadingtomoreeffectiveandtrustworthy
| ishinderedbyconsiderableconstraints,including |     |     |     |     |     | financialguidance. |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
the integration with legacy systems, compliance It should also be considered that although re-
withdatasecurityregulations,andhighinference cent agentic frameworks respond based on real-
costs. (Cemri et al., 2025; Wang et al., 2025). timeknowledge;mostoftheseknowledgesources
| In support | of these | concerns, |     | a recent | study by |     |     |     |     |     |     |
| ---------- | -------- | --------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
needtobemanuallycurated(AggarwalandSingh,
(Meimandietal.,2025)illustratesthataconfluence 2024). In addition to this, we should note that
oftechnicalandcost-relatedfactorshindersthese mostoftherecommendationsneededforgeneral
applicationsfromrealizingeven25%oftheiran-
financialadvicedonotrequirereal-timefinancial
ticipatedreturns. Thisresearchalsoestablishesan knowledge. Instead, this advice needs an agent
importantdifferentiation: successinbenchmarks that can inherently retrieve the relevant informa-
does not necessarily equate to success in deploy- tion from its memory. We address this problem
ment. Inpracticalterms,theseproactivefinancial bycarefullycraftingachain-of-thoughtsectionto
advisorsfrequentlyencounteraswiftdeterioration retrievethefinancialcontextrelevanttothequery.
inperformancewithinamatterofmonthsfollowing Recentstudieshaveshownthatinherentbiases
| their implementation, |               |     | attributable | to the        | inherent |             |           |            |     |           |            |
| --------------------- | ------------- | --- | ------------ | ------------- | -------- | ----------- | --------- | ---------- | --- | --------- | ---------- |
|                       |               |     |              |               |          | often limit | users’    | ability    | to  | make many | wealth-    |
| volatility            | of real-world |     | conditions.  | Concurrently, |          |             |           |            |     |           |            |
|                       |               |     |              |               |          | making      | financial | decisions. |     | (Baker et | al., 2017; |
studies show that the extent of personalization is Agrawal, 2012) These biases are highly variable
oftenlimitedbythevolumeofcontextandinforma- and often depend on the age, experience and lo-
tionthatcanbesuppliedtoanagent,impactingthe
|     |     |     |     |     |     | cation of | the | user. Many | financial | agents | do not |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --------- | ------ | ------ |
overall performance. (Zhou et al., 2025; Winder directlyaddressthesebiaseswhenprovidingfinan-
| etal.,2024) |               |      |     |               |         | cialadvicetotheuser. |     |     | Inthisstudy,wehavetried |     |     |
| ----------- | ------------- | ---- | --- | ------------- | ------- | -------------------- | --- | --- | ----------------------- | --- | --- |
| One         | of the direct | ways | to  | address these | limita- |                      |     |     |                         |     |     |
tointegratethesebiasesintothereasoningmodel’s
tions is to tune a model with a domain-specific naturalchain-of-thoughttotunethefinalresponses
context that integrates financial, behavioral, and towards acknowledging and addressing these bi-
| psychologicalinformation. |     |     | Thisworkaimstoclose |     |     | ases. |     |     |     |     |     |
| ------------------------- | --- | --- | ------------------- | --- | --- | ----- | --- | --- | --- | --- | --- |
thisgapbyprovidingareproducibleframeworkto
Eachstageofchain-of-thoughtgenerationisver-
generatefinancialadvicethroughawell-structured
ifiedbyasetofLargeLanguageModeljuriesthat
chain-of-thought. In particular, the framework rankvariousgenerationsandpickthebestversion
| constructs | supervision |     | data to | train models | to (a) |                            |     |     |     |                  |     |
| ---------- | ----------- | --- | ------- | ------------ | ------ | -------------------------- | --- | --- | --- | ---------------- | --- |
|            |             |     |         |              |        | suitablefortheuserqueries. |     |     |     | Weusedthisframe- |     |
providepersonalizedguidanceforusers’financial
|     |     |     |     |     |     | work to | generate | a 19k | sample | dataset, | which is |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ----- | ------ | -------- | -------- |
dilemmas,(b)reliablyapplycorefinancialknowl- usedtofinetuneaQwen-3-8Bmodel. Thismodel
edge,and(c)recognizeandmitigateuser-sidebe-
isthencomparedtomodelsofsimilarsizestode-
havioralbiasesbyintegratingbehavioralandhis-
terminetheimpactofthisframework.
toricalevidence.
Thispaperintroducesaprincipled,data-centric
To address these limitations, we propose a framework as a step toward smaller, more trust-
| novel, | data-centric | framework |     | for synthesising |     |     |     |     |     |     |     |
| ------ | ------------ | --------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
worthypersonalfinanceLLMs,andweoutlineits
| behaviorally-grounded |     |     | reasoning | chains. | Rather |     |     |     |     |     |     |
| --------------------- | --- | --- | --------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
useasabackbonepolicywithinagenticworkflows
thanrelyingoncomplexagenticarchitectures,our
|     |     |     |     |     |     | to thin | planning | chains | and | lower orchestration |     |
| --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | --- | ------------------- | --- |
approachdirectlybakesfinancial,behavioural,and
cost—anevaluationwedefertofuturework.
psychologicalknowledgeintothetrainingdatait-
self. Crucially,wetreattheinferenceoftheuser’s 2 RelatedWorks
| psychological | state | not | as an | afterthought, | but as |     |     |     |     |     |     |
| ------------- | ----- | --- | ----- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
astandalone,foundationalphaseinthereasoning The application of automated systems to finan-
chain. Thisdesignchoiceisdirectlymotivatedby cialadviceisnotanewundertaking. Priortothe
recent findings that users’ trust and engagement widespreadadoptionoflargelanguagemodels,re-
are heavily influenced by the persona of the ad- searchfocusedonapplyingclassictechniquessuch
visor (Takayanagi et al., 2025a), not just the raw ascollaborativefilteringandcase-basedreasoning
accuracy of its advice. By isolating and explic- towell-defineddomainssuchasloanandinsurance
168

policyrecommendation,assurveyedbyZibriczky as anchoring and overconfidence. Their crucial
(2016). However, the advent of powerful LLMs findingthatfine-tuningonfinancialdatacansome-
hasopenednewfrontiersandpresentedadistinct timesexacerbatetheseirrationaltendenciesunder-
setofchallengesandapproaches. scorestheprofoundrisksofusinguncurateddata.
Much of the recent literature has focused on Thisissupportedbyempiricalstudiesexposinga
benchmarkingthecapabilitiesofgeneral-purpose significant "product bias" in leading LLMs (Zhi
LLMsonarangeofisolatedfinancialtasks. Forin- etal.,2025)andbyfindingsthatLLM-generated
stance,acomprehensivestudybyHeanetal.(2025) advice systematically increases portfolio risk by
evaluated leading models such as ChatGPT and reinforcing investment biases such as geographi-
Claudeagainststandardizedfinancialliteracyques- calconcentrationandtrendchasing(Winderetal.,
tionnairescoveringdiversetopicsfrommortgages 2024). Takentogether,thesefindingsrevealthata
to taxes. While their findings show that newer model’spre-trainedknowledgeisanunreliableand
modelsareconsistentlyimprovingandcanachieve potentiallyriskyfoundationforfinancialadvice.
highaccuracyonspecifictopics, theyalsoreveal Therefore, our work addresses a critical gap.
significantlimitations,concludingthatLLMsstill While large-scale financial language models like
struggle to provide accurate responses for com- FinGPT,whichcontinuouslyingestreal-timemar-
plex financial queries. This highlights a critical ketdatatoupdateandadapttheunderlyingmodel
performance gap: off-the-shelf models are often (Yangetal.,2023;Wangetal.,2023;Zhangetal.,
insufficient for the nuanced demands of holistic 2023; Liu et al., 2023), have been proposed, our
financialadvice. approachdiffersfundamentallyinitscorecontribu-
To overcome the limitations of single models tion. Whereassuchworkfocusesonscalingmodel
and address more complex, multi-step planning, capacity and live data ingestion, our work intro-
asignificantbodyofresearchhasshiftedtowards duces a novel and reproducible methodology for
developingsophisticatedagenticworkflows. Are- creating the supervision data itself. By integrat-
centsurveybyDingetal.(2024)providesacom- ingtherelevantfinancialcontextwithbehavioral
prehensive overview of this landscape, categoriz- financestudies,weconstructahigh-qualityreason-
ing these systems into distinct architectural pat- ingdatasetdesignedtotrainsmaller,moreefficient
terns such as reflection-driven and debate-driven end-to-end advisors that are grounded in sound,
agents. AclearexampleistheworkofOkpalaetal. unbiasedprinciplesfromtheirinception.
(2025), who designed "agentic crews" composed
ofmultiplespecializedLLMagents,suchasdata 3 Datasetconstruction
scientists and compliance checkers, to automate
3.1 DataCollectionandProcessing
the entire financial modelling and risk manage-
mentpipeline. Whilepowerful,suchmulti-agent Our first step was to collect a large pool of real-
systemsdemonstratesignificantarchitecturalcom- world finance questions. Reddit (Reddit, [2025])
plexityandhighmaintenancecosts. Furthermore, proved ideal as a source of complex scenarios
research into these conversational agents has re- that span the breadth of personal finance do-
vealedsignificantrisks;Takayanagietal.(2025a) mains—from debt consolidation and retirement
foundinauserstudythatparticipantsoftenplaced planning to tax optimization and insurance deci-
moretrustinaconfident,"extroverted"agenteven sions. Theplatform’ssubreddits,particularlyr/per-
whenitprovidedlower-qualityadvice,highlighting sonalfinance,whichreceiveshundredsofthousands
thepotentialforthesecomplexsystemstomislead tomillionsofuserqueries,containauthenticscenar-
inexpertusers. iosthatcapturetheintricate,multi-facetednatureof
Weargue,however,thattheprimarybottleneck realfinancialdecision-making,providingthesce-
is not architectural complexity, but the inherent nariodiversityessentialfortrainingcomprehensive
irrationalityofthemodelsthemselves,necessitat- advisorymodels.
ing a data-centric approach. This need is rooted TocomplywithReddit’stermsandconditions,
in the tendency of LLMs to amplify human cog- weexclusivelyutilizedpubliclyavailablearchived
nitive biases. The groundbreaking work of Zhou datafrompostspriortoJune2023,ensuringallcol-
et al. (2025) introduced a comprehensive frame- lectedquerieswereethicallysourcedandproperly
workbasedonbehavioralfinancetodemonstrate de-identified.
thatLLMsexhibitsignificantfinancialbiases,such Afteringestion,wefilteredtherawcorpusintwo
169

Table1: Adetailedbreakdownofthedatasetgeneratedviaourproposedframework. Thistablepresentsthe
distributionofapproximately19ksamplesacrosseightdistinctcategoriesofpersonalfinance. Eachcategory
includeskeymetrics,suchastheaveragetokencountfortheinitialquery,thegeneratedchain-of-thought
delineatingthereasoningsteps,andthefinalanswer.
|          |     |     |             |     |     |     |       | Avg.   | Avg.   | Avg.     |
| -------- | --- | --- | ----------- | --- | --- | --- | ----- | ------ | ------ | -------- |
| Category |     |     | Description |     |     |     | Count | Query  | CoT    | Response |
|          |     |     |             |     |     |     |       | Tokens | Tokens | Tokens   |
DebtManagement&Credit Strategiesfordebtreduction(e.g.snow- 5175 215.76 628.30 393.69
|     |     |     | ball, | avalanche), credit-scoreimprove- |     |     |     |     |     |     |
| --- | --- | --- | ----- | -------------------------------- | --- | --- | --- | --- | --- | --- |
ment,andloananalysis.
RetirementPlanning Strategies,income-needsanalysis,bene- 3286 198.10 648.28 407.02
fitsoptimization(e.g.401(k),pensions)
andwithdrawalstrategies.
TaxPlanning&Optimization Tax-minimization strategies, under- 3019 182.96 630.20 397.81
|     |     |     | standing | deductions | and credits, | and |     |     |     |     |
| --- | --- | --- | -------- | ---------- | ------------ | --- | --- | --- | --- | --- |
investment-taximplications.
Investing&WealthBuilding Investmentstrategiesbasedonrisktol- 2994 200.16 653.54 402.98
erance,diversification,assetallocation,
andlong-termgrowth.
Budgeting&Cash-FlowManagement Creating budgets, tracking expenses, 2503 221.53 628.71 394.47
managingincomestreams,andimprov-
ingcashflow.
Insurance&RiskManagement Assessinginsuranceneeds(life,health, 1035 213.86 621.53 389.65
|     |     |     | property), | understanding | policies, | and |     |     |     |     |
| --- | --- | --- | ---------- | ------------- | --------- | --- | --- | --- | --- | --- |
managingfinancialrisks.
Savings&EmergencyFunds Strategiesforbuildingsavings,establish- 638 177.18 652.25 382.95
|     |     |     | ing | emergency funds, | and goal-based |     |     |     |     |     |
| --- | --- | --- | --- | ---------------- | -------------- | --- | --- | --- | --- | --- |
saving.
EstatePlanning&Legacy Wills,trusts,inheritanceconsiderations, 196 216.90 653.47 409.06
andminimisingestatetaxes(accounting
forregionalvariations).
| stages: |     |     |     |     | modular | approach | helps | us focus | on  | developing |
| ------- | --- | --- | --- | --- | ------- | -------- | ----- | -------- | --- | ---------- |
anindependentrubricforeachphasewhilegiving
| • Topical | validity  | – retained | posts | that con-    |             |           |     |               |     |            |
| --------- | --------- | ---------- | ----- | ------------ | ----------- | --------- | --- | ------------- | --- | ---------- |
|           |           |            |       |              | the ability | to stitch |     | them together | as  | a coherent |
| tained an | explicit, | answerable |       | personal fi- |             |           |     |               |     |            |
chain-of-thought.
| nance question                             |     | (e.g., budgeting, |     | credit, re- |       |               |     |     |     |     |
| ------------------------------------------ | --- | ----------------- | --- | ----------- | ----- | ------------- | --- | --- | --- | --- |
| tirement),discardinggenericnews,advertise- |     |                   |     |             | 3.2.1 | QueryAnalysis |     |     |     |     |
ments,oroff-topiccommentary.
Theissuewithnaturallanguageinquiriesisthepo-
tentialinconsistencyoftheinformationsuppliedto
| • Contextual    | clustering |           | – grouped | seman- |              |             |     |                |           |             |
| --------------- | ---------- | --------- | --------- | ------ | ------------ | ----------- | --- | -------------- | --------- | ----------- |
|                 |            |           |           |        | the model.   | There       | may | be significant |           | redundancy, |
| tically similar |            | posts and | removed   | near-  |              |             |     |                |           |             |
|                 |            |           |           |        | or essential | information |     | may            | be hidden | at times.   |
duplicatestoreducenoise.
Thus,theinitialstageofanswercreation,theques-
| Thispipelineyielded405kuniquequestions. |     |     |     | We  |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionanalysisphase,servesasafundamentalstepin
sampled19krepresentativequeriesthatspaneight
whichtheuser’squestionisdeconstructedintoits
| thematiccategories. | Table1containsthedetailed |     |     |     |                      |     |     |                           |     |     |
| ------------------- | ------------------------- | --- | --- | --- | -------------------- | --- | --- | ------------------------- | --- | --- |
|                     |                           |     |     |     | essentialcomponents. |     |     | Thisisrequiredtoascertain |     |     |
descriptionofthefinaldatasetgeneratedusingthe the (i) primary conflict from the user’s input; (ii)
| framework. Theentire405k-itemcorpusremains |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theprincipalplayersinthedilemma;and(iii)the
| availableforfuturescaling. |     | Detailsaboutprompt |     |     |                                             |     |     |     |     |      |
| -------------------------- | --- | ------------------ | --- | --- | ------------------------------------------- | --- | --- | --- | --- | ---- |
|                            |     |                    |     |     | essentialfinancialfactstoaddresstheinquiry. |     |     |     |     | This |
templates and specific instructions used in each facilitatestheoptimizationofsubsequentcognitive
phaseofthegenerationframeworkarepresentedin
processeswhileremainingalignedwiththeuser’s
AppendixA.1.
inquiry.
| 3.2 Generationmethodology |     |     |     |     | 3.2.2 | ContextAnalysis |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | ----- | --------------- | --- | --- | --- | --- |
Onahighlevel,thedatasetgenerationframework Contextanalysis(ModularRAG). Afterintent
canbedividedintotwoparts: (i)chain-of-thought parsing,weassembleacompactevidencepackvia
generationand(ii)responsegeneration. amodularRAGframework(Gaoetal.,2024)built
Ourchain-of-thoughtgenerationisdividedinto on two self-curated corpora snapshotted through
four major phases, as illustrated in Fig. 1. This February2025: (i)afinancialcorpusof∼600k
170

Figure1: Datasetgenerationpipeline. Fourmodularchain-of-thoughtphasesfeedintofinalresponsegeneration.
EachphaseincludesLLM-juryvalidation(notshown)toensurequality.
tokens—practical sources such as Investopedia evaluationoftheuser’sintent. Thisintentisutilized
and a Bogleheads snapshot (Investopedia, 2025; todirectthefinalresponseintoatonethatismost
Bogleheads, 2025) covering core concepts (e.g., suitablefortheuser,ratherthandirectlyproviding
retirement accounts, debt-repayment strategies), themamonotonousresponse.
pluscuratedsummariesofpolicychangesforma- Tooperatethecue-identificationatscale,andin
jorU.S.credit-cardproductsandotherconsumer- linewiththepriorstudieswhichdemonstratethat
policy/marketupdates; and(ii)abehavioralcor- state-of-the-artlargelanguagemodelsoutperform
pus of ∼300k tokens—research and practitioner human annotators in judgment tasks(Bojic´ et al.,
write-ups spanning psychology of risk, investor 2025; O’Leary, 2025), we adopt an LLM-based
behavior, behavioral portfolio theory, behavioral frameworkforcueidentificationsimilartotheother
asset pricing, psychological effects of debt, and stagesintheframework.
generationaldifferences.
3.2.4 ResponseFormulation
Candidate chunks are retrieved with
text-embeddings-3-large (OpenAI, 2025b) Thefinalphaseofthechain-of-thoughtisadistinct
(top-25), re-ranked with all-MiniLM-L12-v2 response formulation phase, in which we synthe-
(Sentence-Transformers, 2021), and the top-15 sizeasetofinstructions,consolidatinginformation
arecondensedbygemini-2.0-flash(Google,2025; fromallprecedingphases. Thisproducesasetof
Team et al., 2025a) to remove residual noise and directivesthatmustbeadheredtothroughoutthe
unify terminology. The streamlined context and response-generationphase.
theuserquerythenfeedthedownstreamreasoning
3.3 Responsegeneration
stage. FurtherdetailsareprovidedinAppendixB.
Aconclusiveresponseisformulatedtoaddressthe
3.2.3 PsychologicalCueidentification user’s inquiry, utilizing the previously optimized
Inparalleltocontextidentification,apsychological stagesofinformation. Thisconcludingcomment
cue identification module is run to identify cues isbasedonthefinancialcontextpresentedandis
fromthetext. Weextracttheoverallsentimentof articulatedinasuitabletonefortheuser.
the text, the primary emotions identifiable from
3.4 DataValidation
thechoiceofwordsinthequery,andthelevelof
certainty present in the information. Using these GiventhatvariousopenandproprietaryLLMsau-
cues,wetrytogeneralizeasetofcommunicative tomate numerous generations, there is a clear ne-
intents that might be behind the user’s query. By cessitytoassessandauthenticatetheiroutputs. We
breaking down the assessment into four distinct employedaseriesofjuries,specificallygemini-2.0-
categories, the process ensures a comprehensive flashando4-mini(OpenAI,2025a),toevaluateand
171

| rankvariousgenerationsforeachphase. |             |     |             |        | Eachjuror |          |     |       |     |            |     |        |
| ----------------------------------- | ----------- | --- | ----------- | ------ | --------- | -------- | --- | ----- | --- | ---------- | --- | ------ |
|                                     |             |     |             |        |           |          |     | Model |     | BERTScore↑ |     | BLEURT |
| assessed                            | the created |     | information | within |           | a three- |     |       |     |            |     |        |
Gemma3-27B-IT
shotevaluationframework,ultimatelyselectingthe
|     |     |     |     |     |     |     |     |     |     |     | 0.7142 | 0.4374 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ |
(Teametal.,2025b)
highest-rankedresponseforsubsequentgeneration
| jobs. |     |     |     |     |     |     | Gemma3-12B-IT |     |     |     | 0.7139 | 0.4390 |
| ----- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | ------ | ------ |
Mistral-24B-2501
|              |     |     |     |     |     |     |                   |     |     |     | 0.7133 | 0.4464 |
| ------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | ------ | ------ |
| 4 Evaluation |     |     |     |     |     |     | (MistralAI,2025b) |     |     |     |        |        |
QWQ-32B(Qwen,2025)
| Totestwhetherourdatasetenablespracticaldeci- |     |     |     |     |     |     |     |     |     |     | 0.7069 | 0.4452 |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ |
(reasoning)
sionsupport,wefine-tuneQwen-3-8B(Yangetal.,
2025)forfiveepochsandcompareitwithbaselines DeepSeek-Qwen-14B
| ofsimilarsize. |     |     |     |     |     |     | (reasoning) |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
Weperformanadditionalassessmentoftheper- (DeepSeekAI,2025) 0.7069 0.4513
formanceusingtwoseparateheld-outdatasets. We Ours(8B) 0.7000 0.4600
employthesemethodstoassessthequalityofthe
|                                                |     |     |     |     |     |     | Llama-38B(Meta, |     |     |     | 0.6881 | 0.4547 |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ------ | ------ |
| responsesthroughbothquantitativeandqualitative |     |     |     |     |     |     | 2024)           |     |     |     |        |        |
| measures.                                      |     |     |     |     |     |     | Mistral-7Bv0.3  |     |     |     | 0.6650 | 0.4501 |
(MistralAI,2025a)
4.1 QuantitativeEvaluation
Toassessthequantitativeperformanceofthemod- Table2: Automaticevaluationonthe500-querytestset.
els, we utilize a held-out dataset comprising 500 Boldmarksthebestscoreineachcolumn;higheris
| distinct      | queries                       | across | various | categories |     | of per- | better. |     |     |     |     |     |
| ------------- | ----------------------------- | ------ | ------- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- |
| sonalfinance. | Groundtruthswereproducedbythe |        |         |            |     |         |         |     |     |     |     |     |
generationframeworkpresentedinSection3.2(not
|     |     |     |     |     |     |     | default | inference | settings | to  | get their | best perfor- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------- | --- | --------- | ------------ |
thefine-tunedmodel)priortotrainingandvalidated
|                      |     |     |                          |     |     |     | mance. | This | setup allows | us  | to evaluate | whether |
| -------------------- | --- | --- | ------------------------ | --- | --- | --- | ------ | ---- | ------------ | --- | ----------- | ------- |
| byindependentjurors. |     |     | Followingtheground-truth |     |     |     |        |      |              |     |             |         |
ourfine-tunedmodelhasmerelylearnedtomimic
| generation,   | we      | calculate | the                  | BERTScore |     | (Zhang |              |               |     |           |              |              |
| ------------- | ------- | --------- | -------------------- | --------- | --- | ------ | ------------ | ------------- | --- | --------- | ------------ | ------------ |
|               |         |           |                      |           |     |        | the training | data          | or  | if it has | successfully | internal-    |
| et al., 2020) | using   | the       | Qwen-3-8B-embeddings |           |     |        |              |               |     |           |              |              |
|               |         |           |                      |           |     |        | ized a       | generalizable |     | framework | for          | the response |
| (Zhang        | et al., | 2025)     | model                | to assess | the | seman- |              |               |     |           |              |              |
generationthatcanbeappliedtonoveluserprob-
| tic accuracy | of  | the responses. |     | We  | also calculate |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
lems.
theBLEURT(Sellametal.,2020)scoretoassess
the fluency (or) human-likeness of the responses, To mitigate familial bias and leakage, we ex-
cludedjudgesfrommodelfamiliesusedanywhere
| respectively. | The      | quantitative |            | scores | of       | various |                                             |     |                               |     |     |     |
| ------------- | -------- | ------------ | ---------- | ------ | -------- | ------- | ------------------------------------------- | --- | ----------------------------- | --- | --- | --- |
|               |          |              |            |        |          |         | inourpipeline.                              |     | Inparticular,Geminimodelswere |     |     |     |
| models        | utilized | in this      | evaluation | are    | detailed | in      |                                             |     |                               |     |     |     |
| Table2.       |          |              |            |        |          |         | omittedbecausetheywereusedduringdatasetgen- |     |                               |     |     |     |
eration/validation,andQwen-familyjudgeswere
Our8Bmodelachievessemanticaccuracycom-
omittedbecausethesystemundertestisQwen-8B.
| parable | to leading | baselines, |     | including | Gemma3- |     |     |     |     |     |     |     |
| ------- | ---------- | ---------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
27B/12BandMistral-24B.Inparticular,ourmodel Afewotherwisesuitablejudgeswerealsoexcluded
surpasses these larger models by approximately for cost reasons. The final judge pool comprises
modelsfromunrelatedfamilies;noneoverlapped
| 3–5% in | human-likeness |     | and | fluency. | This | indi- |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | -------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
withtrainingordata-creationcomponents.
| cates a reduced |     | deviation | from | ground-truth |     | data |     |     |     |     |     |     |
| --------------- | --- | --------- | ---- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- |
andenhancedfluencysignalscomparedtomodels For each query, every judge sees all k
| twiceitssize. |     |     |     |     |     |     | anonymizedcandidatessimultaneously(noground |        |       |             |     |                |
| ------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | ------ | ----- | ----------- | --- | -------------- |
|               |     |     |     |     |     |     | truth                                       | and no | model | identities) | and | returns a full |
4.2 QualitativeEvaluation
ranking;candidateorderisuniformlyrandomized
Tocomplementreference-basedmetricsand,criti- per replicate. We use two main judges, namely
cally,toassessthemodel’sgeneralizationcapabili- DeepSeek-V3-0324(DeepSeek-AIetal.,2025)and
ties,werunalist-wiseblindLLM-juryrankingon Kimi-k2 (AI, 2025). Kimi-k2 is run three times,
504queriesthatwereentirelyheldoutandunseen and DeepSeek-v3-0324 is run five times on inde-
duringthetrainingphase. Thesetestquerieswere pendently shuffled anonymized candidate orders
collectedfromasubsequenttimeperiodtoensure for each query to reduce possible biases. These
nodatacontamination. Meanwhile,allthecandi- judgeswerechoseninordertoavoidsame-family
dateswerezero-shotgeneratedintheirrespective biasprevalentinmodernLLM-judgestudies.
172

Table3: Rankcorrelationsbetweenjudgesets(higheris
better). τ measureshowoftenthejudgesagreewithA>
B,andρmeasureshowcloselythefullrankliststrack.
| Metric        |          | Kendall’sτ |           | Spearman’sρ |        |        |          |                                        |     |     |     |     |     |
| ------------- | -------- | ---------- | --------- | ----------- | ------ | ------ | -------- | -------------------------------------- | --- | --- | --- | --- | --- |
| Plausibility  |          | 0.6183     |           |             | 0.7711 |        |          |                                        |     |     |     |     |     |
| Accuracy      |          | 0.6183     |           |             | 0.7635 |        |          |                                        |     |     |     |     |     |
| Relevance     |          | 0.6910     |           |             | 0.8264 |        |          |                                        |     |     |     |     |     |
| Overall       |          | 0.6429     |           |             | 0.7904 |        |          |                                        |     |     |     |     |     |
| The           | rankings | are        | converted |             | to     | Borda  |          |                                        |     |     |     |     |     |
| points(Saari, |          | 2023) and  | averaged  |             | across | judges |          |                                        |     |     |     |     |     |
|               |          |            |           |             |        |        | Figure2: | LLM-juryevaluationon504unseensubreddit |     |     |     |     |     |
and replicates to obtain the representative score queries: stackedbarsshowBorda-averagescoresfor
accuracy(blue),plausibility(orange),andrelevance
| ofaresponse. |     | Wereceivetherankingjudgments |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accordingtothreecriteria,namelytheirfinancial (green);tallerbarsindicatestrongeroverallpreference.
Our8Bsystem(fourthfromleft)outperformsallother
| accuracy, | plausibility, |     | and relevance |     | to the | query, |     |     |     |     |     |     |     |
| --------- | ------------- | --- | ------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
sub-14Bmodelsandapproachesthe27B–32B
| and report | the      | aggregate | Borda        | scores | in  | Fig.2.   |          |                                          |     |     |     |     |     |
| ---------- | -------- | --------- | ------------ | ------ | --- | -------- | -------- | ---------------------------------------- | --- | --- | --- | --- | --- |
|            |          |           |              |        |     |          | leaders. | They-axisrepresentstheaverageBordapoints |     |     |     |     |     |
| Whereas    | Appendix |           | C.1 presents |        | the | in-depth |          |                                          |     |     |     |     |     |
amodelhasreceived.
analysisoftheevaluationresults.
Toexaminerankconsistencybetweenthejudge
sets, we compute Kendall’s τ and Spearman’s ρ user constraints even when containing factual er-
| overper-querymodelranks. |     |     |     | Kendall’sτ |     | assesses |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
rorsorpoorreasoning.
pairwiseorderagreement(dobothjudgesprioritize
|                      |     |     |     |                     |     |     | Strengths.      | The | model     | consistently |       | produces |     |
| -------------------- | --- | --- | --- | ------------------- | --- | --- | --------------- | --- | --------- | ------------ | ----- | -------- | --- |
| modelAabovemodelB?). |     |     |     | Spearman’sρassesses |     |     |                 |     |           |              |       |          |     |
|                      |     |     |     |                     |     |     | well-structured |     | responses | with         | clear | headers, | se- |
how closely the complete ranked lists move to- quentialactionsteps,andappropriateempathetic
| gether     | and penalizes |               | significant | rank  | differences. |     |          |             |          |               |     |     |         |
| ---------- | ------------- | ------------- | ----------- | ----- | ------------ | --- | -------- | ----------- | -------- | ------------- | --- | --- | ------- |
|            |               |               |             |       |              |     | framing. | It reliably | extracts | user-specific |     |     | details |
| We observe |               | τ ≈ 0.62-0.69 |             | and ρ | ≈ 0.76-0.83  |     |          |             |          |               |     |     |         |
(monetaryamounts,timelines,constraints)andin-
(overallτ = 0.64,ρ = 0.79),indicatingsubstantial corporates them into tailored advice. Responses
| agreement. | Theconsistentlyhigherρthanτ |     |     |     |     | sug- |           |             |     |           |         |     |        |
| ---------- | --------------------------- | --- | --- | --- | --- | ---- | --------- | ----------- | --- | --------- | ------- | --- | ------ |
|            |                             |     |     |     |     |      | typically | acknowledge |     | emotional | context |     | before |
gestsdisagreementsaremostlylocalswapsrather
|                |     |              |     |           |     |        | providing | practical | guidance—a |     | pattern | that | en- |
| -------------- | --- | ------------ | --- | --------- | --- | ------ | --------- | --------- | ---------- | --- | ------- | ---- | --- |
| than wholesale |     | reorderings. |     | Relevance |     | demon- |           |           |            |     |         |      |     |
hancesperceivedhelpfulness.
| strates | the strongest |     | alignment            | (τ  | = 0.691, | ρ = |               |     |                             |     |     |     |     |
| ------- | ------------- | --- | -------------------- | --- | -------- | --- | ------------- | --- | --------------------------- | --- | --- | --- | --- |
|         |               |     |                      |     |          |     | FailureModes. |     | Theprimaryweaknessisfactual |     |     |     |     |
| 0.826). | Table3showsτ  |     | andρforeachmetricand |     |          |     |               |     |                             |     |     |     |     |
hallucination,particularlyforjurisdiction-specific
overall.
|     |     |     |     |     |     |     | regulations | and | tax details. | The | model | occasion- |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ----- | --------- | --- |
Ourexperimentalresultsdemonstratethatawell-
|     |     |     |     |     |     |     | ally generates | plausible-sounding |     |     |     | but incorrect |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------ | --- | --- | --- | ------------- | --- |
curated,behavior-tunedfinancedatasetcanelevate
|            |       |     |         |             |     |        | specifics          | (e.g., non-existent |                            | grant | programs, |     | out- |
| ---------- | ----- | --- | ------- | ----------- | --- | ------ | ------------------ | ------------------- | -------------------------- | ----- | --------- | --- | ---- |
| an 8B open | model | to  | achieve | performance |     | parity |                    |                     |                            |       |           |     |      |
|            |       |     |         |             |     |        | datedtaxbrackets). |                     | Theseerrorsaremostfrequent |       |           |     |      |
withmodelstwotothreetimesitssize,thusvalidat-
inregulation-heavydomains(taxes,insurance)and
| ingthepracticalutilityofourframework. |     |     |     |     |     | Details |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
leastcommoningeneralplanningtasks(budgeting,
| abouttheentiretrainingenvironmentandsettings |     |     |     |     |     |     | debtmanagement). |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
arepresentedinAppendixD.
|     |     |     |     |     |     |     | Implications. |                | Whilethemodelmaintainsstrong |           |     |        |         |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- | ---------------------------- | --------- | --- | ------ | ------- |
|     |     |     |     |     |     |     | structural    | and empathetic |                              | qualities |     | across | all re- |
4.3 QualitativeAnalysisandErrorPatterns
sponses,factualgroundingremainsthekeybottle-
Analysisofthe504held-outresponsesrevealscon- neck. Thissuggeststhataddingtargetedretrieval
sistentpatternsacrossthethreeevaluationdimen- forregulatoryinformationandcalculationverifica-
sions. Whenmodelsproduceinaccurateresponses, tionwouldyieldthehighestmarginalimprovement.
theytypicallyalsoexhibitdegradedreasoningqual- Evenwithcurrentlimitations,themodel’sconsis-
ity—accuracy and plausibility failures often co- tent task alignment and user-responsive framing
occur. However,relevanceremainsrelativelyinde- provide practical utility for non-critical advisory
| pendent;responsescanstayon-topicandaddress |     |     |     |     |     |     | scenarios. |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
173

4.4 CostAnalysis advice generation as an alignment problem, test-
ingpreference-basedoptimization(e.g.,DPO/IPO)
| Beyond        | performance     | metrics, | practical      | deploy- |                                |         |               |            |               |           |      |
| ------------- | --------------- | -------- | -------------- | ------- | ------------------------------ | ------- | ------------- | ---------- | ------------- | --------- | ---- |
|               |                 |          |                |         | to refine                      | outputs | and deploying |            | rule-based    |           | com- |
| ment requires | careful         | cost     | consideration. | Table   |                                |         |               |            |               |           |      |
|               |                 |          |                |         | pliance layers                 | to      | enforce       | regulatory |               | fidelity, | bias |
| 4 presents    | a comprehensive |          | cost analysis  | of the  |                                |         |               |            |               |           |      |
|               |                 |          |                |         | mitigation,andtoneconsistency. |         |               |            | Successwillbe |           |      |
modelproducedbyourframeworkagainstseveral
|     |     |     |     |     | quantified | through | targeted | evaluations |     | of  | safety, |
| --- | --- | --- | --- | --- | ---------- | ------- | -------- | ----------- | --- | --- | ------- |
baselines,comparinghostinginfrastructure,infer-
complianceadherence,andusertrustmetrics.
encelatency,andtotaloperationalexpenses.
Ourdata-centricapproachdeliversexceptional
6 Conclusion
| costefficiencyinthepersonalfinancedomain. |     |     |     | By  |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
enabling a compact 8B model to achieve perfor- Ourresearchestablishesadata-centricframework
mancecompetitivewithmuchlargersystems,our thatenablesan8B-parametermodeltoachievese-
methodfacilitatesatleastan80%reductioninop- mantic fidelity and human-likeness on par with,
| erational | costs when | compared | to baselines | with |     |     |     |     |     |     |     |
| --------- | ---------- | -------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
andsometimesexceeding,27–32Bbaselinesinour
over 12B parameters. This dramatic cost reduc- held-outevaluationsandblindLLM-jurystudy. On
tionstemsfromtargetedbehavioralintegrationand a500-querytest,themodeloutperformsGemma3-
principleddataconstruction,ratherthansheercom-
|                  |     |     |     |     | 27B by              | 5% on | BLEURT | and                    | is competitive |     | on  |
| ---------------- | --- | --- | --- | --- | ------------------- | ----- | ------ | ---------------------- | -------------- | --- | --- |
| putationalscale. |     |     |     |     | BERTScore,withonlya |       |        | 2%difference;juryrank- |                |     |     |
Theefficiencytranslatestopracticaldeployment ingsshowthe8Bsystemapproachingthe27–32B
advantages: at a hosting cost of $0.8 per hour leaders. These gains stem from three synergistic
and an average inference time of 34.15 seconds, components: explicitpsychologicalcues,retrieval-
our model enables responsive financial advisory augmented grounding, and a thin agentic execu-
serviceswithoutprohibitiveinfrastructurerequire- tionlayer. Themodulardesignsupportsincremen-
ments. Theseresultsvalidatetheeffectivenessof talextension(e.g.,regionalexpertswithminimal
ournoveldatagenerationframework. Theydemon- retraining). While geographic scope, behavioral
strate that by carefully integrating financial and depth,andprivacysafeguardsremainlimitations,
behavioralsignalsintotrainingdata,itispossible thisworkoffersacost-awarebackboneforstand-
tocreatecompetent,domain-specificmodelsthat alonepersonal-financeassistantsandaviablealter-
arealsoeconomicallyviable. Thispresentsacom- nativetomonolithicclouddeployments—leaving
pellingapproachfordevelopingproduction-ready aprecisecost/latencyaudittofuturework.
financialadvisorytoolsthatdonotrelysolelyon
| expensive,large-scalemodels. |     |     |     |     | Limitations |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Severalaspectsofourworkleaveroomforfuture
5 FutureWorks
|     |     |     |     |     | improvements. |     | First, | our study | is  | limited | to in- |
| --- | --- | --- | --- | --- | ------------- | --- | ------ | --------- | --- | ------- | ------ |
We will advance this research by first determin- quiries sourced solely from Reddit, which may
ing the optimal path for global scaling: either fi- overlook other demographics and query formats,
nalizing a US-optimized pipeline for systematic suggesting a need for more diverse data sources.
market porting or—contingent on high-precision Second,our19ksampledataset,thoughsufficient
detection of regional signals (e.g., currency sym- forproof-of-concept,lacksthescaleanddiversity
bols, policy terminology, and spelling conven- needed to cover the full spectrum of real-world
tions)—implementingaMixture-of-Experts(MoE) personalfinancescenarios. Futureworkshouldex-
framework. In the latter case, a shared backbone pandthecorpuswithvariedsourcesbeyondReddit
modelwillprocessuniversalfinanciallogicwhile to improve generalization. Third, our psycholog-
lightweight regional experts handle localized nu- ical analysis remains rudimentary, deriving only
ances. Thiscoremodelwilldeployasabackbone basicsentimentfromphrasesratherthanincorpo-
policywithinathinagenticstack, minimizingla- ratingenhancedpsychologicalindicatorssuchas
tencyandcostbyresolvingqueriesinternallyand risktoleranceorfinancialstressthroughspecialized
invokingexternaltools(e.g.,regulatorydatabases surveysortransferlearningfromclinicaldatasets.
or fact-checking APIs) only for uncertainty reso- Finally,ourframework’sscopeexcludestasksbe-
lution. Wewillrigorouslymeasureresultingcost- yondcorenaturallanguageprocessing,particularly
latencytrade-offsacrossregions. Ratherthanaddi- multi-modal data processing and reasoning capa-
tionalsupervisedfine-tuning,wewilltreatfinancial bilities, which represent critical areas for future
174

Table4: CostandInferencePerformanceAnalysisforDeployment. Totalcostsreflecttheexpensetoinfer504
queriesfromthetestset,witheachmodelbenchmarkedusingfourconcurrentrequests.
Model Size(GB) EndpointCost GPU InferenceTime TotalTime TotalCost
|                    |     |      |     | ($/h) |                       |     | (s/query) |     |     | (h)  | ($)   |
| ------------------ | --- | ---- | --- | ----- | --------------------- | --- | --------- | --- | --- | ---- | ----- |
| QWQ-32B            |     | 65.0 |     | 3.8   | 4xL4                  |     | 167.86    |     |     | 5.82 | 22.33 |
| Gemma3-27B         |     | 46.4 |     | 2.5   | 1xA100                |     | 64.34     |     |     | 2.23 | 5.63  |
| Gemma3-12B         |     | 20.0 |     | 1.8   | 1xL40S                |     | 58.26     |     |     | 2.02 | 3.67  |
| Ours(8B)           |     | 16.4 |     | 0.8   | 1xL4                  |     | 34.15     |     |     | 1.19 | 0.96  |
| Mistral-24B-2501   |     | 46.1 |     | 3.8   | 1xA100                |     | 37.99     |     |     | 1.32 | 5.05  |
| DeepSeek-Qwen-14B  |     | 29.5 |     | 1.8   | 1xL40S                |     | 54.18     |     |     | 1.88 | 3.41  |
| Llama3-8B          |     | 16.1 |     | 0.8   | 1xL4                  |     | 33.58     |     |     | 1.17 | 0.94  |
| Mistral-7B         |     | 14.5 |     | 0.8   | 1xL4                  |     | 29.15     |     |     | 1.01 | 0.82  |
| researchexpansion. |     |      |     |       | EthicalConsiderations |     |           |     |     |      |       |
Acknowledgements We curate data from publicly available Reddit
|                |                    |               |     |          | posts and            | aggressively |       | de-identify |          | them:      | user-  |
| -------------- | ------------------ | ------------- | --- | -------- | -------------------- | ------------ | ----- | ----------- | -------- | ---------- | ------ |
| I want to      | express my sincere | gratitude     |     | to Raghu |                      |              |       |             |          |            |        |
|                |                    |               |     |          | names/links/metadata |              |       | are         | removed, | PII        | (e.g., |
| Ram Theerthala | (KPIT              | Technologies) |     | for his  |                      |              |       |             |          |            |        |
|                |                    |               |     |          | names,               | emails,      | phone | numbers,    |          | addresses, | IDs)   |
valuablecontributionstotherelatedworkssection
|     |     |     |     |     | is scrubbed, | and | queries | are | lightly | rephrased | so  |
| --- | --- | --- | --- | --- | ------------ | --- | ------- | --- | ------- | --------- | --- |
andinsightfuldiscussionsduringthebrainstorming
onlythefinancialsituationremains;norawidenti-
| sessionsthathelpedshapethisresearch. |     |     |              | Iamgrate- |           |        |              |     |     |           |         |
| ------------------------------------ | --- | --- | ------------ | --------- | --------- | ------ | ------------ | --- | --- | --------- | ------- |
|                                      |     |     |              |           | fiers are | stored | or released. |     | The | system is | for ed- |
| fultoPrathyushaAkundi,SyedMd.        |     |     | Bilal,Ashish |           |           |        |              |     |     |           |         |
ucationaluseonly—notfiduciaryorpersonalized
Kubade,andSaiNarayanfortheircarefulreview
financialadvice—andourprompts/filtersforbidun-
| of the manuscript | and | constructive | feedback | that |     |     |     |     |     |     |     |
| ----------------- | --- | ------------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
safeguidance(e.g.,evasion,“guaranteedreturns”).
| improvedtheclarityandqualityofthiswork. |           |            |          | This |            |      |          |     |             |     |        |
| --------------------------------------- | --------- | ---------- | -------- | ---- | ---------- | ---- | -------- | --- | ----------- | --- | ------ |
|                                         |           |            |          |      | Evaluation | uses | multiple |     | LLM judges; | we  | report |
| research was                            | supported | by Perfios | Software | So-  |            |      |          |     |             |     |        |
inter-judgeagreementandrunjudge-swapchecks
lutions,whichsponsoredthecomputationalcosts
tolimitmodel-familybias.
andinfrastructurerequiredformodeltrainingand
evaluation.
References
Data&CodeAvailability
|     |     |     |     |     | RohitAggarwalandHarpreetSingh.2024. |     |     |     |     | Overcoming |     |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | ---------- | --- |
The dataset, model, and code artifacts described limitationsofaiagents: Integratingtacitknowledge
in this paper are publicly available on Hugging throughinferredlatent themes. Availableat SSRN
4843878.
| Face. All | data has been | de-identified |     | following |     |     |     |     |     |     |     |
| --------- | ------------- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
theethicalguidelinesdescribedinSection6,with KhushbuAgrawal.2012. Aconceptualframeworkof
personallyidentifiableinformationremovedfrom behavioralbiasesinfinance. IUPJournalofBehav-
ioralFinance.
| Redditsources. | Theresourcesarereleasedunder |     |     |     |     |     |     |     |     |     |     |
| -------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theApache2.0licensetofacilitatereproducibility Moonshot AI. 2025. Kimi-k2-instruct (revision
| andfutureresearchinbehavioralfinanceandLLM |     |     |     |     | 2f7e011). |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
applications.
HKentBaker,GregFilbeck,andVictorRicciardi.2017.
Thefollowingresourcesareavailable:
Howbehaviouralbiasesaffectfinanceprofessionals.
• Model: Fine-tunedQwen-3-8Bmodelat TheEuropeanFinancialReview,pages25–29.
https://huggingface.co/
|                                      |     |     |     |     | Bogleheads.        | 2025. | Bogleheads |     | - investing | advice | in- |
| ------------------------------------ | --- | --- | --- | --- | ------------------ | ----- | ---------- | --- | ----------- | ------ | --- |
| Akhil-Theerthala/Kuvera-8B-qwen3-v0. |     |     |     |     | spiredbyjohnbogle. |       |            |     |             |        |     |
2.1
|            |                             |     |     |     | Ljubiša       | Bojic´, | Olga  | Zagovora,     | Asta  | Zelenkauskaite,   |     |
| ---------- | --------------------------- | --- | --- | --- | ------------- | ------- | ----- | ------------- | ----- | ----------------- | --- |
|            |                             |     |     |     | Vuk Vukovic´, |         | Milan | Cˇabarkapa,   |       | Selma Veseljevic´ |     |
| • Dataset: | 19ksamplereasoningdatasetat |     |     |     |               |         |       |               |       |                   |     |
|            |                             |     |     |     | Jerkovic´,    | and     | Ana   | Jovancˇevic´. | 2025. | Comparing         |     |
https://huggingface.co/
largelanguagemodelsandhumanannotatorsinla-
datasets/Akhil-Theerthala/
tentcontentanalysisofsentiment,politicalleaning,
Kuvera-PersonalFinance-V2.1 emotionalintensityandsarcasm. naturebriefing.
175

MertCemri,MelissaZ.Pan,ShuyiYang,LakshyaA. KausikLakkaraju,SaraEJones,SaiKrishnaRevanth
Agrawal, Bhavya Chopra, Rishabh Tiwari, Kurt Vuruma,VishalPallagani,BharathCMuppasani,and
Keutzer,AdityaParameswaran,DanKlein,Kannan BiplavSrivastava.2023. Llmsforfinancialadvise-
Ramchandran, MateiZaharia, JosephE.Gonzalez, ment: Afairnessandefficacystudyinpersonalde-
andIonStoica.2025. Whydomulti-agentllmsys- cisionmaking. InProceedingsoftheFourthACM
temsfail? Preprint,arXiv:2503.13657. InternationalConferenceonAIinFinance, ICAIF
’23,page100–107,NewYork,NY,USA.Association
DeepSeek-AI,AixinLiu,BeiFeng,BingXue,Bingx- forComputingMachinery.
| uan Wang, | Bochao |     | Wu, Chengda |     | Lu, Chenggang |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Zhao,ChengqiDeng,ChenyuZhang,ChongRuan, MeisinLeeandSoonLay-Ki.2024. ’financewizard’at
Damai Dai, Daya Guo, Dejian Yang, Deli Chen, thefinllmchallengetask: Financialtextsummariza-
Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, tion. Preprint,arXiv:2408.03762.
| and181others.2025. |     |     | Deepseek-v3technicalreport. |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Preprint,arXiv:2412.19437.
JinzhengLi,JingshuZhang,HongguangLi,andYiqing
|     |     |     |     |     |     |     | Shen. | 2024. | An agent | framework | for | real-time | fi- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | -------- | --------- | --- | --------- | --- |
DeepSeekAI. 2025. deepseek-ai/deepseek-r1-distill- nancial information searching with large language
| qwen-14b. |     |     |     |     |     |     | models. | Preprint,arXiv:2502.15684. |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------- | -------------------------- | --- | --- | --- | --- | --- |
HanDing,YinhengLi,JunhaoWang,andHangChen.
Xiao-YangLiu,GuoxuanWang,HongyangYang,and
2024. Largelanguagemodelagentinfinancialtrad-
|     |     |     |     |     |     |     | DaochenZha.2023. |     |     | Data-centricfingpt: |     | Democra- |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ------------------- | --- | -------- | --- |
ing: Asurvey. Preprint,arXiv:2408.06361. tizinginternet-scaledataforfinanciallargelanguage
|             |     |        |      |       |     |        | models. | NeurIPSWorkshoponInstructionTuning |     |     |     |     |     |
| ----------- | --- | ------ | ---- | ----- | --- | ------ | ------- | ---------------------------------- | --- | --- | --- | --- | --- |
| Yunfan Gao, | Yun | Xiong, | Meng | Wang, | and | Haofen |         |                                    |     |     |     |     |     |
andInstructionFollowing.
| Wang.2024.                             |     | Modularrag:Transformingragsystems |     |     |     |           |         |          |      |        |               |     |       |
| -------------------------------------- | --- | --------------------------------- | --- | --- | --- | --------- | ------- | -------- | ---- | ------ | ------------- | --- | ----- |
| intolego-likereconfigurableframeworks. |     |                                   |     |     |     | Preprint, |         |          |      |        |               |     |       |
|                                        |     |                                   |     |     |     |           | Zhaowei | Liu, Xin | Guo, | Fangqi | Lou, Lingfeng |     | Zeng, |
arXiv:2407.21059. Jinyi Niu, Zixuan Wang, Jiajie Xu, Weige Cai, Zi-
weiYang,XueqianZhao,ChaoLi,ShengXu,Dezhi
| Google. | 2025. | Gemini | 2.0 flash. |     | https://cloud. |     |     |     |     |     |     |     |     |
| ------- | ----- | ------ | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Chen,YunChen,ZuoBai,andLiwenZhang.2025.
google.com/vertex-ai/generative-ai/docs/
|     |     |     |     |     |     |     | Fin-r1: | A large | language |     | model for | financial | rea- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | -------- | --- | --------- | --------- | ---- |
model-reference/inference.
|     |     |     |     |     |     |     | soning | through | reinforcement |     | learning. | Preprint, |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------------- | --- | --------- | --------- | --- |
arXiv:2503.16252.
AlmogGueta,AmirFeder,ZorikGekhman,ArielGold-
| stein,andRoiReichart.2025. |            |     |             | Canllmslearnmacroe- |     |           |          |            |      |       |          |           |     |
| -------------------------- | ---------- | --- | ----------- | ------------------- | --- | --------- | -------- | ---------- | ---- | ----- | -------- | --------- | --- |
|                            |            |     |             |                     |     |           | Zian Liu | and Renjun | Jia. | 2025. | Llm4fts: | Enhancing |     |
| conomic                    | narratives |     | from social | media?              |     | Preprint, |          |            |      |       |          |           |     |
largelanguagemodelsforfinancialtimeseriespre-
arXiv:2406.12109.
|             |       |               |     |           |     |       | diction. | Preprint,arXiv:2505.02880. |     |     |     |     |     |
| ----------- | ----- | ------------- | --- | --------- | --- | ----- | -------- | -------------------------- | --- | --- | --- | --- | --- |
| Udit Gupta. | 2023. | Gpt-investar: |     | Enhancing |     | stock |          |                            |     |     |     |     |     |
YichenLuo,YeboFeng,JiahuaXu,PaoloTasca,and
| investment | strategies |          | through | annual | report | analy-   |                                        |     |             |     |                   |     |       |
| ---------- | ---------- | -------- | ------- | ------ | ------ | -------- | -------------------------------------- | --- | ----------- | --- | ----------------- | --- | ----- |
|            |            |          |         |        |        |          | Yang Liu.2025.                         |     | Llm-powered |     | multi-agentsystem |     |       |
| sis with   | large      | language | models. |        | arXiv  | preprint |                                        |     |             |     |                   |     |       |
|            |            |          |         |        |        |          | forautomatedcryptoportfoliomanagement. |     |             |     |                   |     | arXiv |
arXiv:2309.03079.
preprintarXiv:2501.00826.
XuewenHan,NengWang,ShangkunChe,Hongyang
|                                        |            |        |           |      |            |           | Glenn Matlin, |       | Mika Okamoto, |     | Huzaifa      | Pardawala, |     |
| -------------------------------------- | ---------- | ------ | --------- | ---- | ---------- | --------- | ------------- | ----- | ------------- | --- | ------------ | ---------- | --- |
| Yang,                                  | Kunpeng    | Zhang, | and       | Sean | Xin        | Xu. 2024. |               |       |               |     |              |            |     |
|                                        |            |        |           |      |            |           | Yang Yang,    |       | and Sudheer   |     | Chava. 2025. | Finance    |     |
| Enhancing                              | investment |        | analysis: |      | Optimizing | ai-       |               |       |               |     |              |            |     |
|                                        |            |        |           |      |            |           | language      | model | evaluation    |     | (flame).     | Preprint,  |     |
| agentcollaborationinfinancialresearch. |            |        |           |      |            | Preprint, |               |       |               |     |              |            |     |
arXiv:2506.15846.
arXiv:2411.04788.
|                                         |     |     |     |     |             |     | Kiana Jafari       | Meimandi, |      | Gabriela                  | Aránguiz-Dias, |           |     |
| --------------------------------------- | --- | --- | --- | --- | ----------- | --- | ------------------ | --------- | ---- | ------------------------- | -------------- | --------- | --- |
| OudomHean,UtshaSaha,andBinitaSaha.2025. |     |     |     |     |             | Can |                    |           |      |                           |                |           |     |
|                                         |     |     |     |     |             |     | Grace              | Ra Kim,   | Lana | Saadeddin,                |                | and Mykel | J.  |
| aihelpwithyourpersonalfinances?         |     |     |     |     | AppliedEco- |     |                    |           |      |                           |                |           |     |
| nomics,page1–9.                         |     |     |     |     |             |     | Kochenderfer.2025. |           |      | Themeasurementimbalancein |                |           |     |
agenticaievaluationunderminesindustryproductiv-
|     |     |     |     |     |     |     | ityclaims. | Preprint,arXiv:2506.02064. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------------------- | --- | --- | --- | --- | --- |
ZengyiHuang,ChangChe,HaotianZheng,andChenLi.
2024. Researchongenerativeartificialintelligence
forvirtualfinancialrobo-advisor. AcademicJournal Meta.2024. meta-llama/llama-3.1-8b-instruct.
ofScienceandTechnology,10(1):74–80.
|               |       |     |               |     |              |     | MistralAI.2025a. |     | mistralai/mistral-7b-instruct-v0.3. |     |     |     |     |
| ------------- | ----- | --- | ------------- | --- | ------------ | --- | ---------------- | --- | ----------------------------------- | --- | --- | --- | --- |
| Investopedia. | 2025. |     | Investopedia. |     | https://www. |     |                  |     |                                     |     |     |     |     |
investopedia.com/. MistralAI.2025b. mistralai/mistral-small-24b-instruct-
2501.
| SatyadharJoshi.2025. |     |     | Acomprehensivereviewofgen |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aiagents: Applicationsandframeworksinfinance, IzunnaOkpala,AshkanGolgoon,andArjunRaviKan-
investments and risk domains. International Jour- nan. 2025. Agentic ai systems applied to tasks in
nalofInnovativeScienceandResearchTechnology, financialservices: Modelingandmodelriskmanage-
| pages1339–1355. |     |     |     |     |     |     | mentcrews. |     | Preprint,arXiv:2502.05439. |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------------------- | --- | --- | --- | --- |
176

DanielE.O’Leary.2025. Editorial: Analysisofsenti- GemmaTeam,AishwaryaKamath,JohanFerret,Shreya
ment estimates and cognitive fallacies in large lan- Pathak,NinoVieillard,RamonaMerhej,SarahPerrin,
guage models. Intelligent Systems in Accounting, Tatiana Matejovicova, Alexandre Ramé, Morgane
Finance and Management, 32(3):e70010. E70010 Rivière,LouisRouillard,ThomasMesnard,Geoffrey
| 9691779. |     |     |     |     |     | Cideron,JeanbastienGrill,SabelaRamos,Edouard |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
Yvinec,MichelleCasbon,EtiennePot,IvoPenchev,
OpenAI. 2025a. o3 and o4-mini system and197others.2025b. Gemma3technicalreport.
| card. |     | https://cdn.openai.com/pdf/ |     |     |     | Preprint,arXiv:2503.19786. |     |     |     |     |     |
| ----- | --- | --------------------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
2221c875-02dc-4789-800b-e7758f3722c1/
o3-and-o4-mini-system-card.pdf. KesenWang,DauletToibazar,AbdulrahmanAlfulayt,
AbdulazizS.Albadawi,RanyaA.Alkahtani,AsmaA.
OpenAI.2025b. Openaitext-embeddings-3. Ibrahim, Haneen A. Alhomoud, Sherif Mohamed,
|     |     |     |     |     |     | andPedroJ.Moreno.2025. |     |     |     | Multi-agentinteractive |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | ---------------------- | --- |
Qwen.2025. Qwen/qwq-32b. question generation framework for long document
|                 |         |     |       |        |           | understanding. |     | Preprint,arXiv:2507.20145. |     |     |     |
| --------------- | ------- | --- | ----- | ------ | --------- | -------------- | --- | -------------------------- | --- | --- | --- |
| Reddit. [2025]. | Reddit: | The | heart | of the | internet. |                |     |                            |     |     |     |
NengWang,HongyangYang,andChristinaDanWang.
https://www.reddit.com.
2023. Fingpt:Instructiontuningbenchmarkforopen-
DonaldG.Saari.2023. Selectingavotingmethod: the source large language models in financial datasets.
case for the borda count. Constitutional Political NeurIPSWorkshoponInstructionTuningandInstruc-
tionFollowing.
Economy,34(3):357–366.
PhilippWinder,ChristianHildebrand,andJochenHart-
| Javier Sanz-Cruzado, |     | Edward | Richards, | and | Richard |     |     |     |     |     |     |
| -------------------- | --- | ------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
McCreadie.2024. Far-ai: Amodularplatformforin- mann.2024. Biasedechoes: Generativeaimodels
vestmentrecommendationinthefinancialdomain. In reinforce investment biases and increase portfolio
risksofprivateinvestors.
AdvancesinInformationRetrieval,pages267–271,
Cham.SpringerNatureSwitzerland.
AnYang,AnfengLi,BaosongYang,BeichenZhang,
|                  |          |     |          |          |         | Binyuan | Hui, | Bo Zheng, | Bowen | Yu, | Chang Gao, |
| ---------------- | -------- | --- | -------- | -------- | ------- | ------- | ---- | --------- | ----- | --- | ---------- |
| Thibault Sellam, | Dipanjan |     | Das, and | Ankur P. | Parikh. |         |      |           |       |     |            |
2020. Bleurt: Learningrobustmetricsfortextgener- Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
|     |     |     |     |     |     | iheng | Liu, | Fan Zhou, | Fei | Huang, Feng | Hu, Hao |
| --- | --- | --- | --- | --- | --- | ----- | ---- | --------- | --- | ----------- | ------- |
ation. Preprint,arXiv:2004.04696.
|                             |     |     |                    |     |     | Ge, Haoran |       | Wei, Huan | Lin,      | Jialong Tang, | and 41    |
| --------------------------- | --- | --- | ------------------ | --- | --- | ---------- | ----- | --------- | --------- | ------------- | --------- |
|                             |     |     |                    |     |     | others.    | 2025. | Qwen3     | technical | report.       | Preprint, |
| Sentence-Transformers.2021. |     |     | all-minilm-l12-v2. |     |     |            |       |           |           |               |           |
arXiv:2505.09388.
| Takehiro Takayanagi, |            | Kiyoshi | Izumi, | Atsuo      | Kato, |            |       |                                       |      |               |     |
| -------------------- | ---------- | ------- | ------ | ---------- | ----- | ---------- | ----- | ------------------------------------- | ---- | ------------- | --- |
|                      |            |         |        |            |       | Hongyang   | Yang, | Xiao-Yang                             | Liu, | and Christina | Dan |
| Naoyuki              | Tsunedomi, | and     | Yukina | Abe. 2023. | Per-  |            |       |                                       |      |               |     |
|                      |            |         |        |            |       | Wang.2023. |       | Fingpt: Open-sourcefinanciallargelan- |      |               |     |
sonalizedstockrecommendationwithinvestors’at-
|                                  |     |     |     |               |     | guagemodels. |     | FinLLMSymposiumatIJCAI2023. |     |     |     |
| -------------------------------- | --- | --- | --- | ------------- | --- | ------------ | --- | --------------------------- | --- | --- | --- |
| tentionandcontextualinformation. |     |     |     | InProceedings |     |              |     |                             |     |     |     |
ofthe46thInternationalACMSIGIRConferenceon
BoyuZhang,HongyangYang,andXiao-YangLiu.2023.
ResearchandDevelopmentinInformationRetrieval,
|     |     |     |     |     |     | Instruct-fingpt: |     | Financial | sentiment | analysis | by in- |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | --------- | -------- | ------ |
SIGIR’23,page3339–3343,NewYork,NY,USA. struction tuning of general-purpose large language
AssociationforComputingMachinery.
|                      |     |         |        |        |       | models.       | FinLLMSymposiumatIJCAI2023. |                 |     |           |           |
| -------------------- | --- | ------- | ------ | ------ | ----- | ------------- | --------------------------- | --------------- | --- | --------- | --------- |
| Takehiro Takayanagi, |     | Kiyoshi | Izumi, | Javier | Sanz- |               |                             |                 |     |           |           |
|                      |     |         |        |        |       | Tianyi Zhang, |                             | Varsha Kishore, |     | Felix Wu, | Kilian Q. |
Cruzado,RichardMcCreadie,andIadhOunis.2025a.
|     |     |     |     |     |     | Weinberger, |     | and Yoav | Artzi. | 2020. | Bertscore: |
| --- | --- | --- | --- | --- | --- | ----------- | --- | -------- | ------ | ----- | ---------- |
Aregenerativeaiagentseffectivepersonalizedfinan- Evaluating text generation with bert. Preprint,
| cialadvisors? | Preprint,arXiv:2504.05862. |     |     |     |     | arXiv:1904.09675. |     |     |     |     |     |
| ------------- | -------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
TakehiroTakayanagi,MasahiroSuzuki,KiyoshiIzumi,
YanzhaoZhang,MingxinLi,DingkunLong,XinZhang,
JavierSanz-Cruzado,RichardMcCreadie,andIadh
|     |     |     |     |     |     | Huan | Lin, | Baosong Yang, |     | Pengjun Xie, | An Yang, |
| --- | --- | --- | --- | --- | --- | ---- | ---- | ------------- | --- | ------------ | -------- |
Ounis. 2025b. Finpersona: An llm-driven conver- DayihengLiu,JunyangLin,FeiHuang,andJingren
sational agent for personalized financial advising. Zhou. 2025. Qwen3 embedding: Advancing text
InAdvancesinInformationRetrieval,pages13–18, embeddingandrerankingthroughfoundationmodels.
| Cham.SpringerNatureSwitzerland. |     |     |     |     |     | Preprint,arXiv:2506.05176. |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
GeminiTeam,RohanAnil,SebastianBorgeaud,Jean-
|     |     |     |     |     |     | Yuhan Zhi, | Xiaoyu | Zhang, | Longtian | Wang, | Shumin |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | ------ | -------- | ----- | ------ |
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Jiang,ShiqingMa,XiaohongGuan,andChaoShen.
Schalkwyk, Andrew M. Dai, Anja Hauth, Katie 2025. Exposingproductbiasinllminvestmentrec-
Millican, David Silver, Melvin Johnson, Ioannis ommendation. Preprint,arXiv:2503.08750.
| Antonoglou, | Julian | Schrittwieser, |     | Amelia | Glaese, |     |     |     |     |     |     |
| ----------- | ------ | -------------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- |
JilinChen,EmilyPitler,TimothyLillicrap,Angeliki YuhangZhou,YuchenNi,ZhihengXi,ZhangyueYin,
Lazaridou,and1332others.2025a. Gemini: Afam- YuHe,GanYunhui,XiangLiu,ZhangJian,SenLiu,
ilyofhighlycapablemultimodalmodels. Preprint, XipengQiu,YixinCao,GuangnanYe,andHongfeng
arXiv:2312.11805. Chai.2025. AreLLMsrationalinvestors? astudy
177

|     | onthefinancialbiasinLLMs.             |              |     |         | InFindingsoftheAs- |              |     |                              |            |     |     |     |     |
| --- | ------------------------------------- | ------------ | --- | ------- | ------------------ | ------------ | --- | ---------------------------- | ---------- | --- | --- | --- | --- |
|     | sociationforComputationalLinguistics: |              |     |         |                    | ACL2025,6    |     |                              |            |     |     |     |     |
|     | pages                                 | 24139–24173, |     | Vienna, | Austria.           | Association7 |     | ###                          | Key Points | ### |     |     |     |
|     | forComputationalLinguistics.          |              |     |         |                    |              |     | {key_points_to_keep_in_mind} |            |     |     |     |     |
8
|     | David    | Zibriczky.         | 2016. | Recommender |                        | systems | meet9 |     |     |     |     |     |     |
| --- | -------- | ------------------ | ----- | ----------- | ---------------------- | ------- | ----- | --- | --- | --- | --- | --- | --- |
|     | finance: | Aliteraturereview. |       |             | InInternationalWork-10 |         |       | --- |     |     |     |     |     |
**Inputs**:
|     | shoponPersonalization&RecommenderSystemsin |     |     |     |     |     | 11  |          |     |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
|     | FinancialServices.                         |     |     |     |     |     |     | {inputs} |     |     |     |     |     |
12
---
13
|     |     |     |     |     |     |     | 14  | **Your | Response**:""" |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | --- | --- | --- |
Appendices
|     |     |     |     |     |     |     |     | A.1.2 | IndividualPhases |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------------- | --- | --- | --- | --- |
A PromptingGuidelinesfollowedforthe
|     | generationandevaluationstages |     |     |     |     |     |     | 1.  | Classification: |     |     |     |     |
| --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
A.1 Guidelinesfollowedinthegeneration a. The primary goal of this stage is to
|     |              | stage. |         |     |           |                |     |     | classifyincominguserqueriesintosuit- |            |     |       |          |
| --- | ------------ | ------ | ------- | --- | --------- | -------------- | --- | --- | ------------------------------------ | ---------- | --- | ----- | -------- |
|     |              |        |         |     |           |                |     |     | ablecategoriesofpersonalfinance.     |            |     |       | The      |
|     | This section |        | focuses | on  | outlining | the guidelines |     |     |                                      |            |     |       |          |
|     |              |        |         |     |           |                |     |     | prompt                               | constrains | the | model | by forc- |
followedincraftingthepromptsforeachphaseof
ingasingle-labelclassification(ONEof
generatingandevaluatingtheoutputs.
thefollowing)basedonPRIMARYIN-
A.1.1 Overarchingprinciples TENT,whichpreventsambiguityanden-
There are three core principles followed for the sures a decisive output for downstream
|     | processofcraftingtheprompts: |     |     |     |     |     |     |     | routing. |          |       |       |            |
| --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----- | ----- | ---------- |
|     |                              |     |     |     |     |     |     |     | b. Each  | category | has a | Scope | and an ex- |
a. Modularity
|     |                   |     |     |     |     |     |     |     | ample      | that                      | the model | uses | to make its |
| --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------- | --------- | ---- | ----------- |
|     | b. Deconstruction |     |     |     |     |     |     |     | decisions. | Ifthequerydoesnotfallinto |           |      |             |
anyofthecategories,thequeryislabeled
c. Personification
Not_Applicable.
|     | The | goal | of the | overall | prompt | crafting | is to |     |     |     |     |     |     |
| --- | --- | ---- | ------ | ------- | ------ | -------- | ----- | --- | --- | --- | --- | --- | --- |
2. QueryAnalysis:
|     | keep the | overall | structure |     | of the | prompts | similar |     |     |     |     |     |     |
| --- | -------- | ------- | --------- | --- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- |
andswappabledependingonthetaskathand. As a. The primary goal of this prompt is to
with the framework, where the complex task of directthemodeltobreakdowntheuser
generatingasuitableresponseisbrokendowninto queryintomorespecificandmanageable
individualphases,thepromptsarebrokendownto piecesofinformation.
makesurethestructureoftheinstructionsgivento
|     |                         |     |     |     |     |     |     |     | b. SincemostoftheuserqueriesonReddit |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
|     | themodelremainsthesame. |     |     |     |     |     |     |     | andingeneralareoftenfilledwithunre-  |     |     |     |     |
Eachstageofthepromptinghadaunique,suit- latednoise,thisstagedirectsthemodel
ablepersona(e.g.,linguisticanalysisexpert,expert
todistiltheuser’squeryintoessentialse-
|     | financialreasoningengine). |     |     |     | Thisrole-playingtech- |     |     |     |     |     |     |     |     |
| --- | -------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
manticelements,eliminatingtheconver-
niqueprimesthemodeltoaccessrelevantknowl- sational distractions and concentrating
edge,adopttheappropriatetone,andconstrainits onactionableconcernsandtheirimpact
behaviortothespecificrequirementsofthetask.
onthekeystakeholders.
Thegenericstructureofthepromptisasfollows:
3. ContextAnalysis:
|     |     |     |     |     |     |     |     |     | a. The context |     | analysis | is one | of the key |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------ | ---------- |
"""
| 1   |         |     |            |     |       |         |     |     | promptsthatinfluencesthequalityofthe |        |            |     |            |
| --- | ------- | --- | ---------- | --- | ----- | ------- | --- | --- | ------------------------------------ | ------ | ---------- | --- | ---------- |
| 2   | You are | a   | {persona}, |     | whose | task is | to  |     |                                      |        |            |     |            |
|     |         |     |            |     |       |         |     |     | output                               | by the | framework. |     | The prompt |
{task_details}.
(cid:44)→
directsthefinalmodeltogenerateaction-
| 3   |                 |     |     |     |     |     |     |     | ableandinsightfulcontextualsummaries |        |      |             |         |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | ------ | ---- | ----------- | ------- |
|     | ### INSTRUCTION |     |     | ### |     |     |     |     |                                      |        |      |             |         |
| 4   |                 |     |     |     |     |     |     |     | that are                             | placed | into | the model’s | natural |
{instructions_for_the_task}
5
chain-of-thought.
178

| b. ThepromptexplicitlyasksforaConcise |     |     |     |     |     | 6.  | ResponseGeneration |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- |
chain-of-thoughtAnalysisBlockandin-
|         |     |       |           |       |        |     | a.  | This final | stage synthesises | all preced- |
| ------- | --- | ----- | --------- | ----- | ------ | --- | --- | ---------- | ----------------- | ----------- |
| structs | the | model | that this | is an | inter- |     |     |            |                   |             |
inganalysesintoacoherent,user-facing
nalreasoningstep,notthefinalanswer.
response.
Thisstepforcesthemodeltoexternalise
|     |     |     |     |     |     |     | b.  | Thepromptprovidesthemodelwithall |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- |
itsreasoningprocess,exploringmultiple
previousoutputs(theoriginalqueryand
scenariosandtheirconsequencesbefore
thecomprehensivechain-of-thought)and
concluding.
explicitlyinstructsittointegratebothfac-
| c. By requiring |     | the | model | to detail | the |     |     |     |     |     |
| --------------- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
tualaccuracyandemotionalintelligence
| Stakeholder |     | Impact  | for each   | approach, |     |     |     |             |                          |     |
| ----------- | --- | ------- | ---------- | --------- | --- | --- | --- | ----------- | ------------------------ | --- |
|             |     |         |            |           |     |     |     | seamlessly. | Itactsasafinal"assembly" |     |
| the prompt  |     | ensures | a holistic | analysis  |     |     |     |             |                          |     |
instruction,guidingthemodelonhowto
| that considers |     | the | financial | and | emo- |     |     |     |     |     |
| -------------- | --- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- |
combinetherationalandaffectivecom-
tionalconsequencesforallrelevantpar-
ponents.
| ties mentioned |     | in       | the query. |     | This    |     |     |         |                   |               |
| -------------- | --- | -------- | ---------- | --- | ------- | --- | --- | ------- | ----------------- | ------------- |
|                |     |          |            |     |         |     | c.  | The use | of clear positive | (Do) and neg- |
| scenario-based |     | analysis | moves      |     | the re- |     |     |         |                   |               |
ative(Donot)instructionscreatesstrict
sponsesbeyondsimplefact-basedanal-
|         |        |               |     |      |     |     |     | behavioralboundaries. |     | Forinstance,"Do |
| ------- | ------ | ------------- | --- | ---- | --- | --- | --- | --------------------- | --- | --------------- |
| ysis to | a more | human-centred |     | form | of  |     |     |                       |     |                 |
notreferencethechain-of-thoughtanaly-
reasoning.
sis"ensuresthefinaloutputisnaturaland
user-friendly,hidingthecomplexunder-
4. Psychologicalanalysis
lyingcognitivearchitecturefromtheend-
| a. The goal | of  | this prompt | is  | to direct | the |     |     |     |     |     |
| ----------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- |
user. Theseinstructionscreateahelpful
| model | and | extract | the key | information |     |     |     |     |     |     |
| ----- | --- | ------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
responsewithoutbeingroboticortrans-
abouttheuser’sstateofmindwhenask-
parentaboutitsinnerworkings.
ingthequery.
|     |     |     |     |     |     |     | d.  | Theseresponsesaregeneratedinaway |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- |
b. Thepromptdemandsthateveryconclu-
|     |     |     |     |     |     |     |     | that ensure | the ability | to train non- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ------------- |
sionaboutsentiment,emotion,orintent reasoningmodelsfromthesamedataset.
bejustifiedbyreferencingspecificwords
or phrases. This approach grounds the A.2 PromptGuidelinesforEvaluation
throughLLM-as-a-Judge
analysisintextualevidence,preventing
themodelfrommakingunfoundedpsy- The goal of the evaluation is to determine which
| chological |     | assumptions | and | improving |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- |
responsesarenaturallyrankedbetterthantheoth-
theexplainabilityof itsaffectiveunder- ers. Since this is a list-wise ranking with a high
| standing. |     |     |     |     |     | roomforconfusionorhallucination,theevaluation |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- |
c. Thisanalysisisaseparatestepfromthe criterionarestrictlydefined.
Theoverallpromptstructureforeachofthecase
| financial                            | reasoning  |            | (Context  | Analysis). |        |               |     |     |     |     |
| ------------------------------------ | ---------- | ---------- | --------- | ---------- | ------ | ------------- | --- | --- | --- | --- |
| This                                 | deliberate | separation |           | prevents   | the    | areasfollows: |     |     |     |     |
| user’s                               | emotional  | state      | from      | biasing    | the    |               |     |     |     |     |
| objective                            | financial  |            | analysis, | and        | vice-1 |               |     |     |     |     |
| versa,allowingforafinalresponsethat2 |            |            |           |            |        | """           |     |     |     |     |
cansynthesisebothaspectswithoutcom-3 You are a {persona}. Your task is to
|                  |     |     |     |     |     |           | rank | financial | advice         | responses |
| ---------------- | --- | --- | --- | --- | --- | --------- | ---- | --------- | -------------- | --------- |
| promisingeither. |     |     |     |     |     | (cid:44)→ |      |           |                |           |
|                  |     |     |     |     |     |           | from | best      | to worst based | *solely*  |
(cid:44)→
5. ResponseRubric
|     |     |     |     |     |     |     | on  | the strict | definition | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- |
(cid:44)→
{target_aspect}.
| a. Thisstageconsolidatesallthepreviously |     |     |     |     |     | (cid:44)→ |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
collectedinformationandcreatesacom-4
|     |     |     |     |     |     | ### | **Evaluation |     | Criteria** |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- |
pleterubricthatcandirectthemodelinto5
|     |     |     |     |     |     | 6 {Evaluation |     | Criterion} |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | --- | --- |
generatingthefinalresponse.
7
| b. The                             | key information |     | from | the | previ- |           |      |         |          |          |
| ---------------------------------- | --------------- | --- | ---- | --- | ------ | --------- | ---- | ------- | -------- | -------- |
|                                    |                 |     |      |     |        | ####      | **I. | Primary | Criteria | (What to |
| ousstagesgetshighlightedwhilebeing |                 |     |      |     |        | 8         |      |         |          |          |
|                                    |                 |     |      |     |        | (cid:44)→ | look | for):** |          |          |
linkedtodifferentpartsoftheuserquery
{primary_set_of_instructions}
9
foreasierreferenceandunderstanding.
179

a. A response is considered relevant if it
10
address every component of the user’s
#### **II. Explicit Penalties (What to
11
query. Arelevantresponseshouldincor-
penalize):**
(cid:44)→
porate the specific figures, constraints,
{penalizing_instructions}
12
anddetailsmentionedintheuser’squery,
13
and answer the questions immediately
#### ** III. Key Points to note:**
14
withoutgenericintroductions.
{additional_instructions}
15
b. Anypartialrelevanceoradditionalcon-
---
16
textnotrelevanttothequeryispenalized.
17
**Query:** {query}
18
B ModularRAGforContextAnalysis
19
**Responses to Rank:**
20 Goal. Given a user query, the context-analysis
{anonymized_shuffled_model_responses}
21 phase assembles a compact, high-signal context
"""
22 packfromtwospecializedcorpora: (i)Behavioral
insights (behavioral economics and psychology)
and(ii)Financialconcepts(mainstreampersonalfi-
1. Accuracy:
nanceknowledge). Thecontextpackisthenpassed
a. The goal of this prompt is to direct the totheresponsegenerator.
model to review the search results and
Corpora. Behavioralinsightsaresourcedfrom
thequerytoestimatetheaccuracyofthe
peer-reviewedresearchandreputablepsychology
output.
venues, complemented by carefully selected psy-
b. Theresponsesarepenalizedifandonlyif
chologyblogsforpractitionerframing. Financial
theresponsesdemonstratewrong/harm-
conceptsaredrawnfrompractical,high-visibility
ful advice (or) inappropriate financial
sources such as Investopedia, Bogleheads, and
conceptstothequery.
otherwidelycitedpersonal-financeviewpoints. All
c. Themodelisspecificallyinstructednot
rawpagesareconvertedtoMarkdownwithheaders
to penalise on the style or relevance of
andsectionstructurepreservedtoretaindocument
theresponseandsolelyfocusontheac-
semantics.
curacyofthefinancialconceptsprovided
inthetext. Thisguidesthemodeltorank Preprocessingandindexing.
solelybasedontheaccuracyofthefinan-
cialconceptspresentintheresponse. • Scraping & normalization: We scrape public
pages(respectingrobots/terms), removeboiler-
2. Plausibility:
plate(nav,ads),andnormalizetoMarkdownwith
a. A response is defined to be plausible if stableheadings.
itsoundsreasonableandbelievabletoa
• Semanticchunking: Documentsaresegmented
typicaluser. Someofthekeycharacter-
into modular chunks along header/semantic
isticsinclude
boundaries to keep each chunk topically coher-
• Logicalflowandcoherentreasoning
ent; we attach metadata (source, URL or han-
structure
dle, snapshot time, section path, corpus tag:
• Sensibleapproachtotheproblem
behavioralorfinancial).
b. Aresponseispenalizedifitcontainsun-
necessarilyverboseorcontainexcessive • Denseindexing: Eachchunkisembeddedwith
detail. Theresponsesarealsopenalized text-embeddings-large-003 and stored in a
iftheycontaincomplexorhard-to-follow vectordatabsase(ChromaDB).
reasoning.
c. Themodelisspecificallyinstructednot Retrievalandre-ranking(perquery).
topenaliseontheaccuracyorrelevance
1. Dual retrieval: From each index, retrieve the
oftheresponses.
top-k candidates (k=25) using the query em-
3. Relevance: bedding.
180

2. Cross-encoder re-ranking: Concate- • Penalties. Deductionsoccuriff theanswercon-
nate candidates from both corpora and tainswrongorharmfulguidance,ormisapplies
re-rank with a lightweight cross-encoder financialconceptstotheuser’ssituation.
(sentence-transformers/all-minilm-l12-v2);
|     |     |     |     |     |     | • Non-considerations. |     | Style,tone,verbosity,and |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | ------------------------ | --- | --- |
keeptop-m(m=15).
evenpartialcoveragearenotpenalized;thejudge
3. LLMsynthesis/filter: AfastLLM(gemini-2.0- isinstructedtofocusexclusivelyoncorrectness.
| flash) | receives {top-m | chunks, |     | query} | and (a) |     |     |     |     |     |
| ------ | --------------- | ------- | --- | ------ | ------- | --- | --- | --- | --- | --- |
Plausibility(reasoningquality).
| extractssalientfacts, |     | definitions, |     | anddecision |     |              |                               |     |     |     |
| --------------------- | --- | ------------ | --- | ----------- | --- | ------------ | ----------------------------- | --- | --- | --- |
|                       |     |              |     |             |     | • Objective. | Assesswhethertheanswerreadsas |     |     |     |
criteria;(b)discardsresidualoff-topicspans;(c)
reasonableandbelievabletoatypicaluser—i.e.,
emitsastreamlined,source-attributedcontext.
|     |     |     |     |     |     | it exhibits | a clear | logical flow and | a coherent |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | ---------------- | ---------- | --- |
problem-solvingstructure.
| Assemblyandhandoff. |     | Thestreamlinedcontext |     |     |     |     |     |     |     |     |
| ------------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(withinlinesourceattributionsandcorpustags)is
|         |               |          |        |     |           | • Penalties. | Overlyverbose,needlesslycomplex, |     |     |     |
| ------- | ------------- | -------- | ------ | --- | --------- | ------------ | -------------------------------- | --- | --- | --- |
| passed, | together with | the user | input, | to  | the final |              |                                  |     |     |     |
orhard-to-followchainsofreasoningarepenal-
LLMthatcompletesthecontext-analysisphase.
ized.
| Behavioralvs. | financialmoduleroles. |     |     |     | Thebe- |                       |     |                     |     |     |
| ------------- | --------------------- | --- | --- | --- | ------ | --------------------- | --- | ------------------- | --- | --- |
|               |                       |     |     |     |        | • Non-considerations. |     | Factual correctness |     | and |
havioralmodulesurfacescognitive-biasdescrip- topicalcoveragearenotscoredhere;thelensis
tors,debiasingtactics,anduser-statecues(e.g.,loss
purelyrhetorical/structural.
| aversionframing,presentbiasprompts). |     |     |     | Thefinan- |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Relevance(taskalignment).
| cial module  | surfaces    | actionable | rules   | of          | thumb, |              |                                  |     |     |     |
| ------------ | ----------- | ---------- | ------- | ----------- | ------ | ------------ | -------------------------------- | --- | --- | --- |
|              |             |            |         |             |        | • Objective. | Verifythattheresponsedirectlyad- |     |     |     |
| definitions, | procedures, | and        | typical | constraints |        |              |                                  |     |     |     |
(e.g.,contributionlimits,insuranceconcepts,pay- dresseseverycomponentoftheuser’squery,in-
offorderingheuristics). Bothmodulescontributeto corporates the user’s numbers, constraints, and
thesamecontextpack;behavioralcuesguidehow context,andanswerswithoutgenericpreambles.
| advice is | framed, while | financial |     | chunks | ground |              |                   |            |     |          |
| --------- | ------------- | --------- | --- | ------ | ------ | ------------ | ----------------- | ---------- | --- | -------- |
|           |               |           |     |        |        | • Penalties. | Partial coverage, | tangential |     | content, |
whatadviceisprovided.
orextracontextnotpertinenttothequeryispe-
| Limitations. | (1)Coverageandstalenessdepend |     |     |     |     | nalized. |     |     |     |     |
| ------------ | ----------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
onthesnapshotofpublicsources;(2)blogscanin-
|     |     |     |     |     |     | • Non-considerations. |     | Factualaccuracyandstylis- |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | ------------------------- | --- | --- |
troducestylebiasdespitere-ranking;(3)thesynthe-
ticpolishareignoredforthisaxis.
sisstepmayover-prioritizewell-structuredsources.
| Wemitigatethesebypreservingsourceattributions, |     |     |     |     |     | C.2 BordaPoints |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
trackingsnapshottimestamps,andpromptingsyn-
|     |     |     |     |     |     | Definition. | For a listwise | ranking | of n systems, |     |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------- | ------------- | --- |
thesistopreferhigher-prioritysourceswhencon-
|     |     |     |     |     |     | theitemplacedatrankr |     | (r = 1isbest)receivesa |     |     |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ---------------------- | --- | --- |
flictsarise.
Bordascore
|     |     |     |     |     |     |     | b   | = n−r, |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
C DeeperEvaluationResults
sothetopentrygetsn−1pointsandthelastgets
C.1 ScoreDefinitionsandRationale
0.
| We evaluate | responses | along | three | orthogonal |     |             |                                 |     |     |     |
| ----------- | --------- | ----- | ----- | ---------- | --- | ----------- | ------------------------------- | --- | --- | --- |
|             |           |       |       |            |     | Motivation. | Bordaaggregationiswell–suitedto |     |     |     |
axes—Accuracy,Plausibility,andRelevance—to LLM-as-a-judgeexperimentswhererelativequal-
separatefactualcorrectness,reasoningquality,and
itymattersmorethanabsolutescores:
| taskalignment. | Thisdecompositionavoidsasingle |     |     |     |     |     |     |     |     |     |
| -------------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
scalar that can reward fluent but unsafe answers • Full-order utilisation: every position con-
or penalize terse yet correct ones, and it enables tributes signal, ensuring that small but con-
targetederroranalysisandablations. sistentadvantagesarecapturedratherthandis-
cardedbywinner-takes-allrules.
Accuracy(financialcorrectness).
• Objective. Judge reviews the response against • Cardinal comparability: with a fixed candi-
thequeryandretrievedevidenceandscoresonly date set, raw points can be averaged across
the validity of financial concepts, calculations, queriesandjudgeswithoutnormalisation,giv-
| andadvice. |     |     |     |     |     | ingastable,interpretablemean. |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
181

• Robustnesstomildnoise: swappingadjacent anyonedemonstrationset. Asubsampleofthese
middlerankschangesthetotalbyonly±1,so rankingswerefurthervalidatedbyo4-minimodel
individualjudgeidiosyncrasiesexertlimited toconsolidatetherelativeperformance.
influenceonthefinalaverage.
|     |     |     |     |     |     | Scoring | and aggregation |     | (per criterion). |     | For |
| --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ---------------- | --- | --- |
eachquery,judgesperformmulti-shotlistwiserank-
| Interpretation. |     | Higher | mean | Borda | points in- |     |     |     |     |     |     |
| --------------- | --- | ------ | ---- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
dicatethatasystemoutranksitspeersmoreoften. ingoveranonymizedoutputsusingtherubricsin
Themaximumpossiblemeanisn−1;thegapto Sec. C. Ranks are converted to raw Borda points
|     |     |     |     |     |     | b = n−r. | Wethen: |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ------- | --- | --- | --- | --- |
thisceilingoffersanintuitivesenseofhead-room.
Limitations.
1. averagebacrossshuffles/repeatsforeachjudge;
| • Rank-reversal: |     | insertingorremovingacandi- |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2. averageacrossthejudgestoobtainaper-query,
datecanchangeeverysystem’sscore,compli-
per-criterionscoreforeachmodel;
catinglongitudinalcomparisons.
3. averageacrossallquerieswithinacategory(e.g.,
• IndependenceofIrrelevantAlternatives(IIA)
the“overall”setoraPFsubcategory)toobtain
violation: a judge’s relative preference be- the model’s criterion-wise mean in that cate-
tweentwosystemscanaffect,andbeaffected
gory.
by,ranksassignedtoothers.
ThestackedbarsinFig.2displaythesecriterion-
• Equal-intervalassumption: themethodtreats wisemeans(Accuracy,Plausibility,Relevance)for
| the   | gap      | between    | successive | ranks | as uni-     |             |              |                |     |     |         |
| ----- | -------- | ---------- | ---------- | ----- | ----------- | ----------- | ------------ | -------------- | --- | --- | ------- |
|       |          |            |            |       |             | each model. | For a single | category-level |     |     | number, |
| form, | ignoring | situations |            | where | judges per- |             |              |                |     |     |         |
wealsoreporttheunweightedaverageofthethree
ceivelargerqualityjumpsnearthetop.
criterion-wisemeansasthemodel’sfinalrepresen-
tationscoreinthatcategory.
| • Strategicsusceptibility: |     |     | ifhumanjudgesknow |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
whatinfluencestheaggregation,theycouldin-
C.4 OverallCategoryScores(Accuracy,
flateordeflatelowerrankstobenefitafavored
Plausibility,Relevance)
system.
|     |     |     |     |     |     | We report | criterion-wise | means | derived | from | the |
| --- | --- | --- | --- | --- | --- | --------- | -------------- | ----- | ------- | ---- | --- |
C.3 LLM-JuryProtocol raw Borda points assigned by the LLM jury
LLM-based judging scales across topics, is inex- (Sec. C.3). For each criterion and model, scores
areaveragedacrossjudgesandquerieswithinthe
| pensive, | and achieves |     | strong | agreement | with hu- |             |                 |     |     |     |     |
| -------- | ------------ | --- | ------ | --------- | -------- | ----------- | --------------- | --- | --- | --- | --- |
|          |              |     |        |           |          | overallset. | Higherisbetter. |     |     |     |     |
manraterswhenrubricsareexplicitandtaskcon-
textisprovided. Italsocapturesholisticqualities Accuracy. Figure 3 shows a size-tilted pattern:
(e.g.,coherence,taskfit)thatsingle-numbersimi-
QwQ-32B(reasoning)leads,followedbyGemma3-
laritymetricsmaymiss.
|     |     |     |     |     |     | 27B-itandGemma3-12B-it. |     |     | Mistral-Small-24Bsits |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --------------------- | --- | --- |
Itshouldbenotedthatzero-shotjudgingisvul-
|     |     |     |     |     |     | betweenthistopclusterandtherest. |     |     |     | Theproposed |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | ----------- | --- |
nerabletopositionbias(earlieritemsrankhigher),
8Bmodelismid-pack—behindtheleadersandthe
same-familybias(preferenceforoutputsfromthe
24Bbaseline,butaheadofseveral7–14Bbaselines.
judge’sownfamily),andprompt/leniencyvariance.
Thispointstofactualcalibrationandretrieval/verifi-
Wetherefore(i)usemulti-shotpromptstoanchor
cationastheprimaryleverstoclosethegap,rather
| criteria, | (ii) evaluate | with | listwise | ranking | on in- |     |     |     |     |     |     |
| --------- | ------------- | ---- | -------- | ------- | ------ | --- | --- | --- | --- | --- | --- |
thanrewritingorstylistictuning.
| dependently | shuffled | candidate |     | lists, | and (iii) di- |     |     |     |     |     |     |
| ----------- | -------- | --------- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- |
AsshowninFig.4,QwQ-32Branks
| versifyjudgesacrossmodelfamiliestominimize |     |            |                     |            |          | Plausibility.                      |                 |                            |               |          |       |
| ------------------------------------------ | --- | ---------- | ------------------- | ---------- | -------- | ---------------------------------- | --------------- | -------------------------- | ------------- | -------- | ----- |
| correlatedbias.                            |     |            |                     |            |          | first,withGemma3-27B-itnext.       |                 |                            | Theproposed8B |          |       |
|                                            |     |            |                     |            |          | clustersnearthefront:              |                 | itexceedstheMistral-Small- |               |          |       |
| Judge pool                                 | and | prompting. |                     | We employ  | two      |                                    |                 |                            |               |          |       |
|                                            |     |            |                     |            |          | 24BbaselinebuttrailsGemma3-12B-it. |                 |                            |               | Thissug- |       |
| mainheterogeneousjudges:                   |     |            | DeepSeek-v3-0324(5- |            |          |                                    |                 |                            |               |          |       |
|                                            |     |            |                     |            |          | gests that                         | the dataset     | structure                  | and           | few-shot | con-  |
| shot), Kimi-k2                             |     | (3-shot).  | For                 | each query | and cri- |                                    |                 |                            |               |          |       |
|                                            |     |            |                     |            |          | ditioning                          | induce coherent |                            | reasoning     | steps    | and a |
terion(Accuracy,Plausibility,Relevance),judges
sensibleflowevenatmidscale.
| rank anonymized |     | model | outputs | in a | single list. |     |     |     |     |     |     |
| --------------- | --- | ----- | ------- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
Few-shotexemplarsareheldconstantwithinarun Relevance. Figure5indicatesstrongtaskalign-
and varied across repeats to reduce overfitting to ment at the top end (QwQ-32B, Gemma3-27B-it,
182

Figure3: Accuracy(meanrawBordapointsperquery, Figure4: Plausibility(meanrawBordapoints). The
averagedoverjudges). Asize-drivenleadisvisible;the proposed8Bclustersnearthefrontandmatchesor
proposed8Bismid-pack,indicatingfactualcalibration exceedsseverallargerbaselines,reflectingstrong
astheprimaryimprovementlever. logicalflowandcoherentreasoning.
Gemma3-12B-it). The proposed 8B ranks next parameter,holdingtheevaluationprotocolfixed. It
|        |       |                  |     |            |     |          | is not a | substitute | for | absolute | scores | (Sec. | C.4), |
| ------ | ----- | ---------------- | --- | ---------- | --- | -------- | -------- | ---------- | --- | -------- | ------ | ----- | ----- |
| (4/8), | ahead | of the remaining |     | baselines, |     | suggest- |          |            |     |          |        |       |       |
ingitreliablymapsuserconstraintsandaddresses butacomplementarylensforcost-,latency-,and
allpartsofthequerywithoutdriftingintogeneric memory-constraineddeployments.
| preambles. |     | The residual | gap | likely | reflects | cases |           |             |     |        |     |       |          |
| ---------- | --- | ------------ | --- | ------ | -------- | ----- | --------- | ----------- | --- | ------ | --- | ----- | -------- |
|            |     |              |     |        |          |       | Relevance | efficiency. |     | Figure | 6   | shows | the pro- |
thatrequireexhaustiveedgehandling(e.g.,niche
8B
|             |        |        |      |       |        |          | posed | model | with | the | highest | Borda-per- |     |
| ----------- | ------ | ------ | ---- | ----- | ------ | -------- | ----- | ----- | ---- | --- | ------- | ---------- | --- |
| eligibility | rules) | rather | than | broad | intent | recogni- |       |       |      |     |         |            |     |
parameterinRelevance,followedbyGemma3-12B-
tion.
it,thenMistral-7B-v0.3andLlama3-8B.Largerea-
Cross-criterion takeaway. Across criteria, the soningmodels(e.g.,QwQ-32B,Gemma3-27B-it)
|     |     |     |     |     |     |     | trail on | this per-parameter |     |     | metric | despite | strong |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | --- | ------ | ------- | ------ |
proposed8Bmodelisplausibility–andrelevance-
|                                        |     |     |     |     |     |     | absolute | relevance | (Fig. | 5), | indicating |     | diminish- |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | --- | ---------- | --- | --------- |
| competitivewhilelaggingmostonaccuracy. |     |     |     |     |     | The |          |           |       |     |            |     |           |
nextstepsofimprovementisthereforetoprioritize ingreturnsinalignmentperunitcapacityatlarger
scales.
| factual | grounding | and | numeric | checking: |     | adding |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
targetedretrieval,ruletables,andlightweightcal-
|          |        |        |       |     |         |          | Plausibilityefficiency. |     |     | AsshowninFig.7,the |     |     |     |
| -------- | ------ | ------ | ----- | --- | ------- | -------- | ----------------------- | --- | --- | ------------------ | --- | --- | --- |
| culation | guards | should | yield | the | largest | absolute |                         |     |     |                    |     |     |     |
proposed8Bagainleads,withMistral-7B-v0.3and
gainsrelativetoeffort.
|     |     |     |     |     |     |     | Gemma3-12B-it |     | closebehind(virtuallytied), |     |     |     | fol- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------------------- | --- | --- | --- | ---- |
lowedbyLlama3-8B.Thissuggeststhatthedataset
| C.5 | ParameterEfficiency: |     |     | Category-wise |     |     |           |     |          |              |     |       |        |
| --- | -------------------- | --- | --- | ------------- | --- | --- | --------- | --- | -------- | ------------ | --- | ----- | ------ |
|     |                      |     |     |               |     |     | structure | and | few-shot | conditioning |     | yield | coher- |
BordaperBillionParameters
entreasoningwithhighutilitydensity—qualityper
Toevaluateparameterefficiencyratherthanabso-
parameter.
| lute quality,     |     | we compute     | a   | per-parameter |              | utility |                     |     |     |                       |     |     |     |
| ----------------- | --- | -------------- | --- | ------------- | ------------ | ------- | ------------------- | --- | --- | --------------------- | --- | --- | --- |
|                   |     |                |     |               |              |         | Accuracyefficiency. |     |     | InFig.8,theproposed8B |     |     |     |
| foreachcriterion. |     | FormodeliwithP |     |               | i billionpa- |         |                     |     |     |                       |     |     |     |
rametersandmeanrawBordapoints ¯b oncrite- topsAccuracyperparameter,followedbyMistral-
i,c
|        |                                     |     |     |     |     |      | 7B-v0.3 | and Gemma3-12B-it |     |     | (near-tie). |     | Models |
| ------ | ----------------------------------- | --- | --- | --- | --- | ---- | ------- | ----------------- | --- | --- | ----------- | --- | ------ |
| rion c | ∈ {Accuracy,Plausibility,Relevance} |     |     |     |     | (av- |         |                   |     |     |             |     |        |
thatdominateabsoluteaccuracy(Sec.C.4)deliver
eragedoverjudgesandquerieswithinthecategory),
| wedefine |     |     |     |     |     |     | lower accuracy  |     | per parameter, |             | implying |        | that tar- |
| -------- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- | ----------- | -------- | ------ | --------- |
|          |     |     |     |     |     |     | geted grounding |     | and            | calculation |          | checks | can be    |
¯b
morecost-effectivethanincreasingmodelsize.
| e = | i,c | (Bordapointsperbillionparameters). |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i,c
P
|     | i   |     |     |     |     |     | Takeawaysandcaveats. |     |     | (1)Theproposed8Bis |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------ | --- | --- | --- |
This ratio captures the marginal productivity of the most parameter-efficient across all three cri-
capacity: howmuchjudgedqualityisobtainedper teria, reinforcing the central claim that careful
183

Figure5: Relevance(meanrawBordapoints). The Figure6: Relevanceefficiency: meanrawBordapoints
proposed8Branksimmediatelybehindthetopthree, perbillionparameters(higherisbetter). Theproposed
aheadofotherbaselines,indicatingconsistentmapping 8Bleads,followedbyGemma3-12B-itandLlama3-8B.
fromuserconstraintstoconcreteanswers.
|                 |        |                |            |     |           | most        | categories | and hovers   | around        | the cohort |
| --------------- | ------ | -------------- | ---------- | --- | --------- | ----------- | ---------- | ------------ | ------------- | ---------- |
| supervision     | can    | substitute     | for scale  | in  | personal- | mean.       |            |              |               |            |
| finance         | tasks. | (2) Efficiency | does       | not | equal ab- |             |            |              |               |            |
|                 |        |                |            |     |           | • Strengths | are        | most visible | in Budgeting, | Em-        |
| solute quality; |        | it informs     | deployment |     | decisions |             |            |              |               |            |
ployment,Planning(andclose-to-meaninInsur-
| wherememory/latencyarebinding. |     |     |     | (3)Theratio |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
ance/Retirement).
| ignores           | runtime | constants | (KV-cache      | bandwidth, |           |     |     |     |     |     |
| ----------------- | ------- | --------- | -------------- | ---------- | --------- | --- | --- | --- | --- | --- |
| batch scheduling) |         | and       | training cost; | it         | should be |     |     |     |     |     |
• WidergapsappearinAuto,Housing,Credit(and
readalongsideabsoluteBordaresultsandsystem- occasionally Investing/Taxes), where locality-
levellatency/memorybudgets. andrule-heavyedgecasesrequiremoreexhaus-
tivecoverage.
C.6 QualitativeCategory-wiseEvaluations
| We analyze |     | twelve | personal-finance |     | subdo- |     |     |     |     |     |
| ---------- | --- | ------ | ---------------- | --- | ------ | --- | --- | --- | --- | --- |
C.6.2 AccuracybySubdomain
| mains—Auto,    |     | Budgeting, | Credit,    | Debt, | Employ-   |                                       |     |     |     |           |
| -------------- | --- | ---------- | ---------- | ----- | --------- | ------------------------------------- | --- | --- | --- | --------- |
|                |     |            |            |       |           | Accuracyisolatesfinancialcorrectness: |     |     |     | adviceand |
| ment, Housing, |     | Insurance, | Investing, |       | Planning, |                                       |     |     |     |           |
calculationsmustberightforthestatedscenario;
| Retirement, | Saving, | Taxes. | For | each, | we report |     |     |     |     |     |
| ----------- | ------- | ------ | --- | ----- | --------- | --- | --- | --- | --- | --- |
styleandcoverageareignored(Sec.C.1).
| criterion-wise                            |       | means | derived from | normalized |            |                 |         |         |               |        |
| ----------------------------------------- | ----- | ----- | ------------ | ---------- | ---------- | --------------- | ------- | ------- | ------------- | ------ |
| Borda points                              | (Sec. | C.3). | The dashed   |            | horizontal |                 |         |         |               |        |
|                                           |       |       |              |            |            | • Absolute      | leaders | are the | larger models | across |
| lineineachpanelmarksthecohort-widemeanfor |       |       |              |            |            | mostsubdomains. |         |         |               |        |
orientation.
• Theproposed8Bmodelismid-packoverall,with
Pleasenotethatthecategory-basedevaluations
competitiveaccuracyinDebt,Planning,Employ-
inthisappendixuserawRedditpostflairs,which
ment,andnotablylargergapsinHousing,Insur-
| differ from         | the | eight thematic | categories |     | curated |                        |     |                   |           |        |
| ------------------- | --- | -------------- | ---------- | --- | ------- | ---------------------- | --- | ----------------- | --------- | ------ |
| forthemainanalysis. |     |                |            |     |         | ance,Taxes(andCredit). |     |                   |           |        |
|                     |     |                |            |     |         | • This pattern         |     | suggests targeted | grounding | (poli- |
C.6.1 RelevancebySubdomain
cy/limittables,calculators)isahigher-leverage
| Relevance | captures | task | alignment: | covering | all |     |     |     |     |     |
| --------- | -------- | ---- | ---------- | -------- | --- | --- | --- | --- | --- | --- |
fixthanstylistictuningforclosingtheremaining
partsoftheuser’srequest,usingtheirnumbers/con-
gap.
straints,andansweringwithoutgenericpreambles
(Sec.C.1).
C.6.3 PlausibilitybySubdomain
• A consistent top cluster is formed by larger Plausibilitymeasuresreasoningflowandreadabil-
reasoning-aligned models. The proposed 8B ity: clearstructure,sensiblesteps,andabsenceof
model sits immediately behind this cluster in unnecessarycomplexity(Sec.C.1).
184

Figure7: Plausibilityefficiency: meanrawBorda Figure8: Accuracyefficiency: meanrawBordapoints
pointsperbillionparameters. Theproposed8Branks perbillionparameters. Theproposed8Btopsthe
first;compact7–8Bbaselinesarecompetitive,while cohort,indicatingthatfactualcalibrationgainscanbe
verylargemodelsshowlowerutilitydensity. achievedmorecheaplythanbyscalingparameters
alone.
• The proposed 8B clusters close to the leaders
Theseresultssuggestprioritizingminimal,high-
acrossmostsubdomains, withstrongerrelative
leverage grounding over further size increases:
showings in Debt and Planning; margins are
include compact, versioned rule/limit tables for
lowerinTaxesandRetirement.
regulation-intensivedomains(e.g.,taxes,insurance,
• Lower margins in regulation-dense areas mir- credit), add lightweight calculators/unit-tests for
rortheaccuracypattern: wherefactsarebrittle, numericsteps,sharpensupervisionwithcontrastive
judgespenalizecircuitousexplanations. edge cases in brittle areas (tax/retirement), diver-
sifyjudgechecks(agreementandjudge-swap),and
extend evaluationto shortmulti-turn interactions
C.7 OverallSummary,Limitations,andNext thatrewardclarifyingquestions.
Steps
D TrainingDetails
Summary. Takentogether,theresultstellasim-
plestory. Onabsolutescores(Sec.C.4),thelargest We fine-tuned the 8B parameter Qwen-3 model
baselines lead across Accuracy, Plausibility, and withAdamWoptimizeronbfloat16precisionand
Relevance, as expected. The proposed 8B model a training split containing 15.6K samples and a
sits just behind this front cluster on Relevance validationsetcontaining2.6ksamples. Wetrained
andPlausibilityandlandsmid-packonAccuracy. themodelforfourepochsusinganoptimalbatch
When we switch to a parameter-efficiency lens sizeof256,resultinginaround220stepsoverall.
(Sec.C.5),thepicturereverses: the8Bmodeldeliv- ThemodelunderwenttrainingonasolitaryA100
ersthehighestBorda-per-parameteracrossallthree GPUwithintheRunpodcloudGPUinfrastructure
metrics, indicating unusually high utility density for3hours.
foritssize. Thesubdomainbreakdown(Sec.C.6)is Wepreservedthreecheckpointsperepoch,with
consistentwithbothviews: the8Bmodelissteady theoptimalvalidationlossattainedatstep101. The
orabove-meanineverydaytaskssuchasBudgeting, trainingusedacosinelearningrateschedulewitha
Planning, Employment (and shows strong plausi- maximumlearningrateof5×10−5,a10%linear
bility in Debt), while gaps widen in regulation- warm-up period of 21 steps (a warmup ratio of
andtable-heavyareassuchasHousing,Insurance, 10%), and a minimum learning rate of 5×10−6.
Taxes,Credit(andoccasionallyAuto/Investing). In Gradientswereconstrainedtoaglobalnormof1,
short, scale drives absolute peaks, but careful su- weightdecaywasestablishedat0.01,andallother
pervisionyieldscompetitivequality—andsuperior parameters adhered to the default conventions of
efficiency—atmid-scale. theHuggingFaceTrainer.
185

Figure9: Category-wiseRelevance. Theproposed8Bmodeltypicallysitsjustbehindtheleadingclusterandnear
thecohortmean;gapsarelargestinedge-case,rule-denseareas(e.g.,Auto,Housing,Credit).
186

Figure10: Category-wiseAccuracy. Largermodelsleadoverall;theproposed8Bismid-packwithsmallergapsin
everydayplanningtasksandlargergapswhereyear-/jurisdiction-specificrulesdominate(e.g.,Housing,Insurance,
Taxes).
187

Figure11: Category-wisePlausibility. Theproposed8Bdeliverscoherentreasoningneartheleadingcluster,with
smallermarginsinroutineplanningtasksandlargeronesinregulation-denseareas(e.g.,Taxes,Retirement).
188

E SampleModelResponses
|     |     |     |     |     | start a side | business, | enjoy | life.” | (Not | tailored | to  |
| --- | --- | --- | --- | --- | ------------ | --------- | ----- | ------ | ---- | -------- | --- |
theuser;repeats“startasidebusiness.
Toprovideaqualitativeassessmentofourmodel’s
Analysis
| capabilities,                                | this appendix               | details | three | compara- |            |          |     |            |     |         |     |
| -------------------------------------------- | --------------------------- | ------- | ----- | -------- | ---------- | -------- | --- | ---------- | --- | ------- | --- |
| tivecasestudies.                             | Eachcaseisstructuredarounda |         |       |          |            |          |     |            |     |         |     |
|                                              |                             |         |       |          | • Judge    | Outcome: |     | Baseline-L | >   | Ours–8B | >   |
| real-worlduserquery,presentingtheabridgedre- |                             |         |       |          | Baseline-S |          |     |            |     |         |     |
sponsesfromourmodel(Ours-8B)alongsidetwo
baselinemodelsofdifferentsizes(Baseline-Land • Reasoning: Baseline-L is the most accu-
|              |          |          |         |            | rate          | and relevant: |            | it adds | specifics | for | the  |
| ------------ | -------- | -------- | ------- | ---------- | ------------- | ------------- | ---------- | ------- | --------- | --- | ---- |
| Baseline-S). | For each | case, we | outline | the query, |               |               |            |         |           |     |      |
|              |          |          |         |            | self-employed |               | (SEP-IRA), |         | provides  | a   | con- |
summarizethecontextprovidedtothemodels,dis-
creteallocationsketch,andoutlinesaclearse-
playthegeneratedresponses,andconcludewitha
judge’sfinalrankingandarationalebasedonthe quence(EF→tax-advantaged→brokerage).
Ours–8Bisstrong,empathetic,andpractical
coreprinciplesofaccuracy,relevance,andplausi-
|     |     |     |     |     | butmorehigh-level. |     |     | Baseline-Sisgenericand |     |     |     |
| --- | --- | --- | --- | --- | ------------------ | --- | --- | ---------------------- | --- | --- | --- |
bility.
poorlytargeted.
CaseC1(Comparative)—Budgeting&Early
CaseC2(Comparative)—FullRoth
Investingat18
ConversionwithMixedPositions
Query(Abridged)
Query(Abridged)
| “I’m 18  | with about $40k | in checking. |                  | I run a |                                    |     |                            |                    |     |     |      |
| -------- | --------------- | ------------ | ---------------- | ------- | ---------------------------------- | --- | -------------------------- | ------------------ | --- | --- | ---- |
|          |                 |              |                  |         | “Early50s,Trad.                    |     | IRAhastwonear-worthlesspo- |                    |     |     |      |
| business | (will reinvest  | some),       | have very        | low ex- |                                    |     |                            |                    |     |     |      |
|          |                 |              |                  |         | sitionsandonelargegainer.          |     |                            | FullRothconversion |     |     |      |
| penses,  | and my parents  | cover        | college/housing. |         |                                    |     |                            |                    |     |     |      |
|          |                 |              |                  |         | wouldpushincomeinthe32–35%bracket. |     |                            |                    |     |     | Con- |
WhatshouldIdosoit’snotjustsittingidle?”
vertallatonceorphaseit?”
ContextTitles(Summary)
ContextTitles(Summary)
• Emergencyfund(3–6monthsofspend)
• Rothconversiontaxation;Form8606report-
ing
• Roth/SEP-IRAbasics
• Bracketmanagementandtiming;liquidityto
• Low-costindexfunds
paytax
• Businessreinvestmentdiscipline
|     |     |     |     |     | • Selling | losers | post-conversion; |     |     | market- |     |
| --- | --- | --- | --- | --- | --------- | ------ | ---------------- | --- | --- | ------- | --- |
volatilityrisk
AbridgedModelResponses
Ours–8B Ihearthemixofexcitementandcon- AbridgedModelResponses
fusion... Since you run a business, reinvest a Ours–8B Full conversion now makes strong
| portion. | For the rest, open | a Roth | IRA | (after-tax, |        |         |        |       |           |         |     |
| -------- | ------------------ | ------ | --- | ----------- | ------ | ------- | ------ | ----- | --------- | ------- | --- |
|          |                    |        |     |             | sense. | Convert | entire | Trad. | IRA, then | immedi- |     |
long-horizongrowth)andataxablebrokeragewith ately sell all three holdings inside the Roth and
low-costindexfunds. Beforeinvesting,hold3–6 reallocatetodiversifiedfunds. Steps: computetax;
monthsofexpensesinahigh-yieldsavingsaccount.
|     |     |     |     |     | execute | direct conversion; |     | sell | & reallocate; |     | file |
| --- | --- | --- | --- | --- | ------- | ------------------ | --- | ---- | ------------- | --- | ---- |
Thenallocateacrossbusiness,RothIRA,andbro-
taxes: reportasa‘non-deductiblecontribution
| keragebasedoncomfortwithrisk. |     |     |     |     | (Form8606)‘. |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Baseline-L(32B) Secureanemergencyfundin Baseline-L(32B) Explainsthattaxesarebased
a high-yield account; consider reinvesting in the on total IRAvalue; lossescan’toffset gainshere.
business with a written plan. As self-employed, Laysoutfullvs. phasedconversion,bracketcreep,
consideraSEP-IRAandRoth/TraditionalIRA.Af- irreversibility,andliquidity(useoutsidefundsfor
terthat,diversifyviaabrokeragewithindexETFs tax). Emphasizesabilitytoliquidateloserstax-free
(e.g., S&P 500). Includes a sample split: emer- inRothandnotesmarket-dropriskpost-conversion.
| gency fund, | business, | retirement | accounts, | and |                        |            |       |      |            |         |     |
| ----------- | --------- | ---------- | --------- | --- | ---------------------- | ---------- | ----- | ---- | ---------- | ------- | --- |
|             |           |            |           |     | Provides               | actionable | steps | (run | scenarios, | convert |     |
| ETFs.       |           |            |           |     | losersfirstifphasing). |            |       |      |            |         |     |
Baseline-S (7B) Ten generic ideas: emergency Baseline-S (7B) High-level overview of Roth
fund, pay off debt, invest in stocks/bonds/real es- conversionbasics;repeatsgeneraladvice;defersto
tate,retirementsavings,education,charity,travel, anadvisor;nobracketmodellingorconcretesteps.
189

| Analysis |     |     |     |     |     |     | Analysis |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
• Judge Outcome: Baseline-L > Ours–8B > • Judge Outcome: Baseline-L > Ours–8B >
| Baseline-S |     |     |     |     |     |     | Baseline-S |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
• Reasoning: Baseline-Lismostaccurateand • Reasoning: Baseline-Lismostaccurateand
relevant: covers bracket spillover, irrevoca- relevant: it answers “am I missing a better
|                               |          |      |     |        |            |            | option?”                           | with | a structured |     | comparison, | con-    |
| ----------------------------- | -------- | ---- | --- | ------ | ---------- | ---------- | ---------------------------------- | ---- | ------------ | --- | ----------- | ------- |
| bility,                       | external | cash | for | taxes, | and        | volatility |                                    |      |              |     |             |         |
|                               |          |      |     |        |            |            | cretetrade-offs,andclearnextsteps. |      |              |     |             | Ours–8B |
| risk,withclearoptions(fullvs. |          |      |     |        | phased)and |            |                                    |      |              |     |             |         |
steps. Ours–8Bisconfidentandpracticalbut is strong and user-aligned but single-track
containsamaterialfilingerror(mislabelsa (HYSAonly),offeringlesseducationaldepth
|            |     |      |                |     |              |     | for alternatives. |     |     | Baseline-S | is  | accurate but |
| ---------- | --- | ---- | -------------- | --- | ------------ | --- | ----------------- | --- | --- | ---------- | --- | ------------ |
| conversion |     | as a | non-deductible |     | contribution |     |                   |     |     |            |     |              |
onForm8606),reducingAccuracy. Baseline- genericandlightondecisionguidance.
Sisgenericandleasthelpful.
Conclusion
CaseC3(Comparative)—Liquidity&Safety Thesecasestudiesculminateinaclear,yetnuanced,
withUncertainHorizon conclusion about the trade-offs between model
Query(Abridged) scale,architecture,andperformance. Theconsis-
tenttoprankingofthe32BBaseline-Lunderscores
| “Lifechangesahead(move/career/school). |     |     |     |     |     | Ihave |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
thevalueofalarge-scalereasoningmodelforgen-
| $25,000andmayneeditanytime. |           |        |            |      | Worriedabout |          |                                            |              |            |         |                  |      |
| --------------------------- | --------- | ------ | ---------- | ---- | ------------ | -------- | ------------------------------------------ | ------------ | ---------- | ------- | ---------------- | ---- |
|                             |           |        |            |      |              |          | eratingsuperior,detailedfinancialguidance. |              |            |         |                  | How- |
| market                      | dips.     | Is a   | high-yield |      | savings      | account  |                                            |              |            |         |                  |      |
|                             |           |        |            |      |              |          | ever, the                                  | most         | compelling | finding | emerges          | from |
| (HYSA)                      | the right | place, | or         | am I | missing      | a better |                                            |              |            |         |                  |      |
|                             |           |        |            |      |              |          | an efficiency                              | perspective. |            | Our     | 8B non-reasoning |      |
option?”
|     |     |     |     |     |     |     | model showed |     | consistent | performance |     | at just a |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ----------- | --- | --------- |
ContextTitles(Summary) quarterofthesizeofBaseline-L.Itis,inessence,
|        |        |     |                |     |     |       | punching | significantly |     | above | its weight | class, of- |
| ------ | ------ | --- | -------------- | --- | --- | ----- | -------- | ------------- | --- | ----- | ---------- | ---------- |
| • HYSA | basics | and | FDIC/coverage; |     |     | money |          |               |     |       |            |            |
feringapowerfulbalanceofqualityandresource
marketaccounts
|     |     |     |     |     |     |     | economy. | The | key differentiators |     | were | Baseline- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------------- | --- | ---- | --------- |
L’sabilitytohandlemulti-step,nuancedreasoning
| • Short   | CDs | and | ladders; | T-bills; |     | short-term |              |         |            |     |         |           |
| --------- | --- | --- | -------- | -------- | --- | ---------- | ------------ | ------- | ---------- | --- | ------- | --------- |
| bondfunds |     |     |          |          |     |            | and maintain | factual | integrity, |     | an area | where our |
modelfalteredinCaseC2.
| • Liquidityvs. |     | yieldtrade-offs;ratemonitoring |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AbridgedModelResponses
| Ours–8B | Given | immediate-access |     |     |     | needs and |     |     |     |     |     |     |
| ------- | ----- | ---------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
principalsafety,parkingtheentire$25kinaHYSA
| isoptimal.    | HYSAspaybetterthanregularsavings, |              |     |     |       |           |     |     |     |     |     |     |
| ------------- | --------------------------------- | ------------ | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- |
| allow anytime |                                   | withdrawals, |     | and | avoid | CD penal- |     |     |     |     |     |     |
ties. VerifyacompetitiveAPYandkeepthefunds
fullyflexible.
| Baseline-L(32B) |     | ValidatesHYSAforimmedi- |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ateaccess,thencomparesliquid,low-riskalterna-
| tives: money  | market               |            | accounts, | short  |        | CD ladder-  |     |     |     |     |     |     |
| ------------- | -------------------- | ---------- | --------- | ------ | ------ | ----------- | --- | --- | --- | --- | --- | --- |
| ing, T-bills, | and                  | short-term |           | bond   | funds. | Outlines    |     |     |     |     |     |     |
| pros/cons,    | insurance/volatility |            |           | notes, |        | and action- |     |     |     |     |     |     |
ablesteps(openHYSA;optionallyladderasmall
| slice; monitor |     | rates; | named | providers/tickers |     | as  |     |     |     |     |     |     |
| -------------- | --- | ------ | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
examples).
| Baseline-S(7B) |           | ConfirmsHYSAcouldbegood, |         |        |       |       |     |     |     |     |     |     |
| -------------- | --------- | ------------------------ | ------- | ------ | ----- | ----- | --- | --- | --- | --- | --- | --- |
| mentions       | inflation | in                       | general | terms, | lists | money |     |     |     |     |     |     |
marketandshortCDs,butremainsgenericandde-
ferstoanadvisorwithoutacomparisonframework.
190