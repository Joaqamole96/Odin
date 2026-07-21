---
conversion_metadata:
  converted_at: "2026-07-21T06:07:20Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Essahraui et al.pdf"
  source_pdf_sha256: "25b8f02262ca05a72ebc71d84d753d444ce86c9772624c1dce5ca1c39d618e75"
  page_count: 41
  markdown_char_count: 288308
---

Received7May2025,accepted13July2025,dateofpublication16July2025,dateofcurrentversion25July2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3589938
Human Behavior Analysis: A Comprehensive
Survey on Techniques, Applications,
Challenges, and Future Directions
SIHAMESSAHRAUI 1,(StudentMember,IEEE),
ISMAILLAMAAKAL 1,(StudentMember,IEEE),
YASSINEMALEH 2,(SeniorMember,IEEE),KHALIDELMAKKAOUI1,(SeniorMember,IEEE),
MOUNCEFFILALIBOUAMI 1,IBRAHIMOUAHBI 1,
AHMEDA.ABDEL-LATIF 3,4,(SeniorMember,IEEE),MAYALMOUSA 5,
ANDJOELJ.P.C.RODRIGUES 6,(Fellow,IEEE)
1MultidisciplinaryFacultyofNador,MohammedPremierUniversity,Oujda60000,Morocco
2LaboratoryLaSTI,ENSAK,SultanMoulaySlimaneUniversity,Khouribga54000,Morocco
3EIASDataScienceLaboratory,CollegeofComputerandInformationSciences,CenterofExcellenceinQuantumandIntelligentComputing,PrinceSultan
University,Riyadh11586,SaudiArabia
4DepartmentofMathematicsandComputerScience,FacultyofScience,MenoufiaUniversity,ShebeenEl-Kom32511,Egypt
5InformationTechnologyDepartment,CollegeofComputerandInformationSciences,PrincessNourahbintAbdulrahmanUniversity,Riyadh11671,
SaudiArabia
6FederalUniversityofPiauí(UFPI),Teresina,Piauí64049-550,Brazil
Correspondingauthor:YassineMaleh(yassine.maleh@ieee.org)
ThisworkwassupportedinpartbytheResearchersSupportingProject,PrincessNourahbintAbdulrahmanUniversity,Riyadh,
SaudiArabia,underGrantPNURSP2025R752;inpartbytheResearch,Development,andInnovationAuthority(RDIA),SaudiArabia,
underGrant13325-psu-2023-PSNU-R-3-1-EF;andinpartbyBrazilianNationalCouncilforScientificandTechnologicalDevelopment
(CNPq),underGrant306607/2023-9.
ABSTRACT HumanBehaviorAnalysis(HBA)hasemergedasacriticalinterdisciplinaryfield,combining
psychology, sociology, artificial intelligence, and data science to model, understand, and predict human
behavioracrossdiversedomains.Thispaperprovidesacomprehensivesurvey,addressinggapsinexisting
literature by exploring applications, techniques, challenges, and future directions. We begin by defining
HBA,tracingitshistoricalroots,andoutliningcoreconceptssuchasbehavioralpatterns,cognitiveprocesses,
andemotionalstates.Thesurveythenexplorestraditionalandmoderntechniques,frommanualobservation
to AI-driven methods such as deep learning, natural language processing, and computer vision. A key
contributionisourextensivecoverageofHBAapplicationsinhealthcare,marketing,education,workplace
productivity, activity recognition, and criminal justice. For each domain, we provide detailed examples
of how HBA enhances outcomes and decision-making. The survey also delves into data sources and
methodologiesusedinHBA,suchassensordata,socialmediadata,physiologicalsignals,andmultimodal
analysis. We discuss major challenges such as data privacy, generalization, real-time processing, and
scalability. Finally, we highlight emerging trends and future directions, including edge computing, Large
LanguageModels,privacy-preservingtechniques,andcross-disciplinaryapproaches.Byofferingaholistic
review,thissurveyaimstoguidefutureresearchandinnovationintheevolvingfieldofHBA.
INDEX TERMS Humanbehavioranalysis,humanactivityrecognition,InternetofThings,deeplearning,
machinelearning,computervision,naturallanguageprocessing.
I. INTRODUCTION
The associate editor coordinating the review of this manuscript and Human Behavior Analysis is an interdisciplinary field that
approvingitforpublicationwasMostafaM.Fouda . seeks to understand, model, and predict human actions,
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME13,2025 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 128379

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
reactions, and interactions. By analyzing patterns in human TABLE1. Listofabbreviations.
| behavior,  | HBA | systems | aim         | to     | provide | insights | into   |     |     |     |     |     |     |     |
| ---------- | --- | ------- | ----------- | ------ | ------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| individual | and | group   | activities, | mental | states, | and      | social |     |     |     |     |     |     |     |
dynamics[1].Thestudyofhumanbehavioriscriticalacross
| various              | fields, | including | healthcare, |               | marketing, | education, |            |     |     |     |     |     |     |     |
| -------------------- | ------- | --------- | ----------- | ------------- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| public safety,       | and     | workplace |             | productivity, |            | as it      | offers a   |     |     |     |     |     |     |     |
| deeper understanding |         | of        | how         | individuals   | engage     |            | with their |     |     |     |     |     |     |     |
environmentandinteractwithothers.
| The significance |            | of            | HBA | lies in         | its ability | to       | translate |     |     |     |     |     |     |     |
| ---------------- | ---------- | ------------- | --- | --------------- | ----------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| complex          | behavioral | patterns      |     | into actionable |             | insights | [2].      |     |     |     |     |     |     |     |
| In healthcare,   |            | for instance, |     | monitoring      |             | patient  | behavior  |     |     |     |     |     |     |     |
| can enable       | early      | detection     |     | of health       | problems    |          | such as   |     |     |     |     |     |     |     |
stress,anxiety,orphysicalailments.Similarly,inmarketing,
| analyzing       | consumer         | behavior      |              | provides     | companies   |            | with the   |     |     |     |     |     |     |     |
| --------------- | ---------------- | ------------- | ------------ | ------------ | ----------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| ability to      | tailor           | products,     | services,    | and          | marketing   |            | strategies |     |     |     |     |     |     |     |
| to better       | meet             | consumer      | needs        | [3].         | In          | education, | HBA        |     |     |     |     |     |     |     |
| can improve     | learning         |               | outcomes     | by           | identifying |            | individual |     |     |     |     |     |     |     |
| learning        | patterns         | and providing |              | personalized |             | feedback   | [4].       |     |     |     |     |     |     |     |
| The versatility |                  | of HBA        | applications |              | makes       | it         | an essen-  |     |     |     |     |     |     |     |
| tial tool       | in understanding |               |              | human        | behavior    | in         | modern     |     |     |     |     |     |     |     |
society.
Historically,theanalysisofhumanbehaviorreliedheavily
| on qualitative | methods, |     | such | as interviews, |     | surveys, | and |     |     |     |     |     |     |     |
| -------------- | -------- | --- | ---- | -------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
observationsconductedbypsychologistsandsociologists[5].
| While these      | methods       | provided    |              | valuable       | insights        |               | into indi- |     |     |     |     |     |     |     |
| ---------------- | ------------- | ----------- | ------------ | -------------- | --------------- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| vidual behaviors |               | and social  | trends,      | they           | were            | often         | limited    |     |     |     |     |     |     |     |
| by the           | small scale   | of          | data         | and subjective |                 | biases.       | The        |     |     |     |     |     |     |     |
| emergence        | of digital    |             | technologies |                | has transformed |               | HBA        |     |     |     |     |     |     |     |
| into a           | data-driven   | discipline. |              | With           | the             | proliferation | of         |     |     |     |     |     |     |     |
| smartphones      | [6],          | wearable    | devices,     |                | and social      | media,        | vast       |     |     |     |     |     |     |     |
| amounts          | of behavioral |             | data are     | now            | available,      | allowing      | for        |     |     |     |     |     |     |     |
| large-scale,     | real-time     | analysis    |              | of human       | activities      |               | [7], [8].  |     |     |     |     |     |     |     |
Thisshifthassignificantlyenhancedtheaccuracy,scalability,
andapplicabilityofHBAacrossdifferentdomains.
| Modern | HBA | leverages | advanced |     | technologies |     | such as |     |     |     |     |     |     |     |
| ------ | --- | --------- | -------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
artificialintelligence(AI),machinelearning(ML)[10],and
sensornetworkstoanalyzevariousformsofdata,including
| physiological | signals   | [11],  | facial | expressions  |     | [12], | speech |     |     |     |     |     |     |     |
| ------------- | --------- | ------ | ------ | ------------ | --- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
| patterns      | [13], and | social | media  | interactions |     | [14]. | These  |     |     |     |     |     |     |     |
technologiesenableautomated,real-timeanalysisofhuman
| behavior,    | providing | insights | that     | were      | previously |         | unattain- |     |     |     |     |     |     |     |
| ------------ | --------- | -------- | -------- | --------- | ---------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| able through | manual    |          | methods. | For       | example,   | AI      | models    |     |     |     |     |     |     |     |
| can now      | analyze   | video    | feeds    | to detect | subtle     | changes | in a      |     |     |     |     |     |     |     |
person’sfacialexpressionsorbodylanguage[15],indicating
|     |     |     |     |     |     |     |     | into human | actions | [19]. As | a result, | HBA | has moved | from |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | --------- | --- | --------- | ---- |
emotionalstatessuchasstressorhappiness.Similarly,natural
|     |     |     |     |     |     |     |     | being a | passive | tool for observation |     | to an | active system | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | -------------------- | --- | ----- | ------------- | --- |
languageprocessingtechniquesareusedtoanalyzetextdata,
suchassocialmediapostsoremails[16],togaugesentiment real-timedecision-makingandintervention.
andpsychologicalwell-being.
One of the key strengths of contemporary HBA is its A. PAPERMOTIVATION
|     |     |     |     |     |     |     |     | The motivation |     | for this survey | stems | from | the lack | of com- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------- | ----- | ---- | -------- | ------- |
abilitytointegratemultipledatasources.Bycombiningdata
from wearables, video feeds [17], social interactions, and prehensivestudiesthatcovertheentirescopeofHBA.While
environmental sensors [18], HBA systems create a more severalsurveysexistonHumanActivityRecognition(HAR)
orHumanBehaviorRecognition(HBR),theseonlyrepresent
comprehensivepictureofhumanbehavior.Thismultimodal
approach enables the detection of complex patterns, such partsofthebroaderfieldofHBA.Oursurveyaimstoaddress
|     |     |     |     |     |     |     |     | this gap | by offering | a comprehensive |     | review | that | includes |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --------------- | --- | ------ | ---- | -------- |
astherelationshipbetweenphysicalhealth,emotionalwell-
being, and social behaviors, offering more nuanced insights all major application domains of HBA, such as Healthcare,
| 128380 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
HAR, Marketing and Consumer Behavior, Education and techniques such as motion detection, object classification,
Learning,WorkplaceProductivityandEmployeeWell-being and motion tracking, which form the building blocks of
and more. Another significant motivation is the absence of behavioranalysis.Thesurveyalsoexploredtheintegrationof
surveys that explore the future trends in HBA, such as the semantic analysis to improve accuracy and domain-specific
integrationofedgecomputing,LargeLanguageModelsand event recognition, while addressing the challenges and
other emerging technologies. Our work seeks to fill these limitations in areas such as occlusion handling, person
gapsbyprovidingaholisticviewofHBAandrecommending identification,andsceneclassification.
futureresearchdirections. Unlikeprevioussurveysthatprimarilycatalogalgorithms
|     |     |     |     |     |     |     |     | or focus | on narrow | subdomains | such | as Human | Activity |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | ---- | -------- | -------- | --- |
B. CRITICALREVIEWOFEXISTINGSURVEYS Recognition or behavior modeling in isolated contexts, this
This section provides a critical review of prior surveys review is designed to offer a holistic and critical synthesis
|         |          |         |     |       |          |           |     | of the HBA | landscape. |     | Our goal | is not merely | to  | sum- |
| ------- | -------- | ------- | --- | ----- | -------- | --------- | --- | ---------- | ---------- | --- | -------- | ------------- | --- | ---- |
| and key | research | efforts | in  | Human | Behavior | Analysis, |     |            |            |     |          |               |     |      |
highlighting their scope, methodological frameworks, and marize existing techniques, but to analyze methodological
limitations in orderto contextualize the contributions ofthe patterns, highlight domain-specific challenges, and identify
present work. Below, we provide a brief summary of the overarching limitations across a wide range of application
mostsignificantrelatedworksandhowtheycontributetothe areas—including healthcare, education, marketing, public
safety,workplacewell-being,andfinancialdecision-making.
currentunderstandingofHBA(seeTable2).
Bruno et al. [20] provided a comprehensive overview By comparing models, evaluation approaches, data sources,
of advancements in human action recognition, highlighting and deployment barriers, we aim to surface research gaps
|                |      |             |     |          |         |          |     | and actionable | insights |     | that can inform | future | work. | This |
| -------------- | ---- | ----------- | --- | -------- | ------- | -------- | --- | -------------- | -------- | --- | --------------- | ------ | ----- | ---- |
| the transition | from | handcrafted |     | features | to deep | learning |     |                |          |     |                 |        |       |      |
techniques.Itcategorizestheproblemintoactionclassifica- survey also integrates cross-domain discussions, ethical
considerations,andemergingtrendssuchasedgecomputing
tionandspatiotemporalactionlocalization,discussescurrent
challengessuchasinferencetimeandvideoannotationcom- and privacy-preserving AI to ensure a forward-looking
plexities, and emphasizes the need for unified architectures perspective.Indoingso,weaimtopositionthisworknotjust
asarepositoryofknowledge,butasaroadmapforadvancing
andsemi-supervisedlearningapproaches.Thesurveyserves
as a valuable resource for understanding the state-of-the-art thefieldofHBAinboththeoryandpractice.
methodsandfuturedirectionsinthefieldofHBA.
| Andrew         | et         | al. [21]       | focused          | on modeling,  |           | replicating, |         |                      |                |     |                 |     |            |        |
| -------------- | ---------- | -------------- | ---------------- | ------------- | --------- | ------------ | ------- | -------------------- | -------------- | --- | --------------- | --- | ---------- | ------ |
|                |            |                |                  |               |           |              |         | C. MAINCONTRIBUTIONS |                |     |                 |     |            |        |
| and predicting |            | human behavior |                  | in artificial | systems,  |              | high-   |                      |                |     |                 |     |            |        |
|                |            |                |                  |               |           |              |         | The main             | contributions  |     | of this survey  | are | summarized | as     |
| lighting       | techniques | such           | as reinforcement |               | learning  | to           | learn   | follows:             |                |     |                 |     |            |        |
| behavior       | models     | through        | exploration      | and           | feedback, |              | as well |                      |                |     |                 |     |            |        |
|                |            |                |                  |               |           |              |         | • The                | paper provides |     | a comprehensive |     | review     | of the |
| as methods     | for        | modeling       | human            | reasoning     | processes |              | such    |                      |                |     |                 |     |            |        |
as beliefs and biases. The key contributions included a field of HBA, covering its definition, core concepts
detailedanalysisofhowAIagentscouldbetterinteractwith (behavioral patterns, cognitive processes, emotional
|        |             |      |       |         |                   |     |     | states), | and | historical | context, | with a focus | on modern |     |
| ------ | ----------- | ---- | ----- | ------- | ----------------- | --- | --- | -------- | --- | ---------- | -------- | ------------ | --------- | --- |
| humans | by learning | from | human | actions | and understanding |     |     |          |     |            |          |              |           |     |
mental states, which enabled human-AI hybrid systems to AI-basedmethods.
operate more effectively together. The survey also covered • The survey systematically explores a wide range of
applications in autonomous systems, human-AI interaction, application domains of HBA, including healthcare
and adaptive learning techniques, providing insights into and well-being, marketing and consumer behavior,
activityrecognition,educationandlearning,workplace
futuredevelopmentsinhuman-centricAI.
Alejandroetal.[22]providedacomprehensiveoverviewof productivity and employee well-being, and criminal
thesystematicidentification,analysis,andcategorizationof justiceandpublicsafety.
Thepaperpresentsadetailedreviewofmodernmethod-
| relevantworksinthefieldofUserBehaviorAnalysis(UBA) |     |     |     |     |     |     |     | •   |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
across domains such as cybersecurity, networks, safety and ologiesinHBA,includingML,DL,NLP,andcomputer
|         |             |          |              |     |     |            |     | vision, | showing | how | these advanced | techniques |     | have |
| ------- | ----------- | -------- | ------------ | --- | --- | ---------- | --- | ------- | ------- | --- | -------------- | ---------- | --- | ---- |
| health, | and service | delivery | improvement. |     | It  | introduced | a   |         |         |     |                |            |     |      |
global relevance score for ranking papers and provided a transformedbehavioralanalysis.
graphical visualization based on similarity metrics, offering • Thesurveyoffersacomprehensiveanalysisofthedata
sourcesusedinHBA,suchassensordata,socialmedia
| insights | and guidelines |     | for researchers |     | interested | in  | UBA. |     |     |     |     |     |     |     |
| -------- | -------------- | --- | --------------- | --- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
The survey also highlighted the strong and weak points of data,andphysiologicalsignals.Italsodiscussesvarious
datacollectiontechniquessuchaswearabledevices,IoT
existingapproachesandidentifiedopenchallengesandfuture
researchdirections. sensors, and mobile apps. It discuss also benchmark
Gowsikhaaetal.[23]providedacomprehensiveoverview datasetsforHBAApplications.
Acriticalexaminationofthechallengesandlimitations
| of automated | HBA | from | surveillance |     | videos, | focusing | on  | •   |     |     |     |     |     |     |
| ------------ | --- | ---- | ------------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
methods for detecting, classifying, and tracking abnormal in HBA is provided, addressing issues such as data
|            |              |     |           |               |     |     |       | privacy, | generalization |     | and bias | in models, | real-time |     |
| ---------- | ------------ | --- | --------- | ------------- | --- | --- | ----- | -------- | -------------- | --- | -------- | ---------- | --------- | --- |
| activities | for enhanced |     | security. | It emphasized |     | the | shift |          |                |     |          |            |           |     |
from manual to automated surveillance, highlighting key processing,andscalability.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 128381 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE2. Criticalcomparisonofexistingsurveysandourwork.
• The paper identifies emerging trends and future direc- employedusingtermssuchas‘‘HumanBehaviorAnalysis’’,
tions in HBA, including the integration of edge com- ‘‘Behavioral Modeling’’, ‘‘Behavior Prediction’’, ‘‘Human
puting,LargeLanguageModels,AI-poweredbehavioral Behavior Recognition’’, ‘‘Affective Computing’’, ‘‘Emo-
models,andadvancedsensingtechnologies.Thesurvey tion Recognition’’, ‘‘AI for Behavior Understanding’’, and
also highlights cross-disciplinary approaches and the ‘‘Machine Learning for Behavior Modeling’’. Additionally,
roleofprivacy-preservingtechniquessuchasfederated application-specific terms were incorporated to capture the
learninganddifferentialprivacy. breadth of cross-domain relevance. These included ‘‘HBA
• Thesurveyhighlightstheimportanceofethicalconsid- inHealthcare’’,‘‘HBAinMarketing’’,‘‘ConsumerBehavior
erations in HBA, particularly recommending privacy- Prediction’’, ‘‘Behavior Analysis in Education’’, ‘‘Behavior
preserving methodologies. It stresses the necessity for Monitoring in Learning Environments’’, ‘‘Workplace Pro-
future advancements in the field to align with ethical ductivityPrediction’’,‘‘MentalHealthandStressDetection’’,
standards. ‘‘CrimePredictionusingAI’’,‘‘PublicSafetyandBehavioral
Analysis’’,‘‘DriverBehaviorPrediction’’,‘‘HumanActivity
D. PAPERORGANIZATION Recognition’’, and ‘‘Behavioral Finance Analysis’’. The
Thestructureofthissurveyisorganizedasfollows(seeFig- search was conducted across multiple leading academic
ure 1): Section I introduces the background and motivation databases, including IEEE Xplore, ACM Digital Library,
forHBA.SectionIIIprovidesanoverviewofHBA,including Scopus, Web of Science, SpringerLink, ScienceDirect, and
its key concepts, historical context, and modern techniques. Wiley Online Library. Only peer-reviewed journal articles,
Section IV discusses the data sources and methodologies conference proceedings, and high-quality technical reports
employedinHBA.SectionVreviewsthevariousapplication publishedbetween2020and2024wereconsideredtoensure
domains of HBA. Section VI addresses the challenges and relevancetorecentadvancements.Thefocuswasonstudies
limitations in HBA, including data privacy and scalability. that applied AI, ML, or DL techniques to analyze, predict,
SectionVIIexploresfuturetrendsandemergingtechnologies or model human behavior in diverse domains such as
inHBA.Finally,SectionVIIIconcludeswithasummaryof healthcare, education, workplace environments, marketing,
keyfindingsandimplicationsforfutureresearch. transportation,andpublicsafetyandmore.
II. REVIEWMETHODOLOGY B. INCLUSION/EXCLUSIONCRITERIA
Inthissection,wepresentthereviewmethodologyemployed Table3presentstheinclusionandexclusioncriteriaapplied
to explore the current landscape of HBA. A systematic and inourstudyselectionprocesstoensuretherelevance,quality,
structured approach was adopted to ensure comprehensive and scientific rigor of the surveyed papers. The inclusion
coverage of the literature, eliminate bias, and support the criteria emphasize research that directly applies ML, DL,
critical synthesis of trends, technologies, and application orAItechniquestoHBAacrossmultipledomains,including
domains. This section details the search strategy, inclusion butnotlimitedtohealthcare,education,transportation,work-
andexclusioncriteria,andtheanalysismethodsusedtoderive placeproductivity,andpublicsafety.Studieswiththeoretical
insightsfromtheselectedbodyofliterature. models, empirical evaluations, or real-world applications
wereconsidered.Exclusioncriteriaweresettofilteroutnon-
A. SEARCHSTRATEGY relevant,outdated,ormethodologicallyweakpapersthatdo
To identify the relevant literature for this survey on not directly contribute to understanding or advancing the
HBA, a comprehensive keyword-based search strategy was HBAfield.
128382 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
| FIGURE1. | Paperorganization. |     |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
C. DATAANALYSIS sentedinproceedings(17outof18),indicatingaprevalence
Following the search and selection process, a total of ofrecent,possiblyongoingstudies.
202relevantpaperswereidentifiedandanalyzedacrosseight Marketing and Consumer Behavior presented 17 papers
|     |     |     |     | (13 articles | and | 4 proceedings), | focusing | on behavioral |     |
| --- | --- | --- | --- | ------------ | --- | --------------- | -------- | ------------- | --- |
coredomainsofHBA(seeFigure2).Thesedomainsinclude
healthcare and mental health, marketing and consumer analysis in commercial settings. Lastly, Financial Decision-
behavior, education and learning, workplace productivity Making included 20 papers (7 articles and 13 proceedings),
andemployeewell-being,criminaljusticeandpublicsafety, illustrating the integration of behavioral modeling into
humanactivityrecognition,transportationandmobility,and economicsystemsandriskmanagement.
|     |     |     |     | This analysis |     | highlights | not only the | cross-disciplinary |     |
| --- | --- | --- | --- | ------------- | --- | ---------- | ------------ | ------------------ | --- |
financialdecision-making.
Out of the 202 papers, 134 were journal articles and nature of HBA but also the differing levels of maturity
61wereconferenceproceedings,withanadditional7being and dissemination across domains. It offers a robust foun-
|     |     |     |     | dation for | synthesizing | methodological |     | patterns, evaluating |     |
| --- | --- | --- | --- | ---------- | ------------ | -------------- | --- | -------------------- | --- |
categorizedaspreprints.Nobookchapters,books,ormono-
graphswereincludedinthefinalselection.HumanActivity application-specificinsights,andidentifyingareasrequiring
Recognition emerged as the most represented area with furtherscholarlyattention.
| 47papers(33articles |           | and14proceedings),highlightingthe |          |     |     |     |     |     |     |
| ------------------- | --------- | --------------------------------- | -------- | --- | --- | --- | --- | --- | --- |
| maturity            | and depth | of research in this subdomain.    | Criminal |     |     |     |     |     |     |
III. HUMANBEHAVIORANALYSIS:ANOVERVIEW
JusticeandPublicSafetyfollowedwith36papers(24articles,
|     |     |     |     | HBA refers | to  | the process | of studying | human actions, |     |
| --- | --- | --- | --- | ---------- | --- | ----------- | ----------- | -------------- | --- |
5proceedings,and7preprints),reflectingagrowinginterest
|     |     |     |     | reactions, | cognitive | processes, | and | emotional states | in  |
| --- | --- | --- | --- | ---------- | --------- | ---------- | --- | ---------------- | --- |
inbehaviormodelinginpublicsafetyenvironments.
|     |     |     |     | different | environments | (see | Figure 3). | The core concepts |     |
| --- | --- | --- | --- | --------- | ------------ | ---- | ---------- | ----------------- | --- |
Educationandlearningcontributed26papers(24articles
behindHBAinclude:
| and 2 proceedings), |     | while Transportation | and Mobility |     |     |     |     |     |     |
| ------------------- | --- | -------------------- | ------------ | --- | --- | --- | --- | --- | --- |
accountedfor20papers(15articlesand5proceedings).Both • Behavioral Patterns [24]: Refers to the regular and
Healthcare and Mental Health and Workplace Productivity predictable actions exhibited by individuals or groups
andEmployeeWell-beingyielded18paperseach.However, over time. These patterns are often detected through
workplace productivity research was almost entirely repre- observation, data collection, and analysis of behaviors
| VOLUME13,2025 |     |     |     |     |     |     |     |     | 128383 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE3. Inclusion/exclusioncriteriaforselectingstudiesonHBA.
facialexpressions,speech,andphysiologicalresponses,
providingvaluableinsightsintounderlyingmotivations
andactions.
| The study        | of  | human  | behavior has       | evolved | significantly |           |
| ---------------- | --- | ------ | ------------------ | ------- | ------------- | --------- |
| from its origins | in  | fields | such as psychology |         | and           | sociology |
tomoderndata-driventechniques.Historically,psychology-
| based approaches |     | [27] | relied on | observational |     | studies, |
| ---------------- | --- | ---- | --------- | ------------- | --- | -------- |
surveys,andexperimentstounderstandindividualandgroup
| behavior.       | These | methods | were often | limited | by       | subjective |
| --------------- | ----- | ------- | ---------- | ------- | -------- | ---------- |
| interpretation, | small | sample  | sizes,     | and a   | reliance | on self-   |
reporteddata.
| In parallel,   | sociology-based |             | approaches |          | [28] | examined  |
| -------------- | --------------- | ----------- | ---------- | -------- | ---- | --------- |
| human behavior |                 | in societal | contexts,  | focusing |      | on social |
structures,norms,andgroupdynamics.Theseearlymethods
FIGURE2. Distributionofpapersbyapplicationareareviewedinthis
| laid the groundwork |     | for | understanding | human | behavior | in  |
| ------------------- | --- | --- | ------------- | ----- | -------- | --- |
survey.
relationtotheenvironment,buttheylackedthecomputational
powertoprocesslarge-scalebehavioraldata.
in specific contexts, such as social interactions, online With the advent of AI and ML, the field of HBA
activities,orphysicalmovements. underwentatransformation.AI-poweredapproachesenable
Cognitive Processes [25]: These are mental processes the analysis of vast datasets, capturing behavioral nuances
•
involved in gaining knowledge and understanding, thatwerepreviouslydifficulttoobserve.Forexample,facial
including memory, attention, perception, and decision- recognition technologies can identify micro-expressions,
making. HBA examines how these processes influence speech analysis can detect emotional tone, and wearable
observable behaviors, such as responses to stimuli or sensorscanmonitorphysiologicalsignalssuchasheartrate
problem-solvingapproaches. ormovementpatterns.
• Emotional States [26]: Human emotions play a critical Modern HBA techniques use a combination of big data,
role in influencing behavior. Emotions such as happi- NLP, and DL to automate the analysis of human behavior.
ness, sadness, fear, or anger can be analyzed through This shift has enabled real-time analysis, scalable models,
128384 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
and more objective, data-driven insights, making HBA real-time insights. This section outlines both traditional and
applicabletovariousindustriessuchashealthcare,marketing, moderntechniquesusedinHBAandprovidesacomparative
| education,andsecurity.    |     |     |     |     |     |     | analysis.                |            |     |            |         |           |
| ------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | ---------- | --- | ---------- | ------- | --------- |
| A. IMPORTANCEANDRELEVANCE |     |     |     |     |     |     | 1) TRADITIONALAPPROACHES |            |     |            |         |           |
|                           |     |     |     |     |     |     | Traditional              | approaches | to  | HBA relied | heavily | on manual |
HBAhasbecomeincreasinglyimportantintoday’sintercon-
nected,technology-drivenworld.Itsrelevancecanbeseenin data collection, observation, and subjective analysis. These
|     |     |     |     |     |     |     | methods were | often | used | in fields | such as | psychology, |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ---- | --------- | ------- | ----------- |
avarietyofreal-worldapplications:
|              |             |     |     |     |      |              | sociology, | and anthropology, |     | focusing | on understanding |     |
| ------------ | ----------- | --- | --- | --- | ---- | ------------ | ---------- | ----------------- | --- | -------- | ---------------- | --- |
| • Healthcare | Monitoring: |     | HBA | is  | used | for monitor- |            |                   |     |          |                  |     |
individualandgroupbehaviorwithinspecificenvironments.
| ing patients’ |     | behaviors, | detecting |     | abnormalities, | and |     |     |     |     |     |     |
| ------------- | --- | ---------- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Keytraditionaltechniquesinclude:
| improving | treatment |     | plans. | For | example, | wearable |          |              |     |                   |          |      |
| --------- | --------- | --- | ------ | --- | -------- | -------- | -------- | ------------ | --- | ----------------- | -------- | ---- |
|           |           |     |        |     |          |          | • Manual | Observations |     | [29]: Researchers | observed | sub- |
devicestrackphysicalactivity,sleeppatterns,andheart
rates, which can help in managing chronic conditions jects in natural or controlled environments, noting
|              |       |       |             |        |     |             | behavioral | patterns, | reactions, |     | and social | interactions. |
| ------------ | ----- | ----- | ----------- | ------ | --- | ----------- | ---------- | --------- | ---------- | --- | ---------- | ------------- |
| or detecting | early | signs | of illness. | Mental |     | health mon- |            |           |            |     |            |               |
Theseobservationswereoftensubjectiveanddependent
itoringthroughHBAhelpsidentifyearlysignsofstress,
ontheskilloftheobserver.
| anxiety, | or depression |     | by analyzing |     | speech | patterns, |                 |     |             |       |               |         |
| -------- | ------------- | --- | ------------ | --- | ------ | --------- | --------------- | --- | ----------- | ----- | ------------- | ------- |
|          |               |     |              |     |        |           | • Psychological |     | Evaluations | [30]: | Psychological | assess- |
socialmediaactivity,andphysiologicalindicators.
SmartEnvironments:HBAiscrucialforcreatingadap- ments, such as personality tests, cognitive evaluations,
•
andself-reports,werewidelyusedtounderstandbehav-
tivesystemsthatrespondtouserbehaviors.Forinstance,
|             |     |                |     |      |           |           | ior from | a mental | health | perspective. | While | effective |
| ----------- | --- | -------------- | --- | ---- | --------- | --------- | -------- | -------- | ------ | ------------ | ----- | --------- |
| smart homes |     | use behavioral |     | data | to adjust | lighting, |          |          |        |              |       |           |
forcertainanalyses,thesemethodsoftensufferedfrom
| temperature, | and | security | settings | automatically |     | based |     |     |     |     |     |     |
| ------------ | --- | -------- | -------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
biasesandwerelimitedtosmallsamplesizes.
onresidents’preferencesandroutines.Intransportation,
HBA is applied in autonomous vehicles, traffic man- • Survey-Based Data Collection [31]: Surveys and ques-
tionnaireswereusedtogatherinformationonattitudes,
agement,andpublictransportationsystemstooptimize
|     |     |     |     |     |     |     | beliefs, | and behaviors. |     | This method | allowed | for data |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ----------- | ------- | -------- |
routes,reducecongestion,andimprovesafety.
Security:HBAisintegraltoenhancingsecuritysystems, collectionfromlargerpopulationsbutwasoftenlimited
•
byself-reportbiasandthereliabilityofresponses.
| both in | physical | and | digital | spaces. | By  | analyzing |     |     |     |     |     |     |
| ------- | -------- | --- | ------- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- |
behaviors such as gait, facial expressions, or online • Ethnographic Studies [32]: Long-term observational
|           |         |     |        |           |     |               | studies | where | researchers | embedded | themselves | in the |
| --------- | ------- | --- | ------ | --------- | --- | ------------- | ------- | ----- | ----------- | -------- | ---------- | ------ |
| activity, | systems | can | detect | anomalies |     | that indicate |         |       |             |          |            |        |
cultureorenvironmenttheywerestudyingtounderstand
potentialsecuritythreats.Incybersecurity,HBAhelpsin
identifyingmaliciousbehaviorpatternssuchasphishing human behavior in context. These studies provided
|     |     |     |     |     |     |     | rich qualitative |     | insights | but were | time-consuming | and |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | -------- | -------- | -------------- | --- |
attempts,unauthorizedaccess,orfraudulenttransactions
| byanalyzinguseractivityandnetworktraffic. |     |     |          |     |         |          | difficulttoscale. |             |     |         |          |              |
| ----------------------------------------- | --- | --- | -------- | --- | ------- | -------- | ----------------- | ----------- | --- | ------- | -------- | ------------ |
|                                           |     |     |          |     |         |          | While these       | traditional |     | methods | provided | foundational |
| • Education:                              | HBA | is  | employed | to  | enhance | learning |                   |             |     |         |          |              |
experiences by understanding how students interact knowledge of human behavior, they were often limited by
with educational materials and platforms. Adaptive their reliance on subjective interpretation, smaller datasets,
learning systems use behavior data to personalize andmanualprocessing,whichhinderedscalabilityandreal-
| instruction, | while | engagement |     | monitoring |     | tools track | timeapplication. |     |     |     |     |     |
| ------------ | ----- | ---------- | --- | ---------- | --- | ----------- | ---------------- | --- | --- | --- | --- | --- |
studentparticipationandprovidereal-timefeedbackto
| educators. |     |     |     |     |     |     | 2) MODERNTECHNIQUESINHBA |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- |
Marketing and Consumer Behavior: Companies lever- With advancements in AI, ML, and data science, HBA
•
age HBA to understand consumer preferences and has undergone a transformation. Modern approaches allow
tailor marketing strategies. Behavioral data, including for the collection, analysis, and interpretation of vast
purchasehistory,websiteinteractions,andsocialmedia amountsofbehavioraldatainreal-time,improvingboththe
activity, are analyzed to create personalized recom- scalability and accuracy of HBA. Key modern techniques
| mendations, | targeted |     | advertisements, |     | and | improved | include: |     |     |     |     |     |
| ----------- | -------- | --- | --------------- | --- | --- | -------- | -------- | --- | --- | --- | --- | --- |
customerserviceexperiences. Deep Learning (DL): DL models, particularly CNNs
•
|     |     |     |     |     |     |     | and RNNs, | are | used to | analyze | complex | data patterns. |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | ------- | ------- | -------------- |
B. TRADITIONALANDCONTEMPORARYAPPROACHES InHBA,DLisappliedtotaskssuchasemotiondetec-
The study of human behavior has evolved from traditional tion, facial recognition, and speech analysis, enabling
methodsinvolvingmanualdatacollectionandpsychological real-timebehaviormonitoring[33].
evaluation to modern approaches powered by advanced Natural Language Processing (NLP): NLP techniques
•
computationaltechniques.Traditionalapproacheswereoften are used to analyze textual and speech data, provid-
limited in scope and scale, while contemporary methods ing insights into emotions, intentions, and cognitive
leverage AI and ML to analyze large datasets and generate states [34]. For example, sentiment analysis is used
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 128385 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
FIGURE3. TheHBAworkflowfromdatacollectiontobehaviorrecognition.
to detect mood changes in social media posts, while data. Additionally, it highlights the challenges faced in data
chatbotsutilizeNLPtorespondbasedonuserinput. collectionandanalysis.
• ComputerVision:Computervisiontechniques,particu-
larlythoseusingDL,enabletheautomaticdetectionof
A. TYPESOFDATACOLLECTED
humanactions,facialexpressions,andmovements[35]. ThedatausedinHBAcomesfromdiversesources,capturing
| This | technology |     | is widely | used | in security |     | systems, |               |     |                      |     |                 |     |       |
| ---- | ---------- | --- | --------- | ---- | ----------- | --- | -------- | ------------- | --- | -------------------- | --- | --------------- | --- | ----- |
|      |            |     |           |      |             |     |          | both physical | and | digital interactions |     | of individuals. |     | These |
healthcaremonitoring,andhuman-computerinteraction
datatypesinclude:
toanalyzevisualbehavioraldata.
|          |           |           |                 |            |          |             |          | • Sensor      | Data:   | Collected          | from  | wearable      | devices       | (e.g.,   |
| -------- | --------- | --------- | --------------- | ---------- | -------- | ----------- | -------- | ------------- | ------- | ------------------ | ----- | ------------- | ------------- | -------- |
| • Sensor | Data      | Analysis  |                 | [36]:      | Wearable | sensors     | (e.g.,   |               |         |                    |       |               |               |          |
|          |           |           |                 |            |          |             |          | smartwatches, |         | fitness trackers), |       | environmental |               | sensors, |
| heart    | rate      | monitors, | accelerometers, |            | and      | GPS         | devices) |               |         |                    |       |               |               |          |
|          |           |           |                 |            |          |             |          | or IoT        | devices | [36].              | These | data capture  |               | physical |
| collect  | real-time |           | physiological   |            | and      | movement    | data.    |               |         |                    |       |               |               |          |
|          |           |           |                 |            |          |             |          | activities    | (e.g.,  | walking,           | heart | rate) and     | environmental |          |
| These    | sensors   | are       | used            | to monitor | health   | conditions, |          |               |         |                    |       |               |               |          |
factors(e.g.,temperature,lightlevels).
physicalactivity,andlocation-basedbehaviors,provid-
|     |            |      |      |     |             |     |          | • Behavioral |             | Logs: Behavioral |          | logs capture | interactions    |     |
| --- | ---------- | ---- | ---- | --- | ----------- | --- | -------- | ------------ | ----------- | ---------------- | -------- | ------------ | --------------- | --- |
| ing | continuous | data | that | can | be analyzed | for | behavior |              |             |                  |          |              |                 |     |
|     |            |      |      |     |             |     |          | between      | individuals | and              | systems, | such         | as clickstreams |     |
patterns.
onwebsites,appusage,andhuman-computerinteraction
• ReinforcementLearning:Thistechniqueisusedtotrain
logs[38].Theseareoftenusedtostudyonlinebehavior,
| models | that | can | predict | and | adapt to | human | behavior |     |     |     |     |     |     |     |
| ------ | ---- | --- | ------- | --- | -------- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
preferences,andengagement.
| over | time | [37]. For | instance, |     | in personalized |     | learning |     |     |     |     |     |     |     |
| ---- | ---- | --------- | --------- | --- | --------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
• SocialMediaData:DatafromplatformssuchasTwitter,
| environments, |         | systems |     | use reinforcement |       | learning | to       |           |     |               |     |          |               |     |
| ------------- | ------- | ------- | --- | ----------------- | ----- | -------- | -------- | --------- | --- | ------------- | --- | -------- | ------------- | --- |
|               |         |         |     |                   |       |          |          | Facebook, |     | and Instagram | are | analyzed | to understand |     |
| adapt         | content | based   | on  | how               | users | interact | with the |           |     |               |     |          |               |     |
emotionalstates,opinions,andsocialinteractions[39].
material.
Sentimentanalysisiscommonlyappliedtothistypeof
datatodetectmoodchangesortrends.
| Modern       | techniques |               | are             | data-driven, |                  | capable    | of pro-   |                 |              |               |            |               |       |           |
| ------------ | ---------- | ------------- | --------------- | ------------ | ---------------- | ---------- | --------- | --------------- | ------------ | ------------- | ---------- | ------------- | ----- | --------- |
|              |            |               |                 |              |                  |            |           | • Physiological |              | Signals       | [11]:      | These include | heart | rate,     |
| cessing vast | amounts    |               | of information, |              | and              | offer      | real-time |                 |              |               |            |               |       |           |
|              |            |               |                 |              |                  |            |           | skin            | conductance, | EEG           | (brain     | activity),    | and   | EMG       |
| insights     | into       | human         | behavior.       |              | These approaches |            | have      |                 |              |               |            |               |       |           |
|              |            |               |                 |              |                  |            |           | (muscle         | activity),   | collected     | through    | wearable      |       | devices   |
| been applied | across     |               | various         | fields,      | from             | healthcare | and       |                 |              |               |            |               |       |           |
|              |            |               |                 |              |                  |            |           | and             | specialized  | medical       | equipment. | This          | data  | type is   |
| smart cities | to         | cybersecurity |                 | and          | consumer         |            | behavior  |                 |              |               |            |               |       |           |
|              |            |               |                 |              |                  |            |           | essential       | for          | understanding |            | emotional     | and   | cognitive |
analysis.
statesinrealtime.
|     |     |     |     |     |     |     |     | Audio | and | Video Data: | Audio | recordings | of  | speech, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----------- | ----- | ---------- | --- | ------- |
•
|     |     |     |     |     |     |     |     | video | footage | of human | activity, | and facial | expression |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------- | -------- | --------- | ---------- | ---------- | --- |
IV. DATASOURCESANDMETHODOLOGIESFORHBA
|     |     |     |     |     |     |     |     | data | are used | for detecting | emotions, | analyzing |     | move- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ------------- | --------- | --------- | --- | ----- |
HBAreliesonavarietyofdatasourcesandmethodologiesto
capture, analyze, and interpret human actions and cognitive ments,andmonitoringbehavioralpatterns[40].
processes. This section explores the types of data used in These data types provide a comprehensive picture of
HBA, the techniques for collecting behavior-related data, human behavior, allowing researchers to model actions,
and the methodologies applied to analyze the collected cognitiveprocesses,andemotionalresponses.
| 128386 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
B. DATACOLLECTIONTECHNIQUES These methodologies enable deeper insights into human
behavior,providingbothdescriptiveandpredictiveanalytics
| Collecting | data | for HBA | involves | a   | variety | of techniques |     |     |     |     |     |     |     |     |     |
| ---------- | ---- | ------- | -------- | --- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that depend on the context and the specific behaviors being inHBAapplications.
studied.Keydatacollectionmethodsinclude:
|            |                |     |                     |           |      |         |          | D. BENCHMARKDATASETSFORHBAAPPLICATIONS |     |          |          |                 |                 |     |          |
| ---------- | -------------- | --- | ------------------- | --------- | ---- | ------- | -------- | -------------------------------------- | --- | -------- | -------- | --------------- | --------------- | --- | -------- |
| • Wearable | Devices        |     | [41]: Smartwatches, |           |      | fitness | track-   |                                        |     |          |          |                 |                 |     |          |
|            |                |     |                     |           |      |         |          | The following                          |     | section  | presents | a comprehensive |                 |     | overview |
| ers,       | and biosensors |     | collect             | real-time | data | on      | physical |                                        |     |          |          |                 |                 |     |          |
|            |                |     |                     |           |      |         |          | of key benchmark                       |     | datasets | that     | are             | widely utilized |     | in HBA   |
activity,heartrate,sleeppatterns,andmore.Wearables
tasks,coveringarangeofdomainsincludingHAR,sentiment
| provide | continuous |     | monitoring |     | and | are particularly |     |     |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ---------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
analysis,transportation,healthcare,andmore.
usefulinhealthcareandfitnessapplications.
| • IoT    | Sensors       | [36]: | IoT devices, |     | such        | as smart   | home |                                     |     |     |     |     |     |     |     |
| -------- | ------------- | ----- | ------------ | --- | ----------- | ---------- | ---- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|          |               |       |              |     |             |            |      | 1) HUMANACTIVITYRECOGNITIONDATASETS |     |     |     |     |     |     |     |
| systems, | environmental |       | sensors,     |     | and traffic | monitoring |      |                                     |     |     |     |     |     |     |     |
cameras, collect data on movement, temperature, light, Numerous benchmark datasets support the development
|     |           |       |         |        |     |            |     | and evaluation |     | of machine |     | learning | models | in  | human |
| --- | --------- | ----- | ------- | ------ | --- | ---------- | --- | -------------- | --- | ---------- | --- | -------- | ------ | --- | ----- |
| and | location. | These | sensors | enable | the | monitoring | of  |                |     |            |     |          |        |     |       |
activityrecognition.TheWISDMdataset[44]containsover
humanbehaviorinbothpersonalandpublicspaces.
|          |       |               |          |                |       |         |         | 1.1 million | accelerometer |             | readings |        | from 36  | users | and is  |
| -------- | ----- | ------------- | -------- | -------------- | ----- | ------- | ------- | ----------- | ------------- | ----------- | -------- | ------ | -------- | ----- | ------- |
| • Mobile | Apps: | Applications  |          | on smartphones |       | or      | tablets |             |               |             |          |        |          |       |         |
|          |       |               |          |                |       |         |         | commonly    | used          | to classify |          | motion | patterns | from  | typical |
| track    | user  | interactions, | location |                | data, | and app | usage   |             |               |             |          |        |          |       |         |
behavior. Mobile apps are effective for capturing a physical activities. The UCI-HAR dataset[45], collected
|      |       |         |       |           |     |     |           | from 30 | users | using smartphone |     | accelerometers |     | and | gyro- |
| ---- | ----- | ------- | ----- | --------- | --- | --- | --------- | ------- | ----- | ---------------- | --- | -------------- | --- | --- | ----- |
| wide | range | of user | data, | including |     | GPS | location, |         |       |                  |     |                |     |     |       |
scopes,includes10,299labeledinstancesacrosssixactivities
accelerometerdata,andonlinebehavior[42].
Web Platforms and Social Media: and serves as a standard baseline for activity recognition.
| •      |       |       |         |      | Web     | platforms     | and |             |     |          |      |      |             |            |     |
| ------ | ----- | ----- | ------- | ---- | ------- | ------------- | --- | ----------- | --- | -------- | ---- | ---- | ----------- | ---------- | --- |
|        |       |       |         |      |         |               |     | USC-HAD[46] |     | provides | data | from | 14 subjects | performing |     |
| social | media | sites | provide | data | on user | interactions, |     |             |     |          |      |      |             |            |     |
sentiments, and preferences. Tools such as browser 12 activities over a period of 7 hours, while PAMAP2 [47]
|             |     |          |         |          |         |      |      | includes | 18 labeled | physical |          | activities | from    | 9 participants |     |
| ----------- | --- | -------- | ------- | -------- | ------- | ---- | ---- | -------- | ---------- | -------- | -------- | ---------- | ------- | -------------- | --- |
| extensions, |     | tracking | pixels, | and APIs | collect | data | from |          |            |          |          |            |         |                |     |
|             |     |          |         |          |         |      |      | recorded | through    | multiple | wearable |            | sensors | for multimodal |     |
usersinteractingwithwebsitesandsocialnetworks[43].
recognitionandhealthmonitoring.TheDaphnetFoGdataset
These collection techniques provide rich, multidimen- [48]focusesondetectingfreezing-of-gaitepisodesinParkin-
sionaldatasetsthatsupportadvancedanalysisforunderstand- son’s disease patients using high-frequency accelerometer
inghumanbehaviorinvariouscontexts. data. The MHEALTH dataset[51] is another health-related
|     |     |     |     |     |     |     |     | dataset | capturing | physical | movements |     | and | vital signs | from |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------- | --------- | --- | --- | ----------- | ---- |
10individualsusingwearablesensors.Inindustrialenviron-
C. ANALYSISMETHODOLOGIES
|            |               |          |         |               |           |         |         | ments, the    | Skoda | dataset[49] |         | logs     | over 60,000 |          | annotated |
| ---------- | ------------- | -------- | ------- | ------------- | --------- | ------- | ------- | ------------- | ----- | ----------- | ------- | -------- | ----------- | -------- | --------- |
| Once data  | is collected, |          | various | methodologies |           | are     | applied |               |       |             |         |          |             |          |           |
|            |               |          |         |               |           |         |         | arm movements |       | from        | sensors | embedded | in          | workers’ | arms      |
| to analyze | behavioral    | patterns |         | and           | cognitive | states. | The     |               |       |             |         |          |             |          |           |
duringassemblytasks.Forvideo-basedrecognition,theKTH
followingarekeymethodologiesusedinHBA: dataset[50] includes 600 video sequences of six actions
|     |     |     |     |     |     |     |     | performed | by  | 25 subjects | under | four | different | scenarios, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- | ----- | ---- | --------- | ---------- | --- |
• Time-SeriesAnalysis:Time-seriesmethodsanalyzedata
|           |      |       |             |     |         |           |     | and the | UCF101 | dataset[55] |     | offers | over 13,000 | video | clips |
| --------- | ---- | ----- | ----------- | --- | ------- | --------- | --- | ------- | ------ | ----------- | --- | ------ | ----------- | ----- | ----- |
| collected | over | time, | identifying |     | trends, | patterns, | and |         |        |             |     |        |             |       |       |
sourcedfromYouTubeacross101actioncategories.Kinect-
anomaliesinbehavior.Forexample,time-seriesanalysis
|         |     |             |           |     |          |           |     | based datasets |     | such as | KARD[52] |     | and PKU-MMD[53] |     |     |
| ------- | --- | ----------- | --------- | --- | -------- | --------- | --- | -------------- | --- | ------- | -------- | --- | --------------- | --- | --- |
| is used | to  | study sleep | patterns, |     | physical | activity, | and |                |     |         |          |     |                 |     |     |
onlineengagementacrossdifferentperiods. include skeletal joint and depth data across a wide range of
activities,supportinggestureandinteractionrecognition.The
| • Behavior | Modeling: |     | Behavior |     | modeling    | techniques, |         |             |     |         |      |          |            |     |         |
| ---------- | --------- | --- | -------- | --- | ----------- | ----------- | ------- | ----------- | --- | ------- | ---- | -------- | ---------- | --- | ------- |
|            |           |     |          |     |             |             |         | OPPORTUNITY |     | dataset | [54] | provides | multimodal |     | record- |
| such       | as Markov |     | models   | and | agent-based |             | models, |             |     |         |      |          |            |     |         |
simulate human behavior in different scenarios. These ingsfromwearablesensorscapturing242datastreamsacross
|        |      |         |        |         |     |       |         | locomotion | and | gestures. | Finally, |     | the LIRIS | dataset[56] |     |
| ------ | ---- | ------- | ------ | ------- | --- | ----- | ------- | ---------- | --- | --------- | -------- | --- | --------- | ----------- | --- |
| models | help | predict | future | actions |     | based | on past |            |     |           |          |     |           |             |     |
behaviorsandenvironmentalconditions. presentsvideosequencesof10differentactivitiesrecordedin
realisticindoorsettings,offeringdiversescenariosforactivity
| • ML | Algorithms: | ML  | techniques, |     | including | supervised |     |     |     |     |     |     |     |     |     |
| ---- | ----------- | --- | ----------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classificationandrecognition.
| and   | unsupervised | learning, |     | are used | to       | classify | behav-   |     |     |     |     |     |     |     |     |
| ----- | ------------ | --------- | --- | -------- | -------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| iors, | predict      | outcomes, | and | identify | patterns |          | in large |     |     |     |     |     |     |     |     |
datasets.AlgorithmssuchasSVM,DT,RF,andNNare 2) PHYSIOLOGICALSIGNALDATASETS
commonlyapplied. Several benchmark datasets capture physiological signals
• Multimodal Analysis: Multimodal analysis combines relevant to HBA, especially for emotion and stress recog-
data from multiple sources (e.g., sensor data, video, nition. The CLAS dataset[57] contains PPG, ECG, and
audio) to provide a more holistic view of human EDA recordings from 62 participants who engaged in tasks
behavior. For example, combining video analysis with involving emotive imagery and video clips, with annotated
physiologicalsignalscanenhanceemotiondetectionand labels for stress, valence, and arousal. The DeepBreath
cognitivestateassessment. dataset[58] focuses on breathing patterns captured via
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 128387 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
thermal imaging near the nostrils, using a low-cost thermal sensor-basedmetricsthroughwearabledevicesforbehavioral
camera to assess psychological stress; data were collected andwellnessmonitoringinworkplaceenvironments.
fromeightparticipantsoversessionslasting63to72minutes.
TheASCERTAINdataset[59]offersmultimodalphysiolog-
6) TRANSPORTATIONANDMOBILITYDATASETS
ical responses, including EEG, ECG, and GSR, along with
Transportation and mobility datasets enable the analysis
facial activity captured via webcam while 58 participants
of driver behavior, distraction, fatigue, and stress through
viewed emotionally stimulating film clips. These datasets
multimodal signals and in-vehicle contexts. The State Farm
support the development of affective computing models
Distracted Driver Detection dataset [69] includes over
andstress-detectionsystemsusingwearableornon-intrusive
22,000labeleddashboardcameraimagesofdriversinvarious
sensors.
distracted states, used for classifying visual activities. The
Drive&Act dataset [70] provides 13 hours of data from
3) SPEECHDATASETS 15subjects,coveringover83in-caractivitiesthroughRGB,
In the domain of speech-based emotion and stress analysis, depth,thermal,3Dskeleton,andsynchronizedIMUsignals.
the SUSAS dataset[60] is widely used. It includes speech The Honda Research Institute Driving Dataset (HDD) [76]
recordings collected under stress across different speaking contains over 100 hours of real-world driving videos with
styles and environmental conditions. The dataset features GPS, IMU, and CAN bus data, annotated for high-level
35 potentially confusing aviation-related terms and consists driving actions and driver behaviors. Several datasets focus
of16,000utterancesfrom32speakers,makingitsuitablefor on physiological and cognitive monitoring during driving.
modelingstressdetectionandemotionrecognitionfromvocal TheSRADdataset [73]capturesfourtypesofphysiological
expressions. signals during driving sessions to assess driver stress. The
SEED-VIG dataset [71] collects EEG data to evaluate
4) FACIALEXPRESSIONDATASETS vigilance states like drowsiness and alertness. The MPDB
Facial expression datasets are widely used for training and dataset [77] integrates EEG, ECG, EMG, GSR, and eye
evaluating models in emotion recognition and stress detec- movement data from 35 participants in a driving simulator
tion. The CK+ dataset[61] includes 593 image sequences toclassifyfivecategoriesofdrivingbehavior.Similarly,the
from 123 participants, annotated for both facial expressions MDVFDD dataset [72] combines physiological, facial, eye-
and action units. The Oulu-CASIA dataset[62] provides tracking,andvehiclecontroldatafromsimulateddrivingto
facialexpressiondatafrom80individuals,coveringsixbasic study attention and fatigue. The DMD dataset [75] offers
emotions captured under three different lighting conditions. 41 hours of multimodal recordings from 37 drivers for
The KDEF dataset[63] consists of 4,900 images featuring distraction and behavior analysis. The ADARP dataset [74]
70 individuals expressing a range of emotional states. For targets mental health and stress detection in drivers with
real-worldapplications,theKMU-FEDdataset[64]captures alcohol use disorder by collecting HR, EDA, temperature,
55 sequences from 12 subjects in actual driving scenarios and movement signals. These datasets collectively support
using near-infrared cameras mounted inside vehicles. The research in autonomous driving, driver monitoring, human
FERETdataset[65],originallycreatedforfacialrecognition factors,andbehavioralmodelingintransportcontexts.
research, contains 14,126 facial images from 1,199 indi-
viduals collected over 15 sessions between 1993 and 1996.
7) HEALTHCAREDATASETS
Lastly, the ANUStressDB dataset[66] features thermal and Healthcaredatasetsprovidecriticalphysiologicalandclinical
visible-spectrumvideorecordingsof35individualswatching datafordevelopingmodelsindiseasediagnosis,monitoring,
emotionallyevocativefilms,withannotationsdistinguishing
and behavioral analysis. The CHFDB dataset [78] includes
stressfulfromnon-stressfulresponses.
long-duration ECG recordings (around 20 hours) from
15patientswithseverecongestiveheartfailureandiswidely
5) MULTIMODALDATASETS used in cardiac research and arrhythmia detection. The
Multimodaldatasetsproviderich,synchronizeddatastreams MIT-BIH dataset [79] offers 48 half-hour ECG segments
frommultiplesourcessuchasaudio,video,andphysiological capturing various arrhythmias and normal rhythms, serving
signals, enabling comprehensive behavioral analysis. The asafoundationaldatasetincardiologyandmachinelearning
NNIME dataset[67] includes synchronized audio, video, studies. Similarly, the PTB Diagnostic ECG dataset [84]
and ECG recordings from 44 professionally trained actors provides549ECGrecordingsfrom290individuals,including
participatingin102dyadicinteractionsessions.Thedataset thosewithmyocardialinfarctionandheartfailure.Forsleep
spansapproximately11hoursofannotatedrecordingsacross disorderanalysis,theApnea-ECGdataset[85]includesanno-
six emotional categories, supporting research in emotion tated ECG recordings from 70 individuals, distinguishing
recognition and multimodal interaction. The TILES-2018 between apneic and non-apneic patterns. The CHB-MIT
dataset[68]offerslarge-scalereal-worlddatafrom212hos- Scalp EEG dataset [80] comprises EEG recordings from
pital staff in California, capturing continuous ECG, respi- 22 pediatric epilepsy patients, including seizure and non-
ration, physical activity, speech-derived features, and other seizure events, and is commonly used in seizure detection
128388 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
research. For fetal health monitoring, the Abdominal and performanceindicatorsandappraisals,aidinginunderstand-
Direct Fetal ECG dataset [81] captures ECG signals from ingengagementandproductivitytrends.Additionally,theHR
pregnant women via abdominal and fetal electrodes. The Employee Attrition and Performance dataset [97] captures
BCI IV 2a dataset [83] provides EEG recordings from informationonemployeedemographics,satisfaction,educa-
nine subjects performing motor imagery tasks, useful in tion,andwork-lifebalancetosupportretentionanalysisand
brain-computer interface studies. The MIMIC-IV dataset identifypredictorsofattritionwithinorganizations.
| [82] is | a large-scale  | clinical |           | database  | with | detailed     | ICU |                                          |     |     |     |     |     |     |
| ------- | -------------- | -------- | --------- | --------- | ---- | ------------ | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| records | of over 40,000 |          | patients, | including |      | vital signs, | lab |                                          |     |     |     |     |     |     |
|         |                |          |           |           |      |              |     | 10) MARKETINGANDCONSUMERBEHAVIORDATASETS |     |     |     |     |     |     |
results,diagnoses,andtreatments.Lastly,theElectronicNose
|     |     |     |     |     |     |     |     | Datasets | in marketing | and | consumer | behavior | offer | valu- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | -------- | -------- | ----- | ----- |
DatasetforCOPD[86]containsbreathsamplesfromsmokers able insights into purchasing patterns, financial sentiment,
| and healthy | individuals,       |     | collected |     | via sensors    |     | detecting |              |               |         |            |            |         |          |
| ----------- | ------------------ | --- | --------- | --- | -------------- | --- | --------- | ------------ | ------------- | ------- | ---------- | ---------- | ------- | -------- |
|             |                    |     |           |     |                |     |           | and customer | engagement.   |         | The Online | Retail     | dataset | [98]     |
| volatile    | organic compounds, |     | aimed     | at  | distinguishing |     | COPD      |              |               |         |            |            |         |          |
|             |                    |     |           |     |                |     |           | contains     | transactional | records | from       | a UK-based |         | retailer |
casesfromhealthycontrols.
|     |     |     |     |     |     |     |     | from 2010   | to 2011, | including | invoice  | details,  | stock        | codes, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --------- | -------- | --------- | ------------ | ------ |
|     |     |     |     |     |     |     |     | and country | data,    | widely    | used for | consumer  | segmentation |        |
|     |     |     |     |     |     |     |     | and market  | basket   | analysis. | The      | Instacart | Market       | Basket |
8) EDUCATIONANDLEARNINGDATASETS
Education-focused datasets offer multimodal insights into dataset [99] features over 3 million anonymized grocery
student behavior, engagement, and academic performance. orders from more than 200,000 users, providing detailed
informationonshoppinghabits,orderfrequency,andproduct
| The StudentLife | dataset |     | [87] captures |     | passive | sensing | data |     |     |     |     |     |     |     |
| --------------- | ------- | --- | ------------- | --- | ------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
from mobile phones over 10 weeks from 48 Dartmouth categories. The Bank Marketing dataset [100] includes
|          |          |        |         |           |     |              |     | responses | from 41,188 | clients | contacted | in  | a telemarketing |     |
| -------- | -------- | ------ | ------- | --------- | --- | ------------ | --- | --------- | ----------- | ------- | --------- | --- | --------------- | --- |
| students | to study | mental | health, | behavior, |     | and academic |     |           |             |         |           |     |                 |     |
outcomes. The ATL-BP dataset [88] includes 2,749 labeled campaigntopromotetermdeposits,alongwithdemographic
video samples of 54 students interacting with an online and interaction data, making it ideal for targeted campaign
tutor, providing facial and gesture data for engagement and modeling.TheUKConsumerTrendsdataset[101]provides
affective analysis. The Automated Online Exam Proctoring long-term expenditure statistics from 1997 to 2022 across
diversesectorssuchasfood,health,housing,andeducation,
| dataset | [89] contains | multimedia |     | inputs | such | as  | webcam |     |     |     |     |     |     |     |
| ------- | ------------- | ---------- | --- | ------ | ---- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
and microphone recordings to detect cheating behaviors supporting economic behavior analysis. Lastly, the Con-
in real-time, using gaze tracking, user verification, and sumerComplaintdataset[102]containsrecordsoffinancial
phone usage detection. The Student Performance dataset grievances related to loans, credit, and money transfers,
[90] was collected from 326 university students in Oman which are frequently used to train models for complaint
classificationandregulatoryinsight.
| and includes | 40 features |     | across | academic | records, |     | Moodle |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | ------ | -------- | -------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
activity logs, and video interactions. The xAPI-Educational Table4providesacomprehensiveoverviewofbenchmark
Mining dataset [91] follows the Experience API (xAPI) datasetsforHBAcategorizedbydomain.
| format | and logs | detailed | student | interactions |     | in  | a virtual |     |     |     |     |     |     |     |
| ------ | -------- | -------- | ------- | ------------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
learningenvironment,supportingbehavioralpatternanalysis.
|     |     |     |     |     |     |     |     | V. APPLICATIONDOMAINSOFHBA |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- |
Lastly, the SCB-dataset [92] provides 4,003 classroom Inthissection,wewillexplorevariousapplicationsofHBA
images and over 11,000 labeled instances, specifically tar- usingmodernAI-basedmethods(seeFigure4).
getinghand-raisingbehaviorforautomaticstudentbehavior
detectioninreal-worldclassroomsettings.
|     |     |     |     |     |     |     |     | A. HEALTHCAREANDMENTALHEALTH |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
Severalstudieshaveusedlogisticregression(LR)forhealth-
|     |     |     |     |     |     |     |     | care predictions, | including |     | ICU admissions |     | and in-hospital |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --------- | --- | -------------- | --- | --------------- | --- |
9) WORKPLACEPRODUCTIVITYANDEMPLOYEE
WELL-BEINGDATASETS mortalityforecasting[103],aswellasearlywarningsystems
Datasets related to workplace productivity and well-being for health crises when combined with GBM [104]. SVM,
enable the analysis of physiological stress, mental health, ANN, RF, and KNN were applied in the diagnosis of
and organizational performance. The WESAD dataset [93] chronic kidney disease [105], survival assessment models
collectsphysiologicalsignalssuchasheartrate,respiration, for heart failure [106], and predicting clinical outcomes
andtemperatureusingbothwrist-andchest-mountedsensors, for various health conditions, showing an accuracy of 85%
capturing stress and relaxation states including meditation. with RF, SVM, and LR [107], both showing high accuracy.
Similarly, the S-Test dataset [94] includes heart rate, EDA, LSTM models were utilized for real-time health and fitness
skin temperature, and contextual factors like activity and monitoring, effectively recognizing activities and health
| ambientconditionstoassesswearable-basedstressdetection. |     |     |     |     |     |     |     | zones[108]. |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
The DS-3 dataset [95] replicates the Trier Social Stress In neurological diseases, ensemble learning techniques,
Test (TSST) digitally, providing real-time physiological such as combining MFA, MMD, and MRD, were used
recordingsthatillustrateindividuals’stressresponsesduring to improve Alzheimer’s disease classification [109], while
and after stressful tasks. For HR analytics, the Employee’s VAER paired with K-Means clustering was employed for
Performancedataset[96]includesorganizationaldatasuchas real-time detection of Parkinson’s disease [110]. IoT-based
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 128389 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE4. BenchmarkdatasetsforHBAapplications.
128390 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
| FIGURE4. | Humanbehavioranalysisapplications. |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and IoT-edge fusion approaches using hybrid classifiers, Density-based clustering was used for anomaly detection in
integrating IoT-edge data and LR, achieved near-perfect elderlycare,improvingbehavioralmonitoringsystems[120].
accuracyinremotehealthmonitoring[111].Similarly,HMM Table 5 encapsulates the predominant research endeavors
wereappliedtodetectanomalousbehaviorinremotepatient within the realm of HBA-based healthcare, providing a
monitoring systems [112], and FPGA-based biosensors succinctoverviewofeachinvestigation,theresultantperfor-
were developed for early virus detection [113]. Cognitive mancemetrics,andtheidentifiedconstraintsassociatedwith
| impairment | detection  | in   | healthcare | settings | has     | also been | eachstudy. |     |     |     |     |     |
| ---------- | ---------- | ---- | ---------- | -------- | ------- | --------- | ---------- | --- | --- | --- | --- | --- |
| explored   | using SVM, | KNN, | NN,        | NB,      | and DT, | with DT   |            |     |     |     |     |     |
achieving100%accuracy,thoughthevalidationwaslimited 1) DISCUSSIONANDCRITICALINSIGHTS
toasmallertestsizeandcontrolledenvironment[114].
|     |     |     |     |     |     |     | The application |     | of HBA | in healthcare |     | and mental health |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ------------- | --- | ----------------- |
Formentalhealth,XGBoostandDNNidentifiedbiomark-
|             |             |           |        |           |            |            | demonstrates     |          | significant | promise,   | particularly     | through the     |
| ----------- | ----------- | --------- | ------ | --------- | ---------- | ---------- | ---------------- | -------- | ----------- | ---------- | ---------------- | --------------- |
| ers related | to mental   | disorders |        | connected | with       | air pollu- |                  |          |             |            |                  |                 |
|             |             |           |        |           |            |            | use of deep      | learning |             | and hybrid | machine          | learning models |
| tion [115]. | Voice-based |           | models | using     | DT, CHAID, | and        |                  |          |             |            |                  |                 |
|             |             |           |        |           |            |            | for diagnostics, |          | monitoring, | and        | early detection. | LSTM and        |
CRT were used for depression screening [116]. Addition- ensemble methods have proven effective in recognizing
| ally, multi-class |     | LR was | applied | to identify |     | predictors |     |     |     |     |     |     |
| ----------------- | --- | ------ | ------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
physicalactivitiesandpredictingdiseaseprogression,while
| of depression | and      | anxiety      | during     | the             | COVID-19 | pan-       |           |         |             |           |         |                     |
| ------------- | -------- | ------------ | ---------- | --------------- | -------- | ---------- | --------- | ------- | ----------- | --------- | ------- | ------------------- |
|               |          |              |            |                 |          |            | IoT-based | systems | enable      | real-time |         | remote monitoring.  |
| demic [117].  | In       | other health | monitoring |                 | systems, | system     |           |         |             |           |         |                     |
|               |          |              |            |                 |          |            | However,  | several | limitations |           | persist | across the reviewed |
| dynamics      | modeling | was          | used       | for respiratory |          | monitoring |           |         |             |           |         |                     |
studies.
via smartphones [118], and telemonitoring systems were A key concern is the limited generalizability of many
employedtomanageglucoselevelsindiabetespatients[119].
|     |     |     |     |     |     |     | models | due to | small, | homogeneous | datasets | or controlled |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ------ | ----------- | -------- | ------------- |
VOLUME13,2025 128391

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE5. Summaryofresearchworksonhealthcareandmentalhealth.
testing environments. For instance, while some classifiers explainable, and adaptive systems that can operate reliably
achieved near-perfect accuracy, their performance may not inbothhospitalandhome-caresettings.
| hold in    | diverse, | real-world |      | settings. The | inconsistency | in     |     |     |     |     |     |     |
| ---------- | -------- | ---------- | ---- | ------------- | ------------- | ------ | --- | --- | --- | --- | --- | --- |
| evaluation | metrics  | and        | lack | of external   | validation    | across |     |     |     |     |     |     |
B. MARKETINGANDCONSUMERBEHAVIOR
| studies further |     | complicates | direct | comparisons. |     | In addition, |            |        |            |      |      |            |
| --------------- | --- | ----------- | ------ | ------------ | --- | ------------ | ---------- | ------ | ---------- | ---- | ---- | ---------- |
|                 |     |             |        |              |     |              | Various ML | and DL | techniques | have | been | applied to |
thereisanotableabsenceoflongitudinalanalysesthatcould predict consumer behavior and optimize marketing strate-
| capture behavioral |     | changes | over | time, which | is  | critical for |                   |          |      |         |     |                |
| ------------------ | --- | ------- | ---- | ----------- | --- | ------------ | ----------------- | -------- | ---- | ------- | --- | -------------- |
|                    |     |         |      |             |     |              | gies by analyzing | multiple | data | sources |     | such as social |
chronicandmentalhealthconditions. media sentiment, reviews, and behavioral patterns. Several
From a practical standpoint, real-world deployment studies employed RF models to predict consumer behavior
| remains | a challenge. |     | Privacy | risks, data | security | in IoT |          |                |                 |     |     |               |
| ------- | ------------ | --- | ------- | ----------- | -------- | ------ | -------- | -------------- | --------------- | --- | --- | ------------- |
|         |              |     |         |             |          |        | based on | environmental, | organizational, |     | and | interpersonal |
systems,andtheinterpretabilityofcomplexmodelsareoften factors [121], and Sentiment Analysis combined with ML
| under-addressed. |         | Particularly |     | in mental health  | applications, |             |                 |             |                |             |     |                |
| ---------------- | ------- | ------------ | --- | ----------------- | ------------- | ----------- | --------------- | ----------- | -------------- | ----------- | --- | -------------- |
|                  |         |              |     |                   |               |             | classifiers     | was used to | predict        | preferences |     | for secondhand |
| models           | tend to | focus        | on  | detection without |               | integrating |                 |             |                |             |     |                |
|                  |         |              |     |                   |               |             | luxury products | [122].      | In e-commerce, |             | ML  | models were    |
feedback mechanisms or considering socio-environmental applied to analyze customer behavior, clustering customers
variables.
|     |     |     |     |     |     |     | and predicting | purchase | trends | for personalized |     | marketing |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | ------ | ---------------- | --- | --------- |
Future research should focus on developing standardized strategies[123],whileDLframeworkscombiningCNNand
| benchmarks, | improving |     | model | transparency, | and | validating |               |      |         |         |          |          |
| ----------- | --------- | --- | ----- | ------------- | --- | ---------- | ------------- | ---- | ------- | ------- | -------- | -------- |
|             |           |     |       |               |     |            | LSTM networks | were | used to | predict | consumer | purchase |
algorithmsinreal-worldclinicalenvironments.Ethicalcon-
intentions[124].
siderations, including bias mitigation and patient consent Studies focusing on repurchase behavior and customer
| in behavioral | monitoring, |     | must | be embedded | into | system |           |             |         |           |     |           |
| ------------- | ----------- | --- | ---- | ----------- | ---- | ------ | --------- | ----------- | ------- | --------- | --- | --------- |
|               |             |     |      |             |      |        | retention | used hybrid | models, | combining | CNN | with sen- |
design. There is also a growing need for multimodal, timent analysis [125], and models based on the Recency,
| 128392 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE6. Summaryofresearchworkonmarketingandconsumerbehavior.
Frequency, and Monetary (RFM) framework, combined consumer choice prediction used spatial attention-enhanced
with various ML techniques such as Multilayer Perceptrons deeptransferlearningand2DCNNfore-commerceproducts,
and SVM [126]. Additionally, Naïve Bayes and Decision achieving an accuracy of 95.60%, though limited by small
Treesmodelswereemployedforpredictingcustomerreturn datasetsizeandnicheapplication[137].
visits based on sentiment analysis from feedback [127] and Table 6 provides a comprehensive summary of recent
for customer churn prediction in the telecommunications researchinmarketingandconsumerbehavior.
industry[128].
Foranalyzingconsumerreviews,MLmodelssuchasNaïve
Bayes were applied to classify hospitality reviews [129], 1) DISCUSSIONANDCRITICALINSIGHTS
while ensemble learning techniques were used to predict TheapplicationofHBAinmarketingandconsumerbehavior
the helpfulness of online reviews [130]. Sentiment analysis hasevolvedsignificantlythroughtheintegrationofmachine
combined with data mining techniques was also applied to learning, deep learning, and sentiment analysis techniques.
detectincentivizedreviews[131].Otherstudiesexploredthe Many studies have shown promising results in predicting
impact of Price Elasticity Impact Learning (PEIL) models purchase intent, customer retention, and review helpful-
to optimize product promotions [132] and used regression ness by leveraging textual, behavioral, and biometric data.
analysistoinvestigatetheinfluenceofonlinesearchvolumes Random Forests and CNN-LSTM hybrids are particularly
onmovieticketsales[133]. popularduetotheirrobustnessinhandlinghigh-dimensional
Emotional factors have also been explored, with studies and sequential data, while Naïve Bayes and decision trees
using DL models to assess how emotional robots influence continuetoservewellinlightweightclassificationtasks.
consumer reactions [134] and group recommender systems However,acommonlimitationacrossstudiesisthenarrow
to improve decision-making for hedonic products [135]. focusofdatasets—eithertiedtospecificindustries(e.g.,phar-
Studiesexaminingsustainableconsumerbehavioridentified maceuticals, airlines) or regions (e.g., Indonesia)—which
greeninitiatives,AIintegration,andmemorableexperiences restricts the generalizability of the findings. Additionally,
as key factors influencing shopping choices using text while accuracy metrics are often high, there is limited
mining and ML classifiers [136]. Additionally, EEG-based discussionontheinterpretabilityofthesemodels,especially
VOLUME13,2025 128393

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
when used in customer-facing applications. The absence Thesealgorithmsofferaconsistentandunbiasedapproachto
of standardized behavioral features and inconsistent use of essayevaluation,withsystemssuchasEASEandtopic-aware
evaluationmetricsalsohinderscross-studycomparison. BERT providing high accuracy and reliability [160], [161],
Another gap lies in the underutilization of multimodal [162],[163].Additionally,activelearningmethodshavebeen
data fusion. Although some studies explore EEG signals exploredtoimprovetheperformanceofAESsystems[164].
or image data, these are typically isolated cases and not Pronunciation Training Tools (PTTs), powered by Auto-
yet standard practice. The emotional and psychological matic Speech Recognition (ASR), have been employed in
dimensions of consumer decision-making—while crucial— languagelearningtoimprovephoneticaccuracy.Modelssuch
remain only partially addressed, often through sentiment asGMM-HMM,CRDNN,andwav2vec2havedemonstrated
labelsratherthandeepercognitiveorbehavioralmodeling. success in enhancing pronunciation skills for non-native
Future research should explore the integration of richer speakers[165],[166],[167].
data types (e.g., gaze tracking, voice tone, physiological Table 7 summarizes research work on the education and
signals) for a more holistic understanding of consumer learningfield.
behavior. There is also a need for developing interpretable
andprivacy-preservingmodelsthatmaintainfairnessacross
demographics.Researchshouldadditionallyaimatreal-time 1) DISCUSSIONANDCRITICALINSIGHTS
systemsforadaptivemarketingandcustomerfeedbackloops, TheapplicationofHBAineducationhasseenrapidadvance-
aswellasbenchmarkingprotocolsthatallowreplicableand ment through AI-driven methods that enhance personaliza-
comparativeevaluationacrossstudies. tion, engagement, assessment, and early intervention. ITS
andEWShavedemonstratedmeasurableimpactsonlearning
outcomesandstudentretention,whileclassroomengagement
C. EDUCATIONANDLEARNING monitoring and automated assessment tools have addressed
In the field of education, various ML and DL techniques longstandingchallengesinscalabilityandfeedbackdelivery.
haveenhancedbothteachingandlearningexperiences[138]. These systems commonly employ CNNs, RF, SVM, and
Intelligent Tutoring Systems (ITS), which leverage NLP, more recently, advanced models like BERT and GANs,
ReinforcementLearning(RL),andadaptivelearningmodels, reflectingatrendtowarddeepcontextualunderstandingand
have been effective in subjects such as mathematics, pro- automation.
gramming, and chemistry, providing personalized learning Despitetheseadvancements,severallimitationsareevident
experiences and real-time feedback to improve student across the reviewed studies. Many models are tested in
performance [140], [141], [142], [143], [144], [145]. These controlled or small-scale environments, raising concerns
systems have been shown to improve learning outcomes about their real-world generalizability, particularly across
acrossdifferentdomains. diverseeducationalcontextsorculturalsettings.Thereisalso
Early Warning Systems (EWS) [139], [146] for dropout a notable imbalance between cognitive and non-cognitive
prediction use models such as RF, LR, SVM, and DL to behavior analysis; while performance prediction is well-
analyzestudentperformanceandengagementdatatoidentify studied,emotionalandsocialdimensionsoflearningbehav-
students at risk of dropping out [147], [148], [149], [150], ior remain underexplored. Furthermore, interpretability is
[151]. These systems help institutions intervene early and often sacrificed for performance—especially with deep
improvestudentretentionrates. modelslikeBERT—hinderingeducatortrustandadoptionin
Classroom Engagement Monitoring (CEM) [152] is practice.
anotherapplicationwhereAI-drivenmodels,includingSVM, Another critical gap is the lack of long-term, longi-
DT, KNN, and CNN, have been used to monitor student tudinal studies that assess the impact of these systems
participation in real-time, particularly in remote learning over time. For example, while dropout prediction models
environments. These systems assess emotional, behavioral, report high accuracy, few explore the effectiveness of
and cognitive engagement, offering insights into student subsequentinterventions.Similarly,automatedessayscoring
performance and helping educators create more effective and pronunciation tools offer impressive metrics but rarely
learningenvironments[153],[154],[155],[156]. accountforstudentlearningcurvesorpedagogicalfeedback
Automated Attendance Systems (AAS) have improved integration.
the accuracy and efficiency of attendance tracking through Future research should prioritize interpretable AI models
facial recognition and CNN models such as AlexNet, thatoffertransparentfeedbacktobotheducatorsandlearners.
GoogleNet,andSqueezeNet[157],[158],[159].Thesesys- Thereisalsoaneedforsystemsthatintegratemultimodaldata
temsstreamlineattendancemanagementbyusingbiometric (e.g., visual, auditory, behavioral) to capture richer insights
data, reducing manual errors and saving time in large into student engagement. Longitudinal evaluation frame-
classrooms. works, privacy-aware architectures, and culturally inclusive
AutomatedEssayScoring(AES)hastransformedthegrad- datasets will be essential to scale AI-based education
ingprocessthroughmodelssuchasBERT,RecurrentNeural systems responsibly and equitably across diverse learning
Networks (RNN), and Generative Adversarial Networks. environments.
128394 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE7. Summaryofresearchworkoneducationandlearning.
|     |     |     |     | Employee | attrition prediction | has been another | key area |
| --- | --- | --- | --- | -------- | -------------------- | ---------------- | -------- |
D. WORKPLACEPRODUCTIVITYANDEMPLOYEE
WELL-BEING of research, where models such as RF, AdaBoost, and
In the area of workplace productivity and employee well- XGBoostwereusedtoanalyzeHRdataandpredictemployee
being, ML techniques have been widely applied to assess turnover [172], [173]. Other studies applied KNN, LR,
mental health, predict employee attrition, and optimize and MLP to predict churn and identify factors influencing
workplaceenvironments.Variousstudiesfocusedonmental employees’decisionstoleave[174],[175].
health analysis, using models such as DT and ANN Severalstudiesexploredthephysicalandemotionalwork
to predict mental health issues based on factors such environment, using DT to correlate environmental factors
|                     |               |                |        | such as lighting | and temperature | with employee | productiv- |
| ------------------- | ------------- | -------------- | ------ | ---------------- | --------------- | ------------- | ---------- |
| as stress, anxiety, | and work-life | balance [168], | [169], |                  |                 |               |            |
[170]. DL methods combined with fuzzy clustering have ity [176]. Mood recognition systems integrating KNN, DT,
also been employed to monitor daily stress and mood and wearable sensors were also used to monitor employee
patterns[171]. well-being and productivity in real-time [177]. CatBoost
| VOLUME13,2025 |     |     |     |     |     |     | 128395 |
| ------------- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE8. Summaryofresearchworkonworkplaceproductivityandemployeewell-being.
and Principal Component Analysis (PCA) were combined and association rule mining, offering insights into better
with SHAP analysis to optimize employee satisfaction in hiringpracticestoreduceemployeeturnover[185].
workplacesettings[178]. Table 8 summarizes research work related to workplace
Real-timestressandemotiondetectionsystemshavealso productivity and employee well-being, highlighting their
gained attention, with models such as XGBoost, LR, and contributions, algorithms used, performance metrics, and
| SVMbeingusedinfactoryenvironmentstomonitorworker |     |     |     | limitations. |     |     |     |
| ------------------------------------------------ | --- | --- | --- | ------------ | --- | --- | --- |
stressandprovidereal-timefeedback[179],[180].Sentiment
and emotional analysis have been applied to manage 1) DISCUSSIONANDCRITICALINSIGHTS
workplaceanxietyandimproveperformance,particularlyin
Researchinworkplaceproductivityandemployeewell-being
theITandmanufacturingsectors[181]. hasembracedadiverserangeofmachinelearningtechniques
Inimprovingoverallworkplaceproductivity,studieshave to address mental health, attrition, satisfaction, and per-
employed predictive models to analyze job environments formance optimization. Predictive models such as Random
and employee satisfaction. Transfer learning techniques Forests, AdaBoost, and neural networks have demonstrated
| were used | to predict work | and job factors | that influence |               |                |                   |           |
| --------- | --------------- | --------------- | -------------- | ------------- | -------------- | ----------------- | --------- |
|           |                 |                 |                | high accuracy | in identifying | at-risk employees | and fore- |
employee satisfaction in the service industry [182]. Agent- casting churn, while real-time systems using wearable
based models were applied to simulate the impact of stress sensors and IoT data offer new possibilities for continuous
andproductivity[183],whileonestudyexaminedtheBring
monitoringofstressandmoodintheworkplace.
Your Own Device (BYOD) strategy and its positive effects However, a closer examination reveals several recurring
onemployeeproductivityandsatisfactionthroughenhanced
|     |     |     |     | limitations. | Many studies | are based | on narrow datasets |
| --- | --- | --- | --- | ------------ | ------------ | --------- | ------------------ |
transparencyandworkflowmanagement[184]. restricted to specific sectors (e.g., IT, manufacturing) or
Lastly, applicant prediction models based on employee geographic regions, limiting the generalizability of their
retentionandperformancefactorsweredevelopedusingNB
|        |     |     |     | findings. | Furthermore, | while high classification | accuracy      |
| ------ | --- | --- | --- | --------- | ------------ | ------------------------- | ------------- |
| 128396 |     |     |     |           |              |                           | VOLUME13,2025 |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
is frequently reported, few models have been externally LSTM, Attention LSTM, and Bi-LSTM models demon-
validated or tested in live organizational settings, which strated high prediction accuracy for crime data in urban
raises questions about their practical deployment. There is areas such as Chicago and San Francisco [197]. LR and
also a lack of standardization in feature sets and outcome correlation analysis models were applied to predict crime
definitions,particularlyinstudiesfocusedonemotionalwell- based on historical data [198], [199], and LASSO and
being,whichhamperscross-studycomparison. Geographically Weighted Regression (GWR) models were
Inaddition,whilesomemodelsincorporateenvironmental usedforpredictingpropertycrimes[200].SARIMAmodels
orbehavioraldata,mostareheavilyreliantonsurvey-based have also been applied to forecast crime rates with high
or HR datasets, which can be biased or outdated. Inter- accuracy[201].
pretability remains a challenge in complex models like Crimeriskassessmentresearchemployedmodelssuchas
ensemble learners and deep neural networks, making them binomial LR and semantic segmentation to assess environ-
| less suitable | for | sensitive | domains |     | like mental | health where |                |     |             |       |        |                   |     |
| ------------- | --- | --------- | ------- | --- | ----------- | ------------ | -------------- | --- | ----------- | ----- | ------ | ----------------- | --- |
|               |     |           |         |     |             |              | mental factors |     | influencing | crime | [202]. | In cryptocurrency |     |
actionableinsightsarecrucial.Veryfewstudiesaccountfor crime detection, correspondence analysis and correlation
longitudinal dynamics or explore how behavioral patterns models provided insights into crime risk factors [203].
evolve over time, and almost none integrate ethical frame- Thresholded ridge estimation models were used to detect
workstoaddressprivacyconcernsinworkplacesurveillance. crime hotspots in cities such as Chicago [204], and sea-
| Future | research | should | aim | for | more holistic | modeling |             |       |      |          |               |             |     |
| ------ | -------- | ------ | --- | --- | ------------- | -------- | ----------- | ----- | ---- | -------- | ------------- | ----------- | --- |
|        |          |        |     |     |               |          | sonal crime | rates | were | analyzed | using Poisson | state-space |     |
by combining behavioral, physiological, and environmental models[205].Studiesinvestigatingcrimevariablesandtheir
data using multimodal and explainable AI frameworks. relationshipsusedPearsoncorrelationstoanalyzedata[206].
| Longitudinal | studies |     | that assess |     | the sustained | impact of |             |     |           |               |        |        |      |
| ------------ | ------- | --- | ----------- | --- | ------------- | --------- | ----------- | --- | --------- | ------------- | ------ | ------ | ---- |
|              |         |     |             |     |               |           | In criminal |     | detection | and tracking, | Faster | R-CNN, | CNN, |
interventions or predictive systems are urgently needed. and RNN models have been applied to recognize indi-
| Moreover, | building | adaptable |     | systems | that | can generalize |         |           |          |     |                 |     |           |
| --------- | -------- | --------- | --- | ------- | ---- | -------------- | ------- | --------- | -------- | --- | --------------- | --- | --------- |
|           |          |           |     |         |      |                | viduals | in public | datasets | and | track criminals |     | with high |
acrossdifferentindustrieswhilepreservinguserprivacywill accuracy[207],[208],[209].Heuristicalgorithmswereused
beessentialforreal-worldadoptionandethicalintegrationof toenhancecrimepredictionandsolvecomplexproblemsin
AIinworkplacemanagement.
largedatasets[210].Inaddition,SVM,RF,andNaiveBayes
|     |     |     |     |     |     |     | (NB) models |        | were applied | to  | detect malicious |       | activities |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------------ | --- | ---------------- | ----- | ---------- |
|     |     |     |     |     |     |     | on social   | media, | showcasing   |     | the power        | of ML | for crime  |
E. CRIMINALJUSTICEANDPUBLICSAFETY
detectionacrossdifferentplatforms[211].
Incriminaljusticeandpublicsafety,awiderangeofMLand Forpatroloptimization,techniquessuchasGeneticAlgo-
DLtechniqueshavebeenappliedtoimprovetrafficviolation
|     |     |     |     |     |     |     | rithm (GA) | and | Cuckoo | Search | (CS) were | used to | optimize |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------ | ------ | --------- | ------- | -------- |
detection, crime prediction, vehicle tracking, and criminal policepatrolroutesandimproveresponsetimes[212],[213].
recognition.
|             |           |     |            |         |     |             | Studies  | using  | the Rabbit | Walk | Algorithm | demonstrated |        |
| ----------- | --------- | --- | ---------- | ------- | --- | ----------- | -------- | ------ | ---------- | ---- | --------- | ------------ | ------ |
| For traffic | violation |     | detection, | various | DL  | models have |          |        |            |      |           |              |        |
|             |           |     |            |         |     |             | improved | patrol | coverage   | and  | safety in | smart cities | [214]. |
been used, such as Faster R-CNN and ShuffleNet v2 for Additionally, collaboration between UAVs and patrol cars
red-lightviolationdetection[186],andYOLOv4,YOLOv5,
wasshowntoenhanceemergencyresponseefficiency[215].
| and YOLOv8 |     | for detecting |     | helmet | violations | and other |             |     |             |     |            |          |          |
| ---------- | --- | ------------- | --- | ------ | ---------- | --------- | ----------- | --- | ----------- | --- | ---------- | -------- | -------- |
|            |     |               |     |        |            |           | Multi-agent | RL  | was applied |     | to further | optimize | response |
trafficinfractions[187],[188],[189].Additionally,automatic
timesandimprovepatrolstrategies[213].
| detection | systems | using | radar | and | video-based | methods |     |     |     |     |     |     |     |
| --------- | ------- | ----- | ----- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Table9presentsadetaileddescriptionofcurrentresearch
have reduced accidents and fatalities [190]. Mask R-CNN, inCriminalJusticeandPublicSafety.
| DenseNet-121, |     | and ResNet-101 |     | were | employed | to detect |     |     |     |     |     |     |     |
| ------------- | --- | -------------- | --- | ---- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
helmetsandnumberplateswithhighaccuracy[191].Vehicle
tracking and traffic surveillance models, such as YOLO, 1) DISCUSSIONANDCRITICALINSIGHTS
combined with tracking algorithms such as the Kalman The integration of machine learning and deep learning in
filter and Hungarian algorithm, have demonstrated high criminal justice and public safety has led to considerable
precisioninvehicletracking[192].YOLOv5combinedwith advances in areas such as traffic violation detection, crime
strongSORT has also shown efficiency in detecting traffic prediction,criminaltracking,andpatroloptimization.Mod-
violationsusingdashcamfootage[193]. elslikeYOLOv5,FasterR-CNN,LSTM,andXGBoosthave
In the domain of crime prediction and analysis, a variety consistently demonstrated strong performance across detec-
of models have been employed. LSTM, XGBoost, and tionandforecastingtasks,enablingmoreaccuratemonitoring
ARIMA have been applied in cities such as Chicago and faster response times. Crime prediction, in particular,
and Los Angeles, achieving high accuracy in predicting has benefited from spatio-temporal modeling techniques
crimes [194]. SARIMA, LSTM, and CHD models have (e.g.,Bi-LSTM,SARIMA),whichimprovepredictivepower
been tested to improve prediction accuracy [195]. More by incorporating historical, seasonal, and geographic data
| advancedDLmodelssuchasDeepCrime,Multi-ViewDeep |     |     |     |     |     |     | patterns. |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
Spatial-Temporal Network (MiST), and CrimeForecaster Despite these technical achievements, several challenges
haveshownreducedpredictionerrors[196].Spatio-Temporal andlimitationspersist.Asignificantportionofthereviewed
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 128397 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE9. Summaryofresearchworksoncriminaljusticeandpublicsafety.
studies rely heavily on datasets from specific urban centers models.Ascrimeisasociallycomplexphenomenon,models
(e.g., Chicago, San Francisco), which limits their general- thatoverlookthesedimensionsmayreinforceexistingbiases
izability to other regions or rural areas. Moreover, while orproducemisleadingresults.Similarly,incriminaldetection
many models report high precision or accuracy, few are and surveillance, the ethical considerations around facial
deployedorvalidatedinreal-worldpolicingorpublicsafety recognition, video analytics, and privacy are often under-
contexts, which raises concerns about practical viability, discussed, despite their critical importance in public safety
ethical implications, and public trust. The lack of standard applications.
evaluationbenchmarksacrossstudiesalsocomplicatesmodel Future research should emphasize building transparent
comparison. andinterpretablemodelsthataccountforethicalconstraints,
Another key concern is the limited integration of social, data bias, and explainability—particularly in high-stakes
economic, and demographic variables in most prediction applications like criminal profiling and patrol deployment.
128398 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
FIGURE5. TheHARworkflowfromdatacollectiontoactivityrecognition.Theprocessbeginswithmonitoringhumanactivityusingvariouswearable
andembeddedsensors,suchassmartwatches,smartphones,andIoTdevices.Thesesensorscapturerawdata,includingmotion,position,andaudio
signals,whichthenundergoespreprocessingtofilternoiseandextractrelevantfeatures.Thepreprocesseddataisfedintorecognitionmodelsthat
employvariousapproaches,suchasclassificationandsequencemodeling,toidentifyspecificactivitieslikewalking,typing,ortapping.Theworkflow
incorporatesembeddedsystemsfordataacquisition,communicationprotocols(e.g.,Bluetooth,Wi-Fi)fordatatransmission,andserversforadditional
processingandstorage.
The development of standardized datasets, domain-specific tasks, locomotion, and health-related actions. In several
evaluation metrics, and participatory frameworks involving cases, LSTMs were integrated with other techniques, such
lawenforcementandcivilrightsorganizationswillbeessen- as GANs [244], attention mechanisms [245], or hybrid
tialtoensurefairness,effectiveness,andsocietalacceptance modelssuchasCNN-LSTM[246],tofurtherenhanceactivity
ofAIsystemsinthisfield. recognitionacrossmultipleenvironments.
Generative models such as GANs and autoencoders have
also been explored for HAR. Conditional GANs were
F. HUMANACTIVITYRECOGNITION employed to improve the recognition of activities involving
HAR plays a pivotal role in understanding and analyzing complexmotions,asseenin[247],whileautoencoderswere
humanbehavioracrossvariouscontexts[7],[8],[9].Bylever- appliedinunsupervisedorsemi-supervisedcontextsforfea-
aging sensor data and ML algorithms, HAR enables the tureextractionanddimensionalityreduction,asdemonstrated
detection and interpretation of physical activities. Figure 5 in [248], [249], [250], [251], and [252]. These approaches
depictsHAR’sstructure.Belowarekeycontributionsinthis have helped address challenges related to data scarcity and
field: modelefficiency.
CNN-basedmodelshavebeenwidelyappliedforrecogniz- RNN variants, including structural RNNs and GRU-
ingdailyactivities,gestures,andlocomotionacrossmultiple based networks, have been adopted for group activity
studies. These models have proven effective in handling recognition and other complex tasks. In particular, studies
sensordataforactivityclassification,asseeninworkssuch suchas[253],[254],[255],and[256]focusedonimproving
as [222], [223], [224], [225], [226], [227], [228], [229], HAR performance by leveraging spatio-temporal attention
[230], and [231], where convolutional networks are used or integrating multiple recurrent layers for better modeling
either standalone or in hybrid configurations. Additionally, of sequential data. Additionally, hybrid models combining
CNNs have been combined with attention mechanisms and RNNs with CNNs or attention mechanisms have been
autoencoderstoimproveperformanceinbothlocomotionand explored in works such as [257], [258], and [259], where
gesture recognition tasks [290], as demonstrated in [232], self-supervised learning combined with multi-task learning
[233],[234],and[235].OtherCNNvariantssuchasHS-CNN ledtoanAccof82.9%.
haveshownstrongresults,achievingAccof97.28%,93.75%, Finally, transformers and other innovative architectures
99.02%,and79.02%asreportedin[236]. have emerged in HAR research. Vision Transformers
LSTM networks have been another dominant model for (ViT) were used to improve activity recognition from
HAR, especially in tasks that require capturing long-range radar data [260], while other studies have explored the
temporal dependencies. Studies such as [237], [238], [239], application of transformers in combination with CNNs
[240], [241], [242], and [243] have leveraged LSTMs for and LSTMs to enhance the efficiency and Acc of HAR
detecting a variety of human activities, including daily systems[261],[262].
VOLUME13,2025 128399

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE10. SummaryofresearchworkonHAR.
Recent advancements in gesture and motion recognition Table 10 provides a comprehensive summary of recent
leveragesensor-basedsystemsandMLmodels,suchasIMU researchworkonHAR.
sensors[263],plastic-optical-fibersensors[264],hierarchical
neural networks such as HiMoReNet [265], graph convolu- 1) DISCUSSIONANDCRITICALINSIGHTS
tionalnetworksforskeleton-basedactionrecognition[266], HAR has seen remarkable progress driven by advances in
sEMG signals for continuous gesture recognition [267], deep learning, sensor technologies, and hybrid modeling
[292], and TinyDL models for air handwriting recogni- techniques. CNNs and Long Short-Term Memory (LSTM)
tion[268],toimproveaccuracyandreal-timeperformancein models continue to dominate the field due to their strong
applications such as human-computer interaction, prosthet- performance in extracting spatial and temporal features
ics,andhandwritingrecognition. fromwearableandembeddedsensordata.Moreover,hybrid
128400 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
models—such as CNN-LSTM combinations, attention- makesaferdecisions[273].Inaddition,supervisedlearning
enhanced architectures, and transformer-based systems— algorithms such as RF, SVM, and LR have been applied
have achieved state-of-the-art results across a wide range to classify aggressive and non-aggressive driving behaviors
of HAR tasks, from daily activity detection to gesture based on sensor data [274]. Other studies have focused on
and locomotion recognition. Emerging domains like air detecting unsafe trucker behaviors using DL-based video
handwritingandEEG/EMG-basedrecognitionalsohighlight analysis [275], and a multimodal system combining DL
thefield’sincreasingversatilityandapplicationpotential. and NLP has been employed to eliminate driver distrac-
Despite these achievements, several limitations persist. tions[276].Meanwhile,theRoadSafetyappintegratedDNN
Many studies rely on benchmark datasets that are limited andYOLOmodelstomonitoraccidentrisksandprovidelive
in scope, size, or diversity, which raises concerns about updatestodrivers[277],achievingahighdetectionprecision,
the generalizability of reported results. Real-world deploy- thoughlimitedinobstaclerecognition.
ment scenarios—such as in noisy or dynamically changing In the context of travel behavior analysis, studies have
environments—are rarely simulated, and only a few studies used models such as LightGBM, XGBoost, and SVM to
addresstherobustnessofmodelstosensornoise,placement predict travel mode selection [278], while Bayesian models
variability, or user heterogeneity. Additionally, the use of have been applied to detect pattern changes in individual
complexmodelsliketransformersandGANsoftensacrifices travel behaviors [279]. Other studies focused on university
interpretability, making their outputs difficult to trust in studenttravelbehaviors,employingSVMandRFtoanalyze
high-stakesapplicationssuchashealthcareorsurveillance. active transportation choices, such as walking [280], [281].
Another gap lies in the limited use of multimodal and ClassificationoftravelerchoicesusingNNalsodemonstrated
context-aware inputs. While some models integrate vision, highaccuracyinpredictingbehavioralpatterns[282].
motion, and audio data, few systems effectively fuse data To enhance transportation infrastructure, models such
from multiple sensor types in real time. The lack of stan- as Gradient Boosting (GB), Poisson regression, and NN
dardized performance metrics and inconsistent experimen- have been applied to assess real-time traffic safety and
tal protocols further complicates cross-study comparison. monitorpedestrianbehavior,providinginsightsforcityplan-
Moreover,energyefficiencyandlatency—criticalfactorsfor ning[283],[284].DNNmodelshavealsobeenusedtopredict
mobileandembeddedHARsystems—areseldomevaluated travel behaviors with high accuracy [285], and AdaBoost
oroptimizedinmanystudies. algorithmsclassifieddrivingbehaviorswithexceptionalper-
Future research should focus on building lightweight, formancebasedonOBDdata[286].Intrafficsafety,studies
explainable, and adaptive models suitable for deployment applied Auto-Encoder (AE) models to detect anomalous
on edge devices and in resource-constrained environments. driving behaviors from naturalistic driving data [287], and
Greateremphasisshouldalsobeplacedontransferlearning otherworkusedK-meansclusteringtoidentifyriskydriving
and self-supervised techniques to reduce dependency on patternsfromvehicletrajectorydata[288].
labeled data, as well as privacy-preserving approaches to Table 11 provides a comprehensive summary of recent
handle sensitive behavioral data. Finally, real-world valida- research in transportation and mobility, detailing the con-
tions,cross-culturaltesting,anduser-centeredevaluationsare tributions, algorithms used, performance metrics, and lim-
neededtobridgethegapbetweenacademicperformanceand itations of various studies focused on transportation and
practicalusabilityindiverseHARapplications. mobility.
G. TRANSPORTATIONANDMOBILITY 1) DISCUSSIONANDCRITICALINSIGHTS
In the domain of transportation and mobility, ML and DL The application of ML in transportation and mobility has
techniqueshavebeenwidelyappliedtoenhanceroadsafety, shown promising results across diverse tasks, including
predictdriverbehavior,andoptimizetransportationsystems. driver behavior detection, travel behavior prediction, and
A primary focus has been on using predictive models and trafficsafetyoptimization.Deeplearningarchitecturessuch
sensor data for driver behavior detection, including driver as CNNs, ResNet50, and DNNs have been effectively
drowsiness and distraction. Models such as SVM, RF, and deployed for real-time monitoring of drowsiness, distrac-
CNNhavebeenusedtomonitoreyeandmouthmovements tions, and aggressive driving, while multimodal systems
in real-time to detect drowsiness, as seen in driver fatigue leveragingvision,speech,andsensorinputsfurtherenhance
detection systems [269]. IoT-based frameworks have been context-awarenessindriverassessment.Similarly,supervised
proposedtointegrateMLmodelsfornon-intrusivereal-time models like SVM, RF, and AdaBoost have demonstrated
monitoring of driver behavior [270], [271], while transfer strong performance in classifying travel modes, driving
learningapproachesutilizingVGG-16andLightGBMwere behaviors, and transportation preferences, especially in
employedtotrackdrivereyemovements[272]. structuredenvironments.
Driver behavior prediction models also utilize multitask However,acloserexaminationrevealsseverallimitations
learning approaches and attention mechanisms, such as that hinder real-world applicability. Many studies rely on
in the personalized system RsSafe, which helps drivers datasets collected from constrained environments, such as
VOLUME13,2025 128401

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE11. Summaryofresearchworksontransportationandmobility.
single geographic areas, specific user groups (e.g., univer- focus on classification accuracy, with limited attention paid
sity students or urban commuters), or synthetic settings, tolatency,energyconsumption,andintegrationwithexisting
reducing the generalizability of findings. The variability in infrastructure—factorsthatarevitalfordeploymentinsmart
lighting,weather,andsensorquality—particularlyfordriver vehiclesandcities.
monitoringsystems—remainsacriticalbarrierforreal-time Future research should prioritize robust, multimodal
deployment. Moreover, several models assume consistent frameworksthatcombinesensorfusionwithcontextualdata
camerapositionsoridealsensorcoverage,whichisrarelythe suchasweather,timeofday,androadconditions.Explainable
caseindynamictrafficscenarios. AIapproachesareessentialtoensuretrustandaccountability
In terms of interpretability, closed box models such indecision-making,especiallyinsafety-criticalapplications.
as DNNs and ensemble learners often lack transparency, Additionally, longitudinal studies capturing real-world vari-
making it difficult to extract actionable insights or justify ability and edge-ready models optimized for low-power
decisions in high-risk environments like road safety or devices will be critical to scaling intelligent transportation
insurance assessment. Furthermore, most existing systems systemsinheterogeneousenvironments.
128402 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
TABLE12. Summaryoffinancialdecision-makingresearch.
H. FINANCIALDECISION-MAKING fraudulent activities and manage financial risks in enter-
In financial decision-making, various ML and DL models prises [302], [303], [304], [305]. Fuzzy cluster analysis
have been applied to enhance prediction accuracy and and ontology-based models were also used in credit risk
|     |     |     |     | assessment, | particularly | in microfinance, | offering more |
| --- | --- | --- | --- | ----------- | ------------ | ---------------- | ------------- |
improveriskassessment.Stockmarketpredictionhasbeena
keyfocus,withmodelssuchasLSTMandCNNintegrating nuancedriskevaluationframeworks[306],[307].
investor sentiment and technical indicators to predict stock Incross-sellingpredictionforconsumerloans,DLmodels
pricesandcrudeoilfutures,significantlyimprovingpredic- such as Auto-Encoder (AE) have shown improvements in
tion accuracy [289], [291]. Ensemble learning techniques predictionaccuracy,particularlyinconsumer-focusedfinan-
cialservices[308].StudiesusingSVM,ANN,andsentiment
| combined with | sentiment | analysis have been | applied to |     |     |     |     |
| ------------- | --------- | ------------------ | ---------- | --- | --- | --- | --- |
predict stock price crashes and market movements, demon- analysisdemonstratedbetterperformanceinpredictingstock
stratingimprovedrobustness[293],[294],[295],[296]. markettrends[309].Additionally,hybridmodelscombining
For credit scoring and financial risk assessment, hybrid ARIMA,LSTM,andlinearregressionwereusedtoforecast
models incorporating techniques such as PCA, SVM, and stockmarketprices,utilizingsentimentanalysisfromsocial
media[310].
| DT have been | explored | to enhance prediction | accuracy, |     |     |     |     |
| ------------ | -------- | --------------------- | --------- | --- | --- | --- | --- |
withapplicationsincreditworthinessevaluationandlending Table 12 provides a summary of recent research con-
processes, showing improved risk assessment [297], [298], tributions to financial decision-making, highlighting the
|     |     |     |     | algorithms | used, key | performance metrics, | and any notable |
| --- | --- | --- | --- | ---------- | --------- | -------------------- | --------------- |
[299],[300].BERT,BiGRU,andattentionmechanismswere
| usedtopredictindividualstockprices,combiningsentiment |     |     |     | limitations. |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | ------------ | --- | --- | --- |
dataforhigh-accuracypredictions[301].
Risk management and fraud detection have seen 1) DISCUSSIONANDCRITICALINSIGHTS
improvement through ML models such as SVM, RF,and ML and DL have significantly transformed financial
ARIMA. Also DL models which were applied to detect decision-makingprocesses,particularlyinareassuchasstock
| VOLUME13,2025 |     |     |     |     |     |     | 128403 |
| ------------- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
market forecasting, credit scoring, fraud detection, and risk activity, and geolocation data—protecting individuals’ pri-
assessment.LSTM,CNN,andensemblemodelshaveshown vacy is paramount. The collection, storage, and processing
consistent success in modeling non-linear financial data of such data raise significant ethical dilemmas, including
patterns,especiallywhencombinedwithsentimentanalysis. the necessity of informed consent, anonymization, security,
These models have enhanced the prediction of stock price andthepotentialformisuse[311],[312].Belowarethekey
movements, crash risks, and individual creditworthiness, aspectsoftheseconcerns:
| while hybrid | approaches—such |     |               | as integrating |          | PCA | or opti- |     |     |     |     |     |     |     |     |
| ------------ | --------------- | --- | ------------- | -------------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| mization     | algorithms      |     | like GWO—have |                | improved |     | accuracy |     |     |     |     |     |     |     |     |
1) INFORMEDCONSENTANDANONYMIZATION
androbustness.
Ensuringthatindividualsprovideexplicit,informedconsent
Despite these advances, several limitations persist. Many before their behavioral data is collected and analyzed is
| studies  | are constrained |           | to specific | markets |        | (e.g., Chinese | or    |              |     |          |           |            |     |         |     |
| -------- | --------------- | --------- | ----------- | ------- | ------ | -------------- | ----- | ------------ | --- | -------- | --------- | ---------- | --- | ------- | --- |
|          |                 |           |             |         |        |                |       | fundamental. |     | However, | obtaining | meaningful |     | consent | in  |
| Moroccan | financial       | systems), |             | which   | raises | concerns       | about |              |     |          |           |            |     |         |     |
large-scaleHBAsystems,particularlythosethatoperatepas-
generalizability to other economic contexts. Additionally, sivelyinthebackground—suchassmartsurveillancesystems
| the reliance | on  | historical | financial |     | data or | static | sentiment |             |     |                 |     |     |            |           |     |
| ------------ | --- | ---------- | --------- | --- | ------- | ------ | --------- | ----------- | --- | --------------- | --- | --- | ---------- | --------- | --- |
|              |     |            |           |     |         |        |           | or wearable | IoT | devices—remains |     |     | an ongoing | challenge |     |
indicatorsmeansthatmodelsoftenfailtoadapttovolatileor [313], [314]. Often, users are unaware that their data is
| highly dynamic |     | conditions. | While | some | models |     | show high |                  |     |        |      |          |         |           |     |
| -------------- | --- | ----------- | ----- | ---- | ------ | --- | --------- | ---------------- | --- | ------ | ---- | -------- | ------- | --------- | --- |
|                |     |             |       |      |        |     |           | being collected, |     | making | true | informed | consent | difficult | to  |
accuracyinexperimentalsettings,theirperformanceinreal-
|             |         |     |         |              |     |         |        | achieve. | Even | when anonymization |     |     | techniques | are | applied, |
| ----------- | ------- | --- | ------- | ------------ | --- | ------- | ------ | -------- | ---- | ------------------ | --- | --- | ---------- | --- | -------- |
| world, live | trading | or  | lending | environments |     | remains | under- |          |      |                    |     |     |            |     |          |
theriskofre-identificationpersists[315],[316].Combining
explored.
|     |     |     |     |     |     |     |     | multimodal | data | sources, | such | as  | facial recognition |     | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | -------- | ---- | --- | ------------------ | --- | --- |
Interpretabilityisanotherkeyissue,particularlywithdeep
geolocationtracking,caninadvertentlyrevealidentitieseven
andensemblemodels.Thesemodelsoftenoperateas‘‘closed
ifpersonallyidentifiableinformation(PII)hasbeenremoved.
boxes,’’makingitdifficultforfinancialanalystsorregulators
|     |     |     |     |     |     |     |     | This calls | for stronger |     | data protection |     | measures | and | clearer |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | --------------- | --- | -------- | --- | ------- |
to validate predictions or understand underlying decision communicationbetweendatacollectorsandusersregarding
mechanisms.Thisisparticularlyproblematicindomainssuch
howtheirdatawillbeused.
ascreditscoringandfrauddetection,wheretransparencyand
fairnessarecritical.
2) DATASECURITYANDPROTECTIONAGAINSTBREACHES
| Moreover, | few | studies | incorporate |     | real-time | or  | streaming |     |     |     |     |     |     |     |     |
| --------- | --- | ------- | ----------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
AsHBAsystemshandlelargevolumesofsensitivedata,they
| data, limiting |     | their effectiveness |     | in  | high-frequency |     | trading |        |           |         |     |                 |     |              |     |
| -------------- | --- | ------------------- | --- | --- | -------------- | --- | ------- | ------ | --------- | ------- | --- | --------------- | --- | ------------ | --- |
|                |     |                     |     |     |                |     |         | become | lucrative | targets | for | cybercriminals. |     | Unauthorized |     |
orlivecreditriskmanagement.Ethicalconsiderations—such
asmodelbias,discriminationinlending,anddataprivacy— access to behavioral data can lead to serious consequences,
includingidentitytheft,financialfraud,andintrusivesurveil-
| are rarely | addressed |     | in technical | evaluations, |     | despite | their |              |          |     |           |          |        |             |     |
| ---------- | --------- | --- | ------------ | ------------ | --- | ------- | ----- | ------------ | -------- | --- | --------- | -------- | ------ | ----------- | --- |
|            |           |     |              |              |     |         |       | lance [317]. | Securing |     | this data | requires | robust | encryption, |     |
importanceinfinancialAIsystems.
|             |     |             |               |     |      |              |            | access    | control | mechanisms, |          | and continuous |        | monitoring |     |
| ----------- | --- | ----------- | ------------- | --- | ---- | ------------ | ---------- | --------- | ------- | ----------- | -------- | -------------- | ------ | ---------- | --- |
| To advance  |     | this        | field, future |     | work | should       | prioritize |           |         |             |          |                |        |            |     |
|             |     |             |               |     |      |              |            | to detect | and     | mitigate    | security | threats        | [318]. | However,   |     |
| explainable | AI  | approaches, | real-time     |     | data | integration, | and        |           |         |             |          |                |        |            |     |
robust testing across diverse markets. There is also a achieving this level of security is complex, as behavioral
|     |     |     |     |     |     |     |     | data is often | distributed |     | across | multiple | devices | and | cloud- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | --- | ------ | -------- | ------- | --- | ------ |
needtoestablishstandardizedbenchmarksandcross-market
|            |                 |     |                  |         |            |        |             | based systems. |               | Additionally, |                  | the increasing |     | reliance | on IoT   |
| ---------- | --------------- | --- | ---------------- | ------- | ---------- | ------ | ----------- | -------------- | ------------- | ------------- | ---------------- | -------------- | --- | -------- | -------- |
| datasets   | for comparative |     | evaluation.      |         | Finally,   |        | interdisci- |                |               |               |                  |                |     |          |          |
|            |                 |     |                  |         |            |        |             | devices        | introduces    | further       | vulnerabilities, |                | as  | many     | of these |
| plinary    | collaboration   |     | with economists, |         | regulatory |        | bodies,     |                |               |               |                  |                |     |          |          |
|            |                 |     |                  |         |            |        |             | devices        | lack advanced |               | security         | features.      |     | Without  | proper   |
| and social | scientists      |     | will be          | crucial | to         | ensure | ethical,    |                |               |               |                  |                |     |          |          |
cybersecuritymeasures,HBAsystemsriskexposinguserdata
| equitable, | and | effective | deployment |     | of  | AI in | financial |     |     |     |     |     |     |     |     |
| ---------- | --- | --------- | ---------- | --- | --- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
tomaliciousentities[319].
decision-making.
3) ETHICALUSEANDPOTENTIALFORMISUSE
VI. CHALLENGESANDLIMITATIONSINHBA
WhileHBAhasadvancedsignificantlywiththeintegrationof While HBA has the potential to enhance various domains,
AI,ML,anddatascience,severalchallengesandlimitations including healthcare and security, its use also raises ethical
persist. These challenges are crucial to address to ensure dilemmas.Behavioraldatacanberepurposedforapplications
the effective, ethical, and accurate application of HBA in beyonditsoriginalintent,sometimeswithoutuserawareness
real-world scenarios. This section outlines key challenges or consent. For instance, companies collecting user inter-
related to data privacy, generalization, real-time processing, action data for personalized recommendations could later
andscalability use it for targeted advertising or even behavioral manipu-
|     |     |     |     |     |     |     |     | lation [320]. | Similarly, |     | governments |     | or organizations |     | could |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ----------- | --- | ---------------- | --- | ----- |
A. DATAPRIVACYANDETHICALCONCERNS deploy HBA for mass surveillance [321], raising concerns
One of the most pressing challenges in HBA is ensuring aboutcivillibertiesandpersonalfreedoms.Establishingclear
data privacy and addressing ethical concerns. Since HBA regulatory frameworks and ethical guidelines is essential to
systems analyze personal and sometimes highly sensitive ensure that HBA is used responsibly, without infringing on
information—such as physiological signals, social media individuals’rights.
| 128404 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
4) BIASANDDISCRIMINATIONINHBAMODELS C. REAL-TIMEPROCESSINGANDSCALABILITY
AI models used in HBA are only as good as the data they FormanyHBAapplications,real-timeprocessingisessential
aretrainedon.Ifthetrainingdataisnotdiverse,theresulting to ensure timely responses and decision-making [327].
modelsmayexhibitbias,leadingtodiscriminatoryoutcomes. However, several technical challenges hinder the real-time
Forexample,anemotionrecognitionsystemtrainedondata capabilitiesandscalabilityofHBAsystems:
| from one | cultural | group | may | misinterpret | expressions |     | from |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | --- | ------------ | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
individualsbelongingtodifferentethnicbackgrounds[322]. 1) HIGHCOMPUTATIONALREQUIREMENTS
Similarly,biasinhiringassessmentspoweredbyHBAcould Analyzing behavioral data in real time requires signifi-
leadtounfairtreatmentofcandidatesbasedongender,race,
|     |     |     |     |     |     |     |     | cant computational |     | power, | particularly |     | when | dealing | with |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------ | ------------ | --- | ---- | ------- | ---- |
or socioeconomic status. Addressing these biases requires multimodal inputs such as video, audio, and sensor data.
| the use | of diverse | datasets, |     | fairness-aware | algorithms, |     | and |            |       |         |             |     |         |             |     |
| ------- | ---------- | --------- | --- | -------------- | ----------- | --- | --- | ---------- | ----- | ------- | ----------- | --- | ------- | ----------- | --- |
|         |            |           |     |                |             |     |     | Processing | these | streams | efficiently |     | without | introducing |     |
continuous auditing to identify and mitigate discriminatory delays remains a challenge. Traditional cloud-based archi-
patternsinAImodels. tecturesoftenintroducelatency,makingthemunsuitablefor
time-sensitiveapplicationslikeemergencyresponsesystems
B. GENERALIZATIONANDBIASISSUES orreal-timeemotiondetection[328].
generalization,
| HBA models |     | often struggle |     | with |     | meaning |     |     |     |     |     |     |     |     |     |
| ---------- | --- | -------------- | --- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that they may perform well on specific datasets but fail 2) SCALABILITYACROSSDEVICESANDPLATFORMS
| when applied |     | to different |     | populations, | cultural | settings, |     |            |     |               |     |              |     |        |         |
| ------------ | --- | ------------ | --- | ------------ | -------- | --------- | --- | ---------- | --- | ------------- | --- | ------------ | --- | ------ | ------- |
|              |     |              |     |              |          |           |     | HBA models |     | must function |     | consistently |     | across | various |
or real-world scenarios. Several factors contribute to this devices, ranging from high-performance cloud servers to
limitation:
|     |     |     |     |     |     |     |     | resource-constrained |          | edge | devices  | such        | as smartphones |        | and   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | -------- | ---- | -------- | ----------- | -------------- | ------ | ----- |
|     |     |     |     |     |     |     |     | IoT sensors.         | Ensuring |      | seamless | performance |                | across | these |
1) LIMITEDGENERALIZATIONACROSSDEMOGRAPHICS platforms requires optimized algorithms that can adapt
Humanbehaviorisinfluencedbyavarietyoffactors,includ- to different hardware capabilities. Edge computing and
ing cultural norms, social upbringing, and environmental lightweight deep learning models offer potential solutions,
| conditions. | However, |     | many | HBA models |     | are trained | on  |          |           |            |     |           |       |            |     |
| ----------- | -------- | --- | ---- | ---------- | --- | ----------- | --- | -------- | --------- | ---------- | --- | --------- | ----- | ---------- | --- |
|             |          |     |      |            |     |             |     | enabling | real-time | processing |     | on-device | while | minimizing |     |
datasets that reflect only a subset of the global population. relianceoncloudinfrastructure[329],[330].
| For instance, | a   | facial | expression | analysis | model | developed |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---------- | -------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
usingWesterndatasetsmaynotaccuratelyinterpretemotions 3) MANAGINGBANDWIDTHANDSTORAGECONSTRAINTS
| expressed | by                | individuals | from | Asian      | or African | cultures. |     |            |              |            |                 |               |         |         |         |
| --------- | ----------------- | ----------- | ---- | ---------- | ---------- | --------- | --- | ---------- | ------------ | ---------- | --------------- | ------------- | ------- | ------- | ------- |
|           |                   |             |      |            |            |           |     | Continuous | data         | collection |                 | from multiple |         | sources | gen-    |
| This lack | of generalization |             |      | results in | reduced    | accuracy  | and |            |              |            |                 |               |         |         |         |
|           |                   |             |      |            |            |           |     | erates     | vast amounts |            | of information, |               | leading |         | to high |
potential misinterpretations when the model is applied to a storage and bandwidth demands. Real-time streaming
broaderaudience[323],[324].
|     |     |     |     |     |     |     |     | of behavioral |              | data | can quickly    |     | overwhelm    |     | network |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | ---- | -------------- | --- | ------------ | --- | ------- |
|     |     |     |     |     |     |     |     | resources,    | particularly |      | in large-scale |     | deployments. |     | Imple-  |
2) BIASINDATACOLLECTION
|     |     |     |     |     |     |     |     | menting | efficient | data | compression |     | [331], | feature | extrac- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | ---- | ----------- | --- | ------ | ------- | ------- |
Biasesoftenemergeatthedatacollectionstage,particularly tion, and selective data transmission strategies [332]
whencertaingroupsareoverrepresentedorunderrepresented can help mitigate these issues while maintaining system
| in the dataset. |     | If the | majority | of the | training | data | comes |     |     |     |     |     |     |     |     |
| --------------- | --- | ------ | -------- | ------ | -------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
performance.
| from urban | populations, |     | an              | HBA model  | may | struggle      | to  |                           |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --------------- | ---------- | --- | ------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
| analyze    | behaviors    | in  | rural settings. | Similarly, |     | if behavioral |     |                           |     |     |     |     |     |     |     |
|            |              |     |                 |            |     |               |     | 4) LATENCYANDSYSTEMDELAYS |     |     |     |     |     |     |     |
dataiscollectedprimarilyfromyoungadults,themodelmay High-latency systems undermine the effectiveness of
| perform | poorly | when | assessing | elderly | individuals |     | [325]. |     |     |     |     |     |     |     |     |
| ------- | ------ | ---- | --------- | ------- | ----------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
real-timeHBAapplications.Forinstance,ahealthcaremoni-
| Ensuring | balanced, | diverse |     | datasets | that capture | the | full |     |     |     |     |     |     |     |     |
| -------- | --------- | ------- | --- | -------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
toringsystemthatdetectsanomaliesinpatientbehaviormust
| spectrum | of human | behavior |     | is crucial | for | improving | the |         |         |           |            |     |            |            |     |
| -------- | -------- | -------- | --- | ---------- | --- | --------- | --- | ------- | ------- | --------- | ---------- | --- | ---------- | ---------- | --- |
|          |          |          |     |            |     |           |     | provide | instant | alerts to | caregivers | to  | be useful. | Optimizing |     |
generalizabilityofHBAmodels.
|     |     |     |     |     |     |     |     | processing | pipelines, | using     | dedicated |            | AI accelerators, |             | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --------- | --------- | ---------- | ---------------- | ----------- | --- |
|     |     |     |     |     |     |     |     | leveraging | parallel   | computing |           | techniques |                  | are crucial | for |
3) ADAPTINGTONEWCONTEXTSANDENVIRONMENTS
|            |     |       |           |          |     |              |     | minimizing | delays | and | ensuring | real-time |     | responsiveness |     |
| ---------- | --- | ----- | --------- | -------- | --- | ------------ | --- | ---------- | ------ | --- | -------- | --------- | --- | -------------- | --- |
| HBA models |     | often | fail when | deployed | in  | environments |     | [333].     |        |     |          |           |     |                |     |
differentfromthosetheyweretrainedin.Asystemdesigned
to monitor stress levels in office workers may not per- VII. EMERGINGTECHNOLOGIESANDEXPANDING
| form effectively |     | in a | high-intensity | hospital |     | setting, | where |     |     |     |     |     |     |     |     |
| ---------------- | --- | ---- | -------------- | -------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
METHODOLOGICALHORIZONSINHBA
| behavioral | cues | differ. | One | way to address |     | this is through |     |               |     |           |         |     |             |     |          |
| ---------- | ---- | ------- | --- | -------------- | --- | --------------- | --- | ------------- | --- | --------- | ------- | --- | ----------- | --- | -------- |
|            |      |         |     |                |     |                 |     | HBA continues |     | to evolve | rapidly |     | in response |     | to novel |
techniquessuchastransferlearninganddomainadaptation, technologies and data-centric paradigms that are redefin-
| which allow | models | to  | adjust | to new | datasets | with minimal |     |         |          |               |     |           |     |                  |     |
| ----------- | ------ | --- | ------ | ------ | -------- | ------------ | --- | ------- | -------- | ------------- | --- | --------- | --- | ---------------- | --- |
|             |        |     |        |        |          |              |     | ing how | behavior | is perceived, |     | captured, |     | and interpreted. |     |
retraining[326]. This section synthesizes emerging technological trends and
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 128405 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
methodologicaladvancesthatarereshapingthefield,witha C. ADVANCEDSENSINGMODALITIESANDMULTIMODAL
focusonpracticalimplementation,contextualawareness,and INTEGRATION
system-levelintegration. Sensor advancements are enhancing the fidelity and
granularity of behavioral capture. Traditional sensors—
accelerometers, gyroscopes, and RGB cameras—are now
A. EDGECOMPUTINGFORLOW-LATENCY,
complementedbybiosensors(e.g.,skintemperature,electro-
CONTEXT-AWAREINFERENCE
dermalactivity),LiDARfordepth-basedgesturerecognition
Edge computing is becoming indispensable in HBA appli-
[345],andnear-infraredcamerasfordriverfatiguedetection
cations where latency, privacy, and connectivity constraints
inlowlight.Thesemodalitiesareoftenusedincombination
pose significant concerns [335]. By moving computation
tobuildrich,multimodaldatasetsthatcapturenotjustmotion
from cloud servers to local devices—such as smartphones,
butcontextandaffect.
wearables, and embedded IoT nodes—edge systems enable
Recent studies have integrated real-time EEG and ECG
real-time processing of behavioral signals like posture,
analysis with facial micro-expression detection for appli-
speech, and physiological indicators. This architecture sup-
cations in emotion-aware systems and cognitive workload
ports responsive environments, such as ambient-assisted
monitoring [343]. Wearable patches and smart garments
living [336] and driver monitoring systems [10], [337],
are also being deployed to unobtrusively monitor posture
where milliseconds of delay can affect safety or decision
and stress in workplace settings. Importantly, multimodal
relevance.
fusionstrategies—suchasearlyfusionwithsharedencoders,
Notable implementations include emotion recognition
late fusion with ensemble voting, and hybrid attention
engines running on microcontrollers and wearable stress
mechanisms—are proving effective in synchronizing het-
monitoring that infer behavior without cloud dependency.
erogeneous inputs [344]. These approaches enhance system
These systems utilize lightweight models optimized via
robustnessandallowforadaptivefeatureselectiondepending
pruning, quantization, or TinyML frameworks [339] to
onenvironmentalconstraintsortaskdemands.
achieve near real-time performance. For instance, adaptive
offloading strategies [338] have been proposed where data
is selectively transmitted to the cloud only when local con- D. LEVERAGINGLARGELANGUAGEMODELSFOR
fidence thresholds are not met, balancing energy consump- TEXTUALBEHAVIORALINSIGHTS
tion and inference accuracy. The shift toward edge-native Large Language Models (LLMs) such as BERT, GPT,
behavioral analytics is also contributing to stronger data and T5 are transforming textual behavior analysis by
localization and regulatory compliance in privacy-sensitive enabling semantic understanding of user-generated content
domains. across emails, social media, chat logs, and transcriptions
[346], [347]. Unlike rule-based NLP systems, LLMs can
infer user intent, detect sentiment drift, and recognize
B. AI-DRIVENBEHAVIORALMODELINGWITHCOGNITIVE
psychosocial markers of distress or engagement. In mental
DEPTH
health monitoring, for instance, LLMs have been used to
As ML models become increasingly sophisticated, there
detect depressive tendencies from Reddit posts or analyze
is a move toward capturing not just observable actions
therapeuticconversationsforempathyandcoherence.
but also internal cognitive-emotional states and social sig-
More advanced implementations include dialogue agents
nals.Deeplearningarchitecturesnowsupportmulti-layered
that adapt their conversational strategies based on real-time
understanding of human behavior that reflects intention,
feedback and inferred user mood. In financial behavior
affect,andcontext.Forexample,reinforcementlearninghas
prediction, LLMs have been fine-tuned to extract decision
beenleveragedtosimulatebehavioraladaptationintutoring
drivers from investor sentiment or customer complaints,
systems and social robotics, learning optimal feedback
thereby augmenting classical quantitative models [348].
policies through interaction rather than static labels [334],
Fine-tuning and prompt engineering are critical tools for
[340].
customizing LLMs to behavioral tasks while preserving
Transformer-based networks, which have revolutionized
generallinguisticcompetence.Importantly,whencombined
natural language processing, are being adapted for spa-
withothermodalities—suchasvisionorphysiology—LLMs
tiotemporal action recognition and multi-agent behavior
serve as the linguistic layer of multimodal HBA systems,
modeling. These models offer greater contextual memory
bridgingnarrativeandnumericalreasoning.
andsupportforlong-rangedependencies,whichareessential
for detecting subtle shifts in behavior over time [341].
In addition, neural-symbolic approaches are being explored E. ETHICALANDPRIVACY-PRESERVINGTECHNIQUES
to integrate statistical learning with rule-based reasoning, As HBA technologies become increasingly pervasive in
enabling systems to incorporate domain knowledge and healthcare, smart cities, education [349], and workplace
causality into behavioral inference. These directions are monitoring, the need to protect user data while maintain-
enabling behavior models to be not just predictive but ing the integrity and fairness of analytical models has
explanatoryandinteractive[342]. never been greater. Solutions to these concerns go beyond
128406 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
high-level principles, increasingly incorporating concrete Thesesyntheticdatasetspreservestatisticalpropertiesofthe
technicalmethodsandgovernancestrategies.Thissubsection original data while removing personal identifiers. In HBA,
exploresmultipleprivacy-preservingandethicallygrounded this technique is particularly useful for training models on
approachesthatareshapingtheresponsibleevolutionofHBA sensitive behaviors such as addiction relapse or employee
[350]. burnout. By simulating human-like behavior, these datasets
enablesafeexperimentationandbenchmarking.
1) DIFFERENTIALPRIVACY
Differential privacy is a formalized approach to protecting 5) ETHICALAIFRAMEWORKS
individualdatacontributionsbyaddingcontrolledstatistical Frameworks such as the EU’s High-Level Expert Group
noise to outputs or intermediate computations [351]. This on AI Ethics Guidelines [360], IEEE’s Ethically Aligned
techniqueensuresthatthepresenceorabsenceofasingledata Design, and the Montreal Declaration on Responsible AI
pointdoesnotsignificantlyaltertheoutcomeoftheanalysis, provide practical checklists and design principles. These
thus maintaining plausible deniability for individuals. For include guidelines for fairness, explainability, and non-
HBA tasks such as behavioral clustering or emotional state discrimination.InthecontextofHBA,adoptingtheseframe-
prediction on social media data, researchers can apply works translates into deploying bias mitigation strategies
differentially private mechanisms at the data aggregation (e.g.,reweighting,adversarialdebiasing),usinginterpretable
levelorduringmodeltraining[352].Google’sRAPPORand models (e.g., SHAP, LIME), and conducting algorithmic
Apple’s iOS telemetry systems are real-world deployments auditstoverifycompliance[361].
of this technique. Tools such as TensorFlow Privacy and
PyTorch Opacus allow researchers to build differentially 6) CONSENTMANAGEMENTPLATFORMS(CMPS)
privatedeeplearningmodelsthatcanbeappliedindomains ModernHBAsystems,especiallythoseembeddedinmobile
like mental health analytics [353] or educational feedback apps or online services, are integrating CMPs to facilitate
withoutexposingindividualidentities. transparentdatagovernance.Theseplatformsallowusersto
opt in or out of specific data usage scenarios and provide
2) FEDERATEDLEARNING fine-grained control over consent types (e.g., for training
Federated Learning (FL) [354] is a decentralized ML vs. personalization). Coupled with real-time dashboards,
paradigmthatallowsmultipledevicesorsilos(e.g.,hospitals, CMPsempoweruserstomakeinformedchoicesabouttheir
smartphones,smartwatches)tocollaborativelytrainashared behavioraldata[362].
model while keeping raw data locally stored. FL is ideal
for behavior recognition using physiological data collected 7) DATAMINIMIZATIONANDPURPOSELIMITATION
fromwearables,enablingprivacy-preservingapplicationsin HBA platforms are also being designed to implement the
stressdetection,fitnessmonitoring,orearlydiseasewarning principles of data minimization (collecting only the data
[355]. To enhance FL’s robustness, recent advancements necessaryforatask)andpurposelimitation(restrictingdata
such as secure aggregation protocols, differential privacy use to its stated objectives). Techniques such as feature
integration,andhomomorphicencryptionarebeingexplored selection,task-specificembeddings[363],andmodelpruning
to prevent leakage through gradient updates [356]. In HBA [364]areusedtoavoidunnecessarycollectionofbehavioral
systems, FL can also support personalization by adapting signals.Thisreducestheattacksurfaceforprivacybreaches
global models to local behavior patterns via fine-tuning or whileimprovingmodelefficiency.
federatedmeta-learningtechniques[357].
8) ETHICALOVERSIGHTCOMMITTEESANDIMPACT
3) SECUREMULTI-PARTYCOMPUTATION(SMPC) ASSESSMENTS
Secure Multi-party Computation (SMPC) allows multiple Beyond technical tools, organizations deploying HBA at
entities to compute a joint function over their inputs scale are instituting AI ethics boards and Data Protection
withoutrevealingtheinputsthemselves.Thiscryptographic ImpactAssessments(DPIAs)[365].Thesestructuresenable
approach[358]isincreasinglybeinginvestigatedinscenarios systematicevaluationsofbehavioraldatausage,especiallyin
like collaborative behavioral research across hospitals or high-stakesareaslikelawenforcementoreducation.DPIAs
academicinstitutions.Forexample,SMPCenablesmultiple help in identifying and mitigating risks before deployment,
mentalhealthclinicstocontributetoasharedstressprediction ensuring regulatory compliance (e.g., GDPR) and ethical
modelwithoutdisclosingindividualpatientrecords,thereby accountability.
supportingbothprivacyandresearchgoals.
F. CROSS-DISCIPLINARYAPPROACHES
4) SYNTHETICDATAGENERATION The future of HBA is likely to involve an increasing inte-
In cases where real data cannot be shared or is insuf- grationofcross-disciplinaryapproaches,combininginsights
ficient, synthetic data can be generated using methods from various fields to drive innovation. Key areas where
such as Generative Adversarial Networks (GANs) [359]. cross-disciplinaryapproachesaremakinganimpactinclude:
VOLUME13,2025 128407

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
1) PSYCHOLOGYANDAI Importantly,thisintegrationalsohelpsvalidatethebehavioral
|                 |     |                  |     |          |      |           |     | insights | produced | by  | AI  | models against |     | clinical gold |
| --------------- | --- | ---------------- | --- | -------- | ---- | --------- | --- | -------- | -------- | --- | --- | -------------- | --- | ------------- |
| The integration |     | of psychological |     | theories | with | AI models |     |          |          |     |     |                |     |               |
has proven instrumental in constructing more nuanced and standards,therebyincreasingreliabilityandtrustworthiness.
interpretablebehavioralsystems.Conceptssuchascognitive
dissonance,behavioralreinforcement,emotionalregulation, 4) SOCIOLOGYANDSOCIALBEHAVIORANALYSIS
and attention mechanisms inform the architecture and Sociological theory contributes a macro-level lens to HBA
|          |       |         |     |           |                      |     |     | by emphasizing |     | the role | of social | context, | group | behavior, |
| -------- | ----- | ------- | --- | --------- | -------------------- | --- | --- | -------------- | --- | -------- | --------- | -------- | ----- | --------- |
| function | of ML | models. | For | instance, | cognitive-behavioral |     |     |                |     |          |           |          |       |           |
models [366] can be used to shape personalized feedback and systemic structures. Techniques such as social network
mechanismsinintelligenttutoringsystemsormentalhealth analysis (SNA) [372], role theory, and symbolic interac-
applications. Emotion recognition systems often draw from tionism provide models for understanding how individuals
established psychological taxonomies such as Ekman’s behave in relation to others. In online platforms, for
|           |          |     |           |            |     |       |        | example, | sociologically |     | informed | algorithms |     | can detect |
| --------- | -------- | --- | --------- | ---------- | --- | ----- | ------ | -------- | -------------- | --- | -------- | ---------- | --- | ---------- |
| six basic | emotions | or  | Russell’s | circumplex |     | model | [367], |          |                |     |          |            |     |            |
enabling algorithms to ground prediction in empirically emergent phenomena like echo chambers, opinion polariza-
validated frameworks. Psychological profiling also informs tion, or collective mood shifts. In organizational settings,
recommendation systems, where user traits like openness behavior analytics grounded in social role expectations
or impulsivity are used to predict preferences or behavioral and interaction patterns can improve team cohesion, detect
burnout,orforecastattrition.Toolssuchasdynamicnetwork
| risk. By | embedding | these | theories | into | algorithmic | design, |     |     |     |     |     |     |     |     |
| -------- | --------- | ----- | -------- | ---- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
HBA systems become more aligned with real-world human graphs[373]andsentiment-flowmodelsareusedtoquantify
variabilityandlesspronetooversimplificationorbias. interactions over time, revealing insights into leadership
|     |     |     |     |     |     |     |     | influence,   | information |              | diffusion, | or community |          | resilience. |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------------ | ---------- | ------------ | -------- | ----------- |
|     |     |     |     |     |     |     |     | By embedding |             | sociological |            | constructs   | into HBA | systems,    |
2) NEUROSCIENCEANDBEHAVIORALMONITORING
|           |                 |          |     |          |      |                |     | researchers | and        | practitioners |     | can better     | assess | the interplay |
| --------- | --------------- | -------- | --- | -------- | ---- | -------------- | --- | ----------- | ---------- | ------------- | --- | -------------- | ------ | ------------- |
| Advances  | in neuroscience |          | are | allowing | HBA  | systems        | to  |             |            |               |     |                |        |               |
|           |                 |          |     |          |      |                |     | between     | individual | behavior      |     | and collective | norms, | yielding      |
| go beyond | observable      | behavior |     | and tap  | into | the underlying |     |             |            |               |     |                |        |               |
insightsthatarebothpredictiveandexplanatory.
| neural correlates |              | of cognition |          | and emotion.   |           | Wearable      | neu-  |                      |           |             |                |               |            |              |
| ----------------- | ------------ | ------------ | -------- | -------------- | --------- | ------------- | ----- | -------------------- | --------- | ----------- | -------------- | ------------- | ---------- | ------------ |
| roimaging         | tools        | such as      | EEG      | and functional |           | near-infrared |       |                      |           |             |                |               |            |              |
|                   |              |              |          |                |           |               |       | VIII. CONCLUSION     |           |             |                |               |            |              |
| spectroscopy      | (fNIRS)      | [368]        | offer    | real-time      |           | access to     | brain |                      |           |             |                |               |            |              |
|                   |              |              |          |                |           |               |       | This survey          | has       | provided    | a              | comprehensive | analysis   | of the       |
| activity in       | naturalistic | settings.    |          | These          | data      | can be used   | to    |                      |           |             |                |               |            |              |
|                   |              |              |          |                |           |               |       | current              | state of  | HBA,        | encompassing   | foundational  |            | concepts,    |
| train multimodal  |              | models       | that     | associate      | neural    | patterns      | with  |                      |           |             |                |               |            |              |
|                   |              |              |          |                |           |               |       | recent computational |           |             | techniques,    | and           | diverse    | application  |
| behavioral        | responses,   | enabling     |          | more           | accurate  | detection     | of    |                      |           |             |                |               |            |              |
|                   |              |              |          |                |           |               |       | domains              | such as   | healthcare, |                | education,    | marketing, | security,    |
| cognitive         | load,        | emotional    | arousal, | or             | attention | lapses.       | For   |                      |           |             |                |               |            |              |
|                   |              |              |          |                |           |               |       | and workplace        |           | well-being. | By             | synthesizing  |            | developments |
| example,          | combining    | neural       | signals  | with           | facial    | expressions   |       |                      |           |             |                |               |            |              |
|                   |              |              |          |                |           |               |       | in machine           | learning, |             | deep learning, | computer      |            | vision, and  |
andspeechallowsforricheremotionmodelingintherapeutic
|     |     |     |     |     |     |     |     | natural | language | processing, |     | the review | underscores | how |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ----------- | --- | ---------- | ----------- | --- |
oreducationalsettings[369].Inautonomousdrivingorhigh-
thesetechnologiesarereshapingourabilitytomodel,predict,
| stress environments, |     | real-time |     | brain monitoring |     | can | trigger |     |     |     |     |     |     |     |
| -------------------- | --- | --------- | --- | ---------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
andinterprethumanbehavioracrossreal-worldcontexts.
| adaptive | system | behaviors | to  | reduce | overload | [370]. | This |         |                   |     |     |            |        |             |
| -------- | ------ | --------- | --- | ------ | -------- | ------ | ---- | ------- | ----------------- | --- | --- | ---------- | ------ | ----------- |
|          |        |           |     |        |          |        |      | Despite | its comprehensive |     |     | scope, the | review | has several |
fusionofbehavioralandneurophysiologicalsignalssupports
|     |     |     |     |     |     |     |     | limitations | that | must | be acknowledged. |     | First, | although |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ---- | ---------------- | --- | ------ | -------- |
morepreciseandresponsiveHBAinterventions,particularly
|     |     |     |     |     |     |     |     | we consulted |     | major | academic | databases, | some | relevant |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | -------- | ---------- | ---- | -------- |
inneurodivergentcareorcognitiverehabilitation.
|     |     |     |     |     |     |     |     | grey literature, |     | domain-specific |      | repositories, |         | or emerging |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------- | ---- | ------------- | ------- | ----------- |
|     |     |     |     |     |     |     |     | preprints        | may | have            | been | excluded.     | Second, | the scope   |
3) HEALTHCAREANDWEARABLETECHNOLOGY was limited to English-language publications, potentially
Theconvergenceofwearabletechnologyandhealthcarehas omittingsignificantcontributionsinotherlanguages.Third,
unlocked new frontiers in behavioral monitoring. Devices the review reflects the state of the literature only up to
such as smartwatches, fitness bands, and biosensor patches March 2024, which means recent advances may not be
continuously collect physiological indicators—heart rate, captured. Additionally, the heterogeneity in methodologies,
electrodermal activity, movement patterns—that correlate datasets, and evaluation metrics across studies makes direct
with psychological states such as stress, fatigue, or depres- performance comparisons challenging. Finally, due to these
sion. When these data streams are interpreted alongside inconsistencies, we did not conduct a formal meta-analysis,
self-reportedmeasuresorenvironmentalcontext,theyallow which might have further quantified trends and model
| for the creation |     | of personalized |     | health | profiles | and | just- | effectiveness. |     |     |     |     |     |     |
| ---------------- | --- | --------------- | --- | ------ | -------- | --- | ----- | -------------- | --- | --- | --- | --- | --- | --- |
in-time adaptive interventions (JITAI) [371]. For example, Looking ahead, we recommend several future research
inpost-operativecareorchronicillnessmanagement,behav- directions to strengthen the field of HBA. There is a press-
ioral deviations from baseline can prompt automated alerts ing need for standardized benchmarks, including publicly
or caregiver notifications. Collaboration between clinicians, availabledatasetsandunifiedevaluationprotocols,toenable
biomedical engineers, and behavioral scientists ensures that reproducibilityandfairmodelcomparison.Interdisciplinary
thesetechnologiesarebothmedicallyvalidanduser-friendly. collaboration should also be encouraged, bringing together
| 128408 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
expertise from artificial intelligence, psychology, ethics, [12] S.VishwakarmaandA.Agrawal,‘‘Asurveyonactivityrecognitionand
and social sciences to develop more holistic and socially behavior understanding in video surveillance,’’ Vis. Comput., vol. 29,
no.10,pp.983–1009,Oct.2013.
| responsible | behavior analysis | systems. Privacy-preserving |     |                                                                   |     |     |     |     |
| ----------- | ----------------- | --------------------------- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- |
|             |                   |                             |     | [13] R.Lileikyte,D.Irvin,andJ.H.L.Hansen,‘‘Assessingchildcommuni- |     |     |     |     |
techniquessuchasfederatedlearninganddifferentialprivacy
cationengagementandstatisticalspeechpatternsforAmericanEnglish
must be prioritized to ensure ethical deployment, especially via speech recognition in naturalistic active learning spaces,’’ Speech
Commun.,vol.140,pp.98–108,May2022.
| in sensitive | domains. Furthermore, | more longitudinal | and |     |     |     |     |     |
| ------------ | --------------------- | ----------------- | --- | --- | --- | --- | --- | --- |
cross-cultural studies are essential to capture behavioral [14] G. Onofrei, R. Filieri, and L. Kennedy, ‘‘Social media interactions,
|     |     |     |     | purchase | intention, and | behavioural engagement: | The mediating | role |
| --- | --- | --- | --- | -------- | -------------- | ----------------------- | ------------- | ---- |
diversity and mitigate algorithmic bias. Future models of source and content factors,’’ J. Bus. Res., vol. 142, pp. 100–112,
| should emphasize | explainability | to promote transparency        | in  | Mar.2022.                                                       |                    |                      |              |        |
| ---------------- | -------------- | ------------------------------ | --- | --------------------------------------------------------------- | ------------------ | -------------------- | ------------ | ------ |
|                  |                |                                |     | [15] A.BenMabroukandE.Zagrouba,‘‘Abnormalbehaviorrecognitionfor |                    |                      |              |        |
| decision-making  | processes.     | Finally, advancing lightweight |     |                                                                 |                    |                      |              |        |
|                  |                |                                |     | intelligent                                                     | video surveillance | systems: A review,’’ | Expert Syst. | Appl., |
and real-time solutions suitable for edge computing will be vol.91,pp.480–491,Jan.2018.
criticalfordeployingHBAtechnologiesinmobile,wearable,
|     |     |     |     | [16] N.K.Singh,D.S.Tomar,andA.K.Sangaiah,‘‘Sentimentanalysis:A |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- |
reviewandcomparativeanalysisoversocialmedia,’’J.AmbientIntell.
orresource-constrainedenvironments.
HumanizedComput.,vol.11,no.1,pp.97–117,Jan.2020.
Inconclusion,HBAisarapidlyevolvingfieldattheinter-
|     |     |     |     | [17] J.M.Chaquet,E.J.Carmona,andA.Fernández-Caballero,‘‘Asurveyof |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- |
sectionofdatascienceandhuman-centereddisciplines.This videodatasetsforhumanactionandactivityrecognition,’’Comput.Vis.
survey aims to serve as a foundation for future exploration, ImageUnderstand.,vol.117,no.6,pp.633–659,Jun.2013.
offeringapanoramicviewofexistingtechniques,challenges, [18] F.Demrozi,G.Pravadelli,A.Bihorac,andP.Rashidi,‘‘Humanactivity
recognitionusinginertial,physiologicalandenvironmentalsensors:A
and opportunities. As computational tools become more comprehensivesurvey,’’IEEEAccess,vol.8,pp.210816–210836,2020.
integrated into daily life, the responsible and effective [19] Y.KongandY.Fu,‘‘Humanactionrecognitionandprediction:Asurvey,’’
analysisofhumanbehaviorwillplayavitalroleinshaping Int.J.Comput.Vis.,vol.130,no.5,pp.1366–1401,May2022.
|     |     |     |     | [20] B.DegardinandH.Proença,‘‘Humanbehavioranalysis:Asurveyon |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- |
intelligent,inclusive,andadaptivesystems.
actionrecognition,’’Appl.Sci.,vol.11,no.18,p.8324,Sep.2021.
|     |     |     |     | [21] A. Fuchs, | A. Passarella, | and M. Conti, ‘‘Modeling, | replicating, | and |
| --- | --- | --- | --- | -------------- | -------------- | ------------------------- | ------------ | --- |
predictinghumanbehavior:Asurvey,’’ACMTrans.Auto.Adapt.Syst.,
REFERENCES
vol.18,no.2,pp.1–47,Jun.2023.
[1] J. M. Box-Steffensmeier et al., ‘‘The future of human behaviour [22] A.G.Martín,A.Fernández-Isabel,I.MartíndeDiego,andM.Beltrán,‘‘A
research,’’NatureHumanBehaviour,vol.6,no.1,pp.15–24,Jan.2022,
surveyforuserbehavioranalysisbasedonmachinelearningtechniques:
doi:10.1038/s41562-021-01275-6. Currentmodelsandapplications,’’Int.J.SpeechTechnol.,vol.51,no.8,
[2] N. Jaouedi, N. Boujnah, O. Htiwich, and M. S. Bouhlel, ‘‘Human pp.6029–6055,Aug.2021.
actionrecognitiontohumanbehavioranalysis,’’inProc.7thInt.Conf. [23] D. Gowsikhaa, S. Abirami, and R. Baskaran, ‘‘Automated human
Sci.Electron.,Technol.Inf.Telecommun.(SETIT),Hammamet,Tunisia, behavioranalysisfromsurveillancevideos:Asurvey,’’Artif.Intell.Rev.,
Dec.2016,pp.263–266,doi:10.1109/SETIT.2016.7939877. vol.42,no.4,pp.747–765,Dec.2014.
[3] Q.Wei,A.Bao,D.Lv,S.Liu,S.Chen,Y.Chi,andJ.Zuo,‘‘Theinfluence [24] M.Yoon,J.Lee,andI.-H.Jo,‘‘Videolearninganalytics:Investigating
ofmessageframeandproducttypeongreenconsumerpurchasedecisions behavioralpatternsandlearnerclustersinvideo-basedonlinelearning,’’
:AnERPsstudy,’’Sci.Rep.,vol.14,no.1,p.23232,Oct.2024,doi: InternetHigherEduc.,vol.50,Jun.2021,Art.no.100806.
10.1038/s41598-024-75056-2.
|     |     |     |     | [25] J.B.Jarecki,J.H.Tan,andM.A.Jenny,‘‘Aframeworkforbuilding |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- |
[4] Y.Gao,H.Xie,Q.Wang,andC.Chen,‘‘Howeducationalinequality cognitive process models,’’ Psychonomic Bull. Rev., vol. 27, no. 6,
affectsfamilymultichildbehavior—Evidencefromsuperhighschools,’’ pp.1218–1229,Dec.2020.
HumanitiesSocialSci.Commun.,vol.11,no.1,p.1340,Oct.2024,doi: [26] A.A.Matveeva,K.B.Sultonova,andD.S.Abbasova,‘‘Optimization
10.1057/s41599-024-03838-0. ofpsychodiagnosticsofemotionalstates,’’DanishSci.J.,vol.3,no.5,
[5] K.E.Hoque,X.Wang,Y.Qi,andN.Norzan,‘‘Thefactorsassociatedwith pp.24–27,2020.
teachers’jobsatisfactionandtheirimpactsonstudents’achievement:A [27] P.Hagenaars,‘‘Towardsahumanrightsbasedandorientedpsychology,’’
review(2010–2021),’’HumanitiesSocialSci.Commun.,vol.10,no.1,
Psychol.DevelopingSocieties,vol.28,no.2,pp.183–202,Sep.2016.
p.177,Apr.2023,doi:10.1057/s41599-023-01645-7.
|     |     |     |     | [28] V.Vanberg,‘‘Theperspectiveofsociology,’’inReadingsinPublicChoice |     |     |     |     |
| --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- |
[6] Z.Wang,Y.Hou,K.Jiang,C.Zhang,W.Dou,Z.Huang,andY.Guo,‘‘A andConstitutionalPoliticalEconomy.NewYork,NY,USA:Springer,
| surveyonhumanbehaviorrecognitionusingsmartphone-basedultrasonic |     |     |     | 2008,p.264. |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
signal,’’IEEEAccess,vol.7,pp.100581–100604,2019. [29] R. Bakeman and V. Quera, Sequential Analysis and Observational
[7] Y.Yin,L.Xie,Z.Jiang,F.Xiao,J.Cao,andS.Lu,‘‘Asystematicreviewof MethodsfortheBehavioralSciences.Cambridge,U.K.:CambridgeUniv.
| humanactivityrecognitionbasedonmobiledevices:Overview,progress |     |     |     | Press,2011. |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- |
andtrends,’’IEEECommun.SurveysTuts.,vol.26,no.2,pp.890–929, [30] J.L.Andreassi,Psychophysiology:HumanBehaviorandPhysiological
2ndQuart.,2024,doi:10.1109/COMST.2024.3357591. Response,5thed.,NewYork,NY,USA:PsychologyPress,2010.
[8] F.Gu,M.-H.Chung,M.Chignell,S.Valaee,B.Zhou,andX.Liu,‘‘A [31] H. Timmermans, Pedestrian Behavior: Models, Data Collection and
surveyondeeplearningforhumanactivityrecognition,’’ACMComput.
Applications.Bingley,U.K.:EmeraldGroupPublishingLtd,2009.
Surveys(CSUR),vol.54,no.8,pp.1–34,Oct.2021.
|     |     |     |     | [32] C. J. | Lumsden and E. O. | Wilson, ‘‘Translation | of epigenetic | rules of |
| --- | --- | --- | --- | ---------- | ----------------- | --------------------- | ------------- | -------- |
[9] I. Lamaakal, N. El Mourabit, K. El Makkaoui, I. Ouahbi, and Y. individualbehaviorintoethnographicpatterns,’’Proc.Nat.Acad.Sci.
Maleh,‘‘Efficientgesture-basedrecognitionoftifinaghcharactersinair USA,vol.77,no.7,pp.4382–4386,Jul.1980.
handwritingwithaTinyDLmodel,’’inProc.6thInt.Conf.Intell.Comput. [33] J.Lu,M.Nguyen,andW.Q.Yan,‘‘Deeplearningmethodsforhuman
DataSci.(ICDS),Oct.2024,pp.1–8. behaviorrecognition,’’inProc.35thInt.Conf.ImageVis.Comput.New
[10] S. Essahraui, I. Lamaakal, I.ElHamly, Y. Maleh, I. Ouahbi, Zealand(IVCNZ),Nov.2020,pp.1–6.
K.ElMakkaoui, M. F. Bouami, P. Pławiak, O. Alfarraj, and [34] S. Narayanan and P. G. Georgiou, ‘‘Behavioral signal processing:
A.A.AbdEl-Latif, ‘‘Real-time driver drowsiness detection using Deriving human behavioral informatics from speech and language,’’
facialanalysisandmachinelearningtechniques,’’Sensors,vol.25,no.3, Proc.IEEE,vol.101,no.5,pp.1203–1233,May2013.
p.812,Jan.2025.
|     |     |     |     | [35] P.Vanneste,J.Oramas,T.Verelst,T.Tuytelaars,A.Raes,F.Depaepe, |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- |
[11] H. D. Critchley and S. N. Garfinkel, ‘‘The influence of physiological and W. Van den Noortgate, ‘‘Computer vision and human behaviour,
signalsoncognition,’’CurrentOpinionBehav.Sci.,vol.19,pp.13–18, emotionandcognitiondetection:AusecaseonStudentengagement,’’
| Feb.2018.     |     |     |     | Mathematics,vol.9,no.3,p.287,Feb.2021. |     |     |     |        |
| ------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | ------ |
| VOLUME13,2025 |     |     |     |                                        |     |     |     | 128409 |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[36] R.Krishnamurthi,A.Kumar,D.Gopinathan,A.Nayyar,andB.Qureshi, [58] Y. Cho, N. Bianchi-Berthouze, and S. J. Julier, ‘‘DeepBreath: Deep
‘‘An overview of IoT sensor data processing, fusion, and analysis learningofbreathingpatternsforautomaticstressrecognitionusinglow-
techniques,’’Sensors,vol.20,no.21,p.6076,Oct.2020. costthermalimaginginunconstrainedsettings,’’inProc.7thInt.Conf.
[37] H.ShteingartandY.Loewenstein,‘‘Reinforcementlearningandhuman Affect.Comput.Intell.Interact.(ACII),Oct.2017,pp.456–463.
behavior,’’CurrentOpinionNeurobiol.,vol.25,pp.93–98,Apr.2014. [59] R. Subramanian, J. Wache, M. K. Abadi, R. L. Vieriu, S. Winkler,
[38] M. Acheli, D. Grigori, and M. Weidlich, ‘‘Discovering and analyzing andN.Sebe,‘‘ASCERTAIN:Emotionandpersonalityrecognitionusing
contextual behavioral patterns from event logs,’’ IEEE Trans. Knowl. commercialsensors,’’IEEETrans.Affect.Comput.,vol.9,no.2,pp.147–
| DataEng.,vol.34,no.12,pp.5708–5721,Dec.2022. |     |     |     |     |     |     | 160,Apr.2018. |     |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
[39] Y.Wu,N.Cao,D.Gotz,Y.-P.Tan,andD.A.Keim,‘‘Asurveyonvisual [60] J.H.L.HansenandS.E.Bou-Ghazale,‘‘GettingstartedwithSUSAS:
analyticsofsocialmediadata,’’IEEETrans.Multimedia,vol.18,no.11, Aspeechundersimulatedandactualstressdatabase,’’inProc.5thEur.
pp.2135–2148,Nov.2016. Conf.SpeechCommun.Technol.(Eurospeech),Sep.1997,pp.1–4.
[40] L.N.AbdullahandS.A.M.Noah,‘‘Integratingaudiovisualdatafor [61] P.Lucey,J.F.Cohn,T.Kanade,J.Saragih,Z.Ambadar,andI.Matthews,
humanactiondetection,’’inProc.5thInt.Conf.Comput.Graph.,Imag. (CK+):
|     |     |     |     |     |     |     | ‘‘The | extended | cohn-kanade | dataset |     | A complete | dataset for |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ----------- | ------- | --- | ---------- | ----------- |
Visualisation,Aug.2008,pp.242–246. actionunitandemotion-specifiedexpression,’’inProc.IEEEComput.
[41] S.Seneviratne,Y.Hu,T.Nguyen,G.Lan,S.Khalifa,K.Thilakarathna, Soc.Conf.Comput.Vis.PatternRecognit.Workshops,Jun.2010,pp.94–
| M. Hassan, | and | A. Seneviratne, | ‘‘A | survey of | wearable | devices and | 101. |     |     |     |     |     |     |
| ---------- | --- | --------------- | --- | --------- | -------- | ----------- | ---- | --- | --- | --- | --- | --- | --- |
challenges,’’IEEECommun.SurveysTuts.,vol.19,no.4,pp.2573–2620, [62] G. Zhao, X. Huang, M. Taini, S. Z. Li, and M. Pietikäinen, ‘‘Facial
4thQuart.,2017. expressionrecognitionfromnear-infraredvideos,’’ImageVis.Comput.,
| [42] D. M. | Hilty and | S. Chan, | ‘‘Human | behavior | with mobile | health: |     |     |     |     |     |     |     |
| ---------- | --------- | -------- | ------- | -------- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
vol.29,no.9,pp.607–619,Aug.2011.
Smartphone/devices,appsandcognition,’’Psychol.Cognit.Sci.Open
[63] D.Lundqvist,A.Flykt,andA.Hman,‘‘Karolinskadirectedemotional
J.,vol.4,no.2,pp.36–47,Dec.2018. faces,’’CognitionEmotion,vol.1998,pp.1–5,Apr.1998.
[43] C.-D. Ham, J. Lee, J. L. Hayes, and Y. H. Bae, ‘‘Exploring sharing [64] M.JeongandB.C.Ko,‘‘Driver’sfacialexpressionrecognitioninreal-
behaviorsacrosssocialmediaplatforms,’’Int.J.MarketRes.,vol.61, timeforsafedriving,’’Sensors,vol.18,no.12,p.4270,Dec.2018.
no.2,pp.157–177,Mar.2019.
|                     |     |           |        |           |            |             | [65] P. J. Phillips, | H.  | Moon, | S. A. Rizvi, | and | P. J. Rauss, | ‘‘The FERET |
| ------------------- | --- | --------- | ------ | --------- | ---------- | ----------- | -------------------- | --- | ----- | ------------ | --- | ------------ | ----------- |
| [44] J. R. Kwapisz, | G.  | M. Weiss, | and S. | A. Moore, | ‘‘Activity | recognition |                      |     |       |              |     |              |             |
evaluationmethodologyforface-recognitionalgorithms,’’IEEETrans.
usingcellphoneaccelerometers,’’ACMSIGKDDExplorationsNewslett.,
PatternAnal.Mach.Intell.,vol.22,no.10,pp.1090–1104,Oct.2000.
vol.12,no.2,pp.74–82,Mar.2011.
|     |     |     |     |     |     |     | [66] N. Sharma, | A.  | Dhall, T. | Gedeon, | and R. | Goecke, ‘‘Thermal | spatio- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------- | ------- | ------ | ----------------- | ------- |
[45] D.Anguita,A.Ghio,L.Oneto,X.Parra,andJ.L.Reyes-Ortiz,‘‘Apublic
temporaldataforstressrecognition,’’EURASIPJ.ImageVideoProcess.,
domaindatasetforhumanactivityrecognitionusingsmartphones,’’in vol.2014,no.1,pp.1–12,Dec.2014.
Proc.Eur.Symp.Artif.NeuralNetw.,Jan.2013,pp.437–442.
[67] H.-C.Chou,W.-C.Lin,L.-C.Chang,C.-C.Li,H.-P.Ma,andC.-C.Lee,
[46] M.ZhangandA.A.Sawchuk,‘‘USC-HAD:Adailyactivitydatasetfor
‘‘NNIME:TheNTHU-NTUAChineseinteractivemultimodalemotion
ubiquitousactivityrecognitionusingwearablesensors,’’inProc.ACM
corpus,’’inProc.7thInt.Conf.Affect.Comput.Intell.Interact.(ACII),
Conf.UbiquitousComput.,Sep.2012,pp.1036–1043.
Oct.2017,pp.292–298.
| [47] A. Reiss | and D.        | Stricker, | ‘‘Introducing | a new      | benchmarked | dataset  |                   |     |           |     |              |          |             |
| ------------- | ------------- | --------- | ------------- | ---------- | ----------- | -------- | ----------------- | --- | --------- | --- | ------------ | -------- | ----------- |
|               |               |           |               |            |             |          | [68] K. Mundnich, | B.  | M. Booth, | M.  | L’Hommedieu, | T. Feng, | B. Girault, |
| for activity  | monitoring,’’ | in        | Proc. 16th    | Int. Symp. | Wearable    | Comput., |                   |     |           |     |              |          |             |
Jun.2012,pp.108–109. J.L’Hommedieu,M.Wildman,S.Skaaden,A.Nadarajan,J.L.Villatte,
T.H.Falk,K.Lerman,E.Ferrara,andS.Narayanan,‘‘TILES-2018,a
| [48] M. Plotnik, | D.  | Roggen, N. | Giladi, | J. M. Hausdorff, | G.  | Tröster, and |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | ------- | ---------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
longitudinalphysiologicandbehavioraldatasetofhospitalworkers,’’
| M.Bächlin, | ‘‘A | wearable | system | to assist walking | of  | Parkinson’s |     |     |     |     |     |     |     |
| ---------- | --- | -------- | ------ | ----------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
ScientificData,vol.7,no.1,pp.1–26,Oct.2020.
| disease | patients,’’ | Methods | Inf. Med., | vol. 49, | no. 1, | pp. 88–95, |                  |     |         |     |            |         |               |
| ------- | ----------- | ------- | ---------- | -------- | ------ | ---------- | ---------------- | --- | ------- | --- | ---------- | ------- | ------------- |
|         |             |         |            |          |        |            | [69] A. Montoya, | D.  | Holman, | T.  | Smith, and | W. Kan. | (2016). State |
2010.
FarmDistractedDriverDetection.Accessed:Sep.26,2024.[Online].
[49] P.Zappi,C.Lombriser,T.Stiefmeier,E.Farella,D.Roggen,L.Benini,
andG.Trster,‘‘Activityrecognitionfromon-bodysensors:Acc-power Available: https://kaggle.com/competitions/state-farm-distracted-driver-
detection
| trade-off | by dynamic | sensor | selection,’’ | in Proc. | Eur. Conf. | Wireless |                 |              |     |              |     |           |                |
| --------- | ---------- | ------ | ------------ | -------- | ---------- | -------- | --------------- | ------------ | --- | ------------ | --- | --------- | -------------- |
|           |            |        |              |          |            |          | [70] M. Martin, | A. Roitberg, |     | M. Haurilet, | M.  | Horne, S. | Reiß, M. Voit, |
SensorNetw.,2008,pp.17–33.
|     |     |     |     |     |     |     | and R. | Stiefelhagen, | ‘‘Drive&act: |     | A multi-modal | dataset | for fine- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | ------------ | --- | ------------- | ------- | --------- |
[50] C.Schuldt,I.Laptev,andB.Caputo,‘‘Recognizinghumanactions:A
graineddriverbehaviorrecognitioninautonomousvehicles,’’inProc.
localSVMapproach,’’inProc.17thInt.Conf.PatternRecognit.,2004,
IEEE/CVFInt.Conf.Comput.Vis.(ICCV),Oct.2019,pp.2801–2810,
pp.32–36.
[51] O. Banos, R. Garcia, J. A. Holgado-Terriza, M. Damas, H. Pomares, doi:10.1109/ICCV.2019.00289.
I.Rojas,A.Saez,andC.Villalonga,‘‘MHealthDroid:Anovelframework [71] W.-L. Zheng and B.-L. Lu, ‘‘A multimodal approach to estimating
vigilanceusingEEGandforeheadEOG,’’J.NeuralEng.,vol.14,no.2,
| for agile | development | of mobile | health | applications,’’ |     | in Proc. Int. |     |     |     |     |     |     |     |
| --------- | ----------- | --------- | ------ | --------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Apr.2017,Art.no.026017.
WorkshopAmbientAssist.Living,Jan.2014,pp.91–98.
|     |     |     |     |     |     |     | [72] S. Taamneh, | P.  | Tsiamyrtzis, | M.  | Dcosta, | P. Buddharaju, | A. Khatri, |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | ------- | -------------- | ---------- |
[52] S.Gaglio,G.L.ReandM.Morana,‘‘Humanactivityrecognitionprocess
|     |     |     |     |     |     |     | M.Manser, | T. Ferris, | R.  | Wunderlich, | and | I. Pavlidis, | ‘‘A multimodal |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ----------- | --- | ------------ | -------------- |
using3-Dposturedata,’’IEEETrans.Hum.-Mach.Syst.,vol.45,no.5,
pp.586–597,Oct.2014. datasetforvariousformsofdistracteddriving,’’ScientificData,vol.4,
[53] C.Liu,Y.Hu,Y.Li,S.Song,andJ.Liu,‘‘PKU-MMD:Alargescale no.1,pp.1–21,Aug.2017.
benchmark for continuous multi-modal human action understanding,’’ [73] J.A.HealeyandR.W.Picard,‘‘Detectingstressduringreal-worlddriving
|     |     |     |     |     |     |     | tasks using | physiological |     | sensors,’’ | IEEE | Trans. Intell. | Transp. Syst., |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | --- | ---------- | ---- | -------------- | -------------- |
2017,arXiv:1703.07475.
vol.6,no.2,pp.156–166,Jun.2005.
[54] D.Roggen,A.Calatroni,M.Rossi,T.Holleczek,K.Förster,G.Tröster,
[74] R.K.Sah,M.McDonell,P.Pendry,S.Parent,H.Ghasemzadeh,and
P.Lukowicz,D.Bannach,G.Pirkl,A.Ferscha,J.Doppler,C.Holzmann,
M.Kurz,G.Holl,R.Chavarriaga,H.Sagha,H.Bayati,M.Creatura, M.J.Cleveland,‘‘ADARP:Amultimodaldatasetforstressandalcohol
andJ.D.R.Millán,‘‘Collectingcomplexactivitydatasetsinhighlyrich relapsequantificationinreallifesetting,’’inProc.IEEE-EMBSInt.Conf.
WearableImplant.BodySensorNetw.(BSN),Sep.2022,pp.1–4.
networkedsensorenvironments,’’inProc.7thInt.Conf.NetworkedSens.
Syst.(INSS),Jun.2010,pp.233–240. [75] J.D.Ortega,N.Köse,P.N.Cañas,M.-A.Chao,A.Unnervik,M.Nieto,
O.Otaegui,andL.Salgado,‘‘DMD:Alarge-scalemulti-modaldriver
[55] K.Soomro,A.RoshanZamir,andM.Shah,‘‘UCF101:Adatasetof101
humanactionsclassesfromvideosinthewild,’’2012,arXiv:1212.0402. monitoringdatasetforattentionandalertnessanalysis,’’inProc.Comput.
[56] C. Wolf, E. Lombardi, J. Mille, O. Celiktutan, M. Jiu, E. Dogan, Vision–ECCVWorkshops,Jan.2020,pp.387–405.
G.Eren, M. Baccouche, E. Dellandréa, C.-E. Bichot, C. Garcia, and [76] V.Ramanishka,Y.-T.Chen,T.Misu,andK.Saenko,‘‘Towarddriving
B.Sankur,‘‘Evaluationofvideoactivitylocalizationsintegratingquality sceneunderstanding:Adatasetforlearningdriverbehaviorandcausal
andquantitymeasurements,’’Comput.Vis.ImageUnderstand.,vol.127, reasoning,’’inProc.IEEE/CVFConf.Comput.Vis.PatternRecognit.,
pp.14–30,Oct.2014,doi:10.1016/j.cviu.2014.06.014. Jun.2018,pp.7699–7707.
[57] V.Markova,T.Ganchev,andK.Kalinkov,‘‘Clas:Adatabaseforcognitive [77] X. Tao, D. Gao, W. Zhang, T. Liu, B. Du, S. Zhang, and Y. Qin,
load,affectandstressrecognition,’’in2019Int.Conf.Biomed.Innov. ‘‘A multimodal physiological dataset for driving behaviour analysis,’’
Appl.(BIA),pp.1–4,2019. ScientificData,vol.11,no.1,p.378,Apr.2024.
| 128410 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[78] A. L. Goldberger, L. A. N. Amaral, L. Glass, J. M. Hausdorff, [97] Kaggle.(2017).Employee’sPerformanceforHRAnalytics.Accessed:
P.C.Ivanov,R.G.Mark,J.E.Mietus,G.B.Moody,C.-K.Peng,and Sep. 26, 2024. [Online]. Available: https://www.kaggle.com/datasets/
H.E.Stanley,‘‘PhysioBank,PhysioToolkit,andPhysioNet:Components patelprashant/employee-attrition
ofanewresearchresourceforcomplexphysiologicsignals,’’Circulation, [98] UCIMachineLearningRepository.Accessed:Sep.26,2024.[Online].
vol.101,no.23,pp.e215–e220,Jun.2000. Available:https://archive.ics.uci.edu/dataset/352/online+retail
[79] G.B.MoodyandR.G.Mark,‘‘TheimpactoftheMIT-BIHarrhythmia
|             |           |      |             |          |        |            | [99] Kaggle. | Instacart  | Market                                            | Basket | Analysis. | Accessed: | Sep. | 26, 2024. |
| ----------- | --------- | ---- | ----------- | -------- | ------ | ---------- | ------------ | ---------- | ------------------------------------------------- | ------ | --------- | --------- | ---- | --------- |
| database,’’ | IEEE Eng. | Med. | Biol. Mag., | vol. 20, | no. 3, | pp. 45–50, |              |            |                                                   |        |           |           |      |           |
|             |           |      |             |          |        |            | [Online].    | Available: | https://www.kaggle.com/c/instacart-market-basket- |        |           |           |      |           |
| May2001.    |           |      |             |          |        |            | analysis     |            |                                                   |        |           |           |      |           |
[80] (2010). CHB-MIT Scalp EEG Database. Accessed: Sep. 26, 2024. [100] UCI machine learning repository. Accessed: Sep. 26, 2024. [Online].
[Online].Available:https://physionet.org/content/chbmit/1.0.0/ Available:https://archive.ics.uci.edu/dataset/222/bank
[81] J. Jezewski, A. Matonia, T. Kupka, D. Roj, and R. Czabanski, [101] Kaggle. (2023). U.K. Consumer Trends: 1997–2022, Quarterly.
‘‘Determinationoffetalheartratefromabdominalsignals:Evaluation
Accessed:Sep.26,2024.[Online].Available:https://www.kaggle.com/
ofbeat-to-beataccuracyinrelationtothedirectfetalelectrocardiogram,’’
datasets/matarrgaye/uk-consumer-trends-current-price
BiomedizinischeTechnik/BiomedicalEng.,vol.57,no.5,pp.383–394,
|     |     |     |     |     |     |     | [102] Kaggle. | (2019). | Consumer |     | Complaint | Database. |     | Accessed: |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | -------- | --- | --------- | --------- | --- | --------- |
Jan.2012.
[82] A. E. W. Johnson, L. Bulgarelli, L. Shen, A. Gayles, A. Shammout, Sep. 26, 2024. [Online]. Available: https://www.kaggle.com/datasets/
selener/consumer-complaint-database
S.Horng,T.Li,M.A.Moody,B.M.Pimentel,T.Naumann,D.J.Stone,
[103] S.H.Kim,H.S.Choi,E.S.Jin,H.Choi,H.Lee,S.-H.Lee,C.Y.Lee,
R.Ghassemi,L.A.Celi,andR.G.Mark,‘‘MIMIC-IV,afreelyaccessible
|     |     |     |     |     |     |     | M. G. | Lee, | and Y. Kim, | ‘‘Predicting | severe | outcomes | using | national |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ----------- | ------------ | ------ | -------- | ----- | -------- |
electronichealthrecorddataset,’’Sci.Data,vol.10,no.1,Jan.2023,
earlywarningscore(NEWS)inpatientsidentifiedbyarapidresponse
Art.no.1.
[83] M. Tangermann, K.-R. Müller, A. Aertsen, N. Birbaumer, C. Braun, system:Aretrospectivecohortstudy,’’Sci.Rep.,vol.11,no.1,p.18021,
| C. Brunner, | R. Leeb, | C. Mehring, | K.  | J. Miller, | G. R. | Müller-Putz, | Sep.2021. |     |     |     |     |     |     |     |
| ----------- | -------- | ----------- | --- | ---------- | ----- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
G.Nolte,G.Pfurtscheller,H.Preissl,G.Schalk,A.Schlögl,C.Vidaurre, [104] S.Gumustop,S.Gallo-Bernal,F.McPeake,D.Briggs,M.S.Gee,and
|             |        |            |          |        |                 |       | O.S.Pianykh, |     | ‘‘Predicting | health | crises | from early | warning | signs in |
| ----------- | ------ | ---------- | -------- | ------ | --------------- | ----- | ------------ | --- | ------------ | ------ | ------ | ---------- | ------- | -------- |
| S. Waldert, | and B. | Blankertz, | ‘‘Review | of the | BCI competition | IV,’’ |              |     |              |        |        |            |         |          |
patientmedicalrecords,’’Sci.Rep.,vol.12,no.1,p.19267,Nov.2022.
FrontiersNeurosci.,vol.6,p.55,2012.
[84] N.Flores,R.L.Avitia,M.A.Reyna,andC.García,‘‘Readilyavailable [105] S.I.Ali,H.S.M.Bilal,M.Hussain,J.Hussain,F.A.Satti,M.Hussain,
ECGdatabases,’’J.Electrocardiology,vol.51,no.6,pp.1095–1097, G.H.Park,T.Chung,andS.Lee,‘‘Ensemblefeaturerankingforcost-
Nov.2018. basednon-overlappinggroups:Acasestudyofchronickidneydisease
[85] T.Penzel,G.B.Moody,R.G.Mark,A.L.Goldberger,andJ.H.Peter, diagnosisindevelopingcountries,’’IEEEAccess,vol.8,pp.215623–
215648,2020.
‘‘Theapnea-ECGdatabase,’’Proc.Comput.Cardiol.,vol.27,pp.255–
258,Nov.2002. [106] P.Li,H.Wang,G.Tian,andZ.Fan,‘‘Identificationofkeybiomarkersfor
[86] C.M.D.Acevedo,C.A.C.Vasquez,andJ.K.C.Gómez,‘‘Electronic earlywarningofdiabeticretinopathyusingBPneuralnetworkalgorithm
nose dataset for COPD detection from smokers and healthy people andhierarchicalclusteringanalysis,’’Sci.Rep.,vol.14,no.1,p.15108,
| through exhaled | breath | analysis,’’ | Data | Brief, | vol. 35, | Apr. 2021, | Jul.2024. |     |     |     |     |     |     |     |
| --------------- | ------ | ----------- | ---- | ------ | -------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Art.no.106767. [107] F.Shamout,T.Zhu,andD.A.Clifton,‘‘Machinelearningforclinical
[87] R. Wang, F. Chen, Z. Chen, T. Li, G. Harari, S. Tignor, X. Zhou, IEEE Rev. Biomed. Eng.,
|             |        |              |                |     |           |        | outcome   | prediction,’’ |     |     |     |     | vol. 14, | pp. 116– |
| ----------- | ------ | ------------ | -------------- | --- | --------- | ------ | --------- | ------------- | --- | --- | --- | --- | -------- | -------- |
| D.Ben-Zeev, | and A. | T. Campbell, | ‘‘StudentLife: |     | Assessing | mental | 126,2021. |               |     |     |     |     |          |          |
health,academicperformanceandbehavioraltrendsofcollegestudents [108] A.Hussain,K.Zafar,andA.R.Baig,‘‘Fog-centricIoTbasedframework
usingsmartphones,’’inProc.ACMInt.JointConf.PervasiveUbiquitous forhealthcaremonitoring,managementandearlywarningsystem,’’IEEE
| Comput.,Sep.2014,pp.3–14. |     |     |     |     |     |     | Access,vol.9,pp.74168–74179,2021. |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[88] N.Ruiz,H.Yu,D.A.Allessio,M.Jalal,A.Joshi,T.Murray,J.J.Magee,
|                |     |           |              |            |     |           | [109] E. Lella, | A.  | Pazienza, | D. Lofu, | R. Anglani, | and | F. Vitulano, | ‘‘An |
| -------------- | --- | --------- | ------------ | ---------- | --- | --------- | --------------- | --- | --------- | -------- | ----------- | --- | ------------ | ---- |
| K. M. Delgado, | V.  | Ablavsky, | S. Sclaroff, | I. Arroyo, | B.  | P. Woolf, |                 |     |           |          |             |     |              |      |
ensemblelearningapproachbasedondiffusiontensorimagingmeasures
S.A.Bargal,andM.Betke,‘‘ATL-BP:AStudentengagementdatasetand forAlzheimer’sdiseaseclassification,’’Electronics,vol.10,no.3,p.249,
| modelforaffecttransferlearningforbehaviorprediction,’’IEEETrans. |     |     |     |     |     |     | Jan.2021. |     |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Biometrics,Behav.,IdentitySci.,vol.5,no.3,pp.411–424,Mar.2022. [110] R. Soundararajan, A. V. Prabu, S. Routray, P. P. Malla, A. K. Ray,
[89] Y.Atoum,L.Chen,A.X.Liu,S.D.H.Hsu,andX.Liu,‘‘Automated
|             |               |      |        |             |      |            | G.Palai, | O.  | S. Faragallah, | M. Baz, | M. M. | Abualnaja, | M. M. | A. Eid, |
| ----------- | ------------- | ---- | ------ | ----------- | ---- | ---------- | -------- | --- | -------------- | ------- | ----- | ---------- | ----- | ------- |
| online exam | proctoring,’’ | IEEE | Trans. | Multimedia, | vol. | 19, no. 7, |          |     |                |         |       |            |       |         |
andA.N.Z.Rashed,‘‘Deeplytrainedreal-timebodysensornetworksfor
pp.1609–1624,Jul.2017.
analyzingthesymptomsofParkinson’sdisease,’’IEEEAccess,vol.10,
[90] R.Hasan,S.Palaniappan,S.Mahmood,A.Abbas,andK.U.Sarker, pp.63403–63421,2022.
‘‘DatasetofStudents’performanceusingStudentinformationsystem, [111] M. Izhar, S. A. A. Naqvi, A. Ahmed, S. Abdullah, N. Alturki, and
moodleandthemobileapplication‘eDify,’’’Data,vol.6,no.11,p.110,
|     |     |     |     |     |     |     | L. Jamel, | ‘‘Enhancing |     | healthcare | efficacy | through | IoT-edge | fusion: A |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ---------- | -------- | ------- | -------- | --------- |
Oct.2021.
novelapproachforsmarthealthmonitoringanddiagnosis,’’IEEEAccess,
[91] E.A.Amrieh,T.Hamtini,andI.Aljarah,‘‘Preprocessingandanalyzing
vol.11,pp.136456–136467,2023.
educationaldatasetusingX-APIforimprovingstudent’sperformance,’’
[112] D.Gupta,M.Gupta,S.Bhatt,andA.S.Tosun,‘‘Detectinganomalous
| in Proc. IEEE | Jordan | Conf. | Appl. Electr. | Eng. | Comput. | Technol. |     |     |     |     |     |     |     |     |
| ------------- | ------ | ----- | ------------- | ---- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
(AEECT),Nov.2015,pp.1–5. userbehaviorinremotepatientmonitoring,’’inProc.IEEE22ndInt.
Conf.Inf.ReuseIntegr.DataSci.(IRI),Aug.2021,pp.33–40.
| [92] F. Yang, | ‘‘SCB-dataset: | A dataset | for | detecting | Student | classroom |     |     |     |     |     |     |     |     |
| ------------- | -------------- | --------- | --- | --------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
[113] M.Abdallah,‘‘Design,simulation,anddevelopmentofaBioSensorfor
behavior,’’2023,arXiv:2304.02488.
virusesdetectionusingFPGA,’’IEEEJ.Transl.Eng.HealthMed.,vol.9,
[93] P.Schmidt,A.Reiss,R.Duerichen,C.Marberger,andK.VanLaerhoven,
pp.1–6,2021.
| ‘‘Introducing | WESAD, | a multimodal | dataset | for | wearable | stress and |     |     |     |     |     |     |     |     |
| ------------- | ------ | ------------ | ------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
affect detection,’’ in Proc. 20th ACM Int. Conf. Multimodal Interact., [114] J.Chandrasekharan,A.Joseph,A.Ram,andG.Nollo,‘‘ETMT:Atool
Oct.2018,pp.400–408. foreye-tracking-basedtrail-makingtesttodetectcognitiveimpairment,’’
[94] M.Gjoreski,M.Luštrek,M.Gams,andH.Gjoreski,‘‘Monitoringstress Sensors,vol.23,no.15,p.6848,Aug.2023.
withawristdeviceusingcontext,’’J.Biomed.Informat.,vol.73,pp.159– [115] L.Bai,K.Wang,D.Liu,andS.Wu,‘‘Potentialearlyeffectbiomarkers
forambientairpollutionrelatedmentaldisorders,’’Toxics,vol.12,no.7,
170,Sep.2017.
p.454,Jun.2024.
[95] R.Gavas,D.Das,T.Bhattacharjee,M.B.Sheshachala,L.K.Hissaria,
R.R.Vempada,V.S.Viraraghavan,A.D.Choudhury,K.Muralidharan, [116] X.ChenandZ.Pan,‘‘Aconvenientandlow-costmodelofdepression
R.K.Ramakrishnan,P.Balamuralidhar,andA.Pal,‘‘Asensor-enabled screeningandearlywarningbasedonvoicedatausingforpublicmental
digitaltriersocialstresstestinanenterprisecontext,’’PubMed,vol.2019, health,’’ Int. J. Environ. Res. Public Health, vol. 18, no. 12, p. 6441,
| pp.1321–1325,Jul.2019. |     |     |     |     |     |     | Jun.2021. |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
[96] S. Chaudhari, ‘‘Employee’s performance for HR analytics,’’ [117] S.X.Zhang,H.Huang,J.Li,M.Antonelli-Ponti,S.F.D.Paiva,and
Kaggle, San Francisc, CA, USA, Tech. Rep., 2023, J.A.daSilva,‘‘PredictorsofdepressionandanxietysymptomsinBrazil
doi: 10.34740/KAGGLE/DS/3537629. [Online]. Available: duringCOVID-19,’’Int.J.Environ.Res.PublicHealth,vol.18,no.13,
| https://www.kaggle.com/ds/3537629 |     |     |     |     |     |     | p.7026,Jun.2021. |     |     |     |     |     |     |        |
| --------------------------------- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | ------ |
| VOLUME13,2025                     |     |     |     |     |     |     |                  |     |     |     |     |     |     | 128411 |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[118] M.FaezipourandM.Faezipour,‘‘Sustainablesmartphone-basedhealth- [138] S.Essahraui,K.ElMakkaoui,M.F.Bouami,andI.Ouahbi,‘‘CNNand
caresystems:Asystemsengineeringapproachtoassesstheefficacyof visiontransformermodelsfordetectingcheatinginonlineexaminations:
respiratory monitoring apps,’’ Sustainability, vol. 12, no. 12, p. 5061, Acomparativeevaluation,’’inIntersectionofArtificialIntelligence,Data
Jun.2020. Science,andCutting-EdgeTechnologies:FromConceptsToApplications
[119] J. Y. Lee, C. K. Y. Chan, S. S. Chua, C. J. Ng, T. Paraidathathu, in Smart Environment (Lecture Notes in Networks and Systems),
vol.1353.Springer,2025,pp.295–301,doi:10.1007/978-3-031-88304-
| K.K.C.Lee, |     | and S.      | W. H.   | Lee, ‘‘Telemonitoring |      | and team-based   |     |       |     |     |     |     |     |
| ---------- | --- | ----------- | ------- | --------------------- | ---- | ---------------- | --- | ----- | --- | --- | --- | --- | --- |
| management |     | of glycemic | control | on people             | with | type 2 diabetes: | A   | 0_40. |     |     |     |     |     |
cluster-randomizedcontrolledtrial,’’J.Gen.InternalMed.,vol.35,no.1, [139] S.Essahraui,M.Bouyardan,I.ElHamly,K.ElMakkaoui,I.Ouahbi,and
pp.87–94,Jan.2020. M.F.Bouami,‘‘EnhancingexamintegrityinMoroccanhighereducation:
[120] R. Hu, B. Michel, D. Russo, N. Mora, G. Matrella, P. Ciampolini, AnAI-basedfingerprintverificationmodel,’’inProc.7thInt.Conf.Netw.,
Intell.Syst.Secur.,Apr.2024,pp.1–5.
| F.Cocchi, | E.  | Montanari, | S.  | Nunziata, | and T. | Brunschwiler, | ‘‘An |                                                                     |     |     |     |     |     |
| --------- | --- | ---------- | --- | --------- | ------ | ------------- | ---- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|           |     |            |     |           |        |               |      | [140] P.SharmaandM.Harkishan,‘‘Designinganintelligenttutoringsystem |     |     |     |     |     |
unsupervisedbehavioralmodelingandalertingsystembasedonpassive
sensing for elderly care,’’ Future Internet, vol. 13, no. 1, p. 6, forcomputerprograminginthePacific,’’Educ.Inf.Technol.,vol.27,
| Dec.2020. |     |     |     |     |     |     |     | no.5,pp.6197–6209,Jun.2022. |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
[121] H.Valecha,A.Varma,I.Khare,A.Sachdeva,andM.Goyal,‘‘Prediction [141] M.W.H.SpitzerandK.Moeller,‘‘Performanceincreasesinmathematics
ofconsumerbehaviourusingrandomforestalgorithm,’’inProc.5thIEEE withinanintelligenttutoringsystemduringCOVID-19relatedschool
UttarPradeshSect.Int.Conf.Electr.,Electron.Comput.Eng.(UPCON), closures:Alarge-scalelongitudinalevaluation,’’Comput.Educ.Open,
vol.6,Jun.2024,Art.no.100162.
Nov.2018,pp.1–6.
|             |          |          |     |                 |     |              |          | [142] K.-C. | Pai, B.-C. Kuo, | C.-H. Liao, | and Y.-M. | Liu, | ‘‘An application |
| ----------- | -------- | -------- | --- | --------------- | --- | ------------ | -------- | ----------- | --------------- | ----------- | --------- | ---- | ---------------- |
| [122] M. A. | Khadija, | A. Aziz, | and | W. Nurharjadmo, |     | ‘‘Predicting | consumer |             |                 |             |           |      |                  |
secondhandluxurypreferencesformarketingstrategyinpostpandemic of Chinese dialogue-based intelligent tutoring system in remedial
usingmachinelearning:AcasestudyofconsumerinIndonesia,’’inProc. instruction for mathematics learning,’’ Educ. Psychol., vol. 41, no. 2,
8thInt.Conf.Informat.Comput.(ICIC),Dec.2023,pp.1–6. pp.137–152,Feb.2021.
[123] J.Panduro-Ramirez,‘‘Machinelearning-basedcustomerbehavioranal- [143] A.NiandA.Cheung,‘‘Understandingsecondarystudents’continuance
|      |                |     |              |          |      |            |          | intention | to adopt AI-powered |     | intelligent | tutoring system | for English |
| ---- | -------------- | --- | ------------ | -------- | ---- | ---------- | -------- | --------- | ------------------- | --- | ----------- | --------------- | ----------- |
| ysis | for e-commerce |     | platforms,’’ | in Proc. | Int. | Conf. Adv. | Comput., |           |                     |     |             |                 |             |
learning,’’Educ.Inf.Technol.,vol.28,no.3,pp.3191–3216,Mar.2023.
Commun.Appl.Informat.(ACCAI),May2024,pp.1–5.
|                      |     |              |     |             |     |              |        | [144] G.Asmussen,M.Rodemer,andS.Bernholt,‘‘Steppingstonestosuccess: |     |     |     |     |     |
| -------------------- | --- | ------------ | --- | ----------- | --- | ------------ | ------ | ------------------------------------------------------------------- | --- | --- | --- | --- | --- |
| [124] J. Chatterjee, |     | S. G. Neogi, | R.  | K. Dwivedi, | and | A. Vashisht, | ‘‘Con- |                                                                     |     |     |     |     |     |
sumer perspectives for purchase intentions of online pharmacy prod- A qualitative investigation of the effectiveness of adaptive stepped
ucts using deep learning,’’ in Proc. 11th Int. Conf. Rel., Infocom supportingtoolsforproblem-solvinginorganicchemistrytodesignan
intelligenttutoringsystem,’’Int.J.Sci.Educ.,vol.47,no.10,pp.1–23,
| Technol. | Optim. | (Trends | Future | Directions) | (ICRITO), | Mar. | 2024, |     |     |     |     |     |     |
| -------- | ------ | ------- | ------ | ----------- | --------- | ---- | ----- | --- | --- | --- | --- | --- | --- |
Jul.2025.
pp.1–8.
|     |     |     |     |     |     |     |     | [145] E. Kochmar, | D. Vu, | R. Belfer, | V. Gupta, | I. V. Serban, | and J. Pineau, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------ | ---------- | --------- | ------------- | -------------- |
[125] J.Kim,H.Ji,S.Oh,S.Hwang,E.Park,andA.P.delPobil,‘‘Adeep
|     |     |     |     |     |     |     |     | ‘‘Automated | personalized | feedback | improves | learning | gains in an |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | -------- | -------- | -------- | ----------- |
hybridlearningmodelforcustomerrepurchasebehavior,’’J.Retailing
Consum.Services,vol.59,Mar.2021,Art.no.102381. intelligenttutoringsystem,’’inProc.21stInt.Conf.Artif.Intell.Educ.,
[126] M. A. Rahim, M. Mushafiq, S. Khan, and Z. A. Arain, ‘‘RFM-based Ifrane,Morocco,Jul.2020,pp.140–146.
|            |          |     |          |                |     |                     |     | [146] B.Albreiki,N.Zaki,andH.Alashwal,‘‘Asystematicliteraturereview |     |     |     |     |     |
| ---------- | -------- | --- | -------- | -------------- | --- | ------------------- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- |
| repurchase | behavior | for | customer | classification |     | and segmentation,’’ | J.  |                                                                     |     |     |     |     |     |
ofStudent’performancepredictionusingmachinelearningtechniques,’’
RetailingConsum.Services,vol.61,Jul.2021,Art.no.102566.
Educ.Sci.,vol.11,no.9,p.552,Sep.2021.
[127] S.Hwang,J.Kim,E.Park,andS.J.Kwon,‘‘Whowillbeyournext
|     |     |     |     |     |     |     |     | [147] S.Plak,I.Cornelisz,M.Meeter,andC.vanKlaveren,‘‘Earlywarning |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- |
customer:Amachinelearningapproachtocustomerreturnvisitsinairline
|     |     |     |     |     |     |     |     | systems | for more effective | Student | counselling | in  | higher education: |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------------ | ------- | ----------- | --- | ----------------- |
services,’’J.Bus.Res.,vol.121,pp.121–126,Dec.2020.
EvidencefromaDutchfieldexperiment,’’HigherEduc.Quart.,vol.76,
[128] A. Amin, F. Al-Obeidat, B. Shah, A. Adnan, J. Loo, and S. Anwar, no.1,pp.131–152,Jan.2022.
‘‘Customerchurnpredictionintelecommunicationindustryusingdata
|     |     |     |     |     |     |     |     | [148] D. A. | Gutierrez-Pachas, | G.  | Garcia-Zanabria, | E.  | Cuadros-Vargas, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | --- | ---------------- | --- | --------------- |
certainty,’’J.Bus.Res.,vol.94,pp.290–301,Jan.2019.
G.Camara-Chavez,andE.Gomez-Nieto,‘‘Supportingdecision-making
[129] M.J.Sánchez-Franco,A.Navarro-García,andF.J.Rondán-Cataluña,‘‘A
processonhighereducationdropoutbyanalyzingacademic,socioeco-
naiveBayesstrategyforclassifyingcustomersatisfaction:Astudybased
nomic,andequityfactorsthroughmachinelearningandsurvivalanalysis
ononlinereviewsofhospitalityservices,’’J.Bus.Res.,vol.101,pp.499–
methodsintheLatinAmericancontext,’’Educ.Sci.,vol.13,no.2,p.154,
| 506,Aug.2019. |     |     |     |     |     |     |     | Feb.2023. |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
[130] J.P.Singh,S.Irani,N.P.Rana,Y.K.Dwivedi,S.Saumya,andP.K.Roy, [149] J.Figueroa-CañasandT.Sancho-Vinuesa,‘‘Earlypredictionofdropout
‘‘Predictingthe‘helpfulness’ofonlineconsumerreviews,’’J.Bus.Res.,
andfinalexamperformanceinanonlinestatisticscourse,’’IEEERevista
vol.70,pp.346–355,Aug.2016.
IberoamericanadeTecnologiasdelAprendizaje,vol.15,no.2,pp.86–94,
| [131] A. Costa, | J.  | Guerreiro, | S. Moro, | and | R. Henriques, | ‘‘Unfolding | the |     |     |     |     |     |     |
| --------------- | --- | ---------- | -------- | --- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
May2020.
| characteristics |     | of incentivized |     | online | reviews,’’ | J. Retailing | Consum. |                                                                     |     |     |     |     |     |
| --------------- | --- | --------------- | --- | ------ | ---------- | ------------ | ------- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- |
|                 |     |                 |     |        |            |              |         | [150] P.T.VonHippelandA.Hofflinger,‘‘Thedatarevolutioncomestohigher |     |     |     |     |     |
Services,vol.47,pp.272–281,Mar.2019. education:IdentifyingstudentsatriskofdropoutinChile,’’J.Higher
[132] A.Greenstein-MessicaandL.Rokach,‘‘Machinelearningandoperation Educ.PolicyManage.,vol.43,no.1,pp.2–23,Jan.2021.
research based method for promotion optimization of products with [151] G. Deeva, J. De Smedt, and J. De Weerdt, ‘‘Educational sequence
| no price | elasticity | history,’’ | Electron. |     | Commerce | Res. Appl., | vol. 40, |     |     |     |     |     |     |
| -------- | ---------- | ---------- | --------- | --- | -------- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
miningfordropoutpredictioninMOOCs:Modelbuilding,evaluation,
Mar.2020,Art.no.100914.
andbenchmarking,’’IEEETrans.Learn.Technol.,vol.15,no.6,pp.720–
[133] H.Kim,‘‘Doonlinesearchesinfluencesalesormerelypredictthem?The 735,Dec.2022.
caseofmotionpictures,’’Eur.J.Marketing,vol.55,no.2,pp.337–362, [152] L. Harris, J. Dargusch, K. Ames, and C. Bloomfield, ‘‘Catering
Jan.2021. for catering for, ‘very different kids’: Distance education teachers’
[134] S.H.-W.ChuahandJ.Yu,‘‘Thefutureofservice:Thepowerofemotion understandingsofandstrategiesforStudentengagement,’’Int.J.Incl.
in human–robot interaction,’’ J. Retailing Consum. Services, vol. 61, Educ.,vol.26,no.8,pp.848–864,2022.
Jul.2021,Art.no.102551.
|     |     |     |     |     |     |     |     | [153] J.Kodithuwakku,D.D.Arachchi,andJ.Rajasekera,‘‘Anemotionand |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
[135] T. Hennig-Thurau, A. Marchand, and P. Marx, ‘‘Can automated attentionrecognitionsystemtoclassifythelevelofengagementtoavideo
grouprecommendersystemshelpconsumersmakebetterchoices?’’J. conversationbyparticipantsinrealtimeusingmachinelearningmodels
Marketing,vol.76,no.5,pp.89–109,Sep.2012. andutilizinganeuralacceleratorchip,’’Algorithms,vol.15,no.5,p.150,
| [136] E.Pantano,C.Dennis,andM.DePietro,‘‘Shoppingcentersrevisited: |     |     |     |     |     |     |     | Apr.2022. |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
Theinterplaybetweenconsumers’spontaneousonlinecommunications [154] E.Acosta-Gonzaga,‘‘Theeffectsofself-esteemandacademicengage-
andretailplanning,’’J.RetailingConsum.Services,vol.61,Jul.2021, mentonuniversitystudents’performance,’’Behav.Sci.,vol.13,no.4,
| Art.no.102576. |     |     |     |     |     |     |     | p.348,2023. |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
[137] D.Panda,D.D.Chakladar,S. Rana,andM.N.Shamsudin,‘‘Spatial [155] M.U.UçarandE.Özdemir,‘‘RecognizingstudentsanddetectingStudent
attention-enhancedEEGanalysisforprofilingconsumerchoices,’’IEEE engagementwithreal-timeimageprocessing,’’Electronics,vol.11,no.9,
| Access,vol.12,pp.13477–13487,2024. |     |     |     |     |     |     |     | p.1500,2022. |     |     |     |     |               |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | ------------- |
| 128412                             |     |     |     |     |     |     |     |              |     |     |     |     | VOLUME13,2025 |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[156] X.Solé-Beteta,J.Navarro,B.Gajšek,A.Guadagni,andA.Zaballos, [176] M. I. Alipio, ‘‘Development of smart indoor workplace system using
‘‘Adata-drivenapproachtoquantifyandmeasureStudents’engagement decisiontreealgorithm,’’inProc.IEEEInt.Conf.InternetThingsIntell.
insynchronousvirtuallearningenvironments,’’Sensors,vol.22,no.9, Syst.(IoTaIS),Nov.2021,pp.196–202.
p.3294,Apr.2022. [177] A. Zenonos, A. Khan, G. Kalogridis, S. Vatsikas, T. Lewis, and
[157] K.Alhanaee,M.Alhammadi,N.Almenhali,andM.Shatnawi,‘‘Face M.Sooriyabandara, ‘‘HealthyOffice: Mood recognition at work using
recognitionsmartattendancesystemusingdeeptransferlearning,’’Proc. smartphonesandwearablesensors,’’inProc.IEEEInt.Conf.Pervasive
Comput.Sci.,vol.192,pp.4093–4102,Jan.2021. Comput.Commun.Workshops(PerComWorkshops),Mar.2016,pp.1–6.
[158] D.Sunaryono,J.Siswantoro,andR.Anggoro,‘‘AnAndroidbasedcourse [178] A. Choudhary, S. Mukherjee, B. Roy, I. Sengupta, K. Maji, and
attendancesystemusingfacerecognition,’’J.KingSaudUniv.Comput. S.Gupta,‘‘Optimizingemployeesatisfactionwithhealthandsafetyusing
Inf.Sci.,vol.33,no.3,pp.304–312,Mar.2021. computationalmodelsandmachinelearning,’’inProc.Int.Conf.Circuit,
[159] A. Bhattarai, S. Dhakal, and A. K. Timalsina, ‘‘Enhancing automatic Syst.Commun.(ICCSC),Jun.2024,pp.1–7.
attendancesystemusingfacerecognition,’’inProc.IEEEGlobalEng. [179] H.Hijry,S.MeesamRazaNaqvi,K.Javed,O.H.Albalawi,R.Olawoyin,
Educ.Conf.(EDUCON),Mar.2022,pp.1048–1054. C. Varnier, and N. Zerhouni, ‘‘Real time worker stress prediction in
[160] M.UtoandM.Okano,‘‘Learningautomatedessayscoringmodelsusing a smart factory assembly line,’’ IEEE Access, vol. 12, pp. 116238–
item-response-theory-basedscorestodecreaseeffectsofraterbiases,’’ 116249,2024.
IEEETrans.Learn.Technol.,vol.14,no.6,pp.763–776,Dec.2021. [180] K. S. Chandraprabha, A. N. Shwetha, M. Kavitha, and R. Sumathi,
‘‘Realtime-employeeemotiondetectionsystem(RtEED)usingmachine
[161] M.Uto,I.Aomi,E.Tsutsumi,andM.Ueno,‘‘Integrationofprediction
learning,’’inProc.3rdInt.Conf.Intell.Commun.Technol.VirtualMobile
scoresfromvariousautomatedessayscoringmodelsusingitemresponse
Netw.(ICICV),Feb.2021,pp.759–763.
theory,’’ IEEE Trans. Learn. Technol., vol. 16, no. 6, pp. 983–1000,
Jun.2023. [181] D. Mannapperuma and A. Kirupananada, ‘‘ADAM- anxiety detection
and management: A solution to manage anxiety at workplaces and
[162] Y. Wu, A. Henriksson, J. Nouri, M. Duneld, and X. Li, ‘‘Beyond
improveproductivity,’’inProc.IEEEInt.WomenEng.(WIE)Conf.Electr.
benchmarks:Spottingkeytopicalsentenceswhileimprovingautomated
Comput.Eng.(WIECON-ECE),Dec.2020,pp.243–246.
essayscoringperformancewithtopic-awareBERT,’’Electronics,vol.12,
no.1,p.150,Dec.2022. [182] T. D. Shukla, D. P. Giri, P. Rana, P. V. Krishna, T. Thulasimani, and
S.Vanisri,‘‘Predictingworkenvironmentandjobenvironmentamong
[163] Y.-H.Park,Y.-S.Choi,C.-Y.Park,andK.-J.Lee,‘‘EssayGAN:Essaydata
employees using transfer learning approach,’’ in Proc. 2nd Int. Conf.
augmentation based on generative adversarial networks for automated
Autom.,Comput.Renew.Syst.(ICACRS),Dec.2023,pp.771–776.
essayscoring,’’Appl.Sci.,vol.12,no.12,p.5803,Jun.2022.
[183] M.PageandD.Ashlock,‘‘Stressandproductivityperformanceinthe
[164] T. Firoozi, H. Mohammadi, and M. J. Gierl, ‘‘Using active learning
workforcemodelledwithbinarydecisionautomata,’’inProc.IEEEConf.
methods to strategically select essays for automated scoring,’’ Educ.
Comput.Intell.Bioinf.Comput.Biol.(CIBCB),Aug.2015,pp.1–8.
Meas.,IssuesPract.,vol.42,no.1,pp.34–43,Mar.2023.
[184] K.KalaivaniandS.Venkatachalam,‘‘Ananalysisontheproductivity
[165] C. Tejedor-García, D. Escudero-Mancebo, V. Cardeñoso-Payo, and
of employees through artificial intelligence,’’ in Proc. 7th Int. Conf.
C.González-Ferreras,‘‘Usingchallengestoenhancealearninggamefor
Electron.,Commun.Aerosp.Technol.(ICECA),Nov.2023,pp.1590–
pronunciationtrainingofEnglishasasecondlanguage,’’IEEEAccess,
1594.
vol.8,pp.74250–74266,2020.
[185] E.B.SantiagoandG.P.P.Gara,‘‘Amodelbasedpredictionofdesirable
[166] C. Tejedor-Garcia, D. Escudero-Mancebo, E. Camara-Arenas, applicantsthroughEmployee’sperceptionofretentionandperformance,’’
C.Gonzalez-Ferreras,andV.Cardenoso-Payo,‘‘Assessingpronunciation inProc.IEEE10thInt.Conf.Humanoid,Nanotechnol.,Inf.Technology,
improvementinstudentsofEnglishusingacontrolledcomputer-assisted Commun.Control,Environ.Manage.(HNICEM),Nov.2018,pp.1–6.
pronunciation tool,’’ IEEE Trans. Learn. Technol., vol. 13, no. 2,
[186] M.J.C.Samonte,Y.Wang,X.Tian,andQ.Wang,‘‘Grandchallenge
pp.269–282,Apr.2020.
ofimageprocessinginautomaticdetectionofvehiclesrunninginred
[167] Y.Getman,N.Phan,R.Al-Ghezi,E.Voskoboinik,M.Singh,T.Grósz, lights,’’Proc.SPIE,vol.13158,pp.53–63,May2024.
M.Kurimo,G.Salvi,T.Svendsen,S.Strömbergsson,A.Smolander,and
[187] Y.Jia,‘‘Pedestrianbehaviordetectionandtrafficviolationrecognition
S. Ylinen, ‘‘Developing an AI-assisted low-resource spoken language
basedonYOLOv5,’’inProc.4thInt.Conf.ImageProcess.Intell.Control
learningappforchildren,’’IEEEAccess,vol.11,pp.86025–86037,2023.
(IPIC),Aug.2024,p.97.
[168] S.S.Rautaray,S.Nayak,andM.Pandey,‘‘Amachinelearningbased
[188] A.Aboah,B.Wang,U.Bagci,andY.Adu-Gyamfi,‘‘Real-timemulti-
employee mental health analysis model,’’ in Proc. Int. Conf. Sustain.
classhelmetviolationdetectionusingfew-shotdatasamplingtechnique
Commun.Netw.Appl.(ICSCNA),Nov.2023,pp.1055–1059.
andYOLOv8,’’inProc.IEEE/CVFConf.Comput.Vis.PatternRecognit.
[169] R.Srikanteswara,P.Rithicka,Y.V.S.Kala,S.Rangaraj,andV.Devaiah, Workshops(CVPRW),Jun.2023,pp.5350–5358.
‘‘Machinelearning-basedstressdetectioninITemployees:Adata-driven [189] A. Goyal, D. Agarwal, A. Subramanian, C. V. Jawahar,
approachforworkplacewell-being,’’inProc.2ndInt.Conf.DataSci.Inf. R.K.Sarvadevabhatla,andR.Saluja,‘‘Detecting,trackingandcounting
Syst.(ICDSIS),May2024,pp.1–7. motorcycle rider traffic violations on unconstrained roads,’’ in Proc.
[170] V.Ch.,A.K.Dixit,K.Joshi,K.Pant,L.Thomas,andN.Beri,‘‘Predicting IEEE/CVFConf.Comput.Vis.PatternRecognit.Workshops(CVPRW),
employee mental health using artificial neural network,’’ in Proc. 3rd Jun.2022,pp.4302–4311.
Int.Conf.AdvanceComput.Innov.Technol.Eng.(ICACITE),May2023, [190] M.Bolsunovskaya,A.Leksashov,S.Shirokova,andV.Tsygan,‘‘Devel-
pp.1380–1383. opmentofaninformationsystemstructureforphoto-videorecordingof
[171] W.Lawanot,M.Inoue,T.Yokemura,P.Mongkolnam,andC.Nukoolkit, trafficviolations,’’inProc.E3SWebConf.,vol.244,Jan.2021,p.7007.
‘‘Dailystressandmoodrecognitionsystemusingdeeplearningandfuzzy [191] M.SaravananandG.K.Rajini,‘‘Comprehensivestudyonthedevelop-
clustering for promoting better well-being,’’ in Proc. IEEE Int. Conf. mentofanautomatichelmetviolatordetectionsystem(AHVDS)using
Consum.Electron.(ICCE),Jan.2019,pp.1–6. advancedmachinelearningtechniques,’’Comput.Electr.Eng.,vol.118,
[172] S.KrishnaandS.Sidharth,‘‘Analyzingemployeeattritionusingmachine Aug.2024,Art.no.109289.
learning:ThenewAIapproach,’’inProc.IEEE7thInt.Conf.Converg. [192] H.A.Abdelali,H.Derrouz,Y.Zennayi,R.O.H.Thami,andF.Bourzeix,
Technol.(I2CT),Apr.2022,pp.1–14. ‘‘Multiplehypothesisdetectionandtrackingusingdeeplearningforvideo
[173] R.JainandA.Nayyar,‘‘PredictingemployeeattritionusingXGBoost trafficsurveillance,’’IEEEAccess,vol.9,pp.164282–164291,2021.
machinelearningapproach,’’inProc.Int.Conf.Syst.Model.Advance- [193] D.Dede,M.AliSarsıl,A.Shaker,O.Altıntaş,andO.Ergen,‘‘Next-
mentRes.Trends(SMART),Nov.2018,pp.113–120. gen traffic surveillance: AI-assisted mobile traffic violation detection
[174] S.S.Patil,S.H.Patil,A.M.Pawar,P.KumarPandey,S.Sharma,and system,’’2023,arXiv:2311.16179.
M.S.Bewoor,‘‘EmployeechurnwalkthroughusingKNN,’’inProc.2nd [194] W.Safat,S.Asghar,andS.A.Gillani,‘‘Empiricalanalysisforcrime
AsianConf.Innov.Technol.(ASIANCON),Aug.2022,pp.1–4. prediction and forecasting using machine learning and deep learning
[175] S. Krishna, Shobhitanshu, and D. Borah, ‘‘Machine learning for techniques,’’IEEEAccess,vol.9,pp.70080–70094,2021.
ensuringsustainabledevelopment:Predictingemployeeattritioninthe [195] E.Cesario,P.Lindia,andA.Vinci,‘‘Multi-densitycrimepredictor:An
workplace,’’inProc.Int.Conf.Adv.Comput.Technol.Appl.(ICACTA), approachtoforecastcriminalactivitiesinmulti-densitycrimehotspots,’’
Oct.2023,pp.1–7. J.BigData,vol.11,no.1,p.75,May2024.
VOLUME13,2025 128413

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[196] R.BasakUtsha,M.NoorAlif,Y.Rayhan,T.Hashem,andM.Eunus [218] D. Buil-Gil, Y. Zeng, and S. Kemp, ‘‘Offline crime bounces back to
Ali, ‘‘Deep learning based crime prediction models: Experiments and pre-COVIDlevels,cyberstayshigh:Interruptedtime-seriesanalysisin
analysis,’’2024,arXiv:2407.19324. northernIreland,’’CrimeSci.,vol.10,no.1,pp.1–16,Nov.2021.
[197] N.Tasnim,I.T.Imam,andM.M.A.Hashem,‘‘Anovelmulti-module [219] V.Rotaru,Y.Huang,T.Li,J.Evans,andI.Chattopadhyay,‘‘Event-level
approach to predict crime based on multivariate spatio-temporal data predictionofurbancrimerevealsasignatureofenforcementbiasinU.S.
using attention and sequential fusion model,’’ IEEE Access, vol. 10, cities,’’NatureHumanBehaviour,vol.6,no.8,pp.1056–1068,Jun.2022,
pp.48009–48030,2022. doi:10.1038/s41562-022-01372-0.
[198] A. Rummens, T. Snaphaan, N. Van de Weghe, D. Van den Poel, [220] M. Yang, Z. Chen, M. Zhou, X. Liang, and Z. Bai, ‘‘The impact of
L.J.R.Pauwels, and W. Hardyns, ‘‘Do mobile phone data provide a COVID-19oncrime:AspatialtemporalanalysisinChicago,’’ISPRSInt.
betterdenominatorincrimeratesandimprovespatiotemporalpredictions J.Geo-Information,vol.10,no.3,p.152,Mar.2021.
ofcrime?’’ISPRSInt.J.Geo-Inf.,vol.10,no.6,p.369,May2021. [221] D.Kim,Y.Kan,Y.Aum,W.Lee,andG.Yi,‘‘Hotspots-basedpatrol
[199] R.PrietoCuriel,S.Cresci,C.I.Muntean,andS.R.Bishop,‘‘Crime
routeoptimizationalgorithmforsmartpolicing,’’Heliyon,vol.9,no.10,
anditsfearinsocialmedia,’’PalgraveCommun.,vol.6,no.1,pp.1–12, Oct.2023,Art.no.e20931.
Apr.2020. [222] J.Yang,M.N.Nguyen,P.P.San,X.Li,andS.Krishnaswamy,‘‘Deep
convolutional neural networks on multichannel time series for human
[200] T.Chen,K.Bowers,andT.Cheng,‘‘Applyingdynamichumanactivity
activityrecognition,’’inProc.24thInt.JointConf.Artif.Intell.,Jul.2015,
todisentanglepropertycrimepatternsinLondonduringthepandemic:
pp.3995–4001.
Anempiricalanalysisusinggeo-taggedbigdata,’’ISPRSInt.J.Geo-Inf.,
[223] B. Zhou, J. Yang, and Q. Li, ‘‘Smartphone-based activity recognition
vol.12,no.12,p.488,Dec.2023.
forindoorlocalizationusingaconvolutionalneuralnetwork,’’Sensors,
[201] L. Hahn, ‘‘Forecasting seasonal criminality using SARIMA: An
vol.19,no.3,p.621,Feb.2019.
application to monthly aggravated assaults in California,’’ 2023,
[224] Y. Tang, Z. Wang, J. Lu, J. Feng, and J. Zhou, ‘‘Multi-stream deep
arXiv:2306.03053.
neuralnetworksforRGB-Degocentricactionrecognition,’’IEEETrans.
[202] H.M.AdachiandT.Nakaya,‘‘Analysisoftheriskoftheftfromvehicle
CircuitsSyst.VideoTechnol.,vol.29,no.10,pp.3001–3015,Oct.2019.
crimeinkyoto,Japanusingenvironmentalindicatorsofstreetscapes,’’
[225] L.Pei,S.Xia,L.Chu,F.Xiao,Q.Wu,W.Yu,andR.Qiu,‘‘MARS:
CrimeSci.,vol.11,no.1,p.13,Nov.2022.
Mixedvirtualandrealwearablesensorsforhumanactivityrecognition
[203] O.Kovalchuk,R.Shevchuk,andS.Banakh,‘‘Cryptocurrencycrimerisks withmultidomaindeeplearningmodel,’’IEEEInternetThingsJ.,vol.8,
modeling: Environment, e-commerce, and cybersecurity issue,’’ IEEE no.11,pp.9383–9396,Jun.2021.
Access,vol.12,pp.50673–50688,2024.
[226] F.Wang,J.Feng,Y.Zhao,X.Zhang,S.Zhang,andJ.Han,‘‘Jointactivity
[204] B. Moews, J. R. Argueta, and A. Gieschen, ‘‘Filaments of crime: recognitionandindoorlocalizationwithWiFifingerprints,’’IEEEAccess,
Informing policing via thresholded ridge estimation,’’ Decis. Support vol.7,pp.80058–80068,2019.
Syst.,vol.144,May2021,Art.no.113518. [227] C. A. Ronao and S.-B. Cho, ‘‘Human activity recognition with
[205] N.Shiode,S.Shiode,H.Nishi,andK.Hino,‘‘Seasonalcharacteristics smartphonesensorsusingdeeplearningneuralnetworks,’’ExpertSyst.
ofcrime:Anempiricalinvestigationofthetemporalfluctuationofthe Appl.,vol.59,pp.235–244,Oct.2016.
differenttypesofcrimeinLondon,’’Comput.UrbanSci.,vol.3,no.1, [228] V. Radu and M. Henne, ‘‘Vision2Sensor: Knowledge transfer across
p.19,May2023. sensingmodalitiesforhumanactivityrecognition,’’Proc.ACMInteract.,
[206] J.v.Dijk,P.Nieuwbeerta,andJ.J.Larsen,‘‘Globalcrimepatterns:An Mobile,WearableUbiquitousTechnol.,vol.3,no.3,pp.1–21,Sep.2019.
analysisofsurveydatafrom166countriesaroundtheworld,2006–2019,’’ [229] T. Nagarajan, Y. Li, C. Feichtenhofer, and K. Grauman, ‘‘Ego-topo:
J.QuantumCriminology,vol.38,no.4,pp.793–827,Mar.2021. Environment affordances from egocentric video,’’ in Proc. IEEE/CVF
[207] A. Tundis, H. Kaleem, and M. Mühlhäuser, ‘‘Detecting and tracking Conf.Comput.Vis.PatternRecognit.(CVPR),Jun.2020,pp.160–169.
criminals in the real world through an IoT-based system,’’ Sensors, [230] V. Radu, C. Tong, S. Bhattacharya, N. D. Lane, C. Mascolo,
vol.20,no.13,p.3795,Jul.2020. M.K.Marina,andF.Kawsar,‘‘Multimodaldeeplearningforactivityand
[208] H.-B.Kim,N.Choi,H.-J.Kwon,andH.Kim,‘‘Surveillancesystemfor contextrecognition,’’Proc.ACMInteract.,Mobile,WearableUbiquitous
real-timehigh-precisionrecognitionofcriminalfacesfromwildvideos,’’ Technol.,vol.1,no.4,pp.1–27,Jan.2018.
IEEEAccess,vol.11,pp.56066–56082,2023. [231] X. Wang, Y. Wu, L. Zhu, and Y. Yang, ‘‘Symbiotic attention with
[209] Q.Yang,A.Wu,andW.-S.Zheng,‘‘Personre-identificationbycontour privilegedinformationforego-centricactionrecognition,’’inProc.AAAI,
sketch under moderate clothing change,’’ IEEE Trans. Pattern Anal. 2020,pp.1–12.
Mach.Intell.,vol.43,no.6,pp.2029–2046,Jun.2021. [232] M. S. Seyfioglu, A. M. Özbayoglu, and S. Z. Gürbüz, ‘‘Deep convo-
lutionalautoencoderforradar-basedclassificationofsimilaraidedand
[210] I.MugariandE.E.Obioha,‘‘Predictivepolicingandcrimecontrolin
unaidedhumanactivities,’’IEEETrans.Aerosp.Electron.Syst.,vol.54,
theUnitedStatesofAmericaandEurope:Trendsinadecadeofresearch
no.4,pp.1709–1723,Aug.2018.
andthefutureofpredictivepolicing,’’SocialSci.,vol.10,no.6,p.234,
[233] H.Ma,W.Li,X.Zhang,S.Gao,andS.Lu,‘‘AttnSense:Multi-level
Jun.2021.
attention mechanism for multimodal human activity recognition,’’ in
[211] I. Shafi, S. Din, Z. Hussain, I. Ashraf, and G. S. Choi, ‘‘Adaptable
Proc.28thInt.JointConf.Artif.Intell.,Aug.2019,pp.3109–3115.
reduced-complexityapproachbasedonstatevectormachineforiden-
[234] L.Zhang,J.Yu,Z.Gao,andQ.Ni,‘‘Amulti-channelhybriddeeplearning
tification of criminal activists on social media,’’ IEEE Access, vol. 9,
frameworkformulti-sensorfusionenabledhumanactivityrecognition,’’
pp.95456–95468,2021.
AlexandriaEng.J.,vol.91,pp.472–485,Mar.2024.
[212] S. Khan Rumi, K. K. Qin, and F. D. Salim, ‘‘Multi-officer routing
[235] C.Han,L.Zhang,Y.Tang,W.Huang,F.Min,andJ.He,‘‘Humanactivity
forpatrollinghighriskareasjointlylearnedfromcheck-ins,crimeand
recognition using wearable sensors by heterogeneous convolutional
incidentresponsedata,’’2020,arXiv:2008.00113.
neuralnetworks,’’ExpertSyst.Appl.,vol.198,Jul.2022,Art.no.116764.
[213] M.Repasky,H.Wang,andY.Xie,‘‘Multi-agentreinforcementlearning
[236] Y.Tang,L.Zhang,F.Min,andJ.He,‘‘Multiscaledeepfeaturelearning
forjointpolicepatrolanddispatch,’’2024,arXiv:2409.02246.
forhumanactivityrecognitionusingwearablesensors,’’IEEETrans.Ind.
[214] R.Katole,D.Mallya,L.Vachhani,andA.Sinha,‘‘Balancingpriorities Electron.,vol.70,no.2,pp.2106–2116,Feb.2023.
inpatrollingwithrabbitwalks,’’2023,arXiv:2312.16564. [237] A.MuradandJ.-Y.Pyun,‘‘Deeprecurrentneuralnetworksforhuman
[215] J.Yang,Z.Ding,andL.Wang,‘‘Theprogrammingmodelofair-ground activityrecognition,’’Sensors,vol.17,no.11,p.2556,Nov.2017.
cooperative patrol between multi-UAV and police car,’’ IEEE Access, [238] S. Yousefi, H. Narui, S. Dayal, S. Ermon, and S. Valaee, ‘‘A survey
vol.9,pp.134503–134517,2021. onbehaviorrecognitionusingWiFichannelstateinformation,’’IEEE
[216] K. Panetta, L. Kezebou, V. Oludare, J. Intriligator, and S. Agaian, Commun.Mag.,vol.55,no.10,pp.98–104,Oct.2017.
‘‘Artificial intelligence for text-based vehicle search, recognition, and [239] M. Inoue, S. Inoue, and T. Nishida, ‘‘Deep recurrent neural network
continuouslocalizationintrafficvideos,’’AI,vol.2,no.4,pp.684–704, formobilehumanactivityrecognitionwithhighthroughput,’’Artif.Life
Dec.2021. Robot.,vol.23,no.2,pp.173–185,Jun.2018.
[217] X.LiuandJ.Liu,‘‘Malicioustrafficdetectioncombineddeepneural [240] F.Gu,K.Khoshelham,S.Valaee,J.Shang,andR.Zhang,‘‘Locomotion
networkwithhierarchicalattentionmechanism,’’Sci.Rep.,vol.11,no.1, activity recognition using stacked denoising autoencoders,’’ IEEE
p.12363,Jun.2021. InternetThingsJ.,vol.5,no.3,pp.2085–2093,Jun.2018.
128414 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[241] K.Chen,L.Yao,D.Zhang,B.Guo,andZ.Yu,‘‘Multi-agentattentional [263] D.Zhang,Z.Liao,W.Xie,X.Wu,H.Xie,J.Xiao,andL.Jiang,‘‘Fine-
activityrecognition,’’inProc.Twenty-EighthInt.JointConf.Artif.Intell., grainedandreal-timegesturerecognitionbyusingIMUsensors,’’IEEE
Aug.2019,pp.1344–1350. Trans.MobileComput.,vol.22,no.4,pp.2177–2189,Apr.2023,doi:
[242] I.U.Khan,S.Afzal,andJ.W.Lee,‘‘Humanactivityrecognitionvia 10.1109/TMC.2021.3120475.
hybrid deep learning based model,’’ Sensors, vol. 22, no. 1, p. 323, [264] S.Wang,B.Liu,Y.-L.Wang,Y.Hu,J.Liu,X.-D.He,J.Yuan,andQ.Wu,
Jan.2022. ‘‘Machinelearning-basedhumanmotionrecognitionviawearableplastic
[243] Y.GuanandT.Plötz,‘‘EnsemblesofdeepLSTMlearnersforactivity fibersensingsystem,’’IEEEInternetThingsJ.,vol.10,no.20,pp.17893–
recognitionusingwearables,’’Proc.ACMInteract.,Mobile,Wearable 17904,Oct.2023,doi:10.1109/JIOT.2023.3277829.
UbiquitousTechnol.,vol.1,no.2,pp.1–28,Jun.2017. [265] Z.Wang,J.Wang,N.Ge,andJ.Lu,‘‘HiMoReNet:Ahierarchicalmodel
[244] H. Gammulle, S. Denman, S. Sridharan, and C. Fookes, ‘‘Multi-level for human motion refinement,’’ IEEE Signal Process. Lett., vol. 30,
sequence GAN for group activity recognition,’’ in Proc. Asian Conf. pp.868–872,2023,doi:10.1109/LSP.2023.3295756.
Comput.Vis.,Jan.2019,pp.331–346. [266] Z. Huang, Y. Qin, X. Lin, T. Liu, Z. Feng, and Y. Liu, ‘‘Motion-
[245] T. R. Mim, M. Amatullah, S. Afreen, M. A. Yousuf, S. Uddin, drivenspatialandtemporaladaptivehigh-resolutiongraphconvolutional
S.A.Alyami,andM.A.Moni,‘‘GRU-INC:Aninception-attentionbased networksforskeleton-basedactionrecognition,’’IEEETrans.Circuits
approachusingGRUforhumanactivityrecognition,’’ExpertSyst.Appl., Syst. Video Technol., vol. 33, no. 4, pp. 1868–1883, Apr. 2023, doi:
vol.216,2023,Art.no.119419. 10.1109/TCSVT.2022.3217763.
[246] Y.A.Andrade-Ambriz,S.Ledesma,M.-A.Ibarra-Manzano,M.I.Oros- [267] X.Sun,Y.Liu,andH.Niu,‘‘Continuousgesturerecognitionandforce
Flores, and D.-L. Almanza-Ojeda, ‘‘Human activity recognition using estimation using sEMG signal,’’ IEEE Access, vol. 11, pp. 118024–
temporalconvolutionalneuralnetworkarchitecture,’’ExpertSyst.Appl., 118036,2023,doi:10.1109/ACCESS.2023.3323586.
vol.191,Dec.2021,Art.no.116287. [268] I. Lamaakal, I. Ouahbi, K. El Makkaoui, Y. Maleh, P. Pławiak, and
[247] X.Li,Y.Zhang,J.Zhang,Y.Chen,H.Li,I.Marsic,andR.S.Burd, F.Alblehai,‘‘ATinyDLmodelforgesture-basedairhandwritingArabic
‘‘Region-based activity recognition using conditional GAN,’’ in Proc. numbersandsimpleArabiclettersrecognition,’’IEEEAccess,vol.12,
25thACMInt.Conf.Multimedia,Oct.2017,pp.1059–1067. pp.76589–76605,2024,doi:10.1109/ACCESS.2024.3406631.
[248] L. Wang, ‘‘Recognition of human activities using continuous autoen- [269] T. Srilakshmi, H. Reddy, Y. Potluri, L. R. Burra, M. V. Thota, and
coderswithwearablesensors,’’Sensors,vol.16,no.2,p.189,Feb.2016. R.Gundimeda, ‘‘Automated driver drowsiness detection system using
[249] M.HasanandA.K.Roy-Chowdhury,‘‘Acontinuouslearningframework computer vision and machine learning,’’ in Proc. Int. Conf. Sustain.
foractivityrecognitionusingdeephybridfeaturemodels,’’IEEETrans. Comput.DataCommun.Syst.(ICSCDS),Mar.2023,pp.615–621.
Multimedia,vol.17,no.11,pp.1909–1922,Nov.2015.
[270] R. D. Burri, L. A. Kusampudi, S. M. Sharfuddin, and N. V. S. Sai,
[250] J.Wang,X.Zhang,Q.Gao,H.Yue,andH.Wang,‘‘Device-freewireless ‘‘Enhancingroadsafetywithreal-timedriverdrowsinessdetectionusing
localizationandactivityrecognition:Adeeplearningapproach,’’IEEE machinelearning,’’inProc.IEEEInt.Conf.Contemp.Comput.Commun.
Trans.Veh.Technol.,vol.66,no.7,pp.6258–6267,Jul.2017. (InC4),Mar.2024,pp.1–6.
[251] B. Almaslukh, A. M. Artoli, and J. Al-Muhtadi, ‘‘An effective deep [271] M.A.Khan,T.Nawaz,U.S.Khan,A.Hamza,andN.Rashid,‘‘IoT-
autoencoder approach for online smartphone-based human activity basednon-intrusiveautomateddriverdrowsinessmonitoringframework
recognition,’’Int.J.Comput.Sci.Netw.Secur.,vol.17,no.4,pp.160– forlogisticsandpublictransportapplicationstoenhanceroadsafety,’’
165,Apr.2017. IEEEAccess,vol.11,pp.14385–14397,2023.
[252] S.BhattacharyaandN.D.Lane,‘‘Fromsmarttodeep:Robustactivity
[272] H.A.Madni,A.Raza,R.Sehar,N.Thalji,andL.Abualigah,‘‘Novel
recognitiononsmartwatchesusingdeeplearning,’’inProc.IEEEInt.
transfer learning approach for driver drowsiness detection using eye
Conf. Pervasive Comput. Commun. Workshops (PerCom Workshops),
movementbehavior,’’IEEEAccess,vol.12,pp.64765–64778,2024.
Mar.2016,pp.1–6.
[273] Bhumika,D.Das,andS.K.Das,‘‘RsSafe:Personalizeddriverbehavior
[253] M.Qi,J.Qin,A.Li,Y.Wang,J.Luo,andL.V.Gool,‘‘StagNet:An
prediction for safe driving,’’ in Proc. Int. Joint Conf. Neural Netw.
attentivesemanticRNNforgroupactivityrecognition,’’inProc.Eur.
(IJCNN),Jul.2022,pp.1–8.
Conf.Comput.Vis.(ECCV),Jan.2018,pp.104–120.
[274] P. Sihakhom, S. Sulistyo, and I. W. Mustika, ‘‘Classification Driver’s
[254] M.EdelandE.Köppe,‘‘Binarized-BLSTM-RNNbasedhumanactivity
behaviour using supervised algorithm,’’ in Proc. 6th Int. Conf. Sci.
recognition,’’ in Proc. Int. Conf. Indoor Positioning Indoor Navigat.
Technol.(ICST),vol.1,Sep.2020,pp.1–6.
(IPIN),Oct.2016,pp.1–7.
[275] C. Zhang, Y. Lu, M. Feng, and M. Wu, ‘‘Trucker behavior security
[255] A. M. Helmi, M. A. A. Al-Qaness, A. Dahou, and M. Abd Elaziz,
surveillancebasedonhumanparsing,’’IEEEAccess,vol.7,pp.97526–
‘‘Human activity recognition using marine predators algorithm with
97535,2019.
deep learning,’’ Future Gener. Comput. Syst., vol. 142, pp. 340–350,
May2023. [276] A.AbouOuf,I.Sobh,M.Nasser,O.Alsaqa,O.Elezaby,andJ.F.W.Zaki,
‘‘Multimodelsystemfordriverdistractiondetectionandelimination,’’
[256] G.Khodabandelou,H.Moon,Y.Amirat,andS.Mohammed,‘‘Afuzzy
IEEEAccess,vol.10,pp.72458–72469,2022.
convolutionalattention-basedGRUnetworkforhumanactivityrecogni-
tion,’’Eng.Appl.Artif.Intell.,vol.118,Feb.2023,Art.no.105702. [277] D. Dinesh, ‘‘A novel multi-model machine learning approach to real-
timeroadaccidentpredictionanddrivingbehavioranalysis,’’inProc.
[257] N.Dua,S.N.Singh,V.B.Semwal,andS.K.Challa,‘‘Inceptioninspired
CNN-GRUhybridnetworkforhumanactivityrecognition,’’Multimedia
Int.Symp.Comput.Sci.Intell.Controls(ISCSIC),Nov.2021,pp.67–72.
ToolsAppl.,vol.82,no.4,pp.5369–5403,Feb.2023. [278] H.Zhang,L.Zhang,Y.Liu,andL.Zhang,‘‘Understandingtravelmode
[258] A.Sarkar,S.K.S.Hossain,andR.Sarkar,‘‘Humanactivityrecognition choicebehavior:Influencingfactorsanalysisandpredictionwithmachine
from sensor data using spatial attention-aided CNN with genetic learningmethod,’’Sustainability,vol.15,no.14,p.11414,Jul.2023.
algorithm,’’ Neural Comput. Appl., vol. 35, no. 7, pp. 5165–5191, [279] Q.Chen,D.Li,J.Sun,Z.Luo,andD.Li,‘‘Detectingpatternchangesin
Mar.2023. individualtravelbehaviorbasedonaBayesianmethod,’’IEEEAccess,
[259] B. Z. Tan, M. K. Law, and B. Marlin, ‘‘Self-supervised learning for vol.12,pp.25346–25358,2024.
humanactivityrecognitionusing700,000person-daysofwearabledata,’’ [280] J. Díaz-Ramírez, J. A. Estrada-García, and J. Figueroa-Sayago, ‘‘Pre-
in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), dictingtransportmodechoicepreferencesinauniversitydistrictwith
Jun.2022,pp.11150–11160. decisiontree-basedmodels,’’CityEnviron.Interact.,vol.20,Dec.2023,
[260] S.Huan,Z.Wang,X.Wang,L.Wu,X.Yang,H.Huang,andG.E.Dai, Art.no.100118.
‘‘Alightweighthybridvisiontransformernetworkforradar-basedhuman [281] B. Etaati, A. Jahangiri, G. Fernandez, M.-H. Tsou, and S. Ghanipoor
activityrecognition,’’Sci.Rep.,vol.13,no.1,Oct.2023,Art.no.17996. Machiani, ‘‘Understanding active transportation to school behavior in
[261] I.D.Luptáková,M.Kubovčík,andJ.Pospíchal,‘‘Wearablesensor-based socioeconomicallydisadvantagedcommunities:Amachinelearningand
humanactivityrecognitionwithtransformermodel,’’Sensors,vol.22, SHAPanalysisapproach,’’Sustainability,vol.16,no.1,p.48,Dec.2023.
no.5,p.1911,Mar.2022. [282] R. Buijs, T. Koch, and E. Dugundji, ‘‘Using neural nets to predict
[262] A. Snoun, T. Bouchrika, and O. Jemai, ‘‘Deep-learning-based human transportation mode choice: Amsterdam network change analysis,’’ J.
activityrecognitionforAlzheimer’spatients’dailylifeactivitiesassis- Ambient Intell. Humanized Comput., vol. 12, no. 1, pp. 121–135,
tance,’’NeuralComput.Appl.,vol.35,no.2,pp.1777–1802,Jan.2023. Jan.2021.
VOLUME13,2025 128415

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[283] A.R.MussahandY.Adu-Gyamfi,‘‘Machinelearningframeworkfor [303] X.Dong,B.Dang,H.Zang,S.Li,andD.Ma,‘‘Thepredictiontrendof
real-timeassessmentoftrafficsafetyutilizingconnectedvehicledata,’’ enterprisefinancialriskbasedonmachinelearningARIMAmodel,’’J.
Sustainability,vol.14,no.22,p.15348,Nov.2022. TheoryPract.Eng.Sci.,vol.4,no.1,pp.65–71,2024.
[284] H.Sawandi,A.Jayasinghe,andG.Retscher,‘‘Real-timetrackingdataand [304] T.ZhangandY.Du,‘‘Researchonusercreditscoremodelbasedonfusion
machinelearningapproachesformappingpedestrianwalkingbehavior: neuralnetwork,’’inProc.IEEE5thAdv.Inf.Technol.,Electron.Autom.
Acasestudyattheuniversityofmoratuwa,’’Sensors,vol.24,no.12, ControlConf.(IAEAC),Mar.2021,pp.1391–1395.
p.3822,Jun.2024. [305] Q. Li, ‘‘Research on bank credit risk assessment based on BP neural
[285] Y. Zheng, S. Wang, and J. Zhao, ‘‘Equality of opportunity in travel network,’’inProc.2ndInt.Conf.3DImmersion,Interact.Multi-sensory
behavior prediction with deep neural networks and discrete choice Experiences(ICDIIME),Jun.2023,pp.322–326.
models,’’ Transp. Res. C, Emerg. Technol., vol. 132, Nov. 2021, [306] K.B.AddiandN.Souissi,‘‘Anontology-basedmodelforcreditscoring
Art.no.103410. knowledgeinmicrofinance:Towardsabetterdecisionmaking,’’inProc.
[286] R.KumarandA.Jain,‘‘Drivingbehavioranalysisandclassificationby IEEE10thInt.Conf.Intell.Syst.(IS),Aug.2020,pp.380–385.
vehicle OBD data using machine learning,’’J. Supercomput., vol. 79, [307] X.ZhangandY.Zhang,‘‘Riskassessmentoffinancialloanbasedon
no.16,pp.18800–18819,Nov.2023. fuzzy cluster analysis,’’ in Proc. 14th Int. Conf. Measuring Technol.
[287] S.Abbas,M.O.Malik,A.R.Javed,andS.-P.Hong,‘‘Naturalisticdriving MechatronicsAutom.(ICMTMA),Jan.2022,pp.685–690.
data-basedanomalousdrivingbehaviordetectionusinghypertuneddeep
[308] N.Boustani,A.Emrouznejad,R.Gholami,O.Despic,andA.Ioannou,
autoencoders,’’Electronics,vol.12,no.9,p.2072,Apr.2023.
‘‘Improvingthepredictiveaccuracyofthecross-sellingofconsumerloans
[288] N.O.Khanfar,H.I.Ashqar,M.Elhenawy,Q.Hussain,A.Hasasneh,and usingdeeplearningnetworks,’’Ann.OperationsRes.,vol.339,nos.1–2,
W.K.M.Alhajyaseen,‘‘Applicationofunsupervisedmachinelearning pp.613–630,Aug.2024.
classificationfortheanalysisofdriverbehaviorinworkzonesinthestate
[309] G.J.SawaleandM.K.Rawat,‘‘Stockmarketpredictionusingsentiment
ofQatar,’’Sustainability,vol.14,no.22,p.15184,Nov.2022.
analysisandmachinelearningapproach,’’inProc.4thInt.Conf.Smart
[289] Z. Jiang, L. Zhang, L. Zhang, and B. Wen, ‘‘Investor sentiment and Syst.InventiveTechnol.(ICSSIT),Jan.2022,pp.1–6.
machine learning: Predicting the price of China’s crude oil futures
[310] T.KishoreandJ.Praveenchandar,‘‘Aneffectivestockmarketprediction
market,’’Energy,vol.247,May2022,Art.no.123471.
usinganadvancedmachinelearningalgorithmandemotionalanalysis,’’
[290] I.Lamaakal,K.E.Makkaoui,I.Ouahbi,andY.Maleh,‘‘ATinyMLmodel inProc.3rdInt.Conf.Appl.Artif.Intell.Comput.(ICAAIC),Jun.2024,
for gesture-based air handwriting Arabic numbers recognition,’’ Proc. pp.493–498.
Comput.Sci.,vol.236,pp.589–596,Jan.2024.
[311] E. Di Minin, C. Fink, A. Hausmann, J. Kremer, and R. Kulkarni,
[291] N.Jing,Z.Wu,andH.Wang,‘‘Ahybridmodelintegratingdeeplearning
‘‘Howtoaddressdataprivacyconcernswhenusingsocialmediadatain
withinvestorsentimentanalysisforstockpriceprediction,’’ExpertSyst.
conservationscience,’’ConservationBiol.,vol.35,no.2,pp.437–446,
Appl.,vol.178,Sep.2021,Art.no.115019.
Apr.2021.
[292] I.Lamaakal,Y.Maleh,I.Ouahbi,K.E.Makkaoui,andA.A.A.El-
[312] A. Khanan, S. Abdullah, A. H. H. M. Mohamed, A. Mehmood, and
Latif,‘‘Adeeplearning-poweredTinyMLmodelforgesture-basedair
K.A.Z.Ariffin,‘‘Bigdatasecurityandprivacyconcerns:Areview,’’
handwritingsimpleArabiclettersrecognition,’’inProc.Int.Conf.Digit.
inProc.1stAmer.Univ.EmiratesInt.Res.Conf.SmartTechnol.Innov.
Technol.Appl.Cham,Switzerland:Springer,Jan.2024,pp.32–42.
Sustain.Future,Jan.2019,pp.55–61.
[293] S. Deng, Q. Luo, Y. Zhu, H. Ning, Y. Yu, Y. Gao, Q. Shen, and T.
[313] T. Poongodi, R. Krishnamurthi, R. Indrakumari, P. Suresh, and
Shimada,‘‘Multi-sentimentfusionforstockpricecrashriskprediction
B.Balusamy,‘‘WearabledevicesandIoT,’’inAHandbookofInternet
using an interpretable ensemble learning method,’’ Eng. Appl. Artif.
ofThingsinBiomedicalandCyberPhysicalSystem.Cham,Switzerland:
Intell.,vol.135,Sep.2024,Art.no.108842.
Springer,2019,pp.245–273.
[294] S. Deng, Y. Zhu, Y. Yu, and X. Huang, ‘‘An integrated approach of
[314] J.Wan,M.A.A.H.Al-Awlaqi,M.Li,M.O’Grady,X.Gu,J.Wang,
ensemble learning methods for stock index prediction using investor
andN.Cao,‘‘WearableIoTenabledreal-timehealthmonitoringsystem,’’
sentiments,’’ExpertSyst.Appl.,vol.238,Mar.2024,Art.no.121710.
EURASIP J. Wireless Commun. Netw., vol. 2018, no. 1, pp. 1–10,
[295] H.Bourezk,A.Raji,N.Acha,andH.Barka,‘‘AnalyzingMoroccanstock
Dec.2018.
marketusingmachinelearningandsentimentanalysis,’’inProc.1stInt.
[315] S.Murthy,A.AbuBakar,F.AbdulRahim,andR.Ramli,‘‘Acomparative
Conf.Innov.Res.Appl.Sci.,Eng.Technol.(IRASET),Apr.2020,pp.1–5.
studyofdataanonymizationtechniques,’’inProc.IEEE5thInt.Conf.
[296] S.K.Bharti,P.Tratiya,andR.K.Gupta,‘‘Stockmarketpriceprediction
BigDataSecur.Cloud(BigDataSecurity)Int.Conf.HighPerform.Smart
throughnewssentimentanalysis&ensemblelearning,’’inProc.IEEE
Comput.,(HPSC)IEEEInt.Conf.Intell.DataSecur.(IDS),May2019,
2ndInt.Symp.Sustain.Energy,SignalProcess.CyberSecur.(iSSSC),
pp.306–309.
Dec.2022,pp.1–5.
[316] A.MajeedandS.Lee,‘‘Anonymizationtechniquesforprivacypreserving
[297] W.S.Walusala,R.Rimiru,andC.Otieno,‘‘Ahybridmachinelearning
data publishing: A comprehensive survey,’’ IEEE Access, vol. 9,
approachforcreditscoringusingPCAandLR,’’Int.J.Comput.(IJC),
pp.8512–8545,2021.
vol.27,no.1,pp.84–102,2017.
[317] I.H.Elifoglu,I.Abel,andÖ.Taşseven,‘‘Minimizinginsiderthreatrisk
[298] R.Ramakrishnan,P.Rohella,S.Mimani,N.Jiwani,andJ.Logeshwaran,
withbehavioralmonitoring,’’Rev.Bus.,vol.38,no.2,p.61,Jun.2018.
‘‘Employing AI and ML in risk assessment for lending for assessing
creditworthiness,’’inProc.2ndInt.Conf.DisruptiveTechnol.(ICDT), [318] K.DhanushkodiandS.Thejas,‘‘AIenabledthreatdetection:Leveraging
artificialintelligenceforadvancedsecurityandcyberthreatmitigation,’’
Mar.2024,pp.561–566.
IEEEAccess,vol.12,pp.173127–173136,2024.
[299] C.Fang,T.Bu,andF.Fang,‘‘Researchoncredit-riskmodelsviamachine-
learningalgorithmsandlogisticregressionforpredictingCBAconsumer [319] R. A. Alsharida, B. A. S. Al-Rimy, M. Al-Emran, and A. Zainal,
behaviour,’’inProc.Int.Conf.Comput.,Inf.Process.Adv.Educ.(CIPAE), ‘‘A systematic review of multi perspectives on human cybersecurity
Aug.2023,pp.344–350. behavior,’’Technol.Soc.,vol.73,May2023,Art.no.102258.
[300] D. Balakrishnan, P. A. Kumar, A. J. Krishna, A. Kamalesh, [320] C.Wang,Y.Zheng,J.Jiang,andK.Ren,‘‘Towardprivacy-preserving
L.S.Nakerekanti, and P. G. Naidu, ‘‘Credit score prediction using personalized recommendation services,’’ Engineering, vol. 4, no. 1,
supportvectormachineandgraywolfoptimization,’’inProc.3rdInt. pp.21–28,Feb.2018.
Conf.Intell.Technol.(CONIT),Jun.2023,pp.1–5. [321] E.Watt,‘‘Therighttoprivacyandthefutureofmasssurveillance,’’Int.
[301] H. Ma, J. Ma, S. Liang, and W. Du, ‘‘A model of integrating BERT J.HumanRights,vol.21,no.7,pp.773–799,May2017.
andBiGRU+attentiondual-channelmechanismforinvestorsentiment [322] A. Howard, C. Zhang, and E. Horvitz, ‘‘Addressing bias in machine
analysis of stock price forecast,’’ in Proc. IEEE/ACIS 23rd Int. Conf. learningalgorithms:Apilotstudyonemotionrecognitionforintelligent
Softw.Eng.,Artif.Intell.,Netw.Parallel/DistributedComput.(SNPD), systems,’’inProc.IEEEWorkshopAdv.Robot.SocialImpacts(ARSO),
Dec.2022,pp.126–131. Mar.2017,pp.1–7.
[302] Y. W. Bhowte, A. Roy, K. B. Raj, M. Sharma, K. Devi, and P. [323] L.F.Barrett,R.Adolphs,S.Marsella,A.M.Martinez,andS.D.Pollak,
LathaSoundarraj, ‘‘Advanced fraud detection using machine learning ‘‘Emotionalexpressionsreconsidered:Challengestoinferringemotion
techniquesinaccountingandfinancesector,’’inProc.9thInt.Conf.Sci. fromhumanfacialmovements,’’Psychol.Sci.PublicInterest,vol.20,
Technol.Eng.Math.(ICONSTEM),Apr.2024,pp.1–6. no.1,pp.1–68,Jul.2019.
128416 VOLUME13,2025

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[324] Y.Fan,J.C.K.Lam,andV.O.K.Li,‘‘Demographiceffectsonfacial [344] Y.Zhang,D.Sidibé,O.Morel,andF.Mériaudeau,‘‘Deepmultimodal
emotionexpression:Aninterdisciplinaryinvestigationofthefacialaction fusionforsemanticimagesegmentation:Asurvey,’’ImageVis.Comput.,
unitsofhappiness,’’Sci.Rep.,vol.11,no.1,p.5214,Mar.2021. vol.105,Jan.2021,Art.no.104042.
[325] R.K.Manchanda,A.Miglani,M.Chakraborty,B.S.Meena,K.Sharma, [345] N.Li,C.P.Ho,J.Xue,L.W.Lim,G.Chen,Y.H.Fu,andL.Y.T.Lee,
M.Gupta,A.Sharma,V.Chadha,P.Rani,R.K.Singh,andL.Rutten, ‘‘AprogressreviewonsolidstateLiDARandnanophotonicsbasedLiDAR
‘‘ImpactofbiasindatacollectionofCOVID-19cases,’’Homeopathy, sensors,’’LaserPhoton.Rev.,vol.16,no.11,2022,Art.no.2100511.
vol.111,no.1,pp.057–065,Feb.2022.
|     |     |     |     |     |     |     | [346] G.V.Aher,R.I.Arriaga,andA.T.Kalai,‘‘Usinglargelanguagemodels |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- |
[326] P.Schmitter,J.Steinrücken,C.Römer,A.Ballvora,J.Léon,U.Rascher, to simulate multiple humans and replicate human subject studies,’’ in
andL.Plümer,‘‘Unsuperviseddomainadaptationforearlydetectionof Proc.Int.Conf.Mach.Learn.,Jul.2023,pp.337–371.
droughtstressinhyperspectralimages,’’ISPRSJ.Photogramm.Remote [347] I. Lamaakal, Y. Maleh, K. El Makkaoui, I. Ouahbi, P. Pławiak, O.
Sens.,vol.131,pp.65–76,Sep.2017. Alfarraj,M.Almousa,andA.A.AbdEl-Latif,‘‘Tinylanguagemodels
[327] S.Dávila-Montero,J.A.Dana-Lê,G.Bente,A.T.Hall,andA.J.Mason, forautomationandcontrol:Overview,potentialapplications,andfuture
‘‘Reviewandchallengesoftechnologiesforreal-timehumanbehavior
researchdirections,’’Sensors,vol.25,no.5,p.1318,Feb.2025.
monitoring,’’IEEETrans.Biomed.CircuitsSyst.,vol.15,no.1,pp.2–
|     |     |     |     |     |     |     | [348] I.deZarzà,J.deCurtó,G.Roig,andC.T.Calafate,‘‘Optimizedfinancial |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- |
28,Feb.2021.
planning:Integratingindividualandcooperativebudgetingmodelswith
[328] K.Nimmi,B.Janet,A.K.Selvan,andN.Sivakumaran,‘‘Pre-trained LLMrecommendations,’’AI,vol.5,no.1,pp.91–114,Dec.2023.
ensemblemodelforidentificationofemotionduringCOVID-19based
on emergency response support system dataset,’’ Appl. Soft Comput., [349] S. Essahraui, I. Ouahbi, K. E. Makkaoui, and M. Filali Bouami,
|     |     |     |     |     |     |     | ‘‘A deep | learning-driven | fingerprint | verification | model for enhancing |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | ----------- | ------------ | ------------------- |
vol.122,Jun.2022,Art.no.108842.
|     |     |     |     |     |     |     | exam | integrity in Moroccan | higher | education,’’ | Inf. Secur. J., Global |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------------------- | ------ | ------------ | ---------------------- |
[329] D.Park,S.Kim,Y.An,andJ.-Y.Jung,‘‘LiReD:Alight-weightreal-time
Perspective,vol.33,pp.1–13,Jul.2024.
faultdetectionsystemforedgecomputingusingLSTMrecurrentneural
|     |     |     |     |     |     |     | [350] Y.Tang,‘‘Privacyprotectionframeworkforopendata:Constructingand |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- |
networks,’’Sensors,vol.18,no.7,p.2110,Jun.2018.
assessinganeffectiveapproach,’’LibraryInf.Sci.Res.,vol.46,no.3,
[330] F.Wang,M.Zhang,X.Wang,X.Ma,andJ.Liu,‘‘Deeplearningforedge
computingapplications:Astate-of-the-artsurvey,’’IEEEAccess,vol.8, Jul.2024,Art.no.101312.
pp.58322–58336,2020. [351] Z.Wu,S.Shen,H.Zhou,H.Li,C.Lu,andD.Zou,‘‘Aneffectiveapproach
|                 |     |                |        |             |            |         | for the | protection of | user commodity | viewing | privacy in e-commerce |
| --------------- | --- | -------------- | ------ | ----------- | ---------- | ------- | ------- | ------------- | -------------- | ------- | --------------------- |
| [331] I. Nassra | and | J. V. Capella, | ‘‘Data | compression | techniques | in IoT- |         |               |                |         |                       |
website,’’Knowl.-BasedSyst.,vol.220,May2021,Art.no.106952.
enabledwirelessbodysensornetworks:Asystematicliteraturereview
|     |                 |     |                    |          |         |          | [352] A.Kukkar,R.Mohana,A.Sharma,andA.Nayyar,‘‘PredictionofStudent |     |     |     |     |
| --- | --------------- | --- | ------------------ | -------- | ------- | -------- | ------------------------------------------------------------------ | --- | --- | --- | --- |
| and | research trends | for | QoS improvement,’’ | Internet | Things, | vol. 23, |                                                                    |     |     |     |     |
academicperformancebasedontheiremotionalwellbeingandinteraction
Oct.2023,Art.no.100806.
[332] M.A.Dixon,U.C.Braae,P.Winskill,M.Walker,B.Devleesschauwer, on various e-learning platforms,’’ Educ. Inf. Technol., vol. 28, no. 8,
S.Gabriël,andM.-G.Basáñez,‘‘Strategiesfortacklingtaeniasolium pp.9655–9684,Jan.2023.
taeniosis/cysticercosis: A systematic review and comparison of trans- [353] W.F.Heckler,L.P.Feijó,J.V.deCarvalho,andJ.L.V.Barbosa,‘‘Digital
missionmodels,includinganassessmentofthewidertaeniidaefamily phenotyping for mental health based on data analytics: A systematic
literaturereview,’’Artif.Intell.Med.,vol.163,May2025,Art.no.103094.
transmissionmodels,’’PLOSNeglectedTropicalDiseases,vol.13,no.4,
Apr.2019,Art.no.e0007301. [354] S. Banabilah, M. Aloqaily, E. Alsayed, N. Malik, and Y. Jararweh,
[333] B.Hu,Z.Cao,andM.Zhou,‘‘Energy-minimizedschedulingofreal-time ‘‘Federatedlearningreview:Fundamentals,enablingtechnologies,and
parallel workflows on heterogeneous distributed computing systems,’’ futureapplications,’’Inf.Process.Manage.,vol.59,no.6,Nov.2022,
| IEEETrans.ServicesComput.,vol.15,no.5,pp.2766–2779,Sep.2022. |     |     |     |     |     |     | Art.no.103061. |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
[334] I. Lamaakal, S. Essahraui, Y. Maleh, K. E. Makkaoui, I. Ouahbi, [355] R.Chhabra,S.Singh,andV.Khullar,‘‘Privacyenableddriverbehavior
M.F.Bouami,A.A.A.El-Latif,M.Almousa,J.Peng,andD.Niyato, analysisinheterogeneousIoVusingfederatedlearning,’’Eng.Appl.Artif.
‘‘Acomprehensivesurveyontinymachinelearningforhumanbehavior Intell.,vol.120,Apr.2023,Art.no.105881.
| analysis,’’ | IEEE | Internet | Things J., early | access, | Apr. 29, | 2025, doi: |                    |             |     |             |                           |
| ----------- | ---- | -------- | ---------------- | ------- | -------- | ---------- | ------------------ | ----------- | --- | ----------- | ------------------------- |
|             |      |          |                  |         |          |            | [356] C. Marcolla, | V. Sucasas, | M.  | Manzano, R. | Bassoli, F. H. P. Fitzek, |
10.1109/JIOT.2025.3565688. and N.Aaraj, ‘‘Survey on fully homomorphic encryption, theory, and
[335] K.Cao,Y.Liu,G.Meng,andQ.Sun,‘‘Anoverviewonedgecomputing applications,’’Proc.IEEE,vol.110,no.10,pp.1572–1609,Oct.2022.
research,’’IEEEAccess,vol.8,pp.85714–85728,2020. [357] X.Liu,Y.Deng,A.Nallanathan,andM.Bennis,‘‘Federatedlearningand
[336] G.Cicirelli,R.Marani,A.Petitti,A.Milella,andT.D’Orazio,‘‘Ambient metalearning:Approaches,applications,anddirections,’’IEEECommun.
| assisted | living: | A review | of technologies, | methodologies |     | and future |     |     |     |     |     |
| -------- | ------- | -------- | ---------------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- |
SurveysTuts.,vol.26,no.1,pp.571–618,1stQuart.,2024.
perspectivesforhealthyagingofpopulation,’’Sensors,vol.21,no.10,
|     |     |     |     |     |     |     | [358] S.Ahmad,S.Mehfuz,andJ.Beg,‘‘Hybridcryptographicapproachto |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- |
p.3549,May2021.
enhancethemodeofkeymanagementsystemincloudenvironment,’’J.
[337] Y.Albadawi,M.Takruri,andM.Awad,‘‘Areviewofrecentdevelopments Supercomput.,vol.79,no.7,pp.7377–7413,Nov.2022.
indriverdrowsinessdetectionsystems,’’Sensors,vol.22,no.5,p.2069,
|     |     |     |     |     |     |     | [359] Z. Cai, | Z. Xiong, | H. Xu, P. Wang, | W. Li, | and Y. Pan, ‘‘Generative |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- | --------------- | ------ | ------------------------ |
Mar.2022. adversarialnetworks:Asurveytowardprivateandsecureapplications,’’
[338] D.Wu,R.Ullah,P.Harvey,P.Kilpatrick,I.Spence,andB.Varghese,
ACMComput.Surveys,vol.54,no.6,pp.1–38,Jul.2022.
‘‘FedAdapt:AdaptiveoffloadingforIoTdevicesinfederatedlearning,’’
|     |     |     |     |     |     |     | [360] E.Prem,‘‘FromethicalAIframeworkstotools:Areviewofapproaches,’’ |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------------- | --- | --- | --- | --- |
IEEEInternetThingsJ.,vol.9,no.21,pp.20889–20901,Nov.2022.
AIEthics,vol.3,no.3,pp.699–716,Aug.2023.
| [339] A. Elhanashi, |               | P. Dini, S. | Saponara,    | and Q. Zheng, | ‘‘Advancements |            |                    |       |           |            |                         |
| ------------------- | ------------- | ----------- | ------------ | ------------- | -------------- | ---------- | ------------------ | ----- | --------- | ---------- | ----------------------- |
|                     |               |             |              |               |                |            | [361] S. Siddique, | M. A. | Haque, R. | George, K. | D. Gupta, D. Gupta, and |
| in TinyML:          | Applications, |             | limitations, | and impact    | on IoT         | devices,’’ |                    |       |           |            |                         |
Electronics,vol.13,no.17,p.3562,Sep.2024. M.J.H.Faruk, ‘‘Survey on machine learning biases and mitigation
[340] A. A. Shahid, D. Piga, F. Braghin, and L. Roveda, ‘‘Continuous techniques,’’Digital,vol.4,no.1,pp.1–68,Dec.2023.
controlactionslearningandadaptationforroboticmanipulationthrough [362] P. V. Kakarlapudi and Q. H. Mahmoud, ‘‘A systematic review of
reinforcement learning,’’ Auto. Robots, vol. 46, no. 3, pp. 483–498, blockchainforconsentmanagement,’’Healthcare,vol.9,no.2,p.137,
Feb.2021.
Mar.2022.
|     |     |     |     |     |     |     | [363] L.Xing,S.Shao,W.Liu,A.Han,X.Pan,andB.-D.Liu,‘‘Learningtask- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- |
[341] J.Yan,Y.Cheng,Q.Wang,L.Liu,W.Zhang,andB.Jin,‘‘Transformer
specificdiscriminativeembeddingsforfew-shotimageclassification,’’
andgraphconvolution-basedunsuperviseddetectionofmachineanoma-
loussoundunderdomainshifts,’’IEEETrans.Emerg.TopicsComput. Neurocomputing,vol.488,pp.1–13,Jun.2022.
Intell.,vol.8,no.4,pp.2827–2842,Aug.2024. [364] H.Cheng,M.Zhang,andJ.Q.Shi,‘‘Asurveyondeepneuralnetwork
[342] D. Yu, B. Yang, D. Liu, H. Wang, and S. Pan, ‘‘A survey on neural- pruning:Taxonomy,comparison,analysis,andrecommendations,’’IEEE
symbolic learning systems,’’ Neural Netw., vol. 166, pp. 105–126, Trans. Pattern Anal. Mach. Intell., vol. 46, no. 12, pp. 10558–10578,
| Sep.2023. |     |     |     |     |     |     | Dec.2024. |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- |
[343] M. Pateraki, K. Fysarakis, V. Sakkalis, G. Spanoudakis, I. Varlamis, [365] J.Metcalf,E.Moss,E.A.Watkins,R.Singh,andM.C.Elish,‘‘Algo-
M.Maniadakis,andD.Koutsouris,‘‘BiosensorsandInternetofThings rithmicimpactassessmentsandaccountability:Theco-constructionof
in smart healthcare applications: Challenges and opportunities,’’ in impacts,’’inProc.ACMConf.Fairness,Accountability,Transparency,
WearableandImplantableMedicalDevices.Academic,2020,pp.25–53. Mar.2021,pp.735–746.
VOLUME13,2025 128417

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
[366] N.Almén,‘‘Acognitivebehavioralmodelproposingthatclinicalburnout YASSINE MALEH (Senior Member, IEEE) is
maymaintainitself,’’Int.J.Environ.Res.PublicHealth,vol.18,no.7, currentlyaProfessorofcybersecurityandITgov-
| p.3446,Mar.2021. |     |     |     |     |     |     |     |     |     | ernancewithSultanMoulaySlimaneUniversity, |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
[367] Y.Yin,Y.Shao,Y.Hao,andX.Lu,‘‘Perceivedsoundscapeexperiences Morocco.Hehasmadecontributionsinthefields
and human emotions in urban green spaces: Application of Russell’s of information security and privacy, the Internet
circumplexmodelofaffect,’’Appl.Sci.,vol.14,no.13,p.5828,Jul.2024.
|     |     |     |     |     |     |     |     |     |     | of Things | security, | wireless, | and | constrained |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------- | --- | ----------- |
[368] A.vonLühmann,Y.Zheng,A.Ortega-Martinez,S.Kiran,D.C.Somers,
|     |     |     |     |     |     |     |     |     |     | networks | security. | He has | published | more than |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ------ | --------- | --------- |
A.Cronin-Golomb,L.N.Awad,T.D.Ellis,D.A.Boas,andM.A.Yücel,
200papers(bookchapters,internationaljournals,
‘‘Towardneuroscienceoftheeverydayworld(NEW)usingfunctional
|               |     |                 |         |         |         |       |          |     |     | and conferences/workshops), |     |     | 17  | edited books, |
| ------------- | --- | --------------- | ------- | ------- | ------- | ----- | -------- | --- | --- | --------------------------- | --- | --- | --- | ------------- |
| near-infrared |     | spectroscopy,’’ | Current | Opinion | Biomed. | Eng., | vol. 18, |     |     |                             |     |     |     |               |
Jun.2021,Art.no.100272. and three authored books. His research interests
|          |             |         |          |     |        |                     |     | include information |     | security and | privacy, | the Internet | of Things, | network |
| -------- | ----------- | ------- | -------- | --- | ------ | ------------------- | --- | ------------------- | --- | ------------ | -------- | ------------ | ---------- | ------- |
| [369] H. | Ge, Z. Zhu, | Y. Dai, | B. Wang, | and | X. Wu, | ‘‘Facial expression |     |                     |     |              |          |              |            |         |
security,informationsystems,andITgovernance.Heisamemberofthe
| recognition | based | on  | deep learning,’’ |     | Comput. | Methods Programs |     |     |     |     |     |     |     |     |
| ----------- | ----- | --- | ---------------- | --- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
InternationalAssociationofEngineersIAENGandtheMachineIntelligence
Biomed.,vol.215,Jan.2022,Art.no.106621.
ResearchLaboratories.HeistheFoundingChairoftheIEEEConsultant
| [370] C. Zhao, | Z. Wang, | X.  | Tang, J. | Qin, and | Z. Jiang, | ‘‘Recent | advances |     |     |     |     |     |     |     |
| -------------- | -------- | --- | -------- | -------- | --------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
insensor-integratedbrain-on-a-chipdevicesforreal-timebrainmonitor- Network Morocco and the Founding President of the African Research
ing,’’ColloidsSurf.B,Biointerfaces,vol.229,Sep.2023,Art.no.113431. CenterofInformationTechnologyandCybersecurity.HereceivedPublons
[371] O. Perski, E. T. Hébert, F. Naughton, E. B. Hekler, J. Brown, and Top1%reviewerawards,in2018and2019.HewasthePublicityChairof
M.S.Businelle, ‘‘Technology-mediated just-in-time adaptive interven- BCCA2019andtheGeneralChairoftheMLBDACP19Symposiumand
tions(JITAIs)toreduceharmfulsubstanceuse:Asystematicreview,’’ ICI2C’21 Conference. He is the Editor-in-Chief of International Journal
Addiction,vol.117,no.5,pp.1220–1241,May2022.
|               |           |          |     |       |             |        |          | of Information | Security | and Privacy | and | International | Journal | of Smart |
| ------------- | --------- | -------- | --- | ----- | ----------- | ------ | -------- | -------------- | -------- | ----------- | --- | ------------- | ------- | -------- |
| [372] Z. Lin, | Y. Zhang, | Q. Gong, | Y.  | Chen, | A. Oksanen, | and A. | Y. Ding, |                |          |             |     |               |         |          |
SecurityTechnologies(IJSST).HeservesasanAssociateEditorforIEEE
| ‘‘Structural | hole | theory | in social | network | analysis: | A review,’’ | IEEE |     |     |     |     |     |     |     |
| ------------ | ---- | ------ | --------- | ------- | --------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ACCESS(2019ImpactFactor4.098),InternationalJournalofDigitalCrime
Trans.Computat.SocialSyst.,vol.9,no.3,pp.724–739,Jun.2022. andForensics(IJDCF),andInternationalJournalofInformationSecurity
[373] J.Skarding,B.Gabrys,andK.Musial,‘‘Foundationsandmodelingof and Privacy (IJISP). He is a Series Editor of Advances in Cybersecurity
dynamic networks using dynamic graph neural networks: A survey,’’ Management,byCRCTaylorandFrancis.HewasalsoaGuestEditorof
IEEEAccess,vol.9,pp.79143–79168,2021.
|     |     |     |     |     |     |     |     | a Special | Issue on | Recent Advances | on  | Cyber Security | and | Privacy for |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --------------- | --- | -------------- | --- | ----------- |
CloudofThingsofInternationalJournalofDigitalCrimeandForensics
(IJDCF),Volume10,Issue3,fromJulytoSeptember2019.Hehasserved
andcontinuestoserveonexecutiveandtechnicalprogramcommitteesandas
aReviewerofnumerousinternationalconferencesandjournals,suchasAd
HocNetworks(Elsevier),IEEENetworkMagazine,IEEESENSORSJOURNAL,
ICTExpress,andClusterComputing(Springer).
|     |     | SIHAM | ESSAHRAUI |     | (Student | Member, | IEEE) |     |     |     |     |     |     |     |
| --- | --- | ----- | --------- | --- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
receivedtheMasterofSciencedegreeincomputer
|     |     | science | from     | the | Multidisciplinary | Faculty     | of     |     |     |     |     |     |     |     |
| --- | --- | ------- | -------- | --- | ----------------- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     |     | Nador,  | Mohammed |     | Premier           | University, | Oujda, |     |     |     |     |     |     |     |
KHALIDELMAKKAOUI(SeniorMember,IEEE)
|     |     | Morocco, | where  | she         | is currently | pursuing | the      |     |     |          |              |        |     |              |
| --- | --- | -------- | ------ | ----------- | ------------ | -------- | -------- | --- | --- | -------- | ------------ | ------ | --- | ------------ |
|     |     |          |        |             |              |          |          |     |     | received | the master’s | degree | in  | networks and |
|     |     | Ph.D.    | degree | in computer | science.     | As       | an Arti- |     |     |          |              |        |     |              |
systemsandthePh.D.degreeincomputerscience
ficial Intelligence Scientist, her research primar- from Hassan I University, Settat, Morocco, in
ily focuses on analyzing human behavior using 2014and2018,respectively.Since2019,hehas
advancedAItechniques. been a Researcher and a Professor of computer
|     |     |     |     |     |     |     |     |     |     | science     | and cybersecurity |           | with     | the Multidisci- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------------- | --------- | -------- | --------------- |
|     |     |     |     |     |     |     |     |     |     | plinary     | Faculty           | of Nador, | Mohammed | Premier         |
|     |     |     |     |     |     |     |     |     |     | University, | Oujda,            | Morocco.  | He       | has published   |
|     |     |     |     |     |     |     |     |     |     | more than   | 55 articles,      | including |          | book chapters,  |
internationaljournalarticles,andconferencepapers.Hisresearchinterests
includecybersecurityandartificialintelligence.
|     |     | ISMAIL | LAMAAKAL |     | (Student | Member, | IEEE) |     |     |     |     |     |     |     |
| --- | --- | ------ | -------- | --- | -------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
receivedtheMasterofSciencedegreeincomputer
science from the Multidisciplinary Faculty of MOUNCEFFILALIBOUAMIreceivedtheM.Sc.
Nador, Mohammed Premier University, Oujda, degreeinelectronicsfromtheUniversityofFez,
Morocco, where he is currently pursuing the Morocco, in 1998, and the Ph.D. degree from
Ph.D. degree in computer science. As an Artifi- the University of Granada, Spain, in 2005, after
cial Intelligence Scientist, his research primarily havingdefendedaPh.D.thesisonthemodeling
focuses on the innovative integration of tiny of RBF neural networks using T-Norm and T-
machinelearning,theInternetofThings(IoT),and Conormoperatorsandweightsparameterization.
embeddedsystems.Hisworkischaracterizedby Since2010,hehasbeenaSeniorLecturerwiththe
itspioneeringapproachinthefield,emphasizingpracticalapplicationsand Poly-DisciplinaryFacultyofNador,Mohammed
advancementsintheseinterconnecteddomains.Hiscontributionsaremarked PremierUniversity,Morocco.Hisresearchinter-
byacommitmenttopushingtheboundariesofAIanditsapplicationsinthe ests include machine learning algorithms, text classification, and speech
| moderntechnologicallandscape. |     |     |     |     |     |     |     | recognitionmethods. |     |     |     |     |     |               |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | ------------- |
| 128418                        |     |     |     |     |     |     |     |                     |     |     |     |     |     | VOLUME13,2025 |

S.Essahrauietal.:HumanBehaviorAnalysis:AComprehensiveSurvey
IBRAHIM OUAHBI received the Ph.D. degree MAY ALMOUSA received the Bachelor of Science degree (Hons.) in
in didactics of informatics from Sidi Mohamed computer science from Princess Nourah bint Abdulrahman University
BenAbdellahUniversity,Fez,Morocco,in2018. (PNU),Riyadh,SaudiArabia,in2009,andtheMasterofScienceandPh.D.
He was a Professor of educational technolo- degrees in computer science from North Carolina A&T State University,
gies with the Faculty of Educational Sciences, in 2016 and 2022, respectively. She developed her dissertation under the
MohammedVUniversityofRabat,in2019.Heis supervision of Dr. Mohd Anwar at the Human-Centered AI Laboratory.
currently a Professor of computer science with In 2011, she joined PNU, as a Faculty Member with the College of
the Multidisciplinary Faculty of Nador, Univer- Computer Science, Network, and Communication Systems Department,
sity Mohammed Premier, Oujda, Morocco. His where she taught an array of courses in computer science. She was
research interests include artificial intelligence, recognizedbytheCollegeofEngineering’sannualgraduationreceptionfor
cybersecurity,andICTintegrationinscienceeducationandlearning. heroutstandingacademicaccomplishments.Hercurrentresearchinterests
includecyberattackdetection,datascience,andAItechniques.
AHMED A. ABD EL-LATIF (Senior Member,
IEEE)iscurrentlyaProfessorofcomputerscience JOEL J. P. C. RODRIGUES (Fellow, IEEE) is
with Menoufia University, Egypt. His expertise currentlyaLeaderwiththeCenterforIntelligence,
encompasses quantum cryptography, cybersecu- Fecomércio/CE,Brazil,andaFullProfessorwith
rity,chaoticdynamicalsystems,andAIapplica- LusófonaUniversity,Lisbon,Portugal.Heisalso
tionsin5Gand6Gnetworks.Afull-stackcom- theLeaderoftheNextGenerationNetworksand
puter scientist engaged in coding, development, Applications(NetGNA)ResearchGroup(CNPq).
research, and theoretical work, he has led and Hehasauthoredorco-authoredabout1150papers
participatedinnumeroussuccessfulinternational inrefereedinternationaljournalsandconferences,
research projects, securing grants across Egypt, three books, two patents, and one ITU-T rec-
Russia,SaudiArabia,China,Malaysia,andTunisia.Aprolificauthorwith ommendation. He is a member of the Internet
more than 340 publications, including more than 30 IEEE TRANSACTIONS Society, a Senior Member of ACM, and a fellow of AAIA. He is a
articles and 20 books, his work has garnered more than 13500 citations MemberRepresentativeoftheIEEECommunicationsSocietyontheIEEE
andanH-indexof65.HeleadstheMEGANET6GLaboratoryResearchin BiometricsCouncilandthePresidentoftheScientificCouncilatParkUrbis–
Russiaandhasconsistentlybeenrecognizedamongthetop2%ofscientists Covilhã Science and Technology Park. He has been awarded several the
in his field by the Stanford List of Top Scientists, in 2019 and 2024. Outstanding Leadership and Outstanding Service Awards by the IEEE
Hisresearchinterestsincludequantumcommunicationsandcryptography, Communications Society and several best papers awards. He is a Highly
cybersecurity,artificialintelligenceofthings,AI-basedimageprocessing, Cited Researcher (Clarivate) and one of the top scientists in computer
information hiding, and the application of dynamical systems (chaotic science in Brazil (Research.com). He was the Director for Conference
systems and quantum walks) in cybersecurity. He founded the Center Development—IEEEComSocBoardofGovernors,anIEEEDistinguished
of Excellence in Quantum and Intelligent Computing and has received Lecturer,theTechnicalActivitiesCommitteeChairoftheIEEEComSoc
several prestigious awards, including the State Encouragement Award in LatinAmericaRegionBoard,thePast-ChairoftheIEEEComSocTechnical
EngineeringSciences,Egypt,in2016,theBestPh.D.StudentAward,China, Committee (TC) on eHealth and the TC on Communications Software,
in2013,andtheYoungScientistAwardfromMenoufiaUniversity,in2014. the Steering Committee Member of the IEEE Life Sciences Technical
HeactivelycontributestothescientificcommunityastheChair/Co-Chairof Community,andthePublicationsCo-Chair.HehasbeentheGeneralChair
numerousScopus/EIconferencesandholdskeyeditorialpositions,including and the TPC Chair of many international conferences, including IEEE
the Editor-in-Chief of International Journal of Information Security and ICC, IEEE GLOBECOM, IEEE HEALTHCOM, and IEEE LatinCom.
Privacy and the Series Editor of Quantum Information Processing and HeistheEditor-in-ChiefofInternationalJournalofE-HealthandMedical
ComputingandAdvancesinCybersecurityManagement.Healsoservesas Communicationsandaneditorialboardmemberofseveralhighlyreputed
an academic and associate editor for many Web of Science and Scopus- journals(mainly,fromIEEE).
indexedjournals.
VOLUME13,2025 128419