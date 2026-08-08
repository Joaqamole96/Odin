Directive Explanations for Actionable Explainability in
Machine Learning Applications
RONALSINGH,TIMMILLER,HENRIETTALYONS,LIZSONENBERG,
EDUARDOVELLOSO,andFRANKVETERE,SchoolofComputingandInformationSystems,
TheUniversityofMelbourne,Australia
PIERSHOWE,MelbourneSchoolofPsychologicalSciences,TheUniversityofMelbourne,Australia
PAUL DOURISH,DonaldBrenSchoolofInformationandComputerSciences,UniversityofCalifornia,
Irvine,UnitedStates
Inthisarticle,weshowthatexplanationsofdecisionsmadebymachinelearningsystemscanbeimproved
bynotonlyexplainingwhy adecisionwasmadebutalsoexplaininghow anindividualcouldobtaintheir
desiredoutcome.Weformallydefinetheconceptofdirectiveexplanations (thosethatofferspecificactions
an individual could take to achieve their desired outcome), introduce two forms of directive explanations
(directive-specificanddirective-generic),anddescribehowthesecanbegeneratedcomputationally.Wein-
vestigatepeople’spreferenceforandperceptiontowarddirectiveexplanationsthroughtwoonlinestudies,
onequantitativeandtheotherqualitative,eachcoveringtwodomains(thecreditscoringdomainandthe
employeesatisfactiondomain).Wefindasignificantpreferenceforbothformsofdirectiveexplanationscom-
23
paredtonon-directivecounterfactualexplanations.However,wealsofindthatpreferencesareaffectedby
manyaspects,includingindividualpreferencesandsocialfactors.Weconcludethatdecidingwhattypeof
explanationtoproviderequiresinformationabouttherecipientsandothercontextualinformation.Thisre-
inforcestheneedforahuman-centeredandcontext-specificapproachtoexplainableAI.
CCSConcepts:•Human-centeredcomputing→Userstudies;•Computingmethodologies→Artificial
intelligence;Machinelearning;
AdditionalKeyWordsandPhrases:ExplainableAI,directiveexplanations,counterfactualexplanations
ThereviewingofthisarticlewasmanagedbyspecialissueassociateeditorsUpolEhsan,StylianiKleanthous,Q.VeraLiao,
AlisonSmith-Renner,AdvaitSarkar,andMarkO.Riedl.
ThisprojectissupportedbyAustralianResearchCouncil(ARC)DiscoveryGrantDP190103414:ExplanationinArtificial
Intelligence:AHuman-CentredApproach.
Authors’addresses:R.Singh,T.Miller,H.Lyons,L.Sonenberg,E.Velloso,andF.Vetere,SchoolofComputingandInfor-
mationSystems,TheUniversityofMelbourne,Melbourne,VIC,Australia,3010;email:{singhrr,tmiller,henrietta.lyons,
l.sonenberg,eduardo.velloso,f.vetere}@unimelb.edu.au;P.Howe,MelbourneSchoolofPsychologicalSciences,TheUni-
versityofMelbourne,Melbourne,VIC,Australia,3010;email:pdhowe@unimelb.edu.au;P.Dourish,DonaldBrenSchool
ofInformationandComputerSciences,UniversityofCalifornia,Irvine,Irvine,CA,92697-3440;email:jpd@ics.uci.edu.
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalorclassroomuseisgrantedwithoutfee
providedthatcopiesarenotmadeordistributedforprofitorcommercialadvantageandthatcopiesbearthisnoticeand
thefullcitationonthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthantheauthor(s)mustbe
honored.Abstractingwithcreditispermitted.Tocopyotherwise,orrepublish,topostonserversortoredistributetolists,
requirespriorspecificpermissionand/orafee.Requestpermissionsfrompermissions@acm.org.
©2023Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
2160-6455/2023/12-ART23$15.00
https://doi.org/10.1145/3579363
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:2 R.Singhetal.
ACMReferenceformat:
RonalSingh,TimMiller,HenriettaLyons,LizSonenberg,EduardoVelloso,FrankVetere,PiersHowe,andPaul
Dourish.2023.DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications.ACM
Trans.Interact.Intell.Syst.13,4,Article23(December2023),26pages.
https://doi.org/10.1145/3579363
1 INTRODUCTION
Machine learning models are increasingly playing a critical role in decision-making in various
domains,suchasmedicine,law,andbanking[3,4,16,36,40,42].Oneoftheaimsofexplaining
decisions made by or with the aid of a machine learning model is to enable recourse, that is,
to help individuals understand what they could change to receive a different outcome in the
future[51,74,76,78].Forexample,whentheuseofmachinelearningmodelsleadstothedenial
of a loan application, the explanation should not only describe the reasoning that led to the
decisionbutalsohelpthecustomerunderstandwhattheycoulddointhefuturetogettheloan
approved[72].
Counterfactualexplanationshavethepotentialtoenablerecourse[76,78].Counterfactuals(or
counterfactual states) “describe how the world would have (had) to be different for a desirable
outcometooccur”[78].However,notallcounterfactualsareactionable.Forexample,considera
loanapplicantbeingtoldthattohavetheirloanapproved,theywouldhavehadtohavenoprior
loandefaultsintheprevious5years;thisexplanationdoesnotfacilitaterecoursesincenothingcan
bedonetoalterhistory.Forcounterfactualexplanationstoenablerecourse,explanationsshouldbe
basedonactionableinputfeatures[76].Utsunetal.[76]proposeamethodforgeneratingactionable
explanations orflipsets,thatis,explanationswithactionablefeaturesthatguaranteethedesired
outcome. A challenge of this approach is that some features, such as education level or income,
maybemutableonlyforsomepeople.Thisproblemisusuallyresolvedbyofferingmultiplediverse
counterfactualexplanations[65,76–78]withthehopethatatleastoneexplanationissuitablefor
therecipient.
While multiple counterfactuals may provide some guidance as to what circumstances would
result in a different outcome (e.g., a loan being approved), they do not explicitly indicate which
actionsmayleadtothisdesiredresult;thatis,theydonotprovideexplicitrecommendationson
how to act [38]. Depending on the context, how to reach the counterfactual state might not be
apparenttoanindividual[61].InanAIplanningsense[30],counterfactualexplanationsprovide
the initial state (current instance) and the goal state (the counterfactual state), resulting in the
desired outcome (decision). However, the actions that would take a person from the current
state to the counterfactual state are not part of the explanation. There is an assumption that
each counterfactual maps to a real-world action [6, 66], but this is not always the case [38].
Furthermore, most of the prior works on counterfactual explanations have assumed a one-step
decision-makingprocess[54,65,76,78].
Tobettersupportrecourse,wearguethatcounterfactualexplanationsshouldbedirectiveinthat
theyshouldincludesuggestionsorrecommendationsoftheaction(s)theindividualcouldperform,
thatis,howtoact togettothecounterfactualstate.Othershaveechoedsimilarsentiments,such
asthosethatadvocateforcausalmodels[38–40,50,74].
In this article, we contribute toward the goal of making explanations directive. In Section 3,
weformallydefinetheconceptofdirectiveexplanation,andwepresentamodelandimplementa-
tionforgeneratingdirectiveexplanations.ThismodelisbasedonMarkovDecisionProcesses
(MDPs)[7,60]andgivesusaframeworktoconsiderasequenceofdependentactionsthataperson
hastotaketoachieverecourse.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:3
InSections4through6,wepresenttwostudies,thefirstquantitativeandthesecondqualitative,
toinvestigateparticipants’preferencesandopinionstowarddirectiveexplanationsinthedomains
ofcreditscoringandemployeesatisfaction.
Weconductedtwostudiestoanswertwoquestions:(1)Whichofthethreetypesofexplanation
(non-directive,directive-specific,anddirective-generic)isthepreferred?(2)Whatarethereasons
someonedoesordoesnotpreferdirectiveexplanations?Weconductedthefirststudytoanswer
the first research question and a second study to answer the second research question. We con-
ductedthesetwostudiesoncreditscoringandlendingdecisionsandemployeeturnover(whether
employeeswerelikelytoresign).
For each study, we designed eight scenarios, four where the decision was favorable (e.g., the
loan was approved) and four not (e.g., the loan was denied). For each scenario, we provided
participants with four different types of explanations. The first was non-directive, the second
was directive with specific actions, the third was directive with generic action, and the fourth
wasclearlynotsensibleandservedasanattentioncheck,withusexcludinganyparticipantwho
did not rank this as the least preferred explanation. The non-directive explanation informed the
person how the situation must change for the desired goal to be achieved but did not suggest
actions to achieve this counterfactual state. For example, the participant might be told that to
preventtheemployeefromresigning,theemployeeshouldberequiredtotravelonlyamedium
amountforbusiness,butitwouldnotbeexplainedhowthisreductionintheamountofbusiness
travel could occur. Conversely, the directive-specific explanation recommended specific actions
that an individual could take to reach the counterfactual state. For example, the participant
mightbetoldthattoreducetheamountofbusinesstravelfromhightomedium,clientmeetings
should be conducted online. The directive-generic explanation recommended a generic class
of actions. Directive-generic explanations indicate the kinds of actions that could be taken to
reach the counterfactual state, but only broadly so individuals still had the freedom to decide
which specific actions they would want to take. Participants ranked the four explanations from
mosttoleastpreferredinthefirststudyandprovidedthereasonsfortheirchoiceinthesecond
study.
We ran the studies on Amazon MTurk with 65 participants. We found significant support for
thetwodirectiveexplanationsinbothdomains.Inthecreditscoringdomain,approximately42%,
31%,and27%ofparticipantsselecteddirective-specific,directive-generic,andnon-directiveexpla-
nations,respectively,astheirmostpreferredexplanation.Fortheemployeesatisfactiondomain,
distributions were 35%, 51%, and 14%, respectively, for directive-specific, directive-generic, and
non-directiveexplanations.Thekeyfindingsare:
• Wefindaclearpreferenceforthetwodirectiveexplanationsovernon-directivecounterfac-
tualexplanationsinbothdomains.Thenon-directiveexplanationwasleastpreferred.
• Directive-specificexplanationsaremoresuitedtoscenarioswheretheoutcomeisunfavor-
able.Forexample,whenloansweredeniedoranemployeewaslikelytoleavetheorganiza-
tion,theparticipantspreferreddirective-specificexplanations.Thissuggeststhat,atleastin
thetwodomainswestudied,peopleshouldhaveanoptiontoreceivedirectiveexplanations
iftheywish.
• The preference for directive-generic explanation may depend on the task. We found that
participantsintheemployeesatisfactiondomainstronglypreferredadirective-genericex-
planation. This suggests that participants prefer to provide high-level guidance and avoid
specificactionswhentheyhavetheirownideasforsolvingproblems.
• Non-directivesmaybemoresuitablewhentheoutcomeisfavorable,andthiswascertainly
trueforthecreditscoringdomain.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:4 R.Singhetal.
Aqualitativeanalysisofthereasonsparticipantsprovidedfortheirmostpreferredexplanation
revealedthatthechoiceforexplanationtypedependedonmultiplefactors,suchassocialfactors,
and whether the participants judged the directives to be feasible for the recipient. These results
suggestthatevenwithanefficientcomputationalmodel(e.g.,likeourMDP-basedmodel)togen-
eratedirectiveexplanations,onecannotaprioridecidewhattypeofexplanationtoprovide—one
needs further information about recipients’ preferences and contextual information to generate
actionableexplanations,directiveornon-directive.Thisreinforcestheneedforahuman-centered
andcontext-specificapproachtoexplainableAI.
2 BACKGROUND
Machine-learning-based systems can be complex and opaque, and their use to make critical de-
cisionsdependsonthedegreetowhichthesesystemsareinterpretable,thatis,howwellpeople
understandthecausesofitsdecision-making[9,35,48,51].Thereareseveralwaysofpotentially
makingmachinelearningmodelstransparent,fromusingintrinsicorintelligiblemodels[64]to
usingposthocmethods[1,31,48,53],suchascounterfactualexplanations[78].
2.1 CounterfactualExplanations
Wachteretal.[78]proposetheuseofunconditionalcounterfactualexplanationsforpeopletounder-
standadecision,contestit,andpotentiallyusetheexplanationtochangethedecisionoroutcome.
Rather than discussing the internal logic of a machine learning algorithm, counterfactual expla-
nations describe a dependency on the external facts that led to a decision [26, 78]. The notion
of counterfactuals [45] can significantly assist in making machine-learning-based systems inter-
pretable [17, 18]. We scope our discussions to a subset of machine learning models. Specifically,
weconsiderclassificationproblems,whicharedefinedinDefinition2.1.Whilesubsequentdiscus-
sions are based on classification problems, our discussions and methods can be applied to other
formsofmachinelearningmodelsthatsolveregressionproblems.
Definition2.1(ClassificationProblem). Aclassificationproblemisatuple(f,x,y),where f isa
machinelearningmodel,x ∈ X isafeaturevectordescribingtheinstancethatisbeingclassified,
andy ∈ {0,1}isthelabelassignedby f tox.
In the context of the classification problem, a counterfactual state is a statement of how the
worldwouldhavetobedifferentforadesirableoutcometooccur.Givenaninputfeaturex and
thecorrespondingoutputbyamachinelearningmodelf,acounterfactualexplanationisapertur-
bationoftheinput,x,suchthatadifferentoutput,y,isproducedbythemodel, f.Wachteretal.
[78]proposethefollowingformulation:
c =argminy (f (c),y)+|x −c|, (1)
loss
c
where y () pushes the counterfactual state c toward a different prediction than the original
loss
instance, while the second term keeps the counterfactual close to the original instance using a
distancemetric.
2.2 CounterfactualExplanationsandRecourse
Oneoftheaimsofcounterfactualexplanationsistoenablerecourse,andrecourseisbroadlyrelated
toseveraltopicsinmachinelearning,suchasinverseclassification[2],strategicclassification[24,
34],adversarialperturbations[28],andanchors[63].
Utsunetal.[76]proposeanoptimization-basedapproachusingintegerprogrammingtoevalu-
atealinearclassificationmodelintermsofrecourse.Theirmethodsharessimilaritieswithexisting
ones[47,62,78]butfocusesonsuggestingactionablechangesandevaluatingthefeasibilityand
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:5
difficultyofrecourse.Theirmethodenablesonetoestablishwhetherapersoncouldchangethe
decisionofamachinelearningmodelthroughactionableinputvariables,andtheydothisbyop-
timizingacost functiongivenaninputx.Theydefineanaction,a,asachangetothevalueofa
feature.Theychooseactionsfromasetofactionablefeatures,A(x),thatis,asetofmutableorcon-
ditionallymutablefeatures,andeachactionhasacost.Theysolvetheproblemoffindingactions
thatminimizethecost.
Severalmethodsprovidemultiplecounterfactualstopeopleseekingrecourse[65,76,78].Offer-
ingmultiplecounterfactualsmayensurethatatleastonehasactionablefeaturesforanindividual.
Recently,othershaveextendedthiswork[54,59].Althoughnearestcounterfactualexplanations
provideanunderstandingofthemostsimilarsetoffeaturesthatresultinthedesiredprediction,
they fall short of giving explicit recommendations on how to act to realize this set of features,
and this limits agency for the individual seeking recourse [38]. Karimi et al. [38] show that cur-
rent forms of counterfactuals do not translate to an optimal or feasible set of recommendations.
Instead,theyproposeminimizingthecostofperformingactionsinaworldgovernedbyasetof
lawscapturedinastructuralcausalmodel.
2.3 BeyondOne-stepActionforRecourseUsingMarkovDecisionProcess
Recently,researchhasbeenlookingatmovingbeyondtheone-stepactionassumptionprevalent
inthespaceofalgorithmicrecoursetoconsideringtheproblemasamulti-stepsequentialdecision-
makingproblem[14,55,57,74].
More recently, Tsirtsis et al. [74] proposed a method to find counterfactual explanations
for sequential decision-making processes, modeled as discrete-time Markov Decision Process,
where the state and action spaces are discrete and low-dimensional. Their method identifies
counterfactual trajectories (sequence of actions) that achieve better outcomes and differ by
k actions from the observed sequence. They model the transition probabilities between a pair
of states, given an action, using the Gumbel-Max structural causal model [57] because that
deliversadesirablecounterfactualstabilitypropertyandreliableestimationofthecounterfactual
outcome.
Similarworksexistinthespaceofreinforcementlearning[14,50,57].Forexample,Madumal
etal.[50]proposedanactioninfluencemodeltorelateactionstostatesandtoexplainthelearned
actionsorpoliciesthatpeoplereadilyunderstand,andOberstandSontag[57]usetheGumbel-Max
SCMtoevaluatecounterfactualpolicies.Afewmodelstakeadvantageofcausalassumptions[25,
38,40,43]butinthecontextofone-stepaction;therefore,theyaredifferentfromourmodeland
that of Tsirtsis et al. [74]. We differ from Tsirtsis et al. [74] in that they generate counterfactual
recommendationsgivenanalreadyobservedsequenceofactions,whilewegeneratethedirectives
(sequenceofactions)withoutreferencetoanyobservedtrajectories.However,similartoTsirtsis
etal.[74],wemodeltheproblemofsynthesizingdirectivesasanMDP.
SimilartoKarimietal.[38]andTsirtsisandGomez-Rodriguez[75],webelievethatactionable
counterfactual explanations should provide some guidance to individuals on how to act. In other
words,theyshouldbedirective.Assuch,aswetakeourfirststepstowarddirectiveexplanations,
we conducted two online studies to investigate individuals’ perception of and preference for di-
rective explanations relative to merely counterfactual explanations. We discuss the details of the
studiesandproposeaconceptualmodelcapableofgeneratingthedirectives.
3 AMODELFORDIRECTIVEEXPLANATIONS
Thissectionformallydefinestheconceptofdirectiveexplanationsanddefinesamodelforgener-
atingdirectiveexplanationsforclassificationproblems.Wefocusourdiscussionandexampleson
classification,butthiscanalsoapplymorebroadlytoregressionproblems.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:6 R.Singhetal.
Definition3.1(DirectiveExplanation). Adirectiveexplanationisatuplede = (f,x,y,C,Φ,Y(cid:4) ),
inwhich f isamachinelearningmodel,x ∈Xistheoriginalinputvector,y = f(x)isthecurrent
classlabel,Cisthesetofpossiblecounterfactualssuchthateachc ∈ Chasadifferentclasslabel
i
(i.e.,∀c ,c : i (cid:2) j,f(c ) (cid:2) f(c ),f(c ) (cid:2) y,f(c ) (cid:2) y),Φisthesetofpossiblepoliciessuchthat
i j i j i j
eachπ ∈ Φisapolicy(asetofdirectives)thattransitionsx toc ,andY(cid:4) isthesetofpossible
i i
classlabelswitheachy (cid:4) = f(c ),y (cid:4) ∈Y(cid:4) beingtheoutcomeorclasslabelforeachcounterfactual
i i i
c ∈ C.
i
Ourdesiderataforsuchanapproachconsistsofthefollowing.First,themodelmustgeneratea
setofdirectivesthatshowhowtogetfromthefactualstatex toacounterfactualstate,c .Actions
i
fromπ mustleadfromx toc .Second,themodelmustcapturedifferentwaystoachievespecific
i i
outcomes; that is, getting to each counterfactual statec ∈ C can be done in multiple different
i
ways. Third, the model must capture inherent uncertainty in the outcomes of these actions in
achieving outcomes. Finally, the model should also account for action costs to account for the
coststhatindividualsmayincurwhentryingtoreachacounterfactualstateusingthedirectives,
whichallowsustomodelthatsomedirectivesaremorecostlythanothers,andeventoconsider
different costs for different individuals. To identify potential states that change the outcome, C,
wecanuseanyexistingcounterfactualgenerator,e.g.,[54,65].
Fromthesedesiderata,itisclearthattheframeworkofMDPs[60]isasuitableformalismfor
modeling this problem. This allows us to use a planning-based approach to generate a policy,
π , that transitions x to c ∈ C. Policy π ∈ Φ is the source of the directives in the directive
i i i
explanations.Wedefineaconceptualmodelforgeneratingthedirectivesbelow.
Definition3.2(MarkovDecisionProcess[60]). AnMDPisatupleΠ = (S,A,P,R,λ),inwhichS
isasetofstates;Aisasetofactions;P(s,a,s (cid:4) ) isatransitionfunctionfromS ×A → 2S,which
(cid:4) (cid:4)
definestheprobabilityofactiona goingtostates ifexecutedinstates;R(s,a,s ) isthereward
(cid:4)
receivedfortransitionsfromexecutingactiona instates andendingupinstates ;andλ isthe
discountfactor.
MDPscanbeconceptualizedasgraphsthatmapstateswithtransitions(actions),alongwiththe
(cid:4)
transitionprobabilitiesandrewards.IfΣ s(cid:4)∈S P(s,a,s ) >0,thenthismeansthatactionaisenabled
(cid:4) (cid:4)
instates andwilltransitiontooneofthestatess forwhichP(s,a,s ) > 0.Thediscountfactor
controlshowmuchweightorimportanceisplacedonfuturerewards.
Definition3.3(PlanningProblem[60]). Aplanningproblemisatuple(Π,I,O),inwhichI ∈S is
theinitialstateandOistheobjectivetobeachieved.Inthesimplestcase,agoal-directedMDP[30],
O isjustasetofgoalstates,suchthatO ⊂S,butamorecommonobjectiveissimplytomaximize
theexpecteddiscountedreward[60].Thetaskistosynthesizeapolicy π : S → Afromstatesto
actionsthatstartsinstateI andachievesobjectO.
Toshowhowtoapplythistodirectiveexplanation,wemapDefinition3.3toDefinition3.1.The
initialstateI = x suchthat f(I) =y,andtheobjectiveO isto“reach”c ∈ C,whichisachieved
i
when f(c ) = y (cid:4) . That is, x is the initial state and c is one of the “goal states,” which can be
i i i
modeled as receiving a reward if and only if f(c ) = y (cid:4) . Conceptually, for eachc , we want to
i i i
generateapolicyof actionsthattransitionfrom theinitial statex tothecounterfactualstatec .
i
Thesolutiongivenfortheplanningproblemπ isthesetofdirectives.Eachactionaisadirective
i
(cid:4) (cid:4)
thattransitionsthestatetoanewstates ,whichrepresentstheperturbedfeaturevector,x .For
multi-classproblems,asimpleapproachwouldbetogenerateaplan,π ∈ Φ,foreachc ∈ C to
i i
providetotheuser.
ThereareseveralwaystosolvetheplanningproblemΠ,suchasusingdynamicprogramming
or model-free reinforcement learning [30, 70, 71, 74]. We have implemented this model using
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:7
Monte-CarloTreeSearch[11]tocreateanapproximatepolicy,π.Wechoosethesetofactions,A,
∈A,wespecifyexactlyhowthefeatures
suchthattheymodifyonlymutablefeatures.Foreacha
aremodifiedbytakingdirectivea.Forexample,ifaistocancelacreditcard,thefeature“number
ofcreditcards”issubtractedby1.Tokeeptheproblemrepresentationsimple,foreacha ∈A,we
enumerate multiple versions of the actions,a ,...,a , for every possible assignment of feature
1 n
values.Forexample,ifanactionaupdatesafeature, f ,takingontwovalues,thenwewouldgen-
b
|                                |     | =0)  | =1).Webinnedthecontinuousfeaturesto |     |     |     |
| ------------------------------ | --- | ---- | ----------------------------------- | --- | --- | --- |
| eratetwoversionsoftheactiona:a |     | 1 (b | anda 2 (b                           |     |     |     |
usewithourmethod(wetestedthemodeloncategoricalfeaturesonly).Thetree’srootnodeisthe
initialfeaturevector,x,andeachedgerepresentsapossibleaction.Toguidethesearchtowardthe
∈ C,weuseamulti-objectiverewardstatedasalinearfunctionoftwoobjectives:
| counterfactual,c | i             |                 |               |                   |                 |     |
| ---------------- | ------------- | --------------- | ------------- | ----------------- | --------------- | --- |
|                  |               | r s(cid:4) = (r | +r            | ),                |                 | (2) |
|                  |               | decision        | distance      |                   |                 |     |
|                  | ⎧⎪ (cid:4)    | =y (cid:4)      | ⎧⎪            | (cid:4) ≤δ        |                 |     |
|                  | ⎨ α, f(s )    |                 | ⎨ β, dist(s   | ,c)               |                 |     |
| wherer           | =             | ,r              | =             | ,y (cid:4) = f(c) | is the expected |     |
| decision         | ⎪             | distance        | ⎪             |                   |                 |     |
|                  | ⎩0, otherwise |                 | ⎩0, otherwise |                   |                 |     |
counterfactual outcome,s (cid:4) ∈ S is the state reached after performing the policy π,dist(s (cid:4) ,c) is
the Euclidean distance ((cid:2) 2 norm), andδ is the radius or distance threshold. The radiusδ allows
us to generate multiple directives within δ distance away from c. During the rollout, Upper
ConfidenceBounds(UCBs)guidetheselectionofnodes.
|                       | =0.5,β | =0.5,andδ | =[1,10](wearrivedattheδ |     |                   |     |
| --------------------- | ------ | --------- | ----------------------- | --- | ----------------- | --- |
| Forexperiments,wesetα |        |           |                         |     | valuesempirically |     |
foreachscenariotogetmultipletrajectoriesforthetwotypesofdirectiveexplanation;fromour
=0.8;thisvalue
experience,δ isscenario-ortask-dependent).Therewardswerediscountedbyγ
wasalsoarrivedatempirically.Finally,wechoseallcategoricalfeaturesandassociatedactions,A,
toillustratethedirectiveexplanations.WeprovideanalgorithminAppendixF.
In our implementation, while we have not considered diverse directives, there are numerous
methods to measure the plan differences, and these can be used to devise a metric to compute
multiplediversedirectives[12,41].
⊆
Notice that the set of actions in the policy,A A, are directive-specific actions. That is, in
pi
thepolicy,π,eachactiona ∈ Aisdirective-specific.InourstudyinSection4,weperformpost-
processingontheπtogeneratedirective-genericexplanation.First,wegenerateagraphthatstarts
withaparentorrootnode,p.Thisrootnodesimplyperformstheroleofprovidinganattachment
pointfordirective-genericexplanations.Second,eachdirective-genericexplanation,a ∈A ,
|     |     |     |     |     | дen | дen |
| --- | --- | --- | --- | --- | --- | --- |
∈
is connected top, and then each specific directive,a A, is connected with its respectivea .
дen
| Finally,duringpost-processing,wesimplyreplaceawitha |     |     |     | .   |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
дen
∈
For example, assume that {“consolidate credit cards,” “pay off credit card”} A, and {“reduce
creditcards”}∈A ,andpistherootnode.Thenwehaveanedgefrompto“reducecreditcards.”
дen
Therewillbetwoedgesfrom“reducecreditcards,” oneto“consolidatecreditcards” andtheother
to“payoffcreditcard.” Ifthemodelsuggests“payoffcreditcard,” thenthisactioninthedirective-
specificexplanationisreplacedwith“reducecreditcards” forthedirective-genericversionofthe
explanation.
4 STUDIES
Forcounterfactualexplanationstobedirective,wearguethattheymustprovideindividualswith
recommendationsonhowtoact,asopposedtoindicatingonlywhatstatetheindividualneedsto
reach.Wewishedtoknowwhetherindividualspreferreddirectiveexplanationsovermerecoun-
terfactualexplanationsand,ifso,whethertheypreferredspecificorgenericdirectiveexplanations.
Weconductedtwostudiestoanswertwoquestions:(1)Whichofthethreetypesofexplanation
(non-directive,directive-specific,anddirective-generic)ispreferredmost?(2)Whatarethereasons
someonedoesordoesnotpreferdirectiveexplanations?
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:8 R.Singhetal.
Wedescribetwostudiesinthefollowingsections.Weconductedthefirststudytoanswerthe
firstresearchquestion:Whichofthethreetypesofexplanation(non-directive,directive-specific,
anddirective-generic)ispreferredthemost?Weranasecondstudy,aqualitativestudy,toanswer
the second research question: What are the reasons someone does or does not prefer directive
explanations?Ourstudiesinvolvedanautomatedsystemexplainingtoanintermediarywhythe
automatedsystemmadeaparticulardecision,suchasdenyingaloan.Theintermediarythense-
lectedoneofthefourpossibleexplanationstoprovidetotheclient.Inmanycontexts,suchasloan
applications,webelievethatanautomatedsystemassistspeople(loanofficers)whoassistothers
(customers).Therefore,thissetupallowsustounderstandwhatahumanconsidersrelevantwhen
explainingdecisionstoanotherhumanandprovideinsightsfromthisperspective.
We conducted the two studies using scenarios designed around credit risk and employee
turnover.Wechosethetwodomainsbecauseweanticipatedthatmostparticipantswouldbeaware
ofthebasicsofbothdomainsand,therefore,wouldnotrequiretrainingtounderstandthedomain
concepts.Theotherreasonisthatwehadexperiencewiththetwodomains.Finally,bothdomains
aretypicalcasestudiesintheexplainableAIcommunity.
4.1 ExplanationTypes
We provided participants with three explanation types: (1) non-directive, (2) directive-specific,
and (3) directive-generic, as defined below. We presented only one explanation of each type for
eachscenariotokeepthenumberofexplanationsofeachtypeconsistentacrossscenarios.
ExplanationType1-Non-directive:Thesewerestandardcounterfactualexplanations;thatis,
they specified which parts of the data would have to change to reverse a decision and to what
extenttheywouldneedtochange.Forexample,anon-directiveexplanationtoacustomercould
state the maximum debt-to-income ratio needed to approve the loan. Crucially, the explanation
didnotincludedirectivesonachievingtherequiredchange.
Explanation Type 2 - Directive-specific: These included two components: the desired
counterfactual state and a set of specific actions to help the participant reach that state. For ex-
ample,itmightsuggestthatthecustomerpaysofftheircarloantoreducethedebt-to-incomeratio.
Explanation Type 3 - Directive-generic: These explanations suggested a general class of ac-
tionsthatindividualscouldtaketoreachthedesiredcounterfactualstatewithoutrecommending
aspecificaction.Theideawastopreserveindividuals’autonomyindecidingwhichspecificactions
theywanttotakewhilestillguidingtheirdirection.Forexample,wemightdirectthecustomer
tofindstrategiestoreducethetotaldebtwithoutgivingexamplesofanyspecificstrategiesthey
coulduse.
4.2 IdentifyingDirectives
Togeneratealistofcandidateactionsthatweusedindirectiveexplanations,wereviewedanum-
berofwebsitesthatprovidedfinancialadvice1,2,3,4,5,6andadviceregardingimprovingemployee
1https://www.experian.com/blogs/ask-experian/credit-education/debt-to-income-ratio/.
2https://www.marketwatch.com/story/try-these-creative-strategies-for-lowering-your-debt-to-income-ratio-2018-09-
07.
3https://www.credit.com/blog/6-creative-ways-to-lower-your-debt-to-income-ratio-185695/.
4https://bettermoneyhabits.bankofamerica.com/en/credit/what-is-debt-to-income-ratio.
5https://www.upgrade.com/credit-health/insights/credit-utilization-ratio/.
6https://www.creditkarma.com/advice/i/how-to-lower-your-credit-card-utilization/.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:9
jobsatisfaction,jobinvolvement,managingovertime,andotherHumanResource(HR)-related
strategies.7,8,9,10,11
Todevelopasimplemodelofhowactionsaffectmodelfeatures,wefirstidentifiedasubsetoffea-
turesthatwereusedtotrainmachinelearningmodelsandthatwebelievecouldbeobservedand
acteduponbydecisionmakers.Foreachfeatureinthesubset,forexample,employeesatisfactionor
creditrating,wesearchedoneormoreofthewebsiteslistedabovetoidentifytheactionsthatcould
potentiallymodifythem.Weassumethatthesearetheonlyinterventionsthatmodifythefeatures,
butrealistically,thereareunobservednoisevariablesthatmayinfluencehowthefeaturesaremod-
ified[38,40,74].Furthermore,forthestudy,welimitedthenumberoffeatureseachactioncould
modifytoone.Formoredetailsonthemodel,pleaseseeSection3.Asanalternativetoplanning
fordirectives,onecouldlearnbehaviormodelsandusethosetogeneratecandidateactions[5].
5 STUDY1
Weconductedourstudyintwodomains,creditscoringandemployeesatisfaction.Wetraineda
machinelearningmodeltopredicttheoutcomeineachcase.
Forthecreditscoringdomain,wetrainedalogisticregressionmodeltopredictwhetherabor-
rowerwoulddefaultonaloanusingtheLendingClubdataset.12Themodelachievedanaccuracy
of85%.Similarly,fortheemployeesatisfactiondomain,wetrainedalogisticregressionmodelto
predictwhetheranemployeewouldlikelyresignusinganexistingdataset.13Themodelachieved
anaccuracyof76%.Togeneratethecounterfactualexplanations,weusedRussell’s[65]algorithm,
and we used ourmodel to generatethedirective explanations. Russell’s[65] algorithm can gen-
eratemanydiversecounterfactualexplanations.Forourstudy,weusedRussell’s[65]algorithm
to generate only one counterfactual,c, that is closest to the factual instance,x, with a different
outcomebysolvingthefollowingproblem:
argminmax(cid:9)x −c(cid:9)+τ (f (x)− f (c)). (3)
c τ
The distance function used in [65] is (cid:2) , weighted by the inverse Median Absolute Deviation
1
((cid:9).(cid:9) ).Thefunctionτ maximizesthedifferencebetweenthepredictionofthecounterfactual,
1,MAD
c,andthefactualpoint,x.Thismeansthatthecounterfactualinstanceweuseinourstudiesisthe
closestpointtotheinstanceweareexplainingwithadifferentoutcome.
The machine learning model was used in the credit scoring domain to decide whether to ap-
proveordenyacustomer’sloanapplication.Inthisdomain,participantsplayedtheroleofaLoan
Officer.Theyreceivedmachine-generatedexplanations,andwetoldthemtheirtaskwouldbeto
communicatethedecision(approvalordenial)andexplainittoacustomer.Intheseconddomain,
the employee satisfaction domain, the machine learning model was used to predict whether an
employeeislikelytoresigninthenearfuture.TheparticipantsplayedtheroleofanHRofficer,
who communicated the prediction to the employee’s supervisor using one of the explanations
weprovided.Ineachdomain,weprovidedtheparticipantswithourexplanations:non-directive,
directive-specific,directive-generic,andanattentioncheckquestion.
We designed eight scenarios in each domain (see Appendices B and C for a complete list of
scenarios).Eachscenarioincludeddetailsofaperson,forexample,aloanapplicant(customer)or
7https://www.saviom.com/blog/effective-strategies-reduce-employee-turnover/.
8https://www.findmyshift.com/au/blog/why-overtime-working-can-harm-businesses-and-how-to-reduce-it.
9https://www.challengeconsulting.com.au/announcements/six-strategies-for-increased-job-satisfaction/.
10https://www.challengeconsulting.com.au/announcements/six-strategies-for-increased-job-satisfaction/.
11https://www.findmyshift.com/au/blog/why-overtime-working-can-harm-businesses-and-how-to-reduce-it.
12https://www.kaggle.com/husainsb/lendingclub-issued-loans#lc_loan.csv.
13https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:10 R.Singhetal.
anemployee.Weaskedourparticipantstoreadanintroductorysectionthatincludedthedecision
(e.g.,whethertheloanwasapprovedordeniedorwhetheranemployeewaslikelytoresign)and
thentorankthefourexplanationsofthedecision.Thepurposeoftheintroductorysectionwasto
avoidrepeatingcertainpiecesofinformationineachexplanation;forexample,ratherthanrepeat-
ing the decision in each explanation, we included the decision in the introductory section. The
participantswererequiredtoranktheexplanationsfrommosttoleastpreferredtoindicatewhich
explanationtheyweremostlikelytousetocommunicatethedecisiontotheindividualconcerned.
Oneoutofthefourpossibleexplanationswasclearlyincorrect.Forexample,itmightsuggest
actionsthatwouldhavemadetheemployeemorelikelytoleave.Weusedthisasaqualitycontrol
measure;weremovedanyparticipantwhodidnotindicatethatthiswastheleastpreferredexplana-
tionintwoormorescenarios.Theotherthreeexplanationswerenon-directive,directive-specific,
anddirective-generic.Togeneratethecounterfactualexplanations(type1),weusedRussell’s[65]
algorithm,andweusedourmodeltogeneratethedirectiveexplanations(seeSection3formore
details).
5.1 Procedure
WeconductedthefirststudyusingAmazonMTurk,acrowd-sourcingplatformpopularforhuman-
subjectexperiments[15].WedesignedandadministeredtheexperimentsasaQualtrics14 survey.
Beforetheexperiments,wereceivedethicsapprovalfromourinstitution.Participantswerepaid
USD$15perhourforparticipatinginthestudy.
Seventy-ninepeopleparticipatedinthestudy,spreadovertwodomains:creditscoringandem-
ployeesatisfaction.WerecruitedMastersworkers,thatis,workerswhohaveconsistentlydemon-
strated a high degree of success in performing a wide range of tasks across a large number of
requesters.15AllparticipantswerefromtheUnitedStates.
Theparticipantsfirstreceivedaplainlanguagestatement,andiftheydecidedtocontinuethe
experiment,theyweregivenaconsentform.Iftheparticipantsagreedtoallitemsintheconsent
form,theywereaskedafewlogicalquestionstofilteroutautomatedrespondents.Thenweasked
theparticipantstoprovidetheirAmazonMTurkWorkerIDandfillinthedemographicsquestion-
naire. Following this, they were allocated at random one of the two domains, credit scoring or
employeesatisfaction.Werandomlyselectedsixoftheeightscenariosandpresentedtheseoneat
atime.Recallthatwehadfourscenarioswithafavorableoutcome(e.g.,theloanwasapproved)
andfourscenarioswithanunfavorableoutcome.Werandomlyselectedthreeofthefourscenarios
with a favorable outcome and three of the four with an unfavorable outcome, giving us six sce-
narios.Werandomizedthescenariosandexplanationstoeliminateorderingeffects.Thescenarios
werepresentedsequentiallywithouttheoptionofgoingbackandchangingpreviousanswers.Par-
ticipantswererequiredtorankthefourexplanationsfrommosttoleastpreferredforeachscenario.
Attheendofthesurvey,participantswerethankedandgivenarandomlygeneratedcodetoenter
intotheirAmazonMTurksessionsotheycouldbepaidforcompletingthetask.
5.2 Study1Results
Inthissection,wepresentthequantitativeanalysisshowingthatdirective-specificanddirective-
genericexplanationswerepreferredmorethannon-directiveexplanations.Wealsoshowthatthe
preferencewasdomain-dependent.Inthecreditscoring,participantspreferreddirective-specific
explanationsthemost,whileintheemployeesatisfactiondomain,directive-genericexplanations
werepreferredthemost.
14https://www.qualtrics.com/.
15https://www.mturk.com/worker/help.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:11
Fig.1. (a)Preferenceforeachexplanationtypeinstudy1(creditscoring).(b)Preferenceforeachexplanation
typeinstudy2(employeesatisfaction).FirstPref barisforthemostpreferredexplanationtypeandThird
forleastpreferred.
Domain1-CreditScoring:Beforedoingtheanalysis,weusedtheattentioncheckquestionto
exclude participants who may not have been engaged with the task. Of the 39 participants, we
excludedthosewhodidnotranktheattentioncheckquestionastheirlastpreferencefortwoor
morescenariosoutofsix.Thatis,ifaparticipantmadeoneerrorwithrankingtheattentioncheck
question,wediscardedthatranking,keepingtheotherfive.If,however,aparticipantmadetwo
or more errors, we removed the participant completely from the dataset. After elimination, we
had32participants.Allanalysispresentedinthefollowingsectionsisbasedontheremaining32
participants.Themeantaskcompletiontimewas27minutes(SD =11mins).
5.2.1 ParticipantDemographics. AllparticipantswerefromtheUnitedStates.Around57%self-
identifiedasmales,40%asfemales,and3%didnotstatetheirgender.Intermsofage,32%were25
to34,36%were35to44,25%were45to54,andtherestwereabove55(7%).Regardingeducation,
18% were high school graduates, 14% had some college but no degree, 64% had an Associate’s
orBachelor’sdegree,and4%hadaDoctoraldegree.Regardingfamiliaritywiththedomain,27%
reportedthattheywereslightlyfamiliarwiththeloanapplicationprocesses,48%weremoderately
familiar,18%wereveryfamiliar,and7%wereextremelyfamiliar.
5.2.2 ExplanationTypePreference. Weprovidedparticipantswithanon-directiveexplanation
andtwoformsofdirectiveexplanations.Figure1(a)showsparticipants’explanationtypechoices
forthethreepreferences.Directive-specificexplanationwasthemostpreferred,providingstrong
evidence that directive explanations are well accepted in this domain. Overall, we collected 192
rankings.Ofthe192first-preferencechoices,81(42%)werefordirective-specificexplanations,51
(27%)fordirective-genericexplanations,and60(31%)fornon-directiveexplanations.Achi-square
goodness-of-fit test was performed to examine the likelihood of the participants’ choices being
uniform.Thelikelihoodofobservingthedataifthechoicesforthemostpreferredexplanations
wererandomislow, χ2(2,N =191) =7.58,p <0.02.Similarresultswereobtainedforthesecond
andthirdpreferences(seeAppendixA).
5.2.3 Directive-specificExplanationsPreferredforUnfavorableDecisions. Weencodedthedata
such that we had the counts of the three types of explanations by each participant’s preference.
Essentially,werepresentedthenumberoftimesaparticipantchoseeachexplanationtypeoverthe
eightscenarios.Assuch,foreachparticipant,wehadninevalues.Thefirstthreewerethecountsof
eachexplanationtypetheparticipantchoseasthefirstpreference,thenextthreewerethecounts
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:12 R.Singhetal.
of the explanation types for the second preference, and the last three for the third preference.
The first-preference counts represent the number of times each participant would have given a
particularexplanationtypetoacustomer.
Weperformedanon-parametricFriedmantestofthedifferencesbetweenthenumberoftimes
the participants chose each explanation type. We did this test for the first, second, and third
preferences separately. We did not find significant differences between the number of times
each participant chose an explanation type, χ2(2) = 3.07,p < 0.23,Kendall (cid:4) s W = 0.05. This
suggests that, overall, participants chose each explanation type almost equally for the eight
scenarios.
Weseparatelyanalyzedtheparticipants’preferencesforscenarioswheretheloanwasapproved
(favorableoutcome,threescenarios)andthosewheretheloanwasdenied(threescenarios).We
performedanon-parametricFriedmantestofthedifferencesbetweenthenumberoftimeseach
explanationtypewaschosenbyparticipantswhentheloanwasapproved.Wefoundnosignificant
differences between explanation type choices, χ2(2) = 2.58,p = 0.27,Kendall (cid:4) s W = 0.04. We
found that non-directive explanation was chosen for (M = 1.21,SD = 0.8) scenarios, directive-
specific explanations for (M = 1.0,SD = 0.8) scenarios, and directive-generic explanations for
(M =0.78,SD =0.1)scenarios.
We performed a non-parametric Friedman test of the differences between the number of
times each explanation type was chosen by participants for scenarios when the loan was
denied. We found significant differences between explanation type choices, χ2(2) = 10.75,p =
0.004,Kendall (cid:4) s W = 0.17. We performed the Nemenyi post hoc analysis and found that
directive-specificexplanationwaschosenforsignificantlymorescenarios (M = 1.53,SD = 0.9)
thannon-directiveexplanations (M =0.65,SD =0.7,p < 0.001) andformoderatelysignificantly
morescenariosthandirective-genericexplanations(M =0.81,SD =0.8,p =0.05).
Theabovesuggeststhatdirective-specificexplanationwasmoresuitablewhenthedecisionwas
unfavorable.
5.2.4 ScenarioandIndividualPreferencesInfluencedChoices. Theanalysissofarshowedthat
thechoiceswerenotrandom. Toinvestigatewhichfactorsinfluencedthesechoices,wefirstex-
aminedwhetherthescenarioinfluencedthepreferredexplanationtype.Weencodedthedatato
getthecountsofeachexplanationtypegroupedbyscenarioforfirstpreference.
We then examined whether we could explain the choices by a combination of scenario and
individual preferences. Individual preferences were encoded as the proportion of choices for
non-directive and directive-specific explanations, noting that directive-generic explanation was
linearly dependent (we could compute counts of directive-generic choices given the other two).
In other words, we computed the probability of the participants choosing non-directive and
directive-specificexplanations.Weencodedthescenarioeffectsastheaveragenumberofchoices
for non-directive and directive-specific explanations, that is, the probability of participants
choosingnon-directiveanddirective-specificexplanationsforeachscenario.Usingthisdata,we
thenbuiltandcomparedtwomultinomiallogitmodelsusingthemlogit libraryinR.
The first model was built using directive-generic explanation as the base outcome and us-
ing only the individual preferences. We found that on average, the participant was a good pre-
dictor of which explanation type choice would be made for a given scenario ((cid:2) = −156.48,
McFadden R2 = 0.25,χ2 = 101.64,p < 0.001). Then, we built a model with both the scenario
effectsandindividualdifferences.Wefoundthatboththescenarioandindividualdifferencesinflu-
encedthechoiceofexplanationtype ((cid:2) = −129.33,McFaddenR2 = 0.38,χ2 = 155.95,p < 0.001).
Also,alikelihoodratiotestshowedthatthesecondmodel(withbothscenarioandindividualdif-
ferences)wassignificantlybetterthanthefirst(χ2(1) =54.31,p <0.001).
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:13
Domain2-EmployeeSatisfaction:Weusedthesameattentioncheckquestionandcriteriaas
indomain1toeliminateparticipantswhomaynothavebeenengaged.Ofthe40participantswho
completedtheexperiment,afterelimination,33remained.Allanalysispresentedinthefollowing
sectionsisbasedontheremaining33participants.Themeantaskcompletiontimewas28minutes
(SD =12mins).
5.2.5 ParticipantDemographics. AllparticipantswerefromtheUnitedStates.Around50%self-
identifiedasmales,48%asfemales,and3%didnotstatetheirgender.Intermsofage,23%were25
to34,39%were35to44,23%were45to54,andtherestwereabove55(15%).Regardingeducation,
13% were high school graduates, 13% had some college but no degree, 65% had an Associate’s
orBachelor’sdegree,and9%hadaMaster’sdegree.Regardingfamiliaritywiththedomain,36%
reported that they were slightly familiar with the human resource management processes, 45%
weremoderatelyfamiliar,15%wereveryfamiliar,and4%wereextremelyfamiliar.
5.2.6 Explanation Type Preference. Figure 1(b) shows participants’ explanation type choices
for the three preferences. Participants chose directive-generic explanations more than directive-
specific, and the non-directive explanation was least preferred, providing strong evidence that
thetwodirectiveexplanationsarewellacceptedintheemployeesatisfactiondomain.Overall,we
collected183rankings.Ofthe183first-preferencechoices,94(51%)wereofdirective-genericex-
planations,64(35%)ofdirective-specificexplanations,and25(14%)ofnon-directiveexplanations.
A chi-square goodness-of-fit test was performed to examine the likelihood of the participants’
choicesbeinguniform.Thelikelihoodofobservingthedataifthechoicesforthemostpreferred
explanationswererandomislow, χ2(2,N = 183) = 39.25,p < 0.001.Weobtainedsimilarresults
forthesecondandthirdpreferences(seeAppendixA).
5.2.7 Directive-genericExplanationsPreferredbyMostParticipants. Westartedbyencodingthe
dataaswedidforthecreditscoringdomain;thatis,foreachparticipant,wehadninevalues.The
firstthreewerethecountsofeachexplanationtypetheparticipantchoseasthefirstpreference,
thenextthreewerethecountsoftheexplanationtypesforthesecondpreference,andthelastthree
forthethirdpreference.Thefirstpreferencecountsessentiallyrepresentthenumberoftimeseach
participantwouldhavegivenanexplanationtypetoanemployee’ssupervisor.
Weperformedanon-parametricFriedmantestofthedifferencesbetweenthenumberoftimes
the participants chose each explanation type. We did this test for the first, second, and third
preferences separately. For the first preference, we found significant differences between expla-
nation type choices, χ2(2) = 30.07,p < 0.001,Kendall (cid:4) s W = 0.47. We performed the Ne-
menyi post hoc analysis and found that for the first preference, directive-generic explanation
(M = 2.98,SD = 1.2) was chosen for significantly more scenarios than non-directive explana-
tions(M =0.78,SD =1.0,p <0.001),butwedidnotfindanysignificantdifferencewhenitcame
todirective-specificexplanations (M = 2.0,SD = 1.10,p = 0.13).Thedirective-specificexplana-
tions were chosen for significantly more scenarios than non-directive explanations (p = 0.003).
Weobtainedsimilarresultsforthesecondandthirdpreferences(seeAppendixA).
Weseparatelyanalyzedthescenarioswhereanemployeewasmorelikelytostaythanresign
(favorableoutcome)andthosewheretheemployeewaspredictedtoleave.Weperformedanon-
parametricFriedmantestofthedifferencesbetweenthenumberoftimeseachexplanationtype
was chosen by participants for scenarios when the employee was not likely to leave. We found
significantdifferencesbetweenexplanationtypechoices, χ2(2) = 2.26,p < 0.001,Kendall (cid:4) sW =
0.39.TheNemenyiposthocanalysisfoundthatdirective-genericexplanation(M =1.81,SD =0.9)
was chosen for significantly more scenarios than non-directive explanations (M = 0.62,SD =
0.7,p =0.001)anddirective-specificexplanations(M =0.43,SD =0.7,p <0.001).
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:14 R.Singhetal.
Weperformedanon-parametricFriedmantestofthedifferencesbetweenthenumberoftimes
each explanation type was chosen by participants for scenarios when the employee was likely
to leave or resign. We found significant differences between explanation type choices, χ2(2) =
32.62,p < 0.001,Kendall (cid:4) sW = 0.5.TheNemenyiposthocanalysisfoundthatdirective-specific
explanation (M =1.56,SD =0.8)waschosenforsignificantlymorescenariosthannon-directive
explanations (M = 0.16,SD = 0.4,p < 0.001) butnotdirective-specificexplanations1.13,SD =
0.8,p =0.53).
The results show a shift in the preferred explanation type from directive-generic to directive-
specific when the decision was not favorable, suggesting, like the credit scoring domain, that
directive-specificexplanationwasmoresuitablewhenthedecisionwasunfavorable.
6 STUDY2
We repeated our study using almost the same procedure and a similar number of participants
(ending up with 54 participants from 70 after elimination) to learn why participants chose
their most preferred explanation. We added seven more scenarios, taking the total number of
scenariosto15.Thistime,theparticipantswererequiredtoranktheexplanationsfrommostto
least preferred to indicate which explanation they were most likely to use to communicate the
decision to the concerned individual for all 15 scenarios and provide reasons for their selection
in an open-ended text box. We asked the participants to answer one open-ended question
after ranking the explanations, which was: Please provide the reason(s) for choosing the most
preferred explanation over the other three explanations. We asked this question to learn why
participants chose their explanations. We include the quantitative analysis for this study in
AppendixE.
We performed a thematic analysis of the participants’reasons. However, we did the thematic
analysisforthetwotasksseparately.First,weperformedathematicanalysisforthecreditscoring
task. Then, to test the generalizability of the codes and themes, we ran a validation sub-study
to code the reasons for employee satisfaction tasks using the codes and themes from the credit
scoring task. This sub-study aimed to validate the model from the credit scoring domain, that
is, to learn to what extent the codes and themes from the credit scoring domain translated to
employeesatisfaction.
6.1 QualitativeAnalysisforCreditScoringTask
Toperformthethematicanalysis,wefollowedthestepsoutlinedintheexistingliteratureonthe-
maticanalysis[10,21,56].Inparticular,wefollowedNowelletal.[56],whoprovideastep-by-step
guidetoensurethatthisqualitativedataanalysisisprecise,consistent,andexhaustive.Weformed
agroupofthree(allauthorsonthearticle),withtheleadauthoranalyzinganddocumentingthe
process,thecodes,andthethemes.Twoothermembersverifiedthecodesandthemesbycritically
analyzingthese,andthroughtriangulation,thethreeresearchersdecidedonthefinallistofcodes
andthemesaftermultipleiterations.
Duringcoding,itbecameclearthatitwashelpfultoorganizethecodesaccordingtowhether
ornottheycouldbeusedtopredicttheparticipants’choices.Wecodedreasonsasnon-predictive
if the participantwas justifying the choice and indicated what factor the participantconsidered
was the most important when making a choice, but we could not determine which specific
explanation the participant chose based on this response. Otherwise, the code was predictive,
and of the four themes, three contained predictive codes. The four themes were Action-related,
Language-related,Usefulness/practical,andNon-predictive.
Figure2showsthethemesandcodesthatresultedfromthethematicanalysis.Definitionsfor
thecodescanbefoundinAppendixD.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:15
.sedocdnasemehT
.2.giF
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:16 R.Singhetal.
Action-related: This theme encompassed all responses that we considered to be action-related.
Most participants preferred directive explanations precisely because they explicitly told the
recipient (e.g., the customer) what he or she needed to do. We saw earlier that individual
preferences influenced preference for explanation type. Participants were split between the
two directive explanations, and some did not want directives. Several participants preferred the
directiveexplanationbecauseithadmultipleoptions.Forexample,P15stated:
“ThisexplanationprovidesalternativesforAmirtogetahigherspendinglimit.”
The directive-generic explanations were meant to promote the autonomy of the individuals
tryingtoachieverecourse.Thiswasindeedrecognizedbyparticipantschoosingdirective-generic
explanationsandsummarizedwellbyP9:
“Thepreferredoption[directive-generic]isthemostflexibleintermsofhowEvancan
increase their income. It doesn’t limit him to just getting another job, but he can get
creativewithhowtoincreasehisincome.”
Otherparticipantschosedirective-specificexplanationsbecausethisexplanationtypewasspe-
cific. That is, it provided clear actions for an individual to take. For example, P42 provided the
followingreasonforchoosingthedirective-specificexplanation:
“My first preference [directive-specific] gives her a realistic option on what she has to
do.My2ndoption[directive-generic]isnotbadbutdoesn’tseemtobeasspecific.The
3rdpreference [non-directive]ishonestbutwillleavethecustomerwonderingwhatto
donext.”
Noteveryonepreferreddirectiveexplanations.Therewereseveralreasonsparticipantswerenot
attractedtodirectives.Participantschosethenon-directiveexplanationbecausetheydidnotprefer
totelltherecipientwhattodo.Inthesecircumstances,thenon-directiveexplanationwassufficient
toindicatetotherecipientwhenthedecisionwouldchangeinsteadofprovidingdirectives.For
example,P53stated:
“Option one [non-directive] because two [directive-specific] and three [directive-
generic]aretellingherwhattodoandwillmakethemmad.”
Wealsofoundthatparticipantscarefullyanalyzedthedirectiveswhenchoosingthedirective
explanations, looking at the practical value of the suggested directives in the short term or the
long term. For example, P20 provided the following reason for selecting a directive explanation
(theloanwasapproved):
“It [directive-generic]providesreasonsfortheapprovalbutalsowaysinwhichhecan
ensurehecontinuestogetapprovedinthefuture.”
Knowing what one is doing right may be particularly important for business customers, who
mayrequirecreditmultipletimesoverthelifeofthebusiness.
Usefulness/practical:Thisthemeincludedallreasonsthatalludedtotheusefulnessorpractical-
ityofexplanations.Weincludedcounterfactualinformationinallexplanations.Participantsfound
thecounterfactualinformationusefulnotonlytoknowwhenthedecisionoftheMLmodelwould
changebutalsotounderstandthelimitsorthedecisionboundary.Forexample,inscenarioswith
approvedloans,participantsoftenselectedexplanationsbecausetheexplanationhadinformation
aboutthedecisionboundarythatcouldhelpcustomersbehavetoensureapprovalinthefuture.
Forexample,P27mentionedthat:
“The explanation I chose [directive-specific] explains why he was denied the best and
whatamounthecouldapplyforandbeapproved.”
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:17
Severalparticipantstriedtoimaginehowreasonableorfeasibletheexplanationwouldlikelybe
fortherecipient.Forexample,P43providedthefollowingjustificationfortheirchoice:
“Ipicked [directive-generic]basedonhowfeasibleIthoughteachstrategywouldbe.”
Theaboveexampleindicatesthatparticipantswereengaginginperspective-takingandtrying
tojudgethecostofthedirectivessuggestedfortherecipient.
Theexplainermaynotalwaysbeawareofhowcostly orhowactionabletheexplanationtruly
is.Onewayfortheexplainertoknowthehiddencostsisthroughdialogue[49,68],thatis,explic-
itlyrequestingthisinformation.Thissuggeststhatdialogueisprobablynecessarywhenthereis
uncertaintyaroundthefeasibilityofanactionablecounterfactualexplanation.
Finally, many participants did not feel the need to explain, especially when the loan applica-
tion was approved or the employee was unlikely to resign. If the participant indicated that an
explanationwasunnecessary,theytypicallychosethenon-directive.Forexample,P4:
“Hegotapproved.He’snotlookingforalong-windedexplanationofwhy,justthesimplest
(ifhereadtheexplanationatall).”
Language-related:Thisthemeencompassedallresponsesthatsuggestedthatlanguage-related
factors influenced the participant’s choice. Participants were attracted (mostly toward non-
directiveexplanations)tosimple,short,ordirectexplanations.Wefoundthatparticipantswerepar-
ticularlyattractedtonon-directiveexplanationsinScenario3.Inthisscenario,thecustomer’sloan
wasdeniedbecauseoftheincome,andthetwodirectiveexplanationssuggestedthatthecustomer
couldincreasehisincomebychanginghisjob,findingasecondjob,orgettingapromotion.Many
participantsfoundthesetwoexplanations“condescending” or“impolite.”Forexample,P6wrote:
“Thefirsttwooptions[directive-specificanddirective-generic]feelcondescendingand
don’t take into account Evan’s personal situation. He may not be able to increase his
income.Thethirdone[non-directive]ismorematter-of-factanddoesn’ttrytogetinto
Evan’spersonallife.”
Wenotethatoursuggestionsinthedirectiveexplanationsareverysimilartothetipscommonly
foundonfinancialadvicewebsites.Itappearsthatpeoplemaybecomfortablereadingthisinforma-
tionontheirownbutnotbeing“told”todosowithinanexplanation.Assuch,fromanalgorithmic
standpoint,itappearsthattheremaybespecificattributes/featuresforwhichanon-directiveex-
planationisamorereasonableoptionthantellingpeoplehowtoact.
Non-predictivereasons:Ourfinalthemewascreatedtocatertoresponsesthatdidnotpredict
the explanation type chosen by participants, which is why they are described as non-predictive.
Therewerefoursub-themesunderthenon-predictivetheme:readability/informative,tone,opinion,
andmiscellaneous.Manyparticipantsjustifiedtheirchoiceintermsoftheclarityoftheexplana-
tionsorifexplanationswereinformative.Forexample,P34stated:
“This explanation [directive-generic] is clear and is easily understandable when com-
paredtoothers.”
Weobservedthatparticipantsjustifiedtheirchoicebasedontone,thatis,howpoliteorfriendly
theexplanationswere,howdiplomaticorprofessionaltheysounded,orhowitwouldhavemade
therecipientfeel.Forexample,P26wrotethatanexplanationcouldcomeoutasimpolite:
“Becausethatexplanation[directive-specific] gentlyexplainsthecustomersthewhole
scenarioratherthenbeingjustrude.theytoldifinstalmentisbeenmissedfor6months|
that’saclearpointtheymadeforcustomer.andcustomerwillalsoknowthedeadends.”
Someparticipantsjustifiedtheirchoicebyexpressinganopiniontowardanexplanation:
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:18 R.Singhetal.
“Heneedsrelieffromtravellingandheneedsprofessionaldevelopmenttohelphimengage
withco-workersbetter.”
Finally,manyothercodeswerethinandfellunderthenon-predictive category;wedecidedto
collectthemunderthemiscellaneoussub-theme.
6.2 QualitativeAnalysisforEmployeeSatisfactionTask
We ran a validation study to test the generalizability of the codes and themes we had identified
whencodingthereasonsfromthecreditscoringtask.Thegoalofthisstudywastovalidatethe
model, that is, to see to what extent the codes and themes translated to another domain. To do
this,werecruitedsixcoders.Weintroducedthecodebookfromthefirststudytothesixcodersby
havinganinitial30-minutebriefingwheretheleadauthorexplainedthegoalofthetask(which
wastocodethereasonssothatwecouldunderstandwhyaparticipantchoseaparticulartypeof
explanation),theexistingcodebookfromstudy1withexamples,andtheprocedurethatthecoders
hadtofollow.Followingthis,thecodersdida60-minutetutorialpreparedbytheleadauthorthat
explained how the lead author would have coded a few examples. The tutorial also included a
practicesetof10reasonsfortheparticipanttogetfamiliarwiththecodebook.Weheldafurther
45-minutebriefingtoclarifyanyquestionsandgothroughsixfurtherexamples.Theparticipants
hadaround3.5hourstocodearound180reasons.WeusedQualtricstoadministerthetask,and
thecoderswerecompensatedatAUD$50perhour.Becausewehadaround360reasonstocode,
wesplitthereasonsintotwogroupsof180reasonsandcreatedaseparatesurveyforeachgroup
of180reasons.Werandomlyallocatedthesixcoderstooneofthesurveys.
Foreachreason,weprovidedthecoderswithasimplifiedversionoftheemployeeprofile,the
participant’s selected explanation, and the two other valid explanations that the participant re-
ceived.Foreachexplanation,weincludedtheexplanationtype(non-directive,directive-specific,
anddirective-generic)sothatthecoderswereawareoftheexplanationtypechosenbythepartic-
ipantandcouldusethisinformationtocodethereasonbetter.Recallthatforthecreditscoring
domain,wecodedreasonsasnon-predictive iftheparticipantwasjustifyingthechoiceandindi-
catedwhatfactortheparticipantconsideredwasthemostimportantwhenmakingachoice,but
wecouldnotdeterminewhichspecificexplanationtheparticipantchosebasedonthisresponse.
Otherwise,thecodewaspredictive,andofthefourthemes,threecontainedpredictivecodes.We
includedtheexplanationtypetohelpthecodersfollowthesameprocess.
Followingtheemployeeprofileandexplanations,weprovidedthereasontheparticipantpro-
videdusfortheirmostpreferredexplanation.Afterthereason,welistedthe54codesfromstudy
1 as multiple-choice options; coders could choose more than one, and if none of the codes ap-
propriately described the reason, they selected the miscellaneous:other option. Coders were also
allowedtolistanynewcodesthattheyfeltwereappropriateforthereason.Theinstructionsto
thecodersweretobeasgranularaspossiblewhencomingupwithnewcodes,andtheleadauthor
providedexamplesofhowtodothisduringtheinitialmeetings.Thecodersassessedeachreason
oneatatimewiththeoptionofreturningtopreviouslycodedreasons.However,nocoderdidthis
becauseoftheinconvenienceofclickingthebackbuttonrepeatedly.WeconfiguredQualtricsso
thatacodercouldstopmultipletimesandcompletethecodingovermultipledays.Mostcoders
completedthetaskwithin2workingdays.
Weanalyzedthedataforthetwogroupsof180reasonsseparatelyandthencombinedtheresults
ofthetwosurveys.Ourfirstanalysiswastoseethenumberofnewcodes(orthemes)thatwere
required.Thesixcodersgeneratedeightnewcodesthatcovered3%ofthecodes.Thatis,97%of
reasonscouldbecodedusingthemodelproducedinthecreditriskstudy.
Next,weinvestigatedtheagreementatthecodelevel.Weonlycountedcodesthattwoofthe
threecodersassignedtoeachreason.Therationaleisthatitispossibleforcoderstochoosesimilar
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:19
butnotthesamecodesforareason.Foreachreason,thecodershadachoiceof54codes.Wetook
the majority code—if two coders assign the same code to a reason, we assume it is the correct
code(s).Atleasttwocodersassignedthesamecodefor254/360(70%)reasons,andwediscarded
theother30%beforefurtheranalysis.
Wealsoanalyzedtheagreementatthethemelevel.Naturally,athemeconsistsofmultiplecodes,
andcoderscouldchoosedifferentcodeswithineachtheme.Therefore,welookedatwhetherthe
coders agreed on the theme. Note that the coders were responsible for assigning the codes, not
the themes. At a theme level, the agreement was 91%. Overall, we observed that the codes and
themesfromthecreditscoringdomainhadgoodcoverage(itcovered97%ofthereasonsfromthe
employeesatisfactiondomain).
The top two themes were Action-related (33% of codes) and Usefulness/practical (20%). The
opinionandmiscellaneousthemeswere17%and16%,respectively.Finally,thelowesttwowere
Readability/informativeandLanguagewith9%and5%ofthecodes,respectively.
7 DISCUSSION
In this article, we proposed directive explanations, that is, explanations that give individuals di-
rectives for recourse for machine learning decisions. We assert that actionable explanations can
beimprovedbyexplicitlyprovidingpeoplewithasingleorasequenceofactionstochangethe
decisions.Weevaluatedthepreferenceforandperceptiontowarddirectiveexplanationsovernon-
directive ones through two user studies, one in the space of credit scoring and the other in em-
ployeesatisfactiondomains.
Ourquantitativeanalysisindicatesastrongpreferenceforthetwodirectiveexplanations.The
participants’firstandsecondpreferencesweremostlyforthetwodirectiveexplanations.Inthe
credit scoring domain, 69% chose one of the two directive explanations as their most preferred
explanation, and for the employee satisfaction domain, 86% did so. Our results suggest that the
twodirectiveexplanationscomplement(non-directive)counterfactualexplanations[54,59,76,78].
While we show that explanations should be directive, we found that participants were spread
betweendirective-specificanddirective-genericexplanationsbetweenthetwodomains.
Participantschosedirective-specificexplanationsbecausetheyprovidedaspecificsolutionto
helptherecipientachieverecourse,particularlywhenthedecisionwasnotfavorable(whenthe
loanwasdeniedoranemployeewaslikelytoresign).Forexample,inthesecondstudy,oneofthe
participantslikedthatthedirective-specificexplanationprovidedspecificadvice:
“Ichosemymostpreferredexplanation [directive-specific]becauseitgetsattherootof
theproblem(travel)andoffersupagoodsuggestiononhowtosolvethatproblem.”
Conversely,sometimesparticipantspreferreddirective-genericexplanationsbecausetheywere
perceived as providing some autonomy for peopleto choose theirown specificcourse of action
to achieve recourse. This finding echoes that of Binns et al. [8], who reported that their partici-
pantsthoughtthatprovidingalternativestopeoplewhenthedecisionisnotfavorablewasagood
idea. Generally, directive-generic explanations are most suitable when someone prefers options
oratleasthasorfeelssomesenseofagencywhendecidingthespecificcourseofaction.Forex-
ample,aparticipantprovidedthefollowingreasoninginstudy2forchoosingadirective-generic
explanation:
“Ilikethisreason [directive-generic]becauseitsetcleargoalsforwhichareasneedto
beimproved,speciallytravelandjobsatisfaction,whichisinlinewithherresponsibility
expectationwhensheacceptedthejob.Also,itgivessuggestiontoachievethegoalswhile
allowingfreedomtothesupervisortochoosethemeansandmethods.”
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:20 R.Singhetal.
We noted a higher preference for directive-generic explanations in the employee satisfaction
domain.Webelievethatthiscouldbeduetoafewreasons.First,participantswereslightlymore
familiarwiththecreditdomainthantheemployeedomain(69%statedthattheywerebetweenmod-
eratelyandextremelyfamiliarwiththecreditdomain,while57%statedthattheywerebetween
moderately and extremely familiar with the employee domain). This could be why people were
more comfortable suggesting directive-specific explanations in the credit domain and directive-
generic explanations in the employee domain. Second, we believe that most people would have
their own ideas on improving job satisfaction, which would have a lot of personal preferences.
Therefore,itwaspotentiallyeasierfortheHRofficertoleavethespecificcourseofactionthatthe
employee’ssupervisorwouldtaketoimprovethejobsatisfactionoftheconcernedemployee.On
theotherhand,recourseforcreditscoringisaboutchangingbehaviorto“game”thecreditscoring
model,withwhichmanypeoplewouldhavelimitedexperience,somoreconcreteadvicewould
beappreciated.
Whilewesawsignificantsupportfordirectiveexplanations,around31%and13%ofresponses
in the two domains were for non-directive explanations. One of the main reasons participants
sometimeschosenon-directiveexplanationswasthedecision;manyparticipantssuggestedthat
whenthedecisionisfavorable,themostimportantinformationiswhenthedecisionislikelyto
change (counterfactual information) and not necessarily how that would happen, as one of the
participantsdescribesbelow:
“I like the basic and simple explanation that overtime could cause him to resign [non-
directive]. I don’t think you should try to give a reason for it, just whether or not it
happens.”
Variousotherfactorspotentiallyinfluencedthechoiceofanexplanationtype.Insomescenarios,
thechoicewasimpactedbysocialfactors.Inonecreditscoring,thedirectiveexplanationsuggested
thatthecustomerchangejobs,dopart-timework,ortrytogetapromotiontoincreasetheirin-
come(theserecommendationsarecommononvariouswebsitesthatprovidefinancialadvice).For
thisscenario,participantswerealmostevenlydistributedbetweentheexplanationtypes.However,
manyparticipantshighlightedthatitwascondescendingtotellpeopletochangetheirjobs.Insev-
eralscenariosintheemployeesatisfactiondomain,wefoundthattheparticipantswerechoosing
directivesbasedonwhichonemakesanemployeehappier.Forexample,oneoftheparticipants
wrotethefollowingforchoosingadirective-genericexplanation:
“Ichoosemymostpreferredovertheothersbecauseitgivesthesuggestiontoremovehis
overtimebutwouldallowhimtodotheprojectsmoreeffectivelyandquicker,savingthe
companybothtimeandmoneyandprobablymakinghimahappieremployee.”
Socio-technical systems usually have many stakeholders. For example, credit risk assessment
involvescustomers,datamodelers,modelbuilders,modelusers(suchasloanofficers),andothers.
The roles influence the relevance of different types of explanations [32, 73]. This could explain
whysomeparticipantsfounddirectiveexplanationshelpfulwhileothersdidnot.
Theabovediscussionsimplythatitisnotstraightforwardtoselectbetweenexplanationtypes,
reinforcingthatwecannotdecideaprioriwhethernon-directiveordirectiveexplanationsaremore
suitable for all individuals in all circumstances. This finding is not limited to directives explana-
tions.Forexample,Ehsanetal.[27]foundthatforrationalegeneration,participants’requirements
forthetypeofexplanationwascontext-dependent;theypreferredshortandsimplerationalesto
understandagents,butdetailedrationalesforidentifyingfailureorunexpectedbehavior.Thus,the
explanationtypechoiceisinfluencedbyindividual,social,andcontextualfactors,andwhatisor
isnotactionablemustbeidentifiedbytheindividualconcerned[46,58,79].
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:21
Tosummarize:
• We find a clear preference for the two directive explanations over non-directive counter-
factualexplanationsintwodomains;thenon-directiveexplanationwastheleastpreferred
explanationtype.
• Directive-specificexplanationsaremoresuitedtoscenarioswheretheoutcomeisunfavor-
able.Wefoundthatinscenarioswheretheloanwasdeniedortheemployeewaslikelyto
leave,theparticipantsstronglypreferreddirective-specificexplanations.Thissuggeststhat
in the two domains, explanations should be constructed so that there are options for peo-
pletoreceivedirectiveexplanations.Wefindastrongpreferenceforit,whichsuggeststhat
peoplewillfindituseful.
• Thedomainmayinfluencethepreferenceforthetwodirectiveexplanations(seediscussion
aboveforahigherpreferencefordirective-genericexplanationintheemployeesatisfaction
domain).
• Non-directivesareunsuitablewhentheoutcomeisfavorableforthecreditscoringdomain.
Thenon-directiveexplanationsprovidedecisionboundariesthatwillbeusefultocontinue
goodfinancialbehaviors.Intheemployeesatisfactiondomain,thedominantpreferencefor
a directive-generic explanation could be because people may want to encourage positive
behaviorsandkeeppeopleemployedforlonger.
7.1 Limitations
Ourstudiesinvolvedanautomatedsystemexplainingtoanintermediarywhytheautomatedsys-
tem made a particular decision, such as denying a loan. The intermediary then selected one of
four possible explanations to provide to the client. In many contexts, such as loan applications,
webelievethatanautomatedsystemassistspeople(loanofficers)whoassistothers(customers).
Therefore,thissetupallowsustounderstandwhatahumanconsidersrelevantwhenexplaining
decisionstoanotherhumanandprovideinsightsfromthisperspective.However,wedoacknowl-
edgethatourstudyislimitedtothesesettings.
We noted limitations in terms of the context that we explored. In the credit scoring domain,
participantsfeltthatexplanationswereofnovaluewhenloanswereapproved.However,wedo
notbelievethisholdsinallcontexts.Forexample,ifwehadtoldtheparticipantsthatthecustomer
wasabusinesscustomerwhoregularlyappliesforloans,thismayhaveelicitedadifferentresponse
from these participants; for someone who applies for loans regularly, knowing why a loan was
approvedisusefulasitindicateswhattheyshoulddonexttimetheyapplyforaloan.
Tohaveconfidencethatdirectiveexplanationswereusefulindifferentdomains,weconducted
studiesincreditscoringandhumanresourcespaces.However,weneedfurtherstudiesinother
domainstofullyunderstandtheimplicationsofdirectiveexplanations.
We were also limited by the data collection method, as we could not run this in a lab setting
due to social isolation restrictions resulting from the COVID-19 pandemic. Had we run it in a
lab setting, there were many instances where we would have asked follow-up questions to the
participants.Assuch,theinputprovidedbytheparticipantsthroughthetwoopen-endedquestions
couldbeimprovedifwehadtheopportunitytoclarifytheresponses.
Furthermore,allparticipantsinourstudieswerefromtheUnitedStates,andwecouldpotentially
observeadifferentresultifwerecruitedparticipantsfromdifferentcountries.Severalfactors,such
asculturalvalues,mayinfluencepreferences[20].Forexample,usersfromdifferentbackgrounds
respondeddifferentlytorobotrecommendations(Asianparticipantschangedtheirdecisionsmore
thanUS-basedparticipantswhencollaboratingwithrobots)[80].Therefore,itislikelythatusers
outsideoftheUnitedStatesmayhavedifferentexplanationtypepreferences.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:22 R.Singhetal.
7.2 FutureWork
Theresultsofourpresentstudyindicatesupportforbothnon-directiveanddirectiveexplanations.
First,weidentifiedthatpreferencesfordirectivevs.non-directiveexplanationsdependonmulti-
plefactors.Furtherworkisrequiredtoclarifywhy thesefactorsmatterandhowtheyinfluence
the selection of the explanation types across domains. Such exploration could include studying
preferencesfromadifferentperspective,suchasfromtheperspectiveoftheloanapplicantorthe
employee’ssupervisor.
Further work is needed to understand the effectiveness of directive explanations. Our results
showaclearpreferencefordirectiveexplanations.Thenextstepwillbetoshowhoweffectively
theyimproveactionability.Ourscenariodesigndoesnotconsiderthecostofchanginganattribute
orthefeasibilityoftheactions,andwefoundthatparticipantsreflectedonthisanditsurfacedin
thethematicanalysis.Futureworkshouldexplorescenarioframingtocontrolcostandfeasibility
andstudytheimplicationsonpreferences.
The actions we used in our MDP model were sourced from multiple public websites to get
goodcoverageofthetypesofrecommendationsthatcouldbeincludedinthedirectiveexplana-
tions.Futureworkcouldlookatotherwaystogatherappropriateactions,suchasfromexpertsor
crowdsourcing.
Efficientmodelsareneededtogeneratedirectiveexplanations.Recently,Karimietal.[38]pro-
posedusingstructuralcausalmodelsasoneoption.Madumaletal.[50]alsoshowedthatpeople
may better understand models that employ a causal lens to generate explanations. Future work
could also involve generating and evaluating diverse directives [41] and comparing MDP-based
modelstostructuralcausalmodels[22,33,37,52,74].
Whilewehavenotconsidereddiverse directives,therearenumerousmethodstomeasurethe
plan differences, and we could use these to devise a metric to compute multiple diverse direc-
tives[12,41].Moreover,wecouldusetherewardscomputedbythemodeltoinformtheuserof
themodel’spreferencesoverthesedirectivestomaketheselectioneasierfortheuser.
Another avenue for increasing diversity is by considering multiple counterfactuals. In recent
work,Dandletal.[23]proposedtheMulti-ObjectiveCounterfactuals(MOC)methodandused
multi-objective optimization to find a diverse set of counterfactuals with different tradeoffs be-
tweentheproposedobjectives.Wecouldalsocombinethemethodin[23]withtheoneproposed
by [13], which uses counterfactual constraints to search for a limited but more desirable set of
counterfactuals.Oncewehavethediversesetofcounterfactuals,wecoulduseourmodeltogen-
eratedirectivesforeachandpresentthesetotheuserasoptionswiththehopethatthisfurther
increasestheactionabilityofdirectiveexplanations.Thisapproachmayalsoberelevantformulti-
class problems, especially when the user may have preferences for multiple different outcomes
(classes).
Wecouldconsiderwaystopersonalizeexplanations.Researchsuggestsprovidingmultiplenon-
directiveexplanationsinthehopethatoneofthemwillbeactionablefortherecipient[65,77,78].
Ourresultsshowthatnotallindividualswishtoreceivemultipleexplanations.Atthesametime,
knowing the cost of action for an individual is also important—some of our participants were
thinkingaboutthis,soanautomatedsystemshouldalsoconsiderthis.Onewaytoestablishthe
costofacertainactionisthroughaninteractionwithindividuals(see,e.g.,[68]).Throughdialogue,
wecanidentifytheactionsindividualsaremorecomfortablewithand,therefore,betterpersonalize
theexplanationtotheindividual’spreferencesandcircumstances.Wecouldalsoexploreasking
individuals their preferences over feature values and constraining the counterfactuals to satisfy
theseconstraints,assuggestedin[67].Thisapproachdoesrequireindividualstodivulgepersonal
information [77], but the benefit is that they may be able to receive a more tailored and better
explanation.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:23
Inrecentwork,[13]proposesusingcounterfactualconstraintsanddistancemeasurestostudy
therobustnessofmachinelearningmodelsacrosseachfeature.Inthecreditscoringdomain,they
showed that their method generated counterfactual explanations that allow designers to under-
standtherobustnessofmachinelearningmodels.Futureworkcouldexplorethedifferentdistance
measuresandtheirimpactonthemodelweusetogeneratethedirectives.
Finally,wecouldextendourworkbyexplainingwhythemodelbelievesthedirectivesarelikely
tohelptheusersachievetheirgoals.Thereisgrowingliteratureinthespaceofexplainableplan-
ning[19,29,44,69]thatwecouldleverageconcerningexplaining whythesuggesteddirectiveis
morelikelytohelpusersachievetheirgoalsoverotherpossibilities.
8 CONCLUSION
Weformallydefinedandinvestigateddirectiveexplanationsinthisarticle.Theseexplanationspro-
vide individuals directives for recourse of machine learning decisions, that is, inform people on
how to act. The pursuit of our goal to investigate people’s perception toward directive explana-
tionsleadsustosomeinterestingfindings.Althoughwedemonstratedsignificantsupportfordi-
rectiveexplanations,weconcludethatwecannotalwayspleaseallpeople.Explanationpreference
issubjectiveanddependsonmultiplefactors;thus,wecannotgenericallydeterminethemostsuit-
abletypeofexplanation.Thisreinforcesthecalltotakeahuman-centeredandsituation-specific
approachtoexplainableAI,especiallywhenlookingatwaysofmakingexplanationsactionable.
REFERENCES
[1] AminaAdadiandMohammedBerrada.2018.Peekinginsidetheblack-box:Asurveyonexplainableartificialintelli-
gence(XAI).IEEEAccess6(2018),52138–52160.
[2] CharuC.Aggarwal,ChenChen,andJiaweiHan.2010.Theinverseclassificationproblem.JournalofComputerScience
andTechnology25,3(2010),458–468.
[3] MuhammadAurangzebAhmad,CarlyEckert,andAnkurTeredesai.2018.Interpretablemachinelearninginhealth-
care.InProceedingsofthe2018ACMInternationalConferenceonBioinformatics,ComputationalBiology,andHealth
Informatics(BCB’18).AssociationforComputingMachinery,NewYork,NY,559–560.
[4] KatieAtkinson,TrevorBench-Capon,andDanushkaBollegala.2020.ExplanationinAIandlaw:Past,presentand
future.Artif.Intell.289(Dec.2020),103387.
[5] NikolaBanovic,AnqiWang,YanfengJin,ChristieChang,JulianRamos,AnindDey,andJenniferMankoff.2017.Lever-
aginghumanroutinemodelstodetectandgeneratehumanbehaviors.InProceedingsofthe2017CHIConferenceon
HumanFactorsinComputingSystems(CHI’17).AssociationforComputingMachinery,NewYork,NY,6683–6694.
[6] SolonBarocas,AndrewD.Selbst,andManishRaghavan.2020.Thehiddenassumptionsbehindcounterfactualex-
planationsandprincipalreasons.InProceedingsofthe2020ConferenceonFairness,Accountability,andTransparency
(FAT*’20).AssociationforComputingMachinery,NewYork,NY,80–89.
[7] RichardBellman.1957.AMarkoviandecisionprocess.JournalofMathematicsandMechanics6,5(1957),679–684.
[8] ReubenBinns,MaxVanKleek,MichaelVeale,UlrikLyngs,JunZhao,andNigelShadbolt.2018.“It’sreducingahuman
beingtoapercentage”:Perceptionsofjusticeinalgorithmicdecisions.InProceedingsofthe2018CHIConferenceon
HumanFactorsinComputingSystems(CHI’18).AssociationforComputingMachinery,NewYork,NY,1–14.
[9] BiranandCotton.2017.Explanationandjustificationinmachinelearning:Asurvey.InIJCAI-17WorkshoponExplain-
ableAI(XAI),Vol.8.cs.columbia.edu,8–13.
[10] VirginiaBraunandVictoriaClarke.2006.Usingthematicanalysisinpsychology.QualitativeResearchinPsychology
3,2(2006),77–101.
[11] CameronB.Browne,EdwardPowley,DanielWhitehouse,SimonM.Lucas,PeterI.Cowling,PhilippRohlfshagen,
StephenTavener,DiegoPerez,SpyridonSamothrakis,andSimonColton.2012.AsurveyofMonteCarlotreesearch
methods.IEEETrans.Comput.Intell.AIGames4,1(March2012),1–43.
[12] DanielBryce.2014.Landmark-basedplandistancemeasuresfordiverseplanning.ICAPS24(May2014),56–64.
[13] AndreasC.Bueff,MateuszCytryński,RaffaellaCalabrese,MatthewJones,JohnRoberts,JonathonMoore,andIain
Brown.2022.Machinelearninginterpretabilityforastressscenariogenerationincreditscoringbasedoncounterfac-
tuals.ExpertSyst.Appl.202(Sept.2022),117271.
[14] LarsBuesing,TheophaneWeber,YoriZwols,SebastienRacaniere,ArthurGuez,Jean-BaptisteLespiau,andNicolas
Heess.2018.Woulda,coulda,shoulda:Counterfactually-guidedpolicysearch.(Nov.2018).arXiv:1811.06272[cs.LG]
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:24 R.Singhetal.
[15] MichaelBuhrmester,TracyKwang,andSamuelD.Gosling.2011.Amazon’sMechanicalTurk:Anewsourceofinex-
pensive,yethigh-quality,data?Perspect.Psychol.Sci.6,1(Jan.2011),3–5.
[16] NiklasBussmann,PaoloGiudici,DimitriMarinelli,andJochenPapenbrock.2020.ExplainableAIinfintechriskman-
agement.Front.Artif.Intell.3(April2020),26.
[17] RuthM.J.Byrne.2016.Counterfactualthought.AnnualReviewofPsychology67(2016),135–157.
[18] RuthM.J.Byrne.2019.Counterfactualsinexplainableartificialintelligence(XAI):Evidencefromhumanreasoning.
Proceedingsofthe28thInternationalJointConferenceonArtificialIntelligence(IJCAI’19Macao,10-16August2019),
ijcai.org,6276–6282.
[19] TathagataChakraborti,SarathSreedharan,YuZhang,andSubbaraoKambhampati.2017.Planexplanationsasmodel
reconciliation:Movingbeyondexplanationassoliloquy.(Jan.2017).arXiv:1701.08317[cs.AI]
[20] LarissaChazetteandKurtSchneider.2020.Explainabilityasanon-functionalrequirement:Challengesandrecom-
mendations.RequirementsEngineering25,4(Dec.2020),493–514.
[21] VictoriaClarkeandVirginiaBraun.2014.Thematicanalysis.(2014),1947–1952.https://doi.org/10.1007/978-1-4614-
5583-7_311
[22] ElliotCreager,DavidMadras,ToniannPitassi,andRichardZemel.2020.Causalmodelingforfairnessindynamical
systems.InProceedingsofthe37thInternationalConferenceonMachineLearning(ProceedingsofMachineLearning
Research,Vol.119),HalDauméIiiandAartiSingh(Eds.).PMLR,2185–2195.
[23] SusanneDandl,ChristophMolnar,MartinBinder,andBerndBischl.2020.Multi-objectivecounterfactualexplanations.
InParallelProblemSolvingfromNature(PPSNXVI).SpringerInternationalPublishing,448–469.
[24] JinshuoDong,AaronRoth,ZacharySchutzman,BoWaggoner,andZhiweiStevenWu.2018.Strategicclassification
fromrevealedpreferences.InProceedingsofthe2018ACMConferenceonEconomicsandComputation(EC’18Ithaca,
NY,USA,June18-22,2018),ÉvaTardos,EdithElkind,andRakeshVohra(Eds.).ACM,55–70.https://doi.org/10.1145/
3219166.3219193
[25] TriDungDuong,QianLi,andGuandongXu.2021.Prototype-basedcounterfactualexplanationforcausalclassifica-
tion.(May2021).arXiv:2105.00703[cs.LG]
[26] LilianEdwardsandMichaelVeale.2017.Slavetothealgorithm:Whyarighttoanexplanationisprobablynotthe
remedyyouarelookingfor.DukeL.&Tech.Rev.16(2017),18.
[27] UpolEhsan,PradyumnaTambwekar,LarryChan,BrentHarrison,andMarkO.Riedl.2019.Automatedrationale
generation:AtechniqueforexplainableAIanditseffectsonhumanperceptions.InProceedingsofthe24thInternational
ConferenceonIntelligentUserInterfaces(IUI’19).AssociationforComputingMachinery,NewYork,NY,263–274.
[28] AlhusseinFawzi,OmarFawzi,andPascalFrossard.2018.Analysisofclassifiers’robustnesstoadversarialperturba-
tions.MachineLearning107,3(2018),481–508.
[29] MariaFox,DerekLong,andDanieleMagazzeni.2017.Explainableplanning.(Sept.2017).arXiv:1709.10256[cs.AI]
[30] HectorGeffnerandBlaiBonet.2013.Aconciseintroductiontomodelsandmethodsforautomatedplanning.Synthesis
LecturesonArtificialIntelligenceandMachineLearning8,1(2013),1–141.
[31] RiccardoGuidotti,AnnaMonreale,SalvatoreRuggieri,FrancoTurini,FoscaGiannotti,andDinoPedreschi.2019.A
surveyofmethodsforexplainingblackboxmodels.ACMComputingSurveys(CSUR)51,5(2019),93.
[32] MarkHall,DanielHarborne,RichardTomsett,VedranGaletic,SantiagoQuintana-Amate,AlistairNottle,andAlun
Preece.2019.AsystematicmethodtounderstandrequirementsforexplainableAI(XAI)systems.InProceedingsofthe
IJCAIWorkshoponeXplainableArtificialIntelligence(XAI’19),Vol.11.dais-ita.org.
[33] JosephY.HalpernandJudeaPearl.2020.Causesandexplanations:Astructural-modelapproach.PartI:Causes.Br.J.
Philos.Sci.(2020).
[34] MoritzHardt,NimrodMegiddo,ChristosPapadimitriou,andMaryWootters.2016.Strategicclassification.InProceed-
ingsofthe2016ACMConferenceonInnovationsinTheoreticalComputerScience(ITCS’16).AssociationforComputing
Machinery,NewYork,NY,111–122.
[35] RobertR.HoffmanandGaryKlein.2017.Explainingexplanation,part1:Theoreticalfoundations.IEEEIntelligent
Systems32,3(2017),68–73.
[36] AndreasHolzinger,ChrisBiemann,ConstantinosS.Pattichis,andDouglasB.Kell.2017.Whatdoweneedtobuild
explainableAIsystemsforthemedicaldomain?(Dec.2017).arXiv:1712.09923[cs.AI]
[37] MarkHopkinsandJudeaPearl.2007.Causalityandcounterfactualsinthesituationcalculus.J.LogicComput.17,
5(Oct.2007),939–953.
[38] Amir-HosseinKarimi,BernhardSchölkopf,andIsabelValera.2021.Algorithmicrecourse:Fromcounterfactualexpla-
nationstointerventions.(2021),353–362.https://doi.org/10.1145/3442188.3445899
[39] Amir-HosseinKarimi,GillesBarthe,BorjaBalle,andIsabelValera.2020.Model-agnosticcounterfactualexplanations
forconsequentialdecisions.InProceedingsofthe23rdInternationalConferenceonArtificialIntelligenceandStatistics
(ProceedingsofMachineLearningResearch,Vol.108),SilviaChiappaandRobertoCalandra(Eds.).PMLR,895–905.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

DirectiveExplanationsforActionableExplainabilityinMachineLearningApplications 23:25
[40] Amir-HosseinKarimi,JuliusvonKügelgen,BernhardSchölkopf,andIsabelValera.2020.Algorithmicrecourseunder
imperfectcausalknowledge:Aprobabilisticapproach.(June2020).arXiv:2006.06831[cs.LG]
[41] MichaelKatzandShirinSohrabi.2020.Reshapingdiverseplanning.AAAI34,06(April2020),9892–9899.
[42] JonKleinberg,HimabinduLakkaraju,JureLeskovec,JensLudwig,andSendhilMullainathan.2018.Humandecisions
andmachinepredictions.Q.J.Econ.133,1(Feb.2018),237–293.
[43] GunnarKönig,TimoFreiesleben,andMoritzGrosse-Wentrup.2021.Acausalperspectiveonmeaningfulandrobust
algorithmicrecourse.(July2021).arXiv:2107.07853[stat.ML]
[44] BenjaminKrarup,MichaelCashmore,DanieleMagazzeni,andTimMiller.2019.Model-basedcontrastiveexplanations
forexplainableplanning.InICAPS2019WorkshoponExplainableAIPlanning(XAIP’19).AAAIPress,9.
[45] DavidLewis.2013.Counterfactuals.JohnWiley&Sons.
[46] Q.VeraLiao,DanielGruen,andSarahMiller.2020.QuestioningtheAI:InformingdesignpracticesforexplainableAI
userexperiences.arXivpreprintarXiv:2001.02478(2020).
[47] BrianY.LimandAnindK.Dey.2009.Assessingdemandforintelligibilityincontext-awareapplications.In Ubiquitous
Computing,11thInternationalConference(UbiComp’09),Proceedings(ACMInternationalConferenceProceedingSeries),
SumiHelal,HansGellersen,andSunnyConsolvo(Eds.).ACM,195–204.https://doi.org/10.1145/1620545.1620576
[48] ZacharyC.Lipton.2018.Themythosofmodelinterpretability.Commun.ACM61,10(2018),36–43.https://doi.org/
10.1145/3233231
[49] PrashanMadumal,TimMiller,LizSonenberg,andFrankVetere.2019.Agroundedinteractionprotocolforexplainable
artificialintelligence.InProceedingsofthe18thInternationalConferenceonAutonomousAgentsandMultiAgentSystems
(AAMAS’19).InternationalFoundationforAutonomousAgentsandMultiagentSystems,1033–1041.
[50] PrashanMadumal,TimMiller,LizSonenberg,andFrankVetere.2020.Explainablereinforcementlearningthrougha
causallens.(2020),2493–2500.https://aaai.org/ojs/index.php/AAAI/article/view/5631.
[51] TimMiller.2019.Explanationinartificialintelligence:Insightsfromthesocialsciences.ArtificialIntelligence 267
(2019),1–38.
[52] TimMiller.2021.Contrastiveexplanation:Astructural-modelapproach.Knowl.Eng.Rev.36(2021),e14.
[53] ChristophMolnar.2020.InterpretableMachineLearning.Lulu.com.
[54] RamaravindK.Mothilal,AmitSharma,andChenhaoTan.2020.Explainingmachinelearningclassifiersthroughdi-
versecounterfactualexplanations.InProceedingsofthe2020ConferenceonFairness,Accountability,andTransparency.
607–617.
[55] Philip Naumann and Eirini Ntoutsi. 2021. Consequence-aware sequential counterfactual generation. (April 2021).
arXiv:2104.05592[cs.LG]
[56] LorelliS.Nowell,JillM.Norris,DeborahE.White,andNancyJ.Moules.2017.Thematicanalysis:Strivingtomeetthe
trustworthinesscriteria.InternationalJournalofQualitativeMethods16,1(2017),1609406917733847.
[57] MichaelOberstandDavidSontag.2019.Counterfactualoff-policyevaluationwithgumbel-maxstructuralcausalmod-
els.InInternationalConferenceonMachineLearning(ICML’19).proceedings.mlr.press,4881–4890.
[58] ForoughPoursabzi-Sangdeh,DanielG.Goldstein,JakeM.Hofman,JenniferWortmanWortmanVaughan,andHanna
Wallach.2021.Manipulatingandmeasuringmodelinterpretability.InProceedingsofthe2021CHIConferenceonHuman
FactorsinComputingSystems(CHI’21,Article237).AssociationforComputingMachinery,NewYork,NY,1–52.
[59] RafaelPoyiadzi,KacperSokol,RaúlSantos-Rodríguez,TijlDeBie,andPeterA.Flach.2020.FACE:Feasibleandac-
tionablecounterfactualexplanations.InAAAI/ACMConferenceonAI,Ethics,andSociety(AIES’20,NewYork,NY,USA,
February7-8,2020),AnnetteN.Markham,JuliaPowles,TobyWalsh,andAnneL.Washington(Eds.).ACM,344–350.
https://doi.org/10.1145/3375627.3375850
[60] MartinL.Puterman.2014.MarkovDecisionProcesses:DiscreteStochasticDynamicProgramming.JohnWiley&Sons.
[61] EmileeRader,KelleyCotter,andJangheeCho.2018.Explanationsasmechanismsforsupportingalgorithmictrans-
parency.InProceedingsofthe2018CHIConferenceonHumanFactorsinComputingSystems(CHI’18).Associationfor
ComputingMachinery,NewYork,NY,1–13.
[62] MarcoTúlioRibeiro,SameerSingh,andCarlosGuestrin.2016.“WhyshouldItrustyou?”:Explainingthepredictions
ofanyclassifier.InProceedingsofthe22ndACMSIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining,BalajiKrishnapuram,MohakShah,AlexanderJ.Smola,CharuC.Aggarwal,DouShen,andRajeevRastogi
(Eds.).ACM,1135–1144.https://doi.org/10.1145/2939672.2939778
[63] MarcoTúlioRibeiro,SameerSingh,andCarlosGuestrin.2018.Anchors:High-precisionmodel-agnosticexplanations.
InProceedingsofthe32ndAAAIConferenceonArtificialIntelligence(AAAI’18),the30thinnovativeApplicationsof
ArtificialIntelligence(IAAI’18),andthe8thAAAISymposiumonEducationalAdvancesinArtificialIntelligence(EAAI-
18,NewOrleans,Louisiana,USA,February2-7,2018),SheilaA.McIlraithandKilianQ.Weinberger(Eds.).AAAIPress,
1527–1535.https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/view/16982.
[64] CynthiaRudin.2019.Stopexplainingblackboxmachinelearningmodelsforhighstakesdecisionsanduseinter-
pretablemodelsinstead.NatureMachineIntelligence1,5(2019),206–215.
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.

23:26 R.Singhetal.
[65] ChrisRussell.2019.Efficientsearchfordiversecoherentexplanations.InProceedingsoftheConferenceonFairness,
Accountability,andTransparency(FAccT’19,Atlanta,GA,USA,January29-31,2019),DanahBoydandJamieH.Mor-
genstern(Eds.).ACM,20–28.https://doi.org/10.1145/3287560.3287569
[66] AndrewD.SelbstandSolonBarocas.2018.Theintuitiveappealofexplainablemachines.FordhamL.Rev.87(2018),
1085.
[67] ShubhamSharma,JetteHenderson,andJoydeepGhosh.2019.CERTIFAI:Counterfactualexplanationsforrobustness,
transparency,interpretability,andfairnessofartificialintelligencemodels.(May2019).arXiv:1905.07857[cs.LG]
[68] KacperSokolandPeterA.Flach.2020.Oneexplanationdoesnotfitall:Thepromiseofinteractiveexplanationsfor
machinelearningtransparency.CoRRabs/2001.09734(2020).arXiv:2001.09734https://arxiv.org/abs/2001.09734.
[69] SarathSreedharan,AnaghaKulkarni,andSubbaraoKambhampati.2022.Explainablehuman–AIinteraction:Aplan-
ningperspective.SynthesisLecturesonArtificialIntelligenceandMachineLearning16,1(Jan.2022),1–184.
[70] BiplavSrivastava,TuanAnhNguyen,AlfonsoGerevini,SubbaraoKambhampati,MinhBinhDo,andIvanSerina.2007.
Domainindependentapproachesforfindingdiverseplans.In Proceedingsofthe20thInternationalJointConference
onArtificialIntelligence(IJCAI’07,Hyderabad,India,January6-12,2007),ManuelaM.Veloso(Ed.).2016–2022.http:
//ijcai.org/Proceedings/07/Papers/325.pdf.
[71] RichardS.SuttonandAndrewG.Barto.2018.ReinforcementLearning:AnIntroduction(2nded.).MITPress.
[72] WinnieF.Taylor.1980.MeetingtheEqualCreditOpportunityAct’sspecificityrequirement:Judgmentalandstatistical
scoringsystems.Buff.L.Rev.29(1980),73.
[73] Richard Tomsett, Dave Braines, Dan Harborne, Alun D. Preece, and Supriyo Chakraborty. 2018. Interpretable to
whom? A role-based model for analyzing interpretable machine learning systems. CoRR abs/1806.07552 (2018).
arXiv:1806.07552http://arxiv.org/abs/1806.07552.
[74] StratisTsirtsis,AbirDe,andManuelGomez-Rodriguez. 2021.Counterfactualexplanationsinsequentialdecision
makingunderuncertainty.(July2021).arXiv:2107.02776[cs.LG]
[75] StratisTsirtsisandManuelGomez-Rodriguez.2020.Decisions,counterfactualexplanationsandstrategicbehavior.
(Feb.2020).arXiv:2002.04333[cs.LG]
[76] BerkUtsun,AlexanderSpangher,andYangLiu.2019.Actionablerecourseinlinearclassification.InProceedingsof
theConferenceonFairness,Accountability,andTransparency(FAccT’19,Atlanta,GA,USA,January29-31,2019),Danah
BoydandJamieH.Morgenstern(Eds.).ACM,10–19.https://doi.org/10.1145/3287560.3287566
[77] SureshVenkatasubramanianandMarkAlfano.2020.Thephilosophicalbasisofalgorithmicrecourse.In Conference
onFairness,Accountability,andTransparency(FAccT’20,Barcelona,Spain,January27-30,2020),MireilleHildebrandt,
CarlosCastillo,L.ElisaCelis,SalvatoreRuggieri,LinnetTaylor,andGabrielaZanfir-Fortuna(Eds.).ACM,284–293.
https://doi.org/10.1145/3351095.3372876
[78] SandraWachter,BrentMittelstadt,andChrisRussell.2017.Counterfactualexplanationswithoutopeningtheblack
box:AutomateddecisionsandtheGDPR.Harv.J.L.&Tech.31(2017),841.
[79] DandingWang,QianYang,AshrafAbdul,andBrianY.Lim.2019.Designingtheory-drivenuser-centricexplainable
AI.InProceedingsofthe2019CHIConferenceonHumanFactorsinComputingSystems(CHI’19,NewYork,NY,USA,
May2019).Glasgow,1–15.
[80] LinWang,Pei-LuenPatrickRau,VanessaEvers,BenjaminKrisperRobinson,andPamelaHinds.2010.WheninRome:
Theroleofculture&contextinadherencetorobotrecommendations.In20105thACM/IEEEInternationalConference
onHuman-robotInteraction(HRI’10).ieeexplore.ieee.org,359–366.
Received21February2022;revised13September2022;accepted17December2022
ACMTransactionsonInteractiveIntelligentSystems,Vol.13,No.4,Article23.Publicationdate:December2023.