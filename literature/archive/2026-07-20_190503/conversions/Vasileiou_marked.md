|     | A   | Logic-based |     |                                       |     | Framework  |     | for      | Explainable     |     |     | Agent |     |
| --- | --- | ----------- | --- | ------------------------------------- | --- | ---------- | --- | -------- | --------------- | --- | --- | ----- | --- |
|     |     |             |     |                                       |     | Scheduling |     | Problems |                 |     |     |       |     |
|     |     |             |     | StylianosLoukasVasileioua;*,BorongXua |     |            |     |          | andWilliamYeoha |     |     |       |     |
aWashingtonUniversityinSt.Louis
Abstract. AgentSchedulingProblems(ASPs)arecommoninvar- queries,whichofferguidanceonrenderinginfeasibleschedulingde-
ious real-world situations, requiring explainable decision-making cisions feasible. Recognizing the importance of privacy in multi-
processes to effectively allocate resources to multiple agents while agentscheduling,weusetheconceptofagentaccessrightstodis-
fostering understanding and trust. To address this need, this paper tinguish between public and private information, and introduce a
presents a logic-based framework for providing explainable deci- straightforwardprivacy-lossfunctiontoquantifytheamountofpri-
sions in ASPs. Specifically, the framework addresses two types of vateinformationdisclosedinexplanations.Usingthisfunction,we
queries:reason-seekingqueries,whichexplainthereasoningbehind thendefinethenotionofprivacy-awareexplanationsandpresentthe
schedulingdecisions,andmodification-seekingqueries,whichoffer Query Understanding and Efficient Response with Intelligible Ex-
guidance on making infeasible decisions feasible. Acknowledging planationsofSchedules(QUERIES)algorithmforcomputingthem.
the importance of privacy in multi-agent scheduling, we introduce This approach ensures that the explanations provided maintain the
a privacy-loss function that measures the disclosure of private in- confidentialityofsensitiveinformationwhilestillofferingvaluable
formation in explanations, enabling a privacy-preserving aspect in insightsintotheschedulingdecisions.
our framework. By using this function, we introduce the notion of In summary, our framework advances existing explainable
privacy-awareexplanationsandpresentanalgorithmforcomputing scheduling methods, which typically focus on specific scheduling
them. Empirical evaluations demonstrate the effectiveness and ver- problems[1,3,28],by providingageneralsolutionapplicabletoa
satilityofourapproach. broaderrangeofASPs.Ourmaincontributionsareasfollows:
Weintroduceagenerallogic-basedexplanationgenerationframe-
•
|     |     |     |     |     |     |     |     | work for | ASPs that | addresses | both | reason-seeking | queries and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --------- | ---- | -------------- | ----------- |
1 Introduction
modification-seekingqueries.
Weproposeaprivacy-lossfunctiontoquantifytheamountofpri-
| Agentschedulingproblems(ASPs)involveallocatingafinitesetof |     |     |     |     |     |     |     | •   |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
vateinformationincludedinanexplanationanddefinetheconcept
resourcestomultipleagentsoveraspecifictimeframe.Theseprob-
ofprivacy-awareexplanations.
| lems | are pervasive | in  | real-world | scheduling |     | systems, | ranging from |     |     |     |     |     |     |
| ---- | ------------- | --- | ---------- | ---------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
WepresenttheQUERIESalgorithmforcomputingexplanations.
| personnelshiftassignments[34]tomachinejoballocation[38],and |     |     |     |     |     |     |     | •   |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Empiricalevaluationsdemonstratetheeffectivenessandversatility
evenschedulingawakeandasleepperiodsforMarsrovers[8].Apart
ofourapproach.
| from | generating | a schedule |     | that allocates | resources |     | to agents, it is |     |     |     |     |     |     |
| ---- | ---------- | ---------- | --- | -------------- | --------- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
crucialtoensurethatboththescheduleandtheunderlyingdecision-
making process are explainable. An agent may require an expla- 2 MotivatingThoughtExperiment
| nation | for why | certain | scheduling | decisions |     | were not | satisfied or |     |     |     |     |     |     |
| ------ | ------- | ------- | ---------- | --------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
Tobetterunderstandthechallengesfacedbyagentschedulingprob-
| why | a schedule | could | not | be generated | at  | all. In such | cases, un- |     |     |     |     |     |     |
| --- | ---------- | ----- | --- | ------------ | --- | ------------ | ---------- | --- | --- | --- | --- | --- | --- |
lemsandtheimportanceofgeneratingeffectiveexplanations,letus
| derstanding |     | the reasons | behind | these | issues | is not only | enlighten- |     |     |     |     |     |     |
| ----------- | --- | ----------- | ------ | ----- | ------ | ----------- | ---------- | --- | --- | --- | --- | --- | --- |
engageinathoughtexperimentinspiredbyasimplifiedversionofthe
ingbutalsonecessaryforrectifyingtheproblem.Additionally,pri-
employeeshiftassignmentproblem[34].Considerascenariobased
vacyplaysasignificantroleduetothesensitivenatureofpersonal
ontheemployeeshiftassignmentproblem[34].Inthisscenario,an
| information |     | that may | be included | in  | ASPs, | such as | agents’ con- |     |     |     |     |     |     |
| ----------- | --- | -------- | ----------- | --- | ----- | ------- | ------------ | --- | --- | --- | --- | --- | --- |
automatedschedulingagentnamedAliceisresponsibleforassign-
| straints   | and  | preferences. | Preserving     |     | privacy | helps protect | individ-  |               |           |      |          |               |                 |
| ---------- | ---- | ------------ | -------------- | --- | ------- | ------------- | --------- | ------------- | --------- | ---- | -------- | ------------- | --------------- |
|            |      |              |                |     |         |               |           | ing shifts to | employees | at a | company. | Specifically, | there are three |
| ual agents | from | potential    | discrimination |     | or      | unauthorized  | access to |               |           |      |          |               |                 |
shifttypes–morning,afternoon,andevening–andfouremployees
theirinformation,fosteringtrustandwillingnesstoparticipateinthe
|     |     |     |     |     |     |     |     | – Thanos, Irene, | Vicky, | and Rose | – who | need to | be assigned shifts |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------ | -------- | ----- | ------- | ------------------ |
schedulingprocess.Therefore,incorporatingexplanationgeneration
modalitieswithprivacy-preservingconsiderationsintoASPsystems overthreedaysfromMondaytoWednesday.
|     |     |     |     |     |     |     |     | The scheduling | problem | consists | of  | the following | domain con- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | -------- | --- | ------------- | ----------- |
ishighlydesirable.
straints:
Toaddressthisneed,thispaperpresentsalogic-basedframework
C Allemployeesmustbeassignedatotaloftwoshifts.
| aimedatmakingASPsexplainable.Theframeworkaccommodates |     |     |     |     |     |     |     | 1 : |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
two types of queries: reason-seeking queries, which clarify why a C : Employeescannotbeassignedmultipleshiftsperday.
2
scheduling decision was (or not) derived, and modification-seeking C : Notwoemployeescanbeassignedthesameshiftthesameday.
3
|     |     |     |     |     |     |     |     | C 4 : Employees | cannot | be assigned | a   | morning | shift right after an |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ----------- | --- | ------- | -------------------- |
∗CorrespondingAuthor.Email:v.stylianos@wustl.edu. eveningshift.

3 Background
Wenowprovidesomebackgroundonthesatisfiability(SAT)prob-
lem,ageneralagentschedulingproblem(ASP)definition,andour
logic-basedrepresentationofthatproblem.
3.1 Satisfiability
|     |     |     |     | We assume | familiarity         |        | with propositional | logic.         | A knowledge | base      |
| --- | --- | --- | --- | --------- | ------------------- | ------ | ------------------ | -------------- | ----------- | --------- |
|     |     |     |     | KB is     | aset ofconstraints, |        | whereeach          | constraintis   | built       | uprecur-  |
|     |     |     |     | sively    | from literals       | (i.e., | variables or       | its negations) | using       | the usual |
logicalconnectives.
Figure1:InstanceofthethoughtexperimentwithAliceandThanos. Satisfiability(SAT)[9]istheprototypicalNP-completeproblem
offindinganassignmentoftruthvaluestovariablesinordertomake
|     |     |     |     | aknowledgebaseKB |     |     | true.Ifthereexistsatruthvalueassignmentµ |     |     |     |
| --- | --- | --- | --- | ---------------- | --- | --- | ---------------------------------------- | --- | --- | --- |
Moreover,eachemployeehaspersonalconstraints:
|     |     |     |     | thatmakesKB |     | true,thenwesaythatµisamodelofKB |     |     |     | andKB is |
| --- | --- | --- | --- | ----------- | --- | ------------------------------- | --- | --- | --- | -------- |
C T : Thanoswantsonlymorningorafternoonshifts. satisfiable,otherwiseKB isunsatisfiable,denotedbyKB = .A
|     |     |     |     |     |     |     |     |     |     | | ⊥ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
C : Irenedoesnotwanteveningshifts. KB entailsaconstraintϕ,denotedKB =ϕ,iffKB ϕ = .
I
|     |     |     |     | Partial | weighted | MaxSAT | [24] is | an | extension | of ∪{¬ SAT | in }| which ⊥ |
| --- | --- | --- | --- | ------- | -------- | ------ | ------- | -------------- | ---------- | ------------- |
C V : VickywantstheafternoonshiftonTue.andWed.
C : RosewantsthemorningshiftonTue.andWed. constraintsarepartitionedintohardandsoftconstraints,whereeach
R
softconstraintsisgivenaweight.Hardconstraintsmustalwaysbe
Here, Alice’s objective is to find a schedule that satisfies all do- satisfiedinasolution,whereassoftconstraintsmaynot.Thegoalof
main constraints and, as much as possible, accommodates the em- MaxSATistofindanassignmentthatsatisfiesthehardclausesand
ployeeconstraintsaccordingtotheirweights,whichinthisexample maximizesthesumofweightsofthesatisfiedsoftclauses.
arebasedontheemployees’senioritylevels.
Let us assume that Alice finds a feasible schedule, but it does 3.2 AgentSchedulingProblem
notmeetThanos’constraintofbeingassignedmorningorafternoon
shifts.Thanos,inturn,mayinquireaboutthereasonforthisassign- Ingeneral,thegoalofanagentschedulingproblem(ASP)istodis-
ment.Togenerateaneffectiveexplanation,Aliceneedsaframework tribute a set of resources to a set of agents over a scheduling hori-
thatcangenerateexplanationsthatareinformativeandtailoredtothe zon.Formally,itcanbedefinedasatuple = A,R,S,C ,where
|     |     |     |     |     | n   |     |     | A m | (cid:104) | (cid:105) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- |
s p e c i fic ne e ds o f t h e e x p l ai n e e , thatis,Alicemustfirstrecognizethe A = a i i = 1 i s a s e t o f a ge n t s , R = r j j = 1 i s a se t o f r e s o u rc e s ,
|     |     |     |     |     | { }h |     |     | { } |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
n a tu r e of th e ex p l a i ne e ’ s q u e r y . S = s t i s a s e t o f ti m e s t e p s, and C i s a s e t of c on s t r a in t s th a t
|     |     |     |     |     | { } t = 1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
In our thought experiment, Thanos’ query is a reason-seeking consistsofdomainconstraints,whichareintrinsicanddescribethe
query,ashewantstoknow“why”hisconstraintwasunsatisfiedin problem’sdynamics,aswellasagentconstraints,whichareextrinsic
the schedule. In response, Alice should provide a (reason-seeking) anddescribetheagents’personalconstraints.
|     |     |     |     |     |     |     | isascheduleΣ,thatisan |     | A   | R S |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
explanationthatidentifiesthereasonsbehindher(scheduling)deci- AsolutiontoanASP
|     |     |     |     |     |     |     | A   |     | |   | |×| |×| | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
sion.Forexample,Alicemightexplainthatduetotheconstraintsof matrix,whereeachcellΣ[i,j,t]=1ifagenta i isassignedresource
theproblemandthehigherprioritygiventothepreferencesofRose r attimesteps andΣ[i,j,t]=0otherwise.Ascheduleisfeasible
|     |     |     |     | j   |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and Vicky, it was not possible to assign Thanos morning shifts on ifallthedomainconstraints,whicharetreatedashardconstraints,
Tuesday or Wednesday without affecting the overall quality of the aresatisfied.Ascheduleisoptimalifitisfeasibleandalltheagent
allocation. constraints,whicharetreatedassoftconstraints,aremaximized.
| However, | providing a reason-seeking | explanation | alone may not |     |     |     |     |     |     |     |
| -------- | -------------------------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
besufficientinallscenarios.SupposeAlicecouldnotcreateafea- 3.3 Logic-basedAgentSchedulingProblems
| sible schedule | at all due to conflicting | constraints. | In this case, a |     |     |     |     |     |     |     |
| -------------- | ------------------------- | ------------ | --------------- | --- | --- | --- | --- | --- | --- | --- |
higher-levelemployee,suchasamanager,maywanttounderstand In this paper, we model an ASP as a logic-based problem, that
A
“how”toadjusttheschedulingproblemtoderiveafeasibleschedule. is, we encode into a set of logical constraints for which satis-
|     |     |     |     | fiability | can be | A decided. | By using an | appropriate | logical | language, |
| --- | --- | --- | --- | --------- | ------ | ---------- | ----------- | ----------- | ------- | --------- |
Thistypeofqueryisamodification-seekingquery,whichrequiresan
explanationthathelpsthemanageridentifyissuespreventingafea- the problem’s dynamics are encoded into a knowledge base KB
siblescheduleandsuggestpotentialmodifications. thatexpressesalltheschedulingconstraintsthatadesiredschedule
Inadditiontoaddressingthesetwotypesofqueries,Alice’sexpla- shouldsatisfy.Specifically,theknowledgebaseKB consistsofdo-
nationsshouldrespecttheprivacyoftheotheremployees.Toachieve mainconstraintsC andagentconstraintsC ,whereC aretreated
|     |     |     |     |                       |     | D   |                                      | A   |     | D   |
| --- | --- | --- | --- | --------------------- | --- | --- | ------------------------------------ | --- | --- | --- |
|     |     |     |     | ashardconstraintsandC |     |     | asweightedsoftconstraints.Assuch,the |     |     |     |
this,Alicecouldonlyrevealinformationaccordingtotheemployees’ A
accessrights.Indoingso,Alicedistinguishesbetweenpublicinfor- schedulingproblemturnsintoaMaxSATproblem,wherethequality
mation(informationthatcanberevealedtoemployeeswithaccess ofafeasiblescheduledependsonthedegreetowhichthesoftclauses
rights)andprivateinformation(informationthatcannotberevealed aresatisfied.Theobjectivefunctionofacandidatescheduleisthen
toemployeeswithoutaccessrights). defined as the sum of weights of satisfied soft constraints, and an
optimalscheduleisthesolutionwiththehighestpossibleobjective
Thisthoughtexperimentdemonstratessomeofthechallengesof
generatingexplanationsinthecontextofagentschedulingproblems. value. A plethora of scheduling problems has been modeled using
Indeed, in Section 4 we present an explanation generation frame- logic-basedapproaches[2,5,10,14,18,21,23,27].
workthatcanhandlethecomplexityoftheproblem,accountforthe For ease of presentation, in this paper we will use propositional
explainee’sneedsandaccessrights,andproduceinformativeexpla- logic to encode ASPs. We formally define a logic-based ASP (L-
ASP)asfollows:
nations.

Figure2:OverviewofOurExplainableLogic-basedAgentSchedulingProblemPipeline.
Definition 1 (L-ASP). An L-ASP is a tuple = A,R,S,KB , Generateinformativeandconciseexplanationsforthetwoquery
|         |     |        |     |     | L (cid:104) | (cid:105) | •      |     |     |     |     |     |
| ------- | --- | ------ | --- | --- | ----------- | --------- | ------ | --- | --- | --- | --- | --- |
| whereKB | =C  | C and: |     |     |             |           | types. |     |     |     |     |     |
|         |     | D ∪ A  |     |     |             |           |        |     |     |     |     |     |
C is the set of domain-specific (hard) constraints. These con- Preservetheprivacyofotheragentsbyonlyrevealinginformation
D
| •   |           |              |             |          |              |      | • withrespecttoaccess-rights. |     |     |     |     |     |
| --- | --------- | ------------ | ----------- | -------- | ------------ | ---- | ----------------------------- | --- | --- | --- | --- | --- |
| str | aints are | intrinsic to | the problem | and must | be satisfied | by a |                               |     |     |     |     |     |
solution. AgeneralpipelineisshowninFigure2.Wenowdescribehowto
C = (cid:83) n C i s t h e se t o f a g en t ( we i gh te d s o f t) c o n st r a i n ts . generateexplanationsforthetwoquerytypes.
| A              | i=   | 1 i     |                             |              |                 |                     |     |     |     |     |     |     |
| -------------- | ---- | ------- | --------------------------- | ------------ | --------------- | ------------------- | --- | --- | --- | --- | --- | --- |
| • Ea           | ch C | w , c i | l , w h er                  | e e ac h c i | is a c o n s tr | a in t a s s o c i- |     |     |     |     |     |     |
|                | i =  | ( k k ) | k= 1                        | k            |                 |                     |     |     |     |     |     |     |
|                | {    | }       |                             |              |                 |                     |     |     |     |     |     |     |
| atedwithagenta |      | i andw  | k isitscorrespondingweight. |              |                 |                     |     |     |     |     |     |     |
4.1 ExplainingReason-SeekingQueries
Aschedulecanbederivedbyusingoff-the-shelfSATsolvers[4]
to search for a model µ of KB that satisfies all of the constraints Areason-seekingquery,denotedbyϕ ,aimstouncoverwhycertain
r
schedulingdecisionsweremade.RecallfromSection2thatThanos
| in C | D and possibly | some | of the constraints |     | in C A . If | a model µ |     |     |     |     |     |     |
| ---- | -------------- | ---- | ------------------ | --- | ----------- | --------- | --- | --- | --- | --- | --- | --- |
exists,thenafeasiblescheduleΣµ isderivedbyextractingfromµthe wants to know why Alice did not assign him only morning shifts.
truthvaluesofthevariablescorrespondingtoagents,resources,and Alternatively,ahigher-levelemployee(e.g.,amanager)maywantto
timesteps.Otherwise,theschedulingproblemisinfeasible,i.e.,no understandwhyafeasibleschedulecannotbegenerated.
feasiblescheduleexists.Finally,ascheduleΣµ isdeemedoptimalif To explain reason-seeking queries, we assume that KB = ϕ .
| r
Therearetwopossiblescenariostoconsider:
amodelµexistsandmaximizesthecumulativesumofweightsof
satisfiedsoftconstraintsinC A . Agent Constraints in a Schedule: If the query ϕ r captures an
•
NotethattheknowledgebaseKB = C C maybeunsatis- unsatisfied (or satisfied) agent constraint in a schedule Σµ , then
D ∪ A
fiableduetoinconsistenciesinthedomainco nstraintsand/oragent ϕ C (orϕ C ).1Inthisscenario,anexplanationshould
|     |     |     |     |     |     |     | r ∈¬ | A r ∈ A |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --- | --- | --- | --- |
constraints.However,ifascheduleΣµ exists,thenthatmeansthat identifythereasonswhytheconstraintholdstruewithrespectto
Σµ logicallyfollowsfromasatisfiablesubsetKB µ KB.Inthe theschedule.NotethattheknowledgebaseKB hereissatisfiable
⊆
nextsection,weuseKB todenotetheknowledgebasefromwhich (seeSection3.3).
explanations are derived. Depending on the context, KB could re- InfeasibleSchedulingProblems:Ifthequeryϕ isaimedatcap-
|     |     |     |     |     |     |     | •   |     |     | r   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fertoeitherasatisfiablesubsetoftheoriginalknowledgebase(i.e., turing why a problem is infeasible, i.e., why a feasible schedule
KB )ortheoverallunsatisfiableknowledgebase. cannotbegenerated,thengenerallyϕ
| µ   |     |     |     |     |     |     |     |     |     | r = .Inthiscase,theex- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- |
⊥
planationshouldidentifytheinconsistencieswithinthescheduling
4 ExplainableAgentSchedulingProblems constraintsthatleadtoinfeasibleschedules.Notethattheknowl-
|     |     |     |     |     |     |     | edgebaseKB | hereisunsatisfiable,i.e.,thereisnomodelofKB |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------------------------------- | --- | --- | --- | --- |
We now present our explanation generation framework for agent fromwhichafeasibleschedulecanbeextracted.
schedulingproblems.Weparticularlyaddressthefollowingproblem:
Formallynow,anexplanationforareason-seekingqueryisdefined
asfollows:
| Givenalogic-basedL-ASP |     |     | =   | A,R,S,KB  | andaqueryϕ |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
|                        |     |     | L   | (cid:104) | (cid:105)  |     |     |     |     |     |     |     |
withrespecttoKB,thegoalistofindanexplanationforϕthat
|     |     |     |     |     |     |     | Definition | 2 (Reason-seeking | Explanation). | Given | a knowledge |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | ------------- | ----- | ----------- | --- |
canbeinferredfromKB.
|     |     |     |     |     |     |     | baseKB | thatencodesanL-ASP | andareason-seekingqueryϕ |     |     | ,   |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------------ | ------------------------ | --- | --- | --- |
r
|                                                       |     |     |     |     |     |     | weconsideranexplanation(cid:15) |     | L KB | tobeareason-seekingexpla- |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | ---- | ------------------------- | --- | --- |
| AsdiscussedinSection2,weareinterestedinaframeworkthat |     |     |     |     |     |     |                                 |     | r    |                           |     |     |
⊆
| cangenerateexplanationsforagentschedulingproblemsthatarenot |     |     |     |     |     |     | nationforϕ | r if: |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | ----- | --- | --- | --- | --- |
only informative but also tailored to the specific needs of the ex- (cid:15) issufficient:(cid:15) = ϕ ,meaningthattheexplanation(cid:15) entails
|                                          |     |     |     |     |     |     | • r       | r | r |     |     | r   |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | --- | --- | --- |
| plainee.Suchaframeworkshouldinprinciple: |     |     |     |     |     |     | thequeryϕ | .     |     |     |     |     |
r
|     |     |     |     |     |     |     | isminimal:Forallpropersubsets(cid:15)(cid:48) |     |     | ,(cid:15)(cid:48) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | ----------------- | --- | --- |
Address two general types of queries: reason-seeking queries, (cid:15) r r (cid:15) r r =ϕ r ,indicating
| •   |     |     |     |     |     |     | •   |     |     | ⊂ (cid:54)| |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
whichaimtouncoverwhycertainschedulingdecisionswere(or thatnosmallersubsetof(cid:15) r aresufficient.
not)made,andmodification-seekingqueries,whichfocusoniden-
tifyingpotentialmodificationstotheproblem. 1Notethat¬CAdenotesthelogicalnegationofalltheconstraintsinCA.

Theseconditionsensurethatthereason-seekingexplanationisboth
| sufficientandminimalinaddressingthequery. |     |     |     |     |     |     |                |          | (cid:88) |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | -------------- | -------- | -------- | --- | --- | --- |
|                                           |     |     |     |     |     |     | ρ i((cid:15))= | (cid:15) | α(a      | ,c) |     | (2) |
|                                           |     |     |     |     |     |     |                | | |−     | i        |     |     |     |
c∈(cid:15)
4.2 ExplainingModification-SeekingQueries
|                                        |     |     |     |                     | Lastly,wedefineanexplanation(cid:15)  |     |                                             |     | i asbeingprivacy-awareinrela- |     |     |     |
| -------------------------------------- | --- | --- | --- | ------------------- | ------------------------------------- | --- | ------------------------------------------- | --- | ----------------------------- | --- | --- | --- |
|                                        |     |     |     |                     | tiontoagenta                          |     | andqueryϕifitincurstheleastprivacylossamong |     |                               |     |     |     |
| Modification-seekingqueries,denotedbyϕ |     |     |     | ,focusonidentifying |                                       | i   |                                             |     |                               |     |     |     |
|                                        |     |     | m   |                     | allpossibleexplanationsEforthequeryϕ: |     |                                             |     |                               |     |     |     |
potentialmodificationstoaschedulingproblemtoaddressspecific
issues.Forexample,Thanosmaywanttoknowhowtoincorporate (cid:15) =argmin ρ i((cid:15)) (3)
i
hisunsatisfiedconstraintinAlice’sschedule,oramanagermayseek (cid:15)∈E
waystoadjusttheschedulingproblemtogenerateafeasiblesched-
ule.
4.4 IllustratingExample
| Toexplainmodification-seekingqueries,weassumethatKB |     |     |     | =   |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:54)|
ϕ m .Specifically,toexplainthesequerytypes,weseektoidentifya ConsidertheemployeeshiftassignmentproblempresentedinSec-
setofconstraintsfromtheknowledgebaseKB that,whenretracted, tion2.Torepresenttheproblemusing(propositional)logic,weem-
KB =ϕ .Likebefore,therearetwopossiblescenariostoconsider: ployBooleandecisionvariablesx foralla A,r R,and
| | m |     |     |     |     |     |     |     | i,j,t |     | i   | j   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
UnsatisfiedAgentConstraintsinaSchedule:Ifthequeryϕ s S,whereeachvariableissettotrueifandonlyifagenta ∈ ∈ is
|     |     |     |     | m   | t   |     |     |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| •   |     |     |     |     | ∈   |     |     |     |     |     |     |     |
concerns accommodating an unsatisfied agent constraint in a assignedshiftr j ondays t .Otherwise,itissettofalse.Thesevari-
scheduleΣµ ,thenϕ C . ablescomprisethedomainconstraintsC D andagentconstraintsC A
|     | m ∈ | A   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
InfeasibleSchedulingProblems:Ifthequeryϕ isaimedatex- whichmakeuptheknowledgebaseKB.Notethatweassumethefol-
m
• plaininghowaproblemcanbemodifiedsuchthatafeasiblesched- lowingweightsforemployeeconstraintsC :w(C R) = w(C V) >
A
|                     |     |       |     |     | w(C T)>w(C |     | I).2 |     |     |     |     |     |
| ------------------- | --- | ----- | --- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- |
| ulecanbefound,thenϕ |     | m = . |     |     |            |     |      |     |     |     |     |     |
(cid:62)
We now define an explanation f or a modification-seeking query as Recall from Section 2 that Alice has generated a schedule (see
follows: Figure1)thatdoesnotsatisfyThanos’constraint,promptinghimto
askAliceareason-seekingquery.Inourlogic-basedframework,this
Definition 3 (Modification-seeking Explanation). Given a knowl- translates to the query ϕ = x x . There are two
|     |     |     |     |     |     |     | r   | {¬  | 1,1,2 ∨¬ | 1,2,2 | }   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- |
reason-seekingexplanationsforthisquery:
| edge base | KB that encodes | an  | L-ASP | and a modification- |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | ----- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
L
seeking query ϕ m , we consider an explanation (cid:15) m KB to be a (cid:15) r1 = x 4,1,2 , x 4,1,2 x 1,1,2 ,statingthatonlyoneemployee
|     |     |     |     | ⊆   | •   | {   | ¬ ∨¬ |     | }   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
modification-seekingexplanationforϕ if: can be assigned a morning shift on the same day (domain con-
m
(cid:15) enablestheentailmentofϕ :KB (cid:15) =ϕ ,meaningthat straint)andthatRose’spreferencewasgivenahigherprioritythat
| m         |                                          | m   | m   | m            |      |     |     |     |     |     |     |     |
| --------- | ---------------------------------------- | --- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- |
| •         |                                          |     | \   | |            | day. |     |     |     |     |     |     |     |
| thequeryϕ | m isentailedwhentheconstraintsin(cid:15) |     |     | m areremoved |      |     |     |     |     |     |     |     |
fromtheknowledgebase. (cid:15) r2 = x 3,2,2 , x 3,2,2 x 1,2,2 ,statingthatonlyoneemployee
|     |     |     |     |     | •   | {   | ¬ ∨¬ |     | }   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
(cid:15) isminimal:Forallpropersubsets(cid:15)(cid:48) (cid:15) ,KB (cid:15)(cid:48) =ϕ , canbeassignedanafternoonshiftonthesameday(domaincon-
| m   |     |     | m   | m m m |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
• indicatingthatnosmallersubsetof(cid:15) cansatisfythequerywhen ⊂ \ (cid:54)| straint)andthatVicky’spreferencewasgivenahigherprioritythat
m
day.
removedfromtheknowledgebase.
Now,assumethattheaccess-rightsfunctionαisdefinedsuchthat
Theseconditionsensurethatthemodification-seekingexplanationis Thanoshasaccess-rightstothedomainconstraintsandRose’scon-
botheffectiveandminimalinaddressingthequery. straints,butnottotheconstraintsofotheragents.Inthiscase,thepri-
|     |     |     |     |     | vacylossρ | ofbothexplanationswouldbecalculatedasfollows: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
1
(cid:80)
|                               |     |     |     |     | ρ 1((cid:15) r1) | = (cid:15) |       | α(1,c) | = 2 2 | = 0,sinceThanoshas |     |     |
| ----------------------------- | --- | --- | --- | --- | ---------------- | ---------- | ----- | ------ | ----- | ------------------ | --- | --- |
| 4.3 Privacy-AwareExplanations |     |     |     |     | •                | |          | r1 |− |        | −     |                    |     |     |
c∈(cid:15)r1
accesstoRose’sinformation.
Itisreasonabletoassumethatindividualsmightpreferexplanations (cid:80)
|     |     |     |     |     | ρ 1((cid:15) r2)= | (cid:15) | r2 α(1,c)=2 |     | 1=1,sinceThanosdoes |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | -------- | ----------- | --- | ------------------- | --- | --- | --- |
forschedulingdecisionsthatonlyencompasspublicinformation,as • | |− −
c∈(cid:15)r2
nothaveaccesstoVicky’sinformation.
theycouldperceivetheseasmoresatisfyingandequitablecompared
toexplanationsthatincorporateprivateinformationaswell.Toex- Asρ 1((cid:15) r1)<ρ 1((cid:15) r2),theprivacy-awareexplanationinthiscase
| plore this possibility | and incorporate |     | potential | privacy preferences | wouldbe(cid:15) | r1 . |     |     |     |     |     |     |
| ---------------------- | --------------- | --- | --------- | ------------------- | --------------- | ---- | --- | --- | --- | --- | --- | --- |
intoourframework,weproposethatagentshaveaccessrightsonthe
differentpiecesofinformationabouttheschedulingproblem.Specif-
5 QUERIES:ComputingExplanations
ically,weassumeanaccess-rightsfunction:
WenowpresenttheQuestionUnderstandingandEfficientResponse
α:A KB 0,1 (1) with Intelligible Explanations of Schedules (QUERIES) algorithm,
|     |     | ×   | →{ } |     |                 |     |               |              |     |               |                |     |
| --- | --- | --- | ---- | --- | --------------- | --- | ------------- | ------------ | --- | ------------- | -------------- | --- |
|     |     |     |      |     | which generates |     | privacy-aware | explanations |     | (cid:15)∗ for | reason-seeking |     |
i
| thatdetermineswhetheranagenta |     |     | Ahasaccessrightstoacon- |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i ∈ and modification-seeking queries ϕ of an agent a i . The core of
| straintc KB,returning1ifa |                | hasaccesstocand0otherwise. |                |                  |                                                           |     |     |     |     |     |     |     |
| ------------------------- | -------------- | -------------------------- | -------------- | ---------------- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                           |                | i                          |                |                  | QUERIESisbasedonreasoningviainconsistency.Inparticular,it |     |     |     |     |     |     |     |
| While ∈ we                | have motivated | access                     | rights through | the lens of pri- |                                                           |     |     |     |     |     |     |     |
leveragesasetofmethodsthataredirectlyapplicabletologic-based
vacy, note that the function can also encode access rights through explanationgenerationproblems,namely,minimalunsatisfiablesets
othermeansaswell(e.g.,securityclearancesandotheradministra- (MUS)andminimalcorrectionsets(MCS)[25,29],bothofwhich
tivecompartmentalizationprotocols).
emergewhenasetofclausesisunsatisfiable.Particularly,anMUS
| Givenanagenta | andthefunctionα,wedefinetheprivacylossρ |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|               | i                                       |     |     | i   |     |     |     |     |     |     |     |     |
ofanexplanation(cid:15)withregardtotheagentasthecountofconstraints 2Formoredetailsontheencoding,pleaserefertothesupplementavailable
athttps://github.com/YODA-Lab/QUERIES.
inaccessibletoit:

6.1 ComputationalEvaluation
Algorithm1:QUERIESAlgorithm
Input:KB,ϕ,a i ,α,k WenowpresentacomputationalevaluationofQUERIESforthefol-
Result:privacy-awareexplanation(cid:15)forϕfora lowingfourqueries,twoforeachquerytype,whereC isanagent’s
|         |       | i   |     |                                  |     |     |     |     | a   |
| ------- | ----- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
| forallc | KB do |     |     | clauseandΣaninfeasibleschedule:3 |     |     |     |     |     |
1 ∈
| ifα(a            | ,c)=1then |     |     |                                                |     |     |     |                |     |
| ---------------- | --------- | --- | --- | ---------------------------------------------- | --- | --- | --- | -------------- | --- |
| 2                | i         |     |     | Reason-seekingquery(agent):WhyisC              |     |     |     | a unsatisfied? |     |
| assignweightktoc |           |     |     | •                                              |     |     |     |                |     |
| 3                |           |     |     | Modification-seekingquery(agent):HowtosatisfyC |     |     |     |                | ?   |
|                  |           |     |     | •                                              |     |     |     |                | a   |
Reason-seekingquery(schedule):WhyisΣinfeasible?
ifϕisareason-seekingquerythen
| 4   |     |     |     | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:15) getMUS(KB,ϕ) Modification-seekingquery(schedule):HowtomakeΣfeasible?
| 5   |     |     |     | •   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
elseifϕisamodification-seekingquerythen ← WeranourexperimentsonaMacBookPromachinecomprising
6
7 (cid:15) getMCS(KB,ϕ) an M1 Max processor with 32GB of memory. The time limit was
←
setto500s.OurimplementationofQUERIESiswritteninPython
8 return(cid:15)
|     |     |     |     | and integrates | calls | to MUS and | MCS oracles | through | the PySAT |
| --- | --- | --- | --- | -------------- | ----- | ---------- | ----------- | ------- | --------- |
toolkit[20].4
can be interpreted as explaining why a set of clauses is unsatisfi- To comprehensively evaluate our approach, we ran three sets of
ablebyidentifyingaminimalsetofconflictingclausesthatcausethe
experiments:(1)Todemonstratethescalabilityofourapproach,we
unsatisfiability.AnMUScanthenbeusedtofindareason-seeking
|     |     |     |     | evaluated | it on our | motivating employee |     | shift assignment | problem |
| --- | --- | --- | --- | --------- | --------- | ------------------- | --- | ---------------- | ------- |
explanation: ofvaryingsize;(2)Todemonstratetheimpactofprivacyoraccess
rights,weevaluatedouralgorithmonthesameschedulingproblem,
Proposition1. GivenaknowledgebaseKB andareason-seeking but agents have varying access rights; and (3) To demonstrate the
| queryϕ ,(cid:15) | =M ϕ isareason-seekingexplanationforϕ |     |     |     |     |     |     |     |     |
| ---------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
r r \{¬ r } r generalityofourapproach,weevaluateditonanSMT-basedencod-
| ifM isanMUSofKB | ϕ   | .   |     |                                    |     |     |     |     |     |
| --------------- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
|                 | ∪{¬ | r } |     | ingofthejob-shopschedulingproblem. |     |     |     |     |     |
PROOF (SKETCH).Theexistenceofareason-seekingqueryϕ im- Experiment 1: Scalability: In this experiment, we vary the scale
r
pliesthatKB =ϕ ,whichinturnimpliesthatKB ϕ = andcomplexityoftheagentschedulingproblembyvaryingthenum-
|     | r   |     | r   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ∪{¬ }| ⊥ berofagents A,resources R,andtimesteps S intheproblem.
| accordingtothedefinitionofentailment.Thatis,thenegationofϕ |     |     | r   |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                            |     |     |     |     | | | | | | |     | |   | |   |
is inconsistent with a set of constraints from KB and, as such, an Specifically, we created 14 random instances, where each instance
MUS M of KB ϕ exists. If ϕ M, then M ϕ has A = 10 iagents, R = 10 iresources,and S = 10time
|     | ∪{¬ r } | ¬ r ∈ | \{¬ r } | | | | ·   | | | | ·   |     | | | |
| --- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- |
is satisfiable and M ϕ = ϕ . Therefore, M ϕ is a steps,withitakingthevalues1,1.5,2,...,7.5.Forthedomaincon-
|     | r   | r   | r   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reason-seekingexplan \ at { io ¬ nfo } rϕ | . \{¬ } (cid:50) straints,weextendedtheonesdescribedinSection2toincludemore
r
agents,shifttypes,andtimesteps,aswellasincludedanadditional
| Similarly, | an MCS explains | how to restore consistency | in an in- |     |     |     |     |     |     |
| ---------- | --------------- | -------------------------- | --------- | --- | --- | --- | --- | --- | --- |
consistentKBbyidentifyingaminimalsetofclausesfromKBsuch constraintdescribingthemaximumnumberofconsecutiveshiftsan
thatwhenremoved,KBbecomessatisfiable.Amodification-seeking employeecanundertakewithoutadayoff.Fortheagentconstraints,
explanationcanbethenbegeneratedviaanMCS: wegenerated5typesofconstraintstoreflectdifferentkindsofprefer-
encessimilartothosepresentedinSection2,andrandomlyassigned
Proposition 2. Given a knowledge base KB and a modification- themtotheagents.Wesetthefractionp = 0.5ofagentsthateach
| seekingqueryϕ | ,C isamodification-seekingexplanationforϕ |     |     |     |     |     |     |     |     |
| ------------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
m m agenthasaccessrightsto.Ifanagenta i hasaccessrightstoagent
ifCisanMCSofKB ϕ m andϕ m C. a j ,thena i isawareofallofagenta j ’sconstraints.
|     | ∪{ } | (cid:54)∈ |     |     |     |     |     |     |     |
| --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
Figures3(a)and3(b)plottheruntimesofQUERIESasafunction
The proof of Proposition 2 follows from the fact that a of the cardinalities of the knowledge base KB and the explana-
| |
modification-seekingexplanationforϕ isindeedanMCSofKB tion (cid:15) found,respectively.Unsurprisingly,t heru ntimesincreaseas
|     |     | m   | ∪   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ϕ . |     |     |     | | | |     |     |     |     |     |
{ m } thec ar dinalitiesincrease.Thereasonisthatthesearchspacegrows
Algorithm1presentsthepseudocodeofQUERIES,whichgener-
|     |     |     |     | with KB | ,alsoreflectedin | (cid:15).Also,modification-seekingqueries |     |     |     |
| --- | --- | --- | --- | ------- | ---------------- | ----------------------------------------- | --- | --- | --- |
atesexplanationsforanagenta .Atahighlevel,ititeratesoverall | | | |
i tookl onge rtosolvethanreas o n-seekingqueries.Thereasonisthat
constraintsinKB andassignslargeweightsk >> 1toconstraints ouroff-the-shelfMCSsolver,usedformodification-seekingqueries,
thatarepublictoagenta i withrespecttoaccess-rightsfunctionα. islessefficientthanouroff-the-shelfMUSsolver,usedforreason-
| Then,theMUS(orMCS)solverprioritizestheconstraintswiththe |     |     |     | seekingqueries. |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
largestweights,whichmeansthattheoutputofthesolverisasetof
constraintswiththelargestcumulativesumofweights(i.e.,privacy- Experiment2:AccessRights:Inthisexperiment,weusethesame
|     |     |     |     | employee | shift assignment | problem, | where | we set | the number of |
| --- | --- | --- | --- | -------- | ---------------- | -------- | ----- | ------ | ------------- |
awareexplanation).
|                  |            |                        |         | agents A           | = 40,resources | R                     | = 40,andtimesteps |                       | S = 5.We |
| ---------------- | ---------- | ---------------------- | ------- | ------------------ | -------------- | --------------------- | ----------------- | --------------------- | -------- |
| The completeness | of QUERIES | lies in the assumption | we made |                    |                |                       |                   |                       |          |
|                  |            |                        |         | varythefractionp | | |              | = 0,0.1,0.2,...,1 | | |                   | ofotheragentsthateach | | |      |
forthetwoquerytypes,whichisthatanexplanationforbothquery
|     |     |     |     |     |     | {   | }   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
types always exists. The correctness of QUERIES lies in the cor- agenthasaccessrightsto.
rectnessoftheMUSandMCSsolversandtheassumptionthatkis Figures 4(a), 4(b), and 4(c) plot, as a function of access rights
|     |     |     |     | fraction | p, the runtimes | of QUERIES, | privacy | losses | ρ i((cid:15)) of ex- |
| --- | --- | --- | --- | -------- | --------------- | ----------- | ------- | ------ | -------------------- |
sufficientlylargesuchthatexplanationswiththelargestcumulative
|     |     |     |     | planations,andcardinalityofexplanations |     |     |     | (cid:15),respectively.Similar |     |
| --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | ----------------------------- | --- |
sumofweightsareprivacy-awareexplanations.
|     |     |     |     | tothepreviousexperiment,theruntimesarelargerformodification- |     |     |     | | | |     |
| --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- |
3 Ca wasrandomlyselectedfromapoolofunsatisfiedclausesofagenta
6 EmpiricalEvaluations
andΣwasgeneratedbyrandomlyflipping20%ofthevaluesofafeasible
schedule.
| Wenowempiricallyevaluateourapproachbothinsimulatedcompu- |     |     |     | 4            |                 |              |     |                          |     |
| -------------------------------------------------------- | --- | --- | --- | ------------ | --------------- | ------------ | --- | ------------------------ | --- |
|                                                          |     |     |     | The          | code repository | is available | at  | https://github.com/YODA- |     |
| tationalexperimentsaswellasinahumanuserstudy.            |     |     |     | Lab/QUERIES. |                 |              |     |                          |     |

|     |     |         | Why(agent)                    |     |        |         |      | Why(agent)                  |     |             |     |     |
| --- | --- | ------- | ----------------------------- | --- | ------ | ------- | ---- | --------------------------- | --- | ----------- | --- | --- |
|     |     | 102     | How(agent)                    |     |        |         | 102  | How(agent)                  |     |             |     |     |
|     |     |         | Why(schedule)                 |     |        |         |      | Why(schedule)               |     |             |     |     |
|     |     | 101     | How(schedule)                 |     |        |         | 101  | How(schedule)               |     |             |     |     |
|     |     | )s(emiT |                               |     |        | )s(emiT |      |                             |     |             |     |     |
|     |     | 100     |                               |     |        |         | 100  |                             |     |             |     |     |
|     |     | 10−1    |                               |     |        |         | 10−1 |                             |     |             |     |     |
|     |     | 10−2    |                               |     |        |         | 10−2 |                             |     |             |     |     |
|     |     | 103     | 104                           | 105 | 106    |         | 100  |                             | 101 |             |     |     |
|     |     |         | CardinalityoftheKnowledgeBase |     | | KB | |         |      | CardinalityoftheExplanation |     | || (cid:15) |     |     |
|     |     |         |                               | (a) |        |         |      |                             | (b) |             |     |     |
Figure3:ResultsofExperiment1ontheScalabilityofQUERIES
| 35  |     |     |     |     |     |     |            |     |          | 45    |     |            |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ----- | --- | ---------- |
|     |     |     |     | 20  |     |     | Why(agent) |     |          |       |     | Why(agent) |
| 30  |     |     |     |     |     |     | How(agent) |     | (cid:15) | || 40 |     | How(agent) |
Why(agent) Why(schedule) noitanalpxEehtfoytilanidraC Why(schedule)
| 25  |     |     |     |     |     |     |     |     |     | 35  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
How(agent) )(cid:15)(ρssoLycavirP 15 How(schedule) How(schedule)
Why(schedule)
| )s(emiT 20 |     |     |     |     |     |     |     |     |     | 30  |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
How(schedule)
|     |     |     |     | 10  |     |     |     |     |     | 25  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
15
| 10  |     |     |     |     |     |     |     |     |     | 20  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5
| 5   |     |     |     |     |     |     |     |     |     | 15  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   |     |     |     |     | 0   |     |     |     |     | 10  |     |     |
0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0
|     |     | p   |     |     |     | p   |     |     |     |     | p   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (a) |     |     |     | (b) |     |     |     |     | (c) |     |
Figure4:ResultsofExperiment2ontheImpactofPrivacyandAccessRights
Why(agent)
How(agent)
|     |     | 102 |     |     |     |     | 102 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Why(schedule)
How(schedule)
|     |     | 101     |     |     |     |         | 101 |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     |     | )s(emiT |     |     |     | )s(emiT |     |     |     |     |     |     |
|     |     | 100     |     |     |     |         | 100 |     |     |     |     |     |
Why(agent)
How(agent)
|     |     | 10−1 |     |     |     |     | 10−1 |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Why(schedule)
How(schedule)
|     |     |     | 103                           |     | 104    |     |     |                             | 102 |             |     |     |
| --- | --- | --- | ----------------------------- | --- | ------ | --- | --- | --------------------------- | --- | ----------- | --- | --- |
|     |     |     | CardinalityoftheKnowledgeBase |     | | KB | |     |     | CardinalityoftheExplanation |     | || (cid:15) |     |     |
|     |     |     |                               | (a) |        |     |     |                             | (b) |             |     |     |
Figure5:ResultsofExperiment3onSMT-basedEncodingofJob-ShopScheduling
seeking queries than reason-seeking queries. However, unlike the on a Satisfability Modulo Theory (SMT) encoding of the job-shop
previous experiment, there is a significant difference in (cid:15) for the scheduling problem [30]. SMT is a decision problem that extends
| |
different queries in this experiment. As the modification-seeking Boolean logic and allows for richer representations of real-world
queriesrequiredlongerexplanations,theytooklongertosolvethan problemswithlogicalformulaethatarebasedonacombinationof
reason-seekingqueries. backgroundtheoriessuchasintegersandreals[13].
Additionally,theruntimesstayrelativelyconstantforallvaluesof Thejob-shopschedulingprobleminvolvesassigningasetofjobs,
p,reflectingthefactthattheruntimesfortheMCSandMUScom- eachwithitsownprocessingtime,tomachinesinawaythatensures
putationsareindependentoftheweightsoftheclauses.Also,asex- all jobs are completed. We encoded this problem in Python using
pected,theprivacylossdecreasesaspincreasessincefewerclauses theZ3solver[12],andgenerated11instancesbyvaryingthenum-
areprivateaspincreases.Finally,aspincreases, (cid:15) eitherdecreases berofjobs,processingtimes,andmachines.FortheMUSandMCS
| |
orremainsconstant,indicatingthatthesolvercanfindshorter(i.e., solvers,weusedoff-the-shelfimplementationsavailablewithinZ3.
better)explanationswhentheexplanationspaceexpandswithlarger Similartothepreviousexperiment,wegeneratedquerieswithanun-
| valuesofp. |     |     |     |     |     |     | satisfiedconstraintandaninfeasibleschedule. |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
Figures5(a)and5(b)plottheruntimesofQUERIESasafunction
Experiment3:SMTandJob-ShopScheduling:Finally,todemon- of the cardinalities KB and (cid:15), respectively. We observed trends
|     |     |     |     |     |     |     |     |     | |   | | | | |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
stratethatourexplainableschedulingframeworkandalgorithmcan similar to those in Experiment 1, attributable to the same reasons
begeneralizedtootherschedulingproblemsaswellasothertypes describedearlier."
| of logic aside | from | propositional | logic, we | evaluate | our approach |     |     |     |     |     |     |     |
| -------------- | ---- | ------------- | --------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |

|     |     |     |     |     |     |     |     | be included, | while | the remaining |     | participants | (12%) | suggested | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ------------- | --- | ------------ | ----- | --------- | --- |
combinationofbothpublicandprivateinformation.
Inconclusion,ourstudysupportsthehypothesisthatindividuals
preferexplanationscontainingonlypublicinformation,whichthey
perceiveasnotonlymoresatisfactorybutalsomoreequitable..Based
onthesefindings,ourexplanationgenerationframeworkisdesigned
toalignwithpeople’sexpectationsforaschedulingdecisionexpla-
nationinthisparticularcontext.
|           |               |            |         |               |           |               |            | 7 RelatedWork |     |     |     |     |     |     |     |
| --------- | ------------- | ---------- | ------- | ------------- | --------- | ------------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| Figure 6: | Human         | user study | results | from          | 60 users: | (a)           | Percentage |               |     |     |     |     |     |     |     |
| of users  | that selected | generic    | and     | privacy-aware |           | explanations; | and        |               |     |     |     |     |     |     |     |
Thereisasmallbodyofliteratureonexplainablescheduling,with
(b)Percentageofusersthatweresatisfied,indifferent,orunsatisfied
EXPRES[28]beingthemostrelevantrelatedwork.ItusesaMILP
withtheprivacy-awareexplanation.
tofindexplanationsforunsatisfieduserpreferences.Nevertheless,it
|     |     |     |     |     |     |     |     | is limited | to only | identifying | a set | of reasons | for | unsatisfied | user |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | ----- | ---------- | --- | ----------- | ---- |
6.2 HumanUserStudy
|        |         |              |       |              |     |                 |     | preferences,      | thus | lacking | the ability | to address | and      | explain | other   |
| ------ | ------- | ------------ | ----- | ------------ | --- | --------------- | --- | ----------------- | ---- | ------- | ----------- | ---------- | -------- | ------- | ------- |
| We now | present | a user study | aimed | at examining |     | the assumptions |     |                   |      |         |             |            |          |         |         |
|        |         |              |       |              |     |                 |     | types of queries, |      | such as | how (or     | why) a     | schedule | can be  | (or is) |
madeinourframework.Inparticular,wehypothesize: (in)feasible. With regards to privacy, EXPRES preserves privacy
|     |     |     |     |     |     |     |     | by post-processing |     | explanations | to  | remove | identifying | reference | to  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------ | --- | ------ | ----------- | --------- | --- |
Within agent scheduling problems, individuals prefer expla- agents. In contrast, we give a more thorough treatment on this is-
nations containing only public information (e.g., publicly ac- sueaswefoundthatitiskeytousersinouruserstudy.Onasim-
knowledgedrulesandconstraints)overthoseincludingprivate et al.
|             |        |       |            |       |     |          |      | ilar thread, | Cyras | [11] | proposed | an  | argumentation-based |     | ap- |
| ----------- | ------ | ----- | ---------- | ----- | --- | -------- | ---- | ------------ | ----- | ---- | -------- | --- | ------------------- | --- | --- |
| information | (e.g., | other | employees’ | names | and | personal | con- |              |       |      |          |     |                     |     |     |
proachforexplainingwhyascheduleis(ornot)feasibleandwhya
straints),astheyperceivethemasmoresatisfactory.
preferencewasunsatisfiedintheschedule,aswealsotackleinthis
|     |     |     |     |     |     |     |     | paper. The | key differences |     | between | their approach |     | and ours | is that |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | ------- | -------------- | --- | -------- | ------- |
To evaluate this hypothesis, we conducted a human user study in- theydonotconsideranyprivacypreservationstrategies,theyarere-
volving 60 English-speaking participants recruited through the on- strictedtomakespanschedulingproblems,andtheydidnotprovide
| line platform | Prolific | [26]. | The study | is  | centered | around | the em- |                  |     |            |          |           |          |         |     |
| ------------- | -------- | ----- | --------- | --- | -------- | ------ | ------- | ---------------- | --- | ---------- | -------- | --------- | -------- | ------- | --- |
|               |          |       |           |     |          |        |         | any experimental |     | evaluation | of their | approach. | Finally, | Agrawal | et  |
ployeeshiftassignmentproblemintroducedearlier,withparticipants
al.[1]andBertoluccietal.[3]alsoconsidertheproblemofexplain-
| engaging | in a thought | experiment |     | by assuming |     | the role | of an em- |     |     |     |     |     |     |     |     |
| -------- | ------------ | ---------- | --- | ----------- | --- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingschedulingdecisions,however,theirscopeislimitedtospecific
ployeeinahypotheticalcompany.
domainapplications–schedulingMarsroversandoperatingrooms,
| We informed     |             | the participants    | that          | Alice,   | an automated |                  | schedul-  | respectively. |          |      |                |            |           |           |        |
| --------------- | ----------- | ------------------- | ------------- | -------- | ------------ | ---------------- | --------- | ------------- | -------- | ---- | -------------- | ---------- | --------- | --------- | ------ |
| ing agent,was   | responsible |                     | for creatinga |          | schedule     | under            | theprevi- |               |          |      |                |            |           |           |        |
|                 |             |                     |               |          |              |                  |           | A related     | research | area | is explainable |            | planning, | which     | has a  |
| ously described |             | domain constraints, |               | ensuring | that         | this information |           |               |          |      |                |            |           |           |        |
|                 |             |                     |               |          |              |                  |           | larger body   | of work. | Most | of the         | approaches | in        | this area | aim at |
waspublicandknowntoallusers.Participantswereaskedtochoose
|     |     |     |     |     |     |     |     | explaining | planning-specific |     | queries, | such | as why | a plan | is feasi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | -------- | ---- | ------ | ------ | --------- |
apersonalconstraintfromfouravailableoptions,makingthemaware
|     |     |     |     |     |     |     |     | ble/optimal | and why | a particular |     | action is | (or not) | included | in a |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------------ | --- | --------- | -------- | -------- | ---- |
ofonlytheirownpersonalconstraint,whiletheremainingagentcon- plan[7,16,31,32,37,39].CloselyrelatedistheworkbyVasileiou
| straints were | considered | private | information. |     | The | participants | then |     |     |     |     |     |     |     |     |
| ------------- | ---------- | ------- | ------------ | --- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
etal.[35],whichalsousesminimalcorrectionsets(MCS)andmini-
receivedtheirshiftassignments,andwerenotifiedthattheirpersonal
malunsatisfiablesets(MUS)tofindexplanations.However,thekey
constraintwasnotsatisfiedinAlice’sschedule.
differencesbetweentheirapproachandoursisthattheydonotcon-
| Their primary |     | task was | to select | an explanation |     | out | of two op- |               |              |     |          |        |                 |     |           |
| ------------- | --- | -------- | --------- | -------------- | --- | --- | ---------- | ------------- | ------------ | --- | -------- | ------ | --------------- | --- | --------- |
|               |     |          |           |                |     |     |            | sider privacy | preservation |     | and they | take a | philosophically |     | different |
tions: a generic explanation, which contained another employee’s approachoffindingexplanationsbyreconcilingthedifferencesbe-
nameandprivateconstraintasthereasonfortheirunsatisfiedcon-
tweenthementalmodelsoftheexplainerandexplainee.Finally,for
straint,andaprivacy-awareexplanation,whichincludedonlyapub-
|            |             |              |     |      |          |           |       | a further exposition |     | on the | relationship | between | our | approach | and |
| ---------- | ----------- | ------------ | --- | ---- | -------- | --------- | ----- | -------------------- | --- | ------ | ------------ | ------- | --- | -------- | --- |
| lic domain | constraint. | Participants |     | then | answered | questions | about |                      |     |        |              |         |     |          |     |
previousworkssuchasdiagnosisandMUSgeneration,wereferthe
theirchoiceofexplanationandtheirsatisfactionlevels.
readertotheworkbyVasileiouetal.[35,36].
| Figure | 6 presents | the | main results | of  | the study. | The | majority |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ------------ | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(83.4%)ofparticipantspreferredtheprivacy-awareexplanation(Fig-
ure 6(a)). Among those who chose the privacy-aware explanation, 8 Discussion
54%weresatisfied,whiletheremainingparticipantswereeitherin-
different(22%)orunsatisfied(24%),asshowninFigure6(b).Inthe Privacy:Despiteoptimizingforprivacy,explanationsmaystillcon-
analysisofresponsestothejustificationquestion,i.e.,“whytheyse- tain private constraints with respect to the explainee. As such, pri-
lectedtheparticularexplanation”,weobservedacommontrend:the vacy leakage can occur when these explanations are relayed to the
privacy-aware explanation was considered more “informative” and explainee.Toaddressthisissueandpreservetheagents’privacy,we
“equitable” to all employees. Here, informative meant that it con- canpost-processtheexplanationbyabstractingawaytheremaining
tained well-justified rules (i.e., constraints known to them), while private constraints. This process can take different forms, such as
“equitable”impliedthatitwasnotpersonalinthesensethatitdidnot maskingallidentifyingreferencestotheagents’whoseprivatecon-
discloseotheremployees’information.Finally,whenaskedwhether straintsareincludedintheexplanationorbycompletelyretracting
anexplanationforaschedulingdecisionshouldincludeonlypublic theprivateconstraintsfromtheexplanation.
information,onlyprivateinformation,oracombinationofboth,the As an example, consider that Thanos has no access rights to
vastmajority(88%)respondedthatonlypublicinformationshould any of the agent constraints. Then, the reason-seeking explanation

(cid:15) = x , x x that is generated for him unfor- Acknowledgments
| r {      | 4,1,2 ¬  | 4,1,2 ∨¬ | 1,1,2    | }           |            |     |         |     |     |     |     |     |     |
| -------- | -------- | -------- | -------- | ----------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| tunately | includes | Rose’s   | identity | and private | constraint |     | (= x ). |     |     |     |     |     |     |
4,1,2
ThisresearchispartiallysupportedbytheNationalScienceFounda-
| Post-processing |     | (cid:15) r will | allow | us to retract | x   | 4,1,2 from | (cid:15) r and |     |     |     |     |     |     |
| --------------- | --- | --------------- | ----- | ------------- | --- | ---------- | -------------- | --- | --- | --- | --- | --- | --- |
tionunderawards1812619and2232055.Theviewsandconclusions
| mask the | identity     | of Rose | from            | the remaining |            | clause | x 4,1,2  |                                                         |     |     |     |     |     |
| -------- | ------------ | ------- | --------------- | ------------- | ---------- | ------ | -------- | ------------------------------------------------------- | --- | --- | --- | --- | --- |
|          |              |         |                 |               |            |        | ¬ ∨      | containedinthisdocumentarethoseoftheauthorsandshouldnot |     |     |     |     |     |
| x ,      | for example, |         | by transforming |               | the clause | to its | general- |                                                         |     |     |     |     |     |
¬ 1,1,2 be interpreted as representing the official policies, either expressed
| ized form | atmost | 1( x | ,x  | ,x  | ,x  | )   | (do- |     |     |     |     |     |     |
| --------- | ------ | ---- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
{ 1,j,t 2,j,t 3,j,t 4,j,t } ∀rj∈R,st∈S orimplied,ofthesponsoringorganizations,agencies,ortheUnited
| mainconstraintC |     | ).  |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3
Statesgovernment.
| Explanation | Delivery: |     | After the | (potential) | abstraction |     | phase, the |     |     |     |     |     |     |
| ----------- | --------- | --- | --------- | ----------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
(post-processed)explanationneedstobecommunicatedtotheagent.
References
Unlesstheexplaineeagentisadomainexpert,theexplanationshould
|                     |     |     |              |                 |     |     |             | [1] Jagriti | Agrawal, | Amruta | Yelamanchili, | and Steve | Chien, ‘Using ex- |
| ------------------- | --- | --- | ------------ | --------------- | --- | --- | ----------- | ----------- | -------- | ------ | ------------- | --------- | ----------------- |
| not be communicated |     |     | in a logical | representation, |     | but | rather in a |             |          |        |               |           |                   |
plainableschedulingfortheMars2020rovermission’,arXivpreprint
human-understandableformatsuchasnaturallanguage.Atrivialdi-
arXiv:2011.08733,(2020).
rectioncouldbetoleveragetheexpressivityandsymbolicnatureof [2] CarlosAnsótegui,MiquelBofill,MiquelPalahí,JosepSuy,andMa-
logic.Thatis,wecandefinenaturallanguagetemplatesandusethem teuVillaret,‘Satisfiabilitymodulotheories:Anefficientapproachfor
theresource-constrainedprojectschedulingproblem’,inProceedings
tomapthegeneratedexplanations.Inparticular,noticethateachcon-
|                      |     |     |          |            |          |             |     | of the | Symposium | on Abstraction, |     | Reformulation | and Approximation |
| -------------------- | --- | --- | -------- | ---------- | -------- | ----------- | --- | ------ | --------- | --------------- | --- | ------------- | ----------------- |
| straint “symbolizes” |     | a   | specific | constraint | type and | is grounded | on  |        |           |                 |     |               |                   |
(SARA),pp.2–9,(2011).
(propositional) variables, with each variable denoting a scheduling [3] Riccardo Bertolucci, Carmine Dodaro, Giuseppe Galatà, Marco
element such as an agent, a resource, or a time step. For instance, Maratea,IvanPorro,andFrancescoRicca,‘ExplainingASP-basedop-
(cid:15) = x , x x saysthatRoseisassignedthemorn- eratingroomschedules’,inProceedingsoftheWorkshoponExplain-
| r 4,1,2             |     | 4,1,2 | 1,1,2                                  |     |     |     |     |                                                |     |     |     |     |     |
| ------------------- | --- | ----- | -------------------------------------- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
| {                   | ¬   | ∨¬    | }                                      |     |     |     |     | ableLogic-BasedKnowledgeRepresentation,(2021). |     |     |     |     |     |
| ingshiftonTuesday(x |     |       | 4,1,2 ),andthateitherRoseorThanoscanbe |     |     |     |     |                                                |     |     |     |     |     |
[4] ArminBiere,MarijnHeule,HansvanMaaren,andTobyWalsh,Hand-
assignedamorningshiftonTuesday( x 4,1,2 x 1,1,2 ).Assuch, bookofSatisfiability,volume336,IOSpress,2021.
|     |     |     |     | {¬  | ∨¬  | }   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
alogic-basedexplanationcanbetransformedintoanaturallanguage [5] MiquelBofill,MarcGarcia,JosepSuy,andMateuVillaret,‘MaxSAT-
explanation by identifying and mapping the constraints to their re- basedschedulingofB2Bmeetings’,inProceedingsoftheInternational
spectivepre-defined,naturallanguagetemplates.Anotherpossibility ConferenceonIntegrationofAIandORTechniquesinConstraintPro-
gramming(CPAIOR),pp.65–73,(2015).
istoleverageLargeLanguageModels(LLMs)[6]totranslatelogical [6] RishiBommasani,DrewAHudson,EhsanAdeli,RussAltman,Simran
explanations into natural language. However, the accuracy of such Arora,SydneyvonArx,MichaelSBernstein,JeannetteBohg,Antoine
translationswillneedtobevalidatedthroughadditionalresearchas Bosselut, Emma Brunskill, et al., ‘On the opportunities and risks of
LLMs have been shown to have hallucination issues [40]. Another foundationmodels’,arXivpreprintarXiv:2108.07258,(2021).
|     |     |     |     |     |     |     |     | [7] Tathagata | Chakraborti, | Sarath | Sreedharan, | Yu Zhang, | and Subbarao |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | ------ | ----------- | --------- | ------------ |
approachisthroughvisualizationsystems[22,33],thoughthesesys-
|     |     |     |     |     |     |     |     | Kambhampati, |     | ‘Plan explanations |     | as model reconciliation: | Moving |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------------ | --- | ------------------------ | ------ |
temswilllikelyneedtobecraftedwithsignificantdomainexpertise. beyond explanation as soliloquy’, in Proceedings of the Interna-
tionalJointConferenceonArtificialIntelligence(IJCAI),pp.156–163,
| Ethical | Considerations: |     | It is paramount |     | to assess | the | ethical im- |     |     |     |     |     |     |
| ------- | --------------- | --- | --------------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
(2017).
[8] WayneChi,SteveChien,andJagritiAgrawal,‘Schedulingwithcom-
| plications | of our | work. | In our | context, | two ethical | considerations |     |     |     |     |     |     |     |
| ---------- | ------ | ----- | ------ | -------- | ----------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
plexconsumptiveresourcesforaplanetaryrover’,inProceedingsof
emerge–theexplanationunavoidablyinvolvesprivateinformation,
theInternationalConferenceonAutomatedPlanningandScheduling
| and the | fair resolution |     | of conflicting | agent | constraints. |     | The former |     |     |     |     |     |     |
| ------- | --------------- | --- | -------------- | ----- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- |
(ICAPS),pp.348–356,(2020).
| concern | can be | addressed | by the | post-processing |     | mechanisms | de- |             |       |                 |     |                 |                 |
| ------- | ------ | --------- | ------ | --------------- | --- | ---------- | --- | ----------- | ----- | --------------- | --- | --------------- | --------------- |
|         |        |           |        |                 |     |            |     | [9] Stephen | Cook, | ‘The complexity | of  | theorem-proving | procedures’, in |
scribedabove.Forthelatter,whilewedonotaddresstheissuedi- ACM Symposium on Theory of Computing (STOC), pp. 151–158,
(1971).
| rectly in | our work, | we  | imagine | that fairness | could | be achieved | by  |                                                                  |     |     |     |     |     |
| --------- | --------- | --- | ------- | ------------- | ----- | ----------- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
|           |           |     |         |               |       |             |     | [10] JamesCrawfordandAndrewBaker,‘Experimentalresultsontheappli- |     |     |     |     |     |
employingmulti-objectiveoptimizationtechniques[15,17,19]that
cationofsatisfiabilityalgorithmstoschedulingproblems’,inProceed-
seekabalanceamongconflictingconstraints.
ingsoftheNationalConferenceonArtificialIntelligence(AAAI),pp.
1092–1097,(1994).
Althoughourcurrentframeworkdoesnotpresentdefinitivesolu- [11] Kristijonas Cyras, Dimitrios Letsios, Ruth Misener, and Francesca
tionstothesecomplexissues,thesepotentialdirectionscouldguide Toni, ‘Argumentation for explainable scheduling’, in Proceedings of
the future trajectory of research in this field. Subsequent iterations theAAAIConferenceonArtificialIntelligence(AAAI),pp.2752–2759,
(2019).
shouldintegratetheseconsiderations,workingtowardsnotjustprac- [12] Leonardo De Moura and Nikolaj Bjørner, ‘Z3: An efficient SMT
ticalbutalsoethicallyrobustAIexplanationsystems. solver’,inProceedingsofInternationalConferenceonToolsandAl-
gorithmsfortheConstructionandAnalysisofSystems(TACAS),pp.
337–340,(2008).
|     |     |     |     |     |     |     |     | [13] LeonardoDeMouraandNikolajBjørner,‘Satisfiabilitymodulothe- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
9 Conclusions ories: introduction and applications’, Communications of the ACM,
54(9),69–77,(2011).
|     |     |     |     |     |     |     |     | [14] EmirDemirovic´,NysretMusliu,andFelixWinter,‘Modelingandsolv- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
Inthispaper,wetackledthechallengeofgeneratingexplanationsfor ingstaffschedulingwithpartialweightedMaxSAT’,AnnalsofOpera-
tionsResearch,275,79–99,(2019).
| agent scheduling |     | problems. | We  | proposed | a logic-based |     | framework |                                                                 |     |     |     |     |     |
| ---------------- | --- | --------- | --- | -------- | ------------- | --- | --------- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                  |     |           |     |          |               |     |           | [15] MichaelEmmerichandAndréDeutz,‘Atutorialonmultiobjectiveop- |     |     |     |     |     |
capableofgeneratingprivacy-awareexplanationsforreason-seeking
timization:Fundamentalsandevolutionarymethods’,NaturalComput-
andmodification-seekingqueries.Tothebestofourknowledge,our
ing,17(3),585–609,(2018).
| framework | is the | first to | present | a general | approach | that | tackles a |                                                               |     |     |     |     |     |
| --------- | ------ | -------- | ------- | --------- | -------- | ---- | --------- | ------------------------------------------------------------- | --- | --- | --- | --- | --- |
|           |        |          |         |           |          |      |           | [16] MariaFox,DerekLong,andDanieleMagazzeni,‘Explainableplan- |     |     |     |     |     |
broadspectrumofagentschedulingproblemswhilequantifyingand ning’,arXivpreprintarXiv:1709.10256,(2017).
|     |     |     |     |     |     |     |     | [17] NyomanGunantara,‘Areviewofmulti-objectiveoptimization:Meth- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
optimizingforprivacy.Ourexperimentalresultsdemonstratetheef-
odsanditsapplications’,CogentEngineering,5(1),1502242,(2018).
ficacyofourframework,andouruserstudysupportstheimportance
|             |           |     |                 |     |                |     |            | [18] Stefaan | Haspeslagh, | Tommy | Messelis, | Greet | Vanden Berghe, and |
| ----------- | --------- | --- | --------------- | --- | -------------- | --- | ---------- | ------------ | ----------- | ----- | --------- | ----- | ------------------ |
| of privacy, | fairness, | and | informativeness |     | in explanation |     | generation |              |             |       |           |       |                    |
PatrickDeCausmaecker,‘Anefficienttranslationschemeforrepresent-
forschedulingsystems. ingnurserosteringproblemsassatisfiabilityproblems’,inProceedings

oftheInternationalConferenceonAgentsandArtificialIntelligence [38] Jean-Paul Watson, J. Christopher Beck, Adele Howe, and L. Darrell
(ICAART),pp.303–310,(2013). Whitley,‘Problemdifficultyfortabusearchinjob-shopscheduling’,
[19] Carlos Hernández, William Yeoh, Jorge A. Baier, Han Zhang, Luis ArtificialIntelligence,143(2),189–217,(2003).
Suazo, Sven Koenig, and Oren Salzman, ‘Simple and efficient bi- [39] YuZhang,SarathSreedharan,AnaghaKulkarni,TathagataChakraborti,
objectivesearchalgorithmsviafastdominancechecks’,ArtificialIn- HankzHankuiZhuo,andSubbaraoKambhampati,‘Planexplicability
telligence,314,103807,(2023). andpredictabilityforrobottaskplanning’,inProceedingsoftheInter-
[20] AlexeyIgnatiev,AntonioMorgado,andJoaoMarques-Silva,‘PySAT: nationalConferenceonRoboticsandAutomation(ICRA),pp.1313–
APythontoolkitforprototypingwithSAToracles’,inProceedingsof 1320,(2017).
theInternationalConferenceonTheoryandApplicationsofSatisfiabil- [40] TerryYueZhuo,YujinHuang,ChunyangChen,andZhenchangXing,
ityTesting(SAT),pp.428–437,(2018). ‘Red teaming ChatGPT via jailbreaking: Bias, robustness, reliability
[21] MiyukiKoshimura,HidetomoNabeshima,HiroshiFujita,andRyuzo andtoxicity’,arXivpreprintarXiv:2301.12867,(2023).
Hasegawa, ‘Solving open job-shop scheduling problems by SAT en-
coding’,IEICETransactionsonInformationandSystems,93(8),2316–
2318,(2010).
[22] Ashwin Kumar, Stylianos Loukas Vasileiou, Melanie Bancilhon,
AlvittaOttley,andWilliamYeoh,‘VizXP:Avisualizationframework
forconveyingexplanationstousersinmodelreconciliationproblems’,
inProceedingsoftheInternationalConferenceonAutomatedPlanning
andScheduling(ICAPS),pp.701–709,(2022).
[23] Sudip Kundu and Sriyankar Acharyya, ‘Stochastic local search ap-
proachesinsolvingthenurseschedulingproblem’,inProceedingsof
theInternationalConferneceonComputerInformationSystems-Anal-
ysisandTechnologies(CISIM),pp.202–211.
[24] ChuMinLiandFelipManya,‘MaxSAT,hardandsoftconstraints’,in
HandbookofSatisfiability,903–927,IOSpress,(2021).
[25] João Marques-Silva, Federico Heras, Mikolás Janota, Alessandro
Previti,andAntonBelov,‘Oncomputingminimalcorrectionsubsets’,
inProceedingsoftheInternationalJointConferenceonArtificialIntel-
ligence(IJCAI),pp.615–622,(2013).
[26] StefanPalanand ChristianSchitter,‘Prolific:Asubject poolforon-
line experiments’, Journal of Behavioral and Experimental Finance,
17,22–27,(2018).
[27] JosePintoandIgnacioGrossmann,‘Alogic-basedapproachtoschedul-
ingproblemswithresourceconstraints’,Computers&ChemicalEngi-
neering,21(8),801–818,(1997).
[28] Alberto Pozanco, Francesca Mosca, Parisa Zehtabi, Daniele Maga-
zzeni, and Sarit Kraus, ‘Explaining preference-driven schedules: the
expresframework’,inProceedingsoftheInternationalConferenceon
AutomatedPlanningandScheduling,pp.710–718,(2022).
[29] Alessandro Previti and João Marques-Silva, ‘Partial MUS enumera-
tion’,inProceedingsoftheAAAIConferenceofArtificialIntelligence
(AAAI),pp.818–825,(2013).
[30] Sabino Francesco Roselli, Kristofer Bengtsson, and Knut Åkesson,
‘SMTsolversforjob-shopschedulingproblems:Modelscomparison
andperformanceevaluation’,inInternationalConferenceonAutoma-
tionScienceandEngineering(CASE),pp.547–552,(2018).
[31] TranCaoSon,VanNguyen,StylianosLoukasVasileiou,andWilliam
Yeoh,‘Modelreconciliationinlogicprograms’,inEuropeanConfer-
enceonLogicsinArtificialIntelligence(JELIA),pp.393–406,(2021).
[32] Sarath Sreedharan, Tathagata Chakraborti, and Subbarao Kambham-
pati, ‘The emerging landscape of explainable automated planning &
decisionmaking’,inProceedingsoftheInternationalJointConference
onArtificialIntelligence(IJCAI),pp.4803–4811,(2020).
[33] KarthikValmeekam,SarathSreedharan,SailikSengupta,andSubbarao
Kambhampati,‘RADAR-X:aninteractivemixedinitiativeplanningin-
terfacepairingcontrastiveexplanationsandrevisedplansuggestions’,
inProceedingsoftheInternationalConferenceonAutomatedPlanning
andScheduling(ICAPS),pp.508–517,(2022).
[34] JorneVandenBergh,JeroenBeliën,PhilippeDeBruecker,ErikDe-
meulemeester,andLiesjeDeBoeck,‘Personnelscheduling:Alitera-
turereview’,EuropeanJournalofOperationalResearch,226(3),367–
385,(2013).
[35] StylianosLoukasVasileiou,AlessandroPreviti,andWilliamYeoh,‘On
exploitinghittingsetsformodelreconciliation’,inProceedingsofthe
AAAI Conference on Artificial Intelligence (AAAI), pp. 6514–6521,
(2021).
[36] StylianosLoukasVasileiou,WilliamYeoh,andTranCaoSon,‘Onthe
relationshipbetweenKRapproachesforexplainableplanning’,arXiv
preprintarXiv:2011.09006,(2020).
[37] Stylianos Loukas Vasileiou, William Yeoh, Tran Cao Son, Ashwin
Kumar, Michael Cashmore, and Daniele Magazzeni, ‘A logic-based
explanation generation framework for classical and hybrid planning
problems’,JournalofArtificialIntelligenceResearch,73,1473–1534,
(2022).