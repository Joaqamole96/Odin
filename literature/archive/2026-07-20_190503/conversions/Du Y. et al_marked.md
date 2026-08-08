PAnDA: Combating Negative Augmentation via Large Language
Models for User Cold-Start Recommendations
YantongDu RuiChen* XiangyuZhao*
HarbinEngineeringUniversity HarbinEngineeringUniversity CityUniversityofHongKong
Harbin,China Harbin,China HongKong,China
duyantong94@hrbeu.edu.cn ruichen@hrbeu.edu.cn xianzhao@cityu.edu.hk
QilongHan A.K.Qin
HarbinEngineeringUniversity SwinburneUniversityofTechnology
Harbin,China Hawthorn,Victoria3122,Australia
hanqilong@hrbeu.edu.cn kqin@swin.edu.au
Abstract Keywords
Thecold-startproblemremainsalong-standingchallengeinrec- Cold-startrecommendations;largelanguagemodels;dataaugmen-
ommender systems. Recent advances in large language models tation;meta-learning
(LLMs)haveopenednewavenuesforaddressingcold-startsce-
ACMReferenceFormat:
nariosthroughdataaugmentation.However,existingcold-start
YantongDu,RuiChen*,XiangyuZhao*,QilongHan,andA.K.Qin.2025.
augmentationmethodsoftensufferfromnegativeaugmentation,
PAnDA:CombatingNegativeAugmentationviaLargeLanguageModels
manifestingasincompleteaugmentation,wheregeneratedinterac-
forUserCold-StartRecommendations.InProceedingsofthe34thACMInter-
tionsfailtocomprehensivelyreflectuserpreferences,andinaccurate nationalConferenceonInformationandKnowledgeManagement(CIKM’25),
augmentation,wheretheyconflictwithuserintent.Theseissues November10–14,2025,Seoul,RepublicofKorea.ACM,NewYork,NY,USA,
largelystemfromtwolimitations:(1)theinabilitytoeffectively 11pages.https://doi.org/10.1145/3746252.3761080
incorporatecollaborativesignals,whicharecriticalforpreference
alignment,and(2)thelackofawarenessofthedownstreammodel’s 1 Introduction
learningdynamicsduringdataaugmentation.Tothebestofour
Recommender systems have played a crucial role in mitigating
knowledge,thelatterhasnotbeenstudiedintheliterature.
informationoverloadinawiderangeofreal-worldapplicationsby
Consequently,weproposeanovelframeworknamedPAnDA.
efficientlyprovidingonlineuserswithrelevantcontent.Existing
Toaddresstheincompleteaugmentationissue,weproposeamodel-
recommendationmodels,suchascollaborativefiltering[7]and
agnosticpreference-alignedaugmentationmoduletoiteratively
content-basedmethods[4,8],typicallyrecommendappropriate
extract and fuse textual information and collaborative informa-
itemstousersbylearninguser/itemrepresentationsfromtheir
tionbyuser-userpreferencematchinganduser-itempreference
historicalinteractions(e.g.,clicks,ratings,purchases).Itisnatural
coherence,whichtogetherformacontextualcuetoguidetheaug-
thatthisideawouldfailinscenarioswhereuser-iteminteractions
mentor to generate high-quality augmented data. To overcome
arelimited,whichisknownasthecold-start problem[2,32],a
theinaccurateaugmentationissue,weproposeamodel-specific
long-standingchallengeforrecommendersystems.
downstream-model-awareadaptationmoduletoadaptivelyalign
Anintuitivestrategytoaddressthecold-startproblemistogen-
theaugmenteddatawiththemodel’sstatesduringthetraining
erateadditionaluserinteractions(i.e.,dataaugmentation)toenrich
process,guidedbygradientsimilarity.Extensiveexperimentson
userbehaviorsandfurtherguidemodellearning.Thisallowsrec-
threepublicbenchmarkdatasetsdemonstratethatPAnDAoutper-
ommendationmodelstocapturemorediverseuserpreferences,as
formsdifferentgroupsofstate-of-the-artcold-startrecommenda-
illustratedinFig.1(a).Somestudieshaveexploredmulti-modal
tionmethodsinallscenarios.Thesourcecodeispubliclyavailable
augmentation,leveragingauxiliaryinformationsuchasimages[38],
athttps://github.com/YantongDU/PAnDA.
audio[9],andtext[30,38]tosimulateinteractionsthatbetterrepre-
sentusers’interests.Morerecently,theemergenceoflargelanguage
CCSConcepts
models(LLMs)hasopenedupnewopportunitiesfordataaugmen-
•Informationsystems→Personalization;Informationex-
tationinrecommendationtasks[22,30].Owingtotheirextensive
traction;•Computingmethodologies→Machinelearning.
worldknowledgeandstrongcapabilitiesinlanguagegenerationand
reasoning,LLMsareincreasinglyregardedaspromisingaugmenta-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
tiontoolsincold-startscenarios[35].Theycancomplementsparse
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation useroriteminformationandgeneratecontextuallyappropriateaug-
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe mentedinteractions.However,existingaugmentationmethodsstill
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
sufferfromsignificantlimitationsincold-startsettings.Duetothe
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. difficultyofmulti-modalalignmentandlimitedmodelgenerative
CIKM’25,Seoul,RepublicofKorea capabilities,thesemethodsstruggletoaccuratelycaptureuserpref-
©2025Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
erencesandcanresultinaugmentedinteractionsthatcontradict
ACMISBN979-8-4007-2040-6/2025/11
https://doi.org/10.1145/3746252.3761080 userintents,misleadmodellearning,anddegraderecommendation
3844

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
performance,callednegativeaugmentation,asshowninFig.1(b). User
Itcanbefurthercategorizedintotwocorechallenges.Fromthe
dataperspective,therelianceonmulti-modalinformationoften Item
resultsinincompleteaugmentation,asitfailstocomprehensively
Collaborative captureuserpreferences.Fromthemodelperspective,limitedgen- Data Augmentator signals
erativecapabilitycanleadtoinaccurateaugmentation,wherethe
augmentedinteractionsmisalignwithuserintents.
Toachievecompletedataaugmentation,recentmethodshave
attemptedtointegratecollaborativesignalswithmulti-modalin- User Collaborative signals
formation[9,31].However,effectivelyfusingtheseheterogeneous
Item
sourcesremainsanopenchallenge.Thischallengeisfurtherex-
acerbatedincold-startscenarios,wherelimitedinteractiondata
(a) Traditional data augmentation
makesitevenmoredifficulttobalancethecomplementarystrengths
ofcontentsemanticsandcollaborativepatterns.Asaresult,aug-
mentedinteractionsareoftenbiasedtowardasinglemodalityor
signaltype,failingtoprovideaholisticrepresentationofuserpref-
erencesandultimatelydegradingtheperformanceofdownstream
recommendationmodels.
Ontheotherhand,inaccurateaugmentationarisesfromthecapa-
bilitylimitationsofgenerativemodels.Forexample,clickbaittitles
ormismatchedimage-textpairs[8,31,40]mayguidethemodelto
augmentinteractionsthataresuperficiallyrelevantbutsemanti-
callyinconsistentwiththeuser’strueintent.Incorporatingsuch
inaccurateaugmentationintomodeltrainingindiscriminatelynot
onlyintroduceslabelnoisebutcanalsodistortlearnedpreference
distributionsandincreaseoverfittingrisks.Inextremecases,this
maycausethemodeltoover-personalizeorrecommendirrelevant
items,furtherdeterioratingtheuserexperience.Moreover,theaug-
menteddatawillbeconsumedbyadownstreamrecommendation
model.Differentmodelshavedisparatelearningcapabilitiesand
thusexpectdifferentextents/typesofdataaugmentation(e.g.,the
numberofaugmentedinteractionsneededforacold-startuser),
suggestingthatLLM-baseddataaugmentationneedstobeawareof
thedownstreammodel.Morespecifically,thedownstreammodel’s
trainingstatusneedstobeconsideredinthedataaugmentation
process.Therefore,mitigatinginaccuracywhileensuringcompat-
ibilitywiththedownstreamrecommendationmodelpresentsan
additionalchallengeforLLM-baseddataaugmentation.
Toaddressthesetwochallenges,weproposeanovelpreference-
alignedanddownstream-model-awaredataaugmentationframe-
workPAnDAinspiredbythepre-trainandfine-tuneparadigm[16,
17,38],whichconsistsoftwocomplementarymodules,asshownin
Fig.1(c).Amodel-agnosticpreference-alignedaugmentationmodule
likeapre-trainingstage,andamodel-specificdownstream-model-
awareadaptationmodulelikeafine-tuningstage.Specifically,to
mitigateincompleteaugmentation,wefocusongeneratingdiverse
andcomprehensiveuser-iteminteractions.Weperformtheuser-
userpreferencematchingbyfocusingonpreferencedifferences
betweenusersanddesigningauniqueprompttobeusedasacon-
textualcuetoassistLLMsingeneratingaugmentedinteractions.
Additionally,weleverageuser-itempreferencecoherencetofur-
thermodelcollaborativestructures,enablingmorepersonalised
andaccurateaugmentation.Thesetwocomponentsworkintandem
tointegratebothmulti-modalcontentandcollaborativesignals,
achievingmorecompletedataaugmentation.Toaddressinaccurate
augmentation,wefurtherintroduceamodel-specificadaptation
module. This component dynamically assesses the relevance of
Representations
User
Item
Representations
User Multi-modal data
Item
(b) Multi-modal data augmentation
Representations
Multi-modal data Similar user
Data Augmentator Guide i M nf u o l r t m i-m at o io d n a s l
Data Augmentator
Multi-modal fusion Guide
User Multi-modal Negative User informations
augmentation
Item Item
Ideal augmentation Incomplete augmentation Inaccurate augmentation Dynamic accuracy augmentation
(c) Our method
Figure1:Anillustrationofdifferentdataaugmentationmeth-
odsinthecold-startrecommendationscenario.
eachaugmentedsamplebymonitoringthelearningstateofthe
downstreamrecommender.Byselectivelyincorporatingordiscard-
ingaugmentedinteractions,itenhancesthealignmentbetweenthe
augmenteddataandthemodel’slearningobjectivesandprevents
noisyorharmfulsamplesfromdegradingperformance.
Tosummarize,themaincontributionsofourworkareasfollows:
• Wearethefirsttoidentifyandstudythenegativeaugmen-
tation in cold-start recommendation, highlighting that more
augmenteddatadoesnotnecessarilyleadtobetterperformance.
Werevealtwounderlyingchallenges:incompleteaugmentation
fromthedataperspectiveandinaccurateaugmentationfrom
themodelperspective,whichdegradetheeffectivenessofdata
augmentationmethods.
• Weintroduceanovelpreference-alignedanddownstream-model-
awaredataaugmentationframeworkPAnDApoweredbyLLMs.
Itconsistsofamodel-agnosticpreference-alignedaugmentation
moduleandamodel-specificdownstream-model-awareadapta-
tionmodule,whichtogethereffectivelyaddressthetwolimita-
tions.PAnDAalsofeaturesadecoupleddesigntoaccommodate
differentcombinationsofLLMsanddownstreamrecommenda-
tionmodels.
• Wehaveperformedextensiveexperimentsonthreereal-world
benchmarkdatasetsandshownthatPAnDA,beingbothpreference-
alignedanddownstream-model-aware,canconsistentlyoutper-
formdifferentgroupsofstate-of-the-artcold-startrecommenda-
tionmethodsinallscenarios.
2 Preliminary
In this section, we first introduce the problem formulation and
notations,followedbyageneraloverviewofdataaugmentationin
recommendersystems.
ProblemFormulation.LetUandVdenotethesetsofusersand
items,respectively.Theuser-iteminteractionmatrixisdefinedas
𝑨∈0,1|U|×|V|,where𝐴 𝑢𝑣 =1indicatesthatuser𝑢hasinteracted
withitem𝑣.Theinteractionhistoryofuser𝑢isdenotedbyV𝑢 =
𝑣
1
,𝑣
2
,...,𝑣 |V𝑢|.Collaborativefiltering(CF)methodslearnfrom𝑨
toobtainuseranditemID-basedembeddings 𝑬 = {𝑬𝑢 ,𝑬𝑣} for
prediction.However,suchmethodsstruggleincold-startsettings
whereuser/itemIDsareunseen.Toaddressthis,profile-basedCF
methodsincorporatesideinformationP ={P𝑈,P𝑉}forusersand
items,andlearnrepresentationsusingafunction 𝑓 Θ𝑟𝑒𝑐 basedon
3845

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
both𝑨andP.Themodelistrainedbymaximizingtheposterior:
|     | Θ   | ∗ =argmax𝑝(Θ | 𝑟𝑒𝑐|𝑨,P), |     |     |     |     |     |     | 𝑠 =𝑨𝑢 | ⊙𝑨𝑚 , |     | (5) |
| --- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- |
|     |     | 𝑟 𝑒𝑐         |           |     |     | (1) |     |     |     | 𝑢,𝑚   |       |     |     |
Θ𝑟𝑒𝑐
where⊙denoteselement-wisemultiplication.Weselectthetop-K
| w h e re 𝑓 Θ | w i l l ou | t p u t th e fi na | l u s er r | e pr es en ta | t io n 𝒉 𝑢 | c o n tain |     |     |     |     |     |     |     |
| ------------ | ---------- | ------------------ | ---------- | ------------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
𝑟 𝑒𝑐 similarusers𝑺𝑢asauxiliarycontextandcombineeachuser’sprofile
| bo t h co l la | b or at i v e | si g n a ls f ro m 𝑬 | a n d si | d e in fo rm | a t io n 𝑝 | v ia : |                                                            |     |     |     |     |     |     |
| -------------- | ------------- | -------------------- | -------- | ------------ | ---------- | ------ | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|                |               |                      |          |              | 𝑢          |        | (e.g.,age,gender),interactionhistory,andcandidateitemset𝑪𝑢 |     |     |     |     |     | to  |
=𝑓 (𝑨,𝑝 𝑢). constructatextualpromptP 𝑢fortheLLM.TheLLMthengenerates
|     |     | 𝒉𝑢 Θ𝑟𝑒𝑐 |     |     |     | (2) |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
anaugmentedinteractionpairforuser𝑢,consistingofapreferred
Theitem’sfinalrepresentation𝒉𝑣 canalsobeobtainedsimilarly. item𝑣 +,𝑡 andanon-preferreditem𝑣 −,𝑡
|     |     |     |     |     |     |     |     | 𝑢   |     |     | 𝑢 from𝑪𝑢 | via: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | --- |
DataaugmentationforRecommenderSystems.Incold-start
scenarios,thesparsityofinteractionsmotivatestheuseofdata
augmentation.Let𝑓 denotetheaugmentationfunction,which P =Text(𝑢,𝑺𝑢 ,𝑪𝑢 ,𝑨,P),
|     |     | Θ𝑎𝑢𝑔 |     |     |     |     |     |     |     | 𝑢   |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(6)
generatessyntheticinteractions𝑨(cid:101)from𝑨andPvia: {𝑣 +,𝑡,𝑣 −,𝑡}=LLM(P 𝑢),
|     |     |              |        |     |     |     |     |     | 𝑢 𝑢 |     |     |     |     |
| --- | --- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 𝑨(cid:101)=𝑓 | (𝑨,P). |     |     | (3) |     |     |     |     |     |     |     |
Θ𝑎𝑢𝑔 whereText(·)denotesthepromptconstructionfunction.Thecan-
Thedownstreamrecommendermodel𝑓 didate set 𝑪𝑢 is obtained by hard sampling high-ranking items
Θ𝑟𝑒𝑐 isthentrainedwith
fromabaserecommender(e.g.,BPR[21],LightGCN[6]).Thispro-
| theaugmenteddata𝑨𝑎𝑢𝑔 |     | = {𝑨,𝑨(cid:101)} | toexploreuserpreferences, |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | ---------------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichcanbeexpressedvia: cessyieldsthepositiveandnegativeaugmentedinteractionsets
|     |     |                 |     |      |     |     |              | +, 𝑡}           | − , 𝑡}           |             | + ,𝑡|               | − ,𝑡             |                    |
| --- | --- | --------------- | --- | ---- | --- | --- | ------------ | --------------- | ---------------- | ----------- | ------------------- | ---------------- | ------------------ |
|     |     |                 |     |      |     |     | {V (cid:101) | 𝑢 𝑢 a n d       | { V(cid:101) 𝑢 𝑢 | , w h e     | r e |V (cid:101)𝑢 = | |V (cid:101) 𝑢 | | = 𝑀 f or e a c h   |
|     |     | Θ∗=argmax𝑝(𝑨𝑎𝑢𝑔 |     | ,P), |     |     |              | ∈ U             |                  | ∈ U         |                     |                  |                    |
|     |     |                 |     |      |     | (4) | u s e        | r 𝑢 . B y c o n | str a in i n g   | a u g m e n | t a tio n to a pr   | e - fi l te r    | ed ca n di d a t e |
Θ
|                                               |     |     |     |     |     |     | set | and incorporating | similar | users’ | interactions | as  | context, we |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | ------ | ------------ | --- | ----------- |
| whereΘisthetrainableparameterofthemodels,Θ={Θ |     |     |     |     |     | ,Θ  |     |                   |         |        |              |     |             |
𝑎𝑢𝑔 𝑟𝑒𝑐}.
enhancegenerationaccuracyandmitigatenoisefromsparsedata.
Aftertrainingwithaugmenteddata𝑨𝑎𝑢𝑔,therecommendermodel
Consideringtoken-lengthlimitsofLLMs[3,43],weavoidfeeding
| 𝑓 isusedtopredictpreferencescore𝑦ˆ𝑢,𝑣 |     |     |     | byrankingthelikeli- |     |     |                                                        |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ------------------- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| Θ𝑟𝑒𝑐                                  |     |     |     |                     |     |     | thefullitemsetandinsteadrelyonacompact,informativesub- |     |     |     |     |     |     |
hoodofuser𝑢willinteractwithitem𝑣.
set.Overall,theproposedTextualInteractionAugmentation(TIA)
moduleenablestext-drivenaugmentationguidedbycollaborative
3 Methodology
signals,balancinginterpretabilityandpersonalization.
Toaddresstheusercold-startproblem,weproposethePAnDA
|            |             |           |           |              |     |        | 3.1.2 | User-ItemPreferenceCoherence. |           |              | AlthoughLLMs,astheTIA, |            |         |
| ---------- | ----------- | --------- | --------- | ------------ | --- | ------ | ----- | ----------------------------- | --------- | ------------ | ---------------------- | ---------- | ------- |
| framework, | illustrated | in Figure | 2. First, | we introduce | a   | model- |       |                               |           |              |                        |            |         |
|            |             |           |           |              |     |        | fully | leverage                      | auxiliary | information, | they have              | a critical | limita- |
agnosticpreference-alignedaugmentationmodule.Itleveragestex-
tual and collaborative signals for user-user preference matching, tion:theupperboundoftheaugmenteddataqualitydependson
thecandidateitemset𝐶
whereLLMsserveastheTextualInformationAugmentor(TIA). 𝑢.Unfortunately,duetotheconstraints
ofthecold-startscenario,thebaserecommenderalsostrugglesto
Additionally,user-itempreferencecoherenceisusedtocaptureuser
accuratelycaptureuserpreferences,leadingtovaryingqualityfor
| interests | and item | features, with | LLMs | enhancing | personaliza- |     |     |     |     |     |     |     |     |
| --------- | -------- | -------------- | ---- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
candidatesets.Additionally,LLMsprimarilyrelyonprocessingand
tionbyguidingtheintegrationofcollaborativesignalsandmit-
igating incomplete augmentation. Second, we present a model- understandinginputtext,whichleadstothefactthattheaugmented
specificdownstream-model-awareadaptationmodule.Thiscompo- datageneratedbyLLMsstillhaslimitations.Duetotheinputtoken
nentalignsaugmenteddatawiththetrainingsignalsofdownstream limitationsofLLMsandthedifficultyofincorporatingcollaborative
signalsfrominteractiondataintoLLMsandfurthergainingatten-
recommenders,enablingeffectivepreference-alignedaugmentation
tion,wegenerateaugmenteddatacomplementedbycollaborative
andalleviatingdatasparsityincold-startscenarios.
signalsandproposetheCollaborativeSignalAugmentor(CSA).
3.1 Model-AgnosticPreference-Aligned
|     |     |     |     |     |     |     | 3.1.3 | MetaMaskedAutoencoder(MetaMAE). |     |     |     | Toleveragecollabo- |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------------------------------- | --- | --- | --- | ------------------ | --- |
Augmentation rativeinformation,wefine-tunethepre-trainedmodel𝑓
|     |     |     |     |     |     |     |     |     |     |     |     |     | Θ𝑟 𝑝 𝑡 .For |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- |
𝑒 𝑐
3.1.1 User-User Preference Matching. To address the cold-start user𝑢 andaugmentedinteracteditemsetV𝑢,𝑡 =V𝑢 ∪V(cid:101)𝑢 +,𝑡 ,we
problemandeffectivelyleverageauxiliaryinformationforinterpret-
canobtaintheitemsetrepresentationsvia:
inguserpreferencesanditemcharacteristics,wefocusontextual
signalsandemployLLMsastheTextualInformationAugmentor 𝑯𝑢 =𝑆𝑡𝑎𝑐𝑘({𝒉𝑖}𝑖∈V𝑢,𝑡 ), (7)
(TIA).Byconvertingtheaugmentationtaskintoanaturallanguage
|     |     |     |     |     |     |     | which𝑆𝑡𝑎𝑐𝑘(·)isthevectorstackingoperation.𝒉𝑖 |     |     |     |     | ∈R𝑑istherepre- |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | -------------- | --- |
description,LLMsgeneratemeaningfuluser-iteminteractionpairs
foreachuser𝑢,drawingontheirstrongreasoningcapabilitiesand sentationofitem𝑖andobtainedthroughEq.(2),and𝑯𝑢 ∈R|V𝑢,𝑡|×𝑑.
broadknowledge.Wealsoincorporateinteractionhistoriesfrom Tolearnanaccurateandcomprehensiverepresentationoftheuser,
similarusersasreferencestoenhanceaugmentationquality. weutilizetheaugmentedinteractionsgeneratedbyLLMsfrom
Specifically,foreachuser𝑢,weconstructasimilaruserset𝑺𝑢.In theperspectiveofitemstoguidethemodel’slearning,therebyin-
cold-startscenarios,embedding-basedsimilarityisoftenunreliable corporatingrichtextualinformationintotheitemrepresentations.
duetosparseinteractions.Instead,wemeasuresimilaritybased Tomitigatetheimpactofincompleteaugmentation,weemploya
={0,1}∈R1×|𝑉|
oninteractionhistory.Let𝑨𝑢 denotethebinary MaskedAutoencoder(MAE)toenhancetheuser/itemrepresenta-
interactionvectorofuser𝑢,wecomputesimilaritywithuser𝑚as: tionsofusersanditems.
3846

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
|     | Similar User Set |     |     |     | (a) User-User Preference  |     |     |     | History  |     |     |     |
| --- | ---------------- | --- | --- | --- | ------------------------- | --- | --- | --- | -------- | --- | --- | --- |
Gradient
|     |     |     |     |                    |                     | Matching |     |     | Interactions |     |            |     |
| --- | --- | --- | --- | ------------------ | ------------------- | -------- | --- | --- | ------------ | --- | ---------- | --- |
|     |     |     |     |                    |    LLM as Augmentor |          |     |     |              |     | Similarity |     |
|     |     | ... |     | Prompt Constructor |                     |          |     |     |              |     |            |     |
，
|     |     |     |     |     |     |     |     |     |     |  Recommender System | (   | 1,  2) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------ |
Cold-Start
...
|     | Candidate Item Set |     |     |     |     |     |     |     |     |     |     | 1   |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
User
2
|     |     |     |     |     |     | ，   |     |     | Preference- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- |

Aligned
Augmentation
|     |     |     |     |     |     |     |     |     | ，   |     |     | ，   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | ，   |     | ，   |     |
Pre-Trained Model
|     |     |     |           |     |     | ，   |     |     | ，   |     | ，   |     |
| --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |   MetaMAE |     |     | ... |     |     |     |     |     |     |
|     |     |     |           |     |     |     |     |     | ，   |     | ，   |     |
(c) Model-Guided
，
|     | (b) User-Item Preference Coherence |     |     |     |     |     |     |     |     | Filtering Strategy |     |     |
| --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- |
|     |                                    |     |     |     |     |     |     |     |     |                    |     |     |
ℒ
Figure2:ThearchitectureoftheproposedPAnDAmodel.(a)demonstratesthetextualinformationdataaugmentationprocess
withLLMs.(b)describestheMetaMAEaugmentdatawiththecollaborativesignals.(c)introducesthedownstream-model-aware
filteringstrategyforfilteringmodel-mismatchedinteractions.
| T a s k    D e s        | c r i p t i o n                           |                                   |                       |                                                           |                                                                                   |              |        |          |              |                      |                  |     |
| ----------------------- | ----------------------------------------- | --------------------------------- | --------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------ | ------ | -------- | ------------ | -------------------- | ---------------- | --- |
|                         |                                           |                                   |                       |                                                           |                                                                                   | capabilityof | it e m | s, w e u | s e a f e at | u r er e st o r a ti | o n lo s s v ia: |     |
| Y o u   a r e   a   m o | v i e   r e c o m m e n d a t i o n   s y | s t e m   a n d   r e q u i r e d |   t o   Y r o e u q u | a i r r e e d a   t m o o   v r i e e c o r m e m c e o n | m d m   e u n s d e a r t   i A o   n w h s o y   i s t s e   m a   a 2 n 5 d -   |              |        |          |              |                      |                  |     |
r e c o m m e n d   u s e r   A   w h o   i s   a   [ a g e ] - y e a r - o l d   [ g e n d e r ]   y e a r - o l d   m a l e   p e r s o n   a n d   t h e   o c c u p a t i o n   i s     𝛾
| p e r s o n   a n d   t | h e   o c c u p a t i o n   i s   [ o c c | u p a t i o n ]   w i t h   m o v | i e s   w r i t | e r   w i t h   m o v i e s   b | a s e d   o n   u s e r   h i s t o r y   |     |     |     |     |     |     |     |
| ----------------------- | ----------------------------------------- | --------------------------------- | --------------- | ------------------------------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
b a s e d   o n   u s e r   h i s t o r y   t h a t   e a c h   m o v i e   w i t h   t i t l e ,  y e a r ,  t h a t   e a c h   m o v i e   w i t h   t i t l e ,   y e a r ,   t y p e .   1 ∑︁ 𝑯(cid:98) · 𝑯
t y p e .   F o r   r e f e r e n c e ,   w e   a l s o   w i l l  l i s t   a   s i m i l a r   u s e r   F o r   r   e f e r   e n c e ,   w e   a l s o   w i l l   l i s t   a   s i m i l a r     L 𝑢 = (cid:169) − 𝑢 𝑢 (cid:170) ,
B ’ s   h i s t o r y . u U s s e e r r   B A ’ ’ s s   h h i i s s t t o o r r y y . : 𝑓 𝑟 (cid:173) 1 (cid:13) (cid:13) (cid:174) (10)
|     |     |     | B u t c | h   C a s s i d y   a n d   t h | e  S u n d a n c e  K i d ,  1 9 6 9 ,   |     |     | | V 𝑢, | 𝑡 | | (cid:173) (cid:13) 𝑯(cid:98) (cid:13) · ∥ | 𝑯 ∥ (cid:174) |     |
| --- | --- | --- | ------- | ------------------------------- | ---------------------------------------- | --- | --- | ------ | --- | ----------------------------------------- | ------------- | --- |
P r o m p t A c t i o n   C o m e d y   W e s t e r n 𝑣∈ V 𝑢 ,𝑡 (cid:13) 𝑢 (cid:13) 𝑢
|                                                 |                                                     |         | H o m e         |   A l o n e ,   1 9 9 0 ,   C h                             | i l d r e n ' s   C o m e d y               |              |          |              |              | (cid:171)            | (cid:172)         |     |
| ----------------------------------------------- | --------------------------------------------------- | ------- | --------------- | ----------------------------------------------------------- | ------------------------------------------- | ------------ | -------- | ------------ | ------------ | -------------------- | ----------------- | --- |
| U [ s m e o r v i   e A ’   s t   i h t i l s e | t ] o , r   y [ : r e l e a s e   y e a r ] ,   [ t | yp e ]  | U s e r         |   B ’ s     h i s t o r   y :                               |                                             |              |          |              |              |                      |                   |     |
|                                                 |                                                     |         | S T a w b e r l | i v n e a   , M o 1 n 9 k 9 e y 5 , s , C   o 1 m 9 e 9 d 5 | y ,   R D o r m a a m n a c   S e c i - F i | wh e re 𝛾 is | th e s c | a li n g f a | c to r , w h | ic h i s a h y p e r | p ar a m e t e r. |     |
| . [ . m . o v i e   t i t l e                   | ] ,   [ r e l e a s e   y e a r ] ,   [ t           | y p e ] | W h i l         | e   Y o u  W e r e   S l e e p                              | i n g ,  1 9 9 5 ,   C o m e d y            |              |          |              |              |                      |                   |     |
R o m a n c e L a st ,w e a gg r e g a t e t h e l a t en t r ep r e se n t a ti o n o f u s e r 𝑢 thatin-
| U [ s m e o r v   i B e   ’ s t   i t h l i e s | ] t o ,   ry [ : r e l e a s e   y e a r ] ,   [ t | y p e ] | C a n d | i d a t e s : |     |     |     |     |     |     |     |     |
| ----------------------------------------------- | -------------------------------------------------- | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[ 2 0 4 ]   B a c k  t o  t h e  F u t u r e ,  1 9 8 5 ,  C o m e d y   corporatesitem-levelcollaborativesignalsandtextualinformation,
| . [ . m . ovie title], [release year], [type] |     |     | S c i - | F   i Silence of the Lambs, The, 1991,  |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | ------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
C a n d id a t e s : [ D 9 r 8 a ] m a  T h r i l l e r 𝑧 𝑢,withtheprofile-baseduserrepresentation,ℎ
[ i d ]  [ m o v i e title], [release year], [type] [ 5 0 ]  S t a r   W a r s, 1977, Action Adventure  𝑢 obtainedthrough
| . . . |     |     | R o m a | n c e   S c i - F i   W a r |     |     |     |     |     |     |     |     |
| ----- | --- | --- | ------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
[ i d ]   [ mo v i e   t it l e ],   [ r e l e a se   y e a r ] ,   [ t y p e ] P l e a s e   o u t p u t  t h e   i n d e x   o f  u s e r  A ' s   Eq.(2),toconducttheuser’sfinalcollaborativerepresentationvia:
| P l e a s e  o u t p u                                       | t  t h e  i n d e x   o f  u s e r   A | ' s   f a v o r ite and least  | f a v o                        | r  t i t e     a n d   l e   a s t     f | a  f v o r i t  c e   m o v i e .   P lease   |     |     |     |              |     |     |      |
| ------------------------------------------------------------ | -------------------------------------- | ------------------------------ | ------------------------------ | ---------------------------------------- | --------------------------------------------- | --- | --- | --- | ------------ | --- | --- | ---- |
| f a v o r i t e   m o vie. Please give the index in [] from  |                                        |                                | gi ve                          | h e i n d e x i n [ ]                    | r o m a n d i d a t e s .                     |     |     |     |              |     |     |      |
| c a n d i d a t e s .                                        |                                        |                                |       20 4                     | 98                                       |                                               |     |     | 𝒇𝑢  | =(1−𝛼)𝒉𝑢+𝛼𝒛𝑢 | ,   |     | (11) |
| （a）Thestru ctureo ft he LLM augmentat iontask                |                                        |                                | （b）Exa mpleo fL LM aumentation |                                          |                                               |     |     |     |              |     |     |      |
where𝛼 isthetrainableparameter.Then,wecanconductthepre-
Figure3:Anillustrationofthestructureofprompts.The dictionscoreoftheuser𝑢totheitem𝑣via:
figureshowsthepromptdesignedformoviedatasets.For
|                                                         |     |     |     |     |     |     |     |     | 𝑦ˆ𝑢 𝑐 =𝒇𝑢 | ·𝒉𝑣 . |     | (12) |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | --- | ---- |
| theBook-Crossingdataset,weuse[id],[booktitle],[author], |     |     |     |     |     |     |     |     | ,𝑣        |       |     |      |
[genre]asdescriptors. Subsequently,weselectthetop-𝑀 itemswiththehighestpre-
|     |     |     |     |     |     | dictionscoresasaugmentedpositivesamplesV𝑢 |     |     |     |     | +,𝑐 |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
First,foruser𝑢andthesetofpositivesamplesV 𝑢 +generated .Conversely,
-𝑀
b y L L M s , w e se l e ct a s u bs e t v𝑢 ⊆ V + ,𝑡 a n d m a sk th e ir r e p re se n t a - w e s e l e ct th e b o t to m it e m s w it h t h e l ow e s t s c o re s a s n eg at i v e
|     |     | (cid:101) | (cid:101) 𝑢 |     |     |     | − ,𝑐 |     |     |     |     |     |
| --- | --- | --------- | ----------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
[ 𝑀 𝐴 𝑆𝐾 ] sa m p l e s V 𝑢 . T h e co llab o r at iv e s ig n a l w il l t h e n b e f e d in to t h e
| ti on s w i t | h a m a s k to k e | n   | , r e p r es e | n te d as 𝒉 | [𝑀 𝐴 𝑆 𝐾 ] (e .g . , a |     |     |     |     |     |     |     |
| ------------- | ------------------ | --- | -------------- | ----------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
nextiterationtorefinethecandidateitemset𝑪𝑢.
learnablevectorormeanpooling).Themaskingoperationvia:
|     |     | (cid:26) | 𝑣   |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝒉𝑣 i f ∉ (cid:101) v 𝑢 3 .1 .4 M e ta o p t i m i z a t i on f o r M e t a M A E . S i n c e e a c h u s e r ’s p r ef e r -
|     | (cid:101)𝒉𝑣 = |     | 𝑣   | .   | (8) |     |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
𝒉 [MASK] i f ∈ v 𝑢 en c esa re d iff e r e n t , u s i n g a s h ar e d - pa r a m e t e r a u t o en c o d e r w o u l d
(cid:101)
struggletocapturethepersonalizeddifferencesamongusersac-
Itisworthnotingthatweonlyperformthemaskoperationon
curately.Incold-startscenarios,thelimitedinteractiondatacan
theaugmentedinteractionstomakethemodelmorerobustwithout
alsoleadtoundifferentiatedrepresentationsofusersoritems.In-
losingtheoriginalinformation.
spiredbymeta-learning[33,42],wedesignedameta-optimization
| Second,weusethemaskeduserinteractionsetV |     |     |     |     | 𝑀 astheinput |     |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
𝑢
totheautoencoderandreconstructtherepresentationsvia: strategytoensureeachuserhasapersonalizedautoencoderthat
capturestheiruniquepreferencesvia:
|     | ,𝒛𝑢        | =𝐴𝑢𝑡𝑜𝐸𝑛𝑐𝑜𝑑𝑒𝑟(𝑯𝑢 | 𝑀               | ;𝜃 𝐴𝐸), |     |     |     |     |     |                             |     |     |
| --- | ---------- | --------------- | --------------- | ------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- |
|     | 𝑯(cid:98)𝑢 |                 |                 |         | (9) |     |     |     |     |                             |     |     |
|     |            |                 | tationofuser𝑢.𝜃 |         |     |     |     | ∑︁  |     | 𝑡,V(cid:101)𝑢 𝑐(𝜃 𝑢, ∗);Θ), |     |     |
w h e r e 𝒛 𝑢 re p re s e n t s th e l at e n t r e p r e se n 𝐴𝐸 isthe m in L𝑟𝑒𝑐(V𝑢 ,V(cid:101)𝑢
|     |     |     |     |     |     |     | Θ   |     |     | 𝐴 𝐸 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tra i n a b le p a ra m e t e r o f th e a u t o e n c o d e r. 𝑢 ∈U
(13)
T h i r d, w ea t t em p t t o re c o n s t r u ct t h e r e p re se n t a t io n o f t h e in - 𝑠.𝑡.,𝜃 𝑢, ∗←arg ,V(cid:101)𝑢 𝑡,Θ 𝑝 𝑡 𝑐;𝜃 𝐴𝐸),
|              |                      |                  |             |              |                         |     |     |     | m inL𝑓𝑟(V𝑢 |     | 𝑟 𝑒 |     |
| ------------ | -------------------- | ---------------- | ----------- | ------------ | ----------------------- | --- | --- | --- | ---------- | --- | --- | --- |
| ter ac t e d | it em s e t V 𝑢, 𝑡 f | or u s e r 𝑢 . T | o e n h a n | c e th e r e | p r e se n ta t io n al |     |     | 𝐴 𝐸 |            |     |     |     |
|              |                      |                  |             |              |                         |     |     |     | 𝜃𝐴 𝐸       |     |     |     |
3847

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
where𝜃𝑢,∗ represents the personalized autoencoder parameters First,wecomputetheaveragegradientofthelossovertheorigi-
𝐴𝐸
foruser𝑢afterconvergencethroughtrainingwiththeaugmented nalinteractionsetV𝑢,whichrepresentsthemodel’sdirectionfor
data.𝑉
interaction 𝑢 denotes the original set of interacted items updatingparametersbasedontheuser’sactualpreferencesvia:
|     |     | 𝑡   | ,   | 𝑡, ,𝑡 |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f o r t h e u s e r 𝑢 ,w h i le V(cid:101) = { V(cid:101) 𝑢 + V(cid:101) 𝑢 − } r e p r es e n ts th e i te m p a i rs 1 ∑︁
|     |     | 𝑢   |     |     |     |     |     |     | ∇ΘL(V𝑢)= |     |     | ∇ΘL𝑟𝑒𝑐(𝑢,𝑣+,𝑣−), |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---------------- | --- | --- | --- |
a u g m e n t e d b y th e T IA . V(cid:101) 𝑐( 𝜃 𝑢 , ∗ ) = { V(cid:101) +,𝑐 , V − ,𝑐 } d en o te s t he it e m (15)
|                 |     |        | 𝑢 𝐴 𝐸     | 𝑢           | (cid:101) 𝑢 |          |        |     |     |     | |V 𝑢|      |     |     |     |     |
| --------------- | --- | ------ | --------- | ----------- | ----------- | -------- | ------ | --- | --- | --- | ---------- | --- | --- | --- | --- |
|                 |     |        |           | parameters𝜃 |             | 𝑢, ∗.    |        |     |     |     | {𝑣+,𝑣−}∈V𝑢 |     |     |     |     |
| pairs augmented |     | by the | CSA using |             |             | 𝐴 𝐸 L𝑟𝑒𝑐 | is the |     |     |     |            |     |     |     |     |
recommendationlossofthedownstreamrecommendermodel𝑓 Second,foreachaugmentedinteractionpair𝑣˜+,𝑣˜−,wecalculate
Θ,
whichwillbeelaboratedlater.Tofullyintegratewiththetrain- thecosinesimilaritybetweenitsgradientandthegradientofthe
ingprocessofthedownstreamrecommendersystem,weadopted originaluserinteractionstoevaluatealignmentvia:
theend-to-endoptimizationstrategy.Therefore,weemployedthe (cid:10) (cid:11),
|     |     |     |     |     |     |     |     |     | 𝑠𝑖𝑚({𝑣˜+,𝑣˜−},V𝑢)= |     | ∇ΘL𝑟𝑒𝑐(𝑢,𝑣˜+,𝑣˜−),∇ΘL(V𝑢) |     |     |     | (16) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------------------------- | --- | --- | --- | ---- |
reparameterizationtrick[15]toimplementthedataaugmentation
where⟨·,·⟩denotesacosinesimilarityoperatorbetweengradients.
processoftheCSA.MetaMAEincorporatestextualinformation
Last,foreachuser𝑢,wesortallaugmentedinteractionpairs
toenhancetherepresentationcapabilityofthemodel,learning
{𝑣˜+,𝑣˜−}∈V(cid:101)𝑢
comprehensiveuser/itemrepresentationsthatintegratebothcol- bytheirsimilarityscoresanddiscardthosewiththe
lowestalignment.ThemodelthenupdatesitsparametersΘusing
laborativesignalsandtextualinformation.Additionally,usinga
|     |     |     |     |     |     |     |     | the | remaining | interactions, | ensuring |     | that training | is  | guided by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | -------- | --- | ------------- | --- | --------- |
bi-levelmeta-optimizationstrategydistinguishesbetweendiffer-
interactionsconsistentwiththeuser’soriginalpreferencesignals.
| ent users | when generating |     | augmented |     | data, thereby | producing |     |     |     |     |     |     |     |     |     |
| --------- | --------------- | --- | --------- | --- | ------------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
comprehensiveandpersonalizedaugmenteddata.Thisapproach
|     |     |     |     |     |     |     |     | 3.3 | ModelOptimization |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
effectivelyaddressestheissueofincompleteaugmentation.
|     |     |     |     |     |     |     |     | AfterobtainingthecomprehensiveaugmentedinteractionsV(cid:101) |     |     |     |     |     |     | 𝑢   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
3.2 Model-SpecificDownstream-Model-Aware
|     |     |     |     |     |     |     |     | from | TIA and | CSA, we | use them | to train | a new | recommender |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------- | ------- | -------- | -------- | ----- | ----------- | --- |
model𝑓
Adaptation Θ.Thegoalistoaddressthecold-startchallengebylever-
aginghigh-qualityaugmenteddatatolearnaccurateandexpres-
| Weobtainaugmentedinteractionsforuser𝑢,V(cid:101)𝑢 |     |     |     |     |     | = V(cid:101)𝑢 | 𝑡,V(cid:101)𝑢 𝑐,in- |     |     |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
siveuser/itemrepresentations,therebyenhancingrecommendation
cludingtruepositivesandpreference-alignedsamples.However,
performance.Tobettercapturetheunderlyingrelationshipsfrom
notalloftheseinteractionsareequallyusefulforthedownstream
limitedinteractions,weadoptBayesianPersonalizedRanking(BPR)
recommender.Incold-startsettings,thequalityofaugmenteddata
asthetrainingobjectivevia:
varies,andlimiteduserunderstandingmaycausesomesamplesto
L𝑟𝑒𝑐(𝑢,𝑣+,𝑣−)=−log(𝜎(𝑦ˆ𝑢,𝑣+−𝑦ˆ𝑢,𝑣−)),
divergefromthemodel’scurrentlearningtrajectory.Trainingon (17)
allsamplesindiscriminatelyrisksnoise,misleadingoptimization,
whereeachtrainingtriplet(𝑢,𝑣+,𝑣−)issampledfromtheunion
andperformancedrops.Sincemodelsdifferintrainingdynamics, oftheuser’shistoricalandaugmentedinteractions,i.e.,V𝑢∪V(cid:101) 𝑢.
theymayreactdifferentlytothesamedata.Thus,itisessential Thepredictedscores𝑦ˆ𝑢,𝑣+ and𝑦ˆ𝑢,𝑣− aregeneratedby𝑓
Θ.
tocheckeachinteraction’scompatibilitywiththemodel’scurrent
Theentiremodeladoptsabi-leveloptimizationend-to-endtrain-
state.Inspiredbycurriculumlearning,weevaluatesample–model
ingstrategy,wherethetrainingparametersincludetheparameters
alignmentateachiteration,enablingthemodeltoemphasizeinfor-
|     |     |     |     |     |     |     |     | 𝜃 𝐴𝐸 | oftheMetaMAEandtheparametersΘofthedownstreamrec- |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
mativedataandfiltermismatchedones,improvingrepresentations ommendermodel.TheobjectiveisshowninEq.(13).Similartothe
withoutdistortinguserintent.
trainingapproachinmeta-learning,themodeltrainingprimarily
Specifically,wedefinethetraininglossforuser𝑢’sinteractions:
consistsofinner-loopoptimizationandouter-loopoptimization.
∑︁ L𝑟𝑒𝑐(𝑢,𝑣+,𝑣−), I n n e r- L o o p O p ti m i z a t io n . T h e p r im a r y g o a l o f t h is o p ti m i z a -
|     | L(V𝑢)= |     |          |     |     |     | (14) |        |                                               |            |               |               |              |            | 𝑢 ,∗         |
| --- | ------ | --- | -------- | --- | --- | --- | ---- | ------ | --------------------------------------------- | ---------- | ------------- | ------------- | ------------ | ---------- | ------------ |
|     |        |     |          |     |     |     |      | ti o n | is t o o b tai n                              | th e u s e | r- s pe c ifi | c p e rs o na | l i ze d a u | to e n c o | de r 𝜃 f o r |
|     |        |     | 𝑣+,𝑣−∈V𝑢 |     |     |     |      |        |                                               |            |               |               |              |            | 𝐴 𝐸          |
|     |        |     |          |     |     |     |      | user𝑢  | throughrapidgradientdescent,therebyobtaininga |            |               |               |              |            | c om-        |
whereL𝑟𝑒𝑐(·)isthelossfunctionofthedownstreamrecommender prehensiveandaccuraterepresentation𝒇𝑢 asshowninEq.(11).
| parameterizedbyΘ.Somepriorworkfiltersoutaugmentedinter- |     |     |     |     |     |     |     |                                          |     |     |     |     |     | 𝑐               |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- |
|                                                         |     |     |     |     |     |     |     | Then,wecangenerateaugmentedinteractionsV |     |     |     |     |     | 𝑢 thatprimarily |     |
actionswithhighloss,assumingtheyaremodel-mismatched.How- containcollaborativesignalssupplementedbytextualsignals,as
ever,thisoverlooksakeylimitation:highlossdoesnotnecessarily showninEq.(12).Asadvisedby[19],weuseonegradientdescent
implylowquality.Inmanycases,suchinteractionsareinforma- toapproximatethefinaloptimizedresultvia:
| t i v e ha rd | ex a m p l es | t h a t c a | n im p r | o ve m o | d e l r o b u | s tn e ss . D | i s c a rd i n g |     |     |      |          |      |      |     |      |
| ------------- | ------------- | ----------- | -------- | -------- | ------------- | ------------- | ---------------- | --- | --- | ---- | -------- | ---- | ---- | --- | ---- |
|               |               |             |          |          |               |               |                  |     |     | 𝜃 𝑢, | ∗≈𝜃 𝐴𝐸−𝜔 | ∇𝜃𝐴𝐸 | L𝑢 , |     | (18) |
t h e m m ay le a d t o u n d e r fi t tin g a n d m is s e d l e a r n in g o p p o r t u n it i e s. 𝐴 𝐸 1 𝑓𝑟
where𝜔
Conversely,low-lossinteractionsmaybeuninformativeoreven 1 isthelearningrateofinner-loopoptimization.
misleadingiftheypoorlyreflectuserpreferences.Therefore,loss Outer-Loop Optimization. The optimization objective of this
aloneisnotareliablesignalforevaluatingaugmentationquality. optimization,asshowninEq.(13),remainstoenhancethefinal
Instead,weproposetousegradientsignals[1,11]toassessthe recommendationperformanceofrecommendersystem𝑓 Θ.Addi-
alignmentbetweeneachaugmentedinteractionandthemodel’s tionally,tofullyutilizetheaugmenteddataobtainedfromtextual
currentlearningdirection.Bymeasuringthegradientsimilarity informationandcollaborativesignals,weadaptivelyfilteroutaug-
betweenaugmentedandoriginalinteractions,wecanmoreaccu- mentedinteractionsthatdonotmatchthemodelwiththehelpof
ratelyidentifyandretainusefulsampleswhilefilteringoutthose thetrainingsignals.Thisapproachhelpsthemodellearnmoreaccu-
inconsistentwiththemodel’soptimizationpath. rateuser/itemrepresentationswithoutalteringtheuser’soriginal
3848

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
intent.Ultimately,weupdatetheparameters𝜃 𝐴𝐸 oftheMetaMAE set according to their original papers or carefully tuned on the
andtheparametersΘofthedownstreamrecommendermodelvia: validationset,withthebestresultsreported.Wechoosethetemper-
𝜃 𝐴𝐸 =𝜃 𝐴𝐸−𝜔 2 ∑︁ ∇𝜃𝐴𝐸 L(V𝑢 ,V(cid:101)𝑢 𝑡,V(cid:101)𝑢 𝑐(𝜃 𝐴 𝑢, 𝐸 ∗)), 𝛼 atu to re 0 𝛾 .01 fr . o T m he 0, le 0 a .6 r , n 0 i . n 8 g ,1 r , a a t n es d 𝜔 ini , t 𝜔 ial , i 𝜔 zet a h r e e a s g ea g r r c e h g e a d tio in n t p h a e ra r m an e g t e e s r
𝑢∈U
∑︁ (19) [5e−5,1e−3],[1e−4,8e−4],and[
1
1e−
2
4,8e
3
−4],respectively.Wesetthe
Θ=Θ−𝜔
3
∇ΘL(V𝑢),
numberofcandidateitemsto20foralldatasets.Eachuserreceives
𝑢∈U 5 augmented positive and 5 negative samples, and 3 item pairs
where𝜔 2 ,𝜔 3 arethelearningratesofouter-loopoptimization.It arefilteredoutusingadownstream-model-awarestrategy.The
isworthmentioningthatwefocusonupdatingthemeta-model LLMusedinPAnDA(Table2)isGPT-4o4,whileKARandLLMRec
parameters𝜃 𝐴𝐸 ratherthantheuser-specificpersonalizedautoen- useLLaMA3-8B-Chat5duetocostconsiderations.Wealsoreport
coder𝜃
𝐴
𝑢,
𝐸
∗obtainedintheinner-loopoptimization.
PAnDA’sperformancewithLLaMA3-8B-Chatforcomparison.Our
implementationisbasedonPyTorch2.0.0andPython3.11.1,with
4 Experiments
theRecBolelibrary[41].Experimentsarerunonaworkstation
Inthissection,weconductexperimentstoanswerthefollowing withanIntelXeonPlatinum2.40GHzCPU,NVIDIAQuadroRTX
researchquestions(RQs): 8000GPU,and754GBRAM.
• RQ1:HowdoesourPAnDAperforminthecold-startscenario
4.2 OverallPerformanceComparison(RQ1)
comparedtothecurrentstate-of-the-artbaselines?
• RQ2:Whatistheimpactofcriticalcomponentsontheperfor- WereportthemainexperimentalresultsinTable2.Fromtheresults,
mance? wecandrawthefollowingconclusions:
• RQ3:HowdodifferentLLMsimpactPAnDA? First,ourmodel,PAnDA,consistentlyoutperformsallother
• RQ4:Howsensitiveisthemodeltodifferentparameters? baselinemodels,indicatingitsrobustnessandeffectivenessinad-
• RQ5:Howdoesthemodelaugmentedsampledifferfromother dressingthecold-start.Thissuperiorityisachievedbyincorpo-
samples? ratingahigh-qualitydataaugmentationstrategythatgenerates
comprehensiveaugmenteddataandadaptivelyselectshigh-quality
4.1 ExperimentalSetup augmentedsamplesbasedonmodeltrainingsignals.Thisadaptive
4.1.1 Datasets. WeevaluatePAnDAonthreewidelyusedreal- approachensuresthatthemodelbenefitsfromthemostrelevant
worldbenchmarkdatasets:(1)MovieLens(ML-1M)1,(2)Netflix2, andinformativedata,leadingtosignificantperformancegains.
(3)Book-Crossing3. Second,PAnDAdemonstratessubstantialimprovementsover
Followingpriorworks[13,14,18],wesimulatecold-startsce- traditionalcold-startrecommendermodelssuchasDropoutNetand
nariosbyretainingonlyuserswithnomorethan100interactions. state-of-the-artMAML-basedmethods.Thisresultunderscoresthe
Eachdatasetissplitintotraining,validation,andtestsetswitha importanceofleveragingtextualsignalsincold-startscenarios,as
ratioof8:1:1.DatasetstatisticsaresummarizedinTable1. thesesignalsprovidecrucialcontextualinformationthatneedstobe
includedinsparseuser-iteminteractiondata.Moreover,theresults
4.1.2 Evaluation Metrics. We assess model performance using:
highlightthatdataaugmentation,particularlywhencombinedwith
(1)Recall@K (R@K),(2)NormalizedDiscountedCumulativeGain
adaptiveselectionmechanisms,offersapromisingandpractical
(N@K),and(3)Precision@K (P@K).Tomitigatetestsamplingbias,
directionforovercomingthelimitationsofcold-startscenarios.
weadopttheall-rankingevaluationstrategy[31].Resultsareav-
Atlast,PAnDAalsodemonstratessubstantialimprovements
eragedoverfiveindependentruns,with𝐾 setto10,20,and50.
overtraditionalcold-startrecommendationmethods,suchasDropout-
Statisticalsignificanceisassessedvia𝑝-valuescomputedagainst
Net, and state-of-the-art MAML-based methods, such as TDAS
thebest-performingbaseline.
andM2EU.Thesetextualsignalsprovideessentialcontextualin-
4.1.3 Competingmodels. TodemonstratetheeffectivenessofPAnDA, formationthatcomplementscollaborativesignals,particularlyin
wecompareourmodelwith:(i)CF-basedmethodsincludingBPR[21], cold-startscenarioswhereinteractiondataislimited.Furthermore,
LightGCN[6]andNGCF[28].(ii)Augmentation-basedmethods the results highlight the critical role of adaptive data selection
includingDropoutNet[24],CL4SRec[36],L2Aug[25],KAR[34] mechanisms.Bydynamicallyfilteringandselectingthemostrel-
andLLMRec[30].(iii)Cold-startmethodsincludingM2EU[33] evantaugmentedsamples,PAnDAensuresthatthemodellearns
andTDAS[42]. frompreference-aligned,contextuallyaligneddata,settinganew
benchmarkforaddressingcold-startchallengesinrecommendation
4.1.4 Implementationdetails. Wefixtheembeddingsizeofeach
systems.Insummary,theexperimentalresultsvalidatetheeffective-
profilefeature(e.g.,age,gender)to32andsetthetrainingbatch
nessofPAnDAinovercomingthelimitationsofexistingcold-start
sizeto2048forbothdatasets.Embeddingparametersareinitial-
recommendationmethods.Byintegratingtextualandcollaborative
izedusingaGaussiandistribution[23].Weapplyearlystopping
signalsintoaunifiedaugmentationframeworkandemployingan
whenN@50doesnotimproveformorethan10consecutiveit-
adaptivefilteringstrategy,PAnDAdeliversstate-of-the-artperfor-
erations,selectingthebest-performingmodelduringtrainingas
manceacrossmultipledatasetsandmetrics,establishingarobust
thefinalone.Forallbaselinemodels,hyperparametersareeither
andscalablesolutionforcold-startscenarios.
1https://movielens.org/
2https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data 4https://platform.openai.com/
3http://www2.informatik.uni-freiburg.de/~cziegler/BX/ 5https://llama.meta.com/
3849

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
Table1:Statisticsoftheexperimentaldatasets
|                          | Statistics   |     |     | ML-1M    |     | Netflix    |     | Book-Crossing |
| ------------------------ | ------------ | --- | --- | -------- | --- | ---------- | --- | ------------- |
|                          | #User        |     |     | 3,132    |     | 245,281    |     | 103,459       |
|                          | #Item        |     |     | 3,354    |     | 17,761     |     | 189,284       |
|                          | #Interaction |     |     | 156,507  |     | 10,627,773 |     | 493,175       |
|                          | Sparsity     |     |     | 98.5101% |     | 99.7560%   |     | 99.9975%      |
| Avg.#interactionsperuser |              |     |     | 49.9862  |     | 43.3291    |     | 4.7669        |
userprofiles age,gender,occupation,zip_code age,gender,occupation,zip_code location,age
book_title,book_author,publi-
itemprofiles movie_title,release_year,class movie_title,release_year,class
cation_year,publisher,genre
|     | Rangeofratings |     |     | 1∼5 |     | 1∼5 |     | 1∼10 |
| --- | -------------- | --- | --- | --- | --- | --- | --- | ---- |
Table2:TheexperimentalcomparisonbetweenPAnDAandtheSOTAcold-startmethodsonthetwobenchmarkdatasets.The
bestresultsaremarkedinbold,andthesecond-bestresultsareunderlined.Allimprovementsaresignificantunderatwo-sided
| t-testwith𝑝 | <0.05overthebestbaselines. |                 |      |            |                           |            |                   |               |
| ----------- | -------------------------- | --------------- | ---- | ---------- | ------------------------- | ---------- | ----------------- | ------------- |
|             |                            | CF-basedmethods |      |            | Augmentation-basedMethods |            | Cold-startMethods |               |
| Datasets    | Metrics                    |                 |      |            |                           | KAR LLMRec |                   | PAnDA Improv. |
|             |                            | BPR LightGCN    | NGCF | DropoutNet | CL4SRec L2Aug             |            | TDAS              | M2EU          |
(LLM-based) (LLM-based)
R@10 0.2049 0.2081 0.18 0.2719 0.1478 0.2641 0.5084 0.5106 0.4591 0.4813 0.5891 15.37%
N@10 0.1708 0.1727 0.1505 0.2584 0.0767 0.1343 0.5148 0.4845 0.4266 0.4548 0.5643 16.47%
R@20 0.3015 0.3082 0.2717 0.3689 0.1837 0.3804 0.5933 0.6184 0.5315 0.5798 0.6997 13.15%
ML-1M
N@20 0.2099 0.2127 0.187 0.2912 0.0873 0.1634 0.5367 0.5087 0.4598 0.4757 0.6017 18.28%
R@50 0.4707 0.4752 0.4331 0.5165 0.2845 0.5506 0.7415 0.7612 0.6847 0.7214 0.8516 11.88%
N@50 0.2638 0.266 0.2376 0.3284 0.1204 0.1972 0.6067 0.5536 0.2964 0.5249 0.6644 20.01%
R@10 0.015 0.0158 0.0088 0.0164 0.0115 0.0202 0.0229 0.0229 0.0281 0.0197 0.0315 37.55%
N@10 0.0082 0.0091 0.0066 0.0092 0.0059 0.0098 0.0101 0.0115 0.0151 0.0104 0.0161 40.00%
Book R@20 0.0243 0.0259 0.0159 0.0268 0.0154 0.0324 0.0331 0.0349 0.0382 0.0307 0.0486 39.26%
-Crossing
N@20 0.0107 0.0118 0.0079 0.0121 0.0072 0.0143 0.0150 0.0157 0.0191 0.0144 0.0233 48.41%
R@50 0.0419 0.0466 0.0256 0.0471 0.0292 0.0564 0.0607 0.0631 0.0701 0.0568 0.0811 28.53%
N@50 0.0144 0.0162 0.0091 0.0171 0.0103 0.0203 0.0263 0.0278 0.0324 0.0204 0.0351 26.26%
R@10 0.045 0.0458 0.0388 0.0464 0.0207 0.0497 0.0529 0.0529 0.0482 0.0497 0.0615 16.26%
N@10 0.0382 0.0391 0.0352 0.0392 0.0115 0.0213 0.0415 0.0415 0.0397 0.0404 0.0461 11.08%
R@20 0.0543 0.0559 0.0414 0.0568 0.0326 0.0634 0.0639 0.0649 0.0581 0.0607 0.0786 21.11%
Netflix
N@20 0.0407 0.0418 0.0366 0.0421 0.0143 0.0272 0.0394 0.0457 0.0424 0.0444 0.0533 16.63%
R@50 0.0719 0.0766 0.0556 0.0771 0.0482 0.0861 0.0906 0.0931 0.0781 0.0868 0.1111 19.33%
N@50 0.0444 0.0462 0.0391 0.0471 0.0176 0.0314 0.0523 0.0578 0.0484 0.0504 0.0651 12.63%
Table3:AblationstudyonML-1M.LLMRecemergesasthe
4.3 AblationStudy(RQ2)
second-bestperformingbaselineoverall.
WeconductedaseriesofablationexperimentsonML-1Mtoin-
vestigatethecontributionofcomponentsappliedwithinPAnDA,
| Variants |     | N@10 R@20 | N@20 | R@50 | N@50 |     |     |     |
| -------- | --- | --------- | ---- | ---- | ---- | --- | --- | --- |
asshowninTable3.w/oTIA:TheremovalofTIAleadstoasub-
LLMRec 0.4845 0.6184 0.5087 0.7612 0.5536 stantialdropinperformanceacrossallmetrics.Thisisprimarily
because,withoutintegratingtextualsignals,theaugmentedsamples
| w/oTIA |     | 0.4415 0.5626 | 0.4703 | 0.7056 | 0.5184 |     |     |     |
| ------ | --- | ------------- | ------ | ------ | ------ | --- | --- | --- |
generatedlacksufficientcontextualrichness,therebyincreasing
| w/oCSA |     | 0.5007 0.6176 | 0.5174 | 0.7749 | 0.5689 |     |     |     |
| ------ | --- | ------------- | ------ | ------ | ------ | --- | --- | --- |
theprevalenceoffalsepositivesamples.Theseresultsunderscore
w/oDFS 0.4688 0.5991 0.4954 0.7167 0.5411 theimportanceoftextualinformationinenhancingthemodel’s
understandingofuserpreferences.TheabilityofLLMstoprocess
| PAnDA |     | 0.5643 0.6997 | 0.6017 | 0.8516 | 0.6644 |     |     |     |
| ----- | --- | ------------- | ------ | ------ | ------ | --- | --- | --- |
andintegratethesetextualsignalsplaysapivotalroleinimproving
theoverallqualityoftheaugmenteddata.w/oCSA:Theexclu-
sionofCSAalsoresultsinnoticeableperformancedegradation.
3850

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
| Table4:AblationstudyonML-1M.ImpactofdifferentLLMs |     |     |     |     |     |     | 0.8 |     |     | 0.1  |      |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- |
| onaccuracy,cost,andlatency                        |     |     |     |     |     |     |     |     |     |      | R@20 |     |
|                                                   |     |     |     |     |     |     | 0.6 |     |     | 0.08 |      |     |
N@20
|     | LLMs |     | R@20 | N@20 | Cost | Latency |     |     |     | 0.06 |     |     |
| --- | ---- | --- | ---- | ---- | ---- | ------- | --- | --- | --- | ---- | --- | --- |
0.4
0.04
|     | LLama2-7B-chat |     | 0.6178 | 0.4981 | -     | 33s  |     |                   | R@20 |      |                    |     |
| --- | -------------- | --- | ------ | ------ | ----- | ---- | --- | ----------------- | ---- | ---- | ------------------ | --- |
|     | LLama3-8B-chat |     | 0.6813 | 0.5847 | -     | 1.5s | 0.2 |                   | N@20 | 0.02 |                    |     |
|     | gpt-3.5-turbo  |     | 0.6345 | 0.5381 | $24.2 | 27s  |     |                   |      |      |                    |     |
|     |                |     |        |        |       |      | 0   |                   |      |      | 0                  |     |
|     | gpt-4o-mini    |     | 0.6807 | 0.5833 | $2.4  | 13s  | 1   | 3                 | 5    | 7    | 1 3                | 5 7 |
|     |                |     |        |        |       |      |     | (a) MovieLens-1M  |      |      | (b) Book-Crossing  |     |
|     | gpt-4o         |     | 0.6997 | 0.6017 | $40.3 | 18s  |     |                   |      |      |                    |     |
Table5:Analysisof|C|onML-1MandBook-Crossing. Figure 4: Performance comparison (Recall@20 and
NDCG@20)withvaryingnumbersofaugmenteddatapairs.
|     |     | ML-1M |     |     | Book-Crossing |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|C|
|     |      |      |      |      |      |      | 0.8 |     |     | 0.1  |     |      |
| --- | ---- | ---- | ---- | ---- | ---- | ---- | --- | --- | --- | ---- | --- | ---- |
|     | R@20 | N@20 | P@20 | R@20 | N@20 | P@20 |     |     |     |      |     |      |
|     |      |      |      |      |      |      |     |     |     | 0.08 |     | R@20 |
0.6
|     | 3 0.6514 | 0.5814 | 0.1849 | 0.0407 | 0.0204 | 0.0048 |     |     |     |     |     | N@20 |
| --- | -------- | ------ | ------ | ------ | ------ | ------ | --- | --- | --- | --- | --- | ---- |
0.06
| 10  | 0.6866 | 0.5948 | 0.1906 | 0.0467 | 0.0228 | 0.0051 |     |     |     |     |     |     |
| --- | ------ | ------ | ------ | ------ | ------ | ------ | --- | --- | --- | --- | --- | --- |
0.4
| 20  | 0.6997 | 0.6017 | 0.1987 | 0.0486 | 0.0233 | 0.0053 |     |      |     | 0.04 |     |     |
| --- | ------ | ------ | ------ | ------ | ------ | ------ | --- | ---- | --- | ---- | --- | --- |
| 30  | 0.6915 | 0.6003 | 0.1954 | 0.0479 | 0.0231 | 0.0052 | 0.2 | R@20 |     |      |     |     |
0.02
N@20
| WithoutCSA,themodelreliessolelyonLLM-generatedaugmen- |       |       |                   |     |                 |           | 0   |                   |     |     | 0                  |     |
| ----------------------------------------------------- | ----- | ----- | ----------------- | --- | --------------- | --------- | --- | ----------------- | --- | --- | ------------------ | --- |
|                                                       |       |       |                   |     |                 |           | 1   | 3                 | 5   | 7   | 1 3                | 5 7 |
| tations,                                              | which | often | produce partially |     | aligned samples | that fail |     |                   |     |     |                    |     |
|                                                       |       |       |                   |     |                 |           |     | (a) MovieLens-1M  |     |     | (b) Book-Crossing  |     |
tocaptureuserpreferences.Thisincompletealignmenthampers
|     |     |     |     |     |     |     | Figure | 5: Performance |     | comparison | (Recall@20 | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | --- | ---------- | ---------- | --- |
thedownstreamrecommendermodel’sabilitytoaccuratelyand
NDCG@20)withdiscardaugmenteddatapairs.
comprehensivelylearnuser/itemrepresentations,highlightingcol-
laborativesignals’crucialroleinensuringtheaugmenteddata’s {3,10,20,30},andTable5showsthat |C| = 20givesthebestre-
robustnessandaccuracy.w/oDFS:Theabsenceofdownstream-
sults.Smallervalueslimitthechoices,whilelargervaluesmakethe
modeltrainingfeedbacksignalsleadstoadeclineinperformance,
recommendationmoredifficult.
asithindersthemodel’sabilitytofilteroutsamplesmismatched
Analysisofthe#.augmenteddatapairs.Wecanobservefrom
withthemodel’scurrenttrainingtrajectory.Withoutthisprun- Figure4thattheimpactofthenumberofaugmentedsamplepairs
ing,themodelstrugglestoadapttothediversesetofaugmented variesacrossdifferentdatasets.UnlikeML-1M,theBook-Crossing
samples,resultinginlessconsistentuser/itemrepresentationsand
datasetissparse,makingitdifficulttogeneratecomprehensiveand
ultimatelyleadingtosuboptimalrecommendationperformance.
accurateaugmentedsamples.Asaresult,themodelismoresensi-
Thisemphasizesthenecessityofintegratingfeedbacksignalsto
tivetothenumberofaugmentedsamples.Thisalsoindicatesthat
maintaintherelevanceandqualityofthetrainingdata. thequalityofgeneratedaugmentedsamplesiscriticallyimportant.
Analysisofthe#.discardaugmenteddatapairs.Wecanobserve
4.4 LLMsAnalysis(RQ3)
fromFigure5thattherearemodelmismatchedaugmentedsamples.
Table4presentstheresultsoftheablationstudyanalyzingthe Themodel’sperformanceimprovesbydiscardingthesesamples
impactofdifferentLLMsastextualinformationaugmentorson basedonthemodel’strainingsignals.However,excessivediscard-
PAnDA.Weincludebothopen-sourcemodels(LLaMAseries)and ingmayleadtothelossofhighlyinformativeandhigh-quality
closed-sourcemodels(ChatGPTseries),andcomparetheireffects augmenteddata,harmingthemodel’sperformance.
onaccuracy,cost,andlatency.Theresultsshowthatthechoice
Analysisofthe#.similaruser.WecanobservefromFigure6
ofLLMhasasubstantialinfluenceonperformance:strongermod- thatalthoughtheintroductionofsimilaruserscanimproveLLM’s
elssuchasGPT-4oachievethebestRecall@20andNDCG@20, ability to understand user preferences, over-information brings
whileLLaMA3-8B-chatalsodeliverscompetitiveaccuracyatnegli- performancedegradationbecausethereistoomuchtextualinfor-
giblecostandextremelylowlatencywhendeployedonoptimized mation,anditisdifficultforLLMtofocusonthekeyinformation.
hardware.Thisindicatesaclearcorrelationbetweenmodelscale
4.6 CaseStudy(RQ5)
andperformance,withlargerandmoreadvancedLLMsproviding
moreaccuraterecommendations.Overall,thefindingsdemonstrate AsshowninFigure7,thedifferencesinaugmenteddatagenerated
thatemployinghigher-capacityLLMscansignificantlyimprove
byvariousmethodsforcold-starttasksareevident.Theleftside
PAnDA,highlightingtheimportanceofcarefullyselectingmodels
showsthegroundtruthuserinteractiondataandtherightside
thatbalanceaccuracygainswithefficiencyandcostconsiderations.
displaystheaugmenteddatadistribution.Weassessthequalityof
augmentedsamplesusingthemaximumcosinesimilarity,denoted
4.5 HyperparameterAnalysis(RQ4)
as𝑞,betweeneachaugmentedsample’sembeddingandtheground
|C|.SincetheinputtokenconstraintsoftheLLMs,
Analysisof truthsamples.Thismetricindicatesthequalityoftheaugmented
coupledwiththeproblemoffalsepositiveaugmentedsamples,we samples.TraditionalmethodslikeL2Augstrugglewithaccurately
usethecandidateitemsetCtolimitthecandidateitemsbasedon capturinguserpreferences,leadingtomanyfalse-positivesamples
theLLMsaugmentedsamples.Duetocostconstraints,weexplored (𝑞 ≤ 0.25),whichnegativelyimpactmodellearning.LLM-based
3851

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
1 1
0 0
0 1 3 5
02@R 02@N
0.08 0.08
0 0
0 1 3 5
02@R 02@N
1 1
0 0
0 1 3 5
05@R 05@N
0.1 0.06
0 0
0 1 3 5
05@R 05@N
LargeLanguageModels(LLMs)forRecommendation.LLMs
havegarneredattentioninrecommendersystems,withvariousef-
fortsmadetomodeluserbehaviorwithLLMs[10,20,29].LLMs
havebeenemployedasinferencemodelsinvariousrecommenda-
tiontasks,suchasratingprediction,sequentialrecommendation,
anddirectrecommendation.Recentworkhasfurtherexploredtheir
potentialinaddressingcold-startchallenges,suchasleveraging
language-modelpriorstoovercomeitemcold-start[26],andusing
keyword-drivenretrieval-augmentedLLMstoalleviateusercold-
startissues[12].However,mostpreviousapproachesprimarilyuti-
lizedLLMsasrecommenders[3],focusingontheirtext-processing
capabilitieswhileoverlookingthecollaborativesignalsthattradi-
(a) MovieLens-1M (b) Book-Crossing
Figure6:Analysisofthe#similarusersonML-1MandBook- tionalrecommendersystemsexcelatcapturing.Inthispaper,we
Crossing. combineLLM-baseddataaugmentation[30,43]withtraditional
dataaugmentationmethodsbasedoncollaborativesignals,combin-
ingbothattwolevelstoachievepreference-alignedaugmentation
Ground truth 1259 2065 1266 737 590 736 1270
andimprovetheperformanceofdownstreamrecommendermodels.
LLM as DataAugmentationforRecommendation.Dataaugmen-
augmentor 1259 2065 1266 737 149 94 736 15 tationhasbeenalong-standingresearchfocusinrecommender
（LLMRec）
systems.Commonaugmentationoperationsincludepermutation,
RSs as
augmentor 1259 2065 1266 481 590 36 481 1597 deletion,swapping,insertion,andduplication[17],aswellasmore
（L2Aug)
recentstrategiessuchascounterfactualreasoning[39]andcon-
trastive learning [27]. Despite these efforts, the quality of aug-
Ours 1259 2065 1266 737 590 94 736 1270 menteddataremainsanopenproblem,particularlyinsparseor
cold-startsettings.Inthiswork,werevisitinsertionanddeletion
Available data when
Augmented data operationsfromtheperspectiveofuserpreferencealignmentand
model training
proposePAnDAtailoredforthecold-startscenario.
Available data when model training High-quality augmentations ( )
Augmented data for training Partially-aligned augmentatioqns≥ (0.75 )
0.25<q<0.75 6 Conclusion
Ground truth False-positive augmentations ( )
Figure7:Casestudyonaugmentationsamplqe≤s0b.25ydifferent Inthispaper,weaddressedusercold-startrecommendationvia
augmentors. dataaugmentation.WeanalyzedlimitationsofexistingLLM-based
methodsandidentifiedtwokeypropertiesofhigh-qualityaugmen-
tation:preferencealignmentanddownstream-modelawareness.
methods(LLMRec)useworldknowledgetogeneratepreference-
Basedonthis,weproposedPAnDA,anovelLLM-poweredframe-
alignedsamplesbutstillproducepartiallyalignedandfalse-positive
workthatiterativelyintegratestextualandcollaborativesignalsat
samples,showingthelimitationsofrelyingsolelyontextualinfor-
bothinteractionandrepresentationlevels,whileadaptivelyfilter-
mation.Incontrast,PAnDAgeneratesaugmenteddatathatclosely
inginconsistentsamplesduringtraining.Extensiveexperiments
alignswithvaliduserpreferences,effectivelycapturingaccurate
onthreereal-worlddatasetsconfirmedthebenefitsofgenerating
preferencesandeliminatingfalse-positiveandpartiallyalignedsam-
preference-alignedanddownstream-model-awareaugmenteddata
ples.Bycombiningtextualaugmentation,collaborativesignals,and
forrecommendationtasks.Forfuturework,weplantoenhance
adownstream-model-awarefilteringstrategy,PAnDAaddresses
scalabilityandefficiencyofthebi-leveloptimizationandconduct
datasparsityandqualityissuesincold-startscenarios,providing
morerigorousvalidationsofalignmentwithtrueuserpreferences.
high-quality,preference-alignedaugmentedsamples.
5 RelatedWork Acknowledgments
Cold-startRecommendation.Toaddressthisissue,manyworks ThisworkwassupportedbytheHeilongjiangKeyR&DProgram
useauxiliaryinformationtoimprovecold-startuseroritemrepre- ofChinaunderGrantNo.GA23A915,AustralianResearchCoun-
sentations,suchassocialnetworks[16]orcross-domaindata[4]. cil (ARC) under Grant No. DP200102611, Hong Kong Research
GraphNeuralNetworks(GNNs)furthercapturehigh-orderseman- GrantsCouncil’sResearchImpactFund(No.R1015-23),Collabo-
ticsfromknowledgegraphs[5]andheterogeneousnetworks[37]. rative Research Fund (No.C1043-24GF), General Research Fund
Whensideinformationislimited,contrastivelearning[27]helps (No.11218325),InstituteofDigitalMedicineofCityUniversityof
refinecollaborativeembeddings.Morerecently,meta-learning[5, HongKong(No.9229503),Huawei(HuaweiInnovationResearch
33,42]hasemergedasadominantsolution.Ourmethodinstead Program),Tencent(CCF-TencentOpenFund,TencentRhino-Bird
leveragesLLMstogeneratecontextuallyrelevantsampleswhilere- FocusedResearchProgram),Alibaba(CCF-AlimamaTechKanga-
tainingcollaborativesignals,allowingPAnDAtohandlecold-start rooFundNo.2024002),AntGroup(CCF-AntResearchFund),Didi
morerobustlywithoutcomplexauxiliarydataorgraphstructures. (CCF-DidiGaiaScholarsResearchFund),Kuaishou,andBytedance.
3852

CIKM’25,November10–14,2025,Seoul,RepublicofKorea YantongDu,RuiChen,XiangyuZhao,QilongHan,andA.K.Qin
7 GenAIDisclosureStatement
InProceedingsofthe44thinternationalACMSIGIRconferenceonResearchand
developmentininformationretrieval.1608–1612.
GenAItoolswereactivelyusedaspartoftheresearchmethodology
[18] YuanfuLu,YuanFang,andChuanShi.2020.Meta-learningonheterogeneous
inthiswork.Specifically,LLMswereemployedtogenerateaug- informationnetworksforcold-startrecommendation.InProceedingsofthe26th
mentedtrainingsamplesforcold-startuserswithintheproposed ACMSIGKDDinternationalconferenceonknowledgediscovery&datamining.
1563–1573.
PAnDAframework.Theseaugmentedinteractionswereintegrated [19] AlexNichol,JoshuaAchiam,andJohnSchulman.2018. Onfirst-ordermeta-
intothedataaugmentationpipelineundertheauthors’fullsupervi- learningalgorithms.arXivpreprintarXiv:1803.02999(2018).
[20] XubinRen,WeiWei,LianghaoXia,LixinSu,SuqiCheng,JunfengWang,Dawei
sion.Inaddition,LLMswerealsousedtoassistwithminorediting
Yin,andChaoHuang.2024.Representationlearningwithlargelanguagemodels
andwordingimprovementsinthemanuscript.AllAI-generated forrecommendation.InProceedingsoftheACMonWebConference2024.3464–
contentwascarefullyreviewedandvalidatedbytheauthorsto 3475.
[21] SteffenRendle,ChristophFreudenthaler,ZenoGantner,andLarsSchmidt-Thieme.
ensureaccuracy,relevance,andalignmentwiththeresearchgoals.
2012.BPR:Bayesianpersonalizedrankingfromimplicitfeedback.arXivpreprint
arXiv:1205.2618(2012).
References [22] ScottSanner,KrisztianBalog,FilipRadlinski,BenWedin,andLucasDixon.
2023.Largelanguagemodelsarecompetitivenearcold-startrecommendersfor
[1] SungyongBaik,JanghoonChoi,HeewonKim,DoheeCho,JaesikMin,andKy- language-anditem-basedpreferences.InProceedingsofthe17thACMconference
oungMuLee.2021.Meta-learningwithtask-adaptivelossfunctionforfew-shot onrecommendersystems.890–896.
learning.InProceedingsoftheIEEE/CVFinternationalconferenceoncomputer [23] LukeVilnisandAndrewMcCallum.2014. Wordrepresentationsviagaussian
vision.IEEE,9465–9474. embedding.arXivpreprintarXiv:1412.6623(2014).
[2] YuweiCao,LiangweiYang,ChenWang,ZhiweiLiu,HaoPeng,ChenyuYou, [24] MaksimsVolkovs,GuangweiYu,andTomiPoutanen.2017. Dropoutnet:Ad-
andPhilipSYu.2023. Multi-taskitem-attributegraphpre-trainingforstrict dressingcoldstartinrecommendersystems. Advancesinneuralinformation
cold-startitemrecommendation.InProceedingsofthe17thACMConferenceon processingsystems30(2017).
RecommenderSystems.322–333. [25] JianlingWang,YaLe,BoChang,YuyanWang,EdHChi,andMinminChen.2022.
[3] Zhikai Chen, Haitao Mao, Hang Li, Wei Jin, Hongzhi Wen, Xiaochi Wei, Learningtoaugmentforcasualuserrecommendation.InProceedingsoftheACM
ShuaiqiangWang,DaweiYin,WenqiFan,HuiLiu,etal.2024. Exploringthe WebConference2022.2183–2194.
potentialoflargelanguagemodels(llms)inlearningongraphs.ACMSIGKDD [26] ShiyuWang,HaoDing,YupengGu,SergulAydore,KoushaKalantari,and
ExplorationsNewsletter25,2(2024),42–61. BranislavKveton.2024.Language-modelpriorovercomescold-startitems.arXiv
[4] WenjingFu,ZhaohuiPeng,SenzhangWang,YangXu,andJinLi.2019.Deeply preprintarXiv:2411.09065(2024).
fusingreviewsandcontentsforcoldstartusersincross-domainrecommendation [27] WenboWang,BingquanLiu,LiliShan,ChengjieSun,BenChen,andJianGuan.
systems.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.33. 2024.PreferenceAwareDualContrastiveLearningforItemCold-StartRecom-
AAAIPress,PaloAlto,California,USA,94–101. mendation.InProceedingsoftheAAAIConferenceonArtificialIntelligence,Vol.38.
[5] DiHan,XiaotianJing,YijunChen,JunminLiu,KaiLiao,andWentingLi.2025. 9125–9132.
Cold-startrecommendationbasedonknowledgegraphandmeta-learningunder [28] XiangWang,XiangnanHe,MengWang,FuliFeng,andTat-SengChua.2019.
positiveandnegativesampling.ACMTransactionsonRecommenderSystems3,3 Neuralgraphcollaborativefiltering.InProceedingsofthe42ndinternationalACM
(2025),1–24. SIGIRconferenceonResearchanddevelopmentinInformationRetrieval.165–174.
[6] XiangnanHe,KuanDeng,XiangWang,YanLi,YongdongZhang,andMeng [29] XiaoleiWang,XinyuTang,WayneXinZhao,JingyuanWang,andJi-RongWen.
Wang.2020.Lightgcn:Simplifyingandpoweringgraphconvolutionnetworkfor 2023.Rethinkingtheevaluationforconversationalrecommendationintheera
recommendation.InProceedingsofthe43rdInternationalACMSIGIRConference oflargelanguagemodels.arXivpreprintarXiv:2305.13112(2023).
onResearchandDevelopmentinInformationRetrieval.ACM,NewYork,NY,USA, [30] WeiWei,XubinRen,JiabinTang,QinyongWang,LixinSu,SuqiCheng,Jun-
639–648. fengWang,DaweiYin,andChaoHuang.2024.Llmrec:Largelanguagemodels
[7] XiangnanHe,LiziLiao,HanwangZhang,LiqiangNie,XiaHu,andTat-Seng withgraphaugmentationforrecommendation.InProceedingsofthe17thACM
Chua.2017.Neuralcollaborativefiltering.InProceedingsofthe26thInternational InternationalConferenceonWebSearchandDataMining.806–815.
ConferenceonWorldWideWeb.InternationalWorldWideWebConferences [31] YinweiWei,XiangWang,XiangnanHe,LiqiangNie,YongRui,andTat-SengChua.
SteeringCommittee,Geneva,Switzerland,173–182. 2021.Hierarchicaluserintentgraphnetworkformultimediarecommendation.
[8] NicoleImmorlica,MeenaJagadeesan,andBrendanLucier.2024. Clickbaitvs. IEEETransactionsonMultimedia24(2021),2701–2712.
quality:Howengagement-basedoptimizationshapesthecontentlandscapein [32] XuanshengWu,HuachiZhou,YuchengShi,WenlinYao,XiaoHuang,andNing-
onlineplatforms.InProceedingsoftheACMWebConference2024.36–45. haoLiu.2024.CouldSmallLanguageModelsServeasRecommenders?Towards
[9] YangqinJiang,LianghaoXia,WeiWei,DaLuo,KangyiLin,andChaoHuang. Data-centricCold-startRecommendation.InProceedingsoftheACMonWeb
2024.Diffmm:Multi-modaldiffusionmodelforrecommendation.InProceedings Conference2024.3566–3575.
ofthe32ndACMInternationalConferenceonMultimedia(ACMMM).ACM,New [33] ZhenchaoWuandXiaoZhou.2023.M2eu:Metalearningforcold-startrecom-
York,NY,USA,7591–7599. mendationviaenhancinguserpreferenceestimation.InProceedingsofthe46th
[10] Wang-Cheng Kang, Jianmo Ni, Nikhil Mehta, Maheswaran Sathiamoorthy, InternationalACMSIGIR.1158–1167.
LichanHong,EdChi,andDerekZhiyuanCheng.2023.DoLLMsUnderstand [34] YunjiaXi,WeiwenLiu,JianghaoLin,XiaolingCai,HongZhu,JiemingZhu,Bo
UserPreferences?EvaluatingLLMsonUserRatingPrediction.arXivpreprint Chen,RuimingTang,WeinanZhang,andYongYu.2024.Towardsopen-world
arXiv:2305.06474(2023). recommendationwithknowledgeaugmentationfromlargelanguagemodels.In
[11] MikhailKhodak,Maria-FlorinaFBalcan,andAmeetSTalwalkar.2019.Adaptive Proceedingsofthe18thACMConferenceonRecommenderSystems.12–22.
gradient-basedmeta-learningmethods.AdvancesinNeuralInformationProcessing [35] ChangrongXiao,SeanXinXu,KunpengZhang,YufangWang,andLeiXia.2023.
Systems32(2019). EvaluatingreadingcomprehensionexercisesgeneratedbyLLMs:Ashowcase
[12] Hai-DangKieu,Minh-DucNguyen,Thanh-SonNguyen,andDungDLe.2025. ofChatGPTineducationapplications.InProceedingsofthe18thWorkshopon
Keyword-drivenretrieval-augmentedlargelanguagemodelsforcold-startuser InnovativeUseofNLPforBuildingEducationalApplications(BEA2023).610–625.
recommendations.InCompanionProceedingsoftheACMonWebConference2025. [36] XuXie,FeiSun,ZhaoyangLiu,ShiwenWu,JinyangGao,JiandongZhang,Bolin
2717–2721. Ding,andBinCui.2022.Contrastivelearningforsequentialrecommendation.In
[13] HoyeopLee,JinbaeIm,SeongwonJang,HyunsoukCho,andSeheeChung.2019. 2022IEEE38thinternationalconferenceondataengineering(ICDE).IEEE,1259–
Melu:Meta-learneduserpreferenceestimatorforcold-startrecommendation.In 1273.
Proceedingsofthe25thACMSIGKDD.1073–1082. [37] GuangpingZhang,DongshengLi,HansuGu,TunLu,andNingGu.2024.Het-
[14] XixunLin,JiaWu,ChuanZhou,ShiruiPan,YananCao,andBinWang.2021. erogeneousGraphNeuralNetworkwithPersonalizedandAdaptiveDiversity
Task-adaptiveneuralprocessforusercold-startrecommendation.InProceedings forNewsRecommendation.ACMTransactionsontheWeb18,3(2024),1–33.
oftheWebConference2021.1306–1316. [38] LingziZhang,XinZhou,ZhiweiZeng,andZhiqiShen.2024.MultimodalPre-
[15] HuafengLiu,JingxuanWen,LipingJing,andJianYu.2019.Deepgenerativerank- trainingforSequentialRecommendationviaContrastiveLearning.ACMTrans-
ingforpersonalizedrecommendation.InProceedingsofthe13thACMConference actionsonRecommenderSystems3,1(2024),1–23.
onRecommenderSystems.34–42. [39] ShengyuZhang,DongYao,ZhouZhao,Tat-SengChua,andFeiWu.2021.
[16] SiweiLiu,XiWang,CraigMacdonald,andIadhOunis.2024. ASocial-aware Causerec:Counterfactualusersequencesynthesisforsequentialrecommen-
GaussianPre-trainedmodelforeffectivecold-startrecommendation.Information dation.InProceedingsofthe44thInternationalACMSIGIRConferenceonResearch
Processing&Management61,2(2024),103601. andDevelopmentinInformationRetrieval.367–377.
[17] ZhiweiLiu,ZiweiFan,YuWang,andPhilipSYu.2021.Augmentingsequential [40] YanZhang,ChangyuLi,IvorWTsang,HuiXu,LixinDuan,HongzhiYin,Wen
recommendationwithpseudo-prioritemsviareverselypre-trainingtransformer. Li,andJieShao.2022.Diversepreferenceaugmentationwithmultipledomains
3853

PAnDA:CombatingNegativeAugmentationviaLargeLanguageModelsforUserCold-StartRecommendations CIKM’25,November10–14,2025,Seoul,RepublicofKorea
forcold-startrecommendations.In2022IEEE38thInternationalConferenceon [42] XuhaoZhao,YanminZhu,ChunyangWang,MengyuanJing,JiadiYu,andFeilong
DataEngineering(ICDE).IEEE,2942–2955. Tang.2023.Task-difficulty-awaremeta-learningwithadaptiveupdatestrategies
[41] WayneXinZhao,ShanleiMu,YupengHou,ZihanLin,KaiyuanLi,YushuoChen, forusercold-startrecommendation.InProceedingsofthe32ndACMInternational
YujieFLu,HuiWang,ChangxinTian,XingyuPan,YingqianMin,ZhichaoFeng, ConferenceonInformationandKnowledgeManagement.3484–3493.
XinyanFan,XuChen,PengfeiWang,WendiJi,YaliangLi,XiaolingWang,and [43] ZhiZheng,WenshuoChao,ZhaopengQiu,HengshuZhu,andHuiXiong.2024.
Ji-RongWen.2021. Recbole:Towardsaunified,comprehensiveandefficient Harnessinglargelanguagemodelsfortext-richsequentialrecommendation.In
frameworkforrecommendationalgorithms.InCIKM. ProceedingsoftheACMonWebConference2024.3207–3216.
3854