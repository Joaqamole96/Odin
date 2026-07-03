Received24April2026,accepted13May2026,dateofpublication20May2026,dateofcurrentversion27May2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3695458
Provably Adaptive Trust Dynamics in
Context-Aware Zero-Trust Systems: A Formal
Framework for Continuous Verification
VIVINKRISHNAN 1 ANDC.S.SREEJA 2,(SeniorMember,IEEE)
1DepartmentofComputerScience,CHRIST(DeemedtobeUniversity),Bengaluru,Karnataka560029,India
2CenterforQuantumTechnologiesandComplexSystems(CQTCS),CHRIST(DeemedtobeUniversity),Bengaluru,Karnataka560029,India
Correspondingauthor:VivinKrishnan(vivin.krishnan@res.christuniversity.in)
ABSTRACT Zero-Trust (ZT) requires continuous, context-aware evaluation of authentication and
authorization decisions. This paper introduces Zero-Trust Hybrid Adaptive Authentication (ZeTHAA),
a continuous authentication and authorization framework integrating contextual attributes, authentication
strength, behavioral evidence, and retry dynamics. ZeTHAA utilizes a probabilistic risk model and
dual-policythresholdstopartitionoutcomesintoallow,step-up,andblockregions,enablingprecisecontrol
over security–usability trade-offs. The system introduces a global admissibility predicate to distinguish
hardviolationsfromprobabilisticsoftviolations.Attributeimportanceisdynamicallyderivedfromentropy
andBeta-posteriordistribution,enablingrobustcold-startinitializationandonlinerecalibration.ZeTHAA
presents a unified composite attack surface covering credential compromise, attribute forgery, and post-
grant hijacking, modeling retry behavior with exponential risk escalation and temporal decay. A large-
scalesyntheticdatasetcapturingrealisticauthenticationflows,adversarialandtemporalpatterns,wasused
to evaluate ZeTHAA against heuristic, logistic regression, random forest, XGBoost, and isolation forest
baselines.ZeTHAAproducedamoreexpressiveriskdistributionandsignificantlyhigherattackdetection
andefficiencywhileminimizinguserfriction.ZeTHAAoutperformedbaselinemodels,withRecallandArea
UndertheCurve(AUC)exceeding79%and15.1%,respectively.F1-Scoreshowedincreasesof48%-147%,
with efficiency boost of 20-65%, while reducing the cost per attack by up to 39.6%. Benchmarks against
frameworks from Dasu et al. and Matiushin et al. showed a 57.5% lead in F1-Score, more than double
increase in detection rate, while blocking 70.78% more attacks. Additional analysis shows that ZeTHAA
providesamathematicallygroundedfoundationforZero-Trustsystems,alignswithNISTstandards,offering
improvedsecurityguaranteesandadaptiveenforcement.
INDEXTERMS Adaptiveauthentication,applicationintegritycheck,Bayesianonlinelearning,continuous
authentication,deviceauthentication,dynamicsecretinjection,risk-basedaccesscontrol.
I. INTRODUCTION The need for secure authentication accelerated the devel-
Single-factor authentication (SFA) schemes have been the opmentofmultifactorauthentication(MFA)systems,which
mainstay of authentication because of their usability and are more secure [5], [6]; however, MFA remains a static
easeofimplementation[1].However,ascomputingresources approachthatreliesonsequentialchainingofauthentication
andthreatvectorsbecomeincreasinglysophisticated,attacks challenges [7]. Blancaflor et al. [8] reported sophisticated
on SFA systems have become commonplace [2], [3]. With attack measures that specifically target MFA systems. The
SFA, the attacker must focus on breaking only a single layering of challenges also contributes to user friction
authenticationmethod[4]. and reduces usability and adoption [9]. Traditional MFA
techniques,whileeffectiveinbolsteringsecurity,frequently
The associate editor coordinating the review of this manuscript and leadto‘‘MFAfatigue’’anduserfrustrationduetorepetitive
approvingitforpublicationwasSedatAkleylek . prompts,eveninlow-riskscenarios[10].
2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME14,2026 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 77839

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Consequently, Adaptive Authentication (AA) systems, posture,behavioralcontext,accessmedium,application
which utilize users’ behavioral and contextual patterns to attributes, and threat indicators) and transforms them
challengeuserssparinglywhenbehaviordeviatesfromestab- intoanormalizedriskmetricfortrustevolution.
lishedpatterns,havegainedpopularity[11].AAincorporates • Trustevolutionwithreinforcementandtemporaldecay
contextual signals such as device posture, geolocation, dynamics.
behavioral biometrics, and network attributes to compute • Parameterization and recalibration of weighting and
dynamicriskscores.Whenthebehavioralcontextofarequest penaltycoefficients.
varies from the established profile, the system selects an • Explicitmappingoftruststatetopolicydecisionswithin
alternative authentication modality to challenge the user. ZeroTrustarchitecture.
The complexity of the selected alternative authentication • Standards-aligned architectural integration, including
modality is proportional to the risk of malicious agents identity,application,anddevicetrustconsiderations.
accessing resources. In contrast to MFA, AA employs a Formulate and evaluate a hypothesis that policy-aware
•
dynamic strategy in which risk factors are considered when multi-threshold authentication improves the trade-off
selecting the subsequent action. This evolution in security betweensecurityandusability.
design is largely driven by the inherent tension between The remainder of this paper is organized as follows.
| achieving | robust | protection | and | maintaining | enhanced | user |         |             |     |          |           |     |                |     |
| --------- | ------ | ---------- | --- | ----------- | -------- | ---- | ------- | ----------- | --- | -------- | --------- | --- | -------------- | --- |
|           |        |            |     |             |          |      | Section | II outlines | the | research | questions |     | and hypotheses |     |
experiences[12].
|     |     |     |     |     |     |     | guiding | the proposed |     | framework. |     | Section | III presents | the |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ---------- | --- | ------- | ------------ | --- |
As authentication systems began to incorporate adaptive foundational principles of Zero Trust Architecture and
| and risk-based |     | authentication |     | (RBA), a | new cybersecurity |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | -------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
relevantstandards.SectionIVpresentsadetailedanalysisof
design paradigm, i.e., zero-trust (ZT), evolved in parallel, theexistingliteratureinthefieldandidentifieskeyresearch
withmanyenterprisesadoptingitasthedrivingprinciple.ZT, gaps. Section V discusses the methodology of the proposed
| which revolves |     | around | the principle | of  | ‘‘never | trust, always |        |           |     |                |     |     |                 |     |
| -------------- | --- | ------ | ------------- | --- | ------- | ------------- | ------ | --------- | --- | -------------- | --- | --- | --------------- | --- |
|                |     |        |               |     |         |               | ZeTHAA | framework |     | and formulates |     | the | trust evolution |     |
verify’’,ensuresthatnoimplicittrustisassignedtousersor model. Section VI formalizes the security guarantees of the
resourcesregardlessoflocation(physicalornetwork)[13].
|     |     |     |     |     |     |     | ZeTHAA | framework, |     | followed | by  | experimental | evaluation |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | -------- | --- | ------------ | ---------- | --- |
However, many risk-based systems rely on heuristic or and findings in section VII. Finally, Section VIII concludes
| proprietary  | scoring      | mechanisms, |               | and             | they typically | lack        | thepaper. |     |     |     |     |     |     |     |
| ------------ | ------------ | ----------- | ------------- | --------------- | -------------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| a formalized | mathematical |             |               | model governing |                | trust accu- |           |     |     |     |     |     |     |     |
| mulation,    | decay,       | and         | re-evaluation | over            | time.          | This gap    |           |     |     |     |     |     |     |     |
II. RESEARCHQUESTIONSANDHYPOTHESES
| motivates | a transition |     | from | authentication-centric |     | security |              |     |             |     |            |     |            |     |
| --------- | ------------ | --- | ---- | ---------------------- | --- | -------- | ------------ | --- | ----------- | --- | ---------- | --- | ---------- | --- |
|           |              |     |      |                        |     |          | We establish | the | theoretical |     | foundation | by  | presenting | the |
toarchitecturalparadigmsthatassumepersistentadversarial
researchquestionsandhypothesesthatunderpintheproposed
presence.
framework.
| This          | paper | presents   | ZeTHAA | - a      | novel | convergence |     |     |     |     |     |     |     |     |
| ------------- | ----- | ---------- | ------ | -------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| of Zero-Trust |       | philosophy | into   | Adaptive | and   | Continuous  |     |     |     |     |     |     |     |     |
A. RESEARCHQUESTIONS
| Authentication. |     | This | work | is based | on the | hypothesis |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ---- | -------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
AAandRBAsystemshavetraditionallyfocusedonimprov-
| that incorporating |     | policy-aware, |     | multi-threshold |     | decision |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------------- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ingclassificationaccuracythroughenhancedriskestimation
| mechanisms  | into        | risk-based |          | authentication | systems | leads          |                 |                |                     |         |     |              |          |          |
| ----------- | ----------- | ---------- | -------- | -------------- | ------- | -------------- | --------------- | -------------- | ------------------- | ------- | --- | ------------ | -------- | -------- |
|             |             |            |          |                |         |                | using heuristic |                | or machine-learning |         |     | approaches.  | However, |          |
| to improved | operational |            | outcomes | compared       |         | to traditional |                 |                |                     |         |     |              |          |          |
|             |             |            |          |                |         |                | real-world      | authentication |                     | systems |     | must balance |          | security |
single-thresholdapproaches.TheproposedZero-Trust-based
|                  |     |                |        |                   |          |           | (attack        | detection) | with     | usability   | (user | friction | and       | cost), |
| ---------------- | --- | -------------- | ------ | ----------------- | -------- | --------- | -------------- | ---------- | -------- | ----------- | ----- | -------- | --------- | ------ |
| hybrid Adaptive  |     | Authentication |        | system            | operates | on a com- |                |            |          |             |       |          |           |        |
|                  |     |                |        |                   |          |           | with decisions |            | governed | by policies |       | rather   | than risk | scores |
| posite attribute |     | set that       | covers | all participating |          | discrete  |                |            |          |             |       |          |           |        |
alone.
| entities. | The system |          | covers | the actor,         | the | medium of |         |          |      |      |           |     |               |     |
| --------- | ---------- | -------- | ------ | ------------------ | --- | --------- | ------- | -------- | ---- | ---- | --------- | --- | ------------- | --- |
|           |            |          |        |                    |     |           | In this | context, | this | work | is guided | by  | the following |     |
| access,   | and the    | platform | it     | runs, establishing |     | a ‘‘who - |         |          |      |      |           |     |               |     |
researchquestions:
| uses what | - on | which’’ | relationship. | This | allows | for the |     |     |     |     |     |     |     |     |
| --------- | ---- | ------- | ------------- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
• RQ1:Doesincorporatingpolicy-aware,multi-threshold
| collection | of a | wider | range | of attributes | while | employ- |     |     |     |     |     |     |     |     |
| ---------- | ---- | ----- | ----- | ------------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ing a minimally invasive profile. The hybrid nature of decision mechanisms improve the trade-off between
|              |        |     |         |                |     |            | security | and | usability | compared |     | to traditional |     | single- |
| ------------ | ------ | --- | ------- | -------------- | --- | ---------- | -------- | --- | --------- | -------- | --- | -------------- | --- | ------- |
| the proposed | system |     | enables | the validation | of  | contextual |          |     |           |          |     |                |     |         |
thresholdRBAapproaches?
attributes,groupedbytheircomposition,inparallel,thereby
• RQ2:Canmulti-stagedecisionregions(allow,step-up,
allowingfasteroutcomes.Thekeycontributionsofthispaper
block)reducefalseblockingrateswithoutsignificantly
are:
• Formalization of trust as a continuous, time-evolving, degradingattackdetectionperformance?
|     |         |       |          |             |          |         | • RQ3:  | Does       | the calibration |         | of  | model outputs |         | to oper- |
| --- | ------- | ----- | -------- | ----------- | -------- | ------- | ------- | ---------- | --------------- | ------- | --- | ------------- | ------- | -------- |
| and | bounded | state | variable | rather than | a binary | policy- |         |            |                 |         |     |               |         |          |
|     |         |       |          |             |          |         | ational | thresholds |                 | improve | the | alignment     | between | risk     |
basedoutcome.
Assurance-awareTrustinitialization,integratingauthen- estimationandauthenticationdecisions?
•
ticationandidentitystrengths. These questions aim to shift the focus from risk pre-
• Contextual Risk aggregation framework that inte- diction alone to decision effectiveness under operational
| grates | multi-dimensional |     |     | contextual | signals | (device | constraints. |     |     |     |     |     |               |     |
| ------ | ----------------- | --- | --- | ---------- | ------- | ------- | ------------ | --- | --- | --- | --- | --- | ------------- | --- |
| 77840  |                   |     |     |            |         |         |              |     |     |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| B. RESEARCHHYPOTHESES |     |     |     |     |     |     | ThecoreprinciplesofZTAinclude: |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- |
Based on the above research questions, we formulate the • Eliminationofimplicittrust
followinghypotheses:
• Leastprivilegeaccessenforcement
• H1 (Trade-off Hypothesis): A policy-aware, dual- • Strictauthenticationandauthorizationactions
threshold authentication framework achieves a bet- • Continuous evaluation of signals for data-driven
| ter | balance | between | security |     | and usability | than |     |     |     |     |     |     |     |     |
| --- | ------- | ------- | -------- | --- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
decisions
single-thresholdAAorRBAapproaches. • DynamicPolicy-drivendecisionmechanisms
| • H2 | (Decision | Structure | Hypothesis): |     | Multi-threshold |     |     |     |     |     |     |     |     |     |
| ---- | --------- | --------- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
UndertheZTA,trustistreatedasdynamicandcontextual
| decision    |     | regions reduce |     | false-blocking |                  | rates while |             |           |         |              |              |        |            |      |
| ----------- | --- | -------------- | --- | -------------- | ---------------- | ----------- | ----------- | --------- | ------- | ------------ | ------------ | ------ | ---------- | ---- |
|             |     |                |     |                |                  |             | rather than | static    | and     | rule-driven. |              | Access | decisions  | are  |
| maintaining |     | comparable     | or  | improved       | attack-detection |             |             |           |         |              |              |        |            |      |
|             |     |                |     |                |                  |             | evaluated   | by policy | engines |              | that analyze |        | continuous | data |
performance.
|      |              |              |     |             |     |          | supplied | across | sources. | However, |     | while | ZTA articulates |     |
| ---- | ------------ | ------------ | --- | ----------- | --- | -------- | -------- | ------ | -------- | -------- | --- | ----- | --------------- | --- |
| • H3 | (Calibration | Hypothesis): |     | Calibration |     | of model |          |        |          |          |     |       |                 |     |
architecturalcomponents—policyenforcementpoints,policy
| outputs | to  | policy thresholds |     | improves | the | alignment |          |         |           |        |     |               |      |     |
| ------- | --- | ----------------- | --- | -------- | --- | --------- | -------- | ------- | --------- | ------ | --- | ------------- | ---- | --- |
|         |     |                   |     |          |     |           | decision | points, | and trust | signal |     | collectors—it | does | not |
between risk scores and authentication decisions, formallydefineaquantitativetrustfunctionoramethodology
enablingmoreeffectiveutilizationofdecisionregions.
forcontinuoustrustevolution.
C. HYPOTHESISEVALUATIONSTRATEGY
B. IDENTITYASSURANCEANDAUTHENTICATOR
| The hypotheses |     | were evaluated |     | through | a comprehensive |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
STRENGTH
| experimental | framework |     | using a | held-out | test dataset. | Each |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | ------- | -------- | ------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
NISTSP800-63,referredtoas‘‘DigitalIdentityGuidelines’’,
hypothesisistestedusingspecificmetrics:
standardizesauthenticationandidentityproofingforprivate
| • Operational |          | Trade-off | (H1): | Assessed |       | using cost- |            |        |              |     |           |        |            |     |
| ------------- | -------- | --------- | ----- | -------- | ----- | ----------- | ---------- | ------ | ------------ | --- | --------- | ------ | ---------- | --- |
|               |          |           |       |          |       |             | and public | sector | enterprises. |     | It covers | a Risk | Management |     |
| based         | metrics, | step-up   | rate, | block    | rate, | and false   |            |        |              |     |           |        |            |     |
Framework,alongwithIdentityandauthenticationlifecycle
| block | rate, | capturing | the | balance | between | security |     |     |     |     |     |     |     |     |
| ----- | ----- | --------- | --- | ------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
management,assurances,andassertions[14].
enforcementanduserfriction.
ThisframeworkdefinesIdentityAssuranceLevels(IAL),
| • Discrimination |     | Performance  |                | (H2): | Evaluated | using        |               |           |           |         |          |          |                   |         |
| ---------------- | --- | ------------ | -------------- | ----- | --------- | ------------ | ------------- | --------- | --------- | ------- | -------- | -------- | ----------------- | ------- |
|                  |     |              |                |       |           |              | Authenticator |           | Assurance | Levels  | (AAL),   |          | and Federation    |         |
| Receiver         |     | Operating    | Characteristic |       | (ROC)     | curves, Area |               |           |           |         |          |          |                   |         |
|                  |     |              |                |       |           |              | Assurance     | Levels    | (FAL)     | for     | identity | proofing | and               | authen- |
| Under            | the | Curve (AUC), | and            | Equal | Error     | Rate (EER),  |               |           |           |         |          |          |                   |         |
|                  |     |              |                |       |           |              | tication      | strength. | AAL       | defines | metrics  |          | that characterize |         |
whichmeasuretheabilitytodistinguishbetweenbenign
|     |     |     |     |     |     |     | the strength | of  | an authentication |     | process. |     | AALs 1-3 | offer |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------------- | --- | -------- | --- | -------- | ----- |
andmaliciousevents.
|     |     |     |     |     |     |     | an indicator | of  | confidence |     | in an | authentication | method. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ----- | -------------- | ------- | --- |
• DecisionAlignment(H3):Analyzedthroughcalibrated
|     |     |     |     |     |     |     | Higher assurance |     | levels | (e.g., | AAL2 | and | AAL3) mandate |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------ | ---- | --- | ------------- | --- |
riskscoredistributions,decisionboundaryanalysis,and
|             |     |          |         |          |         |        | stronger | authenticators, |     | including | cryptographic |     | hardware- |     |
| ----------- | --- | -------- | ------- | -------- | ------- | ------ | -------- | --------------- | --- | --------- | ------------- | --- | --------- | --- |
| region-wise |     | behavior | (allow, | step-up, | block), | demon- |          |                 |     |           |               |     |           |     |
boundcredentials.
| strating | how | well | model | outputs | align | with policy |          |       |           |     |      |        |                |     |
| -------- | --- | ---- | ----- | ------- | ----- | ----------- | -------- | ----- | --------- | --- | ---- | ------ | -------------- | --- |
|          |     |      |       |         |       |             | Although | these | standards |     | help | choose | authentication |     |
thresholds.
methodsbasedonsecurityneeds,theyremainlargelyfocused
Acomparativeevaluationwasconductedagainstheuristic
|             |                |     |           |     |             |          | on the strength |             | of the authentication |       |        | event  | itself. Assurance |     |
| ----------- | -------------- | --- | --------- | --- | ----------- | -------- | --------------- | ----------- | --------------------- | ----- | ------ | ------ | ----------------- | --- |
| and machine | learning-based |     | baselines |     | to validate | the pro- |                 |             |                       |       |        |        |                   |     |
|             |                |     |           |     |             |          | levels do       | not specify | how                   | trust | should | decay, | accumulate,       |     |
posedhypotheses.
|                  |       |                |           |                |            |             | or be recalibrated |             | during | an     | active     | session, | nor    | do they |
| ---------------- | ----- | -------------- | --------- | -------------- | ---------- | ----------- | ------------------ | ----------- | ------ | ------ | ---------- | -------- | ------ | ------- |
| Together,        | these | research       | questions | and            | hypotheses | estab-      |                    |             |        |        |            |          |        |         |
|                  |       |                |           |                |            |             | address            | the dynamic |        | threat | conditions | that     | emerge | after   |
| lish a framework |       | for evaluating |           | authentication |            | systems not |                    |             |        |        |            |          |        |         |
sessionestablishment.
| only in     | terms    | of predictive | accuracy, |             | but also | in terms   |     |     |     |     |     |     |     |     |
| ----------- | -------- | ------------- | --------- | ----------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| of decision | quality, | operational   |           | efficiency, | and      | real-world |     |     |     |     |     |     |     |     |
C. PHISHING-RESISTANTAUTHENTICATIONANDFIDO
applicability.
|     |     |     |     |     |     |     | The FIDO | Alliance | and | W3C’s | work | on  | phishing-resistant |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | ----- | ---- | --- | ------------------ | --- |
III. ZEROTRUSTARCHITECTUREANDSTANDARDS andlargelypasswordlessauthenticationmethodsresultedin
| CONTEXT |     |     |     |     |     |     | theFIDO2frameworkandtheWebAuthnstandard[15]. |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
A. ZEROTRUSTARCHITECTURE FIDO-based authentication aims to eliminate or replace
The Zero Trust paradigm operates on the tenet of ‘‘no shared secrets such as passwords or OTPs with public-key
implicit trust’’. ZT assumes that no entity is trustworthy, cryptography,whereprivatekeysaresecurelyboundtouser
regardless of user identity, network, or device posture. The devices and never transmitted over the network. By lever-
keyprinciplesandcomponentsoftheZeroTrustArchitecture aging device-bound hardware credentials, this architecture
(ZTA) have been formalized by the National Institute of provides strong resistance to phishing attacks, credential
Standards and Technology under NIST SP 800-207 [13]. replays,etc.,significantlystrengtheningauthentication.
ZTA mandates continuous authentication, and verification Nevertheless,similartootherauthenticationmechanisms,
of identity, device, and contextual attributes across all data FIDO aims to secure the authentication event rather than
points at all times before granting access to protected definingcontinuoustrustevaluationmechanismsthroughout
resources. thelifeofauthenticatedsessions.Theydonotprovideformal
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 77841 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
models for adaptive trust recalibration or continuous risk modalitiesbasedonauser’scontext.Theworkconcentrated
aggregation. onaccesstomobiledeviceapplicationsbasedonusercontext
andresourcesensitivity.AlthoughtheDRLapproachenables
|     |     |     |     |     |     | rapid learning | and | inference, | the system |     | lacks cold-start |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ---------- | --- | ---------------- | --- |
D. ARCHITECTURALGAPSINSTANDARDS-BASEDZERO
TRUSTIMPLEMENTATIONS initializationwhennopriordataareavailable.
Zero Trust architecture and identity assurance standards AnRBAimplementationforOpenStackwaspresentedby
|         |          |           |            |        |          | Unsel et al. | in [18]. | This study | attempts | to mitigate |     | the low |
| ------- | -------- | --------- | ---------- | ------ | -------- | ------------ | -------- | ---------- | -------- | ----------- | --- | ------- |
| provide | a robust | framework | for secure | access | control. |              |          |            |          |             |     |         |
However,theydonotdefineacomputationalmodelfortrust adoptionratesofRBA.However,theframeworkusesonlythe
IPaddress,round-trip-time(RTT),andUser-Agenttoevaluate
evaluationandrecalibration.Thisresultsinimplementations
relyingonarbitraryorheuristicscoringapproaches. variance from baseline behavior. Matiushin et al. proposed
|                |            |             |             |        |          | Machine    | Learning-Empowered |          | Risk-Based |             | Authentication |          |
| -------------- | ---------- | ----------- | ----------- | ------ | -------- | ---------- | ------------------ | -------- | ---------- | ----------- | -------------- | -------- |
| • Trust        | is treated | as a policy | outcome     | rather | than as  |            |                    |          |            |             |                |          |
|                |            |             |             |        |          | (MLE-RBA), | a LightGBM-based   |          | RBA        | framework,  |                | in [19]. |
| a continuously |            | monitored,  | measurable, | and    | evolving |            |                    |          |            |             |                |          |
|                |            |             |             |        |          | Although   | MLE-RBA            | operates | on a       | dynamically | computed       |          |
variable.
|     |     |     |     |     |     | binary threshold, |     | it focuses | on the mathematical |     | optimality |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | ------------------- | --- | ---------- | --- |
• Thereisnoformaldefinitionofhowcontextualsignals
|      |           |             |            |     |             | and does | not account | for | user friction | in  | the outcome. |     |
| ---- | --------- | ----------- | ---------- | --- | ----------- | -------- | ----------- | --- | ------------- | --- | ------------ | --- |
| from | different | sources are | aggregated | and | transformed |          |             |     |               |     |              |     |
Inaddition,theframeworkassumesthatpriordataisavailable
intoquantitativetrustmetrics.
|     |     |     |     |     |     | to compute | the threshold. |     | Further studies | on  | risk-based | and |
| --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | --------------- | --- | ---------- | --- |
Theparameterizationofreinforcingweightsordegrad-
•
|     |     |     |     |     |     | AA have | been proposed |     | by [20], | [21], [22], | [23], | [24], |
| --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | -------- | ----------- | ----- | ----- |
ingpenaltiesandtheirformulationisnotdefined.
and[25]thatutilizevariousattributessuchasusagepatterns,
| • Trust | decay, | recalibration, | and | convergence | during |     |     |     |     |     |     |     |
| ------- | ------ | -------------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
behavioralbiometrics,andsmartphoneusage.However,these
ongoingsessionsarenotmodeledformally.
|     |     |     |     |     |     | studies propose | binary | decision-making |     | systems | based | on  |
| --- | --- | --- | --- | --- | --- | --------------- | ------ | --------------- | --- | ------- | ----- | --- |
These limitations highlight a critical research gap: the singularbehavioralaspects,thatareindividuallysusceptible
| lack of | a formal | mathematical | framework |     | capable of |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
tospoofing.
modelingcontinuous,adaptivetrustcomputationwithinZero
|                      |     |               |         |         |          | RBA and | AA systems | focus | on the | authentication |     | phase, |
| -------------------- | --- | ------------- | ------- | ------- | -------- | ------- | ---------- | ----- | ------ | -------------- | --- | ------ |
| Trust architectures. |     | The following | section | surveys | existing |         |            |       |        |                |     |        |
andnotbeyondintopost-loginauthorizationrequests,token
| academic | approaches | that attempt | to address | aspects | of this |     |     |     |     |     |     |     |
| -------- | ---------- | ------------ | ---------- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
grants,andresourcerequests.Thisishandledbycontinuous
problemandidentifiestheremainingchallengesthatmotivate
authenticationsystems.
theproposedmodel.
| IV. RELATEDWORK |     |     |     |     |     | B. CONTINUOUSAUTHENTICATION |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
Strongsecuritysystemshavebeenapriorityareaofresearch
Continuousauthentication(CA)systemsfocusonvalidating
in both industry and academia, and previous studies on auser’sidentitywhileausersessionisinprogress.
implicitauthenticationusingbehavioralmetricssetthepath Acar et al. [26] presented a wearables-assisted CA
towardsAA.
|     |     |     |     |     |     | framework | that verifies | user        | identity | based | on keystroke |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------- | ----------- | -------- | ----- | ------------ | --- |
|     |     |     |     |     |     | dynamics  | detected      | by sensors. | The      | work  | proposed     | by  |
A. RISK-BASEDANDADAPTIVEAUTHENTICATION Buriroetal.[27]usedkeystrokedynamicsandtouch-timing
Risk-based authentication (RBA) and Adaptive Authenti- differences to continuously authenticate users throughout
cation (AA) for systems have been a growing focus of active sessions. The framework distinguishes itself from
study. RBA focuses on risk analysis using contextual and othersbynotrequiringuserstomemorizeafixedpassword.
behavioralsignals,comparingthemwiththeuser’shistorical Shen et al. presented a behavioral biometrics-based CA
profile, and derives a risk score. The risk score determines systemforsmartphones[28].Liangetal.[29]investigatedthe
whichauthenticatorswillbeemployedtochallengetheuser. useofwearable-devicebehavioralbiometricsforcontinuous
Adaptive authentication focuses on choosing authenticators authentication, in which ML was employed to derive
to activate based on the risk score derived from behavioral behavioralpatternsfrombiometricdata.In[30],Meknietal.
and contextual analysis. They represent an ‘‘at the point of presented a study in which CA was achieved using gait
authentication’’phase. biometrics and was enhanced using machine learning. The
Dasu et al. [16] proposed an Adaptive Authentication authorsemployedadeep-learning-basedclassifiertoenhance
framework to defend against identity threats. However, the authenticationaccuracy.Shahetal.intheirstudyoncontin-
authors adopt a heuristic approach to weight assignment, uousdevice-to-deviceauthenticationproposedalightweight
in which risk signal weights are assigned statically and CAframeworkthatutilizeschannelpropertiestodynamically
are independent of the data distribution and attack history. rotatesessionkeys[31].SimilarstudiesinCAhighlightthe
Furthermore, the variance computation is performed only growing interest in monitoring behavioral aspects for user
on the last 10 login records, limiting the scope of vari- identity verification, with a focus mainly on wearables and
ance computation to strictly heuristic and not statistical. mobile devices [32], [33], [34], [35]. While promising, the
Picard and Pierre [17] presented an RBA system that uses proposed CA systems effectively work on binary decision
deep reinforcement learning (DRL) to select authentication controls,wheretheuserrequestiseithertreatedasbenignor
| 77842 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
askedtostepuptheirauthentication.Hardviolations,suchas Attribute importance, spoofability, and temporal sta-
impossibletravels,andcryptographicbindingviolat,ions,are bility are set by fixed rules or expert heuristics. Sys-
notconsidered.Inaddition,decisionsaremadebyevaluating temslackcold-startstrategiesandonlinerecalibration
datafromlimitedbehavioralattributes,whichcanbespoofed methods[16],[54],[55].
individually, and by assuming that historical data will be 3) ImplicitTrust:
presentasthesystemisonline. Risk evaluation and trust computations are performed
Furthermore, established products in the cybersecurity only until the point of authentication. Post-login
domain, such as RSA Cybersecurity, CA Risk Authen- requestsareimplicitlydeemedvalidandfallwithinthe
tication, Okta, BIO-Key Portal Guard, Duo Risk-Based realmofimplicittrust[17],[18],[19].
Authentication, and IBM Security, employ risk-based AA 4) Lack of an explicit admissibility/safety invariant.
systems. However, the detailed working patterns of these Industrycontrols(e.g.,impossibletravelchecks,attes-
products,includingtheattributestheygatherandthemethods tation failures) are often implemented as scattered
employedtocreatethecontextualprofile,areproprietary. heuristics. There is little formal distinction between
|     |     |     |     |     |     |     | non-compensable |           |       | (hard) failures |     | and         | probabilistic |       |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | ----- | --------------- | --- | ----------- | ------------- | ----- |
|     |     |     |     |     |     |     | (soft)          | evidence, | which | complicates     |     | correctness |               | argu- |
C. ZERO-TRUSTSYSTEMS
mentsandpolicyproofs.
Zero-trust,asadesignphilosophy,isbeingrapidlyevaluated
|     |     |     |     |     |     |     | 5) Poor | integration |     | of retry/attack |     | dynamics |     | into |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --------------- | --- | -------- | --- | ---- |
andadoptedbyresearchersandindustry.
threatmodels.
| Hasan | et al. | in their | study | [36] presented |     | design and |       |          |         |         |          |     |           |     |
| ----- | ------ | -------- | ----- | -------------- | --- | ---------- | ----- | -------- | ------- | ------- | -------- | --- | --------- | --- |
|       |        |          |       |                |     |            | Retry | behavior | (failed | logins, | repeated |     | attempts) | is  |
assurancepatternsforZTcomponents.Withpatternlibraries
|            |           |                 |                 |          |                   |             | frequently |     | handled    | by synthetic | counters |      | or lockout    |     |
| ---------- | --------- | --------------- | --------------- | -------- | ----------------- | ----------- | ---------- | --- | ---------- | ------------ | -------- | ---- | ------------- | --- |
| enriched   | with      | their findings, | the             | authors  | claim             | that system |            |     |            |              |          |      |               |     |
|            |           |                 |                 |          |                   |             | rules;     | few | approaches | model        | retries  | as   | probabilistic |     |
| architects | can model | ZT              | transformations |          | of Cyber-Physical |             |            |     |            |              |          |      |               |     |
|            |           |                 |                 |          |                   |             | amplifiers |     | of attack  | likelihood   | with     | time | decay         | and |
| systems.   | The       | authors         | in [37]         | proposed | a process-driven  |             |            |     |            |              |          |      |               |     |
contextualconsistencychecks.
| framework | for | migrating | to a | ZT architecture, |     | aimed at |     |     |     |     |     |     |     |     |
| --------- | --- | --------- | ---- | ---------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
6) Insufficientadversary-awarethreatsurfaces.
addressingthegapsandchallengesidentifiedinpreviousZT Compositeattacksurfacesthatcombineauthentication,
| migrations. | A similar | study | on  | the cost-effectiveness |     | of ZT |     |     |     |     |     |     |     |     |
| ----------- | --------- | ----- | --- | ---------------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
attributeforgery,tokenreplay,andpost-granthijackare
| transformation |     | for organizational |     | security | was published | by  |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------------ | --- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rarelymodeledtogether;asaresult,policythresholds
| Adahman | et al. | [38]. Similar | studies | on  | ZT transformation |     |     |     |     |     |     |     |     |     |
| ------- | ------ | ------------- | ------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arehardtojustifyquantitatively.
| of industry | sectors | have | been published |     | in [39], | [40], [41], |          |                |         |     |            |          |     |      |
| ----------- | ------- | ---- | -------------- | --- | -------- | ----------- | -------- | -------------- | ------- | --- | ---------- | -------- | --- | ---- |
|             |         |      |                |     |          |             | Based on | the literature | review, | the | identified | research |     | gaps |
and[42].
|     |     |     |     |     |     |     | highlight | the need | to develop | an  | AA system | that | covers | the |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ---------- | --- | --------- | ---- | ------ | --- |
Haleetal.[43]presentedaZT-basedmitigationapproach
for ML components originating from data or model manip- followingfactors.
ulation. In addition, Krishnan and Sreeja [44] proposed a 1) Discardsimplicittrust.
zero-trust-based adaptive authentication system that uses 2) Models trust as a continuous, evolving, and bounded
variable
| composite | attribute | sets. | Ahmed | et al. | in their | work [45] |     |     |     |     |     |     |     |     |
| --------- | --------- | ----- | ----- | ------ | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
presentedaZT-basedaccesscontrolsystemtoguardsensitive 3) Multi-dimensionalcontextualsignalsforriskaggrega-
data stores. The authors utilized an access-control proxy to tionandpolicy-driventhresholds-basedevaluation.
analyze request parameters and arrive at the enforcement 4) Enables parameterization and online recalibration of
decisions.AZT-basedimplementationofsecuritymeasures attribute and authentication weighting and penalty
coefficients.
| for Oracle | ERP | cloud | was studied | by the | authors | in Qazi |     |     |     |     |     |     |     |     |
| ---------- | --- | ----- | ----------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
and Arshad [46]. In contrast, a framework to protect power 5) Resistsprofilepoisoning.
grids from security attacks using a Zero-Trust strategy was 6) Distinguishesbetweenhardviolationsandprobabilistic
softviolations.
| discussed | by Faraj | [47]. | Similar | zero-trust | frameworks | for |     |     |     |     |     |     |     |     |
| --------- | -------- | ----- | ------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
protectingresourceshavebeenfeaturedintheliterature[48], 7) Incorporatesretryattackdynamicsintothreatmodels.
8) Alignedtoindustrystandards.
[49].
TheproposedZeTHAAsystemisanextensionofthework
|     |     |     |     |     |     |     | of Krishnan | and | Sreeja [44] | to mitigate |     | identified | research |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ----------- | --- | ---------- | -------- | --- |
D. RESEARCHGAPANALYSIS
gapswithanimplementedproof-of-concept.
Basedontheinferencederivedfromtheliteraturereview,the
followingresearchgapshavebeenidentified,whichneedto
V. METHODOLOGY
beaddressed:
|     |     |     |     |     |     |     | This section | presents |     | the methodology |     | underlying |     | the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | --------------- | --- | ---------- | --- | --- |
1) Vendor-locked,opaqueimplementation: proposed Zero-Trust Hybrid Adaptive Authentication
Existing Zero-Trust implementations are proprietary, (ZeTHAA) framework. The methodology proceeds from
resultinginvendorlock-in,anddonotofferaviewof system definition and state modeling to threat analysis,
internalworkingandcalibrations[50],[51],[52],[53]. risk computation, adaptive enforcement, and security
| 2) Staticattributeweightingandpenaltypolicies: |     |     |     |     |     |     | guarantees. |     |     |     |     |     |     |       |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ----- |
| VOLUME14,2026                                  |     |     |     |     |     |     |             |     |     |     |     |     |     | 77843 |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| A. NOTATION |     |     |     |     |     |     | 1) SYSTEMANDTRUSTMODELASSUMPTIONS |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
Table1summarizesthesymbolsandnotationsusedthrough- • Continuous Evaluation. Trust is evaluated at every
outthisstudy. request and is not persistent across sessions. Each
requestistreatedasafreshevaluationunderZeroTrust
| B. SYSTEMMODEL |          |          |              |     |           |     | semantics.                                       |     |     |     |     |     |     |
| -------------- | -------- | -------- | ------------ | --- | --------- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|                |          |          |              |     |           | =   | • CompositeTrustFunction.Trustisaunifiedfunction |     |     |     |     |     |     |
| The system     | consists | of a set | of protected |     | resources | R   |                                                  |     |     |     |     |     |     |
{R ,R ,...,R }. Each resource R is associated with a of authentication strength, contextual attributes, and
| 1 2 | n   |     |     | i   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
requiredtrustthresholdT(R),whichmustbeachievedbefore behavioral history. No independent trust components
i
(e.g.,authentication-onlyorbehavior-onlytrust)existin
| access is | granted. A set | of registered |     | users | U interacts | with |     |     |     |     |     |     |     |
| --------- | -------------- | ------------- | --- | ----- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
thesystembyperformingactionsAct = {login,read,write} isolation.
ontheresourcesinR. • Separation of Trust and Risk. Trust and risk are
AccessdecisionsaredeterminedunderaZeroTrustmodel, complementary but distinct quantities. Trust represents
inwhichnouser,device,orsessionisimplicitlytrusted.Each confidence in legitimacy, whereas risk represents the
|     |     |     |     |     |     |     | likelihood | of  | adversarial | success. |     | The decisions | are |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | -------- | --- | ------------- | --- |
accessrequestisevaluatedbasedon:
|         |                 |                |            |            |     | =       | basedonbothquantities.            |     |     |     |     |     |     |
| ------- | --------------- | -------------- | ---------- | ---------- | --- | ------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
| • A set | of contextual   | and            | behavioral | attributes |     | A t     |                                   |     |     |     |     |     |     |
| {a      | (t),a (t),...}; |                |            |            |     |         |                                   |     |     |     |     |     |     |
| 1       | 2               |                |            |            |     |         |                                   |     |     |     |     |     |     |
| A set   | of supported    | authentication |            | methods    |     | M, each |                                   |     |     |     |     |     |     |
| •       |                 |                |            |            |     |         | 2) ATTRIBUTEANDCONTEXTASSUMPTIONS |     |     |     |     |     |     |
associatedwithanintrinsicauthenticationstrength; • AttributeObservability.Contextualattributes(device,
• A dynamically evaluated session context C(t), com- location, time, network, etc.) are observable with
prising attributes, authentication state, and historical boundednoiseandmayexhibitnaturalvariability.
evidence; • SpoofabilityandStability.Eachattributeisassociated
AtrustscoreTrust(C(t))andanestimatedattacksuccess
| •   |     |     |     |     |     |     | with | a spoofability | likelihood |     | and | temporal | stability, |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------------- | ---------- | --- | --- | -------- | ---------- |
probabilityPr[AttackSuccess|C(t)].
|     |     |     |     |     |     |     | which | influences | its | weight | and | penalty | in trust |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ------ | --- | ------- | -------- |
computation.
| Authorization | decisions            |     | are issued   | per | session | and per |     |     |     |     |     |     |     |
| ------------- | -------------------- | --- | ------------ | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
| resource,     | and are continuously |     | re-evaluated |     | as the  | context |     |     |     |     |     |     |     |
evolves.
|     |     |     |     |     |     |     | 3) BEHAVIORALANDLEARNINGASSUMPTIONS |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
TheZeTHAAframeworkdefinestheZero-TrustAdaptive
|     |     |     |     |     |     |     | • Behavioral | Profiles |     | are Probabilistic. |     | User | behavior |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------------ | --- | ---- | -------- |
Authenticationsystemasthetuple:
|     |     |     |     |     |     |     | is modeled | as  | a probabilistic |     | distribution | derived | from |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------------- | --- | ------------ | ------- | ---- |
historicalobservationsratherthandeterministicrules.
=(U,A,M,C,R,T)
Z
• TemporalDrift.Legitimateuserbehaviorevolvesover
|     |     |     |     |     |     |     | time, | and the | system | accommodates |     | this | evolution |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------ | ------------ | --- | ---- | --------- |
where:
throughboundedlearningratesandwindowedupdates.
• U denotesthesetofusers,
| • A = | {a ,a ,...,a | }denotesthesetofcontextualand |     |     |     |     |                                       |     |     |     |     |     |     |
| ----- | ------------ | ----------------------------- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
|       | 1 2          | n                             |     |     |     |     |                                       |     |     |     |     |     |     |
|       |              |                               |     |     |     |     | 4) ADVERSARYANDTHREATMODELASSUMPTIONS |     |     |     |     |     |     |
behavioralattributes,
• M = {m ,m ,...,m } denotes the set of supported • Polynomial-time, probabilistic Adversary Model.
|     | 1 2 |     | k   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
authenticationmethods, The adversary’s success is modeled probabilistically
• C denotessessioncontext, through authentication breakability, attribute forgery,
• R∈{0,1}denotestheobservedsecurityoutcome, andpost-authenticationattackvectors.
∈Rdenotesthetrustscore. Retry Behavior as Attack Signal. Repeated authenti-
| • T |     |     |     |     |     |     | •      |          |             |     |               |            |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----------- | --- | ------------- | ---------- | --- |
|     |     |     |     |     |     |     | cation | failures | are treated | as  | probabilistic | indicators | of  |
ThetupleZdefinesthesystem’sstaticstructure.Dynamic
|          |             |               |     |          |     |         | adversarial | activity | and | contribute | to  | risk through | retry |
| -------- | ----------- | ------------- | --- | -------- | --- | ------- | ----------- | -------- | --- | ---------- | --- | ------------ | ----- |
| behavior | is captured | by explicitly |     | modeling | the | session |             |          |     |            |     |              |       |
contextC(t),thetrustscoreT(t),andtheobservedoutcomes amplificationfunctions.
|     |     |     |     |     |     |     | • Hard | vs Soft | Violations. |     | Hard violations |     | represent |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ----------- | --- | --------------- | --- | --------- |
R(t)astime-dependentvariables.
|                |              |     |        |          |        |     | non-compensable |     | failures | (e.g., | cryptographic |     | failure, |
| -------------- | ------------ | --- | ------ | -------- | ------ | --- | --------------- | --- | -------- | ------ | ------------- | --- | -------- |
| The high-level | architecture |     | of the | proposed | system | is  |                 |     |          |        |               |     |          |
impossibletravel),whilesoftviolationsrepresentprob-
presentedinFig.1:
abilisticdeviationsthatreducetrustbutdonotterminate
thesession.
C. ASSUMPTIONSANDDESIGNSCOPE
| The proposed | framework    |             | is built | on a | set of | system,  |                           |     |     |     |     |     |     |
| ------------ | ------------ | ----------- | -------- | ---- | ------ | -------- | ------------------------- | --- | --- | --- | --- | --- | --- |
| threat,      | and modeling | assumptions |          | that | enable | the for- |                           |     |     |     |     |     |     |
|              |              |             |          |      |        |          | 5) OPERATIONALASSUMPTIONS |     |     |     |     |     |     |
malization of trust, risk, and attack probability. These • Availability of Logging and Telemetry. Sufficient
assumptions are aligned with Zero Trust principles and logging and telemetry are available to estimate
standardidentityframeworkssuchasNISTSP800-207and attribute distributions, behavioral profiles, and attack
| SP800-63B. |     |     |     |     |     |     | probabilities. |     |     |     |     |               |     |
| ---------- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | ------------- | --- |
| 77844      |     |     |     |     |     |     |                |     |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE1. Summaryofnotations.
• Policy-Driven Thresholds. Thresholds for authentica- enclaves,orplatform attestationservices.Thesemech-
tion,authorization,andescalationaredefinedbysystem anisms provide evidence of the device state (e.g., non-
policyandmayvaryaccordingtoresourcesensitivity. rooted,verifiedboot,emulator).
|     |     |     |     |     | • Cryptographic | Capability:           | The | device | can securely  |
| --- | --- | --- | --- | --- | --------------- | --------------------- | --- | ------ | ------------- |
|     |     |     |     |     | generate        | and use cryptographic |     | keys   | for authenti- |
6) DEVICECAPABILITIES
Every request is assumed to originate from a client device cation, including signing challenges and participat-
capableof: ing in hardware-backed authentication protocols (e.g.,
|            |                      |     |            |          | FIDO2 | and, Trusted | Platform | Module | (TPM)-based |
| ---------- | -------------------- | --- | ---------- | -------- | ----- | ------------ | -------- | ------ | ----------- |
| Contextual | Signal Provisioning: |     | The device | can pro- |       |              |          |        |             |
•
attestation).
| vide contextual | attributes | such             | as location | (coarse or  |            |                |                   |     |               |
| --------------- | ---------- | ---------------- | ----------- | ----------- | ---------- | -------------- | ----------------- | --- | ------------- |
|                 |            |                  |             |             | • Secure   | Communication: | All communication |     | between       |
| fine-grained),  | device     | characteristics, | and         | application |            |                |                   |     |               |
|                 |            |                  |             |             | the device | and verifier   | is assumed        |     | to occur over |
metadata.Theseattributesmaybederivedfromsystem
securechannels(e.g.,TLS),ensuringconfidentialityand
| application | programming | interfaces | (APIs), | network |     |     |     |     |     |
| ----------- | ----------- | ---------- | ------- | ------- | --- | --- | --- | --- | --- |
integrityoftransmitteddata.
observations,ortrustedexecutionenvironments.
• Device Integrity and Attestation: The device sup- 7) SCOPEOFAPPLICABILITY
ports mechanisms to assert platform integrity, such Inenvironmentswheresuchdevicecapabilitiesareunavail-
as Trusted Execution Environments (TEE), secure able (e.g., legacy systems without attestation support), the
| VOLUME14,2026 |     |     |     |     |     |     |     |     | 77845 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
FIGURE1. ZeTHAAsystemarchitecture.
framework degrades gracefully by assigning lower weights E. SECURITYOBJECTIVE
tountrustedattributesandrelyingmoreheavilyonbehavioral The primary security objective of the proposed system is to
andcontextualrisksignals. ensure that access to any protected resource is granted and
maintainedonlywhentheprobabilityofadversarialsuccess
D. TRUSTANDRISK inthecurrentcontextremainsbelowanacceptablethreshold.
The trust state T(t) ∈ [0,1] represents an accumulated ForanysessioncontextC(t)atanygiventimet,thesystem
confidence.Thetrustevolvesovertimeastheusercontinues enforces:
tointeractwiththesystem.ThetrustT(t)isthusafunction
ofthecurrentandhistoricalcontext,modeledas: ∀t,∀k ∈K, Pr(R k (t)=1|C(t)≤δ k
T(t)=f(C(t),T(t − ), R (t)∈{0,1}∀k ∈K
k
where T(t−) is the historical trust. Trust T(t) at any time is where R k (t) = 1 indicates a successful attack of class k at
a composite of contextual conformance, behavioral history, timet.R k (t) = 0otherwise.δ representsaconfigurablerisk
devicepostures,andrisksignals. tolerance.
R(t) ∈ 0,1 represents the security outcome at time t. Thesystemadaptsauthenticationstrengthsandauthoriza-
R(t) = Pr[AttackSuccess | C(t)] = 1 represents the risk tiondecisionstoevolvingrisk,therebyenforcingcontinuous
ofadversarialaccess. riskevaluation,consistentwithZero-Trustprinciples.
77846 VOLUME14,2026

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| F. ATTRIBUTES |     |     |     |     |     | I. SESSIONCONTEXTMODEL |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
ThesystemdefinesasetofattributesA.Anattributea i isa The session context captures the environmental and situa-
measurable contextual or behavioral property derived from tionalconditionsunderwhichaccessrequestsareevaluated.
the user, the device, or the application that facilitates the Itisdefinedasatime-dependenttuple:
| construction          | of an overall | risk profile |     | and the | computation |     |         |     |       |          |     |     |
| --------------------- | ------------- | ------------ | --- | ------- | ----------- | --- | ------- | --- | ----- | -------- | --- | --- |
|                       |               |              |     |         |             |     | C(t)=(R |     | ,D ,N | ,T (t),L | ),  |     |
| oftheriskprobability. |               |              |     |         |             |     |         |     | s p s | c        | c   |     |
∈
| Eachuserrequesttransmitsacollectionofattributesa |     |     |     |     | i   | where: |     |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Atothesystem.ThesetofattributesAanditsweightW(A)
• R s denotesresourcesensitivity,
canbedefinedas:
• D denotesdeviceposture,
p
|     |      |        | )<T | )}, |     |       |                      |     |     |     |     |     |
| --- | ---- | ------ | --- | --- | --- | ----- | -------------------- | --- | --- | --- | --- | --- |
|     | A={a | ∈A|w(a |     | (R  |     | • N s | denotesnetworkstate, |     |     |     |     |     |
|     | i    |        | i   | r i |     |       |                      |     |     |     |     |     |
• T (t)denotestemporalcontext,
| wheretheweightassignedtoanyattributeislessthanthetrust |     |     |     |     |     | c   |     |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• L denoteslocationcontext.
c
| requiredtoaccessanyresourceR. |     |     | i   |     |     |             |         |         |      |      |              |        |
| ----------------------------- | --- | --- | --- | --- | --- | ----------- | ------- | ------- | ---- | ---- | ------------ | ------ |
|                               |     |     |     |     |     | The session | context | evolves | over | time | and directly | influ- |
ThesetofattributesAisextensible,andnewattributescan
|     |     |     |     |     |     | ences risk | estimation, | trust | computation, |     | and authorization |     |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----- | ------------ | --- | ----------------- | --- |
beaddedasdiscovered.
|     |     |     |     |     |     | decisions. | Given the | dynamic | nature | of the | session | context, |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | ------- | ------ | ------ | ------- | -------- |
authorizationmustbecontinuouslyevaluatedandnottreated
G. AUTHENTICATIONMODALITIES
asaone-timedecision.
| The system | is configured | with          | a set | of authentication |       |     |     |     |     |     |     |     |
| ---------- | ------------- | ------------- | ----- | ----------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| modalities | M with a      | corresponding | set   | of weights        | W(M). |     |     |     |     |     |     |     |
ThesetofauthenticationmodalitiesMisdefinedasfollows: J. ATTRIBUTETAXONOMYANDCLASSIFICATION
|     |     |     |     |     |     | An attribute | a is | a behavioral |     | or contextual |     | property |
| --- | --- | --- | --- | --- | --- | ------------ | ---- | ------------ | --- | ------------- | --- | -------- |
i
M={m∈M|w(m)<T ( )} associatedwithauser,device,session,orrequest.Attributes
r i
wherew(m)istheweightassignedtoaselectedauthentication provide contextual signals that are relevant to dynamic risk
|          |        |            |          |     |            | and trust | computation | in  | Zero Trust | systems. | This | section |
| -------- | ------ | ---------- | -------- | --- | ---------- | --------- | ----------- | --- | ---------- | -------- | ---- | ------- |
| modality | m ∈ M. | The weight | obtained | by  | successful |           |             |     |            |          |      |         |
authenticationwithanyparticipatingmodalitywillalwaysbe introducesanattributetaxonomyandclassificationbasedon
theirproperties.
| lessthanthetrustrequiredtoaccesstheresource,T |                 |     |     |             | r (R). i |                          |     |     |     |     |     |     |
| --------------------------------------------- | --------------- | --- | --- | ----------- | -------- | ------------------------ | --- | --- | --- | --- | --- | --- |
| The set                                       | M is extensible | and | can | accommodate | newer    |                          |     |     |     |     |     |     |
| authenticationmodalities.                     |                 |     |     |             |          | 1) COMPOSITEATTRIBUTESET |     |     |     |     |     |     |
TheproposedZeTHAAframeworkclassifiesattributesunder
Withthissystemmodelestablished,wedefineuseridentity
usingauthenticationsessions. threecategories,i.e.,-‘‘User,’’‘‘Application,’’and‘‘Device,’’
basedontheparticipatingentities.Theattributesandentities
H. AUTHENTICATIONSESSIONMODEL are discrete yet related. This establishes a ‘‘who uses what,
TheauthenticationAuth isrepresentedas: where’’ relationship among the three discrete entities (user,
i
|     |     |     |     |     |     | device, | browser/application), |     | and | this relationship |     | model |
| --- | --- | --- | --- | --- | --- | ------- | --------------------- | --- | --- | ----------------- | --- | ----- |
Auth(U,m,C)→{True,False}
i i i allows attribute variances to be flagged across categories.
where U represents the user requesting verification of Theapplicationattributesprovideawaytouniquelyidentify
i
identity, m i denotes the authentication method applied, and ‘‘theapplication,runningondevice’’combination.Thus,the
context C = C ∪ C denotes the context attribute-driven context becomes a composite construct of
|     | contextual | behavioral |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
‘‘user,usingtheapplication,ondevice’’.Theattributesused
originatingfrombehavioralandcontextualsignals.
An authentication session is a construct established upon intheCompositeAttributesetarelistedinTable2.
successfulauthentication,definedas: Formobiledevices,thedeviceattributesetisobtainedvia
|     |         |     |        |     |     | Application | Programming |     | Interfaces(APIs) |     | provided | by the |
| --- | ------- | --- | ------ | --- | --- | ----------- | ----------- | --- | ---------------- | --- | -------- | ------ |
|     | =(U,m,t |     | ,t ,σ) |     |     |             |             |     |                  |     |          |        |
S
|     |     | i   | 0 e |     |     | nativemobileoperatingsystem. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
where:
| • U ∈U | istheauthenticateduser, |     |     |     |     | 2) ATTRIBUTECLASSIFICATION |     |     |     |     |     |     |
| ------ | ----------------------- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
i
m∈M istheauthenticationmethodused, Attributes are classified based on their type, stability, and
•
• t 0 istheauthenticationstarttime, applicabilitytocontextbinding.
| • t istheexpirationtime, |     |     |     |     |     | 1) ContextualVsBehavioral |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
e
| σ ∈ | {active,expired,revoked} |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• denotes the authentica- Attributesthatdescribetheexecutionenvironmentare
tionstate. classified as contextual, and those that describe user
An authentication session only establishes the identity interactionovertimeareconsideredbehavioral.Table3
of a user at a given point in time. This does not imply classifiestheattributesascontextualorbehavioral.
continuedauthorization.Whileauthenticationsessionsverify 2) Stability
andestablishuseridentity,authorizationdecisionsdependon Attributescanbeclassifiedasstaticordynamicbased
additional environmental and situational factors, which are on their tendency to change over time, which affects
modeledasasessioncontext. theircontributiontothepersistenceortrustdecayand
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     | 77847 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE2. Compositeattributeset.
TABLE3. Contextualvsbehavioralattributeclassification. frombenignhistoricalobservations.Aprofilerepresentsthe
|     |     |     |     |     | expected distribution | or pattern  | of attribute | values    | and may    |
| --- | --- | --- | --- | --- | --------------------- | ----------- | ------------ | --------- | ---------- |
|     |     |     |     |     | include summary       | statistics, | temporal     | patterns, | or learned |
probabilisticbehavior.
|     |     |     |     |     | For an attribute | a, the profile | Pi  | captures | its expected |
| --- | --- | --- | --- | --- | ---------------- | -------------- | --- | -------- | ------------ |
|     |     |     |     |     |                  | i              |     | u        |              |
behavior,modeledas:
Pi ={E[a],Var[a],...},
|     |     |     |     |     |     | u i | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereE[a]representsthemeanvalueandVar[a]denotesthe
|     |     |     |     |     | i   |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
observedvarianceoftheattributea.Profilesareupdatedcon-
i
servativelytoaccommodatebenigndriftwhileavoidingrapid
adaptationresultingfrompotentiallyadversarialbehavior.
theirsuitabilityforcontinuousvalidation.Forinstance, 2) DEVIATIONANDANOMALYSCORING
application and device attributes are predominantly Behavioral patterns can change, subject to human behavior
staticanddonotchangeduringtheirinteractionswith or associated changes. If a user with an established pattern
thesystem.Table4classifiesattributesbasedontheir of logging in at 10 A.M. daily logs in at 9 A.M., the
dispositiontochange. system records this as a deviation from the established
Predominantly static attributes contribute to longer-lived pattern. However, this does not conclusively establish risk
|     |     |     |     |     | or adversarial | behavior. While | the | deviation | indicates an |
| --- | --- | --- | --- | --- | -------------- | --------------- | --- | --------- | ------------ |
trust,whiledynamicattributesarecontinuouslyevaluatedand
utilizedtodetectanomalies. elevatedrisk,itcouldbeanisolatedincidentofauserlogging
inatadifferenttime.Thesystemrecords,flags,andvalidates
deviationsagainsttolerancelimitssetperpolicy.
K. DYNAMICATTRIBUTEANALYSISANDBEHAVIORAL
PROFILING At time t, the observed attribute value a(t) i is compared
|                       |                |            |               |         | againstthecorrespondingprofilePi |                   |                         | tocomputeadeviation |     |
| --------------------- | -------------- | ---------- | ------------- | ------- | -------------------------------- | ----------------- | ----------------------- | ------------------- | --- |
| Contextual            | and behavioral | attributes | change owing  | to user |                                  |                   | u                       |                     |     |
| behavior, operational | changes,       | and        | modifications | to the  | score:                           |                   |                         |                     |     |
|                       |                |            |               |         |                                  | (cid:49)a(t)=dist | (cid:0) a(t),Pi(cid:1), |                     |     |
access device. For example, a login location or access time i i u
may be benign for one user while anomalous for another. where(cid:49)a representsthedeviationoftheobservedvalueof
i
| As such, static | interpretation | of  | attributes is not | sufficient |     |     |     |     |     |
| --------------- | -------------- | --- | ----------------- | ---------- | --- | --- | --- | --- | --- |
theattributefromtheestablishedmeanvalue.
in Zero Trust environments. In ZT systems, trust must be Observed deviations are evaluated relative to acceptable
| continuouslyevaluated,updated,orrecalibrated. |     |     |     |     |                    |           |             | θ   |              |
| --------------------------------------------- | --- | --- | --- | --- | ------------------ | --------- | ----------- | --- | ------------ |
|                                               |     |     |     |     | attribute-specific | variation | thresholds. | Let | i denote the |
This section introduces a dynamic analysis of observed permissible deviation for attribute a. Deviations within
i
attributes, how they contribute to user-specific profiles, and this tolerance are treated as benign, while excess deviation
providessignalsandevidencefortrust,risk,andauthorization
contributestoanomalyscoringandpenaltyassignment.
| decisions. |     |     |     |     |     |                     | (cid:0) (cid:49)a(t)−θ(cid:1) |     |     |
| ---------- | --- | --- | --- | --- | --- | ------------------- | ----------------------------- | --- | --- |
|            |     |     |     |     |     | (cid:49)a + (t)=max | 0,                            |     |     |
|            |     |     |     |     |     | i                   |                               | i i |     |
1) BEHAVIORALANDCONTEXTUALPROFILES The deviation score quantifies how unusual the current
For each user u (or device, where applicable), the system observation is relative to established behavior, but does not
maintainsabehavioralandcontextualprofileP u ,constructed directlyresultinaclassificationdecision.
| 77848 |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE4. Temporaldispositionofattributes.
3) MAPPINGDEVIATIONSTOATTRIBUTEPENALTIES described in subsequent sections. Attribute penalties influ-
|     |     |     |     |     |     |     |     | ence trust | decay, | contribute | to  | attack | success | probability |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ---------- | --- | ------ | ------- | ----------- | --- |
Deviationscoresaremappedtoattributepenaltiesthatreflect
increased suspicion or reduced confidence in the observed estimation, and trigger adaptive enforcement actions during
evidence.Forattributea,thepenaltyattimet isafunction continuousmonitoring.
i
ofthedeviationobserved: Thus, dynamic attribute analysis provides the foundation
forthreatmodeling,authorizationdecisions,andZeroTrust
|            |      | π              |         | (cid:0)(cid:49)a (cid:1), |      |          |      |             |     |     |     |     |     |     |     |
| ---------- | ---- | -------------- | ------- | ------------------------- | ---- | -------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|            |      |                | i (t)=g | i (t)                     |      |          |      | guarantees. |     |     |     |     |     |     |     |
| where g(·) | is a | policy-defined |         | function                  | that | controls | sen- |             |     |     |     |     |     |     |     |
sitivity to deviations. Larger deviations result in higher L. BEHAVIORALPROFILECONSTRUCTIONAND
EVOLUTION
| penalties,         | which | in turn       | reduce | trust and | increase  | estimated |     |              |            |     |                  |     |     |           |     |
| ------------------ | ----- | ------------- | ------ | --------- | --------- | --------- | --- | ------------ | ---------- | --- | ---------------- | --- | --- | --------- | --- |
|                    |       |               |        |           |           |           |     | This section | formalizes |     | the construction |     | and | evolution | of  |
| risk in subsequent |       | computations. |        | The       | penalties | represent |     |              |            |     |                  |     |     |           |     |
the system’s assessment of elevated risk based on observed behavioral profiles introduced earlier. Behavioral profiles
|     |     |     |     |     |     |     |     | capture long-term |     | patterns | of user | behavior |     | and serve | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ------- | -------- | --- | --------- | --- |
behavior;theydonotimplythatanattackhasoccurred.
Thedeviation-derivedpenaltiesintroducedinthissection the reference against which deviations are evaluated for
|               |               |              |          |            |           |              |     | penalty assignment |     | and          | trust computation. |            | The        | framework |       |
| ------------- | ------------- | ------------ | -------- | ---------- | --------- | ------------ | --- | ------------------ | --- | ------------ | ------------------ | ---------- | ---------- | --------- | ----- |
| represent     | instantaneous |              | evidence | of         | anomalous | behavior.    |     |                    |     |              |                    |            |            |           |       |
|               |               |              |          |            |           |              |     | design balances    |     | adaptability | to                 | legitimate | behavioral |           | drift |
| These signals | are           | subsequently |          | aggregated | and       | recalibrated |     |                    |     |              |                    |            |            |           |       |
over time by the penalty assignment model described withresistancetoprofilepoisoning.
| later, which                      | accounts |     | for historical | observations, |     | resource |     |                                                      |     |     |     |     |     |     |     |
| --------------------------------- | -------- | --- | -------------- | ------------- | --- | -------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| sensitivity,andpolicyconstraints. |          |     |                |               |     |          |     | 1) PROFILEINITIALIZATION                             |     |     |     |     |     |     |     |
|                                   |          |     |                |               |     |          |     | Foreachuseruandbehavioralattributea,aninitialprofile |     |     |     |     | i   |     |     |
4) ROLEOFMACHINELEARNING P i(t ) is established at the first trusted observation. The
|         |          |             |     |         |                   |     |     | u 0               |     |         |            |       |     |           |     |
| ------- | -------- | ----------- | --- | ------- | ----------------- | --- | --- | ----------------- | --- | ------- | ---------- | ----- | --- | --------- | --- |
|         |          |             |     |         |                   |     |     | profile maintains |     | summary | statistics | (mean | and | variance) |     |
| Machine | learning | is employed |     | in this | layer exclusively |     | for |                   |     |         |            |       |     |           |     |
evidence interpretation. Machine learning is strictly limited representingnormalbehavior.
to learning and updating behavioral profiles and computing This initialization phase provides a stable baseline from
|     |     |     |     |     |     |     |     | which learning |     | can proceed |     | cautiously | as  | observations |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | --- | ---------- | --- | ------------ | --- |
deviationscores.Itdoesnotdirectlydetermineauthentication
orauthorizationoutcomes,ormodifyauthenticationstrength accumulate. Algorithm 1 details the initialization of the
behavioralprofile.
| or policy | thresholds. | Instead, |     | ML-derived | outputs | serve | as  |     |     |     |     |     |     |     |     |
| --------- | ----------- | -------- | --- | ---------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inputstotrust,risk,andauthorizationdecisions.
| This separation |     | enables | the | system | to adapt | to evolving |     |                                    |     |     |     |     |     |     |     |
| --------------- | --- | ------- | --- | ------ | -------- | ----------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                 |     |         |     |        |          |             |     | 2) HARDANDSOFTCONTEXTUALVIOLATIONS |     |     |     |     |     |     |     |
userbehaviorandenvironmentalconditions. Observed deviations from behavioral profiles are classified
|     |     |     |     |     |     |     |     | aseitherhard | orsoft | violations. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------- | --- | --- | --- | --- | --- |
5) INTEGRATIONWITHDOWNSTREAMCOMPONENTS Hard violations correspond to physically or logically
The penalties derived through dynamic attribute analysis impossiblestates(e.g.,infeasiblegeo-velocity,cryptographic
are incorporated into the composite trust and risk models binding failures, token replay, hardware attestation failure,
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 77849 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm1BehavioralProfileInitialization as:
Require: Attributea,initialobservationa(t )
Require: Defaultvar
i
ianceσ2,learningrate
i
γ
0 Learn(t)=Trust(t)≥τ
learn
0
Ensure: InitializedbehavioralprofileP u i ∧ (cid:53) i (t)≤ϵ ∧ S(m)≥S learn
1: Initializemean:µ i ←a i (t 0 ) ∧ ¬HardViolation(t) (1)
2:
Initializevariance:σ2 ←σ2
3 4 : : S In e i t ti p a r l o iz fi e le pe P n u i al ← tya { c µ c i i u , m σ i u 2 l } at 0 or(cid:53) i ←0 w th h e er c e um τ le u a l r a n ti i v s e a p m en in a i l m tie u s m at tru ti s m t e thr t e , sh ϵ ol i d s , a (cid:53) i s ( m t) a r ll ep p re e s n e a n lt t y s
tolerance, S(m) is the current authentication strength, S
learn
isaminimumauthenticationassurancerequiredforlearning,
and no hard violations have been observed. In addition,
application signature mismatch). Such violations indicate
astatevariableLearningEnabled(t)governswhetherprofile
sessioncompromisewithhighconfidenceandresultinimme-
updates are allowed, transitioning to false upon anomalous
diate access denial or session termination. Hard violations
events, and returning to true only when sufficient trust has
permanently disable learning for the affected session. Let
been built, and soft violations remain within acceptable
HV(t) ∈ {0,1}denotethehardviolationpredicateattimet,
bounds.Thebehavioralprofileupdateproceedsonlyif:
whereHV(t)=1indicatesthatatleastonehardviolationhas
occurredwithinthecurrentauthenticationoraccesssession. UpdateAllowed(t)=Learn(t)∧LearningEnabled(t)
Onceahardviolationoccurs,trust-andrisk-basedreasoning
When Learn(t) = 1, the profile is updated using an
isnolongervalid,andthesessionmustbeterminatedorre-
exponentiallyweightedmovingaverage(EWMA):
authenticated.Thehardviolationcheckisusedbythesystem
asaprimarydefensivevalidationforeachrequest,enablingit Pi(t +1)=(1−γ)Pi(t)+γ a(t), γ ∈(0,1), γ ≪1.
u u i
torejectanyrequestthatviolatestheconditionimmediately.
(2)
Soft violations correspond to statistically unlikely but
plausiblebehavioraldeviations(e.g.,unusuallogintime,new IfLearn(t)=0,thenPi(t +1)=Pi(t).
u u
location). These violations incur penalties that reduce trust This separation ensures immediate reaction to suspicious
butdonotimmediatelyinvalidatethesession.Softviolations behavior while allowing learning to resume only after
temporarilysuspendlearninguntiltrustisre-established. sustainedtrustisre-established.
Table 5 classifies contextual signals into hard and soft
violations with the corresponding action executed by the 4) LEARNINGSUSPENSIONANDRE-ENABLEMENT
system. To prevent adversarial manipulation, learning is suspended
GlobalAdmissibilityPredicate whenever anomalous behavior is observed and the state
Thesystemdefinesaglobaladmissibilitypredicate: variableLearningEnabled(t)transitionstofalse.
However, suspending learning indefinitely would prevent
Admissible(t) ⇐⇒ (HV(t)=0 (cid:1)
adaptationtolegitimatebehavioralshifts.Therefore,learning
is re-enabled only after sustained evidence of legitimacy is
The admissibility predicate represents a system-wide
observedoveratemporalwindowW:
safety invariant. All authentication, authorization, token
issuance, and resource access events are defined only over 1 X
ReLearn(t)= Trust(s)≥τ
an admissible system state. If Admissible(t) = 0, all |W| learn
s∈W
subsequent requests are denied irrespective of accumulated X
∧ Indicator.((cid:53)(s)>0)≤k, (3)
trust,authenticationstrength,orcontextualevidence. i
This separation ensures that trust computation operates s∈W
strictly within safe execution states, while hard violations wheresisatimeindexandk istheupperlimitofthenumber
triggerimmediateanddeterministicsecurityresponses.This of soft violation events permitted within the relearning
distinctionallowsthesystemtoreactdecisivelytoimpossible windowW,andIndicator(.)isanindicatorfunction.
states while remaining tolerant of legitimate behavioral WhenReLearn(t) = true,LearningEnabled transitionsto
variation. true.
3) BEHAVIORALLEARNINGPOLICY 5) BEHAVIORALLEARNINGSTRATEGIES
Behavioralprofilesareupdatedinanevent-drivenandtrust- Once initialized, behavioral profiles evolve through con-
based manner. Profile updates occur only when no hard trolled learning. Different attributes exhibit varying obser-
violations are observed, the current trust level exceeds a vation frequencies and noise characteristics; therefore,
learningthreshold,authenticationstrengthissatisfactory,and a single learning mechanism is insufficient. Accordingly,
no significant penalties are present. This approach ensures each attribute a is assigned a learning strategy χ ∈
i i
that anomalous behavior does not contribute to profile {online,windowed} based on its volatility, observation fre-
learning and adaptation. The learning condition is modeled quency,andsecuritysensitivity.
77850 VOLUME14,2026

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE5. Hardviolationsvssoftcontextualsignals.
The system responds faster to behavioral attributes with Algorithm2Trust-GatedOnlineBehavioralProfileUpdate
naturaldrift,toensurefasteradaptationandpreventstep-up Require: Currentobservationa i (t)
authenticationineveryrequest.Stableandsecurity-sensitive Require: CurrentprofileP u i(t)={µ i (t),σ i 2(t)}
attributespresentaveryslowrateofchange.Suddenchanges Require: TrustTrust(t),penalty(cid:53) i (t)
totheseattributescouldsignifyanattemptatrepeatedattacks Require: Thresholdsτ learn ,ϵ
orprofilepoisoningbyadversarialelements.Assuch,stable Require: Learningrateγ
andsecurity-sensitiveattributesareassignedaslowlearning Ensure: UpdatedprofilePi(t +1)
u
andadaptationrate. 1: ifTrust(t)<τ learn or(cid:53) i (t)>ϵ then
The system defines a learning rate γ i that controls 2: P u i(t +1)←P u i(t)
the speed at which the behavioral profile adapts to new 3: return
observations.Thesevaluesarepolicy-configurableandserve 4: endif
as conservative defaults for evaluation. This hybrid strategy 5: Updatemean(EWMA):
ensures responsiveness to legitimate behavioral drift while 6: µ i (t +1)←(1−γ)µ i (t)+γa i (t)
improvingrobustnessagainstnoiseandprofilepoisoning. 7: Updatevariance:
8:
σ
i
2(t +1)←(1−γ)σ
i
2(t)+γ(a
i
(t)−µ
i
(t))2
γ ↓ forstable/contextualattributes, 9: P u i(t +1)←{µ i (t +1),σ i 2(t +1)}
i
γ ↑ forbehavioralattributeswithnaturaldrift.
i
Furthermore,profileupdatesarecalculatedusingEWMA observations.Theaggregatedbehavioriscomputedas:
toensurethatprofilesrespondimmediatelytochanges,adapt
gradually to legitimate behavioral drift, maintain historical 1 X
a¯ (W)= a(t). (4)
precedents,andgivenewobservationsmoreweightageinthe i i |W| i
profile.
i t∈Wi
Behavioral profile updates are performed at two levels ProfileupdatesarethenappliedusingEWMA:
of granularity. Trust-based online updates apply to low-
frequency,low-noiseattributes,enablingimmediatebutcon- µ(t +1)=(1−γ)µ(t)+γa¯ (W).
i i i i i i
servative adaptation. For high-frequency or noisy attributes,
updates are performed over trusted observation windows, Windowed updates reduce sensitivity to transient noise and
allowinglearningfromaggregatebehaviorwhileimproving improve robustness against in-session profile poisoning.
stabilityandresistancetoprofilepoisoning. Algorithm 3 presents the windowed approach to behavioral
profileupdateforhigh-frequencyattributes.
a: TRUST-GATEDONLINEUPDATE
Forstable,low-noisebehavioralattributes(e.g.,logintime), Algorithm3WindowedBehavioralProfileUpdate
profile updates are performed using trust-gated online Require: ObservationwindowW ={a(t ),...,a(t )}
i 1 i k
learning. When learning is permitted, the profile mean is
Require: WindowtrustsummaryTrust(W)
updatedusingEWMA: Require: Windowpenaltyindicator(cid:53)(W)
i
µ i (t +1)=(1−γ i )µ i (t)+γ i a i (t), Require: ProfileP u i(t)
Require: Learningparametersτ ,γ
where 0 < γ i ≪ 1 is the attribute-specific learning rate. Ensure: UpdatedprofilePi(t + le 1 a ) rn
Online updates enable gradual adaptation from individual
1:
ifTrust(W)<τ
learn
or(cid:53) u
i
(W)>0then
t s r i u n s g t l e e d ev o e b n s t e . rvations while restricting the influence of any 2: P u i(t +1)←P u i(t)
3: return
Algorithm2demonstratesthetrust-gatedonlinebehavioral
4: endif
profileupdate.
5: Computewindowaggregate:
b: WINDOWEDBEHAVIORALUPDATE
6: a¯ i ← |W 1 | P t∈W a i (t)
7: Updatemean:
For high-frequency or noisy attributes (e.g., IP address, 8: µ i (t +1)←(1−γ)µ i (t)+γa¯ i
a ti c o c n es w s i p n a d t o te w r s n . s) L , e l t ea W rn i in = gi { s t 1 p , e . r . f . o , rm t|W e i d | } o d v e e n r o t t r e us a te w d i o n b d s o e w rv o a f - 9: P u i(t +1)←{µ i (t +1),σ i 2(t)}
VOLUME14,2026 77851

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Together, these strategies define how behavioral profiles Trustisupdatedas:
areupdated,asattributesareobservedandevaluated.
|     |     |     |     |     |     |     |     | Trust(t | +1)=Trust(t)+w |     |     | ·(AuthSuccess(t)) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | --- | ----------------- | --- | --- | --- |
m
|                                              |     |     |     |     |     |     |     |     |     |     | −π  | ·(1−AuthSuccess(t)), |     |     | (5) |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
| M. AUTHENTICATIONANDTRUSTINITIALIZATIONEVENT |     |     |     |     |     |     |     |     |     |     | m   |                      |     |     |     |
Anauthenticationsessionbeginswithanauthenticationand
trust initialization event, which establishes the initial trust where w m is the positive contribution of authentication
methodm,andπ
isthepenaltyapplieduponfailure.
| stateofauser–devicepairpriortoanyauthorizationdecision. |       |                |     |         |                 |     |     |     | m   |     |     |     |     |     |     |
| ------------------------------------------------------- | ----- | -------------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| This event                                              | marks | the transition |     | from an | unauthenticated |     |     |     |     |     |     |     |     |     |     |
requesttoanauthenticatedsessionandprovidesthebaseline 4) STEP-UPAUTHENTICATIONTRIGGER
Repeatedfailuresorlowresultingtrustmaytriggeradditional
trustfromwhichsubsequentauthorization,continuousmon-
itoring,andadaptiveenforcementoperate.Authenticationis authentication factors. Step-up authentication is required
when:
modeledasaniterativeprocessthatmayincluderetriesand
step-upchallengesbeforeastabletruststateisachieved.
|     |     |     |     |     |     |     |     |     |     | Trust(t)<τ |     |     | ,   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
step-up
| 1) AUTHENTICATIONEVENT |     |     |     |     |     |     | whereτ |         |                                          |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
|                        |     |     |     |     |     |     |        | step-up | isapolicy-definedthreshold.Step-upmecha- |     |     |     |     |     |     |
LetE auth (t)denoteanauthenticationeventattimet,defined nismsmayincludeOTP,hardware-backedchallenge,oraddi-
| as: |     |             |            |     |          |     | tionalverificationfactors. |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ---------- | --- | -------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | (t)=(cid:0) |            |     | (cid:1), |     |                            |     |     |     |     |     |     |     |     |
|     |     | E           | U,m,C(t),t |     |          |     |                            |     |     |     |     |     |     |     |     |
auth
5) RETRYCONSISTENCYANDTRUSTDELTAANALYSIS
whereU istheuseridentity,mistheauthenticationmethod Letk denotetheretryindexwithinthecurrentauthentication
|           |     |         |                |     |       |             | session.Thetrustvalueatretryk |     |     |     |     | isdefinedas: |     |     |     |
| --------- | --- | ------- | -------------- | --- | ----- | ----------- | ----------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- |
| employed, | and | C(t) is | the contextual |     | state | observed at |                               |     |     |     |     |              |     |     |     |
authenticationtime.
|     |     |     |     |     |     |     |     |     |     |     | =f (cid:0) | ,m ,H | (cid:1), |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | -------- | --- | --- |
AuthSuccess(t) ∈ {0,1} denotes the outcome of the Trust k C k k k−1
| authentication     |     | attempt. Authentication |            | succeeds  |     | if and only |                                   |     |                                        |     |     |     |                 |     |       |
| ------------------ | --- | ----------------------- | ---------- | --------- | --- | ----------- | --------------------------------- | --- | -------------------------------------- | --- | --- | --- | --------------- | --- | ----- |
|                    |     |                         |            |           |     |             | whereC                            |     | representsthecontextualstateatretryk,m |     |     |     |                 |     | isthe |
| if Admissible(t)=1 |     | and                     | the system | validates |     | method m    |                                   | k   |                                        |     |     |     |                 |     | k     |
|                    |     |                         |            |           |     |             | authenticationmethodemployed,andH |     |                                        |     |     |     | denotestheprior |     |       |
k−1
accordingtoitsdefinedassurancerequirements.
retryhistory.
Thetrustdeltabetweensuccessiveretriesismodeledas:
2) INITIALTRUSTASSIGNMENT
Upon successful authentication, an initial trust value is (cid:49)T =Trust −Trust . (6)
|     |     |     |     |     |     |     |     |     |     | k   | k   |     | k−1 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
assigned:
|     |     |     |           |       |     |     | In  | a Zero-Trust |     | system, | contextual |     | drift, device |     | change |
| --- | --- | --- | --------- | ----- | --- | --- | --- | ------------ | --- | ------- | ---------- | --- | ------------- | --- | ------ |
|     |     | )=T | (S(m),C(t | ),H(t | )), |     |     |              |     |         |            |     |               |     |        |
Trust(t 0 init 0 0 (e.g.,logginginfromadifferentdevice),ornetworkvariation
|         |     |                     |     |          |     |             | (e.g., | turning | on  | VPN) | may legitimately |     | reduce | trust | even |
| ------- | --- | ------------------- | --- | -------- | --- | ----------- | ------ | ------- | --- | ---- | ---------------- | --- | ------ | ----- | ---- |
| where T | (·) | is a policy-defined |     | function | of  | the authen- |        |         |     |      |                  |     |        |       |      |
init when authentication succeeds. The system can verify trust
| tication | strength | S(m), | the observed | authentication-time |     |     |             |     |         |           |     |       |                     |     |     |
| -------- | -------- | ----- | ------------ | ------------------- | --- | --- | ----------- | --- | ------- | --------- | --- | ----- | ------------------- | --- | --- |
|          |          |       |              |                     |     |     | fluctuation |     | between | attempts, |     | based | on a policy-defined |     |     |
context,andbehavioralhistory.Thisinitialtrustreflectsthe thresholdϵ >0,suchthat:
T
| assurance                                      | obtained | during | the authentication |     | phase, | along |     |     |     |     |               |     |     |     |     |
| ---------------------------------------------- | -------- | ------ | ------------------ | --- | ------ | ----- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
| withcontextualandhistoricalbehavioralevidence. |          |        |                    |     |        |       |     |     |     |     | (cid:49)T <−ϵ |     |     |     |     |
|                                                |          |        |                    |     |        |       |     |     |     |     | k             | T   |     |     |     |
Authenticationandtrustinitializationarecompletewhen:
|     |     |     |     |     |     |     | to  | determine | and | record | the | possibility | of  | brute | force |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | --- | ----------- | --- | ----- | ----- |
Admissible(t)=1 ∧ Trust(t)≥τ . attacks,credentialmisuse,automation,oradversarialreplay.
auth
|               |     |             |         |         |     |              | The                                                     | authentication |     | and | trust initialization |     | event | defines | the |
| ------------- | --- | ----------- | ------- | ------- | --- | ------------ | ------------------------------------------------------- | -------------- | --- | --- | -------------------- | --- | ----- | ------- | --- |
| The resulting |     | trust value | Trust(t | ) forms | the | baseline for |                                                         |                |     |     |                      |     |       |         |     |
|               |     |             |         | 0       |     |              | startingstateforcontinuousverificationundertheZeroTrust |                |     |     |                      |     |       |         |     |
subsequentauthorizationdecisionsandcontinuousmonitor-
|     |     |     |     |     |     |     | model. | Algorithm |     | 4 defines |     | the authentication |     | and | trust |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | --------- | --- | ------------------ | --- | --- | ----- |
ing.
initializationevent.
3) AUTHENTICATIONATTEMPTANDRETRYSEMANTICS
6) HARDVIOLATIONESCALATION
| Authentication |        | attempts may | succeed       | or  | fail due | to benign    |                |     |         |     |       |          |            |     |        |
| -------------- | ------ | ------------ | ------------- | --- | -------- | ------------ | -------------- | --- | ------- | --- | ----- | -------- | ---------- | --- | ------ |
|                |        |              |               |     |          |              | Authentication |     | failure |     | alone | does not | constitute |     | a hard |
| user error     | (e.g., | mistyped     | credentials). |     | Such     | failures are |                |     |         |     |       |          |            |     |        |
violation.However,excessivefailuresordetectionofadver-
| treated as | soft | violations | and result | in a | reduction | in trust |        |          |        |       |       |          |            |           |     |
| ---------- | ---- | ---------- | ---------- | ---- | --------- | -------- | ------ | -------- | ------ | ----- | ----- | -------- | ---------- | --------- | --- |
|            |      |            |            |      |           |          | sarial | patterns | (e.g., | brute | force | attacks, | credential | stuffing, |     |
ratherthanimmediatetermination.Authenticationretriesare automation,orcryptographicprooffailure)resultin:
| re-evaluated | under | ZT principles, |     | in which | each | retry is |     |     |     |     |     |     |     |     |     |
| ------------ | ----- | -------------- | --- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
treatedasanindependentrequestwithafreshcontextualand HV(t)←1.
behavioralassessment.
LetE (k) (t)denotethek-thauthenticationattemptwithina Once HV(t) = 1, the system becomes non-admissible and
auth
| sessionattimet. |     |     |     |     |     |     | thesessionisterminated. |     |     |     |     |     |     |               |     |
| --------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- |
| 77852           |     |     |     |     |     |     |                         |     |     |     |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm4AuthenticationWithRetryandTrustInitializa- Algorithm5AuthorizationDecisionEvaluation
tion Require: Resource R , context C(t), authentication state
s
procedureAuthenticate(U,m,C(t))
| 1:  |     |     |     |     |     |     | S(t) |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
attempts←0
| 2:            |     |     |     |     |     | Ensure: |                        | Authorizationdecision |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ------- | ---------------------- | --------------------- | --- | --- | --- | --- | --- |
| 3: Trust(t)←0 |     |     |     |     |     |         | if¬AuthValid(S(t))then |                       |     |     |     |     |     |
1:
| whileattempts<N |                       |     | do  |     |     |     |            |     |     |     |     |     |     |
| --------------- | --------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| 4:              |                       |     | max |     |     | 2:  | returnDeny |     |     |     |     |     |     |
| 5:              | ifAdmissible(t)=0then |     |     |     |     |     | endif      |     |     |     |     |     |     |
3:
|     | returnReject |                        |     |     |     |     | ˆ                           | (m,t)<S | ˆ (C(t),R |         |     |     |     |
| --- | ------------ | ---------------------- | --- | --- | --- | --- | --------------------------- | ------- | --------- | ------- | --- | --- | --- |
| 6:  |              |                        |     |     |     | 4:  | ifS eff                     |         | req       | s )then |     |     |     |
| 7:  | endif        |                        |     |     |     | 5:  | returnStep-UpAuthentication |         |           |         |     |     |     |
| 8:  | result       | ←VerifyAuthMethod(U,m) |     |     |     |     | endif                       |         |           |         |     |     |     |
6:
|     | ifresult            | =successthen |     |     |     |     | ifTrust(C(t))<τ |     |          |         |     |     |     |
| --- | ------------------- | ------------ | --- | --- | --- | --- | --------------- | --- | -------- | ------- | --- | --- | --- |
| 9:  |                     |              |     |     |     | 7:  |                 |     | grant (R | s )then |     |     |     |
| 10: | Trust(t)←Trust(t)+w |              |     | m   |     | 8:  | returnDeny      |     |          |         |     |     |     |
| 11: | else                |              |     |     |     |     |                 |     |          |         |     |     |     |
9: endif
Trust(t)←Trust(t)−π
| 12: |                     |     |     | m   |     | 10: | ifPr[AttackSuccess|C(t)]>δ |     |     |     | (R    | )then |     |
| --- | ------------------- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ----- | ----- | --- |
|     |                     |     |     |     |     |     |                            |     |     |     | grant | s     |     |
| 13: | attempts←attempts+1 |     |     |     |     |     | returnDeny                 |     |     |     |       |       |     |
11:
endif
| 14: |     |     |     |     |     | 12: | endif |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
ifTrust(t)<τ
| 15: |                  |     | step-up then     |     |     | 13: | returnAuthorize |     |     |     |     |     |     |
| --- | ---------------- | --- | ---------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
| 16: | TriggerStepUp(U) |     |                  |     |     |     |                 |     |     |     |     |     |     |
|     | stepResult       |     | ←VerifyStepUp(U) |     |     |     |                 |     |     |     |     |     |     |
17:
| 18: | ifstepResult |     | =failurethen |     |     |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Authorizationisgrantedifandonlyif:
HV(t)←DetectHardAttack(U)
19:
ifHV(t)=1then
20:
|     |     |                        |     |     |     | AuthValid(S(t))∧ContextAcceptable(C(t))∧(T(t)≥T |     |     |     |     |     |     | (R)) |
| --- | --- | ---------------------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
| 21: |     | returnTerminateSession |     |     |     |                                                 |     |     |     |     |     |     | r i  |
endif
22:
|     |                     |                     |      |      |     | where                                | T             | (R) is the              | trust required | to            | access       | R based | on the |
| --- | ------------------- | ------------------- | ---- | ---- | --- | ------------------------------------ | ------------- | ----------------------- | -------------- | ------------- | ------------ | ------- | ------ |
| 23: | else                |                     |      |      |     |                                      | r             | i                       |                |               |              | i       |        |
|     |                     |                     |      |      |     | specifiedpolicyPolicy                |               |                         | ontheresource. |               |              |         |        |
|     |                     | Trust(t)←Trust(t)+w |      |      |     |                                      |               |                         | Ri             |               |              |         |        |
| 24: |                     |                     |      | step |     |                                      |               |                         |                |               |              |         |        |
|     |                     |                     |      |      |     |                                      | Authorization |                         | decisions      | are evaluated | continuously |         | over   |
| 25: | endif               |                     |      |      |     |                                      |               |                         |                |               |              |         |        |
|     |                     |                     |      |      |     | time.Theauthorizationdecisionattimet |               |                         |                |               | ismodeledas: |         |        |
| 26: | endif               |                     |      |      |     |                                      |               |                         |                |               |              |         |        |
|     | ifTrust(t)≥τ        |                     | then |      |     |                                      |               |                         |                |               |              |         |        |
| 27: |                     |                     | auth |      |     |                                      |               |                         |                |               |              |         |        |
|     |                     |                     |      |      |     |                                      |               | A(t)=f(S(t),C(t),T(t),R |                |               |              | ),      |        |
| 28: | returnAuthenticated |                     |      |      |     |                                      |               |                         |                |               |              | s       |        |
endif
29:
whereS(t)denotestheauthenticationstate,C(t)thesession
30: endwhile
context,andT(t)thetrustgained.
31: HV(t)←1
|     |     |     |     |     |     |     |     | =   |     |     | |   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
returnLockorEscalate Let R(t) Pr[AttackSuccess C(t)] denote the
32:
|     |     |     |     |     |     | composite |     | risk evaluated | under | session | context |     | C(t). Each |
| --- | --- | --- | --- | --- | --- | --------- | --- | -------------- | ----- | ------- | ------- | --- | ---------- |
33: endprocedure
|     |     |     |     |     |     | protected |     | resource | R is associated |     | with two | risk | thresholds |
| --- | --- | --- | --- | --- | --- | --------- | --- | -------- | --------------- | --- | -------- | ---- | ---------- |
i
δ (R)andδ
(R)suchthat:
|                                |             |           |                |                     |       | 1   | i                 | 2 i |           |         |      |         |        |
| ------------------------------ | ----------- | --------- | -------------- | ------------------- | ----- | --- | ----------------- | --- | --------- | ------- | ---- | ------- | ------ |
| 7) SEPARATIONFROMAUTHORIZATION |             |           |                |                     |       |     |                   |     | 0<δ (R)<δ | (R)<1.  |      |         |        |
|                                |             |           |                |                     |       |     |                   |     | 1         | i 2     | i    |         |        |
| The trust                      | initialized | at        | authentication | time serves         | as an |     |                   |     |           |         |      |         |        |
| input to authorization         |             | decisions |                | but does not itself | imply |     |                   |     |           |         |      |         |        |
|                                |             |           |                |                     |       |     | The authorization |     | decision  | at time | t is | defined | as the |
accesstoanyprotectedresource.Authorizationisevaluated
followingthreshold-basedfunction:
| independently                                          | based | on  | resource | sensitivity, required | assur- |     |     |        |          |     |      |     |     |
| ------------------------------------------------------ | ----- | --- | -------- | --------------------- | ------ | --- | --- | ------ | -------- | --- | ---- | --- | --- |
| ancelevels,andcontextualrisk.Thisseparationensuresthat |       |     |          |                       |        |     |     |       |          |     |      |     |     |
|                                                        |       |     |          |                       |        |     |     | allow, | ifR(t)≤δ |     | (R), |     |     |
authentication establishes identity and baseline confidence,  1 i
while authorization enforces ZT prescribed least-privilege A(t)= step_up, ifδ (R)<R(t)≤δ (R), (7)
|     |     |     |     |     |     |     |     |     |     | 1 i |     | 2 i |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a c c e s s u nd e r c o n ti n u o us e va l u at i o n . W e n ow mo d el t h e deny,
|     |     |     |     |     |     |     |     |     | ifR(t)>δ |     | (R ). |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | --- | --- |
p o s t- l og in a u th o r iz a t io n an d s u b s e q u en t flo w s in th e n e x t 2 i
section.
|     |     |     |     |     |     |     | This ensures | that        | increasing    | risk | enforces  | stricter | actions |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------------- | ---- | --------- | -------- | ------- |
|     |     |     |     |     |     | to  | protect      | the system. | Authorization |      | decisions | thus     | become  |
N. AUTHORIZATIONDECISIONANDEVENT
continuousverificationconsistentwithZero-Trustprinciples.
Anauthorizationeventisdefinedas:
|     |     |                  |     |     |     | Algorithm |     | 5 defines | the | evaluation | of  | the authorization |     |
| --- | --- | ---------------- | --- | --- | --- | --------- | --- | --------- | --- | ---------- | --- | ----------------- | --- |
|     |     | (t)=(U,R,A(t),t) |     |     |     | decision. |     |           |     |            |     |                   |     |
|     |     | E a              | i i |     |     |           |     |           |     |            |     |                   |     |
Theissuanceanduseofauthorizationtokensthatmediate
whereU istheuser,R istherequestedresource,A(t)isthe access to protected resources following an authorization
| i   |     | i   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
authorizationdecisionandt isthedecisiontimestamp. decisionaremodeledinthefollowingsection.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     | 77853 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm6AuthorizationTokenGrant Algorithm7ResourceAccessEnforcement
Require: Authorizationdecision,contextC(t),resourceR Require: Accessrequest(T,R ),currentcontextC(t)
|         |        |          |     |     |     | s   |         |                |     | s   |     |     |
| ------- | ------ | -------- | --- | --- | --- | --- | ------- | -------------- | --- | --- | --- | --- |
| Ensure: | TokenT | ordenial |     |     |     |     | Ensure: | Accessdecision |     |     |     |     |
1: ifAuthorizationdecision̸=Authorizethen 1: if¬ValidateToken(T)then
|          | returnNoTokenIssued |     |     |     |     |     |     | returnDenyAccess |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
| 2:       |                     |     |     |     |     |     |     | 2:               |     |     |     |     |
| 3: endif |                     |     |     |     |     |     |     | 3: endif         |     |     |     |     |
Bindtokentocontext:T ←Bind(u,R ,C(t),t) if¬ContextMatch(T,C(t))then
| 4:  |     |     |     |     | s   |     |     | 4:  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5: Settokenvaliditywindowandscope 5: Applytoken-contextmismatchpenalty
| 6:  | LogauthorizationgranteventE |     |     |     | (t) |     |     | 6: returnDenyAccess |     |     |     |     |
| --- | --------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
g
| returnTokenT |     |     |     |     |     |     |     | endif |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
| 7:           |     |     |     |     |     |     |     | 7:    |     |     |     |     |
ifTrust(C(t))<τ
|     |     |     |     |     |     |     |     | 8:  | access | (R s )then |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | --- |
9: returnRe-authenticationRequired
| O. AUTHORIZATIONGRANTANDTOKEN-BASED |     |     |     |     |     |     | 10: | endif                      |     |     |          |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | -------- | --- |
|                                     |     |     |     |     |     |     | 11: | ifPr[AttackSuccess|C(t)]>δ |     |     | (R )then |     |
| RESOURCEACCESS                      |     |     |     |     |     |     |     |                            |     |     | access s |     |
returnDenyAccess
| In Zero-Trust |              | systems,   | authentication |          | alone does | not grant | 12: |       |     |     |     |     |
| ------------- | ------------ | ---------- | -------------- | -------- | ---------- | --------- | --- | ----- | --- | --- | --- | --- |
| access        | to protected | resources. |                | Instead, | successful | authen-   | 13: | endif |     |     |     |     |
14: returnGrantAccess
| tication | enables | an explicit |     | authorization | grant, | typically |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | ------------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
realizedthroughshort-livedauthorizationtokens(e.g.,OAuth
accesstokens,SecurityAssertionMarkupLanguage(SAML)
Tokenvalidityisdefinedas:
assertions,orJSONWebTokens(JWT)).
TokenValid(T,C(t))
| 1) AUTHORIZATIONTOKENMODEL |     |     |     |     |     |     |     | (cid:16) |                |     |                   | (cid:17) |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ----------------- | -------- |
|                            |     |     |     |     |     |     |     | =1 <τ    | ∧ Bind(T,C(t)) | ∧   | ScopeAllowed(ℓ,r) |          |
Authorization tokens are security artifacts distinct from t e
authentication sessions. An authorization token is modeled (9)
as:
Resourceaccessisgrantedifandonlyif:
|     |     | T   | =(U,s,ℓ,τ |     | ,κ) |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i e
|     |     |     |     |     |     |     |     | AuthValid(S(t)) |     | ∧ TokenValid(T,C(t))∧ |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------------- | --- | --- |
where:
|     |      |                 |     |     |     |     |     |     | Pr[AttackSuccess|C(t)]≤δ |     | r(Rs) | (10) |
| --- | ---- | --------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | ----- | ---- |
| •   | U ∈U | denotestheuser, |     |     |     |     |     |     |                          |     |       |      |
i
• sdenotestheassociatedauthenticationsessionidentifier, This formulation enforces continuous authorization even
• ℓdenotestheauthorizedscopeorprivileges, inthepresenceofvalidtokens.
τ denotesthetokenexpirationtime,
• e
κ
• denotescryptographicorcontextualbinding. P. CONTINUOUSMONITORINGANDRE-EVALUATION
|     |     |     |     |     |     |     | As  | a Zero-Trust | system, | the context, | risk, and trust | states |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------------ | --------------- | ------ |
2) AUTHORIZATIONGRANTEVENT mustbecontinuouslyevaluated,andauthorizationdecisions
Anauthorizationgranteventisdefinedas: should be revalidated throughout the lifetime of a session.
Thesystementersacontinuousmonitoringandre-evaluation
|     |     | E (t)=(S(t),C(t),T,t) |     |     |     |     |                                                       |     |     |     |     |     |
| --- | --- | --------------------- | --- | --- | --- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
|     |     | g                     |     |     |     |     | phasefollowingtheauthorizationgrantandtokenissue.This |     |     |     |     |     |
phasespansthelifetimeofthesession.
Anauthorizationtokenisissuedifandonlyif:
|     |     |     |     |     |     |     |     | The continuous | monitoring | function | at time t is modeled |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---------- | -------- | -------------------- | --- |
as:
|     | AuthValid(S(t)) |     | ∧   | S(m)≥S | req (C(t))∧ |     |     |     |     |     |     |     |
| --- | --------------- | --- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
Pr[AttackSuccess|C(t)]≤δ M(t):(C(t),T(t − ),R(t − ),T )→(T(t),R(t),E(t)),
|     |     |         |          |      | grant (R s ) |     |       |     |     | t   |     |     |
| --- | --- | ------- | -------- | ---- | ------------ | --- | ----- | --- | --- | --- | --- | --- |
|     | ∧   | (T(t)≥T |          |      |              |     |       |     |     |     |     |     |
|     |     |         | grant (R | s )) |              | (8) | where |     |     |     |     |     |
• C(t):currentcontext
| whereS(m)denotesauthenticationstrength,T |       |            |     |       |               | (R )isthe |     |                                      |     |     |     |     |
| ---------------------------------------- | ----- | ---------- | --- | ----- | ------------- | --------- | --- | ------------------------------------ | --- | --- | --- | --- |
|                                          |       |            |     |       | g ra nt       | s         |     | T(t−),T(t):pastandcurrenttruststates |     |     |     |     |
| minimum                                  | trust | threshold, | and | δ     | (R ) is t h e | ma ximum  |     | •                                    |     |     |     |     |
|                                          |       |            |     | grant | s             |           |     | R(t−),R(t):pastandcurrentriskstates  |     |     |     |     |
•
acceptableattacksuccessprobability.
• T :currentandactivetoken
| This | ensures | that possession |     | of  | valid credentials | alone |     | t   |     |     |     |     |
| ---- | ------- | --------------- | --- | --- | ----------------- | ----- | --- | --- | --- | --- | --- | --- |
is insufficient to obtain authorization artifacts. Algorithm 6 • E(t):enforcementdecision
Algorithm8representsthecontinuousmonitoringandre-
describestheauthorizationtokengrantflow.
evaluationflow.
3) RESOURCEACCESSUSINGAUTHORIZATIONTOKENS
| Aresourceaccessrequestattimet |     |     |     | isdefinedas: |     |     | 1)  | TRUSTUPDATE |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------ | --- | --- | --- | ----------- | --- | --- | --- | --- |
Trustevolvesasafunctionofpriortrust,currentcontext,and
(t)=(U,R,T,C(t))
|       |     | E r |     | i i |     |     | estimatedrisk. |     |     |     |               |     |
| ----- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | ------------- | --- |
| 77854 |     |     |     |     |     |     |                |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| Algorithm8ContinuousMonitoringandRe-Evaluation |     |     |     |     |     |     | 2) TRUSTDECAY |     |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Require: Activesession,contextstreamC(t)
Trustisdesignedtodecayevenintheabsenceofuseractions
Ensure: Updatedtrust,enforcementactions orreinforcingevidence.Trustdecayismodeledas:
1: whileSessionActivedo
|     | Observenewattributesandevents |     |     |     |     |     |     |     |          |     | −    | −µ(cid:49)t, |     |      |
| --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | ------------ | --- | ---- |
| 2:  |                               |     |     |     |     |     |     |     | T(t)=T(t |     | ) ∗e |              |     | (13) |
3: UpdatecontextC(t)
|     | Updateattributepenaltiesformismatchorabsence |     |     |     |     |     |       | (cid:49)t | = −t−, |          |              |     |         |          |
| --- | -------------------------------------------- | --- | --- | --- | --- | --- | ----- | --------- | ------ | -------- | ------------ | --- | ------- | -------- |
| 4:  |                                              |     |     |     |     |     | where |           | t      | the time | that elapsed |     | between | the past |
5: Updateauthenticationpenaltiesifapplicable truststateandcurrenttruststate,ensuringthatstalesessions
6: RecomputeTrust(C(t)),Pr[AttackSuccess|C(t)]
donotretainimplicittrust.
ifAnyauthorizationthresholdviolatedthen
| 7:  |                                               |     |     |     |     |     | The           | risk | R(t) is, however, |     | always | fully | recomputed | and |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | ------------- | ---- | ----------------- | --- | ------ | ----- | ---------- | --- |
| 8:  | Enforcestep-upauthentication,tokenrevocation, |     |     |     |     |     | doesnotdecay. |      |                   |     |        |       |            |     |
ortermination
9: endif
3) BINDINGVALIDATION
10: endwhile
|     |     |     |     |     |     |     | For     | attributes | bound | to       | the authorization |            | token, | con-   |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ----- | -------- | ----------------- | ---------- | ------ | ------ |
|     |     |     |     |     |     |     | tinuous | monitoring |       | verifies | that bound        | attributes |        | remain |
withindefinedtolerancethresholds.Violationscontributeto
Thecurrentcontextcanbemodeledas: increasedriskandacceleratedtrustdecay,mitigatingreplay
| C(t)=λ+X |     |     |     |     |     |     | andsessionhijackingattacks. |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
w ·Indicator(a).[match(a(t))]
|     |       | i   | i   | i   |     |     |     |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | ai ∈A |     |     |     |     |     |     |     |     |     |     |     |     |     |
4) RE-EVALUATIONANDENFORCEMENT
X(cid:16)
− λmm(R )· π ·Indicator(a).[mismatch(a(t))] Authorizationvalidityisre-evaluatedateachmonitoringstep
|     |     | i s i |     | i   |     | i   |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accordingto:
ai ∈A
|     |           |                        |     | ).(cid:2) |     | (t))(cid:3)(cid:17) |     |     |          |        |     |       |        |      |
| --- | --------- | ---------------------- | --- | --------- | --- | ------------------- | --- | --- | -------- | ------ | --- | ----- | ------ | ---- |
|     | +λm iss(R | )· π miss ·Indicator(a |     | missing(a |     |                     |     |     |          |        |     |       |        |      |
|     | i         | s i                    |     | i         |     | i                   |     |     |  Allow, | T(t)≥τ |     | ∧     | R(t)≤δ | ,    |
|     |           |                        |     |           |     |                     |     |     |       |        |     | allow |        | risk |
(11)
|        |     |     |     |     |     |     | Reeval(t)= |     | Step-Up,   | τ      | ≤T(t)<τ |        | ,      |      |
| ------ | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ------ | ------- | ------ | ------ | ---- |
|        |     |     |     |     |     |     |            |     |            |        | deny    |        | allow  |      |
| where: |     |     |     |     |     |     |            |     | Revoke, |        |         |        |        |      |
|        |     |     |     |     |     |     |            |     |            | T(t)<τ |         |        | R(t)>δ |      |
|        |     |     |     |     |     |     |            |     |            |        |         | deny ∨ |        | risk |
λ+ ∈ (0,1)denotestherateatwhichtrustincreasesin
| •   |                                          |              |        |            |     |         |      |             |     |         |                    |     |     | (14)   |
| --- | ---------------------------------------- | ------------ | ------ | ---------- | --- | ------- | ---- | ----------- | --- | ------- | ------------------ | --- | --- | ------ |
|     | responsetoamatchingcontextualattributea. |              |        |            | i   |         |      |             |     |         |                    |     |     |        |
| •   | w denotes                                | the positive | weight | associated |     | with an |      |             |     |         |                    |     |     |        |
|     | i                                        |              |        |            |     |         | This | formulation |     | ensures | that authorization |     | and | access |
attributea.
|     |           | i              |            |         |             |           | privilegesarecontinuouslyevaluatedandadaptivelyenforced |     |     |     |     |     |     |     |
| --- | --------- | -------------- | ---------- | ------- | ----------- | --------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | λm        | (0,1]          |            |         |             |           |                                                         |     |     |     |     |     |     |     |
| •   | m ∈       | denotes        | a mismatch |         | coefficient | for       |                                                         |     |     |     |     |     |     |     |
|     | i         |                |            |         |             |           | inresponsetotheevolvingcontextandthreatconditions.      |     |     |     |     |     |     |     |
|     | attribute | a. It controls | how        | rapidly | trust       | decreases |                                                         |     |     |     |     |     |     |     |
|     |           | i              |            |         |             |           | Havingdefinedtheauthenticationandauthorizationmech-     |     |     |     |     |     |     |     |
when the observed value of a i deviates from expected anisms,theadversarialthreatstothesystemaremodeledin
behavior.
thenextsection.
|     | λmiss ∈ | (0,1] denotes | the missing-attribute |     | coefficient |     |     |     |     |     |     |     |     |     |
| --- | ------- | ------------- | --------------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
• i
forattributea.Itgovernstherateoftrustreductionwhen
|     |              | i              |     |     |     |     | Q.  | THREATMODEL |     |     |     |     |     |     |
| --- | ------------ | -------------- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
|     | evidencefora | isunavailable. |     |     |     |     |     |             |     |     |     |     |     |     |
i
|     | π > |     |     |     |     |     | 1) ADVERSARYDEFINITION |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
• i 0denotesthepenaltyassociatedwithamismatch
Apolynomial-timeadversaryismodeledas:
ofattributea.
i
πmiss >0denotesthepenaltyassociatedwithamissing
| •   | i   |     |     |     |     |     |     |     |     | A=(K,C,G) |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
π
|     | at tribute | a. i This value | may differ | from | i   | to reflect |     |     |     |     |     |     |     |     |
| --- | ---------- | --------------- | ---------- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
scenarioswheretheabsenceofevidenceismoreorless
whereKdenotesattackerknowledge,Cattackercapabilities,
suspiciousthananexplicitmismatch.
andG theobjectiveofunauthorizedaccess.
•
(cid:26) : if x ispresent The knowledge and capability of the adversary can fall
|     |     | Indicator(x)= | 1   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
underdifferentattackclasses,suchas,butnotlimitedto:
0 : if x isabsent
|     |     |     |     |     |     |     |     | K={k | ,k  | ,k  | ,k  | ,k  | ,...}, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------ | --- |
Using(11),thecurrenttrustcanbemodeledas: auth grant replay hijack priv
|       |     | (1−λ+ | − λ+·C(t)−γ |     |      |      |        |     |     |     |     |     |     |     |
| ----- | --- | ----- | ----------- | --- | ---- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
| T(t)= |     | )T(t  | ) +         |     | R(t) | (12) | where: |     |     |     |     |     |     |     |
k :Authenticationcompromise
auth
Here,R(t) = Pr[AttackSuccess | C(t)]denotestheriskat k :Illicitauthorizationgrant
grant
|     |     |     |     | γ   | >   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
time t based on the current context and 0 represents k replay :Authorizationtokenreplay
the coefficient of risk, indicating how fast it suppresses k :Sessionhijack
hijack
| trust.        |     |     |     |     |     |     | k priv | :Privilegeescalation |     |     |     |     |     |       |
| ------------- | --- | --- | --- | --- | --- | --- | ------ | -------------------- | --- | --- | --- | --- | --- | ----- |
| VOLUME14,2026 |     |     |     |     |     |     |        |                      |     |     |     |     |     | 77855 |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| 2) ATTRIBUTE-LEVELTHREATS |     |     |     |     |     | 5) PROFILEPOISONING |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
∈Aischaracterizedby:
Eachcontextualattributea i Sincetheproposedframeworkincorporatesadaptivebehav-
|     |     |     |     |     |     | ioral | profiling, | an adversary | may | attempt to | manipulate |
| --- | --- | --- | --- | --- | --- | ----- | ---------- | ------------ | --- | ---------- | ---------- |
a =(E,S,D,ρ)
i i i i i learnedbaselinesbyinjectingmaliciousoratypicalbehavior
where E denotes entropy, S spoofability, D temporal over time, aiming to redefine normal context and reduce
|     | i   |     |     | i   | i   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
stability,andρ = Pr(R = 1 | a),representstheprobability anomalysensitivity.
|     |     | i   |     | i   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofattackgivena.
i
| Attribute-levelriskisdefinedas: |     |     |     |     |     | 6) COMPOSITETHREATSURFACE |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
Thecompositethreatsurfaceisdefinedastheprobabilityof
|     |     | Risk(a)=λ | (1−E)+λ | S +λ | ρ   |     |     |     |     |     |     |
| --- | --- | --------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
i 1 i 2 i 3 i unauthorized access under session context C(t), accounting
|                                                 |     |     |     |     |       | for attacks | during | both | authentication | and authorization |     |
| ----------------------------------------------- | --- | --- | --- | --- | ----- | ----------- | ------ | ---- | -------------- | ----------------- | --- |
| Theprobabilityofanadversaryspoofinganattributea |     |     |     |     | i can |             |        |      |                |                   |     |
| bedefinedas:                                    |     |     |     |     |       | phases.     |        |      |                |                   |     |
Pr[Forge(a)|C]∈[0,1]
i
a: AUTHENTICATION-PHASEATTACK
The effective attribute compromise probability can be Theprobabilityofasuccessfulauthentication-phaseattackis
definedas:
definedas:
n
|C(t)]
|     | Pr[Forge(A)|C]= |     |     | Y Pr[Forge(a)|C] |     |     | Pr[Attack | auth |     |     |     |
| --- | --------------- | --- | --- | ---------------- | --- | --- | --------- | ---- | --- | --- | --- |
i
=1−(1−Pr(Break(m)|C(t))·
i=1
Y
|                                |     |     |     |     |     |     |          | (1−Pr(Forge(a)|C(t))), |     |     | (15) |
| ------------------------------ | --- | --- | --- | --- | --- | --- | -------- | ---------------------- | --- | --- | ---- |
| 3) AUTHENTICATIONMETHODTHREATS |     |     |     |     |     |     |          |                        | i   |     |      |
| Eachauthenticationmethodm∈M    |     |     |     |     |     |     | ai ∈C(t) |                        |     |     |      |
isrepresentedas:
|     |     |     |     |     |     | where | Pr[Break(m) | | C(t) | denotes | the probability | of  |
| --- | --- | --- | --- | --- | --- | ----- | ----------- | ------ | ------- | --------------- | --- |
m=(S(m),Rel(m),PR(m))
|     |     |     |     |     |     | compromising | the | active | authentication | method | m and |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | -------------- | ------ | ----- |
|
where S(m) denotes strength, Rel(m) reliability, and PR(m) Pr[Forge(a i ) C(t)] captures the forgeability of contextual
| phishingresistance. |     |     |     |     |     | attributesusedduringauthentication. |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
The probability of compromise of an authentication Ifmultipleauthenticationmethodsareusedduringthelife
| methodmisapproximatedas: |     |     |     |     |     | ofasession,then(15)canbemodifiedas: |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
−S(m)(1−PR(m))
|     |     | Pr[Break(m)]=e |     |     |     |     | Pr[Attack | |C(t)] |     |     |     |
| --- | --- | -------------- | --- | --- | --- | --- | --------- | ------ | --- | --- | --- |
auth
Y
|     |           |             |     |                 |             |     | =1− | (1−Pr(Break(m)|C(t))· |     |     |     |
| --- | --------- | ----------- | --- | --------------- | ----------- | --- | --- | --------------------- | --- | --- | --- |
| The | effective | probability |     | of an adversary | breaking an |     |     |                       |     |     |     |
authentication method, given a surrounding context C, can m∈M(t)
| bemodeledas: |     |     |     |     |     |     | Y   |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(1−Pr(Forge(a)|C(t)))
i
| Pr[Break(m)|C]=Pr[Break(m)]·(1+η·Risk(C)), |     |     |     |     |     |     | ai ∈C(t) |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
whereηdefinesthesensitivityofthemethodmtocontextual
b: AUTHORIZATION-PHASEATTACK
riskRisk(C). In a Zero-Trust system, contextual attributes are validated
|     |     |     |     |     |     | after authentication |     | through | authorization | and | continuous |
| --- | --- | --- | --- | --- | --- | -------------------- | --- | ------- | ------------- | --- | ---------- |
4) SESSIONHIJACKINGANDTOKENREPLAY access checks. Let A ⊆ A denote the subset of attributes
b
boundtotheauthorizationtokenorsession.
Asessionhijackingortokenreplayeventismodeledas:
Theauthorization-phaseattackprobabilityisdefinedas:
|                                                    |     | E (t)=(U |     | ′,R,T′,C(t)) |     |     |           |        |     |     |     |
| -------------------------------------------------- | --- | -------- | --- | ------------ | --- | --- | --------- | ------ | --- | --- | --- |
|                                                    |     | r        | i   | i            |     |     |           |        |     |     |     |
|                                                    |     |          |     |              |     |     | Pr[Attack | |C(t)] |     |     |     |
| whereU′maydifferfromtheoriginalauthenticateduserU, |     |          |     |              |     |     |           | authz  |     |     |     |
|                                                    | i   |          |     |              | i   |     |           |        |     |     |     |
capturingsessionhijackingortokentheftscenarios. =Pr[IllicitGrant]
Y
Tokenreplayattacksaremodeledas: +Pr[Replay]· Pr[Forge(a)|C(t)]
i
|     | ∃T′ | ̸=T | TokenValid(T′,C(t))=1 |     |     |     |     |     | ai ∈Ab |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | ------ | --- | --- |
s.t.
|                                                |     |     |     |     |     |     |              |     | Y Pr[Forge(a)|C(t)]. |     |      |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------------------- | --- | ---- |
|                                                |     |     |     |     |     |     | +Pr[Hijack]· |     |                      |     | (16) |
| Theprobabilityofreplaysuccessisapproximatedas: |     |     |     |     |     |     |              |     |                      | i   |      |
ai ∈Ab
Pr[ReplaySuccess]=Pr[Steal(T)]·Pr[BindFail(T,C(t))]
c: UNIFIEDATTACKSUCCESSPROBABILITY
Sessionhijackingisdefinedas: Combining(15)and(16),theoverallprobabilityofunautho-
rizedaccessisdefinedas:
|     |     | U   | ′ ̸=U | ∧ T′ =T |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | i i   |         |     |     |     |     |     |     |     |
Pr[AttackSuccess|C(t)]
| Both | attacks | are | mitigated | through contextual | binding, |            |             |        |                            |     |                |
| ---- | ------- | --- | --------- | ------------------ | -------- | ---------- | ----------- | ------ | -------------------------- | --- | -------------- |
|      |         |     |           |                    |          | =1−(cid:0) | 1−Pr[Attack | |C(t)] | (cid:1)(cid:0) 1−Pr[Attack |     | |C(t)] (cid:1) |
continuousauthorization,andadaptivetrustdegradation. auth authz
| 77856 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
R. ATTRIBUTEWEIGHTANDPENALTYASSIGNMENT aphase-specificversionw i (p).Phase-specificweightsallow
MODEL factoringinresourcesensitivityateachphaseofaction.
This section formalizes the computation, initialization, and
β θ
e p i
online adaptation of attribute weights and penalties used in w(phase)= ,
trustevaluation.Weightsarederivedfromthreat-relatedprop-
i Pn
j=1 e
β
p
θ
j
erties and are computed periodically, ensuring continuous wherephase∈{login,grant,access,continuous access}.
validation.
2) ATTRIBUTEPENALTYFORMULATION
1) ATTRIBUTEUTILITYANDWEIGHTFORMULATION
While attribute weights determine how trust is accumulates
a: ATTRIBUTEUTILITY
throughpositiveevidence,attributepenaltiesmodeltheloss
Let A = {a ,a ,...,a } denote the set of attributes. Each
1 2 n of trust when expected evidence is absent or contradicts
attributea ischaracterizedbythefollowingproperties:
i it. In a Zero Trust system, both missing and mismatched
• E i ∈[0,1]:entropy(uniqueness), attributesconstitutenegativeevidence,withdifferentsecurity
• S i ∈[0,1]:spoofability, implications.
• D i ∈[0,1]:temporalstability,
• ρ i ∈ [0,1]:riskcorrelation,whereρ i = Pr(R = 1 | a i ) a: PENALTYTYPESFORMISSINGANDMISMATCHED
denotestheprobabilityofanattack.
ATTRIBUTES
Here, ρ i follows a Beta distribution, ρ i ∼ Beta(α i ,β i ), Foreachattributea i ,twopenaltyparametersaremaintained:
whereα i andβ i denotethecountofattackandbenignobser- • π i miss: penalty applied when the attribute a i is missing
vations, respectively. The Beta distribution model allows
fromtheobservedcontext.
incremental learning and refining the attack correlation • π i mm:penaltyappliedwhentheattributea i ispresentbut
as data builds. Spoofability and stability properties of an
mismatchesitsexpectedorboundvalue.
attribute are treated as structural properties that remain
constant over time. They are re-evaluated as attack vectors
3) INTEGRATIONOFATTRIBUTEPENALTIESINTOTRUST
evolve.
COMPUTATION
Each attribute is associated with a normalized attribute
The overall trust score incorporates both weights and
utilityscoreasafunctionofitsproperties:
penalties:
θ i =U(a i )=α E E i +α D D i +α ρ(1−ρ i )−α S S i (17) Trust(C(t))= X w (t) Indicator.[match(a)]
i i
whereα E ,α D ,α ρ ,α S ≥0and: i
− X πmiss,(t) Indicator.[missing(a)]
α E +α D +α ρ +α S =1 i i i
− X πmm,(t) Indicator.[mismatch(a)],
b: COMPUTATIONOFATTRIBUTEWEIGHTS i i
Attributeweightsareobtainedusingsoftmaxnormalization: i
(19)
βθ
w = e i (18) enabling the accumulation and degradation of trust in
i Pn
j=1 e
βθ
j accordancewithZeroTrustprinciples.
where β > 0 determines how a difference in the attribute’s
4) ATTRIBUTEWEIGHTINITIALIZATIONSTRATEGIES
utilityaffectstheweightderivationoftheattribute.
In the proposed system, attribute weights are derived from
Byconstruction:
attribute properties such as entropy, spoofability, reliability,
n and attack correlation. Attribute weight derivation operates
X
w =1
i under three regimes, depending on the availability of
i=1 empiricaldata.
Thesoftmaxnormalizationisutilizedtoensurethatstrong
attributes(highentropy,lowspoofability)contributemoreto a: INITIALIZATIONUSINGHISTORICALOBSERVATIONS
trustgainthanweakattributes.Thisensuresthatevenifthe Whensufficienthistoricaldataisavailable,attributeweights
adversarymanagestospoofweakattributes,thecontribution are initialized using evidence derived from prior authen-
totrustwillbeminimal. tication and access logs. This process combines entropy,
Depending on the sensitivity of the resources, attribute Bayesian estimation of attack correlation, and structural
weights can be modified based on the phase in which they attribute properties to derive an initial utility score for each
are participating (authentication, authorization, token grant, attribute.
resource access). The parameter β can be modified to be Leta denoteanattributeandR∈{0,1}denotethesecurity
i
a phase-specific version β such that the weight becomes outcome,whereR = 1correspondstoanadversarialevent.
p
VOLUME14,2026 77857

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
HistoricallogsareanalyzedtocomputetheentropyofRand Algorithm9AttributeWeightInitializationWithHistorical
theconditionalentropyofRgivenattributea. Data
i
Shannonentropyoftheattackandconditionalentropyare Require: AttributesetA={a 1 ,a 2 ,...,a n }
computedas: Require: HistoricallogdatasetL
Require: Structuralattributeproperties{S,D}
X i i
H(R)=− P(R)log 2 P(R) (20) Require: InitialBetapriorparameters{(α i ,β i )}
H(R|a)=
X
P(a =v)H(R|a =v), (21)
Require: Coefficientsλ
1
,λ
2
,λ
3
,λ
4
>0
i i i Require: Inversetemperatureβ >0
v∈Vi Ensure: Initialandupdatedattributeweights{w (t)}
i
where V i represents the set of all possible values that the ▷OfflinePhase:BatchInitializationUsingHistorical
attributea cantake.InformationgainIG(a)ofattributea
i i i Data
IG =H(R)−H(R|a), (22) 1: foreachattributea i ∈Ado
ai i
2: Compute:IG(a i )←H(R)−H(R|a i )
quantifies the reduction in uncertainty about the security 3: Countattackandbenignoccurrences(α i ,β i )
outcomeafterobservingtheattribute.
4:
ComputeposteriormeanE[ρ(0) ],utilityθ(0)
i i
Inparallel,theattackcorrelationofattributea i ismodeled 5: endfor
asaBayesianrandomvariable: ▷ComputeInitialWeights
ρ =Pr(R=1|a), 6: foreachattributea i ∈Ado
i i
7: w
(0) ←softmax(β,θ(0)
)
i i
withaBetapriorinitializedfromhistoricalattackandbenign 8: endfor
observations.Theposteriormean, return{w (0)}
i
α
E[ρ]= i , (23)
i α +β
i i
providestheestimateofthelikelihoodthatthepresenceofa i of historical data. Structural properties such as spoofability
isassociatedwithadversarialbehavior. andtemporalstabilityareencodedinbaselineutilities,while
Using these quantities, the initial utility of attribute a i is Bayesianpriorsareinitializedtoenablesubsequentlearning.
definedas:
θ(0) =λ IG +λ D +λ E[ρ]−λ S, (24) Algorithm 10 Offline Expert-Only Attribute Utility Initial-
i 1 ai 2 i 3 i 4 i
ization
where D i denotes the temporal stability of the attribute, S i Require: AttributesetA={a 1 ,a 2 ,...,a n }
denotes its spoofability, and λ k > 0 are policy-defined Require: Expert-definedbaselineutilities{θ(0)}n
i i=1
coefficientsreflectingtherelativeimportanceofeachfactor.
Require:
InitialBetapriorparameters{α(0),β(0)}n
The initial attribute weights are then computed using Require: Inversetemperatureparameterβ
i
>0
i i=1
softmaxnormalization: Ensure: Initialattributeweights{w (0)}n
i i=1
w ( i 0) = P e βθ β i (0 θ ) (0) 1: foreachattribu ▷ te In a i i ti ∈ al A ize do attributeutilitiesandpriors
j
e j
2:
θ
i
←θ
i
(0)
ensuringcontributionsacrossattributes. 3: ρ i ∼Beta(α i (0),β i (0) )
Algorithm9representsattributeweightinitializationusing 4: endfor
historicalevidence. ▷Computeinitialweights
5: foreachattributea i ∈Ado
b: INITIALIZATIONUSINGEXPERTKNOWLEDGE 6: w ( i 0) ←softmax(β,θ i )
Whennoattackhistorylogsexist,andonlyexpertknowledge 7: endfor
is available to set attribute values, the expert defines initial
return{w (
i
0)}n
i=1
utilityscoresforattributesθ0 =θexpert .
i i
Intheabsenceofhistoricalobservationslinkingattributes
to security outcomes, the expert assigns θ0 and embeds an c: INITIALIZATIONUNDERMAXIMALUNCERTAINTY
initial ρ0 as a prior belief. The initial attr i ibute weights are Whenreliableestimatesof{E i ,D i ,S i ,ρ i }areunavailable,the
compute
i
dbasedontheθ(0) as:
systemadoptsauniformfallbackinitialization:
i
w (0) = e βθ i (0) w i = n 1 , ∀a i ∈A
i Pn
e
βθ
j
(0)
j=1 Thisfallbackrepresentsanon-informativepriorandtotal
Algorithm 10 denotes attribute utilities and weights uncertainty over the attributes, ensuring unbiased baseline
initialization using expert knowledge alone, in the absence behavior.Asempiricalobservationsaccumulate,thesystem
77858 VOLUME14,2026

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
transitions from uniform to entropy-driven weights without Everytimethesystemobservesattributea:
i
alteringtheunderlyingtrustorauthorizationlogic. (
(α +1,β), (Attack |a)=1
(α,β)← i i i (27)
i i (α,β +1), (Attack |a)=0
5) ATTRIBUTEPENALTYINITIALIZATIONSTRATEGIES i i i
Similar to attribute weights, penalties are initialized under
The system computes the updated risk correlation and the
threedistinctregimesdependingoninformationavailability. posteriormeanofρ as:
i
α
a: INITIALIZATIONUSINGHISTORICALOBSERVATIONS ρ i (t) =E[ρ i |α i ,β i ]= α + i β
i i
When historical logs are available, penalties are initialized
usingempiricalattackcorrelation.Let: Informationgainmayberecomputedperiodicallyorupdated
incrementally.WithinformationgainIG(a)ofattributea
i i
ρmiss =Pr(R=1|a missing),
i i IG =H(R)−H(R|a),
ρmm =Pr(R=1|a mismatched), ai i
i i
,theoverallattributeutilityattimetrelativetoitsinitialvalue
bemodeledusingBetadistributions.Theinitialpenaltiesare
isdefinedas:
thendefinedas:
π i miss,(0) =ν 1 E[ρ i miss], π i mm,(0) =ν 2 E[ρ i mm], θ i (t) =θ i (0)+η 1 (cid:0)E[ρ i (t) ]−E[ρ i (0) ] (cid:1)+η 2 (cid:0) IG( a t i )−IG( a 0 i ) ( (cid:1) 2 , 8)
withν >ν ,ensuringstrongerpenaltiesformismatches.
2 1 whereη ,η >0controlsthesensitivityofutilityupdatesto
1 2
newlyobservedevidence.
b: INITIALIZATIONUSINGEXPERTKNOWLEDGE (t)
Updated attribute weights w are obtained via softmax
When expert knowledge is available but historical data is i
normalizationandusedinsubsequenttrustcomputationand
absent, penalties are initialized based on structural attribute
adaptiveenforcementdecisions.
propertiessuchasspoofabilityandtemporalstability:
βθt
π
π
i
m
m
i
m
ss
,
,
(
(
0
0
)
) =
=
µ
π
1
m
S
is
i
s,
+
(0)
µ
+
2
(
(cid:49)
1−
,
D
i
), (
(
2
2
5
6
)
)
wt
i
=
Pn
j
e
=1 e
i
βθ
j
t
,
i i i
where β > 0 determines how a difference in the attribute’s
whereS denotesspoofability,D denotestemporalstability,
i i
utilityaffectstheweightderivationoftheattribute.
andµ ,(cid:49) >0arepolicy-definedcoefficientsreflectingthe
k i
Algorithm 11 incrementally refines attribute utilities
severityofnegativeevidence.
and weights using Bayesian updating and entropy-based
information gain. This enables adaptation from cold start
c: INITIALIZATIONUNDERMAXIMALUNCERTAINTY
or arbitrary assignment to data-driven operation, based on
In the absence of both expert guidance and historical data,
accumulatingevidence.
penaltiesareinitializeduniformly:
πmiss,(0) =πmiss, πmm,(0) =πmm, b: ONLINERECALIBRATIONOFPENALTIES
i base i base
Thepenaltyrecalibrationprocessoperatesonpenaltysignals
where πmm > πmiss are conservative, policy-defined
base base obtainedbydynamicattributeanalysis,adjustingtheirimpact
constants.
ontrustandriskbasedonaccumulatedevidenceandsystem
policy.
6) ONLINELEARNINGANDADAPTATIONOFWEIGHTSAND
As new session outcomes are observed, penalties are
PENALTIES
updated incrementally using Bayesian estimation. Separate
Once the baseline weights and penalties are defined, the
Beta posteriors are maintained for missing and mismatched
system continues to learn and recalibrate its values as data
events and updated based on observed attack or benign
accumulates. At this stage, the system transitions into an
outcomes.
entropy-basedlearningregime.
Penaltiesarerecalibratedusingadelta-basedupdate:
a: ONLINERECALIBRATIONOFATTRIBUTEWEIGHT π i miss,(t) =π i miss,(t−1)+γ miss (cid:0)E[ρ i miss,(t) ]−E[ρ i miss,(t−1) ] (cid:1),
Asthesystemoperates,newsessionoutcomesareobserved (29)
andincorporated intothemodel.The Betaposteriorparam- πmm,(t) =πmm,(t−1)+γ (cid:0)E[ρmm,(t) ]−E[ρmm,(t−1)
]
(cid:1),
eters (α,β) are updated incrementally based on observed i i mm i i
i i (30)
attack and benign events, generating an updated posterior
mean E[ρ(t) ]. Initially, attribute weights are dominated by subject to predefined bounds πmin ≤ π(·) ≤ πmax.
i i i i
expertpriorsorarbitraryassignments.Asobservationsaccu- This formulation ensures stable learning while preventing
mulate, Bayesian posterior means and entropy-based infor- unboundedtrustloss.
mationgaingraduallyshiftimportancetowardsattributesthat Algorithm12recordsincrementalrecalibrationofattribute
correlatewithattacks. penaltiesbasedonaccumulatingevidence.
VOLUME14,2026 77859

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm 11 Online Attribute Weight Recalibration via Algorithm12OnlineBayesianAttributePenaltyRecalibra-
| BayesianLearning |     |                  |     |      |          |     | tion     |               |     |     |            |           |     |
| ---------------- | --- | ---------------- | --- | ---- | -------- | --- | -------- | ------------- | --- | --- | ---------- | --------- | --- |
|                  |     | AttributesetA={a |     | ,a   | ,...,a } |     | Require: | AttributesetA |     |     |            |           |     |
| Require:         |     |                  |     | 1    | 2 n      |     |          |               |     |     |            |           |     |
|                  |     |                  |     | (0 ) |          |     |          |               |     |     | { π m is s | , π m m } |     |
R e q u i r e : I n i t i a l i z e d u t i l i t i e s { θ } n R e q u i r e : I n i ti a l i z e d p e n a lt i e s
|     |     |     |     | i   | i= 1 |     |     |     |     |     | i   | i   |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
R e q u i r e : I n i t i a l i z e d B e t a p a r a m e t e r s {α , β }n R e q u i r e : L e a r n i n g c o e f fi c i e n t s α , α > 0
|     |     |     |     |     | i i i=1 |     |     |     |     |     | 1   | 2   |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
α , α > R e q u i r e : P e n a l t y le a rn in g r a te s γ , γ >0
R e q u i r e : L e a r n i n g co e f fi c i e n t s 0 m is s m m
|          |                           |                              |     |     | 1 2   |     |          | Penaltyboundsπ   |     | min,π | max |     |     |
| -------- | ------------------------- | ---------------------------- | --- | --- | ----- | --- | -------- | ---------------- | --- | ----- | --- | --- | --- |
| Require: |                           | Inversetemperatureparameterβ |     |     | >0    |     | Require: |                  |     |       |     |     |     |
|          |                           |                              |     |     |       |     |          |                  |     | i     | i   |     |     |
|          | Updatedattributeweights{w |                              |     |     | (t)}n |     | Ensure:  | Updatedpenalties |     |       |     |     |     |
Ensure:
i i=1
whilenewsessionobservation(C(t),R(t))isavailabledo 1: whilenewsession(C(t),R(t))observeddo
1:
▷Penaltylearningformissingandmismatched
▷Updateattackcorrelationposteriors
|     | foreachattributea |              |     | ∈C(t)do |                 |     | attributes |                   |                       |      |     |     |     |
| --- | ----------------- | ------------ | --- | ------- | --------------- | --- | ---------- | ----------------- | --------------------- | ---- | --- | --- | --- |
| 2:  |                   |              |     | i       |                 |     |            |                   |                       |      |     |     |     |
|     |                   | ifR(t)=1then |     |         |                 |     | 2:         | foreachattributea |                       | ∈Ado |     |     |     |
| 3:  |                   |              |     |         |                 |     |            |                   |                       | i    |     |     |     |
| 4:  |                   | α ←α         | +1  |         | ▷Attackobserved |     | 3:         | ifa               | i ismissinginC(t)then |      |     |     |     |
|     |                   | i            | i   |         |                 |     |            |                   |                       |      |     |     |     |
|     |                   | else         |     |         |                 |     | 4:         |                   | ifR(t)=1then          |      |     |     |     |
5:
|     |     | β ←β  |     |     |                 |     |     |     | π    | miss ←min(π | miss+γ |      | ,π max) |
| --- | --- | ----- | --- | --- | --------------- | --- | --- | --- | ---- | ----------- | ------ | ---- | ------- |
| 6:  |     |       | +1  |     | ▷Benignobserved |     | 5:  |     | i    |             | i      | miss | i       |
|     |     | i     | i   |     |                 |     |     |     |      |             |        |      |         |
|     |     | endif |     |     |                 |     | 6:  |     | else |             |        |      |         |
7:
|     |        |     |     |     |     |     | 7:  |     | π   | miss ←max(π | miss−γ |      | ,π min) |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ---- | ------- |
| 8:  | endfor |     |     |     |     |     |     |     | i   |             | i      | miss | i       |
endif
| 9:  | foreachattributea |     |     | ∈Ado |     |     | 8:  |     |     |     |     |     |     |
| --- | ----------------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
|     |                   | Compute:E[ρ       |     | ],IG(a | )   |     | 9:  | elseifa |              | mismatchesbaselineinC(t)then |      |     |         |
| --- | ----------------- | ----------------- | --- | ------ | --- | --- | --- | ------- | ------------ | ---------------------------- | ---- | --- | ------- |
| 10: |                   |                   |     | i      | i   |     |     |         | i            |                              |      |     |         |
|     |                   | Updateutilityθ(t) |     |        |     |     |     |         | ifR(t)=1then |                              |      |     |         |
| 11: |                   |                   |     |        |     |     | 10: |         |              |                              |      |     |         |
|     |                   |                   |     | i      |     |     |     |         | π            | mm ←min(π                    | mm+γ |     | ,π max) |
|     | endfor            |                   |     |        |     |     | 11: |         |              |                              |      | mm  |         |
| 12: |                   |                   |     |        |     |     |     |         | i            |                              | i    |     | i       |
|     |                   |                   |     | ∈Ado   |     |     | 12: |         | else         |                              |      |     |         |
| 13: | foreachattributea |                   |     | i      |     |     |     |         |              |                              |      |     |         |
|     |                   | ( t)              |     | (t)    |     |     |     |         | π            | mm ←max(π                    | mm−γ |     | ,π min) |
| 14: |                   | w ←softmax(β,θ    |     |        | )   |     | 13: |         | i            |                              | i    | mm  | i       |
|     |                   | i                 |     | i      |     |     |     |         |              |                              |      |     |         |
|     | endfor            |                   |     |        |     |     | 14: |         | endif        |                              |      |     |         |
15:
endif
| 16: | endwhile |       |     |     |     |     | 15: |        |     |     |     |     |     |
| --- | -------- | ----- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
|     | return{w | (t)}n |     |     |     |     | 16: | endfor |     |     |     |     |     |
i i=1
17: endwhile
return{πmiss,πmm}
|     |     |     |     |     |     |     |     | i   | i   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7) BASELINEATTRIBUTEWEIGHTINGASSUMPTION
| Although |     | NIST standards |     | primarily | define | requirements |     |     |     |     |     |     |     |
| -------- | --- | -------------- | --- | --------- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
for authentication mechanisms, they explicitly permit and S(m)=f(H ,R ,B ,L ),
|     |     |     |     |     |     |     |     |     |     | m   | m m | m   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
encouragetheuseofcontextualandbehavioralattributesfor
where
risk-basedandcontinuousauthorizationdecisions,provided
such attributes are not treated as standalone authenticators. • H represents credential entropy or cryptographic
m
| Table6showcasesindicativebaselinevaluesofweightsand |     |     |     |     |     |     | strength |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
penaltiesforthecompositeattributesetdefinedinTable2. • R m representsresistancetoattacks
The expert priors defined in this work align with these • B representshowtightlymcanbindtotheuser,device,
m
| guidelines |     | and serve | solely | as initial | conditions | that are |     |     |     |     |     |     |     |
| ---------- | --- | --------- | ------ | ---------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
orsessioncontext
progressivelyrefinedthroughempiricallearning. • L representslifecycleassurance
m
S. AUTHENTICATIONSTRENGTHANDPENALTY b: RELATIONSHIPTOAUTHENTICATIONASSURANCE
| ASSIGNMENTMODEL |     |     |     |     |     |     | LEVELS |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
1) AUTHENTICATIONSTRENGTHFORMULATION Authentication strength provides a quantitative mapping to
|     |     |     |     |     |     |     | authentication |     | assurance | levels. | A mapping |     | function φ(·) |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | ------- | --------- | --- | ------------- |
a: DEFINITIONOFAUTHENTICATIONSTRENGTH
associatesstrengthvalueswithrequiredassurancethresholds:
| Definition1: |     | The | authentication |     | weight w | reflects the |     |     |     |     |     |     |     |
| ------------ | --- | --- | -------------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
m
relativeexposureofanauthenticationmethodtoanadversary AAL(m)=φ(cid:0) ˆ (cid:1),
|                                               |     |     |     |     |     |            |     |     |     |     | S (m) |     | (31) |
| --------------------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ----- | --- | ---- |
| anditscontributiontotheoverallattacksurface.w |     |     |     |     |     | m provides |     |     |     |     |       |     |      |
φ(·)
thedegreeoflikelihoodthatanadversarywilltargetmethod where is indicative and aligns with the assurance
requirementsdefinedinNISTSP800-63B.
m.
| Authentication |     | weights | do  | not represent | security | strength. |     |     |     |     |     |     |     |
| -------------- | --- | ------- | --- | ------------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Instead,weightsscaletheimpactofasuccessfulbreakrather c: DEFINITIONOFAUTHENTICATIONUTILITY
|                            |     |     |     |     |     |     | Let M | = {m ,m | ,...,m | } denote | the | set of | authentication |
| -------------------------- | --- | --- | --- | --- | --- | --- | ----- | ------- | ------ | -------- | --- | ------ | -------------- |
| thanreducingitslikelihood. |     |     |     |     |     |     |       | 1       | 2      | k        |     |        |                |
Letmdenoteanauthenticationmethod.Theauthentication methods.Eachmethodmischaracterizedby:
strengthofm,denotedasS(m),isdefinedas: • S(m):authenticationstrength,
| 77860 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE6. Indicativeattributeweightsandpenaltiesfromexpertpriors.
• Rel(m)∈[0,1]:reliability, e: INTEGRATIONOFAUTHENTICATIONWEIGHTSINTO
PR(m)∈{0,1}:phishingresistance,
| •   |     |     |     |     | THREATMODELING |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
• Pr[Break(m)]:probabilityofcompromise. The weighted authentication-phase attack probability is
definedas:
Theauthenticationmethodutilityscoreisdefinedas:
|        | =γ logS(m)+γ | Rel(m)+γ  | PR(m)−γ |                |     | Pr[Attack                        | |C]            |     |     |                  |     |      |
| ------ | ------------ | --------- | ------- | -------------- | --- | -------------------------------- | -------------- | --- | --- | ---------------- | --- | ---- |
| U m    | S            | R         | P       | B Pr[Break(m)] |     |                                  | auth           |     |     |                  |     |      |
|        |              |           |         |                |     |                                  |                |     | !   |                  |     |      |
|        |              |           |         | (32)           |     |                                  |                |     | n   |                  |     |      |
|        |              |           |         |                |     | X                                |                |     | Y   | Pr[Forge(a)|C]wi |     |      |
|        |              |           |         |                |     | =                                | w Pr[Break(m)] |     | ·   |                  |     | (33) |
|        |              |           |         |                |     |                                  | m              |     |     |                  | i   |      |
| whereγ | ,γ ,γ        | ,γ ≥0and: |         |                |     |                                  |                |     |     |                  |     |      |
|        | S R          | P B       |         |                |     | m∈M                              |                |     | i=1 |                  |     |      |
|        |              | γ +γ +γ   | +γ =1   |                | 2)  | AUTHENTICATIONPENALTYFORMULATION |                |     |     |                  |     |      |
|        |              | S R       | P B     |                |     |                                  |                |     |     |                  |     |      |
a: DEFINITIONOFAUTHENTICATIONPENALTY
ThevalueofS(m)isdrivenbyitsentropyscore.Theutility Definition2(AuthenticationPenalty): An authentication
functiontakesthelogarithmicvalueofS(m)toensureitdoes penalty (cid:53) (t) represents a reactive measure the sys-
m
|     |     |     |     |     | tem | undertakes | by  | reducing | the | effective | authentication |     |
| --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | --- | --------- | -------------- | --- |
notdominateovertheotherproperties.
|     |     |     |     |     | assurance |             | in response |          | to observed |      | failures,      | degrada- |
| --- | --- | --- | --- | --- | --------- | ----------- | ----------- | -------- | ----------- | ---- | -------------- | -------- |
|     |     |     |     |     | tion,     | or fallback |             | behavior | associated  | with | authentication |          |
d: COMPUTATIONOFAUTHENTICATIONMETHODSCORES
| Authenticationmethodweightsarecomputedas: |     |     |     |     | methodm. |                   |     |                |            |        |         |             |
| ----------------------------------------- | --- | --- | --- | --- | -------- | ----------------- | --- | -------------- | ---------- | ------ | ------- | ----------- |
|                                           |     |     |     |     | Let      | m denote          | an  | authentication |            | method | invoked | at time     |
|                                           |     |     | λUm |     | t.       | An authentication |     | penalty        | quantifies |        | the     | degradation |
e
w =
m P λU m′ in trust caused by failed, weak, or downgraded authen-
m′∈M e
|     |     |     |     |     | tication | during | an  | authentication |     | or  | re-authentication |     |
| --- | --- | --- | --- | --- | -------- | ------ | --- | -------------- | --- | --- | ----------------- | --- |
whereλ>0controlssensitivity.Byconstruction:
event.
Theauthenticationpenaltyisdefinedasafunction:
|     |     | X   | =1  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
w m
|               |     |     |     |     |     | (cid:53) | (t)=f(Auth |     | ,Auth | ,Auth |          |       |
| ------------- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ----- | ----- | -------- | ----- |
|               |     | m∈M |     |     |     |          | m          |     | fail  | deg   | fallback | )     |
| VOLUME14,2026 |     |     |     |     |     |          |            |     |       |       |          | 77861 |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
b: PENALTYTYPESFORAUTHENTICATIONMETHODS a: INITIALIZATIONUSINGSTANDARDSANDHISTORICAL
The system defines the following authentication penalty OBSERVATIONS
types: When standards, guidance, and historical security data are
(cid:53)fail available, authentication strength is initialized based on the
|     | 1) Authentication |     | failure | penalty |     | (t), | when an |     |     |     |     |     |     |     |     |
| --- | ----------------- | --- | ------- | ------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
m
authenticationchallengeusingmfails. intrinsic properties of the authentication method and its
alignmentwithestablishedassurancerequirements.
(
|     |     |     |     | πfail,ifAuthFail(m,t) |     |     |     |     | =   | ,R  | ,B ,L |     |     |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
(cid:53)fail(t)= m LetS(m) f(H m m m m )denotetheintrinsicstrength
m 0,otherwise, formulation defined in Section V-S1. Initial strength values
arecomputedas:
|     | whereπfail |     | >0  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
m
|     |                   |     |             |     |          |         |          |             |     | (cid:16) |      |     |      |      | (cid:17) |
| --- | ----------------- | --- | ----------- | --- | -------- | ------- | -------- | ----------- | --- | -------- | ---- | --- | ---- | ---- | -------- |
|     |                   |     |             |     |          |         |          | S(0)(m)=log |     | 1+ω      | H +ω | R   | +ω B | +ω L | ,        |
|     |                   |     |             |     |          |         |          |             |     |          | 1 m  | 2 m | 3 m  | 4    | m        |
|     | 2) Authentication |     | degradation |     | penalty, | applied | when the |             |     |          |      |     |      |      |          |
(35)
methodmdoesnotmeettherequiredassuranceforthe
currentcontextC(t). where the constituent properties are instantiated using
|     |     |     |     |     |     |     |     | method-specific |     | characteristics |     | derived | from | standards | such |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | --- | ------- | ---- | --------- | ---- |
(
|     |     |     | πdeg∗(cid:49)S,ifS(m)<S |     |     | (C(t) |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ----------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:53)deg(t)= m req as NIST SP 800-63B and industry best practices. The
m
0,otherwise, logarithmic conversion ensures stronger properties do not
dominatetheresult.
where S(m) is the authentication strength of m, ˆ(0)(m)isthenmappedtoanNIST
ThenormalizedstrengthS
|     | S (C(t))     | is          | the strength | required |     | by the context, | and |                |     |           |       |         |           |         |     |
| --- | ------------ | ----------- | ------------ | -------- | --- | --------------- | --- | -------------- | --- | --------- | ----- | ------- | --------- | ------- | --- |
|     | req          |             |              |          |     |                 |     | authentication |     | assurance | level | using a | monotonic | mapping |     |
|     | (cid:49)S =S | (C(t))−S(m) |              |          |     |                 |     |                |     |           |       |         |           |         |     |
|     |              | req         |              |          |     |                 |     | function:      |     |           |       |         |           |         |     |
3) Authenticationfallbackpenalty,appliedwhenaweaker
methodisusedafterastrongermethodwasrequested AAL(m)=φ(cid:0) ˆ(0)(m) (cid:1),
S
orfailed.
|     |     |     | (   |     |     |     |     | Thismappingisindicative. |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
πfb,iffallbacktomoccurs
|     | (cid:53)fallback(t)= |     |     | m            |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | m                    |     |     | 0,otherwise, |     |     |     |     |     |     |     |     |     |     |     |
b: INITIALIZATIONUSINGEXPERTKNOWLEDGE
whereπfb >0 In the absence of authoritative standards mappings or
m
|     |            |     |        |     |           |     |            | sufficient  | historical | data,        | authentication |     | strength      | may | be    |
| --- | ---------- | --- | ------ | --- | --------- | --- | ---------- | ----------- | ---------- | ------------ | -------------- | --- | ------------- | --- | ----- |
|     | Typically, | πfb | > πdeg | ≥   | πfail and | the | cumulative |             |            |              |                |     |               |     |       |
|     |            | m   |        | m   | m         |     |            |             |            |              |                |     |               |     |       |
|     |            |     |        |     |           |     |            | initialized |            | using expert | knowledge.     |     | This approach |     | helps |
authenticationpenaltyismodeledas:
|     |     |     |     |     |     |     |     | in deriving |     | authentication | strengths | in  | case | of customized, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --------- | --- | ---- | -------------- | --- |
(cid:53) (t)=(cid:53)fail(t)+(cid:53)deg(t)+(cid:53)fallback(t) proprietary, enterprise-specific, or emerging authentication
|     |     | m   |     |     |     |     | (34) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | m   | m   |     | m   |      |     |     |     |     |     |     |     |     |
mechanismsforwhichstandardizedassurancelevelsarenot
|     | The ordering | πfb | > πdeg | ≥ πfail | reflects | the | increasing |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------ | ------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
yetestablished.Domainexpertsassignaninitialutilityscore
| severityofauthenticationcontroldegradation,consistentwith |     |     |     |     |     |     |     | θexpert |      |              |          |               |     |           |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------------ | -------- | ------------- | --- | --------- | --- |
|                                                           |     |     |     |     |     |     |     | m       | that | reflects the | expected | cryptographic |     | hardness, |     |
riskmanagementguidanceinNISTSP800-30andNISTSP
attackresistance,bindingproperties,andlifecycleguarantees
800-37, and in the authentication literature [56], [57], [58], ofthemethod:
[59].
|     |     |     |     |     |     |     |     |     |     | S(0)(m)=U |     | expert. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --- | --- | --- |
m
c: INTEGRATIONOFAUTHENTICATIONPENALTIESINTO
TRUSTCOMPUTATION
c: INITIALIZATIONUNDERMAXIMALUNCERTAINTY
Authentication penalties reduce the overall trust score of a When neither standards guidance nor expert knowledge is
contextC(t),modeledas:
available,authenticationstrengthisinitializedconservatively
|     |                       |     |     |     | X   |              |     | under                             | maximal | uncertainty. | All | authentication |     | methods | are |
| --- | --------------------- | --- | --- | --- | --- | ------------ | --- | --------------------------------- | ------- | ------------ | --- | -------------- | --- | ------- | --- |
|     | Trust(t)=Trust(C(t))− |     |     |     |     | (cid:53) (t) |     |                                   |         |              |     |                |     |         |     |
|     |                       |     |     |     |     | m            |     | assignedauniformbaselinestrength: |         |              |     |                |     |         |     |
m∈M(t)
|     |     |     |     |     |     |     |     |     |     |     | S(0)(m)=S | ,   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
base
3) AUTHENTICATIONSTRENGTHINITIALIZATION
STRATEGIES
|     |     |     |     |     |     |     |     | whereS |     | isapolicy-definedconstantrepresentingminimal |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
base
Authentication strength initialization defines the baseline assurance.Thisstrategyensuressafedefaultbehaviorwhile
| assurance | associated |     | with | each authentication |     | method | prior |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ---- | ------------------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
avoidingoverestimationofauthenticationassurance.
to any runtime observations. The authentication method In the absence of prior data, the system initializes
| strength | initialization |              | strategies | depend       |           | on historical | obser-     |                    |     |        |         |              |     |      |      |
| -------- | -------------- | ------------ | ---------- | ------------ | --------- | ------------- | ---------- | ------------------ | --- | ------ | ------- | ------------ | --- | ---- | ---- |
|          |                |              |            |              |           |               |            | the authentication |     | method | utility | coefficients |     | from | (32) |
| vations, | the            | availability |            | of standards | guidance, |               | and expert |                    |     |        |         |              |     |      |      |
uniformly,as:
| knowledge.                                              |     | These | strategies | differ | only | in how | the initial |     |     |      |     |     |     |               |     |
| ------------------------------------------------------- | --- | ----- | ---------- | ------ | ---- | ------ | ----------- | --- | --- | ---- | --- | --- | --- | ------------- | --- |
| strengthvalueisinstantiated;thesubsequentenforcementand |     |       |            |        |      |        |             |     |     |      |     |     | 1   |               |     |
|                                                         |     |       |            |        |      |        |             |     |     | γ =γ | =γ  | =γ  | =   |               |     |
|                                                         |     |       |            |        |      |        |             |     |     | S    | R   | P B |     |               |     |
| adaptationlogicremainsunchanged.                        |     |       |            |        |      |        |             |     |     |      |     |     | 4   |               |     |
| 77862                                                   |     |       |            |        |      |        |             |     |     |      |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Under this assumption, the authentication method utility c: INITIALIZATIONUNDERMAXIMALUNCERTAINTY
functionmodeledin(32)reducesto: When neither historical data nor expert knowledge is
available,conservativedefaultsareused:
1
U = (logS(m)+Rel(m)+PR(m)−Pr[Break(m)])
m 4 πx,(0) =πx , x ∈{fail,degrade,fallback},
m base
This uniform initialization treats all security-relevant withπfb >πdeg ≥πfail.
propertiesofanauthenticationmethodasequallyimportant. base base base
TheresultingutilityU isinterpretedasasecurityscoreand
m 5) ONLINELEARNINGANDADAPTATIONOF
isnormalizedviasoftmaxtoobtaintheauthenticationmethod
AUTHENTICATIONPENALTIES
weight:
The penalty recalibration process operates on instantaneous
e
λUm penalty signals generated by dynamic attribute analysis,
w m = P
m′∈M
e λU m′ a
ev
d
i
j
d
u
e
st
n
i
c
n
e
g
a
th
n
e
d
ir
sy
im
st
p
em
act
p
o
o
n
lic
tr
y
u
.
standriskbasedonaccumulated
For each penalty type x, a Beta posterior ρx ∼
The uniform initialization is adopted solely for baseline m
evaluation and reproducibility; the coefficients γ i can be Beta(α m x,β m x) is maintained. Upon observing a session
outcomeR(t),theposteriorparametersareupdatedas:
re-estimated or adapted using security outcomes once the
systemisoperational. αx ←αx +1[R(t)=1], βx ←βx +1[R(t)=0] (37)
Regardless of the initialization strategy, authentication m m m m
strength is treated as an intrinsic, static property of the Penaltiesarerecalibratedusingadelta-basedupdaterule:
authentication method. Runtime behavior, authentication
outcomes,andcontextualfactorsdonotmodifyS(m)directly π m x,(t) =π m x,(t−1)+γ x (cid:0)E[ρ m x,(t)]−E[ρ m x,(t−1)] (cid:1), (38)
andareinsteadcapturedthroughauthenticationpenaltiesand
subjecttoboundsπmin ≤πx,(t) ≤πmax.
contextual trust signals. Authentication strengths are recal- m m m
ibrated as standards evolve (e.g., NIST standards revision),
whenexploitationofthemethodisreported,orcryptographic T. INTEGRATIONOFAUTHENTICATIONSTRENGTHAND
breaksoccur. PENALTIESINTOAUTHORIZATIONTHRESHOLDS
Thisseparationensuresthatdifferencesbetweeninitializa- Authorization decisions in the proposed framework are
tionstrategiesaffectonlybaselineassuranceanddonotalter governed by both the intrinsic assurance provided by
threatmodelingassumptionsorenforcementdecisions. authentication methods and the dynamic trust and risk
signals accumulated during system interaction. Authenti-
cation strength acts as a minimum assurance gate, while
4) AUTHENTICATIONPENALTYINITIALIZATIONSTRATEGIES
authenticationpenaltiesdynamicallyadjusttheeffectivetrust
a: INITIALIZATIONUSINGSTANDARDSANDHISTORICAL
andattacksuccessprobability.
OBSERVATIONS
When historical data is available, penalties are initialized
1) PENALTY-ADJUSTEDEFFECTIVEAUTHENTICATION
using empirical attack correlations. We model the Beta
distribution: STRENGTH
Authentication penalties degrade the effective assurance of
ρx =Pr(R=1|x), x ∈{fail,degrade,fallback}, an authentication method without modifying its intrinsic
m
strength. We define the penalty-adjusted authentication
as the probability distribution of an attack scenario. Initial strengthas:
penaltiesaredefinedas:
S ˆ
eff
(m,t)=S ˆ (m)−λ (cid:53)·(cid:53)
m
(t), (39)
π
m
x,(0) =κ
x
E[ρ
m
x],
where (cid:53) (t) is the cumulative authentication penalty and
m
withκ >κ ≥κ .
λ
(cid:53)
>0isapolicy-definedscalingfactor.
fb deg fail
2) PENALTY-ADJUSTEDTRUSTTHRESHOLD
b: INITIALIZATIONUSINGEXPERTKNOWLEDGE
Authentication penalties also influence authorization indi-
Intheabsenceofhistoricaldata,penaltiesareinitializedusing
rectlythroughtrustdegradation:
expert-definedpriorsreflectingtheintrinsicweaknessofthe
authenticationmethod: Trust(C(t))=Trust (C(t))− X (cid:53) (t), (40)
attr m
πx,(0) =µ (1−S(m)), x ∈{fail,degrade,fallback},
m∈M(t)
m x
(36) ensuring that repeated authentication failures or downgrade
attemptsrapidlyreducetrustbelowauthorizationthresholds
withµ >µ ≥µ . forsensitiveresources.
fb deg fail
VOLUME14,2026 77863

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
3) AUTHORIZATIONGRANTCONDITION • Step-upauthenticationtoastrongermethodm′suchthat
|     |     |     |     |     |     |     |     |     | S ˆ (m′,t)≥S | ˆ   | (C(t),R | );  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | --- | --- | --- | --- |
Let R s denote a protected resource with sensitivity level eff req s
σ(R ).Anauthorizationgranteventattimet isdefinedas • Tokenrevocationorscopereduction;
s
• Accessdenialorsessiontermination.
|     |     | (t)=(cid:0) | S(t),C(t),T,t |     | (cid:1), |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E
|            |     | g          |                |     |        |      |        |     | Thismechanismenablescontinuousauthorization,ensur- |     |            |     |        |          |        |
| ---------- | --- | ---------- | -------------- | --- | ------ | ---- | ------ | --- | -------------------------------------------------- | --- | ---------- | --- | ------ | -------- | ------ |
|            |     |            |                |     |        |      |        | ing | that authentication                                |     | assurance, |     | trust, | and risk | remain |
| where S(t) | is  | the active | authentication |     | state, | C(t) | is the |     |                                                    |     |            |     |        |          |        |
sessioncontext,andT istheissuedauthorizationtoken. alignedwithresourcesensitivitythroughoutthesession.
| The          | authorization |     | token grant | event | from | (8) | can be |     |                                          |     |     |     |     |     |     |
| ------------ | ------------- | --- | ----------- | ----- | ---- | --- | ------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| rewrittenas: |               |     |             |       |      |     |        | U.  | BASELINEPARAMETERIZATIONFOREVALUATIONAND |     |     |     |     |     |     |
POLICYTUNING
|     |     |     |     | ˆ (m,t)≥S |     | ˆ (C(t),R |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E (t) ⇐⇒ AuthValid(S(t)) ∧ S ) Authentication strength values are indicative baselines used
| g   |     |     |     | eff |     | req | s   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Trust(C(t))≥τ
| ∧   |     |       | (R ) |     |     |     |     | forevaluationandpolicytuning,derivedfromtheassurance |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | grant | s    |     |     |     |     |                                                      |     |     |     |     |     |     |     |
Pr[AttackSuccess|C(t)]≤δ ), propertiesdefinedinNISTSP800-63BandFIDOspecifica-
| ∧   |     |     |     |       | (R  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     | grant | s   |     |     |     |     |     |     |     |     |     |     |
tions,anddonotimplyformalcertification.
ˆ
where S (m) denotes effective authentication strength, Table 7 maps common authentication methods to NIST
eff
S (t) = f(Pr[AttackSuccess | C(t)]), τ (R ) is the AALandFIDO,alongwithindicativebaselineauthentication
| req |     |     |     |     |     | grant s |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
δ
minimum trust threshold, and grant (R s ) is the maximum strengthsandpenaltiesforevaluationandpolicytuning.
| acceptable | attack | success | probability, |     | thereby | allowing |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | ------- | ------------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
authentication degradation and fallback behavior to directly V. DETECTINGANDENFORCINGHARDVIOLATIONS
influenceauthorizationoutcomes. Hardviolationsrepresentnon-compensablestatesthatresult
inrequestdenialandsuspensionoflearningandrecalibration.
4) PENALTY-AMPLIFIEDATTACKSUCCESSPROBABILITY We model the computation and validation of hard violation
Authenticationpenaltiesrepresentruntimeevidenceofdegra- signalsbelow.
| dation, | failure, | or fallback | behavior | of  | authentication |     | meth- |     |     |     |     |     |     |     |     |
| ------- | -------- | ----------- | -------- | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ods,indicatingincreasedadversarialactivity.Authentication 1) GEO-VELOCITYCOMPUTATION
penalties thus provide a baseline of the break probability of Geo-velocity,calculatedfromthetimebetweenrequestsand
the authentication method and reflect elevated risk. This is the geographic distance, is crucial for risk assessment and
in line with NIST SP 800-30, which recommends treating analysis.Thegeo-velocityriskmodelisrepresentedusingthe
| indicatorsasameasureofthelikelihoodofathreat. |           |             |     |          |     |                |     | riskFunction: |     |     |     |     |     |     |     |
| --------------------------------------------- | --------- | ----------- | --- | -------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| With                                          | this, the | probability | of  | breaking | an  | authentication |     |               |     |     |     |     |     |     |     |
methodisremodeledas:
|     |     |     |     |     |     |     |     |     |     |      |     | ifv≤v |       |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | ----- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |  0 |     |       | saf e |     |     |
v−
Pr[Break(m)|(cid:53) (t)]=Pr[Break(m)] (cid:0) 1+η (cid:53) (t) (cid:1), v s afe
|     |     | m   |     |     |     | m m |     |     | G(v)= |          |     | ifv  | < v  | <v  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | ---- | ---- | --- | --- |
|     |     |     |     |     |     |     |     |     |       | v        | − v |      | safe | max |     |
|     |     |     |     |     |     |     |     |     |       | ∞ max |     | safe |      |     |     |
where (cid:53) (t) represents the authentication penalty imposed ifv≥v
|         | m                 |     |           |     |          |            |     |     |     |     |            |     | max       |     |     |
| ------- | ----------------- | --- | --------- | --- | -------- | ---------- | --- | --- | --- | --- | ---------- | --- | --------- | --- | --- |
| in case | of authentication |     | challenge |     | failure, | downgrade, |     |     |     |     |            |     |           |     |     |
|         |                   |     |           |     |          |            |     |     |     | =   | (cid:49) d |     | (cid:49)d |     |     |
or fallback using m, and η > 0 is a method-specific where velocity v (cid:49) km/h and is the Haversine
|     |     |     | m   |     |     |     |     |     |     |     | t   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distancebetweentwoconsecutivelogins.
sensitivityparameter.
|                                                       |     |     |     |     |     |     |     |     | The geo-velocity |     | safe threshold |     | v is | set between | 800- |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------- | --- | ---- | ----------- | ---- |
| Theauthentication-phaseattackprobabilitydefinedin(15) |     |     |     |     |     |     |     |     |                  |     |                |     | safe |             |      |
isredefinedas: 1000 km/h [60]. The threshold v is set to 1000 km/h as
max
|           |     |        |     |     |     |     |     | the | upper bound | of  | plausible | commercial |     | air travel | speed, |
| --------- | --- | ------ | --- | --- | --- | --- | --- | --- | ----------- | --- | --------- | ---------- | --- | ---------- | ------ |
| Pr[Attack |     | |C(t)] |     |     |     |     |     |     |             |     |           |            |     |            |        |
auth allowing margin for geolocation inaccuracy and clock skew
|     |     | (cid:16) |     |     |     |     | (cid:17) |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Y 1−Pr[Break(m)](1+η (cid:53) while excluding physically impossible transitions. Speeds
| =1− |     |     |     |     |     | m m (t)) |     |       |                |     |               |     |        |        |           |
| --- | --- | --- | --- | --- | --- | -------- | --- | ----- | -------------- | --- | ------------- | --- | ------ | ------ | --------- |
|     |     |     |     |     |     |          |     | below | this threshold |     | but exceeding |     | normal | travel | rates are |
m∈M(t)
(cid:16) (cid:17) treated as probabilistic anomalies rather than deterministic
| .   | Y 1−Pr[Forge(a)|C(t)) |     |     |     |     |     |     |             |          |     |      |              |           |     |          |
| --- | --------------------- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ---- | ------------ | --------- | --- | -------- |
|     |                       |     | i   |     |     |     |     | violations. | Requests |     | with | geo-velocity | exceeding |     | the hard |
∈C(t)
ai limit are blocked and reported as risky, given typical user
displacement.
Thismodelingcontributesdirectlytothecompositeattack
φ ,φ
successprobabilityusedinauthorizationdecisions. Given two points with latitudes 1 2 and longitudes
|     |     |     |     |     |     |     |     | λ   | ,λ            |     |               |          |     | (cid:49)d     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------- | -------- | --- | ------------- | --- |
|     |     |     |     |     |     |     |     |     | (in radians), |     | the Haversine | distance |     | is calculated |     |
|     |     |     |     |     |     |     |     | 1   | 2             |     |               |          |     |               |     |
as:
5) ADAPTIVEAUTHORIZATIONENFORCEMENT
|                                          |     |                               |     |     |     |              |     |     |           | (cid:18)(cid:49)φ(cid:19) |           |          |      | (cid:18)(cid:49)λ(cid:19) |     |
| ---------------------------------------- | --- | ----------------------------- | --- | --- | --- | ------------ | --- | --- | --------- | ------------------------- | --------- | -------- | ---- | ------------------------- | --- |
| Therequiredauthenticationstrengthattimet |     |                               |     |     |     | isdefinedas: |     |     |           |                           |           |          |      |                           |     |
|                                          |     |                               |     |     |     |              |     |     | a=sin2    |                           | +cosφ     | cosφ     | sin2 |                           | ,   |
|                                          |     |                               |     |     |     |              |     |     |           |                           |           | 1        | 2    |                           |     |
|                                          |     |                               |     |     |     |              |     |     |           |                           | 2         |          |      | 2                         |     |
|                                          | S   | (t)=f(Pr[AttackSuccess|C(t)]) |     |     |     |              |     |     |           |                           | (cid:16)√ | √        |      |                           |     |
|                                          | req |                               |     |     |     |              |     |     |           |                           |           | (cid:17) |      |                           |     |
|                                          |     |                               |     |     |     |              |     |     | c=2·atan2 |                           | a,        | 1−a      | ,    |                           |     |
Ifanyconditionin(V-T3)isviolated,thesystemenforces
·c,
| oneofthefollowingactionsbasedonpolicy: |     |     |     |     |     |     |     |     | d =R | E   |     |     |     |               | (41) |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | ------------- | ---- |
| 77864                                  |     |     |     |     |     |     |     |     |      |     |     |     |     | VOLUME14,2026 |      |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE7. IndicativebaselineauthenticationstrengthsandpenaltiesmappedtoNISTAALandFIDO.
| where:        |       |                           |     |     |     |     | attackerrebuildstheapplication,thevaluechanges,andcan |     |         |             |           |     |           |
| ------------- | ----- | ------------------------- | --- | --- | --- | --- | ----------------------------------------------------- | --- | ------- | ----------- | --------- | --- | --------- |
| (cid:49)φ     | =φ −φ |                           |     |     |     |     | bedetectedbytheserver.                                |     |         |             |           |     |           |
| •             |       | (differenceinlatitudes),  |     |     |     |     |                                                       |     |         |             |           |     |           |
|               | 2     | 1                         |     |     |     |     | The algorithms                                        |     | for the | application | integrity |     | check and |
| • (cid:49)λ=λ | −λ    | (differenceinlongitudes), |     |     |     |     |                                                       |     |         |             |           |     |           |
|               | 2     | 1                         |     |     |     |     | dynamicbuildsecretinjectionarepresentedinAlgorithms13 |     |         |             |           |     |           |
• R E istheEarth’sradius(meanradius=6,371km),
|     |     |     |     |     |     |     | and 14, | respectively. |     | The corresponding |     | anti-tampering |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ----------------- | --- | -------------- | --- |
• atan2(y,x)isthetwo-argumentarctangentfunction.
techniquesaredescribedinAlgorithm15.
2) APPLICATIONINTEGRITYENFORCEMENT
With the increased penetration of smartphones, mobile W. DEVICEINTEGRITYENFORCEMENT
|              |      |         |        |         |     |             | In ZT architecture, |     | device | posture | is  | a trust | signal that |
| ------------ | ---- | ------- | ------ | ------- | --- | ----------- | ------------------- | --- | ------ | ------- | --- | ------- | ----------- |
| applications | form | a major | access | medium. | The | application |                     |     |        |         |     |         |             |
attributesdescribedinTable2provideacontextualattribute is given as much weight as user identity. Policy-driven
subset that can be used to statically verify the origin of the specificationscandetectifthedeviceposturedoesnotmeet
request.Theapplicationattributesprovideawaytouniquely the policy-set requirements and deny access, even if the
identify ‘‘the application, running on device’’ combination. user identity is valid. Just as trust signals related to users’
|              |     |          |           |     |            |         | behavioral | and contextual |     | attributes | are | validated, | device- |
| ------------ | --- | -------- | --------- | --- | ---------- | ------- | ---------- | -------------- | --- | ---------- | --- | ---------- | ------- |
| In addition, | the | proposed | framework |     | introduces | two new |            |                |     |            |     |            |         |
approachestomitigatetheriskofapplicationspoofing. originated attributes are also continuously monitored. The
proposedZeTHAAframeworkintroducesanadaptivedevice
|     |     |     |     |     |     |     | authentication | protocol |     | that aligns | with | NIST guidance | on  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --- | ----------- | ---- | ------------- | --- |
a: APPLICATIONINTEGRITYCHECKS
|        |           |            |     |            |        |             | device binding | by  | combining |     | contextual | device | attributes |
| ------ | --------- | ---------- | --- | ---------- | ------ | ----------- | -------------- | --- | --------- | --- | ---------- | ------ | ---------- |
| During | the first | connection | of  | the device | to the | system, the |                |     |           |     |            |        |            |
withhardware-backedverification.Passivedeviceattributes
| Cyclic Redundancy |                 | Check  | (CRC)       | value        | of the   | constituent    |                  |                   |                |            |                   |          |            |
| ----------------- | --------------- | ------ | ----------- | ------------ | -------- | -------------- | ---------------- | ----------------- | -------------- | ---------- | ----------------- | -------- | ---------- |
|                   |                 |        |             |              |          |                | provide evidence |                   | that adds      | to         | or degrades       | trust.   | Contex-    |
| files of          | the application |        | package     | is computed  |          | and stored on  |                  |                   |                |            |                   |          |            |
|                   |                 |        |             |              |          |                | tual trust       | degradation       | and            | risk-based | escalation        |          | result in  |
| the server.       | Upon            | each   | application | load         | in the   | user’s device, |                  |                   |                |            |                   |          |            |
|                   |                 |        |             |              |          |                | hardware         | challenges        | that           | require    | the participating |          | device     |
| the CRC           | is recomputed   |        | and         | compared     | with the | CRC data       |                  |                   |                |            |                   |          |            |
|                   |                 |        |             |              |          |                | to establish     | a hardware-backed |                |            | cryptographic     | binding. | This       |
| on the            | server to       | ensure | that        | the binaries | have     | not been       |                  |                   |                |            |                   |          |            |
|                   |                 |        |             |              |          |                | adaptive         | device            | authentication |            | protocol          | offers   | resistance |
tamperedwith.
|     |     |     |     |     |     |     | to replay  | and device | impersonation, |       | consistent |         | with NIST |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | -------------- | ----- | ---------- | ------- | --------- |
|     |     |     |     |     |     |     | SP 800-63B | and        | Zero           | Trust | principles | defined | in NIST   |
b: DYNAMICBUILDSECRETINJECTION SP 800-207. Algorithms 16 and 17 describe the proposed
DynamicBuildSecretInjectioncomprisesinjectingarandom AdaptiveDeviceAuthenticationProtocol.
value into the application properties at build time. This With the system definitions described, we move into the
value is stored in the server during the first contact. If an securityguaranteesformalizedbytheZeTHAAframework.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     | 77865 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm13ApplicationIntegrityVerification Algorithm14SecureBuildSecretEmbeddingandVerifica-
| Require: |     | serverKey←HKDF(masterKey,‘‘checksum′′ |     |     |     |     | ▷   | tionProtocol |     |        |     |     |                    |     |     |
| -------- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | --- | ------------------ | --- | --- |
|          |     |                                       |     |     |     |     |     | Require:     |     | κ ←256 |     |     | ▷Securityparameter |     |     |
Keyderivation
|     |        |                 |     |     |     |     |     |     |        | ←HKDF-SHA512(k |     |        | ,’’secret-wrap’’) |     |     |
| --- | ------ | --------------- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | ------ | ----------------- | --- | --- |
|     | appCRC | ←0,fileHashes←∅ |     |     |     |     |     | 1:  | K wrap |                |     | master |                   |     |     |
1:
|     |                         |     |     |                          |     |     |     | 2:  | procedureEmbedSecret(S |         |     | ,build_config) |     |                |     |
| --- | ----------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | ---------------------- | ------- | --- | -------------- | --- | -------------- | --- |
| 2:  | procedure               |     |     | ComputeAndRegisterCheck- |     |     |     |     |                        |         |     | src            |     |                |     |
|     |                         |     |     |                          |     |     |     |     | σ                      | ←PRF(κ) |     |                |     | ▷256-bitsecret |     |
|     | sum(ApplicationPackage) |     |     |                          |     |     |     | 3:  |                        |         |     |                |     |                |     |
|     |                         |     |     |                          |     |     |     |     | σ                      |         |     |                | ,σ) |                |     |
foreachfile∈ApplicationPackageinparalleldo 4: enc ←AES-GCM-SIV(K wrap
3:
|     |     | hash←xxHash64(file.content) |     |     |     |     |     |     | //ObfuscatedInjection |               |     |     |                   |     |     |
| --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --------------------- | ------------- | --- | --- | ----------------- | --- | --- |
| 4:  |     |                             |     |     |     |     |     | 5:  |                       |               |     |     |                   |     |     |
|     |     |                             |     |     |     |     |     |     |                       | ∈MatchFiles(S |     |     | ,*.cpp,py,java)do |     |     |
|     |     | fileHashes.add(hash)        |     |     |     |     |     | 6:  | foreachf              | i             |     | src |                   |     |     |
5:
←appCRC ⊕hash ▷XORchaining 7: InjectAsConst(f ,base64(σ [0:32]))
| 6:  |           | appCRC |                                |     |     |     |     |     |        |                   | i   |           | enc |         |     |
| --- | --------- | ------ | ------------------------------ | --- | --- | --- | --- | --- | ------ | ----------------- | --- | --------- | --- | ------- | --- |
|     |           |        |                                |     |     |     |     |     |        | InjectAsComment(f |     | ,base64(σ |     | [32:])) |     |
| 7:  | endfor    |        |                                |     |     |     |     | 8:  |        |                   |     | i         | enc |         |     |
|     | sealedCRC |        | ←HMAC-SHA256(serverKey,appCRC) |     |     |     |     | 9:  | endfor |                   |     |           |     |         |     |
8:
|     |                                             |     |     |     |                    |     |     | 10: | CompileWithPIE(S               |     |     | ,build_config) |      |      | ▷   |
| --- | ------------------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | ------------------------------ | --- | --- | -------------- | ---- | ---- | --- |
| 9:  | SecureStore(sealedCRC)                      |     |     |     | ▷Encrypteddatabase |     |     |     |                                |     | src |                |      |      |     |
| 10: | endprocedure                                |     |     |     |                    |     |     |     | Position-IndependentExecutable |     |     |                |      |      |     |
|     |                                             |     |     |     |                    |     |     | 11: | StoreSecret(HMAC-SHA256(K      |     |     |                |      | ,σ)) |     |
| 11: | procedureVerifyChecksum(ApplicationPackage) |     |     |     |                    |     |     |     |                                |     |     |                | wrap |      |     |
endprocedure
| 12: | localCRC |     | ←0  |     |     |     |     | 12: |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
foreachfile∈ApplicationPackagedo 13: procedureVerifySecret(B app )
13:
|     |                        |          |     | ←   |     |          | ⊕   | 14: | σ   | ←ExtractFromBinary(B   |     |     | )   |            |     |
| --- | ---------------------- | -------- | --- | --- | --- | -------- | --- | --- | --- | ---------------------- | --- | --- | --- | ---------- | --- |
| 14: |                        | localCRC |     |     |     | localCRC |     |     | ext |                        |     |     | app |            |     |
|     |                        |          |     |     |     |          |     |     | σ   | ←AES-GCM-SIV-Decrypt(K |     |     |     | ,σ         |     |
|     | xxHash64(file.content) |          |     |     |     |          |     | 15: | dec |                        |     |     |     | wrap ext ) |     |
iffile∈/ fileHashesthen ▷Detectnew/deleted 16: seal ←FetchSeal()
| 15: |       |     |     |     |     |     |     |     |                     | server         |     |       |      |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | ------------------- | -------------- | --- | ----- | ---- | --- | --- |
|     |       |     |     |     |     |     |     |     | seal                | ←HMAC-SHA256(K |     |       | ,σ   | )   |     |
|     | files |     |     |     |     |     |     | 17: |                     | local          |     |       | wrap | dec |     |
|     |       |     |     |     |     |     |     |     | if¬SecureEqual(seal |                |     | ,seal |      |     |     |
Reject(‘‘Unauthorizedfilemodification’’) 18: local server )then
16:
|     |              |       |                                  |     |     |     |     | 19: |          | Reject(‘‘Tamperingdetected’’) |     |     |                   |     |     |
| --- | ------------ | ----- | -------------------------------- | --- | --- | --- | --- | --- | -------- | ----------------------------- | --- | --- | ----------------- | --- | --- |
| 17: |              | endif |                                  |     |     |     |     |     |          |                               |     |     |                   |     |     |
|     |              |       |                                  |     |     |     |     |     |          | FireCanaryToken()             |     |     | ▷Triggerdeception |     |     |
| 18: | endfor       |       |                                  |     |     |     |     | 20: |          |                               |     |     |                   |     |     |
|     | receivedSeal |       | ←HMAC-SHA256(serverKey,localCRC) |     |     |     |     |     | measures |                               |     |     |                   |     |     |
19:
else
| 20: | ifreceivedSeal |                                        |     | ̸=SecureFetch()then |     |     |     | 21: |     |               |     |     |     |     |     |
| --- | -------------- | -------------------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
|     |                | RejectAndAudit(‘‘Integrityviolation’’) |     |                     |     |     |     | 22: |     | GrantAccess() |     |     |     |     |     |
21:
|     |     |                |     |     | ▷Securitymonitoring |     |     | 23: | endif |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | ------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
| 22: |     | ReportToSIEM() |     |     |                     |     |     |     |       |     |     |     |     |     |     |
endprocedure
| 23: | endif |     |     |     |     |     |     | 24: |     |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
endprocedure
24:
Algorithm15Anti-TamperingTechniques
|     |                    |     |     |     |     |     |     | 1:  | functionInjectAsConst(file,data) |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
| VI. | SECURITYGUARANTEES |     |     |     |     |     |     | 2:  | varName←RandomIdentifier()       |     |     |     |     |     |     |
This section formalizes the security guarantees provided by InsertCode(file,’’constautovarName = ’’+data+
3:
| theproposedZeTHAAframework.Theguaranteesarestated |     |     |     |     |     |     |     |     | ’’;’’) |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
relative to baseline assumptions and follow directly from InsertDeadCode(file,varName) ▷Control-flow
4:
the models and mechanisms introduced in the preceding obfuscation
| sections. |     |     |     |     |     |     |     | 5:  | endfunction |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
functionExtractFromBinary(binary)
6:
A. IMPOSSIBLETRAVELELIMINATIONGUARANTEE
|           |     |               |     |                     |     |     |        | 7:  | mem←ReadELF/PE/MachO(binary) |     |     |     |         |     |     |
| --------- | --- | ------------- | --- | ------------------- | --- | --- | ------ | --- | ---------------------------- | --- | --- | --- | ------- | --- | --- |
| Guarantee |     | 1 (Impossible |     | State Elimination). |     | The | system |     |                              |     |     |     |         |     |     |
|           |     |               |     |                     |     |     |        |     | FindXORedSegments(mem,K      |     |     |     | [0:16]) |     |     |
|           |     |               |     |                     |     |     |        | 8:  |                              |     |     |     | wrap    |     |     |
guaranteesthatnoauthorizationgrantorsessioncontinuation
|        |       |            |     |              |            |            |     | 9:  | returnReconstructSecret(mem) |     |     |     |     |     |     |
| ------ | ----- | ---------- | --- | ------------ | ---------- | ---------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
| occurs | under | physically |     | or logically | impossible | contextual |     |     |                              |     |     |     |     |     |     |
|        |       |            |     |              |            |            |     | 10: | endfunction                  |     |     |     |     |     |     |
states.Formally,foranytimet,
|     | ImpossibleTravel(t)=1 |     |     |     | ⇒ Grant(t)=0. |     |     |            |     |                         |     |     |          |        |     |
| --- | --------------------- | --- | --- | --- | ------------- | --- | --- | ---------- | --- | ----------------------- | --- | --- | -------- | ------ | --- |
|     |                       |     |     |     |               |     |     | suspicious |     | activity. Specifically, |     | for | any time | window | W   |
Grant(t) ⇐⇒ ¬ImpossibleTravel(t) ∧ AuthValid(S(t)) duringwhichLearn(t)=0forallt ∈W,theprofileremains
invariant:
|     |     |     | ∧ S(m)≥S                     | (C(t)) |     |     |      |     |     |        |      |            |     |     |     |
| --- | --- | --- | ---------------------------- | ------ | --- | --- | ---- | --- | --- | ------ | ---- | ---------- | --- | --- | --- |
|     |     |     |                              | req    |     |     |      |     |     | ∀t ∈W, | Pi(t | +1)=Pi(t). |     |     |     |
|     |     |     | ∧ Pr[AttackSuccess|C(t)]≤δ(R |        |     | ).  | (42) |     |     |        | u    |            | u   |     |     |
s
|     |     |     |     |     |     |     |     | Moreover, |     | when learning |     | is permitted, |     | the maximum |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | ------------- | --- | ----------- | --- |
B. SECURITYGUARANTEE:POISONINGRESISTANCE cumulative influence of any sequence of observations of
Guarantee (Profile Poisoning Resistance). Under the length n is bounded by 1 − (1 − γ)n, ensuring that
learning policy defined in (1)–(2), an adversary cannot no finite sequence of events can rapidly redefine normal
| significantly |     | shift | a behavioral | profile | through | transient | or  | behavior. |     |     |     |     |     |               |     |
| ------------- | --- | ----- | ------------ | ------- | ------- | --------- | --- | --------- | --- | --- | --- | --- | --- | ------------- | --- |
| 77866         |     |       |              |         |         |           |     |           |     |     |     |     |     | VOLUME14,2026 |     |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
Algorithm16AdaptiveDeviceAuthenticationProtocol increases monotonically, implying that additional penalties
1: procedureDeviceAuthentication(C(t),P u ,θ dev ) strictlyincreaseadversarialsuccessprobability. □
2: (cid:49) pen ←0
3: D OS ←ExtractOSAttributes(C(t)) 3) TRUSTDEGRADATIONANDRAPIDLOSSGUARANTEE
4: foralld i ∈D OS do Theorem3(AsymmetricTrustEvolution): Trust accumu-
5: ifMatch(d i ,P u (d i ))=1then lates gradually through positive contextual evidence but
6: Trust(t)←Trust(t)+w i degrades rapidly in the presence of authentication penalties
orattributeviolations.
7: else
8:
(cid:49)
pen
←(cid:49)
pen
+π
i
Proof:Trustiscomputedas:
9: endif Trust(t)=Trust (C(t))− X (cid:53) (t)− X π(t).
attr m i
10: endfor m∈M(t) i
11: if(cid:49) pen ≥θ dev then
Positive evidence contributes additively through weighted
12: D RS ←SelectHWChallengeSet(D HW \D OS )
attributes, while penalties are unbounded in frequency and
13: SendChallenge(D RS )
additive in magnitude, ensuring faster trust decay than
14: BindState(D RS ,C(t)) accumulation. □
15: LearningEnabled(t)←0
16: endif 4) ADAPTIVEENFORCEMENTGUARANTEE
17: endprocedure Theorem4(AdaptiveStep-UpandRevocation): Ifauthen-
tication strength, trust, or acceptable attack risk thresholds
Algorithm17HardwareChallengeVerification are violated at any time, the system enforces step-up
1: procedureVerifyDeviceChallenge(U id ,C(t),D r R e S sp ) authe P n r ti o c o a f t : io A n u , t t h o o k r e i n za r t e i v o o n c i a s ti c o o n n , t o in r u a o cc u e s s ly st e e v r a m lu in a a te ti d on a . gainst
2 3 : : D if s R V t S a e t r e if ← yH R W e P tr r i o e o v f eB (D o r u e n sp d , S D ta s t ta e t ( e U ) i = d ) 1then thresholds S ˆ req , τ grant , and δ grant . Violation of any condition
RS RS triggerspredefinedenforcementactions,ensuringthataccess
4: Trust(t)←Trust(t)+w HW
isnevermaintainedunderinsufficientassuranceorexcessive
5: LearningEnabled(t)←1
risk. □
6: else
7:
Trust(t)←Trust(t)−π
HW 5) END-TO-ENDZEROTRUSTGUARANTEE
8: HardViolation(t)←1 Theorem5(End-to-EndZeroTrustEnforcement): Under
9: LogSecurityEvent(U id ,t) the stated assumptions, the proposed framework ensures
10: endif that no access is granted or retained solely based on
11: endprocedure prior authentication, and that all access decisions are
continuously re-evaluated against current authentication
assurance,contextualtrust,andestimatedattackrisk.
1) AUTHENTICATIONASSURANCEGUARANTEE Proof: Initial access requires satisfaction of authen-
Theorem1(MinimumAuthenticationAssurance): An tication strength, trust, and risk constraints. Continuous
authorization grant is issued only if the effective authen- monitoring updates penalties, trust, and attack probability.
tication strength meets or exceeds the required assurance Anydeviationfromacceptableboundstriggersenforcement
thresholdforthecurrentcontextandresourcesensitivity. perTheorem4.Therefore,trustisneverimplicit,persistent,
Proof: By construction, authorization is granted only orunconditional. □
whenS ˆ (m,t) ≥ S ˆ (C(t),R ),whereS ˆ (m,t) = S ˆ (m)− Havingestablishedthesecurityguarantees,Table8maps
eff req s eff
λ (cid:53) (cid:53) m (t). Since (cid:53) m (t) ≥ 0, penalties can only reduce the 7 NIST Zero Trust tenets to the proposed framework’s
effective strength, ensuring that authentication assurance is securityguarantees.
neveroverestimated. □
6) SCOPEANDLIMITATIONS
The guarantees hold relative to the accuracy of attribute
2) MONOTONICRISKAMPLIFICATIONGUARANTEE
measurements, the correct initialization of authentication
Theorem2(Penalty-InducedRiskMonotonicity): The
strengths, and the timely observation of security outcomes.
probability of a successful authentication attack is a
Compromiseoftheseassumptionsmayreducetheeffective-
monotonicincreasingfunctionofaccumulatedauthentication
ness of enforcement, but does not invalidate the structural
penalties.
guarantees of monotonic risk amplification and adaptive
Proof: The authentication attack probability is defined
control.
as:
Pr(Break(m)|(cid:53) (t))=Pr(Break(m)) (cid:0) 1+η (cid:53) (t) (cid:1), VII. EXPERIMENTALEVALUATION
m m m
A. TESTBEDANDIMPLEMENTATION
with η > 0. Since (cid:53) (t) is non-negative and increasing The evaluation was conducted on a Lenovo IdeaPad run-
m m
under negative events, the conditional break probability ning 12th Gen Intel(R) Core(TM) i5-12450H (2.00 GHz)
VOLUME14,2026 77867

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE8. MappingofsecurityguaranteestoNISTzerotrusttenets.
| TABLE9. | Datasetsummary. |     |     |     |     |     | TABLE10. Attackdistribution. |     |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
[H]
and16GBofRAM,runningWindows11HomeEdition(64-
| bit).ToevaluatetheeffectivenessoftheproposedZeTHAA |     |           |             |       |             |     |     |     |     |     | [H] |     |
| -------------------------------------------------- | --- | --------- | ----------- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| framework,                                         | we  | conducted | experiments | using | a synthetic |     |     |     |     |     |     |     |
authenticationdatasetthatincorporatesrealisticuserbehav-
|         |             |            |     |                         |     |     | a single attack | pattern. | Table | 10 shows | the diversity | and |
| ------- | ----------- | ---------- | --- | ----------------------- | --- | --- | --------------- | -------- | ----- | -------- | ------------- | --- |
| ior and | adversarial | scenarios. | To  | ensure reproducibility, |     | the |                 |          |       |          |               |     |
distributionoftheattacktypesinthedataset.
sourcecode,thebaselineimplementations,andtheevaluation
scriptsareavailableat[61].
|     |     |     |     |     |     |     | B. CONTEXTUALRISKMODELING |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- |
Theproposedframeworkevaluatesauthenticationriskusing
1) DATASETDESCRIPTION
|                |          |               |              |          |                |     | contextual    | signals    | derived   | from device    | characteristics, | net-  |
| -------------- | -------- | ------------- | ------------ | -------- | -------------- | --- | ------------- | ---------- | --------- | -------------- | ---------------- | ----- |
| The dataset    | contains | approximately |              | 50,000   | authentication |     |               |            |           |                |                  |       |
|                |          |               |              |          |                |     | work context, | user       | mobility, | and behavioral | patterns.        | These |
| sessions       | across   | 500 users,    | generating   | close    | to 150,000     |     |               |            |           |                |                  |       |
|                |          |               |              |          |                |     | signals are   | calibrated | using     | evidence–based | weighting        | to    |
| authentication |          | events.       | Each session | includes | contextual     |     |               |            |           |                |                  |       |
estimatetheirrelativecontributiontoauthenticationrisk.
| attributes | such | as device | model, | operating | system | version, |     |     |     |     |     |     |
| ---------- | ---- | --------- | ------ | --------- | ------ | -------- | --- | --- | --- | --- | --- | --- |
geographiclocation,andtemporalloginbehavior.Thedataset
|        |             |          |     |             |       |         | 1) CONTEXTUALSIGNALS |     |     |     |     |     |
| ------ | ----------- | -------- | --- | ----------- | ----- | ------- | -------------------- | --- | --- | --- | --- | --- |
| models | user travel | patterns | and | device life | cycle | events, |                      |     |     |     |     |     |
Keycontextualsignalsinclude:
| such as | new phone | purchases, | operating | system | upgrades, |     |     |     |     |     |     |     |
| ------- | --------- | ---------- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
andapplicationversionupgrades.Approximately70%ofthe • geographicanomalydetection
sessionsrepresentnormaluserbehavior,whiletheremaining • travelstatusandtimezoneshifts
30% model adversarial scenarios. Table 9 summarizes the • devicefingerprintconsistency
• sessiontokenreusepatterns
overalldatasetcharacteristics.
• repeatedattackerIPactivity
2) DATASETPROPERTIES Thesecontextualsignalscaptureidentity,device,network,
Thedatasetmodelsmultipleadversarialscenarios,including temporal,andbehavioralcontext.Therelativeimportanceof
coordinated attack campaigns, credential theft, bot-driven each contextual feature was derived using Bayesian online
login attempts, device spoofing, session hijack, token theft calibrationviaBetaposteriorupdating.Thecalibratedresults
and replay, and application tampering. The attack classes show the probability of an attack given the exposure of the
werebalancedandevenlydistributedtopreventbiastowards attributesignal.
| 77868 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
FIGURE3. Riskscoredistributionbyclass.
| FIGURE2. Featureimportance. |     |     |     | TABLE11. | Decisionrates. |     |     |
| --------------------------- | --- | --- | --- | -------- | -------------- | --- | --- |
2) FEATUREIMPORTANCE
Therelativeimportanceofcontextualfeatures,derivedusing
| Bayesian online | calibration, | is shown | in Fig. 2. Attack |     |     |     |     |
| --------------- | ------------ | -------- | ----------------- | --- | --- | --- | --- |
τ
campaign-related features contribute the highest to risk, lower threshold was set to the 75th percentile of benign
1
followed by geographic anomalies. Device and session traffictominimizeuserfriction.
integrity-related signals, particularly fingerprint mismatch Thethresholdsweresubsequentlyderivedfromthedataset
| andsessioncontextinconsistencies,contributemoderatelyto |     |     |     | as: |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
theriskscore,whiletemporalandtravelanomaliesserveas τ =0.1180,τ =0.1809
|     |     |     |     |     | 1   | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
weakindicators.
2) POLICYDECISIONS
C. RISKSCOREBEHAVIOR Table 11 captures the policy decisions that apply thresholds
| Fig. 3 compares | the distribution | of risk | scores by class | totheevents. |     |     |     |
| --------------- | ---------------- | ------- | --------------- | ------------ | --- | --- | --- |
- benign and attack sessions. The figure shows a clear Thedatashowsthatapproximately75%ofbenignevents
separation between benign and attack events, with attack were allowed without additional verification, while 17.5%
sessionsshowingconsistentlyhigherriskvaluesthanbenign required step-up authentication. Only 7.5% of benign ses-
sessions. The attack classes form two clusters, with the sionswereincorrectlyblocked.Inthecaseofattacksessions,
majority of the sessions in the first cluster showing risk about 73% were immediately blocked, and approximately
scores ranging from 0 to 0.11, indicating stable contextual 9.7%weresubjectedtostep-upverification.Theresultsshow
behavior.Asecondgroupisidentifiedwithriskrangingfrom thattheframeworkbalancessecurityandusability,minimizes
0.12to0.4,indicatinganaturalseparationofriskvalues.This userfriction,andmaintainsattackdetection.
demonstratestheproposedframework’sabilitytodistinguish Fig. 4 shows the policy decisions based on the risk score
| anomalousbehavior.Thedistributionshowsthatthedecision |     |     |     | distribution. |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- |
thresholdscanbeplacedlogically. Thederiveddecisionthresholdsbalancebetweensecurity
andusability.Themajorityofthebenigneventswereallowed
|     |     |     |     | without | friction, while | a controlled percentage | underwent |
| --- | --- | --- | --- | ------- | --------------- | ----------------------- | --------- |
D. DECISIONPOLICYANDDETECTIONPERFORMANCE
1) THRESHOLDSELECTION step-up verification. The framework blocked a significant
|     |     |     |     | proportion | of attack events, | demonstrating | the effectiveness |
| --- | --- | --- | --- | ---------- | ----------------- | ------------- | ----------------- |
Authenticationeventsareclassifiedintothreeregionsbased
ontheircomputedriskscoredecisionthresholds.Eventswith ofarisk-basedpolicy.
| riskscoresbelowthelowerthresholdτ |     |     | areallowedwithout |     |     |     |     |
| --------------------------------- | --- | --- | ----------------- | --- | --- | --- | --- |
1
additional verification, while moderate-risk events trigger E. CLASSIFICATIONPERFORMANCE
step-up authentication until the upper threshold τ . Events To quantify the effectiveness of the proposed ZeTHAA
2
|     |     |     |     | framework, | standard classification | metrics | were computed |
| --- | --- | --- | --- | ---------- | ----------------------- | ------- | ------------- |
exceedingtheupperthresholdareclassifiedhighriskandwill
| resultindenialofaccess. |            |             |                  | usingthecalibratedriskthresholds. |     |     |     |
| ----------------------- | ---------- | ----------- | ---------------- | --------------------------------- | --- | --- | --- |
| The decision            | thresholds | τ and τ are | derived from the |                                   |     |     |     |
1 2
dataset.Theupperthresholdτ
|     |     | 2 iscomputedasthemaximum |     | 1) CONFUSIONMATRIX |     |     |     |
| --- | --- | ------------------------ | --- | ------------------ | --- | --- | --- |
Youden’s value youden = tpr −fpr, where tpr denotes the Table 12 presents the global confusion matrix comparing
truepositiverateandfprrepresentsthefalsepositiverate.The theinputdatasettotheZeTHAAframework’soutput,while
VOLUME14,2026 77869

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
FIGURE4. Policydecisionwithriskscoredistribution. FIGURE6. Risk-trustcorrelation.
TABLE14. Stealthattackmetrics.
TABLE12. Globalconfusionmatrix.
TABLE13. Performancemetrics.
|     |     |     |     | The low-risk | phase            | is represented   | by the region | with risk   |
| --- | --- | --- | --- | ------------ | ---------------- | ---------------- | ------------- | ----------- |
|     |     |     |     | scores less  | than the step-up | threshold.       | While         | this region |
|     |     |     |     | shows a      | high density     | of benign events | as expected,  | it also     |
showsthepresenceofattackevents.Thesubsetofattacksthat
|     |     |     |     | fall in the | low-risk region | can be considered | stealth | attacks, |
| --- | --- | --- | --- | ----------- | --------------- | ----------------- | ------- | -------- |
whereadversarialbehaviordoesnotmanifeststronglyacross
theobservedcontextualsignals.Table14recordsthenumber
ofattackeventsthatwerefoundinthelow-riskzone.
|     |     |     |     | However,      | even in the         | low-risk area,     | malicious       | activities  |
| --- | --- | --- | --- | ------------- | ------------------- | ------------------ | --------------- | ----------- |
|     |     |     |     | were found    | to dominate         | the lower trust    | areas, while    | benign      |
|     |     |     |     | activities    | clustered in        | the higher trust   | region.         | This trend  |
|     |     |     |     | continues     | into the transition | phase between      | the             | thresholds. |
|     |     |     |     | The higher    | risk zone           | (>0.18) represents | a concentration | of          |
|     |     |     |     | attack events | and is also         | characterized      | by a high       | density     |
|     |     |     |     | of events     | with very low       | trust scores.      | The diagonal    | linear      |
trendrepresentsthecorrelationbetweenriskandtrustinthe
framework:astheriskscoreincreases,thetrustscoredeclines
|     |     |     |     | linearly. | This suggests | that risk alone | is not | sufficient to |
| --- | --- | --- | --- | --------- | ------------- | --------------- | ------ | ------------- |
distinguishevents;trustscoresaretheprimarydifferentiator.
|     |     |     |     | Fig. 6 | also closely corresponds | to  | the findings | noted in |
| --- | --- | --- | --- | ------ | ------------------------ | --- | ------------ | -------- |
Table11.
FIGURE5. ROCcurve.
F. DETECTIONLATENCY
|     |     |     |     | An important | requirement | of an adaptive | authentication |     |
| --- | --- | --- | --- | ------------ | ----------- | -------------- | -------------- | --- |
the corresponding performance metrics are summarized in system is its ability to rapidly detect malicious activity.
| Table 13. Fig. | 5 shows | the derived Receiver | Operating |             |              |                   |     |             |
| -------------- | ------- | -------------------- | --------- | ----------- | ------------ | ----------------- | --- | ----------- |
|                |         |                      |           | To evaluate | this aspect, | the delay between | the | onset of an |
Characteristic(ROC)curve. attackandthefirsteventexceedingtheblockthresholdτ was
2
|     |     |     |     | measured. | The detection | latency is | defined as | the number |
| --- | --- | --- | --- | --------- | ------------- | ---------- | ---------- | ---------- |
2) RISK-TRUSTCORRELATIONANDATTACK of events required before the risk score crosses the block
| CLASSIFICATIONPERFORMANCE |     |     |     | thresholdτ | .   |     |     |     |
| ------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
2
Fig.6presentsthecorrelationbetweenriskandtrust,andhow Table15recordsthedetectionperformanceoftheproposed
theframeworkusesthetrustscore,alongwiththecomputed framework. Strong contextual signals, such as Attack cam-
thresholdstoclassifyevents. paignsignatures,devicefingerprintmismatches,andsession
| 77870 |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE15. Detectiondelaybyevents. TABLE16. Userfrictionanalysis.
|     |     |     |     |     |     | FIGURE8. | Costvsattackdetectionrecall. |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ---------------------------- | --- | --- | --- |
FIGURE7. Detectiondelaydistribution.
anduserexperience.Thecostmapusedwas:
| context violations, |            | elevate | the aggregated |        | risk score   | above |     |     |     |     |
| ------------------- | ---------- | ------- | -------------- | ------ | ------------ | ----- | --- | --- | --- | --- |
| the block           | threshold. | The     | framework      | showed | an immediate |       |     |     |     |     |
ALLOW:1,STEPUP:5,BLOCK:10
| detection | rate | of 98.4%, | with a | 95th percentile | delay | of  |     |     |     |     |
| --------- | ---- | --------- | ------ | --------------- | ----- | --- | --- | --- | --- | --- |
0events.Theaveragedelay,intermsofthenumberofevents Table 16 captures the user friction metrics, including the
| was 0.0170. | Fig. | 7 represents | the | distribution | of detection |     |     |     |     |     |
| ----------- | ---- | ------------ | --- | ------------ | ------------ | --- | --- | --- | --- | --- |
costdetails.
delaybyeventsduringtheattackcampaigns. The usability impact analysis of the data showed that
|     |     |     |     |     |     | 73% of genuine | attacks | were blocked | by  | the framework. |
| --- | --- | --- | --- | --- | --- | -------------- | ------- | ------------ | --- | -------------- |
G. USERFRICTIONANALYSIS Approximately 15% of the benign users were challenged to
The usability of the proposed ZeTHAA framework was performadditionalauthentication.About5%ofbenignusers
evaluatedthroughuserfrictionanalysis.Userfrictionanalysis wereblockedfromaccessingresources.
aimstoidentifytherateatwhichbenignusersareforcedto Fig. 8 illustrates the trade-off between authentication
performadditionalauthentication.Whilestep-upauthentica- cost and attack detection rate across varying threshold
tionintroducesmoderatefriction,blockingabenignusercan configurations.Theplottedcurvedepictspossibleoperating
significantlydegradetheuserexperience,includingpotential points of the framework when thresholds are varied. Each
servicedenial.
pointrepresentsauniquethresholdconfiguration,illustrating
Thefrictionmetricswerecomputedas: the relationship between authentication cost and detection
|     |     |     |     |     |     | performance. | As expected, | increasing | the strictness | of deci- |
| --- | --- | --- | --- | --- | --- | ------------ | ------------ | ---------- | -------------- | -------- |
BenignStep-UpEvents
Step-UpRate= sionthresholdsleadstohigherdetectionratesattheexpense
TotalBenignEvents
|     |     |     |     |     |     | of increased | user friction. | The selected |     | operating point |
| --- | --- | --- | --- | --- | --- | ------------ | -------------- | ------------ | --- | --------------- |
BenignBlockEvents (marked with x) achieves a favorable balance, delivering
FalseBlockRate=
|     |     |     |     |     |     | strong detection | performance | while maintaining |     | a moderate |
| --- | --- | --- | --- | --- | --- | ---------------- | ----------- | ----------------- | --- | ---------- |
TotalBenignEvents
authenticationcost.
AttackBlockEvents
AttackBlockRate=
TotalAttackEvents
H. ROBUSTNESSANALYSIS
A non-linear cost model was adopted to reflect the Robustness analysis of the proposed framework aimed at
assessinghowthesystemrespondedtoparameterchanges.
| disproportionate |     | impact  | of user-facing | decisions. | Step-up       |     |     |     |     |     |
| ---------------- | --- | ------- | -------------- | ---------- | ------------- | --- | --- | --- | --- | --- |
| authentication   |     | demands | on benign      | users      | were assigned | a   |     |     |     |     |
moderate cost, while blocking a benign user was assigned 1) ABLATIONSTUDY
asignificantlyhighercostduetouserdisruptionanddenial. As the system validates contextual signals to arrive at
Blockinglegitimateusersispenalizedmoreheavilythanstep- a decision, an ablation study was conducted to measure
up authentication, as it directly impacts service availability how the performance changes when the contextual signals
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     | 77871 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
| are removed. |     | The study | also | aimed | to confirm |     | that each |     |     |     |     |     |     |     |     |
| ------------ | --- | --------- | ---- | ----- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
contextualsignalcontributestothesystem.
| Table            | 17 records |            | how       | the system | responded |            | to the |     |     |     |     |     |     |     |     |
| ---------------- | ---------- | ---------- | --------- | ---------- | --------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| removal          | of each    | contextual |           | signal.    | F1-score  | and        | Area   |     |     |     |     |     |     |     |     |
| Under Curve(AUC) |            |            | were used | as the     | primary   | comparison |        |     |     |     |     |     |     |     |     |
metrics.Thesystemwasunaffectedbytheremovaloftravel,
timezone,andtemporalanomalies.Theremovalofrepeated
| attacker  | IP resulted | in           | the        | largest variation |      | in the         | metrics, |     |     |     |     |     |     |     |     |
| --------- | ----------- | ------------ | ---------- | ----------------- | ---- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| followed  | by          | Geo anomaly. |            | The session       |      | token          | mismatch |     |     |     |     |     |     |     |     |
| showed    | the next    | highest      | variation, | followed          |      | by fingerprint |          |     |     |     |     |     |     |     |     |
| mismatch. | The         | observations |            | matched           | with | the contextual |          |     |     |     |     |     |     |     |     |
featureimportancecomputedinFig.2.
Afurtherstudywasconductedbyremovinggroupsignals,
inwhichallcontextualsignalsrelatedtoaspecificcontextual
| group were | removed. |     | Table | 18 presents |                  | the observations |       |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----- | ----------- | ---------------- | ---------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| from the   | removal  | of  | group | signals.    | The observations |                  | align |     |     |     |     |     |     |     |     |
withresultsfromtheremovalofsingularcontextualsignals, FIGURE9. ROCcomparisonacrossmodels.
withtheattackcampaign-relatedgroupshowingthehighest
impactonF1andAUC,followedbymobility,whichgroups
geo-anomaly-related signals. The session group showed 2) DETECTIONPERFORMANCE
the next highest impact, followed by temporal and device The performance of the proposed framework and baseline
integrity. modelswasevaluatedusingseveralcommonlyusedsecurity
metrics.Allmodelcomparisonswereperformedonatestset
toensurefairandunbiasedevaluation.
2) ATTACKINTENSITYANALYSIS
Table21showstheperformancemetricsobservedcompar-
| The performance |     | of  | the framework | under | increasing |     | attack |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | ------------- | ----- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ingtheZeTHAAframeworkagainstbaselines.Thesimilarity
| intensities    | was | studied    | to understand |     | its response |     | to coordi- |                |     |         |        |        |     |         |     |
| -------------- | --- | ---------- | ------------- | --- | ------------ | --- | ---------- | -------------- | --- | ------- | ------ | ------ | --- | ------- | --- |
|                |     |            |               |     |              |     |            | in performance |     | between | Random | Forest | and | XGBoost | is  |
| nated attacks. |     | This study | exposed       | the | framework    |     | to attack  |                |     |         |        |        |     |         |     |
intensitiesvaryingfrom10%to40%,simulatingcoordinated attributedtothelimitedfeaturespaceandthedominanceof
|                    |     |       |     |          |              |     |          | a few contextual |     | signals, | leading | to both | models | learning |     |
| ------------------ | --- | ----- | --- | -------- | ------------ | --- | -------- | ---------------- | --- | -------- | ------- | ------- | ------ | -------- | --- |
| attack conditions. |     | Table | 19  | presents | the findings |     | from the |                  |     |          |         |         |        |          |     |
identicaldecisionstructures.
study.
|       |          |           |        |              |     |        |         | The ZeTHAA      |     | framework | outperformed |             | other    | classifica- |       |
| ----- | -------- | --------- | ------ | ------------ | --- | ------ | ------- | --------------- | --- | --------- | ------------ | ----------- | -------- | ----------- | ----- |
| The   | proposed | framework |        | demonstrated |     | robust | perfor- |                 |     |           |              |             |          |             |       |
|       |          |           |        |              |     |        |         | tion algorithms |     | across    | most         | performance | metrics. |             | While |
| mance | under    | varying   | attack | intensities. | The | AUC    | value   |                 |     |           |              |             |          |             |       |
remains stable, showing that the framework is robust under Random Forest and XGBoost showed a marginal increase
|     |     |     |     |     |     |     |     | in precision, | ZeTHAA |     | showed | better results |     | recall and | F1- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | --- | ------ | -------------- | --- | ---------- | --- |
attackandcandistinguishbetweenattackandbenignevents,
|     |     |     |     |     |     |     |     | score respectively. |     | The | ZeTHAA | Framework |     | significantly |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------ | --------- | --- | ------------- | --- |
evenastheproportionofattacksincreases.Therecallvalue
|     |     |     |     |     |     |     |     | outperforms | every | other | model | in Recall, | notably | beating |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ----- | ----- | ---------- | ------- | ------- | --- |
alsoremainsstabilewithincreasingattackdensity,indicating
|     |     |     |     |     |     |     |     | the Isolation | Forest | by  | over 251%. | As  | the Recall | is higher, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | --- | ---------- | --- | ---------- | ---------- | --- |
thattheattackdetectioncapabilityisconsistent.Theprecision
improves, indicating the system becomes more efficient as the overall F1-Score (the balance of Precision and Recall)
showsamassivejumpof48%to147%overthecomparison.
| attacks | increase. | The | accuracy | shows | slight | degradation | but |     |     |     |     |     |     |     |     |
| ------- | --------- | --- | -------- | ----- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TheLogisticRegressionandHeuristicapproachesperformed
remainsstableoverall.
The results highlight that the proposed framework main- better than Isolation Forest, which offered the lowest
performancemetricsamongalltheapproaches.
tainsstabledetectionperformance,whileadaptingefficiently
Fig.9recordstheROCcurveoftheZeTHAAframework
toincreasingcomplexattackscenarios.
|     |     |     |     |     |     |     |     | compared | to the | baseline | models. | The | proposed | framework |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | -------- | ------- | --- | -------- | --------- | --- |
recordsahightruepositiveratecomparedtotheothermodels.
I. COMPARISONWITHBASELINEMODELS
|            |     |               |     |        |          |     |        | The computed      |     | decision | thresholds         | are | highlighted | on     | the   |
| ---------- | --- | ------------- | --- | ------ | -------- | --- | ------ | ----------------- | --- | -------- | ------------------ | --- | ----------- | ------ | ----- |
| To compare | the | effectiveness |     | of the | proposed |     | ZeTHAA |                   |     |          |                    |     |             |        |       |
|            |     |               |     |        |          |     |        | curve, indicating |     | the      | policy’s operating |     | region.     | At the | step- |
framework,itsperformancewascomparedwithmultiplerep- up decision threshold (τ ) indicated by the blue marker, the
1
resentativeauthenticationandanomalydetectionapproaches
|     |     |     |     |     |     |     |     | framework | detects | 83.2% | of  | attack events | and | challenges |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ----- | --- | ------------- | --- | ---------- | --- |
commonlyusedinrisk-basedauthenticationsystems.
|     |     |     |     |     |     |     |     | with step-up | verification, |     | while         | incurring | a     | false positive |       |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ------------- | --------- | ----- | -------------- | ----- |
|     |     |     |     |     |     |     |     | rate of      | 24.7%.        | The | True Positive | Rate      | (TPR) | and            | False |
1) BASELINEMODELS Positive Rate (FPR) represent aggressive detection, but use
Theselectedbaselinemethodsrepresentdifferentcategories step-upauthenticationanddonotblockusers.Theredmarker
ofauthenticationmodels.Table20liststhebaselinemodels indicates the operating point corresponding to the blocking
against which the proposed framework is assessed for threshold (τ ), achieving 73.2% attack detection with a
2
performance. 7.24% false positive rate, showcasing strict security while
| 77872 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE17. Singlesignalablationresults.
TABLE18. Groupsignalablationresults.
TABLE19. Attackintensityanalysis.
TABLE20. Selectedbaselinesforcomparison.
TABLE21. Performancecomparisonbetweenbaselines.
minimizinguserdisruption.Theshadedportionbetweenthe showed a lower range of step-up challenges and block
policy thresholds represents the adaptive decision region of decisions, indicating a conservative approach to security.
the framework. The sharp rise of the proposed framework’s Unliketraditionalclassifiersthatoperateatasinglethreshold,
ROC curve near the origin indicates early-stage discrimina- the ZeTHAA framework defines a controllable decision
tioncapability,whichhelpsinminimizinguserfrictionwhile band,enablingresponsesbasedonrisklevelsandimproving
maintaininghighdetectionrates. detection performance. The ZeTHAA framework produces
Fig. 10 records the policy decisions taken by the models. a well-spread risk distribution, enabling effective utilization
The ZeTHAA framework balances security and usability of allow, step-up, and block regions. In contrast, baseline
compared to the baseline models. Although it showed a models exhibit clustered score distributions. This supports
lower‘‘ALLOW’’stateforevents,ithadahigherproportion RQ3 and H3, demonstrating improved alignment between
of step-up challenges than the baselines. This shows that risk scores and decision policies. With a more effective use
events with higher risk scores were automatically asked of the intermediate step-up region, the framework further
to perform additional verification. The baseline models supportsRQ2andH2.
VOLUME14,2026 77873

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
|     |     |     |     |     |     |     | The proposed          |               | framework     | achieves         | the            | lowest     | cost per    |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | ------------- | ------------- | ---------------- | -------------- | ---------- | ----------- |
|     |     |     |     |     |     |     | detected              | attack        | among         | all models.      | This           | indicates  | that        |
|     |     |     |     |     |     |     | although              | the framework |               | incurs higher    | overall        | costs,     | it uses     |
|     |     |     |     |     |     |     | authentication        | resources     |               | more efficiently |                | to detect  | attacks.    |
|     |     |     |     |     |     |     | Baseline              | models        | exhibit       | a lower          | average        | cost but   | a higher    |
|     |     |     |     |     |     |     | cost per              | detected      | attack,       | reflecting       | inefficient    |            | security    |
|     |     |     |     |     |     |     | performance.          | The           | proposed      | ZeTHAA           | framework      |            | achieves    |
|     |     |     |     |     |     |     | a higher              | detection     | efficiency,   | indicating       |                | a more     | effective   |
|     |     |     |     |     |     |     | use of authentication |               | resources.    |                  | The controlled |            | increase in |
|     |     |     |     |     |     |     | intervention,         | with          | significantly | improved         |                | detection, | further     |
demonstratessupportofRQ1andH1.
J. COMPARISONWITHEXISTINGFRAMEWORKS
WiththeZeTHAAframeworkexhibitingbetterperformance
| FIGURE10. | Proportionofdecisionsperpolicyregion. |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
metrics,operationalefficiency,andcosteffectivenessagainst
baselinemodels,wefurthercompareZeTHAAwithmethod-
3) OPERATIONALEFFICIENCYANDCOSTPERATTACK ologies presented in the existing literature. Comparison
The operational efficiency of the proposed framework was studieswereperformedwithDasuetal.[16]andMatiushin
|     |     |     |     |     |     |     | and Korkhov | [19]. | Dasu | et al. | use a | weighted | heuristic |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---- | ------ | ----- | -------- | --------- |
verifiedagainstthebaselinemodels.
Table 22 reports the operational efficiency metrics for the approach to derive risk scores and make decisions. On the
ZeTHAA framework compared with the baseline models. other hand, Matiushin et al. use an ML-based approach to
The proposed ZeTHAA framework records the highest identify anomalies in user behavior and classify requests as
step-upandblockratesamongthemodels,exceeding47.9% an attack or benign. As representatives of two widely used
|           |               |     |          |     |             |        | approaches | to risk | classification |     | - heuristic | and | ML-based, |
| --------- | ------------- | --- | -------- | --- | ----------- | ------ | ---------- | ------- | -------------- | --- | ----------- | --- | --------- |
| and 59.9% | respectively. |     | However, | in  | the context | of the |            |         |                |     |             |     |           |
higher recall value, indicating higher attack detection, the theseworkswerechosenforthecomparisonstudy.
higherstep-upandblockratescanbecorrelatedtoincreased
intervention.Thebaselinemodelsincurlowercostsbecause 1) DASUETAL
they fail to identify and act on a large proportion of Dasu et al. utilize five risk signals - travel risk(r ), location
1
attack events. The proposed framework maintains a higher risk(r 2 ), browser risk(r 3 ), device risk(r 4 ), and password
Efficiency(+20%to+65%)butincursahigherFalseBlock risk(r ). The risk score for each signal is bounded as {x ∈
5
Rate than Random Forest and XGBoost, suggesting a more R|0 ≤ x ≤ 5}. Each risk signal is assigned a static weight
aggressiveyethighlyeffectivedetectionposture. thatrepresentsitsrelativeimportanceinheuristicscoring.
| The analysis | used     | a non-linear |           | cost | model,   | as adopted |                  |     |           |     |     |     |     |
| ------------ | -------- | ------------ | --------- | ---- | -------- | ---------- | ---------------- | --- | --------- | --- | --- | --- | --- |
|              |          |              |           |      |          |            | • TravelRisk(w   |     | 1 )-80/33 |     |     |     |     |
| earlier in   | the user | friction     | analysis. | The  | cost map | used was   |                  |     |           |     |     |     |     |
|              |          |              |           |      |          |            | • LocationRisk(w |     | )-40/33   |     |     |     |     |
|              | 1,Stepup | 5,Block      |           |      |          |            |                  |     | 2         |     |     |     |     |
{Allow : : : 10}, indicating the cost of BrowserRisk(w )-20/33
|     |     |     |     |     |     |     | •   |     | 3   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
askingabenignuserforastep-upchallengeorblockinghim
|                      |     |     |     |     |     |     | • DeviceRisk(w   |     | 4 )-20/33 |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | --- | --- | --- | --- |
| fromusingtheservice. |     |     |     |     |     |     | • PasswordRisk(w |     | )-5/33    |     |     |     |     |
5
| Detection | efficiency | is  | defined | as the | ratio of | the Attack |        |         |          |             |         |          |     |
| --------- | ---------- | --- | ------- | ------ | -------- | ---------- | ------ | ------- | -------- | ----------- | ------- | -------- | --- |
|           |            |     |         |        |          |            | Travel | risk is | assigned | the highest | weight, | followed | by  |
detectionrate(Recall)totheAveragecostofauthentication.
location,browser,anddevicerisk,withpasswordriskbeing
assignedtheleastweight.Thetotalriskisthencomputedas:
Attackdetectionrate(Recall)
Efficiency=
Averageauthenticationcost TotalRisk=(w 1 r 1 +w 2 r 2 +w 3 r 3 +w 4 r 4 +w 5 r 5 )
| The models | were | further | compared |     | in terms | of their |     |     |     |     |     |     |     |
| ---------- | ---- | ------- | -------- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
Theweightsareassignedstatically,andtheframeworkdoes
averagecost,costperattackdetected,andhigherefficiency. not propose an approach to recalibrate them or the binary
| We define | the cost | per detected |     | attack | as the ratio | of the |     |     |     |     |     |     |     |
| --------- | -------- | ------------ | --- | ------ | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
decisionthreshold.Riskscoresthatexceedthethresholdare
averageauthenticationcosttotheattackdetectionrate.
subjectedtovalidation.However,theriskanalysisconsiders
|     |     |     |     |     |     |     | only the | last 10 | login attempts, | thereby | excluding |     | historical |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------------- | ------- | --------- | --- | ---------- |
Averageauthenticationcost
Costperattackdetected=
patterns.
Attackdetectionrate(Recall)
|     |     |     |     |     |     |     | To compare |     | the ZeTHAA | framework |     | with Dasu | et al., |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --------- | --- | --------- | ------- |
Althoughtheaveragecostpertransactionishigher,the‘‘Cost wefirstmaptheriskstotheproposedrisksignals.Table23
perattackdetected’’issignificantlylower,indicatinga17.3% presents the mapping of risks from Dasu et al. to ZeTHAA
to39.6%reductionincostcomparedwiththeothermodels. framework’srisksignals.
However, this increased cost is offset by improved attack In the absence of separate browser or device features,
detection performance. The cost vs. recall and detection fingerprintmismatchisusedasaproxyforboth.Thebrowser
efficiencyobservationssupportRQ1andH1,respectively. signalisapproximatedusingadevicefingerprintmismatch,
| 77874 |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE22. Operationalefficiencyandcost/attackdetected.
TABLE23. Risktosignalmapping. TABLE24. Performancemetricscomparison.
byMLE-RBA.Dasuetal.presentedtheloweststep-uprate,
|                |            |     |                  |     |                  |     | indicating      | that a | higher | number  | of requests  |       | were classified |
| -------------- | ---------- | --- | ---------------- | --- | ---------------- | --- | --------------- | ------ | ------ | ------- | ------------ | ----- | --------------- |
|                |            |     |                  |     |                  |     | as benign.      | ZeTHAA |        | had the | highest      | block | rate among      |
| which captures | deviations |     | in client-device |     | characteristics. |     |                 |        |        |         |              |       |                 |
|                |            |     |                  |     |                  |     | the frameworks, |        | while  | MLE-RBA | demonstrated |       | the lowest      |
While the dataset does not explicitly distinguish between falseblockrates,followedbyZeTHAA.However,ZeTHAA
browser and device features, fingerprint-based signals pro- exhibited the highest efficiency figures while recording the
videareasonableapproximationofboth. lowest cost per correctly detected attack. The proposed
|     |     |     |     |     |     |     | framework | achieves | higher | recall | at  | comparable | cost levels, |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------ | ------ | --- | ---------- | ------------ |
2) MATIUSHINETAL demonstrating a more favorable security–usability balance
TheMachineLearning-EmpoweredRisk-BasedAuthentica- andsupportingRQ1andH1.
| tion (MLE-RBA) |     | framework | proposed | by  | Matiushin | et al., |     |     |     |     |     |     |     |
| -------------- | --- | --------- | -------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
usesamulti-stageMLpipelinetoidentifyirregularitiesand b: SECURITYPOSTUREANDATTACKDETECTION
makedynamicdecisions.ItcombinestwounsupervisedML Table 26 lists the combined confusion matrix of the three
| models: Local | Outlier | Factor | (LOF) | and Isolation |     | Forest to | frameworks. |     |     |     |     |     |     |
| ------------- | ------- | ------ | ----- | ------------- | --- | --------- | ----------- | --- | --- | --- | --- | --- | --- |
capturebothlocalandglobaldeviationsinauser’sbehavior, The Proposed ZeTHAA Framework blocks significantly
generatinganaggregateanomalyscore.Thisanomalyscoreis
|     |     |     |     |     |     |     | more attacks | (7,963) | than | both | the | heuristic | (Dasu et al.) |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ---- | ---- | --- | --------- | ------------- |
fedintoaLightGBMclassifiertogenerateacontinuousrisk (3,630) and MLE-RBA (3,695). ZeTHAA is much more
score for every login attempt. Instead of relying on a static, aggressive with ‘‘Step-Up’’ challenges for benign users
| predefined | threshold, | MLE-RBA | dynamically |     | calculates | an  |              |      |        |        |       |             |          |
| ---------- | ---------- | ------- | ----------- | --- | ---------- | --- | ------------ | ---- | ------ | ------ | ----- | ----------- | -------- |
|            |            |         |             |     |            |     | (4,184) than | Dasu | et al. | (240), | which | corresponds | with the |
optimal threshold by evaluating the Receiver Operating higher recall noted in Table 24. ZeTHAA also allows the
| Characteristic | (ROC) | curve. | If a login’s | risk | score | exceeds |     |     |     |     |     |     |     |
| -------------- | ----- | ------ | ------------ | ---- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
fewestattacks(1,826)throughthesystem,whereastheothers
thisthreshold,thesystemclassifiesitasanattackandtriggers allow over 5,000. MLE-RBA has the lowest FPR (1.95%),
secondaryauthentication. indicating it rarely interrupts legitimate users. However,
asobservedfromtheRecallvalue,itmisses66%ofattacks
3) RESULTSANDOBSERVATIONS toachievethis.ZeTHAAblocked5%morebenignusersthan
Allthreeframeworksweresubjectedtothesamedatasetand
MLE-RBA,butinexchange,caughtnearly40%moreattacks.
| cost mapping.      | The | comparisons | were | conducted |     | under the |                   |          |     |            |     |           |             |
| ------------------ | --- | ----------- | ---- | --------- | --- | --------- | ----------------- | -------- | --- | ---------- | --- | --------- | ----------- |
| broadcategoriesof: |     |             |      |           |     |           | c: ERRORREDUCTION |          |     |            |     |           |             |
|                    |     |             |      |           |     |           | We further        | compared | the | frameworks |     | for their | Equal Error |
a: PERFORMANCEANALYSIS Rate(EER).EERrepresentsthepointonaROCcurve,where
Table 24 records the performance metrics recorded by the theFalsePositiveRate(benignusersincorrectlyblocked)and
threeframeworks.TheproposedZeTHAAframeworkexhib- False Rejection Rate are equal. A lower EER represents a
ited demonstrably higher performance indicators compared betterbalancebetweenfalseacceptsandrejects,showcasing
toDasuetal.andMLE-RBA.WhileMLE-RBApresenteda theabilitytodetectattackswhilemakingfewermistakeson
slightlyhigherprecision,indicatingaccuracyintruepositive identifyinglegitimateusers.
prediction,ZeTHAAwasclosebehindandfaredmuchbetter Fig. 11 presents the ROC curves and corresponding
thanDasuetal.ZeTHAApresentedahigherrecall,indicating EER points for the ZeTHAA, heuristic-based Dasu et al.,
anedgeincorrectlyclassifyingrequests. and ML-based MLE-RBA frameworks. The EER point
Table25presentstheoperationalefficiencyfiguresforthe in the plot represents the balanced operating point at
threeframeworks.TheZeTHAAframeworkpresentsahigher which false positives equal the missed attacks. The pro-
step-up rate due to an active engagement policy, followed posed framework consistently achieves a higher TPR at
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     | 77875 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
TABLE25. Operationalefficiencycomparison.
TABLE26. Combinedconfusionmatrix.
|     |     |     |     |     |     |     | entropy | and Bayesian-driven |     | parameterization |          |           | of attribute |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------- | --- | ---------------- | -------- | --------- | ------------ |
|     |     |     |     |     |     |     | weights | and penalties       |     | provides         | a robust | mechanism | for          |
cold-startinitializationandcontinuousrecalibration,address-
|     |     |     |     |     |     |     | ing one   | of the         | key limitations |          | in existing     | systems.   | The          |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --------------- | -------- | --------------- | ---------- | ------------ |
|     |     |     |     |     |     |     | framework | further        | establishes     |          | a clear         | separation | between      |
|     |     |     |     |     |     |     | intrinsic | authentication |                 | strength | and operational |            | reliability, |
enablingconsistentmappingtoNISTassurancelevels.With
evidence-drivendecisionthresholds,theframeworkcancap-
tureadversarialbehaviors,suchascredentialstuffing,while
|           |                        |     |     |     |     |     | tolerating         | benign     | user error. | The      | paper           | highlights | how the     |
| --------- | ---------------------- | --- | --- | --- | --- | --- | ------------------ | ---------- | ----------- | -------- | --------------- | ---------- | ----------- |
|           |                        |     |     |     |     |     | proposed           | system     | extends     | security | and risk        | assessment | well        |
|           |                        |     |     |     |     |     | into the           | resource   | access      | phase,   | a functionality |            | not covered |
|           |                        |     |     |     |     |     | under conventional |            | AA          | systems. | The proposed    |            | multiphase  |
|           |                        |     |     |     |     |     | hybrid             | evaluation | strategy    | ensures  | that            | the        | system can  |
| FIGURE11. | ROCcurvewithEERpoints. |     |     |     |     |     |                    |            |             |          |                 |            |             |
validateriskandtrustevenintheabsenceofhistoricalcontext
|         |                 |          |     |                |     |             | or access     | patterns. | The           | efficacy | of the    | proposed | system     |
| ------- | --------------- | -------- | --- | -------------- | --- | ----------- | ------------- | --------- | ------------- | -------- | --------- | -------- | ---------- |
|         |                 |          |     |                |     |             | was validated | on        | a large-scale |          | synthetic | dataset  | simulating |
| a lower | FPR, indicating | superior |     | discrimination |     | capability. |               |           |               |          |           |          |            |
The proposed model achieves the lowest EER (0.1981), real-world attack conditions. With novel security checks
significantly outperforming both the heuristic (0.2992) and extending to newer attributes,e.g., application integrity and
|          |            |           |            |     |     |         | dynamic | build | secrets, | and device | posture | evaluation, | the |
| -------- | ---------- | --------- | ---------- | --- | --- | ------- | ------- | ----- | -------- | ---------- | ------- | ----------- | --- |
| ML-based | approaches | (0.2729), | supporting |     | RQ2 | and H2, |         |       |          |            |         |             |     |
which hypothesize improved detection performance and proposed system minimizes user friction and ensures the
|         |                   |        |     |          |               |     | user obtains | only | the minimum |     | degree | of trust | required to |
| ------- | ----------------- | ------ | --- | -------- | ------------- | --- | ------------ | ---- | ----------- | --- | ------ | -------- | ----------- |
| reduced | error trade-offs. | ZeTHAA |     | reported | approximately |     |              |      |             |     |        |          |             |
33%reductioninerrorcomparedtoDasuetal. accesstheintendedresources.TheproposedZeTHAAframe-
The observations show that the proposed framework work provides a coherent, mathematically grounded, and
practicallyimplementableapproachtoZT-basedcontinuous
| provides | a more | favorable | balance | between | false | positives |     |     |     |     |     |     |     |
| -------- | ------ | --------- | ------- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
and false negatives, improving both security and usability, authenticationandauthorization.
| while achieving      |     | higher performance, |     | greater | efficiency, | and |              |     |     |     |     |     |     |
| -------------------- | --- | ------------------- | --- | ------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
| loweroperatingcosts. |     |                     |     |         |             |     | DECLARATIONS |     |     |     |     |     |     |
CONFLICTSOFINTEREST
| VIII. CONCLUSION  |                |            |     |              |        |             | Theauthorsdeclarenoconflictsofinterest. |     |     |     |     |     |     |
| ----------------- | -------------- | ---------- | --- | ------------ | ------ | ----------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
| Adaptive          | authentication | represents |     | an evolution |        | in security |                                         |     |     |     |     |     |     |
| while maintaining |                | usability  | as  | a central    | design | factor.     | REFERENCES                              |     |     |     |     |     |     |
This paper presents ZeTHAA, a novel, unified, and for- [1] C.JacommeandS.Kremer,‘‘Anextensiveformalanalysisofmulti-factor
mally grounded Zero-Trust-based Adaptive Authentication authentication protocols,’’ ACM Trans. Privacy Secur., vol. 24, no. 2,
pp.1–34,Jan.2021,doi:10.1145/3440712.
| and continuous |     | authorization | framework. |     | By  | integrating |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | ---------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
[2] S.S.U.Hasan,A.Ghani,A.Daud,H.Akbar,andM.F.Khan,‘‘Areviewon
authentication strength, contextual attributes, behavioral secureauthenticationmechanismsformobilesecurity,’’Sensors,vol.25,
no.3,p.700,Jan.2025,doi:10.3390/s25030700.
evidence,andretrydynamicsintoatime-dependenttrust–risk
[3] A.Agarwal,S.B.Verma,andB.K.Gupta,‘‘Areviewofcloudsecurity
| model, | the proposed | approach |     | moves | beyond | heuristic |     |     |     |     |     |     |     |
| ------ | ------------ | -------- | --- | ----- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
issuesandchallenges,’’ADCAIJ,Adv.Distrib.Comput.Artif.Intell.J.,
| scoring | systems. | A central | contribution |     | is the | introduction |     |     |     |     |     |     |     |
| ------- | -------- | --------- | ------------ | --- | ------ | ------------ | --- | --- | --- | --- | --- | --- | --- |
vol.12,Dec.2023,Art.no.e31459,doi:10.14201/adcaij.31459.
of a global admissibility predicate, which distinguishes [4] Y. Chen, Y. Yu, and L. Zhai, ‘‘Infinitygauntlet: Brute-force attack on
|                 |     |                 |     |      |               |      | smartphone | fingerprint | authentication,’’ |     | in Proc. | 32nd | USENIX Conf. |
| --------------- | --- | --------------- | --- | ---- | ------------- | ---- | ---------- | ----------- | ----------------- | --- | -------- | ---- | ------------ |
| non-compensable |     | hard violations |     | from | probabilistic | soft |            |             |                   |     |          |      |              |
Secur.Symp.,2023,pp.2027–2041.[Online].Available:https://dl.acm.
signals, thereby enabling clear enforcement decisions. The org/doi/10.5555/3620237.3620351
| 77876 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
[5] Q. Wang and D. Wang, ‘‘Understanding failures in security proofs of [24] A. A. Megahed, M. F. Arnous, Y. Elmoataz, A. Moussa, S. Haitham,
multi-factorauthenticationformobiledevices,’’IEEETrans.Inf.Forensics andM.Hany,‘‘Enhancedsecuritythroughintelligentrisk-basedauthen-
Security,vol.18,pp.597–612,2023,doi:10.1109/TIFS.2022.3227753. tication: Leveraging big data and machine learning for real-time threat
[6] D. Wang, X. Zhang, Z. Zhang, and P. Wang, ‘‘Understanding security mitigation,’’inProc.6thNovelIntell.Lead.Emerg.Sci.Conf.(NILES),
failures of multi-factor authentication schemes for multi-server envi- Oct.2024,pp.246–249.
ronments,’’ Comput. Secur., vol. 88, Jan. 2020, Art.no.101619, doi: [25] M. Al-Zubaidie, Z. Zhang, and J. Zhang, ‘‘RAMHU: A new robust
10.1016/j.cose.2019.101619.
lightweightschemeformutualusersauthenticationinhealthcareapplica-
[7] M. Syahreen, N. Hafizah, N. Maarop, and M. Maslinan, ‘‘A sys- tions,’’Secur.Commun.Netw.,vol.2019,pp.1–26,Mar.2019.[Online].
tematic review on multi-factor authentication framework,’’ Int. J. Available:https://onlinelibrary.wiley.com/doi/abs/10.1155/2019/3263902
Adv. Comput. Sci. Appl., vol. 15, no. 5, pp. 1043–1050, 2024, doi: [26] A.Acar,H.Aksu,A.S.Uluagac,andK.Akkaya,‘‘Ausableandrobust
10.14569/ijacsa.2024.01505105. continuous authentication framework using wearables,’’ IEEE Trans.
[8] E. B. Blancaflor, J. O. Duldulao, J. V. E. Espeño, G. S. M. Patag, MobileComput.,vol.20,no.6,pp.2140–2153,Jun.2021.
M.T.Menor,andG.L.Intal,‘‘Advancedphishingtechniques:Analyzing [27] A. Buriro, S. Gupta, A. Yautsiukhin, and B. Crispo, ‘‘Risk-driven
| adversary-in-the-middle |     |     | and browser-in-the-browser |     |     | attacks | in modern |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | -------------------------- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
behavioralbiometric-basedone-shot-cum-continuoususerauthentication
cybersecurity,’’Cybern.Inf.Technol.,vol.25,no.1,pp.55–77,Mar.2025,
scheme,’’J.SignalProcess.Syst.,vol.93,no.9,pp.989–1006,Sep.2021,
| doi:10.2478/cait-2025-0004. |     |     |     |     |     |     |     | doi:10.1007/s11265-021-01654-2. |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[9] A.F.BaigandS.Eskeland,‘‘Security,privacy,andusabilityincontinuous [28] Z. Shen, S. Li, X. Zhao, and J. Zou, ‘‘MMAuth: A continuous
authentication:Asurvey,’’Sensors,vol.21,no.17,p.5967,Sep.2021,doi: authentication framework on smartphones using multiple modalities,’’
10.3390/s21175967. IEEETrans.Inf.ForensicsSecurity,vol.17,pp.1450–1465,2022,doi:
[10] F.Al-Husari,O.Nakov,andP.Nakov,‘‘Multi-factorauthenticationfatigue: 10.1109/TIFS.2022.3160361.
Agrowingconcerninuserexperienceandsecurity,’’inProc.60thInt.Sci.
|     |     |     |     |     |     |     |     | [29] Y. Liang, | S.  | Samtani, B. | Guo, and | Z. Yu, | ‘‘Behavioral | biometrics | for |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----------- | -------- | ------ | ------------ | ---------- | --- |
Conf.Inf.,Commun.EnergySyst.Technol.(ICEST),Jun.2025,pp.1–4,
|     |     |     |     |     |     |     |     | continuous | authentication |     | in the | Internet-of-Things |     | era: An artificial |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------ | ------------------ | --- | ------------------ | --- |
doi:10.1109/ICEST66328.2025.11098219. intelligence perspective,’’ IEEE Internet Things J., vol. 7, no. 9,
[11] S. Wiefling, M. Dürmuth, and L. Lo Iacono, ‘‘More than just good pp.9128–9143,Sep.2020,doi:10.1109/JIOT.2020.3004077.
passwords?Astudyonusabilityandsecurityperceptionsofrisk-based [30] M.Mekni,E.O.Ogunwobi,andS.C.Russell,‘‘Context-adaptivegait
authentication,’’inProc.Annu.Comput.Secur.Appl.Conf.,Dec.2020, biometrics for real-time continuous authentication,’’ in Proc. Int. Conf.
pp.203–218,doi:10.1145/3427228.3427243.
Adv.Mach.Learn.DataSci.(AMLDS),Jul.2025,pp.799–807.
| [12] A. Hassan,   | B.  | Nuseibeh, | and L.    | Pasquale, | ‘‘Engineering |         | adaptive |                                                              |             |            |     |                  |                |     |       |
| ----------------- | --- | --------- | --------- | --------- | ------------- | ------- | -------- | ------------------------------------------------------------ | ----------- | ---------- | --- | ---------------- | -------------- | --- | ----- |
|                   |     |           |           |           |               |         |          | [31] S.W.Shah,N.F.Syed,A.Shaghaghi,A.Anwar,Z.Baig,andR.Doss, |             |            |     |                  |                |     |       |
| authentication,’’ |     | in Proc.  | IEEE Int. | Conf.     | Autonomic     | Comput. | Self-    |                                                              |             |            |     |                  |                |     |       |
|                   |     |           |           |           |               |         |          | ‘‘LCDA:                                                      | Lightweight | continuous |     | device-to-device | authentication |     | for a |
OrganizingSyst.Companion(ACSOS-C),Sep.2021,pp.275–280,doi:
|     |     |     |     |     |     |     |     | zero | trust architecture | (ZTA),’’ | Comput. | Secur., | vol. | 108, Sep. | 2021, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------ | -------- | ------- | ------- | ---- | --------- | ----- |
10.1109/ACSOS-C52956.2021.00068.
Art.no.102351,doi:10.1016/j.cose.2021.102351.
| [13] S. Rose, | O. Borchert, |     | S. Mitchell, | and | S. Connelly, | ‘‘Zero | trust |                                                                   |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | ------------ | --- | ------------ | ------ | ----- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|               |              |     |              |     |              |        |       | [32] G.Dahia,L.Jesus,andM.PamplonaSegundo,‘‘Continuousauthentica- |     |     |     |     |     |     |     |
architecture,’’NationalInstituteofStandardsandTechnology,Tech.Rep., tionusingbiometrics:Anadvancedreview,’’WIREsDataMiningKnowl.
2020.[Online].Available:https://doi.org/10.6028/NIST.SP.800-207
Discovery,vol.10,no.4,p.1365,Jul.2020,doi:10.1002/widm.1365.
[14] D.Temoshok,D.Proud-Madruga,Y.-Y.Choong,R.Galluzzo,S.Gupta,
|     |     |     |     |     |     |     |     | [33] A. F. | Baig, S. | Eskeland, | and B. Yang, | ‘‘Privacy-preserving |     | continuous |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --------- | ------------ | -------------------- | --- | ---------- | --- |
C.LaSalle,N.Lefkovitz,andA.Regenscheid,‘‘Digitalidentityguide-
|     |     |     |     |     |     |     |     | authentication |     | using behavioral | biometrics,’’ |     | Int. J. Inf. | Secur., vol. | 22, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | ------------- | --- | ------------ | ------------ | --- |
lines,’’NationalInstituteofStandardsandTechnology,Gaithersburg,MD,
no.6,pp.1833–1847,Dec.2023,doi:10.1007/s10207-023-00721-y.
USA,Tech.Rep.800-63-4,2025,doi:10.6028/NIST.SP.800-63-4.
|     |     |     |     |     |     |     |     | [34] S. | Ayeswarya | and | K. J. Singh, | ‘‘A | comprehensive |     | review |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------------ | --- | ------------- | --- | ------ |
[15] (2021).WebAuthentication:AnApiforAccessingPublicKeyCredentials
|     |     |     |     |     |     |     |     | on  | secure | biometric-based | continuous |     | authentication | and | user |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------------- | ---------- | --- | -------------- | --- | ---- |
Level2.[Online].Available:https://www.w3.org/TR/webauthn-2/
|     |     |     |     |     |     |     |     | profiling,’’ | IEEE | Access, | vol. | 12, pp.82996–83021, |     | 2024, | doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------- | ---- | ------------------- | --- | ----- | ---- |
[16] L.S.Dasu,M.Dhamija,G.Dishitha,A.Vivekanandan,andV.Sarasvathi,
10.1109/ACCESS.2024.3411783.
| ‘‘Defending | against | identity | threats | using | risk-based | authentication,’’ |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | ------- | ----- | ---------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Cybern. Inf. Technol., vol. 23, no. 2, pp.105–123, Jun. 2023, doi: [35] S.AmbolandS.Rashad,‘‘Continuousauthenticationofsmartphoneusers
usingmachinelearning,’’inProc.11thIEEEAnnu.UbiquitousComput.,
10.2478/cait-2023-0016.
Electron.MobileCommun.Conf.(UEMCON),Oct.2020,pp.0056–0062,
| [17] C. Picard | and | S. Pierre, | ‘‘RLAuth: |     | A risk-based | authentication |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --------- | --- | ------------ | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
doi:10.1109/UEMCON51285.2020.9298040.
| system | using | reinforcement | learning,’’ |     | IEEE | Access, | vol. 11, |         |        |              |     |            |              |     |        |
| ------ | ----- | ------------- | ----------- | --- | ---- | ------- | -------- | ------- | ------ | ------------ | --- | ---------- | ------------ | --- | ------ |
|        |       |               |             |     |      |         |          | [36] S. | Hasan, | I. Amundson, | and | D. Hardin, | ‘‘Zero-trust |     | design |
pp.61129–61143,2023,doi:10.1109/ACCESS.2023.3286376.
|                |              |     |              |     |               |              |     | and      | assurance | patterns  | for cyber–physical   |     | systems,’’ | J.         | Syst. |
| -------------- | ------------ | --- | ------------ | --- | ------------- | ------------ | --- | -------- | --------- | --------- | -------------------- | --- | ---------- | ---------- | ----- |
| [18] V. Unsel, | S. Wiefling, |     | N. Gruschka, | and | L. Lo Iacono, | ‘‘Risk-based |     |          |           |           |                      |     |            |            |       |
|                |              |     |              |     |               |              |     | Archit., | vol.      | 155, Oct. | 2024, Art.no.103261. |     | [Online].  | Available: |       |
authentication for OpenStack: A fully functional implementation and https://www.sciencedirect.com/science/article/pii/S138376212400198X
guidingexample,’’inProc.13thACMConf.DataAppl.Secur.Privacy,
Apr.2023,pp.237–243,doi:10.1145/3577923.3583634. [37] P. Phiayura and S. Teerakanok, ‘‘A comprehensive framework
|                   |     |     |          |            |     |         |           | for | migrating | to zero | trust architecture,’’ |     | IEEE | Access, vol. | 11, |
| ----------------- | --- | --- | -------- | ---------- | --- | ------- | --------- | --- | --------- | ------- | --------------------- | --- | ---- | ------------ | --- |
| [19] I. Matiushin | and | V.  | Korkhov, | ‘‘MLE-RBA: | A   | machine | learning- |     |           |         |                       |     |      |              |     |
pp.19487–19511,2023.
empoweredrisk-basedauthenticationalgorithm,’’inProc.Comput.Sci.
|             |            |     |                   |     |      |                    |     | [38] Z. Adahman, |     | A. W. Malik, | and Z. | Anwar, | ‘‘An analysis | of zero-trust |     |
| ----------- | ---------- | --- | ----------------- | --- | ---- | ------------------ | --- | ---------------- | --- | ------------ | ------ | ------ | ------------- | ------------- | --- |
| Appl.-ICCSA | Workshops, |     | 2025, pp.325–339, |     | doi: | 10.1007/978-3-031- |     |                  |     |              |        |        |               |               |     |
architectureanditscost-effectivenessfororganizationalsecurity,’’Com-
97648-3_22.
|                |          |          |          |     |        |            |         | put. | Secur., vol. | 122, Nov. | 2022, | Art.no.102911. | [Online]. | Available: |     |
| -------------- | -------- | -------- | -------- | --- | ------ | ---------- | ------- | ---- | ------------ | --------- | ----- | -------------- | --------- | ---------- | --- |
| [20] Y. Zhang, | F. Wang, | J. Zeng, | L. Chen, | X.  | Huang, | Z. Li, and | K. Xue, |      |              |           |       |                |           |            |     |
‘‘Userbehavior-baseddynamicauthenticationdesignforenhancedidentity https://www.sciencedirect.com/science/article/pii/S0167404822003042
security,’’ in Proc. IEEE Int. Conf. Commun., Jun. 2025, pp.1–6, doi: [39] C. Liu, R. Tan, Y. Wu, Y. Feng, Z. Jin, F. Zhang, Y. Liu, and Q. Liu,
10.1109/ICC52391.2025.11161955. ‘‘Dissectingzerotrust:ResearchlandscapeanditsimplementationinIoT,’’
Cybersecurity,vol.7,no.1,p.20,May2024,doi:10.1186/s42400-024-
| [21] M. Papaioannou, |     | G. Zachos, | G.  | Mantas, | and J. Rodriguez, |     | ‘‘Novelty |     |     |     |     |     |     |     |     |
| -------------------- | --- | ---------- | --- | ------- | ----------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
00212-0.
| detection | for risk-based |         | user authentication |      | on mobile | devices,’’  | in   |                                                                        |     |     |     |     |     |     |     |
| --------- | -------------- | ------- | ------------------- | ---- | --------- | ----------- | ---- | ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|           |                |         |                     |      |           |             |      | [40] W.Yeoh,M.Liu,M.Shore,andF.Jiang,‘‘Zerotrustcybersecurity:Critical |     |     |     |     |     |     |     |
| Proc.     | IEEE Global    | Commun. | Conf.,              | Dec. | 2022,     | pp.837–842, | doi: |                                                                        |     |     |     |     |     |     |     |
10.1109/GLOBECOM48099.2022.10000843. successfactorsandamaturityassessmentframework,’’Comput.Secur.,
[22] Q. I. M. Hussain and V. Kale, ‘‘Risk-based adaptive authentication in vol.133,Oct.2023,Art.no.103412,doi:10.1016/j.cose.2023.103412.
mobile network system using dynamic elliptic curve digital signature [41] E.W.Tomlinson,W.D.Abrha,S.D.Kim,andS.A.Ortega,‘‘Cyber-
algorithm,’’ Concurrency Comput., Pract. Exper., vol. 37, nos. 21–22, securityaccesscontrol:Frameworkanalysisinahealthcareinstitution,’’
p.70208,Sep.2025.[Online].Available:https://onlinelibrary.wiley.com/ J. Cybersecurity Privacy, vol. 4, no. 3, pp.762–776, Sep. 2024, doi:
| doi/abs/10.1002/cpe.70208 |     |     |     |     |     |     |     | 10.3390/jcp4030035. |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
[23] M. Papaioannou, G. Mantas, and J. Rodriguez, ‘‘Risk-based user [42] Y.Kim,S.-G.Sohn,K.T.Kim,H.S.Jeon,S.-M.Lee,Y.Lee,andJ.Kim,
authenticationformobilepassengerIDdevicesforlandandseaborder ‘‘Exploringeffectivezerotrustarchitecturefordefensecybersecurity:A
control,’’inProc.IEEEInt.Medit.Conf.Commun.Netw.(MeditCom), study,’’ KSII Trans. Internet Inf. Syst., vol. 18, no. 9, pp.2665–2691,
Sep.2021,pp.180–185,doi:10.1109/MEDITCOM49071.2021.9647603. Sep.2024,doi:10.3837/tiis.2024.09.011.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 77877 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

V.Krishnan,C.S.Sreeja:ProvablyAdaptiveTrustDynamicsinContext-AwareZero-TrustSystems
[43] B. Hale, D. L. Van Bossuyt, N. Papakonstantinou, and B. O’Halloran, [57] National Institute of Standards and Technology. (2012). Guide for
‘‘Azero-trustmethodologyforsecurityofcomplexsystemswithmachine Conducting Risk Assessments. [Online]. Available: https://nvlpubs.nist.
learning components,’’ in Proc. 41st Comput. Inf. Eng. Conf. (CIE), gov/nistpubs/Legacy/SP/nistspecialpublication800-30r1.pdf
Aug.2021,p.002,doi:10.1115/detc2021-70442. [58] National Institute of Standards and Technology. (2018). Risk Manage-
[44] V.KrishnanandC.S.Sreeja,‘‘Zerotrust-basedadaptiveauthentication ment Framework for Information Systems and Organizations. [Online].
usingcompositeattributeset,’’inProc.IEEE3rdPhDColloq.Ethically Available:https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.
Driven Innov. Technol. Soc. (PhD EDITS), Nov. 2021, pp.1–2, doi: 800-37r2.pdf
10.1109/PHDEDITS53295.2021.9649474. [59] (2024).OWASPAuthenticationCheatSheet.[Online].Available:https://
[45] I.Ahmed,T.Nahar,S.S.Urmi,andK.A.Taher,‘‘Protectionofsensitive cheatsheetseries.owasp.org/cheatsheets/AuthenticationCheatSheet.html
data in zero trust model,’’ in Proc. Int. Conf. Comput. Advancements, [60] N. Harwood-Nash. (Jun. 2023). How Fast Do Planes Fly. [Online].
Jan.2020,pp.1–5,doi:10.1145/3377049.3377114. Available:https://airadvisor.com/en/blog/how-fast-do-planes-fly
[46] A.QaziandS.Arshad,‘‘Implementationofenhancedsecuritymeasuresin [61] V. Krishnan. (2026). ZeTHAA. [Online]. Available: https://github.com/
OracleERPcloudwithzerotrustarchitecture(ZTA),’’inProc.Int.Conf. vivinkrishnan/ZeTHAA
Commun.Technol.(ComTech),Apr.2025,pp.1–6.
[47] A.Farraj,‘‘Onusingzerotrusttosecuringindustrialcontrolsystemsin
thepowersystemsindustry,’’inProc.IEEETexasPowerEnergyConf. VIVIN KRISHNAN receivedthemaster’sdegree
(TPEC),Feb.2025,pp.1–5,doi:10.1109/TPEC63981.2025.10906998. intechnologyfromCochinUniversityofScience
[48] M. A. Aleisa, ‘‘Blockchain-enabled zero trust architecture for andTechnology.HeiscurrentlyaSoftwareArchi-
privacy-preserving cybersecurity in IoT environments,’’ IEEE Access, tect with Numentica Technologies, Bengaluru.
vol.13,pp.18660–18676,2025,doi:10.1109/ACCESS.2025.3529309. He is a Research Scholar at CHRIST (Deemed
[49] M.Tsai,S.Lee,andS.W.Shieh,‘‘Strategyforimplementingofzerotrust to be University), Bengaluru. He has more than
architecture,’’IEEETrans.Rel.,vol.73,no.1,pp.93–100,Mar.2024,doi: 18 years of IT experience. His areas of interest
10.1109/TR.2023.3345665. include information security, authentication, and
[50] A. Hassan, A. Rauf, N. Shafqat, R. Latif, and H. Khan, ‘‘ZenGuard a scalablesoftwaresystems.
machine learning based zero trust framework for context aware threat
mitigation using SIEM SOAR and UEBA,’’ Sci. Rep., vol. 15, no. 1,
p.35871,Oct.2025,doi:10.1038/s41598-025-20998-4.
[51] N.F.Syed,S.W.Shah,A.Shaghaghi,A.Anwar,Z.Baig,andR.Doss, C. S. SREEJA (Senior Member, IEEE) received
‘‘Zerotrustarchitecture(ZTA):Acomprehensivesurvey,’’IEEEAccess, the Ph.D. degree from CHRIST (Deemed to
vol.10,pp.57143–57179,2022. be University), Bengaluru, which focused on
[52] E.Hosney,I.Halim,andA.H.Yousef,‘‘Anartificialintelligenceapproach Informationsecurityaspects.SheisanAssistant
for deploying zero trust architecture (ZTA),’’ in Proc. 5th Int. Conf. Professor with the Quantum Technologies and
Comput.Inform.(ICCI),Mar.2022,pp.343–350. Complex Systems (CQTCS), CHRIST (Deemed
[53] E.Bertino,‘‘Zerotrustarchitecture:Doesithelp?’’IEEESecur.Privacy, to be University), where she has been a Faculty
vol.19,no.5,pp.95–96,Sep.2021,doi:10.1109/MSEC.2021.3091195. Member, since 2019. She has published her
[54] L.Bradatsch,O.Miroshkin,N.Trkulja,andF.Kargl,‘‘Zerotrustscore- researchworkinpeer-reviewedjournals,including
basednetwork-levelaccesscontrolinenterprisenetworks,’’inProc.IEEE ElsevierandInderscience,andintheproceedings
22nd Int. Conf. Trust, Secur. Privacy Comput. Commun. (TrustCom),
ofrenownedInternationalconferencesbyIEEE,Springer,andACM.Her
CA. Los Alamitos, CA, USA: IEEE Computer Society, Nov. 2023,
area of expertise in research includes, but is not limited to, information
pp.1422–1429. [Online]. Available: https://doi.ieeecomputersociety.org/
security,authentication,publickeycryptography,E-signature,bio-molecular
10.1109/TrustCom60117.2023.00194
computing, DNA cryptography, and blockchain. She also received the
[55] Q. Yao, Q. Wang, X. Zhang, and J. Fei, ‘‘Dynamic access control
IEEEbestthesisaward(second)forherPh.D.ThesisduringtheGraduate
and authorization system based on zero-trust architecture,’’ in Proc.
Int. Conf. Control, Robot. Intell. Syst., Oct. 2020, pp.123–127, doi: CongressGraTE’7’2019.ShealsoservedasareviewerforprestigiousIEEE
10.1145/3437802.3437824. Conferences,theSessionChair,andthePublicationsCo-ChairfortheIEEE
[56] SpecialPublication800-63b:DigitalIdentityGuidelines:Authentication PhDColloquiumonEthicallyDrivenInnovationandTechnologyforSociety
and Authenticator Management, National Institute of Standards and 2019and2020.SheisanactivememberoftheIEEEComSocBangalore
Technology,Gaithersburg,MD,USA,2025,doi:10.6028/NIST.SP.800- Chapter.
63B-4.
77878 VOLUME14,2026