2104 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
| Towards |     | Human-Centered |     |         |     |     | Explainable |              |     | AI: | A   | Survey |     |
| ------- | --- | -------------- | --- | ------- | --- | --- | ----------- | ------------ | --- | --- | --- | ------ | --- |
|         |     | of User        |     | Studies |     | for | Model       | Explanations |     |     |     |        |     |
YaoRong ,TobiasLeemann ,Thai-TrangNguyen ,LisaFiedler ,PeizhuQian ,VaibhavUnhelkar ,
|     |     |     | TinaSeidel |     | ,GjergjiKasneci |     | ,andEnkelejdaKasneci |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
(SurveyPaper)
Abstract—ExplainableAI(XAI)iswidelyviewedasasinequa high-stakesdecision-makingtaskslikemedicaldiagnosis[106],
| non for ever-expanding |     | AI  | research. | A better | understanding |     | of            |        |         |        |        |        |           |
| ---------------------- | --- | --- | --------- | -------- | ------------- | --- | ------------- | ------ | ------- | ------ | ------ | ------ | --------- |
|                        |     |     |           |          |               |     | [107], [108], | credit | scoring | [109], | [110], | [111], | jurispru- |
theneedsofXAIusers,aswellashuman-centeredevaluationsof
|             |         |                    |             |             |              |           | dence [112],    | [113] | or recruiting | and | hiring          | decisions | [114],    |
| ----------- | ------- | ------------------ | ----------- | ----------- | ------------ | --------- | --------------- | ----- | ------------- | --- | --------------- | --------- | --------- |
| explainable | models  | are both           | a necessity | and         | a challenge. | In this   |                 |       |               |     |                 |           |           |
|             |         |                    |             |             |              |           | [115], However, | the   | behavior      | and | decision-making |           | processes |
| paper, we   | explore | how human-computer |             | interaction |              | (HCI) and |                 |       |               |     |                 |           |           |
AIresearchersconductuserstudiesinXAIapplicationsbasedon ofmodernAIsystemsareoftennotunderstandable,sotheyare
a systematic literature review. After identifying and thoroughly frequently considered black boxes. Deploying such black-box
analyzing97corepaperswithhuman-basedXAIevaluationsover modelspresentsaseriousdilemmaincertainsafety-criticaldo-
thepastfiveyears,wecategorizethemalongthemeasuredchar-
mains,forinstance,publichealthorfinance[116].Thisisdueto
| acteristics | of explanatory | methods, |     | namely | trust, understanding, |     |     |     |     |     |     |     |     |
| ----------- | -------------- | -------- | --- | ------ | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
thenecessityforatransparentandtrustworthyAIsystem,which
usability,andhuman-AIcollaborationperformance.Ourresearch
shows that XAI is spreading more rapidly in certain application is required by both practitioners (to gain better insights into
domains, such as recommender systems than in others, but that systemfunctioning)andendusers(torelyonmodeldecisions).
userevaluationsarestillrathersparseandincorporatehardlyany Methods toincrease the interpretability and transparency of
insightsfromcognitiveorsocialsciences.Basedonacomprehensive
anAIsystemaredevelopedintheresearchareaofExplainable
discussionofbestpractices,i.e.,commonmodels,designchoices,
|     |     |     |     |     |     |     | AI(XAI).Specifically, |     | human-centered |     | XAI,whichaddresses |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | -------------- | --- | ------------------ | --- | --- |
andmeasuresinuserstudies,weproposepracticalguidelineson
designing and conducting user studies for XAI researchers and the importance of human stack-holders to the AI systems, has
practitioners. Lastly, this survey also highlights several open re- beenproposedanddiscussedsince[117],[118].Whileahuge
search directions, particularly linking psychological science and numberofmodelexplanationsareavailable,thequestionofhow
human-centeredXAI.
|     |     |     |     |     |     |     | to transparently | evaluate |     | their quality | is still | an  | open research |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | --- | ------------- | -------- | --- | ------------- |
Index Terms—Explainable AI (XAI), human-centered XAI, question,andhence,extensivelystudiedinrecentyears.Apopu-
explainableML,userstudy,human-AIinteraction.
lartaxonomyofevaluationstrategiesforXAImethodsproposes
threecategories:functionally-groundedevaluation,application-
|     |     |                 |     |     |     |     | grounded                    | evaluation, | and | human-grounded |     | evaluation  | [119]. |
| --- | --- | --------------- | --- | --- | --- | --- | --------------------------- | ----------- | --- | -------------- | --- | ----------- | ------ |
|     |     | I. INTRODUCTION |     |     |     |     |                             |             |     |                |     |             |        |
|     |     |                 |     |     |     |     | While functionally-grounded |             |     | measures       | do  | not require | human  |
ARTIFICIAL Intelligence (AI) is driving digital transfor- labor,theothertwoinvolvehumansubjectsandaremorecostly
| mation | and | is already | an integral | part | of various | every- |     |     |     |     |     |     |     |
| ------ | --- | ---------- | ----------- | ---- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
toconduct.
day technologies. Recent developments in AI are essential to Many functionally-grounded measures have been proposed
progress in fields such as recommendation systems [97], [98], toevaluateXAIalgorithms(see[120]forreview),however,the
[99],autonomousdriving[100],[101],[102]orrobotics[103],
|     |     |     |     |     |     |     | difficult | comparability | between | different |     | automatic | evaluation |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ------- | --------- | --- | --------- | ---------- |
[104], [105]. Moreover, AI’s success story has not excluded measuresisacommonproblem[121],[122].Anotherdrawback
|     |     |     |     |     |     |     | of automated  | measures | is          | that there | is no        | guarantee | that they     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | -------- | ----------- | ---------- | ------------ | --------- | ------------- |
|     |     |     |     |     |     |     | truly reflect | humans’  | preferences |            | [40], [123]. |           | Consequently, |
Manuscriptreceived3February2023;revised26October2023;accepted4
userstudiesinXAI,especiallywhenmovingtowardsreal-world
November2023.Dateofpublication13November2023;dateofcurrentversion
6March2024.RecommendedforacceptancebyM.Cheng.(Corresponding
products,areinevitableifonewishestotestmoregeneralbeliefs
author:YaoRong.)
ofthequalityofexplanations[16].However,onlyasmallportion
| Yao Rong,          | Tina | Seidel, Gjergji | Kasneci, | and           | Enkelejda | Kasneci are |             |        |            |          |          |     |            |
| ------------------ | ---- | --------------- | -------- | ------------- | --------- | ----------- | ----------- | ------ | ---------- | -------- | -------- | --- | ---------- |
|                    |      |                 |          |               |           |             | (about 20%) | of XAI | evaluation | projects | consider |     | human sub- |
| with the Technical |      | University of   | Munich,  | 80335 Munich, | Germany   | (e-mail:    |             |        |            |          |          |     |            |
yao.rong@tum.de; tina.seidel@tum.de; gjergji.kasneci@tum.de; enkelejda. jects[120].Thereexisteffortsindevelopingtaxonomiesorintro-
kasneci@tum.de).
ducingthedefinitionsorimplicationsofdifferenthuman-centric
| Tobias Leemann, |     | Thai-Trang | Nguyen, and | Lisa | Fiedler are | with the Uni- |     |     |     |     |     |     |     |
| --------------- | --- | ---------- | ----------- | ---- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
versity of Tübingen, 72076 Tübingen, Germany (e-mail: tobias.leemann@ evaluations[124],[125],[126],buttherecentgenerationofuser
uni-tuebingen.de; thai-trang.nguyen@student.uni-tuebingen.de; lisa.fiedler@ studiesandtheirfindingshavenotbeensystematicallydiscussed
student.uni-tuebingen.de).
|     |     |     |     |     |     |     | yet.Moreover,Yangetal. |     |     | [127]pointoutthatXAIisgrowing |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | ----------------------------- | --- | --- | --- |
PeizhuQianandVaibhavUnhelkararewiththeRiceUniversity,Houston,
TX77005USA(e-mail:pq3@rice.edu;vaibhav.unhelkar@rice.edu). separatelyandtreateddifferentlyindifferentcommunities(e.g.,
This article has supplementary downloadable material available at machinelearningandHCI).Hence,effectiveguidanceinXAI
https://doi.org/10.1109/TPAMI.2023.3331846,providedbytheauthors.
DigitalObjectIdentifier10.1109/TPAMI.2023.3331846 user study design is crucial to better let both XAI algorithm
©2023TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.Formoreinformation,see
https://creativecommons.org/licenses/by/4.0/

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2105
TABLEI
OVERVIEWOFTHECOREPAPERSCONTAININGUSERSTUDIESINXAIGROUPEDBYCATEGORIESOFMEASUREMENTSASSOMECOREPAPERSASSESS
QUANTITIESBELONGINGTOSEVERALGROUPS,ASINGLEPAPERCANALSOBELISTEDAMONGMULTIPLEGROUPS
andapplicationdesignersrecognizetheusers’realneeds.This Our study highlights under-investigated areas in the context
workaimstobridgethisresearchgapinmodernXAIuserstudy ofcurrentuser-centeredXAIresearchsuchascognitiveorpsy-
designbydistillingpracticalguidelinesforuserstudiesthrough chological sciences through data-driven bibliometric analysis.
acomprehensiveandstructuredliteraturereview. Together with our proposed guidelines, we believe that this
Therefore, we reviewed highly relevant papers that include workwillbenefitXAIpractitionersandresearchersfromvarious
user studies from top-tier HCI and XAI venues. Specifically, disciplines and will help to approach the overarching goal of
we included the recent five years of CHI, IUI, UIST, CSCW, human-centeredXAI.
FA(cc)T,ICML,ICRL,NeurIPS,andAAAI.Asweaimatana-
lyzinghumanuserevaluationofadvancedmodelexplanations,
weransearchqueriesinvolvingkeywordsfromthetwogroups II. RELATEDWORK
| “explainable | AI” | and “user | study”, | as  | listed | in the | Table II. |      |             |                |     |         |                |
| ------------ | --- | --------- | ------- | --- | ------ | ------ | --------- | ---- | ----------- | -------------- | --- | ------- | -------------- |
|              |     |           |         |     |        |        |           | As a | vast amount | of explanation |     | methods | have been pro- |
We selected the papers containing at least one keyword from posed,manyresearchersseekasystematicoverviewoftheever-
| each group, | resulting | in  | over one | hundred | papers. | Then, | we  |     |     |     |     |     |     |
| ----------- | --------- | --- | -------- | ------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
growingfieldofXAI.In[128],[129],[130],[131],[132],[133],
thoroughly studied these papers and filtered out papers that theauthorsaimtocovermanyfacetsofXAItechnologiesrang-
| did not | fulfill the | criteria: | (1) | deploying | explainable |     | models |     |     |     |     |     |     |
| ------- | ----------- | --------- | --- | --------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
ingfromproblemdefinitions,goals,AI/MLmodelexplanations
| or techniques | and | (2) conducting |     | an  | assessment | with | human |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | --- | ---------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
toevaluationmeasures,whilein[134]theauthorsemphasizethe
subjects.Weidentifiedatotalof97corepapersforthissurvey researchtrendsandchallengesinHuman-Computer-Interaction
(seeTableIforanoverviewofcorepaperswithrespecttotheir
|     |     |     |     |     |     |     |     | (HCI) applications. |     | A large | body | of XAI | surveys focuses |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------- | ---- | ------ | --------------- |
measuredquantitiesinuserstudies).Basedonthesecorepapers, mainly on the interpretability of a particular family of models
weperformedacomprehensiveanalysistofilltheresearchgap
andcorrespondingexplanationtechniques.Forinstance,[135],
| by offering | a systematic |     | overview | of  | user studies | in  | XAI. We |     |     |     |     |     |     |
| ----------- | ------------ | --- | -------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- |
[136],[137]investigateexplanationsforDeepNeuralNetworks
highlightthemaincontributions: (DNNs),wheremodelsoftentakeimagesasinput[135],[136].
1) Toofferanoverviewofthefoundationalworkofuserstud-
|     |     |     |     |     |     |     |     | Joshi et | al. [137], | however, | provide | an extensive | review for |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | -------- | ------- | ------------ | ---------- |
iesinXAI,weinvestigatedreferencesofall97corepapers DNNs with multimodal input for instance that of joint vision-
inadata-drivenmanner.Likewise,weanalyzedfollow-up language tasks. Causal interpretable models are gaining more
| works | building | on  | these core | papers | (identified |     | through |                                   |     |     |     |                         |     |
| ----- | -------- | --- | ---------- | ------ | ----------- | --- | ------- | --------------------------------- | --- | --- | --- | ----------------------- | --- |
|       |          |     |            |        |             |     |         | attentionrecentlyandMoraffahetal. |     |     |     | [138]providealiterature |     |
citationsofcorepapers)torevealthefieldsimpactedby reviewforcausalexplanations.Asystematicliteraturereviewon
XAIuserevaluations(SectionIII).
|     |     |     |     |     |     |     |     | explanations | for | advice-giving |     | systems is conducted | in [139]. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | -------------------- | --------- |
2) WepresentasummaryofthedesigndetailsinXAIuser Among these surveys focusing on general XAI technologies,
studies with particular focus on the deployed models evaluationmeasuresareonlybrieflyexamined.
andexplanationtechniques,experimentaldesignpatterns,
|     |     |     |     |     |     |     |     | One challenge |     | in XAI | research | is to evaluate | and com- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------ | -------- | -------------- | -------- |
participantsaswellasconcretemeasures,providinginspi- pare different explanation methods, due to the multidisci-
rationofhowtocollecthumanassessment(SectionIV).
|     |     |     |     |     |     |     |     | plinary concepts |     | in interpretability/explainability |     |     | [119], [120], |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------------------------------- | --- | --- | ------------- |
3) Wediscusstheimpactofusingexplanationsondifferent
|     |     |     |     |     |     |     |     | [140]. Evaluation |     | measures | can | be divided | into two groups: |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | -------- | --- | ---------- | ---------------- |
aspects of user experience (Section V), which can serve human-grounded measures that rely on human subjects and
| as  | an overview | of  | the effectiveness |     | of  | the current | XAI |                       |     |         |     |                      |         |
| --- | ----------- | --- | ----------------- | --- | --- | ----------- | --- | --------------------- | --- | ------- | --- | -------------------- | ------- |
|     |             |     |                   |     |     |             |     | functionally-grounded |     | metrics |     | that can be computed | without |
technologyandasummaryofthestate-of-the-art. humansubjects[119],[120].Manyresearchersseeksolutionsto
4) Basedontheexamineduserstudydetailsandtheirbest-
evaluateexplanationsautomatically.Acomprehensiveliterature
practicefindings,wesynthesizeguidelinesfordesigning
reviewwithafocusonthesefunctionally-groundedevaluation
aneffectiveuserstudyforXAI(SectionVI). methods (without human subjects) can be found in [120]. Ex-
| 5) Beyond | the | user | study | design, | we discuss |     | potential |     |     |     |     |     |     |
| --------- | --- | ---- | ----- | ------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- |
plainabilityisaninherentlyhuman-centricproperty,therefore,
paradigms of AI systems understanding humans in the the research community should and has started to recognize
| context | of  | e.g., theory | of  | minds, | as well | as other | future |          |                    |     |     |                  |            |
| ------- | --- | ------------ | --- | ------ | ------- | -------- | ------ | -------- | ------------------ | --- | --- | ---------------- | ---------- |
|         |     |              |     |        |         |          |        | the need | for human-centered |     |     | evaluations when | working on |
researchdirections(SectionVII).
XAI[119],[141].

2106 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
Fig.1. Roadmapofourliteratureanalysis.Wefindoutthefoundationalworksofcorepapersandtheirapplicationdomainsusingadata-drivenmethodintroduced
inSectionIII.Threemainresearchquestionsinuserstudiesaredistilledfromcorepapers.MethodsrelatedtomeasuresofeachcategoryarediscussedinSection
IV,andfindingsoftheresearchquestionsaresummarizedinSectionV.Basedonthefindings,weproposefuturedirectionstofurtherpromotehuman-centered
XAIinSectionVII.Wedistillimportantmessagesinthisfigure,butrefertothediscussioninthecorrespondingsectionsformoredetails.
Forinstance,ChromikandSchuessler[125]proposeataxon- information on experimental design. To this end, we present
omyonXAIevaluationsinvolvinghumans.Mohsenietal. [126] a practical guideline in user study design, which can be used
summarize four groups of human-related evaluation metrics: asastartingpointforfutureexplorationofhuman-centricXAI
| mental          | model (e.g., | user’s           | understanding |     | of          | the | model), user | applications. |     |     |     |     |     |
| --------------- | ------------ | ---------------- | ------------- | --- | ----------- | --- | ------------ | ------------- | --- | --- | --- | --- | --- |
| trust, human-AI |              | task performance |               | and | explanation |     | usefulness   |               |     |     |     |     |     |
and satisfaction (i.e., user experience). Hoffman [124] places III. METHODOLOGY
| more focus        | on    | psychometric |             | evaluations | by             | proposing  | a con-    |             |                       |        |               |         |            |
| ----------------- | ----- | ------------ | ----------- | ----------- | -------------- | ---------- | --------- | ----------- | --------------------- | ------ | ------------- | ------- | ---------- |
|                   |       |              |             |             |                |            |           | To analyze  | the collected         | papers | related       | to user | studies on |
| ceptual           | model | of the       | XAI process |             | and specifying |            | four key  |             |                       |        |               |         |            |
|                   |       |              |             |             |                |            |           | XAI, we     | first categorize them | into   | four groups   | based   | on their   |
| components        | that  | should       | be          | evaluated:  | explanation    |            | goodness  |             |                       |        |               |         |            |
|                   |       |              |             |             |                |            |           | objectives. | From these studies,   | we     | distill three | main    | research   |
| and satisfaction, |       | (user’s)     | mental      | models,     |                | curiosity, | trust and |             |                       |        |               |         |            |
questionsconcerningtheeffectsofmodelexplanationsoneach
| performance. | Beyond |     | assessing | evaluation |     | methods, | XAI ap- |     |     |     |     |     |     |
| ------------ | ------ | --- | --------- | ---------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- |
objective.Wethensummarizethemethodsusedinthesestudies
| plications  | are designed |        | to eventually |        | support | decision-making |              |                     |                   |           |                   |      |          |
| ----------- | ------------ | ------ | ------------- | ------ | ------- | --------------- | ------------ | ------------------- | ----------------- | --------- | ----------------- | ---- | -------- |
|             |              |        |               |        |         |                 |              | to quantify         | these objectives. | Important | findings          | from | the pa-  |
| and benefit | end          | users. | A recent      | review | by      | Lai             | et al. [142] |                     |                   |           |                   |      |          |
|             |              |        |               |        |         |                 |              | pers are discussed, | and we            | propose   | future directions |      | based on |
considersstudiesoncollaborativeHuman-AIdecision-making,
thesefindings.Additionally,weexaminethefoundationalworks
| which may | include | AI  | agents | providing | explanations. |     | Success |     |     |     |     |     |     |
| --------- | ------- | --- | ------ | --------- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- |
uponwhichtheseuserstudiesarebased(i.e.,theirreferences)
inhuman-AIdecision-makingtaskscanbeseenasoneamongst
|     |     |     |     |     |     |     |     | and the follow-up | papers that | cite them, | shedding |     | light on the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ----------- | ---------- | -------- | --- | ------------ |
manyotherwaystoevaluatetheeffectofexplanations.Ferreira
foundationalworksandemergingtrendsinhuman-centeredXAI
| andMonteiro[143]presentareviewoftheuserexperience |     |     |     |     |     |     | of  |     |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
studies.Fig.1presentsaroadmapofouranalysis.
XAIapplicationstoanswerwhousesXAI,why,andinwhich
|     |     |     |     |     |     |     |     | In this | section, we first | describe | the criteria | used | for their |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------------- | -------- | ------------ | ---- | --------- |
context(what+when)theexplanationispresented.
categorization.Wethendiscussthefoundationalandapplication
| Closer | to our | focus | on user | studies | concerning |     | XAI, Liao |     |     |     |     |     |     |
| ------ | ------ | ----- | ------- | ------- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- |
domainsofthesepapers,providingabroaderviewbeforediving
| etal. [141]studyuserexperiences |     |     |     |     | withXAItoreveal |     | pitfalls |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
intotheirdetailedanalysis.
| of existing | XAI | methods, | underscoring |     | the | important | role of |     |     |     |     |     |     |
| ----------- | --- | -------- | ------------ | --- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- |
humansinXAIdevelopment.AssuggestedbyDoshi-Velezand
A. CategorizationofUser-StudyObjectives
| Kim [119], | a human-subject |     |     | experiment | needs | to  | be designed |     |     |     |     |     |     |
| ---------- | --------------- | --- | --- | ---------- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- |
sophisticatedly to reduce confounding factors. In contrast to Sincethecorepaperscovervariousfactorsofmodelexplana-
previous surveys on XAI, we aim to provide XAI researchers tions, we decided to categorize the core papers into different
| and practitioners |     | with | a comprehensive |     | overview |     | of the re- |             |                    |               |     |     |              |
| ----------------- | --- | ---- | --------------- | --- | -------- | --- | ---------- | ----------- | ------------------ | ------------- | --- | --- | ------------ |
|                   |     |      |                 |     |          |     |            | clusters to | better study their | commonalities |     | and | differences. |
searchquestionsexploredinuserstudies,alongwiththorough In[119],interpretabilityinthecontextofMLsystemsisdefined

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2107
astheabilitytoexplainorpresentmodelpredictionsinunder- These are a frequent subject of study in works measuring un-
standabletermstoahuman.Beyondfosteringcomprehension, derstandingandusability.Additionally,convolutionalnetworks,
theauthorsarguethatinterpretabilitycanassistinqualitatively which are commonly employed in experiments, use tools like
ascertainingwhetherotherdesiderata,suchasusabilityandtrust GradCAM[148]andvarioussaliencymapstogeneratemodel
aremet.Duringaprofoundstudyoftherelevantliteraturethat explanations.Notably,manyresearchpapersappearwithinthe
waspreviouslyselected,weidentifiedfoursensiblecategories, domainofrecommendersystems,becausemanyXAIuserstud-
thatarederivedfromtheconsidereddependentvariablesinuser ies are conducted in the context of recommendation solutions.
studies (desiderata of interpretability). These four categories he EU’s General Data Protection Regulation (GDPR) [149] is
aretrust,understanding,usability,andhuman-AIcollaboration frequentlymentionedincorepapersduetotheongoingdebate
performance. In Table I, the studied papers are categorized ontherighttoexplanation”[150].Thisdebatehassignificantly
according to the measured quantities. As each measure can influencedtheshiftinmodernAIsystemstowardsexplainability.
usually be assigned to only one of these categories, we found While the ultimate consumers of model explanations are hu-
thisdistinctiontobeintuitive. mans, well-established research domains that focus on human
These categories reflect different functionalities (goals) of understanding are underrepresented. For instance, only a few
XAI. As interpretability is defined as “the ability to explain papers related to “Cognition” are cited compared to those on
or to present in understandable terms to a human.”, humans’ otheralgorithmictopics.Millecampetal. [18]suggestenhanc-
“understanding” is the direct goal of XAI. To be concrete, ing XAI theory with insights from social sciences, including
understanding in the context of interacting with an ML model cognitivescienceandpsychology.Giventhescantreferencesto
refers to a user’s grasp or “mental model” of how the model psychology,itappearsthatonlyahandfulofXAIuserstudies
operates,andthisknowledgegrowsfromusingthesystemand delve into evaluating XAI from a psychological standpoint.
fromclearexplanationsaboutit[141].“Usability”iscommonly We highlight a nascent research domain of XAI frameworks
studied in human-computer interaction [144], which is one of based on human cognition and behavior theories [141]. This
the desiderata of XAI [119]. According to [145], usability is theoretical guidance can also offer conceptual tools for better
the extent to which users can utilize a product to successfully, evaluating XAI from user perspectives. More details about
efficiently, and satisfactorily accomplish their intended objec- common references can be found in Appendix A.1, available
tives.Thus,thiscategoryencompassesuserstudiesthatemploy online.
modelexplanationstosupportusersinachievingspecifictasks.
Inusability,differentaspectsaremeasured,forinstance,whether
C. ImpactofUserStudies
thesystemiseasytouseorhowmuchcognitiveloaditrequires.
Theaspect“undesired behavior detection” relatestousecases Fig. 1 presents applications that make use (and thus are the
where explanations uncover model discriminatory behaviors, consumers) of the findings from core papers. We noticed that
such as the utilization of undesired features. “Trust” in AI is studies on user understanding and trust span a wide range of
summarized as a combination of the user’s confidence in a applications. For example, trust is frequently addressed in the
model’s accuracy, a personal comfort level with understand- contextsofmedicaldiagnosisandtransportation,indicatingits
ing and using it, and the willingness to let the model make significance in high-risk scenarios. Recommendation systems
decisions[140].Itencompassesmorerequirements.Human-AI emerge as a primary focus in follow-up works. Papers on
collaborationperformanceisrelatedtoscenarioswheretheAI usability have a significant impact on fields like data visual-
systemprovidesitspredictions,buthumansretainthefinaldeci- ization, software development, and education. In these areas,
sions[89].Inthiscase,modelexplanationsaredeployedtoreach models frequently serve as tools to ease the burden on end
a performance superior to that of the AI system or the human users. Human-AI collaboration measures particularly promote
decision-maker alone. These categories cover different depen- the further development of robotics and or natural language
dentvariablesofinterestintherevieweduserstudies,primarily processing. The prominence of recommendation systems in
relatedtohowXAImethodsfunction.Thesefunctionsmainlytie both foundational works and their impact implies that XAI is
tothemodels’reasoningandknowledgerepresentation.Awider an integral component of contemporary recommendation sys-
perspectiveonXAI,whichassessesgeneralizationorrobustness, tems.Acomprehensiveoverviewofthefundamentalworksand
remains an important field for future exploration through user application domains can be found in Appendix A.1, available
studies. online.
B. FoundationsofUserStudies IV. COMPREHENSIVEUSERSTUDYANALYSIS
Based on a data-driven bibliometric analysis of the refer- In this section, we present details of the covered XAI user
ences in core papers, we highlight significant research topics studies.WefirstintroducesomecommonlyusedAImodelsand
within the “Foundational Domain” in Fig. 1. It is evident that explanation techniques (Section IV-A), followed by a discus-
modelexplanationsandinterpretabilityarepivotalcomponents. sion of application domains and measures with respect to the
This includes papers that introduce explanation methods such fourmeasuredquantities.Theexperimentaldesigns,aswellas
as LIME [146], SHAP [147], and other attribution methods. analysistoolsarepresentedinSectionIV-C.

2108 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
TABLEII and LIME (Local Interpretable Model-Agnostic Explana-
KEYWORDSFOROURPAPERSEARCHQUERY
tions [146]). There is a clear differentiation between local,
instance-wise,explanationsandglobalexplanationsthatapply
tothemodelinitsentirety.Forinstance,theweightsofalinear
model have a global scope. This differentiation is common
among these feature-based explanations, where most of the
papersusinglocalexplanations.Otherpopularexplanationtypes
are example-based explanations, counterfactual explanations,
which aim at providing actionable suggestions for attaining a
user-preferredpredictionbychangingcertaininputfeatures,and
concept-based explanations, which use meaningful high-level
TABLEIII conceptssuchasobjectsorshapestoexplainaprediction.
MODELSANDEXPLANATIONSINCOREPAPERS Besidesthesefourmaintypesofexplanations,thereareother
explanationssuchasrules[11],[88]orgamestrategies[7],[10]
whenAIplaysgames.Moredetailsaboutconcretemodelsand
explanationscanbefoundinAppendixB,availableonline.
B. Measurements
Theeffectivenessofexplanationscanbecharacterizedfrom
severalangles.Wespecificallyidentifiedthecategoriesoftrust,
understanding, usability, and human-AI collaboration perfor-
mance. In this section, we give an overview of the contexts in
whicheachofthesevariablesisstudiedandthemeasuresused
toquantifythem.
1) Trust: User trust is studied in decision-making applica-
tionssuchasimageclassification[13],[17],(review)deception
detection [25] or loan approval [27]. Besides decision mak-
ing,[5],[8],[16],[18],[19],[23]studyusertrustinthedomain
ofrecommendation systems.Whether explainable MLmodels
canincreaseusertrustinthemedicaldomainisstudiedin[1],
[6], [9]. Moreover, Colley et al. [3] measure user trust in an
autonomousdrivingapplicationwithandwithoutexplanations.
Trustmeasuresusedinmuchoftheexistingresearchcanbe
dividedintotwogroups:self-reportedandobservedtrust[155].
Self-reported trust is commonly measured by asking users to
fill out questionnaires whereas observed trust is quantified by
humans’agreementwiththemodel’sdecisions.InTableIIIin
Appendix,availableonline,trustmeasuresinthesetwogroups
A. ModelsandExplanations
arelisted.Theagreementrateofuserswiththemodeldecisions
As our selected core papers comprise a large spectrum of iscommonlyused[9],[11],[12],[25]asameasureofobserved
AI models, data modalities, and explanation approaches, we trust. Parallel to observed trust measurement, van der Waa
initially list the models and explanation techniques deployed etal. [156]ascribetheuser’salignmentbehaviorstothepersua-
alongwiththecorrespondingcorepaperreferencesinTableIII. sivepowerofmodelexplanations,i.e.,thecapacitytoconvince
It presents the utilization of explanation types in columns and userstofollowmodeldecisions despitethecorrectness.Asan
modeltypesinrows.Theexplanationmethodsusedisorganized extension, trust calibration is defined based on this measure.
according the the taxonomy by Molnar [151]. First, there are Forexample,ahighagreementratetowronglymadedecisions
intrinsicallyinterpretablemodels,alsoknownaswhite-boxmod- represents overtrust, while a low agreement rate to correct
els.Forinstance,white-boxmodelsincludedecisiontreesand decisionsmeansundertrust[12].Inself-reportedmeasurements,
linearmodels.Second,thereareblack-boxmodelsthatprovide researcherseitherutilizewell-developedquestionnairesorself-
no parameter access or are too complex to be explained in a designedones,withtheexceptionof[4]whichconductsasemi-
human-understandable way [152]. These include ensembling structuredinterviewtoexploreuseropinions.Severalworks[6],
techniquessuchasRandomForestsorneuralmodels. [11], [13], [16], [17], [18], [19], [24], [27] propose their own
As for explanation techniques, we identified five key types questionnaires.Amongthese,asubgroup[13],[16],[18],[19],
in the scope of the surveyed papers (rows of Table III). [24] simply asks users to rate a single statement such as “I
Most frequently used are feature-based (attribution) explana- trust the system’s recommendation/decision”, which is named
tions,forinstance,SHAP(Shapleyadditiveexplanations[147]) as one-dimensional trust by [8]. When deploying previously

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2109
proposed questionnaires [2], [3], [5], [7], [8], [10], [21], [22], failure prediction measures the accuracy of users’ prediction
[23], [157], Trust in Automation [158] is the most commonly whenthemodelpredictioniswrong.
used one, in which the underlying constructs of trust between SubjectiveUnderstanding:Besidestheobjectiveunderstand-
humanandcomputerizedsystemsareexplored. ingwhichissupportedbyperformanceindicators,understand-
2) Understanding: An important goal of explanation tech- ingofamodelmaybesubjective,i.e.,itmaydependonauser’s
niques is to foster users’ understanding of complex ML sys- own perception. The most commonly used applications that
tems. An important separation has to be made between users’ measuresubjectiveunderstandingarevariousrecommendation
perceivedunderstandingandtheiractualcomprehensionofthe systemsetups[16],[33],[34],[38].
underlyingmodel,asthetwooftendonotagree[35],[40].Cheng Most of the works assess the subjective understanding of a
etal. [22]explicitlydifferentiatebetweenobjectiveunderstand- user with a post-task questionnaire. Guo et al. [7] adapted a
ingandself-reportedunderstanding,whichwetermsubjective popularquestionnairedesignedforrecommendationsystemsby
understanding in this work. While subjective understanding is Knijnenburgetal. [160],whileBelletal.[39]accommodated
usually measured through questionnaires, measuring objective thequestionnairewhichoriginallyintendedtomeasurethein-
understandingrequiresaproxytaskwheretheusers’understand- telligibility of differenet explanations by Lim and Dey [161].
ingisputtoatest.Additionally,userstudiescanberuntoassess On the other hand, agreement to simple subjective statements
howwelluserscanunderstandtheexplanationitself(andnotthe such as “I understand this decision algorithm” [22], “I un-
underlyingmodel).Thiscanbeanimportantsanitycheckandis derstandhowtheAI...”[13],[17]or“Theexplanation(s)help
particularlyusedinthedomainofconceptualexplanations[62], metounderstand...”[33]canbecollectedtoassesssubjective
[159],wheretheintelligibilityofconceptsneedstobeverified. understanding.
We refer to the third category as understanding of explana- 3) Usability: UsabilityisakeyconcernofeveryHCIsystem
tionsbutdeferitsdetailedfindingstoAppendixC.3,available andthusappliestoalmostalldomains.Thisisreflectedinthe
online. surveyed papers, where usability is studied in a wide range
ObjectiveUnderstanding:Worksinthesubdomainofobjec- of setups and contexts. We also include application-specific
tive understanding deploy proxy tasks to verify users’ under- performancemeasuresinthiscategory.
standingofamodel’sinnerworkings.Themostcommonlycon- Basedonthemeasurementsintheuserstudies,werefinedus-
sidereddomaininworksonunderstandingisfinance[35],[39], abilityintomeasuresofhelpfulness,workload(cognitiveload),
[40],[47],[48],[49],[53]followedbyimageclassification[13], satisfaction, ease of use and detecting undesired behaviors of
[21],[52].Oneofthemostcriticaldesignchoiceswhenassessing thesystem,asshowninTableI.Toassessworkload(cognitive
objectiveunderstandingistheselectionofasuitableproxytask. load),NASA-TLXscale[162]isusedin[3],[6],[16],[21],[66],
Doshi-VelezandKim[119]arguethatthetaskshould“maintain whileAbduletal. [48]measurecognitiveloadbycapturingthe
theessenceofthetargetapplication”thatisanticipated.Oneof log-reading time of memorizing the explanation. Most of the
the most prominent tasks is forward simulation [119], [140]. worksuseself-designedquestionnairesorstatementstomeasure
Thistaskdemandssubjectsthataregivenaninputtosimulate, satisfaction[6],[16],[18],[19],[29],[30],[69],[70],however,
i.e.,predict,themodel’soutput.Theextenttowhichparticipants theExplanationSatisfactionScale[163]canbedeployedasan
can successfully provide the model’s output is also referred to established alternative [1], [47]. Helpfulness can be assessed
assimulatability[140].However,scholarshavedesignedmany bysimplyaskingforsubjective ratings oftheexplanations for
more tasks to quantify understanding and applied them across accomplishing a specific task [13], [46], [56], [65], [67], [68].
avarietyofdatamodalities(cf.Table2inAppendix,available Colleyetal. [3]useanadaptedversionoftheSystemUsability
onlineforanexhaustivelisting). Scaleproposedin[164].
We briefly describe other common tasks below. A special Using model explanations to audit models is one purpose
variant of forward simulation is called relative simulation. In of explainability [129]. Some of the surveyed works study
thistask,userspredictwhichexampleoutofapredefinedchoice howmodelexplanationscanassistusersindetectingundesired
will have the highest prediction score (or class probability). A behaviors of models. These issues mainly include (perceived)
manipulationorcounterfactualsimulationtask[119]asksusers unfairnessinthemodeldecision-making[38],[74],[78],[79],
to manipulate the input features in such a way that a certain biases in models [72] or features [57], and wrong decisions
modeloutcome(counterfactual)isreached.Users’performance (failures)[24]inthestudiedpapers.Adetailedsummaryoftypes
onthistaskcanbeusedasaproxyfortheirunderstanding.Lip- of undesired behaviors is listed in Table VI. In the undesired
ton[140]pointedoutthatsimulatabilitycanonlybeareasonable behaviordetection,theeffectivenessofexplanationsisevaluated
measure,ifthemodelissimpleenoughtobecapturedbyhumans byobjectiveperformancemeasures,suchasthenumberofbugs
andthatsimplertasksarerequiredotherwise.Anexamplecould identified [71], the share of participants that identify a certain
be a feature importance query, where users have to tell which bias[57,FirstExperiment]orbythedeviationsbetweenmodel
features are actually used by the model. A directed and more predictions and human predictions for unusual samples [53].
localversionofthistaskismarginaleffectsqueries,wherethe Theperceptionofusersregardingfairtreatmentbyasystemhas
subjectspredicthowchangesinagiveninputfeaturewillaffect primarily been researched in high-stakes applications such as
theprediction(e.g.,“DoesincreasingfeatureXleadtoahigher grantingloans[27]orgrantingbailforcriminaloffenders[73],
predictionofY beingclass1?”).Becauseexplanationsshould [74],[75].Forexample,[73],[74],[75]investigatethefairness
allow the identification of weaknesses in models, the task of ofCOMPAS,acommercialcriminalriskestimationtoolthatwas

2110 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
TABLEIV
EXPERIMENTALDESIGNSINCOREPAPERS
|     |     |     |     |     |     |     | Fig.2. Distributionofparticipantnumbersinthesurveyeduserstudiesby |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
designandparticipanttype(eachbarrepresentsonestudy).Per-designmeans
areindicatedinbold.
usedintheUStohelpmakejudicialbaildecisions.Itisalsocon-
sideredineverydayuse-casessuchasnews[38]andmusic[77]
recommendations, or possible career suggestions [76], where Mechanical Turk. For instance, Ooge et al. [8] use 12 school
a bias in the underlying system can be to the detriment of the studentspercondition.Someauthorsplaceparticularemphasis
user.Astheassessmentoffairnessisaverysubjectivematter, onparticipantsbeingsimilartotheaveragedemographic[73],
[75].
questionsregardingperceivedfairnessareprevalent,e.g.,“how
the software made the prediction was fair” [74], which can be Theconditionsusuallyincludethedifferentexplanationtech-
answered on 5- or 7-point Likert scales [2], [27], [38], [73], niquesincombinationwithotherparameterssuchasthemodel,
|                  |       |        |              |     |             |        | data set, | data modality, |     | or a number | of  | features | used as in- |
| ---------------- | ----- | ------ | ------------ | --- | ----------- | ------ | --------- | -------------- | --- | ----------- | --- | -------- | ----------- |
| [74],[75]. Among | these | works, | an effective |     | explanation | is the |           |                |     |             |     |          |             |
onethatcaneitherincreaseordecreasethefairnessperceptions, dependent variables. Note that a full grid design with many
independentvariablesmayquicklyresultinaveryhighnumber
sincetheaimofexplanationsistoshowfairnessorunfairness.
An exhaustive overview of measures for usability is given in ofconditions,whichinturnrequiresmanyparticipants.Theout-
TableIVoftheAppendix,availableonline. comevariableofinterestiscommonlymeasuredonanumerical
|             |               |     |              |     |     |         | or ordinal | scale | right away, | however, | in  | the fairness | domain, |
| ----------- | ------------- | --- | ------------ | --- | --- | ------- | ---------- | ----- | ----------- | -------- | --- | ------------ | ------- |
| 4) Human-AI | Collaboration |     | Performance: |     | The | goal of |            |       |             |          |     |              |         |
human-AI teaming is to improve the performance in AI- qualitativeanalysesaresometimesobtainedthroughconducted
interviewsorwrittenresponses[2],[27],[73].
| supported decision-making |     | above | the | bar set | by humans | or an |     |     |     |     |     |     |     |
| ------------------------- | --- | ----- | --- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
AIalone[89].Improvinghumanperformancewiththehelpof The statistical analysis directly follows from this design. If
AIhasbeenconsideredingames[10],[88],questionanswering one is interested in identifying significant differences between
|     |     |     |     |     |     |     | the groups, | common | statistical | hypotheses |     | tests | are used. For |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ----------- | ---------- | --- | ----- | ------------- |
tasks[89],[91],deceptiondetection[25],[90]andtopicmodel-
ing[29],[30]. overallcomparison,oneortwo-wayANOVAtestsarethemost
|          |        |            |     |         |          |       | commonly | used | statistical | tool. | Interesting | post-hoc | compar- |
| -------- | ------ | ---------- | --- | ------- | -------- | ----- | -------- | ---- | ----------- | ----- | ----------- | -------- | ------- |
| The most | common | assessment | is  | to rate | AI-aided | human |          |      |             |       |             |          |         |
performancebythepercentageofcorrectlypredictedinstances isonsbetween twogroups can bemade withastandard T-test,
inthedecision-makingprocess[25],[89],[90].Palejaetal. [10], if the data is normally distributed with equal variance, or by
|     |     |     |     |     |     |     | using non-parametric |     | tests | such | as the | Wilcoxon | rank-sum |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | ---- | ------ | -------- | -------- |
however,definetheperformanceasthetimetocompletethetask.
In[88],performanceismeasuredinagame-basedapplication, test (also known as Mann-Whitney U-test) for comparison of
chess,usingawinningpercentage(whichiscommonlyusedin two populations (e.g, [57]) or the Tukey HSD test (e.g., [49])
|     |     |     |     |     |     |     | for multiple | populations. |     | When | running | multiple | post-hoc |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | ---- | ------- | -------- | -------- |
sports)aswellasapercentilerankofplayermoves.
|     |     |     |     |     |     |     | tests, some | works | make | use of | the | Bonferroni | correction |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ---- | ------ | --- | ---------- | ---------- |
(e.g,[57]).
| C. ExperimentalDesignandAnalysis |     |     |     |     |     |     |                     |     |     | 30%    |     |            |         |
| -------------------------------- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ------ | --- | ---------- | ------- |
|                                  |     |     |     |     |     |     | 2) Within-Subjects: |     |     | Around | of  | the papers | use the |
Therearethreecommonexperimentalsettingswhenconduct- within-subjects design, where each participant sequentially
ing user evaluation: between-subjects (or between-groups) de- passes through all conditions and provides feedback. Fewer
signs,within-subjectsdesigns,andmixeddesignsthatcombine participants are recruited in within-subjects experiments com-
elementsofboth.Anoverviewofthedesignsfoundinthecore paredtothebetween-subjectsones.Hence,theyareparticularly
papers and their participant numbers is presented in Table IV popularwhenparticipantswithrestrictivecharacteristics,such
andFig.2,respectively. asdomain-specificprofessionalexpertise,arerequired.Forex-
1) Between-Subjects: With slightly above 55% of the user ample, Suresh et al. [9] and Rong et al. [26] recruit fourteen
studiesconductedinabetween-subjectsmanner,i.e.,onesubject medicalprofessionalsandfiveradiologistsintheiruserstudies,
is only exposed to one condition, this design choice is most respectively.Thesmallnumberofmedicalexpertscontributing
common in the XAI literature. The number of participants in totheuserstudyisalimitation[26],however,itisoftenthecase
thebetween-subjectsmannerusuallystartsataround30partic- in expert user research. Gegenfurtner et al. [165] evaluate 73
ipants, while it may go up to 1070 in total for 3 conditions as sourcesandpointoutthatthemajorityofthesestudiesinclude
in[17]andto1250for5conditionsin[53].However,thenumber only five, maybe ten experts. Besides the medical domain,
of participants can be limited when the studied application is other works [3], [4], [19], [21] also invite subjects with par-
designed for specific groups of lay persons, which cannot be ticularprofessionssuchasengineersinatechnologycompany.
easily recruited from the Internet platforms such as Amazon When no specific knowledge is required, however, participant

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2111
TABLEV
USERSTUDYFINDINGSWHENUSINGMODELEXPLANATIONSASEVALUATIONDIMENSIONS
numbersreachupto740alsoforwithin-subjectsdesigns[93]. V. FINDINGSOFUSERSTUDIES
Forwithin-groupsdesigns,theWilcoxonsigned-ranktest(e.g.,
Inthissection,wesummarizetheprimaryfindingsfromthe
| used by | [35], [52]) | is  | the most | common | method | to  | compare |     |     |     |     |     |
| ------- | ----------- | --- | -------- | ------ | ------ | --- | ------- | --- | --- | --- | --- | --- |
corepapers.TableVlistsfindingswithrespecttofourmeasured
| paired samples |     | for significant |     | differences. | Repeated-measures |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | ------------ | ----------------- | --- | --- | --- | --- | --- | --- | --- |
quantities.Tobuildanoverviewofthefindings,wedividepapers
ANOVAisacommonanalysistool,whenmultiplecomparisons
|     |     |     |     |     |     |     |     | according | to their evaluation | dimensions, | i.e., | the independent |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------- | ----------- | ----- | --------------- |
arerequired(see,e.g.,[35]).
variablesintheuserstudies.Whenusingthepresenceofexpla-
| 3) Mixed: | The | smallest | group | of  | studies, | about | 15%, use |     |     |     |     |     |
| --------- | --- | -------- | ----- | --- | -------- | ----- | -------- | --- | --- | --- | --- | --- |
nationsastheevaluationaspect,thefindingsaresummarizedin
| a mixture | of between- |     | and within-subjects |     |     | settings. | In these |     |     |     |     |     |
| --------- | ----------- | --- | ------------------- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- |
TableV.Thelistedimpactsusingexplanationsaretobeseenin
works,subjectsarefirstassignedrandomlytoonegroup,where
comparisonwithacontrolgroupwithoutexplanations.Effects
| they are     | exposed | to         | multiple  | conditions. | Anik                | and | Bunt [2] |             |                  |              |          |              |
| ------------ | ------- | ---------- | --------- | ----------- | ------------------- | --- | -------- | ----------- | ---------------- | ------------ | -------- | ------------ |
|              |         |            |           |             |                     |     |          | are divided | into two groups: | (1) Positive | effects, | for example, |
| useknowledge |         | background | inmachine |             | learningasabetween- |     |          |             |                  |              |          |              |
increasingusertrustorunderstanding;(2)Non-positiveeffects:
| subjects | factor | to divide | the | participants | into | three | groups |     |     |     |     |     |
| -------- | ------ | --------- | --- | ------------ | ---- | ----- | ------ | --- | --- | --- | --- | --- |
theeffectcanbenegative,ornotsignificantlypositive(neural),
| (expert, | intermediate |     | and beginner), |     | while inside | each | group |     |     |     |     |     |
| -------- | ------------ | --- | -------------- | --- | ------------ | ---- | ----- | --- | --- | --- | --- | --- |
oramixtureofdifferenteffects(e.g.,feature-basedexplanations
| participants | interact  | with   | explanations |            | in the      | context | of four |               |             |                |              |          |
| ------------ | --------- | ------ | ------------ | ---------- | ----------- | ------- | ------- | ------------- | ----------- | -------------- | ------------ | -------- |
|              |           |        |              |            |             |         |         | have positive | effects but | counterfactual | explanations | do not). |
| different    | scenarios | (e.g., | facial       | expression | recognition |         | or au-  |               |             |                |              |          |
Beyondtheexplanationsthemselves,otherpossibleevaluation
| tomated | speech | recognition). |     | Dominguez | et  | al. | [16] make |     |     |     |     |     |
| ------- | ------ | ------------- | --- | --------- | --- | --- | --------- | --- | --- | --- | --- | --- |
dimensionssuchasthatmighthaveanimpactontheperception
thepresenceofexplanationsabetween-subjectsconditionand
ofXAI,forinstance,AItechnologyliteracy,modelperformance,
| different | types | of explanations |     | a within-subjects |     | factor | in the |     |     |     |     |     |
| --------- | ----- | --------------- | --- | ----------------- | --- | ------ | ------ | --- | --- | --- | --- | --- |
orthedimensionalityofthedata.Insteadofusingthemerepres-
groupwithmodelexplanations.Aparticularchallengeforsuch
enceofexplanations,manyworkscomparedifferentexplanation
astudydesignisthatstatisticaltoolsfromboththeindependent-
techniqueswitheachother(seeAppendixD,availableonlinefor
| samples | and | dependent-samples |     | categories |     | need | to be |     |     |     |     |     |
| ------- | --- | ----------------- | --- | ---------- | --- | ---- | ----- | --- | --- | --- | --- | --- |
moredetails).
combined.

2112 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
TABLEVI the pronoun “I” would gain more trust of users than the ex-
OVERVIEWOFRESULTSFORUNDESIREDBEHAVIORDETECTIONUSINGMODEL
planationsformalizedina“help-provider”style.Nevertheless,
EXPLANATIONS
However,theoppositeresultisfoundandusingself-referential
expressionresultedinloweraffectivetrust.Modelperformance
together with model explanation was studied in [17] for an
imagerecognitiontask.Theauthorsfoundoutwhenimageswere
recognized (high model performance), users feel the system
morecapable(“capability”isdefinedasabeliefoftrust).
Understanding:Thefundamentalquestioninthissubdomain
is to find out which explanation technique is most beneficial
for increasing the user’s understanding of a machine learning
model. As pointed out earlier, understanding can be measured
bothinasubjectiveandobjectivemanner.
As various research questions and findings are addressed Wefirstdiscussresultsonobjectiveunderstanding.Thegoal
in 97 core papers, many papers compare explanation types in of increasing objective understanding was explicitly posed by
ordertochoose apreferableone,itisnotpossibletocover all Alqaraawi et al. [54] who reported that saliency maps have
resultsinonetable.Basedonthem,weoutlinesomeinteresting a positive effect on understanding. Wang and Yin [12] show
trendsintheeffectivenessofexplanationsonuserexperience:(1) thatcounterfactualexplanationsandfeatureimportanceincrease
Explanationsareeffectiveinimprovingusers’subjectiveunder- usersobjectiveunderstanding.Onthecontrary,Sixtetal. [57]
standing;(2)Theeffectivenessofexplanationsinincreasinguser findnoneoftheirexaminedexplanationtechniques(counterfac-
trustandusabilityofmodelsisnotclear;(3)Explanationsarenot tuals,conceptualexplanations)superiortoabaselinetechnique
good at convincing users that models are fair; (4) Interactivity consisting of example images for each class and the work by
of the model has positive impact on user trust, understanding Hase and Bansal [40] reveals that many explanations (includ-
and model usability. The first three statements can validated inganchors,prototypes)havenoeffectinincreasingobjective
throughthenumberofpapersobtainingpositiveornon-positive understanding, which LIME on tabular data being the only
effectsineachcategory,whilethelastfindingisextractedfrom exception.Apartfromtheexplanation,severalotherfactorshave
TableVintheAppendix,availableonline,whichdetailsfindings been identified to have an effect on objective understanding.
with on other independent variables. We encourage the reader HaseandBansal[40]suggestthatthedatamodalitymayhavea
toconsidertheshortsummaryofprimaryfindingsinthetables non-negligibleimpactonhowdifferentexplanationtechniques
andcheckforfurtherdetailsaccordingtotheirspecificinterests. increase understanding. Some results highlight that the choice
In the following section, we highlight some findings for each of proxy task is influential. Arora et al. [50] show that their
categoryofmeasurement. manipulatablitytaskrevealeddifferencesremainedhiddenwhen
Trust:Amongthepaperscomparingtheeffectofusingexpla- forwardsimulationisused.Inspiteofthesefindings,Buçincaet
nations to using no explanations, or placebo (randomly gener- al. [13]underlinethatpreferredexplanationsmaybedifferent
ated)explanations[8],[25],abouthalfofthepapersvalidatethat in a real-world application from a simulated one. Regarding
explanationshaveapositiveimpactonusertrust[1],[8],[10], the type of model, there is disagreement on whether white or
[13],[16],[25],[27],[28],whiletheotherhalfcannotverifythis black-boxmodelscanleadtoincreasedobjectiveunderstanding.
hypothesis[3],[11],[12],[21],[22],[24].Forinstance,Colleyet Whileblack-boxmodelswithoutexplanationsresultedinhigher
al. [3]investigatedtheexplanationsinanautonomousdriving simulation performance than white-box models with SHAP
task and discover that the trust is improved in simulation but valuesin[39],Chengetal. [22]observethatwhite-boxmodels
notwiththereal-worldfootage.Anotherexampleofthemixed increasesimulatabilityandalsoconcludethatinteractivityisan
effect of using explanations is found in [12], where (minimal) importantfactorwhenitcomestoobjectiveunderstanding.
evidenceisfoundthatfeature-basedexplanationshelpincrease Incomparisonwiththeobjectiveunderstanding,theresearch
appropriatetrust,butcounterfactualexplanationsdonot. question in the subdomain subjective understanding is to find
Apartfromusingexplanationsasindependentvariables,the outhowexplanationsimpactuser’sperceivedunderstanding[7],
user personalities or expertise may also affect their percep- [12],[17],[22],[32],[33],[34],[37],[56].Thereexistatrend
tions[2],[17],[18],[22],[23],[30].Millecampetal. [18]cap- ofusingmodelexplanationstoimprovesubjectiveunderstand-
turedpersonalcharacteristicsintheaspectssuchastheLocusof ing[13],[16],[17],[28],[34],[38],[167].However,Chromiket
ControldefinedbyFourier(“theextenttowhichpeoplebelieve al. [35]challengetheimprovementinperceivedunderstanding
theyhavepowerovereventsintheirlives”),NeedforCognition with the cognitive bias named illusion of explanatory depth
(“ameasureofthetendencyforanindividualtoengageineffort- (IOED)[168],whichmeansthatlaypeopleoftenhaveovercon-
fulcognitiveactivities”)orTech-Savviness(“theconfidencein fidence bias in their understanding of complex systems. Their
tryingoutnewtechnology”).However,nosignificantinteraction resultsconfirmtheIOEDissueinXAI,i.e.,questioningusers’
effectcouldbefoundbetweenthepersonalcharacteristicsand understanding by asking them to apply their understanding
thetrust.LiaoandSundar[5]studiedarecommendationsystem in practice consistently reduces their subjective understand-
asking users’ personal data with different explanations. They ing.Explanationscanhavedifferentimpactsonsubjectiveand
hypothesizedthatexplanationsina“help-seeker”styleandusing objective understandings [22], where white-box explanations

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2113
increase objective understanding but do not have significant that the performance gain of novices and experts comes from
impactonsubjectiveunderstanding.Similardisagreementshave different explanation sources. Paleja et al. [10] reveal that
been observed in multiple other works [40], [167]. Radensky explanations can improve novices’ performance but decrease
etal. [33]examinethejointeffectsoflocalandglobalexpla- experts’ performance. Additionally, less complex models
nations in a recommendation system and their results provide with explanations can better convince humans in correct
evidencethatbotharebetterthaneitheralone. decisions[90].
Usability:Similartotrust,itisnotclearwhetherexplanations
areeffectiveinimprovingusers’perceptionsofhelpfulness,sat-
VI. AGUIDELINEFORXAIUSERSTUDYDESIGN
isfactionorotherdimensionsofusability.Forinstance,in[16],
[30],[47],theexplanationshaveapositiveeffectonsatisfaction, Learning from the best practices of the previous works, we
whilenosignificanteffectsonsatisfactionareobservedin[18], summarizeahandyguidelineforXAIuserstudy,whichserves
[19], [29], [69]. Parallel to trust, Smith-Renner et al. [29] asachecklistforXAIpractitioners.Thisguidelinecontainssug-
provide evidence for the hypothesis that it is harmful to user gestionstoavoidpitfallsthatresearcherscouldeasilyoverlook.
trust and satisfaction to show explanations by highlighting the Weintroduceourguidelinesintheorderofbefore,duringand
importantwordsinatextclassificationtask.Astrongcorrelation after user studies, which reflects user study design, execution
betweenself-reportedtrustandsatisfactioncanalsobeobserved anddataanalysis,respectively.
in [3], where explanations have a positive impact in a simu- Before the User Study: When designing a user study, the
lateddrivingenvironment,butnosignificanteffectswhenusing firststepistodecidewhattomeasure.Todefinethemeasured
real-worlddata.Beyondexplanations,Nouranietal. [56]study quantities, one can consider two alternatives: using a general
the order of observing system weakness and strengths, which definitionoranapplication-basedquantitythatisspecifictothe
reveals that encountering weakness firstresults in a lower rate application at hand. The former one refers to a quantity that
ofusageofsystemexplanationsthanencounteringstrengthfirst. is borrowed from previous well-established research, such as
Schoeffer etal. [27] find outthatshowing featureimportance using “trust in automation” [2], [3], [21] or “general trust in
scoresorcounterfactualexplanations(oracombinationofboth) technology” [7], [23]. To further construct “trust” as a quanti-
for explaining decisions helps increase the perceived fairness, tative measurement, one needs to examine how existing work
whereashighlightingimportantfeatureswithoutscoresdoesnot. has conceptualized “trust” in both social sciences context as
However, several studies don’t show a significant difference wellasXAIandtechnicalcontext[169].Theapplication-based
between scenarios with and without explanations [27], [38], quantitydependsontheapplicationgoal,forinstanceinachess
[78].Effectsofexplanationsmaybedependentoninputsamples, game[88],themeasurementisthehumanwinningpercentage
asshownin[67].TheauthorsshowthatbothDebiased-CAMand withthehelpofmodelexplanations(Human-AIcollaboration).
Biased-CAMimprovethehelpfulnessforaweaklyblurredim- FromTableV,wecanseethatpreviousworkshavefrequently
age,however,thereisnosignificantimprovementforunblurred struggledtoprovetheeffectivenessofXAIevenwithrespectto
orstronglyblurredimages.Whenusedtoassistusersindetecting acontrolgroupthatiswithoutexplanation.Whenonlydifferent
undesired behaviors, model explanations are likely to identify explanation techniques are considered, there will always be
various types of problems that exist within models or data, as one winner explanation, but the overall benefit will remain
demonstratedby[57],[71],[72].However,successfuldetection undisclosed (see examples in Appendix D, available online).
is not guaranteed. For example, Poursabzi-Sangdeh et al. [53] Therefore, it is important to compare with a baseline without
showthatuserswithmodelexplanationsarelessabletoidentify explanations to rigorously show the strength of XAI. When
incorrectpredictions.Alimitationofcurrentdetectionmethods a comparative design is explicitly desired, baselines such as
is that users may have varying assessments, such as perceived randomexplanations[28],[41],[62]).
unfairnessandirrelevance[53],[71],[73],regardingthefeatures Whendeployingaproxytask,itsdifficultyshouldbegauged
usedinmodelsfordecision-making.Duetothislimitation,the andmonitoredcarefully.Inthepast,theforwardsimulationtask
effectiveness of methods assessed through self-reported data hasbeencriticizedasbeingunrealisticallycomplexfordomains
may face challenges in generalizability as discussed in [73]. such as computer vision [54]. Thus, other proxy tasks such as
Yet, these methods generally offer a one-size-fits-all solution, featureimportancequeries[57]ormanipulatabilitychecks[32],
failingtoaccountforvariationsinindividualassessments. [50]wereproposed.Anotherimportantpointistochooseaproxy
Human-AI Collaboration Performance: A strain of task that is simplified, but features many characteristics of the
works [25], [88], [90], [91], [95], [96], [96] show that application in mind [119]. Notably, the proxy task should be
viewing explanations can improve human accuracy in making designedclosetothefinalanticipatedapplication,asevenslight
decisions, especially with feature-based explanations taking differencesinthetasksmayvoidthevalidityofthefindingson
text data as input [25], [90], [91]. When using example-based theproxytasksintherealworld[13].
explanations in text classification, there is no improvement The measurement is often dependent on the definition of
in human performance [25]. Likewise, utilizing explanations the measured quantity. For instance, in [58], the objective
has no significant impact on human performance in [89], understanding is measured as failure prediction (the accu-
[92], but simply showing model predictions has a positive racy of user prediction when the model prediction is wrong).
effect in [92]. Experts and novices perceive explanations For subjective measurements such as subjective understand-
differently,forexample,FengandBoyd-Graber[91]conclude ingortrust,one-dimensionalmeasures(i.e.,simplyratingone

2114 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
questionsuchas“Doyoutrustthemodelexplanation?”)have shouldleavetheirbackpacks,waterbottles,andlunchboxes)and
thedrawbackthattheycannotcompletelyreflectdifferentcon- plansforunexpectedsituations(e.g.,uncooperativeparticipants
structs of measured quantities [8]. Moreover, subjective ques- andmultifunctionalsystems).Howtoobtainparticipants’con-
tions and behavioral measurements often appear to be weakly sent should be an important part of the procedure. Additional
correlated.Forexample,theusersstatethattheytrustmodelbut procedureisrequiredforobtainingconsentwhenworkingwith
they do not really follow the model suggestions [11]. Similar vulnerablepopulations(e.g.,childrenandpregnantwomen),in
findingshavebeenmadewithrespecttoobjectiveandsubjective which case alternative consent procedures might take place.
understanding[12],[35],[40].Toovercomethislimitation,both Another benefit of pre-designing the experiment script is to
self-reportedandobservedmeasuresshallbeusedinparallel. fine-tune the language to avoid inadvertent cues. Researchers
Besides the measures introduced in Section IV-B, there are can unintentionally pass on their expectations to participants
severalpsychologicalconstructsthatcanbedeployedtoevaluate through verbal and nonverbal behavior, which might result
multiple facets of the interaction between humans and XAI. in participants’ skewed performance towards the researchers’
Forinstance,thesubjectivetaskvalueintheexpectancy-value desire [169]. To ensure a sound experiment procedure and to
frameworkisoftenusedtoanalyzesubjectivemotivationtotake protecttheintegrityofthedata,itisworthwhiletoputinmuch
any actions [170], which is not thoroughly studied in the XAI efforttodesignadetailedexperimentscript.
experience yet. The subjective task value consists of intrinsic During the User Study: A sufficient number of participants
value(enjoyment),attainmentvalue(importanceforone’sself), istheprerequisiteofasoliduserstudyanalysis.Togetarough
utilityvalue(usefulness),andcost(theamountofeffortortime estimate of common sample sizes, we refer the reader to the
needed) [170], [171]. A good explanation interface should be participant statistics in Fig. 2 where we analyze the subject
positivelycorrelatedwiththesubjectivetaskvalue,consequently numbersindifferentexperimentaldesigns.Forinstance,around
boostingone’sinterestandmotivationtousethemodelexpla- 350userswithoutanyspecificexpertiseareaveragelyrecruited
nation. With regard to the cost of using model explanations, in between-subject experiments. However, we would like to
cognitive load is popularly measured in the current literature underlinethattherequirednumberofparticipantsishighlyspe-
with conventional Likert scales [162], [172]. Cognitive load cifictothestudydesignandshouldbedeterminedindividually,
researchersstudythevalidityofdifferentvisualappearancesin for instance by conducting a statistical power analysis [177].
ratingscalesbeyondnumericalLikertscales,i.e.,pictorialscales Additionally,recruitedparticipantsshouldhavethesameknowl-
suchasemoticons(faceswithdifferentemotions),orembodied edgebackgroundastheendusersthatapplicationsaredesigned
pictures of different weights [173]. Their results demonstrate for.Forinstance,whenevaluatinganinterfaceexplainingloan
that numerical scales are more proper in complex tasks while approvaldecisionstobankcustomers,itisnotpropertoinclude
pictorialscalesareforsimpleones. onlystudentswhosemajoriscomputerscience,sincetheymay
Pre-registrationusingonlineplatformssuchasAsPredicted1 have prior knowledge of how model explanations work. Note
has become a common practice in recent years [174]. In this thatthedesignofanAIapplicationrequiresdifferentaudiences
process,researcherssubmitadocumentdetailingtheirplanned acrosstheprojectcycle,thusmodelexplanationsneedtoevolve
studyonlinebeforeinitiatingthedatacollection.Amongother aswell[178].
details,thepre-registrationincludesthemeasuredvariablesand Toupholdhigh-qualitystandardsofthecollecteddata,atten-
hypotheses,dataexclusioncriteria,andthenumberofsamples tion or manipulation checks are essential to filter out careless
thatwillbecollected.Anexhaustivepre-registrationcanprovide feedback. This particularly applies to long surveys or online
evidenceagainstthefindingsbeingaresultofselectivereporting surveyswithlayusers.Kungetal. [179]justifytheuseofthese
orp-hacking[175]andthusstrengthenthecredibilityofastudy. checks without compromising scale validity. In within-subject
Expertinterviewsandpre-studiesfollowingathink-aloudproto- experiments,arandomorderofconditionsisnecessarytoavoid
col[176],e.g.,inthereferences[32],[46],areoftenmentioned order effect [1]. Participants can learn knowledge of data or
ashelpfultoolstodeveloptheexplanationsystemandthestudy examplesshowninthepreviousconditions,andTsaietal. [6]
design and gain first qualitative insights or complement the choosetouseaLatinsquaredesigntoavoidthelearningeffect.
qualitativeanalysis[13],[65]. After the User Study: After the data collection, statistical
When preparing for a user study, it is important to plan for tests are run to find significant effects. The applicable tests
explicitstepsandtohaveabackupplanfordifferentsituations. usedaredeterminedbyexperimentaldesignsandtheformand
Before participants arrive, it is helpful to provide them with distributionofthedata.Generally,ANOVAtestsandT-testare
informationsuchaswheretheresearcherswillmeetwiththem, usually used when comparing distributions between different
what they need to bring, and how they can prepare for the conditions. Structural Equation Models (SEM) or multi-level
study.Ifconductingtheexperimentinperson,sendparticipants modelsareusedformediationanalysis.Moredetailsofstatistic
areminderthedaybeforeandprovidethemwithyourcontactin tools can be found in Section IV-C. Distributional assumption
casetheycannotfindtheexperimentsiteortheyneedtocancel checks should be applied. When Likert-type data is collected
theexperimentsession.Onceparticipantsarrive,makesurethe as in most of the questionnaires, non-parametric tests such as
researchershaveaplanthatcoversallstagesoftheexperiment. pairedWilcoxonsigned-ranktest,orKruskal-WallisHtestfor
Theprotocolshouldcoversmalldetails(e.g.,whereparticipants multiplegroupscanbeusedtoavoidnormalityassumptions.
Ifmultiplemeasuresareaggregatedintoasingleinstrument,
1[Online].Available:https://aspredicted.org it is important to assess the validity of this aggregation with

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2115
Fig.3. SummarycardsoftheguidelinesextractedfrompastXAIuserstudies.
reliability measures such as the tau-equivalent reliability (also modeling and involving users in the design phase and not just
knownasCronbach’sα).Forexample,ifobjectiveandsubjec- inapost-hocmannerduringtheevaluationphase,weexpectthe
tivemeasuresofaquantity,suchasunderstandingarecombined, developmentofXAIsolutionsthatbetterrespondtouserneeds.
it is necessary to verify that there is sufficient agreement. If Asdiscussedin[117],therearetwoaspectsofhuman-centered
multiple items (e.g., data samples or visualizations) are rated AI:(1)AIsystemsthatunderstandhumanswithasociocultural
by several subjects, statistics such as Cohan’s κ as Fleiß’s κ background and (2) AI systems that help humans understand
formorethantworaters[180]canbeusedtoassessagreement them.TheformerpointcanguidethedesignofAIsystems.In
beyondchancebetweentheseratersandserveasanindication thissection,wediscussXAIresearchthatleveragesthisinsight.
forthereliabilityoftheratings. The process of explaining a machine’s decisions to human
In the final writing phase, it is essential to report sufficient users can be viewed as a teaching-learning process where the
detailsthatallowreaderstoestimatetheexplanatorypowerof XAIsystemistheteacherandthehumanusersarethestudents.
the study. On the level of participants, this should include the From a user-centered perspective, the problem of designing
totalnumberofparticipantsandhowmanyareassignedtoeach effectiveteachingmethodstoenhancethestudent’s(i.e.,user’s)
treatmentgroup,theirrecruitment,consentandincentivization, learning outcomes is essential to human-centered XAI algo-
andtheexacttreatmentconditionstheyaresubjectedto.Further- rithms. To leverage the ability of humans and address unique
more,somedescriptivestatisticsofthecollecteddatacanhelp user’s needs, it is important to review studies and findings
readersassessthecharacteristicsoftheadequacyofthestatistical frompsychologyandeducation.Thesestudiesprovideinsights
tools used. Regarding the analysis, we found it important to into how humans perceive other intelligent agents (humans or
mentionhowtheunderlyingassumptionsofthestatisticaltests artificial agents) and how they utilize limited information to
usedwerecheckedandtomentiontheexactvariantofthetest inferandgeneralize.Understandinghowhumansthinkandlearn
used (e.g., stating “a two-way ANOVA with the independent willhelpXAIdevelopersbuildanddesignsystemsthatarenot
variables X and Y” is used instead of just mentioning that only informative but also user-friendly to people with differ-
ANOVA-testisused). entbackgrounds.Inthissection,wediscussthreepedagogical
frameworks,namely(1)theexpectancy-valuemotivationtheory,
VII. FUTURERESEARCHDIRECTIONS (2) the theory of mind, and (3) hybrid teaching, to shed light
on incorporating such methods in computational approaches.
Our survey of recent and ongoing XAI research also helps
Inspired by existing work in pedagogy and XAI, we provide
usidentifyresearchgapsanddistillafewdirectionsforfuture
implications for designing future transparent AI systems and
investigations.Inthissection,wehighlightthesedirectionsand
human-centeredevaluations.
summarizeourfindings.
Expectancy-Value Motivation Theory: Human interaction
withXAIinterfacescanbeviewedasanactivitywherehumans
A. TowardsIncreasinglyUser-CenteredXAI
learn about the model’s inner workings through explanations
Weadvocatethatuser-centeredmethodsshouldbeusednot andthenachieveanunderstandingofthemodels.Thequestion
onlytoassessXAIsolutions(e.g.,throughuserstudies)butalso ofhowtoenhancetheefficiencyandtheoutcomeofthishuman
todesignthem(e.g.,throughuser-centereddesign).Byexplicitly learning process is of high importance [181]. This research

2116 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
problemiswidelyconsideredineducationalpsychologythrough ExplanationsthroughLargeLanguageModels(LLMs):The
the lens of expectancy-value motivation theory. For instance, recent rise of Large Language Models [183], [184] naturally
Hullemanetal. [171]proposetoutilizeinterventionstoincrease opens up new research directions. There is a growing interest
the perception of usefulness (utility value) to subsequently in- in leveraging their unprecedented capabilities [185] to offer
creasemotivationandfinalperformance.Interventionhererefers explanations for model decisions [186], [187]. Through their
toidentifyingtherelevanceofmodelexplanationstotheuser’s natural language interface, LLMs offer the possibility to build
own situation, which can be a prompt question while working interactive explainers [188]. Intriguingly, textual explanations
withtheinterface.Moreover,whenutilizingmodelexplanations can also be used as subsequent inputs to LLMs which may
inhuman-AIcollaboration,explanationscanbeseenasatypeof help to solve subsequent problems and result in superior per-
“scaffolding” (promptduringatask)proposed inaconceptual formance[189].Thistechnique,referredtoaschain-of-thought
frameworkineducation. reasoning[190],opensupaninterestingresearchterritorycom-
TheoryofMind:WheninteractingwithXAIsystems,humans bininginterpretabilityandperformanceconsiderations.
form mental models of the machine learning algorithms that
reflect their belief of how the algorithms work. The formation
B. OpenResearchProblems
ofthesementalmodelscomesfromobservingexplanations or
examplesgiventothehuman,whooftensubconsciouslyapplies 1) Automatic versus Human-Subject Evaluations: With au-
theobservationsinafewexamplestothebroaderunderstanding tomaticevaluations,werefertoevaluationmethodsthatdonot
of the whole machine learning system. This incredible ability requirehumansubjects,whichcorrespondstothefunctionally-
to infer, rationalize, and summarize other intelligent agent’s groundedmetricsdiscussedin[119],[120].Thesemetricsaim
decisionsisknownastheTheoryofMind(ToM)inpsychology. totestdesiderataaroundthe“faithfulness”/“fidelity”/“truthful-
Based on this theory, the Bayesian Theory of Mind (BToM) ness”ofmodelexplanations[120],[121],[191].Faithfulnessof
provides a probabilistic framework to predict inferences that explanationsisdefinedasthatexplanationsareindicativeoftrue
people make about mental states underlying other agents’ ac- importantfeaturesintheinput[191].Theautomaticevaluations
tions. Recent work, at the intersection of XAI and robotics, aimatcapturinggeneralobjectivitywhichisindependentfrom
indicatesthathumansalsoattributeToMtoartificialagentsthat downstreamtasks,whilehumanevaluationsarecontextualized
they observe or interact with. Guided by these user-centered with specific use cases. Generally speaking, automatic evalu-
results, several works at the intersection of XAI and robotics ations and human evaluations tackle different research chal-
haveutilizedBToMtocreateasimulateduser,andthenuseitto lenges:theformerobjectivelyexamineshowtrulyexplanations
generatehelpfulexplanations. reflectmodelsandthelatteronemeasureshowhumansperceive
Hybrid Teaching: Teaching strategies for the human-to- modelsthroughexplanations(althoughthereexistingalgorithms
humansettinghavebeenwidelystudiedandmanycategoriza- for automated evaluation designed to align with human evalu-
tionsexist.Onewayofcategorizingthesestrategiesisthrough ations, which we will discuss later). All explanations used in
the following three concepts: (1) direct teaching, (2) indirect human-subjectexperimentsshouldhavesatisfyingperformance
teaching,and(3)hybridteaching.Directteachingutilizesdirect inautomaticevaluations,i.e.,theexplanationsshouldbeableto
instructions that are teacher-centered, involve clear teaching faithfullyunboxthemodel.Thisverificationstepisessentialto
objectives,andareconsistentwithclassroomorganizations.In guaranteethevalidityoftheempiricaluserstudyandtoensure
XAIapplications,directteachingmethodsgenerateexplanations thatusersarenottrickedbyunfaithfulexplanations.However,in
byselectingrepresentativeexamplesofanagent’sdecisionsto most current human-subject experiments, the functional faith-
convey the patterns in its policy. In contrast, indirect teaching fulness of explanations is not thoroughly verified beforehand.
isstudent-centeredandencouragesindependentlearning.Inthe Using unfaithful explanations could lead to the problem that
XAI perspective, methods utilizing indirect teaching provide only the placebo effect of explanations is measured. Ideally,
userswithtoolstoactivelyandindependentlyexploreanAIsys- a good explanation should be faithful to the model as well as
tem.Technically,directteachingfocusesonprovidingguidance understandablebyusers.
(usingacomputationalapproach)toassistusersinbuildingan 2) IdentifyingandHandlingConfounders: Existingresearch
understanding of a machine, whereas indirect teaching (often underscores the vulnerability of model explanation studies to
through a user interface) enables users to address individual significant confounding effects. For instance, Papenmeier et
learningpreferencesandmitigateindividualconfusionaboutthe al. [155]revealthatusertrustcanbemoreinfluencedbymodel
AI.Toleveragetheadvantagesofthetwoteachingstrategies,hy- accuracythanthefaithfulnessoftheexplanationitself.Similarly,
bridteachinghasbeenwidelyusedinhuman-to-humanteaching Yinetal. [192]demonstratethattheaccuracyscoreperceived
withanemphasisoninteractivity.Recentwork [182]indicates byusersandtheoneshowntouserscontributetotrustformation.
that hybrid teaching reduces the amount of time for a user to A different problem is that good explanations also reveal
understand an agent’s policy compared to direct and indirect weaknesses of the model. However, when seeing unexpected
teaching,andismoresubjectivelypreferredbytheparticipants. explanations, users may express their negative feelings about
Buildingonthis,futureXAIsystemscanconsiderusinghybrid themodelthroughnegativeratingsoftheexplanations.There-
teachingmethodsthat(i)generatedirectinstructionstoprovide fore,goodmodelexplanationsshouldhelpuserscalibratetheir
guidance to user’s understanding of an AI system; and (ii) trust[26],[193],i.e.,trustthemodel’sdecisionwhenitiscorrect
providemethodstoallowuserstointeractwiththeagent. but distrust it otherwise. There is a disagreement on how to

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2117
handle such cases: When evaluating model fairness, several existingwork.Yet,thelinkbetweenevaluationsthroughdiffer-
works[2],[27],[38],[73],[75]reckontheincreaseinperceived entproxytasksandreal-worldapplicationshasnotbeenmade
fairnessaspositive,whileDodgeetal. [74]definethedecrease veryexplicittodate.Buçincaetal. [13]showthattheoutcomes
as positive. Other factors, such as the temporal occurrence of of proxy evaluations can be different from a real-world task.
modelerrors(Nouranietal. [56]),andthedimensionsofmodels Morespecifically,thewidelyacceptedproxytasks,whereusers
(Rossetal. [32],Poursabzietal. [53]),alsocomeintoplay. areaskedtobuildthementalmodelsoftheAI,maynotpredict
In summary, these confounding elements suggest that users the performance in actual decision-making tasks, where users
might be led to put more trust in oversimplified, deceptive, makeuseoftheexplanationstoassistinmakingdecisions.The
or simply unfaithful explanations. To mitigate this, we rec- resultsshowthatuserstrustdifferentexplanationsintheproxy
ommend meticulous analysis, control and reporting of poten- task and the actual decision-making task. Therefore, we argue
tial confounders, such as explanation faithfulness and model that further research is required to uncover the links between
accuracy, across various test conditions. More advanced mea- current proxy tasks and on-task performance or to devise new
sureshavebeensuggestedaswell.Forinstance,Schoefferand proxytaskswithaverifiedconnectiontoactualtasks.
Kuehl’s [79] propose appropriate fairness perceptions, which 6) Simulated Evaluation as a Cost-Efficient Solution: As
measureswhetherpeopleincreaseordecreasetheirfairnessper- human-subject experiments are costly to conduct, Chen
ceptionsdependingonthealgorithmicfairnessoftheunderlying et al. [198] propose a simulated evaluation framework
model.Nevertheless,thethoroughinvestigationofconfounding (SimEvals)toselectpotentialexplanationsforuserstudiesby
factors remains a challenge. Calibrated measures that are less measuringthepredictiveinformationprovidedbyexplanations.
pronetoconfoundingcanbeavaluablestepforward. Concretely, the authors consider three use cases where model
3) MitigatingPersonalBiasesforXAI: MostXAItechniques explanations are deployed: forward simulation, counterfactual
and corresponding designed user studies provide one-size-fits- reasoning,anddatadebugging.Humanperformanceismeasured
all solutions. Individual bias, rooted in a user’s mental frame- for these three tasks with different explanations. If there is a
work,influencestheuser’sperceptionofamodel.Itshouldbe significant gap in settings of using two types of explanations,
consideredinXAIdesign,development,andevaluationproce- thesimulatedevaluationcanalsoobservesuchagapunderthe
dures.Severalstudiesthataimtoexplainreinforcementlearning sametasksettingsaswell.Meanwhile,firstattemptstosimulate
policies utilize cognitive science theories to create a model of humantextualresponsesinagivencontextusinglargelanguage
the human user [181], [182], [194], [195]. They then generate modelsshowthatmodelscanprovidesurprisinglyanthropomor-
explanationsbasedonthishumanmodelandverifythebenefits phicanswers[199].UndoubtedlyandalsoaffirmedbyChenet
oftailoringexplanationsforindividualusermodels.Withinthe al. [198],itisnotyetrealistictoreplacehumanevaluationwith
scopeofXAI,[196],[197]utilizeaBayesianTeachingframe- thesimulatedframeworkasotherfactorse.g.,cognitivebiases
work to capture human perception of model explanations. In can affect human decisions. To better simulate human evalua-
userstudies,dependingonculturalandeducationalbackground, tions,moreeffortshouldbedirectedtowardsmodelinghuman
participantsmaylikelygivedifferentfeedback[31].Thiskindof cognitiveprocesses.Concurrentlyandwithappropriatecaveats,
personalbiascanbemitigatedbydeployingalargesamplesize XAIresearchersshouldalsoleverageexistingandapproximate
andrecruitingparticipantswhoarerepresentativeofthetarget models of human cognition to enable rapid prototyping and
audience.Weadvocatethatpersonalbiasesshouldbetakeninto assessment of explanations. Section VII-A discusses several
accountintherealmofXAIdevelopment. candidate human cognition models and highlights recent XAI
4) Human-in-the-LoopandSequentialExplanations: Insev- works[181],[182]thatutilizethis“Oz-of-Wizard”paradigm.
eral relevant cases, such as online recommendation systems,
users are not only confronted with an explanation once but
VIII. CONCLUSION
instead view decisions and potential explanations repeatedly.
Recent work in this domain [35] has shown that the order of Inrecentyears,therehasbeenaproliferationofXAIresearch
decisions and explanations may indeed have an effect on user inbothacademiaandindustry.Explainabilityisahuman-centric
perception and understanding. The AI model may continue property[141]andthereforeXAIshouldbepreferablystudied
to shape the user’s mental model over time. The differences by taking humans’ feedback into account. In this work, we
betweenthesingle-useandthesequentialsettingstillremainto investigated recent user studies for XAI techniques through a
bethoroughlyinvestigated. principled literature review. Based on our review, we found
5) ProxyTasksShouldBeClosetoReal-WorldTasks: When out that the effectiveness of XAI in users’ interaction with
usingproxytaskstoevaluate models,forinstance,tomeasure ML models was not consistent across different applications,
subjectiveunderstanding,thereisagreatchoiceoftaskspresent thussuggestingthatthereisastrongneedformoretransparent
in the literature. A good proxy task should have the following andcomparablehuman-basedevaluationsinXAI.Furthermore,
features:(1)ithasclosereal-worldconnections[119];(2)users relevant disciplines, such as cognitive psychology and social
or participants have some background knowledge of the task sciences in general, should become an integral part of XAI
butnottoomuchtoaffecttheirjudgmentorperformanceduring research.
the task; (3) the task is not too complicated to implement or We comprehensively analyzed the design patterns and find-
thereexistsanexistingimplementationbutwasusedfordifferent ings from previous works. Based on best-practice approaches
purposes(i.e.,notusedforXAI);and(4)ithasconnectionsto and measured quantities, we propose a general guideline for

2118 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
human-centereduserstudiesandseveralfutureresearchdirec- [20] T.Li,G.Convertino,R.K.Tayi,andS.Kazerooni,“WhatdatashouldI
tionsforXAIresearchersandpractitioners.Thereby,thiswork protect?recommenderandplanningsupportfordatasecurityanalysts,”
inProc.ACMInt.Conf.Intell.UserInterfaces,2019,pp.286–297.
represents a starting point for more transparent and human-
[21] H.Kaur,H.Nori,S.Jenkins,R.Caruana,H.Wallach,andJ.Wortman
centeredXAIresearch. Vaughan, “Interpreting interpretability: Understanding data scientists’
useofinterpretabilitytoolsformachinelearning,”inProc.SIGCHIConf.
Hum.FactorsComput.Syst.,2020,pp.1–14.
[22] H.-F.Chengetal.,“Explainingdecision-makingalgorithmsthroughUI:
REFERENCES
Strategiestohelpnon-expertstakeholders,”inProc.SIGCHIConf.Hum.
FactorsComput.Syst.,2019,pp.1–12.
[1] C.Panigutti,A.Beretta,F.Giannotti,andD.Pedreschi,“Understanding
[23] J.Kunkel,T.Donkers,L.Michael,C.-M.Barbu,andJ.Ziegler,“Let
theimpactofexplanationsonadvice-taking:AuserstudyforAI-based
meexplain:Impactofpersonalandimpersonalexplanationsontrustin
clinicaldecisionsupportsystems,”inProc.SIGCHIConf.Hum.Factors
recommendersystems,”inProc.SIGCHIConf.Hum.FactorsComput.
Comput.Syst.,2022,pp.1–9.
Syst.,2019,pp.1–12.
[2] A.I.AnikandA.Bunt,“Data-centricexplanations:Explainingtraining
[24] D.H.Kim,E.Hoque,andM.Agrawala,“Answeringquestionsabout
data of machine learning systems to promote transparency,” in Proc.
chartsandgeneratingvisualexplanations,”inProc.SIGCHIConf.Hum.
SIGCHIConf.Hum.FactorsComput.Syst.,2021,pp.1–13.
FactorsComput.Syst.,2020,pp.1–13.
[3] M.Colley,B.Eder,J.O.Rixen,andE.Rukzio,“Effectsofsemantic
[25] V.LaiandC.Tan,“Onhumanpredictionswithexplanationsandpre-
segmentationvisualizationontrust,situationawareness,andcognitive
dictionsofmachinelearningmodels:Acasestudyondeceptiondetec-
loadinhighlyautomatedvehicles,”inProc.SIGCHIConf.Hum.Factors
tion,”inProc.ACMConf.FairnessAccountabilityTransparency,2019,
Comput.Syst.,2021,pp.1–1.
pp.1–13.
[4] U.Ehsan,Q.V.Liao,M.Muller,M.O.Riedl,andJ.D.Weisz,“Expanding
[26] Y. Rong, N. Castner, E. Bozkir, and E. Kasneci, “User trust
explainability: Towards social transparency in ai systems,” in Proc.
on an explainable ai-based medical diagnosis support system,”
SIGCHIConf.Hum.FactorsComput.Syst.,2021,pp.1–19.
2022,arXiv:2204.12230.
[5] M. Liao and S. S. Sundar, “How should AI systems talk to users
[27] J. Schoeffer, N. Kuehl, and Y. Machowski, ““there is not enough in-
whencollectingtheirpersonalinformation?effectsofroleframingand
formation”: On the effects of explanations on perceptions of infor-
self-referencingonHuman-AIinteraction,”inProc.SIGCHIConf.Hum.
mational fairness and trustworthiness in automated decision-making,”
FactorsComput.Syst.,2021,pp.1–14.
2022,arXiv:2205.05758.
[6] C.-H.Tsai,Y.You,X.Gui,Y.Kou,andJ.M.Carroll,“Exploringand
[28] U.Ehsan,P.Tambwekar,L.Chan,B.Harrison,andM.O.Riedl,“Auto-
promotingdiagnostictransparencyandexplainabilityinonlinesymptom
matedrationalegeneration:AtechniqueforexplainableAIanditseffects
checkers,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2021,
onhumanperceptions,”inProc.ACMInt.Conf.Intell.UserInterfaces,
pp.1–17.
2019,pp.263–274.
[7] L.Guo,E.M.Daly,O.Alkan,M.Mattetti,O.Cornec,andB.Knijnen-
[29] A.Smith-Renneretal.,“Noexplainabilitywithoutaccountability:An
burg,“Buildingtrustininteractivemachinelearningviausercontributed
empiricalstudyofexplanationsandfeedbackininteractiveML,”inProc.
interpretablerules,”inProc.ACMInt.Conf.Intell.UserInterfaces,2022,
SIGCHIConf.Hum.FactorsComput.Syst.,2020,pp.1–13.
pp.537–548.
[30] A.Smith-Renner,V.Kumar,J.Boyd-Graber,K.Seppi,andL.Findlater,
[8] J.Ooge,S.Kato,andK.Verbert,“ExplainingrecommendationsinE-
“Diggingintousercontrol:Perceptionsofadherenceandinstabilityin
learning:Effectsonadolescents’trust,”inProc.ACMInt.Conf.Intell.
transparent models,” in Proc. ACM Int. Conf. Intell. User Interfaces,
UserInterfaces,2022,pp.93–105.
2020,pp.519–530.
[9] H.Suresh,K.M.Lewis, J.Guttag,andA.Satyanarayan,“Intuitively
[31] A.SpringerandS.Whittaker,“Progressivedisclosure:Empiricallymoti-
assessingMLmodelreliabilitythroughexample-basedexplanationsand
vatedapproachestodesigningeffectivetransparency,”inProc.ACMInt.
editingmodelinputs,”inProc.ACMInt.Conf.Intell.UserInterfaces,
Conf.Intell.UserInterfaces,2019,pp.107–120.
2022,pp.767–781.
[32] A. Ross, N. Chen, E. Z. Hang, E. L. Glassman, and F. Doshi-Velez,
[10] R.Paleja,M.Ghuy,N.RanawakaArachchige,R.Jensen,andM.Gom-
“Evaluatingtheinterpretabilityofgenerativemodelsbyinteractivere-
bolay,“TheutilityofexplainableAIinadhochuman-machineteaming,”
construction,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2021,
inProc.Int.Conf.NeuralInf.Process.Syst.,vol.34,2021,pp.610–623.
pp.1–15.
[11] J.Schaffer,J.O’Donovan,J.Michaelis,A.Raglin,andT.Höllerer,“I
[33] M.Radensky,D.Downey,K.Lo,Z.Popovic,andD.S.Weld,“Exploring
candobetterthanyourAI:Expertiseandexplanations,”inProc.ACM
theroleoflocalandglobalexplanationsinrecommendersystems,”in
Int.Conf.Intell.UserInterfaces,2019,pp.240–251.
Proc.SIGCHIConf.Hum.FactorsComput.Syst.,2022,pp.1–7.
[12] X.WangandM.Yin,“Areexplanationshelpful?Acomparativestudy
[34] S.Hadash,M.C.Willemsen,C.Snijders,andW.A.IJsselsteijn,“Im-
oftheeffectsofexplanationsinAI-assisteddecision-making,”inProc.
proving understandability of feature contributions in model-agnostic
ACMInt.Conf.Intell.UserInterfaces,2021,pp.318–328.
explainable AI tools,” in Proc. SIGCHI Conf. Hum. Factors Comput.
[13] Z. Buçinca, P. Lin, K. Z. Gajos, and E. L. Glassman, “Proxy tasks
Syst.,2022,pp.1–9.
and subjective measures can be misleading in evaluating explainable
[35] M.Chromik,M.Eiband,F.Buchner,A.Krüger,andA.Butz,“IthinkI
AI systems,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2020,
getyourpoint,AI!theillusionofexplanatorydepthinexplainableAI,”
pp.454–464.
inProc.ACMInt.Conf.Intell.UserInterfaces,2021,pp.307–317.
[14] X.Peng,M.Riedl,andP.Ammanabrolu,“Inherentlyexplainablerein-
[36] J.Rebanal,J.Combitsis,Y.Tang,andX.Chen,“XAlgo:Adesignprobe
forcementlearninginnaturallanguage,”inProc.Int.Conf.NeuralInf.
ofexplainingalgorithms’internalstatesviaquestion-answering,”inProc.
Process.Syst.,2022,pp.16178–16190.
ACMInt.Conf.Intell.UserInterfaces,2021,pp.329–339.
[15] Y. Zhang, Q. V. Liao, and R. K. Bellamy, “Effect of confidence and
[37] U. Kuhl, A. Artelt, and B. Hammer, “Keep your friends close and
explanation on accuracy and trust calibration in AI-assisted decision
your counterfactuals closer: Improved learning from closest rather
making,” in Proc. Conf. Fairness Accountability Transparency, 2020,
than plausible counterfactual explanations in an abstract setting,”
pp.295–305.
2022,arXiv:2205.05515.
[16] V.Dominguez,P.Messina,I.Donoso-Guzmán,andD.Parra,“Theeffect
[38] E.Rader,K.Cotter,andJ.Cho,“Explanationsasmechanismsforsup-
ofexplanationsandalgorithmicaccuracyonvisualrecommendersystems
portingalgorithmictransparency,”inProc.SIGCHIConf.Hum.Factors
ofartisticimages,”inProc.ACMInt.Conf.Intell.UserInterfaces,2019,
Comput.Syst.,2018,pp.1–13.
pp.408–446.
[39] A.Bell,I.Solano-Kamaiko,O.Nov,andJ.Stoyanovich,“It’sjustnot
[17] C.J.Cai,J.Jongejan,andJ.Holbrook,“Theeffectsofexample-based
thatsimple:Anempiricalstudyoftheaccuracy-explainabilitytrade-off
explanationsinamachinelearninginterface,”inProc.ACMInt.Conf.
in machine learning for public policy,” in Proc. ACM Conf. Fairness
Intell.UserInterfaces,2019,pp.258–262.
AccountabilityTransparency,2022,pp.248–266.
[18] M.Millecamp,N.N.Htun,C.Conati,andK.Verbert,“Toexplainornot
[40] P.HaseandM.Bansal,“EvaluatingexplainableAI:Whichalgorithmic
toexplain:Theeffectsofpersonalcharacteristicswhenexplainingmusic
explanationshelpuserspredictmodelbehavior?,”inProc.58thAnnu.
recommendations,”inProc.ACMInt.Conf.Intell.UserInterfaces,2019,
MeetingAssoc.Comput.Linguistics,2020,pp.5540–5552.
pp.397–407.
[41] H. Schuff, A. Jacovi, H. Adel, Y. Goldberg, and N. T. Vu,
[19] C.-H. Tsai and P. Brusilovsky, “Beyond the ranked list: User-driven
“Human interpretation of saliency-based explanation over text,”
explorationanddiversificationofsocialrecommendation,”inProc.ACM
2022,arXiv:2201.11569,.
Int.Conf.Intell.UserInterfaces,2018,pp.239–250.

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2119
[42] S.Bang,P.Xie,H.Lee,W.Wu,andE.Xing,“Explainingablack-box [64] I. Laina, R. Fong, and A. Vedaldi, “Quantifying learnability and de-
byusingadeepvariationalinformationbottleneckapproach,”inProc. scribability of visual concepts emerging in representation learning,”
AAAIConf.Artif.Intell.,2021,pp.11396–11404. Adv.NeuralInf.Process.Syst.,vol.33,2020,pp.13112–13126.
[43] S.S.Kim,N.Meister,V.V.Ramaswamy,R.Fong,andO.Russakovsky, [65] Y. Wang, P. Venkatesh, and B. Y. Lim, “Interpretable directed di-
“HIVE:Evaluatingthehumaninterpretabilityofvisualexplanations,”in versity: Leveraging model explanations for iterative crowd ideation,”
Proc.Eur.Conf.Comput.Vis.,2022,pp.280–298. in Proc. SIGCHI Conf. Hum. Factors Comput. Syst., 2022,
[44] M.Szymanski,M.Millecamp,andK.Verbert,“Visual,textualorhybrid: pp.1–28.
Theeffectofuserexpertiseondifferentexplanations,”inProc.ACMInt. [66] D.L.Arendt,N.Nur,Z.Huang,G.Fair,andW.Dou,“Parallelembed-
Conf.Intell.UserInterfaces,2021,pp.109–119. dings:Avisualizationtechniqueforcontrastinglearnedrepresentations,”
[45] G.Plumb,M.Al-Shedivat,Á.A.Cabrera,A.Perer,E.Xing,andA.Tal- inProc.ACMInt.Conf.Intell.UserInterfaces,2020,pp.259–274.
walkar,“Regularizingblack-boxmodelsforimprovedinterpretability,” [67] W.Zhang,M.Dimiccoli,andB.Y.Lim,“Debiased-CAMtomitigateim-
inProc.Int.Conf.NeuralInf.Process.Syst.,2020,pp.10526–10536. ageperturbationswithfaithfulvisualexplanationsofmachinelearning,”
[46] W. Zhang and B. Y. Lim, “Towards relatable explainable ai with the inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2022,pp.1–32.
perceptualprocess,”inProc.SIGCHIConf.Hum.FactorsComput.Syst., [68] J.Gao,X.Wang,Y.Wang,andX.Xie,“Explainablerecommendation
2022,pp.1–24. throughattentivemulti-viewlearning,”inProc.AAAIConf.Artif.Intell.,
[47] C.Bove,J.Aigrain,M.-J.Lesot,C.Tijus,andM.Detyniecki,“Con- 2019,pp.3622–3629.
textualizationandexplorationoflocalfeatureimportanceexplanations [69] P.Kouki,J.Schaffer,J.Pujara,J.O’Donovan,andL.Getoor,“Personal-
toimproveunderstandingandsatisfactionofnon-expertusers,”inProc. izedexplanationsforhybridrecommendersystems,”inProc.ACMInt.
ACMInt.Conf.Intell.UserInterfaces,2022,pp.807–819. Conf.Intell.UserInterfaces,2019,pp.379–390.
[48] A.Abdul,C.vonderWeth,M.Kankanhalli,andB.Y.Lim,“COGAM: [70] C.-H. Tsai and P. Brusilovsky, “Explaining recommendations in an
Measuring and moderating cognitive load in machine learning model interactivehybridsocialrecommender,”inProc.ACMInt.Conf.Intell.
explanations,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2020, UserInterfaces,2019,pp.391–396.
pp.1–14. [71] A. Balayn, N. Rikalo, C. Lofi, J. Yang, and A. Bozzon, “How can
[49] K.NatesanRamamurthy,B.Vinzamuri,Y.Zhang,andA.Dhurandhar, explainabilitymethodsbeusedtosupportbugidentificationincomputer
“Modelagnosticmultilevelexplanations,”inProc.Int.Conf.NeuralInf. visionmodels?,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,
Process.Syst.,2020,pp.5968–5979. 2022,pp.1–16.
[50] S. Arora, D. Pruthi, N. Sadeh, W. W. Cohen, Z. C. Lipton, and G. [72] K. Rawal and H. Lakkaraju, “Beyond individualized recourse: Inter-
Neubig,“Explain,edit,andunderstand:Rethinkinguserstudydesign pretableandinteractivesummariesofactionablerecourses,”inProc.Int.
forevaluatingmodelexplanations,”inProc.AAAIConf.Artif.Intell., Conf.NeuralInf.Process.Syst.,2020,pp.12187–12198.
2022,pp.5277–5285. [73] N.Grgic´-Hlacˇa,E.M.Redmiles,K.P.Gummadi,andA.Weller,“Human
[51] J.Antoran,U.Bhatt,T.Adel,A.Weller,andJ.M.Hernández-Lobato, perceptionsoffairnessinalgorithmicdecisionmaking:Acasestudyof
“Gettinga{clue}:Amethodforexplaininguncertaintyestimates,”in criminalriskprediction,”inProc.WideWebConf.,2018,pp.903–912.
Proc.Int.Conf.Learn.Representations,2021. [74] J.Dodge,Q.V.Liao,Y.Zhang,R.K.Bellamy,andC.Dugan,“Explaining
[52] J.Borowskietal.,“Exemplarynaturalimagesexplain{CNN}activations models:Anempiricalstudyofhowexplanationsimpactfairnessjudg-
better than state-of-the-art feature visualization,” in Proc. Int. Conf. ment,”inProc.ACMInt.Conf.Intell.UserInterfaces,2019,pp.275–285.
Learn.Representations,2021. [75] G.Harrison,J.Hanson,C.Jacinto,J.Ramirez,andB.Ur,“Anempirical
[53] F.Poursabzi-Sangdeh,D.G.Goldstein,J.M.Hofman,J.W.Wortman studyontheperceivedfairnessofrealistic,imperfectmachinelearning
Vaughan,andH.Wallach,“Manipulatingandmeasuringmodelinter- models,” in Proc. Conf. Fairness Accountability Transparency, 2020,
pretability,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2021, pp.392–402.
pp.1–52. [76] C.Wangetal.,“DohumanspreferdebiasedAIalgorithms?acasestudyin
[54] A.Alqaraawi,M.Schuessler,P.Weiß,E.Costanza,andN.Berthouze, careerrecommendation,”inProc.ACMInt.Conf.Intell.UserInterfaces,
“Evaluating saliency map explanations for convolutional neural net- 2022,pp.134–147.
works:Auserstudy,”inProc.ACMInt.Conf.Intell.UserInterfaces, [77] N.N.Htun,E.Lecluse,andK.Verbert,“Perceptionoffairnessingroup
2020,pp.275–285. music recommender systems,” in Proc. ACM Int. Conf. Intell. User
[55] M. T. Ribeiro, S. Singh, and C. Guestrin, “Anchors: High-precision Interfaces,2021,pp.302–306.
model-agnosticexplanations,”inProc.AAAIConf.Artif.Intell.,2018, [78] R.Binns,M.VanKleek,M.Veale,U.Lyngs,J.Zhao,andN.Shadbolt,
pp.1527–1535. “‘it’sreducingahumanbeingtoapercentage’perceptionsofjusticein
[56] M.Nouranietal.,“Anchoringbiasaffectsmentalmodelformationand algorithmicdecisions,”inProc.SIGCHIConf.Hum.FactorsComput.
userrelianceinexplainableaisystems,”inProc.ACMInt.Conf.Intell. Syst.,2018,pp.1–14.
UserInterfaces,2021,pp.340–350. [79] J. Schoeffer and N. Kuehl, “Appropriate fairness perceptions? on the
[57] L.Sixt,M.Schuessler,O.-I.Popescu,P.Weiß,andT.Landgraf,“Dousers effectivenessofexplanationsinenablingpeopletoassessthefairness
benefitfrominterpretablevision?auserstudy,baseline,anddataset,”in ofautomateddecisionsystems,”inProc.Companion:CompanionPub.
Proc.Int.Conf.Learn.Representations,2022. Conf. Comput. Supported Cooperative Work Social Comput., 2021,
[58] A. Chandrasekaran, V. Prabhu, D. Yadav, P. Chattopadhyay, and D. pp.153–157.
Parikh, “Do explanations make VQA models more predictable to [80] T.Donkers,T.Kleemann,andJ.Ziegler,“Explainingrecommendations
a human?,” in Proc. Conf. Empir. Methods Natural Lang. Process., bymeansofaspect-basedtransparentmemories,”inProc.ACMInt.Conf.
2018,pp.1036–1042. Intell.UserInterfaces,2020,pp.166–176.
[59] J.Colin,T.Fel,R.Cadene,andT.Serre,“WhatIcannotpredict,Ido [81] F.Hohman,A.Head,R.Caruana,R.DeLine,andS.M.Drucker,“Gamut:
not understand: A human-centered evaluation framework for explain- Adesignprobetounderstandhowdatascientistsunderstandmachine
ability methods,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2022, learningmodels,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,
pp.2832–2845. 2019,pp.1–13.
[60] H. Shen and T.-H. Huang, “How useful are the machine-generated [82] U.Kuhl,A.Artelt,andB.Hammer,“Let’sgotothealienzoo:Intro-
interpretations to general users? a human evaluation on guessing the ducinganexperimentalframeworktostudyusabilityofcounterfactual
incorrectlypredictedlabels,”inProc.AAAIConf.Hum.Comput.Crowd- explanationsformachinelearning,”2022,arXiv:2205.03398.
sourcing,2020,pp.168–172. [83] T.Schneider,J.Hois,A.Rosenstein,S.Ghellal,D.Theofanou-Fülbier,
[61] C.-K. Yeh, B. Kim, S. O. Arik, C.-L. Li, T. Pfister, and P. Raviku- andA.R.Gerlicher,“ExplAInyourself!transparencyforpositiveUX
mar,“Oncompleteness-awareconcept-basedexplanationsindeepneu- inautonomousdriving,”inProc.SIGCHIConf.Hum.FactorsComput.
ral networks,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2019, Syst.,2021,pp.1–12.
pp.20554–20565. [84] S.Choi,K.Aizawa,andN.Sebe,“FontMatcher:Fontimageparingfor
[62] A. Ghorbani, J. Wexler, J. Y. Zou, and B. Kim, “Towards automatic harmoniousdigitalgraphicdesign,”inProc.ACMInt.Conf.Intell.User
concept-basedexplanations,”inProc.Int.Conf.NeuralInf.Process.Syst., Interfaces,2018,pp.37–41.
2019,pp.9277–9286. [85] P.LeBras,D.A.Robb,T.S.Methven,S.Padilla,andM.J.Chantler,
[63] T.Leemann,Y.Rong,S.Kraft,E.Kasneci,andG.Kasneci,“Coherence “Improving user confidence in concept maps: Exploring data driven
evaluationofvisualconceptswithobjectsandlanguage,”inProc.Int. explanations,”inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2018,
Conf.Learn.RepresentationsWS,2022. pp.1–13.

2120 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
[86] R.Shang,K.K.Feng,andC.Shah,“WhyamInotseeingit?under- [111] P. M. Addo, D. Guegan, and B. Hassani, “Credit risk analysis using
standingusers’needsforcounterfactualexplanationsineverydayrecom- machineanddeeplearningmodels,”Risks,vol.6,no.2,p.38,2018.
mendations,”inProc.ACMConf.FairnessAccountabilityTransparency, [112] N. Van Berkel, J. Goncalves, D. Hettiachchi, S. Wijenayake, R. M.
2022,pp.1330–1340. Kelly,andV.Kostakos,“Crowdsourcingperceptionsoffairpredictorsfor
[87] J.Dodge,A.A.Anderson,M.Olson,R.Dikkala,andM.Burnett,“How machinelearning:Arecidivismcasestudy,”inProc.ACMHum.-Comput.
dopeoplerankmultiplemutantagents?,”inProc.ACMInt.Conf.Intell. Interact.,vol.3,pp.1–21,2019.
UserInterfaces,2022,pp.191–211. [113] T.Sourdin,“JudgeVrobot?:Artificialintelligenceandjudicialdecision-
[88] D.DasandS.Chernova,“Leveragingrationalestoimprovehumantask making,”Univ.NewSouthWalesLawJ.,vol.41,no.4,pp.1114–1133,
performance,” in Proc. ACM Int. Conf. Intell. User Interfaces, 2020, 2018.
pp.510–518. [114] M.Raghavan,S.Barocas,J.Kleinberg,andK.Levy,“Mitigatingbias
[89] G. Bansal et al., “Does the whole exceed its parts? the effect of ai inalgorithmichiring:Evaluatingclaimsandpractices,”inProc.Conf.
explanationsoncomplementaryteamperformance,”inProc.SIGCHI FairnessAccountabilityTransparency,2020,pp.469–481.
Conf.Hum.FactorsComput.Syst.,2021,pp.1–16. [115] P.Tambe,P.Cappelli,andV.Yakubovich,“Artificialintelligenceinhu-
[90] V. Lai, H. Liu, and C. Tan, ““why is’ Chicago’deceptive?,” towards manresourcesmanagement:Challengesandapathforward,”California
buildingmodel-driventutorialsforhumans,”inProc.SIGCHIConf.Hum. Manage.Rev.,vol.61,pp.15–42,2019.
FactorsComput.Syst.,2020,pp.1–13. [116] D. Castelvecchi, “Can we open the black box of AI?,” Nature News,
[91] S.FengandJ.Boyd-Graber,“Whatcanaidoforme?evaluatingmachine vol.538,pp.20–23,2016.
learninginterpretationsincooperativeplay,”inProc.ACMInt.Conf. [117] M.O.Riedl,“Human-centeredartificialintelligenceandmachinelearn-
Intell.UserInterfaces,2019,pp.229–239. ing,”Hum.Behav.Emerg.Technol.,vol.1,pp.33–36,2019.
[92] Y.Alufaisan,L.R.Marusich,J.Z.Bakdash,Y.Zhou,andM.Kantar- [118] U.EhsanandM.O.Riedl,“Human-centeredexplainableAI:Towardsa
cioglu,“Doesexplainableartificialintelligenceimprovehumandecision- reflectivesociotechnicalapproach,”inProc.Int.Conf.Human-Comput.
making?,”inProc.AAAIConf.Artif.Intell.,2021,pp.6618–6626. Interact.,2020,pp.449–466.
[93] K.Z.GajosandL.Mamykina,“DopeopleengagecognitivelywithAI? [119] F.Doshi-VelezandB.Kim,“Towardsarigorousscienceofinterpretable
impactofAIassistanceonincidentallearning,”inProc.ACMInt.Conf. machinelearning,”2017,arXiv:1702.08608.
Intell.UserInterfaces,2022,pp.794–806. [120] M. Nauta et al., “From anecdotal evidence to quantitative evaluation
[94] M.Liao,S.S.Sundar,andJ.B.Walther,“Usertrustinrecommenda- methods: A systematic review on evaluating explainable AI,” ACM
tionsystems:Acomparisonofcontent-based,collaborativeanddemo- Comput.Surv.,vol.55,pp.1–42,2023.
graphicfiltering,”inProc.CHIConf.Hum.FactorsComput.Syst.,2022, [121] R. Tomsett, D. Harborne, S. Chakraborty, P. Gurram, and A. Preece,
pp.1–14. “Sanitychecksforsaliencymetrics,”inProc.AAAIConf.Artif.Intell.,
[95] G. Nguyen, D. Kim, and A. Nguyen, “The effectiveness of feature 2020,pp.6021–6029.
attributionmethodsanditscorrelationwithautomaticevaluationscores,” [122] Y. Rong, T. Leemann, V. Borisov, G. Kasneci, and E. Kasneci, “A
inProc.Int.Conf.NeuralInf.Process.Syst.,2021,pp.26422–26436. consistentandefficientevaluationstrategyforattributionmethods,”in
[96] M.R.Taesiri,G.Nguyen,andA.Nguyen,“Visualcorrespondence-based Proc.Int.Conf.Mach.Learn.,2022,pp.18770–18795.
explanationsimproveAIrobustnessandhuman-AIteamaccuracy,”in [123] D. Nguyen, “Comparing automatic and human evaluation of lo-
Proc.Int.Conf.NeuralInf.Process.Syst.,2022,pp.34287–34301. cal explanations for text classification,” in Proc. Conf. North Amer.
[97] J.Wei,J.He,K.Chen,Y.Zhou,andZ.Tang,“Collaborativefilteringand Chapter Assoc. Comput. Linguistics: Hum. Lang. Technol., 2018,
deeplearningbasedrecommendationsystemforcoldstartitems,”Expert pp.1069–1078.
Syst.Appl.,vol.69,pp.29–39,2017. [124] G.Hoffman,“Evaluatingfluencyinhuman–robotcollaboration,”IEEE
[98] S.Yang,M.Korayem,K.AlJadda,T.Grainger,andS.Natarajan,“Com- Trans.Human-Mach.Syst.,vol.49,no.3,pp.209–218,Jun.2019.
biningcontent-basedandcollaborativefilteringforjobrecommendation [125] Workshop, “ExSS-ATEC: Explainable smart systems for algorithmic
system:Acost-sensitivestatisticalrelationallearningapproach,”Knowl.- transparencyinemergingtechnologies,”inProc.25thInt.Conf.Intell.
BasedSyst.,vol.136,pp.37–45,2017. UserInterfacesCompanion,vol.1,2020.
[99] Y.Zhang,X.Chen,Q.Ai,L.Yang,andW.B.Croft,“Towardsconversa- [126] S.Mohseni,N.Zarei,andE.D.Ragan,“Amultidisciplinarysurveyand
tionalsearchandrecommendation:Systemask,userrespond,”inProc. frameworkfordesignandevaluationofexplainableAIsystems,”ACM
ACMInt.Conf.Inf.Knowl.Manage.,2018,pp.177–186. Trans.Interact.Intell.Syst.(TiiS),vol.11,no.3/4,pp.1–45,2021.
[100] S.Grigorescu,B.Trasnea,T.Cocias,andG.Macesanu,“Asurveyofdeep [127] Q.Yang,N.Banovic,andJ.Zimmerman,“Mappingmachinelearningad-
learningtechniquesforautonomousdriving,”J.FieldRobot.,vol.37, vancesfromHCIresearchtorevealstartingplacesfordesigninnovation,”
pp.362–386,2020. inProc.SIGCHIConf.Hum.FactorsComput.Syst.,2018,pp.1–11.
[101] H.Cuietal.,“Multimodaltrajectorypredictionsforautonomousdriving [128] A.AdadiandM.Berrada,“Peekinginsidetheblack-box:Asurveyon
usingdeepconvolutionalnetworks,”inProc.Int.Conf.Robot.Automat., explainableartificialintelligence(XAI),”IEEEAccess,vol.6,pp.52138–
2019,pp.2090–2096. 52160,2018.
[102] Y. Rong, C. Han, C. Hellert, A. Loyal, and E. Kasneci, “Artificial [129] A.B.Arrietaetal.,“Explainableartificialintelligence(XAI):Concepts,
intelligencemethodsinin-cabinusecases:Asurvey,”IEEEIntell.Transp. taxonomies,opportunitiesandchallengestowardresponsibleAI,”Inf.
Syst.Mag.,vol.14,no.3,pp.132–145,May/Jun.2021. Fusion,2020,vol.58,pp.82–115.
[103] R.R.Murphy,“IntroductiontoAIrobotics,”Ind.Robot:AnInt.J.,vol.28, [130] W. Samek and K.-R. Müller, “Towards explainable artificial intelli-
no.3,pp.266–267,2001. gence,” in Proc. Explainable AI: Interpreting Explaining Visualizing
[104] K. Rajan and A. Saffiotti, “Towards a science of integrated AI and DeepLearn.,2019,pp.5–22.
robotics,”Artif.Intell.,vol.247,pp.1–9,2017. [131] N.BurkartandM.F.Huber,“Asurveyontheexplainabilityofsupervised
[105] S.Wachter,B.Mittelstadt,andL.Floridi,“Transparent,explainable,and machinelearning,”J.Artif.Intell.Res.,vol.70,pp.245–317,2021.
accountableAIforrobotics,”Sci.Robot.,vol.2,2017,Art.no.eaan6080. [132] D. V. Carvalho, E. M. Pereira, and J. S. Cardoso, “Machine learning
[106] S. H. Park and K. Han, “Methodologic guide for evaluating clinical interpretability:Asurveyonmethodsandmetrics,”Electronics,vol.8,
performanceandeffectofartificialintelligencetechnologyformedical 2019,Art.no.832.
diagnosisandprediction,”Radiology,vol.286,pp.800–809,2018. [133] L.H.Gilpin,D.Bau,B.Z.Yuan,A.Bajwa,M.Specter,andL.Ka-
[107] J. A. Sidey-Gibbons and C. J. Sidey-Gibbons, “Machine learning in gal, “Explaining explanations: An overview of interpretability of ma-
medicine:Apracticalintroduction,”BMCMed.Res.Methodol.,vol.19, chinelearning,”inProc.IEEE5thInt.Conf.DataSci.Adv.Analytics,
2019,Art.no.64. 2018,pp.80–89.
[108] R.Vaishya,M.Javaid,I.H.Khan,andA.Haleem,“Artificialintelli- [134] A. Abdul, J. Vermeulen, D. Wang, B. Y. Lim, and M. Kankanhalli,
gence(AI)applicationsforCOVID-19pandemic,”DiabetesMetabolic “Trends and trajectories for explainable, accountable and intelligible
Syndrome:Clin.Res.Rev.,vol.14,pp.337–339,2020. systems:AnHCIresearchagenda,”inProc.SIGCHIConf.Hum.Factors
[109] X.Dastile,T.Celik,andM.Potsane,“Statisticalandmachinelearning Comput.Syst.,2018,pp.1–28.
models in credit scoring: A systematic literature survey,” Appl. Soft [135] G.Montavon,W.Samek,andK.-R.Müller,“Methodsforinterpreting
Comput.,vol.91,2020,Art.no.106263. andunderstandingdeepneuralnetworks,”Digit.SignalProcess.,vol.73,
[110] M.Ala’raj,M.F.Abbod,M.Majdalawieh,andL.Jum’a,“Adeeplearning pp.1–15,2018.
modelforbehaviouralcreditscoringinbanks,”NeuralComput.Appl., [136] A.DasandP.Rad,“Opportunitiesandchallengesinexplainableartificial
vol.34,pp.5839–5866,2022. intelligence(XAI):Asurvey,”2020,arXiv:2006.11371.

RONGetal.:TOWARDSHUMAN-CENTEREDEXPLAINABLEAI:ASURVEYOFUSERSTUDIESFORMODELEXPLANATIONS 2121
[137] G.Joshi,R.Walambe,andK.Kotecha,“Areviewonexplainabilityin [163] R. R. Hoffman, S. T. Mueller, G. Klein, and J. Litman, “Metrics for
multimodaldeepneuralnets,”IEEEAccess,vol.9,pp.59800–59821, explainableAI:Challengesandprospects,”2018,arXiv:1812.04608.
2021. [164] A. Holzinger, A. Carrington, and H. Müller, “Measuring the quality
[138] R. Moraffah, M. Karami, R. Guo, A. Raglin, and H. Liu, “Causal of explanations: The system causability scale (SCS),” KI-Künstliche
interpretabilityformachinelearning-problems,methodsandevaluation,” Intelligenz,2020.
ACMSIGKDDExplorationsNewslett.,vol.22,pp.18–33,2020. [165] A. Gegenfurtner, E. Lehtinen, and R. Säljö, “Expertise differences in
[139] I.NunesandD.Jannach,“Asystematicreviewandtaxonomyofex- the comprehension of visualizations: A meta-analysis of eye-tracking
planationsindecisionsupportandrecommendersystems,”UserModel. researchinprofessionaldomains,”KI-KunstlicheIntelligenz,vol.34,
User-AdaptedInteract.,vol.27,pp.393–444,2017. no.2,pp.193–198,2020.
[140] Z.C.Lipton,“Themythosofmodelinterpretability:Inmachinelearning, [166] K.Cotter,J.Cho,andE.Rader,“Explainingthenewsfeedalgorithm:
theconceptofinterpretabilityisbothimportantandslippery,”Queue, Ananalysisofthe“newsfeedFYI,”blog,”inProc.CHIConf.Extended
vol.16,pp.31–57,2018. Abstr.Hum.FactorsComput.Syst.,2017,pp.1553–1560.
[141] Q.V.LiaoandK.R.Varshney,“Human-centeredexplainableAI(XAI): [167] D.Wang,Q.Yang,A.Abdul,andB.Y.Lim,“Designingtheory-driven
Fromalgorithmstouserexperiences,”2021,arXiv:2110.10790. user-centricexplainableAI,”inProc.SIGCHIConf.Hum.FactorsCom-
[142] V.Lai,C.Chen,Q.V.Liao,A.Smith-Renner,andC.Tan,“Towardsa put.Syst.,2019,pp.1–15.
scienceofHuman-AIdecisionmaking:Asurveyofempiricalstudies,” [168] L. Rozenblit and F. Keil, “The misunderstood limits of folk science:
2021,arXiv:2112.11471. An illusion of explanatory depth,” Cogn. Sci., vol. 26, pp. 521–562,
[143] J.J.FerreiraandM.S.Monteiro,“WhatarepeopledoingaboutXAIuser 2002.
experience?asurveyonaiexplainabilityresearchandpractice,”inProc. [169] G. Hoffman and X. Zhao, “A primer for conducting experiments in
Int.Conf.Hum.-Comput.Interact.,2020,pp.56–73. human–robotinteraction,”ACMTrans.Human-RobotInteract.,vol.10,
[144] N.Bevan,“InternationalstandardsforHCIandusability,”Int.J.Hum.- pp.1–31,2020.
Comput.Stud.,vol.55,pp.533–552,2001. [170] J.Eccles,“Expectancies,valuesandacademicbehaviors,”Achievement
[145] W.Iso,“9241–11:1998,Ergonomicrequirementsforworkwithvisual AchievementMotives,vol.58,pp.58–74,1983.
display terminals (VDTs)-Part 11: Guidance on usability,” Int. Org. [171] C.S.Hulleman,J.J.Kosovich,K.E.Barron,andD.B.Daniel,“Making
Standardization,vol.45,no.9,1998. connections:Replicatingandextendingtheutilityvalueinterventionin
[146] M. T. Ribeiro, S. Singh, and C. Guestrin, ““Why should I trust theclassroom,”J.Educ.Psychol.,vol.109,2017,Art.no.387.
you?,” explaining the predictions of any classifier,” in Proc. 22nd [172] F.G.Paas,“Trainingstrategiesforattainingtransferofproblem-solving
ACM SIGKDD Int. Conf. Knowl. Discov. Data Mining, 2016, skillinstatistics:Acognitive-loadapproach,”J.Educ.Psychol.,vol.84,
pp.1135–1144. pp.429–434,1992.
[147] S.M.LundbergandS.-I.Lee,“Aunifiedapproachtointerpretingmodel [173] K.Ouwehand,A.V.D.Kroef,J.Wong,andF.Paas,“Measuringcognitive
predictions,”inProc.Int.Conf.NeuralInf.Process.Syst.,2017,pp.4768– load:Aretheremorevalidalternativestolikertratingscales?,”Front.
4777. Educ.,FrontiersEduc.,vol.6,p.702616,2021.
[148] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and [174] J.P.Simmons,L.D.Nelson,andU.Simonsohn,“Pre-registration:Why
D. Batra, “Grad-CAM: Visual explanations from deep networks via andhow,”J.Consum.Psychol.,vol.31,pp.151–162,2021.
gradient-basedlocalization,”inProc.IEEEInt.Conf.Comput.Vis.,2017, [175] U.Simonsohn,L.D.Nelson,andJ.P.Simmons,“P-curve:Akeytothe
pp.618–626. file-drawer,”J.Exp.Psychol.:Gen.,vol.143,pp.534–547,2014.
[149] P. Voigt and A. Von dem Bussche, “The EU general data protection [176] K.A.EricssonandH.A.Simon,ProtocolAnalysis:VerbalReportsas
regulation (GDPR),” in A Practical Guide, 1st ed., Berlin, Germany: Data.Cambridge,MA,USA:MITPress,1984.
Springer,2017. [177] J.Cohen,StatisticalPowerAnalysisfortheBehavioralSciences,San
[150] B.GoodmanandS.Flaxman,“Europeanunionregulationsonalgorith- Francisco,CA,USA:Academic,2013.
mic decision-making and a “right to explanation”,” AI Mag., vol. 38, [178] S.Dhanorkar,C.T.Wolf,K.Qian,A.Xu,L.Popa,andY.Li,“Who
no.3,pp.50–57,2017. needstoknowwhat,when?:BroadeningtheexplainableAI(XAI)design
[151] C.Molnar,“Interpretablemachinelearning,”pp.26–27,2020. spacebylookingatexplanationsacrosstheAIlifecycle,”inProc.Des.
[152] C.Rudin,“Stopexplainingblackboxmachinelearningmodelsforhigh InteractiveSyst.Conf.,2021,pp.1591–1602.
stakesdecisionsanduseinterpretablemodelsinstead,”Nat.Mach.Intell., [179] F. Y. Kung, N. Kwok, and D. J. Brown, “Are attention check ques-
vol.1,pp.206–215,2019. tionsathreattoscalevalidity?,”Appl.Psychol.,vol.67,pp.264–283,
[153] R.Caruana,Y.Lou,J.Gehrke,P.Koch,M.Sturm,andN.Elhadad,“In- 2018.
telligiblemodelsforhealthcare:Predictingpneumoniariskandhospital [180] J.L.Fleiss,“Measuringnominalscaleagreementamongmanyraters,”
30-day readmission,” in Proc. 21th ACM SIGKDD Int. Conf. Knowl. Psychol.Bull.,vol.76,pp.378–382,1971.
Discov.DataMining,2015,pp.1721–1730. [181] I.Lage,D.Lifschitz,F.Doshi-Velez,andO.Amir,“Exploringcompu-
[154] C.Panigutti,A.Perotti,andD.Pedreschi,“DoctorXAI:Anontology- tationalusermodelsforagentpolicysummarization,”inIJCAI:Proc.
based approach to black-box sequential data classification explana- Conf.,2019,Art.no.1401.
tions,” in Proc. Conf. Fairness Accountability Transparency, 2020, [182] P.QianandV.Unhelkar,“Evaluatingtheroleofinteractivityonimprov-
pp.629–639. ingtransparencyinautonomousagents,”inProc.21stInt.Conf.Auton.
[155] A.Papenmeier,G.Englebienne,andC.Seifert,“Howmodelaccuracy AgentsMultiagentSyst.,2022,pp.1083–1091.
andexplanationfidelityinfluenceusertrust,”2019,arXiv:1907.12652. [183] A.Radfordetal.,“Languagemodelsareunsupervisedmultitasklearn-
[156] J.vanderWaa,E.Nieuwburg,A.Cremers,andM.Neerincx,“Evaluating ers,”OpenAIBlog,vol.1,no.8,2019,Art.no.9.
XAI: A comparison of rule-based and example-based explanations,” [184] ChatGPT,Introducing,“OpenAI,”2023.Accessed:Feb.17,2023.[On-
Artif.Intell.,vol.291,2021,Art.no.103404. line].Available:https://openai.com/blog/chatgpt
[157] B.J.Erickson,P.Korfiatis,Z.Akkus,andT.L.Kline,“Machinelearning [185] S.Bubecketal.,“Sparksofartificialgeneralintelligence:Earlyexperi-
formedicalimaging,”Radiographics,vol.37,no.2,pp.505–515,2017. mentswithGPT-4,”2023,arXiv:2303.12712.
[158] J.-Y. Jian, A. M. Bisantz, and C. G. Drury, “Foundations for an em- [186] W.Zhouetal.,“Towardsinterpretablenaturallanguageunderstanding
piricallydeterminedscaleoftrustinautomatedsystems,”Int.J.Cogn. with explanations as latent variables,” in Proc. Int. Conf. Neural Inf.
Ergonom.,vol.4,pp.53–71,2000. Process.Syst.,2020,pp.6803–6814.
[159] B.Kimetal.,“Interpretabilitybeyondfeatureattribution:Quantitative [187] S.Wiegreffe,J.Hessel,S.Swayamdipta,M.Riedl,andY.Choi,“Re-
testingwithconceptactivationvectors(TCAV),”inProc.Int.Conf.Mach. framingHuman-AIcollaborationforgeneratingfree-textexplanations,”
Learn.,2018,pp.2668–2677. inProc.Conf.NorthAmer.ChapterAssoc.Comput.Linguistics:Hum.
[160] B. P. Knijnenburg, M. C. Willemsen, Z. Gantner, H. Soncu, and C. Lang.Technol.,2022,pp.632–658.
Newell,“Explainingtheuserexperienceofrecommendersystems,”in [188] S.Wang,Z.Zhao,X.Ouyang,Q.Wang,andD.Shen,“Chatcad:Inter-
UserModelingUser-AdaptedInteraction.Berlin,Germany:Springer, activecomputer-aideddiagnosisonmedicalimageusinglargelanguage
2012. models,”2023,arXiv:2302.07257.
[161] B.Y.LimandA.K.Dey,“Assessingdemandforintelligibilityincontext- [189] N.F.Rajani,B.McCann,C.Xiong,andR.Socher,“Explainyourself!
awareapplications,”inProc.11thInt.Conf.UbiquitousComput.,2009, leveraginglanguagemodelsforcommonsensereasoning,”inProc.57th
pp.195–204. Annu.MeetingAssoc.Comput.Linguistics,2019,pp.4932–4942.
[162] S.G.HartandL.E.Staveland,“DevelopmentofNASA-TLX(taskload [190] J. Wei et al., “Chain-of-thought prompting elicits reasoning in large
index): Results of empirical and theoretical research,” Adv. Psychol., languagemodels,”inProc.Int.Conf.NeuralInf.Process.Syst.,2022,
vol.52,pp.139–183,1988. pp.24824–24837.

2122 IEEETRANSACTIONSONPATTERNANALYSISANDMACHINEINTELLIGENCE,VOL.46,NO.4,APRIL2024
[191] D.AlvarezMelisandT.Jaakkola,“Towardsrobustinterpretabilitywith PeizhuQianiscurrentlyworkingtowardthePhDde-
self-explainingneuralnetworks,”inProc.Int.Conf.NeuralInf.Process. greeincomputersciencewithRiceUniversity,USA
Syst.,2018,pp.7786–7795. working with Dr. Vaibhav Unhelkar on problems
[192] M.Yin,J.WortmanVaughan,andH.Wallach,“Understandingtheeffect inhuman-robotinteraction,robottransparency,and
ofaccuracyontrustinmachinelearningmodels,”inProc.SIGCHIConf. explainableAI.Herresearchinterestliesinbuilding
Hum.FactorsComput.Syst.,2019,pp.1–12. amutualunderstandingbetweenarobotanditshu-
[193] A.Bussone,S.Stumpf,andD.O’Sullivan,“Theroleofexplanationson mancollaborators.Herworkappliespsychologythe-
trustandrelianceinclinicaldecisionsupportsystems,”inProc.Int.Conf. oriestocomputationalframeworks,enablingrobots
HealthcareInform.,2015,pp.160–169. tocommunicatetheirobjectives.
[194] C.Baker,R.Saxe,andJ.Tenenbaum,“Bayesiantheoryofmind:Mod-
elingjointbelief-desireattribution,”inProc.Annu.MeetingCogn.Sci.
Soc.,vol.33,no.33,2011.
[195] S.H.Huang,D.Held,P.Abbeel,andA.D.Dragan,“Enablingrobots VaibhavUnhelkarreceivedtheMSdegreeinaero-
tocommunicatetheirobjectives,”Auton.Robots,vol.43,pp.309–326, nauticsandastronauticsandthePhDdegreeinau-
2019. tonomoussystems,in2015and2020,respectively.
[196] S.C.-H.Yang,N.E.T.Folke,andP.Shafto,“Apsychologicaltheoryof Heisanassistantprofessorofcomputersciencewith
explainability,”inProc.Int.Conf.Mach.Learn.,2022,pp.25007–25021. RiceUniversity,USAwhereheleadsaresearchgroup
[197] S. C.-H. Yang, W. K. Vong, R. B. Sojitra, T. Folke, and P. Shafto, in the emerging area of Human-Centered AI and
“Mitigating belief projection in explainable artificial intelligence via Robotics.Unhelkarearnedhisundergraduatedegree
Bayesianteaching,”Sci.Rep.,vol.11,2021,Art.no.9863. in aerospace engineering from the Indian Institute
[198] V. Chen, N. Johnson, N. Topin, G. Plumb, and A. Talwalkar, ofTechnologyinBombay,in2012.FromtheMas-
“Use-case-grounded simulations for explanation evaluation,” 2022, sachusettsInstituteofTechnology,whereheworked
arXiv:2206.02256. intheComputerScienceandArtificialIntelligence
[199] G.Aher,R.I.Arriaga,andA.T.Kalai,“Usinglargelanguagemodelsto Laboratory(CSAIL).
simulatemultiplehumans,”2022,arXiv:2208.10264.
Yao Rong received the MSc degree in electrical
TinaSeidelreceivedthediplomadegreeinpsychol-
andcomputerengineeringfromtheTechnicalUni-
ogyfromtheUniversityofRegensburg(Germany)
versity of Munich, Germany, in 2019. She is cur-
andVanderbiltUniversityNashville(USA),in1998,
rentlyworkingtowardthedoctoraldegreewiththe
andthePhDdegreewithexcellence,in2002fromthe
Human-CenteredTechnologiesforLearningGroup,
LeibnizInstituteforScienceandMathematicsEdu-
theTechnicalUniversityofMunich.From2022to
cationKiel(Germany).SheholdstheFriedlSchoeller
2023,sheservedasavisitingscholarwiththeDATA
ChairforEducationalPsychologywiththeSchoolof
Lab, Rice University. Her research interests lie in
SocialSciencesandTechnology,TechnicalUniver-
human-centeredAI,explainableAI,andhuman-AI
sity ofMunich, Germany. Her research focuses on
interactiontechnologies.
teachingandteachereducation.Shehasestablisheda
TeacherResearch&TrainingSimulationCenterthat
conductsseveralresearchprojectsfundedbytheGermanScienceFoundation
Tobias Leemann received the MSc degree from andtheGermanFederalMinistryofEducationandResearch.
theUniversityofErlangen-Nuremberg,Germany,in
2020.HeiscurrentlyworkingtowardthePhDdegree
withtheUniversityofTübingen,Germanywherehis
researchisfocusedontrustworthymachinelearning. GjergjiKasnecireceivedtheMScdegreeincom-
Specifically,hisresearchinterestsincludethequality puterscienceandmathematicsfromtheUniversity
assessmentofinterpretabilitytechniquesandthein- ofMarburg,in2005,andthePhDdegreefromthe
tersectionsofinterpretability,fairnessandprivacy. UniversityofSaarland-whilewiththeMaxPlanck
Institute-in2009.HethenworkedwithMicrosoft
ResearchCambridge,theHassoPlattnerInstitute,and
SCHUFAHoldingAG,whereheservedasCTOfrom
2017to2022.Between2018and2023,heledtheData
Thai-TrangNguyenisgraduatedwithaBScdegree
ScienceandAnalyticsGroupwiththeUniversityof
incomputersciencefromtheUniversityofTübingen,
TübingenasanHonoraryprofessor.In2023,Gjergji
Germany.SheiscurrentlyworkingtowardtheMSc
KasneciwasappointedprofessorofResponsibleData
degree with the same university. Furthermore, she
SciencewiththeTechnicalUniversityofMunich.
servedasaresearchassistant,theHuman-Computer
Interactiongroupfrom2019to2022.
Enkelejda Kasneci received the PhD degree in
computersciencefromtheUniversityofTübingen,
in 2013. She was postdoctoral researcher and a
Margarete-von-WrangellFellowwiththeUniversity
Lisa Fiedler is currently working toward the BSc of Tübingen. She is a distinguished professor for
degreeinmediainformaticsfromtheUniversityof Human-CenteredTechnologiesforLearningwiththe
Tübingen, Germany. Additionally, she works as a TechnicalUniversityofMunichandCoreMember
studentassistantfortheHuman-ComputerInteraction oftheMunichDataScienceInstitute.Herresearch
GroupattheUniversityofTübingen. evolves around Human-Centered Technologies and
AIsystemsthatsenseandinfertheuser’scognitive
state,theleveloftask-relatedexpertise,actions,and
intentionsbasedonmultimodaldataandprovideinformationformediaand
assistivetechnologiesinmanyactivitiesofeverydaylife,andespeciallyinthe
contextoflearning.