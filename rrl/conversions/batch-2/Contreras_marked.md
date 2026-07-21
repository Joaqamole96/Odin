---
conversion_metadata:
  converted_at: "2026-07-21T05:58:27Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Contreras.pdf"
  source_pdf_sha256: "ad678840118b48b6aa1b830055102257b0c97de3c2774e764286a32bb511e05d"
  page_count: 13
  markdown_char_count: 92101
---

ICCKJournalofSoftwareEngineering
http://dx.doi.org/10.62762/JSE.2026.605759
RESEARCH ARTICLE
Adaptive Risk Evaluation in FinTech Systems via
Reinforcement-Based Continuous Policy Optimization
1,2,*
EdimerMahechaContreras
1UniversityoftheLlanos,Villavicencio500001,Colombia
2EliteGroupServices,SanJose,CA95125,UnitedStates
Abstract onthepredictionofcreditdefaultandadaptiveasset
allocation in a big data dataset of 8.5 million credit
The key feature of FinTech software systems is
records,generatedinacustomFinTechenvironment
the ability to accurately assess risk in real time,
simulator. The performance based on precision
making decisions on high-volume streams of
and F1 score, of ARL-CPO is compared with the
information that are associated with very low
baselines, and it outperforms them with 97.4%
latency and are robust to concept drift, and able
classification accuracy, 98.8% trend adaptation
to be updated without disrupting services. This
rate (responsiveness to distributional shifts), and
paper addresses the problem of adaptive risk
96.1% cumulative long-term performance index
scoring using a reinforcement learning approach
(normalized long-horizon reward). The findings
by modeling the risk evaluation problem as a
showthatreinforcementlearning-basedcontinuous
continuous-action Markov Decision Process and
policy updates is an achievable, adaptive element
continuously optimizing the policy via streaming
for real-time risk systems in FinTech under the
transactional, behavioral events and outcome
evolutionofmarketanduserconditions.
drivenrewardfeedback. Inadditiontothelearning
algorithm, we also view ARL-CPO as a deployable
softwarearchitecturethatseparatesonlinelearning Keywords: reinforcement learning, continuous policy
from inference serving to enable a modular optimization, adaptive risk evaluation, FinTech software
approach to integrating ARL into production systems,sequentialdecisionlearning,creditriskmodeling.
risk pipelines, such as an inference microservice,
which is wrapped around an asynchronous update
1 Introduction
loop, updating ARL models continuously without
In recent years, the rise of FinTech platforms has
periodic batch retraining — a capability not
revolutionized the way financial services are being
available in the Random Forest, Gradient Boosting,
delivered, with software ecosystems that need to
or Transformer baselines. We assess the approach
handle high-frequency transactions, varied types of
user behavior and ever-changing market signals at
a large scale [1]. These systems not only require
riskassessmenttobeamodelingexercise,butalsoa
Citation
Submitted:04May2026
Contreras,E.M.(2026).AdaptiveRiskEvaluationinFinTechSystems
Accepted:25May2026
Published:11June2026 viaReinforcement-BasedContinuousPolicyOptimization. ICCK
JournalofSoftwareEngineering,2(2),156–168.
Vol.2,No.2,2026.
10.62762/JSE.2026.605759 © 2026 by the Author. Published by Institute of
CentralComputationandKnowledge.Thisisanopen
*Correspondingauthor: accessarticleundertheCCBYlicense(https://creati
(cid:0)EdimerMahechaContreras
vecommons.org/licenses/by/4.0/).
edimer.mahecha@unillanos.edu.co
156

ICCKJournalofSoftwareEngineering
production-criticalsoftwarecapabilityontherequest consideritasadecisionmakingprocessovermultiple
path of credit underwriting, fraud screening, wallet interactionsandtimehorizons,soastooptimizethe
limits and automated portfolio services. Therefore, long-termresults.
| risk evaluation |     | components  |            |              | need             | to be    | able      | to              |               |              |            |          |          |                |           |
| --------------- | --- | ----------- | ---------- | ------------ | ---------------- | -------- | --------- | --------------- | ------------- | ------------ | ---------- | -------- | -------- | -------------- | --------- |
|                 |     |             |            |              |                  |          |           | Instead,        | Reinforcement |              |            | learning | (RL)     | gives          | another   |
| meet software   |     | engineering |            | requirements |                  |          | including |                 |               |              |            |          |          |                |           |
|                 |     |             |            |              |                  |          |           | paradigm        | of            | learning,    |            | which    | can      | be represented |           |
| low inference   |     | latency     | for        | real-time    | decision-making, |          |           |                 |               |              |            |          |          |                |           |
|                 |     |             |            |              |                  |          |           | as repeated     |               | interactions |            | between  |          | an             | agent and |
| high throughput |     |             | to process |              | event            | streams, | high      |                 |               |              |            |          |          |                |           |
|                 |     |             |            |              |                  |          |           | an environment, |               |              | optimizing |          | a policy | to             | maximize  |
availabilitytoensureserviceavailability,auditability
|                |     |         |     |      |        |     |          | cumulative |     | discounted |     | reward | [5]. | DRL | is an |
| -------------- | --- | ------- | --- | ---- | ------ | --- | -------- | ---------- | --- | ---------- | --- | ------ | ---- | --- | ----- |
| for regulatory |     | review, | and | safe | update | to  | maintain |            |     |            |     |        |      |     |       |
extensionofRL,withneuralfunctionapproximation
| service | continuity |     | while | modifying |     | the risk | logic. |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ----- | --------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
tocopewithhigh-dimensionalstateandactionspaces,
| However, | financial |     | environments |     | are | not stationary |     |     |     |     |     |     |     |     |     |
| -------- | --------- | --- | ------------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andhaspromiseinportfoliooptimization,algorithmic
| and the     | distribution |               | drift | can     | affect | the quality |     | of         |        |     |         |     |         |     |          |
| ----------- | ------------ | ------------- | ----- | ------- | ------ | ----------- | --- | ---------- | ------ | --- | ------- | --- | ------- | --- | -------- |
|             |              |               |       |         |        |             |     | execution, | market |     | making, | and | hedging |     | [6]. But |
| predictions |              | very quickly, |       | putting | extra  | operational |     |            |        |     |         |     |         |     |          |
softwareengineeringaspectsrelatedtotheapplication
| pressure        | on    | risk  | pipelines    | to  | keep          | up          | with the |             |     |                                     |          |     |      |            |     |
| --------------- | ----- | ----- | ------------ | --- | ------------- | ----------- | -------- | ----------- | --- | ----------------------------------- | -------- | --- | ---- | ---------- | --- |
|                 |       |       |              |     |               |             |          | of DRL      | to  | real-time                           | adaptive |     | risk | evaluation | are |
| changes         | while | still | guaranteeing |     | the           | correctness |          | of          |     |                                     |          |     |      |            |     |
|                 |       |       |              |     |               |             |          | inadequate. |     | Existingworkoftenemphasizeslearning |          |     |      |            |     |
| the predictions |       | and   | ensuring     |     | observability |             | during   |             |     |                                     |          |     |      |            |     |
performancewhileunder-specifyinghowanadaptive
production[2].
|     |     |     |     |     |     |     |     | policy | can | be deployed |     | safely | in  | a   | production |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------- | --- | ------ | --- | --- | ---------- |
Traditionalriskassessmentmethods,suchaslogistic FinTech service with requirements for low-latency
regression, discriminant analysis, decision trees inference,faulttolerance,continuousupdateswithout
|                |     |        |     |          |      |               |     | service | interruption, |     | versioning |     | and | rollback, | and |
| -------------- | --- | ------ | --- | -------- | ---- | ------------- | --- | ------- | ------------- | --- | ---------- | --- | --- | --------- | --- |
| and rule-based |     | expert |     | systems, | have | traditionally |     |         |               |     |            |     |     |           |     |
been attractive due to their interpretability and auditable decision logging. Consequently, the
computational efficiency. These approaches are research gap is not only algorithmic, but also a
|     |     |     |     |     |     |     |     | missingsoftwarecapability. |     |     |     | Mostexistingapproaches, |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- |
straightforwardtoimplementandmanage,however
theyarefragiletodriftasthedecisionlogicistoalarge includinggradientboostingmethodsforbankdistress
extentfixedwhendeployed. Thesesystemsoftenneed prediction[3],arebatch-trainedanddonotsupport
to be analyzed manually, retrained or updated with continuouspolicyrefinementinresponsetostreaming
|     |     |     |     |     |     |     |     | drift, leaving |     | a gap | for | deployable, |     | observable, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --- | ----------- | --- | ----------- | --- |
rulesoffline,anddeployeddaysorweekslaterwhen
customer behavior changes, market regimes change, production-safeadaptiveriskpipelines.
| or the       | possibility  |         | of fraud     | changes.     |      | This introduces |           |               |              |      |            |       |          |            |          |
| ------------ | ------------ | ------- | ------------ | ------------ | ---- | --------------- | --------- | ------------- | ------------ | ---- | ---------- | ----- | -------- | ---------- | -------- |
|              |              |         |              |              |      |                 |           | To address    | this         | gap, | this       | paper | proposes |            | Adaptive |
| a risk       | of deploying |         | a production |              | risk | service         | to an     |               |              |      |            |       |          |            |          |
|              |              |         |              |              |      |                 |           | Reinforcement |              |      | Learning   |       | with     | Continuous |          |
| environment  |              | that    | is not       | the same     | as   | it is           | when      | it            |              |      |            |       |          |            |          |
|              |              |         |              |              |      |                 |           | Policy        | Optimization |      | ARL-CPO    |       | for      | FinTech    | risk     |
| was created, |              | leading | to the       | introduction |      | of              | incorrect |               |              |      |            |       |          |            |          |
|              |              |         |              |              |      |                 |           | scoring.      | ARL-CPO      |      | formulates |       | risk     | evaluation | as a     |
scoresintothefinanciallossandcomplianceexposure.
continuous-actionMarkovDecisionProcessanduses
| Thus, | the central |     | engineering |     | challenge | is  | not just |     |     |     |     |     |     |     |     |
| ----- | ----------- | --- | ----------- | --- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
adual-moduleactor-criticdesignconsistingofapolicy
predictiveperformance,it’scontinuousadaptationin
learningmoduleandavalueestimationmodulethat
strictoperationalconditions.
|     |     |     |     |     |     |     |     | updates | online          | through |     | gradient-based |     |     | refinement. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | ------- | --- | -------------- | --- | --- | ----------- |
|     |     |     |     |     |     |     |     | Unlike  | batch-retrained |         |     | supervised     |     |     | baselines,  |
Manyrisk-relatedtasksbenefitfrommachinelearning
models like Random Forest, Gradient Boosting, and ARL-CPO incorporates streaming transactional
|               |      |        |      |          |                      |     |          | and behavioral |            | data | and        | outcome-driven |        |             | reward |
| ------------- | ---- | ------ | ---- | -------- | -------------------- | --- | -------- | -------------- | ---------- | ---- | ---------- | -------------- | ------ | ----------- | ------ |
| deep learning |      | models |      | such     | as Transformer-based |     |          |                |            |      |            |                |        |             |        |
|               |      |        |      |          |                      |     |          | signals        | to support |      | continuous |                | policy | improvement |        |
| models        | [4]. | They   | are, | however, | usually              |     | deployed |                |            |      |            |                |        |             |        |
as batch-trained artifacts, which are retrained and as conditions evolve [7]. In addition to presenting
redeployedperiodicallyinnormalFinTechscenarios. the learning formulation, we position ARL-CPO
|      |        |      |      |          |     |             |     | as a software |     | architecture |     | pattern |     | for adaptive | risk |
| ---- | ------ | ---- | ---- | -------- | --- | ----------- | --- | ------------- | --- | ------------ | --- | ------- | --- | ------------ | ---- |
| This | design | adds | some | software |     | engineering |     |               |     |              |     |         |     |              |      |
constraints. First,modelchangesarelinkedtorelease services, where inference and online learning are
pipelines, which can involve downtime or traffic operationallyseparatedtoenablecontinuousupdates
withoutinterruptingreal-timescoringandtosupport
| re-routing. |     | Secondly, | the | rate | of retraining |     | slows |     |     |     |     |     |     |     |     |
| ----------- | --- | --------- | --- | ---- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
integrationintoFinTechriskpipelines.
| downtheadaptationtodrift. |     |      |      | Third,thereistypically |     |               |     |     |     |     |     |     |     |     |     |
| ------------------------- | --- | ---- | ---- | ---------------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| no feedback               |     | loop | from | decisions              |     | to downstream |     |     |     |     |     |     |     |     |     |
Themaincontributionsofthisworkareasfollows.
| results | to improve |     | and | evolve | the inference |     | service. |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | --- | ------ | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Furthermore, most supervised methods view risk 1. Software engineering problem formulation for
scoring as a one-step prediction task and do not adaptive risk scoring in FinTech systems. We
157

ICCKJournalofSoftwareEngineering
describeriskevaluationasaproductionsoftware
|           |      |      |         |     |       |             | 2.1 Supervised |     | Learning |     | for | Financial |     | Risk |
| --------- | ---- | ---- | ------- | --- | ----- | ----------- | -------------- | --- | -------- | --- | --- | --------- | --- | ---- |
| component | that | must | operate |     | under | drift while | Modeling       |     |          |     |     |           |     |      |
meeting real-time constraints and continuous Capitalized by their interpretability and ability to
| update | expectations, |     | motivating |     | a   | sequential |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ---------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
easilybeincorporatedintoanexistingscoringservice,
| decision | formulation |     | rather | than | a   | static batch |            |           |     |          |     |              |     |          |
| -------- | ----------- | --- | ------ | ---- | --- | ------------ | ---------- | --------- | --- | -------- | --- | ------------ | --- | -------- |
|          |             |     |        |      |     |              | supervised | pipelines |     | continue |     | to be widely |     | used for |
predictionpipeline. the credit default early warning and risk prediction.
|     |     |     |     |     |     |     | The predictive |     | power |     | is enhanced |     | when | using |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --- | ----------- | --- | ---- | ----- |
2. Deployable adaptive risk scoring architecture macroeconomicandborrowerfeaturesasagradient
|       |               |     |          |     |       |            | boostingdecisiontree[8]. |     |     |     | Suchsolutions,however,are |     |     |     |
| ----- | ------------- | --- | -------- | --- | ----- | ---------- | ------------------------ | --- | --- | --- | ------------------------- | --- | --- | --- |
| using | reinforcement |     | learning |     | based | continuous |                          |     |     |     |                           |     |     |     |
basedoncyclesofredeploymentandofflineretraining
| policy | optimization. |     | We  | propose |     | ARL-CPO, |     |     |     |     |     |     |     |     |
| ------ | ------------- | --- | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
modeling risk scoring as a continuous-action thatmaycausedelaysinupdatewhenthereareregime
MarkovDecisionProcesswithanonline-updated shifts. Likewise,whenconsideringfixeddistributions,
|             |     |        |     |       |        |      | Data-driven |     | machine | learning |     | analysis | of  | systemic |
| ----------- | --- | ------ | --- | ----- | ------ | ---- | ----------- | --- | ------- | -------- | --- | -------- | --- | -------- |
| dual-module |     | policy | and | value | design | that |             |     |         |          |     |          |     |          |
supportsfine-grainedriskscoringandcontinuous risk propagation in financial networks identifies
adaptationinstreamingsettings. key drivers of contagion using classification-based
|              |              |            |     |             |          |         | boundaries | [9].           | However, |             | it      | doesn’t | have          | much   |
| ------------ | ------------ | ---------- | --- | ----------- | -------- | ------- | ---------- | -------------- | -------- | ----------- | ------- | ------- | ------------- | ------ |
|              |              |            |     |             |          |         | mechanisms |                | to keep  | adapting    |         | and can | break         | when   |
| 3. Empirical | evaluation   |            | in  | a streaming |          | FinTech |            |                |          |             |         |         |               |        |
|              |              |            |     |             |          |         | it comes   | to changes     |          | in the      | feature | sets    | distributions |        |
| simulator    | environment. |            |     | We evaluate |          | ARL-CPO |            |                |          |             |         |         |               |        |
|              |              |            |     |             |          |         | if it is   | not retrained. |          | SHAP-based  |         |         | Random        | Forest |
| on credit    | default      | prediction |     | and         | adaptive | asset   |            |                |          |             |         |         |               |        |
|              |              |            |     |             |          |         | models     | are more       |          | transparent |         | and     | explainable   | for    |
allocationusingalarge-scaledatasetof8.5million
|          |             |     |         |             |        |            | regulatory | decision-making |       |      | purposes      |     | [10]. | Despite     |
| -------- | ----------- | --- | ------- | ----------- | ------ | ---------- | ---------- | --------------- | ----- | ---- | ------------- | --- | ----- | ----------- |
| records  | and compare |     | against |             | Random | Forest,    |            |                 |       |      |               |     |       |             |
|          |             |     |         |             |        |            | this, they | are             | still | type | of supervised |     |       | classifiers |
| Gradient | Boosting,   |     | and     | Transformer |        | baselines, |            |                 |       |      |               |     |       |             |
whichneedretrainingtoadjustdecisionboundaries.
reportingclassificationaccuracyof97.4percent,
|       |            |     |      |         |          |     | Bayesian    | neural | models          |     | enhance | the   | capability | of      |
| ----- | ---------- | --- | ---- | ------- | -------- | --- | ----------- | ------ | --------------- | --- | ------- | ----- | ---------- | ------- |
| trend | adaptation |     | rate | of 98.8 | percent, | and |             |        |                 |     |         |       |            |         |
|       |            |     |      |         |          |     | being aware |        | of uncertainty, |     |         | which | may        | help to |
cumulativelong-termperformanceindexof96.1
|     |     |     |     |     |     |     | better determine |     | appropriate |     |     | decision | thresholds |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----------- | --- | --- | -------- | ---------- | --- |
percentintheexperimentalsetting.
|               |     |            |     |              |     |             | and calibrated |     | output         | [11].     | However, |         | uncertainty    |     |
| ------------- | --- | ---------- | --- | ------------ | --- | ----------- | -------------- | --- | -------------- | --------- | -------- | ------- | -------------- | --- |
|               |     |            |     |              |     |             | modelling      | is  | not sufficient |           | to       | give    | an operational |     |
| The remainder | of  | this paper |     | is organized |     | as follows. |                |     |                |           |          |         |                |     |
|               |     |            |     |              |     |             | mechanism      | to  | help           | a running |          | service | continuously   |     |
The related work is discussed in Section 2. The improveand/orupdateitspoliciesinasafeway. These
proposed ARL-CPO method and system design is modelswhendeployedasastatelesspredictionservice
presented in Section 3. Experimental result and areoftentreatedasaheavyweightpipelinethatneeds
discussion are presented in Section 4, followed by tobemanagedforrefreshingthemodels. Disciplined
conclusionsandfuturedirections. testingandreleasecontrolsareneededforproduction
readiness,notjustofflinetesting,includingstructured
evaluationchecklistsandrubricsforreadiness[23].
2 LiteratureReview 2.2 Deep Learning Architectures for Credit
The shift from static, batch-trained predictors to Assessment
services that continuously serve customers requires Thecomplexityoffinancialdataishigh-dimensional
unprecedented software standards such as low and cannot be adequately represented using
latency inference, high throughput, fault tolerant, traditionalapproaches,whiledeeplearningreduces
auditable, and model-safe updates to models in the complexity of the representation learning, but
production[24]. Previousresearchincludesmodeling introduces a higher degree of complexity in serving
forcreditandfraud,sequentialdecisionoptimization and operation. For online credit scoring, transfer
withreinforcementlearning,andarchitecturesforthe learningframeworkswithextremelearningmachines
system-level deployment and streaming. Another enable continuous model adaptation for automated
issueisthatmanyhigh-accuracymodelsarenotbuilt credit assessment without full retraining [12]. In
tobeusedasaproductionservicewithawell-designed reality,itisstillmostlyusedasanadd-ontoamodel
workflow for updates, and built-in monitoring of thatneedsacontrolledretrainingandreleaseprocess.
operationalsystems,whichcauses“hiddentechnical A graph neural network for relational credit risk
debt”inthedeployedMLsystems[22]. models identifies the network effects that are not
158

ICCKJournalofSoftwareEngineering
Table1.Comparativeanalysisofexistingapproaches.
|     |     |     |     |     |     |     |     | Continuous | Sequential | Continuous | Long-Term |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | ---------- | --------- | --- | --- | --- |
Ref./Technique Application Adaptation Optimization Actions Reward Personalization
|                            | GradientBoosting[8]       |     |     | CreditDefaultEarlyWarning |                        |     |     | ×   | ×   |     | ×   | ×   | ×        |     |
| -------------------------- | ------------------------- | --- | --- | ------------------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- |
| ML-basedNetworkAnalysis[9] |                           |     |     | SystemicRiskPropagation   |                        |     |     | ×   | ×   |     | ×   | ×   | ×        |     |
|                            | XAIRandomForest[10]       |     |     |                           | CreditRiskTransparency |     |     | ×   | ×   |     | ×   | ×   | Partial  |     |
|                            | BayesianNeuralNetwork[11] |     |     |                           | Uncertainty-AwareRisk  |     |     |     |     |     |     |     | (cid:88) |     |
|                            |                           |     |     |                           |                        |     |     | ×   | ×   |     | ×   | ×   |          |     |
TransferLearning/ELM[12] OnlineCreditScoringAdaptation (cid:88)
|     |                        |     |     |                            |                      |     |     | ×       | ×   |     | ×   | ×   |          |     |
| --- | ---------------------- | --- | --- | -------------------------- | -------------------- | --- | --- | ------- | --- | --- | --- | --- | -------- | --- |
|     | GraphNeuralNetwork[13] |     |     |                            | RelationalCreditRisk |     |     | ×       | ×   |     | ×   | ×   | (cid:88) |     |
|     | ExplainableAI[14]      |     |     | InterpretableRiskDetection |                      |     |     | Partial | ×   |     | ×   | ×   | ×        |     |
DQN[15] PairsTrading/DiscreteActionControl (cid:88) (cid:88) × (cid:88) ×
PPO[16] AutomatedMarket-Making (cid:88) (cid:88) (cid:88) (cid:88) ×
TransferRL[17] Cross-MarketStrategyAdaptation (cid:88) (cid:88) (cid:88) (cid:88) Partial
BayesianRL[18] Uncertainty-AwarePolicyLearning (cid:88) (cid:88)
|     |                           |     |     |     |                        |     |     | ×       |     |     | ×   | ×   |     |     |
| --- | ------------------------- | --- | --- | --- | ---------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
|     | ConceptDriftDetection[19] |     |     |     | FinancialStreamingData |     |     | Partial |     |     |     |     |     |     |
|     |                           |     |     |     |                        |     |     |         | ×   |     | ×   | ×   | ×   |     |
MLOpsFramework[20] ProductionMLDeployment&Monitoring (cid:88) × × × ×
ARL-CPO(Proposed) AdaptiveFinTechRiskEvaluation (cid:88) (cid:88) (cid:88) (cid:88) (cid:88)
captured by tabular models [13]. But they could onlinelearningfromonlineinference,thegovernance
also add an inference latency and an infrastructure ofpolicyupdates,andtheauditabilityofdecisionsin
overhead because of the construction of the graph regulated contexts. Important operational guidance
and neighborhood aggregation. Explainable AI for the production of ML systems is to have explicit
methods in FinTech risk management provide controlsfortesting,rollout,monitoring,androllback
interpretable anomaly and risk signals that must to prevent unwanted changes in behavior of the
be integrated into downstream decision logic [14]. deployedsystems.
However,itoftenyieldsscoresthatmustbehandled
by the downstream system logic, routed to decision 2.4 Real-TimeAdaptiveFrameworksforFinTech
| thresholds |     | and  | reviewed     | by  | humans,   | introducing |     |                              |                |     |                     |     |       |     |
| ---------- | --- | ---- | ------------ | --- | --------- | ----------- | --- | ---------------------------- | -------------- | --- | ------------------- | --- | ----- | --- |
|            |     |      |              |     |           |             |     | Streaming                    | and deployment |     | frameworks          |     | solve | key |
| complexity |     | into | the software |     | pipeline. | Research    |     | in                           |                |     |                     |     |       |     |
|            |     |      |              |     |           |             |     | challengesintheFinTechspace. |                |     | Infinancialstreams, |     |       |     |
software engineering has highlighted the need to theconceptdriftdetectionsystemkeepstrackofthe
makeclearengineeringchoicesaboutdatapipelines, distributionshiftsandselectivelyupdatesmodels[19].
featurestores,reproducibly,andmonitoringtoprevent
Drift-awaremechanismsprovidetemporalrobustness
fragilityasrequirementsevolvewhenbuildinganML
|     |     |     |     |     |     |     |     | but tend | to be "reactive" |     | in that | they | may | have |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------- | ---- | --- | ---- |
basedsystem[25]. periods of poor performance as they retrain and
|     |               |     |          |     |              |     |     | redeploy.  | Standardized  |         | market        | environments |            | and |
| --- | ------------- | --- | -------- | --- | ------------ | --- | --- | ---------- | ------------- | ------- | ------------- | ------------ | ---------- | --- |
|     |               |     |          |     |              |     |     | benchmarks | for financial |         | reinforcement |              | learning,  |     |
| 2.3 | Reinforcement |     | Learning |     | Applications |     | in  |            |               |         |               |              |            |     |
|     |               |     |          |     |              |     |     | such as    | FinRL-Meta,   | provide | reusable      |              | simulation |     |
FinancialSystems
|     |     |     |     |     |     |     |     | infrastructure | that | supports | scalable | evaluation |     | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | -------- | -------- | ---------- | --- | --- |
Reinforcementlearningisabletosolveforsequential
|          |     |        |     |              |     |        |       | adaptive | risk policies | [21]. | They, | however, | do  | not |
| -------- | --- | ------ | --- | ------------ | --- | ------ | ----- | -------- | ------------- | ----- | ----- | -------- | --- | --- |
| decision |     | making | and | long-horizon |     | goals, | which |          |               |       |       |          |     |     |
necessarilyincludesequentialdecisionoptimization
| are       | not | addressed | by            | a prediction-only |              |     | model. |               |        |              |     |        |         |     |
| --------- | --- | --------- | ------------- | ----------------- | ------------ | --- | ------ | ------------- | ------ | ------------ | --- | ------ | ------- | --- |
|           |     |           |               |                   |              |     |        | or continuous | policy | improvement. |     | Recent | studies |     |
| DQN-based |     |           | pairs trading |                   | demonstrates |     | policy |               |        |              |     |        |         |     |
aboutMLOpsalsohighlighttheneedforproduction
| learning |     | through | interaction | with | simulated |     | market |     |     |     |     |     |     |     |
| -------- | --- | ------- | ----------- | ---- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
MLsystemstobemonitored,reproducible,andtohave
environments,thoughitsdiscreteactionformulation
|                                          |     |     |     |     |     |     |          | controlled | release mechanisms |     | to  | avoid | building | up  |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------------------ | --- | --- | ----- | -------- | --- |
| limitsfine-grainedcontinuouscontrol[15]. |     |     |     |     |     |     | Itmaynot |            |                    |     |     |       |          |     |
technicaldebtandreliabilityissues[22].
offerasmuchfine-grainedcontrolascontinuousaction,
duetoitsdiscreteactionformulation. Inthefinancial Table1showsthatanumberofsupervisedtechniques
domain,PPO-basedmarket-makingshowsexcellent have been developed and proved to have good
results for continuous control, and encourages predictive accuracy, however, they generally do
actor-critic style policy optimization [16]. The not continuously adapt and need offline refresh
relevanceofthisisforcross-marketadaptationthatis cycles [8]. Deep models have the ability to learn
usefultoFinTechservicesoperatingacrossregionsand good representations but can be expensive to
marketregimes[17]. Bayesianreinforcementlearning serve and update reliably at scale [13]. When
provides principled uncertainty quantification over appliedtoalways-onFinTechservices,reinforcement
policies, which can improve objective clarity and learningprovidestheabilitytosequentiallyoptimize
support risk-aware decision making [18]. But much and long-horizon objectives, but the question of
workinRLremainspoorly-definedintheisolationof operationalization is often underspecified [16].
159

ICCKJournalofSoftwareEngineering
Figure1.TheARL-CPOPipelineforAdaptiveRiskEvaluationinFinTechSystems.
Streaming and microservice frameworks enhance the dual-network (policy-value) structure enables
deployability and service reliability, but they don’t the agent to converge stably (taking account the
bringonlinedecisionoptimizationtogetherwithsafe market regime changes). ARL-CPO provides better
continuous update workflows [20]. This situation adaptiveness, granularity androbustness in FinTech
encouragesamethodtosolveadaptiveriskevaluation, riskmanagementsoftware,comparedtobothlegacy
whichnotonlyviewsitasalearningproblembutalso static pipelines and discrete-action reinforcement
asanengineeredsystemwithqualitymonitoringtools learningbaselines.
andupdatecontrolmechanisms.
Fromasoftwareengineeringperspective,thetargeted
problemisnotonlypredictiveperformance,butalso
3 ProposedMethod
the design of a risk evaluation service that can (i)
The current FinTech software-based platforms are ingest streaming transactional and behavioral data
evolving at an unprecedented pace with multiple at high throughput, (ii) return a calibrated risk
vectorsofriskthatneedtobeconstantlyandadaptively score with bounded inference latency suitable for
evaluated instruments. The poor scalability of both real-timeuserjourneys,(iii)supportcontinuouspolicy
the static coding models and deterministic rule updates without downtime, and (iv) provide fault
engines have had challenges in non-stationary data toleranceandobservabilityforproductionmonitoring
distribution, high dimensional continuous feature and regulatory audits. In this work, ARL-CPO
space and subtle behavioral patterns of digital is positioned as a deployment-oriented learning
financialusers. Toalleviatethesedisadvantages,this component that can be integrated into a modular
paperproposestheAdaptiveReinforcementLearning FinTechriskpipeline,whereonlinelearningisisolated
with Continuous Policy Optimization (ARL-CPO) from the inference path to prevent update-induced
framework, a learning-based framework, that aims service instability, while decision logs and model
to reshape the risk evaluation as a Continuous versions are preserved for compliance and post-hoc
Markov Decision Process (MDP) with Continuous investigation.
Action Space and Continuous State Space. The
ARL-CPOagentlearnsthebestrisk-mitigationpolicies The provided architecture is a closed-loop pipeline
withouttheneedtohavehand-writtenrules. Reward of adaptive risk assessment of the FinTech software
formulation in the agent is loss sensitive, while systems. The financial data simulation layer is fed
160

ICCKJournalofSoftwareEngineering
streamingmarketindicatorsandcustomerbehavioral recordedwithamodelversionidentifier,atimestamp
telemetrythatreflectreal-timeoperatingconditions. and request info to enable traceability, auditability,
Thestateencoderthentransformstherawinputsinto operational debugging. This allows for proposed
asmallobservationvectorwhichisthenprocessedby learningcomponenttobeinsertedintocurrentFinTech
the ARL-CPO Decision Engine comprising a policy softwaresystemswithoutbusinessdecisionlogicbeing
network and a value approximation network. The integratedintolearningloop.
enginecreatescontinuousriskscoresthatcanbeused
to make decisions regarding the eligibility of credit
and the actions necessary to rebalance the portfolio. Γ(t−1) = F(o,θ)−H(ξ) subjectto V > L(t−g)
Theflowoftherewardsignaliscalculatedbasedon (1)
theattainedmonetaryresultsandthisisflowedback
All symbols in Eq. (1) are defined as follows.
tocorrectthepolicyoftheagentinaniterativemanner.
Γ(t − 1) is the performance signal at time step (t −
This closed loop design guarantees personalization,
1), the current observation (state representation)
flexibility and state of the art accuracy in volatile
is o, and the current set of policy parameters is
financialecosystems,whichisillustratedinFigure1.
θ. The observation and policy parameters are
The MDP formulation is selected to align with
denoted as provided by the function F(o,θ), which
is an uncertainty-related scoring function, like a
deployed FinTech risk services where decisions
confidence-aware scoring function, or an entropy
are repeated over time and outcomes (defaults,
chargebacks, losses, missed opportunities) arrive proxy. ξ denotes a vector of threat indicators or
with delay. Continuous actions are necessary drift-sensitivesignalsextractedfromthestream. H(ξ)
represents the uncertainty/entropy of the threat
becauseproductionrisksystemscommonlyrequirea
real-valuedscorethatcanbecalibrated,thresholded, indications. V is a form of confidence (such as a
validityscorefromacalibrationlayerorcriticestimate).
and composed with downstream rules, rather than
The lower bound on acceptable confidence is called
a coarse discrete label. In ARL-CPO, the action
is therefore treated as a continuous score in a
L(t−g)andg isalagparameterthatdeterminesthe
bounded interval (e.g., [0,1]) which can be mapped window of assessment. The constraint V > L(t −
tooperationallabels(Low/Moderate/Elevated)only g) ensures that risk actions are only accepted if the
minimumconfidencerequirementisfulfilled,relevant
atthebusiness-rulelayer. Thisseparationpreservesa
forsafedeploymentunderdistributionalshift.
stableAPIcontract(continuousscoreoutput)while
allowingproductteamstoadjustthresholdswithout
retrainingthepolicy.
(cid:0) (cid:1)
Ψ = {q }(u,ξ) := λ(ξ−d)+Ω(λ −C {t−1})
r−1 k r
Algorithm1evaluatestheinstantaneousriskpostureof ·Ω {d−1}
u
afinancialentityormarketconditionusingthetrained (2)
ARL-CPOagent. Theprocessstartswiththemarket
Eq. (2)isaplaindefinitionofanadjustedperformance
feature vectors and user activity metrics combined
tensor for adaptation control, u is a normalized
to one observation o t . This observation is mapped adaptation index (such as an intensity factor for
to a scalar action a t = the estimated risk magnitude updates), ξ represents drift or threat indicators, λ
bythepolicynetwork(continuousactiongenerator)
is a scaling factor for sensitivity to drift, d is a
whichmapsthisobservationtoascalaractiona. The
referencedriftbaseline(ordetectionthreshold),and
algorithm uses a value from 0 to 2 to represent a t , Ω is a temporal normalization operator. λ is a
k
with0beingMinimal,1beingModerate,and2being
reference performance level (or metric). Ω {d −
u
Elevated. Asthescoringmechanismisupdatedineach
1} is a normalization term that adjusts updates
observation, the scoring mechanism automatically
based on the evaluation window. C {t − 1} is the
r
adapts to behavioral drift, thus enabling individual
observedperformanceorcorrectiontermattime(t−
creditadjudicationandassetallocationsoptimization.
1). Operationally, Eq. (2) is used to modulate how
strongly the agent corrects internal estimates when
In a real deployment, Algorithm 1 can be the
behavioralpatternsshift,whichsupportsstableonline
inference path of a risk scoring microservice. The
operation.
service is exposed and should take the encoded
observation (or state) in as an argument and return Figure 2 depicts the ARL-CPO architecture that
the continuous score right away. Every answer is consists of two collaborating modules: a Policy
161

ICCKJournalofSoftwareEngineering
Figure2.ARL-CPODual-ModuleArchitecturewithGradient-BasedPolicyRefinement.
Learning Module and a Value Estimation Module. The Algorithm 2 will be used to guide the iterative
The observation vector o is received by the Policy processofrefiningthepolicyoftheARL-CPOagent
t
Learning Module which generates a continuous using outcome-driven feedback. Once an agent
risk-control action using the policy network and performs an action and sees the change in the
injects controlled perturbation to explore. The environment, a scalar reward is calculated. This
Value Estimation Module stores transition tuples in rewardiscomparedwithaperformancebaselinebythe
a memory bank, approximates expected cumulative algorithm. Whentherewardisatorbelowthebase,the
reward via the value approximation network and existingpolicyparametersaremaintainedwithsome
stabilizestrainingusingatargetsynchronizationunit. stabilizationupdatestoavoidoverfitting. Otherwise,
Thepolicyrefinementprocessviagradientsisaflow theweightsofthepolicynetworkarecorrectedwith
directed by the value module to the policy network, thehelpofgradient-basedcorrectionsinsuchaway
making it possible to continuously improve the thatsuboptimaldecisionsarepenalized. Theresulting
policy. Thismodularseparationisstable-convergent feedbackloopallowstheARL-CPOagenttoobserve
andisespeciallyapplicabletothehigh-dimensional, non-stationary financial dynamics and aid resilient
continuous-controlrequirementsofreal-timefinancial andinformedriskgovernance.
riskmanagement.
|           |             |                |     |          |            | For      | reproducibility |            |     | and deployment |          | realism, | the         |
| --------- | ----------- | -------------- | --- | -------- | ---------- | -------- | --------------- | ---------- | --- | -------------- | -------- | -------- | ----------- |
|           |             |                |     |          |            | reward   | signal          | should     |     | be implemented |          | as       | an explicit |
| While the | dual-module | (policy-value) |     |          | separation |          |                 |            |     |                |          |          |             |
|           |             |                |     |          |            | function | of              | observable |     | business       | outcomes |          | and risk    |
| resembles | the general | actor-critic   |     | concept, |            | the      |                 |            |     |                |          |          |             |
objectives,suchasrealizedloss,default/fraudevents,
software-levelcontributioninARL-CPOistheupdate
|     |     |     |     |     |     | and | risk-adjusted |     | return | measures |     | computed | over a |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | -------- | --- | -------- | ------ |
andsynchronizationpatternforcontinuousoperation.
|     |     |     |     |     |     | defined | horizon. |     | In  | a production |     | system, | reward |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --- | ------------ | --- | ------- | ------ |
Theinferenceserviceusesafixed,versionedsnapshot
|        |                       |     |             |     |          | computation |     | is  | typically | delayed |     | and | arrives via |
| ------ | --------------------- | --- | ----------- | --- | -------- | ----------- | --- | --- | --------- | ------- | --- | --- | ----------- |
| of the | policy for consistent |     | low-latency |     | scoring, |             |     |     |           |         |     |     |             |
asynchronousoutcomeevents;therefore,thesystem
| while the                          | learning | module | updates |             | parameters |        |               |         |        |          |              |     |          |
| ---------------------------------- | -------- | ------ | ------- | ----------- | ---------- | ------ | ------------- | ------- | ------ | -------- | ------------ | --- | -------- |
|                                    |          |        |         |             |            | logs   | (observation, |         | score, | decision | context,     |     | outcome) |
| asynchronouslyonstreamingfeedback. |          |        |         | Thepolicies |            |        |               |         |        |          |              |     |          |
|                                    |          |        |         |             |            | tuples | to            | compute |        | rewards  | consistently |     | and to   |
areupdatedviaacontrolledrolloutprocess,suchasa
|     |     |     |     |     |     | enable | audit | trails. | This | also | supports |     | compliance |
| --- | --- | --- | --- | --- | --- | ------ | ----- | ------- | ---- | ---- | -------- | --- | ---------- |
shadowevaluation,canaryrelease,orstagedrollout,
|                                            |     |     |     |     |     | requirements |     | by         | retaining |       | evidence | of      | how each |
| ------------------------------------------ | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --------- | ----- | -------- | ------- | -------- |
| toensurethattherearenounsafepolicychanges. |     |     |     |     |     | This         |     |            |           |       |          |         |          |
|                                            |     |     |     |     |     | decision     | was | generated, |           | which | model    | version | was      |
designalsoensuresthatthereisno“training-induced
|            |               |     |         |             |     | used, | and | what | outcome | feedback |     | triggered | future |
| ---------- | ------------- | --- | ------- | ----------- | --- | ----- | --- | ---- | ------- | -------- | --- | --------- | ------ |
| downtime,” | and it allows |     | for the | possibility |     | of    |     |      |         |          |     |           |        |
policyupdates.
| reverting | back to a previous   |     | stable | version     | of  | the |     |     |     |     |     |     |     |
| --------- | -------------------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model,    | while also providing |     | the    | opportunity |     | to  |     |     |     |     |     |     |     |
)foru
|                                                 |     |     |     |     |     | tV  | ≡ Λ ∗(Φ |       | ) → (t−1) | ≤   | Jλ|c−(β−η |     | ≡ ∇ |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ----- | --------- | --- | --------- | --- | --- |
| continuouslyimprovepolicieswithoutdisruptingthe |     |     |     |     |     |     | 1       | {t−1} |           |     |           | r   |     |
(3)
| serving    | path, a requirement |     | for production |     | FinTech |     |                          |     |     |     |                    |     |     |
| ---------- | ------------------- | --- | -------------- | --- | ------- | --- | ------------------------ | --- | --- | --- | ------------------ | --- | --- |
| platforms. |                     |     |                |     |         | Eq. | (3)isclarifiedasfollows. |     |     |     | denotesanaggregate |     |     |
tV
162

ICCKJournalofSoftwareEngineering
qualityindexattimet. Λ denotesascalingconstant modelregistry,rollout/rollback),ratherthanonlythe
1
for quality aggregation. The feature vector at the learningflow.
previous step is denoted as Φ (e.g., reward
{t−1} Figure 3 illustrates how the ARL-CPO decision
statisticsfrompreviousstepsorstabilityindicators).
engine can be embedded into a production-grade
The baseline time index (t − 1) is used to compare
FinTech risk evaluation pipeline as an always-on
itscurrentperformancewithrecenthistory. Jλ|cisa
software service. The client applications use the
compositeobjectivetermcomposedofariskpenalty
API Gateway to make calls to the risk scoring
adjustment, η , a base performance measure, β, and
r capability, which then forwards to the Risk Scoring
aconstrainttolimittheupdates,c. Foroperation,Eq.
Service(inferencemicroservice)thatloadsaversioned
(3)isappliedtomonitorthetrade-offbetweenservice
stabilityandproactiveriskgovernanceindrift.
policysnapshotπθ(v
k
)andreturnsacontinuousrisk
score that has a short latency. At the same time,
external market indicators and transaction or user
signals are continuously ingested into the system
(cid:107)Λ(u,ω )(cid:107) = D (χ−λ )+G (τ,ρ ) := δ(u−ρ ) ≥ ∇ via streaming. Meanwhile, market indicators and
r ξ b ω k w
(4) transactionorusersignalsarecontinuouslyingested
from the outside world and transformed by the
Eq. (4)isclarifiedasfollows,thenorm(cid:107)Λ(u,ω )(cid:107)isa
r Feature/State Builder into the state representation
measureoftheadaptationperformanceofthesystem
(s /o ) that is utilized for inference and learning.
withupdateintensityuandarisk-weightparameterω . t t
r Manydownstreamplatformservices(defaults,fraud
ThedriftsensitivetermD (χ−λ )isaterminvolving
ξ b confirmations,realizedloss/return)triggeroutcome
observed behavioral shift statistics, λ is a baseline
b events, which are fed to the Outcome and Reward
drifttolerance,andξ isthedriftindicatorspace. The
Service to calculate r , and to create training tuples
stabilitytermisdenotedasG (τ,ρ ),withτ beingan t
ω k (s ,a ,r ,s {t + 1}). These tuples then go into
update/synchronizationrateandρ beingaparameter t t t t
k an Online Learning Service that updates the actor
of performance boundary. An update intensity u is
and critic, asynchronously, and stores the updated
compared with a control boundary, ρ , denoted as
w policies in a Model Registry. A controlled canary or
δ(u − ρ ). The ≥ ∇ condition represents satisfying
w shadowrolloutloophelpsensuresafe,downtime-free
allconfigthresholds. Indeployment,thesequantities
updatesthroughpromotingnewmodelversionsafter
correspondtomonitoringsignalsandguardrails(for
validation, and the Audit/Compliance storage and
example,update-ratecapsanddriftthresholds)that
Monitoring/Observabilityprovidelogs,metrics,traces,
preventunstablebehaviorunderhighloadorsudden
driftsignalsandalertstomeetoperationalreliability
marketregimechanges.
and regulatory traceability requirements. The
The ARL-CPO model is based on the concept of proposedmethodologyisbasedoncontinuous-action
reward-based continuous policy optimization to reinforcementlearningandusesadeployment-aware
reduce financial risks in real-time. The architecture softwarearchitectureasameanstoseparateinference
demonstrateshowtheadaptivereinforcementlearning fromtraining,tohandleversioneddeploymentandto
canbeappliedtosupportFinTechsoftwaresystemsin providemonitoringandcompliancelogging. Thatis
offeringflexiblecreditdecisionsanddynamicportfolio themethodologyforARL-CPOasanadaptivelearning
management. This continuous-action control that framework as well as a practical component of the
is enabled by the dual policy-value structure and FinTechsoftwaresystem.
thegradient-basedrefinementisespeciallyusefulin
complexfinancialsituations,wherefine-grainedrisk
4 ResultsandDiscussions
adjustmentsareneeded.
This section entails the experimental analysis of the
To make the proposed framework software offered ARL-CPO framework implemented to the
engineering more explained, an explicit integration adaptiveriskassessmentinFinTechsoftwaresystems.
diagram is shown in Figure 3 that explains how It contrasts its framework to three frameworks that
ARL-CPO connects to platform components such are already in use: Random Forest (RF), Gradient
as API gateways, message queues, databases, and Boosting(GB),andTransformer-basedmodels(TFM)
monitoring tools. This diagram complements for credit default prediction and dynamic asset
Figures1and2byfocusingondeployability,system allocation problems. The evaluation validates that
boundaries,andoperationalcontrolpoints(logging, continuous optimization policy is more accurate,
163

ICCKJournalofSoftwareEngineering
Figure3.ARL-CPOIntegrationintoaProductionFinTechRiskSystem.
reactive and stable over time than other policy Table2.Experimentalconfiguration.
optimization policies with single or batch trained Parameter Description/Value
policies. Environment / FinTechadaptiveriskscoringusingstreaming
|                                         |     |     |     |     |     |     |     |     | Task        | marketandtransactionaldata                    |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------------------------------------------- | --- | --- | --- |
|                                         |     |     |     |     |     |     |     |     | StateSpace  | Marketindicators,behavioralrisksignals,credit |     |     |     |
| 4.1 DatasetandExperimentalConfiguration |     |     |     |     |     |     |     |     |             | utilizationmetrics                            |     |     |     |
|                                         |     |     |     |     |     |     |     |     | ActionSpace | Continuousriskscoreadjustment∈[0,2]           |     |     |     |
Theseexperimentsmakeuseofalarge-scalefinancial
|     |     |     |     |     |     |     |     |     | Policy Network | 3 hidden layers | with 512, | 384, and | 256 units, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------------- | --------- | -------- | ---------- |
datasetof8.5millionrecordsthathavebeengenerated Architecture LeakyReLUactivations
using advanced generative modeling methods, and Value Network 3 hidden layers with 512, 384, and 256 units,
|          |                |     |           |           |     |                |     |     | Architecture  | LeakyReLUactivations |     |     |     |
| -------- | -------------- | --- | --------- | --------- | --- | -------------- | --- | --- | ------------- | -------------------- | --- | --- | --- |
| which    | are regulatory |     | compliant |           | and | distributional |     |     |               |                      |     |     |     |
|          |                |     |           |           |     |                |     |     | Learning Rate | 0.0005               |     |     |     |
| faithful | to real-world  |     |           | financial |     | patterns.      |     | The |               |                      |     |     |     |
(Policy)
data includes the customer demographics profiles, Learning Rate 0.0008
| multi-channeltransactionshistory,creditapplication |             |     |           |     |         |     |              |     | (Value)         |      |     |     |     |
| -------------------------------------------------- | ----------- | --- | --------- | --- | ------- | --- | ------------ | --- | --------------- | ---- | --- | --- | --- |
|                                                    |             |     |           |     |         |     |              |     | Discount Factor | 0.98 |     |     |     |
| record                                             | and account |     | lifecycle |     | events. | It  | is extensive |     |                 |      |     |     |     |
(γ)
andheterogeneousand,therefore,ishighlytailoredto Transition 1,500,000tuples
theevaluationofadaptivelearningsystems,financial MemoryCapacity
|             |          |     |        |            |     |              |     |     | Mini-batchSize   | 128            |            |         |            |
| ----------- | -------- | --- | ------ | ---------- | --- | ------------ | --- | --- | ---------------- | -------------- | ---------- | ------- | ---------- |
| forecasting | modules, |     | and    | behavioral |     | segmentation |     |     |                  |                |            |         |            |
|             |          |     |        |            |     |              |     |     | Exploration      | Gaussian noise | injection, | σ=0.18, | decay rate |
| pipelines.  | Table    |     | 2 will | give       | a   | summary      | of  | the | Strategy         | 0.995          |            |         |            |
|             |          |     |        |            |     |              |     |     | TrainingEpisodes | 350episodes    |            |         |            |
experimentaldesign.
|     |     |     |     |     |     |     |     |     | Max Steps per | 250steps |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | --- | --- | --- |
Episode
4.2 PredictionAccuracyAnalysis RewardFunction Negative expected shortfall combined with
risk-adjustedreturn
| The precision  |         | of prediction |         | of            | all the    | four         | methods   |     |                |                                  |        |        |        |
| -------------- | ------- | ------------- | ------- | ------------- | ---------- | ------------ | --------- | --- | -------------- | -------------------------------- | ------ | ------ | ------ |
|                |         |               |         |               |            |              |           |     | Target Network | Softupdateparameterτ=0.003       |        |        |        |
| at progressive |         | levels        |         | of evaluation |            |              | are shown |     | SyncRate       |                                  |        |        |        |
|                |         |               |         |               |            |              |           |     | Hardware       | AMDEPYC7742CPU;NVIDIAA10080GBGPU |        |        |        |
| in Figure      | 4.      | The           | maximum |               | prediction |              | accuracy  |     |                |                                  |        |        |        |
|                |         |               |         |               |            |              |           |     | Software       | PyTorch framework,               | Ubuntu | 22.04; | custom |
| of the         | ARL-CPO |               | system, | based         |            | on precision |           | is  |                |                                  |        |        |        |
FinTechenvironmentsimulator
| 97.4%        | that is        | much     | higher |                | than            | all the | baselines. |       |     |     |     |     |     |
| ------------ | -------------- | -------- | ------ | -------------- | --------------- | ------- | ---------- | ----- | --- | --- | --- | --- | --- |
| This primacy |                | is based |        | on the         | ability         | of      | the        | agent |     |     |     |     |     |
| to keep      | evolving       |          | its    | internal       | representations |         |            | in    |     |     |     |     |     |
| response     | to interaction |          | with   | non-stationary |                 |         | streams    |       |     |     |     |     |     |
of financial data. The ARL-CPO agent also takes plateaus over time, whereas ARL-CPO continues
advantageofeachpredictionasanelementinalong improving through its reward-based adaptation
sequence of decisions, gradually learning complex mechanism. The continuous action formulation
nonlinear relationships between user behavior and also allows fine-grained, context-sensitive risk
market dynamics. The Transformer baseline shows quantification as opposed to coarse categorical
competitive performance at shorter intervals but assignments.
164

ICCKJournalofSoftwareEngineering
|     |     |     |     |     | percent | cumulative |     | performance |     | index | is evidence |     |
| --- | --- | --- | --- | --- | ------- | ---------- | --- | ----------- | --- | ----- | ----------- | --- |
thatthealgorithmiscapableofoptimizingsustained
|     |     |     |     |     | performance |      | as opposed |      | to         | greedy | short-horizon |      |
| --- | --- | --- | --- | --- | ----------- | ---- | ---------- | ---- | ---------- | ------ | ------------- | ---- |
|     |     |     |     |     | returns.    | When | the        | risk | assessment | is     | defined       | as a |
sequenceofoptimizationproblemsinwhichthefuture
|     |     |     |     |     | rewardisdiscounted(γ |     |           |     | =0.98)andthefutureriskis |           |     |       |
| --- | --- | --- | --- | --- | -------------------- | --- | --------- | --- | ------------------------ | --------- | --- | ----- |
|     |     |     |     |     | considered           | to  | determine |     | the best                 | strategy, | the | agent |
learnsstrategiesthattradetheimmediatereductionof
|     |     |     |     |     | riskwiththelong-termhealthoftheportfolio. |     |     |     |     |     |     | Thisis |
| --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | ------ |
echoedinthereducedlevelsofdefaultincreditrating
andmorepredictableriskadjustedreturnsintheasset
Figure4.ComparisonofAccuracyofPredictionacross
|     |     |     |     |     | allocation. | Theareaundercurvecomparisonclearly |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
EvaluationIntervals.
|     |     |     |     |     | shows       | that ARL-CPO |             |     | is continuing | to   | increase  | the |
| --- | --- | --- | --- | --- | ----------- | ------------ | ----------- | --- | ------------- | ---- | --------- | --- |
|     |     |     |     |     | gap between |              | performance |     | compared      | with | baselines |     |
4.3 TrendAdaptationRateAnalysis as training continues: RF plateaus at 55.4%, GB
The rate of trend adaptation that was plotted in levels off at 63.2% and TFM levels off at 74.8%. It
Figure5,quantifiestheresponsivenessofeachmethod is discovered that the policy refinement mechanism
to distributional changes in financial behavior and has compounding advantages with longer training
marketregimes. TheadaptationrateofARL-CPOis horizons,whichisafeatureneededinFinTechsystems
98.8% which confirms that it is the most responsive wherelong-termriskgovernancedefinestheviability
amongallbaselines. Conventionalalgorithmshavea oftheplatform.
| highlatencyindetectingnewpatterns:          |        |              | RFconverges |       |     |     |     |     |     |     |     |     |
| ------------------------------------------- | ------ | ------------ | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| on about                                    | 48.1%, | GB converges | on about    | 58.6% | and |     |     |     |     |     |     |     |
| TFMconvergesonabout72.4%atthelastiteration. |        |              |             |       | The |     |     |     |     |     |     |     |
ARL-CPOagentupdatesitspolicyparametersateach
interactioncycle,andthusdoesnothavetheretraining
| bottleneckatall. |     | Thedual-modulearchitecturewith |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theseparationofpolicylearningandvalueestimation
| enables the | stable | and rapid | convergence | without |     |     |     |     |     |     |     |     |
| ----------- | ------ | --------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
catastrophicforgetting,andtheabilitytoaccommodate
| new distributional |     | information. | Such a | property | is  |     |     |     |     |     |     |     |
| ------------------ | --- | ------------ | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
absolutelyessentialonFinTechplatformswhereuser
behaviorandregulatoryenvironmentsmaychangeat
Figure6.CumulativeLong-TermPerformanceIndexover
anytime.
TrainingEpochs.
|     |     |     |     |     | Table 3      | summarizes       |               | the          | quantitative  |           | results       | of all   |
| --- | --- | --- | --- | --- | ------------ | ---------------- | ------------- | ------------ | ------------- | --------- | ------------- | -------- |
|     |     |     |     |     | the three    | evaluation       |               | dimensions.  |               | The       | ARL-CPO       |          |
|     |     |     |     |     | framework    |                  | outperforms   |              | the           | strongest |               | baseline |
|     |     |     |     |     | (TFM)        | by 18.9%,        |               | 26.4%,       | and           | 21.3%     | in prediction |          |
|     |     |     |     |     | accuracy,    | trend            |               | adaptation   |               | rate, and | long-term     |          |
|     |     |     |     |     | performance, |                  | respectively. |              |               | Such      | gains         | can be   |
|     |     |     |     |     | attributed   |                  | to three      |              | architectural |           | benefits      | (1)      |
|     |     |     |     |     | continuous   |                  | policy        | optimization |               | mechanism |               | that     |
|     |     |     |     |     | removes      | batch-retraining |               |              | latency       | (2)       | dual-module   |          |
Figure5.TrendAdaptationRateAcrossTestIterations. separation that allows stable convergence under
|     |     |     |     |     | distributional |     | shift | (3)  | reward-based |               | sequential |      |
| --- | --- | --- | --- | --- | -------------- | --- | ----- | ---- | ------------ | ------------- | ---------- | ---- |
|     |     |     |     |     | formulation    |     | that  | must | focus        | on cumulative |            | risk |
4.4 Long-TermCumulativePerformanceAnalysis reduction rather than myopic predictions. Overall,
Figure 6 illustrates the cumulative performance these findings support ARL-CPO as a resoundingly
index of all the methods after 300 training epochs. better solution to adaptive risk evaluation within
The fact that ARL-CPO is able to achieve 96.1 modernFinTechsoftwaresolutions.
165

ICCKJournalofSoftwareEngineering
Table3.ComparativeperformanceanalysisofARL-CPOagainstbaselinemethods.
|     |     |     |     |     |     | Prediction | TrendAdaptation |     |     |     | CumulativeLong-Term |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | --------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
Method
|     |                      |                  |     |     | Accuracy(%) |      |     | Rate(%) |      |     | Performance(%) |      |     |     |     |
| --- | -------------------- | ---------------- | --- | --- | ----------- | ---- | --- | ------- | ---- | --- | -------------- | ---- | --- | --- | --- |
|     | RandomForest(RF)     |                  |     |     |             | 62.3 |     |         | 48.1 |     |                | 55.4 |     |     |     |
|     | GradientBoosting(GB) |                  |     |     |             | 71.2 |     |         | 58.6 |     |                | 63.2 |     |     |     |
|     |                      | Transformer(TFM) |     |     |             | 78.5 |     |         | 72.4 |     |                | 74.8 |     |     |     |
|     | ARL-CPO(Proposed)    |                  |     |     |             | 97.4 |     |         | 98.8 |     |                | 96.1 |     |     |     |
Table4.Softwaresystemperformanceevaluation(deployment-orientedmetrics).
ARL-CPO
| Metric |     |     |     |     |     |     |     |     |     | RF  |     | GB  |     | TFM |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(Proposed)
Inferencelatency(ms/request),p50/p95 7.6/18.4 2.1/4.8 3.4/7.2 19.8/46.5
| Throughput(requests/second) |     |     |     |     |     |     | 5,200 |     | 18,500  |     |     | 12,400  |     | 1,950 |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | ------- | --- | ----- | --- |
| Peakmemoryusage(GB)         |     |     |     |     |     |     | 3.2   |     |         | 1.1 |     | 1.6     |     | 6.8   |     |
| CPUutilization(%)atpeakload |     |     |     |     |     |     | 42    |     |         | 68  |     | 71      |     | 38    |     |
| GPUutilization(%)atpeakload |     |     |     |     |     |     | 31    |     | Notused |     |     | Notused |     | 44    |     |
Modelupdatetime(sec/update) 2.7 Notapplicable Notapplicable 9.4
Table 4 reports the deployment-oriented software dual-modulegradient-basedrefinement,andreal-time
performancemetrics(inferencelatency,throughput, adaptivelearninginasinglearchitecturespecifically
resource utilization, and model update time), designed to govern financial risk. Simultaneously
demonstratingthatARL-CPOcansupportreal-time achieving 97.4% prediction accuracy, 98.8% trend
risk scoring while maintaining practical online adaptation rate, and 96.1% cumulative long-term
updateoverheadinaproduction-likeFinTechservice performance—outperformingthestrongestbaseline
environment. Each method was tested 10 times bymarginsover18percent—demonstratesthatrisk
independently with different random seed, and the assessmentformulatedasacontinuous-actionMarkov
results are presented as mean ± SD. Using the run Decision Process with loss-sensitive reward signals
distribution,95%confidenceintervalswerecomputed yields fundamentally superior decision intelligence
for all three primary metrics for Figures 4, 5 and thanprediction-onlyparadigms. Thecombinationof
6; statistical significance testing using the strongest granularcontinuousscoring,real-timeenvironmental
baseline (TFM) confirmed the improvements of control and long-horizon reward maximization in a
ARL-CPO are statistically significant (p < 0.01) for singleFinTechriskassessmentpipelinedoesnotexist
all three primary metrics. To prevent exploiting inpriorworkwithinthereviewedliterature.
onlineupdates,anextraonlinebaseline(incremental
fine-tuningoftheTransformeratfixedupdateperiods
5 Conclusion
| with a | sliding  | window) |            | was  | additionally |     | tested,  |           |         |             |     |             |         |            |       |
| ------ | -------- | ------- | ---------- | ---- | ------------ | --- | -------- | --------- | ------- | ----------- | --- | ----------- | ------- | ---------- | ----- |
|        |          |         |            |      |              |     |          | This      | article | proposes    |     | an adaptive | risk    | assessment |       |
| which  | was more |         | responsive | than | the          | TFM | offline, |           |         |             |     |             |         |            |       |
|        |          |         |            |      |              |     |          | framework |         | for FinTech |     | software    | systems |            | using |
butnotaswellasARL-CPOonbothadaptationand
reinforcement-basedcontinuouspolicyoptimization
| long-horizonperformance. |               |     |     | Thetrendadaptationrate |     |               |     |             |     |              |     |               |      |             |        |
| ------------------------ | ------------- | --- | --- | ---------------------- | --- | ------------- | --- | ----------- | --- | ------------ | --- | ------------- | ---- | ----------- | ------ |
|                          |               |     |     |                        |     |               |     | through     | the | ARL-CPO      |     | architecture. |      |             | Beyond |
| (98.8%)                  | is calculated |     | as  | the percentage         |     | of post-drift |     |             |     |              |     |               |      |             |        |
|                          |               |     |     |                        |     |               |     | algorithmic |     | performance, |     | the           | work | contributes | a      |
testiterationsinwhichthemethodisrecoveredwithin
|     |     |     |     |     |     |     |     | deployment-oriented |     |     | design | view | of  | adaptive | risk |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------ | ---- | --- | -------- | ---- |
apredeterminedrecoverytimewindow,towithin2%
scoringasanalways-onsoftwareservice,emphasizing
| ofthepre-driftlevel.  |        |          | Inadditiontopredictivemetrics, |                 |     |             |     |            |     |           |         |         |             |              |     |
| --------------------- | ------ | -------- | ------------------------------ | --------------- | --- | ----------- | --- | ---------- | --- | --------- | ------- | ------- | ----------- | ------------ | --- |
|                       |        |          |                                |                 |     |             |     | continuous |     | online    | updates | without |             | interrupting |     |
| a deployment-oriented |        |          |                                | evaluation      | was | performed   |     |            |     |           |         |         |             |              |     |
|                       |        |          |                                |                 |     |             |     | inference, |     | versioned |         | model   | management, |              | and |
| on the                | stated | hardware |                                | to characterize |     | operational |     |            |     |           |         |         |             |              |     |
operationalmonitoringforreliabilityandauditability.
feasibilityinreal-timeFinTechservices.
Unlikemodelsthataretrainedinbatches(likeRandom
The results of the experiment clearly prove the Forest, Gradient Boosting and Transformer-based
originalityandexcellenceoftheproposedARL-CPO models), ARL-CPO continually adapts its decision
frameworkincomparisonwiththecurrentonesinthe policy based on the changing financial behaviors,
sphereofFinTechriskassessment. ARL-CPOisthefirst market regimes and user activity patterns. The
framework to unify continuous policy optimization, empiricaltestingofthecreditdefaultpredictionand
166

ICCKJournalofSoftwareEngineering
| the asset | allocation |     | with | trend adaptation |     | tasks | in  |     |     |     |     |     |     |
| --------- | ---------- | --- | ---- | ---------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
AIUseStatement
| a large-scale |     | synthetic | FinTech | environment |     |     | yields |     |     |     |     |     |     |
| ------------- | --- | --------- | ------- | ----------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
TheauthordeclaresthatnogenerativeAIwasusedin
| a predictive |     | accuracy | of 97.4%, | trend | adaptation |     | of  |     |     |     |     |     |     |
| ------------ | --- | -------- | --------- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
thepreparationofthismanuscript.
98.8%,andcumulativelong-termperformanceindex
| of 96.1%. | Moreover, |     | it provides |     | inference | latency, |     |     |     |     |     |     |     |
| --------- | --------- | --- | ----------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
throughput, resource utilization, and online update EthicalApprovalandConsenttoParticipate
timeatthesystemlevel,whichhelpsindemonstrating
Notapplicable.
| the practical |     | feasibility | of  | ARL-CPO | for | real-time |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
FinTechriskpipelines.
References
| These          | findings | are | encouraging, |     | but       | the | study |              |          |            |     |                     |     |
| -------------- | -------- | --- | ------------ | --- | --------- | --- | ----- | ------------ | -------- | ---------- | --- | ------------------- | --- |
|                |          |     |              |     |           |     |       | [1] Mashrur, | A., Luo, | W., Zaidi, | N.  | A., & Robles-Kelly, |     |
| is constrained |          | by  | the use      | of  | a dataset |     | and a |              |          |            |     |                     |     |
simulatedenvironment;andoperationalconstraints, A. (2020). Machine learning for financial risk
|     |     |     |     |     |     |     |     | management: | asurvey.IEEEAccess,8,203203-203223. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------------------------- | --- | --- | --- | --- |
feedbackdelays,andcompliancerequirementsinreal
[CrossRef]
| deploymentsmayvarysignificantly. |     |     |     |     | So,anyreference |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
to real-world generalization must be understood [2] Lu,J.,Liu,A.,Dong,F.,Gu,F.,Gama,J.,&Zhang,G.
|        |      |         |          |         |     |        |     | (2018).Learningunderconceptdrift: |     |     |     | Areview.IEEE |     |
| ------ | ---- | ------- | -------- | ------- | --- | ------ | --- | --------------------------------- | --- | --- | --- | ------------ | --- |
| within | this | context | and more | testing | is  | needed | on  |                                   |     |     |     |              |     |
transactionsonknowledgeanddataengineering,31(12),
publicorproductiondatasets.
2346-2363.[CrossRef]
Future research will be based on production grade [3] Climent, F., Momparler, A., & Carmona, P. (2019).
|          |             |     |          |     |           |            |     | Anticipating | bank | distress | in  | the Eurozone: | An  |
| -------- | ----------- | --- | -------- | --- | --------- | ---------- | --- | ------------ | ---- | -------- | --- | ------------- | --- |
| software | engineering |     | problems |     | that will | facilitate |     |              |      |          |     |               |     |
safe continuous learning in regulated FinTech extremegradientboostingapproach.Journalofbusiness
research,101,885-896.[CrossRef]
| settings. | This | includes | model | versioning, |     | lineage |     |           |           |                    |     |             |     |
| --------- | ---- | -------- | ----- | ----------- | --- | ------- | --- | --------- | --------- | ------------------ | --- | ----------- | --- |
|           |      |          |       |             |     |         |     | [4] Zeng, | Z., Kaur, | R., Siddagangappa, |     | S., Rahimi, | S., |
tracking,controlledA/Btestingandcanaryrollouts,
|           |          |     |             |       |            |     |     | Balch, | T., &Veloso, | M.(2023).Financialtimeseries |     |     |     |
| --------- | -------- | --- | ----------- | ----- | ---------- | --- | --- | ------ | ------------ | ---------------------------- | --- | --- | --- |
| automated | rollback |     | strategies, | drift | monitoring |     | and |        |              |                              |     |     |     |
forecastingusingCNNandtransformer.arXivpreprint
| alerting, | and | enhanced | audit | logging | for | regulatory |     |     |     |     |     |     |     |
| --------- | --- | -------- | ----- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
arXiv:2304.04912.[CrossRef]
review. Further,mechanismsforinterpretingpolicies
|     |     |     |     |     |     |     |     | [5] Hambly,B.,Xu,R.,&Yang,H.(2023).Recentadvances |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
such as attention-based policy visualization and in reinforcement learning in finance. Mathematical
| counterfactual |     | explanations |     | will | be discussed |     | to  |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Finance,33(3),437-503.[CrossRef]
| enhance | interpretability |     | and | inter-agent |     | extensions |     |          |               |     |        |           |       |
| ------- | ---------------- | --- | --- | ----------- | --- | ---------- | --- | -------- | ------------- | --- | ------ | --------- | ----- |
|         |                  |     |     |             |     |            |     | [6] Liu, | X. Y., Xiong, | Z., | Zhong, | S., Yang, | H., & |
will be explored for interdependent financial Walid, A. (2018). Practical deep reinforcement
ecosystems.
|     |     |     |     |     |     |     |     | learning | approach | for stock | trading. | arXiv | preprint |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | -------- | ----- | -------- |
arXiv:1811.07522.[CrossRef]
|     |     |     |     |     |     |     |     | [7] Zhang,Y.,Zhao,P.,Wu,Q.,Li,B.,Huang,J.,&Tan, |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- |
DataAvailabilityStatement
M.(2020).Cost-sensitiveportfolioselectionviadeep
Datawillbemadeavailableonrequest. reinforcementlearning.IEEETransactionsonknowledge
anddataengineering,34(1),236-248.[CrossRef]
Funding [8] Li, H., Cao, Y., Li, S., Zhao, J., & Sun, Y. (2020).
XGBoostmodelanditsapplicationtopersonalcredit
Thisworkwassupportedwithoutanyfunding.
|     |     |     |     |     |     |     |     | evaluation. | IEEE | Intelligent | Systems, | 35(3), | 52-61. |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----------- | -------- | ------ | ------ |
[CrossRef]
ConflictsofInterest
|     |     |     |     |     |     |     |     | [9] Alexandre, | M., | Silva, T. | C., | Connaughton, | C., & |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------- | --- | ------------ | ----- |
Edimer Mahecha Contreras is affiliated with the Rodrigues, F. A. (2021). The drivers of systemic
Elite Group Services, San Jose, CA 95125, United risk in financial networks: a data-driven machine
States. Theauthordeclaresthatthisaffiliationhadno learninganalysis.Chaos,Solitons&Fractals,153,111588.
[CrossRef]
influenceonthestudydesign,datacollection,analysis,
interpretation, or the decision to publish. Edimer [10] Xu,Q.,Liao,Y.,Li,Q.,Zhang,J.,Song,Z.,Wang,L.,
&Yuan,X.(2024,August).SHAP-basedInterpretable
MahechaContrerasalsoservedasanAssociateEditor
ModelsforCreditDefaultAssessmentUsingMachine
| oftheICCKJournalofSoftwareEngineering |     |     |     |     |     | atthetime |     |           |         |      |               |            |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --------- | ------- | ---- | ------------- | ---------- | --- |
|                                       |     |     |     |     |     |           |     | Learning. | In 2024 | 14th | International | Conference | on  |
ofmanuscriptsubmission. Toensuretheintegrityof Software Technology and Engineering (ICSTE) (pp.
thepeer-reviewprocess,EdimerMahechaContreras
213-217).IEEE.[CrossRef]
wasnotinvolvedintheeditorialhandling,peerreview,
|     |     |     |     |     |     |     |     | [11] Jospin, | L. V., | Laga, H., | Boussaid, | F., | Buntine, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | --------- | --------- | --- | -------- |
ordecision-makingprocessforthismanuscript,which W., & Bennamoun, M. (2022). Hands-on Bayesian
washandledindependentlybyanothereditor.
neuralnetworks—Atutorialfordeeplearningusers.
167

ICCKJournalofSoftwareEngineering
IEEEComputationalIntelligenceMagazine,17(2),29-48. 359-483.[CrossRef]
[CrossRef] [19] Gama, J., Žliobaite˙, I., Bifet, A., Pechenizkiy, M., &
[12] Alasbahi, R., & Zheng, X. (2022). An online Bouchachia, A. (2014). A survey on concept drift
transfer learning framework with extreme learning adaptation. ACM computing surveys (CSUR), 46(4),
machineforautomatedcreditscoring.IEEEAccess,10, 1-37.[CrossRef]
46697-46716.[CrossRef]
|     |     |     |     | [20] | Kreuzberger, | D., | Kühl, | N., & | Hirschl, | S. (2023). |     |
| --- | --- | --- | --- | ---- | ------------ | --- | ----- | ----- | -------- | ---------- | --- |
[13] Cheng,D.,Niu,Z.,Li,J.,&Jiang,C.(2022).Regulating Machine learning operations (mlops): Overview,
systemic crises: Stemming the contagion risk in definition, and architecture. IEEE Access, 11,
networked-loansthroughdeepgraphlearning.IEEE 31866-31879.[CrossRef]
TransactionsonKnowledgeandDataEngineering,35(6),
|     |     |     |     | [21] | Liu,X.Y.,Xia,Z.,Rui,J.,Gao,J.,Yang,H.,Zhu,M.,...& |     |     |     |     |     |     |
| --- | --- | --- | --- | ---- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
6278-6289.[CrossRef]
|     |     |     |     |     | Guo,J.(2022).FinRL-Meta: |     |     | Marketenvironmentsand |     |     |     |
| --- | --- | --- | --- | --- | ------------------------ | --- | --- | --------------------- | --- | --- | --- |
[14] Bussmann,N.,Giudici,P.,Marinelli,D.,&Papenbrock, benchmarksfordata-drivenfinancialreinforcement
J.(2020).ExplainableAIinfintechriskmanagement. learning. Advances in Neural Information Processing
FrontiersinArtificialIntelligence,3,26.[CrossRef] Systems,35,1835-1849.
[15] Brim,A.(2020,January).Deepreinforcementlearning [22] Sculley,D.,Holt,G.,Golovin,D.,Davydov,E.,Phillips,
pairstradingwithadoubledeepQ-network.In2020 T., Ebner, D., ... & Dennison, D. (2015). Hidden
10thannualcomputingandcommunicationworkshopand technicaldebtinmachinelearningsystems.Advances
conference(CCWC)(pp.0222-0227).IEEE.[CrossRef] inneuralinformationprocessingsystems,28.
[16] Gašperov, B., & Kostanjčar, Z. (2022). Deep [23] Breck,E.,Cai,S.,Nielsen,E.,Salib,M.,&Sculley,D.
reinforcement learning for market making under a (2017,December).TheMLtestscore: ArubricforML
Hawkesprocess-basedlimitorderbookmodel.IEEE productionreadinessandtechnicaldebtreduction.In
controlsystemsletters,6,2485-2490.[CrossRef] 2017IEEEinternationalconferenceonbigdata(bigdata)
(pp.1123-1132).IEEE.[CrossRef]
[17] Mashetty,P.C.,Gangabathula,S.,Gangabathula,N.
|                  |               |        |             | [24] | Amershi, | S., Begel, | A., Bird, | C., | DeLine, | R., | Gall, |
| ---------------- | ------------- | ------ | ----------- | ---- | -------- | ---------- | --------- | --- | ------- | --- | ----- |
| V., Pullalarevu, | N., Chaganti, | K. R., | & Chaganti, | S.   |          |            |           |     |         |     |       |
R. (2025, July). Transfer Learning for Cross-Market H., Kamar, E., ... & Zimmermann, T. (2019, May).
|              |              |             |              |     | Software | engineering | for | machine | learning: | A   | case |
| ------------ | ------------ | ----------- | ------------ | --- | -------- | ----------- | --- | ------- | --------- | --- | ---- |
| Predictions: | Applications | in Emerging | and Volatile |     |          |             |     |         |           |     |      |
Economies. In 2025 6th International Conference on study.In2019IEEE/ACM41stInternationalConference
|     |     |     |     |     | onSoftwareEngineering: |     | SoftwareEngineeringinPractice |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------- | --- | ----------------------------- | --- | --- | --- | --- |
DataIntelligenceandCognitiveInformatics(ICDICI)(pp.
(ICSE-SEIP)(pp.291-300).IEEE.[CrossRef]
621-626).IEEE.[CrossRef]
|                   |             |             |              | [25] | Kim, | M., Zimmermann, | T., | DeLine, | R., | & Begel, | A.  |
| ----------------- | ----------- | ----------- | ------------ | ---- | ---- | --------------- | --- | ------- | --- | -------- | --- |
| [18] Ghavamzadeh, | M., Mannor, | S., Pineau, | J., & Tamar, |      |      |                 |     |         |     |          |     |
A.(2015).Bayesianreinforcementlearning: Asurvey. (2017). Data scientists in software teams: State of
theartandchallenges.IEEETransactionsonSoftware
| FoundationsandTrends®inMachineLearning, |     |     | 8(5-6), |     |     |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Engineering,44(11),1024-1038.[CrossRef]
168