Polyglot Teachers: Evaluating Language Models for Multilingual
|     |                      |     | Synthetic |     | Data Generation |              |     |     |     |     |
| --- | -------------------- | --- | --------- | --- | --------------- | ------------ | --- | --- | --- | --- |
|     | LesterJamesV.Miranda |     |           |     | IvanVulic´      | AnnaKorhonen |     |     |     |     |
LanguageTechnologyLab,UniversityofCambridge
ljvm2@cam.ac.uk
Collection ljvmiranda921/polyglot-teachers Code ljvmiranda921/polyglot-teachers
Abstract
pairsofuserpromptsandacorrespondingresponse,
whichisoftenscarceforless-resourcedlanguages
6202 rpA 31  ]LC.sc[  1v09211.4062:viXra Synthesizingsupervisedfinetuning(SFT)data
|     |     |     |     |     | (Kunchukuttan | et  | al., 2025). | Generating |     | prompt- |
| --- | --- | --- | --- | --- | ------------- | --- | ----------- | ---------- | --- | ------- |
fromlanguagemodels(LMs)toteachsmaller
|     |     |     |     |     | response | pairs for | these languages |     | demands | sub- |
| --- | --- | --- | --- | --- | -------- | --------- | --------------- | --- | ------- | ---- |
modelsmultilingualtaskshasbecomeincreas-
stantialhumaneffort(Singhetal.,2024;Kapania
| ingly common. | However,         | teacher   | model      | se- |                |          |              |     |     |           |
| ------------- | ---------------- | --------- | ---------- | --- | -------------- | -------- | ------------ | --- | --- | --------- |
|               |                  |           |            |     | et al., 2025), | creating | a bottleneck |     | for | language- |
| lection       | is often ad hoc, | typically | defaulting |     |                |          |              |     |     |           |
to the largest available option, even though specificmodeldevelopment.
such models may have significant capability To alleviate the challenge of human effort and
gapsinnon-Englishlanguages. Thispractice datascarcity,syntheticdatagenerationusingLMs
| can result | in poor-quality | synthetic | data | and |            |          |      |           |     |              |
| ---------- | --------------- | --------- | ---- | --- | ---------- | -------- | ---- | --------- | --- | ------------ |
|            |                 |           |      |     | has gained | traction | as a | promising |     | solution for |
suboptimalstudentdownstreamperformance.
multilingualLMdevelopment(Cahyawijayaetal.,
| In this work, | we systematically |              | characterize |          |          |               |              |     |               |            |
| ------------- | ----------------- | ------------ | ------------ | -------- | -------- | ------------- | ------------ | --- | ------------- | ---------- |
|               |                   |              |              |          | 2024; Ng | et al., 2025; | Martins      |     | et al.,       | 2025; Ham- |
| what makes    | an effective      | multilingual |              | teacher. |          |               |              |     |               |            |
|               |                   |              |              |          | moud et  | al., 2026,    | inter alia). |     | This approach | in-        |
| We measure    | intrinsic         | measures     | of data      | qual-    |          |               |              |     |               |            |
itywithextrinsicstudentmodelperformance volvesleveragingatypicallylargerteachermodel
in a metric we call POLYGLOT SCORE; eval- togeneratetrainingexamples,whicharethenused
uating10LMsacross6typologicallydiverse tofinetuneasmallerstudentmodeltoreplicatethe
languages,generatingover1.4MSFTexamples knowledge of the teacher (Kim and Rush, 2016).
| andtraining240studentmodels. |     |     | Amongthe |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
However,existingworksoftenselectteachermod-
modelstested,Gemma327BandAyaExpanse
elsarbitrarily,defaultingtothelargeststate-of-the-
32Bemergeasconsistentlyeffectiveteachers
|                  |         |      |       |           | art models                            | that excel | on  | benchmarks |     | (Xu et al., |
| ---------------- | ------- | ---- | ----- | --------- | ------------------------------------- | ---------- | --- | ---------- | --- | ----------- |
| across different | student | base | model | families. |                                       |            |     |            |     |             |
|                  |         |      |       |           | 2025b;Lietal.,2025;Zhangetal.,2025a). |            |     |            |     | This        |
Furtheranalysesrevealthatmodelscalealone
doesnotsignificantlypredictteachereffective- practiceisproblematicbecausethesemodels,de-
ness; instead, data qualities such as prompt spitestrongperformance,mayhavesignificantca-
diversity,length,andresponsefluencycapture pability gaps in non-English languages, leading
over93.3%ofvarianceinintrinsicdataquality
topoor-qualitysyntheticdatathatpropagatesthe
| andpredictstudentperformance. |     |     | Finally,we |     |                                            |     |     |     |     |     |
| ----------------------------- | --- | --- | ---------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
|                               |     |     |            |     | teacher’sweaknessesratherthanitsstrengths. |     |     |     |     | And |
providepracticalrecommendations,including
|     |     |     |     |     | soweask: | “whatmakesaneffectivemultilingual |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --------------------------------- | --- | --- | --- | --- |
matchingthemodelfamiliesofteacher-student
teacherforsyntheticdatageneration,andhowcan
pairsandtranslatingfromorrespondingtoex-
wesystematicallymeasureit?”
istingprompts,whichcanyieldimprovements
forless-resourcedlanguages. Wehopethatour Inthiswork,weconductacomprehensiveanal-
workadvancesdata-centricresearchinmulti- ysisof10LMsacross6typologicallydiverselan-
lingualsyntheticdataandLMdevelopment.
guagesonthreecommonsyntheticdatageneration
|     |     |     |     |     | methods: | responding | to  | a user | query | or instruc- |
| --- | --- | --- | --- | --- | -------- | ---------- | --- | ------ | ----- | ----------- |
tion,translatingpromptsfromEnglishtoatarget
1 Introduction
|     |     |     |     |     | language, | and generating |     | prompt-response |     | pairs |
| --- | --- | --- | --- | --- | --------- | -------------- | --- | --------------- | --- | ----- |
Supervisedfinetuning(SFT,Ouyangetal.,2022) given in-context examples (§2.2). To systemati-
has emerged as a standard approach for adapting callyassessteachermodeleffectiveness,weeval-
languagemodels(LMs)tospecifictargetlanguages uateLMsusingbothintrinsicmeasuresofdata
quality(§2.2,i.e.,thediversityofpromptsandre-
(Zhangetal.,2025b;Aryabumietal.,2024,inter
alia). Central to the success of SFT is the avail- sponses, the perplexity of the base model on the
abilityofhigh-qualitytrainingdata,consistingof response, and response quality based on a multi-
1

|     |     | = Multilingual
 | + Student Model
 |     | Multilingual Data Quality |     |     |
| --- | --- | ---------------- | ----------------- | --- | ------------------------- | --- | --- |
Polyglot Score
|     |     | Data Quality | Performance |     |     |     |     |
| --- | --- | ------------ | ----------- | --- | --- | --- | --- |
Diversity of prompts and responses
Seed
Perplexity of the base model
Multilingual LLM-as-a-judge score
SFT
Student Model Performance
Synthetic

|           | Data Generation |                 |     |           | Cultural and Factual Knowledge |              |     |
| --------- | --------------- | --------------- | --- | --------- | ------------------------------ | ------------ | --- |
| Teacher
 |                 | Synthetic
     |     | Student
 |                                |              |     |
|           | Generate        | Respond Dataset |     | Model     |                                |              |     |
| Model     |                 |                 |     |           |                                | General Chat |     |
Translate
Mathematical Reasoning
Base Model
Figure 1: Overview of our method for evaluating language models as multilingual teachers (POLYGLOT
SCORE). Weevaluateteachermodelsontheirsyntheticdatagenerationcapabilitiesacrossthreemethods: Generate
aprompt-responsepairgivenfew-shotexamples,TranslatepromptsfromEnglishandgeneratearesponse,and
Respondtoapromptinthetargetlanguage. ThePOLYGLOTSCOREincorporatesbothintrinsicdataqualitymetrics
andextrinsicstudentmodelperformancetoassesstheeffectivenessofateachermodelforatargetlanguage.
extrinsicmeasure
lingualreward model)andan themodelfamiliesoftheteacherandstudentis
of student model performance on multilingual areliableheuristicforchoosingateachermodel
tasks(§2.3,culturalunderstanding,mathematical (§3.2), and generating responses to existing
reasoning,generalchat). Weaggregatethesemea- prompts or translating from English can yield
surements into a single metric called POLYGLOT substantialimprovementsonless-resourcedlan-
SCORE(PG-SCORE),inordertoprovideaholistic guagescomparedtoarandommixofdatagen-
assessment of a teacher model’s data generation erationmethods,thoughgainsvarybyteacher
model(§3.3).1
| capabilities. | Ourcontributionsareasfollows: |     |     |     |     |     |     |
| ------------- | ----------------------------- | --- | --- | --- | --- | --- | --- |
• Weclosetheevaluationgapbyevaluating10 Wehopethatthisworkpavesthewayfordevel-
|     |     |     | oping | inclusive | and equitable | language | technolo- |
| --- | --- | --- | ----- | --------- | ------------- | -------- | --------- |
teachermodels,generatingover1.4MSFTex-
amplesandfinetuning240studentmodelsfrom gies through quality and cost-effective data. We
OLMo37B.WefindthatGemma327Bcon- releaseourcode,data,andmodelstodriveresearch
inmultilingualsyntheticdatageneration.
| sistentlyrankswithinthetopthreehighest |     |     | PG- |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
SCOREandthattheGemma3modelfamilyout-
|     |     |     | 2   | EvaluatingLanguageModelsas |     |     |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | --- |
performsotherfamiliessuchasLlama3.1and
MultilingualTeachers
| IBMGranite(§3.1). |     | OurPG-SCORErankings |     |     |     |     |     |
| ----------------- | --- | ------------------- | --- | --- | --- | --- | --- |
areconsistentacrossotherbasemodelfamilies The POLYGLOT SCORE (Figure 1) of a teacher
(Llama3.18B,Qwen38B,Gemma34B,§3.2).
|     |     |     | modelT | foratargetlanguageℓisbasedonthe(1) |     |     |     |
| --- | --- | --- | ------ | ---------------------------------- | --- | --- | --- |
• Weprovideanalysesandinsightsonthechar-
intrinsicqualityofthesyntheticdatageneratedby
acteristicsofagoodmultilingualteachermodel. theteacher(§2.2)andthe(2)extrinsicperformance
Ouranalysesrevealthatmodelscaleandbench-
|     |     |     | ofastudentmodelS |     | finetunedonthisdata(§2.3). |     |     |
| --- | --- | --- | ---------------- | --- | -------------------------- | --- | --- |
markperformance,whicharecommonassump-
|     |     |     | 2.1 | Creatingtheseeddataset |     |     |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | --- |
tionsofa“strong”model,donotsignificantly
predictteachereffectiveness(§4.1). Instead,we In order to bootstrap the synthetic data gener-
findthatqualitiesofthegenerateddata,namely
|     |     |     | ation | process, | we create | a seed dataset | seed,ℓ |
| --- | --- | --- | ----- | -------- | --------- | -------------- | ------ |
D
prompt diversity and length coupled with flu- for each target language ℓ. We create
seed,ℓ
D
entanddiverseresponses,captureover93.3% by aggregating publicly available multilingual
ofthevarianceinintrinsicdataqualitymetrics,
instruction-tuningdatasets,includingtheAyaCol-
andtheirprincipalcomponentspredictstudent
|     |     |     | lection | (Aryabumi | et al., | 2024), WildChat | 4.8-M |
| --- | --- | --- | ------- | --------- | ------- | --------------- | ----- |
performancewithR2=0.664(§4.2).
(Zhaoetal.,2024),EuroBlocks-SFT(Martinsetal.,
|         |                    | recommend | a   |     |     |     |     |
| ------- | ------------------ | --------- | --- | --- | --- | --- | --- |
| • Based | on these findings, | we        |     |     |     |     |     |
1Asasupplementary,weshowthatourrecipeimproves
| recipe | (§5) for generating | multilingual | syn- |     |     |     |     |
| ------ | ------------------- | ------------ | ---- | --- | --- | --- | --- |
performanceonaheld-outlanguage(Tagalog)onalanguage-
theticdata. Forexample,wefindthatmatching specificbenchmark(AppendixI).
2

2025),andMagpie-Align(Xuetal.,2025a). Inor- (Pombaletal.,2025)asanLMjudgetoscore
der to simulate scenarios where English prompts the quality of the prompt-response pair (Fig-
are translated into a target language, we also in- ure13). WechooseM-Prometheusbecauseof
cludeexamplesfromTülu3SFT(Lambertetal., itshighperformanceonhuman-alignedevalu-
2025),Helpsteer3(chosenresponses,Wangetal., ation benchmarks, suggesting that the reward
2025),andGSM8K(trainsplit,Cobbeetal.,2021). modelalignswellwithnativespeakers.
DetailedseeddatasetstatisticsinAppendixB. We combine these intrinsic metrics by scaling
eachmetricusingz-scorenormalizationandaver-
2.2 MultilingualDataQuality&Diversity
agingthemasshowninEquation1.
| Synthetic |     | data generation |     | Given | a   | teacher |     |     |     | 1   |     |     |     |
| --------- | --- | --------------- | --- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
|                                           |     |     |     |     |     |     | Intrinsic |     | =   |     | z-score(m( |     | ))  |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ---------- | --- | --- |
| modelT,targetlanguageℓ,andaseeddatasetfor |     |     |     |     |     |     |           | T,ℓ |     | M   |            | D   | T,ℓ |
(1)
| language | ℓ,  | , we | distill | a synthetic |     | dataset |     |     | |   | | m∈M |     |     |     |
| -------- | --- | ---- | ------- | ----------- | --- | ------- | --- | --- | --- | ----- | --- | --- | --- |
seed,ℓ
D
= (x ,y ) N consisting of N prompt- whereM = d x ,d y , log(1+PPL),R
| T,ℓ             |     | i i i=1   |                          |     |     |     |     |                         | {   |     | −   |     | }   |
| --------------- | --- | --------- | ------------------------ | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
| D               | {   | }         |                          |     |     |     |     |                         |     |     |     |     |     |
| responsepairs(x |     | i ,y i ). | Weconsiderthreesynthetic |     |     |     |     |                         |     |     |     |     |     |
|                 |     |           |                          |     |     |     | 2.3 | StudentModelPerformance |     |     |     |     |     |
datagenerationmethodsfoundinliterature:
Weperformsupervisedfinetuningofabasemodel
| • Generate: |          | wesamplek   | prompt-responsepairs |          |             |       |                         |     |         |             |                  |      |             |
| ----------- | -------- | ----------- | -------------------- | -------- | ----------- | ----- | ----------------------- | --- | ------- | ----------- | ---------------- | ---- | ----------- |
|             |          |             |                      |          |             |       | S onthesyntheticdataset |     |         |             | toobtainastudent |      |             |
| from        |          | as few-shot |                      | examples | and         | use T | ϕ                       |     |         |             | T,ℓ              |      |             |
|             |          | seed,ℓ      |                      |          |             |       |                         |     |         |             | D                |      |             |
|             | D        |             |                      |          |             |       | model                   | S   | . Then, | we evaluate |                  | on   | a suite of  |
| to          | generate | a new       | pair (x              | i ,y i ) | conditioned | on    |                         | T,ℓ |         |             | S                | T,ℓ  |             |
|             |          |             |                      |          |             |       | multilingual            |     | tasks   | to assess   | how              | well | the student |
theseexamples.
|              |     |     |                   |     |     |         | haslearnedfromtheteacher. |     |     |     | Thesetasksinclude: |     |     |
| ------------ | --- | --- | ----------------- | --- | --- | ------- | ------------------------- | --- | --- | --- | ------------------ | --- | --- |
| • Translate: |     | we  | forward-translate |     |     | English |                           |     |     |     |                    |     |     |
• Culturalandfactualunderstanding(CULTURE):
| prompts |     | from | to  | the target | language | ℓ   |     |     |     |     |     |     |     |
| ------- | --- | ---- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
D seed,ℓ
weevaluateonGlobal-MMLULite(Singhetal.,
| to  | obtain | x i , and | use T | to generate | the | corre- |     |     |     |     |     |     |     |
| --- | ------ | --------- | ----- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
spondingresponsey . 2025),containingculturallydiverseandrelevant
i
questionsthatwerelocalizedbynativespeakers
| • Respond: |                        | wetakeapromptx |        | from            |     | and    |                                   |     |      |         |     |          |       |
| ---------- | ---------------------- | -------------- | ------ | --------------- | --- | ------ | --------------------------------- | --- | ---- | ------- | --- | -------- | ----- |
|            |                        |                |        | i               |     | seed,ℓ |                                   |     |      |         |     |          |       |
|            |                        |                |        |                 | D   |        | fromEnglish(Hendrycksetal.,2021). |     |      |         |     |          |       |
| useT       | togeneratetheresponsey |                |        |                 | i . |        |                                   |     |      |         |     |          |       |
|            |                        |                |        |                 |     |        | • General                         |     | chat | (CHAT): | we  | evaluate | on M- |
| We         | provide                | a brief        | review | of multilingual |     | syn-   |                                   |     |      |         |     |          |       |
RewardBench(Gurejaetal.,2025)whichmea-
theticdatagenerationmethodsin§6andasupple-
suresthealignmentofmodelswithhumanpref-
mentarysurveyinAppendixA.
erencesinconversationalsettings.
| Data | quality | and diversity |     | metrics | Synthetic |     |                                |     |     |     |     |            |     |
| ---- | ------- | ------------- | --- | ------- | --------- | --- | ------------------------------ | --- | --- | --- | --- | ---------- | --- |
|      |         |               |     |         |           |     | • Mathematicalreasoning(MATH): |     |     |     |     | weevaluate |     |
dataisvaluablewhenitisbothhigh-qualityanddi- onM-GSM(Shietal.,2023),amultilingualver-
verse(Raventosetal.,2023;Chenetal.,2024;Zhu sionoftheGSM8Kdataset(Cobbeetal.,2021)
| et al., | 2025).2 | To estimate |     | the value | of  | , we |                                            |     |     |     |     |     |     |
| ------- | ------- | ----------- | --- | --------- | --- | ---- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
|         |         |             |     |           |     | T,ℓ  | thatteststhemodel’sabilitytosolvemathemat- |     |     |     |     |     |     |
D
| computeasetoflexicalandmodel-basedmetrics: |     |     |     |     |     |     | icalwordproblems. |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
• Diversity of prompts and responses (d ,d ): InspiredbyKimetal.(2025), wecomputethe
x y
a corpus-level statistic that computes the co- PerformanceGapRecovered(PGR)thatmeasures
| sine | distance | of the | prompt | and | response | em- |                   |     |     |     |                 |     |      |
| ---- | -------- | ------ | ------ | --- | -------- | --- | ----------------- | --- | --- | --- | --------------- | --- | ---- |
|      |          |        |        |     |          |     | theimprovementofS |     |     | T,ℓ | overabasemodelS |     | ϕ on |
beddings. In practice, we use Llama-Embed- abenchmarkbrelativetoareferencemodelS
REF
| Nemotron-8B(Babakhinetal.,2025),thetop- |     |     |     |     |     |     | (Equation2). |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
performingmodelontheMMTEBleaderboard
|                                             |     |     |     |     |     |     |           |     | 1   | (cid:88) | score (S | )   | score (S ) |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | -------- | -------- | --- | ---------- |
| (Enevoldsenetal.,2025),toembedthetexts.     |     |     |     |     |     |     |           |     |     |          | b        | T,ℓ | b ϕ        |
|                                             |     |     |     |     |     |     | Extrinsic | T,ℓ | =   |          |          | −   |            |
|                                             |     |     |     |     |     |     |           |     | B   | score    | (S       | )   | score (S ) |
| • Perplexity(PPL):theperplexityofabasemodel |     |     |     |     |     |     |           |     |     |          | b REF    |     | b ϕ        |
|                                             |     |     |     |     |     |     |           |     | |   | | b∈B    |          | −   |            |
on the response y i conditioned on the prompt whereB = CULTURE,CHAT,MATH
| x              | ,measuringthefluencyandnaturalnessofthe |                              |     |     |     |     |     |     | {   |     |     |     | }   |
| -------------- | --------------------------------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                | i                                       |                              |     |     |     |     |     |     |     |     |     |     | (2) |
| generatedtext. |                                         | Lowerperplexityindicatesmore |     |     |     |     |     |     |     |     |     |     |     |
coherentandlinguisticallynaturalresponses.
|          |     |            |              |     |        |       | 2.4 | Computing |     | POLYGLOT | SCORE |     |     |
| -------- | --- | ---------- | ------------ | --- | ------ | ----- | --- | --------- | --- | -------- | ----- | --- | --- |
| • Reward |     | score of a | multilingual |     | reward | model |     |           |     |          |       |     |     |
(R): the verbalized score (1-5) of a multilin- Toprovidestraightforwardcomparisonsbetween
gualrewardmodelbasedonrubricsrelatingto teachermodels, PG-SCORE reportsasinglescore
thatcombinesbothextrinsicandintrinsicmetrics
fluency,naturalness,andinstruction-following.
| In  | practice, | we prompt |     | M-Prometheus |     | 14B | asshowninEquation3. |     |     |     |     |     |     |
| --- | --------- | --------- | --- | ------------ | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
2Weuse“dataquality”torefertobothaspectshereafter. PG-SCORET,ℓ = z-score(Intr. +Extr. ) (3)
|     |     |     |     |     |     |     |     |     |     |     | T,ℓ |     | T,ℓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3

TeacherModel Average Arabic(ar) Czech(cs) German(de) Spanish(es) Indonesian(id) Japanese(ja)
| Gemma327BInst.   |     | 0.726 |     | 0.145  | 0.360  |     | 1.655 | 1.358 | 0.214  |     | 0.626  |     |
| ---------------- | --- | ----- | --- | ------ | ------ | --- | ----- | ----- | ------ | --- | ------ | --- |
| AyaExpanse32B    |     | 0.706 |     | -0.058 | 0.222  |     | 1.468 | 1.129 | 1.153  |     | 0.320  |     |
| Gemma312BInst.   |     | 0.595 |     | -0.464 | 0.327  |     | 1.756 | 1.228 | 0.151  |     | 0.573  |     |
| CommandA         |     | 0.546 |     | -1.360 | 0.114  |     | 1.673 | 1.102 | 1.063  |     | 0.683  |     |
| Gemma34BInst.    |     | 0.469 |     | -0.488 | 0.330  |     | 1.644 | 0.929 | -0.105 |     | 0.504  |     |
| GPT4omini        |     | 0.461 |     | -1.117 | 0.015  |     | 1.766 | 0.908 | 1.003  |     | 0.189  |     |
| IBMGranite4.0    |     | 0.312 |     | -0.072 | -0.031 |     | 1.000 | 0.734 | -0.079 |     | 0.321  |     |
| IBMGraniteMicro  |     | 0.304 |     | -0.282 | 0.290  |     | 1.102 | 0.783 | -0.329 |     | 0.264  |     |
| Llama3.170BInst. |     | 0.140 |     | -0.964 | 0.109  |     | 1.195 | 0.688 | 0.182  |     | -0.373 |     |
Llama3.18BInst. -0.356 -1.693 -0.974 0.891 0.182 0.322 -0.863
TopmodelswiththehighestPG-SCORE(averageacrosssixlanguages).
| Table1: |     |     |     |     |     |     |     |     | Weevaluateteachermodels |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
withvaryingsizeandmodelfamilyon6typologically-diverselanguages. Foreachlanguage,wehighlightthebest
modelinboldandthesecond-bestmodelwithanunderline. DetailedresultswithstandarderrorsareinTable13.
We combine both intrinsic and extrinsic met- Then,wefinetuneapretrainedOLMo37Bmodel
ricsbecausetheycapturecomplementaryaspects (OLMoTeametal.,2025)oneach T,ℓ toobtain
D
of teacher quality. Extrinsic metrics alone may S . AppendixE.1describesSFTinformation.
T,ℓ
| overlook | the quality | of  | synthetic | data | that | propa- |     |     |     |     |     |     |
| -------- | ----------- | --- | --------- | ---- | ---- | ------ | --- | --- | --- | --- | --- | --- |
TeacherModels
WeincludeLlama3.1(8B,70B,
| gates through | the | ecosystem, |     | while | intrinsic | met- |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ----- | --------- | ---- | --- | --- | --- | --- | --- | --- |
Grattafiorietal.,2024),Gemma3(4B,12B,27B,
ricsalonedonotguaranteethatthestudentmodel
GemmaTeametal.,2025),CommandA(Cohere
| achievesstrongdownstreamperformance. |     |     |     |     |     | There- |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Teametal.,2025),AyaExpanse32B(Dangetal.,
sultingPG-SCOREisz-scorenormalized,where0
2024),andIBMGranite(4.0,Micro,GraniteTeam,
indicatesaverageteachereffectiveness,andhigher
|                 |     |        |           |      |         |     | IBM, 2025). | In addition, |     | we also | include | GPT |
| --------------- | --- | ------ | --------- | ---- | ------- | --- | ----------- | ------------ | --- | ------- | ------- | --- |
| scores indicate |     | better | synthetic | data | quality | and |             |              |     |         |         |     |
4omini(OpenAIetal.,2024)asarepresentative
| studentperformanceforthatlanguage. |     |     |             |     | Weadopt |      |                     |     |                      |     |     |     |
| ---------------------------------- | --- | --- | ----------- | --- | ------- | ---- | ------------------- | --- | -------------------- | --- | --- | --- |
|                                    |     |     |             |     |         |      | closed-sourcemodel. |     | SeeTable7inAppendixD |     |     |     |
| equal weighting                    |     | as  | a baseline; | we  | show    | that |                     |     |                      |     |     |     |
fordetailedmodelinformation.
teacherrankingsarerobusttoalternativeweighting
schemesinAppendixG.4. TargetLanguages Weselect6typologicallydi-
|                |     |                  |     |     |     |     | verselanguages: | Arabic(ar),Czech(cs),German |     |       |     |          |
| -------------- | --- | ---------------- | --- | --- | --- | --- | --------------- | --------------------------- | --- | ----- | --- | -------- |
| 3 Experiments: |     | EvaluatingLMsand |     |     |     |     |                 |                             |     |       |     |          |
|                |     |                  |     |     |     |     | (de), Spanish   | (es), Indonesian            |     | (id), | and | Japanese |
PG-SCORE Generalization (ja). Theselanguagesarechosenduetotheirvaria-
|                            |     |     |     |          |     |       | tioninresourceavailability,script,andfamily. |     |     |     |     | This |
| -------------------------- | --- | --- | --- | -------- | --- | ----- | -------------------------------------------- | --- | --- | --- | --- | ---- |
| Inthissection,wemeasurethe |     |     |     | POLYGLOT |     | SCORE |                                              |     |     |     |     |      |
languagechoiceisalsosupportedbypriorworkon
| of state-of-the-art |     | LMs | (§3.1). | Then, |     | we test |     |     |     |     |     |     |
| ------------------- | --- | --- | ------- | ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
informedsampling(Ploegeretal.,2026)thatcon-
| whether | our findings |     | are consistent |     | across | other |     |     |     |     |     |     |
| ------- | ------------ | --- | -------------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- |
siderstypologicalvarietyofthechosenlanguages.
| basemodels(§3.2). |     | Finally,wedetermineifacer- |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
SeeTable8inAppendixDforlanguagestatistics.
| tain data | generation | method |     | is more | effective | in  |     |     |     |     |     |     |
| --------- | ---------- | ------ | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
multilingualsettings(§3.3). Weconductadditional Results Table 1 shows the PG-SCORE of each
experimentsandablationsinAppendixG. teacher model across all target languages. The
resultssuggestthefollowing:
3.1 WhichState-of-the-ArtLMsAreGood
|     |     |     |     |     |     |     | • Gemma | 3 27B and | Aya | Expanse |     | 32B are |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------- | --- | ------- |
MultilingualTeachers?
|     |     |     |     |     |     |     | the | most effective | teachers. |     | Gemma | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | ----- | --- |
Setup
In order to evaluate the effectiveness of 27B achieves the highest average PG-SCORE
differentLMsasmultilingualteachers, weselect (0.726),followedcloselybyAyaExpanse32B
10 state-of-the-art models that vary in scale, ar- (0.706),bothoutperforminglargermodelslike
chitecture, and training data, then evaluate them Llama 3.1 70B Inst. (0.140), suggesting that
on 6 typologically diverse languages by generat- modelscalealonedoesnotdetermineteacheref-
ing10.5kprompt-responsepairsforeachteacher- fectiveness. WealsoobservethattheGemma3
language pair where each data generation (§2.2) familydominatesthetopranks,whiletheLlama
methodisequallyrepresented. Werepeatthedata 3.1familyunderperformsonmostlanguages.
generationprocessthreetimeswithdifferentran- • Smaller LMs can be effective multilingual
domseedstoaccountforvariabilityinLMoutputs. teachers. Gemma312B(0.595)and4B(0.469)
4

|     |     |     |     |     |     |     |     |     |     | B   | 4 B | B   | B    |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|     |     |     |     |     |     |     |     |     |     | 3 7 | 3   | 8   | 8    |
|     |     |     |     |     |     |     |     |     |     | Mo  | ma  | 3   | ma 3 |
m wen
|                  |     |         |          | BaseModel(S | ϕ)      |          |       |          |      | O L Ge | Q    | Lla  |     |
| ---------------- | --- | ------- | -------- | ----------- | ------- | -------- | ----- | -------- | ---- | ------ | ---- | ---- | --- |
| TeacherModel     |     | OLMo37B | Gemma34B |             | Qwen38B | Llama38B |       |          |      |        |      |      |     |
|                  |     |         |          |             |         |          |       | Llama38B | 0.63 | 0.68*  | 0.57 | 1.00 |     |
| GPT4omini        |     | 0.551   |          | 1.022       | 1.005   |          | 0.621 |          |      |        |      |      |     |
| Llama3.170BInst. |     | 0.138   |          | 0.338       | 1.039   |          | 0.497 |          |      |        |      |      |     |
Llama3.18BInst. −0.160 −0.133 0.365 0.048 Qwen38B 0.60 0.65 1.00
| CommandA       |     | 0.459 |     | 0.725 | 0.974 |     | 0.737 |          |        |      |     |     |     |
| -------------- | --- | ----- | --- | ----- | ----- | --- | ----- | -------- | ------ | ---- | --- | --- | --- |
| AyaExpanse32B  |     | 0.854 |     | 0.762 | 1.183 |     | 0.793 |          |        |      |     |     |     |
| Gemma327BInst. |     | 0.672 |     | 0.810 | 1.301 |     | 0.800 | Gemma34B | 0.87** | 1.00 |     |     |     |
**:p<0.01
| Gemma312BInst.  |     | 0.481 |     | 0.666 | 1.393 |        | 0.804 |         |      |     | *:p<0.05 |     |     |
| --------------- | --- | ----- | --- | ----- | ----- | ------ | ----- | ------- | ---- | --- | -------- | --- | --- |
| Gemma34BInst.   |     | 0.350 |     | 0.712 | 0.545 |        | 1.062 |         |      |     |          |     |     |
|                 |     |       |     |       |       |        |       | OLMo37B | 1.00 |     |          |     |     |
| IBMGranite4.0   |     | 0.283 |     | 0.278 | 0.831 | −0.001 |       |         |      |     |          |     |     |
| IBMGraniteMicro |     | 0.164 |     | 0.455 | 1.079 |        | 0.396 |         |      |     |          |     |     |
PG-SCOREacrossdifferentbasemodels(averageacrossArabic,German,andIndonesian). Left:
Figure2:
AveragePG-SCOREofeachteachermodelonstudentsfinetunedonthreedifferentbasemodels. Wehighlightthe
top, second,and third bestteachermodelsforeachsetting. Right: HeatmapshowingSpearmanrankcorrelation
ρofteachermodelrankingsacrossbasemodels. WeshowpercentageincreasesinPG-SCOREonTable14.
|     |     |     | Arabic(ar) |     |     | German(de) |     |     |     | Indonesian(id) |     |     |     |
| --- | --- | --- | ---------- | --- | --- | ---------- | --- | --- | --- | -------------- | --- | --- | --- |
TeacherModel Generate Translate Respond Generate Translate Respond Generate Translate Respond
Gemma327BInst. 0.032 0.276 0.802 2.140 2.086 1.212 1.189 1.196 0.046
|               |     | −0.276 |     | 0.148 | −1.349 | 1.473 |       |     |       |       |       |     | 1.606 |
| ------------- | --- | ------ | --- | ----- | ------ | ----- | ----- | --- | ----- | ----- | ----- | --- | ----- |
| AyaExpanse32B |     |        |     |       |        |       | 1.255 |     | 1.451 | 0.039 | 0.733 |     |       |
Llama3.170BInst. −0.867 −1.025 −0.215 1.391 0.459 1.187 −0.146 0.089 0.155
Table2: PG-SCOREacrossthreedatagenerationmethods: Generate,Translate,andRespond(§2.2). For
eachdatagenerationmethod,wegenerate10ksamplesperteacher-languagepairandfinetuneastudentmodelon
OLMo37B.WeshowpercentageincreasesinPG-SCOREcomparedtoabaseline(equalrepresentationofthethree
datagenerationmethods)onTable15.
rankamongthetop-5teachers,whiletheLlama Results Figure2showstheaveragePG-SCORE
3.1 70B Inst. (0.140) ranks ninth, suggesting of each teacher model across different base mod-
that smaller LMs can match or exceed larger elswhileTable14showsthepercentageincrease
LMsindatagenerationcapabilities. offamily-matchedteacher-studentpairscompared
Teacherperformancevariessignificantlyby
| •   |     |     |     |     |     | to  | the OLMo | 3   | 7B (mismatch) |     | baseline. |     | We ob- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------- | --- | --------- | --- | ------ |
language. German and Spanish consistently servethatthebestteachermodelsremainconsis-
showthehighestscoresacrossallmodels,while tentacrossdifferentstudentbasemodels,with
Arabic proves challenging with most teach- Gemma327BandAyaExpanse32Bconsistently
ers yielding negative scores, suggesting that ranking among the top three teachers. Further-
language-specific factors influence teacher ef- more, the Gemma 3 family continues to outper-
fectiveness. Wehypothesizethatalanguage’s form other model families. In addition, we find
resourcestatusorpresenceinpretrainingdata that the model rankings vary slightly depending
maycontributetothisvariability(§G.5). on the base model used, as Spearman rank corre-
|                      |     |     |                |     |     | lation    | ranges                              | from | ρ=0.57 | (moderate) |     | to  | ρ=0.87 |
| -------------------- | --- | --- | -------------- | --- | --- | --------- | ----------------------------------- | ---- | ------ | ---------- | --- | --- | ------ |
| 3.2 Generalizationof |     |     | PG-SCOREAcross |     |     |           |                                     |      |        |            |     |     |        |
|                      |     |     |                |     |     | (strong). | Wehypothesizethatthisvariationmaybe |      |        |            |     |     |        |
DifferentBaseModels due to differences in architecture and pretraining
|     |     |     |     |     |     | databetweenbasemodels. |     |     |     | Despitethisvariation, |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --------------------- | --- | --- | --- |
Setup InsteadofusingOLMo37Basthebase
|          |         |         |             |     |     | we        | observe | that | teacher-student |           | model |           | family |
| -------- | ------- | ------- | ----------- | --- | --- | --------- | ------- | ---- | --------------- | --------- | ----- | --------- | ------ |
| model (S | ϕ ) for | student | finetuning, | we  | use | (1)       |         |      |                 |           |       |           |        |
|          |         |         |             |     |     | alignment |         | is a | reliable        | heuristic | for   | achieving |        |
Llama3.18B,(2)Gemma34BPT,and(3)Qwen
|                          |     |     |     |              |     | goodPG-SCORE. |     |     | Forexample,Gemma3teach- |     |     |     |     |
| ------------------------ | --- | --- | --- | ------------ | --- | ------------- | --- | --- | ----------------------- | --- | --- | --- | --- |
| 38BBase(Yangetal.,2025). |     |     |     | WerecomputeS |     | -             |     |     |                         |     |     |     |     |
ϕ
|     |     |     |     |     |     | ers | consistently |     | perform | well | with Gemma |     | 3 stu- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | ---- | ---------- | --- | ------ |
dependentmetricssuchasperplexityandPGR.To
|     |     |     |     |     |     | dent | bases, | with | family-matched |     | pairs | achieving |     |
| --- | --- | --- | --- | --- | --- | ---- | ------ | ---- | -------------- | --- | ----- | --------- | --- |
reducecomputationalcosts,wefocusonthreelan-
|                           |        |       |            |            |     | at least | +20.5% |           | higher | PG-SCORE |      | compared | to     |
| ------------------------- | ------ | ----- | ---------- | ---------- | --- | -------- | ------ | --------- | ------ | -------- | ---- | -------- | ------ |
| guages:                   | German | (high | PG-SCORE), | Indonesian |     |          |        |           |        |          |      |          |        |
|                           |        |       |            |            |     | the      | worst  | pair (see | Table  | 14).     | This | finding  | is in- |
| (mid-range),andArabic(low |        |       | PG-SCORE). |            |     |          |        |           |        |          |      |          |        |
5

teresting but reasonable given that models from PC VarianceExpl. Cumulative
| the same | family | likely | share | similar | tokenization |     |     |     |     |       |     |       |     |
| -------- | ------ | ------ | ----- | ------- | ------------ | --- | --- | --- | --- | ----- | --- | ----- | --- |
|          |        |        |       |         |              |     |     | PC1 |     | 42.2% |     | 42.2% |     |
schemes,leadingtoeasiertransferfromteacherto
|     |     |     |     |     |     |     |     | PC2 |     | 22.1% |     | 64.3% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
student. Inaddition,family-matchingisnotahard
|     |     |     |     |     |     |     |     | PC3 |     | 16.5% |     | 80.8% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
constraintunlikeinotherdistillationsettings(on-
|     |     |     |     |     |     |     |     | PC4 |     | 12.6% |     | 93.3% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- |
policy,Agarwaletal.,2024;Boizardetal.,2025),
|     |     |     |     |     |     |     |     | PC5 |     |     | 3.5% | 96.8% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- |
butitremainsareliableheuristicforteacherselec-
|                                     |     |     |          |      |        |        |     | PC6 |     |     | 3.2% | 100.0% |     |
| ----------------------------------- | --- | --- | -------- | ---- | ------ | ------ | --- | --- | --- | --- | ---- | ------ | --- |
| tionwhentheoptimalteacherisunknown. |     |     |          |      |        | Forour |     |     |     |     |      |        |     |
| core experiment,                    |     | we  | use OLMo | 3 7B | as the | base   |     |     |     |     |      |        |     |
Table4:Varianceexplainedbyprincipalcomponents
modelforfinetuningtocontroltheeffectofmodel
|     |     |     |     |     |     |     | from | intrinsic | data | quality | metrics. | There | are four |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ---- | ------- | -------- | ----- | -------- |
familyalignmentwhenevaluatingteacherquality.
principalcomponentsthatexplainover93.3%(cumula-
tive)ofthevariance.
3.3 EffectofSyntheticDataGeneration
| Methodon |     | PG-SCORE |     |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Setup Inordertodetermineifadatageneration have an impact on teacher effectiveness. In our
method is more effective than others, we gener- core experiment, we sample an equal mix of all
|     |     |     |     |     |     |     | three | methods | (3.5k | each) | to control |     | their effect |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | ----- | ----- | ---------- | --- | ------------ |
ate10kprompt-responsepairsforeachmethodin
whenevaluatingteachermodelquality.
| §2.2andcomparethePG-SCOREofeachmix. |     |     |     |     |     | We  |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recomputeintrinsicdataqualitymetricsandfine-
|           |     |         |        |           |       |     | 4   | Analysis: | WhatMakesaGoodPolyglot |     |     |     |     |
| --------- | --- | ------- | ------ | --------- | ----- | --- | --- | --------- | ---------------------- | --- | --- | --- | --- |
| tune OLMo |     | 3 7B to | obtain | a student | model | and |     |           |                        |     |     |     |     |
Teacher?
| evaluate | the | teacher’s | PG-SCORE. |     | We also | com- |     |     |     |     |     |     |     |
| -------- | --- | --------- | --------- | --- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
pareeachmixagainstabaselineconsistingof10k
Weinvestigatethefactorsthatcontributetoeffec-
| instances | with | roughly      | equal | number    | of       | samples |                                           |              |     |           |          |     |           |
| --------- | ---- | ------------ | ----- | --------- | -------- | ------- | ----------------------------------------- | ------------ | --- | --------- | -------- | --- | --------- |
|           |      |              |       |           |          |         | tive                                      | multilingual |     | teachers. | We start | by  | analyzing |
| ( 3.3k)   | from | each method. |       | To reduce | computa- |         |                                           |              |     |           |          |     |           |
| ≈         |      |              |       |           |          |         | commonassumptionsaboutteachermodelperfor- |              |     |           |          |     |           |
tionalcosts,weconductthisexperimentonthree
mance,suchassizeandbenchmarkscores(§4.1),
| representative |     | teachers | (Gemma | 3   | 27B, | Aya Ex- |      |           |     |       |           |         |            |
| -------------- | --- | -------- | ------ | --- | ---- | ------- | ---- | --------- | --- | ----- | --------- | ------- | ---------- |
|                |     |          |        |     |      |         | then | determine |     | which | intrinsic | factors | drive stu- |
panse32B,andLlama3.170B)spanninghighto
|     |     |     |     |     |     |     | dentperformance(§4.2). |     |     |     | Lastly,weexaminelan- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | -------------------- | --- | --- |
low PG-SCORE,andthreelanguages(German,In-
|     |     |     |     |     |     |     | guage | properties |     | that might | influence |     | a teacher’s |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ---------- | --------- | --- | ----------- |
donesian,Arabic)coveringdiverseresourcelevels.
PG-SCORE(§G.5).
Results
|     | Table | 2 shows | the | PG-SCORE |     | of each |     |                                     |     |     |     |     |     |
| --- | ----- | ------- | --- | -------- | --- | ------- | --- | ----------------------------------- | --- | --- | --- | --- | --- |
|     |       |         |     |          |     |         | 4.1 | Dostrongermodelsmakebetterteachers? |     |     |     |     |     |
datageneration(seeTable15forbaselinecompar-
isons). We observe that for a high-resource lan- Setup In order to determine if there is a rela-
guagelikeGerman,theGeneratemethodyields tionshipbetweenamodel’ssizeorbenchmarkper-
thehighestPG-SCORE,whileforless-resourced formance (i.e., common assumptions to assess a
languages like Arabic and Indonesian, the Re- model’s “strength”) to its effectiveness as a mul-
spondorTranslatemethodsaremoreeffective. tilingualteacher,wefitamixed-effectsmodelre-
WehypothesizethatthisoccursbecausetheGener- gressingPG-SCOREon(a)parametersize(N=27,
atemethoddependsonfew-shotexamplesfromthe 9models,excludingGPT-4o-miniwithunknown
seeddataset,whicharetypicallyofhigherquality size 3trials),and(b)averagemultilingualbench-
×
|                           |     |     |     |                     |     |     | mark | performance |     | on  | Global-MMLU |     | Lite, M- |
| ------------------------- | --- | --- | --- | ------------------- | --- | --- | ---- | ----------- | --- | --- | ----------- | --- | -------- |
| inhigh-resourcelanguages. |     |     |     | Overall,ourfindings |     |     |      |             |     |     |             |     |          |
suggestthatselectingadatagenerationmethodcan GSM, and M-RewardBench (N=180, 10 models
|           |     |     |     |     |     |     |         | 6languages |                                  | 3trials). |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ------- | ---------- | -------------------------------- | --------- | --- | --- | --- |
|           |     |     |     |     |     |     | ×       |            | ×                                |           |     |     |     |
| Predictor |     |     |     | β   | SE  | p   | Results |            | Table3showstheregressionresults. |           |     |     | We  |
observethatneitherparametersizenoraverage
| log(Param. |                   | Size) | 0.053           |     | 0.080      | 0.507 |                                |     |           |     |                  |     |               |
| ---------- | ----------------- | ----- | --------------- | --- | ---------- | ----- | ------------------------------ | --- | --------- | --- | ---------------- | --- | ------------- |
|            |                   |       |                 |     |            |       | multilingual                   |     | benchmark |     | performance      |     | signifi-      |
| Avg.       | MultilingualPerf. |       | 1.387           |     | 2.204      | 0.529 |                                |     |           |     |                  |     |               |
|            |                   |       |                 |     |            |       | cantlypredictPG-SCORE(p>0.05). |     |           |     |                  |     | Specifically, |
|            |                   |       |                 |     |            |       | a1-unitincreaseinlog(Param.    |     |           |     | Size)corresponds |     |               |
| Table      | 3: Results        | from  | a mixed-effects |     | regression |       |                                |     |           |     |                  |     |               |
model on PG-SCORE on an LM’s (a) size and (b) toanon-significant0.053increasein PG-SCORE.
avg. multilingualbenchmarkperformance.
|     |     |     |     |     |     | Thelack | Although |     | this finding |     | confirms | the results | of Xu |
| --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ------------ | --- | -------- | ----------- | ----- |
ofsignificantcorrelationsuggeststhatbothpredictors et al. (2025b) and Kim et al. (2025) for English-
arenotsolelysufficienttoensureteachereffectiveness.
basedtasks,weshowthat“stronger”modelsdonot
6

|     | Distinct |       |       |             |       |        |     | 0.50 |     |     |     |     |     |
| --- | -------- | ----- | ----- | ----------- | ----- | ------ | --- | ---- | --- | --- | --- | --- | --- |
|     | Prompts  | 0.073 | 0.654 | 0.008 0.744 | 0.012 | -0.117 |     |      |     |     |     |     |     |
erocSkramhcneBdetciderP
Distinct
|     |     | 0.579 | -0.098 | -0.017 0.111 | -0.660 | 0.456 |     | 0.45 |     |     |     |     |     |
| --- | --- | ----- | ------ | ------------ | ------ | ----- | --- | ---- | --- | --- | --- | --- | --- |
Responses
|     | Perplexity | -0.578 | -0.037 | 0.017 0.211 | 0.075 | 0.784 |     |     |     |     |     |     |     |
| --- | ---------- | ------ | ------ | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
0.40
RubricScore
|     |     | 0.514 | -0.237 | 0.354 0.182 | 0.678 | 0.247 |     |     |     |     |     |     |     |
| --- | --- | ----- | ------ | ----------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
(M-Prometheus)
Avg.Prompt
0.35
|     | Length | -0.079 | 0.388 | 0.838 -0.332 | -0.171 | 0.048 |     |     |     |     |     |     |     |
| --- | ------ | ------ | ----- | ------------ | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
R2=0.664
Avg.Response
|     |        | -0.234 | -0.596 | 0.415 0.497 | -0.265 | -0.318 |     |      |     |     |     | RMSE=0.440 |     |
| --- | ------ | ------ | ------ | ----------- | ------ | ------ | --- | ---- | --- | --- | --- | ---------- | --- |
|     | Length |        |        |             |        |        |     | 0.30 |     |     |     |            |     |
|     |        |        |        |             |        |        |     |      | 0.3 |     | 0.4 |            | 0.5 |
|     |        | PC1    | PC2    | PC3 PC4     | PC5    | PC6    |     |      |     |     |     |            |     |
ActualBenchmarkScore
|     |     |     |     |     |     |     |     |     |     | Arabic | German  | Indonesian |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ---------- | --- |
|     |     |     | 0.5 | 0.0 | 0.5 |     |     |     |     |        |         |            |     |
|     |     |     | −   |     |     |     |     |     |     | Czech  | Spanish | Japanese   |     |
LoadingStrength
|     |     |     |     |     |     |     | Figure | 4:  | Fit | of a linear | regression | model | on the |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ----------- | ---------- | ----- | ------ |
Figure3:Loadingstrengthofintrinsicmetricsonthe
principalcomponents(PCs). PC1suggeststhatgood PCsoftheintrinsicmetricstopredictstudentper-
teachers produce diverse and high-quality responses, formance. Intrinsic metrics, via their PCs, can pre-
|                                            |     |     |     |     |     |     | dict | extrinsic | student | performance |     | (R2 = | 0.664 and |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---- | --------- | ------- | ----------- | --- | ----- | --------- |
| whilePC2focusesonpromptdiversityandlength. |     |     |     |     |     | PC3 |      |           |         |             |     |       |           |
andPC4,together,indicatestheimportanceofprompts RMSE=0.440)onmultilingualbenchmarks(§2.3).
onstudentperformance.
showsthefitofalinearmodelonthetestsetwhen
necessarilymakebettermultilingualteachers. thePCslearntopredictstudentperformance. We
|     |     |     |     |     |     |     | observe |     | that interactions |     | within | the intrinsic | met- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------------- | --- | ------ | ------------- | ---- |
4.2 Whichintrinsicmetricsdetermine
ricscanpredictextrinsicstudentperformancede-
|     | extrinsicstudentmodelperformance? |     |     |     |     |     |         |     |      | R2  |           |      |          |
| --- | --------------------------------- | --- | --- | --- | --- | --- | ------- | --- | ---- | --- | --------- | ---- | -------- |
|     |                                   |     |     |     |     |     | cently, |     | with | =   | 0.664 and | RMSE | = 0.440. |
Setup Inordertoidentifylatentfactorsfromthe Thisfindingsuggeststhatevenwithasimplelinear
|     |     |     |     |     |     |     | model, |     | our chosen | intrinsic |     | metrics | are predic- |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---------- | --------- | --- | ------- | ----------- |
intrinsicmetricsthatexplainstudentperformance,
we perform principal component analysis (PCA) tiveofstudentperformance. Inpractice,thesein-
ontheintrinsicmetricsdescribedin§2.2. Then,we sightscanhelppractitionersselectteachermodels
basedonintrinsicmetricsalone,whicharecheaper
fitaregressionmodeltopredictextrinsicstudent
performance based on the principal components tocomputethanextrinsicstudentevaluations.
(PCs)obtainedfromPCA:wesplit180datapoints
|     |        |     |           |           |      |     | 5   | Discussion: |     | TowardsaRecipefor |     |     |     |
| --- | ------ | --- | --------- | --------- | ---- | --- | --- | ----------- | --- | ----------------- | --- | --- | --- |
| (10 | models | 6   | languages | 3 trials) | into | 80% |     |             |     |                   |     |     |     |
|     |        | ×   |           | ×         |      |     |     |             |     |                   |     |     |     |
MultilingualSyntheticDataGeneration
| train | and 20% | test, | then | train a linear | regression |     |     |     |     |     |     |     |     |
| ----- | ------- | ----- | ---- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
modelwiththePCsasthefeaturesandthestudent
Ourresultsprovideactionableinsightsforselect-
performanceasthetarget.
|     |     |     |     |     |     |     | ing | and | effectively | using | teacher | models | in mul- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------- | ------ | ------- |
Results Table4showshowmuchofthevariance tilingualsyntheticdatageneration. First, we find
is explained by each principal component while that model scale does not significantly predict
Figure 3 shows the loading strength of each in- teachereffectiveness: Llama3.170BInstruct,de-
trinsic metric on the principal components. We spite being the largest model evaluated, ranks at
observethatthefirstfourPCsexplainover93.3% the bottom half in PG-SCORE across all student
ofthevarianceintheintrinsicdataqualitymetrics. basemodelswetested(§3.1,§3.2). Ouranalyses
Specifically, PC 1 (42.2%) captures characteris- suggestthatwhatmattersinsteadisthequalityof
ticssuchaslowerresponseperplexityandhigh generateddata: promptdiversity,responsefluency,
distinctiveness, PC2 (22.1%) captures variance and length collectively capture over 93% of the
in characteristics such as higher prompt diver- variance in intrinsic data quality and predict stu-
| sity | and length, |     |         |             |     |         | dentperformancewithR2=0.664(§4.2),offering |     |     |     |     |     |     |
| ---- | ----------- | --- | ------- | ----------- | --- | ------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
|      |             |     | whereas | PC3 (16.5%) |     | and PC4 |                                            |     |     |     |     |     |     |
(12.6%)capturevariancethatreinforcetrendson practitioners a cheaper alternative to full student
promptlengthanddiversity. Inaddition,Figure4 trainingrunsforscreeningteachercandidates.
7

Second, whentheoptimalteacherisunknown, multilingualsyntheticdatageneration,distillthem
matchingmodelfamiliesoffersareliableheuris-
|     |     |     |     |     |     |     | into three | strategies, |     | and | test each | in  | isolation. |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --- | --------- | --- | ---------- |
ticforteacherselection. Gemmateacherspaired Thissetupenabledustoprovidepractitionerswith
with Gemma students, and Llama teachers with empirically-grounded recipe on selecting teacher
Llamastudents,outperformamismatchedbaseline LMsthatwehopetobeapplicableacrossanygen-
| by at least | 20% | (Figure | 2). | We hypothesize |     | this | erationmethod. |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | -------------- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- |
findingreflectssharedtokenizationandsimilarpre-
|     |     |     |     |     |     |     | Evaluating | and | Improving |     | the | Synthetic | Data |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | --- | --------- | ---- |
trainingdistributions,thoughdisentanglingthese
|     |     |     |     |     |     |     | Pipeline | While | prior | works | have | evaluated | as- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ----- | ----- | ---- | --------- | --- |
factorsremainsfuturework.
pectsofthesyntheticdatapipeline,theytypically
| Finally,                             | we             | find | that           | there are    | language-   |       |                                |        |               |            |           |                 |         |
| ------------------------------------ | -------------- | ---- | -------------- | ------------ | ----------- | ----- | ------------------------------ | ------ | ------------- | ---------- | --------- | --------------- | ------- |
|                                      |                |      |                |              |             |       | dosoinisolation(i.e.,intrinsic |        |               |            |           | extrinsic)orfo- |         |
| dependent                            | considerations |      |                | for data     | generation. |       |                                |        |               |            | ⊕         |                 |         |
|                                      |                |      |                |              |             |       | cus exclusively                |        | on English    |            | (Zhang    | et al.,         | 2025a). |
| Forhigh-resourcelanguageslikeGerman, |                |      |                |              |             | where |                                |        |               |            |           |                 |         |
|                                      |                |      |                |              |             |       | For instance,                  |        | Kim et        | al. (2025) | evaluated |                 | teacher |
| seed data                            | quality        | is   | high,          | the Generate | method      |       |                                |        |               |            |           |                 |         |
|                                      |                |      |                |              |             |       | models                         | solely | as a function |            | of        | extrinsic       | student |
| performs                             | best.          | For  | less-resourced | languages    |             | like  |                                |        |               |            |           |                 |         |
performanceonEnglishtasks(e.g.,reasoningand
ArabicandIndonesian,methodsthatleverageex-
coding),whileCaietal.(2025)’sOpenDataArena
istingprompts(Respond)ortransferfromEnglish
focusesonintrinsicdataquality(model-basedand
(Translate)canyieldsubstantialgainsoverauni-
|     |     |     |     |     |     |     | heuristic)toscoremodels. |     |     |     | Signalsofmultilingual |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --------------------- | --- | --- |
formmixofmethods,thoughthemagnitudevaries
|            |        |     |     |                    |     |      | data quality | are | often | a function |     | of corpus-level |     |
| ---------- | ------ | --- | --- | ------------------ | --- | ---- | ------------ | --- | ----- | ---------- | --- | --------------- | --- |
| by teacher | (Table | 2). | For | truly low-resource |     | lan- |              |     |       |            |     |                 |     |
diversity(ArtetxeandSchwenk,2019;Enevoldsen
guages,werecommendcombiningsyntheticdata
etal.,2025;Sametal.,2025)andgenerationqual-
generationwithtargeteddatacollection.
ity(Pombaletal.,2025;Anugrahaetal.,2026)On
Asasupplementary,wedemonstratetheapplica-
theotherhand,multilingualLMsaretypicallyeval-
bilityofourfindingsbybuildingamultilingualsyn-
|     |     |     |     |     |     |     | uated on | general-knowledge |     |     | and | culture-specific |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | --- | --- | ---------------- | --- |
theticdatarecipeforaheld-outlanguage,Tagalog,
benchmarks(Qinetal.,2025;GemmaTeametal.,
| inAppendixI. |        | Weshowthatmodelstrainedusing |          |      |           |     |                 |     |     |            |       |        |       |
| ------------ | ------ | ---------------------------- | -------- | ---- | --------- | --- | --------------- | --- | --- | ---------- | ----- | ------ | ----- |
|              |        |                              |          |      |           |     | 2025; Salamanca |     | et  | al., 2026, | inter | alia). | These |
| our recipe   | (based | on                           | analyses | from | PG-SCORE) |     |                 |     |     |            |       |        |       |
practicesinformedourchoiceofintrinsicandex-
| have better | performance |     |          | on an unseen   | Filipino- |     |            |          |            |                           |            |     |          |
| ----------- | ----------- | --- | -------- | -------------- | --------- | --- | ---------- | -------- | ---------- | ------------------------- | ---------- | --- | -------- |
|             |             |     |          |                |           |     | trinsic    | metrics  | throughout |                           | this work. |     | More im- |
| centric     | benchmark,  |     | and that | each component |           | of  |            |          |            |                           |            |     |          |
|             |             |     |          |                |           |     | portantly, | PG-SCORE |            | providesaholisticanalysis |            |     |          |
ourrecommendation(e.g.,choosetopteacherfrom
thatcombinesbothintrinsicdataqualityandextrin-
| Table1,matchmodelfamilies,etc.) |     |     |     | resultedinob- |     |     |             |            |     |             |     |     |          |
| ------------------------------- | --- | --- | --- | ------------- | --- | --- | ----------- | ---------- | --- | ----------- | --- | --- | -------- |
|                                 |     |     |     |               |     |     | sic student | downstream |     | performance |     | to  | evaluate |
servableperformancegains. Thissuggeststhatour teachermodelsacrossvariousgenerationmethods.
evaluationprotocolisrobustthattheinsightstrans-
| fer to an | unseen | language, |     | even when | measured |     | 7 Conclusion |     |     |     |     |     |     |
| --------- | ------ | --------- | --- | --------- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
withadifferentsetofdownstreammetrics.
Weconductacomprehensiveevaluationofstate-of-
the-artLMsasmultilingualteachersforsynthetic
6 RelatedWork
|     |     |     |     |     |     |     | data generation |               | by assessing |         | both  | intrinsic    | data |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------------- | ------------ | ------- | ----- | ------------ | ---- |
|     |     |     |     |     |     |     | quality         | and extrinsic |              | student | model | performance. |      |
SyntheticDataGenerationforMultilingualSFT
Wefindseveralpropertiesthatcontributetoteacher
| In order | to offset | the | high | costs of recruiting |     | lan- |     |     |     |     |     |     |     |
| -------- | --------- | --- | ---- | ------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
guage experts for data collection, prior works re- effectivenessoutsideofmodelsizeorbenchmark
lied on generating synthetic datasets. This ef- performance, such as prompt-response diversity,
|     |     |     |     |     |     |     | fluency,andlanguagerepresentation. |     |     |     |     | Finally,we |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ---------- | --- |
fortresultedinlargemultilingualdatasetssuchas
|            |             |     |     |                |          |     | outline | practical | recommendations |     |     | for | creating a |
| ---------- | ----------- | --- | --- | -------------- | -------- | --- | ------- | --------- | --------------- | --- | --- | --- | ---------- |
| Bactrian-X | (Translate, |     | Li  | et al., 2023), | MultiAl- |     |         |           |                 |     |     |     |            |
paca (Generate, Wei et al., 2023), and xP3 (Re- multilingualsyntheticdatagenerationrecipe. We
|     |     |     |     |     |     |     | hope our | findings | guide | future | work | on  | develop- |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----- | ------ | ---- | --- | -------- |
spond,Muennighoffetal.,2023)thatwerecreated
inginclusivelanguagetechnologiesthroughhigh-
| through | various | data | generation | methods. |     | These |     |     |     |     |     |     |     |
| ------- | ------- | ---- | ---------- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
workshavedifferentdatagenerationrecipes,and qualitysyntheticdata.
| so we provide |     | a brief | survey | of these | works | and |     |     |     |     |     |     |     |
| ------------- | --- | ------- | ------ | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Limitations
| their recipes |     | in Appendix |     | A, then classify |     | them |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
acrossthethreestrategies/archetypes(Generate, Our work comes with some limitations and open
Translate,Response;2.2). Buildingontheseprior questions left for future work. For example, our
efforts, we examine the three core strategies for languagesetencompassessixlanguages. Although
8

we chose these languages carefully based on (1) ProceedingsoftheFourthWorkshoponGeneration,
EvaluationandMetrics(GEM²),pages927–946,Vi-
whethertheycanbeevaluatedonpublicly-available
|     |     |     |     |     |     | enna, Austria | and | virtual | meeting. | Association | for |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ----------- | --- |
LMbenchmarksand(2)priortheoreticalworkon
ComputationalLinguistics.
| principled | test | language | selection | (Ploeger | et al., |                 |                        |     |     |     |       |
| ---------- | ---- | -------- | --------- | -------- | ------- | --------------- | ---------------------- | --- | --- | --- | ----- |
|            |      |          |           |          |         | Anthropic.2024. | TheClaude3ModelFamily: |     |     |     | Opus, |
2026),validatingourfindingsacrossabroaderlan-
guage sample remains important future work. In Sonnet,Haiku. Technicalreport,Anthropic.
addition,ourTranslatedatagenerationmethodas-
|     |     |     |     |     |     | David Anugraha, | Shou-Yi |     | Hung, | Zilu | Tang, En- |
| --- | --- | --- | --- | --- | --- | --------------- | ------- | --- | ----- | ---- | --------- |
sumesaccesstoEnglishpromptsthatcanbemean- ShiunAnnieLee,DerryTantiWijaya,andGentaIn-
ingfully translated to target languages. This ap- dra Winata. 2026. mR3: Multilingual Rubric-
|        |          |             |      |          |       | AgnosticRewardReasoningModels. |     |     |     | InTheFour- |     |
| ------ | -------- | ----------- | ---- | -------- | ----- | ------------------------------ | --- | --- | --- | ---------- | --- |
| proach | inherits | limitations | from | LM-based | tech- |                                |     |     |     |            |     |
teenthInternationalConferenceonLearningRepre-
| niques | such as | localizing | culture-specific |     | refer- | sentations. |     |     |     |     |     |
| ------ | ------- | ---------- | ---------------- | --- | ------ | ----------- | --- | --- | --- | --- | --- |
ences,introducingtranslationeseartifacts.
|     |     |     |     |     |     | Mikel Artetxe | and Holger | Schwenk. |     | 2019. | Margin- |
| --- | --- | --- | --- | --- | --- | ------------- | ---------- | -------- | --- | ----- | ------- |
EthicsStatement basedParallelCorpusMiningwithMultilingualSen-
|     |     |     |     |     |     | tenceEmbeddings. |     | InProceedingsofthe57thAn- |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------------- | --- | --- | --- |
nualMeetingoftheAssociationforComputational
Syntheticdatagenerationrisksamplifyingbiases
Linguistics,pages3197–3203,Florence,Italy.Asso-
| presentinteachermodels. |     |     | Ifateachermodelunder- |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ciationforComputationalLinguistics.
performsoncertainlanguagesorexhibitscultural
|     |     |     |     |     |     | Viraat Aryabumi, |     | John Dang, | Dwarak |     | Talupuru, |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | ------ | --- | --------- |
biases,theseweaknessespropagatetostudentmod-
|                         |     |     |                       |     |     | Saurabh    | Dash, David | Cairuz, | Hangyu | Lin,  | Bharat  |
| ----------------------- | --- | --- | --------------------- | --- | --- | ---------- | ----------- | ------- | ------ | ----- | ------- |
| elstrainedonitsoutputs. |     |     | Ourfindingthatteacher |     |     |            |             |         |        |       |         |
|                         |     |     |                       |     |     | Venkitesh, | Madeline    | Smith,  | Jon    | Ander | Campos, |
effectivenesscorrelateswithCommonCrawlrepre-
|     |     |     |     |     |     | Yi Chern | Tan, Kelly | Marchisio, |     | Max Bartolo, | Se- |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ---------- | --- | ------------ | --- |
sentation(ρ = 0.886,basedonsixlanguages)sug- bastianRuder,AcyrLocatelli,JuliaKreutzer,Nick
Frosst,AidanGomez,PhilBlunsom,MarziehFadaee,
geststhatalreadyunderrepresentedlanguagesmay
|     |     |     |     |     |     | and 2 others. | 2024. | Aya | 23: | Open | Weight Re- |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | --- | --- | ---- | ---------- |
befurtherdisadvantagedinsyntheticdatapipelines,
|     |     |     |     |     |     | leases to | Further | Multilingual | Progress. |     | Preprint, |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ------------ | --------- | --- | --------- |
potentiallywideningtheperformancegapbetween
arXiv:2405.15032.
high-andlow-resourcelanguages.
YauhenBabakhin,RadekOsmulski,RonayAk,Gabriel
| Acknowledgments |     |                    |     |             |        | Moreira,MengyaoXu,BenediktSchifferer,BoLiu, |                   |                |                       |       |           |
| --------------- | --- | ------------------ | --- | ----------- | ------ | ------------------------------------------- | ----------------- | -------------- | --------------------- | ----- | --------- |
|                 |     |                    |     |             |        | andEvenOldridge.2025.                       |                   |                | Llama-Embed-Nemotron- |       |           |
|                 |     |                    |     |             |        | 8B: A Universal                             |                   | Text Embedding |                       | Model | for Mul-  |
| LJVM and        | AK  | acknowledge        |     | the support | of the |                                             |                   |                |                       |       |           |
|                 |     |                    |     |             |        | tilingual                                   | and Cross-Lingual |                | Tasks.                |       | Preprint, |
| UKRI Frontier   |     | Grant EP/Y031350/1 |     | (EQUATE).   |        |                                             |                   |                |                       |       |           |
arXiv:2511.07025.
Thisworkwasperformedusingjointresourcespro-
vided by the Cambridge Service for Data Driven NicolasBoizard,KevinElHaddad,CelineHudelot,and
Discovery(CSD3)EP/T022159/1,IsambardAINa- Pierre Colombo. 2025. Towards Cross-Tokenizer
|     |     |     |     |     |     | Distillation: | theUniversalLogitDistillationLossfor |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------ | --- | --- | --- | --- |
tionalAIResearchResource(AIRR)ST/AIRR/I-A-
|                                      |     |     |     |     |      | LLMs. TransactionsonMachineLearningResearch. |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ---- | -------------------------------------------- | --- | --- | --- | --- | --- |
| I/1023,andtheMicrosoftResearchGrant. |     |     |     |     | LJVM |                                              |     |     |     |     |     |
SamuelCahyawijaya,HolyLovenia,FajriKoto,Rifki
wouldalsoliketothankSongboHu,ChenCecilia
Putri,WawanCenggoro,JhonsonLee,SalsabilAk-
Liu,MillicentOchieng,andFelerminoAliforhelp-
|     |     |     |     |     |     | bar, Emmanuel | Dave, | Nuurshadieq |     | Nuurshadieq, |     |
| --- | --- | --- | --- | --- | --- | ------------- | ----- | ----------- | --- | ------------ | --- |
fulandproductivediscussionsontheproject.
MuhammadMahendra,RrPutri,BryanWilie,Genta
|            |     |     |     |     |     | Winata,                                        | Alham Aji, | Ayu                          | Purwarianti, | and     | Pascale |
| ---------- | --- | --- | --- | --- | --- | ---------------------------------------------- | ---------- | ---------------------------- | ------------ | ------- | ------- |
|            |     |     |     |     |     | Fung.2024.                                     | Cendol:    | Openinstruction-tunedgenera- |              |         |         |
| References |     |     |     |     |     | tivelargelanguagemodelsforIndonesianlanguages. |            |                              |              |         |         |
|            |     |     |     |     |     | In Proceedings                                 | of         | the 62nd                     | Annual       | Meeting | of the  |
RishabhAgarwal,NinoVieillard,YongchaoZhou,Piotr
AssociationforComputationalLinguistics(Volume1:
Stanczyk,SabelaRamosGarea,MatthieuGeist,and
LongPapers),pages14899–14914,Bangkok,Thai-
| Olivier | Bachem. | 2024. | On-Policy | Distillation | of  |     |     |     |     |     |     |
| ------- | ------- | ----- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
land.AssociationforComputationalLinguistics.
| Language | Models: | Learning | from | Self-Generated |     |     |     |     |     |     |     |
| -------- | ------- | -------- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Mistakes. InTheTwelfthInternationalConference Mengzhang Cai, Xin Gao, Yu Li, Honglin Lin,
onLearningRepresentations. ZhengLiu,ZhuoshiPan,QizhiPei,XiaoranShang,
MengyuanSun,ZinanTang,XiaoyangWang,Zhan-
Sanchit Ahuja, Kumar Tanmay, Hardik Hansrajbhai ping Zhong, Yun Zhu, Dahua Lin, Conghui He,
Chauhan,BarunPatra,KritiAggarwal,LucianoDel
|        |         |        |       |         |           | andLijunWu.2025. |     | OpenDataArena: |     |     | AFairand |
| ------ | ------- | ------ | ----- | ------- | --------- | ---------------- | --- | -------------- | --- | --- | -------- |
| Corro, | Arindam | Mitra, | Tejas | Indulal | Dhamecha, |                  |     |                |     |     |          |
OpenArenaforBenchmarkingPost-TrainingDataset
Ahmed Hassan Awadallah, Monojit Choudhury, Value. Preprint,arXiv:2512.14051.
| Vishrav | Chaudhary, | and | Sunayana | Sitaram. | 2025. |     |     |     |     |     |     |
| ------- | ---------- | --- | -------- | -------- | ----- | --- | --- | --- | --- | --- | --- |
sPhinX: Sample Efficient Multilingual Instruction Hao Chen, Abdul Waheed, Xiang Li, Yidong Wang,
Fine-TuningThroughN-shotGuidedPrompting. In Jindong Wang, Bhiksha Raj, and Marah I. Abdin.
9

2024. OntheDiversityofSyntheticDataanditsIm- Srishti Gureja, Lester James Validad Miranda,
pactonTrainingLargeLanguageModels. Preprint, Shayekh Bin Islam, Rishabh Maheshwary, Drishti
arXiv:2410.15226. Sharma,GustiTriandiWinata,NathanLambert,Se-
|     |     |     |     |     |     | bastian | Ruder, | Sara | Hooker, | and | Marzieh | Fadaee. |
| --- | --- | --- | --- | --- | --- | ------- | ------ | ---- | ------- | --- | ------- | ------- |
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, 2025. M-RewardBench: EvaluatingRewardModels
MarkChen,HeewooJun,LukaszKaiser,Matthias inMultilingualSettings. InProceedingsofthe63rd
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro AnnualMeetingoftheAssociationforComputational
Nakano, Christopher Hesse, and John Schulman. Linguistics(Volume1: LongPapers),pages43–58,
2021. TrainingVerifierstoSolveMathWordProb- Vienna,Austria.AssociationforComputationalLin-
| lems. | Preprint,arXiv:2110.14168. |     |     |     |     | guistics. |     |     |     |     |     |     |
| ----- | -------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
CohereTeam,Aakanksha,ArashAhmadian,Marwan NathanHabib,ClémentineFourrier,HynekKydlícˇek,
Ahmed,JayAlammar,MiladAlizadeh,YazeedAl- ThomasWolf,andLewisTunstall.2023. LightEval:
numay,SophiaAlthammer,ArkadyArkhangorodsky, AlightweightframeworkforLLMevaluation.
ViraatAryabumi,DennisAumiller,RaphaëlAvalos,
HasanAbedAlKaderHammoud,MohamadBilalZbib,
| Zahara                              | Aviv, | Sammie      | Bae, Saurabh |           | Baji, Alexan- |                                     |                |                               |             |                     |               |       |
| ----------------------------------- | ----- | ----------- | ------------ | --------- | ------------- | ----------------------------------- | -------------- | ----------------------------- | ----------- | ------------------- | ------------- | ----- |
|                                     |       |             |              |           |               | andBernardGhanem.2026.              |                |                               |             | HalaTechnicalReport |               |       |
| dre Barbet,                         | Max   | Bartolo,    | Björn        | Bebensee, | Neeral        |                                     |                |                               |             |                     |               |       |
|                                     |       |             |              |           |               | Building                            | Arabic-Centric |                               | Instruction |                     | & Translation |       |
| Beladia,                            | and   | 210 others. | 2025.        | Command   | A: An         |                                     |                |                               |             |                     |               |       |
|                                     |       |             |              |           |               | ModelsatScale.                      |                | InProceedingsofthe2ndWorkshop |             |                     |               |       |
| Enterprise-ReadyLargeLanguageModel. |       |             |              |           | Preprint,     |                                     |                |                               |             |                     |               |       |
|                                     |       |             |              |           |               | onNLPforLanguagesUsingArabicScript, |                |                               |             |                     |               | pages |
arXiv:2504.00698.
236–244,Rabat,Morocco.AssociationforComputa-
tionalLinguistics.
| John Dang, | Shivalika | Singh, | Daniel | D’souza, | Arash |     |     |     |     |     |     |     |
| ---------- | --------- | ------ | ------ | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Ahmadian,AlejandroSalamanca,MadelineSmith,
|     |     |     |     |     |     | Daniel Han, | Michael | Han, | and | Unsloth | Team. | 2023. |
| --- | --- | --- | --- | --- | --- | ----------- | ------- | ---- | --- | ------- | ----- | ----- |
AidanPeppin,SungjinHong,ManojGovindassamy,
Unsloth.
| TerrenceZhao, |     | SandraKublik, |     | MeorAmer, | Viraat |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Aryabumi,JonAnderCampos,Yi-ChernTan,Tom DanHendrycks,CollinBurns,StevenBasart,AndyZou,
Kocmi,FlorianStrub,NathanGrinsztajn,YannisFlet- MantasMazeika,DawnSong,andJacobSteinhardt.
Berliac,and26others.2024. AyaExpanse: Combin- 2021. MeasuringMassiveMultitaskLanguageUn-
ingResearchBreakthroughsforaNewMultilingual
|           |                            |     |     |     |     | derstanding.        |     | InInternationalConferenceonLearn- |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | ------------------- | --- | --------------------------------- | --- | --- | --- | --- |
| Frontier. | Preprint,arXiv:2412.04261. |     |     |     |     | ingRepresentations. |     |                                   |     |     |     |     |
Kenneth Enevoldsen, Isaac Chung, Imene Kerboua, PratikJoshi, SebastinSanty, AmarBudhiraja, Kalika
Márton Kardos, Ashwin Mathur, David Stap, Bali,andMonojitChoudhury.2020. TheStateand
Jay Gala, Wissam Siblini, Dominik Krzemin´ski, FateofLinguisticDiversityandInclusionintheNLP
|       |       |              |         |         |         | World. | InProceedingsofthe58thAnnualMeetingof |     |     |     |     |     |
| ----- | ----- | ------------ | ------- | ------- | ------- | ------ | ------------------------------------- | --- | --- | --- | --- | --- |
| Genta | Indra | Winata, Saba | Sturua, | Saiteja | Utpala, |        |                                       |     |     |     |     |     |
theAssociationforComputationalLinguistics,pages
MathieuCiancone,MarionSchaeffer,DigantaMisra,
Shreeya Dhakal, Jonathan Rystrøm, Roman Solo- 6282–6293,Online.AssociationforComputational
| matin, | Ömer    | Veysel Çag˘atan, |     | and 63 | others. 2025. | Linguistics. |     |     |     |     |     |     |
| ------ | ------- | ---------------- | --- | ------ | ------------- | ------------ | --- | --- | --- | --- | --- | --- |
| MMTEB: | Massive | Multilingual     |     | Text   | Embedding     |              |     |     |     |     |     |     |
Benchmark. In The Thirteenth International Con- Armand Joulin, Edouard Grave, Piotr Bojanowski,
MatthijsDouze,HérveJégou,andTomasMikolov.
ferenceonLearningRepresentations.
|     |     |     |     |     |     | 2016.   | FastText.zip:              | Compressingtextclassification |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | -------------------------- | ----------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     | models. | Preprint,arXiv:1612.03651. |                               |     |     |     |     |
GemmaTeam,AishwaryaKamath,JohanFerret,Shreya
Pathak,NinoVieillard,RamonaMerhej,SarahPerrin,
ArmandJoulin,EdouardGrave,PiotrBojanowski,and
| Tatiana | Matejovicova, |     | Alexandre | Ramé, | Morgane |       |          |       |     |           |     |           |
| ------- | ------------- | --- | --------- | ----- | ------- | ----- | -------- | ----- | --- | --------- | --- | --------- |
|         |               |     |           |       |         | Tomas | Mikolov. | 2017. | Bag | of Tricks | for | Efficient |
Rivière,LouisRouillard,ThomasMesnard,Geoffrey
|     |     |     |     |     |     | TextClassification. |     | InProceedingsofthe15thCon- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | -------------------------- | --- | --- | --- | --- |
Cideron,JeanbastienGrill,SabelaRamos,Edouard
ferenceoftheEuropeanChapteroftheAssociation
Yvinec,MichelleCasbon,EtiennePot,IvoPenchev,
|                    |     |     |                        |     |     | forComputationalLinguistics: |     |     |           | Volume2,ShortPa-  |     |     |
| ------------------ | --- | --- | ---------------------- | --- | --- | ---------------------------- | --- | --- | --------- | ----------------- | --- | --- |
| and197others.2025. |     |     | Gemma3TechnicalReport. |     |     |                              |     |     |           |                   |     |     |
|                    |     |     |                        |     |     | pers, pages427–431,          |     |     | Valencia, | Spain.Association |     |     |
Preprint,arXiv:2503.19786.
forComputationalLinguistics.
GraniteTeam,IBM.2025. Granite4.0LanguageMod- ShivaniKapania,StephanieBallard,AlexKessler,and
els. https://huggingface.co/collections/ Jennifer Wortman Vaughan. 2025. Examining the
ibm-granite/granite-40-language-models.
ExpandingRoleofSyntheticDataThroughoutthe
| Accessed: | 2025-12-08. |     |     |     |     |                        |            |     |                        |                 |     |     |
| --------- | ----------- | --- | --- | --- | --- | ---------------------- | ---------- | --- | ---------------------- | --------------- | --- | --- |
|           |             |     |     |     |     | AIDevelopmentPipeline. |            |     | InProceedingsofthe2025 |                 |     |     |
|           |             |     |     |     |     | ACM                    | Conference | on  | Fairness,              | Accountability, |     | and |
AaronGrattafiori,AbhimanyuDubey,AbhinavJauhri, Transparency,FAccT’25,pages45–60,NewYork,
Abhinav Pandey, Abhishek Kadian, Ahmad Al- NY,USA.AssociationforComputingMachinery.
| Dahle, | Aiesha | Letman, | Akhil | Mathur, | Alan Schel- |     |     |     |     |     |     |     |
| ------ | ------ | ------- | ----- | ------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ten,AlexVaughan,AmyYang,AngelaFan,Anirudh JaredKaplan,SamMcCandlish,TomHenighan,TomB.
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi- Brown,BenjaminChess,RewonChild,ScottGray,
tra, Archie Sravankumar, Artem Korenev, Arthur AlecRadford,JeffreyWu,andDarioAmodei.2020.
Hinsvark,and542others.2024. TheLlama3Herd Scalinglawsforneurallanguagemodels. Preprint,
| ofModels. | Preprint,arXiv:2407.21783. |     |     |     |     | arXiv:2001.08361. |     |     |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
10

Seungone Kim, Juyoung Suk, Xiang Yue, Vijay Pombal, Nicolas Boizard, Manuel Faysse, Pierre
Viswanathan,SeongyunLee,YizhongWang,Kiril Colombo,FrançoisYvon,BarryHaddow,JoséG.C.
Gashteovski,CarolinLawrence,SeanWelleck,and deSouza,AlexandraBirch,andAndréF.T.Martins.
Preprint,
GrahamNeubig.2025. Evaluatinglanguagemodels 2025. EuroLLM-9B: Technical Report.
| assyntheticdatagenerators. |     | InProceedingsofthe | arXiv:2506.04079. |     |     |     |
| -------------------------- | --- | ------------------ | ----------------- | --- | --- | --- |
63rdAnnualMeetingoftheAssociationforCompu-
tationalLinguistics(Volume1: LongPapers),pages PedroHenriqueMartins,PatrickFernandes,JoãoAlves,
6385–6403,Vienna,Austria.AssociationforCompu- NunoM.Guerreiro,RicardoRei,DuarteM.Alves,
tationalLinguistics. José Pombal, Amin Farajian, Manuel Faysse, Ma-
teuszKlimaszewski,PierreColombo,BarryHaddow,
Yoon Kim and Alexander M. Rush. 2016. Sequence- JoséG.C.deSouza,AlexandraBirch,andAndréF.T.
levelknowledgedistillation. InProceedingsofthe Martins. 2024. EuroLLM: Multilingual Language
2016 Conference on Empirical Methods in Natu- ModelsforEurope. Preprint,arXiv:2409.16235.
ralLanguageProcessing,pages1317–1327,Austin,
Texas.AssociationforComputationalLinguistics. LesterJamesValidadMiranda,ElyanahAco,ConnerG.
Manuel,JanChristianBlaiseCruz,andJosephMar-
AnoopKunchukuttan,RajDabre,RudraMurthy,Mo- vin Imperial. 2025. FilBench: Can LLMs Under-
|     |     |     |     |     |     | Proceedings of |
| --- | --- | --- | --- | --- | --- | -------------- |
hammed Safi Ur Rahman Khan, and Thanmay stand and Generate Filipino? In
Jayakumar. 2025. Data and Model Centric Ap- the2025ConferenceonEmpiricalMethodsinNatu-
proachesforExpansionofLargeLanguageModels ralLanguageProcessing,pages2496–2529,Suzhou,
toNewlanguages. InProceedingsofthe2025Con- China.AssociationforComputationalLinguistics.
ferenceonEmpiricalMethodsinNaturalLanguage
NiklasMuennighoff,ThomasWang,LintangSutawika,
Processing:TutorialAbstracts,pages12–13,Suzhou,
|     |     |     | Adam Roberts, | Stella | Biderman, | Teven Le Scao, |
| --- | --- | --- | ------------- | ------ | --------- | -------------- |
China.AssociationforComputationalLinguistics.
|     |     |     | MSaifulBari, | ShengShen, | ZhengXinYong, | Hai- |
| --- | --- | --- | ------------ | ---------- | ------------- | ---- |
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying ley Schoelkopf, Xiangru Tang, Dragomir Radev,
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Alham Fikri Aji, Khalid Almubarak, Samuel Al-
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Ef- banie,ZaidAlyafeai,AlbertWebson,EdwardRaff,
|                                 |            |                    | and Colin                       | Raffel. 2023. | Crosslingual | Generaliza-   |
| ------------------------------- | ---------- | ------------------ | ------------------------------- | ------------- | ------------ | ------------- |
| ficient Memory                  | Management | for Large Language |                                 |               |              |               |
|                                 |            |                    | tionthroughMultitaskFinetuning. |               |              | InProceedings |
| ModelServingwithPagedAttention. |            | InProceedings      |                                 |               |              |               |
oftheACMSIGOPS29thSymposiumonOperating of the 61st Annual Meeting of the Association for
SystemsPrinciples. ComputationalLinguistics(Volume1: LongPapers),
pages15991–16111,Toronto,Canada.Association
Nathan Lambert, Jacob Morrison, Valentina Pyatkin, forComputationalLinguistics.
| Shengyi Huang, | Hamish           | Ivison, Faeze Brahman, |             |            |         |             |
| -------------- | ---------------- | ---------------------- | ----------- | ---------- | ------- | ----------- |
|                |                  |                        | Raymond Ng, | Thanh Ngan | Nguyen, | Huang Yuli, |
| Lester James   | Validad Miranda, | Alisa Liu,             | Nouha       |            |         |             |
TaiNgeeChia,LeongWaiYi,WeiQiLeong,Xianbin
Dziri,XinxiLyu,YulingGu,SaumyaMalik,Victoria
Graf, Jena D. Hwang, Jiangjiang Yang, Ronan Le Yong,JianGangNgui,YosephineSusanto,Nicholas
Bras, Oyvind Tafjord, Christopher Wilhelm, Luca Cheng,HamsawardhiniRengarajan,PeeratLimkon-
Soldaini,and4others.2025. Tulu3: PushingFron- chotiwat, Adithya Venkatadri Hulagadri, Kok Wai
|               |          |                      | Teng, Yeo | Yeow Tong, | Bryan Siow, | Wei Yi Teo, |
| ------------- | -------- | -------------------- | --------- | ---------- | ----------- | ----------- |
| tiers in Open | Language | Model Post-Training. | In        |            |             |             |
TanChoonMeng,BrandonOng,and11others.2025.
SecondConferenceonLanguageModeling.
SEA-LION:SoutheastAsianLanguagesinOneNet-
HaonanLi,FajriKoto,MinghaoWu,AlhamFikriAji, work. InProceedingsofthe14thInternationalJoint
andTimothyBaldwin.2023. Bactrian-X:Multilin- Conference on Natural Language Processing and
gual replicable instruction-following models with the 4th Conference of the Asia-Pacific Chapter of
low-rankadaptation. Preprint,arXiv:2305.15011. theAssociationforComputationalLinguistics,pages
512–526,Mumbai,India.TheAsianFederationof
YuetaiLi,XiangYue,ZhangchenXu,FengqingJiang, NaturalLanguageProcessingandTheAssociation
LuyaoNiu,BillYuchenLin,BhaskarRamasubrama- forComputationalLinguistics.
| nian,andRadhaPoovendran.2025. |     | SmallModels |     |     |     |     |
| ----------------------------- | --- | ----------- | --- | --- | --- | --- |
StruggletoLearnfromStrongReasoners. InFind- NLLBTeam,MartaR.Costa-jussà,JamesCross,Onur
ingsoftheAssociationforComputationalLinguistics: Çelebi,MahaElbayad,KennethHeafield,KevinHef-
|     |     |     | fernan, Elahe | Kalbassi, | Janice Lam, | Daniel Licht, |
| --- | --- | --- | ------------- | --------- | ----------- | ------------- |
ACL2025,pages25366–25394,Vienna,Austria.As-
sociationforComputationalLinguistics. JeanMaillard,AnnaSun,SkylerWang,Guillaume
Wenzek,AlYoungblood,BapiAkula,LoicBarrault,
RyanMarten,TrungVu,CharlieCheng-JieJi,Kartik Gabriel Mejia Gonzalez, Prangthip Hansanti, and
Sharma,ShreyasPimpalgaonkar,AlexDimakis,and 20 others. 2022. No language left behind: Scal-
MaheswaranSathiamoorthy.2025. Curator: ATool inghuman-centeredmachinetranslation. Preprint,
| forSyntheticDataCreation. |     | https://github.com/ |     |     |     |     |
| ------------------------- | --- | ------------------- | --- | --- | --- | --- |
arXiv:2207.04672.
bespokelabsai/curator.
OLMoTeam,AllysonEttinger,AmandaBertsch,Bailey
Pedro Henrique Martins, João Alves, Patrick Fernan- Kuehl,DavidGraham,DavidHeineman,DirkGroen-
des, Nuno M. Guerreiro, Ricardo Rei, Amin Fara- eveld, Faeze Brahman, Finbarr Timbers, Hamish
jian,MateuszKlimaszewski,DuarteM.Alves,José Ivison, Jacob Morrison, Jake Poznanski, Kyle Lo,
11

LucaSoldaini,MattJordan,MayeeChen,Michael AllanRaventos,MansheejPaul,FengChen,andSurya
Noukhovitch,NathanLambert,PeteWalsh,and49 Ganguli. 2023. Pretraining task diversity and the
others.2025. OLMo3. Technicalreport,AllenInsti- emergenceofnon-Bayesianin-contextlearningfor
tuteforAI. TechnicalReport. regression. InThirty-seventhConferenceonNeural
InformationProcessingSystems.
OpenAI,AaronHurst,AdamLerer,AdamP.Goucher,
Adam Perelman, Aditya Ramesh, Aidan Clark, Alejandro R. Salamanca, Diana Abagyan, Daniel
AJ Ostrow, Akila Welihinda, Alan Hayes, Alec D’souza,AmmarKhairi,DavidMora,SaurabhDash,
Radford,AleksanderMa˛dry,AlexBaker-Whitcomb, ViraatAryabumi,SaraRajaee,MehrnazMofakhami,
Alex Beutel, Alex Borzunov, Alex Carney, Alex AnanyaSahu, ThomasEuyang, BrittawnyaPrince,
Chow, Alex Kirillov, Alex Nichol, and 400 oth- MadelineSmith,HangyuLin,AcyrLocatelli,Sara
ers. 2024. GPT-4o System Card. Preprint, Hooker,TomKocmi,AidanGomez,IvanZhang,and
arXiv:2410.21276. 7others.2026. TinyAya: BridgingScaleandMulti-
lingualDepth. Preprint,arXiv:2603.11510.
LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,
CarrollWainwright,PamelaMishkin,ChongZhang, DylanSam,AyanChakrabarti,AfshinRostamizadeh,
SandhiniAgarwal,KatarinaSlama,AlexGray,John SrikumarRamalingam,GuiCitovsky,andSanjivKu-
Schulman,JacobHilton,FraserKelton,LukeMiller, mar. 2025. Analyzing Similarity Metrics for Data
Maddie Simens, Amanda Askell, Peter Welinder, SelectionforLanguageModelPretraining. InThe
Paul Christiano, Jan Leike, and Ryan Lowe. 2022. Thirty-ninthAnnualConferenceonNeuralInforma-
Traininglanguagemodelstofollowinstructionswith tionProcessingSystems.
humanfeedback. InAdvancesinNeuralInformation
ProcessingSystems. MuhammadAliShafique,KanwalMehreen,Muham-
madArham,MaazAmjad,SaburButt,andHamza
ParinthapatPengpun,CanUdomcharoenchaikit,Weer- Farooq. 2025. Alif: Advancing Urdu Large Lan-
ayut Buaphet, and Peerat Limkonchotiwat. 2024. guageModelsviaMultilingualSyntheticDataDis-
Seed-free synthetic data generation framework for tillation. In Proceedings of the 5th Workshop on
instruction-tuningLLMs: AcasestudyinThai. In MultilingualRepresentationLearning(MRL2025),
Proceedingsofthe62ndAnnualMeetingoftheAsso- pages271–284,Suzhuo,China.AssociationforCom-
ciationforComputationalLinguistics(Volume4:Stu- putationalLinguistics.
dentResearchWorkshop),pages445–464,Bangkok,
Thailand.AssociationforComputationalLinguistics. FredaShi,MiracSuzgun,MarkusFreitag,XuezhiWang,
SurajSrivats,SoroushVosoughi,HyungWonChung,
EstherPloeger,WesselPoelman,AndreasHolckHøeg- YiTay,SebastianRuder,DennyZhou,DipanjanDas,
Petersen,AndersSchlichtkrull,MiryamdeLhoneux, and Jason Wei. 2023. Language models are multi-
andJohannesBjerva.2026. Aprincipledframework lingualchain-of-thoughtreasoners. InTheEleventh
for evaluating on typologically diverse languages. International Conference on Learning Representa-
ComputationalLinguistics,pages1–33. tions.
JoséPombal,DongkeunYoon,PatrickFernandes,Ian ShivalikaSingh,AngelikaRomanou,ClémentineFour-
Wu,SeungoneKim,RicardoRei,GrahamNeubig, rier,DavidIfeoluwaAdelani,JianGangNgui,Daniel
andAndreMartins.2025. M-Prometheus: ASuite Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
ofOpenMultilingualLLMJudges. InSecondCon- sio, Wei Qi Leong, Yosephine Susanto, Raymond
ferenceonLanguageModeling. Ng, Shayne Longpre, Sebastian Ruder, Wei-Yin
Ko, Antoine Bosselut, Alice Oh, Andre Martins,
Libo Qin, Qiguang Chen, Yuhang Zhou, Zhi Chen, Leshem Choshen, Daphne Ippolito, and 4 others.
YinghuiLi,LiziLiao,MinLi,WanxiangChe,and 2025. GlobalMMLU:UnderstandingandAddress-
PhilipS.Yu.2025. Asurveyofmultilinguallarge ing Cultural and Linguistic Biases in Multilingual
languagemodels. Patterns,6(1):101118. Evaluation. InProceedingsofthe63rdAnnualMeet-
ingoftheAssociationforComputationalLinguistics
NeelPrabhanjanRachamalla,AravindKonakalla,Gau- (Volume1: LongPapers), pages18761–18799, Vi-
tamRajeev, AshishKulkarni, ChandraKhatri, and enna, Austria. Association for Computational Lin-
Shubham Agarwal. 2025. Pragyaan: Designing guistics.
and Curating High-Quality Cultural Post-Training
DatasetsforIndianLanguages. InProceedingsofthe Shivalika Singh, Freddie Vargus, Daniel D’souza,
5thWorkshoponMultilingualRepresentationLearn- Börje F. Karlsson, Abinaya Mahendiran, Wei-Yin
ing(MRL2025),pages285–321,Suzhuo,China.As- Ko,HerumbShandilya,JayPatel,DeividasMataci-
sociationforComputationalLinguistics. unas, Laura O’Mahony, Mike Zhang, Ramith Het-
tiarachchi,JosephWilson,MarinaMachado,Luisa
ColinRaffel,NoamShazeer,AdamRoberts,Katherine Moura,DominikKrzemin´ski,HakimehFadaei,Irem
Lee,SharanNarang,MichaelMatena,YanqiZhou, Ergun, Ifeoma Okoh, and 14 others. 2024. Aya
WeiLi,andPeterJ.Liu.2020. Exploringthelimits Dataset: An Open-Access Collection for Multilin-
oftransferlearningwithaunifiedtext-to-texttrans- gualInstructionTuning. InProceedingsofthe62nd
former. J.Mach.Learn.Res.,21(1). AnnualMeetingoftheAssociationforComputational
12

Linguistics(Volume1: LongPapers),pages11521– ShengyuZhang,LinfengDong,XiaoyaLi,SenZhang,
11567,Bangkok,Thailand.AssociationforCompu- XiaofeiSun,ShuheWang,JiweiLi,RunyiHu,Tian-
tationalLinguistics. weiZhang, FeiWu, andGuoyinWang.2025b. In-
structionTuningforLargeLanguageModels: ASur-
Bibek Upadhayay and Vahid Behzadan. 2024. TaCo: vey. Preprint,arXiv:2308.10792.
EnhancingCross-LingualTransferforLow-Resource
Languages in LLMs through Translation-Assisted WentingZhao,XiangRen,JackHessel,ClaireCardie,
Chain-of-Thought Processes. In 5th Workshop on Yejin Choi, and Yuntian Deng. 2024. WildChat:
practicalMLforlimited/lowresourcesettings. 1MChatGPTInteractionLogsintheWild. InThe
TwelfthInternationalConferenceonLearningRepre-
YizhongWang,YeganehKordi,SwaroopMishra,Alisa
sentations.
Liu,NoahA.Smith,DanielKhashabi,andHannaneh
Hajishirzi. 2023. Self-instruct: Aligning language AlanZhu,ParthAsawa,JaredQuincyDavis,Lingjiao
modelswithself-generatedinstructions. InProceed- Chen,BorisHanin,IonStoica,JosephE.Gonzalez,
ingsofthe61stAnnualMeetingoftheAssociationfor andMateiZaharia.2025. BARE:LeveragingBase
ComputationalLinguistics(Volume1: LongPapers), LanguageModelsforFew-ShotSyntheticDataGen-
pages13484–13508,Toronto,Canada.Association eration. Preprint,arXiv:2502.01697.
forComputationalLinguistics.
Zhilin Wang, Jiaqi Zeng, Olivier Delalleau, Daniel
Egert,EllieEvans,Hoo-ChangShin,FelipeSoares,
Yi Dong, and Oleksii Kuchaiev. 2025. Help-
Steer3: Human-AnnotatedFeedbackandEditData
toEmpowerInference-TimeScalinginOpen-Ended
General-DomainTasks. Preprint,arXiv:2503.04378.
Xiangpeng Wei, Haoran Wei, Huan Lin, Tianhao Li,
Pei Zhang, Xingzhang Ren, Mei Li, Yu Wan, Zhi-
wei Cao, Binbin Xie, Tianxiang Hu, Shangjie Li,
Binyuan Hui, Bowen Yu, Dayiheng Liu, Baosong
Yang, Fei Huang, and Jun Xie. 2023. PolyLM:
An Open Source Polyglot Large Language Model.
Preprint,arXiv:2307.06018.
Zhangchen Xu, Fengqing Jiang, Luyao Niu, Yun-
tian Deng, Radha Poovendran, Yejin Choi, and
Bill Yuchen Lin. 2025a. Magpie: Alignment data
synthesisfromscratchbypromptingalignedLLMs
withnothing. InTheThirteenthInternationalCon-
ferenceonLearningRepresentations.
ZhangchenXu,FengqingJiang,LuyaoNiu,BillYuchen
Lin,andRadhaPoovendran.2025b. Strongermod-
elsarenotalwaysstrongerteachersforinstruction
tuning. InProceedingsofthe2025Conferenceofthe
NationsoftheAmericasChapteroftheAssociation
for Computational Linguistics: Human Language
Technologies(Volume1: LongPapers),pages4392–
4405, Albuquerque, New Mexico. Association for
ComputationalLinguistics.
AnYang,AnfengLi,BaosongYang,BeichenZhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025. Qwen3 Technical Report. Preprint,
arXiv:2505.09388.
Hengyuan Zhang, Shiping Yang, Xiao Liang, Chen-
ming Shang, Yuxuan Jiang, Chaofan Tao, Jing
Xiong, Hayden Kwok-Hay So, Ruobing Xie, An-
gel X. Chang, and Ngai Wong. 2025a. Find Your
Optimal Teacher: Personalized Data Synthesis via
Router-GuidedMulti-TeacherDistillation. Preprint,
arXiv:2510.10925.
13

Appendix
| A MultilingualSyntheticDataGeneration  |            |     | 16  |
| -------------------------------------- | ---------- | --- | --- |
| B SeedDatasetStatistics                |            |     | 16  |
| C The POLYGLOT                         | Collection |     | 16  |
| D TeacherModelandTargetLanguageDetails |            |     | 16  |
| E ExperimentalDetails                  |            |     | 16  |
E.1 SupervisedFinetuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
E.2 ModelEvaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
| F FullResultsforIntr.               | andExtr. Metrics |     | 16  |
| ----------------------------------- | ---------------- | --- | --- |
| G AdditionalExperimentsandAblations |                  |     | 17  |
G.1 EffectofDataScaleonStudentModelPerformance . . . . . . . . . . . . . . . . . . . . 17
G.2 GeneralizationAcrossModelSize . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
G.3 EffectofTranslationMethod(PromptinganLMvs. TranslationModel) . . . . . . . . . 18
G.4 WeighingofIntrinsicandExtrinsicMetricsin PG-SCORE . . . . . . . . . . . . . . . . 19
G.5 Effectoflanguageresourcelevelson PG-SCORE . . . . . . . . . . . . . . . . . . . . . 21
| H DisclosureontheUseofLLMs         |     |                    | 21  |
| ---------------------------------- | --- | ------------------ | --- |
| I MultilingualSyntheticDataRecipe: |     | CaseStudyonTagalog | 21  |
I.1 Setup: RecipeDesignandEvaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
I.2 Results: LeaderboardScoresandAblations . . . . . . . . . . . . . . . . . . . . . . . . 23
I.3 Analysis: AblationExperiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
| J InferenceDetails |     |     | 25  |
| ------------------ | --- | --- | --- |
14

| Dataset | Language(s) |     |     |     | GenerationMethod/Description |     |     |     |
| ------- | ----------- | --- | --- | --- | ---------------------------- | --- | --- | --- |
Bactrian-X(Lietal.,2023) 52languages-Arabic,Indonesian,Chi- Translate-usedGoogleTranslateAPI
|     | nese,Malaysian,Tamil,Tagalog,etc. |     |     |     | to translate |     | English instructions | from |
| --- | --------------------------------- | --- | --- | --- | ------------ | --- | -------------------- | ---- |
Alpaca(52K)andDolly(15K).
MultiAlpaca(Weietal.,2023) 18languages-English,Chinese,Rus- Generate,Translate-usedamultilin-
|     | sian,Spanish,German,French,etc. |     |     |     | gual | self-instruct | (Wang | et al., 2023) |
| --- | ------------------------------- | --- | --- | --- | ---- | ------------- | ----- | ------------- |
methodfromEnglishprompt-response
pairstoperformtranslation.
xP3-MT(Muennighoffetal.,2023) 46languages-Arabic,English,Span- Translate, Respond - used Google
|     | ish,Hindi,Chinese,Indonesian,etc. |     |     |     | Translate       |          | API to translate | English      |
| --- | --------------------------------- | --- | --- | --- | --------------- | -------- | ---------------- | ------------ |
|     |                                   |     |     |     | prompt-response |          | pairs            | from differ- |
|     |                                   |     |     |     | ent             | sources, | in addition      | to creating  |
template-basedpromptswhereanLM
respondstoit.
Cendol(Cahyawijayaetal.,2024) 18Indonesianlanguages-Sundanese, Translate, Respond - curated various
|     | Javanese,           | Acehnese, | Banjarese, | Bugi- | prompts                             | from | past Indonesian | NLP |
| --- | ------------------- | --------- | ---------- | ----- | ----------------------------------- | ---- | --------------- | --- |
|     | nese,Gorontalo,etc. |           |            |       | tasks,includingtranslationsofDolly. |      |                 |     |
SeedFreeThai(Pengpunetal.,2024) Thai Generate-generatedsyntheticinstruc-
tiondatawithoutseedexamplesbyus-
|     |     |     |     |     | ingWikipediacontexts. |     |     | Identifiesflu- |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | -------------- |
ency,diversity,andculturalcontextas
keyproperties.
AyaDatasetandCollection(Singhetal., 114languages-Arabic,French,Hindi, Translate,Respond-involvesacollec-
2024) Indonesian,Japanese,Spanish,Swahili, tionoftranslatedpromptsfromEnglish,
|     | Turkish,Yoruba,Filipino,etc. |     |     |     | andtemplatedprompts.Asizeablepor- |        |            |                  |
| --- | ---------------------------- | --- | --- | --- | --------------------------------- | ------ | ---------- | ---------------- |
|     |                              |     |     |     | tion                              | of the | collection | includes native- |
speakerannotations.
sPhinX(Ahujaetal.,2025) 51languages-Afrikaan,Arabic,Ben- Translate-selectivelytranslatesessen-
|     | gali, Bulgarian,    |     | Burmese, | Chinese, | tialportionsofmultilingualinputsinor- |     |     |     |
| --- | ------------------- | --- | -------- | -------- | ------------------------------------- | --- | --- | --- |
|     | Croatian,Czech,etc. |     |          |          | dertosemanticallypreservemeaning.     |     |     |     |
EuroBlocks(Martinsetal.,2025,2024) 31languages-English,Chinese,Span- Generate,Translate-promptedLlama
|     | ish, Italian,             | French, | German, | Por- | 3 or                             | an earlier | EuroLLM | checkpoint |
| --- | ------------------------- | ------- | ------- | ---- | -------------------------------- | ---------- | ------- | ---------- |
|     | tuguese,Dutch,Polish,etc. |         |         |      | withadocument,targetlanguage,and |            |         |            |
category,thenaskingittogeneratean
|     |     |     |     |     | instruction. |     | Alsoinvolvedtranslating |     |
| --- | --- | --- | --- | --- | ------------ | --- | ----------------------- | --- |
prompt-responsepairs.
SEA-LIONDataset(Ngetal.,2025) 11 languages - English, Chinese, In- Generate,Translate-forthemajority
|     | donesian, | Vietnamese, | Malay,           | Thai, | ofthedatasets,sampleswerefirstgener- |     |     |     |
| --- | --------- | ----------- | ---------------- | ----- | ------------------------------------ | --- | --- | --- |
|     | Burmese,  | Lao,        | Filipino, Khmer, | and   | atedintoEnglishusingQwen32B,and      |     |     |     |
|     | Tamil     |             |                  |       | thentranslatedintothetargetlanguage  |     |     |     |
usingGemma227B.
Urdu-InstructDataset(Shafiqueetal., Urdu Generate-usesamodifiedSelf-Instruct
| 2025) |     |     |     |     | from | a pool | of culturally | relevant |
| ----- | --- | --- | --- | --- | ---- | ------ | ------------- | -------- |
prompts.
Pragyaan(Rachamallaetal.,2025) 10 Indian languages - Gujarati, Kan- Generate,Translate-performtransla-
|     | nada, Marathi, |         | Bengali, Odia, | Tamil, | tionusinganLMforasubsetofdata.     |     |     |     |
| --- | -------------- | ------- | -------------- | ------ | ---------------------------------- | --- | --- | --- |
|     | Malayalam,     | Telugu, | Punjabi,       | Hindi, | UsedSelf-Instructfromapoolofnative |     |     |     |
|     | andSanskrit    |         |                |        | promptsforanothersubsetofdata.     |     |     |     |
Table5: ShortsurveyofrelatedworkonsyntheticdatagenerationformultilingualLMs. Foreachwork,we
provideabriefdescriptionoftheirdatagenerationmethod. Wefindthatmostmethodsfallintooneofthethree
categoriesdescribedin§2.2,i.e.,Generate,Translate,orRespond,whichwetestedinourexperiments.
15

A MultilingualSyntheticData
theUnslothframework(Hanetal.,2023)usinga
Generation
|     |     |     |     | clusterofGraceHopperGH200Superchips. |     |     | Full |
| --- | --- | --- | --- | ------------------------------------ | --- | --- | ---- |
finetuning(7B)takesaround1.5hours(wallclock)
WepresentanoverviewofpriorworksinTable5
for2epochsand2nodes.
thatusedsyntheticdatatotrainmultilingualLMs.
Ingeneral,wefindthatmostdatagenerationmeth-
|     |     |     |     | Hyperparameter | Value | Hyperparameter | Value |
| --- | --- | --- | --- | -------------- | ----- | -------------- | ----- |
odsfallintooneofthethreecategoriesdescribedin
|     |     |     |     | Learningrate | 5e-5 | Batchsize | 32  |
| --- | --- | --- | --- | ------------ | ---- | --------- | --- |
§2.2,i.e.,Generate,Translate,orRespond,which
|                           |     |                   |     | Epochs        | 2      | Grad.Acum.Steps | 4     |
| ------------------------- | --- | ----------------- | --- | ------------- | ------ | --------------- | ----- |
| wetestedinourexperiments. |     | Oursurveysuggests |     |               |        |                 |       |
|                           |     |                   |     | Maxseq.length | 16,384 | Weightdecay     | 0.001 |
thatourchoiceofdatagenerationmethodsare Optimizer AdamW Scheduler Linear
groundedinpriorworkandcoversthemajority
Table9: Hyperparametersforfinetuninga7Bstudent
ofapproachesusedinsyntheticdatageneration.
modelfromOLMo37B.
B SeedDatasetStatistics
E.2 ModelEvaluation
Table6showsthestatisticsoftheseeddatasetused
WeusedtheLightevalframework(v0.13.1dev0,
forsyntheticdatageneration.
|     |     |     |     | Habibetal.,2023)forevaluation. |     | Table10summa- |     |
| --- | --- | --- | --- | ------------------------------ | --- | ------------- | --- |
C The POLYGLOT Collection rizes the benchmarks used for evaluating student
models. WedecidedtouseGlobal-MMLULitein-
Inordertofacilitatefutureresearchonmultilingual
steadofGlobal-MMLUbecauetheformercontains
syntheticdatageneration,weintroducethePOLY-
actualnativespeakerannotationsthatlocalizedthe
GLOTcollection,acollectionofsyntheticdatasets
benchmarkintodifferentculturalcontexts.
andstudentmodelsgeneratedbythebestteacher
| modelacrossalltargetlanguages. |     | ThePOLYGLOT |     |           |             |        |         |
| ------------------------------ | --- | ----------- | --- | --------- | ----------- | ------ | ------- |
|                                |     |             |     | Benchmark | Formulation | Metric | N-shots |
collectionincludes:
|     |     |     |     | Global-MMLULite | MCF | Accuracy | 0   |
| --- | --- | --- | --- | --------------- | --- | -------- | --- |
• POLYGLOT-INSTRUCTIONS-SYNTH: Synthetic M-RewardBench MCF WeightedAcc. 0
|     |     |     |     | M-GSM | Generative | Exact-Match | 5   |
| --- | --- | --- | --- | ----- | ---------- | ----------- | --- |
datasetsforeachtargetlanguagegeneratedby
eachteachermodelusingallthreedatagenera-
Table10:Evaluationsettingsforeachbenchmark(MCF:
tionmethods(§2.2).
Multiple-ChoiceFormulation).
• POLYGLOT-GEMMA-SFT:Asetof8Bstudent
modelsfinetunedoneachsyntheticdatasetfrom
ForGlobal-MMLULiteandM-RewardBench,
theOLMo37BbasemodelusingtheGemma
|     |     |     |     | we use | the Multiple-Choice | Formulation | (MCF) |
| --- | --- | --- | --- | ------ | ------------------- | ----------- | ----- |
327B(highest-scoringmodel)teacher.
|                      |     |          |            | withcharacternormalization. |     | Inaddition,wealso |     |
| -------------------- | --- | -------- | ---------- | --------------------------- | --- | ----------------- | --- |
| Wepubliclyreleasethe |     | POLYGLOT | Collection |                             |     |                   |     |
followthecorpus-levelmetricinM-RewardBench
inHuggingFace.3
whichusesaweightedaccuracyforeachdatasub-
|     |     |     |     | setandcategory(Gurejaetal.,2025). |     | ForM-GSM, |     |
| --- | --- | --- | --- | --------------------------------- | --- | --------- | --- |
D TeacherModelandTargetLanguage
weshow5few-shotexamplesfromthetrainingset
Details
inorderforthemodeltoproperlygeneratethean-
Inthissection,weprovideadditionaldetailsabout swer. Werunallevaluationexperimentsforthree
the teacher models and target languages used in trials with different random seeds and report the
ourexperiments. Table7summarizesthekeychar- averageandstandarddeviation.
| acteristics | of each teacher | model. | On the other |     |     |     |     |
| ----------- | --------------- | ------ | ------------ | --- | --- | --- | --- |
hand,Table8providesinformationaboutthetarget F FullResultsforIntr. andExtr. Metrics
languages,includinglanguagefamily,numberof
Table11showsallthedataqualitymetricsforeach
speakers,andresourceavailability.
|     |     |     |     | teachermodelacrossalllanguages. |     | Table12shows |     |
| --- | --- | --- | --- | ------------------------------- | --- | ------------ | --- |
E ExperimentalDetails thefullresultsofstudentmodelsfinetunedonsyn-
|                          |     |     |     | thetic datasets           | generated | by each teacher | model |
| ------------------------ | --- | --- | --- | ------------------------- | --------- | --------------- | ----- |
| E.1 SupervisedFinetuning |     |     |     | acrossalltargetlanguages. |           |                 |       |
Table9summarizesthehyperparametersusedfor
|                          |     |                    |     | Percentage | Increase Tables |            |       |
| ------------------------ | --- | ------------------ | --- | ---------- | --------------- | ---------- | ----- |
|                          |     |                    |     |            |                 | We provide | addi- |
| finetuningstudentmodels. |     | Wetrainmodelsusing |     |            |                 |            |       |
tionaltablesfromthemainexperimentsin§3and
3 :ljvmiranda921/polyglot-teachers §4. Table 14 shows the percentage increase in
16

Language
Source English(en)Arabic(ar)Czech(cs)German(de)Spanish(es)Indonesian(id)Japanese(ja)
| AyaDataset         |     | -      | -     | 5,000 |     | 241    | 3,854  |     | 2,786 | 6,259 |
| ------------------ | --- | ------ | ----- | ----- | --- | ------ | ------ | --- | ----- | ----- |
| Tülu3SFT           |     | 10,000 | -     |       | -   | -      |        | -   | -     | -     |
| WildChat4.8M       |     | 10,000 | 4,660 | 1,266 |     | 5,908  | 5,900  |     | 7,983 | 602   |
| CIDAR              |     | -      | 6,000 |       | -   | -      |        | -   | -     | -     |
| Cendolv2           |     | -      | -     |       | -   | -      |        | -   | 3,000 | -     |
| OpenAssistant2     |     | -      | 23    |       | 4   | 2,328  | 8,785  |     | 3     | 306   |
| EuroBlocksSFT      |     | -      | -     | 3,813 |     | 12,551 | 15,641 |     | -     | 2,893 |
| GSM8k(train)       |     | 7,473  | -     |       | -   | -      |        | -   | -     | -     |
| Helpsteer3(chosen) |     | -      | -     |       | -   | 462    |        | 778 | 156   | 534   |
| MagpieProFiltered  |     | 10,000 | -     |       | -   | -      |        | -   | -     | -     |
Totalperlanguage
|     |     | 30,743 | 10,683 | 10,083 |     | 21,490 | 34,958 |     | 13,928 | 10,594 |
| --- | --- | ------ | ------ | ------ | --- | ------ | ------ | --- | ------ | ------ |
Table6: Seeddatasetstatistics. Inordertobootstrapoursyntheticdatagenerationmethods,weuseaseeddataset
composedofvariousmultilingualinstruction-followingdatasets. WeincludeEnglishsamplesinordertosimulate
datagenerationpipelineswhereEnglishistranslatedintoatargetlanguage. Wecollectatotalof132,929seed
examplesacross7languages(includingEnglish).
|     | ModelName                    |     |     |     | Provider | Size(B) |     | #Langs | License     |     |
| --- | ---------------------------- | --- | --- | --- | -------- | ------- | --- | ------ | ----------- | --- |
|     | GPT-4omini(OpenAIetal.,2024) |     |     |     | OpenAI   | –       |     | 50+    | Proprietary |     |
Llama3.170BInstruct(Grattafiorietal.,2024) Meta 70 8 Llama3.1
|     | Llama3.18BInstruct(Grattafiorietal.,2024) |     |     |     | Meta   | 8   |     | 8    | Llama3.1     |     |
| --- | ----------------------------------------- | --- | --- | --- | ------ | --- | --- | ---- | ------------ | --- |
|     | CommandA(CohereTeametal.,2025)            |     |     |     | Cohere | 104 |     | 23   | CC-BY-NC-4.0 |     |
|     | AyaExpanse32B(Dangetal.,2024)             |     |     |     | Cohere | 32  |     | 23   | CC-BY-NC-4.0 |     |
|     | Gemma327BInstruct(GemmaTeametal.,2025)    |     |     |     | Google | 27  |     | 100+ | Gemma        |     |
|     | Gemma312BInstruct(GemmaTeametal.,2025)    |     |     |     | Google | 12  |     | 100+ | Gemma        |     |
|     | Gemma34BInstruct(GemmaTeametal.,2025)     |     |     |     | Google | 4   |     | 100+ | Gemma        |     |
|     | IBMGranite4.0(GraniteTeam,IBM,2025)       |     |     |     | IBM    | 3   |     | 116  | Apache2.0    |     |
|     | IBMGraniteMicro(GraniteTeam,IBM,2025)     |     |     |     | IBM    | 0.4 |     | 116  | Apache2.0    |     |
Table7: Teachermodeldetails. Weevaluate10teachermodelsacrossdifferentproviders, sizes,multilingual
capabilities,andlicensingterms. Sizeisreportedinbillionsofparameters(B)whereavailable. #Langsindicates
thenumberoflanguagesthemodelwastrainedonorevaluatedfor.
PG-SCORE when using family-matched teacher- minehowmuchsyntheticdataisneededtoreliably
| studentpairscomparedtotheOLMo37Bbaseline |                                   |     |     |     | compute | PG-SCORE. |     |     |     |     |
| ---------------------------------------- | --------------------------------- | --- | --- | --- | ------- | --------- | --- | --- | --- | --- |
| (see§3.2).                               | Table15showsthepercentageincrease |     |     |     |         |           |     |     |     |     |
in PG-SCOREwhenusingthebestdatageneration Setup We finetune an OLMo 3 7B base
methodforeachteacher-languagepaircompared model on n SFT instances where n
∈
toanequalmixbaseline(see§3.3). 1k,5k,10k,25k,50k . Toreducecomputational
|     |     |     |     |     | {   |     |     | }   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
costs,weperformthisexperimentonlyonasingle
G AdditionalExperimentsandAblations teacher model (Gemma 3 27B Instruct) on three
targetlanguagesthatrepresentdiversescriptsand
Inthissection,weablateseveralaspectsofoureval-
|     |     |     |     |     | resourceavailability: |     |     | Arabic,German,andIndone- |     |     |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | ------------------------ | --- | --- |
uationprotocolthatmayaffectateachermodel’s
|     |     |     |     |     | sian. | Similartothemainexperiments,werepresent |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --------------------------------------- | --- | --- | --- | --- |
PG-SCORE.
eachdatagenerationmethodequallywhencreating
|     |     |     |     |     | theSFTdatasets. |     |     | Then,werecomputetheintrinsic |     |     |
| --- | --- | --- | --- | --- | --------------- | --- | --- | ---------------------------- | --- | --- |
G.1 EffectofDataScaleonStudentModel
metricsandfinetunestudentmodelsandmeasure
Performance
theirperformanceacrossthreebenchmarks(§2.3).
OnecomponentofPG-SCOREistheextrinsicstu-
dent performance metric (§2.3) as measured by Results Figure 5 shows the average student
PGR.Scalinglawssuggestthatthisperformance model performance as a function of the number
improves with more data (Kaplan et al., 2020). of SFT instances. We observe that student per-
Then,itispossibletoinflatePG-SCOREbysimply formanceimproveswithmoresyntheticdata,but
usingmoresyntheticdata. Inordertocontrolfor gainsdiminishbeyond10kexamples. Thisfinding
this variable, we conduct an experiment to deter- suggests that using 10k synthetic examples per
17

Language Family Script ResourceAvailability %inCC
Arabic Afro-Asiatic Arabic 5(High) 0.65%
Czech Indo-European Latin 4(Medium-High) 0.99%
German Indo-European Latin 5(High) 6.01%
Spanish Indo-European Latin 5(High) 4.37%
Indonesian Austronesian Latin 3(Medium) 0.95%
Japanese Japonic Japanese 5(High) 5.20%
Table8: Targetlanguagedetails. Weevaluateteachermodelsacrosssixtypologicallydiverselanguagesspanning
differentlanguagefamiliesandscripts. ResourceavailabilityisbasedontheclassificationfromJoshietal.(2020),
rangingfrom0(lowest)to5(highest). CommonCrawlpercentages(Raffeletal.,2020)indicatetheproportionof
webtextavailableforeachlanguage.
0.65
0.60
0.55
0.50
0.45
103 104
Num. samples,log
ecnamrofrePlaugnilitluM
.gvA
Instruct, Aya Expanse 32B, Llama 30B Instruct)
andall6targetlanguages.
Results Table 16 shows the PG-SCORE scores
forthreeteachermodelswhenusingOLMo332B
asthestudentmodel. WefindthatGemma327B
Instructremainsthehighest-scoringteacherin
this comparison, achieving the highest average
PG-SCORE of 0.805 across all languages. This
resultisconsistentwithourfindingsusingthe8B
student model (§3), demonstrating that the supe-
riordataqualitygeneratedbyGemma327Bgen-
eralizes across model scales. Aya Expanse 32B
achieves a positive average PG-SCORE of 0.227,
while Llama 3.1 70B Instruct shows a negative
Arabic German Indonesian averageof 0.267.
−
Furthermore, the language-dependent effects
Figure 5: Effect of synthetic data scale on student observedinthe8Bexperimentsremainconsis-
model performance. Student performance improves tentat32Bscale. Germancontinuestoshowthe
withmoresyntheticdata,butgainsdiminishbeyond10k
highest PG-SCORE values across all three teach-
examples.
ers (2.389 for Gemma, 1.979 for Aya, 0.838 for
Llama), suggesting that certain languages bene-
language is sufficient to reliably compute PG- fitmorefromsyntheticdataregardlessofstudent
SCORE withoutinflatingthemetricbyincreas- modelsize. Similarly,Spanishexhibitsstrongper-
ing the number of samples. In our experiments, formanceacrossallteachers,with PG-SCOREval-
weuse10ksyntheticexamplesperlanguagewhen uesrangingfrom1.353to1.855. Incontrast,Ara-
computing PG-SCORE. Specifically,weshowthat bicshowsthemostvariableresults,withGemma
10ksyntheticexamplesfromastrongteacherare achievingslightlynegativescores( 0.239)while
−
sufficienttofinetuneastudentmodeltoachieverea- Aya and Llama show substantially lower perfor-
sonableperformanceacrossmultiplebenchmarks. mance( 0.872and 1.688,respectively). Overall,
− −
these findings demonstrate that PG-SCORE and
G.2 GeneralizationAcrossModelSize teacher model rankings generalize to the 32B pa-
rameterrange.
Setup Inordertotestwhether PG-SCORE gen-
eralizesbeyond8Bparametersizemodels,weuse
G.3 EffectofTranslationMethod(Prompting
anOLMo32Bbasemodel(S )andrecomputethe
ϕ
anLMvs. TranslationModel)
intrinsic and extrinsic metrics to obtain the PG-
SCORE. Tosavecomputationalcosts,wetrainstu- AnalternativetousinganLMfortranslatingtexts
dentmodelsacrossthreeteachers(Gemma327B fromEnglishtoatargetlanguageisviaatranslation
18

|       |     |     |     | Arabic(ar) |     |     | Czech(cs) |     |     | German(de) |       |
| ----- | --- | --- | --- | ---------- | --- | --- | --------- | --- | --- | ---------- | ----- |
| Model |     |     | d   | d          | PPL | R   | d d       | PPL | R d | d          | PPL R |
|       |     |     | x   | y          |     |     | x y       |     | x   |            | y     |
GPT4omini 0.704 0.869 8.40 3.516 0.643 0.862 3.18 3.716 0.732 0.889 3.65 3.810
Llama3.170BInst. 0.701 0.875 7.00 2.719 0.654 0.889 3.18 3.327 0.707 0.892 3.22 3.396
Llama3.18BInst. 0.708 0.779 6.2e4 1.731 0.673 0.799 2.7e4 1.908 0.738 0.873 3.6e3 2.513
CommandA 0.690 0.846 5.41 3.996 0.647 0.865 3.24 4.184 0.730 0.889 3.59 4.235
AyaExpanse32B 0.693 0.888 4.34 3.964 0.650 0.884 3.15 4.133 0.700 0.902 3.44 4.140
Gemma327BInst. 0.717 0.890 4.40 3.932 0.675 0.885 3.77 4.342 0.731 0.898 3.96 4.260
Gemma312BInst. 0.721 0.864 4.43 3.774 0.676 0.882 3.88 4.266 0.751 0.899 4.06 4.203
Gemma34BInst. 0.728 0.869 5.52 3.470 0.682 0.883 3.87 4.127 0.744 0.898 3.96 4.103
IBMGranite4.0 0.704 0.829 1.9e4 2.463 0.665 0.862 5.29 3.158 0.717 0.885 24.61 3.365
IBMGraniteMicro 0.741 0.863 12.45 3.033 0.713 0.874 4.61 3.568 0.726 0.892 4.59 3.704
|       |     |     |     | Spanish(es) |     |     | Indonesian(id) |     |     | Japanese(ja) |           |
| ----- | --- | --- | --- | ----------- | --- | --- | -------------- | --- | --- | ------------ | --------- |
| Model |     |     | d x | d y         | PPL | R   | d x d y        | PPL | R d | x            | d y PPL R |
GPT4omini 0.729 0.887 3.78 3.883 0.728 0.854 5.50 3.656 0.736 0.880 5.81 3.639
Llama3.170BInst. 0.728 0.892 3.15 3.434 0.727 0.874 4.85 3.293 0.756 0.799 4.52 2.459
Llama3.18BInst. 0.744 0.898 503.0 2.860 0.738 0.863 1.1e3 2.599 0.759 0.796 5.4e4 1.806
CommandA 0.733 0.884 3.77 4.336 0.747 0.857 4.94 3.899 0.739 0.881 4.92 4.174
AyaExpanse32B 0.724 0.893 3.67 4.181 0.726 0.879 4.43 4.017 0.743 0.883 5.96 3.821
Gemma327BInst. 0.768 0.903 4.30 4.266 0.740 0.854 5.49 4.057 0.765 0.875 5.90 3.956
Gemma312BInst. 0.763 0.895 4.14 4.193 0.762 0.851 5.84 3.958 0.756 0.885 5.78 4.017
Gemma34BInst. 0.754 0.887 4.52 4.021 0.760 0.851 6.46 3.657 0.794 0.875 6.45 3.656
IBMGranite4.0 0.743 0.882 5.22 3.309 0.729 0.833 16.80 2.437 0.761 0.849 9.79 2.889
IBMGraniteMicro 0.729 0.887 4.58 3.779 0.760 0.860 11.92 3.113 0.764 0.877 7.22 3.295
Table11: Fullintrinsicevaluationresultsacrossalllanguages. Dataqualitymetricsincludethediversityof
promptsandresponses(d P andd R ),averageperplexityofthestudentmodelontheresponse(PPL),andaverage
rewardscorebasedonamultilingualLLMjudge(R).
modelsuchasNLLB(NLLBTeametal.,2022). In syntheticdatasettocompute PG-SCORE.
thissection,weexaminetheeffectofthetranslation
methodonthe PG-SCOREofteachermodels. Results Figure6showsthePG-SCOREandaver-
agebenchmarkperformanceofthestudentmodel
| Setup |        |     |        |     |            |     | for each | translation | method | across | Arabic, Ger- |
| ----- | ------ | --- | ------ | --- | ---------- | --- | -------- | ----------- | ------ | ------ | ------------ |
|       | First, | we  | filter | and | sample 10k | En- |          |             |        |        |              |
glish prompt-response pairs from the Tülu 3 man, andIndonesian. WefindthatLM-Translate
SFT dataset.4 Then, using the NLLB model outperformsbothNLLB-basedapproaches,achiev-
(nllb-200-distilled-600M), ing an average PG-SCORE of 1.36 compared to
|     |     |     |     |     | we perform | two |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
translation methods: (1) NLLB-Translate-then- 0.85forNLLB-Translate-Bothand0.80forNLLB-
Respond: translatethepromptstoeachtargetlan- Translate-then-Respond. Thispatternholdsacross
allthreelanguages,withthelargestgapobserved
guageandpromptGemma327BInstructtogener-
atearesponse,and(2)NLLB-Translate-Both: trans- forGerman(2.09vs1.26/1.68).
lateboththepromptsandresponsesfromEnglishto Ourfindingssuggestthatpromptnaturalness,
thetargetlanguage. Wechoosethe600Mversion ratherthanresponsequality,isabottleneckin
|     |     |     |     |     |     |     | translation-basedpipelines: |     |     | havinganLMgen- |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | -------------- | --- |
duetoitscomputationalefficiencyandpopularity
amongpractitioners,asmeasuredbyHuggingFace erate responses to NLLB-translated prompts pro-
downloadsandcommunitylikes. videsnoimprovementoverpureNLLBtranslation
Wecomparethesemethodsagainstouroriginal (0.80 vs 0.85), indicating that translated prompts
failtoelicitthesamequalityofresponsesasLM-
Translatemethod,i.e.,promptingGemma327BIn-
| structtodirectlytranslatethepromptandgenerate |     |     |     |     |     |     | translatedprompts. |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
theresponseinthetargetlanguage(LM-Translate).
|     |     |     |     |     |     |     | G.4 | WeighingofIntrinsicandExtrinsic |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- |
Then,wecomputetheintrinsicdataqualitymetrics
|     |     |     |     |     |     |     |     | Metricsin | PG-SCORE |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --- |
andfinetuneOLMo37Bstudentmodelsoneach
|       |     |               |     |             |          |         | Our PG-SCORE |     | formulationusesanassumption- |     |     |
| ----- | --- | ------------- | --- | ----------- | -------- | ------- | ------------ | --- | ---------------------------- | --- | --- |
| 4Tülu | 3   | also contains |     | non-English | data. We | perform |              |     |                              |     |     |
freeandequalweighingschemebetweentheintrin-
English-languagefilteringusingfastText(Joulinetal.,2016,
2017)andthestaticvectorslibrary. sic ( ) and extrinsic ( ) metrics. In this section,
|     |     |     |     |     |     |     | I   |     | E   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
19

Model Arabic(ar) Czech(cs) German(de) Spanish(es) Indonesian(id) Japanese(ja)
GPT4omini -2.086 0.538 3.098 1.395 2.025 0.099
Llama3.170BInst. -1.528 0.538 2.265 1.075 0.329 0.013
Llama3.18BInst. -0.841 0.525 2.623 0.595 1.425 0.236
CommandA -2.476 0.505 2.759 1.613 1.863 0.841
AyaExpanse32B -0.293 0.538 2.491 1.701 1.943 0.221
Gemma327BInst. -0.074 0.552 2.635 1.724 0.198 0.677
Gemma312BInst. -1.015 0.538 2.700 1.592 -0.017 0.524
Gemma34BInst. -1.033 0.538 2.568 1.209 -0.388 0.349
IBMGranite4.0 1.565 0.538 2.061 1.235 0.614 0.802
IBMGraniteMicro -0.421 0.538 1.842 1.203 -0.659 0.210
Table12: Averageperformancegainrecovered(PGR)ofastudentmodelacrossvariousmultilingualbench-
marks. Our multilingual evaluation suite includes Global-MMLU Lite (Singh et al., 2025), M-RewardBench
(Gurejaetal.,2025), andM-GSM(Shietal.,2023). ThePGRcomputationisbasedonKimetal.(2025)and
detailedin§2.3(Equation2)whereS =OLMo37BInstructSFTandS =OLMo310257B.
REF ϕ
Model Arabic(ar) Czech(cs) German(de) Spanish(es) Indonesian(id) Japanese(ja)
Gemma327BInst. 0.145(0.0121) 0.360(0.0004) 1.655(0.0141) 1.358(0.0141) 0.214(0.0167) 0.626(0.0124)
AyaExpanse32B -0.058(0.0116) 0.222(0.0004) 1.468(0.0134) 1.129(0.0123) 1.153(0.0124) 0.320(0.0111)
Gemma312BInst. -0.464(0.0119) 0.327(0.0004) 1.756(0.0137) 1.228(0.0140) 0.151(0.0126) 0.573(0.0142)
CommandA -1.360(0.0112) 0.114(0.0004) 1.673(0.0139) 1.102(0.0145) 1.063(0.0125) 0.683(0.0122)
Gemma34BInst. -0.488(0.0119) 0.330(0.0004) 1.644(0.0137) 0.929(0.0140) -0.105(0.0126) 0.504(0.0113)
GPT4omini -1.117(0.0117) 0.015(0.0004) 1.766(0.0136) 0.908(0.0149) 1.003(0.0125) 0.189(0.0117)
IBMGranite4.0 -0.072(0.0123) -0.031(0.0004) 1.000(0.0135) 0.734(0.0151) -0.079(0.0125) 0.321(0.0108)
IBMGraniteMicro -0.282(0.0121) 0.290(0.0004) 1.102(0.0139) 0.783(0.0133) -0.329(0.0126) 0.264(0.0121)
Llama3.170BInst. -0.964(0.0117) 0.109(0.0004) 1.195(0.0146) 0.688(0.0146) 0.182(0.0126) -0.373(0.0116)
Llama3.18BInst. -1.693(0.0120) -0.974(0.0004) 0.891(0.0148) 0.182(0.0164) 0.322(0.0124) -0.863(0.0129)
Table13: DetailedresultsfromTable1withstandarderrors. Wecompute PG-SCORE thricewithdifferent
synthetically-generateddata(eachtrialusesadifferentdatamixbasedonarandomseed). Wereportthemeanand
standarderrorforeachteachermodelacrossalltargetlanguages. Foreachlanguage,wehighlightthebestmodelin
boldandthesecond-bestmodelwithanunderline.
BaseModel(S ) betweentheintrinsicandextrinsicmetricsacross
ϕ
allteacher-languagepairs(N=60,10models 6
TeacherModel Gemma34BLlama3.18B ×
languages). Inaddition,inordertotesttheeffect
Llama3.170BInst. +362.3% +260.1% of weighing one metric against the other, we for-
Llama3.18BInst. +183.1% +130.0% mulateageneralizedversionof PG-SCORE:
Gemma327BInst. +20.5% +26.5%
Gemma312BInst. +38.5% +67.2% PG-SCORET,ℓ = α +(1 α)
I − E (4)
Gemma34BInst. +103.4% +203.4% where0 α 1
≤ ≤
Table 14: Percentage increase in PG-SCORE for Notethattheexperimentsin§3and§4assume
family-matched teacher-student pairs. Percentage α = 0.5. We compute the PG-SCORE across
increasewhenusingfamily-matchedteacherscompared α = 0.00,0.25,0.50,0.75,1.00 and then test
toOLMo37Bbaseline(averageacrossArabic,German, { }
theresultingmodelranks’ρacrossallpairsofα.
andIndonesian).
Weperformthisexperimentonallteacher-language
pairswherestudentsarefinetunedfromtheOLMo
wetestwhetherthesetwometricscapture(1)com- 37Bbasemodel(N=30,10models 6languages).
×
plementaryaspectsofteachereffectivenessand(2)
Results Intrinsic and extrinsic metrics show a
howmodelrankingsdifferifonemetricisweighted
moderatepositivecorrelation(Spearmanρ=0.41,
morethantheother.
p < 0.01), suggesting that data quality metrics
Setup In order to test whether each metric cap- arepredictiveofstudentperformancewhilecap-
turescomplementaryaspectsofteachereffective- turingcomplementaryinformation. Thisfinding
ness,wecomputetheSpearmanrankcorrelation(ρ) motivatesourcombined PG-SCORE computation.
20

|     |                |            |           |         | TeacherModel(S |         | T,ℓ)        |        |     |     |     |
| --- | -------------- | ---------- | --------- | ------- | -------------- | ------- | ----------- | ------ | --- | --- | --- |
|     | Language       | BestMethod | Gemma327B |         | AyaExpanse32B  |         | Llama3.170B |        |     |     |     |
|     | Arabic(ar)     | Respond    |           | +453.1% |                | +355.2% |             | +77.7% |     |     |     |
|     | German(de)     | Generate   |           | +29.3%  |                | +0.3%   |             | +16.4% |     |     |     |
|     | Indonesian(id) | Translate  |           | +458.9% |                | +39.3%  |             | −14.8% |     |     |     |
Table15: PercentageincreaseinPG-SCOREforbestdatagenerationmethod. Percentageincreasewhenusing
thebest-performingdatagenerationmethodcomparedtoanequalmixbaselineofallthreemethods(Generate,
Translate,Respond). Forless-resourcedlanguages(ArabicandIndonesian),usingTranslateorRespondmethods
yieldssubstantialimprovementsformostteachers,thoughgainsareteacher-dependent.
TeacherModel Average Arabic(ar) Czech(cs) German(de) Spanish(es) Indonesian(id) Japanese(ja)
| Gemma327BInst. | 0.805 | -0.239 | 0.222  |     | 2.389 | 1.855 |     | 0.239  |     | 0.366  |     |
| -------------- | ----- | ------ | ------ | --- | ----- | ----- | --- | ------ | --- | ------ | --- |
| AyaExpanse32B  | 0.227 | -0.872 | -0.038 |     | 1.979 | 1.353 |     | -0.249 |     | -0.809 |     |
Llama3.170BInst. -0.267 -1.688 -0.807 0.838 1.407 -1.441 0.089
Table16: PG-SCOREofthreeteachermodels(S ϕ =OLMo332B)Weshowthatourfindingsgeneralizeupto
the32Bparameterrangeonthethreeteachermodelswetested: (1)Gemma327Bmaintainsitspositionasthe
mosteffectiveteacher,andthe(2)language-dependenteffectsarestillapparentwithGermanhavingthehighest
PG-SCOREsacrossmostteachers.
Inaddition,teacherrankingsarestablefornearby but it provides empirical evidence of a structural
weighting schemes (ρ 0.90 for adjacent α val- gapthatinhibitsqualitysyntheticdatageneration
≥
ues) as shown in Figure 7. Our finding suggests forlong-taillanguages. Incontrast,wedonotfind
thatmodelrankingsarerobusttosmallchanges a significant correlation between resource avail-
in the weighing of intrinsic and extrinsic met- abilityandPG-SCORE(ρ =0.372,p =0.468).
Our
rics. Ourequalweighting(α = 0.5)balancesboth findingssuggestthatteachermodelgenerationqual-
perspectives, correlating strongly with extrinsic- itydependsmoreheavilyonpretrainingexposure
focused(ρ = 0.89)andreasonablywithintrinsic- than linguistic resources. Additionally, the data
focused(ρ = 0.74)rankings. sourcesfromJoshietal.(2020)donotreflectthe
|     |     |     |     |     | currentlandscape: |     | recentLMsaretrainedoneither |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | --------------------------- | --- | --- | --- | --- |
G.5 Effectoflanguageresourcelevelson
|          |     |     |     |     | publicly-available |           | datasets | from | HuggingFace |          | or    |
| -------- | --- | --- | --- | --- | ------------------ | --------- | -------- | ---- | ----------- | -------- | ----- |
| PG-SCORE |     |     |     |     | in-house           | datasets. | While    | our  | work        | includes | 6 di- |
verselanguages,thesamplesizeremainslimited;
Setup Foreachlanguage,weconsiderthefollow-
weencouragefutureworktoexpandthenumberof
| ing properties | drawn from | prior | work: Common- |     |     |     |     |     |     |     |     |
| -------------- | ---------- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Crawl(CC)percentageasaproxyforpresencein languagestovalidatethesefindings.
pretrainingdata(%inCC,Raffeletal.,2020),and
|     |     |     |     |     | H DisclosureontheUseofLLMs |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
linguisticresourceavailability(scorefrom1–5,5
ashigh-resource,obtainedfromtheLDCCatalog We used Claude (Anthropic, 2024) to assist with
| andtheELRAMap,Joshietal.,2020). |     |     | Wecom- |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
editing,titleideation,andproofreadingportionsof
| pute the Spearman | rank | correlation | (ρ) between |     |           |                                       |     |     |     |     |     |
| ----------------- | ---- | ----------- | ----------- | --- | --------- | ------------------------------------- | --- | --- | --- | --- | --- |
|                   |      |             |             |     | thiswork. | Allscientificclaimsandinterpretations |     |     |     |     |     |
each property and PG-SCORE across all teacher- are solely our own. We reviewed and revised all
| languagepairs(N=60,10models |     |     | 6languages). |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
LLM-assistedtext.
×
| Results Figure8showstherelationshipbetween |     |     |     |     |                                    |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
|                                            |     |     |     |     | I MultilingualSyntheticDataRecipe: |     |     |     |     |     |     |
alanguage’spercentageinCommonCrawlandPG-
CaseStudyonTagalog
SCORE. Weobserveasuggestivepositivetrend
betweenCommonCrawlrepresentationandPG- Asanapplicationofourfindingsanddiscussionin
SCORE (ρ =0.886, p <0.05). This finding sug- §5,wepresentacasestudyondevelopingamulti-
geststhatlanguageswithgreaterpresenceinpre- lingualsyntheticdatarecipeonaheld-outlanguage:
training data enable teacher models to generate Tagalog. Itisamid-resourcelanguage(Category3
higher-quality synthetic data that leads to better inJoshietal.(2020)’staxonomy)andthestandard-
studentperformance. Thisfindingisunsurprising, izedformofFilipino,thenationallanguageofthe
21

GenerationParameters
|     | ModelName           |     |     |     | Temperature |     | Top-p | Top-k | MaxSeqLen |       |     |
| --- | ------------------- | --- | --- | --- | ----------- | --- | ----- | ----- | --------- | ----- | --- |
|     | GPT-4omini          |     |     |     |             | 0.8 | 0.9   | –     | 16,384    |       |     |
|     | Llama3.170BInstruct |     |     |     |             | 0.6 | 0.9   | –     | 131,072   |       |     |
|     | Llama3.18BInstruct  |     |     |     |             | 0.6 | 0.9   | –     | 131,072   |       |     |
|     | CommandA            |     |     |     |             | 0.3 | –     | –     | 128,000   |       |     |
|     | AyaExpanse32B       |     |     |     |             | 0.3 | –     | –     | 128,000   |       |     |
|     | Gemma327BInstruct   |     |     |     |             | 1.0 | 0.95  | 64    |           | 8,192 |     |
|     | Gemma312BInstruct   |     |     |     |             | 1.0 | 0.95  | 64    |           | 8,192 |     |
|     | Gemma34BInstruct    |     |     |     |             | 1.0 | 0.95  | 64    |           | 8,192 |     |
|     | IBMGranite4.0       |     |     |     |             | 0.0 | –     | –     |           | 4,096 |     |
|     | IBMGraniteMicro     |     |     |     |             | 0.0 | –     | –     |           | 4,096 |     |
|     | Default             |     |     |     |             | 0.8 | 0.9   | –     |           | –     |     |
Table 17: Inference settings for each teacher model. Generation parameters are based on model provider
recommendationsfromHuggingFaceand/orofficialdocumentation. TheDefaultrowindicatesparametersused
whenmodel-specificrecommendationsareunavailable. The“–”symbolindicatestheparameterwasnotspecified
intheofficialrecommendations.
| Philippines. |                           |     |     |     |     |     | Source        |     | Num. | Instances |     |
| ------------ | ------------------------- | --- | --- | --- | --- | --- | ------------- | --- | ---- | --------- | --- |
|              |                           |     |     |     |     |     | TaCoAlpaca    |     |      | 10,000    |     |
| I.1 Setup:   | RecipeDesignandEvaluation |     |     |     |     |     |               |     |      |           |     |
|              |                           |     |     |     |     |     | AyaCollection |     |      | 1,241     |     |
|              |                           |     |     |     |     |     | WildChat4.8M  |     |      |           | 997 |
Data WecollectFilipinoseeddatafromvarious
|     |     |     |     |     |     |     | WildChat1M |     |     |     | 250 |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
publicly-availableSFTdatasetssuchasWildChat
4.8MandtheAyaCollection. Inaddition,wealso Tagalogseeddatasetstatistics.
|     |     |     |     |     |     |     | Table18: |     |     |     | Inorderto |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --------- |
includeEnglishdatafromtheTülu3SFTdataset
bootstrapthesyntheticdatagenerationrecipeforTaga-
fortheTranslatemethod. Table18showsthestatis- log,wecurateaseeddatasetcontainingamixofTagalog
ticsoftheseeddatasetusedforTagalogsynthetic andEnglishpromptsfromvarioussources. Majorityof
datageneration. Then,weimplementthefollowing theseeddatasetisfromtheTaCopaper(Upadhayayand
| datainterventionsbasedonourfindings:     |             |          |           |                |           |     | Behzadan,2024).                            |     |          |      |           |
| ---------------------------------------- | ----------- | -------- | --------- | -------------- | --------- | --- | ------------------------------------------ | --- | -------- | ---- | --------- |
| Teacher                                  | Model:      |          |           |                |           |     |                                            |     |          |      |           |
| •                                        |             | we       | use Gemma | 3              | 27B       | In- |                                            |     |          |      |           |
| struct as                                | the teacher |          | model,    | as it was      | the best- |     |                                            |     |          |      |           |
|                                          |             |          |           |                |           |     | matchedteacher-studentpairsyieldhigher     |     |          |      | PG-       |
| performingmodelacrossmosttargetlanguages |             |          |           |                |           |     | SCORE(§3.2).                               |     |          |      |           |
| weevaluated(§3).                         |             |          |           |                |           |     | Forthepurposesofthisreport,wewilldesignate |     |          |      |           |
| • DataGenerationMethod:                  |             |          |           | weusetheTrans- |           |     |                                            |     |          |      |           |
|                                          |             |          |           |                |           |     | the model finetuned                        |     | on Gemma | 3 4B | using our |
| late and                                 | Respond     | methods, |           | as they        | were      | the |                                            |     |          |      |           |
syntheticrecipeas10K-Polyglot-TL,where“10K”
best-performingmethodsformid-resourcelan- indicatesthenumberofSFTinstancesusedduring
| guageslikeIndonesian(§3.3). |     |     |     | Inaddition,we |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
finetuning.
| add a small | sample |     | of prompt-response |     | pairs |     |     |     |     |     |     |
| ----------- | ------ | --- | ------------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
synthesizedviatheGeneratemethod. Evaluation WeevaluateonFILBENCH(Miranda
Synthetic Data Scale: et al., 2025), a benchmark for LMs that includes
| •   |     |     | we  | generate | 10k syn- |     |     |     |     |     |     |
| --- | --- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
theticexamplesusingtheselectedteacherand Filipino-centric multiple-choice and generative
data generation method, as we found that this tasks. It measures an LM’s performance across
scaleissufficienttoachievestrongstudentper- four categories such as classical NLP, cultural
formance (Appendix G.1). However, we also knowledge, reading comprehension, and genera-
test on finetuning a model with 25k synthetic tion,alongsideanaggregated FILBENCHscore.
examples to see if more data improves perfor- Wealsocompareagainsttwodatamixbaselines:
10K-Public:
| mance. |     |     |     |     |     |     | 1.  | we  | sample 10k | Tagalog | prompt- |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | ------- |
• Student Base Model: we finetune using the responsepairsfromtheseeddataset. Thisbase-
Gemma 3 4B model, as we find that family- line aims to simulate a non-synthetic data ap-
22

1.50
1.25
1.00
0.75
0.50
0.25
0.00
NLLB NLLBTranslate LMTranslate
TranslateBoth thenRespond
erocS-GPegarevA
1.36
0.85
0.80
2.0
1.5
1.0
0.5
0.0
NLLB NLLBTranslate LMTranslate
TranslateBoth thenRespond
erocS-GP
Arabic
Indonesian 0.0 0.25 0.5 0.75 1.0
German
Figure 6: Effect of translation method on PG-
SCORE. We compare three methods: LM translates
promptEN-to-XXandresponds(LM-Translate),NLLB
translatespromptEN-to-XXandLMresponds(NLLB-
Translate-then-Respond), and NLLB translates both
promptandresponse(NLLB-Translate-Both).
proachtotrainingmultilingualLMs.
2. 10K-GPT-4oM: we synthesize 10k instances
usinganoff-the-shelfteachermodel(GPT-4o-
mini). This baseline simulates a typical data
generation approach of choosing a teacher in
anadhocmannerduetoitsperceivedstrength
(sizeorbenchmarkperformance)oreaseofuse.
Forallmethods,wefinetuneaGemma34Bbase
modelusingthesametrainingsettingsindicatedin
AppendixE.1.
I.2 Results: LeaderboardScoresand
Ablations
Table 19 shows the FILBENCH score of our op-
timal synthetic recipe compared to other models
in the same parameter range. We find that 10K-
Polyglot-TLiscompetitiveagainst10K-GPT-4oM
(+1.85pp),andhasbetterperformancecomparedto
10K-Public(+2.28pp). Theseresultssuggestthat
(1)syntheticdatagenerationisaviableapproach
for building less-resource language models, and
(2)ourfindingthatselectingstrongteachermodels
basedonPG-scoreiseffective,aslargermodelsdo
0.0
52.0
5.0
57.0
0.1
*:p<0.05 **:p<0.01
1.00
0.97** 1.00
0.89** 0.96** 1.00
0.71** 0.82** 0.94** 1.00
0.41** 0.55** 0.74** 0.91** 1.00
0.6 0.8 1.0
Spearman rank ρ
Figure7: Effectofweighingintrinsicandextrinsic
metricsin PG-SCORE. Modelrankingsremainrela-
tivelystableacrossneighboringweightingsofintrinsic
andextrinsicmetrics.
notalwaysproducebettertrainingdata(§3).
In addition, comparing 10K-Polyglot-TL to
othermodelsintheFILBENCHleaderboard5shows
thattheformeriscompetitiveagainstQwen34B
andLlama3.18BInstruct. Wehighlightthatour
4B models are competitive against other mod-
elswithlargerparametersizes,suggestingthat
a multilingual synthetic data recipe based on our
PG-SCOREfindingsisdata-efficient. Wealsofind
thatincreasingthenumberofSFTinstances(10k
to 25k) led to a performance increase of 0.21pp.
While we previously found that 10K instances
showed diminishing returns (see Appendix G.1),
thecontinuedgainsfromscalingto25Kinstances
on FILBENCH suggestthatsaturationpointsmay
depend on task diversity. FILBENCH covers a
broader range of NLP tasks (e.g., named-entity
recognition)comparedtoourexperimentalbench-
marksin§3andAppendixG,indicatingthatprac-
titionersworkingwithdiversetaskdistributions
may benefit from exploring larger synthetic
datasetsbeyondthe10Kthreshold.
I.3 Analysis: AblationExperiments
In order to measure the contribution of our find-
ingsandrecommendationsin§5,weperformthe
following ablation experiments as shown in Fig-
ure9. Notethattheinterventionsdescribedbelow
5Official FILBENCH leaderboard: https://hf.co/
spaces/filbench/filbench-leaderboard
23

|     |     |                |     |     |     | Model |     |     |     | FILBENCHScore |     |     |
| --- | --- | -------------- | --- | --- | --- | ----- | --- | --- | --- | ------------- | --- | --- |
|     | ρ   | =0.886, p<0.05 |     |     |     |       |     |     |     |               |     |     |
4
|          |     |     |     |     |     | GPT-4o(2024-08-06) |     |     |     |     |     | 74.27 |
| -------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | ----- |
|          |     |     |     |     |     | Gemma327BInst.     |     |     |     |     |     | 55.17 |
| erocS-GP |     |     |     |     |     | Gemma312BInst.     |     |     |     |     |     | 54.04 |
2
|     |     |      |      |     |     | 25K-Polyglot-TL4B |     |     |     |     |     | 49.73 |
| --- | --- | ---- | ---- | --- | --- | ----------------- | --- | --- | --- | --- | --- | ----- |
|     |     |      |      |     |     | 10K-Polyglot-TL4B |     |     |     |     |     | 49.52 |
|     |     |      |      |     |     | Qwen34B           |     |     |     |     |     | 48.42 |
|     | 0   |      |      |     |     | 10K-GPT-4oM       |     |     |     |     |     | 47.67 |
|     |     |      |      |     |     | Llama3.18BInst.   |     |     |     |     |     | 47.38 |
|     |     |      |      |     |     | Ministral8BInst.  |     |     |     |     |     | 47.33 |
|     | <1% | 1–2% | 2–5% |     | >5% | 10K-Public        |     |     |     |     |     | 47.24 |
|     |     |      |      |     |     | Pangea7B          |     |     |     |     |     | 43.98 |
PercentageofaLanguage
|     |     | inCommonCrawl |     |     |     | SeaLLMs31.5B |     |     |     |     |     | 43.20 |
| --- | --- | ------------- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ----- |
Relationshipbetweenalanguage’spercent-
Figure8:
Table19: Modelperformanceonaheld-outlanguage
| ageinCommonCrawlandPG-SCORE. |     |     |     |     | Weobservea |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
(Tagalog)asevaluatedonFILBENCH(Mirandaetal.,
suggestivepositivetrend(ρ=0.886,p<0.05)between
|     |     |     |     |     |     | 2025). | We  | compare | ouroptimalsyntheticrecipe |     |     |     |
| --- | --- | --- | --- | --- | --- | ------ | --- | ------- | ------------------------- | --- | --- | --- |
CommonCrawlrepresentationandPG-SCOREacross
thesixlanguagestested. against baselineapproaches and other models in the
sameparameterrange.
areadditive.
|          |     |                       |     |      |          | 4Bbasemodel. |     | Thisinterventionyieldsasubstan- |     |     |     |     |
| -------- | --- | --------------------- | --- | ---- | -------- | ------------ | --- | ------------------------------- | --- | --- | --- | --- |
| Curation |     | of publicly-available |     | data | vs. Syn- |              |     |                                 |     |     |     |     |
tialperformanceimprovement,demonstratingthat
| theticdatageneration |     |     | Wecomparestudentmod- |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
familyalignmentisareliableheuristicforteacher
elstrainedon(1)publicly-availableTagalogSFT selection. Theimprovementfromfamilymatching
data and (2) synthetic SFT instances generated isconsistentwithourfindingsthatfamily-matched
| by a | GPT-4o    | teacher (note | that | these | are also the |               |     |          |        |        |          |     |
| ---- | --------- | ------------- | ---- | ----- | ------------ | ------------- | --- | -------- | ------ | ------ | -------- | --- |
|      |           |               |      |       |              | pairs achieve |     | at least | +20.5% | higher | PG-SCORE |     |
| same | baselines | in Appendix   |      | I.2). | We find that |               |     |          |        |        |          |     |
comparedtomismatchedpairs,likelyduetoshared
theperformanceofthesetwobaselinesaresimilar tokenization schemes and architectural similari-
(∆ = 0.5pp),
suggesting that there is no signifi- tiesthatfacilitatebetterknowledgetransferfrom
| cant | advantage | to using | a synthetic |     | data pipeline |     |     |     |     |     |     |     |
| ---- | --------- | -------- | ----------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
teachertostudent.
| if the    | teacher | model is                 | not optimal. |     | We also hy- |          |      |       |     |          |     |        |
| --------- | ------- | ------------------------ | ------------ | --- | ----------- | -------- | ---- | ----- | --- | -------- | --- | ------ |
|           |         |                          |              |     |             | Increase | data | scale | We  | increase | the | number |
| pothesize | that    | some publicly-accessible |              |     | datasets    |          |      |       |     |          |     |        |
in Tagalog were semi-synthetic (e.g., TaCO uses of synthetic instances from 10k to 25k to assess
whetheradditionaldatacontinuestoimproveper-
asyntheticpipelineakintotheTranslatemethod,
|     |     |     |     |     |     | formance. | We  | observe | a   | modest | gain | of 0.21pp, |
| --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --- | ------ | ---- | ---------- |
butusingchain-of-thoughttoimprovethequality
|     |     |     |     |     |     | which | is smaller | than | the | improvements |     | from |
| --- | --- | --- | --- | --- | --- | ----- | ---------- | ---- | --- | ------------ | --- | ---- |
oftranslations),makingitdifficulttoperformafair
| comparison. |     |     |     |     |     | teachermodelselectionandmodelfamilymatch- |         |        |      |     |         |          |
| ----------- | --- | --- | --- | --- | --- | ----------------------------------------- | ------- | ------ | ---- | --- | ------- | -------- |
|             |     |     |     |     |     | ing. This                                 | finding | aligns | with | our | earlier | observa- |
Usingateacherwithahigher PG-SCORE We tionthatgainsdiminishbeyond10kexamples(Ap-
thenswaptheGPT-4o-miniteacherwithAyaEx-
pendixG.1),thoughthecontinuedimprovementon
panse 32B, a teacher with a higher PG-SCORE FILBENCH’sdiversetaskdistributionsuggeststhat
based on our main findings (0.461 vs. 0.706, c.f. saturationpointsmaybetask-dependent.
| §3, Table |     | 1). We observe | a   | slight | performance |          |       |       |     |          |     |         |
| --------- | --- | -------------- | --- | ------ | ----------- | -------- | ----- | ----- | --- | -------- | --- | ------- |
|           |     |                |     |        |             | Increase | model | scale |     | Finally, | we  | explore |
improvementinthisintervention,suggestingthat
whetherscalingthestudentmodelfrom4Bto12B
| the PG-SCORE |     | metric | is generalizable |     | across an |           |            |     |          |            |     |         |
| ------------ | --- | ------ | ---------------- | --- | --------- | --------- | ---------- | --- | -------- | ---------- | --- | ------- |
|              |     |        |                  |     |           | (and 27B) | parameters |     | provides | additional |     | perfor- |
unseenlanguage.
|     |     |     |     |     |     | mancegains. | Wefindthatthelargerstudentmodel |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------- | ------------------------------- | --- | --- | --- | --- | --- |
Matching teacher and student model families achieves higher performance, demonstrating that
Oneofourkeyfindingsandrecommendationisto our synthetic data recipe benefits from increased
match the model families of the teacher and the modelcapacity. Thisresultisconsistentwithour
student (§3.2). We use a Gemma 3 Instruct 27B generalizationexperiments(AppendixG.2),where
teachermodeltomatchthefamilyoftheGemma3 weshowedthat PG-SCORE generalizesacrossdif-
24

|     |     | EROCS |           |            |                |            | + S c ale            | s i ze + S c a les i z e |
| --- | --- | ----- | --------- | ---------- | -------------- | ---------- | -------------------- | ------------------------ |
|     |     |       | + U se    | sy nthetic | + B e tt e r + | M a t ch + | S c a le d a ta      |                          |
|     |     | 75    |           |            | fa             | m il y (1  | 0 k → 2 5 k ) (4 B → | 1 2 B ) (1 2 B → 2 7 B ) |
|     |     |       | pi pe lin | e          | te ac h e r    |            |                      |                          |
51.4 53.0
|     |     | 50  | 47.2 | 47.7 | 48.2 | 49.5 | 49.7 |     |
| --- | --- | --- | ---- | ---- | ---- | ---- | ---- | --- |
HCNEBLIF
25
0
|     |     |     | None | GPT-4o | AyaExp  | ——–Gemma327B——– |       |     |
| --- | --- | --- | ---- | ------ | ------- | --------------- | ----- | --- |
|     |     |     |      |        |         | |               |       | |   |
|     |     |     |      |        | Teacher |                 | Model |     |
Studentmodelperformanceonaheld-outlanguage(Tagalog)acrossseveralsyntheticdatainterven-
Figure9:
tions. Givenaheld-outlanguage(Tagalog)andanevaluationbenchmark(FILBENCH),weapplydatainterventions
basedonourrecommendationsoncreatingamultilingualsyntheticdatarecipe(§5).
| ferent model            | sizes | while                        | maintaining        | the   | relative  |     |     |     |
| ----------------------- | ----- | ---------------------------- | ------------------ | ----- | --------- | --- | --- | --- |
| rankingofteachermodels. |       |                              | However,wenotethat |       |           |     |     |     |
| the performance         |       | of our                       | best models        | are   | still be- |     |     |     |
| hind Gemma              | 3 27B | Instruct                     | and                | Gemma | 3 12B     |     |     |     |
| Instruct(Table19).      |       | Giventhatobservation,westill |                    |       |           |     |     |     |
arguethatoursyntheticpipeline,whichuses25K
instancestrainedonlyviaSFT,canbeconsidered
| data and | resource-efficient |     | compared | to  | the post- |     |     |     |
| -------- | ------------------ | --- | -------- | --- | --------- | --- | --- | --- |
traininginterventionsdoneinGemma3,whichin-
volvedinstruction-tuningandreinforcementlearn-
ingobjectives(GemmaTeametal.,2025).
J InferenceDetails
| Prompttemplates |     | Figure10toFigure12show |     |     |     |     |     |     |
| --------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
theprompttemplatesusedforeachdatageneration
| method. Inaddition,Figure13showstheprompt |     |     |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
templateusedfortheLLM-as-a-judgemethodto
evaluatetextquality.
| Inferencesettings |     | WeusevLLM(Kwonetal., |     |     |     |     |     |     |
| ----------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
2023)andCurator(Martenetal.,2025)forinfer-
| ence. Foreachteachermodel, |     |     | wecheckwhether |     |     |     |     |     |
| -------------------------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
themodelproviderrecommendedbestsettingsfor
| usage. If         | not, then | we set      | a default | configuration |        |     |     |     |
| ----------------- | --------- | ----------- | --------- | ------------- | ------ | --- | --- | --- |
| (temperature=0.8, |           | top_p=0.9). | Table     | 17            | summa- |     |     |     |
rizestheinferencesettingsweusedforeachteacher
model.
25

Generate:samplekprompt-responsepairsfromD seed,ℓanduseitasin-contextexamples
Asamultilingualdatagenerator,yourtaskistogenerateanewexample(‘prompt‘and‘response‘)fora
datasetdemonstratinghowAIagentscanfulfillgeneralinstructionsfor{lang_name}.
Todothis,youwillwanttogeneratetwopiecesofinformation:
1)A"prompt"specifyingatasktobecompletedoraquestiontobeanswered(what,where,when,how,who,
why).Thetaskshouldbeverychallengingyetsolvable.
2)A"response"representingavalidcompletionofthattaskinnaturallanguage. Ifthe"response"doesnot
satisfythe"prompt", thenyouhavefailedatyourjob. Donotprovideunnecessarydetails, beyondwhatis
explicitlyneededtosatisfytheinstructionyougenerated.
Hard constraint: The generated task MUST belong to exactly one of the following categories (pick
oneatrandomanddoNOTmentionthecategory).
1.Logicalreasoning/erroranalysis
2.Mathorquantitativereasoningwithexplanation
3.Classificationorlabeling
4.Dialogueorrole-play
5.Translationorparaphrasingwithconstraints
6.Proceduralinstructions(step-by-step)
7.Grammarcorrectionorlinguisticanalysis
8.Short-formcreativeoutput(≤50words)
9.Knowledgerecallwithverificationorcorrection
10.Culturalorpragmaticjudgment
Add diversity to your generations by varying the types of tasks you create, the styles and tones of the
responses,andthecomplexityofthelanguageused.Thiswillhelpensurearichandvarieddataset.Forexample,
youmightcreatetasksthatinvolveansweringknowledge-basedquestions,answeringmathquestions,providing
explanations,generatingcreativecontent,orperformingtranslations.
Please provide a JSON dictionary response that includes the new ‘prompt‘ and its corresponding
‘response‘.Usethe‘prompt‘and‘response‘keysinthedictionary.
Donotgenerateanyothertextinyourresponse(forexample,donotstartyourmessagewithanygreetings,and
neveraskforclarificationorapologizeforstrugglingwiththetask).
Tryyoubesttoensurethattheinputandresponseyougeneratearedistinctfromtheprovidedexampleswhile
maintainingadiverse,detailed,precise,comprehensive,andhigh-qualityresponse.
Itisimportanttogenerateresponsesthatarecontextuallyrelevantandculturallyappropriatefor{lang_name}.
Here are some examples to guide your generation. The best way to use these examples is to identify
thepatternsandstructurestheyfollow,ratherthancopyingthemdirectly:
{% for example in examples[:k] %}
Prompt: {{example[“prompt”]}}
Response: {{example[“response”]}}
{% endfor %}
NewExample:
Figure10: PrompttemplatefortheGeneratedatagenerationmethod.
26

Translate: forward-translateEnglishpromptsfrom anduseteacherT togeneratethe
seed,ℓ
D
responsey
i
Asamultilingualdatagenerator,yourtaskistotranslatethegivenpromptfromEnglishinto
{lang_name}andgeneratetheappropriateresponseinthesamelanguage.
Important: youmustreturnboththetranslatedprompt(into{lang_name})andtheresponse.
Ensurethatboththetranslatedpromptandtheresponsearecoherent,culturallyappropriate,
anddemonstrateadeepunderstandingofthelanguagenuances.
Do not generate any other text in your response (for example, do not start your
messagewithanygreetings,andneveraskforclarificationorapologizeforstrugglingwith
thetask).
DonotreturntheoriginalEnglishprompt. Remember,youmusttranslatethepromptfirst
andreturnit.
Hereisthepromptyouneedtotranslateandrespondto:
{prompt}
Figure11: PrompttemplatefortheTranslatedatagenerationmethod.
Respond: takepromptsfrom anduseteacherT togeneratetheresponsey
seed,ℓ i
D
As a multilingual data generator, you will be presented a user request or instruction in
the{lang_name}language. Yourtaskistogenerateanappropriateresponseforthegiven
request. Ensurethatyourresponseiscoherent,culturallyappropriate,anddemonstratesa
deepunderstandingofthelanguagenuancesDonotgenerateanyothertextinyourresponse
(forexample,donotstartyourmessagewithanygreetings,andneveraskforclarificationor
apologizeforstrugglingwiththetask). Hereisthepromptyouneedtorespondto:
{prompt}
Figure12: PrompttemplatefortheResponddatagenerationmethod.
27

LLM-as-a-judge: evaluatingtextqualityusingthemultilingualrubriclanguagemodel
TaskDescription:
Aninstruction(mightincludeanInputinsideit)in{language},aresponsetoevaluate,and
ascorerubricrepresentingaevaluationcriteriaaregiven.
1. Writeadetailedfeedbackthatassessthequalityoftheresponsestrictlybasedonthegiven
scorerubric,notevaluatingingeneral.
2. After writing a feedback, write a score that is an integer between 1 and 5. You should
refertothescorerubric.
3. Theoutputshouldcontainthescoreandfeedbackonly.
4. Pleasedonotgenerateanyotheropening,closing,andexplanations.
Theinstructiontoevaluate:
{{instruction}}
Responsetoevaluate:
{{response}}
ScoreRubrics:
[Isthemodelproficientinlanguage{lang_name},includingitsculturalnuanceandgram-
maticalusage,andrespondsinahelpfulandharmlessmanneraccordingtotheinstruction?]
Score1: Theresponsecontainsseveregrammaticalerrors,lacksculturalappropriateness,or
isunhelpful/harmful. Thelanguageproficiencyisverypoor.
Score 2: The response has noticeable grammatical errors and limited cultural awareness.
It partially addresses the instruction but with significant gaps in language proficiency or
helpfulness.
Score 3: The response demonstrates adequate language proficiency with some minor
grammaticalerrors. Itshowsreasonableculturalawarenessandaddressestheinstructionina
helpfulmanner,thoughimprovementsarepossible.
Score4: Theresponseexhibitsstronglanguageproficiencywithminimalgrammaticalerrors
andgoodculturalnuance. Itaddressestheinstructioninahelpfulandharmlesswaywith
onlyminorroomforimprovement.
Score5: Theresponsedemonstratesexcellentlanguageproficiencywithpropergrammar,
appropriate cultural nuance, and idiomatic usage. It fully addresses the instruction in a
helpfulandharmlessmanner.
Feedback:
Figure13: WeevaluatetextqualityofsynthesizedtextsusingamultilingualrubricmodelcalledM-Prometheus
(Pombaletal.,2025). WechooseM-Prometheusduetoitsstrongperformanceonmultilingualandhuman-aligned
benchmarks.
28