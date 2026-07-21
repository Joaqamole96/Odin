---
conversion_metadata:
  converted_at: "2026-07-21T06:04:54Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Eigenschink et al.pdf"
  source_pdf_sha256: "b8cd694f1b038fd229b3f68adb9eb411db54950a15dfa40237b31be8da71fa7c"
  page_count: 17
  markdown_char_count: 117206
---

Received12March2023,accepted1May2023,dateofpublication10May2023,dateofcurrentversion18May2023.
DigitalObjectIdentifier10.1109/ACCESS.2023.3275134
Deep Generative Models for Synthetic
Data: A Survey
PETEREIGENSCHINK 1,THOMASREUTTERER 1,STEFANVAMOSI1,RALFVAMOSI1,2,
CHANGSUN 3,ANDKLAUDIUSKALCHER4
1DepartmentofMarketing,ViennaUniversityofEconomicsandBusiness,1020Vienna,Austria
2HighPerformanceComputing,ViennaUniversityofTechnology,1040Vienna,Austria
3InstituteofDataScience,MaastrichtUniversity,6200MDMaastricht,TheNetherlands
4MostlyAIGmbH,1030Vienna,Austria
Correspondingauthor:ThomasReutterer(thomas.reutterer@wu.ac.at)
Thisworkwassupportedbythe‘‘InformationandCommunicationTechnology(ICT)oftheFuture’’FundingProgrammeoftheAustrian
FederalMinistryforClimateAction,Environment,Energy,Mobility,InnovationandTechnology.
ABSTRACT A growing interest in synthetic data has stimulated the development and advancement of a
large variety of deep generative models for a wide range of applications. However, as this research has
progressed, its streams have become more specialized and disconnected from one another. This is why
models for synthesizing text data for natural language processing cannot readily be compared to models
for synthesizing health records anymore. To mitigate this isolation, we propose a data-driven evaluation
frameworkforgenerativemodelsforsyntheticsequentialdata,animportantandchallengingsub-categoryof
syntheticdata,basedonfivehigh-levelcriteria:representativeness,novelty,realism,diversityandcoherence
ofasyntheticdata-setrelativetotheoriginaldata-setregardlessofthemodels’internalstructures.Thecriteria
reflectrequirementsdifferentdomainsimposeonsyntheticdataandallowmodeluserstoassessthequality
ofsyntheticdataacrossmodels.Inacriticalreviewofgenerativemodelsforsequentialdata,weexamine
andcomparetheimportanceofeachperformancecriterioninnumerousdomains.Wefindthatrealismand
coherencearemoreimportantforsyntheticdatanaturallanguage,speechandaudioprocessingtasks.Atthe
same time, novelty and representativeness are more important for healthcare and mobility data. We also
findthatmeasurementofrepresentativenessisoftenaccomplishedusingstatisticalmetrics,realismbyusing
humanjudgement,andnoveltyusingprivacytests.
INDEX TERMS Artificial intelligence, big data, deep learning, generative models, neural networks,
syntheticdata,privacy.
I. INTRODUCTION correlated,high-dimensionaldataandgeneratesyntheticdata
In recent years, the adoption of deep generative models for formanyuse-cases.Amongothers,applicationsofsynthetic
synthetic data has spread to various domains. Such models dataapproachesboostedprogressindataaugmentation[32],
can generate impressive high-quality synthetic images [96], imputation of missing data [19], fairness in biased data-
text [54], and music [12] as well as sensory data [61], sets [87], and sharing of privacy-sensitive data-sets [91].
electronic health records [6], mobility trajectories [53], and Today, deep generative data synthesis is a large and mature
financial time-series [85]. This significant progress was field that involves many streams of research across a wide
made possible by a facilitated accessibility of vast amounts rangeofdomains.Anoverviewisprovidedbyafewreview
of data and computing technologies capable of handling articles on deep generative data synthesis, for example,
the data, both emerging from the continuing rise of ‘‘big in molecular science [50], graph data [39], engineering
data’’ and advances in deep learning. Models based on design [71], in finance [3], and in the industrial Internet of
deep learning can handle large amounts of complex, highly Thingsarea[21].
While the field has advanced in big leaps, research in
The associate editor coordinating the review of this manuscript and the various (sub-)domains also tend to drift apart. This is
approvingitforpublicationwasChi-YuanChen . particularly the case for domains that deal with processing
ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
47304 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME11,2023

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
FIGURE1. Illustrationoftheheterogeneityofsequentialdatabasedon
cardinalityanddimensionality.
| of sequential | data, | such | as  | geo-locations | [75], | shopping |     |     |     |     |     |
| ------------- | ----- | ---- | --- | ------------- | ----- | -------- | --- | --- | --- | --- | --- |
paths[47],text[54],videostreaming[46],[78],music[12],
| [95], clickstreams |              | [15], | internet         | browsing | behavior |     | [28],  |     |     |     |     |
| ------------------ | ------------ | ----- | ---------------- | -------- | -------- | --- | ------ | --- | --- | --- | --- |
| financial          | transactions |       | [60], electronic | health   | records  |     | [6] or |     |     |     |     |
watertreatment.Thesedatastemfromdynamicphenomena
| which are | at the | heart | of many | fields of | research, | but | they |     |     |     |     |
| --------- | ------ | ----- | ------- | --------- | --------- | --- | ---- | --- | --- | --- | --- |
posesignificantchallengesformodelersandanalysts.While FIGURE2. High-levelstructureofthearticle.
| different | types | of sequential |     | data share | underlying |     | serial |     |     |     |     |
| --------- | ----- | ------------- | --- | ---------- | ---------- | --- | ------ | --- | --- | --- | --- |
correlationalstructures,theyarealsoheterogeneousinterms [35], [64], [81]. Furthermore, in addition to the above
of the dimensionality and cardinality of steps in a sequence mentioneddomain-specificreviewsonsyntheticdata,anum-
|             |     |           |         |                 |     |            |     | ber of review | articles have | focused | on specific model |
| ----------- | --- | --------- | ------- | --------------- | --- | ---------- | --- | ------------- | ------------- | ------- | ----------------- |
| (see Figure | 1). | And thus, | indeed, | it is difficult |     | to compare |     |               |               |         |                   |
models applied to problems in natural language processing architectures, such as generative adversarial networks [44],
(NLP) with models for the generation of synthetic health normalizingflows[52].However,thescopeofthosearticles
records. Still, some domains share common characteristics, is narrow. They address specific model architectures or
and models applied in one field can be applied in others. domains and disregard literature in other domains. The
Considertherecentsuccessofso-calledtransformermodels present article contributes to filling the gap between such
introduced in natural language generation (NLG) [14], [70] broadmethodologicalandnarrowfield-levelreviewsofdeep
andnowbeingappliedinotherdomainstogeneratesynthetic generativemodelsforsyntheticdatabyproposingadomain-
time-series data [45]. Because model transfer into other and model-agnostic framework to assess deep generative
fieldsisnotalwaysstraightforward,newinsightscanremain modelsforsyntheticsequentialdata.
isolatedtospecificdomainsandfailtodisseminate.Thetwo The remainder of the article is organized as summarized
most common barriers are (i) heterogeneity of the data and in Figure 2. Section II introduces the high-level evaluation
(ii) conflicting requirements for synthetic data in different framework for generative models. Then, in section III,
use-cases.Becauseresearchinonedomaincanbenefitfrom weassessapplicationsofsyntheticdataindifferentdomains,
insightsfromotherdomains,acommonbasisfordiscussing compare strengths and weaknesses of the used models and
generativemodelsandguidingresearchisneeded,especially their architectures and critically analyze them according
indomainsinwhichresearchtodateissparse. to the proposed evaluation framework. Finally, section IV
To facilitate this discussion, we propose a framework concludes the paper and provides directions for future
| for deep       | generative | models    | designed      | to       | generate         | synthetic |     | research.                           |     |     |     |
| -------------- | ---------- | --------- | ------------- | -------- | ---------------- | --------- | --- | ----------------------------------- | --- | --- | --- |
| sequential     | data       | based     | on high-level |          | evaluation       | criteria. |     |                                     |     |     |     |
| This framework |            | addresses | the           | barriers | of heterogeneity |           | in  |                                     |     |     |     |
|                |            |           |               |          |                  |           |     | II. EVALUATIONOFGENERATIVEMODELSFOR |     |     |     |
the data and the data requirements via abstraction and SYNTHETICDATA
allows researchers to put generative models into broader Metrics to evaluate the performance of deep generative
contexts.Wepresentacriticalreviewofpublicationsondeep modelsareasdiverseasthemodels’objectivesandspecific
generativemodelsinthecontextofsyntheticsequentialdata datastructuresinvolved.General-purposemetrics,suchasthe
andapplytheproposedframeworktothosemodels. commonlyusednegativelog-likelihood(NLL),averagelog-
The present article complements prior reviews in related likelihood (ALL) and maximum mean discrepancy (MMD)
fields,suchasbroadreviewsondeeplearningingeneral[67] arerareandhavelimitationsoftheirown[79].Othermetrics
and reviews of architectures of deep generative models are specific particular model architectures. References [9]
VOLUME11,2023 47305

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
and [10], for example, give a thorough overview of metrics colors and eye distances, and those distributions and the
commonly used to evaluate generative adversarial networks dependencies between the distributions (e.g., gray hair and
(GANs). Some metrics are domain-specific, such as the theamountofwrinklesonaface)intheoriginalandsynthetic
classifier-based inception score (IS) for synthetic images datashouldmatch.Dependingonthetypeofdata,therecan
proposed by [74]. [79] reviews metrics used to evaluate beamultitudeofwaystomeasureandquantifythesimilarity
generative models in the visual domain, and [39] for graph ofthedistributions.
data. These metrics effectively measure progress in specific Representativeness of synthetic data matters because
domains and compare models of a specific type, such as statisticalanalysesandmachinelearningmethodsperformed
GANs;usingthemtocomparedifferentmodelsanddomains onsyntheticdatashouldresultinthesamestatisticalfindings
can be challenging. Even when considering only sequential asanalysisoftheoriginaldata.Alackofrepresentativeness
data, heterogeneity is quickly apparent. The cardinality and despite all other criteria being fulfilled, indicates that the
dimensionalityofthedataillustratethisheterogeneity,being syntheticdataprovideagoodrepresentationonlyofabiased
augmented only further by the lengths of sequences. For subspaceoftheactualdatadistributionandmisspotentially
example,textisone-dimensionalanddiscretesinceitismade criticalinformation.
upofsinglewordsinadiscretevocabulary.Videodata,onthe Inmanycases,representativenessisevaluatedbystatistical
otherhand,iscontinuousandhigh-dimensional.Ateachstep, measures.CommonmethodsareALL,MMDandKullback-
there is a whole image that consists of many pixels, each Leibler divergence (KLD), which compare the probability
is described by real numbers between 0 and 255. Figure 1 distribution of the original data to the approximation of
illustrates the heterogeneity in the landscape of sequential the distribution by the generative model. Recently, repre-
data by plotting the cardinality and dimensionality the data sentativeness has also been evaluated by comparing the
forseveralexamplesofsequentialdatarelativetoeachother. performanceofclassificationmodelsappliedtotheoriginal
To tackle the numerous challenges associated with het- andthesyntheticdata(see[17]foranexampleinhealthcare).
erogeneous data and applications, we propose five high-
level abstract criteria for evaluation of generative models:
representativeness, novelty, realism, diversity, and coher-
ence. The criteria are designed to compare the original data 2) NOVELTY
to the synthetically generated sample and can be applied Evaluating the novelty of data from a generative model
to any generative model for synthetic data (see [66] for a compares the original and synthetic data at an individual
recent example of a holdout-based framework for empirical level. Novelty is sometimes overlooked in explicit quality
assessment). They reflect requirements that are imposed on evaluations, but the value of synthetic data without novelty
syntheticdatainspecificuse-cases. istypicallyquitelimited.Thegoalofusingdeepgenerative
Becausethecriteriacanbeimposedonnumeroustypesof models usually is creation of entirely novel data-points.
sequential data, obtaining high scores on all five will rarely Noveltymeansthatthesyntheticdata-pointsareentirelynew
bethegoal.Borjireviewsqualitativeandquantitativemetrics observationsofthelatentdistributionoftheoriginaldataand
for generative models in [9] and [10], but there is no one- shouldnotcloselyresembleanyoriginaldata-points.
to-one mapping between those criteria and ours. The two Models that generate only novel data-points do not allow
approachessharesomeaspects,reflectedinwhat[9]defined any individual-level information from the training data
asthedesiderataofevaluationmeasures. to leak into the synthetic data. Thus, novelty is tightly
Our proposed criteria are abstract in nature but capture linked to privacy, and a high novelty score indicates that
different concrete metrics depending on the use-case. Fur- the ‘‘inspiration’’ behind the synthetic data-points is not
thermore, some of our criteria conflict with each other. identifiableattheindividuallevel.Thesyntheticdatarecords
For example, we expect to see trade-offs between high couldjustaswellhavebeenaholdoutsubsetoftheoriginal
representativeness of the synthetic data-set and it’s novelty. data.Theoppositeofhighnoveltyisamodelthatmemorizes
Figure 3 illustrates synthetic data that have high and low and exactly recreates the training data. Such synthetic data
scoresoneachcriterionrelativetoagivendata-set. would fulfill the other four criteria (since a copy of the
originaltrainingdataisobviouslyindistinguishableinmany
respectsfromthatdata).
A. EVALUATIONCRITERIA In some cases, such as in NLP, novelty of the synthetic
1) REPRESENTATIVENESS data is irrelevant. In other cases, however, such as creative
The representativeness of a generative model for synthetic domains (e.g., music composition), the goal is to generate
data describes its ability to capture population-level prop- new creative content. For example, [23] used the average
erties of the original data. Ideally, generative models distill Euclideandistanceofasyntheticdata-pointfromitsnearest
abstractstructuresfromasetoftrainingdata.Consequently, neighbor in the original data-set to measure the novelty of
the population-level properties of the synthetic and original syntheticmusic(seeSectionIII-Bfordetails).Inothercases,
data should be the same. For example, a data-set of face such as healthcare, privacy is more important than novelty.
images is likely to have a certain distribution of hair Thegenerativemodelsusedtoproduceprivatesyntheticdata
47306 VOLUME11,2023

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
FIGURE3. Illustrationofsyntheticdata-setsthatscorehigh(top)andlow(bottom)ontheproposedcriteriawhen
comparedtotheoriginaldata-setontheleft.Coherenceonlycapturestheinternalstructureofthedataandisillustrated
ontheright.
mustnotleakanysensitiveinformation(seeSectionIII-Dfor as some early versions of GANs, obviously lack diversity.
moredetails). For instance, generators sometimes create a single image
|     |     |     |     |     |     |     | that the          | discriminator | cannot | distinguish |     | from             | an original |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------- | ------ | ----------- | --- | ---------------- | ----------- |
|     |     |     |     |     |     |     | image. Generating |               | only   | that image  | is  | a local optimum, | and         |
3) REALISM
When considering an individual synthetic data-point gener- theresultingeffectiscalledmodecollapse.
|           |                  |       |     |          |                 |     | Many | publications | have | not | addressed | the diversity | of  |
| --------- | ---------------- | ----- | --- | -------- | --------------- | --- | ---- | ------------ | ---- | --- | --------- | ------------- | --- |
| ated by a | highly realistic | model | on  | its own, | it is difficult | to  |      |              |      |     |           |               |     |
know whether it is synthetic or original. Realism is similar the generative models’ synthetic data. In most cases, it is
torepresentativenessofthedata,butattheindividualsubject important that models achieve at least some diversity, and
|          |                    |     |       |         |            |        | some models | can | generate | only | a small | number | of different |
| -------- | ------------------ | --- | ----- | ------- | ---------- | ------ | ----------- | --- | -------- | ---- | ------- | ------ | ------------ |
| level. A | synthetic data-set | can | match | all the | statistics | of the |             |     |          |      |         |        |              |
original data and still be unrealistic when individual data- samples(e.g.,theaforementionedGANwithmodecollapse).
Thereareseveralwaystomeasurethediversityofamodel.
| points share | characteristics | that | make | them | easily | identifi- |     |     |     |     |     |     |     |
| ------------ | --------------- | ---- | ---- | ---- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
able as synthetic. Consider a representative but unrealistic Donahue et al. [23] used the average Euclidean distance of
exampleobtainedusingaGANtrainedonrandomcatimages synthetic data-points to their respective nearest neighbors
|     |     |     |     |     |     |     | to evaluate | the diversity |     | of their | model | (see Section | III-B). |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | -------- | ----- | ------------ | ------- |
fromtheinternet.Syntheticcatimagescancontaincaptions
reminiscent of online memes that look plausible from a Othershaveusedmetricsbasedonclassifiers.Forexample,
tomeasurethediversityoftheirvideo-generationmodels,the
distancebutactuallyconsistsolelyofabstractsymbolshaving
shapessimilartoletters. authorsof[73]and[80]usedtheIS[74](seeSectionIII-C).
Realism has been addressed in many publications in a Inothercasesdiversityhasbeencapturedonlybysubjective
qualitativeevaluationsbyhumans.
| variety of | ways. The        | most common |         | method  | is judgement |       |     |     |     |     |     |     |     |
| ---------- | ---------------- | ----------- | ------- | ------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
| of realism | of the synthetic |             | data by | humans, | either       | qual- |     |     |     |     |     |     |     |
itatively (e.g. [59], [62]) or using empirical evaluations 5) COHERENCE
| (e.g. [7], | [63], [83]). | Evaluation |     | studies | present | indi- |     |     |     |     |     |     |     |
| ---------- | ------------ | ---------- | --- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Unlikethefirstforcriteria,whicharebasedonthestructure
| viduals | with the original |     | data-point | and | the | synthetic |                  |      |     |               |     |               |        |
| ------- | ----------------- | --- | ---------- | --- | --- | --------- | ---------------- | ---- | --- | ------------- | --- | ------------- | ------ |
|         |                   |     |            |     |     |           | of the synthetic | data | at  | an individual |     | or population | level, |
data-point and ask them to choose which is the most. coherence captures the internal structure of single synthetic
| In some | publications, | participants |     | in  | the evaluation |     |              |              |     |       |              |           |     |
| ------- | ------------- | ------------ | --- | --- | -------------- | --- | ------------ | ------------ | --- | ----- | ------------ | --------- | --- |
|         |               |              |     |     |                |     | data-points, | specifically |     | their | consistency. | Coherence | is  |
studies were restricted to experts (e.g., medical experts particularlyrelevantforsequentialdata,thatreflectsequential
in [7] and [20] and music experts [11], [63]). In some orders of events and for data such as images. Coherence
| cases, realism | is quantitatively |     | evaluated |     | using | objective |              |        |     |              |     |                  |      |
| -------------- | ----------------- | --- | --------- | --- | ----- | --------- | ------------ | ------ | --- | ------------ | --- | ---------------- | ---- |
|                |                   |     |           |     |       |           | requirements | depend | on  | the use-case |     | and the original | data |
measures. These evaluations are usually domain-specific and, thus, can differ in terms of coarseness. Music, for
| and use | metrics such | as IS [73], | [80] | and | the evaluation | of  |     |     |     |     |     |     |     |
| ------- | ------------ | ----------- | ---- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
example,shouldsoundsmoothandnaturalnote-by-noteand
syntheticmusicagainsttheoreticalmusicrules[48]. measure-by-measure, but also should stay within a certain
genreoverall.Inimageswhenmultipleobjectscastshadows
4) DIVERSITY fromasinglelightsource,theshadowsmustbecoherentin
While representativeness, novelty and realism capture simi- terms of the direction in which they point and their length.
laritiesbetweentheoriginalandthesyntheticdata,diversity While some incoherence in the data can lead to greater
measures similarities between each synthetic data-point novelty or diversity, too much results in unrealistic data.
and the whole synthetic data-set at the individual level. A music sample that frequently changes its genres would
Therefore, models that score well on diversity generate certainlysoundcreativebutwouldalsosoundunrealistic.
unique data-points even when data-sets are large. Models Some studies have measured the coherence of synthetic
thatgeneratethesameindividualpointsoverandover,such data implicitly when evaluating its realism. In the study
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     | 47307 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
TABLE1. Excerptsofstudiesofgenerativemodelsfornaturallanguage
processingandmetricsusedforevaluation.
|     |     |     |     |     | has made | significant | progress | in  | accomplishing | these | tasks. |
| --- | --- | --- | --- | --- | -------- | ----------- | -------- | --- | ------------- | ----- | ------ |
FIGURE4. Popularityofvariousarchitecturalelementsindeeplearning
|     |     |     |     |     | Today, highly | capable |     | language | models | can generate | texts |
| --- | --- | --- | --- | --- | ------------- | ------- | --- | -------- | ------ | ------------ | ----- |
modelsusedtogeneratesyntheticsequentialdata.Thetopgraphshows
thepercentageofeacharchitecturefoundtobethebasisformodels almostindistinguishablefromhuman-generatedtext.
usedintheallreviewedstudies.Theheatmapinthebottomfigureshows
|     |     |     |     |     | Language | data-sets |     | are comprised | of  | text, which | can |
| --- | --- | --- | --- | --- | -------- | --------- | --- | ------------- | --- | ----------- | --- |
theprevalenceinpercentofeacharchitecturalelementinfivedomains.
ThedataunderlyingbothgraphicsisincludedintheWebAppendix. come in many different flavors - news articles, product
|     |     |     |     |     | reviews, | medical | diagnoses, | and | music lyrics. | However, | all |
| --- | --- | --- | --- | --- | -------- | ------- | ---------- | --- | ------------- | -------- | --- |
conducted by Bretran et al. [11] experts evaluated the text can be represented as a combination of tokens from a
naturalnessoftransitionsinsyntheticmusic.Inmanycases, discrete vocabulary. The tokens are the most basic compo-
however,domain-specificobjectivemetricshavebeenusedto nents of text, commonly single words complemented with
judgecoherence.In[80]coherencewascomputedusingthe
punctuation.
averagecontentdistancebetweenframesinsyntheticvideos Sentences, paragraphs, and longer texts are then merely
(seeSectionIII-C). sequencesofsuchtokens.However,thesequencesmustobey
|     |     |     |     |     | certain grammatical, |     | semantic, |     | and logical | rules. Moreover, |     |
| --- | --- | --- | --- | --- | -------------------- | --- | --------- | --- | ----------- | ---------------- | --- |
III. ASSESSMENTOFAPPLICATIONS since sentences are not just loosely strung together, later
| We next review | applications | of  | deep generative | models to |           |             |     |          |                        |     |     |
| -------------- | ------------ | --- | --------------- | --------- | --------- | ----------- | --- | -------- | ---------------------- | --- | --- |
|                |              |     |                 |           | sentences | and wordsin |     | the text | can be highlydependent |     | on  |
generate synthetic sequential data in a variety of domains. wordsthatappearedmultiplesentencesbefore.Forexample,
We critically analyze the contributions to this fast-growing acharacterinashortstorythatdisappearsinthebeginning,
| literature, evaluate | them | using | our proposed | criteria, and |              |            |     |        |           |                |     |
| -------------------- | ---- | ----- | ------------ | ------------- | ------------ | ---------- | --- | ------ | --------- | -------------- | --- |
|                      |      |       |              |               | can reappear | paragraphs |     | later. | The rules | and contextual |     |
demonstrate that the criteria individually are not equally dependenciesofatextposesignificantchallengestolanguage
relevantinalldomainsandarenotmeasuredthesameway. models and to the generation of synthetic text. A model
Each subsection discusses the applications in their focal must be capable of capturing the proper setting of various
domain and summarizes a few representative contributions linguistic features such as syntax, semantics, pragmatics,
| in terms of | the proposed | assessment | criteria. | See Tables 1 |                 |     |            |     |           |          |         |
| ----------- | ------------ | ---------- | --------- | ------------ | --------------- | --- | ---------- | --- | --------- | -------- | ------- |
|             |              |            |           |              | and morphology. |     | Otherwise, | the | resulting | text can | quickly |
to5foroverviewsofrepresentativecontributionsinparticular becomeincoherentorunrealistic.
domains. Additionally, we analyze the architectures of A fascinating language model is provided by [40]. It was
the models used in the selected publications. Figure 4 inspired by how humans create complex texts, which rarely
summarizes the prevalence of architectural elements used arise from scratch in a single pass. Instead, humans rather
| in the reviewed | articles in | different | domains. | An excellent |                |        |     |            |                       |     |      |
| --------------- | ----------- | --------- | -------- | ------------ | -------------- | ------ | --- | ---------- | --------------------- | --- | ---- |
|                 |             |           |          |              | create initial | drafts | and | revise the | drafts incrementally. |     | [40] |
overview of deep neural network architectures is provided adopted this idea in their neural editor model by sampling
by[36]. a prototype sentence from the training corpus, combining
|     |     |     |     |     | it with a | random | parameter | for | editing | the sentence, | and |
| --- | --- | --- | --- | --- | --------- | ------ | --------- | --- | ------- | ------------- | --- |
A. NATURALLANGUAGEPROCESSING generating a modified, new sentence. Their edit parameter
NLP is a broad field devoted to computers interacting can lead to changes such as altered wording, shorter or
with human language. Common tasks in NLP include longer sentences, and change from active to passive voice.
language modeling, text translation [77], human-machine Architecturally, the model is based on a VAE (variational
dialoggeneration,andnaturallanguagegeneration[26],[33]. autoencoder; [51], [72]) with an attention-based LSTM
Thankstothewidespreadadoptionofmachinelearningand (longshort-termmemory;[34],[43])encoderandanLSTM
deepneuralnetworksinrecentyears,theresearchcommunity decoder.Theprototypesentenceandtheeditparametersare
| 47308 |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
randomlysampledandthenusedtotransformthesentencein oftheoutput.TheBLEUscorewasoriginallydevelopedfor
asequence-to-sequencefashion. in-text translation and has proven to be a good metric for
A metric commonly used to evaluate the quality of measuringtranslationqualitythatcorrelateswellwithhuman
languagemodelsistheperplexity[49],whichcaptureshow evaluations. It measures similarities between the generated
‘‘surprised’’ a language model is to see the words in the text and a set of references by comparing their n-grams: n
original training corpus in terms of probabilities it assigns consecutivewords/tokensinatext.Whenthesetofreferences
to each word. Looking at language models as generative, isthewholesyntheticdata-set,theBLEUscoreiscalledself-
perplexitymeasurestherepresentativenessofthegenerative BLEU.
model. Reference [40] evaluated their neural editor using The average BLEU score of the ml-VAE model obtained
a data-set of restaurant reviews from Yelp and a more- bycomparinggeneratedtexttothetrainingcorpusindicated
generaltextdata-set.Theyfoundthatthesynthetictextswere thatrepresentativenessimprovedrelativetothebaseline.The
representative when measured by perplexity in both cases. authorsalsoreportedanacceptablediversityscore.Diversity
Thoughtheywereabletogeneratenovelsentencesthatwere was especially important to them because VAEs used for
significantly different from the prototype sentences, each NLG often suffer from mode collapse. They evaluated
synthetic sentence still originated from a single prototype diversitybycalculatingself-BLEUscores,thepercentageof
sentenceandthuswassomewhatclosetotheprototype. uniquen-grams,andthe2-gramentropyofasetofsynthetic
Theeditparametercanbeusedtoperformsimilareditson texts. They further evaluated the coherence and realism of
multiple sentences or to smoothly vary the degree to which the synthetic text by asking individuals to compare text
editing is performed on a single sentence. Reference [40] generated by the baseline model to the ml-VAE synthetic
used these properties to generate a variety of sentences, text and choose the one that seemed most ‘‘real’’ to them.
qualitatively suggesting that the generation of diverse data- Individualsratedthetexts’fluency,grammar,andconsistency
sets is possible. Individuals deemed the synthetic sentences to measure their coherence. These human evaluations also
realistic and coherent according to their ratings of overall showedthat,intermsofrealismandcoherence,theml-VAE
quality,grammaticality,andplausibility. yieldedresultsthatweresuperiortotheresultsofthebaseline
Though the neural editor effectively generates synthetic model and acceptable when compared to human-generated
sentences,creatinglongertextsamplescomposedofseveral text.
coherent sentences that are non-repetitive, grammatically Likelihood-basedmodelssuchasVAEshavetheircritics,
correct,andnon-contradictoryremainschallenging.Models who suggest that the models are well suited to optimizing
capableofthattaskrequireagreatercapacitytocapturethe perplexity and representativeness but lack the ability to
long-term dependencies in such texts. Shen et al. proposed generate realistic, coherent high-quality samples. In [30],
such a model in [76] and, given the inherent hierarchical Fedus et al. attempted to generate higher-quality sam-
paragraphstructureoflongertexts,theychoseahierarchical ples using a GAN-based model that incorporated LSTM
VAEarchitecture.Theencodernetworkconsistsofonelow- encoder-decodernetworksinthegeneratoranddiscriminator.
level CNN (convolutional neural network) that maps each To improve overall training, they masked the sentences by
sentence to a latent variable and one high-level CNN that blanking words and asking the generator to predict the
mapsallthelatentvariablesforeachsentenceintoonelatent missingwordsbasedontherestofthesentence.Inthatcase,
variable for the entire text input. On the decoding side, two the networks knew the entire sentence context; most other
hierarchical LSTM networks operate the other way around modelsconditionawordsolelyontheprecedingwordsinthe
at the sentence and on word level. The decoder obtains a sentence.TheyfoundthattheirhybridGANmodelimproved
latent variable for a text and transforms it via the sentence- perplexityandthusrepresentativenessrelativetoalikelihood-
levelLSTMintolatentsentencevariables.Thesentence-level based baseline model. Still, they claim that low perplexity
latent variables are then passed down to the word-level alone does not indicate high-quality synthetic text, their
LSTM,whichgeneratesthewordsforthesyntheticsentences. primaryfocus.Theirhumanevaluationsalsoshowedthatthe
Themodelcanoutputlongersyntheticparagraphsbyputting hybridGANmodelproducedmorerealisticsamplesthanthe
all the words together into sentences and the sentences into baseline model in most cases. Distinguishing between the
paragraphs. Passing the latent variables down the LSTM syntheticandhuman-generatedtextsseemsrelativelyeasyfor
hierarchy allows the decoder to capture relatively coarse the participants. Since mode collapse is a common issue in
characteristics of text and sentences, such as the topic and GANs, the authors also took a narrow look at the diversity
sentiment. of the synthetic results. They evaluated the percentages
Shenetal.[76]evaluatedtheirmodelusingYelpreviews of unique 2-, 3-, and 4-grams. They found some mode
and abstracts from arXiv papers and found that their collapse, indicating that the text generated by their model
multilevel-VAE (ml-VAE) model improved the representa- lackeddiversityrelativetothetextgeneratedbythebaseline
tiveness of the output relative to a flat VAE model (the model.Inaddition,thesyntheticsentencessometimeslacked
baseline). They evaluated representativeness by measuring coherence because they lost the global context. However,
the perplexity of the language model and calculating the the authors expected to be able to improve coherence by
corpus-level bilingual evaluation understudy (BLEU) score increasingthecapacityofthemodel.
VOLUME11,2023 47309

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
TABLE2. Excerptofstudiesofsyntheticspeechandaudiodataand of vast quantities of audio data, researchers began to apply
metricsusedtoevaluatetheoutput. the techniques to audio-synthesis. The resulting models
|     |     |     |     | learned | either from raw | audio signals | or from | intermediary |     |
| --- | --- | --- | --- | ------- | --------------- | ------------- | ------- | ------------ | --- |
representationssuchasmusicalscoresandlinguisticspeech
parameters.Themodelscangrasptheunderlyingstructureof
thedatatocreaterealistic-soundingsyntheticaudiodata.
Themostgeneralrepresentationofsoundistheamplitude
|     |     |     |     | of sound | waves over | time sampled | at a constant | rate | (i.e., |
| --- | --- | --- | --- | -------- | ---------- | ------------ | ------------- | ---- | ------ |
rawaudio).Consequently,thesoundsignaliscontinuousand
|     |     |     |     | one-dimensional. | Still, | because | of the high | frequencies | of  |
| --- | --- | --- | --- | ---------------- | ------ | ------- | ----------- | ----------- | --- |
naturalsounds,thesequencesarelongandcomplex.Typical
|     |     |     |     | sampling | rates are at | least 16kHz, | resulting | in signals | with |
| --- | --- | --- | --- | -------- | ------------ | ------------ | --------- | ---------- | ---- |
thousandsofstepspersecond.
|     |     |     |     | Models           | designed to       | work with       | raw audio      | generally          | are     |
| --- | --- | --- | --- | ---------------- | ----------------- | --------------- | -------------- | ------------------ | ------- |
|     |     |     |     | the most         | adaptable.        | Unlike models   | that           | use intermediary   |         |
|     |     |     |     | representations, | their             | results do      | not have to    | go through         | one     |
|     |     |     |     | or more          | conversion        | steps before    | becoming       | audible            | [63].   |
|     |     |     |     | The drawback     | of raw            | audio is        | the need       | for high-capacity  |         |
|     |     |     |     | models           | that can learn    | certain         | rules on their | own                | instead |
|     |     |     |     | of having        | to encode         | the rules       | in specific    | representation.    |         |
|     |     |     |     | To generate      | realistic         | speech, for     | example,       | models have        | to      |
|     |     |     |     | learn how        | intonation        | affects meaning | to             | generate realistic |         |
|     |     |     |     | speech.          | Speech parameters | already         | encode         | intonation         | rules   |
tosomeextent.
NLP is a heavily researched domain that has produced Deep learning models can leverage some aspects of
| a wide | range of applications. | The primary | concern of |            |             |             |                  |     |      |
| ------ | ---------------------- | ----------- | ---------- | ---------- | ----------- | ----------- | ---------------- | --- | ---- |
|        |                        |             |            | audio data | by choosing | appropriate | representations. |     | But, |
most studies of generative models is the generation of as previously mentioned, there are drawbacks. Musical
| representative | and realistic    | synthetic     | texts with realism |         |                        |                  |            |              |     |
| -------------- | ---------------- | ------------- | ------------------ | ------- | ---------------------- | ---------------- | ---------- | ------------ | --- |
|                |                  |               |                    | scores, | for example,           | require multiple | conversion | steps        | to  |
| implicitly     | used as a metric | for coherence | in most cases.     |         |                        |                  |            |              |     |
|                |                  |               |                    | become  | audible. Additionally, | representations  |            | can abstract |     |
Diversity is also investigated in detail when models are away relevant nuances of music and speech. Timing and
pronetomodecollapse.However,noveltyisrarelyaddressed
|     |     |     |     | volume, | for example, | can be | important | when generating |     |
| --- | --- | --- | --- | ------- | ------------ | ------ | --------- | --------------- | --- |
and could be of interest primarily in privacy-sensitive cases synthetic music, but often cannot be represented accurately
suchasmedicalpatients’chiefcomplaints[55].Interestingly,
inmusicalscores.
| for most | of our high-level | evaluation criteria | (Section II) |      |            |           |             |        |       |
| -------- | ----------------- | ------------------- | ------------ | ---- | ---------- | --------- | ----------- | ------ | ----- |
|          |                   |                     |              | When | generating | music and | speech, use | of raw | audio |
some metrics have been established for NLP. NLL, BLEU, signalsingenerativemodelsisintheminority.Applications
andperplexityareoftenusedtomeasurerepresentativeness.
|     |     |     |     | such as | WaveNet [62] | show that | raw audio | models | can |
| --- | --- | --- | --- | ------- | ------------ | --------- | --------- | ------ | --- |
Realism and coherence are mainly evaluated together as succeedinmultipledomainsbyleveragingtheflexibilityof
partsofhumanevaluationstudies,withparticipantschoosing
|     |     |     |     | deep learning | models. | WaveNet | is an autoregressive |     | model |
| --- | --- | --- | --- | ------------- | ------- | ------- | -------------------- | --- | ----- |
betweensyntheticandhuman-generatedtextbasedonvarious
|     |     |     |     | that predicts | one step | of a sequence | at a | time conditioned |     |
| --- | --- | --- | --- | ------------- | -------- | ------------- | ---- | ---------------- | --- |
properties.Finally,toassessthediversityofsyntheticresults, on previous steps. Multiple layers of causal convolutions
| studies | used either self-BLEU | or statistics | such as the |             |           |          |          |           |      |
| ------- | --------------------- | ------------- | ----------- | ----------- | --------- | -------- | -------- | --------- | ---- |
|         |                       |               |             | incorporate | causality | into the | network. | These are | one- |
percentage of unique n-grams. Metrics employed in [30] dimensional convolutions that depend only on present and
and [76] to evaluate diversity stood out, especially when pasttimesteps.Akeyproblemofnetworksinvolvingcausal
comparedtothequalitativediversityevaluationusedin[40].
|     |     |     |     | convolutions | is that,     | when the convolutions |             | depend | on the |
| --- | --- | --- | --- | ------------ | ------------ | --------------------- | ----------- | ------ | ------ |
|     |     |     |     | present      | and previous | time steps,           | the network | has    | to be  |
B. SPEECHANDAUDIOPROCESSING quitedeeptocapturelong-termdependencies.WaveNet[62]
Generation of audio data has a long history. It originated overcomesthisobstaclebydilatingtheconvolutionsineach
in several quite different domains and relied on completely layer.Therefore,insteadofusingtheoutputofthepreceding
different theories. Most notable the generation of synthetic timestepasinput,WaveNetskipsmultipletimesteps.
music and speech. Both ultimately make data audible by TheWaveNet[62]modelhasbeenevaluatedinnumerous
converting it to sound. As different as these origins and the experiments. Most important for this review is the uncondi-
rulesusedtogeneratesyntheticsoundare,botharespecific tionalgenerationofpolyphonicsingle-voicepianomusicand
types of digital audio data that eventually yield the same of speech for a single speaker. WaveNet made a significant
result. leap forward in the ability to generate of synthetic audio
Followingthesuccessofdeepneuralnetworksingenerat- data by adopting deep learning models and still serves as
ingcontentsuchasimages,video,andtextandtheavailability a baseline for evaluation of new models. Reference [62]
| 47310 |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
addressed novelty, realism, and coherence of the sample SpecGANthengeneratessynthetictwo-dimensionalspectro-
output of WaveNet only qualitatively and did not address grams that are inverted back to raw audio to obtain audible
representativeness or diversity. Qualitatively, the synthetic sound.
music was rated as harmonious and aesthetically pleasing. Withasamplingrateof16kHzWaveGANandSpecGAN
Their synthetic speech samples consisted of non-existent generate synthetic audio samples that have a duration of
words that resembled actual words and were spoken with about one second. The models are applied to data-sets with
realisticintonations.Theauthorsarguethatconditioningon similarly short sounds, such as intonations of the numbers
information such as a speaker’s ID for speech and genre zero through nine in speech, short drum and piano sounds,
for music, yields better results. Additionally, because the and bird vocalizations. The authors thoroughly evaluated
input size was limited, WaveNet’s synthetic outputs lacked thetwomodelsusingIS,nearest-neighborcomparisons,and
long-termcoherenceandsyntheticmusicsamplessometimes human judgement. Donahue et al. [23] used the IS, which
changedgenreandvolumefromonesecondtoanother. was originally developed to evaluate of synthetic images,
The structure of raw audio makes generation of long to determine the realism and diversity of their synthetic
coherent audio signals challenging. The signal at one time sounds. To evaluate diversity, they measured the mean
stepcandependonthevaluesofneighboringtimestepsand Euclideandistancebetweenasyntheticsoundanditsnearest
onthevaluesofthousandsofprecedingtimesteps.WaveNet neighbors. Novelty was determined by the mean Euclidean
lacksthislong-termcoherencebutyieldsshortaudiosamples distance between a synthetic sound and nearest neighbors
of good quality. To overcome this limitation, WaveNet in the original data-set. Additionally, study participants
has been incorporated into higher-level architectures evaluated the quality, diversity, and realism of the synthetic
(e.g.,[22],[58]).Dielemanetal.[22]transformedrawaudio vocalizationsofthenumbers.Theauthorsreportbetterresults
signalsintoamore-abstract,higher-levelrepresentationand intermsofnovelty,diversityandrealismthanachievedusing
trainWaveNetontherepresentation. SampleRNN[58]andWaveNet[62].
In their SampleRNN model, Mehri et al. [58] addressed The limitations associated with using raw audio data
theproblemofcoherencebyhierarchicallystackingnetworks in terms of sequence length make use of higher-level
thatoperatedatdifferenttimescales.Thelowestlayerofthe representations of sound such as musical scores and the
SampleRNN is a WaveNet network operating on the raw Musical Instrument Digital Interface (MIDI) standard for
audiosignal.Higherlayersoperateoncoarsertimescalesby music beneficial in some scenarios. Higher-level repre-
collating multiple time steps of the signal into the state of sentations can encode important information but abstract
a recurrent neural network (RNN). As a result, the higher away some aspects of raw audio. Less capacity is needed
layers can capture long-term dependencies and pass that for these models, but the representations cannot be made
informationdownthenetworkhierarchy,allowingWaveNet audible directly. Often, some interpretation is to musi-
toobtainaggregateddependencyinformationfromnumerous cians or to computer programs. Additionally, abstrac-
preceding time steps. The SampleRNN was evaluated on tion reduces sequence length while usually increasing
speech data, human sounds, and music data. The authors dimensionality.
reportedthatitgeneratedmore-representativesyntheticaudio Pianorollsareanexampleofahigher-levelrepresentation
samples than a simple WaveNet, based on the NLL of ofmusic.Theywereinspiredbytherollsusedinautomated
the synthetic samples. Also, participants who evaluated the pianosthattriggeredplayingofanoteforacertainduration.
results of SampleRNN in an empirical study perceived the Similarly, piano roll representations encode whether a note
syntheticoutputmorerealisticthantheoutputofWaveNet. —or multiple notes in polyphonic cases —is played in a
Donahueetal.[23]alsoworkedwithrawaudiobutapplied particular time step of a song. The duration of the time
an interesting approach. They transferred the DCGAN steps is constant for a single piano roll and across a data-
network [69], a model prominently known for its success set. The duration is much longer than in raw audio data
in image synthesis, to audio generation. They created so piano rolls can encode multiple seconds of melodies
two models: WaveGAN for raw audio and SpecGAN using shorter sequences and thus make it easier to capture
for spectrograms of sound data. Both are GAN models intra-sequence dependencies. However, piano rolls slightly
with a convolutional generator and discriminator and a increase dimensionality because each note in a track is
structure similar to DCGAN. However, since as raw audio encoded instead of amplitudes of sound waves. There are
is one-dimensional and images are two-dimensional, the severalotherrepresentationsusedformusic,andtheliterature
convolutions are flattened. Two-dimensional filters sized on deep learning models for generating symbolic music is
5×5 in DCGAN become one-dimensional filters of length extensive[13],[31].
25 in WaveGAN and WaveGAN’s output is a raw audio In [24], Dong et al. described a model designed to gen-
sample of length 16,384 instead of an image of size erate multi-voice polyphonic rock music called MuseGAN
128×128.SpecGAN,ontheotherhand,operatesonthetwo- operating on piano rolls. Multi-voice music consists of
dimensionalspectrogramsofrawaudiodata.Therawaudio multiple tracks for the instruments (e.g., piano, guitar,
samples are first transformed into intensity distributions of and bass). Each track is represented by a piano roll. The
differentfrequenciesateachtimestep,creatingspectrograms. challenge in modelling multi-voice polyphonic piano rolls
VOLUME11,2023 47311

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
is capturing the intra-dependencies of notes in a track TABLE3. Excerptofmodelsforsyntheticvideosandmetricsusedto
| and the | inter-dependencies |     | of  | notes | played | in different | evaluatethem. |     |     |     |
| ------- | ------------------ | --- | --- | ----- | ------ | ------------ | ------------- | --- | --- | --- |
tracks.
| MuseGAN   | [24]       | uses      | the intra- | and    | inter-dependencies |            |     |     |     |     |
| --------- | ---------- | --------- | ---------- | ------ | ------------------ | ---------- | --- | --- | --- | --- |
| of tracks | to compose | synthetic |            | music, | further            | separating |     |     |     |     |
thedependenciesintotime-dependentandtime-independent
| parts. The   | network       | is a    | GAN           | that uses    | a generator  | partly     |     |     |     |     |
| ------------ | ------------- | ------- | ------------- | ------------ | ------------ | ---------- | --- | --- | --- | --- |
| inspired     | by generative | video   | models        | [73],        | [80],        | [83] (see  |     |     |     |     |
| Section      | III-C for     | details | on these      | models).     | The          | synthetic  |     |     |     |     |
| music is     | sampled       | from    | the generator | by           | track.       | Each track |     |     |     |     |
| is generated | from          | two     | random        | numbers      | representing | all        |     |     |     |     |
| tracks and   | two           | random  | numbers       | representing |              | individual |     |     |     |     |
tracksencodingtime-dependentandtime-independentintra-
| and inter-track |     | dependencies. | The | track-generator |     | captures |     |     |     |     |
| --------------- | --- | ------------- | --- | --------------- | --- | -------- | --- | --- | --- | --- |
dependenciesintimeandbetweennotesplayedusingaCNN
| structure. | Similarly, | the | MuseGAN | discriminator |     | is a CNN |     |     |     |     |
| ---------- | ---------- | --- | ------- | ------------- | --- | -------- | --- | --- | --- | --- |
thatjudgeswhetheramelodyisrealorsyntheticbasedonthe Evaluation of synthetic audio data poses a challenge that
|     |     |     |     |     |     |     | cannot adequately | be addressed | in general: | the significance |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------ | ----------- | ---------------- |
structureofthenotesplayedinasingletrackovertimeand
inmultipletracksatthesametime. of our proposed criteria and validity of metrics used to
Dong et al. [24] leveraged symbolic representation to measurethecriteriavarywiththetypeofaudio(e.g.,speech
reducethecomplexityoftheproblemandtoassessthequality versusmusic).Rhythmsandharmonyarehighlyrelevantfor
of the generated music samples. To evaluate the represen- music but only somewhat relevant for speech. Reasonable
evaluationsareoftenbasedondomain-knowledge.Inthecase
| tativeness | and | coherence | of the | meusic | they compared | the |     |     |     |     |
| ---------- | --- | --------- | ------ | ------ | ------------- | --- | --- | --- | --- | --- |
training data and synthetic data based on music-theoretical of music, the relevant domain is music theory, for which
measures. The authors computed the ratio of bars in which metricssuchastheratioofpauses,fragmentationofasample,
andthetonaldistance,asusedin[24],arereasonable.Fora
| no notes | were | played, the | number | of pitch | classes | used in |     |     |     |     |
| -------- | ---- | ----------- | ------ | -------- | ------- | ------- | --- | --- | --- | --- |
a bar, and the ratio of notes lasting longer than a 32nd review of objective metrics for evaluating synthetic music,
see[92].Forallkindsofaudioandformusicandspeechin
notetoevaluaterepresentativeness.Themodelcaptureddrum
patterns observed in the training data fairly well, but the particular,subjectiveevaluationsofrealismandcoherenceby
syntheticmelodiesweremorefragmentedandusedalarger humansareasignificantpartofevaluations.Reference[24]
makesuseofdomain-specificmetricsforrepresentativeness
numberofpitchclassesthantheoriginalmelodies,indicating
noise in the synthetic data. The tonal distance [41] between andcoherenceand,thus,theirassessmentisbettersuitedfor
syntheticmusicthan,forexample,thequalitativeevaluation
| tracks in | the generated |     | samples | generally | showed | a strong |     |     |     |     |
| --------- | ------------- | --- | ------- | --------- | ------ | -------- | --- | --- | --- | --- |
harmonicrelation,indicatingstrongcoherence.Inadditionto used in [22], [58], and [62]. Additionally, Donahue et al.
theseobjectivemeasures,theauthorsevaluatedthesynthetic introducedmetricsfortheevaluationofnoveltyanddiversity
ofsyntheticsoundin[23],whichishardlyanalyzedinanyof
| samples’ | harmonicity, | rhythmicity, |     | musical | structure, | and |     |     |     |     |
| -------- | ------------ | ------------ | --- | ------- | ---------- | --- | --- | --- | --- | --- |
coherencebasedonresponsesbystudyparticipants,whoalso theotherreviewedstudies.
| gave the | samples | overall | ratings | that measured |     | coherence |     |     |     |     |
| -------- | ------- | ------- | ------- | ------------- | --- | --------- | --- | --- | --- | --- |
andrealismasdefinedinourproposedframework.Thestudy C. VISUALDATAPROCESSING
participants rated the samples as 2.3 to 3.5 on a 1–5 scale; Today,thankstotheprevalenceofsmartphones,imagesand
they did not compare the samples to baseline samples from videos are produced and consumed en masse. Access to
othermodelsortotheoriginalmusic. such a vast amount of data has led to dramatic advances
|        |      |                  |     |                        |     |     | in processing | and classification | of existing | images and in |
| ------ | ---- | ---------------- | --- | ---------------------- | --- | --- | ------------- | ------------------ | ----------- | ------------- |
| Speech | also | can be generated |     | using representations. |     | One |               |                    |             |               |
ofthemoststudiedparadigmsisstatisticalparametricspeech modelstogeneratesyntheticones(see,e.g.,[69],[96]).Since
synthesis (SPSS) [94], which uses linguistic features of videosaremerelysequencesofimages,theabilitytogenerate
speech such as phonemes, cadence, and word frequency synthetic videos also has advanced. The ongoing challenge
to synthesize spoken words. Considerable research has is capturing a smooth dynamic motion in the transitions
been conducted on SPSS, but unconditional generation of betweenimages.
synthetic speech data-sets is uncommon. Common tasks ModelsbasedonCNNsandGANshavebeenhighlysuc-
are text-to-speech, voice conversion, and vocoding (making cessfulingeneratingimages.Consequently,manysuccessful
speech parameters audible). In all three, cases speech is generative models for synthetic videos have been based on
being generated from an input (text, speech fragments, them [73], [80], [83]. The primary challenge in designing
speech parameters). Though these tasks fall outside the suchmodelsisincorporationofthetemporaldimensionwith
scope of our literature review it is important to note that videos’twospatialdimensionsofthevideo.
deep learning based models for speech data are emerging TheVGANmodelproposedin[83]tacklesthischallenge
(see,e.g.,[68],[84],[93]). by decomposing the dynamic foreground from the static
| 47312 |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
background, reducing the complexity of the problem. The inthevideoissynthesizedbyatwo-dimensionalCNNimage
dynamic foreground is captured by a three-dimensional generator. Similarly, the discriminator judges the realism of
spatio-temporal CNN, and the static background can be the content and motion of a video separately using a two-
captured by a two-dimensional spatial CNN. Both CNNs dimensional CNN for the content and a three-dimensional
are incorporated into the generator of a GAN that is spatio-temporalCNNforthemotion.
then optimized against a three-dimensional spatio-temporal The authors evaluated the MoCoGAN’s performance
discriminator that judges the realism of the scene and the synthesizingsmallshortvideosofvariousscenes,including
motion. tai-chimovementsandfacialexpressions.Theyqualitatively
TheVGANmodelhasbeenappliedtosmallshortvideos assessedtheabilityofthemodeltodecomposecontentfrom
of 64 × 64 pixels with 32 frames and duration of around motion by fixing a person as the content and generating
onesecondfromFlickrindifferentcategoriescollectedsuch videos of that person performing different motions. The
as beaches, golf courses, and train stations. The authors results demonstrated MoCoGAN’s ability to generate novel
of [83] assessed the representativeness of the resulting contentbyadjustingtheinputvariablesofthegenerator.They
syntheticvideosqualitativelyandreportedgenerallycorrect foundthatthesyntheticvideosgeneratedbyMoCoGANwere
motionpatternsforscenesinthevariouscategories.Synthetic morediverseandrealisticthansyntheticvideosgeneratedby
videos of beaches contained crashing waves and synthetic VGAN [83] and TGAN [73] based on the IS. Additionally,
videos of trains contained train tracks and train cars with participants in an empirical study viewed the videos gener-
windows moving by quickly, as one would expect. The ated by MoCoGAN as more realistic than videos generated
generated scenes were sharp overall, but individual objects usingVGAN[83]andTGAN[73].Tulyakovetal.[80]also
such as people in the synthetic beach scenes tended to lack quantitativelyevaluatedthecoherenceofsyntheticvideosof
resolution.Therealismoftheresultingvideoswasevaluated facialexpressionsusingtheclassifier-basedaveragecontent
byparticipantsinanempiricalstudywhowereaskedtoview distance (ACD), which quantifies the difference between
the synthetic and original videos and choose which seemed two frames in a video in terms of content. OpenFace [5]
mostrealistic.Thoughtheparticipantsoverwhelminglychose is applied to each frame of a video presenting a facial
theoriginalvideos,thesyntheticsceneswerechosenin18% expressiontoextractfacialfeaturesthatidentifytheperson.
ofthecomparisons. Smalldifferences(distances)inthefeaturesbetweenframes
TheVGANarchitecture[83]isoptimizedforvideoswith indicate that the same person is displayed throughout the
static backgrounds. Saito et al. [73] relaxed this restriction videoand,therefore,asmallACD.TheMoCoGANobtained
in their TGAN model by decoupling the temporal dimen- highercoherencescoresthantheVGAN[83]andTGAN[73]
sion from the spatial dimensions. First, a one-dimensional videos.
temporal generator produces a sequence of temporal codes When generating synthetic videos, many concepts from
that are then mapped one-by-one to an image by a two- image generation carry over. We see this in the prevalence
dimensional image generator. The discriminator, a three- ofCNNandGANmodelsandinthemetricsusedtoevaluate
dimensional spatio-temporal CNN, then distinguishes real syntheticvideos.Specifically,theISisoftenusedtomeasure
videosfromsyntheticones.AccordingtotheIS,thesynthetic realism and diversity of synthetic videos and [80] uses
videos generated by TGAN are more diverse and realistic ACD to measure coherence; both rely on image classifiers.
thanthosegeneratedbyVGAN. When evaluating reaslism, human studies are heavily used
Tulyakovetal.[80]arguedthatthestraightforwarddecom- in addition to IS and ACD. Human evaluations of realism
position of a video into temporal and spatial dimensions, alsocapturecoherencetosomeextent.Therepresentativeness
as done in TGAN, unnecessarily increases the complexity andnoveltyofsyntheticvideosarerarelyevaluatedexplicitly.
oftheproblembyignoringsimilarmotionpatterns.In[80], Altogether, the results so far are promising for synthetic
they proposed a decomposition of the content of a video videosthatareshortandrelativelylowresolution.Thelarge
and the motion therein, which they incorporated into a number of dimensions associated with high-quality videos
generative model called MoCoGAN. Consider the various combined with the large number of frames needed even for
facial expressions presented by a person in a video. In such short videos continue to thwart efforts to synthesize more
a video, the person’s face is the content and performance complexvideos.TheintroductionoftheACDasanobjective
ofanexpressionisthemotion.Thisdisentanglementallows measure for coherence in [80] is particularly noteworthy,
the model to generate videos with the same content but sinceotherstudiessuchas[73]and[83]evaluatecoherence
differentmotionsandviceversa—thatis,videosofaperson onlyasapartoftherealismassessment.
performingdifferentfacialexpressions.
MoCoGAN incorporates this decomposition in the latent
spaceofthegenerator.Theinputtothegeneratorissplitinto D. HEALTHCARE
acontentvariableandasequenceofmotioncodes.AnRNN Generative models for synthetic medical data have gained
generatesthemotioncodesandconnectsthemtosubsequent attention in recent years. The sensitivity of medical data
codes to ensure a coherent motion. Then, given the fixed and strict access restrictions make sharing of original
contentvariableforallframesandamotioncode,eachframe medical data from patients extremely challenging [7].
VOLUME11,2023 47313

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
TABLE4. Excerptofmodelstogeneratesyntheticmedicaldataand EHRsincludepatients’demographicinformation,diagnoses,
metricsusedtoevaluatethem. laboratory test results, medication history, clinical notes,
|     |     |     |     |     |     | and medical | images,         |     | and other | medical        | records | [86]         | and |
| --- | --- | --- | --- | --- | --- | ----------- | --------------- | --- | --------- | -------------- | ------- | ------------ | --- |
|     |     |     |     |     |     | disclose    | discrete-valued |     | codes     | for diagnoses, |         | medications, |     |
andprocedures.
|     |     |     |     |     |     | Choi | et al. [20] | studied | synthetic | sequences |     | of  | discrete- |
| --- | --- | --- | --- | --- | --- | ---- | ----------- | ------- | --------- | --------- | --- | --- | --------- |
valuedmulti-labelEHRdatacontaininginformationondiag-
|     |     |     |     |     |     | noses and | treatments. |     | The sequences |     | in the | data were | long |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ------------- | --- | ------ | --------- | ---- |
andhigh-dimensional,thuspresentingsignificantchallenges
forgenerationofsyntheticdata.Theauthorsaddressedthese
challengesbycombininganautoencoder(AE)andaGANin
theirgenerativemodel,medGAN.TheAEwasusedtoreduce
|     |     |     |     |     |     | the complexity |     | of the | output | data of | the generator, |     | which |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ------ | ------- | -------------- | --- | ----- |
learnssalientfeaturesofthesamplesbyprojectingthemtoa
lowerdimensionalspaceandthenprojectingthembacktothe
originalspace[36],[82].Thus,medGANgeneratessynthetic
A promising solution is to use generated synthetic data data in the lower dimensional space. Then, the pre-trained
instead.Syntheticmedicaldatacanbesharedandpublished decoderconvertsthegeneratedoutputtosyntheticEHRdata
for secondary analyses since the privacy of patients is intheoriginalspace.
guaranteed.
TheauthorsevaluatedmedGANandfoundthatitoutper-
Datafromintensivecareunits(ICUs),wherepatientswith formed several generative models, including random noise,
severeandlife-threateningconditionsfirstreceivetreatment, independent sampling [20], stacked restricted Boltzmann
are especially valuable for clinical analysis [16]. The data machines [42] and VAEs. Representativeness and diversity
can include real-valued monitoring information, such as are only evaluated qualitatively, but the authors argued that
measuredoxygensaturation,heartrate,andrespiratoryrate.
significantimprovementswereaccomplishedbyapplyingthe
Esteban et al. [27] generated such synthetic medical data minibatch averaging method [20] to reduce overfitting and
based on information collected from the first four hours mode collapse. Novelty was evaluated by conducting two
of patients’ stays in an ICU. They employed an LSTM privacyriskevaluations.Onemeasuredtheriskofdisclosure
as the generator in a GAN and another LSTM as the ofpersonallyidentifiableinformationandtheothermeasured
discriminator of real and synthetic data sequences. They the risk of disclosure of personal sensitive medical data.
evaluated representativeness of the generated data using The evaluations determined that medGAN can generate
MMD and by training a classifier model on the synthetic novel private synthetic data that reveal little information to
data-set and testing it on a real holdout data-set (train on potentialattackersratherthansimplyreproducingthetraining
synthetic, test on real (TSTR)). They evaluated realism by samples. Overall, medGan’s synthetic data were reported to
training a classifier model on the real data-set and testing berealistic,butqualitativeevaluationbyasingledoctorisnot
it on the synthetic data-set (train on real, test on synthetic entirelyconvincing.
(TRTS)).Inbothcases,theclassifiermodelsachievedresults Since introduction of medGAN, other researchers have
| comparable | to models trained | and | tested solely | on original |     |           |        |           |             |             |          |          |      |
| ---------- | ----------------- | --- | ------------- | ----------- | --- | --------- | ------ | --------- | ----------- | ----------- | -------- | -------- | ---- |
|            |                   |     |               |             |     | extended  | it in  | different | directions. |             | Two that | have     | out- |
| data.      |                   |     |               |             |     | performed | medGAN |           | in all      | experiments | were     | proposed |      |
Noveltyisespeciallyimportantinprivacycontexts;thatis, by Baowaly et al. [6]. The medWGAN model combines
it must be impossible to reconstruct the original data-points medGAN with the Wasserstein GAN model, which uses
fromthesyntheticones.Overall,[27]foundthatthesynthetic a gradient penalty [2], [38] to minimize divergences in
data-pointswerenotclosetooriginalsingledata-pointsbased
|     |     |     |     |     |     | Wasserstein | distances. |     | The medBGAN |     | (medical | boundary- |     |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ----------- | --- | -------- | --------- | --- |
on the evaluation of the distances between the synthetic seeking GAN) model trains the generator to obtain a
data-pointsandtheirrealnearestneighbors.Theirqualitative distribution of samples located on the decision boundary of
explorationofthelatentspace—conductedbyinterpolating thediscriminator.Toevaluatethemodels’representativeness,
between generated points —also showed that the model the authors conducted the Kolmogorov-Smirnov (K-S) test
| yielded diverse | results. To | account | for the | importance | of  |             |     |                |     |               |     |              |     |
| --------------- | ----------- | ------- | ------- | ---------- | --- | ----------- | --- | -------------- | --- | ------------- | --- | ------------ | --- |
|                 |             |         |         |            |     | and compare | the | dimension-wise |     | probabilities |     | and averages |     |
privacy, they adapted the training of the original model to of the real and synthetic data. Realism was evaluated by
incorporate differential privacy [1], [25]. Under the stricter comparingpredictionsmadebymachinelearningmodelsfor
privacyconditions,theyreportedthatthesyntheticdatawere the real and synthetic data. Association rule mining (ARM)
highlyrepresentativeandslightlylessrealistic. isoftenusedtoidentifyassociationsandpatternsinclinical
Thereal-valuedtime-seriesdatausedbyEstebanetal.[27]
|     |     |     |     |     |     | concepts | in EHR | data | [89] and | was used | by  | [6] to | evaluate |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ---- | -------- | -------- | --- | ------ | -------- |
are important in healthcare but are one of many types of realism and coherence. Another extension of medGAN for
electronichealthrecords(EHR).EHRdatahasbeenthemain generatingreal-valuedtime-seriesdata,hasbeenproposedby
focusofrecentstudies[4]andturnsouttobequitediverse. Yahietal.[90].
| 47314 |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
TABLE5. Excerptofmodelsforgeneratingmobilitydataandapplied data or generating completely synthetic trajectories that
metrics. cannotberelatedtoindividuals.
Ouyangetal.[65]studiedgenerationofsyntheticrealistic
human location trajectories for privacy-sensitive secondary
data analyses. Usually, mobility trajectories are represented
as sequences of continuous coordinates (x,y) consisting
of a longitudinal and latitudinal component over time t.
Ouyang et al. converted this time-major representation
into a location-major representation in the form of maps
corresponding to times of stays at each coordinate (x,y).
The maps were then fed into a GAN consisting of a
deconvolutionalgeneratorandaconvolutionaldiscriminator.
Theauthorsevaluatethemodelresultsprimarilyinterms
ofrepresentativenessandcoherence.Representativenesswas
evaluated by comparing geographical statistics describing
Medical text and images also have attracted attention.
the real data with the same statistics for the synthetic data.
Medical text consists of clinical notes and patients’ chief
Theycomparethemarginalprobabilitiesofvisitingacertain
complaints, which share characteristics of other types of
locationatacertaintimeandofremainingthereforacertain
text data (see Section III-A) but typically are short and
durationusingJensen-Shannondivergence(JSD).
are composed of a limited number of words from medical
The so called semantics of the trajectories play a key
vocabularies.Lee[55]appliedanencoder-decodermodelto
role in producing representativeness and coherence. The
generate synthetic natural-language chief complaints using
semantics give a trajectory intrinsic meaning, which can be
EHR data from around 5.5 million records of emergency
difficult for generative models to capture. The path ‘‘home-
department visits. Guan et al. [37] proposed a GAN model
bus-work-bus-home’’, for example, intuitively makes sense
to generate Chinese EHR text data. Both models use
whereas ‘‘airport-home-work-train’’ does not make sense
demographic and disease features as inputs and generate
and semantically is unlikely to be true. Ouyang et al. fur-
correspondingEHRtextdata.However,theyareconditional
ther distinguished between absolute and relative semantics.
modelsthatfalloutsidethescopeofthissurvey.
Absolute semantics captures the meaning of each location
In healthcare, synthetic EHR data is primarily used to
in a trajectory; relative semantics capture the meaning of
protect patients’ privacy while enabling data sharing and
a location in a trajectory relative to other visited locations
secondary data analyses. Thus, most studies in the field are
in the trajectory. To evaluate representativeness, the authors
mainlyconcernedwithnovelty,representativeness,andreal-
compared the absolute semantics of the real and synthetic
ism. Novelty is particularly important to privacy-protection
data at the population level. Likewise, they measured
and, thus, is often evaluated using privacy tests. Tests for
coherence using a comparison of the relative semantics
representativesnessandrealisminEHRsarenotnecessarily
measured by the pair-wise semantic distance which was
domain-specific;TSTRandTRTShavemostoftenbeenused
originallyintroducedbyBindschaedlerandShokri[8].This
to evaluate those criteria. [27] used particularly interesting
metric accounts for trajectories of people who can live in
evaluation procedures, compared to other reviewed studies
geographically different locations but still share semantic
suchas[6]and[20].Theycomparedtheoriginaldatawiththe
patterns.TheirresultsshowedthattheGAN-basedapproach
syntheticdataandevaluatedrepresentativenessusingTSTR,
preserved both the statistical characteristics of the original
realismusingTRTSandnoveltyviatheNNdistance.
dataandtheirrelativesemantics.
Ouyang et al. [65] did not conduct any privacy tests
E. MOBILITY and limited the evaluation to one GAN-based model.
Everyday, massive quantities of data on human mobility In [53], Kulkarni et al. extended their study by testing the
are collected. Mobile devices such as smartphones are performance of seven generative models that used different
equippedwithGPSfunctionalityandtransportationsystems architectures and conducting privacy tests to measure the
(carsharing,logistics,publictransports)usuallyincorporate noveltyoftheresults.Theycompareddeepgenerativemodels
automatic tracking. Mobility data are used in a wide basedonGANs,LSTMs,andothervariationsofRNNswith
range of tasks, including urban traffic predictions [57], eachotherandwithastatisticalmodel,Copulas.Interestingly,
shared mobility services [18], marketing services [47], and CopulasandtheGANsperformedbestintermsofrepresen-
transportation of people and goods [29]. However, the tativeness, which was evaluated by comparing geographical
risk of re-identification of individuals makes sharing of statistics and absolute semantics (similar to [65]) and by
such data highly sensitive. The relevance of this risk has measuring MMD. The RNNs and Copulas generated the
been demonstrated even for aggregated mobility data [88]. mostcoherentsynthetictrajectories.Thelong-rangetemporal
Synthetic mobility trajectories do not present this risk and dependencies throughout the generated trajectories, which
thus enable sharing, by either obfuscating the original path measurecoherence,decayedmostslowly.
VOLUME11,2023 47315

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
Interestingly,Kulkarnietal.[53]measuredthenoveltyof andtheirrelationships,deepgenerativemodelshaveboosted
the synthetic data by conducting two specific privacy tests. progressinsyntheticdatagenerationsignificantly.
They applied a location-sequence attack, which determines Thisarticlediscussesdeepgenerativemodelsforsynthetic
the level of accuracy to which trajectories in the original dataandintroducesasetofhigh-levelevaluationcriteriafor
data can be reconstructed, and a membership interference a data-driven assessment of the quality of generated data.
attack,whichmeasurestheaccuracyofaninferencethatan Weexaminetheiruseandapplicabilitytosyntheticsequential
individual contributed to a specific trajectory. In both tests, datainthefieldsofnaturallanguage,speech,audioandvisual
the RNN and GAN models outperformed the other models dataprocessing,healthcareandmobility.
byaconsiderablemargin. The proposed evaluation framework allows for clear and
The synthetically generated data in [53] and [65] were easycommunicationoftherequirementsposedonsynthetic
intended to be used in privacy-sensitive secondary data data in different domains and use-cases. We find that
analyses.Thisisanimportantuse,butthevalueofsynthetic synthetic texts in NLP applications are primarily evaluated
mobility data extends far beyond that. In [56], Lin et al. forrepresentativenessandrealism.Syntheticmusic,speech,
usedlabeledcellulargeo-locationdatacollectedfrommobile and video data must be realistic and coherent. Studies in
devicestogeneratesyntheticmobilitydatafortrafficvolume healthcare are mainly concerned with generating private
simulations. Actual high-quality data on traffic volumes are synthetic EHRs that still allow for secondary data analysis
difficulttocollect.Thesimulationswereappliedtoasuper- and, thus, assess the data’s representativeness, novelty and
districtintheSanFranciscoBayAreainCaliforniaandwere realism. Synthetic mobility trajectories are generated for
used to provide decision support for several transportation similarpurposeswithanadditionalfocusontheircoherence.
projects designed to improve urban transportation planning. However,notallmobilitystudiesexaminethesyntheticdata’s
The authors employed an LSTM model and evaluated its novelty, potentially leading to privacy risks when sharing
representativeness by comparing the vehicle traffic counts such data. Table 6 provides an overview of the assessment
and public transit boarding and alighting counts of the resultsintherevieweddomains.
simulated results and the actual counts. They argue that The results show that in many domains the requirements
transportation policy-makers and planners can benefit from posed on synthetic data do not conflict each other. For
usingsyntheticlocationdatatoimprovetheirunderstanding example,representativenessandrealisminNLPapplications
ofurbanmobility. or realism and coherence in video data go well together.
The literature on models for generating mobility data is However,therearedomainswhererequirementsdoconflict
not vast, and the quantitative approaches used to validate eachother.Thiscanbeobservedinprivacysensitivedomains
suchmodelsvarygreatly.Inreviewingdifferentapplications such as healthcare and in creative domains such as music
to mobility data, we observed that representativeness was composition, where synthetic data have to be representative
particularly important in all of the studies. Consequently, and novel at the same time. Finding an acceptable trade-
the studies provide reliable metrics for representativeness, off between those criteria can be challenging and usually
suchasMMD,JSD,absolutesemantics,andcountvariables. involvesalotoftuningbytheexperimenter.
Coherence seems to be important in many cases but is Wealsofindthatthenatureofmetricsusedtoevaluatethe
evaluated in various ways, including relative semantics of criteriacanvarysignificantly.Somestudiesevaluatecriteria
the trajectories and observations of decays of temporal only qualitatively by looking at synthetic text samples or
dependencies throughout the trajectory. Privacy, of course, listeningtosyntheticmusicsamples.Inmostcases,onlythe
is a significant issue. Reference [53] especially stands out individual-levelcriteria(i.e.,novelty,realism,andcoherence)
its consideration of privacy as the authors conducted robust are evaluated in this subjective way, but sometimes also,
privacytestsontheirsyntheticdata.Wealsofindthatallof representativeness and diversity are. Other studies rely on
the reviewed studies related to mobility presented a strong human evaluations by laypeople or experts to judge realism
use-caseforthegenerativemodels. and coherence of synthetic data. Human evaluations often
also contain subjectivity either by the designer or the study
IV. SUMMARYANDCONCLUSION participants. Thus, the most objective measures are formal
Synthetic data allows governments, businesses, and computational metrics. Such metrics are primarily used to
researcherstoeasilyaccessandsharesensitivedatawithout evaluate representativeness (e.g., by MMD or NLL) and
the risk of violating privacy regulations. The importance diversity (e.g., self-BLEU or distances) of synthetic data.
of having access to highly sensitive data was highlighted Inmanycases,noveltyisnotevaluatedatallandcoherence
again through the COVID pandemic, where governments isassessedaspartofevaluatingthedata’srealism.
and researchers rely on high-quality sensitive medical data. Ourreviewhighlightsthatgenerativearchitecturesareused
Furthermore,thedemocratizingeffectofaccessiblesynthetic inavarietyofapplicationsand,inparticular,GANsreceive
data mitigates the power of large data aggregators, such as much attention. Most often, the architectural elements are
GoogleandFacebook.Itreducesthelimitationsofreal-world used in conjunction with each other. In many cases, at the
data-sets,suchasinherentbiases,insufficientquantities,and coreofthenetworks,RNNsorCNNsareinvolvedtoensure
class imbalance. With their ability to capture complex data causally coherent generation of synthetic sequential data.
47316 VOLUME11,2023

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
TABLE6. Overviewofreviewedapplicationdomainsandmetricsusedtomeasurerepresentativeness,novelty,realism,diversity,andcoherenceofdeep
generativemodels.
Autoregressive elements and attention mechanisms are also the data. The decisions made during the COVID pandemic,
appliedtosomeuse-cases. forexample,werehighlysensitivetotherecencyofthedata.
For the future, our proposed evaluation framework for Adecision-orientedevaluationapproachcouldhelpimprove
unconditionally generated synthetic data has the potential decision-making(oravoidweakdecisions)bycontrastingthe
tobeextendedfortheevaluationofconditionallygenerated decisions derived from synthetic data scenarios with those
data. That kind of data is always generated within a based on the original, real-life data. Recent research into
given context, such as categories of videos or genres of fairness and debiasing using synthetic data are promising
songs.Anevaluationframeworkforconditionallygenerated startingpointsinthisdirection.
| synthetic     | data has  | to account |           | for that context. |      | We expect  |     |     |     |     |     |
| ------------- | --------- | ---------- | --------- | ----------------- | ---- | ---------- | --- | --- | --- | --- | --- |
| conditionally | generated |            | synthetic | data to           | need | robustness |     |     |     |     |     |
REFERENCES
within a context and variability to be more nuanced [1] M.Abadi,A.Chu,I.Goodfellow,H.B.McMahan,I.Mironov,K.Talwar,
dependingonthecontext. andL.Zhang,‘‘Deeplearningwithdifferentialprivacy,’’inProc.ACM
SIGSACConf.Comput.Commun.Secur.,2016,pp.308–318.
Withmorejurisdictionspassingprivacylaws,inthefuture,
|           |           |      |         |                 |     |           | [2] M. Arjovsky, | S. Chintala, | and L. Bottou, ‘‘Wasserstein |     | GAN,’’ 2017, |
| --------- | --------- | ---- | ------- | --------------- | --- | --------- | ---------------- | ------------ | ---------------------------- | --- | ------------ |
| we expect | synthetic | data | to gain | more attention. |     | We expect |                  |              |                              |     |              |
arXiv:1701.07875.
moreadvancedandmoreobjectivemetricsthatallowabetter [3] A. S. Assefa, D. Dervovic, M. Mahfouz, E. R. Tillman, P. Reddy,
|          |           |            |     |              |      |          | and M.Veloso, | ‘‘Generating | synthetic data in | finance: | Opportunities, |
| -------- | --------- | ---------- | --- | ------------ | ---- | -------- | ------------- | ------------ | ----------------- | -------- | -------------- |
| and more | objective | assessment |     | of synthetic | data | quality, |               |              |                   |          |                |
challengesandpitfalls,’’inProc.1stACMInt.Conf.AIFinance(ICAIF).
| particularly | on the        | individual | level. | The development |           | of the  |          |                      |               |            |       |
| ------------ | ------------- | ---------- | ------ | --------------- | --------- | ------- | -------- | -------------------- | ------------- | ---------- | ----- |
|              |               |            |        |                 |           |         | NewYork, | NY, USA: Association | for Computing | Machinery, | 2021, |
| IS, used     | for synthetic | images     | and    | videos,         | and other | metrics | pp.1–8.  |                      |               |            |       |
[4] J.R.A.Solares,F.E.D.Raimondi,Y.Zhu,F.Rahimian,D.Canoy,J.Tran,
| that correlate | well | with | the human | judgement | of  | realism, |     |     |     |     |     |
| -------------- | ---- | ---- | --------- | --------- | --- | -------- | --- | --- | --- | --- | --- |
A.C.P.Gomes,A.H.Payberah,M.Zottoli,M.Nazarzadeh,N.Conrad,
pointinthatdirection.In-depthresearchofobjectivemetrics
K.Rahimi,andG.Salimi-Khorshidi,‘‘Deeplearningforelectronichealth
allows systematic assessment of synthetic data quality with records: A comparative review of multiple deep neural architectures,’’
more robustness and less subjectivity in it. Meanwhile, J.Biomed.Informat.,vol.101,Jan.2020,Art.no.103337.
|     |     |     |     |     |     |     | [5] T. Baltrusaitis, | P. Robinson, | and L.-P. Morency, | ‘‘OpenFace: | An open |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | ------------ | ------------------ | ----------- | ------- |
weexpectacontinuationofthecoexistenceandcombination sourcefacialbehavioranalysistoolkit,’’inProc.IEEEWinterConf.Appl.
of quality assessment based on expert judgment and formal Comput.Vis.(WACV),Mar.2016,pp.1–10.
computationalmetrics. [6] M. K. Baowaly, C.-C. Lin, C.-L. Liu, and K.-T. Chen, ‘‘Synthesizing
electronichealthrecordsusingimprovedgenerativeadversarialnetworks,’’
| Another | potentially | interesting |     | area worth | further | explor- |     |     |     |     |     |
| ------- | ----------- | ----------- | --- | ---------- | ------- | ------- | --- | --- | --- | --- | --- |
J.Amer.Med.Inform.Assoc.,vol.26,no.3,pp.228–241,Mar.2019.
ing is to complement a purely data-driven approach to [7] B. K. Beaulieu-Jones, Z. S. Wu, C. Williams, R. Lee, S. P. Bhavnani,
assess the quality of synthetic data with a decision-oriented J.B.Byrd,andC.S.Greene,‘‘Privacy-preservinggenerativedeepneural
networkssupportclinicaldatasharing,’’Circulat.,CardiovascularQual.
| view. Credible |     | decisions | made | on the basis | of  | data can |     |     |     |     |     |
| -------------- | --- | --------- | ---- | ------------ | --- | -------- | --- | --- | --- | --- | --- |
Outcomes,vol.12,no.7,Jul.2019,Art.no.e005122.
| require          | certain | properties | of     | the data. | Biased | data with |                      |                    |                        |           |               |
| ---------------- | ------- | ---------- | ------ | --------- | ------ | --------- | -------------------- | ------------------ | ---------------------- | --------- | ------------- |
|                  |         |            |        |           |        |           | [8] V. Bindschaedler | and R.             | Shokri, ‘‘Synthesizing | plausible | privacy-      |
|                  |         |            |        |           |        |           | preserving           | location traces,’’ | in Proc. IEEE Symp.    | Secur.    | Privacy (SP), |
| underrepresented |         | minority   | groups | can be    | a weak | basis for |                      |                    |                        |           |               |
May2016,pp.546–563.
| decisions    | influencing | all | individuals, | including    | the    | minority  |               |                 |                               |     |              |
| ------------ | ----------- | --- | ------------ | ------------ | ------ | --------- | ------------- | --------------- | ----------------------------- | --- | ------------ |
|              |             |     |              |              |        |           | [9] A. Borji, | ‘‘Pros and cons | of GAN evaluation measures,’’ |     | Comput. Vis. |
| group. Other | decisions   |     | can be       | sensitive to | recent | events in |               |                 |                               |     |              |
ImageUnderstand.,vol.179,pp.41–65,Feb.2019.
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     | 47317 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
[10] A. Borji, ‘‘Pros and cons of GAN evaluation measures: New develop- [32] M. Frid-Adar, E. Klang, M. Amitai, J. Goldberger, and H. Greenspan,
ments,’’2021,arXiv:2103.09396. ‘‘Synthetic data augmentation using GAN for improved liver lesion
[11] M. Bretan, G. Weinberg, and L. Heck, ‘‘A unit selection methodology classification,’’ in Proc. IEEE 15th Int. Symp. Biomed. Imag. (ISBI),
formusicgenerationusingdeepneuralnetworks,’’inProc.8thInt.Conf. Apr.2018,pp.289–293.
Comput.Creativity(ICCC),2017,pp.72–79. [33] A.GattandE.Krahmer,‘‘Surveyofthestateoftheartinnaturallanguage
generation:Coretasks,applicationsandevaluation,’’J.Artif.Intell.Res.,
[12] J.-P.Briot,‘‘Fromartificialneuralnetworkstodeeplearningformusic
generation:History,conceptsandtrends,’’NeuralComput.Appl.,vol.33, vol.61,no.1,p.65170,Jan.2018.
no.1,pp.39–65,Jan.2021. [34] F. A. Gers, J. Schmidhuber, and F. Cummins, ‘‘Learning to forget:
[13] J.-P.Briot,G.Hadjeres,andF.-D.Pachet,‘‘Deeplearningtechniquesfor Continual prediction with LSTM,’’ Neural Comput., vol. 12, no. 10,
pp.2451–2471,Oct.2000.
musicgeneration—Asurvey,’’2017,arXiv:1709.01620.
|                  |     |                 |        |     |          |             |       | [35] H.Gm,M.K.Gourisaria,M.Pandey,andS.S.Rautaray,‘‘Acompre- |     |     |     |     |     |     |     |
| ---------------- | --- | --------------- | ------ | --- | -------- | ----------- | ----- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
| [14] T. B. Brown | et  | al., ‘‘Language | models | are | few-shot | learners,’’ | 2020, |                                                              |     |     |     |     |     |     |     |
hensivesurveyandanalysisofgenerativemodelsinmachinelearning,’’
arXiv:2005.14165.
[15] R.E.BucklinandC.Sismeiro,‘‘ClickhereforInternetinsight:Advances Comput.Sci.Rev.,vol.38,Nov.2020,Art.no.100285.
inclickstreamdataanalysisinmarketing,’’J.Interact.Marketing,vol.23, [36] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning.
|     |     |     |     |     |     |     |     | Cambridge, | MA, | USA: | MIT | Press, | 2016. | [Online]. Available: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---- | --- | ------ | ----- | -------------------- | --- |
no.1,pp.35–48,Feb.2009.
http://www.deeplearningbook.org
| [16] L. Anthony | Celi,    | R. G.         | Mark, D. | J. Stone,     | and R. | A. Montgomery, |       |                                                                    |     |     |     |     |     |     |     |
| --------------- | -------- | ------------- | -------- | ------------- | ------ | -------------- | ----- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|                 |          |               |          |               |        |                |       | [37] J.Guan,R.Li,S.Yu,andX.Zhang,‘‘Generationofsyntheticelectronic |     |     |     |     |     |     |     |
| ‘‘‘Big          | data’ in | the intensive | care     | Unit. Closing | the    | data loop,’’   | Amer. |                                                                    |     |     |     |     |     |     |     |
medicalrecordtext,’’inProc.IEEEInt.Conf.Bioinf.Biomed.(BIBM),
J. Respiratory Crit. Care Med., vol. 187, no. 11, pp.1157–1160, Dec.2018,pp.374–380.
Jun.2013.
|     |     |     |     |     |     |     |     | [38] I.Gulrajani,F.Ahmed,M.Arjovsky,V.Dumoulin,andA.C.Courville, |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[17] Z.Che,Y.Cheng,S.Zhai,Z.Sun,andY.Liu,‘‘Boostingdeeplearning
|     |     |     |     |     |     |     |     | ‘‘Improved | training | of  | Wasserstein | GANs,’’ | in  | Advances in | Neural |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ----------- | ------- | --- | ----------- | ------ |
riskpredictionwithgenerativeadversarialnetworksforelectronichealth
|            |          |      |            |      |                |      |       | Information | Processing |     | Systems, | I. Guyon, | U.  | V. Luxburg, S. | Bengio, |
| ---------- | -------- | ---- | ---------- | ---- | -------------- | ---- | ----- | ----------- | ---------- | --- | -------- | --------- | --- | -------------- | ------- |
| records,’’ | in Proc. | IEEE | Int. Conf. | Data | Mining (ICDM), | Nov. | 2017, |             |            |     |          |           |     |                |         |
H.Wallach,R.Fergus,S.Vishwanathan,andR.Garnett,Eds.RedHook,
| pp.787–792. |     |     |     |     |     |     |     | NY,USA:CurranAssociates,2017,pp.5767–5777. |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
[18] T. D. Chen, K. M. Kockelman, and J. P. Hanna, ‘‘Operations of a [39] X.GuoandL.Zhao,‘‘Asystematicsurveyondeepgenerativemodelsfor
| shared, | autonomous, | electric | vehicle | fleet: | Implications | of vehicle | &   |     |     |     |     |     |     |     |     |
| ------- | ----------- | -------- | ------- | ------ | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
graphgeneration,’’IEEETrans.PatternAnal.Mach.Intell.,vol.45,no.5,
charginginfrastructuredecisions,’’Transp.Res.A,PolicyPract.,vol.94,
pp.5370–5390,May2023.
pp.243–254,Dec.2016. [40] K.Guu,T.B.Hashimoto,Y.Oren,andP.Liang,‘‘Generatingsentences
[19] Y.Chen,Y.Lv,andF.Wang,‘‘Trafficflowimputationusingparalleldata by editing prototypes,’’ Trans. Assoc. Comput. Linguistics, vol. 6,
andgenerativeadversarialnetworks,’’IEEETrans.Intell.Transp.Syst., pp.437–450,Dec.2018.
vol.21,no.4,pp.1624–1630,Apr.2020.
|     |     |     |     |     |     |     |     | [41] C. Harte, | M.  | Sandler, | and M. | Gasser, | ‘‘Detecting | harmonic change | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | ------ | ------- | ----------- | --------------- | --- |
[20] E.Choi,S.Biswal,B.Malin,J.Duke,W.F.Stewart,andJ.Sun,‘‘Gen-
|     |     |     |     |     |     |     |     | musical | audio,’’ | in Proc. | 1st | ACM Workshop |     | Audio Music Comput. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | -------- | --- | ------------ | --- | ------------------- | --- |
erating multi-label discrete patient records using generative adversarial Multimedia(AMCMM).NewYork,NY,USA:AssociationforComputing
| networks,’’2017,arXiv:1703.06490. |     |     |     |     |     |     |     | Machinery,2006,p.2126. |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
[21] S.De,M.Bermudez-Edo,H.Xu,andZ.Cai,‘‘Deepgenerativemodelsin [42] G.E.HintonandR.R.Salakhutdinov,‘‘Reducingthedimensionalityof
theindustrialInternetofThings:Asurvey,’’IEEETrans.Ind.Informat., data with neural networks,’’ Science, vol. 313, no. 5786, pp.504–507,
| vol.18,no.9,pp.5728–5737,Sep.2022. |     |     |     |     |     |     |     | Jul.2006. |     |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[22] S.Dieleman,A.V.D.Oord,andK.Simonyan,‘‘Thechallengeofrealistic [43] S.HochreiterandJ.J.Schmidhuber,‘‘Longshort-termmemory,’’Neural
musicgeneration:Modellingrawaudioatscale,’’inAdvancesinNeural Comput.,vol.9,no.8,pp.1735–1780,Dec.1997.
InformationProcessingSystems,S.Bengio,H.Wallach,H.Larochelle, [44] Y.Hong,U.Hwang,J.Yoo,andS.Yoon,‘‘Howgenerativeadversarial
K.Grauman,N.Cesa-Bianchi,andR.Garnett,Eds.RedHook,NY,USA: networks and their variants work: An overview,’’ ACM Comput. Surv.,
CurranAssociates,2018,pp.7989–7999. vol.52,no.1,pp.1–43,Feb.2019.
[23] C.Donahue,J.McAuley,andM.Puckette,‘‘Adversarialaudiosynthe- [45] C.-Z. A. Huang, A. Vaswani, J. Uszkoreit, N. Shazeer, I. Simon,
sis,’’ in Proc. Int. Conf. Learn. Represent., 2019. [Online]. Available: C.Hawthorne,A.M.Dai,M.D.Hoffman,M.Dinculescu,andD.Eck,
https://arxiv.org/abs/1802.04208 ‘‘Musictransformer,’’2018,arXiv:1809.04281.
|            |          |           |       |           |       |                  |     | [46] L.Huang,B.Ding,Y.Xu,andY.Zhou,‘‘Analysisofuserbehaviorin |     |           |     |            |          |             |       |
| ---------- | -------- | --------- | ----- | --------- | ----- | ---------------- | --- | ------------------------------------------------------------- | --- | --------- | --- | ---------- | -------- | ----------- | ----- |
| [24] H. W. | Dong, W. | Y. Hsiao, | L. C. | Yang, and | Y. H. | Yang, ‘‘MuseGAN: |     |                                                               |     |           |     |            |          |             |       |
|            |          |           |       |           |       |                  |     | a large-scale                                                 | VoD | system,’’ | in  | Proc. 27th | Workshop | Netw. Oper. | Syst. |
Multi-tracksequentialgenerativeadversarialnetworksforsymbolicmusic
generationandaccompaniment,’’inProc.32ndAAAIConf.Artif.Intell., SupportDigit.AudioVideo(NOSSDAV),NewYork,NY,USA,Jun.2017,
| 2018,pp.34–41. |     |     |     |     |     |     |     | pp.49–54.  |         |           |        |             |        |                    |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --------- | ------ | ----------- | ------ | ------------------ | --- |
|                |     |     |     |     |     |     |     | [47] S. K. | Hui, P. | S. Fader, | and E. | T. Bradlow, | ‘‘Path | data in marketing: |     |
[25] C.Dwork,K.Kenthapadi,F.McSherry,I.Mironov,andM.Naor,‘‘Our
Anintegrativeframeworkandprospectusformodelbuilding,’’Marketing
data,ourselves:Privacyviadistributednoisegeneration,’’inProc.Annu.
Sci.,vol.28,no.2,pp.320–335,Mar.2009.
Int.Conf.TheoryAppl.Cryptograph.Techn.Berlin,Germany:Springer,
|     |     |     |     |     |     |     |     | [48] N. Jaques, | S.  | Gu, E. | Richard | Turner, | and D. | Eck, ‘‘Tuning recurrent |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ------- | ------- | ------ | ----------------------- | --- |
2006,pp.486–503.
|     |     |     |     |     |     |     |     | neural | networks | with | reinforcement | learning,’’ |     | in Proc. 5th Int. | Conf. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---- | ------------- | ----------- | --- | ----------------- | ----- |
[26] E.Erdem,M.Kuyu,S.Yagcioglu,A.Frank,L.Parcalabescu,B.Plank, Learn.Represent.(ICLR),Toulon,France,Apr.2017.[Online].Available:
| A. Babii, | O. Turuta, | A.  | Erdem, | I. Calixto, | E. Lloret, | E.-S. | Apostol, |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------ | ----------- | ---------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://arxiv.org/abs/1611.02796
| C.-O.Truică, | B.       | Šandrih, | S. Martinčić-Ipšić, |             | G. Berend, | A.        | Gatt, and |                  |     |            |       |       |           |                      |     |
| ------------ | -------- | -------- | ------------------- | ----------- | ---------- | --------- | --------- | ---------------- | --- | ---------- | ----- | ----- | --------- | -------------------- | --- |
|              |          |          |                     |             |            |           |           | [49] F. Jelinek, | R.  | L. Mercer, | L. R. | Bahl, | and J. K. | Baker, ‘‘Perplexity— |     |
| G.Korvel,    | ‘‘Neural | natural  | language            | generation: | A          | survey on | multilin- |                  |     |            |       |       |           |                      |     |
Ameasureofthedifficultyofspeechrecognitiontasks,’’J.Acoust.Soc.
guality,multimodality,controllabilityandlearning,’’J.Artif.Intell.Res., Amer.,vol.62,no.S1,p.S63,Dec.1977.
vol.73,pp.1131–1207,Apr.2022.
|                  |        |            |      |            |               |         |        | [50] P.B.Jørgensen,M.N.Schmidt,andO.Winther,‘‘Deepgenerativemodels |     |            |                 |     |          |                |       |
| ---------------- | ------ | ---------- | ---- | ---------- | ------------- | ------- | ------ | ------------------------------------------------------------------ | --- | ---------- | --------------- | --- | -------- | -------------- | ----- |
| [27] C. Esteban, | S.     | L. Hyland, | and  | G. Rätsch, | ‘‘Real-valued |         | (medi- |                                                                    |     |            |                 |     |          |                |       |
|                  |        |            |      |            |               |         |        | for molecular                                                      |     | science,’’ | Mol. Informat., |     | vol. 37, | nos. 1–2, Jan. | 2018, |
| cal) time        | series | generation | with | recurrent  | conditional   | GANs,’’ | 2017,  |                                                                    |     |            |                 |     |          |                |       |
Art.no.1700133.
arXiv:1706.02633.
|     |     |     |     |     |     |     |     | [51] P. D. | Kingma | and M. | Welling, | ‘‘Auto-encoding |     | variational | Bayes,’’ |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------ | -------- | --------------- | --- | ----------- | -------- |
[28] X.-X.Fan,K.-P.Chow,andF.Xu,‘‘Webuserprofilingbasedonbrowsing in Proc. 2nd Int. Conf. Learn. Represent. (ICLR), Y. Bengio and
behavioranalysis,’’inAdvancesinDigitalForensicsX,G.Petersonand Y. LeCun, Eds., Banff, AB, Canada, Apr. 2014. [Online]. Available:
S.Shenoi,Eds.Berlin,Germany:Springer,2014,pp.57–71.
https://arxiv.org/abs/1312.6114
| [29] E. Fatnassi, | J.  | Chaouachi, | and W. | Klibi, | ‘‘Planning | and operating | a   |                  |      |            |     |                |     |               |        |
| ----------------- | --- | ---------- | ------ | ------ | ---------- | ------------- | --- | ---------------- | ---- | ---------- | --- | -------------- | --- | ------------- | ------ |
|                   |     |            |        |        |            |               |     | [52] I. Kobyzev, | S.J. | D. Prince, | and | M. A.Brubaker, |     | ‘‘Normalizing | flows: |
shared goods and passengers on-demand rapid transit system for sus- Anintroductionandreviewofcurrentmethods,’’2019,arXiv:1908.09257.
tainablecity-logistics,’’Transp.Res.B,Methodol.,vol.81,pp.440–460, [53] V. Kulkarni, N. Tagasovska, T. Vatter, and B. Garbinato, ‘‘Generative
Nov.2015. modelsforsimulatingmobilitytrajectories,’’CoRR,vol.abs/1811.12801,
[30] W. Fedus, I. Goodfellow, and M. A. Dai, ‘‘MaskGAN: Better text 2018.[Online].Available:https://arxiv.org/abs/1811.12801
generationviafillinginthe______,’’Jan.2018,arXiv:1801.07736. [54] L. Kurup, M. Narvekar, R. Sarvaiya, and A. Shah, ‘‘Evolution of
[31] J.D.FernándezandF.Vico,‘‘Aimethodsinalgorithmiccomposition: neuraltextgeneration:Comparativeanalysis,’’inAdvancesinComputer,
Acomprehensivesurvey,’’J.Artif.Intell.Res.,vol.48,no.1,Oct.2013, CommunicationandComputationalSciences.Singapore:Springer,2021,
| Art.no.513582. |     |     |     |     |     |     |     | pp.795–804. |     |     |     |     |     |               |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | ------------- | --- |
| 47318          |     |     |     |     |     |     |     |             |     |     |     |     |     | VOLUME11,2023 |     |

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
[55] S.H.Lee,‘‘Naturallanguagegenerationforelectronichealthrecords,’’npj [80] S.Tulyakov,M.Liu,X.Yang,andJ.Kautz,‘‘MoCoGAN:Decomposing
Digit.Med.,vol.1,no.1,p.63,Dec.2018. motion and content for video generation,’’ in Proc. IEEE/CVF Conf.
[56] Z. Lin, M. Yin, S. Feygin, M. Sheehan, J.-F. Paiement, and Comput.Vis.PatternRecognit.,Jun.2018,pp.1526–1535.
A.Pozdnoukhov, ‘‘Deep generative models of urban mobility,’’ IEEE [81] C.G.TurhanandH.S.Bilge,‘‘Recenttrendsindeepgenerativemodels:
Trans.Intell.Transp.Syst.,2017. Areview,’’inProc.3rdInt.Conf.Comput.Sci.Eng.(UBMK),Sep.2018,
[57] Z.Liu,Z.Li,K.Wu,andM.Li,‘‘Urbantrafficpredictionfrommobility pp.574–579.
datausingdeeplearning,’’IEEENetw.,vol.32,no.4,pp.40–46,Jul.2018. [82] P.Vincent,H.Larochelle,Y.Bengio,andP.-A.Manzagol,‘‘Extractingand
[58] S.Mehri,K.Kumar,I.Gulrajani,R.Kumar,S.Jain,J.Sotelo,A.Courville, composingrobustfeatureswithdenoisingautoencoders,’’inProc.25thInt.
andY.Bengio,‘‘SampleRNN:Anunconditionalend-to-endneuralaudio Conf.Mach.Learn.(ICML),2008,pp.1096–1103.
generationmodel,’’inProc.5thInt.Conf.Learn.Represent.(ICLR),2017, [83] C.Vondrick,H.Pirsiavash,andA.Torralba,‘‘Generatingvideoswithscene
pp.1–11. dynamics,’’ in Proc. 30th Int. Conf. Neural Inf. Process. Syst. (NIPS).
[59] O.Mogren,‘‘C-RNN-GAN:Continuousrecurrentneuralnetworkswith RedHook,NY,USA:CurranAssociates,2016,Art.no.613621.
adversarialtraining,’’2016,arXiv:1611.09904. [84] X. Wang, S. Takaki, and J. Yamagishi, ‘‘Neural Source-filter-based
[60] B.Noori,‘‘Ananalysisofmobilebankinguserbehaviorusingcustomer waveform model for statistical parametric speech synthesis,’’ in Proc.
segmentation,’’inInt.J.GlobalBus.,vol.8,pp.55–64,Dec.2015. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP), May 2019,
[61] S.Norgaard,R.Saeedi,K.Sasani,andA.H.Gebremedhin,‘‘Synthetic pp.5916–5920.
sensordatagenerationforhealthapplications:Asuperviseddeeplearning [85] M. Wiese, R. Knobloch, R. Korn, and P. Kretschmer, ‘‘Quant GANs:
approach,’’ in Proc. 40th Annu. Int. Conf. IEEE Eng. Med. Biol. Soc. Deepgenerationoffinancialtimeseries,’’Quant.Finance,vol.20,no.9,
(EMBC),Jul.2018,pp.1164–1167. pp.1–22,2020.
[62] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, [86] C.Xiao,E.Choi,andJ.Sun,‘‘Opportunitiesandchallengesindeveloping
A.Graves,N.Kalchbrenner,A.Senior,andK.Kavukcuoglu,‘‘WaveNet: deeplearningmodelsusingelectronichealthrecordsdata:Asystematic
Agenerativemodelforrawaudio,’’2016,arXiv:1609.03499. review,’’J.Amer.Med.Inform.Assoc.,vol.25,no.10,pp.1419–1428,
[63] S.Oore,I.Simon,S.Dieleman,D.Eck,andK.Simonyan,‘‘Thistime Oct.2018.
withfeeling:Learningexpressivemusicalperformance,’’NeuralComput. [87] D. Xu, S. Yuan, L. Zhang, and X. Wu, ‘‘FairGAN: Fairness-aware
Appl.,vol.32,no.4,pp.955–967,Feb.2020. generativeadversarialnetworks,’’inProc.IEEEInt.Conf.BigData(Big
[64] A.OussidiandA.Elhassouny,‘‘Deepgenerativemodels:Survey,’’inProc. Data),Dec.2018,pp.570–575.
Int.Conf.Intell.Syst.Comput.Vis.(ISCV),Apr.2018,pp.1–8. [88] F.Xu,Z.Tu,Y.Li,P.Zhang,X.Fu,andD.Jin,‘‘Trajectoryrecovery
[65] K.Ouyang,R.Shokri,D.S.Rosenblum,andW.Yang,‘‘Anon-parametric from ash: User privacy is not preserved in aggregated mobility data,’’
generativemodelforhumantrajectories,’’inProc.27thInt.JointConf. inProc.26thInt.Conf.WorldWideWeb(WWW).Geneva,Switzerland:
Artif.Intell.,Jul.2018,pp.3812–3817. InternationalWorldWideWebConferencesSteeringCommittee,2017,
[66] M. Platzer and T. Reutterer, ‘‘Holdout-based empirical assessment of Art.no.12411250.
mixed-typesyntheticdata,’’FrontiersBigData,vol.4,p.43,Jun.2021. [89] P. Yadav, M. Steinbach, V. Kumar, and G. Simon, ‘‘Mining electronic
[67] S.Pouyanfar,S.Sadiq,Y.Yan,H.Tian,Y.Tao,M.P.Reyes,M.-L.Shyu, healthrecords(EHRs):Asurvey,’’ACMComput.Surv.,vol.50,no.6,
S.-C.Chen,andS.S.Iyengar,‘‘Asurveyondeeplearning:Algorithms, pp.1–40,Jan.2018.
techniques, and applications,’’ ACM Comput. Surv., vol. 51, no. 5, [90] A. Yahi, R. Vanguri, N. Elhadad, and N. P. Tatonetti, ‘‘Generative
pp.1–36,Sep.2018. adversarial networks for electronic health records: A framework for
[68] R. Prenger, R. Valle, and B. Catanzaro, ‘‘WaveGlow: A flow-based exploringandevaluatingmethodsforpredictingdrug-inducedlaboratory
generativenetworkforspeechsynthesis,’’inProc.IEEEInt.Conf.Acoust., testtrajectories,’’2017,arXiv:1712.00164.
SpeechSignalProcess.(ICASSP),May2019,pp.3617–3621. [91] A.Yale,S.Dash,R.Dutta,I.Guyon,A.Pavao,andK.Bennett,‘‘Privacy
[69] A. Radford, L. Metz, and S. Chintala, ‘‘Unsupervised representation preservingsynthetichealthdata,’’inProc.Eur.Symp.Artif.NeuralNetw.,
learning with deep convolutional generative adversarial networks,’’ Comput.Intell.Mach.Learn.(ESANN),2019,pp.465–470.
in Proc. 4th Int. Conf. Learn. Represent. (ICLR), San Juan, Puerto [92] L.-C. Yang and A. Lerch, ‘‘On the evaluation of generative models in
Rico, Y. Bengio and Y. LeCun, Eds., May 2016. [Online]. Available: music,’’NeuralComput.Appl.,vol.32,no.9,pp.4773–4784,May2020.
https://arxiv.org/abs/1511.06434 [93] H. Zen, A. Senior, and M. Schuster, ‘‘Statistical parametric speech
[70] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever, synthesisusingdeepneuralnetworks,’’inProc.IEEEInt.Conf.Acoust.,
‘‘Languagemodelsareunsupervisedmultitasklearners,’’OpenAIBlog, SpeechSignalProcess.,May2013,pp.7962–7966.
vol.1,no.8,p.9,2019. [94] H. Zen, K. Tokuda, and A. W. Black, ‘‘Statistical parametric speech
[71] L.Regenwetter,A.H.Nobari,andF.Ahmed,‘‘Deepgenerativemodelsin synthesis,’’SpeechCommun.,vol.51,no.11,pp.1039–1064,Nov.2009.
engineeringdesign:Areview,’’J.Mech.Des.,vol.144,no.7,Mar.2022, [95] B.Zhang,G.Kreitz,M.Isaksson,J.Ubillos,G.Urdaneta,J.A.Pouwelse,
Art.no.071704. andD.Epema,‘‘Understandinguserbehaviorinspotify,’’inProc.IEEE
[72] D.J.Rezende,S.Mohamed,andD.Wierstra,‘‘Stochasticbackpropagation INFOCOM,Apr.2013,pp.220–224.
andapproximateinferenceindeepgenerativemodels,’’inProc.31stInt. [96] H. Zhang, T. Xu, H. Li, S. Zhang, X. Wang, X. Huang, and D.
Conf.Mach.Learn.,vol.32,E.P.XingandT.Jebara,Eds.,Bejing,China, Metaxas,‘‘StackGAN:Texttophoto-realisticimagesynthesiswithstacked
Jun.2014,pp.1278–1286. generativeadversarialnetworks,’’inProc.IEEEInt.Conf.Comput.Vis.
[73] M.Saito,E.Matsumoto,andS.Saito,‘‘Temporalgenerativeadversarial (ICCV),Oct.2017,pp.5908–5916.
netswithsingularvalueclipping,’’inProc.IEEEInt.Conf.Comput.Vis.
(ICCV),Oct.2017,pp.2849–2858.
[74] T. Salimans, I. Goodfellow, W. Zaremba, V. Cheung, A. Radford, and
X.Chen,‘‘ImprovedtechniquesfortrainingGANs,’’inProc.30thInt.
Conf. Neural Inf. Process. Syst. (NIPS). Red Hook, NY, USA: Curran
PETER EIGENSCHINK received the B.S. and
Associates,2016,Art.no.22342242.
M.S. degrees in physics, with specialization in
[75] Y.ShavittandN.Zilberman,‘‘Ageolocationdatabasesstudy,’’IEEEJ.Sel.
computationalandgravitationalphysicsfromthe
AreasCommun.,vol.29,no.10,pp.2044–2056,Dec.2011.
University of Vienna, Austria. He is currently
[76] D.Shen,A.Celikyilmaz,Y.Zhang,L.Chen,X.Wang,J.Gao,andL.Carin,
pursuingthePh.D.degreeineconomicswiththe
‘‘Towardsgeneratinglongandcoherenttextwithmulti-levellatentvariable
models,’’2019,arXiv:1902.00154. Vienna University of Economics and Business
[77] F.Stahlberg,‘‘Neuralmachinetranslation:Areview,’’J.Artif.Intell.Res., (WUVienna).
vol.69,pp.343–418,Oct.2020. Since 2017, he has been an independent
[78] A.M.Tekalp,DigitalVideoProcessing,2nded.UpperSaddleRiver,NJ, IT consultant based in Vienna, Austria. From
USA:Prentice-Hall,2015. 2019 to 2021, he was a Research and Teaching
[79] L.Theis,A.V.D.Oord,andM.Bethge,‘‘Anoteontheevaluationof AssociatewithWUVienna.Hisresearchinterestsincludesyntheticdata-
generative models,’’ in Proc. Int. Conf. Learn. Represent., Apr. 2016. basedprivacyinconsumersanalyticsandalgorithmicdynamicpricingof
[Online].Available:https://arxiv.org/abs/1511.01844 perishableproductsingroceryretailing.
VOLUME11,2023 47319

P.Eigenschinketal.:DeepGenerativeModelsforSyntheticData:ASurvey
THOMASREUTTERERiscurrentlyaProfessorin CHANG SUN received the Ph.D. degree in
marketingandcustomeranalyticswiththeVienna data science and the M.S. degree in artificial
University of Economics and Business (WU intelligence from the University of Maastricht,
Vienna).Hisresearchinterestsincludeanalyzing, TheNetherlands.
modeling, and forecasting customer behavior in From 2017 to 2022, she was a Research
data-rich environments. In his research projects, and Teaching Associate with the University of
heemploysadvancedstatisticalormachinelearn- Maastricht, where she has been a Postdoctoral
ing methods to provide decision support for Researcher, since 2022. Her research interests
variousbusinessapplications.Hisrecentresearch includeprivacy-preservingmachinelearningand
interestsincludecustomervalueandrelationship syntheticdatageneration.
management,customerbaseanalysis,andcontentmarketingsupportedby
generativenaturallanguagemodels.
STEFAN VAMOSI received the B.S. and M.S.
degreesinphysics,withspecializationincomputa-
tionalphysics.HeiscurrentlypursuingthePh.D.
degreewiththeViennaUniversityofEconomics
andBusiness(WUVienna).
HeisalsoaResearchandTeachingAssociate
with WU Vienna. During his master’s thesis,
he was based with CERN, where he developed
asimulationsoftwareforananti-hydrogenbeam
experiment.PriortojoiningWU’sDoctoralPro-
gram, in May 2018, he gained professional experience in a consulting
firm.Hisresearchinterestsincludetime-seriesanalysis,behavioralcustomer
segmentation,anddatapredictionwithdeeplearningapproaches.
KLAUDIUSKALCHERreceivedtheB.S.andM.S.
RALF VAMOSI received the B.S. degree in degreesinstatisticsfromtheTechnicalUniversity
physics from the University of Vienna, Austria, ofViennaandthePh.D.degreeinmedicalphysics
whereheiscurrentlypursuingthePh.D.degreein fromtheMedicalUniversityofVienna,Austria.
computerscience. Heco-foundedthestartupMostlyAI,focusedon
Since 2017, he has been a Software Engineer syntheticdatagenerationforprivacyapplications,
withtheTechnicalUniversityofVienna,Austria. in2017.From2015to2016,hewasaPostdoctoral
From2019to2020,hewasaResearcherwiththe ResearcherwiththeMedicalUniversityofVienna.
ViennaUniversityofEconomicsandBusiness. Hisresearchinterestsincludesyntheticdatagener-
ationandethicalartificialintelligence.
47320 VOLUME11,2023