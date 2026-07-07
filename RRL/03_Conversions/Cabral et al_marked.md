d
e
Non-Stationarity in Financial Time Series: A Unifying Survey on Drift
w
|     |     |     | Detection, |     | Adaptive | Learning, |     | and | Evaluation |     |     |     |     |
| --- | --- | --- | ---------- | --- | -------- | --------- | --- | --- | ---------- | --- | --- | --- | --- |
DaviM.Cabrala,∗,AdrianoM.A.Limaa,GustavoH.F.M.Oliveirab,AdrieanoL.I.Oliveiraa
aCentrodeInformática(CIn),UniversidadeFederaldePernambuco,Recife,PE,Brasil
bSistemasdeInformação,UniversidadeFederaldeAlagoas,Penedo,ALi,Brasil
v
e
Abstract
Predictiveanddecisionmodelsinfinancearetypicallyvalidatedunrderassumptionsofdistributionalstabilityover
the evaluation window. In deployment, those assumptions fail: the data-generating process undergoes structural

change—breaks,regimetransitions,anddrift—thatcaninvalidateconditionalrelationships,degradecalibration,and
amplify tail risk precisely when decisions are most consequentrial. Despite a large literature, results remain hard to
reconcileacrosseconometrics,statisticalmonitoring,andmachinelearningduetodivergentterminologyandincom-
e
patible evaluation protocols. This survey aims to overcome the fragmentation and provides three concrete tools for
research and deployment under non-stationarity in financial time series: (1) a unified taxonomy of drift and regime
change, (2) a pipeline that connects representation,edetection, and adaptation choices, and (3) an evaluation play-
book that supports apples-to-apples comparison. We align terms such as structural breaks, regimes, concept drift,
and dataset shift, and propose a taxonomy along temporal, statistical, spatial, and ontological axes to describe real
wpe
drift scenarios consistently. Using this lens, review drift-aware representations, change detection methods, and
continuous adaptation strategies—from classical sequential monitoring and segmentation to Bayesian, multivariate,
and embedding-based out-of-distribution approaches. We then consolidate evaluation guidance spanning detection

delay,false-alarmcontrol,computationalcost,andfinance-specificutility. Finally,wehighlightemergingdirections
(foundation models, multimodal context t , parameter-efficient adaptation) and open challenges in benchmark design
| andreliableonlinecalibration. |     |     |     | o   |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Keywords:
financialtimeseries,non-stationarity,conceptdrift,change-pointdetection,adaptivelearning,evaluationprotocols
n
1. Introduction predictive modeling in real-world, high-stakes deploy-

ments.
| Financial        | markets   | aretdynamic |           | and         | inherently | non-       |                                                    |            |                  |          |                 |             |              |
| ---------------- | --------- | ----------- | --------- | ----------- | ---------- | ---------- | -------------------------------------------------- | ---------- | ---------------- | -------- | --------------- | ----------- | ------------ |
|                  |           |             |           |             |            |            | In                                                 | practice,  | non-stationarity |          | progressively   |             | degrades     |
| stationary       | systemsn, | in          | which     | the data    | generation | pro-       |                                                    |            |                  |          |                 |             |              |
|                  |           |             |           |             |            |            | the                                                | predictive | performance      |          | and calibration |             | of forecast- |
| cess alternates  | between   |             | distinct  | statistical | regimes    | due        |                                                    |            |                  |          |                 |             |              |
|                  |           |             |           |             |            |            | ing                                                | models     | [? ?             | ? ? ].   | Under           | prequential | evalua-      |
| to macroeconomic |           | shocks,     | liquidity |             | crises,    | regulatory |                                                    |            |                  |          |                 |             |              |
|                  | shiifts   |             |           |             |            |            | tion,thisdegradationmanifestsassystematicincreases |            |                  |          |                 |             |              |
| changes,         | and       | in          | agent     | behavior    | [? ?       | ? ? ].     |                                                    |            |                  |          |                 |             |              |
|                  |           |             |           |             |            |            | in forecast                                        |            | error, unstable  | decision |                 | thresholds, | and de-      |
Thisphenomrenonappearsintheliteratureundervarious
|                             |     |                        |                 |                     |            |        | layed                                           | reactions       | to  | new regimes—often     |        | precisely | when        |
| --------------------------- | --- | ---------------------- | --------------- | ------------------- | ---------- | ------ | ----------------------------------------------- | --------------- | --- | --------------------- | ------ | --------- | ----------- |
| terms—including             |     | concept                | drift,          | regime              | change,    | struc- |                                                 |                 |     |                       |        |           |             |
| p                           |     |                        |                 |                     |            |        | errorsaremostcostlyintermsofriskexposureandeco- |                 |     |                       |        |           |             |
| tural breaks,               | and | heteroscedasticity—and |                 |                     | directly   | af-    |                                                 |                 |     |                       |        |           |             |
|                             |     |                        |                 |                     |            |        | nomic                                           | decision-making |     | [?                    | ? ? ]. | These     | effects ex- |
| fectscorefinancialtasks[??? |     |                        |                 | ??]suchaspricefore- |            |        |                                                 |                 |     |                       |        |           |             |
|                             |     |                        |                 |                     |            |        | pose                                            | the limitations |     | of stationarity-based |        |           | assumptions |
| caesting, riskmanagement,   |     |                        | orderexecution, |                     | andportfo- |        |                                                 |                 |     |                       |        |           |             |
andmotivateapproachescapableofanticipatingandre-
| lio allocation | [?  | ? ], creating |     | persistent | challenges | for |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
spondingtodistributionshiftsastheyoccur.
| r   |     |     |     |     |     |     | Addressing |     | these | challenges | requires | coupling | drift- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ---------- | -------- | -------- | ------ |
∗Correspondingauthor.Email:dmc6@cin.ufpe.br awarerepresentationswithtimelychangedetectionand
PEmailaddresses:dmc6@cin.ufpe.br(DaviM.Cabral),
|     |     |     |     |     |     |     | continuous |     | adaptation | [? ? | ? ? | ? ], | while evalua- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | ---- | --- | ---- | ------------- |
amal@cin.ufpe.br(AdrianoM.A.Lima),
|     |     |     |     |     |     |     | tion | must explicitly |     | account | not only | for | predictive ac- |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------------- | --- | ------- | -------- | --- | -------------- |
gustavo.oliveira@penedo.ufal.br(GustavoH.F.M.
Oliveira),alio@cin.ufpe.br(AdrianoL.I.Oliveira) curacy but also for detection delay and computational
| PreprintsubmittedtoNeurocomputing |     |     |     |     |     |     |     |     |     |     |     | February2,2026 |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- |
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
constraints[? ? ]. Inpractice, theeffectivenessofthis vergingacrosscommunities.Asaresult,machinelearn-
couplingdependscriticallyonhowdataarerepresented, ing,econometrics,andquantitwativefinancehavelargely
sinceinformativerepresentationsarenecessarytomake evolved in parallel, with limited cross-fertilization and
distributionshiftsobservableratherthanmaskingthem incompatibleframeworks. Theabsenceofasharedtax-
[? ? ]. Thisdependencynaturallyshiftsattentiontothe onomyandstandardizedevaluationhinderscumulative
e
role and design of financial data representations under evidenceandslowstheadoptionofdrift-awaremethods
non-stationarity. in practice, particularly in real-time and high-stakes fi-
Innon-stationaryfinancialenvironments,datarepre- nancialsettings[? ? ].
i
sentations must capture both endogenous market dy- With the aim of addressing these gaps, we formu-
v
namics and exogenous drivers. Embeddings learned latethefollowingresearchquestions: (RQ1)Howdoes
from price and volume series summarize endogenous the literature define and categorize the different forms
e
behavior, enabling comparisons across historical peri- of non-stationarity in financial time series? (RQ2)
odsandtheidentificationoflatentregimesbeyondclas- How can financial series be represented by integrat-
sicalindicators[??].However,marketbehaviorisalso ing endogenous and exogenous information to sup-
r
shapedbyexternalforces—suchasmacroeconomican- portthedetectionandinterpretationofregimechanges?
nouncements,geopoliticalevents,andfirm-leveldisclo- (RQ3 )Howcandistributionshiftsbeautomaticallyde-
sures—whicharenotobservableinpricedataalone.In- tected over time? (RQ4) How can model learning be
r
corporatingexogenousinformationthroughmultimodal adapted to distribution shifts continuously and effec-
inputs(e.g.,news,textualreports,andeconomicindica- etively? (RQ5) How can detection and adaptation sys-
tors)addseconomiccontexttodetectedshifts[? ? ? ], tems be evaluated under non-stationarity using appro-
yieldingrepresentationsthataremoreexpressiveunder priatemetricsandprotocols? (RQ6)Howcandetection
e
conceptdriftandbettersuitedtodistinguishingtransient and adaptation methods be benchmarked under non-
fluctuationsfromstructurallymeaningfulregimetransi- stationarity?(RQ7)Whatarethecurrentlimitationsand
tions. pfutureresearchdirections?
Withsuchenrichedrepresentations,continuousadap- In addressing these questions, this work makes four
tation becomes feasible. Model behavior can be up- contributions. (i) We introduce a unified taxonomy
datedthroughclassicalmechanisms—includ ingforget- of drift and regime change phenomena in financial
tingfactorsandregime-switchingstructutres[? ? ? ? ? timeseries,aligningterminologyacrossmachinelearn-
]—aswellasthroughmodernarchitecturesthatsupport ing, econometrics, andquantitativefinance(RQ1, Sec-
o
lightweight domain adaptation, such as specialized fi- tion 2). (ii) We structure the literature around a five-
nancialfoundationmodels[??].Inbothcases,contex- pillarpipeline—non-stationaritycharacterization,drift-
tualizedrepresentationsenablnemodelstorespondmore aware representations, change detection, continuous
selectivelyandinterpretablytoevolvingconditions,bal- adaptation, and evaluation—and review representative
ancing stability and responsiveness to improve robust- approaches for representation learning, change detec-
ness in online forecasting and decision-making. How- tion, and adaptation (RQ2–RQ4, Sections 3, 4, and
ever, the practical relevtance of these adaptive gains is 5).(iii)Wesummarizeevaluationmetrics,experimental
inseparablefromhowmodelperformanceisdefinedand protocols,andbenchmarkingpracticesusedinfinancial
n
measuredovertime. timeseries(RQ5–RQ6,Sections6and7). (iv)Finally,
Evaluation therefore emerges as a third essential di- we synthesize current limitations and outline open re-
mension,compleimentingrepresentationandadaptation. searchdirections(RQ7,Sections8and9).
To ensure prractical effectiveness, evaluation protocols
mustjointlyaccountforpredictiveperformance,detec- 1.1. Researchmethodologyandrelatedwork
tionspeped, false-alarmcontrol, computationalbudgets, Thissurveywasdevelopedthroughaniterativestrat-
and economic impact, reinforcing the need for realis- egy for literature retrieval, reading, and synthesis,
tic and comparable benchmarks [? ? ? ? ? ? ]. guidedbykeywordsearchesandbythetemporalchain-
e
Despite advances along these axes, progress remains ing of contributions. Initial searches were carried out
uneven and often confined to specific methodological inbroad-coveragedigitallibrariesandacademicaggre-
rtraditions, limiting comparability and cumulative evi- gators(e.g.,ScienceDirect,IEEEXplore,ACMDigital
dence. Library,SpringerLink,andGoogleScholar),withapri-
P
Atabroaderlevel,thetheoreticallandscaperemains maryfocusonpublicationsfrom2000to2025. When-
fragmented [? ? ? ? ], with modeling assumptions, ever needed to contextualize modern formulations of
methodological choices, and evaluation practices di- driftandregimechanges,wealsoincludedasmallsetof
2
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
earlierfoundationalreferences(e.g.,insequentialanal- tionalchangesandregimes;(4)adaptationmechanisms;
ysis,econometrics,andchange-pointdetection). and (5) evaluation and benchwmarking. We emphasize
Searchstringscombinedthreeintersectingfronts: (i) thatthegoalisnottoexhaustivelycoverallpublications
non-stationarity terminology (e.g., concept drift, dis- in this rapidly growing area, but to highlight seminal
tribution shift, regime change/shift, structural break, and representative contributions that clarify concepts,
change point); (ii) operational mechanisms (e.g., drift design trade-offs, and pr e actical implications for finan-
detection, change-point detection, sequential tests, cialdeployment.
adaptive/continual learning, test-time adaptation, re-
i
training,ensembles);and(iii)financialcontextsandre-
2. DriftsandRevgimesFoundationsandTaxonomy
alisticprotocols(e.g.,algorithmictrading,riskmanage-
ment,portfolio,volatility,marketmicrostructure,back- Thissectionseekstoanswerthequestion: howdoes
testing,transactioncosts).Beyondsurveysandreviews, the literaturee define and categorize the different forms
we also considered experimental and methodological of non-stationarity in financial time series? Different
studieswhenevertheycontributeddirectlytoanswering fields — statistics, econometrics, machine learning, fi-
r
theRQsandtostructuringthesurvey’spipeline(foun- nance,andthenaturalsciences—proposecomplemen-
dations,detection,adaptation,andevaluation). taryta xonomiestoaddressnon-stationarity. Inthiscon-
The corpus was progressively refined based on topi- text, there is a broad consensus that non-stationarity
r
calrelevanceandusefulnessfortheproposedsynthesis, referstovariation, overtime, inthestatisticalorstruc-
complementedbysnowballing(backwardandforward) etural properties of a data-generating process [? ? ? ?
fromseminalworks,recentsurveys,andrecurringrefer- ? ]. However, beyond this high-level definition, these
ences. Thisprocessresultedinasupersetof289unique fields differ in the way such changes in the data distri-
e
candidate references (deduplicated across sources and butionareformalized,categorized,andanalyzed.
rounds). Motivated by these differences in conceptualization
A central element of this refinement waspexamin- and emphasis, we present an ontology, illustrated in
ing the future-work sections of the retrieved papers Figure 1, that describes the non-stationarity problem
and,wheneverpossible,checkingwhethertheproposed in financial time series [? ? ? ? ? ] along four
directions were later investigated or addre ssed. This main classification axes: (i) a temporal axis, which
“from-future-to-present”trackingservedtasastructured characterizeswhenandhowchangesunfoldovertime;
scan of gaps and adjacent research lines: by relating (ii) a statistical axis, which specifies which proper-
o
explicit recommendations to subsequent evidence, we ties of the data-generating process are affected; (iii) a
were able to make persistent gaps explicit and map spatial axis, which describes where changes manifest
emerging themes correlated wnith regime changes and within the data structure; and (iv) an ontological axis,
concept drift (e.g., GNNs, foundation models, multi- whichdistinguishesthenatureandformalstatusofthe
modality, deep reinforcement learning, and knowledge change. Finally,wediscussthecausalaxis,whichiden-
representation). After an initial relevance screening tifiestheunderlyingdriversofnon-stationarity, includ-
and consolidation to retmove near-duplicates and out- ing exogenous shocks, endogenous feedback mecha-
of-scope items, this process yielded a shortlist of 220 nisms, and adversarial or institutional effects, linking
n
references. observeddriftsandregimetransitionstotheirsources.
For scope reasons and to preserve coherence with
the RQs and thie proposed conceptual pipeline, part 2.1. Temporalaxis
oftheseadjarcentthemeswasdeliberatelydeprioritized In the specific case of time series, non-stationarity
and not discussed in depth (e.g., topics centered on may affect the mean and variance of the very relation-
MLOpsp/operationalmonitoring, temporalfairness, pri- shipbetweenvariablesorthemechanismthatproduces
vacy/federatedlearning,andvintagedata/real-timedata them. Onewaytocharacterizetheseeffectsisbyfocus-
revisions,amongothers),remainingasopportunitiesfor ingonhowthechangesunfoldinrelationtothetiming
e
future work. The final manuscript therefore cites 174 andtemporalshapeofthechangeintheprocess,thatis,
references. howandwhenthechangeoccurs,forexample,asillus-
rFinally, the selected studies were organized accord- tratedinFigure2. Commontypesincludeabruptdrift,
ing to their predominant role in an end-to-end pipeline gradualdrift, incremental(orcontinuous)drift, andre-
P for financial systems under non-stationarity: (1) foun- current (or seasonal) drift [? ? ? ? ? ? ], but some
dations and terminology harmonization; (2) represen- surveys also highlight blips (transient deviations / out-
tation and context modeling; (3) detection of distribu- liers) to differentiate short-lived noise from structural
3
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Abrupt
Gradual Incremental Recurrent transition from an upward-trending regime to a
|     |     |     |     |     |     |     | downward-trending |     | regimwe, |     | as market | conditions |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | --- | --------- | ---------- |
how/when Temporal progressively weaken (from a bull market—a pe-
|     |     |     |     |     |     | ∆P(X) | riod | of broadly | rising | prices | and optimistic | senti- |
| --- | --- | --- | --- | --- | --- | ----- | ---- | ---------- | ------ | ------ | -------------- | ------ |
Regime
|     |     |                     |                  |     |     |                     | ment—to | a   | bear ma rket—a | period | of broadly | de- |
| --- | --- | ------------------- | ---------------- | --- | --- | ------------------- | ------- | --- | -------------- | ------ | ---------- | --- |
|     |     | O n to l o g i c al | Non-stationarity |     | Sta | ti s ti cal ∆P(Y|X) |         |     |                |        |            |     |
s tr u c t u r e w h a t cliningpricesandpessimisticsentiment1). e
Mechanism
∆P(Y)
S p a t ia l • Incremental / continuous drift: continuous drift
w h e r e
i
Global Local of parameters without a clear breakpoint or sta-
C au s al ble plateaus v , i.e., without discrete states. Exam-
w h y
|     |           |           |          |                     |             |                  | ples          | include | long-run                        | structural | (secular)    | trends, |
| --- | --------- | --------- | -------- | ------------------- | ----------- | ---------------- | ------------- | ------- | ------------------------------- | ---------- | ------------ | ------- |
|     |           | Exogenous |          | Endogenous          | Adversarial |                  |               |         |                                 |            |              |         |
|     |           |           |          |                     |             |                  | such          | aes the | multi-decade                    | decline    | in long-term | in-     |
|     |           |           |          |                     |             |                  | terestrates[? |         | ? ](Fig.3A),drivenbyslow-moving |            |              |         |
|     | Figure 1: | Extended  | taxonomy | of non-stationarity |             | along five axes: |               |         |                                 |            |              |         |
temporal(how/when),statistical(whatchanges),spatial(where),on-
forcesinsavingandinvestmentratherthanasingle
(structure/state),
tological with causal drivers (why) as the founda- abrruptshock.
tionallayer.

(A)DGS10
|     | changes                   | [? ? ? | ? ], which | we define | below   | to clar- | r   |     |     |     |     |     |
| --- | ------------------------- | ------ | ---------- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
|     | ifytheirtemporaldynamics. |        |            |           |         |          | e   |     |     |     |     |     |
|     | θ Abrupt                  |        |            | θ         | Gradual |          |     |     |     |     |     |     |
e
C2
|     |     |     |     | C1  |         | p   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | t   |     |         | t   |     |     |     |     |     |     |
|     |     | τ   |     |     | mixture |     |     |     |     |     |     |     |
(B)FEDFUNDS

|     | θ Incremental |     |     | θ   | Recurrent |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
t
S2
o
S1
|     |                |                             | t           | n            |                     | t           |     |     |     |     |     |     |
| --- | -------------- | --------------------------- | ----------- | ------------ | ------------------- | ----------- | --- | --- | --- | --- | --- | --- |
|     | Figure2:       | Temporalmorphologyofdrifts: |             |              | Abrupt—suddenchange |             |     |     |     |     |     |     |
|     | at changepoint | τ; Gradual—transition       |             | interval     | where               | old and new |     |     |     |     |     |     |
|     | concepts       | coexist and                 | switch with |   each other | gradually;          | Incremen-   |     |     |     |     |     |     |
tal—continuousparameterdritftwithoutstableplateaus;Recurrent—
alternationbetweenpreviouslyobservedstates.
Figure3:U.S.interest-rateseriesatmacromonthlytimescales(sam-
n ple: 1962-01 to 2025-12). (A) 10-year Treasury constant-maturity
yield(DGS10;end-of-periodatthisfrequency).(B)Effectivefederal
• Abrupt drift: sudden change that establishes a fundsrate(FEDFUNDS),summarizingthestanceofU.S.monetary
newlevelailmostinstantaneously. policy.Overthisperiod,the10-yearyielddeclinesfromaround14%
Forinstance,the
intheearly1980stoabout8%intheearly1990s,around5–6%in
|     | revelatiorn | of  | a major | accounting | fraud | at a large |                 |      |                      |     |           |             |
| --- | ----------- | --- | ------- | ---------- | ----- | ---------- | --------------- | ---- | -------------------- | --- | --------- | ----------- |
|     |             |     |         |            |       |            | the late 1990s, | near | 2% in the mid-2010s, |     | and below | 1% in 2020. |
corporationmaytriggeranimmediatemarket-wide Policy-ratemovementsin(B)shapeshort-termfinancingconditions
p
sell-off, abruptly shifting volatility regimes, risk andcantransmittolongermaturitiesin(A)throughexpectationsand
premia, and correlation structures across related termpremia,althoughthe10-yearyieldalsoreflectsinflationexpec-
tationsandbroaderriskcompensation.Source:FRED[??].
|     | esectors, | withthenewpricedynamicsandinvestor |     |     |     |     |     |     |     |     |     |     |
| --- | --------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sentimentestablishingthemselveswithinhoursor
|     |     |     |     |     |     |     | •         |     | /        |         |                |        |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------- | ------- | -------------- | ------ |
|     |     |     |     |     |     |     | Recurrent |     | seasonal | drifts: | unlike gradual | drift, |
asingletradingsession.
| r   |           |        |            |          |     |              | which | describes | a one-way |     | transition | where old |
| --- | --------- | ------ | ---------- | -------- | --- | ------------ | ----- | --------- | --------- | --- | ---------- | --------- |
|     | • Gradual | drift: | transition | interval |     | in which ob- |       |           |           |     |            |           |
P
|     | servations | from | the | old and | new concepts | coex- |     |     |     |     |     |     |
| --- | ---------- | ---- | --- | ------- | ------------ | ----- | --- | --- | --- | --- | --- | --- |
1Inequitymarkets,acommonruleofthumbdefinesabull(bear)
|     | ist, | withafuzzyboundary(amixtureofstatesfor |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
marketasarise(fall)ofabout20%ormoreinabroadmarketindex
some period). A canonical example is the slow overatleastatwo-monthperiod[??].
4
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
|     |     |     |     |     |     |     |     | • / |     | /   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and new concepts coexist for some time, recur- Prior label target shift: change in P(Y) t
rent drift refers to settings in which previously (class/event proportions,wor the marginal distribu-
observed concepts reappear after a period. Sea- tion of the target). This captures situations where
sonaldriftisaspecialcaseofrecurrentdriftwhere thefrequencyofoutcomeschangesovertime,even
these recurrences follow a deterministic periodic ifconditionalrelationsarerelativelystable.Anex-
e
pattern. For example, trading volume and volatil- ample is a trading signal classifier where the pro-
ity patterns may exhibit recurrent behavior tied to portionofbuy/sell/holdsignalschangesovertime
monthlyoptionsexpirationcycles, quarterlyearn- due to changing market conditions, while the fea-
i
ingsannouncements,orannualtax-lossharvesting turesthatcharacterizeeachsignaltyperemainsim-
v
|     | periods,withsimilarstatisticalpropertiesrecurring |     |     |     |     |     |     | ilar. |     |     |     |     |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
atregularintervals.
|     |     |     |     |     |     |     |     | • Class-econditional |     | shift: | change | in P (X | | Y) |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------ | ------ | ------- | ---- |
t
|     |     |     |     |     |     |     |     | with P(Y) | approximately |     | constant. | Again, | ap- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | --------- | ------ | --- |
t
2.2. Statisticalaxis
|     |     |     |     |     |     |     |     | proximately" | indicates |     | a working | approximation: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | --------- | -------------- | --- |
thermarginalprevalenceofclasses/eventsistreated
Thestatisticalaxisspecifieswhichcomponentofthe
data-generating distribution changes over time. To un- as stable (or controlled for) over the comparison

window,whilethefeaturedistributionwithineach
| derstand,letP(X,Y)denotethejointprobabilitydistri- |     | t   |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r classmoves(e.g.,duetomeasurement,microstruc-
butiongoverningthegenerationofinput–outputpairsat
effects).
timet,withthefactorizationP(X,Y)= P(Y | X)P(X). e ture, or representation For instance, in
|       |      |         |     | t           |              | t   | t    |         |            |       |      |                  |     |
| ----- | ---- | ------- | --- | ----------- | ------------ | --- | ---- | ------- | ---------- | ----- | ---- | ---------------- | --- |
|       |      |         |     |             |              |     |      | a model | predicting | order | book | price movements, |     |
| Here, | P(X) | defines | the | probability | distribution |     | from |         |            |       |      |                  |     |
t
whichinputsaredrawn,whileP(Y | X)definesthecon- the proportion of upward, downward, and stable
t
epricemovementsmayremainconstant,buttheor-
ditionalprobabilitygoverningthegenerationofoutputs
|     |     |     |     |     |     |     |     | der flow | patterns | characterizing |     | each movement |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------------- | --- | ------------- | --- |
giventheinputs.
|       |                                              |      |     |                    |     |      |        | class evolve  | as   | the composition |     | of market | partic-  |
| ----- | -------------------------------------------- | ---- | --- | ------------------ | --- | ---- | ------ | ------------- | ---- | --------------- | --- | --------- | -------- |
|       | Inthistaxonomy,categoriesaredefinedbythedom- |      |     |                    |     | p    |        |               |      |                 |     |           |          |
|       |                                              |      |     |                    |     |      |        | ipants shifts | from | predominantly   |     | retail to | institu- |
| inant | changing                                     | term | in  | this decomposition |     | (or, | equiv- |               |      |                 |     |           |          |
alently, in P(X | Y)P(Y)), i.e., whether the drift pri- tionaltraders,orastheprevalenceofspoofingand
|        |           | t        | t        |             |       |        |        |                                               |     |     |     |                   |     |
| ------ | --------- | -------- | -------- | ----------- | ----- | ------ | ------ | --------------------------------------------- | --- | --- | --- | ----------------- | --- |
|        | affects   |          |          |             |       |        |        | fakeorderschangesovertime.                    |     |     |     | IfP (Y)alsovaries |     |
| marily |           | P(X),    | P(Y),    | P(X         | | Y), | or P(Y | | X).  |                                               |     |     |     | t                 |     |
|        |           | t        | t        | t           |       | t      |        | materially,thesettingisbetterdescribedasamix- |     |     |     |                   |     |
| In     | practice, | however, | multiple | componentts |       | may    | evolve |                                               |     |     |     |                   |     |
turewithprior/labelshift.
| simultaneously. |     |     | Accordingly, | and | consistent |     | with the |     |     |     |     |     |     |
| --------------- | --- | --- | ------------ | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- |
o
| dominance-baseddefinitionabove,thecategoriesbelow |     |             |     |           |             |     |          | •       |           |          | /    |                  |     |
| ------------------------------------------------- | --- | ----------- | --- | --------- | ----------- | --- | -------- | ------- | --------- | -------- | ---- | ---------------- | --- |
|                                                   |     |             |     |           |             |     |          | Concept | (strict   | sense)   | real | drift: change    | in  |
| should                                            | be  | interpreted | as  | idealized | descriptors |     | that em- |         |           |          |      |                  |     |
|                                                   |     |             |     |           |             |     |          | P(Y |   | X), i.e., | a change | in   | the relationship | be- |
t
phasizetheprimarysourceofnchangeratherthanasmu- tween inputs and targets (often corresponding to
tuallyexclusivecases.
|     |                          |     |         |                |                     |         |       | "structural                                   | breaks" | or           | "regime | shifts" in         | econo- |
| --- | ------------------------ | --- | ------- | -------------- | ------------------- | ------- | ----- | --------------------------------------------- | ------- | ------------ | ------- | ------------------ | ------ |
|     |                          |     |         |                |                     |         |       | metrics/finance).                             |         | For example, |         | a price prediction |        |
|     | • Covariate              | /   | virtual | d rift: change |                     | in P(X) | while |                                               |         |              |         |                    |        |
|     |                          |     |         |                |                     | t       |       | modelmayobservethatthesametechnicalindica-    |         |              |         |                    |        |
|     | thepredictivemechtanismP |     |         |                | (Y | X)isassumedap- |         |       |                                               |         |              |         |                    |        |
|     |                          |     |         | t              |                     |         |       | tors(movingaverages,volumepatterns)thatprevi- |         |              |         |                    |        |
proximately invariant. Here, "approximately" re- ously signaled upward price movements now pre-
n
|     | flects | an idealized |     | assumption: | empirically, |     | one |     |     |     |     |     |     |
| --- | ------ | ------------ | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
dictdownwardmovements,reflectingafundamen-
|     |         | P(Y | | X) | ≈ P (Y | | X) on | the | overlap- |                            |     |     |     |     |     |
| --- | ------- | --- | ---- | ------ | ------- | --- | -------- | -------------------------- | --- | --- | --- | --- | --- |
|     | expects | t   |      | t′     |         |     |          | talchangeinmarketdynamics. |     |     |     |     |     |
pingsupporitofX(i.e.,regionswherebothperiods
assign nron-negligible probability mass), up to es- Many authors use the term concept drift in a broad
timationnoiseandminorresidualeffects.
|     |     |     |     |     |     |     | Inprac- | sense,todenoteanychangeinthedata-generatingpro- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------------------------------------------- | --- | --- | --- | --- | --- |
ticpe,thedriftisinterpretedasbeingdrivenmainly cess ∆P(X,Y), and not only real drift ∆P(Y | X) [? ?
by context/environment or sampling changes that ]. Inthissurvey,weadopttherestrictedconvention: we
reserve“conceptdrift”for∆P(Y
movethedistributionofinputs. Forinstance,are- | X)(realdrift)anduse
e
turn forecasting model trained on a market index “distributionshift”or“non-stationarity”forthegeneral
|     | may | face covariate |     | drift when | the | composition | of  | case. |     |     |     |     |     |
| --- | --- | -------------- | --- | ---------- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
rtheindexshiftstowardtechnologycompaniesand Toavoidambiguity,whencitedauthorsuse“concept
away from traditional manufacturing firms, even drift”inthebroadsense,weexplicitlyflagthisandmap
P
though the relationship between company-level ittoourtaxonomybyidentifyingwhichterminthestan-
features (valuation ratios, momentum, volatility) dardfactorizationsofP(X,Y)isdrifting. Table1sum-
t
andexpectedreturnsremainsstable. marizes the main terminological equivalences across
5
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Shock/stress
| machine                                    | learning, | econometrics, |     | statistics, | and | quanti- |                 |     |     |     |     |     |
| ------------------------------------------ | --------- | ------------- | --- | ----------- | --- | ------- | --------------- | --- | --- | --- | --- | --- |
| tativefinanceforbroad-sense“conceptdrift,” |           |               |     |             |     | mapping |                 |     |     |     | w   |     |
| changesin∆P(X),∆P(Y),∆P(Y                  |           |               |     | | X),∆P(X   |     | |Y),and |                 |     |     |     |     |     |
|                                            | t         |               | t   | t           | t   |         | leveldezilamroN |     |     |     |     |     |
∆P(X,Y)totheircommonlyusednamesineachcom-
t
munity.
Reallocation:risk→safety
|                        |               |        |               | “dataset/distribution |         |          |     |     |     | e   |     |     |
| ---------------------- | ------------- | ------ | ------------- | --------------------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
| In the                 | dataset-shift |        | literature,   |                       |         |          |     |     |     |     |     |     |
| shift” typically       |               | refers | to a mismatch |                       | between | training |     |     |     |     |     |     |
| and test distributions |               | (i.e., | the           | joint distribution    |         | differs  |     |     |     |     |     |     |
i
| across stages). |     | In contrast, | the | concept-drift |     | literature |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
v
| emphasizes | online/streaming |      | settings    |           | in which | the dis- |     |     |     |      |     |     |
| ---------- | ---------------- | ---- | ----------- | --------- | -------- | -------- | --- | --- | --- | ---- | --- | --- |
|            |                  |      |             | affecting |          |          |     |     |     | Time |     |     |
| tribution  | evolves          | over | time, often |           | the      | input–   |     |     |     |      |     |     |
e
targetrelationship.
|            |      |         |     |                           |     |     | Riskyasset(e.g.,equities) |     |     |     | Safeasset(e.g.,Treasuries) |     |
| ---------- | ---- | ------- | --- | ------------------------- | --- | --- | ------------------------- | --- | --- | --- | -------------------------- | --- |
| Throughout | this | survey, | we  | use “distribution/dataset |     |     |                           |     |     |     |                            |     |
shift” (or “non-stationarity”) as an umbrella term that Figure4:Schematicillustrationofflight-to-quality:duringstress,in-
r
coversbothoffline(train–test)andonline(time-varying) vestorsshiftfromriskyassetstosaferones,depressingriskyprices
andsupportingsafe-assetprices.
| settings, whilereserving“conceptdrift”forchangesin |                     |          |                |              |       |         |                     |     |               |     |                 |     |
| -------------------------------------------------- | ------------------- | -------- | -------------- | ------------ | ----- | ------- | ------------------- | --- | ------------- | --- | --------------- | --- |
| P(Y | X)underourrestrictedconvention.              |                     |          |                |              | [?    | ? ]     |                     |     | Externalshock |     |                 |     |
| t                                                  |                     |          |                |              |       |         | r                   |     |               |     |                 |     |
| But, in                                            | addition            | to these | terminologies, |              | other | classic | )citamehcs(levelXIV |     |               |     |                 |     |
|                                                    |                     |          |                |              |       |         | e                   |     |               |     | volatilityspike |     |
| dimensions                                         | of non-stationarity |          |                | can quantify | how   | much    |                     |     |               |     |                 |     |
| andwhichstatisticalmomentshavechanged[?            |                     |          |                |              |       | ? ? ? ? |                     |     |               |     |                 |     |
]:
e
| • First | order: | change | in E[X] | (mean, | trend) | or in |     |     |     |     |     |     |
| ------- | ------ | ------ | ------- | ------ | ------ | ----- | --- | --- | --- | --- | --- | --- |
t
| univariatelocationstatistics; |     |     |     |     |     |     |     |     |     |     |     | meanreversion |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
p
low-volregime
•
| Secondorder: |     | changeinVar(X)(volatility)orin |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
| Cov(X,X |     | )(autocorrelation)2[? |     |     | ? ];and |     |     |     |     | Time |     |     |
| ------- | --- | --------------------- | --- | --- | ------- | --- | --- | --- | --- | ---- | --- | --- |
t t−k

| • Multivariate: |     | change | in  | cross-dependence |     | (e.g., |          |                              |     |     |     |                   |
| --------------- | --- | ------ | --- | ---------------- | --- | ------ | -------- | ---------------------------- | --- | --- | --- | ----------------- |
|                 |     |        |     |                  | t   |        | Figure5: | SchematicexampleofaVIXspike: |     |     |     | anabruptjumpinim- |
covariance/correlation
across variables or assets) pliedvolatilityaroundashock,followedbygradualnormalization.
o
| andtaildependence3[? |     |     | ?   | ? ? ? | ].  |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
In multivariate settings, drifts may affect variances, ity explosions characterized by abrupt spikes in im-
n
covariance, correlation, and tail dependence across as- pliedvolatility(Fig.5),andincreasesincorrelationsand
sets. Financialcrisesaretypicallymarkedbyanabrupt taildependencereflectingcrisiscontagionmechanisms
increase in tail dependence, with losses converging (Fig.6). Thesephenomenaoccurinparallel,combining

first-order,second-order,andmultivariateeffects.
| across assets | that | were | previously | weakly | correlated, |     |     |     |     |     |     |     |
| ------------- | ---- | ---- | ---------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
t
leadingtothecollapseofdiversificationstrategies(see Figure 7 illustrates the typical inverse co-movement
Fig. 6). Conceptually, n such changes can be described between equity prices and implied volatility: equity
[?
as breaks in covariance matrices, transitions in depen- drawdowns often coincide with increases in VIX ],
dence graphs (financial networks), or changes in dy- which is computed from S&P 500 index option prices
i
|     |     |     |     |     |     |     | and is widely |     | used as | a market | “fear | gauge” [? ]. As |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ----- | --------------- |
namiccopulasthatcaptureasymmetricdependenceand
r
heavy tails [? ? ? ? ? ]. In these episodes, changes an example of a news-driven repricing episode, late-
of different orders often coexist: mean shifts associ- Jan.2025coveragereportedasharptech-ledsellofffol-
p
|           |                   |     |          |     |           |          | lowing                             | DeepSeek-related |                 | developments, |       | accompanied        |
| --------- | ----------------- | --- | -------- | --- | --------- | -------- | ---------------------------------- | ---------------- | --------------- | ------------- | ----- | ------------------ |
| ated with | flight-to-quality |     | dynamics |     | (Fig. 4), | volatil- |                                    |                  |                 |               |       |                    |
|           |                   |     |          |     |           |          | byaspikeinvolatilityexpectations[? |                  |                 |               |       | ? ? ].             |
| e         |                   |     |          |     |           |          | In terms                           | of               | the statistical |               | axis, | first/second-order |
2Foraunivariateseries{Xt },themeanisµt = E[Xt]andtheau- ∆P(X)
|                             |     |     |                 |                      |                      |     | tends to      | manifest | as           |            | changes        | in the features; |
| --------------------------- | --- | --- | --------------- | -------------------- | -------------------- | --- | ------------- | -------- | ------------ | ---------- | -------------- | ---------------- |
| tocovarianceatlaghisγ(h)    |     |     | = Cov(Xt+h,Xt); |                      | theautocorrelationis |     |               |          |              |            |                |                  |
|                             |     |     |                 |                      |                      |     | ∆P(Y) affects |          | marginal     | statistics | of the         | target; and real |
| r thenormalizedquantityρ(h) |     |     | = γ(h)/γ(0).    | Inweak(second-order) |                      |     |               |          |              |            |                |                  |
|                             |     |     |                 |                      |                      |     | drift ∆P(Y    | |        | X) manifests |            | as instability | of parame-       |
stationarity,µtisconstantandγ(h)dependsonlyonthelagh(noton
P t).
| 3Tail dependence |     | captures | extremal | co-movement | and | is often |     |     |     |     |     |     |
| ---------------- | --- | -------- | -------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
quantifiedbycoefficientsdefinedaslimitsofconditionalquantileex- 4https://github.com/davimcabral/NonStationarityIn
ceedanceprobabilities. FinancialTS/blob/main/graphic_sp500_vix.ipynb
6
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
|     |     |     | Crisis/contagion |     |     | • Globaldrift,whenthechangebroadlyaffectsthe |     |     |     |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
Normalconditions
|     |     |     |     |     |     | entire | domain, | impacting | w most | regions | of  | the fea- |
| --- | --- | --- | --- | --- | --- | ------ | ------- | --------- | ------ | ------- | --- | -------- |
turespaceorthemajorityofsubpopulationssimul-
|     |                    |     |     |     |     | taneously. |           | Forinstance,acentralbankinterestrate |         |           |          |        |
| --- | ------------------ | --- | --- | --- | --- | ---------- | --------- | ------------------------------------ | ------- | --------- | -------- | ------ |
|     |                    |     |     |     |     | change     | typically | affects                              | pricing | dynamics  |          | across |
|     | Taildependence:    | co- |     |     |     |            |           |                                      |         |           |          |        |
|     | movementinextremes |     |     |     |     |            |           | e                                    |         |           |          |        |
|     |                    |     |     |     |     | all asset  | classes   | and                                  | market  | segments, | inducing | a      |
(jointlossesbecome
system-wideshiftinexpectedreturnsandriskpre-
morelikely)
mia.
i
| lowercross-dependence                                         |     |     | highercorrelationand |     |     |                                               |         |              |        |             |     |          |
| ------------------------------------------------------------- | --- | --- | -------------------- | --- | --- | --------------------------------------------- | ------- | ------------ | ------ | ----------- | --- | -------- |
|                                                               |     |     | taildependence       |     |     | •                                             |         | v            |        |             |     |          |
|                                                               |     |     |                      |     |     | Local                                         | drift,  | when the     | change | is confined |     | to spe-  |
|                                                               |     |     |                      |     |     | cific                                         | regions | of the input | space, | such        | as  | a single |
| Figure6: Schematicillustrationofcrisiscontagioninacross-asset |     |     |                      |     |     |                                               |         |              |        |             |     |          |
|                                                               |     |     |                      |     |     | economicsector,assetclass,geographicmarket,or | e       |              |        |             |     |          |
network.Nodesrepresentassets(orvariables)andedgesdenotestatis-
ticaldependence,withthickeredgesindicatingstrongerdependence. customergroup. Forexample, regulatorychanges
Undernormalconditions(left),dependenceisweakeranddiversifi- affectingonlythepharmaceuticalsectormayalter
| cationiseffective. | Duringcrises(right),dependenceandtaildepen- |     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r
denceincrease,makingjointextremelossesmorelikelyandreducing the predictive relationships for healthcare stocks
diversificationbenefits. while leaving technology or energy sectors unaf-

|     |     |     |     |     |     | fected. | Thesechangesarespatiallyheterogeneous, |          |           |     |         |         |
| --- | --- | --- | --- | --- | --- | ------- | -------------------------------------- | -------- | --------- | --- | ------- | ------- |
|     |     |     |     |     |     | r       |                                        |          | difficult |     |         |         |
|     |     |     |     |     |     | often   | subtle,                                | and more |           | to  | detect, | requir- |
(A)S&P500andits125-daymovingaverage
e ingregion-awareorsubdomain-sensitivemonitor-
ingmethods.
e
|     |     |     |     |     |         | (A)GlobalDrift:MarketCrash |     |              |         | (B)LocalDrift:Sector-Specific |            |                  |
| --- | --- | --- | --- | --- | ------- | -------------------------- | --- | ------------ | ------- | ----------------------------- | ---------- | ---------------- |
|     |     |     |     |     | Returns |                            |     |              | Returns |                               |            |                  |
|     |     |     |     | p   |         |                            |     | —Tech        |         |                               |            | — T e c h        |
|     |     |     |     |     |         |                            |     | —Energy —Fin |         |                               |            | —E —n F ie n rgy |
|     |     |     |     |     |         |                            |     | —Health      |         |                               |            | —Health          |
|     |     |     |     |     |         |                            |     | noigertfird  |         |                               | tfirdlacol |                  |
(B)VIXandits50-daymovingaverage
drift

|     |     |     |     |     |     |           | Allsectors   |                  |     | Othersectors |          |          |
| --- | --- | --- | --- | --- | --- | --------- | ------------ | ---------------- | --- | ------------ | -------- | -------- |
|     |     |     | t   |     |     |           | droptogether |                  |     | stable       |          |          |
|     |     |     |     |     |     |           |              | t                |     |              |          | t        |
|     |     |     |     |     |     | Pre-crash |              | Mar2020 Recovery |     | Stable       | Oilcrash | Recovery |
o
Figure8:Spatialdriftinfinancialtimeseries.(A)Globaldrift:Dur-
ingtheMarch2020COVID-19marketcrash,allsectorsexperienced
synchronizedvolatilityincreaseanddrawdown—driftaffectstheen-
n
tiremarket.(B)Localdrift:Duringthe2014oilpricecollapse,only
|     |     |     |     |     | the                         | energy | sector (bold | orange)                              | experienced | significant |     | drift while |
| --- | --- | --- | --- | --- | --------------------------- | ------ | ------------ | ------------------------------------ | ----------- | ----------- | --- | ----------- |
|     |     |     |     |     | othersectorsremainedstable. |        |              | Localdriftrequiressector-specificde- |             |             |     |             |
Figure7:Co-movementbetweenequitypricesandimpliedvolatility   tectionandadaptationratherthanmarket-wideretraining.
| (dailydata).                               | Authors’ownplot. | Theplottingnotebookisavailable |     |      |        |         |                 |                |         |        |               |           |
| ------------------------------------------ | ---------------- | ------------------------------ | --- | ---- | ------ | ------- | --------------- | -------------- | ------- | ------ | ------------- | --------- |
| online.4.                                  | t                |                                |     |      |        |         |                 |                |         |        |               |           |
| DataaccessedviaFRED(seriesSP500andVIXCLS   |                  |                                |     | [? ? |        |         |                 |                |         |        |               |           |
|                                            |                  |                                |     |      |        | Beyond  | the distinction |                | between | global | and           | local ef- |
| ];underlyingindexdataarenotredistributed). | n                |                                |     |      |        |         |                 |                |         |        |               |           |
|                                            |                  |                                |     |      | fects, | spatial | drifts          | may differ     | in      | their  | structural    | foot-     |
|                                            |                  |                                |     |      | print  | across  | the             | feature space. | Changes |        | can propagate |           |
ters/coefficientsandofconditionaldependencies,going
|     | i   |     |     |     | smoothly |     | across | neighboring | regions, |     | remain | isolated |
| --- | --- | --- | --- | --- | -------- | --- | ------ | ----------- | -------- | --- | ------ | -------- |
beyondmarginalmoments[? ? ? ? ? ? ]. within well-defined clusters, or emerge along specific
r
unaffected.
|     |     |     |     |     | dimensions |     | while | leaving | others |     | Such | pat- |
| --- | --- | --- | --- | --- | ---------- | --- | ----- | ------- | ------ | --- | ---- | ---- |
2.3. Spatialaxis p ternsreflectthegeometryoftheinputspaceandthein-
Thespatialaxisconcernsthereachofachangewithin teractionstructureamongvariables,ratherthantempo-
thefeaturespaceoracrosssubpopulations,asillustrated ral ordering, and are naturally described through par-
e
in Fig. 8. It characterizes where in the input domain a titions of the feature domain, network representations,
change occurs and how broadly it spreads across vari- or conditional submodels tailored to specific subpopu-
| r ables, assets, | or groups. From | this | perspective, | spatial | lations. |     |     |     |     |     |     |     |
| ---------------- | --------------- | ---- | ------------ | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
changescanbedistinguishedaccordingtotheirextent, Whydoscalesmatterforthetaxonomy? Driftsman-
P rangingfromdriftsthataffecttheentiredomaintothose different
|     |     |     |     |     | ifest | at  |     | frequencies, | and | the | scale | often de- |
| --- | --- | --- | --- | --- | ----- | --- | --- | ------------ | --- | --- | ----- | --------- |
confinedtospecificregionsofthefeaturespace,asfor- termines which morphological pattern dominates. At
(years/decades),
malizedin[? ? ? ],anddescribedbelow: macro scales drifts tend to be abrupt
7
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table1:Terminologicalequivalencesacrosstraditions(broad-sense“conceptdrift”).
w
|     |     |            |     | Machine         |     |                 |     |     |            | Quant   |     |     |
| --- | --- | ---------- | --- | --------------- | --- | --------------- | --- | --- | ---------- | ------- | --- | --- |
|     |     | Phenomenon |     | learning        |     | Econometrics    |     |     | Statistics | finance |     |     |
|     |     |            |     | Covariateshift/ |     | Exogenousshift/ |     |     |            |         |     |     |
Covariate
∆P(X)
tfirDtpecnoC )esnesdaorb( covariatedrift exogenousshock shift eMarketdislocation
Conceptdrift
|     |     |      |     |                   |     | Structural |       | Conditional     |       |             |     |     |
| --- | --- | ---- | --- | ----------------- | --- | ---------- | ----- | --------------- | ----- | ----------- | --- | --- |
|     |     | ∆P(Y | |X) | (strictsense)     |     |            | break |                 | shift | Regimeshift |     |     |
|     |     |      |     | Labelshift/prior- |     | Endogenous |       | Target/marginal |       | Behavioural |     |     |
i
|     |     | ∆P(Y) |     | probabilityshift |     |     | change |     | shift               |     | shift |     |
| --- | --- | ----- | --- | ---------------- | --- | --- | ------ | --- | ------------------- | --- | ----- | --- |
|     |     |       |     | Datasetshift/    |     |     |        |     | vMarketregimeshift/ |     |       |     |
∆P(X,Y) distributionshift Non-stationarity Jointshift non-stationarity
e
(policy shocks, interest-rate regime changes; Fig. 3B) through piecewise models with approximate stationar-
or incremental (secular trends linked to business and ity,wheretimeseriesalternatebetweenafinitenumber
r
monetary-policy cycles;Fig. 3A) [? ? ? ? ]. At of discrete and persistent states separated by change-
daily/weekly
scales, recurrent drifts prevail, associated points (see Fig. 9). Transitions between regimes may
with risk-on/risk-off switches, news cycles and repric- berabrupt,asduringfinancialcrises,orgradual,reflect-
ingofriskaroundannouncementwindows[? ? ? ? ]. ingslowstructuraladjustmentsintheeconomy.
e
Athighfrequency,intradayseasonalityandmicrostruc-
|     |     |     |     |     |     |     | This | framework | helps | clarify | the relationship | be- |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ----- | ------- | ---------------- | --- |
tureeffects(open/closepatterns,auctions,lunchbreaks)
|     |     |     |     |     |     |     | tweendriftandregimechange. |     |     | Everyregimetransition |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --------------------- | --- | --- |
generate deterministic patterns that overlay structu ral necessarily involves a statistical change. But the con-
e
| driftsobservedatlongerhorizons[? |     |     |     | ?   | ? ]. Incryptoas- |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
versedoesnothold,becausemanydriftsarisefromcon-
sets,boom–bustcyclestendtooverlapwiththesescales, tinuousorincrementaladjustmentsthatdonotintroduce
whiledeterministicevents(suchashalvings)apctasnat- a new regime. For instance, a brief spike in volatility
| ural triggers | for | regime | changes | [? ]. | Multiscale | ap- |            |     |                        |     |         |             |
| ------------- | --- | ------ | ------- | ----- | ---------- | --- | ---------- | --- | ---------------------- | --- | ------- | ----------- |
|               |     |        |         |       |            |     | represents | a   | short-lived deviation, |     | whereas | a sustained |
proaches[? ? ? ] allowtimeseriestobedecomposed periodofelevatedvolatilityoverseveralmonthsreflects
| into different | frequencies, |     | reveal | regimes |  that | remain |     |     |     |     |     |     |
| -------------- | ------------ | --- | ------ | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- |
agenuineregimechange.Thedistinctionbetweenthese
hiddenatsingleresolutions,andthusclatssifydriftsac- casesisillustratedinFig.9.
| cordingtotheirdominantscale[? |     |     |     | ? ? ? | ].  |     |                                                |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ----- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
|                               |     |     |     | o     |     |     | Inpractice,achangeistypicallyinterpretedasanew |     |     |     |     |     |
regimewhenitsatisfiesthreebroadcriteria[??].First,
2.4. Ontologicalaxis
|     |     |     |     |     |     |     | the change | must | be persistent, | lasting | long | enough to |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | -------------- | ------- | ---- | --------- |
n
|     |     |     |     |     |     |     | ruleouttransientnoise. |     | Second, | itmustbedistinctive, |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | ------- | -------------------- | --- | --- |
Notallchangesindatacorrespondtothesametypeof
differ
structural transformation. Some variations reflect tran- meaning that its statistical properties meaning-
|     |     |     |     |     |     |     | fully | from those | observed | previously. | Finally, | regimes |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | -------- | ----------- | -------- | ------- |
sientfluctuationsarounda stablesystemconfiguration,
|     |     |     |     |     |     |     | may | be recurrent, | in the | sense that | the same | state can |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ | ---------- | -------- | --------- |
whileotherssignaladeeperchangeinhowthedatagen-
t
|                    |        |                                  |     |                 |      |         | reappear                                     | over  | time, although       | recurrence     |     | is not a strict |
| ------------------ | ------ | -------------------------------- | --- | --------------- | ---- | ------- | -------------------------------------------- | ----- | -------------------- | -------------- | --- | --------------- |
| eration system     |        | operates.                        | The | ontological     | axis | focuses |                                              |       |                      |                |     |                 |
|                    |        | n                                |     |                 |      |         | requirement.                                 |       |                      |                |     |                 |
| onthesequalitative |        | differencesbetweendistinctsystem |     |                 |      |         |                                              |       |                      |                |     |                 |
| states.            |        |                                  |     |                 |      |         | Beyondregimechanges,theontologicalaxisencom- |       |                      |                |     |                 |
|                    |        |                                  |     |                 |      |         | passes                                       | other | forms of qualitative | transformation |     | in the          |
| A useful           | wayito | understand                       |     | such structural |      | changes |                                              |       |                      |                |     |                 |
is through the notion of a regime. Intuitively, a regime data-generatingprocess, capturingchangesinwhatthe
r
|     |     |     |     |     |     |     | system | is, rather | than only | in how | its statistical | prop- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --------- | ------ | --------------- | ----- |
correspondstoapersistentmodeofoperationofthedata
generatpionsystem. Whilearegimeisinplace,datafol- erties evolve. In financial applications, such transfor-
lowrelativelystablepatterns;whentheregimechanges, mationsincludeshiftsbetweenpersistentmarketstates,
theemergenceofnewmarketcategoriesorinstruments,
| these patterns |     | are altered | in a | systematic | and | lasting |     |     |     |     |     |     |
| -------------- | --- | ----------- | ---- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
e
way. In financial markets, common examples include andstructuralchangesinhowdataaregenerated,asil-
lustratedbyexamplessummarizedinTable2.
bullandbearphases,sustainedtransitionsbetweenlow-
rand high-volatility states, and crisis periods character- These ontological changes intersect with the tempo-
izedbypersistentlyhighcross-assetcorrelations. ral,statistical,andspatialaxes,butaredistinguishedby
P
In econometrics, from a modeling perspective, reflecting modifications in the underlying structure or
regimes are often treated as latent states that govern semantics of the problem, rather than purely quantita-
the data-generating process. This idea is formalized tivevariation[? ? ? ? ? ? ]. Commonempiricaldrivers
8
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
(A)RegimeDrift:DiscreteStates (B)MechanismDrift:RelationshipChange 2.5. CausesofNon-Stationary
| Returns |     |     | Returns |     |     |     |     |     |     |     | w   |     |     |     |
| ------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
—Stocks—Bonds From a causal standpoint, drifts and regime changes
ρ(t)
µ>0,σlow BullRegime µ<0,σhigh BearRegime µ>0,σlow BullRegime -10+1 can be triggered by exogenous, endogenous, or adver-
|     |     |     |     |     | tfirdmsinahcem |     | sarialfactors. |     | Amongexogenousdrivers,monetarypol- |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
ρ<0
ρ>0
icyandinterest-ratecyclees,supplyanddemandshocks,
financialcrises,andgeopoliticaleventsstandout.These
|        |        |        |     | correlation Negative |                  | correlation Positive |                      |       |               |           |               |       |               |        |
| ------ | ------ | ------ | --- | -------------------- | ---------------- | -------------------- | -------------------- | ----- | ------------- | --------- | ------------- | ----- | ------------- | ------ |
|        |        | t      |     |                      |                  | t                    |                      |       |               |           |               |       |               |        |
|        |        |        |     |                      |                  |                      | forces               | alter | expectations, |           | risk pricing, |       | and risk      | premia |
| State1 | State2 | State1 |     |                      | structuralchange |                      |                      |       |               | i         |               |       |               |        |
|        |        |        |     |                      |                  |                      | acrossdifferenttimeh |       |               | orizons[? |               | ? ? ? | ]. Endogenous |        |
S1→S2 S2→S1 mechanisms arise v from within the financial system it-
|     |     |     |     |     |     |     | self. | Leverage, | liquidity |     | constraints, | margin | calls, | and |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --------- | --- | ------------ | ------ | ------ | --- |
Figure9:Ontologicaldriftinfinancialtimeseries.(A)Regimedrift:
feedbackdyenamicsbetweeninvestorstrategiescanam-
Discretestatetransitionsbetweenbullandbearmarkets.Eachregime
hasdistinctstatisticalproperties(µ,σ),buttheunderlyingdatagener- plifyshocksandgenerateregimetransitionseveninthe
ationmechanismremainsconsistentwithinstates. ModeledbyHid- absenceofnewexternalevents[? ? ? ].
| denMarkovModels(HMMs),regime-switchingmodels. |                                                 |     |     |     | (B)Mech- |     |       | r   |            |     |       |        |         |     |
| --------------------------------------------- | ----------------------------------------------- | --- | --- | --- | -------- | --- | ----- | --- | ---------- | --- | ----- | ------ | ------- | --- |
|                                               |                                                 |     |     |     |          |     | Table | 3   | summarizes | how | these | causal | drivers | map |
| anismdrift:                                   | Fundamentalrelationshipchanges—stock-bondcorre- |     |     |     |          |     |       |     |            |     |       |        |         |     |
lationshiftsfromnegativetopositive(asobserved2020-2022). The onto  the temporal, statistical, and spatial axes of the
correlationstructureρ(t)evolvescontinuously,representingachange proposed taxonomy, illustrating how different sources
| inthecausal/structuralrelationshipsratherthanjuststateswitching. |     |     |     |     |     |     | r                                                      |                |     |              |               |             |         |         |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------ | -------------- | --- | ------------ | ------------- | ----------- | ------- | ------- |
|                                                                  |     |     |     |     |     |     | of non-stationarityinducecharacteristicpatternsofdrift |                |     |              |               |             |         |         |
|                                                                  |     |     |     |     |     |     | eacross                                                | dimensions.    |     | In addition, |               | adversarial | or      | manipu- |
|                                                                  |     |     |     |     |     |     | lative                                                 | behaviors—such |     | as           | pump-and-dump |             | schemes | or      |
ofthesechanges—suchaspolicyinterventions,techno-
|                      |                   |           |         |                 |                  |         | spoofing | practices |        | in less    | liquid | markets—may |            | distort |
| -------------------- | ----------------- | --------- | ------- | --------------- | ---------------- | ------- | -------- | --------- | ------ | ---------- | ------ | ----------- | ---------- | ------- |
| logical innovations, |                   | or market |         | disruptions—are |                  | further |          |           |        |            |        |             |            |         |
|                      |                   |           |         |                 |                  | elocal  |          | signals.  | These  | actions    | often  | produce     | short-term |         |
| mapped to            | the corresponding |           | axes    | in              | Table 3.         | Within  |          |           |        |            |        |             |            |         |
|                      |                   |           |         |                 |                  |         | drifts   | that      | do not | correspond | to     | long-term   | structural |         |
| this framework,      | ontological       |           | changes |                 | can be organized |         |          |           |        |            |        |             |            |         |
changes.
| intothefollowingcategories: |     |     |     |     | p   |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Athighfrequency,marketmicrostructureeffectsplay
|          |        |     |             |     |         |         | a central | role. | Latency, | order | flow, | tick | size, and | mar- |
| -------- | ------ | --- | ----------- | --- | ------- | ------- | --------- | ----- | -------- | ----- | ----- | ---- | --------- | ---- |
| • Regime | change | —   | transitions |     | between | persis- |           |       |          |       |       |      |           |      |
 ketrulescancreatespecificregimes,suchasshallowor
tentlatentstateswithdistinctstatisticalsignatures,
deeporderbooks,narroworwidespreads,andwindows
| while | preserving | the | same | set | ofttarget | classes |     |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ---- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ofelevatedmicrostructuralnoise.Thesemicrostructure-
| (e.g., | bull versus | bear | markets, |     | low versus | high |     |     |     |     |     |     |     |     |
| ------ | ----------- | ---- | -------- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
o
|     |     |     |     |     |     |     | driven | regimes | overlay |     | macroeconomic |     | regimes | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------- | --- | ------------- | --- | ------- | --- |
volatility);
|           |                  |     |        |            |             |       | contribute     |     | to the | overall | complexity | of  | observed | finan- |
| --------- | ---------------- | --- | ------ | ---------- | ----------- | ----- | -------------- | --- | ------ | ------- | ---------- | --- | -------- | ------ |
|           |                  |     |        |            |             |       | cialdynamics[? |     |        | ? ? ].  |            |     |          |        |
| • Concept | evolution        |     | / nenw | classes    | — the       | emer- |                |     |        |         |            |     |          |        |
| gence     | or disappearance |     | of     | previously | nonexistent |       |                |     |        |         |            |     |          |        |
effectively
| target                 | classes, |     |                          | expanding | or redefining |     |     |                          |     |     |     |     |     |     |
| ---------------------- | -------- | --- | ------------------------ | --------- | ------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
|                        |          |     |                          |           |               |     | 3.  | RepresentationandContext |     |     |     |     |     |     |
| theproblem’sontolog y. |          |     | Forinstance,theintroduc- |           |               |     |     |                          |     |     |     |     |     |     |
tionofanewassettclass(suchasexchange-traded
fundsorcryptocurrencyfutures)createsnovelpre- The purpose of this section is to provide the foun-
n
dictiontargetsthatdidnotexistinthetrainingpe- dationsforaddressingthefollowingquestion: howcan
financialtimeseriesberepresented,andhowcaninter-
| riod, | requiring | models | to  | recognize | and | adapt to |     |     |     |     |     |     |     |     |
| ----- | --------- | ------ | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
entirelynewicategories; nal and external information be integrated, to support
|     |     |     |     |     |     |     | thedetectionandinterpretationofregimechanges? |     |     |     |     |     |     | For |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
r
| • Mechanism |            | change | — modifications |      | to               | the un- |                   |          |           |          |     |                    |     |     |
| ----------- | ---------- | ------ | --------------- | ---- | ---------------- | ------- | ----------------- | -------- | --------- | -------- | --- | ------------------ | --- | --- |
|             |            |        |                 |      |                  |         | this,             | we adopt | a layered | approach |     | to representation, |     | il- |
| deprlying   | generative |        | process,        | such | as the introduc- |         | lustratedinFig10. |          |           |          |     |                    |     |     |
tionofnewvariables,rules,ordependencies,even Atthefirstlevel,weconsiderinternalsignalsderived
when observable classes remain unchanged. An fromthetimeseriesitself,correspondingtoendogenous
e
example is the implementation of circuit breakers information. At the second level, we incorporate ex-
| or new | trading | halts | that alter | market | microstruc- |     |     |     |     |     |     |     |     |     |
| ------ | ------- | ----- | ---------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ogenouscontext,representingexternalinformationthat
r ture,changinghoworderflowtranslatesintoprice influencestheobserveddynamics. Athirdlayerexplic-
movementswithoutnecessarilychangingtheclas- itly models the latent structure of underlying states or
Psificationtargets(e.g.,up/down/neutralpricedirec-
regimesaspartoftherepresentation,enablingaconnec-
| tion). |     |     |     |     |     |     | tionbetweenobserveddataandunobservedmarketcon- |         |     |             |                 |     |     |          |
| ------ | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | ------- | --- | ----------- | --------------- | --- | --- | -------- |
|        |     |     |     |     |     |     | ditions.                                       | Fourth, |     | we consider | representations |     |     | oriented |
9
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table2:Summaryofdrifttaxonomicaxeswithfinancialexamples
w
Temporalaxis(how Statisticalaxis(what Spatialaxis Ontologicalaxis Typicalfinancialexample
| andwhen) | changes) |     | (where) | (structure/state) |     |     |     |
| -------- | -------- | --- | ------- | ----------------- | --- | --- | --- |
Abrupt ∆P(Y|X) Global Regimechange(normal→ Marketcrash;jumpinriskpremium
|     |     |     |     | crisis) |     | e   |     |
| --- | --- | --- | --- | ------- | --- | --- | --- |
Abrupt ∆P(Y) Global Samesetofclasses(nonew Suddendowngradeofsovereignor
|        |       |     |       | ontology)       | large-bankcreditrating            |     |     |
| ------ | ----- | --- | ----- | --------------- | --------------------------------- | --- | --- |
|        | ∆P(X) |     |       |                 | Riegulatoryshockinaspecificsector |     |     |
| Abrupt |       |     | Local | Mechanismchange |                                   |     |     |
(regulation/rules)
v
∆P(X)
Gradual Local Samesetofclasses(flows Slowsectorrotation(outofonesectorinto
|     |     |     |     | withintheregime) | another) |     |     |
| --- | --- | --- | --- | ---------------- | -------- | --- | --- |
e
Incremental/ 1st/2ndorderinP(X) Global Macroregimeinsl owdrift Seculardownwardtrendininterestrates
continuous
Recurrent/seasonal P(X)/P(Y)and2ndorder Globalor Recurrentseasonalregimes Januaryeffect;intradayopen/closepatterns
|     |     |     | local | r   |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- |
Gradual ∆P(Y|X) Local Mechanismadjustment Marketlearningtopriceanewassetor
|     |     |     |     | withinthesameregime   | technology |     |     |
| --- | --- | --- | --- | --------------------- | ---------- | --- | --- |
Abrupt 2ndorder(dependence/ Global Contagrionregime(normal Correlationcollapseincrises;lossof
|        | tails)  |     |       | →highdependence)   | diversification                       |     |     |
| ------ | ------- | --- | ----- | ------------------ | ------------------------------------- | --- | --- |
|        | ∆P(X|Y) |     |       | eChangeinselection |                                       |     |     |
| Abrupt |         |     | Local |                    | Newcredit-scoringcriterionchangingthe |     |     |
|        |         |     |       | mechanism          | profileofapprovedclients              |     |     |
Table3:Mappinegdriftcausestotaxonomicaxes
| Cause |     | Temporalaxis | Statisticalaxis | Spatialaxis | Example |     |     |
| ----- | --- | ------------ | --------------- | ----------- | ------- | --- | --- |
p
∆P(Y|X)+∆P(X)
| Monetary-policyshock |     | Abrupt |     | Global | Surpriseinterest-ratehike |     |     |
| -------------------- | --- | ------ | --- | ------ | ------------------------- | --- | --- |
(exogenous)
 ∆P(X),2ndorder,
Liquiditycontagion Gradual Global(systemic) Cascadingmargincalls
| (endogenous) |     |     | multivariate |     |     |     |     |
| ------------ | --- | --- | ------------ | --- | --- | --- | --- |
t
Demographictrend Incremental(long-run) ∆P(Y) Global Populationageing
(country/region)
| (exogenous) |     | o   |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
Pump-and-dump Blip(transient) ∆P(X),1storder Local Manipulationincryptomarkets
(adversarial)
Bitcoinhalving(exogenous) Recunrrent ∆P(X)+∆P(Y|X) Global(crypto Supply-reductionevents
|     |     | (deterministic) |     | assets) |     |     |     |
| --- | --- | --------------- | --- | ------- | --- | --- | --- |

towardrobustness,emphasizinginvarianceandtransfer- can also be summarized through learned representa-
t
abilityacrossassets,timeperiods,andmarketenviron- tions. Fig. 11 illustrates this idea: each time window
n
| ments. |     |     |     | w isencodedintoalatentvectorz,sothatdriftcanbe |     |     |     |
| ------ | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
|        |     |     |     | t                                              |     | t   |     |
The goal of these representations is to transform monitored as a change in the trajectory {z} in the em-
t
| raw data | into a i feature space | in which | regime-relevant | beddingspace. |     |     |     |
| -------- | ---------------------- | -------- | --------------- | ------------- | --- | --- | --- |
changes become explicit, whether as drifts in embed- Classical studies in time-series statistics and econo-
r
dings, reorganizations of network structures, or varia- metricsshowthatalargeshareoffinancialdriftsmani-
tions inplatent indicators. Figure 10 provides a com- festsaschangesinfirst-andsecond-orderpropertiesof
pactroadmapofhowweorganizedrift-awarerepresen- theseries(level,trend,volatility,autocorrelation),orin
tationsinthissurvey.
|     |     |     |     | morecomplexformsoftemporaldependence[? |     |     | ? ? ? |
| --- | --- | --- | --- | -------------------------------------- | --- | --- | ----- |
e
|     |     |     |     | ? ]. Thus, | a natural starting | point is to construct | diag- |
| --- | --- | --- | --- | ---------- | ------------------ | --------------------- | ----- |
3.1. InternalSignalsandSeriesEmbeddings nostic features computed in moving time windows (or
rInternal Signals. The most basic layer of representa- multiple time scales) that capture these statistics. Ex-
| tionconsistsoftheinternalsignalscontainedinthetime |     |     |     | amplesinclude: |     |     |     |
| -------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- |
P
seriesitself—prices,returns,volumes,spreads,among
others—analyzedthroughthelensofnon-stationarity. • Location and dispersion statistics: moving
Beyondclassicalhandcraftedstatistics, internalsignals means,medians,orquantiles;realizedvolatilityin
10
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
rollingwindows;measuresofskewnessandkurto-
|     |     |     |     |     |     |     | sisofreturns. |     |     |     | w   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
•
|     |     |     |     |     |     |     | Temporal  |     | dependence |                 | measures: |       | autocorre-   |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --------------- | --------- | ----- | ------------ | --- |
|     |     |     |     |     |     |     | lation    | and | partial    | autocorrelation |           |       | coefficients |     |
|     |     |     |     |     |     |     | (ACF/PACF |     | [? ?       | e]) at          | several   | lags; | assessment   |     |
RawData:prices,volumes,spreads,news
oflongmemoryviastatisticssuchaslong-runvari-
anceorunit-roottests(toidentifychangesbetween
InternalSignals •Movingstatistics(mean,var,ACF) stationaryandnoin-stationarytrends).
•Multi-scaledecomposition
|     |                                                       | endogenousfeatures |     |     | •Learnedembeddingszt |     |                          |     |     |     |                         |     |     |     |
| --- | ----------------------------------------------------- | ------------------ | --- | --- | -------------------- | --- | ------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- |
|     | lacigolotno,laitaps,laropmet,lacitsitats:sexaymonoxaT |                    |     |     |                      |     |                          |     | v   |     |                         |     |     |     |
|     |                                                       |                    |     |     |                      |     | • Multi-scaleindicators: |     |     |     | featuresobtainedthrough |     |     |     |
ExogenousContext •Macrovariables(rates,VIX) waveletdecompositionsorlow-/high-passfiltersat
•Microstructure(spread,depth)
|     |     | externalinformation |     |     | •News&sentiment(multimodal) |     |         | e                                       |     |     |     |     |     |     |
| --- | --- | ------------------- | --- | --- | --------------------------- | --- | ------- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |                     |     |     |                             |     | differe | nthorizons,toseparateshort-,medium-,and |     |     |     |     |     |     |
long-termmovements[????].Forexample,dif-
•RegimeprobabilitiesP(St)
|     |     | LatentStructure |     |     | •Dynamicgraphs(correlations) |     |     |     |     |     |     |     |     |     |
| --- | --- | --------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
states&relationships ferencesinmeansacrossscales(detectionoftrend
|     |     |     |     |     | •Changepointposteriors |     |     | r   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
changes)orenergymetricsinspecificfrequencies
( detectionofemerging/vanishingcycles).
|     |     | Robustness&Invariance |     |     | •Causal/invariantfeatures |     |     |     |     |     |     |     |     |     |
| --- | --- | --------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•Foundationmodelembeddings
|     |     | stablefeatures |     |     | •Cross-regimestability |     |                 |          |              |     |            |          |          |     |
| --- | --- | -------------- | --- | --- | ---------------------- | --- | --------------- | -------- | ------------ | --- | ---------- | -------- | -------- | --- |
|     |     |                |     |     |                        |     | rThese          | features | provide      | an  | aggregated |          | view of  | how |
|     |     |                |     |     |                        |     | the statistical |          | axis evolves |     | when       | computed | continu- |     |
e
Drift-awarerepresentation→Detection(Section4)/Adaptation(Section5)
|           |                                                      |     |     |     |     |     | ously in      | sliding | windows.         | For         | example,     | one        | can          | mon- |
| --------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | ------- | ---------------- | ----------- | ------------ | ---------- | ------------ | ---- |
|           |                                                      |     |     |     |     |     | itor whether  |         | the mean         | or variance |              | of returns | exhibits     |      |
| Figure10: | Representationlayersfordrift-awarefinancialmodeling. |     |     |     |     |     |               |         |                  |             |              |            |              |      |
|           |                                                      |     |     |     |     |     | a significant |         | drift indicating |             | a transition | in         | the volatil- |      |
Rawdataisprogressivelytransformedthroughinternalsignalexterac-
tion, exogenous context integration, latent structure modeling, and ity regime [? ? ? ]; track changes in the correla-
robustness-orientedfeatures,producingrepresentationsthatfeedde- tion between an asset and an important risk factor [?
| tectionandadaptationsystems. |     |     |     |     |     | p?  |          |           |               |       |            |           |                |      |
| ---------------------------- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------------- | ----- | ---------- | --------- | -------------- | ---- |
|                              |     |     |     |     |     |     | ? ];     | or detect | instabilities |       | in the     | estimated | param-         |      |
|                              |     |     |     |     |     |     | eters of | a local   | model         | (such | as changes |           | in the coeffi- |      |
|                              |     |     |     |     |     |     | cients   | of a CAPM | calibrated    |       | in rolling | windows)  |                | [? ? |

|     |     |     |     |     |     |     | ]. Indeed,                                         | many     | change-detection |        | approaches |            | in        | finan- |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | -------- | ---------------- | ------ | ---------- | ---------- | --------- | ------ |
|     |     |     |     |     | t   |     | cialtimeseriesrelyonmonitoringsuchstatisticsinreal |          |                  |        |            |            |           |        |
|     |     |     |     | o   |     |     | time.                                              | However, | as the           | number | of         | series and | variables |        |
increases—suchaswhenconsideringmultipleassetssi-
multaneouslyormultiplefrequencies(e.g.,dailyandin-
n
|     |     |     |     |     |     |     | traday)—relying |     | solely | on pre-defined, |     | manually |     | engi- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | --------------- | --- | -------- | --- | ----- |
neeredfeaturesquicklybecomesinfeasible.
|     |     |     |     |     |     |     | Series | Embeddings. | In  | this | context, | the | concept-drift |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ---- | -------- | --- | ------------- | --- |
EmbeddingSpace
TimeSeries z(2) (broad sense) literature for data streams, together with
|     | xt  |     | t   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Bull
|     |     |     |     | z2  |     |     | advances | in deep | learning, | suggests |     | the need | to  | learn |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------- | -------- | --- | -------- | --- | ----- |
n
|     |     |     |     | z1  |     |     | representations |     | automatically, |     | rather | than | manually |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- | --- | ------ | ---- | -------- | --- |
drift
|     |     |     | encode |     | z3  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
specifyingallrelevantstatistics.Theobjectiveistotrain
|     |     | i   |     |     | z4  | z5  | a parametric |     | function | f that | maps | sequences | or  | time |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------ | ---- | --------- | --- | ---- |
θ
|     |          | t      |     |     | Bear |      | windows | to dense | vectors | z   | ∈ Rd | (i.e., temporal |     | em- |
| --- | -------- | ------ | --- | --- | ---- | ---- | ------- | -------- | ------- | --- | ---- | --------------- | --- | --- |
|     | w1 w2 w3 | rw4 w5 |     |     |      | z(1) |         |          |         | t   |      |                 |     |     |
fθ:wt(cid:55)→zt beddings), such that periods exhibiting similar behav-
|     | p   |     |     |     |     |     | ior are | mapped | to nearby | regions | in  | latent | space | [? ? |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | --------- | ------- | --- | ------ | ----- | ---- |
Figure11: Learnedembeddingsfordriftdetection. Timewindows ? ? ]. This idea—learning embeddings that represent
| wt  | areencodedintolatentvectorszt |     |     | ∈ Rd. Similarmarketcondi- |     |     |            |       |        |            |     |        |              |     |
| --- | ----------------------------- | --- | --- | ------------------------- | --- | --- | ---------- | ----- | ------ | ---------- | --- | ------ | ------------ | --- |
|     |                               |     |     |                           |     |     | the latent | state | of the | series—has |     | become | particularly |     |
tioensclustertogether(bullvs.bearregimes),whiledriftmanifestsas
|                                            |     |     |     |     |                |     | prominent | in  | non-stationary |     | settings, | as learned |     | repre- |
| ------------------------------------------ | --- | --- | --- | --- | -------------- | --- | --------- | --- | -------------- | --- | --------- | ---------- | --- | ------ |
| trajectorymovementacrosstheembeddingspace. |     |     |     |     | Changepointde- |     |           |     |                |     |           |            |     |        |
effective
tectioncanbeapplieddirectlytothesequence{zt }. sentations are often more at capturing com-
| r   |     |     |     |     |     |     | plex drift | patterns | than | hand-crafted |     | indicators |     | [? ? |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | ------------ | --- | ---------- | --- | ---- |
]. Table4summarizesthemaindrift-awarerepresenta-
P
tionoptionsdiscussedinthissection,providingastruc-
|     |     |     |     |     |     |     | tured overview |     | before | we examine |     | specific | approaches |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ---------- | --- | -------- | ---------- | --- |
inmoredetail.
11
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
As an example, the TS2Vec approach proposed by tiple horizons, wavelet decompositions, or specialized
Yue et al. [? ] uses hierarchical contrastive learning layersforcapturingdistinctfrwequenciesincreasesensi-
to produce embeddings that are robust across multiple tivity to drifts at various scales [? ? ? ? ? ? ? ?
temporal resolutions. Essentially, the model is trained ]. Rather than deciding in advance on a single “cor-
togenerateconsistentrepresentationsz forsimilarsub- rect” scale, these architectures internalize multiple fre-
t
e
sequences,whileseparatingsequenceswithdistinctpat- quenciesintherepresentation. Thisconnectsdirectlyto
terns. Thus,locallysimilarwindowsremaincloseinla- thetemporal/morphologicalaxisofthetaxonomy(Sec-
tentspace,whereaswindowscorrespondingtodifferent tion2): bysimultaneouslyconsideringlong-andshort-
i
behavior patterns (e.g., bull vs. bear markets, low vs. termcomponents,wecandetectbothgraduallong-term
v
highvolatilityperiods)aremappedtodistantregionsof changesandseasonalorabruptshort-termshifts. Stud-
the embedding space. Studies report that such learned iesinhigh-frequencymarketsshowthatignoringsimul-
e
embeddingsareusefulnotonlyforchangedetectionbut taneousscales—forexample,analyzingonlythemacro
alsoforpredictivetasksandanomalydetectionintime trend and ignoring daily/intraday cycles — can lead to
series. distortedassessmentsofvolatilityandregimeidentifica-
r
Inthecontextofdriftdetection,operatinginthelatent tion[? ? ? ]. Multi-scaleembeddingsthereforetendto
spacez hasanadvantage: classicalchangepointmeth- provid erobustnessinthedetectionofcomplexchanges.
t
ods can be applied directly to the embedding series[?
r
? ]. Techniques such as CUSUM [? ? ], PELT [? ], 3.2. Exogenous Context, Multimodality, and Market
or non-parametric (kernel) tests [? ? ? ] can be run eStructure
on sequences of vectors z instead of on the raw data. MacroeconomicandExogenousContext. Thesecond
t
Since these embeddings are trained to condense high- representation layer concerns the exogenous context
e
dimensional relevant information (including nonlinear that influences financial regimes. As discussed in Sec-
dynamics)intoafewcomponents,asignificantchange tion2.5,manydriftsoriginateinmacroeconomicshocks
inseriesbehaviortendstomanifestasadetectapbleshift and cycles, monetary-policy decisions, liquidity crises,
intheembeddings. Inshort, thelearnedrepresentation or geopolitical events [? ? ? ? ? ]. Ignoring these
“pre-processes”thedatasothatrelevantchangesareal- contextual dimensions can lead to myopic representa-
readyhighlighted,facilitatingthedetection stage. tionsthattreattheseriesasanisolatedsystemwhen,in
A recent line of research goes furthertand explores reality,itrespondstoexternalfactors.
trainingobjectivesorientedspecificallytowardanoma- A fundamental strategy is to incorporate macroeco-
o
liesanddrifts. Forexample,contrastivelearningmeth- nomicandaggregatefinancialvariablesascovariatesin
odsthatinjectsyntheticanomaliesorperturbationsdur- the representation model. For example, one might in-
ing training, following a philnosophy similar to expos- cludeseriessuchasshort-andlong-terminterestrates,
ing deep networks to outliers [? ]. Here, embeddings inflationindices,activityindicators,creditspreads,risk-
are trained to maximize separation between “normal” aversionmetrics(VIX,etc.),aswellasestablishedrisk
and “altered” patterns. Su ch approaches include new- factors (value, momentum, size, etc.) [? ? ? ? ?
class detection methodstin data streams [? ? ] and ]. Thesecontextualvariablescanbeintegratedintothe
self-supervised techniques like the CARLA model for
representationsystemindifferentways:
n
timeseries,whichusescontrastiveobjectivescalibrated 1. Direct feature fusion: includes contextual vari-
to highlight temporal anomalies [? ]. The result is to ables as additional attributes concatenated to the
bring the represeintation stage closer to the final detec- internalfeaturesoftheseriesineachtimewindow.
tiontask:onerconstructsalatentspacedesignedtomake That is, the input to the representation model in-
breaks,noveltyevents,andout-of-distributionobserva- cludes not only attributes derived from the target
tionsmporeevident[? ? ? ? ]. Inotherwords, instead series,butalsothecorrespondingvaluesofmacro
ofgenericembeddings, one trainsembeddingsthatare indicatorsinthatinterval.
explicitlysensitivetodrift. 2. State models with exogenous drivers: in latent-
e
Another important consideration is to embed the in- regime models (such as HMMs5 or MS-VAR 6),
trinsicmulti-scaletemporalstructureofthedataintothe
rrepresentation[? ? ]. Differentchangesmanifestatdif- 5AHiddenMarkovModel(HMM)assumesalatentregime/state
ferent time scales — for example, a secular trend ver- processStthatevolvesasaMarkovchain,whileobservationsYtare
P generated conditionally on the current state (via emission distribu-
sus intraday cycles — and choosing a single analysis
tions).Inferencetypicallyreliesonforward–backwardrecursionsand
scale a priori can lead to blind spots for certain types EM/Baum–Welch-typeestimation[???].
of change [? ? ]. Models that integrate filters at mul- 6AMarkov-SwitchingVectorAutoregression(MS-VAR)isaVAR
12
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
w
Table4:Comparisonofembeddingmethodsfordrift-awarefinancialtime-seriesrepresentation.
Method LearningType Real-time Interpretability Advantages Limitations
e
Manual Statistical None (hand- Yes High(domainstatis- Transparent; com- Requires feature
Features [? ? ? ? crafted) tics) putationally light; engineering;limited
|     | ?]  |     |     |     | domain | knowledge | tolinear/simplepat- |     |
| --- | --- | --- | --- | --- | ------ | --------- | ------------------- | --- |
i
|     |     |     |     |     | integration |     | terns;           | doesn’t scale |
| --- | --- | --- | --- | --- | ----------- | --- | ---------------- | ------------- |
|     |     |     |     |     | v           |     | tohighdimensions |               |
TS2Vec[?] Self-supervised Yes (after Low(black-box) Multi-resolution Requires pre-
erobust
|     |     | (contrastive) | training) |     |          | embeddings;    | training;         | limited |
| --- | --- | ------------- | --------- | --- | -------- | -------------- | ----------------- | ------- |
|     |     |               |           |     | no       | labels needed; | interpretability; |         |
|     |     |               |           |     | captures | complex        | sensitive         | to aug- |
|     |     |               |           | r   | patterns |                | mentationdesign   |         |
Drift-Oriented Self-supervised Yes (after Low–Medium Explicitly sensitive Requires careful
Embeddings (anomaly con- training) to drifts; synthetic anomaly design;
r
|     | (CARLA)[?] | trastive) |     |           | anomaly | injection; | may       | overfit to |
| --- | ---------- | --------- | --- | --------- | ------- | ---------- | --------- | ---------- |
|     |            |           |     | etailored |         | for detec- | injected  | patterns;  |
|     |            |           |     |           | tion    |            | black-box |            |
Regime-Switching Unsupervised Yes (online High (discrete Probabilisticregime Assumes discrete
|     | (HMM/MS-VAR) |     | e   |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
(EM) filtering) regimes) states; interpretable states; parametric
|     | [????] |     |     |     | transitions;       | inte- | assumptions;     | model |
| --- | ------ | --- | --- | --- | ------------------ | ----- | ---------------- | ----- |
|     |        |     |     |     | gratesmacrodrivers |       | misspecification |       |
p
risk
Bayesian On- Unsupervised Yes (on- High (run-length Real-time change- Computational
line Changepoint (Bayesian) line ) posterior) point probabilities; complexity; para-
|     | (BOCPD)[? | ? ? ? |     |     | uncertaintyquantifi- |     | metric | likelihood |
| --- | --------- | ----- | --- | --- | -------------------- | --- | ------ | ---------- |
t
|     | ??] |     |     |     | cation;   | principled | assumptions; | tuning |
| --- | --- | --- | --- | --- | --------- | ---------- | ------------ | ------ |
|     |     |     | o   |     | inference |            | priors       |        |
Multimodal(Series Supervised / Yes (after Medium (attention Early signals from Alignment com-
+Text)[???]
Self-supervised n training) maps) news; rich context; plexity; requires
|     |     |     |     |     | captures | narrative | textualdata;    | modal- |
| --- | --- | --- | --- | --- | -------- | --------- | --------------- | ------ |
|     |     |     |     |     | drivers  |           | ityfusiondesign |        |
GraphNeuralNet- Supe rvised / Yes (after Medium (graph Systemic view; Graph construction
works (GNN) [? ? Stelf-supervised training) structure) captures cross-asset choice; scalability
|     | ?]  |     |     |     | dependencies; | net- | to large | networks; |
| --- | --- | --- | --- | --- | ------------- | ---- | -------- | --------- |
n
|     |     |     |     |     | work      | reorganization | dynamic  | edge com- |
| --- | --- | --- | --- | --- | --------- | -------------- | -------- | --------- |
|     |     |     |     |     | detection |                | putation |           |
Foundation Miod- Self-supervised Yes (infer- Low(black-box) Generalization;data Domain gap; adap-
els (Pre-trairned) [? (transfer) ence) efficiency; lever- tation needed;
|     | ?]  |     |     |     | ages      | cross-domain | updatemechanisms;    |     |
| --- | --- | --- | --- | --- | --------- | ------------ | -------------------- | --- |
|     | p   |     |     |     | patterns; | minimal      | interpretabilityloss |     |
training
Invariant/Causal Supervised Yes (after High (causal struc- Robustness to dis- Requires environ-
e
Features[? ? ? ? ? (IRM) training) ture) tribution shifts; ment annotations;
|     | ?]  |     |     |     | focuses      | on sta-        | assumptions  | on     |
| --- | --- | --- | --- | --- | ------------ | -------------- | ------------ | ------ |
|     | r   |     |     |     | ble          | relationships; | causal       | graph; |
|     |     |     |     |     | reduces      | spurious       | optimization | com-   |
| P   |     |     |     |     | correlations |                | plexity      |        |
13
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
•
macro variables can act as drivers that modulate Impact and resilience metrics: how much the
transition dynamics between regimes. For exam- price moves after a larwge order (price impact)
ple,interest-rateorinflationdynamicscanbeused andhowquicklythemarketrecovers(liquidityre-
| asexplanatoryvariablesinthetransitionprobabil- |        |           |       |          |                   |             | silience); |          |             |        |               |          |          |
| ---------------------------------------------- | ------ | --------- | ----- | -------- | ----------------- | ----------- | ---------- | -------- | ----------- | ------ | ------------- | -------- | -------- |
| ities                                          | of a   | Markovian | model | [?       | ? ? ?             | ]. This ap- |            |          |             |        |               |          |          |
|                                                |        |           |       |          |                   |             | Together,  | these    | indicaetors | make   | it            | possible | to iden- |
| proach                                         | embeds | context   |       | into the | very state-change |             |            |          |             |        |               |          |          |
|                                                |        |           |       |          |                   |             | tify early | signs of | liquidity   | stress | or structural |          | changes  |
process,increasinginterpretability(regimescanbe
associated with certain macro levels) and poten- inmarketfunctioning. Empiricalstudiesshowthatsuch
i
microstructureindicatorscananticipateveryshort-term
tiallyimprovingthedetectionoftransitions.
v
Jointmultimodalembeddings: drifts related to phenomena such as flight-to-liquidity,
| 3.  |     |     |     |     | indeeparchitec- |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
liquiditycrunches,orlocalizedstressphasesinspecific
| tures,       | one | can train | a network |         | to learn | joint rep-  |           |              |         |       |         |               |      |
| ------------ | --- | --------- | --------- | ------- | -------- | ----------- | --------- | ------------ | ------- | ----- | ------- | ------------- | ---- |
|              |     |           |           |         |          |             | markets   | [?e? ?       | ]. That | is,   | before  | a broader     | risk |
| resentations |     | that      | combine   | prices  | with     | macro indi- |           |              |         |       |         |               |      |
|              |     |           |           |         |          |             | regime is | established, | we      | often | observe | deterioration |      |
| cators       | and | other     | factors.  | In this | case,    | rather than |           |              |         |       |         |               |      |
inmicrostructureindicators(e.g.,wideningspreads,re-
| simply | concatenating |     | series, | it  | is common | to em- |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
r
ploy sub-networks or cross-attention mechanisms duceddepth)thatsignalalossofliquidity. Incorporat-
ingth esesignalsintotherepresentationmakesitreflect
| that | integrate | the | modalities. |     | The network | then |     |     |     |     |     |     |     |
| ---- | --------- | --- | ----------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
thecurrentstateofmicrostructure,whichoftenprecedes
producesaunifiedembeddingthatsimultaneously
broaderchangesinprice/riskregimes.Incontrast,arep- r
encodesthebehaviorofthefinancialseriesandits
eresentationbasedsolelyonaggregatedpricesmayfailto
| associatedmacroeconomiccontext[? |     |     |     |     | ?   | ].  |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
capturethesesubtlestructuralchanges.
Studieswithregime-switchingandMS-VARmodels
|            |         |      |       |       |         | eMultimodalContextandTextualInformation. |     |     |     |     |     |     | Inad- |
| ---------- | ------- | ---- | ----- | ----- | ------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
| in finance | suggest | that | using | macro | factors | as part of                               |     |     |     |     |     |     |       |
dition,animportantaspectisthemultimodalityofinfor-
thelatentstateimprovesregimeseparationandtheeco-
|                                   |       |        |      |      |                  |        | mation.        | Financial  | series | rarely | exist          | “alone”: | markets |
| --------------------------------- | ----- | ------ | ---- | ---- | ---------------- | ------ | -------------- | ---------- | ------ | ------ | -------------- | -------- | ------- |
| nomicinterpretationoftransitions. |       |        |      |      | Forexample,atwo- | p      |                |            |        |        |                |          |         |
|                                   |       |        |      |      |                  |        | are constantly | influenced |        | and    | contextualized |          | by tex- |
| regime                            | model | can be | much | more | interpretable    | if one |                |            |        |        |                |          |         |
tualinformation—newspaperarticles,analystreports,
| regime is | associated |     | with “high | inflation, | rising | rates” |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ---------- | ---------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
social-mediaposts,corporateandregulatoryannounce-
| andtheotherwith“lowinflation, |     |     |     | stablerat es”. |     | Repre- |              |         |      |            |     |        |        |
| ----------------------------- | --- | --- | --- | -------------- | --- | ------ | ------------ | ------- | ---- | ---------- | --- | ------ | ------ |
|                               |     |     |     |                |     |        | ments, among | others. | Many | disruptive |     | events | appear |
sentingthiscontextinthemodelstatehelpsavoidspu-
t
|     |     |     |     |     |     |     | first as news | or narratives |     | before | being | fully | reflected |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------- | --- | ------ | ----- | ----- | --------- |
riousorpracticallymeaninglessregimedetections.
|     |     |     |     | o   |     |     | in prices. | This motivates |     | a class | of multimodal |     | repre- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- | --- | ------- | ------------- | --- | ------ |
sentationsthatcombinenumericaltime-seriesdatawith
| Market  | Microstructure |          | Context.      |     | The same | principle |                 |      |          |       |             |     |         |
| ------- | -------------- | -------- | ------------- | --- | -------- | --------- | --------------- | ---- | -------- | ----- | ----------- | --- | ------- |
|         |                |          |               |     |          |           | textual sources | (and | possibly | other | modalities, |     | such as |
| applies | at finer       | temporal | resnolutions, |     | where    | the rele- |                 |      |          |       |             |     |         |
chartimages,sentimentdata,etc.).
vantcontextisnolongermacroeconomicbutstructural.
|                   |        |                          |         |        |          |              | Figure         | 12 provides | an  | overview  | of  | the       | main mul- |
| ----------------- | ------ | ------------------------ | ------- | ------ | -------- | ------------ | -------------- | ----------- | --- | --------- | --- | --------- | --------- |
| At high-frequency |        | time                     | scales, | market | dynamics | are          |                |             |     |           |     |           |           |
|                   |        |                          |         |        |          |              | timodal fusion | strategies, |     | organized |     | according | to the    |
| strongly          | shaped | by market microstructure |         |        |          | effects. In- |                |             |     |           |     |           |           |
stageatwhichinformationfromdifferentsourcesisin-
| traday behavior |          | exhibitstsystematic |            |          | patterns | (opening, |                |            |           |           |             |           |          |
| --------------- | -------- | ------------------- | ---------- | -------- | -------- | --------- | -------------- | ---------- | --------- | --------- | ----------- | --------- | -------- |
|                 |          |                     |            |          |          |           | tegrated       | within the | modeling  | pipeline. |             | Depending | on       |
| midday,         | closing, | and                 | auction    | periods) | as well  | as dis-   |                |            |           |           |             |           |          |
|                 |          | n                   |            |          |          |           | how modalities | are        | combined, |           | integration | can       | occur at |
| tinct liquidity |          | regimes             | throughout | the      | trading  | day. As   |                |            |           |           |             |           |          |
differentprocessingstages:
| a result, | representations |          | designed | for | drift              | and regime |              |     |                                |     |     |     |     |
| --------- | --------------- | -------- | -------- | --- | ------------------ | ---------- | ------------ | --- | ------------------------------ | --- | --- | --- | --- |
| detection | at thesie       | horizons | benefit  |     | from incorporating |            | •            |     |                                |     |     |     |     |
|           |                 |          |          |     |                    |            | Earlyfusion: |     | combinenumericalandtextualrep- |     |     |     |     |
microstructurre-relatedinformation,suchas:
|               |     |                                   |     |     |     |     | resentations | at            | the        | outset, | for example, |      | by con- |
| ------------- | --- | --------------------------------- | --- | --- | --- | --- | ------------ | ------------- | ---------- | ------- | ------------ | ---- | ------- |
|               |     |                                   |     |     |     |     | catenating   | series        | embeddings |         | with         | news | embed-  |
| • Orpderflow: |     | metricsofaggressivenessvs.passiv- |     |     |     |     |              |               |            |         |              |      |         |
|               |     |                                   |     |     |     |     | dings        | corresponding |            | to the  | same         | time | window. |
ityoforders;buy/sellimbalanceintheorderbook;
|     |     |     |     |     |     |     | Each | time window |     | is then | represented |     | by a joint |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ------- | ----------- | --- | ---------- |
[series+text]vector.
e•
| Order-book                               |     | indicators: |     | bid–ask | spreads, | depth |                                            |     |                              |     |     |     |           |
| ---------------------------------------- | --- | ----------- | --- | ------- | -------- | ----- | ------------------------------------------ | --- | ---------------------------- | --- | --- | --- | --------- |
| (volume)availableoneachside,bookchanges; |     |             |     |         |          |       | •                                          |     |                              |     |     |     |           |
|                                          |     |             |     |         |          |       | Intermediatefusion(cross-attention):       |     |                              |     |     |     | usecross- |
| r                                        |     |             |     |         |          |       | attentionmechanismsbetweentimesequencesand |     |                              |     |     |     |           |
|                                          |     |             |     |         |          |       | textsequences.                             |     | Forexample,atransformermodel |     |     |     |           |
Pmodelwhoseparameters(e.g.,intercept,autoregressivematrices,and
|                                              |     |     |     |     |     |             | in which | relevant | news | influence |     | — via | attention |
| -------------------------------------------- | --- | --- | --- | --- | --- | ----------- | -------- | -------- | ---- | --------- | --- | ----- | --------- |
| oftenshockcovariance)dependonalatentregimeSt |     |     |     |     |     | governedbya |          |          |      |           |     |       |           |
—thelearnedrepresentationofmarketdataatthat
| Markovchain, | allowingthemultivariatedynamicstoswitchacross |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
regimes(e.g.,lowvs.highvolatility)[???]. time. Thisallowsthefinalseriesrepresentationto
14
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
bemodulatedbytextualcontent,amplifyingorat- important to account for the structure of interrelation-
tenuatingmovementsaccordingtothepresenceof ships in the market as a dynawmic graph. In multivari-
explanatorynews. ate settings, drifts rarely affect a single asset in isola-
tion—typically,thereisareorganizationofdependen-
• Late fusion: combine only at the end the out-
cies among assets. For example, in a given regime,
puts or alerts originating from detectors special- e
economic sectors form clusters with high intra-cluster
izedineachmodality. Inthiscase,onecouldhave
correlations and lower inter-cluster correlations; dur-
a change detector operating on series and another
ing crisis periods, correlations across most asset pairs
i
analyzing news, and then merge detections (e.g.,
tend to rise simultaneously and may approach unity,
v
flagachangeonlyifbothagree,orusetextascon-
signaling a collapse of diversification and strong sys-
firmation that a quantitative signal corresponds to
temic contagion. Likewise, measures of tail depen-
arealevent). e
dence can change, revealing new channels of extreme
co-movement[? ? ? ? ? ]. Representingeachseriesin-
dividually ignores this cross-information, whereas rep-
EarlyFusion Intermediate LateFusion r
(cross-attention) resenting the system as an evolving graph allows us to
Series Text
xt dt Series Text Series Text captu reco-movementregimes.
xt dt xt dt
Concat Series Text Series Text r
Encoder Encoder Encoder Encoder NormalMarket CrisisMarket
Joint
Encoder Cross-Attention Detector Detector eTech Finance Highcorrelation
zt zt Merge
Alert e
crisis
Figure12:Multimodalfusionstrategiesforintegratingtimeseriesand
textualdata. Earlyfusion: inputsconcatenatedbeforejointencod-
p
ing. Intermediatefusion: separateencoderswithcross-attentionto
exchangeinformation.Latefusion:independentprocessingpipelines
mergedatthedecisionlevel.
Energy Consumer
Sparse,clustered Dense,correlated
These fusion strategies are not meretly conceptual;
Figure13: Dynamiccorrelationnetworks. Normalmarket: stocks
theyareincreasinglyadoptedinrecentresearchonmul-
o clusterbysectorwithsparseinter-sectorconnections.Crisismarket:
timodaltime-seriesanalysisandLargeLanguageMod-
correlationsincreasedramaticallyacrossallsectors(correlationcol-
els(LLMs). Inparticular,studiesonapplyingLLMsto lapse),withdenseinterconnectionreplacingthecommunitystructure.
time series highlight architectnures that perform tempo- Thisregimechangeiscapturedbytime-varyinggraphrepresentations.
ral alignment and information fusion across numerical
series, text, and other sources [? ? ? ]. From the per- ThisintuitionisillustratedinFigure13,contrastinga
spective of regime detectio n, the key advantage is that sector-clusteredcorrelationstructureinnormalperiods
eventsdescribedprimaritlyintext(e.g.,politicalorregu- with the dense, near-uniform dependence typically ob-
latorynewsthatanticipatesamarketshift)caninfluence servedduringcrisisepisodes. Insuchagraph,wetypi-
n
thejointrepresentationbeforethecorrespondingmove- callydefinenodesrepresentingfinancialentities(assets,
mentisfullyreflectedinprices[? ? ? ]. indices, sectors, or countries) and weighted edges en-
As a result, diistances in multimodal space thus cap- codingsomestatisticaloreconomicrelationshipamong
turethecombrinedeffectsofnumericalandnarrativesig- them. Edgesmayreflect,forexample,estimatedcorre-
nals:twoperiodswillonlybeconsideredsimilarifboth lationsorco-movements,measuresofnonlineardepen-
thequa p ntitativepatternsandthenewscontextaresimi- dence (tail copulas), exposure–credit relationships be-
lar.Thisenrichmentcanreducefalsenegatives(missing tweeninstitutions,orcapitalflowsacrossmarkets.Edge
a change because the model did not “understand” that weights vary over time, and regime changes appear as
e
thenewsimpliedanewregime)andalsofalsepositives abrupt or gradual reconfigurations in network topol-
(distinguishing price drops caused by concrete events ogy/weights. Examples include: during a financial-
rfromthoseduetonoise,viathepresenceorabsenceof contagion event, sector clusters may dissolve and all
textualexplanations)[? ? ? ? ]. nodes become highly interconnected; in subtler tran-
P
sitions, a new systemic hub may emerge (an asset or
Market Structure and Inter-Asset Dependencies. Be- sector that starts to leaddynamics), or some links may
yond individual series and external signals, it is also weaken while others strengthen, reshaping the correla-
15
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
tionnetwork. suchasthepredictedprobabilityofremaininginthecur-
The recent literature on Graph Neural Networks rentregimeortheexpectedregimeduration. w
(GNNs) for time series provides a framework for In this sense, latent regime probabilities provide a
learningembeddingsthatencodesuchcomplexspatio- compactandinterpretablesummaryofthesystemstate,
temporal dependencies [? ? ]. Essentially, dynamic- integrating information from multiple variables into a
e
graph models can learn both a representation for each small set of indicators. Figure 14 illustrates this idea:
node (asset) and a representation for the graph as a regime transitions appear as crossovers in the filtered
| wholeateachtimeinterval. |     |     | Thesenetworkembeddings |     |     |     |             |        |          |               |         |      |     |
| ------------------------ | --- | --- | ---------------------- | --- | --- | --- | ----------- | ------ | -------- | ------------- | ------- | ---- | --- |
|                          |     |     |                        |     |     |     | probability | paths, | yielding | i drift-aware | signals | that | are |
capturethecurrentstateofthefinancialstructure—for suitableforbothdetectionandadaptation.
v
| example, they     | may | encode    | that there | are     | currently | two    |     |     |     |     |     |     |     |
| ----------------- | --- | --------- | ---------- | ------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| weakly correlated |     | clusters, | or that    | a given | asset     | is ab- |     | xt  |     |     |     |     |     |
e
normallyconnectedtoothers,indicatingstress. Regime Bull Crisis Bear Recovery
changesthenmanifestaschangesintheseembeddings:
|     |     |     |     |     |     |     | Observed |     | 1τ  | 2τ  | 3τ  |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Series
| a shift indicating |     | that the | graph topology |     | has changed |     |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
r
significantly.
t
P(St)
| Recent   | financial          | models | combine | this | graph-based |     |     |   1    |     |     |     |     |     |
| -------- | ------------------ | ------ | ------- | ---- | ----------- | --- | --- | ------ | --- | --- | --- | --- | --- |
| approach | with multimodality |        | (prices | +    | indicators  | +   |     | Regime |     |     |     |     |     |
Probabilities r
| news), producing  |     | unified      | representations |      | that account |     |     |     |     |     |     |     |     |
| ----------------- | --- | ------------ | --------------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                   |     |              |                 |      |              |     | e   |     |     |     |     |     | t   |
| for relationships |     | among assets | together        | with | economic     |     |     | 0   |     |     |     |     |     |
P(Bull)
context [? ]. In practice, node and graph embeddings P(Crisis)
P(Bear)
| can serve | directly | as inputs | to change | detectors |     | (Sec- |     |     |     |     |     |     |     |
| --------- | -------- | --------- | --------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
e
tion4)—forexample,bymonitoringthetimeseriesof Figure 14: Regime probabilities from a latent-state model (e.g.,
thegraphembeddingtodetectbreaksinthecorrelation HMM).Top: observedserieswithregime-coloredbackground. Bot-
|     |     |     |     |     |     |     | tom: | filteredprobabilitiesP(St |     | | x1:t)foreachregime. |     | Transitions |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------- | --- | --------------------- | --- | ----------- | --- |
network — or as additional context for regime-based pmanifestasprobabilitycrossoversatchangepointsτ1,τ2,τ3. These
adaptation mechanisms (Section 5), guiding models to probabilities serve as drift-aware features for detection and adapta-
| treatgroupsofaffectedassetsjointly[? |     |     |     |     |         |        | tion. |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
|                                      |     |     |     | ?   | ? ? ? ? | ? ? ]. |       |     |     |     |     |     |     |

|                      |     |          |        |            |     |     | From | a Bayesian |     | standpoint, | models | such | as  |
| -------------------- | --- | -------- | ------ | ---------- | --- | --- | ---- | ---------- | --- | ----------- | ------ | ---- | --- |
| 3.3. Representations |     | Oriented | Toward | Robustness | t   | and |      |            |     |             |        |      |     |
BayesianOnlineChangepointDetection(BOCPD)and
Interpretation
o
itsnon-parametricextensionsprovideanalternativeyet
This subsection introduces representation strategies related representation: they estimate, at each time t,
| oriented toward |     | robustness | and | interpretability. |     | The |                                                     |     |     |     |     |     |     |
| --------------- | --- | ---------- | --- | ----------------- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                 |     |            | n   |                   |     |     | theposteriordistributionoftherun-length(timeelapsed |     |     |     |     |     |     |
goal is to construct representations that remain stable sincethelastchange)andofcurrentmodelparameters
under distribution shifts while providing economically [? ? ? ? ? ? ]. In practice, BOCPD computes,
meaningfulsignalsofregimechanges.   Anaturalwayto at each new datum, a probability p(changepoint) t in-
achievethisistomakeregimesexplicitintherepresen- dicating how likely it is that a change occurred at that
t
tation itself, so that changes correspond to transitions point, and maintains parameter distributions under the
n
| betweeninterpretablesystemstates. |     |     |     |     |     |     | no-changehypothesis. |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
Thetimeseriesofthesechangeprobabilitiesandstate
Latent-State and i Regime-Based Representations.. statistics (for example, the posterior distribution of the
Oneprominentclassofapproacheswithinthisperspec- currentlyactivelevelorvariance)become, themselves,
r
tive relies on latent-state models with explicit regimes. rich representations of the degree of change perceived
Classical p regime-switching models—such as HMMs, by the model. It is like a continuously updated “evi-
MS-VAR,orregimeGARCH—representthesystemas dencepanel”:ifp(changepoint)risesabruptly,wehave
t
a finite set of discrete states, each associated with dis- astrongindicationofdrift;ifuncertaintyaboutparam-
e
tinct statistical properties, and define transition proba- etersincreases,thispointstostructuralinstability.
bilitiesamongthesestates[? ? ? ? ]. In summary, latent-state models (whether classical
r From a representation standpoint, fitting such a HMMs or online Bayesian methods) provide regime-
model amounts to mapping each time point to a vec- orientedrepresentations—mappingdataintoprobabil-
P
torofregime-membershipprobabilities,obtainedeither itiesofscenarios—thatbothrobustlycapturerelevant
inrealtime(filtered)oraposteriori(smoothed). These changes and enhance interpretability (since they make
vectors may be complemented by derived quantities, explicit “I am X% in regime A and Y% in regime B
16
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
now”). cent studies show that causality-inspired models can
yield more robust forecasts prwecisely in turbulent peri-
Causal and Invariant Representations.. While this ods,whenspuriousrelationshipschangeandonlystruc-
approach achieves robustness by explicitly modeling tural links remain[? ? ? ? ? ]. This suggests that
regimetransitions,acomplementarylineofworkseeks invariantrepresentationsnotonlyhelpdetection(reduc-
e
robustnessatadeeperlevel: byidentifyingrepresenta- ingnoisyfalsealarmsduetosuperficialvariations)but
tions that remain valid across changing environments. also serve as a basis for adaptive models that maintain
Thismotivatesagroupoftechniquesfocusedoncausal performanceunderdrift.
i
and invariant representations. The dataset-shift litera-
v
ture in classification emphasizes that many drifts arise Foundation Models and Universal Embeddings..
fromchangesinconfoundersorinthesurroundingenvi- Alongthesamelineofpursuingrobustandtransferable
ronment—altering P(X) or jointly P(X,Y)—while cer- embeddingse, recent work explores time-series founda-
tain underlying causal relationships remain stable over tion models as providers of universal embeddings. In-
time[? ? ? ? ? ]. Forexample,aninvestmentstrategy spiredbythesuccessoflargepre-trainedmodelsinlan-
r
mayfailinanewregimebecauseitreliedonaspurious guage and vision, researchers have examined whether
correlationthatheldhistoricallybutlatervanished,even large- scaletime-seriesmodels,pre-trainedonheteroge-
though the fundamental causal drivers of returns per- neous collections of series, can serve as backbones for
r
sisted (e.g., a macroeconomic factor whose effect was diversefinancialtasks[? ? ]. Theideaisthataneural
previouslymasked). emodeltrainedonawiderangeofdomainsandfrequen-
Inresponse,aclassofmethodshasemergedthataims cieslearnsembeddingsofwindowsorentireseriesthat
to learn features invariant to environmental changes, carrytemporalknowledgeinageneralway—capturing
e
drawing on ideas from Invariant Risk Minimization seasonalpatterns,typicalreactionstoshocks,etc.—and
(IRM) [? ] and related frameworks. Rather than that these embeddings can later be specialized to fi-
optimizing only average predictive performance on nance.
p
historical data, these approaches impose constraints Instead of training a representation model from
or regularizers that penalize excessive dependence scratch on often limited market- or asset-specific data,
on environment-specific components, enco uraging the one can adopt strategies such as: (1) using the pre-
model to rely on more stable and transfe t rable relation- trained foundation model as a fixed feature extractor
ships[? ? ? ? ]. andapplyingchangedetectorstotheembeddingsitgen-
o
In financial contexts, this amounts to seeking repre- erates; or(2)performinglightadaptation(fine-tuning),
sentationsthatprivilegestructuraldrivers(e.g.,riskpre- adjusting only the final layers to specialize the repre-
mia genuinely linked to econnomic fundamentals) and sentation to the financial domain [? ? ? ]. Both ap-
downweight correlations that, although effective in a proaches aim to leverage the inductive bias contained
given regime, are peculiar to that environment and do in large-scale pretraining—for example, a foundation
notpersistoutsideit. Asa nexample, imaginearepre- modelmayalready“know”howtorepresentmacrocy-
sentation of equities thatt emphasizes fundamental fac- clesorcommonshocks;eveniftheassetinquestionhas
tors (valuation metrics, earnings growth, etc.) and is never experienced a given regime in the available his-
n
lesssensitivetoshort-termtechnicalfactorswhosesign tory,themodelmayrecognizeanalogouspatternsfrom
may flip when the regime changes — such a represen- other contexts and thus generalize better under moder-
tationtendstobiemorerobusttomarketshifts,because ateshifts.
fundamentals r persist while transient technical patterns From a pipeline perspective, embeddings provided
maydisappear. byfoundationmodelsenterasenrichedinternalsignals,
Inprpactice,buildinginvariantrepresentationsmayin- representingtheseriesthroughvectorsofadvancedfea-
volve: (i) selecting features whose relationship with tures. Thisisarapidlyevolvingarea;althoughpromis-
returns remains stable across subperiods or regimes ing, it requires careful assessment of whether patterns
e
(identifying“resilient”variableswhoseestimatedcoef- learned from other domains apply to specific financial
ficients vary little between regimes); (ii) training em- contexts,aswellasmechanismsforupdatingthefoun-
rbeddingswithobjectivesthatenforcepredictiveconsis- dationmodelwhenthevery“universe”ofseriesevolves
tencyacrossmultipleenvironments(e.g.,differentmar- (for example, new data types or post-2020 dynamics).
P
ket windows); (iii) integrating with latent-state models Well-designed representations not only increase sensi-
that make environments/regimes explicit and penalize tivity and timeliness in identifying changes, but also
excessive variation in causal effects across states. Re- facilitate the economic interpretation of the resulting
17
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
regimes—sincetheyconnecteachdriftalarmtounder- 4. ChangeDetection
| standableinternalsignalsandpotentialstructuralmech- |     |     |     |     |     |     |     |     |     |     | w   |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anisms.
|     |     |     |     |     |     |     | This | Section | addresses | the | research | question: | How |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------- | --------- | --- | -------- | --------- | --- |
candriftsindatabeautomaticallydetectedovertime?
|             |            |     |     |             |             |     | To answer | it, | we organize |     | the discussion |     | around the |
| ----------- | ---------- | --- | --- | ----------- | ----------- | --- | --------- | --- | ----------- | --- | -------------- | --- | ---------- |
| 3.4. Design | Guidelines |     | for | Drift-Aware | Representa- |     |           |     |             |     |                |     |            |
e
| tions |     |     |     |     |     |     | main methodological |               |     | paradigms    | used | in practice. | We    |
| ----- | --- | --- | --- | --- | --- | --- | ------------------- | ------------- | --- | ------------ | ---- | ------------ | ----- |
|       |     |     |     |     |     |     | first cover         | retrospective |     | segmentation |      | methods,     | which |
Table5summarizespracticalchoicesforrepresenta- identify changes after observing a full data window
i
tionandmonitoringunderdifferentdriftscenarios,link-
|     |     |     |     |     |     |     | (4.1). We | then | move | to sequential |     | (online) | monitor- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ---- | ------------- | --- | -------- | -------- |
v
ingobservabledriftpatternstoconcretesignalfamilies ing techniques, designed to trigger alarms as data ar-
| and failure | modes. | In  | practice, | representation |     | design |     |     |     |     |     |     |     |
| ----------- | ------ | --- | --------- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
rive(4.2),followedbyBayesianapproachesthatmodel
e
canbeguidedbyasmallnumberofrecurringsituations: regimechan gesprobabilistically(4.3). Thesectionfur-
therexaminesdetectorsoperatinginlearnedrepresenta-
| • Abrupt | shocks | (e.g., | crashes, |     | policy | announce- |     |     |     |     |     |     |     |
| -------- | ------ | ------ | -------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
tionspacesandout-of-distributionsettings(4.4),aswell
r
ments): monitor short-window statistics (mean, as methods that target changes in multivariate depen-
| variance) |     | or regime | probabilities |     | from | HMMs. |     |     |     |     |     |     |     |
| --------- | --- | --------- | ------------- | --- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
dence structures(4.5).
These signals react quickly and are suitable for rTosynthesizetheseperspectives,4.6providesacom-
| early | warning, | but | may | trigger | false alarms | under |     |     |     |     |     |     |     |
| ----- | -------- | --- | --- | ------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
pactoverviewthatlinksthetypesofchangedefinedby
temporarynoise. ethetaxonomicaxestosuitabledetectionstrategies.This
|     |     |     |     |     |     |     | overview | serves | as a | practical | guide | for method | selec- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---- | --------- | ----- | ---------- | ------ |
•
| Gradual | or  | long-term |     | changes | (e.g., | persistent |     |     |     |     |     |     |     |
| ------- | --- | --------- | --- | ------- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
tion,whilealsoemphasizinghowthechoiceoftheob-
| volatility | increases): |     | use | longer | rolling | windoews |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | --- | ------ | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
servedsignalandtherepresentationspaceshapesdetec-
ormulti-scaleembeddingstotrackslowdrifts,ac-
|     |     |     |     |     |     |     | tor behavior | and | interpretability |     | [?  | ? ? | ]. Together, |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------- | --- | --- | --- | ------------ |
ceptinglaterdetectioninexchangeforstability.
ptheseelementsconnectmethodologicaldecisionstothe
|     |     |     |     |     |     |     | effective | detection | of  | different | forms | of drift | in real- |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --- | --------- | ----- | -------- | -------- |
• Frequentregimeswitching:adoptlatent-statemod-
worlddata.
| els | (HMM, | MS-VAR) | and | track | regime | probabil- |     |     |     |     |     |     |     |
| --- | ----- | ------- | --- | ----- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |

| ities | or expected |     | durations; | performance |     | depends |     |     |     |     |     |     |     |
| ----- | ----------- | --- | ---------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
oncorrectlyspecifyingthenumbero t fregimes. 4.1. Segmentation(retrospectiveoptimization)
o
| •                            |     |                 |     |                   |                 |     | Segmentationmethodsseektopartitionthehistorical |     |            |     |         |                 |     |
| ---------------------------- | --- | --------------- | --- | ----------------- | --------------- | --- | ----------------------------------------------- | --- | ---------- | --- | ------- | --------------- | --- |
| Asset-                       | or  | sector-specific |     | drift:            | use dependency- |     |                                                 |     |            |     |         |                 |     |
|                              |     |                 |     |                   |                 |     | timeseriesX                                     |     | = X ,...,X |     | ,whereT | denotesthetotal |     |
| basedrepresentations(graphs, |     |                 |     | taildependence)to |                 |     |                                                 | 1:T | 1          | T   |         |                 |     |
correlantions numberofobservationsandX t theobservationattimet,
| detect | changes | in  |     | and | contagion | pat- |     |     |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
intoapproximatelystationarysegments,retrospectively
| terns, | noting | that | estimates | may | become | unstable |            |     |             |     |           |      |              |
| ------ | ------ | ---- | --------- | --- | ------ | -------- | ---------- | --- | ----------- | --- | --------- | ---- | ------------ |
|        |        |      |           |     |        |          | optimizing | the | changepoint |     | locations | that | best explain |
insmallsamples.
|     |     |     |     |     |     |     | the data.    | In this | setting,   | it  | is assumed | that    | the series |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ---------- | --- | ---------- | ------- | ---------- |
| •   |     |     |     |     |     |     | is generated | by      | a sequence | of  | distinct   | regimes | indexed    |
Externallydrivencthanges(e.g.,news,narratives):
combine prices with textual data through multi- byr,eachassociatedwithaprobabilitydistribution(or
n
|        |             |     |            |            |     |             | model)P(X              | |θ  | ),whereθ | denotesthesetofparameters |     |     |     |
| ------ | ----------- | --- | ---------- | ---------- | --- | ----------- | ---------------------- | --- | -------- | ------------------------- | --- | --- | --- |
| modal  | embeddings  |     | to capture | signals    |     | before they |                        | r   |          | r                         |     |     |     |
|        |             |     |            |            |     |             | characterizingregimer. |     |          | Eachregimeisapproximately |     |     |     |
| appear | in returns, |     | while      | accounting | for | alignment   |                        |     |          |                           |     |     |     |
andscalingiissues. stationarywithinitscorrespondingsegment,andregime
changescorrespondtobreaksintheunderlyingdistribu-
r
| •                                        |     |     |     |     |     |     | tionor,equivalently,intheparametersθ |     |     |     |     | .   |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | --- |
| Needforrobustnessacrossmarketconditions: |     |     |     |     |     | fa- |                                      |     |     |     |     | r   |     |
voprinvariantorcausalrepresentationstoreducere- In some cases, segmentation is applied not directly
liance on regime-specific correlations, at the cost to X, but to representations Z = f(X) or Z = f(X,Y)
ofdiscardingsomeshort-termpredictivesignals. (forexamplelatentfactorsorfeaturesextractedfromre-
e
turnsandcovariates),sothatonesearchesforbreaksin
Taken together, the checklist and table emphasize a P(Z)overtime.Segmentationalgorithmsthenapplyop-
rsimple principle: the representation should match the timization routines (exhaustive or approximate) to find
dominant form of drift one expects to face. Fast sig- the optimal partition in terms of a global cost criterion
P
| nals favor | sensitivity, |     | stable | embeddings | favor | robust- | [? ? ? ]. |     |     |     |     |     |     |
| ---------- | ------------ | --- | ------ | ---------- | ----- | ------- | --------- | --- | --- | --- | --- | --- | --- |
ness, and interpretable regimes favor control and diag- A classical approach is the minimization of an ad-
| nosis. |     |     |     |     |     |     | ditivecostcriterion. |     | Onedefinesanintra-segmentcost |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----------------------------- | --- | --- | --- | --- |
18
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table5:Designchecklistlinkingdrifttaxonomyaxestorepresentationchoices.
w
Driftcharacteristic Signal/featurefamily Early-warning indica- Principalfailuremode
tor
Abruptdrift Short-windowstatistics, Sharp changes in mean, False alarms due to tran-
e
|     |     |     |     | BOCPD,   | HMM | proba- | variance,   | or  | regime | sientnoise |     |     |     |
| --- | --- | --- | --- | -------- | --- | ------ | ----------- | --- | ------ | ---------- | --- | --- | --- |
|     |     |     |     | bilities |     |        | probability |     |        |            |     |     |     |
Gradual or secular Multi-scale statistics, Slow but persistent fea- iDelayeddetection
| drift |     |     |     | embeddings |     |     | turedrift |     |     |     |     |     |     |
| ----- | --- | --- | --- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
v
/
Regimeswitching HMM MS-VAR latent Probability crossovers, Regimemisspecification
|     |     |     |     | states |     |     | durationshifts |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
e
Localized or sectoral Graph embeddings, tail Rewiringofdependency Estimationinstability
| drift |     |     |     | dependence |     |     | clusters |     |     |     |     |     |     |
| ----- | --- | --- | --- | ---------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Narrative-drivendrift Multimodal (price + Text-led dirvergence be- Alignment and modality
|     |     |     |     | text)embeddings |     |     | forepricemoves |     |     | noise |     |     |     |
| --- | --- | --- | --- | --------------- | --- | --- | -------------- | --- | --- | ----- | --- | --- | --- |
Spurious correlation Invariant / causal repre- Stability acrossenviron- Loss of short-term pre-
| drift |     |     |     | sentations |     |     | mentrs |     |     | dictability |     |     |     |
| ----- | --- | --- | --- | ---------- | --- | --- | ------ | --- | --- | ----------- | --- | --- | --- |
e
thatusuallycoincideswithanegativelog-likelihood,for
example
eAlgorithm1:PELT:PrunedExactLinearTime
|        | C(a,b)≈−logp                    |     |     | (cid:0) |θˆ | (cid:1) |      |     |                   |     |     |          |                  |     |
| ------ | ------------------------------- | --- | --- | ----------- | ------- | ---- | --- | ----------------- | --- | --- | -------- | ---------------- | --- |
|        |                                 |     |     | X a:b       | a:b ,   |      |     |                   |     | =(x |          |                  |     |
|        |                                 |     |     |             |         |      |     | Input:Timeseriesx |     | 1:n | 1 ,...,x | n );costfunction |     |
| whereX | isthedatablockinthesegmentandθˆ |     |     |             |         | are  |     | C(·);penaltyβ     |     |     |          |                  |     |
|        | a:b                             |     |     |             |         | pa:b |     |                   |     |     |          |                  |     |
Output:Setofchangepointlocations
| parameters                                        | estimated |            | under the | hypothesis | that,      | in that |     |          |            |         |           |            |      |
| ------------------------------------------------- | --------- | ---------- | --------- | ---------- | ---------- | ------- | --- | -------- | ---------- | ------- | --------- | ---------- | ---- |
|                                                   |           |            |           |            |            |         |     | T        | ={τ ,...,τ | }       |           |            |      |
| interval,thedistributionP(X)(orP(Z))isstationary. |           |            |           |            |            |         | A   |          | 1          | K       |           |            |      |
|                                                   |           |            |           |            |            |         |     | F(0)←−β; | //         | Optimal | cost      | up to time | 0    |
| costisthenaddedforeachbreakintroduced (apenalty   |           |            |           |            |            |         |     | 1        |            |         |           |            |      |
|                                                   |           |            |           |            |            |         |     | R ←{0};  |            | //      | Candidate | set of     | last |
| as a function                                     | of        | the number | of        | segments). | Algorithms |         |     | 2 0      |            |         |           |            |      |
t
| suchasBai&Perron[? |            |     | ] implementexhaustivesearch |               |     |           |     | changepoints |     |              |     |            |     |
| ------------------ | ---------- | --- | --------------------------- | ------------- | --- | --------- | --- | ------------ | --- | ------------ | --- | ---------- | --- |
|                    |            |     |                             | o             |     |           |     | 3 cp(0)←∅;   | //  | Changepoints |     | up to time | 0   |
| for multiple       | structural |     | breaks                      | by minimizing |     | the total |     |              |     |              |     |            |     |
fort=1tondo
| penalizedcost. |     |     |     |     |     |     |     | 4   |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AnothermoreefficientmethodsuchasPELT(Pruned // Find optimal previous changepoint
|     |     |     | n   |     |     |     |     |               |     | (cid:2) |          | (cid:3) |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ------- | --- |
|     |     |     |     |     |     |     |     | (F(t),τ∗)←min |     |         | F(τ)+C(x | )+β     |     |
Exact Linear Time) [? ], sum marized in Algorithm 1, 5 τ∈Rt−1 τ+1:t
|                           |     |     |     |           |      |         |     | cp(t)←cp(τ∗)∪{τ∗}; |     |     |     | // Store | best |
| ------------------------- | --- | --- | --- | --------- | ---- | ------- | --- | ------------------ | --- | --- | --- | -------- | ---- |
| use a dynamic-programming |     |     |     | recursion | with | pruning |     | 6                  |     |     |     |          |      |
configuration
rulesthatexploittheadditi vestructureofthecostfunc-
tion C to discard suboptimal candidates, achieving lin- // Prune: remove candidates that
t
|                   |     |                                 |         |           |           |      |     | cannot    | be  | optimal       |     |               |     |
| ----------------- | --- | ------------------------------- | ------- | --------- | --------- | ---- | --- | --------- | --- | ------------- | --- | ------------- | --- |
| ear computational |     | cost                            | in many | practical | settings, | with |     |           |     |               |     |               |     |
|                   |     | n                               |         |           |           |      |     | 7 R ←{τ∈R |     | ∪{t}|F(τ)+C(x |     | τ+1:t )≤F(t)} |     |
| thepenaltyβcontro |     | llingthenumberofdetectedchange- |         |           |           |      |     | t         | t−1 |               |     |               |     |
end
| points.    |                   |          |           |          |                  |      |     | 8             |     |     |         |              |     |
| ---------- | ----------------- | -------- | --------- | -------- | ---------------- | ---- | --- | ------------- | --- | --- | ------- | ------------ | --- |
|            |                   |          |           |          |                  |      |     | T ←cp(n)\{0}; |     | //  | Extract | changepoints |     |
| Once       | the segmientation |          | framework |          | and optimization |      |     | 9             |     |     |         |              |     |
|            |                   |          |           |          |                  |      |     | (exclude      | 0)  |     |         |              |     |
| algorithms | are               | defined, | a key     | modeling | choice           | con- |     |               |     |     |         |              |     |
r
10 returnT
| cerns which | aspect | of  | the data-generating |     | distribution |     |     |     |     |     |     |     |     |
| ----------- | ------ | --- | ------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Complexity:O(n)averagecasewithpruning,O(n2)
| istargeptedbythecostfunction.                     |     |     |     | Segmentationmethods |     |     |     | 11                 |     |               |     |             |     |
| ------------------------------------------------- | --- | --- | --- | ------------------- | --- | --- | --- | ------------------ | --- | ------------- | --- | ----------- | --- |
| thereforerequirespecifyingwhetherchangesaresought |     |     |     |                     |     |     |     | worstcase          |     |               |     |             |     |
|                                                   |     |     |     |                     |     |     |     | 12 Costfunctions:C |     | (meanshift),C |     | (variance), |     |
in the mean (location parameters), variance or covari- L2 Gauss
| e                                                  |     |     |     |     |     |     |     | C (nonparametric) |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- |
| ancestructure,orinthefulldistributionofP(X)orP(Z). |     |     |     |     |     |     |     | RBF               |     |     |     |     |     |
Penalty:β=c·logn(BIC-type);higherβ⇒fewer
13
| The choice |     | of contrast | statistic | directly | determines |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
changepoints
rthe type of changepoint that can be detected. Mean- Typicaluse:Offlinesegmentation;multiplebreaks;
14
| based contrasts |     | primarily | identify | level | shifts, | while |     |     |     |     |     |     |     |
| --------------- | --- | --------- | -------- | ----- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
longseries
P
| variance-based |     | contrasts | are | sensitive | to changes | in  |     | References:[??] |     |     |     |     |     |
| -------------- | --- | --------- | --- | --------- | ---------- | --- | --- | --------------- | --- | --- | --- | --- | --- |
15
| volatility.      | More | general   | distributional |              | contrasts, | such      |     |     |     |     |     |     |     |
| ---------------- | ---- | --------- | -------------- | ------------ | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| as density-based |      | measures, |                | divergences, |            | or energy |     |     |     |     |     |     |     |
19
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
distances, allow the detection of broader structural timeseries.
changes. Inpractice,segmentationoftenreliesonsim- w
ple within-segment models, including constant means, 4.2. SequentialMethods(onlinemonitoring)
linear regressions, or AR/ARMA processes, with Sequential methods perform detection in real time,
changepoints corresponding to shifts in the regime- examining the series continuously as new data arrive.
e
specificparametersθ . In probabilistic terms, one typically assumes a “pre-
r
An important characteristic is that segmentation change” distribution P (X) and a “post-change” distri-
0
methods provide a set of estimated changepoints for butionP (X)(or,moreagnostically,oneseekstodetect
1 i
the entire series (off-line mode), being suitable for ex- when P (X) starts to differ from P (X)). The
recent v baseline
ploratory analysis or historical validation of regimes. goal is to trigger an alarm as quickly as possible af-
They do not operate in real time, but often offer high terachangein P(X)occurs,whilecontrollingthefalse
precision in ex post localization of significant changes alarmrate. T e hesemethodstypicallymaintainawindow
in P(X) or its parameters, especially when combined oradaptivemodelandapplyrecurrentstatisticaltests.
withrobuststoppingcriteria(penalties)thatavoidover- AclassicexampleistheCUSUM(CumulativeSum)
r
segmentation (inserting breaks where there is only testanditsvariants,detailedintheAlgorithm2,which
noise)[??].Forexample,techniquessuchastheBarry monit ortheaccumulateddeviationofastatistic(forex-
&Hartiganmethod[? ] usepartitionmodelsandpriors amplethemeanofX orofaresidual)relativetoarefer-
r t
for optimal segmentation with uncertainty, obtaining a ence value associated with P (X), signaling a change
0
posterior distribution over partitions of the series into ewhen this deviation exceeds a threshold. The choice
approximatelystationaryblocksintermsofP(X). of the decision threshold and reference value (and the
Beyond these canonical algorithms, there is a broad implied false-alarm/delay trade-off). In its likelihood-
e
family of techniques that build upon segmentation as ratio formulation, CUSUM accumulates contrasts of
a basic block. Non-parametric extensions, such as theformlog p1(Xt),approximatingoptimaldetectionbe-
p0(Xt)
E-Divisive, energy-distance segmentation, anpd kernel tweenP
0
(X)andP
1
(X)undercertainassumptions. An-
changepointmethods(kernelCPD),allowthedetection otherexampleistheapproachofPage–Hinkley, which
ofbreaksincomplexdistributionsP(X)orP(Z)without statesthatderivativesfollowasimilarlogic[? ].
specifying an explicit parametric model, a nd are par- Another common formulation compares two win-
ticularlyusefulforfinancialserieswithhteavytailsand dows: arecentslidingwindow, associatedwithanem-
asymmetries. pirical distribution P (X), versus a past window or
o recent
Multi-scale methods based on random sub-intervals, long-termestimate P (X). Onlinetwo-sampletest
baseline
suchasWildBinarySegmentation(WBS)anditsexten- techniques,suchasADWINandotherdriftdetectorsin
sion WBS2, explore a large nnumber of candidate seg- data streams, continuously compute the statistical dif-
ments to locate multiple changepoints, including sce- ference between these empirical distributions (e.g., in
narios with frequent breaks and very short spacing be- terms of mean, variance, or non-parametric measures
tweendrifts[? ? ]. ofdivergence)andperformsequentialhypothesistests,
Narrowest-Over-Thretshold (NOT), in turn, priori- shrinking or expanding windows as needed to confirm
tizes the smallest interval whose contrast exceeds a a change in P(X). Algorithms such as DDM, EDDM,
n
threshold, producing well-localized estimates of fea- etc.,areusedinthedata-streamliteraturetomonitorer-
turessuchasjumpsinthemeanorchangesinslopeand rormetricsofaclassifierovertime–thatis, anaggre-
generalizingtodiifferenttypesofstructuralchange[? ]. gatedlossfunctionL
t
=ℓ(Y
t
,Yˆ
t
)whenpairs(X
t
,Y
t
)are
In summarry, segmentation methods frame change- available–andtriggeralarmswhenthereisasignificant
point detection as an offline optimization problem, in increaseinthesemetrics–indicatingconceptdrift(strict
whichaptimeseriesisretrospectivelypartitionedintoap- sense)inP(Y | X)[? ? ? ].
proximatelystationaryregimesbyminimizingapenal- A central challenge in these methods is controlling
izedglobalcost. Theireffectivenessdependsjointlyon the trade-off between rapid detection and false alarms.
e
thechoiceofrepresentation(X orZ),theintra-segment Thresholdsthataretoosensitiveleadtofrequentalarms
cost function, and the penalty controlling model com- duetorandomfluctuationsinP(X);highthresholdsare
rplexity. As a result, segmentation provides a flexible slow to react to real changes. For this reason, several
and principled way to identify structural breaks and techniquesuseresultsfromsequentialstoppingtheory:
P
regimeboundariesinhistoricaldata,servingasafoun- forexample,definingthresholdsthatguaranteeacertain
dational tool for exploratory analysis, regime charac- level of ARL (Average Run Length) for false detec-
0
terization, and downstream modeling in non-stationary tions – that is, on average, how long a change-free pe-
20
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
|     |     |     |     |     |     | riodunder | P 0 (X)lastsuntilafalsealarmoccurs. |     |     |     |     | Well- |
| --- | --- | --- | --- | --- | --- | --------- | ----------------------------------- | --- | --- | --- | --- | ----- |
knownsequentialmethodssucwhasShiryaev–Robertsor
|     |     |     |     |     |     | multivariate | CUSUM |      | calibrate | thresholds |     | via the de- |
| --- | --- | --- | --- | --- | --- | ------------ | ----- | ---- | --------- | ---------- | --- | ----------- |
|     |     |     |     |     |     | siredARL     | [?    | ? ]. |           |            |     |             |
0
|     |     |     |     |     |     | Both | approaches | are | necessary | in  | financial | applica- |
| --- | --- | --- | --- | --- | --- | ---- | ---------- | --- | --------- | --- | --------- | -------- |
e
tions,becauseonlinemonitoringisusedtodetectstruc-
|     |     |     |     |     |     | turalchangesinproduction: |     |     |     | forexample, | warningthat |     |
| --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ----------- | ----------- | --- |
ariskmodelhasstartedtofailbecauseP(X)orP(X,Y)
i
|     |     |     |     |     |     | haschanged. | Sothatportfoliocorrelations,thedistribu- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ---------------------------------------- | --- | --- | --- | --- | --- |
v
tionofP&L,ortherateofVaRviolationsarenolonger
compatiblewiththehistoricalregime.
effie
|     |     |     |     |     |     | Some | cient | implementations |     | (for | example, | using |
| --- | --- | --- | --- | --- | --- | ---- | ----- | --------------- | --- | ---- | -------- | ----- |
Algorithm 2: CUSUM for Mean Shift Detec- low-complexitynon-parametrictests)allowdetectorsto
| tion |     |     |     |     |     | runinstreamingonmarketdata. |     |     |     | Itisworthnotingthat |     |     |
| ---- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ------------------- | --- | --- |
r
Input:Datastreamx ,x ,...,x ;in-controlmeanµ ; many sequential methods assume some knowledge of
|     |                                     |     | 1 2 | n   | 0   |         |           |       |     |          |      |             |
| --- | ----------------------------------- | --- | --- | --- | --- | ------- | --------- | ----- | --- | -------- | ---- | ----------- |
|     | standarddeviationσ;thresholdh;slack |     |     |     |     | P (X) ; |           |       |     |          |      |             |
|     |                                     |     |     |     |     | 0 in    | contrast, | works | on  | drift in | data | streams aim |
parameterk(typically0.5)
|     |                                       |     |     |     |     | to be more               | agnostic, | using | sliding-window |            |     | approaches |
| --- | ------------------------------------- | --- | --- | --- | --- | ------------------------ | --------- | ----- | -------------- | ---------- | --- | ---------- |
|     | Output:Detectiontimeτor∅(nodetection) |     |     |     |     | r                        |           |       |                |            |     |            |
|     |                                       |     |     |     |     | andempiricallycomparingP |           |       |                | (X)versusP |     | (X)        |
|     |                                       |     |     |     |     |                          |           |       |                | recent     |     | baseline   |
|     | S+←0;                                 |     |     |     |     | eordirectlymonitoring    |           |       |                |            |     |            |
1 // Cumulative sum for upward P recent (Y | X)throughpredictive
|     | shifts |     |     |     |     | performance. |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
2 S−←0; // Cumulative sum for downward In practice, sequential methods are the backbone of
|     | shifts |     |     |     | e   |                  |     |       |            |     |         |        |
| --- | ------ | --- | --- | --- | --- | ---------------- | --- | ----- | ---------- | --- | ------- | ------ |
|     |        |     |     |     |     | many operational |     | tools | in finance | and | machine | learn- |
fort=1tondo
| 3   |           |            |     |     |              | ing for                                    | data streams. |     | In risk | monitoring, |     | variants of |
| --- | --------- | ---------- | --- | --- | ------------ | ------------------------------------------ | ------------- | --- | ------- | ----------- | --- | ----------- |
|     | z ← (x    | − µ ) / σ; |     | //  | Standar dize |                                            |               |     |         |             |     |             |
| 4   | t t       | 0          |     |     |              |                                            |               |     |         |             |     |             |
|     |           |            |     |     | p            | CUSUM,EWMA,andGLR(generalizedlikelihoodra- |               |     |         |             |     |             |
|     | o bse r v | at i o n   |     |     |              |                                            |               |     |         |             |     |             |
S+←max(0,S++z tio tests) are applied to P&L series, counts of VaR vi-
| 5   |     |     | −k); | // Update | upward |           |                     |     |     |           |     |              |
| --- | --- | --- | ---- | --------- | ------ | --------- | ------------------- | --- | --- | --------- | --- | ------------ |
|     |     |     | t    |           |        | olations, | or volatility-model |     |     | residuals | to  | build early- |
CUSUM
S−←max(0,S−−z −k); //   Update warning dashboards that trigger limit reviews or stress
| 6   |     |     | t   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
downward CUSUM tests whenever the statistic crosses pre-defined control
t
|     | ifS+>horS−>hthen |     |     |     |     |                               |     |     |     | =   |                  |     |
| --- | ---------------- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | ---------------- | --- |
| 7   |                  |     |     |     |     | bands,indicatingthatP(X)orP(Z |     |     |     |     | f(X))haschanged. |     |
|     | returnτ=t;       |     |     | o   |     |                               |     |     |     |     |                  |     |
8 // Alarm: change In terms of algorithmic standpoint, sequential pro-
|     | detected |     |     |     |     | cedures | based | on GLR | and | SPRT, | as well | as control |
| --- | -------- | --- | --- | --- | --- | ------- | ----- | ------ | --- | ----- | ------- | ---------- |
end
| 9   |     |     | n   |     |     | schemesonspreadandliquidityindicators,actas“kill- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
10 end switches” that halt strategies when recent behavior be-
| 11  | return∅; |     | //  | No change | detected |                    |     |      |     |            |         |     |
| --- | -------- | --- | --- | --------- | -------- | ------------------ | --- | ---- | --- | ---------- | ------- | --- |
|     |          |     |     |           |          | comes incompatible |     | with | the | historical | regime. | GLR |
12 Complexity:O(n)time,O( 1)space compares online the likelihood of the data under no
Parameters:hcontrols ARL (falsealarmrate);kis change against the best-fitting post-change alternative,
| 13  |     |     | t 0 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theallowancefornoise
|     |     |     |     |     |     | while SPRT | (Sequential |     | Probability |     | Ratio | Test) accu- |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ----------- | --- | ----- | ----------- |
Typicaluse:Abrunptshiftsinmean;online
| 14  |     |     |     |     |     | mulatesevidencebetweentwospecifiedhypothesesun- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
monitoring;lowlatency
|     |               |     |     |     |     | til a decision                                   | threshold |     | is reached. |     | Control | schemes |
| --- | ------------- | --- | --- | --- | --- | ------------------------------------------------ | --------- | --- | ----------- | --- | ------- | ------- |
| 15  | References:[? | ??] |     |     |     |                                                  |           |     |             |     |         |         |
|     |               | i   |     |     |     | basedonspreadandliquidityindicatorsfollowthesame |           |     |             |     |         |         |
logic.
r
|     |     |     |     |     |     | In the         | supervised |        | data-stream |                  | settings, | libraries |
| --- | --- | --- | --- | --- | --- | -------------- | ---------- | ------ | ----------- | ---------------- | --------- | --------- |
|     | p   |     |     |     |     | such as        | MOA,       | River, | and         | Scikit-Multiflow |           | provide   |
|     |     |     |     |     |     | DDM/EDDM/ECDD, |            |        | ADWIN,      | KSWIN,           | and       | CUSUM     |
variantsasplug-and-playcomponentswithinincremen-
e
|     |     |     |     |     |     | tal classifiers,                                    | which                                  | in  | practice | has       | consolidated | these        |
| --- | --- | --- | --- | --- | --- | --------------------------------------------------- | -------------------------------------- | --- | -------- | --------- | ------------ | ------------ |
|     |     |     |     |     |     | sequential                                          | detectors                              | as  | de facto | standards |              | for monitor- |
| r   |     |     |     |     |     | ingcovariatedriftinP(X),conceptdrift(strictsense)in |                                        |     |          |           |              |              |
|     |     |     |     |     |     | P(Y | X),                                           | andchangesintimeseriesinquasi-realtime |     |          |           |              |              |
P
|     |     |     |     |     |     | [? ? ? ? | ? ? ? | ].  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | ----- | --- | --- | --- | --- | --- |
Finally,sequentialdetectorsareoftencombinedwith
|     |     |     |     |     |     | segmentation | methods: |     | the onlinecomponent |     |     | provides |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------------------- | --- | --- | -------- |
21
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
whileoff-linesegmentation
fast, near-real-timealarms, assummarizedinAlgorithm3,viaamessage-passing
refines the dating and statistical significance of struc- scheme that combines: (i) twhe likelihood under the
tural breaks in subsequent analyses [? ? ]. Together, current regime, p(x | θ ) (or more generally p(x |
|     |     |     |     |     |     |     |     |     |     | t   | rt  |     |     | t   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theseapproachesbalanceresponsivenessandstatistical r,x ) for dependent models); and (ii) a prior on
t t−rt:t−1
robustness, making sequential change detection a cen- regime duration, encoded by a hazard function h(r)
t
e
tral building block in non-stationary time-series analy- specifyingtheprobabilityofchangeasafunctionofr. t
| sis. |     |     |     |     |     |     | In     | terms | of data | distributions, |          | each | segment | corre- |
| ---- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------- | -------------- | -------- | ---- | ------- | ------ |
|      |     |     |     |     |     |     | sponds | to    | a time  | interval       | in which | P(X) | (or P(Z | =      |
i
4.3. BayesianMethods f(X))) is assumed constant, and regime changes occur
v
whenthemodeldeemsitmorelikelythattherecentdata
| Bayesian | methods | model | changepoint |     | detection | by  |     |     |     |     |     |     |     |     |
| -------- | ------- | ----- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
specifying a probabilistic structure both for the occur- comefromanewdistribution.
e
|             |         |         |                     |     |        |         | At        | each | step, the | algorithm       | weighs | two         | hypotheses: |        |
| ----------- | ------- | ------- | ------------------- | --- | ------ | ------- | --------- | ---- | --------- | --------------- | ------ | ----------- | ----------- | ------ |
| rence of    | changes | and for | the data-generating |     |        | process |           |      |           |                 |        |             |             |        |
|             |         |         |                     |     |        |         | “continue |      | in the    | current regime” |        | (increasing | r)          | versus |
| within each | regime. | Change  | times               | and | regime | states  |           |      |           |                 |        |             | t           |        |
=
are treated as latent variables, jointly inferred with the “startanewregimenow”(resettingr 0). Ifthepos-
|                  |     |     |     |     |     |     |        | r           |     |        |        | t     |                |     |
| ---------------- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --- | ------ | ------ | ----- | -------------- | --- |
|                  |     |     |     |     |     |     | terior | probability |     | of r = | 0, p(r | = 0 | | x ), increases |     |
| modelparameters. |     |     |     |     |     |     |        |             |     | t      |        | t     | 1:t            |     |
It is assumed that the observations X —or pairs sharp ly,thisindicatesachangepointinnearrealtime.
1:T
|                                   |      |           |                   |        |     |           | In                                                | finance, | one   | often adjusts |           | the hazard | function | to     |
| --------------------------------- | ---- | --------- | ----------------- | ------ | --- | --------- | ------------------------------------------------- | -------- | ----- | ------------- | --------- | ---------- | -------- | ------ |
| (X,Y) t t                         | when | responses | are available—are |        |     | generated | r                                                 |          |       |               |           |            |          |        |
|                                   |      |           |                   |        |     |           | reflect                                           | beliefs  | about | the           | frequency | of         | regime   | breaks |
| fromregime-dependentdistributions |      |           |                   | P(X    | | θ | )or P(Y | |                                                   |          |       |               |           |            |          |        |
|                                   |      |           |                   |        |     | r         | e(forexample,volatilityshocksbeingrarerthansmooth |          |       |               |           |            |          |        |
| X,θ ), where                      |      | r indexes | the latent        | regime |     | and θ de- |                                                   |          |       |               |           |            |          |        |
| r                                 |      |           |                   |        |     | r         |                                                   |          |       |               |           |            |          |        |
changesinthemean)andchooseslikelihoodscompati-
| notes its | associated | parameters. |     | The | temporal | evolu- |     |     |     |     |     |     |     |     |
| --------- | ---------- | ----------- | --- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
tion of regimes is itself probabilistic, commonly mod- blewithasymmetricorheteroscedasticreturns,oreven
e
|     |     |     |     |     |     |     | withdistributionsoverrepresentationsZ |     |     |     |     |     | = f(X). | Exact |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ------- | ----- |
eledthroughhazardfunctionsorMarkoviandynamics.
|           |     |              |     |        |              |      | BOCPD | has | cost | O(T2) in | the length | of  | the series, | but |
| --------- | --- | ------------ | --- | ------ | ------------ | ---- | ----- | --- | ---- | -------- | ---------- | --- | ----------- | --- |
| Inference | can | be performed |     | either | sequentially | (on- |       |     |      |          |            |     |             |     |
line) or retrospectively (off-line). As new obseprvations run-length truncations or sliding windows allow O(T)
approximations.
| arrive, or                                    | given | the full | data | history, | the | model up- |     |     |     |     |     |     |     |     |
| --------------------------------------------- | ----- | -------- | ---- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| datesposteriordistributionsovertheparametersθ |       |          |      |          |     | and       |     |     |     |     |     |     |     |     |
r
|                                          |     |     |     |     |  Retrospective |            |           |     |                 | Bayesian | segmentation |        | (Barry– |        |
| ---------------------------------------- | --- | --- | --- | --- | -------------- | ---------- | --------- | --- | --------------- | -------- | ------------ | ------ | ------- | ------ |
| overlatentquantitiessuchastherun-lengthr |     |     |     |     |                | t (thetime |           |     |                 |          |              |        |         |        |
|                                          |     |     |     |     |                |            | Hartigan, |     | Fearnhead–Liu). |          | A            | second | line    | of ap- |
elapsedsincethemostrecentchange)andttheprobabil-
off-line
ityofachangepointattimet. proaches works in mode, seeking the most
o
|     |     |     |     |     |     |     | probable | segmentation |     | (or | samples | from | the segmen- |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | --- | ------- | ---- | ----------- | --- |
Thisframeworknaturallysupportsuncertaintyquan-
|                                                  |     |     |     |     |     |     | tationdistribution)giventheentirehistory |     |     |     |     |     | X   | [? ? ]. |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | ------- |
| tification,allowingonetoassessbothwhetherachange |     |     |     |     |     |     |                                          |     |     |     |     |     | 1:T |         |
occurrned. The change times τ 1 ,...,τ K are explicitly modeled as
| occurred | and | when it |     | It  | enables | the prin- |     |     |     |     |     |     |     |     |
| -------- | --- | ------- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
latentvariables,withpriordistributionsspecifyingboth
| cipled incorporation                       |                 | of prior       | knowledge |       | about         | regime     |                                                    |      |             |     |                  |             |            |     |
| ------------------------------------------ | --------------- | -------------- | --------- | ----- | ------------- | ---------- | -------------------------------------------------- | ---- | ----------- | --- | ---------------- | ----------- | ---------- | --- |
|                                            |                 |                |           |       |               |            | the number                                         |      | of segments |     | K and            | the typical | duration   | of  |
| persistence—such                           |                 | as preferences |           | for   | rare          | changes or |                                                    |      |             |     |                  |             |            |     |
|                                            |                 |                |           |       |               |            | regimes.Intermsofdatadistribution,itisassumedthat, |      |             |     |                  |             |            |     |
| long-lasting                               | regimes—through |                |           | prior | distributions | on         |                                                    |      |             |     |                  |             |            |     |
|                                            |                 |                |           |       |               |            | within                                             | each | segment     | k,  | an approximately |             | stationary |     |
| P(changeatt|r)andonttheregimeparametersP(θ |                 |                |           |       |               | ).         |                                                    |      |             |     |                  |             |            |     |
|                                            |                 | t              |           |       |               | r          |                                                    |      |             |     |                  |             |            |     |
Schematically,wnecangroupthesemethodsintothree distribution generates the data, and that the task is to
|                   |     |                   |        |           |     |         | inferP(τ |      | ,K,θ          | | X | ).           |     |           |     |
| ----------------- | --- | ----------------- | ------ | --------- | --- | ------- | -------- | ---- | ------------- | --- | ------------ | --- | --------- | --- |
| main subfamilies: |     | (a)               | online | detection | via | BOCPD   |          | 1:K  | 1:K           | 1:T |              |     |           |     |
|                   |     |                   |        |           |     |         | Given    | this | probabilistic |     | formulation, |     | inference | can |
| and extensions;   |     | (b) retrospective |        | Bayesian  |     | segmen- |          |      |               |     |              |     |           |     |
iregime-switching (HMM/MS- be performed either by maximum a posteriori (MAP)
| tation; and                             | (c) |     |     | models |     |     |             |     |          |          |           |     |           |        |
| --------------------------------------- | --- | --- | --- | ------ | --- | --- | ----------- | --- | -------- | -------- | --------- | --- | --------- | ------ |
|                                         |     |     |     |        |     |     | estimation, |     | yielding | a single | “optimal” |     | partition | τ , or |
| VAR)withBrayesianfilteringandsmoothing. |     |     |     |        |     |     |             |     |          |          |           |     |           | k      |
byMCMC-basedsampling,whichproducesadistribu-
BOCPD p and online detection via run-length. In tion over possible segmentations and credibility inter-
|          |        |             |     |           |         |     | vals | for each | transition | date. | In  | both cases, | the | result |
| -------- | ------ | ----------- | --- | --------- | ------- | --- | ---- | -------- | ---------- | ----- | --- | ----------- | --- | ------ |
| Bayesian | Online | Changepoint |     | Detection | (BOCPD) | [?  |      |          |            |       |     |             |     |        |
], the time series is modeled as a sequence of approxi- isaBayesiancharacterizationoftheregimestructureof
e
P(X)overtime,withuncertaintyexplicitlyquantified.
matelystationarysegmentsseparatedbylatentchange-
points, with the run-length r—the number of observa- This explicit treatment of uncertainty makes these
t
rtionssincethelastchangepoint—servingasthehidden models particularlyappealing infinancial applications,
wherethegoalisoftentoreconstructhistoricalregimes
| state. Ateachnewobservation |     |     |     | x, thealgorithmrecur- |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P                           |     |     |     | t                     |     |     |     |     |     |     |     |     |     |     |
sivelyupdatestheposteriordistribution ex post—such as bull and bear markets, high- and
|     |     |     |     |     |     |     | low-volatility |     | periods, | or  | episodes | of  | policy interven- |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --- | -------- | --- | ---------------- | --- |
|
p(r t x 1:t ) tion—while accounting for ambiguity in the precise
22
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
timingofregimeboundariesfortherelevantdistribution
P(X)(e.g.,returns,volatilities,worspreads).
Concrete instances of this class include the partition
Algorithm 3: BOCPD: Bayesian Online
models of Barry–Hartigan [? ], which place priors di-
ChangepointDetection
rectly over partitions of the time series into approxi-
Input:Datastreamx ,x ,...;predictivelikelihood e
1 2 mately stationary blocks and derive the corresponding
p(x |r ,x );hazardfunctionH(r);max
t t−1 1:t−1 posterior distribution. Related algorithms developed
run-lengthR (optional)
max by Fearnhead and collaborators [? ] exploit dynamic
Output:Run-lengthposteriorp(r |x )ateachtime i
t 1:t programming or forward-type recursions to compute
t;changepointprobabilities v
the joint distribution over the number and locations of
1 p(r 0 =0)←1; // Initialize: run-length is changepoints,P(τ | X ).Whileexactinferencetyp-
0 icallyincurs e acom 1 p :K utati 1 o : n T alcostofO(T2),resampling-
2
fort=1,2,...do
basedvariants,suchasparticlefilters,provideapproxi-
// Compute predictive probability for matesolutionswithnear-O(T)complexity.
each run-length r
3 forr=0tomin(t−1,R max )do Regim e-switchingmodels(HMM,MS-VAR). Finally,
4 π( t r)← p(x t |r,x 1:t−1 ); // Likelihood regime-switching models—most notably Hidden
under run r r
MarkovModels(HMMs)andMarkov-switchingVARs
5 end
e(MS-VARs)—model regime changes through an unob-
// Growth probabilities: no served discrete-state process S T . At each time t, the
changepoint at t
tt=1
latent state S ∈ 1,...,R represents the active regime
6 forr=1tomin(t,R max )do e and evolves a t ccording to a first-order Markov chain,
7 p(r t =r|x 1:t )∝π( t r−1)·p(r t−1 =r−1| governingthemodelparametersineachperiod[? ? ].
x )·(1−H(r−1))
1:t−1
AclassicalexampleisHamilton’smodel[? ],which
8 end p
assumes that X | S = r ∼ P(X | θ ). In this set-
t t t r
// Changepoint probability: reset to
ting,theseriesfollowsanautoregressiveprocesswhose
r=0
9 p(r t =0|x 1:t )∝ (cid:80)m r= i 0 n(t−1,Rmax)π( t r)·p(r t−1 = r| c a o n e d ffi ea c c ie h nt s s ta a t n e d r /o c r o i r n r t e e s r p c o e n p d ts s d to ep a en re d g o im n e th c e h l a a r t a e c n t t e s r t i a z t e e d ,
x )·H(r) t
1:t−1
by specific mean, volatility, and correlation patterns.
// Normalize posterior o In multivariate extensions (MS-VAR), P(X | S = r)
10 Z t ← (cid:80)m r= i 0 n(t,Rmax)p(r t =r|x 1:t ) jointly captures regime-dependent autoreg t ressiv t e dy-
11 p(r t |x 1:t )← p(r t |x 1:t )/Z t n namicsandcovariancestructures.
// Changepoint alarm (optional) Inference in these models is typically Bayesian and
12 if p(r t =0|x 1:t )>θ alarm then combinesfilteringandsmoothingprocedures—suchas
13 Signal:Changepo intdetectedattimet the forward–backward algorithm—to estimate p(S |
t
14 end t x 1:T ) and p(S t ,S t+1 | x 1:T ), together with parameter
// Update sufficient statistics for estimation via MCMC or variational methods. This
n
each run-length (model-dependent) yieldsposteriordistributionsforboththetransitionma-
15 Updateposteriorparametersfor p(θ r |x 1:t )for trix P(S t+1 | S t ) and the regime-specific parameters θ r
16 end eachr i definingP(X |S t =r).
From a change detection perspective, regime-
r
17 Complexity:O(n2)withouttruncation;O(nR max )with switching models can be employed online, by moni-
truncationatR
pmax toring changes in state probabilities or transition like-
18 H g a a z p a s r ) d ;H fu ( n r) ct = io 1 n / : (r H + (r 1 ) ) = (i 1 n / c λ re ( a c s o in n g s ) tant,geometric lihoods, and off-line, to reconstruct historical regimes
and infer the most likely change dates. Their ability
19eLikelihood:Conjugatepairs(Normal-Normal,
Poisson-Gamma)enableclosed-formupdates to jointly model multiple variables and complex de-
20 Typicaluse:Onlinedetectionwithuncertainty pendence structures makes MS-VARs particularly well
rquantification;gradualdrifts;regimemodels suited for multivariate financial series, where regime
21 References:[???] changes often involve simultaneous shifts in means,
P volatilities,andcorrelations—i.e.,structuralchangesin
P(X).
In summary, Bayesian regime-switching methods
23
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
provide a unified framework for regime detection and ? ? ? ? ]. Inmultivariatefinancialapplications,embed-
modeling, with explicit uncertainty quantification and dingslearnedbytransformersworgraphneuralnetworks
theabilitytoincorporatepriorinformation, suchasas- are often combined with classical detectors—such as
sumptionsaboutregimepersistenceorplausibleparam- kNN,kerneldensityestimation,MMDtests,orstandard
etervalues. Atthesametime,theircomputationalcost CPD methods applied in latent space—to handle com-
e
and sensitivity to modeling choices—such as the num- plextemporalandcross-sectionaldependencies[? ? ?
| ber of regimes, |     | transition | priors, | and | likelihood | spec- | ? ? ? | ].  |     |     |     |     |     |
| --------------- | --- | ---------- | ------- | --- | ---------- | ----- | ----- | --- | --- | --- | --- | --- | --- |
ification—require careful consideration, especially in In finance, embeddiing- and OOD-based detectors
high-dimensionalfinancialsettings. areespeciallyusefulforidentifyinggenuinelyunprece-
v
|     |     |     |     |     |     |     | dented | situations, | where | patterns | of  | co-movement, | liq- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----- | -------- | --- | ------------ | ---- |
4.4. DetectioninEmbeddingsandOOD
uidity,orvolatilitydeviatefromallpreviouslyobserved
e
Thisfamilyofapproachesdetectschangesbymoni- regimes. T heir effectiveness, however, depends criti-
toringhowdatapointsevolveinarepresentation,orla- callyonthequalityofthelearnedrepresentation. When
tentfeature,space. Insteadofoperatingdirectlyonthe theembeddingcaptureseconomicallymeaningfulstruc-
r
rawobservations,theideaistofirsttransformtheseries ture,changesinP(Z)reliablysignalchangesinP(X)or
intoasequenceoflatentvectorsandthentrackchanges P(X,Y ). Whenitdoesnot,thesemethodsmayconfuse
intheirdistributionovertime. Inpractice, thisisoften minorfluctuationswithtruenovelty.
r
framedasanomalyorout-of-distribution(OOD)detec-
e
tioninstreamingsettings. 4.5. MultivariateStructuralDependenceMethods
| Formally, | a   | representation |     | mapping | Z = | f(X) or |     |     |     |     |     |     |     |
| --------- | --- | -------------- | --- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Z = f(X,Y)islearnedfromtheobservedseries X and, Finally, we highlight methods aimed at detecting
e
when available, from covariates Y. At each time t, a regimechangesthatarisefromshiftsinthejointbehav-
latent vector z = f(x ) or z = f(x ,y ) sum- ior of multiple variables. Instead of focusing on uni-
|         | t      | t−k:t        |         | t   | t−k:t           | t−k:t |         |           |         |               |     |                  |     |
| ------- | ------ | ------------ | ------- | --- | --------------- | ----- | ------- | --------- | ------- | ------------- | --- | ---------------- | --- |
|         |        |              |         |     |                 |       | variate | marginals | P(X(i)) | in isolation, |     | these approaches |     |
| marizes | recent | observations | through | a   | slidingpwindow. |       |         |           |         |               |     |                  |     |
A regime change is then interpreted as a shift in the operatedirectlyonthemultivariatedistribution
| induceddistribution |     | P(Z),whichreflectsanunderlying |     |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:0) X(1),...,X(d)(cid:1)
|                                                  |     |           |         |          |           |        |      |     | P(X)=          | P    |         | ,                |     |
| ------------------------------------------------ | --- | --------- | ------- | -------- | --------- | ------ | ---- | --- | -------------- | ---- | ------- | ---------------- | --- |
| changeinP(X)orP(X,Y)[?                           |     |           | ?       | ? ? ? ]. |           |        |      |     |                |      |         |                  |     |
| A simple                                         | and | intuitive | example | is       | prtovided | by au- |      |     |                |      |         |                  |     |
|                                                  |     |           |         |          |           |        | Here | X   | = (X (1),...,X | (d)) | denotes | the multivariate |     |
| toencodersorotherunsupervisedmodelstrainedonhis- |     |           |         |          |           |        |      | t   | t              | t    |         |                  |     |
|                                                  |     |           |         | o        |           |        |      |     |                |      |         | X(i)             |     |
torical data. These models learn a notion of “normal” observation at time t, with each component repre-
t
dynamics for the series. As new observations arrive, sentingadistinctvariableofinterest,suchasthereturn
reconstruction errors or anomnaly scores are computed. ofanasset,ariskfactor,oraliquiditymeasure. Regime
Whenthesescoresincreasepersistently,thecurrentdata changes are then modeled as alterations in the depen-
|           |          |     |          |               |     |            | dence | structure | of the | joint distribution, |     | which | may be |
| --------- | -------- | --- | -------- | ------------- | --- | ---------- | ----- | --------- | ------ | ------------------- | --- | ----- | ------ |
| no longer | resemble | the | training | distribution, |     | indicating |       |           |        |                     |     |       |        |
that the process generatin g X—and therefore Z—has reflected,forinstance,inchangesinthecovariancema-
| changed. |     |     |     |     |     |     | trixΣ | =Cov(X | ),thecorrelationmatrixR |     |     | ,acopulaC |     |
| -------- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----------------------- | --- | --- | --------- | --- |
|          |     |     | t   |     |     |     |       | t      | t                       |     |     | t         | t   |
Beyond reconstruction-based signals, changes can linkingthemarginaldistributions,orinthetopologyof
n
also be detected directly in the latent space. One ap- a dependence graph (graphical model) associated with
|           |           |           |     |         | P(Z) |            | P(X). |     |     |     |     |     |     |
| --------- | --------- | --------- | --- | ------- | ---- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
| proach is | to define | reference |     | regions |      | associated |       |     |     |     |     |     |     |
with known regiimes, for instance, through contrastive One example involves algorithms for detecting
learning or rclustering. A regime transition is then changes in the covariance matrix or in the graph of
detected when latent states drift away from these re- a graphical model. Typically, we compare P baseline
gions opr move closer to others. Related methods com- andP (X)viastatisticsthatsummarizetheirdepen-
recent
pare distributions in representation space across time dence: forexample,testsforequalityofcovariancema-
|          |       |            |     |               |     |          | tricesΣ |          | vs.Σ   | ,orstatisticsofmaximaldiffer- |     |     |     |
| -------- | ----- | ---------- | --- | ------------- | --- | -------- | ------- | -------- | ------ | ----------------------------- | --- | --- | --- |
| windows, | using | tools such | as  | density-ratio | or  | density- |         |          |        |                               |     |     |     |
| e        |       |            |     |               |     |          |         | baseline | recent |                               |     |     |     |
difference estimation, to explicitly test whether P(Z) it enceincorrelationcoefficientsρ overtime. Inthisdi-
ij
haschanged[? ? ? ? ? ? ]. rection,methodssuchasICSS[? ],MOSUM[? ],and
rThisgeneralideanaturallyextendstoawiderangeof PELTextensionsforthecovariancematrix(PELT–Σ)[?
deepOODtechniques. Theseincludeenergy-basedde- ] monitor breaks in univariate variance and, in multi-
| P   |     |     |     |     |     |     | variateversions,injointvariance/covariance,beinguse- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
tectors,one-classandDeep-SVDDmethods,generative
models that estimate latent densities, and uncertainty ful for identifying volatility and co-movement regime
| monitoring | in Bayesian |     | or ensemble | networks |     | [? ? ? | changes[? |     | ? ]. |     |     |     |     |
| ---------- | ----------- | --- | ----------- | -------- | --- | ------ | --------- | --- | ---- | --- | --- | --- | --- |
24
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Building on this idea, several methodological lines jointextremeevents.Similarly,historicallystablehedge
havebeendeveloped. Onthesequentialside,multivari- relationships may deteriorate owr invert sign, translating
ateversionsoftheCUSUMofsquares[? ? ] monitor into localized changes in Σ and R and into increased
t t
sumsofsquares(oraggregatedportfoliostatistics)over residualvolatilityoflong–shortstrategies.
| time to detect | changes | in joint | volatility | [? ? | ]. An- |     |     |     |     |     |     |     |
| -------------- | ------- | -------- | ---------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
e
otherlinefocusesontechniquesfordetectingchangesin 4.6. ChangeDetectionOverview
copulasC,whichdescribeexclusivelythedependence
t
structure between variables, decoupled from marginals This overview is anchored by three complementary
i
|            |           |      |               |         |      | summaries. |     | Together, | Table 6, | Figure | 15, and | Table 7 |
| ---------- | --------- | ---- | ------------- | ------- | ---- | ---------- | --- | --------- | -------- | ------ | ------- | ------- |
| F. In this | case, the | idea | is to compare | an old” | cop- |            |     |           |          |        |         |         |
| i          |           |      |               |         |      |            |     | v         |          |        |         |         |
ulaC withanew”copulaC andtestwhether mapthetypeofchangeofinteresttosuitabledetection
| baseline |     |     | recent |     |     |     |     |     |     |     |     |     |
| -------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
methods,practicalselectioncriteria,andtheircomputa-
| therehasbeenachange,includingintailregions[? |     |     |     |     | ?   | ?   |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionalfeasibeility.
? ? ? ].
Some parametric methods assume Gaussian graphi- Table 6 serves as the primary entry point. It maps
|                               |     |     |                   |     |     | different | change | axes—temporal, |     | statistical, |     | structural, |
| ----------------------------- | --- | --- | ----------------- | --- | --- | --------- | ------ | -------------- | --- | ------------ | --- | ----------- |
| calmodelsorrelatedstructures. |     |     | Anexampleistheuse |     |     |           |        |                |     |              |     |             |
r
of (possibly adaptive) Graphical Lasso to estimate, in andontological—toindicativemethodfamiliesandcon-
|              |             |        | Θ   | = Σ−1        |     | crete financial |     | examples. | For | instance, | abrupt | tem- |
| ------------ | ----------- | ------ | --- | ------------ | --- | --------------- | --- | --------- | --- | --------- | ------ | ---- |
| each window, | a precision | matrix | t   | t associated |     |                 |     |           |     |           |        |      |
withaconditionalindependencegraphG [? ]. Inthis poral changes suggest segmentation or CUSUM-type
|     |     |     |     | t   |     | r   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
context,monitoringchangesindependenceamountsto methods, while shifts in dependence structures point
|                      |     | orΘ. |     |     |     | etoward | covariance-, | copula-, |     | or graph-based |     | detectors. |
| -------------------- | --- | ---- | --- | --- | --- | ------- | ------------ | -------- | --- | -------------- | --- | ---------- |
| monitoringchangesinG |     | t    | t   |     |     |         |              |          |     |                |     |            |
Other methods avoid strong parametric assumptions Thiscompactviewallowsthepractitionertostartfrom
and compare multivariate dependence measures con- the phenomenon of interest (e.g., contagion, regime
|     |     |     |     |     | e   | changes, | beta | instability) | and | narrow | the methodolog- |     |
| --- | --- | --- | --- | --- | --- | -------- | ---- | ------------ | --- | ------ | --------------- | --- |
structeddirectlyfromthedata,suchasdistancematrices
D(X) or kernel matrices K(X) [? ], using multivariate icalspaceaccordingly.
|                      |     |       |         |              |       | Figure | 15  | operationalizes |     | this mapping |     | as a deci- |
| -------------------- | --- | ----- | ------- | ------------ | ----- | ------ | --- | --------------- | --- | ------------ | --- | ---------- |
| Friedman–Rafsky-type |     | tests | [? ] or | graph-bapsed | vari- |        |     |                 |     |              |     |            |
ants (MST, k-NN graph) [? ? ] to assess whether two sion tree. Starting from label availability, it guides
samplesoriginatefromthesamejointdistributionP(X). methodselectionthroughasequenceofpracticalques-
OntheBayesianside,BOCPDextensions tailoredto tionsaboutdimensionality,operationalobjective,usage
context(onlinevs.offline),andscaleofconcern.
| detecting     | changes | in structural | dependetnce | have          | also |      |            |          |            |     |            | Inthis    |
| ------------- | ------- | ------------- | ----------- | ------------- | ---- | ---- | ---------- | -------- | ---------- | --- | ---------- | --------- |
|               |         |               |             |               |      | way, | the figure | connects | conceptual |     | choices    | to imple- |
| been proposed | [?      | ? ? ?         | ? ]. In     | these models, | the  |      |            |          |            |     |            |           |
|               |         |               | o           |               |      |      |            |          |            |     | trade-offs |           |
dependence structure (for example, a graphG or a pa- mentable detector families, highlighting be-
rametersetΘencodingtheedges)istreatedaslatentand tweensupervision,sensitivity,andinterpretability.
evolvingbyregimes,andinfernencefocusesondetecting A complementary decision concerns the representa-
abruptswitchesinthisstructureovertime. tion space in which change is monitored. As summa-
|        |            |             |         |       |         | rized | in Table | 6 and | operationalized |     | in Figure | 15, de- |
| ------ | ---------- | ----------- | ------- | ----- | ------- | ----- | -------- | ----- | --------------- | --- | --------- | ------- |
| From a | structural | standpoint, | methods | based | on cor- |       |          |       |                 |     |           |         |
relationmatrices,copulas,o rgraphicalmodelsinterpret tectors may act on raw series, on hand-crafted finan-
these events as rearrangtements in the dependence net- cial features, or on learned embeddings, depending on
work [? ? ? ? ]. This perspectiveis particularly rele- dimensionality and interpretability requirements. This
n
vantinfinancialapplications, wherestructuralchanges choicedetermineswhetherchangesaredetecteddirectly
inobservablequantities(e.g.,returnsorcorrelations)or
| tend to manifest | more | strongly | in the | relationships | be- |     |     |     |     |     |     |     |
| ---------------- | ---- | -------- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tween variablesithan in each series taken individually. indirectlythroughshiftsinlatentmultivariatepatterns.
Indistributiornalterms,thismeansthatchangesinP(X) Finally,Table7constrainsthesechoicesfromacom-
are often driven primarily by shifts in its dependence putational perspective. It highlights how method fam-
componpent,whilethemarginalsP(X(i))mayremainrel- ilies differ in time and memory complexity as a func-
ativelystable. tion of series length, dimensionality, and model struc-
Importantly, such changes can often be detected be- ture. Thiscomparisonisessentialinhigh-frequencyor
e
foreanyunivariatemodelsignalsinstability,sinceindi- high-dimensional settings, where theoretically appeal-
vidualseriesmayremainwithintypicalvariationranges ingmethodsmaybeimpracticalwithoutdimensionality
rwhilethejointdependencestructurebecomesunprece- reductionortruncationstrategies.
dented[? ? ? ? ? ]. Forinstance,acontagionregime Taken together, these complements transform the
P
maynotbeevidentwheninspectingindividualassetre- broadtaxonomyofchangedetectionintoapracticalse-
turns,butitbecomesclearwhencorrelationsrisecollec- lectionframework:fromidentifyingtherelevantchange
tivelyorwhenthetailcopulaconcentratesmoremasson axis, to choosing an appropriate method family, repre-
25
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Time-varyingparameters(TVP/state-space)
| sentation | space, and | control | mechanism, |     | all while re- | 5.1.1. |     |     |     |     |     |
| --------- | ---------- | ------- | ---------- | --- | ------------- | ------ | --- | --- | --- | --- | --- |
spectingcomputationalconstraints. Time-varying-parameter(TVwP)modelsaddressnon-
coefficients
|     |     |     |     |     |     | stationarity    | by allowing | model     |               | themselves   |          |
| --- | --- | --- | --- | --- | --- | --------------- | ----------- | --------- | ------------- | ------------ | -------- |
|     |     |     |     |     |     | to change       | over time.  | Instead   | of estimating |              | a single |
|     |     |     |     |     |     | fixed parameter | vector,     | the model | treats        | coefficients | as       |
5. AdaptationandContinualLearning
e
evolvingquantitiesthatareupdatedasnewdataarrive,
|              |           |     |              |     |               | typically | through a state-space |     | formulation | [?  | ? ? ]. |
| ------------ | --------- | --- | ------------ | --- | ------------- | --------- | --------------------- | --- | ----------- | --- | ------ |
| This section | addresses |     | the research |     | question: How |           |                       |     |             |     |        |
Thisperspectivenaturaillyleadstoregressionmodelsin
canweadaptmodellearningtodatadistributionshifts
whichparametersvfollowanexplicitevolutionequation.
effectively?
| continuously | and |     | The | focus | is on strate- |     |     |     |     |     |     |
| ------------ | --- | --- | --- | ----- | ------------- | --- | --- | --- | --- | --- | --- |
gies that enable learning systems to react to evolving =β⊤x +ε,
|     |     |     |     |     |     |     | y t | t   | t   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | e   | t   |     |     |     |
datadistributionsinordertosustainorimproveperfor-
mance in non-stationary environments, with particular inwhichβ followsanevolutionequationβ =β +u
|                                    |     |     |     |      |     |           | t              |      |                  | t   | t−1 t  |
| ---------------------------------- | --- | --- | --- | ---- | --- | --------- | -------------- | ---- | ---------------- | --- | ------ |
| relevancetofinancialapplications[? |     |     |     | ? ]. |     |           |                |      |                  |     |        |
|                                    |     |     |     |      |     | (a random | walk, possibly | with | some structure). |     | In fi- |
r
The discussion is organized around the main nance, this is applied to dynamic market betas (betas
thatc hangeovertime)andotheradaptiveregressionco-
| paradigms | for continuous |     | adaptation. |     | We begin |     |     |     |     |     |     |
| --------- | -------------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
efficients.
| with parametric | adaptation |     | methods | that | incorporate |     |     |     |     |     |     |
| --------------- | ---------- | --- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
r
change mechanisms directly into statistical models EstimationistypicallycarriedoutusingtheKalman
efilter
(5.1).Wethenexaminedynamicensemblesandregime- or its extensions (for linear-Gaussian cases) or
specialized models that adaptively activate or reweight through online optimization methods for more general
learners across regimes (5.2). Next, we cover hybrid cases [? ? ? ]. The Kalman filter directly provides
|     |     |     |     |     | e   |     | coefficient |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
adaptationflowsthatcombineexplicitchangehandl ing recursive updates as new data arrive, using
with model updating (5.3). Finally, we discuss recent atransitionmodelthatpenalizesoverlyabruptchanges
|     |     |     |     |     |     |     |     |     | Q   | u   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
approachesbasedoncontinuallearning,test-timpeadap- (through the variance matrix of the term t ). This
tation,andmeta-learning,whichaimtoenablerapidand yieldsanoptimizedadaptiveforgetting:ifthedataindi-
data-efficientadaptation(5.4)[? ? ]. catethatβischanging,thefilteradjusts;ifnot,itkeeps
To synthesize these perspectives, Table 8 provides a it stable. In many cases, this “smooth” layer of adapt-
structuredcomparisonofadaptationmethtodsacrosskey ability responds adequately to incremental or gradual
drifts,reservingmoreradicalinterventions(suchasre-
operationaldimensions,servingasapracticalguidefor
o
methodselectionunderdifferentapplicationconstraints. setsormodelswitches)formomentsofclearstructural
|                |            |     |             | trade-off |         | break. |     |     |     |     |     |
| -------------- | ---------- | --- | ----------- | --------- | ------- | ------ | --- | --- | --- | --- | --- |
| This synthesis | highlights |     | the central |           | between |        |     |     |     |     |     |
stabilityandplasticitythatchanracterizesadaptivelearn- Forexample,supposeastock’ssensitivitytoamarket
ing in finance: overly aggressive adaptation may am- factor slowly increases over several months — a TVP
|             |                 |     |        |         |              | model with | Kalman filtering |     | will gradually |     | raise the |
| ----------- | --------------- | --- | ------ | ------- | ------------ | ---------- | ---------------- | --- | -------------- | --- | --------- |
| plify noise | and transaction |     | costs, | whereas | conservative |            |                  |     |                |     |           |
updates risk sustained per   formance degradation after estimated beta, tracking the change without ever hav-
|                |     |                |     |       |               | ing to explicitly | declare | a one-shot | “regime |     | change”. |
| -------------- | --- | -------------- | --- | ----- | ------------- | ----------------- | ------- | ---------- | ------- | --- | -------- |
| regime changes | [?  | ? ].tTogether, |     | these | elements con- |                   |         |            |         |     |          |
nectadaptationstrategiestotheirpracticalimplications Thisavoidslosingaccumulatedinformationandensures
n
inreal-worldnon-stationarysystems. smoothness. However, if an abrupt shock drastically
changesβ,theTVPmodelwilltakeafewstepstofully
|     | i   |     |     |     |     | adjust (unless | one temporarily |     | increases | the | transition |
| --- | --- | --- | --- | --- | --- | -------------- | --------------- | --- | --------- | --- | ---------- |
5.1. Parametricadaptationapproaches varianceQatthatinstant,whichisequivalenttodetect-
r
|         |              |     |             |       |            | ing and     | nearly resetting | — hence | the | interaction | with |
| ------- | ------------ | --- | ----------- | ----- | ---------- | ----------- | ---------------- | ------- | --- | ----------- | ---- |
| Withpin | this family, | we  | distinguish | three | main para- | detectors). |                  |         |     |             |      |
metric strategies according to how change is repre- In summary, TVP and state-space models provide a
sented in the model. The first relies on continuously formof“built-incontinuousadaptation,”especiallyuse-
e
evolvingparameters,typicallyformulatedinstate-space fulwhenweexpectparameterstomoveslowly.Infinan-
form(5.1.1).Thesecondintroducesregimedependence cial time series, there is broad application: stochastic-
rthrough observable drivers via threshold or smooth- volatility models with time-varying parameters, macro
transition mechanisms (5.1.2). The third assumes a fi- VARmodelswithvaryingcoefficients,dynamicCAPM
P
nite set of discrete latent regimes, with probabilistic models, and so on [? ? ]. They tend to preserve eco-
switching dynamics captured by regime-switching and nomic interpretability (e.g., one can track how a given
coefficientevolvesandrelateittomarketconditions).
HiddenMarkovmodels(5.1.3).
26
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Start
w
ArelabelsYavailable?
|     |     |     |     |     | No  |     | Yes |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e
|     |     |     | No(focuson∆P(X)) |     |     |     |     | Yes(focuson∆P(Y),∆P(Y|X)) |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |
i
H i g h d i m e n s i o n
|     |     |      | L o w d i m e n s i o n    |        | ( p ≥ 1 0 )                             |     | G o a l   | : F a s t a l a r m  | G o a l : R e g i m e d a t i n  | g     |     |
| --- | --- | ---- | -------------------------- | ------ | --------------------------------------- | --- | --------- | -------------------- | -------------------------------- | ----- | --- |
|     |     |      | ( p < 1 0 )                |        | ⇒ E m b e d d i n g s                   |     | ⇒D D M /  | E D D M / E C DD, v⇒ | S eg m e n t a t i o n ( S e c . | 4 .1) |     |
|     |     | ⇒Seg | m e n t a t io n / C U SUM | + M    | M D / E n e r g y o r o t h e r         |     | L os s -b | a s e d C U S U M    | + B O C P D / H M M              |       |     |
|     |     |      | (S e c s . 4 . 1 - 4 . 2 ) | +O O D | /n o v e l t y i n l a t e n t s p a ce |     | (         | S e c . 4 . 2 )      | R e g i m e m o d e ls           |       |     |
|     |     |      |                            |        | ( S e c . 4 . 4 )                       |     |           |                      | ( S e c . 4 . 3 )                |       |     |
e
Usagecontext?
r
|     |     |     |     | E x | p o s t |     |  (quas | O i n re l a in l- e time) |     |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ------ | -------------------------- | --- | --- | --- |
(backtestin g, h is t o ricalstudy)
|     |     |     |     | ⇒S e g | m e n ta tion |     | + ⇒    | S e q u e n t i a l (S e c . 4 . 2 )                                        |     |     |     |
| --- | --- | --- | --- | ------ | ------------- | --- | ------ | --------------------------------------------------------------------------- | --- | --- | --- |
|     |     |     |     | (S e c | . 4 .1 )      |     | rvi as | o e c g c m as e i n o t n a a t l io r n e fi ( n S e e m c . e 4 n . t 1) |     |     |     |
e
Scaleofconcern?
Global/Systemic
eLocal/Sectoral
|     |     |     |     | ⇒A g g r e g a t e s e r i                     | e s / s y s t e m i c f a c tors                         |     | ⇒   | R u n b y c l u s t e r / s e c t or; |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------- | -------------------------------------------------------- | --- | --- | ------------------------------------- | --- | --- | --- |
|     |     |     |     | s ( e b e ro a a l s d o m s t a r r u k c e t | t u , r s a y l s d t e e p m e i n c d r e is n k c ; e |     |     | A g g r e g a t e a la r m s          |     |     |     |
|     |     |     |     | m e t h o d s                                  | , S e c . 4 . 5 )                                        |     |     | a f t e r w a r d s ( S e c . 4 . 5 ) |     |     |     |
Colorcoding:Start|Decision|Branch|Method|Context
p
Figure15: Decisiontreeforchoosingchange-detectionmethodfamilies. Theflowchartguidesmethodselectionbasedonlabelavailability,
dimensionality, operationalgoal, usagecontext, andscaleofconcern. Colorsdistinguishdecisionnodes(yellow), branchingpoints(orange),
recommendedmethods(green),andcontextualconsiderations(purple).

t
withdifferentmean-reversiondynamics.
| 5.1.2. Smooth-transition |     |     | and threshold |     | models |     |     |     |     |     |     |
| ------------------------ | --- | --- | ------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
o
(TAR/STAR)
STAR(SmoothTransitionAutoregressive)models,in
| In some | applications, |     | changes in | behavior | are asso- |                                              |     |     |     |     |     |
| ------- | ------------- | --- | ---------- | -------- | --------- | -------------------------------------------- | --- | --- | --- | --- | --- |
|         |               |     |            |          |           | turn,implementthetransitioninacontinuousway: |     |     |     |     | pa- |
ciatedwithobservablevariabnlesthatindicatewhenthe
|     |     |     |     |     |     | rameters |     | are weighted | combinations | of two | (or more) |
| --- | --- | --- | --- | --- | --- | -------- | --- | ------------ | ------------ | ------ | --------- |
systemisoperatingunderdifferentconditions. Thresh- base regimes via a smooth function (typically logistic)
oldandsmooth-transitionmodelsbuildonthisideaby of the driver z [? ? ? ? ]. Thus, if z is in extreme
|     |     |     |     |     |     |     |     | t   |     | t   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
allowing model parameters to change as a function of values, themodelapproximatesapureregime; inmid-
suchvariables,ratherthtanevolvingautonomouslyover
|     |     |     |     |     |     | range | values, | it is a mixture | of the | two. This | is useful |
| --- | --- | --- | --- | --- | --- | ----- | ------- | --------------- | ------ | --------- | --------- |
time. This resultsnin adaptation mechanisms in which forcapturinggradualchangesorsituationsinwhichthe
regimechangesaretriggeredbyexplicitdrivers. regime does not switch abruptly but as some indicator
In TAR models, one defines one or more thresholds deteriorates or improves. For example, a STAR model
i
|            |          |        |            |        |             | for | inflation: | as expected | inflation | gradually | moves |
| ---------- | -------- | ------ | ---------- | ------ | ----------- | --- | ---------- | ----------- | --------- | --------- | ----- |
| on a state | variable | (which | may be the | series | itself at a |     |            |             |           |           |       |
r
lag,oranothervariable)thatdeterminediscretechanges from X% to Y%, the monetary-policy regime (central
inthepparameters. Forexample, abilinearTARforre- bankreactionparameters)transitionssmoothly.
turns: ifthevariablez t−d (whichmaybealaggedreturn Thesemodelsallowustoincorporate,exante,knowl-
oramacroindicator)isbelowathresholdγ,weuseone
edgeaboutwhichvariablesignalsabehavioralchange.
seet
of parameters (µ 1 , ϕ 1 , etc.); if it is above, we use Infinance,thereareclearcases:forinstance,avolatility
| anotherset(µ | ,ϕ  | ).  |     |     |     |       |       |        |            |                       |     |
| ------------ | --- | --- | --- | --- | --- | ----- | ----- | ------ | ---------- | --------------------- | --- |
|              | 2   | 2   |     |     |     | model | whose | regime | depends on | an implied-volatility |     |
rThis results in deterministic regime switching: not indicator (VIX [? ]) — when VIX is high, differ-
stochastic as in an HMM, but governed by the driver entparametersapply. Oraconsumer-creditmodelthat
Pz.
A financial example is a price-momentum model in changes when the unemployment rate exceeds a given
which,ifashort-termreturnexceedsagiventhreshold, threshold. Byspecifyingthis,adaptationbecomesauto-
the system enters a high-volatility regime or a regime mated: themodelinstantlyadjustsitsparameterswhen
27
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table6:Changeaxesandindicativemethods(compactview).
w
| Axis/feature |     |     | Typicalmethods |     |     |     | Illustrativefinancialexample |     |     |     |     |     |     |
| ------------ | --- | --- | -------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
Temporal–abrupt Segmentation(PELT,Bai–Perron); Suddencrashinamarketindex
CUSUM
|                  |     |     | EWMA/GLR;BOCPDwithsmoothhazard |     |     |     |                    |     | e                |     |     |     |     |
| ---------------- | --- | --- | ------------------------------ | --- | --- | --- | ------------------ | --- | ---------------- | --- | --- | --- | --- |
| Temporal–gradual |     |     |                                |     |     |     | Slowtransitionfrom |     | bulltobearregime |     |     |     |     |
Statistical–∆P(X) E-Divisive,kernelCPD;ADWIN/KSWIN Sectorrotationinstockreturns
Statistical–∆P(Y|X) Regressionsegmentation;supervised Instabilityofbetasinafactormodel
i
CUSUM
Structure–Σ/dependence PELT–Σ;CUSUMofsquares;copulatests Increasein v correlationsduringcrises(contagion)
| Ontological–newclasses/regimes |     |     | BOCPD/HMM(recurrentregimes);OOD |     |     |     |     |     |     |     |     |     |     |
| ------------------------------ | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Newmarketregimes;unprecedentedevents
inembeddings
e
thedrivercrossesthethreshold(TAR),oradjustsgrad- observatrionmodels,thistransitionstructuredefinesthe
ually(STAR),withoutneedingtobere-estimatedfrom jointevolutionoflatentstatesandobservations.
scratch. Mo   del parameters and latent-state probabilities are
Thelimitationisobvious:onemustchoosethedriver tyrpically inferred using the Expectation–Maximization
and calibrate the threshold/transition function. If the (EM)algorithmorBayesianmethodssuchasMCMC[?
e
cause of regime change is not clear, these models may ? ? ]. Infinance, thesemodelsarewidelyapplied, for
notbeapplicable.However,whenthedriveriswellcho- example in Markov-switching GARCH and VAR for-
sen,theyofferrapidadaptation(virtuallywithoutdelay mulations [? ? ? ? ], where volatility or mean levels
e
if the driver is observed in real time) and usually sta- canshiftabruptlyacrossregimes.
bility within each regime, since each submodel can be In the adaptation context, latent-regime models act
calibratedforthatcontext. pproactively: they incorporate regime change in the
|     |     |     |     |     |     | model     | structure  | itself. | When    | a        | new            | regime | occurs, |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | ------- | ------- | -------- | -------------- | ------ | ------- |
|     |     |     |     |     |     | the model | recognizes |         | it (via | filtered | probabilities) |        | and     |
5.1.3. Discretelatentstates(HMM/regime -switching)
switchestothecorrespondingparameterset,whichmay
| Anotherclassicalwayofmodelingstru |      |                     |     | cturalchange |          | differ    |           |        |              |     |        |            |       |
| --------------------------------- | ---- | ------------------- | --- | ------------ | -------- | --------- | --------- | ------ | ------------ | --- | ------ | ---------- | ----- |
|                                   |      |                     |     | t            |          |           | radically | from   | the previous |     | one.   | Thus, we   | avoid |
| is to assume                      | that | the data-generating |     | process      | switches |           |           |        |              |     |        |            |       |
|                                   |      |                     |     |              |          | “forcing” | a         | single | parameter    | set | across | the entire | his-  |
o
| between | a small | number of | distinct | regimes | over time. |     |     |     |     |     |     |     |     |
| ------- | ------- | --------- | -------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
tory.
Inthisapproach,regimemembershipisnotdirectlyob-
|            |          |          |         |          |           | However, |     | a classical | HMM | with | a fixed | number | of  |
| ---------- | -------- | -------- | ------- | -------- | --------- | -------- | --- | ----------- | --- | ---- | ------- | ------ | --- |
| served but | inferred | from the | n data, | and each | regime is |          |     |             |     |      |         |        |     |
regimesKhasadaptivelimitations:itcanonlyalternate
| associatedwithitsownsetofparameters. |     |                  |     | Thisassump- |        |                                   |     |     |     |     |                  |     |     |
| ------------------------------------ | --- | ---------------- | --- | ----------- | ------ | --------------------------------- | --- | --- | --- | --- | ---------------- | --- | --- |
|                                      |     |                  |     |             |        | amongthoseKpre-estimatedpatterns. |     |     |     |     | Ifaqualitatively |     |     |
| tion underlies                       |     | regime-switching |     | and Hidden  | Markov |                                   |     |     |     |     |                  |     |     |
newregimeemerges,themodeldoesnotexplicitlyrep-
| models [? | ? ? | ? ]. Reg ime-switching |     |     | models with |        |            |     |            |     |            |      |        |
| --------- | --- | ---------------------- | --- | --- | ----------- | ------ | ---------- | --- | ---------- | --- | ---------- | ---- | ------ |
|           |     |                        |     |     |             | resent | it (unless | K   | was chosen |     | larger and | that | regime |
discretelatentstatesarearguablytheclassicalparamet-
|     |     | t   |     |     |     | occupies | one | of the | slots). | In other | words, | it  | handles |
| --- | --- | --- | --- | --- | --- | -------- | --- | ------ | ------- | -------- | ------ | --- | ------- |
ricapproachtostructuralbreaks.
|         |            | n        |                 |     |         | recurrences |     | of known | regimes | well | but | not truly | novel |
| ------- | ---------- | -------- | --------------- | --- | ------- | ----------- | --- | -------- | ------- | ---- | --- | --------- | ----- |
| In this | framework, | a latent | discrete-valued |     | process |             |     |          |         |      |     |           |       |
regimes.
| S ∈ {1,...,K} |     |     |     |     | t.  |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t indicates the regime active at time Even so, within the set of modeled regimes, HMM
| ConditionalonSit |     | ,theobservedvariableisgeneratedby |     |     |     |            |     |         |           |     |              |           |     |
| ---------------- | --- | --------------------------------- | --- | --- | --- | ---------- | --- | ------- | --------- | --- | ------------ | --------- | --- |
|                  |     |                                   |     |     |     | adaptation |     | is fast | — as soon | as  | the filtered | probabil- |     |
aregime-spercificdistribution,witheachregimecharac-
|     |     |     |     |     |     | ity of | a new | state | exceeds, | say, | 0.5, the | model | essen- |
| --- | --- | --- | --- | --- | --- | ------ | ----- | ----- | -------- | ---- | -------- | ----- | ------ |
terizedbyitsownparameters(e.g.,means,variances,or
tiallyusesthatstate’sparameters,whichismuchfaster
| coefficipents). | Thisallowsthedata-generatingprocessto |     |     |     |     |                                     |     |     |     |     |     |              |     |
| --------------- | ------------------------------------- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | ------------ | --- |
|                 |                                       |     |     |     |     | thanrecalibratingamodelfromscratch. |     |     |     |     |     | Moreover,the |     |
switchabruptlybetweendistinctparameterizations.
|     |     |     |     |     |     | Markov | structure |     | imposes | some | inertia | (e.g., | if Π is |
| --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ------- | ---- | ------- | ------ | ------- |
ii
| A Hidden                                    | Markov | Model       | (HMM) | specifies    | the      |                                                  |        |                 |     |         |       |      |         |
| ------------------------------------------- | ------ | ----------- | ----- | ------------ | -------- | ------------------------------------------------ | ------ | --------------- | --- | ------- | ----- | ---- | ------- |
| e                                           |        |             |       |              |          | high,                                            | states | are persistent, |     | and the | model | does | not im- |
| regime dynamics                             |        | by assuming | that  | {S } follows | a first- |                                                  |        |                 |     |         |       |      |         |
|                                             |        |             |       | t            |          | mediatelyswitchback),whichpreventsreactingtoeach |        |                 |     |         |       |      |         |
| orderMarkovchainwithtransitionprobabilities |        |             |       |              |          | fluctuation.                                     |        |                 |     |         |       |      |         |
r
|     | P(S | = j|S | =i)=Π | ,   |     |      |                                         |     |     |     |     |     |     |
| --- | --- | ----- | ----- | --- | --- | ---- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     | t     | t−1   | ij  |     |      |                                         |     |     |     |     |     |     |
| P   |     |       |       |     |     | 5.2. | Dynamicensemblesandregimespecialization |     |     |     |     |     |     |
whereΠencodesregimepersistenceandswitchingbe- No single model performs well across all regimes,
havior [? ? ]. Together with the regime-conditional particularly in non-stationary environments where
28
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table7: Computationalcomplexityofchange-detectionmethods. n=serieslength, p=dimension,S =numberofstates(HMM),Rmax =run-
lengthtruncation(BOCPD),K=numberofchangepoints.
w
|     | Method |     | Time |     | Space | Real-time? |     | Scalability | Notes |     |     |     |     |
| --- | ------ | --- | ---- | --- | ----- | ---------- | --- | ----------- | ----- | --- | --- | --- | --- |
SequentialMethods(Section4.2)
|     | CUSUM        |     | O(n) |     | O(1) |     | Yes | High | Singleepass,constantmemory |     |     |     |     |
| --- | ------------ | --- | ---- | --- | ---- | --- | --- | ---- | -------------------------- | --- | --- | --- | --- |
|     | Page-Hinkley |     | O(n) |     | O(1) |     | Yes | High | VariantofCUSUM             |     |     |     |     |
|     | EWMA         |     | O(n) |     | O(1) |     | Yes | High | Exponentialsmoothing       |     |     |     |     |
|     | DDM/EDDM     |     | O(n) |     | O(w) |     | Yes | High | Windowsizew                |     |     |     |     |
i
|     | ADWIN      |     | O(nlogn) |                                 | O(logn) |     | Yes | Medium | Dynamicwindow              |     |     |     |     |
| --- | ---------- | --- | -------- | ------------------------------- | ------- | --- | --- | ------ | -------------------------- | --- | --- | --- | --- |
|     |            |     |          | SegmentationMethods(Section4.1) |         |     |     |        | v                          |     |     |     |     |
|     | BinarySeg. |     | O(nlogn) |                                 | O(K)    |     | No  | High   | Greedyapproximation        |     |     |     |     |
|     | PELT       |     | O(n)avg  |                                 | O(n)    |     | No* | Medium | O(n2)worst;pruningcritical |     |     |     |     |
e
O(n2)worst
|     | WBS        |     | O(nlog2n) |     | O(n) |     | No  | Medium | Wildbinarysegmentation |     |     |     |     |
| --- | ---------- | --- | --------- | --- | ---- | --- | --- | ------ | ---------------------- | --- | --- | --- | --- |
|     | Bai-Perron |     | O(Kn2)    |     | O(n) |     | No  | Low    | Regressionbreaks       |     |     |     |     |
BayesianMethods(Section4.3r)
|     | BOCPD        |     | O(n2)         |     | O(n)    |     | Yes* | Low    | O(nRmax)withtruncation |     |     |     |     |
| --- | ------------ | --- | ------------- | --- | ------- | --- | ---- | ------ | ---------------------- | --- | --- | --- | --- |
|     |              |     | O(nRmax)trunc |     | O(Rmax) |     |      |        |                        |     |     |     |     |
|     | HMM(Forward) |     | O(nS2)        |     | O(S)    |     | Yes  | Medium | Onlinefiltering        |     |     |     |     |
r
|     | HMM(Viterbi)    |     | O(nS2)  |     | O(nS) |     | No  | Medium | MAPsequence   |     |     |     |     |
| --- | --------------- | --- | ------- | --- | ----- | --- | --- | ------ | ------------- | --- | --- | --- | --- |
|     | HMM(Baum-Welch) |     | O(TnS2) |     | O(nS) | e   | No  | Low    | TEMiterations |     |     |     |     |
EmbeddingMethods(Section4.4)
|     | Embed+CUSUM |     | O(np+p3) |     |       |     |     |        |                         |     |     |     |     |
| --- | ----------- | --- | -------- | --- | ----- | --- | --- | ------ | ----------------------- | --- | --- | --- | --- |
|     |             |     |          |     | O(np) |     | Yes | Medium | p3fromembeddingtraining |     |     |     |     |
O(n2m2)
|     | MMD(kernel) |     |     |     | O(nm) |     | No  | Low | Windowsn,m;kernelmatrix |     |     |     |     |
| --- | ----------- | --- | --- | --- | ----- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
e
|     | EnergyDistance |     | O(nmlognm) |     | O(nm) |     | No  | Medium | Sorting-based         |     |     |     |     |
| --- | -------------- | --- | ---------- | --- | ----- | --- | --- | ------ | --------------------- | --- | --- | --- | --- |
|     |                |     | O(np+p2)   |     | O(p2) |     |     |        |                       |     |     |     |     |
|     | OOD(density)   |     |            |     |       |     | Yes | Medium | Afterembeddingtrained |     |     |     |     |
StructuralDependence(Section4.5)
|     | ICSS(Σ)        |     | O(np2)  |     | pO(p2) |       |     |        |                      |     |     |     |     |
| --- | -------------- | --- | ------- | --- | ------ | ----- | --- | ------ | -------------------- | --- | --- | --- | --- |
|     |                |     |         |     |        | Quasi |     | Medium | Covariancebreaks     |     |     |     |     |
|     |                |     | O(np2)  |     | O(p2)  |       |     |        |                      |     |     |     |     |
|     | CUSUMofsquares |     |         |     |        |       | Yes | Medium | Multivariatevariance |     |     |     |     |
|     | Copulatests    |     | O(n2p2) |     | O(np)  |       | No  | Low    | Taildependence       |     |     |     |     |

Scalability(rule-of-thumb):ratingsindicatethetypicalmaximumserieslengthnthatcanbehandledonastandardworkstationwithanefficient
implementation,assumingsmall-to-moderatedimentsion(p≲20).High:n≳106;Medium:105≲n≲106;Low:n≲105.Inpractice,largep
andexpensiveoperations(e.g.,kernelmatrices)reducetheselimitssubstantially.
*Real-timenote:PELTisoffline,butcanb o eusedinaquasi-onlinewayviasliding/rollingwindows.BOCPDisonline,butthenaive
implementationisO(n2);real-timeoperationtypicallyusesrun-lengthtruncationtoamaximumRmax(e.g.,100–500),yieldingO(nRmax)timeand
O(Rmax)memory.
Practicalconsiderations:forhigh-dnimensionalstreams(p>100),dimensionalityreduction(e.g.,PCAorlearnedembeddings)isusually
requiredbeforeapplyingmostdetectors.Sequentialmethods(CUSUM/EWMA)arepreferredforlow-latencymonitoring;segmentationmethods
(PELT/BinarySegmentation)arepreferredforretrospectiveanalysis.

changesmaybeabrupt,trecurrent,ordifficulttoparam- for range-bound markets. An ensemble can monitor
eterize [? ? ]. nWhen multiple behaviors coexist or a trend indicator and dynamically adjust model usage,
regimechangesareheterogeneous,evenadaptivemod- either by gradually shifting weights toward the trend
elscanfail. Anaturalresponseisthereforetomaintain model when momentum increases or by switching en-
anensembleofciomplementarymodelsandadaptatthe
|                                 |            |        |           |     |            |     | tirely  | to the range-bound |     | model     | during      | consolidation |           |
| ------------------------------- | ---------- | ------ | --------- | --- | ---------- | --- | ------- | ------------------ | --- | --------- | ----------- | ------------- | --------- |
| modellevelarsconditionsevolve[? |            |        | ?         | ].  |            |     | phases. |                    |     |           |             |               |           |
|                                 |            |        |           |     |            |     | In      | this context,      | we  | therefore | distinguish |               | three dy- |
| Thepcore                        | motivation | behind | ensembles | is  | to provide |     |         |                    |     |           |             |               |           |
namicensemblemechanisms:(i)gatedmodelselection,
| both robustness | and | continuity. | By maintaining |     | multi- |     |               |            |     |            |     |       |            |
| --------------- | --- | ----------- | -------------- | --- | ------ | --- | ------------- | ---------- | --- | ---------- | --- | ----- | ---------- |
|                 |     |             |                |     |        |     | (ii) adaptive | prediction |     | weighting, | and | (iii) | the incre- |
plespecializedmodels,thesystembecomesresilientto
uneexpectedregimes, whilepreservingknowledgefrom mentalintroductionandretirementofexperts.
| pastconditionsthatmayrecur. |     |     | Thispropertyisparticu- |     |     |     |              |           |     |           |     |                |       |
| --------------------------- | --- | --- | ---------------------- | --- | --- | --- | ------------ | --------- | --- | --------- | --- | -------------- | ----- |
|                             |     |     |                        |     |     |     | Active-model | selection |     | (gating). | A   | first strategy | is to |
larlyvaluableinfinance,wheremarketregimestendto
| r   |     |     |     |     |     |     | explicitlychoose,ateachtimestep,whichmodelshould |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
repeat, and discarding models learned during previous be active. Several specialized models are maintained
Pcrisescanresultinthelossofusefulinformation.
|     |     |     |     |     |     |     | (for example, |     | one trained | for | a stable | market | and an- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | -------- | ------ | ------- |
As an illustration, consider a trading algorithm with otherforacrisis),andagatingmechanism(whichmay
one model optimized for trending markets and another be a regime detector or a learned function) chooses
29
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Table8:Comparisonofadaptationmethodsfornon-stationaryfinancialtimeseries.Methodsarecategorizedbyfamilyandcomparedacrosskey
operationaldimensions.
w
Method Family Speed Memory Complexity WhentoUse Example
ParametricApproaches(Section5.1)
TVP/Kalman Parametric Fast Low O(p2)perstep Gradual pearameter drift, Dynamic market
linearmodels betas
TAR/STAR Parametric Instant Low O(1)switch Known regime driver VIX-based volatil-
availabile ityregimes
HMM/MS Parametric Medium Medium O(KS2) Recurrent discrete Bull/bear market
v
regimes switching
DynamicEnsembles(Section5.2)
e
Gating(MoE) Ensemble Medium Medium O(M·c) Distinct regime special- Trend vs range
ists models
Weightedcombine Ensemble Fast Medium O(M·c) Hedge against uncer- DWM,
r tainty Learn++.NSE
Onlineexperts Ensemble Slow High O(M·t) Evolving regimes, suffi- Streaming classi-
cientdata fiers
r
IncrementalLearning(Section5.3)
SGD+forget Incremental Veryfast Verylow eO(p)perstep Continuousmilddrift Onlinelinearmod-
els
Periodicretrain Batch Slow High O(np) Stable with periodic Monthly model re-
shifts fresh
e
Hyperparameteradapt Meta Medium Low Varies Regime-dependent tun- Learning rate
ing scheduling
ModernApproaches(Section5.4) p
Continual+EWC Continual Medium Medium O(np+p2) Preserveoldknowledge Multi-task fraud
detection
Test-timeadapt Online Fast Low O(k·p) Distribution shift, unla- Domainadaptation
beledtest
t
FoundationFT Transfer Slow* High O(npf) Limitedlabeleddata Pre-trained trans-
o formers
Notation: p=parameters,S =HMMstates,K=iterations,M=ensemblesize,c=expertcost,t=trainingcost,n=samples,pf =fine-tuned
parameters(typicallypf ≪p),k=TTAgradientsteps.
Speedratings:Veryfast(<1ms),Fasnt(1–10ms),Medium(10–100ms),Slow(>100ms),Instant(0ms-rule-based).
Memoryratings:Verylow(O(1)orO(p)),Low(O(p2)orO(S)),Medium(O(M)orO(np)),High(O(nM)orfullhistory).
*Foundationmodelfine-tuningisslowinitiallybutenablesfastsubsequentadaptation.
whichmodeltouseateatchmoment[? ? ? ? ? ]. This changesandanalternativemodelstartsperformingbet-
isessentiallythemnixture-of-experts(MoE)ideawitha ter,theweightingschemeautomaticallyadjusts. Thisis
gatingnetwork,appliedovertime[??].Forinstance,a usedintrackingandconceptdriftmeta-learning: algo-
forecastingsystemmayhaveoneexpertforlowvolatil- rithmssuchasDynamicWeightedMajority(DWM)in
ity and another i for high volatility; a volatility detector theconcept-driftliteraturefollowthisstrategy[? ? ? ].
(oreventheHrMM)determinesinrealtimewhichexpert
shouldmaketheprediction[? ? ? ? ].
p Onlinetrainingofnewexperts. Amoreproactivestrat-
egyistoexpandtheensembleovertimebyintroducing
Predictioncombination(ensembleweighting). Asofter newmodelsasdataevolves. Incontinuousstreams,one
e
alternativeistoavoidhardswitchingandinsteadblend can continuously train new models on recent windows
the predictions of multiple models. Instead of choos- andaddthemtotheensemble,possiblyremovingor“re-
ring a single model, combine the outputs of all of them tiring”oldmodelsthathavebecomeobsolete—aform
withtime-varyingadaptiveweights.Asimplemethodis ofcontinuouslearninginwhichtheensemblegrowsand
P to weight models inversely proportional to their recent is pruned. For example, in the Learn++.NSE [? ? ]
error — thus, models that are performing poorly (per- methodandvariants,foreachnewbatchofdata,anew
hapsduetodrift)receivelowerweight,andiftheregime classifieristrained,andthefinalpredictionisacombi-
30
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
nationofallclassifierswithweightsthatdecayforolder Actionsupondetectingclearstructuralchanges. When
onesiftheymisclassifyrecentdata.Thisgradually“for- a detector confirms a substantwial change, more disrup-
gets”oldhypotheseswithoutdiscardingthemabruptly. tive actions are initiated, as incremental updates may
nolongersuffice.
Despite the advantages of ensemble-based ap- Possibleresponsesincludepartialor
proaches, they are not universally appropriate. Their total model resets, where prior knowledge is discarded
e
use may be impractical when computational resources or strongly downweighted; on-the-fly hyperparameter
are severely constrained, as in ultra–low-latency trad- or architecture adjustments tailored to the new regime;
ingsystems,orwhenstrongmodelinterpretabilityisre- or specialization and branching, where a new model is
i
quiredforregulatoryoroperationalreasons. Ensembles addedtoanensembleratherthanreplacingtheexisting
v
mayalsobeunnecessaryinstableenvironmentswhere one. Thesemechanismsallowflexibleresponsestohet-
suffices,
a single well-calibrated model or undesirable erogeneousorrecurringregimes.
e
| when the         | operational | burden |         | of maintaining |     | and | mon- |            |             |            |     |      |           |
| ---------------- | ----------- | ------ | ------- | -------------- | --- | --- | ---- | ---------- | ----------- | ---------- | --- | ---- | --------- |
| itoring multiple |             | models | becomes | prohibitive.   |     | In  | such |            |             |            |     |      |           |
|                  |             |        |         |                |     |     |      | Continuity | and memory. | Adaptation |     | does | not imply |
cases,simpleradaptiveapproaches—suchasincremen-
r
tallearningortime-varying-parametermodels—canof- forgetting. Topreserveusefulpastknowledge,continu-
|            |          |         |     |         |              |     |     | ity m echanisms | from                                      | continual | learning |     | are often em- |
| ---------- | -------- | ------- | --- | ------- | ------------ | --- | --- | --------------- | ----------------------------------------- | --------- | -------- | --- | ------------- |
| fer a more | suitable | balance |     | between | adaptability |     | and |                 |                                           |           |          |     |               |
|            |          |         |     |         |              |     |     | ployed.         | Replay-basedstrategies,suchasmaintaininga |           |          |     |               |
complexity.
|     |     |     |     |     |     |     |     | r      | buffer        |     |         |     |             |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | ------- | --- | ----------- |
|     |     |     |     |     |     |     |     | memory | of historical |     | samples | and | mixing them |
eintoretraining,mitigatecatastrophicforgettinganden-
5.3. Hybridcontinuous-adaptationflows
|     |     |     |     |     |     |     |     | able faster | readaptation | if previously |     | observed | regimes |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | ------------- | --- | -------- | ------- |
Hybridadaptationflowsareinherentlymulti-layered.
re-emerge.
| Theycombinelow-cost, |     |     | incrementalupdatesoperating |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
e
| continuously      | with      | explicit | responses |        | triggered | by  | de-  |             |                |            |                   |        |             |
| ----------------- | --------- | -------- | --------- | ------ | --------- | --- | ---- | ----------- | -------------- | ---------- | ----------------- | ------ | ----------- |
| tected structural |           | changes. | This      | design | seeks     | to  | rec- |             |                |            |                   |        |             |
|                   |           |          |           |        |           |     |      | Supervision | and supervised |            | reinitialization. |        | In many     |
| oncile two        | competing |          | goals:    | smooth | trackinpg | of  | mi-  |             |                |            |                   |        |             |
|                   |           |          |           |        |           |     |      | high-stakes | applications,  | adaptation |                   | is not | fully auto- |
norfluctuationsanddecisiveinterventionwhenregime matic. Drift signals may prompt human review or of-
| changesareabruptorpersistent. |     |     |     | Figure16summarizes |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
flineanalysis,particularlyinregulateddomainssuchas

agenerichybridadaptationarchitectureforlearningin finance. In these cases, experts may recalibrate mod-
| non-stationaryenvironments. |     |     |     |     | t   |     |     |                  |     |             |            |     |             |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | ---------- | --- | ----------- |
|                             |     |     |     |     |     |     |     | els, incorporate | new | explanatory | variables, |     | or validate |
TheFigure16highlightshowcontinuousmonitoring,
|     |     |     |     | o   |     |     |     | changes | under regulatory | constraints |     | before | redeploy- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------------- | ----------- | --- | ------ | --------- |
lightweight online updates, and event-driven interven- ment,formingahybridmanual–automaticloop.
tionsinteractinasingleprocessingflow.Thediscussion
Theseapproachesareconstrainedbypracticaltrade-
belowfollowsthisstructure,dnetailingthemaincompo-
offs.
|     |     |     |     |     |     |     |     | Strong | adaptation | actions | increase |     | computational |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ------- | -------- | --- | ------------- |
nentsofsuchsystemsandhowtheyjointlybalancere-
|     |     |     |     |     |     |     |     | cost and | latency, whereas |     | purely | incremental | updates |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------ | ----------- | ------- |
sponsivenesstochangewithstabilityovertime.
|     |     |     |     |     |     |     |     | mayrespondtooslowlytoabruptchanges. |     |     |     |     | Theappro- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --------- |

priatebalancedependsonthecostofmodelerrorrela-
| Onlinemonitoringanddtriftalarms. |     |     |     |     | Atthebaseofthe |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
tivetothecostanddelayofadaptation,assummarized
| pipeline, | change       | detectors | operate    | continuously, |               |     | track- |           |     |     |     |     |     |
| --------- | ------------ | --------- | ---------- | ------------- | ------------- | --- | ------ | --------- | --- | --- | --- | --- | --- |
|           |              | n         |            |               |               |     |        | inTable9. |     |     |     |     |     |
| ing model | performance, |           | residuals, |               | or properties |     | of the |           |     |     |     |     |     |
Adaptationshouldnotbeautomaticinallsituations.
| input data | distribution. |     | When | these | detectors | signal | a   |     |     |     |     |     |     |
| ---------- | ------------- | --- | ---- | ----- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
potential structuiral drift, they act as triggers that acti- Itmaybesuppressedwhendriftistransient,whendata
|     |     |     |     |     |     |     |     | after change | are insufficient, |     | when | transaction | or oper- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------------- | --- | ---- | ----------- | -------- |
vatehigher-lerveladaptationmechanisms.
|     |     |     |     |     |     |     |     | ational costs | dominate, | or when | regulatory |     | or stability |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | ------- | ---------- | --- | ------------ |
Local pcontinuous adaptation. Between alarms, the constraintsrequirefixedmodels. Insuchcases,delayed
model is kept up to date through lightweight orconservativeadaptationcanbepreferabletorapidbut
| incremental-learning |     | schemes. |     | Typical | approaches |     | in- | unreliableupdates. |     |     |     |     |     |
| -------------------- | --- | -------- | --- | ------- | ---------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
e
cludeexponentialforgettingingradientupdatesorregu- In summary, hybrid adaptation architectures provide
laronlineretrainingwithnewlyarrivingdata.Thislayer aprincipledwaytomanagenon-stationaritybycoordi-
rhandles small, gradual shifts without destabilizing the nating continuous learning with selective intervention.
modelandissupportedbymanystandardlearners,such Theireffectivenessliesnotonlyinhowtheyadapt,but
P
aslinearmodelstrainedviastochasticgradientdescent also in deciding when adaptation should be limited or
and neural networks updated through progressive fine- deferred, ensuring robustness without unnecessary in-
| tuning. |     |     |     |     |     |     |     | stability |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
31
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
w
e
i
v
Table9: Cost-benefittrade-offsforadaptationstrategiesinfinancialapplications. Performancegainsareapproximateandcontext-dependent;
valuesshownaretypicalforfinancialtimeseriesforecastingandclassificationtasks.
e
Strategy Latency ComputeCost Data Require- Perf.Gain WhentoUse
ments
r
Noadaptation 0ms None N/A Baseline(0%) Stable regimes only; bench-
mark
Incrementalupdate 1–10ms Verylow Streamingornly +5–10% Gradual drift; HFT; latency-
critical
e
Hyperparameter 1–10min Medium Recent window +10–15% Moderateregimechange;peri-
tuning (100–1000) odicmaintenance
Ensemblereweight 10–100ms Low eRecent window +10–20% Uncertain regimes; multiple
(50–500) hypotheses
Addensemblemem- 10min–1hr High New regime data +15–25% Novel regime emerges; suffi-
ber p(500–5000) cientdata
Fullretrain 1–24hrs Veryhigh Full history +20–30% Abruptstructuralbreak;offline
(5000+) batch
Modelreset 10min–1hr High Newregimeonly +15–25% Completeregimechange; his-
t(1000+) toryirrelevant
Test-timeadapt 10–100ms oLow–medium Unlabeled test +5–15% Domain shift; batch inference
batch mode
Foundationfine-tune 1–12hrs* Veryhigh Limited labels +15–30% New domain; leverage pre-
n
(100–1000) training
Latency:Timetoapplyadaptationandresumenormaloperation.Excludesinitialtraining.
Computecost:RelativeCPU/GP Urequirements."Verylow"=single-coreCPUsufficient;"Veryhigh"=multi-GPUordistributedcluster.
Datarequirements:Approximatenumberofobservationsneededforreliableadaptation.Variesbyproblemdimensionality.
Performancegain:Typicalimtprovementoverno-adaptationbaseline,measuredbyaccuracy,RMSEreduction,orrisk-adjustedreturns.Highly
problem-dependent.
n
*Foundationmodelfine-tuningisexpensiveinitiallybutenablesrapidsubsequentadaptation(<1hr)tonewsub-regimes.
HFT=High-frequencytrading(microsecond-levellatencyrequirements).
Decisionguidance:iInpractice,hybridpoliciesareoptimal:incrementalupdatesasdefault(<10msoverhead),triggeredactions(ensemble
reweight,hyperparametertuning)formoderatedrift,andscheduledfullretraining(nightly/weekly)formajorregimechanges.Thecostoferror
r
relativetoadaptationcostdeterminesaggressiveness:riskmanagement(higherrorcost)justifiesexpensiveadaptation;informationalforecasts
(lowerrorcost)favorcheapincrementalapproaches.
p
e
r
P
32
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
OnlineMonitoring
w
DriftDetector(Sec.4)
Continuous:
Alwaysactive,
lowoverhead
|     |     | IncrementalUpdate |     | No  |     |     |     |     |     | e   |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DriftDetected?
Yes
|     |     |     |     |     | ClassifySeverity |     |     |     |     | i   |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
v
Memory
|     |                        | L G ig r h a t d D u r a if | l t |     | Regi | M m od e e c ra h te ange |     | S Se tr v u er c e t D u | r r i a ft l |     | B u ff e r |     |
| --- | ---------------------- | --------------------------- | --- | --- | ---- | ------------------------- | --- | ------------------------ | ------------ | --- | ---------- | --- |
|     | Ev T e r n ig t g -d e | r re iv d e b n y :         |     |     |      |                           |     |                          |              |     | R e p la y |     |
|     | detection              |                             |     |     |      |                           |     | e                        |              |     |            |     |
Prevents
|     |     | IncrementalSGD |     |     | Adjusthyperparams |             |                       |                 |     |                  | catastrophic |     |
| --- | --- | -------------- | --- | --- | ----------------- | ----------- | --------------------- | --------------- | --- | ---------------- | ------------ | --- |
|     |     | withforgetting |     |     | +reweightensemble |             |                       | Type?           |     |                  | forgetting   |     |
|     |     | (Sec.5.4.1)    |     |     | (Sec.5.2)         |             |                       |                 |     |                  |              |     |
|     |     |                |     |     |                   |             |                       | ArR             | N   |                  |              |     |
|     |     |                |     |     |                   |             | Abrupt:  Recurrent:   |                 |     | Novel:           |              |     |
|     |     |                |     |     |                   |             | Reset/retrain         | Activatedormant |     | Addensemble      |              |     |
|     |     |                |     |     |                   | (Sec.5.4.1) | withreplay r(Sec.5.2) | expert          |     | (Sec.5.2) member |              |     |
e
ReturntoMonitoring
Figure 16: Hybrid continuous-adaptation pipeline. The system combines low-overhead incremental updates (continuous monitoring) with
event-drivenadaptationactionstriggeredbydriftdetection.Seveerityclassificationroutestoappropriatestrategies:lightdriftsreceiveincremental
adjustments,moderatedriftstriggerhyperparametertuningandensemblereweighting,severedriftsinvokemoredrasticmeasures(reset,expert
activation,orensembleexpansion). Memorybuffersenablereplaytomitigatecatastrophicforgetting(Sec.5.4.1). Thismulti-layerarchitecture
balancesadaptationspeed,stability,andperformance(Sec.5.3).
p
5.4. Continuous learning, test-time adaptation, and new training; and dynamic architectures, which allo-

foundationmodels cateadditionalcapacity—suchasnewneuronsormod-
|                 |     |              |     |        | t              |     | ules—to | represent | emerging | regimes | while | preserving |
| --------------- | --- | ------------ | --- | ------ | -------------- | --- | ------- | --------- | -------- | ------- | ----- | ---------- |
| This subsection |     | is organized |     | around | three learning |     |         |           |          |         |       |            |
existingones.Infinancialsettings,forinstance,afraud-
| strategies | for | non-stationary | enviroonments. |     | We  | first |     |     |     |     |     |     |
| ---------- | --- | -------------- | -------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
detectionsystemthatlearnsanewfraudpatternshould
| present continuous |     | learning | methods | (5.4.1), | followed |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | ------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
notbecomeblindtoolder,still-relevantfraudbehaviors.
| by test-time | adaptation | techniques |     | (5.4.2). | Then, | we  |     |     |     |     |     |     |
| ------------ | ---------- | ---------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
n
ArepresentativeexampleofthisphilosophyisElas-
thendiscusslightadaptationoffoundationmodelsand
meta-learning approaches (5.4.3), which aim to enable ticWeightConsolidation(EWC)[? ]. EWCaugments
rapidspecializationunderd istributionshift. the training loss with a penalty that discourages devia-
|     |     |     |     |     |     |     | tions | in parameters | deemed | critical | for previous | tasks, |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------- | ------ | -------- | ------------ | ------ |
t
5.4.1. Continuouslearningandmemorypreservation as measured by Fisher information. In a drift context,
|     |     | n   |     |     |     |     | once | a regime | change | is identified, | the model | can be |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------ | -------------- | --------- | ------ |
Incontinuallearning,theobjectiveistoenablemod-
els to incorporate new information sequentially while updated using recent data while preserving parameters
|          |               |              |     |            |          |     | that encode | information |     | from the | earlier regime. | This |
| -------- | ------------- | ------------ | --- | ---------- | -------- | --- | ----------- | ----------- | --- | -------- | --------------- | ---- |
| avoiding | catastroiphic | forgettingof |     | previously | acquired |     |             |             |     |          |                 |      |
knowledge [? ]. This property is particularly impor- allows the model, at least partially, to function across
r
multipleregimeswithoutfullretraining.
tantunderdistributionshift,whereadaptationtoanew
regimepshouldnoteliminatethemodel’sabilitytooper- Replay-based memory further supports this process,
ateifearlierregimesreappearorcontinuetocoexistin especiallywhenhistoricaldataarelimitedorexpensive
tocollect.Maintainingevenasmallbufferofpastobser-
partofthedata.
e
To achieve this, continual-learning methods rely on vationscansubstantiallyreduceforgettingwhenadapt-
mechanisms that constrain how new knowledge is ab- ing to new conditions. In practice, this often connects
rsorbed. Common strategies include parameter reg- continual learning with ensemble methods: rather than
ularization, which penalizes changes to parameters forcing a single model to remember everything, multi-
P
that were important for past tasks; replay-based ap- plespecializedmodelscanbemaintained, withtheen-
proaches[? ? ], which store or generate samples sembleasawholepreservingbroaderhistoricalknowl-
| from previous |     | data distributions |     | and mix | them | into | edge. |     |     |     |     |     |
| ------------- | --- | ------------------ | --- | ------- | ---- | ---- | ----- | --- | --- | --- | --- | --- |
33
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
Thisideaisexplicitindata-streamalgorithmssuchas regime may, when deployed in a new regime, ob-
Learn++.NSEanditsvariants,whichcontinuallyintro- serve incoming inputs and adwjust selected parameters
ducenewmodelswhileretainingolderonesandadjust- or statistics to preserve internal consistency or invari-
ing their weights based on current performance. Older ants. Whilethiscanprovidefastcorrectionwithoutex-
hypothesesarenotdiscardedoutright,allowingthemto ternal retraining, it is inherently risky: incorrect self-
| remaineffectiveifearliercontextsrecur. |     |     |     |     |     |            |         |       | e                |     |         |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ---------- | ------- | ----- | ---------------- | --- | ------- | --- |
|                                        |     |     |     |     |     | supervised | signals | or po | orly constrained |     | updates | may |
Overall,despitetheseadvantages,continuallearning introducebiasoramplifymodeldrift.
|           |              |     |                  |      |      | Aparticularlypracti |     | calusecasearisesinanomalyde- |     |     |     |     |
| --------- | ------------ | --- | ---------------- | ---- | ---- | ------------------- | --- | ---------------------------- | --- | --- | --- | --- |
| has clear | limitations. | It  | can underperform | when | suc- |                     |     | i                            |     |     |     |     |
cessive regimes are too heterogeneous to be captured tection,wheretestdataareoftenassumedtobemostly
v
by a shared representation, when memory buffers are normal. In such scenarios, thresholds, activity levels,
too small to adequately represent past distributions, or orinternalreferencestatisticscanberecalibratedusing
e
whenthemodelarchitecturelackssufficientcapacityto onlycurren tobservations. Infinance,thisisanalogous
todailyrecalibrationofriskmodelsusingrecentintra-
| expressnewregimecomplexity. |     |     | Inaddition,ifdriftoc- |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
curs faster than the model can adapt—such as during daypricestomaintainalignmentwithcurrentvolatility
r
| abrupt market | shocks—gradual |     | continual-learning |     | up- | levels. |     |     |     |     |     |     |
| ------------- | -------------- | --- | ------------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
theeffectivenessofTTAapproachesislim-
dates may lag behind reality. In such cases, ensemble Ov erall,
specialization or explicit regime-switching approaches ite d when shifts are severe or conceptual in nature:
r
maybemoreeffectivethanattemptingtopreserveasin- if the relationship between inputs and targets changes
eabruptly,unlabeledtestdataprovidelittlereliableguid-
glecontinuouslyadaptingmodel.
|                            |     |     |     |     |     | ance for | adjustment, | unless   | robust | self-supervised |          | ob-     |
| -------------------------- | --- | --- | --- | --- | --- | -------- | ----------- | -------- | ------ | --------------- | -------- | ------- |
|                            |     |     |     |     |     | jectives | correlate   | with the | task   | loss or         | reliable | pseudo- |
| 5.4.2. Test-timeadaptation |     |     |     |     | e   |          |             |          |        |                 |          |         |
labelscanbegenerated.
| Test-time | adaptation | (TTA) | encompasses |     | methods |     |     |     |     |     |     |     |
| --------- | ---------- | ----- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
that allow a model to adjust parts of its behavior dur- 5.4.3. Lightadaptationoffoundationmodelsandmeta-
p
inginferenceitself,usingonlyunlabeleddatafromthe
learning
current environment [? ]. Rather than accumulating Foundation models and meta-learning address non-
| new labeled | data and | retraining | offline, | the model | per- |              |     |          |          |     |          |          |
| ----------- | -------- | ---------- | -------- | --------- | ---- | ------------ | --- | -------- | -------- | --- | -------- | -------- |
|             |          |            |          |           |      | stationarity | by  | reducing | the need | for | frequent | full re- |
forms limited self-adjustment on the fly, aiming to re- training. Instead of rebuilding models whenever the
t
mainalignedwiththeprevailingdatadistribution.
|     |     |     |     |     |     | data distribution |     | changes, | they | rely on | pre-trained | rep- |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | ---- | ------- | ----------- | ---- |
o
Atabasiclevel, TTAoftenoperatesbyupdatingin- resentationsthatcanbequicklyre-specializedwithlim-
ternal statistics rather than model parameters. A com- ited data and computation. This shift is significant in
| mon example | is adaptive |     | no rmalization: | neural | net- |                                                  |     |     |     |     |     |     |
| ----------- | ----------- | --- | --------------- | ------ | ---- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
|             |             |     | n               |        |      | domainssuchasfinance,wherefullretrainingisexpen- |     |     |     |     |     |     |
workswithnormalizationlayers(e.g.,BatchNorm[? ] sive, slow to deploy, and difficult to govern in produc-
| orLayerNorm[? | ])  | relyonestimatesofinputmeanand |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tion.
variance, which may beco me misaligned under distri- This approach is effective under drift for two main
bution shift. Recomputi ng or gradually updating these reasons. First,pre-trainingondiversedatasetsproduces
t
| statistics | at test time, | without | modifying | the | network |                 |     |            |        |        |      |        |
| ---------- | ------------- | ------- | --------- | --- | ------- | --------------- | --- | ---------- | ------ | ------ | ---- | ------ |
|            |               |         |           |     |         | representations |     | that often | remain | useful | when | market |
n
weights, can already improve robustness to covariate conditionschange,evenifthetargetdistributionshifts.
shift.
|     |     |     |     |     |     | Second, | adaptation | can | be limited | to  | a small subset | of  |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | ---------- | --- | -------------- | --- |
parameter-efficient
Moreadvance i dTTAmethodsextendthisideabyal- parameters—such as a task head or
lowing const rained parameter updates guided by self- moduleslikeLoRAoradapters—allowingfastupdates
r
[?
supervised objectives defined on test data ]. Typ- with bounded computational cost and reduced risk of
ical chpoices include entropy minimization or self- overfittingorinstability[? ? ? ? ? ]. Asaresult,mod-
consistencycriteria,whichcanbeevaluatedwithoutla- elscanrespondtoregimechangeswithoutcontinuously
bels. The model performs a small number of gradient modifyingthefullparameterspace.
e
stepstominimizesuchobjectivesbeforeproducingpre- Operationally, a simple deployment loop follows
dictions. Thesetechniqueshaveshownpromiseincor-
|     |     |     |     |     |     | three steps. | Incoming | data | are | first encoded |     | into em- |
| --- | --- | --- | --- | --- | --- | ------------ | -------- | ---- | --- | ------------- | --- | -------- |
rrecting moderate domain shifts in vision and language beddings using a frozen pre-trained backbone. These
| models. |     |     |     |     |     | embeddingsarethenmonitoredovertimetodetectdis- |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
P
In time-series and financial settings, TTA can be in- tributional shifts by comparing recent representations
terpreted as rapid internal recalibration. For instance, againstareferencewindowthatcharacterizesthebase-
a return-forecasting model trained under one market lineregime. Whenadriftdetectorsignalsasignificant
34
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
change, a lightweight adaptation step is triggered us- and false alarms (6.2). Finally, we discuss adaptive-
ingasmallbufferofrecentdata. Onlytheselectedpa- performanceandcost-awaremwetricsthatcapturerecov-
rameters—typicallythetaskheadorparameter-efficient ery,stability,andadaptationcosts(6.3).
components—areupdated,whilethebackboneremains
fixed.Adaptationisusuallyconstrainedbyexplicitbud-
6.1. Temporalvalidationprotocols
e
| gets on | data, optimization |     | steps, | and validation |     | crite- |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | ------ | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
ria,ensuringthatupdatesimproveshort-horizonperfor- In time-series problems, proper evaluation requires
manceandcanbesafelyrolledbackifnecessary. validationprotocolsthatrespecttemporalorder, ensur-
i
ingthatnofutureinformationisusedduringtrainingor
| This paradigm |     | is already | reflected |     | in recent | time- |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
v
series foundation models such as TimesFM, Chronos, calibration[? ? ]. Whilethisprincipleisconceptually
|             |       |        |        |           |     |        | simple, it | demands | careful | implementation |     | in  | practice: |
| ----------- | ----- | ------ | ------ | --------- | --- | ------ | ---------- | ------- | ------- | -------------- | --- | --- | --------- |
| and Moirai, | which | report | strong | zero-shot | and | trans- |            |         |         |                |     |     |           |
vaelidation,
fer performance across heterogeneous benchmarks. In training, and test splits must be defined by
|             |                   |     |              |         |             |        | contiguous  | time | blocks | rather | than random |     | partitions, |
| ----------- | ----------------- | --- | ------------ | ------- | ----------- | ------ | ----------- | ---- | ------ | ------ | ----------- | --- | ----------- |
| financial   | and macroeconomic |     | forecasting, |         | pre-trained |        |             |      |        |        |             |     |             |
|             |                   |     |              |         |             |        | as commonly | done | under  | i.i.d. | assumptions |     | [? ? ].     |
| forecasters | like TimeGPT-1,   |     | as           | well as | compact     | trans- |             |      |        |        |             |     |             |
r
ferable models such as Lag-LLaMA and Tiny Time Moreover,whenevaluatingadaptivemodels,validation
|     |     |     |     |     |     |     | shoul d replicate |     | production | conditions; |     | for instance, | if  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | ----------- | --- | ------------- | --- |
Mixers,providepracticalstartingpointsundercommon
productionconstraintsonlatencyandcompute.Inthese amodelisupdatedmonthlyindeployment,thebacktest
r
settings, light adaptation through heads or adapters is shouldexplicitlysimulatethisupdatecycle[? ? ? ].
| sufficient |     |          |             |     |        |        | eAwidelyusedtemporalvalidationprotocolisthepre- |     |     |     |     |     |     |
| ---------- | --- | -------- | ----------- | --- | ------ | ------ | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
| often      | to  | maintain | performance |     | across | chang- |                                                 |     |     |     |     |     |     |
ingmarketconditions,avoidingrepeatedfullretraining quential(sequentialpredictivetest)scheme[? ? ? ]. In
thissetting,themodelistraineduptoagiventimeand
cycles.
e
In summary, foundation models and meta-learning then used to generate predictions sequentially as new
observationsarrive,withthetrainingsetbeingupdated
| support       | a controlled | and | scalable | response     |     | to non- |              |                                       |     |     |     |     |     |
| ------------- | ------------ | --- | -------- | ------------ | --- | ------- | ------------ | ------------------------------------- | --- | --- | --- | --- | --- |
|               |              |     |          |              |     |         | accordingly. | Thisprotocolcloselymirrorsonlineoper- |     |     |     |     |     |
| stationarity. | By combining |     | reusable | pre-trainepd |     | repre-  |              |                                       |     |     |     |     |     |
sentations,continuousmonitoringofembeddingbehav- ation and allows evaluation under realistic data arrival
ior,andparameter-efficientadaptation,forecastingsys- andadaptationconditions[? ? ].
temscanhandledriftmorequicklyandwit hlowerop- Beyond general forecasting evaluation, specialized
|           |                     |       |          |        |          |           | protocols | are required |            | for systems | that | include | change |
| --------- | ------------------- | ----- | -------- | ------ | -------- | --------- | --------- | ------------ | ---------- | ----------- | ---- | ------- | ------ |
| erational | risk. While         | these | methods  | dotnot |          | eliminate |           |              |            |             |      |         |        |
|           |                     |       |          |        |          |           | detection | and          | adaptation | components. |      | For     | change |
| the need  | for full retraining |       | in cases | of     | large or | persis-   |           |              |            |             |      |         |        |
o
tentshifts,theyofferapracticalmiddlegroundbetween detection, when real or approximate annotations of
|               |     |        |            |            |     |        | changepoint | times | are | available, | evaluation |     | is com- |
| ------------- | --- | ------ | ---------- | ---------- | --- | ------ | ----------- | ----- | --- | ---------- | ---------- | --- | ------- |
| static models | and | costly | retraining | pipelines, |     | making |             |       |     |            |            |     |         |
them well-suited for deploymnent in evolving financial monly performed by running detectors on series with
environments. known changes and observing their behavior relative
|     |     |     |     |     |     |     | to these     | events | [?       | ? ].         | In real-world |     | scenarios |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | -------- | ------------ | ------------- | --- | --------- |
|     |     |     |     |     |     |     | where ground |        | truth is | unavailable, | detectors     |     | are often |
assessedindirectlythroughtheirinteractionwithdown-
t
| 6. Evaluation: | ProtocolsandMetrics |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
streamadaptationmechanisms,forexamplebyembed-
n
dingtheminafulladaptivepipelineandevaluatingthe
This section addresses the research question: How resultingsystembehavior[? ? ? ].
can we evaluate i the performance of models and de- Similarly, adaptation methods should be evaluated
tection/adaptation systems under non-stationarity, us- usingprotocolsthatemphasizeperformanceacrosstime
r
ing appropriate metrics and protocols? Proper evalu- and regimes rather than relying on static train–test
ation ispessential, as inappropriate protocols or metrics splits [? ? ]. Common practices include organizing
canleadtomisleadingconclusionsabouttheeffective- evaluationbytemporalwindowsorregimesandanalyz-
nessofmethodsinevolvingenvironments. ing system behavior before, during, and after distribu-
e
The discussion is organized around three evalua- tion shifts, ensuring that adaptation is assessed under
tion components that together define a concise frame- conditionsthatreflectitsintendedoperationaluse[? ].
rwork for fair and meaningful evaluation under non- Insummary,robustevaluationundernon-stationarity
stationarity. Wefirstpresenttemporalvalidationproto- reliesontemporallyconsistentvalidationprotocols,re-
P
colsthatrespectdatachronologyandavoidinformation alisticsimulationofdeploymentconditions,andend-to-
leakage(6.1).Wethenreviewmetricsspecifictochange endassessmentofdetectionandadaptationmechanisms
anddriftdetectors,includingdetectionaccuracy,delay, withinevolvingdatastreams[? ? ? ].
35
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
•
6.2. Metricsspecifictodetectors Mean Time To Detection (MTTD): beyond
|     |                |     |           |           |     |         |        |     | whether                           | a change | is  | detewcted, | this | criterion  | cap- |
| --- | -------------- | --- | --------- | --------- | --- | ------- | ------ | --- | --------------------------------- | -------- | --- | ---------- | ---- | ---------- | ---- |
|     | The evaluation |     | of change | detectors |     | depends | funda- |     |                                   |          |     |            |      |            |      |
|     |                |     |           |           |     |         |        |     | tureshowquicklythedetectorreacts. |          |     |            |      | Itmeasures |      |
mentallyontheavailabilityandnatureofchange-point
annotations,whichinturnarecloselytiedtothetypeof the average delay between the true changepoint
|     |     |     |     |     |     |     |     |     | and the | alarm | time [? | ? ]. | What | constitutes | an  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------- | ---- | ---- | ----------- | --- |
dataused.Inpractice,detectorsareevaluatedonaspec-
e
trum ranging from synthetic and semi-synthetic series acceptabledelayisapplication-dependent—forin-
tofullyreal-worlddata,eachofferingdifferentlevelsof stance,secondsmaymatterinhigh-frequencytrad-
|     |                     |     |     |      |     |     |     |     | ing, whereas | dela | ys of | months | may | be acceptable |     |
| --- | ------------------- | --- | --- | ---- | --- | --- | --- | --- | ------------ | ---- | ----- | ------ | --- | ------------- | --- |
|     | controlandrealism[? |     |     | ? ]. |     |     |     |     |              |      | i     |        |     |               |     |
A common intermediate setting relies on semi- inmacroeco nomicanalysis.
v
|     | syntheticdatasets, |      | whereartificialchangesareinjected |          |     |          |          | •   |                                         |     |     |     |     |     |     |
| --- | ------------------ | ---- | --------------------------------- | -------- | --- | -------- | -------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |                    |      |                                   |          |     |          |          |     | ARL (AverageRunLengthtofalsealarm):this |     |     |     |     |     |     |
|     | into real          | time | series. This                      | approach |     | provides | approxi- |     | 0                                       |     |     |     |     |     |     |
measureefocusesondetectorbehaviorunderstable
mategroundtruthwhilepreservingrealisticnoisechar-
|     |                                                 |            |              |               |            |           |       |     | conditions.      | Itcorrespondstotheexpectedtimeun- |                |     |               |           |        |
| --- | ----------------------------------------------- | ---------- | ------------ | ------------- | ---------- | --------- | ----- | --- | ---------------- | --------------------------------- | -------------- | --- | ------------- | --------- | ------ |
|     | acteristics                                     | and        | temporal     | dependencies, |            | allowing  | con-  |     |                  |                                   |                |     |               |           |        |
|     |                                                 |            |              |               |            |           |       |     | til a false      | alarm                             | occurs         | and | is inversely  | related   | to     |
|     | trolled evaluation                              |            | under        | conditions    | that       | resemble  | real  |     |                  |                                   |                |     |               |           |        |
|     |                                                 |            |              |               |            |           |       |     | the r sequential |                                   | false-positive |     | rate. In      | practice, | de-    |
|     | data [?                                         | ? ]. Fully | synthetic    | series,       | on         | the other | hand, |     |                  |                                   |                |     |               |           |        |
|     |                                                 |            |              |               |            |           |       |     | tectors          | are often                         | calibrated     |     | by specifying | a         | target |
|     | offercompletecontroloverchangelocationsandmech- |            |              |               |            |           |       |     |                  |                                   |                |     |               |           |        |
|     |                                                 |            |              |               |            |           |       |     | ARL [?           | ? ].                              |                |     |               |           |        |
|     | anisms,                                         | but may    | oversimplify |               | real-world | dynamics  | [?    |     | 0                |                                   |                |     |               |           |        |
r
|     | ].  |     |     |     |     |     |     | •   | MDR | (Missed | Detection | Rate): | defined |     | as the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ------ | ------- | --- | ------ |
e
In contrast, for real-world series without exact proportion of true changes that are not detected,
changepointlabels,evaluationbecomesmorechalleng- this criterion complements recall by explicitly
ing. One pragmatic strategy is indirect assessment quantifyingfailurestosignalchangepoints[? ? ].
e
|     | within an | adaptive | modeling | pipeline: |     | different | detec- |     |     |     |     |     |     |     |     |
| --- | --------- | -------- | -------- | --------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
torsarecombinedwiththesameadaptationpolicy,and 6.3. Adaptive-performanceandcostmetrics
|     | their effectiveness |     | is inferred | from | downstreampbehav- |     |     |        |           |     |            |     |       |              |     |
| --- | ------------------- | --- | ----------- | ---- | ----------------- | --- | --- | ------ | --------- | --- | ---------- | --- | ----- | ------------ | --- |
|     |                     |     |             |      |                   |     |     | Before | analyzing |     | adaptation |     | costs | and benefits |     |
ior[? ? ? ]. IfdetectorAconsistentlyleadstobetter- through specific metrics, it is necessary to define how
adaptedmodelperformancethandetectorBunderiden-
|     |                   |     |                  |     |             |        |      | adaptive | models     | are  | evaluated | in  | practice.        | Metrics | are |
| --- | ----------------- | --- | ---------------- | --- | ----------- | ------ | ---- | -------- | ---------- | ---- | --------- | --- | ---------------- | ------- | --- |
|     | tical conditions, |     | it is reasonable |     | to conclude |   that | A is |          |            |      |           |     |                  |         |     |
|     |                   |     |                  |     |             |        |      | only     | meaningful | when | computed  |     | under evaluation |         | se- |
effective
more at identifying relevant chatnges. Finally, tups that reflect how models are trained, updated, and
infullyunlabeledrealdata,qualitativeinspectionorex-
|     |               |     |              |       | o         |     |          | deployedinareal-worldenvironmentovertime[? |     |     |     |     |     |     | ? ? |
| --- | ------------- | --- | ------------ | ----- | --------- | --- | -------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | pert judgment |     | is sometimes | used, | comparing |     | detected | ].                                         |     |     |     |     |     |     |     |
changepointsagainstknownhistoricalevents—suchas
|     |     |     |     |     |     |     |     | Accordingly, |     | the | evaluation | design | must | be  | made |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---------- | ------ | ---- | --- | ---- |
the2008–09financialcrisisorntheMarch2020COVID-
|     |     |     |     |     |     |     |     | explicit. | The | recommendations |     |     | below | specify | how |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------- | --- | --- | ----- | ------- | --- |
related market crash—to assess plausibility [? ? ]. scenarios and protocols may be defined to determine
|     | Whilesubjective, |     | thisapproachcanprovidecontextual |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereandunderwhichconditionsadaptivemodelsare
|     | validation. |     |     |     |     |     |     |          |      |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
|     |             |     |     |     |     |     |     | tested[? | ? ]. |     |     |     |     |     |     |
So,whenchange-pointtannotationsareavailable,de-
|     | tectors can | be  | eva luated | in a | supervised | manner, | sim- | •   |         |        |          |           |     |           |     |
| --- | ----------- | --- | ---------- | ---- | ---------- | ------- | ---- | --- | ------- | ------ | -------- | --------- | --- | --------- | --- |
|     |             |     | n          |      |            |         |      |     | Testing | across | multiple | scenarios | and | datasets: |     |
ilarly to classifiers, by contrasting correct detections adaptationshouldbeevaluatedondiverseseriesor
with false alarms [? ? ]. In this setting, several com- assets, covering different temporal structures and
|     | plementary | criteiria | are | commonly | used | to characterize |     |     |              |        |      |      |                  |     |     |
| --- | ---------- | --------- | --- | -------- | ---- | --------------- | --- | --- | ------------ | ------ | ---- | ---- | ---------------- | --- | --- |
|     |            |           |     |          |      |                 |     |     | drift types, | rather | than | on a | single benchmark |     | [?  |
detectorbeharvior[? ? ]. ? ? ]. Reliance on a small number of canonical
|     |               |     |         |        |            |            |     |     |            |        |     |             | dataset[? |     | ?    |
| --- | ------------- | --- | ------- | ------ | ---------- | ---------- | --- | --- | ---------- | ------ | --- | ----------- | --------- | --- | ---- |
|     |               |     |         |        |            |            |     |     | benchmarks | (e.g., | the | Electricity |           |     | ] or |
|     | • Prpecision, |     | recall, | and F1 | for change | detection: |     |     |            |        |     |             |           |     |      |
afewmarketindices7),especiallywhencombined
thesemetricsquantifyhowmanytruechangesare
|     |                      |     |     |                          |     |     |     |     | with simplified              |     | protocols, | may | limit | the extent | to  |
| --- | -------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | ---------------------------- | --- | ---------- | --- | ----- | ---------- | --- |
|     | detected(recall)and, |     |     | amongalldetectedchanges, |     |     |     |     |                              |     |            |     |       |            |     |
|     | e                    |     |     |                          |     |     |     |     | whichconclusionsgeneralize[? |     |            |     | ? ].  |            |     |
howmanycorrespondtoactualchangepoints(pre-
|     | cision) | [?  | ? ]. | They are | particularly | useful | in  |     |     |     |     |     |     |     |     |
| --- | ------- | --- | ---- | -------- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
rscenarioswithimbalancedoutcomes,whereeither 7Examplesofwidelyusedmarket-indexdatasourcesincludethe
falsealarmsormisseddetectionsdominate. Inthe S&P 500 level series distributed via FRED [? ]; volatility bench-
| P   |       |             |       |            |     |               |     | markssuchastheVIXfromCboe(alsomirroredinFRED)[? |     |     |     |     |     |     | ? ]; |
| --- | ----- | ----------- | ----- | ---------- | --- | ------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- |
|     | drift | literature, | these | quantities |     | are sometimes | re- |                                                 |     |     |     |     |     |     |      |
research-gradeequityandindexreturnsviaCRSPthroughWRDS[?
ferredtoas“driftdetectionrate”and“falsealarm
];andprovidermethodology/governancedocumentsformajorglobal
|     | rate”[? | ?   | ].  |     |     |     |     | benchmarks(e.g.,MSCIandFTSERussell)[??]. |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
36
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
•
Robustevaluationprotocols: allmethodsshould 7. BenchmarkandReproducibility
| be  | compared | under | identical |     | backtesting | and up- |     |     |     | w   |     |     |     |
| --- | -------- | ----- | --------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
date procedures, with statistical testing applied This section addresses the research question: How
candetectionandadaptationmethodsbebenchmarked
| whereappropriate[? |     |           | ].       |     |            |          |                                             |     |             |     |               |            |        |
| ------------------ | --- | --------- | -------- | --- | ---------- | -------- | ------------------------------------------- | --- | ----------- | --- | ------------- | ---------- | ------ |
|                    |     |           |          |     |            |          | undernon-stationarityinfinancialtimeseries? |     |             |     |               |            | Proper |
| •                  |     |           |          |     |            |          | benchmarking                                | is  | essentieal, | as  | inappropriate | protocols, |        |
| Sensitivity        |     | analysis: | critical |     | parameters | control- |                                             |     |             |     |               |            |        |
ling adaptation (e.g., forgetting factors, detection scenario choices, or reporting conventions can lead to
|             |     |        |              |     |        |           | misleading     | conclusion | s   | about | what works | in  | evolving |
| ----------- | --- | ------ | ------------ | --- | ------ | --------- | -------------- | ---------- | --- | ----- | ---------- | --- | -------- |
| thresholds, |     | update | frequencies) |     | should | be varied |                |            | i   |       |            |     |          |
|             |     |        |              |     |        |           | environments[? |            | ].  |       |            |     |          |
toverifythatresultsarenotdrivenbynarrowtun-
v
| ing[? | ].  |     |     |     |     |     | Thediscussionisorganizedaroundfourcomponents. |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
Wefirstdefinebenchmarkcriteriaandascenariospec-
ificationthaetmakesassumptionsexplicitandcompara-
| • External |     | validity | and | replicability: |     | consistent |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
bleacrossstudies(Section7.1).Wethenreviewdatasets
| evaluation   |     | pipelines | and      | shared  | datasets | enable |           |            |     |         |           |      |      |
| ------------ | --- | --------- | -------- | ------- | -------- | ------ | --------- | ---------- | --- | ------- | --------- | ---- | ---- |
|              |     |           |          |         |          |        | and tasks | for regime | and | anomaly | detection | from | both |
| verification |     | that      | reported | results | persist  | across |           |            |     |         |           |      |      |
r
|           |     |     |     |     |     |     | the financial | and | data-stream |     | literature | (Section | 7.2). |
| --------- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ---------- | -------- | ----- |
| studies[? |     | ].  |     |     |     |     |               |     |             |     |            |          |       |
Next, weproposeaminimalscenario-coveragebaseline
|                                                  |     |     |     |     |     |     | that enables                                | comparable |     | benchmark | suites | without | re-      |
| ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------------------------------------- | ---------- | --- | --------- | ------ | ------- | -------- |
| Oncetheseevaluationsetupsarefixed,thecriteriafo- |     |     |     |     |     |     | r                                           |            |     |           |        |         |          |
|                                                  |     |     |     |     |     |     | quiringasinglecanonicaldataset(Section7.3). |            |     |           |        |         | Finally, |
cusonwhatshouldbemeasuredtoquantifythepracti-
|                              |     |     |     |                      |     |     | ewe provide | a compact |     | recipe | for constructing |     | bench- |
| ---------------------------- | --- | --- | --- | -------------------- | --- | --- | ----------- | --------- | --- | ------ | ---------------- | --- | ------ |
| calconsequencesofadaptation. |     |     |     | Inadditiontostandard |     |     |             |           |     |        |                  |     |        |
marksandreportingreproducibleevaluationsunderre-
| predictive | metrics | computed |     | sequentially |     | over time— |     |     |     |     |     |     |     |
| ---------- | ------- | -------- | --- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
alisticdeploymentconstraints(Section7.4).
| for example, | forecasting |     | error | tracked | across | windoews |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | ----- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
orregimes—adaptivemodelsmustbeassessedwithre-
7.1. Criteriaandscenariospecification
| spect to | the computational, |     |     | behavioral, | and | economic |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
effectsintroducedbymodelupdates,assummaprizedbe-
Benchmarksfornon-stationarityshouldsupportcon-
low[? ? ? ]. trolled, reproducible comparison across methods and
|     |     |     |     |     |     |     | research | traditions. | In  | finance, | this is | challenging | be- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | -------- | ------- | ----------- | --- |

| •             |     |          |          |       |          |           | causestudiesoftenrelyonproprietarydatasets,        |     |     |     |     |     | adhoc |
| ------------- | --- | -------- | -------- | ----- | -------- | --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | ----- |
| Computational |     |          | overhead | and   | latency: | the fre-  |                                                    |     |     |     |     |     |       |
|               |     |          |          |       | t        |           | assetselections,andheterogeneousexperimentalproto- |     |     |     |     |     |       |
| quency        | and | duration | of       | model | updates  | determine |                                                    |     |     |     |     |     |       |
cols,whichlimitsreproducibilityandunderminescross-
| whether |     | adaptation | is  | feasibloe | under | time con- |     |     |     |     |     |     |     |
| ------- | --- | ---------- | --- | --------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
papercomparability.
straints.Streamingframeworks(e.g.,MOA,River)
Tomakebenchmarkdesignexplicitandcomparable,
typicallyreportthroughputtocharacterizethisas-
n
pect[? ? ]. we specify each benchmark scenario s by a taxonomy-
conditioneddescriptor:
| • Memory |     | footprint: |  adaptive |     | architectures | differ |     |     |     |     |     |     |     |
| -------- | --- | ---------- | --------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
ϕ(s)=(Temporal,
|     |     |     |     |     |     |     |     |     | Statistical, |     | Spatial, | Ontological), |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------- | --- |
inresourceusage;largeensemblesrequiresubstan-
|     |     |     | t   |     |     |     |     |     |     |     |     |     | (1) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tiallymorememorythansingle-modelapproaches,
|     |     |     |     |     |     |     | using the | four axes | introduced |     | in Section | 2,  | together |
| --- | --- | --- | --- | --- | --- | --- | --------- | --------- | ---------- | --- | ---------- | --- | -------- |
n
which may be prohibitive in constrained environ- ,anonlineprotocolΠ
|     |     |     |     |     |     |     | withadatainstantiationD |     |     | s   |     |     | s ,and |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | ------ |
ments.
|     |     |     |     |     |     |     | anevaluationmappingE |     |     | (Fig.17): |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --------- | --- | --- | --- |
s
i
• Stabilit yandvolatilityofpredictions:aggressive B={(D ,ϕ(s),Π ,E )}S
|                                     | r   |     |     |     |     |            |     |     | s   |     | s s s=1 | .   | (2) |
| ----------------------------------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ------- | --- | --- |
| adaptationcaninduceerraticbehavior. |     |     |     |     |     | Evaluation |     |     |     |     |         |     |     |
shpouldverifythatmodelupdatesdonotintroduce Here, Π fixes the online setting (e.g., prequential
s
excessive oscillations in predictions or decisions vs. rolling updates, label delay/availability, latency
overtime[? ? ]. and compute budgets, and model-access assumptions),
e
|     |     |     |     |     |     |     | while E | defines | what | is reported | (detection |     | quality, |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---- | ----------- | ---------- | --- | -------- |
s
•
Direct economic impact: in financial applica- predictive performance and calibration, computational
rtions,adaptationshouldbeevaluatedthroughrisk- cost,andfinance-specificutility).
adjusted utility measures. When multiple strate- Under this specification, desirable benchmark prop-
P
gies are compared, statistical controls such as ertiesbecomerequirementson(i)coverageofdriftsig-
White’s Reality Check [? ] are required to miti- natures {ϕ(s)} and (ii) comparability of protocols and
gatedata-snoopingeffects[?
|     |     |     |     | ?   | ].  |     | outcomes: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
37
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
castingandregimechange. Wethencoveranomalyand
ScenarioSpecification out-of-distributionbenchmarkswoftenusedasproxiesfor
B s =(D s ,ϕ(s),Π s ,E s ) rareorextremeregimes.Weclosewithpracticalconsid-
erationsontoolingandreproduciblepipelines.
Datain- Assets/markets;samplingfrequency;horizon; e
stantiation calendarrulesandpreprocessing 7.2.1. Financial time series and forecasting bench-
D (optional)alignedcontextchannels: marksunderchangingregimes
s macro/microstructure/text
Infinance,thereareistillnoconsolidatedbenchmark
repositoriescompvarabletothoseusedinthedata-stream
Driftsig- Temporal: abrupt/ Spatial: global/local
nature gradual/recurrent literature.Instead,evaluationtypicallyreliesonisolated
ϕ(s) Statistical: ∆P(X)/ Ontological: regime/ time series and task-specific experimental setups cho-
e
∆P(Y|X)/dep.shift mechanism
senbyindividualstudies. Asaconsequence,thereisno
single “standard dataset” for problems such as regime
Online Updateprotocol: prequential/rolling;label
protocol delayandavailability change orr adaptive forecasting: different works select
Π Latency/computebudgets;modelaccess: white- different assets, markets, and time periods. For exam-
s box/black-box
ple,onestudymayfocusonBitcoinprices[? ],another
onrindividualstocks[????],andanotheronsectorin-
Evaluation Detection: delay,false-alarmcontrol;Predic- dices, making direct comparison difficult, since results
mapping tion: loss,calibration e
E Compute: wall-clock/memory;Utility: costs, can vary substantially across assets and historical win-
s
drawdown,risk-adj.return
dows.
eSeveral efforts attempt to partially mitigate this lim-
Figure17:Scenariospecificationschemaforbenchmarkdesignunder itation by defining approximate regimes using known
non-stationarity.AscenarioisdefinedbydataDs,driftsignatureϕ(s) economicormarketevents. Commonstrategiesinclude
(four-axistaxonomy),onlineprotocolΠ s,andevaluationmpappingE s.
splitting series into pre- and post-crisis windows (e.g.,
the 2008 global financial crisis or the 2020 COVID
• Identifiability. Scenarios should include anno- shock) and treating them as distinct regimes to assess
tated or controlled changes (event-based, statisti- robustnessunderdistributionshifts. Whileuseful,these
t
cal, or semi-synthetic) to enable objective assess- constructions remain ad hoc and lack standardization
ment. o acrossstudies.
In this fragmented scenario, other types of datasets
• Coverage. Suites should span diverse morpholo-
andtasksaremorecommonlyused,suchas:
gies and mechanisms acnross the four axes (e.g.,
abrupt vs. gradual, global vs. local, regime vs. • Return or volatility forecasting for equity indices
mechanism).
(S&P 500, Dow Jones, and international indices)
• Realism–control balance. Combine real-market over long horizons, where economic cycles and
episodes with cont t rolled synthetic/semi-synthetic crisesprovideimplicitregimevariation.
settingstosepnaratemethodologicaleffectsfromid-
• Detection of regime changes in macroeconomic
iosyncraticartifacts.
series (GDP, inflation) or market indicators such
• Sufficient iduration. Scenarios should be long as implied volatility and trading volume, includ-
enoughrtoevaluatelong-runstability,repeatedup- inginterest-rateseriesaffectedbymonetarypolicy
dates,andcumulativeadaptationeffects.
shifts.
p
• Context metadata. When relevant, pro- • High-frequencyfinancialdata(tickortransaction-
vide aligned macro/microstructure/textual context
levelseries)usedtodetectmicro-regimes,suchas
eto evaluate context-aware and multimodal ap-
intradaychangesinliquidityandvolatility; recent
proaches[? ? ? ].
examples include microstructure data from B3 [?
r ? ? ].
7.2. Datasetsandtasksforregimeandanomalydetec-
Ption • Specialized tasks such as financial contagion de-
Weorganizethisdiscussionintotwocategories. We tection,basedontimeseriesofcorrelationsortail-
first discuss financial time series benchmarks for fore- riskmeasuresacrossmarkets[? ? ? ? ? ].
38
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
7.2.2. Benchmarks for anomalies and out-of- economicfeedback,includingtradingfrictionsandsta-
distribution tisticalcontrolsagainstbacktewstoverfitting[? ? ? ].
|                 |     |         |     |         |                 |     | These | tools | facilitate | implementation, |     | but | fair com- |
| --------------- | --- | ------- | --- | ------- | --------------- | --- | ----- | ----- | ---------- | --------------- | --- | --- | --------- |
| The distinction |     | between |     | concept | drift, regimes, | and |       |       |            |                 |     |     |           |
anomalies is often blurred: rare regimes may appear parisons require explicit scenario and protocol specifi-
anomalous when viewed from dominant market con- cations, which we formalize in Sections 7.3 and 7.4 [?
|                  |       |            |           |              | effectively |            |     |     |     | e   |     |     |     |
| ---------------- | ----- | ---------- | --------- | ------------ | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| ditions,         | while | persistent | anomalies |              | can         | de-        | ].  |     |     |     |     |     |     |
| fine short-lived |       | regimes.   |           | As a result, |             | benchmarks |     |     |     |     |     |     |     |
originally designed for anomaly or out-of-distribution 7.3. Scenario coveragie: towards comparable bench-
| (OOD)detectionarefrequentlyreusedtoevaluatedrift |     |     |     |                      |     |     |         | marksuitesv |            |       |             |     |               |
| ------------------------------------------------ | --- | --- | --- | -------------------- | --- | --- | ------- | ----------- | ---------- | ----- | ----------- | --- | ------------- |
| andregime-detectionmethods,                      |     |     |     | andthemethodological |     |     |         |             |            |       |             |     |               |
|                                                  |     |     |     |                      |     |     | Section | 7.2         | highlights | that, | in finance, |     | evaluation is |
boundariesbetweenthesetasksarenotalwaysclear.
|         |                 |     |     |            |            |      | oftendrivenbyidiosyncraticchoicesofassets,timepe- | e              |     |       |       |         |              |
| ------- | --------------- | --- | --- | ---------- | ---------- | ---- | ------------------------------------------------- | -------------- | --- | ----- | ----- | ------- | ------------ |
| Several | general-purpose |     |     | benchmarks | illustrate | this |                                                   |                |     |       |       |         |              |
|         |                 |     |     |            |            |      | riods,                                            | and protocols, |     | which | makes | results | difficult to |
overlap. TheNumentaAnomalyBenchmark(NAB)[? compareacrossstudies. Toaddressthislimitationwith-
| ], for example, |     | includes   | multiple   |                  | time series—some |          |                |         |           |              |           |       |            |
| --------------- | --- | ---------- | ---------- | ---------------- | ---------------- | -------- | -------------- | ------- | --------- | ------------ | --------- | ----- | ---------- |
|                 |     |            |            |                  |                  |          | out requriring |         | a single  | “standard    | dataset”, |       | we propose |
| with financial  |     | relevance, | such       | as stock-related |                  | Twitter  |                |         |           |              |           |       |            |
|                 |     |            |            |                  |                  |          | to standardize |         | coverage: | a            | benchmark | suite | should in- |
| activity—with   |     | annotated  | anomalies. |                  | Although         | its pri- |                |         |           |              |           |       |            |
|                 |     |            |            |                  |                  |          | clude          | a small | set       | of scenarios | whose     | drift | signatures |
| mary focus      | is  | on point   | anomalies, |                  | extended         | anoma-   |                |         |           |              |           |       |            |
spranthemainregionsofthefour-axistaxonomy(tem-
lous segments can be interpreted as short regimes, and poral,statistical,spatial,ontological),whilekeepingthe
e
| some studies | evaluate |     | drift | detectors | on NAB | by treat- |     |     |     |     |     |     |     |
| ------------ | -------- | --- | ----- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
suitecompactenoughforreproducibleevaluation.
ingeachannotatedanomalyasachangepointtodetect.
Similarly, recently compiled shift benchmarks such eMinimal as reference suite. We recommend the follow-
| the Shifts                | Dataset | [?            | ] provide | real                    | distribution | shifts      |             |            |       |                  |              |                 |           |
| ------------------------- | ------- | ------------- | --------- | ----------------------- | ------------ | ----------- | ----------- | ---------- | ----- | ---------------- | ------------ | --------------- | --------- |
|                           |         |               |           |                         |              |             | ing minimal |            | suite | as a coverage    | baseline.    |                 | Each sce- |
| acrossmultiplemodalities, |         |               |           | eventhoughtheiremphasis |              |             |             |            |       |                  |              |                 |           |
|                           |         |               |           |                         |              |             | nario       | is defined | by    | a characteristic |              | drift signature | ϕ(s)      |
| liesmainlyoutsidefinance. |         |               |           |                         |              | p(Section   |             |            |       |                  |              |                 |           |
|                           |         |               |           |                         |              |             |             | 2)         | and   | can be           | instantiated | using           | multiple  |
| In financial              |         | applications, |           | however,                | there        | is no stan- |             |            |       |                  |              |                 |           |
datasets/tasksfromSection7.2:
| dardized | anomaly | or  | OOD | benchmark. | Most | studies |     |     |     |     |     |     |     |
| -------- | ------- | --- | --- | ---------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
relyonadhoc,event-basedconstructions,su chascom- • S1: Crisis dependence regime. Abrupt changes
paring returns during “normal” periods wtith those ob- in multivariate dependence/tails with global im-
servedaroundmajorshocks(e.g., September11orthe pact,interpretedasaregimeshift(e.g.,contagion;
o
LehmanBrotherscollapse). Whileintuitive,theseprac- correlation/tail-riskbreakdownacrossmarkets).
| tices lack | consistency |            | and comparability |          | across   | works. |     |                          |           |      |                   |     |     |
| ---------- | ----------- | ---------- | ----------------- | -------- | -------- | ------ | --- | ------------------------ | --------- | ---- | ----------------- | --- | --- |
|            |             |            |                   |          |          |        | •   | S2: Localmechanismshift. |           |      | Gradualchangepri- |     |     |
| As noted   | by          | Žliobaite˙ | [?                | ]nin her | critique | of the |     |                          |           |      |                   |     |     |
|            |             |            |                   |          |          |        |     |                          | affecting | ∆P(Y |                   |     |     |
long-standing use of the Electricity data set for con- marily | X) (often coupled with
|            |                                       |     |     |     |     |     |     | ∆P(X)), | local | to a subset | of  | assets/segments, | in- |
| ---------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ----- | ----------- | --- | ---------------- | --- |
| ceptdrift, | thewidespreadadoptionofaconvenientbut |     |     |     |     |     |     |         |       |             |     |                  |     |
limitedbenchmarkcanobs cureimportantmethodolog- terpretedasamechanismchange(e.g.,sectorrota-
tion;microstructure/regulatorychange).
| ical weaknesses. |     | By                | atnalogy, | commonly |      | used finan-  |     |                        |     |     |                      |     |     |
| ---------------- | --- | ----------------- | --------- | -------- | ---- | ------------ | --- | ---------------------- | --- | --- | -------------------- | --- | --- |
| cial anomaly     |     | series—especially |           | those    | with | artificially |     |                        |     |     |                      |     |     |
|                  |     | n                 |           |          |      |              | •   | S3: Secularmacrodrift. |     |     | Incrementaldriftdom- |     |     |
injectedoutliers—shouldbecriticallyexaminedbefore
|     |     |     |     |     |     |     |     | inated | by ∆P(X) | and | slow parameter |     | drift with |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | -------------- | --- | ---------- |
beingusedtoevaluateregime-changeordrift-detection
|          |     |     |     |     |     |     |     | global       | scope, | interpreted | as                            | regime | drift (e.g., |
| -------- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----------- | ----------------------------- | ------ | ------------ |
| methods. |     | i   |     |     |     |     |     |              |        |             |                               |        |              |
|          |     |     |     |     |     |     |     | long-horizon |        | evolution   | in rates/inflation/volatility |        |              |
r
| 7.2.3. Practical  |     | considerations: |                  | tooling |        | and repro- |     | regimes).                |     |          |              |           |      |
| ----------------- | --- | --------------- | ---------------- | ------- | ------ | ---------- | --- | ------------------------ | --- | -------- | ------------ | --------- | ---- |
| dpuciblepipelines |     |                 |                  |         |        |            | •   |                          |     |          |              |           |      |
|                   |     |                 |                  |         |        |            |     | S4: Recurrent            |     | seasonal | regimes.     | Recurrent | pat- |
| To complement     |     | the             | dataset-and-task |         | survey | above,     |     |                          |     |          |              |           |      |
|                   |     |                 |                  |         |        |            |     | terns (calendar/intraday |     |          | seasonality) | primarily | ex-  |
w e note that reproducible benchmarking pipelines are pressedthrough∆P(X)andhigher-orderstructure;
e
| often built | on: | (i) | data-stream | frameworks |     | (MOA, |     |     |     |     |     |     |     |
| ----------- | --- | --- | ----------- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
globalorlocal;typicallyaregimephenomenon.
| Scikit-Multiflow, |     | River) | for | incremental | learning, | drift |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | --- | ----------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
rdetectors,andprequentialevaluation[? ? ? ];(ii)fore- • S5: True concept drift (signal efficacy). Abrupt
castingtoolkitsandarchives(Monash,GluonTS,Darts) orgradualshiftsin∆P(Y|X)thatchangetheuse-
P
for standardized baselines and dataset access [? ? ? fulness or sign of predictive relationships; local
];and(iii)finance-orientedbacktesting/simulationenvi- orglobal; interpretedasmechanismorregimede-
ronments(Gym-likesetups)toevaluateadaptationwith pendingondomainassumptions.
39
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
How this complements existing datasets. This suite model access such as white-box vs. black-box).
is intentionally data-agnostic: it does not prescribe AvoidtuningΠ posthocwtofavoramethod.
s
| a single | dataset, | but | specifies | what | a benchmark |     |           |                |     |         |       |           |
| -------- | -------- | --- | --------- | ---- | ----------- | --- | --------- | -------------- | --- | ------- | ----- | --------- |
|          |          |     |           |      |             |     | 4. Define | the evaluation |     | mapping | E s . | Report at |
suite should cover. For example, index forecasting minimum: (i) detection quality (delay and false-
and macro/indicator monitoring naturally instantiate alarm control), (ii) predictive performance and
| S3/S4; |     |     |     |     |     |     |     |     | e   |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
contagionandcorrelation-networktasksinstan- calibration under d rift, (iii) computational cost
tiate S1; microstructure datasets support S2/S4; and (wall-clock/memory, including retraining), and
| strategy/feature |     | instability | across | regimes | targets | S5. |     |     |     |     |     |     |
| ---------------- | --- | ----------- | ------ | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
(iv)finance-speciificutility(e.g.,transactioncosts,
Anomaly/OOD
benchmarks can be used as proxies for turnover, drvawdown, risk-adjusted return). Use
specific cases (most often S4–S5), but should not be consistent protocols and metrics across methods
| treatedasfullsubstitutesforS1–S3unlesstheypreserve |     |     |     |     |     |     | (Section6). |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
e
multivariatedependencestructureandrealistictemporal 5. Establishbaselinesandtuningbudgets. Include
context.
|                                     |     |     |     |     |             |     | non-adaptive  |         | baselines | and simple | adaptive      | base-  |
| ----------------------------------- | --- | --- | --- | --- | ----------- | --- | ------------- | ------- | --------- | ---------- | ------------- | ------ |
|                                     |     |     |     |     |             |     | liners (e.g., | rolling | retrain)  | to         | contextualize | gains. |
| Minimumreportingforcoveragestudies. |     |     |     |     | Foranysuite |     |               |         |           |            |               |        |
= ,ϕ(s),Π )}S Specify hyperparameter tuning budgets and cali-
| instantiationB |          | {(D           | s   | s ,E s | ,authorsshould |         |          |         |        |                   |     |           |
| -------------- | -------- | ------------- | --- | ------ | -------------- | ------- | -------- | ------- | ------ | ----------------- | --- | --------- |
|                |          |               |     | s=1    |                |         | b ration | targets | (e.g., | fixed false-alarm |     | rate/ARL0 |
| report the     | scenario | specification |     | from   | Section        | 7.1 ex- |          |         |        |                   |     |           |
rfordetectors)topreventunfaircomparisons.
| plicitly.                                              | At minimum, |     | this | includes | (i) the | intended |                    |     |           |            |     |         |
| ------------------------------------------------------ | ----------- | --- | ---- | -------- | ------- | -------- | ------------------ | --- | --------- | ---------- | --- | ------- |
|                                                        |             |     |      |          |         |          | 6. Reproducibility |     | checklist | (minimal). |     | Provide |
| driftsignature(s)ϕ(s)(temporal,statistical,spatial,on- |             |     |      |          |         |          | e                  |     |           |            |     |         |
enoughdetailtoreproduceend-to-endresults:data
| tological),(ii)theonlineprotocolΠ |     |     |     | (updatemodeand |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
s
availability/delay, latency/compute provenance and time span; asset identifiers; ex-
| cadence,           | label |               |     |     |           | bud-     |             |             |     |         |      |         |
| ------------------ | ----- | ------------- | --- | --- | --------- | -------- | ----------- | ----------- | --- | ------- | ---- | ------- |
|                    |       |               |     |     |           |          | act feature | computation |     | windows | (and | leakage |
| gets, model-access |       | assumptions), |     | and | (iii) the | evaleua- |             |             |     |         |      |         |
tion mapping E (detection delay and false-alarm con- checks); protocol definition (warm-up length, up-
s
datecadence);detectorcalibrationandthresholds;
trol,predictivelossandcalibration,computationalcost,
|                      |     |           |     |            |             | prandomseeds; |     |     | computeenvironment; |     |     | andcodeto |
| -------------------- | --- | --------- | --- | ---------- | ----------- | ------------- | --- | --- | ------------------- | --- | --- | --------- |
| and finance-specific |     | utility). |     | To support | attribution | of            |     |     |                     |     |     |           |
runthefullpipelinefromdatatometrics.
| improvements, |     | results | should | include | controlled | com- |     |     |     |     |     |     |
| ------------- | --- | ------- | ------ | ------- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
parisonsorablationsthatseparaterepresenta tion,detec-
tion,andadaptationchoices(cf.Section6).
8. DiscussionandFutureDirections
t
7.4. Recipe: constructing financeobenchmarks under This Section complements the research question:
non-stationarity
Whatarethelimitationsandfutureresearchdirections?
To enable consistent benchmark construction across The discussion is organized around four classes of
n
datasetsandresearchcommunities,weproposethefol- threatstovalidityinlearningundernon-stationarity.We
affect
lowing compact recipe. The goal is not to enforce a first examine data- and label-related issues that
singledataset, buttoenfor cecomparableexperimental construct validity (8.1). We then analyze evaluation-

design.
|     |     |     |     |     |     |     | protocol choices | that | introduce | internal | and | statistical- |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ---- | --------- | -------- | --- | ------------ |
t
|           |      |        |          |            |          |         | conclusionvaliditythreats(8.2). |     |             | Next,wediscussmod- |     |              |
| --------- | ---- | ------ | -------- | ---------- | -------- | ------- | ------------------------------- | --- | ----------- | ------------------ | --- | ------------ |
| 1. Choose | the  | target | drift    | signature. | Select   | a sce-  |                                 |     |             |                    |     |              |
|           |      | n      |          |            |          |         | eling and adaptation            |     | assumptions | that               | can | bias conclu- |
| nario     | from | the    | coverage | suite      | (Section | 7.3) or |                                 |     |             |                    |     |              |
define a new one by specifying ϕ(s) along the sions about robustness under drift (8.3). Finally, we
|             |      |            |     |          |            |        | address finance-specific |     | limitations—such |                             |     | as the “fac- |
| ----------- | ---- | ---------- | --- | -------- | ---------- | ------ | ------------------------ | --- | ---------------- | --------------------------- | --- | ------------ |
| four        | axes | i(Section  | 2). | This     | determines | what   |                          |     |                  |                             |     |              |
|             |      |            |     |          |            |        | tor zoo,” replicability, |     | and              | limited generalization—that |     |              |
| constitutes |      | a “change” |     | and what | should     | be de- |                          |     |                  |                             |     |              |
r
| tectable/adaptable. |     |      |      |                 |     |        | challengeexternalvalidity(8.4). |     |     |     |     |     |
| ------------------- | --- | ---- | ---- | --------------- | --- | ------ | ------------------------------- | --- | --- | --- | --- | --- |
| 2. Inpstantiate     |     | data | D at | the appropriate |     | scale. |                                 |     |     |     |     |     |
s
Choose markets/assets, sampling frequency, pre- 8.1. Data-andlabel-relatedthreats(constructvalidity)
dictionhorizon,andanycontextchannels(macro, Afirstfamilyofthreatsconcernsthequalityofeval-
e
microstructure, text). Make preprocessing rules uation data and the definition of “change labels”. In
explicit(calendar,missingdata,corporateactions, real-world financial time series, there is rarely a pre-
rnormalization). cise ground truth for when drifts occur. As a result,
3. Specify the online protocol Π . Fix the eval- researchers often rely on proxies, such as associating
s
P
uation mode (prequential vs. rolling), update ca- changeswithknownevents(e.g.,marketcrashes)orin-
dence(time-basedorevent-based),labelavailabil- jectingsyntheticdriftsintorealdata. Whilepragmatic,
ity/delay,andconstraints(latency/computebudget;
|     |     |     |     |     |     |     | these strategies | may | fail to | capture | the true | nature of |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------- | ------- | -------- | --------- |
40
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
non-stationarity,whichcandirectlyaffectconstructva- methodiscarefullytunedorevaluatedwithouttemporal
lidity: theexperimentalsetupmaynotaccuratelymea- leakage, while others are not.wIn such cases, observed
surethephenomenonitisintendedtoassess. performance gaps reflect experimental bias rather than
This limitation becomes evident when coarse labels methodologicalsuperiority.
are used to summarize complex dynamics. For exam- Statistical-conclusion validity is compromised when
ple,assigningtheentirefinancialcrisisperiodtoasin- performance differences e are reported without sig-
gleregimeX”andthepost-crisistoregimeY”ignores nificance analysis. Many studies claim improve-
thepresenceofmultiplemicrodriftswithineachphase. ments based on small error reductions or detection
i
Insuchcases,methodsthatmerelyreacttolarge,well- gains, without testing whether these differences are
v
defined shocks may appear overly effective. Similarly, robust. In sequential settings, proper tests—such
validationonsyntheticdatawithsimplelinearorabrupt as Diebold–Mariano or paired tests over repeated
e
drifts can lead to overly optimistic conclusions, as de- runs—are required to separate systematic gains from
tectors tuned to these idealized settings often struggle noise.Withoutthem,non-replicableresultsmaybemis-
when faced with the nonlinear, overlapping, and grad- takenforprogress.
r
ualchangesobservedinrealmarkets. Overall,internalandstatistical-validityfailuresimply
Closely related to this issue is the frequent ab- thatre portedgainsmaydisappearunderstrictercontrols
sence—orlowreliability—ofvalidationlabels. Thisis orralternativesamples,inflatingtheperceivedeffective-
particularly problematic in unsupervised detection set- nessofcurrentmethods. Infinancialapplications,these
tings, where evaluation is often indirect or qualitative. eproblems can become more serious. Multiple models
Withoutobjectivecriteria,performanceclaimsmayrely orvariantsareoftentestedonthesamehistoricalsam-
on visual inspection or on the proximity of detected ple, and only the best result is reported. Apparent im-
e
changes to well-known events, leaving room for sub- provementsarelikelydrivenbychanceandoverfitting,
jective interpretation and making systematic compari- withoutcorrectionformultipletesting,forexamplevia
sonacrossmethodsdifficult. pWhite’sRealityCheck[? ],
Addressingthesechallengesopensseveraldirections Futureresearchshouldprioritizecontrolledandstan-
for future research. One avenue is the development of dardized evaluation protocols, in which all methods
better-annotatedbenchmarkdatasets,possib lycombin- should share the same data access, tuning budget, and
ingexpertknowledgewithdata-drivenlatbelingandun- temporal constraints. Performance comparisons must
certaintyquantification.Moregenerally,evaluationpro- include significance testing and repeated runs. In fi-
o
tocolsshouldconstrainadaptationrules,computational nance, multiple-testing corrections should be manda-
budgets,andretrainingstrategiestoensurecomparabil- tory. Suchpracticeswouldreducespuriousresultsand
ity. Detection frequency, falsne-alarm cost, and adapta- enablemorereliableassessmentofprogressundernon-
tion latency should be reported explicitly. In financial stationarity.
settings,downstreammetricsmayincluderisk-adjusted
returns, drawdowns, or tu rnover. This framing shifts
8.3. Modeling-andadaptation-relatedthreats
evaluation from proxy-btased drift detection to robust-
ness and decision-relevant utility under realistic non- Another family of threats arises from modeling as-
n
stationaryconditions. sumptions and from the design of adaptation mecha-
nisms. To make analysis tractable, many studies adopt
8.2. Evaluation-protocol threats (internal and simplifyingassumptionsthatrarelyholdinoperational
i
statistical-conclusionvalidity) settings,whichweakensbothconstructandexternalva-
r
A second family of threats stems from inadequate lidity.
evaluatpionprotocols,whichcanbiasconclusionsabout A central limitation concerns the assumption of in-
drift detectors and adaptation methods. These threats dependencewithin regimes. Much oftheconcept-drift
fallintotwocategories: internalvalidity, relatedtoex- literature models data as i.i.d. until an abrupt change,
e
perimental control, and statistical-conclusion validity, after which a new i.i.d. regime is assumed. In con-
relatedtothestrengthoftheempiricalevidence. trast, financial time series exhibit strong temporal de-
rInternal-validity problems arise when methods are pendence, including autocorrelation and heteroskedas-
not compared under the same conditions. Common is- ticity,evenwithinstableregimes.
P
suesincludeunequalaccesstodataorcomputation,un- Beyondtemporaldependence,manyapproachesalso
even hyperparameter tuning, and inconsistent tempo- assume a fixed feature space. Most methods focus on
ral protocols. In drift studies, it is frequent that one distributionshiftsinthetargetorinobservedcovariates,
41
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
whileignoringfeatureevolution. Inrealsystems,how- tightlycalibratedtopastpatternsoftenstruggletomain-
ever, variables may appear, disappear, or change rele- taintheirpredictiveperformanwceundernewconditions.
vanceovertime.
|     |     |     |     | Future | research | should prioritize |     | broader | and more |
| --- | --- | --- | --- | ------ | -------- | ----------------- | --- | ------- | -------- |
As a consequence, detectors that ignore temporal systematic evaluations across multiple assets and time
structure may respond to volatility clustering or tran- spans, with explicit attention to replicability. Claims
e
sient dynamics rather than to genuine regime changes, aboutspecificregimesshouldbetestedinanalogousset-
producing misleading signals. When this occurs, a de- tings, and greater emphasis should be placed on struc-
tectormaycorrectlyidentifyadistributionshiftbutfail turallygroundedapproachesthatreduceoverfittingand
i
toadaptbecausetheinformativefeaturesthemselvesare enhance generalization, thereby increasing the likeli-
v
notupdated. hood that methods maintain their effectiveness outside
Thesemodelingassumptionsalsopropagatedirectly oftheoriginaltestconditions.
e
to adaptation mechanisms. Evaluation setups often By confronting these limitations honestly and build-
presume that retraining or model updates can be per- ing robust evidence, the field can progress toward pro-
formed at negligible cost and without operational side viding finance practitioners with reliable tools to navi-
r
effects. Inpractice,adaptationintroduceslatency,com- gateaworldofever-changingdata.
| putationaloverhead,andpotentialinstability,especially |     |                  |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
| whenlabelsaredelayedornoisy.                          |     | Whensuchcostsare |     |     |     |     |     |     |     |
r
9. Conclusion
ignored,explainswhymethodsthatperformwellunder
e
| controlled benchmarks | may fail | when exposed | to real |     |     |     |     |     |     |
| --------------------- | -------- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
financialdata. This research organized the literature on machine
|                 |                  |             |      | learning, | econometrics, | and quantitative |     | finance | into a |
| --------------- | ---------------- | ----------- | ---- | --------- | ------------- | ---------------- | --- | ------- | ------ |
| Future research | should therefore | move toward | more |           |               |                  |     |         |        |
e
realistic modeling and evaluation. Methods should be coherent framework specifically focused on financial
|                      |                    |                       |      | timeseries.                | Weproposedafour-axistaxonomytochar- |              |     |           |      |
| -------------------- | ------------------ | --------------------- | ---- | -------------------------- | ----------------------------------- | ------------ | --- | --------- | ---- |
| tested on temporally | dependent          | data with overlapping |      |                            |                                     |              |     |           |      |
|                      |                    |                       |      | acterize non-stationarity, |                                     | encompassing |     | temporal, | sta- |
| sources of change,   | such as concurrent | shiftspin             | mean |                            |                                     |              |     |           |      |
and volatility. Feature evolution should be explicitly tistical, spatial, and ontological dimensions. Exter-
|                               |     |                    |     | nal representations |     | of non-stationarity |     | were | organized |
| ----------------------------- | --- | ------------------ | --- | ------------------- | --- | ------------------- | --- | ---- | --------- |
| modeledratherthanassumedaway. |     | Finally,adaptation |     |                     |     |                     |     |      |           |
costs, delays, and stability effects should b e incorpo- around embeddings, multiscale features, and both en-
|                               |     |                        |     | dogenousandexogenouscontext. |            |                  | Inaddition,westruc- |          |          |
| ----------------------------- | --- | ---------------------- | --- | ---------------------------- | ---------- | ---------------- | ------------------- | -------- | -------- |
| ratedintoevaluationprotocols. |     | Addressintgthesepoints |     |                              |            |                  |                     |          |          |
|                               |     |                        |     | tured the                    | literature | as an end-to-end |                     | pipeline | covering |
isessentialforbridgingthegapbetweenlaboratoryper-
o
formanceandreal-worldrobustness. drift detection, continuous adaptation, evaluation, and
benchmarking.
limitationns: Thestudyshowsthattheliteratureadequatelydefines
| 8.4. Finance-specific |     | “factor zoo”, | repli- |     |     |     |     |     |     |
| --------------------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
thevariousformsofdrift,providesapproachestorepre-
cability,andgeneralization(externalvalidity)
|     |     |     |     | sent financial | series | and integrate | internal | and | external |
| --- | --- | --- | --- | -------------- | ------ | ------------- | -------- | --- | -------- |
In the financial domain, several challenges threaten information, proposes methods to automatically detect
external validity, that ist, the ability of results to gen- changes,andexploresadaptivemechanismstomaintain
eralize across markets and time periods. A key issue predictive performance over time. Nevertheless, eval-
n
is the factor zoo, in which many reported factors or uationandbenchmarkingpracticesremainunderdevel-
strategies show positive historical performance but fail oped, with limited standardization, weak replicability,
andinsufficientconsiderationofoperationalconstraints.
| toreplicateoutoifsample. | Ananalogousriskarisesfor |     |     |     |     |     |     |     |     |
| ------------------------ | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
learning-based methods, which may become overfitted A key insight is that there is no universally opti-
r
tothecharacteristicsofspecificmarketsandtimewin- mal detector or adaptation strategy. Method selection
dowsraptherthancapturingbroadlystablerelationships. mustalignwiththeexpectedtype,scale,anddynamics
This risk becomes more pronounced in studies that of drift, while deployment decisions must account for
relyonnarrowevaluationsettings,whereamethodmay computational and operational constraints. Evaluation
e
perform well on a specific market or historical period practices should extend beyond predictive accuracy to
butfailtogeneralizetootherassetsortimespans. For include detection delay, false-alarm control, economic
rexample, a regime detector could capture bull–bear al- utility,andrealisticbacktestingthatincorporatestrans-
ternations in US equities between 2000 and 2020 with actioncostsandmarketfrictions.
P highaccuracy,yetitseffectivenessmightnotcarryover
|     |     |     |     | Addressing | these | gaps requires | future | research | fo- |
| --- | --- | --- | --- | ---------- | ----- | ------------- | ------ | -------- | --- |
toemergingmarketsortoearlierhistoricalintervals.As cused on standardized, multi-market benchmarks and
financial structures evolve over time, methods that are decision-centric evaluation protocols that incorporate
42
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273

d
e
| economic                                          | outcomes, | implementation |     | costs, | and | real- | Dataavailability |     |     |     |
| ------------------------------------------------- | --------- | -------------- | --- | ------ | --- | ----- | ---------------- | --- | --- | --- |
| worlddeploymentconsiderations.Takentogether,these |           |                |     |        |     |       |                  |     | w   |     |
points highlight that methodological performance can- No new datasets were created in this survey. The
|     |     |     |     |     |     |     | bibliographic | metadata | of the reviewed | corpus (Bib- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --------------- | ------------ |
notbeseparatedfrompracticalfeasibility.
In conclusion, by offering a unified taxonomy and TeX) and machine-readable versions of the survey ta-
bles(CSV)areavailableefromthecorrespondingauthor
| structured | pipeline, | this | survey | provides | a framework |     |     |     |     |     |
| ---------- | --------- | ---- | ------ | -------- | ----------- | --- | --- | --- | --- | --- |
uponreasonablerequest.Codeusedtogenerateillustra-
| to support | more | comparable | evidence, |     | facilitate | reli- |     |     |     |     |
| ---------- | ---- | ---------- | --------- | --- | ---------- | ----- | --- | --- | --- | --- |
tiveplotsispubliclyavailableintheauthors’repository
| ableimplementation, |                | andstrengthenthefeedbackloop |          |               |     |        |          |            | i                    |                 |
| ------------------- | -------------- | ---------------------------- | -------- | ------------- | --- | ------ | -------- | ---------- | -------------------- | --------------- |
|                     |                |                              |          |               |     |        | (see the | caption of | Fig. 7). Copyrighted | full-text arti- |
| between             | methodological |                              | advances | and practical |     | appli- |          |            |                      |                 |
v
cations in finance, emphasizing that addressing non- cles are not shared. Underlying third-party index data
|              |     |           |             |               |     |        | accessed | via FRED | (e.g., SP500/VIXCLS) | are not re- |
| ------------ | --- | --------- | ----------- | ------------- | --- | ------ | -------- | -------- | -------------------- | ----------- |
| stationarity | in  | financial | time series | is inherently |     | a sys- |          |          |                      |             |
distributed.e
temsproblemspanningrepresentation,detection,adap-
| tation,      | and evaluation |     | under practical |     | and economic |     |             |     |     |     |
| ------------ | -------------- | --- | --------------- | --- | ------------ | --- | ----------- | --- | --- | --- |
| constraints. |                |     |                 |     |              |     | Disclaimrer |     |     |     |
The viewsexpressedinthisarticlearethoseoftheau-
thorsanddonotnecessarilyreflecttheofficialpositions
CRediTauthorshipcontributionstatement
r
oftheirinstitutions.
e
| Davi | M. Cabral: | Data | Curation, | Conceptualization, |     |     |     |     |     |     |
| ---- | ---------- | ---- | --------- | ------------------ | --- | --- | --- | --- | --- | --- |
Methodology,Writing–originaldraft,Writing–review
&editing,Visualization.
e
AdrianoL.I.Oliveira:Supervision,Validation,Writ-
ing–review.
| Gustavo | H.  | F. M. | Oliveira: | Conceptuaplization, |     |     |     |     |     |     |
| ------- | --- | ----- | --------- | ------------------- | --- | --- | --- | --- | --- | --- |
Methodology,Writing–review&editing.
| Adriano  | Lima: | Visualization, |     | Writing | – review | &   |     |     |     |     |
| -------- | ----- | -------------- | --- | ------- | -------- | --- | --- | --- | --- | --- |
| editing. |       |                |     |         |          |     |     |     |     |     |
t
o
| Declaration | of  | generative | AI  | and AI-assisted |     | tech- |     |     |     |     |
| ----------- | --- | ---------- | --- | --------------- | --- | ----- | --- | --- | --- | --- |
nologiesinthemanuscriptpreparationprocess
n
Duringthepreparationofthisworktheauthorsused
ChatGPTtoimprovetheclarityandqualityofthewrit-
| ing. Afterusingthistool/s ervice, |     |     |     | theauthorsreviewed |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
andeditedthecontentastneededandtakefullresponsi-
bilityforthecontentofthepublishedarticle.
n
| Funding |     | i   |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
r
Thisresearchdidnotreceiveanyspecificgrantfrom
fundingpagenciesinthepublic,commercial,ornot-for-
profitsectors.
e
DeclarationofCompetingInterests
r
| The authors |     | declare | that they | have no | known | com- |     |     |     |     |
| ----------- | --- | ------- | --------- | ------- | ----- | ---- | --- | --- | --- | --- |
P
| peting financial |          | interests | or personal | relationships |          | that |     |     |     |     |
| ---------------- | -------- | --------- | ----------- | ------------- | -------- | ---- | --- | --- | --- | --- |
| could have       | appeared | to        | influence   | the work      | reported | in   |     |     |     |     |
thispaper.
43
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=6170273