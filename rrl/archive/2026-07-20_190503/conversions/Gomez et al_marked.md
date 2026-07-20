Modeling Personality Traits by Predicting Questionnaire Responses as an
Alternative Approach to Filipino Automatic Personality Recognition
AlessandraPauleenI.Gomez,IbrahimD.Kahil,
ShaunVincentN.Ong,EdwardP.Tighe
DepartmentofSoftwareTechnology and CenterforLanguageTechnologies
DeLaSalleUniversity,Manila,Philippines
{alessandra_gomez,ibrahim_kahil,shaun_ong,edward.tighe}@dlsu.edu.ph
|     | Abstract |     |     |     | today. Aspartofitsevolution,personalitypsychol- |     |     |     |     |
| --- | -------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- |
ogyhasbeenintegratedintocomputationalscience;
EmergingresearchinFilipinoAutomaticPer-
|     |     |     |     |     | through | the use of | machine | learning | and natural |
| --- | --- | --- | --- | --- | ------- | ---------- | ------- | -------- | ----------- |
sonalityRecognition(APR)oftenutilizesso-
|     |     |     |     |     | language | processing | (NLP), | personality | recogni- |
| --- | --- | --- | --- | --- | -------- | ---------- | ------ | ----------- | -------- |
cialmediadataforitswidespreadavailability
|                       |     |          |     |            | tion was | made possible |     | by incorporating | data or |
| --------------------- | --- | -------- | --- | ---------- | -------- | ------------- | --- | ---------------- | ------- |
| andnaturalexpression. |     | However, |     | currentap- |          |               |     |                  |         |
signalsfromhuman-machineinteraction,including
| proaches | focusing | on direct | personality | trait |     |     |     |     |     |
| -------- | -------- | --------- | ----------- | ----- | --- | --- | --- | --- | --- |
modelingoftenyieldsubparresults,prompting butnotlimitedtosocialmediaandtelecommunica-
tion(MushtaqandKumar,2022).
| explorationofalternativemethods. |     |     |     | Thus,we |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
exploredanAPRframeworkwhereindividual Works on text-based APR have branched out
personality questionnaire item responses are toincludeattemptstoderivepersonalityfromso-
predictedandthenaggregatedtoestimatetrait
|               |      |           |       |          | cial media | posts | within | a specific | regional con- |
| ------------- | ---- | --------- | ----- | -------- | ---------- | ----- | ------ | ---------- | ------------- |
| scores. Using | text | data from | 2,168 | Filipino |            |       |        |            |               |
text. Therearealotofculturallinguisticnuances
X(formerlyTwitter)users,wetrainedmodels
thatcanserveasintegralpersonalityindicators,yet
foreachitemintheBigFiveInventory(BFI)
relatedtoExtraversionandConscientiousness. modelsarenotalwaysabletoextractinformation
thatproperlyencapsulatestheseintricaciesbrought
| We also experimented |     | with | multiple | configu- |     |     |     |     |     |
| -------------------- | --- | ---- | -------- | -------- | --- | --- | --- | --- | --- |
rations of logistic regression, SVM, and XG- aboutbymultilingualism.
Boost models using TF-IDF and term occur- WiththisnewaspectofAPR,studiesonperson-
| rencevalues. | Findingshighlightthechallenges |     |     |     |     |     |     |     |     |
| ------------ | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
alityrecognitiononFilipinouserdatahavebegun
inpredictingtraitscoresforbothExtraversion
|                       |     |                    |     |     | to take | place. From | attempts | at extraction | meth- |
| --------------------- | --- | ------------------ | --- | --- | ------- | ----------- | -------- | ------------- | ----- |
| andConscientiousness. |     | Whileimplementinga |     |     |         |             |          |               |       |
ods(Agnoetal.,2019;ChuaChiacoetal.,2022)
hierarchicalclassificationschemeattheitem
tomodelingFilipinopersonalitytraitsusingsuper-
| level showed | some | improvement, |     | especially |     |     |     |     |     |
| ------------ | ---- | ------------ | --- | ---------- | --- | --- | --- | --- | --- |
visedlearningmodels(TigheandCheng,2018),Fil-
| for Conscientiousness, |     | overall | trait-level | per- |     |     |     |     |     |
| ---------------------- | --- | ------- | ----------- | ---- | --- | --- | --- | --- | --- |
formanceremainslacking. Overall,whilethe ipinoAPRstudiesareslowlybreakinggroundwith
originalpipelineaswellastheintegrationof the goal of applying techniques that can capture
ahierarchicalapproachshowpotential,signifi- therichlinguisticdiversityofthenation. However,
cantimprovementsareneededbeforethisitem- since this particular branch of study is relatively
| based framework |     | can be effectively |     | used for |     |     |     |     |     |
| --------------- | --- | ------------------ | --- | -------- | --- | --- | --- | --- | --- |
new,therehavebeenunsuccessfulventuresaswell;
APR.
|     |     |     |     |     | at present, | existing | studies | on the | use of higher |
| --- | --- | --- | --- | --- | ----------- | -------- | ------- | ------ | ------------- |
complexitymodelssuchasneuralnetworks(Tighe
1 Introduction
etal.,2020)failedtoyieldgoodresults,especially
Theextentofaperson’sindividualityandidentity consideringthatthiswasattemptedwhenFilipino
| encompassesagreatnumberoffactors,fromtheir |     |     |     |     | userdatawasscarce. |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
dailyexperiencesallthewaytotheirhobbies,in- GiventhecurrentstateofFilipinoAPR,itbegs
terests, and way of interacting with others. Such thequestionofwhetheritispossibletoutilizean-
traits are often considered part of one’s personal- other approach at modeling personality traits in-
ity—definedbytheAmericanPsychologicalAsso- stead of directly generating user personality pro-
ciationasacollectionof“enduringcharacteristics files from social media data. One such alterna-
and behavior that comprise a person’s unique ad- tive is a questionnaire-based approach, wherein
justmenttolife.”Numerousscientifictheoriesand modelstrainedonsocialmediadatawillthenpre-
approacheshavebeencreatedinordertodeepenthe dict how the user might answer a question from
world’sunderstandingofpersonalityintohowitis apersonalityinventory. BycombiningAPRwith

aquestionnaire-basedframework,itmayreveala
newangleofextracting,processing,andanalyzing
| data that will | be able | to account | for the | cultural |     |     |     |     |     |     |     |
| -------------- | ------- | ---------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
linguisticcuesfoundintheFilipinolanguage—and
byextension,canalsobeappliedinthecontextof
general,non-regionalAPRresearch.
Thegeneralobjectiveofthisstudyistoinvesti-
gatetheeffectivenessofaquestionnaireitem-based
predictionapproachtoautomaticpersonalityrecog-
| nition on | social media | text data. | The specific | ob- |     |     |     |     |     |     |     |
| --------- | ------------ | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
jectivesofthestudyaredefinedbelow:
| 1. To define | a list | of qualification | criteria | for |     |     |     |     |     |     |     |
| ------------ | ------ | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
derivingasubsetofthePagkataoKodataset;
2. Toextracttext-basedinformationfromusers’
socialmediaposts;
|     |     |     |     |     | Figure 1: | Diagram | of  | the Overall |     | Research | Pipeline |
| --- | --- | --- | --- | --- | --------- | ------- | --- | ----------- | --- | -------- | -------- |
3. Tobuildandtrainpredictionmodelsforeach FollowingOurProposedItem-BasedApproach
personalityquestionnaireitemusingthegen-
erateduserembeddings;
|     |     |     |     |     | then built | for | each questionnaire |     |     | item | under the |
| --- | --- | --- | --- | --- | ---------- | --- | ------------------ | --- | --- | ---- | --------- |
4. To evaluate and analyze the performance of ExtraversionandConscientiousnesstraits,which
the item-based prediction models at an indi- weretrainedandtested. Thementionedtraitswere
vidual item level and an overall trait score chosen among the Big Five in accordance with
| level;and |     |     |     |     | TigheandCheng’s(2018)findingsaboutthetwo |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
beingtheeasiesttomodel.
5. To compare the item-based prediction ap- Theresultingpredictionsforeachquestionnaire
| proach | to automatic | personality | recognition |     |     |     |     |     |     |     |     |
| ------ | ------------ | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
itemwerethenaggregatedtoestimatetheExtraver-
againstbaselinepredictionmodels
sionandConscientiousnesstraitscoresofeachuser.
|                |          |                 |              |            | Evaluation | of  | the machine |            | learning | models | were   |
| -------------- | -------- | --------------- | ------------ | ---------- | ---------- | --- | ----------- | ---------- | -------- | ------ | ------ |
| The results    | of this  | study represent |              | the output |            |     |             |            |          |        |        |
|                |          |                 |              |            | conducted  | for | each        | individual | item,    | along  | with a |
| of a different | approach | to APR,         | specifically | pre-       |            |     |             |            |          |        |        |
separatetrait-levelevaluationtoassesstheperfor-
dictingusers’Likertscale-typeanswerstotheBFI
manceoftheoverallapproachofutilizingquestion-
questionnaireinsteadofpredictingtheirpersonal-
|                 |           |     |                  |     | naire item | predictions |     | for | estimating | personality |     |
| --------------- | --------- | --- | ---------------- | --- | ---------- | ----------- | --- | --- | ---------- | ----------- | --- |
| ity traitscores | directly. | Due | tothe uniqueness | of  |            |             |     |     |            |             |     |
traitscores.
theapproach,itofferstheviabilityofutilizingthe
| approachtoconductAPRandintroducestheidea |     |     |     |     | 2.1 DataSource |     |     |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
ofpredictingquestionnaireitemsforothermodels
|     |     |     |     |     | The dataset | used | in  | the study | is  | the PagkataoKo |     |
| --- | --- | --- | --- | --- | ----------- | ---- | --- | --------- | --- | -------------- | --- |
aswell.
|     |     |     |     |     | dataset  | curated   | by Tighe | et      | al. (2022). |     | Collected |
| --- | --- | --- | --- | --- | -------- | --------- | -------- | ------- | ----------- | --- | --------- |
|     |     |     |     |     | starting | the first | week     | of June | 2019        | up  | until the |
2 Methodology
secondweekofFebruary2020,thestudywasable
Thissectionprovidesastep-by-stepbreakdownof togatheratotalof3,128recordsandcontainsinfor-
theindividualprocessesundertakentoachievethe mationaboutFilipinoX(formerlyTwitter)and/or
objectives of this study. As seen in Figure 1 that Instagramuserssuchasdemographicdata,account
showstheoverallresearchpipeline,usingtheorig- metadata,postdata,andpersonalitydata.
inalPagkataoKodataset,asmallersubsetofdata The primary information utilized from the
wasderivedbyfilteringbasedonasetofdefined datasetincludestheX(formerlyTwitter)postdata
qualificationcriteria. Then,preprocessingandfea- such as the actual post text and the data contain-
tureextractionweredoneonthedataofeachuser ingBFIresponsesandoverallscoreperdimension
fromtheirX(formerlyTwitter)posts. After,feature whichareneededforgroundtruthcomparisonsand
| reductionwasperformedtofurthertrimdownthe |     |     |     |     | evaluation. |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
numberoffeatures. Machinelearningmodelswere Toalignwiththescopeofthestudy,thedatawas

| filteredaccordingtosetqualificationcriteria. |         |               |       | First,        | 6. Lowercasing |     |     |     |     |     |     |
| -------------------------------------------- | ------- | ------------- | ----- | ------------- | -------------- | --- | --- | --- | --- | --- | --- |
| the users                                    | must be | of Philippine | legal | age; that is, |                |     |     |     |     |     |     |
ForN-Grams,thestudyutilizedNLTK’snltk.lm
| theymustbeatleast18yearsold. |     |     | Second,asthe |     |         |            |         |     |              |     |         |
| ---------------------------- | --- | --- | ------------ | --- | ------- | ---------- | ------- | --- | ------------ | --- | ------- |
|                              |     |     |              |     | package | to extract | n-grams |     | of different |     | lengths |
studyisfocusedontext-baseddata,theusersmust
|     |     |     |     |     | needed(Birdetal.,2009). |     |     | Itshouldbenotedthat |     |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------- | --- | --- | --- |
haveX(formerlyTwitter)withatleast50posted
onlyunigramandbigramfeaturesweretested.
tweets.
A simple demographic and summary statistic 2.3 FormulatingUserDocuments
| analysis was | conducted | on              | the original | curated  |               |     |                  |     |      |             |     |
| ------------ | --------- | --------------- | ------------ | -------- | ------------- | --- | ---------------- | --- | ---- | ----------- | --- |
|              |           |                 |              |          | Concurrently, |     | while performing |     | text | preprocess- |     |
| dataset as   | well      | as the filtered | qualifying   | dataset. |               |     |                  |     |      |             |     |
ing,userdocumentswereconstructedwhereinall
ThesestatisticsarereportedonTable1..
tweetsofauserwerecombinedintoonedocument
|     |     |     |     |     | foranalysis. | Todothis,thestudyutilizedthetech- |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --------------------------------- | --- | --- | --- | --- | --- |
Demographics UniversalSet TwitterSubset QualifiedSubset niqueofconcatenationofstringsineachtweetofa
| Count |     | 3,128 | 2,283 | 2,168 |     |     |     |     |     |     |     |
| ----- | --- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
particularuserwhichthenformstheuserdocument.
Age
Toimplementthis,tokenizationwasfirstperformed
| Mean |     | 21.2 | 21.0 | 21.0 |     |     |     |     |     |     |     |
| ---- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
onthetextatthetweetlevel,followedbyapplying
| SD       |     | 3.9   | 3.9   | 3.6   |                                           |     |     |     |     |     |     |
| -------- | --- | ----- | ----- | ----- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
| AgeRange |     |       |       |       | n-gramstothetokensofeachtweet,outputtinga |     |     |     |     |     |     |
| 18-20    |     | 53.9% | 55.9% | 56.0% |                                           |     |     |     |     |     |     |
21-23 29.3% 29.0% 29.2% group of tokens per tweet. From there, we con-
| 24-26 |     | 9.3% | 8.5% | 8.5% |     |     |     |     |     |     |     |
| ----- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
catenatethearraysoftokenstogether,formulating
| ≥27 |     | 7.5% | 6.6% | 6.3% |     |     |     |     |     |     |     |
| --- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
auserdocumentforaparticularuserwherethese
Sex
tokensaretreatedasterms.
| Male   |     | 21.0% | 22.0% | 21.5% |     |     |     |     |     |     |     |
| ------ | --- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
| Female |     | 76.1% | 75.0% | 75.5% |     |     |     |     |     |     |     |
2.4 FeatureExtraction
| Intersex |     | 0.5% | 0.6% | 0.6% |     |     |     |     |     |     |     |
| -------- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
Declined1
|     |     | 2.4% | 2.5% | 2.4% |         |            |     |           |     |        |         |
| --- | --- | ---- | ---- | ---- | ------- | ---------- | --- | --------- | --- | ------ | ------- |
|     |     |      |      |      | Feature | extraction | was | performed |     | on the | prepro- |
Nationality
Filipino 99.2% 99.1% 99.2% cessed text data to extract the necessary informa-
Mixed2 0.8% 0.9% 0.8% tionfromthetext. ThestudyutilizedTF-IDFand
1Declinedtodisclosetheirsex TermOccurrenceastheextractionmethods. Due
2Filipinoswithoneormoreothernationalities
tothePagkataoKodatasetcontainingmultiplelan-
|     |     |     |     |     | guages | (i.e., English |     | and Filipino), |     | both | TF-IDF |
| --- | --- | --- | --- | --- | ------ | -------------- | --- | -------------- | --- | ---- | ------ |
Table1: Demographicstatisticsacrosstheuniversalset
ofallparticipants(U),thesubsetofparticipantswith andTermOccurrenceareamongthemoreviable
Twitteraccounts(T),andthesubsetofparticipantswith methodsasthesecanhandlemultilingualtextand
Twitteraccountsthatsatisfiedthequalificationcriteria
terms. TherearetwoparametersinthetfidfVector-
| (QT) |     |     |     |     | izerthatwereincludedasexperimentparameters, |        |     |         |      |        |     |
| ---- | --- | --- | --- | --- | ------------------------------------------- | ------ | --- | ------- | ---- | ------ | --- |
|      |     |     |     |     | which are                                   | min_df | and | max_df. | Both | min_df | and |
max_df aredocumentfrequencyfiltersthatremove
2.2 TextPreprocessing
featuresdependingonthepercentageofdocuments
| Preprocessingwasfirstperformedonthetextcor- |       |                 |              |     | theyarefoundin. |     |     |     |     |     |     |
| ------------------------------------------- | ----- | --------------- | ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- |
| pus. The                                    | study | mainly utilized | tokenization | and |                 |     |     |     |     |     |     |
2.5 FeatureReduction
| N-Grams. | Fortokenization,Marges’s(2019)Pinoy |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TweetTokenizerwillbeused,whichisamodified In order to retain only the most relevant features
| TweetTokenizerfortheFilipinolanguage. |     |     |     | Thetok- |     |     |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
asinputformodelbuilding,featurereductiontech-
enizerfeaturesareasfollows: niqueswereemployedonthetrainingset. Notethat
|     |     |     |     |     | this was | also treated | as  | an experiment |     | parameter, |     |
| --- | --- | --- | --- | --- | -------- | ------------ | --- | ------------- | --- | ---------- | --- |
1. Replacingusernameswithaplaceholder(i.e.
testingbetweentheuseofthechi-squaretestand
| USERNAME); |     |     |     |     | principalcomponentanalysis(PCA).Usingthechi- |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
square(X²)test,weonlyretainedthefeaturesthat
2. Hashtagtokenization;
fallwithinthetop20%ofresultsandthesefeatures
|     |     |     |     |     | were selected |     | for training |     | the machine | learning |     |
| --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ----------- | -------- | --- |
3. Limitingrepeatingsyllables;
models.
4. Emoticontokenization;
2.6 ModelBuilding
5. Replacing URLs with a placeholder (i.e. The study made use of the following supervised
| URL);and |     |     |     |     | machinelearningmodelsthatfocusedonsolving |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |

a classification problem centered around the pre- Algorithm 1 Aggregating Item-Level Model Re-
| dictionofBFIitemresponsesbasedontheirsocial |     |     |     |     |     |     | sults   |                                       |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------------- | --- | --- | --- |
| mediadata:                                  |     |     |     |     |     |     | Input:  | Predicteditemresponsesforagivenuser   |     |     |     |
|                                             |     |     |     |     |     |     | Output: | Listofestimatedpersonalitytraitscores |     |     |     |
• LogisticRegression
initializeemptytraitscorelist
| • Support | Vector | Machine |     | with | a Non-Linear |     |     |     |     |     |     |
| --------- | ------ | ------- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
foreachpersonalitytraitdo
Kernel
sum=0
| • XGBoost |     |     |     |     |     |     | foreachquestionitemundercurrenttraitdo |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- |
ifquestionitemisreversedthen
| These three | models | were | chosen |     | because | in the |     |     |                      |     |     |
| ----------- | ------ | ---- | ------ | --- | ------- | ------ | --- | --- | -------------------- | --- | --- |
|             |        |      |        |     |         |        |     | sum | += REVERSE(predicted |     | re- |
contextofthestudy,theymayperformbestgiven
sponse)
theamountofdataavailable.
else
Itisworthnotingthatsincethestudyfocuseson
sum+=predictedresponse
predictingresponsestoBFIquestions,individual
endif
modelswerecreatedforeachofthe17BFIitems
endfor
| undereitherExtraversionorConscientiousness. |     |     |     |     |     | In  |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
traitscore=sum/numberofquestionsunder
additiontotheapproachofdirectlyclassifyingthe
currenttrait
specificLikertscale-typeresponsesforeachitem,
appendcurrenttraitscoretotraitscorelist
| the study | also experiments |     | with | a   | two-phase, | hi- |     |     |     |     |     |
| --------- | ---------------- | --- | ---- | --- | ---------- | --- | --- | --- | --- | --- | --- |
endfor
| erarchical | classification |     | scheme. | This | alternative |     |     |     |     |     |     |
| ---------- | -------------- | --- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- |
returntraitscorelist
methodinvolvestraininginitialmodelsthatbroadly
| classify | users’ responses |     | into | one | of three | cate- |     |     |     |     |     |
| -------- | ---------------- | --- | ---- | --- | -------- | ----- | --- | --- | --- | --- | --- |
gories: (a) 1-2, (b) 3, or (c) 4-5. Then, for the describedabovetocorrespondtoeachoftheitems
secondphase,asetofbinarymodelsistrainedfor
intheBigFiveInventorythatcorrespondtoeither
| each item | to further | distinguish |     | users’ | responses |     |     |     |     |     |     |
| --------- | ---------- | ----------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- |
ExtraversionorConscientiousness.
within each category, thus obtaining the specific Furthermore,itshouldalsobenotedthatatrain-
itemresponses.
validation-testsplitwasappliedonthedataset,with
|     |     |     |     |     |     |     | a split ratio | of 70%, | 15%, and 15%, | respectively. |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ------------- | ------------- | --- |
2.7 AggregatingItem-LevelModelResults
|     |     |     |     |     |     |     | This was | implemented | by utilizing | scikit-learn’s |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------------ | -------------- | --- |
Oncetheindividualitem-levelmodelswereusedto
|     |     |     |     |     |     |     | train_test_split | function | to ensure | objective | and |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | --------- | --------- | --- |
predicttheresponsesofagivenuser,theseresults
black-boxedsplitting.
werethenbeaggregatedtoestimatetheirrawper-
sonalitytraitscores. Thismaybeaccomplishedby 3.2 Item-LevelEvaluation
followingthepseudocodedepictedinAlgorithm1,
Thisphaseoftheexperimentscentersonbuilding
whichispatternedaftertheactualscoringmetric
modelsforthe8itemsunderExtraversionandthe
oftheBFI.Thealgorithmshowshowtocalculate
9itemsunderConscientiousness.
| each trait | score | by obtaining |     | the | average | of the |     |     |     |     |     |
| ---------- | ----- | ------------ | --- | --- | ------- | ------ | --- | --- | --- | --- | --- |
Experimentparameterscameintheformofmul-
predictedresponsesforallquestionitemsthatfall
tiplecombinationsoffeatureextractionandreduc-
| underaparticularpersonalitytrait. |     |     |     |     | Indoingso,it |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
tiontechniquesaswellasmachinelearningalgo-
shouldalsobekeptinmindthatquestionstagged
rithmsandconfigurations,allutilizedtoderivethe
asreversedshouldhavetheirresponsesconverted
|     |     |     |     |     |     |     | bestperformingmodelforeachitem. |     |     | Takinginto |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | ---------- | --- |
accordingly.
accountalloftheexperimentparametersexceptfor
3 ExperimentSetupandEvaluation the two-phase hierarchical classification scheme,
|     |     |     |     |     |     |     | there are | a total of | 96 configurations | generated |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | ----------------- | --------- | --- |
3.1 ExperimentSetup
|     |     |     |     |     |     |     | for each | item (2 feature | extraction | methods | × 2 |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ---------- | ------- | --- |
This study experimented with multiple combina- feature reduction methods × 3 machine learning
tionsoffeatureextraction,featurereduction,and algorithms×2min_dfvalues×4max_dfvalues).
machine-learningtechniquestoidentifytheconfig- Additionally, the set of 96 experiment configura-
urationsthatyieldthemostoptimalresults. tionsisconductedusingthetwo-phasehierarchical
Atotalof17item-levelmodelswerecreatedfor classificationapproach,resultinginafinaltotalof
eachconfigurationorcombinationoftechniquesas 192modelsperquestionnaireitem(96modelsus-

ingdirectapproach+96modelsusingtwo-phase on the raw personality trait scores of each user,
hierarchicalclassificationapproach). ratherthanontheindividualitemresponsesasin
| Following |     | model | training | and | hyperparameter |     | theproposedapproach. |     |     |     |     |     |     |
| --------- | --- | ----- | -------- | --- | -------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
tuning,theprimarymetricthatwasusedtodeter-
|          |      |       |               |     |          |      | 4 Results |     |     |     |     |     |     |
| -------- | ---- | ----- | ------------- | --- | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- |
| mine the | best | model | configuration |     | for each | item |           |     |     |     |     |     |     |
wasthevalidationF1score,asthistakesintocon-
|     |     |     |     |     |     |     | 4.1 EvaluationofInitialProposedApproach |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
siderationtheclassimbalancepresentinthesource
|                                       |     |     |     |     |           |     | 4.1.1 | Item-LevelEvaluationResults |     |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --------- | --- | ----- | --------------------------- | --- | --- | --- | --- | --- |
| dataset’sdistributionofitemresponses. |     |     |     |     | Inthecase |     |       |                             |     |     |     |     |     |
ofthemodelscreatedfollowingthetwo-phasehier- Out of all the item-level models constructed and
testedduringexperimentation,onlytheconfigura-
archicalclassificationapproach,thevalidationF1
|          |             |     |       |                |        |     | tions that | achieved | the | best validation |     | results | for |
| -------- | ----------- | --- | ----- | -------------- | ------ | --- | ---------- | -------- | --- | --------------- | --- | ------- | --- |
| score of | the initial |     | broad | classification | models | is  |            |          |     |                 |     |         |     |
themetricusedasthebasisfordeterminingthebest eachindividualquestionnaireitemarereported.
configurations. Thesebestmodelsthenmakethe Table 2 and Table 3 provide overviews of the
best-performingmodelsforeachExtraversionitem
finalpredictionsofthetestusers’answers,which
|     |     |     |     |     |     |     | andeachConscientiousnessitem,respectively. |     |     |     |     |     | The |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
arethencomparedtotheirground-truthresponses
foreachitem. results of these item models are also juxtaposed
|          |        |     |      |             |       |     | with the | results | of baseline | majority |     | class | classi- |
| -------- | ------ | --- | ---- | ----------- | ----- | --- | -------- | ------- | ----------- | -------- | --- | ----- | ------- |
| Baseline | models |     | were | implemented | using | ma- |          |         |             |          |     |       |         |
fiers,asillustratedinFigure2andFigure3.
jorityclassclassifierstoserveasbenchmarksfor
comparingtheproposedbestitemmodels. These AcrossalloftheExtraversionandConscientious-
classifiersweretrainedusingtheresponsesforeach nessitemmodels,thereappearstobeafairamount
ofvarianceintheoptimalconfigurationsidentified
| item, identifying |     | the | majority | class | as a constant |     |            |        |     |            |          |     |        |
| ----------------- | --- | --- | -------- | ----- | ------------- | --- | ---------- | ------ | --- | ---------- | -------- | --- | ------ |
|                   |     |     |          |       |               |     | for almost | all of | the | parameters | included |     | in the |
predictor.
|     |     |     |     |     |     |     | experiment. | Theoneexception,itseems,isthefea- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------------------------- | --- | --- | --- | --- | --- |
3.3 Trait-LevelEvaluation turetypefortheExtraversionitemmodels,asmost
seemtofavortheuseofTermOccurrence,possibly
| This second | phase |     | of the | experiment | focused | on  |     |     |     |     |     |     |     |
| ----------- | ----- | --- | ------ | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
acquiringthepredicteditemresponsesforeachtrait duetoitspotentialtoaidinmodelgeneralization.
fromthebestitemmodelsinthepreviousphaseand AsseeninTable2,theoveralltestF1scoresof
thebestitemmodelsforExtraversionfallbetween
computingfortheusers’trait-levelscoresusingthe
designatedformulaoftheBFI. 0.3000to0.5000,withItem31Rachievingthehigh-
Once the personality trait results were aggre- esttestF1scoreat0.4334. Conversely,theweakest
performingmodelbelongstoItem36,whichhasa
| gated for | each  | user         | in the | test  | set and compared   |     |                                   |     |     |     |     |           |     |
| --------- | ----- | ------------ | ------ | ----- | ------------------ | --- | --------------------------------- | --- | --- | --- | --- | --------- | --- |
|           |       |              |        |       |                    |     | testF1scoreofapproximately0.3196. |     |     |     |     | Acompari- |     |
| against   | their | ground-truth |        | trait | scores, evaluation |     |                                   |     |     |     |     |           |     |
wasperformedwiththeuseofrootmeansquared sonoftheseF1scoreswiththoseobtainedonthe
error(RMSE)andR2 score. train-validation set suggests a possibility that the
modelsoverfittedonthetrainingdata.
Similartothepreviousphase,baselinemodels
wereemployedtohaveafurthercomparisonand
Item-LevelResultsforExtraversion
performanceevaluationoftheproposedapproach.
|     |     |     |     |     |     |     | Item | Min_df Max_df | Feature | Algorithm | Feature | Train- | TestF1 |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------- | ------- | --------- | ------- | ------ | ------ |
|     |     |     |     |     |     |     |      |               | Reduc-  |           |         | ValF1  |        |
Thesebaselinesincludedameanregressor,asim-
tion
|     |     |     |     |     |     |     | Item1 | 0.1 | 0.9 PCA | LR  | TO  | 1.0000 | 0.3450 |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- | --- | ------ | ------ |
plelinearregressionmodel,andamulti-layerper-
|     |     |     |     |     |     |     | Item6R | 0.05 | 0.7 CHI | XGB | TF-IDF | 1.0000 | 0.3740 |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---- | ------- | --- | ------ | ------ | ------ |
ceptron(MLP)regressor. Item11 0.05 0.9 CHI LR TO 1.0000 0.3311
|                                       |      |           |     |         |           |     | Item16  | 0.1  | 0.7 CHI | LR  | TF-IDF | 1.0000 | 0.3586 |
| ------------------------------------- | ---- | --------- | --- | ------- | --------- | --- | ------- | ---- | ------- | --- | ------ | ------ | ------ |
| The                                   | mean | regressor | was | trained | using the | raw |         |      |         |     |        |        |        |
|                                       |      |           |     |         |           |     | Item21R | 0.05 | 0.6 PCA | LR  | TO     | 1.0000 | 0.3386 |
|                                       |      |           |     |         |           |     | Item26  | 0.1  | 0.6 CHI | XGB | TO     | 1.0000 | 0.3785 |
| personalitytraitscoresfromthedataset, |      |           |     |         | withthe   |     |         |      |         |     |        |        |        |
|                                       |      |           |     |         |           |     | Item31R | 0.05 | 0.8 CHI | SVM | TO     | 0.9875 | 0.4334 |
average score for each trait serving as a constant Item36 0.1 0.9 PCA SVM TO 0.9962 0.3196
| predictor. | Meanwhile, |     | the | pipeline | for both | the |         |                                          |     |     |     |     |     |
| ---------- | ---------- | --- | --- | -------- | -------- | --- | ------- | ---------------------------------------- | --- | --- | --- | --- | --- |
|            |            |     |     |          |          |     | Table2: | Theperformanceandconfigurationsofthebest |     |     |     |     |     |
mean regressor and the MLP regressor follows a performingclassificationmodelsperExtraversionitem.
processsimilartotheproposedapproachupuntil ModelswereselectedbasedonvalidationF1score.
| the feature | reduction |     | stage. | However, | instead | of  |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
proceedingtoitem-specificmodel-buildingandag- Compared to the results produced by the Ex-
gregation, the pipeline for these baseline models traversionitemmodels,therangeofvaluesforthe
directlytransitionstotrait-specificmodelbuilding testF1scoresofthebestperformingConscientious-
and trait-level evaluation. This divergence stems nessitemmodelsisgenerallybroader,bothonthe
fromtheirtrait-basedapproachoftrainingdirectly lowerandhigherendsofthescale. Table3reveals

thatthebestperformingitemmodelforConscien-
tiousnessproducedatestF1scoreof0.5416,while
theworstperformingmodelhadatestF1scoreof
0.2426.
Item-LevelResultsforConscientiousness
| Item | Min_df | Max_df Feature | Algorithm | Feature | Train- TestF1 |     |     |     |     |     |     |     |
| ---- | ------ | -------------- | --------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
|      |        | Reduc-         |           | ValF1   |               |     |     |     |     |     |     |     |
tion
| Item3   | 0.05 | 0.9 CHI | XGB | TO 0.7207     | 0.4574 |     |     |     |     |     |     |     |
| ------- | ---- | ------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Item8R  | 0.05 | 0.9 CHI | XGB | TO 0.9902     | 0.5416 |     |     |     |     |     |     |     |
| Item13  | 0.1  | 0.6 CHI | XGB | TF-IDF 0.2761 | 0.2426 |     |     |     |     |     |     |     |
| Item18R | 0.1  | 0.6 PCA | SVM | TO 0.8959     | 0.2534 |     |     |     |     |     |     |     |
Item23R
|        | 0.1  | 0.6 PCA | LR  | TO 1.0000     | 0.4373 |     |     |     |     |     |     |     |
| ------ | ---- | ------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| Item28 | 0.05 | 0.7 PCA | LR  | TF-IDF 0.9680 | 0.4152 |     |     |     |     |     |     |     |
Item33 0.1 0.7 CHI LR TF-IDF 1.0000 0.3534 Figure3: AcomparisonoftestF1scoresbetweenbase-
| Item38 | 0.05 | 0.6 PCA | LR  | TF-IDF 1.0000 | 0.2750 |     |     |     |     |     |     |     |
| ------ | ---- | ------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
linemajorityclassclassifiersandthebestitemmodels
| Item43R | 0.1 | 0.9 PCA | XGB | TF-IDF 1.0000 | 0.3921 |     |     |     |     |     |     |     |
| ------- | --- | ------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
forConscientiousness
Table3: Theperformanceandconfigurationsofthebest
performingclassificationmodelsperConscientiousness
| item. | Models | were selected | based | on validation | F1  |            |          |            |     |        |     |          |
| ----- | ------ | ------------- | ----- | ------------- | --- | ---------- | -------- | ---------- | --- | ------ | --- | -------- |
|       |        |               |       |               |     | regressor, | a linear | regression |     | model, | and | a multi- |
score.
layerperceptronregressor.
FortheExtraversiontrait,Table4showsthatthe
Asevidencedbytheside-by-sidecomparisonsof
proposedapproachproducedthebestresults,with
thetestF1scoresfortheitemmodelsofbothtraits
thelowesttestRMSEofapproximately0.6714,and
againstthebaselinemajorityclassifiersinFigure
|     |     |     |     |     |     | the highest | R2  | score | of around | 0.1240. |     | However, |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --------- | ------- | --- | -------- |
2andFigure3,itbecomesapparentthatallofthe
whentakingthesevaluesontheirown,theR2value
proposeditemmodelsconsistentlyunderperform.
|      |           |                   |     |             |     | canbeconsideredrelativelylow. |     |     |     | Thismaysuggest |     |     |
| ---- | --------- | ----------------- | --- | ----------- | --- | ----------------------------- | --- | --- | --- | -------------- | --- | --- |
| This | disparity | in classification |     | performance | may |                               |     |     |     |                |     |     |
potentiallybecausedinpartbythedisproportionate thatthevarianceintheExtraversiontraitscoresis
stillnotexplainedverywellbythepredictorusing
numberofsamplesforthemajorityclasslabelof
thegivenfeatures.
| eachquestionnaireitem. |     |     | Thedegreetowhichthis |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classimbalanceexistscanbeseenfromhowmost
of the majority class classifiers exhibited test F1 Trait-LevelResultsforExtraversion
|                 |     |     |     |     |     | Model            |                                           | Train-ValRMSE |     | Train-ValR2 | TestRMSE | TestR2  |
| --------------- | --- | --- | --- | --- | --- | ---------------- | ----------------------------------------- | ------------- | --- | ----------- | -------- | ------- |
| scoresabove0.5. |     |     |     |     |     | MeanRegressor    |                                           | 0.7499        |     | 0.0000      | 0.7175   | -0.0003 |
|                 |     |     |     |     |     | LinearRegression |                                           | 0.2650        |     | 0.8751      | 0.6747   | 0.1154  |
|                 |     |     |     |     |     | MLPRegressor     |                                           | 0.7500        |     | -0.0004     | 0.7174   | 0.0000  |
|                 |     |     |     |     |     | ProposedApproach |                                           | 0.0382        |     | 0.9974      | 0.6714   | 0.1240  |
|                 |     |     |     |     |     | Table4:          | Thetrait-levelresultsforExtraversionusing |               |     |             |          |         |
theproposedapproachaswellasbaselinemodels
ComparedtoExtraversion,theresultsproduced
byallofthemodelsfortheConscientiousnesstrait
|     |     |     |     |     |     | are considerably |     | worse. |      | The proposed |     | approach |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ---- | ------------ | --- | -------- |
|     |     |     |     |     |     | performs         | the | worst  | with | a test RMSE  | of  | 0.6760   |
andatestR2
valueof-0.2273,whilethelinearre-
gressionmodelperformsthebestwithatestRMSE
Figure2: AcomparisonoftestF1scoresbetweenbase- of0.6010andatestR2 valueof0.0298. Thesere-
linemajorityclassclassifiersandthebestitemmodels
sultsshowthattheinitialitem-basedapproachfor
forExtraversion
Conscientiousnessleavesmuchtobeimproved,as
directtraitmodelingstillworksbetterinpredicting
| 4.1.2 | Trait-LevelEvaluationResults |     |     |     |     | overalltraitscores. |     |     |     |     |     |     |
| ----- | ---------------------------- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
Table 4 and Table 5 present the trait-level results Interestingly,despitegenerallyhavingbettertest
comparingtheaggregatedpredictionsagainstthe RMSE scores, the Conscientiousness models ap-
peartohavepoorertestR2
ground-truthpersonalitytraitscoresforExtraver- scoresacrosstheboard,
sionandConscientiousness,respectively. There- whichmaysuggestthatwiththegivenfeatureset,
sultsoftheproposedapproacharealsocompared Conscientiousnesstraitscoresaremorechalleng-
tothatof3differentbaselines,particularly,amean ingtopredictcomparedtoExtraversion.

Trait-LevelResultsforConscientiousness
|                  |       |               |        |             |          |         | curacy                             | in  | the first | layer of classes, | specifically |             | in  |
| ---------------- | ----- | ------------- | ------ | ----------- | -------- | ------- | ---------------------------------- | --- | --------- | ----------------- | ------------ | ----------- | --- |
|                  | Model | Train-ValRMSE |        | Train-ValR2 | TestRMSE | TestR2  |                                    |     |           |                   |              |             |     |
|                  |       |               |        |             |          |         | Classes1-2,3,and4-5,respectively.  |     |           |                   |              | Theseafore- |     |
| MeanRegressor    |       |               | 0.6108 | 0.0000      | 0.6105   | -0.0010 |                                    |     |           |                   |              |             |     |
| LinearRegression |       |               | 0.2499 | 0.8326      | 0.6010   | 0.0298  |                                    |     |           |                   |              |             |     |
|                  |       |               |        |             |          |         | mentioned                          |     | scores    | for both traits   | show         | generally   |     |
| MLPRegressor     |       |               | 0.6144 | -0.0120     | 0.6162   | -0.0199 |                                    |     |           |                   |              |             |     |
| ProposedApproach |       |               | 0.2033 | 0.8892      | 0.6760   | -0.2273 |                                    |     |           |                   |              |             |     |
|                  |       |               |        |             |          |         | highervalues,meaningthatonthebroad |     |           |                   |              | levelof     |     |
classification,themodelsareabletoclassifymore
| Table | 5: The | trait-level |     | results for | Conscientiousness |     |     |     |     |     |     |     |     |
| ----- | ------ | ----------- | --- | ----------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- |
usingtheproposedapproachaswellasbaselinemodels accuratelycomparedtopreviousscores.
ThevalidationF1scoreslabeledspecific,onthe
|     |     |     |     |     |     |     | otherhand,arenotashighasthebroad |     |     |     |     | F1scores. |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --------- | --- |
4.2 EvaluationofProposedApproachwith
ThespecificF1scorespertainstotheaccuracyof
HierarchicalClassification
classifyingthedatatotheactualresponsepredic-
| Another |     | experiment | was | done | with the | proposed |                  |     |                  |     |     |     |     |
| ------- | --- | ---------- | --- | ---- | -------- | -------- | ---------------- | --- | ---------------- | --- | --- | --- | --- |
|         |     |            |     |      |          |          | tionclasses(i.e. |     | Class1,2,3,4,5). |     |     |     |     |
approach,particularlytheintegrationofahierarchi-
|     |     |     |     |     |     |     | The | validation | F1  | scores labeled |     | Binary | repre- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | ------ | ------ |
calclassificationscheme. Asmentionedpreviously, sent the accuracy of predicting the right binary
hierarchicalclassificationattemptstoclassifythe class after the first classification layer has been
| dataintobroaderclasses(e.g. |     |     |     | Class1-2,Class4-5) |     |     |      |       |        |             |     |           |     |
| --------------------------- | --- | --- | --- | ------------------ | --- | --- | ---- | ----- | ------ | ----------- | --- | --------- | --- |
|                             |     |     |     |                    |     |     | done | (i.e. | Binary | 1 - Class 1 | and | 2, Binary | 2 - |
onthefirstclassificationlayer,thenclassifiesthe Class 3, Binary 3 - Class 4 and 5). Although the
datainamorespecificclass(e.g. Class1,Class2) F1scoresforeachBinaryaregenerallyhigh,this
| onthesecondlayer. |     |     | Thisexperimentwasdoneto |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
onlydealswithclassifyingthedataintooneortwo
attempttoclassifydatapointsbetterbygrouping
classes.
classesthatwereclosertoeachotherfirstandthen
Trait-LevelResultsforExtraversion
differentiatingthemlateron.
|     |     |     |     |     |     |     |     | Version |     | TestRMSE |     | TestR² |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | --- | ------ | --- |
Extraversion
|               |         |        |        |             |             |        |     | Original       |     | 0.6714 |     | 0.1240 |     |
| ------------- | ------- | ------ | ------ | ----------- | ----------- | ------ | --- | -------------- | --- | ------ | --- | ------ | --- |
| Train-ValRMSE |         |        | 0.2097 | TestRMSE    |             | 0.7126 |     |                |     |        |     |        |     |
| Train-ValR²   |         |        | 0.9218 | TestR²      |             | 0.0131 |     | Hierarchical   |     | 0.7126 |     | 0.0131 |     |
| Item          | ValF1   | ValF1  | ValF1  | ValF1 ValF1 | Train-ValF1 | TestF1 |     |                |     |        |     |        |     |
|               | (Broad) | (Spe-  | (Bi-   | (Bi- (Bi-   |             |        |     | Classification |     |        |     |        |     |
|               |         | cific) | nary   | nary nary   |             |        |     |                |     |        |     |        |     |
|               |         |        | 1)     | 2)          | 3)          |        |     |                |     |        |     |        |     |
Item1 0.5685 0.3502 0.6520 1.0000 0.5399 0.9519 0.3892 Table8: ExtraversionTrait-LevelResultsforOriginal
| Item6R | 0.5359 | 0.3990 | 0.7825 | 1.0000 0.6313 | 0.9822 | 0.3138 |     |     |     |     |     |     |     |
| ------ | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
andHierarchicalExperiments
| Item11  | 0.5220 | 0.3431 | 0.6040 | 1.0000 0.5613 | 1.0000 | 0.3905 |     |     |     |     |     |     |     |
| ------- | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| Item16  | 0.5560 | 0.3350 | 0.7307 | 1.0000 0.5815 | 0.7085 | 0.3205 |     |     |     |     |     |     |     |
| Item21R | 0.5567 | 0.3643 | 0.7508 | 1.0000 0.5445 | 0.7209 | 0.2999 |     |     |     |     |     |     |     |
| Item26  | 0.4956 | 0.3913 | 0.6427 | 1.0000 0.7402 | 1.0000 | 0.3230 |     |     |     |     |     |     |     |
| Item31R | 0.6579 | 0.4650 | 0.6269 | 1.0000 0.5986 | 0.9412 | 0.4284 |     |     |     |     |     |     |     |
Trait-LevelResultsforConscientiousness
| Item36 | 0.5317 | 0.3236 | 0.5018 | 1.0000 0.5692 | 0.6096 | 0.2848 |     |         |     |          |     |        |     |
| ------ | ------ | ------ | ------ | ------------- | ------ | ------ | --- | ------- | --- | -------- | --- | ------ | --- |
|        |        |        |        |               |        |        |     | Version |     | TestRMSE |     | TestR² |     |
Table6: ExtraversionResultswithHierarchicalClassi-
|     |     |     |     |     |     |     |     | Original |     | 0.6760 |     | -0.2273 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------ | --- | ------- | --- |
fication
|     |     |     |     |     |     |     |     | Hierarchical |     | 0.6270 |     | -0.0560 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | --- | ------- | --- |
Classification
Conscientiousness
Train-ValRMSE 0.2015 TestRMSE 0.6270 Table9:ConscientiousnessTrait-LevelResultsforOrig-
| Train-ValR² |     |     | 0.8911 | TestR² |     | -0.0560 |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------ | ------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
inalandHierarchicalExperiments
| Item  | ValF1   | ValF1  | ValF1  | ValF1 ValF1   | Train-ValF1 | TestF1 |          |     |           |             |       |     |       |
| ----- | ------- | ------ | ------ | ------------- | ----------- | ------ | -------- | --- | --------- | ----------- | ----- | --- | ----- |
|       | (Broad) | (Spe-  | (Bi-   | (Bi- (Bi-     |             |        |          |     |           |             |       |     |       |
|       |         | cific) | nary   | nary nary     |             |        |          |     |           |             |       |     |       |
|       |         |        | 1)     | 2)            | 3)          |        |          |     |           |             |       |     |       |
|       |         |        |        |               |             |        | Overall, |     | observing | the results | found | in  | Table |
| Item3 | 0.6373  | 0.6281 | 0.8617 | 1.0000 0.5824 | 0.8263      | 0.5742 |          |     |           |             |       |     |       |
Item8R 0.6366 0.5419 0.5513 1.0000 0.6123 0.8297 0.5078 7,thevalidationscoreslooksomewhatpromising,
| Item13 | 0.7167 | 0.4909 | 0.8526 | 1.0000 0.5480 | 1.0000 | 0.4366 |     |     |     |     |     |     |     |
| ------ | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Item18R 0.5135 0.4036 0.4775 1.0000 0.5090 0.9859 0.3380 withpredictionsthatlookmoreaccurateafterpass-
| Item23R | 0.7327 | 0.4451 | 0.7957 | 1.0000 0.5514 | 0.9712 | 0.4388 |     |     |     |     |     |     |     |
| ------- | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Item28 0.6344 0.5052 1.0000 1.0000 0.5099 0.8611 0.4555 ingthroughtwolayersasopposedtotheoriginal
Item33 0.5780 0.4435 0.9033 1.0000 0.6314 0.9925 0.3608 proposed approach for Conscientiousness. It can
| Item38 | 0.5016 | 0.4434 | 0.7528 | 1.0000 0.6323 | 0.6317 | 0.3406 |     |     |     |     |     |     |     |
| ------ | ------ | ------ | ------ | ------------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Item43R 0.6583 0.4156 0.7148 1.0000 0.5480 0.7604 0.5399 be observed that the approach with hierarchical
Table7: ConscientiousnessResultswithHierarchical classificationisapotentiallyviablemethodinclas-
| Classification |     |     |     |     |     |     | sifyingasitproducedmoreaccurateresultsatthe |     |                 |     |        |        |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --------------- | --- | ------ | ------ | --- |
|                |     |     |     |     |     |     | item-level.                                 |     | This difference | in  | metric | scores | may |
Tables6and7showtheresultsoftheitemmod- likelybeattributedtothestep-by-stepprocessof
elswithhierarchicalclassification,alongwiththe classifying the data, where data is classified in a
validationF1scoresforeachlayerforbothbroad broaderthresholdofsimilarclassesandthenfurther
andbinaryclassification. differentiatedonthesecondlevel. Bybreakingthe
Thebroad F1scoresrepresentclassificationac- modeling process into two phases, this approach

betteraccountedfortheinherentordinalityofthe Theycandelveintomoreexperimentationsthataim
dataandshowedthatthemodelsstillhadpotential todeterminehowthedataqualitativelycorrelates
fordistinguishingbetweenhighandlowresponses, to model performance, and what can be changed
which was particularly beneficial for the Consci- duringpreprocessing,extraction,andreductionin
entiousness trait. However, despite an improved orderformodelstolearnbetterfromthemandat-
item-levelperformance,thetrait-levelresultsstill tainthemostoptimalperformanceresults. Another
muchtobedesired. Thatsaid,itisstillastepinthe angleofinterestisexaminingtrait-levelresultcor-
rightdirectiontobeabletoclassifytheitem-level relations with feature tokens, as this may help in
datamoreaccuratelyatleastatthebroad level. identifyingtrendsorpatternsintermsofhoweach
|     |     |     |     |     |     | trait’s best | performing |     | approach |     | assigns | weights |     |
| --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | -------- | --- | ------- | ------- | --- |
5 Conclusion
|     |     |     |     |     |     | or significance |     | to  | certain | terms | or phrases, |     | espe- |
| --- | --- | --- | --- | --- | --- | --------------- | --- | --- | ------- | ----- | ----------- | --- | ----- |
ciallyconsideringthemixofEnglishandFilipino
Followinginitialitem-levelandtrait-levelevalua-
linguisticnuances.
| tions of | the approach, |     | it was | inferred | that due to |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ------ | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Atamoregenerallevel,futurestudiesmayoptto
dataimbalance,substantialresultsbecamehardto
|     |     |     |     |     |     | focusonawiderscope. |     |     | Recommendationsinclude |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---------------------- | --- | --- | --- | --- |
derivebecausemodelsperformedpoorlyinterms
|               |     |             |     |      |              | exploring | multimodal |     | approaches |     | that | make | use |
| ------------- | --- | ----------- | --- | ---- | ------------ | --------- | ---------- | --- | ---------- | --- | ---- | ---- | --- |
| of item-level |     | prediction, | and | were | even outper- |           |            |     |            |     |      |      |     |
ofimagesalongsidetextualdata,testingtheitem-
formedbybaselineclassifiersandregressionmod-
|     |     |     |     |     |     | based approach |     | on  | a high-resource |     |     | language | like |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --------------- | --- | --- | -------- | ---- |
els. Inhopesofaddressingthisissue,ahierarchical
|                |          |     |     |             |           | English | to more | accurately |     | assess |     | the impact | of  |
| -------------- | -------- | --- | --- | ----------- | --------- | ------- | ------- | ---------- | --- | ------ | --- | ---------- | --- |
| classification | approach |     | was | integrated, | which in- |         |         |            |     |        |     |            |     |
dataquantity,andinvestigatingmethodologieson
| volved | breaking | down | the modeling |     | process into |     |     |     |     |     |     |     |     |
| ------ | -------- | ---- | ------------ | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
howtoproperlystructuresocialmediadata.
| twophases. | Implementingthismethodshoweda |     |     |     |     |        |       |     |      |         |     |                |     |
| ---------- | ----------------------------- | --- | --- | --- | --- | ------ | ----- | --- | ---- | ------- | --- | -------------- | --- |
|            |                               |     |     |     |     | Future | works | may | also | address |     | the identified |     |
somewhatdistinctadvantage,mostnotablyforthe
|                         |     |     |                         |     |     | issues from | the     | results | of       | the          | study, | mainly   | data |
| ----------------------- | --- | --- | ----------------------- | --- | --- | ----------- | ------- | ------- | -------- | ------------ | ------ | -------- | ---- |
| Conscientiousnesstrait. |     |     | However,whilethehierar- |     |     |             |         |         |          |              |        |          |      |
|                         |     |     |                         |     |     | imbalance   | leading |         | to model | overfitting, |        | hyperpa- |      |
chicalapproachworkedrelativelybetterforCon-
rameterlimitations,anddataqualityorweightas-
| scientiousness,  |     | the original                  |     | pipeline | still reigned |                      |     |     |                         |       |     |        |     |
| ---------------- | --- | ----------------------------- | --- | -------- | ------------- | -------------------- | --- | --- | ----------------------- | ----- | --- | ------ | --- |
|                  |     |                               |     |          |               | signmentsonfeatures. |     |     | Thiscanbedonebyincreas- |       |     |        |     |
| forExtraversion. |     | Thisdifferenceinmodelinclina- |     |          |               |                      |     |     |                         |       |     |        |     |
|                  |     |                               |     |          |               | ing hyperparameter   |     |     | search                  | space | and | number | of  |
tionmaybeattributedtothedifferenceinfeature
iterationsforthemodels,aswellasattemptingto
significancebetweenthetwotraits.
experimentonlywiththeunigramdatainsteadof
| It is | also worth |     | noting that | when | compared |     |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ----------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
includingbigrams.
againstbaselinemodels,theoriginalpipelinestill
|     |     |     |     |     |     | The | potential | of  | the hierarchical |     |     | approach | can |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------------- | --- | --- | -------- | --- |
performedbestforExtraversion,whereasthebase-
alsobeexpoundedupon;withproperdatabalanc-
linesperformedbetterforConscientiousnesseven
ingmethodsandtherightsetofconfigurations,this
withtheslightimprovementprovidedbythehierar-
|                 |     |                              |     |     |     | approach | may | proveto | beintegraland |     |     | beneficial |     |
| --------------- | --- | ---------------------------- | --- | --- | --- | -------- | --- | ------- | ------------- | --- | --- | ---------- | --- |
| chicalapproach. |     | Thissupportsthedeductionthat |     |     |     |          |     |         |               |     |     |            |     |
totheoverallpipeline.
Conscientiousnessitemsresponsesmaybeharder
Otherrecommendationsincludeexploringother
topredict,particularlywiththegivendata.
featureextractionandreductiontechniques,aswell
Withtheseresults,itisevidentthatthisparticular
|     |     |     |     |     |     | as utilizing | the | remaining |     | three | traits | of the | Big |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --- | ----- | ------ | ------ | --- |
fieldofAPRstudy,especiallyinaFilipinocontext,
Five(Openness,Agreeableness,andNeuroticism)
| leaves much | room | for | pondering |     | and experimen- |     |     |     |     |     |     |     |     |
| ----------- | ---- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
todetermineiftheproposedapproachcouldwork
tation. Somemodelsindeedshowedpromise,but
|                          |           |      |                     |        |               | equally               | or better | as  | compared |     | to its   | Extraversion |     |
| ------------------------ | --------- | ---- | ------------------- | ------ | ------------- | --------------------- | --------- | --- | -------- | --- | -------- | ------------ | --- |
| even the                 | so-called | best | performing          |        | models have   |                       |           |     |          |     |          |              |     |
|                          |           |      |                     |        |               | and Conscientiousness |           |     | results. |     | Future   | works        | are |
| verylowtestmetricscores. |           |      | Theoverallresultsof |        |               |                       |           |     |          |     |          |              |     |
|                          |           |      |                     |        |               | also recommended      |           |     | to test  | the | proposed | approach     |     |
| this study               | signify   | that | more                | tuning | for both data |                       |           |     |          |     |          |              |     |
againstdiversedatasetsanddifferentsocialmedia
| and models | needs | to  | be done | for this | item-based |           |     |          |     |          |     |        |        |
| ---------- | ----- | --- | ------- | -------- | ---------- | --------- | --- | -------- | --- | -------- | --- | ------ | ------ |
|            |       |     |         |          |            | platforms | and | contexts |     | in order | to  | have a | better |
approachtomanifestimprovementsandbecomea
benchmarkforperformanceandgeneralizability.
frameworkthatcanprovebeneficialtoAPR.
6 Recommendation
Futureworksthatwillchoosetobuilduponthere-
sultsfromthisstudyareencouragedtofocusmore
| on the best | performing |     | approaches |     | for each trait. |     |     |     |     |     |     |     |     |
| ----------- | ---------- | --- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |

References
Alexander H. II Agno, Jesah R. Gano, and
ClaudeKristofferSedillo.2019. InstagramvsTwit-
ter: Analyzing the manifestation of personality
throughthewritingstyleofFilipinoSNSusers. Bach-
elor’sthesis,DeLaSalleUniversity.
AmericanPsychologicalAssociation. Personality.
Steven Bird, Edward Loper, and Ewan Klein. 2009.
NaturalLanguageProcessingwithPython.O’Reilly
MediaInc.
Ronn Christian Chua Chiaco, Howard Montecillo,
RonellJohnRoxas,andBryanEthanTio.2022. Ap-
plicationofwordembeddingsonautomaticperson-
alityrecognitionusingFilipinoTwitterdata. Bache-
lor’sthesis,DeLaSalleUniversity.
AndrewMarges.2019. pinoy_tweetokenize.
Sumiya Mushtaq and Neerendra Kumar. 2022. Text-
based automatic personality recognition: Recent
developments. In Proceedings of Third Interna-
tionalConferenceonComputing,Communications,
and Cyber-Security: IC4S 2021, pages 537–549.
Springer.
EdwardTighe,LuigiAcorda,AlexanderIiAgno,Jesah
Gano, Timothy Go, Gabriel Santiago, and Claude
Sedillo.2022. Collectionmethodsanddatacharac-
teristicsofthePagkataoKodataset. InProceedings
ofthe36thPacificAsiaConferenceonLanguage,In-
formationandComputation,pages513–524,Manila,
Philippines.AssociationforComputationalLinguis-
tics.
EdwardTighe,OyaAran,andCharibethCheng.2020.
Exploringneuralnetworkapproachesinautomatic
personalityrecognitionofFilipinoTwitterusers. In
Proceedingsofthe20thPhilippineComputingSci-
enceCongress,pages137–145.
Edward Tighe and Charibeth Cheng. 2018. Model-
ing personality traits of Filipino Twitter users. In
Proceedings of the Second Workshop on Computa-
tional Modeling of People’s Opinions, Personality,
andEmotionsinSocialMedia,pages112–122,New
Orleans,Louisiana,USA.AssociationforComputa-
tionalLinguistics.