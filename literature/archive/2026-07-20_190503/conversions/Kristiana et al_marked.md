Received12December2025;revised23January2026;accepted24January2026.Dateofpublication28January2026;
dateofcurrentversion17February2026.ThereviewofthisarticlewasarrangedbyAssociateEditorFrancescoRundo.
DigitalObjectIdentifier10.1109/OJCS.2026.3658518
Validating AI-Driven Nudge Recommendations:
A/B Testing Two-Tower and Bandit Models in
Simulated Digital Banking Environment
IDHAKRISTIANA 1,HARJANTOPRABOWO1,FORDLUMBANGAOL 1 (SeniorMember,IEEE),
ANDNUNUNGNURULQOMARIYAH 2
1ComputerScienceDepartment,DoctorofComputerScience,BinaNusantaraUniversity,Jakarta11480,Indonesia
2ComputerScienceDepartment,SchoolofComputingandCreativeArts,BinaNusantaraUniversity,Jakarta11480,Indonesia
CORRESPONDINGAUTHOR:IDHAKRISTIANA(e-mail:idha.kristiana@binus.ac.id).
ABSTRACT Whileradicalmovestowardspersonalizationcharacterizeincreasinglyambitiousdigitalbank-
ing campaigns, recommender systems are typically based on either collaborative filtering or content-based
filtering, and they often prove ineffective due to a lack of behavioral awareness, as well as issues such as
highsparsity,coldstart,andhistoricalsignalsparsity.Toovercomethisgap,thisworkproposesanAI-based
Nudge Recommendation Model that incorporates a Two-Tower Network (TWN) for static personalization
along with a Multi-Armed Bandit (MAB) for real-time adaptive nudge optimization. We tested the model
usingacontrolledA/Bexperimentinamobilebankingsimulatorwithverifiedbankcustomers.Resultsshow
substantialbehavioralimprovementsinthetreatmentgroupusingtheAI-drivensystem,includinganincrease
inoverallpurchasebehavior(48.6%to62.07%)andamorethanfourfoldriseinrecommendation-following
rates (13.6% to 52.87%). Statistical testing confirms the significance of these differences (χ2 = 6.49, p <
0.0108). These findings validate the causal impact of personalized and adaptive nudging on user decision
behavior and provide a reproducible machine learning behavioral economics model with implications for
improvingdigitalbankingengagement.
INDEX TERMS A/B testing evaluation, AI in digital banking, multi-armed bandit (MAB), nudge recom-
mendationmodel,two-towernetwork(TWN).
I. INTRODUCTION havenotbeenabletofullyaccountforchangesinuserprefer-
The banking industry is progressively using artificial intelli- encesandbehaviorovertime[7].
gencetoimprovecustomerengagementandcampaignresults Theintegrationofbehavioralnudgetheorywithstaticand
inthedigitalage[1].Nudgingtechniqueisoneofthepromis- adaptiverecommendationmodelsisstillnotfullydeveloped,
ing approaches for the application of behavioral economics and this research suggests a combined model that uses a
thathasbeenwidelyimplementedinofflineenvironments[2], Multi-ArmedBanditalgorithmforfastadjustmentandaTwo-
[3].Nudgingreferstosubtlemodificationsinchoicearchitec- Tower Network for fixed personalization to fill the gap [8],
turethatsteeruserstowardbetterdecisionswithoutrestricting [9], [10]. The purpose of this research is to evaluate the pre-
their freedom of choice [4]. In digital banking, nudging is viously developed AI-based nudge recommendation model.
particularly relevant due to high perceived risk, low product Through A/B testing in a simulated mobile banking applica-
familiarity, and decision fatigue commonly observed among tion designed to mirror real banking features, allowing users
retailbankingcustomers[5].However,tooptimizethetiming to explore products and perform purchase-like actions, this
andrelevanceofthesenudges,AImodelsmustbeintelligent research aims to provide empirical evidence regarding the
andresponsive[6].Staticrecommendationsystemshavebeen model’sperformanceindeliveringrelevantandtimelynudges
the focus of previous research, the drawback being that they indigitalbankingcampaigns[11].
©2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/
404 VOLUME7,2026

While simultaneously improving personalization and behaviour such as responsible spending, saving and prod-
adaptability, the integrated model proposes a strategic ap- uct engagement, by making changes to the way in which
proach to maintain a trade-off between exploration and ex- options are framed or presented [2]. We implement nine
ploitation, a critical aspect of financial decision space [12]. established nudging dimensions: default options, personal-
Addressing cold-start problems and sparsity of user behav- ization, framing effect, social proof, loss aversion, gamifi-
ior, the Two-Tower Network ensures personalization at the cation/incentives, just-in-time nudging, and saliency, as well
baseline level through user and product profiles that capture defined by previous literature [7]. Despite nudging has been
historical information as well [13]. On the other hand, the studied in intersection with behavioral economics, nudging
Multi-Armed Bandit algorithm continually integrates real- implementedinthecontextofAI-basedrecommendationsys-
timefeedbackfromusers,sotherecommendationscanchange temsisstilllimited[27].Byintegratingthesenudgeprinciples
depending on the history of user actions over time and the into the AI system in ongoing personal real-time interac-
changingcontextualenvironments[14]. tion with the user with respect to the user’s behaviour and
|     |     |     |     |     |     | feedback,   | this gap   | is addressed. |     | As a           | result, | the | system |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | ------------- | --- | -------------- | ------- | --- | ------ |
|     |     |     |     |     |     | can provide | real-time, | context-aware |     | considerations |         | for | each   |
II. LITERATUREREVIEW
| A. STATICANDADAPTIVEMODELSOFAI-DRIVEN |     |     |     |     |     | user[28]. |           |              |     |               |     |           |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --------- | --------- | ------------ | --- | ------------- | --- | --------- | --- |
|                                       |     |     |     |     |     | Classical | financial | consultation |     | methodologies |     | generally |     |
RECOMMENDATIONSYSTEMS
Recent developments in AI-based recommendation systems apply universal rules, without considering complex psycho-
have made profound impacts on digital banking [7], [8]. logicalandbehavioral profilesofendusers[29].Byintegrat-
|                 |       |             |             |          |     | ing nudge | design | into the | AI recommendation |     |     | architecture, |     |
| --------------- | ----- | ----------- | ----------- | -------- | --- | --------- | ------ | -------- | ----------------- | --- | --- | ------------- | --- |
| The advancement | of AI | has enabled | large-scale | adoption |     |           |        |          |                   |     |     |               |     |
of personalization through recommender engines [6]. Most the system is now able to personalize what to recommend
|     |     |     |     |     |     | and when | and how | to present | a   | recommendation. |     | This | leads |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ---------- | --- | --------------- | --- | ---- | ----- |
traditionalsystemsareeithercollaborativefilteringorcontent-
based [7], [15]. Two-Tower Model (TWN) architecture is a to increased relevance and responsiveness especially when it
solution to learn deep discrete representations of users and comes to high-stake financial decisions where users usually
sufferfromcognitiveloadandperceptionofrisk[30].
| items in | a very powerful | way [15], | [16]. Typically, |     | these |     |     |     |     |     |     |     |     |
| -------- | --------------- | --------- | ---------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
embeddingsarecombinedviaadotproducttocomputesome
| relevance | score, allowing | for scalable | recommendations |     | as  |     |     |     |     |     |     |     |     |
| --------- | --------------- | ------------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C. LIMITATIONSOFEXISTINGAPPROACHESAND
user and item representations are independent [17], [18]. RESEARCHGAP
TWNsenableefficientstaticpersonalizationbased onusers’ Historically,recommendedsystemsinfinancialserviceshave
interestsandproducts’characteristicswhileavoidingsparsity become global unique identification numbers (GUID) on ei-
in users’ behaviors [15], [19]. As the static recommendation ther collaborative filtering (CF) or content-based filtering
| backbone | of the hybrid model, | TWNs | are used | to  | obtain |        |                  |     |           |       |     |           |     |
| -------- | -------------------- | ---- | -------- | --- | ------ | ------ | ---------------- | --- | --------- | ----- | --- | --------- | --- |
|          |                      |      |          |     |        | (CBF). | These approaches |     | have been | shown | to  | work well | in  |
contextually relevant product recommendations for every dense interaction history settings, such as e-commerce or
user[15]. entertainment platforms, but they fundamentally limit their
Although TWNs can learn a good ordering of items, it applicabilitytothebankingcontext[7],[15].Firstofall,the
cannot dynamically adapt. The Multi-Armed Bandit (MAB) cold-startproblem iscommon among bank userssince most
algorithmsfillthisgapbybalancingexplorationandexploita-
bankcustomersperformfinancialproducttransactionsrarely,
tion[20],[21],leveraginguserinteractionsforonlinelearning resulting in sparse behavioral signals that CF models need
anddynamiccalibrationofrecommendationsovertime[22]. to calculate similarity [8], [16]. First of all, the cold-start
Using this hybrid architecture, digital banking applications problemiscommonamongbankuserssince mostbankcus-
increasingly use behavioral economic principles based on tomersperformfinancialproducttransactionsrarely,resulting
nudge theory to layer a further degree of personalization on insparsebehavioralsignalsthatCFmodelsneedtocalculate
top of a recommendation system, using cognitive and emo- similarity [15], [19]. Third, and most critical for this study,
tionalnudgessuchassocialproof,defaults,lossaversion,and CF and CBF do not incorporate psychological or behavioral
framingeffects[2],[3],[23]. mechanisms, meaning they cannot model how nudges, such
|     |     |     |     |     |     | as framing, | personalization |     | cues, | loss aversion, |     | or salience, |     |
| --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | ----- | -------------- | --- | ------------ | --- |
B. NUDGETHEORYANDBEHAVIORALECONOMICS shape financial decisions [2], [3], [23]. These constraints re-
Behavioral economics studies the effects of psychological, duce their usefulness in environments where perceived risk,
cognitive, emotional, cultural and social factors on the de- trust,andcognitiveloadstronglyinfluenceuseractions[8].
cisions of individuals and institutions and how those deci- Beyondclassicalrecommenders,existingAI-basedperson-
sions vary from those implied by classical economic theory alization approaches in digital banking also show important
[24]. The discipline is based on the concept of nudging, as gaps. While machine learning has been widely applied to
conceived by Thaler and Sunstein [25]. It is all about in- credit scoring, fraud detection, and targeted marketing, very
direct changes in decision architecture that help people few studies explicitly integrate behavioral economics into
choosewhilemaintainingfreedomofchoice[26].Nudgesare algorithmic recommendation workflows [6], [31]. Current
increasinglyappliedindigitalbankingtoencouragedesirable models optimize engagement metrics, but rarely account for
| VOLUME7,2026 |     |     |     |     |     |     |     |     |     |     |     |     | 405 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

KRISTIANAETAL.:VALIDATINGAI-DRIVENNUDGERECOMMENDATIONS:A/BTESTINGTWO-TOWERANDBANDITMODELS
the distinct behavioral effects of different nudge mecha-
nisms [8], [32]. Likewise, adaptive learning methods such
as Multi-Armed Bandits have been employed in marketing
optimization,yetseldominsettingswhereeachactionrepre-
sentsabehavioralnudgetypedesignedtoinfluencefinancial
choices[33].
A further limitation in the literature is the lack of em-
pirical validation with verified bank customers. Previous
studies often rely on simulated settings, hypothetical vi-
gnettes,orrecordsfromahistoricallogratherthanobserving
actual decision-making among individuals who are real cus-
tomers of a financial institution [34]. Although there has
been progress in recommender systems, adaptive learning,
and digital nudging, to the best of our knowledge there
are no empirically validated nudge-aware AI recommenda-
tion model in banking that integrate these three components,
specifically: (1) static personalization, (2) real-time adaptive
learning, and (3) explicit behavioral design tested under a
controlled experimental setting with verified bank customers
[8].Previousstudieshavemainlybenchmarkedcollaborative
filtering, content-based filtering with behavioral design, and
contextual bandits without behavioral design. None of these
approachesjointlyintegratestaticpersonalizationwithadap-
tive nudge optimization. This study thus offers an empirical
hybridbaselinenevertestedpreviouslyinbankingcontexts.
III. RESEARCHMETHODS
A. DESIGNSCIENCERESEARCHMETHODOLOGY(DSR)
The research is primarily based on Design Science Research
(DSR) [35] (Fig. 1), which emphasizes the construction,
validation, and evaluation of a new artifact (in this case, an
AI Nudge recommendation model for digital banking cam-
paigns). This study aligns with primary DSR phases starting
from identifying the problem and defining the objectives to
thedesignanddevelopmentofthemodelbasedonsixbuild-
ing blocks obtained from literature and expert opinions. The
overall experimental design and evaluation flow, including
the control and treatment groups, model development, and FIGURE1. Designscienceresearchmethodology(DSRM).
outcomemeasurement,areillustratedinFig.2.Althoughthe
general research framework fits well with the DSR iterative
build-and-evaluate cycle, in this article we focus especially B. A/BTESTINGPROCEDURE
ontheevaluationphasebyperformingA/Btesting.TheA/B A controlled A/B testing procedure was implemented to
test is the main tool to empirically validate if the model evaluate the effectiveness of the AI-driven nudge model,
leads users to make better decisions. Primarily, this article consistent with best practices in experimental design [3].
addresses Research Question 3, concerning the performance Twoapplicationenvironmentsweredeployed:Appv1(Con-
oftheAI-basedNudgeRecommendationModelthatweapply trol), which used rule-based nudge assignment, and App v2
in a digital banking environment. The earlier stages, repre- (Treatment),whichincorporatedtheTwo-TowerNetworkand
sentedbyRQ1andRQ2,centeredondefiningthemodel’skey Multi-Armed Bandit for personalized and adaptive nudging.
components and developing the system, including a mobile Both environments followed the same simulation flow, prod-
bankingprototypedesignedtomirrorrealapplicationbehav- uctchoices,pagestructure,anddecisionpoints,ensuringthat
ior. Here, the intention is to move beyond design and theory theonlymanipulatedvariablewasthenudge-selectionmech-
and instead highlight how well the model works in influenc- anism[8].
ing user decisions. By focusing on A/B testing results, user Participants were segmented based on the version of the
interactions,andperformanceoutcomes,thisarticleshowsthe application they interacted with. Group A consisted of 214
model’srealimpactinapractical,measurableway. verified bank customers who used App v1 during the initial
406 VOLUME7,2026

wassmallerthanthecontrolsample,butthearchitecturewas
|     |     |     |     |     | trained    | exclusively  | on          | the larger | baseline        | dataset |               | (Group A), |
| --- | --- | --- | --- | --- | ---------- | ------------ | ----------- | ---------- | --------------- | ------- | ------------- | ---------- |
|     |     |     |     |     | and Group  | B was        | used        | only       | for evaluation. |         | Such          | separation |
|     |     |     |     |     | prevents   | information  |             | leakage    | and             | adheres | to sequential | A/B        |
|     |     |     |     |     | deployment | conventions. |             | This       | design          | ensures | that          | learning   |
|     |     |     |     |     | effects    | are not      | transferred |            | across          | cohorts | while         | preserving |
operationalrealisminstagedsystemdeployment.
|     |     |     |     |     | Due                 | to the | lack of | overlap                           | in  | time periods | from | which |
| --- | --- | --- | --- | --- | ------------------- | ------ | ------- | --------------------------------- | --- | ------------ | ---- | ----- |
|     |     |     |     |     | controlandtreatment |        |         | samplesweredrawn,thisevaluationis |     |              |      |       |
betterconsideredasequentialquasi-experimentthanaparallel
|     |     |     |     |     | random                                               | A/B test. | Therefore, |        | the             | research   | design         | does not    |
| --- | --- | --- | --- | --- | ---------------------------------------------------- | --------- | ---------- | ------ | --------------- | ---------- | -------------- | ----------- |
|     |     |     |     |     | allow us                                             | to make   | strong     | claims | about           | causality, |                | and differ- |
|     |     |     |     |     | ences measuredshouldbeinterpretedinlightoftimeperiod |           |            |        |                 |            |                |             |
|     |     |     |     |     | effects.                                             | However,  | the        | scale  | and consistency |            | of differences | in          |
|     |     |     |     |     | behavior                                             | indicate  | that       | time   | cannot          | be the     | sole driver    | of this     |
effect.
Inadditiontotherule-basedbaselineconsideredinGroup
|     |     |     |     |     | A and           | the AI-based   |          | system   | evaluated | in         | Group      | B, we in-   |
| --- | --- | --- | --- | --- | --------------- | -------------- | -------- | -------- | --------- | ---------- | ---------- | ----------- |
|     |     |     |     |     | troduce         | a TWN-only     |          | ablation | baseline. | In         | this       | regime, the |
|     |     |     |     |     | recommendations |                | are      | made     | by the    | Two-Tower  | Network    | it-         |
|     |     |     |     |     | self with       | no multi-armed |          |          | bandit    | adaptation | or         | behavioral  |
|     |     |     |     |     | nudging.        | This           | ablation | is done  | to        | extract    | the effect | of be-      |
FIGURE2. A/Btestingresearchflowdiagram. havioral nudging and adaptive bandit layer beyond static
personalization.Itthusconstitutesanintermediatebenchmark
|     |     |     |     |     | between | static | personalization |     | and | fully adaptive, |     | behavior- |
| --- | --- | --- | --- | --- | ------- | ------ | --------------- | --- | --- | --------------- | --- | --------- |
testingwindow.GroupBconsistedof174verifiedcustomers optimized recommendation.
| who used App | v2 during | the second testing | window. | No  |     |     |     |     |     |     |     |     |
| ------------ | --------- | ------------------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
participant appeared in both groups, ensuring independence C. DATACOLLECTIONANDSIMULATIONENVIRONMENT
and preventing cross-conditioning contamination [36], [37]. Data for this study was collected through a structured sim-
The system recorded important variables for each recom- ulation environment designed to capture user preferences,
mendation event, including the recommended item, assigned decision patterns, and behavioral responses during the fi-
nudge type, user choices, timestamp, and purchase results. nancial product selection journey. All participants answered
Theselogsallowedustocompareacrossthetwoexperimen- a 54-item questionnaire related to demographic characteris-
tal conditions directly for our main purchase outcomes and tics,financialbehavior,riskperception,spendingorientation,
recommendations, which were the main metrics used in the saving patterns, and digital engagement behavior. This type
evaluationofthetreatment[38]. of multi-dimensional survey instrument is typically used to
|         |                 |              |            |        | build psychographic |     |     | and behavioral |     | profiles | that | feed into |
| ------- | --------------- | ------------ | ---------- | ------ | ------------------- | --- | --- | -------------- | --- | -------- | ---- | --------- |
| The A/B | testing in this | study used a | sequential | quasi- |                     |     |     |                |     |          |      |           |
experimental design, which reflects the two-stage develop- personalized modeling [39]. This set of responses made up
ment and deployment cycle of the Nudge Simulation App. for the main features used while building the user embed-
App v1 (rule-based nudging) was released during the first dingwithinthe personalizationmodel.Participantsthenwent
data-collection phase. These were subsequently used to train through a simulation in either App v1 (Control) or App
andcalibratetheTwo-TowerNetworkandMulti-ArmedBan- v2 (Treatment), depending on their group assignment after
dit models. Once the AI model was built, a second version the survey. Using a common Supabase data pipeline, the
oftheapp,Appv2,wasimplementedtorecorddatafromthe app automatically recorded all events throughout the inter-
treatment group within a subsequent testing period. Partici- action,includingrecommended items,assignednudge types,
pants were therefore separated into two temporally distinct timestamps,andpurchaseoutcomes.Theselogsprovidedthe
cohorts, as the two application versions were released at behavioralgroundtruthusedforevaluatingbaselinedecision
different times. To ensure all experimental conditions were patternsinGroupAandfortrainingandvalidatingtheadap-
independent, App v1 users were removed from the users tivenudgemodeldeployedinGroupB.
| available to | include in the App | v2 dataset. | This ensured | that |     |     |     |     |     |     |     |     |
| ------------ | ------------------ | ----------- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
no participant was a member of both groups. By separating D. NUDGEMECHANISMS
users into Group A and Group B, these represent mutually From the systematic literature review conducted in this re-
exclusiveuserpopulationsthatwereexposedtotwodifferent search developed in accordance with the systematic review
versions of the simulation environment, in accordance with ofmethods[15],whichsynthesized100empiricalstudies on
best practices in quasi-experimental evaluation of sequential digital nudging, behavioral economics, and financial deci-
deployments of a system. Our treatment sample (Group B) sionsupportsystems,thewiderliteraturehighlightsnumerous
| VOLUME7,2026 |     |     |     |     |     |     |     |     |     |     |     | 407 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

KRISTIANAETAL.:VALIDATINGAI-DRIVENNUDGERECOMMENDATIONS:A/BTESTINGTWO-TOWERANDBANDITMODELS
| nudging | strategies | that     | could  | impact | user                 | choice. | Framing |     |     |     |     |     |
| ------- | ---------- | -------- | ------ | ------ | -------------------- | ------- | ------- | --- | --- | --- | --- | --- |
| nudges  | influence  | decision | making |        | byframinginformation |         |         | in  |     |     |     |     |
termsoffeaturesofachoice,andpersonalizationcuesadjust
messagesbasedoncharacteristicsofusertomakeitrelevant.
| By framing   | a    | loss instead | of         | a gain, | loss    | aversion | compels   |     |     |     |     |     |
| ------------ | ---- | ------------ | ---------- | ------- | ------- | -------- | --------- | --- | --- | --- | --- | --- |
| people to    | act, | while        | incentives | give    | people  | either   | money     | or  |     |     |     |     |
| non-monetary |      | rewards      | to push    | them    | towards |          | desirable | be- |     |     |     |     |
haviours.Socialproofusesinformationonhowpeersbehave
toinformindividualdecisions,andsaliencyenhancementin-
| creases        | visibility | of         | key information |        | to  | users. | Gamification |     |     |     |     |     |
| -------------- | ---------- | ---------- | --------------- | ------ | --- | ------ | ------------ | --- | --- | --- | --- | --- |
| brings similar |            | activities | from            | gaming | to  | boost  | engagement,  |     |     |     |     |     |
defaultoptionssimplifydecision-makingbypre-selectingan
optimaloption,andjust-in-timenudgesareinterventionsde-
liverednowofdecision-making.
Nevertheless,thisarticletargetsninemechanismsthathave
beenconsistentlyreportedacrossdigitalinterventionsandthat
| have shown | large | effect | sizes | on  | behavior | in  | the financial |     |     |     |     |     |
| ---------- | ----- | ------ | ----- | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- |
domain:personalization,defaultoption,framing,socialproof,
| loss aversion, |      | incentives, | gamification, |           | just-in-time    |     | nudging, |      |     |     |     |     |
| -------------- | ---- | ----------- | ------------- | --------- | --------------- | --- | -------- | ---- | --- | --- | --- | --- |
| and saliency   | [3], | [7],        | [40]. These   |           | nine mechanisms |     | were     | se-  |     |     |     |     |
| lected because |      | they appear |               | with high | frequency       |     | in the   | SLR, |     |     |     |     |
aredirectlyrelevanttosavings,investing,insurance,andrisk-
relateddecisions,andcanbeoperationalizedasmessage-level
| cues suitable |              | for integration |          | into    | the model. | The          | mapping |        |     |     |     |     |
| ------------- | ------------ | --------------- | -------- | ------- | ---------- | ------------ | ------- | ------ | --- | --- | --- | --- |
| of nudges     | to financial |                 | products | follows |            | a structured |         | coding |     |     |     |     |
derivedfromtheSLRtaxonomy[15],inwhicheachproduct
| may be | associated | with | multiple |     | nudges | depending |     | on its |                                                              |     |     |     |
| ------ | ---------- | ---- | -------- | --- | ------ | --------- | --- | ------ | ------------------------------------------------------------ | --- | --- | --- |
|        |            |      |          |     |        |           |     |        | FIGURE3. Integratedarchitectureofthenudgerecommendationmodel |     |     |     |
attributes,behavioraldrivers,anddecisionpatternsdescribed
(TWN+MAB).
| in prior   | literature. | Savings |         | products, | for            | instance, | are        | often |     |     |     |     |
| ---------- | ----------- | ------- | ------- | --------- | -------------- | --------- | ---------- | ----- | --- | --- | --- | --- |
| consistent | with        | default | options | and       | loss aversion, |           | investment |       |     |     |     |     |
products with framing and social proof, and insurance prod- environment deployment. We set binary cross-entropy as a
| ucts with | loss | aversion | and | incentives | [40]. | These | mapped |     |               |          |                 |                |
| --------- | ---- | -------- | --- | ---------- | ----- | ----- | ------ | --- | ------------- | -------- | --------------- | -------------- |
|           |      |          |     |            |       |       |        |     | loss function | and Adam | as an optimizer | and used early |
nudges subsequently define the action space of the Multi- stopping to avoid overfitting. Because this study focuses on
Armed Bandit, while the Two-Tower Network provides the decisionbehaviorratherthandeepmodeloptimization,archi-
relevancescoresusedtopersonalizewhichnudgemechanism tectural details are intentionally kept concise while ensuring
| ismostappropriateforeachuserateachmoment. |     |     |     |     |     |     |     |     | reproducibility. |                 |        |                  |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --------------- | ------ | ---------------- |
|                                           |     |     |     |     |     |     |     |     | The relevance    | score generated | by the | TWN is passed to |
E. MODELARCHITECTUREANDTRAINING the Multi-Armed Bandit, which determines the most appro-
The Nudge Recommendation Model has two main com- priate behavioral nudge to display at each recommendation
ponents: a Two-Tower Network (TWN) to capture static event. Each bandit chooses the best nudge with respect to
personalizationandaMulti-ArmedBandit(MAB)todynam- its known reward while still exploring alternative nudges in
icallyselectandadaptnudgestousersinreal-time.TheTWN order to achieve optimal behavior, consistent with adaptive
consists of a User Tower, which transforms demographic at- learning and online decision optimization models [41]. The
tributes, behavioral indicators, and questionnaire responses chosen nudge mechanism, then, constitutes the last output
into a latent user embedding, and a Product Tower, which of the system based on (i) personalized signals from the
encodes product attributes into a corresponding item embed- long-term profile of the user and (ii) recent feedback from
ding. Both embeddings are projected into a shared vector the behavioral signals [42]. A hybrid design was chosen,
space, and a dot-product similarity generates a personalized combining static personalization (through the TWN) with
relevance score for each user–product pair, following stan- adaptivebehaviorallearning(throughtheMAB).Fig.3shows
dard dual-encoder practices in large-scale recommendation theoverallarchitectureanddataflow,illustratingtheembed-
systems[15],[16].Thisscoreisnotshowntotheuserdirectly; ding generation, bandit-based decision making, and nudge
| instead,itfunctionsasapriorsignalthatinformsthebandit’s |     |     |     |     |     |     |     |     | deployment. |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |
decision-makingprocess[8]. We also present a formalized workflow of the hybrid
TWN was trained in preference labels derived from base- model to improve the clarity and reproducibility of its pro-
line interactions in Group A, allowing the model to learn posed architecture. Using the Two-Tower Network to gen-
stable representation of user preference prior to treatment erate user and product embeddings, relevance scores, and
| 408 |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

Algorithm1:Two-TowerNetworkTrainingPipeline. TABLE1. Two–TowerNetworkConfigurationParameters
Input:UserdatasetU,ProductdatasetP,Interaction
datasetI
Output:Userembeddingfunctionf(u),Product
embeddingfunctiong(p),Relevancescores(u,p)
| 1.LoadU,PandI,and |     |     | buildunifiedinteraction |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
datasetD
2.Datasetpreprocessing→Missingvalues+
| Categorical |     | attributeencoding |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3.PerformPCAonUser&ProductNumerical
| Features | toGetCompactEmbeddings. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4.CombinePCAfeatureswithDtoConstructmodel
inputs(X_user,X_product,y)
5.Addressdataimbalanceandquality:
a.Imputemissingvalues
b.Applyoversampling(e.g.,SMOTE)
c.Calculateclassweightsfortraining
6.Splitdatasetsintotrainingandtestingpartitions
7.DefineTwo–Towerarchitecture:
a.Usertower→userembeddingf(u)
b.Producttower→productembeddingg(p)
c.Concatenateembeddingsandcomputerelevance
scores(u,p)
| 8.Trainmodelusingweightedlossand |     |     |     |     | testset |     |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
evaluation.
9.Generatepredictedrelevancescoresfordownstream
integrationwithbanditpolicy layer used to seed the recommendation process. TWN was
stationaryduringdeployment,whiletheMulti-ArmedBandit
EndAlgorithm
adaptedonlinebaseduponuserfeedback.
F. ACTIONSPACEANDREWARDFORMULATION
| adaptive           | nudge          | selection     | by incorporating       |          | relevance     |              | scores |              |                  |       |             |           |                 |           |
| ------------------ | -------------- | ------------- | ---------------------- | -------- | ------------- | ------------ | ------ | ------------ | ---------------- | ----- | ----------- | --------- | --------------- | --------- |
|                    |                |               |                        |          |               |              |        | Our system   | considers        | each  | financial   | product   | as an           | indepen-  |
| in the Multi-Armed |                | Bandit.       | This                   | stepwise | demonstration |              | de-    |              |                  |       |             |           |                 |           |
|                    |                |               |                        |          |               |              |        | dent arm     | in a Multi-Armed |       | Bandit      | (MAB).    | The             | Two-Tower |
| scribes the        | basic          | functionality |                        | of the   | system        | and explains |        |              |                  |       |             |           |                 |           |
|                    |                |               |                        |          |               |              |        | Network      | (TWN) generates  |       | an initial  | relevance | score           | for all   |
| the process        | of integrating |               | static personalization |          |               | and dynamic  |        |              |                  |       |             |           |                 |           |
|                    |                |               |                        |          |               |              |        | user–product | pairs,           | which | constitutes | the       | prior estimates | for       |
learningatthetimeofdeployment.
|     |     |     |     |     |     |     |     | the bandit. | The bandit | produces | a   | ranked | list of products | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | -------- | --- | ------ | ---------------- | --- |
The static personalization engine is TWN output, where ε-greedy
|           |           |            |        |                   |      |          |     | each recommendation |            | round | following |     | an     | policy.     |
| --------- | --------- | ---------- | ------ | ----------------- | ---- | -------- | --- | ------------------- | ---------- | ----- | --------- | --- | ------ | ----------- |
| predicted | relevance | scores     | for    | each user–product |      | pair     | are |                     |            |       |           |     |        |             |
|           |           |            |        |                   |      |          |     | For illustrative    | simulation |       | purposes, | the | reward | signal used |
| generated | from      | TWN. These | scores | are               | then | provided | to  |                     |            |       |           |     |        |             |
toupdatethebanditpolicyismodeledasstochasticfeedback
| the multi-armed |       | bandit     | as prior | utilities | for    | exploration– |     |         |                 |     |              |     |          |            |
| --------------- | ----- | ---------- | -------- | --------- | ------ | ------------ | --- | ------- | --------------- | --- | ------------ | --- | -------- | ---------- |
|                 |       |            |          |           |        |              |     | sampled | from a Gaussian |     | distribution |     | centered | around the |
| exploitation.   | Table | 1 provides | a        | summary   | of the | operational  |     |         |                 |     |              |     |          |            |
expectedutilityoftheselectedproduct.
parametersfortraininganddeployingTWN.
ThevalueestimateQ(a)foreachproductaisupdatedusing
| The selected |     | architecture | (128–64–128) |     | is  | aligned | with |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | ------------ | --- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
anincrementalstochasticrule:
| standard | dual-encoder | architecture |     | in recommender |     | systems. |     |     |     |     |     |     |     |     |
| -------- | ------------ | ------------ | --- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
The period of 20 epochs for training was chosen in an em- =Q (a)+ −Q
|     |     |     |     |     |     |     |     | Q t+1 | (a) |     | (R  |     | (a)) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ---- | --- |
pirical manner from the graphs of validation loss, which t N (a) t t
t
suggested that training settled quickly. Dimensionality re- (cid:2)
|         |         |         |        |         |                 |     |     |     |              |     | (a), | with | probability1−ε |     |
| ------- | ------- | ------- | ------ | ------- | --------------- | --- | --- | --- | ------------ | --- | ---- | ---- | -------------- | --- |
|         |         |         |        |         |                 |     | >   |     | = argmax     | a Q | t    |      |                |     |
| duction | through | PCA was | set at | a level | that maintained |     |     |     | a            |     |      |      |                |     |
|         |         |         |        |         |                 |     |     |     | t randomarm, |     |      | with | probabilityε   |     |
95%totalvariance.Classimbalanceledtotheapplicationof
=μ∗−μ
| SMOTE          | oversampling | in        | parallel | to balanced | class    | weights. |     | Regret |     |     |     |     |     |     |
| -------------- | ------------ | --------- | -------- | ----------- | -------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- |
|                |              |           |          |             |          |          |     |        | t   | at  |     |     |     |     |
| In this study, | the          | Two-Tower | Network  |             | has been | built    | and |        |     |     |     |     |     |     |
developed from scratch and trained from scratch. The user While the Gaussian reward formulation supports stable
and item towers were initialized with no pretrained weights simulation and regret analysis, the effectiveness of the pro-
andweretrainedofflineforeachuserbypassingtheentirebe- posed system is evaluated using real interaction outcomes,
havioralandprofiledatasetrecordedduringthestudyperiod. including recommendation-following behavior and purchase
These relevance scores constitute the static personalization events, as reported in the experimental results. Through this
| VOLUME7,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 409 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

KRISTIANAETAL.:VALIDATINGAI-DRIVENNUDGERECOMMENDATIONS:A/BTESTINGTWO-TOWERANDBANDITMODELS
|     |     |     |     |     | Network | for personalized |     | product | scoring | and | the Multi- |
| --- | --- | --- | --- | --- | ------- | ---------------- | --- | ------- | ------- | --- | ---------- |
Algorithm2:AdaptiveNudgeSelectionviaMulti-Armed
Bandit(IllustrativeSimulation). ArmedBanditforadaptivenudgeselection[44].Thisdesign
|     |     |     |     |     | ensured | that differences |     | were | attributable | to  | the AI-driven |
| --- | --- | --- | --- | --- | ------- | ---------------- | --- | ---- | ------------ | --- | ------------- |
Therewardsignalinthisalgorithmdoesnotrepresent
| actualuserfeedbackbutisanillustrative |     |     |     |     | intervention[22]. |          |     |        |            |           |           |
| ------------------------------------- | --- | --- | --- | --- | ----------------- | -------- | --- | ------ | ---------- | --------- | --------- |
|                                       |     |     |     |     | During            | runtime, | App | v2 ran | the entire | inference | pipeline: |
(simulation-level)signalnecessaryfordriving
userembeddingswereproducedthroughtheTWN,relevance
| policy | updatesandshowingtheinterplayofexploration |     |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andexploitation. scoreswerecalculated,andthebanditchoseoneamongnine
|     |     |     |     |     | nudge mechanisms |     | to accompany |     | the suggested |     | product. We |
| --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | ------------- | --- | ----------- |
Input:
showedtheuseraselectednudgeandtheproductonanimme-
S={s(u,p)}:TWNrelevancescoresforuseruand
|     |     |     |     |     | diate basis, | and | the system | collected | the | behavioral | response |
| --- | --- | --- | --- | --- | ------------ | --- | ---------- | --------- | --- | ---------- | -------- |
productp
|     |     |     |     |     | after each | interaction. |     | In App | v1, we | maintained | the same |
| --- | --- | --- | --- | --- | ---------- | ------------ | --- | ------ | ------ | ---------- | -------- |
P:setofavailableproducts
Output: interaction structure, but nudges were assigned determinis-
|     |     |     |     |     | tically according |     | to business | rules | [45]. | All aspects | of user |
| --- | --- | --- | --- | --- | ----------------- | --- | ----------- | ----- | ----- | ----------- | ------- |
A_t:rankedrecommendationlistforinteractionroundt
interaction(recommendedproducts,nudgesdisplayed,selec-
1.Foreachuserudo
Initializepolicyvaluesπ[u][p]←s(u,p) tionbytheuser,appointmenttimes,andpurchaseoutcomes)
|     |     |     |     |     | were recorded |     | via a common |     | backend | with Supabase. | This |
| --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ------- | -------------- | ---- |
InitializerewardestimatesR[u][p]←0
InitializecountersC[u][p]←1 levelofbehavioralloggranularityenablesthereconstruction
|     |     |     |     |     | of decision | trajectories |     | and model | testing | in  | digital exper- |
| --- | --- | --- | --- | --- | ----------- | ------------ | --- | --------- | ------- | --- | -------------- |
Endfor
|     |     |     |     |     | imentation | [46]. | We leveraged |     | these event | logs | to analyze |
| --- | --- | --- | --- | --- | ---------- | ----- | ------------ | --- | ----------- | ---- | ---------- |
2.Foreachinteractionroundtwithuserudo
Determineexplorationrateε model performance, calculate reward and regret trajecto-
|     |     |     |     |     | ries, and | validate | the behavioral |     | influence | of  | the treatment |
| --- | --- | --- | --- | --- | --------- | -------- | -------------- | --- | --------- | --- | ------------- |
Rankproductsbycurrentpolicyvaluesπ[u][p]
| ConstructrecommendationlistA_tusingε-greedy |     |     |     |     | condition[47]. |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
logic
PresentrecommendationlistA_ttotheuserand
IV. RESULTSANDDISCUSSIONS
observeselectedproductsB_t Duetothequasi-experimentalsequentialnatureofthestudy,
3.Foreachproductp(cid:2)B_tdo
|     |     |     |     |     | we interpret | results | as  | associations | consistent |     | with a treat- |
| --- | --- | --- | --- | --- | ------------ | ------- | --- | ------------ | ---------- | --- | ------------- |
Samplerewardr_tfromGaussiandistribution
|     |     |     |     |     | ment effect | rather | than | causal | estimates. | To  | control for |
| --- | --- | --- | --- | --- | ----------- | ------ | ---- | ------ | ---------- | --- | ----------- |
Updatecumulativereward:R[u][p]←R[u][p]+r_t
|     |     |     |     |     | possible | cohort | and time-window |     | confounds | and | better cap- |
| --- | --- | --- | --- | --- | -------- | ------ | --------------- | --- | --------- | --- | ----------- |
Updatepolicyestimate:π[u][p]←π[u][p]+(1/
turetreatment-relateddifferences,wepresenteffectsizeswith
C[u][p])·(r_t−π[u][p])
|     |     |     |     |     | confidence | limits | and, | in addition | to  | descriptive | compar- |
| --- | --- | --- | --- | --- | ---------- | ------ | ---- | ----------- | --- | ----------- | ------- |
Incrementcounter:C[u][p]←C[u][p]+1
isons, regression-adjustedestimates.
Endfor
4.Computeregret
A. PARTICIPANTANDEXPERIMENTOVERVIEW
Loginteraction
GeneratenextrecommendationlistA_{t+1}using In this study, a true A/B experiment with real human users
updatedpolicyvaluesπ[u][p] and a realistic digital environment is described. A total
Endfor of 276 individuals entered the research funnel by com-
|     |     |     |     |     | pleting | the consent | process, |     | of whom | 254 completed | the |
| --- | --- | --- | --- | --- | ------- | ----------- | -------- | --- | ------- | ------------- | --- |
EndAlgorithm
|     |     |     |     |     | behavioral | questionnaire |     | and | 253 completed | the | simulation |
| --- | --- | --- | --- | --- | ---------- | ------------- | --- | --- | ------------- | --- | ---------- |
journey.
|             |              |                  |     |                | In the       | first round | of  | testing   | (26–29 November |      | 2024), 214 |
| ----------- | ------------ | ---------------- | --- | -------------- | ------------ | ----------- | --- | --------- | --------------- | ---- | ---------- |
|             |              |                  |     |                | participants | validated   | as  | real bank | customers       | were | randomly   |
| combination | of TWN-based | personalization, |     | Gaussian feed- |              |             |     |           |                 |      |            |
back modeling, incremental learning, and regret evaluation, allocatedtoGroupA(Control)andinteractedwithAppVer-
sion1,astaticrule-basedsystemprovidingnon-personalized
| the MAB | adaptively | prioritizes | the products | most likely | to  |     |     |     |     |     |     |
| ------- | ---------- | ----------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
alignwiththeuser’spreferencesovertime. nudges[7],[48].Thecontrolphasecollectedbaselinebehav-
|     |     |     |     |     | ioral data.      | The | 54-item       | instrument | included    | seven         | categories |
| --- | --- | --- | --- | --- | ---------------- | --- | ------------- | ---------- | ----------- | ------------- | ---------- |
|     |     |     |     |     | (psychographics, |     | communication |            | tendencies, | demographics, |            |
G. DEPLOYMENTPIPELINE financial behavioral patterns, preference tendencies, nudge
The integrated nudge recommendation system was deployed preferences, and timing/frequency sensitivities),representing
in a split A/B setting through two parallel application en- multidimensionalbehavioralmodelingapproaches[6].Simu-
vironments: App v1 (Control) and App v2 (Treatment). To latedinteractionsandtransactionlogsforbrowsingaproduct
maintain equivalence in our experiment [43] both applica- and responding to a nudge were captured following standard
tionsfollowedthesamesimulationflow,productcatalog,de- loggingtechniques[49],[50].
cisionpoints,anduserinterface.Theonlydifferencewasthe The resulting dataset from Group A served as the training
recommendationengine.Appv1reliedonastaticrule-based foundationfortheAI-drivenNudgeRecommendationModel.
mechanism, whereas App v2 incorporated the Two-Tower The second test (2 April – 19 May 2025) of 174 Group B
| 410 |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

(Treatment) verified bank customers interacting with the AI- itsintegratedTWNpersonalizationandMABadaptivity,pro-
enabledsystemwasconductedafterthemodelwasplacedin ducednudgesthatwerebettermatchedincontext,motivation,
production in App Version 2 [51]. The two phases used dif- andeffectiveness.Movingawayfromstaticrecommendations
ferentgroupstoavoidcarryovereffectsandpreserveinternal towardmoreresponsivedecisionpathwaysisconsistentwith
validity. previousworkshowingthatadaptivenudgesaresignificantly
moreeffectivethanstaticnudges[54].
B. BASELINEPERFORMANCEANDBEHAVIORALPATTERNS
INGROUPA(CONTROL)
|           |              |     |             |     |             |     |            | D. COMPARATIVEANALYSIS:GROUPAVSGROUPB |          |             |              |           |         |                 |     |
| --------- | ------------ | --- | ----------- | --- | ----------- | --- | ---------- | ------------------------------------- | -------- | ----------- | ------------ | --------- | ------- | --------------- | --- |
| To better | understand   |     | the sources | of  | performance |     | improve-   |                                       |          |             |              |           |         |                 |     |
|           |              |     |             |     |             |     |            | From Group                            |          | A (Control) |              | and Group | B       | (Treatment),    | the |
| ments,    | we extend    | the | comparison  |     | beyond      | the | rule-based |                                       |          |             |              |           |         |                 |     |
|           |              |     |             |     |             |     |            | comparative                           | analysis |             | demonstrates |           | a clear | and substantial |     |
| baseline  | by including |     | a TWN-only  |     | ablation.   |     | This en-   |                                       |          |             |              |           |         |                 |     |
behavioralshiftattributabletotheimplementationoftheAI-
| ables a     | three-way       | comparison |     | between  | the | rule-based | sys-     |         |       |                |     |     |        |                |     |
| ----------- | --------------- | ---------- | --- | -------- | --- | ---------- | -------- | ------- | ----- | -------------- | --- | --- | ------ | -------------- | --- |
|             |                 |            |     |          |     |            |          | powered | Nudge | Recommendation |     |     | Model. | The experiment |     |
| tem, static | personalization |            |     | via TWN, | and | the        | proposed |         |       |                |     |     |        |                |     |
involved214verifiedbankcustomersinteractingwitharule-
| TWN+MAB+nudge |     | system. |     | Group | A interacted |     | with App |     |     |     |     |     |     |     |     |
| ------------- | --- | ------- | --- | ----- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
basedenvironment(Appv1)and174verifiedbankcustomers
Version1,arule-basedprototypewithoutpersonalizednudges
|     |     |     |     |     |     |     |     | engaging | with | an AI-enabled |     | environment |     | (App v2). | The |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------------- | --- | ----------- | --- | --------- | --- |
orAI-drivenrecommendationlogic.Thisgroupincluded214
|          |      |           |       |            |     |          |        | comparison | focuses |     | on three | key | behavioral | metrics: | (1) |
| -------- | ---- | --------- | ----- | ---------- | --- | -------- | ------ | ---------- | ------- | --- | -------- | --- | ---------- | -------- | --- |
| verified | bank | customers | whose | behavioral |     | patterns | served |            |         |     |          |     |            |          |     |
totalpurchaseconversion,(2)recommendation-drivenconver-
| as the benchmark. |     | Two | data | sources | were | collected: | (1) re- |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ---- | ------- | ---- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
sion,and(3)alignmentwithbest-armpredictions.Withinthe
| sponses | to the | 54-item | behavioral |     | instrument | [52]; | and (2) |     |     |     |     |     |     |     |     |
| ------- | ------ | ------- | ---------- | --- | ---------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
constraintsofasimulateddeploymentenvironmentandacon-
| logs of | behaviors | such | as product | views, | responses |     | to static |                      |     |     |         |       |                 |     |         |
| ------- | --------- | ---- | ---------- | ------ | --------- | --- | --------- | -------------------- | --- | --- | ------- | ----- | --------------- | --- | ------- |
|         |           |      |            |        |           |     |           | trolled experimental |     |     | design, | these | metrics provide | a   | focused |
nudges,andmock-purchaseoutcomes[8].
|        |        |     |      |            |          |     |            | basis for | evaluating |     | relative | behavioral | differences | between |     |
| ------ | ------ | --- | ---- | ---------- | -------- | --- | ---------- | --------- | ---------- | --- | -------- | ---------- | ----------- | ------- | --- |
| Of 214 | users, | 104 | made | a purchase | (48.6%). |     | A total of |           |            |     |          |            |             |         |     |
conditions.
| 29purchaseswereinaccordance |     |     |     | withthesystemsuggestion |     |     |     |               |     |        |          |         |     |                |     |
| --------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | ------------- | --- | ------ | -------- | ------- | --- | -------------- | --- |
|                             |     |     |     |                         |     |     |     | The strongest |     | causal | evidence | emerges |     | from recommen- |     |
(13.6%).Theapplackedadaptiveoptimization,andtherefore
dation-drivenbehavior.InGroupA,only29purchasesaligned
therewasnobestrecommendationmechanism.Theseresults
|           |             |     |                 |     |          |     |           | with the | system’s | static | rules | (13.6%). | In contrast, | Group | B   |
| --------- | ----------- | --- | --------------- | --- | -------- | --- | --------- | -------- | -------- | ------ | ----- | -------- | ------------ | ----- | --- |
| show that | the failure | of  | personalization |     | resulted | in  | poor rec- |          |          |        |       |          |              |       |     |
produced92purchasesalignedwithAI-generatedrecommen-
| ommendation |     | compliance | and | limited | behavioral |     | influence. |         |           |              |     |        |             |           |     |
| ----------- | --- | ---------- | --- | ------- | ---------- | --- | ---------- | ------- | --------- | ------------ | --- | ------ | ----------- | --------- | --- |
|             |     |            |     |         |            |     |            | dations | (52.87%), | representing |     | nearly | a four-fold | increase. |     |
GroupAdatawasaggregatedtotraintheTwo-TowerNetwork
|                 |     |        |       |           |     |          |         | This result  | mirrors | prior | evidence        |     | that adaptive | nudges   | and |
| --------------- | --- | ------ | ----- | --------- | --- | -------- | ------- | ------------ | ------- | ----- | --------------- | --- | ------------- | -------- | --- |
| and Multi-Armed |     | Bandit | [53], | providing | a   | baseline | of user |              |         |       |                 |     |               |          |     |
|                 |     |        |       |           |     |          |         | contextually | framed  |       | recommendations |     | significantly | increase |     |
behaviorinaconventionalstaticcampaigncontext.
|     |     |     |     |     |     |     |     | compliance | with   | suggested  |     | actions | [36], [37].   | Since  | all el- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---------- | --- | ------- | ------------- | ------ | ------- |
|     |     |     |     |     |     |     |     | ements     | of the | experiment |     | were    | held constant | except | the     |
C. PERFORMANCEOFTHEAI-DRIVENMODELINGROUPB nudge-generation mechanism, this disparity directly reflects
(TREATMENT) the causal effect of the AI-driven intervention. This causal
In the second testing period (2 April – 19 May 2025), the interpretation should be understood within the bounds of the
174 real users interacted with Nudge Simulation App v2, sequentialA/Bdesignandsimulatedcontext,whichmaynot
andtheAI-drivenNudgeRecommendationModelwastested fullycapturereal-worldtemporaloreconomiceffects.
in Group B. In contrast to the fixed-rule context in Group The Multi-Armed Bandit (MAB) further amplified this
A, app v2 incorporated the hybrid architecture in which the effect by adaptively optimizing nudge strategies in real
Two-Tower Network (TWN) produced personalized product time. The bandit algorithm consistently identified the op-
relevancescores,whiletheMulti-ArmedBandit(MAB)used timal arm with the highest reward expectation, and all 92
streaming reward signals to dynamically adapt nudge selec- recommendation-driven purchases (100%) converged on this
tioninrealtime.Thisconfigurationenabledbothpersonalized optimal arm. This indicates strong user acceptability of the
baseline recommendations and adaptive behavioral nudging algorithmicrecommendationsandalignswithliteratureshow-
throughouttheuserjourney. ing that adaptive bandit systems tend to concentrate user
The behavioral outcomes demonstrated a clear improve- actions on high-performing arms once stable reward esti-
ment in decision-making effectiveness. Out of 174 users, mates are established [55]. While this concentration reflects
108 completed a purchase (62.07%), higher than the 48.6% short-term behavioral alignment with the learned policy, it
baseline observed in Group A. A total of 92 users made does not by itself imply long-term preference stabilization.
purchases that directly matched the nudges generated by the Conversely, Group A displayed diffused, unguided choice
model, yielding a 52.87% recommendation-driven conver- patterns, consistent with non-adaptively optimized environ-
| sion rate. | The | strongest | finding | in  | this study | is  | that 100% | ments. |     |     |     |     |     |     |     |
| ---------- | --- | --------- | ------- | --- | ---------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
(92) of recommendation-driven purchases were aligned with Taken together, these findings show that the hybrid model
the optimal arm identified by the MAB algorithm. Reduced combiningTwo-Towerpersonalizationwithadaptivenudging
exploratory behavior and clearer decision paths were also via MAB consistently outperforms the rule-based baseline
reflectedinlogsofsysteminteraction.Together,theseresults across all major behavioral metrics. The treatment group
constitutesubstantialevidencethattheAI-drivenmodel,with demonstrated higher engagement, greater responsiveness to
| VOLUME7,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 411 |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

KRISTIANAETAL.:VALIDATINGAI-DRIVENNUDGERECOMMENDATIONS:A/BTESTINGTWO-TOWERANDBANDITMODELS
|          |                                                     |     |     |     |     |     |     | FIGURE5.     | Smoothedinstantregretoverround(Threshold-based |     |     |     |     |
| -------- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | ---------------------------------------------- | --- | --- | --- | --- |
| FIGURE4. | Stabilityofevent-levelrewardtrajectoriesunderonline |     |     |     |     |     |     | evaluation). |                                                |     |     |     |     |
multi-armedbanditlearning.
|     |     |     |     |     |     |     |     | TABLE2. | A/BTestingMetricsforControlandTreatmentGroups |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------------------------------------- | --- | --- | --- | --- |
recommendations,andsubstantiallystrongerbehavioralcon-
| sistency.      | These        | results  | provide  | strong      | empirical    |             | evidence |     |     |     |     |     |     |
| -------------- | ------------ | -------- | -------- | ----------- | ------------ | ----------- | -------- | --- | --- | --- | --- | --- | --- |
| that AI-driven | nudging      |          | produces | meaningful, |              | consistent, | and      |     |     |     |     |     |     |
| causally       | attributable | benefits |          | in digital  | banking      |             | campaign |     |     |     |     |     |     |
| performance,   | reinforcing  |          | insights | from        | recent       | work        | on per-  |     |     |     |     |     |     |
| sonalized      | decision     | support  | systems  | [54].       | Accordingly, |             | these    |     |     |     |     |     |     |
benefitsshouldbeinterpretedasdemonstratingrelativeeffec-
tivenessunderthestudiedexperimentalconditionsratherthan
unconditionalgeneralizabilitytoreal-worldfinancialdeploy-
ments.
| A chi-square | test | was | applied | to evaluate |     | whether | the dif- |     |     |     |     |     |     |
| ------------ | ---- | --- | ------- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- |
ferenceinrecommendation-alignedbehaviorbetweengroups
| was statistically |       | significant. |               | The result | (χ2 | =           | 6.49, p | <   |     |     |     |     |     |
| ----------------- | ----- | ------------ | ------------- | ---------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- |
| 0.0108) confirms  |       | that         | the treatment | group’s    |     | behavioral  | shift   |     |     |     |     |     |     |
| is unlikely       | to be | driven       | by random     | variation, |     | reinforcing | the     |     |     |     |     |     |     |
causaleffectoftheAI-drivennudgingmechanism.
E. MULTI-ARMEDBANDITPERFORMANCE:REWARDAND
REGRETANALYSIS
per-recommendation-eventbasisasthedifferencebetweenthe
| To allow | insights | into | the internal | working |     | of MAB | in the |     |     |     |     |     |     |
| -------- | -------- | ---- | ------------ | ------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- |
rewardobtainedforthenudgeselectedbythebanditandthe
| treatment                                     | environment,                              |     | we provide | reward |     | and regret | trajec- |                   |                 |        |          |              |                 |
| --------------------------------------------- | ----------------------------------------- | --- | ---------- | ------ | --- | ---------- | ------- | ----------------- | --------------- | ------ | -------- | ------------ | --------------- |
|                                               |                                           |     |            |        |     |            |         | reward            | that would have | been   | obtained | had          | the empirically |
| toriesover                                    | timeforallrecommendationevents.Boththeraw |     |            |        |     |            |         |                   |                 |        |          |              |                 |
|                                               |                                           |     |            |        |     |            |         | best-performing   | nudge           | been   | opted    | for instead. | This results    |
| rewardsignalanda50-iterationrunningaverageare |                                           |     |            |        |     |            | givenin |                   |                 |        |          |              |                 |
|                                               |                                           |     |            |        |     |            |         | in an oscillating | curve           | across | the      | interaction  | window, be-     |
Fig.4.Thisfigureisnotmeanttodepictamonotonicincrease
|     |     |     |     |     |     |     |     | cause this | metric represents |     | the quality | of  | an instantaneous |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | ----------- | --- | ---------------- |
inperformancebutrathertohighlightthatthelearnedpolicy
|                |       |        |     |                    |     |        |       | decision | rather than | a long-horizon |     | cumulative | formulation. |
| -------------- | ----- | ------ | --- | ------------------ | --- | ------ | ----- | -------- | ----------- | -------------- | --- | ---------- | ------------ |
| remains stable | under | highly |     | noisy, event-level |     | online | feed- |          |             |                |     |            |              |
Thesmoothedregrettrajectorystayswellunderourthreshold
| back. Although | realizations |     | of  | individual | rewards |     | are highly |     |     |     |     |     |     |
| -------------- | ------------ | --- | --- | ---------- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
of0.10and0.15,demonstratingthatthebanditrarelystrayed
variable,thetime-averagedrewardcurveremainsremarkably
|     |     |     |     |     |     |     |     | far from | the empirically | optimal | nudge | in  | recommendation. |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ------- | ----- | --- | --------------- |
stablearoundacommonmeanoveriterations.Thisisaligned
|          |             |        |        |          |     |           |       | The occasional | spikes | correspond | to  | intentional | exploratory |
| -------- | ----------- | ------ | ------ | -------- | --- | --------- | ----- | -------------- | ------ | ---------- | --- | ----------- | ----------- |
| with the | anticipated | online | bandit | learning |     | behavior, | which |                |        |            |     |             |             |
behavior,whichisasignatureandnormalfeatureofadaptive
| originates | from | early | stochasticity | due | to  | exploration, | and |     |     |     |     |     |     |
| ---------- | ---- | ----- | ------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
learningsystemsthataredesignedtoavoidprematureconver-
| then stable | reward | levels | can | be maintained |     | in later | rounds |     |     |     |     |     |     |
| ----------- | ------ | ------ | --- | ------------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- |
gence[56].
| given enough         | observational |     | evidence.  |     | Fig.       | 4 is a | validating |     |     |     |     |     |     |
| -------------------- | ------------- | --- | ---------- | --- | ---------- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
| test of operability, |               | and | such decay | in  | all states | could  | be cap-    |     |     |     |     |     |     |
turedwhentherearecontinuousonlineupdates,eventhough F. BEHAVIORALINTERPRETATIONANDDISCUSSION
MABwouldnotdeviateasillustratedbecauseimprovements The substantial increase in recommendation-aligned pur-
forperformanceachievedbyitandpolicy’seffectivenessare chases (13.6% in Group A versus 52.87% in Group B)
moredirectlydeterminedthroughregretanalysis(asdepicted indicates that the AI-driven recommendation model signifi-
inFig.5)andoutcome-basedmetricsrevealedinTable2. cantlyinfluencedusers’decisionprocessesbydirectingthem
More information on the quality of the model decision- toward system-optimized options. The experimental design
making can be found in the regret analysis in Fig. 5. supports a causal interpretation within the setting studied,
Specifically, in this experiment, regret was calculated on a as the recommendation engine was the only manipulated
| 412 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ |

variable, users were independently assigned without cross- a simulated context in which real financial risk and long-
exposure,andrecommendation-followingbehaviorincreased term behavioral adaptation were not fully present. There-
bymorethanfourfoldinthetreatmentgroup. fore, the outcomes really indicate that AI-based nudging
For additional context on the size of the behavior effect can be operationalized and has a relative impact when ap-
observed, we provide an effect-size estimate for following plied under restricted conditions that deployment will lead
recommendationbehavior.Theprescriptionadherenceproba- to comparable results. Internal learning diagnostics comple-
bilityofthecontrolgroupincreasedfrom13.6%to52.87%in menttheseresults.Treatment-grouprecommendation-aligned
thetreatment group.Thisvaluecorrespondstoanoddsratio purchasesalwaysagreedwiththebandit’sbestarm,whilere-
of approximately 7.15, implying that users who were sub- gretcurvesrevealednearlyconstant exploration–exploitation
jectedtotheAI-basednudgesystem willbeoverseventimes without policy-averse divergence. Such signals affirm the
more likely to mimic a rule-based environment. The magni- internallearningofthesystemandcomplementtheoutcome-
tude of this effect is sufficiently large that it decreases the basedevaluation.
possibility that the observed behavioral change derives en- Collectively, our work provides a reproducible and inter-
tirelyfromtime-orcohort-basedconfoundsandisconsistent pretable approach for combining machine learning models
withtheframingofourstudyasanongoingquasi-experiment. withbehavioraleconomicframeworksinthedesignofdigital
Taken together, these factors suggest that the observed personalizationsystems.Thus,interpretationsofourreported
behavioral differences are primarily attributable to the AI- findings couldbeclarifiedasthatofevidencesupportive(not
based nudging mechanism rather than to user composition confirmatory) of a causal role in the studied context (not
or experimental artifacts. This interpretation, however, re- alldeployment).Futureapplicationinvolvesgeneralization to
mains bound by the sequential A/B design and simulated other, possibly larger and more diverse, user populations; a
deployment context. Within these constraints, the results newrewardsdefinitionconsistentwithdomain-specificgoals;
indicatethatcombiningstaticpersonalizationthroughaTwo- and further precautions tackling fairness, transparency, and
TowerNetworkwithadaptiveoptimizationviaaMulti-Armed long-terminducedbehaviors.
Bandit enhances user responsiveness to personalized recom-
mendations by jointly addressing individual relevance and LIMITATIONS
momentarydecisioncontext. Despite contributing important evidence of the benefit of
While the proposed AI-driven nudge system demonstrates AI-driven nudging, there are limitations to our study. We
measurable behavioral effects under controlled experimen- conducted our experiments in a simulated mobile bank-
tal conditions, real-world deployment would require explicit ing environment and not in the actual financial application,
Responsible AI guardrails. These include risk-tier caps to leading to low ecological validity because users were not
limit high-impact recommendations, lightweight explanation involved in real monetary losses. The personalization model
mechanisms to support user understanding, continuous fair- was limited because it was trained on a medium-sized and
nessmonitoringacrossusersegments,andopt-outoroverride domain-specific corpus, making generalizability weaker for
options to preserve user autonomy. In addition, periodic au- userswherepastbehaviorsaresparseordemographicprofiles
ditingofmodelbehaviorandoutcomeswouldbenecessaryto are underrepresented in the training data. The A/B testing
ensureaccountability,transparency,andregulatoryalignment designequallydependedontwonon-overlappingdeployment
infinancialapplications. windows, which implies that time-based effects cannot be
completelydiscarded,eventhoughthetwoenvironmentswere
V. CONCLUSION thesameinflowandinterface.Thestudy,therefore,shouldbe
Using a simulated digital banking environment, results offer viewedasaquasi-experimentwithtemporalor cohort(resid-
empirical evidence for the effectiveness of AI-driven nudg- ual)influencesontheobservedmeasures,evenifoperational
ing in increasing recommendation-following behavior and controlwasachieved.Lastly,althoughtheuseofAIfornudg-
purchase outcomes. The proposed Nudge Recommendation inghasobviousadvantages,ethicalconsiderationsshouldnot
Model that uses a Two-Tower Network to incorporate static be overlooked; due to its personalized models, the system
personalization and a Multi-Armed Bandit for dynamic be- learns from individual behavioral patterns, this entails chal-
havioral optimization yielded results whose predictive distri- lenges for both personal autonomy and fairness. While these
butionsweredrasticallydifferentfromthoseoftherule-based risksdidnotarisein thisstudy,deploymentinthereal-world
baseline.InourA/Bexperimental control,thetreatmenthad wouldrequiresafeguardspreventingthedifferentialdisadvan-
a 62.07% purchase rate and the control group, 48.6%. More tageofcertainusergroupsthroughincreasedpersonalization,
importantly, recommendation-following behavior rose from ordecreasedtransparencyindecisiongenerationovertime.
13.61%inthecontrolto52.87%underAI,andthisincreased
behavioralalignmentwas greaterthanfourfold. FUTUREWORK
These outcome-level improvements should be interpreted To enhance the impact of the proposed Nudge Recommen-
considering the study’s experimental design and limitations. dationModel,wesuggestconductingexperimentalvalidation
While the observed behavioral effects are statistically sig- in live mobile banking settings to evaluate how it holds up
nificant (χ2 = 6.49, p < 0.0108), they are derived from under actual financial consequences, contextual signals, and
VOLUME7,2026 413

KRISTIANAETAL.:VALIDATINGAI-DRIVENNUDGERECOMMENDATIONS:A/BTESTINGTWO-TOWERANDBANDITMODELS
| real behavioral | trajectories. | Putting | the | system | in production |     |           |             |           |         |               |     |             |       |
| --------------- | ------------- | ------- | --- | ------ | ------------- | --- | --------- | ----------- | --------- | ------- | ------------- | --- | ----------- | ----- |
|                 |               |         |     |        |               |     | [8] A. G. | Cossatin,   | N. Mauro, | and     | L. Ardissono, |     | “Promoting  | green |
|                 |               |         |     |        |               |     | fashion   | consumption | through   | digital | nudges        | in  | recommender | sys-  |
wouldallowassessmentofsustainedengagement,fairnesstra-
tems,”IEEEAccess,vol.12,pp.6812–6829,2024,doi:10.1109/AC-
| jectories, | and long-term | learning | behaviors, | including |     | model |     |     |     |     |     |     |     |     |
| ---------- | ------------- | -------- | ---------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
CESS.2024.3349710.
driftandnudgefatigue.Futureworkontheadaptivelayercan [9] W. Guo, H. Yao, Y. Q. Zhu, and Z. Z. Zhang, “A self-organization
look at contextual or hierarchical bandit models, reinforce- reconstruction method of ESN reservoir structure based on rein-
|               |          |           |                 |     |     |         | forcement | learning,” | Inf. | Sci., vol. | 677, 2024, | Art. | no. 120826, | doi: |
| ------------- | -------- | --------- | --------------- | --- | --- | ------- | --------- | ---------- | ---- | ---------- | ---------- | ---- | ----------- | ---- |
| ment learning | methods, | or hybrid | symbolic–neural |     |     | systems |           |            |      |            |            |      |             |      |
10.1016/j.ins.2024.120826.
that incorporate domain rules with behavioral optimization. [10] Q. He, X. Li, and B. Cai, “Graph neural network recommendation
Finally,asthenudgingapproachusingAIbecomesprevalent algorithm based on improved dual tower model,” Sci. Rep., vol. 14,
in financial applications, more work is needed to identify no.1,2024,Art.no.3853,doi:10.1038/s41598-024-54376-3.
|     |     |     |     |     |     |     | [11] B.C.Bragaetal.,“Feasibilityofusinganartificialintelligence-based |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
ethical,regulatory,andtransparencychallenges. telephoneapplicationfordietaryassessmentandnudgingtoimprove
thequalityoffoodchoicesoffemaleadolescentsinVietnam:Evidence
fromarandomizedpilotstudy,”Curr.DevelopmentsNutr.,vol.8,2023,
DATA,CODEAVAILABILITY,ANDAUTHOR Art.no.102063,doi:10.1016/j.cdnut.2023.102063.
|     |     |     |     |     |     |     | [12] C.Zhang,D.Lakens,andW.A.IJsselsteijn,“Theoryintegrationfor |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
CONTRIBUTIONS lifestyle behavior change in the digital age: An adaptive decision-
The processed datasets underlying this study are pub- makingframework,”J.Med.InternetRes.,vol.23,no.4,Apr.2021,
licly available from Zenodo at https://zenodo.org/records/ Art.no.e17127,doi:10.2196/17127.
|     |     |     |     |     |     |     | [13] S. Sengupta |     | et al., “A review | of  | deep learning | with | special | empha- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------------- | --- | ------------- | ---- | ------- | ------ |
16088582, consisting of anonymized and aggregated experi- sis on architectures, applications and recent trends,” Knowl.-Based
mentaloutputsusedforanalysisandfiguregenerationwithout Syst., vol. 194, 2020, Art. no. 105596, doi: 10.1016/j.knosys.2020.
105596.
| exposing                                             | raw or confidential |     | user data. | The | source | code for |                |     |                    |         |             |             |               |       |
| ---------------------------------------------------- | ------------------- | --- | ---------- | --- | ------ | -------- | -------------- | --- | ------------------ | ------- | ----------- | ----------- | ------------- | ----- |
|                                                      |                     |     |            |     |        |          | [14] C. Zeng,  | Q.  | Wang, S. Mokhtari, |         | and T.      | Li, “Online | context-aware |       |
| thebackendservices,recommendationlogic,andexperimen- |                     |     |            |     |        |          |                |     |                    |         |             |             |               | Proc. |
|                                                      |                     |     |            |     |        |          | recommendation |     | with time          | varying | multi-armed |             | bandit,”      | in    |
tal scripts is accessible via the project’s Git repository at ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., Aug. 2016,
pp.2025–2034,doi:10.1145/2939672.2939878.
https://github.com/nudge-deploy/NudgeCronjob,enablingre-
|            |                 |         |     |         |        |        | [15] I.Kristiana,H.Prabowo,F.L.Gaol,andN.N.Qomariyah,“AI-driven |     |     |     |     |     |     |     |
| ---------- | --------------- | ------- | --- | ------- | ------ | ------ | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| production | of the reported | figures | and | tables; | direct | access |                                                                 |     |     |     |     |     |     |     |
nudgeoptimization:Integratingtwo-towernetworksandmulti-armed
|                   |          |            |                 |         |            |      | bandit | with    | behavioral economics       |     | for digital | banking | campaign,”       |     |
| ----------------- | -------- | ---------- | --------------- | ------- | ---------- | ---- | ------ | ------- | -------------------------- | --- | ----------- | ------- | ---------------- | --- |
| to the production | Supabase |            | infrastructure  | remains | restricted |      |        |         |                            |     |             |         |                  |     |
|                   |          |            |                 |         |            |      | IEEE   | Access, | vol. 13, pp.112948–112961, |     |             | 2025,   | doi: 10.1109/AC- |     |
| due to security   | and      | regulatory | considerations. |         | This       | work |        |         |                            |     |             |         |                  |     |
CESS.2025.3584648.
| was conducted | as part | of the | doctoral | dissertation |     | of the |                  |     |                   |     |                |     |           |          |
| ------------- | ------- | ------ | -------- | ------------ | --- | ------ | ---------------- | --- | ----------------- | --- | -------------- | --- | --------- | -------- |
|               |         |        |          |              |     |        | [16] E. Engström |     | and P. Strimling, |     | “Deep learning |     | diffusion | by infu- |
lead author, Idha Kristiana, who led the conceptualization, sion into preexisting technologies – Implications for users and so-
|             |         |                |       |              |     |     | ciety | at large,” | Technol. | Soc., vol. | 63, 2020, | Art. | no. 101396, | doi: |
| ----------- | ------- | -------------- | ----- | ------------ | --- | --- | ----- | ---------- | -------- | ---------- | --------- | ---- | ----------- | ---- |
| methodology | design, | data analysis, | model | development, |     | and |       |            |          |            |           |      |             |      |
10.1016/j.techsoc.2020.101396.
manuscript preparation. Harjanto Prabowo, Ford Lumban [17] R. Karlsen and A. Andersen, “Recommendations with a nudge,”
Gaol,andNunungNurulQomariahservedasacademicsuper- Technologies,vol.7,no.2,2019,Art.no.45,doi:10.3390/technolo-
visors,providingintellectualguidance,validation,andcritical gies7020045.
|     |     |     |     |     |     |     | [18] G. Fan, | C.  | Zhang, K. Wang, | and | J. Chen, | “MV-HAN: |     | A hybrid |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------------- | --- | -------- | -------- | --- | -------- |
reviewthroughouttheresearchprocess.Allauthorsreviewed attentive networks based multi-view learning model for large-scale
andapprovedthefinalmanuscript. contentsrecommendation,”inProc.37thIEEE/ACMInt.Conf.Auto-
matedSoftw.Eng.,2022,vol.1,no.1,pp.1–5,doi:10.1145/3551349.
3559496.
|     |     |     |     |     |     |     | [19] P.Agarwal,M.Srivastava,V.Singh,andC.Rosenberg,“Modelinguser |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
REFERENCES behaviorwithinteractionnetworksforspamdetection,”inProc.45th
[1] L.Cao,Q.Yang,andP.S.Yu,“DatascienceandAIinFinTech:An Int.ACMSIGIRConf.Res.Develop.Inf.Retrieval,2022,vol.1,no.1,
overview,”Int.J.DataSci.Anal.,vol.12,no.2,pp.81–99,2021,doi: pp.2437–2442,doi:10.1145/3477495.3531875.
10.1007/s41060-021-00278-w. [20] F.Liuetal.,“Deepreinforcementlearningbasedrecommendationwith
[2] R.N.TeningandM.K.Harder,“Anexplorationofnudgingtowards explicituser-iteminteractionsmodeling,”2018,arXiv:1810.12027.
transformative environmental behaviour changes prior to a values- [21] Y. Han, “Comparative evaluation, challenges, and diverse applica-
crystallizationevent,”Heliyon,vol.9,no.8,2023,Art.no.e18689,doi: tionsofmulti-armedbanditalgorithms,”HighlightsSci.Eng.Technol.,
10.1016/j.heliyon.2023.e18689. vol.94,pp.206–210,2024,doi:10.54097/jdcjkj94.
[3] T. Keller and P. Szakál, “The framing of information nudge affects [22] C. Vandelanotte et al., “Increasing physical activity using an just-
students’Anticipatedeffort:Alarge-scale,randomizedsurveyexper- in-time adaptive digital assistant supported by machine learning:
iment,” J. Behav. Exp. Econ., vol. 104, 2023, Art. no. 102012, doi: A novel approach for hyper-personalised mHealth interventions,” J.
10.1016/j.socec.2023.102012. Biomed. Inform., vol. 144, no. June, 2023, Art. no. 104435, doi:
[4] T. A. G. Venema, F. M. Kroese, E. De Vet, and D. T. D. De Rid- 10.1016/j.jbi.2023.104435.
|           |            |              |          |             |     |            | [23] M.Guath,B.Stikvoort,andP.Juslin,“Nudgingforeco-friendlyon- |     |     |     |     |     |     |     |
| --------- | ---------- | ------------ | -------- | ----------- | --- | ---------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| der, “The | one that I | want: Strong | personal | preferences |     | render the |                                                                 |     |     |     |     |     |     |     |
center-stagenudgeredundant,”FoodQual.Preference,vol.78,2019, line shopping – Attraction effect curbs,” J. Econ. Psychol., vol. 81,
Art.no.103744,doi:10.1016/j.foodqual.2019.103744. Dec.2022,Art.no.102368,doi:10.1016/j.joep.2022.102368.
[5] S. Chandra, S. Verma, W. M. Lim, S. Kumar, and N. Donthu, [24] M. Poch et al., “Increasing resilience through nudges in the urban
“Personalization in personalized marketing: Trends and ways for- water cycle: An integrative conceptual framework to support policy
decision-making,”Chemosphere,vol.317,2023,Art.no.137850,doi:
ward,”Psychol.Marketing,vol.39,no.8,pp.1529–1562,2022,doi:
| 10.1002/mar.21670. |     |     |     |     |     |     | 10.1016/j.chemosphere.2023.137850. |     |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[6] C. Mele, T. R. Spena, V. Kaartemo, and M. L. Marzullo, “Smart [25] A.Caraban,E.Karapanos,D.Gonçalves,andP.Campos,“23Waysto
nudging: How cognitive technologies enable choice architectures for nudge:Areviewoftechnology-mediatednudginginhuman-computer
value co-creation,” J. Bus. Res., vol. 129, pp.949–960, 2021, doi: interaction,”inProc.Conf.Hum.FactorsComput.Syst.-Proc.,2019,
pp.1–15,doi:10.1145/3290605.3300733.
10.1016/j.jbusres.2020.09.004.
[7] M.JesseandD.Jannach,“Digitalnudgingwithrecommendersystems: [26] D. Bec´irovic´, A. Z. Suhonjic´, and M. Stanic´, “Using loss aversion
Surveyandfuturedirections,”Comput.Hum.Behav.Rep.,vol.3,Jan.– andframingtonudgestudents’classroomperformance,”Management,
Jul.2021,Art.no.100052,doi:10.1016/j.chbr.2020.100052. vol.27,no.2,pp.5–17,Dec.2022,doi:10.30924/mjcmi.27.2.2.
| 414 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME7,2026 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

[27] L. T. T. Loan and R. M. Balanay, “Towards reinforcing the waste [47] S. Gupta, S. Chaudhari, S. Mukherjee, G. Joshi, and O. Y. Gan,
separation at source for Vietnam’s waste management: Insights from “A unified approach to translate classical bandit algorithms to
theNudgetheory,”Environ.Challenges,vol.10,2023,Art.no.100660, structured bandits,” in Proc. IEEE Int. Conf. Acoust. Speech Sig-
doi:10.1016/j.envc.2022.100660. nalProcess.,2021,pp.3360–3364,doi:10.1109/ICASSP39728.2021.
[28] J. Yang et al., “Mixed negative sampling for learning two-tower 9413628.
neural networks in recommendations,” in Proc. Web Conf. 2020 [48] M.Guath,B.Stikvoort,andP.Juslin,“Nudgingforeco-friendlyon-
- Companion World Wide Web Conf., 2020, pp.441–447, doi: line shopping – Attraction effect curbs price sensitivity,” J. Environ.
10.1145/3366424.3386195. Psychol., vol. 81, 2022, Art. no. 101821, doi: 10.1016/j.jenvp.2022.
[29] E. Hrnjic and N. Tomczak, “Machine learning and behavioral eco- 101821.
nomicsforpersonalizedchoicearchitecture,”Workingpaper,Jul.2019. [49] A.G.Barto,R.S.Sutton,andC.W.Anderson,“Neuronlikeadaptiveel-
[30] A.KhamajandA.M.Ali,“Adaptinguserexperiencewithreinforce- ementsthatcansolvedifficultlearningcontrolproblems,”IEEETrans.
mentlearning:Personalizinginterfacesbasedonuserbehavioranalysis Syst.ManCybern.,vol.SMC-13,no.5,pp.834–846,Sep./Oct.1983,
in real-time,” Alexandria Eng. J., vol. 95, pp.164–173, 2024, doi: doi:10.1109/TSMC.1983.6313077.
10.1016/j.aej.2024.03.045. [50] S.Carriesetal.,“Aneconomicincentivepackagetosupportthewellbe-
[31] M. A. Raji, H. B. Olodo, T. T. Oke, W. A. Addy, O. C. ingofcaregiversofadolescentslivingwithHIVduringtheCOVID-19
Ofodile, and A. T. Oyewole, “E-commerce and consumer behav- pandemicinSouthAfrica:Afeasibilitystudyprotocolforapilotran-
ior: A review of AI-powered personalization and market trends,” domisedtrial,”PilotFeasibilityStud.,vol.9,no.1,pp.1–11,2023,doi:
GSC Adv. Res. Rev., vol. 18, no. 3, pp.66–77, Mar. 2024, doi: 10.1186/s40814-023-01237-x.
10.30574/gscarr.2024.18.3.0090. [51] R. Wongprawmas et al., “Nudging Italian university students to-
[32] A.C.Powell,“Impactoftheartificialnudge,”Acad.Radiol.,vol.27, wards healthy and sustainable food choices: An online experi-
no.1,pp.143–146,2020,doi:10.1016/j.acra.2019.09.010. ment,” Food Qual. Preference, vol. 111, 2023, Art. no. 104971, doi:
[33] S. Gupta, S. Chaudhari, G. Joshi, and O. Yagan, “Multi-armed ban- 10.1016/j.foodqual.2023.104971.
dits with correlated arms,” IEEE Trans. Inf. Theory, vol. 67, no. 10, [52] M. Mariani, S. Bresciani, and G. B. Dagnino, “The competitive
pp.6711–6732,Oct.2021,doi:10.1109/TIT.2021.3081508. productivity (CP) of tourism destinations: An integrative conceptual
[34] A˚. Löfgren and K. Nordblom, “Reconciling sustainability prefer- frameworkandareflectiononBigDataandanalytics,”Int.J.Contem-
ences and behavior — The case of mutual fund investments,” poraryHospitalityManage.,vol.33,no.9,pp.2970–3002,Jan.2021,
J. Behav. Exp. Financ., vol. 41, 2024, Art. no. 100880, doi: doi:10.1108/IJCHM-09-2020-1102.
10.1016/j.jbef.2023.100880. [53] Z. Wei, N. Wu, F. Li, K. Wang, and W. Zhang, “MoCo4SRec: A
[35] Y. Yu, D. M. Yazan, M. van den Berg, D. R. Firdausy, V. Junjan, momentumcontrastivelearningframeworkforsequentialrecommen-
andM.-E.Iacob,“Circularityinformationplatformforthebuiltenvi- dation,” Expert Syst. Appl., vol. 223, 2023, Art. no. 119911, doi:
ronment,”Autom.Construction,vol.152,2023,Art.no.104933,doi: 10.1016/j.eswa.2023.119911.
10.1016/j.autcon.2023.104933. [54] D. Hummel and A. Maedche, “How effective is nudging? A quan-
[36] B. D. Horne et al., “Behavioral nudges as patient decision sup- titative review on the effect sizes and limits of empirical nudg-
port for medication adherence: The ENCOURAGE randomized con- ing studies,” J. Behav. Exp. Econ., vol. 80, pp.47–58, 2019, doi:
trolled trial,” Am. Heart J., vol. 244, pp.125–134, 2022, doi: 10.1016/j.socec.2019.03.005.
10.1016/j.ahj.2021.11.001. [55] L. Nosrati, A. M. Bidgoli, and H. H. S. Javadi, “Identifying peo-
[37] V. Bagga et al., “Adaptive fusion and transfer learning for enhanced ple’sfacesinsmartbankingsystemsusingartificialneuralnetworks,”
E – commerce recommendations,” Procedia Comput. Sci., vol. 229, Int. J. Comput. Intell. Syst., vol. 17, no. 1, 2024, Art. no. 9, doi:
pp.345–356,2023. 10.1007/s44196-023-00383-7.
[38] C. Almeida, J. Azevedo, A. Fogel, E. Lopes, C. Vale, and P. [56] C.DongandD.Li,“Adaptiveevolutionaryreinforcementlearningwith
Padrão, “Effectiveness of nudge interventions to promote fruit and policydirection,”NeuralProcess.Lett.,vol.56,no.2,pp.1–19,2024,
vegetables’ selection, purchase, or consumption: A systematic re- doi:10.1007/s11063-024-11548-6.
view,” Food Qual. Preference, vol. 116, 2024, Art. no. 105122, doi:
10.1016/j.foodqual.2024.105122.
[39] R. Ranjan, “Behavioural finance in banking and management: A
studyonthetrendsandchallengesinthebankingindustry,”AsianJ.
Econ. Bus. Accounting, vol. 25, no. 1, pp.374–386, Jan. 2025, doi:
10.9734/ajeba/2025/v25i11657.
[40] R.ThalerandC.S,“Nudge:Improvingdecisionsabouthealth,wealth
andhappiness,”AmsterdamLawForum,2008. IDHAKRISTIANAreceivedthebachelor’sdegree
[41] D.Bouneffouf,I.Rish,andC.Aggarwal,“Surveyonapplicationsof (S.Kom)ininformaticsengineeringfromUniver-
multi-armedandcontextualbandits,”inProc.IEEECongr.Evol.Com- sitasKristenDutaWacana,Yogyakarta,Indonesia,
putation,Jul.2020,pp.1–8,doi:10.1109/CEC48606.2020.9185782. themaster’sdegree(MMSI)ininformationsystem
[42] A. H. Sadeghian and A. Otarkhani, “Data-driven digital nudging: managementandthedoctoratedegreeincomputer
A systematic literature review and future agenda,” Behav. Inf. Tech- sciencefromBINUSUniversity,WestJakarta,In-
nol., vol. 43, pp.1–29, Nov. 2023, doi: 10.1080/0144929X.2023. donesia. She was a Lead of data science with
2286535. OCBC Indonesia, where she led end-to-end AI
[43] N.Mota,A.Chakraborty,A.J.Biega,K.P.Gummadi,andH.Heidari, initiatives from problem formulation and model
“On the desiderata for online altruism: Nudging for equitable dona- development to deployment. She is currently the
tions,”Proc.ACMHum.-Comput.Interact.,vol.4,no.CSCW2,2020, FounderandtheCEOofV-TEKI(PTViktoriAk-
Art.no.126,doi:10.1145/3415197. sara Teknologi Indonesia), an AI and data solutions company focusing on
[44] X.Yietal.,“Sampling-bias-correctedneuralmodelingforlargecorpus appliedartificialintelligence,analytics,anddigitaltransformation.Sheisalso
itemrecommendations,”inProc.13thACMConf.Recomm.Syst.,2019, aFacultyMemberwithBINUSOnlineLearning.Sheactivelyengagedasa
pp.269–277,doi:10.1145/3298689.3346996. Researcherofartificialintelligence.Withmorethan16yearsofprofessional
[45] O. M. Omisore et al., “An affective learning-based system for experience,shebridgesacademicresearchandindustrypractice.Herresearch
diagnosis and personalized management of diabetes mellitus,” Fu- interests include AI-driven recommendation systems, behavioral nudging,
ture Gener. Comput. Syst., vol. 117, pp.273–290, 2021, doi: andresponsibleAIforfinancialanddigitalplatforms.
10.1016/j.future.2020.10.035. Shehascontributedtoenterpriseanalyticsandbusinessintelligenceini-
[46] G.ShmueliandA.Tafti,“Howto‘improve’predictionusingbehavior tiatives with Bank Central Asia and Sinarmas Agribusiness and Food (PT
modification,”Int.J.Forecast.,vol.39,no.2,pp.541–555,2023,doi: SMARTTbk),focusingondatawarehousing,OLAPsystems,anddecision-
10.1016/j.ijforecast.2022.07.008. supportplatforms.
VOLUME7,2026 415

KRISTIANAETAL.:VALIDATINGAI-DRIVENNUDGERECOMMENDATIONS:A/BTESTINGTWO-TOWERANDBANDITMODELS
HARJANTO PRABOWO received the first top NUNUNG NURUL QOMARIYAH received the
graduate degree from Electrical Engineering De- S.Kom,M.T.I.,andPh.D.degrees.Sheiscurrently
partment, Diponegoro University, Semarang, In- an Assistant Professor with Bina Nusantara Uni-
donesia,in1988,thesecondtopgraduatedegree versity International, Jakarta, Indonesia. With a
from Information Systems Management Depart- richbackgroundinartificialintelligence,sheisa
ment,BINUSUniversity,WestJakarta,Indonesia, DistinguishedAlumnaoftheUniversityofYork,
in1996,andthedoctoratedegreeinbusinessman- York,U.K.,whereshewasapartoftheArtificial
agementwithaCumLaudedistinctionfromPad- Intelligence Research Group. Her doctoral work
jadjaranUniversity,Bandung,Indonesia,in2005. delvedintopreferencelearningusingDescription
Heheldkeypositions,suchastheHeadwithIn- Logic, laying the groundwork for her future en-
dustrial Engineering Department, the Head with deavors.Shespearheadedgroundbreakingresearch
ManagementDepartment,theDeanwiththeFacultyofComputerScience, in explainable AI within the medical domain, a co-funded project by the
theDirectorofOperations,theDirectorofIT,andtheRectorwithBINUS NewtonBritishCouncilandtheIndonesianMinistryofResearchandEdu-
University from 2009 to 2023. He is currently a Professor of information cation.ThiscollaborationinvolvestheUniversityofYork,BinusUniversity,
systems management with Bina Nusantara University, West Jakarta. He is andPasarMingguRegionalHospital,Jakarta,leadingtonumerousScopus
alsotheVicePresidentwithBINUSHigherEducation.Hisresearchinter- indexedpublications,firstplacewinnerintheMendixcompetition,andlisted
estsincludeITgovernance,strategicalignment,ERPimplementation,digital astheTop20intheOpenInnovationstartupcompetitionbyIMERIUniver-
transformation,andAIimplementationinuniversities,withpublicationsin- sityofIndonesia.
dexed in Scopus from 2006 to 2023. He has an h-index of 13 on Scopus,
with 222 published papers indexed in Scopus and 714 citations in fields
suchasKnowledgeManagement,StrategicInnovation,QualityManagement
Systems, Information Systems, Global Competitive Advantage, and Good
Governance. He is actively involved in various national and international
professionalassociations,contributingtotheadvancementofeducationand
technology.With30yearsofserviceatBINUSUniversity,hehasplayeda
pivotalroleinadvancingtheuniversity’seducationsystem.Heisthefounder
of BINUS Online Learning, the university’s distance education program,
whichcelebrated15yearswithmorethan12000activestudentsin2024.
FORD LUMBAN GAOL(SeniorMember,IEEE)
wasborninJakarta.HereceivedtheB.Sc.degree
(S. Si) in mathematics, the Master of Computer
Science (M. Kom), and the doctorate degree in
computersciencefromtheUniversityofIndone-
sia, Jakarta, Indonesia, in 1997, 2001, and 2009,
respectively. He was the Vice Chair of IEEE In-
donesia Section and the former Chair of ACM
Indonesia, contributing significantly to the ad-
vancement of computer science and technology,
Indonesia.HeiscurrentlyaProfessorofcomputer
sciencewithBinaNusantaraUniversity,WestJakarta,Indonesia.Heisalso
theHeadwiththeDepartmentofDoctorofComputerScience,BinaNusan-
taraUniversity.HeisaResearchFellowwithRCAISIS,AdvancedInstitute
ofIndustrialTechnology,TokyoMetropolitanPublicUniversityCorporation,
Japan, and an Advisory Board Member with Shridhar University, Pilani,
India.HeistheGroupLeaderin"AdvanceSysteminComputationalIntel-
ligence & Knowledge Engineering". He is the also the Chair of the IEEE
IndonesiaSectionComputerSocietyChapterandtheIIAIASEANPresident.
Hewastherecipientofseveralprestigiousinternationalgrants,reflectinghis
extensive research collaborations and contributions to the global academic
community.ThesegrantsincludedfundingfromKazanFederalUniversity
(Russia) in 2015, Vladimir State University (Russia) in 2016, Financial
University under the Government of the Russian Federation in 2017, and
Southern Federal University (Russia) in 2018. These research grants sup-
portedhisworkincomputationalintelligence,knowledgeengineering,and
variousinterdisciplinaryfields,furthersolidifyinghisimpactinacademiaand
research.
416 VOLUME7,2026