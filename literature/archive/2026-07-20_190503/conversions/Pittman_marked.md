Latenrgy: Model Agnostic Latency and Energy Consumption Prediction
|     |     |     |     |     |     | for Binary |         | Classifiers |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |            | JasonM. | Pittman     |     |     |     |     |     |     |     |
UniversityofMarylandGlobalCampus
https://orcid.org/0000-0002-5198-8157
Abstract - Machine learning systems increasingly treme weather events. Across industries, ML is revolu-
4202 ceD 62  ]GL.sc[  1v14291.2142:viXra drive innovation across scientific fields and industry, tionizing healthcare through diagnostic support and ad-
yetchallengesincomputeoverhead—specifically dur- vancingfinanceviafrauddetection systems.
| ing inference—limit             |             |               | their scalability |                       | and               | sustainabil-   |         |                                           |                |                  |                |                      |                    |                |          |
| ------------------------------- | ----------- | ------------- | ----------------- | --------------------- | ----------------- | -------------- | ------- | ----------------------------------------- | -------------- | ---------------- | -------------- | -------------------- | ------------------ | -------------- | -------- |
|                                 |             |               |                   |                       |                   |                |         | Despite                                   | its widespread |                  | success,       |                      | the field          | of ML          | faces    |
| ity. Responsible                |             | AI            | guardrails,       |                       | essential         | for            | ensur-  |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | persistent                                | challenges.    |                  | One            | such                 | challenge          | is             | compute  |
| ing fairness,                   |             | transparency, |                   | and                   | privacy,          | further        | ex-     |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | overhead                                  | or the         | computational    |                | resources            |                    | consumed       | dur-     |
| acerbate                        | these       | computational |                   | demands.              |                   | This           | study   |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | ing the                                   | training       | and              | inference      | phases               |                    | of ML          | models.  |
| addresses                       | critical    | gaps          | in                | the literature,       |                   | chiefly        | the     |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | Training                                  | involves       | the              | extensive      |                      | energy             | and processing |          |
| lack of                         | generalized |               | predictive        | techniques            |                   | for            | latency |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | power                                     | required       | to optimize      |                | model                | parameters         |                | across   |
| and energy                      |             | consumption,  |                   | limited               | cross-comparisons |                |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | large datasets.                           |                | Inference,       | on             | the                  | other hand,        | focuses        | on       |
| of classifiers,                 |             | and           | unquantified      |                       | impacts           |                | of RAI  |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | generating                                | predictions    |                  | from           | trained              | models,            | where          | com-     |
| guardrails                      | on          | inference     | performance.      |                       |                   | Using          | Theory  |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | pute overhead                             |                | is characterized |                | by                   | the interplay      |                | between  |
| Construction                    |             | Methodology,  |                   | this                  | work              | constructed    |         | a                                         |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | latency                                   | (the time      | required         |                | to produce           | a                  | prediction)    | and      |
| model-agnostic                  |             | theoretical   |                   | framework             |                   | for predicting |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | energy                                    | consumption    |                  | (the power     |                      | expended           | during         | infer-   |
| latency                         | and         | energy        | consumption       |                       | in binary         | classifica-    |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | ence tasks).                              | High           | latency          |                | or energy            | consumption        |                | can      |
| tionmodelsduringinference.      |             |               |                   | Theframeworksynthe-   |                   |                |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | limit the                                 | scalability,   |                  | accessibility, |                      | and sustainability |                | of       |
| sizesclassifiercharacteristics, |             |               |                   | datasetproperties,and |                   |                |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | ML systems,                               | especially     |                  | in             | resource-constrained |                    |                | environ- |
| RAI guardrails                  |             | into          | a unified         | analytical            |                   | instrument.    |         |                                           |                |                  |                |                      |                    |                |          |
|                                 |             |               |                   |                       |                   |                |         | mentssuchasmobileandedgedevices(Henderson |                |                  |                |                      |                    |                | etal.,   |
Twopredictiveequationsarederivedthatcapturethe
2020).
| interplay   | between | these   | factors      |     | while | offering     | gener- |        |          |            |     |     |             |     |          |
| ----------- | ------- | ------- | ------------ | --- | ----- | ------------ | ------ | ------ | -------- | ---------- | --- | --- | ----------- | --- | -------- |
|             |         |         |              |     |       |              |        | Adding | to these | challenges |     | is  | the growing |     | emphasis |
| alizability | across  | diverse | classifiers. |     |       | The proposed |        |        |          |            |     |     |             |     |          |
framework provides foundational insights for design- on Responsible AI (RAI). RAI is a framework of prin-
ing efficient, responsible ML systems. It enables re- ciples aimed at ensuring AI technologies are ethical,
|           |     |           |     |          |     |           |      | fair, and | trustworthy. |     | RAI | principles |     | include | trans- |
| --------- | --- | --------- | --- | -------- | --- | --------- | ---- | --------- | ------------ | --- | --- | ---------- | --- | ------- | ------ |
| searchers | to  | benchmark | and | optimize |     | inference | per- |           |              |     |     |            |     |         |        |
formance and assists practitioners in deploying scal- parency, accountability, fairness, privacy, and robust-
ablesolutions. Finally,thisworkestablishesatheoret- ness (Li,Liu,Yang,&Ren, 2024). To operationalize
icalfoundationforbalancingcomputationalefficiency these principles, technical controls and guardrails are
|              |     |                |     |        |     |         |        | employed. | While | essential |     | for trustworthy |     | AI  | deploy- |
| ------------ | --- | -------------- | --- | ------ | --- | ------- | ------ | --------- | ----- | --------- | --- | --------------- | --- | --- | ------- |
| with ethical |     | AI principles, |     | paving | the | way for | future |           |       |           |     |                 |     |     |         |
empiricalvalidation andbroaderapplications. ment, these principles impose additional computational
|           |             |     |     |          |        |          |     | burdens       | during                               | training | and | inference. | Doing | so  | exacer- |
| --------- | ----------- | --- | --- | -------- | ------ | -------- | --- | ------------- | ------------------------------------ | -------- | --- | ---------- | ----- | --- | ------- |
| Keywords: | Responsible |     | AI, | Latency, | Energy | Consump- |     |               |                                      |          |     |            |       |     |         |
|           |             |     |     |          |        |          |     | batesexisting | issuesoflatencyandenergyconsumption. |          |     |            |       |     |         |
tion,MachineLearning,ArtificialIntelligence
|     |     |     |     |     |     |     |     | Surprisingly | given   | the     | importance |          | of     | RAI,       | the liter- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------- | ---------- | -------- | ------ | ---------- | ---------- |
|     |     |     |     |     |     |     |     | ature offers | limited |         | insights   | into     | how    | guardrails | in         |
|     |     |     |     |     |     |     |     | particular   | impact  | compute |            | overhead | during |            | inference  |
1 Introduction
|     |     |     |     |     |     |     |     | (Elesedy,Esperança, |     |     | Oprea,&Ozay, |     | 2024). | While | this |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------ | --- | ------ | ----- | ---- |
gapmayseemabstractatabroadlevel,itbecomeshighly
Machine learning (ML) has become integral to diverse relevant in specific scenarios, such as binary classifica-
scientific fields and business applications. In genomics, tionmodelsdeployedinresource-sensitive environments.
|          |     |        |         |         |           |     |       | Understanding |     | these | impacts | is critical |     | for guiding | the |
| -------- | --- | ------ | ------- | ------- | --------- | --- | ----- | ------------- | --- | ----- | ------- | ----------- | --- | ----------- | --- |
| ML helps | to  | decode | complex | genetic | patterns, |     | while | in            |     |       |         |             |     |             |     |
climatology, it improves the predictive accuracy of ex- design and scaling of ML systems in both scientific and
1

industrial contexts. both training and inference phases, with significant im-
|                             |             |                  |            |      |            |          |                | plications        | for scalability, |             | sustainability, |             | and       | accessibility |         |
| --------------------------- | ----------- | ---------------- | ---------- | ---- | ---------- | -------- | -------------- | ----------------- | ---------------- | ----------- | --------------- | ----------- | --------- | ------------- | ------- |
| This study                  |             | is motivated     |            | by   | three      | specific |                | chal-             |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | (Strubell,Ganesh, |                  | &McCallum,  |                 | 2020;       | Henderson |               | etal.,  |
| lenges                      | within      | the              | broader    | gap. |            | First,   | there          | is a              |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | 2020).            | While            | training    | requires        | substantial |           | resources     | to      |
| lack of                     | generalized |                  | predictive |      | techniques |          | for            | esti-             |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | optimize          | model            | parameters, |                 | inference   | focuses   |               | on gen- |
| mating                      | classifier  |                  | latency    | and  | energy     |          | consumption    |                   |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | erating           | predictions      | in          | real-time.      | With        |           | inference,    | met-    |
| (Mallik,Wang,Xie,Chen,&Han, |             |                  |            |      |            | 2023).   |                | Sec-              |                  |             |                 |             |           |               |         |
|                             |             |                  |            |      |            |          |                | rics such         | as latency       |             | (prediction     | time)       | and       | energy        | con-    |
| ond,                        | limited     | cross-comparison |            |      |            | of       | classification |                   |                  |             |                 |             |           |               |         |
sumption(powerusage)arecritical(Mattsonetal.,2020;
| algorithms        | has                     | hindered        |                  | understanding |             |             | of        | how             |                 |            |         |              |              |            |          |
| ----------------- | ----------------------- | --------------- | ---------------- | ------------- | ----------- | ----------- | --------- | --------------- | --------------- | ---------- | ------- | ------------ | ------------ | ---------- | -------- |
|                   |                         |                 |                  |               |             |             |           | Reddietal.,     | 2020)           | to         | total   | cost of      | ownership    |            | and user |
| different         | models                  |                 | contribute       |               | to          | these       | overheads |                 |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | experience.     | Thus,           | effective  |         | benchmarking |              | provides   | a        |
| (Cassales,        | Gomes,Bifet,Pfahringer, |                 |                  |               | &Senger,    |             |           | 2022).          |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | foundation      | for             | evaluating | and     | improving    |              | ML         | systems  |
| Finally,          | the potential           |                 | impacts          |               | of RAI      | guardrails, |           | such            |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | where achieving |                 | low        | latency | and high     | energy       | efficiency |          |
| as explainability |                         | and             | interpretability |               |             | mechanisms, |           | on              |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | is paramount    | (Cassalesetal., |            |         | 2022;        | Malliketal., |            | 2023).   |
| inference         | latency                 |                 | and              | energy        | consumption |             |           | remain          |                 |            |         |              |              |            |          |
|                   |                         |                 |                  |               |             |             |           | Additionally,   |                 | benchmarks | such    | as           | MLPerf       | and        | related  |
| underexplored     |                         | (Lietal.,2024). |                  |               |             |             |           |                 |                 |            |         |              |              |            |          |
studieshaveemphasizedthegrowingimportanceofquan-
In response to these challenges, this work sought tocon- tifying compute overhead to address operational effi-
| struct a          | model-agnostic |            | equation    |             | for            | predicting  |            | latency                |             |               |                            |                  |              |             |           |
| ----------------- | -------------- | ---------- | ----------- | ----------- | -------------- | ----------- | ---------- | ---------------------- | ----------- | ------------- | -------------------------- | ---------------- | ------------ | ----------- | --------- |
|                   |                |            |             |             |                |             |            | ciencyandenvironmental |             |               | impact(Tschandetal.,2024). |                  |              |             |           |
| and energy        | consumption    |            |             | in binary   | classification |             |            | models                 |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | A critical             | distinction |               | exists                     | between          | compute      | overhead    |           |
| during            | inference      | with       | RAI         | guardrails. |                | By          | addressing |                        |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | duringtraining         |             | andinference. |                            | Traininginvolves |              |             | iterative |
| these issues,     |                | this study | contributes |             | a              | theoretical |            | founda-                |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | optimization           | over        | large         | datasets,                  |                  | requiring    | substantial |           |
| tion for          | optimizing     |            | compute     | overhead    |                | while       | balancing  |                        |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | computational          |             | resources     | andprolongedprocessing     |                  |              |             | times     |
| the computational |                | efficiency |             | and         | ethical        | robustness  |            | of                     |             |               |                            |                  |              |             |           |
|                   |                |            |             |             |                |             |            | (Strubelletal.,        |             | 2020).        | Inference,                 |                  | by contrast, |             | focuses   |
MLsystems.
|     |     |     |     |     |     |     |     | on real-time | applications, |     | where | latency |     | (the | time re- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | ----- | ------- | --- | ---- | -------- |
Theremainder ofthispaperisorganized asfollows: Sec- quired to produce a prediction) and energy consumption
| tion 2 reviews |     | related | work, | providing |     | a foundation |     | of                |     |           |     |            |     |              |     |
| -------------- | --- | ------- | ----- | --------- | --- | ------------ | --- | ----------------- | --- | --------- | --- | ---------- | --- | ------------ | --- |
|                |     |         |       |           |     |              |     | (thepowerrequired |     | toperform |     | inference) |     | areparamount |     |
background research. Section 3 details the theoretical (Henderson etal.,2020)). Althoughtheliteraturehastra-
methodology usedtoderivethepredictive equation. Sec- ditionally emphasized the training phase, inference has
| tion 4 presents     |         | the derived |               | equation | and                | its        | components. |                       |             |               |                |             |              |              |          |
| ------------------- | ------- | ----------- | ------------- | -------- | ------------------ | ---------- | ----------- | --------------------- | ----------- | ------------- | -------------- | ----------- | ------------ | ------------ | -------- |
|                     |         |             |               |          |                    |            |             | receivedcomparatively |             |               | lessattention. |             |              |              |          |
| Finally,            | Section | 5           | concludes     | with     | a                  | discussion |             | of the                |             |               |                |             |              |              |          |
|                     |         |             |               |          |                    |            |             | To address            | some        | of            | these          | challenges, |              | benchmarking |          |
| study’simplications |         |             | anddirections |          | forfutureresearch. |            |             |                       |             |               |                |             |              |              |          |
|                     |         |             |               |          |                    |            |             | frameworks            | such        | as            | MLPerf         | have        | been         | developed.   |          |
|                     |         |             |               |          |                    |            |             | MLPerf                | provides    | comprehensive |                | benchmarks  |              |              | for both |
|                     |         |             |               |          |                    |            |             | training              | and         | inference,    | enabling       |             | standardized |              | perfor-  |
| 2 Related           |         | work        |               |          |                    |            |             |                       |             |               |                |             |              |              |          |
|                     |         |             |               |          |                    |            |             | mance                 | evaluations | across        | hardware       |             | and          | software     | plat-    |
|                     |         |             |               |          |                    |            |             | forms (Mattsonetal.,  |             |               | 2020).         | The         | MLPerf       | Inference    |          |
A comprehensive understanding of this study’s contribu- Benchmark evaluates system performance on tasks such
tion requires familiarity with three key topics: bench- as image classification and object detection, offering in-
|         |     |         |           |     |     |           |         | sights into | latency | and | energy | efficiency | across |     | different |
| ------- | --- | ------- | --------- | --- | --- | --------- | ------- | ----------- | ------- | --- | ------ | ---------- | ------ | --- | --------- |
| marking | ML  | compute | overhead, |     | the | trade-off | between |             |         |     |        |            |        |     |           |
latency and energy consumption, as well as the founda- implementations (Reddietal., 2020). Further, MLPerf
tionforRAI.Thefollowing sections summarize seminal Powerintroduces methodologies forassessing energy ef-
ficiency,reflectingthegrowingconcernovertheenviron-
| and highly | influential |     | works | in  | each | topic. | Such | exist- |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ----- | --- | ---- | ------ | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
ing literature provides necessary context and grounding mental impact of AI workloads (Tschandetal., 2024).
for this study’s theoretical framework and its focus on While these benchmarks are instrumental in understand-
model-agnostic predictions ofcomputeoverhead. ing empirical performance, they focus on specific tasks
|                  |     |         |           |          |     |          |          | and lack            | predictive | models    |                 | that generalize |                 | across | classi- |
| ---------------- | --- | ------- | --------- | -------- | --- | -------- | -------- | ------------------- | ---------- | --------- | --------------- | --------------- | --------------- | ------ | ------- |
|                  |     |         |           |          |     |          |          | fiersoroperational  |            | contexts. |                 |                 |                 |        |         |
| 2.1 Benchmarking |     |         | MLCompute |          |     | Overhead |          |                     |            |           |                 |                 |                 |        |         |
|                  |     |         |           |          |     |          |          | Despiteadvancements |            |           | inbenchmarking, |                 | significantgaps |        |         |
|                  |     |         |           |          |     |          |          | remain.             | First,     | current   | benchmarks      |                 | such as         | MLPerf | pro-    |
| Benchmarking     |     | compute |           | overhead | in  | machine  | learning |                     |            |           |                 |                 |                 |        |         |
videempiricalperformancedatabutdonotoffergeneral-
| (ML) is | essential | for | understanding |     | and | optimizing |     | the             |     |            |     |            |     |         |         |
| ------- | --------- | --- | ------------- | --- | --- | ---------- | --- | --------------- | --- | ---------- | --- | ---------- | --- | ------- | ------- |
|         |           |     |               |     |     |            |     | ized predictive |     | techniques | for | estimating |     | latency | and en- |
performanceandefficiencyofMLsystemsacrossdiverse
|     |     |     |     |     |     |     |     | ergy consumption |     | across | classifiers. |     | This | limitation | hin- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ------------ | --- | ---- | ---------- | ---- |
tasks and deployment scenarios. Compute overhead en- ders the ability to anticipate performance bottlenecks or
compassesthecomputationalresourcesconsumedduring
2

energy demands in novel deployment scenarios, partic- the reliance on specific algorithmic properties limits the
ularly those involving Responsible AI (RAI) guardrails immediate applicability of these findings to non-neural
(Malliketal., 2023). Second, no universally accepted networkclassifiers.
metrics exist for comparing latency and energy con-
In contrast, Hauschild and Hellbrück
sumption across ML frameworks and hardware config-
(Hauschild&Hellbrück, 2022) analyzed convolu-
urations, making cross-platform evaluations inconsistent
tional neural networks (CNNs) deployed on Internet of
(Mattsonetal.,2020).
Things (IoT) edge devices, emphasizing the dependency
Additionally, the literature on benchmarking compute oflatencyandenergyconsumption onmodelcomplexity
overhead demonstrates a limited cross-comparison of andwirelessdatarates. Theresultsshowthatsimplifying
classification algorithms (e.g., SVM, k-Nearest Neigh- CNN architectures can yield substantial efficiency gains
bors, Random Forest, and Neural Networks) concerning in resource-constrained environments, underscoring the
their effects on latency and energy consumption. Most importance of tailoring models to deployment scenarios.
studies focus on single-model architectures or narrowly However, this approach is tightly coupled to CNNs and
compare a few model types (Cassalesetal., 2022). This does not address broader classification paradigms, such
narrow scope restricts generalizability, leaving gaps in asdecision treesorsupportvectormachines.
understanding how diverse classifiers perform in terms
While these studies offer valuable insights into optimiz-
of computational efficiency across real-world scenarios.
ing latency and energy efficiency, the work reflects a
Addressingtheselimitationsrequiresatheoretical frame-
broader trend in the literature of focusing on specific
work capable of predicting latency and energy consump-
modelsorhardwareconfigurations(Cassalesetal.,2022;
tion in a model-agnostic manner. Doing so also requires
Tschandetal., 2024). This limitation underscores the
anunderstandingoftheinherenttradeoffbetweenlatency
need for generalized predictive techniques that span di-
andenergyconsumptionduringinferenceonMLmodels.
verseclassification algorithms, bridgingthegapbetween
theoretical models and empirical benchmarks. Address-
ingthis challenge iscritical foradvancing thescalability
2.2 The Latency and Energy Consumption
andefficiencyofMLsystems,particularly astheintegra-
Tradeoff
tion ofResponsible AI(RAI)guardrails introduces addi-
tionalcomputational overhead.
The relationship between latency and energy consump-
tion during machine learning inference is complex, of-
ten involving trade-offs influenced by model architec-
2.3 RAI Controlsand Guardrails
ture, hardware, and optimization strategies. Generally,
reducing latency requires increased computational re-
Put simply, RAI ensures AI systems are developed and
sources, which can lead to higher energy consumption.
deployed in ways that are ethical (Floridietal., 2018;
Conversely, minimizing energy usage may involve tech-
Mittelstadt, Allo,Taddeo,Wachter, &Floridi, 2016).
niquesthatintroduce additional processing time,thereby
Ethical, in this context, includes fairness, transparency,
increasing latency. This inverse relationship is particu-
privacy, security, and trustworthiness as core principles.
larly evident inresource-constrained environments, such
The idea is an AI system can be considered responsible
as edge devices, where balancing performance and effi-
when the set of relevant principles are present. Here,
ciencyiscritical.
one should consider present as technical continuous
Recent studies have explored the trade-off between monitoring.
latency and energy consumption during machine
To that end, ethical principles have experienced rapid
learning inference, with varying levels of generaliz-
theoretical and practical expansion. In a short time, re-
ability across classification algorithms. For instance,
searchershavedevelopedrobusttechnicalframeworksto
researchers examining multilayer perceptrons (MLPs)
measure and evaluate these principles. Two prominent
demonstrated that hyperparameter optimization could
examplesaretheMicrosoftResponsibleToolboxandthe
significantly reduce energy consumption during infer-
IBM AI 360 Toolkit. Yet, as much as AI practitioners
ence with minimal impact on classification accuracy
canusetheseframeworkstoevaluatemodels,researchers
(Desislavov, Martínez-Plumed, &Hernández-Orallo,
(Radclyffe, Ribeiro,&Wortham, 2023; Luetal., 2024)
2021). By tuning model complexity, such as reducing
suggestRAIisoneofthemostcriticalchallengespresent
hidden layers or using lower-precision arithmetic, the
inAIandML.
study highlights strategies that, while tested on MLPs,
may generalize to other model architectures. However, Culturally, the rapid expansion has been motivated
3

by demonstrable harm arising from a lack of RAI. 3 Method
Such examples include discriminatory sentenc-
ing and parole decisions in the US justice system
This work was motivated by a single research question:
(Angwin,Larson,Mattu,&Kirchner, 2022) as well as
Whatvariables,coefficients,andpropositionaloperations
Amazon’s recruitment tool (Dastin, 2022). Increasing
are necessary for a model-agnostic equation to be ca-
legal and regulatory requirements such as the US Presi-
pable of predicting latency and energy consumption in
dent’sExecutiveOrderandtheEU’sAIAct(Wörsdörfer,
binary classification models during inference with RAI
2023)arealsodrivingRAIresearch.
guardrails? Toanswer thisquestion, thestudy employed
Meanwhile, the literature (Khanetal., 2022;
Theory Construction Methodology (TCM) to derive the
Alzubaidietal., 2023) has coalesced around five
model-agnostic equation.
specific RAI principles: explainability, bias or fairness,
TCM is a structured approach to developing theoretical
robustness or safety, transparency or interpretability,
frameworks by defining key variables, establishing rela-
and privacy. Additional principles, such as explicability
tionships, and formalizing them into mathematical mod-
(Prem, 2023) and accountability (Liuetal., 2022), have
els (Dubin, 1978). While TCM has been widely applied
been studied but ultimately fall within the scope of one
in theoretical modeling, its application to derive predic-
or more of the five specific principles. Consequently,
tiveequations forlatencyandenergy consumption inthe
industry (IBM, Microsoft, US Department of Defense)
context of RAI guardrails represents a novel adaptation
has settled on explainability, bias, robustness, inter-
of this methodology. This approach is particularly well-
pretability, and privacy for practical implementation
suited to the research problem because the abstraction
of RAI. Trustworthiness tends to be discussed as an
and generalization required for a predictive equation ap-
emergent principle only present when the complete set
plicable across diverse classifiers necessitates a theoreti-
ofRAIprinciples havesoundimplementations.
calframework(Kaplan&Haenlein,2019).
On that note, the RAI principles can be implemented
The TCM process began with identifying core variables
either as a control or guardrail. On the one hand,
influencing latency and energy consumption during in-
controls are techniques applied during the training
ference. These variables were selected based on prior
phase of a model to ensure that the AI system be-
empirical findings and theoretical reasoning, ensuring
haves ethically and responsibly (Mitchelletal., 2019;
relevance to diverse classification contexts and com-
Mehrabi,Morstatter, Saxena,Lerman,&Galstyan,
putational scenarios. For example, the computational
2021). On the other hand, guardrails are measures
overhead introduced by explainability and interpretabil-
implemented in deployed models to assess the run-
ity guardrails, such as those implemented using SHAP
time behavior of models (Raji&Buolamwini, 2019;
(Lundberg, 2017) or LIME (Ribeiro,Singh,&Guestrin,
Varshney&Alemzadeh, 2017). The aim is to ensure
2016), was identified as a critical variable. This as-
that the AI system continues to operate responsibly and
sumption is supported by computational complexity the-
ethically throughout the life of the system deployment
ory, which posits that even linear increases in input size
(Holstein, WortmanVaughan,DauméIII,Dudik,&Wallach,
(O(n))resultinproportional growthincomputational de-
2019).
mand. In the context of RAI guardrails, the overhead
Despite the stated need for RAI and the availability of
arises from explainability mechanisms that augment in-
broad technical frameworks, the computational costs of
ference operations with additional interpretive computa-
implementing these guardrails are often excluded from
tions.
benchmarking studies. For example, the additional
Relationships among these variables—such as the in-
overhead introduced by explainability mechanisms dur-
verse correlation between latency and energy con-
ing inference remains an under explored area (Lietal.,
sumption—are then proposed based on prior research
2024). Without incorporating RAI considerations, exist-
(Henderson etal., 2020; Malliketal., 2023). For in-
ingbenchmarksriskbecomingoutdatedorincompleteas
stance,studiessuchasthosebyHauschildandHellbrück
the adoption of RAI increases. Moreover, and perhaps
(Hauschild&Hellbrück,2022)demonstratehowcompu-
mostimportantly, the fieldisbereft ofoperationally vali-
tational trade-offs between latency andenergy efficiency
dated knowledge of how runtime RAImay be more of a
areparticularly evidentinedgecomputing environments.
poisonthanacure.
Coefficients are incorporated to represent adjustable fac-
tors, including the type of classifier and specific deploy-
ment conditions. These variables and coefficients are
connected through mathematical operations, such as ad-
4

ditive and multiplicative terms, to capture their interac- Data type is represented as a categorical variable with
tions(Cassalesetal.,2022). tabulardataencoded as0,textas1,andimagedataas2.
Finally, the equation is formalized to ensure generaliz- RAI guardrails (G) encompass five principles: explain-
ability, interpretability, and scalability across classifiers ability,fairness,interpretability,safety,andprivacy. Each
suchasSVM,k-NearestNeighbors, RandomForest,and principle is modeled as a binary state ([0,1]), which,
NeuralNetworks. Thistheoreticalframeworkestablishes when active, can include a continuous intensity score.
a foundation for subsequent empirical validation, where For example, explainability (expl) could take a value of
its predictive accuracy will be tested against experimen- 0.7,representing partialfeature-level explanations cover-
taldataindiverseoperational settings. ingthetop70%offeatures.
4 Discussion 4.3 Prediction Equations
The general equation was expanded into two prediction
The development of a model-agnostic equation for pre-
equations,capturinglatency(L)andenergyconsumption
dictinglatencyandenergyconsumption beganwithiden-
(E). These equations model inference performance as a
tifying foundational variables (Table 1). These variables
function of algorithm type, dataset characteristics, and
are organized into three sets—classification algorithm,
thecomputational costofRAIguardrails.
RAI guardrail, and dataset characteristics—all of which
serve as inputs to a prediction function f. The outputs The latency equation (2) incorporates logarithmic scal-
ofthefunction, latency (L)and energy consumption (E), ing for dataset size, capturing the diminishing impact of
arerepresented collectively asO. largerdatasetsonprediction time:
4.1 General Equation
L=α+β A+β log(n)+γ p+δ t+∑φ g +ε (2)
A D D D G,i i
i
A general equation (1) was constructed to unify the di-
mensionsoflatencyandenergyconsumptionintoacohe-
Theenergy consumption equation (3)applies linear scal-
siveanalytical framework:
ing for dataset size to account for cumulative resource
demandsduringinference:
O= f(A,D,G) (1)
This equation serves two purposes. First, it provides E =α ′ +β A+β ′ n+γ p+δ t+∑φ ′ g +ε ′ (3)
A D D D G,i i
a unified framework to compare inference performance i
across binary classifiers. Second, it establishes a foun-
dation for synthesizing disparate dimensions of model Bothequationsusecoefficientstomodelthecontribution
performance intoapredictive tool,enabling cross-model ofeachvariable, assummarizedinTable2.
comparisons,performanceprediction,andtheintegration
ofRAIguardrails intosystemdesign.
4.4 Noveltyand Practical Implications
4.2 Expanded Variables These equations provide a novel approach to predicting
inference performance across diverse binary classifiers.
Eachvariablesetinthegeneralequationisexpandedinto Unlike prior studies, which focus on empirical bench-
measurable elements. Algorithm type (A) contains four marking or specific algorithms (Cassalesetal., 2022;
discrete elements: support vector machines (SVM), k- Malliketal., 2023), this framework offers generalizabil-
nearest neighbors (k-NN),random forests(RF),andneu- ity and scalability. Furthermore, it uniquely integrates
ral networks (NN). Categorical encoding is used to rep- the computational cost of RAI guardrails, addressing a
resentbinaryclassifiersasa∈SVM,k-NN,RF,NN,with criticalgapintheliterature(Lietal.,2024;Ribeiroetal.,
A encoded as 1,0,0,0 to predict L or E for SVM,for in- 2016).
stance.
Future empirical validation willuse benchmarks such as
Dataset characteristics (D) include the number of sam- MLPerf (Mattsonetal., 2020) to evaluate the predictive
ples (n), feature dimensionality (p), and data type (t). accuracy of these models. Practical applications include
5

|     |     |     |     | Table1: | Foundational |     | variablesinamodel-agnostic |     |     |     | equa- |     |     |     |     |
| --- | --- | --- | --- | ------- | ------------ | --- | -------------------------- | --- | --- | --- | ----- | --- | --- | --- | --- |
tion
|     |     |     |                   | VariableSet                   |                |                |          |                |           | Symbol    |          |     |     |     |     |
| --- | --- | --- | ----------------- | ----------------------------- | -------------- | -------------- | -------- | -------------- | --------- | --------- | -------- | --- | --- | --- | --- |
|     |     |     |                   | Classification                |                | algorithm      |          |                |           | A         |          |     |     |     |     |
|     |     |     |                   | RAIguardrail                  |                |                |          |                |           | G         |          |     |     |     |     |
|     |     |     |                   | Datasetcharacteristics        |                |                |          |                |           | D         |          |     |     |     |     |
|     |     |     |                   | Outputmetric                  |                |                |          |                |           | O         |          |     |     |     |     |
|     |     |     |                   | Note:                         | The prediction |                | function | f is undefined |           | in        | the gen- |     |     |     |     |
|     |     |     |                   | eral equation.                |                | The formalized |          | prediction     | equations |           | for L    |     |     |     |     |
|     |     |     |                   | andE                          | areoutlined    | inTable2.      |          |                |           |           |          |     |     |     |     |
|     |     |     | Table2:           | Coefficientsformodel-agnostic |                |                |          | prediction     |           | equations |          |     |     |     |     |
|     |     |     | CoefficientSet    |                               |                |                |          |                | Symbol    |           | Variable |     |     |     |     |
|     |     |     | Baselineinference |                               |                |                |          |                | α,α       | ′         |          | O   |     |     |     |
′
|     |     |     | Errortermsforvariability1 |     |     |     |     |     | ε,ε |     |     | -   |     |     |     |
| --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
′
|     |     |     | Algorithm | type |     |     |     |     | β   | A ,β |     | A   |     |     |     |
| --- | --- | --- | --------- | ---- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
A
|     |     |     | Datasetsize |     |     |     |     |     | β   | ,β ′ |     | D   |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     |     |             |     |     |     |     |     |     | D D  |     | n   |     |     |     |
′
|     |     |     | Featuredimensionality |     |     |     |     |     | γ   | ,γ  |     | D   |     |     |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |                       |     |     |     |     |     | D   | D   |     | p   |     |     |     |
′
|     |     |     | Datasettype |     |     |     |     |     | δ D | ,δ  |     | D t |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
D
|     |     |     | Guardrails |     |     |     |     |     | φ   | ,φ ′ |     | G   |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
G,i G,i
1
|     |     |     | Note: | Errortermshandleunmodeled |     |     |     | variability |     | duringinference. |     |     |     |     |     |
| --- | --- | --- | ----- | ------------------------- | --- | --- | --- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- |
optimizing ML systems for edge devices, estimating re- overhead of RAI guardrails into a cohesive analytical
source demands for RAI-integrated classifiers, and en- tool. Unlike previous studies that focus on specific clas-
abling informed trade-offs between latency, energy con- sifiers or empirical benchmarks, this work offers gener-
sumption, andethicalrobustness. alizability and scalability, bridging theoretical modeling
|     |     |     |     |     |     |     |     | withpractical |              | performance |                | evaluation. |     |                 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | ----------- | -------------- | ----------- | --- | --------------- | --- |
|     |     |     |     |     |     |     |     | Thebroader    | significance |             | ofthisresearch |             |     | liesinitsimpli- |     |
5 Conclusion cationsfordesigninganddeployingefficient,responsible
|                |               |          |              |           |                  |              |         | ML systems.        |                | For researchers, |                      | the              | predictive |               | equations    |
| -------------- | ------------- | -------- | ------------ | --------- | ---------------- | ------------ | ------- | ------------------ | -------------- | ---------------- | -------------------- | ---------------- | ---------- | ------------- | ------------ |
|                |               |          |              |           |                  |              |         | provide            | a foundational |                  | tool                 | for benchmarking |            |               | and opti-    |
| AI broadly,    | and           | ML       | in specific, | continues |                  | to transform |         |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | mizing             | inference      | performance      |                      | across           | diverse    |               | classifiers. |
| science        | and industry. |          | Yet,         | AI and    | ML scalability   |              | and     |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | For practitioners, |                | they             | enable               | informed         |            | decisions     | about        |
| accessibility  | are           | often    | constrained  |           | by compute       | overhead.    |         |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | deploying          | models         | in               | resource-constrained |                  |            | environments, |              |
| The literature |               | suggests | such         | issues    | are particularly |              | no-     |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | such as            | edge           | or mobile        | devices,             | while            |            | maintaining   | ethi-        |
| table during   | inference.    |          | Challenges   |           | such as          | the          | lack of |                    |                |                  |                      |                  |            |               |              |
|                |               |          |              |           |                  |              |         | cal robustness.    |                | This             | work                 | also aligns      | with       | the           | growing      |
generalized predictive techniques for latency and energy need for sustainable AI, offering a pathway to balance
| consumption, |            | limited | cross-comparison |     | of            | classification  |        |                |     |                                      |                |     |               |     |         |
| ------------ | ---------- | ------- | ---------------- | --- | ------------- | --------------- | ------ | -------------- | --- | ------------------------------------ | -------------- | --- | ------------- | --- | ------- |
|              |            |         |                  |     |               |                 |        | computational  |     | efficiencywithethicalconsiderations. |                |     |               |     |         |
| algorithms,  | and        | the     | unquantified     |     | computational |                 | impact |                |     |                                      |                |     |               |     |         |
|              |            |         |                  |     |               |                 |        | In conclusion, |     | this                                 | study provides |     | a theoretical |     | founda- |
| of RAI       | guardrails | have    | left critical    |     | gaps in       | the literature. |        |                |     |                                      |                |     |               |     |         |
This study aimed to address these gaps by developing tion for understanding and predicting inference perfor-
|                  |     |          |         |     |               |     |         | manceinMLsystems. |     |     | Byaddressing |     | criticalgapsinthe |     |     |
| ---------------- | --- | -------- | ------- | --- | ------------- | --- | ------- | ----------------- | --- | --- | ------------ | --- | ----------------- | --- | --- |
| a model-agnostic |     | equation | capable |     | of predicting |     | latency |                   |     |     |              |     |                   |     |     |
literature,itlaysthegroundworkforfutureadvancements
| and energy      | consumption   |                    | in        | binary | classification |           | models |                   |     |                          |     |             |     |            |     |
| --------------- | ------------- | ------------------ | --------- | ------ | -------------- | --------- | ------ | ----------------- | --- | ------------------------ | --- | ----------- | --- | ---------- | --- |
|                 |               |                    |           |        |                |           |        | in model-agnostic |     | performance              |     | prediction, |     | enabling   | the |
| duringinference |               | withRAIguardrails. |           |        |                |           |        |                   |     |                          |     |             |     |            |     |
|                 |               |                    |           |        |                |           |        | nextgeneration    |     | ofscalableandresponsible |     |             |     | AIsystems. |     |
| The key         | contributions |                    | of this   | work   | include        | a         | model- |                   |     |                          |     |             |     |            |     |
| agnostic        | theoretical   |                    | framework | for    | analyzing      | inference |        |                   |     |                          |     |             |     |            |     |
performanceandtwopredictiveequationsforlatencyand
| energyconsumption. |     |         | Thesemodelssynthesizealgorithm |     |                     |     |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | ------------------------------ | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| characteristics,   |     | dataset | properties,                    |     | andthecomputational |     |     |     |     |     |     |     |     |     |     |
6

5.1 Limitations ity of the equations to different input variables, such as
|                       |           |          |         |                  |     |             | dataset            | characteristics |     |                  | and RAI      | guardrails, |            | to refine | the       |
| --------------------- | --------- | -------- | ------- | ---------------- | --- | ----------- | ------------------ | --------------- | --- | ---------------- | ------------ | ----------- | ---------- | --------- | --------- |
| While this            | study     | provides |         | a foundational   |     | framework   | for modelsfurther. |                 |     |                  |              |             |            |           |           |
| predicting            | inference |          | latency | and energy       |     | consumption | in                 |                 |     |                  |              |             |            |           |           |
|                       |           |          |         |                  |     |             | Furthermore,       |                 | the | generalizability |              | of          | the L      | and       | E predic- |
| binary classification |           |          | models, | five limitations |     | should      | be                 |                 |     |                  |              |             |            |           |           |
|                       |           |          |         |                  |     |             | tive               | equations       |     | may be           | investigated |             | by varying |           | the set A |
acknowledged.
|     |     |     |     |     |     |     | across | a   | variety | of AI | subfields. | Of  | particular |     | interest, |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------- | ----- | ---------- | --- | ---------- | --- | --------- |
First,theprediction equations relyonassumptions about given the mainstream perception of AI, might be the ap-
|          |                |     |      |                |     |         | plication |     | of the | framework |     | to Large | Language |     | Models |
| -------- | -------------- | --- | ---- | -------------- | --- | ------- | --------- | --- | ------ | --------- | --- | -------- | -------- | --- | ------ |
| variable | relationships, |     | such | as logarithmic |     | scaling | for       |     |        |           |     |          |          |     |        |
dataset size in latency prediction and linear scaling (LLMs), where inference latency and energy efficiency
for energy consumption. While these assumptions are arecriticalduetotheirsizeandcomplexity. Additionally,
groundedinpriorresearchandtheoreticalreasoning,they frontier research areas such as neuro-symbolic AI repre-
|         |       |         |            |              |     |     | sent     | a compelling |     | opportunity |     | for | extending | the | frame- |
| ------- | ----- | ------- | ---------- | ------------ | --- | --- | -------- | ------------ | --- | ----------- | --- | --- | --------- | --- | ------ |
| may not | fully | capture | real-world | complexities |     | in  | all sce- |              |     |             |     |     |           |     |        |
narios. Additionalresearch, moreespecially practicalex- worktohybrid models that combine symbolic reasoning
perimentationmayrevealtowhatextentsuchalimitation withdeeplearning. Theseextensions couldprovidevalu-
|     |     |     |     |     |     |     | able | insights | into | the computational |     |     | trade-offs |     | in emerg- |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ---- | ----------------- | --- | --- | ---------- | --- | --------- |
isaddressable.
ingAIparadigms.
| Second, | thefocus | onbinary |     | classification |     | tasksexcludes |     |     |     |     |     |     |     |     |     |
| ------- | -------- | -------- | --- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
multi-class classification and other ML tasks, such as Another avenue for future work involves refining the
regression or clustering, which may involve different representation of RAI guardrails. Current binary and
|               |     |             |     |               |     |           | intensity-scale |     |     | representations |     | may | oversimplify |     | the |
| ------------- | --- | ----------- | --- | ------------- | --- | --------- | --------------- | --- | --- | --------------- | --- | --- | ------------ | --- | --- |
| computational |     | trade-offs. |     | Along similar |     | thinking, | this            |     |     |                 |     |     |              |     |     |
work does not account for potential innovations becom- computational demands of advanced guardrails, such as
ingavailable inthefuture. differentialprivacy,adversarialrobustness,ornuancedin-
|                   |                |           |                 |                 |         |              | terpretability                 |     | mechanisms. |        | Developing    |     | more              | granular | or    |
| ----------------- | -------------- | --------- | --------------- | --------------- | ------- | ------------ | ------------------------------ | --- | ----------- | ------ | ------------- | --- | ----------------- | -------- | ----- |
| Third, the        | representation |           | of              | RAI guardrails, |         | while        | prac-                          |     |             |        |               |     |                   |          |       |
|                   |                |           |                 |                 |         |              | context-aware                  |     |             | models | for guardrail |     | contributions     |          | could |
| tical, simplifies |                | potential |                 | computational   |         | impact.      | Com-                           |     |             |        |               |     |                   |          |       |
|                   |                |           |                 |                 |         |              | enhancetheframework’sprecision |     |             |        |               |     | andapplicability. |          |       |
| plex guardrails,  |                | such      | as differential |                 | privacy | or trustwor- |                                |     |             |        |               |     |                   |          |       |
thiness mechanisms, may require more nuanced model- Finally, while this study focused on binary classifica-
ingtofullycaptureresource demands. tion tasks, future research could extend the framework
|                                                    |                 |                  |                                 |              |                     |         | to                  | multi-class | classification |             | and   | other             | ML  | tasks,     | such as |
| -------------------------------------------------- | --------------- | ---------------- | ------------------------------- | ------------ | ------------------- | ------- | ------------------- | ----------- | -------------- | ----------- | ----- | ----------------- | --- | ---------- | ------- |
| Fourth,theframeworkabstractsdatasetcharacteristics |                 |                  |                                 |              |                     |         | to                  |             |                |             |       |                   |     |            |         |
|                                                    |                 |                  |                                 |              |                     |         | regression          |             | or             | clustering. | These | extensions        |     | would      | test    |
| size, feature                                      | dimensionality, |                  |                                 | and data     | type.               | Other   | impor-              |             |                |             |       |                   |     |            |         |
|                                                    |                 |                  |                                 |              |                     |         | the                 | framework’s |                | scalability |       | and adaptability, |     | addressing |         |
| tant factors,                                      | such            | as               | data quality                    | or           | sparsity,           | are     | not in-             |             |                |             |       |                   |     |            |         |
|                                                    |                 |                  |                                 |              |                     |         | broaderapplications |             |                | inAI.       |       |                   |     |            |         |
| cludedandcouldaffectpredictions                    |                 |                  |                                 |              | inspecificcontexts. |         |                     |             |                |             |       |                   |     |            |         |
| Finally,                                           | this study      | presents         |                                 | theoretical  | equations           | without |                     |             |                |             |       |                   |     |            |         |
| empiricalvalidation.                               |                 |                  | Whilethemodelsarerigorous,their |              |                     |         |                     |             |                |             |       |                   |     |            |         |
| accuracy                                           | and             | generalizability |                                 | remain       | untested.           |         | Future References   |             |                |             |       |                   |     |            |         |
| work will                                          | involve         | validating       |                                 | these        | equations           | with    | exper-              |             |                |             |       |                   |     |            |         |
| imental                                            | data across     |                  | diverse                         | classifiers, | datasets,           |         | and de-             |             |                |             |       |                   |     |            |         |
Alzubaidi,L.,Al-Sabaawi,A.,Bai,J.,Dukhan,A.,Alke-
| ployment | environments |     | to  | ensure their | practical | applica- |     |       |     |               |     |         |        |         |     |
| -------- | ------------ | --- | --- | ------------ | --------- | -------- | --- | ----- | --- | ------------- | --- | ------- | ------ | ------- | --- |
|          |              |     |     |              |           |          |     | nani, | A.  | H., Al-Asadi, |     | A., ... | others | (2023). | To- |
bility.
|                               |         |       |     |                 |       |     |           | wards                        | risk-free  |                       | trustworthy      |               | artificial      | intelligence: |         |
| ----------------------------- | ------- | ----- | --- | --------------- | ----- | --- | --------- | ---------------------------- | ---------- | --------------------- | ---------------- | ------------- | --------------- | ------------- | ------- |
|                               |         |       |     |                 |       |     |           | Significanceandrequirements. |            |                       |                  |               | International   |               | Jour-   |
|                               |         |       |     |                 |       |     |           | nalofIntelligent             |            |                       | Systems,2023(1), |               |                 | 4459198.      |         |
| 5.2 Future                    |         | work  |     |                 |       |     |           |                              |            |                       |                  |               |                 |               |         |
|                               |         |       |     |                 |       |     | Angwin,   |                              | J.,Larson, | J.,Mattu,             |                  | S.,&Kirchner, |                 | L.            | (2022). |
|                               |         |       |     |                 |       |     |           | Machine                      |            | bias. In              | Ethics           | of data       | and             | analytics     | (pp.    |
| There are                     | several | areas | for | future work     | based | on  | the the-  |                              |            |                       |                  |               |                 |               |         |
|                               |         |       |     |                 |       |     |           | 254–264).                    |            | AuerbachPublications. |                  |               |                 |               |         |
| oreticalframeworkdemonstrated |         |       |     | inthisresearch. |       |     |           |                              |            |                       |                  |               |                 |               |         |
|                               |         |       |     |                 |       |     | Cassales, |                              | G., Gomes, | H.M.,                 |                  | Bifet,        | A., Pfahringer, |               | B.,&    |
Foremost, experimentation is necessary to validate and Senger, H. (2022). Balancing performance and
quantify the coefficients in the latency (L) and energy energy consumption of bagging ensembles for the
consumption (E)prediction equations. Empiricalstudies classification of data streams in edge computing.
usingbenchmark datasets andplatformssuchasMLPerf IEEE Transactions on Network and Service Man-
willhelpcalibrate these coefficients, ensuring theiraccu- agement,20(3),3038–3054.
racy across diverse classifiers and deployment environ- Dastin, J. (2022). Amazon scraps secret ai recruiting
ments. Validationeffortsshouldalsoexplorethesensitiv- tool that showed bias against women. In Ethics of
7

dataandanalytics(pp.296–299). AuerbachPubli- Lundberg, S. (2017). A unified approach to in-
cations. terpreting model predictions. arXiv preprint
Desislavov, R., Martínez-Plumed, F., & Hernández- arXiv:1705.07874.
Orallo, J. (2021). Compute and energy con- Mallik, A., Wang, H., Xie, J., Chen, D., & Han, K.
sumption trends in deep learning inference. arXiv (2023). Epam: A predictive energy model for mo-
preprintarXiv:2109.05472. bile ai. In Icc 2023-ieee international conference
Dubin,R. (1978). Theorybuilding. TheFreePress. oncommunications (pp.954–959).
Elesedy, H., Esperança, P. M., Oprea, S. V., & Ozay, M. Mattson, P., Reddi, V. J., Cheng, C., Coleman, C., Di-
(2024). Lora-guard: Parameter-efficient guardrail amos, G., Kanter, D., ... others (2020). Mlperf:
adaptation for content moderation of large lan- Anindustrystandardbenchmarksuiteformachine
guagemodels. arXivpreprintarXiv:2407.02987. learningperformance. IEEEMicro,40(2), 8–16.
Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., &
Chazerand, P., Dignum, V., ... others (2018). Galstyan, A. (2021). A survey on bias and fair-
Ai4people—anethicalframeworkforagoodaiso- nessinmachinelearning. ACMcomputingsurveys
ciety: opportunities, risks, principles, and recom- (CSUR),54(6),1–35.
mendations. Mindsandmachines,28,689–707. Mitchell,M.,Wu,S.,Zaldivar,A.,Barnes,P.,Vasserman,
Hauschild, S.,& Hellbrück, H. (2022). Latency and en- L., Hutchinson, B., ... Gebru, T. (2019). Model
ergyconsumption ofconvolutional neuralnetwork cards for model reporting. In Proceedings of the
models from iot edge perspective. In Global iot conference on fairness, accountability, and trans-
summit(pp.385–396). Springer. parency(pp.220–229).
Henderson, P., Hu, J., Romoff, J., Brunskill, E., Juraf- Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S.,
sky, D.,& Pineau, J. (2020). Towards the system- & Floridi, L. (2016). The ethics of algorithms:
atic reporting of the energy and carbon footprints Mapping the debate. Big Data & Society, 3(2),
ofmachinelearning. JournalofMachineLearning 2053951716679679.
Research,21(248), 1–43. Prem, E. (2023). From ethical ai frameworks to tools:
Holstein, K., Wortman Vaughan, J., Daumé III, H., a review of approaches. AI and Ethics, 3(3), 699–
Dudik, M.,&Wallach, H. (2019). Improving fair- 716.
ness in machine learning systems: What do indus- Radclyffe, C., Ribeiro, M., & Wortham, R. H. (2023).
trypractitioners need? InProceedings ofthe2019 Theassessmentlistfortrustworthyartificialintelli-
chiconference onhumanfactors incomputing sys- gence: A review and recommendations. Frontiers
tems(pp.1–16). inartificial intelligence, 6,1020592.
Kaplan, A., & Haenlein, M. (2019). Siri, siri, in my Raji, I. D., & Buolamwini, J. (2019). Actionable audit-
hand: Who’s the fairest in the land? on the inter- ing: Investigating the impact of publicly naming
pretations, illustrations, and implications of artifi- biased performance results of commercial ai prod-
cialintelligence. Businesshorizons,62(1),15–25. ucts. In Proceedings of the 2019 aaai/acm confer-
Khan, A.A.,Badshah, S.,Liang, P.,Waseem, M., Khan, enceonai,ethics,andsociety(pp.429–435).
B., Ahmad, A., ... Akbar, M. A. (2022). Ethics Reddi, V. J., Cheng, C., Kanter, D., Mattson, P.,
of ai: A systematic literature review of principles Schmuelling, G., Wu, C.-J., ... others (2020).
andchallenges. InProceedingsofthe26thinterna- Mlperf inference benchmark. In 2020 acm/ieee
tional conference onevaluation andassessment in 47thannualinternational symposiumoncomputer
softwareengineering (pp.383–392). architecture (isca)(pp.446–459).
Li, P., Liu, Y., Yang, J., & Ren, S. (2024). Towards Ribeiro, M. T., Singh, S., & Guestrin, C. (2016). "
socially andenvironmentally responsible ai. arXiv whyshoulditrustyou?"explainingthepredictions
preprintarXiv:2407.05176. of any classifier. In Proceedings of the 22nd acm
Liu, H., Wang, Y., Fan, W., Liu, X., Li, Y., Jain, S., ... sigkdd international conference on knowledge dis-
Tang, J. (2022). Trustworthy ai: A computational coveryanddatamining(pp.1135–1144).
perspective. ACM Transactions on Intelligent Sys- Strubell, E., Ganesh, A., & McCallum, A. (2020). En-
temsandTechnology, 14(1), 1–59. ergy and policy considerations for modern deep
Lu, Q., Zhu, L., Xu, X., Whittle, J., Zowghi, D., & learning research. In Proceedings of the aaai
Jacquet, A. (2024). Responsible ai pattern cata- conference on artificial intelligence (Vol. 34, pp.
logue: A collection of best practices for ai gover- 13693–13696).
nance and engineering. ACM Computing Surveys, Tschand, A., Rajan, A. T. R., Idgunji, S., Ghosh, A.,
56(7),1–35. Holleman,J.,Kiraly,C.,... others (2024). Mlperf
8

power: Benchmarking the energy efficiency of
machine learning systems from microwatts to
megawatts for sustainable ai. arXiv preprint
arXiv:2410.12032.
Varshney,K.R.,&Alemzadeh,H. (2017). Onthesafety
of machine learning: Cyber-physical systems, de-
cision sciences, and data products. Big data, 5(3),
246–255.
Wörsdörfer, M. (2023). The eu’s artificial intelligence
act: an ordoliberal assessment. AI and Ethics, 1–
16.
9