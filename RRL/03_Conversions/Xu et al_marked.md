Toward Personalized LLM-Powered Agents: Foundations, Evaluation, and
Future Directions
YUEXU,ShanghaiTechUniversity,China
QI’ANCHEN,TongjiUniversity,China
ZIZHANMA,TheChineseUniversityofHongKong,China
DONGRUILIU,ShanghaiArtificialIntelligenceLaboratory,China
WENXUANWANG,RenminUniversityofChina,China
XITINGWANG,RenminUniversityofChina,China
LIXIONG,EmoryUniversity,UnitedStates
WENJIEWANG†,ShanghaiTechUniversity,China
Largelanguagemodelshaveenabledagenticsystemsthatreason,plan,andinteractwithtoolsandenvironmentstoaccomplish
complextasks.Astheseagentsoperateoverextendedinteractionhorizons,theireffectivenessincreasinglydependsonadapting
behaviortoindividualusersandmaintainingcontinuityacrossinteractions,givingrisetopersonalizedLLM-poweredagents(PLAs).
Insuchlong-term,user-dependentsettings,personalizationpermeatestheentiredecisionpipelineratherthanremainingconfinedto
surface-levelresponsegeneration.Thissurveyprovidesacapability-orientedreviewofpersonalizedLLM-poweredagents.Existing
workisorganizedaroundfourinterdependentcapabilities:profilemodeling,memory,planning,andactionexecution.Usingthis
taxonomy,representativemethodsaresynthesizedandanalyzedtoillustratehowusersignalsarerepresented,propagated,and
utilizedacrosstheagentpipeline,highlightingcross-componentinteractionsandrecurringdesignchallenges.Evaluationmetrics
andbenchmarkingparadigmstailoredtopersonalizedagentsarefurtherexamined,alongwithapplicationscenariosrangingfrom
conversationalassistantstodomain-specificexpertsystems.Byclarifyingthedesignspaceofpersonalizationinagentsystems,
thissurveyprovidesastructuredfoundationfordevelopingmoreuser-aligned,adaptive,anddeployableLLM-poweredagents.
CCSConcepts:•Generalandreference→Surveysandoverviews;•Human-centeredcomputing;•Computingmethod-
ologies→Intelligentagents;
AdditionalKeyWordsandPhrases:Personalization,PersonalizedLLM-poweredAgent
ACMReferenceFormat:
Yue Xu, Qi’an Chen, Zizhan Ma, Dongrui Liu, Wenxuan Wang, Xiting Wang, Li Xiong, and Wenjie Wang†. 2026. Toward
PersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections.ACMComput.Surv.1,1(March2026),35pages.
https://doi.org/XXXXXXX.XXXXXXX
1 Introduction
Largelanguagemodels(LLMs)haveevolvedfrompassivetextgeneratorsintogeneral-purposereasoningsystems
capableofunderstandingdiversedata,planningactions,andusingexternaltools.Buildingonthesecapabilities,
LLM-poweredagentsextendLLMsintointegratedsystemsthatdecomposecomplexobjectives,invoketools,interact
withdynamicenvironments,andcoordinatewithhumansorotheragentstoachievehigh-levelgoalsoverextended
†CorrespondingAuthor.
Authors’Contactinformation:YueXu,ShanghaiTechUniversity,China;email:xuyue2022@shanghaitech.edu.cn;Qi’anChen,TongjiUniversity,
China;email:2250951@tongji.edu.cn;ZizhanMa,TheChineseUniversityofHongKong,China;email:zzma2@cse.cuhk.edu.hk;DongruiLiu,
ShanghaiArtificialIntelligenceLaboratory,China;email:liudongrui@pjlab.org.cn;WenxuanWang,RenminUniversityofChina,China;email:
wangwenxuan@ruc.edu.cn;XitingWang,RenminUniversityofChina,China;email:xitingwang@ruc.edu.cn;LiXiong,EmoryUniversity,United
States;email:lxiong@emory.edu;WenjieWang,ShanghaiTechUniversity,China;email:wangwj1@shanghaitech.edu.cn.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfeeprovidedthatcopiesare
notmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitationonthefirstpage.Copyrightsfor
componentsofthisworkownedbyothersthantheauthor(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,
topostonserversortoredistributetolists,requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2026Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
ACM1557-7341/2026/3-ART
https://doi.org/XXXXXXX.XXXXXXX
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.
6202
raM
61
]IA.sc[
2v08622.2062:viXra

2 • Y.Xuetal.
horizons[1,110,192,204].ThisshiftmarksnotonlyatechnicalexpansionofLLMcapabilitiesbutalsoabroader
shifttowardautonomous,adaptive,andsociallygroundedintelligentassistants.
Asagentsystemsincreasinglysupportlong-terminteractionandautonomousdecision-making,personalization
emergesasacentralrequirementformaintainingcontextualcontinuityandaligningagentbehaviorwithindividual
userpreferencesacrossdomainssuchaseducation,healthcare,andrecommendation[24,139,208].Forpersonalized
LLM-poweredagents(PLAs),personalizationextendsbeyondresponsestyleandoperatesacrossthefulldecision
pipeline,influencinghowagentsinferuserintent,preserveuser-relevantinformationovertime,generatepersonalized
plans,andcarryoutactionsinexternalenvironments[194,261].However,thisbroadenedscopealsointroduces
substantial challenges, including integrating dynamic and multimodal feedback, preserving consistency across
interactingcomponents,reconcilinguser-specificadaptationwithgeneralcompetence,andsafeguardingprivacyand
security.Asaresult,theevaluationofPLAsmustmovebeyondstaticcorrectnessandinsteadaccountforlong-term
effectiveness,adaptability,andusersatisfaction.
Despitethegrowinginterest,reviewsonPLAsremainfragmented.Priorsurveysoftenfocusonisolatedcapabilities
of general LLM-powered agents or isolated components of personalization, such as user modeling and memory
construction[227,260],planningandreasoningstrategies[217],oradaptiveinteractionmechanisms[38,94].Such
capability-specificperspectiveshaveprovidedvaluableinsights,butaunifiedviewofhowpersonalizationobjectives
propagateacrossthefullagentlifecycleisstilllacking.Inparticular,theinteractionsamongdifferentpersonalization
mechanismsandtheirimplicationsforevaluationanddeploymentremaininsufficientlyunderstood.
Toaddressthisgap,thissurveypresentsacapability-orientedandsystem-levelperspectiveonPLAs.Weexamine
personalization as a distributed property instantiated across four interdependent components: profile modeling,
memory,planning,andactionexecution.Thisdecompositionenablesasystematicanalysisofhowuser-specific
signalsarerepresented,propagated,andoperationalizedthroughouttheagentlifecycle,fromintentunderstandingto
real-worldoutcomes.AsillustratedinFigure1,whenanindividualusersubmitsarequest,aPLAcoordinatesthese
fourcapabilitiestoproduceatailoredresponse.Profilerepresentationsandroledefinitionsshapetheagent’sinternal
modeloftheuser,thememorymoduleorganizesandretrievesrelevantcontextualinformation,planningdetermines
personalizeddecisionstrategies,andactionexecutiongroundsthesedecisionsintheexternalenvironment.The
resultingoutcomes,togetherwithsubsequentuserfeedback,inturnrefinetheagent’sinternalrepresentationofuser
preferences,formingaclosedloopthatenablesiterativeandsustainedpersonalizationovertime.
Buildingonthistaxonomy,wereviewrepresentativemethods,benchmarks,andevaluationprotocols,summarize
majorapplicationdomains,andidentifyopenchallengesandfutureresearchdirections.Thesurveyaimstoclarifythe
designspaceofpersonalizedagents,connectbenchmark-drivenresearchwithreal-worlddeploymentrequirements,
andprovideastructuredfoundationfordevelopingtrustworthy,effective,andscalablepersonalizedagentsystems.
Ourcontributionsareasfollows:
(1) WeintroduceaunifiedtaxonomythatorganizespersonalizedLLM-poweredagentsaroundfourcorecapabilities
(profilemodeling,memorymanagement,planning,andactionexecution),providingasystem-levelviewof
howpersonalizationisrealizedacrosstheagentpipeline(§2).
(2) Wepresentanextensivereviewofrecenttechniques,benchmarks,andevaluationprotocols(§3–§7),highlighting
howpersonalizationmechanismsoperatewithinandacrossagentcomponentsandhowpersonalizationis
assessedinpractice.
(3) Wesurveyrepresentativeapplicationdomainsofpersonalizedagentsanddiscussopenchallengesandpromising
researchdirections(§8-§9).
2 FoundationsofPersonalizedLLM-poweredAgents
2.1 LLM-poweredAgents
AnLLM-poweredagentisanautonomoussystemthatintegratesalargelanguagemodelwithexternaltoolsand
utilitiestosupportstep-by-stepinteractionwithopen-endedenvironmentsfortaskcompletion[35].Theenvironment
includesboththeuserandtheexecutioncontext,andischaracterizedbyanexternalstatespaceS thatgoverns
environmentdynamicsandfeedback.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 3
User Profile Modeling
|     |     |     |     |     | Profiles | Memory Schemes | Personalized Retrieval |
| --- | --- | --- | --- | --- | -------- | -------------- | ---------------------- |
(structure+update)
|             |     |               | response-based /      |     |                  |            | content-based /  |
| ----------- | --- | ------------- | --------------------- | --- | ---------------- | ---------- | ---------------- |
|             |     |               | persona-based         |     | +                | textual/   | structure-aware/ |
|             |     |               |                       |     |                  | structured | policy-guided    |
| Individual  |     | Personalized  | Agent Role Definition |     |                  |            |                  |
|             |     |               |                       |     | § 3.  P r o f il | e          |                  |
| User        |     | Agent         | user-substituting /   |     |                  | §4. Memory | Relevant         |
|             |     |               |                       |     | M o d e li n g   |            |                  |
|             |     |               | user-adaptive         |     |                  |            | Memory           |
Request
One-Shot
Execution
|     | Response |     | Outcome |     | §6. Action  |              |                        |
| --- | -------- | --- | ------- | --- | ----------- | ------------ | ---------------------- |
|     |          |     |         |     | Execution   | §5. Planning | user signal grounding/ |
internal refinement
|     |     |     | Post-action |     | Pre-action |     |     |
| --- | --- | --- | ----------- | --- | ---------- | --- | --- |
Feedback-Driven
| User Request ing |     |     | execution-time  |     |                 |               |                        |
| ---------------- | --- | --- | --------------- | --- | --------------- | ------------- | ---------------------- |
|                  |     |     |                 |     | action policy + | Personalized  | clarification seeking/ |
Personalized Response Generation correction +  action grounding Plan user revision/
outcome realization
| Iterative Personalization |     |     |     |     |     |     | non-user feedback |
| ------------------------- | --- | --- | --- | --- | --- | --- | ----------------- |
Fig.1. OverviewofpersonalizedLLM-poweredagents.Uponreceivingauserrequest,theagentcoordinatesprofilemodeling,
memory,planning,andactionexecutiontogenerateatailoredresponse.Interactionoutcomesprovidefeedbackthatrefinesuser
preferencerepresentations,enablingiterativeandlong-termpersonalization.
Ateachtimestep𝑡,theenvironmentisinastate𝑠 thatcapturestheexternallyavailableinformationrelevantto
𝑡
thetask,includinguserinputs,tooloutputs,orotherexternalsignals.Theagentmaintainsaninternalstateℎ ,which
𝑡
capturesaccumulatedcontextsuchasretrievedmemory,intermediatereasoningresults,andinternalrepresentations
usedfordecisionmaking.Theagent’sbehaviorcanbeabstractedasapolicythatselectsanaction𝑎 conditionedon
𝑡
boththecurrentenvironmentstateanditsinternalstate:
|     |     |     |     | 𝜋(𝑎 𝑡|𝑠 | ,ℎ 𝑡). |     |     |
| --- | --- | --- | --- | ------- | ------ | --- | --- |
𝑡
Actions may correspond to natural language responses, planning steps, tool invocations, or other environment
interactions.Theenvironmentthenevolvesaccordingtoacontrolledtransitionprocess,producingasubsequent
externalstate𝑠 ,andtheagentupdatesitsinternalstateaccordinglyas
𝑡+1
|     |     |     | ℎ   | =𝑓(ℎ | ,𝑎 ,𝑠 𝑡+1). |     |     |
| --- | --- | --- | --- | ---- | ----------- | --- | --- |
|     |     |     | 𝑡+1 | 𝑡    | 𝑡           |     |     |
Startingfromaninitialstate𝑠 0 ,suchasauserqueryortaskspecification,executionproceedsiterativelyuntila
terminationconditionismet,yieldingatrajectory
|     |     |     | 𝜏 =(𝑠 ,ℎ | ,𝑎 ,𝑠 | ,...,𝑎 ,𝑠 | 𝑇). |     |
| --- | --- | --- | -------- | ----- | --------- | --- | --- |
|     |     |     | 0        | 0 0 1 | 𝑇−1       |     |     |
Thistrajectoryreflectstheagent’sevolvinginterpretationofthetaskanditsinteractionhistory.Foranalysisor
evaluation purposes, execution outcomes can be assessed using a feedback or reward function defined over the
| trajectory,denotedas𝑟 |     | =R(𝜏). |     |     |     |     |     |
| --------------------- | --- | ------ | --- | --- | --- | --- | --- |
Atthesystemlevel,LLM-poweredagentsrelyonasetoftightlycoupledcognitivecapabilitiesthatenableadaptive
andgoal-directedbehavior[110,204].Profilingshapeshowtheagentinterpretsitsroleandoperatingcontext.Memory
supportscontinuitybyretainingandorganizinginformationacrossinteractions.Planninggovernsthetransformation
ofhigh-levelobjectivesintostructureddecisionprocesses.Actionexecutionrealizesthesedecisionsthroughtooluse
ordirectinteractionwiththeenvironment.Together,thesecapabilitieselevatelargelanguagemodelsintointeractive
decision-makingsystemscapableofsustainedautonomy.
2.2 PersonalizedLLM-poweredAgents
ApersonalizedLLM-poweredagentisanLLM-basedagentwhoseinternalpipelineisadaptedtoindividualusers
throughuser-specificpreferences.Foreachuser𝑢 ∈U,theagentmaintainsarepresentationoftheuser’spreferences
𝑝 inferredfrominteractionhistory,feedback,orexplicitinput.
𝑢
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

4 • Y.Xuetal.
Ateachtimestep𝑡,theenvironmentisinastate𝑠 ,andtheagentmaintainsaninternalstateℎ(𝑢) specifictothe
𝑡 𝑡
user.Theagentinterpretsandactsuponuserpreferencesbyconditioningitsdecisionpolicyon𝑝 .Thisyieldsa
𝑢
user-conditionedpolicy
𝜋(𝑎 𝑡|𝑠
𝑡
,ℎ
𝑡
,𝑝 𝑢),
whichselectsanaction𝑎 giventhecurrentenvironmentstate,internalstate,anduserpreferences.Theenvironment
𝑡
transitionstoanewstate𝑠 ,andtheagentupdatesitsinternalstateas
𝑡+1
ℎ
𝑡+1
=𝑓(ℎ
𝑡
,𝑎
𝑡
,𝑠
𝑡+1
,𝑝 𝑢),
whereuserpreferencesmaybeexplicitlystoredwithintheinternalstateorprovidedasanexternalconditioning
signal.Executingthispolicyfromaninitialstateproducesauser-conditionedinteractiontrajectory
𝜏(𝑢) =(𝑠
0
,ℎ
0
(𝑢),𝑎
0
(𝑢),𝑠
1
,...,𝑠 𝑇),
wherethesuperscript(𝑢)indicatesthatthetrajectoryisinducedbydecision-makingconditionedonuserpreferences.
Personalizationreferstotheprocessthroughwhichuserpreferencesareaccumulated,represented,andintegrated
intoanagent’sdecisionpipeline,allowingthesametaskspecificationQtogiverisetodifferentoutcomesfordifferent
users. Through repeated interaction, the agent collects user-centric data D𝑢 and refines an internal preference
representation𝑝ˆ
𝑢
=𝑝(D𝑢),whichconditionssubsequentactionselection.Atanabstractlevel,personalizationcan
beviewedasfavoringdecisionsthatyieldhigheruser-alignedutilityoverinteractiontrajectories:
𝜋
𝑢
∗ ∝ argm
𝜋
axE
𝜏(𝑢)∼𝜋(·|Q,𝑝ˆ 𝑢)
R𝑢(𝜏(𝑢)),
where𝑝ˆ
𝑢
denotes an internal representation of user preferences maintained by the agent, and R𝑢(𝜏(𝑢)) denotes
feedbackreflectinguser-specificsatisfactionoralignment.
Fromasystemperspective,personalizationformsaclosedinteractionloop.User-specificpreferencerepresentations
conditiontheagent’sperception,reasoning,andactionselection;executedactionsshapesubsequentinteractions;
andtheresultingoutcomesprovidenewsignalsthatrefine𝑝ˆ .Throughrepeatedexecutionofthisloop,personalized
𝑢
LLM-poweredagentsprogressivelyaligntheirbehaviorwithindividualusers,enablinglong-termadaptivityand
consistentuser-specificbehavior.
2.3 User-CentricData
TheinternalrepresentationofuserpreferencesinLLM-powered agentsisgroundedinuser-centric data,which
capturescontextualinformation,feedback,andinteractiontracesassociatedwithaspecificuser.Fromatemporaland
functionalperspective,user-centricdatacanbebroadlydividedintohistoricaldataandinteractiondata.
Historical Data refers to information available before task execution, including user identifiers, demographic
attributes,andrecordsofpriorinteractionsandfeedback.Thiscontextprovidesafront-loadedpriorovertheuserfor
thecurrentepisode,capturingrelativelystableusercharacteristicstogetherwithaccumulatedevidencefrompast
interactions,whichsupportsconsistentbehaviorandcross-taskgeneralization.
InteractionDataisgeneratedduringtaskexecutionandcapturesreal-timeuserinputs,feedback,andcontextual
cues.Itincludesbothexplicitsignals,suchascorrectionsorratings,andimplicitsignals,suchasbehavioralpatterns
or response timing. Interaction data reflects the user’s momentary intent and is critical for guiding immediate
decision-making,includingreasoningadjustmentsanddynamicactionselection.
Thesetwodatatypesenabledual-timescalepersonalization:historicaldatadefineswhotheuseris,whileinteraction
datadetermineshowtheagentshouldactnow.AsillustratedinFigure2,historicaldataguidestheagent’sbehavior
duringinteraction,whileinteractiondatarefinesandexpandsthehistoricalrecord,togetherformingacontinuous
cycleofuser-awareadaptation.
2.4 UserPreferences
UserpreferencesconstitutethecoresignalsthatenablepersonalizationinLLM-poweredagentsbyconditioningtheir
internalstate,decision-makingprocesses,anduser-specificfeedback.Priorworkcommonlycategorizespreferences
according to their mode of expression [87, 261]. Explicit preferences are directly specified by users and can be
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 5
Historical Data Guide Interaction Data
User Demographic Explicit Feedback
Identifiers Attributes
(confirmations, corrections, ratings......)
Historical User Implicit Feedback
Interactions Feedback Refine (response latency, tone, emotions.....)
Fig.2. User-specificdatainpersonalizationprocess.
incorporatedintotheagentwithoutadditionalinference.Implicitpreferencesareinferredindirectlyfrombehavioral
patternsorcontextualcues,reflectinguserjudgmentsinalatentorunder-specifiedform.
Beyondexpressionform,preferencescanbecharacterizedbytheirsemanticfunction,capturingwhichaspect
oftheusertheyencode.Wedistinguishbehavioralpreferences,whichgovernhowuserscommunicateandreason,
andtopicalpreferences,whichspecifywhatusersprioritizeinagivencontext.Behavioralpreferencesencompass
tone,reasoningstyle,generalinteractiontendencies,andpersonality-relatedtraits,andareoftenstableacrosstasks.
Topicalpreferencescoverdomaininterests,factualstances,andlikesordislikestowardspecificentitiesorevents,
andvarymorewithcontext.Bothtypescanbestatedexplicitlyorinferredimplicitly,yieldingthetwo-dimensional
taxonomyinFigure3.
User: Heyyy! Can you help me pick a place for dinner tonight?
User Preference
I?m hungry and excited but totally indecisive.
Assistant: Sure! There are many factors we can consider, such
as cuisine type, price range, location, dietary restrictions, Behavioral
ambiance, popularity, customer reviews, and whether the
restaurant offers unique or innovative dishes. For example, if
you like Asian food, there are Korean, Thai, and Chinese
options, each with different flavor profiles and dining ...... -Avoid long explanations -Extroverted and lively
User: Whoa whoa pause. That?s way too much already. Long - Concise communication -Prefers minimal options
explanations make my head spin and make choosing harder.
Assistant: Got it! Any dietary restrictions or strong dislikes? Explicit Implicit
User: Yep! Important one. I?m allergic to peanuts.
Assistant: Okay. I?ll avoid peanut-containing restaurants.
User: Oh and two more things! I really don?t like spicy food. -Peanut-free food -Dislikes fusion restaurants
Mild only, please. Last time we went to a super trendy fusion
-Non-spicy cuisine -Prefers quiet dining
spot, the food was awful. And it was loud, chaotic, and
stressful. Totally not my vibe... environments
Assistant: Thanks for letting me know. Based on this, I
recommend a traditional Japanese udon restaurant nearby. It?s
peanut-free, mild in flavor, and known for a calm atmosphere.
If you want one alternative, I can suggest a similar option. Topical
User: Perfect!! That sounds exactly right. Thanks a ton!
Fig.3. Exampleofatwo-dimensionaltaxonomyofuserpreferences.Preferencesarecategorizedbytheirexpressionform(explicit
vs.implicit)andsemanticfunction(behavioralvs.topical),illustratedthroughamulti-turnrecommendationscenario.
In practical systems, explicit preferences can be represented in various forms, including reward vectors [10],
preferenceembeddings[141],ornatural-languageprompts[76].Althoughexplicitsignalsareoftenhighlyinformative,
theyaretypicallysparse,whichlimitstheirdirectapplicabilityforoptimization.Asaresult,implicitpreferencesare
frequentlyleveragedthroughin-contextprompting[75],retrieval-augmentedgeneration(RAG;[144]),orpreference
modelingtechniques[45]thatextractstructuredrepresentationsfromuserbehavioralfeedback.Whenperforming
suchanextraction,accountingforthesemanticfunctionofpreferencesenablesmoretargetedmodelingstrategies
andimprovesinterpretability.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

6 • Y.Xuetal.
2.5 Capability-orientedTaxonomy
PersonalizationinLLM-poweredagentsemergesfromthecoordinatedoperationofmultipleinternalcapabilities
ratherthanfromasingleadaptationmodule.Giventhediversityofuserdata,tasksettings,andpreferencetypes,
user-specificsignalsmustberepresented,retained,reasonedover,andoperationalizedthroughoutthewholepipeline.
Wethereforeadoptacapability-orientedtaxonomy(illustratedinFigure4)thatorganizespersonalizationintofour
interdependentcomponents:
PersonalizationinLLM-poweredagentsdoesnotarisefromasingleadaptationmodule,butfromthecoordinated
operationofmultiplecapabilitiesdistributedacrosstheagentpipeline.Giventhediversityofuserdata,tasksettings,
andpreferencetypes,user-specificsignalsmustberepresented,retained,reasonedover,andultimatelyrealizedin
externalactionsandoutcomes.Wethereforeadoptacapability-orientedtaxonomythatorganizespersonalization
intofourinterdependentcomponents.Thesecomponentsarenotisolatedmodules,butcomplementaryfunctional
stagesthattogethersupportend-to-endpersonalizationinagentsystems.
(1) ProfileModelingstructuresuser-specificinformationintointernalrepresentations,definingbothusercharac-
teristicsandtheagent’srole.
(2) Memorymaintainsandretrievesuser-relevantinformationacrossinteractions,supportingtemporalcontinuity
andconsistentpreferencegrounding.
(3) Planning integrates user-specific information into reasoning processes, shaping decision paths, strategy
selection,andprioritizationundercontextualconstraints.
(4) ActionExecutionoperationalizespersonalizeddecisionsthroughtoolinvocationandenvironmentinteraction,
enablingthefinalpersonalizedoutcome.
To further clarify the distinctions among these four capabilities, Table 1 compares them along several shared
dimensions,includingtheirtypicalinputs,temporalscope,andprimaryobjectives,providingaunifiedanalyticallens
fortheremainderofthesurvey.Inthefollowingsections,werevieweachcapabilityindetail,whilenotingthatmost
existingmethodsfocusononlyoneorasubsetofthesecapabilitiesratherthanthefullpipeline.
Table1. ComparisonofthefourcorecapabilitiesinpersonalizedLLM-poweredagents.
Capability TypicalInputs TemporalScope PrimaryObjective
ProfileModeling User attributes, behavioral his- Lifelong Establishuserunderstandingandsup-
tory,anduserinstructions portagent-useralignment
Memory Interactionhistory,userevents, Turntolifelong Maintaintemporalcontinuityandcon-
contextualrecords sistentpersonalization
Planning Profileinformation,memory,task Turntotask Enablepersonalizedreasoningandde-
context,in-taskfeedback cisionmaking
ActionExecution Plans,toolstates,executionfeed- Steptotask Realize personalized actions and out-
back comes
3 ProfileModeling
Ingeneral-purposeagentsystems,profilesareprimarilyusedtodefinetheagentitself,includingitsintrinsicattributes,
behavioraltendencies,andoperationalboundaries[110].Suchidentitiesareoftenstaticorexternallyspecifiedthrough
fixedroleinstructions,domainexpertise,orpre-definedfunctionalassignments[224,251].InPLAs,however,profile
modelingbecomesexplicitlyuser-centered,modelingtheuseranddynamicallyshapinghowtheagentpositionsitself
whencarryingouttasksforthatuser.Inthissense,profilemodelingservesasthefoundationallayerofPLAs,linking
userunderstandingwithagentroleconfiguration.Accordingly,wediscussprofilemodelingfromtwocomplementary
perspectives:userprofilemodelingandagentroledefinition.
3.1 UserProfileModeling
Userprofilemodelingextractsandorganizesuser-specificsignalsintorepresentationsthatcanguidehowanagent
shouldrespondoract[221].Inthissurvey,wedistinguishtwomajorparadigmsaccordingtohowuserpreferences
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 7
AlignXpert[87],FSPO[175],[201],RLPF[223],RLPA[263],
UserProfile
|     | Modeling | CURIO[197],PFM[10],PReF[168],LoRe[12], |     | Janus[82], |
| --- | -------- | -------------------------------------- | --- | ---------- |
PLUS[125],
ProfileModeling
§3
|     | AgentRole  | ASFM[39],LD-Agent[86],RecAgent[205],PAA[85],Per- |     |     |
| --- | ---------- | ------------------------------------------------ | --- | --- |
|     | Definition | sonaAgent[254],PersonaX[172],RPP[115],           |     |     |
LD-Agent[86],MemoryBank[269],SeCom[136],RMM
[187],Nemori[126],CAIM[219],PREMem[77],Mem-
|     | Memory  | oBase[119],MemInsight[154],MIRIX[209], |                            | Mem-𝛼 |
| --- | ------- | -------------------------------------- | -------------------------- | ----- |
|     | Schemes | [213], MemWeaver[246],                 | M3-Agent[109],RAPTOR[160], |       |
MemTree[152],SGMem[230],LicoMemory[57],Mem0[22],
| Memory |     | Memory-R1[241],A-Mem[237],TRAIL[264] |     |     |
| ------ | --- | ------------------------------------ | --- | --- |
§4
tnegAderewop-MLLdezilanosreP RAPTOR[160],[247],HippoRAG[65],AriGraph[5],Zep
|     | Personalized | [150],MemGAS[233],AssoMem[252],PBR[257],Person- |     |     |
| --- | ------------ | ----------------------------------------------- | --- | --- |
|     | Retrieval    | aRAG[248],UniMS-RAG[200],Persona-DB[180],OCG-   |     |     |
Agent[171],MemInsight[154]
ALIGNXPLORE[88],ReaRec[189],PbP[234],PRIME[256],
|     | One-shot | PSG-Agent[226],TravelPlanner++[176],PTS[165],PREFINE |     |     |
| --- | -------- | ---------------------------------------------------- | --- | --- |
Planning
[195],IoTGPT[245]
Planning
| §5  | Feedback- |     |     |     |
| --- | --------- | --- | --- | --- |
SAGE-Agent[183],ECLAIR[124],Ask-before-Plan[255],
|     | Driven   | AIPOM[74],Dango[18],PlanFitting[173],VAIAGE[101], |     |     |
| --- | -------- | ------------------------------------------------- | --- | --- |
|     | Planning | Collab-Rec[9],SceneWeaver[244]                    |     |     |
PEToolLLaMA[235],PUMA[14],ToolSpectrum[20],Color-
Pre-Action
| ActionExecution |     | Agent[90],AWARE-US[80],[55],ValuePilot[111] |     |     |
| --------------- | --- | ------------------------------------------- | --- | --- |
§6
PEAR[96],MIR[232],WARPP[117],ETAPP[50]
Post-Action
|     | Goalsand | Effectiveness,Adaptivity,Generalization,Robustness,Risk |     |     |
| --- | -------- | ------------------------------------------------------- | --- | --- |
Metrics
IndieValueCatalog[63],ALOE[225],
Evaluation
| §7  |     | Interactive | AgentRecBench[164],LongMemEval   |     |
| --- | --- | ----------- | -------------------------------- | --- |
|     |     | Alignment   | [222],PTBench[55],ETAPP[50],Per- |     |
sonaMem[61],PENGUIN[229]...
Benchmarks
LongLaMP[79],PGraphRAG[7],Per-
|     |     | User- | sonaConvBench[89],LaMP-QA[157], |     |
| --- | --- | ----- | ------------------------------- | --- |
PRISM[78],PEToolBench[235],Trip-
Substitution
Tailor[203],PersONAL[270]...
| Fig.4. | TaxonomyofpersonalizedLLM-poweredagents. |     |     |     |
| ------ | ---------------------------------------- | --- | --- | --- |
arerepresented:persona-based approaches,whichmodeltheuserthroughrelativelyholistictraitsandpreference
descriptions,andresponse-based approaches,whichmodeltheuserthroughpreferencesovercandidateresponsesor
modelbehaviors.
Persona-basedmethodsmodeltheuserthroughrelativelystabletraits,characteristics,
Persona-basedModeling.
andlong-termpreferencedescriptionsthatremaininformativeacrosscontexts.Suchprofilesmaybeconstructed
fromexplicitself-descriptions,behavioralhistory,orhistoricalinteractions,andareoftenrepresentedasstructured
attributevectorsorfree-formnatural-languagepersonasummaries.Indownstreamuse,persona-basedprofilesare
oftenincorporatedaspromptsorconstraintstoguidepersonalizedgenerationanddecisionmaking.Forinstance,
AlignXpert[87]constructsahigh-dimensionalpreferencespacegroundedinpsychologicalandalignment-related
dimensions,whileFSPO[175]producesmorefine-grainedpersonadescriptionsthroughauser-descriptionchain-
of-thought mechanism. Beyond such one-shot profiling, several methods iteratively refine user representations
through interaction: RLPA [263] and Wang and Yang [201] update user representations across rounds, RGMem
[191]hierarchicallyaggregatesuserinsightsfromepisodicmemory.Relatedly,RLPF[223]optimizesconcise,human-
readableusersummariesusingafeedbacklooptiedtodownstreamperformance,andCURIO[197]introducesan
intrinsicmotivationobjectivethatencouragesactiveinferenceoflatentusertypesduringmulti-turninteraction.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

8 • Y.Xuetal.
Response-based Modeling. Response-based modeling represents user preferences through how users evaluate
candidateoutputs,therebycapturingmorefine-grainedandcontext-sensitivenotionsofwhatconstitutesapreferred
response.Comparedwithpersona-basedapproaches,whichemphasizeholisticuserdescriptions,response-based
approachesfocusmoredirectlyonusersatisfactionwithmodelbehavior.Indownstreamuse,theserepresentations
are naturally suited to feedback-driven correction and refinement of personalized outputs. A common strategy
istofactorizeindividualpreferenceintoasharedrewardfeaturebasiswithuser-specificweights,enablingrapid
adaptationundersparseuserdata.RFM[10],PReF[168],andLoRe[12]followthisparadigmbyinferringuser-specific
coefficientsfromlimitedfeedback.Complementarily,somemethodsrepresentpreferencesinnaturallanguageto
improveinterpretabilityandcontrollability.Janus[82]organizespreferencedimensionshierarchicallyfromcoarse
categoriestofine-grainedvaluedescriptions,whilePLUS[125]learnstext-basedpreferencesummariesthatcondition
downstreamrewardmodelingforpersonalizedscoringandgeneration.
3.2 AgentRoleDefinition
Whileuserprofilemodelingfocusesonrepresentingtheuser,agentroledefinitiondetermineshowtheagentshould
positionitselfwithrespecttothatuser.Wedistinguishbetweenuser-substitutingagentdefinition,wheretheagentis
configuredtoactonbehalfoftheuser,anduser-adaptiveagentdefinition,wheretheagentdynamicallyadjustsitsrole
tobetterservearealuserduringinteraction.
User-substitutingAgentDefinition. User-substitutingroledefinitioniscommonindelegation-orientedandsimulation
scenarios,whereagentsareexpectedeithertoperformtasksfromtheuser’sperspectiveortogenerateuser-like
behaviorsanddialoguedata.Inthesecases,theagentisconfiguredtoactonbehalfoftheuserbyinstantiatingthe
user’sprofileasitsroleconfiguration.Theresultingrolepriorthenguidesplanningandexecutiontowardpersonalized
objectives[128].Thisformofroledefinitiondoesnotprimarilyrelyononlineadaptationtoarealuser,butremains
importantforuserproxyexecution,realistichuman-agentsimulation,andscalablegenerationofdiversesynthetic
users[39,85,205].
User-adaptiveAgentDefinition. Ininteractivepersonalizedsystems,PLAsadaptthemselvestobettersupportthe
userduringcollaboration.Here,theagentrolebecomesconditionalontheuserprofile,allowingtheagenttoadjustits
persona,tone,levelofautonomy,orinteractionstrategyaccordingtotheuser’sprofile.Thisformsatwo-wayadaptive
processinwhichuserunderstandinginformsroleconfiguration,andtheadaptedroleinturnaffectssubsequent
interaction. Representative methods realize user-adaptive role definition through either joint persona modeling
orprofile-conditionedpromptadaptation.LD-Agent[86]adoptsabidirectionaluser-agentmodelingframework
[238] with a tunable persona extractor and a long-term persona bank for both users and agents. PersonaAgent
[254],PersonaX[172],andRPP[115]insteadadapttheagentrolethroughuser-conditionedpromptsorprofiles:
PersonaAgentoptimizesuser-specificsystempromptsviatextuallossfeedback,PersonaXcombinesofflinemulti-
personaprofilingwithonlineprofileretrieval,andRPPgeneratespersonalizeddiscretepromptsfromhistoricaluser
informationandtaskguidance.
3.3 Discussion
RoleandChallenges. Profilemodelingprovidesthefoundationallayerofpersonalizationbydeterminingboth
howtheuserisrepresentedandhowtheagentisconfiguredinresponsetothatrepresentation.Theybridgeraw
user-relatedevidencewithdownstreampersonalizedmemory,planning,andaction.Atthesametime,theyface
severaltightlycoupledchallenges.Userprofilingmustfirstcopewithsparse,noisy,andinconsistentpreference
signals.Beyondsignalquality,aseparatechallengeisdeterminingwhichuser-relatedfeaturesaregenuinelyrelevant
fordownstreampersonalization.Inparallel,agentroledefinitionmustbalanceadaptabilitywithstabilityacrosstasks,
avoidingbothrigidroleassignmentsandundesirableroledrift.Finally,abroaderchallengeliesintherequirementof
effectivecouplingandbidirectionalalignmentbetweenuserprofilingandagentroleadaptation.
FutureDirections. Existinguserprofilingmethodsoftenproducerepresentationsthatareeitheroverlystaticor
narrowlytask-specific,whileagentrolesoftenlackcontrollabilityorprincipledadaptationdynamics.Moreover,
userprofilingandagentroledefinitionaretypicallydevelopedinisolation,withlimitedmechanismsformutual
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 9
adjustment.Promisingdirectionsthereforeincludelightweightandinterpretableprofilingmethodsthatremainrobust
undersparseornoisysignals,aswellasunifiedframeworksthatjointlymodelevolvinguserprofilesandstableyet
adaptiveagentroles.
4 Memory
Whileprofilemodelingcapturesrelativelystableandhigh-levelusercharacteristics,personalizedagentsalsorequire
mechanismsforretaininguser-relatedinformationacrossinteractions.Memoryprovidesthiscapabilitybyenabling
thesystemtostore,recall,andleveragepastexperiencetoimprovefuturebehavior[218].Memoryiscommonly
dividedintopersonalmemory,whichstoresuserinputsandinteractionhistories,andsystemmemory,whichrecords
intermediatereasoningstatesortask-executionartifacts[227].Thissurveyfocusesonpersonalmemory,asit
directlyshapeshowagentsadapttoindividualusers.
Personalmemorycanbeimplementedeitherasinternalmemory,whichembedsuser-relatedinformationwithinthe
LLM,orasexternalmemory,whichstoressuchinformationinanauxiliarysystem.Internalmemorymayberealized
through model parameters, key–value caches, or hidden states [129, 144, 207, 211, 231, 259]. Although compact
andparameter-efficient[212],internalmemoryislimitedbyconstrainedcapacity,difficultiesinupdatingstored
information,andfrequentrelianceonretraining,makingitlesssuitablefordynamicandlong-horizonpersonalization.
Bycontrast,externalmemoryismoreflexibleandtypicallyoperatesthroughretrieval-augmentedgeneration(RAG;
83)toincorporatestoreduserinformationintothecurrentcontext.
Externalpersonalmemorycanfurtherbeviewedatdifferenttemporalscales,includingshort-termmemory,which
retainsrecentconversationalcontext,andlong-termmemory,whichaccumulatesenduringuserinformationacross
sessions.Short-termmemorysupportsimmediateresponsesbutisconstrainedbycontextwindows,whereaslong-
termmemoryenablestheaccumulationoflong-tailpersonalinformationandcontinualadaptation[64],yetismore
vulnerabletoinformationoverloadandstalecontent.Asaresult,manypersonalizedagentsadopthybriddesigns
thatcombineboth.Intheremainderofthissection,however,wefocusonlong-termexternalpersonalmemory,
wherethestructureddesignofpersonalizedmemoryhasbeenmostextensivelystudied.Wediscussitfromtwo
perspectives:personalmemoryschemes,whichdeterminehowuser-relatedinformationisstoredandupdated,and
personalizedretrieval,whichdetermineshowstoredinformationisaccessedtosupportpersonalizedbehavior.
4.1 MemorySchemes
Memoryschemesdeterminehowuser-relatedinformationisorganized,stored,andupdatedovertime.Inlong-term
externalpersonalmemorysystems,thismainlyinvolvesthedesignofmemorystructureandupdatemechanism.
4.1.1 MemoryStructure. Memorystructuredetermineswhatinformationisstoredandhowitisrepresented,thereby
shapingthescalabilityandusefulnessofpersonalmemory.Earlyagentsystemsoftenstoredfulldialoguehistoriesor
executiontrajectoriesdirectly[104],butsuchrawstorageintroducedredundancyandmadeitdifficulttosurface
user-relevantinformation.Recentmethodsthereforetransforminteractionhistoriesintomorecompactandtask-
adaptiverepresentations[103,269].Basedonrepresentationformat,thesestructurescanbebroadlygroupedinto
textualmemoryandstructuredmemory.
TextualMemory. Textualmemorystoresuser-relatedinformationinnaturallanguageform,typicallybysummariz-
ingmulti-turninteractionsintoconciseandinterpretableunits.Becausesuchrepresentationspreserverichsemantics
andalignnaturallywiththeinput–outputformatofLLMs,textualmemoryhasbecomeacommonchoiceforperson-
alizedagentsacrossdiversetasks[260].Itsdesignmainlyinvolvestwokeychallenges:determiningthegranularity
ofmemoryunitsthroughappropriatesegmentation,andpreservinguser-relevantinformationaccuratelywithin
thoseunits.Earlyapproachesoftenreliedonrigidturn-levelorsession-levelsegmentation,whichcouldfragment
semanticallycoherentinteractionsandhinderretrieval.Recentworkthereforeexploresmoreflexible,topic-consistent
segmentationstrategies.Forexample,SeCom[136]andRMM[187]partitionconversationsintosemanticallycoherent
segments,whileNemori[126]furtherimprovessegmentationbydetectingepisodeboundariesandpreservingthe
integrityofuserintent.Onceappropriatememoryunitsareformed,asecondchallengeistopreserveuser-relevant
information faithfully and compactly. Many systems augment textual memory with auxiliary attributes such as
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

10 • Y.Xuetal.
timestamps,topiclabels,anduserpersonality[103,119,237].Forinstance,CAIM[219]augmentsmemoryentries
withtags,inductivethoughts,andtimestamps,whileMemInsight[154]extractsstructuredsemanticattributesfrom
dialogueforrichermemoryaugmentation.Morerecently,someworksdrawinspirationfromhumanmemorysystems
byintroducingmulti-levelorganizationsthatdistinguishsemanticandepisodicmemory[107,109,140].Forexample,
MIRIX[209]adoptsahierarchicallyorganizedmulti-componentmemoryarchitecture,andMem-𝛼 [213]combines
core,semantic,andepisodicmemorywithreinforcementlearningformemorymanagement.Overall,theseefforts
movetextualmemorytowardmorecoherentsegmentation,morefaithfulpreservationofuser-relevantcontent,and
bettersupportforlong-termpersonalization.
StructuredMemory. Structuredmemoryrepresentsinteractionhistoriesinpredefinedformatswithexplicitorga-
nizationalrelationships,makingstoredinformationeasiertomanipulatecomputationally.Comparedwithtextual
summaries,itintroducesstrongerinductivebiasesforscalableretrieval,multi-granularityreasoning,andfine-grained
personalization.Currentapproachescanbebroadlygroupedintovector-basedmemory,hierarchicaltreestructures,
andgraph-basedmemoryarchitectures.
Vector-basedmemoryencodeseachmemoryunitasanembeddingstoredinavectordatabase,enablingefficient
similaritysearchandfastretrievalofuser-relevantinformation.Owingtoitsefficiencyandflexibility,thisdesign
hasbecomeacommonpracticeinmemorymodules[22,133,230].However,vectormemoryaloneprovideslimited
interpretabilityanddoesnotexplicitlycapturerelationsamongmemoryitems,motivatingmorestructuredalternatives
orhybridsystemsthatcombinevectorswithexplicitorganizationalformats.Hierarchicaltreestructuresorganize
memory at multiple abstraction levels, where parent–child relations encode increasingly coarse summaries. For
example,RAPTOR[160]andMemTree[152]recursivelyclusterandsummarizetextintotrees,supportingretrievalat
bothfine-andcoarse-grainedlevels.Graph-basedarchitecturescapturericherrelationshipsbylinkingmemory
unitsthroughtypededgesthatencodetemporal,semantic,orrelationaldependencies[22,65,97].Somemethods
emphasizebehavioralcoherence.Forexample,MemWeaver[246]constructsanevent-levelbehaviorgraphinwhich
interaction events are connected by temporal and semantic edges, together with a context-aware random walk
mechanism.Otherdesignsinsteadintegratemulti-dimensionalsubgraphstomodelmorenuancedrelationsamong
memoryunits.AriGraph[5]combinessemanticknowledgewithepisodicobservationnodestosupportbothlong-
termaccumulationandtemporallygroundedrecall,whileZep[150]organizesmemoryintoatemporallyaware
multi-tier knowledge graph spanning episodic, semantic, and conceptual levels. While expressive, graph-based
memoryoftendependsoncostlyLLM-basedextractionandmaylosefine-grainedcontextduringgraphconstruction.
Lightweightvariantsthereforesimplifygraphdesignwhilepreservingcontextualinformation.SGMem[230]uses
sentence-levelgraphorganization,whereasLiCoMemory[57]adoptsalightweighthierarchicalindexinggraphwith
fullcontentstoredexternally.Overall,structuredmemoryaimstoprovidericherorganizationbyexplicitlymodeling
howuser-relatedinformationisorganized,connected,andabstractedacrossinteractions.
4.1.2 Update mechanism. The update mechanism determines how memory evolves as new interactions arrive,
ensuringthatstoredinformationremainsusefulovertime.Whenanewmemoryunitisobserved,thesystemmust
decidewhethertoadditasanewentry,mergeitwithexistingmemory,reviseoutdatedcontent,ordiscardirrelevant
information[34].Inexternalpersonalmemorysystems,updatesdifferbetweentextualmemory,wheresummary-level
contentisrewrittenorreorganized,andstructuredmemory,wherenodes,edges,andtheirrelationsaremodified.We
discussthesetwocasesseparately.
Textual memory stores interaction histories as natural-language segments or summaries. Updating therefore
concernshowtheseunitsaremerged,rewritten,orreorganizedasnewdialoguearrives.Existingapproachescanbe
broadlygroupedintosimilarity-drivenupdatesandinference-guidedupdates.
Similarity-drivenupdates. Thesemethodsupdatememorybycomparingnewcontentwithexistingentriesand
applyingmerge,revision,orreplacementoperationsbasedonsemanticsimilarityandauxiliarymetadata.Earlier
approaches, such as RMM [187] and CAIM [219], perform summary-level merging and refinement. Mem0 [22]
makesthisprocessmoreexplicitthroughADD,UPDATE,DELETE,andNOOPoperationsovercandidatememories,while
Memory-R1[241]furtherlearnstheupdatepolicywithreinforcementlearningacrossmulti-sessioninteractions.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 11
Inference-guidedupdates. Othersystemstreatmemoryupdatingasareasoningordecision-makingprocess,allowing
theagenttoincorporateimplicitpreferenceshiftsorcontextualdynamicsnotcapturedbysimilarityalone.Nemori
[126]exemplifiesthisthroughitsPredict–Calibratemechanism,achievingproactivelyevolvingmemorybasedongaps
betweenpredictedandactualuserresponses.PREMem[77]similarlyperformspre-storagereasoningacrosssessions
to analyze thematic evolution before inserting new content, enabling more consistent long-term topic tracking.
Thesemethodsprovidemoreadaptiveandself-correctingmemorydynamics,capturingbothshort-termchangesand
long-termshiftsinuserpreferences.
Structuredmemoryorganizesinformationintointerconnectedarchitectureswhereinsertinganewunitoften
requiresreorganizingitsrelatedcounterparts.Updatemechanismscanlikewisebegroupedintosimilarity-drivenand
reasoning-oragentic-drivenstrategies.
Similarity-drivenupdates. Thesemethodsupdatestructuredmemorybymatchingnewinformationtoexistingunits
throughsemanticsimilarityandthenapplyinglocalstructuralmodificationstopreservecoherence.Inhierarchical
treestructures,MemTree[152]traversesthetreebysemanticsimilarity,insertsnewnodesthroughsiblingattachment
orleafexpansion,andincrementallyupdatesancestorsummariestomaintainhierarchicalconsistency.Ingraph-based
memory,updatesaremorecomplexbecauseeachnodemayconnecttomultipleothers[57].Mem0𝑔[22]matchesnew
triplestoexistingnodes,addsmetadata-richedges,andusesanLLM-basedconflictresolvertodeactivateoutdated
relations.Similarly,Zep[150]updatesepisodicfactsthroughtimestamp-awarealignmentwhileadjustinginconsistent
edgesandhigher-levelclusters,andMemGAS[233]selectivelyreinforcescontextuallyrelevantcross-granularity
associationstomaintainlong-horizonpersonalization.
Reasoning-guidedupdates. Anemerginglineofworkusesexplicitreasoningordecision-makingtoguidememory
updates,movingbeyondsimilaritymatchingtowardmoreadaptiveupdatedynamics.A-mem[237]exemplifiesthis
directionbytreatingeachnewmemoryasastructurednotethattriggerssemanticlinkingandretroactiverefinement
ofhistoricalnotes,enablingaself-evolvingmemorygraph.Althoughnotdesignedspecificallyforpersonalization,
systemssuchasTRAIL[264]andAriGraph[5]furthersuggestthatreasoning-guidedgraphevolutioncansupport
morecoherentmemoryupdates.
4.2 PersonalizedRetrieval
Memoryretrievaldetermineswhichstoredinformationbecomesavailabletoanagentatinferencetimeandtherefore
directlyinfluencesthequalityandconsistencyofpersonalizedbehaviors.UnlikeconventionalRAGsystems,retrieval
forpersonalizedLLM-poweredagentsmustsimultaneouslysatisfythreerequirements:(1)contentrelevancetothe
currentquery,(2)structuralconsistencywiththeunderlyingmemoryorganization,and(3)personalalignmentwith
theuser’spreferences.Existingretrievalmethodsaddressthesechallengesthroughthreedominantmechanisms:
content-basedretrieval,structure-awareretrieval,andpolicy-guidedretrieval.
Content-basedretrieval. Content-basedretrievalselectsrelevantmemoryprimarilythroughsemanticorlexical
similaritybetweenthecurrentqueryandstoredinformation,typicallyusingdenseorsparseretrievers[59,68,153].
Retrievedcontentisthenincorporatedintotheagent’sprompttoimprovecontextualgrounding[77,209,237].This
mechanismcanalsooperateatmultiplelevelsofgranularity.Forexample,RAPTOR[160]andMemTree[152]retrieve
memoryacrossdifferentabstractionlevelsbasedprimarilyonquerysimilarity,evenwhenthestoredmemoryis
hierarchicallyorganized.Somemethodsfurtherrefineretrievalaftertheinitialsearch.Forinstance,Yuanetal.[247]
usesself-reflectiontoassesswhethertheretrievedcontentissufficientforresponsegenerationandrevisethequery
whennecessary.Whileeffectiveforsemanticmatching,content-basedretrievaldoesnotexplicitlymodelstructural
dependenciesamongmemoryitemsandmaythereforeoverlooklong-rangecontextualrelations.
Structure-awareretrieval. Structure-awareretrievalaccessesmemorybyexplicitlyexploitinggraph,hierarchy,or
episodicrelations,ratherthanrelyingoncontentsimilarityalone.Thesemethodsoftenoperatehierarchically,where
theretrievalofentities,topics,orrelationsguidessubsequentaccesstodetailedmemoryunits[47,65],sometimes
withgraph-basedtechniquessuchasPersonalizedPageRank(PPR;8).Forexample,AriGraph[5]retrievesrelational
tripletsbeforeretrievingrelevantepisodicmemories,whileZep[150]combinessemanticsearchwithgraph-structured
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

12 • Y.Xuetal.
signalssuchasepisodefrequencyandnodedistance.MoreadaptivevariantsincludeMemGAS[233],whichcombines
entropy-basedroutingwithPPRoveranassociationgraph,andAssoMem[252],whichperformsmulti-signalranking
overcluenodesandlinkedutterances.Bymodelingdependenciesamongmemoryunitsexplicitly,structure-aware
retrievalbettercaptureslong-rangeandimplicituserpreferences.
Policy-guidedretrieval. Policy-guidedretrievalreferstoretrievalstrategiesinwhichmemoryaccessiscontrolledby
user-ortask-conditioneddecisionpoliciesratherthanbystaticsimilaritymatchingalone.Suchapolicydetermines
howretrievalshouldproceed,includinghowqueriesareformed,whichretrievaltoolsareinvoked,andwhether
additional information should be acquired. One line of work focuses on pre-retrieval query transformation,
wherepersonalizedretrievalintentisconstructedbeforesearch.Forexample,PBR[257]generatesuser-stylepseudo
feedbackandcorpus-anchoredexpansionstoformapersonalizedqueryrepresentation,whilePersonaRAG[248]
adaptsdocumentselectionandrankingusingreal-timebehavioralsignals.Asecondlineofworkadoptspolicy-driven
strategyselection,learningtoinvokeorcombineheterogeneousretrievaltoolsaccordingtotaskneeds.UniMS-RAG
[200]formulatesretrievalasapolicy-learningproblemoverkeywordsearch,denseretrieval,andknowledge-graph
lookup,whilePersona-DB[180]employsapersona-awarepolicytocombineretrievalsfromtargetandcollaborator
usersforimprovedpersonalizationundersparsedata.Athirddirectionincorporatesschema-guidedinformation
completion,framingretrievalasastructuredinferenceprocess.OCG-Agent[171]decomposesnarrativequeriesinto
schemafields,retrievesrelevantinformationthroughmultipleroutes,anditerativelysupplementsmissingattributes
untiltheschemaiscompleted.Overall,policy-guidedretrievalshiftsretrievalfrompassivematchingtowardactive
decisionmaking,enablingmoreflexibleandpersonalizedinformationacquisition.
4.3 Discussion
RoleandChallenges. Personalmemorybridgesshort-terminteractioncontextwithlong-termpreferencemodeling,
fulfillingthreecloselyrelatedroles.Itprovidespersonalizedcontextualgroundingbypreservingfine-graineduser
detailsthatcannotbefullyencodedinstaticprofiles,supportspreferenceevolutionbyallowingtheagenttotrackhow
userpreferenceschangeacrosssessions,andenablespreference-conditionedgenerationbysupplyinguser-relevant
signalsatinferencetime.Atthesametime,theserolesmakepersonalmemorydifficulttodesigneffectively.User
preferencesevolveatdifferentrates,requiringmemorysystemstobalancerapidadaptationwiththepreservation
oflong-termtraits.Memorystoresmayalsoaccumulateredundancyorhallucinations,especiallywhenupdates
relyonLLM-basedsummarizationorrelationextraction,leadingtodegradedpersonalizationoverlonghorizons.
Moreover, retrieving content that is not only semantically relevant but also truly aligned with user preferences
remainsapersistentchallenge.Finally,personalmemoryraisesprivacyandtransparencyconcerns,highlightingthe
needforuser-controllableandprivacy-preservingmemorymechanisms.
Future Directions. These limitations point to several promising directions across the memory pipeline. One is
hybridmemoryarchitecturesthatcombinethesemanticrichnessoftextualrepresentationswiththeorganizational
clarityofstructuredformats.Anotherismoreprincipledanduser-controllableupdatemechanismsthatimprove
reliability, transparency, and long-term consistency. A third is retrieval strategies that better integrate personal
alignmentwithsemanticrelevance,sothatretrievedinformationisnotonlyrelatedtothequerybutalsotrulyuseful
forpersonalization.
5 Planning
InPLAs,planningisthestageatwhichuser-specificinformationistranslatedintoactionabledecisions.Whileprofile
modelingcaptureswhatisknownabouttheuserandmemorypreservesuser-relatedinformationovertime,planning
determineshowthesesignalsshapesubgoaldecomposition,strategyselection,andtrade-offresolutionduringtask
execution[110,181].Thus,itgoesbeyondgenerictask completionandinsteadseeksto optimizeuserutilityby
aligningdecisionswithindividualpreferences,constraints,andlatentintents[37,48,261].Weorganizeexisting
methodsintotwobroadparadigmsaccordingtohowusersignalsentertheplanningprocess:One-shotPlanning,in
whichpersonalizationisincorporatedasapriorduringplangeneration,andFeedback-drivenPlanning,inwhich
personalizationisprogressivelyrefinedthroughinteraction[183,255].
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 13
5.1 One-ShotPlanning
One-shotpersonalizedplanninggeneratesacompleteplanwithinasingleinferencepass,wheretheplanisrepresented
asastructureddecompositionofsubgoalsanddecisionsconditionedonuser-specificconstraintsandlatentintent.
Weanalyzethisparadigmalongtwocomplementaryaxes:usersignalgrounding,whichconcernshowusersignals
areincorporatedintotheplanningprocess,andinternalrefinement,whichconcernshowaninitialplanisinternally
improvedwithinthesameinferencepass.
5.1.1 UserSignalGrounding. One-shotplanningcangrounduser-specificinformationintwomainways.Onedirectly
conditionsplanningonexistinguserrepresentations,suchasexplicitprofiles,retrievedmemory,orcompressed
interactionhistory.Theotherinfersplanning-readyconstraintsorobjectivesfromheterogeneoususersignalsbefore
plangeneration.
ProfileandMemoryConditioning. Thesemethodsconditionone-shotplanningonexistinguserrepresentations,
suchasexplicitprofiles,retrievedmemory,orcompressedinteractionhistory,therebyhelpingmaintainconsistency
withbothlong-termpreferencesandrecentcontext[187,219].PRIME[256]integratesadual-memoryarchitecture
withaPersonalizedThoughtProcessthatexplicitlytraceshowpastexperiencesandstablebeliefsinfluencecurrent
decisions.Beforeplangeneration,PRIMEsynthesizesapersonalizedthoughttraceviaself-distillation,effectively
groundingplanningintheuser-specificcognitivecontext.PersonaAgent[254]adoptsaretrieval-augmentedpersona
mechanism,dynamicallyconstructingsystempromptsfromaunifiedmemorybanktomaintaincross-sessionplanning
consistency.Relatedworkinrecommendationanddialoguesystemssimilarlyshowsthatstructuredusermemory
retrievalsignificantlyimprovesalignmentandcoherenceinone-shotdecision-making[17,54].
PreferenceInduction. Complementarytodirectconditioning,thislineofworkconstructsaplanning-readyuser
statebyinferringlatentintentandtranslatingheterogeneoususersignalsintoexplicitconstraintsorsoftobjectives
thatguideplangeneration[48].Forinstance,ALIGNXPLORE[88]utilizesaUser-descriptionChain-of-Thought
frameworktosynthesizeacompact,semanticallygroundedpreferencedescriptionfromsparseinteractiontraces.
Insteadofretrievingrawlogs,themodelperformsextendedinductivereasoningtoformglobalpreferenceconstraints
thatconditiondownstreamplanning.Similarly,insequentialrecommendation,ReaRec[189]proposesaThink-Before-
Recommendparadigm,usingreasoningpositionembeddingstoinfertheuser’slatentintenttrajectorypriortoplan
generation.Inembodiedanddecision-makingcontexts,PbP[234]demonstratesthattreatinglearneduserpreferences
asintermediateabstractionssubstantiallyimprovesfew-shotpersonalizedplanningperformance.
5.1.2 InternalRefinement. Internalrefinementimprovesone-shotplanningbyfirstgeneratinganinitialplanand
theninternallycritiquingandrevisingitagainstauser-conditionedobjective.Generalself-refinementframeworks,
suchasReflexionandstructuredcritique-and-revisemethods,providereusablemechanismsforreflectivefeedback
andplanediting[44,174],whilerecenttest-time-computereasoningmodelsmakedeeperwithin-passself-correction
increasinglypractical[46,121].Representativesystemsinstantiatethisparadigminseveraldomains.Inpersonalized
travelplanning,TravelPlanner++[176]andPTS[165]iterativelyrefineintermediateitinerariesunderimplicitlong-
horizonuserpreferences.PREFINE[195]constructsapseudo-usercriticanduser-specificrubricsfrominteraction
historytocritiqueandrevisecandidateplans.Inembodiedcommandexecution,IoTGPT[245]performsself-correction
bytestingintermediatecommandsequencesinasimulatedenvironmentbeforedeployment.
5.2 Feedback-DrivenPlanning
Feedback-drivenplanningtreatsaninitialplanasaprovisionalhypothesistoberefinedthroughinteraction.Itis
motivatedbythefactthatuserintentisoftenunderspecified,evolving,oronlypartiallyobservable[108,255].Rather
thancommittingtoafixedplaninasinglepass,thesesystemsiterativelyupdateplanstoconvergetowardamore
personalizedsolution[183,202].Weorganizethisparadigmaccordingtothesourceoffeedbackandhowitupdates
theplan,includingclarificationseeking,userrevision,andnon-userfeedback.
Clarification Seeking. A central challenge in feedback-driven personalized planning lies in deciding when to
askforadditionalinformation:excessiveclarificationincreasesuserburden,whileprematurecommitmentrisks
misinterpretinguser-specificconstraintsorlatentintent.Priorstudiesindicatethatuserrequestsinplanningtasksare
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

14 • Y.Xuetal.
frequentlyunderspecifiedorambiguous[108],motivatingapproachesthattreatclarificationasdecision-makingunder
uncertainty.Forinstance,SAGE-Agent[183]formulatesselectivequestioningasaPOMDPandissuesclarification
queriesonlywhentheexpectedvalueofinformationoutweighsinteractioncost.Similarly,ECLAIR[124]focuseson
detectingmissingargumentsorambiguousentitiesinuserinstructionsandtriggerstargetedfollow-upquestions
beforecommittingtoaplan.Additionally,Ask-before-Planstyleframeworks[255]explicitlydecoupleclarification
fromplansynthesis,showingthatresolvingkeyuncertaintiesupfrontimprovesrobustnessanddownstreamplan
quality.
UserRevision. Usereditsprovideahigh-fidelitypersonalizationsignalthatcanupdateuser-conditionedobjectives,
constraints, and preferences for subsequent planning and generation. Gao et al. [37] shows that learning latent
preferences from historical edits can reduce future edit effort and improve user-specific alignment in subjective
settings.Buildingonthismixed-initiativeview,AIPOM[74]representsplansaseditablestructures,enablingusers
toreviseintermediateplanswhiletheagentupdatesconstraintsandprioritiesaccordingly.Similarrevisionloops
appearindomainsystemssuchasDango[18],whichsupportsiterativecorrectionofagent-produceddata-processing
workflows,andPlanFitting[173],whichrefinespersonalizedexerciseplansthroughconversationalrevisions.Similar
revisionpatternsarealsoincreasinglyvisibleindeployedcodingassistants[6,41].
Non-userFeedback. Beyonddirectuserinput,planscanalsoberefinedthroughnon-usersignalsthatimprove
feasibilityandpreferencesatisfactionwithoutrepeatedlyincreasinginteractionburden.Onesourceisagent-mediated
feedback.Forexample,VAIAGE[101]employsspecializedagentstonegotiateroutefeasibilityandrecommendations
underuserpreferences,whileCollab-Rec[9]supportsmulti-stakeholderplanningthroughexplicituser-advocacy
mechanisms.Anothersourceisenvironment-mediatedfeedback,whereintermediateoutcomesaresimulatedand
usedtotriggerre-planning.Forinstance,SceneWeaver[244]followsaReason–Act–Reflectloopandrevisesplans
whenintermediaterenderingresultsrevealviolations.
5.3 Discussion
RoleandChallenges. PlanningservestwocomplementaryrolesinPLAs.First,itoperationalizespersonalizationby
translatinguserintentinferenceandpreferencemodelingintodownstreamdecisions,instantiatinguser-contingent
objectives,constraints,andtrade-offsthatgovernplangeneration[17].Second,especiallyinfeedback-drivenset-
tings[74],planningfunctionsasaclosed-loopoptimizationprocessthatalternatesbetweenelicitinginformative
feedbackandrevisingtheplan,enablingtheagenttoprogressivelyuncoveruserintentandmovetowardstronger
personalization.However,theserolesintroduceseveralchallengesatthesametime.Userintentandpreferences
areoftenonlypartiallyobservedandmayevolveovertime[108,183],makingitdifficulttodecidewhentoinfer,
elicit,andcommit.Moreover,personalizedutilityisinherentlymulti-objective[165],requiringarbitrationamong
competingconstraintsandidiosyncratictrade-offs.Ininteractivesettings,refinementmustalsoremaincontrollable
andconvergent,limitinguserburdenwhileavoidingunstablerevisions.Thesedifficultiesarereflectedinthetrade-off
betweenexistingparadigms:one-shotplanningofferslow-latencyandcoherentdecisionsbyinternalizingusersignals
aspriors,butcanbebrittleundersparseorshiftingsignals,whereasfeedback-drivenplanningimprovesalignment
throughiterativeelicitationandrevisionatthecostofadditionallatencyandusereffort[101].
FutureDirections. Promisingdirectionsincludeuncertainty-awareplanningworkflowsthatadaptivelyallocate
internalcomputationandrevisioneffortaccordingtoconfidenceininferredpreferencesandtaskstakes[121],thereby
combiningtheefficiencyofone-shotplanningwiththealignmentbenefitsoffeedback-drivenrefinement.Another
directionistolearnuser-conditionedplanningpatternsatbothinter-andintra-userlevels[146],capturingsystematic
differencesindecompositionstyleandtrade-offresolutionwhilemodelingtheirstabilityanddriftovertime.More
broadly,importantbutstillunder-exploreddirectionsincluderobustnesstovariationinuserspecification[183]and
privacy-preservingplanning[229]thatsupportslong-horizonuserconditioningwithoutexposingrawpersonaldata.
6 ActionExecution
ActionexecutionisthestageatwhichaPLArealizesdecisionsthroughconcreteoperationsinexternalenvironments
andreceivesfeedbackfromexecutionoutcomes[73,167].Unlikepurelytask-centricexecution,personalizedexecution
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 15
mustgroundactionsinuser-specificconstraintsandpreferences,whileremainingadaptivewhentoolsorenvironments
produceunexpectedoutcomes.Weorganizepersonalizedactionexecutionintotwostages:apre-actionstagethat
selectsandparameterizesactionsunderuser-conditionedconstraints,andapost-actionstagethatleveragesexecution
signalsforrecoveryandpreference-consistentoutcomerealization.
6.1 Pre-actionStage
Thepre-actionstagefocusesonuser-conditionedactiondecisionandgrounding.Ittranslatesaselectedintentor
planstepintoexecutabletoolcallsorenvironmentoperationsunderuser-specificconstraints.Wefurtherdecompose
thisstageintoactionpolicy,whichselectsamongfunctionallyvalidexecutionoptionsforagivenstep,andaction
grounding,whichinstantiatestheselectedactionwithuser-specificargumentsandrealizations.
6.1.1 Action Policy. At this level, personalization manifests as a bias over functionally valid execution choices,
spanningbothtoolutilizationandhigher-levelactionselection.PEToolLLaMA[235]formalizespersonalizedtool
learningfrominteractionhistoryandtrainsmodelstoimprovepreference-awaretoolselection.Inweb-agentsettings,
PUMA[14]adoptsasimilarpreference-awarelearningstrategy,whileToolSpectrum[20]furtherconditionstool
useonbothuserprofilesandenvironmentalcontext.Beyondtoolinvocation,ValuePilot[111]studiesaction-level
decisionmakingunderuservalues,showingthatexecutionchoicescanbeguidedbyindividualizedvaluepreferences.
Incasesofambiguity,actionpolicymayalsoinvolveproactiveclarification.Forexample,ColorAgent[90]learnsto
engagetheuserwhenintentionsorinstructionsareincompletebeforecommittingtoanexecutionchoice.
6.1.2 ActionGrounding. Actiongroundingoperationalizesaselectedactionbyinstantiatingitintoexecutabletool
callswithuser-conditionedconstraintsandparameters[14,20].Whilemanyrequestscanbegroundedbydirectly
applyinguser-specificsettings,personalizationbecomesmorechallengingincornercases.Afrequentgrounding-time
failure mode is infeasibility, where the instantiated query becomes unsatisfiable under the imposed constraints.
AWARE-US[80]framesthisasapreference-awarequeryrepairproblem,arguingthatagentsshouldrestorefeasibility
byrelaxingtheleastpreferredconstraintstotheuserratherthanapplyingdefaultheuristics.Anotherrecurringissue
istheomissionofessentialtoolarguments.Huangetal.[55]studyhowagentsinferunspecifiedargumentsfromuser
profiles,reducingexecutionfrictionwhilemaintainingalignmentwithuserintent.
6.2 Post-actionStage
Thepost-actionstageclosestheloopafteranactionisexecuted.Givenexecutionresult,theagentevaluateswhetherthe
outcomesatisfiesuser-conditionedobjectives,appliescorrectiveadjustmentswhenmismatchesarise(execution-time
correction),andproducesfinaloutputsthatconformtouserpreferencesandqualitycriteria(outcomerealization).
6.2.1 Execution-TimeCorrection. Afailedexecutioncommonlyproducesfeedbacksignals,whichcanbeleveraged
foradjustingbehaviorwithoutre-planningfromscratch.Explicitstudiesonpreference-awarerecoveryinPLAs
remainlimited.Nevertheless,adjacentworksuggestsusefulmechanismsforthisstage.Forexample,researchon
mitigatingtooloveruseunderdiminishingreturns[143]andstructuredreflectionovertool-interactionfailures[179]
providesbuildingblocksforfuturepersonalizedrecoverystrategies.
6.2.2 OutcomeRealization. Evenwhenmultipleexecutionoutcomesarefunctionallyvalid,usersatisfactiondepends
onhowfinalresultsarepresentedinaccordancewithindividualpreferences.Onecommonmechanismispersonalized
re-ranking,whichtransformscandidateresultsintooutputsthatbetterreflectuser-specificutility[138].Methodssuch
asPEARandMIRexplicitlymodeluserpreferencefeaturestogetherwithcross-itemdependencies,producingmore
faithfulfinalrankings[96,232].Personalizationmayalsogovernwhichoutcomesareretainedordiscarded:WARPP
[117]adjustsworkflowbranchesatruntimebasedonuserattributes,reducingirrelevantorerroneousoutcomes
withoutre-planningthefullprocess.Finally,outcomerealizationcanextendbeyondselectingamongexistingresults
toproactivelyaugmentingthem.ETAPP[50]treatsproactivityasapersonalizationsignal,evaluatingwhetheragents
canproposeadditionalactionsorsuggestionstobettersatisfyuserneeds.
RoleandChallenges. Actionexecutionisthestageatwhichpersonalizeddecisionsaretranslatedintoconcrete
operationsandexternaloutcomesinPLAs[23,148].Assuch,itbridgeshigh-levelreasoningwithobservablebehavior,
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

16 • Y.Xuetal.
determiningwhetherpersonalizationisactuallyrealizedratherthanremainingatthelevelofinternalreasoning.This
stageisespeciallyimportantbecauseuserexperiencedependsnotonlyonwhattheagentdecides,butalsoonhow
thosedecisionsareinstantiatedanddelivered.Atthesametime,personalizedactionexecutionremainschallenging
forseveralreasons.Executioncontextsarehighlyheterogeneousacrosstools,environments,anddomains,makingit
difficulttodesigngeneralmechanismsthatconsistentlyrespectindividualpreferences.Moreover,execution-time
personalizationsignalsareoftensubtle,requiringabstractpreferencestobetranslatedintoconcreteparametersrather
thanexplicitinstructions.Finally,executionfeedbackmayrevealambiguityorbrittlenessinhowuserpreferences
wereinterpretedupstream,requiringcarefulhandlingand,insomecases,coordinationwithplanningorpreference-
modelingcomponentstoavoidcascadingerrors.
FutureDirections. Researchonpersonalizedactionexecutionremainsrelativelylimited,leavingseveralpromising
directionsopen.Oneisthedevelopmentofpersonalization-awareexecutionprimitivesandtoolsthataccountnot
onlyfortaskcorrectnessbutalsofornon-functionaluserpreferences.Anotherislearningpreference-conditioned
executionpoliciesthatgeneralizeacrosstoolsandenvironments,enablingagentstoreusepersonalizationsignals
moreeffectively.Itisalsoimportanttoimprovehowagentshandlevagueormissingarguments,localizeexecution
failures,andaggregateoutcomesinwaysthatreflectuserprioritiesratherthandefaultheuristics.Morebroadly,this
stagewouldbenefitfromexecution-levelevaluationprotocolsthatmovebeyondtasksuccesstoassesspreference
adherence,consistency,andusersatisfaction.
7 Evaluation
Evaluatingpersonalizedagentsrequiresgoingbeyondconventionaltask-centricassessment,becausetheobjective
is not only task correctness but also long-horizon, user-specific utility. This challenge stems from the fact that
humanpreferencesareoftenimplicit,context-dependent,andevolvingthroughinteraction,makingpersonalization
difficulttomeasurewithasingleobjectivecriterion.Asaresult,evaluationshouldcapturenotonlywhetheran
agentcompletesatask,butalsowhetheritalignswithanindividualuser’spreferences,expectations,andexperience
overtime.Inthissection,weprovideasystematicoverviewofevaluationforpersonalizedLLM-poweredagents.
AssummarizedinFigure5,weorganizethediscussionintothreelayers:evaluationgoalsandmetricdimensions,
assessmentparadigms,andrepresentativebenchmarkfamilies.
Evaluation Goals Assessment Paradigms Benchmarks
Effectiveness Restrictive Interactive Alignment Benchmarks
Automatic Scoring -Preference Discover
-Output-level Alignment
Risk Adaptivity Rule-based Constraint -Component-probing
Personalized Checking
Agent
LLM-as-a-judge User-Substitution Benchmarks
-Textual and Dialogue
Robustness Generalization
LLM-based Evaluator -Planning and Tool-use
-Embodied and Spatial
Flexible
Fig.5. OverviewofevaluationforpersonalizedLLM-poweredagents.Evaluationisorganizedalongthreelayers:(1)evaluation
goalsandmetricdimensions,includingeffectiveness,adaptivity,generalization,robustness,andrisk;(2)assessmentparadigms,
suchasautomaticscoring,rule-basedchecking,learnedevaluators,andLLM-as-a-judge;and(3)representativebenchmark
families,includinginteractivealignmentanduser-substitutionsettings.
7.1 EvaluationGoalsandMetrics
Arigorousevaluationframeworkforpersonalizedagentsmustreflectthemulti-facetednatureofpersonalization
quality.Beyondobjectivetasksuccess,anagentshouldalignwithindividualpreferences,remaincoherentacross
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 17
contexts and over time, adapt when preferences are revealed or revised, and operate within safety and privacy
constraints. Motivated by these requirements, we organize evaluation metrics for personalized agents into five
complementarydimensions:Effectiveness,Adaptivity,Generalization,Robustness,andRisk,asillustratedin
Table2.Thesemetricdimensionsdonotapplyuniformlyacrossallcapabilities,butprovideastructuredbasisfor
comparingpersonalizedagentsacrosstasks,preferencesources,andassessmentparadigms.
Table2. EvaluationmetricsforpersonalizedLLM-poweredagents.
Goal Metric Description
Measureswhethertheagentcancorrectlydiscoveruserpreferences
DiscoveryAccuracy[63,92]
orintentsfromtheinteraction.
Measurestheabilityofthemodeltoincorporateuser-specificknowl-
KnowledgeIntegrationScore[7,199]
edgeorpersonainformationintogeneratedoutputs.
Measuresthealignmentbetweentheagent’soutputanduserpref-
PreferenceAlignment[229,262]
erencesorstatedconstraints.
Measureswhethermulti-stepplansortool-usesequencesconform
Effectiveness Preference-AwarePlanningAccuracy[234,235]
toindividualuserpreferences.
Comparespersonalizedoutputsagainstanon-personalizedbaseline
PreferenceLift[50,92,225]
onthesameprompt,reportingtheliftinpreferencescore.
Measurestheconsistencyoftheagent’stextualstyleandexpressed
ConsistencyScore[123]
personalityacrossthewholeconversation.
Measuresthedegreetowhichtheresponseshowsunderstanding
EmotionalEmpathy[229]
andcompassionfortheuser’semotionalstate.
Assessestheratioofsuccessfulpersonalizationafterreceivingnew
AdaptationSuccessRate[62,164]
preferencesignals.
Measures the ability to revise, overwrite, or remove previously
SelectiveForgetting[52]
storedinformationofuserswhenfacedwithcontradictoryevidence.
Measurestheefficiencyofadapting,suchasnumberofturns,clari-
Adaptivity InteractionEfficiency[92]
ficationquestions,oreditsneededtosatisfyuserexpectations.
Measurestheabilityoftheagenttoproactivelyidentifyuserneeds
Proactivity[50] andofferingextrasuggestionsoractionstoenhanceusersatisfac-
tion.
Measurestheabilityoftheagenttogeneralizeuserpreferencesto
Generalization Out-of-DomainPerformance[62]
otherscenariosortaskswithoutexplicitinstruction.
Measurestheaccuracyoftheagent’sactionwhensomeinformation
AccuracyunderAmbiguity[55,135]
Robustness ismissingorambiguous.
Evaluatesthemodel’sabilitytoidentifyandrejectincorrectinfor-
MisinformedConditionPerformance[53]
mationwhentheuserismisinformed.
Measureswhethertheagentcanmakesafedecisionsbasedondif-
SafetyRate[226]
ferentuserprofiles.
Measureswhethertheagentcanrecognizeandrespondappropri-
Risk RiskSensitivity[229]
atelytopotentialrisksintheuser’scontext.
Measuresthepercentageofconversationsinwhichtheagentdis-
PrivacyLeakageRate[123,266] closesprivateinformationinappropriatelyintasksrelatedtousers’
privacyinformation.
Over-SecrecyRate[123] Measuresthefailuresofutilitythatarisefromexcessivecaution.
Effectiveness. Effectivenesscaptureswhetherapersonalizedagentcanproduceuser-contingentutilityratherthan
merelygenerichelpfulness.Itcoversatleastthreeaspects:whethertheagentcaninferwhattheuserwantsfrom
partialinteractiontracesorcontextualsignals;whetheritcancorrectlyincorporateuser-specificinformationinto
planningandgeneration;andwhetherthefinalresponseoractionactuallysatisfiesexplicitconstraintsandimplicit
preferences.MetricssuchasDiscoveryAccuracy[63],KnowledgeIntegrationScore[7,199],PreferenceAlignment
[229,262],andPreference-AwarePlanningAccuracy[234,235]targettheseaspectsfromdifferentangles.Beyond
absolutealignment,PreferenceLift[50,92,225]measuresgainsoveranon-personalizedbaselineunderthesame
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

18 • Y.Xuetal.
prompt.Inmulti-turnsettings,ConsistencyScore[123]evaluatesstabilityofpersonaandvaluesovertime,while
EmotionalEmpathy[229]captureswhetherresponsesremainaffect-appropriateandsupportive.
Adaptivity. Adaptivityevaluateswhetherapersonalizedagentcanupdateitsbehaviorasnewevidenceabout
userpreferencesbecomesavailable,whilepreservingcontinuityandminimizinguserburden.AdaptationSuccess
Rate[62,164]measureswhethertheagentimprovespersonalizationafterreceivingexplicitfeedback,additional
constraints, or new user context. Because preferences may evolve or even contradict earlier evidence, Selective
Forgetting[52]isequallyimportantforassessingwhetheroutdatedmemorycanberevised,overwritten,orremoved
appropriately.InteractionEfficiency[92]capturesthecostofadaptation,suchasthenumberofturns,clarifications,
oreditsrequiredbeforetheuseracceptstheresult.Proactivity[50]complementsthesemetricsbymeasuringwhether
theagentcananticipateneedsandofferhelpfulnextstepsattherighttimewithoutcreatingunnecessaryinterruption
orirrelevantsuggestions.
Generalization. Generalizationcaptureswhetherpersonalizationtransfersbeyondthecontextsinwhichitwas
originallylearned.Inpractice,ausefulpersonalizedagentshouldnotrequiretheusertorestatepreferencesforevery
newdomain,task,orsituation.Out-of-DomainPerformance[62]thereforemeasureswhetherpreferencesacquired
inonesettingcanbeappliedappropriatelyinothers.Thisdimensionisespeciallyimportantforgeneral-purpose
agentsthatareexpectedtosupportdiversedailyactivities,wherepersonalizationmustremainreusableratherthan
narrowlytiedtoasingletaskcontext.
Robustness. Personalizedagentsoperateundernoisy,incomplete,andsometimesmisleadingpreferenceevidence,so
evaluationmustmeasurereliabilityunderstressratherthanonlyaverage-casealignment.Tworobustnesspressures
areespeciallyimportant.First,userpreferencesareoftenunderspecified,partiallyobserved,orexpressedindirectly.
AccuracyunderAmbiguity[55,135]thereforeevaluateswhethertheagentcanmakereasonableinferences,ask
targetedclarificationquestions,andavoidoverconfidentassumptionswhenkeysignalsaremissing.Second,user
inputsmaybeincorrectorbasedonmisconceptions.MisinformedConditionPerformance[53]measureswhetherthe
agentcanidentifyflawedpremises,providecorrectiveguidance,andstillpreserveapersonalizedinteractionstyle.
Risk. Riskmetricsquantifysafety,privacy,andotherdownsideconstraintsthatareinseparablefrompersonalization.
SafetyRate[226]measureswhethertheagentremainssafeacrossheterogeneoususerprofiles,includingcaseswhere
userpreferencesmayconflictwithpoliciesorwhererequestsinvolveriskyactions.RiskSensitivity[229]evaluates
whethertheagentcanrecognizecontextualhazardsandcalibrateitsadviceappropriately,forexample,byproviding
warnings,suggestingsaferalternatives,orencouragingprofessionalhelpwhenneeded.Becausepersonalization
reliesonuser-specificinformation,PrivacyLeakageRate[123,266]measureswhethertheagentdisclosesprivatedata
indisallowedways,especiallyunderadversarialorindirectprompts.Conversely,Over-SecrecyRate[123]captures
utilitylossfromexcessivecaution,wheretheagentwithholdsbenignbuthelpfulinformationdespitealegitimate
request.Thesemetricsreflectthecentralchallengeofmaximizinguserutilitywhilerespectingriskconstraints.
7.2 AssessmentParadigms
Themetricdimensionsabovecanbeoperationalizedthroughdifferentassessmentparadigms,dependingonwhether
thetargetcriterionisobjectivelyverifiableorinherentlyuser-contingent.Wegroupmainstreamparadigmsinto
fourfamilies.(1)Automaticscoringapplieswhenground-truthlabelsorreferenceanswersareavailable.Typical
examplesincludeaccuracyandprecision/recall/F1forclassification,aswellasoverlap-basedmetricssuchasBLEU
[137]andROUGE[100]forgeneration.(2)Rule-basedconstraintcheckingevaluateswhetheroutputssatisfy
explicitandverifiablerequirements,suchasincludingrequiredattributes,avoidingforbiddenones,orrespecting
structuredpreferenceconstraints.Thisparadigmisespeciallyusefulfordelegation-styletasksinwhichcompliance
canbedeterministicallyvalidated.(3)LearnedLLM-basedevaluators(LLM-E)traindedicatedevaluationmodels
toassessspecificpreferencedimensions,oftenprovidingmorestableandfine-graineddiagnosticfeedbackatthe
costofreducedgenerality[198].(4)LLM-as-a-judge(LLM-J)usesageneral-purposeLLMastheevaluatorfor
user-contingentcriteriasuchaspreferencealignment,tone,andsatisfaction.Inthissetting,thejudgeistypically
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 19
conditionedonauserprofileorpreferencedescriptionandaskedtoscoreorrankcandidateoutputs[267].Toimprove
reliability,LLM-Jprotocolsoftenadoptpairwisecomparison,calibratedrubrics,andmulti-judgeaggregation.
7.3 Benchmark
Building on the above metric taxonomy, we summarize representative benchmarks for personalized agents and
organizethemintotwobroadfamilies.InteractiveAlignmentBenchmarksevaluateanagent’sabilitytoelicit,negotiate,
andrefineuserpreferencesthroughmulti-turninteraction,wheretheuserremainsanindispensablepartoftheloop.
Incontrast,User-SubstitutionBenchmarksevaluatewhetheranagentcanstandinfortheuserbysimulatingtheir
preferencesorpersonatoproduceuser-consistentresponsesordecisionswithoutfurtheruserinput.Mainstream
benchmarksaresummarizedinTable31.
7.3.1 InteractiveAlignmentBenchmarks.
PreferenceDiscoveryBenchmarks. Acorechallengeininteractivealignmentispreferencediscovery,wherethe
agentmustrecognize,infer,anditerativelyrefineuserintentsandpreferencesfromheterogeneoussignals,ranging
fromexplicitinstructionstoimplicitfeedbackandcontextualcues[193].Inthiscategory,IndieValueCatalog[63]
curatesvalue-expressingstatementsfromdiverseindividualsandevaluateswhethermodelscaninferindividualized
valuejudgments,highlightinglimitationsincapturingfine-grainedpersonalvalues.PersonaBench[186]constructs
syntheticyetrealisticpersonalprofilesandassociatedartifactstotestwhetheragentscanextractandreasonover
user-specificinformation.PrefDisco[92]proposesameta-evaluationframeworkthatemphasizesinteractiveelicitation
efficiency,measuringwhetheranagentcanproactivelyaskinformativequestionsforauser-alignedsolutionwith
minimalinteractionturns.
Output-levelAlignmentBenchmarks. Thiscategoryevaluatespersonalizationinanend-to-endmanner,focusingon
whethertheagent’sfinaloutputssatisfyatargetuser’spreferencesandconstraintsinrealisticinteractivesettings.
Forconversation-centeredpersonalization,benchmarkssuchasALOE[225]andPrefEval[262]testwhetheragents
caninfer,retain,andconsistentlyfollowuserpreferencesacrossmulti-turndialogues.Beyondconversationaltasks,
PDR-Bench[99]evaluateswhetheragentscanincorporateuserprofilesintoresearchworkflowsandproduceoutputs
thatarepracticallyusefulfortheenduser.Forrecommendation,AgentRecBench[164]andRecBench+[53]assess
whetheragentscangeneratepreference-conditionedrecommendationsandadapttouserfeedback.Moregenerally,
PersonaLens[265]targetsmulti-scenario,task-orientedassistantsandevaluateswhetherpersonalizationremains
coherentacrossdiversedomainsanduserintents.
Component-probingBenchmarks. Complementarytotheabove,component-probingbenchmarksprovidecontrolled
testbedsthatisolatespecificpersonalizationcapabilities,enablingdiagnosticanalysisofwhenandhowanagent
leveragesuserinformation.PersonaFeedback[190]pairspredefinedpersonaswithqueriesandasksthemodelto
selectpersona-consistentresponses,offeringadirectprobeofpreference-conditionedalignment.Amajorsub-line
focusesonpersonalizedmemory,includingLongMemEval[222],LoCoMo[114],PerLTQA[30],MemoryAgentBench
[52],ConvoMem[135],andPAL-Bench[56],whichtestwhetheragentscanorganize,retrieve,andapplyuser-specific
memoriesunderlongconversationsorincrementalpreferencerevelation.Forpersonalizedtooluse,ETAPP[50]
andPTBench[55]evaluatewhetheragentstailortool-invocationstrategiestouserneeds,includingproactivityand
handlingmissingorambiguousinformation.Somebenchmarksexplicitlytargetadaptivityovertime;forexample,
PersonaMem[61,62]assesswhetheranagentcantrackevolvingtraitsandpreferences,reviseoutdatedbeliefs,and
generalizethemtonewscenarios.Finally,severalbenchmarksdiagnoseuser-specificrisk,suchasPSG-Agent[226]
andPENGUIN[229]thatevaluateprofile-contingentsafetyconsiderationsforLLM-basedagents,whilePrivacyBench
[123]andAgentDam[266]testprivacycomplianceforagentswhenhandlingsensitiveuserinformation.
7.3.2 User-SubstitutionBenchmarks.
TextualandDialogueBenchmarks. Textualanddialoguepersonalizationbenchmarksfocusonevaluatinghow
modelsgeneratecontentthatalignswithindividualuserpreferences,styles,andcontextualknowledge.Forinstance,
1Somebenchmarkscanpartiallyspanbothfamilies,andweplacetheminthemajorcategorytoavoidduplication.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

20 • Y.Xuetal.
long-formgenerationtasks,asinLaMP[156]andLongLaMP[79],testwhethermodelscanadaptoutputstoevolving
userinterestsovertime,whilePEFT-U[26]reformulatesclassificationproblemsintoannotator-specificinstancesto
measureuser-conditionedgenerationcapabilities.Benchmarksthatleverageretrievalorknowledgegraphs,such
asPGraphRAG[7],furtherexamineperformanceinsparseorcold-startscenarios.Beyondsingle-turngeneration,
multi-turn conversational benchmarks, including PersonaConvBench [89], PER-CHAT [228], LaMP-QA [157],
DPL[147],REGEN[161],andKBP[199]—assesswhethermodelsmaintaincoherence,adapttoauser’sconversational
style,andintegratepersonalizedknowledgeconsistentlyacrossdialogue.PRISM[78]targetsmorecomplexscenarios
whereuservaluesvaryculturallyorcontextually,evaluatingthereproductionofindividualizedsubjectivechoices.
PlanningandTool-UseBenchmarks. Benchmarksinplanningandtool-useexaminewhetherpersonalizedagents
canlearnandapplyuserpreferencestoperformsequentialormulti-steptasks.Preference-basedPlanning(PBP)[234]
simulateseverydayactivitiesacrossdiverseenvironmentstoevaluatepreference-drivenplanning,whilePETool-
Bench[235]specificallymeasurestheagent’sabilitytoselectandusetoolsaccordingtoindividualuserpreferences.
FamilyTool[210]extendsthisfocustocomplextool-basedworkflows,emphasizingtheintegrationofuser-specific
needs.Broadermulti-domainplanningbenchmarks,includingTravelPlanner++[176],TripTailor[203],TripCraft[16],
COMPASS[145],TripTide[71],andPersonalTravelSolver(PTS)[165],assesstasksrangingfromadaptiveitinerary
generationtodisruptionhandling,testingwhetheragentscaninterpretexplicitorinferredpreferencesandconstruct
coherent,user-alignedplans.
EmbodiedandSpatialBenchmarks. Embodiedandspatialbenchmarksinvestigatewhetheragentscannavigate,
manipulateobjects,andgroundactionsinphysicalorsimulatedspacesaccordingtouserpreferences.Memory-guided
interactiontasks,suchasMEMENTO[81],assesstheagent’sabilitytorecalluser-specificcues,whilePersONAL[270]
focusesonpersonalizednavigationandobjectgroundinginphotorealistichomeenvironments.PersonalizedInstance-
basedNavigation(PIN)benchmark[11]addsfurthercomplexitybyrequiringagentstolocateuser-specifictarget
objectsamongdistractorsin3Dscenes,emphasizingindividualizednavigationstrategies.
Table3. SummaryofPersonalizedBenchmark.
Benchmark Scale Task Pref. Goal Eval. Metrics
InteractiveAlignmentBenchmarks
IndieValueCatalog[63] 800 Human Inferred Effectiveness Auto. Accuracy
Value
PersonaBench[186] 582 General Inferred Effectiveness Auto. Recall,F1
PrefDisco[92] 10,000 General Interactive Effectiveness, Auto., DiscoveryAccuracy,PreferenceAlignment,
Adaptivity Rule- InteractionEfficiency,Correctness
based
PersonalLLM[225] 1000 General Given, Effectiveness LLM-J, PersonalizedReward
Inferred LLM-E
ALOE[225] 100 General Inferred Effectiveness LLM-J AlignmentLevel,ImprovementRate
PrefEval[262] 3,000 General Given, Effectiveness Auto., Accuracy,PersonalizedRate
Inferred Rule-
based,
LLM-J
AgentRecBench[164] 1,500 Recomm. Inferred Effectiveness, Auto. HitRate@N
Adaptivity
RecBench+[53] 34,494 Recomm. Given, Effectiveness, Auto. Precision,Recall,ConditionMatchRate,Fail
Inferred Robustness toRecommend
PDR-Bench[99] 250 Deep Given Effectiveness LLM-J PersonalizationAlignment,ContentQuality,
Research FactualReliability
PersonaLens[265] 122,133 Multi- Inferred Effectiveness LLM-J TaskCompletionRate,Personalization,
domain Naturalness,Coherence
PersonaFeedback[190] 8,298 General Given Effectiveness Auto. Accuracy
PerLTQA[30] 8,593 Memory Given, Effectiveness Auto., Accuracy,Precision,Recall,F1,Recall@K,
Inferred LLM-J MAP,Coherence
LoCoMo[114] 7,512 Memory Inferred Effectiveness, Auto. Precision,F1,Recall@K,ROUGE
Robustness
LongMemEval[222] 500 Memory Inferred Effectiveness Auto., Accuracy,Precision,Recall,F1,Recall@K,
LLM-J MAP,Coherence
Continuedonnextpage...
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 21
Table3–Continuedfrompreviouspage
Benchmark Scale Task Pref. Goal Eval. Metrics
MemoryAgentBench[52] 146 Memory Inferred Effectiveness, Auto. Accuracy,Recall@5,F1inAccurateRetrieval,
Adaptivity Test-TimeLearning,Long-range
UnderstandingandSelectiveForgetting
settings
ConvoMem[135] 75,336 Memory Inferred Effectiveness, Auto. Accuracy,Cost,Latency
Adaptivity
PAL-Bench[56] 100 Memory Inferred Effectiveness Auto., BLEU,WinRate
LLM-J
PTBench[55] 1,083 ToolUsage Given, Effectiveness, Auto. Accuracy
Inferred Robustness
ETAPP[50] 800 ToolUsage Inferred Effectiveness, Rule- PersonalizationScore,ProactivityScore
Adaptivity based,
LLM-J
PersonaMem[61] 5,990 General Inferred Effectiveness, Auto. Accuracy
Adaptivity
PersonaMem-v2[62] 10,000 General Inferred Effectiveness, Auto. Accuracy
Adaptivity
PSG-Agent[226] 2,900 Multi- Inferred Risk Auto. Accuracy,Precision,Recall,F1-score
domain
PENGUIN[229] 14,000 Multi- Given Risk LLM-J RiskSensitivity,EmotionalEmpathy,
domain User-specificAlignment
PrivacyBench[123] 478 General Given Risk LLM-J LeakageRate,Over-SecrecyRate,
InappropriateRetrievalRate,Consistency
Score
User-SubstitutionBenchmarks
LaMP[156] 25,095 General Inferred Effectiveness Auto. Accuracy,F1,MAE,RMSE,ROUGE
LongLaMP[79] 9,658 General Inferred Effectiveness Auto. ROUGE,METEOR
PEFT-U[26] 15,300 General Inferred Effectiveness Auto. BLEU,ROUGE-L,Distinct-1/2
PERSONA[15] 3,868 Dialogue Inferred Effectiveness Auto., Perplexity,BLEU,BERTScore,Persona
LLM-J consistency
PGraphRAG[7] 10,000 TextGen. Inferred Effectiveness Auto. MAE,RMSE,ROUGE,METEOR
PersonaConvBench 111,634 Multi- Inferred Effectiveness Auto., Accuracy,ROUGE,METEOR,BLEU,SBERT
[89] domain LLM-J similarity
PER-CHAT[228] 1,500,000 General Inferred Effectiveness Auto. Perplexity,BLEU
LaMP-QA[157] 29,666 Q&A Given Effectiveness Auto. ROUGE-1,ROUGE-L,METEOR
DPL[147] 9,472 TextGen Inferred Effectiveness Auto. ROUGE-1,ROUGE-L,BLEU,METEOR
REGEN[161] 1,258,224 Multi- Inferred Effectiveness, Auto. Recall@K,NDCG@K,MRR,BLEU,
domain Generalization ROUGE-L,Semanticsimilarity
KBP[199] 9,821 Q&A Given Effectiveness Auto., BLEU,ROUGE,Personagrounding,
LLM-J Knowledgegrounding
PRISM[78] 1,500 Decision Given Effectiveness LLM-J Preferenceagreement(LLM-J)
PBP[234] 50,000 Planning Inferred Effectiveness Auto. Levenshteindistance
PEToolBench[235] 3,000 ToolUsage Inferred Effectiveness, Auto. ToolAccuracy
Adaptivity
TravelPlanner++[176] 1,000 Travel Inferred Effectiveness Auto. Feasibility,Constraintsatisfaction
Planning
TripTailor[203] 3,800 Travel Inferred Effectiveness, Rule- Feasibility,Rationality,Personalization
Planning Adaptivity based,
Auto.,
LLM-J
TripCraft[16] 1,000 Travel Inferred Effectiveness, Auto., Temporal,Spatial,Ordering,Persona
Planning Adaptivity LLM-J
TripTide[71] 1,000 Travel Inferred Effectiveness, Auto., Intentpreservation,Adaptability
Planning Adaptivity LLM-J
PTS[165] 1,000 Travel Inferred Effectiveness, Auto. Constraintsatisfaction,Preferencealignment
Planning Adaptivity
PersonalWAB[14] 38,000 WebSearch Inferred Effectiveness Auto. Searchaccuracy,Rec.accuracy
PersONAL[270] 1,800 Embodied Inferred Effectiveness, Auto., Success,SPL,Grounding
Nav Adaptivity LLM-J
PIN[11] 1,193 Embodied Inferred Effectiveness, Auto., Success,Pathefficiency
Nav Adaptivity LLM-J
MEMENTO[81] 1,900 Embodied Inferred Effectiveness, Auto., Memoryrecall,Tasksuccess
Tasks Adaptivity LLM-J
FamilyTool[210] 1,152 ToolUsage Inferred Effectiveness, Auto. Toolaccuracy
Adaptivity
AgentDam[266] 246 WebSearch Given Risk LLM-J PrivacyLeakageRate
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

22 • Y.Xuetal.
8 Applications
PersonalizedLLM-poweredagentshavebeenappliedacrossawiderangeofsettings,fromconversationalsupportand
contentcreationtodelegatedassistanceandexpert-domainworkflows.Theseapplicationsdifferinautonomylevel,
riskprofile,andtheprimarytargetofpersonalization,butallrequireagentstotranslateuser-specificinformation
intosustained,context-sensitivebehavior.Weorganizerepresentativeapplicationsintofourgroups:conversational
assistants,contentcreation,delegationassistants,andexpertsupportinspecificdomains.
8.1 ConversationalAssistant
Conversationalassistantsarepersonalizedagentswhoseprimaryobjectiveistosupportusersthroughongoing
interaction. In this setting, personalization is realized through long-term dialogue continuity, context-sensitive
responsegeneration,andadaptationtouser-specificpreferences,tone,andsupportneeds.Weorganizerepresentative
applicationsinthiscategoryintodailydialogueassistants,emotionalsupportcompanions,andeducationalagents.
8.1.1 DailyDialogueAssistants. Personalizeddialogueassistantsfocusonmaintaininglong-termconversational
continuity,whereagentsmustpreserveuser-specificcontextandproducepreference-consistentresponsesacross
interactions[53,258].Recentworkincreasinglytreatslong-horizoninteractionitselfasabenchmarkedpersonal-
izationproblem[135,164],whilestudiesofdeployedassistantshighlighthowmemorybehaviorshapesusertrust
andexpectations[69].Inrecommendationandsearchsettings,personalizationfurtherdependsonsustaineduser
understanding, interaction history, and preference-aware decision making [214, 248, 250]. These trends are also
reflectedindeployedassistantssuchasChatGPT,Gemini,andDeepSeek,whichsupportpersistentusermemories
andcontrollablepersonalization[28,43,134].
8.1.2 EmotionalSupportCompanions. Emotionalsupportcompanionsprovidesustainedandempatheticassistance
forusers’well-being,wherepersonalizationdependsstronglyonpreferredtone,boundaries,andproactivity[58].
Inthissetting,personalizationcanarisebothfromuser-sidecustomizationoftheagent’spersonaandfromagent-
sideadaptationofsupportivestrategiesduringinteraction[4,268].RepresentativesystemsincludeComPeer[106],
whichdeliversproactivepeersupportbasedondialoguehistory,MultiAgentESC[239],whichusesastrategy-aware
multi-agentpipelineforemotionallycomplexinteractions,andARIEL[178],whichfurtherincorporatesphysiological
signalsforaffect-awareadaptation.Similarprioritiesarereflectedincompanion-styleproductssuchasReplikaand
Pi,wherelong-termpersonalizationandrelationship-buildingarecentraldesignfeatures[3,151].
8.1.3 EducationalAgents. Educationalagentspersonalizeinstructionandsupportbyadaptingguidance,feedback,
and learning materials to individual users [98, 166]. A common distinction is between personalized pedagogical
agents,whichsupportgeneralteachingandlearningworkflows,anddomain-specificagents,whichtailorassistance
tospecializedsubjects[24].RepresentativepedagogicalsystemssuchasEduAgent[236]andTeachTune[66]adapt
coursesupportbasedonlearnerprofilesandcontextualsignals,whiledomain-specificagentssuchasMathAgent
[242]andEduMAS[91]combinepersonalizationwithspecializedknowledgetoimprovelearningeffectiveness.These
directionsarealsoreflectedindeployededucationalsystemssuchasDuolingo[31].
8.2 ContentCreation
Personalized content creation concerns the generation of standalone textual artifacts, where agents adapt style,
structure,andframingtopersonalizationtargetsratherthansustaininginteractivedialogue[240].Inthissetting,
personalizationisevaluatedattheartifactlevel,givingrisetotwocomplementaryparadigms:author-centricalignment
withindividualwritingstyleandaudience-centricadaptationtoreaderknowledge,interests,orexpectations[132].
8.2.1 Author-Centric. Author-centriccontentcreationtreatspersonalizationasarequirementofauthorship,where
usersexpectgenerateddocumentstoreflecttheirwritingstyle,habitualphrasing,andlong-termpreferencesacross
independentoutputs[95,240,261].Thissettingisparticularlyimportantincreativewriting,professionaldocumenta-
tion,andbrandcommunication,wherequalityisjudgedattheartifactlevelratherthanthroughdialogue.Deployed
systemssuchasAdobeFireflyreflectthisparadigmbyadaptinggenerationtopersistentuserassets,priordocuments,
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 23
orstylisticconventions[2,60,131].Correspondingly,recentresearchhighlightsstablepreferencerepresentations
anddocument-levelalignmentascentralingredientsforeffectiveauthorialpersonalization[13,29,155,195].
8.2.2 Audience-Centric. Audience-centriccontentcreationpersonalizestextfortargetreadersratherthanforthe
author,adaptingcontenttoaudienceknowledge,expertise,interests,orusagecontextswhilepreservingtheintended
information[32,130,253].Thisparadigmappearsinsettingssuchasdifferentiatededucationalmaterials,culturally
adapteddocumentation,andaudience-awarecommunication,wherepersonalizationoperatesatthelevelofreader
groupsorsegments.Inpractice,itisreflectedinsystemssuchasPredis.aiandSalesForgeAI,whichtailorgenerated
contenttointendedaudiencegroups[142,158].Recentresearchsimilarlyemphasizesaudiencealignment,relevance,
andcomprehensionaskeycriteriaforqualityinaudience-conditionedgeneration[36,113,159,169,177,188].
8.3 DelegationAssistants
Delegationassistantsactonbehalfofusersbyinternalizingpreferences,managinginformation,planningactions,
andadaptingbehavioroverextendedhorizons.Comparedwithconversationalassistants,theyassumeastronger
degreeofdelegatedresponsibilityandthereforerequiremorepersistent,user-alignedrepresentations.
8.3.1 Information Handling. Information handling concerns the long-term acquisition, organization, retention,
andretrievalofuser-specificknowledgeasadelegatedcognitivefunction.Inthissetting,personalizationliesin
maintainingacoherentinformationalcontextthatcansupportdownstreamplanningandactionwithoutrepeated
userinput.RepresentativesystemsincludeARAG[116]andSPARK[21],whichtreatretrievalasapersonalized,
agent-drivenprocess,aswellasmemory-centricassistantssuchasMr.Rec[54]andlog-contextualizedRAG[27],
whichusepersistentinteractionhistorytosupportcontinuityacrosstasks.Similarideasappearindeployedsystems
suchasGleanandMem[42,118].
8.3.2 Task Planning. Task-planning delegation assistants translate high-level user goals into executable action
sequences while respecting user-specific preferences and contextual constraints. Personalization in this setting
is crucial for resolving trade-offs and prioritizing subtasks in a user-aligned way. Representative work includes
VAIAGE,whichframespersonalizedtravelplanningasacollaborativemulti-agentprocessunderuserrequirements
[101],aswellaslearning-basedapproachesshowingthatexplicitlymodelinguserpreferencesimprovesplanning
qualityandalignment[234].Relatedworkalsoextendspersonalizedplanningtocollaborative,embodied,andsocial
decision-makingsettings[48,149,249].
8.3.3 BehaviorAdaptation. Behavioradaptationconcernshowdelegationassistantsaligninteractionstyle,initiative,
anddecisiontendencieswithauser’shabitualpatternsovertime.Itsupportsreliabledelegationbyinternalizingstable
routineswhileremainingresponsivetoevolvinggoals,therebyreducingsupervisionandcognitiveburden.MEAgent
modelspersistentuserhabitsinmobileassistantsettings[206],whilememory-centricframeworksenableagents
toaccumulateandreuseuser-specificknowledgebeyondsingleinteractions[213,220].Test-timepersonalization
methodssuchasPersonaAgentfurthershowthatadaptivedelegationcanberealizeddynamicallythroughinferred
userpersonaswithoutretraining[254].Atthesametime,recentworkhighlightsthatmoreautonomousbehavior
adaptationalsoincreasestheneedforcontrollablepersonalizationandsafeguardsagainstmisalignment[40,182].
8.4 ExpertSupportinSpecificDomains
Personalizedagentsareincreasinglydeployedasexpertassistantsinspecializeddomainssuchashealthcare,finance,
legalservices,andresearchworkflows,whereuser-centrictailoringcanimproverelevanceandusabilitybutmustbe
reconciledwithstringentdomainconstraintsandrisk-sensitiverequirements[196].
8.4.1 Healthcare. Inhealthcare,personalizationisshiftingfromsingle-turnquestionansweringtolongitudinal,state-
fulinteraction,whereagentsmustsupportapatienttrajectoryratherthanonlyisolateddiagnoses.Frameworkssuch
asMedChainandMedPlanorganizemulti-stageclinicalpipelinesspanninghistoryelicitation,symptomclarification,
andtreatmentplanning[51,102].Toreducetherisksofover-accommodationandunsafeagreement,recentsystems
increasinglyadoptmodulararchitecturesthatseparatepatient-facingcommunicationfromclinicalverification,as
illustratedbyPolarisandColaCare[122,215].Fordata-intensivesettings,EHRAgentfurthergroundspersonalized
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

24 • Y.Xuetal.
EHRanalysisindeterministiccodeexecutionratherthanpurelygenerativereasoning[67,170].Evaluationenvi-
ronmentssuchasAgentClinichighlighttheneedtostress-testpersonalizedclinicalagentsunderdiversesimulated
patientbehaviors[112,163].
8.4.2 Finance. In finance, personalization must balance alignment with individual goals and behaviors against
cognitivebias,trustcalibration,andhardcompliancerequirements.FinPersona-basedstudiesrevealatrust–quality
paradox,showingthatpersona-drivenpersonalizationcanincreaseusertrustevenwhentheunderlyingadviceis
poorerorriskier[184,185].Thismotivatessafety-awarepersonalizationframeworkssuchasPSG-Agent,which
introducepersonality-conditionedguardrailstocalibraterecommendations[226].Atthearchitecturallevel,systems
suchasFinRobotdecomposeworkflowsintospecializedrolesfordataaggregation,quantitativeanalysis,andthesis
generation,whileGraphComplianceconstrainspersonalizationwithstructuredregulatoryreasoningpaths[25,243].
8.4.3 Legalservices. Inlegalservices,personalizationconditionsreasoningonuser-specificfacts,jurisdictions,and
draftingintents,turningassistanceintoacontext-sensitiveinferenceproblem.Acentralchallengeisstatutorydrift,
whereagentsmustapplyevolvinglawstoindividualcasesratherthanrelyingonstaticknowledge.Benchmarkssuch
asLawShiftshowthatthisadaptabilitymustoftenbeachievedatinferencetimeratherthanthroughretraining[49].
Personalizationalsoamplifieshallucinationrisksinlegaldrafting,motivatingpost-hocverificationloopssuchas
Citation-EnhancedGenerationandwatchdogframeworkslikeHalMit,whichvalidateoutputsagainstauthoritative
legalsourcesbeforedelivery[93,105].Thisisespeciallyimportantformultilingualandjurisdiction-awarelegal
assistantssuchasMina[216].
8.4.4 ResearchAssistance. Researchassistancesupportsexpertusersacrosstheresearchlifecyclebyperforming
project-andgoal-conditionedscholarlywork.EarlysystemspositionLLMagentsasgeneralresearchcollaborators
forexplorationandorchestration,asinAgentLaboratory[162],whilelaterworkmovestowarduser-andcontext-
conditionedpipelinesforprojectscoping,retrieval,anddialogue[33,120].Multi-agentsettingsfurtherextendthis
intosustained,statefulworkflowsthroughvirtualresearchgroupsanditerativeinvestigation[84,127].Recentstudies
emphasizehuman-centereddeployment,trust,andverifiabilityinrealresearchsettings,whilecomplementarywork
explorespersonalizedscaffoldingandcustomizedwritingsupportforproductivity[19,70,72].
9 OpenProblemsandFutureDirections
Despiterapidprogress,buildingrobust,scalable,anddeployablepersonalizedagentsremainsanopenchallenge.
Manyoftheremainingdifficultiesarecross-cuttingratherthanmodule-specific:theyarisefromhowusermodels
areconstructed,updated,generalized,evaluated,anddeployedunderreal-worldconstraints.Below,wesummarize
severaldirectionsthatweviewasespeciallyimportantforfutureresearch.
9.1 Decision-CriticalUserModeling
Acentralopenprobleminpersonalizedagentsishowtorepresentuserinformationinaformthatisbothexpressive
and decision-relevant. User preferences vary not only across individuals but also across tasks, aspects of a task,
andevensituationswithinthesameuser,andtheyareoftenrevealedonlyindirectlythroughbehavior,interaction
patterns,ortoolusage.Asaresult,effectivepersonalizationrequiresmorethanrichusermodeling:italsorequires
identifyingwhichuserattributesactuallymatterforthedecisionathand.Thischallengeisespeciallypronounced
acrossapplicationsettings,wheregeneral-purposeassistantsmayrelyonbroadstylisticorvaluealignment,while
domain-specificorhigh-stakesagentsdependonfine-grainedattributesthatdirectlyaffectoutcomes.Futurework
shouldthereforefocusonstructuredandadaptiveuserrepresentationsthatcandistinguishdecision-criticalsignals
fromperipheralones,ratherthanassumingafixedoruniversallyrelevantusermodel.
9.2 TemporalDynamicsandContinualPersonalization
Personalizationisinherentlydynamic:userpreferencesareprogressivelyrevealedthroughinteraction,anddifferent
aspectsofuserinformationevolveatdifferenttemporalscales.Short-terminterestsmayshiftrapidlyacrosscontexts,
whereas long-term values, goals, or reasoning styles are often more stable. This temporal heterogeneity makes
staticpersonalizationmechanismsfundamentallyinadequate.Futureresearchshouldthereforedevelopcontinual
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 25
personalization methods that can update user representations over time without catastrophic forgetting, while
distinguishingtransientpreferencesfromdurableones.Morebroadly,personalizedagentsshouldclosetheloop
betweenobservationandaction,sothatnewlyacquiredsignalscanbeincorporatedinwaysthatmaintainalignment
ratherthangraduallydegradingit.
9.3 Generalization
Personalizedagentsmustoftenoperateundersparse,uneven,ormissinguserdata,makinggeneralizationacore
challengeforreal-worlddeployment.Thisproblemarisesalongatleasttwodimensions.First,agentsmustgeneralize
tounseenorlow-interactionusers,wherelimitedevidencemakesdirectpreferenceinferenceunreliable.Second,
theymustgeneralizeacrossdomainsandtasks,wherepreferenceslearnedinonecontextmayonlypartiallytransfer
toanotherbecausetaskstructures,actionspaces,ordecisioncriteriadiffer.Promisingdirectionsincludefew-shot
andmeta-learningapproachesforrapidadaptation,uncertainty-awarepersonalizationthatavoidsoverconfident
alignmentunderweakevidence,andtransferablepreferenceabstractionsthatcapturereusabledecisionprinciples
ratherthannarrowtask-specificbehaviors.
9.4 EvaluationandBenchmarking
Evaluatingpersonalizationposesauniquechallengebecausesuccessisdefinedrelativetoindividualusersratherthan
objectivetaskcompletion.Existingbenchmarksoftenrelyonsyntheticuserdatageneratedbylanguagemodels,which
mayfailtocapturerealhumandiversityandcansufferfromhomogenizationeffects.Additionally,commonevaluation
protocolssuchasLLM-as-a-judgeraiseconcernsaboutreliabilityandalignmentwithhumansatisfaction.Future
evaluationframeworksshouldemphasizefine-grained,component-levelanalysisanddistinguishbetweenintra-user
consistencyandinter-userdifferentiation.Incorporatinghuman-in-the-loopevaluation,longitudinalinteraction
studies,anduser-centricsatisfactionmetricsmayprovidemorefaithfulassessmentsofpersonalizationquality.
9.5 PrivacyandUserControl
Personalizationinherentlydependsoncollecting,storing,andreusinguserdata,makingprivacyacentralchallenge
fordeployment.Evenwhenuserdataisstoredseparately,risksremainintheformofunauthorizedaccess,unintended
leakage,orsecondarymisuse.Moreover,self-evolvingagentsmayerodetrustifusersfeeltheynolongerunderstand
orcontrolhowtheirinformationisbeingretainedandapplied.Futuresystemsmustthereforebalancedatautility
withprivacypreservationthroughprivacy-awarememoryarchitectures,selectiveretentionpolicies,on-deviceor
federatedpersonalization,andtransparentinterfacesforinspecting,editing,andmanagingstoredinformation.In
thissense,privacyshouldbetreatednotonlyasatechnicalsafeguardbutalsoasacorepartoftheuserexperience.
9.6 EfficiencyandDeployment
Apracticalopenproblemishowtodelivermeaningfulpersonalizationunderreal-worldresourceconstraints.In
currentsystems,personalizationisoftenimplementedthroughpost-trainingadaptation,inference-timeaugmentation,
memoryretrieval,orrepeatedplanningandtooluse,allofwhichintroduceadditionalstorage,latency,andcomputation
costs.Futureworkshouldthereforeexploreworkflowdesignsthatexplicitlytradeoffpersonalizationdepthagainst
deploymentcost.Lightweightpersonalizationmechanisms,adaptivememoryusage,andbudget-awareinference
strategiesmayallowagentstoprovidesustaineduseralignmentwithoutincurringprohibitiveoverhead.
10 Conclusion
PersonalizationisbecomingadefiningcapabilityofLLM-poweredagents,enablingthemtomovebeyondgenerictask
executiontowardsustained,user-alignedcollaboration.Thissurveypresentedasystem-levelviewofpersonalized
LLM-powered agents through four core capabilities: profile modeling, memory, planning, and action execution.
Overall,personalizationshouldbeunderstoodnotasanisolatedmodule,butasasystem-widepropertyofagent
design.Despitesubstantialprogress,majorchallengesremaininusermodeling,generalization,evaluation,privacy,
and efficiency. Future progress will require integrated architectures that support personalization together with
robustness,safety,anddeployability.
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

26 • Y.Xuetal.
References
[1] DeepakBhaskarAcharya,KarthigeyanKuppan,andBDivya.2025.Agenticai:Autonomousintelligenceforcomplexgoals–acomprehensive
survey.IEEeAccess(2025).
[2] Adobe.2023.AdobeFirefly—firefly.adobe.com.https://firefly.adobe.com/.
[3] InflectionAI.[n.d.].Pi,yourpersonalAI—pi.ai.https://pi.ai/onboarding/pi-intro.
[4] JaberOAlotaibiandAmerSAlshahre.2024.TheroleofconversationalAIagentsinprovidingsupportandsocialcareforisolatedindividuals.
AlexandriaEngineeringJournal108(2024),273–284.
[5] PetrAnokhin,NikitaSemenov,ArtyomSorokin,DmitryEvseev,AndreyKravchenko,MikhailBurtsev,andEvgenyBurnaev.2024.Arigraph:
Learningknowledgegraphworldmodelswithepisodicmemoryforllmagents.arXivpreprintarXiv:2407.04363(2024).
[6] Anthropic.2025.Commonworkflows-ClaudeCodeDocs—code.claude.com.https://code.claude.com/docs/en/common-workflows.
[7] StevenAu,CameronJDimacali,OjasmithaPedirappagari,NamyongPark,FranckDernoncourt,YuWang,NikosKanakaris,Hanieh
Deilamsalehy,RyanARossi,andNesreenKAhmed.2025.Personalizedgraph-basedretrievalforlargelanguagemodels.arXivpreprint
arXiv:2501.02157(2025).
[8] BahmanBahmani,AbdurChowdhury,andAshishGoel.2010.Fastincrementalandpersonalizedpagerank.arXivpreprintarXiv:1006.2880
(2010).
[9] AshmiBanerjee,AdithiSatish,FitriNurAisyah,WolfgangWörndl,andYasharDeldjoo.2025.Collab-REC:AnLLM-basedAgenticFramework
forBalancingRecommendationsinTourism.arXivpreprintarXiv:2508.15030(2025).
[10] AndréBarreto,VincentDumoulin,YiranMao,NicolasPerez-Nieves,BobakShahriari,YannDauphin,DoinaPrecup,andHugoLarochelle.
2025.Capturingindividualhumanpreferenceswithrewardfeatures.arXivpreprintarXiv:2503.17338(2025).
[11] LucaBarsellotti,RobertoBigazzi,MarcellaCornia,LorenzoBaraldi,andRitaCucchiara.2024.Personalizedinstance-basednavigationtoward
user-specificobjectsinrealisticenvironments.AdvancesinNeuralInformationProcessingSystems37(2024),11228–11250.
[12] AvinandanBose,ZhihanXiong,YuejieChi,SimonShaoleiDu,LinXiao,andMaryamFazel.2025.LoRe:PersonalizingLLMsviaLow-Rank
RewardModeling.arXivpreprintarXiv:2504.14439(2025).
[13] HyungjuneBu,ChanjooJung,MinjaeKang,andJaehyungKim.2025.Personalizedllmdecodingviacontrastingpersonalpreference.In
Proceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.33946–33966.
[14] HongruCai,YongqiLi,WenjieWang,FengbinZhu,XiaoyuShen,WenjieLi,andTat-SengChua.2025.Largelanguagemodelsempowered
personalizedwebagents.InProceedingsoftheACMonWebConference2025.198–215.
[15] LouisCastricato,NathanLile,RafaelRafailov,Jan-PhilippFränken,andChelseaFinn.2025.Persona:Areproducibletestbedforpluralistic
alignment.InProceedingsofthe31stInternationalConferenceonComputationalLinguistics.11348–11368.
[16] SoumyabrataChaudhuri,PranavPurkar,RitwikRaghav,ShubhojitMallick,ManishGupta,AbhikJana,andShreyaGhosh.2025.Tripcraft:
A benchmark for spatio-temporally fine grained travel planning. In Proceedings of the 63rd Annual Meeting of the Association for
ComputationalLinguistics(Volume1:LongPapers).17035–17064.
[17] JiaruiChen.2025.MemoryAssistedLLMforPersonalizedRecommendationSystem.arXivpreprintarXiv:2505.03824(2025).
[18] Wei-HaoChen,WeixiTong,AmandaCase,andTianyiZhang.2025.Dango:amixed-initiativedatawranglingsystemusinglargelanguage
model.InProceedingsofthe2025CHIConferenceonHumanFactorsinComputingSystems.1–28.
[19] ZanChen,JingjingChen,YuGuangWang,andYiqingShen.2025.AHuman-CenteredAIAgentFrameworkwithLargeLanguageModelsfor
AcademicResearchTasks.InCCFInternationalConferenceonNaturalLanguageProcessingandChineseComputing.Springer,363–374.
[20] ZihaoCheng,HongruWang,ZemingLiu,YuhangGuo,YuanfangGuo,YunhongWang,andHaifengWang.2025.ToolSpectrum:Towards
personalizedtoolutilizationforlargelanguagemodels.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.20679–20699.
[21] GaurabChhetri,SubasishDas,andTausifIslamChowdhury.2025.SPARK:SearchPersonalizationviaAgent-DrivenRetrievalandKnowledge-
sharing.arXivpreprintarXiv:2512.24008(2025).
[22] PrateekChhikara,DevKhant,SaketAryan,TaranjeetSingh,andDeshrajYadav.2025.Mem0:Buildingproduction-readyaiagentswith
scalablelong-termmemory.arXivpreprintarXiv:2504.19413(2025).
[23] SadiaSultanaChowa,RiasadAlvi,SubheySadiRahman,MdAbdurRahman,MohaimenulAzamKhanRaiaan,MdRafiqulIslam,Mukhtar
Hussain,andSamiAzam.2026.Fromlanguagetoaction:areviewoflargelanguagemodelsasautonomousagentsandtoolusers.Artificial
IntelligenceReview(2026).
[24] ZhendongChu,ShenWang,JianXie,TinghuiZhu,YiboYan,JinhengYe,AoxiaoZhong,XumingHu,JingLiang,PhilipSYu,etal.2025.Llm
agentsforeducation:Advancesandapplications.arXivpreprintarXiv:2503.11733(2025).
[25] JiseongChung,RonnyKo,WonchulYoo,MakotoOnizuka,SungmokKim,Tae-WanKim,andWon-YongShin.2025.GraphCompliance:
AligningPolicyandContextGraphsforLLM-BasedRegulatoryCompliance.arXivpreprintarXiv:2510.26309(2025).
[26] ChristopherClarke,YuzhaoHeng,LingjiaTang,andJasonMars.2024.Peft-u:Parameter-efficientfine-tuningforuserpersonalization.arXiv
preprintarXiv:2407.18078(2024).
[27] ClaytonCohn,SuryaRayala,CaitlinSnyder,JoyceFonteles,ShrutiJain,NaveeduddinMohammed,UmeshTimalsina,SarahKBurriss,
NamrataSrivastava,MentonDeweese,etal.2025.PersonalizingStudent-AgentInteractionsUsingLog-ContextualizedRetrievalAugmented
Generation(RAG).arXivpreprintarXiv:2505.17238(2025).
[28] DeepSeek.2024.DeepSeek|deepseek.com.https://www.deepseek.com/.
[29] PriyankaDey,DanieleRosa,WenqingZheng,DanielBarcklow,JieyuZhao,andEmilioFerrara.2025.GRAVITY:AFrameworkforPersonalized
TextGenerationviaProfile-GroundedSyntheticPreferences.arXivpreprintarXiv:2510.11952(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 27
[30] YimingDu,HongruWang,ZhengyiZhao,BinLiang,BaojunWang,WanjunZhong,ZezhongWang,andKam-FaiWong.2024.Perltqa:A
personallong-termmemorydatasetformemoryclassification,retrieval,andsynthesisinquestionanswering.arXivpreprintarXiv:2402.16288
(2024).
[31] Duolingo.2025.Learnalanguageforfree—duolingo.com.https://www.duolingo.com/.
[32] MehmetSametDuranandTevfikAytekin.2025.Beyondone-size-fits-allsummarization:Customizingsummariesfordiverseusers.arXiv
preprintarXiv:2503.10675(2025).
[33] JacobEmmerson,RayidGhani,andZheyuanRyanShi.2025.TowardsAutomatedScopingofAIforSocialGoodProjects.arXivpreprint
arXiv:2504.20010(2025).
[34] JizhanFang,XinleDeng,HaomingXu,ZiyanJiang,YuqiTang,ZiwenXu,ShuminDeng,YunzhiYao,MengruWang,ShuofeiQiao,etal.
2025.LightMem:LightweightandEfficientMemory-AugmentedGeneration.arXivpreprintarXiv:2510.18866(2025).
[35] MohamedAmineFerrag,NorbertTihanyi,andMerouaneDebbah.2025.Fromllmreasoningtoautonomousaiagents:Acomprehensive
review.arXivpreprintarXiv:2504.19678(2025).
[36] XiaoFu,HosseinARahmani,BinWu,JeromeRamos,EmineYilmaz,andAldoLipani.2025.PREF:Reference-FreeEvaluationofPersonalised
TextGenerationinLLMs.arXivpreprintarXiv:2508.10028(2025).
[37] GeGao,AlexeyTaymanov,EduardoSalinas,PaulMineiro,andDipendraMisra.2024.Aligningllmagentsbylearninglatentpreferencefrom
useredits.AdvancesinNeuralInformationProcessingSystems37(2024),136873–136896.
[38] Huan-angGao,JiayiGeng,WenyueHua,MengkangHu,XinzheJuan,HongzhangLiu,ShilongLiu,JiahaoQiu,XuanQi,YiranWu,etal.
2025.Asurveyofself-evolvingagents:Onpathtoartificialsuperintelligence.arXivpreprintarXiv:2507.21046(2025).
[39] ShenGao,YuntaoWen,MinghangZhu,JianingWei,YuhanCheng,QunziZhang,andShuoShang.2024.Simulatingfinancialmarketvia
largelanguagemodelbasedagents.arXivpreprintarXiv:2406.19966(2024).
[40] SimretArayaGebreegziabher,YukunYang,CharlesChiang,HojunYoo,ChaoranChen,HyoJinDo,ZahraAshktorab,WernerGeyer,Diego
Gómez-Zará,andTobyJia-JunLi.2026. TheBehavioralFabricofLLM-PoweredGUIAgents:HumanValuesandInteractionOutcomes.
arXivpreprintarXiv:2601.16356(2026).
[41] Github.2025.GitHubCopilotfeatures-GitHubDocs—docs.github.com.https://docs.github.com/en/copilot/get-started/features.
[42] Inc.GleanTechnologies.2023.Glean—glean.com.https://www.glean.com/.
[43] Google.2023.GoogleGemini—gemini.google.com.https://gemini.google.com/.
[44] ZhibinGou,ZhihongShao,YeyunGong,YelongShen,YujiuYang,NanDuan,andWeizhuChen.2023.Critic:Largelanguagemodelscan
self-correctwithtool-interactivecritiquing.arXivpreprintarXiv:2305.11738(2023).
[45] JianGuan,JunfeiWu,Jia-NanLi,ChuanqiCheng,andWeiWu.2025.ASurveyonPersonalizedAlignment—TheMissingPieceforLarge
LanguageModelsinReal-WorldApplications.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.5313–5333.
[46] DayaGuo,DejianYang,HaoweiZhang,JunxiaoSong,RuoyuZhang,RunxinXu,QihaoZhu,ShirongMa,PeiyiWang,XiaoBi,etal.2025.
Deepseek-r1:Incentivizingreasoningcapabilityinllmsviareinforcementlearning.arXivpreprintarXiv:2501.12948(2025).
[47] BernalJiménezGutiérrez,YihengShu,WeijianQi,SizheZhou,andYuSu.2025.Fromragtomemory:Non-parametriccontinuallearningfor
largelanguagemodels.arXivpreprintarXiv:2502.14802(2025).
[48] DonggeHan,TrevorMcInroe,AdamJelley,StefanoVAlbrecht,PeterBell,andAmosStorkey.2025.Llm-personalize:Aligningllmplanners
withhumanpreferencesviareinforcedself-trainingforhousekeepingrobots.InProceedingsofthe31stInternationalConferenceon
ComputationalLinguistics.1465–1474.
[49] ZhuoHan,YiYang,YiFeng,WanhongHuang,XuxingDing,ChuanyiLi,JidongGe,andVincentNg.2025.LawShift:BenchmarkingLegal
JudgmentPredictionUnderStatuteShifts.InTheThirty-ninthAnnualConferenceonNeuralInformationProcessingSystemsDatasetsand
BenchmarksTrack.
[50] YupuHao,PengfeiCao,ZhuoranJin,HuanxuanLiao,YuboChen,KangLiu,andJunZhao.2025.Evaluatingpersonalizedtool-augmentedllms
fromtheperspectivesofpersonalizationandproactivity.InProceedingsofthe63rdAnnualMeetingoftheAssociationforComputational
Linguistics(Volume1:LongPapers).21897–21935.
[51] Hsin-LingHsu,Cong-TinhDao,LuningWang,ZitaoShuai,ThaoNguyenMinhPhan,Jun-EnDing,Chun-ChiehLiao,PengfeiHu,Xiaoxue
Han,Chih-HoHsu,etal.2025.Medplan:atwo-stagerag-basedsystemforpersonalizedmedicalplangeneration.InProceedingsofthe63rd
AnnualMeetingoftheAssociationforComputationalLinguistics(Volume6:IndustryTrack).1072–1082.
[52] YuanzheHu,YuWang,andJulianMcAuley.2025.Evaluatingmemoryinllmagentsviaincrementalmulti-turninteractions.arXivpreprint
arXiv:2507.05257(2025).
[53] ChengkaiHuang,JundaWu,YuXia,ZixuYu,RuhanWang,TongYu,RuiyiZhang,RyanARossi,BranislavKveton,DongruoZhou,etal.
2025.Towardsagenticrecommendersystemsintheeraofmultimodallargelanguagemodels.arXivpreprintarXiv:2503.16734(2025).
[54] JianiHuang,XingchenZou,LianghaoXia,andQingLi.2025.Mr.rec:Synergizingmemoryandreasoningforpersonalizedrecommendation
assistantwithllms.arXivpreprintarXiv:2510.14629(2025).
[55] XuHuang,YuefengHuang,WeiwenLiu,XingshanZeng,YashengWang,RuimingTang,HongXie,andDefuLian.2025.Advancingand
BenchmarkingPersonalizedToolInvocationforLLMs.arXivpreprintarXiv:2505.04072(2025).
[56] ZhaopeiHuang,QifengDai,GuozhengWu,XiaopengWu,KehanChen,ChuanYu,XubinLi,TiezhengGe,WenxuanWang,andQin
Jin.2025. Mem-PAL:TowardsMemory-basedPersonalizedDialogueAssistantsforLong-termUser-AgentInteraction. arXivpreprint
arXiv:2511.13410(2025).
[57] ZhengjunHuang,ZhoujinTian,QintianGuo,FangyuanZhang,YingliZhou,DiJiang,andXiaofangZhou.2025.LiCoMemory:Lightweight
andCognitiveAgenticMemoryforEfficientLong-TermReasoning.arXivpreprintarXiv:2511.01448(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

28 • Y.Xuetal.
[58] BaharIrfan,SannaKuoppamäki,andGabrielSkantze.2024.Recommendationsfordesigningconversationalcompanionrobotswitholder
adultsthroughfoundationmodels.FrontiersinRoboticsandAI11(2024),1363713.
[59] GautierIzacard,MathildeCaron,LucasHosseini,SebastianRiedel,PiotrBojanowski,ArmandJoulin,andEdouardGrave.2021.Unsupervised
denseinformationretrievalwithcontrastivelearning.arXivpreprintarXiv:2112.09118(2021).
[60] Jasper.2023.JasperBrandVoice—jasper.ai/brand-voice.https://www.jasper.ai/brand-voice.
[61] BowenJiang,ZhuoqunHao,Young-MinCho,BryanLi,YuanYuan,SihaoChen,LyleUngar,CamilloJTaylor,andDanRoth.2025.Knowme,
respondtome:Benchmarkingllmsfordynamicuserprofilingandpersonalizedresponsesatscale.arXivpreprintarXiv:2504.14225(2025).
[62] BowenJiang,YuanYuan,MaohaoShen,ZhuoqunHao,ZhangchenXu,ZichenChen,ZiyiLiu,AnveshRaoVijjini,JiashuHe,HanchaoYu,
etal.2025.PersonaMem-v2:TowardsPersonalizedIntelligenceviaLearningImplicitUserPersonasandAgenticMemory.arXivpreprint
arXiv:2512.06688(2025).
[63] LiweiJiang,TaylorSorensen,SydneyLevine,andYejinChoi.2024.Canlanguagemodelsreasonaboutindividualistichumanvaluesand
preferences?arXivpreprintarXiv:2410.03868(2024).
[64] XunJiang,FengLi,HanZhao,JiahaoQiu,JiayingWang,JunShao,ShihaoXu,ShuZhang,WeilingChen,XavierTang,etal.2024.Longterm
memory:Thefoundationofaiself-evolution.arXivpreprintarXiv:2410.15665(2024).
[65] BernalJimenezGutierrez,YihengShu,YuGu,MichihiroYasunaga,andYuSu.2024.Hipporag:Neurobiologicallyinspiredlong-termmemory
forlargelanguagemodels.AdvancesinNeuralInformationProcessingSystems37(2024),59532–59569.
[66] HyoungwookJin,MinjuYoo,JeongeonPark,YokyungLee,XuWang,andJuhoKim.2025.Teachtune:Reviewingpedagogicalagentsagainst
diversestudentprofileswithsimulatedstudents.InProceedingsofthe2025CHIConferenceonHumanFactorsinComputingSystems.
1–28.
[67] MingyuJin,QinkaiYu,DongShu,ChongZhang,LizhouFan,WenyueHua,SuiyuanZhu,YandaMeng,ZhentingWang,MengnanDu,etal.
2024.Health-llm:Personalizedretrieval-augmenteddiseasepredictionsystem.arXivpreprintarXiv:2402.00746(2024).
[68] JeffJohnson,MatthijsDouze,andHervéJégou.2019.Billion-scalesimilaritysearchwithGPUs.IEEETransactionsonBigData7,3(2019),
535–547.
[69] BrennanJones,KelseyStemmler,EmilySu,Young-HoKim,andAnastasiaKuzminykh.2025.Users’ExpectationsandPracticeswithAgent
Memory.InProceedingsoftheExtendedAbstractsoftheCHIConferenceonHumanFactorsinComputingSystems.1–8.
[70] AymenKabir,SurajShah,AlexanderHaddad,andDanielMSRaper.2025.IntroducingourcustomGPT:Anexampleofthepotentialimpact
ofpersonalizedGPTbuildersonscientificwriting.WorldNeurosurgery193(2025),461–468.
[71] PriyanshuKarmakar,SoumyabrataChaudhuri,ShubhojitMallick,ManishGupta,AbhikJana,andShreyaGhosh.2025.TripTide:ABenchmark
forAdaptiveTravelPlanningunderDisruptions.arXivpreprintarXiv:2510.21329(2025).
[72] SeanKelley,DavidDeCremer,andChristophRiedl.2025.PersonalizedAIScaffoldsSynergisticMulti-TurnCollaborationinCreativeWork.
arXivpreprintarXiv:2510.27681(2025).
[73] CallieYKim,ChristinePLee,andBilgeMutlu.2024. Understandinglarge-languagemodel(llm)-poweredhuman-robotinteraction.In
Proceedingsofthe2024ACM/IEEEinternationalconferenceonhuman-robotinteraction.371–380.
[74] HannahKim,KushanMitra,ChenShen,DanZhang,andEstevamHruschka.2025.AIPOM:Agent-awareInteractivePlanningforMulti-Agent
Systems.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing:SystemDemonstrations.85–96.
[75] JaehyungKimandYimingYang.2024.Few-shotpersonalizationofllmswithmis-alignedresponses.arXivpreprintarXiv:2406.18678(2024).
[76] MinbeomKim,Kang-ilLee,SeonghoJoo,HwaranLee,ThibautThonet,andKyominJung.2025.Drift:Decoding-timepersonalizedalignments
withimplicituserpreferences.arXivpreprintarXiv:2502.14289(2025).
[77] SangyeopKim,YohanLee,SanghwaKim,HyunjongKim,andSungzoonCho.2025.Pre-StorageReasoningforEpisodicMemory:Shifting
InferenceBurdentoMemoryforPersonalizedDialogue.arXivpreprintarXiv:2509.10852(2025).
[78] HannahRoseKirk,AlexanderWhitefield,PaulRottger,AndrewMBean,KaterinaMargatina,RafaelMosquera-Gomez,JuanCiro,Max
Bartolo,AdinaWilliams,HeHe,etal.2024.Theprismalignmentdataset:Whatparticipatory,representativeandindividualisedhuman
feedbackrevealsaboutthesubjectiveandmulticulturalalignmentoflargelanguagemodels.AdvancesinNeuralInformationProcessing
Systems37(2024),105236–105344.
[79] IshitaKumar,SnigdhaViswanathan,SushritaYerra,AlirezaSalemi,RyanARossi,FranckDernoncourt,HaniehDeilamsalehy,Xiang
Chen,RuiyiZhang,ShubhamAgarwal,etal.2024. Longlamp:Abenchmarkforpersonalizedlong-formtextgeneration. arXivpreprint
arXiv:2407.11016(2024).
[80] MehmetKurmaz.2026.AWARE-US:BenchmarkforPreference-AwareResolutioninTool-CallingAgents.arXivpreprintarXiv:2601.02643
(2026).
[81] TaeyoonKwon,DongwookChoi,SunghwanKim,HyojunKim,SeungjunMoon,Beong-wooKwak,Kuan-HaoHuang,andJinyoungYeo.
2025.EmbodiedAgentsMeetPersonalization:ExploringMemoryUtilizationforPersonalizedAssistance.arXivpreprintarXiv:2505.16348
(2025).
[82] SeongyunLee,SueHyunPark,SeungoneKim,andMinjoonSeo.2024.Aligningtothousandsofpreferencesviasystemmessagegeneralization.
AdvancesinNeuralInformationProcessingSystems37(2024),73783–73829.
[83] PatrickLewis,EthanPerez,AleksandraPiktus,FabioPetroni,VladimirKarpukhin,NamanGoyal,HeinrichKüttler,MikeLewis,Wen-tau
Yih,TimRocktäschel,etal.2020. Retrieval-augmentedgenerationforknowledge-intensivenlptasks. Advancesinneuralinformation
processingsystems33(2020),9459–9474.
[84] EdLi,JunyuRen,XintianPan,CatYan,ChuanhaoLi,DirkBergemann,andZhuoranYang.2025.BuildYourPersonalizedResearchGroup:A
MultiagentFrameworkforContinualandInteractiveScienceAutomation.arXivpreprintarXiv:2510.15624(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 29
[85] HaoLi,RuoyuanGong,andHaoJiang.2025.Politicalactoragent:Simulatinglegislativesystemforrollcallvotespredictionwithlarge
languagemodels.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.39.388–396.
[86] HaoLi,ChenghaoYang,AnZhang,YangDeng,XiangWang,andTat-SengChua.2025.Helloagain!llm-poweredpersonalizedagentfor
long-termdialogue.InProceedingsofthe2025ConferenceoftheNationsoftheAmericasChapteroftheAssociationforComputational
Linguistics:HumanLanguageTechnologies(Volume1:LongPapers).5259–5276.
[87] Jia-NanLi,JianGuan,SonghaoWu,WeiWu,andRuiYan.2025.From1,000,000userstoeveryuser:Scalinguppersonalizedpreferencefor
user-levelalignment.arXivpreprintarXiv:2503.15463(2025).
[88] Jia-NanLi,JianGuan,WeiWu,andRuiYan.2025.Extendedinductivereasoningforpersonalizedpreferenceinferencefrombehavioral
signals.arXivpreprintarXiv:2505.18071(2025).
[89] LiLi,PeilinCai,RyanARossi,FranckDernoncourt,BranislavKveton,JundaWu,TongYu,LinxinSong,TiankaiYang,YuehanQin,etal.
2025.APersonalizedConversationalBenchmark:TowardsSimulatingPersonalizedConversations.arXivpreprintarXiv:2505.14106(2025).
[90] NingLi,QiqiangLin,ZhengWu,XiaoyunMo,WeimingZhang,YinZhao,XiangmouQu,JiamuZhou,JunWang,CongminZheng,etal.
2025.ColorAgent:BuildingARobust,Personalized,andInteractiveOSAgent.arXivpreprintarXiv:2510.19386(2025).
[91] QiaomuLi,YingXie,SumitChakravarty,andDabaeLee.2024.EduMAS:AnovelLLM-poweredmulti-agentframeworkforeducational
support.In2024IEEEInternationalConferenceonBigData(BigData).IEEE,8309–8316.
[92] ShuyueStellaLi,AvinandanBose,FaezeBrahman,SimonShaoleiDu,PangWeiKoh,MaryamFazel,andYuliaTsvetkov.2025.PrefDisco:
EvaluatingProactivePersonalizationthroughInteractivePreferenceDiscovery.InFirstWorkshoponMulti-TurnInteractionsinLarge
LanguageModels.
[93] WeitaoLi,JunkaiLi,WeizhiMa,andYangLiu.2024. Citation-enhancedgenerationforLLM-basedchatbots.InProceedingsofthe62nd
AnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).1451–1466.
[94] XinzheLi.2025. Areviewofprominentparadigmsforllm-basedagents:Tooluse,planning(includingrag),andfeedbacklearning.In
Proceedingsofthe31stinternationalconferenceoncomputationallinguistics.9760–9779.
[95] XiaopengLi,PengyueJia,DerongXu,YiWen,YingyiZhang,WenlinZhang,WanyuWang,YichaoWang,ZhaochengDu,XiangyangLi,
etal.2025.Asurveyofpersonalization:Fromragtoagent.arXivpreprintarXiv:2504.10147(2025).
[96] YiLi,JiemingZhu,WeiwenLiu,LiangcaiSu,GuohaoCai,QiZhang,RuimingTang,XiXiao,andXiuqiangHe.2022.Pear:Personalized
re-rankingwithcontextualizedtransformerforrecommendation.InCompanionProceedingsoftheWebConference2022.62–66.
[97] ZhiyuLi,ShichaoSong,ChenyangXi,HanyuWang,ChenTang,SiminNiu,DingChen,JiaweiYang,ChunyuLi,QingchenYu,etal.2025.
Memos:Amemoryosforaisystem.arXivpreprintarXiv:2507.03724(2025).
[98] GuannanLiangandQianqianTong.2025.LLM-poweredAIagentsystemsandtheirapplicationsinindustry.In2025IEEEWorldAIIoT
Congress(AIIoT).IEEE,0463–0471.
[99] YuanLiang,JiaxianLi,YuqingWang,PiaohongWang,MotongTian,PaiLiu,ShuofeiQiao,RunnanFang,HeZhu,GeZhang,etal.2025.
TowardsPersonalizedDeepResearch:BenchmarksandEvaluations.arXivpreprintarXiv:2509.25106(2025).
[100] Chin-YewLin.2004.Rouge:Apackageforautomaticevaluationofsummaries.InTextsummarizationbranchesout.74–81.
[101] BinwenLiu,JiexiGe,andJiaminWang.2025.Vaiage:AMulti-AgentSolutiontoPersonalizedTravelPlanning.arXivpreprintarXiv:2505.10922
(2025).
[102] JieLiu,WenxuanWang,ZizhanMa,GuolinHuang,YihangSU,Kao-JungChang,WentingChen,HaoliangLi,LinlinShen,andMichaelLyu.
2024.Medchain:Bridgingthegapbetweenllmagentsandclinicalpracticethroughinteractivesequentialbenchmarking.arXivpreprint
arXiv:2412.01605(2024).
[103] LeiLiu,XiaoyanYang,YueShen,BinbinHu,ZhiqiangZhang,JinjieGu,andGuannanZhang.2023. Think-in-memory:Recallingand
post-thinkingenablellmswithlong-termmemory.arXivpreprintarXiv:2311.08719(2023).
[104] NaLiu,LiangyuChen,XiaoyuTian,WeiZou,KaijiangChen,andMingCui.2024.Fromllmtoconversationalagent:Amemoryenhanced
architecturewithfine-tuningoflargelanguagemodels.arXivpreprintarXiv:2401.02777(2024).
[105] SiyuanLiu,WenjingLiu,ZhiweiXu,XinWang,BoChen,andTaoLi.2025. TowardsMitigationofHallucinationforLLM-empowered
Agents:ProgressiveGeneralizationBoundExplorationandWatchdogMonitor.arXivpreprintarXiv:2507.15903(2025).
[106] TianjianLiu,HongzhengZhao,YuhengLiu,XingboWang,andZhenhuiPeng.2024. Compeer:Agenerativeconversationalagentfor
proactivepeersupport.InProceedingsofthe37thAnnualACMSymposiumonUserInterfaceSoftwareandTechnology.1–22.
[107] WenTaoLiu,RuohuaZhang,AiminZhou,FengGao,andJiaLiLiu.2025.Echo:Alargelanguagemodelwithtemporalepisodicmemory.
arXivpreprintarXiv:2502.16090(2025).
[108] YuhanLiu,MichaelJQZhang,andEunsolChoi.2025.UserFeedbackinHuman-LLMDialogues:ALenstoUnderstandUsersButNoisyasa
LearningSignal.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.2666–2681.
[109] LinLong,YichenHe,WentaoYe,YiyuanPan,YuanLin,HangLi,JunboZhao,andWeiLi.2025. Seeing,listening,remembering,and
reasoning:Amultimodalagentwithlong-termmemory.arXivpreprintarXiv:2508.09736(2025).
[110] JunyuLuo,WeizhiZhang,YeYuan,YushengZhao,JunweiYang,YiyangGu,BohanWu,BinqiChen,ZiyueQiao,QingqingLong,etal.2025.
Largelanguagemodelagent:Asurveyonmethodology,applicationsandchallenges.arXivpreprintarXiv:2503.21460(2025).
[111] YitongLuo,HouHeiLam,ZiangChen,ZhenliangZhang,andXueFeng.2025. ValuePilot:ATwo-PhaseFrameworkforValue-Driven
Decision-Making.arXivpreprintarXiv:2503.04569(2025).
[112] ChenhanLyu,YutongSong,PengfeiZhang,andAmirMRahmani.2025.Domain-SpecificConstitutionalAI:EnhancingSafetyinLLM-
PoweredMentalHealthChatbots.arXivpreprintarXiv:2509.16444(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

30 • Y.Xuetal.
[113] YiboLyu,GongweiChen,RuiShao,WeiliGuan,andLiqiangNie.2026.PersonalAlign:HierarchicalImplicitIntentAlignmentforPersonalized
GUIAgentwithLong-TermUser-CentricRecords.arXivpreprintarXiv:2601.09636(2026).
[114] AdyashaMaharana,Dong-HoLee,SergeyTulyakov,MohitBansal,FrancescoBarbieri,andYuweiFang.2024.Evaluatingverylong-term
conversationalmemoryofllmagents.InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
1:LongPapers).13851–13870.
[115] WenyuMao,JiancanWu,WeijianChen,ChongmingGao,XiangWang,andXiangnanHe.2025.Reinforcedpromptpersonalizationfor
recommendationwithlargelanguagemodels.ACMTransactionsonInformationSystems43,3(2025),1–27.
[116] RezaYousefiMaragheh,PratheekVadla,PriyankGupta,KaiZhao,AysenurInan,KehuiYao,JianpengXu,PraveenKanumala,JasonCho,and
SushantKumar.2025.ARAG:AgenticRetrievalAugmentedGenerationforPersonalizedRecommendation.arXivpreprintarXiv:2506.21931
(2025).
[117] MariaEmiliaMazzolenisandRuiruiZhang.2025.Agentwarpp:Workflowadherenceviaruntimeparallelpersonalization.arXivpreprint
arXiv:2507.19543(2025).
[118] Inc.Mem.2023.Mem—mem.ai.https://mem.ai/.
[119] memodb.2025.GitHub-memodb-io/memobase:Profile-BasedLong-TermMemoryforAIApplications.Memobasehandlesuserprofiles,
memoryevents,andevolvingcontext—perfectforchatbots,companions,tutors,customerservicebots,andallchat-basedagents.—
github.com.https://github.com/memodb-io/memobase.
[120] FengranMo,YuchenHui,YuxingTian,ZhaoxuanTan,ChuanMeng,ZhanSu,KaiyuHuang,andJian-YunNie.2025.Towardsadaptive
personalizedconversationalinformationretrieval.InProceedingsofthe34thACMInternationalConferenceonInformationandKnowledge
Management.2137–2147.
[121] NiklasMuennighoff,ZitongYang,WeijiaShi,XiangLisaLi,LiFei-Fei,HannanehHajishirzi,LukeZettlemoyer,PercyLiang,Emmanuel
Candès,andTatsunoriBHashimoto.2025. s1:Simpletest-timescaling.InProceedingsofthe2025ConferenceonEmpiricalMethodsin
NaturalLanguageProcessing.20286–20332.
[122] SubhabrataMukherjee,PaulGamble,MarkelSanzAusin,NeelKant,KritiAggarwal,NehaManjunath,DebajyotiDatta,Zhengliang
Liu,JiayuanDing,SophiaBusacca,etal.2024. Polaris:Asafety-focusedllmconstellationarchitectureforhealthcare. arXivpreprint
arXiv:2403.13313(2024).
[123] SrijaMukhopadhyay,SathwikReddy,ShruthiMuthukumar,JisunAn,andPonnurangamKumaraguru.2025.PrivacyBench:AConversational
BenchmarkforEvaluatingPrivacyinPersonalizedAI.arXivpreprintarXiv:2512.24848(2025).
[124] JohnMurzaku,ZifanLiu,MdMehrabTanjim,VaishnaviMuppala,XiangChen,andYunyaoLi.2025.ECLAIR:EnhancedClarificationfor
InteractiveResponses.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.39.28864–28870.
[125] HyunjiNam,YanmingWan,MickelLiu,JianxunLian,PeterAhnn,andNatashaJaques.2025.Learningtosummarizeuserinformationfor
personalizedreinforcementlearningfromhumanfeedback.arXivpreprintarXiv:2507.13579(2025).
[126] JiayanNan,WenquanMa,WenlongWu,andYizeChen.2025.Nemori:Self-organizingagentmemoryinspiredbycognitivescience.arXiv
preprintarXiv:2508.03341(2025).
[127] VladimirNaumov,DianaZagirova,ShaLin,YupengXie,WenhaoGou,AnatolyUrban,NinaTikhonova,KhadijaAlawi,MikeDurymanov,
FedorGalkin,etal.2025. Doraaiscientist:Multi-agentvirtualresearchteamforscientificexplorationdiscoveryandautomatedreport
generation.bioRxiv(2025).
[128] LewisNewshamandDanielPrince.2025.Personality-DrivenDecisionMakinginLLM-BasedAutonomousAgents.InProceedingsofthe
24thInternationalConferenceonAutonomousAgentsandMultiagentSystems.1538–1547.
[129] LinNing,LuyangLiu,JiaxingWu,NeoWu,DevoraBerlowitz,SushantPrakash,BradleyGreen,ShawnO’Banion,andJunXie.2025.User-llm:
Efficientllmcontextualizationwithuserembeddings.InCompanionProceedingsoftheACMonWebConference2025.1219–1223.
[130] WenyuNing,ShaotaoShi,YuchenYin,ZixuanGuo,andJinrongXie.2025.Intent-awarepersonalizedsummarizationforeducationaltexts
withlargelanguagemodels.JournalofKingSaudUniversityComputerandInformationSciences37,9(2025),308.
[131] Inc.NotionLabs.2023.NotionAI—notion.com/product/ai.https://www.notion.com/product/ai.
[132] RodrigoNovelo,RodrigoRochaSilva,andJorgeBernardino.2025.ALiteratureReviewofPersonalizedLargeLanguageModelsforEmail
GenerationandAutomation.FutureInternet17,12(2025),536.
[133] FelixOcker,JörgDeigmöller,PavelSmirnov,andJulianEggert.2025. Agroundedmemorysystemforsmartpersonalassistants. arXiv
preprintarXiv:2505.06328(2025).
[134] OpenAI.2022.ChatGPT—chatgpt.com.https://chatgpt.com/.
[135] EgorPakhomov,ErikNijkamp,andCaimingXiong.2025.ConvomemBenchmark:WhyYourFirst150ConversationsDon’tNeedRAG.
arXivpreprintarXiv:2511.10523(2025).
[136] ZhuoshiPan,QianhuiWu,HuiqiangJiang,XufangLuo,HaoCheng,DongshengLi,YuqingYang,Chin-YewLin,HVickyZhao,LiliQiu,
etal.2025.Onmemoryconstructionandretrievalforpersonalizedconversationalagents.arXivpreprintarXiv:2502.05589(2025).
[137] KishorePapineni,SalimRoukos,ToddWard,andWei-JingZhu.2002.Bleu:amethodforautomaticevaluationofmachinetranslation.In
Proceedingsofthe40thannualmeetingoftheAssociationforComputationalLinguistics.311–318.
[138] ChanghuaPei,YiZhang,YongfengZhang,FeiSun,XiaoLin,HanxiaoSun,JianWu,PengJiang,JunfengGe,WenwuOu,etal.2019.
Personalizedre-rankingforrecommendation.InProceedingsofthe13thACMconferenceonrecommendersystems.3–11.
[139] QiyaoPeng,HongtaoLiu,HuaHuang,QingYang,andMinglaiShao.2025. Asurveyonllm-poweredagentsforrecommendersystems.
arXivpreprintarXiv:2502.10050(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 31
[140] MathisPink,QinyuanWu,VyAiVo,JavierTurek,JianingMu,AlexanderHuth,andMariyaToneva.2025.Position:EpisodicMemoryisthe
MissingPieceforLong-TermLLMAgents.arXivpreprintarXiv:2502.06975(2025).
[141] SriyashPoddar,YanmingWan,HamishIvison,AbhishekGupta,andNatashaJaques.2024. Personalizingreinforcementlearningfrom
humanfeedbackwithvariationalpreferencelearning.AdvancesinNeuralInformationProcessingSystems37(2024),52516–52544.
[142] Predis.ai.2023.Predis.ai—predis.ai.https://predis.ai/.
[143] ChengQian,EmreCanAcikgoz,HongruWang,XiusiChen,AvirupSil,DilekHakkani-Tur,GokhanTur,andHengJi.2025. SMART:
Self-awareagentfortooloverusemitigation.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.4604–4621.
[144] HongjinQian,ZhengLiu,PeitianZhang,KelongMao,DefuLian,ZhichengDou,andTiejunHuang.2025.Memorag:Boostinglongcontext
processingwithglobalmemory-enhancedretrievalaugmentation.InProceedingsoftheACMonWebConference2025.2366–2377.
[145] TianQin,FelixBai,Ting-YaoHu,RavitejaVemulapalli,HemaSwethaKoppula,ZhiyangXu,BowenJin,MertCemri,JiaruiLu,ZiruiWang,
etal.2025.COMPASS:AMulti-TurnBenchmarkforTool-MediatedPlanning&PreferenceOptimization.arXivpreprintarXiv:2510.07043
(2025).
[146] YilunQiu,TianhaoShi,XiaoyanZhao,FengbinZhu,YangZhang,andFuliFeng.2025. Latentinter-userdifferencemodelingforllm
personalization.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.10610–10628.
[147] YilunQiu,XiaoyanZhao,YangZhang,YimengBai,WenjieWang,HongCheng,FuliFeng,andTat-SengChua.2025. Measuringwhat
makesyouunique:Difference-awareusermodelingforenhancingllmpersonalization.InFindingsoftheAssociationforComputational
Linguistics:ACL2025.21258–21277.
[148] ChangleQu,SunhaoDai,XiaochiWei,HengyiCai,ShuaiqiangWang,DaweiYin,JunXu,andJi-RongWen.2025.Toollearningwithlarge
languagemodels:Asurvey.FrontiersofComputerScience19,8(2025),198343.
[149] StevenJigeQuanandSeojungLee.2025.EnhancingparticipatoryplanningwithChatGPT-assistedplanningsupportsystems:ahypothetical
casestudyinSeoul.InternationalJournalofUrbanSciences29,1(2025),89–122.
[150] PrestonRasmussen,PavloPaliychuk,TravisBeauvais,JackRyan,andDanielChalef.2025.Zep:atemporalknowledgegrapharchitecture
foragentmemory.arXivpreprintarXiv:2501.13956(2025).
[151] Replika.[n.d.].Replika—replika.com.https://replika.com/.
[152] AlirezaRezazadeh,ZichaoLi,WeiWei,andYujiaBao.2024.Fromisolatedconversationstohierarchicalschemas:Dynamictreememory
representationforllms.arXivpreprintarXiv:2410.14052(2024).
[153] StephenRobertson,HugoZaragoza,etal.2009.Theprobabilisticrelevanceframework:BM25andbeyond.FoundationsandTrends®in
InformationRetrieval3,4(2009),333–389.
[154] RanaSalama,JasonCai,MichelleYuan,AnnaCurrey,MonicaSunkara,YiZhang,andYassineBenajiba.2025.Meminsight:Autonomous
memoryaugmentationforllmagents.arXivpreprintarXiv:2503.21760(2025).
[155] AlirezaSalemi,ChengLi,MingyangZhang,QiaozhuMei,WeizeKong,TaoChen,ZhuowanLi,MichaelBendersky,andHamedZamani.
2025.Reasoning-EnhancedSelf-TrainingforLong-FormPersonalizedTextGeneration.arXivpreprintarXiv:2501.04167(2025).
[156] AlirezaSalemi,ShesheraMysore,MichaelBendersky,andHamedZamani.2024.Lamp:Whenlargelanguagemodelsmeetpersonalization.
InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).7370–7392.
[157] AlirezaSalemiandHamedZamani.2025.Lamp-qa:Abenchmarkforpersonalizedlong-formquestionanswering.InProceedingsofthe
2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.1139–1159.
[158] Salesforge.2023.SalesforgeAI—salesforge.ai.https://www.salesforge.ai/.
[159] RohanCharudattSalvi,ChiragChawla,DhruvJain,SwapnilPanigrahi,MdShadAkhtar,andShwetaYadav.2025.PERCS:Persona-Guided
ControllableBiomedicalSummarizationDataset.arXivpreprintarXiv:2512.03340(2025).
[160] ParthSarthi,SalmanAbdullah,AditiTuli,ShubhKhanna,AnnaGoldie,andChristopherDManning.2024.Raptor:Recursiveabstractive
processingfortree-organizedretrieval.InTheTwelfthInternationalConferenceonLearningRepresentations.
[161] KrishnaSayana,RaghavendraVasudeva,YuriVasilevski,KunSu,LiamHebert,JamesPine,HubertPham,AmbarishJash,andSukhdeep
Sodhi.2025.BeyondRetrieval:GeneratingNarrativesinConversationalRecommenderSystems.InCompanionProceedingsoftheACMon
WebConference2025.2411–2420.
[162] SamuelSchmidgall,YushengSu,ZeWang,XimengSun,JialianWu,XiaodongYu,JiangLiu,MichaelMoor,ZichengLiu,andEmadBarsoum.
2025.Agentlaboratory:Usingllmagentsasresearchassistants.FindingsoftheAssociationforComputationalLinguistics:EMNLP2025
(2025),5977–6043.
[163] SamuelSchmidgall,RojinZiaei,CarlHarris,EduardoReis,JeffreyJopling,andMichaelMoor.2024. AgentClinic:amultimodalagent
benchmarktoevaluateAIinsimulatedclinicalenvironments.arXivpreprintarXiv:2405.07960(2024).
[164] YuShang,PeijieLiu,YuweiYan,ZijingWu,LehengSheng,YuanqingYu,ChumengJiang,AnZhang,FengliXu,YuWang,etal.2025.
Agentrecbench:Benchmarkingllmagent-basedpersonalizedrecommendersystems.arXivpreprintarXiv:2505.19623(2025).
[165] ZijianShao,JiancanWu,WeijianChen,andXiangWang.2025. PersonalTravelSolver:APreference-DrivenLLM-SolverSystemfor
TravelPlanning.InProceedingsofthe63rdAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).
27622–27642.
[166] SahilSharma,PuneetMittal,MukeshKumar,andVivekBhardwaj.2025. Theroleoflargelanguagemodelsinpersonalizedlearning:a
systematicreviewofeducationalimpact.DiscoverSustainability6,1(2025),1–24.
[167] ZhuochengShen.2024.Llmwithtools:Asurvey.arXivpreprintarXiv:2409.18807(2024).
[168] IdanShenfeld,FelixFaltings,PulkitAgrawal,andAldoPacchiano.2025.Languagemodelpersonalizationviarewardfactorization.arXiv
preprintarXiv:2503.06358(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

32 • Y.Xuetal.
[169] TengShi,JunXu,XiaoZhang,XiaoxueZang,KaiZheng,YangSong,andHanLi.2025.Retrievalaugmentedgenerationwithcollaborative
filteringforpersonalizedtextgeneration.InProceedingsofthe48thInternationalACMSIGIRConferenceonResearchandDevelopment
inInformationRetrieval.1294–1304.
[170] WenqiShi,RanXu,YuchenZhuang,YueYu,JieyuZhang,HangWu,YuandaZhu,JoyceCHo,CarlYang,andMayDongmeiWang.2024.
Ehragent:Codeempowerslargelanguagemodelsforfew-shotcomplextabularreasoningonelectronichealthrecords.InProceedingsof
the2024ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.22315–22339.
[171] YunxiaoShi,HaoningShang,XingZi,WujiangXu,YueFeng,andMinXu.2025.AnsweringNarrative-DrivenRecommendationQueries
viaaRetrieve–RankParadigmandtheOCG-Agent.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguage
Processing.13192–13213.
[172] YunxiaoShi,WujiangXu,ZhangZeqi,XingZi,QiangWu,andMinXu.2025.PersonaX:Arecommendationagent-orientedusermodeling
frameworkforlongbehaviorsequence.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.5764–5787.
[173] DonghoonShin,GaryHsieh,andYoung-HoKim.2025.PlanFitting:PersonalizedExercisePlanningwithLargeLanguageModel-driven
ConversationalAgent.InProceedingsofthe7thACMConferenceonConversationalUserInterfaces.1–19.
[174] NoahShinn,FedericoCassano,AshwinGopinath,KarthikNarasimhan,andShunyuYao.2023. Reflexion:Languageagentswithverbal
reinforcementlearning.AdvancesinNeuralInformationProcessingSystems36(2023),8634–8652.
[175] AnikaitSingh,SherylHsu,KyleHsu,EricMitchell,StefanoErmon,TatsunoriHashimoto,ArchitSharma,andChelseaFinn.2025.Fspo:Few-
shotpreferenceoptimizationofsyntheticpreferencedatainllmselicitseffectivepersonalizationtorealusers.arXivpreprintarXiv:2502.19312
(2025).
[176] HarmanpreetSingh,NikhilVerma,YixiaoWang,ManasaBharadwaj,HomaFashandi,KevinFerreira,andChulLee.2024.Personallarge
languagemodelagents:Acasestudyontailoredtravelplanning.InProceedingsofthe2024ConferenceonEmpiricalMethodsinNatural
LanguageProcessing:IndustryTrack.486–514.
[177] YutongSong,JiangWu,WeijiaZhang,ChengzeShen,ShaofanYuan,WeitaoLu,JianWang,AmirRahmani,NikilDutt,andYuWang.2026.
CARD:Cluster-levelAdaptationwithReward-guidedDecodingforPersonalizedTextGeneration.arXivpreprintarXiv:2601.06352(2026).
[178] PaoloSorino,GiovanniMariaBiancofiore,DomenicoLofù,TommasoColafiglio,AngelaLombardi,FedelucioNarducci,andTommaso
DiNoia.2024.Ariel:Brain-computerinterfacesmeetlargelanguagemodelsforemotionalsupportconversation.InAdjunctProceedingsof
the32ndACMConferenceonUserModeling,AdaptationandPersonalization.601–609.
[179] JunhaoSu,YuanliangWan,JunweiYang,HengyuShi,TianyangHan,JunfengLuo,andYuruiQiu.2025.Failuremakestheagentstronger:
Enhancingaccuracythroughstructuredreflectionforreliabletoolinteractions.arXivpreprintarXiv:2509.18847(2025).
[180] ChenkaiSun,KeYang,RevanthGangiReddy,YiFung,HouPongChan,KevinSmall,ChengXiangZhai,andHengJi.2025. Persona-db:
Efficientlargelanguagemodelpersonalizationforresponsepredictionwithcollaborativedatarefinement.InProceedingsofthe31st
InternationalConferenceonComputationalLinguistics.281–296.
[181] HaotianSun,YuchenZhuang,LingkaiKong,BoDai,andChaoZhang.2023.Adaplanner:Adaptiveplanningfromfeedbackwithlanguage
models.Advancesinneuralinformationprocessingsystems36(2023),58202–58245.
[182] WeiweiSun,XuhuiZhou,WeihuaDu,XingyaoWang,SeanWelleck,GrahamNeubig,MaartenSap,andYimingYang.2025. Training
proactiveandpersonalizedllmagents.arXivpreprintarXiv:2511.02208(2025).
[183] MananSuri,PuneetMathur,NedimLipka,FranckDernoncourt,RyanARossi,andDineshManocha.2025.StructuredUncertaintyguided
ClarificationforLLMAgents.arXivpreprintarXiv:2511.08798(2025).
[184] TakehiroTakayanagi,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,andIadhOunis.2025. AregenerativeAIagentseffec-
tivepersonalizedfinancialadvisors?.InProceedingsofthe48thInternationalACMSIGIRConferenceonResearchandDevelopmentin
InformationRetrieval.286–295.
[185] TakehiroTakayanagi,MasahiroSuzuki,KiyoshiIzumi,JavierSanz-Cruzado,RichardMcCreadie,andIadhOunis.2025. FinPersona:An
LLM-DrivenConversationalAgentforPersonalizedFinancialAdvising.InEuropeanConferenceonInformationRetrieval.Springer,13–18.
[186] JuntaoTan,LiangweiYang,ZuxinLiu,ZhiweiLiu,RitheshRN,TulikaManojAwalgaonkar,JianguoZhang,WeiranYao,MingZhu,Shirley
Kokane,etal.2025.Personabench:Evaluatingaimodelsonunderstandingpersonalinformationthroughaccessing(synthetic)privateuser
data.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.878–893.
[187] ZhenTan,JunYan,IHsu,RujunHan,ZifengWang,LongTLe,YiwenSong,YanfeiChen,HamidPalangi,GeorgeLee,etal.2025.Inprospect
andretrospect:Reflectivememorymanagementforlong-termpersonalizeddialogueagents.arXivpreprintarXiv:2503.08026(2025).
[188] ZhaoxuanTan,ZixuanZhang,HaoyangWen,ZhengLi,RongzhiZhang,PeiChen,FengranMo,ZheyuanLiu,QingkaiZeng,QingyuYin,
etal.2025.InstantPersonalizedLargeLanguageModelAdaptationviaHypernetwork.arXivpreprintarXiv:2510.16282(2025).
[189] JiakaiTang,SunhaoDai,TengShi,JunXu,XuChen,WenChen,JianWu,andYuningJiang.2025.Thinkbeforerecommend:Unleashingthe
latentreasoningpowerforsequentialrecommendation.arXivpreprintarXiv:2503.22675(2025).
[190] MeilingTao,ChenghaoZhu,DongyiDing,TiannanWang,YuchenEleanorJiang,andWangchunshuZhou.2025. PersonaFeedback:A
Large-scaleHuman-annotatedBenchmarkForPersonalization.arXivpreprintarXiv:2506.12915(2025).
[191] AoTian,YunfengLu,XinxinFan,ChanghaoWang,LanzhiZhou,YeyaoZhang,andYanfangLiu.2025.Rgmem:Renormalizationgroup-based
memoryevolutionforlanguageagentuserprofile.arXivpreprintarXiv:2510.16392(2025).
[192] Khanh-TungTran,DungDao,Minh-DuongNguyen,Quoc-VietPham,BarryO’Sullivan,andHoangDNguyen.2025.Multi-agentcollaboration
mechanisms:Asurveyofllms.arXivpreprintarXiv:2501.06322(2025).
[193] IoannisTsaknakis,BingqingSong,ShuyuGan,DongyeopKang,AlfredoGarcia,GaowenLiu,CharlesFleming,andMingyiHong.2025.
DoLLMsRecognizeYourLatentPreferences?ABenchmarkforLatentInformationDiscoveryinPersonalizedInteraction.arXivpreprint
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 33
arXiv:2510.17132(2025).
[194] Yu-MinTseng,Yu-ChaoHuang,Teng-YunHsiao,Wei-LinChen,Chao-WeiHuang,YuMeng,andYun-NungChen.2024. Twotalesof
personainllms:Asurveyofrole-playingandpersonalization.arXivpreprintarXiv:2406.01171(2024).
[195] KentaroUedaandTakehiroTakayanagi.2025.PREFINE:PersonalizedStoryGenerationviaSimulatedUserCriticsandUser-SpecificRubric
Generation.arXivpreprintarXiv:2510.21721(2025).
[196] HarshVishwakarma,AnkushAgarwal,OjasPatil,ChaitanyaDevaguptapu,andMaheshChandran.2025.CanLLMsHelpYouatWork?A
SandboxforEvaluatingLLMAgentsinEnterpriseEnvironments.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNatural
LanguageProcessing.9178–9212.
[197] YanmingWan,JiaxingWu,MarwaAbdulhai,LiorShani,andNatashaJaques.2025. EnhancingPersonalizedMulti-TurnDialoguewith
CuriosityReward.arXivpreprintarXiv:2504.03206(2025).
[198] DanqingWang,KevinYang,HanlinZhu,XiaomengYang,AndrewCohen,LeiLi,andYuandongTian.2024.Learningpersonalizedalignment
forevaluatingopen-endedtextgeneration.InProceedingsofthe2024ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.
13274–13292.
[199] HongruWang,MindaHu,YangDeng,RuiWang,FeiMi,WeichaoWang,YashengWang,Wai-ChungKwan,IrwinKing,andKam-Fai
Wong.2023.Largelanguagemodelsassourceplannerforpersonalizedknowledge-groundeddialogues.InFindingsoftheAssociationfor
ComputationalLinguistics:EMNLP2023.9556–9569.
[200] HongruWang,WenyuHuang,YangDeng,RuiWang,ZezhongWang,YufeiWang,FeiMi,JeffZPan,andKam-FaiWong.2024.Unims-rag:
Aunifiedmulti-sourceretrieval-augmentedgenerationforpersonalizeddialoguesystems.arXivpreprintarXiv:2401.13256(2024).
[201] HanpengWangandZijiangYang.2025.AMulti-AgentApproachtoInvestorProfilingUsingLargeLanguageModels.In2025International
ConferenceonControl,AutomationandDiagnosis(ICCAD).IEEE,1–6.
[202] KuanWang,YadongLu,MichaelSantacroce,YeyunGong,ChaoZhang,andYelongShen.2023.Adaptingllmagentswithuniversalfeedback
incommunication.arXivpreprintarXiv:2310.01444(2023).
[203] KaiminWang,YuanzheShen,ChangzeLv,XiaoqingZheng,andXuanjingHuang.2025.TripTailor:AReal-WorldBenchmarkforPersonalized
TravelPlanning.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.AssociationforComputationalLinguistics,Vienna,
Austria,9705–9723.doi:10.18653/v1/2025.findings-acl.503
[204] LeiWang,ChenMa,XueyangFeng,ZeyuZhang,HaoYang,JingsenZhang,ZhiyuanChen,JiakaiTang,XuChen,YankaiLin,etal.2024.A
surveyonlargelanguagemodelbasedautonomousagents.FrontiersofComputerScience18,6(2024),186345.
[205] LeiWang,JingsenZhang,HaoYang,Zhi-YuanChen,JiakaiTang,ZeyuZhang,XuChen,YankaiLin,HaoSun,RuihuaSong,etal.2025.User
behaviorsimulationwithlargelanguagemodel-basedagents.ACMTransactionsonInformationSystems43,2(2025),1–37.
[206] ShuoxinWang,ChangLiu,GowenLoo,LifanZheng,KaiwenWei,XinyiZeng,JingyuanZhang,andYuTian.2026.Me-Agent:APersonalized
MobileAgentwithTwo-LevelUserHabitLearningforEnhancedInteraction.arXivpreprintarXiv:2601.20162(2026).
[207] TianzeWang,DongnanGui,YifanHu,ShuhangLin,andLinjunZhang.2025. Mpo:Anefficientpost-processingframeworkformixing
diversepreferencealignment.arXivpreprintarXiv:2502.18699(2025).
[208] WenxuanWang,ZizhanMa,ZhengWang,ChenghanWu,JiamingJi,WentingChen,XiangLi,andYixuanYuan.2025.Asurveyofllm-based
agentsinmedicine:Howfararewefrombaymax?arXivpreprintarXiv:2502.11211(2025).
[209] YuWangandXiChen.2025.Mirix:Multi-agentmemorysystemforllm-basedagents.arXivpreprintarXiv:2507.07957(2025).
[210] YuxinWang,YiranGuo,YiningZheng,ZhangyueYin,ShuoChen,JieYang,JiajunChen,YuanLi,XuanjingHuang,andXipengQiu.2025.
FamilyTool:AMulti-hopPersonalizedToolUseBenchmark.arXivpreprintarXiv:2504.06766(2025).
[211] YuWang,DmitryKrotov,YuanzheHu,YifanGao,WangchunshuZhou,JulianMcAuley,DanGutfreund,RogerioFeris,andZexueHe.2025.
M+:ExtendingMemoryLLMwithScalableLong-TermMemory.arXivpreprintarXiv:2502.00592(2025).
[212] YuWang,XinshuangLiu,XiusiChen,SeanO’Brien,JundaWu,andJulianMcAuley.2024.Self-updatablelargelanguagemodelsbyintegrating
contextintomodelparameters.arXivpreprintarXiv:2410.00487(2024).
[213] YuWang,RyuichiTakanobu,ZhiqiLiang,YuzhenMao,YuanzheHu,JulianMcAuley,andXiaojianWu.2025.Mem-{\alpha}:Learning
MemoryConstructionviaReinforcementLearning.arXivpreprintarXiv:2509.25911(2025).
[214] ZhefanWang,YuanqingYu,WendiZheng,WeizhiMa,andMinZhang.2024. Macrec:Amulti-agentcollaborationframeworkfor
recommendation.InProceedingsofthe47thInternationalACMSIGIRConferenceonResearchandDevelopmentinInformationRetrieval.
2760–2764.
[215] ZixiangWang,YinghaoZhu,HuiyaZhao,XiaochenZheng,DehaoSui,TianlongWang,WenTang,YashaWang,EwenHarrison,Chengwei
Pan,etal.2025.Colacare:Enhancingelectronichealthrecordmodelingthroughlargelanguagemodel-drivenmulti-agentcollaboration.In
ProceedingsoftheACMonWebConference2025.2250–2261.
[216] AzmineToushikWasi,WahidFaisal,andMstRafiaIslam.2025.Mina:AMultilingualLLM-PoweredLegalAssistantAgentforBangladesh
forEmpoweringAccesstoJustice.arXivpreprintarXiv:2511.08605(2025).
[217] HuiWei,ZihaoZhang,ShenghuaHe,TianXia,ShijiaPan,andFeiLiu.2025.Plangenllms:Amodernsurveyofllmplanningcapabilities.In
Proceedingsofthe63rdAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).19497–19521.
[218] LilianWeng.2023.LLM-poweredAutonomousAgents.lilianweng.github.io(Jun2023). https://lilianweng.github.io/posts/2023-06-23-agent/
[219] RebeccaWesthäußer,FrederikBerenz,WolfgangMinker,andSebastianZepf.2025.CAIM:DevelopmentandEvaluationofaCognitiveAI
MemoryFrameworkforLong-TermInteractionwithIntelligentAgents.arXivpreprintarXiv:2505.13044(2025).
[220] RebeccaWesthäußer,WolfgangMinker,andSebatianZepf.2025. EnablingPersonalizedLong-termInteractionsinLLM-basedAgents
throughPersistentMemoryandUserProfiles.arXivpreprintarXiv:2510.07925(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

34 • Y.Xuetal.
[221] BinWu,ZhengyanShi,HosseinARahmani,VarshaRamineni,andEmineYilmaz.2024. Understandingtheroleofuserprofileinthe
personalizationoflargelanguagemodels.arXivpreprintarXiv:2406.17803(2024).
[222] DiWu,HongweiWang,WenhaoYu,YuweiZhang,Kai-WeiChang,andDongYu.2025.LongMemEval:BenchmarkingChatAssistantson
Long-TermInteractiveMemory.InTheThirteenthInternationalConferenceonLearningRepresentations.
[223] JiaxingWu,LinNing,LuyangLiu,HarrisonLee,NeoWu,ChaoWang,SushantPrakash,ShawnO’Banion,BradleyGreen,andJunXie.
2025.Rlpf:Reinforcementlearningfrompredictionfeedbackforusersummarizationwithllms.InProceedingsoftheAAAIConferenceon
ArtificialIntelligence,Vol.39.25488–25496.
[224] QingyunWu,GaganBansal,JieyuZhang,YiranWu,BeibinLi,ErkangZhu,LiJiang,XiaoyunZhang,ShaokunZhang,JialeLiu,etal.2024.
Autogen:Enablingnext-genLLMapplicationsviamulti-agentconversations.InFirstConferenceonLanguageModeling.
[225] ShujinWu,MayFung,ChengQian,JeonghwanKim,DilekHakkani-Tur,andHengJi.2024.Aligningllmswithindividualpreferencesvia
interaction.arXivpreprintarXiv:2410.03642(2024).
[226] YaozuWu,JizhouGuo,DongyuanLi,HenryPengZou,Wei-ChiehHuang,YankaiChen,ZhenWang,WeizhiZhang,YangningLi,Meng
Zhang,etal.2025.Psg-agent:Personality-awaresafetyguardrailforllm-basedagents.arXivpreprintarXiv:2509.23614(2025).
[227] YaxiongWu,ShengLiang,ChenZhang,YichaoWang,YongyueZhang,HuifengGuo,RuimingTang,andYongLiu.2025. Fromhuman
memorytoaimemory:Asurveyonmemorymechanismsintheeraofllms.arXivpreprintarXiv:2504.15965(2025).
[228] YuweiWu,XuezheMa,andDiyiYang.2021. Personalizedresponsegenerationviagenerativesplitmemorynetwork.InProceedings
ofthe2021ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:HumanLanguageTechnologies.
1956–1970.
[229] YuchenWu,EdwardSun,KaijieZhu,JianxunLian,JoseHernandez-Orallo,AylinCaliskan,andJindongWang.2025.PersonalizedSafetyin
LLMs:ABenchmarkandAPlanning-BasedAgentApproach.arXivpreprintarXiv:2505.18882(2025).
[230] YaxiongWu,YongyueZhang,ShengLiang,andYongLiu.2025.Sgmem:Sentencegraphmemoryforlong-termconversationalagents.arXiv
preprintarXiv:2509.21212(2025).
[231] YunjiaXi,WeiwenLiu,JianghaoLin,BoChen,RuimingTang,WeinanZhang,andYongYu.2024.Memocrs:Memory-enhancedsequential
conversationalrecommendersystemswithlargelanguagemodels.InProceedingsofthe33rdACMInternationalConferenceonInformation
andKnowledgeManagement.2585–2595.
[232] YunjiaXi,WeiwenLiu,JiemingZhu,XilongZhao,XinyiDai,RuimingTang,WeinanZhang,RuiZhang,andYongYu.2022. Multi-
levelinteractionrerankingwithuserbehaviorhistory.InProceedingsofthe45thInternationalACMSIGIRConferenceonResearchand
DevelopmentinInformationRetrieval.1336–1346.
[233] DerongXu,YiWen,PengyueJia,YingyiZhang,YichaoWang,HuifengGuo,RuimingTang,XiangyuZhao,EnhongChen,TongXu,etal.
2025.Towardsmulti-granularitymemoryassociationandselectionforlong-termconversationalagents.arXivpreprintarXiv:2505.19549
(2025).
[234] ManjieXu,XinyiYang,WeiLiang,ChiZhang,andYixinZhu.2025. LearningtoPlanwithPersonalizedPreferences. arXivpreprint
arXiv:2502.00858(2025).
[235] QianchengXu,YongqiLi,HemingXia,FanLiu,MinYang,andWenjieLi.2025. Petoolllm:Towardspersonalizedtoollearninginlarge
languagemodels.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.21488–21503.
[236] SonglinXu,XinyuZhang,andLianhuiQin.2024.Eduagent:Generativestudentagentsinlearning.arXivpreprintarXiv:2404.07963(2024).
[237] WujiangXu,ZujieLiang,KaiMei,HangGao,JuntaoTan,andYongfengZhang.2025. A-mem:Agenticmemoryforllmagents. arXiv
preprintarXiv:2502.12110(2025).
[238] XinchaoXu,ZhibinGou,WenquanWu,Zheng-YuNiu,HuaWu,HaifengWang,andShihangWang.2022.Longtimenosee!open-domain
conversationwithlong-termpersonamemory.InFindingsoftheAssociationforComputationalLinguistics:ACL2022.2639–2650.
[239] YangyangXu,JinpengHu,ZhuoerZhao,ZhanglingDuan,XiaoSun,andXunYang.2025. MultiAgentESC:ALLM-basedMulti-Agent
CollaborationFrameworkforEmotionalSupportConversation.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNatural
LanguageProcessing.4665–4681.
[240] YiyanXu,JinghaoZhang,AlirezaSalemi,XintingHu,WenjieWang,FuliFeng,HamedZamani,XiangnanHe,andTat-SengChua.2025.
Personalizedgenerationinlargemodelera:Asurvey.arXivpreprintarXiv:2503.02614(2025).
[241] SikuanYan,XiufengYang,ZuchaoHuang,ErcongNie,ZifengDing,ZonggenLi,XiaowenMa,KristianKersting,JeffZPan,HinrichSchütze,
etal.2025.Memory-r1:Enhancinglargelanguagemodelagentstomanageandutilizememoriesviareinforcementlearning.arXivpreprint
arXiv:2508.19828(2025).
[242] YiboYan,ShenWang,JiahaoHuo,PhilipSYu,XumingHu,andQingsongWen.2025. Mathagent:Leveragingamixture-of-math-agent
frameworkforreal-worldmultimodalmathematicalerrordetection.InProceedingsofthe63rdAnnualMeetingoftheAssociationfor
ComputationalLinguistics(Volume6:IndustryTrack).69–82.
[243] HongyangYang,BoyuZhang,NengWang,ChengGuo,XiaoliZhang,LikunLin,JunlinWang,TianyuZhou,MaoGuan,RunjiaZhang,etal.
2024.Finrobot:Anopen-sourceaiagentplatformforfinancialapplicationsusinglargelanguagemodels.arXivpreprintarXiv:2405.14767
(2024).
[244] YandanYang,BaoxiongJia,ShujieZhang,andSiyuanHuang.2025. Sceneweaver:All-in-one3dscenesynthesiswithanextensibleand
self-reflectiveagent.arXivpreprintarXiv:2509.20414(2025).
[245] ChaerinYu,ChihunChoi,SunjaeLee,HyosuKim,StevenYKo,Young-BaeKo,andSangeunOh.2026.LeveragingLLMsforEfficientand
PersonalizedSmartHomeAutomation.arXivpreprintarXiv:2601.04680(2026).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.

TowardPersonalizedLLM-PoweredAgents:Foundations,Evaluation,andFutureDirections • 35
[246] ShuoYu,MingyueCheng,DaoyuWang,QiLiu,ZiruiLiu,ZeGuo,andXiaoyuTao.2025.MemWeaver:AHierarchicalMemoryfromTextual
InteractiveBehaviorsforPersonalizedGeneration.arXivpreprintarXiv:2510.07713(2025).
[247] RuifengYuan,ShichaoSun,YongqiLi,ZiliWang,ZiqiangCao,andWenjieLi.2025.PersonalizedLargeLanguageModelAssistantwith
EvolvingConditionalMemory.InProceedingsofthe31stInternationalConferenceonComputationalLinguistics.
[248] SaberZerhoudiandMichaelGranitzer.2024. Personarag:Enhancingretrieval-augmentedgenerationsystemswithuser-centricagents.
arXivpreprintarXiv:2407.09394(2024).
[249] CongZhang,XinDeikGoh,DexunLi,HaoZhang,andYongLiu.2025.Planningwithmulti-constraintsviacollaborativelanguageagents.
InProceedingsofthe31stInternationalConferenceonComputationalLinguistics.10054–10082.
[250] JunjieZhang,YupengHou,RuobingXie,WenqiSun,JulianMcAuley,WayneXinZhao,LeyuLin,andJi-RongWen.2024. Agentcf:
Collaborativelearningwithautonomouslanguageagentsforrecommendersystems.InProceedingsoftheACMWebConference2024.
3679–3689.
[251] JiayiZhang,JinyuXiang,ZhaoyangYu,FengweiTeng,XionghuiChen,JiaqiChen,MingchenZhuge,XinCheng,SiruiHong,JinlinWang,
etal.2024.Aflow:Automatingagenticworkflowgeneration.arXivpreprintarXiv:2410.10762(2024).
[252] KaiZhang,XinyuanZhang,EjazAhmed,HongdaJiang,CalebKumar,KaiSun,ZhaojiangLin,SanatSharma,ShereenOraby,AaronColak,
etal.2025.AssoMem:ScalableMemoryQAwithMulti-SignalAssociativeRetrieval.arXivpreprintarXiv:2510.10397(2025).
[253] LemeiZhang,PengLiu,MarcusHenriksboe,EvenLauvrak,JonAtleGulla,andHeriRamampiaro.2024.Personalsum:Auser-subjective
guidedpersonalizedsummarizationdatasetforlargelanguagemodels. AdvancesinNeuralInformationProcessingSystems37(2024),
99333–99346.
[254] WeizhiZhang,XinyangZhang,ChenweiZhang,LiangweiYang,JingboShang,ZhepeiWei,HenryPengZou,ZijieHuang,ZhengyangWang,
YifanGao,etal.2025.Personaagent:Whenlargelanguagemodelagentsmeetpersonalizationattesttime.arXivpreprintarXiv:2506.06254
(2025).
[255] XuanZhang,YangDeng,ZifengRen,SeeKiongNg,andTat-SengChua.2024.Ask-before-plan:Proactivelanguageagentsforreal-world
planning.InFindingsoftheAssociationforComputationalLinguistics:EMNLP2024.10836–10863.
[256] XinliangFrederickZhang,NickBeauchamp,andLuWang.2025. PRIME:LargeLanguageModelPersonalizationwithCognitiveDual-
MemoryandPersonalizedThoughtProcess.InProceedingsofthe2025ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.
33695–33724.
[257] YingyiZhang,PengyueJia,DerongXu,YiWen,XiannengLi,YichaoWang,WenlinZhang,XiaopengLi,WeinanGan,HuifengGuo,etal.
2025.PersonalizeBeforeRetrieve:LLM-basedPersonalizedQueryExpansionforUser-CentricRetrieval.arXivpreprintarXiv:2510.08935
(2025).
[258] YuZhang,ShutongQiao,JiaqiZhang,Tzu-HengLin,ChenGao,andYongLi.2025.Asurveyoflargelanguagemodelempoweredagentsfor
recommendationandsearch:Towardsnext-generationinformationretrieval.arXivpreprintarXiv:2503.05659(2025).
[259] ZhaoweiZhang,FengshuoBai,QizhiChen,ChengdongMa,MingzhiWang,HaoranSun,ZilongZheng,andYaodongYang.2025.Amulet:
RealignmentduringtesttimeforpersonalizedpreferenceadaptationofLLMs.arXivpreprintarXiv:2502.19148(2025).
[260] ZeyuZhang,QuanyuDai,XiaoheBo,ChenMa,RuiLi,XuChen,JiemingZhu,ZhenhuaDong,andJi-RongWen.2025.Asurveyonthe
memorymechanismoflargelanguagemodel-basedagents.ACMTransactionsonInformationSystems43,6(2025),1–47.
[261] ZhehaoZhang,RyanARossi,BranislavKveton,YijiaShao,DiyiYang,HamedZamani,FranckDernoncourt,JoeBarrow,TongYu,Sungchul
Kim,etal.2024.Personalizationoflargelanguagemodels:Asurvey.arXivpreprintarXiv:2411.00027(2024).
[262] SiyanZhao,MingyiHong,YangLiu,DevamanyuHazarika,andKaixiangLin.2025. Dollmsrecognizeyourpreferences?evaluating
personalizedpreferencefollowinginllms.arXivpreprintarXiv:2502.09597(2025).
[263] WeixiangZhao,XingyuSui,YulinHu,JiaheGuo,HaixiaoLiu,BiyeLi,YanyanZhao,BingQin,andTingLiu.2025. TeachingLanguage
ModelstoEvolvewithUsers:DynamicProfileModelingforPersonalizedAlignment.arXivpreprintarXiv:2505.15456(2025).
[264] XinkuiZhao,HaodeLi,YifanZhang,GuanjieCheng,andYueshenXu.2025.TRAIL:JointInferenceandRefinementofKnowledgeGraphs
withLargeLanguageModels.arXivpreprintarXiv:2508.04474(2025).
[265] ZhengZhao,ClaraVania,SubhradeepKayal,NailaKhan,ShayBCohen,andEmineYilmaz.2025.Personalens:Abenchmarkforpersonal-
izationevaluationinconversationalaiassistants.InFindingsoftheAssociationforComputationalLinguistics:ACL2025.18023–18055.
[266] ArmanZharmagambetov,ChuanGuo,IvanEvtimov,MayaPavlova,RuslanSalakhutdinov,andKamalikaChaudhuri.2025. Agentdam:
Privacyleakageevaluationforautonomouswebagents.arXivpreprintarXiv:2503.09780(2025).
[267] LianminZheng,Wei-LinChiang,YingSheng,SiyuanZhuang,ZhanghaoWu,YonghaoZhuang,ZiLin,ZhuohanLi,DachengLi,Eric
Xing,etal.2023.Judgingllm-as-a-judgewithmt-benchandchatbotarena.Advancesinneuralinformationprocessingsystems36(2023),
46595–46623.
[268] XiZheng,ZhuoyangLi,XinningGui,andYuhanLuo.2025.CustomizingEmotionalSupport:HowDoIndividualsConstructandInteract
WithLLM-PoweredChatbots.InProceedingsoftheExtendedAbstractsoftheCHIConferenceonHumanFactorsinComputingSystems.
[269] WanjunZhong,LianghongGuo,QiqiGao,HeYe,andYanlinWang.2024.Memorybank:Enhancinglargelanguagemodelswithlong-term
memory.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.38.19724–19731.
[270] FilippoZiliotto,JelinRaphaelAkkara,AlessandroDaniele,LambertoBallan,LucianoSerafini,andTommasoCampari.2025. Personal:
Towardsacomprehensivebenchmarkforpersonalizedembodiedagents.arXivpreprintarXiv:2509.19843(2025).
ACMComput.Surv.,Vol.1,No.1,Article.Publicationdate:March2026.