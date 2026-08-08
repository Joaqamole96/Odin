TYPE OriginalResearch
PUBLISHED 20March2026
DOI 10.3389/frai.2026.1705245
Small LLMs can be good coldstart
recommenders
OPENACCESS
EDITEDBY
VasileDanielPavaloaia, JosephNoel1*,ChristopherMonterola1* and
AlexandruIoanCuzaUniversity,Romania
DanielStanleyTan1,2
REVIEWEDBY
BarkaouiKamel, 1AboitizSchoolofInnovation,TechnologyandEntrepreneurship,AsianInstituteofManagement,
ConservatoireNationaldesArtset Makati,Philippines,2FacultyofScience,OpenUniversiteitNederland,Heerlen,Limburg,Netherlands
Métiers(CNAM),France
RullyAgusHendrawan,
SepuluhNopemberInstituteof LargeLanguageModels(LLMs)haverevolutionizedtheArtificialIntelligence(AI)
Technology,Indonesia
fieldsincethelaunchofChatGPTin2022.Sincethen,increasinglylargermodels
*CORRESPONDENCE have been released such as ChatGPT-4o having over 175 billion parameters,
JosephNoel
Llama 3.1 with 405 billion parameters, and PaLM with 560 billion parameters.
josephnoel.phdinds2024@aim.edu
ChristopherMonterola However,LLMsofthesesizesarenolongerfeasibletoruneasilyoutsideofthe
cmonterola@aim.edu largest research labs and organizations due to the extremely large amount of
RECEIVED14September2025 GPUcomputerequiredforbothtrainingandinference.Morerecently,research
REVISED23February2026
ACCEPTED27February2026 effort has been done to create smaller LLMs which can still perform relatively
PUBLISHED20March2026 well compared to much larger models. Research has also been done to apply
CITATION LLMsfordomain-specificusecasessuchasrecommendationsystemsviaprompt
NoelJ,MonterolaCandTanDS(2026)
engineering and fine-tuning. In this paper we combine the two research fields
SmallLLMscanbegoodcoldstart
recommenders. and fine-tune two small LLMs (2 billion parameters or less) for the sequential
Front.Artif.Intell.9:1705245. recommendation task. We find that fine-tuned small LLMs still perform as well
doi:10.3389/frai.2026.1705245
and can even be better than standard sequential recommendation baseline
COPYRIGHT modelssuchasGRU4RecandSASRec,especiallyinthecoldstartsetting.
©2026 Noel,MonterolaandTan.Thisis
anopen-accessarticledistributedunder
thetermsoftheCreativeCommons KEYWORDS
AttributionLicense(CCBY).Theuse, coldstart recommendations, large language models, machine learning, PEFT,
distributionorreproductioninother recommendationsystems
forumsispermitted,providedthe
originalauthor(s)andthecopyright
owner(s)arecreditedandthatthe
1 Introduction
originalpublicationinthisjournalis
cited,inaccordancewithaccepted
academicpractice.Nouse,distribution
orreproductionispermittedwhichdoes Pre-trainedLargeLanguageModelshavebeenusefulasfoundationmodelswhichcan
notcomplywiththeseterms. thenbecustomizedfordownstreamtaskseitherviapromptengineeringorviafine-tuning.
Theyhavebeencustomizedtodomainssuchasmusic(Agostinellietal.,2023),healthcare
(Mengetal.,2024),education(Maetal.,2023;Khalidetal.,2021;Harunaetal.,2017),and
forecasting(Jinetal.,2024).LLMshavealsobeenappliedtotherecommendationdomain
in numerous works (Sanner et al., 2023; Bao et al., 2023; Harte et al., 2023; Wei et al.,
2024),takingadvantageoftheirpre-trainedlearnedrepresentationsandtheexpressivity
ofnaturallanguage.HowevermostresearchofLLMsforrecommendationsystemsmake
useofstate-of-the-artLLMswithover100billionparameters.TrainingandrunningLLMs
ofthesesizesareintractableforallbutthelargestandbestfundedorganizationsduetothe
extremelylargeamountofGPUcomputerequiredforbothtrainingandinference.
SmallLLMsarebecominganactivefieldofdevelopment(Wanetal.,2024)duetotheir
cheapercomputecostandtheyhavebecomemorecapableovertime.Thesemodelsare
smallenoughthattheycanbefine-tunedandrunusingoff-the-shelfGPUswhicharemore
readilyavailabletoeveryone.
Inthispaperweexplorefine-tuningsmallLLMswith2billionparametersorlessfor
therecommendationdomain.WeuseLow-RankAdaptation(LoRA)tofine-tunetwosmall
FrontiersinArtificialIntelligence 01 frontiersin.org

Noeletal. 10.3389/frai.2026.1705245
LLMs, Danube-1.8B (Singer et al., 2024) and Gemma-2B Popular methods devised for handling the coldstart problem
(Team et al., 2024), and evaluate them on two standard include incorporating user and item attributes in the model
recommendationsdatasets,MovieLens10M(HarperandKonstan, training(Gantneretal.,2010;Burke,2007),hybridcontent-based
2015) and Yoochoose-clicks (Ben-Shimon et al., 2015). We find and collaborative filtering algorithms (Schein et al., 2002; Stern
that the fine-tuned LLMs are able to adequately learn to do et al., 2009), user classification (Lika et al., 2014), cross-domain
sequential recommendation, and are able to beat the baseline recommendation (Kang et al., 2019; Man et al., 2017; Omidvar
recommendationmodelsinthecoldstartsetting.Tothebestofour andTran,2023),andnovelobjectivefunctionsandregularization
knowledgethisisthefirstworkonfine-tuningsmallLLMsforthe (Weietal.,2021;Abdollahpourietal.,2017;KuznetsovandKordík,
sequentialrecommendationdomaininacoldstartsetting. 2023).
WiththeadventofLLMs,newmethodsfordataaugmentation
(Weietal.,2024)andinitialpreferenceelicitations(Sanneretal.,
2 Background and related work 2023)havealsobeenexploredforcoldstartrecommendations.
2.1 Recommendation systems
2.2 Large language model
Let U be the set of users and X be the set of items. recommendation systems
Recommendation systems use machine learning algorithms to
predictauser-itemratingR(u,x)forallusersu ∈ U andallitems
Numerousworkshavepreviouslyexploredtheuseoflanguage
x∈X.
modelsforrecommendation.Onesuchuseisasasingleunifying
Different classes of recommendation system models have
model architecture that can handle different recommendation
been developed over the years, such as Content-based Filtering
problemssuchassequentialrecommendation,ratingsprediction,
(Lops et al., 2019), Collaborative Filtering (Zhang et al., 2014;
and review summarization (Harte et al., 2022). Others have used
SalakhutdinovandMnih,2007;Lindenetal.,2003),andSequential
bi-directionalencoderspioneeredinBERT(Devlinetal.,2019)for
Recommendation(Wuetal.,2019;Lietal.,2017;Liuetal.,2018;
recommendation(Zhangetal.,2019;Chenetal.,2019).
Yuetal.,2020;HidasiandKaratzoglou,2018;Wang-ChengKang,
The advent of pre-trained Large Language Models has
2018).Availabilityofpastuserpreferenceinformationisaconcern
broughtaboutnumerousresearchinvestigatingtheirapplicability
asmodeltrainingismainlydoneonprevioususer-iteminteractions
for recommendation. Most applications have focused on their
such as explicit rating scores and implicit activities such as item
usefulnessonthecoldstartproblem.LLMsfromOpenAIhavebeen
clicksorviews.
usedfordataaugmentationtohandlethecommoncoldstartand
data sparsity challenge in recommendation systems (Wei et al.,
2024). OpenAI’s LLM text embeddings have also been used to
2.1.1 Sequentialrecommendation
initialize BERT4Rec (Zhang et al., 2019) item embeddings and
have been found to improve its performance (Harte et al., 2023).
A common formulation of the recommendation problem
Google’s PaLM (Chowdhery et al., 2023) was used to investigate
models the data as a sequence of user-item interactions. In
solely using prompt-engineering for recommendation and found
sequential recommendation, let X be the set of items to be
itwascompetitiveinnearcold-startsettings(Sanneretal.,2023).
recommended,andx1:t =x1,x2,...,xT bethethesequenceofpast
Facebook’s Llama (Touvron et al., 2023a) was fine-tuned for a
user-iteminteractionswherexi ∈ Xistheuser-iteminteractionat
binaryrecommendationproblemandperformedwellinafew-shot
timestampt.Asequentialrecommendationmodelcanbeamulti-
settingwhichissimilartocoldstart(Baoetal.,2023).
classclassifierwhere,giventheinteractionsequencex1:t,themodel
The above examples all use state-of-the-art and extremely
tries to predict the next item in the sequence xt+1. The model
large language models with the order of hundreds of billions of
outputcanbearankedlistofitemswithclassificationlogitsy =
t+1
[y1,y2,...,yn] ∈ Rnwheren = |I|isthenumberofpossibleitems. parameters. Running these LLMs locally will require extremely
large amounts of compute which may not be feasible for most
Thefinalrecommendationlistattimestampt+1arethetop-kitems
organizations. We explore two options for scaling down the
fromy .
t+1
requirements of using LLMs for recommendation: Smaller large
languagemodelsandparameter-efficientfine-tuning.
2.1.2 Coldstartrecommendation
The coldstart problem is one of the fundamental research 2.2.1 Smalllargelanguagemodels
problem in the field of recommendation systems and numerous
research efforts have been dedicated to solving it (Gope and Recently, research has been done on the creation of smaller
Jain, 2017). Because traditional recommendation models rely on largelanguagemodelswhichcanstillperformcompetitivelywith
past user-item interactions, new users and items won’t have had themuchlargerstate-of-the-artLLMs(Wanetal.,2024;Sheiketal.,
enoughhistoricalinformationtomakeaccuraterecommendation 2024).Smallermodelsareeasiertofine-tuneandwillhavecheaper
predictionson.Newitemsinparticularmaybedisadvantagedand inferencecostswhendeployedinreal-worldproductionuse-cases
won’tberecommendedatallduetopopularitybiaswhichcanfavor (Singeretal.,2024;Teametal.,2024;Zhangetal.,2024).Wenote
olderitems(Noeletal.,2024;Abdollahpourietal.,2017). that the term “small” here is relative and applied specifically to
FrontiersinArtificialIntelligence 02 frontiersin.org

| Noeletal. |     |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1705245 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
TABLE1Numberofsequencesusedfortrainingandtesting.
LLMswhichhavelessthan2billionparameters,whichcanstillbe
quitelargewhencomparedtomoretraditionalmachinelearning
|     |     |     |     |     |     |     |     | Dataset |     | Trainingsequences |     |     | TesSequencest |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ----------------- | --- | --- | ------------- | --- | --- |
models.
|     |     |     |     |     |     |     |     | Yoochoose |     |     | 53,840 |     |     | 13,560 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | ------ | --- | --- | ------ | --- |
|     |     |     |     |     |     |     |     | MovieLens |     |     | 55,902 |     |     | 13,976 |     |
2.2.2 LLMfine-tuning
| Fine-tuning |     | is a commonly | used | technique | in  | deep learning |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | ---- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
totakeadvantageofpre-trainedmodelsandadaptthemforother onlyafractionofthedataduetoitslargesize(Wuetal.,2019;Li
domains(Jungetal.,2015;Yinetal.,2017;Jaquesetal.,2016,2017; etal.,2017;Liuetal.,2018;Yuetal.,2020).
HowardandRuder,2018).Duetotheextremelylargemodelsizesof Forbothdatasetsweusethelastinteractioninthesequenceas
LLMs,updatingtheweightsoftheentiremodelisinfeasiblewithout thepredictiontargetxt+1,andonlygettheprevious5interactions
| having access | to  | a large amount | of  | GPU compute |     | which may | be  |     |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
astheinputsequence.Thisleavesalimitedsetofinteractionswhich
unrealisticformostorganizationsandresearchers.Techniquesfor simulatesthecoldstartsetting,whereonlyasmallnumberofusers
parameter-efficientfine-tuning(PEFT)(Dingetal.,2023)needed willhavealimitednumberofinteractionswiththeitems.Table1
tobedeveloped. showsthenumberofsequencesusedfortrainingandtestinginour
One of the more popular PEFT methods is Low-Rank experiments.OnlytheitemIDsareusedfromthedatasetandno
| Adaptation | (LoRA) | (Hu | et al., 2022). | LoRA | works | by adding | a   |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | -------------- | ---- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
otheradditionaluseroritemfeatureshavebeenutilized.
| small number | of  | new weight | matrices | into | the model | and | only |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | -------- | ---- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
thesenewadditionsareupdatedduringfine-tuningtraining.The
| much smaller | number | of  | trainable | parameters | makes | the | fine- |     |     |     |     |     |     |     |     |
| ------------ | ------ | --- | --------- | ---------- | ----- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
3.1.1 LLMfine-tuningdataset
tuningprocessfasterandmoreefficientcomparedtoupdatingall
theweightsoftheentiremodel.Formally,thelearningobjectivefor
|     |     |     |     |     |     |     |     | To fine-tune |     | the LLMs | we  | need to | convert | the datasets | into |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | --- | ------- | ------- | ------------ | ---- |
anLLMcanbedefinedas
|     |     |     |     |     |     |     |     | prompts  | suitable  | for causal | language | modeling. |       | Causal language |      |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | -------- | --------- | ----- | --------------- | ---- |
|     |     |     |     |     |     |     |     | modeling | is a text | generation |          | workflow  | which | predicts the    | next |
|y|
|     |     |     |     |     |     |     |     | token in | a sequence | of  | tokens, | using only | the | previous tokens | as  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ------- | ---------- | --- | --------------- | --- |
m ax X Xlog(P8(yt |x,y<t)), information.Weconvertthesequenceinputandtargetoutputinto
8
(x,y)∈Zt=1
promptsinthefollowingmannershowninTable2.Thefinalword
|     |     |     |     |     |     |     |     | target output | is  | left out | of the | test input | data | and the LLM | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------ | ---------- | ---- | ----------- | --- |
wherexandyareintheinputandoutputtokensoftrainingsetZ,
yt isthet-thtokenofy,y<t arethetokensbeforeyt,and8isthe promptedforthepredictedoutput.
originalparameterweights.Thenumberofparametersin8willbe
verylargeforlargelanguagemodels,thereforeLoRAintroducesa
newsetofparameters2suchthat
|     |     |      |              |           |     |     |     | 3.2 Small | LLMs    |             |     |            |     |                  |     |
| --- | --- | ---- | ------------ | --------- | --- | --- | --- | --------- | ------- | ----------- | --- | ---------- | --- | ---------------- | --- |
|     |     |      | |y|          |           |     |     |     | We        | use two | open-source |     | LLM models | in  | our experiments, |     |
|     | m   | ax X | Xlog(P8+2(yt | |x,y<t)), |     |     |     |           |         |             |     |            |     |                  |     |
2 Danube-1.8B (Singer et al., 2024) and Gemma-2B (Team et al.,
(x,y)∈Zt=1
|     |     |     |     |     |     |     |     | 2024). Danube-1.8B |     | is  | a decoder | model | based | on the Llama | 2   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --------- | ----- | ----- | ------------ | --- |
andwherethenumberofnewparametersin2willbemuchsmaller architecture(Touvronetal.,2023b)with1.8billionparametersand
thanthenumberofparametersin8.Onlytheparametersof2are trained on 1 trillion tokens. Gemma-2B is decoder model with 2
billionparametersandtrainedon3trilliontokens.Akeyelement
updatedduringtheLoRAfine-tuning,makingthismoreefficient
andlesstime-consumingthanregularfine-tuning. inselectingthesemodelsistheiropen-sourcenaturesothattheir
|     |     |     |     |     |     |     |     | trainedmodelweightsareavailableonline1,2 |     |     |     |     | andcanbeusedfor |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --------------- | --- | --- |
Inthenextsectionwefine-tunesmallLLMsforthesequential
| recommendationdomaininthecoldstartsettingusingLoRAand |     |     |     |     |     |     |     | furtherfine-tuning. |          |     |         |       |               |             |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | -------- | --- | ------- | ----- | ------------- | ----------- | --- |
|                                                       |     |     |     |     |     |     |     | We                  | use LoRA | (Hu | et al., | 2022) | for efficient | fine-tuning | of  |
showourresults.
|     |     |     |     |     |     |     |     | both models | for | recommendation, |     | using | the | converted prompts |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --------------- | --- | ----- | --- | ----------------- | --- |
datasetdetailedintheprevioussection.Table3showsthenumber
|     |     |     |     |     |     |     |     | of trainable | parameters |     | that were | used | for fine-tuning | and | what |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | --------- | ---- | --------------- | --- | ---- |
3 Experiments
|     |     |     |     |     |     |     |     | percentage | they         | were of | the original | model | size.    | It can be  | seen   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | ------- | ------------ | ----- | -------- | ---------- | ------ |
|     |     |     |     |     |     |     |     | that we    | are updating | only    | a very       | small | fraction | (less than | 1%) of |
3.1 Dataset
thenumberofweightsoftheoriginalmodels,whichallowsusto
|             |     |            |       |     |           |            |     | fine-tune | them | on relatively | dated | NVIDIA | GeForce | GTX | 1080 |
| ----------- | --- | ---------- | ----- | --- | --------- | ---------- | --- | --------- | ---- | ------------- | ----- | ------ | ------- | --- | ---- |
| We evaluate |     | our method | using | two | datasets: | Yoochoose- |     |           |      |               |       |        |         |     |      |
TiGPUs.
| clicks (Ben-Shimon |     | et al., | 2015), | and MovieLens10M |     | (Harper |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | ------ | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andKonstan,2015).InMovieLens10Meachuser-movieratingis
consideredaninteraction,withtheactualvalueoftheratingbeing
disregarded. In Yoochoose-clicks we remove duplicate item IDs 1 https://huggingface.co/h2oai/h2o-danube-1.8b-base
fromthesequences.Wealsofollowacommonpracticeofsampling
2 https://huggingface.co/google/gemma-2b
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 03  |     |     |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Noeletal. |     |     |     |     |     |     |     | 10.3389/frai.2026.1705245 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
TABLE2LLMfine-tuningdatasetconvertedtoprompts.
|     |     |     |     |     |     | N   | |y−xi | |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- |
X
N
| Dataset | Example |     |     |     |     | i   |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Trainingdata “Thisuserinteractedwiththefollowingitemsinthegiven Theaveragedistanceiscalculatedusingthehammingdistance
betweentwostringswhichisthenumberofpositionsinthestrings
order:466,520,151,1408,1912.Thenextmovietheuser
willclickis8784” inwhichtheydiffer.Forexamplethestrings“11059”and“15069”
haveahammingdistanceof2,pertainingtothetwopositionsthat
| Testdata | “Thisuserinteractedwiththefollowingitemsinthegiven |     |     |     |     |     |     |     |     |     |
| -------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
order:832,1271,3108,3252,224.Thenextitemtheuser arebolded.Theaveragedistanceiscalculatedas:
willclickis”
N
| Targetoutput | “5629” |     |     |     |     | Hamming(y,xi) |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
X
TABLE3NumberoftrainableLoRAparametersandtheirpercentageoftheoriginalmodelsize. N
i
| LLM    |     | Trainableparameters |     |           |     |     |     |     |     |     |
| ------ | --- | ------------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
| Danube |     | 8,650,752(0.47%)    |     | 4 Results |     |     |     |     |     |     |
| Gemma  |     | 9,805,824(0.39%)    |     |           |     |     |     |     |     |     |
Werunourexperimentsfivetimesforeachmodelanddataset
3.2.1 Baselinemodels combinationandtheaverageoftheresultsarepresented.Wealso
doone-wayANOVA(Fisher,1992)followedbyTukey’sHSDtest
We compare against three deep learning sequential (Tukey,1949)toconfirmthatthedifferenceinresultsoftheLLMs
comparedtothebaselinemethodsarestatisticallysignificant.
| recommendation | models as baselines, | GRU4Rec (Hidasi | et al., |        |           |           |        |      |          |          |
| -------------- | -------------------- | --------------- | ------- | ------ | --------- | --------- | ------ | ---- | -------- | -------- |
|                |                      |                 |         | Table4 | shows the | HitRate@1 | of the | LLMs | together | with the |
2016),SASRec(Wang-ChengKang,2018)andBERT4Rec(Zhang
|     |     |     |     | baseline | models, along | with | the average | distance | and | average |
| --- | --- | --- | --- | -------- | ------------- | ---- | ----------- | -------- | --- | ------- |
etal.,2019).AllmodelsaretrainedwiththeAdam(KingmaandBa,
|     |     |     |     | deviation | of their predicted |     | outputs. | We see | that | the LLMs |
| --- | --- | --- | --- | --------- | ------------------ | --- | -------- | ------ | ---- | -------- |
2015)optimizerusingcross-entropyloss.Modelhyperparameters
weretunedwithgrid-searchandthebestresultsarereported. have superior sequential recommendation performance in the
|     |     |     |     | MovieLens | and Yoochoose | datasets | under | the | coldstart | setting. |
| --- | --- | --- | --- | --------- | ------------- | -------- | ----- | --- | --------- | -------- |
Thedetailsoftheirfinalmodelarchitecturesarebelow:
|     |     |     |     | With the | limited training | data, | the LLMs | were | able | to take |
| --- | --- | --- | --- | -------- | ---------------- | ----- | -------- | ---- | ---- | ------- |
• GRU4Rec:1embeddinglayerand1GRUlayer,20%dropout advantage of the closer similarity between IDs in the sequences
andfully-connecteddenseoutputlayerwithsoftmaxoutput. for its predictions. The baseline algorithms are trying to learn
The embedding and GRU layers have sizes of both 100 for embeddingsforeachitemIDwhichnecessitatesmoretrainingdata
MovieLensandsizesof400and100forYoochoose. tomodeltheuserpreferencesaccurately.
• SASRec: 1 embedding layer and 1 self-attention layer, 20% Finally,inbothdatasetstheaveragedistanceanddeviationof
dropoutandfully-connecteddenseoutputlayerwithsoftmax the LLMs are smaller than of the baseline models. This suggests
output.Theembeddingsizesandfeedforwardlayersizesare that the LLMs are more likely to predict item ID values that are
64and256forMovieLensand32and512forYoochoose. closerinvaluetotheinputsequencebothtextuallyandnumerically.
• BERT4Rec:1embeddinglayerand2self-attentionlayers,20% SequencesofIDsthatarerelativelyclosetoeachotherareeasierfor
dropoutandfully-connecteddenseoutputlayerwithsoftmax theLLMtolearnefficiently.
output.Theembeddingsizesandfeedforwardlayersizesare
64and128forMovieLensand64and64forYoochoose.
|               |     |     |     | 5 Analysis       |     |          |     |     |     |     |
| ------------- | --- | --- | --- | ---------------- | --- | -------- | --- | --- | --- | --- |
| 3.2.2 Metrics |     |     |     | 5.1 Tokenization |     | behavior |     |     |     |     |
TomeasuretheperformanceofourmodelweuseHitRate@1. WeanalyzedhowbothGemma-2BandDanube-1.8Btokenize
HitRate@k measures whether the correct item is in the top-k itemIDs.AsshowninTable5neithermodeltreatsnumericitem
position in the recommendation list. HitRate@1 is equivalent to IDs as atomic symbols. Instead, each ID is decomposed into a
multi-classclassificationaccuracy. sequence of digit-level tokens. Because the number of tokens
Wealsomakeuseoftwoadditionalmetricstohelpusanalyze correspondsdirectlytothenumberofdigits,themodelsimplicitly
the predicted outputs of the models. Given that the LLMs are learn the morphological structure of item IDs rather than their
predicting the item IDs by each single-digit token one by one, symbolicidentity.ThisexplainswhytheLLMssometimespredict
we measure the average deviation and the average distance of the outputswithsimilardigitpatternsorsimilarnumberofdigits.
predicteditemIDstotheIDsintheinputsequence.Wemeasure However this tokenizer-induced numeric bias cannot fully
the average deviation by getting the absolute difference between accountformodelbehavior.Manycorrectpredictionscorrespond
the predicted ID with each input ID and averaging them. In our to items that are not numerically close to any input IDs.
=
experiments where N 5, y is the prediction output and xi is These predictions cannot be explained by digit continuity or
thei−thitemIDintheinputsequence,theaveragedeviationis numeric similarity, indicating that the models are also learning
calculatedas: co-occurrencestructureinthedataratherthanperformingtrivial
| FrontiersinArtificialIntelligence |     |     |     | 04  |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Noeletal. |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1705245 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
TABLE4Averagedistanceandaveragedeviationofpredictions. TABLE7ResultsofdifferentinputsequencelengthsontheMovielensdataset.
Dataset Model HitRate@1 Average Average Model Inputsequencelength Tokenization
|           |          |     |        |     | distance | deviation |                   |     |     |     |     |        |     |
| --------- | -------- | --- | ------ | --- | -------- | --------- | ----------------- | --- | --- | --- | --- | ------ | --- |
|           |          |     |        |     |          |           | Danube            |     | 5   |     |     | 0.0995 |     |
| Yoochoose | Danube   |     | 0.0555 |     | 3.50     | 11,610.96 |                   |     | 10  |     |     | 0.1044 |     |
|           | Gemma    |     | 0.0540 |     | 3.48     | 11,326.80 |                   |     | 20  |     |     | 0.0973 |     |
|           | GRU4Rec  |     | 0.0440 |     | 3.75     | 13,336.70 |                   |     |     |     |     |        |     |
|           |          |     |        |     |          |           |                   |     | 50  |     |     | 0.0917 |     |
|           | SASRec   |     | 0.0354 |     | 3.82     | 13,906.85 |                   |     |     |     |     |        |     |
|           |          |     |        |     |          |           | GRU4Rec           |     | 5   |     |     | 0.0934 |     |
|           | BERT4Rec |     | 0.0499 |     | 3.66     | 12,419.45 |                   |     |     |     |     |        |     |
|           |          |     |        |     |          |           |                   |     | 10  |     |     | 0.0961 |     |
| MovieLens | Danube   |     | 0.0995 |     | 3.20     | 4163.35   |                   |     | 20  |     |     | 0.1037 |     |
|           | Gemma    |     | 0.1019 |     | 3.19     | 3,999.54  |                   |     | 50  |     |     | 0.1080 |     |
|           | GRU4Rec  |     | 0.0934 |     | 3.35     | 4,773.73  | Bestresultinbold. |     |     |     |     |        |     |
|           | SASRec   |     | 0.0898 |     | 3.37     | 5,319.92  |                   |     |     |     |     |        |     |
BERT4Rec 0.0854 3.34 4,429.16 representations,thesmallLLMsshineatshorteriteminteraction
HighestHR@1andthelowestAverageDistanceandAverageDeviationareinbold.TheLLMs historiestypicalofthecoldstartscenarioinourstudy.
performbetterthanthebaselinealgorithmsinthecoldstartsettingandtheirpredictionsare
closertotheinputsequencesbothtextuallyandnumerically.
|     |     |     |     |     |     |     | 5.3 Inference | efficiency |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | --- | --- | --- | --- |
TABLE5ExampleoftokenizationoutputforbothDanubeandGemma.
Model ID Tokenization WealsomeasuredinferenceperformanceforthesmallLLMs
usedinourexperiments.Inourmachines,3Gemma-2Bachieveda
| Danube |     |     | 4,568 |     |     | [4,5,6,8] |     |     |     |     |     |     |     |
| ------ | --- | --- | ----- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
latencyof59.5mspergeneratedtoken,whileDanube-1.8Bachieved
|       |     |     | 376   |     |     | [3,7,7]   |              |                   |        |               |      |         |             |
| ----- | --- | --- | ----- | --- | --- | --------- | ------------ | ----------------- | ------ | ------------- | ---- | ------- | ----------- |
|       |     |     |       |     |     |           | 34.3ms, with | both models       | using  | approximately |      | 5.2GB   | of GPU      |
| Gemma |     |     | 4,568 |     |     | [4,5,6,8] |              |                   |        |               |      |         |             |
|       |     |     |       |     |     |           | memory       | during inference. | Larger | LLMs          | will | require | much larger |
376 [3,7,7] computing requirements and also higher latency in the same
|     |     |     |     |     |     |     | machines | (Chitty-Venkata | et  | al., 2025). | Additionally, |     | while these |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | --- | ----------- | ------------- | --- | ----------- |
TABLE6SampleofcorrectpredictionswhicharenotnumericallyclosetotheinputIDs. latencies are higher than those of the baseline recommendation
models,theLLMsdonotrequireaseparateitem-embeddingmatrix
| Input |     |     |     |     | Prediction |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
whosesizegrowslinearlywiththenumberofitemsinthecatalog.
|                                 |     |     |     |     |     |        | LLMs operate  | directly      | on the       | tokenized    | string | representation | of         |
| ------------------------------- | --- | --- | --- | --- | --- | ------ | ------------- | ------------- | ------------ | ------------ | ------ | -------------- | ---------- |
| 36,431,40,655,40,661,249,28,858 |     |     |     |     |     | 30,761 |               |               |              |              |        |                |            |
|                                 |     |     |     |     |     |        | item IDs      | and therefore | rely on      | a fixed-size |        | tokenizer      | vocabulary |
| 421,1,183,205,143,117           |     |     |     |     |     | 722    |               |               |              |              |        |                |            |
|                                 |     |     |     |     |     |        | and embedding | table.        | As a result, | the          | memory | footprint      | of the     |
50,47,51,28,413,9 23,164 LLMs remains constant regardless of catalog size which can
2,614,41,456,3,735,6,775,41,446 2,210 be advantageous in domains where item vocabularies are large
ordynamic.
| numeric | continuations. |     | These observations |     | suggest | that small |     |     |     |     |     |     |     |
| ------- | -------------- | --- | ------------------ | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
6 Conclusion
| LLMs do  | exploit          | digit-level | regularities | imposed  |     | by tokenization |     |     |     |     |     |     |     |
| -------- | ---------------- | ----------- | ------------ | -------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
| but also | learn meaningful |             | sequential   | patterns |     | beyond simple   |     |     |     |     |     |     |     |
numericmorphology.Weshowasampleofthesepredictionsfrom WehaveshownthatsmallLLMscanpunchabovetheirweight
andbeviablesequentialrecommendationmodelsafterfine-tuning
theDanubemodelinTable6.
withLoRA.WealsofoundthattheLLMsweremorelikelytomake
predictionsthatareclosertotheinputsequencesbothtextuallyand
numerically.InourexperimentsthesmallLLMswereevenableto
| 5.2 Input | Sequence |     | Length |     |     |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
beatstandardsequentialrecommendationmodelsinthecoldstart
setting.Wealsoperformedtoken-levelanalysis,whichshowedthat
WealsoranadditionalexperimentsontheMovielensdataset
althoughthemodelsexploitdigit-leveltokenizationpatternswhich
| using the | Danube-1.8B | LLM | model | and | the GRU4Rec | basleline |                |            |      |      |                  |     |            |
| --------- | ----------- | --- | ----- | --- | ----------- | --------- | -------------- | ---------- | ---- | ---- | ---------------- | --- | ---------- |
|           |             |     |       |     |             |           | biases numeric | proximity, | they | also | learn meaningful |     | sequential |
modeltotesttheeffectsofincreasingthelengthofinputsequences
patterns.TheLLMsalsoavoiditem-embeddingtablesandtherefore
andshowtheseresultsinTable7.Unlikeconventionalsequential
scaleindependentlyofcatalogsizewhichcanbeadvantageousin
| recommenders | which  | typically | benefit        |     | from longer | interaction |         |                |       |            |        |          |         |
| ------------ | ------ | --------- | -------------- | --- | ----------- | ----------- | ------- | -------------- | ----- | ---------- | ------ | -------- | ------- |
|              |        |           |                |     |             |             | domains | with extremely | large | vocabulary | sizes. | Finally, | we also |
| histories,   | wefind | thatthe   | small LLMmodel |     | wasnot      | ableto      | take    |                |       |            |        |          |         |
lookedattheeffectsoflongerinputsequencehistoriesandfound
advantageofthelongerinputsequencestoimproveitsperformance
|                |         |     |         |       |     |                | that traditional | sequential | recommenders |     | like | GRU4Rec | are able |
| -------------- | ------- | --- | ------- | ----- | --- | -------------- | ---------------- | ---------- | ------------ | --- | ---- | ------- | -------- |
| significantly, | whereas | the | GRU4Rec | model | was | able to better |                  |            |              |     |      |         |          |
improveitsperformanceastheinputsequencelengthincreased.
| Our | results show | that | while | the baseline | GRU4Rec | model |     |     |     |     |     |     |     |
| --- | ------------ | ---- | ----- | ------------ | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
can better leverage longer histories through learned item 3 IntelXeonCPUwith4NVIDIAGeForceRTX2080TiGPUs.
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 05  |     |     |     |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- |

| Noeletal. |     |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1705245 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
Funding
toleveragelongeritemhistoriesbetterandwilleventuallybeatthe
smallLLMsoutsideofthecoldstartscenario.Afuturestudybeyond
thescopeofthispapercouldbeonhowtoimprovethesmallLLMs Theauthor(s)declaredthatfinancialsupportwasnotreceived
tobetterleveragelongeritemhistories. forthisworkand/oritspublication.
| Our results | holds | great       | promise | in future | democratization |               | of  |     |     |     |     |     |     |     |     |
| ----------- | ----- | ----------- | ------- | --------- | --------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the use of  | small | LLMs, which | can     | be run by | more            | organizations |     |     |     |     |     |     |     |     |     |
withrelativelylessercomputecapacities.Futureworkinthisfield
|                      |      |                |              |               |                     |              |         | Conflict       | of        | interest |            |      |              |               |     |
| -------------------- | ---- | -------------- | ------------ | ------------- | ------------------- | ------------ | ------- | -------------- | --------- | -------- | ---------- | ---- | ------------ | ------------- | --- |
| can explore          | even | smaller        | LLMs, as     | well as       | their applicability |              | for     |                |           |          |            |      |              |               |     |
| other recommendation |      | domains        | such         | as ratings    |                     | predictions. | A       |                |           |          |            |      |              |               |     |
|                      |      |                |              |               |                     |              |         | The            | author(s) | declared | that       | this | work         | was conducted |     |
| more systematic      |      | study of       | tokenization | strategies    | such                | as           | learned |                |           |          |            |      |              |               |     |
|                      |      |                |              |               |                     |              |         | in the absence |           | of any   | commercial |      | or financial | relationships |     |
| ID embeddings        |      | or alternative | numeric      | decomposition |                     | methods      |         |                |           |          |            |      |              |               |     |
can be also done for comparison. Using small LLMs for feature that could be construed as a potential conflict
ofinterest.
| augmentation | or               | dataset | augmentation | can        | also | be additional |     |     |     |     |     |     |     |     |     |
| ------------ | ---------------- | ------- | ------------ | ---------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| use cases    | for exploration. |         | These        | directions | can  | deepen        | our |     |     |     |     |     |     |     |     |
understandingofwhensmallLLMsrepresentapracticalalternative
toembedding-basedrecommendersandhowtheycanbeusedmost Generative AI statement
effectivelywithinreal-worldsystems.Wehopethatourworkalso
encouragestheuseofopen-sourceandsmallerLLMsinotherfields
Theauthor(s)declaredthatgenerativeAIwasnotusedinthe
outsidetherecommendationdomain,astheymayprovideamore
creationofthismanuscript.
realisticalternativethanalwaysgoingforthebiggeststate-of-the-
|     |     |     |     |     |     |     |     | Any | alternative | text | (alt | text) provided |     | alongside | figures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ---- | -------------- | --- | --------- | ------- |
artmodels.
|     |     |     |     |     |     |     |     | in this   | article       | has been     | generated |           | by Frontiers |         | with the |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ------------ | --------- | --------- | ------------ | ------- | -------- |
|     |     |     |     |     |     |     |     | support   | of artificial | intelligence |           | and       | reasonable   | efforts | have     |
|     |     |     |     |     |     |     |     | been made | to            | ensure       | accuracy, | including |              | review  | by the   |
Data availability statement authors wherever possible. If you identify any issues, please
contactus.
Theoriginalcontributionspresentedinthestudyareincluded
| in the article/supplementary |     |     | material, | further | inquiries |     | can be |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --------- | ------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
directedtothecorrespondingauthor.
|        |               |     |     |     |     |     |     | Publisher’s    |           | note            |         |            |            |          |            |
| ------ | ------------- | --- | --- | --- | --- | --- | --- | -------------- | --------- | --------------- | ------- | ---------- | ---------- | -------- | ---------- |
|        |               |     |     |     |     |     |     | All claims     | expressed |                 | in this | article    | are solely | those    | of the     |
| Author | contributions |     |     |     |     |     |     |                |           |                 |         |            |            |          |            |
|        |               |     |     |     |     |     |     | authors and    | do        | not necessarily |         | represent  | those      | of their | affiliated |
|        |               |     |     |     |     |     |     | organizations, | or        | those           | of the  | publisher, | the        | editors  | and the    |
JN:Writing–originaldraft,Writing–review&editing.CM: reviewers. Any product that may be evaluated in this article, or
Supervision,Writing–review&editing.DT:Supervision,Writing claimthatmaybemadebyitsmanufacturer,isnotguaranteedor
endorsedbythepublisher.
–review&editing.
References
Abdollahpouri,H.,Burke,R.,andMobasher,B.(2017).“Controllingpopularitybias onHighPerformanceComputing,Network,Storage,andAnalysis(Atlanta,GA:IEEE
| inlearning-to-rankrecommendation,”inProceedingsofthe11thACMConferenceon |     |     |     |     |     |     |     | Press). |     |     |     |     |     |     |     |
| ----------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
RecommenderSystems.
|     |     |     |     |     |     |     |     | Chowdhery, | A., Narang, | S., Devlin, | J., | Bosma, M., | Mishra, | G., Roberts, | A., et al. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ----------- | --- | ---------- | ------- | ------------ | ---------- |
Agostinelli,A.,Denk,T.I.,Borsos,Z.,Engel,J.,Verzetti,M.,Caillon,A.,etal.(2023). (2023). PaLM: Scaling language modeling with pathways. J. Mach. Learn. Res.
Musiclm:GeneratingMusicFromText.arXiv[Preprint].arXiv:2301.11325. 24,1–113.doi:10.5555/3648699.3648939
Bao,K.,Zhang,J.,Zhang,Y.,Wang,W.,Feng,F.,andHe,X.(2023).“TALLRec: Devlin,J.,Chang,M.-W.,Lee,K.,andToutanova,K.(2019).“BERT:Pre-training
an effective and efficient tuning framework to align large language model with of deep bidirectional transformers for language understanding,” in Proceedings
recommendation,”inProceedingsofthe17thACMConferenceonRecommenderSystems of the 2019 Conference of the North American Chapter of the Association
(NewYork,NY:AssociationforComputingMachinery). for Computational Linguistics (Minneapolis, MN: Association for Computational
Linguistics).
Ben-Shimon,D.,Tsikinovsky,A.,Friedmann,M.,Shapira,B.,Rokach,L.,andHoerle,
J.(2015).“RecSyschallenge2015andtheyoochoosedataset,”inProceedingsofthe9th Ding,N.,Qin,Y.,Yang,G.,Wei,F.,Zonghan,Y.,Su,Y.,etal.(2023).Parameter-
ACMConferenceonRecommenderSystems. efficientfine-tuningoflarge-scalepre-trainedlanguagemodels.Nat.Mach.Intellig.5,
Burke, R. (2007). Hybrid Web Recommender Systems. Cham: Springer-Verlag, p. 1–16.doi:10.1038/s42256-023-00626-4
377–408 Fisher, R. (1992). “Statistical methods for research workers,” in Breakthroughs in
Chen,X.,Liu,D.,Lei,C.,Li,R.,Zha,Z.-J.,andXiong,Z.(2019).“BERT4SessRec: Statistics:MethodologyandDistribution(NewYork,NY:Springer).
Content-basedvideorelevancepredictionwithbidirectionalencoderrepresentations Gantner, Z., Drumond, L., Freudenthaler, C., Rendle, S., and Schmidt-Thieme, L.
from transformer,” in Proceedings of the 27th ACM International Conference on (2010).“Learningattribute-to-featuremappingsforcold-startrecommendations,”in
Multimedia(NewYork,NY:AssociationforComputingMachinery). 2010IEEEInternationalConferenceonDataMining(Sydney:IEEE).
Chitty-Venkata,K.T.,Raskar,S.,Kale,B.,Ferdaus,F.,Tanikanti,A.,Raffenetti,K.,etal. Gope,J.,andJain,S.K.(2017).“Asurveyonsolvingcoldstartprobleminrecommender
(2025).“LLM-inference-bench:inferencebenchmarkingoflargelanguagemodelson systems,” in 2017 International Conference on Computing, Communication and
aiaccelerators,”inProceedingsofthe2024WorkshopsoftheInternationalConference Automation(ICCCA)(GreaterNoida:IEEE),133–138.
| FrontiersinArtificialIntelligence |     |     |     |     |     |     | 06  |     |     |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Noeletal. |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2026.1705245 |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
Harper,F.M.,andKonstan,J.A.(2015).Themovielensdatasets:historyandcontext. Meng, X., Yan, X., Zhang, K., Liu, D., Cui, X., Yang, Y., et al. (2024). The
ACMTrans.Interact.Intellig.Syst.5,1–19.doi:10.1145/2827872 applicationoflargelanguagemodelsinmedicine:ascopingreview.iScience27:109713.
doi:10.1016/j.isci.2024.109713
Harte,J.,Zorgdrager,W.,PanosLouridas,A.K.,Jannach,D.,andFragkoulis,M.(2022).
“ShijieGengandShuchangLiuandZuohuiFuandYingqiangGeAndyongfengZhang,” Noel, J., Monterola, C., and Tan, D. S. (2024). Improving recommendation
inProceedingsofthe16thACMConferenceonRecommenderSystems(NewYork,NY: diversitywithoutretrainingfromscratch.Int.J.DataSci.Analytics.20,1151–1160.
AssociationforComputingMachinery). doi:10.1007/s41060-024-00518-9
Harte,J.,Zorgdrager,W.,PanosLouridas,A.K.,Jannach,D.,andFragkoulis,M.(2023). Omidvar, S., and Tran, T. (2023). Tackling cold-start with deep
“Leveraginglargelanguagemodelsforsequentialrecommendation,”inProceedingsof personalized transfer of user preferences for cross-domain recommendation.
the17thACMConferenceonRecommenderSystems. Int. J. Data Sci. Analytics. 20, 121–130. doi: 10.1007/s41060-023-00
467-9
| Haruna, K., | Ismail, M. | A., Damiasih, | D., | Sutopo, J., | and Herawan, | T. (2017). |     |     |     |     |     |     |     |
| ----------- | ---------- | ------------- | --- | ----------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
A collaborative approach for research paper recommender system. PLoS ONE. Salakhutdinov, R., and Mnih, A. (2007). “Probabilistic matrix factorization,” in
12:e0184516.doi:10.1371/journal.pone.0184516 Proceedings of the 20th International Conference on Neural Information Processing
Systems(RedHook,NY:CurranAssociatesInc.).
Hidasi,B.,andKaratzoglou,A.(2018).“Recurrentneuralnetworkswithtop-kgains
forsession-basedrecommendations,”inProceedingsofthe27thACMInternational Sanner,S.,Balog,K.,Radlinski,F.,Wedin,B.,andDixon,L.(2023).“Largelanguage
ConferenceonInformationandKnowledgeManagement(NewYork,NY:Association modelsarecompetitivenearcold-startrecommendersforlanguageanditem-based
forComputingMachinery). preferences,”inProceedingsofthe17thACMConferenceonRecommenderSystems(New
York,NY:AssociationforComputingMachinery).
| Hidasi, B., | Karatzoglou, | A., Baltrunas, | L., | and Tikk, | D. (2016). | “Session-based |     |     |     |     |     |     |     |
| ----------- | ------------ | -------------- | --- | --------- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
recommendations with recurrent neural networks,” in Proceedings of the 4th Schein, A. I., Popescul, A., Ungar, L. H., and Pennock, D. M. (2002). “Methods
InternationalConferenceonLearningRepresentations. and metrics for cold-start recommendations,” in Proceedings of the 25th Annual
Howard, J., and Ruder, S. (2018). “Universal language model fine-tuning for InternationalACMSIGIRConferenceonResearchandRevelopmentInInformation
Retrieval(NewYork,NY:AssociationforComputingMachinery).
| text classification,” | in Proceedings |     | of the 56th | Annual | Meeting | of the Association |     |     |     |     |     |     |     |
| --------------------- | -------------- | --- | ----------- | ------ | ------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
for Computational Linguistics (Melbourne, VIC: Association for Computational Sheik,R.,Sundara,K.P.S.,andNirmala,S.J.(2024).Neuraldataaugmentationfor
Linguistics). legaloverrulingtask:Smalldeeplearningmodelsvs.largelanguagemodels.Neural
Hu,E.J.,Shen,Y.,Wallis,P.,Allen-Zhu,Z.,Li,Y.,Wang,S.,etal.(2022).“LoRA: Proc.Letters56:4.doi:10.1007/s11063-024-11574-4
Low-rankadaptationoflargelanguagemodels,”inProceedingsofthe10thInternational Singer, P., Pfeiffer, P., Babakhin, Y., Jeblick, M., Dhankhar, N., Fodor, G., et al.
ConferenceonLearningRepresentations. (2024). H2o-danube-1.8b Technical Report. arXiv [Preprint]. arXiv:2401.16818.
doi:10.48550/arXiv.2401.16818
| Jaques, N., | Gu, S., Bahdanau, |     | D., Hernandez, | J. M., | Turner, | L. R. E., | and |     |     |     |     |     |     |
| ----------- | ----------------- | --- | -------------- | ------ | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Eck, D. (2017). “Tuning recurrent neural networks with reinforcement learning,” Stern, D., Herbrich, R., and Graepel, T. (2009). “Matchbox: large scale bayesian
in Proceedings of the 5th International Conference on Learning Representations recommendations,” in Proceedings of the 18th International World Wide Web
(Toulon). Conference(NewYork,NY:AssociationforComputingMachinery).
Jaques,N.,Gu,S.,Turner,R.E.,andEck,D.(2016).“Generatingmusicbyfine-tuning Team,G.,Mesnard,T.,Hardin,C.,Dadashi,R.,Bhupatiraju,S.,Pathak,S.,etal.(2024).
recurrentneuralnetworkswithreinforcementlearning,”inProceedingsofthe30th Gemma:OpenModelsBasedonGeminiResearchandTechnology.arXiv[Preprint].
| ConferenceonNeuralInformationProcessingSystems. |     |     |     |     |     |     | arXiv:2403.08295. |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Jin,M.,Wang,S.,Ma,L.,Chu,Z.,Zhang,J.Y.,Shi,X.,etal.(2024).“Time-LLM:Time Touvron,H.,Lavril,T.,Izacard,G.,Martinet,X.,Lachaux,M.-A.,Lacroix,T.,etal.
seriesforecastingbyreprogramminglargelanguagemodels,”inProceedingsofthe12th (2023a).Llama:OpenandEfficientFoundationLanguageModels.arXiv[Preprint].
| InternationalConferenceonLearningRepresentations(Vienna). |     |     |     |     |     |     | arXiv:2302.13971. |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Jung, H., Lee, S., Yim, J., Park, S., and Kim, J. (2015). “Joint fine-tuning in deep Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., et al.
neuralnetworksforfacialexpressionrecognition,”inProceedingsofthe2015IEEE (2023b).Llama2:OpenFoundationandFine-TunedChatModels.arXiv[Preprint].
| InternationalConferenceonComputerVision(Santiago:IEEE). |     |     |     |     |     |     | arXiv:2307.09288. |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Kang, S., Hwang, J., Lee, D., and Yu, H. (2019). “Semi-supervised learning for Tukey,J.(1949).Comparingindividualmeansintheanalysisofvariance.Biometrics5,
cross-domainrecommendationtocold-startusers,”inProceedingsofthe28thACM 99–114.doi:10.2307/3001913
InternationalConferenceonInformationandKnowledgeManagement.(NewYork,NY:
Wan,Z.,Wang,X.,Liu,C.,Alam,S.,Zheng,Y.,Liu,J.,etal.(2024).“Efficientlarge
AssociationforComputingMachinery).
languagemodels:Asurvey,”inACMTransactionsonInteractiveIntelligentSystems
Khalid, A., Lundqvist, K., Yates, A., and Ghzanfar, M. A. (2021). Novel online (NewYork,NY:AssociationforComputingMachinery).
recommendationalgorithmformassiveopenonlinecourses(nor-moocs).PLoSONE.
16:e0245485.doi:10.1371/journal.pone.0245485 Wang-Cheng Kang, J. M. (2018). “Self-attentive sequential recommendation,” in
|                                                                       |     |     |     |     |     |     | Proceedingsofthe18thIEEEInternationalConferenceonDataMining |     |     |     |     | (Singapore: |     |
| --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | ----------- | --- |
| Kingma,D.P.,andBa,J.(2015).“Adam:amethodforstochasticoptimization,”in |     |     |     |     |     |     | IEEE).                                                      |     |     |     |     |             |     |
Proceedingsofthe3rdInternationalConferenceonLearningRepresentations(SanDiego,
Wei,W.,Ren,X.,Tang,J.,Wang,Q.,Su,L.,Cheng,S.,etal.(2024).“LLMRec:Large
CA).
languagemodelswithgraphaugmentationforrecommendation,”inProceedingsofthe
Kuznetsov, S., and Kordík, P. (2023). Improving recommendation diversity and 17thACMInternationalConferenceonWebSearchandDataMining(NewYork,NY:
serendipitywithanontology-basedalgorithmforcoldstartenvironments.Int.J.Data AssociationforComputingMachinery).
Sci.Analyts.20,431–443. Wei,Y.,Wang,X.,Li,Q.,Nie,L.,Li,Y.,Li,X.,etal.(2021).“Contrastivelearningfor
Li, J., Ren, P., Chen, Z., Ren, Z., Lian, T., and Ma, J. (2017). “Neural attentive cold-startrecommendation,”inProceedingsofthe29thACMInternationalConference
session-based recommendation,” in Proceedings of the 26th ACM Conference on onMultimedia.doi:10.1145/3474085.3475665
InformationandKnowledgeManagement(NewYork,NY:AssociationforComputing
|     |     |     |     |     |     |     | Wu, S., Tang, | Y., Zhu, Y., Wang, | L., | Xie, X., | and Tan, T. | (2019). “Session-based |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------ | --- | -------- | ----------- | ---------------------- | --- |
Machinery). recommendation with graph neural networks,” in Proceedings of the 33rd AAAI
Lika, B., Kolomvatsos, K., and Hadjiefthymiades, S. (2014). Facing the cold ConferenceonArtificialIntelligence(Washington,DC:AAAIPress).
start problem in recommender systems. Expert Syst. Appl. 41, 2065–2073. Yin, X., Chen, W., Wu, X., and Yue, H. (2017). “Fine-tuning and visualization
doi:10.1016/j.eswa.2013.09.005
|     |     |     |     |     |     |     | of convolutional | neural networks,” | in  | Proceedings | of the 12th | IEEE Conference | on  |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ----------------- | --- | ----------- | ----------- | --------------- | --- |
Linden, G., Smith, B., and York, J. (2003). Amazon.com recommendations: IndustrialElectronicsandApplications(SiemReap:IEEE).
| item-to-item | collaborative | filtering. | IEEE | Intern. | Comp. | 7, 76–80. |     |     |     |     |     |     |     |
| ------------ | ------------- | ---------- | ---- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
Yu,F.,Zhu,Y.,Liu,Q.,Wu,S.,Wang,L.,andTan,T.(2020).“Tagnn:Targetattentive
doi:10.1109/MIC.2003.1167344
graphneuralnetworksforsession-basedrecommendation,”inProceedingsofthe43rd
Liu, Q., Zeng, Y., Mokhosi, R., and Zhang, H. (2018). “Stamp: Short-term InternationalACMSIGIRConferenceonResearchandDevelopmentinInformation
attention/memoryprioritymodelforsession-basedrecommendation,”inProceedings Retrieval.(NewYork,NY:TransactionsonMachineLearningResearch).
ofthe24THACMConferenceonKnowledgeDiscoveryandDataMining(NewYork,
Zhang,P.,Zeng,G.,Wang,T.,andLu,W.(2024).TinyLlama:AnOpen-SourceSmall
NY:AssociationforComputingMachinery).
LanguageModel.arXiv[Preprint].arXiv:2401.02385.
| Lops, P., Jannach, | D., Musto,      | C., | Bogers,     | T., and     | Koolen, M. | (2019). Trends |                |                         |             |               |                |              |         |
| ------------------ | --------------- | --- | ----------- | ----------- | ---------- | -------------- | -------------- | ----------------------- | ----------- | ------------- | -------------- | ------------ | ------- |
|                    |                 |     |             |             |            |                | Zhang, R.,     | dong Liu, Q., Chun-Gui, |             | W., Jia-Xuan, | J.-X.,         | and Huiyi-Ma | (2014). |
| in content-based   | recommendation. |     | User Model. | User-Adapt. | Interact.  | 29, 239–249.   |                |                         |             |               |                |              |         |
|                    |                 |     |             |             |            |                | “Collaborative | filtering for           | recommender | systems,”     | in Proceedings | of           | the 2nd |
doi:10.1007/s11257-019-09231-w InternationalConferenceonAdvancedCloudandBigData(Washington,DC:IEEE
| Ma,Y.,Ouyang,R.,Long,X.,Gao,Z.,Lai,T.,andFan,C.(2023).Doris:Personalized |     |     |     |     |     |     | ComputerSociety). |     |     |     |     |     |     |
| ------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
course recommendation system based on deep learning. PLoS ONE. 18:e0284687. Zhang, R., dong Liu, Q., Chun-Gui, W., Jia-Xuan, J. X., and Huiyi-Ma (2019).
doi:10.1371/journal.pone.0284687
“BERT4Rec:Sequentialrecommendationwithbidirectionalencoderrepresentations
Man,T.,Shen,H.,Jin,X.,andCheng,X.(2017).“Cross-domainrecommendation: from transformer,” in Proceedings of the 28th ACM International Conference on
anembeddingandmappingapproach,”inProceedingsofthe26thInternationalJoint InformationandKnowledgeManagement(NewYork,NY:AssociationforComputing
| ConferenceonArtificialIntelligence(AAAIPress). |     |     |     |     |     |     | Machinery). |     |     |     |     |                 |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --------------- | --- |
| FrontiersinArtificialIntelligence              |     |     |     |     |     |     | 07          |     |     |     |     | frontiersin.org |     |