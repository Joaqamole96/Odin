---
conversion_metadata:
  converted_at: "2026-07-21T06:07:14Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Espiritu P. et al.pdf"
  source_pdf_sha256: "80c06e6e70da94b224818d31314eaa6a1a8a17fd50eff62ddd0e82da3835a882"
  page_count: 9
  markdown_char_count: 69990
---

Balarila: Deep Learning for Semantic Grammar Error Correction in
|     |                |     |     |              | Low-Resource |             | Settings |                    |     |     |     |     |
| --- | -------------- | --- | --- | ------------ | ------------ | ----------- | -------- | ------------------ | --- | --- | --- | --- |
|     | PaoloEspiritu, |     |     | JoshueJadie, |              | AndrePonce, |          | and CharibethCheng |     |     |     |     |
CollegeofComputerStudies
DeLaSalleUniversity,Manila
{paolo_edni_v_espiritu, joshue_jadie, andre_ponce, charibeth.cheng}@dlsu.edu.ph
|     |     |     | Abstract |     |     |     | TherealreadyexistsaFilipinogrammarchecker |     |     |     |     |     |
| --- | --- | --- | -------- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
calledGramatika–whichutilizesrule-basedmeth-
Whiletherearemanygrammarcheckersavail-
odscombinedwithstatisticalmachinetranslation
ableforvariouslanguages,especiallytheEn-
|       |           |       |      |       |         |      | (SMT) | (Go et al., | 2017). | However, | it is | limited |
| ----- | --------- | ----- | ---- | ----- | ------- | ---- | ----- | ----------- | ------ | -------- | ----- | ------- |
| glish | language, | those | that | exist | for the | low- |       |             |        |          |       |         |
resourceFilipinolanguagecanonlyeffectively bytheavailabilityofexpert-annotatedcorporaand
correct lexical errors. There is yet to be a byotherlimitationsthatcomewithSMT-basedim-
publicly available Filipino grammar checker plementations(Solymanetal.,2021;Chollampatt
| that            | can also | address | semantic              |     | errors, | which |         |                     |     |     |           |     |
| --------------- | -------- | ------- | --------------------- | --- | ------- | ----- | ------- | ------------------- | --- | --- | --------- | --- |
|                 |          |         |                       |     |         |       | and Ng, | 2018). Furthermore, |     | as  | Gramatika | was |
| aremorecomplex. |          |         | Assuch,thisstudyfound |     |         |       |         |                     |     |     |           |     |
releasedin2017,thereisyettobeaFilipinogram-
| an opportunity |     | to  | introduce | Balarila, |     | a deep |     |     |     |     |     |     |
| -------------- | --- | --- | --------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- |
marcheckerthatadoptsstate-of-the-artapproaches
learning-basedFilipinoGECmodelinspiredby
suchastransformer-basedmodels.
| theGECToRapproach. |     |     | Toaddresstheabsence |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ofatrainingandtestdataset,anautomateder- Inarecentstudy,asequencetaggingapproach
rorgenerationpipelinewasdevised, creating was introduced to simplify the task of sequence
syntheticdatasetsoferror-freeanderror-filled generation. The proposed model only utilized a
Filipinosentencessourcedfromvariousonline
transformerencoderandsomebasiclinearlayers.
| news | sources. | Tagalog |     | BERT and | RoBERTa |     |     |     |     |     |     |     |
| ---- | -------- | ------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Theresultsshowedthattheinferencespeedofthe
modelswerefine-tunedintwostagesusingthis
modelimproved10timescomparedtotransformer-
| generatedcorpus. |     |     | Evaluationmetricsincluded |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
basedseq2seqsystems(Omelianchuketal.,2020).
| precision, |     | recall, | and F | scores | for | GEC, |     |     |     |     |     |     |
| ---------- | --- | ------- | ----- | ------ | --- | ---- | --- | --- | --- | --- | --- | --- |
0.5
and a multi-class confusion matrix for GED. However,thesemodelsrequirelargeamountsof
Thetop-performingmodel,RoBERTaTagalog data for training. This poses a problem for low-
Large,achievedanF scoreof70.75,while resourcelanguagessuchasFilipino. Workarounds
0.5
theRoBERTaTagalogBase,withaF 0.5 score were created to address this such as synthetic
| of 69.00, |                                 | demonstrated |     | cost-effectiveness |     | in  |             |                        |          |       |               |        |
| --------- | ------------------------------- | ------------ | --- | ------------------ | --- | --- | ----------- | ---------------------- | -------- | ----- | ------------- | ------ |
|           |                                 |              |     |                    |     |     | dataset     | creation (Grundkiewicz |          |       | et al., 2019) | and    |
| training. | Thecreateddatasetscanalsobeused |              |     |                    |     |     |             |                        |          |       |               |        |
|           |                                 |              |     |                    |     |     | large-scale | corpus                 | creation | (Cruz | and           | Cheng, |
asabenchmarkforFilipinogrammarchecker
2021).
models.
Inthispaper,anopportunityhasbeenfoundto
1 Introduction
|         |           |     |           |          |     |          | develop          | a transformer | encoder-based |         | model        | that |
| ------- | --------- | --- | --------- | -------- | --- | -------- | ---------------- | ------------- | ------------- | ------- | ------------ | ---- |
|         |           |     |           |          |     |          | will effectively | detect        | and           | correct | grammatical  |      |
| Writing | sentences | in  | a certain | language |     | requires |                  |               |               |         |              |      |
|         |           |     |           |          |     |          | errors in        | the Filipino  | language.     |         | Furthermore, | a    |
skillsthatareonlydevelopedthroughalotofprac-
|           |            |               |              |     |          |           | demonstration | of how   | a synthetic  |     | error-free  | and  |
| --------- | ---------- | ------------- | ------------ | --- | -------- | --------- | ------------- | -------- | ------------ | --- | ----------- | ---- |
| tice. A   | sufficient | understanding |              |     | of the   | rules and |               |          |              |     |             |      |
|           |            |               |              |     |          |           | error-filled  | Filipino | text dataset |     | can be used | as a |
| syntax of | a language |               | is necessary |     | to avoid | break-    |               |          |              |     |             |      |
benchmarkforgrammarerrordetectionandcorrec-
| downsincommunication. |     |     | TheFilipinolanguageis |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionisalsoprovided.
notexemptedfromsuchanecessity.
GrammarcheckerssuchasGrammarlyaresaid
2 RelatedLiterature
tobebeneficialinaidingindividualshonethediffer-
entaspectsoftheirwritingskillssuchassentence GECToR (Omelianchuk et al., 2020) is a trans-
construction, vocabulary usage, proper grammar, formerencoder-basedmodelthatapproachesGEC
and language mechanics (Ghufron and Rosyida, as an iterative sequence tagging task instead of
2018; Jayavalan and Razali, 2018). Using such sequence generation. The approach essentially
tools is one of the many ways one can develop reduces the task into a language-understanding
betterwritingskills. problem,whichonlyneedsatransformerencoder
21
ProceedingsoftheFirstWorkshopinSouthEastAsianLanguageProcessing,pages21–29
November1,2023.©2023AssociationforComputationalLinguistics

stackedwithlinearlayers. Givenatargetsentence, • Wrong use of nang vs. ng. These are gram-
thesequencetaggermodelpredictsthetag-encoded maticalerrorsthatmaybecausedbytheim-
transformationsforeachtoken. Thepredictedtags properuseofthewordsnangandng. These
arethenappliedtothetargetsentencethroughpost- wordsarecommonlyinterchangedmainlydue
processing to get the modified sentence. Since totheirsimilarpronunciations.
somecorrectionsinasentencemaydependonpre-
3.1.2 SpellingErrors
viouscorrections,thesameprocessisexecutedto
themodifiedsentencetocorrectitfurther. Thisis • Duplicate Words. These are spelling errors
repeateduntilthesentenceisfullycorrected. caused by mistakenly repeating a word that
The model predicts two types of token-level should not be repeated. Words such as ang
transformations: basic transformations and g- ’the’, ng ’of’, and mga (denotes the plural
transformations(Omelianchuketal.,2020). Basic form of a word) are some of the commonly
transformationsarecommontoken-leveleditoper- duplicatedwords(Octavianoetal.,2016).
ationssuchaskeepingthetokenunchanged,delet-
|     |     |     |     |     |     | • Missing | Spaces. | These | are | spelling | errors |     |
| --- | --- | --- | --- | --- | --- | --------- | ------- | ----- | --- | -------- | ------ | --- |
ingthetoken,andreplacingthetokenwithanew
token. Meanwhile,g-transformationsarecustom- causedbyimpropermergingofFilipinowords
|     |     |     |     |     |     | duetoamissingspace. |     |     | Forexample, |     | parin |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ----------- | --- | ----- | --- |
designedtransformationsthatperformtask-specific
meaning’still’iscommonlywrittenasparin
operationssuchaschangingthecaseofthecurrent
similartohow’goingto’issometimeswritten
tokenandsplittingthetokenintotwonewtokens.
as’gonna’.
Themodeltrainingisperformedthroughthree
| stages:       | (1) pre-train |          | the model  | on synthetic        | data,         |                |                                  |                              |          |     |       |     |
| ------------- | ------------- | -------- | ---------- | ------------------- | ------------- | -------------- | -------------------------------- | ---------------------------- | -------- | --- | ----- | --- |
|               |               |          |            |                     |               | • ExtraSpaces. |                                  | Thesearespellingerrorscaused |          |     |       |     |
| (2) fine-tune | the           | model    | on         | a corpus            | full of gram- |                |                                  |                              |          |     |       |     |
|               |               |          |            |                     |               | by not         | properly                         | merging                      | Filipino |     | words | to- |
| matically     | incorrect     |          | sentences, | and                 | (3) fine-tune |                |                                  |                              |          |     |       |     |
|               |               |          |            |                     |               | gether.        | Forexample,pinakamalaki’biggest’ |                              |          |     |       |     |
| the model     | on            | a corpus | of         | mixed grammatically |               |                |                                  |                              |          |     |       |     |
iserroneouslyspelledaspinakamalaki.
| correctandincorrectsentences. |     |     |     | Withpre-trained |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
transformerencoderssuchasBERT(Devlinetal., • Wrong Use of Hyphens. These are spelling
| 2018),onlytrainingstages2and3areused. |     |     |     |     | Model |        |        |        |       |        |         |     |
| ------------------------------------- | --- | --- | --- | --- | ----- | ------ | ------ | ------ | ----- | ------ | ------- | --- |
|                                       |     |     |     |     |       | errors | caused | by the | wrong | use of | hyphens | -   |
optimizationwasdoneusingtheAdamoptimizer whichmaybeusedtoseparateprefixesfrom
(KingmaandBa,2015)withdefaulthyperparame- the base word. Hyphens are used when the
ters(Omelianchuketal.,2020).
|     |     |     |     |     |     | base   | word is | a proper | noun,      | loan | word,       | or  |
| --- | --- | --- | --- | --- | --- | ------ | ------- | -------- | ---------- | ---- | ----------- | --- |
|     |     |     |     |     |     | starts | with a  | vowel    | (Octaviano | et   | al., 2016). |     |
3 Methodology
Forexample,nag-usapiserroneouslywritten
asnagusap.
3.1 CoveredGrammaticalErrors
Twocategoriesofgrammaticalerrorswerecovered • Wrong Use of Enclitics. These are spelling
bythisstudy: (1)grammarerrorsand(2)spelling errorscausedbyconfusionontherulesofen-
errors. These were derived from a book and pre- cliticsstartingwith/d/and/r/. Forexample,
vious studies that tackle Filipino grammatical er- thewordsdinandrinbothmean’also’. How-
rors(KomisyonsaWikangFilipino,2013;Goand ever,rinisusedwhenthepreviouswordsends
Borra,2016;Octavianoetal.,2016). withavowelorsemi-vowel,otherwisedinis
used.
3.1.1 GrammarErrors
| • MorphologicalErrors. |     |     |     | Thesearegrammatical |     | 3.2 Balarila |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | ------------------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
errorsthatmaybecausedbywordsthatwent ThemodeladoptedtheapproachoftheGECToR
through morphological changes (Octaviano model (Omelianchuk et al., 2020). It performs
| et  | al., 2016). | Due | to  | various morphological |     |              |         |           |          |     |         |     |
| --- | ----------- | --- | --- | --------------------- | --- | ------------ | ------- | --------- | -------- | --- | ------- | --- |
|     |             |     |     |                       |     | the GEC task | through | iterative | sequence |     | tagging |     |
processes, certain Filipino words alter their insteadofsequencegeneration. Theapproachcon-
spelling. Forexample,whentheprefix/pang- sistedoftwo(2)phases: fine-tuningandinference.
| / is | attached | to  | the word | bili ’buy’, | it yields |     |     |     |     |     |     |     |
| ---- | -------- | --- | -------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
3.2.1 Fine-tuning
thewordpambili’aresourceusedtobysome-
thing’sincetheoriginalwordbeginswith/p/, As shown in Figure 1, a pre-trained transformer
| /b/,or/m/. |     |     |     |     |     | encodersuchasBERTwasfine-tunedfortheGEC |     |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
22

|     |     |     |     |     |     | then | passed | to the | error | detection | and correction |     |
| --- | --- | --- | --- | --- | --- | ---- | ------ | ------ | ----- | --------- | -------------- | --- |
linearlayers,withSoftmaxlayersonthetoptopre-
|     |     |     |     |     |     | dict | the transformation |     |     | tags per | token. | Based on |
| --- | --- | --- | --- | --- | --- | ---- | ------------------ | --- | --- | -------- | ------ | -------- |
thepredictedtags,transformationsareappliedto
eachtokenthroughpost-processingafterwardsto
producetheoutputsentence.
Asthetechniqueisiterative,theoutputsentence
maynotbefullycorrectedyetinthefirstiteration.
Theprocessisthenrepeatedtotheoutputsentence
|     |     |     |     |     |     | to correct |     | it further. | Table | 1 shows | an  | example |
| --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | ----- | ------- | --- | ------- |
ofhowtheiterativesequencetaggingtechniqueis
usedtocorrectaninputsentence.
|          | Figure1:   | Fine-tuningPipeline |        |     |            |     | #ofIterations |     |                           | Sentence |     |     |
| -------- | ---------- | ------------------- | ------ | --- | ---------- | --- | ------------- | --- | ------------------------- | -------- | --- | --- |
|          |            |                     |        |     |            |     |               | 0   | Puntaniyasamallkahapon    |          |     |     |
|          |            |                     |        |     |            |     |               | 1   | Puntaniyasamallkahapon.   |          |     |     |
|          |            |                     |        |     |            |     |               | 2   | Puntasiyasamallkahapon.   |          |     |     |
| task. In | the second | training            | stage, | two | (2) linear |     |               |     |                           |          |     |     |
|          |            |                     |        |     |            |     |               | 3   | Pumuntasiyasamallkahapon. |          |     |     |
layerswereaddedontopofthemodelfirstwhich
|     |     |     |     |     |     |     | Table1: | Iterativesequencetaggingexample |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------- | --- | --- | --- | --- |
aretheerrordetectionanderrorcorrectionlinear
| layers.           | This was | done      | to produce |            | the task out- |     |       |                 |     |              |     |       |
| ----------------- | -------- | --------- | ---------- | ---------- | ------------- | --- | ----- | --------------- | --- | ------------ | --- | ----- |
|                   |          |           |            |            |               | In  | three | (3) iterations, |     | the sentence | was | fully |
| puts. Afterwards, |          | the model | was        | fine-tuned | with          |     |       |                 |     |              |     |       |
correctedbyaddingaperiodintheend,replacing
| error-filled | Filipino | sentences |     | (Dataset | 1). In the |      |      |           |          |       |     |          |
| ------------ | -------- | --------- | --- | -------- | ---------- | ---- | ---- | --------- | -------- | ----- | --- | -------- |
|              |          |           |     |          |            | niya | with | siya, and | changing | punta | to  | pumunta. |
thirdtrainingstage,themodelwasfine-tunedwith
|     |     |     |     |     |     | This | implied | that | the higher | the | number | of itera- |
| --- | --- | --- | --- | --- | --- | ---- | ------- | ---- | ---------- | --- | ------ | --------- |
botherror-filledanderror-freeFilipinosentences
|             |                                  |     |     |     |     | tions, | the | better the | result | will be. | However, | it is |
| ----------- | -------------------------------- | --- | --- | --- | --- | ------ | --- | ---------- | ------ | -------- | -------- | ----- |
| (Dataset2). | Thesetrainingstageswereperformed |     |     |     |     |        |     |            |        |          |          |       |
tobetakenintoaccountthatthehigherthenumber
insequenceascrucialtothemodel’sperformance
(Omelianchuketal.,2020). Fine-tuningthemodel ofiterations,thelowertheinferencespeedofthe
|          |              |           |     |         |           | model.  | The      | number | of      | iterations  | should | be con-  |
| -------- | ------------ | --------- | --- | ------- | --------- | ------- | -------- | ------ | ------- | ----------- | ------ | -------- |
| first on | error-filled | sentences |     | allowed | the model |         |          |        |         |             |        |          |
|          |              |           |     |         |           | figured | properly | to     | produce | an accurate |        | and fast |
toeffectivelylearnthedifferenttypesofFilipino
|     |     |     |     |     |     | model | (Omelianchuk |     | et  | al., 2020). | For | Balarila, |
| --- | --- | --- | --- | --- | --- | ----- | ------------ | --- | --- | ----------- | --- | --------- |
errorscovered,thecontextsoftheerrors,andthe
|          |            |          |          |     |           | the                     | default | number | of iterations |                     | set by | GECToR |
| -------- | ---------- | -------- | -------- | --- | --------- | ----------------------- | ------- | ------ | ------------- | ------------------- | ------ | ------ |
| patterns | of correct | Filipino | grammar. |     | For model |                         |         |        |               |                     |        |        |
|          |            |          |          |     |           | wasused,whichisfive(5). |         |        |               | Themodelcorrectsone |        |        |
optimization,theAdamoptimizer(KingmaandBa,
|     |     |     |     |     |     | errorperiteration. |     |     | Withthisapproach,errorsthat |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --------------------------- | --- | --- | --- |
2015)withdefaulthyperparameterswasutilized.
canonlybecorrectedbasedonpreviouscorrections
| 3.2.2 | Inference |     |     |     |     | arecorrectedonthesucceedingiterations. |     |     |     |     |     |     |
| ----- | --------- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
3.2.3 TransformationTags
Table2showsthetransformationtagsusedbythe
|     |     |     |     |     |     | model | to  | correct each | covered | grammatical |     | error. |
| --- | --- | --- | --- | --- | --- | ----- | --- | ------------ | ------- | ----------- | --- | ------ |
MostofthetagswereadoptedfromtheGECToR
|     |     |     |     |     |     | (Omelianchuk             |     | et al., | 2020) | model,           | and | a new set |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | ------- | ----- | ---------------- | --- | --------- |
|     |     |     |     |     |     | oftagswasalsointroduced. |     |         |       | Thesenewtagswere |     |           |
usedforothererrorsthatwerenotcoveredbythe
defaultsetoftagssuchasFilipinomorphological
errorsandpunctuationerrors.
| Figure2: | InferenceSequenceTaggingPipeline |     |     |     |     |     |     |     |     |     |     |     |
| -------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thetagsusedinmorphologicalerrorsrepresent
|     |     |     |     |     |     | Tagalogverbformtransformations. |     |     |     |     | Tagalogverb |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ----------- | --- |
Figure2showsBalarila’sinferencepipelineas forms are created using four (4) aspects which
adoptedfromGECToR(Omelianchuketal.,2020). arecompleted,incompleted,contemplated,andre-
Tocorrectthegrammaticalerrorsinaninputsen- cently completed. The focus of the verb is also
tence, the input sentence is first passed into the includedthustheverbanditsaspectcaneitherbe
fine-tuned transformer encoder model to be con- in actor-focus or object-focus form. See Table 3
vertedintoacontextvector. Thecontextvectoris forsomeexamplesundereach.
23

|     | ErrorTypes |     |     | Tags |     | Tag | VerbForm |     |     | Examples |     |
| --- | ---------- | --- | --- | ---- | --- | --- | -------- | --- | --- | -------- | --- |
WrongUseofnangvs.ng $REPLACE_nang,$REPLACE_ng BASE Base luto,sagot,sukat
|     |     |     | $REPLACE_daw,$REPLACE_din,    |     |     |         | CompletedAspect+ |     |     |                          |     |
| --- | --- | --- | ----------------------------- | --- | --- | ------- | ---------------- | --- | --- | ------------------------ | --- |
|     |     |     | $REPLACE_dito,$REPLACE_diyan, |     |     | COMPACT | ActorFocus       |     |     | nagluto,sumagot,nagsukat |     |
WrongUseofEnclitics $REPLACE_doon,$REPLACE_raw, IncompletedAspect+
|     |     |     |                              |     |     | INCACT  |                     |     | nagluluto,sumasagot,nagsusukat |     |     |
| --- | --- | --- | ---------------------------- | --- | --- | ------- | ------------------- | --- | ------------------------------ | --- | --- |
|     |     |     | $REPLACE_rin,$REPLACE_roon,  |     |     |         | ActorFocus          |     |                                |     |     |
|     |     |     | $REPLACE_rito,$REPLACE_riyan |     |     |         | ContemplatedAspect+ |     |                                |     |     |
|     |     |     |                              |     |     | CONTACT |                     |     | magluluto,sasagot,magsusukat   |     |     |
|     |     |     | $MERGE_HYPHEN,               |     |     |         | ActorFocus          |     |                                |     |     |
WrongUseofHyphens $TRANSFORM_INSERT_HYPHEN, ImperativeAspect+
|     |     |     |     |     |     | IMPACT | ActorFocus |     |     | magluto,magsagot,magsukat |     |
| --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | --- | ------------------------- | --- |
$TRANSFORM_SPLIT_HYPHEN
|                  |     |     | $ M E  | R G E _ SP A C E | ,          |         | Com p | le te d A s p ect+ |     |                        |     |
| ---------------- | --- | --- | ------ | ---------------- | ---------- | ------- | ----- | ------------------ | --- | ---------------------- | --- |
| WrongUseofSpaces |     |     |        |                  |            | COMPOBJ |       |                    |     | niluto,sinagot,sinukat |     |
|                  |     |     | $ TR A | N S F O R M _ S  | PLIT_SPACE |         | A     | c to r F oc u s    |     |                        |     |
IncompletedAspect+
| DuplicateWords |     |     | $DELETE                  |     |     | INCOBJ  |                     |     |     | niluluto,sinasagot,sinusukat |     |
| -------------- | --- | --- | ------------------------ | --- | --- | ------- | ------------------- | --- | --- | ---------------------------- | --- |
|                |     |     | $TRANSFORM_VERB_BASE,    |     |     |         | ObjectFocus         |     |     |                              |     |
|                |     |     | $TRANSFORM_VERB_COMPACT, |     |     |         | ContemplatedAspect+ |     |     |                              |     |
|                |     |     |                          |     |     | CONTOBJ | ObjectFocus         |     |     | lulutuin,sasagutin,susukatin |     |
$TRANSFORM_VERB_COMPOBJ,
|     |     |     |     |     |     |     | Imp er | a t iv e A s p e ct+ |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------------------- | --- | --- | --- |
MorphologicalErrors $ T R A N S F O R M _ V E R B _ C O N T A C T , IMPOBJ lutuin,sagutin,sukatin
|     |     |     | $ T R A | N S F O R M _ V | E R B _ C O N T O B J, |         | O b                     | j e ct F o c u s |     |                              |     |
| --- | --- | --- | ------- | --------------- | ---------------------- | ------- | ----------------------- | ---------------- | --- | ---------------------------- | --- |
|     |     |     |         |                 |                        | RECCOMP | RecentlyCompletedAspect |                  |     | kaluluto,kasasagot,kasusukat |     |
$TRANSFORM_VERB_INCACT,
$TRANSFORM_VERB_INCOBJ,
$TRANSFORM_VERB_RECCOMP Table3: TagalogVerbFormTransformationTags
$ADD_PUNC_EMARK,
$ADD_PUNC_PERIOD,
$ADD_PUNC_QMARK,
WrongUseofPunctuationMarks
$CHANGE_PUNC_EMARK, contained multiple sentences within them-
$CHANGE_PUNC_PERIOD,
|     |     |     | $CHANGE_PUNC_QMARK |     |     | selvesseparatedbyperiods. |     |     |     | Thesesentences |     |
| --- | --- | --- | ------------------ | --- | --- | ------------------------- | --- | --- | --- | -------------- | --- |
$TRANSFORM_CASE_CAPITAL, werefurthersplitbasedontheperiodcharac-
ImproperWordCasing
$TRANSFORM_CASE_LOWER
|     |     |     | $APPEND_t1 |     |     | ter’slocation. |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
MissingWords
$REPLACE_nila,$REPLACE_niya
WrongUseofAngandNgPronouns
$REPLACE_sila,$REPLACE_siya
|     |     |     |     |     |     | • Invalid | Characters. |     | Some | sentence | entries |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ---- | -------- | ------- |
Table2: ErrorTypesandTransformationTags contained invalid characters such as emojis.
Assuch,thesesentencesweredropped.
3.3 DataCollection
|     |     |     |     |     |     | • English-dominantSentences. |     |     |     | Somesentence |     |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------------ | --- |
The datasets used for this study are composed of entries were dominated by English words.
|     |     |     |     |     |     | Withthis, |     | sentencesthatarecomposedofat |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | ---------------------------- | --- | --- | --- |
sentencesscrapedfromvariouspubliclyavailable
mainstream Filipino news websites - specifically least50%Filipinowordswereretained,while
Abante,Bandera,GMA,andPilipinoStarNgayon. the rest were dropped. The 50% threshold
In total, 58,464 news articles were scraped, and wassetbecauseusingFilipinosometimesstill
requiresborrowedEnglishwords.
thesearticlescontainedatotalof510,411rawsen-
tences. Itisworthnotingthatsomeofthesearticles
3.5 ErrorAutomation
arewritteninTaglish-whichisacombinationof
EnglishandTagalogwords. Furthermore,inorder Incorruptingthecleanedsentences,avarietyofap-
to prevent re-introducing the Filipino RoBERTa proacheswereuseddependingonthegrammatical
models(CruzandCheng,2021)tothesamenews errortobereproduced. Itisalsoworthnotingthat
articles they were trained on, only news articles thispipelinewasdesignedwiththeassumptionthat
datedJanuary2021andonwardwereincludedin
onlyoneerrorwastobeintroducedpercorrupted
| scraping. | ThecutoffforthescrapeddatawasMay |          |          |          |          | sentence. |              |     |         |          |      |
| --------- | -------------------------------- | -------- | -------- | -------- | -------- | --------- | ------------ | --- | ------- | -------- | ---- |
| 2023,     | since                            | this was | when the | scraping | was last |           |              |     |         |          |      |
|           |                                  |          |          |          |          | • Word    | Replacement. |     | Replace | a target | word |
performedbeforethemodelswerefinalized.
|     |     |     |     |     |     | with | another. | Applicable |     | to morphological |     |
| --- | --- | --- | --- | --- | --- | ---- | -------- | ---------- | --- | ---------------- | --- |
3.4 DataCleaning
|     |     |     |     |     |     | errors,wronguseofnangvs. |     |     |     | ng,andwrong |     |
| --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | ----------- | --- |
useofenclitics.
| Some | cleaning | were | performed | on the | collected |     |     |     |     |     |     |
| ---- | -------- | ---- | --------- | ------ | --------- | --- | --- | --- | --- | --- | --- |
rawsentences:
|     |     |     |     |     |     | • Character |     | Replacement. |     | Replace | a single |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ------- | -------- |
• IncorrectEnclitics. Somesentenceentriesin- characterwithanother. Applicabletowrong
correctlyuseentries(i.e., rawvs. daw, roon use of hyphens, wrong use of punctuation
vs. doon)priortoscraping. Thesewerecor- marks,andimproperwordcasing.
|     | rected | using a rule-based |     | enclitic-correcting |     |                       |     |     |                   |     |     |
| --- | ------ | ------------------ | --- | ------------------- | --- | --------------------- | --- | --- | ----------------- | --- | --- |
|     |        |                    |     |                     |     | • PunctuationRemoval. |     |     | Removethepunctua- |     |     |
algorithm.
|     |     |     |     |     |     | tionmarkattheendofthesentence. |     |     |     |     | Applica- |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | -------- |
• Multiple Sentences. Some sentence entries bletothewronguseofpunctuationmarks.
24

|                    |              |                       |     |             | Dataset | Error-freeSentences |     | Error-filledSentences | TOTAL   |
| ------------------ | ------------ | --------------------- | --- | ----------- | ------- | ------------------- | --- | --------------------- | ------- |
| • Word             | Duplication. | Duplicate             | a   | target word |         |                     |     |                       |         |
|                    |              |                       |     |             | 1       | 0                   |     | 601,256               | 601,256 |
| withinthesentence. |              | Applicabletoduplicate |     |             |         |                     |     |                       |         |
|                    |              |                       |     |             | 2       | 155,419             |     | 150,283               | 305,702 |
| worderrors.        |              |                       |     |             | TOTAL   | 155,419             |     | 751,539               | 906,958 |
Table4: Balariladataseterror-freeanderror-filledsen-
| • Word | Deletion. | Delete | a target | word within |     |     |     |     |     |
| ------ | --------- | ------ | -------- | ----------- | --- | --- | --- | --- | --- |
tencescomposition
| thesentence. |     | Applicabletomissingworder- |     |     |     |     |     |     |     |
| ------------ | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
rors.
|        |            |        |           |          | As for | the two datasets, |     | a 0:100 error-free | and |
| ------ | ---------- | ------ | --------- | -------- | ------ | ----------------- | --- | ------------------ | --- |
| • Word | Stitching. | Stitch | two words | together |        |                   |     |                    |     |
80:20error-filledratiowasestablishedbetweenthe
byremovingthespaceorhyphenin-between
two. Thisresultsinanapproximatelyequalnumber
| them. | Applicable | to  | missing | spaces and |     |     |     |     |     |
| ----- | ---------- | --- | ------- | ---------- | --- | --- | --- | --- | --- |
oferror-freeanderror-filledsentencesinDataset
wronguseofhyphenserrors.
2. Theactualnumberofsentencesperdatasetcan
• Word Splitting. Insert a single space in- be seen in Table 4. The whole Balarila dataset
containsatotalof906,958sentences.
| between | a pair | of syllables | in a | target word. |     |     |     |     |     |
| ------- | ------ | ------------ | ---- | ------------ | --- | --- | --- | --- | --- |
Thedatasetswerethensplitintothree(3)subsets
Applicabletoextraspaceserrors.
|            |            |       |                  |     | each: train,          | dev, and | test              | with a 70:15:15 | ratio of |
| ---------- | ---------- | ----- | ---------------- | --- | --------------------- | -------- | ----------------- | --------------- | -------- |
| • Multiple | Sentences. | Given | a multi-sentence |     |                       |          |                   |                 |          |
|            |            |       |                  |     | sentencedistribution. |          | Asforthetestsets, |                 | itssen-  |
input, a single sentence is randomly chosen tences were further grouped according to: (1) its
andiscorruptedusingeitherthecharacterre- transformationtagand(2)whetheritisgrammati-
placementorpunctuationremovalapproach. callycorrectornot. Thisisfortheeasierevaluation
ofthemodelsundereachtag.
3.6 Datasets
Finally,forthedistributionoferrors,asidefrom
A total of two (2) datasets were needed with re- theimpositionofa30,000-sentencecap,thedataset
spect to the second and third fine-tuning stages creationalgorithmalsogoesthroughthesentences
in the GECToR model’s approach (Omelianchuk undereachtransformationtaganddistributesthe
etal.,2020). Adatasetcreationalgorithmwasused error-freeanderror-filledsentencesontothetrain,
to create the needed datasets using the corrupted dev,andtestsubsetswithrespecttotheaforemen-
sentencesproducedbytheerrorautomationalgo- tioned 0:100, 80:20, and 70:15:15 ratios. Since
| rithm. |     |     |     |     | this splitting | was performed |     | for each | transforma- |
| ------ | --- | --- | --- | --- | -------------- | ------------- | --- | -------- | ----------- |
The first dataset is intended for fine-tuning on tion tag, this also ensures that each tag was split
error-filled sentences alone. The second dataset inthesamemanner. Thus,thisalsoensuresbetter
is intended for fine-tuning on both error-free and equalityandrepresentationforeachtag.
| error-filled | sentences. | Each | sentence | in these |     |     |     |     |     |
| ------------ | ---------- | ---- | -------- | -------- | --- | --- | --- | --- | --- |
3.7 DataPre-processing
datasetshaditscorrectedcounterpartasitslabel–
eventheerror-freeones. Beforefeedingthedatasetsintothemodels,each
For each transformation tag, it was ensured source-targetpairofsentenceswerepre-processed
that each tag was equally represented within the first with respect to the pre-processing algorithm
datasets. A 30,000 upper limit on the number of used in the GECToR (Omelianchuk et al., 2020)
sentences under each transformation tag. How- model. This is done to efficiently determine and
ever, there were certain tags that contained less attach the transformation tags needed to convert
than 30,000 sentences, since there was a lack of the source tokens into their corresponding target
| sentencesneededincorruptingforthosetags. |     |     |     | This      | tokens. |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --------- | ------- | --- | --- | --- | --- |
| wasalimitationwiththedatascraped.        |     |     |     | Anexample |         |     |     |     |     |
3.8 ExperimentSetup
ofthisisthe$REPLACE_riyantag–whichonly
hadatotalof472corruptedsentences. Thisisbe- Toachievethebest-performingmodel,anexperi-
causethewordriyanwasnotbeingusedthatmuch mentalsetupinvolvingthethree(3)transformeren-
inthescrapednewsarticles. codermodelswasprepared. Specifically,theBERT
Furthermore, a 17:83 ratio was maintained be- Tagalog Base (BERT-Base) (Cruz and Cheng,
tweenerror-freeanderror-filledsentencesforeach 2019),RoBERTaTagalogBase(RoBERTa-Base)
transformationtag. Thisimpliesthat,ifapplicable, (Cruz and Cheng, 2021), and RoBERTa Tagalog
agiventransformationtagcontainsapproximately Large(RoBERTa-Large)(CruzandCheng,2021)
5,000error-freeand25,000error-filledsentences. modelswerefine-tunedandtestedusingthedataset
25

| discussedinSubsection3.6. |     |     |     | Furthermore,allofthe |     |     |     |
| ------------------------- | --- | --- | --- | -------------------- | --- | --- | --- |
modelswerefine-tunedandtestedonanNVIDIA
RTXA6000GPUusingtheGECToRmodel’sde-
faultfine-tuningandpredictinghyperparameters.
3.9 Evaluation
| To evaluate    | the | GEC     | performance |         | of the  | models, |     |
| -------------- | --- | ------- | ----------- | ------- | ------- | ------- | --- |
| the precision, |     | recall, | and         | F score | metrics | from    |     |
0.5
| the CoNLL-2014 |     | Shared |     | Task | (Ng et | al., 2014) |     |
| -------------- | --- | ------ | --- | ---- | ------ | ---------- | --- |
wereadopted.
| Forthemodels’GEDperformance,amulti-class |                                    |     |          |     |               |        | (a)Precision |
| ---------------------------------------- | ---------------------------------- | --- | -------- | --- | ------------- | ------ | ------------ |
| confusion                                | matrix                             | was | used     | and | visualized    | with a |              |
| heatmap.                                 | Withthe39pre-defineduniquetagsenu- |     |          |     |               |        |              |
| merated                                  | in Table                           | 2,  | the task | of  | the model     | was to |              |
| classify                                 | the erroneous                      |     | token    | in  | a sentence    | to its |              |
| correspondingtransformationtag.          |                                    |     |          |     | Thelighterthe |        |              |
colorofthetileintheconfusionmatrix,thebetter
theperformanceofthemodelindetectingerrors.
| The        | GED          | performance |          | was         | tested     | on error-  |           |
| ---------- | ------------ | ----------- | -------- | ----------- | ---------- | ---------- | --------- |
| free and   | error-filled |             | datasets | separately. |            | To de-     |           |
| termine    | the accuracy |             | of       | the model   | on         | error-free |           |
| sentences, | the          | prediction  |          | should      | correspond | with       | (b)Recall |
’NOCHANGES’sinceitisexpectedthatthemodel
shouldnotmakeanycorrectionsonthesesentences.
| When the | models       | are | tested         | on  | the incorrect | sen-     |     |
| -------- | ------------ | --- | -------------- | --- | ------------- | -------- | --- |
| tences,  | the accuracy |     | is ascertained |     | when          | the pre- |     |
dictedtagmatchesthetargettag.
4 Results&Analysis
TheGECperformanceresultsofthethree(3)mod-
| els are             | shown | in Figure |          | 3. In | terms       | of preci- |     |
| ------------------- | ----- | --------- | -------- | ----- | ----------- | --------- | --- |
| sion, RoBERTa-Large |       |           | obtained |       | the highest | score     |     |
(c)F Score
| of 67.94 | as illustrated |     | in  | Figure | 3a. On | the other | 0.5 |
| -------- | -------------- | --- | --- | ------ | ------ | --------- | --- |
hand, Figure 3b shows the performances of the Figure3: GECPerformanceoftheThreeModels
| models            | in regard | to  | recall   | where | RoBERTa-Base |           |     |
| ----------------- | --------- | --- | -------- | ----- | ------------ | --------- | --- |
| and RoBERTa-Large |           |     | achieved |       | similar      | scores of |     |
84.69and84.76respectively. FortheF scores Thedifficultyindetectingduplicatewordsmay
0.5
asdisplayedinFigure3c,RoBERTa-Largealsoob- beattributedtotheerrorautomationalgorithmused
whichisWordDuplication. Theproblemthatmay
tainedthehighestscoreof70.75incomparisonto
RoBERTa-Base’sscoreof69.00. Moreover,BERT- arise from this algorithm is the vagueness of the
Base had the poorest performance in every GEC duplicated word in a sentence since there are no
scoreamongthethree(3)models. restrictions on when to duplicate a word. This
mayhaveresultedinapoorperformancetowards
| As for | the | GED | performance |     | of the | three (3) |     |
| ------ | --- | --- | ----------- | --- | ------ | --------- | --- |
models,Table6showsthesummaryoftheresults correctingerrorsrelatedtoDuplicateWordssince
fromtheconfusionmatrices. Thesearethegrouped themodelswouldfinditdifficulttodeterminewhen
todeleteawordinasentencegivenalltheunique
averagescoresofthetransformationtagspererror
Filipinowordsitwasintroducedto.
typeonbotherror-freeanderror-filleddatasets.
As observed in Table 6a, all three (3) models For themorphologicalerrors, its errorautoma-
faced difficulties in identifying errors associated tionrandomlyreplacesaverbbyeitherchanging
withduplicatewords,morphologicalerrors,wrong itsaspect,focus,orboth. Withsix(6)possiblemor-
useofpunctuationmarks,andmissingwords. phological transformations for a single Tagalog
26

BERT-Base RoBERTa-Base RoBERTa-Large addtothesentence,themodelsalsostruggledwith
CoveredErrors
WrongUseofnangvs.ng 96.21% 96.86% 96.73% addingtheappropriateFilipinowordgiventhecon-
| WrongUseofEnclitics |     | 97.48% |     | 87.43% | 84.85% |     |                    |     |     |                         |     |     |     |
| ------------------- | --- | ------ | --- | ------ | ------ | --- | ------------------ | --- | --- | ----------------------- | --- | --- | --- |
| WrongUseofHyphens   |     | 98.39% |     | 98.61% | 98.82% |     |                    |     |     |                         |     |     |     |
|                     |     |        |     |        |        |     | textofthesentence. |     |     | Thisalsocausedthemodels |     |     |     |
| WrongUseofSpaces    |     | 98.82% |     | 99.28% | 99.35% |     |                    |     |     |                         |     |     |     |
| DuplicateWords      |     | 99.48% |     | 98.95% | 98.82% |     |                    |     |     |                         |     |     |     |
MorphologicalErrors 91.59% 92.87% 91.61% toobtainalowerscoreinthiserrortype.
AdditionalErrors
WrongUseofPunctuationMarks 95.77% 94.78% 93.58% It was also discovered that some scraped sen-
| ImproperWordCasing |     | 98.45% |     | 98.32% | 98.49% |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
MissingWords 98.04% 96.47% 96.99% tenceswerealreadyerroneousbeforeevengoing
| WrongUseofAngandNgPronouns |     | 89.89% |     | 96.91% | 97.41% |     |         |           |            |     |           |     |        |
| -------------------------- | --- | ------ | --- | ------ | ------ | --- | ------- | --------- | ---------- | --- | --------- | --- | ------ |
|                            |     |        |     |        |        |     | through | the error | automation |     | pipeline. |     | An ex- |
(a)Error-FreeDataset
|               |     |           |              |     |               |     | ample of  | this    | are sentences |       | that   | incorrectly | used     |
| ------------- | --- | --------- | ------------ | --- | ------------- | --- | --------- | ------- | ------------- | ----- | ------ | ----------- | -------- |
|               |     |           |              |     |               |     | enclitics | - which | were          | fixed | in the | data        | cleaning |
| CoveredErrors |     | BERT-Base | RoBERTa-Base |     | RoBERTa-Large |     |           |         |               |       |        |             |          |
WrongUseofnangvs.ng 94.31% 95.72% 96.45% pipeline. However,fortheotherunaddressederrors,
| WrongUseofEnclitics |     | 97.24% |     | 98.06% | 95.66% |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
WrongUseofHyphens 89.83% 94.65% 93.84% itwentthroughtheerrorautomationpipelinewith
| WrongUseofSpaces |     | 82.46% |     | 88.42% | 88.55% |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
DuplicateWords 61.31% 80.99% 79.12% theassumptionthatitwasgrammaticallycorrect.
| MorphologicalErrors |     | 56.43% |     | 71.87% | 73.13% |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
AdditionalErrors As such, there may be some corrupted sentences
| WrongUseofPunctuationMarks |     | 67.51% |     | 79.98% | 80.76% |     |     |     |     |     |     |     |     |
| -------------------------- | --- | ------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ImproperWordCasing 93.52% 96.35% 96.31% within the dataset that contain more than one (1)
| MissingWords               |     | 27.18% |     | 48.73% | 49.40% |     |         |      |       |      |             |          |     |
| -------------------------- | --- | ------ | --- | ------ | ------ | --- | ------- | ---- | ----- | ---- | ----------- | -------- | --- |
| WrongUseofAngandNgPronouns |     | 95.53% |     | 97.96% | 97.78% |     |         |      |       |      |             |          |     |
|                            |     |        |     |        |        |     | errors. | This | could | have | potentially | affected | the |
(a)Error-FilledDataset resultsofthestudyinavarietyofwayssuchas:
| Table 6:    | Grouped | GED | Performance |     | Results | of the |              |               |                          |       |            |       |           |
| ----------- | ------- | --- | ----------- | --- | ------- | ------ | ------------ | ------------- | ------------------------ | ----- | ---------- | ----- | --------- |
| ThreeModels |         |     |             |     |         |        | • A          | model         | being                    | able  | to correct | the   | unex-     |
|             |         |     |             |     |         |        | pectederror. |               | Thoughthismaybemoreprac- |       |            |       |           |
|             |         |     |             |     |         |        | tical        | in real-world |                          | uses, | this       | would | result in |
verb,thereareoccurrenceswhereinthecorrupted
lowerperformancescoresforthemodelinthe
sentencemaystillbegrammaticallysoundwhich
|     |     |     |     |     |     |     | contextofthisstudy. |     |     |     | Thisisbecausethegold |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | -------------------- | --- | --- |
canconfusethemodels. Anexampleofthiswould standard edits assumed that the only errors
| be’Tiranilangbolakahapon.’ |     |     |     | whereinitwasex- |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thatthecorruptedsentenceshadweretheones
| pected that | the | words Tira | and | ng were | replaced |     |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
introducedbytheerrorautomationpipeline.
| withTiniraandangrespectively. |      |      |        | Instead,themod- |           |       |     |     |     |     |     |     |     |
| ----------------------------- | ---- | ---- | ------ | --------------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| els replaced                  | Tira | with | Tumira | and             | nila with | sila, |     |     |     |     |     |     |     |
• Amodelbeingmistakenlytaughtthatthe
| resultingin’Tumirasilangbolakahapon.’ |     |     |     |     |     | which |                             |     |     |     |     |              |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ----- | --------------------------- | --- | --- | --- | --- | ------------ | --- |
|                                       |     |     |     |     |     |       | erroneoussentenceiscorrect. |     |     |     |     | Thiscouldpo- |     |
isstillgrammaticallycorrect. Thismayhavebeen tentiallyleadtomoreconfusionforthemod-
the cause regarding the models’ performances in els - mainly due to the inconsistencies with
| this error | type | for both | error-free | and | error-filled |     |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
howcorrectandincorrectsentencesarebeing
| sentences. |     |     |     |     |     |     | presented |     | to it. | Though | this | would | result in |
| ---------- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | ------ | ---- | ----- | --------- |
Moreover, the models struggled in identifying better performance scores in the context of
thewronguseofpunctuationmarksspecificallyfor thisstudy,thisisnotpracticalwhenitcomes
EMARKtransformationtagsastherearenocom-
toreal-worldusage.
| mon indicators |     | when a | Filipino | sentence |     | should |     |     |     |     |     |     |     |
| -------------- | --- | ------ | -------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
be ended with an exclamation mark. Although, Therewasalsoaninconsistencytowardscorrect-
| the models | performed |     | well for | the | PERIOD | and |     |     |     |     |     |     |     |
| ---------- | --------- | --- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ingthesameerroneoussentencewhenmoreerrors
QMARK tags since the PERIOD tags are often were added. An example of this is when given
usedtoendasentence,andtheQMARKtagsare theerroneoussentence’Angadoboaykinainniya
|     |     |     |     | sino, | saan, | ano, |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
hinted by many words such as kahapon.’,whereinthewordsadoandbomustbe
bakit,andba,whichEMARKdoesnothave. An mergedtogether,thiswillnotbecorrectedbythe
exampleofthiswouldbe’Anggalingnamanniya.’ modelsanymorewhentheperiod(’.’) isremoved
whereinitwasexpectedforthemodelstoreplace from the erroneous sentence. The inconsistency
| theperiodwithanexclamationmark. |     |     |     |     | However,the |     |            |      |        |     |                  |     |         |
| ------------------------------- | --- | --- | --- | --- | ----------- | --- | ---------- | ---- | ------ | --- | ---------------- | --- | ------- |
|                                 |     |     |     |     |             |     | might have | been | caused |     | by the dataset’s |     | lack of |
modelsdidnotperformthecorrectionandtreated instancestorepresentthesameerrorinadifferent
the sentence as non-erroneous, which is still cor- setting. In the case of the example sentence, the
| rect. |     |     |     |     |     |     | datasetdidnothaveenoughinstancestorepresent |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
Forthemissingwordserror,theerrorautomation theerrorinsentenceswithoutaperiodattheend.
algorithmusedforthiserrortypeisWordDeletion Solvingthisissueischallengingwiththecurrenter-
which had similar issues with Word Duplication. rorautomationsinceonlyoneerrorwasintroduced
With all the unique Filipino words it learned to percorruptedsentence.
27

Overall, RoBERTa-Large was the best model duplicatewords,morphologicalerrors,wronguse
for the Filipino GEC task. Even though BERT- of nang vs. ng, wrong use of spaces, wrong use
BaseandRoBERTa-BaseoutperformedRoBERTa- of hyphens, wrong use of enclitics, wrong use of
LargeinsomeerrortypesasobservedintheGED punctuationmarks,improperwordcasing,missing
results,RoBERTa-Largegenerallyperformedbet- words,andwronguseofangandngpronouns.
| ter than | them | in terms | of the | GEC scores. | This |         |            |     |                |     |           |
| -------- | ---- | -------- | ------ | ----------- | ---- | ------- | ---------- | --- | -------------- | --- | --------- |
|          |      |          |        |             |      | Another | limitation | is  | the rule-based |     | error au- |
meansthatwhenitcomestoproducingcorrections, tomation. The generation of a synthetic dataset
RoBERTa-Large’soutputsweretheclosesttothe for this study was hindered by a number of prob-
gold-standardsentencesinthedatasetcomparedto
|     |     |     |     |     |     | lems such | as the vagueness |     | of Word | Duplication |     |
| --- | --- | --- | --- | --- | --- | --------- | ---------------- | --- | ------- | ----------- | --- |
BERT-BaseandRoBERTa-Base’soutputs.
andWordDeletionalgorithmsusedforthedupli-
However, RoBERTa-Large often encountered cateandmissingworderrors.
memoryissuesduringtrainingwhichcausedsome Several recommendations are suggested based
| modifications |     | to the model’s |     | training parameters. |     |                 |       |     |           |      |          |
| ------------- | --- | -------------- | --- | -------------------- | --- | --------------- | ----- | --- | --------- | ---- | -------- |
|               |     |                |     |                      |     | on this study’s | scope | and | findings. | With | the lim- |
Theparameteradjustmentswerenecessarydueto
|     |     |     |     |     |     | ited types | of errors | covered | by  | Balarila, | the first |
| --- | --- | --- | --- | --- | --- | ---------- | --------- | ------- | --- | --------- | --------- |
thelackofavailableGPUMemory(VRAM)which
|        |             |             |     |             |        | recommendation | is  | greater | error | coverage. | It is |
| ------ | ----------- | ----------- | --- | ----------- | ------ | -------------- | --- | ------- | ----- | --------- | ----- |
| caused | the model’s | fine-tuning |     | to abruptly | termi- |                |     |         |       |           |       |
recommendedthatfutureresearcherscovermore
| nate intermittently. |     | Such | problems | were | less re- |     |     |     |     |     |     |
| -------------------- | --- | ---- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- |
Filipinogrammaticalerrorsinordertoproducea
curringforBERT-BaseandRoBERTa-Basesince
morerobustandcomprehensivemodel.
| these two | models | are | smaller | in size. | With this, |     |     |     |     |     |     |
| --------- | ------ | --- | ------- | -------- | ---------- | --- | --- | --- | --- | --- | --- |
Thenextrecommendationistointroduceamore
RoBERTa-Basewasthemostcost-effectivemodel
sophisticatederrorautomationalgorithmthatwill
| sinceitonlyhada1.75%F |     |               |     | scoredifferencein |           |                                             |     |     |     |     |        |
| --------------------- | --- | ------------- | --- | ----------------- | --------- | ------------------------------------------- | --- | --- | --- | --- | ------ |
|                       |     |               | 0.5 |                   |           | improvetheperformancetowardsthefour(4)error |     |     |     |     |        |
| comparison            | to  | RoBERTa-Large |     | despite           | utilizing |                                             |     |     |     |     |        |
|                       |     |               |     |                   |           | typeswhereinBalarilaperformedpoorly,        |     |     |     |     | aswell |
fewerresourcesduringtraining.
asresolvetheinconsistencytowardscorrectingthe
|     |     |     |     |     |     | same erroneous | sentence. |     | An example |     | of this is |
| --- | --- | --- | --- | --- | --- | -------------- | --------- | --- | ---------- | --- | ---------- |
5 Conclusion&Recommendations
|     |     |     |     |     |     | to target | specific words |     | which commonly |     | trigger |
| --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | -------------- | --- | ------- |
In this study, a proof-of-concept deep learning- duplicate and missing words errors, which could
bedeterminerslikeangandmga.
| based | model | named | Balarila | was built | to de- |     |     |     |     | Anotheristoin- |     |
| ----- | ----- | ----- | -------- | --------- | ------ | --- | --- | --- | --- | -------------- | --- |
troducemultipleerrorsuponcorruptingasentence,
| tect and | correct | grammatical |     | errors in | the Fil- |     |     |     |     |     |     |
| -------- | ------- | ----------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- |
whichwasnotdone.
| ipino language |     | effectively. | With | the adoption | of  |     |     |     |     |     |     |
| -------------- | --- | ------------ | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
GECToR (Omelianchuk et al., 2020)’s approach, Theuseofrealdataforbuildingandtraininga
three (3) Balarila models were created and fine- GEC model for the Filipino language could also
tuned for the task. Each model utilized the open- helptoremovethebiasorinaccuracythatmayhave
source pre-trained BERT Tagalog Base (BERT- beencausedbytheerrorautomation. AsBalarila
Base)(CruzandCheng,2019),RoBERTaTagalog wastrainedonasyntheticallygenerateddataset,fu-
Base (RoBERTa-Base) (Cruz and Cheng, 2021), tureresearchersarerecommendedtouseadataset
collectedfromreal-worldsourcesinordertorepre-
| and RoBERTa |     | Tagalog | Large | (RoBERTa-Large) |     |     |     |     |     |     |     |
| ----------- | --- | ------- | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- |
(CruzandCheng,2021)transformerencodermod- senttheactualdiversityofdataandproducemore
| elsrespectively. |     |     |     |     |     | accuratecorrections. |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
Furthermore,anerrorautomationpipelinewas Itisalsorecommendedtoperformhyperparam-
alsobuilttocreateasyntheticdatasetofgrammati- eter tuning. As an alternative to increasing the
callyincorrectFilipinosentences. Itwasthenuti- datasetsize,hyperparametertuningcanalsohelp
lizedinfine-tuningandtestingthethree(3)Balarila toimprovethemodel’sperformancebyfindingthe
models. Two(2)fine-tuningstagesfromGECToR optimal values for the hyperparameters used dur-
| (Omelianchuketal.,2020)wereadopted: |     |     |     |     | firstona |              |                 |     |     |          |          |
| ----------------------------------- | --- | --- | --- | --- | -------- | ------------ | --------------- | --- | --- | -------- | -------- |
|                                     |     |     |     |     |          | ing training | and prediction. |     | It  | can also | possibly |
datasetoferror-filledsentencesthenonadatasetof reduce training time, increase model robustness
botherror-filledanderror-freesentences. Thecre- bymakingitlesssensitivetochangesinthedata,
ateddatasetscanalsobeusedasabenchmarkfor
andimprovethemodel’sgeneralizationofthedata
Filipinogrammarerrordetectionandcorrection. to produce more accurate corrections. In short,
However, there are several limitations to this conducting hyperparameter tuning can lead to a
study. Firstisthecoverageoferrors. Thegrammat- significantimprovementinthemodel’sGECand
| icalerrorsthatBalarilaonlycoversareasfollows: |     |     |     |     |     | GEDperformance. |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- |
28

Acknowledgements
|     |     |     |     |     |     | Hwee Tou | Ng, Siew Mei | Wu, Ted Briscoe, | Christian |
| --- | --- | --- | --- | --- | --- | -------- | ------------ | ---------------- | --------- |
Hadiwinoto,RaymondHendySusanto,andChristo-
ThisresearchisfundedbythePhilippineDepart- pher Bryant. 2014. The conll-2014 shared task on
|     |     |     |     |     |     | grammaticalerrorcorrection. |     | InProceedingsofthe |     |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | ------------------ | --- |
mentofScienceandTechnologythroughits2021
Junior Level Science Scholarships MERIT pro- Eighteenth Conference on Computational Natural
|     |     |     |     |     |     | LanguageLearning: |     | SharedTask,pages1–14. |     |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --------------------- | --- |
gram.
ManolitoOctaviano,MatthewPhillipGo,AllanBorra,
|            |     |     |     |     |     | andNathanielOco.2016.    |     | Acorpus-basedanalysis   |     |
| ---------- | --- | --- | --- | --- | --- | ------------------------ | --- | ----------------------- | --- |
| References |     |     |     |     |     | offilipinowritingerrors. |     | In2016InternationalCon- |     |
ferenceonAsianLanguageProcessing(IALP),pages
| ShamilChollampattandHweeTouNg.2018. |     |     |     | Amulti- |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
95–98.
layerconvolutionalencoder-decoderneuralnetwork
|                 |     |                   |     |                |     | Kostiantyn | Omelianchuk, | Vitaliy Atrasevych, | Artem |
| --------------- | --- | ----------------- | --- | -------------- | --- | ---------- | ------------ | ------------------- | ----- |
| for grammatical |     | error correction. |     | In Proceedings |     |            |              |                     |       |
oftheThirty-SecondAAAIConferenceonArtificial Chernodub, and Oleksandr Skurzhanskyi. 2020.
Intelligence.AssociationforComputationalLinguis- GECToR – grammatical error correction: Tag, not
| tics. |     |     |     |     |     | rewrite. | In Proceedings | of the Fifteenth | Workshop |
| ----- | --- | --- | --- | --- | --- | -------- | -------------- | ---------------- | -------- |
onInnovativeUseofNLPforBuildingEducational
Applications,pages163–170,Seattle,WA,USA→
JanChristianBlaiseCruzandCharibethCheng.2019.
Evaluatinglanguagemodelfinetuningtechniquesfor Online.AssociationforComputationalLinguistics.
low-resourcelanguages.
AimanSolyman,WangZhenyu,TaoQian,ArafatAb-
JanChristianBlaiseCruzandCharibethCheng.2021. dulgaderMohammedElhag,MuhammadToseef,and
Improvinglarge-scalelanguagemodelsandresources ZeinabAleibeid.2021. Syntheticdatawithneural
forfilipino. arXivpreprintarXiv:2111.06053. machinetranslationforautomaticcorrectioninarabic
|                         |          |     |                          |      |     | grammar. | EgyptianInformaticsJournal,22(3):303– |     |     |
| ----------------------- | -------- | --- | ------------------------ | ---- | --- | -------- | ------------------------------------- | --- | --- |
| Jacob Devlin,           | Ming-Wei |     | Chang, Kenton            | Lee, | and | 315.     |                                       |     |     |
| KristinaToutanova.2018. |          |     | Bert: Pre-trainingofdeep |      |     |          |                                       |     |     |
bidirectionaltransformersforlanguageunderstand-
ing. Proceedingsofthe2019ConferenceoftheNorth
AmericanChapteroftheAssociationforComputa-
| tionalLinguistics: |     | HumanLanguageTechnologies, |     |     |     |     |     |     |     |
| ------------------ | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
1:4171–4186.
| MuhammadAliGhufronandFathiaRosyida.2018. |     |     |     |     | The |     |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
roleofgrammarlyinassessingenglishasaforeign
| language(efl)writing.      |            | LinguaCultura.            |                   |       |        |     |     |     |     |
| -------------------------- | ---------- | ------------------------- | ----------------- | ----- | ------ | --- | --- | --- | --- |
| Matthew                    | Philip Go, | Nicco                     | Nocon, and        | Allan | Borra. |     |     |     |     |
| 2017.                      | Gramatika: | Agrammarcheckerforthelow- |                   |       |        |     |     |     |     |
| resourcedfilipinolanguage. |            |                           | InTENCON2017-2017 |       |        |     |     |     |     |
IEEERegion10Conference.
| MatthewPhillipGoandAllanBorra.2016. |     |     |     | Developing |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
anunsupervisedgrammarcheckerforFilipinousing
| hybridn-gramsasgrammarrules. |     |     | pages105–113. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
RomanGrundkiewicz,MarcinJunczys-Dowmunt,and
| KennethHeafield.2019. |         |      | Neuralgrammaticalerror |              |     |     |     |     |     |
| --------------------- | ------- | ---- | ---------------------- | ------------ | --- | --- | --- | --- | --- |
| correction            | systems | with | unsupervised           | pre-training |     |     |     |     |     |
InProceedingsoftheFourteenth
onsyntheticdata.
| Workshop | on Innovative |     | Use of NLP | for Building |     |     |     |     |     |
| -------- | ------------- | --- | ---------- | ------------ | --- | --- | --- | --- | --- |
EducationalApplications,pages252–263.
| Kalpana     | Jayavalan | and Abu | Bakar Razali. | 2018.      | Ef- |     |     |     |     |
| ----------- | --------- | ------- | ------------- | ---------- | --- | --- | --- | --- | --- |
| fectiveness | of online | grammar | checker       | to improve |     |     |     |     |     |
secondarystudents’englishnarrativeessaywriting.
InternationalResearchJournalofEducationandSci-
ences(IRJES).
| Diederik | P. Kingma | and Jimmy | Ba. | 2015. Adam: | A   |     |     |     |     |
| -------- | --------- | --------- | --- | ----------- | --- | --- | --- | --- | --- |
methodforstochasticoptimization.
| Komisyon  | sa Wikang | Filipino.   | 2013. | Ortograpiyang |     |     |     |     |     |
| --------- | --------- | ----------- | ----- | ------------- | --- | --- | --- | --- | --- |
| Pambansa. | Accessed: | 2022/10/17. |       |               |     |     |     |     |     |
29