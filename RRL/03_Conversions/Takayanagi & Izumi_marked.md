NewGenerationComputing(2024)42:635–649
https://doi.org/10.1007/s00354-024-00241-w
IncorporatingDomain-SpecificTraitsinto
Personality-AwareRecommendationsforFinancial
Applications
Takehiro Takayanagi1 ·Kiyoshi Izumi1
Received:18August2023/Accepted:14November2023/Publishedonline:25February2024
©TheAuthor(s)2024
Abstract
The general personality traits, notably the Big-Five personality traits, have been
increasinglyintegratedintorecommendationsystems.Thepersonality-awarerecom-
mendations,whichincorporatehumanpersonalityintorecommendationsystems,have
shown promising results in general recommendation areas including music, movie,
ande-commercerecommendations.Ontheotherhand,thenumberofresearchdelving
intotheapplicabilityofpersonality-awarerecommendations inspecializeddomains
suchasfinanceandeducationremainslimited.Inaddition,thesedomainshaveunique
challenges in incorporating personality-aware recommendations as domain-specific
psychological traits such as risk tolerance and behavioral biases play a crucial role
inexplaininguserbehaviorinthesedomains.Addressingthesechallenges,thisstudy
addressesanin-depthexplorationofpersonality-awarerecommendationsinthefinan-
cialdomain,specificallywithinthecontextofstockrecommendations.First,thisstudy
investigatesthebenefitsofdeployinggeneralpersonalitytraitsinstockrecommenda-
tionsthroughtheintegrationofpersonality-awarerecommendationswithuser-based
collaborative filtering approaches. Second, this study further verifies whether incor-
porating domain-specific psychological traits along with general personality traits
enhances theperformanceofstockrecommender systems.Thirdly,thispaperintro-
duces a personalized stock recommendation model that incorporates both general
personalitytraitsanddomain-specificpsychologicaltraitsaswellastransactiondata.
Theexperimentalresultsshowthattheproposedmodeloutperformedbaselinemodels
infinancialstockrecommendations.
B
TakehiroTakayanagi
takayanagi-takehiro590@g.ecc.u-tokyo.ac.jp
KiyoshiIzumi
izumi@sys.t.u-tokyo.ac.jp
1 DepartmentofEngineering,TheUniversityofTokyo,Hongo7-3-1,Bunkyo-ku1138656,Tokyo,
Japan
123

636 NewGenerationComputing(2024)42:635–649
Keywords Stockrecommendation·Financialdatamining·Collaborativefiltering·
Behavioralfinance
1 Introduction
Inthecurrentdigitalera,usersarepresentedwithanoverwhelmingamountofonline
information and multiple sources of knowledge, which can lead to a phenomenon
known as information overload. Recommender systems represent a promising
approach to assist users in managing this challenge by suggesting items that match
their preferences. Personality is a core human characteristic that remains relatively
stableacrosstimeandissuitableformodelinguserbehavior,incontrasttoemotions
andmood,whichtendtobemoretransientandcontext-dependent.Incorporatingper-
sonalityintorecommendersystemscanimprovetheaccuracyofrecommendationsand
enhanceusersatisfactionbytailoringsuggestionstotheirindividualcharacteristics.
Personality traits have gained significant attention in recommender systems due
totheirpotentialtomitigatethecold-startproblemwhenwedonothaveaccesstoa
user’s interaction data, enhance recommendation diversity, and capture users’ com-
plexnature[1,2].Accordingly,recentstudieshavedemonstratedtheeffectivenessof
personality-awarerecommendation[1–3],whichemployspersonalitytraitstomake
recommendations,ingeneraldomainswithabundantopendatasuchasfilms,music,
andbooks.
While personality-aware recommendation systems have demonstrated success in
general domains where data is readily available, research on their applicability in
specific domains, such as finance, has been limited due to privacy concerns and the
requirement for domain expertise to produce precise recommendations [1, 4]. Con-
sequently, it is worthwhile to explore the potential usefulness of personality traits
in finance recommendation systems, as they may help address challenges such as
informationoverloadinthefinancialdomain.
In addition, it is important to note that domain-specific variables can have a sig-
nificant impact on decision-making processes, particularly in the domain of finance
whilepreviousstudiesonpersonality-awarerecommendationhavemainlyfocusedon
generalpersonalitytraits,suchastheBig-Fivepersonalitytraits[5].Forinstance,fac-
torssuchasrisktoleranceplayacriticalroleininvestmentdecision-making,butmay
not be as relevant in movie or music recommendations. Thus, it is essential to con-
siderdomain-specificvariableswhendevelopingpersonality-awarerecommendation
systems for finance to ensure that they accurately capture the unique characteristics
ofthisdomain.
Finally, personality-aware recommendation systems have primarily been used to
addressthecold-startprobleminrecommendation[1,3],buttheirpotentialtoenhance
existing recommendation models with transaction data remains underexplored [2].
Therefore,itisalsointriguingtoinvestigatewhetherincorporatinggeneralpersonality
traits and domain-specific psychological traits in non-cold start settings can lead to
improvedperformanceinrecommendationsystems.
Insummary,weformulatedthefollowingresearchquestions.
123

NewGenerationComputing(2024)42:635–649 637
1. RQ1:Cangeneralpersonalitytraitsbeusefulinstockrecommendationtasks?
2. RQ2: Do domain-specific psychological traits contribute to the performance of
stockrecommendations?
3. RQ3: How can we integrate investors’ general personality traits and domain-
specific psychological traits with their interaction history to enhance the stock
recommendationmodel?
Therestofthisworkbroadlycorrespondstotheresearchquestions.
2 RelatedWork
2.1 Personality-AwareRecommenderSystem
Personalitytraitshavebeenincreasinglyutilizedintheresearchofrecommendation
[1–3,6].Utilizingpersonalitytraitsforarecommendersystemhasthreeadvantages.
First,usingpersonalitytraitsfortherecommendersystemwillmitigatethecold-start
problem,especiallyfornewusersratherthanitems.Second,personalitytraitscanbe
used to increase recommendation diversity [7]. Third, personality traits help model
the complex nature of user behaviors. For example, personality traits are known to
be significantly correlated with users’ preferences in some areas such as music and
moviepreference[3,6].
Various theories in the literature of personality psychology have attempted to
describehumanpersonalitytraits.Amongothertheories,theFive-factormodel,also
known as the Big-Five personality traits theory is one of the most commonly used
models, where the human personality is characterized by five factors: Extraversion,
Opennesstoexperience,Conscientiousness,Agreeableness,andNeuroticism[5].
While five-factor models are widely used to measure the users’ similarity across
variousdomainsinpersonality-awarerecommendations,mostworksonlyutilizeper-
sonalitytraitstorepresentusers’psychologicaltraitsandignoreotherpsychological
effectswhichmightbeasimportantaspersonalitytraits[3,6].Thus,previousstud-
ieshavenotexploredthebenefitofincorporatingdomain-specificpsychologicaltraits
suchasbehavioralbiasesinfinanceintothepersonality-awarerecommendationmodel.
2.2 StockRecommendation
Thereisagrowingdemandforstockrecommendationsasthenumberofretailinvestors
using online brokers has been rapidly increasing. Accordingly, many studies have
tackled stock recommendation tasks. Stock recommendations can be classified into
two approaches: non-personalized stock recommendations and personalized stock
recommendations.Mostworksinstockrecommendationfallwithinthescopeofnon-
personalized recommendation, which focuses on identifying optimal strategies for
selectingstocksorportfoliosthatarelikelytobemoreprofitableinthefuture[8].On
theotherhand,littleresearchhasbeendoneonpersonalizedstockrecommendations
duetothelackofopendataanddifficultiesindatacollectionduetoprivacyconcerns
[4,9–13].Despitethelimitedliteratureonthesubject,somestudieshavetackledthe
123

638 NewGenerationComputing(2024)42:635–649
problemofpersonalizedstockrecommendations.Collaborativefilteringhasbeenused
forpersonalizedstockrecommendations,oftentimescombinedwithotherrecommen-
dationapproachessuchasorderbookanalysis,andmultiplecriteriadecisionanalysis
[4, 9, 10]. For instance, Robin et al. [4] estimate the investor’s risk tolerance from
users’ portfolios and recommends stock based on the relevance of the stock’s risk
returnwiththeuser’srisktolerancecombinedwithacollaborativefilteringmethod.
Themethodofpersonalizingstockrecommendationsbasedoninvestors’risktolerance
hastwoshortcomings.First,itsuffersfromthecold-startproblem.Second,itisnot
clearwhetheronevariable,risktolerance,cancapturethecomplexnatureofinvestors.
Therefore,thebenefitofpersonality-awarerecommendationswhichcanmitigatethe
cold-startproblemandhelpmodelusers’behaviorsneedstobeinvestigatedforstock
recommendations.
2.3 BehavioralFinance
The theory of modern economics is built on the assumption that human beings are
rationalagents.Theseagentsaimtomaximizetheirwealthandminimizerisk,care-
fully assessing the risk and return of investment choices to obtain a portfolio that
matchestheirriskaversion.However,empiricalstudiessuggestthattherealindivid-
ualinvestors’behaviorsaredifferentfromthoseoftheassumption.Theliteraturein
behavioralfinancehasshownthatpsychologicaltraitssuchasbehavioralbiases,per-
sonality,andcognitiveabilityaffectthefinancialbehaviorsofindividualinvestorsand
suggestedthatthesepsychologicaltraitsandbiasesareusefulinexplainingindividual
investors’ behavior. The relationships among investors’ traits—such as personality,
behavioral biases, cognitive ability, and investment goals—have been extensively
studied. This examination spans both empirical research in behavioral finance and
theoreticalstudies.Whileempiricalstudieshighlightthevalueofdomain-specificpsy-
chologicalfactors,includingbehavioralbiases,inexplainingandpredictinginvestor
behavior, their benefits remain unexplored in personality-aware recommendations
[14–17].Therefore,theeffectivenessofdomain-specificpsychologicaltraitsinstock
recommendationsmeritsfurtherinvestigation.
3 Method
TheoverviewofourproposedmodelispresentedinFig.1.Themodelcomprises
foursteps:(1)groupingindividualinvestorsbasedonspecificcriteria,whichwillbe
discussedlater;(2)measuringusersimilarity;(3)forminguserneighborhoodsbased
onthesimilarityscores;and(4)predictinginvestors’preferencesandgeneratingstock
recommendations.WealsoprovideanotationlistinTable1forclarityandconsistency.
Togroupindividualinvestors,weemployedoneoftwomethods:aclusteringanal-
ysis based on psychological traits or an equal division based on the number of past
transactions.Specifically,wedividedallinvestors I inton groupsusingoneof
cluster
thesemethods,whichwillbedescribedinthefourthandfifthexperiments.
123

NewGenerationComputing(2024)42:635–649 639
Table1 Notationandsymbols
| Symbol     |          | Meaning                      |
| ---------- | -------- | ---------------------------- |
| ={i1 ,i    | ,...in } |                              |
| I (cid:2)2 |          | Thesetofalltheinvestors      |
| Cj ⊂I,     | Cj =I    | ThesetofinvestorsinclusterCj |
j
| SimT(u,v) |     | Similaritybetweeninvestoruandinvestorvbasedontheir |
| --------- | --- | -------------------------------------------------- |
transactiondata
| SimP(u,v) |     | Similaritybetweeninvestoruandinvestorvbasedontheir |
| --------- | --- | -------------------------------------------------- |
psychologicaltraits
| Yuv={a,b,...} |     | Thesetofstocksbothstockuandstockvpurchased |
| ------------- | --- | ------------------------------------------ |
| rua           |     | Thepreferenceofinvestorutostocka           |
| ru            |     | Themeanofpreferenceofinvestoru             |
Psy={Psy1 ,Psy2 ,...Psyl } Thesetofpsychologicaltraitsincludingpersonality,behavioral
bias,cognitiveability,andpurposesofinvestment
i
| p u |     | Thevalueofu’spsychologicalvariablei                    |
| --- | --- | ------------------------------------------------------ |
| pu  |     | Themeanvalueofthepsychologicaltraitsvectorforinvestoru |
| α   |     | TheweightofSimT(u,v)ofinvestoruinclusterCi             |
u∈Ci
| k         |     | Thenumberofneighbors |
| --------- | --- | -------------------- |
| n_cluster |     | Thenumberofclusters  |
Fig.1 Outlineofourproposedrecommendationmodel
{C ,C ,...C }=DM(I)
1 2 n_cluster (1)
whereDMrepresentsthemethodtodivideinvestorssuchastheclusteringalgorithm.
Then, we computed the similarity between investors based on their transaction
data, general personality traits, and domain-specific psychological traits. First, we
measuredthesimilaritybasedontransactiondata(SimT).SimT wascomputedusing
thePearsoncorrelationcoefficientasinEq.(2).
123

| 640 |     |     |     | NewGenerationComputing(2024)42:635–649 |     |     |     |
| --- | --- | --- | --- | -------------------------------------- | --- | --- | --- |
(cid:3)
|     |            |     |                | (r −  | r )(rva   | −rv )       |     |
| --- | ---------- | --- | -------------- | ----- | --------- | ----------- | --- |
|     | SimT(u,v)= |     | (cid:4) a∈Yu,v | ua    | (cid:4) u |             |     |
|     |            |     | (cid:3)        |       | (cid:3)   |             | (2) |
|     |            |     | (r             | −r )2 |           | (rva −rv )2 |     |
|     |            |     | a∈Yuv ua       | u     | a∈Yuv     |             |     |
andv
whereu areindividualinvestorsfromset I,r u,a isthepreferenceofu toa,r u
isthemeanofpreferenceofu,andY u,v isthesetofstocksbothu andvpurchased.
Likewise, we computed the similarity based on investors’ psychological traits
(SimP).SimP wascomputedusingPearsoncorrelationcoefficientasinEq.(3).
(cid:3)
|     |            |     |               | (p i −   | p )(p i     | − pv )       |     |
| --- | ---------- | --- | ------------- | -------- | ----------- | ------------ | --- |
|     | SimP(u,v)= |     | (cid:4) i∈Psy | u        | (cid:4) u v |              |     |
|     |            |     | (cid:3)       |          | (cid:3)     |              | (3) |
|     |            |     | (p            | i − p )2 |             | (p i − pv )2 |     |
|     |            |     | i∈Psy         | u u      | i∈Psy       | v            |     |
where Psy is the set of psychological traits, pi is the value of u’s psychological
u
variable i, and p is the mean value of the psychological traits vector for investor
u
u. We computed similarity (Sim) based both on SimP and SimT. Then, Sim was
computed using a weighted average of SimT and SimP as in Eq.(4). α was
u∈Ci
dependentontheclusterinvestoru belongsto,andcomputedasinEq.(5).
|     | Sim(u,v)=α |      | SimT(u,v)+(1−α   |     |      | )SimP(u,v) |     |
| --- | ---------- | ---- | ---------------- | --- | ---- | ---------- | --- |
|     |            | u∈Ci |                  |     | u∈Ci |            | (4) |
|     |            |      | α = α∈[0,1]Score |     | (α)  |            | (5) |
|     |            |      | u∈Ci             |     | Ci   |            |     |
whereα istheweightof SimT foru,and Score showstheevaluationmetrics
|     | u∈Ci |     |     |     | Ci  |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- |
suchastheF1scoreoftheperformanceofrecommendationwhentheweightparameter
isα.
| Third,theneighborsoftargetuserx |                     |     | weresetasinEq.(6).      |           |               |     |     |
| ------------------------------- | ------------------- | --- | ----------------------- | --------- | ------------- | --- | --- |
|                                 | N(x,k)={u           | ∈   | :|{v ∈ :                | Sim(x,v)< | Sim(x,u)}|<k} |     |     |
|                                 |                     |     | I I                     |           |               |     | (6) |
| wherex                          | isatargetinvestor,k |     | isthenumberofneighbors. |           |               |     |     |
Finally, we predicted the preference score of each stock for the target investor
by aggregating the preference scores of their neighbors, weighted by the similarity
betweenthetargetinvestorandtheirneighbors.ThiswasdoneusingEq.(7).Finally,
we recommended the top-n stocks with the highest preference scores to the target
| investor. |     |             | (cid:3)     |            |     |     |     |
| --------- | --- | ----------- | ----------- | ---------- | --- | --- | --- |
|           |     |             |             | Sim(x,y)(r | −r  | )   |     |
|           |     |             | y∈N(cid:3)x |            | y,a | y   |     |
|           |     | r(cid:5) =r | +           |            |     |     | (7) |
|           |     | xa          | x           | Sim(x,y)   |     |     |     |
y∈Nx
wherer(cid:5)isthepredictedpreferencescoreofxtoa,r
|         | xa                               |     |     |          | x istheaveragepreferencescore |     |     |
| ------- | -------------------------------- | --- | --- | -------- | ----------------------------- | --- | --- |
| ofx,and | N representsthesetofneighborsofx |     |     | (Fig.2). |                               |     |     |
x
123

NewGenerationComputing(2024)42:635–649 641
Fig.2 Thedetailsoftheclusteringanalysis.Subfigure(a)showstheelbowmethodonpersonalitytraits.
Subfigure(b)showstheclusteringanalysisonpersonalitytraitsusingKmeansandreducedthedimension
into2dwitht-SNE
4 Dataset
4.1 DataAcquisition
In our study, we collected data from a Japanese securities company, focusing on
individual investors who had made over 50 transactions in a year. We obtained
general personality traits and domain-specific psychological traits data along with
past transaction history from a total of 969 investors. The data range from July
2020 to September 2022. We collected various domain-specific psychological traits
from investors, including behavioral biases, cognitive ability, investment purposes,
and general personality traits. Personality traits were assessed using the ten-item
personality inventory (TIPI) [18, 19]. To ensure the validity of the questionnaire
domain-specificpsychologicaltraits,wereferredtotheJapanHouseholdPanelSurvey
(JHPS)questionnaire.1 Wecollectedbehavioraldataincludingriskpreference,time
discount,overconfidence,hyperbolicdiscounting,signeffect,andmagnitudeeffect.
Tomeasurecognitiveability,weassessedfinancialliteracythroughasetofquestions
regardingfinancialknowledgeandwealthmanagementandadministeredacognitive
reflectiontesttoevaluateinvestors’cognitiveability[20].Furthermore,weinquired
aboutinvestors’investmentgoals,includingretirement,housing,education,medical
expenses,vacation,andotherobjectives.
Weprocessedthetransactiondataintoauser-itemmatrixgivenmusersandnitems.
Followingtheworkin[4],wedefinem×nmatrixU withcomponents
f
(U ) = f(i, j) (8)
f ij
1 https://www.iser.osaka-u.ac.jp/survey_data/survey_eng.html.
123

642 NewGenerationComputing(2024)42:635–649
Let q i,j,t be the portfolio of user i on stock j on the day t which is obtained from
transactiondata. (cid:6)
1 ifuseri holdsstock j intimet
q i,j,t =
0 otherwise
(9)
We define implicit feedback collaborative filtering user-item matrix R as U in
fR
Eq.(10). (cid:6)
f (i, j)= 1 ifthereist ∈Ts.t.q i,j,t (cid:4)=0 (10)
R 0 otherwise
whereT isanentireperiod.Simplyspeaking,rowsoftheRmatrixrepresent,foruser
i,whethertheyheldstock j duringanyperiod.
4.2 InvestorBehaviorAnalysis
Figure3presentsthehierarchicalclusteringheatmapofinvestorbehavioraltraits.The
visualizationrevealsseveralnoteworthyobservations.Forinstance,inFig.3,neuroti-
cismexhibitslowercorrelationswithopennessandconscientiousness,whilecognitive
abilitydemonstratesahighercorrelationwithfinancialliteracy.Furthermore,ithigh-
lightsthatinvestorswithlowriskaversiontendtoexhibithigh-risktolerance,andthat
annualincomeandinvestmentexperiencesarestronglycorrelated.Additionally,Fig.3
suggeststhatinvestorscanbegroupedintodistinctclustersbasedontheirbehavioral
traits.Thevisualrepresentationsprovidevaluableinsightsintotheinterrelationships
amongvariousinvestorcharacteristics.
5 Experiment
5.1 TasksandEvaluationMetrics
Weevaluateitsabilitytorecommendrelevantstockstoindividualinvestors.Specifi-
cally,weevaluatedthemodel’sperformanceintwotasks:generalstockrecommen-
dationandnewstockrecommendation.
Forthegeneralstockrecommendationtask,weusedtestdatathatconsistedofeach
investor’sfivemostrecenttransactionstoevaluatethemodel’stop10recommended
items. In the new stock recommendation task, we removed the transaction data of
stocksthateachuserhadinthetestdatafromthetraindata.Thelattertaskisparticularly
importantinfinancialstockrecommendations,asinvestorstendtobebiasedtowards
familiarstocks,ratherthanexploringnewassets[21].Therefore,itiscrucialforstock
recommendersystemstorecommendnewstockstoinvestors,whichcanhelpmitigate
familiarity bias and encourage exploration. We used precision@10, recall@10, and
F1scoresasevaluationmetrics.
5.2 Experiments
Weconductedfiveexperimentstoaddressthethreeresearchquestions.
123

NewGenerationComputing(2024)42:635–649 643
Fig.3 Hierarchicalclusteringheatmapofinvestortraits:Thisheatmapillustratestherelationshipsamong
investorsbasedontheirkeytraits.Eachcolumnrepresentsadistinctinvestor,whileeachrowcorresponds
toaspecifictrait.Thehierarchicalclusteringalgorithmorganizesinvestorswithsimilarcharacteristics
together
To address RQ1, we conducted the first experiment to investigate the impact of
investors’ personality traits on stock recommendations. We compared the perfor-
manceofapersonality-basedmodel,whichusestheBig-Fivepersonalitytraits,witha
transaction-basedmodelandarandommodel.Inthepersonality-basedmodel,weset
n to1andα =0forallinvestorsu ∈ I,whileinthetransaction-basedmodel,
cluster u
wesetn to1andα =1forallinvestorsu ∈ I.
cluster u
To address RQ2, we conducted the second experiment to analyze the value of
domain-specific psychological traits in the personality-aware recommendation. We
conducted an ablation study for the combinations of general personality traits and
domain-specificpsychologicaltraits.
To address RQ3, we conducted three experiments to compare the performance
ofexistingmethodswiththatofourproposedrecommendationmodels.Inthethird
123

| 644 |     | NewGenerationComputing(2024)42:635–649 |     |     |
| --- | --- | -------------------------------------- | --- | --- |
Table2 Resultsforthefirst,fourth,andfifthexperiment
|             | GSR         |       | NSR         |       |
| ----------- | ----------- | ----- | ----------- | ----- |
|             | P@10 R@10   | F1    | P@10 R@10   | F1    |
| Randommodel | 0.002 0.007 | 0.003 | 0.001 0.005 | 0.002 |
Generalpersonality-basedmodel 0.059 0.176 0.088 0.040 0.122 0.060
|                        | 0.329       |       | 0.160       |       |
| ---------------------- | ----------- | ----- | ----------- | ----- |
| Transaction-basedmodel | 0.104       | 0.158 | 0.050       | 0.076 |
| Clustermodel           | 0.104 0.324 | 0.157 | 0.058 0.153 | 0.083 |
|                        | 0.105 0.329 | 0.159 | 0.058       | 0.085 |
| Divisionmodel          |             |       | 0.154       |       |
experiment,weimplementedaweightedaveragemodel,whichisamodificationofthe
approachproposedbyNingetal.[22]thatcombinesthetwosimilaritymetrics,SimP
andSimT.Specifically,wevariedtheweightparameterα
|     |     |     | u from0to1toinvestigate |     |
| --- | --- | --- | ----------------------- | --- |
itsimpactonperformance.Inthefourthandfifthexperiments,weaimedtovalidate
theeffectivenessoftheproposedrecommendationmodels.Todeterminetheoptimal
weightparameterα
u∈Ci ,wesplitthedatasetintotrain,validation,andtestsets.The
testandvalidationsetscontainedthemostrecentandnextfivetransactionrecordsfor
each investor. We performed a grid search on the train and validation sets and used
thebestparametertoevaluateperformanceonthetestset.Inthefourthexperiment,
weclusteredinvestorsbasedontheirpsychologicaltraits,hypothesizingthatinvestors
withspecificpsychologicaltraitswouldbebetterpredictedby SimP.Wetunedthe
weightparameterα foreachclusterC andnamedthismodeltheclustermodel.
u∈Ci i
=
The number of clusters was determined to be n clusters 8 using the elbow method
asshowninFig.2.Inthefifthexperiment,wepartitionedinvestorsintoequalgroups
based on their number of past transactions, hypothesizing that investors with more
transaction data would be better predicted by SimT, while investors with limited
transactiondatacouldbebetterpredictedby SimP.Wetunedtheweightparameter
α
| u∈Ci foreachclusterC i | andnamedthismodelthedivisionmodel. |     |     |     |
| ---------------------- | ---------------------------------- | --- | --- | --- |
5.3 Results
Table 2 presents the results of the first, fourth, and fifth experiments. The evalua-
tion metrics used are Precision@10 and Recall@10, denoted as P@10 and R@10,
respectively.GSRandNSRstandforgeneralstockrecommendationsandnewstock
recommendations,respectively.Theresultsdemonstratethatthegeneralpersonality-
basedmodelsignificantlyoutperformedtherandommodelinbothsettings.
The second experiment’s result is presented in Table 3. The table shows the per-
formanceoftheablationstudyonthecombinationsofgeneralpersonalitytraitsand
domain-specificpsychologicaltraits.Theresultsindicatethataddingdomain-specific
traitssuchascognitiveability,behavioralbias,andpurposesofinvestmentimproved
the performance in both general and new stock recommendation tasks. However,
adding more variables did not necessarily lead to higher performance, as the model
withallvariablesdidnotperformbetterthanthemodelswithasubsetofvariables.
123

NewGenerationComputing(2024)42:635–649 645
Table3 Resultsforthesecondexperiment
|                          | GSR         | NSR         |             |
| ------------------------ | ----------- | ----------- | ----------- |
|                          | P@10 R@10   | F1 P@10     | R@10 F1     |
| Personality              | 0.059 0.176 | 0.088 0.040 | 0.122 0.060 |
| Cognitive                | 0.055 0.165 | 0.083 0.038 | 0.117 0.057 |
| Goal                     | 0.056 0.169 | 0.084 0.038 | 0.118 0.057 |
| Behavioral               | 0.059 0.178 | 0.089 0.039 | 0.124 0.059 |
| Cognitivegoal            | 0.057 0.175 | 0.086 0.039 | 0.120 0.059 |
| Behavioralcognitive      | 0.054 0.169 | 0.082 0.037 | 0.118 0.056 |
| Personalitybehavioral    | 0.058 0.177 | 0.087 0.039 | 0.122 0.059 |
| Behavioralgoal           | 0.059 0.180 | 0.089 0.038 | 0.122 0.058 |
| Personalitycognitive     | 0.059 0.179 | 0.089 0.040 | 0.126 0.061 |
| Personalitygoal          | 0.061 0.184 | 0.092 0.040 | 0.124 0.060 |
| Personalitycognitivegoal | 0.058 0.175 | 0.087 0.040 | 0.123 0.060 |
| Behavioralcognitivegoal  | 0.059 0.180 | 0.089 0.039 | 0.124 0.059 |
Personalitybehavioralcognitive 0.057 0.173 0.086 0.038 0.120 0.058
Personalitybehavioralgoal 0.058 0.179 0.088 0.040 0.130 0.061
Personalitybehavioralcognitivegoal 0.059 0.182 0.089 0.040 0.129 0.061
Fig.4 Theresultsforthethirdexperiment.aistheresultswithvaryingweightofSimTinGeneralStock
RecommendationandbistheresultinNewStockRecommendation
Theresultsofthethirdexperiment,presentedinFig.4,indicatethattheperformance
oftheweightedaveragemodelmostlyfellbetweentheperformanceofthepsychology-
basedmodelandthetransaction-basedmodel.Theresultsofthefourthexperiment,as
showninTable2suggestthattheclustermodeloutperformedthetransaction-based
model in the new stock recommendation task with regard to F1 score. Finally, the
resultsofthefifthexperiment,presentedinTable2andFig.5,suggestthatmostofthe
divisionmodelsperformedbetterthanthetransaction-basedmodelinthenewstock
123

646 NewGenerationComputing(2024)42:635–649
Fig.5 ThecomparisonoftheF1scoreamongthedivisionmodelwiththetransaction-basedmodelandthe
clustermodel.Thex-axisshowsncluster
recommendationtask,withthetransaction-basedmodelbeingoutperformedonlyin
onesettingwhenn equaled9inthegeneralstockrecommendationtask.
cluster
6 Discussion
For RQ1, we can conclude that the comparison between the random model and the
general personality-based model in Table 2 supports the value of general personal-
ity traits in stock recommendation tasks, which is consistent with previous findings
in other recommendation domains like music, book, and movie recommendation.
The personality-based model outperformed the random model by a significant mar-
gin, demonstrating that personality traits can be leveraged for addressing cold start
problemsinpersonalized stockrecommendations. However, theperformance ofthe
personality-basedmodelwasinferiortothetransaction-basedmodel,indicatingthat
personalitytraitsshouldbeusedinconjunctionwithtransactiondataforoptimalper-
formanceinstockrecommendationtaskswherepasttransactiondataisavailablefor
eachinvestor.
ForRQ2,wecanconcludethatincorporatingdomain-specificpsychologicaltraits
in addition to general personality traits can improve recommendation performance,
as shown in Table 3. However, further investigation is required to identify the most
usefulcombinationsofthesevariablesforoptimalrecommendationperformance.This
highlights the need for future research to carefully analyze and select the optimal
psychologicalvariablesforpersonalizedrecommendations.
ToaddressRQ3,wecarriedoutthreeexperiments.Thethirdexperiment,presented
inFig.4,revealedthatasimpleweightedaverageof SimP and SimT didnotyield
betterperformancethanthetransaction-basedmodel.Thisoutcomesuggestedthatit
isnecessarytopartitioninvestorsintogroupswithdistinctcharacteristicstotakefull
advantageofgeneralpersonalitytraits,domain-specificpsychologicaltraits,andtrans-
123

NewGenerationComputing(2024)42:635–649 647
actiondata.Thefourthexperiment,detailedinTable2,demonstratedthatourcluster
model outperformed the transaction-based model in the new stock recommendation
task,butnotinthegeneralstockrecommendation.Theusefulnessofpersonality-aware
recommendationforenhancingthediversityofrecommendationsiswell-documented
inliterature[1,2,7].Consequently,weconsiderthatthediversityintherecommended
listscontributedtotheimprovedperformanceofournewstockrecommendationtask,
which mandated the provision of diverse recommendations to enable investors to
explorenewstocks.Moreover,wenotedthatspecificclusterswithcharacteristicpsy-
chologicaltraitswerebetterpredictedusing SimP thanothers,whichneedsfurther
investigation.Therefore,itisworthwhiletoanalyzethecharacteristicsofclusterswith
differentperformances.Thesuperiorperformanceofthetransaction-basedmodelin
general stock recommendation can be attributed to the repeat purchase behavior of
stocks,whichisinfluencedbyfamiliaritybias.Thisbiascausesinvestorstorepeatedly
purchasecertainstocks,andasaresult,thetransaction-basedmodelthatlearnsdirectly
frompasttransactionsperformedbetterinprovidinggeneralstockrecommendations.
Theresultsofthefifthexperimentshowasimilarpatterntothatobservedinthecluster
model.Specifically,thedivisionmodeloutperformedthetransaction-basedmodelin
mostcasesforthenewstockrecommendationtask,whileitonlydidsoinonecasefor
thegeneralstockrecommendationiswhenthenumberofclusterswas9.Inadditionto
thediversityaddedtotherecommendations,wearguethatpsychologicaltraitsplaya
significantroleinenhancingtheperformanceofthedivisionmodelforinvestorswith
limitedtransactiondata.Figure5showsthattheclustermodelandthedivisionmodel
outperformedthetraditionaltransaction-basedmodelinnewstockrecommendations.
Therefore,thisresultsupportsourhypothesisthatdividingtheinvestorsintogroups
withcharacteristicsisessentialinexploitinggeneralpersonalitytraits,domain-specific
psychologicaltraits,andtransactiondata.
Tofullyleveragethebenefitsofdividinginvestorsintogroupswithdifferentchar-
acteristics,itisessentialtoexplorehowinvestorsindifferentgroupsareaffectedby
psychological traits. Future work should investigate the selection of psychological
traitsandoptimalweightsattheclusterleveltomaximizethebenefitsofpersonalized
recommendations.
7 Conclusion
Inthispaper,weexaminepersonality-awarerecommendationsinthefinancialdomain.
Specifically,weconductfiveexperimentsinfinancialstockrecommendationtaskswith
Precision@10, Recall@10, and F1 scores as evaluation metrics. This paper reports
three findings. First, we show that general personality traits such as the Big-Five
personalitytraitsareusefulfordomain-specificrecommendationssuchasstockrec-
ommendations. Second, we show that utilizing domain-specific psychological traits
enhances the performance of the recommendation. Third, we show that our pro-
posed models that divide investors into groups with characteristics outperform the
transaction-based model, especially in the new stock recommendation task. While
thispapersuggeststhebenefitsofincorporatingdomain-specificpsychologicaltraits
forrecommendationsandproposesamodeltoutilizeallthedata,carefulanalysisof
123

648 NewGenerationComputing(2024)42:635–649
optimalselectionsofweightsandpsychologicalvariablesneedstobestudiedinfuture
work.
Acknowledgements ThisworkwassupportedbytheJapanScienceandTechnology-Future(JST-Mirai)
ProgramGrantNumberJPMJMI20B1,Japan.Also,thisworkwassupportedbyDaiwaSecuritiesGroup
Inc.
Funding OpenAccessfundingprovidedbyTheUniversityofTokyo.
Declarations
ConflictofInterest Thesecondauthorofthismanuscript,KiyoshiIzumi,isaleadguesteditorforthis
journal.Thisroleisdisclosedasperthejournal’spolicy.
OpenAccess ThisarticleislicensedunderaCreativeCommonsAttribution4.0InternationalLicense,which
permitsuse,sharing,adaptation,distributionandreproductioninanymediumorformat,aslongasyougive
appropriatecredittotheoriginalauthor(s)andthesource,providealinktotheCreativeCommonslicence,
andindicateifchangesweremade.Theimagesorotherthirdpartymaterialinthisarticleareincluded
inthearticle’sCreativeCommonslicence,unlessindicatedotherwiseinacreditlinetothematerial.If
materialisnotincludedinthearticle’sCreativeCommonslicenceandyourintendeduseisnotpermitted
bystatutoryregulationorexceedsthepermitteduse,youwillneedtoobtainpermissiondirectlyfromthe
copyrightholder.Toviewacopyofthislicence,visithttp://creativecommons.org/licenses/by/4.0/.
References
1. Lex,E.,Schedl,M.:Psychology-informedrecommendersystemstutorial.In:Proceedingsofthe16th
ACMConferenceonRecommenderSystems,pp.714–717(2022)
2. Dhelim,S.,Aung,N.,Bouras,M.A.,Ning,H.,Cambria,E.:Asurveyonpersonality-awarerecom-
mendationsystems.Artif.Intell.Rev.55(3),2409–2454(2022)
3. Ferwerda,B.,Tkalcic,M.,Schedl,M.:Personalitytraitsandmusicgenres:Whatdopeoplepreferto
listento?In:UserModeling,AdaptationandPersonalization,pp.285–288(2017)
4. Swezey,R.M.E.,Charron,B.:Large-scalerecommendationforportfoliooptimization.In:Proceedings
ofthe12thACMConferenceonRecommenderSystems,pp.382–386(2018)
5. McCrae,R.R.,John,O.P.:Anintroductiontothefive-factormodelanditsapplications.J.Pers.60(2),
175–215(1992)
6. Wu,W.,Chen,L.:Implicitacquisitionofuserpersonalityforaugmentingmovierecommendations.
In:UserModeling,AdaptationandPersonalization,pp.302–314(2015)
7. Wu,W.,Chen,L.,Zhao,Y.:Personalizingrecommendationdiversitybasedonuserpersonality.User
Model.User-Adap.Inter.28,237–276(2018)
8. Voditel,P.,Deshpande,U.:Astockmarketportfoliorecommendersystembasedonassociationrule
mining.Appl.SoftComput.13,1055–1063(2013)
9. Yujun,Y.,Jianping,L.,Yimei,Y.:Anefficientstockrecommendationmodelbasedonbigordernet
inflow.Math.Probl.Eng.2016,1–15(2016)
10. Taghavi,M.,Bakhtiyari,K.,Scavino,E.:Agent-basedcomputationalinvestingrecommendersystem.
In:Proceedingsofthe7thACMConferenceonRecommenderSystems,pp.455–458(2013)
11. Takayanagi,T.,Chen,C.-C.,Izumi,K.:Personalizeddynamicrecommendersystemforinvestors.
In:Proceedingsofthe46thInternationalACMSIGIRConferenceonResearchandDevelopmentin
InformationRetrieval,pp.2246–2250(2023)
12. Takayanagi,T.,Izumi,K.,Kato,A.,Tsunedomi,N.,Abe,Y.:Personalizedstockrecommendationwith
investors’attentionandcontextualinformation.In:Proceedingsofthe46thInternationalACMSIGIR
ConferenceonResearchandDevelopmentinInformationRetrieval,pp.3339–3343(2023)
123

NewGenerationComputing(2024)42:635–649 649
13. Takayanagi, T., Izumi, K.: Context-aware stock recommendations with stocks’ characteristics and
investors’traits.IEICETrans.Inf.Syst.E106D,1732–1741(2023).https://doi.org/10.1587/transinf.
2023EDP7017
14. Oehler,A.,Wendt,S.,Wedlich,F.,Horn,M.:Investors’personalityinfluencesinvestmentdecisions:
experimentalevidenceonextraversionandneuroticism.J.Behav.Fin.19(1),30–48(2018)
15. Tauni,M.Z.,Fang,H.X.,Rao,Z.-U.-R.,Yousaf,S.:Theinfluenceofinvestorpersonalitytraitson
informationacquisitionandtradingbehavior:evidencefromChinesefuturesexchange.Pers.Individ.
Differ.87,248–255(2015)
16. Grinbaltt,M.,Keloharju,M.,Linnainmaa,J.:Iqandstockmarketparticipation.J.Fin.66(6),2121–
2164(2011)
17. Shefrin,H.,Statman,M.:Behavioralportfoliotheory.J.Fin.Quant.Anal.35(2),127–151(2000)
18. Gosling,S.D.,Rentfrow,P.J.,Swann,W.B.:Averybriefmeasureofthebig-fivepersonalitydomains.
J.Res.Pers.37(6),504–528(2003)
19. Oshio,A.,Abe,A.,Cutrone,S.,Samuel,P.G.:BigfivecontentrepresentationoftheJapaneseversion
oftheten-itempersonalityinventory.Psychology4,924–929(2013)
20. Frederick,S.:Cognitivereflectionanddecisionmaking.J.Econ.Perspect.19(4),25–42(2005)
21. Huberman,G.:Familiaritybreedsinvestment.Rev.Fin.Stud.14(3),659–680(2015)
22. Ning,H.,Dhelim,S.,Aung,N.:Personet:friendrecommendationsystembasedonbig-fivepersonality
traitsandhybridfiltering.IEEETrans.Comput.Soc.Syst.6(3),394–402(2019)
Publisher’sNote SpringerNatureremainsneutralwithregardtojurisdictionalclaimsinpublishedmaps
andinstitutionalaffiliations.
123