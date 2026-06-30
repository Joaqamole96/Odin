Situation Graph Prediction: Structured Perspective Inference for
User Modeling
JisungShin∗ DanielPlatnick∗
FlybitsLabs,CreativeAIHub FlybitsLabs,CreativeAIHub
UniversityofToronto TorontoMetropolitanUniversity
chris.shin@flybits.com daniel.platnick@flybits.com
MarjanAlirezaie HosseinRahnama
FlybitsLabs,CreativeAIHub FlybitsLabs,CreativeAIHub
TorontoMetropolitanUniversity TorontoMetropolitanUniversity
marjan.alirezaie@flybits.com MITMediaLab
rahnama@mit.edu
Abstract ThislimitationmotivatestheemergingparadigmofPerspective-
Perspective-AwareAI(PAi)requiresmodelingevolvinginternal AwareAI (PAi)[2],whichshiftsthefocusfromgenericpersonal-
states—goals,emotions,contexts—notmerelypreferences.Progress izationtowardmodelinghowanentityexperiencesandinterprets
islimitedbyadatabottleneck:digitalfootprintsareprivacy-sensitive situationsovertime.Ratherthanmodelingusersasstaticprefer-
and perspective states are rarely labeled. We propose Situation encevectorsoroverisolatedinteractions,PAirepresentsidentityas
GraphPrediction(SGP),ataskthatframesperspectivemodelingas alongitudinal,structuredtrajectoryshapedbylivedexperience,en-
aninverseinferenceproblem:reconstructingstructured,ontology- ablinguser-centricapplicationssuchasadaptiveeducation,health
alignedrepresentationsofperspectivefromobservablemultimodal support,explainabledecision-making,andbiasauditing.
artifacts.Toenablegroundingwithoutreallabels,weuseastructure- ProgressinPAiisconstrainedbyafundamentaldatabottleneck:
firstsyntheticgenerationstrategythatalignslatentlabelsandob- longitudinaldigitalfootprintsaresiloedandprivacy-sensitive,and
servabletracesbydesign.Asapilot,weconstructadatasetandrun thelatentperspectivevariablesunderlyingbehavior(goals,affect,
adiagnosticstudyusingretrieval-augmentedin-contextlearningas interpretation)arerarelylabeled.ConsideranAIthatrecognizes—
aproxyforsupervision.InourstudywithGPT-4o,weobserveagap fromvoicetremors,sparsereplies,andavoidancepatterns—thata
betweensurface-levelextractionandlatentperspectiveinference– userisspiralingtowardcrisiswhilebehavioralmetricsreportonly
indicatinglatent-stateinferenceisharderthansurfaceextraction “decreasedengagement.”Thisgapmotivatesourwork.
underourcontrolledsetting.ResultssuggestSGPisnon-trivialand WeadvancePAithroughthreecontributions:
provideevidenceforthestructure-firstdatasynthesisstrategy. (1) WeformalizeSituationGraphPrediction (SGP):astructured
inverseinferencetaskmappingobservableuserdataartifacts
toontology-alignedperspectiverepresentations.
CCSConcepts
(2) Weproposestructure-firstsyntheticgenerationasaprivacy-
•Human-centeredcomputing→Humancomputerinterac-
preservingapproachtolabeledperspectivedata.
tion(HCI);•Computingmethodologies→Knowledgerepre-
(3) Throughapilotstudy,weprovideevidencethatSGPisnon-
sentationandreasoning.
trivialforGPT-4oandthatlatentinferenceappearsharderthan
surfaceextractioninoursetting.
Keywords
Perspective-AwareAI,GraphPrediction,Long-termPersonaliza-
tion,UserModeling,KnowledgeGraphs,MultimodalLearning 2 RelatedWork
Ourworkbridgespersonalization,long-termidentitymodeling,
andstructuredmultimodalinference.
1 Introduction
Recentadvancesinfoundationmodelshaveshownthattrainingon FromPersonalizationtoPerspective-AwareAI. Classicaluser
large-scalecorporayieldsimpressivegeneral-purposereasoning modelingrepresentsusersasstaticprofilesorpreferencevectors,
andgenerationcapabilities.However,thesesystemsremainfunda- enablingsurface-leveladaptationbutnotreasoningaboutevolving
mentallyimpersonal:theyreasonabouttheworld,butnotfrom internalstates[9].Persona-conditioneddialogueimprovesspeaker
thestandpointofaspecificindividualororganization.Asaresult, consistencybuttreatsidentityaslightweighttext[10,19],while
currentAIsystemsstruggletoactastrustworthycollaboratorsin personalizedalignmentemphasizesbehavioraladaptationviapref-
domainswhereunderstandingevolvinggoals,values,emotions, erencesandcontrollability[7].Theseapproachesprimarilyopti-
andcontextisessential. mizeoutputtailoringandrarelymodelhowinternalstatesevolve
acrosssituations.Incontrast,Perspective-AwareAItargetsstruc-
turedlongitudinalrepresentations,framingidentityasatrajectory
†Preprint,underreview.
∗Theseauthorscontributedequallyandshareco-firstauthorship. ofsituation-levelstates(context,affect,goals)ratherthanisolated
6202
beF
01
]IA.sc[
1v91331.2062:viXra

preferences[2].Neurosymbolicusermentalmodelingsimilarlycon- Well-formednessisenforcedthroughtypedconstraints:each
structsontology-alignedidentitygraphsfrommultimodaltraces tripletsatisfies(𝑠,𝑝,𝑜) ∈T𝑡 ⇒(𝜅 ,𝜅 𝑜) ∈A(𝑝),whereA(𝑝)spec-
𝑠
[1,17]. ifiesvalid(subject-kind,object-kind)pairs.Additionalstructural
LongitudinalMemoryandIdentityGraphs.Long-termmem- constraintsenforceboundedgraphsizeandminimalcompleteness
| orysupportscoherenceininteractiveagents:GenerativeAgents |     |     |     |     | conditions. |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- |
storeexperiencesforplanning[12],butdonotenforceontology-
aligned,queryableperspectiverepresentations.PriorworkonPAi 3.2 ProblemFormulation
introducesChroniclesastemporallycoherentidentityknowledge
WeformalizeSGPasalatentvariableinferencetask.Atagiven
graphs[2],relyingontheuseofsituationgraphsasatomicunits.
|     |     |     |     |     | timesegment𝑡,let𝑍 | denotetheuser’struelatentcognitivestate |     |     |
| --- | --- | --- | --- | --- | ----------------- | --------------------------------------- | --- | --- |
𝑡
Identity-grounded generation is shown to reduce persona drift (encompassinginternalgoals,affect,andcontext).Because𝑍 is
𝑡
[14],andChronicle-basedsystemsfurtherdemonstratenarrative-
|     |     |     |     |     | abstractandunobservable,wedefinetheSituationGraph𝐺 |     |     | 𝑡 ∈G |
| --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | ---- |
groundedpersonalization[15].
asastructured,symbolicapproximationalignedwithourontology,
SituationUnderstandingandLatentMentalStates.Ourfor-
whereGdenotesthespaceofvalidgraphsundertheschema.
mulationrelatestonarrativeandcommonsenseinference.Narrative
Theuser’sstatemanifestsexternallythroughasetofobservable
eventchainscapturetypicaleventsequences[6],whileATOMIC digitalartifacts𝑋 (e.g.,logs,audio,images,socialmediaposts).
𝑡
andCOMETmodelevent-intent-reactionrelations[4,18].These Forcomputationaltractability,wemodelthegenerativeprocess
resourcesprovideusefulpriorsbutdonotofferinstance-levelsu-
|     |     |     |     |     | bytreatingthestructuredapproximation𝐺 |     | 𝑡   | asthelatentvariable |
| --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | ------------------- |
pervisiongroundedinaspecificuser’smultimodalfootprint.
governingartifactgeneration.Specifically,weassumeartifactsare
GroundedDynamicGraphPrediction.Scenegraphgenera-
|     |     |     |     |     | drawnfromaconditionaldistribution𝑋 |     | ∼𝑃(· | |𝐺 𝑡).Underthis |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | ---- | --------------- |
𝑡
tionextractsobject–relationstructurefromimages[13],butdoes formulation,𝑋 constitutesapartial,noisy,andunstructuredpro-
𝑡
notrecoversituationalstructurefrommultimodalartifacts.Tempo- jectionoftheuser’sunderlyingperspectivestructureencodedby
ralknowledgegraphcompletionmodelsevolvingrelationaldata
𝐺 𝑡 .
[5],butassumesaccesstostructuredinputsratherthaninferring
themfromrawtraces.StructuredgroundingapproachessuchasK-
3.3 TheInferenceTask
BERTandREALMmotivatetheuseofgraph-basedrepresentations
|                                           |     |     |     |     | Inareal-worldsetting,weonlyobserve𝑋 |     | .ThegoalofSGPisto |     |
| ----------------------------------------- | --- | --- | --- | --- | ----------------------------------- | --- | ----------------- | --- |
| forimprovingreasoningandfactuality[8,11]. |     |     |     |     |                                     |     | 𝑡                 |     |
invertthegenerativeprocesstorecovertheperspectivestructure𝐺 .
𝑡
Toenablelearningthisinversiondespitetheabsenceofnaturally
3 SituationGraphPrediction occurringlabels,werelyonasynthetic proxydataset.Let
D =
| InthissectionweformalizethetaskofSituationGraphPrediction |     |     |     |     | 𝑁            |                                  |     |              |
| --------------------------------------------------------- | --- | --- | --- | --- | ------------ | -------------------------------- | --- | ------------ |
|                                                           |     |     |     |     | {(𝑋 𝑖 ,𝐺 𝑖)} | denoteaproxydatasetofpairswhere𝐺 |     | 𝑖 isaground- |
𝑖 =1
(SGP),whichaimstorecoversituation-levelstructuredperspective truthSituationGraphand𝑋 isthecorrespondingsetofmultimodal
𝑖
representationsfromobservabledigitaltraces. digitalartifacts.Wedefinetheinferenceobjectiveas:
𝐺ˆ
|     |     |     |     |     |     | 𝑡 =argmax𝑃(𝐺 | |𝑋 𝑡 ;Θ), |     |
| --- | --- | --- | --- | --- | --- | ------------ | --------- | --- |
3.1 SituationGraphRepresentation
𝐺∈G
| Thestructuredrepresentation𝐺 |     | isgroundedintheDOLCEUl- |     |     |                                            |     |     |     |
| ---------------------------- | --- | ----------------------- | --- | --- | ------------------------------------------ | --- | --- | --- |
|                              |     | 𝑡                       |     |     | whereΘrepresentstheinferenceconfiguration. |     |     |     |
tralite(DUL)upperontology[3]anditsapplicationtoPAi,which Whilethisobjectivecanbeapproachedusingdifferentlearning
providesafoundationalvocabularyfordescribingsituations,par-
paradigms(e.g.,unsupervisedorsemi-supervisedlearning),inthis
ticipants,events,andtheirrelationships.Weinstantiateadomain-
workwefocusontwoprimaryregimes:
specificschematailoredforperspective-awareidentitymodeling,
|              |          |                     |                |         | 1) Supervised | Learning: | Θ = 𝜃 represents | trainable model |
| ------------ | -------- | ------------------- | -------------- | ------- | ------------- | --------- | ---------------- | --------------- |
| treating the | ontology | as a representation | of perspective | that is |               |           |                  |                 |
parameters,andtheinferencemodelisinstantiatedasafunction
s u ffi c i e n t f o r t a s k g r o u n d i n g . 𝑓 s u c h t h a t pr e d ic t io ns a r e g iv e n b y 𝐺 ˆ 𝑓 𝑋 ). T h e p a r am e t e rs
|           |                       |                         |               |                    | 𝜃   |     | 𝑖 = 𝜃 | ( 𝑖 |
| --------- | --------------------- | ----------------------- | ------------- | ------------------ | --- | --- | ----- | --- |
| R e p r e | s e n t a t i o n . A | S i t u a t i on G r ap | h 𝐺 = ( 𝑉 , R | ) i s e q u i va - |     |     |       |     |
𝑡 𝑡 𝑡 a re o p t i m i z e d b y m i n im iz i n g a ta s k -s p e c ifi c l o s s L ( 𝑓 𝜃 ( 𝑋 𝑖) , 𝐺 𝑖) o v e r
| le n tl y r e p | r e s e n t e d a s a s | e t o f s e m an ti c  | tr ip le ts T𝑡 = { (    | 𝑠 , 𝑝, 𝑜 ) : 𝑠 , 𝑜 ∈        |                     |     |     |     |
| --------------- | ----------------------- | ---------------------- | ----------------------- | --------------------------- | ------------------- | --- | --- | --- |
|                 |                         |                        |                         |                             | t h e d a t a s e t | D . |     |     |
| 𝑉 , 𝑝 ∈ R       | } , w h e r e 𝑠 is      | a s u b je c t n o d e | , 𝑝 i s a p r e d i c a | t e ( e d g e l a b e l ) , |                     |     |     |     |
𝑡 𝑡 2 ) I n - C o n t e x t I n f e r e n c e : Θ = {𝜃 , S } , w h e r e 𝜃 d e-
a n d 𝑜 i s a n o b j e c t n o d e . E a c h n o d e 𝑣 𝑉 is a t u p le 𝜅 , 𝜈 c o m p r is i n g f ro z e n 𝑡 f r o ze n
∈ 𝑡 ( ) n o t e s a fi x e d p r e - t r a i n e d f o u n d a t i o n m o d e l a n d S ⊂ D i s a d y -
𝑡
a k in d 𝜅 d ra w n f ro m a fi x e d ty p e v o c a b u la r y a n d a c a t e g o r i ca l n a m e na m i c a ll y r e tr i e v e d s u p p o r t s e t b a s e d o n s i m il a r i ty t o t h e i n p u t 𝑋 ,
𝑡
𝜈drawnfromatype-specificenumeration.Wesummarizethekey
whichisprovidedasin-contextdemonstrations.
designprinciplesbelow.
|     |     |     |     |     | Thisformulation | enablesprincipledevaluation |     | ofSGPusing |
| --- | --- | --- | --- | --- | --------------- | --------------------------- | --- | ---------- |
TaxonomyandStructuralConstraints.Theschemadefines
frozenmodels.Note,inourexperimentswefocusexclusivelyonthe
11nodekindsand14edgetypesorganizedintofoursemanticstrata:
in-contextinferenceregimetoprovideevidenceforthetaskdesign
participants,spatio-temporalstructure,contextualatmosphere,and
onthepilotdataset,whileleavingfullysupervisedtrainingtofuture
psychologicalstate.Crucially,theschemadistinguishessurfacefrom
large-scalesettings.
latentattributes.Surfacenodes(participants,locationtypes,times,
ambience)representobservablefacetsthatcanplausiblymanifest A critical challenge in PAi
|     |     |     |     |     | 3.3.1 Bridging | the Supervision | Gap. |     |
| --- | --- | --- | --- | --- | -------------- | --------------- | ---- | --- |
inartifacts,whilelatentpredicates(feels,evokes,has_valence, isthatreal-worlddigitalfootprintslackexplicitgroundtruthla-
conveys_val)connecttopsychologicalstates(Emotion,Valence) bels𝐺 ;usersdonotannotatetheirliveswithknowledgegraphs.
𝑡
encodingunobservableinternalperspective. Consequently,standardsupervisionisimpossibleonrealdata.
2

Toaddressthis,weadoptasyntheticsupervisionapproach.We 5 PilotDataConstruction
| useasyntheticgeneratortosamplealignedpairs(𝐺 |     |     |                          | ,𝑋 𝑡)fromthe |     |                                                             |     |
| -------------------------------------------- | --- | --- | ------------------------ | ------------ | --- | ----------------------------------------------------------- | --- |
|                                              |     |     |                          | 𝑡            |     | Totestthestructure-firstpipelineandinstantiatetheSGPtask,we |     |
| ontology’spriordistribution,where𝐺           |     |     | specifiesavalidsituation |              |     |                                                             |     |
|                                              |     |     | 𝑡                        |              |     | constructedafocusedpilotdatasetofsyntheticsituations.Data   |     |
structureand𝑋 𝑡 consistsofartifactsconditionallyrenderedtobe weregeneratedusingthepipelinedescribedinSection4andre-
consistentwiththatstructure.WedetailthisapproachinSection4. viewedbyahumanexperttoensureconsistencyandquality.The
|     |     |                           |     |     |     | datasetcontains𝑁 75situationinstancesacrossmultipledo- |     |
| --- | --- | ------------------------- | --- | --- | --- | ------------------------------------------------------ | --- |
|     |     | WedecomposeSGPintotwosub- |     |     |     | =                                                      |     |
3.3.2 SGPTaskDecomposition.
mains(e.g.,professional,personal,health-related)andmodalities
taskstoisolatedistinctmodelingchallenges:
(primarilytext,withasubsetincludingimagesandaudio),com-
Task1:StaticSituationGraphPrediction.Thestatictaskevaluates
prising225uniquesyntheticartifacts.Eachinstanceisapaired
multimodalgroundinginisolation,requiringthemodeltoinfer𝐺
|     |     |     |     |     | 𝑡   | (𝑋 ,𝐺 𝑡)sample,where𝐺 | isaground-truthSituationGraphand |
| --- | --- | --- | --- | --- | --- | --------------------- | -------------------------------- |
fromasingletimesegment’sartifactswithoutaccesstohistorica l 𝑡 𝑡
|            |               |                                         |     |     |     | 𝑋 thecorrespondingsetofartifacts. |     |
| ---------- | ------------- | --------------------------------------- | --- | --- | --- | --------------------------------- | --- |
| context:𝐺ˆ |               | 𝑡).Thissettingmeasuresamodel’sabilityto |     |     |     | 𝑡                                 |     |
|            | 𝑡 =𝑓 static(𝑋 |                                         |     |     |     |                                   |     |
Alldataarecenteredonafictionalpersona,EliseNavarro,a28-
integrateheterogeneoussignals(text,images,audio,logs)intoa
year-oldFilipinoprofessionallivinginTorontoandworkingasa
unifiedstructuredrepresentationconsistentwiththeontology.
SeniorMarketingAnalyst.Thedatasetspans75temporallyordered
Task2.TemporalSituationGraphPrediction.Thetemporaltask
eventsacross2021–2025(∼60months),coveringfourdomains:pro-
evaluateslongitudinalreasoning,includingcausalconsistencyand
fessionaldevelopments,personalandlifestylechanges,healthand
narrativecontinuity.Todisentanglereasoningcapabilityfromerror
physicalmilestones,andsocialandrelationalexperiences.Events
accumulation,weconsidertwoevaluationmodes:
weresampledviathestructuredgenerationpipelineandmanually
1)Single-StepTransition(OracleHistory).Themodelesti-
curatedintoacoherentlongitudinaltimelinetosupporttemporal
| mates𝐺ˆ | =argmax | 𝑃(𝐺 |𝑋 ,𝐻 ;Θ),leveragingtheground-truth |     |     |     |     |     |
| ------- | ------- | --------------------------------------- | --- | --- | --- | --- | --- |
𝑡 𝐺 𝑡 𝑡 consistency.Weuseasinglepersonatoensurelongitudinalcoher-
| history𝐻 | =(𝐺 | ,...,𝐺 𝑡−1)toconstrainthelatentstatetransi- |     |     |     |     |     |
| -------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
𝑡 𝑡−𝑘 ence;multi-personascalingfollowsthesamemethodologywithout
tion.Thismodeisolatesthemodel’sabilitytoinferstatetransitions
changingthetaskformulation.
underidealhistoricalcontext.
Whileintentionallysmall-scale,thisdatasetsufficestoexplore
2)Multi-StepTrajectory(Autoregressive).Themodelpre-
ourstructure-firstapproachanddemonstratethatSGPposesnon-
| dicts𝐺ˆ | =argmax | 𝑃(𝐺 |𝑋 ,𝐻ˆ ;Θ),where𝐻ˆ | =(𝐺ˆ | ,...,𝐺ˆ | 𝑡−1) |     |     |
| ------- | ------- | ---------------------- | ---- | ------- | ---- | --- | --- |
𝑡 𝐺 𝑡 𝑡 𝑡 𝑡−𝑘 trivialstructuralandinferentialchallengesfortheevaluatedmodel.
arethemodel’spriorpredictions(withcontextwindowsize𝑘).This
settingevaluatesrobustnesstoerroraccumulationandtheability
| tomaintaincoherentperspectiveovertime. |     |     |     |     |     | 6 DiagnosticStudy |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- |
Note,weevaluateTask1exclusively,asreliablesingle-timestep ToassessthedifficultyofSituationGraphPrediction,weconduct
groundingisaprerequisitebeforetemporalerroraccumulationcan
adiagnosticstudywithanLLM-basedpipeline.Weevaluateonly
bemeaningfullystudied.
Task1(StaticSGP),focusingongroundingmultimodalartifacts
intoasingle-stepstructuredgraph,anddeferlongitudinalmodeling
| 3.3.3 OutputRepresentationandEvaluation. |             |                                   | Because𝐺           | isisomor-   |             |                             |                                |
| ---------------------------------------- | ----------- | --------------------------------- | ------------------ | ----------- | ----------- | --------------------------- | ------------------------------ |
|                                          |             |                                   |                    | 𝑡           |             | (Task2).Giventhepilotsize(𝑁 | =75),thegoalisnotbenchmarking, |
| p h ic t o a                             | s e t o f s | e m an ti c t rip l e s T , t h e | m o d e l o u tp u | t is d e fi | n e d a s a |                             |                                |
𝑡 b u t s t u d y i n g ta s k fe a s ib il i ty a n d p r o b i n g t h e b et w e e n
p re di c te d s e t ˆ d r aw n f ro m t h e s p a c e o fo n t o lo g y -c o m p li a n t tr ip l e s. s em an ti c ga p
T 𝑡 su r f a c e p r o c es si n g a n d la t e nt -s t at e i n f e r en c e . W eu se a n 8 0/ 20 s tr a t i-
Forin-contextinference,weevaluateperformanceusingstandard
fiedsplitwith5-foldcross-validation(60retrieval,15test),ensuring
| set-basedmetrics(precision,recall,𝐹 |     |       | )betweenthepredictedset |     |     |                              |     |
| ----------------------------------- | --- | ----- | ----------------------- | --- | --- | ---------------------------- | --- |
|                                     |     |       | 1                       |     |     | eachinstanceisevaluatedonce. |     |
| T ˆ andgroundtruthT𝑡                |     | [16]. |                         |     |     |                              |     |
𝑡
|     |     |     |     |     |     | 6.1 MethodologyandExperimentProcedure |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------- | --- |
4 Structure-FirstSyntheticDataGeneration
|     |     |     |     |     |     | Ourpipelinemapsrawartifacts𝑋 | totripletsT ˆ in3stages: |
| --- | --- | --- | --- | --- | --- | ---------------------------- | ------------------------ |
To train and evaluate SGP models, we require paired examples 𝑡 𝑡
| (𝑋 ,𝐺 𝑡),where𝑋 |     | denotesmultimodaldigitalartifactsand𝐺 |     |     | the |     |     |
| --------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
| 𝑡               |     | 𝑡                                     |     |     | 𝑡   |     |     |
correspondingground-truthSituationGraph.Becausereal-world 1.ModalityDecomposition. Toaddresstheheterogeneityof
datalacksexplicit𝐺 labels,weadoptastructure-first synthetic digitalfootprints,wefirsttransformrawartifactsintoaunified
𝑡
generationpipeline.Ratherthanpromptingalanguagemodelto textualrepresentationusingmodality-specificencoders.Textis
processeddirectly(e.g.,socialmediaposts,chatlogs).Imagesare
freelysimulateusers,weexplicitlyinvertthegenerativeprocess.
First,wesampleavalidSituationGraph𝐺 fromthepredefined convertedintodescriptivetagsandscenesummariesviaaVision-
𝑡
ontology,encodingentities,relations,goals,andaffectforahypo- LanguageModel(VLM).Audiofilesareprocessedintoexacttran-
theticaluserinagivencontext(e.g.,JobInterview,FamilyConflict). scriptsandparalinguisticdescriptors(e.g.,voice_tremor,loudness).
Next,wetreatartifactgenerationasaconditionalrenderingtask.
AnLLMispromptedtoproduceobservableevidence𝑋 𝑡 (e.g.,emails, 2. Diagnostic Protocols. We evaluate the central reasoning
chatlogs,calendarentries)thatisconstrainedtobeconsistentwith agent(GPT-4o)undertwodistinctprotocolstoisolatetheimpact
thestructureencodedin𝐺 .Thisinversionalignssupervisionwith ofstructuredsupervision:
𝑡
evidencebyconstruction:artifactsaregroundedintheperspective (1)Zero-shotschemaalignment.Themodelreceivesdecom-
structureratherthanposthocannotated.Theresultingdataseten- posedartifactsandfullontologydefinitions(node/edgetaxonomies
ablescontrolled,privacy-preservingstudyofSGPwithoutrelying andconstraints)butnoin-contextexamples,measuringitsability
| onrealuserdata. |     |     |     |     |     | tomapsurfaceevidencetoabstractschema. |     |
| --------------- | --- | --- | --- | --- | --- | ------------------------------------- | --- |
3

Table1:SGPZero-Shotvs.RA-ICL suggeststhatretrieval-augmenteddemonstrationsprovidemoreac-
tionablesignalforextractingobservableelementsthanforinferring
Metric(Mean±SD) Zero-Shot RA-ICL Δ
internalstates.
Strict𝐹
1↑
0.016(±0.015) 0.163(±0.081) +0.147
EntropyNormalization.Thelatentvocabularyissubstantially
Soft𝐹
1↑
0.145(±0.072) 0.424(±0.097) +0.279
smaller(8uniquevaluesvs.106surfacevalues),whichshould,in
ViolationRate(PVR)
↓
0.061(±0.011) 0.065(±0.024) +0.005
principle,makelatentmatchingeasier.Tocontrolforthisconfound,
Latent𝐹 1 (soft) ↑ 0.145(±0.061) 0.351(±0.129) +0.206 weapplyentropynormalization,scalingeachcategory’s𝐹 byits
1
Surface𝐹
1
(soft)
↑
0.143(±0.095) 0.464(±0.191) +0.322
vocabularyentropyratio.Thenormalizedresultsrevealaconsistent
Gap(Δ
𝐿𝑆
) −0.003(±0.081) +0.113(±0.284) +0.116
andsubstantialgapinbothconditions:+0.14(zero-shot)and+0.53
Entropy-Normalized(adjustingforvocabularydiversity) (RA-ICL).Thissuggeststherawparityinzero-shotperformanceis
Latent𝐹
1
∗(norm.)
↑
0.090(±0.038) 0.218(±0.080) +0.128 misleading—whenaccountingfortaskdifficulty,latentinferenceis
Surface𝐹
1
∗(norm.)
↑
0.229(±0.152) 0.747(±0.308) +0.517 substantiallyharder.
Gap(norm.)(Δ∗ ) +0.139(±0.134) +0.528(±0.359) +0.389 GapAmplification.Normalizationincreasesthelatent-surface
𝐿𝑆
gapbyroughlyafactorof4underRA-ICL(0.14→0.53).Thissug-
RA-ICLsubstantiallyimproves𝐹1.Therawlatent–surfacegapΔLSisnear
geststhatstructureddemonstrationsprimarilyhelpmodelslearn
zeroinzero-shotbutpositiveunderRA-ICL,indicatingretrievalaidssurface
extractionmorethanlatentinference.Entropynormalization—adjustingfor whatsurfaceinformationtoextract,whilerecoveringlatentuser
vocabularydiversity(8latentobjectvaluesvs.106surfaceobjectvalues)— statesfromsurfaceevidenceremainschallenginginthissetup.
revealsapositivegapinbothconditions,indicatinglatentinferenceisharder
thansurfaceextractioninoursetting.Resultsaveragedover3runsper5folds.
7 Discussion,Limitations,andEthics
(2)Retrieval-augmentedin-contextlearning(RA-ICL).We SGPprovidesaconcretetaskforstructuredperspectiveinference,
retrievethetop-𝑘=3semanticallysimilar(𝑋,𝐺)pairsusingtext- butthisworkhaslimitations.Ourpilotdataset(𝑁 =75)provides
embedding-3-largeandprovidethemasdemonstrations.Theseserve evidenceforstructure-firstgenerationratherthansupportinglarge-
asproxysupervision,illustratinghowartifactpatterns(e.g.,acurt scaletraining,andscalingthepipelineisakeynextstep.While
emailandhigh-tempoaudio)maptographstructures(e.g.,Social- weevaluateSGPviaretrieval-augmentedin-contextinference,the
Context:Professional,Emotion:Stressed). formulationnaturallysupportsunsupervisedandsemi-supervised
paradigms(e.g.,treating𝐺 aslatentinaVAEframework).
𝑡
3. Graph Generation and Evaluation Metrics. The agent Thestructure-firstpipelineislimitedbytheexpressivityofthe
predictstripletsT ˆ
𝑡
byfusingmultimodaldescriptors,schemacon- ontology:phenomenanotrepresentedinourschema(e.g.,culturally
straints,andoptionaldemonstrations.Weassessfidelityusingfour specificnorms)cannotbecaptured.Further,syntheticartifactslack
metrics:(1)PredicateViolationRate(PVR)forontologicalcompli- somenoiseandirregularityofreal-worldtraces—oursettingoffers
ance(fractionofinvalidpredicates);(2)Strict𝐹 1 viaexactstring a lower bound on difficulty, and the gap may widen on noisier
matching;(3)Soft𝐹
1
usingembeddingsimilarity(text-embedding-3- real data. Our study only evaluates a single foundation model;
large),decomposedintolatent(Tlat,e.g.,Emotion,Valence)and broaderevaluationacrossmodelsandtrainingregimesisneeded
surface(Tsurf)subsetstoseparateextractionfromstateinference; todisentangletaskdifficultyfrommodel-specificbehavior.
and(4)thelatent–surfacegap Δ LS = 𝐹 1 surf−𝐹 1 lat (positivevalues SGPraisesethicalconsiderationsduetoitsfocusoninferring
indicatesurfaceextractionoutperformslatentinference,suggesting internalstates.Ourapproachprioritizesprivacybyrelyingexclu-
latentstatesarehardertorecover). sivelyonsyntheticdataandavoidingrealusertraces.Anyontology
Tocontrolforvaryingvocabularysparsity(8latentobjectvalues: forhumanperspectiveisinherentlynormativeandrequiresinter-
6emotions+2valencevs.106surfaceobjectvalues),wereportan disciplinaryscrutiny.Deployedsystemsmustensureusersretain
entropy-weighted𝐹
1
∗=𝐹 1·(𝐻 cat/𝐻 surf),where𝐻
cat
istheShannon controloverhowinferredstatesinformadaptation.
entropyofthetargetcategory’svaluedistributionandthesurface
entropy 𝐻 serves as the complexity baseline. All results use
surf
5-foldcross-validationwith𝑘=3retrievedexamplesperquery.
8 Conclusion
WeintroducedSituationGraphPrediction(SGP)asataskforre-
6.2 Results,Analysis,andTaskFeasibility coveringstructured,ontology-alignedperspectiverepresentations
Table1summarizesourdiagnosticresults.SGPposesanon-trivial frommultimodaldigitalartifacts.Toenableresearchunderpri-
challengeforGPT-4o,astrongfoundationmodel:whileRA-ICL vacyconstraints,weproposedastructure-firstsyntheticgeneration
substantiallyimprovesoverallperformance(Soft𝐹
1
:0.145→0.424), methodologyandinstantiateditwithapilotdatasetanddiagnostic
modelsmorereadilyextractexplicitsurfaceelements(e.g.,Par- evaluation.Inthispilot,wefindthemodelextractssurface-level
ticipants,Locations)thaninferlatentperspectivevariables(e.g., structuremorereadilythanlatentstatesaftercontrollingforvocab-
Emotion,Valence). ularydiversity.Theentropy-normalizedlatent–surfacegap(+0.53
RawPerformance.Inzero-shot,latentandsurface𝐹
1
areroughly underRA-ICL)suggeststhatmappingobservableartifactevidence
equivalent(0.145vs.0.143),yieldinganear-zerogap(−0.003).With topsychologicalstatesremainschallengingbeyondextractionin
RA-ICL,bothimprovesubstantially,butsurfaceextractiongains oursetting.Ourworkprovidesausefultaskframeworkforadvanc-
more(+0.322vs.+0.206),producingapositivegap(+0.113).This ingstructured,transparent,andperspective-awarepersonalization.
4

Acknowledgments [19] SaizhengZhang,EmilyDinan,JackUrbanek,ArthurSzlam,DouweKiela,and
JasonWeston.2018.PersonalizingDialogueAgents:Ihaveadog,doyouhave
The authors wish to express gratitude to the teams at Flybits,
petstoo?.InProceedingsofthe56thAnnualMeetingoftheAssociationforCompu-
TorontoMetropolitanUniversity,TheCreativeSchool,andMIT tationalLinguistics(Volume1:LongPapers),IrynaGurevychandYusukeMiyao
MediaLabfortheirvaluablesupport. (Eds.).AssociationforComputationalLinguistics,Melbourne,Australia,2204–
2213.doi:10.18653/v1/P18-1205
References
[1] MarjanAlirezaie,DanielPlatnick,HosseinRahnama,andAlexPentland.2024.
Perspective-AwareAI(PAi)forAugmentingCriticalDecisionMaking.TechRxiv
(2024).
[2] MarjanAlirezaie,HosseinRahnama,andAlexPentland.2024.StructuralLearning
intheDesignofPerspective-AwareAISystemsUsingKnowledgeGraphs.In
DigitalHumanWorkshopatAAAIConferenceonArtificialIntelligence.
[3] StefanoBorgo,RobertaFerrario,AldoGangemi,NicolaGuarino,ClaudioMasolo,
DanielePorello,EmilioM.Sanfilippo,andLaureVieu.2022.DOLCE:Adescriptive
ontologyforlinguisticandcognitiveengineering1. AppliedOntology17,1
(2022),45–69.arXiv:https://journals.sagepub.com/doi/pdf/10.3233/AO-210259
doi:10.3233/AO-210259
[4] AntoineBosselut,HannahRashkin,MaartenSap,ChaitanyaMalaviya,Asli
Celikyilmaz,andYejinChoi.2019. COMET:CommonsenseTransformersfor
AutomaticKnowledgeGraphConstruction.InProceedingsofthe57thAnnual
MeetingoftheAssociationforComputationalLinguistics,AnnaKorhonen,David
Traum,andLluísMàrquez(Eds.).AssociationforComputationalLinguistics,
Florence,Italy,4762–4779.doi:10.18653/v1/P19-1470
[5] BoruiCai,YongXiang,LongxiangGao,HeZhang,YunfengLi,andJianxinLi.
2023. TemporalKnowledgeGraphCompletion:ASurvey.InProceedingsof
theThirty-SecondInternationalJointConferenceonArtificialIntelligence(IJCAI-
2023).InternationalJointConferencesonArtificialIntelligenceOrganization,
6545–6553.doi:10.24963/ijcai.2023/734
[6] NathanaelChambersandDanJurafsky.2008.UnsupervisedLearningofNarrative
EventChains.InProceedingsofACL-08:HLT,JohannaD.Moore,SimoneTeufel,
JamesAllan,andSadaokiFurui(Eds.).AssociationforComputationalLinguistics,
Columbus,Ohio,789–797. https://aclanthology.org/P08-1090/
[7] JianGuan,JunfeiWu,Jia-NanLi,ChuanqiCheng,andWeiWu.2025.ASurvey
onPersonalizedAlignment—TheMissingPieceforLargeLanguageModels
inReal-WorldApplications.InFindingsoftheAssociationforComputational
Linguistics:ACL2025,WanxiangChe,JoyceNabende,EkaterinaShutova,and
MohammadTaherPilehvar(Eds.).AssociationforComputationalLinguistics,
Vienna,Austria,5313–5333. doi:10.18653/v1/2025.findings-acl.277
[8] Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasupat, and Ming-Wei
Chang.2020. REALM:Retrieval-AugmentedLanguageModelPre-Training.
arXiv:2002.08909[cs.CL] https://arxiv.org/abs/2002.08909
[9] AlfredKobsa.2001.GenericUserModelingSystems.UserModel.User-Adapted
Interact.11(062001). doi:10.1023/A:1011187500863
[10] JiweiLi,MichelGalley,ChrisBrockett,GeorgiosSpithourakis,JianfengGao,and
BillDolan.2016.APersona-BasedNeuralConversationModel.InProceedingsof
the54thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:
LongPapers),KatrinErkandNoahA.Smith(Eds.).AssociationforComputational
Linguistics,Berlin,Germany,994–1003.doi:10.18653/v1/P16-1094
[11] WeijieLiu,PengZhou,ZheZhao,ZhiruoWang,QiJu,HaotangDeng,andPing
Wang.2019.K-BERT:EnablingLanguageRepresentationwithKnowledgeGraph.
arXiv:1909.07606[cs.CL] https://arxiv.org/abs/1909.07606
[12] JoonSungPark,JosephC.O’Brien,CarrieJ.Cai,MeredithRingelMorris,Percy
Liang,andMichaelS.Bernstein.2023.GenerativeAgents:InteractiveSimulacra
ofHumanBehavior.arXiv:2304.03442[cs.HC] https://arxiv.org/abs/2304.03442
[13] DanielPlatnick,MarjanAlirezaie,andHosseinRahnama.2024. Enabling
Perspective-AwareAiwithContextualSceneGraphGeneration.Information15,
12(2024).doi:10.3390/info15120766
[14] DanielPlatnick,MohamedE.Bengueddache,MarjanAlirezaie,DavaJ.Newman,
Alex”Sandy”Pentland,andHosseinRahnama.2025.ID-RAG:IdentityRetrieval-
AugmentedGenerationforLong-HorizonPersonaCoherenceinGenerative
Agents.arXiv:2509.25299[cs.AI] https://arxiv.org/abs/2509.25299
[15] DanielPlatnick,MattiGruener,MarjanAlirezaie,KentLarson,DavaJ.New-
man,andHosseinRahnama.2025.Perspective-AwareAIinExtendedReality.
arXiv:2507.11479[cs.AI] https://arxiv.org/abs/2507.11479
[16] DavidM.W.Powers.2011.Evaluation:FromPrecision,RecallandF-Measure
toROC,Informedness,Markedness&Correlation.JournalofMachineLearning
Technologies2,1(2011),37–63.
[17] HosseinRahnama,MarjanAlirezaie,andAlexPentland.2021.ANeural-Symbolic
ApproachforUserMentalModeling:AStepTowardsBuildingExchangeable
Identities.InAAAI2021SpringSymposiumonCombiningMachineLearningand
KnowledgeEngineering(MAKE).
[18] MaartenSap,RonanLeBras,EmilyAllaway,ChandraBhagavatula,Nicholas
Lourie, Hannah Rashkin, Brendan Roof, Noah A. Smith, and Yejin Choi.
2019. ATOMIC:AnAtlasofMachineCommonsenseforIf-ThenReasoning.
arXiv:1811.00146[cs.CL] https://arxiv.org/abs/1811.00146
5