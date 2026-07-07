| Misplaced     | trust            | in AI: | the explanation    | paradox | and           | the |
| ------------- | ---------------- | ------ | ------------------ | ------- | ------------- | --- |
| human-centric |                  | path.  | A characterisation | of      | the cognitive |     |
| challenges    | to appropriately |        | trust algorithmic  |         | decisions     | and |
|               | applications     |        | in the financial   | sector  |               |     |
Astrid Bertrand
| To cite this | version: |     |     |     |     |     |
| ------------ | -------- | --- | --- | --- | --- | --- |
AstridBertrand. MisplacedtrustinAI:theexplanationparadoxandthehuman-centricpath. Acharacterisa-
tionofthecognitivechallengestoappropriatelytrustalgorithmicdecisionsandapplicationsinthefinancial
sector. Artificial Intelligence [cs.AI]. Institut Polytechnique de Paris, 2024. English. ⟨NNT: 2024IPPAT012⟩.
⟨tel-04661844⟩
|     |     | HAL | Id: tel-04661844 |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- |
https://theses.hal.science/tel-04661844v1
Submittedon25Jul2024
HAL is a multi-disciplinary open access archive L’archiveouvertepluridisciplinaireHAL,estdes-
for the deposit and dissemination of scientific re- tinée au dépôt et à la diffusion de documents scien-
searchdocuments,whethertheyarepublishedornot. tifiquesdeniveaurecherche,publiésounon,émanant
Thedocumentsmaycomefromteachingandresearch des établissements d’enseignement et de recherche
institutionsinFranceorabroad,orfrompublicorpri- français ou étrangers, des laboratoires publics ou
| vateresearchcenters. |     |     | privés. |     |     |     |
| -------------------- | --- | --- | ------- | --- | --- | --- |
HALAuthorization

210TAPPI4202
|     |     | Misplaced |                  | trust   | in            | AI:              | the | explanation |           |     |
| --- | --- | --------- | ---------------- | ------- | ------------- | ---------------- | --- | ----------- | --------- | --- |
|     |     | paradox   |                  | and the | human-centric |                  |     |             | path.     | A   |
|     |     |           | characterisation |         |               |                  | of  | the         | cognitive |     |
|     |     |           | challenges       |         |               | to appropriately |     |             | trust     |     |
:
| TNN | algorithmic |     |     | decisions |     | and | applications |     |         | in  |
| --- | ----------- | --- | --- | --------- | --- | --- | ------------ | --- | ------- | --- |
|     |             |     |     |           |     | the | financial    |     | sector. |     |
The`sededoctoratdel’InstitutPolytechniquedeParis
|     |     |     |     |     |     |     |     | pre´pare´ea` | Te´le´comParis |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- |
E´coledoctoralen◦626Ecoledoctoraledel’InstitutPolytechniquedeParis(EDIP
Paris)
|     |     |     |     |     |                               |     | Spe´cialite´ | dedoctorat:Informatique   |          |     |
| --- | --- | --- | --- | --- | ----------------------------- | --- | ------------ | ------------------------- | -------- | --- |
|     |     |     |     |     | The`sepre´sente´eetsoutenuea` |     |              | Palaiseau,le21mai2024,par |          |     |
|     |     |     |     |     |                               |     |              | ASTRID                    | BERTRAND |     |
CompositionduJury:
AlexandredeStreel
|     | Professeur,Universite´ |     |     | deNamur |     |     |     | Pre´sident/Examinateur |     |     |
| --- | ---------------------- | --- | --- | ------- | --- | --- | --- | ---------------------- | --- | --- |
FoscaGiannotti
|     | Professeure,ScuolaNormaleSuperiorediPisa |     |     |     |     |     |     | Rapporteure |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
TimMiller
|     | Professeur,UniversityofQueensland |     |     |     |     |     |     | Rapporteur |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
NadiaBoukhelifa
Charge´ederecherche,INRAE,Universite´ ParisSaclay Examinatrice
WinstonMaxwell
|     | Professeur,i3,CNRS,Te´le´comParis |     |     |     |     |     |     | Directeurdethe`se |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- |
JamesR.Eagan
Maˆıtredeconfe´rences,LTCI,Te´le´comParis Co-directeurdethe`se
OlivierFliche
|     | DirecteurdupoˆleFintech-Innovation,ACPR,BanquedeFrance |     |     |     |     |     |     | Invite´ |     |     |
| --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
626

Abstract
Deep learning, the technology behind ChatGPT relies on a complex
and massive network of mathematical operations. Although we know
the math for each individual operation, we do not understand why the
network as a whole produces the results we see. For most of "artificial
1
intelligence" (AI) models , it is unclear why they behave the way they 1The term "artificial in-
do, making it difficult to determine when they fail and if they have bi- telligence" (AI) encom-
passesthesedeeplearn-
ases. Thisproblemhasledtoasignificantgrowthofresearchonexplain-
ing techniques as well
ability in recent years, which focuses on understanding the behaviour
aslesscomplexmachine
of machine learning models. However, there has been comparatively
learningmodels.
little exploration of how current explainability methods align with the
requirements of highly regulated environments such as finance, taking
into account human factors. In such contexts, the warranted, i.e. well-
calibrated trust of customers and regulators in AI systems can be critical
for achieving regulatory compliance. This thesis explores the potential
ofexplainabilitytoenablewarrantedtrustinAIandhelpensurecompli-
ance of AI-enhanced systems in financial applications.
The first part explores the cognitive barriers related to the construc-
tion of explainable AI interfaces that promote appropriate levels of trust,
through two detailed scoping literature reviews. In the first analysis, we
present a heuristic map of the different cognitive biases to be taken into
38
account in the design of explainability through the review of research
articles. We also detail the context in which these different biases were
found, in particular the method of explicitation used and the types of
users and tasks in which they appear. This study reveals an ‘explanation
paradox’, where explanations intended to inform users may ultimately
increase their confidence in untrustworthy AI models, which is undesir-
able. The second detailed scoping literature review of this thesis studies
48
a corpus of articles and provides a taxonomy of the different ways of
interacting with explainability solutions. We identify three categories of
interactionaccordingtotheirroleinthecognitiveprocessofexplanation:
‘selective’, ‘mutable’ or ‘dialogic’. We also analyse the effects of these
types of interaction on users. We find that interactive explanations im-
prove the perceived usefulness and performance of the human+AI team,
but that they take longer. Finally, we describe some little-explored av-
enues, such as measuring curiosity or learning.
The second part deals with the needs and effects of explanations in fi-
256
nancial contexts. We conduct a controlled study with participants in
the context of online life insurance distribution, where there are already
legalrequirementsforexplanations,tocomparetheeffectofseveraltypes

2
of explanation representation on user trust. We show that feature-based
explanations did not significantly improve customers’ understanding of
the recommendation or their ability to perceive its inappropriateness, a
result that is the opposite of what the law hoped to achieve. In addi-
tion, explanations in the form of dialogue increased users’ trust in the
recommendationsmade bythe robo-advisor, sometimes tothe detriment
of the users themselves. This real-life scenario illustrates how explain-
ability can prove insufficient to remedy information asymmetry in com-
plex areas such as finance. Another study analyses supervisors’ require-
ments for explainability solutions in the fight against money launder-
ing and the financing of terrorism (AML-CFT). Through scenario-based
13 6
workshopswith supervisorsand bankingindustryprofessionals,we
describe the audit practices and the supervisor’s socio-technical context.
Combiningobservationsfromtheworkshopswithananalysisofcompli-
ance requirements, we identify AML-CFT obligations that conflict with
AI opacity. We then articulate supervisors’ needs for model justification.
We discuss the role of explanations as reliable evidence on which to base
justifications.
The conclusion discusses the potential of explanations to manipulate
usertrust. Wethenreviewpromisinghuman-centereddevelopmentpaths
for developing explainable AI interfaces that enhance user autonomy.
These include personalising explanations, presenting a range of options
ratherthanasinglerecommendation/explanation,stimulatinguserscep-
ticism, and fostering user engagement, curiosity and learning. The role
of explainability in mitigating regulatory tensions caused by the use of
opaque AI models in AML-CFT is also examined.

Résumé
L’apprentissage profond, la technologie derrière ChatGPT, repose sur
un réseau complexe et massif d’opérations mathématiques. Bien que
nousconnaissionslesmathématiquesdechacunedecesopérations,nous
necomprenonspaspourquoileréseaudanssonensembleproduitlesré-
sultats que nous voyons. Pour la plupart des modèles d’« intelligence
artificielle » (IA), on ne sait pas pourquoi ils se comportent comme ils le
font, ce qui rend difficile de déterminer quand ils peuvent se tromper
et s’ils ont des biais. Ce problème a conduit à une croissance signi-
ficative de la recherche sur l’explicabilité au cours des dernières an-
nées, qui se concentre sur la compréhension du comportement des mod-
èles d’apprentissage automatique. Toutefois, la façon dont les méthodes
actuelles d’explicabilité s’alignent sur les exigences d’environnements
hautementréglementéstelsquelafinance,entenantcomptedesfacteurs
humains, a été relativement peu explorée. Dans de tels contextes, la con-
fiance justifiée, i.e. bien calibrée des clients et des régulateurs dans les
systèmes d’IA peut être critique pour atteindre la conformité réglemen-
taire. Cette thèse explore le potentiel de l’explicabilité pour permettre
uneconfiancejustifiéedansl’IAetpouraideràassurerlaconformitédes
systèmes améliorés par l’IA dans les applications financières.
La première partie explore les obstacles cognitifs liés à la construc-
tion d’interfaces d’IA explicables et favorisant des niveaux de confiance
appropriés, grâce à deux examens détaillés de la littérature. Dans une
première analyse, nous présentons une carte heuristique des différents
biais cognitifs à prendre en compte dans la conception de l’explicabilité
38
grâce à l’examen de articles de recherche. Nous détaillons aussi le
contexte dans lequel ces différents biais identifiés ont été trouvés, no-
tamment la méthode d’explicitation utilisée et les types d’utilisateurs et
de tâches dans lesquels ils apparaissent. Cette étude révèle un « para-
doxe de l’explication », où les explications destinées à informer les util-
isateurs peuvent finalement accroître leur confiance dans des modèles
d’IA non dignes de confiance, ce qui n’est pas souhaitable. La deux-
48
ième revue de littérature de cette thèse étudie un corpus de articles
et fournit une taxonomie des différentes façons d’interagir avec les solu-
tions d’explicabilité. Nous déterminons trois catégories d’interaction en
fonction de leur rôle dans le processus cognitif d’explication : « sélectif
», « mutable » ou « dialogique ». Nous analysons également les effets
de ces types d’interaction sur les utilisateurs. Nous constatons que les
explications interactives améliorent l’utilité perçue et la performance de
l’équipe humaine+AI, mais qu’elles prennent plus de temps. Enfin, nous

4
décrivons des pistes peu explorées, notamment la mesure de la curiosité
ou de l’apprentissage.
La deuxième partie traite des besoins et des effets des explications
256
danslescontextesfinanciers. Nousmenonsuneétudecontrôléeavec
participants dans le contexte de la distribution en ligne d’assurances-
vie, où il existe déjà des exigences légales en matière d’explications,
pour comparer l’effet sur la confiance des utilisateurs de plusieurs types
de représentation d’explications. Nous montrons que les explications
baséessurlescaractéristiquesn’amélioraientpasdemanièresignificative
la compréhension de la recommandation par les clients ou leur capacité
àpercevoirsoncaractèreinapproprié,unrésultatquiestàl’opposédece
que la loi espérait obtenir. En outre, les explications sous forme de dia-
logueaugmententlaconfiancedesutilisateursdanslesrecommandations
durobot-conseiller,parfoisaudétrimentdesutilisateurs. Cescénarioréel
illustrecommentl’explicabilitépeutserévélerinsuffisantepourremédier
à l’asymétrie de l’information dans des domaines complexes tels que la
finance.
Une autre étude analyse les exigences des autorités de contrôle en
matière de solutions d’explicabilité dans le cadre de la lutte contre le
blanchiment d’argent et le financement du terrorisme (LCB-FT). Grâce à
13 6
des ateliers basés sur des scénarios avec superviseurs et profession-
nels du secteur bancaire, nous décrivons les pratiques d’audit et le con-
texte sociotechnique du superviseur. En combinant les observations des
ateliers avec une analyse des exigences de conformité, nous identifions
les obligations en matière de LCB-FT qui entrent en conflit avec l’opacité
de l’IA. Nous formulons ensuite les besoins des superviseurs en matière
de justification des modèles. Nous discutons du rôle des explications en
tant que preuves fiables sur lesquelles fonder les justifications.
La conclusion aborde le potentiel des explications pour manipuler la
confiance des utilisateurs. Nous passons ensuite en revue les pistes
de développement centrées sur l’humain qui sont prometteuses pour
développer des interfaces d’IA explicables qui améliorent l’autonomie
des utilisateurs. Ces pistes sont la personnalisation des explications, la
présentation d’un éventail d’options plutôt que d’une seule recomman-
dation/explication, la stimulation du scepticisme des utilisateurs, et la
favorisation de l’engagement, de la curiosité et de l’apprentissage des
utilisateurs. Le rôle de l’explicabilité dans l’atténuation des tensions ré-
glementaires causées par l’utilisation de modèles d’IA opaques dans la
LCB-FT est également examiné.

Acknowledgments
Work setup
I have been fortunate to be welcomed into a variety of working en-
vironments during my PhD. This thesis is a reflection of these many
experiences.
My research was carried out as part of a PhD contract with Télécom
Paris, an engineering school affiliated to the Institut Polytechnique de
Paris. Since my arrival at Télécom, I have been part of the newly formed
OperationalAIEthics(OpAIE)team,foundedbyWinstonMaxwell,which
explores interdisciplinary issues related to the societal impact of AI. As
one of the first PhD students of this group, it has been fantastic to see
6
it grow over the last three years—we are now over PhD students and
3
full-time professors. Starting from the second year of my PhD, thanks
to James Eagan, I joined the Design, Interaction, Visualizations and Appli-
cations (DIVA) group, the Human-Computer Interaction (HCI) team of
Télécom Paris. Finding colleagues with whom to discuss HCI methods,
conferences and best practices was invaluable.
Figure 1: Distribution
of my time between
different work environ-
ments during my PhD,
inspired from [Huron,
2014].
MyPhDfundingcomesfromtheExplainabilityforAnti-MoneyLaun-
2
deringandCounterTerrorismFinancing(AML-CFT) researchchair,spon- 2https://xai4aml.org/
sored by the Agence Nationale de la Recherche (ANR) through the grant
20 0023 01
ANR- -CHIA- - and several private partners, including Pricewa-
terCopperhouse(PwC),aninternationalconsultingfirm,Dataiku,aFrench
AI services provider startup, the Crédit Agricole, a large French bank,
3
and the ACPR , the French Regulatory Authority for Financial Services. 3Acronym for "Pruden-
tial Control and Resolu-
tionAuthority".

6
Asaresult, Ihadvariouscollaborationopportunitieswiththesepartners
| to carry | out applied | research. |     |     |     |     |
| -------- | ----------- | --------- | --- | --- | --- | --- |
At the beginning of my PhD, I worked briefly with PwC on a survey
about AI use in AML-CFT. It enabled me to gain a better understand-
ing of the AML-CFT context. However, the pace of consulting and of
researchoftenprovedincompatible. Therefore,Ifocusedmyfirstyearon
| academic | research, | with little industrial | collaboration. |     |     |     |
| -------- | --------- | ---------------------- | -------------- | --- | --- | --- |
The most fruitful collaboration I benefited from was with the Fintech-
Innovation team of the ACPR, thanks to Olivier Fliche and Christine
Saidani, starting from my second year. This collaboration gave me ac-
cess to industry expertise and guidance. As a result, I was able to find
real-world applications and research questions for XAI in finance that I
would not have been able to find alone. More than that, it has provided
me with a thriving working environment: welcoming and inspiring col-
leagues, a second office (close to my home), and a sense of belonging to
| the Fintech-Innovation |     | team. |     |     |     |     |
| ---------------------- | --- | ----- | --- | --- | --- | --- |
2022
| Between | September | and December | , I took a break | from my PhD |     |     |
| ------- | --------- | ------------ | ---------------- | ----------- | --- | --- |
to do a research internship at Google’s "People and AI Research" team
in Toronto. I wrote an interactive article about Saliency Maps, a set of
techniques to understand how computer vision models work. It was a
2:
| fun and | rich adventure. |     |     |     | Figure This    | saliency    |
| ------- | --------------- | --- | --- | --- | -------------- | ----------- |
|         |                 |     |     |     | map highlights | (in         |
|         |                 |     |     |     | white) the     | pixels that |
|         |                 |     |     |     | cause an AI    | model to    |
| Thanks  | to              |     |     |     |                |             |
|         |                 |     |     |     | recognise      | this cat as |
|         |                 |     |     |     | "cat". Find    | out more    |
I extend my heartfelt appreciation to my PhD supervisor, Winston
|     |     |     |     |     | in this article | I wrote |
| --- | --- | --- | --- | --- | --------------- | ------- |
Maxwell, whose unwavering support has been instrumental in guiding during my Google
me through the intricate journey of my doctoral research. You have not internship:
only provided invaluable insights into the interdisciplinary and legal as- https://pair.withg
oogle.com/explorable
pects of my research but your mentorship has been a beacon of inspi-
s/saliency/
ration, making me grow both professionally and personally. I would
also like to express my gratitude to James Eagan, my co-supervisor, who
| joinedmyadvisoryteammidwaythroughmyPhDjourney. |     |     |     | Youbrought |     |     |
| ---------------------------------------------- | --- | --- | --- | ---------- | --- | --- |
a fresh perspective to my research, offering invaluable insights to help
me better anchor in the discipline of HCI. I am deeply grateful for your
| thoughtful | and friendly | guidance. |     |     |     |     |
| ---------- | ------------ | --------- | --- | --- | --- | --- |
ThankyoualsototheOpAIEandDIVAteammembersfortheirfriendly
support. I want to thank Rafik Belloum, Joshua Brand, Mélanie Gornet,
Simon Delarue, Tiphaine Viard, Elise Bonnail and Xavier Vamparys for
| being great | colleagues | and friends | to work with. |     |     |     |
| ----------- | ---------- | ----------- | ------------- | --- | --- | --- |
A special thanks goes to Olivier Fliche and Christine Saidani, who af-
forded me the unique opportunity to collaborate with the Autorité de
Contrôle Prudentiel et de Résolution (ACPR). Olivier, your expert in-
sights and guidance have been a cornerstone in this dissertation. Thank
you for your continued support. Christine, your expertise but also your
friendship and shared interest in pottery made my experience particu-
larly enriching and warm. Thanks also to David Bounie for making this
| fruitful | collaboration | possible. |     |     |     |     |
| -------- | ------------- | --------- | --- | --- | --- | --- |

7
Thank you also to the entire FinTech-SupTech team, Jules, Julien, Lau-
rent, Matthieu, Nicolas, Timothée, Lucasformakingmefeelsowelcome,
to Laurent Dupont for his help on the Robex experiment, and to all the
participants in my user studies at the ACPR for their cooperation and
willingnesstosharetheirexpertise. Workingwithsuchabenevolentand
knowledgeablegrouphasbeenanenrichingexperiencethatsignificantly
contributed to the depth of my research.
To my family and friends, your support and understanding have been
a constant source of encouragement. Benoît, your support has been a
driving force throughout this demanding journey.
Thanks also to Samuel Huron, David Cortés, Jan Gugenheimer and
WendyMackayfortheirvaluableinsightsandconstructivefeedbackthat
have greatly enhanced the rigor and clarity of my dissertation. In addi-
tion, I thank Tim Miller for his very relevant and thorough comments in
his report, and Fosca Giannetti, Alexandre de Streel and Nadia Boukhe-
lifa for their very helpful and constructive feedback.

Contents
1
Abstract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
| Résumé |     |     |     |     |     |     |     | 3   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- |
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
Acknowledgments
|     |     | . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | .   |
| --- | --- | --------- | ------------- | ------------- | ------------- | ------------- | ------------- | --- |
18
List of Figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
| List of Tables |     |               |               |               |               |               |               | 19  |
| -------------- | --- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | --- |
|                | . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . |     |
20
List of Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
| 1 Introduction |     |               |               |               |               |               |               | 21  |
| -------------- | --- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | --- |
|                | . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . |     |
24
1.1 Research scope. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
1.1.1 DefiningAI—notawalkinthepark . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1.1.2 TowardstrustworthyAI—andhumans . . . . . . . . . . . . . . . . . . . . . . . . . . 26
29
1.1.3 HCIandlegalperspectivescollideinthehuman-centricapproach . . . . . . . . . . . . .
1.1.4 Explainability(may)contributetowarrantedtrust . . . . . . . . . . . . . . . . . . . . . 30
31
1.1.5 Explainability(may)contributetolawfulAI . . . . . . . . . . . . . . . . . . . . . . . .
36
1.1.6 Researchdomains. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
| 1.2 Problem  | statement |           |               |               |               |               |               | 38  |
| ------------ | --------- | --------- | ------------- | ------------- | ------------- | ------------- | ------------- | --- |
|              |           | . .       | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | .   |
| 1.3 Thesis   | overview  |           |               |               |               |               |               | 39  |
|              |           | . . . .   | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | .   |
| 1.4 Research | approach  |           |               |               |               |               |               | 41  |
|              |           | . .       | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | .   |
| 1.5 Major    | findings  |           |               |               |               |               |               | 44  |
|              |           | . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | .   |

9
1.6 Academic publications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
2 Background 47
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2.1 A historical perspective on explainability. . . . . . . . . . . . . . . . . . . . . . 47
2.2 Explainability in Computer Science: the toolbox . . . . . . . . . . . . . . . . . 51
2.2.1 Thewiderangeofexplainabilitymethods . . . . . . . . . . . . . . . . . . . . . . . . . . 51
2.2.2 Thetechnicalchallengesingeneratingexplanations . . . . . . . . . . . . . . . . . . . . 55
2.3 Explainability in the Social Sciences: the foundations . . . . . . . . . . . . . 57
2.3.1 Theroleofexplanations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
2.3.2 Theexplanationprocess . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
2.3.3 Explanationsarecontrastive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
2.4 Explainability in HCI: user and context first . . . . . . . . . . . . . . . . . . . . 61
2.4.1 Theneedforuser-centeredexplainability . . . . . . . . . . . . . . . . . . . . . . . . . . 61
2.4.2 Differentaudiences,differentgoals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
2.4.3 Understandinguserneedsincontext . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
2.4.4 Designingexplainabilitysystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
2.4.5 Evaluatingexplainabilitysystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
2.5 Explainability in Law: dreaming in color? . . . . . . . . . . . . . . . . . . . . . 69
2.5.1 Legalrequirementsforalgorithmicexplainability . . . . . . . . . . . . . . . . . . . . . . 69
2.5.2 Legalobjectivesforexplainability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
2.5.3 Isexplainabilitythebestdisinfectant? . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
PART I CALIBRATING TRUST IN EXPLAINABLE AI: COMMON PITFALLS AND
THE PROMISE OF INTERACTIVITY
3 Trust, overtrust, distrust in explainable AI: a cognitive approach 81
.
3.1 Motivation and research questions . . . . . . . . . . . . . . . . . . . . . . . . . . 82
3.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
3.2.1 Trustinautomation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
3.2.2 TrustinautomationbyAIsystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

10
3.2.3 Explanationsarebiasedand(maybe)biasing . . . . . . . . . . . . . . . . . . . . . . . . 86
3.3 Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
3.3.1 Reviewtype . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
3.3.2 Corpuscreation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
3.4 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
3.4.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
3.4.2 Cognitivemechanismsexplanationsshouldadaptto . . . . . . . . . . . . . . . . . . . . 94
3.4.3 WhenexplainableAIleadstoovertrust . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
3.4.4 WhenexplainableAIleadstodistrust . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
3.4.5 WhenexplainableAIismisused . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.4.6 WhenexplainableAIcorrectsfalsebeliefs . . . . . . . . . . . . . . . . . . . . . . . . . 100
3.4.7 Whenexplanationsaremisevaluated . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
3.4.8 Explanationstendtoincreaseunwarrantedtrust . . . . . . . . . . . . . . . . . . . . . 105
3.4.9 Importantfactorsforappropriatetrust: aBayesianapproach . . . . . . . . . . . . . . . 105
3.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
3.5.1 TakeintoaccountcognitivemechanismsandbiasesinthedesignofexplainableAI . . . 107
3.5.2 Clarifythenormalvs. problematicbiaseswithempiricalandnormativework . . . . . . 108
3.5.3 Detailtaxonomiesofusergroupswithcognitivefactors . . . . . . . . . . . . . . . . . 109
3.5.4 Improveourperceptionofusers’reactionstoXAI . . . . . . . . . . . . . . . . . . . . 109
3.5.5 FocusonstrategiesbeyondXAI:contextualization,training,timing,cognitiveforcing... 109
3.5.6 Giveargumentsagainsttheprediction. . . . . . . . . . . . . . . . . . . . . . . . . . . 110
3.6 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
3.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
4 Towards "human-like" explanations: the promise of interactivity 113
4.1 Motivation and research Questions . . . . . . . . . . . . . . . . . . . . . . . . . 114
4.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
4.2.1 InteractivityinHCI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
4.2.2 InteractivityinExplainability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
4.2.3 Interactivityforlearningandsensemaking . . . . . . . . . . . . . . . . . . . . . . . . 118

11
4.3 Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
4.3.1 Reviewtype . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
4.3.2 Corpuscreation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
4.3.3 Analysisandcodingbook . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
4.4 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
4.4.1 Interactivitytypesinexplainability: Select,Mutate,Dialoguewith . . . . . . . . . . . 125
4.4.2 Context,contentandformofinteractiveexplanations . . . . . . . . . . . . . . . . . . 130
4.4.3 Evaluatinginteractiveexplanations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
4.4.4 Interactiveexplanationsincreasetrust,butnotnecessarilyovertrust . . . . . . . . . . 138
4.4.5 Interactiveexplanationsareuseful,butnoteasytouse . . . . . . . . . . . . . . . . . . 140
4.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142
4.5.1 Interactivitycallsformetaexplanations . . . . . . . . . . . . . . . . . . . . . . . . . . 142
4.5.2 Aredialogicexplanationsreallythegrail? . . . . . . . . . . . . . . . . . . . . . . . . . 143
4.6 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
4.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145
PART II COMPLYING WITH REGULATION USING HUMAN-CENTRIC EXPLAINABLE
AI: TWO CASE STUDIES IN FINANCE
5 Empowering customers of robo-advisors with explainability 151
. . .
5.1 Motivation and research questions . . . . . . . . . . . . . . . . . . . . . . . . . 153
5.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
5.2.1 Mitigatingoverrelianceissuesfornonexperts . . . . . . . . . . . . . . . . . . . . . . 154
5.2.2 DesigningvisualisationsofAIexplanationsfornon-expertusers . . . . . . . . . . . . 155
5.2.3 Context: life-insurancedistributionwith"robo-advisors" . . . . . . . . . . . . . . . . 155
5.3 Study 1 Methodology: a market-driven co-design approach . . . . . . . . 158
5.3.1 Systemdesign: Robex,therobo-advisor . . . . . . . . . . . . . . . . . . . . . . . . . . 158
5.3.2 Explanationprototype . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
5.3.3 Co-designsessionsandanalysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163

12
5.4 Study 1 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166
5.4.1 Understandingexplanationneedsfromtwoperspectives . . . . . . . . . . . . . . . . . 166
5.4.2 Redesignprinciplesdrawnfromtheco-designsessions . . . . . . . . . . . . . . . . . . 166
5.5 Study 2 Methodology: A deception-based between-subjects experiment 170
5.5.1 A2x4factorialdesign . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
5.5.2 Surveyprocedureandanalysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
5.6 Study 2 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
5.6.1 Explanationsdonothelptobettercalibratetrust . . . . . . . . . . . . . . . . . . . . . 178
5.6.2 Dialogicexplanationsincreasesubjectivetrust . . . . . . . . . . . . . . . . . . . . . . 179
5.6.3 Dialogicorgraphicalexplanationsdonotimproveuserunderstanding . . . . . . . . . 179
5.6.4 Explanationsdonotaffectcognitiveloadanduserengagement . . . . . . . . . . . . . 179
5.6.5 Higherlevelsofeducationreduceoverreliance. . . . . . . . . . . . . . . . . . . . . . . 180
5.7 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
5.7.1 Dialogicvs. Graphicalexplanations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
5.7.2 Legalrequirementsforfeature-basedexplanations. . . . . . . . . . . . . . . . . . . . . 181
5.8 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
5.9 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
6 Understanding the supervisors’ needs for explainable AI in financial
crime detection 185
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6.1 Motivation and research questions . . . . . . . . . . . . . . . . . . . . . . . . . 186
6.2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188
6.2.1 HCIworkonelicitinguserexplainabilityneeds . . . . . . . . . . . . . . . . . . . . . . 188
6.2.2 DesigningAIjustificationsforcompliance . . . . . . . . . . . . . . . . . . . . . . . . 188
6.2.3 AuditingAIsystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
6.2.4 TheAML-CFTcontext . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
6.3 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192
6.3.1 Scenario-basedsemi-structuredworkshops . . . . . . . . . . . . . . . . . . . . . . . . 193
6.3.2 Empiricallegalresearch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 197

13
6.4 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199
6.4.1 Socio-techno-legalcontextandauditingapproachesofsupervisorsinAML-CFT . . . . 199
6.4.2 WhatprovisionsinAML-CFTlawsdoesAIopacityconflictwith? . . . . . . . . . . . 203
6.4.3 Supervisors’needsformodeljustifiabilityinAML-CFT . . . . . . . . . . . . . . . . . 205
6.5 Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
6.5.1 Theroleofexplanationsforjustifications . . . . . . . . . . . . . . . . . . . . . . . . . 208
6.5.2 Consideringthelimitsofexplanations . . . . . . . . . . . . . . . . . . . . . . . . . . . 209
6.5.3 Supportingmodelperformancemeasurementandtesting . . . . . . . . . . . . . . . . . 210
6.6 Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
6.7 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
7 Discussion 217
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.1 Research contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
7.2 The potential of explanations to manipulate decision-subjects’ trust. . 220
7.2.1 TheSelf-governancefallacy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 220
7.2.2 Thedarkpatternpotentialofexplanations . . . . . . . . . . . . . . . . . . . . . . . . . 221
7.2.3 Safeguardsagainstusermanipulationforcriticalonlinedecisions . . . . . . . . . . . . 221
7.3 Human-centric directions for improved customer empowerment . . . . . 222
7.3.1 Thinkingbeyondinformationaccess . . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
7.3.2 Tailoringexplanationstorelevantusercommunities . . . . . . . . . . . . . . . . . . . 223
7.3.3 Stimulatingskepticism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
7.3.4 Presentingaselectedrangeofoptions . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
7.3.5 Fosteringuserengagement,curiosityandlearning . . . . . . . . . . . . . . . . . . . . 225
7.4 The human-centric way forward for explainability in a highly regulated
environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
7.4.1 AML-CFTillustratesthetensionofusingAIinahighlyregulatedenvironment . . . . 229
7.4.2 Explainabilityisincompleteanduncertain . . . . . . . . . . . . . . . . . . . . . . . . 230
7.4.3 Human-centricexplainabilityalleviatessomeoftheregulatorytensionofblack-boxAI . 231
7.5 Peripheral observations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
7.5.1 Whythefinancialsectorisinterestingforotherhighly-regulatedindustries . . . . . . . 233

14
234
7.5.2 Principlesfordealingwithinterdisciplinarity . . . . . . . . . . . . . . . . . . . . . . .
235
7.5.3 OnexplainabilityforLLMs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7.6 General conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238
| Appendix |     |     |     |     |     |     | 241 |
| -------- | --- | --- | --- | --- | --- | --- | --- |
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
A1. List of cognitive patterns when interpreting explainable AI 241
|     |     |     |     |     |     | . . . . . . . | . . . |
| --- | --- | --- | --- | --- | --- | ------------- | ----- |
B1. Co-design Study Questionnaire . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243
244
B2. The Robex recommendation system. . . . . . . . . . . . . . . . . . . . . . . . . . . .
246
C1. Workshop guide . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
| C2. Compliance | assessment |           |               |               |               |               | 248   |
| -------------- | ---------- | --------- | ------------- | ------------- | ------------- | ------------- | ----- |
|                |            | . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . . . . . | . . . |
251
Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

List of Figures
1 Distribution of my time between different work environments during my PhD, inspired
from [Huron, 2014]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2 Thissaliencymaphighlights(inwhite)thepixelsthatcauseanAImodeltorecognisethis
cat as "cat". Find out more in this article I wrote during my Google internship: . . . . . 6
1.1 John MacCarthy plays chess against a computer in 1967 at Stanford. . . . . . . . . . . . 24
1.2 AI subdisciplines and their relations from [High-Level Expert Group on AI (HLEG), 2018]. 24
1.3 A Geographical Perspective on Explainability. Comparison of keyword searches for "ex-
plainability" and "interpretability" on Google from 2004 to present. Shows that China
only uses "interpretability", while Israel and Viet-Nam only use "explainability". . . . . 30
1.4 Visual representation of the core notions used in this dissertation. We focus on one of the
three pillars defined by the HLEG of trustworthy AI: lawful AI. Specifically, we examine
the role of explanations to support justifications of AI systems with respect to regulations
or regulatory objectives. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
1.5 The concept of warranted trust and the trust relationships explored in this dissertation.
We investigate whether explanations can enhance warranted trust between an individ-
ual subject to an AI decision and the AI system, as well as whether explanations can
contribute to the development of justifications that support warranted trust between a
regulator and the AI system of a regulatee. . . . . . . . . . . . . . . . . . . . . . . . . . 35
1.6 Domain scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
1.7 Topic network of the FAT and Interpretable ML community in [Abdul et al., 2018].. . . . 37
1.8 Overview of the work presented in this dissertation through a modified version of the
triangulation framework of Mackay and Fayard [1997], inspired from [Huron, 2014] . . . 41
2.1 AHistoricalPerspectiveonExplainability. Thebarplot(inred)showstheevolutionofthe
number of academic contributions on XAI. The bubble chart on top displays the number
of citations—represented by size and y-axis—of the most influential papers in XAI. . . . 49
2.2 Distribution of contributions in explainable AI accross disciplines. This graph is based
on a corpus of 5756 articles published from 2015 to present, extracted from searching
"explainab*" in the article title in the Scopus Database. . . . . . . . . . . . . . . . . . . 50
2.3 Categorization of explainable AI methods along four dimensions inspired by Nauta et al.
[2023] and Barredo Arrieta et al. [2020]. . . . . . . . . . . . . . . . . . . . . . . . . . . 51
2.4 Illustrativeexamplesoffeature-basedexplanationsfordifferentdatatypes(image,tabular
and text data) with input saliency [Alammar, 2021, Unruh and Robinson, 2020]. . . . . 52
2.5 Illustration of the gradient-based method to identify "salient" pixels. . . . . . . . . . . . 53
2.6 Figure1in[Tomsettetal.,2018]identifiesthedifferentstakeholdersinamachinelearning
ecosystem. "Direction of arrow indicates direction of interaction." . . . . . . . . . . . . . 62
2.7 ThefourreasonsmotivatingtheneedforexplainableAIpresentedin[AdadiandBerrada,
2018]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

16
2.8 Examples of visual explanations for different AI models a) Hybrid visual and textual ex-
planations for the estimation of the reading time of an article [Szymanski et al., 2021],
b) Influence of features on loan default risk [Chromik et al., 2021], c) Multiple explana-
tions for house price forecasts [Hohman et al., 2019]), d) Example-based explanation for
drawing recognition [Cai et al., 2019]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
2.9 The 12 Explanation quality properties proposed by [Nauta et al., 2023]. . . . . . . . . . . 67
3.1 PRISMA flow diagram [Moher et al., 2009] on how the final corpus was curated (n = 38). 90
3.2 The distribution of the corpus across disciplines. . . . . . . . . . . . . . . . . . . . . . . 92
3.3 Summary of the cognitive constraints, biases and mitigation strategies discussed in the
papers included in our corpus (n=38). . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
3.4 The 38 papers in the corpus and a rough indication of whether the paper reports on over-
ordistrusteffectsofexplanations,onthemisuseofexplanations,oronotherexplanation-
related phenomena. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
4.1 Summary of the role of explanations, the process by which we construct and present
explanations and the biases involved in explanations. . . . . . . . . . . . . . . . . . . . . 114
4.2 Illustrative example of interactive explanation: "Conversational XAI" enables users to
interact with users through natural language. . . . . . . . . . . . . . . . . . . . . . . . . 114
4.3 Illustrative example of interactive, rule-based explanation where users can create and
modify rules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
4.4 PRISMAflowdiagramadaptedfromPageetal.[2021]givinganoverviewofthePRISMA
2020 survey guidelines, used for the search and selection phases of our scoping review. . . 119
4.5 Example of the clarify interaction taken from [Anik and Bunt, 2021]. . . . . . . . . . . . 126
4.6 Examples of the arrange interaction taken from [Hohman et al., 2019] (top) and [Cheng
et al., 2021] (bottom). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
4.7 Examplesofthefilter/focusinteractiontakenfrom[Hohmanetal.,2019](top)and[Ming
et al., 2019] (bottom). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
4.8 Examplesofthereconfigureinteractiontakenfrom[Mingetal.,2019](top)and[Collaris
and van Wijk, 2020] (bottom). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
4.9 Examplesofthesimulateinteractiontakenfrom[Rossetal.,2021](top)and[Chengetal.,
2019] (bottom). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
4.10 Example of the compare interaction taken from [Hohman et al., 2019]. . . . . . . . . . . . 128
4.11 Example of the progress interaction taken from [Melsión et al., 2021]. . . . . . . . . . . . 129
4.12 Examplesoftheanswerinteractiontakenfrom[Melsiónetal.,2021](top)and[Guoetal.,
2022] (bottom). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
4.13 Example of the ask interaction taken from [Melsión et al., 2021]. . . . . . . . . . . . . . . 129
4.14 "Interactive XAI helps users..."
Illustrationofthetaxonomyofinteractioninexplainabilitywithscreenshotsfromthecorpus.130
4.15 Left: Frequency of the interaction categories used in the corpus and frequency of their
combinations ; Middle: Percentage of studies using an explanation representation per
interaction category; Right: Percentage of studies focusing on a type of user question per
interaction category/ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
4.16 Thefirstpartoftheconceptmatrix[WebsterandWatson,2002],reportingtheexplanation
context and content. The design of this concept matrix was inspired from [Bae et al., 2022].133
4.17 The second part of the concept matrix, reporting the explanation communication and
evaluation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134

17
4.19 Left: Count of the positive, negative and neutral quantitative evaluations of interactive
explanations compared to static ones, against various user-based metrics, based on 9 dif-
ferent studies. Right: Count of the different evaluation outcomes in the empirical studies
comparing interactive explanations with no explanation as a baseline, extracted from 13
different papers in the corpus. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139
5.1 Fictional life-insurance plans proposed by Robex, the explainable robo-advisor developed
for this study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 159
5.2 ScreenshotoftheRobexinterface,showingtheprofilingquestionnairestageatthestartof
the user journey. Translated from French to English. . . . . . . . . . . . . . . . . . . . . 160
5.3 ScreenshotoftheRobexinterface,showingtherecommendationstage. Asrequiredbylaw,
a summary of the user’s profile is displayed first, followed by a life-insurance contract
proposal with details. The explanation is presented on the same page, just after the proposal.160
5.4 Screenshot of the Robex interface, showing the answers it provided for test questions on
participants’ financial knowledge. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162
5.5 Screenshot of the feature-based explanation prototype for Robex. In orginial language
(French). Individual factors that decrease investment risk are shown on the left in de-
scending order of importance and factors increasing investment risk are on the right. . . . 164
5.6 ExplanationinterfacesforeachoftheconditionA"Graphical-static": usersseeagraphical
summary of how their characteristics impact the risk of the proposal. Translated from
French to English. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
5.7 ExplanationinterfacesforeachoftheconditionB"Graphical-mutable": usersfirstseethe
graphical-static interface and then a pop-up message indicates they can change some of
their characteristic. Translated from French to English. . . . . . . . . . . . . . . . . . . . 172
5.8 Explanation interfaces for each of the condition C "Dialogic": the same information pro-
vided in the interfaces A and B)is delivered through "sms-like" textual messages. Some
graphicsareaddedtofacilitatethevisualisationoftheriskandofthevariablesdecreasing
and increasing the risk of the proposal. Translated from French to English. . . . . . . . . 173
5.9 Explanationinterfacesexamplesforanincorrectrecommendationforeachofthethreecon-
ditions: A’ "Graphical-static"; B’ "Graphical-mutable"; C’ "Dialogic". The correct user
profile in this case would have been "Secure", but the skewed Robex algorithm outputs
"Dynamo". Only A’ is translated from French to English, the rest are in original language.174
5.10 The workflow of our quantitative experiments. The profiling questionnaire is used to
produce a personalized recommendation of a life-insurance contract. Clients can review
the recommendation, the explanation and then decide to follow the recommendation or not. 176
5.11 Results for Study 2. Vertical lines represent the 95% confidence interval. Asterisks
and dots indicate the statistical significance of the results: *** p-value≤0.001, ** p-
value≤0.01, * p-value≤0.05, • p-value≤0.07, "ns" non significant. . . . . . . . . . . . . 178
5.12 Effectsofeducationonreliance,understandingoftherecommendationandoftheexplanation.180
6.1 Scenarios used during the workshops with supervisors, with a description of the two use
cases of AI in AML-CFT, and two examples of alerts that were generated or closed by the
AI-enhanced systems. Only one of these case studies was presented in each workshop. . . 194
6.2 Conceptual justifications shown for the scenario 2 and its example alert. Conceptual
justifications for the scenario 1 followed the same format. . . . . . . . . . . . . . . . . . . 195
6.3 Summary of the workshops, with socio-techno-legal context of supervisors, supervisors’
questions on AI, AI auditing approaches ideas and ideas for justifications and explanations.199
6.4 Flow diagram of the supervisor’s control procedures in AML-CFT . . . . . . . . . . . . . 202

18
7.1 Explanation interface to engage users cognitively and stimulate their curiosity. First, a
brief explanation of Robex is given: a); second, the user answers several multiple choice
questions that lead them to question the impact of some features: b) and c); third, the full
graphical explanation is given. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 228

List of Tables
2.1 The different classifications of audiences, goals, explanation content, explanation timing
and contexts presented in the XAI literature. . . . . . . . . . . . . . . . . . . . . . . . . 64
3.1 Coding book used for the analysis of the corpus. . . . . . . . . . . . . . . . . . . . . . . . 92
4.1 Codebook used to retrieve information from the corpus with four dimensions: [explana-
tion]context,content,communicationandevaluation,theircorrespondingsub-dimension
and reference from which codes were inspired from. . . . . . . . . . . . . . . . . . . . . . 123
4.2 Two-level taxonomy of interactivity techniques in XAI, including a first level reflecting
the type of support interaction techniques provide to the cognitive process of explaining,
a second task-oriented level, and corresponding definitions. . . . . . . . . . . . . . . . . . 126
5.1 Question used in the Robex’s profiling questionnaire for measuring users’ personal char-
acteristics (translated from French to English). . . . . . . . . . . . . . . . . . . . . . . . 161
5.2 Mainthemesemergingfromthecontentanalysisofsupervisorsandend-usersinterviews,
with corresponding lexical field and citations. . . . . . . . . . . . . . . . . . . . . . . . . 167
5.3 Question used for measuring different metrics with Cronbach alphas (translated from
French to English). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175
6.1 Description of role, experience, familiarity with AI of participants in the study. . . . . . . 213
6.2 Data used for the empirical legal research . . . . . . . . . . . . . . . . . . . . . . . . . . 214
6.3 Summary of supervisors’ needs for model justifiability, corresponding description, model
concerned and developer of justifications/explanations, and justification and explanation
design ideas that emerged during the workshops. . . . . . . . . . . . . . . . . . . . . . . 215

| List | of  |     | Important |     |     |     |     | Defi- |     |     |
| ---- | --- | --- | --------- | --- | --- | --- | --- | ----- | --- | --- |
nitions
| 1 1          |     |              |           |     |     |         |       |     |           | 24  |
| ------------ | --- | ------------ | --------- | --- | --- | ------- | ----- | --- | --------- | --- |
| . Artificial |     | Intelligence | (McCarthy |     | and | Minsky, | 1956) | .   | . . . . . | .   |
1 . 2 AI system (OECD, 2023) . . . . . . . . . . . . . . . . . . . . . . 25
| 1 3           |     |     |       |         |       |         |       |         |           | 26  |
| ------------- | --- | --- | ----- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . Trustworthy |     | AI  | . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
1 . 4 Trust . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
1 . 5 Warranted trust . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
| 1 6     |             |     |       |         |       |         |       |         |           | 28  |
| ------- | ----------- | --- | ----- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . Trust | calibration |     | . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
1 . 7 Overtrust and Distrust . . . . . . . . . . . . . . . . . . . . . . . 28
| 1 8             |     |     |               |         |       |         |       |         |           | 29  |
| --------------- | --- | --- | ------------- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . Overreliance  |     | or  | Underreliance |         | . .   | . . . . | . . . | . . . . | . . . . . | .   |
| 1 9             |     |     |               |         |       |         |       |         |           | 29  |
| . Human-centric |     |     | AI . .        | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
1 . 10 Explanation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
| 1 11             |     |     |         |         |       |         |       |         |           | 30  |
| ---------------- | --- | --- | ------- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . Explainability |     |     | . . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
| 1 12 Explainable |     | AI  | (XAI)   |         |       |         |       |         |           | 30  |
| .                |     |     |         | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
1 . 13 Interpretable AI . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
| 1 14         |     |     |         |         |       |         |       |         |           | 32  |
| ------------ | --- | --- | ------- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . Regulation |     | . . | . . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
1 . 15 Audit, auditability . . . . . . . . . . . . . . . . . . . . . . . . . . 33
| 1 16             |     |     |         |         |       |         |       |         |           | 33  |
| ---------------- | --- | --- | ------- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . Accountability |     |     | . . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
| 1 17             |     |     |         |         |       |         |       |         |           | 34  |
| . Justification  |     | .   | . . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
3 . 1 Complacency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
| 3 2          |     |        |       |         |       |         |       |         |           | 83  |
| ------------ | --- | ------ | ----- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . Automation |     | bias   | . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
| 3 3          |     |        |       |         |       |         |       |         |           | 87  |
| . Cognitive  |     | biases | . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
4 . 1 Perceived usability . . . . . . . . . . . . . . . . . . . . . . . . . . 136
| 4 2         |     |            |     |         |       |         |       |         |           | 136 |
| ----------- | --- | ---------- | --- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . Perceived |     | usefulness | .   | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
7 . 1 Dark patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
| 7 2         |            |       |         |         |       |         |       |         |           | 225 |
| ----------- | ---------- | ----- | ------- | ------- | ----- | ------- | ----- | ------- | --------- | --- |
| . User      | engagement |       | . .     | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
| 7 3         |            |       |         |         |       |         |       |         |           | 226 |
| . Curiosity |            | . . . | . . . . | . . . . | . . . | . . . . | . . . | . . . . | . . . . . | .   |
7 . 4 RegTech . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234

| Chapter |     | 1   |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Introduction
“High-risk AI systems shall be designed and developed in such
a way to ensure that their operation is sufficiently transparent
| to enable | users | to  | interpret | the | system’s | output and | use | it  |     |
| --------- | ----- | --- | --------- | --- | -------- | ---------- | --- | --- | --- |
appropriately. An appropriate type and degree of transparency
shall be ensured, with a view to achieving compliance with the
| relevant | obligations |     | of the | user | and of | the provider.” |     |     |     |
| -------- | ----------- | --- | ------ | ---- | ------ | -------------- | --- | --- | --- |
ProposalfortheAIAct,April,21st,2021
| is hype | today | 2023 |     |            |               |            |       |     |     |
| ------- | ----- | ---- | --- | ---------- | ------------- | ---------- | ----- | --- | --- |
| AI      |       | .    | was | Generative | AI’s breakout | year, with | Chat- |     |     |
1
GPTandMidjourney generatingsignificantexcitementaroundperfectly 1Models
like ChatGPT
credible presidential speeches produced in a few seconds or videos of or MidJourney, which
|     |     |     |     |     |     |     |     | create text or | images |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------ |
teddy bears skating. However, AI’s large scope of benefits, from per-
fromprompts,arecalled
sonalized movie recommendations to the detection of cancerous lesions
|     |     |     |     |     |     |     |     | “generative AI”. | https: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------ |
in medical imaging, comes with risks. Public and expert opinions have
//chat.openai.com/
expressed concerns about AI taking over human jobs, people gradually AccessedJanuary2024.
losing skills, or privacy and fundamental rights being violated by AI
|                      |     |     | 2023    | 2021 |                              |     |     |     |     |
| -------------------- | --- | --- | ------- | ---- | ---------------------------- | --- | --- | --- | --- |
| decisionsystems[Cui, |     |     | ,Zhang, |      | ]. Notably,theuseofAIinauto- |     |     |     |     |
mated settings has fueled concerns about AI replacing humans, and the
need for keeping humans in control for important decisions. In a recent
2023
survey, [Tyson and Kikuchi, ] highlighted that Americans’ concern
| about AI | in daily | life outweighed |     | excitement. |     |     |     |     |     |
| -------- | -------- | --------------- | --- | ----------- | --- | --- | --- | --- | --- |
Many concerns arise from the complexity and opacity of some AI
|     |     |     |     |     | 2   |     |     | 2Deeplearningisasub- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- |
models, and more specifically deep learning . While we know the math-
ematical operations that occur in perceptrons, units of neural networks set of machine learn-
|     |     |     |     |     | 2014 |     |     | ing which involves | neu- |
| --- | --- | --- | --- | --- | ---- | --- | --- | ------------------ | ---- |
inspired by brain neurons [Cox and Dean, ], we do not understand
ralnetworkswithmulti-
why, when put together, they result in the behavior we observe [An-
|     | 2023 |     |     |     |     |     |     | plehiddenlayers. |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
thropic, ]. The scale of the data on which these models are trained,
|     |     |     |     |     |     | 3   |     | 3GPT-4, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
and the massive number of parameters that compose them makes them for example,
unintelligible to humans. Like the human brain, we have a good under- has 1.7 trillion parame-
ters.
standing of its component units, such as synapses, and how they com-
municate with each other, but we cannot fully explain the results they
produce [Anthropic, 2023 ]. Sophisticated machine learning models, es-
pecially generative ones, are often considered as "black-boxes". They can

| 22 the | explanation | paradox |     | and the | human | centric | path |     |     |
| ------ | ----------- | ------- | --- | ------- | ----- | ------- | ---- | --- | --- |
-
provide very accurate predictions, but it is unclear how they arrive at
those conclusions.
The emergence of deep learning models in 2012 [Krizhevsky et al.,
2012 , LeCun et al., 2015 ] and more recently, transformers [Vaswani et al.,
| 2017  |            |         |         |       |              |          | 2021 |     |     |
| ----- | ---------- | ------- | ------- | ----- | ------------ | -------- | ---- | --- | --- |
| ] and | generative | AI, has | brought | us in | what Melanie | Mitchell | [    | ]   |     |
describes as an "AI spring", a period of massive investment and opti-
mism in AI. This "race to AI" has led to a "race to regulation" [Smuha,
2021
| ]. Regulatory |     | efforts | to prevent | the harmful |     | effects of | AI systems |     |     |
| ------------- | --- | ------- | ---------- | ----------- | --- | ---------- | ---------- | --- | --- |
have multiplied in recent years, the results of which are only now start-
ing to emerge. In Europe, the proposal for the regulation of AI in the
2021
| EuropeanUnion(the"AIAct")[EuropeanCommission, |     |     |     |     |     |     | ],whichsets |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
out requirements for AI applications considered as "high risk" will re-
quire thorough certification mechanisms for machine learning systems
consideredas"highrisk". Chinahasalsoadoptedasetofregulationsfol-
lowing its "Next Generation AI Development Plan" [Zheng and Zhang,
| 2023 | 20174 |     |     |     |     |     |     | 4This |     |
| ---- | ----- | --- | --- | --- | --- | --- | --- | ----- | --- |
]in . IntheUnitedStates,themostrecentfederalregulatoryef- plan includes
fortconsistsoftheWhiteHouseexecutiveorderonAI[TheWhiteHouse, the 2022 "Adminis-
| 2023      |      |            |     |             | 5   |                |           | trative   | Provisions on |
| --------- | ---- | ---------- | --- | ----------- | --- | -------------- | --------- | --------- | ------------- |
| ], laying | down | principles | for | responsible | AI  | . In parallel, | questions |           |               |
|           |      |            |     |             |     |                |           | Algorithm | Recommen-     |
ariseaboutthecomplianceofAIsystemswithexistingregulatoryframe-
|     |     |     |     |     |     |     |     | dation" | [Zheng and |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- |
works,particularlyinhighlyregulatedareaswithwell-establishednorms 2023]
|     |     |     |     |     |     |     |     | Zhang, | and the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- |
2019
| [Mittelstadt | et al., | ].  |     |     |     |     |     | world’s first | Generative |
| ------------ | ------- | --- | --- | --- | --- | --- | --- | ------------- | ---------- |
AIRegulationpublished
inAugust2023.
A key objective of regulation is to protect end users and citizens from
5Additionally,
tenstates
various detrimental consequences such as being deceived, being dis-
|     |     |     |     |     |     |     |     | have regulated | the use |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------- |
criminated against, or suffering from algorithmic errors. As a result,
|     |     |     |     |     |     |     |     | of AI, | including hir- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- |
many of the AI policies detailed above present transparency as a cen- ing and profiling al-
|     |     |     |     |     |     |     |     | gorithms, | as part of |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- |
traltheme. Someexisting,sector-specific,regulatoryframeworksalready
impose obligations to explain an algorithmic prediction to the end user. broader consumer pri-
|     |     |     |     |     |     |     |     | vacy laws | [Katrina Zhu, |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- |
Thisisthecase,forexample,inthecontextofprotectingcustomersofon- 2023].
line life insurance recommendation systems. In other situations, the use
ofmachinelearningmodelsinregulatedenvironmentsrequiresexplana-
tionsaddressedtoregulatorsinchargeofverifyingthecomplianceofthe
system. Shedding light on the complex inner workings of AI models has
been the subject of an entire field of research called explainability (XAI),
whichhasgainedconsiderableinterestoverthelastfiveyears. Inparticu-
lar,theresearchandpolicycommunitieshavebecomeincreasinglyaware
of the importance of "human-centric" design of AI explanations. How-
ever, little attention has been paid so far to the human-centric design of
explanations in view of demonstrating compliance with applicable regu-
lation and ensure "lawful AI" [High-Level Expert Group on AI (HLEG),
2018 ].
In this thesis, we show through literature reviews and experiments
in the context of life-insurance online distribution that AI explanations
can have the paradoxical effect of increasing user trust, including un-
warranted trust. Instead of empowering them, explanations can make
non-expert users more vulnerable. This may undermine the regulatory
objectives to inform and "enlighten" customers about the AI-based de-
cisions being made about them. We also identify the different ways in

introduction 23
which explanations can lead AI users to overtrust, distrust, or misun-
derstand the system. Additionally, we investigate the effects of more
interactive "human-like" explanations that could avoid the identified pit-
falls. WearguethatbettereffortscanbemadetocreatemoreeffectiveAI
explanations through the human-centric approach, by supporting user
engagement, curiosity and learning.
We also discuss how explainability can contribute to building justifi-
able trust of AI stakeholders, including regulators, in the context of anti-
money laundering and countering terrorism financing (AML-CFT). The
success of explainability for regulators will depend on taking a human-
centredapproachdesignedtoavoidhumanbiasesandadapttothesocio-
technicalfeaturesofthiscontext. Wehighlightthatcurrentexplainability
methods have severe limitations and may contribute to an unjustified
sense of certainty about AI systems’ behavior. However, human-centric
explainability can still help alleviate the tensions created by the use of
black-box AI systems in AML-CFT by contributing to justifiability and
accountability.

| 24 the | explanation | paradox | and | the human | centric path |     |     |
| ------ | ----------- | ------- | --- | --------- | ------------ | --- | --- |
-
| 1.1 Research |     | scope |     |     |     |     |     |
| ------------ | --- | ----- | --- | --- | --- | --- | --- |
This section outlines some key terms and ideas necessary to under-
stand the scope and motivation of this dissertation. It then details the
| research | domains in | which it falls. |            |        |      |     |     |
| -------- | ---------- | --------------- | ---------- | ------ | ---- | --- | --- |
| 1.1.1    | Defining   | AI —            | not a walk | in the | park |     |     |
1996
AI is a broad church [Boden, ]. There may exist as many defini-
tionsastherearepeoplewhouseit[Smuha, 2021 ]. Oneworking,illustra-
tive definition was given by John McCarthy of MIT and Marvin Minsky
1.1:
|     |     |     |     | 1956 |     | Figure | John Mac- |
| --- | --- | --- | --- | ---- | --- | ------ | --------- |
of Carnegie-Mellon in the context of the Dartmouth College. They
|         |        |     |     |     |     | Carthy  | plays chess   |
| ------- | ------ | --- | --- | --- | --- | ------- | ------------- |
| defined | AI as: |     |     |     |     |         |               |
|         |        |     |     |     |     | against | a computer in |
1967atStanford.
Definition
Artificial Intelligence (McCarthyandMinsky,1956). Theconstruc-
tion of computer programs that engage in tasks that are currently more sat-
isfactorilyperformedbyhumanbeingsbecausetheyrequirehigh-levelmental
processessuchas: perceptuallearning,memoryorganizationandcriticalrea-
| soning" | [Council of | Europe, 2023]. |     |     |     |     |     |
| ------- | ----------- | -------------- | --- | --- | --- | --- | --- |
For example, playing chess, driving a car, translating, are examples of
tasksthatrequirecomplexacquisitionandreasoningprocessesincluding
vision, spatial awareness, judgment [Surden, 2019 ], and which AI was
| being programmed |     | to achieve. |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | --- | --- | --- | --- |
The decades between 1950 and 1990 were the years of fundamental
6
advancesinneuralnetworks and"symbolicartificialintelligence"which
was based on knowledge and reasoning representation. Expert systems
1.2:
|     | 1980 |     |     |     |     | Figure | AI subdis- |
| --- | ---- | --- | --- | --- | --- | ------ | ---------- |
built in the s mirrored human logic in their "inference engine" and
|     |     |     |     |     |     | ciplines | and their rela- |
| --- | --- | --- | --- | --- | --- | -------- | --------------- |
marked the golden age of symbolic AI. In the 2010 s, access to massive
|     |     |     |     |     |     | tions from | [High-Level |
| --- | --- | --- | --- | --- | --- | ---------- | ----------- |
amounts of data and the development of powerful processors made it Expert Group on AI
(HLEG),2018].
possible to fully exploit the ideas previously developed on neural net-
6Neural
works[CouncilofEurope, 2023 ]. Insteadofcodinghuman-drivenlogical networks were
|     |     |     |     |     |     | invented | much earlier |
| --- | --- | --- | --- | --- | --- | -------- | ------------ |
rules in computers, the neural network or machine learning approach
|           |                 |          |       |               |              | than the | AI boom of   |
| --------- | --------------- | -------- | ----- | ------------- | ------------ | -------- | ------------ |
| relied on | letting systems | discover | rules | by themselves | in the data. |          |              |
|           |                 |          |       |               |              | 2012.    | For example, |
Itisgenerallyconsideredthatfourtypesofmachinelearningexist: su- the idea of the ReLU
|     |     |     |     |     |     | function | was presented |
| --- | --- | --- | --- | --- | --- | -------- | ------------- |
pervised, semi-supervised, unsupervised, and reinforced learning. Fol-
1969
lowingGhahramani[ 2004 ]’sdefinitions,"insupervisedlearningthemachine in by Fukushima,
backpropagationwasin-
is given a sequence of desired outputs y1, y2,..., and the goal of the machine is
|     |     |     |     |     |     | vented in | 1970 by Lin- |
| --- | --- | --- | --- | --- | --- | --------- | ------------ |
to learn to produce the correct output given a new input.". In unsupervised nainmaa,LSTMwerein-
learning, however, "the machine simply receives inputs x1, x2,. . ., but [does troducted in 1995 by
not] obtain supervised target outputs". For instance, clustering is a com- Hochreiter and Schmid-
mon unsupervised learning technique where the machine finds groups huber, etc. [Hochreiter
1997,
and Schmidhuber,
of data that share similarities. In semi-supervised learning, the machine
Mülleretal.,1995]
1 2
generates its own targets y , y ,... to "supervise itself". In reinforcement
learning the machine gets rewards whenever its forecast or behavior is
correct.
From this historical perspective, artificial intelligence encompasses all
systems designed to imitate, match or surpass problem solving skills

introduction 25
of the human brain, from symbolic AI, to machine and deep learning
or robotic systems. While illustrative, this definition carries the risk of
mistakingAIforactuallyintelligent,thinking,orevensentient,machines
2021 2019 2019
[Mitchell, , Surden, ]. Surden [ ] argues that it is essential to
understandwhatAIisnot,emphasisingthatthecomputationalprocesses
it employs are nothing like human thinking: "AI systems are often able to
produce useful, intelligent results without intelligence".
AImustthereforebedefineddifferentlyfromtheobjectiveofmatching
or surpassing human intelligence, which is either evasive, speculative or
even misleading. Recent attempts at aligning AI policy have provided
alternative definitions that offer a functional, rather than intentional de-
2019
scription,basedonthecapabilitiesthatAIsystemsdemonstrate. In ,
theOECDproposedadefinitionforAIsystemsinthe"Recommendation
38
of the Council on Artificial Intelligence", that was adopted by coun-
tries. The definition was amended on November,
8th, 2023
:
Definition
AI system (OECD, 2023). A machine-based system that, for explicit or
implicit objectives, infers, from the input it receives, how to generate outputs
suchaspredictions,content,recommendations,ordecisionsthatcaninfluence
physical or virtualenvironments. Different AI systems varyin their levels of
autonomy and adaptiveness after deployment [OECD, 2019].
2021
The AI Act [European Commission, ] considers a similar definition
of AI systems in Article 3 "Definitions" 7 . 7It also draws on the
definition proposed by
the High-Level Expert
However, defining AI in legal terms has proven difficult, giving rise Group in 2018 [High-
towide-rangingpoliticaldiscussionsandacademicdebates. Someschol- Level Expert Group on
ars have argued that agreeing on a single definition of AI was unfeasible
AI(HLEG),2018].
2018 2023 2023
[Reed, ], or even undesirable [Schuett, ]. Schuett [ ] con-
tends that policy makers should not use the term AI, which does not
comply with common requirements for legal definitions. These require-
ments stem from general legal principles of democratic countries, such
as the principle of proportionality, effectiveness, legal certainty or the
vagueness doctrine. With regard to these principles, Schuett argues that
artificial intelligence is too vague, over-inclusive, unpractical, imprecise
and unintelligible of a term to be used as a legal definition.
Aware of all of these difficulties to delineate the scope of AI, this dis-
sertation nonetheless focuses on algorithmic systems that fit the second
definition provided above. In the first part of the dissertation, we will
be particularly interested in how these systems "influence" their envi-
ronment, and more specifically human operators, when used as decision
aids. In the second part, we will narrow our focus to AI systems used in
finance. The first use case is an expert system providing recommenda-
tions for life-insurance contracts. The second use case explores different
types of machine learning systems, supervised and unsupervised, to de-
tect money laundering and terrorism financing.

| 26 the | explanation | paradox | and the | human centric | path |     |     |
| ------ | ----------- | ------- | ------- | ------------- | ---- | --- | --- |
-
| 1.1.2 | Towards | trustworthy | AI — | and humans |     |     |     |
| ----- | ------- | ----------- | ---- | ---------- | --- | --- | --- |
Against a backdrop of surging investments and competition in AI, re-
8
search has shown that AI could cause harms, intended or not , such 8AI
|     |     |     |     |     |     | harms | studied |
| --- | --- | --- | --- | --- | --- | ----- | ------- |
as discrimination, wrongful arrests, spreading of fake-news, defamatory in such research are
|     |     |     | 2021 |     |     | mainly not | human- |
| --- | --- | --- | ---- | --- | --- | ---------- | ------ |
deep-fakes, among others [Acemoglu, ]. In response to AI-specific
intended,howeversome
risks, a multitude of ethical principles for AI have emerged. A notable
|     |     |     |     |     |     | are direct consequences |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- |
success in aligning different stakeholders at scale was achieved with of poor AI devel-
|     |     |     | 2019 |     | 46  |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- |
the OECD principles developed in and endorsed by countries opment choices and
[OECD, 2019 ]. The OECD proposed ten principles for AI, which repre- optimizationobjectives.
sent a set of priorities to reflect democratic values in AI policies, such
as protecting human rights, equity, or establishing stakeholder account-
ability. A similar early attempt at characterizing desirable AI properties
2019
comes from the Guidelines for Trustworthy AI by the HLEG [High-
Level Expert Group on AI (HLEG), 2019 ]. The guidelines propose seven
key requirements that AI systems should meet to be considered trust-
worthy: human agency and oversight, technical robustness and safety,
privacy and data governance, transparency, diversity, societal and envi-
ronmental well-being, and accountability. The guidelines were influen-
tial in the drafting of the AI Act [European Commission, 2021 ]. Other
initiatives include the trustworthiness framework for AI proposed by the
International Organization for Standardization (ISO) [International Or-
ganization for Standardization (ISO), 2022 ] or the National Institute of
Standards and Technology’s (NIST) Method for Evaluating User Trust in
2023
| AIsystem[NIST, |     | ]developedintheU.S.Theaforementionedefforts |     |     |     |     |     |
| -------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
areamongthemostinfluentialones, butmanyotherframeworks, ethical
guidelines, principles for AI have been proposed by either international,
governmental, or private organizations [Kaur et al., 2022 , Jobin et al.,
2019 ].
Overall, two umbrella terms have emerged, "Responsible" or "Trust-
worthy" AI, to embody the ethical and safe use of AI. The former was
used mainly by private organisations, and possibly comes from the Cor-
porate Social Responsibility (CSR) culture where the notion of responsi-
| bility and | accountability | are predominant. |     |     |     |     |     |
| ---------- | -------------- | ---------------- | --- | --- | --- | --- | --- |
The term trustworthy AI has emerged as a comprehensive objective for
AI systems. It was promoted by the EU strategy for AI [European Com-
2023 2017
| mission, | ] in | , the OECD | principles, | the ISO and | NIST frame- |     |     |
| -------- | ---- | ---------- | ----------- | ----------- | ----------- | --- | --- |
works, among others, and places trustworthiness as a higher, ultimate
value. The High-Level Expert Group on AI give three conditions for AI
systems to be trustworthy: they should be lawful, ethical and robust (cf.
|     | 14  |     |     | 2019 |     |     |     |
| --- | --- | --- | --- | ---- | --- | --- | --- |
Figure . ) [High-Level Expert Group on AI (HLEG), ] . According
2022
| to Kaur | et al. [ | ]’s review: |     |     |     |     |     |
| ------- | -------- | ----------- | --- | --- | --- | --- | --- |
Definition
Trustworthy AI. is a framework to ensure that a system is worthy of be-
ingtrustedbasedontheevidenceconcerningitsstatedrequirements. Itmakes
sure that the users’ and stakeholders’ expectations are met in a verifiable way
| [Kaur | et al., 2022]. |     |     |     |     |     |     |
| ----- | -------------- | --- | --- | --- | --- | --- | --- |

introduction 27
The HLEG’s decision to concentrate on the concept of trust is under-
standable. Trust is pillar of our society and lives. It determines our inter-
actions with people, institutions, organizationsand machines. Many dis-
tinct conceptual visions of trust have been proposed through the lenses
of philosophers, economists or psychologists. In the context of trust in
2019
AI, we retain one proposed by Danks [ ] for the remainder of this
dissertation, which focuses on the functional value of trust:
Definition
Trust. Condition in which "the user has a reasonable belief that the system
(whetherhumanormachine)willbehaveapproximatelyasintended"[Danks,
2019].
2021
Thedefinitionisinlinewiththeonegivenin[Jacovietal., ]. Follow-
2004 2021
ing [Lee and See, ], Jacovi et al. [ ]’s model of trust also incorpo-
ratesthedimensionofvulnerability: "trustisanattempttoanticipatethe
impactofbehaviorunderrisk". Inthecaseofhuman-AItrust, theuseris
vulnerabletotheriskoftheAIbeingwrong. Trustmakesherbelievethat
the risk is low. This risk-taking element is present in other definitions of
trust in the literature [Mayer et al., 1995 , Glikson and Woolley, 2020 ] 9 . 9Mayer et al. [1995]
explain that trust im-
The core value of trust is to enable cooperation [Hardin, 2006 ]. Trust plies"takingameaning-
2006 ful risk while believing
makes social cooperation easier and even possible [Hardin, ]. It
inahighchanceofposi-
also enables cooperation between people and technology [Jacovi et al.,
tiveoutcome".
2021 2022 2021
, Ferrario and Loi, , Chatila et al., ], in part because we
often apply the same social norms of interaction with machines as we
2019
do with humans [Miller, ]. Consequently, trustworthy AI ultimately
aims to enable and improve human-AI cooperation, or collaboration which
2021
oneobjectiveofhuman-computerinteractionresearch[Jacobsetal., ,
2020
Khadpe et al., ]. This enriched collaboration between humans and
AI systems can also be framed as enhanced decision-making. In criti-
2021
cal applications such as healthcare, finance, justice, Chatila et al. [ ]
contends that really useful AI systems make it possible for human deci-
sion makers to take decisions that are more informed, as free of bias as
possible and "ultimately better".
TheconceptoftrustworthyAIissubject,however,tocontroversy. Crit-
ics mainly point to the fact that trustworthy AI and other expressions
suchasresponsibleAIoraccountableAIcanobscureanecessary,activerole
2018
for humans, and pose the wrong questions. Joanna Joanna Bryson [ ]
argues that trust can only be deferred to peers (other human beings),
2018 2021
and not to machines [Joanna Bryson, , Smuha, ]. As physical
and legal entities, humans are the ones who should be "responsible" and
2020
"accountable" for AI systems, not AI. Marisa Tschopp [ ] advances
that tech companies should ask themselves "How can we be trustwor-
thy?" rather than "How can we we increase trust in AI?". Additionally,
some note that the idea of trust, in its philosophical meaning, involves
delegating control, in this case to the machine, without the need for su-
2021 2020
pervision [Smuha, , Ferrario et al., ]. In fact, due to the opaque
nature of machine learning models, AI stakeholders are likely to have to

28 the explanation paradox and the human centric path
-
trust an AI system without a complete understanding of its underlying
2022
algorithms. Ferrario and Loi [ ] even propose an account of trust as
"anti-monitoring", as it goes against the idea of complete comprehensi-
2004
bility and control. As Lee and See [ ] note:
"Trustguidesreliancewhencomplexityandunanticipatedsituationsmakeacomplete
understandingoftheautomationimpractical".
[LeeandSee,2004],(p. 50).
However,inmostsituations,itisnotdesirablethatpeopleblindlytrust
so-called"trustworthy"AIsystems. Rather,thegoalistohaveresponsible
usersabletocalibratetheirtrustbyrelyingontangibleinformationabout
the system, provided by measures such as transparency, explainability,
2022 2006
safety tests, uncertainty metrics [Kurz et al., ], etc. Hardin [ ]
states "I am likely to trust you when you have given some evidence of being
trustworthy". Jacovi et al. [ 2021 ] note that trustworthiness and trust are
two entirely disentangled concepts. Trust can exist for an untrustworthy
system and vice-versa.
Definition
Warranted trust. Trust is warranted when it is caused by trustworthi-
ness (to some contract, defined for example by the HLEG’s key requirements
fortrutworthyAI).Intheoppositecase,itisunwarranted[Jacovietal.,2021],
or misplaced.
10This model of trust
2020 poses the reduced level
Ferrario et al. [ ] define "paradigmatic trust" as the disposition of in-
of monitoring as an im-
dividualstorelyonanAIsystemwithoutmonitoring,buthavingformed
portant characteristic of
beliefs about the system’s trustworthiness, through evidence of its reli- trust. However, we see
ability 10 . Ferrario and Loi [ 2022 ] present paradigmatic trust as justified the reduced levels of
monitoring as a conse-
and warranted trust. We use hereinafter the terms warranted [Jacovi et al.,
2021 ], justified [Ferrario and Loi, 2022 ] or appropriate trust as synonyms quence of trust and not
a defining characteristic
2019
[Gunning and Aha, ]. oftheconcept.
In this dissertation, we focus on the impact of explanations of AI sys-
tems on users’ warranted trust. This amounts to studying the process of
calibrating trust.
Definition
Trust calibration. The process of assigning a level of trust to a system
based on its performance, capabilities and behaviour [Culley and Madhavan,
2013].
Inappropriate trust calibration may lead to overtrust, distrust, overre-
liance or underreliance, i.e. misplaced or inappropriate trust. We use here-
inafter the following definitions for these terms:
Definition
Overtrust and Distrust. As an excessive or insufficient level of sub-
jectivetrust. Subjectivetrustmeasurestheparticipants’subjectivereportsof

introduction 29
trustinthe(X)AIsystem(alsocalledperceivedtrust)[BagheriandJamieson,
2004, Miller, 2022].
Definition
Overreliance or Underreliance. An excessive or insufficient level of
demonstrated trust. Demonstrated trust, or reliance, refers to the propen-
sity of participants to follow and accept the advice or prediction of an (X)AI
system [Miller, 2022].
1.1.3 HCIandlegalperspectivescollideinthehuman-centric
approach
A crucial element of this trust calibration process is human behaviour
in the context of receiving AI predictions. Developing trustworthy AI
requires understanding the factors and mechanisms in human-AI inter-
2021 2019
actions that contribute to building trust [Jacovi et al., , Danks, ].
Worktoadvanceinthisdirectionmustthereforeadoptahuman-centered
approach. Thisendeavourhasbeencharacterizedashuman-centricAI in
2020 2023
recent literature [Shneiderman, , Maxwell and Dumas, , Bryson
2019
and Theodorou, ].
Definition
Human-centric AI. This approach places people and users at the centre
ofthedevelopmentofAI[EuropeanCommission,2019]. Itpromotesthestudy
of AI users in context, to understand their needs. The approach also encom-
passes the understanding of the cognitive processes that underlie human-AI
interactions.
In recent years, the goal of human-centred AI has become sufficiently
clear and consensual for several disciplines to feel concerned, allowing
a holistic view of the problem. Specifically, Human-Computer Interac-
tion (HCI) and legal perspectives seem to collide in the human-centric
AI approach. HCI is obviously part of the mix of the disciplines in-
11"Rules for AI available
volved. Specifically, human-centric AI builds on HCI’s long history of
in the Union market or
2004
user-centred design [Abras et al., ]. However, policy and legal ex-
otherwise affecting people
pertshavealsoadoptedahuman-centricapproachtoAI,despitelawhis- intheUnionshouldthere-
torically being a rather independent academic discipline [Barocas et al., fore be human centric, so
2020 that people can trust that
]. For instance, the High-Level Expert Group (HLEG) has fully
thetechnologyisusedina
embraced a human-centric approach [High-Level Expert Group on AI
2019 11 way that is safe and com-
(HLEG), ], which is also reflected in the new AI Act regulation .
pliantwiththelaw,includ-
Theregulationalsotakesintoaccountobservationsfrompsychologyand ing the respect of funda-
Human-Computer Interaction (HCI) literature regarding the impact of mental rights" in Section
12 1.1"Reasonsforandobjec-
human factors on trust, such as the severity of consequences .
tives of the proposal" [Eu-
This thesis falls within the human-centric AI approach. We focus on ropeanCommission,2021]
the calibration of trust between humans and AI systems, through ex-
12Recital38aofthedraft
proposal
plainability, as a key enabler of meaningful human-AI collaboration. We
alsocomplementthehuman-centricperspectivewithlegalapproachesin
the case studies presented in Part II.

| 30  | the | explanation |     | paradox | and | the | human centric |     | path |     |     |
| --- | --- | ----------- | --- | ------- | --- | --- | ------------- | --- | ---- | --- | --- |
-
|     | 1.1.4 | Explainability |     |     | (may) | contribute | to warranted |     | trust |     |     |
| --- | ----- | -------------- | --- | --- | ----- | ---------- | ------------ | --- | ----- | --- | --- |
Explainability serves as one of the levers to extract information about
2021
the behaviour of AI systems [Markus et al., , High-Level Expert
Group on AI (HLEG), 2019 , Jacovi et al., 2021 ]. However, there exist
terminologicalnuancesandcontroversiesinthedefinitionofexplainabil-
ity [Markus et al., 2021 ]. Some argue that the term explainability and
the acronym XAI are reserved for the mathematical methods used to in-
terrogate AI systems and extract insightful information about their inner
workings[Herzog, 2022 ]. Anotherterm,interpretablityisthereforeusedto
refer to the propensity of an AI system to be contextualized and human-
2021
understandable [Broniatowski, ]. Additionally, interpretable AI usu- 1.3:
|     |     |     |     |     |     |     |     |     |     | Figure | A Geo- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------ |
ally refers to models that are designed in a way that is simple enough
|     |     |     |     |     |     |     |     |     |     | graphical | Perspective |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- |
2019
for humans to fully understand them [Rudin, ]. As for the term on Explainability.
| intelligibility, |     |           |     |         |            |       |             |     |           | Comparison       | of key-      |
| ---------------- | --- | --------- | --- | ------- | ---------- | ----- | ----------- | --- | --------- | ---------------- | ------------ |
|                  |     | it refers | to  | the     | propensity | of an | explanation | to  | be human- |                  |              |
|                  |     |           |     |         |            |       |             |     |           | word             | searches for |
| understandable   |     | [Weld     | and | Bansal, | 2018       | ].    |             |     |           |                  |              |
|                  |     |           |     |         |            |       |             |     |           | "explainability" | and          |
We can see that the variations between these different terms can be
|     |     |     |     |     |     |     |     |     |     | "interpretability" | on  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- |
subtle. Moreover, there is no consensus on their definitions in the cur- 2004
|     |     |     |     |     |     |     |     |     |     | Google | from to |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------- |
rent literature. For example, some use explainability and interpretability present. Shows that
|     |     | 2021 |     |     |     |     |     |     |     | China only | uses "inter- |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------------ |
[Markus et al., ] interchangeably. Depending on their geographical
|     |     |     |     |     |     |     |     |     |     | pretability", | while Israel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ |
region, researchers may only use one term and not the other, as shown
|     |     | 13  |     |     |     |     |     |     |     | and Viet-Nam | only use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- |
in Figure . . To clarify the meanings of explainability-related terms, we
"explainability".
| retain | the | following | definitions |     | for the | rest of | this dissertation: |     |     |     |     |
| ------ | --- | --------- | ----------- | --- | ------- | ------- | ------------------ | --- | --- | --- | --- |
Definition
Explanation. ExplanationsofAIsystemsaretransfersofknowledgeabout
the behavior AI systems [Henin and Le Métayer, 2022, Miller, 2019]. Henin
and Le Métayer [2022] state that explanations are "descriptive and intrinsic
|     | in the sense | that | they only | depend | on  | the system | itself". |     |     |     |     |
| --- | ------------ | ---- | --------- | ------ | --- | ---------- | -------- | --- | --- | --- | --- |
Definition
Explainability.
|     |     |     | Explainability |     |     | broadly refers | to providing |     | explanations |     |     |
| --- | --- | --- | -------------- | --- | --- | -------------- | ------------ | --- | ------------ | --- | --- |
of AI systems to relevant stakeholders to scrutinize AI models in their de-
velopment, implementation, and deployment stages [Herzog, 2022]. It most
commonly involves demands for transparency and interpretability of AI sys-
|     | tems [Herzog, | 2022]. |     |     |     |     |     |     |     |     |     |
| --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Definition
|     | Explainable |     | AI (XAI). |     |             |          |        |           |          |     |     |
| --- | ----------- | --- | --------- | --- | ----------- | -------- | ------ | --------- | -------- | --- | --- |
|     |             |     |           |     | Explainable | AI (XAI) | is the | technical | arm that |     |     |
aims to provide explainability. Following Markus et al. [2021] and Gilpin
et al. [2018], an AI system is explainable if it is intrinsically interpretable,
orifitiscomplementedwithaninterpretableandfaithfulexplanation. Inter-
pretability covers aspects related to the intelligible and understandable aspect
of explanations by humans. Fidelity captures the capacity of an explanation
|     | to provide | accurate | and | truthful | accounts | of an | AI system. |     |     |     |     |
| --- | ---------- | -------- | --- | -------- | -------- | ----- | ---------- | --- | --- | --- | --- |

introduction 31
Definition
Interpretable AI. A subset of algorithms that are simple enough to be
completely understood by design. These include linear and logistic regres-
sions,decisiontreesandrules,GenerativeLinearModelsandGenerativeAd-
ditive Models [Molnar, 2019].
Expressions such as the ones we use in this section "explainability
contributes to trust", "explainability fosters trust in AI" are common in
2022
the recent literature on human-AI collaboration [Ferrario and Loi, ].
However,therelationshipbetweenexplainabilityandtrustisnotstraight-
forward and needs to be challenged.
2022
Ferrario and Loi [ ] argue that there exists a causal relationship
between the perceived reliability of an AI system, given by reliability in-
dicators,andtheperceivedtrustworthinessofasystem. Accordingtothe
authors, explainability therefore fosters trusts only if it is an indicator of
reliability of the AI system. In the context of medical AI, the authors do
not believe that explainability can meet this condition, as it does not di-
rectly depict how reliable and predictable an algorithm is. They consider
that explainability is neither sufficient, nor necessary, to form justified
beliefs about the trustworthiness of the AI system. They also note that
there is no link between the explainability of a system and the absence
of need to monitor it, which for them characterises trust [Ferrario and
2022
Loi, ]. The authors, however, note that these claims have yet to be
demonstrated empirically.
2021
On the contrary, Jacovi et al. [ ] note that explainability enables
warranted trust by making possible the observation of the intrinsic rea-
soningprocessoftheAIsystemandexternalsymptomsofthemodelbe-
havior. In other words, explainability is unique in its ability to establish
‘intrinsic trust’, whereas other mechanisms for establishing calibrated
trust rely on ‘extrinsic’ trust mechanisms. As a result, explainability can
foster distrust in a non-trustworthy system and trust in a trustworthy
one.
Inthisdissertation,weaimtofurtherclarifythechallengesinenabling
warrantedtrustwithexplainableAIbyreviewingexistingpracticesinthe
XAI field and conducting empirical studies in the financial sector.
1.1.5 Explainability (may) contribute to lawful AI
As AI enters highly regulated environments, and specific AI regula-
tion emerges, the issue of monitoring compliance of AI systems with
existing or new regulations arises. This thesis examines the role of ex-
13
plainability in enabling such controls, and enforcing "lawful" or com- 13"Lawful AI" is one
pliantAI.Morespecifically,welookatexplanations’roleinjustifyingthat of the three conditions
for trustworthy AI. It
AI systems are compliant within some set of rules. We consider that, if
is defined as "respecting
explainability can contribute to fostering warranted regulator trust and,
allexistingapplicablelaws
in specific cases, warranted consumer trust, it participates to making AI and regulations" [High-
"lawful". We examine the challenges in using explainability for demon- Level Expert Group on
strating compliance with specific financial regulations.
AI(HLEG),2018].

32 the explanation paradox and the human centric path
-
Figure1.4: Visualrepre-
sentationofthecoreno-
tions used in this dis-
sertation. We focus on
one of the three pillars
defined by the HLEG
of trustworthy AI: law-
ful AI. Specifically, we
examine the role of ex-
planationstosupportjus-
tifications of AI systems
with respect to regula-
tions or regulatory ob-
jectives.
Central to the notion of regulation is the power to compel regulated
entitiestoconformtoasetofstandards. JuliaBlackproposedthefollow-
ing seminal definition of regulation:
Definition
Regulation. "The intentional use of authority to affect behaviour of a
different party according to a set of standards, involving instruments of
information-gathering and behaviour modification" [Black, 2001].
The holders of this authority are regulators. Their role is twofold: to
create, and to enforce regulations. The financial sector typically distin-
guishes between these two functions through the use of two separate
terms: regulators and supervisors. Regulators are in charge of drafting
the rules, and supervisors of verifying that the rules are applied. In this
14
thesis, we consider the perspective of supervisors in the domains of 14alsocalled"regulatory
customer protection in life-insurance and anti-money laundering. supervisors"
Regulations are designed to meet specific objectives. The question of
whether it is the pursuit of social welfare that animates regulation has
been debated for decades in the economic sphere [Levine and Forrence,
1990 2011
, Levi-Faur, ]. However, scholars generally agree that regulation
can be presented as an instrument to promote the general interest, par-
2009
ticularly in situations of market failure [Moss et al., ]. For example,
some regulations aim to protect customers against asymmetries of infor-
mation, preserve trade secrets or prevent fraud. In this thesis, we exam-
ine specific cases of the use of AI in the highly-regulated financial sector
2015
[Hadjiemmanuil, ]. We focus on two narrow objectives of financial
regulation. We explore the case of protecting customers from the knowl-
edge asymmetry that arises between them and an online recommender
system of life-insurance. This is the "customer protection objective" of fi-
2015
nancial regulation, as presented in [Hadjiemmanuil, ]. Additionally,
we analyse the issue of preventing money laundering using AI systems,

introduction 33
in which the applicable regulation pursues the "reduction of financial
2015
crime objective" [Hadjiemmanuil, ].
To enforce regulation, supervisors carry out controls of regulated en-
2015
tities, also known as inspections [Hadjiemmanuil, ], in which they
15
verify that the rules are being properly applied . Inspections are close 15The finance industry
to the concept of an audit. However, audits are not necessarily on-site is known to impose
tightregulatorycontrols
nor carried out by regulators. They are usually conducted by other par-
2017 on banks and other
ties external to the entity being monitored [Wright, ]. The literature
financial intermediaries
on algorithmic audits has grown in recent years. Audits of AI systems in [Hadjiemmanuil,2015].
productioninregulatedindustrieshaveadaptedhistoricalapproachesto
2021
auditing from the social sciences [Vecchione et al., , Sandvig et al.,
2014 2021 2023
, Metaxa et al., , Mökander et al., ].
Definition
Audit, auditability. In the context of a regulated environment, an al-
gorithmicauditisagovernancemechanisminwhichauditorsparticipateina
field experiment to diagnose the compliance risks associated with AI systems
in relation to specific regulations [Sandvig et al., 2014, Metaxa et al., 2021,
Mökander et al., 2023]. The auditability of AI systems enables "the assess-
mentofalgorithms,dataanddesignprocesses"[High-LevelExpertGroupon
AI (HLEG), 2019] and permits auditors to conclude on the compliance of AI
systems [Toader, 2019, Raji et al., 2020].
The EU’s High Level Expert Group on AI highlighted the key role of
auditability for accountability [High-Level Expert Group on AI (HLEG),
2019 2021
]. Koshiyamaetal.[ ]givefourmainverticalsofalgorithmaudit-
ing: performanceandrobustness,biasanddiscrimination,explainability,
andprivacy. Someoftheseverticalstheyargue, are"closelylinkedtothe
principleofpreventionofharm[High-LevelExpertGrouponAI(HLEG),
2019
]." Audits aim to verify that systems do not adversely affect human
beings.
This regulatory enforcement process contributes to making regulated
firms accountable for their AI systems. Doshi-Velez and Kortz [ 2017 ] de-
fine accountability as:
Definition
Accountability. "The ability to determine whether a decision was made
inaccordancewithproceduralandsubstantivestandardsandtoholdsomeone
responsible if those standards are not met." [Doshi-Velez and Kortz, 2017]
2016
AccordingtoKrolletal.[ ], theaccountabilitymechanismsthatover-
see critical decisions, such as loan approvals, immigration procedures or
vote counting, are lagging behind technological advances. The authors
argue that new technological approaches are needed to verify that AI-
based decision-making processes are accountable and compliant with a
set of standards.
Additionally, an important element of accountability is the capacity to
demonstrate compliance. Felici et al. [ 2013 ] state: "Accountability involves

| 34 the | explanation | paradox | and the human | centric path |     |     |
| ------ | ----------- | ------- | ------------- | ------------ | --- | --- |
-
[...] demonstrating ethical implementation to internal and external stakehold-
ers". We consider that this demonstration element is provided by the
| concept of | justification. |     |     |     |     |     |
| ---------- | -------------- | --- | --- | --- | --- | --- |
Justification is another central concept in the enforcement of regula-
tions. During inspections, regulated entities typically need to justify that
theircurrentpracticesareconsistentwithapplicableregulationsandtheir
16
underlyingobjectives . Weadoptthefollowingdefinitionofjustification 16The
|          |              |             |     |     | regulators’       | need     |
| -------- | ------------ | ----------- | --- | --- | ----------------- | -------- |
| provided | by Henin and | Le Métayer: |     |     | for justification | is actu- |
|          |              |             |     |     | ally something    | we hy-   |
pothesizeanddocument
Definition
|     |     |     |     |     | in this thesis. | To date, |
| --- | --- | --- | --- | --- | --------------- | -------- |
Justification.
AccordingtoHeninandLeMétayer[2022],ajustification, verylittleworkhasbeen
or “justifiability”, is an argumentative process that refers to external norms done to understand the
socio-technicalrealityof
to argue that a decision (or a system) is “good” (or adequate). Justifications
inspections.
are grounded in norms, such as legal requirements [Henin and Le Métayer,
| 2022, Hildebrandt, |     | 2019]. |     |     |     |     |
| ------------------ | --- | ------ | --- | --- | --- | --- |
This definition works in relation to the decisions of an AI system. Henin
2022
| andLeMétayer[ |     | ]furtherdefinestheconceptoflegitimacyinregards |     |     |     |     |
| ------------- | --- | ---------------------------------------------- | --- | --- | --- | --- |
to when the AI system as a whole is "good" within some regulation, ob-
jectivesorsystemofnorms[Suchman, 1995 ,HeninandLeMétayer, 2022 ].
Hereinafter, we use the expression justifiability to refer to the adequacy
of both an AI decision or whole system with respect to applicable legal
requirements [Henin and Le Métayer, 2022 ], for the sake of simplicity.
To date, little work has addressed the role of explainability in the reg-
ulatory enforcement process, i.e. for accountability, auditing, or justifi-
2017
ability. Doshi-Velez and Kortz [ ] argued that explanations have an
importantroleinenablingaccountabilityofAIdevelopersandusers. The
practice of providing reasons for decisions has an important legitimacy
function in legal culture, promoting trust of decision-making, the rule
of law, and acceptance of outcomes [Schauer, 1995 ]. However, Henin
2022
and Le Métayer [ ] highlighted the fundamental differences between
justifications and explanations. Contrary to explanations, which are de-
scriptiveandcontainedtotheAIsystem,justificationsarenormativeand
| 17  |     | 2019 |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- |
extrinsic . Hildebrandt [ ] also states that explanations are not suffi- 17In Chapter 6, we ar-
|     |     |     |     |     | gue that | justifications |
| --- | --- | --- | --- | --- | -------- | -------------- |
cient to justify a decision and that a justification may require an explana-
|     |     |     |     |     | must also be | grounded |
| --- | --- | --- | --- | --- | ------------ | -------- |
tion, but not systematically. She adds that "wemustnotallowthediscourse
|     |     |     |     |     | in intrinsic | and accu- |
| --- | --- | --- | --- | --- | ------------ | --------- |
ofexplainabilitytostandinthewayofthequestionwhetheradecisionislegally
|     |     |     |     |     | rate information | about |
| --- | --- | --- | --- | --- | ---------------- | ----- |
justified, which requires a specific type of legal reasons" [Hildebrandt, 2019 ].
AIsystemsimplementa-
Nevertheless, explanations may be necessary to provide tangible infor- tion, such as explana-
tions.
mation about AI systems’ behavior on which to base legal arguments.
AI explanations, justifications, and audits provide pieces of evidence
about the trustworthiness of AI systems. However, the point of view of
regulators,whoareresponsibleforauditingandrequestingjustifications,
has not been empirically investigated. This thesis addresses this issue
by studying how human-centric explainability can support justifications
for AI systems during regulatory inspections, taking the perspective of
| financial | supervisors. |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- |

introduction 35
Additionally, explainablitymayalsohavearoletoplayincertaintrust
calibration mechanisms that are critical for compliance. We can distin-
guish several trust relations that influence the compliance of AI systems
with some regulation.
Figure 1.5: The con-
cept of warranted trust
First, customer protection regulation may require that customers be and the trust relation-
able to make informed choices by receiving meaningful explanations ships explored in this
about an AI-based recommendation for some product or service. If cus- dissertation. We in-
vestigate whether ex-
tomersappropriatelytrustandrelyontherecommendations,itindicates
planations can enhance
that the regulated entity provides users with the necessary means to cal-
warrantedtrustbetween
ibrate their trust in the system, or that the system only provides appro- an individual subject
priate recommendations. Either outcome is a sign of compliance. to an AI decision and
the AI system, as well
Second, compliance is often guided by an appropriate level of trust aswhetherexplanations
and a healthy dose of skepticism between the regulated entity and its cancontributetothede-
AI system, specifically in high-risk industries. For example, a human AI velopment of justifica-
tions that support war-
operatorwhoblindlyescalatesAI-generatedfinancialcrimealertswillbe
ranted trust between a
guiltyofovertrust,therebybreachinglegalrequirementsaboutmeaning-
regulator and the AI
ful human review of alerts. systemofaregulatee.
Third,warrantedregulatortrustinAIsystemsofregulatedentitiesen-
ablesregulatortoappropriatelyassessthelegalityofAIsystems,thereby
contributing to "lawful AI". Justifications enable "justified" trust by artic-
ulatingreasonstotrustordistrustanAIsystem. Explanationsandaudits
arelikelytoplay animportantroleinsupportingsuch justificationswith
factual evidence about an AI system’s behaviour.
Fourth, regulators’ trust in regulatees also influences compliance in a
2013
complexandcontradictoryway[Six, ]. Ontheonehand,ifregulators
fully trusted regulatees, there would be no need for inspections, and
2013
public trust in regulators would be reduced [Six, ]. On the other
hand, some research has shown that if regulators act out of distrust in
regulated entities, the overall result is poorer compliance [Gunningham
2009
and Sinclair, ]. It has also been shown that the more inspectors trust
regulated entities, the more likely they are to be compliant [Braithwaite
1994
and Makkai, ].
In this thesis, we investigate the first and third trust relationships
through two case studies. We examine the challenges to warranted trust

36 the explanation paradox and the human centric path
-
between customers and AI systems in life-insurance, and trust between
regulators and regulatees’ AI systems in anti-money laundering.
1.1.6 Research domains
Explainability is an interdisciplinary topic. XAI researchers have pri-
marily focused on developing statistical tools to gain insight into the
inner workings of "black boxes". For example, many techniques rely
on querying the AI system and looking at specific entry/outcome pairs.
18
Varying degrees—local or global—and types of explanations can be 18For example, coun-
achieved. The technique for generating explanations is a critical research terfactual explanations
explain the minimal
stream where much progress has yet to come on the robustness, fidelity,
changes to make for a
causality of explanations. However, other fields of research like human-
specific decision to be
computer interaction (HCI), social sciences or law help us make sure we
flipped.
keep this research aligned with why we want to generate explanations
and what kind of explanation is needed in specific situations, i.e. the
2020
human and societal aspects of XAI [Longo et al., ]. For instance, a
2023
new stream of research called "contestable AI" [Alfrink et al., , Bal-
2023 2021 2021
ayn et al., , Lyons et al., , Kaminski and Urban, ] aims to
design explanations for citizens to contest an algorithmic decision. In re-
centyears,anincreasingbodyofresearchhasbeendedicatedtostudying
people’ needs for explanations, relying on qualitative user studies or on
cognitive science theories. It has also endeavoured to better understand
the effects of explanations on users to inform their design.
Figure 1.6: Domain
scope
The work presented in this dissertation falls within this line of re-
search. It is situated at the intersection of three primary research com-
1
munities, all focused on the subject of explainability: ( ) the design of
2
interactive interfaces, rooted in HCI, ( ) psychological theories of ex-
3
planations, ( ) and the study of algorithmic fairness, accountability and

|     |     |     |     |     | introduction | 37  |
| --- | --- | --- | --- | --- | ------------ | --- |
transparency, an emerging multidisciplinary community that addresses
thesocietalaspectsofAI.Allthreecommunitieshavebeennotedasinflu-
2018
entialanddistinctresearchstreamsinAbduletal.[ ]’stopicnetwork
| analysis | of explainability | literature. |     |     |     |     |
| -------- | ----------------- | ----------- | --- | --- | --- | --- |
The design of interfaces and human-computer interactivity are core
HCI topics. This discipline aims to expand the horizons of "communica-
tion between user and system" or "human-computer dialogue", as phrased by
Dix and Ellis [ 1998 ], Foley et al. [ 1996 ]. One could also make a parallel
19
between Infovis and XAI, or even view the design of XAI interfaces 19A domain close to
|     |     |     | 2007 |     | HCI which | focuses on |
| --- | --- | --- | ---- | --- | --------- | ---------- |
as an InfoVis problem [Yi et al., ]. In the XAI field, questions also
arise about how to represent information about AI systems, and how to transforming informa-
|            |               |      |              |     | tion into | a visual form |
| ---------- | ------------- | ---- | ------------ | --- | --------- | ------------- |
| manipulate | and interpret | that | information. |     |           |               |
|            |               |      |              |     | to enable | readers to    |
makesenseofthedata
Psychological theories of explanations provide hypotheses on the way
peopleexplainthingstoeachother,ontheroleofexplanations,oronde-
sirable properties explanations, such as broadness and simplicity [Lom-
2016
brozo, ]. This work has been put forward by Tim Miller’s review
| "Insights | from the | social sciences" | for XAI [Miller, | 2019 ]. |     |     |
| --------- | -------- | ---------------- | ---------------- | ------- | --- | --- |
In his review of the trends and trajectories in Explainability, Abdul
2018
et al. [ ] highlight the nascent "Fairness, Accountability and Trans-
parency" community. The research community is gathered around the
societal problems posed by AI, and is marked by topics related to soci-
etaljustice,includingresearchonalgorithmicbiases,orjudicialandlegal
work[Krolletal., 2016 ,Doshi-VelezandKortz, 2017 ,Nanninietal., 2023 ,
|           | 2019  |            | 2021       |     |               |                |
| --------- | ----- | ---------- | ---------- | --- | ------------- | -------------- |
| Green and | Chen, | , Kaminski | and Urban, | ].  |               |                |
|           |       |            |            |     | Figure 1.7:   | Topic net-     |
|           |       |            |            |     | work of       | the FAT and    |
|           |       |            |            |     | Interpretable | ML com-        |
|           |       |            |            |     | munity in     | [Abdul et al., |
2018].

38 the explanation paradox and the human centric path
-
1.2 Problem statement
Explanations of AI systems are supposed to lift the veil of AI’s com-
plexity, enable meaningful human understanding, and solve the black-
box problem. However, their effects on warranted trust, and specifi-
cally the warranted trust of regulators and customers to enable compli-
2019
ance,hasnotbeennotclearlyestablished[Poursabzi-Sangdehetal., ,
2019 2021 2020
Wang et al., a, Ghassemi et al., , Kaur et al., ]. For example,
2021
Ghassemietal.[ ]arguethatexplainabilityisa"falsehope"inhealth-
2020
care to help inform patients and Kaur et al. [ ] showed that the data
scientistsintheirexperimentsreliedtooheavilyonXAItoolsoverall,and
used them to rationalize suspicious observations. Additionally, it seems
clear that explanations are bound to fail if they are not "human-centric",
i.e. tailored to their human audience and purpose [Tomsett et al., 2018 ,
2023 2022 2023
Ooge, , Ooge et al., , Maxwell, ]. Various groups, such as
medical doctors or AI practitioners (AI developers or expert users), have
2019
receivedacertainamountofattentionintheliterature[Wangetal., a,
2021 2023 2022
Ghassemi et al., , Panigutti et al., a, Sun et al., , Liao et al.,
2023
]. However, there is a scarcity of research on the development of
human-centricexplainabilityaddressedtoeithercustomersorregulators
to verify compliance. The importance of this issue is likely to increase in
the future as more regulations are introduced.
The question we address in this dissertation is: To what extent can
human-centricexplainableAIenablewarrantedtrustandregulatorycom-
pliance in financial applications? To answer this question, we break
down the problem into two parts:
P roblem 1 How do AI explanations affect our trust calibration in AI
predictions and systems? As we presented in Section 1 . 1 . 4 ,
it is still unclear whether AI explanations are able to lead to
warranted trust. Specifically, some argue that explanations
can lead to various cognitive pitfalls, leading to inappropri-
2021
atetrustandpoordecision-making[ChromikandButz, ,
2021 2020
Ghassemi et al., , Kaur et al., ]. This research there-
fore begins with the identification of what cognitive patterns
might get in the way of appropriately using, interpreting
and trusting explainable AI decision systems. We first ask:
What are the cognitive challenges to fostering appropriate trust
in explainable AI?. We review the cognitive biases that inter-
vene in the trust calibration process, notably those that lead
to overtrust or distrust of AI decisions. We stress the need
for human-centric XAI design, that take into account human
cognitive constraints. Secondly, in response to a growing in-
terest for designing more interactive explanations [Weld and
2018 2019
Bansal, , Cheng et al., ], we examine whether inter-
active explanations designed to fit the human cognitive ar-
chitecture are more effective in enabling warranted trust. We
ask: Towhatextentcan"human-like"interactiveexplanationshelp
overcome trust calibration issues?

introduction 39
| roblem | 2           |            |                |                    |                   |                |                    |           |                |             |
| ------ | ----------- | ---------- | -------------- | ------------------ | ----------------- | -------------- | ------------------ | --------- | -------------- | ----------- |
| P      | To what     | extent     |                | can explainability |                   |                | support            |           | regulatory     | com-        |
|        | pliance     | of         | AI in          | the financial      |                   | sector?        | Although           |           | AI             | is increas- |
|        | ingly       | entering   | regulated      |                    | industries        |                | and                | new       | AI regulation  | is          |
|        | emerging    |            | [European      | Commission,        |                   |                | 2021               | ], very   | little         | research    |
|        | has         | examined   | the            | role               | of explainability |                |                    | to ensure | regulatory     |             |
|        | compliance. |            | In the         | second             | part              | of             | this dissertation, |           |                | we exam-    |
|        | ine         | how AI     | explainability |                    | can               | foster         | warranted          |           | trust          | by cus-     |
|        | tomers,     | and        | warranted      |                    | trust             | by regulators, |                    | and       | thereby        | meet        |
|        | regulatory  |            | objectives     | in                 | two               | applications   |                    | of        | AI in finance. | In          |
|        | the         | first case | study,         | customers’         |                   | warranted      |                    | trust     | in             | an online   |
recommendersystemoflife-insurancecontractsisadesirable
|     | objectiveofcustomerprotectionregulation. |     |     |     |     |     |     | Wethereforeask: |     |     |
| --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- |
Doesexplainabilityenhancecustomerwarrantedtrustandempow-
|     | erment               | in              | life-insurance? |          | We also    | ask: | What        | is  | the impact | of dif-    |
| --- | -------------------- | --------------- | --------------- | -------- | ---------- | ---- | ----------- | --- | ---------- | ---------- |
|     | ferent               | explanation     |                 | formats, | including  |      | interactive |     | ones, to   | meet this  |
|     | regulatoryobjective? |                 |                 | In       | the second |      | case study, |     | we examine | the        |
|     | role                 | of explanations |                 | to       | enable     | the  | warranted   |     | trust      | by regula- |
torstoevaluatecomplianceofAIsystemsinanti-moneylaun-
|            | dering               | and | countering |            | terrorism                             |           | (AML-CFT). |                 | Our | research |
| ---------- | -------------------- | --- | ---------- | ---------- | ------------------------------------- | --------- | ---------- | --------------- | --- | -------- |
|            | questionisasfollows: |     |            |            | Whataretheregulatorysupervisors’needs |           |            |                 |     |          |
|            | for explainability   |     |            | to justify | the                                   | decisions | and        | characteristics |     | of AI    |
|            | systems              | in  | AML-CFT?   |            |                                       |           |            |                 |     |          |
| 1.3 Thesis | overview             |     |            |            |                                       |           |            |                 |     |          |
This dissertation is divided into seven chapters, including this intro-
duction, and two research parts. Chapter 2: Background reviews the rel-
evant literature setting the stage for this research. In particular, it sheds
light on the different disciplinary approaches in the very active field of
explainability,whichhasgrownimpressivelyinrecentyears. Toexamine
the challenges of human-centric explainability in supporting warranted
| trust and | compliance, | we  | then | divide | our analysis |     | into | two | parts. |     |
| --------- | ----------- | --- | ---- | ------ | ------------ | --- | ---- | --- | ------ | --- |
Part I: Calibrating trust in explainable AI: common pitfalls and the
promise of interactivity focuses on the cognitive challenges for war-
ranted trust in human-centric explainable AI, taking a cognitive ap-
proach. As the field of explainability has grown considerably in recent
years, with thousands of academic papers published each year, reviews
are much needed to distill important insights. This is why we decided
tobeginthisresearchwithtworeviewsoftheliterature. PartItherefore
| contains | two chapters | presenting |     | two | reviews. |     |     |     |     |     |
| -------- | ------------ | ---------- | --- | --- | -------- | --- | --- | --- | --- | --- |
Chapter 3: Trust, overtrust, distrust in explainable AI: a cognitive ap-
proach identifies the cognitive processes people use when calibrating
trust in XAI-assisted settings, highlighting common uses, misuses and
disuses of explanations. We also review the other ways in which cogni-
| tive biases | affect the | design | and | evaluation |     | of explainable |     |     | AI. |     |
| ----------- | ---------- | ------ | --- | ---------- | --- | -------------- | --- | --- | --- | --- |

40 the explanation paradox and the human centric path
-
Chapter4: Towards"human-like"explanations: thepromiseofinterac-
tivity explores the potential of interactive XAI to limit biases by adopt-
ingamore"human-like"explanationprocess. Wepresentataxonomyof
the different ways in which explanations are interactive and summarise
the effects of explanations on trust, reliability or understanding.
Part II: Complying with regulation using human-centric explainable
AI: two case studies in finance explores two real-world contexts in fi-
nancewhereexplanationsmaybenecessaryforcompliance. PartIIalso
containstwochapters. Thetwocasestudiesalsoprovideinformationon
the entry of cross-sector AI regulation, such as the forthcoming AI Act,
into a highly regulated sector. The first AI application in life-insurance
distribution is considered as high-risk under the AI Act. It is sill uncer-
tainwhetherthesecondcaseinAML-CFTisconsideredhigh-riskunder
the AI Act, as the final text of the AI Act has not yet been released, but
it is probable. In either case, the study documents how regulators are
adapting to AI in light of existing financial regulations.
Chapter5: Empoweringcustomersofrobo-advisorswithexplainability
investigates the explanation needs of customers of life-insurance robo-
20
advisors , and the explanation requirements from the perspective of 20A robo-advisor is an
customer protection supervisors in this context. We examine, in a con- online platform for fi-
nancial investment ad-
trolled study, the correspondence between the regulatory objectives of
vice.
explanations and their actual effects on users. Specifically, we focus
on explanations’ effect on appropriate trust and reliance by customers.
We test different forms of explanations, including interactive ones. We
highlightthechallengesthatarisetoempoweruserswhileavoidingmis-
placed trust.
Chapter 6: Understanding the supervisors’ needs for explainable AI in
financial crime detection analyses the needs of regulatory supervisors
for explanations to audit AI decisions and systems using a qualitative
workshop-basedmethodandalegalanlysis. Thisuser-centricapproach
allows us to delineate the challenges of using explainability for demon-
strating compliance in AML-CFT. We also describe the socio-techno-
legal context of supervisors and their auditing practices in this domain.
Chapter 7 concludes on the main findings of this thesis and discusses
open questions and avenues for future research.

|              |     |          | introduction | 41  |
| ------------ | --- | -------- | ------------ | --- |
| 1.4 Research |     | approach |              |     |
Human-computer interaction researchers are concerned with observ-
ing how people interact with tools that they build. Explainability re-
search also involves designing XAI artefacts and observing users inter-
actingwiththemincontext. Thisdissertationappliesasetofbehavioural
researchmethodstocollectinformationonuserbehaviourwithXAI.The
studies conducted in this work follow typical methods used in explain-
ability and HCI research, such as reviews, and field experiments. We
also demonstrate the usefulness of bridging legal and HCI approaches.
Our argument is that a comprehensive understanding of the legal re-
quirements enforced by regulators is necessary to understand the needs
of this user group. Below is a brief description of the methodological
approachesweemployedforobservinganddesigning(initalics)human-
XAI interactions.
1.8:
|     |     |      | Figure Overview    | of  |
| --- | --- | ---- | ------------------ | --- |
|     |     | 1997 | the work presented | in  |
Mackay and Fayard [ ] described a triangulation framework which
thisdissertationthrough
explains how natural sciences, design and engineering sciences can be a modified version of
integrated. WepresentanadaptedtriangulationframeworkinFigure 18 . the triangulation frame-
| showing | the contributions | of our work. | work of Mackay | and |
| ------- | ----------------- | ------------ | -------------- | --- |
[1997],
|     |     |     | Fayard | inspired |
| --- | --- | --- | ------ | -------- |
from[Huron,2014]

| 42 the explanation | paradox |     | and | the | human | centric |     | path |     |     |
| ------------------ | ------- | --- | --- | --- | ----- | ------- | --- | ---- | --- | --- |
-
Reviews, At the start of my PhD, a significant number of primary
Collections studies on explainability had been freshly published but
|     | there was | little  | hindsight |            | or  | analysis | about   | them.   | Thus,      | it  |
| --- | --------- | ------- | --------- | ---------- | --- | -------- | ------- | ------- | ---------- | --- |
|     | seemed    | fitting | to        | synthesize |     | that     | work    | through | literature |     |
|     | reviews.  | We      | used      | detailed   |     | scoping  | reviews |         | in Chapter |     |
3 4
|     | and      | to           | synthesize |           | some       | observations |            | made         | on          | XAI-   |
| --- | -------- | ------------ | ---------- | --------- | ---------- | ------------ | ---------- | ------------ | ----------- | ------ |
|     | human    | interaction. |            | Scoping   |            | reviews      | are        | an           | appropriate |        |
|     | survey   | type         | to examine |           | how        | research     |            | is conducted |             | on a   |
|     | specific | topic,       | give       | a summary |            | of           | the        | focus        | of the      | field, |
|     | map key  | concepts,    |            | identify  | the        | types        | of         | evidence     | found       | in     |
|     | a field, | pave         | the        | way       | for future |              | systematic |              | reviews,    | and    |
2018
|     | identify      | gaps         | in the    | literature |                  | [Munn    | et           | al.,       | ].          | More- |
| --- | ------------- | ------------ | --------- | ---------- | ---------------- | -------- | ------------ | ---------- | ----------- | ----- |
|     | over, reviews |              | are       | also       | ways             | to get   | inspiration  |            | for the     | de-   |
|     | sign of       | XAI          | artefacts | [Herring   |                  | et       | al., 2009    | ]. This    | collection  |       |
|     | process       | allows       | to        | identify   | state-of-the-art |          |              | designs    | as          | well  |
|     | as features   |              | that do   | not        | exist            | yet.     | In both      | of         | the reviews |       |
|     | presented     | in           | this      | paper,     | we               | followed |              | the PRISMA |             | (Pre- |
|     | ferred        | Reporting    |           | Items      | for Systematic   |          | Reviews      |            | and         | Meta- |
|     | Analyse)      | methodology, |           |            | a systematic,    |          | standardised |            | way         | of    |
|     |               |              |           |            |                  | 2021     |              |            | 2018        |       |
|     | collecting    | papers       |           | [Page      | et al.,          |          | , Tricco     | et al.,    |             | ].    |
5
Co-design In the context of life-insurance (Chapter ), we first re-
|     | lied on         | a market-driven   |               |               | approach  |                  | to understand |                | the       | com-    |
| --- | --------------- | ----------------- | ------------- | ------------- | --------- | ---------------- | ------------- | -------------- | --------- | ------- |
|     | plexities       | of                | the domain,   |               | and       | take inspiration |               | from           | existing  |         |
|     | online          | life insurance    |               | tools         | to        | make             | our           | experiment     |           | as re-  |
|     | alistic         | as possible.      |               | We            | then      | supplemented     |               | our            | approach  |         |
|     | with interviews |                   | with          | regulators    |           | and              | non-expert    |                | users     | to      |
|     | enhance         | our               | understanding |               |           | of the           | life          | insurance      | indus-    |         |
|     | try and         | end-users         |               | needs,        | following |                  | a co-design   |                | methodol- |         |
|     |                 |                   |               | 2023          |           |                  | 2023          |                |           |         |
|     | ogy [Panigutti  |                   | et            | al.,          | a, Luria, |                  |               | ]. Co-design   |           | in the  |
|     | context         | of human-computer |               |               |           | interaction      |               | (HCI)          | refers    | to a    |
|     | collaborative   |                   | and           | participatory |           | approach         |               | [Spinuzzi,     |           | 2005 ], |
|     | where           | both              | researchers   |               | and       | end-users        |               | engage         | in the    | de-     |
|     | sign process.   |                   | This          | approach      |           | recognizes       |               | the importance |           | of      |
|     | involving       | users             | to            | meet          | their     | needs,           | preferences,  |                | and       | ex-     |
|     | pectations      | effectively.      |               |               |           |                  |               |                |           |         |
Field experiment This method involves investigating the impacts of a phe-
|     | nomenon | with | some | controlled |     | variables, |     | but | in a | real- |
| --- | ------- | ---- | ---- | ---------- | --- | ---------- | --- | --- | ---- | ----- |
1995
|     | world | setting. | Mcgrath |     | [   | ] describes |     | it  | as "working |     |
| --- | ----- | -------- | ------- | --- | --- | ----------- | --- | --- | ----------- | --- |
withinanon-goingnaturalsystemasunobtrusivelyaspossible,
|     | except                                    | for intruding |           | on that | system  | by       | manipulating |               | one          | major |
| --- | ----------------------------------------- | ------------- | --------- | ------- | ------- | -------- | ------------ | ------------- | ------------ | ----- |
|     | feature                                   | of that       | system."  | It      | offers  | the      | advantage    |               | of increased |       |
|     | generalisability,                         |               | enabling  |         | testing | with     | a            | larger        | number       | of    |
|     | participants,whileminimisinginvasiveness. |               |           |         |         |          |              | Nevertheless, |              |       |
|     | it sacrifices                             |               | a certain | degree  | of      | control. |              |               |              |       |

introduction 43
5
In this Chapter , we wanted to study the effects of differ-
ent formats of explanations on regulatory objectives, in-
cluding user understanding. As the case study dealt with
robo-advisors, which are online platforms, we decided to
conductanonlinefieldexperimentusingacrowdsourcing
platform to recruit potential users. This approach curtails
the invasive impact of the research.
Interviews In this work, we developed interview protocols several
times to better understand our case studies contexts and
stakeholders’ needs. Interview guides can be found in the
Appendix. Our first set of interviews were conducted in
5
life-insurance (Chapter ), where we used semi-structured
interviewswithathinkaloudsectioninwhichparticipants
used our explanation prototype. We chose this approach
to better understand and compare the perspectives of dif-
ferent user groups and improve our explanation proto-
6
types. InChapter ,weconductedinterviewsagain,inthe
contextofanti-moneylaundering. Ouraimwastogainan
in-depth understanding of the regulators’ perspective. As
1996
a result, we opted for focus groups [Morgan, ], using
a semi-structured interview protocol based on scenarios.
Each time, we took a grounded analysis approach, as de-
2012
scribed in [Creswell, ], either using simple thematic
coding or by combining it with axial coding.
6
Compliance In our AML-CFT case study (Chapter ), we observed
assessment that the interview participants, particularly the supervi-
sors, consistently referred to legal requirements or regula-
tory sanction cases when asked about the questions they
had about the AI systems and the explanations or justi-
fications they wished to see. This prompted us to find
out more about the AML-CFT laws that participants ref-
erenced. We also found that the literature was not clear
abouthowcomplianceinthisdomaincouldbeaffectedby
AI’s opacity. We therefore supplemented our HCI, qual-
itative, interview-based approach with a qualitative com-
pliance assessment, i.e. a legal analysis. We begun with a
2017
doctrinal research as described by McConville [ ]. We
highlightinthisworkthebenefitsofcombiningtheseHCI
and legal qualitative research approaches.

| 44 the explanation |     | paradox |     | and the | human | centric | path |
| ------------------ | --- | ------- | --- | ------- | ----- | ------- | ---- |
-
| 1.5 Major | findings |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- |
This section serves as an executive summary of the contributions of
thisthesis,whicharedevelopedinChapter 7 concludingthedissertation.
1
. Explanations tend to increase trust, including overtrust, depending
mainly on users’ knowledge and skills, and explanations’ complete-
| ness, framing | and | timing. |     |     |     |     |     |
| ------------- | --- | ------- | --- | --- | --- | --- | --- |
2
. Interactive explanations of AI systems tend to increase trust, but not
| necessarily | overtrust. |     |     |     |     |     |     |
| ----------- | ---------- | --- | --- | --- | --- | --- | --- |
3
. Interactive explanations seem to be more useful for performing a task
| than static | ones, but | they | are less | easy | to use and | take | longer. |
| ----------- | --------- | ---- | -------- | ---- | ---------- | ---- | ------- |
4
. In the context of life insurance robo-advisors, explanations—even in-
teractive ones—were of little use in helping customers understand al-
gorithmic recommendations and trust them appropriately, thus failing
| to meet | their main | regulatory | objective. |     |     |     |     |
| ------- | ---------- | ---------- | ---------- | --- | --- | --- | --- |
5
. Dialogic explanations provided in natural language (in the form of a
chat) increased unwarranted trust of customers in algorithmic recom-
| mendations, | in the | context | of life | insurance. |     |     |     |
| ----------- | ------ | ------- | ------- | ---------- | --- | --- | --- |
6
. In the context of anti-money laundering, regulatory supervisors re-
quire justifications in order to verify: ( 1 ) human alignment with AI
2
systemsparametrization,( )businessexpertunderstandingoftheout-
3
| puts, and | ( ) control | of AI-specific |     | risks. |     |     |     |
| --------- | ----------- | -------------- | --- | ------ | --- | --- | --- |
7
. Explanations have a role of "trial evidence" for justifications. Justifica-
tions should not only be extrinsic by referring to norms or regulations
[HeninandLeMétayer, 2022 ],butalsointrinsicbydependingonfaith-
| ful evidence | of the | system’s | behavior, | that | explanations |     | can provide. |
| ------------ | ------ | -------- | --------- | ---- | ------------ | --- | ------------ |

introduction 45
| 1.6 Academic |     | publications |     |     |     |     |
| ------------ | --- | ------------ | --- | --- | --- | --- |
Below is an overview of the publications in workshops, conferences
| and journals | that I have | contributed | to  | during | my PhD. |     |
| ------------ | ----------- | ----------- | --- | ------ | ------- | --- |
| Publications | as first    | author      |     |        |         |     |
"HowCognitiveBiasesAffectXAI-AssistedDecision-Making:ASystematicReview",Astrid
Bertrand,RafikBelloum,JamesR.Eagan,WinstonMaxwell,Proceedingsofthe2022
’22),
AAAI/ACM Conference on AI, Ethics, and Society (AIES Oxford, UK, August
2022
https://doi.org/10.1145/3514094.3534164
"OnSelective,MutableandDialogicXAI:AReviewofWhatUsersSayaboutDifferentTypes
of Interactive Explanations", Astrid Bertrand, Tiphaine Viard, Rafik Belloum, James
2023
R. Eagan, Winston Maxwell, Proceedings of the CHI Conference on Human
FactorsinComputingSystems(CHI’23.), Hambourg, Germany, April2023 https:
| //doi.org/10.1145/3544548.3581314. |     |     | Honorablemention. |     |     |     |
| ---------------------------------- | --- | --- | ----------------- | --- | --- | --- |
"Towards Informed Decision-making: Triggering Curiosity in Explanations to Non-expert
Users",AstridBertrand,2022WorkshoponXAIandHCI,IHMConference,Namur,
| Belgium,April2022 | https://hal.science/hal-03651368/document. |     |     |     |     |     |
| ----------------- | ------------------------------------------ | --- | --- | --- | --- | --- |
"Questioningtheabilityoffeature-basedexplanationstoempowernon-expertsinrobo-advised
financial decision-making", Astrid Bertrand, James R. Eagan, Winston Maxwell, Pro-
ceedingsofthe2023ACMConferenceonFairness,Accountability,andTransparency
(FAccT’23),Chicago,USA,June2023
https://doi.org/10.1145/3593013.3594053.
Toappear: "AIisEnteringRegulatedTerritory:UnderstandingtheSupervisors’Perspective
on Model Justifiability in Financial Crime Detection", Astrid Bertrand, James R. Eagan,
Winston Maxwell, Joshua Brand, conditionally accepted for publication in the pro-
ceedingsofthe2024CHIConferenceonHumanFactorsinComputingSystems(CHI
’24),Honolulu,Hawaï,May2024.
| Publications | as co-author |     |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- | --- |
"DoAI-basedanti-moneylaundering(AML)systemsviolateEuropeanfundamentalrights?",
Winston Maxwell, Astrid Bertrand, Xavier Vamparys, International Data Privacy
|             | 11,   | 3,     | 2021, | 276–293, | 2021                 |     |
| ----------- | ----- | ------ | ----- | -------- | -------------------- | --- |
| Law, Volume | Issue | August | Pages |          | April https://doi.or |     |
g/10.1093/idpl/ipab010.
"AreAI-basedAnti-MoneyLaundering(AML)SystemsCompatiblewithEuropeanFunda-
2020
| mental Rights?", | Winston | Maxwell, | Astrid | Bertrand, | Xavier Vamparys, | ICML |
| ---------------- | ------- | -------- | ------ | --------- | ---------------- | ---- |
LawandMachineLearningWorkshop,Vienna,Australia,July2020
https://hal.sc
ience/hal-02884824/document.

Chapter 2
Background
his chapter
T provides an overview of the explainability field focusing
on its origins, its interdisciplinarity, and its ongoing and future direc-
21
tions. In Section . , we look at a historical perspective of explainability
to reveal the interdisciplinary and far-reaching roots of this emerging
22 23 25
field of research. Further, Sections . , . and . develop the ongoing
work on explainability respectively from a computer science, social sci-
ences and legal angle. Finally, we explore the role of Human-Computer
Interaction, as a multidisciplinary field by essence, to advance research
24
in explainability in Section . .
2.1 A historical perspective on explainability
Explainability is not a new subject. Before the research interest in
explainability errupted in the context of deep neural networks, a wide
range of work already existed on the epistemology of explanations and
2020
early computational systems. However, Atakishiyev et al. [ ] and
2020
Longoetal.[ ]notedthelackofaconfirmedandresilientconnection
between the historical origins of XAI and present-day AI applications.
Nevertheless, we can broadly trace back the origins of XAI to two histor-
ical avenues: on the one hand, the philosophical and social foundations
of explanations; on the other hand, the development of expert systems
1
and machine learning applications . 1Expert systems are
usually regarded as the
first implementation of
The first historical root of XAI is work on formal theories of explana-
AI [Russell and Norvig,
tions. This line of thought challenges us to think about what counts as 2010].
an explanation, particularly in science, and what purposes explanations
serve. Throughout the evolution of philosophical thought, scholars have
analysed the nature and types of explanations, their explanatory power,
1998 2006 2016 1988
functions, and reach [Bunge, , Lombrozo, , , Hilton, ].
2006
Aristotlealreadydiscussedthenotionofexplanation[Falcon, ],argu-
ing that "knowledge becomes scientific when it tries to find the causes of why"
2020
[Longo et al., ]. This has been reiterated in more recent literature,
which emphasises the challenge of responding to "why-questions" that
1973
entail counterfactual and abductive reasoning [Pople, , Muggleton,
1991 1987 2019
, Poole et al., , Miller, ]. Counterfactual reasoning involves
testing whether an event E is the cause of a phenomenon of interest P

48 the explanation paradox and the human centric path
-
2019
by mentally undoing E and assessing how it affects P [Miller, ]. Ab-
ductive reasoning originates from the field of formal philosophy and in-
volves constructing an explanation that best fits a set of observed data
2020 2020 2019
[Atakishiyev et al., , Longo et al., , Miller, ]. It is often
1965
described as "inference to the best explanation" [Harman, ]. This
strand of work has also stressed the importance of causality in explana-
2005 1988
tion[HalpernandPearl, ]. Forexample,Hilton[ ]establishedthe
notion of "causal chain", i.e. successive causes that lead to the occurrence
of the phenomena of interest. Meanwhile, other work in social sciences
1989
highlighted the structural and social aspects of explanation [Roth, ,
2004 2017 2019
Malle, , Graaf and Malle, , Miller, ].
2020
As Longo et al. [ ] highlighted, little connection has been made so
far to the formal history of XAI, i.e. theories of explanation or causation
2019 2019
[Holzinger et al., ]. Miller [ ]’s review stands out as a rare work
that links this knowledge in philosophy and social sciences to modern
applications of AI. This introductory paragraph on the study of explana-
tion in the fields of philosophy, sociology and psychology only scratches
the surface of the vast body of knowledge that has accumulated on the
subject over the centuries. We will develop the important findings from
23
these disciplines in Section . .
The origins of explainability as a field of research can also be linked
to an early body of work on the explanation of socio-technical systems
1950
dating back as far as the s. As soon as computers became more so-
phisticated and "intelligent", thanks to the implementation of knowledge
andrule-basedreasoninginexpertsystems, thequestionaroseofhowto
explain their decision-making procedures in a synthetic and comprehen-
sible way that is adapted to the explanation recipient. From this point of
view, explainability is nothing new. For example, the book by Winograd
1987
andFlorespublishedin "UnderstandingComputersandCognition"
examinestheunderpinningsofunderstandingwhatcomputersdo,inre-
lationtohumanlanguage,thought,andaction. Aseminal,earlyworkon
the design of explanations for expert systems can be found in medicine
2021
[Confalonieri et al., ]. MYCIN was a famous expert system designed
to assist doctors in their diagnosis about infections. It was presented by
1970
Buchanan and Shortliffe in the s. The system was based on domain
and factual knowledge modeled as "production rules". It was able to
provide explanations as "lines of reasoning" of the system [Confalonieri
2021
et al., ], that is to allow the user to explore the sequence of rules that
wereused. Moreover,itincludedaquestion-answeringmodule,allowing
the user to seek answers for some predefined questions.
Other expert systems, featured explanation as "stories", presenting
how a system considered a problem and some observations, then in-
ferred hypotheses, studied causal relations and eventually found a cause
2021 1989
for the problem [Confalonieri et al., , Roth, ]. An example of
expert system presenting such reasoning is Rex [Wick and Thompson,
1992
]. It used a story structure, a set of reasoning cues, problem and
solutions constraints to produce explanations.

background 49
"Iattemptedtofindthecauseofanexcessiveloadonaconcretedam. Basedonthebrokenpipesin
thefoundation,theslidingofthedam,theupliftpressuresandtheslowdrainage,Iwasabletofind
aninitialhypothesis. Instudyingcausalrelations,Ifoundthattheerosionofthesoilwouldcause
brokenpipes,resultinginslowdrainage[...]. Thisledmetoconcludethaterosionwasthecauseof
theexcessiveload."
ExampleofalineofexplanationintheexpertsystemRex[WickandThompson,1992].
Overall, early research into the explainability of expert systems was
already based on social science considerations. Specifically, it was con-
cerned with how people come to understand information, complement-
ing earlier work on how people explain. For example, in designing Rex,
1992
Wick and Thompson [ ] observed that people tend to narrate causal
chains of events as stories that selectively summarise the most impor-
tant causes. Decision trees were among the first explanations of neural
1995
networks [Craven and Shavlik, ]. Later, the emergence and popu-
2010
larity of deep learning models in the s led research attention over
explainability to skyrocket.
Figure 2.1: A Historical
Perspective on Explain-
Today, thousands of academic papers are published every year on the
21 ability. The bar plot
topic of explainability. Figure . shows—with the red bar plot—the
(in red) shows the evo-
2015 2022 6200
surgeofinterestinthetopicstartingfrom . In ,over papers lution of the number of
17
were published on the topic of explainable or interpretable AI, times academic contributions
more than in 2015 . These numbers were extracted by doing a keyword on XAI. The bubble
2 chartontopdisplaysthe
searchforpaperswiththeterms"explainab*"or"interpretab*" andwith
number of citations—
a keyword related to AI (artificial intelligence, deep learning, machine
represented by size and
learning, neural network) in their titles, abstracts or authors keywords, y-axis—of the most in-
in the Scopus database. fluentialpapersinXAI.
The research interest on XAI was propelled by the computer science 2The wildcard * is used
in keyword searches to
field that focused on how to generate explanations, i.e. the mechanis-
2018 2021 allow for variations of a
ticaspectsofexplanations[Guidottietal., ,Confalonierietal., ].
wordafterthesymbol.
21 60
EachbubbleinFigure . representsoneofthetop- mostcitedpaperto
dateintheexplainabilityfield. Thesizeandpositionofthebubbleonthe

| 50 the | explanation | paradox | and | the human | centric | path |
| ------ | ----------- | ------- | --- | --------- | ------- | ---- |
-
y-axisrepresentthenumberofcitationsofthearticle,anditscolourindi-
catesitsdiscipline. Thisgraphwasmadebysearchingformanydifferent
3
keywordsrelatedtoexplainableAIandintepretableAI ontheSemantic 3For example "inter-
scholar database, which enables to sort results per citation count. The pretable AI system",
explainable machine
top 60 wasrefinedbyplottingthecitationgraphforafewpapersinCon-
learning, explanation
nected Papers. We stopped collecting papers when we did not find any
algorithm, trustworthy
new addition to the top 60 when we plotted different graphs or searched
AI,etc.
| for different | XAI-related | keywords. |     |     |     |     |
| ------------- | ----------- | --------- | --- | --- | --- | --- |
We can see that the green bubbles, representing the computer science
field, are far more numerous and wider in this top 60 . Popular papers—
10000
with over citations—looked at interpretation of convolutional neu-
2014
ral networks (image classifiers), like [Simonyan et al., ], which pre-
sented gradient-based saliency maps, or [Zeiler and Fergus, 2013 ] which
introducedafeaturevisualizationinConvNets. Otherseminalwork,like
|                  | 2017 |                    |     | 2016 |                        |     |
| ---------------- | ---- | ------------------ | --- | ---- | ---------------------- | --- |
| [LundbergandLee, |      | ]and[Ribeiroetal., |     |      | ], presentedtechniques |     |
to identify the most important features used by any kind of classifier.
|                               |     |     | 2017 |                  | 2020 |          |
| ----------------------------- | --- | --- | ---- | ---------------- | ---- | -------- |
| Meanwhile,[Doshi-VelezandKim, |     |     |      | ],[Adebayoetal., |      | ]and[Kim |
etal., 2016 ]providedcriticalintrospectionintotheemergingfieldofXAI,
| but still | focused on the | computer | science | side. |     |     |
| --------- | -------------- | -------- | ------- | ----- | --- | --- |
Contributions in legal and social sciences are scarce in XAI, compar-
22
atively to computer science, as shown in Figure . . However, interdis-
ciplinary work is gaining traction. For example, [Lipton, 2018 ], [Bur-
| 2016 |     | 2019 |     |     |     |     |
| ---- | --- | ---- | --- | --- | --- | --- |
rell, ] or [Rudin, ], reflect on the discourse of interpretability,
on the problem of opacity, or on the use of inherently opaque models
vs. interpreable ones. For example, Lipton [ 2018 ] highlights that "Papers
provide diverse and sometimes non-overlapping motivations for interpretabil-
ity, and offer myriad notions of what attributes render models interpretable".
Kulesza et al. was a pioneer in studying explainability from an HCI lens
|          | 2013      | 2015        |     |                    | 2018 | 2019    |
| -------- | --------- | ----------- | --- | ------------------ | ---- | ------- |
| [Kulesza | et al., , | ]. Starting |     | from approximately |      | - , XAI |
gained popularity among HCI researchers. They have focused on better
understanding users’ needs, designing user-centered XAI interfaces or
2019
developing user-centered metrics for evaluating XAI [Wang et al., a,
| Hoffman | et al., 2019 ]. |     |     |     |     |     |
| ------- | --------------- | --- | --- | --- | --- | --- |
2.2:
Given the exponential body of work in explainability, review papers Figure Distribution
have been timely contributions in recent years to process important in- of contributions in ex-
plainableAIaccrossdis-
sights and to navigate the myriad of XAI techniques, XAI design arte-
ciplines. This graph is
facts, evaluation metrics, or XAI goals and applications. Seminal review based on a corpus of
work include [Adadi and Berrada, 2018 , Barredo Arrieta et al., 2020 , Ab- 5756 articles published
|     | 2018 |     | 2019 |     | 2019 | 2018 from2015topresent,ex- |
| --- | ---- | --- | ---- | --- | ---- | -------------------------- |
dul et al., , Carvalho et al., , Miller, , Guidotti et al., ].
tracted from searching
This dissertation contributes to this need for review papers in the Chap-
"explainab*" in the arti-
| ters 3 and | 4 . |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- |
cle title in the Scopus
Database.

background 51
2.2 Explainability in Computer Science: the tool-
box
ExplainabilityformodernAIapplicationshasfirstbeenapproachedas
a purely technical problem. The aim was to find tools to meet computer
scientists’growinginterestinunderstandingwhathappensinneuralnet-
2020
works [Atakishiyev et al., ]. As a result, a myriad of explainability
techniques have been proposed over the last ten years. We provide a
221 222
brief overview of these in Section . . . In Section . . , we review the
current technical challenges for generating and evaluating explanations
in machine learning.
2.2.1 The wide range of explainability methods
Thearrayofexplanationtechniquesprovidedbythecomputerscience
community is extensive. This breadth arises from the wide scope of ma-
chine learning which encompasses diverse data types, such as images,
text, tables, audio, graphs, and time series, as well as a range of mod-
els, spanningfromDNNs, BayesianNetworks, SVMs, toTreeEnsembles.
Moreover, there are varying approaches to the explainability problem.
Forinstance,explanationsmaypertaintospecificdataandmodeltypesor
beagnosticandapplicabletoanymodelordata. Anotherpossibilityisfor
explanations to be local, focusing on individual forecasts, or global, offer-
ing a comprehensive explanation of the model throughout its definition
range. Further, explanations may arrive post-hoc, meaning that an expla-
nation is reconstructed given some inputs and predictions from a model.
Thisisalsoknownasreverseengineeringintheliterature[Guidottietal.,
2018 ]. However,explanationscanalsobebuilt-in,meaningthatthemodel
is trained in a way that is inherently interpretable (e.g. white box mod-
els, training with sparsity constraints or with supervised explanations).
Many surveys have proposed taxonomies to gain a clearer picture of the
different types and approaches of explanations [Barredo Arrieta et al.,
2020 2018 2023 2021
, Guidotti et al., , Nauta et al., , Burkart and Huber, ,
2019 2020 2021
Carvalho et al., , Das and Rad, , Mohseni et al., b, Molnar,
2019 2018
, Gilpin et al., ]. We drew on these to summarize main expla-
nation concepts, production mechanisms and representations, using our
23
synthetic categorization outlined in Figure . .
Figure 2.3: Categoriza-
tion of explainable AI
methods along four di-
mensions inspired by
Nauta et al. [2023] and
Barredo Arrieta et al.
[2020].

52 the explanation paradox and the human centric path
-
Explainability methods and production mechanisms
Let us begin with an overview of what are the explanations offered by
the computer science field. We present below six different explanatory
concepts that can help inform on the operation and behaviour of black-
box models.
• Feature-based. One of the most popular way to shed light on AI mod-
els’ inner workings is by determining the influence of input features
on the outcomes or intermediate representations of the model. We
includein thiscategory featureimportance, feature attribution, activa-
2016
tion maximization [Nguyen et al., ] and saliency methods [Zeiler
2013
and Fergus, ].
Feature importance consists in generating a vector with the weight and
magnitude of the inputs used by the black-box. It can be either local
or global. It is also sometimes referred to as feature attribution such as
2019
in [Lundberg et al., ] for tree ensembles. There are various ap-
proaches to creating this vector, such as using game-theory inspired
2017
computations [Lundberg and Lee, ] or using the coefficients of
a linear model that approximates the black-box in a region of inter-
2016
est [Ribeiro et al., ]. Most of these methodologies are post-hoc
and rely on querying the black box using input records produced in
a controlled manner or through random perturbations of the original
2018
training or testing data [Guidotti et al., ].
Figure 2.4: Illustrative
examples of feature-
based explanations for
different data types
(image, tabular and
text data) with input
saliency [Alammar,
2021, Unruh and
Robinson,2020].
Saliency methods consist in determining the inputs (either words in a
sentence or areas in an image) that are most “salient” from a model’s
perspective. They are broadly divided into three categories [Kinder-
mans et al., 2017 ]. Sensitivity methods show how a small change to the
inputaffects theprediction[Simonyanet al., 2014 ]. Signalmethods, like
2013
DeConvNet [Zeiler and Fergus, ] or Guided BackProp [Springen-
2015 2019
berg et al., ], look at the neuron activations [Carter et al., ]
in the model to attribute importance to input features. This type of
methodisalsoknowasactivationmaximization. Finally,attributionmeth-
ods, like Integrated Gradients [Sundararajan et al., 2017 ] aim at com-
pletelyspecifyingtheattributionsforalltheinputfeaturessothatthey
sum up to the output. Saliency techniques usually rely on gradient-
based calculations. To gain a better understanding of gradients, let’s
25
consider a CNN that classifies cats and dog images. Figure . illus-
trateshowchangingindividualpixelsaffectsthemodel’sidentification
of the picture as a "cat": the upward arrows represent changes that
make it more likely for the model to identify the image as a cat. Ad-
ditionally, the thickness of the arrow indicates the amount of gradient

background 53
shift that occurs due to that pixel being altered. Pixels that alter the
image substantially are called "salient" and are usually represented in
white or warm colors in saliency maps.
• Prototype-based methods consist in extracting representative exam-
ples or "prototypes" of the black-box outcomes. This approach is in-
spired by case-based reasoning, which allows users to reason based
on retrieved similar input patterns and their outcomes. However, Kim
Figure 2.5: Illustration
2016
et al. [ ] argued that "examples were not enough" and can lead
of the gradient-based
to over-generalization. They proposed to also to "criticize" the ex- method to identify
tracted prototypes by extracting "criticism" samples that are not well- "salient"pixels.
explainedbytheprototypes. Thesetechniquesarebasedoncalculating Moreat: https://pair
.withgoogle.com/expl
similarities or discrepancies between distributions. Other methods in-
orables/saliency/
clude finding prototypical parts in images pointing to aspects of one
2019
class or another [Chen et al., ], finding the nearest neighbors of a
point of interest in the input data space, or finding prototypical con-
2018
cepts that represent a class [Kim et al., , Ghandeharioun et al.,
2022
].
• Counterfactual explanations. Algorithms can also be explained by
considering how an outcome could be changed to another outcome,
2021
for example more desirable [Stepin et al., ]. The problem of find-
ing a counterfactual explanation in ML is usually described as "the
smallest change to the feature values that changes the prediction to a
2019
predefined output" [Molnar, ]. This is achieved by defining a no-
tion of distance between the point of interest and a hypothetical point
for which the outcome would be different. Counterfactual explana- 4Counterfactual expla-
nations help identify
tionshavereceivedagrowingattentioninrecentyearsbecauseoftheir
4 featuresthat,ifchanged
potential to be actionable , their alignment with people’s needs for ex-
can lead to a different
planations: peopleusuallyaskforexplanationswhentheAIoutcomes
result. These explana-
2016
violate their expectations [Kizilcec, ]. Other advantages include tions are actionable if
that they do not require model disclosure or place no constraint on the identified features
2020 can in fact be changed
model complexity. Barocas et al. [ ], however, warn against the
easily. Age or ethnicity
fact that defining a notion of distance to compute counterfactuals is
for example, are not
challenging, and implies somewhat arbitrary choices about the nor- actionable features that
malization of features. Moreover, counterfactual explanations do not someone can change
examinetherationalityordifficultyofrecommendedactionsandmay, to get admitted into a
school. Getting good
for example, suggest that an individual should make less money, or
grades, however, is an
2020
stay longer at his current job [Barocas et al., ].
actionablefeature.
"Onedecisionmakermightscaletheaxessuchthatincreasingincomeby$5,000annuallyis
equivalenttoanadditionalyearonthejob. Acompetinglender,usingdifferenttrainingdata,could
concludethat$10,000ofincomecorrespondstooneyearofwork. Theselendersmighttherefore
producedifferentexplanationsdependingonthescalingofattributes."
Extractfrom[Barocasetal.,2020]onnormalizingfeaturesforcounterfactuals.
• Influence functions. Koh and Liang [ 2020 ] presented influence func-
tionstolinkmodeloutcomestoinfluentialtrainingpoints. Alsoknown
as training data attribution, influence methods suggest which training

54 the explanation paradox and the human centric path
-
data points might be the cause of a model’s behavior for a given input
2020 2022
and output [Pruthi et al., , Akyürek et al., ].
• Simplification. Another popular way to approach explainability is by
approximatingblack-boxmodelsbysimpler,interpretableones[Rudin,
2019
]. It becomes a problem of "finding an interpretable model that
approximatestheblack-boxmodelasmuchaspossible,typicallyseek-
2021
ing high fidelity" [Confalonieri et al., ]. Those simpler models are
called"surrogatemodels". Thesemethodsoftenleveragelogicalor/and
visual models such as decision trees, rules, generative additive mod-
2015
els [Caruana et al., ], logistic and linear regressions or bayesian
2015
models [Kim et al., ]. There also exist methods for reformulating
2020
"connectionist" models as logical models [Barceló et al., ]. This is
considered as "built-in" interpretability, which involves setting inter-
pretability constraints like sparsity in the model training [Nauta et al.,
2023
]. However, the concept of "explainability by design" lacks a fixed
set of rules, and the boundaries between an interpretable and a black-
box model remain unclear. For instance, it is arguable whether a ran-
dom forest is typically more explainable than a neural network.
• Uncertainty estimation. Current explainability methods have often
been criticised for their lack of consistency, stability, and for providing
2021 2021
little insight into their reliability [Bhatt et al., , Slack et al., ,
2020 2017
Leavitt and Morcos, , Kindermans et al., ]. Consequently,
somehaveproposedtorepresenttheuncertaintyofexplanations. Slack
2021
et al. [ ] proposed Bayesian versions of LIME and KernelSHAP to
provide confidence estimates of their quality. Others have considered
the uncertainty estimation of black box models as part of the explain-
2023
abilityscope[ThuyandBenoit, ],orasanecessarycomplementto
2022 2021
transparency[Zhangetal., ,Bhattetal., ]. Forexample,Bhatt
2021
et al. [ ] presents different ways, such as Bayesian and frequentist
methods, to present uncertainty to stakeholders, that are more accu-
ratethantheclassicMaximumClassprobabilitymethod(MCP).Zhang
2022
et al. [ ] include both model and explanation uncertainty in their
explainability framework.
Explanation representations
Explanations can alternatively be presented in natural language, as
1992
it was the case for the expert system Rex [Wick and Thompson, ],
through plots, such as partial dependence plots (PDPs), accumulated lo-
cal effects (ALE) plots, and influence sensitivity plots (ISPs), "tornado
plots" that show the feature weights from most to least important, di-
mensionality reduction plots, through decision rules, tables or trees to
visually present the logic of the model on specific data ranges, by lever-
aging the initial data structure, such as for saliency maps or prototypes,
or by creating artificial visualizations of the concept used by, for exam-
2023
ple, neurons or layers [Nauta et al., ]. Above, we have only hinted
at the wide range of explanation designs that have been tested. The HCI
literature has introduced wide range of explanation visualisations and

background 55
interfaces, adapted to the task, context, user, and model at hand. We
24
summarize these efforts in Section . .
2.2.2 The technical challenges in generating explanations
Rigorous and falsifiable research. Seminal papers like [Lipton, 2018 ],
2017 2020
[Doshi-Velez and Kim, ] or [Leavitt and Morcos, ] have warned
against a lack of rigor and consensus regarding explainability definition,
2020
aims, and practices. In particular, Leavitt and Morcos [ ] noted the
growing shortcomings of the methodologies carried out in the XAI liter-
ature and endeavoured to analyze them. Specifically, they highlight the
lack of scrutiny, criticism and falsifiable hypotheses in explainability re-
search. For example, they point to the incapacity of saliency methods to
reflectmeaningfulproperties ofthedataandnetwork, despitetheir intu-
2017
itivenessandappealingvisualization[Sundararajanetal., ,Adebayo
2020 2023
et al., ]. More recently, Bilodeau et al. [ ] proved mathematically
that some complete and linear feature attribution methods like SHAP or
IntegratedGradientsdonothelpmorethanrandomguessingforthetask
of inferring model behavior. The authors point to other, simpler tech-
niques such as repeated model evaluations in order to perform precisely
definedinterpretabilitytasks. Thiscriticalexaminationofstate-of-the-art
research is important for the progress of explainability.
Causality and reasoning. Research in psychology emphasizes the im-
2005
portanceofcausalityintheexplanationprocess[HalpernandPearl, ].
Yet, most of the explanation strategies described above, specifically fea-
ture importance explanations, do not provide any measure of causality.
Causability is defined in [Holzinger et al., 2019 ] as "the extent to which
an explanation [...] achieves a specified level of causal understanding with ef-
fectiveness, efficiency and satisfaction in a specified context of use." It is not
because a feature is marked as important that it is necessarily a relevant
cause to the outcome. Instead, other confounding variables may be at
play. In their review, Confalonieri et al. [ 2021 ] noted: "causal explanations
arelargelylackinginthemachinelearningliterature,withonlyfewexceptions."
Consequently, the literature in XAI has been increasingly interested in
causal models in search of technical means to address causality in ex-
planations. Explanations based on causal models, like counterfactual ex-
planations, can be action-guiding, i.e. explain the events resulting from
2019 2022
an action [Chattopadhyay et al., , Beckers, ]. However, apply-
ing causal models to the machine learning field is challenging since it
2020
is based on correlation rather than causation [Holzinger et al., , Guo
2021 2017 2017
etal., ,Petersetal., ]. Furthermore,Milleretal.[ ]highlights
that identifying causal attributions is not the same as providing a causal
explanation,asacompletecausalchainiscomplexandhighdimensional,
and therefore not comprehensible to a layperson.
Moreover, some have emphasized the shortcomings of XAI to produce
2021
explanations based on reasoning and logic. Confalonieri et al. [ ] in-
dicate that "establishing a common ground of inherent logic from the ground
upappearsreasonable",forexamplebyintegratingsymbolicorknowledge-
based modules in non-symbolic machine learning models. Doran et al.

56 the explanation paradox and the human centric path
-
2017
[ ] also argue that "truly explainable AI should integrate reasoning".
Promisingwork to goin thatdirection includecausal graphsand knowl-
2021
edge graph mining for generating explanations [Holzinger et al., ,
2020
Lecue, ]. These efforts seek either to integrate an external knowl-
2021
edge base (as in [Holzinger et al., ]), or to model sets of causes and
2020
effects(asin[Lecue, ])intheformofgraphs, whichfacilitatesexpla-
nation processes.
Evaluation. Additionally, many have highlighted the shortage of con-
2020
trolled and harmonized evaluations of the methods [Longo et al., ,
2020 2017
Leavitt and Morcos, , Doshi-Velez and Kim, ]. This stems from
the difficulty of identifying the qualities of an explanation that should
be evaluated. The issue at hand pertains to the qualities of a satisfactory
explanation,whichcannotberesolvedbycomputersciencealone. Other-
wise, there may arise a risk that AI researchers design explainability for
2017
themselves only, rather than for the intended users [Miller et al., ].
It has therefore been suggested that evaluations of explanatory agents
should incorporate the viewpoint of end-users or a human perspective
2017 2017
[Doshi-Velez and Kim, , Miller et al., ]. Valuable insights can
be gained regarding the quality of explanations through analysis of the
social sciences, philosophy, and psychology.

|                    |     |        |                  |           | background | 57  |
| ------------------ | --- | ------ | ---------------- | --------- | ---------- | --- |
| 2.3 Explainability |     | in the | Social Sciences: | the foun- |            |     |
dations
Wehavealreadymentionedinthissectionthatthesocialscienceshave
playedacentral,historicalroleinXAI’spursuitofhumanunderstanding.
Insightsfromthesocialsciencesandthephilosophyofscience[Hedström
and Ylikoski, 2010 ] establish foundational theories regarding the process
by which people explain phenomena, or what people look for in expla-
nations. These insights help to bridge the gap between the explainability
technique seen in the previous section and the explanations needed to
21
promote human understanding. However, as stated in Section . , con-
temporaryXAIresearchers,whohavebeenworkingonexplainingrecent
forms of AI systems, have been slow to take full advantage of this line of
2017
work. Miller et al. [ ]’s review has been a major boost to this endeav-
our.
Manydifferentaspectsoftheconceptofexplanationhavebeenstudied
inepistemology,philosophyandcognitivesciences,includingthereason-
inginvolvedinexplanations[Lombrozo, 2006 ,Leake, 1995 ],theeffectsof
1989
belief and preconditions on explanations [Paul Thagard, ], or how
|     |     |     | i.e. | 2004 |     |     |
| --- | --- | --- | ---- | ---- | --- | --- |
people explain the behavior of others, social attribution [Malle, ].
| All of these | facets of explanations | are | explored in [Miller, | 2019 ]. |     |     |
| ------------ | ---------------------- | --- | -------------------- | ------- | --- | --- |
Below, we make a brief summary of this large array of work, focusing
on explanations’ role, their contrastive nature, the cognitive and social
processesbywhichwe,ashuman,explainphenomena,andthecognitive
| biases involved | in explanations. |              |     |     |     |     |
| --------------- | ---------------- | ------------ | --- | --- | --- | --- |
| 2.3.1           | The role of      | explanations |     |     |     |     |
Seeking explanations is part of our everyday life [Williams and Lom-
5
brozo, 2010 ]. Why is my train late this time? Why didn’t you tell your 5Very
|     |     |     |     |     | often | heard in |
| --- | --- | --- | --- | --- | ----- | -------- |
friend? Why is the Earth round? Young children notoriously question France. The SNCF,
|     |     |     |     |     | France’s | leading train |
| --- | --- | --- | --- | --- | -------- | ------------- |
literally everything with endless "why?" questions [Williams and Lom-
|     |     |     |     |     | company, | is often the |
| --- | --- | --- | --- | --- | -------- | ------------ |
brozo, 2010 ]. In fact, explanations are central to individual’s acquisition
|     |     |     |     |     | subject of | complaints. |
| --- | --- | --- | --- | --- | ---------- | ----------- |
of knowledge and ability to ascribe mental states to oneself and oth- That being said French
| 6   |     | 2006 |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- |
ers [Amsterlaw and Wellman, ]. Reasons why people ask for ex- people’s reputation for
planations involve assessing the soundness of a claim, support learning, grumblingisaccurate.
|     |     |     | 2019 |     | 6This ability | is known |
| --- | --- | --- | ---- | --- | ------------- | -------- |
but also satisfy one’s curiosity [Miller, ]. This study of the role of
|     |     |     |     |     | as theory of | mind in psy- |
| --- | --- | --- | --- | --- | ------------ | ------------ |
explanations mainly falls within the domain of philosophy. chology.
Lombrozo [ 2006 ] highlights three distinct functions that explanations
1
serve. These functions are ) to enable the assessment of the likelihood
of a claim to be true, referred to as causal inference; 2 ) to allow for the
transfer of knowledge to novel cases, which is known as generalization;
3
and, ) to assist in the acquisition of knowledge, i.e. for learning and
discovery. Lombrozo describes how explaining why a claim might be
true is an important process for evaluating the soundness of that claim.
This process of causal inference often favours mechanistic explanations,
i.e. explanations of the mechanisms involved in making the explanan-
7
dum happen. Further, Lombrozo uncovers how explanation supports 7The subject of the ex-
generalization. Generalization enables to solve transfer problems and planation, or event to
|     |     |     |     |     | explain   | is called ex-  |
| --- | --- | --- | --- | --- | --------- | -------------- |
|     |     |     |     |     | planandum | in social sci- |
ences.

58 the explanation paradox and the human centric path
-
extend known properties to novel cases. In a controlled experiment, Re-
2006
hder[ ]showedthatparticipantswhoweregivenanexplanationfora
problemthatinvolvedarelevantcauseforthatproblemandanotherwere
more able to extend that cause to the other problem than if they did not
receive explanations. In short, people could better generalize the cause
2006
ofoneproblemtoanotherwithrelevantexplanations. Rehder[ ]also
demonstrated that similarity and diversity are important factors in the
generalization process. People can generalize from one problem to an-
other specifically when they are similar. Furthermore, people are more
likely to generalise an explanation if it stands true in a diverse range of
contexts. Finally, Lombrozo argued that explaining novel information
to one-self is one of the best ways to learn. Self-explanations are more
powerful for learning than "thinking out loud, reading study materials twice
or merely receiving feedback". Specifically, self-explaining requires to relate
2016 1994
knowledge within prior beliefs [Lombrozo, , Chi et al., ].
Similarly, Miller [ 2019 ] presented that explanations serve to find mean-
ing, i.e. to "reconcile the contradictions or inconsistencies between elements of
ourknowledgestructures". Ithasbeenshown,forexample,thatpeopleask
questions about events that they find unusual or abnormal [Hilton and
1986
Slugoski, ]. Additionally, explanations enable us to construct social
meaning. Throughexplanations,wecanpersuadenotonlyourselvesbut
2019
also others that a claim is true [Miller, ].
Furthermore, we learn more and better when driven by our own cu-
2019
riosity and motivation to understand phenomena. [Shin and Kim, ].
Curiosity is driven by an individual’s realization that she has a gap in
knowledge,butitdecreasesifthatgapistoolarge,thatis,iftheinforma-
tion is unattainable, or if the gap is too narrow, meaning the knowledge
is not very useful. In summary, there is an optimal gap in knowledge
thatmaximizescuriosity. Therefore,arousingAIusers’curiositythrough
explanations is more likely to have an impact.
"Themostimportantfactorsinthegenerationofcuriosityareanindividual’sreferencepointof
knowledgeandtheirawarenessoftheunknownwhichisraisedbycuriosity-evokingstimuli. This
informationgapthencreatesasenseofdeprivation,whichnaturallyinstillsadesiretolearn."
ExtractfromShinandKim[2019]
These findings offer valuable insights into people’s needs for expla-
nations. By understanding why we ask explanations and their role in
forging knowledge, we can design explanations that people perceive as
useful.
2.3.2 The explanation process
Understanding how individuals explain phenomena to one another is
valuable to designing explanations that align with the cognitive archi-
tecture of humans. In fact, the process of explaining is a defining aspect
2019
of an explanation. Miller [ ] describes an explanation as being the
product resulting from answering a why-question, the cognitive process of

background 59
inferring plausible hypotheses, probing, selecting and evaluating them,
and the social process of communicating the explanation to others.
The cognitive process of explaining is composed of several steps, in-
cluding causal connection and explanation selection [Miller, 2019 ]. Causal
connection involves identifying plausible causes for an explanandum ei-
therthroughabductivereasoningand/orthroughsimulation. Abductive
reasoning involves inferring the most probable causes of an observed
event by making hypotheses and testing these. Simulation consists in
undoingalikelycauseinordertoconsidertheeffectsofthismutationon
the observed event and evaluate the likelihood of the plausible cause ac-
tuallycausingtheexplanandum. Explanationselectioninvolvesselecting
asubsetoftheidentifiedcauses,i.e. themost"interesting"ones,basedon
our cognitive biases to discount or regard certain observations. These bi-
ases include our attention to causes that are abnormal (unusual causes),
intentional (for example deliberate intent is usually seen as a stronger
cause for murder than the murder weapon), or functional (causes that
cite the function of an object or event). We also tend to select causes that
are necessary, sufficient and robust to change.
Explaining is also a social process that follows the conventional struc-
2019
tures of a dialogue [Miller, ]. Explaining involves the explainee and
the explainer asking and answering questions in an iterative way, so
that follow-up questions are addressed until the explainee is satisfied.
Through this iterative process, conversational explanations are able to be
truly relevant by finding the explainee’s knowledge gap and taking into
accountwhatshealreadyknows. Conversationsallowforcontextualand
1993 2019
incremental explanations [Cawsey, , Miller, ].
Socialdialoguesalsohaveanumberofconventionswhich,iffollowed,
increase the impact and effectiveness of the conversation. These include
1975
Grice’s maxims of quality, quantity, relation, manner [Grice, ]. As
2019
Miller [ ] presents it: "Coarsely, these respectively mean: only say
what you believe; only say as much as is necessary; only say what is
relevant; and say it in a nice way."
Furthermore,accordingtothetheoryofmind,whichreferstopeople’s
abilitytoattributementalstatestoothers,individualsengagedinasocial
explanationprocesskeeptrackofwhathasalreadybeenexplained. Thus,
2019
this should also be true for computational XAI agents [Miller, ]. In
general, the social aspect of explanations calls for XAI agents to also be
"socially interactive".
These cognitive and social processes describe the mechanisms em-
ployed by an individual (an explainer) to explain an event to someone
else (an explainee). Explainability leverage these theories to build XAI
systems that adopt these processes.
Other useful insights for explainable AI include how people receive
2019
explanations, as explainees. Miller [ ] details that explanations are
evaluated based on our "human" criteria of a "good" explanation. These
1989
involvecoherenceorconsistencywithpriorbeliefs[Thagard, ,Atak-
2020 2007
ishiyevetal., ],simplicity,broadness(orgenerality)[Lombrozo, ],
truthfulness and probability. People also prefer explanations that are

| 60 the | explanation | paradox | and the human | centric | path |
| ------ | ----------- | ------- | ------------- | ------- | ---- |
-
simple, i.e. which cite fewer causes, and broader explanations, i.e. which
explain more events [Thagard, 1989 , Read and Marcus-Newhall, 1993 ,
| 2019 |     | 2015 |     |     |     |
| ---- | --- | ---- | --- | --- | --- |
Miller, ]. Kuleszaetal.[ ]highlightedthecontradictionofpeople
preferring both simple and complete explanations. However, they found
that over-simplification was often problematic for correct understanding
of the explained event and suggested to design complete explanations
"that do not overwhelm". They also found that completeness was more
important than soundness, as it helped participants form more accurate
| mental | models and increased | perceived | usefulness  | of explanations. |     |
| ------ | -------------------- | --------- | ----------- | ---------------- | --- |
| 2.3.3  | Explanations         | are       | contrastive |                  |     |
An important insight from social sciences for XAI put forward by
|          | 2019      |           |                  | explanandum, |     |
| -------- | --------- | --------- | ---------------- | ------------ | --- |
| Miller [ | ] is that | we do not | explain an event | E, the       | per |
se, butratherexplainwhyEhappenedinsteadofsomeothercounterfac-
tual event P. In other terms, in every why-question such as "why did E
happen?", we ask in reality "why did E happen, and not F?" [Miller, 2019 ,
1988
Hilton, ]. This is called the contrastive nature of explanations. Lip-
| 1990 |     |     |     | 2019 |     |
| ---- | --- | --- | --- | ---- | --- |
ton [ ] refers to E as the fact, and F as the foil. Miller [ ] presents
an illustrative example: if someone in a room asks "Why did Elizabeth
openthewindow?",shesurelyhasafoilinmindthatdroveherquestion.
Therecanbemanydifferentpossibilitiesforthatfoil,including"Whydid
Elizabeth open the door, rather than leave it closed?", or "Why did Eliza-
beth open the door rather than the window?". Depending on what the foil
| actually | is, the questions | call for | different answers | .   |     |
| -------- | ----------------- | -------- | ----------------- | --- | --- |
|          | 2019              |          | 2021              |     |     |
As [Miller, ] or [Stepin et al., ] specified, there is a difference
between contrastive explanations and counterfactual explanations. Con-
trastive explanations aim to explain why an output differs from a cer-
2021
tain expected result [Miller, ], whereas counterfactual explanations
point out how to change one result to another. As illustrated in [McGill
and Klein, 1993 ], the former asks "What made the difference between the
employee who failed and the employees who did not fail?", whereas counter-
|                |                     | "Would       | the employee | have failed if | she had not |
| -------------- | ------------------- | ------------ | ------------ | -------------- | ----------- |
| factual        | reasoning addresses |              |              |                |             |
| been a woman?" | [Stepin             | et al., 2021 | ].           |                |             |

background 61
2.4 Explainability in HCI: user and context first
While a mathematical perspective is crucial for providing insights into
opaquemachinelearningsystems,thesocialscienceviewpointisequally
important for offering insights into the human black-box. In turn, the
Human-ComputerInteraction(HCI)perspectiveservesasalinkbetween
these technical and human aspects of XAI.
In this section, we present the diverse range of contributions that the
HCI community provides for the field of explainability.
2.4.1 The need for user-centered explainability
1986 1987
By , Winograd and Flores [ ] had already implemented ex-
planations in early AI systems. They also promoted scientifically-based
design principles to replace informal notions of "user-friendly" and "self-
explanatory" interfaces. However, these developments have been slow
2018 2021
to be transposed to today’s AI [Abdul et al., , Broniatowski, ].
In recent years, the "modern AI" community has finally begun to recog-
nise the importance of considering the human element of XAI [Longo
2020
et al., ]. Several computer scientists have advocated for increased
human involvement in the process of explanation evaluation [Poursabzi-
2020 2017
Sangdeh et al., , Doshi-Velez and Kim, , Vaughan and Wallach,
2020
]. These calls were primarily concerned with examining the impact
of explanations on users, and evaluating whether specific explanation
methods were successful in translating abstract information used by AI
2017
systems into human concepts [Doshi-Velez and Kortz, , Kim et al.,
2018
].
Concerns have also been raised that AI explainability tools are only
aimed at computer scientists and are too technical for non-experts and
end users to understand, in practical cases of AI development [Miller
etal., 2017 ,Confalonierietal., 2021 ,Bhattetal., 2020 ] 8 Thesediscussions 8As Confalonieri et al.
encouraged XAI researchers to consider what information end-users ac-
[2021]argues,"aspectsof
understandabilityofexpla-
tuallywantandhowtopresentthatinformationdependingontheuser’s
nations for lay users has
context, background, experience and other characteristics.
for a long time been over-
looked".
The methods, goals and experience of the HCI community in dealing
withbehaviouralresearchareperfectlysuitedtothispurpose. Infact,the
issueofexplainabilityisprofoundlyamatterofhuman-computerinterac-
tion. By enabling users to make full use of machine learning predictions
and systems, explainability aligns with the founding goals of the HCI
discipline, which are to expand the range of possible human-computer
interactions and collaborations. The HCI community has been study-
2020
ing for decades [Longo et al., ] how people interact with computers,
how to adapt to users’ experience and cognitive architecture, and how to
2022
design usable, useful and empowering interfaces [Oulasvirta et al., ,
2019
Amershietal., ]. Specifically,HCIresearchershavedrawnheavilyon
phenomenology and cognitive science to design computer systems and
interfaces tailored to the cognitive architecture of the human mind.
The explainability research line adopting an HCI perspective has been

62 the explanation paradox and the human centric path
-
labelledasuser-centeredorhuman-centricexplainability[LiaoandVarsh-
2022
ney, ]. This approach has made significant progress across various
fronts in order to make AI systems more understandable to end users
2019 2018 2020 2021
[Wang et al., a, Kim et al., , Liao et al., , Liu et al., ,
2021 6
Shin, ]. Below we outline main research threads in HCI and XAI
1 2
research: ) characterizing explainability user profiles, ) understanding
users’ goals and mental states contextually to inform their precise needs
3
for XAI, ) designing explainable interfaces through iterative cycles of
5
ideation-design-evaluation, ) developing metrics for evaluating explain-
6
ability systems and ) better understanding the factors that contribute
to appropriately trust (X)AI systems. The following sections provide an
overview of the research advances along these six dimensions.
2.4.2 Different audiences, different goals
Theliteratureinexplainabilityhasidentifiedvarioususerprofiles[Kirsch,
2017 2019 2018
,RosenfeldandRichardson, ,Tomsettetal., ,Mohsenietal.,
2021 2021 2020
b, Langer et al., , Ferreira and Monteiro, ]. This helped
to identify the gap between the technical explanations provided by the
computersciencecommunityandthediverseexplanationneedsofother,
real-world XAI users.
Some studies have placed emphasis on AI expertise and application
domain knowledge to classify users. As a result, three distinct user
groups have been put forward in the XAI literature: AI novices, also
known as non-experts or lay users, domain experts, and AI experts
2021 2019
[Mohseni et al., b, Ribera and Lapedriza, ]. AI novices are in-
dividuals impacted by AI systems, but who have little knowledge in the
technicalities of AI. Examples are users of an online recommender sys-
tem, decision-subjects of a loan application, medical patients or citizens
interestedinlearningmoreaboutpublicAIsystems. Domainexpertsare
people with significant knowledge in the field of application of the AI
2023
system, such as doctors, or loan officers [Ooge, ]. AI experts are ma-
chine learning developers, engineers and researchers. This classification,
however, is coarse. for example, the lay user group is extremely diverse
2022
specifically in terms of familiarity with AI [Liao and Varshney, ].
Other classifications distinguish user groups according to their role in Figure 2.6: Figure 1
2018 in [Tomsett et al., 2018]
the machine learning ecosystem. For example, Tomsett et al. [ ] iden-
identifies the different
tified six roles that require different, if any, AI explanations, as shown
stakeholders in a ma-
26 2019
in Figure . . Similarly Hind [ ] identified four explainability user chine learning ecosys-
groups: AI system builders, who want to debug their models and test tem. "Directionofarrow
indicatesdirectionofin-
them before deployment; end-user decision makers, who use the AI rec-
teraction."
ommendations to make a decision; regulatory bodies, in charge of pro-
tectingcitizens’rights;andendconsumers,whoaredirectlyimpactedby
2023
the decision of the AI system and may want to contest it. Maxwell [ ]
recognisesroughlythesamefouraudiences: machinelearningengineer,
human operator of the system, person affected by the algorithmic de-
cision and judge, auditor or regulator.

background 63
These user profiles ("whom to explain?") are associated with different
goals ("why explain?") [Leake, 1991 ], leading to different information
needs and different explanation designs. Some have listed the expla-
nation content ("what to explain?") and explanations methods ("how to
explain"?) corresponding to different user groups [Liao and Varshney,
| 2022 |             |     | 2020                 |     |     |     | 2019 |                | 2021 |     |     |
| ---- | ----------- | --- | -------------------- | --- | --- | --- | ---- | -------------- | ---- | --- | --- |
|      | ,Liaoetal., |     | ,RiberaandLapedriza, |     |     |     |      | ,Mohsenietal., |      | b]. |     |
For example, Liao et al. [ 2020 ] provided a "question bank" of user ques-
tions related to explainability, including questions related to the general
model logic, "how?", to the changes that would get the alternative pre-
diction, "why not?", or to the feature(s) that if changed, could alter the
| prediction |     | in  | a direction, | "how | to  | be that?". |     |     |     |     |     |
| ---------- | --- | --- | ------------ | ---- | --- | ---------- | --- | --- | --- | --- | --- |
The amount of time each user is prepared to invest in the explanation
|                                         |     |     |     |     |     |     |     | 2022          |     | 2009 |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | --- |
| ("howlongtoexplain?")[GajosandMamykina, |     |     |     |     |     |     |     | ,Stumpfetal., |     | ]    |     |
alsodependsontheuser’sprofile,asdoesthetimeatwhichtheexplana-
2021
tion is presented to the user ("when to explain?"). Nourani et al. [ ]
argue that the timing of the presentation of explanations, either before,
during or after the explainee has generated her own explanation, greatly
2023
affects the user’s mental model and reliance on the AI. Maxwell [ ]
depict four different contexts in which user attend explanations. These
aretestingthesystem,human-in-the-loop,human-on-the-looporex-post
investigation. Some work also posits different levels of explanability for
specific audiences and contexts taking into account legal, economic, so-
2020
cial and technical considerations [Beaudouin et al., , Dupont et al.,
| 2020 |          |     | 2021    |     |     |     |     |     |     |     |     |
| ---- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
|      | , Langer |     | et al., | ].  |     |     |     |     |     |     |     |
2018
Adadi and Berrada [ ] identified four main reasons why people
need explainability: explain to justify that an AI decision is good, for
example to regulators; explain to control and identify errors quickly, for
example to human operators of the AI system; explain to improve AI
models, which is what AI developers want; and explain to discover new
knowledge from powerful AI systems, such as how AlphaGo beats hu-
mans at chess. Suresh et al. [ 2021 ] and Mohseni et al. [ 2021 b] present
explain to build trust as a distinct important user goal, specifically for
2021
novice users. Suresh et al. [ ] also identified compliance with regula-
tions as a key objective of explainability users, that is tied to the overar-
ching goals of building trust and understanding AI models. More fine-
grained and contextual approaches are needed, however, to understand
| the | precise | needs | of users.     |     |      |       |     |         |     |         |                |
| --- | ------- | ----- | ------------- | --- | ---- | ----- | --- | ------- | --- | ------- | -------------- |
|     | 2.4.3   |       | Understanding |     | user | needs | in  | context |     |         | 2.7:           |
|     |         |       |               |     |      |       |     |         |     | Figure  | The four       |
|     |         |       |               |     |      |       |     |         |     | reasons | motivating the |
A growing number of XAI systems have been developed for specific need for explainable AI
presentedin[Adadiand
users in specific contexts, with some examples provided in [Zhu et al.,
Berrada,2018].
2018 , Wang et al., 2019 a, Panigutti et al., 2023 a, Krause et al., 2016 , Cop-
|      |     | 2018 |         |     | 2019 |         | 2023 |               |          |     |     |
| ---- | --- | ---- | ------- | --- | ---- | ------- | ---- | ------------- | -------- | --- | --- |
| pers | et  | al., | , Cheng | et  | al., | , Ooge, |      | ]. To provide | relevant |     |     |
explainability designs, these studies go through the endeavour of un-
derstanding the specific needs of users to support them in their context-
specifictasksandgoals. HCIresearchershavereliedoncognitivetheories
about how users explain [Miller, 2019 , Wang et al., 2019 a, Bertrand et al.,

| 64  | the explanation |     | paradox | and | the | human | centric | path |     |
| --- | --------------- | --- | ------- | --- | --- | ----- | ------- | ---- | --- |
-
2.1:
Who? Developers or AI researchers / Domain experts / Lay users [Ribera Table The differ-
andLapedriza,2019,Mohsenietal.,2021b] ent classifications of au-
diences, goals, explana-
|     |     | AI Creator | / Operator | / Executor |     | / Data-subjects | / Decision-subject |     | /   |
| --- | --- | ---------- | ---------- | ---------- | --- | --------------- | ------------------ | --- | --- |
tion content, explana-
Auditors[Tomsettetal.,2018]
tiontimingandcontexts
MachineLearningEngineer/Humanoperator/Personaffected/Reg-
presentedintheXAIlit-
ulatororauditor[Maxwell,2023,Hind,2019].
erature.
Why? Explain to justify / to control / to improve / to discover [Adadi and
Berrada,2018]
tobuildtrust[Sureshetal.,2021,Mohsenietal.,2021b].
What? For example: What did the system do? / Why did the system do
|     |     | P? / Why   | did the system |       | not do  | X? / What | would the      | system | do if   |
| --- | --- | ---------- | -------------- | ----- | ------- | --------- | -------------- | ------ | ------- |
|     |     | Y happens? | / How          | can I | get the | system    | to do Z, given | the    | current |
context?"[RiberaandLapedriza,2019].
Seealso[Liaoetal.,2020]’squestionbank.
Before/during/afterthetask[Nouranietal.,2021].
When?
|     |     | Depends | on the context: |     | human-in-the-loop |     | / human-on-the-loop |     | /   |
| --- | --- | ------- | --------------- | --- | ----------------- | --- | ------------------- | --- | --- |
testingthesystem/ex-postinvestigation[Maxwell,2023].
Howlong? How long will the user explore the explanation? [Gajos and
Mamykina,2022,Stumpfetal.,2009].
| 2022 |        | 2021            |     | 2017 |            |     | 2006           |     |     |
| ---- | ------ | --------------- | --- | ---- | ---------- | --- | -------------- | --- | --- |
|      | ,Shin, | ,GraafandMalle, |     |      | ,Lombrozo, |     | ,LiaoandVarsh- |     |     |
ney, 2022 , Danry et al., 2023 ], on interviews [Sun et al., 2022 , Liao et al.,
| 2023 | 2020 |            | 2021   |         |     | 2021 |           | 2021 |       |
| ---- | ---- | ---------- | ------ | ------- | --- | ---- | --------- | ---- | ----- |
|      | ,    | , Ehsan et | al., , | Maltbie | et  | al., | , Tsai et | al., | , Kim |
|      | 2023 |            |        |         |     |      | 2023      |      |       |
et al., ] or participatory design [Panigutti et al., a, Cheng et al.,
2022 , Wang et al., 2019 a] to learn about users’ contexts and needs. These
approaches form the starting point of the HCI disciplinary triangulation
between natural science theory, artefact design, and scientific observa-
tions to design empowering explainability systems [Mackay and Fayard,
1997
].
Using interviews, articles such as [Sun et al., 2022 , Liao et al., 2020 ,
Lim and Dey, 2009 ] give fine-grained accounts of users’ questions and
motivations regarding explainability. They inform on the actual user de-
mandforinformationaboutAIsystems, invariouscontexts,forexample
|                                     |      |     |      |     |     | 2018 |               | 2016 |      |
| ----------------------------------- | ---- | --- | ---- | --- | --- | ---- | ------------- | ---- | ---- |
| AIdevelopmentanddebugging[Zhuetal., |      |     |      |     |     |      | ,Krauseetal., |      | ,Sun |
|                                     | 2022 |     | 2015 |     |     |      |               |      |      |
et al., , Kulesza et al., ]; ideation with AI for designers [Liao
et al., 2023 ]; doctor assistance in healthcare [Panigutti et al., 2023 a, Wang
|     | 2019 |     | 2015 |     |     | 2020 |     |     | 2021 |
| --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | ---- |
et al., a, Caruana et al., , Jin et al., , Jacobs et al., ]; or
2022
pretrial risk assessment [Yacoby et al., ]. For example, Ehsan et al.
[ 2021 ]interviewed 29 AIusersandpractitionerstolearnaboutthesocio-
organizational context of XAI-aided decision making, a perspective they
call "Social Transparency". Sun et al. [ 2022 ] conducted workshops with
43
software engineers to explore their explainability needs when using
2021
generative AI for code. Maltbie et al. [ ] conducted stakeholder inter-
views to implement XAI in the public sector for sewer overflow predic-
tions.
Some studies have also summarized the wide range of questions that
users can have on AI systems [Liao et al., 2020 , Lim and Dey, 2009 ]. Liao
2020
et al. [ ] employed card-sorting exercises to encourage participants to
| sort | the most | important | questions | they | had. |     |     |     |     |
| ---- | -------- | --------- | --------- | ---- | ---- | --- | --- | --- | --- |

background 65
1997
Scenario-based design [Carroll, ], in which participants are en-
gaged in a scenario to elicit their feedback, has often been used to un-
2020
derstand explainability users in context [Cirqueira et al., , Sun et al.,
2022 2019 2023
, Wolf, , Liao et al., ].
Another challenge that HCI researchers are tackling is the capture of
users’ mental states when they are interacting with AI systems. Work
1
in the social sciences has highlighted the importance of ( ) identifying
the specific knowledge gap and the foil that the explainee is trying to
2
address, and ( ) keeping track of what the explainee already knows, as
23
seen in Section . . This allows for more relevant explanations. Some
efforts to capture dynamically users’ specific questions and mental rep-
resentations of AI systems and domains are starting to emerge in the
explainability literature. This what several currents known as conversa-
2019 2021 2019
tional XAI [Ehsan et al., , Grimes et al., , Madumal et al., ,
2021 2021
Weitz et al., , Hernandez-Bocanegra and Ziegler, ], interactive
2021 2022
XAI [Chromik et al., , Ooge et al., ] and interactive ML [Teso
2023 2014 2022
et al., , Amershi et al., , Guo et al., ] are working towards.
Early AI systems used human-like communication processes to provide
explanations in the form of dialogues and conversations in natural lan-
2018 1986
guage [Abdul et al., ]. In , for example, Winograd and Flores
1987
[ ]stressedtheneedforexplanationsystemstoreflecttheuser’smen-
2021
tal representation of the domain [Broniatowski, ].
2.4.4 Designing explainability systems
Design methods from user experience research such as card sorting,
participatorydesignorscenario-baseddesignhavesometimesbeenused
to ideate and conceive explainability interfaces.
Low-fidelity prototypes with conceptual artefacts as test explanations
have sometimes been proposed to to build and test ideas quickly. These
wereoftenputincontext,throughscenario-baseddesign[Cirqueiraetal.,
2020 2022 2019 2023 2021
, Sun et al., , Wolf, , Liao et al., , Tsai et al., ].
Higher fidelity prototypes in which an explainable technique (XAI)
2015
is programmed were used more frequently [Kulesza et al., , Cheng
2019 2016 2021
et al., , Krause et al., , Chromik and Butz, , Panigutti et al.,
2023 2019 2019
a, Wang et al., a, Springer and Whittaker, ]. Kulesza et al.
2015
[ ] drew on existing literature and design principles to develop their
2023 2019
prototype. Paniguttietal.[ a]andWangetal.[ a]usedco-design
2023
methods to involve end-users in designing solutions [Rogers et al., ,
2019
InternationalOrganizationforStandardization(ISO)].Wangetal.[ a]
sketched initial visualisation prototypes, which they improved through
14
five iterations with clinician participants. Then, in co-design sessions
withaclinicianparticipant,theyextractedkeydesignimplicationsforex-
9Heuristic evaluation is
plainability interfaces in the medical domain, such as "supporting access
a method for identify-
to source and situational data" or "supporting forward (data-driven) reason-
ing problems in a user
ing by showing feature values and attributions before class attribution to avoid interface (UI), which in-
confirmation bias". Panigutti et al. [ 2023 a] redesigned their explainability volves a team of evalu-
interfacebasedonusers’feedbackonaninitialprototypeandthenrelied ators judging it accord-
9 ing to a set of usabil-
on heuristic evaluation to test the usability of the new interface. The
ity guidelines [Nielsen,
1992].

| 66  | the | explanation | paradox | and | the | human | centric | path |     |     |
| --- | --- | ----------- | ------- | --- | --- | ----- | ------- | ---- | --- | --- |
-
redesignoftheirexplainableUIenablednotableimprovement,including
enhanced user controls and aesthetics. By conducting two user studies,
2019
Springer and Whittaker [ ] found that it is essential to gradually dis-
close information about machine learning models so as not to distract
| users | and | undermine | their | proper understanding |     |     | of the system. |     |                      |     |
| ----- | --- | --------- | ----- | -------------------- | --- | --- | -------------- | --- | -------------------- | --- |
|       |     |           |       |                      |     |     |                |     | Figure 2.8: Examples | of  |
|       |     |           |       |                      |     |     |                |     | visual explanations  | for |
|       |     |           |       |                      |     |     |                |     | different AI models  | a)  |
As a result of these design processes, many different visuals for ex-
|     |     |     |     |     |     |     |     |     | Hybrid visual and | tex- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ---- |
planationuserinterfaceshavebeengenerated. Explainabilityresearchers
tualexplanationsforthe
have been focusing on ways to present information visually in the more estimation of the read-
usefulandeffectivemanner[Ooge, 2023 ]. Theresearchdomainsofinfor- ing time of an article
2021],
mation visualisation and visual analytics specifically address this issue. [Szymanski et al.,
|     |     |     |     |     |     |     |     |     | b) Influence of features |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- |
Information visualization (or Infovis) has been exploring ways to repre-
|     |     |     |     |     |     |     |     |     | on loan default | risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ---- |
sentdatasoastobestassistusersintheirtasks. Visualanalyticsisaspe-
|     |     |     |     |     |     |     |     |     | [Chromik et al., | 2021], |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------ |
cialized subfield of Infovis that focuses on complex interfaces designed c)Multipleexplanations
forhousepriceforecasts
for experts or analysts. Visual analytics interfaces typically consolidate
2019]),
several visualisations on a single screen and provide users with an ex- [Hohman et al.,
|     |     |     |     |     |     |     | 2023 |     | d) Example-based | ex- |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---------------- | --- |
tensiveselectionofcontrolsandinteractionoptions[Ooge, ]. Several
|     |     |     |     |     |     |     |     |     | planation for drawing |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- |
interfaces of this type have been proposed in the explainability literature
|             |       |              |                |             |         |      |              |      | recognition [Cai | et al., |
| ----------- | ----- | ------------ | -------------- | ----------- | ------- | ---- | ------------ | ---- | ---------------- | ------- |
|             |       | 2019         |                | 2021        |         | 2019 |              | 2019 |                  |         |
| [Mingetal., |       | ,Chengetal., |                | ,Wangetal., |         |      | b,Zhaoetal., |      | ]. 2019].        |         |
|             | 2.4.5 | Evaluating   | explainability |             | systems |      |              |      |                  |         |
In a seminal paper calling for rigorous approaches to interpretabilty,
Doshi-Velez and Kim [ 2017 ] cautioned against evaluating explanations

background 67
in a "you’ll know it when you see it" fashion, as this is prone to confir-
mation bias and unscientific practices. They introduced three different
approaches to evaluate explanations. These approaches are functionally-
grounded,human-groundedandapplication-grounded,fromlesstomoredomain-
specific and costly. Functionally-grounded evaluation, also referred to
2023
as algorithm-centered evaluation [Ooge, ], is a method that does not
involve human participation and relies on statistical metrics to quantify
the effectiveness of an explanation. Several common metrics used in
this approach include stability, robustness, consistency, sparsity, discrim-
inativeness, and computational efficiency [Afchar et al., 2022 ]. Human-
grounded evaluation requires human participants to rate explanations
along various criteria, or complete tasks such as simulating a model’s
prediction for a given input after seeing explanations of the model’s be-
havior. Human-centred evaluation does not involve real users in specific
applications. Instead, it usually involves artificial tasks that enable the
testing of explanations with a large panel of human participants. Lastly,
application-groundedevaluationconsistsintestingexplanationsinreal-
world settings, with real users. Users are instructed to engage with ex-
planationsandsubsequentlyprovidefeedbackontheirsubjectiveexperi-
ence. For example, participants rate their level of satisfaction, subjective
trustorperceivedutilityoftheexplanations. Theymayalsoanswerques-
tions that allow researchers to determine the amount of knowledge they
gained or the extent to which they relied on the AI [Poursabzi-Sangdeh
2019
et al., ].
Figure 2.9: The 12
Explanation quality
properties proposed by
[Nautaetal.,2023].
2019
Hoffman et al. [ ] suggested that the three tests of satisfaction, un-
derstanding and performance are key to measuring the "goodness" of
explanation. The paper also presents an Explanation Satisfaction Scale

68 the explanation paradox and the human centric path
-
andsummarizesthedifferentwaystoelicitusers’understandingandthe
differentapproachestomeasureperformanceofthe(X)AI+humanteam
at conducting the tasks for which the technology is designed. Addition-
ally,itprovidesachecklisttomeasureusers’curiosityandtrustmeasure-
2021
mentscales. Vereschaketal.[ ]conductedathoroughreviewoftrust
2020
measurement for explainable AI. Holzinger et al. [ ] proposed a Sys-
temCausabilityScale,similartotheSystemUsabilityScale[Jordanetal.,
1996
], to determine whether an explanation is suited to an intended pur-
2023
pose. More recently, Nauta et al. [ ] reviewed explanation evaluation
strategies in XAI and presented a grid of twelve properties for assessing
explanations. Threeofthesepropertiesrequireinputfromusers: context,
coherence, and controllability. The other properties pertain to explana-
29
tion content and presentation, as shown in Figure . .

background 69
2.5 Explainability in Law: dreaming in color?
Lawhaslongrecognizedtheneedtoimposeinformationdisclosureon
certain, generally powerful, actors. Justice Louis Brandeis’s saying that
"Sunlight is the best disinfectant" has inspired transparency obligations
2011 2017
in a broad range of fields [Schauer, , Lee, ]. Law and economics
scholars have traced the need for information disclosure to various mar-
ket failures, such as information asymmetries and monopoly [Daniels
2019 2013
et al., , Wolfe, ]. It is no surprise therefore that information dis-
closure obligations have found their way into legislation on algorithmic
transparency and explainability.
2.5.1 Legal requirements for algorithmic explainability
2016
In , legal scholars started to analyze the legal foundations of ex-
2016
plainability for machine learning models [Kroll et al., , Selbst and
2018 2017
Barocas, , Wachter et al., ]. Legal scholars pointed to preexisting
obligations to explain algorithmic decisions, which existed well before
the advent of deep learning models and before the term "explainable
AI" became fashionable. These obligations were found for example in
1995
the European Data Protection Directive and in the US Fair Credit
1970
Reporting Act of .
Today explainability can be found, with different names, in numerous
EU legal texts that do not specifically target AI.
2016 679
TheGDPR(GeneralDataProtectionRegulation / ,GDPR)[Eu-
ropean Parliament and Council, 2016 ], requires disclosure of "meaningful
information about the logic involved" (articles 13 - 15 ) in fully automated de-
cisions. The GDPR provisions apply "when the decisions (i) involve the
processing of personal data, (ii) are based solely on an automated pro-
cessing of data and (iii) produce legal or significant effects on the recipi-
2021
entofthedecision"[Bibaletal., ]. AccordingtoMaxwellandDumas
2023
[ ], the GDPR requirements correspond to both local and global ex-
plainability.
Several explainability obligations concern platform regulation, which
aims at protecting consumers and business users of platforms. The Dig-
ital Services Act ("DSA") requires disclosure of "meaningful information
directlyandeasilyaccessible[...] aboutthemainparameters" of recommender
systems (art. 26 ) and more generally of the "reasons for the relative im-
portance of those parameters" (art. 27 ) [European Parliament and Council,
2022 2023
]. As stated by Maxwell and Dumas [ ], the decision of whether
the given "reasons" should faithfully and logically represent the actual
10
system behavior will be left to regulators and the CJEU . The Platform 10Court of Justice of the
to Business (P 2 B) Regulation [European Parliament and Council, 2019 ] EuropeanUnion
mandates that business users of platforms have access to information on
algorithmic parameters to allow for an "adequate understanding" of the
ranking and recommendation algorithms used, and that the main pa-
rametersandtheirimportancebejustified. TheProposedplatformwork-
ers’ directive contains similar provisions to disclose the main parame-
ters used by algoritmic systems and their relative importance. Addition-

70 the explanation paradox and the human centric path
-
ally, consumer protection law also has provisions regarding explanations
of recommender systems in online marketplaces. It notably imposes to
show "the main parameters determining ranking [...] of offers presented to the
consumer as result of the search query and the relative importance of those pa-
rameters as opposed to other parameters" (new art. 6 (a) of Directive 2011 / 83
on Consumer Rights).
2021
Bibal et al. [ ] also emphasize that explainability requirements are
stronger in the public sector. Any decision made by a public author-
ity, such as an administration or a judge, must always be justified and
reasons for the decision must be clarified and explained. When the ad-
ministrativedecision-makingprocessisautomated,furtherexplainability
requirements may be necessary. French administrative law is among the
most demanding frameworks, requiring that the person subject to the
decision be able to request the parameters used in the process and their
311 3 1 2
weighting (art. R. - - - of the French Code on the relationships be-
2023
tween the public and the administration) [Maxwell and Dumas, ].
Theabovesectiondoesnotprovideacomprehensivelistofallthepro-
visionsforexplainabilityinlegaltextsordecisions. Rather,itgivesabrief
overview of the ways in which explainability may be provided in law.
Below we extend the discussion by focusing on two of the most cross-
11
sectoriallegalfoundationsforexplainability: theupcomingAIAct and 11As this thesis was
human rights case law. written between
September 2023 and
January 2024, the final
Explainability and the AI Act
text of the AI Act had
not been published yet.
2023
In December , the EU reached an agreement on the text of the AI
Wethereforereliedona
Act, which aims to harmonise regulation on AI systems and make the near final draft version
EU the first region in the world to do so. The text promotes a regulatory inthesectionsbelow.
approach based on the level of risk that AI systems pose to fundamental
rights. It sets out different obligations depending on whether the AI
application falls into one of these four risk categories:
• Unacceptable risk: this includes systems that comprise manipulation,
exploitation,socialscoring,orbiometricidentificationofpeople. These
AI applications will be strictly prohibited, with very limited excep-
tions.
• High-risk: AI applications in critical sectors such as transport, educa-
tion, employment and health or law enforcement are among the ar-
eas concerned. For example, AI systems used to evaluate individuals’
creditworthiness are considered as high-risk. AI applications that fall
within products already regulated by EU law, such as an AI-based di-
agnostictoolusedinhealthcare,areconsideredhigh-risk. High-riskAI
system suppliers will have to carry out a prior conformity assessment
and satisfy other requirements to ensure the safety of their AI systems
before putting them into service in the EU. Suppliers are also bound
to transparency requirements to provide information on high-risk AI
systems for all stakeholders.
• Limited risk: Systems with low risk should meet basic transparency

background 71
requirements, such as informing users that they are interacting with
an AI, allowing them to make informed decisions.
• General purpose and generative AI: The initial proposal of the Euro-
pean commission did not account for "general-purpose AI models" or
2023
foundation models. The trilogue discussions in late have inte-
grated generative AI regulation in an entirely separate risk class. In-
side this class, generative AI models that are used for research and
development and not used in the EU market are exempt from obliga-
tions. OthergenerativeAImodelswillhavetocomplytotransparency
requirements such as disclosing that content was generated by an AI,
preventing the model to produce illegal content, and disclosing copy-
righted data used for training. In addition, models that may pose
4
systemic risk, such as the latest GPT- , will have to undergo more
thorough risk evaluations. Classified in this category are models for
which the compute power exceeds 1025 FLOPS.
It should be noted that the rules are designed to be evolutionary: the
definition of AI or the quantitative criteria for considering a model to
represent systemic risk could easily change.
Classification of the AI applications studied in this dissertation.
5 6
In Chapter and , we consider two applications of AI systems which
may be considered high-risk under the AI Act.
The first one involves using an AI system to provide an online rec-
ommendation for a life insurance plan that matches a user’s financial
situation. These systems are called "robo-advisors". It is clearly covered
byAnnexIIIofthedraftAIActwhichlistshigh-riskAIapplications: "AI
systemsintendedtobeusedforriskassessmentandpricinginrelationtonatural
12
persons in the case of life and health insurance." 12Annex III, paragraph
The second application of AI we consider is the detection of money
6.
launderingandterroristfinancing. Anti-moneylaunderingandcounter-
terrorismfinancing(AML-CFT)systemsareimplementedbybanks,which
arerequiredtoreportsuspicionsofmoneylaunderingorterroristfinanc-
ing in their customer base to financial intelligence units (FIUs). In turn,
FIUs investigate these suspicions in order to refer serious ones to law
enforcement authorities. It is unclear if AI systems used in AML-CFT
systems can be considered as "high risk" under the AI Act. Some schol-
2023
ars have interpreted it could be the case [Pavlidis, ], considering a
former point in the Commission proposal, which has been removed in
7
the most recent AI Act draft. Nevertheless, Annex III, point (e) and
7
specifically (f) could be interpreted as applying to AI systems in AML-
CFT:"AIsystemsintendedtobeusedbylawenforcementauthoritiesorontheir
behalf or by Union institutions, agencies, offices or bodies in support of law en-
forcement authorities for profiling of natural persons as referred to in Article
3(4)ofDirective(EU)2016/680inthecourseofdetection,investigationorpros-
ecution of criminal offences." However, recital 37 foresees an exception for
"AIsystemsusedforthepurposeofdetectingfinancialfraud". Inlightofthese
provisions, it is more likely that AI systems used by banks to enhance
ML/TFdetectionwouldnotbeconsideredhighrisk. However,onecould

72 the explanation paradox and the human centric path
-
arguethatmoneylaundering,terrorismfinancingandfinancialfraudare
2007
distinct concepts [Unger and Busuioc, ]. The systems put in place to
prevent money laundering target a larger scope of criminal offenses than
fraud, including, for example, human and drug trafficking.
The role of explainability in the AI Act.
2023
Panigutti et al. [ b] highlights that the AI Act does not mandate a
requirement for explainable AI, but rather aims to achieve trustworthy
AI through the pillars of transparency and human oversight. The au-
thors consider, however, that implementing such measures may be done
2023
through use of explainable AI. As Maxwell and Dumas [ ] notes, hu-
mans in charge of oversight should be "able to correctly interpret the high-
risk AI system’s output, taking into account in particular the characteristics of
13
the system and the interpretation tools and methods available" For Maxwell 13art. 14-4(c) of the
and Dumas [ 2023 ], this indirectly suggests the need for local explana- Commission’s proposal
fortheAIAct.
tions.
Explainability in human rights case law
14
Decisions of the Court of Justice of the European Union (CJEU) also 14CJEU, 6 October
inform us on the need for explainability with regard to fundamental 2020, La Quadrature
2023 du Net, joined cases
rightsprotectedbytheCharter[MaxwellandDumas, ]. Maxwelland
Dumas [ 2023 ] unpack those explainability requirements. In the Ligue des a C n -5 d 11/ C 1 -5 8 2 , 0/18 C ; -5 C 12 JE / U 18 ,
droits humains v. Council of Ministers case, the CJEU said that AI systems 21 June 2022, Ligue
which decisions can lead to serious consequences should rely on "pre- des droits humains v.
determined models and criteria", therefore calling for global explainabil- Council of Ministers,
CaseC-817/19
ityandexcludingtheuseofmachinelearning. Furthermore,high-riskAI
systems, such as those used for terrorism detection, should provide ex-
plainability to enable human operators to evaluate the generated alerts.
The CJEU also considers that local explainability enables contestability,
which falls within an individual’s due process rights.
2.5.2 Legal objectives for explainability
The objectives of regulation are intertwined with economic goals to
1990
correct market failures [Levine and Forrence, ] such as information
asymmetry, customer abuse, trade secrets, economic crime or distrust in
theeconomyandinstitutions. Theseregulatoryambitionsarereflectedin
the purposes of legal requirements for explainability, which are outlined
2023
by Maxwell and Dumas [ ]. Further, the appeal towards explana-
tions in legal texts can be attributed to the notion of reason-giving in
2023
law, as argued by Rozen et al. [ ], which pursues specific objectives.
Below, we summarize the explainability purposes of explainability and
2023
reason-giving as presented by Rozen et al. [ ] and Maxwell and Du-
2023
mas [ ]:
1 . Userempowerment. Requirementsforglobalexplanationsenableindi-
vidual or business users to access minimal information to understand
algorithmic recommendations and preserve their agency. This reflects
a regulatory concern to correct information asymmetries and protect

background 73
consumers. This objective corresponds to acknowledging the human
2012
agency of the decision subject as described in [Lombrozo, ].
2 . Evaluationandqualityofindividualdecisions. [MaxwellandDumas,
2023
] contends that providing local explanations may be necessary to
allow for effective human oversight of individual decisions, which is a
fundamental right protected by the EU Charter. This aligns with the
primary purpose of reason-giving in law, which is to ensure fair and
2023
just decisions [Rozen et al., ].
3 . Contestability and due process. Provisions for local explainability aim
to enable individuals to challenge decisions. This stems from regu-
latory goals to protect individuals’ fundamental rights to quality de-
cisions concerning them and due process of administrative decisions.
2021
For example, Margot Kaminski and Urban [ ] discusses what an
individualrighttocontestalgorithmicdecisionshouldlooklike,build-
ing on the United States’ tradition of due process theory.
4 . Control over system performance. Explanability is also needed to
check that systems used to pursue general interest objectives are suffi-
ciently efficient, such as AI-based anti-money laundering systems, for
example.
5 . Accountability and legitimacy of decision makers. Additionally, legal
requirements for explainability may arise from the need to preserve
2023
transparency in public administration [Maxwell and Dumas, ], in
ordertopreservepublictrustininstitutions. ThisisinlinewithRozen
2023
et al. [ ]’s view that reason-giving serve the purpose of promot-
ing compliance and legitimacy of deciding bodies. They quote Jerry
Mashaw who asserts that "the authority of all law relies on a set of com-
plex reasons for believing that it should be authoritative" [Mashaw, 2001 ].
In this context, explanations serve as accountability mechanisms in
socio-techno-legal contexts in which human deciders are concerned
with reputational risks, peers’ approval or other incentives to make
2023
the "right" decision [Rozen et al., ].

74 the explanation paradox and the human centric path
-
2.5.3 Is explainability the best disinfectant?
"Sunlightissaidtobethebestofdisinfectants;electriclightisthemostefficientpoliceman"
LouisBrandeis,1913
Explainability for decision-subjects empowerment and contestability.
Returning to Louis Brandeis’ famous saying, transparency can be seen
as a remedy to corruption and illegitimacy in politics and society. How-
ever, there are opposing views and nuances to consider. Here, the judge
takes"electriclight"asametaphorfora"technologyoftransparency"that
2020
enables effective oversight and enforcement [Obar, ]. In explainabil-
ity,itamountstogivingaccesstoexplanationsofalgorithmicdecisionsto
decision-subjects and citizens, as a way to achieve greater accountability
2017
and trustworthiness of AI systems. However, Wachter et al. [ ] state:
"the feasibility and practical requirements to offer explanations to data subjects
remain unclear." In fact, many legal scholars have criticised Brandeis’ vi-
sion as overly simplistic, advancing that it may represent an ideal, but
1993 2020
an unattainable one [Lippmann, ]. Jonathan Obar [ ] argues that
advocating transparency is one thing, but achieving "meaningful forms
of transparency" is more difficult. Taking the example of consent to per-
sonal data practices, the author observes that the self-governance fallacy
is deeply ingrained in the occidental democratic approach. Indeed, as
Pasquale [ 2015 ] puts it, "discovering problems in Big Data should not be a
burden we expect individuals to solve on their own". Obar [ 2020 ] therefore
asserts the need to recognise human limitations and to move the discus-
sion beyond on access to information, and rather towards what happens
afterwards,raisingquestionssuchashowdoweeffectivelycommunicate
information to end-users and how do we support engagement with the
content of the message? and is that even realistic?
Therefore, focusing on explanation design, representation and com-
munication could provide some answers to the propensity of explain-
ability for lay users to meet legal objectives. In the context of GDPR
2017
requirements, Wachter et al. [ ] defend that there should be more ef-
forts to "determine whether and how explanations can and should be offered
to data subjects (or proxies thereof) with differing levels of expertise and inter-
ests." We explore in Chapter 5 this tension between the capabilities and
needs of decision-subjects on the one hand, and the ideal of appropriate
trust calibration, on the other. Specifically, we explore this in the context
of AI-based recommendations for life-insuranceplans, where non-expert
end-usersshouldbegivenclear,conciseandnon-misleadinginformation
in order to make an informed choice.
Explainability for decision quality, due process and accountability.
Even for audiences other than decision-subjects and citizens, there is
growing scepticism from law scholars about whether explainability can
2023
achieve legal objectives. Rozen et al. [ ] are rather sceptical about
explainability’spropensitytocontributetotheobjectivesofreason-giving

background 75
in law.
First, for the authors, explainability cannot contribute to restraining
and slowing down human judgement for "a better and more just deci-
sion" because it is not humans but machines that are making decisions.
This objective for reason-giving in law relies on the human nature and
our capacity to "feel" accountable, which is not applicable to machines in
the XAI context.
2023
Second, Rozen et al. [ ] emphasizes the problem of unreliable ex-
plainability methods and the difficulty it creates to meet due process re-
2017
quirements. Wachter et al. [ ], also highlight that leveraging algorith-
mic audits is critical to "provide an evidence trail for providing explanations
of automated decisions." We study the role of explanations for AI auditing
6
in Chapter , where we describe the approaches and needs of regulatory
supervisors for auditing AI-based anti-money laundering systems.
Third, while explanations provide "clues" and approximations about
the model behavior, they require human deduction skills to be inter-
preted, and humans can potentially be manipulated in that process. This
makes it harder to challenge decisions and facilitate due process rights
3
relying solely on explanations. We explore this in detail in Chapter ,
where we uncover the different human biases at play in explainability
interpretation.
2023
Finally, Rozen et al. [ ] concede that explainability can play a role
instrengtheningtheaccountabilityandauthorityofdecision-makers. We
5
also explore this aspect in chapter by considering the role of explain-
abilityinstrengtheningtheaccountabilityoflifeinsuranceproviders,and
6
in Chapter , where explanations are used as means to increase account-
ability and auditability of banks regarding their AI-based anti-money
laundering systems.

PART I
| Calibrating | trust         | in explainable |     |
| ----------- | ------------- | -------------- | --- |
| AI: common  | pitfalls      | and            | the |
| promise of  | interactivity |                |     |

79
Chapter 3: Trust, overtrust, distrust in explainable AI: a cognitive ap-
proach presents a review of the cognitive biases in explainable AI litera-
ture. Thischapterbuildsonanarticlethatwaspublishedasaconference
paper:
"HowCognitiveBiasesAffectXAI-AssistedDecision-Making:ASystematicReview",Astrid
Bertrand,RafikBelloum,JamesR.Eagan,WinstonMaxwell,Proceedingsofthe2022
AAAI/ACM Conference on AI, Ethics, and Society (AIES ’22), Oxford, UK, 2022
https://doi.org/10.1145/3514094.3534164.
This thesis deepens the analysis presented in the conference paper. As
the first author, I delineated the motivation and research questions. I led
the review process and was helped by the second author to classify and
analyze the papers. I wrote most of the paper, specifically the findings
and discussion. The methods, results, and text were discussed with all
three co-authors.
Chapter 4: Towards "human-like" explanations: the promise of in-
teractivity presents a detailed scoping review on interactive explainable
AI. This chapter builds on an article that was published as a conference
paper:
"OnSelective,MutableandDialogicXAI:AReviewofWhatUsersSayaboutDifferentTypes
ofInteractiveExplanations",AstridBertrand,TiphaineViard,RafikBelloum,JamesR.
Eagan,WinstonMaxwell,Proceedingsofthe2023CHIConferenceonHumanFactors
inComputingSystems(CHI’23.),Hambourg,Germany,2023
https://doi.org/10
.1145/3544548.3581314.
Asthefirstauthor, Idelineatedthemotivationandresearchquestions.
I led the review process and was helped by the second and third authors
to classify and analyze the papers. I wrote most of the paper, specifi-
cally the findings and discussion. The methods, results, and text were
discussed with all co-authors.

| Chapter        | 3          |          |          |           |              |
| -------------- | ---------- | -------- | -------- | --------- | ------------ |
| Trust,         | overtrust, |          |          | distrust  |              |
| in explainable |            |          | AI:      |           |              |
| a cognitive    |            |          | approach |           |              |
| "Automated     | decision   | aids are | designed | to reduce | human error, |
but actually can cause new errors in the operation of a system if
| not designed | with human | cognitive |     | limitations | in mind". |
| ------------ | ---------- | --------- | --- | ----------- | --------- |
Cummings[2004]
| t the heart | of                                              |     |     |     |     |
| ----------- | ----------------------------------------------- | --- | --- | --- | --- |
| A           | human-computerinteractionresearchisthesearchfor |     |     |     |     |
optimal collaboration between humans and machines. Trust plays a sig-
nificant role in this collaborative relationship, as it determines the extent
to which users will use the machine’s advice when faced with complex
|     |     |     |     | 2013 | 2004 |
| --- | --- | --- | --- | ---- | ---- |
or uncertain situations [Culley and Madhavan, , Lee and See, ].
We therefore begin our research with a characterization of the cognitive
challenges to trust explainable AI systems. We review of the cognitive
ways in which people trust, but also overtrust, distrust or misuse expla-
nations by searching the literature in explainable AI. We highlight im-
portant individual and contextual factors in the trust calibration process.
This allows us to emphasise the relevance of human-centred approaches
| to explainability | design. |     |     |     |     |
| ----------------- | ------- | --- | --- | --- | --- |
31
Section . presents the motivation and research questions for the sur-
vey presented in this Chapter. We build on HCI research regarding hu-
man biases when working with automation, as well as on work in so-
ciology and philosophy of science regarding cognitive aspects of expla-
|     | 32  |     |     |     | 33  |
| --- | --- | --- | --- | --- | --- |
nations. Section . describes this prior research. Section . develops
34
the methodology used for the review. Section . presents the results,
including the cognitive mechanisms explanations should adapt to, the
way explanations can be misused and disused through users’ cognitive
biases, or misevaluated in user studies. We also describe the bias mitiga-
tion strategies identified in the explainability literature. Finally, Section
35
. discussesavenuesinexplainabilityresearchtotakeintoaccountiden-
tified pitfalls.

| 82 the | explanation |     | paradox |     | and | the | human | centric path |     |
| ------ | ----------- | --- | ------- | --- | --- | --- | ----- | ------------ | --- |
-
| 3.1 Motivation |     |     | and |     | research |     | questions |     |     |
| -------------- | --- | --- | --- | --- | -------- | --- | --------- | --- | --- |
Correctly calibrating trust in AI decisions and systems may be paved
withimportantcognitivechallenges,includingAutomation-InducedCom-
1993
| placency | (AIC) | [Parasuraman |     | et  | al., | ],  | and possibly | other biases. |     |
| -------- | ----- | ------------ | --- | --- | ---- | --- | ------------ | ------------- | --- |
While there are growing efforts from researchers [Green and Chen,
| 2019          |     |     | 2019 |     |         |     | 2020 |                    |      |
| ------------- | --- | --- | ---- | --- | ------- | --- | ---- | ------------------ | ---- |
| , Mittelstadt |     | et  | al., | ,   | Rastogi | et  | al., | ] to tie cognitive | sci- |
ence literature to a mostly technical explainability field, more research
is needed to identify what kind of cognitive biases and heuristics are
involved in the explanation process, and whether and how to leverage
people’s heuristics to improve XAI systems. Several studies exist that
shedlight oncognitivemechanismsleading issueswheninterpreting ex-
|     |     |     |     |     |     |     | 2021 |     | 2019 |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- |
planations of AI systems [Chromik and Butz, , Wang et al., a].
However,theliteraturelacksacomprehensivereviewoftheeffortsmade
so far on this front in the explainable AI field. In this chapter, we fo-
cus on cognitive biases in order to pin down the cognitive challenges to
| fostering | appropriate |     | trust | in explainable |     | AI. |     |     |     |
| --------- | ----------- | --- | ----- | -------------- | --- | --- | --- | --- | --- |
To the best of our knowledge, there is not yet a comprehensive review
of how cognitive biases have been accounted for in the explainability lit-
erature. A analysis like the one we present appears necessary to summa-
rize findings on how cognitive biases interfere with explanations, how
to address them, and to highlight promising directions concerning the
| integration | of  | cognitive | processes |     | in XAI | systems. |     |     |     |
| ----------- | --- | --------- | --------- | --- | ------ | -------- | --- | --- | --- |
Inthiswork,weconsidercognitivebiasesnotonlyintermsof“errors”
(e.g., automation bias that leads to inappropriate trust in AI modes) but
also as the cognitive constraints that are inherent in the human explana-
tion process.
We analyze how the field of XAI has been dealing with human cogni-
tive biases and constraints, and we discuss promising mitigation strate-
gies and research directions to support human critical thinking. To this
38
end, we conducted a scoping review of papers, based on a systematic
searchmethodology,andguidedbythefollowingfiveresearchquestions:
RQ1: What cognitive biases have been studied in the explainability literature?
RQ2: In which contexts (e.g., explainability method, human expertise, tasks
| type) | do these | cognitive | biases | arise? |     |     |     |     |     |
| ----- | -------- | --------- | ------ | ------ | --- | --- | --- | --- | --- |
RQ3: How to adapt to human cognitive architecture to improve explainable AI
systems?
RQ4: What evaluation methods have been used to detect cognitive biases (spe-
| cific to | each bias)? |     |     |     |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
RQ5: Whatarethestatedfutureresearchdirectionsandchallengesidentifiedby
| the scientific |     | community? |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |

trust overtrust distrust in explainable ai a cognitive approach 83
|     |     |     | ,   |     |     | ,   |     |     | :   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3.2 Background
|     | 3.2.1 | Trust |     | in automation |     |     |     |     |     |
| --- | ----- | ----- | --- | ------------- | --- | --- | --- | --- | --- |
DecadesofresearchattheintersectionofpsychologyandHCIresearch
highlight important and pernicious challenges to appropriately calibrate
trust in automated intelligent decision support systems [Parasuraman
|     |        | 1997         |          |      |             | 2007 |                    | 1992 |           |
| --- | ------ | ------------ | -------- | ---- | ----------- | ---- | ------------------ | ---- | --------- |
| and | Riley, |              | , Bailey | and  | Scerbo,     |      | , Lee and Moray,   |      | , Wickens |
|     | 2009   |              |          | 2004 |             |      | 2004               |      |           |
| et  | al.,   | , Gawronski, |          |      | , Cummings, |      | ]. This literature |      | emerged   |
from the study of complex systems in critical environments, specifically
1990
the aeronautics in the s. The analyses of plane crashes, such as the
1996 accident[NationalTransportationSafetyBoard, 2000 ], shedlighton
difficulties for pilots in understanding system warnings, detecting au-
tomation errors or monitoring highly reliable systems, leading to catas-
| trophic | consequences |     |     | [Billings, | 1996 | ].  |     |     |     |
| ------- | ------------ | --- | --- | ---------- | ---- | --- | --- | --- | --- |
Definition
Complacency. Parasuraman et al. [1993] described the phenomenon of
Automation-InducedComplacency(AIC),whichisastateof"lowsuspicion"
by the human operator when the automation performs a task for them, also
|     | defined | as "self-satisfaction" |     |     | resulting | in  | non-vigilance". |     |     |
| --- | ------- | ---------------------- | --- | --- | --------- | --- | --------------- | --- | --- |
The term "complacency" is necessary because it encompasses constructs
broader than vigilance failure, boredom, or workload issues. Compla-
cency represents a unique attitude, and complacency and boredom are
| not | connected | [Parasuraman |     |     | et al., | 1993 | ].  |     |     |
| --- | --------- | ------------ | --- | --- | ------- | ---- | --- | --- | --- |
A related notion in the literature is automation bias. According to
2004
| Cummings |     | [   | ]:  |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Definition
Automation bias. Automation bias "occurs when a human decision
maker disregards or does not search for contradictory information in light
of a computer-generated solution which is accepted as correct" [Cummings,
2004].
Complacency and automation bias have often been discussed as sep-
arate concepts in the literature [Parasuraman and Manzey, 2010 ]. On
the one hand, complacency involves a lack of attention, predominantly
observed in conditions of multitasking, and high automation reliability.
On the other hand, automation bias is seen as a tendency to overtrust
decision-support systems. By noting these differences, we can see that
they are due to variances in the observation of these concepts. However,
ultimately both notions result in the same underlying problem. If we
2020
take Ferrario et al. [ ]’s definition of trust which involves the lack of
monitoring, automation bias becomes very similar to complacency. In
2010
fact, Parasuraman and Manzey [ ] argued that "automation-induced
complacency and automation bias represent closely linked theoretical
concepts that show considerable overlap with respect to the underlying
processes". Therefore, for simplicity, we will consider the two terms as
| synonymous |     | in  | the remainder |     | of  | the dissertation. |     |     |     |
| ---------- | --- | --- | ------------- | --- | --- | ----------------- | --- | --- | --- |

| 84 the | explanation |     | paradox | and the | human | centric | path |     |     |     |
| ------ | ----------- | --- | ------- | ------- | ----- | ------- | ---- | --- | --- | --- |
-
Additionally,wesummarizebelowsignificantfactorsdeterminingtrust
2013
in automation, building on Culley and Madhavan [ ]’s review. These
factors include: variability of system reliability, operator cognitive load
(e.g. multitasking), alarm threshold, severity of the consequences of fail-
| ure or trust | in  | the system | designer. |     |     |     |     |     |     |     |
| ------------ | --- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Human operators are not well suited to monitoring infrequent and
unanticipated problems in complex systems, particularly when the sys-
temishighlyreliableandtheoperatorismultitasking[BaileyandScerbo,
2007 , Parasuraman et al., 1993 ]. In general, system reliability and perfor-
2007
mance have a great effect on operator trust [Bailey and Scerbo, ].
AIC occurs over time, after a period of familiarisation with automation
[Molloy and Parasuraman, 1996 ]. Varying system reliability eliminates
|     |     |     |     | 1993 |     |     | 2007 | 1   |     |     |
| --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
complacency effects [Parasuraman et al., , Bailey and Scerbo, ] . 1During the 1990s, Air-
Wickensetal.[ 2009 ]investigatedthe"crywolfeffect",wherebylowalarm bus planes were the
|     |     |     |     |     |     |     |     | most | automated | com- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ---- |
thresholds and a surplus of alarms result in an operator’s distrust and
|     |     |     |     |     |     |     |     | mercial | planes | in op- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------ |
disregard of the alarm system, potentially leading to the neglect of true
|     |     |     |     |     |     |     |     | eration. | To  | prevent |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- |
alerts.
|     |     |     |     |     |     |     |     | automation | bias, | pilots |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------ |
When systems make mistakes, the loss of trust is proportional to the werewarnedagainstbe-
|     |     |     |     |     |     |     | 2013 | coming | excessively | de- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ----------- | --- |
severity of the consequences of the failure [Culley and Madhavan, ].
|     |     |     |     |     |     |     |     | pendent | during | train- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------ |
However, difficult or near misses can result in a lower loss of confidence
|           |     | 2006 |     |     |     |     |     | ing. | Following   | an Air- |
| --------- | --- | ---- | --- | --- | --- | --- | --- | ---- | ----------- | ------- |
| [Madhavan | et  | al., | ].  |     |     |     |     |      |             | 1992,   |
|           |     |      |     |     |     |     |     | bus  | plane crash | in      |
ParasuramanandRiley[ 1997 ]alsoemphasisedtheimportanceoftrust
|     |     |     |     |     |     |     |     | French | airlines | imple- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------ |
in the human designer of the system as a key factor in calibrating trust mented a policy requir-
ingpilotstoperiodically
in automation.
|     |     |     |      |     |     |     |     | take              | manual control | of  |
| --- | --- | --- | ---- | --- | --- | --- | --- | ----------------- | -------------- | --- |
|     |     |     | 2004 |     |     |     |     | automatedsystems. |                |     |
Finally, Lee and See [ ] introduced the notions of resolution and
specificity
|     | of  | trust. Resolution |     | is the ability | to adjust | one’s | confidence |     |     |     |
| --- | --- | ----------------- | --- | -------------- | --------- | ----- | ---------- | --- | --- | --- |
in proportion to changes in the system’s capabilities. A person with a
low confidence resolution will only slightly change their confidence in a
system that has undergone major changes to its capabilities. Specificity
refers to the ability to calibrate one’s trust in all the different system’s
| distinctive | components. |     |            |       |         |     |     |     |     |     |
| ----------- | ----------- | --- | ---------- | ----- | ------- | --- | --- | --- | --- | --- |
| 3.2.2       | Trust       | in  | automation | by AI | systems |     |     |     |     |     |
40
Over years after a first research wave on automation provided by
intelligentdecision-supportsystems,withthedifferencethatsystemsare
even more complex and opaque. Findings from early research on trust
2019
in automation appear more topical today than ever [Zerilli et al., ,
| Cummings, | 2004 | ].  |     |     |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2020
Glikson and Woolley [ ] highlight the differences between the tra-
ditionalautomationthatwasthesubjectofearlystudiesoncomplacency
and automation of decisions by modern AI systems. They define tra-
ditional automation as "systems that perform repetitive and monotonic tasks
that were previously performed by humans" [Parasuraman and Riley, 1997 ,
2020
Glikson and Woolley, ]. These systems are deterministic and their
behavior is known and fully pre-programmed. On the contrary, machine
learning models execute tasks significantly differently from the human
approach, primarily because of their probabilistic nature and ability to
| learn from | large | data. |     |     |     |     |     |     |     |     |
| ---------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |

trust overtrust distrust in explainable ai a cognitive approach 85
, , :
2020
Glikson and Woolley [ ] then review studies on trust in AI and re-
veal six factors enabling cognitive and emotional trust. These are tangi-
bility, transparency, reliability, task characteristics, immediacy behaviors
and anthropomorphism. Tangibility refers to the different forms that AI
can embody, from physical presence as in the case of robots, to virtual
agents or bots or to AI embedded in computers. Humans tend to trust
more AI systems that are more tangible in this order: physical > virtual
> embedded. Transparency and explanations of AI systems tend to in-
crease trust. Low levels of reliability significantly reduce trust, and it
is difficult and time-consuming to regain it. For tasks that require data
analysis, AI is trusted more while for tasks that require social skills, AI
is trusted less than humans. Immediacy behaviors refer to personaliza-
tion, interactivity, adaptiveness and responsiveness, which are usually
associated with increasing trust.
2021
Furthermore, Stanton and Jensen [ ] identify other factors that af-
fecthumantrustinAI,namelyusabilityofAIsystems(i.e. theuserexpe-
rience), and the technical characteristics identified by HLEG’s definition
of trustworthy AI (accuracy, reliability, security, explainability, privacy...)
2019
Zerilli et al. [ ] also ties the research on complacency and trust in
automationbyintelligentsystemswiththemorerecenttrendsinautoma-
tion by machine learning and AI systems.
2019
Zerilli et al. [ ] focus on the "control problem", which is broader
than the issue of trust in automation. Control here pertains to the ca-
pacity to diagnose and address faults or issues as they arise in real-time,
as well as to proactively address future issues. Zerilli et al. decompose
the control issue into three main sub-problems: the capacity, attentional
and attitudinal problems. The capacity problem refers to the lack of pro-
cessing power of human architecture compared to computer processing,
that make them inherently unable to monitor in real time a task they
1983 2019
cannot do themselves [Bainbridge, ]. Zerilli et al. [ ] argue how
this becomes particularly salient in the age of deep learning, where even
software engineers cannot fully understand the "multi-vector logic" of a
neural network. The attentional problem refers to humans’ limits in term
of attention over time. It refers to studies on "vigilance" that point to the
cognitive impossibility for humans to maintain effective visual attention
1983
on an interface on which little happens [Bainbridge, ]. Finally, the
attitudinal problem refers to humans’ tendency to believe that the system
is reliable enough to be left alone. It therefore refers precisely to a trust
calibrationissue,andtotheobservationsincomplacencyandautomation
bias studies.
Overall, research in psychology and HCI has shown that humans are
at a severe disadvantage to occupy monitoring functions of complex and
1983 2019
autonomous systems [Bainbridge, ]. Zerilli et al. [ ] claim that
there are no reason to believe that the human tendencies observed with
early automation, that result from million years of evolution, would not
manifest with machine learning systems. Does this mean that human
2019
and AI collaboration is doomed? Zerilli et al. [ ] add nuance to that
view. First, some AI systems show impressive levels of performance that
exceed those of well-trained humans, making it inconsequential that hu-

86 the explanation paradox and the human centric path
-
mans cannot monitor machine decisions. For example, there are AI sys-
80
tems which can detect Alzheimer’s disease with over % accuracy ten
years before the appearance of the first symptoms. Depriving ourselves
of the capabilities of this algorithm for reasons of human control would
2019
beamajoropportunitycostforhealthcare. Second,Zerillietal.[ ]ar-
gue that in acknowledging unavoidable human biases with automation,
we can work towards complementary and dynamic allocation of tasks
between humans and AIs.
Inthiscontext,explainabilityrepresentsanadditionalwayoutofwhat
seems like a dead end for appropriate human oversight and trust cal-
ibration. It promises to remedy to the capacity problem by producing
human-intelligible explanations and potentially to the attitudinal prob-
lem by enabling correct trust calibration. However, Glikson and Wool-
2020 2021
ley [ ] and Stanton and Jensen [ ] point out studies that showed
that transparency overall reinforce trust. The effects of explainability for
human cognitive architectures and cognitive trust mechanisms are still
unclear.
This chapter focuses on the concept of cognitive bias to examine how
explanations can either bolster or undermine trust in AI.
3.2.3 Explanations are biased and (maybe) biasing
"Inthecontextofexplanationandrevision,thestrengthofcausalreasoningandtheweaknessof
diagnosticreasoningaremanifestinthegreateasewithwhichpeopleconstructcausalaccountsfor
outcomeswhichtheycouldnotpredict".
[Kahnemanetal.,1982]
In theory, explainability ought to serve as an aid for humans to regain
control of AI black-boxes, restore their autonomy in decision-making
with AI, and prevent their errors like complacency or automation bias.
Naturally, reality is not so simple. On the contrary, some results high-
light the harmful potential of explanations to amplify automation biases
2021 2021
inhigh-stakessettings[Jacovietal., ,Eibandetal., ,Wangetal.,
2019
a]. These findings are in line with previous research in the context
of intelligent decision support systems that show that automation deci-
sion aids could cause new errors instead of reducing them [Cummings,
2004 2006
, Madhavan et al., ]. In fact, human cognitive architecture is not
2022
something that can be "fixed" [Lindström et al., ]. However, it is a
2004
key element for technology designers to consider [Cummings, ].
In this section, we review the cognitive processes involved in expla-
nation and the way they are inherently biased, which is not necessarily
"bad" per se.
1980
In the s, Amos Tversky and Daniel Kahneman [Kahneman et al.,
1982
] introduced the concept of cognitive bias as:

trust overtrust distrust in explainable ai a cognitive approach 87
, , :
Definition
Cognitive biases. “Systematic error in judgment and decision-making
commontoallhumanbeingswhichcanbeduetocognitivelimitations,moti-
vational factors, and/or adaptations to natural environments.”
2011 2011
In ,Kahnemandevelopedthedual-processtheory[Kahneman, ],
inwhichhedescribedtwosystemsthatillustratethewaywethink. "Sys-
1
tem " reflects our fast, intuitive and emotional thinking which often
2
leads us to make errors. "System " is more deliberative, logical, but also
requires more effort to activate.
1
System , and cognitive biases do not necessarily have bad conse-
quences or results: they have been developed over the course of our
evolution to help us think faster, interact better with our peers or keep
2011
us safe [Kahneman, ]. Kahneman also describes the extraordinary
1
abilities that result from our System . These biases should be seen as
constraints on the problem of explainability, as integral aspects of our
human nature.
23
As seen in Section . , cognitive biases and social expectations are
present when people evaluate and generate explanations.
Specifically,peopleselectcausesinabiasedwaybypayingmoreatten-
2019
tion to causes that have specific characteristics [Miller, ]. Lombrozo
2006
[ ] talks about "the frailties of induction". As for Pennington and
1993
Hastie[ ], anexplanationisastorythatcoherentlyputsallthepieces
of evidence together to give them causal sense. The produced story is
subjective, as it depends on the explainer’s world knowledge about sim-
ilar events, or even knowledge about story structures. Graaf and Malle
2017
[ ] also argue that people have social expectations towards machines
because they attribute human traits to them. For example, we expect AI
explainers to use the framework of conversations, or tend to attribute in-
2017 1980
tentstothem[GraafandMalle, ,DoddandBradshaw, ]. Wealso
have cognitive biases in interpreting explanations. Although generalis-
ing from explanations is necessary and useful for learning and problem
solving, it can come at the cost of over-generalising. We have previously
231
discussedinSection . . thatgeneralisationissignificantlylinkedtothe
2006
similarity and diversity of the properties involved [Rehder, ]. Lom-
2006
brozo[ ]arguesthatthesefactorscanleadpeopletoover-generalizeif
anovelcaseseemssimilartothecasethatisexplainedorifthepresented
explanation seems to hold true in a diverse range of contexts. Specifi-
cally,explanationsreinforcethateffect"byprovidingamorerestrictivebasis
for generalizing from known to novel cases".

| 88 the | explanation | paradox | and | the human | centric path |     |
| ------ | ----------- | ------- | --- | --------- | ------------ | --- |
-
"Explanationscanleadreasonerstooverridetheinfluenceofsimilarity. Iftoldthatherringandtuna
haveadisease,naiveparticipantsaremorelikelytoextendthepropertytowolffish,themoresimilar
item,thantodolphins[ShaftoandColey,2003]. However,amongfishingexperts,whocangenerate
anexplanationforwhythepropertymighthold(e.g. tunacontractthediseasebyeatinginfected
herring),similarityislesspredictiveofpropertyextensions. Instead,propertiesareextendedifthe
| explanationgeneralizes(e.g. |     | todolphins,whoalsoeatherring)." |     |     |     |     |
| --------------------------- | --- | ------------------------------- | --- | --- | --- | --- |
Extractfrom[Lombrozo,2006].
Although many studies have shown that XAI methods can improve
users’ understanding of black-box models [Lakkaraju et al., 2017 , Lucic
| 2020 |     |     | 2018 |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- |
et al., , Ribeiro et al., ], recent empirical studies have drawn
attentiontoobstaclesresultingfromamismatchbetweenpeople’scogni-
tive constraints and current XAI techniques. Specifically, there have been
concerns that AI explanations can bias users and impair their decision-
making process [Ghassemi et al., 2021 , Kaur et al., 2020 , Nourani et al.,
| 2021  |             |            |          |                | 1985       |     |
| ----- | ----------- | ---------- | -------- | -------------- | ---------- | --- |
| ]. At | the root of | the issue, | Buchanan | and Shortliffe | [ ] argue, | is  |
the choice between trusting an AI recommendation or engaging in an
effortful and time consuming cognitive analysis of its explanations (i.e.
2
engaging System ). People thus develop biases "about whether and when
tofollowtheAIsuggestions"[Buçincaetal., 2021 ],andAIexplanationscan
| reinforce | such biases. |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- |
For example, explanations can lead to unwarranted trust in AI recom-
|     |     | 2021 |     | 2019 |     |     |
| --- | --- | ---- | --- | ---- | --- | --- |
mendations [Jacovi et al., ]. Eiband et al. [ ], show that placebic
explanationselicitasimilarleveloftrustasrealexplanations. Otherwork
|     | 2021 |     |     | 2020 | 2021 |     |
| --- | ---- | --- | --- | ---- | ---- | --- |
[Chromik et al., , Fürnkranz et al., , Nourani et al., , Wang
2019
et al., a] shows that explanations can cause reasoning errors such
as backward reasoning and confirmation bias. Leveraging Kahneman’s
2021
dual process theory, Kliegr et al. [ ] reviewed the effects of cognitive
biases on the interpretation of AI models and provide a rich analysis of
over 20 different biases. That work, however, focuses on rule-based ex-
2019
planations. In turn, Wang et al. [ a] propose operational pathways
between users’ reasoning needs and XAI methodologies. They describe
howpeoplereasonwhenexplainingandreviewsomecommoncognitive
biases and the ways in which they can be mitigated. However, this work
doesnotcomprehensivelycoverthecognitivebiasesthatmayariseinthe
| presence | of explainable | AI. |     |     |     |     |
| -------- | -------------- | --- | --- | --- | --- | --- |

trust overtrust distrust in explainable ai a cognitive approach 89
, , :
3.3 Methodology
In this section, we detail the method used for the scoping literature
review and how we selected the papers for inclusion.
3.3.1 Review type
1994
Likeasystematicreview[Mulrow, ],ascopingreview[Arkseyand
2005
O’Malley, ] includes many rigorous steps to survey the literature.
Scoping reviews do not require the pre-registration of the results nor the
2018
assessment of the quality of the studies [Munn et al., ] as systematic
reviews do, but they include similar methodological steps: the definition
of research questions, a systematized search and selection process, and
2005
an analysis and reporting the results [Arksey and O’Malley, ]. We
followedthestandardizedsearchandselectionmethodsfromthesystem-
2005
atic review methodologies, as suggested in [Arksey and O’Malley, ]
for scoping reviews, to ensure the replicability and transparency of our
findings. In particular, we followed the steps of the Preferred Reporting
Items Systematic Reviews and Meta-Analyses (PRISMA) standard [Mo-
2009
heretal., ]: paperidentification,screening,eligibilityevaluationand
analysis procedure. In doing so, it is possible to reproduce the processes
of searching, selecting, and analyzing the relevant literature. This allows
us to guarantee the quality of our search and selection process, as en-
couraged by the PRISMA Extension for Scoping Reviews PRISMA-ScR
2018
[Tricco et al., ].
Scoping reviews are an appropriate survey type to examine how re-
search is conducted on a specific topic, give a summary of the focus of
the field, map key concepts, identify the types of evidence found in a
field, pave the way for future systematic reviews, and identify gaps in
2018
the literature [Munn et al., ]. This corresponds to the objectives of
study: identify, map, report and discuss the available evidence on cogni-
tive biases in XAI.
3.3.2 Corpus creation
Our aim was to give a sense of how the XAI literature has addressed
the notion of cognitive biases so far. We therefore relied on a keyword-
based approach, which essentially has the advantage of ensuring trans-
parency,reproducibilityand,also,leadingtomorecomprehensiveresults
bysamplingawiderangeofwork. However,itispossiblethatsomeXAI
articles have addressed the notion of cognitive biases in different terms,
referring to specific types of cognitive bias. However, we could not in-
clude all possible types of cognitive biases as keywords, since there are
200
over . We also did not want to focus the investigation on specific
typesofbiasinordertoprovideamorerepresentativeviewofthediffer-
ent cognitive biases discussed in explainability. In addition, because we
conductedoursearchesonACM,IEEE,andScopus,wemayhavemissed
other relevant work from other sources. To address these limitations, we

| 90 the explanation | paradox | and the | human centric path |
| ------------------ | ------- | ------- | ------------------ |
-
supplemented the keyword-search with selected papers addressing cog-
nitivebiasesinXAIdrawnfromtwoauthors’knowledgeoftheXAIfield.
Section 36 . discusses the limitation of the methodology in further detail.
3.1:
Figure PRISMA
Keyword Match. During the identification phase, we performed a flow diagram [Moher
2009]
et al., on how the
structured keyword search using the following sources: ACM, IEEE, and
finalcorpuswascurated
Scopus. Since this survey focuses on cognitive biases related to XAI,
(n=38).
the search query was contextualized in three dimensions: AI systems,
Explainability, and Cognitive biases. Drawing on the authors’ back-
ground in XAI, we assigned keywords that describe each dimension. We
searched for keywords representing AI systems and Explainability di-
mensions in the Title, Abstract, and Author Keywords fields, because we
wantedtofocusonpaperswhosemaintopicwasXAI.ForCognitivebias
keywords, we searched in the Full text of papers. The search result was
filtered to include recent papers ( 2008 or after) since XAI is a young field
of study. The search query was as follows, adapted to each database ad-
vanced search specificities (the wildcard * indicates where we retrieved
| plurals and different | spellings): |     |     |
| --------------------- | ----------- | --- | --- |
AI systems: Abstract: (AI, artificial intelligence, machine learning, algo-
| rithm*, intelligent | system*, | neural network*) | AND |
| ------------------- | -------- | ---------------- | --- |
Explainability: Abstract: (explainab*,explanation*,intelligib*,interpretab*,
| transparen*, | XAI) AND |     |     |
| ------------ | -------- | --- | --- |
Cognitive biases: Full Text: (cognitive bias*, decision bias*, explanatory
| bias*, explanation | bias*, | human bias*) AND |     |
| ------------------ | ------ | ---------------- | --- |
| Date: 2008 and     | after. |                  |     |
Screening and Eligibility. We considered the following inclusion and
exclusion criteria. The logic followed is (IC1 OR IC2 OR IC3) AND EC.
IC1 Cognitive biases. The paper describes cognitive biases that are in-
| volved in the | field of XAI. |     |     |
| ------------- | ------------- | --- | --- |
IC2 Mitigation techniques. The paper describes techniques to mitigate
| cognitive biases | involved | in the XAI process. |     |
| ---------------- | -------- | ------------------- | --- |
IC3 Measurementtechniques. The paper describes ways to measure cogni-
| tive biases related | to explanations. |     |     |
| ------------------- | ---------------- | --- | --- |

trust overtrust distrust in explainable ai a cognitive approach 91
, , :
EC Papersthat donot provideprimary insightson cognitivebias inXAI
areexcluded(e.g.,apaperthatdoesnotprovideenoughdetailonhow
the heuristics manifest and in what context).
Additionally, only peer-reviewed papers written in English were in-
cluded. We excluded very few papers to which we did not have access.
273 59
The identification phase yielded a total of results: papers from
64 150 12
ACM, from IEEE, from Scopus, and additional papers selected
from the references of relevant papers or based on the authors’ knowl-
edge. The authors’ names, article title, source title, and publication year
of the identified records were exported to an Excel spreadsheet. A to-
261 24
tal of results were obtained after eliminating duplicates. In the
screening stage, each paper’s title and abstract was reviewed by an au-
thor based on the inclusion and exclusion criteria, and a decision was
made as to whether the paper should be rejected or retained for the next
176
phase(eligibility). paperswereexcludedbecausetheydidnotdiscuss
85
cognitive biases involved in the field of XAI. A total of papers were
advanced to the next phase. In the eligibility stage, two of the authors
read the remaining articles in full. Based on the inclusion and exclusion
criteria, a decision was then made as to whether the article should pro-
48
ceed to the final phase. articles were finally excluded at this stage
because they did not sufficiently address the proposed research ques-
38
tions (cf. introduction). articles were retained and advanced to the
final phase.
Coding book. In the inclusion stage, we started the coding of the pa-
persbyhavingtwoauthorsextractrelevantinformationfromthepapers.
Except for the type of article (primary study or survey), this informa-
2
tion essentially relates to RQ (see introduction). To ensure coding qual-
ity, this information was brainstormed by the authors and the research
team and was drawn from related surveys of empirical studies of XAI
(e.g., [Lai et al., 2021 ]). As such, our code book included: Cognitive bias
type; Mitigation strategy; Explainability technique and format (local fea-
ture explanation, global explanation, etc.); Paper type (primary study or
review); Application/domain (high-risk or low risk); AI type (shallow,
deep or wizard of oz) and algorithm used (when specified); Human task
type (proxy or real and description); Human expertise (lay-user, domain
31
expert or ML expert). The full code description is presented in Table . .
Corpuspresentation. Inthecorpusof 38 papersweanalyzed, 7 papers
31
are reviews of the literature, and papers are primary studies. Figure
2
illustrates the distribution of our corpus across the disciplines, show-
ing the diversity of the subject areas. As we can see, over half of these
papersareHumanComputerInteraction(HCI)works,publishedinlead-
ingconferences(e.g.,CHIandIUI).Theremainingpapershavealsobeen
published in leading conferences and journals directly or indirectly re-
lated to the explainability of AI systems, in the fields of AI, computer
science and psychology.

| 92 the | explanation |     | paradox |     | and | the | human | centric |     | path |     |     |
| ------ | ----------- | --- | ------- | --- | --- | --- | ----- | ------- | --- | ---- | --- | --- |
-
3.1:
| Dimension |     | Codewithexamplesfoundinthecorpus                         |     |     |     |     |     |     |     |     | Table Coding          | book |
| --------- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | ---- |
|           |     |                                                          |     |     |     |     |     |     |     |     | used for the analysis | of   |
| AItypes   |     | Deeplearningmodels(deepreinforcementlearning,RoBERTa,Re- |     |     |     |     |     |     |     |     |                       |      |
thecorpus.
|     |     | ID  | networks, | BERT, | CNN | VGG-19, | deep | neural | network | based on |     |     |
| --- | --- | --- | --------- | ----- | --- | ------- | ---- | ------ | ------- | -------- | --- | --- |
GoogleNet),Shallowmodels(LASSOregression,GAM/sLM,De-
|     |     | cision | trees, | logistic | regression, |     | 1 to 2 | layer neural | network, | Ran- |     |     |
| --- | --- | ------ | ------ | -------- | ----------- | --- | ------ | ------------ | -------- | ---- | --- | --- |
domforestclassifier,GAMandgradientboosteddecisiontrees(Light-
GBM),SVM,linearregression,Multi-labelgradientboostedtree,k-
nearestneighborandbaggeddecisiontree),WizardofOz
| Explanation |     | Local            | feature          | importance   |                                               | (saliency |             | maps,       | word highlighting, |             |     |     |
| ----------- | --- | ---------------- | ---------------- | ------------ | --------------------------------------------- | --------- | ----------- | ----------- | ------------------ | ----------- | --- | --- |
| types       |     | LIME,            | SHAP,            | sensitivity  |                                               | analysis  | MOEA/D...), |             | Rule-based,        |             |     |     |
|             |     | Example-based    |                  | (MMD-critic, |                                               | nearest   |             | neighbours, | manual             | induc-      |     |     |
|             |     | tive             | explanation...), |              | Counterfactual                                |           | (LORE,      | other...),  |                    | Textual (in |     |     |
|             |     | naturallanguage: |                  |              | expert-generatedorautomatic),Uncertaintyesti- |           |             |             |                    |             |     |     |
mation,OtherGlobal(distributionofvalues,decisiontree,output
visualisation)
| Userexpertise |     | Domainexpert,Machinelearningexpert,Layuser,Researcher        |                   |                                                     |              |             |            |         |              |          |     |     |
| ------------- | --- | ------------------------------------------------------------ | ----------------- | --------------------------------------------------- | ------------ | ----------- | ---------- | ------- | ------------ | -------- | --- | --- |
| Tasksand      |     | Artificial                                                   |                   | task (sentimentanalysisofbookandbeerreviews,predic- |              |             |            |         |              |          |     |     |
| domains       |     | tionoffatcontentinafoodimage,predictionoftrafficaccidentsina |                   |                                                     |              |             |            |         |              |          |     |     |
|               |     | country...),                                                 |                   | Law and                                             | regulation   |             | (child     | welfare | screening,   | identity |     |     |
|               |     | recognition,                                                 |                   | recidivism                                          | prediction), |             | Business   | and     | finance      | (credit  |     |     |
|               |     | scoring,                                                     | house             | price                                               | estimate),   |             | Education, | Leisure | (chess,      | mu-      |     |     |
|               |     | sic                                                          | recommendations), |                                                     |              | Healthcare, |            | Others  | (application | to lose  |     |     |
weight,professionprediction,imagerecognition...)
Identification of cognitive biases. To identify by name the cognitive
effects that were discussed in the papers we reviewed, we either took the
wordingusedinthepapers,orreliedonexternaltaxonomies[Kahneman,
| 2011       |     |     | 1982 |            |     |        |         |     | 2021 |            |     |     |
| ---------- | --- | --- | ---- | ---------- | --- | ------ | ------- | --- | ---- | ---------- | --- | --- |
| , Kahneman |     | et  | al., | ], surveys |     | (e.g., | [Kliegr | et  | al., | ]), and on |     |     |
our own knowledge of cognitive biases, specifically when the bias was
not named explicitly. For a few cases we coined a phrase to be able
to refer to the effect under study (e.g. “pre-use algorithmic optimism”
| [Springer | and | Whittaker, |     | 2019 ]). |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure3.2:
Thedistribu-
tionofthecorpusacross
| 3.4 | Results |     |     |     |     |     |     |     |     |     | disciplines. |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
This section presents the results of the analysis of the articles studied.
1
First, we give an overview of the biases identified (RQ ). We then exam-
ine the stated mitigation strategies as well as the research methods used
|     |     |     | 2   | 3   | 4   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to identify them (RQ , RQ and RQ ). For the sake of brevity, we do not
systematically provide the definitions of the biases we examine, but the
| interested | reader | can | refer | to the | lexicon | provided |     | in Appendix |     | A 1 . |     |     |
| ---------- | ------ | --- | ----- | ------ | ------- | -------- | --- | ----------- | --- | ----- | --- | --- |
1
The first contribution of this work is to answer our RQ and identify
the cognitive biases encountered in our corpus, along with the context
in which they were found, namely the explainability technique that was
used, the domain, the task, and the user type. We identified a list of
cognitive biases in Appendix A 1 . The list presents all the expressions
and concepts found in the corpus, but we recognise that some concepts
may overlap and represent the same underlying cognitive mechanism.

trust overtrust distrust in explainable ai a cognitive approach 93
, , :
We then analyzed the way these biases were presented in the articles
reviewed,revealingfourmainwayscognitivebiasesaffectorareaffected
by the use of explainable AI systems for decision-making.
3.4.1 Overview
33
Figure . presents the different categories of explanation techniques
that were seen in our corpus (in the middle). Each link represents a con-
nection made in the literature between an explainability technique and
a cognitive bias or between a cognitive bias and a mitigation technique.
The legends in color underlined by arrows indicate how and in what di-
rection the links should be read (e.g. "XAI techniques should adapt to
explanatory heuristics"). The pale and wide links indicate that the bias
or constraint applies more generally to all XAI methods. We identified
moreconnectionsbetweenbiasesandmitigationstrategiesbutshowonly
the most supported ones for brevity.
Figure 3.3: Summary
of the cognitive con-
The first type are heuristics and characteristics of users that should straints, biases and mit-
igation strategies dis-
affect how explainable AI systems are designed. They are listed in
cussed in the papers in-
the yellow boxes in Figure 3 . 3 (top-left corner). They include all the
cluded in our corpus
explanatory heuristics that people use when explaining or receiving an (n=38).
explanation. These explanatory heuristics are well documented in psy-
2007
chological works on the human explanation process [Lombrozo, ,
2019
Miller, ]. Unlike the other types of cognitive biases discussed in our
survey, these explanatory heuristics are not considered to lead to errors.
Onthecontrary,theyweresimplypresentedasneithergoodnorbadbut

94 the explanation paradox and the human centric path
-
merely cognitive architecture constraints to be taken into account before
342
designing explainability techniques. We present them in Section . . .
The second type of cognitive biases are those caused or exacerbated
by explainability, and which can lead to erroneous decision-making.
TheyarepresentedintheredboxesontherightofthediagraminFigure
33
. . Among these, we find cognitive biases that lead either to overtrust,
distrust, or to misusing the explanation. We present these in Sections
343 344 345
. . , . . and . . .
The third category are cognitive biases that were successfully cor-
rected by explainable AI. They are presented in the orange box in Fig-
3 346
ure (top-right corner). In Section . . , we review successful examples
of using an explainability technique to address a false belief that was
observed with non-explainable AI systems.
The fourth category we identified are cognitive biases which can dis-
tort how XAI techniques are evaluated in user studies. They are pre-
sented in the brown box in Figure 3 . 3 (middle left). Prompted by Doshi-
2017
VelezandKim[ ],recentattentionhasbeenfocusedonapproachesto
evaluating explanations, with some researchers arguing for the need to
2019
test explanations with users [Poursabzi-Sangdeh et al., ], and others
cautioning against doing so, concerned that cognitive biases could skew
2019
evaluations and mislead the XAI field [Herman, ]. We take stock of
347
these cognitive biases in Section . . .
Finally, the bias mitigation strategies mentioned in the corpus are pre-
sented in the pale orange box (bottom-left of Figure 3 . 3 ). The identified
biases leading to overtrust, distrust and misuse of explanations of AI
343
systems are summarized in Table . . .
3.4.2 Cognitive mechanisms explanations should adapt to
Explanatory heuristics
Inthissectionwesummarizethecognitive(andbiased)waysinwhich
people select causes, evaluate, and ultimately trust explanations. As the
term “bias” usually refers to errors in judgment and we do not consider
suchcognitivemechanismsaserrors,weusetheterm"explanatoryheuris-
tics". UnlikethecognitivebiasoftheothercategoriesinFigure 3 . 3 ,inthis
class, the explanatory heuristics are inherent to the explanation process
and help humans select some events as being relevant causes out of a
1988
potentially infinite causal chain of events [Hilton, ]. As presented in
23 2
Section . inChapter ,explanatoryheuristicsweremainlyexaminedby
2017
reviews such as [Miller et al., ], but also by primary studies focusing
on explainability desiderata such as simplicity and completeness.
Attentionalheuristics. Peoplepayattentiontosomecausesmorethan
2019 2006 2004
other to form explanations [Miller, , Lombrozo, , Malle, ].

trust overtrust distrust in explainable ai a cognitive approach 95
, , :
Specifically, people tend to focus on causes that are abnormal, inten-
tional, that point to the responsibility of individuals, that are necessary,
sufficientandrobust. Further,thestudiesinourcorpusshowthatpeople
select and assess causes according to confidence estimates [Bhatt et al.,
2021 2019 2019 2021
, Miller, , Wang et al., a], demographic features [Liu, ]
2018 2019
and inherent features [Bekele et al., , Miller, ].
2021
Bhatt et al. [ ] stress the importance of showing confidence esti-
matesofAIprediction. Theyarguethatpeopleneedtoassessuncertainty
to make decisions, relying on prospect theory [Kahneman and Tversky,
1979
]. In social interactions, we are used to estimating the confidence
level of a person’s assertion based on their tone and other social cues.
These cues are not applicable in human-AI interactions, hence the need
2015
to explicitly state AI’s confidence levels. However, Bussone et al. [ ]
nuanced that view by empirically demonstrating that "the amount of sys-
tem confidence had only a slight effect on trust and reliance".
2021
Liu et al. [ ] report on people’s tendency to focus on demographic
features such as race or age in feature-based explanations. We can hy-
pothesize that may be due to the discriminatory potential of these fea-
tures and may be linked to either the severity of the consequences of
2
weighting in these variables or to the availability bias . This is consis- 2Human tendency to
tent with earlier observations on trust in automation, that trust depends rely on information that
on the severity of the consequences of failure, cf. Section 3 . 2 . comes readily to mind
(such as information
Another interesting example of incorporating these attentional biases
seen recently in the
2018
into the design of XAI techniques is [Bekele et al., ], which used the
press) when evaluating
inherence bias—a human tendency to focus on inherent features instead a situation [Kahneman,
of extrinsic ones to explain a phenomenon—to select explanations for
2011].
person re-identification systems.
Preference for broad, simple, complete explanations. Additionally, ex-
isting work on explanation desiderata has evidenced that people look
23
for specific qualities in explanations (cf. Section . ). In our corpus, we
2019
also observe such preferences for "broad" [Miller, , Shimojo et al.,
2020 2021 2020 2019
, Woodcock et al., ], "simple" [Abdul et al., , Miller, ,
2020 2021
Shimojo et al., , Zytek et al., ] and "more complete" [Kulesza
2013
et al., ] explanations. However, the preference for simple and com-
plete explanations raises several ambiguities. While it is unchallenged
that simpler explanations are more comprehensible and readable [Ab-
2020 2020
dul et al., , Fürnkranz et al., ]—some researchers even show
thatinterpretabilityisinverselyrelatedtoexplanationlength[Fürnkranz
2020
etal., ]—theycanalsobereceivedwithskepticismbyusers[Bussone
2015 2020 2015
et al., , Fürnkranz et al., , Kulesza et al., ].Similarly, Kulesza
2013
et al. [ ] argue that more comprehensive explanations help to signif-
icantly improve participants’ mental models, but other work [Bussone
2015 2021
etal., ,Szymanskietal., ]foundcompleteexplanationscanlead
2021 2020
to overreliance [Woodcock et al., ]. Shimojo et al. [ ], Woodcock
2021
et al. [ ] contend that coherent and broad explanations are preferred,
with scope being even more important than simplicity, consistently with
Lombrozo’s point of view in cognitive science that broader and simpler
2007
explanations are better [Lombrozo, ]. Based on these findings, it can
be challenging to gauge the right level of complexity in explanations.

96 the explanation paradox and the human centric path
-
Some suggested general principles such as not providing explanations
2020
that are too complex to be readable [Fürnkranz et al., ] or adjusting
to the level of “completeness” to each user and context [Woodcock et al.,
2021
].
Social expectations. Furthermore, Weld and Bansal [ 2018 ] support
2019
Miller’s view [Miller, ] that explanation is a social process and state
that adopting more "social" explanations would be highly beneficial to
provide more relevant explanations. Through the process of dialogue,
socialexplanationscanbeusedtoidentifyeachuser’sspecificknowledge
gap that needs to be explained.
2021
Woodcock et al. [ ] highlight the impact of considering the ex-
plainee’spriorknowledgeandthefoilinherquestionthatneedstobead-
dressed. They show that explaining a disease to a user of an AI-powered
chatbot who possesses prior knowledge of that disease has little impact
on her trust. Then, tailoring explanations to addresses specific users’
questions has an important impact on trust. For that reason, some re-
searchers have argued for more interactive explanations. However, there
issomeconcerninthearticlesofourcorpusthatinteractiveexplanations
2021
may lead to overtrust or overreliance [Liu et al., ].
Moreover, people tend to attribute human traits to machines, and
therefore tend to expect that AI systems use the same communication
2019 2018
framework as humans [Miller, , Weld and Bansal, ]. This was
already highlighted in early research on trust in automation [Lee and
1992 2020 1992
Moray, , Glikson and Woolley, ]. In , Lee and Moray ex-
plainedthatpeopletendtoanthropomorphizemachinesandattachmore
importance to system characteristics than to system behaviour, as they
would do when calibrating human-to-human trust. This is also known
as the correspondence bias, whereby we tend to explain behaviour in
terms of motives, traits and intentions, and underestimate the influence
2004
of external factors [Gawronski, ].
User individual characteristics
Some studies showed that certain individual characteristics of users
2021
impact the way explanations are received. Broniatowski [ ] stressed
the importance of considering individual differences to design meaning-
ful explanations.
Skills and expertise. The author considers the effect of skills such
as numeracy— mathematical ability—, having a computer science back-
ground, or reading skills—which enable users to better "extract the gist
from narratives with poorly defined causal structures" [Broniatowski, 2021 ].
The studies in our corpus also identified major differences in the way
explanationsarereceiveddependingontraditionalclassificationsofuser
expertise. Experts have a greater ability to extract relevant information,
follow efficient and trained reasoning paths, and generally avoid over-
2021 2009
reliance and overtrust [Broniatowski, , Kahneman and Klein, ,
2021 2020
Szymanski et al., , Simkute et al., ]. Novices are more exposed
2020
to overreliance [Simkute et al., ].

trust overtrust distrust in explainable ai a cognitive approach 97
, , :
Personality traits. Browniatowski also reviews the effect of certain
personality traits on explanation reception. One aspect to consider is
the Need for Cognition (NFC), which refers to an individual’s desire for
mental effort and can be quantified using the NFC scale [Broniatowski,
2021 2021 2019
, Buçinca et al., ]. Additionally, Schaffer et al. [ ] discussed
3
how illusory superiority makes people less likely to seek advice and 3Refers to psychologi-
may be linked to higher susceptibility to cognitive overload. cal observations where
low-skilled people felt
People also differ in the way they make decisions. Some tend to rely
a sense of superior-
ontheirgutfeeling,whileothersprefertothinklongandhard. Thistrait
ity which made them
can be measured through the Cognitive Reflection Test (CRT) [Bronia-
less likely to rely on
2021 2019
towski, ]. This echoes Coba et al. [ ]’s results. Coba et al. used a advice [Schaffer et al.,
Choice-Based Methodology [Louviere et al., 2010 ] and eye-tracking mea- 2019]. Also known as
the Dunning-Kruger ef-
surements to reveal that people’s various decision making styles impact
fect.
how they perceive hotel ratings—shown as "collaborative explanations".
People of the "maximizer" type were more prone to insensitivity to sam-
ple variance and choice overload.
3.4.3 When explainable AI leads to overtrust
As studies in automation show, overtrust phenomenons such as au-
tomation bias and complacency may arise with automated and AI sys-
tems. ThesemechanismscanbeexacerbatedbyexplainableAI,asstudies
in our corpus show. The interested reader can refer to the lexicon in the
1
Table A. of the Appendix of this thesis for definitions of the cognitive
mechanisms and biases in bold in the text.
According to the mere exposure effect [Kliegr et al., 2021 ], the sheer
presence of an explanation increases confidence in the machine’s predic-
2021
tion. This effect was evidenced in [Eiband et al., , Fürnkranz et al.,
2020 2019
, Lai and Tan, ], with lay users, rule-based and local feature
importance explanations, by demonstrating that random or placebic ex-
planations increase trust.
Several papers examined user’s bias for completeness [Bussone et al.,
2015 2020 2013 2019
, Fürnkranz et al., , Kulesza et al., , Lai and Tan, , Szy-
2021 2020
manski et al., ]. For example, Fürnkranz et al. [ ] showed that
users found longer explanations more plausible than shorter ones. This
2015
isconsistentwith[Bussoneetal., ]whichshowedthatgivingafuller
explanation in the context of a medical diagnosis led to overreliance is-
2019
sues. Lai and Tan [ ] demonstrated that additional details including
irrelevant ones improved user’s trust in AI predictions. Szymanski et al.
2021
[ ] contended that the additional details contained in visual explana-
tionscomparedtotextualonescanincreaseusers’misattributedtrust. Fi-
2021
nally,Szymanskietal.[ ]showedthatlayusersweremoreexposedto
confirmationandcompletenessbiasthanmachinelearningexpertswhen
faced with visual explanations of a reading time prediction algorithm.

| 98 the | explanation | paradox |     | and | the | human | centric | path |     |     |
| ------ | ----------- | ------- | --- | --- | --- | ----- | ------- | ---- | --- | --- |
-
"Givingafullerexplanationofthefactsusedinmakingadiagnosishadapositiveeffectontrustbut
alsoledtooverrelianceissues,whereaslessdetailedexplanationsmadeparticipantsquestionthe
system’sreliabilityandledtoself-relianceproblems."
[Bussoneetal.,2015]
Thesearticlesprovideseveralavenuesforaddressingthebiasforcom-
pleteness problem, including by combining the use of textual and visual
explanations [Szymanski et al., 2021 ] or by providing arguments against
2015
| the machine’s | suggestion |     | [Bussone | et  | al., | ].  |     |     |     |     |
| ------------- | ---------- | --- | -------- | --- | ---- | --- | --- | --- | --- | --- |
Some mentioned the possibility that more complete explanations are
more likely to contain elements that the user recognizes, thus contribut-
4
ing to the persuasive effect through the recognition bias [Kliegr et al., 4Recognizing informa-
| 2021 |     |     |     |     |     |     |     |     | tion makes | the user |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- |
].
In a healthcare application, Wang et al. [ 2019 a] also reported that doc- more likely to trust
|     |     |     |     |     |     |     |     |     | the explanation | [Kliegr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------- |
torswhoconsideredtheAIpredictionbeforemakingtheirowndiagnosis etal.,2021].
| fell into | confirmation | bias | and | relied | on backward |     | reasoning. |     |     |     |
| --------- | ------------ | ---- | --- | ------ | ----------- | --- | ---------- | --- | --- | --- |
Anotherbiasstudiedinthecorpusisthephenomenoncalled"illusion
5
of explanatory depth" , coined by Koehler [ 1991 ] and evidenced in the 5People
|     |     |     |     |     |     |     |     |     | think | they have |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --------- |
2021
explainability literature by Chromik et al. [ ] using local feature im- a much deeper under-
|                               |     |     |     |     | 2017            |     |              |     | standing | of how com- |
| ----------------------------- | --- | --- | --- | --- | --------------- | --- | ------------ | --- | -------- | ----------- |
| portance(SHAP[LundbergandLee, |     |     |     |     | ])explanations. |     | Theyprompted |     |          |             |
plexconceptsworkthan
users to self-explain so that they would realize that they knew less about
theyactuallydo.
the concept being explained than they had originally imagined. We can
also perceive this effect in [Kaur et al., 2020 , Naiseh et al., 2021 b] which
| mentions | "superficial" | and | "rush | understanding". |     |     |     |     |     |     |
| -------- | ------------- | --- | ----- | --------------- | --- | --- | --- | --- | --- | --- |
Several articles in our corpus emphasized that experts were particu-
6
larly affected by narration or causal bias. , including researchers who 6Tendency
to interpret
2020
attribute causal meaning to saliency maps [Atrey et al., ], data scien- information as being
|     |     |     |     |     |     |     |     |     | part of | a larger story |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- |
tistswhomakefalsenarrativesabouthowSHAPandGAMexplanations
|     |     |     |     |     |     |     |     |     | and to | assume causal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------- |
work [Kaur et al., 2020 ] or domain experts in the domain of child wel-
relationsintheeventsof
2021
fare screening using counterfactuals [Zytek et al., ]. The authors that story [Betsch et al.,
mainly called for incorporating knowledge-based narratives in explana- 2015].
2020
tions. Atreyetal.[ ]encouragedresearcherstousedirectexperimen-
tal evidence to back up their claims. In our corpus of articles, narration
biaswaslinkedtooverrelianceonexplanations, followingthesamelogic
2019
as confirmation bias and backward reasoning [Wang et al., a]. Peo-
pleusednarrativestomakesenseofthepredictionsofAIsystems,which
reinforced their trust in them. In [Zytek et al., 2021 ], counterfactual ex-
planations lead users to mistake correlation for causation and develop
| flawed causal | narratives. |     |     |     |     |     |     |     |     |     |
| ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Other biases related to complacency. Several studies reported tendencies
from participants to over-rely on AI’s predictions [Bansal et al., 2021 ,
|         | 2015    |         |     | 2023 |        | 2021 |           | 2019 |     |     |
| ------- | ------- | ------- | --- | ---- | ------ | ---- | --------- | ---- | --- | --- |
| Bussone | et al., | , Danry | et  | al., | , Liu, |      | , Lai and | Tan, | ,   |     |
2021
| Naiseh et | al., | b]. |     |     |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Using an AI aid for chess, Bayer et al. [ 2021 ]demonstrated that chess
7
players displayed a default bias , that is, users tended to prefer the de- 7Tendency to accept a
fault option suggested by the AI. This behavior may overlap with the presenteddefaultoption
|     |     |     |     |     |     |     |     |     | (almost similar | to status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------- |
quobias).

trust overtrust distrust in explainable ai a cognitive approach 99
|     |     |     | ,   |     | ,   |     |     |     | :   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
conceptofautomationbiasdemonstratedinearlystudiesonautomation.
This suggests that offering AI predictions as a default option is probably
a flawed strategy if we want users to actively critique and challenge AI
decisions.
2019
|     | InataskcalledtheDiner’sDilemmagame,Schafferetal.[ |     |     |     |     |     |     |     | ]demon- |     |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |
strated automation bias towards AI recommendations. The authors did
| not | find | explanations |     | to be an | effective | remedy. |     |     |     |     |     |
| --- | ---- | ------------ | --- | -------- | --------- | ------- | --- | --- | --- | --- | --- |
2020
Additionally, Danry et al. [ ] discussed the "cognitive dissonance"
8
effect —as study participants called it—and ties it to cognitive overload 8Having
two opposing
in a fake news detection task. When given a suggestion by the AI, the and coexisting beliefs,
leadingtocognitivecon-
study participants were inclined to follow the AI’s suggestions, even
|     |     |     |     |     |     |     |     |     |     | flict and | psychological |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- |
though they knew they might have opposing personal beliefs. Explana-
stress.
tions reinforced that effect. In this study, AI suggestions were explained
through arguments of why a claim is supported or not by evidence, in
| plain | language |      | and spoken  | to  | participants |       | through     | an earpiece. |     |     |     |
| ----- | -------- | ---- | ----------- | --- | ------------ | ----- | ----------- | ------------ | --- | --- | --- |
|       | 3.4.4    | When | explainable |     | AI           | leads | to distrust |              |     |     |     |
Ourcorpusalsocontainsarticlesdiscussingunderrelianceissues,which
we refer to as "distrust". These were manifested through various aspects
of overconfidence in one’s abilities or choices, such as “the escalation of
9
commitment” evidenced with chess players receiving text-based expla- 9The
|     |     |     |     |      |     |     |     |     |     | tendency | to re- |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | -------- | ------ |
|     |     |     |     | 2021 |     |     |     | 10  |     |          |        |
nations [Bayer et al., ], the "illusion of validity" evidenced with main committed to
|     |     |     |     |     | 2020 |     |     |     |     | a choice | made, even |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | -------- | ---------- |
domain experts [Simkute et al., ] or "illusory superiority" [Schaffer
thoughoneunderstands
| et  | al., 2019 | ] for | lay users | with | low levels | of  | cognition. |     |     |            |             |
| --- | --------- | ----- | --------- | ---- | ---------- | --- | ---------- | --- | --- | ---------- | ----------- |
|     |           |       |           |      |            |     |            |     |     | with newer | informa-    |
|     |           |       |           |      |            |     |            |     |     | tion that  | it leads to |
Several works have highlighted the role of user expertise in distrust
undesirableresults.
problems. Domain experts have developed cognitive routes that enable 10Tendency
to over-
themtomakequickandaccuratedecisionsinenvironmentsthatare"reg- estimate one’s ability
|     |     |     |     |     |     |     |     | 2009 |     | to accurately | interpret |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------------- | --------- |
ular" enough to be predictable [Kahneman and Klein, ]. Their intu-
|     |     |     |     |     |     |     |     |     |     | and predict | results |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- |
ition is therefore more sophisticated than a lay user’s "System 1 " [Kah-
|     |     |      |     |     |      |     |     |      |     | when analysing | a data |
| --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | -------------- | ------ |
|     |     | 2011 |     |     | 2020 |     |     | 1988 |     |                |        |
neman, ]. Simkute et al. [ ] highlight Klein [ ]’s findings that [Kahneman,2011].
expertsmakedecisionsintuitively, withlittleuncertainty, andrarelycon-
sider more than one option. While useful heuristics, this reasoning also
1991
make experts more prone to belief perseverance [Koehler, ] or al-
11
gorithm aversion , especially when faced with contradictions from the 11"People
erroneously
2020
machine’s predictions [Simkute et al., ]. In addition, user studies avoid algorithms af-
|     |     |     |     |     |     |     |     |     |     | ter seeing | them err" |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- |
involving domain experts often focus on decision-making contexts that
[Dietvorstetal.,2015].
are high-stake, time-limited and stressful, as it is the case in the critical
industries such as healthcare. This may explain the reluctance of experts
2021
toengageinexplanations. Naisehetal.[ b]arguethatexpertsincrit-
ical domains are in a serious state of mind, where they tend to perceive
| additional |     | information |     | as "goal | impediment". |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
12
Negativity bias , was found to affect everyone including non-expert 12A
|     |     |     |     |     |     |     |     |     |     | tendency | to pay |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ |
users. Itcanleadtosignificanttrustlosswhenshowingtheweaknessesof more attention to nega-
|     |     |     |     |     |     |     |     | 2021 |     | tivefeatures. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ------------- | --- |
the system early through explanations [Nourani et al., , Kliegr et al.,
2021 ,Shimojoetal., 2020 ,Zyteketal., 2021 ]. Nouranietal.[ 2021 ]suggest
controllingwhattypesofpredictionsusersseewhenfirstinteractingwith
the system.

| 100 | the | explanation | paradox |     | and | the | human | centric path |     |     |
| --- | --- | ----------- | ------- | --- | --- | --- | ----- | ------------ | --- | --- |
-
|     | 3.4.5 | When | explainable | AI  | is  | misused |     |     |     |     |
| --- | ----- | ---- | ----------- | --- | --- | ------- | --- | --- | --- | --- |
ThissectionanalysesothercognitivepatternspresentinAI-baseddecision-
making. These patterns are not consistently correlated with overtrust or
distrust,butinsteaddisplayamisapplicationormisunderstandingofthe
| explanation. |     | This | leads to a | poor calibration |     | of  | trust. |     |     |     |
| ------------ | --- | ---- | ---------- | ---------------- | --- | --- | ------ | --- | --- | --- |
Related to the integration of probabilities. In their review of biases related
2021
torule-basedexplanations,Kliegretal.[ ]describedseveralcognitive
biasesrelatedtopeople’sdifficultytointegrateprobabilitiessuchasbase
|     |     | 13  |     |     | 14  |     |     | 2021 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
rate neglect or conjunction fallacy [Kliegr et al., ]. Fürnkranz 13"The tendency to un-
2020
et al. [ ] further evidenced that people (lay users in this case) tend to derweightevidencepro-
ignorethestatisticalsignificanceofastatement,aphenomenoncalledin- vided by base rates"
[Kliegretal.,2021].
2019
sensitivity to sample size. Miller [ ] stressed that probabilities don’t
|     |     |     |     |     |     |     |     |     | 14Estimating | the con- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- |
2021
mattertopeople—aclaimsomewhatdisputedby[Bhattetal., ]ifun- junction of two state-
certainty estimates are probabilities—and that explanations should focus
|     |        |                |     |     |     |     |     |     | ments to be         | more prob- |
| --- | ------ | -------------- | --- | --- | --- | --- | --- | --- | ------------------- | ---------- |
| on  | causal | relationships. |     |     |     |     |     |     | ablethanoneofthetwo |            |
statements.
15
Related to memory. Wang et al. [ 2019 a] discussed representativeness 15The similarity of
and availability bias in the context of medical diagnosis, and proposed objects or events makes
showing prior probability and prototypes of outcomes to mitigate these. people disregard the
|     |     |     |     |     |     |     |     |     | probability | of an out- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- |
|     |     |     |     |     |     |     |     |     | come        | [Kahneman, |
Misunderstanding language elements. Biases leading to misusing the ex-
2011].
planations can also be due to misunderstanding some elements of the
2021
| language[Kliegretal., |     |     |     | ]thatiscommonlyusedinexplanationssuch |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | --- |
2020
as the logical operator "AND" in rules [Fürnkranz et al., ], Boolean
logic in counterfactuals [Zytek et al., 2021 ], or confidence scores when it
2021
| is  | ambiguous | what | they refer | to [Bhatt | et  | al., | ].  |     |     |     |
| --- | --------- | ---- | ---------- | --------- | --- | ---- | --- | --- | --- | --- |
Relatedtopositionandcontext. Nouranietal.[ 2021 ]discusstheprimacy
16
effect . They suggest controlling the type of predictions users observe 16Atendencytoforman
2021
when first interacting with the system [Nourani et al., , Kliegr et al., opinion based solely on
| 2021 | ].  |     |     |     |     |     |     |     | the first piece | of infor- |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------- |
mationreceived.
2020
Additionally, Branley-Bell et al. [ ] explore user biases towards ex-
plainableAIsysteminahealthcareapplication. Theresearchfindingsin-
dicated that users exhibited greater trust in the system’s accuracy when
a malignant diagnosis was provided and explained, as opposed to when
a benign diagnosis was given. Unlike the negative bias we examined in
|     |     | 3 4 4 |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Section . . , this occurrence of negative bias leads to poor trust cali-
bration rather than distrust. Here, trust is based on an irrelevant factor.
Similarly, Mohseni et al. [ 2021 a] observed that "users pay less attention to
false positive explanation errors and in turn, are more critical for false nega-
tive explanation errors". This may be related to people’s tendency to see
false positives as less harmful than false negatives, and therefore relates
to people’s attention to the severity of the consequences of failure when
| calibrating |       | trust | in automation | [Culley | and      | Madhavan, |       | 2013 ]. |     |     |
| ----------- | ----- | ----- | ------------- | ------- | -------- | --------- | ----- | ------- | --- | --- |
|             | 3.4.6 | When  | explainable   | AI      | corrects |           | false | beliefs |     |     |
Other explainability researchers have examined the extent to which
explainable AI can successfully mitigate the cognitive biases that arise in

trust overtrust distrust in explainable ai a cognitive approach 101
, , :
decision-making with AI systems. As Liao et al. [ 2020 ] indicate, "users
also consider explanations of the AI’s decision as potential mitigation of their
own decision biases". The literature on explainability frequently discusses
broadnotionsoftransparencyasapotentialtooltomitigateaversionbias,
2021
see [Park et al., ] for example. However, we exclusively consider
research that focuses on explainable AI and substantiates claims about
explanation’s ability to mitigate bias.
2019
[Wangetal., a]observedthatexplainabilityusersinhealthcarefell
into confirmation bias, whereby they would pay more attention to infor-
mationconfirminganexistinghypothesis,insteadoflookingforevidence
of alternative possibilities. To mitigate this effect, they implemented an
explainable AI system in which input attributions (feature-based expla-
nations) are showed before the class attribution (AI’s hypothesis). Fur-
2020 2019
thermore, as [Bhatt et al., ], [Wang et al., a] argue for showing
AI’s certainty estimates to mitigate overtrust effects.
2019
Springer and Whittaker [ ] evidenced how users had positive ex-
pectations of the transparent system before using it. To be able to refer
to it later, we call this phenomenon "pre-use algorithmic optimism".
Springer and Whittaker conclude that showing explanations progres-
sively, in this case local feature importance, was important to prevent
users from overestimating the capabilities of the system. They suggest
presenting explanations gradually or only when requested, to prevent
users from losing trust when their expectations about the system are
contradicted.
2020
Danryetal.[ ]designedanexplainableAIprototypethatwassuc-
cessfully able to correct people’s tendency to believe persuasive claims
thatarenotsupportedbyevidence. Foreachclaimonasociallydivisive
topic such as immigration or poverty, an explainable AI device classified
the claim as supported by evidence or not and provided an explanation
of that evidence, e.g. "a majority of Americans support a ban on flag-burning
because a poll conducted by CNN in June 2006 found that 56% of Americans
supportedaflagdesecrationamendment.". Peoplewerebetterabletodistrust
unsupportedclaimsandtrustsupportedclaims,althoughthissometimes
caused cognitive dissonance problems. Additionally, people trusted less
evidence supported by anecdotal and expert evidence instead of study
evidence.
2021
Further, Zytek et al. [ ] demonstrated through a user study the
usefulness of their "Case-Specific Details" interface for domain experts to
screen child welfare cases. The interface displays the local contribution
of the factors pre-selected by users, which proved useful in correcting
experts’ lack of trust in the model, and highlighting differences between
human and AI logic.
Topreventusersfromrelyingonhowsimilarthecurrentsituationwas
2019
to a previously seen case (representativeness bias), Wang et al. [ a]
also suggest to show prototypes of other cases, either sorted per a metric
ofsimilarity,oraccompaniedwithadissimilaritymetric. However,Zytek
2021
et al. [ ] evidenced that case-based explanations of examples similar
to the current situation enhance people’s tendency to make decisions
based on similarity.

102 the explanation paradox and the human centric path
-
Other studies suggested mitigation strategies to overcome systematic
errorswithexplainableAIsystems,withouttestingthemexperimentally.
2019 2019
Forexample,[Wangetal., a,LaiandTan, ,SpringerandWhit-
2019 2020
taker, ,Buçincaetal., ]suggesttodelayshowingtheAI’spredic-
tion and/or explanations to enable users to form their own hypotheses.
2021 2020 2020
[Naiseh et al., b, Buçinca et al., , Simkute et al., ] propose to
usecognitiveforcingfunctionsandfrictiontofavorusers’activecognitive
2020 2019
engagement. [Simkute et al., , Wang et al., a] argue for enabling
2021 2015
exploration of raw data, and [Naiseh et al., b, Bussone et al., ,
2021
Kliegr et al., ] propose to educate users and clearly explain how to
2021 2015
use explanations. Lastly, [Bansal et al., , Bussone et al., , Wang
2019
et al., a] recommend to give arguments for non-predicted outcomes
to favor the consideration of alternative possibilities than the one sug-
gested by the AI.
3.4.7 When explanations are misevaluated
Users’ stated preferences are not indicative of performance. Buçinca
2021
et al. [ ] warned against using proxy tasks to evaluate explanations
through user studies, i.e., tasks that consist in subjectively rating the ex-
planations. They noted that people’s subjective preferences for expla-
nations were not indicative of the performance they would exhibit in
making decisions with these explanations. Instead, researchers should
use real tasks. This observation was also evidenced in our corpus with
local feature importance, rule-based, example-based, and counterfactual
2021 2021 2021
explanations [Buçinca et al., , Liu, , Szymanski et al., ].
More attention to false negatives than false positives. Focusing on
2021
saliency maps for image recognition, Mohseni et al. [ a] showed that
people pay less attention to explanations of false positives than explana-
tions of false negatives. They also showed that people rate differently
techniques that differ only in appearance. To address these biases, they
designed a human attention baseline to evaluate saliency explanations
without having to resort to user studies.
2020
Furthermore, Sokol and Flach [ ] called for caution about the phe-
nomenon of change blindness in user studies, namely the “inability to
notice all of the changes in a presented medium", especially in an im-
age. To address it, any change should be highlighted or made salient.
Researchers should also be wary of selection bias when selecting partic-
ipants for user studies through Amazon Mechanical Turk, usually more
2019
computerliteratethanthe‘normal’population[BarbosaandChen, ].
To circumvent the problems associated with user studies, Mohseni
2021
et al. [ a] presented a promising evaluation methodology. Leverag-
ing human annotators, they developed human attention masks which
can be used to evaluate model saliency explanations for image and text
domains.

trust overtrust distrust in explainable ai a cognitive approach 103
, , :
Year Title Authors Venue
tsurtrevo
ot
dael…
tsurtsid
ot
dael…
desusim
era
…
noitaulave
noitanalpxe
sesaib
gnitcerroc
tiart
evitingoc
rehtO
EXPLANATIONS… THE PAPER INFORMS ON…
2020 COGAM: MeaAsubrdinugl eatn adl. ModeratCinHg ICognitive Load in Macxhine Learning Model Explanations x
2022 Visual AnalyticAsn fdorri eHnukmo aent -aCl.enteIrEeEdE M CaGchAine Learning x
2019 Exploratory noAt terexpy laent aatl.ory: CounItCeLrfRac tual analysis of saliexncy maps for dxeep reinforcement learning
2021 Does the WhoBlea nEsxacle eetd a ilt.s Parts?C THhIe Effect of AI Explanaxtions on Complementary Team Performance
2021 The role of domBaayine re extp aelr.tise in truJsotin. go fa Dnedc fiosliloonw Sinygs teexmplsaixnable AxI decision support systems
2018 Implementing Bae Rkoebleu sett Eaxl.planatoIrEyE BEia Cs VinP aR WPerson Re-identification Network x
2021 Uncertainty asB ah aFtot remt aolf. TransparAeInEcSy: Measuring, Communicating, and Using Uncertaixnty x
2020 User trust andB urnadnelerys-taBnedll inegt aol.f exHpClaCinIable ai: Exploring algorithm visualisxations and user biasesx
2021 Psychological BFroounniadtaotwiosnksi of ExpNlaIiSnTa bRileityp oarntd Interpretability in Artificial Intelligence x
2020 Proxy Tasks aBndu çSinucbaje ectt ivael. MeasIuUrIes Can Be Misleading in Evaluating Explainabxle AI Systems
2021 To Trust or to TBhuiçnikn:c Ca oegt naitl.ive ForAcCinMg FHuCncI Jtioon.s Can Reduxce Overreliance on AI in AI-Assisted Decision-Making
2015 The Role of ExBpulasnsoantioen est oanl. Trust2 a0n1d5 IREeEliEa nICceH Iin Clinical Dxecisionx Support Systems
2021 I Think I Get YCouhrr oPmoiikn te, tA aI!l .The IlluIUsIion of Explanatory Deptxh in Explainable AI
2019 Decision makiCngo bsatr aette agli.es difer inIU thIe presence of collaborative explanatioxns: Two conjoint studxies
2020 Wearable ReaDsoanneryr: eTto awl.ards EnhAaCnMce Ad hHsuman Rationalityx Through A Wearable Devicex With An Explainable AI Assistant
2019 The Impact of EPiblaacnedb eict Ealx.planatioCnHs Ion Trust in Intelligent Sxystems
2020 On cognitive pFreüfrenrkernacnez se at nadl. the ApClaMus Mibialitcyh oinf eru Llea-nbgausaegde mBodels x x
2020 Interpreting IntKearpurre etat bailli.ty: UndersCtaHnIding Data Scientists’ Uxse of Interpretability Tools for Machine Learning
2020 The Effect of MKiems saangde S Foranmging anCdH TI iming on the Acceptance of Artificiaxl Intelligence’s Sxuggestion
2021 A review of poKsslieibgler eetf faelc.ts of cogAnrittiifvicei abl iaInsteeslli goenn icneterpretaxtion of xrule-basxed machine learning models
2013 Too much, tooK luitlteles,z oar jeuts at lr.ight? WIEaEyEs VeLxp/HlaCnaCtions impacxt end usxers' mental models x
2019 On human preLdaici taionnds T wainth explanFaAticocnTs and predictions of xmachine learning models: A case study on deception detection
2021 UnderstandingL ituh ee tE affl.ect of Out-oAf-CDMis tHribCuIt iJoon. Examples axnd Interactive Explanations on Humanx-AI Decision Making
2019 Explanation inM airltleifircial intelligenceJ: oIn. soigf hAtIs from the social sciences x
2021 Quantitative EMvaoluhasteionni eotf aMl.achinIeU LIearning Explanations: A Human-Grouxnded Bxenchmark
2021 Explainable ReNcaoismemh eent daal.tions anCdo Cmapliubtrearted Trust: Two Systemaxtic Usexr Errors
2021 Nudging throuNgha isFerihc teiotn a: l.An ApprBoEaSchC for Calibrating Trustx in Explainable AI
2021 Anchoring BiaNs oAuffreacntis e Mt ael.ntal MoIUdeIl Formation and User Reliance in Expxlainable AI Systems
2019 I can do betteSr tchhaanf fyeor uert AaIl:. ExpeIrUtisIe and explanations
2020 How Does ExSplhainmaotojor ye Vt airtl.ue DetFerromnitnieer sP irno bPasbyiclithyo Elosgtiymation?—Empirical Discussion on Effecxt of Instruction
2020 Experts in the SSihmakduotwe eotf aAl.lgorithmACicM S yDsItSems: Exploring Inxtelligibility in a Decision-Making Context
2020 Explainability FSaockt oSl haenedt sF:l aAc FhramFeAwcocrTk for Systematic Assessment of Explainablxe Approaches
2019 Progressive disScplorinsugreer eamndp iWrichaitlltya IkmUeIortivated approaches to designing effective transparenxcy
2021 Visual, TextuaSl ozry mHyabnrsidk:i Teht ea l.EffeIcUtI of User Expertise on Dxifferent Explanations
2019 Designing TheWorayn-Dg reivte anl .User-CeCntHricI Explainable AI x x x
2019 The ChallengeW oef ldC raanftdin Bga InntseallligibCleo mInt.e AlliCgeMnce x
2021 The impact of Wexopoladcnoactiokn est oanl. layJpoe.r soofn M treudsitc ianl aInrtteifircnieatl iRnetBesl.ligence-driven symptom checker apxps: Experimental study
2021 Sibyl: UnderstaZnytdeinkg e at nadl. AddressIiEnEg Eth TeV UCsGability Challenges of Mxachine xLearning In High-Stakes Decision Making
Figure 3.4: The 38 pa-
pers in the corpus and
a rough indication of
whether the paper re-
ports on over- or dis-
trust effects of expla-
nations, on the mis-
use of explanations, or
on other explanation-
relatedphenomena.

| 104 the | explanation | paradox | and | the human |     | centric | path |     |     |     |
| ------- | ----------- | ------- | --- | --------- | --- | ------- | ---- | --- | --- | --- |
-
Cognitivebiases Ex. ofevidencingstrategies Ex. ofmitigatingstrategies
Leadingtoovertrust
Mereexposureeffect, Com- Study the correlation between explana- Give arguments for non-predicted outcomes
|     |     |     |     |     |     |     |     | 2015, |     | 2019a, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------ |
pleteness bias, recognition tion length and perceived plausibility [Bussone et al., Wang et al.,
bias, Confirmation bias, Il- [Fürnkranz et al., 2020], Ask participants Weld and Bansal, 2018], Delay showing the
lusionofexplanatorydepth to rate their own understanding before AI’spredictionand/orexplanations[Buçinca
and after self-explaining AI predictions et al., 2021, Lai and Tan, 2019, Springer and
|     |     |          |     | 2021], |       |         | Whittaker,2019,Wangetal.,2019a],Usecog- |     |     |     |
| --- | --- | -------- | --- | ------ | ----- | ------- | --------------------------------------- | --- | --- | --- |
|     |     | [Chromik | and | Butz,  | Study | the ef- |                                         |     |     |     |
fect of placebo or random explanations nitive forcing functions and friction [Buçinca
[Eibandetal.,2021] etal.,2021,Naisehetal.,2021a,Simkuteetal.,
|     |     |     |     |     |     |     | 2020], Include | uncertainty     | estimates  | [Bhatt  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --------------- | ---------- | ------- |
|     |     |     |     |     |     |     | et al., 2020,  | Bussone et al., | 2015, Wang | et al., |
2019a]
Related to causality: Askparticipantstodescribeexplanations, Incorporate human expertise into explana-
tions[Andrienkoetal.,2022]
| Narrative        | bias, Over- | analyze               | free text | answers | and | verbaliza- |     |     |     |     |
| ---------------- | ----------- | --------------------- | --------- | ------- | --- | ---------- | --- | --- | --- | --- |
| generalization,  | Causation   | tions[Kauretal.,2020] |           |         |     |            |     |     |     |     |
| vs. correlation, | attention   | to                    |           |         |     |            |     |     |     |     |
demographicfeatures
Relatedtocomplacencyandin- Observe user’s degree of agreement with Do not use too many explainability types
formation overload: Default the AI with vs. without explanations [Zytek et al., 2021], Use user-centric ap-
bias, Cognitive Dissonance, [Danry et al., 2020], Measure the user’s proaches[Naisehetal.,2021b]
| Choiceoverload |     | cognitive | load             | using | the NASA | Task    |     |     |     |     |
| -------------- | --- | --------- | ---------------- | ----- | -------- | ------- | --- | --- | --- | --- |
|                |     | Load      | Index (NASA-TLX) |       | [Kaur    | et al., |     |     |     |     |
2020,SpringerandWhittaker,2019],
Eye-
trackingmeasurements[Cobaetal.,2019]
Leadingtodistrust
Escalation of commitment, Observe the relation between subjec- Enable to actively explore the data [Simkute
|     |     |     |     |     |     |     | 2020, |     | 2019a], |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------- | --- |
Illusion of validity, Nega- tive confidence, subjective comprehen- et al., Wang et al., Use gami-
tivity bias, Familiarity bias, sion, and positive and negative AI out- fication and personalization [Simkute et al.,
Perceivedgoalimpediment, comes [Nourani et al., 2021], Ask partic- 2020], Keep track of what has already been
Redundancy aversion, ipantstothinkaloudwhiletheymakede- explained [Miller, 2019, Naiseh et al., 2021a],
Weakevidenceeffect cisions[Wangetal.,2019a] Control the predictions users observe in the
trainingphase[Nouranietal.,2021]
Leadingtomisusingtheexplanation
Related to the integration of Measure the correlation between the Reminderofprobabilitytheory,Usefrequen-
probabilities:
Averagingbias, user’s confidence and supporting evi- cies instead of percentages, Show support as
dence[Cobaetal.,2019,Fürnkranzetal., anabsolutenumber[Kliegretal.,2021]
| Base-rate | neglect, Conjunc- |     |     |     |     |     |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2020]
| tion fallacy, | Disjunction | fal- |     |     |     |     |     |     |     |     |
| ------------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
lacy,Insensitivitytosample
size,Unitbias
Related to memory: Rep- Analyze reasoning process through free Show prior probabilities of outcome and ex-
resentativeness, Availability text questions and think-aloud protocols amples of decision outcome [Wang et al.,
|     |     | [Wangetal.,2019a,Zyteketal.,2021] |     |     |     |     | 2019a] |     |     |     |
| --- | --- | --------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- |
bias
Related to misunderstanding Clarify the meaning of language ele- Clearly communicate what the presented in-
oflanguage: Misunderstand- ments to only one group of participants formation means [Bussone et al., 2015], State
[Fürnkranzetal.,2020]
ing of the inverse, of ’and’, only true statements for the presentation of
Boolean logic, confidence Booleanelements,includingbynegatingfalse
ones[Zyteketal.,2021]
| scores | Analyze free text | re- |     |     |     |     |     |     |     |     |
| ------ | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sponses[Zyteketal.,2021]
Relatedtotimingandcontext:
Measure the perceived reasonableness Describetheuncertaintyofbothpositiveand
negativeoutcomes[Bhattetal.,2021],Control
| Framing | bias, Primacy | ef- of explanations |     | and the | performance |     | of  |     |     |     |
| ------- | ------------- | ------------------- | --- | ------- | ----------- | --- | --- | --- | --- | --- |
fect,Anchoringbias usersatataskunderdifferentexplanation the kind of predictions users observe in the
|     |     | framing | conditions | [Kim | and Song, | 2020, | trainingphase[Nouranietal.,2021] |     |     |     |
| --- | --- | ------- | ---------- | ---- | --------- | ----- | -------------------------------- | --- | --- | --- |
Nouranietal.,2021]
Table3.2:
CognitivebiasesexacerbatedbyexplainableAIandexamplesofevidencingandmitigatingstrategies.

trust overtrust distrust in explainable ai a cognitive approach 105
, , :
3.4.8 Explanations tend to increase unwarranted trust
Overall, the studies in our corpus show a general tendency for expla-
nations to increase trust, even when it is unwarranted, i.e. the AI is not
trustworthy. For example, Bansal et al. [ 2021 ] note that "explanations are
interpreted as a general sign of competence" and that "explanations increased
the chance that humans will accept the AI’s recommendation, regardless of its
correctness." Nourani et al. [ 2021 ] also find that "In all conditions, explana-
tions increased confidence in the user’s estimations".
34
As illustrated in Figure . , our corpus analysis revealed that explana-
18 6
tions resulted in overtrust in studies, while studies reported distrust
12
effects of explanations. Additionally, studies identified cognitive bi-
ases that led to miscalibrated trust (it is not clear in which direction,
overtrust or distrust). Although a broad range of cognitive biases have
been discussed in the literature on explainability, it is possible that these
biasesmayoverlapandsharecommonunderlyingtrustmechanisms. For
example, anchoring bias and confirmation bias may be two sides of the
samecoinwhencalibratingtrustinexplainableAIpredictions. Centralto
the cognitive issue is the timing of when the explanation is presented to
the user: whether it is before or after the user has formed her own opin-
ion. Similarly, earlier investigations into trust in automation first distin-
guished between automation bias and complacency, eventually finding
that these two phenomena largely overlap.
3.4.9 Important factors for appropriate trust: a Bayesian ap-
proach
Central to calibrating trust in explainable AI systems is how people
reconcile AI predictions and their explanations with their prior knowl-
2023 2020
edge [Chen et al., , Shimojo et al., ]. This "belief reconciliation"
process is related to the process of evaluating explanations according
2019
to coherence, or generality as described in [Miller, ]. The problem
has also been framed in a more rational way in terms of probabilities as
2020 2020
detailed in [Shimojo et al., ]. Shimojo et al. [ ] argue that "the
[explainability] problem is one of updating posterior probability". Ac-
17
cording to the authors, the Bayesian approach can be described as "the 17Bayes’ rule [Phillips
update of the probability that a cause induced an event after taking into
andEdwards,1966]:
considerationnewinformationoftheevent."Inotherwords,theexplain-
P(E|C)
ability problem in Bayesian terms consists in assessing the probability of P(C|E)=P(C)
P(E)
an explanation to be true knowing an AI prediction (P(C|E), the "pos-
terior"), using the probability of the AI prediction to be true (P(E), the
"marginalization"), the probability of the cause presented in the explana-
tion to be true (P(C), the "prior") and the probability of the AI prediction
to be true given that the explanation is true (P(E|C), the "likelihood").
However, the authors also note that in practice, humans tend to disre-
gardBayes’ruleandestimate"subjectiveposteriorprobability"according
1979
to cognitive biases [Kahneman and Tversky, ].
The studies in our corpus reveal what appear to be recurrent and sig-

106 the explanation paradox and the human centric path
-
nificant trust factors involved in belief reconciliation, which ultimately
lead to trust calibration. Furthermore, individuals’ ability to reconcile
prior knowledge and critically examine the coherence of explanations
appear to be limited by three aspects: individuals’ prior knowledge, the
"probability" that a cause presented in an explanation is the cause of the
AI prediction, and human and individual cognitive and attentional ca-
pacities. We examine the important trust factors in our corpus in terms
of these three aspects of the belief reconciliation problem.
Prior knowledge. Several studies in our corpus highlighted the impor-
tance of user expertise, task expertise and task familiarity on the way
2021
people calibrate trust in explainable AI systems [Bayer et al., , Bus-
2015 2021 2021
sone et al., , Zytek et al., ]. For example, Bayer et al. [ ]
note that "experts use explanations to resolve their disagreements. In contrast,
noviceslackexpertise,whichmakesthemreliantontheopinionsofthirdparties,
and rather than question these opinions, they tend to use them to learn (Gre-
gor and Benbasat, 1999)." Following the Bayesian approach, this expertise
would enable users to assess the prior probability that a cause presented
in an explanation is true (P(C)), or that an AI prediction is true (P(E)).
For example, Bhatt et al. [ 2020 ] highlight the importance of showing es-
timations of the AI’s confidence.
Explanation likelihood. Similarly, the quality and persuasiveness of the
explanations providing information to update beliefs plays an important
role for people to infer the posterior probability that a given explanation
C is the cause of an AI prediction. Specifically, the papers we reviewed
shedlightontheimportanceofexplanationcompleteness[Kuleszaetal.,
2013 6
]. Out of studies in our corpus that reported distrust effect, all
were related to either user expertise (experts trusted less AI systems) or
explanation’s lack of completeness (incomplete explanations decreased
trust in AI systems).
Cognitive and attention capacity. In addition, certain trust factors are
linked to cognitive overload and limitations of human attention, i.e. the
2019
"capacity" and "attentional" problems described by Zerilli et al. [ ].
These factors include the timing and framing of explanations, users’
motivation and individual characteristics such as need for cognition
2021 2021
[Buçinca et al., , Broniatowski, ] of decision-making preferences
2019
underchoiceoverload[Cobaetal., ]. AspresentedbyKimandSong
2020 2021
[ ] and Nourani et al. [ ], timing and framing of explanation have
an important part to play in human’s ability to revise prior knowledge.
These conditions seem to be decisive in activating confirmation or a nar-
2019 2021 2020
rative bias [Wang et al., a, Bansal et al., , Kim and Song, ].
Bansal et al. [ 2021 ] argue that "by presenting an answer and accompanying
justification upfront, and perhaps overlaid right onto the instance, our design
makes it almost impossible for the human to reason independently, ignoring the
AI’s opinion while considering the task."
All these factors at play in the belief reconciliation problem may be
2019
related. For example, Schaffer et al. [ ] argued that lower cognitive
ability as demonstrated by "illusory superiority" could be predicted by
higher reported task familiarity.

trust overtrust distrust in explainable ai a cognitive approach 107
, , :
Althoughourgoalhereistoidentifyhigh-leveltrustfactorsinexplain-
able AI, we acknowledge that these may depend on specific AI applica-
tions and tasks. Liu [ 2021 ] note: "Our work suggests that tasks may play an
important role, and it can be challenging to understand the generalisability of
results across tasks." In addition, it was not always clear in the studies we
reviewed what is the effect of explanations and what is the effect of AI
predictionsinusers’trustcalibration. Forexample,theillusorysuperior-
ity bias leads to a general aversion to advice, and it is not clear whether
explanationsincreasethisbiascomparedtoAIpredictionalone[Schaffer
2019
et al., ].
3.5 Discussion
Wepresentbelowadiscussionofresearchdirectionswebelieveshould
be pursued in future work to address cognitive biases in XAI.
3.5.1 Take into account cognitive mechanisms and biases in
the design of explainable AI
Oneofouraimsinthisworkistohighlighttheimportanceofconsider-
2004
ing human cognitive architecture in XAI design [Cummings, ]. This
iscommonpracticeintheHCIfield, butitmaynothavefullypermeated
a historically technical explainability field.
2021
This may be a complex endeavour, however. Bayer et al. [ ] high-
light the complexity of designing AI systems that takes into account op-
posing cognitive biases. On the one hand, they showed that users fell
into a default bias when AI suggestions were presented at the same time
as users were making decisions. On the other hand, participants fell
into escalation of commitment when the AI suggestion came after they
2021
had made their choice. Kliegr et al. [ ] also mentioned the possibil-
ity that different cognitive biases could have opposing effects, such as
information bias (leading to overreliance) and ambiguity aversion (lead-
ing to under reliance), thus emphasizing the need to consider biases in
theircontextandtoputtheminrelationtotheuser’sknowledge. Wealso
2021
foundcontradictoryresultsbetweenZyteketal.[ ],whichfoundthat
example-based explanations for child welfare screening led to represen-
2019
tativeness bias and Wang et al. [ a], which presented prototypes of
decision outcomes as a mitigation for the same bias. In addition, Lai and
Tan [ 2019 ] warned about the "backfire effect" according to which "correc-
tionsofmisperceptionsmayenhancepeople’sfalsebeliefs" [Nyhan and Reifler,
2010
].
Lastly, there has been a surge of interest in interactive explanations
recently, responding to the call to design explanations that fit the social
2018
process of explanation [Weld and Bansal, ]. However, concerns were
2021
expressedin[Liuetal., ]asinteractiveexplanationswerefoundtore-
inforce user’s over reliance on AI suggestions. A possibility is that inter-
2021
active explanations were more complex to interpret in Liu et al. [ ]’s
study, leading to information overload.

108 the explanation paradox and the human centric path
-
Overall, more work is needed on the effects of interactive explana-
tions, of bias mitigation measures and on identifying opposing biases
and backfire phenomena.
3.5.2 Clarify the normal vs. problematic biases with empiri-
cal and normative work
Whichcognitivebiasesneedtobemitigated? Inthisreview,weidenti-
fied some cognitive biases as being neutral heuristics, i.e. "normal" ones,
inherent to the process of explanations. Instead of mitigating those bi-
ases, some argue that they should be taken into account in the design
2019 2018
of explanations [Miller, , Weld and Bansal, ], for example by
providing explanations as social processes or by adopting contrastive ex-
planations. However, there is a blurred line between biases XAI needs to
adapt to and those that need to be mitigated. It goes back to the impor-
tant question posed by Weld and Bansal: "Should an explanation system
exploit human limitations or seek to protect us from them?". Lakkaraju and
2020
Bastani [ ] argue that by exploiting certain human cognitive biases,
such as preferences for relevant or familiar features, trust could be ma-
2019
nipulated. Conversely,Miller[ ]explainsthatAIexplanationsshould
be contrastive, simple and when applicable delivered in the form of a di-
alogue, i.e. interactive. Clarifying which biases are normal and which
are undesirable appears to be important for moving the XAI field for-
ward. To that end, more empirical work on the benefits and drawbacks
of incorporating cognitive constraints into explanation is needed.
Further, not only do we need more empirical research into user bi-
ases in explainable AI, but we also need more theoretical and normative
worktodistinguishgenuinelybiasedcognitiveprocessesfromthosethat
are normal. Such a distinction seems difficult to make without norma-
tive evaluations referring to the correctness of decisions and the inherent
quality of the decision process for the users, including his or her level of
participation. In fact, recent work has advocated for "functional" mod-
els of cognition, which differ from the "deficit" model of cognition such
2011
as the dual system theory [Kahneman, ]. These more contemporary
models highlight that cognitive biases exist for good reasons, and often
produce "good" rather than "bad" decisions, and study how heuristics
help to make people better decision makers. Much of this research ques-
tions the conventional wisdom that intuition/heuristic thinking ("system
1 2
thinking") is "quick and dirty" while reasoning ("system thinking")
2023
is slow and good. For example, Gigerenzer [ ]’s work shows that
intuition is quick and error-prone, while reasoning is slow and just as
error-prone. Normative work to help researchers and XAI designers de-
cide whether, how and in which priority different biases need to be ad-
dressed should also keep in mind these more contemporary models of
cognition.

trust overtrust distrust in explainable ai a cognitive approach 109
|     |       | ,                                                |     | ,   |     |     |     | :   |     |
| --- | ----- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
|     | 3.5.3 | Detailtaxonomiesofusergroupswithcognitivefactors |     |     |     |     |     |     |     |
Recent efforts to tailor explanations to the task at hand, the user’s
|     |     |     |     | 2019 |     |     |     | 2021 |     |
| --- | --- | --- | --- | ---- | --- | --- | --- | ---- | --- |
goals, knowledge [Coba et al., , Szymanski et al., , Woodcock
et al., 2021 ] and specific needs [Simkute et al., 2020 , Wang et al., 2019 a],
in order to meet the user’s understanding, would be improved by taking
into account the individual personality traits and specific skills we have
mentioned in Section 342 . . . Future work could consider how the current
high-level groups of explainability users (currently categorized per AI
expertise or role in AI system) could be detailed with this cognitive in-
|     |     |     |     | 2021 |     | 2021 |     |     | 2018 |
| --- | --- | --- | --- | ---- | --- | ---- | --- | --- | ---- |
formation, [Mohseni et al., b, Suresh et al., , Tomsett et al., ]
highlighting cognitive biases each user group may be prone to. Bronia-
towski [ 2021 ] also suggested that the explainability field should strive to
identify the individual factors that influence explainability in each user
community.
|     | 3.5.4 | Improve | our | perception | of  | users’ | reactions | to XAI |     |
| --- | ----- | ------- | --- | ---------- | --- | ------ | --------- | ------ | --- |
Several authors have advocated that we need a better perception of
social and emotional behavior of users to be able to correct errors in
2020
| theirreasoningandtheirmentalmodelsofthesystem[Akataetal., |     |     |     |     |     |     |     |     | ,   |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Chromik et al., 2021 , Woodcock et al., 2021 ]. As a first step towards this,
343
we highlighted some methods to evidence biases in Table . . . Notably,
whatseemstobeagoodpracticeforcontrollingforthemereexposureef-
fectisusingplacebicexplanationsorrandomlygeneratedexplanationsas
|     |     |     | 2021 |     |     | 2021 |     |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- |
a baseline [Eiband et al., , Nourani et al., ]. Then, cognitive load
can be measured through the means of the TLX workload assessment
|     |     |     | 2020 |     |     |     | 2019 |     |     |
| --- | --- | --- | ---- | --- | --- | --- | ---- | --- | --- |
method [Kaur et al., , Springer and Whittaker, ], eye-tracking
2019
measurements [Coba et al., ] or through the number of cognitive
chunksandasubjectivemeasureencompassingthereadingtime,theself-
reported load and memory performance (how well the user remembers
the explanation) [Abdul et al., 2020 ]. In addition, we frequently encoun-
tered the use of qualitative analyses in our review, such as think-aloud
|     |     |     | 2021 |     |     |     |     | 2019 |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | ---- | --- |
protocols [Naiseh et al., b, Springer and Whittaker, , Szymanski
et al., 2021 , Wang et al., 2019 a], useful as pre-studies but not general-
|     |     |     |     | 12  | 20  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
izable (they involved from to participants in our corpus), or the
analysis of free text comments, which can be implemented more easily
on a larger scale[Naiseh et al., 2021 a, Szymanski et al., 2021 , Zytek etal.,
2021
|     | ]. Further, | the | ability of | XAI systems |     | to capture | users’ | mental | states |
| --- | ----------- | --- | ---------- | ----------- | --- | ---------- | ------ | ------ | ------ |
could be complemented by a memory of these states and a memory of
| what | has   | already been                                        | explained | [Miller,  | 2019       | , Naiseh | et  | al., 2021 | b]. |
| ---- | ----- | --------------------------------------------------- | --------- | --------- | ---------- | -------- | --- | --------- | --- |
|      | 3.5.5 | FocusonstrategiesbeyondXAI:contextualization,train- |           |           |            |          |     |           |     |
|      |       | ing, timing,                                        |           | cognitive | forcing... |          |     |           |     |
Various work in our corpus mentioned the need to pay more atten-
2021
tion to other interaction design choices [Buçinca et al., , Zhang et al.,
2021 ]beyondthechoiceofanexplanationmethod. Theseincludecontex-
tual information, training, timing, framing, and other specific strategies
tomitigatecognitivebiases. Forexample,Simkuteetal.[ 2020 ]suggested

110 the explanation paradox and the human centric path
-
the use of gamification strategies in low-stakes environments to address
thelackofmotivationofsomeusers,andtheuseoffeedbackandcontrols
in high-stakes environments. Others stressed the need to clarify specific
2015
elements in the explanations. Bussone et al. [ ] proposed present-
2021
ing how the explanations were derived, which Dazeley et al. [ ] calls
2021 2019
"meta-explanations". Buçincaetal.[ ],LaiandTan[ ],Wangetal.
2019
[ a] suggested to delay showing the AI’s prediction and/or explana-
2021
tions to decrease overreliance issues. Nourani et al. [ ] recommended
tocontrolthetypeofpredictionsthatusersobservewhenlearningtouse
the system, during the initial instructions and training phase. Finally,
2021 2021
Buçinca et al. [ ], Naiseh et al. [ b] proposed cognitive forcing
functions and friction-based strategies to address users’ lack of curios-
ity. Cognitive forcing functions consisted in making users wait for the
explanations, updating them or asking for them. The friction function
2021
designed by Naiseh et al. [ a] consisted in asking the user to confirm
that they did not want to review the explanation. All these strategies
proved to be useful in decreasing user’s unjustified trust, though it de-
creased their satisfaction in the system.
3.5.6 Give arguments against the prediction
TheideaofexplainingnotonlytheAI’spredictionbutalsoalternative
2015
possibilitiesappearedinseveralpapers[Bussoneetal., ,Wangetal.,
2019 2018
a,WeldandBansal, ]asawaytocounterautomationbias. Wang
et al. [ 2019 a] recommended to support "premortem of decision outcomes",
a reasoning consisting in trying to disprove a hypothesis. Bussone et al.
2015
[ ]highlightedcommentsfromparticipantssayingtheywantedtosee
bothpositiveandnegativeevidenceforthesuggestedmedicaldiagnosis.
Finally, Bansal et al. [ 2021 ] envisioned an AI that would play"adevil’sad-
vocate role, explaining its doubts, even when it agrees with the human". They
proposedaprototypeofsuchanexplanationandfoundthatwhileitwas
effective in informing the human that the AI might be wrong, it was not
sufficient to reduce significantly errors related to overreliance. One of
the main challenges is getting users to come up with their own solution
when they are informed that the AI may be wrong. Additional work
is still needed to find the right kind of interaction that could help users
2021
detect that the AI is wrong [Bansal et al., ], but the direction seems
promising,notablyfortworeasons. First,itremindsusoftheadversarial
structure of a judicial system where two parties (a defense attorney and
a prosecutor) present opposing arguments. Implementing such “adver-
sarial explanations” could increase societal trust in the AI-aided decision
process. Second, a necessary condition for free will is the availability of
alternative possibilities, or the ability to "choose otherwise" [McKenna
2021
and Coates, ]. Therefore, showing alternative explanations to the
decision-maker helps with sustaining her autonomy and accountability.

trust overtrust distrust in explainable ai a cognitive approach 111
, , :
3.6 Limitations
Since our goal was to provide insight into how the XAI field has con-
sidered cognitive biases to date, we used a systematic search methodol-
ogy. ThisallowedustocoverabroadsampleofarticlesonXAI.However,
it is possible that some articles did not use our general search terms on
cognitive biases and focused on specific types of cognitive biases in XAI.
Our paper augmentation is limited by potential biases in the authors’
viewoftheXAIfield. Tocontinuethislineofresearchoncognitivebiases,
future review work could focus on specific biases, such as “automation
bias”. Evidently, our list of cognitive biases cannot be considered as the
finite list of biases affecting explainable AI systems, there are numerous
othersinthecognitivescienceliteraturewhichmaybeworthstudyingin
thecontextofXAI.Moreover,itwasquitedifficulttoassessthegeneraliz-
ability of the results presented in our corpus. To address this limitation,
we tried to preserve the context in which these results were obtained —
explainabilitytechnique,usertype,andtasktype. However,itispossible
thattheseresultsdependonmoregranulardetails. Finally,weleaveitfor
futureworktoproducemoreinteractiveversionsofaheuristicmapsuch
2021
as the one we present, in a similar fashion as Suresh et al. [ ]. This
couldfacilitatethetrackingofcognitivebiasesthathavebeenhighlighted
in the explainability literature and the contexts in which they have been
highlighted.
3.7 Conclusion
38
In this chapter, we presented a scoping review of papers — from a
285
corpusof papers—toinvestigatewhatkindofcognitivebiaseswere
identified in the presence of explainable AI systems. In addition, we
conducted a qualitative analysis of these papers, providing a map of the
different cognitive biases and revealing the context in which they occur,
specificallywithwhichXAItechnique,typeofuser,andAI-assistedtask.
Furthermore, our mapping shows the different ways in which these
biases affect XAI-assisted decisions. We highlighted the ways in which
explainableAIcanoftenleadtoovertrust,ordistrust,thelatteroccurring
eitherwithexpertusersorwithincompleteexplanations. ExplainableAI
hassometimesbeenmisusedbyendusers,whohavebeenshowntomis-
understandsomelinguisticelementsorprobabilities,torelyonirrelevant
informationfromtheirpriorexperiences,ortobesensitivetotheframing
and timing of the explanation. Cognitive biases can also affect the way
explanations are evaluated in user studies. However, explanations can
still contribute to correct cognitive biases such as confirmation bias, cor-
rectingoverlypositiveexpectationsofAIsystemsorbelievingpersuasive
claims that are unsupported by evidence.
Overall, explanations tend to have a positive effect on trust. This
can lead to an "explanation paradox", where explanations may increase
users’ unwarranted trust and make them more vulnerable, rather than
empoweringthemwithinformationabouttheAI’sprediction. Important

112 the explanation paradox and the human centric path
-
factors in calibrating trust in explainable AI systems include user exper-
tise, taskexpertiseandtaskfamiliarity, estimationoftheAI’sconfidence,
explanation completeness, timing of explanations and users’ motivation
and individual cognitive characteristics (need for cognition, rational or
intuitive decision-making style...). We provided several directions for fu-
ture work that pave the way for meeting users’ cognitive needs.
In the next chapter, we explore whether interactive explanations can
effectively address this search for human-centric and even ’human-like’
explanations.

| Chapter     | 4   |     |              |     |         |     |     |     |
| ----------- | --- | --- | ------------ | --- | ------- | --- | --- | --- |
| Towards     |     |     | "human-like" |     |         |     |     | ex- |
| planations: |     |     |              | the | promise |     |     |     |
of interactivity
"Explanations should be interactive, allowing the explainee to
| revise and | consolidate |     | some | previous | background |     | knowledge." |     |
| ---------- | ----------- | --- | ---- | -------- | ---------- | --- | ----------- | --- |
Confalonierietal.[2021]
o address
T the trust calibration challenges posed by cognitive biases,
we have stressed the importance of the human-centric approach, and to
take into account the human cognitive explanation process. Both em-
3
pirical research surveyed in Chapter and theories in psychology and
sociology support this view. Interactivity in explanations has been ad-
vanced by recent work on human-centered XAI as a promising way to
align with cognitive human architecture and support reconciliation with
prior beliefs [Chen et al., 2023 , Wang et al., 2019 a, Adadi and Berrada,
| 2018     | 2019 |               | 2021 |             | 2019 |              | 2020 |     |
| -------- | ---- | ------------- | ---- | ----------- | ---- | ------------ | ---- | --- |
| ,Miller, |      | ,Langeretal., |      | ,Aryaetal., |      | ,Longoetal., |      | ,   |
|          |      | 2020          |      |             | 2021 |              | 2016 |     |
Atakishiyev et al., , Confalonieri et al., , Krause et al., ].
However,empiricalresearchoninteractiveexplanationsisstillemerging,
and it is still unclear whether they really live up to their promise. In par-
ticular,itremainsuncertainwhethertheyareabletocorrecttheovertrust
and overreliance effects that "normal" explanations tend to produce, as
2
| seen in Chapter |     | , or whether, | on  | the contrary, | they | exacerbate | them. |     |
| --------------- | --- | ------------- | --- | ------------- | ---- | ---------- | ----- | --- |
In this chapter, we examine what are the different types of interactive
explanations and to what extend they align to the human explanation
process through a detailed scoping review. We also take stock of their
effectonusertrustandrelianceonAIsystemsandotheruser-basedmet-
rics. Section 41 . outlines the motivation for the survey presented in this
42
chapter and researchquestions. Section . describes the relevantrelated
45
work and Section . lays down the survey methodology used. The re-
sults are a taxonomy of the interaction types for explainablity, and an
analysis of interactive explanations’ usage, evaluations and effects. They
arepresentedinSection 44 . . Finally,Section 45 . discussesopenchallenges

| 114 the | explanation |     | paradox | and | the human | centric path |     |     |
| ------- | ----------- | --- | ------- | --- | --------- | ------------ | --- | --- |
-
| for interactive |            | XAI. |     |          |           |     |     |     |
| --------------- | ---------- | ---- | --- | -------- | --------- | --- | --- | --- |
| 4.1             | Motivation |      | and | research | Questions |     |     |     |
Building on natural sciences theories is common practice in HCI. The
objectiveistodesignartefactsthatalignwithhumancognitiveprocesses.
Recent work in HCI has focused on aligning explanation design with
people’scognitiveexplanationprocess,resultingintheadvocacyofmore
interactiveexplanations[Longoetal., 2020 ,Atakishiyevetal., 2020 ,Con-
|                 |     | 2021        |     | 2019          |     | 2016               |     |     |
| --------------- | --- | ----------- | --- | ------------- | --- | ------------------ | --- | --- |
| falonierietal., |     | ,Aryaetal., |     | ,Krauseetal., |     | ]. Relevantresults |     |     |
in the social sciences for explanations are summarized succinctly in Fig-
ure 41 . .
4.1:
|     |     |     |     |     |     |     | Figure      | Summary of    |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- |
|     |     |     |     |     |     |     | the role of | explanations, |
theprocessbywhichwe
|     |     |     |     |     |     |     | construct | and present |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------- |
explanationsandthebi-
|     |     |     |     |     |     |     | ases involved | in expla- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------- |
nations.
For example, people expect explanations to be provided in a person-
2017
alized request-response pattern [Graaf and Malle, ]. In addition, as
seen in Section 23 . presenting explainability literature in the social sci-
ences,onedoesnotask"whyP?"butrather"whyPandnotQ?"[Hesslow,
| 1988     | 1990 |                  |     | 2019 |                                |     |     |     |
| -------- | ---- | ---------------- | --- | ---- | ------------------------------ | --- | --- | --- |
| ,Lipton, |      | ,Millecampetal., |     |      | ]. Thatistosay,explanationsare |     |     |     |
contrastive. Theseexplanationcharacteristicscallforwaystoenableuser
interaction with explanations, and to make explanations more respon-
2021
sive. Rohlfing et al. [ ] emphasises thath these considerations are still
largely unaddressed in the explainability literature and calls for a ’social
practice’ of explanation in which explainers and explainee co-construct
understanding.
Furthermore,researchinthefieldofeducationshowsthatinteractivity
1997 1994
plays a fundamental role in learning [Sims, , Barker, ]. Barker Figure 4.2: Illustrative
| 1994 |     |     |     |     |     |     | example | of interactive |
| ---- | --- | --- | --- | --- | --- | --- | ------- | -------------- |
[ ] describe interactivity as "a necessary and fundamental mechanism for
|     |     |     |     |     |     |     | explanation: | "Conver- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- |
knowledge acquisition". Although the objectives of an explainable AI user
|     |     |     |     |     |     |     | sational | XAI" enables |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ |
may not include long-term learning, they generally revolve around ac-
|     |     |     |     |     |     |     | users to | interact with |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- |
quiring knowledge about the AI system. We can therefore consider the users through natural
problem of explainability as a learning one, reinforcing our assumptions language.
| about the | important | role | of  | interactivity. |     |     |     |     |
| --------- | --------- | ---- | --- | -------------- | --- | --- | --- | --- |
The term "interactive", however, can refer to many different kinds of
user interactions. According to Miller [ 2019 ], the ideal interaction model

towards human like explanations the promise of interactivity 115
" - " :
follows a human-like dialogue structure, where the AI agent is able to
answer a series of questions. Other types of user interaction have been
implemented by XAI researchers, such as simulating the black box with
2019 2021 2018
newinputs[Chengetal., ,Chromiketal., ,Morrisonetal., ],
2019
re-configuring the explanation space [Hohman et al., ], changing ex-
2021 2020
planations[Khuranaetal., ,Spinneretal., ],etc. However,these
studies in XAI do not use a common vocabulary to designate different
interaction types, making it difficult to study and draw general conclu-
sionsonthedifferentformsofinteractiveXAI.Thevisualization(Infovis)
2007 2002 1990 2005
[Yietal., ,Keim, ,RothandMattis, ,Wilkinson, ,Amar
2005 1997
et al., ] and other Human-Computer Interaction (HCI) [Sims, ,
1985
Rhodes and Azbell, ] communities have done extensive work on the
classification of different modes of interaction. The explainability field is
less mature. We believe that the explainability field would benefit from
using a more precise and shared vocabulary to designate the different
types of interactivity, taking inspiration from other HCI sub-fields.
Due to the increasingly large number of articles on XAI, researchers
may be overlooking best practices and opportunities for interaction. To
1997
illustratethecomplexityofdesigninginteractions,Sims[ ]referredto
it as "an art" requiring multiple considerations and a vast array of skills
on the part of designers. This work aims at helping XAI system builders
by centralizing examples of interactive explanations taken from various
contexts (user expertise, XAI method, domain...).
Over the past few years, a growing body of work has been testing
interactiveXAIsystemswithrealusers,generatingsometimesseemingly
2019
contradictory observations. Cheng et al. [ ] find that the possibility
to simulate new predictions by changing input features improved user
understanding compared to static explanations. However, concerns were
2021
expressedinLiuetal.[ ]becauseinteractiveexplanationswerefound
to reinforce users’ overreliance on AI suggestions. One possibility is that
interactive explanations were more complex to interpret in [Liu et al.,
2021
]’s study, leading to information overload. Another possibility is
that understanding a model may not help much when the model and
the user disagree. In short, explanations may not be so useful at helping
people determine whether to trust one’s own intuition or to trust the
model output. At this stage, review work is needed to summarise the
effects of interactive XAI from a user perspective, paving the way for
subsequent systematic reviews to formally disentangle these findings.
In this work, we conduct a detailed scoping review on interactive and Figure 4.3: Illustrative
user-evaluated explainability systems. We survey two popular digital example of interactive,
rule-based explanation
libraries for the HCI community: IEEE Xplore and ACM Digital Library.
where users can create
We are guided by four research questions.
andmodifyrules.
RQ1: What are the interactivity approaches that have been implemented so far
in the explainability field?
RQ2: Inwhatcontext,withwhatcontent,andinwhatformweretheinteractive
explanations presented to users?
RQ3: What are the metrics used in user-based evaluations of interactive expla-
nations?

116 the explanation paradox and the human centric path
-
RQ4: What are the effects of interactive explanations on users’ perception of
explanations?
To the best of our knowledge, we present the first review of the effects of
interactive explainable AI on user experience.
4.2 Background
Below, we highlight work in HCI, XAI, and education that is relevant
for our work. We also highlight, through these different strands of lit-
erature, reasons to believe that interactivity in explainability could help
users in building sense and knowledge about models.
4.2.1 Interactivity in HCI
Defininginteractivityproveschallenging,andmultipledefinitionshave
been offered over time. Early work on interactivity defined it simply as
1997
the extent to which a user can "activate" [Sims, ] or "exert an influ-
2010 1992
ence" [Sundar et al., , Steuer, ] on the technology being used, its
1997 1997
form and its content. In , Sims [ ] mentioned that "there appears
to be no consensus of what interactivity actually represents or involves".
1998 1996
DixandEllis[ ]andFoleyetal.[ ]broadlydefineitusingthekey-
words"communicationbetweenuserandsystem"and"human-computer
2007 2007
dialogue"[Yietal., ]. InInfovis,Yietal.[ ]viewinteractiontech-
niques as "the features that provide users with the ability to directly or
indirectly manipulate and interpret representations". The authors noted
that Infovis systems were designed to communicate information from
the computer to the user, but less so for the user to enter data, thus over-
lookinganentireaspectofinteractioninHCI.Therefore,differencesarise
betweenHCIsubdomainsonhowinteractivityisdefined. Atfirstglance,
it seems that the vision adopted by the Infovis domain could correspond
to interactivity in XAI. In the explainability field as well, the user needs
to manipulate, interpret and discover information about the model from
441
explanations or raw data. In Section . . , we will examine how adapted
the Infovis’ view of interaction is to the XAI domain. Despite the lack
2017
of a consensual definition, Janlert and Stolterman [ ] state that "there
seemstobeacommonsenseunderstandingofinteractivityassomething
fairlysimple"thatHCIresearchersseeas"thecontrolandactionbetween
a human and an artifact or system."
However, defining the different types of interactions quickly compli-
cates the task. Some studies have addressed it by proposing taxonomies
of user-system interactions. Early ones attempted to provide holistic
views of the interaction space in HCI; they focused on interaction lev-
els, with the idea that "the higher the interaction level, the better the
1997
product" [Sims, ]. For example, Rhodes and Azbell [Rhodes and
1985
Azbell, ] introduced a three-level scale of interactivity, ranging from
reactive to proactive to coactive. Schwier and Misanchuk [Schwier and
1993
Misanchuk, ] added two other dimensions to this taxonomy: func-
tions (confirmation, pacing, navigation, inquiry, elaboration) and trans-

towards human like explanations the promise of interactivity 117
" - " :
actions (keyboard, touch screen, mouse, voice). Sims’ taxonomy [Sims,
1997
] extends the two previous ones by intertwining functions and lev-
els. It is presented as a scale from basic to complex with the following
levels of interactivity: object, linear, hierarchical, support, update, construct,
reflective,simulation,hyperlinked,nonimmersivecontextualandimmersivevir-
tual. In the Infovis domain, there is typically no hierarchy between in-
teraction types; however, taxonomies with finer granularity have been
2007
designed. For example, Yi et al. [ ] observes a difference of approach
betweensystem-centrictaxonomies(includingcategorieslike"interactive
linking and brushing" [Keim, 2002 ] or "navigating", e.g. zooming, pan-
2005
ning[Wilkinson, ])anduser-task-centrictaxonomies(includingcate-
1990
gorieslike"comparewithinrelations"[RothandMattis, ]or"retrieve
2005 2007
value" [Amar et al., ]). The taxonomy in [Yi et al., ] proposes to
"connect user objectives with the interaction techniques that help accom-
plishthem."Itincludessevencategories: select,explore,reconfigure,encode,
abstract/elaborate, filter, connect. Yi et al.’s taxonomy has been extensively
used and referred to in Infovis in the last decade.
4.2.2 Interactivity in Explainability
The call for more interactive explanations in XAI finds roots in results
from the social sciences about how people communicate explanations
and in the growing number of studies focusing on human needs rather
2019
thansolelytechnicalaspects. Forexample,Miller[ ]findsthat"anex-
planation is an interaction between two roles: explainer and explainee".
As such explanations should be thought as a social process, i.e. a con-
versation. The paper also mentions the rules that govern this interaction
1975
such as Grice’s maxims [Grice, ] of quality (say only what is true),
quantity (say no more than you need to), relation (say what is relevant
to the conversation) and manner (say it in a nice way). Although it is
easier to imagine these exchanges taking place in natural language, Tim
Miller argues that this interaction can use other media such as images,
keywords, or logical rules, while still respecting Grice’s maxims. This
work envisions what "human-like" explanations may look like, noting
that users of XAI systems will expect explanations to be delivered in this
manner.
The line of research on interactive XAI has begun to investigate how
to tailor explanations to users. Work pertaining to the technical as-
pectsofXAIalsoidentifiestheimportanceofsuch"user-centric"explana-
2020 2019
tions. [Sokol and Flach, , Schneider and Handali, ]. Numerous
papers have emphasized the need for explanations that are tailored to
the context, audience and purpose of the explanation [Doshi-Velez and
2017 2018 2018
Kim, , Adadi and Berrada, , Ras et al., , Ferreira and Mon-
2020 2018 2019
teiro, ,Došilovic´ etal., ]. SchneiderandHandali[ ]reviewed
XAI studies focusing on personalization. For each paper in their corpus,
they documented personalized explanation properties (complexity, con-
tent and presentation), personalization granularity (to each user or per
categoryofuser)andpersonalizationautomation(manualorautomatic).
Additionally, they observed that personalization of explanations can be

118 the explanation paradox and the human centric path
-
either iterative or one-off, with user information being collected once
2019
prior to showing explanations [Schneider and Handali, , Sokol and
2020
Flach, ]. Whilethepersonalizationofexplanationsisparticularlyim-
portant given the role of explanations in filling one’s specific knowledge
gaps, we believe there is a greater granularity of interaction to explore
2019
beyond the categories mentioned in [Schneider and Handali, ].
24
As seen in Section . , more and more HCI researchers have been
investigating user’s needs for XAI using standard HCI methods [Kou
2020 2009 2018 2022
and Gui, , Lim and Dey, , Penney et al., , Sun et al., ].
These efforts have resulted in numerous examples of sophisticated in-
teractive interfaces integrating sometimes complex XAI techniques. For
example, the strand of research called "conversational XAI" made sig-
nificant strides in providing explanations in natural language to a wide
2020 2021
range of user questions [Sokol and Flach, , Hepenstal et al., ,
2021
Hernandez-Bocanegra and Ziegler, ].
4.2.3 Interactivity for learning and sensemaking
Explainability is also deeply connected to results in educational re-
search. The parallel seems natural, as the field of explainability aims to
improve human understanding of algorithms, or for machines to teach
2019
humans about their breakthroughs [Schneider and Handali, ]. Ac-
2004
cording to Roussou [ ], many educational researchers agree that in-
teractivity plays an important role in learning, notably by supporting
"learningbydoing". Amthor[ 1992 ]arguesthat"peopleretainabout20%of
what they hear; 40% of what they see and hear; and 75% of what they see, hear,
and do". This follows the constructivist approach, which emphasizes the
need for people to build knowledge by testing and simulating new situ-
1903 2004
ations that have meaning for them [Dewey, , Roussou, ]. Kent
et al. [ 2016 ] demonstrates through quantitative user studies "the role of
interactivity as a process of knowledge construction" and further asserts that
interactivity patterns inform on the actual learning process of an indi-
2007
vidual. Evans and Gibbons [ ] find that interactivity promotes deep
learning by stimulating users’ cognitive engagement in the learning pro-
cess. To tie more concretely these results to the explainability field, we
can draw a parallel between the processes of learning, knowledge con-
2022
struction and that, closely related, of sensemaking. Cabrera et al. [ ]
studiedthecognitiveprocessofsensemakingofmodels,andhighlighted
that "understanding of models is an iterative and ongoing process", motivat-
ing the need for their XAI system to be interactive. In this case, the
sensemaking—or knowledge construction—, comes from the ability to
iterate between the discovery of instances, the formation of hypotheses,
their evaluation, etc.

towards human like explanations the promise of interactivity 119
|     | "   | - " |     | :   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
4.3 Methodology
To review the role of interactivity in XAI, we conducted a scoping
716
review drawn from an initial extraction of papers, narrowed down
48
to our final corpus comprising articles. In this section we detail the
| characteristics | and different | phases of | the survey | method. |     |     |
| --------------- | ------------- | --------- | ---------- | ------- | --- | --- |
| 4.3.1           | Review type   |           |            |         |     |     |
This chapter presents a scoping review [Arksey and O’Malley, 2005 ],
331
as presented in Section . . . The scoping review methodology corre-
sponded to our objectives of identifying, mapping, reporting and dis-
cussing the available evidence on interactivity in XAI. As in the previous
chapter, we also rely on a standardized search and selection methods
2021
from the systematic review methodologies [Page et al., ], as sug-
gested in [Arksey and O’Malley, 2005 ] for scoping reviews, to ensure
the replicability and transparency of our findings. We followed the pa-
peridentification,screening,eligibilityevaluationandanalysisprocedure
stages outlined in the PRISMA methodology [Page et al., 2021 ] to guar-
2018
antee the quality of our search and selection process [Tricco et al., ].
|     |     |     |     |     | Figure 4.4: PRISMA   |        |
| --- | --- | --- | --- | --- | -------------------- | ------ |
|     |     |     |     |     | flow diagram adapted |        |
|     |     |     |     |     | from Page et al.     | [2021] |
However, our work goes beyond what is traditionally expected of a
|     |     |     | 445 | 444 | giving an overview | of  |
| --- | --- | --- | --- | --- | ------------------ | --- |
scoping review in particular in Sections . . and . . , where we ad- 2020
|     |     |     |     |     | the PRISMA | sur- |
| --- | --- | --- | --- | --- | ---------- | ---- |
vance a summary of the effects of interactivity through Figure 419 . . We
|     |     |     |     |     | vey guidelines, used | for |
| --- | --- | --- | --- | --- | -------------------- | --- |
arguethatthisstepenablesustobetterdelimitgapsintheliterature,and the search and selection
|     |     |     |     |     | phases of our scoping |     |
| --- | --- | --- | --- | --- | --------------------- | --- |
provide qualitative grounds for a following systematic review on a more
review.
restrictedsetofstudies. Thisanalysisismadepossiblethroughaminimal
quality control of the included studies that we enforced through the ex-
clusion of entries that were not published in a peer-reviewed conference
proceeding or journal. However, a more thorough quality assessment of
studies—which entails a restriction on the scope of the survey—should
be performed in order to extract quantitative evidence about the effects
of interactivity. Here, we aim at identifying the different types of re-
sults in the interactive explainability field and orientate further research.
Section 46 . discusses the limitation of the methodology in further detail.
| Forallthesereasons, | werefertoourtypeofreviewasadetailedscop- |     |     |     |     |     |
| ------------------- | ---------------------------------------- | --- | --- | --- | --- | --- |
ing review.

120 the explanation paradox and the human centric path
-
4.3.2 Corpus creation
Identification. We focused on the ACM Digital Library and IEEE
Xplore, two popular databases for the HCI community, which encom-
passprominentpublishingvenuesfortheexplainabilityfield(ACMCHI,
ACM IUI, IEEE VIS, IEEE TVCG...). Consequently, we focused on XAI
work that mainly—though not exclusively—pertain to the HCI commu-
nity, rather than the computer science side of XAI. The main reason for
this is that our focus was on interactivity and user studies—two topics
finding roots in HCI. Moreover, the CS side of XAI has been historically
and predominantly occupied with technical advances in XAI [Doshi-
2017
Velez and Kim, ], and has only very recently taken into considera-
tion the user’s perspective. While we acknowledge that more interactive
XAI systems have been emerging from the CS community recently, such
2022
as[Slacketal., ],interactiondesignhasbeenquitedistantfromtheo-
2018
reticaldomainsincomputerscience,asmentionedin[Abduletal., ].
This led us to focus on HCI databases and leave out works published in
purely AI conferences, such as NeurIPS, AAAI, or CVPR, among others.
Our aim was to review different types of interactive explanations, fo-
cusing on how they are perceived by end users. Therefore, we narrowed
ourfocustoworkpresentinganXAIinterfaceandincludingauser-based
evaluation of the XAI system. Note that there also exist non user-based
2017
evaluations of XAI methods. Doshi-Velez and Kim [ ] distinguish
three evaluation strategies: application-grounded—testing explanations
in real-word settings with domain experts—, human-grounded—testing
explanations with lay users—, and functionality-grounded—testing ex-
planations using metrics that do not require human feedback. The scope
of our survey is limited to empirical studies with human subjects, as we
are interested on the users’ perception of XAI systems. Providing insight
into how people interact with XAI can guide practitioners in making
more effective technical and design choices.
Thekeywordsearchwascontextualizedfocusingonthreedimensions:
AISystems, Explainability and Userstudies. The term "interaction" is ubiq-
1
uitousinHCI ,andassuchwedidnotrestrictourkeywordsearchtothis 1for example the CSS
dimension, choosing instead to select articles on interactive explanations concepts section in
ACM papers often
in the eligibility phase. Since we wanted to focus on articles whose main
includetheterm
topic was AI, we searched for keywords representing AI systems and
explainability dimensions in the Title, Abstract and Author Keywords
fields. For the user study dimension, we searched the full text of the ar-
ticles: we noticed that often, authors do not explicitly mention that they
conducted a user-based evaluation in their abstract. The search results
2015
were limited to relatively recent articles ( or later), as XAI is a recent
2016 2017
field of study, found to be expanding around - [Barredo Arrieta
2020 2018
et al., , Adadi and Berrada, ]. In addition, user-based evalua-
tionsandinterestfromtheHCIcommunityinthedomainareevenmore
2017 2015
recent [Doshi-Velez and Kim, ]. Using as a starting point, we
are sure to capture the uptake in number of contributions in XAI.
In addition, we used ACM DL and IEEE Xplore filtering tools to nar-
row our search to research articles only. In ACM DL, we used the fol-

towards human like explanations the promise of interactivity 121
|     |     |     | "   | -   | "   |     | :   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lowing filter: All Publications/Proceedings/Content type/Research arti-
cleANDAllPublications/Journals/Contenttype/Researcharticle,there-
fore excluding surveys, tutorials, introductions, editorials, newsletters,
books, magazines, reports, encyclopedias, short papers, extended ab-
stracts, posters, and other non-archival content. In IEEE Xplore, we used
the filters Conferences and Journals, leaving out early access articles,
magazines, books and standards. This step allowed us to make a first
sorting of the non-archived articles, and facilitate the following phase
of manual screening. For each record, the article title, authors, publica-
tion venue, and publication year were exported to an Excel spreadsheet.
Below is the search query used (the wildcards * denote where we have
| retrieved | the | plurals | and | term variants): |     |     |     |     |     |
| --------- | --- | ------- | --- | --------------- | --- | --- | --- | --- | --- |
AI systems => Abstract: (AI, artificial intelligence, machine learning, al-
| gorithm*) |     | AND |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Explainability => Abstract: (explainab*, explanation*, intelligib*, inter-
| pretab*, | transparen*, |     |     | XAI) AND |     |     |     |     |     |
| -------- | ------------ | --- | --- | -------- | --- | --- | --- | --- | --- |
User studies => Abstract: (participant*, human-subject*, human evalua-
| tion*, | human | experiment*, |     | user-stud*) |     | AND |     |     |     |
| ------ | ----- | ------------ | --- | ----------- | --- | --- | --- | --- | --- |
2015
| Date =>    |               | or after         | AND     |                 |                                   |         |              |      |     |
| ---------- | ------------- | ---------------- | ------- | --------------- | --------------------------------- | ------- | ------------ | ---- | --- |
| Journal    | or conference |                  | article | => Non-archival |                                   | records | pre-filtered | out. |     |
| Screening. |               |                  |         | 44              |                                   |         |              |      |     |
|            |               | Oneauthordeleted |         |                 | recordsthatwereeitherduplicatesor |         |              |      |     |
non-archivalrecordsthatremainedafterthedatabasefiltering(primarily
workshop entries and student consortia). This step resulted in a total
| corpus | of 672 | unique | papers. |     |     |     |     |     |     |
| ------ | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- |
Eligibilityevaluation. Theremainingrecordswererandomlyassigned
to three of the authors, who performed a two-phase eligibility assess-
ment: a first one based on the title and abstract and a second, more in-
depthonebasedonthefulltext. Thefirstphasewasprimarilyconcerned
|     |     |     |     |     |     |     |     | 1 2 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
with excluding recordings that were not focused on XAI (IC , IC ), that
did not include a human-AI interaction (IC 3 ), or that were a secondary
|     | 7   |     |     |     |     |     | 4   | 5   | 6   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
study (IC ). The second phase consisted of verifying IC , IC , and IC ,
sincefull-textviewingwasrequiredtoassessthesecriteria. Theinclusion
| criteria       | were   | the following:                               |         |              |     |                          |     |        |     |
| -------------- | ------ | -------------------------------------------- | ------- | ------------ | --- | ------------------------ | --- | ------ | --- |
| IC1 XAI        | focus. | The                                          | paper’s | contribution |     | is in the explainability |     | field; |     |
| IC2 XAIsystem. |        | ThepapershowsanimplementationofanXAIsystems; |         |              |     |                          |     |        |     |
IC3 Human-AI interaction. The paper is in the field of human-AI interac-
| tion | (works | in human-robot |     | interactions |     | are excluded); |     |     |     |
| ---- | ------ | -------------- | --- | ------------ | --- | -------------- | --- | --- | --- |
IC4 User-basedevaluation. Thepaperpresentsanevaluationofitsexplain-
ability approach using human-grounded evaluation [Doshi-Velez and
| Kim, | 2017 | ];  |     |     |     |     |     |     |     |
| ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
IC5 Human-computerinterface. The paper describes the interface that was
| presented |     | to the | human | users evaluating |     | the XAI | system; |     |     |
| --------- | --- | ------ | ----- | ---------------- | --- | ------- | ------- | --- | --- |

122 the explanation paradox and the human centric path
-
IC6 Interactivity. The explainability approach presented in the paper is
interactive,meaningtheusercaninteractwiththeexplanation(requiring
another interaction than that with the interface to perform a specific
2
task) ; 2Some examples of pa-
pers excluded because
IC7 Primary study. The paper is not a review nor a position paper. of IC6 are [Bansal et al.,
2021, Buçinca et al.,
Afterthethreereviewingauthorshadcompletedtheeligibilityphase,an 2020, Dominguez et al.,
external reviewer was asked to apply the above criteria to a subset of 67 2019], which present
672 10 static explanations to
articles randomly selected from the base of papers, representing %
end-users, although the
92
ofthepapers. Inter-raterreliabilitywas %,andtheremainingdisagree-
user interface to per-
ments involved mostly cases in which the external reviewer included the formadownstreamtask
articles when the authors did not. However, we believe that the extra maybeinteractive.
step of reviewing the full text in detail is what justified the exclusion of
the items that the external reviewer included.
2021
One of the articles included in our corpus [Gu et al., ] was an
analysis of an external primary study that did not match our keywords
because it did not mention explainability-related terms in the abstract,
but it met our inclusion criteria. We therefore replaced the secondary
2020
study with the primary study [Yan et al., ].
48
Eventually, papers met the inclusion criteria and were included in
the final corpus.
4.3.3 Analysis and coding book
Analysis process. The synthesis methodology we used in this review
2016
is an emerging synthesis [Schick-Makaroff et al., ], more specifically
a narrative account of included studies, as is usually the case in scoping
2005
reviews [Arksey and O’Malley, ]. To support this analysis, we use
a concept matrix and a charting approach to provide basic numerical
summaries of the extent, nature and distribution of the studies included
in the review.
2002
Following Webster and Watson [ ], we created a concept matrix
for the analysis of the interactivity landscape in the explainability field.
The matrix is organized into four dimensions, whether the concepts re-
late to the context of the explanation, its content, its communication, or its
user-based evaluation. Three authors independently coded and classified
the articles included in the final corpus. For the dimensions context and
content, the categories used for coding were predefined. In the com-
munication dimension, only the concept of "representation" had a set of
predefinedcategories. Withrespecttothetypeofinteractivity,thediffer-
ent categories were intentionally not preset in advance and each of the
three coders created their own categories after encountering an interac-
tive explanation implementation. We did this because our goal was to
create new categories that matched the range of interactivity types pro-
vided by the corpus. The authors then reviewed the resulting categories
and discussed how to reconcile them into a taxonomy of interactivity
2007 1997
typesadaptedfromwell-knownexistingones[Yietal., ,Sims, ].
A similar approach was taken for the evaluation portion of the matrix.
As new types of evaluations were found, new categories were created.

towards human like explanations the promise of interactivity 123
" - " :
Wegroupedtogetherconceptsthatwereverysimilar(suchasexplanation
utilityandexplanationusefulness). Finally,evaluationsthatwereusedonly
once in the corpus were regrouped in the "other" category of the matrix.
The authors of this work discussed and shared the definition of the no-
tions during several meetings. One author reviewed all the papers and
corresponding codings to check the consistency of the two other review-
ers’ coding with their own, and subsequently consolidated the matrix.
Below we detail the different concepts we have analyzed in each dimen-
sion.
Dimension Code Reference
Context
Domain LawandCivic,Healthcare,BusinessandFinance,Education,Leisure, [Laietal.,2021]
Artificial,Generic,Other.
Audience Domainexperts,AIexperts/Datascientists,Non-expert,Other. [Laietal.,2021]
Datatype Image,Video,Audio,Tabular,Naturallanguage,Sequentialdata. NA
Content
XAIfocus Raw Data, Output, Model Limitations, Model Confidence How?, [Lim and Dey,
Why?, Why not?, How to?, What if?, What’s the difference with?, 2009, Liao et al.,
Context. 2020, Sun et al.,
2022]
XAImethod Local Feature Contribution, Decision Rules, Sensitivity Analysis and [Laietal.,2021]
Partial Dependence Plot, Example-based, Saliency mask, Concept-
based,Surrogatemodel,Counterfactual,WizardofOz.
Communication
Interactivity Clarify, Arrange, Filter/focus, Reconfigure, Simulate, Compare, [Yi et al., 2007,
Progress,Answer,Ask. Sims,1997]
Representation Chart,Table,Text,Rules,Directlyonthedatastructure,Other. NA
Evaluation
Comparison Noexplanation,Staticexplanation,Other,Nobaseline. NA
Evaluation mea- Perceived usability, Perceived usefulness, Understanding, Perceived NA
sure explanationlength/quantity,TimespentinteractingwithXAIsystem,
Trust, Cognitive load, Performance at task, Learning, Predicted ac-
curacy, Perceived control, Perceived fairness, Perceived transparency,
Userskepticism,Other.
Only for evaluations using static or no explanation as a baseline: Higher
than,Sameas,Lowerthan[thebaseline],Other.
Table 4.1: Codebook
used to retrieve infor-
Context. We retrieved the environment in which the explanations for
mation from the corpus
each item were designed: domain, audience, and data type. The domain with four dimensions:
andaudiencecategoriesareadaptedfromthosefoundby[Laietal., 2021 ] [explanation] context,
intheirsurveyofAI-assisteddecisionmakingtasks. Thisallowsustosee content, communica-
tion and evaluation,
iftheinteractiveexplanationsarewelldistributedacrossthesecontextual
their corresponding
concepts.
sub-dimension and
reference from which
Content. To analyze the content of the explanation, we searched for
codes were inspired
the explanation focus, which described the type of information that was
from.
providedtotheuser,andtheexplainabilitymethodusedtoextractit. The
2009
list of explanation focus points was adapted from Lim and Dey [ ],
2020 2022
Liao et al. [ ] and Sun et al. [ ]’s classifications of user questions
in XAI. The categories of the explainability method were adapted from
2021
[Lai et al., ].

124 the explanation paradox and the human centric path
-
Communication. Communication refers to the form in which the ex-
planationwasprovidedtotheuser,includingthetypeofinteractionused
and the type of visual representation of the explanation. The categories
441
of interactivity are described in more detail in Section . . . The cate-
gories of representation were kept general as they were not the focus of
this study.
Evaluation. One of the main challenges in XAI is how to measure the
2015
quality of an explanation [Colquitt and Rodell, ]. User-based meth-
ods have been an increasingly adopted approach following calls such as
2017
Doshi-Velez’s [Doshi-Velez and Kim, ] to take user perspective into
account instead of just technical constraints. While "human-grounded"
evaluations may have drawbacks such as sampling bias or change blind-
2020
ness [Sokol and Flach, ], they do inform how end users understand,
perceive, and use explanations. This approach also has the advantage
that standard questionnaires are shared by researchers to measure con-
cepts such as trust (using the McKnight framework), satisfaction, un-
derstanding, cognitive load (using NASA-TLX), etc. We also retrieved
the baselines (no evaluation, static evaluation, other explanation, etc.)
used to evaluate the presented explanation in each empirical study. This
makesitpossibletocomparetheresultsofmultiplestudiesandtogetan
overview of assessments of interactive explanations. For each evaluation
in the corpus that used either static or no explanation as a baseline, we
reported the results according to four categories: higher than, same as,
lower than the baseline, or "other", which referred to more nuanced re-
sults dependent on other external factors, or to evaluations that did not
rely on a defined baseline.

towards human like explanations the promise of interactivity 125
" - " :
4.4 Results
4.4.1 Interactivity types in explainability: Select, Mutate,
Dialogue with
Let us now describe the categories of interactivity in XAI that we have
identified in our corpus. We took inspiration from other existing tax-
1997 2007
onomies of interactivity [Sims, , Yi et al., ] to define these cate-
1 2
gories. This section addresses our RQ and RQ .
Nine different categories of interactivity in XAI emerged from our
2007 1990
analysis. Following Yi et al. [ ] and Roth and Mattis [ ], we for-
mulatedthecategoriessothattheyexpressinteractionactionsthatcorre-
1997
spond to user intents. We adapted some categories from Sims [ ] and
2007
Yi et al. [ ]. However, contrarily to Yi et al.’s taxonomy, the object of
the interaction are explanations instead of datapoints. Explanations are
larger constructs encompassing a visual representation, an input data
range,anAImodel’sconfiguration(dataset,modeltypeandparameters)
and an explainability technique.
In addition to the categorisation of interaction types, we organized
the taxonomy into three different groups corresponding to the type of
support they provide for the human cognitive process of explaining.
This higher-level categorization is based on Miller’s review of social
science findings on properties of human explanations. Miller points out
that explanations are selective, contrastive, and social. First, explana-
tions are selective as they involve only a few causes in a large chain of
causal events. Only a few causes address the explainee’s question and
are thus relevant. Then, explanations are contrastive as they are thought
in contrast to a specific foil. People’s questions are almost always "why"
questionsimplyingafoil: "whydidPhappenedandnotQ?"Toassessthe
plausibilityofafactorasacauseofanevent,peoplethenneedtoperform
mental mutations, i.e. to cancel a factor which might have led to P and
see if Q happens, or to consider situations where Q happened instead of
P. This mental process is called the mutability of events and allows the
formationofcontrastiveexplanations. Finally,explanationsaresocialbe-
cause they are best understood in a conversation. The structure of the
dialogue allows people to get specific answers to their "why" questions
andcorrespondingfoils,toaskfollow-upquestionsandprogressivelyfill
the gaps in their knowledge.
Ourproposedinteractivitygroupsreflectthedegreetowhichtheinter-
active features enable these explanatory properties—selective, mutable,
social. The three categories are: select (interactive features facilitate the
selection of causes and the formulation of hypotheses), mutate (interac-
tive features allow users to compare or simulate different configurations
oftheAI’sinputs,outputsorparameters),anddialoguewith(interactiv-
ity allows users to engage in a conversation with the XAI system). The
42
resulting interactivity taxonomy is outlined in Table . .
Below we describe in detail the nine different categories of interactive
explanations, as well as three levels of interaction into which they fall.

| 126 the | explanation | paradox |     | and | the human | centric |     | path |     |     |
| ------- | ----------- | ------- | --- | --- | --------- | ------- | --- | ---- | --- | --- |
-
|          |          |     |            |     |     |     |     |     | Table 4.2: | Two-level tax-   |
| -------- | -------- | --- | ---------- | --- | --- | --- | --- | --- | ---------- | ---------------- |
| Function | Category |     | Definition |     |     |     |     |     |            |                  |
|          |          |     |            |     |     |     |     |     | onomy      | of interactivity |
Clarify
|        |              |     | Give additional                       |             | information/explanations |                 |     | on       | techniques       | in XAI, in-       |
| ------ | ------------ | --- | ------------------------------------- | ----------- | ------------------------ | --------------- | --- | -------- | ---------------- | ----------------- |
|        |              |     | demand                                |             |                          |                 |     |          | cluding          | a first level re- |
|        |              |     |                                       |             |                          |                 |     |          | flecting         | the type of sup-  |
| Select | Arrange      |     | Choose                                | and         | organize                 | the explanation |     | type(s), |                  |                   |
|        |              |     |                                       |             |                          |                 |     |          | port interaction | tech-             |
|        |              |     | parametersandvisualrepresentation(s). |             |                          |                 |     |          | niques           | provide to the    |
|        |              |     |                                       |             |                          |                 |     |          | cognitive        | process of ex-    |
|        | Filter/focus |     | Filter the                            | explanation |                          | according       | to  | an in-   |                  |                   |
|        |              |     |                                       |             |                          |                 |     |          | plaining,        | a second task-    |
put/inputmetric.
|     |     |     |     |     |     |     |     |     | oriented | level, and cor- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- |
Reconfigure Changethedataset,theAImodel,AImodelpa- respondingdefinitions.
|     |     |     | rameters | and | show me | the corresponding |     | pre- |     |     |
| --- | --- | --- | -------- | --- | ------- | ----------------- | --- | ---- | --- | --- |
dictionandexplanations.
Simulate
| Mutate |     |     | Changetheinputs,theoutputorthedatasetdis- |     |         |                   |     |      |     |     |
| ------ | --- | --- | ----------------------------------------- | --- | ------- | ----------------- | --- | ---- | --- | --- |
|        |     |     | tribution                                 | and | show me | the corresponding |     | pre- |     |     |
dictionandexplanations.
|     | Compare |     | Show me | explanations |     | of related | or  | selected |     |     |
| --- | ------- | --- | ------- | ------------ | --- | ---------- | --- | -------- | --- | --- |
datainputsoroutputs.
|          | Progress |     | Guideuserthroughanexplanationsequence.     |     |     |     |     |     |             |               |
| -------- | -------- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | ----------- | ------------- |
| Dialogue | Answer   |     | Givefeedback,editexplanationcomponents.    |     |     |     |     |     |             |               |
| with     |          |     |                                            |     |     |     |     |     | 3A parallel | can be        |
|          |          |     |                                            |     |     |     |     |     | drawn       | here with the |
|          | Ask      |     | Askiterativequestionsandreceiveanswersfol- |     |     |     |     |     |             |               |
"select"categoryfromYi
lowingadialoguestructure.
|        |     |     |     |     |     |     |     |     | et al. for       | the Infovis do- |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --------------- |
|        |     |     |     |     |     |     |     |     | main, which      | is defined      |
|        |     |     |     |     |     |     |     |     | as "marking      | something       |
| Select |     |     |     |     |     |     |     |     | as interesting". | Assum-          |
|        |     |     |     |     |     |     |     |     | ing we           | view this level |
3
The user may be able to select the information they wish to see by of interaction as "mark-
clicking on hyperlinks to display explanations on demand, by configur-
|     |     |     |     |     |     |     |     |     | ing an | explanation as |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------------- |
ingtheexplanationspace,orbyfilteringtheexplanationconditionallyon interesting", we found,
|     |     |     |     |     |     |     |     |     | however, | several sub- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ |
an input metric. These interactions can help users formulate hypotheses
|     |     |     |     |     |     |     |     |     | categories | of interaction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------- |
and actively search for factors that may lead to causal explanations. As
typesthatcouldbeused
| such, they | enable explanations |     | to be | "selective". |     |     |     |     |            |            |
| ---------- | ------------------- | --- | ----- | ------------ | --- | --- | --- | --- | ---------- | ---------- |
|            |                     |     |       |              |     |     |     |     | to support | this. This |
justifieswhywereferto
Clarify. Thissubsetofinteractioncapabilitiesenablestheusertomake it as a whole interaction
|     |     |     |     |     |     |     |     |     | level instead | of just one |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- |
on demand information appear, whether by clicking on or by brush-
category.
ing explanation components. In this approach, the user actively seeks
answers to their questions, controlling what explanation to display and
when it should be displayed. This set of interaction techniques is close
2007
to Yi et al. [ ]’s "elaborate" category. The analysis of our corpus re-
vealedthreemainwaysforausertogetclarificationonsomething. First,
users can navigate through a menu so as to choose the themes they want
to know more about. Sims [ 1997 ] refers to this interaction technique as
2021
"hierarchical interactivity". Anik and Bunt [ ] is an example of this
interactivity type. Second, explanations can be displayed after a user
clicks on a link, following Sims [ 1997 ]’s "hyperlinked interactivity". One
|     |     |     |     |     |     |     |     |     | Figure | 4.5: Example |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ |
2021
example is Sovrano and Sovrano and Vitali [ ]’s explanation system of the clarify interaction
in which the user can click on a concept to get more information about taken from [Anik and
Bunt,2021].
it. With each click, a new window with an explanation appears, itself
providing other hyperlinks about the notions used in the explanation.
Finally, tooltips are convenient interaction techniques to provide clarifi-

towards human like explanations the promise of interactivity 127
|     | " - | "   | :   |     |     |
| --- | --- | --- | --- | --- | --- |
cations and additional details on a visualisation in a non-overwhelming
way [Jin et al., 2020 , Shi et al., 2019 , Ahmad et al., 2019 , Sevastjanova
2021
et al., ].
Clarify interactions also allow the explanation interface to be less over-
whelming at first glance by disclosing explanations progressively. In a
study on the progressive disclosure of explanations, Springer and Whit-
taker [Springer and Whittaker, 2019 ] note that "because transparency is
provided ‘on demand’ this removes confusions and inefficiencies arising
from spurious, unwanted explanations, and adjusts explanations to the
users’ requirements." They also observe that this on demand disclosure
approach is able to adapt to the different reactions and expectations of
| each individual | user. |     |     |                         |     |
| --------------- | ----- | --- | --- | ----------------------- | --- |
|                 |       |     |     | Figure 4.6: Examples    | of  |
|                 |       |     |     | the arrange interaction |     |
Arrange. Arrange interaction techniques provide the user with the
|     |     |     |     | taken from [Hohman |     |
| --- | --- | --- | --- | ------------------ | --- |
ability to organize the explanation space as desired by hiding or collaps- 2019]
|     |     |     |     | et al., (top) | and |
| --- | --- | --- | --- | ------------- | --- |
ing explanations and selecting the type of explanation to be displayed [Chengetal.,2021](bot-
2019
[Kwon et al., ]. It is similar to the "rearrange" category in Yi et al. tom).
[ 2007 ]. Instead of interacting for more information, (which corresponds
to the Clarify category), here the user’s goal is to configure the explana-
2021
tion space following their preferences. For example, in Liu et al. [ ],
users can increase or decrease the number of highlighted words in the
2020
saliency-based explanation. In Collaris and van Wijk [ ], the user can
chose the surrogate model used in the explanation along with the other
| parameters for | that model. |     |     |     |     |
| -------------- | ----------- | --- | --- | --- | --- |
Filter/focus.
Inspired by Yi et al.’s "filter" category, the Filter/focus class regroups
controls that let the user zoom either on specific inputs of the AI model
or subgroups in the the training or testing dataset. The user can there-
fore focus their attention on the explanation built from a restricted input Figure 4.7: Examples
|     |     |     | 2021 | of the filter/focus | in- |
| --- | --- | --- | ---- | ------------------- | --- |
space. Theexplanationinterfacepresentedin[Jacobsetal., ]isanex-
ampleofaFilter/focusinteractiontechniquewhereusers(doctors)canfil- teraction taken from
2019]
|     |     |     |     | [Hohman et al., |     |
| --- | --- | --- | --- | --------------- | --- |
ter explanations based on the presence of a specific symptom. In [Cheng
|     |     |     |     | (top) and [Ming | et al., |
| --- | --- | --- | --- | --------------- | ------- |
2019
et al., ], users can create and delete subgroups in the model’s input 2019](bottom).
data to see the corresponding explanations for each subgroup. VBridge
|     | 2022 |     | 2020 |     |     |
| --- | ---- | --- | ---- | --- | --- |
[Cheng et al., ] and ExplainExplore [Collaris and van Wijk, ]
providetheabilityforuserstoselectasubsetoffeaturestobeusedinan
explanation. We also put in the Filter/focus class sorting functions, such
2019
as the one in Gamut [Hohman et al., ] which lets the user sort input
| features according | to several feature | metrics. |     |     |     |
| ------------------ | ------------------ | -------- | --- | --- | --- |
Mutate
i.e.
Interactive explanations can allow the user to "mutate" causes, to
test their hypotheses by simulating or comparing different situations.
The resulting explanations are cumulatively selective and contrastive.
4.8:
|     |     |     |     | Figure Examples | of       |
| --- | --- | --- | --- | --------------- | -------- |
|     |     |     |     | the reconfigure | interac- |
Reconfigure. This category includes a set of interactions that offer the
|     |     |     |     | tion taken from | [Ming |
| --- | --- | --- | --- | --------------- | ----- |
possibility to modify the parameters of the AI model such as the dataset, et al., 2019] (top) and
the model type or the model parameters in order to observe changes on [Collaris and van Wijk,
2020](bottom).

128 the explanation paradox and the human centric path
-
the explanation. Users may want to evaluate the impact of these factors
on the model’s prediction and corresponding explanation to make sense
of how the model works. This is especially true when explainability is
2020
used to assess the fairness of the model such as in [Yan et al., ] or
2019 2020
[Lee et al., ]. The Silva explanation interface [Yan et al., ], simi-
360 2019
larly to IBM’s AIF tool [Bellamy et al., ], allows the user to mod-
ify dataset attributes and sensitive inputs to see how it affects specified
fairness measures. Various explanation components, including causal
graphs and measures of feature importance, change based on the user’s
chosen dataset settings.
Simulate (inputs). Interactive explanations can be useful for users to
test how changes in inputs affects local explanations and the outcome of
the model. Understanding of a model then comes not only from static
information about the AI algorithm, but also from the learning expe- Figure 4.9: Examples of
rience provided by repeated simulations of the model. Interactions in the simulate interaction
taken from [Ross et al.,
the Simulate category refer to mutations of the inputs of the AI model.
2021] (top) and [Cheng
18 47
Many articles in our corpus ( / ) have integrated this interactive fea- etal.,2019](bottom).
ture, reflecting an appreciation of the XAI community for "learning by
2004
doing" [Roussou, ]. The simulation functionality is usually activated
by sliders or drop-down lists and gives the user a local understanding of
2021
the model’s behavior. Examples can be found in [Liu et al., , Morri-
2018 2022 2021
son et al., , Ahn, Yongsu et al., , Sevastjanova et al., ].
Compare.
This category gathers interaction techniques that are used to compare
1 2
either ( ) explanations for different inputs or group of inputs or ( ) ex-
planations for different predictions.
In the first case, the user can select the inputs or input groups to com-
pare so as to analyze differences in the explanation. Connections, simi- Figure 4.10: Example of
larities and differences between the selected inputs or outcomes can be the compare interaction
highlighted in the comparative explanations. Compare interaction meth- taken from [Hohman
etal.,2019].
ods would often use parallel coordinates graphs to ease the compari-
2019
son between explanations. Hohman et al. [ ] give an example of an
explanation view in which the user can see local explanations for two
inputs they selected for analysis. The second case occurs when the AI
model predicts several possible outcomes with varying levels of confi-
dence. Theuserthenusuallywantstocomparetheexplanationsforeach
2022
of the probable outcomes to assess their likelihood. Dodge et al. [ ]’s
2020
and Jin et al. [ ]’s systems are examples of this type of outcome com-
2022
parison. In [Dodge et al., ], the user can tap on a game board (rep-
resenting a game situation) to see its corresponding chance of winning
and how it compares to the chance of winning from other game boards.
2020
In CarePre [Jin et al., ], doctors are users, and can explore in detail
the records of a patient, as well as compare it with similar patients; their
focus is on sequences of "events" (a patient enters the medical facility, a
scan is performed, etc.). This allows the user to detect similar paths, and
adapt treatment accordingly. This interaction class is inspired from Yi et
al.’s "connect" category.

towards human like explanations the promise of interactivity 129
" - " :
Dialogue with
Interactivity can support the user in engaging in a dialogue-like struc-
ture. InformationabouttheAImodelisthengivenprogressivelyand/or
iteratively. The user could ask the system a question or give it feedback.
These "dialogic" explanations are in line with the properties expressed
by Miller for human-like explanations. However, there may be different
degrees in which explanations are truly social, depending on the range
of questions a system can actually answer.
Figure 4.11: Example
Progress. The Progress interaction style is inspired by Sim’s "linear in- of the progress interac-
tion taken from [Mel-
teractivity"throughwhich"theuserisabletomoveforwardorbackward
siónetal.,2021].
in a pre-determined sequence of instruction materials". The explanation
is designed in several steps, and the user can click "next" or "previous"
to navigate through the explanation displays. It is generally progressive,
withbasicinformationprovidedinthefirstfewpagesandmorein-depth
information presented in subsequent sections. This style of interactivity
1997
isreactive[Sims, ]anddoesnotprovidespecificfeedbacktotheuser
but instead lets them walk through the explanation at their own pace.
The user can only control when the explanation is provided.
The Progress interaction style can be seen as the lowest level of "dia-
logic" explanations. It does not enable the user to ask nor answer ques-
1975
tions but it follows some of the rules of a conversation [Grice, ] by
providing sparse information progressively (maxim of quantity), and by
predefining user questions that need to appear in the explanation guide
(maxim of quality). The "next" and "previous" commands can be con-
sidered as the users’ options to punctuate the conversation (compared to
saying "ok tell me more" or "wait, what did you say").
Figure 4.12: Examples
Answer. While information flow in interactive XAI systems goes pri-
of the answer interac-
marily from the machine to the user, like in Infovis systems [Yi et al.,
tion taken from [Mel-
2007 ], itcan alsobe reversed, withusers providingthe systemwith feed- sión et al., 2021] (top)
back, corrections or information about the state of their mental models. and [Guo et al., 2022]
Theseinteractionscanservetoincreaseuserscognitiveengagement(and (bottom).
2 1979
activate their "System " [Kahneman and Tversky, ]) by challenging
2021
users. For example, in [Melsión et al., ], users (in this case children)
are asked to click on the part of the image that they think had the most
impactonthealgorithm’sprediction. Thisinteractiontypecanalsoserve
to improve the AI system by building on human feedback. Examples are
2022 2019
[Jia et al., , Shi et al., ] in which users are asked to improve the
semantic meaning of the concepts learned by the algorithms, [Guo et al.,
2022 2021
, Cheng et al., ] in which users can create or edit explanations—
2021
such as adding a new rule or correcting one, [Virgolin et al., ] in
which users can indicate to the system their personal preferences about
2021 2021
model interpretability, or [Hepenstal et al., , Ghazimatin et al., ,
2021 2020
Ghai et al., , Spinner et al., ].
Ask. In[Miller, 2019 ],theultimatelevelofinteractionisaconversation
where the user can ask the AI system anything they want. We can there-
fore view the Ask interactivity as the higher end of the interactivity scale Figure 4.13: Example of
for XAI. The conversational XAI research line has made some progress theaskinteractiontaken
from [Melsión et al.,
2021].

130 the explanation paradox and the human centric path
-
in achieving such interactivity. For instance, [Hernandez-Bocanegra and
2021 2021
Ziegler, , Hepenstal et al., ] present logical dialogue maps to
deliver explanations that answer users’ questions. The challenge is to
cover as wide a range of questions as possible. Note that this "dialogic"
interaction between user and machine does not necessarily have to take
2019
placethroughnaturallanguage. AsMillerstated[Miller, ],wecould
imagine an XAI system that answers the user’s questions with images
or other communication means. An illustration of this can be found in
2021
[Khurana et al., ], where the user submits a query such as "create a
graph showing the predicted trend" and the XAI system responds with
the desired graph.
Figure 4.14: "Interactive
XAIhelpsusers..."
Illustrationofthetaxon-
omyofinteractioninex-
4.4.2 Context, content and form of interactive explanations
plainabilitywithscreen-
shotsfromthecorpus.
This section present a qualitative analysis based on our conceptual
2
matrix to address our RQ .
Context. The work in our corpus is well distributed across the differ-
ent domain categories constituted by [Lai et al., 2021 ] (cf. Figures 4 . 16
417 32 48
and . ). Notably, the corpus reflects a large number of studies ( /
papers) implemented in real-world applications rather than in artificial
or generic domains. Healthcare stands out as one of the most studied
domains in the corpus.
2022 2019
Some work [Bove et al., , Cheng et al., ] expressed concern
that too few studies focused on making explanations understandable to
novices and that most current XAI techniques were only comprehensible
2019
to AI-educated users. Cheng et al. [ ] also argues that the majority
of studies providing explanations to novices have been conducted in the
context of generic tasks [Lai et al., 2021 ], i.e. computer science problems,

towards human like explanations the promise of interactivity 131
|     |     |     | "   | -   | "   |     |     | :   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
and are therefore not generalizable to real-world applications. In con-
trast to the first concern, we found that the majority of articles included
27 48
in the corpus ( / ) were aimed at a general audience of non-expert
users. This at least reflects an awareness of the field to design explana-
tions with this user group in mind. In addition, 15 / 27 of these studies
are in real-world application areas, including areas that may be consid-
ered sensitive— 4 in legal and civil, 2 in healthcare, and 3 in business
and finance. However, it is possible that the empirical studies included
in our corpus targeted non-expert users for practical reasons, such as to
solicit platform workers like those on Amazon MTurk [Guo et al., 2022 ,
|     |     |     |     |     | 2021 |     |     | 2021 |
| --- | --- | --- | --- | --- | ---- | --- | --- | ---- |
Hernandez-Bocanegra and Ziegler, , Ross et al., , Ghai et al.,
| 2021 |         |         | 2019       |     |         | 2015      |     | 2016              |
| ---- | ------- | ------- | ---------- | --- | ------- | --------- | --- | ----------------- |
|      | , Cheng | et al., | , Schaffer |     | et al., | , Ribeiro |     | et al., , Wilkin- |
son et al., 2021 ]. Nevertheless, some of these studies are primarily aimed
at making the XAI systems more transparent and more accessible to a
non-expert audience [Tsai et al., 2021 , Springer and Whittaker, 2019 , Yan
|     | 2020   |           |     | 2021 |        |           | 2021 |     |
| --- | ------ | --------- | --- | ---- | ------ | --------- | ---- | --- |
| et  | al., , | Szymanski | et  | al., | , Anik | and Bunt, |      | ].  |
Regarding the data type used in our corpus, tabular and text data are
79
predominant ( % of the studied papers). This points to an opportunity
for the explainability field to empirically study interactive explanations
usingaudio(onlyonepaperdiscussedaudiodata[AnikandBunt, 2021 ]),
| images, | and | video | data. |     |     |     |     |     |
| ------- | --- | ----- | ----- | --- | --- | --- | --- | --- |
Content. The interactive explanations in the corpus focused heavily
37
on the "why?" user question recurring times, and which can be an-
swered by local feature explanations, the most commonly used explana-
|                        |     |     |     | 26 48 |                  |     |     | 415          |
| ---------------------- | --- | --- | --- | ----- | ---------------- | --- | --- | ------------ |
| tionmethodinthecorpus( |     |     |     | / ).  | WecanseeinFigure |     |     | . (Right)how |
some interaction techniques were favored for specific types of user ques-
tion. For example, quite logically, explanations addressing "what is the
difference with?" were implemented with Compare, but also frequently
with Filter/focus interactions. Context and raw data can be elaborated
through Clarify interaction. "How to?" and "What if?" were facilitated
through Simulate interactions. Model limitations were rarely presented
in the studies (only twice). But perhaps a bigger opportunity for inter-
active explanations is the small numbers of papers addressing "how to?"
2021
| questions. | Oneexampleis[Rossetal., |     |     |     |     | ]inwhichtheusercanchange |     |     |
| ---------- | ----------------------- | --- | --- | --- | --- | ------------------------ | --- | --- |
input"conceptfeatures"toseetheadjustedoutputinrealtimeandbetter
understand the meaning of each "concept feature". However, we found
only two studies enabling direct interventions on the model output [Jin
et al., 2020 , Dodge et al., 2022 ]. Such interventions (which would fall in
|     |     |     |     | 4 2 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
the Simulate category cf. Table . ) could help the user characterize what
kinds of contexts and situations are emblematic of a particular outcome,
thereby addressing "how to?" questions. In addition, concept-based ex-
planations, which are considered promising in the field for their human
comprehensibility, were rarely used in the corpus [Kim et al., 2018 , Koh
2020
| et  | al., ]. |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Communication. The most used interaction techniques were Clarify
and Simulate. These were frequently combined with compare, Filter/focus
and Arrange as illustrated in Figure 4 . 15 (Left). The techniques Progress

| 132 the | explanation | paradox | and the | human centric path |     |     |
| ------- | ----------- | ------- | ------- | ------------------ | --- | --- |
-
andAskwereusedinonlythreeandfourstudiesrespectively,illustrating Figure 4.15: Left: Fre-
|     |     |     |     |     | quency of | the inter- |
| --- | --- | --- | --- | --- | --------- | ---------- |
a trend in the field of interactive XAI towards complex, Infovis-type XAI
|     |     |     |     |     | action categories | used |
| --- | --- | --- | --- | --- | ----------------- | ---- |
interfaces rather than simpler step-by-step or dialog box interfaces. The
|     | 415 |     |     |     | in the corpus | and fre- |
| --- | --- | --- | --- | --- | ------------- | -------- |
matrix in Figure . (Left)shows this clear cut between the "Select" and
|     |     |     |     |     | quency of | their combi- |
| --- | --- | --- | --- | --- | --------- | ------------ |
"Mutate" interaction groups on the one hand, and the "Dialogue with" nations ; Middle: Per-
group on the other. The interactions techniques in the first two groups centage of studies using
|     |     |     |     |     | an explanation | repre- |
| --- | --- | --- | --- | --- | -------------- | ------ |
are frequently combined with each other, while the interaction styles in
sentationperinteraction
the latter group are less frequently used. In addition, these more "so-
|     |     |     |     |     | category; | Right: Per- |
| --- | --- | --- | --- | --- | --------- | ----------- |
cial" interactions were rarely combined with other interactions from the
centageofstudiesfocus-
"Mutate" or "Select" levels. In particular, Progress was never used in com- ing on a type of user
bination with other "Mutate" or "Select" interaction categories. It would question per interaction
category/
be interesting for future research to explore combining these as a way
to take advantage of the social nature of "progress" explanations while
| giving | greater control | to the user | with selections | and mutations. |     |     |
| ------ | --------------- | ----------- | --------------- | -------------- | --- | --- |
Therepresentationsusedfortheinteractiveexplanationswereprimar-
415
ily charts and texts. As shown in Figure . (Middle), tables were use-
ful to support Filter/focus and Compare interactions. Textual explanations
often came with Clarify interactions. Rules, although not appearing fre-
quentlyinthecorpus( 5 times),whereusedtosupportClarifyandAnswer
interactions. Indeed, rules are easy objects for users to modify, create or
2022 2021
delete, as exemplified in [Guo et al., , Hepenstal et al., , Ming
| et al., 2019 | ].  |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- |

towards human like explanations the promise of interactivity 133
|     | "   | -   | "   |         | :   |     |         |     |
| --- | --- | --- | --- | ------- | --- | --- | ------- | --- |
|     |     |     |     | CONTEXT |     |     | CONTENT |     |
PDP & sisylanA ytivitisneS
|                    |       |                   | ecnaniF & ssenisuB                      |                                         |                                  | ecnedifnoC ledoM  | ?htiw .ffid eht s'tahW .pmI erutaeF lacoL             |                                                           |
| ------------------ | ----- | ----------------- | --------------------------------------- | --------------------------------------- | -------------------------------- | ----------------- | ----------------------------------------------------- | --------------------------------------------------------- |
|                    |       |                   |                                         | strepxE niamoD                          | egaugnal larutaN atad laitneuqeS | snoitatimiL ledoM | dohtem IAX seluR noisiceD desab-elpmaxE ksam ycneilaS | desab-tpecnoC ledom etagorruS lautcafretnuoC zO fo draziW |
|                    |       | niamoD cviC & waL | erachtlaeH noitacudE erusieL laicifitrA | cireneG ecneiduA strepxE IA trepxe noN  | epyt ataD ralubaT sucof IAX      | ataD waR          | ?ton yhW ?ot woH ?fi tahW txetnoC                     |                                                           |
|                    |       |                   |                                         | rehtO rehtO                             | egamI oediV oiduA                | tuptuO ?woH       | ?yhW                                                  | rehtO                                                     |
| Year Title Authors | Venue |                   |                                         |                                         |                                  |                   |                                                       |                                                           |
2021 To Trust or to ThiBnukç: iCncoag neitti vael. ForAcCinMg  HFCuI nJcot.ions Can Reducxe Overreliancex on AI xin AI-Assisted Decision-xMakxing x
2021 Explainable ActivGeh Laei aertn ainl.g (XAL)A: CTMow HaCrId J oA.I Explanations as Ixnterfaces foxr Machine Teaxchers x x
2019 Procedural JusticLee ein e At laglo.rithmic FAaCiMrn HeCssI :J oL.everaging Transxparency and Oxutcome Contxrol for Fair Axlgorithmxic Mediationx x
Understanding thLeiu E effte acl.t of Out-oAf-CDMi sHtrCibI uJoti.on Exxamples and Interactive Exxplanations onx Hxuman-AI Decisionx Makingx x x
2021
2020 CarePre: An InteJlliigne entt  aCl.linical DeAcCisMio HnE AAsLsTiHstancex System x x x x x x xx
2021 Why or Why Not?W Tilkhien sEofnfe ectt  aolf. JuAsCtMifi cTa Itniof. nS .Styles on Chaxtbot Recommenxdations x xx x
2022 Tribe or Not? CritAichanl  Ients aple.ction ofA GCMro uTIpIS Differenxces Using TribalGramx x x xx x x xx x
2021 Developing ConvHeerspaetniosntaall  eAtg aeln.tsA CfoMr  TUIIsSe in Crimxinal Investigations x x x xx x x x x
Learn, Generate,K Rima nekt ,a El.xplain: AA CCMa sTeIIS Study of Visual Explanxation by Gexnerative Mxachine Learnxing x x x x x
2021
2018 Visualizing UbiquMitoourrsislyo nS eent sael.d MAeCaMs uTrIeISs of Motorx Ability in Multiple Sxclerosis: Reflexctionxs on Comxmunxicatixng Machixne Lxearning in Practice x
2021 QuestionComb: AS eGvaamstjiaficnaotvioan e At apAlp.CrMo aTcIISh for the Visual xExplanation oxf Linguistic Phenomexna throxugxh Interaxctive Labelingx x x
2020 Progressive DiscSlopsruinreg:e Wr ahnedn ,W WhhiAttyCa,M kae nTrIdIS How Do Uxsers Want Algorithmic xTransparency Infxormation? x x
2021 Nudging throughN Fariicsetiohn e: tA anl. ApprBoEaScCh for Calibratxing Trust in Explainxable AI x xx x x
Data-Centric ExpAlannika ationnds B: uEnxtplaiCnHinIg Training Dxata of Machine Learninxg Sxystemxs to Pxroxmote Traxnsparency x x
2021
2019 Explaining DecisCiohne-Mnga keitn agl .AlgorCithHmI s through UI: Straxtegies to Help Nonx-Expert Stakehxolders x x x
2019 Gamut: A DesignH Porhombea nto e Ut anld.ersCtHaInd How Data Scienxtists Understandx Machine Learnixng Modelxs xx xx x x
2021 Designing AI for TJraucsot basn de tC aol.llaboCraHtIion in Time-Coxnstrained Medical xDecisions: A Socioxtechnical Lens xxx xxx x x
2021 Evaluating the InRteorpssre etat baill.ity of GeCnHeIrative Models by Interactivxe Reconstruxctionx xx x x
Exploring and ProTmsaoi teint ga lD.iagnostCicH ITransparency xand Explainability in Onlxine Symptom xCheckersx x x x x x
2021
2019 Designing TheoryW-Danrivge ent  Uals.er-CeCnHtrIic Explainable xAI x x x xx x xx x
2020 Silva: InteractivelYy aAns seet sasli.ng MachCiHnIe Learning Fxairness Using Causalityxx x x xx x x
2021 Conversational RHeevirenwan-Bdaesze-Bdo EcxapCnlUaeIngarati oannsd  fZoire Rgelecrommexnder Systems: Exxploring Usersx' Query Bxehxavior x xx x
2021 Model Learning wViitrhg oPlienr seot naal.lizedG InEtCeCrpOretability Estimxation (ML-PIE) x x x x
|     |     |     | x   | x   | x   | xx  | x x x |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- |
2020 SIMFIC: An ExplaPinoallebyle e Bt oaol.k SeaICrcHhM CSompanion
2021 Using ExplainabiMlitye ltsoió Hne elpt  aCl.hildreIDnC Understand Gendexr Bias in AI x x x x
2019 DeepClue: VisuaSl hIni teetr parle.tation ofI ETEeEx Tt- BKDaEsed Deep Sxtock Predictionx x x x x x x
2021 DECE: Decision CEhxepnlogre er tw ailt.h CouIEnEtEe TrfVaCcGtual Explaxnaxtioxns for xMachinxe xLearning Modelsx x xx xxx x x
2022 VBridge: ConnecCtihnegn tgh ee tD aol.ts BetIEwEeEe TnV CFGeatures axnd Data to Explainx Healthcare Modelsx xx xx xxx x x
Towards Visual EJxiap laeitn aalb.le ActiveIE LEeE aTrVnCinGg for Zero-Shot Clasxsificationx x x xx x
2022
2019 RetainVis: VisualK Awnoanly teict sa lw.ith IntIeEErpEr eTVtaCbGle and Inxteractive Recurrentx Nxeural Networks on Elxectroxnic Medicalx Rxecordxsxx x
2019 RuleMatrix: VisuaMliziningg e at nadl. UndersIEtEaEn dTVinCgG Classifiexrs with Rules xx x x xxx x x xx
2020 explAIner: A VisuSapl Ainnnaelry teict sa lF.ramIeEEwEo TrkVC fGor Interactive and Expxlainable Mxachine Lxearning x xx x x x x
2022 ContextualizationB aonved  eEtx apll.oration IUoIf Local Feature Imxportance Explanationxs to Improve Uxnderstanding and Saxtisfactixon of Nonx-Expxert Users
| I Think I Get YouCr Phrooinmt,ik A eI!t  Tahl.e IlluIUsIion of Explanatoryx Depth in Explainablex AI |     |     |     |     | x   |     | x x x x |     |
| ---------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- |
2021
2022 How Do People DRaondkg eM eutl taipl.le MuIUtaInt Agents? x x x x x x
2019 What Can AI Do Ffeorn gM eet? a El.valuatinIUgI Machine Learning Interpxretations xin Coxoperative Playx x x xx
2022 Building Trust in IGntueora ectt iavle. MachinIUeI Learning via User Contrxibuted Interprextable Rules x x x
2021 Anchoring Bias ANffoeucrtasn Mi eetn atal.l MoIUdIel Formation and User Reliaxnce in Explxainable AxI Systems x x x x
2021 XAlgo: A Design RPerobbaen aolf  eEt xapl.lainiInUgI Algorithms' Internal Statxes via Quxestioxn-Answering xx x x xxx x x xx
2015 Getting the MessSacghea?f fAe rS ettu adly. of IEUIxplanation Interfaces for Microxblog Dxata Analysis x xx x x
2021 From PhilosophyS too vInratenrofa acneds :V AitnaIl UiEIxplanatory Methoxd and a Tool Inspired xby Achinstein'xs Theory of Explanatixon x x x x
2022 Intuitively AssessSinugr eMshL  eMt oadl.el ReIlUiaIbility through Exxample-Based Expxlanations and Editing Mxodel Inputs xxx x x
2021 Visual, Textual orS Hzyymbraidn:s Tkhi ee tE aflf.eIcUtI of User Expertise on Difxferent Explaxnaxtions x x x x
2020 Bot-Detective: AKn oEuxvpelalain eatb alel. TwMittEeDr EBSot Detectxion Service with Crowdsoxurcing Functionaxlities x xx x x
2020 ExplainExplore: VCisoullaalr iEs xept loarl.ationP oafc MificaVcishine Learning Explanxations x x x x x x
2016 Why Should I TruRsitb Yeoirou ?e:t  Eaxl.plainiSnIgG KthDeD Predictions of Any Cxlassifier x x x x x
2021 ChatrEx: DesigniKnhgu Eraxnpala ienta abll.e CVhLa/HtbCoCt Interfaces for Enhancingx Usexfulness, Transparencxy, and Trust x x
2021 ELIXIR: Learning Gfrhoamz iUmsaetirn F eete adlb.WacWkW on Explanations To xImprove Recommxender Modelxs x x
  612 6 5 4 8 8 2 171226 1 6 3 12612 5 23 8 2 71337 9 422 917 26 6 3 8 6 2 3 5 614
|     |     |     |     |     |     |     | Figure 4.16:  | The first   |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- |
|     |     |     |     |     |     |     | part of the   | concept ma- |
|     |     |     |     |     |     |     | trix [Webster | and Wat-    |
son,2002],reportingthe
|     |     |     |     |     |     |     | explanation  | context and   |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- |
|     |     |     |     |     |     |     | content.     | The design of |
|     |     |     |     |     |     |     | this concept | matrix was    |
inspiredfrom[Baeetal.,
2022].

| 134 | the | explanation | paradox | and the | human | centric |     | path |     |     |     |
| --- | --- | ----------- | ------- | ------- | ----- | ------- | --- | ---- | --- | --- | --- |
-
|     |     |     |     | COMMUNICATION |     |     |     |     | EVALUATION |     |     |
| --- | --- | --- | --- | ------------- | --- | --- | --- | --- | ---------- | --- | --- |
ytixelpmoc/htgnel deviecreP
|     |      |               |       |                                          |                 |                   | erutcurts atad eht nO   |                     | esu fo esaE / ytilibasU ssenlufesU deviecreP | ksat ta ecnamrofreP | ycnerapsnart deviecreP                                  |
| --- | ---- | ------------- | ----- | ---------------------------------------- | --------------- | ----------------- | ----------------------- | ------------------- | -------------------------------------------- | ------------------- | ------------------------------------------------------- |
|     |      |               |       |                                          | noitatneserpeR  |                   |                         | noitanalpxe citatS  |                                              | tsurT evitcejbuS    | ycarucca detciderP lortnoc deviecreP ssenriaf deviecreP |
|     |      |               |       | ytivitcaretnI sucof / retliF erugifnoceR |                 |                   | enilesaB noitanalpxe oN | enilesab oN erusaeM | gnidnatsrednU                                | daol evitingoC      |                                                         |
|     |      |               |       | yfiralC egnarrA  etalumiS erapmoC        | ssergorP rewsnA | trahC elbaT seluR | rehtO                   | rehtO               |                                              | gninraeL            | tsurtrevO rehtO                                         |
|     |      |               |       |                                          | ksA             | txeT              |                         |                     | emiT                                         |                     |                                                         |
|     | Year | Title Authors | Venue |                                          |                 |                   |                         |                     |                                              |                     |                                                         |
2021 To Trust or to ThiBnukç: iCncoag neitti vael. ForAcCinMg  HFCuI nJcot.ions Can Reduce Overrelianxce oxn AI in AI-Assixsted Decxision-Mxakxing xx x
2021 Explainable ActivGeh Laei aertn ainl.g (XAL)A: CTMow HaCrId J oA.I Explanations as Intexrfacesx for Machine Teaxcherxs x xxx
2019 Procedural JusticLee ein e At laglo.rithmic FAaCiMrn HeCssI :J oL.everaging Txransparency and Oxutcome Controlx foxr Fair Axlgorithmic Mediation x
2021 Understanding thLeiu E effte acl.t of Out-oAf-CDMi sHtrCibI uJoti.on Examples xand Interactivex Explanaxtions onx Hxumxan-AI Dxecision Makingx x
|     | 2020 | CarePre: An InteJlliigne entt  aCl.linical DeAcCisMio HnE AAsLsTiHstanxce Systemx |     |     |     | x x | xx  | x   | xx  |     |     |
| --- | ---- | --------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2021 Why or Why Not?W Tilkhien sEofnfe ectt  aolf. JuAsCtMifi cTa Itniof. nS .Styles on Chatbot Rexcommendaxtions x x xx x x x
|     | 2022 | Tribe or Not? CritAichanl  Ients aple.ction ofA GCMro uTIpIS Differencexs xUsinxg TxribalGramx |     |     |     | x   |     | x   | xx  |     |     |
| --- | ---- | ---------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2021 Developing ConvHeerspaetniosntaall  eAtg aeln.tsA CfoMr  TUIIsSe in Crimxinxal Invexstigatioxnsx xx x x x x
2021 Learn, Generate,K Rima nekt ,a El.xplain: AA CCMa sTeIIS Study of Visuaxl Explanation by Generativxe Machxine Lxearninxg x xx x x
2018 Visualizing UbiquMitoourrsislyo nS eent sael.d MAeCaMs uTrIeISs of Moxtor Ability xin xMultiple Sclxerosis: Reflections on Cxommxunxicating Machixne Learning in Practice
2021 QuestionComb: AS eGvaamstjiaficnaotvioan e At apAlp.CrMo aTcIISh for thex Visuxal Explanatixon of Linguixstixc Phenomena thxrougxh Ixntexractive Labxeling
2020 Progressive DiscSlopsruinreg:e Wr ahnedn ,W WhhiAttyCa,M kae nTrIdIS How Dxo Users Want Algorithmic Transpxarency Inforxmation?x x xx x x
2021 Nudging throughN Fariicsetiohn e: tA anl. ApprBoEaScCh for Calibrating Trust in Exxplainabxle AI x x x
2021 Data-Centric ExpAlannika ationnds B: uEnxtplaiCnHinIg Training Dxata of Machine Learning Syxstems to Promote Txransxparexncy x x x
2019 Explaining DecisCiohne-Mnga keitn agl .AlgorCithHmI s through UI: Strategxies to Help Noxn-Expert Stakehxoxlders x xx
|     | 2019 | Gamut: A DesignH Porhombea nto e Ut anld.ersCtHaInd How Datxa Sxcxientists xUnderstandx Mxacxhine Learning Modxelsxxx |     |     |     |     |     |     |     |     |     |
| --- | ---- | --------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2021 Designing AI for TJraucsot basn de tC aol.llaboCraHtIion in Time-Consxtrainedx Medical Decixsions: A Sociotechnicxal Lexns x
2021 Evaluating the InRteorpssre etat baill.ity of GeCnHeIrative Models by Intexractive Reconstrucxtionx x x xx
2021 Exploring and ProTmsaoi teint ga lD.iagnostCicH ITransparency and Explainabilityx in Onlxine Symptom xCheckers x x xx x x
2019 Designing TheoryW-Danrivge ent  Uals.er-CeCnHtrIic Explainabxle AI x x x x x
2020 Silva: InteractivelYy aAns seet sasli.ng MachCiHnIe Learning Fairnessx Uxsing Causalityxx xx x xx x
2021 Conversational RHeevirenwan-Bdaesze-Bdo EcxapCnlUaeIngarati oannsd  fZoire Rgxelecrommender Systxems: Expxloring Users' Queryx Behavior x x x
|     | 2021 | Model Learning wViitrhg oPlienr seot naal.lizedG InEtCeCrpOretability Estimation (ML-PxIE) |     |     |     |     | x   | x   | x   |     |     |
| --- | ---- | ------------------------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2020 SIMFIC: An ExplaPinoallebyle e Bt oaol.k SeaICrcHhM CSompanion x x x x x
2021 Using ExplainabiMlitye ltsoió Hne elpt  aCl.hildreIDnC Understand Gender Bias ixn AxI x x xx
2019 DeepClue: VisuaSl hIni teetr parle.tation ofI ETEeEx Tt- BKDaEsed Deexp Sxtock Predicxtion x x x x x
|     | 2021 | DECE: Decision CEhxepnlogre er tw ailt.h CouIEnEtEe TrfVaCcGtual Exxplaxnaxtionxs fxor Machine xLearning Models |     |     |     |     |     | x   | x   |     |     |
| --- | ---- | --------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 2022 | VBridge: ConnecCtihnegn tgh ee tD aol.ts BetIEwEeEe TnV CFGeaturesx axndx Datxa txo Explain Hxealthcare Models  |     |     |     |     |     | x   | x   |     |     |
2022 Towards Visual EJxiap laeitn aalb.le ActiveIE LEeE aTrVnCinGg for Zero-Shot Classifixcationx x x x x x
2019 RetainVis: VisualK Awnoanly teict sa lw.ith IntIeEErpEr eTVtaCbGle andx Interxactivxe Rxecurrent Nxeuxral Netwoxrks on Elecxtronicx Mexdical Records
|     | 2019 | RuleMatrix: VisuaMliziningg e at nadl. UndersIEtEaEn dTVinCgG Classixfiexrs xwixth Ruxlesx                           |     |     |     | x x |     | x   | x x |     |     |
| --- | ---- | -------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 2020 | explAIner: A VisuSapl Ainnnaelry teict sa lF.ramIeEEwEo TrkVC fGor Interaxcxtive axnd Explaxinable Machxine Learning |     |     |     |     |     | x   | xx  |     |     |
2022 ContextualizationB aonved  eEtx apll.oration IUoIf Local Featuxre Importaxnce Explanatxions to Improve Unxderstandinxg anxd Satisfaction of Non-Expert Users
2021 I Think I Get YouCr Phrooinmt,ik A eI!t  Tahl.e IlluIUsIion of Explanxatory Depxth in Explainablex AI x x x x
|     |      |                                                           |     | xx x |     | x   |     | x   | x   | x   |     |
| --- | ---- | --------------------------------------------------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
|     | 2022 | How Do People DRaondkg eM eutl taipl.le MuIUtaInt Agents? |     |      |     |     |     |     |     |     |     |
What Can AI Do Ffeorn gM eet? a El.valuatinIUgI Machine Learnxing Interpretations in Cooxperatxive Play x x
2019
Building Trust in IGntueora ectt iavle. MachinIUeI Learning via User Contributexd Interpretablex Rxules x x x x
2022
Anchoring Bias ANffoeucrtasn Mi eetn atal.l MoIUdIel Formation xand User Reliance in Explainable AxI Sysxtemsx x x x x
2021
2021 XAlgo: A Design RPerobbaen aolf  eEt xapl.lainiInUgI Algorithms' Internal Statesx via Qxuestion-Answexring x xxx x x
2015 Getting the MessSacghea?f fAe rS ettu adly. of IEUIxplanation Interfacxes for Mxicroblog Datax Analyxsis x x x
2021 From PhilosophyS too vInratenrofa acneds :V AitnaIl UiEIxplanatory Mxethod and a Tool Inspired byx Achinstein's Txheory of xExxplanatixon
2022 Intuitively AssessSinugr eMshL  eMt oadl.el ReIlUiaIbility through Exxamplex-Bxased Explanxations anxd Editing Mxodel Inpxuts x
2021 Visual, Textual orS Hzyymbraidn:s Tkhi ee tE aflf.eIcUtI of User Expertise on Dxifferent Explaxnatioxns x xx xx
|     | 2020 | Bot-Detective: AKn oEuxvpelalain eatb alel. TwMittEeDr EBSot Detection Servicxe with Crowdsourcxing Functionalitiesx |     |     |     |     |     |     | xx  |     |     |
| --- | ---- | -------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 2020 | ExplainExplore: VCisoullaalr iEs xept loarl.ationP oafc MificaVcishine Lexarxninxg xExplaxnations                    |     |     |     | xx  |     | x   | x   |     |     |
2016 Why Should I TruRsitb Yeoirou ?e:t  Eaxl.plainiSnIgG KthDeD Predictions of Any Classxifier x x x x x
2021 ChatrEx: DesigniKnhgu Eraxnpala ienta abll.e CVhLa/HtbCoCt Interfaces for Enhancxing Usefulnessx, Transparexncxy, and Trustxx x
2021 ELIXIR: Learning Gfrhoamz iUmsaetirn F eete adlb.WacWkW on Explanations To Improvxe Recommenderx Modelsx x
|     |     |     |     | 201211 61613 | 314 4 | 23 917 | 512 8 14 | 91619 | 351417 3 | 712 521 2 | 3 2 2 4 4 5 |
| --- | --- | --- | --- | ------------ | ----- | ------ | -------- | ----- | -------- | --------- | ----------- |

|     |     |     |     |     |     |     |     |     |     | Figure       | 4.17: The sec- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- |
|     |     |     |     |     |     |     |     |     |     | ond part     | of the con-    |
|     |     |     |     |     |     |     |     |     |     | cept matrix, | reporting      |
theexplanationcommu-
nicationandevaluation.

towards human like explanations the promise of interactivity 135
|     |       |            |     | "           | -   | "            |     | :   |     |
| --- | ----- | ---------- | --- | ----------- | --- | ------------ | --- | --- | --- |
|     | 4.4.3 | Evaluating |     | interactive |     | explanations |     |     |     |
To address our RQ 4 , we report below how XAI researchers in our cor-
pushavebeenmeasuringexplanationsandexplainableAIsystemsbased
onhuman-groundedevaluations[Doshi-VelezandKim, 2017 ]. Belowwe
providebriefdescriptionsofthemeasuresandhighlighttrendsandchal-
| lenges | in  | evaluating | interactive |     | explanations. |     |     |     |     |
| ------ | --- | ---------- | ----------- | --- | ------------- | --- | --- | --- | --- |
Few controlled experiments. Few empirical studies supported a cross-
sectional analysis of results on interactive XAI by using a static explana-
|                  |     |     |             |     | 20  | 48                              |     |     |     |
| ---------------- | --- | --- | ----------- | --- | --- | ------------------------------- | --- | --- | --- |
| tionasabaseline. |     |     | Mostpapers( |     |     | / )didnotuseanycontrolcondition |     |     |     |
(cf. Figure 4 . 17 . Even if the measures in these articles are sometimes
2021
quantitative as in [Hernandez-Bocanegra and Ziegler, ] where the
authors measured different constructs (system efficiency, transparency...)
|     |     |     |     | 1 5 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on Likert scales from to points, these results are hard to interpret in
| comparison |     | with | the | rest of | the XAI | literature. |     |     |     |
| ---------- | --- | ---- | --- | ------- | ------- | ----------- | --- | --- | --- |
Nine of the 48 articles in our corpus compared interactive and static
explanations through between-subject experiments. These comparisons
were very informative for analyzing the added value of interactivity in
XAI.WeprovideinSection 44 . aqualitativeanalysisoftheaddedvalueof
interactive explanations based on this work. To a lesser extent, compar-
isons between interactive explanations and no explanation ( 13 / 48 items)
are also useful for understanding the benefit of interactive explanations.
44
WealsoleveragedthisbodyofworkinSection . . Othercontext-specific
comparisonsweremadebetweenaninteractiveexplanationandotherex-
|     |     |     |     |     | 2015 |     | 2022 |     | 2022 |
| --- | --- | --- | --- | --- | ---- | --- | ---- | --- | ---- |
planation types [Schaffer et al., , Guo et al., , Suresh et al., ,
|     |     |     | 2021 |     |     |     |     |     | 2020 |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---- |
Wilkinson et al., ], other interactive systems [Polley et al., , Yan
et al., 2020 ], other AI models [Ross et al., 2021 ], other interactivity types
|     |     | 2021 |     |     |     |     |     | 2022 |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | ---- | --- |
[Ghai et al., ] or random baselines [Jia et al., ], among others.
Some of these user-based evaluations were within-subject experiments
[Dodgeetal., 2022 ,SpringerandWhittaker, 2019 ,FengandBoyd-Graber,
2019
].
Much of the work that did not use a baseline provided valuable qual-
itative assessments instead. This research often employs usage scenario
(or "use cases") to study users’ reactions to XAI systems in realistic set-
tings [Kwon et al., 2019 , Ming et al., 2019 , Jia et al., 2022 , Cheng et al.,
2022
|     | ]. These | qualitative |     | insights |     | often focused | on  | capturing | the user’s |
| --- | -------- | ----------- | --- | -------- | --- | ------------- | --- | --------- | ---------- |
|     |          |             |     |          |     |               |     |           | 16 20      |
perceived ease of use and/or usefulness of the XAI system ( / pa-
pers).
19
A wide toolbox. We identified different metrics to evaluate XAI
systems with users from our corpus. Fourteen of them were used twice
or more: perceived usability, perceived usefulness, understanding, per-
ceived explanation length/quantity, time, trust, cognitive load, perfor-
mance at task, learning, predicted accuracy, perceived control, perceived
|     |     |     |     |     |     |     |     | 4   | 16 4 17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |
fairness, perceived transparency and reliance (cf. Figures . and . ).
Other measures were used such as perceived feedback quality and diffi-
culty[Guoetal., 2022 ],explanationpersuasivenessandsufficiency[Hernandez-
2021
Bocanegra and Ziegler, ], number of interactions (clicks, etc.) with
the explanations [Naiseh et al., 2021 a] and naturalness and humanness

| 136 | the | explanation |     |     | paradox | and | the human | centric | path |     |
| --- | --- | ----------- | --- | --- | ------- | --- | --------- | ------- | ---- | --- |
-
|     |     |     |     |     |     | 2021 | 443 |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
of the explanations [Rebanal et al., ]. Table . . provides the defini-
| tions | used | for | each | of these | metrics. |     |     |     |     |     |
| ----- | ---- | --- | ---- | -------- | -------- | --- | --- | --- | --- | --- |
Werecognizedfourofthefiveuser-basedmeasuresforevaluatingXAI
systems outlined in [Hoffman et al., 2019 ]: user satisfaction, understand-
ing, trust (and reliance) and human-XAI performance. Indeed, none of
the papers in our corpus measured participants’ curiosity, highlighting
a gap in the literature for making XAI systems more engaging through
users’ feedback. However, we actually found more than five types of
human-based metrics. Measures of the propensity of XAI systems to
enhance learning, perceived transparency and fairness, humanness and
naturalness of explanations, or cognitive workload, provide additional
| nuances |     | to the | XAI | researchers’ |     | toolbox. |     |     |     |     |
| ------- | --- | ------ | --- | ------------ | --- | -------- | --- | --- | --- | --- |
The many shades of user satisfaction. User satisfaction was the most
frequently used measure in the corpus. However, we found many nu-
ances of this concept. Some assessed whether users liked the systems
[Kim, Chris et al., 2021 , Jia et al., 2022 ], and/or found them useful [Jin
|     | 2020 |     |     |     | 2021 |     |     | 2021 |     |     |
| --- | ---- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- |
et al., , Khurana et al., , Sovrano and Vitali, ], helpful [Yan
etal., 2020 ,Jacobsetal., 2021 ],effective[Hernandez-BocanegraandZiegler,
| 2021 |          |     |      |        |            |     | 2021   |      | 2019    |       |
| ---- | -------- | --- | ---- | ------ | ---------- | --- | ------ | ---- | ------- | ----- |
|      | ] and/or |     | easy | to use | [Szymanski | et  | al., , | Kwon | et al., | ], or |
preferred the explanation or explanation system over another. In order
to capture some of these nuances while keeping the papers coding man-
ageable, we divided user satisfaction into two main clusters: ease of use
(i.e., perceived usability) and perceived usefulness of the XAI system.
Some articles already made distinctions between these two constructs
|     |     | 2020 |     |     |     | 2021 |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | ---- | --- | --- | --- | --- |
[Jin et al., , Szymanski et al., ], but others did not, especially
when using questionnaires such as the Explanation Satisfaction Scale
2019
[Hoffman et al., ], which incorporates both usability and usefulness
|     |     |     |     | 2022 |     | 2022 |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- |
concepts [Bove et al., , Guo et al., ]. When this was the case, we
| reported |     | the | measure | under | both | "usability" | and "usefulness". |     |     |     |
| -------- | --- | --- | ------- | ----- | ---- | ----------- | ----------------- | --- | --- | --- |
Definition
Perceived usability. A user-reported measure of how easy and likeable
|     | something | is  | to use. |     |     |     |     |     |     |     |
| --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Under the "perceived usability" construct, we included measures of us-
ability,easeofuse,likeability,i.e. whetherusersexpressedthattheyliked
theinteractiveexplanation(ortheXAIsystem)—typicallythroughaone-
itemquestionnaire[Guoetal., 2022 ]orthroughaqualitativethink-aloud
2020
study[Jinetal., ],—anduserpreference,i.e. whetheruserspreferred
the system to a given baseline. Questionnaires such as the Post-Scenario
Questionnaire[Lewis, 1991 ]ortheUserEngagementScale[O’Brienetal.,
2018
|     | ] were | often | used | to  | measure | usability. |     |     |     |     |
| --- | ------ | ----- | ---- | --- | ------- | ---------- | --- | --- | --- | --- |
Definition
Perceivedusefulness. Auser-reportedmeasureofhowusefulsomething
|     | is to achieve |     | the users’ |     | goals. |     |     |     |     |     |
| --- | ------------- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- |
In the concept of usefulness, we reported the accounts of "usefulnes"
and"perceivedeffectiveness",thelatterbeingassessedthroughTintarev’s

towards human like explanations the promise of interactivity 137
|     |     |     | "    | -   | "   |     | :   |      |
| --- | --- | --- | ---- | --- | --- | --- | --- | ---- |
|     |     |     | 2021 |     |     |     |     | 2021 |
questionnaire [Tsai et al., , Hernandez-Bocanegra and Ziegler, ,
| Tintarev, | 2007 | ].  |     |     |     |     |     |     |
| --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
Joint use of subjective and objective measures. Many self-reported
measureshaveanobjectiveequivalent,andthepapersinourcorpushave
taken advantage of this. This was the case for understanding, trust and
| cognitive | load. |     |     |     |     |     |     |     |
| --------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Understanding was most often measured subjectively by asking par-
2022
ticipants if they understood the system [Bove et al., , Chromik et al.,
2021 ]. However, some also assessed understanding objectively by ask-
2022
ing carefully designed, often context-specific questions [Bove et al., ,
|     |     | 2019 |     | 2019 |     |     | 2021 |     |
| --- | --- | ---- | --- | ---- | --- | --- | ---- | --- |
Cheng et al., , Ming et al., , Rebanal et al., ]. Predicted ac-
curacy, referring to the ability of users to predict what the system will
2021
output given certain entries, has been measured in [Nourani et al., ,
Chromik et al., 2021 , Springer and Whittaker, 2019 ] and could be consid-
2021
| ered,assomeargue[Chromiketal., |     |     |     |     | ],asanobjectiveunderstanding |     |     |     |
| ------------------------------ | --- | --- | --- | --- | ---------------------------- | --- | --- | --- |
of the system.
Participants’ trust in the system or explanations was mostly assessed
subjectively, by asking people to report their confidence in the XAI tool.
2021
| McKnight’sframeworkwasusedinthreestudies[Ghaietal., |     |     |     |     |     |     |     | ,Wilkin- |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- |
son et al., 2021 , Hernandez-Bocanegra and Ziegler, 2021 ]. Other pa-
2007
persreferredtoTintarev’s[Tintarev, ]measuresoftrust[Hernandez-
Bocanegra and Ziegler, 2021 , Wilkinson et al., 2021 , Tsai et al., 2021 ].
2021
[Hernandez-Bocanegra and Ziegler, ] also used items from Kouki
2019
et al. [ ] to measure trust related to explanations rather than to the
system. However, trust was also measured objectively, by observing
2016
users’ ability to reject an incorrect AI suggestion [Ribeiro et al., ,
|     | 2021 |     |     | 2021 |     |     | 2021 |     |
| --- | ---- | --- | --- | ---- | --- | --- | ---- | --- |
Liu et al., , Buçinca et al., , Kim, Chris et al., ]. We referred
to this measure as "reliance", but [Kim, Chris et al., 2021 ] framed it more
positively as "user skepticism", while others have called it "human-AI
| agreement" |     | [Liu et | al., 2021 | ].  |     |     |     |     |
| ---------- | --- | ------- | --------- | --- | --- | --- | --- | --- |
Users’ cognitive workload when interacting with XAI systems was re-
ported in five studies. It was measured by the NASA-TLX workload
index, or a subset of its items. Closely related to cognitive load are es-
timates of the time spent on the XAI system or explanation, and the
perceivedlengthand/orcomplexityoftheexplanation. Theformerisan
objective, quantitative estimate, while the latter is a self-reported mea-
|     |     |     | 2020 |     | 2021 |     |     | 2021 |
| --- | --- | --- | ---- | --- | ---- | --- | --- | ---- |
sure [Kouvela et al., , Buçinca et al., , Szymanski et al., ].
The quality of self-reported measures can sometimes fall short of re-
searchers’ expectations, as some [Dodge et al., 2022 , Naiseh et al., 2021 a,
2019
Wang et al., a] argue. Objective measures of understanding, trust
and cognitive load may offer more reliable observations, even though at
present, their measures are less standardized and more context-specific,
making results more difficult to compare across different studies. Dodge
et al. [ 2022 ] notably proposed "the ranking task" as an alternative to self-
| reported | measures. |     |     |     |     |     |     |     |
| -------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Task performance as the new benchmark. Some work [Buçinca et al.,
| 2020     |     |         | 2021      |     |                 |          |       |         |
| -------- | --- | ------- | --------- | --- | --------------- | -------- | ----- | ------- |
| , Bansal |     | et al., | ] advance |     | that subjective | measures | could | be mis- |
leading to properly assess the added value of explanations. Buçinca

138 the explanation paradox and the human centric path
-
2020
et al. [ ] found that an increase in user satisfaction did not necessar-
ily lead to improved performance, if not the opposite. Instead, Buçinca
argues, measuring task performance should be the standard benchmark
as it comes down to directly evaluating XAI systems against what they
were designed for: increasing humans’ autonomy and complementarity
with AI. While XAI may serve other purposes, such as increasing user
confidence and understanding, measuring task performance has the ad-
vantageofbeingametricthatisbothobjectiveandeasilyquantifiable. In
21 48
fact,manyempiricalstudiesinthecorpushaveadoptedit( / ). Some
articles also measured other constructs related to the task at hand, such
2021
as task complexity or time spent performing the task [Ross et al., ].
Lessfrequent goal-specificmetrics. Evaluationmeasures arechosen in
relation to the purpose that explanation serve. For example, Lee et al.
2019 2021
[ ]andAnikandBunt[ ]aimedatincreasingpublictransparency
and perceived fairness of an AI system. Therefore, Anik et al. used the
2018
questionnaire from [Binns et al., ] to assess users’ perception of the
fairnessofthesystemandLeeetal. reliedontheirownquantitativemet-
rics by asking participants to indicate on a Likert scale their agreement
with the sentences "My assignment is fair", "This participant’s assign-
mentisfair",or"Theoverallgroupoutcomewasfair". Similarly,learning
was a few times measured as a separate concept from the understanding
of the AI model. Measures of "learning" focused on how well XAI ex-
planations and systems helped users learn about a topic such as gender
2021 2021
bias ([Melsión et al., ]) or self-care awareness ([Tsai et al., ]). In
conversational interfaces, explanations were evaluated according to their
2021 2019
humanness and engagingness [Hepenstal et al., , See et al., ], to
2021
their persuasiveness [Hernandez-Bocanegra and Ziegler, ], or their
2021
naturalness [Rebanal et al., ].
4.4.4 Interactive explanations increase trust, but not neces-
sarily overtrust
3
In Chapter we found some evidence that explanations tend to in-
crease trust, even when it is unwarranted. However, it is still uncer-
tain whether interactivity in explainability can mitigate or resolve these
problems by better matching human cognitive processes. While theoreti-
cal work in education and psychology outline the benefits of interaction
2004 2019
for explanation and learning [Roussou, , Miller, ], empirical re-
2021
sults do not always align with these statements. In [Liu et al., ] for
example, they find that interactivity could increase human biases and
overreliance on AI. This subsection summarises the effects of interactive
explanations on trust and reliance using the controlled and qualitative
evaluations in our corpus. We base our qualitative findings on the sum-
419
mary presented in Figure . , and on the qualitative analyses of the
effects of interactivity provided in the corpus.
Noclearindicationofaninteractivityeffectonovertrust,overreliance
or cognitive load. Some concern has been expressed that interactivity
could increase users’ cognitive load and their overreliance on AI [Liu

towards human like explanations the promise of interactivity 139
" - " :
Figure 4.19: Left: Count
of the positive, negative
and neutral quanti-
tative evaluations of
interactive explanations
compared to static
ones, against various
user-based metrics,
based on 9 different
studies. Right: Countof
the different evaluation
outcomes in the empir-
ical studies comparing
interactive explanations
withnoexplanationasa
baseline, extracted from
13 different papers in
thecorpus.
2021
etal., ]. Wedidnotfindmanyresultstoeitherconfirmorrefutethis.
The results for user cognitive load were generally not directly related to
explanations alone, but to other external factors, either with the static
2021 2021
or no-explanation baseline. Buçinca et al. [ ] and Ghai et al. [ ]
highlighted the importance of the user’s individual need for cognition,
knowledge of the task to perform, or of the model used [Ross et al.,
2021 ]. Qualitative analyses suggest, however, that Simulate interactivity
techniquescanincreaseusers’perceiveddifficultyofinteractingwiththe
445
system as we detail in the paragraph . . .
Compared to no explanation, interactive explanations did not lead
users to over rely more on the AI. However, results were mixed for the
comparison of interactive explanations to static ones. On the one hand,
using Simulate interaction techniques, Liu et al. [ 2021 ] found that inter-
active explanations could increase users’ tendency to blindly trust the
2021
AI. On the other hand, Buçinca et al. [ ] found that their on demand
interactive features in the Clarify style could significantly decrease over-
reliance. The interactivity type therefore seems to be instrumental in the
development of overreliance.
Higher perceived control leads to greater perceived fairness, perceived
transparency, and (less clearly) trust. A participant in [Yan et al., 2020 ]
said "I want to know why it is biased, not have the machine tell me
why". This highlights the power of user controls and interactivity to
drive trust and support users’ autonomous exploration of the AI model.
2019
Lee et al. [ ] confirmed this with quantitative evidence, finding that
Reconfigure interactions significantly improved perceived fairness. The

140 the explanation paradox and the human centric path
-
authors mentioned that the Answer interaction—here participants could
correctthealgorithmicallocation—causeduserstoperceivethemodelas
fairer.
Wedidnotfindasubstantialtrendintheeffectofinteractivityontrust
in the quantitative studies in the corpus. As indicated by the right side
419 2021
of Figure . , the results in [Khurana et al., ] and [Cheng et al.,
2019
] do not converge. Some studies described the link between trust
and external factors such as users’ prior experience with AI [Ghai et al.,
2021 2021
] or on users’ individual propensity to trust [Kim, Chris et al., ].
4.4.5 Interactive explanations are useful, but not easy to use
Totakestockonthebenefitsofinteractivityinexplainability,wepresent
below a summary of empirical evaluations of interactive XAI on several
user based metrics other than trust.
Interactive explanations improve perceived usefulness but not usabil-
ity. Overall,thereappearstoberepeatedevidencethatinteractivitydoes
2022
not significantly improve perceived usability [Guo et al., , Sovrano
2021 2019
and Vitali, , Lee et al., ] compared to static explanations, but it
2022 2021
does improve perceived usefulness [Bove et al., , Ghai et al., ,
2021
Buçinca et al., ]. However, when compared to a baseline of no ex-
planation, interactive explanations lead to an increase in perceived ease
2021 2021 2021
of use [Hepenstal et al., , Tsai et al., , Kim, Chris et al., ].
This reinforces the hypothesis that interactivity is not responsible for the
improvement in perceived usability, but the presence of explanations is.
Itispossiblethatinteractivityincreasesthecomplexityofthesystem,but
atthesametimesupportsusersintheirtaskandexplorationofthemod-
2019
els. The authors of the Gamut interface [Hohman et al., ] state that
"interactivity was so fundamental for our participants’ understanding of
the models, that when we prompted them to comment on interactivity,
peoplecouldnotconceivenon-interactivemeanstoanswerboththeirhy-
potheses and prepared questions". This study illustrates the potential of
interactivity in terms of usefulness and as a factor in enabling users to
achieve their goals.
Interactiveexplanationsimproveperformancesofthe(human+AI)team,
sometimes increasing time spent on explanations. Human+AI team per-
2021
formance was found to be improved in [Ghazimatin et al., , Buçinca
2021 2019
et al., , Lee et al., ] with interactive versus static explanations.
2019 2021
However, in two other studies [Cheng et al., , Buçinca et al., ],
the time spent to interact with the explanation system was higher for
interactive explanations compared to static ones. The presence of in-
teractive explanations compared to a "no explanation" baseline also im-
proved task performance. These results seem logical, as greater interac-
tivity can help users dive deeper into exploring a model and augment
theircognitiveengagementintheprocess. However,increasingthenum-
ber of interactions with the system, as well as deeper analytical thinking,
would understandably take more time. For example, interactivity can be
designed to elicit user cognitive engagement such as in [Buçinca et al.,

towards human like explanations the promise of interactivity 141
" - " :
2021
], which in turn can enhance task performance. Further, Buçinca
et al. [ 2021 ] showed that on demand explanations—from the Clarify in-
teraction category—could significantly increase the performance of the
human+AI team compared to static explanations.
2021
However,Naisehetal.[ a]demonstratedthataninteractivefriction-
basedfeature—fallingintheAnswercategory—couldleadparticipantsto
interact significantly more with the system, while having no impact on
the time spent using the system.
Unclear role of interactivity on understanding and learning. From
419
Figure . , it appears clearly that the presence of (interactive) expla-
nations compared to no explanation enhances user understanding of a
model. Similarly,learningseemstobepersistentlyenhancedbythepres-
2021 2021
ence of interactive explanations [Tsai et al., , Melsión et al., ].
At the same time, user understanding of a model was dependent on
other factors, including the order in which users saw weaknesses in the
2021
system [Nourani et al., ], or the stage of interaction with the sys-
2021
tem [Chromik et al., ], or the type of model that was explored [Ross
2021 2019
et al., ]. In addition, Cheng et al. [ ] found that interactive ex-
planations led to higher objective and subjective understanding of the
2022
model compared to a static baseline, but Bove et al. [ ] could not find
any statistically significant improvement of interactive over static expla-
nations for both objective and subjective understanding. More work is
therefore needed to clarify the added value of interactive explanations
over static explanations for understanding and learning.
Qualitative evidence of the added-value of a few interaction tech-
niques. Despite the unclear quantitative evidence, the qualitative analy-
sis of the corpus suggests that understanding is facilitated by interactiv-
ity. For example, one participant reported that receiving feedback and
interacting with the model helped him "learn from my mistakes and ex-
2022 2021
pose my misconceptions" [Dodge et al., ]. Sevastjanova et al. [ ]
showed that participants appreciated the on demand display of explana-
2018
tionsaswellastheabilitytoeditthem. Morrisonetal.[ ]emphasized
the usability of Compare interactive features to support human cognitive
processes, finding that "comparison is much easier than classification for
2015
a person". Schaffer et al. [ ] demonstrated qualitatively that linear in-
teractivitywasperceivedasuseful. Furthermore,SpringerandWhittaker
2019
[ ]highlighttheneedforprogressivedisclosureofmodelinformation
inordertopreventusersfromseeingtheirexpectationsviolatedanddis-
trusting the system when it is correct.
"Simulate" interactions can strain users’ memory and time. While
interactive explanations of the type Simulate have been evaluated posi-
tively on many fronts, notably usability, usefulness and understanding,
theyalsoseemtotakeupmoretimeasqualitativeanalysesin[Boveetal.,
2022 2021
,Ghaietal., ]show. Additionally,afterusingasimulation-based
2022
interactionfeature,aparticipantin[Jiaetal., ]indicatedthat: "Atthe
end of the design process, I think my brain is stuck. I do not know what
I have specified before. When I want to add a new attribute, I need to

142 the explanation paradox and the human centric path
-
go back to check if I have specified it already". This calls for a careful
consideration of the natural tendency of people to lose track of previous
simulations in the design of Simulate interactions. Consistent with this
2021
observation, Ross et al. [ ] found that user performance in recreating
an outcome through perturbations of concept-features degraded as the
dimensionalityoftheconcept-featuresincreased. Futureresearchshould
therefore design simulation explanations taking into account the limita-
tions of people’s memory.
Current dialogic explanations lack humanness. In [Rebanal et al.,
2021
], participants rated the naturalness of conversational explanations
more harshly than the other measured aspects of the explanations.
2021
Also, in [Tsai et al., ], participants reported a similar lack of nat-
uralness for the questions that were asked by the system to the user.
The authors describe: "our participants felt confused about the questions
asked by the [conversational agent] in terms of the sequence, quantity,
2021
and relevance." However, in [Hepenstal et al., ] participants indi-
cated they preferred to be able to "recognize when they were talking to
a human or to a machine", actually preferring that humanness levels of
explanations remain low. This questions the validity of aiming for more
"dialogic" explanations that replicate a human-like explanation process.
We provide more thoughts on this issue in the following section.
4.5 Discussion
WediscussbelowtwoopenissuesininteractiveXAI.First,interactivity
itself needs to be explained to users, adding another layer of complexity
to XAI systems. Second, it is unclear whether dialogic/human-like ex-
planations should be considered the ideal form of explanation commu-
nication by XAI researchers.
4.5.1 Interactivity calls for meta explanations
2004
Interactivity itself requires some learning by the user [Roussou, ].
In addition to learning about the model, users must learn how to use the
controls of the interface.
2021
Hepenstal et al. [ ] observed that participants had many questions
abouthowtousetheinterfaceandcontrolit—"CanIclickonthat?". With
Answer interactions, Tsai et al. [ 2021 ] also found that some participants
felt confused by the questions asked by the system. They suggest that
it would be helpful to provide additional explanations answering ques-
tions like "why does the system ask these questions?", or "how many
2021
questions would be asked or needed?" [Tsai et al., ]. These observa-
2022
tions align with Sun et al. [ ]’s categorisation of user questions. One
ofthemiscalled"Control",andisdefinedas"Questionsaboutoptionsfor
customizing or specifying preferences for how the model should work".
Therefore, interactivity adds a layer of explanation in addition to model
explanations.

towards human like explanations the promise of interactivity 143
" - " :
We can make a parallel with the concept of meta-explanation intro-
2021 2021
ducedin[Dazeleyetal., ]. Dazeleyetal.[ ]pointtoamajorissue
in XAI research, which is the user’s need to know where explanations
come from in order to be able to trust the model and its explanations.
As the authors put it: "if we cannot trust the agent’s original decision,
how can we trust the agent’s explanation of that decision?". They call
"meta-explanations" the explanations about the explanations themselves.
Meta-explanations introduce a paradox whereby more explanations calls
for more explanations, leading to unsustainable complexity. Similarly,
explanations on the control of the interface could lead to cognitive over-
load and effects such as users ignoring explanations and AI predictions,
2021
as described in [Tsai et al., ].
Our corpus highlighted diverging results on whether interactivity has
an effect on cognitive load. Our analysis highlighted, however, the role
of individual factors to drive cognitive workload. There is therefore a
needforfutureresearchtoinvestigatehowtotacklethemetaexplanation
paradox in the context of interactive XAI, and how to find the right level
2021 2021
of explanation for each user [Dazeley et al., , Buçinca et al., ].
4.5.2 Are dialogic explanations really the grail?
2019 2017
According to Miller [ ] and Graaf and Malle [ ], people expect
explanations to follow the conceptual framework of a social interaction.
One reason for this is that people attribute human traits to XAI agents
and therefore expect them to follow social conventions [Graaf and Malle,
2017
]. Therefore, a good explanation would be provided through a so-
cial conversation. In fact, at least two studies from our corpus provided
quantitative evidence that explanations communicated through Ask in-
teractions improved perceived usability and understanding.
2021
However, the participants in [Hepenstal et al., ] were bothered by
the humanness of the XAI agent and preferred to have it made clear that
they were not talking to a real person. Instead, they preferred robot-
like explanations with "logical and clear responses". Indeed, while ex-
plainability should bring trust, anthropomorphism through human-like
conversations can diminish trust by giving people the feeling of being
2021
manipulated. Hepenstal et al. [ ] suggest that different evaluation
metrics could be applied to assess conversational XAI, such as under-
standing and bias mitigation, which are more representative of explain-
ability’s purpose.
If we take Miller [ 2019 ]’s depicted ideal of an AI agent’s explanation 4 , 4Miller presents it as a
perhaps a more important criteria than the social structure of the expla- conversation, not nec-
essarily in natural lan-
nation would be the range of questions the explaining agent is able able
guage, where the user
to answer. Overall, further theoretical work may be needed to clarify
asks a first request and
what "social interaction" means, whether it refers to its dialogue struc-
follow-upquestions
1975
ture or to the social rules it abides by, such as Grice [ ]’s maxims.
Future work could also examine the extent to which a "social" interac-
tion with an AI agent can resemble human conversations, or even if this
comparison makes sense.

144 the explanation paradox and the human centric path
-
4.6 Limitations
One of the main limitations of scoping reviews is that they do not for-
mallyappraisethequalityoftheincludedstudies[ArkseyandO’Malley,
2005
] through the means of, for example, the Cochrane Risk of Bias or
other quality assessment tools. While this is compatible with the objec-
tives of this survey—to identify, map and discuss evidence on empirical
results in interactive XAI—we remind the reader again of this limitation.
Furthermore, although we applied a standardized methodology to
identify articles, it is possible that relevant papers were missed because
they were not published in peer-reviewed conferences or journals, be-
cause they were not present in the databases we surveyed or because
they did not match our keyword search. This was the case for [Slack
2022
et al., ], which was published in a workshop and was therefore ex-
2021
cluded during the eligibility phase, or for [Wu et al., ] which did not
appear in the databases we searched. Indeed, as mentioned earlier, we
chose to focus on HCI-oriented databases (ACM DL and IEEE Explore)
rather purely AI ones, which may have led us to leave out relevant work
in CS-focused venues. Since our interest is in interactivity and user stud-
ies, it seemed reasonable to limit ourselves to academic venues in HCI.
2016 2015
Other work like [Krause et al., ] and [Kulesza et al., ] were not
includedinourstudybecausetheauthorsusetheterms"interpreting"or
"explanatory" in their title/abstract as references to the "explainability"
notion. However, we believe that it would have been difficult to define
the verbs interpret or explain and their conjugations as keywords be-
cause of their ubiquity. To remedy the limitation of a keyword search
for the interactivity dimension, we searched for papers presenting an in-
teractive XAI system in the eligibility phase instead of the identification
2009
phase [Moher et al., ]. This enabled us to include papers presenting
interactive XAI solutions even though they did not expressed or empha-
sized in the abstract their contributions to the interactive explainability
field.
In addition, we acknowledge that there may be a positive outcome
1998
bias [Callaham et al., ] in the results on interactivity because we
searchedpublishedarticles. Wehopethatbyhighlightingareasofuncer-
tainty where it is unclear whether interactivity has positive or negative
effects,thisworkwillencourageothers,includingpublishers,toconsider
all types of outcomes, including neutral or negative.
Then,althoughstepsweretakentoensureconsistencyinourcoding—
including a final review of all the codings by one researcher—the final
matrix may reflect each reviewer’s own way of thinking.
Finally, it is possible that the summary of the papers’ findings in Sec-
445 444
tions . . and . . maynotcapturethenuanceofeachcontextinwhich
theresultswerefound. However, itdoesprovideahigh-level, qualitative
view of the results of empirical studies, and that was our goal.

towards human like explanations the promise of interactivity 145
" - " :
4.7 Conclusion
This chapter presented a review of the literature on interactive expla-
nations evaluated with human users. We provided a qualitative analysis
48 1
of papers shedding light on ( ) the types of interactivity techniques
2
that have been used so far in XAI, ( ) the context in which interactive
3
explanations were implemented, ( ) the metrics used to evaluate inter-
4
active explanations with human users, and ( ) the effects of interactivity
on user satisfaction, understanding, trust, performance at task and other
user-based metrics.
We provided a classification of XAI-specific interactivity techniques
whichcanserveasabasisforexplainabilitysystemdesignerstonavigate
the interactivity spectrum in XAI.
Our analysis showed that attention has been focused on interactivity
that allows for input modification, but less attention has been paid to
perturbing outcomes of AI systems, and to dialogic interactions. Combi-
nations of dialogic interactions with interactions that allow mutation or
selection is an under-explored area. The evaluation metrics we observed
provide a wide range of ideas for XAI researchers to evaluate their sys-
tems against what they were designed for. Finally, we found converg-
ing results regarding the effect of interactive explanations on users. We
identified that interactivity increases perceived usefulness and the per-
formance of the human+AI team compared to static explanations, but
it does not improve usability. In addition, it increases time spent by
users on XAI systems. The empirical studies gathered in our corpus
also demonstrated conflicting results on the role that interactivity has on
overreliance,cognitiveload,learningandunderstanding. Thishighlights
grey areas to be addressed in future empirical research.
We hope that this work will help future research to share a common
vocabulary on interactive XAI. Also, we hope it will facilitate future sys-
tematic reviews to identify best practices in interactive XAI design, as
more empirical research is conducted in this area.
In the next part, we contribute to the onging efforts in explainability
to test explanations’ needs and effects empirically. We study explanation
needs in two applications of AI in the financial sector, taking a human-
centric approach.

| 146 the | explanation | paradox | and | the human | centric |     | path |     |     |     |
| ------- | ----------- | ------- | --- | --------- | ------- | --- | ---- | --- | --- | --- |
-
| Evaluationconcept |     | Definition |     |     | Mainevaluationmethods |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
Perceivedusability User’s perception of how easy to use Adapted question items from Explanation Satis-
theexplanationuserinterfaceis. factionScale[Hoffmanetal.,2019],Post-Scenario
Questionnaire[Lewis,1991]ortheUserEngage-
2018];
|     |     |     |     |     | ment | Scale | [O’Brien | et al., |     | qualitative |
| --- | --- | --- | --- | --- | ---- | ----- | -------- | ------- | --- | ----------- |
think-aloudstudy[Jinetal.,2020].
Perceivedusefulness User’sperceptionofhowuseful,effec- Question items from Tintarev’s questionnaire
2007],
tive or helpful the XAI system is for [Tintarev, Explanation Satisfaction Scale
2019]
|     |     | achievingtheirgoals. |     |     | [Hoffman |     | et al., | or  | [Vandenbosch | and |
| --- | --- | -------------------- | --- | --- | -------- | --- | ------- | --- | ------------ | --- |
1996];
|     |     |     |     |     | Ginzberg, |     | qualitative |     | think-aloud | study |
| --- | --- | --- | --- | --- | --------- | --- | ----------- | --- | ----------- | ----- |
[Yanetal.,2020].
Understanding The extent to which the user under- "Objective understanding": Likert-type, context-
2022,
standsamodeloritsexplanations. specific questionnaires [Bove et al., Cheng
|     |     |     |     |     |     | 2019, |         | 2019, |         |         |
| --- | --- | --- | --- | --- | --- | ----- | ------- | ----- | ------- | ------- |
|     |     |     |     |     | et  | al.,  | Ming et | al.,  | Rebanal | et al., |
2021],
|     |     |     |     |     |                                    | "Subjective | understanding": |     |             | qualitative |
| --- | --- | --- | --- | --- | ---------------------------------- | ----------- | --------------- | --- | ----------- | ----------- |
|     |     |     |     |     | thinkaloudorfree-textanalyses,e.g. |             |                 |     | [Boveetal., |             |
2022,Chromiketal.,2021].
Perceived explana- User’s perception of the length or Direct questions about the quantity, length, or
tionlength/quantity quantityoftheexplanation,oftenused complexity of the explanation, e.g. [Kouvela
etal.,2020,Buçincaetal.,2021,Szymanskietal.,
asproxiesforthecomplexityoftheex-
|     |     | planation. |     |     | 2021]. |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | ------ | --- | --- | --- | --- | --- |
Time Thetimespentbytheuserinteracting Directmeasureoftheinteractiontime, e.g. [Ross
etal.,2021].
withtheXAIsystemtoperformatask.
Trust User’s willingness to depend on an Question items from McKnight’s framework
XAI system because of the character- [Mcknight et al., 2011], Tintarev’s questionnaire
istics of the system [Mcknight et al., [Tintarev, 2007] or Kouki et al. [2019]’s measure
|     |     | 2011,Rousseauetal.,1998]. |     |     | oftrusttowardsexplanations. |     |     |     |     |     |
| --- | --- | ------------------------- | --- | --- | --------------------------- | --- | --- | --- | --- | --- |
Cognitiveload The amount of working memory re- NASA-TLXworkloadindex.
|     |     | sources     | used by the user | while inter-   |     |     |     |     |     |     |
| --- | --- | ----------- | ---------------- | -------------- | --- | --- | --- | --- | --- | --- |
|     |     | acting with | the XAI          | system [Miyake |     |     |     |     |     |     |
andShah,1999].
Performanceattask The performance of the human+XAI Measured through case-by-case metrics adapted
teaminperformingaspecifictask. to a context-specific task, e.g. [Dodge et al.,
2022,Buçincaetal.,2021,FengandBoyd-Graber,
2019].
Learning How well explanations and/or XAI Context-specificquestionsusuallydefinedbythe
systems help users learn about a spe- authors themselves about a topic. See examples
|     |     | cifictopic. |     |     | for | learning | about gender | bias | ([Melsión | et al., |
| --- | --- | ----------- | --- | --- | --- | -------- | ------------ | ---- | --------- | ------- |
2021])orself-careawareness([Tsaietal.,2021]).
Predictedaccuracy User’s ability to correctly anticipate NumberofcorrectguessesoftheAI’sprediction
|     |     | theAI’sbehavior. |     |     | bytheuser[Nouranietal.,2021,Chromiketal., |     |     |     |     |     |
| --- | --- | ---------------- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- |
2021,SpringerandWhittaker,2019].
Perceivedcontrol User’sperceptionoftheircontrolover Adapted question items from the Knijnenburg
|     |     | theXAIsystem. |     |     | etal.[2012]framework. |     |     |     |     |     |
| --- | --- | ------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
Perceivedfairness Theextenttowhichusersperceivethe Fairness questionnaires from Binns et al. [2018]
Leeetal.[2019].
|     |     | XAIsystemtobefairandtransparent. |     |     | or  |     |     |     |     |     |
| --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Perceived trans- User’sperceivedunderstandingofthe Adapted question items from Millecamp et al.
parency recommendationrationale [2019]orTintarev[2007]frameworks.
Reliance User’s ability to reject an incorrect AI Precisionand/orrecallincorrectrejectionsorac-
|     |     |     |     |     | ceptancesofaprediction,e.g. |     |     |     | [Ribeiroetal.,2016, |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | ------------------- | --- |
suggestion.
|     |     |     |     |     |     |         | 2021,   |         | 2021, |       |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ----- | ----- |
|     |     |     |     |     | Liu | et al., | Buçinca | et al., | Kim,  | Chris |
etal.,2021].
4.18:
Figure Evaluation concepts used twice or more in the corpus with corresponding definitions and
evaluationmethods.

| PART II   |               |         |            |             |
| --------- | ------------- | ------- | ---------- | ----------- |
| Complying |               | with    | regulation |             |
| using     | human-centric |         |            | explainable |
| AI: two   | case          | studies |            | in finance  |

149
Chapter 5: Empowering customers of robo-advisors with explainabil-
ity presents a mixed-methods experiment (qualitative and quantitative)
on the impact of different formats of explanations on customers’ trust
and empowerment in life-insurance underwriting. This chapter builds
2022
onthereflectionspresentedina workshoppaperandonsubsequent
2023
studies that were published as a conference paper in :
"Towards Informed Decision-making: Triggering Curiosity in Explanations to Non-expert
Users",AstridBertrand,2022WorkshoponXAIandHCI,IHMConference,Namur,
Belgium,2022 https://hal.science/hal-03651368/document.
"Questioningtheabilityoffeature-basedexplanationstoempowernon-expertsinrobo-advised
financial decision-making", Astrid Bertrand, James R. Eagan, Winston Maxwell, Pro-
ceedingsofthe2023ACMConferenceonFairness,Accountability,andTransparency
(FAccT’23),Chicago,USA,2023 https://doi.org/10.1145/3593013.3594053.
As the first author of these studies, I delineated the motivation and
research questions with the guidance of my colleagues at the ACPR, no-
tably Olivier Fliche and Christine Saidani, and both co-authors. I con-
ducted interviews with supervisors and novice users, coded a fictitious
robo-advisor using python and javascript, designed and coded expla-
nation prototypes, conducted and analyzed the quantitative study, and
wrote the paper. The methods, results, and text were discussed with all
three co-authors.
Chapter 6: Understanding the supervisors’ needs for explainable AI in
financial crime detection presents a qualitative, mixed-methods analysis
(leveraging HCI and legal approaches) of the perspective of regulatory
supervisors on the role of explainability in the field of anti-money laun-
dering. This chapter will soon be published as a conference paper:
"AIisEnteringRegulatedTerritory: UnderstandingtheSupervisors’PerspectiveonModel
Justifiability in Financial Crime Detection", Astrid Bertrand, James R. Eagan, Winston
Maxwell, Joshua Brand, was conditionally accepted for publication in the proceed-
ingsofthe2024CHIConferenceonHumanFactorsinComputingSystems(CHI’24),
Honolulu,Hawaï,USA,2024.
Asthefirstauthor, Idelineatedthemotivationandresearchquestions,
designedandconductedalltheworkshopsandinterviews,andwrotethe
paper. The fourth co-author helped in the analysis of a few workshop
transcripts. The methods, results, and text were discussed with all co-
authors.

| 150 the | explanation | paradox | and the human | centric path |
| ------- | ----------- | ------- | ------------- | ------------ |
-

Chapter 5
Empowering customers
of robo-advisors with
explainability
his chapter
T sheds light on the challenge of using algorithmic expla-
nations for user empowerment and customer protection compliance. We
examine in a real world scenario the "explanation paradox": one the
one hand, explanations are necessary to inform users of critical infor-
mation regarding the decisions made about them. On the other hand,
3
Chapter revealed that explanations tend to reinforce trust, even when
it is unwarranted, making customers more vulnerable to inappropriate
recommendations. In this chapter, we therefore explore the potential of
human-centric explainable AI to address this challenge.
Specifically, we investigate whether legally required feature-based ex-
1
planations for life-insurance robo-advisors help clients make better fi- 1Robo-advisors are on-
nancial decisions. We also consider the perspective of regulatory super- line platforms that pro-
videfinancialadvice.
visors in customer protection in life insurance. We find that providing
feature-based explanations does not improve appropriate reliance or un-
derstanding compared to not providing any explanation. In addition,
dialogicexplanationsincreaseusers’trustintherecommendationsofthe
robo-advisor,sometimestotheusers’detriment. Thisreal-worldscenario
illustrateshowXAIcanaddressinformationasymmetryincomplexareas
such as finance. This case study was made possible by our collaboration
2
withtheACPR ,theregulatoryauthorityforfinancialservicesinFrance. 2In French "Autorité de
Contrôle Prudentiel et
We begin by presenting some background on the literature on XAI for
deRésolution"
52
non-expert users and on the context of life-insurance in Section . . We
then build Robex, an explainable robo-advisor, to enable our domain-
driven, contextual enquiry, using market research. We design explana-
tions of Robex using co-design with end-users and regulatory supervi-
sors. We present the methodology for this co-design qualitative study in
53
Section . . We redesign our explainability prototype based the needs
of non-expert clients and the requirements of regulatory supervisors, ex-
54
perts in customer protection, in Section . . In a subsequent study, we
use Robex to quantitatively compare the effectiveness of various expla-
nation formats in helping users understand, and appropriately rely on
recommendations. We test the capacity of explanations to meet the cus-

| 152 the | explanation | paradox | and the human | centric path |
| ------- | ----------- | ------- | ------------- | ------------ |
-
tomer protection objectives pursued by financial regulation. We present
55
the methodology used for this quantitative experiment in Section . ,
anditsresultsinSection 56 . . Section 57 . discussestheimplicationsofour
| findings | on the role | of explainability | to inform customers | in finance. |
| -------- | ----------- | ----------------- | ------------------- | ----------- |

empowering customers of robo advisors with explainability 153
-
| 5.1 | Motivation |     | and | research |     | questions |     |     |     |     |     |
| --- | ---------- | --- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- |
With the rise of commercial recommender systems, online AI-based
services are becoming increasingly common. As a result, internet users
are frequently presented with opaque personalized suggestions. While
explanations are often unnecessary or non-critical in many low-risk ap-
plications of AI, such as for movie or music suggestions, they can be
required by law in some high-stakes industries, such as finance. This is
| the case | for | systems | distributing | life | insurance | proposals |     | in France. |     |     |     |
| -------- | --- | ------- | ------------ | ---- | --------- | --------- | --- | ---------- | --- | --- | --- |
Robo-advisors are democratising access to investing by enabling full
onlinedistributionoflifeinsurancecontractsandotherinvestmentplans.
After answering a few profiling questions, users receive a recommenda-
tion for a life insurance contract that matches their financial situation. In
recentyears,theserecommendersystemshavestartedtoutingAItomake
more targeted suggestions. In Europe, financial legislation requires that
the reasons for recommending a life insurance plan be explained accord-
ingtothecharacteristicsoftheclient,inordertoempowerherinmaking
a "fully informed decision". In this context, the financial regulation aims
at protecting clients from recommendations misaligned with their objec-
| tives, | risk appetite |     | and other | personal | characteristics. |     |     |     |     |     |     |
| ------ | ------------- | --- | --------- | -------- | ---------------- | --- | --- | --- | --- | --- | --- |
3
Additionally,theforthcomingAIActclassifies AI-basedrobo-advisors 3as 2023,
of December
4
as "high-risk" , subjecting them to a demanding certification process and based on the European
|                   |     |     |              |     |          |         |     |     |     | Commission’s | proposal    |
| ----------------- | --- | --- | ------------ | --- | -------- | ------- | --- | --- | --- | ------------ | ----------- |
| high transparency |     |     | requirements | in  | the near | future. |     |     |     |              |             |
|                   |     |     |              |     |          |         |     |     |     | and the      | Council and |
|                   |     |     |              |     |          |         |     |     |     | Parliament’s | adopted     |
Moreover,thefinancialdomaincanfeeloverwhelmingandcomplexto
texts.
many people [Prawitz et al., 2006 ], which poses an additional challenge:
|     |     |     |     |     |     |     |     |     |     | 4Text adopted | by the |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------ |
explaining in simple terms not only the attributes of the system but also Council in Nov. 2022,
|     |     |     |     |     |     |     |     | 2021 |     |     | 5:  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
financial principles to novice users. Few studies [Bibal et al., ] have Annex III, point "AI
focused on how to design legally required explanations for lay users in systems intended to be
|     |     |     |     |     |     |     | 2   |     |     | used for | risk assessment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------------- |
complex,high-stakesscenarios. AsseeninChapter ,,cross-disciplinary
|     |     |     |     |     |     |     |     |     |     | and pricing | in relation to |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------------- |
effortsinbothlawandHCIarerare,andtheregulatorychallengesassoci- naturalpersonsinthecase
atedwithexplainabilityhavenotbeenfullyexploredbyHCIresearchers. of life and health insur-
Nevertheless, recent advances in the fast-growing field of explainabil- ance with the exception of
ity have brought a better understanding of how different representations AIsystemsputintoservice
|     |     |     |     |     |     |     |     | 5   |     | by providers | that are mi- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ |
and interactions of AI explanations impact non-expert users [Szyman-
|     |      |     |     |      |     |      |     |     |      | cro and | small-sized enter- |
| --- | ---- | --- | --- | ---- | --- | ---- | --- | --- | ---- | ------- | ------------------ |
|     | 2021 |     |     | 2022 |     | 2019 |     |     | 2021 |         |                    |
ski et al., , Bove et al., , Cheng et al., , Rebanal et al., , prises."
Mohseni et al., 2021 b]. Szymanski et al. [ 2021 ] found that lay users pre-
|     |     |     |     |     |     |     |     |     |     | 5Here, | "non-expert" |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ |
ferred graphical explanations but could more easily misinterpret them refers to users who are
|     |     |     |     |     |     |     |     |     |     | either | inexperienced |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------- |
comparedtotextualexplanations,motivatingtheneedforhybridtextual
andvisualexplanations. However,littleisknownaboutwherethecursor in the domain task or
|        |           |         |     |             |        |          |     |     |     | inexperienced | in using |
| ------ | --------- | ------- | --- | ----------- | ------ | -------- | --- | --- | --- | ------------- | -------- |
| should | be placed | between |     | textual and | visual | content. |     |     |     |               |          |
AIsystems.
We aim to address these gaps by leveraging the knowledge of cus-
tomer protection specialists. We believe the insights from experts from
the regulatory sphere present interesting yet so far unsolicited proxies
for characterizing the users’ needs. We address the question of enabling
2021
warranted customer trust in recommender systems [Buçinca et al., ],
| which | ties in  | with      | the research | in the          | previous | chapters. |     |     |     |     |     |
| ----- | -------- | --------- | ------------ | --------------- | -------- | --------- | --- | --- | --- | --- | --- |
| Our   | research | questions |              | are as follows: |          |           |     |     |     |     |     |

154 the explanation paradox and the human centric path
-
RQ1: Whataretheregulatoryexpectationsforexplanationsinfinancialinvest-
ment services to protect customers? How can current XAI methods meet
them?
RQ2: How do regulatory supervisors on the one hand and end users on the
other describe the need for explanations?
RQ3: Howeffectivearedifferentrepresentationsofhybridtextualandgraphical
explanations to protect non-expert users?
Ourcasestudyinlife-insurancehasimplicationsforotherprofilingAI
systems that interact with customers and data-subjects. For example, for
systems making automatic individual decisions based on profiling, the
GDPR requires to provide explanations such as "meaningful information
6
about the logic involved" . 6Article 15(1)(h) Gen-
eral Data Protection
Regulation(GDPR).
5.2 Background
This study falls in the HCI line of research on understanding explain-
2022 2020 2009
ability needs [Sun et al., , Liao et al., , Lim and Dey, ], and
on testing explanations’ effects with real users ("application-grounded
2017
evaluations" [Doshi-Velez and Kim, ]). We describe those research
24 2
trendsinSection . ofChapter . Specifically,webuildonexplainability
research focusing on non-expert users. We highlight relevant findings
below.
5.2.1 Mitigating overreliance issues for non experts
3 4
As reviewed in Chapters and , some user studies evaluated the
ability of XAI methods to successfully convey accurate mental models
of AI systems to users. This line of research sheds light on the lim-
itations of some technical solutions for aiding user understanding, or
2020
worse, on their potential for deception [Kumar et al., , Kim et al.,
2016 2016 3
, Ribeiro et al., ]. In Chapter , we found that user expertise,
knowledge and skills appeared to be an essential factor for appropriate
trust calibration in explainable AI systems. Specifically, non-expert users
were more likely to be convinced by the mere presence of an explana-
2021 2020 2019
tion [Eiband et al., , Fürnkranz et al., , Lai and Tan, ], or
2021
to fell into confirmation or completeness bias [Szymanski et al., ].
2020
Further, Simkute et al. [ ] stressed the importance of differentiating
the reasoning of experts from that of lay users and reflecting this differ-
ence in the design of explanations. Quite logically, experts are able to be
more critical of the explanations, sometimes at the cost of not trusting
them enough, whereas lay users are more subject to overreliance [Schaf-
2019 2021
fer et al., , Bayer et al., ]. Explanations must therefore support
either trust building for experts, or critical thinking for lay users.
Another key difference is the level of motivation to use explanations,
whichcanbemuchlowerfornon-expertusers. Thismakesitparticularly
challengingtomakeexplanationsbothsimpleandappealingtolayusers,
whileencouragingcognitiveengagementandskepticism[Bertrandetal.,

empowering customers of robo advisors with explainability 155
-
2022 ,Naisehetal., 2021 a]. Itisstillunclearifexplanationsfornon-expert
users can be designed to foster trust and understanding while encourag-
ing users’ critical thinking (i.e. ability to detect errors) on the other. This
maybedesirableinsensitivecontextswherealgorithmicpredictionsmay
| have | a strong | impact    | on    | the user’s     | quality | of    | life.        |     |          |
| ---- | -------- | --------- | ----- | -------------- | ------- | ----- | ------------ | --- | -------- |
|      | 5.2.2    | Designing |       | visualisations |         | of AI | explanations |     | for non- |
|      |          | expert    | users |                |         |       |              |     |          |
Some work has focused on the implementation of explanations for
non-expert users in specific contexts [Szymanski et al., 2021 , Bove et al.,
| 2022 |         |         | 2019 |     |     |     |     |     |     |
| ---- | ------- | ------- | ---- | --- | --- | --- | --- | --- | --- |
|      | , Cheng | et al., |      | ].  |     |     |     |     |     |
2019
|     | Chengetal.[ |     | ]presentedexplanationsofanalgorithmicschoolad- |     |     |     |     |     |     |
| --- | ----------- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
mission decision process to users with no domain or technical expertise.
They found that static and interactive explanations, where users could
change the inputs to see the resulting outcome, improved users’ under-
standing of the AI decisions. Bove et al. [ 2022 ], however, were unable
to replicate these results in the context of explaining an algorithmic car
insurancepricingdecision. Theydidnotfindthatexplanationsimproved
comprehension but they did improve user satisfaction. Szymanski et al.
2021
[ ] studied how different representations of explanations, either vi-
sual, textual or both, affect users’ understanding of an AI system in an
|     |     | 7   |     |     |     |     |     |     | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
artificial task . The paper shows that purely visual explanations can be 7In
the experiment,
subject to misinterpretation, while purely textual explanations are better participantsweretasked
with estimating the
understood but less satisfactory to users. A combination of the two rep-
reading time of news
resentations could therefore provide the best of both worlds. However,
articles.
there may be many different ways to design "hybrid" textual and visual 8inthiscase,linegraphs
explanations. Additionally, it is still unclear if textual explanations pre-
sentedasconversationsachievebetteruserpreferencesandimprovetask
| accuracy | compared |     | to  | graphical | formats. |     |     |     |     |
| -------- | -------- | --- | --- | --------- | -------- | --- | --- | --- | --- |
Then, explanations’ ability to engage users in a sensitive and complex
topic such as financial investment has not yet been studied in the XAI
literaturewhereartificialcontextsareoftenusedastestbenches[Buçinca
| et  | al., 2021 | , Dodge  | et al., | 2022                                          | , Feng and | Boyd-Graber, |     | 2019 ]. |     |
| --- | --------- | -------- | ------- | --------------------------------------------- | ---------- | ------------ | --- | ------- | --- |
|     | 5.2.3     | Context: |         | life-insurancedistributionwith"robo-advisors" |            |              |     |         |     |
In this chapter, we focus on a real-case application of explainability:
explanations of online recommendations for life insurance products. In
Europe,explanationsinthiscontextarelegallyrequiredbysector-specific
regulations to ensure customer protection. We describe below the case
| study | context | and | the | related | legal requirements |     | for | explanations. |     |
| ----- | ------- | --- | --- | ------- | ------------------ | --- | --- | ------------- | --- |
Overview. As AI systems gain performance, their adoption expands
to areas considered critical. In finance, increasingly sophisticated rec-
ommender systems known as "robo-advisors" are democratizing online
distribution of life insurance. In France, where the study was conducted,
life insurance is a savings vehicle used both to pass on money to a des-
ignated beneficiary upon the death of the subscriber of the contract, and
to make a long-term financial investment in a tax-advantaged environ-

156 the explanation paradox and the human centric path
-
ment. In the rest of the paper, we will only address the latter, most com-
mon usage of life-insurance. Life insurance subscribers are presented
with a financial recommendation with a specific level of risk (a higher
level of risk means more chances to win big but also more chances to
lose). Choosing a life insurance contract with an appropriate risk level—
not too high for the client’s financial situation—is crucial to ensuring
clients’ financial stability. However, many clients may not be financially
9
literate. Therefore, French and European legislation require insurance 9The European Parlia-
providers to produce "clear, precise and non-misleading" explanations to ment and the European
Concil. 2016. Directive
guide potential customers towards an "informed" decision and address
(EU) 2016/97 on insur-
the asymmetry of information between client and advisor. Most existing
ancedistribution.
online recommender systems currently fall short of this explanation re-
quirement, according to our discussions with French supervisors in the
life-insurance sector. Specifically, explanations of online recommender
systems,i.e. robo-advisors,rarelyfocusonthereasonswhyarecommen-
dation is adapted to the user’s need, which is the type of explanation we
focus on in this paper.
A trend towards more digital, AI-powered robo-advisors. The auto-
mated advice provided by robo-advisors is seen as a more cost-effective
way of delivering propositions to parts of the population that otherwise
have no access to financial advice, as highlighted in an OECD report
2020
[Mamiko, ]. In addition, the COVID crisis has accelerated the in-
terest in online systems by increasing the demand for online and real-
2021
time services [Balasubramanian et al., ]. In France, most current
robo-advisors are rule-based, with varying degrees of complexity in the
10
amount and nature of the rules . Yet, many studies foresee an ac- 10This was pointed out
celeration of AI-based solutions to distribute financial services and in by the participants in
2021 2020 our study who are su-
life-insurance plans[Balasubramanian et al., , Mamiko, ]. AI-
pervisors of the life in-
poweredsystemsofferfasterandmorepersonalizedfinancialadvice. For
surancesector.
brokers, data-driven profiling helps identify risk in a more fine-grained
2020
manner [Balasubramanian et al., ]. The insurance market is also
gaining interest in AI-powered robo-advisors with the successful exam-
ples of companies which used this technology to increase sales revenue
2020
significantly [Balasubramanian et al., ].
Regulatory requirements for feature-based explanations. In the life-
insurance context, financial legislation regarding the insurance sector
20 30
apply. The law on insurance distribution (Articles and of Direc-
2016 97 20 2016
tive (EU) / of January , ), which aims to protect consumers
against the sale of products unsuited to their needs, specifies: "The dis-
tributor shall advise on a contract that is consistent with the requirements and
needs of the prospective subscriber and shall specify the reasons motivating this
11
advice." . The text also mentions that: "the distributor specifies in writing 11Article L. 521-4 of the
[...] the client’s requirements and needs and provides objective information on FrenchInsuranceCode
the insurance product offered in a comprehensible, accurate and non-misleading
form to enable the prospective subscriber to make a fully informed decision."
522 5
Further, the duty of information and advice in life insurance (L. - of
the French Insurance Code) requires to "formalize the reasons for the ap-
propriateness of the proposed contract in relation to the requirements and needs

empowering customers of robo advisors with explainability 157
-
expressed.", which implies a requirement for feature-based explanations.
This leads us to question more precisely the purpose of the explana-
tion in light of the objectives of the law. What exactly is expected of the
explanationsothatitiseffectivewithregardtotheobjectivesoftheArti-
521 4 522 5
clesL. - andL. - oftheFrenchInsuranceCodeandEUDirective
2016 97
/ ? One of the objectives of the explanations is to enable future
life-insurance subscribers to make a "fully informed" decision about the
product being proposed. This objective is explicitly stated in the text of
521 4 20
ArticleL. - oftheFrenchInsuranceCodeandArticle ofEUDirec-
2016 97
tive / . However, this objective is relatively imprecise and difficult
to measure. To better assess whether an explanation allows for an "in-
formed" decision, the goal should be broken down into subgoals that are
1
easier to verify. We understand these subgoals to be ) help users appro-
priately rely on a recommendation (and be able to detect a big mistake)
2
) help users understand a recommendation and why it is appropriate
3
for them ) help users calibrate their trust in robo-advisors. This is what
2
we measured in Study .
In addition to the goal of "fully informing" clients, the law aims at
enhancing the accountability of intermediaries by imposing the obliga-
tion to set out in writing the client’s needs as well as the reasons why
the recommended product is in line with those needs. The formalization
of these steps will reduce the risks of intermediaries letting conflicts of
interest interfere with their duty to give objective investment advice to
customers.
In other contexts, AI systems may also be affected by requirements
for feature-based explanations. Consumer protection law has provisions
regarding explanations of recommender systems in online marketplaces.
It notably imposes to show "the main parameters determining the ranking
[...] of offers presented to the consumer as a result of the search query and the
12
relative importance of those parameters as opposed to other parameters" . The 12New art. 6(a) of Di-
General Data Protection Regulation [European Parliament and Council, rective 2011/83 on Con-
2016 sumerRights
] provisions also apply in the case of entirely automated individual
decisions based on profiling. It requires that data controllers disclose
"meaningfulinformationaboutthelogicinvolved"(articles 13 - 15 ). TheGDPR
provisions apply "when the decisions (i) involve the processing of personal
data, (ii) are based solely on an automated processing of data and (iii) produce
legal or significant effects on the recipient of the decision" [Bibal et al., 2021 ,
2016
European Parliament and Council, ].

| 158 | the | explanation |     |     | paradox | and | the human | centric | path |
| --- | --- | ----------- | --- | --- | ------- | --- | --------- | ------- | ---- |
-
| 5.3 |       | Study  | 1        | Methodology: |        |     | a market-driven  |     | co- |
| --- | ----- | ------ | -------- | ------------ | ------ | --- | ---------------- | --- | --- |
|     |       | design | approach |              |        |     |                  |     |     |
|     | 5.3.1 |        | System   | design:      | Robex, |     | the robo-advisor |     |     |
13
Robex is a simplified and fictional life-insurance recommender sys- 13Standing for EXplain-
tem developed for the purpose of this study. The recommendation algo- ableROBo-advisor
rithm of Robex is not AI but a rule-based algorithm established with the
4
helpof domainexperts,morepreciselysupervisorsofthelife-insurance
industry. Indeed,sinceourgoalwastostudyexplanationrepresentations
using existing agnostic explainability methods, we did not need to use a
real AI algorithm for this study. Similarly, the design of Robex was not
ourfocus. However,wewantedourfictionalrobo-advisortoreplicatethe
type of interface that robo-advisor clients would face. Therefore, we con-
ducted a market analysis of existing online robo-advisors in France. This
lead us to review the design of four major players in France: Yomoni,
14
Nalo, Linxea and Wesave . For each of the identified robo-advisors, we 14https://www.yonomi
testedtheuserjourneyfromtheprofilingquestionnairetothesimulation .fr/,https://www.nalo
.fr/,https://www.linx
of the robo-advisor’s proposal. We took inspiration from their content
ea.com/, https://www.
andinterfacedesign. Thisalsoallowedustoidentifiedtheclassicalsteps
wesave.fr/
| in  | a robo-advisor |     | user | journey. |     |     |     |     |     |
| --- | -------------- | --- | ---- | -------- | --- | --- | --- | --- | --- |
The usual subscription process with robo-advisors is as follows. First,
users go through a series of questions about their profile and financial
objectives. Then, they can see the summary of their profile and the pro-
posed recommendation, on the same page. Robex follow the same first
stages. During the recommendation phase, Robex presents an additional
| section |     | on why | this | product | is  | recommended | to you. |     |     |
| ------- | --- | ------ | ---- | ------- | --- | ----------- | ------- | --- | --- |
The following elements from existing robo-advisors on the market
| have | inspired |     | us to | implement |     | similar | features in Robex: |     |     |
| ---- | -------- | --- | ----- | --------- | --- | ------- | ------------------ | --- | --- |
• thequestionsusedintheprofilingquestionnaireabouttheuser’schar-
acteristics (risk appetite, financial knowledge) and project. The ones
51
|     | we used | in  | Robex | are presented |     | in Table | . . |     |     |
| --- | ------- | --- | ----- | ------------- | --- | -------- | --- | --- | --- |
• the brief, textual explanations in the profiling questionnaire to give
some context and to indicate the answer to a question testing financial
54
|     | knowledge, |     | as shown |     | in Figure | . . |     |     |     |
| --- | ---------- | --- | -------- | --- | --------- | --- | --- | --- | --- |
• the vocabulary used, driven by domain specificity and also by an in-
|     | tention | to be | accessible |     | to all. |     |     |     |     |
| --- | ------- | ----- | ---------- | --- | ------- | --- | --- | --- | --- |
• theseamlessnavigationbetweenthedifferentstepsoftheuserjourney,
and the clear presentation of the different stages upfront thanks to a
progress bar at the top of the page, usually including "project", "sim-
ulation", "subscription", "documents", "signature". As with real robo-
advisors, Robex presents a user journey progress bar, but adapted to
|     | the journey |     | of the | participants |     | in our | experiments. |     |     |
| --- | ----------- | --- | ------ | ------------ | --- | ------ | ------------ | --- | --- |
• the presentation of the allocation of assets into large themes "actions",
"obligations"... or by geographical region. However, all financial sup-
|     | port | and allocations |     | in  | Robex | were fictionnal. |     |     |     |
| --- | ---- | --------------- | --- | --- | ----- | ---------------- | --- | --- | --- |

empowering customers of robo advisors with explainability 159
-
• matchingtheusertooneofanumberofproposalswithdifferentlevels
of risk. Most robo-advisors propose a range of seven to ten proposals
(whichtheysometimepresentas"userprofiles"). Welimitedtherange
of proposals to five to reduce the complexity of our study.
Figure 5.1: Fictional
life-insurance plans
proposed by Robex,
the explainable robo-
advisor developed for
thisstudy
4
In parallel, we conducted informal interviews with supervisors with
experience in the supervision of life-insurance distributors to better un-
derstandthedomain. Thesediscussionswereinstrumentalindeveloping
5
our own, simplified, profiling questionnaire to measure user character-
istics: the amount to be invested compared to the user’s total financial
wealth, her investment objective, her financial knowledge and experi-
ence, her risk appetite and the proportion of her financial assets already
placed on financial markets. For each of the questions used to measure
51
thesecharacteristics(cf.. Table . ),weassociatedcoefficientssoastoob-
tainarisk-scorethatdenotedtheamountofriskausercantake. Wethen
5
sketched five fictional but realistic life-insurance plans that represent
51
levels of risk, as shown in Figure . . Our score-based rules for insur-
ance distribution then matched a profile to a plan. Robex is simplified
because we have not taken into account the fees, investment horizons or
performance of the funds in order to keep the complexity of the exper-
iment manageable. The simplified Robex algorithm is presented in the
2
Appendix B .

160 the explanation paradox and the human centric path
-
Figure 5.2: Screenshot
of the Robex interface,
showing the profiling
questionnaire stage at
thestartoftheuserjour-
ney. Translated from
FrenchtoEnglish.
Figure 5.3: Screenshot
of the Robex interface,
showing the recom-
mendation stage. As
required by law, a
summary of the user’s
profile is displayed
first, followed by a
life-insurance contract
proposal with details.
The explanation is
presented on the same
page, just after the
proposal.

empowering customers of robo advisors with explainability 161
-
Usercharact. Questionswith[possibleanswers]
Objective Whatwouldbethemainobjectiveofyourinvestment? [Makemysavingsgrow,Financea
project,Financemyretirement,Passonmyassets,Protectmysavings]
Amount to be in- Howmuchwouldyouliketoinvest? [Lessthan5000€,Between5000€and10000€,Between
vested 10000€and50000€,Morethan50000€]
This amount represents what percentage of your total financial assets (excluding your
home)? [Less than 5%, Between 5% and 25%, Between 25% and 50%, Between 50% and
75%,Morethan75%]
Percentage of Have you already invested in a financial product with a risk of capital loss? If so, how
assets already much of your total financial assets do these financial products represent? [Less than 5%,
invested Between5%and25%,Between25%and50%,Between50%and75%,Morethan75%]
Riskappetite Which of the following statements is closest to the level of financial risk you are willing
to take when saving or investing? [Take significant financial risk hoping for significant
returns, Take above average financial risk hoping for above average returns, Take average
financialriskhopingforaveragereturns,Idonotwishtotakeanyfinancialrisk]
For the next three sentences, please indicate the likelihood that you would engage in the specified
behaviorifyouwereinthesituationdescribed"Investing10%ofyourannualincomeinanin-
vestmentconsistingofsecuritiesissuedbytheEuropeanUnion"[Veryunlikely,Somewhat
unlikely,Uncertain,Somewhatlikely,Verylikely]
"Investing5%ofyourannualincomeinhighlyspeculativesecurities"[Veryunlikely,Some-
whatunlikely,Uncertain,Somewhatlikely,Verylikely]
"Investing 10% of your annual income in a new business" [Very unlikely, Somewhat un-
likely,Uncertain,Somewhatlikely,Verylikely]
Financial Haveyoueversubscribedtoalifeinsurancecontract? [Yes,No]
knowledge and ex- Have you ever invested in a financial product with a risk of capital loss (e.g. PEA (Plan
perience d’Epargne en Actions), multi-support life insurance contract, securities account, crypto
assets,investmentfunds...)? [Yes,No]
Ahighexpectationofgainsimpliesahighriskofcapitalloss. [True,False]
Arealestatefund(SCPIorOPCI)isafundwithguaranteedcapital. [True,False]
Thecapitalinvestedinalifeinsuranceplanisblockedfor8years. [True,False]
The capital invested in life insurance units of account is subject to a risk of capital loss.
[True,False]
Table 5.1: Question
used in the Robex’s
profiling questionnaire
for measuring users’
personal characteristics
(translated from French
toEnglish).

162 the explanation paradox and the human centric path
-
Figure 5.4: Screenshot
of the Robex interface,
showing the answers it
provided for test ques-
tions on participants’ fi-
nancialknowledge.

empowering customers of robo advisors with explainability 163
-
5.3.2 Explanation prototype
523
As seen in Section . . , the required explanations in life-insurance
shouldlinkclient’scharacteristicstotherecommendation, whichiswhat
feature importance techniques do. To investigate the impact of feature
importance explanations on users’ trust and appropriate reliance on rec-
ommendations,wedevelopedfeatureimportanceexplanationsinRobex.
We approached the explainability phase as if the rule-based recom-
mender algorithm in Robex was a black-box. Our results can therefore
be transposed to more opaque AI-powered robo-advisors. In each of
2017
the studies presented below, we used SHAP [Lundberg and Lee, ]
a post-hoc, agnostic, and widespread interpretability method, to gener-
ate feature weights. We then use these weights as a basis for designing
explanations that differ in representation format and interactivity.
55
One of our early prototypes is shown in Figure . . We first de-
signed the explanation interface taking inspiration from the graphical
2017
Shapley explanations presented in [Lundberg and Lee, ]. However,
we tried to simplify the visual elements to make them readable by non-
professional users. Specifically, we simplified the graph into a table, be-
cause some research on explainability showed that tables were the most
interpretable representation medium for non-professional users [Huys-
2011
mans et al., ]. The table sorts features per their influence on the risk
of the prediction: features that decreased the risk of the proposal are
shown in the left column and features that increased it on the left. We
also applied a card-based design for the display of each feature-related ex-
planation. Thisdesignenablestoprovidemorecontextwitheachfeature.
Each card contains the name of the feature in boldface, the value of the
feature for the user in grey, and its impact in natural language sentence
2022
[Bove et al., ].
1
We showed to participants in Study a prototypical "graphical" sum-
mary of the importance of each variable on the risk of the proposal, as
55
shown in Figure . . We improved the explanation representation based
on the feedback from expert and lay participants of the co-design exper-
iment we present in the following section.
5.3.3 Co-design sessions and analysis
1 2
To answer our RQ and RQ , we interviewed domain experts and lay
userstobetterunderstandendusersandsupervisorsneedsandexpecta-
2005
tions, following a participatory design approach [Spinuzzi, ]
Procedure. Each participant took part in an individual session that
45 1 30
lasted between minutes and h . The aim of the interviews was
to collect users’ feedback on our prototype, and work with users and
domain experts to create explanations that meet their needs and require-
ments. This participatory design approach has already been endorsed in
2023
the field of explainability, for example in [Panigutti et al., a, Cheng
2022 2019
et al., , Wang et al., a]. Each co-design session was divided into

164 the explanation paradox and the human centric path
-
Figure 5.5: Screenshot
of the feature-based ex-
planation prototype for
Robex. In orginial lan-
guage (French). Indi-
vidual factors that de-
crease investment risk
are shown on the left in
descending order of im-
portance and factors in-
creasinginvestmentrisk
areontheright.
three parts: a semi-structured interview, a task-oriented think aloud por-
tion and a post-study questionnaire. One researcher was present during
all interviews and took detailed notes of the participants’ answers and
think-aloud statements. The first part of the session consisted of a semi-
structured interview to explore the needs of life-insurance clients for ex-
planations of recommendations. Structured questions varied slightly if
participants were supervisors or novice end-users. Regulatory supervi-
sors were asked about the role of explanations in enabling users to make
informed decisions. They were also asked about the best format and
type of explanation to achieve this goal. Additionally, they were asked
to provide their thoughts on the explanations currently offered by robo-
advisors and how to adapt to clients with little financial knowledge. We
askednoviceusersiftheyhadanyexperienceinusingrobo-advisorsorin
receiving financial investment recommendations and what explanations
theywouldliketoreceiveabouttherecommendedfinancialproduct. We
gave some context on life-insurance and on robo-advisors to people that
had no experience at all with financial investments. During the second
partofthestudy,participantswereaskedtouseRobex. Participantswere
observedbytheresearcherandaskedtothinkaloudthroughouttheirin-
teraction with the system. Finally, participants were asked about their
overall impression of the system.
Participants. We conducted interviews with 11 participants: 6 con-
sumer protection experts 15 and 5 end-users. 15Fourofthemweredif-
The consumer protection experts were volunteers from the consumer ferent from the 4 per-
sons we interviewed to
protection department of the ACPR, the French regulatory authority for
design the Robex algo-
bankingandinsuranceserviceswithwhomwecollaboratedforthisstudy.
rithm.
All participants had strong experience in auditing insurance providers
3 10
(from to more than years). Their expertise and role is to verify that
insurancedistributorsrespect"therulesintendedtoensuretheprotection

empowering customers of robo advisors with explainability 165
-
of the customers" as well as the "adequacy of the means and procedures
which they implement for this purpose" and to promote fair commer-
16
cial practices among industrial professionals . Half of them had some 16https://acpr.banqu
experience in supervising robo-advisors. e-france.fr/en/custom
The novice users were volunteer doctoral students recruited through er-protection/profes
sionals/customer-pro
the network of the university with which the authors are affiliated. All
tection-principles
participants received a consent form informing them of the study objec-
tives and identified risks. All participants were volunteers, not compen-
sated, recruited through an email describing the objective and duration
of the experiment. An ethics committee was not required for this study.
Inductive content analysis. We conducted an inductive [Elo and Kyn-
2008
gäs, ]contentanalysisofthedetailednotestakenbyoneauthordur-
ingtheinterviewswithsupervisorsandend-users. Oneauthoridentified
concepts and themes about the characteristics of the explanations that
emerged from reading the interview notes. First, the author observed
thatparticipantstalkedmainlyabouteithertheexplanationimplementa-
tion or the explanation’s purpose (notably with discussion around risk).
Onthisbasis,differentthemesforeitherexplanations’format/contentor
explanations’ purpose could be derived that encompass most of the con-
cepts mentioned by participants. The translation from French to English
was done after the final categorization.

166 the explanation paradox and the human centric path
-
5.4 Study 1 Results
5.4.1 Understanding explanation needs from two perspec-
tives
We grouped the main identified themes of the explanation require-
ments according to their connection to the format or content of the ex-
planation. Through the supervisor’s view, we were able to gather do-
main perspectives that end users alone would not necessarily have pro-
vided, such as understanding the interests of different stakeholders and
potential misalignment, where the vulnerability of certain users can be
exploited, or the wide range of best practices seen for recommendations
and explanations. Conversely, the end-users’ perspective reminds us of
what clients truly care about, regardless of existing regulations. While
the main focus of the supervisors was on the notion of risk, the main
concern of the users was not as clear. For some, it was the performance
of the proposed contract, for others the reliability of the robo-advisor,
and for others, the risk. We discuss below some themes that emerged
from both perspectives.
5.4.2 Redesign principles drawn from the co-design sessions
Give more precise explanations. The supervisors reported an increas-
ing trend for automated online robo-advisors, and a lack of "good" au-
tomated explanations to support those tools. Current robo-advisors’ ex-
planations were seen as very "generic" and "nebulous" in general. One
of the reasons is the use by many brokers of a third-party software to
produce explanations and recommendations, over which they have little
control. Supervisors also reported the difficulty for brokers to produce
explanations with the increasing complexity of their tools: "There’s too
much complexity even for them." This highlights the relevance of the
XAI domain to help solve real-world problems, even when the underly-
ing recommendation system is AI but rule-based.
Inform customers of the risk. The supervisors insisted on the impor-
tance of explanations as a safeguard to inform customers about risk, tak-
ing as an example cases of overestimation of the risk for vulnerable peo-
ple. Supervisors used to phrase "prise décision éclairée", which can be
translated literally into English as "enlightened decision-making", to de-
scribetheaimoftheexplanations. ThisFrenchphraseconveysastronger
notion of user empowerment than "informed choice".
Rule-based algorithm improvement. The supervisors we interviewed
also gave us feedback on the rule-based algorithm that we developed.
Duringalgorithmtesting, theydeliberatelysimulatedspecificvulnerable
user profiles to verify that Robex’s recommendation was low-risk. This
enable us to add several exceptions to our rules such as if users’ risk
0 7
appetite is / , redirect the user to the most secure proposal regardless

empowering customers of robo advisors with explainability 167
-
| Explanation | Supervisorview |     |     | End-userview |     |     |
| ----------- | -------------- | --- | --- | ------------ | --- | --- |
aspect
Format
Schematic "schematic", "graphics and diagrams [for "Iwanttoseethescaleoftherisk,andwhere
|     | noviceusers]","playful","step-by-step" |     |     | I’mplacedonthatscale" |     |     |
| --- | -------------------------------------- | --- | --- | --------------------- | --- | --- |
Content
Synthetic vs. short, simple, readable, "[Explanations] are a simple, "Something that tells you "this is re-
vs.
exhaustive sort of synthesis", "clean and clear" ex- allythepointsyouneedtoknow""
haustive,"Justputtingasentence"considering
|     | this and          | that..." is not enough", | give links | to  |     |     |
| --- | ----------------- | ------------------------ | ---------- | --- | --- | --- |
|     | more information, | give enough              | documenta- |     |     |     |
tion
Adapted vo- "adapt vocabulary", "not too much text", "usesimplifiedlanguage,notthelanguageof
cabulary "avoidfinancialjargon" a banker", "need to have more familiar lan-
guage","I’mnotsurewhataplacementis"
Purpose
Justify linkusercharacteristicsandproduct, "justifi- "Why are you making this recommendation?
cation","realneedoftransparency"motivated Whatfactorsareyoubasingiton?","Iwantan
bymisalignmentofinterestbetweeninsurers explanationonlyifthereisadisagreement."
andclients,prevent"scams","whatitisbased
on?"
Warn control, notify, warn, inform, "tendency to "What are the risks?", "How much do I con-
50,000
underestimate [the risk]", "Explanations are cretely risk losing on the I put in?",
useful because there is a risk.", "the [hu- "WhatcanIexpectintermsofrisksandben-
|     | man]advisorwillnotsayeverything","robo- |                   |              | efits?" |     |     |
| --- | --------------------------------------- | ----------------- | ------------ | ------- | --- | --- |
|     | advisors                                | don’t have enough | safeguards", |         |     |     |
"makethem[theusers]understandthatthere
|     | is a step | to take, make them | question | "do I |     |     |
| --- | --------- | ------------------ | -------- | ----- | --- | --- |
agree?""
| Engageusers |     |     |     | "It looks | boring", "I’ll open | them [the links] |
| ----------- | --- | --- | --- | --------- | ------------------- | ---------------- |
andprobablynotlookatthem."
Teach enable users to have answers to their follow- "Idon’tknowanythingaboutthat.","Ineither
|     | upquestions |     |     | agree nor | disagree because I       | don’t really un- |
| --- | ----------- | --- | --- | --------- | ------------------------ | ---------------- |
|     |             |     |     | derstand  | this financial concept", | "I don’t un-     |
derstandthisfield"
|     |     |     |     |     | Table | 5.2: Main themes |
| --- | --- | --- | --- | --- | ----- | ---------------- |
of the other parameters, and if the objective is to protect my savings, cap
|     |     |     |     |     | emerging | from the con- |
| --- | --- | --- | --- | --- | -------- | ------------- |
the recommendation at the second safest. tent analysis of supervi-
sorsandend-usersinter-
| Supportuserengagementandlearning. |     |     |     |     | views,withcorrespond- |     |
| --------------------------------- | --- | --- | --- | --- | --------------------- | --- |
Althoughwecouldgroupboth
inglexicalfieldandcita-
supervisorandend-userperspectivesintocommonthemes,somethemes
tions.
were discussed more by one group. For example, end-users expressed
their need to be engaged—some felt either overwhelmed or bored by
the topic. supervisors talked about the need for complete information
although end-users insisted on their need for simple, easy-to-digest in-
formation, that used simple vocabulary. One participant said that he
found it difficult to understand what the numbers or ranged used in the
explanations represented because he had no concept of scale in this area.
For example, it was difficult to make sense of "less than 30 % of my as-
sets". Is that a small, a large portion? This makes it difficult to assess
explanations.

168 the explanation paradox and the human centric path
-
Find the balance between text and graphics. One of the themes we
found was the need for schematic explanations on the one hand and
the need for more human explanations that can answer a wide range
of users’ questions on the other. Two supervisors very much appreci-
ated our graphical, Shapley-based explanations, finding they had never
seen something like that in the market and that it responded well to the
need to link users’ characteristics to the recommended product. How-
ever, many—supervisors and end-users alike—indicated their need to be
abletochatwithahumancounsellordespitetheexplanation. Asupervi-
sor also imagined explanations could look more like a Frequently Asked
Questions menu and a participant said "I can imagine a chatbot with
someone behind it who can answer my questions." This led us to try to
2021
balance between text and graphics, following Szymanski et al. [ ]’s
findings, and to compare more "conversational" or more "graphical" ex-
planations in the next study.
Clarify visually and accurately the feature’s impact. Some partici-
pants commented that it was quite difficult to understand what the two
columns represented. They would have liked more visual clues, with ar-
rowsasintheoriginalShapexplanation, toindicatethedirectionofeach
feature’s effect. One participant also expressed that she would trust an
explanation that correctly scaled the effects of each impact.
Redesign specifications. Based on the legal requirements for explana-
tions and the analysis of supervisors’ and end-users’ expressed needs,
we derived the following elements for the redesign of our explanations.
• Risk of the recommendation. We added the risk score of each user from
the rule-based algorithm of Robex, and reported it on a scale of one
to five to make it correspond to the five recommendations. We added
the user risk score and risk scale below the visualisations of the five
recommendations.
• Important Definitions. As highlighted by end-users and supervisors in
1 2022
Study , and by prior work [Bove et al., ], it is essential to give the
minimalbackgroundknowledgenecessarytounderstandthefinancial
conceptsusedintherecommendationsandexplanations. Wetherefore
provided on-demand definitions for all important financial concepts
through information buttons.
• Vocabulary. As pointed out by a non-expert participant, we simplified
the vocabulary used in the text. Initially, it contained some financial
jargon that we had learned from our informal talks with regulatory
supervisors.
• Descriptions of the effect of complex user input parameters. Robex used
five user input parameters: "Your risk appetite", "Your level of finan-
cial knowledge", "the amount to invest proportionally to your total
financial assets", "Your financial objective" and "The portion of your
financial assets already invested". Out of those five parameters, we
1
saw in Study that the last three were more complex to interpret. For

empowering customers of robo advisors with explainability 169
-
eachoftheseconcepts,weprovided( 1 )theeffectitshouldhaveonthe
proposition—either lower or increase the risk the customer can take—
( 2 ) an indication of the magnitude of the user’s input (e.g. " 75 % is a
56
| very big | portion"). | An example | is shown | in Figure . . |
| -------- | ---------- | ---------- | -------- | ------------- |
• Directionandscaleoftheimpactoffeatures. We have converted our origi-
nal tabular visualisation into a tornado plot to make the direction and
| scale of | the features’ | impact | clearer. |     |
| -------- | ------------- | ------ | -------- | --- |
2
Study tests two additional formats to explore the optimal balance
betweentextandgraphics: aninteractivegraphicalformatandachatbot-
| style dialogic | format | with a | few graphical | cues. |
| -------------- | ------ | ------ | ------------- | ----- |

170 the explanation paradox and the human centric path
-
5.5 Study 2 Methodology: A deception-based between-
subjects experiment
1
In this study, we expand upon the results of Study to examine the
usefulness of legally required feature-based explanations in the context
of life insurance to help lay users appropriately rely on robo-advisor rec-
ommendations. Specifically, we conduct a between-subjects experiment
with deception to test for overtrust and overreliance effects. Below we
describe the design of the quantitative study, explaining the rationale for
2 4
the use of a x factorial design and a between subject crowd-sourced
survey.
5.5.1 A 2x4 factorial design
Experimental conditions. We used the results of Study 1 to refine the
original Robex explanation prototypes and to create different explana-
1
tion conditions for comparative evaluation. Study led us to question
the right balance between text and graphics. Additionally, we build on
4
the findings of the explainability literature presented in Chapter , ac-
cording to which interactivity improves the usefulness of explanations.
Specifically,wewanttotesttwotypesofinteractionidentifiedinourtax-
onomy: "simulate" and "ask" interactions, which have not been directly
compared in the existing literature. Therefore, our explanation condi-
tions vary in terms of interactivity and balance between visuals and text.
In this quantitative analysis, we examined four distinct explanation con-
ditions.
1 . Control. Some participants did not receive any explanation. They
served as our control condition.
2 . Graphical-static. The "graphical" explanation we had initially proto-
1
typed for Study was improved based on participants’ feedback and
53
the redesign specifications outlined in Section . .
3 . Graphical-mutable. Weimplementedaversionofthegraphicalexplana-
tion where user could change a few parameters that were actionable
such as investment amount, objective and portion of assets invested
eleswhere. This interaction corresponds to the "mutate / simulate"
4
interaction described in our interaction taxonomy in Chapter .
4 . Dialogic. As somme end users and supervisors compared Robex’s
explanations to those of a human advisor, we also designed more
human-like explanations, i.e."dialogic" ones. This approach has been
adopted in previous XAI work by [Hernandez-Bocanegra and Ziegler,
2021 2021
, Hepenstal et al., ] for "conversational" explanations. It cor-
respondsto the"ask" interactioninour taxonomy. Thedialogues were
not responses to free text input from the user, but responses to pre-
defined questions. The user would first see the list of these predefined
questions formatted like individual SMS text on the user side of the
conversation (in blue) and could click on any of these questions to see

empowering customers of robo advisors with explainability 171
-
the answer on the Robex side of the conversation (in grey). The an-
swers to each predefined question was also predefined but adapted to
the user’s characteristics and recommendations. After having clicked
on a question, the user could click on any of the remaining predefined
questions.
Participants were divided into four groups corresponding to these
four different interfaces. The same contextual information was delivered
across all the different explanation conditions.
Figure 5.6: Explanation
interfacesforeachofthe
condition A "Graphical-
static": users see a
graphical summary of
howtheircharacteristics
impact the risk of the
proposal. Translated
fromFrenchtoEnglish.
Additionally, as we wanted to test for overreliance and overtrust, we
introduced deceptive recommendations as an experimental condition.
The objective was to compare the ability of users of different interfaces
to detect a crude recommendation error. Each of the four explanation
groups described above was divided in two:
1 . Reliable recommendation. One group received a correct recommenda-
tion. These were delivered through the building of a rule-based
2 . Deceptive recommendation. The other group a false recommendation.
The false recommendation was produced by altering the score-based
algorithmsothattherecommendationwaseithermuchtooriskyorre-
ally not risky enough. This was done by altering the initial user’s risk
50
score calculated by Robex by a roughly % change. The direction of
the change was so that more-than average risk-takers were redirected
to low-risk proposals and vice versa. For example, if a participant was
recommended "Securimax" by the normal Robex algorithm, her risk-
score would be increased artificially so as to output the "Flexiplus"
recommendation. On the contrary, participants for whom the initial
correct recommendation was the more risky "Flexiplus" would be rec-
ommended the more conservative "Securimax" product. For partici-
pants who initially got the "Flexi" recommendation, if their risk-score

| 172 the | explanation |     | paradox | and | the | human | centric |     | path |
| ------- | ----------- | --- | ------- | --- | --- | ----- | ------- | --- | ---- |
-
5.7:
Figure Explanation
interfacesforeachofthe
condition B "Graphical-
mutable": users first see
the graphical-static in-
terface and then a pop-
up message indicates
they can change some
of their characteristic.
Translated from French
toEnglish.
|     |       | 12   |              |     |          | 21  |           |            |     |
| --- | ----- | ---- | ------------ | --- | -------- | --- | --------- | ---------- | --- |
| was | below | —out | of a maximum |     | score of | —,  | they were | redirected |     |
to "Dynamo" and for risk-scores above 12 , to "Securimax". The modi-
2
| fied | Robex | algorithm | is presented | in  | the appendix |     | B . |     |     |
| ---- | ----- | --------- | ------------ | --- | ------------ | --- | --- | --- | --- |
The explanations of the false recommendation were produced in the
same way as the correct recommendations, using agnostic SHAP feature
importances based on the skewed Robex algorithm. As a result, the ex-
planations for false recommendations were illogical, such as "Your risk
1 7
appetite: low ( / ) contributed to increase the risk of the recommenda-
| tion" cf. | Figure | 5 . 9 . |     |     |     |     |     |     |     |
| --------- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
Measures. Building on prior work conducting empirical studies to
|                                  |     |     |     | 2021 |        | 2021 |            | 2021 |      |
| -------------------------------- | --- | --- | --- | ---- | ------ | ---- | ---------- | ---- | ---- |
| evaluateXAIsystems[Buçincaetal., |     |     |     |      | ,Shin, |      | ,Laietal., |      | ,Liu |
et al., 2021 ], we measured the concepts described below. We tested the
Cronbach’salpha’sforthedifferentsetsofquestionstoverifytheinternal
consistencyofthequestionsaskedforeachdimension. Thequestionsare
| reported | in Table | 53 . | .   |     |     |     |     |     |     |
| -------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
• Reliance. Reliancewasmeasuredbyaskingparticipantsiftheythought
the robo-advisor’s recommendation was adapted to their need or not.
We were able to measure overreliance when the participant followed
| an incorrect |     | recommendation. |     |     |     |     |     |     |     |
| ------------ | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
• Trust. Trust was measured through the five question items from the
benevolence and competence aspects of McKnight’s framework [McK-
night et al., 2002 ]. One item was added to measure if participants felt
the need for any additional human advice. overtrust occurred when
| the participant |     | trusted | an incorrect |     | recommendation. |     |     |     |     |
| --------------- | --- | ------- | ------------ | --- | --------------- | --- | --- | --- | --- |
• Cognitive load. Cognitive load was measured through the mental de-
| mand | and | effort items | of the NASA-TLX |     | Index. |     |     |     |     |
| ---- | --- | ------------ | --------------- | --- | ------ | --- | --- | --- | --- |

empowering customers of robo advisors with explainability 173
-
Figure 5.8: Explanation
interfacesforeachofthe
condition C "Dialogic":
the same information
provided in the inter-
faces A and B)is deliv-
ered through "sms-like"
textual messages. Some
graphics are added to
facilitate the visualisa-
tion of the risk and of
the variables decreasing
and increasing the risk
of the proposal. Trans-
latedfromFrenchtoEn-
glish.

| 174 the | explanation | paradox | and the human | centric path |     |     |
| ------- | ----------- | ------- | ------------- | ------------ | --- | --- |
-
• Userengagement. Three user engagement question items were adapted 5.9:
|     |     |     |     |     | Figure Explana- |     |
| --- | --- | --- | --- | --- | --------------- | --- |
2015
from O’Brien and Cairns [ ]’s framework. Two items were taken tion interfaces examples
|     |     |     |     |     | for an incorrect | rec- |
| --- | --- | --- | --- | --- | ---------------- | ---- |
from the Felt Involvment (FI) category and one from the Novelty cate-
|     |     |     |     |     | ommendation for | each |
| --- | --- | --- | --- | --- | --------------- | ---- |
gory (NO).
|     |     |     |     |     | of the three conditions: |     |
| --- | --- | --- | --- | --- | ------------------------ | --- |
|     |     |     |     |     | A’ "Graphical-static";   | B’  |
• Objective understanding. Understanding of the recommendation on the
|     |     |     |     |     | "Graphical-mutable"; | C’  |
| --- | --- | --- | --- | --- | -------------------- | --- |
onehandandunderstandingoftheexplanationontheotherweremea-
|     |     |     |     |     | "Dialogic". The | correct |
| --- | --- | --- | --- | --- | --------------- | ------- |
sured through "test" questions. The question about the recommenda- user profile in this case
|     |     |     |     |     | would have been | "Se- |
| --- | --- | --- | --- | --- | --------------- | ---- |
tion was developed by the authors relying on their knowledge of the
|     |     |     |     |     | cure", but the | skewed |
| --- | --- | --- | --- | --- | -------------- | ------ |
field and discussions with experts. To measure understanding of the
|     |     |     |     |     | Robex algorithm | out- |
| --- | --- | --- | --- | --- | --------------- | ---- |
explanation, we used three questions to test if they understood the di-
|     |     |     |     |     | puts "Dynamo". | Only |
| --- | --- | --- | --- | --- | -------------- | ---- |
rection of the impact of some user inputs, as seen in prior XAI work
|     |     |     |     |     | A’ is translated | from |
| --- | --- | --- | --- | --- | ---------------- | ---- |
2021
| [Szymanski | et al., | ].  |     |     | French to English,   | the  |
| ---------- | ------- | --- | --- | --- | -------------------- | ---- |
|            |         |     |     |     | rest are in original | lan- |
guage.

empowering customers of robo advisors with explainability 175
-
| Measure | Questionswith[possibleresponses] |     |     |     |     |     |     | Cronbach’s |
| ------- | -------------------------------- | --- | --- | --- | --- | --- | --- | ---------- |
alpha
Understanding of Whatisyourestimateoftheeurofundpercentageintheproposalthat NA
| recommendation | wasmadetoyou? | [Severalproposals] |     |      |             |       |        |       |
| -------------- | ------------- | ------------------ | --- | ---- | ----------- | ----- | ------ | ----- |
|                | On a scale    | of 1 to 5 (5 being | the | most | risky), how | risky | do you | think |
theRobexproposalis?
|     | What is   | special about a | euro fund? | [it       | offers   | a high | expectation | of    |
| --- | --------- | --------------- | ---------- | --------- | -------- | ------ | ----------- | ----- |
|     | gains for | a high risk of  | loss, it   | is mostly | composed |        | of actions, | it is |
guaranteedbytheinsurer,Idonotknow]
Understanding of Of your characteristics and goals, which factor weighed the most in NA
| explanation | theproposalthealgorithmofferedyou? |                 |                             |           | [Severalproposals] |          |          |         |
| ----------- | ---------------------------------- | --------------- | --------------------------- | --------- | ------------------ | -------- | -------- | ------- |
|             | How did                            | the proportion  | of your                     | financial | assets             | already  | invested | in      |
|             | risky financial                    | products,       | which                       | is for    | you ... ,          | impacted | the      | risk of |
|             | proposalmadebyRobex?               |                 | [Increase/decrease/neutral] |           |                    |          |          |         |
|             | How did                            | your investment | objective,                  | which     | is ...             | impacted | the      | risk of |
theproposalmadebyRobex?
| Trust-Benevolence | IthinkRobexisactinginmybestinterest |     |     |     |     |     |     | 0.854 |
| ----------------- | ----------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
Robexwantstounderstandmyneedsandpreferences
Trust-Competence Robex is skilled and effective in providing life insurance recommen-
dations
|     | Robexhastheexpertisetounderstandmyneedsandpreferences |     |     |     |     |     |     | 0.878 |
| --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
Robexisfulfillingitsroleasalifeinsuranceadvisorverywell
Trust-Other (not Iwouldneedahumanadvisortohelpmechoosealifeinsuranceplan Notused
used)
| Userengagement | Ifeltinvolvedinmytaskofchoosingalifeinsuranceplan |     |     |     |     |     |     |     |
| -------------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
0.818
|     | The content | of the life | insurance | recommendation |     | site | has attracted |     |
| --- | ----------- | ----------- | --------- | -------------- | --- | ---- | ------------- | --- |
mycuriosity
Iwasinterestedintheexperience
0.829
Cognitiveload Ifounditmentallydemandingtoreadandunderstandtheproposed
lifeinsuranceformula
|     | I had to | make an effort | to read | and understand |     | the proposed |     | life in- |
| --- | -------- | -------------- | ------- | -------------- | --- | ------------ | --- | -------- |
suranceformula
Table5.3: Questionused
|     |     |     |     |     |     |     |     | for measuring different |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------- |
|     |     |     |     |     |     |     |     | metrics with Cronbach   |
|     |     |     |     |     |     |     |     | alphas (translated from |
FrenchtoEnglish).

| 176 the | explanation | paradox | and the human | centric path |     |     |
| ------- | ----------- | ------- | ------------- | ------------ | --- | --- |
-
| 5.5.2 | Survey | procedure | and analysis |     |     |     |
| ----- | ------ | --------- | ------------ | --- | --- | --- |
5.10:
|     |     |     |     |     | Figure       | The work-    |
| --- | --- | --- | --- | --- | ------------ | ------------ |
|     |     |     |     |     | flow of our  | quantitative |
|     |     |     |     |     | experiments. | The pro-     |
Procedure. Ourgoalwastotargetparticipantswhomightbelifeinsur- filing questionnaire is
ance robo-advisor users. As participants were crowd-sourced, we began used to produce a per-
with a selective question to filter out users who were not likely to be sonalized recommenda-
|     |     |     |     |     | tion of a life-insurance |     |
| --- | --- | --- | --- | --- | ------------------------ | --- |
users of life-insurance in the near or distant future. The question used
|     |     |     |     |     | contract. | Clients can |
| --- | --- | --- | --- | --- | --------- | ----------- |
was "To begin with, we would like to know how you feel about life in-
|     |     |     |     |     | review the | recommen- |
| --- | --- | --- | --- | --- | ---------- | --------- |
1
surance: - I might sign up (for the first time or again) to life insurance dation, the explanation
in the near or distant future. / 2 - I am not considering signing up (for and then decide to fol-
thefirsttimeoragain)tolifeinsuranceinthenearordistantfuture,even low the recommenda-
tionornot.
though I’m curious to find out more on the subject." The answers were
formulated so that it was not obvious to guess which answer to select to
beabletocontinue. Onlyparticipantswhocheckedthefirstanswerwere
selected to continue. On the crowd-sourcing platform, participants were
asked about their highest level of education and gender. Participants
were redirected to Robex and provided with an overview of the study.
They were asked to provide their consent to participate and then under-
went an attention check. The two following steps in the study process
replicate what we can see in existing robo-advisors: a profiling question-
naire followed by recommendation page. Participants had to go through
the profiling questionnaire. They were then distributed randomly in our
510
eight different conditions as shown in Figure . , which illustrates the
experimental workflow. They read through their user profile summary
at the top of the page, the description of the recommendation. If appli-
cable, they saw an explanation of why this recommendation was made
to them, and then they had to choose whether to accept or reject the pro-
posed life-insurance plan. We also collected their qualitative feedback
about explanations through a short free-text field. Finally, a two-page
post-questionnaire measured their understanding, workload, trust and
| engagement | in using | Robex. |     |     |     |     |
| ---------- | -------- | ------ | --- | --- | --- | --- |
The whole study lasted around 10 minutes. Participants were paid
3€5017
around for completing the study. We randomly assigned partici- 17Lucid goes through
|     |     |     |     |     | several suppliers | to  |
| --- | --- | --- | --- | --- | ----------------- | --- |
pants to an experimental condition until we had reached a minimum of
30 participants in each of our eight conditions. gather participants.
|     |     |     |     | 5   | Each supplier | receives |
| --- | --- | --- | --- | --- | ------------- | -------- |
Participants who failed attention checks, took less than minutes or 3.50€
|     |     |     |     |     | for | each study |
| --- | --- | --- | --- | --- | --- | ---------- |
wrote non-serious content (repeated keyboard strokes, clearly ironical or
completed,takesacom-
|     |     |     |     |     | mission and | pays the |
| --- | --- | --- | --- | --- | ----------- | -------- |
resttotheparticipant.

empowering customers of robo advisors with explainability 177
-
insulting content) in the free-text field were excluded. We also imple-
mented time counters: participants could not continue to next page if a
(small) minimum amount of time had not elapsed. In addition, on the
recommendation page, we set time counters for each of the three sec-
tions of the page: profile summary, recommendation and explanation.
The time thresholds were calibrated to correspond to a quick reading of
each section. After the time had elapsed, a button appeared to say "OK
continue"or"Showrecommendation". Thesetimecountersthereforealso
served as a way to gradually disclose content and avoid cognitive over-
2019
load [Springer and Whittaker, ]. This was to make sure that partici-
pantsreadthroughtheprofilingquestionnaire, therecommendationand
32
the explanation. We ended up with participants in each condition.
At the end of the survey, participants in the deceptive condition were
informed that they had received a wrong recommendation. All partic-
ipants were reminded that the financial advice presented was fictitious
and non-relevant for their personal needs. The study was approved by
an academic research ethics committee.
Participants. French workers between 18 and 65 years old were re-
18
cruited online through the platform Lucid . Of the study respondents 18https://lucid.co/
73 27
thatwerefinallyincludedinthesurvey, %werefemaleand %male—
although some participants did not provide any answer to that question.
61
% had an undergraduate or a graduate degree (Bachelor, Master, Doc-
torate and other specialized education). We cannot explain the skew
towards women participants but it is possible that more male partic-
ipants did not want to answer this demographic question or that our
filters about the interest in life-insurance or seriousness of the responses
excluded more male participants. Participants had an average financial
13 5
knowledge score of . out of , and were therefore for the most part
representative of non-expert users. Financial knowledge was measured
in the pre-questionnaire through specific questions written with the help
of four supervisors from the French Regulation Authority of financial
services (cf. Table 5 . 1 for the detail of the questions).
Analysis. Forallevaluationmeasures,weranatwo-wayANOVAanal-
ysiswiththeexplanationconditionsandtherecommendationconditions
(correct or false) as the independent variables. Our eight groups had a
32
minimumof participantsinordertoconfidentlymeetsamplesizecon-
siderations for ANOVA. For groups that had more participants, we ran-
32
domly selected responses. When significant, we conducted post-hoc
Tukey’s HSD test for pairwise comparisons. We used the Shapiro-Wilk
test to check that the assumptions for ANOVA were met and the Bartlett
test to verify the homogeneity of variances. We also controlled for socio-
demographic confounding factors: education, age, and gender as control
variables, although this data variables was incomplete.

178 the explanation paradox and the human centric path
-
5.6 Study 2 Results
Figure 5.11: Results
for Study 2. Vertical
All Cronbach’s alphas for the different sets of questions were signifi- lines represent the 95%
cant, except for trust: we had to remove the question about the human confidence interval.
advisor(weinitiallythoughtthisquestioncouldberelatedtotrustinthe Asterisks and dots
indicate the statistical
robo-advisor,asitmeasuredtrustina(human)advisor,butitwasafalse
significance of the re-
intuition). Foralltheevaluationmeasures,theresidualsoftheregression sults: ***p-value≤0.001,
showed a near-normal distribution, as confirmed by the Shapiro-Wilk ** p-value≤0.01, *
test, validating the assumptions for ANOVA. Additionally, the Bartlett p-value≤0.05, • p-
test indicated that variances were homogeneous. value≤0.07, "ns" non
significant.
5.6.1 Explanations do not help to better calibrate trust
We found that the no-explanation control group was more or equally
likely to distinguish between good and bad advice than the explanation
0001
groups. We found a statistically significant difference in trust (p= . )
001
and reliance (p= . ) between the no-explanation control group that re-
ceived a correct proposal and the no-explanation control group that re-
ceived an incorrect one. However, we did not always observe this with
participants who received explanations. Specifically, there was no statis-
tical difference in trust and reliance on the advice between the dialogic
explanation group that received a correct recommendation and the di-
alogic explanation group that received and incorrect recommendation.
For the graphic-mutable explanation, we found participants were able to
calibrate their reliance on the advice between the incorrect and correct
003
proposal (p= . ), but not their trust. In the graphic-static explanation
condition,peopletrustedacorrectpropositionsignificantlymorethanan
005
incorrect one (p-value= . ) and relied on the correct proposition almost
0064
but not significantly more (p= . ) than on the incorrect one. Overall,

empowering customers of robo advisors with explainability 179
-
out of those three explanations, it may be the graph-mutable explana-
tion that performed best, because it enabled partcipants to appropriately
calibrate their demonstrated trust, i.e. reliance on the recommendation.
However, none of the explanations outperformed the control condition
in appropriately calibrating trust and reliance.
5.6.2 Dialogic explanations increase subjective trust
We found that users who were shown an incorrect recommendation
and a dialogic explanation trusted significantly more the robo-advice
0001
compared to the no-explanation group (p= . ). Further, we found that
participants in the incorrect recommendation and dialogic explanation
0068
condition were almost significantly (p= . ) more likely to rely on the
incorrectrobo-advicethanparticipantsintheincorrect/controlcondition.
5.6.3 Dialogicorgraphicalexplanationsdonotimproveuser
understanding
The different explanation formats did not improve users’ understand-
1
ingoftherecommendationandmorespecificallyitsrisk—question out
3 53
of measuringrecommendationunderstanding(cf.. Table . ). Basedon
511
the graphs in Figure . , there appears to be a tendency for graphical-
mutable explanations to lead to better understanding of the recommen-
01
dation than other conditions, but the effect was not significant (p= . ).
Further, the level of understanding of the explanations was compara-
ble across the different explanation conditions. However, people in the
deceptiveconditionsweresignificantlylesslikelytounderstandthechar-
0001
acteristics of the recommendation and the explanations (p= . ). This
resultisbasedonone-wayANOVAwithsolelytherecommendationcon-
dition (correct or false) as the independent variable.
This evidences that people are less likely to understand a recommen-
dation that is not suited to their needs, or that they did not expect.
5.6.4 Explanations do not affect cognitive load and user en-
gagement
We do not find any statistically significant effect for the different ex-
planationconditionsonusers’subjectivecognitiveloadanduserengage-
ment. This finding contradicts other work on the cognitive cost of expla-
2022
nation[Vasconcelosetal., ]. Perhapsthisisthecaseherebecauseun-
derstanding financial recommendations is already cognitively demand-
ing enough due to the complexity of the field, and the cost of adding
explanations is negligible in comparison—average perceived cognitive
56 10
workload for using the robo-advisor was . out of . The "simulate"
and "ask" interactions did not improve users’ subjective engagement in
the task. This may also be explained by the seriousness and unamusing
nature of this specific task in the finance domain.

180 the explanation paradox and the human centric path
-
5.6.5 Higher levels of education reduce overreliance
512
AsshowninFigure . ,weconductedanadditionalanalysistostudy
the effects of education. Indeed, while controlling for confounding fac-
tors, we had noticed that education could play a role in trust and un-
derstanding of the recommendation. The original categorical data col-
lected on the education crowdsourcing platform included eight different
68
categories representing levels of education in French. participants
256
out of respondants did not provide their education levels. We cre-
ated larger groups by combining educational levels equal to or less than
the "Baccalauréat", which is the equivalent of a high school diploma in
France. Educational levels one to three years after the Baccalauréat were
grouped together. Masters and doctorates, corresponding to more than
four years of education after the Baccalauréat, formed a third group. To
runatwo-wayANOVAwitheducation(threegroups)andrecommenda-
tion conditions (two groups) as independent variables, we checked the
minimum number of participants in these six groups m and randomly
selected participants in the largest groups to form six groups of size m =
20. The results from the two-way ANOVA indicated that participants in
the highest education level group tended to rely significantly less on the
005
wrong recommendation compared to the correct one (p= . ). This indi-
cates that education plays a role in critical thinking and ability to exhibit
a healthy dose of skepticism. In addition, we found that participants in
the lowest educational group understood the incorrect recommendation
003
significantly less than the correct one (p= . ).
Figure 5.12: Effects of
education on reliance,
understanding of the
recommendation and of
theexplanation.

empowering customers of robo advisors with explainability 181
-
5.7 Discussion
5.7.1 Dialogic vs. Graphical explanations
2019
According to Miller [ ], explanations are best provided through a
social process, i.e. a conversation, because it matches the way humans
explain things. In fact, "dialogic" explanations have been favorably pre-
sented in the XAI literature. For example, Hernandez-Bocanegra and
2021
Ziegler [ ] presented how dialogic management systems can respond
to users’ questions about a hotel recommender system, and Hepenstal
2021
et al. [ ] showed how conversational explanations can be useful for
criminal investigators. While the benefits of dialogic explanations might
be real regarding user satisfaction and explanation usefulness in some
2021 2021
contexts[Hernandez-BocanegraandZiegler, ,Hepenstaletal., ],
our results, in turn, shed light on the overtrust downside of "dialogic"
explanations for clients of online recommender systems. It is possible
that either the "humanness" of the dialogic explanation we presented, or
the familiarity of users with chats, made them more inclined to accept
robo-advice. In fact, some people might see the anthropomorphisation
of systems as suspicious. One of our end-user participants in the pilot
Study said that "It’s quite a lot of anthropomorphization". This is consistent
2021
with the study by Hepenstal et al. [ ] in which participants were un-
comfortable with the humanness of the XAI agent and wanted to have it
clear that they were not talking to a real person. Our findings also qual-
2021
ifySzymanskietal.[ ]’sresultsaccordingtowhichparticipantsprefer
graphical explanations but understand textual explanations better. The
authors further advance that hybrid textual and graphical formats could
improve both user satisfaction and understanding. Our study qualifies
this result by showing that users made less mistakes with graphical for-
mats which presented small amounts of text than with dialogic formats
with small amounts of graphical visualizations. This contrasts with Szy-
2021
manskiet al.[ ]’sfinding thattext isbetter understood—howeverthe
textualexplanationsinthisworkweremuchshorter. Perhapsthebrevity
and the synthetic aspect of our graphic explanations compared to the
dialogic explanations were instrumental in improving users’ appropriate
reliance.
5.7.2 Legal requirements for feature-based explanations
In this study, we showed how legal requirements to justify investment
advice based on client’s features may take shape using a classical XAI
method (SHAP) and various explanation representations. We further
found that the legal sub-objectives of the explanation that we defined
523
in Section . . to help users make "fully informed" decisions were not
1
fully achieved. Users were not better able to ) appropriately rely on the
2 3
recommendation, )understandtherecommendationor )appropriately
calibrate their trust in the robo-advisor compared to the control condi-
tion.

182 the explanation paradox and the human centric path
-
523
As noted in Section . . , the objective of the law requiring insurance
intermediaries to specify in writing "the reasons for the appropriate-
ness of the proposed contract" is also to discipline brokers by making
non-objective, self-interested, recommendations more visible and pun-
ishable. Feature-based explanations are therefore not useless, because
they at least serve the purpose of disciplining insurance intermediaries
by forcing them to show how the proposed product corresponds to the
customer’s risk profile.
However, our work changes the perspective on the benefit of explana-
tionsforcustomers’understandingandreliance. Explanationsarenotal-
ways"allgood",theymustbedesignedsothatovertrustandoverreliance
effects are mitigated. If the explanation formats we presented could not
meet the legal objectives we highlighted, future work could address how
to design explanations that are cognitively engaging for lay-users. We
72 7
develop this in Section . of Chapter .
5.8 Limitations
This work has some limitations. First, the content analysis in Study
1
was performed based on the detailed notes that one author took dur-
ing the interviews, which may have limited the amount and breadth of
captured input from participants. In addition, the non-expert partici-
pants from the qualitative study were graduate students, who represent
a very specific sample of non-expert users. One of the limitations in our
domain-driven contextual enquiry is that we used a simplified and fic-
tional life-insurance robo-advisor. Some factors such as time horizon,
detailed descriptions of the funds, of their historical performances and
the costs of each contract were not taken into account. We did this to
simplify the building of the tool, and also because we felt adding costs
and performances might have diverted participants’ focus from the risk
of the proposals, which is the most critical information for users to un-
derstandaccordingtosupervisorsandthespiritofthelegislation. Future
work could explore similar research questions with a real robo-advisor.
Additionally, one of the main limitations of crowd-sourcing participants
2
in Study is that they might lack the mental engagement or involve-
ment with the subject. To increase participant engagement, we let them
answer the survey with their own profile, instead of presenting a prede-
fined profile for all participants. We verified that the type of recommen-
dation did not have a significant impact on our measures. Additionally,
we implemented a question to filter out users completely uninterested
in life-insurance, attention checks, text fields and time counters to filter
out non-serious participants. Nevertheless, it is possible that the par-
ticipants in our study were not representative of a real user of a real
life-insurance robo-advisor. Also, the participants in our study were also
73
mainly women ( %).

empowering customers of robo advisors with explainability 183
-
5.9 Conclusion
Inthischapter,wecarriedoutaco-designexperimentaimedatunder-
standing the needs and requirements for explanations in robo-advisors
from the perspectives of non-expert end-users and supervisors in cus-
tomer protection. Based on these findings, we designed various proto-
types of feature-based explanations for online recommendations in life-
insurance, including both interactive and static options. We then pre-
2 4
sented the results of a x between-subjects experiment to investigate
whetherdifferentformatsoffeature-basedexplanationshelpnoviceusers
to appropriately rely on, trust, and understand life insurance plan rec-
ommendations. We found that providing feature-based explanations did
not significantly improve users’ understanding of the recommendation,
or lead to more accurate reliance on the recommendations compared to
having no explanation at all. We also found that explanations provided
in a dialogic format, where users can choose a question and get chatbot-
like text answers, increased users’ trust in the robo-advisor and did not
significantly improve user understanding. This led us to conclude that
graphical formats could be better suited to inform clients. This leaves us
in a quite unsatisfactory state of affairs where the obligation to inform
clients does not fulfill its promises to empower users in better under-
standing the recommendation or in making better decisions. However,
in regulated contexts such as life insurance, regulators and internal com-
pliancesystemsactasbarrierstothemanipulationofusertrust,aheadof
the protection provided by user self-regulation. The ability to detect un-
trustworthy recommendations does not primarily rest on the shoulders
of end-customers.
In the next chapter, we investigate the explanation needs of financial
reguatory supervisors to control the trustworthiness of AI systems.

| 184 the | explanation | paradox | and the human | centric path |
| ------- | ----------- | ------- | ------------- | ------------ |
-

Chapter 6
Understanding the
supervisors’ needs for
explainable AI in
financial crime detection
egulatory supervisors play
R a critical role in ensuring the trust-
worthiness of AI systems and preventing end-customers from having to
detect false AI recommendations. Rather than mere explanations, super-
visors expect "justifications" by regulatees that an AI system or decision
1
complies with a legal standard, rule, or objective . However, little is 1Cf. Section 1.1.5 in
known about the actual needs of supervisors concerning such justifica-
Chapter1foraclarifica-
tion of the terminology
tions of AI systems.
employedandthediffer-
In this chapter, we take another case study in finance: anti-money ences between explana-
laundering and countering financing terrorism (AML-CFT). We take a tionandjustification. As
noted by [Hildebrandt,
dual user-centered and legal approach to describe the explanation needs
2019] and [Henin and
of regulatory supervisors to verify AI compliance with AML-CFT regu- Le Métayer, 2022], justi-
lation. Weexamineasocio-techno-legalsupervisionsysteminAML-CFT fications are extrinsic as
in France, as an example of AI use in a highly-regulated industry. We they refer to norms and
6 regulations.
draw on workshops with supervisors and bank practitioners to outline
the auditing approaches of AML-CFT supervisors. Our findings present
the AML obligations that conflict with AI opacity. We then formulate
seven needs that supervisors have for model justifiability. Finally, we
discuss the role of explanations as reliable evidence on which to base
justifications.
We begin by presenting the related literature and the relevant back-
62
ground in AML-CFT in Section . . We then describe our methods and
63 64
findings in Sections . and . .
ThisstudywasmadepossiblethankstothecollaborationoftheACPR,
theFrenchregulatoryauthorityoffinancialservicesandtheCréditAgri-
cole, a large French bank. The views expressed in this chapter are ex-
clusively those of the authors and the participants of this study in their
personal capacity. They cannot be taken as the views or policies of the
ACPR or Crédit Agricole.

186 the explanation paradox and the human centric path
-
6.1 Motivation and research questions
AI regulation has been rapidly gaining interest due to the advances
2
of generative AI and the emergence of new AI regulations . However, 2Forexample,thedevel-
highly regulated industries, such as banking, healthcare, or the mili- opments of the AI, Dig-
ital Services and Digital
tary, already have structures in place to deal with technological risks.
Markets Acts in Europe
These domains are characterized by well-established norms, experience
andtheAlgorithmicAc-
in putting principles into practice, a common goal of social welfare, and
countability Act in the
2019
robust professional accountability mechanisms [Mittelstadt, ]. In US this year [European
banking, machine learning adoption is on the rise [Financial Conduct Commission, 2021, Eu-
2019 ropean Parliament and
Authority, ], with regulators sometimes encouraging industry play-
Council, 2022, Yvette D.
ers to consider AI to improve the efficiency of their systems [Board of Clarke,2023]
2018
Governors of the Federal Reserve System et al., ]. However, lit-
tle new regulatory guidance has been provided to address the specific
risks of AI [The Federal Reserve Board of Governors in Washington DC,
2011 2022
,FinancialConductAuthority, ]andfirmscallforamoreproac-
2019
tiveregulationapproach[FinancialConductAuthority, ,Trubyetal.,
2020 2020
]. Trubyetal.[ ]notesanoveralllackofguidanceonAIusefrom
"typically cautious financial regulators". Overall, clarification is needed
on how current regulatory mechanisms address the risks of AI.
In this study, we focus on a highly-regulated area, anti-money laun-
dering and countering financing terrorism (AML-CFT). AI applications
for AML-CFT, such as unsupervised anomaly detection, have attracted
increasing attention from both industry players and academics for their
potential to reduce compliance costs and detect new patterns of money
launderingthatcurrentrule-basedsystemsarenotawareof [Guptaetal.,
2023 2018 2018
, Singh et al., ]. In experimental conditions, Weber et al. [ ]
has found that these methods can reduce the number of false alerts for
20 30
money laundering by to %. The impact of such technologies is all
the more promising as current AML-CFT systems are relatively ineffec-
2021
tive [Bertrand et al., ]. The United Nations Office on Drugs and
2 5
Crime estimates that between and % of global GDP is laundered each
1 2011
yearandlessthan %ofthesefundsareseizedorfrozen[UNODC, ].
Bankshavebeenincreasinglytoutingtheuseofartificialintelligence(AI),
to the extent that AI use for AML-CFT is entering a tipping point. In
2022
October , a Dutch court ruling confirmed that the financial institu-
tion Bunq could use AI despite reservations from the regulator [Trade
2022
and Industry Appeals Tribunal, ]. Big tech companies have also be-
gun to provide AI services for AML-CFT systems within banks, such as
60
Google’s collaboration with HSBC which resulted in a % reduction of
falsepositivealertsandquadruplingthenumberoftruepositives[Tokar,
2023
].
2019
Kruse et al. [ ] argue that the primary challenge posed by AI algo-
rithms in the finance industry is related to their opacity. As highlighted
2021
by Kuiper et al. [ ], AI opacity undermines the ability of financial in-
stitutions and regulators to control their systems, thereby posing a risk
to financial stability, institutional trust and consumer protection [Kuiper
2021 2019
et al., , McWaters and Blake, ]. In AML-CFT, concerns of regu-
lators have also focused on the lack of transparency in AI models and on

understanding the supervisors needs for explainable ai in financial crime
’
detection 187
2017
measuring their added value [Gruppetta, ]. Overall, it is undisputed
that a certain level of transparency is required for AI models [McCaul,
2022
]. However, it is rarely specified to what extent and why AI expla-
nations should be generated in relation to applicable legal requirements.
Moreover, few studies have explored the regulator perspective, despite
the fact that they are an essential audience of AI explanations.
In this chapter, we focus on AML-CFT supervisors in France, who act
as the national public auditors of AML-CFT systems in banks. We strive
to understand the supervisors’ perspective on AI transparency and justi-
fications, in this case in the highly regulated AML-CFT environment in
France. Specifically, we leverage two scenarios of promising AI applica-
tions from the AML-CFT literature and conceptual design artifacts of AI
2000
justifications and explanations[Gaver and Martin, ]. We outline the
justification requirements and information needs of supervisors regard-
ing AI systems to help banks better design justifications for AI systems
and to help supervisors build relevant explainability and testing solu-
tions for auditing purposes. Grounded in the context of AML-CFT, our
study is guided by the following research questions:
RQ1: What are regulatory supervisors’ current auditing practices and socio-
techno context? (Section 6.4.1)
RQ2: How does AI opacity conflict with compliance requirements and to what
extent can justifiability address these tensions? (Section 6.4.2)
RQ3: WhataretheneedsofsupervisorsforjustifiabilityofAIsystems? (Section
6.4.3)
Our study adopts two original approaches. First, the needs and con-
text of regulators, supervisors and auditors is not currently well under-
stood. By exploring their justification needs, we can reduce regulatory
uncertainty around the use of AI. Investigating the supervisor perspec-
tive will inform how existing accountability mechanisms can be applied
to AI technology. Second, in order to fully understand the objectives and
needs of supervisors, it is necessary to consider the legal requirements.
As such, we conduct a multi-pronged socio-techno-legal study of these
users and their context.

188 the explanation paradox and the human centric path
-
6.2 Background
6.2.1 HCI work on eliciting user explainability needs
243 2
As presented in Section . . in Chapter , HCI researchers have often
2022 2023
relied on interviews and workshops [Sun et al., , Liao et al., ,
2020 2021 2021 2021
, Ehsan et al., , Maltbie et al., , Tsai et al., , Kim et al.,
2023 2019
, Ehsan et al., ] to learn about the needs and context of specific
user groups and inform the design of explainability systems. Addition-
1997
ally, scenario-based design, [Carroll, ], in which participants are en-
gagedinascenariotoelicittheirfeedback,wasusedmultipletimesinex-
2020 2022 2019
plainability [Cirqueira et al., , Sun et al., , Wolf, , Liao et al.,
2023
]. However, very little work has explored the needs of regulators
2021
as a user group [Kuiper et al., ], and no work in the HCI field has
addressed the elicitation of explainability needs using both a scenario-
based and a legal approach, to the best of our knowledge. Our view is
that it is particularly relevant to the study of the needs of regulators. For
2020
example, Chazette and Schneider [ ] emphasised that the elicitation
of explainability needs should also take into account laws and norms,
culturalandcorporatevalues,domainaspects,organisationalconstraints
2021
such as time, resources, etc [Maltbie et al., ].
6.2.2 Designing AI justifications for compliance
2019
As noted by Hildebrandt [ ], explainability is only a small part
of the justifiability equation for AI systems and may obscure the big-
ger picture. However, the notion of legal justification of AI systems has
not received as much traction so far. Explainability has received much
more attention. Specifically, "legal explanations", i.e. explanations de-
signed to support the legal compliance process, have been examined by
2019 2020
XAI researchers [Carvalho et al., , Beaudouin et al., , Dupont
2020
et al., ]. The requirements of the General Data Protection Regulation
2016
(GDPR) [European Parliament and Council, ] to provide users with
"meaningful information about the logic involved" have received much
2022 2020
attention from explainability researchers [Hamon et al., , , Bibal
2021 2021 2017
etal., ,Confalonierietal., ,Doshi-VelezandKortz, ]. Recent
work reviews in detail the legal requirements for explainable AI [Nan-
2023 2021 2017
nini et al., , Bibal et al., , Doshi-Velez and Kortz, , Panigutti
2023 2023
et al., b]. Nannini et al. [ ] highlight that regulations are in-
formed by coarse notions of explanations. Nevertherless, Doshi-Velez
2017
and Kortz [ ] argue that "legal explanations" are technically feasible,
2021
mainlythroughlocalexplanationsandcounterfactuals. Bibaletal.[ ]
presentsfourlevelsofexplanationstomeetthedifferenttypesofrequire-
ments: explanation of the main features, of all features, of the features
involved in a decision, or of the whole model.
However, this interdisciplinary body of work, has not yet adopted a
user-centric approach to study the needs of regulators, who are the main
end-users of such "legal explanations".

understanding the supervisors needs for explainable ai in financial crime
’
detection 189
6.2.3 Auditing AI systems
Some work has emerged to define AI auditing and its role in relation
2014 2021
to traditional audits [Sandvig et al., , Metaxa et al., , Toader,
2019 2014
] or to outline audit approaches and principles [Sandvig et al., ,
2021 2019
Koshiyama et al., , Raji and Buolamwini, , Mökander et al.,
2023 2014
]. Sandvigetal.[ ]firstintroducedthenotionofalgorithmaudit,
withtheapplicationofInternetplatformsalgorithmsinmind. Mökander
2023
et al. [ ] summarized the promise of AI auditing in three ideas: it is
procedurally regular and transparent, it enables proactivity in address-
ing AI harms, and it is conducted by independent parties. Koshiyama
2021
et al. [ ] give four main verticals of algorithm auditing: performance
and robustness, bias and discrimination, explainability, and privacy. The
first vertical encompasses concepts such as resilience to attacks, fallback
plan, accuracy, reliability, and reproducibility. They define seven levels
of explainability, corresponding to increasing levels of access to infor-
2020
mation up to the complete "white-box" setup. Raji et al. [ ] drew
lessons for AI auditing from industries including finance. The authors
discuss the historical role of internal audits in this domain, and their
focus on organisational aspects and risks. They also consider financial
auditing to be "lagging behind the process of technology-enabled finan-
cialisation of markets and firms". The literature on AI auditing is still
2021
in its infancy [Falco et al., ], and has so far only focused on defini-
tions and methodological aspects of audits, from a theoretical point of
view. Verylittleresearchhasofferedqualitativeempiricalinsightsonthe
socio-techno-legal aspects of AI audits.
6.2.4 The AML-CFT context
Overview. Money laundering is the action of concealing the origin of
funds illegally obtained. Terrorist financing is a different process: it in-
volves concealing the destination of funds by raising, storing, moving,
2006
and using the money [Levi and Reuter, ]. To detect these financial
crimes, AML-CFT laws require banks to carefully control with whom
theyareengaginginabusinessrelationshipandtoactivelymonitortheir
2021
customers’ transactions [Bertrand et al., ]. This implies that banks
map out the money laundering risks to which they are exposed, tak-
ing into account their activities and customers, and putting in place a
detection system, including an often automated "transaction monitoring
system"thatflagsunusualactivities. Ingeneral,thisrule-basedapproach
begins with an alert is first triggered from an automated system usually
based on rules (such as "transaction is superior to a certain amount"),
then it is quickly reviewed by a human analyst and either closed or
passed on to a second level of review. If the alert is still considered
suspicious at this stage, a case is created and a more extensive investi-
gation is opened to be reviewed by more experienced analysts. If the
suspicion is confirmed, it is reported to the national financial investiga-
tive body—TRACFIN in France—which conducts a deeper investigation
2020
[Jullum et al., ]. If there is evidence of a financial offence, the case is
3
passed on to the law enforcement authorities . 3c.f. Figure 1 in [Kute
etal.,2021].

190 the explanation paradox and the human centric path
-
Legal requirements. AML-CFT laws propose a risk-based approach,
meaning that banks have to identify the risks they are exposed to and
takeappropriatemeasurestomitigatethem[FinancialActionTaskForce,
2007
]. The risk-based approach to AML-CFT is widely adopted and has
been recommended by the Financial Action Task Force (FATF), the in-
tergovernmentalorganizationdedicatedtocombatingmoneylaundering
39 24
andthefinancingofterrorism,toits members,whichincludes non-
2014
EU countries [Financial Action Task Force, ]. It is also the standard
approach in Europe as it has been recommended by the European Bank-
2016
ing Authority [European Banking Authority, ].
The banking sector also has "internal control" obligations that consti-
tute a set of safeguards enabling financial institutions to control the risks
2020 2011
of their activities [Raji et al., , Soh and Martinov-Bennie, ]. EU
2013 36
countries are subject to such requirements under Directive / /EU.
Under these requirements, banks have to implement three "lines of de-
fense" to ensure that their financial activities remain legal: level one cor-
responds to the day-to-day business operators; level two requires a sepa-
rateunitresponsibleformonitoringlevelone;levelthreeisanauditteam
that intervenes periodically. If banks fail to comply with these obliga-
tions, they can face heavy fines by the national supervisory authority. In
2016 2021
France,thesefinesamountedtoseveralmillioneurosbetween - ,
65
sometimes amounting up to . % of the fined banks’ revenues [Conseil
d’Orientation pour la lutte contre le blanchiment et le financement du
2023
terrorisme, ].
The role of supervisors. Supervisors are agents of regulation. In
4
France, their role is laid down in the regulation , and described on the 4In Articles L561-36 to
French Regulator’s website 5 . Supervisors monitor the compliance of fi- L561-44 of the French
MonetaryCode.
nancial institutions with European and national AML-CFT laws. They
5https://acpr.banqu
also influence the development of AML-CFT frameworks by synthesiz-
e-france.fr/controler
ing gaps, threats, and best practices at the national level. For example,
/lutte-contre-le-bla
the French supervisor annually reports on the threat posed by money nchiment-des-capitau
laundering and terrorist financing and often publishes guidelines and x-et-le-financement
thematic reviews detailing the supervisor’s expectations and interpreta- -du-terrorisme/presen
tation-du-controle-l
tions of the law.
cb-ft
AIforAML-CFT.Bankshaveonlyrecentlybeguntoexploretheuseof
machine learning in AML-CFT, but it is one of the most impactful appli-
2022
cations of AI in banking [Fritz-Morgenthal et al., ]. AI development
ismainlyduetotwofactors. Firstly,AIpromisesbetterperformancethan
traditional detection systems, which are based on known scenarios of
money-launderingschemes. Themostpromisinguseisthroughunsuper-
vised and reinforced learning that have the potential to detect anomalies
which shed light on typologies of money laundering that have not been
2020
previously reported [Canhoto, ]. AI can also help set smarter alert
thresholds, help human analysts prioritize alert treatment, and enhance
thequalityanddiversityofthedatausedincriminalinvestigations[Chen
2018 2021 2020 2020
etal., ,KurshanandShen, ,Labibetal., ,Lorenzetal., ,
2011
Ngai et al., ]. Secondly, AI enables banks to cut costs by alleviating
repetitive tasks and reducing the human staff required to review alerts

understanding the supervisors needs for explainable ai in financial crime
’
detection 191
2020 2018
[Overrein, , Singh et al., ].
However,AIisstillarelativelyrecenttopicinAML-CFT,andAI-based
systemshavebeensubjecttofew, ifany, regulatoryauditstodate. Sofar,
only a handful of national supervisory authorities have expressed posi-
2018
tions on AI. In , the Monetary Authority of Singapore stated to be
"in agreement that such advanced technologies can and should be lever-
2018
aged by banks" [Singh et al., ]. A report on AI for AML in Norway,
however, argues that banks "as well as regulators have historically been
2020
reluctant to use AI" [Overrein, ]. The Dutch Central Bank (DNB),
2022
in November , was hesitant over machine learning technologies for
2022
AML as illustrated in a regulatory sanction [Blakey, ] but has since
2018
cautiously opened the door for its use [Singh et al., , Hoegen et al.,
2023
]. The French supervisor has not yet expressed clear guidance on AI
buthasbeengenerallyopentothetechnology. Theyhavealsodeveloped
aninternalAI-basedtooltochallengetheperformanceofbanks’systems
2021
[Laporte, ].
Explainability and transparency in AML-CFT. Explainability (XAI)
has often been presented as a requirement to meet compliance standards
2020 2022
in AML-CFT [Bellomarini et al., , Fritz-Morgenthal et al., , Ger-
2022 2019 2022
lings and Constantiou, , Al-Shabandar et al., ]. In her
speech about technologies to fight financial crime, Elizabeth McCaul,
member of the Supervisory Board of the European Central Bank (ECB),
presented explainability and transparency as "two of the most important
2022
challenges for AI" [McCaul, ]. However, the specific requirements
for explainability and transparency remain vague and general. It is not
yet clear which precise legal requirements they would fulfill.
Nevertheless,severaleffortstobuildexplainabilitysolutionshaveemerged
2021
in AML-CFT over the past few years. According to Kute et al. [ ]’s
51
review of AI solutions in AML-CFT, % of the scientific papers that
present a machine learning method for AML also consider the explain-
ability of their solution, such as knowledge-graphs rule-based reasoning
2020 2023
approaches [Bellomarini et al., ]. Weber et al. [ ] identify case
studies from the literature where AI and XAI were successfully applied
in real financial contexts. The paper also stresses that XAI in AML is
under-explored. However,themajorityofthesecontributionsareincom-
puter science and do not consider the complex realities of the AML-CFT
context.
Some studies have provided more detail on users’ needs for explain-
abilityinAML-CFT.Recentworkhasemphasizedtheneedtounderstand
why an AI model raised an alert, and understand the main features that
drove the decision, for the banks’ investigators and the national financial
2019
investigativebodies[Al-Shabandaretal., ,GerlingsandConstantiou,
2022 2020 2018 2020
, Bellomarini et al., , Chen et al., , Cirqueira et al., ].
The purpose of this explanation is to provide sufficient evidence about
2021
the suspiciousness of a case [Kute et al., ]. Gerlings and Constantiou
2022
[ ] investigated the needs for XAI in AML-CFT for banks’ investiga-
tors and capacity planners. They highlighted the need to explain the

192 the explanation paradox and the human centric path
-
reasonsforautomaticclosuresofalertsanddemonstratedtheriskofbias
when the scoring of an alert was made visible to the investigators.
However,veryfewstudieshaveexploreduserneedsfromtheperspec-
2022
tive of supervisors. While Gerlings and Constantiou [ ] hypothesize
that "auditors may require additional information on the model logic",
theydonotdescribethesupervisor’sexplainabilityrequirementsinmore
2021
detail. Kuiper et al. [ ] explored the perspectives of banks and su-
pervisors in the Netherlands regarding explainability in three financial
domains, including AML-CFT. They found that supervisors expected ex-
planations to have a broader scope than banking practitioners, who have
amoretechnicalandlocalunderstandingofexplainability. Theydidnot,
however, detail the goals and needs of supervisors for explanations nor
justificationsanddidnotconsiderthelegalrequirementssupervisorsex-
pect to see in model explanations.
6.3 Methods
This section presents the qualitative methods we used to understand
the socio-techno-legal supervision system in AML-CFT and supervisors’
needs for model justifiability. We first conducted five semi-structured,
13
scenario-based workshops of two to three participants with supervi-
sors in total. At the beginning of our research, we had initially planned
to study the need for transparency and explanation of the models, both
for the supervisory authorities and for the banks, but we shifted our fo-
cus early on to the supervisory authorities in order to provide a more
targeted and in-depth analysis. We nevertheless ran one workshop with
participants from a large French bank, which improved our understand-
ing of the existing supervisory mechanism from an other perspective:
that of regulated entities.
During the workshops, we observed that the participants, particularly
the supervisors, consistently referred to legal requirements or regulatory
sanction cases when asked about the questions they had about the AI
systems and the explanations or justifications they wished to see. This
promptedustofindoutmoreabouttheAML-CFTlawsthatparticipants
referenced. Additionally, we noticed that the existing scientific or grey
literature did not clearly indicate which legal requirements could under-
minetheuseofAI.Forthatreason,weadjustedourinitialresearchques-
2
tions and added the RQ on how AI opacity conflicts with compliance
requirements.
We present below the different methodological building blocks we
used in the study, presented in chronological order of implementation.
First,wepresenttheprocedure,artifactsused,andanalysisforthework-
shops. We then present the methodology we used to complement the
analysis of the workshops with regulation-driven needs for algorithmic
justifiability. Lastly, we present our findings in post-analysis interviews
with two experts in AML-CFT regulation.

understanding the supervisors needs for explainable ai in financial crime
’
detection 193
6.3.1 Scenario-based semi-structured workshops
Procedure. All workshops were held in person at the participants’
90 100
workplaceandlastedbetween and minutes. Participantswerenot
compensated. Upon their arrival, participants were asked to read and
fill in a paper consent form. The consent form included a description
of the purpose and possible risks (mainly confidentiality) of the study,
the mitigating measures we implemented to ensure the confidentiality
of the recordings and data presented in a publication, and finally their
choicetovoluntarilyparticipateinthisresearchandtoberecorded. They
werethenaskedtoanswerpreliminaryquestionsabouttheirexpertisein
AML-CFT and their familiarity with AI on a printed form. The inter-
viewer then detailed the workshop agenda.
4
The workshop questions focused on main themes. First, participants
wereaskedabouttheexistingcomplianceprocedureinAML-CFTintheir
profession (either controllers or bank practitioners). The following ques-
tions addressed the use of AI in AML-CFT to understand participants’
impressionsofAI.Weoriginallyplannedthistofindoutmoreabouthow
banking supervisors and practitioners envisage AI’s future in AML-CFT.
However, as the French supervisors were about to publish their position
on AI at the time of the study, they considered this information to be too
sensitive. We therefore limited the scope of our research to justifiability
and explainabilityneeds. Wethen presented participantswith a scenario
in which a supervisor controlled an AI-enhanced transaction monitoring
system. We asked participants which kind of questions they had about
the AI system and what kind of justifications they wanted to see. This
scenario-based elicitation approach was used in prior research to under-
2023
stand users’ needs for justifications and explanations [Liao et al., ,
2020 2022 2009 2019
, Sun et al., , Rosson and Carroll, , Wolf, ]. Finally, con-
2000
ceptualdesignartifacts[GaverandMartin, ]ofdifferentexplanations
and justifications were presented to the participants for fictitious alerts.
Participantswereinvitedtodiscusstherelevanceofthejustificationsand
624
their limitations. As seen in Section . . , AI’s entrance in AML-CFT is
a recent topic where regulatory thinking has not yet matured. Therefore
someofthequestionscalledforspeculativethinking. Forthisreason, we
chose to interview the participants in small groups, so that they could
1996
discuss these issues together [Morgan, ].
Participants. OneoftheauthorshadseveralconnectionsattheFrench
SupervisoryAuthoritytohelpcontacttheappropriatedirectorstoobtain
the necessary approvals to carry out the research and to connect with
controllers. We also learned that the French Supervisory Authority has
two departments, one for ongoing monitoring of all financial institutions
registered in France and one dedicated to on-site inspections. We used
the email lists for these two departments to recruit participants, describ-
ing the purpose of the research, the time, location, and agenda of the
13
workshops. In total, we recruited controllers from the French super-
6 7
visory authority, from the on-site inspections department and from
1 20
the on-going monitoring department. They had between and years
of experience in AML-CFT supervision and their level of familiarity in

| 194 the | explanation |     | paradox | and | the | human centric path |     |     |     |
| ------- | ----------- | --- | ------- | --- | --- | ------------------ | --- | --- | --- |
-
|     | 36  |     |     |     | 7   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
AI averaged . out of a Likert scale of ; two participants had extensive
| expertise | in AI—familiarity |     | level | with | AI was | 7 / 7 . |     |     |     |
| --------- | ----------------- | --- | ----- | ---- | ------ | ------- | --- | --- | --- |
The participants from the large French bank were recruited by a con-
tact the authors had at the bank with a specific selection criteria for the
participants,i.e. peoplespecialisinginAML-CFTwithsomepreviousex-
posuretoAIand,ifpossible,alsotosupervisorycompliance. Intotal,six
participantstookpartintheworkshop. Threeparticipants’expertisewas
AML-CFT compliance. The other three participants came from machine
learning model development. Naturally, the participants in this study
spoke in their individual capacity and their views do not represent the
official positions of either the French Supervisory Authority or the Bank
| that employed | them. |     |     |     |     |     |        | 6.1: |           |
| ------------- | ----- | --- | --- | --- | --- | --- | ------ | ---- | --------- |
|               |       |     |     |     |     |     | Figure |      | Scenarios |
Of the 6 workshops, 4 were recorded and 2 were not as some partic-
|     |     |     |     |     |     |     | used | during | the work- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | --------- |
ipants did not feel comfortable with being recorded, notably due to the shops with supervisors,
sensitivity of AML-CFT. However, participants who did not want to be with a description of
recorded agreed to the interviewer writing notes. One of the unrecorded the two use cases of
|     |     |     |     |     |     |     | AI  | in AML-CFT, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
workshops was with controllers with extensive AI experience, the other
|     |     |     |     |     |     |     | two | examples | of alerts |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- |
wastheworkshopwithbankingactors. AllparticipantswereFrenchand
|     |     |     |     |     |     |     | that | were | generated |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --------- |
thequotespresentedinthispaperweretranslatedfromFrenchtoEnglish or closed by the AI-
|        |                | 6 1 |         |             |     |               | enhancedsystems. |     | Only |
| ------ | -------------- | --- | ------- | ----------- | --- | ------------- | ---------------- | --- | ---- |
| by the | authors. Table | .   | details | the profile | of  | participants. |                  |     |      |
oneofthesecasestudies
| Artifacts | provided. |     |     |     |     |     | was | presented | in each |
| --------- | --------- | --- | --- | --- | --- | --- | --- | --------- | ------- |
workshop.
Thescenariosfeaturedafictionalcharacter,Eric,whoserolewaseither
a controller carrying an on-site mission at a Bank B (for supervisors) or
| Bank B’s | head of compliance |     | (for | banking | practitioners). |     |     |     |     |
| -------- | ------------------ | --- | ---- | ------- | --------------- | --- | --- | --- | --- |
We designed two scenarios involving two types of AI-enhanced trans-

understanding the supervisors needs for explainable ai in financial crime
’
detection 195
Figure 6.2: Conceptual
justifications shown for
the scenario 2 and its
example alert. Concep-
tualjustificationsforthe
scenario 1 followed the
sameformat.

196 the explanation paradox and the human centric path
-
action monitoring systems which have been presented as the most com-
2020
monapplicationsofAIinthescientificliterature[Canhoto, ,Gerlings
2022
and Constantiou, ] and in reports from the French supervisory au-
2023
thority [Autorité de Contrôle Prudentiel et de Résolution, b, Dupont
2020
et al., ]. In the first scenario, an unsupervised learning algorithm
is used to detect new typologies of financial crime. This algorithm trig-
gers alerts when it identifies a transaction as unusual for certain groups
of customers that it has defined. Those alerts come in addition to the
ones generated by the bank’s traditional rule-based system, which gen-
erates alerts based on predefined rules or "scenarios", e.g. "transaction
10000
for this specific customer group is superior to $ . ". When an alert
is generated, a human analyst examines it and determines whether the
identified risk should be addressed by the creation of a new rule in the
traditional alert system. The second AI use case involved scoring alerts
from Bank B’s transaction monitoring system in order to prioritise, redi-
rect, or close them. For high-scored alerts, a Suspicious Activity Report
(SAR) was pre-filled automatically with generic information to be sent
quickly to the Financial Investigation Unit. Only one scenario was used
in each workshop. The first use case was used in three workshops and
the second in the other three.
For each scenario, we described fictional example alerts triggered by
the AI-enhanced AML-CFT system. For example, the example alert for
the first scenario was an alert triggered by the unsupervised AI module.
An example alert for the second scenario was an alert considered as low
risk and closed by the AI. For these examples, we designed conceptual
2000
artifacts [Gaver and Martin, ] of different types of justifications and
explanations. Our aim was to encourage participants to comment and
imagine possible transparency solutions. We tried to balance the con-
creteness and openness of these artifacts and to leverage multiplicity in
order to get feedback on the concept of these justifications rather than
on their design. We chose to show the following justifications and expla-
nations based on what we considered as most common in the literature
2021 2021
on XAI for AML-CFT [Kuiper et al., , Kute et al., , Weber et al.,
2023 2017
, Financial Stability Board, ].
• a visualisation of the context of the alert in the form of graph net-
works
• afeature-basedexplanationshowingthemostimportantvariablesfor
the AI-produced decision, their impact (positive or negative) and their
weight
• an uncertainty estimator showing the probability of the alert to be
suspect, as calculated by the algorithm
• a model documentation structure, including examples of sections:
role of the AI system, training data used, performance evaluations,
and choice of parameters.
• an example-based explanation presenting similar cases and their out-
comes.

understanding the supervisors needs for explainable ai in financial crime
’
detection 197
• acertificationofthedesign,development,evaluationandmaintenance
of the model by an external body. We added this artifact because it is
one of the provisions in the upcoming AI Act relating to high-risk AI
systems.
61
Figure . presents the scenarios we showed to participants. The con-
62
ceptual justification artifacts are presented in Figure . .
Analysis. We used a content analysis methodology [Bengtsson, 2016 ]
to analyse the audio transcriptions—including question-answering and
think-aloud data—and the notes taken from the workshops. The notes
were taken by the interviewer during the workshops and we recognise
their limitations. Although they cannot reflect the details and nuances of
the participants’ thoughts and words, the notes nevertheless capture the
general and sometimes strong opinions of the participants. The broad
themes used for the content analysis followed the workshop structure:
1 2
( ) the socio-technical context and ( ) technical approaches of the super-
3 4
visory authorities, ( ) the AML-CFT legal requirements, ( ) supervisors’
5
questions on AI, ( ) ideas for designing AI justifications and explana-
tions. Basedontheopencodesgatheredforeachofthesefiveoverarching
themes,weusedaxialcodingtoestablishlinksbetweentheconceptsand
2014
refinethem[CorbinandStrauss, ]. Thefirstauthor,whowasalsothe
interviewer and note-taker for the non-recorded workshops, carried out
5
the thematic and axial coding for workshops—three fully transcribed
and two partially-transcribed using notes. Another author analysed the
audio transcripts of a workshop and applied open thematic coding sep-
arately. The two authors then discussed all the codes they had created
6
and refined them on a Miro board . 6https://miro.com/app
/dashboard/
6.3.2 Empirical legal research
As agents of regulation, supervisors’ goals are embedded in the legal
requirements they enforce. During the workshops, we observed that not
having a full grasp of the various legal themes to which the participants
were referring prevented us from capturing their motivations to ask for
specific justifications. Therefore, we complemented the scenario-based
eliciting approach with a qualitative empirical legal research [Webley,
2010
]. We believe that combining needs elicitation with a legal analysis
is key to fully understanding regulators’ needs. In fact, the legal field
is also keen on qualitative approaches, using interviews and legal docu-
ment analyses, with methods similar to those used in the social sciences.
2010
Webley [ ] points out that "many common law practitioners are un-
aware that they undertake qualitative empirical legal research on a regu-
lar basis". We conducted this legal approach in parallel to the analysis of
the workshops.
AI Compliance Assessment. Our methodology was adapted to ad-
2010
dress our research question, as recommended by Webley [ ]. It was
carried out by the first author, who does not have a legal background,
but the methodology and findings were discussed multiple times with
another author with extensive experience in legal practice and research.

198 the explanation paradox and the human centric path
-
2017
We began using a doctrinal research as described by McConville [ ],
which consists in seeking what the law is in a particular area. We thus
examined regulatory sanction cases on AML-CFT, the relevant articles
of the French Monetary Code, and other useful legal documents on the
advice of a lawyer from the French Banking Supervisory Authority. The
62
data collected we used for this legal approach is detailed in Table . .
We narrowed our focus on AML-CFT and internal control requirements,
as these are the requirements that banks are evaluated against during
AML-CFT supervisory audits. We identified the main legal themes and
specified their meaning, first using open coding on five regulatory sanc-
tion cases, because they reflect how supervisors’ interpret and structure
AML-CFTlaws. Wethenrefinedthethemeswiththerestofthedatacol-
631
lected. We used the scenarios we defined in Section . . to assess how
AIopacityimpactseachidentifiedtheme. Finallyweconductedfeedback
interviews. In short, our method follows these six steps:
1
. Identify the applicable laws in AML-CFT and define the scope of the
research through "doctrinal research"
2
. Define the main themes in the applicable laws, building on the format
of the legal documents and invoked themes in the workshops,
3
. Specify the meaning of the requirements in each theme, drawing on
the supervisors’ perspective and legal documents such as case law,
which inform on how the law is commonly interpreted,
4
. Define scenarios featuring AI systems in AML-CFT,
5
. Consider how the opacity of these systems conflicts with each sub-
theme identified, which can also be formulated as goals for which the
supervisors seek transparency,
6
. Obtain feedback on our analysis from AML-CFT experts during inter-
views.
Feedback interviews. Because step 5 of the above methodology can be
somewhat subjective and potentially inaccurate due to the lack of exper-
tise of the first author in AML-CFT law, we conducted two interviews to
elicit feedback and corrections from experts. The two participants were
soliciteduponadvicefrominternalcontactsattheFrenchsupervisoryau-
thority,giventheiruniqueexpertiseinbothAIandlaw. Oneofthemwas
alawyerandtheotheranon-siteinspectorwithextensivebackgroundin
AI. Our pre-interview included a presentation of the research, confiden-
tiality risk mitigation measures, and request to record interviews. We
began by asking participants two general questions: what do they see as
the key challenges in assessing AI’s compliance with AML-CFT require-
ments, andhowdoestheopacityofAImakecompliancewithAML-CFT
requirements difficult. We then presented them an initial version of the
2
table shown in Appendix C and asked for feedback. Interviews were
used to both correct and complement our prior analyses. Interviews
were recorded, transcribed, and two authors analyzed and coded them
631
according to the process described in Section . . .

understanding the supervisors needs for explainable ai in financial crime
’
detection 199
6.4 Results
The results presented in this section are structured around three axes,
each aimed at improving our understanding of a user group that is
under-represented in the literature: regulators, more specifically, super-
visors in AML-CFT. The three axes correspond to our research ques-
1
tions: understanding the supervisors’ socio-technical context (RQ ), un-
2
derstanding the regulatory goals of supervisors in AMl-CFT (RQ ), and
articulating the supervisors’ needs for AI justifications and explanations
3
(RQ ).
6.4.1 Socio-techno-legal context and auditing approaches of
supervisors in AML-CFT
63
Figure . provides an overview of the workshop findings and the
socio-techno-legal context of supervisors.
Figure 6.3: Summary
of the workshops,
with socio-techno-legal
How are supervisory audits organized in practice?
context of supervisors,
supervisors’ questions
The French Banking Supervisory Authority carries out two types of
on AI, AI auditing
approaches ideas and
ideas for justifications
andexplanations.

200 the explanation paradox and the human centric path
-
inspections: document-based control and on-site.
The document-based control unit’s mission is to assess the maturity
of the AML-CFT system of each regulated entity in France (around
1,300). This control is based on numerous records, including an AML
questionnaire that banks report annually and exchange with the regu-
lated entities. They then notify the banks of their observations. This unit
can also suggest on-site inspections, as one participant notes:
"whenweseealotofdeficiencies,wewillinformtheon-siteinspectionandpropose
thattheestablishmentbeincludedintheinvestigationprogramme".
The role of on-site inspections is to confirm the true state of a bank’s
declarations concerning their system for AML-CFT and to assess their
effectiveness. Inspectors will challenge a bank’s system, observe how
employees work, compare declarative practices with what actually oc-
curs, exchange information with bank practitioners, and perform IT ex-
tractionstoidentifyanymajordeficiencieswithintheallottedtimeforin-
spection, i.e. a few months. One participant emphasised the importance
of the iterative process when communicating with banks which helps
40
prevent misunderstandings. Around on-site investigations take place
2023
annually [Autorité de Contrôle Prudentiel et de Résolution, a]. Fol-
lowing the findings of an on-site inspection, a sanctions committee may
thenbecalledupontodecidewhetherapenaltyshouldbeimposed. Fig-
64
ure . detailstheanti-moneylaunderingandterroristfinancingcontrols
for the French supervisor.
It is worth noting that the large majority of controllers have a legal
background with expertise in financial crime analysis. Many partici-
pants, therefore, expressed unease with complex statistical tools such
as AI. For example, some participants said "ourITskillsarealittlelimited"
3
(P )andexpressedtheirlackofcomputerscienceknowledgetodealwith
theparticularitiesofmachinelearningmodels. Oneoftheseparticipants,
however, was aware of unsupervised and supervised learning and many
participantswithlittlefamiliaritywithAIwereabletogenerallydescribe
the functioning of the AI-based systems they had seen in banks. More-
over, on-site missions include at least one computer scientist to support
non-tech controllers. One participant stated
"Whenyouneedtogointodetails,youneedtohaveknowledge,experienceoreven
ideasofwhattodo. Their[thebankingactors’]jobandoursisevolving,we’llhave
tospeakboththefinancialcrimeandpythonlanguages."(P11)
How do supervisors describe the legal context in AML-CFT?
624
Section . . provided an objective review of the legal context. Below
we give a brief impression of participants’ perspectives on these regula-
tions. SupervisorsdescribedtheAML-CFTregulationas"prolix"(P 1 )and
"subtle, with high expectations and not much room for error" (P 11 ). Another
participantaddedthat"everysystem,eventhebest,doesnotdetecteverything,
confirming that a small margin for errors is left in transaction monitor-
ing given there is an obligation of implementing the best means and not
an obligation of results. Just as there exists a small margin for error for

understanding the supervisors needs for explainable ai in financial crime
’
detection 201
7
data quality they expect AI tools to also make errors. Supervisor toler- 7roughlybelow5%
ance is qualitative, and depends on error severity and systematicity. It
was also noted the regulation does not stipulate a requirement to auto-
mate tools. It is instead the size of the regulated entity and its volume of
transactions that will drive an implementation of automated "scenarios"
and ultimately, AI. One participant noted that
"[Banks]arefairlyuptospeedwithregulation,theywillenduponAIonedayor
another."
What are the approaches of supervisors to audit the automated
AML-CFT systems in banks?
Participants emphasized that there is no single approach to auditing;
all audits adapt to their context. We identified, however, some common
approaches to auditing. Investigations or document-based assessments
8
usually start by examining the risk classification of banks . Banks must 8One participant noted:
produce this document, which identifies the money laundering and ter- "everythingflowsfromthe
riskclassification"
rorist financing risks related to the bank’s activities, size, customers, etc.
Supervisorscanthenidentifygapsintheidentifiedrisks,intheriskscov-
ered by scenarios, and other automated tools. Then, during controls, su-
pervisors assess the quality and compliance of two aspects of the bank’s
AML-CFTsystems: processesandresults. Approachestoevaluateresults
may pinpoint failures in the process and vice versa. Audit strategies of
AML-CFT frameworks can be broadly summarized in three approaches:
"global", "global to local" and "local towards global".
Global approaches consist in looking at metrics characterising the
efficiency of AML-CFT devices. These metrics include, for example, the
number of alerts generated, the number of reinforced examinations, and
the number of SARs. Supervisors interpret these metrics in relation to
the bank’s characteristics; as a participant notes,
"We’llseeifthey’reconsistentwiththeestablishment’sactivity. (P3)
It takes some time, however, for these measures to reflect the value of a
new tool:
"aslongasthescenariohasn’treallyrunforayear,wewon’thaveveryinteresting
statistics."(P4)
Furthermore, a "global to local approach" enables controllers to find
cases to investigate. The French supervisory authority recently devel-
opedanAI-basedtool,"LUCIA",tosupportcontrollersinsamplingcases
2021
andcomparingthemwiththebank’sresults[Laporte, ]. Participants
highlighted time-savings and novel offerings of this tool:
"It makes it possible to review, I don’t know, thousands of operations, whereas as
anon-sitecontrollerwecanseeapanelofaboutfiftyoperations."(P8)
1
P reportedthattheworkofcontrollersisoftenverytediousandstressed
the need for tools like LUCIA,

| 202 the | explanation |     | paradox | and | the | human | centric | path |
| ------- | ----------- | --- | ------- | --- | --- | ----- | ------- | ---- |
-
"sothatweareinaposition,nottoanticipateanything,buttoreacttoregulations
andperhapstodetectloopholesmoreeasily."(P1)
7
| P summarized |     | the main | goal | of SupTech | tools: |     |     |     |
| ------------ | --- | -------- | ---- | ---------- | ------ | --- | --- | --- |
"enrichthecontrolbygivingpossibilitiesorideasthattheanalystswouldnothave
hadorthattheywouldnothavehadthemeanstolookat."(P7)
LocalapproachesinvolveexaminingspecificcasesorpartoftheAML-
CFT framework to see if there are any crude errors in reasoning. Exam-
ining local cases can also give conclusions about the results. The "local
towards global" approach aims at drawing conclusions on the system
| from ad-hoc |     | observations. |     |             |      |      |           |            |
| ----------- | --- | ------------- | --- | ----------- | ---- | ---- | --------- | ---------- |
|             |     |               |     | Supervisors | draw | on a | thread of | errors ob- |
served in specific cases to trace systematic errors in the system. This is
enabledby"failureanalyses"or"sampleanalyses"whichconsistofexam-
iningcaseseitherbroughttotheattentionofsupervisorsbyTRACFINor
anotherpublicauthority,ordrawnfromasamplingstrategy. Supervisors
ask:
| "should | the | system have | detected | [the errors]? | Was | it within | its scope? | Was it |
| ------- | --- | ----------- | -------- | ------------- | --- | --------- | ---------- | ------ |
"(P14)
withinitsobjectivesandwhydidn’titdetectthem,whatwentwrong?
Overall, the superposition of different methods for auditing and de-
tecting financial crime in banks, whether AI-based or not, improves the
| efficiency                                               | and | robustness  | of            | the frameworks: |            |         |                  |        |
| -------------------------------------------------------- | --- | ----------- | ------------- | --------------- | ---------- | ------- | ---------------- | ------ |
| "Weknowthattherewillbeillegaloperationsthatgoundetected. |     |             |               |                 |            |         | Wecan’tdetect    |        |
| everything,                                              |     | but there’s | an obligation | to try          | and detect | as much | as possible,     | and if |
| westartrelyingsolelyonAI,well,we’reboundtomissthings.    |     |             |               |                 |            |         | Butwe’llmissless |        |
ifwesuperimposedifferentmethods."(P14)
Figure 6.4: Flow di-
agram of the supervi-
sor’scontrolprocedures
inAML-CFT

understanding the supervisors needs for explainable ai in financial crime
’
detection 203
6.4.2 What provisions in AML-CFT laws does AI opacity
conflict with?
This section presents the results of our compliance assessment, the
632
methodology of which was presented in Section . . . The paragraphs
below present a regulatory goal (RG) with which AI opacity can conflict.
2
Table C. in the Appendix also provides a summary of this analysis.
Verifying risk adaptation (RG1)
Aspartofcompliancerequirements,supervisoryauthoritiesverifythe
adequacy and completeness of a bank’s operation monitoring system in
9
relation to its risk classification . Much of this assessment is based on a 9c.f. Article R. 561-12-
qualitative understanding of the reasoning and criteria used by the sys- 1 of the French Mon-
etary Code (CMF) and
tem to generate alerts. This enables controllers to verify that important
Decision against AXA
characteristics of the business relationship are considered (e.g., income), Banqueofthe15/02/23
orthatthethresholdsarerelevantbasedonbusinessexpertise. Theopac-
ityandcomplexityofAIledsomeparticipantstofearthatthisassessment
would become difficult:
"We’re going to end up with this like chickens with a knife and we won’t know
exactly why it generated this alert...we won’t be able to assess the adaptation to
therisk". (P4)
Verifying the bank’s ability to perform constant and careful ex-
amination (RG2)
Supervisorsalsohavetoverifythattransactionmonitoringsystemsde-
tect inconsistencies with up-to-date customer knowledge and fulfill the
10
bank’sobligationsofcarryingout"carefulexaminations"ofoperations . 10c.f. Article L561-6 of
Supervisors typically use performance metrics and a "local to global ap- theCMF
proach"toevaluatethis. AsAIalgorithmsareopaque, however, supervi-
sors may not be able to establish if an ad-hoc error in detecting financial
crime is linked to a broader issue in the system. Moreover, clarifying
how AI systems adjust to input updates might be needed to comply to
constant vigilance obligations.
Verifying the bank’s ability to perform "enhanced vigilance", to
produce quality Suspicious Activity Reports, and to update their
risk classification (RG3)
Financial institutions also have the obligation to increase surveillance
with regard to complex or risky transactions and to submit high-quality
SARs to TRACFIN. As one participant said:
"Allalertsmustbedulysubstantiatedandanalysed."(P10)
This implies that sufficient explanations be given on why a scoring algo-
rithm (as in the first scenario) considers an operation as risky and why
an alert was generated by an algorithm (as in the second scenario), so
that human analysts can write high-quality SARs:

| 204 the | explanation |     | paradox |     | and | the | human | centric | path |     |
| ------- | ----------- | --- | ------- | --- | --- | --- | ----- | ------- | ---- | --- |
-
| "Weneedtobeabletounderstandthecriteriathatgeneratearisk. |     |                                                             |     |     |     |     |     |     | It’saquestion |     |
| -------------------------------------------------------- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | --- |
| ofauditability.                                          |     | Actually,beforethat,it’saquestionofahumananalyst’sabilityto |     |     |     |     |     |     |               |     |
understandwhattolookat."(P14)
Verifying that banks can detect incidents and have control over
| the purpose | and | operation |     | of  | any device | used | (RG4) |     |     |     |
| ----------- | --- | --------- | --- | --- | ---------- | ---- | ----- | --- | --- | --- |
Internal control obligations require banks to: be able to detect inci-
dents; control the operation of their devices, notably over time; demon-
strate control over the purpose of their system, particularly when it is
11
provided by a third party; and plan for safety nets in case of failures . 11C.f Article R561-38-4
However, AI opacity can prevent banks from correctly detecting insta- of the CMF, Order of
November3,2014
| bilities | like drift | or anticipating |           |     | failures:    |     |       |          |              |     |
| -------- | ---------- | --------------- | --------- | --- | ------------ | --- | ----- | -------- | ------------ | --- |
| "If you  | don’t know | what            | behaviour |     | is expected, | you | can’t | say that | there’s been | a   |
malfunction."(P10)
| The inscrutability |     | of algorithms |     |     | can also | create | dependencies |     | on  | AI: |
| ------------------ | --- | ------------- | --- | --- | -------- | ------ | ------------ | --- | --- | --- |
(P7)
"thereisariskofdependenceonAIifthecriteriaarenotunderstood.
Verifying the correct allocation of material and human resources
(RG5)
AML-CFT laws also require banks to put in place the material tools
12
andhumanresourcesneededtomonitoroperations . Caselawindicates 12c.f. Article R561-38
CMF
that it is a question of striking a balance between human and automated
tools. AI transparency will be needed to show how human expertise
and AI systems are balanced and complementary. Many participants
| insisted | that human | expertise |     | cannot | be  | replaced | in  | many | instances: |     |
| -------- | ---------- | --------- | --- | ------ | --- | -------- | --- | ---- | ---------- | --- |
"thereisahumanexpertisethatcannotbereplaced,particularlyinadvisingbanks
onsignsofradicalisation..."(P1)
Forthatreason,theauto-fillingofSARsbyAI,ifnotverifiedandsubstan-
tiated by a human, as presented in scenario 1 , was seen as problematic.
Moreover, explainabilitycanhaveamajorroleinenablingtransitionsbe-
tween machine and human analysts and to ensure timely processing of
| the alerts, | as P | 10 noted: |     |     |     |     |     |     |     |     |
| ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
"theremaybeanimpactofexplainabilityonprocessingtimes."
Indeed, SARs should be filed without delay so that TRACFIN can bring
| cases to      | court | as quickly | as          | possible. |     |        |       |     |     |     |
| ------------- | ----- | ---------- | ----------- | --------- | --- | ------ | ----- | --- | --- | --- |
| Understanding |       | the        | motivations |           | for | AI use | (RG6) |     |     |     |
Some participants, during the semi-structured workshops, were also
questioned on whether banks needed to justify the use of AI. Most par-
ticipants claimed that while it is not legally required, it could help better
understandtheimplementedtransactionmonitoringsystem. Onepartic-
ipant explained:
"I’dusemotivateratherthanjustify,inotherwords,theBankisfreetouseAI.On
theotherhand,itmustalwaysbeabletomotivate,toexplainwhysuchchangein
itssystem."(P7)

understanding the supervisors needs for explainable ai in financial crime
’
detection 205
6.4.3 Supervisors’ needs for model justifiability in AML-
CFT
63
The summary of the workshops presented in Figure . shows the
questions that supervisors asked about the AI systems described in the
scenarios. Basedonthesupervisors’regulatoryobjectivesdescribedabove
and their questions about AI, we formulate supervisor needs for justifia-
bility below.
Understand the basics (N1)
Supervisorswhoareprimarilylawyersrequirehigh-levelexplanations
or machine-learning training to answer their questions like "How does
it work?", "What are we programming exactly [in machine learning pro-
grams]". They want be able to autonomously use a "Challenger" model,
the supervisor’s AI model, to assess bank’s systems. As noted by one par-
ticipant:
"controllershavetobeabletounderstandthepurposeandoperationoftheSupTech
toolsthattheirITteamimplements"(P11)
Their profession will evolve towards hybrid profiles that are both legal
and technical. However, the current challenger model developed by the
Supervisor, LUCIA, is designed as a support tool for in-depth analyses.
One participant explained:
"Paradoxically, the stakes may not be so high because you get to the stage where
you’rediggingintothedetailsanyway,andthenyouabstractfromthesurveillance
system."(P10)
Demonstrate legitimacy (N2)
With LUCIA, supervisors are in an advanced position where AI is
challenging traditional rule-based systems. The errors found during
this process also highlight the added-value of AI, one participant noted.
However, participants from the bank have stressed the need to be on a
13The participants
levelplayingfield,accordingtothelegitimacyprincipleofdueprocess
from the bank were
rights of regulated companies ("equality of arms") [OECD, 2021 a]. For
concerned that LUCIA
that purpose, they would like to understand the data or methodology woulduseinsightscom-
used by the supervisor, especially data they do not have access to. Bank- ing from comparisons
with other banks or
ing professionals also wanted to know if the challenger model was using
sensitive data, but this
sensitive data, or if it was discriminatory in any way, as they are entities
13 is not the case. The
subject to privacy regulations . Nevertheless, a supervisor pointed out
AI-based supervisory
that they are rather at a disadvantage when it comes to finding unde- tool only relies on the
tected financial crime, which fuels their need for AI tools: dataprovidedbythein-
spected bank [Laporte,
14 2021].
"the tight time-frame [for investigations four months] , we need to start every-
thingfromscratcheachtime,thedata,everything..."(P14) 14which is already
longer than in some
other countries, where
Supervisorshaveimplementedquestion-answeringsessionsforbankson
they investigations are
this issue.
sometimes carried out
in a flash (a few days),
theparticipantnoted.

| 206 the | explanation |     | paradox |     | and | the human |     | centric |     | path |
| ------- | ----------- | --- | ------- | --- | --- | --------- | --- | ------- | --- | ---- |
-
| Measure | global |     | efficiency | (N3) |     |     |     |     |     |     |
| ------- | ------ | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- |
641
| TheglobalapproachesdescribedinSection |     |     |     |     |     |     | . . tomeasuretheAML- |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
CFT framework performance are likely to remain valid for any system,
AIornot. Oneparticipantindicatedthat"EvenbeforeAI,theblackboxphe-
14
nomenonalreadyexisted."(P ). Inparticular,thecurrentsamplingstrategy
by the supervisory authorities is still suited to assess AI-enhanced AML-
CFT systems.
| "For       | us, the     | most practical | and       | realistic             | way          | of checking | that  | this           | [the system] | is     |
| ---------- | ----------- | -------------- | --------- | --------------------- | ------------ | ----------- | ----- | -------------- | ------------ | ------ |
| not absurd | is          | not to         | look at   | the parameterisation. |              | Because     |       | it’s difficult | to           | under- |
| stand      | the effects | of a           | parameter | when                  | it interacts | with        | other | parameters.    |              | It’s a |
questionofseeinginsituhowitbehavesinrealitywhenfacedwithexamplesthat
wehaveselectedourselves."(P14)
A participant indicated three main approaches envisaged for evaluating
1
global performance of AI-enhanced AMl-CFT systems: ( ) compare effi-
ciencywiththepre-AIsystem, potentiallycomparingperformanceswith
2
similar establishments; ( ) analysis of the "failures" reported to the su-
3
pervisory authority; ( ) comparison of the banks’ results with the results
obtained using a challenger model on sampled cases. The sampling ap-
| proach | was mentioned |     | in  | all the | workshops | with | supervisors. |     |     |     |
| ------ | ------------- | --- | --- | ------- | --------- | ---- | ------------ | --- | --- | --- |
| 1      | 2             |     |     |         |           |      |              |     |     |     |
P andP alsobrainstormedabout"simple,basic"indicatorstomeasure
efficiency, using, for example, the ratio of suspicious transaction reports
to turnover "or something similar", refined for relevant clusters of similar
establishments, potentially made with AI. Aggregated statistics of this
indicator could also be shared with financial institutions to encourage
improvement:
| "if we | give themthe |     | average, | theyset | themselves | a performance |     | target | whichis, | I   |
| ------ | ------------ | --- | -------- | ------- | ---------- | ------------- | --- | ------ | -------- | --- |
don’tknow,like,20%aboveaverage."(P2)
Another group of participants felt more dismayed by the increasing
opacityandcomplexityofAIsystems. Theyarguedforanotherapproach
| to measure | efficiency  |            | that | relies        | more on | financial | intelligence |              | units:    |       |
| ---------- | ----------- | ---------- | ---- | ------------- | ------- | --------- | ------------ | ------------ | --------- | ----- |
| "the       | standard    | controller | will | be completely |         | helpless. | We’ll        | have         | to change | the   |
| way        | we monitor, | we’ll      | have | to work       | more    | with the  | financial    | intelligence |           | unit, |
TRACFIN,whichwillthenbetheonlyoneabletogiveanopiniononthealerts."
| Establish |     | reprehensibility |     | (N4) |     |     |     |     |     |     |
| --------- | --- | ---------------- | --- | ---- | --- | --- | --- | --- | --- | --- |
Despite implementing sampling strategies, having a closer look into
the AI system inner workings might be necessary to establish the rep-
rehensibility of the errors detected. Understanding why a suspicious
transaction was not detected might help conclude on the systematicity,
and therefore the reprehensibility of the problem. This requires a con-
trastive explanation, focusing on the negative which answers questions
suchas"whydidthesystembehaveinthisway(lettingthefishytrans-
action go) and not in this other way (flagging the transaction)?". One
| participant | described:   |     |         |         |           |            |     |             |          |     |
| ----------- | ------------ | --- | ------- | ------- | --------- | ---------- | --- | ----------- | -------- | --- |
| "It’s       | the question | of  | how you | go from | analysing | individual |     | declarative | failings | to  |
(P10)
makingstructuralobservationsaboutthestructuralfailingsofthesystem.

understanding the supervisors needs for explainable ai in financial crime
’
detection 207
Banks also need to implement such explanations when implementing
anomaly detection AI systems, as in Scenario 2 . In this case, the unsu-
pervised algorithm may encounter a risk typology, not covered by the
traditional bank’s system. The bank then has to understand why this
| risk was | not detected  | and, | if necessary, |     | update        |     | the risk | classification. |     |
| -------- | ------------- | ---- | ------------- | --- | ------------- | --- | -------- | --------------- | --- |
| Verify   | and challenge |      | banks’        | AI  | understanding |     | (N5,     | N6,             | N7) |
642
As noted in Section . . , supervisors may need to examine a bank’s
explanatory practices to ensure that analysts are able to understand
alerts and justify their suspicious nature (N 6 ). To that end, justifica-
tions based on local feature importance explanations, which would be
| implemented  | by         | banks, | have been   | preferred |                  | by  | participants: |                   |     |
| ------------ | ---------- | ------ | ----------- | --------- | ---------------- | --- | ------------- | ----------------- | --- |
| "the feature | importance |        | explanation | is        | more interesting |     | than          | the example-based |     |
one,whichisquitelimitedeventually."(P7)
Bank participants said they were currently testing an explanation based
on Shapley values [Lundberg and Lee, 2017 ]. The contextualisation with
graphs networks has also been appreciated by some participants. In the
adventwheregraphneuralnetworkswouldbeused,wecanalsoimagine
that graph visualisation will be highly recommended by supervisors, as
isthecasefordigitalassetserviceprovidersusingblockchain,onepartic-
ipantcommented. Viewsregardinguncertainty estimatorsweredivided.
| One participant  | mentioned |      | that:   |                 |     |      |                  |     |          |
| ---------------- | --------- | ---- | ------- | --------------- | --- | ---- | ---------------- | --- | -------- |
| "It is important | to        | know | whether | the connections |     | made | are coincidental |     | or not." |
(P14)
. However,someparticipantswarnedagainsttheconfirmationbiasitcan
trigger:
| "alltheseverypreciseindicatorscreateapush-buttonrisk: |                             |     |     |     |     |     | assoonasthere’salot |     |     |
| ----------------------------------------------------- | --------------------------- | --- | --- | --- | --- | --- | ------------------- | --- | --- |
| ofred,bang!                                           | [thealertisescalated]."(P9) |     |     |     |     |     |                     |     |     |
Bankparticipantsalsoconfirmedtheysawinvestigatorsfallintothisbias
| when testing | explanations. |     |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Supervisors also want to verify the human alignment of the decision
criteria used by AI systems (N 6 ). Even though the need for explanations
ofsupervisorsismoreglobal,theymaylookforad-hocexamplesoflocal
explanations:
| "We’remoreinterestedintheglobal[...] |     |     |     |     | We’llaskthemforlocal, |     |     | butlocalexam- |     |
| ------------------------------------ | --- | --- | --- | --- | --------------------- | --- | --- | ------------- | --- |
plesforspecificcases."(P7)
Supervisors will not only be interested in the explanation, but more im-
portantly in the justification of why or how developers have validated
| these feature | weights: |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
"Theweighthastobelessthan...,OKapriori,butwhy?"(P6)
| "It can be | a relatively | aggregated |     | explanation, |     | i.e. we’re | not trying | to  | go into the |
| ---------- | ------------ | ---------- | --- | ------------ | --- | ---------- | ---------- | --- | ----------- |
detailsofthecalculation,buttoidentifythemainsteps."(P8)
Finally, supervisors also need justifications that banks control what
| their AI | system is | doing | (N 7 ): |     |     |     |     |     |     |
| -------- | --------- | ----- | ------- | --- | --- | --- | --- | --- | --- |

208 the explanation paradox and the human centric path
-
"it’stheideathatitcreatesadependencyontheAIandthatthedaytheAIchanges
or is hacked, we don’t notice the change because we don’t know what was at the
origin?"
Feature-based importance was seen as useful to that goal:
"withthefeatureimportanceexplanation,we’llbeabletoassess: areweinagree-
mentwithallthesefactors?"(P7)
Anotherparticipantmentionedthatjustifications,suchasthedailynum-
ber of alerts generated, and periodic human verification of a sample of
alerts could be effective measures to prevent drift. Documentation was
also seen as crucial for N 7 and N 6 : documentation is super-important to
check that they master their tools (P 9 ). Certifications from third parties,
however, elicited more cautious responses. Some supervisor participants
argued that, if certification was to become the norm for AI models, it
wouldputregulatorsinthedifficultpositionofhavingtoadjustthescope
of their audits. Other participants from the AML department of the su-
pervisory authority said they would ignore this third party accreditation
which infringes upon their role.
6.5 Discussion
In this section, we discuss the importance of relying on accurate infor-
mation about AI systems to justify compliance, explanations’ limits and
alternative approaches like tests or challenger models.
6.5.1 The role of explanations for justifications
In this paper, we saw that regulators mainly seek justifications from
regulatees, i.e. argumentative demonstrations that their AI systems com-
ply with certain legal requirements. Justification is therefore a criti-
cal element in the process of enforcing regulations, i.e. for auditability
and more broadly for accountability [High-Level Expert Group on AI
2019
(HLEG), ]. Just like explanation, justification is a process [Miller,
2019
]. One participant mentioned the importance of exchanging with
regulatees. Another mentioned that "justifications are meant to be chal-
lenged" (P 11 ).
2022 2022 2019
[Henin and Le Métayer, , Hamon et al., , Hildebrandt, ]
argued that explanations are not sufficient to justify a decision. Further,
2019
Hildebrandt [ ] added "we must not allow the discourse of explain-
ability to stand in the way of the question whether a decision is legally
justified, which requires a specific type of legal reasons" [Hildebrandt,
2019 2022
, Henin and Le Métayer, ]. Additionally, Henin and Le Métayer
2022
[ ]precisethat"justificationsarecompleteonlyiftheyestablishacon-
tinuous link between the high-level objectives of the [AI system] (the ap-
plicable norms, for example non-discrimination, reduction of recidivism
rate, or compliance with a given legal requirement) and its implemen-
tation". The authors also stress that justifications are "extrinsinc" in the
sense that they refer to external norms such as legal requirements.

understanding the supervisors needs for explainable ai in financial crime
’
detection 209
However,wearguethatacceptablejustificationsaboutAIsystemsshould
also take into account descriptive, intrinsic, and accurate information
about the "implementation" of AI models, to establish this "continuous
link". Just like explanations may not always be sufficient to ensure the
legitimacy of AI systems , information about an AI system’s objectives,
design choices, or performance may not always be sufficient to justify
the proper implementation of AI models. Furthermore, justifications are
intended to be challenged and if they do not rely on factual information
about algorithms, there is a risk that the question of the legitimacy of an
AI system becomes subjective and arbitrary. In their paper about algo-
2021
rithmic audits, Koshiyama et al. [ ] argued that, without explainabil-
ity, a decision cannot be duly contested. Explanations may therefore be
insufficient, but are necessary, to provide descriptive, accurate and faith-
ful information about the behavior of an algorithm on which to develop
a justification.
64
ThelistofneedsdescribedinSection . illustratewhyregulatorsmay
need justifications from banks in AML-CFT, whether those rely on ex-
plainabilityoronotherkindsofproofsuchasdocumentationortests. In
AML-CFT, regulators not only assess results but also processes. There-
fore, looking at explanations of the inner workings of AI systems, even
2021 2020
high-level ones [Bibal et al., , Dupont et al., ], may become nec-
1 2
essary, not only for banks but also for supervisors. The needs N , N
4 64
and N in Section . reflect this.
6.5.2 Considering the limits of explanations
However, current XAI techniques may fall short of regulators’ expec-
tations to provide accurate and faithful information about AI system’s
2022 2020
inner workings. As outlined in [Hamon et al., , ], the fidelity,
robustness and truthfulness of explainability can be limited by the fact
thatthemanyfeaturesusedbycomplexalgorithmsarehighlycorrelated.
Thisisawell-studiedandstronglimitationoffeature-basedexplanations,
which make it difficult to comply with legal requirements to indicate the
2022 2013
mostimportantfactorsinadecision[Hamonetal., ,Rouvroy, ].
This goes back to the question of the reliance of AI systems on correla-
tionsratherthancausalrelationships. Thiscanbeanissueformeasuring
2022
model performance as well [Hamon et al., ].
Another issue with explanations is that they can be misinterpreted by
their users due to the technical language they usually use. Ronan et al.
callitthe"transparencyfallacy"whenexplanationsarenoteffectivelyun-
derstood. We saw this in the reaction of some of the participants in this
study, who were unsettled by the precise weightings given by the fea-
ture importance explanations. Moreover, as demonstrated by Gerlings
2022
and Constantiou [ ] and highlighted by some participants, investiga-
tors must have access to sufficient information other than explanations,
specifically risk scores, or they will fall into confirmation bias. Supervi-
sors will therefore need to verify that the context in which explanations
are presented to investigators, or supervisors themselves, takes account
of this bias and mitigates it.

210 the explanation paradox and the human centric path
-
Giventheirmostlylegalbackground, regulatorsmayalsobetooquick
toaccepttheseexplanationsastrustworthy. Moreover,theargumentative
process of transforming explanations into justifications could be used to
the advantage of regulated entities to conceal technical inaccuracies. For
2023
example, Zhouand Joachims[ ]investigate theconcept of"malicious
justification". They develop a malicious explanation system that replaces
the discriminatory factors (i.e. race) used by a biased decision model
with other, non-discriminatory factors to defend the decision. Further,
they demonstrate that it’s almost impossible even for auditors, who have
access to all the decisions, to uncover the deception. The authors also
highlight that current explanations do not provide answers to questions
like: "what factors caused the model to predict X instead of Y?". Yet,
643
as highlighted in Section . . , supervisors are likely to need such con-
4
trastive explanations to establish reprehensibility of failure cases (N ).
As a result, regulators may be in a difficult position to evaluate the ad-
equacy of explainable methods developed by banks, and may have to
develop their own "explainability challenger" toolkit.
2022
Lastly, Lima et al. [ ] argues that there is a trade-off between ac-
countabilityandexplainability,statingthatpost-hocexplanationssuchas
feature-importancecould"obscuretheresponsibilityofdevelopersinthe
decision-makingprocess". Whilethisphenomenonmightbemitigatedin
highly-regulatedindustrieswheresolidaccountabilitymechanismsarein
place, it is worth bringing this to the attention of regulators.
6.5.3 Supporting model performance measurement and test-
ing
To address the limits of explainability to audit AI systems, specifically
2023
regarding fairness, Zhou and Joachims [ ] suggest that system-wide
metrics are more useful. This was overall supported by the supervisors
interviewed in this study. In fact, system-wide evaluation is a pillar in
the auditing approaches implemented by the AML-CFT supervisor. This
isreflectedintheroleofthedocument-basedunit: assessingthematurity
ofbanks’AML-CFTsystems,andinthenewchallengermodeldeveloped
for investigations. Supervisors are therefore more likely to continue on
that "global" or "local to global" path, c.f. Section 6 . 4 . 1 .
InthefieldofAML-CFT,however,currentmetricstoevaluatetheeffec-
tiveness of systems are limited, notably because banks and supervisors,
do not know the ground truth regarding alerts, i.e. whether a suspicious
case was actually money laundering or not. Instead, they have to rely
on proxies such as number of suspicious activity reports. The supervisor
may have more feedback on the ground truth through the financial in-
vestigation unit, but perhaps not to the point that they can calculate the
precisionofthesystem,i.e. truepositivesreportedtothesumoftruepos-
itives and false positives. AI’s entry in the industry could represent an
opportunity for the supervisor to get closer to the financial investigation
unit, as one participant noted.
The consolidation and disclosure of aggregated data such as precision
ontheperformanceofAImodelsfromdifferentbankscouldbeusefulfor

understanding the supervisors needs for explainable ai in financial crime
’
detection 211
the regulated entities self-assessment and research purposes. In health-
care, the disclosure of a database of AI-based medical technologies with
regulatory approvals enabled researchers to point out some AI weak-
nesses[MeskóandTopol, 2023 ]. Further,suchinitiativescanhelprespect
the due process rights of regulated entities (N 2 ), while striking a balance
| with advancing | the fight | against financial | crime. |     |
| -------------- | --------- | ----------------- | ------ | --- |
However,thisapproachdoesnotinformonthefalsenegativesofAML-
CFT systems. Challenger models such as LUCIA can do this to some
extent by identifying some crimes that have fallen through the cracks.
However,theycannotfullymeasurethetrueproportionofcrimethathas
not been detected. This calls for relative comparisons instead of absolute
ones, such as comparing banks’ practices or pre-AI systems as outlined
by participants.
Lastly, to verify processes in addition to results, supervisors in this
study have proposed some testing and human oversight mechanisms.
More advanced testing methods will however have to be developed to
prevent risks specific to AI such as drift, discrimination, over-reliance on
AI. Certifications of the model development were seen as overlapping
with supervisors’ role. Discussions between certification providers and
supervisors might be beneficial to talk about best practices, such as stan-
dard models for documentation [Mitchell et al., 2019 , Gebru et al., 2021 ],
or mathematical proofs that a code is correct, when applicable [Henin
2022
| and Le Métayer, | ].          |                   |            |     |
| --------------- | ----------- | ----------------- | ---------- | --- |
| In summary,     | future work | could investigate | the design | of: |
• contrastive explanations to help supervisors establish reprehensibility
| of failure | cases (N 4 ), |     |     |     |
| ---------- | ------------- | --- | --- | --- |
• meaningful sectorial, system-wide, metrics and databases to compare
the efficiency of AI-enhanced systems in relation to each other or to
3
| pre-AI | systems (N ), |     |     |     |
| ------ | ------------- | --- | --- | --- |
• meaningful tests for AI to support supervisors in verifying correct use
|         | 5                                    |     |     | 6              |
| ------- | ------------------------------------ | --- | --- | -------------- |
| ofXAI(N | ),humanalignmentofdecisioncriteria(N |     |     | )andmodeldrift |
7
| control | (N ). |     |     |     |
| ------- | ----- | --- | --- | --- |

212 the explanation paradox and the human centric path
-
6.6 Limitations
As the scenario-based elicitation task came fairly early in supervisors’
thinking about the use and audit of AI, their responses may not include
in-depth considerations on the issue. The purpose of this paper was to
articulate the needs of supervisors at a time when the use of AI in AML-
CFTandinvestigationsintoAI-enhancedsystemsareintheirinfancy. We
recognise that their needs may evolve as AI audits in AML-CFT develop
and new regulatory and case law guidance is issued. Moreover, our re-
search results rely on the specific scenarios and artefacts we presented to
participants. This may limit the scope and generalisablity of the results.
Specifically,weinvestigatedtwousecasesofAI,whichareconsideredas
the most common and promising in the literature, but other AI applica-
2018
tions exist [Chen et al., ]. We also limited the number of conceptual
explanations and justifications to six to not overwhelm the participants
and to respect their time as volunteers. Other explanations could be
considered in future explorations with regulators. Further, we described
in the methodology section that two workshops were not recorded due
to participants’ concerns, we are aware that this limits the analysis and
findings from those workshops. However, we were able to conduct a
recorded interview with one of the participants in an unrecorded work-
shop, which enabled us to study the views of this person more closely.
Finally,asthefirstauthorwhoconductedthelegalapproachhasnolegal
training, the method remains fairly straightforward, but we did put in
place quality controls with another author, who has a legal background,
and two AML-CFT experts. We hope this study demonstrates the feasi-
bility and suitability of such an approach for HCI practitioners.
6.7 Conclusion
In this chapter, we examined a socio-techno-legal supervision system
in a highly-regulated industry, taking the example of the anti-money
laundering and countering terrorism financing domain (AML-CFT) in
6
France. We drew on workshops with supervisors and bank practi-
tioners to outline the auditing approaches of AML-CFT supervisors. We
then outlined AML-CFT compliance requirements which raise clear is-
sues with AI opacity, and drew up a list of seven model justifiability
needs for the supervisors, integrating explainability aspects. In partic-
ular, we found that supervisors primarily need to measure the perfor-
mance of the AI-enhanced AML-CFT system. However, supervisors may
needcontrastiveAIexplanationstoestablishthereprehensibilityofsam-
pled failure cases, to verify and challenge banks’ correct understanding
of the AI and to demonstrate the legitimacy of their challenger model.
These needs are intricately linked to the regulations that supervisors en-
force, hence the need for a dual interview-based and legal approach. We
alsopresentedexplanationsashavingaroleof"trialevidence"forjustifi-
cations. We hope that this work will inform future research to design AI
justifications for regulators.

understanding the supervisors needs for explainable ai in financial crime
’
|             |             |                |                  |                  | detection  | 213      |
| ----------- | ----------- | -------------- | ---------------- | ---------------- | ---------- | -------- |
|             |             |                |                  | Familiarity with | Workshop   |          |
| Participant |             |                | Years in profes- |                  |            |          |
|             | Role        |                |                  | AI(ona7points    | and Inter- | Recorded |
| ID          |             |                | sion             |                  |            |          |
|             |             |                |                  | Likertscale)     | viewID     |          |
|             | Supervisor, | document-based |                  |                  |            |          |
| P1          |             |                | >10              | 2                | W1         | Yes      |
control
| P2  |                           |                | >10          | 3   | W1  |     |
| --- | ------------------------- | -------------- | ------------ | --- | --- | --- |
|     | Supervisor,on-sitecontrol |                |              |     |     | Yes |
|     | Supervisor,               | document-based |              |     |     |     |
| P3  |                           |                | Between1and3 | 3   | W2  | Yes |
control
|     | Supervisor, | document-based |               |     |     |     |
| --- | ----------- | -------------- | ------------- | --- | --- | --- |
| P4  |             |                | Between4and10 | 3   | W2  |     |
Yes
control
|     | Supervisor, | document-based |              |     |     |     |
| --- | ----------- | -------------- | ------------ | --- | --- | --- |
| P5  |             |                | Between1and3 | 3   | W2  | Yes |
control
| P6  | Supervisor, | document-based |               | 3   | W3  |     |
| --- | ----------- | -------------- | ------------- | --- | --- | --- |
|     |             |                | Lessthanayear |     |     | Yes |
control
|     | Supervisor, | document-based |               |     |     |     |
| --- | ----------- | -------------- | ------------- | --- | --- | --- |
| P7  |             |                | Between4and10 | 5   | W3  | Yes |
control
| P8  | Supervisor, | document-based | Between4and10 | 3   | W3  |     |
| --- | ----------- | -------------- | ------------- | --- | --- | --- |
Yes
control
| P9  | Supervisor,on-sitecontrol |     | Between1and3  | 7   | W4    | No  |
| --- | ------------------------- | --- | ------------- | --- | ----- | --- |
| P10 |                           |     | Between4and10 | 7   | W4,I1 | No, |
Supervisor,on-sitecontrol
Yes
| P11 | Supervisor,on-sitecontrol |            | Between4and10 | 1   | W5  | Yes |
| --- | ------------------------- | ---------- | ------------- | --- | --- | --- |
| P12 | Supervisor,on-sitecontrol |            | Between4and10 | 3   | W5  | Yes |
| P13 |                           |            | Between4and10 | 3   | W5  |     |
|     | Supervisor,on-sitecontrol |            |               |     |     | Yes |
| P14 | Supervisor,AML-CFTpolicy  |            | >10           | 6   | I2  | Yes |
| P15 | Bank, Head                | of AML-CFT | com- >10      | 3   | W6  |     |
No
pliance
| P16 | Bank,Headofdatascience |            | Between4and10 | 7   | W6  | No  |
| --- | ---------------------- | ---------- | ------------- | --- | --- | --- |
|     | Bank, AML-CFT          | Compliance |               |     |     |     |
| P17 |                        |            | Between4and10 | 1   | W6  |     |
No
Officer
|     | Bank, AML-CFT | Compliance |               |     |     |     |
| --- | ------------- | ---------- | ------------- | --- | --- | --- |
| P18 |               |            | Between4and10 | 3   | W6  | No  |
Officer
| P19 | Bank,Datascientist |     | Between1and3 | 7   | W6  | No  |
| --- | ------------------ | --- | ------------ | --- | --- | --- |
| P20 |                    |     | Between1and3 | 7   | W6  |     |
|     | Bank,Datascientist |     |              |     |     | No  |
Table6.1:
Descriptionof
|     |     |     |     |     | role, experience, | famil-        |
| --- | --- | --- | --- | --- | ----------------- | ------------- |
|     |     |     |     |     | iarity with       | AI of partic- |
ipantsinthestudy.

| 214 the | explanation |     | paradox | and | the human |     | centric | path |     |     |     |
| ------- | ----------- | --- | ------- | --- | --------- | --- | ------- | ---- | --- | --- | --- |
-
6.2:
| Type |     | Document |     |     |     |     |     |     |     | Table Data    | used for  |
| ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------- |
|      |     |          |     |     |     |     |     |     |     | the empirical | legal re- |
Regulatory • Sanction Commission Decision 2022-04 against BMW Fi-
search
nance
•SanctionCommissionDecision2022-02againstFinancière
sanctioncases
despaiementsélectroniques
2022-01
|     |     | • Sanction |     | Commission | Decision |     |     | against | Axa |     |     |
| --- | --- | ---------- | --- | ---------- | -------- | --- | --- | ------- | --- | --- | --- |
Banque
|     |     | • Sanction | Commission |     | Decision | 2021-05 | of  | 1 December |     |     |     |
| --- | --- | ---------- | ---------- | --- | -------- | ------- | --- | ---------- | --- | --- | --- |
2022againstCaisserégionaledeCréditagricolemutueldu
Languedoc
|     |     |            |            |     |          | 2021-01 |     | 1     | 2022 |     |     |
| --- | --- | ---------- | ---------- | --- | -------- | ------- | --- | ----- | ---- | --- | --- |
|     |     | • Sanction | Commission |     | Decision |         | of  | March |      |     |     |
againstW-HA
| Law,orders |     | •AML-CFT:ArticlesL561-1toL564-2oftheFrenchMone- |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
taryandFinancialCode[Légifrance,2023b]
|     |     | • Internal | control: |         | French Monetary |     | and Financial |       | Code, |     |     |
| --- | --- | ---------- | -------- | ------- | --------------- | --- | ------------- | ----- | ----- | --- | --- |
|     |     |            | L511-55, | L522-6, | L522-14         |     | L526-27,      |       |       |     |     |
|     |     | Articles   |          |         |                 | and |               | Order | of    |     |     |
November3rd,2014[Légifrance,2023a].
Softlaw • Joint ACPR and Tracfin guidelines on reporting obliga-
tionstoTRACFIN
|     |     | • Thematic | review: |     | Automated | systems | for monitoring |     | of  |     |     |
| --- | --- | ---------- | ------- | --- | --------- | ------- | -------------- | --- | --- | --- | --- |
AML-CFTtransactions
| Interviews |     | •5Workshopswith13supervisors/controllers |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
•2Interviewswith2AI/AML-CFTsupervisors

understanding the supervisors needs for explainable ai in financial crime
’
|     |     |     |     |     |     |     |     |     |     | detection |     | 215 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
Description and related regulatory Model/XAIDe- Design ideas for explana-
Need
|     |     | goal                            |     |     |     |     | veloper    |     | tionsandjustifications |     |            |     |
| --- | --- | ------------------------------- | --- | --- | --- | --- | ---------- | --- | ---------------------- | --- | ---------- | --- |
|     |     | Understandhowthechallengermodel |     |     |     |     |            |     | High-level             |     | and global | ex- |
|     |     |                                 |     |     |     |     | Challenger | and |                        |     |            |     |
works to extract relevant and repre- planation, practice using
| N1: | General |     |     |     |     |     | Bank model |     | /   |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
sentativecasesamples. Haveageneral the model and training, de-
| comprehension |     |                                  |     |     |     |     | Supervisor | and |            |     |             |     |
| ------------- | --- | -------------------------------- | --- | --- | --- | --- | ---------- | --- | ---------- | --- | ----------- | --- |
|               |     | understandingofhowthebanks’algo- |     |     |     |     |            |     | scriptions | and | motivations |     |
|               |     | rithmworks(RG6).                 |     |     |     |     | Banks      |     |            |     |             |     |
ofAI’srole
| N2: Ensure  | le-      | Monitorperformanceofthechallenger |                  |       |                |           |              |        |                        |              |          |          |
| ----------- | -------- | --------------------------------- | ---------------- | ----- | -------------- | --------- | ------------ | ------ | ---------------------- | ------------ | -------- | -------- |
|             |          |                                   |                  |       |                |           | Challenger   |        | Global                 | explanation, |          | specific |
| gitimacy    | and ef-  | model                             | and make         | banks | appreciate     |           |              |        |                        |              |          |          |
|             |          |                                   |                  |       |                |           | model /      | Super- | question-answering     |              |          | with     |
| ficiency    | of chal- | the                               | overall workings | of    | the challenger |           |              |        |                        |              |          |          |
|             |          |                                   |                  |       |                |           | visor        |        | banks                  |              |          |          |
| lengermodel |          | model.                            |                  |       |                |           |              |        |                        |              |          |          |
|             |          |                                   |                  |       |                |           |              |        | Performance            |              | metrics: | de-      |
|             |          | Measure                           | the performance  |       | of             | the algo- |              |        | lays,numberofSARs,num- |              |          |          |
|             |          |                                   |                  |       |                |           | Bank’s model |        | /                      |              |          |          |
N3: Measureeffi- rithm, not only in absolute terms but ber of reinforced exami-
|     |     |     |     |     |     |     | Bank and | Super- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --- | --- | --- | --- |
ciency alsomoreconcretelyinarelativeway. nations, sampling analysis,
|     |     | Linkedto(RG1),(RG2),(RG3). |     |     |     |     | visor |     |           |          |     |          |
| --- | --- | -------------------------- | --- | --- | --- | --- | ----- | --- | --------- | -------- | --- | -------- |
|     |     |                            |     |     |     |     |       |     | Tracfin’s | feedback |     | on alert |
quality
|               |     | Understand | why        | a bank’s     | algorithm |          |     |     |     |     |     |     |
| ------------- | --- | ---------- | ---------- | ------------ | --------- | -------- | --- | --- | --- | --- | --- | --- |
| N4: Establish | the | did        | not detect | a suspicious |           | case, so |     |     |     |     |     |     |
reprehensibility as to understand if it was an iso- Bank’s model / Local feature importance,
of sampled error latedeventorpartofabiggerpattern: Supervisor Conterfactualexplanations
| cases |     | is the | error systematic, |     | reprehensible? |     |     |     |     |     |     |     |
| ----- | --- | ------ | ----------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Linkedto(RG1),(RG2),(RG3).
|              |        | Ensure                            | that banking  |     | analysts   | have   | a            |     |                |     |            |        |
| ------------ | ------ | --------------------------------- | ------------- | --- | ---------- | ------ | ------------ | --- | -------------- | --- | ---------- | ------ |
| N5:          |        |                                   |               |     |            |        |              |     | Justifications |     | that       | expla- |
| Verify       | cor-   | clear                             | understanding | of  | the alerts | they   |              |     |                |     |            |        |
|              |        |                                   |               |     |            |        | Bank’s model |     | / nations      | for | analysts   | are    |
| rect use     | of ex- | arerequiredtohandle,sothattheycan |               |     |            |        |              |     |                |     |            |        |
|              |        |                                   |               |     |            |        | Bank         |     | present        | and | efficient, | alert  |
| plainability |        | producehigh-qualityanalyses.      |               |     |            | Linked |              |     |                |     |            |        |
contextualisations
(RQ3),(RQ4),(RG5).
N6: Verify that the criteria used by AI to Feature combination used
| Verify | hu- |     |     |     |     |     |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
generate or escalate alerts are con- for few cases with justifica-
| man alignment |     |     |     |     |     |     | Bank’s model |     | /   |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- |
sistent with the risk exposure and tions of the weights (divide
| of decision | crite- |                            |     |     |     |        | Bank |     |                            |     |     |     |
| ----------- | ------ | -------------------------- | --- | --- | --- | ------ | ---- | --- | -------------------------- | --- | --- | --- |
|             |        | alignedwithhumanexpertise. |     |     |     | Linked |      |     | featuresfulllistintogroups |     |     |     |
ria
|     |     | to(RG1),(RG6) |     |     |     |     |     |     | forreadability) |     |     |     |
| --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- |
Justifytheexistenceandrel-
| N7:         |        |                                 |            |            |     |          |              |     | evanceoftests: |            | Periodically |          |
| ----------- | ------ | ------------------------------- | ---------- | ---------- | --- | -------- | ------------ | --- | -------------- | ---------- | ------------ | -------- |
| Verifymodel |        | Ensurethatthebank’smodeldoesnot |            |            |     |          |              |     |                |            |              |          |
|             |        |                                 |            |            |     |          | Bank’s model |     | / draw         | up a       | list of      | impor-   |
| control     | by the | drift                           | over time, | that there | is  | no bias. |              |     |                |            |              |          |
|             |        |                                 |            |            |     |          | Bank         |     | tant           | factors,   | periodic     | hu-      |
| bank        |        | Linkedto(RG4).                  |            |            |     |          |              |     |                |            |              |          |
|             |        |                                 |            |            |     |          |              |     | man            | evaluation | of           | an alert |
sample
6.3:
|     |     |     |     |     |     |     |     |     |     | Table           |           | Summary         |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | --------------- |
|     |     |     |     |     |     |     |     |     |     | of supervisors’ |           | needs           |
|     |     |     |     |     |     |     |     |     |     | for model       |           | justifiability, |
|     |     |     |     |     |     |     |     |     |     | corresponding   |           | descrip-        |
|     |     |     |     |     |     |     |     |     |     | tion,           | model     | concerned       |
|     |     |     |     |     |     |     |     |     |     | and             | developer | of justi-       |
fications/explanations,
|     |     |     |     |     |     |     |     |     |     | and         | justification | and     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------- | ------- |
|     |     |     |     |     |     |     |     |     |     | explanation |               | design  |
|     |     |     |     |     |     |     |     |     |     | ideas       | that          | emerged |
duringtheworkshops.

| 216 the | explanation | paradox | and the human | centric path |
| ------- | ----------- | ------- | ------------- | ------------ |
-

| Chapter | 7   |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Discussion
| his chapter | presents |              |     |     |              |     |        |          |
| ----------- | -------- | ------------ | --- | --- | ------------ | --- | ------ | -------- |
| T           |          | a discussion |     | and | a conclusion |     | of the | findings |
of this thesis. We first summarize the research contributions made in
71
this dissertation in Section . . The following sections are devoted to
|     |     |     |     |     |     |     | 72  | 73  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
a discussion of our findings and future work. In Sections . and . ,
we discuss the "explanation paradox" for decision-subjects of AI-based
decisionsandthehuman-centricavenuestoimproveuserempowerment.
InSection 74 . ,wereviewtheroleofexplainabilitytoalleviatesomeofthe
regulatory tension created by black-box AI models in AML-CFT. We also
highlight the relevance of the human-centric approach for implementing
explainabilityeffectivelyintheAML-CFTcontext. Finally, thediscussion
presents some thoughts on the lessons from the financial sector for other
industries, on my experience as an interdisciplinary researcher, or on the
challenge posed by Large Language Models for the explainability field.
| 7.1 Research |     | contributions |     |     |     |     |     |     |
| ------------ | --- | ------------- | --- | --- | --- | --- | --- | --- |
In this thesis, we investigated the research question: To what extent can
AI explanations enable warranted trust and regulatory compliance in financial
applications? In Part I, we focused on the cognitive challenges for expla-
nations to enable warranted trust, i.e. trust that is well-calibrated. In
Part II, we explored how explanations can contribute to customer and
regulator warranted trust, and enable compliance in two use cases in fi-
nance. We summarize below the research contributions presented in this
dissertation.
Part I: Calibrating trust in explainable AI: common pitfalls and the
| promise of | interactivity |            |          |     |                |     |       |           |
| ---------- | ------------- | ---------- | -------- | --- | -------------- | --- | ----- | --------- |
| Chapter    | 3: Trust,     | overtrust, | distrust |     | in explainable |     | AI: a | cognitive |
approach
– Weprovidedageneralvisionofwhatandhowcognitivebiasesaffect
| explainability      | systems: | with        | which   | XAI         | technique |           | (e.g., counterfac- |            |
| ------------------- | -------- | ----------- | ------- | ----------- | --------- | --------- | ------------------ | ---------- |
| tual explanations), |          | user type   | (domain |             | expert,   | AI expert | or                 | lay users) |
| and AI-assisted     |          | task (e.g., | medical | diagnosis). |           |           |                    |            |
– We highlighted how explainable AI can lead to overtrust, distrust, or
| how it can | be misinterpreted. |     | Some | implementations |     |     | of explainable |     |
| ---------- | ------------------ | --- | ---- | --------------- | --- | --- | -------------- | --- |

218 the explanation paradox and the human centric path
-
AI, however, have proven useful in correcting prior human biases in
decision-making. We also emphasize that cognitive biases may affect
the evaluation of explanations.
– Overall, we found that explanations usually have a tendency to in-
crease trust, specifically for lay users, and potentially lead to unwar-
ranted trust.
– We summarized several important factors at play in trust calibration
with explainable AI systems, including user expertise, task expertise
and task familiarity, estimation of the AI’s confidence, explanation
completeness,timingofexplanationsandusers’motivationandindi-
vidual cognitive characteristics (need for cognition, rational or intu-
itive decision-making style...).
Chapter 4: Towards "human-like" explanations: the promise of in-
teractivity
– We adapted existing HCI taxonomies of interactivity to create a two-
level taxonomy of interactive techniques specific to XAI, describing
the interaction types and the way they support the human cognitive
process of explaining: "selective", "mutable" or "dialogic".
– Weanalyzedtheextent,natureanddistributionoftheinteractiveXAI
systems included in the review.
– We offered a summary of the user-based evaluation metrics imple-
mented in interactive XAI.
– We offered a qualitative summary of the effects of interactive expla-
nations on several user-based evaluation metrics, finding that inter-
active explanations increase trust, but not necessarily overtrust, and
thatinteractiveexplanationsaremoreusefulthanstaticones,butless
easy to use and more time-consuming.
Part II: Complying with regulation using human-centric explainable
AI: two case studies in finance
Chapter 5: Empowering customers of robo-advisors with explain-
ability
– We developed a fictitious but realistic rule-based recommendation
system for life insurance plans, "Robex", based on interviews with
insurance supervisors and on market research.
– We created prototype explanations for Robex and redesigned them
based on feedback from insurance regulators, customer protection
specialists and end-users with no experience of life insurance invest-
ments.
2 4
– Inourstudy,whichinvolveda x between-subjectsexperimentwith
256
participants,wefoundthatexplanationsdidnotcontributetothe
legal objectives of financial regulation to empower users. Explana-
tions did not significantly improve understanding, appropriate trust
or reliance, revealing a misalignment between legal objectives and
actual observed benefits of explanations.

discussion 219
– Wehighlightedhowexplanationsstillcontributetothelegalobjective
of enhancing accountability of life insurance distributors by forcing
them to provide written reasons why a given financial product is
adapted to the customer’s profile.
Chapter 6: Understanding the supervisors’ needs for explainable AI
in financial crime detectiony
– Wedescribedthesocio-techno-legalsupervisionsystemandauditing
approaches in the AML-CFT context. We reveal three main auditing
approaches: global, from global to local, and from local to global.
The global approach is focused on measuring the performance of the
system, the global to local approach is used to sample cases where
regulators discovered mistakes, and the local to global approach at-
tempts at establishing the seriousness, and therefore the reprehen-
sibility of the error on the whole AML system put in place by the
financial institution.
– We assessed compliance obligations specific to AI-enhanced AML-
CFT systems highlighting why the opacity of AI models may pose
problems with regard to AML-CFT obligations.
– We formulated seven needs that supervisors have regarding model
justifications and explanations. In particular, we find that supervi-
sors primarily need to measure the performance of the AI-enhanced
AML-CFT system such as gaps in detection (false negatives). How-
ever, supervisors may need contrastive AI explanations to establish
the reprehensibility of sampled failure cases, to verify and challenge
banks’ correct understanding of the AI and to demonstrate the legit-
imacy of their challenger model.
– WedemonstratedthecomplementarityofadualHCIandlegalmethod-
ology to fully understand regulatory supervisors’ justification needs.
– Wearguedthatexplanationshavearoleof"trialevidence"tosupport
justifications. Justifications should not only be extrinsic by referring
2022
tonormsorregulations[HeninandLeMétayer, ],butalsointrin-
sic by depending on faithful evidence of the system’s behavior that
explanations can provide.

220 the explanation paradox and the human centric path
-
7.2 The potential of explanations to manipulate
decision-subjects’ trust
Inthisdissertation, weexaminedwhetherexplanationscouldenhance
the understanding, appropriate reliance, and trust of lay users, in order
toachievetheregulatoryobjectiveofuserempowerment—individualau-
tonomy,agency,freechoice,informedconsent—isanimportantobjective
of many legal texts imposing explanations. Specifically, we appreciated
the complexity of the user empowerment problem and encountered an
"explanationparadox". Ontheonehand,itappearslogicalandnecessary
to give individuals who are subject to an AI decision access to important
informationaboutthedecisionmadeaboutthem. Ontheotherhand, we
revealedthatexplanationstendtoincreaseunwarrantedtrust,anddonot
appear to improve significantly users’ understanding of the decisions in
thelife-insurancecontext,wheredomain(financial)knowledgeisimpor-
tant. Explanationsplayaimportantroleinempoweringend-users, while
also having the potential to create inappropriate trust and reliance.
Thissectiondescribesthepotentialforuserstobemanipulatedthrough
explanations. The following section will focus on the human-centric av-
enues that show promise for more effective explanations.
Much of the discussion below draws a comparison between meaning-
ful consent to data practices, which has been extensively studied in the
privacy literature, and meaningful consent to a decision made by an on-
line AI-based recommendation system. Consent for data processing and
AI recommendations share similar challenges in correcting power imbal-
ances between data/decision subjects and data/AI operators [Acquisti
2015
et al., ].
7.2.1 The Self-governance fallacy
Our observations echo the warning of some legal scholars who have
stressed that end-user meaningful consent in the digital age is a theoreti-
2020 2015 2020
calandunattainableideal[Obar, ,Pasquale, ]. Obar[ ]char-
acterized the situation as: "the seemingly impossible scenario of achieving,
consistently and ubiquitously, meaningful forms of consent". This is known
as the self-governance fallacy. Self-governance by end-users is an ideal
that aims to empower users to understand, then consent to or decline
the decisions made about them or their data. However, in the era of
big data and profiling, it seems unrealistic to expect end-users to con-
2015
trol every decision they are subject to. Pasquale [ ] argued that the
"boring, time-consuming and overwhelming" nature of online consent,
coupled with its mismatch with end users’ real goals, who just want to
use a service, make it unrealistic to expect end users to engage in "tan-
gential"discussionsaboutdatapolicy(i.e.,informationthatdoesnothave
2020
todowiththeuser’ssearch). Furthermore,Morleyetal.[ ]described
how the self-governance approach risks creating a complex mechanism
of victim-blaming in case of failure. When "empowering" an individual
by providing them with choices and tools, responsibility is shifted to the
individualincasesomethinggoeswrong. Inthehealthcarecontext,Mor-

discussion 221
2020
ley et al. [ ] describe how an individual may be seen as a "bad actor"
for failing to follow the algorithm’s advice and be framed as morally
responsible for his or her poor health.
7.2.2 The dark pattern potential of explanations
At the same time, the objective of user empowerment stems from a
genuine concern that online recommendations can be harmful to end-
users when the interests of online service providers and users are not
2023
aligned. Rozen et al. [ ] spoke of "dark patterns" in explainability to
refer to the situation where the effect of explanations to increase trust is
used to the advantage of the service provider and to the detriment of the
user: "this phenomenon of nudging users to act according to others’ interest
is known as "Dark Patterns" in XAI and benefits from humans’ automation
bias towards trusting machines [Gray et al., 2018 , Rozen et al., 2023 ]. In
2020
the context of data protection, Waldman [ ] argues that dark patterns
1
exploit users’ cognitive biases to nudge users to cede control over their 1For example, the
privacy. Mathur et al. [ 2019 ] define dark patterns as: author mentions hy-
perbolic discounting, a
Definition tendency to overweight
immediate conse-
Dark patterns. "Interface design choices that benefit an online service quences and discount
longertermones.
by coercing, steering, or deceiving users into making decisions that, if fully
informedandcapableofselectingalternatives,theymightnotmake."[Mathur
et al., 2019].
Explanations can have the effect to disguise relevant or even contradic-
tory information as evidence in favour of a product that is inappropriate
5
for the user. In the experiment we presented in Chapter , participants
who accepted incorrect life-insurance proposals explained in the course
of dialogic explanations did not process the contradictory information
presented in the explanations. Instead, the explanations had the oppos-
2016
ing effect of reinforcing trust. Following Bösch et al. [ ]’s taxonomy
of dark patterns, explanations could therefore fall into the dark pattern
category of "Hidden Legalese Stipulations", which consists of hiding ma-
licious information in lengthy legal paragraphs. Alternatively, untrust-
worthyexplanationsmaybeincludedinthebroader"Sneaking"category
2018
of Gray et al. [ ], where dark patterns are used to hide, disguise or
delay information that is relevant to the user.
7.2.3 Safeguards against user manipulation for critical on-
line decisions
The discussions on dark patterns or self-governance in academic lit-
erature have primarily focused on data privacy issues. In the privacy
context, Waldman contends that the "predatory behavior" of online plat-
forms is made possible because the law, "based on the myth of rational
disclosure", allows it [Waldman, 2020 ]. As a result, Waldman argues that
online privacy shouldbe better regulated byrequiring large platforms to
ensure the trustworthiness of their systems.

222 the explanation paradox and the human centric path
-
5
However, in the context investigated in Chapter , which pertains to
online recommendations for life insurance contracts, recommender sys-
tems must be trustworthy by law. In finance and other highly regulated
environments, regulators and internal compliance systems act as safe-
guards against the manipulation of user trust and dark patterns, ahead
of the protection provided by user self-governance. The risk of using ex-
planations as "dark patterns" is therefore lower for critical decisions that
are subject to important regulation. In life insurance, it can be assumed
2020
that the ’fiduciary model’ described by Obar [ ] is applicable. This
modelpositionstherobo-advisercompanyasafiduciary, responsiblefor
ensuring that the user’s best interests are served and that relevant infor-
mation is presented in an understandable manner.
However, the challenge of self-governance and consent remains preva-
lent in finance and other regulated industries. The legal concept of "en-
lightened choice" in life insurance is not solely intended for users to val-
idate their decisions, as recommendations are expected to be reliable.
Rather, it is intended to ensure that users understand the decisions they
are making. This can be particularly challenging in regulated environ-
ments where there is a significant domain knowledge requirement and
information asymmetry.
7.3 Human-centric directions for improved cus-
tomer empowerment
Explanations may not always have the intended effect of improving
userunderstandingandtrust,despiteregulatoryexpectations. Therefore,
itisimportanttoavoidthemisconceptionthatexplanationsareacure-all
for user empowerment and instead take a more realistic approach.
However,providingdecision-subjectswithrelevantinformationonthe
decisionremainscriticalandnecessary,specificallyforonlinerecommen-
dations for which human advisors are usually unavailable. The research
in this dissertation shows that human-centric explainability still has a es-
sential role to play to communicate important information to the user.
Explanation interfaces may not be useful for everyone at all times, but
wecanoptimizetheirdesigntomakethem"goodenough",i.e. usefulfor
as many users as possible, most of the time. The explanation interfaces
5
designed in Chapter offer only a few examples of the many design
choices available. More research needs to be done to craft quality inter-
actions to support customers’ understanding of AI-based decisions. In
whatfollows,Ioutlinesomepromisinghuman-centricwaysofdesigning
explanations that are worth presenting to users, and that avoid, as much
as possible, the pitfalls of over-reliance and uselessness for understand-
ing.
7.3.1 Thinking beyond information access
2020
According to Obar [ ], part of the problem is that the discussion
of user control and empowerment in legal and policy literature usually

discussion 223
ends at the point of access of information. The author states: "once indi-
viduals have access to notice and choice manifestations, then what?". In legal
discussion,moreemphasisshouldbeputonthe"toolsforconvertingnotice
materials into meaningful consent". Obar also discusses "a modified scenario
where users receive summaries as opposed to details, guidance as opposed to full
autonomy, support as opposed to silence". The turn that explainability has
taken in recent years towards making explanations more visual, concise
2023
and interactive precisely aims at answering this call [Ooge, ].
In this thesis, we have linked legal and policy discussions on the non-
expert user control problem to this current trend in explainability, which
focuses on making information intelligible. The interactive, visual and
dialogic explanation approaches we tested showed disappointing results
in terms of end-user empowerment. However, many more explanation
design strategies remain to be tested. Specifically, below I highlight that
the explainability field has yet to fully exploit a wealth of research in
educational psychology.
The problem is as follows: How can explanations of online AI-based rec-
ommendationsfostertheempowermentofdecision-subjects,specificallytheirun-
derstanding of decisions, and prevent user manipulation? Below, we discuss
three pathways to address the issue of client empowerment through ex-
plainability interface design:
1
. Tailoring explanations to relevant user communities
2
. Stimulating skepticism
3
. Presenting a selected range of options
4
. Fostering user engagement, curiosity and learning
7.3.2 Tailoring explanations to relevant user communities
In their discussion on the right to explanations for data protection,
Wachter et al. [ 2017 ] highlighted that: "What counts as a meaningful expla-
nation for one individual or group may not be meaningful for another". The
research community in explainability and HCI has also emphasized the
2023
importanceofadaptingtotheneedsofdifferentusergroups[Ooge, ,
2019
Cheng et al., ]. This involves striking a balance between one-size-
fits-allandindividualizedinterfacestoefficientlymeettheneedsofmost
2006 1999
users [Bødker, ]. As highlighted in [Stephanidis et al., ], the
information society and now AI have brought us to a world where peo-
ple are becoming increasingly dependent on online and AI-based ser-
vices, and where AI decision subjects are not necessarily domain experts
and have different skills, needs and preferences. This underlines the
need for designing human-centred and high-quality technological inter-
actions. Specifically, it requires the identification of relevant user com-
munities, within which individuals share key characteristics influencing
1999
explanation design and have the same needs [Stephanidis et al., ].
The HCI discipline has a long history of "fitting" a computer artefact to a
2009
specificusergroupandproblemsetting[AvitalandTe’eni, ]. Forex-
1991
ample, Vessey and Galletta [ ]discussed cognitive and Goodhue and

224 the explanation paradox and the human centric path
-
1995
Thompson [ ] organizational task technology fit. I am hopeful that,
in the near future, HCI research efforts will be able to identify the key
individual cognitive factors that influence explanation effectiveness and
"fit" explainability interfaces to maximize understanding among the user
groupsformedbytheseidentifiedcharacteristics. Todate,littleisknown
about whether, which and how other aspects of a user’s personality and
profile, such as information processing styles, general intellectual ability,
1997
personal goals [Klaczynski et al., ], should affect the design of ex-
2020 3
planations [Naiseh et al., ]. In Chapter , we highlighted that user
domainknowledge,personalgoals,orneedforcognitionhavebeeniden-
tified in the literature as influential in the way users process information
1997 5
andexplanations[Klaczynskietal., ]. However,inChapter ,wedid
not test whether different explanation strategies could be used for differ-
ent user domain knowledge. Future work could address this question.
Itcanbenotedthatadaptingexplanationtechniquestoindividualpro-
files raises two legal challenges. First, the explainer must know some-
thingaboutthepersonreceivingtheexplanation. Thishappensnaturally
in person-to-person communications. In online contexts, the creation of
profiles, even for the sake of providing effective explanations, raises pri-
vacy concerns. Second, providing varying levels of information to differ-
ent user groups may raise concerns about unequal treatment, especially
if some groups receive less comprehensive information.
7.3.3 Stimulating skepticism
As previously mentioned, tangential explanations about the reasons
for receiving the recommendation may not always be in line with the
goals of the users, who are primarily interested in using the service, es-
pecially for low-stake decisions. One design approach therefore consists
in forcing users to pay attention to explanations through friction. Some
work has tested hiding explanations by default, or forcing users to at-
tend explanations through friction-based interface design. For example,
2021
Buçinca et al. [ ] tested three friction-based designs: time counters,
whichconsistinmakingtheuserwaitforacertainamountoftimebefore
seeing the AI decision, on-demand buttons, which consist in displaying
theexplanationonlyon-demandoftheuser, anduncertainty, whichcon-
sists in showing probability of the AI’s prediction (e.g., "the AI is 81 %
confident in its suggestion").
Another possible friction-based design might be to make the warn-
ings about the risks of the AI proposal more prominent. Buçinca et al.
2021
[ ] found that friction-based explanations reduced significantly over-
reliance, at the expense of user satisfaction, however. This approach ex-
ploits users’ possible suspicion that the service provider is not acting
in their best interests. The lack of transparency and certainty, or the
perceived risk of the AI suggestion can foster users’ skepticism and crit-
1997
ical thinking. According to Klaczynski et al. [ ], threatening prob-
lems induces more sophisticated reasoning than goal-enhancing prob-
lems. However, the effectiveness of friction-based design in improving
understanding and learning has yet to be tested experimentally.

discussion 225
7.3.4 Presenting a selected range of options
Promisingavenuesforexplainabilitytobetteralignwithhuman’scog-
2023
nitive architecture include Evaluative XAI [Miller, ], in which expla-
nations are provided without the AI recommendations to avoid confir-
mation bias and clarify alternatives and trade-offs. For the same reason,
some researchers have advocated presenting multiple recommendations
rather than a single one. This follows the important observation that
good advice does not necessarily have to be presented as a single rec-
2023
ommendation [Miller, ]. While this approach may seem useful and
necessary for experts such as doctors to make critical decisions, it may
notbeappropriateinallcontextsandtocurrentbusinesspractices,which
seek to satisfy users’ demand for fast, clear and therefore single advice
to follow. Avoiding presenting recommendations defeats the purpose
of providing a service in the first place, and providing multiple recom-
mendations may increase the cognitive load for customers, who may not
be willing to invest time and thought. As a result, offering one recom-
mendation is often how medical (and much legal) advice is presented.
Nevertheless, it seems necessary that customers invest a certain amount
of time and thought if they are to make empowered decisions. We could
imagine designing recommendations and their explanations in such a
way that the cognitive load for customers remains low, for example by
presenting a small set of relevant recommendations. For example, in
situations where there are too many options to consider meaningfully,
the evaluative AI framework suggests helping people narrow down the
options.
7.3.5 Fostering user engagement, curiosity and learning
Myintuitionaftertheresearchinthisthesisisthatcreatingtrulyuseful
explanations requires improving user engagement or curiosity. Work on
fostering motivation, curiosity, and learning in education, psychology,
or HCI provides a wealth of relevant knowledge for explanation design.
However, the explainability field has yet to fully tap into this research.
User engagement is related to users’ motivation and goals, and to
2008
other attributes [O’Brien and Toms, ] such as challenge, positive af-
fect, endurability, aesthetic and sensory appeal, attention, feedback, vari-
ety/novelty, interactivity, and perceived user control. O’Brien and Toms
2008
[ ] propose the following definition of user engagement:
Definition
User engagement. Engagement is a category of user experience charac-
terized by attributes of challenge, positive affect, endurability, aesthetic and
sensory appeal, attention, feedback, variety/novelty, interactivity, and per-
ceived user control.
5
The explanations we designed in Chapter did not improve user en-
gagement. Future work could try to improve explanation design in the
context of life-insurance in order to optimize for the above aspects. I am
not aware of work in explainability that has considered all these aspects

226 the explanation paradox and the human centric path
-
of user engagement for explanation design.
However,interestingworkhasstartedtoemergeonthetangentialcon-
2023 2021
cept of curiosity [Danry et al., , Melsión et al., ]. This work
is rooted in educational psychology. Unlike friction-based design, sup-
porting curiosity does not sacrifice users’ satisfaction, on the contrary.
2019
According to Shin and Kim [ ], curiosity leads to a search for infor-
mation which, when fulfilled, resolves the psychological discomfort of
23
uncertainty and leads to a sense of satisfaction. In Section . of Chapter
2
, we have seen that curiosity is one of the main reasons people ask for
explanations. It also helps them learn and memorize better [Shin and
2019
Kim, ]. In the field of education, several studies have demonstrated
that curiosity is a key factor in learning, creativity and well-being [von
2011
Stumm et al., ]. These provide promising avenues for research on
explainability to promote learning through curiosity.
Definition
Curiosity. "The desire for knowledge in the absence of extrinsic reward"
[Shin and Kim, 2019].
2019
AccordingtoShinandKim[ ],curiosityisgeneratedbytheaware-
ness of a gap in knowledge, generally aroused by stimuli [Kang et al.
2009 ; Markey et Loewenstein 2014 ]. The authors argue: "This lack of in-
formation creates a feeling of deprivation, which naturally leads to a desire to
learn." Moreover, Shin and Kim argue that there is an optimal level of
knowledge gap to arouse curiosity. Curiosity depends on how attainable
the information is for them, meaning that the knowledge gap should not
betoolarge. Thefeelingofhavingthebackgroundknowledgeandability
to find an answer intensifies curiosity.
"Thefirststeptoinstigatecuriosityiscreatinganoptimalknowledgegapandhelpingstudentstobe
awareofit. Asimplewaytoachievethisistointroducecognitiveincongruityimmediatelyafter
providingstudentswithbasicknowledgeinaparticularsubject."
[ShinandKim,2019]
Asking questions to users is one way to introduce this "cognitive in-
2023
congruity" and pique users’ curiosity. Danry et al. [ ]’s intuition in
their paper "Don’t Just Tell Me, Ask Me" is that framing explanations as
questions, rather than presenting them directly to the user, encourages
2
people to critically evaluate explanations . They find that AI explana- 2In [Danry et al., 2023],
tions framed as questions were able to significantly increase human dis- anexampleofcausalex-
2021 planation is: "If one per-
cernment of logically flawed statements. Similarly, Melsión et al. [ ]
son played violent video
designed "quiz" explanations by asking users—in this case children—
gamesandwasaggressive,
what they thought were the most important characteristics for an AI to it does not follow that
predict gender. The use of such gamified explanations was useful in everyonewhoplaysviolent
improving understanding and learning in the domain of gender bias. videogameswillbeaggres-
2023 2021 sive". Framedasaques-
The authors’ intentions in Danry et al. [ ] and Melsión et al. [ ]
tion, it becomes: "If one
wastoimproverespectivelyhumandiscernmentandlearning. Although
personplayedviolentvideo
the authors do not connect their research to the notion of curiosity, it gamesandwasaggressive,
doesitfollowthat...?"

discussion 227
seems like designing explanations as questions corresponds to the pro-
2019
cess of stimulating curiosity described by Shin and Kim [ ]. Asking
usersquestionsmakesthemawareoftheirknowledgegapsandservesas
a stimulus for curiosity. The notion of curiosity is interesting because it
extendsbeyondsimplyimprovingcriticalthinking. Curiositycanprompt
an active search for missing information, leading to enhanced user sat-
isfaction and learning upon resolution. This is particularly relevant in
domainswithhighinformationasymmetry,suchaslifeinsurance,where
effective explanation design could capitalise on significant opportunities
for learning. While fostering curiosity may seem like a worthwhile ob-
jective,itmaybeunattainableforsomeusersduetotimeconstraintsand
context specificities. Further research is needed to confirm or invalidate
this hypothesis.
2019
Based on Shin and Kim [ ]’s description of how to instigate cu-
riosity, we imagined explanations designed to support it in the context
2023
of Robex, similarly as in [Danry et al., ]. However, due to a lack of
time and resources, we did not test them. Below, we present the expla-
nations we developed, with the hope of inspiring future researchers to
empirically test similar designs.
71
Figure . shows the prototype interface we created. Users would first
71
read basic information about Robex, as shown in Figure . a), to intro-
duce basic knowledge of the Robex algorithm. Curiosity stimuli then
2023
taketheformofquestionsasin[Danryetal., ]. Userswouldhaveto
find the answer to two or three questions such as "In your opinion, what
featurehadthemostimpactontherecommendationmadetoyou?"(Singlechoice
question) or "In your opinion, which of the following characteristics led Robex
to make you a riskier offer?" (Multiple choice question) as shown in Figure
71
. b) and c). Users can click on feature cards, which turn green if it is
therightanswer andgreyotherwise. The questionsaredisplayedone by
2019
one to allow for progressive disclosure. [Springer and Whittaker, ,
2023
Panigutti et al., a]. After answering a few questions, users are able
to view the complete explanation, in a graphical format. The answers to
the questions are saved and displayed at the top of the interface.

228 the explanation paradox and the human centric path
-
Figure 7.1: Explanation
interfacetoengageusers
cognitively and stimu-
latetheircuriosity. First,
a brief explanation of
Robex is given: a); sec-
ond, the user answers
several multiple choice
questionsthatleadthem
to question the impact
ofsomefeatures: b)and
c);third,thefullgraphi-
calexplanationisgiven.

discussion 229
7.4 The human-centric way forward for explain-
ability in a highly regulated environment
In the EU, the forthcoming AI Act will require internal compliance
mechanisms and third party audits to ensure that high-risk AI systems
are trustworthy. In parallel, highly regulated sectors such as finance al-
readyhaveinplaceaccountabilityandoversightmechanismsthatrequire
all systems, including AI-based, to be trustworthy. In this context, expla-
nations of AI systems serve to control the algorithms’ outputs and verify
their compliant functioning. They are directed to auditors, regulators or
supervisors who are experts in the domain of application or/and ma-
chine learning. However, designing explanations for this user group also
presentsitsownchallenges,quitedifferentfromthechallengesofdesign-
ing explanations for lay users. On the one hand, explanations appear to
ease the tension created by the use of black-box systems in highly reg-
ulated contexts. On the other hand, the limitations of current XAI tech-
niques make them weak candidates for providing reliable and tangible
evidence about machine learning’s behaviour.
7.4.1 AML-CFTillustratesthetensionofusingAIinahighly
regulated environment
6
InChapter ,wedescribedthesupervisorycontextinanti-moneylaun-
dering and countering financing terrorism (AML-CFT), where the use of
AI is progressing. The industry is experiencing a paradigm shift in the
detection of financial crime from deterministic rule-based models, which
20
havedominated the marketfor over years, to probabilisticapproaches
using machine learning.
An increasing number of projects in banks have been utilizing AI in
AML-CFT systems in recent years. AI’s benefits to reduce compliance
2020
costs are beginning to materialize [Overrein, ], although scientific
evidence that it improves the detection of money laundering and terror-
ism financing is still lacking. So far, financial institutions and regulators
have seemed reluctant for machine learning to replace rules-based sce-
2022
narios that detect known patterns of criminal activity [Blakey, ]. For
compliance, it is important to be able to map identified AML-CFT risks
to specific scenarios created in the system. Machine learning may actu-
ally be better than rules-based systems at detecting new, sophisticated,
patterns of criminal activity, but the mapping exercise will be more chal-
lenging. Compliance may become less certain.
ThecontextofAML-CFThasgivenusanillustrationofthefundamen-
tal conflict that black box AI creates in highly regulated sectors between
6
compliance risks and efficiency. In Chapter , we delved into the heart
of this conflict by detailing the regulatory reasons that make AI opacity
and complexity problematic. We saw that AI opacity hinders supervi-
sors’ ability to verify several key requirements of AML-CFT systems, in
particular that:
1
. an AML-CFT system is adapted to the specific risks of the bank’s mar-

230 the explanation paradox and the human centric path
-
ket,
2
. an AML-CFT system "carefully examines" ongoing financial opera-
tions,
3
. bankinganalystscanjustifywhyanAIgeneratedalertshouldorshould
not be further examined,
4
. banking operators can detect and anticipate AI failures,
5
. the roles of human AML-CFT analysts and automated tools are com-
plementary.
Additionally, the strict compliance requirements in AML-CFT create
a conservative environment. To comply with AML-CFT regulation and
6 7
avoidfinesthatcansoarupto - %oftheirturnover,banksspenddozens
of billion of dollars in compliance every year and have developed costly
2017
and large-scale information systems [Farley, , Goranitis and Cailali,
2023
]. Updating these systems is costly and takes time [Singh et al.,
2018
]. Furthermore, regulators have been slow to produce guidelines
on AI, enhancing the regulatory uncertainty around the use of machine
2022
learning in AML [Blakey, ].
All these factors heighten the tension between using AI to improve
AML-CFT efficiency and compliance risks.
7.4.2 Explainability is incomplete and uncertain
3
The CJEU’s Ligue des Droits Humains case requires models used to 3CJUE, June 2021, 21,
detect terrorist threats to be based on "predetermined criteria", which Ligue des droits hu-
mains, Case law n° C-
raises the question of whether post-hoc explainability of black box mod-
817/19.
els will ever go far enough to permit the kind of verification required
for critical use cases such as AML-CFT. In this section, we discuss why
explainabilityisunlikelytofullyresolvethetensionbetweencompliance
and black box efficiency. In the next section, however, we argue that ex-
plainability does help to reduce this tension. We emphasize below that
explainability is just one technique in the auditor’s toolbox, that some
XAImethodshaveareliabilityproblem,andthatsomeexplanbilityneeds
still lack computational solutions to match specific regulator needs.
First, explainability only covers one aspect of the technological ap-
proaches necessary to demonstrate compliance. For example, in Chapter
6
, we revealed that supervisors needed enhanced model performance
metricstocomparemachinelearningbasedAML-CFTsystemswithpre-
machine learning ones.
For the verification of the "careful examination" of ongoing financial
2
operations by an AML-CFT system (point ), a sampling approach is
first needed to select some cases of interest with potential errors. Subse-
quently, explainability can be used to determine whether the algorithm’s
examination of specific cases indeed contains methodological shortcom-
ings. Challengermodels, suchasthoseusedby theACPRinFrance, also
2
seem particularly relevant and necessary to challenge point .
Similarly, explainability seems insufficient to fully demonstrate that
4
banking operators can detect and anticipate AI failures (point ). What

discussion 231
seems necessary in this case is a demonstration of a high-quality model
governance, which goes beyond the scope of explainability.
Second, current XAI techniques have a reliability problem. Currently,
there is a lack of assurance that the concept of explainability is one hun-
2023 2017
dred percent truthful [Bilodeau et al., , Kindermans et al., ]. As
652 6
presented in Section . . of Chapter , feature-based explanation tech-
niques are based on correlations between features, not on causation [Ha-
2022 2020 2013
mon et al., , , Rouvroy, ], making it hard for regulators to
rely on explanations as "faithful" and factual evidence for justifications.
Explanationscanalsobemanipulatedinblack-boxauditsettingssoasto
hide potential biases in a model, as demonstrated by Zhou and Joachims
2023
[ ]. Inresponse,JeannetteWingadvocatesfortheuseofformalmeth-
ods to address the probabilistic nature of machine learning and the role
2021
of data in training with a deterministic tool [Wing, ]. Formal verifi-
cations, she argues, are needed complements to fairness, robustness, ac-
countability,andexplainabilityinordertoachievetrustworthyAI.Addi-
tionally,someworkonthecausabilityofexplanationssuchas[Holzinger
2020
et al., ] are promising to address some of the inherent flaws of cur-
2021
rent explainability methods [Confalonieri et al., ].
6
Third, our findings in Chapter pointed to supervisors’ explainabil-
ity need to establish the level of reprehensibility of sampled failure cases
2
(point ): "Wasthefailureanisolatedincidentordoesitrevealamorese-
2023
rious systemic problem?" However, Zhou and Joachims [ ] argue that
current explanations do not provide answers to questions like: "what
factors caused the model to predict X instead of Y?", although this is
precisely what supervisors are looking for in AML-CFT: "what factors
caused the model not to produce an alert for this case (instead of flag-
ging the case)? Computational solutions to provide such explanations are
2021
indeed lacking in the explainability literature [Miller, ]. Future re-
search in explainability could investigate if contrastive explanation mod-
2021
els such as in [Miller, ] could provide solutions to this problem.
7.4.3 Human-centricexplainabilityalleviatessomeofthereg-
ulatory tension of black-box AI
Nevertheless, explainability can ease some of the tension for regula-
tory compliance caused by AI opacity. Explanations help to determine
whether a decision was made in accordance with procedural and sub-
stantive standards, which is the first aspect of accountability as defined
2017
in [Doshi-Velez and Kortz, ]. Explainability also contributes to ac-
countability by providing evidence to support the justifications made by
2013
the regulated entity [Felici et al., ]. The evidence may be imperfect
due to the reliability problem highlighted above, but at least some evi-
dence will be present.
4
The list below gives our assessment on the level of contribution of 4This argumentation
XAI to the five regulatory requirements listed above. The points 1 ’ and format is inspired from
[Miller,2023].

232 the explanation paradox and the human centric path
-
2
’ describe some of the technical functions that XAI methods can per-
form, contributing to demonstrate compliance respectively to the points
1 2
and in the list above. Furthermore, explainability may contribute to
3 4 5
answer the regulatory issues presented in points , , and . However,
the predominant human element in these contexts of XAI use makes the
adoption of a human-centric approach to explainability design particu-
larly critical.
1 ’. can reveal if certain characteristics of a bank’s clientele and risk pro-
files are duly taken into account, through global XAI,
2 ’. can reveal if the algorithm’s "examination" of operations contains
methodological errors, and how it adjusts to new information, using
local and global XAI methods,
3 ’. may enable an analyst to understand an alert and produce quality
reports using local XAI, provided that human cognitive biases and
human factors are carefully accounted for,
4 ’. mayhelpbankingoperatorstodemonstratecontrolovertheirAIsys-
tem,
5 ’. may allow better coordination between machine and human analysts
and more timely processing of alerts.
In a qualitative enquiry with similar AML-CFT scenarios as we used
6 2022
in , Gerlings and Constantiou [ ] found that contextual explanations
weremuchneededtoenablebankinginvestigatorstounderstandanalert
produced by machine learning in a timely manner. Explanations can
3 5
therefore contribute to points ’ and ’. However, they also noted the
5
risk of investigators being influenced by an alert’s risk score and losing 5"If the score is low,
time trying to understand it. The authors suggest removing such scores effort is low and vice
versa." [Gerlings and
altogether or providing more context-relatable explanations to point in-
Constantiou,2022]
vestigators to the issues with an alert.
6
In Chapter , we found that supervisors need explainability to verify
that the AI’s criteria for escalating or closing alerts are consistent with
human expertise. However, more research in HCI is needed to develop
useful explainability interfaces for supervisors to verify the bank’s con-
trol over its model and for banking practitioners to detect and anticipate
3 4
errors (points and ).
6
WealsodescribedinChapter thecomplexityofthesocio-techno-legal
contextofAML-CFTsupervision. Wefoundthatsupervisorsmainlyhad
legalbackgrounds,withfewinvestigatorshavingAIdevelopmentknowl-
edge. The holistic perspective provided by human-centric approaches
willbeparticularlyimportanttodesignexplanationsforsupervisorsthat
take into account these social factors.
Inthecomplexandhigh-dimensionalcontextofAML-CFT,thehuman-
centricapproachstrikesmeasparticularlynecessaryforeffectiveexplain-
ability implementation. It allowed us to uncover the need for contrastive
explanations among supervisors, which can pave the way for adapted
computational XAI solutions that respond to this need. The human-
centric approach will also be necessary to ensure that banking analysts
are not biased by explanations, that development teams feel accountable

discussion 233
for their models, that explanations improve human-machine collabora-
tion and that supervisors with high domain expertise but little computer
science skills have the means to challenge bank’s implementation of ex-
plainability. Explainabilityshouldnotbeseenasanoff-the-shelfsolution,
but as one tool among many in a complex socio-techno-legal context.
7.5 Peripheral observations
7.5.1 Why the financial sector is interesting for other highly-
regulated industries
AsourdiscussionisbasedonthefinancecasestudiespresentedinPart
II, we highlight below two reasons why the results we presented in the
financialsectorcanprovideinsightsforotherhighlyregulatedindustries.
First, the risk-based approach used in AML-CFT is a common regu-
latory approach, specifically in law pursuing "crime-fighting and pub-
2001
lic safety objectives" [Black, ] The lessons we learned in the area of
AML-CFT therefore resonate in these other risk-based fields. The ap-
proach is generally presented as virtuous because of its proportionality
2021
and cost-effectiveness [OECD, b]. It is adopted, for example, in the
recent Digital Services Act to prevent the systemic risks posed by AI-
2022
basedinformationplatforms[EuropeanParliamentandCouncil, ]or
in the Draft Regulation on the Dissemination of Terrorist Content Online
2021 2021
[European Parliament and Council, , Maxwell, ]. Maxwell also
notes some downsides to this approach. One of its peculiarities is that it
shiftstheburdenofattainingpublicinterestobjectivesthrough’appropri-
ate’ means to private actors, which are not as directly accountable as are
public authorities for respect of fundamental rights. Where regulatory
compliance is measured in part by the quantity of resources devoted to a
detection or enforcement task, this can incentivize companies "to do too
much, rather than too little, to satisfy the law’s crime-fighting objectives,
a phenomenon known as gold-plating." Gold plating can in turn create
risks for fundamental rights by going beyond what is strictly necessary
and proportionate.
Second, the digital developments we have seen in this thesis in the
financial sector with the emergence of online robo-advisors and super-
visory technology tools for AML-CFT, such as "LUCIA", are likely to be
adopted in other areas of the regulated digital economy.
Currentglobaleffortstoregulatetechnologyposeunprecedentedchal-
lengesforregulatorsandcreateademandfornewregulatorytechnology.
The financial sector has been at the forefront of the development of tools
to support compliance and reporting. The rapid development of FinTech
2008
intheaftermathofthe crisis,togetherwiththeburdensomecompli-
ance measures in the financial sector, have necessitated a corresponding
evolution of regulatory tools. RegTech addresses this demand by pro-
viding software tools that support regulatory compliance. It has been
instrumental in catalysing innovation and allowing digital companies to

234 the explanation paradox and the human centric path
-
navigate in the complex financial compliance landscape [Paul Fehlinger,
2023
].
Definition
RegTech. ”Any use of technology to match structured and unstructured
data to information taxonomies or decision rules that are meaningful to both
regulators and the firms they regulate, in order to automate compliance or
oversight processes.” [Emmanuel Schizas et al., 2019].
In summary, the risk-based approach to regulation and the pioneer-
ing regulatory developments in the financial sector suggest that lessons
learned in this area could be instructive for other highly regulated sec-
tors.
7.5.2 Principles for dealing with interdisciplinarity
This thesis has underlined the need for interdiscipliinarity in XAI re-
search. Interdisciplinary, however, is challenging. Acquiring adequate
proficiency in a single field demands extensive practice, making it par-
ticularly challenging to attain expertise in multiple areas. For a novice
researcher,notfullyestablishedinanyresearchdomain, interdisciplinar-
ity can therefore seem like an impossible endeavour, running the risk
of making no contribution anywhere and tackling subjects only superfi-
cially. I was confronted with this problem throughout my thesis. More-
over,buildingondifferentfieldscanmakeitparticularlydifficulttohave
relevant experts review the scientific value of interdisciplinary contribu-
tions, and ensure their quality. Below, I highlight three principles that I
believeareimportant,althoughverysimple,andnotspecificallyoriginal,
to address the challenges of interdisciplinarity.
1. Clarifyingone’sroots. First,interdisciplinaryauthorsshouldclarify
the disciplinary origin(s) of the methodologies used. Interdisciplinary
contributions sometimes lack a clear indication of the field or litera-
ture they draw upon. This can make it difficult to evaluate their sci-
entific value and can contribute to the undermining of interdisciplinary
research. However, if relationships to disciplines are clearly specified,
relevant reviewers can be called upon to verify research quality. Further-
more, I have realized in my research the importance of borrowing estab-
lishedmethodsfromacademicdisciplines(inmycasemainlyfromHCI).
Using established methods allows for capitalising on decades of evolu-
tion in a field towards scientific value, and provides the opportunity to
demonstrate rigour, transparency, and accuracy in their application. It
also allows peer reviewers to assess the quality of the implementation of
the methods.
2. Establishing a shared vocabulary and knowledge base. Second,
interdisciplinary fields have to establish a shared knowledge base and
vocabulary among researchers from diverse backgrounds. Dealing with
various terms, multiple definitions for the same concept, and diverse
backgrounds is a well-known challenge faced by interdisciplinary re-
search communities. In explainability, several researchers have called

discussion 235
for more unity and consensus in the vocabulary used [Doshi-Velez and
2017 2021
Kortz, , Markus et al., ]. However, the idea is difficult to put
2023
into practice, as in , divergences still exist on the definition of ex-
plainability. Notable efforts to map the landscape of interdisciplinary
research on AI ethics, transparency or fairness are presented in [Jobin
2019 2018
et al., , Abdul et al., ]. They provide useful insights on the com-
plex sub-communities that form the interdisciplinary research field on
AI. Other useful initiatives are workshops and courses provided in inter-
disciplinary conferences. They contribute to give all authors and review-
ers a minimum understanding of the different approaches and theories
relevant to the field.
3. Embracing historical research. Third, emerging interdisciplinary
movements and fields may sometimes lack sufficient connection to their
historical research roots. This is related to my first two points. It can be
hardtorealizethatsomeresearchhasalreadybeendoneonatopicifthe
terminology employed was not exactly the same. Specifically, human-
AI interaction research should better embrace past research in HCI and
psychology to build upon it. For instance, the field of psychology and
visualisation has generated a considerable amount of literature on how
to communicate information effectively to individuals, without neces-
sarily referring to the concept of explanation. Yet, explainability would
have much to gain from these findings. If explainability does not recog-
nise its links with these disciplines, it not only misses the opportunity
to capitalise on relevant knowledge but also runs the risk of replacing
such knowledge with more recent studies that may not be based on as
well-established methodologies.
7.5.3 On explainability for LLMs
Significantdevelopmentshaveoccurredinthefieldofexplainabilityin
2023
, driven by research on LLMs. The unprecedented size of large lan-
6
guage models (LLMs) , their dependence on context thanks to attention 6The phenomenon of
mechanisms [Vaswani et al., 2017 ], and their capture of the intricate nu- emergence in LLMs
refers to the abilities
ances of language have fascinated many researchers. LLMs also present
2021 that are not present
new risks [Gebru et al., ]. Specifically, they suffer from "hallucina-
in smaller language
tion", i.e. generating inaccurate, non-factual content [Yao et al., 2023 a]
models but appear
and their mode of interaction with people through dialogue, as we have whenscalingupmodels
seeninChapter
5
, makesthemparticularlypronetocheatusersandper-
[Weietal.,2023].
2023 2023
suade them of false claims [Rozen et al., ]. As Bubeck et al. [ ]
puts it: "[GPT4] is remarkably good at generating reasonable and coherent ex-
planations, even when the output is nonsensical or wrong". This has driven
many scholars to attempt to better understand the underlying mecha-
nisms of LLMs. The last couple of years have therefore seen interesting
developments in the field of explainability, from an observation-based,
"natural science" approach to a more promising, mechanistic and engi-
neering approach.
4
One of the specificities of LLMs like GPT- is that it can give you an
explanation of its answers if you ask it to. A lot of the efforts to bet-
ter understand large language models have therefore focused on design-

236 the explanation paradox and the human centric path
-
ing inputs or "prompts" that elicit explanations. For example, Chain-
of-Thought prompting (CoT) consists in eliciting intermediate reasoning
2023
stepsintheLLM’soutput[Weietal., ]. Manymorestrategiesinthat
vein have been developed to improve end task performance, for example
few-shot prompting which consists in giving an example of the expected
2020 2023
result in the prompt [Brown et al., ] or ReAct [Yao et al., b]
which instructs the model to perform specific actions such as searching
2023 4
an external information source. Bubeck et al. [ ] also tested GPT- ’s
explainability abilities by asking it to provide explanations for its an-
swers. They examined its output consistency, i.e. whether the explanation
4
given by GPT- is consistent with its output, and its process consistency,
i.e. whether the explanation gives us the ability to simulate GPT- 4 ’s pre-
4
dictionsindifferentsimilarcontexts. TheyfoundthatGPT- wasparticu-
larlyoutput-consistent,evenwhenprovidinganexplanationforawrong
answer, but not reliably process-consistent, especially for tasks that are
not inherently explainable, such as arbitrary ones.
Although these strategies are called "prompt engineering", they devi-
ate from the idea of understanding the algorithms’ internal components
through formal engineering and mathematical methods. In this sense,
they are more closely aligned with natural science approaches.
Most of the above-mentioned approaches rely on inference, observa-
tions, and more specifically on the language models’ outputs. However,
2023
since LLMs’ outputs are unreliable [Yao et al., a] there is no guaran-
tee that prompting strategies will make their answers and explanations
2023
more accurate. Turpin et al. [ ] recently demonstrated that Chain-of-
Thoughts prompting can fail and generate false reasons for the chatbots’
answersinthestep-bystepreasoning. Moreover,theconsistencyofGPT-
4
’soutputpresentsasignificantissue. Iftheresponsesareinaccurate,the
corresponding explanations will align with them and convince users of
2023
erroneous assertions [Bubeck et al., ].
Theclassicalblack-boxapproachestoexplainabilityprovidedbymeth-
ods like SHAP, counterfactual and other model-agnostic techniques have
2023
also been tested on LLMs. Martens et al. [ ] have even taken advan-
tage of the LLMs to provide "SHAPstories" and "CFstories", narratives
generated from the results provided by these techniques. They show
that these narratives are more convincing for human users, providing
useful tools to generate explanations to a general audience and nonspe-
cialists, they argue. Yet, these approaches have the limitations we know
of classical explainability methods, specifically lack of causability, in ad-
dition to the limitations of prompt-based explanation methods such as
non-robustness due to high sensitivity to prompt details combined with
output consistency problems and persuasiveness.
Some recent research has introduced promising results to "mechanis-
tic" explainability, i.e. explain models’ internal mechanisms and compo-
nents. Such advances have been made possible by experimenting with
small models. Early attempts at understanding LLMs and deep learn-
ing models have focused on trying to find what best activates individual
2016 2019
neurons [Nguyen et al., , Carter et al., ]. However, the activa-
tion of a single neuron can take many different meanings in different

discussion 237
contexts, which makes it impossible to interpret neural networks on this
basis. This is what Anthropic [ 2023 ] call the polysemanticity of individual
neurons. This can be due to the superposition phenomenon by which "a
neural network represents more independent "features" of the data than
it has neurons by assigning each feature its own linear combination of
2023
neurons." [Anthropic, ]. However, recent research by Anthropic has
shown that mechanistic explanations are possible on small models at the
feature scale, which is much more appropriate than the scale of a single
neuron. By analyzing patterns (linear combinations) of neuron activa-
tions, they provide a promising path to breaking down the complexities
of neural networks into parts we can understand. For the first time, it
feels like the mechanistic approach could be surmountable, and explain-
ability could be achieved through a formal rather than purely inference-
based methods. These findings have yet to be replicated on larger, "fron-
tier" models, however.

238 the explanation paradox and the human centric path
-
7.6 General conclusion
The first part of this thesis examined the impact of explainability on
appropriate trust through two detailed scoping reviews focusing respec-
tively on cognitive biases and interactive explainability. We established
that explanations have the potential to manipulate trust, by triggering
cognitive mechanisms that lead to overtrust, distrust or misusing al-
gorithmic explanations and predictions. We documented some factors
that play an important role in the trust calibration process with AI sys-
tems, namely users’ prior beliefs and knowledge, and the completeness,
framing and the timing of the explanation. Interactivity has recently
been advocated by some scholars as a possible way of better aligning
explainability interfaces with the human cognitive processes of explana-
tion. Therefore analysed the different types of interaction found in the
literature on explainability and summarised the effects of interactivity
on explainability. Currently, interactive explanations do not appear to
increase misplaced trust in AI systems. However, there is a scarcity of
relevant controlled experiments to confidently confirm or refute this.
In the second part of the dissertation, we explored the role of expla-
nations for appropriate trust, which is critical for AI compliance in two
case studies in finance.
In the domain of life-insurance distribution, we came across an "ex-
planation paradox". Explanations are intended to empower users by pro-
viding them with important domain knowledge to enable them to make
free, informed choices. However, explanations also have the potential to
increase unwarranted trust and make users more vulnerable to untrust-
worthyrecommendations. Inthesecircumstances,itappearschallenging,
if not unattainable, for explanations to meet regulatory expectations of
ensuring meaningful consent from each and every individual. As high-
73
lighted in Section . , explanations should not be seen as a silver bullet
for empowering customers. However, future work could explore how to
develop"betterthannothing"explanationsthatworkfairlywellformost
people. Promisingworkinexplanationdesignismovinginthisdirection
by studying how explanations can be tailored to relevant client groups,
howfriction-basedinterfacedesigncanbeused,anddesignsthatsupport
curiosity and learning.
In the domain of anti-money laundering and countering terrorism
financing, we have discovered that explanations are necessary to en-
able regulatory supervisors to trust (or not) AML-CFT systems oper-
ated by financial institutions. Explanations can provide evidence on AI
systems’ behaviour. Such factual information supports the provision of
justifications—i.e. demonstrations of compliance—by regulated entities.
For example, explainability will be necessary to verify the alignment of
machine and human criteria for flagging money laundering cases, and
less clearly to verify the appropriate prevention of potential AI failures.
We also established the need of supervisors for contrastive explanations
that help to determine the level of reprehensibility of sampled failure
cases: "Was the failure an isolated incident or does it reveal a more se-
rious systemic problem?". However, computational solutions remain to

discussion 239
be developed to address this need. Additionally, we noted that current
explainability methods have reliability issues that need to be resolved.
We argued that taking a human-centric approach is crucial in mitigating
the regulatory tensions caused by the use of opaque machine learning in
the complex socio-techno-legal environment of highly regulated sectors
such as AML-CFT.
Belowaresomeshortrecommendationsforfutureresearchandpolicy.
Theserecommendationsreflectmysubjectiveinterpretationoftheresults
of my thesis.
Recommendation 1. Examine the needs of online robo-advisor clients
inmoredetail. Thiswillhelptobetteralignthemwithregulatoryobjec-
tives. Furtherqualitativeresearchshoulddelveintotheneedsofdifferent
types of robo-advisor clients in light of the regulatory objectives they are
intended to fulfill.
Recommendation 2. Determine whether friction-based explainabil-
ity design can improve user understanding and critical thinking, even
marginally. Some work has started to investigate how to force users
2021
to pay attention to explanations through "friction" [Buçinca et al., ,
2021
Naiseh et al., a]. Further work could explore the effect of explana-
tions that use prominent risk warnings or that only appear if requested,
on user understanding of an AI recommendation
Recommendation 3. Examine the impact of question-driven explain-
ability design to optimize curiosity and learning. Absence of domain
knowledge can create obstacles to users’ effective understanding of AI
recommendations. Explainability should be viewed as an opportunity to
educate consumers on basic domain knowledge. Formulating explana-
2023 2021
tions as questions [Danry et al., , Melsión et al., ] can be useful
in sparking consumer curiosity and learning. Research in educational
psychology should be leveraged to make sure explanations can foster
curiosity.
Recommendation 4. Take a human-centric approach for explainabil-
ityuseinAML-CFTandothercomplexsocio-techno-legalenvironments.
Explainabilityshouldnotbeviewedasaready-madesolution,butrather
as one tool among many in a complex socio-techno-legal context. There-
fore, we emphasise the importance of designing explainability with a
human-centric approach, taking into account the diverse backgrounds,
needs, feelings of accountability, and cognitive biases of different stake-
holders. This approach can be complemented by legal analyses to better
understand regulatory requirements, which go hand in hand with the
needs of supervisors.
Recommendation 5. Develop and design contrastive explanations to
help supervisors gauge the level of reprehensibility of failure cases. The
aim of this exploration would be to answer the supervisor’s question:
’Was the failure an isolated incident or does it reveal a more serious
systemic problem?’ At present, XAI techniques provide inadequate solu-
tions to this issue.

| 240 the | explanation | paradox | and the human | centric path |
| ------- | ----------- | ------- | ------------- | ------------ |
-
Recommendation 6. Elaborate tests to verify the correct human and
AI alignment of decision criteria and prevention of failures. As we have
seen,machinelearninginhighly-regulatedtaskssuchasAML-CFTmust
permit regulated entities and supervisors to verify alignment of the sys-
tem with human-defined decision criteria. Current ex-post XAI tech-
niquesdonotpermitthisyet,butXAIdevelopmentsarequicklyadvanc-
| ing so | that this alignment | can be | verified in the near | future. |
| ------ | ------------------- | ------ | -------------------- | ------- |

Appendix
A1. List of cognitive patterns when interpreting
explainable AI
TableA.1: Listofcognitivepatternsidentifiedinthecorpuscreatedin
3
Chapter that may lead to reasoning errors when using explainable AI
systems.
Cognitivepattern Definition Ref.inthecorpus
Ambiguityaversion "Thetendencytopreferknownrisksoverunknownrisks"[Kliegretal.,2021] [Kliegretal.,2021]
Anthropomorphism PeopletendtoattributehumantraitstomachinesandthereforeexpectAIexplanationstousethesamecon- [Miller,2019,WeldandBansal,2018]
ceptualframeworkusedtoexplainhumanbehaviors.
Attentiontoaesthetics Humanjudgmentratingsofexplanationsarebiasedtowardvisualappearance. [Mohsenietal.,2021a]
Attentiontoabnormality "Peoplemostlyaskforexplanationsofeventsthattheyfindunusualorabnormal"[Miller,2019] [Miller,2019,WeldandBansal,2018]
Attention to confidence PeopleneedconfidencelevelstomakebetteruseofML-assisteddecision-makingsystems."ProspectTheory [Bhattetal.,2021,Miller,2019]
levels suggeststhatuncertainty(orrisk)isnotconsideredindependentlybuttogetherwiththeexpectedoutcome"
[Bhattetal.,2020]
Attentiontodemographic Tendencytofixateondemographicfeaturesinexplanationssuchasageandrace [Liuetal.,2021]
features
AttentiontoFalseNega- "UserspaylessattentiontoFPexplanationerrorsandinturn,aremorecriticalforFNexplanationerrors". [Mohsenietal.,2021a]
tivesratherthantoFalse [Mohsenietal.,2021a]
Positives
Attentiontofoil "Explanationsaresoughtinresponsetoparticularcounterfactualcases,whicharetermedfoils.Thatis,peopledonotask [Miller, 2019, Weld and Bansal, 2018,
whyeventPhappened,butratherwhyeventPhappenedinsteadofsomeeventQ."[Miller,2019] Woodcocketal.,2021]
Attentiontointentional- Peopletendtofocusonintentionalactionsratherthannon-intentionalonestoselectaneventasacausein [Miller,2019,WeldandBansal,2018]
ityandresponsibility acausalchain. Similarly,"aneventconsideredmoreresponsibleforanoutcomeislikelytobejudgedasabetter
explanationthanothercauses."
Attention to necessity, Eventsthatarenecessary,sufficientandrobusttosomechangesaremorelikelytobeselectedasacause. [Miller,2019]
sufficiency and robust-
ness
Automation bias / au- Thetendencytooverrelyonmachine’spredictions. [Bansaletal.,2021,Bussoneetal.,2015,
tomationoverreliance Danryetal.,2020,Liuetal.,2021,Naiseh
etal.,2021b]
Availabilitybias Thetendencytobelievethatexamplesandeventsthateasilycometomindaremorerepresentativethanis [Kliegretal.,2021,Wangetal.,2019a,
actuallythecase. Zyteketal.,2021]
Averagingbias "Usingtheaverageofprobabilitiesoftwoeventsfortheestimationoftheprobabilityofaconjunctionofthe [Kliegretal.,2021]
twoevents".[Kliegretal.,2021]
Backfireeffect "Correctionsofmisperceptionsmayenhancepeople’sfalsebeliefs".[NyhanandReifler,2010] [LaiandTan,2019]
Base-rateneglect "Thetendencytounderweightevidenceprovidedbybaserates".[Kliegretal.,2021] [Kliegretal.,2021]
Changeblindness "Humansinabilitytonoticeallofthechangesinapresentedmedium".[Simons,2000] [SokolandFlach,2020]
Choiceoverload Thedifficultytomakeachoicewhenfacingmanychoicesforpeopleofthetype"mazimizer".Asaconsequence, [Cobaetal.,2019]
theyarelesscommittedtotheirchoices,displaylowersatisfactionwiththeirchoices.
Cognitivedissonance ThetendencytoagreewiththeAI’ssuggestions,whilebeingawaretohaveadifferentopinion. [Danryetal.,2020]
Completenessbias Longerexplanationstendtoleadmoretooverreliancethanshorterones. [Bussoneetal.,2015,Fürnkranzetal.,
2020,Kuleszaetal.,2015,LaiandTan,
2019,Szymanskietal.,2021]

242 the explanation paradox and the human centric path
-
Cognitivepattern Definition Ref.inthecorpus
Confirmation bias and "Thetendencytoseeksupportingevidenceforone’scurrenthypothesis".[Kliegretal.,2021] [Bayeretal.,2021,Kliegretal.,2021,Bus-
hindsightbias soneetal.,2015,Naisehetal.,2021b,Szy-
manskietal.,2021,Wangetal.,2019a]
Confusionoftheinverse "ThemistakeofconfusingtheconfidenceofanimplicationA(cid:25)BwithitsinverseB(cid:25)A."[Kliegretal.,2021] [Kliegretal.,2021]
Conjunctionfallacy Estimatingtheconjunctionoftwostatementstobemoreprobablethanoneofthetwostatements. [Fürnkranzetal.,2020,Kliegretal.,2021,
WeldandBansal,2018]
Default or Status quo "Thetendencytofavorthedefaultoptionandthustheproposedsuggestion".[Bayeretal.,2021] [Bayeretal.,2021]
bias
Disjunctionfallacy "Judgingtheprobabilityofaneventashigherthantheprobabilityofaunionoftheeventwithanotherevent". [Kliegretal.,2021]
[Kliegretal.,2021]
Disregardofevidence Tendencytobelievepersuasiveclaimsunsupportedbyevidence. [Danryetal.,2020]
Escalation of commit- "Peoplesticktoachoicetheymadedespiteunderstandingthelogicalimplicationthatdoingsomightleadto [Bayeretal.,2021]
ment undesirableconsequences"[Bayeretal.,2021]
Familiaritybias “Unfamiliarinformationmightinduceareinforcementeffectthatcausesuserstoavoidinteractingwithvarious [Szymanskietal.,2021]
content”.[Szymanskietal.,2021]
Framingbias Peopledecideonoptionsbasedonwhethertheyarepresentedwithpositiveornegativeconnotationsor [Bansaletal.,2021,Bhattetal.,2021,Kim
whethertheyarepresentedafterorbeforetheAIrecommendation. andSong,2020,Kliegretal.,2021]
Illusion of Explanatory Peoplethinktheyhaveamuchdeeperunderstandingofhowcomplexconceptsworkthantheyactuallydo. [Chromiketal.,2021,Kauretal.,2020,
Depth Naisehetal.,2021b]
Illusionofvalidity "Unjustifiedsenseofconfidenceandhencefailurewhenevaluatingdifferentpossibilities"[Simkuteetal.,2020] [Simkuteetal.,2020]
Illusorysuperiority "Userswiththehighestneedforadvicemaybetheleastlikelytodeferjudgment."AlsoknownastheDunning-
Krugereffect[Schafferetal.,2019].
Inherencebias "Humanstendtoconstructexplanationsbasedonaccessibleinformationabouttheinherentpropertiesofa [Bekeleetal.,2018,Miller,2019]
particularphenomenoninsteadofinaccessibleinformationaboutextrinsicfactors".[Bekeleetal.,2018]
Informationoverload "Providingtoomuchinformationatoncecanresultinreducedaccuracy"[Simkuteetal.,2020] [Abduletal.,2020,Naisehetal.,2021b,
Simkuteetal.,2020,Zyteketal.,2021]
Insensitivity to sample Whenbothconfidenceandsupportarestated,confidencescorespositivelyaffectsplausibilityandsupportis [Fürnkranzetal.,2020,Kliegretal.,2021]
size largelyignored.
Insensitivity to sample "Usersareprimarilyguidedbythemeanandthenumberofratings,andtolesserdegreebythevarianceand [Cobaetal.,2019]
variance originofarating"[Cobaetal.,2019]
Mereexposureeffect TheincreaseoftrustinanAIsuggestionfollowingthemereexposureofanexplanation. [Eibandetal.,2019,Kliegretal.,2021,
LaiandTan,2019]
Misunderstanding of "Peopleinterpret"AND"differentlythanlogicalconjunction",theTRUEandFALSEconditionsareperceived [Kliegretal.,2021,Fürnkranzetal.,2020]
Booleanlogic asnon-intuitive.[Kliegretal.,2021]
Misunderstanding of Notunderstandingwhattheconfidencescoresreferto. [Bussoneetal.,2015]
confidencescores
Narrationbias(linkedto Tendencytointerpretinformationasbeingpartofalargerstoryandtoassumecausalrelationsintheevents [Andrienkoetal.,2022,Atreyetal.,2020,
over-generalization) ofthatstory. Kauretal.,2020,Zyteketal.,2021]
Negativitybias UserspaymoreattentiontonegativefeaturesintheAIortheAIexplanationswhichmayleadtoerodingtrust [Branley-Belletal.,2020,Kliegretal.,
andpaymoreattentiontonegativeoutcomes. 2021,Nouranietal.,2021,Shimojoetal.,
2020,Zyteketal.,2021]
Perceived goal impedi- "Peopleinhighlycriticaldecision-makingenvironmentsarelikelytobeinaserious-mindedstate,where [Naisehetal.,2021b]
ment additionalinformationmightbepronetobeingperceivedasagoalimpediment".
Pre-usealgorithmicopti- BeforeusingtheXAIsystem,usershadpositiveinferencesaboutalgorithmiccapability,whichdisappeared [SpringerandWhittaker,2019]
mism afterusingit.
Preferenceforbroadex- Peoplepreferbroadexplanations,thatexplainmoreobservations. [Miller,2019]
planations
Preferenceformorecom- Peopletendtoprefercompleteexplanationsoversoundones.Completeexplanationshelpthemformbetter [Kuleszaetal.,2013]
pleteexplanations mentalmodels.
Preferenceforsimpleex- Peopleprefersimpleexplanationstocomplexones. [Abduletal.,2020,Miller,2019,Shimojo
planations etal.,2020,Zyteketal.,2021]
Preference for usability Userperformanceandpreferenceonproxytasksmaynotaccuratelypredicttheirperformanceandpreference [Buçincaetal.,2020,Liuetal.,2021,Szy-
vs.performance ontheactualdecision-makingtaskswheretheircognitivefocusiselsewhere,andtheycanchoosewhetherand manskietal.,2021]
howmuchtoattendtotheAI.
PrimacyeffectorAnchor- Peoplequicklyformopinionsaboutsomethingbasedonthefirstinformationwereceiveaboutit. [Kliegretal.,2021,Naisehetal.,2021b,
ingbias Nouranietal.,2021,Wangetal.,2019a]
Recognitionbias Recognizinginformationmakestheusermorelikelytotrusttheexplanation. [Fürnkranzetal.,2020,Kliegretal.,2021,
Szymanskietal.,2021,Woodcocketal.,
2021]
Redundancyaversion Redundantinformationisanothercauseofskippingexplanations,makinguserslosetrustintheexplanations. [Naisehetal.,2021b]
Reinforcement effect or Theincreaseoftrustfollowingrepetition. [Kliegretal.,2021]
Reiterationeffect
Representativenessbias Thesimilarityofobjectsoreventsmakespeopledisregardtheprobabilityofanoutcome. [Fürnkranzetal.,2020,Kauretal.,2020,
Kliegretal.,2021,Wangetal.,2019a,
Zyteketal.,2021]
Unitbias "Thetendencytogiveasimilarweighttoeachunitratherthanweighitaccordingtoitssize". [Kliegretal., [Kliegretal.,2021]
2021]
Weakevidenceeffect "Weakargumentinfavorofastatementcanleadtodecreasedbelievabilityofthestatement". ([Kliegretal., [Kliegretal.,2021,Fürnkranzetal.,2020]
2021]

appendix 243
B1. Co-design Study Questionnaire
Figure B.1: The following figure presents the questions used in the
5
co-designWinoterrvkieswhsocpon Gduuctieddein Chapter .
Each interview included the following steps:
1. Preliminary questions: End-user participants are asked questions on their experience with life-
insurance and robo-advisors, and on their explanations needs.
1'. Preliminary questions: Regulator participants are asked questions about explanations’ role for
customers and customer protection in life-insurance
2. Testing the interface: Participants are asked to use Robex from the profiling questionnaire up to
the recommendation and explanation. They are also asked to think aloud. Regulators are
prompted to use Robex with several different imaginary user profiles.
3. Feedback: Participants are asked for feedback about their overall experience using Robex.
Below are the questions asked to participants. The questions have been adapted slightly depending
on whether they were asked to regulators or end-users. Questions for regulators are shown in the
blue boxes, those for non-expert participants in the red boxes. The purple boxes indicate that there
was no difference between the questions asked to regulators and end-users for the phase in question.
Phase 1: Preliminary questions (Regulators)
1. How important are explanations for users in life insurance? What type of explanations
should be provided?
2. How good are the explanations offered by robo-advisors?
3. How can we reach people with no financial knowledge?
4. What do you think potential subscribers need to make an informed decision?
Phase 1: Preliminary questions (End-users)
1. Do you have any experience of using a robo-advisor or life insurance?
2. What is your level of familiarity with financial investment?
3. What kind of explanations would you like to receive about an online financial
recommendation?
Phase 2: Testing the interface
1. Do you agree with the proposal?
2. What would you have suggested?
3. Do you agree with the explanations?
4. Test another profile
Phase 3: Feedback
1. What is your experience / opinion of the system? Do you think these explanations could
help users?
2. What do you think of the proposed explanations? Are there any limitations, other needs?
3. What user characteristic would it be interesting to change in the explanations?

| 244 | the | explanation | paradox |     | and | the human | centric | path |     |
| --- | --- | ----------- | ------- | --- | --- | --------- | ------- | ---- | --- |
-
| B2. | The | Robex | recommendation |     |     | system |     |     |     |
| --- | --- | ----- | -------------- | --- | --- | ------ | --- | --- | --- |
We descibe below the simple, rule-based scoring algorithm for Robex.
o,a ,c,a ,k represent the dimensional risk scores obtained by a user
|     | s   | p   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
after responding to a profiling questionnaire. o represents the user’s
financial objective, a her assets, c her asset composition, a her risk ap-
|     |     |     | s   |     |     |     | p   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
petite and k her knowledge in finance. Dimensional risk score values
were calibrated through multiple discussions and tests with regulators.
| rs is | the | total risk score, | the | sum | of the | dimensional | risk scores. |     |     |
| ----- | --- | ----------------- | --- | --- | ------ | ----------- | ------------ | --- | --- |
|       |     |                   |     |     | 1      |             | 5            |     |     |
reco is Robex’s recommendation. is the least risky and is the most
risky.
| Ensure: |     |     |     |     |     |     |     |     | Algorithm1: |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- |
TheRobex
| IR  | ← o,a  | ,c,a ,a ,rs  |        |     |     |     |     |     | rule-basedalgorithm |
| --- | ------ | ------------ | ------ | --- | --- | --- | --- | --- | ------------------- |
|     |        | s p k        |        |     |     |     |     |     |                     |
| Z   | ← reco | ≤            | reco ≤ |     |     |     |     |     |                     |
|     |        | with 1       |        | 5   |     |     |     |     |                     |
| 0   | ≤ o    | ≤ 3          |        |     |     |     |     |     |                     |
| −2  | ≤      | a s ≤ 4      |        |     |     |     |     |     |                     |
| −9  | ≤      | c ≤ 1 with c | = f(a  | )   |     |     |     |     |                     |
s
| 0   | ≤ a | ≤ 7 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p
|     | ≤    | ≤ = o+a | +c+a |     | +k  |     |     |     |     |
| --- | ---- | ------- | ---- | --- | --- | --- | --- | --- | --- |
| 0   | k    | 5 r s   | s    | p   |     |     |     |     |     |
| if  | rs < | 6 then  |      |     |     |     |     |     |     |
|     | reco | ← 1     |      |     |     |     |     |     |     |
<
| else | if   | rs 10 then   |     |     |     |     |     |     |     |
| ---- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|      | reco | ← 2          |     |     |     |     |     |     |     |
| else | if   | rs < 15 then |     |     |     |     |     |     |     |
|      | reco | ← 3          |     |     |     |     |     |     |     |
| else | if   | rs < 19 then |     |     |     |     |     |     |     |
←
|     | reco | 4   |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
else
|     | reco | ← 5 |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
end if
|     | Additionally, |     | ▷ Safety |     | measures | where | added for specific | user |     |
| --- | ------------- | --- | -------- | --- | -------- | ----- | ------------------ | ---- | --- |
answers.
| if  | o = | then |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
0
|     | reco | ← min(reco,2) |     |     |     |     |     |     |     |
| --- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
end if
and
| if  | a 1 | = 0 then |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
s
←
|     | reco | 1   |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
end if
The biased Robex algorithm works like this: the total risk score rs
that is obtained by a user is artificially reduced or increased by about 10
points, which amounts to the total false risk score frs. The following al-
gorithm calculates false dimensional risk scores o,a s ,c,a p ,k that together
| sum | up  | to the total false | risk | score | frs. |     |     |     |     |
| --- | --- | ------------------ | ---- | ----- | ---- | --- | --- | --- | --- |

appendix 245
Ensure: Algorithm2:
Thebiased
←
IR frs Robexalgorithmusedto
| frs ← | rs                |             |               |               | make inappropriate | rec-    |
| ----- | ----------------- | ----------- | ------------- | ------------- | ------------------ | ------- |
| R5    |                   |             |               |               | ommendations       | and ex- |
| ←     | w is the array of | o,a ,c,a ,k | values sorted | in descending | order              |         |
s p planations.
R5
| ←   | MAX is the array | of maximum | values | for o,a ,c,a ,k |     |     |
| --- | ---------------- | ---------- | ------ | --------------- | --- | --- |
|     |                  |            |        | s p             |     |     |
R5
| ←   | MIN is the array | of minimum | values | for o,a s ,c,a p ,k |     |     |
| --- | ---------------- | ---------- | ------ | ------------------- | --- | --- |
R5 ←
|         | INC is the array | of increments | for o,a | s ,c,a p ,k |     |     |
| ------- | ---------------- | ------------- | ------- | ----------- | --- | --- |
| if rs < | 6 then           |               |         |             |     |     |
| for     | each i in W do   |               |         |             |     |     |
<
|     | while frs 15 do |          |      |     |     |     |
| --- | --------------- | -------- | ---- | --- | --- | --- |
|     | if W(i)+INC(i)  | > MAX(i) | then |     |     |     |
|     | W(i) = MAX(i)   |          |      |     |     |     |
else
|     | W(i) ← W(i)+INC(i) |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- |
end if
frs ← Sum(W.values)
|     | end while |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
end for
| else if | rs < 12 then   |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- |
| for     | each i in W do |     |     |     |     |     |
<
|     | while frs 20 do |          |      |     |     |     |
| --- | --------------- | -------- | ---- | --- | --- | --- |
|     | if W(i)+INC(i)  | > MAX(i) | then |     |     |     |
|     | W(i) = MAX(i)   |          |      |     |     |     |
else
|     | W(i) ← W(i)+INC(i) |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- |
end if
frs ← Sum(W.values)
|     | end while |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
end for
| else if | rs < 19 then     |          |      |     |     |     |
| ------- | ---------------- | -------- | ---- | --- | --- | --- |
| for     | each i in W do   |          |      |     |     |     |
|         | while frs > 2 do |          |      |     |     |     |
|         | if W(i)+INC(i)   | < MIN(i) | then |     |     |     |
|         | W(i) = MIN(i)    |          |      |     |     |     |
else
|     | W(i) ← W(i)−INC(i) |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- |
end if
frs ← Sum(W.values)
|     | end while |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
end for
| else if | rs ≥ 19 then     |          |      |     |     |     |
| ------- | ---------------- | -------- | ---- | --- | --- | --- |
| for     | each i in W do   |          |      |     |     |     |
|         | while frs > 9 do |          |      |     |     |     |
|         | if W(i)+INC(i)   | < MIN(i) | then |     |     |     |
|         | W(i) = MIN(i)    |          |      |     |     |     |
else
|     | W(i) ← W(i)−INC(i) |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- |
end if
frs ← Sum(W.values)
|     | end while |     |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
end for
end if

246 the explanation paradox and the human centric path
-
C1. Workshop guide
Figure C.1: The following figures present the questions used in the
6
workshops conducted in Chapter .
Workshop Guide
Each workshop included the following steps:
0. Participants read and fill in the consent form, and then the pre-questionnaire (paper format)
1. Participants are asked questions on the normal procedure in their AML-CFT profession (either the
control procedures for regulators or conception procedure for model designers in banks)
2. Participants questions are asked questions about the use of AI in AML-CFT to understand their
impressions on AI.
3. A scenario where AI is used in AML-CFT transaction monitoring systems is then introduced and
participants are asked questions about this scenario.
4. Finally, conceptual design artifacts of different explanations and justifications are shown to
participants. Participants are asked to discuss them.
Below are the questions asked to participants. The questions have been adapted slightly depending
on whether they were asked to regulators or bank practitioners. Questions for regulators are shown
in the blue boxes, those for participants from banks in the red boxes. The purple boxes indicate that
there was no difference between the questions asked to regulators and bank practitioners for the
phase in question.
Phase 0: Pre-Questionnaire (Regulators)
1. How many years of experience do you have in controlling AML/CFT systems? (Between 1
and 3, Between 4 and 10, More than 10 years)
2. Do you have any specific expertise in LCB-FT?
3. What is your level of familiarity with: artificial intelligence? The cloud? Big data? (Likert-
type responses on a scale of 1 to 7)
Phase 0: Pre-Questionnaire (Banks)
1. How many years of experience do you have in AML/CFT systems in financial institutions?
(Between 1 and 3, Between 4 and 10, More than 10 years)
2. Do you have any specific expertise in LCB-FT?
3. What is your level of familiarity with: artificial intelligence? The cloud? Big data? (Likert-
type responses on a scale of 1 to 7)
Phase 1: Understanding the control processes (Regulators)
4. What are the different steps of a control? What are the criteria to evaluate AML/CFT
processes?
5. What should banks justify/explain regarding the tools used in AML/CFT (the example of
transaction monitoring could be used)?
6. What form do these justifications take?
Phase 1: Understanding the implementation of models in AML-CFT in banks
4. What are the different steps in implementing a financial security project?
5. What should banks justify/explain regarding the tools used in AML/CFT (the example of
transaction monitoring could be used)?
6. What form do these justifications take?

appendix 247
Phase 2: Impressions on AI
1. What new technologies are emerging in banks' AML/CFT systems?
2. Can these situations be linked to artificial intelligence in your opinion: data collection,
customer risk characterization, transaction monitoring system, alert review, monitoring
tools. If so, what is the role of AI in these systems?
3. How promising do you think this technology is?
4. Do you think (and why) that using AI could be more or less risky for financial security
than current systems (without AI)?
5. Do you think these systems could be more or less difficult to control/monitor?
AI debrief: at the end of this phase, if the participants are not very familiar with AI, the
moderator will define AI (OECD and Wikipedia definitions of AI and Machine learning) and
give a short presentation on different types of machine learning.
For phase 3, a "scenario" will be introduced. It describes a hypothetical situation involving an AI
system in a bank. Its purpose is to provoke questions from the controllers and to bring out ideas. It
also features a fictional character. The purpose of this character is to encourage the participants to
immerse themselves in a situation and encourage them to speak freely and react to details.
There are two different scenarios involving AI in AML-CFT transaction monitoring systems:
• Case study 1: Automatic redirection and closing of alerts (Transaction Monitoring)
• Case study 2: Detection of new risk typologies (Transaction Monitoring)
See the scenarios in the rest of the registration files for more details.
Phase 3: The need for justifications
1. Do you think this use of AI is legitimate? useful?
2. What will Eric want to know to audit the system? What questions will Eric want to know
about the algorithm?
3. Does Bank B have to justify the use and the potential added value of AI? If so, how? What
would be the baseline?
4. Does Bank B need to justify changing or even eliminating any existing systems? If so, how?
5. Is it possible to set an overall system performance target in the AML-CFT environment? If
so, how can it be quantified? If not, why not?
For phase 4, examples of justifications are shown to participants showing examples of explanations of
AI systems/decisions.
Phase 4: Ideation on justifications
6. Are these justifications useful? Are they good ones? Are they necessary? Why?
7. What are the limits of these justifications? How can they be improved?

| 248 the | explanation |     | paradox | and | the | human | centric |     | path |     |     |     |
| ------- | ----------- | --- | ------- | --- | --- | ----- | ------- | --- | ---- | --- | --- | --- |
-
| C2. Compliance |      |         | assessment        |     |            |     |      |     |         |     |     |     |
| -------------- | ---- | ------- | ----------------- | --- | ---------- | --- | ---- | --- | ------- | --- | --- | --- |
| Table          | C.2: |         |                   |     |            |     |      |     |         |     |     |     |
|                |      | Summary | of the compliance |     | assessment |     | made | in  | Chapter |     |     |     |
6 to determine the points in the AML-CFT legislation with which AI
opacity interferes. The assessment was made for the two AI use cases
presented in Figure 631 . . : "SR" refers to "Risk Scoring" (Scenario 1 ), and
2
| "NT" to | "New | typologies | (scenario | ).  |     |     |            |     |     |     |     |     |
| ------- | ---- | ---------- | --------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|         |      |            |           |     |     | Is  | AI opacity |     | a   |     |     |     |
problem?
| AML-CFTTheme |     |     | Legalreference |     |     |     |     |       | Why? |     |     |     |
| ------------ | --- | --- | -------------- | --- | --- | --- | --- | ----- | ---- | --- | --- | --- |
|              |     |     |                |     |     | For |     | which |      |     |     |     |
model?
|          |           |     | French |       | Monetary |     |     |     |                                  |     |     |     |
| -------- | --------- | --- | ------ | ----- | -------- | --- | --- | --- | -------------------------------- | --- | --- | --- |
| Customer | knowledge | and | con-   |       |          |     |     |     | Theupdateofcustomerandbeneficial |     |     |     |
|          |           |     | Code   | (CMF) | Articles |     |     |     |                                  |     |     |     |
stantvigilanceoverbusinessre- L.561-4-1 561- No owner databases is not made with AI
to L.
| lationships |     |     |     |     |     |     |     |     | intheusecasesweareconsidering. |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- |
14-2
Banksneedtounderstandthenewty-
|     |     |     | CMF | Article | L. 561- |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
Riskclassification 4-1 YesforNT pologies of risk detected by the AI to
updatetheirriskclassification.
Calibration / allocation of ma- CMF Article R. 561- AssessingthesuitabilityofAIforpri-
YesforRS
| terialandhumanresources |     |     | 38                |     |     |          |     |     | oritizingalerts |          |        |        |
| ----------------------- | --- | --- | ----------------- | --- | --- | -------- | --- | --- | --------------- | -------- | ------ | ------ |
|                         |     |     | CMFArticleL.561-6 |     |     |          |     |     | Justifications  | might be | needed | on the |
| Constantvigilance       |     |     |                   |     |     | YesforNT |     |     |                 |          |        |        |
trainingfrequency.
|     |     |     |     |     |     |     |     |     | The relevance | of a model | can | be jus- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ------- |
Careful examination: Abil- tified with performance statistics, but
CMFArticleL.561-6
ity to detect inconsisten- YesforNT understanding why an anomaly was
| cies/anomalies |     |     |     |     |     |     |     |     | not detected | is important | for | both su- |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | --- | -------- |
pervisorsandbanks.
|            |        |      | Sanction |     | Decision |     |     |        |                               |     |     |     |
| ---------- | ------ | ---- | -------- | --- | -------- | --- | --- | ------ | ----------------------------- | --- | --- | --- |
| Processing | alerts | in a | timely   |     |          | Yes | for | NT and |                               |     |     |     |
|            |        |      | BMW      |     | Finance  |     |     |        | AIopacitycanmakereviewslonger |     |     |     |
| manner     |        |      |          |     |          | SR  |     |        |                               |     |     |     |
16/06/23
561-
|            |     |              | CMF   | Article  | R.  |     |     |     |               |         |       |     |
| ---------- | --- | ------------ | ----- | -------- | --- | --- | --- | --- | ------------- | ------- | ----- | --- |
| Adaptation | /   | completeness | of    |          |     |     |     |     | The alignment | between | human | and |
|            |     |              | 12-1, | Sanction | De- |     |     |     |               |         |       |     |
the system in relation to the YesforNT machine on important parameters
|                    |     |     | cision | Axa | Banque |     |     |     |                      |     |     |     |
| ------------------ | --- | --- | ------ | --- | ------ | --- | --- | --- | -------------------- | --- | --- | --- |
| riskclassification |     |     |        |     |        |     |     |     | shouldbedemonstrated |     |     |     |
15/02/23
561-
Enhanced vigilance: ability to CMF Article L. We need to be able to understand the
|                    |              |         | 10-2    |         |         | YesforSR |     |        |                                  |               |            |     |
| ------------------ | ------------ | ------- | ------- | ------- | ------- | -------- | --- | ------ | -------------------------------- | ------------- | ---------- | --- |
| analyzeriskyalerts |              |         |         |         |         |          |     |        | criteriathatgenerateariskyalert. |               |            |     |
| SAR obligation:    |              | ability | to pro- |         |         |          |     |        |                                  |               |            |     |
|                    |              |         | CMF     | Article | L. 561- | Yes      | for | SR and | We need                          | to be able to | understand | the |
| duce               | high-quality | SAR     | when 15 |         |         |          |     |        |                                  |               |            |     |
|                    |              |         |         |         |         | NT       |     |        | criteriathatgenerateariskyalert. |               |            |     |
relevant
|                  |     |                |          |         |       |     |     |        | Have to       | be able to             | anticipate | the     |
| ---------------- | --- | -------------- | -------- | ------- | ----- | --- | --- | ------ | ------------- | ---------------------- | ---------- | ------- |
| Internalcontrol: |     | incidentdetec- |          |         |       |     |     |        |               |                        |            |         |
|                  |     |                |          |         |       |     |     |        | model’s       | behavior to anticipate |            | plausi- |
| tion; Stability  |     | over time;     | mas- CMF | Article | R561- |     |     |        |               |                        |            |         |
|                  |     |                |          |         |       | Yes | for | SR and | bleincidents; | HavetodemonstrateAI    |            |         |
38-4,
| tering | of the system | (from      | ex-            | Order |     | of  |     |     |          |                 |      |       |
| ------ | ------------- | ---------- | -------------- | ----- | --- | --- | --- | --- | -------- | --------------- | ---- | ----- |
|        |               |            | November3,2014 |       |     | NT  |     |     | behavior | does not drift; | Have | to be |
| ternal | service       | provider); | Safety         |       |     |     |     |     |          |                 |      |       |
abletodemonstratethecontrolofyour
netincaseoffailure
system.

appendix 249

| 250 the | explanation | paradox | and the human | centric path |
| ------- | ----------- | ------- | ------------- | ------------ |
-

Bibliography
Ashraf Abdul, Jo Vermeulen, Danding Wang, Brian Y. Lim, and Mohan Kankanhalli. Trends and Tra-
jectories for Explainable, Accountable and Intelligible Systems: An HCI Research Agenda. In Pro-
ceedings of the 2018 CHI Conference on Human Factors in Computing Systems, CHI ’18, pages 1–18, New
York, NY, USA, April 2018. Association for Computing Machinery. ISBN 978-1-4503-5620-6. doi:
10.1145/3173574.3174156. URLhttps://doi.org/10.1145/3173574.3174156.
Ashraf Abdul, Christian von der Weth, Mohan Kankanhalli, and Brian Y. Lim. COGAM: Measuring
and Moderating Cognitive Load in Machine Learning Model Explanations. In Proceedings of the 2020
CHI Conference on Human Factors in Computing Systems, pages 1–14, New York, NY, USA, April 2020.
AssociationforComputingMachinery. ISBN978-1-4503-6708-0. URLhttps://doi.org/10.1145/3313
831.3376615.
Chadia Abras, Diane Maloney-Krichmar, Jenny Preece, and others. User-centered design. Bainbridge,W.
EncyclopediaofHuman-ComputerInteraction.ThousandOaks: SagePublications,37(4):445–456,2004.
DaronAcemoglu. HarmsofAI,September2021. URLhttps://www.nber.org/papers/w29247. Accessed
2023-11-27.
Alessandro Acquisti, Laura Brandimarte, and George Loewenstein. Privacy and human behavior in the
age of information. Science, 347(6221):509–514, January 2015. doi: 10.1126/science.aaa1465. URL
https://www.science.org/doi/10.1126/science.aaa1465. Publisher: American Association for the
AdvancementofScience.
A. Adadi and M. Berrada. Peeking Inside the Black-Box: A Survey on Explainable Artificial Intelli-
gence (XAI). IEEE Access, 6:52138–52160, 2018. ISSN 2169-3536. doi: 10.1109/ACCESS.2018.2870052.
ConferenceName: IEEEAccess.
Julius Adebayo, Justin Gilmer, Michael Muelly, Ian Goodfellow, Moritz Hardt, and Been Kim. Sanity
ChecksforSaliencyMaps,November2020. URLhttp://arxiv.org/abs/1810.03292. arXiv:1810.03292
[cs,stat].
Darius Afchar, Alessandro B. Melchiorre, Markus Schedl, Romain Hennequin, Elena V. Epure, and
ManuelMoussallam. Explainabilityinmusicrecommendersystems. AIMagazine,43(2):190–208,2022.
ISSN 2371-9621. doi: 10.1002/aaai.12056. URL https://onlinelibrary.wiley.com/doi/abs/10.100
2/aaai.12056. _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/aaai.12056.
Sabbir Ahmad, Andy Bryant, Erica Kleinman, Zhaoqing Teng, Truong-Huy D. Nguyen, and Magy Seif
El-Nasr. Modeling Individual and Team Behavior through Spatio-temporal Analysis. In Proceedings
of the Annual Symposium on Computer-Human Interaction in Play, CHI PLAY ’19, pages 601–612, New
York, NY, USA, October 2019. Association for Computing Machinery. ISBN 978-1-4503-6688-5. doi:
10.1145/3311350.3347188. URLhttps://doi.org/10.1145/3311350.3347188.
Ahn, Yongsu, Yan, Muheng, Lin, Yu-Ru, Chung, Wen-Ting, and Hwa, Rebecca. Tribe or Not? Critical
Inspection of Group Differences Using TribalGram. ACM Transactions on Interactive Intelligent Systems
(TiiS), March 2022. doi: 10.1145/3484509. URL https://dl.acm.org/doi/full/10.1145/3484509.
Publisher: ACMPUB27NewYork,NY.

| 252 the | explanation | paradox |     | and the | human | centric path |     |     |     |
| ------- | ----------- | ------- | --- | ------- | ----- | ------------ | --- | --- | --- |
-
Zeynep Akata, Dan Balliet, Maarten de Rijke, Frank Dignum, Virginia Dignum, Guszti Eiben, Antske
Fokkens,DavideGrossi,KoenHindriks,HolgerHoos,HayleyHung,CatholijnJonker,ChristofMonz,
Mark Neerincx, Frans Oliehoek, Henry Prakken, Stefan Schlobach, Linda van der Gaag, Frank van
Harmelen, Herke van Hoof, Birna van Riemsdijk, Aimee van Wynsberghe, Rineke Verbrugge, Bart
Verheij, Piek Vossen, and Max Welling. A Research Agenda for Hybrid Intelligence: Augmenting
Human Intellect With Collaborative, Adaptive, Responsible, and Explainable Artificial Intelligence.
|           | 53(8):18–28, |        | 2020. |      | 1558-0814. | doi: 10.1109/MC.2020.2996587. |     |            |     |
| --------- | ------------ | ------ | ----- | ---- | ---------- | ----------------------------- | --- | ---------- | --- |
| Computer, |              | August |       | ISSN |            |                               |     | Conference |     |
| Name:     | Computer.    |        |       |      |            |                               |     |            |     |
Ekin Akyürek, Tolga Bolukbasi, Frederick Liu, Binbin Xiong, Ian Tenney, Jacob Andreas, and Kelvin
Guu. Towards Tracing Factual Knowledge in Language Models Back to the Training Data, October
| 2022. | URLhttp://arxiv.org/abs/2205.11482. |     |     |     | arXiv:2205.11482[cs]. |     |     |     |     |
| ----- | ----------------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
Raghad Al-Shabandar, Gaye Lightbody, Fiona Browne, Jun Liu, Haiying Wang, and Huiru Zheng. The
Application of Artificial Intelligence in Financial Compliance Management. In Proceedings of the 2019
InternationalConferenceonArtificialIntelligenceandAdvancedManufacturing,AIAM2019,pages1–6,New
|     |     | 2019. |     |     |     |     | 978-1-4503-7202-2. |     | doi: |
| --- | --- | ----- | --- | --- | --- | --- | ------------------ | --- | ---- |
York, NY, USA, October Association for Computing Machinery. ISBN
10.1145/3358331.3358339. URLhttps://dl.acm.org/doi/10.1145/3358331.3358339.
J Alammar. Ecco: An Open Source Library for the Explainability of Transformer Language Models. In
Heng Ji, Jong C. Park, and Rui Xia, editors, Proceedings of the 59th Annual Meeting of the Association for
ComputationalLinguisticsandthe11thInternationalJointConferenceonNaturalLanguageProcessing: System
|     |     | 249–257, |     |     | 2021. |     |     |     | doi: |
| --- | --- | -------- | --- | --- | ----- | --- | --- | --- | ---- |
Demonstrations, pages Online, August Association for Computational Linguistics.
10.18653/v1/2021.acl-demo.30. URL https://aclanthology.org/2021.acl-demo.30. Accessed 2023-
11-02.
Kars Alfrink, Ianus Keller, Neelke Doorn, and Gerd Kortuem. Contestable Camera Cars: A Speculative
Design Exploration of Public AI That Is Open and Responsive to Dispute. In Proceedings of the 2023
CHIConferenceonHumanFactorsinComputingSystems,CHI’23,pages1–16,NewYork,NY,USA,2023.
|             |               |     |            |      | 978-1-4503-9421-5. | doi: 10.1145/3544548.3580984. |     |     |     |
| ----------- | ------------- | --- | ---------- | ---- | ------------------ | ----------------------------- | --- | --- | --- |
| Association | for Computing |     | Machinery. | ISBN |                    |                               |     |     | URL |
https://dl.acm.org/doi/10.1145/3544548.3580984.
R.Amar, J.Eagan, andJ.Stasko. Low-levelcomponentsofanalyticactivityininformationvisualization.
InIEEESymposiumonInformationVisualization,2005.INFOVIS2005.,pages111–117,October2005. doi:
| 10.1109/INFVIS.2005.1532136. |     |     | ISSN:1522-404X. |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
Saleema Amershi, Maya Cakmak, William Bradley Knox, and Todd Kulesza. Power to the People: The
Role of Humans in Interactive Machine Learning. AI Magazine, 35(4):105–120, December 2014. ISSN
| 2371-9621. | doi: 10.1609/aimag.v35i4.2513. |     |     |     |     |     |     |     |     |
| ---------- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
URLhttps://ojs.aaai.org/index.php/aimagazine/arti
Accessed2021-04-16.
cle/view/2513.
SaleemaAmershi,DanWeld,MihaelaVorvoreanu,AdamFourney,BesmiraNushi,PennyCollisson,Jina
Suh, Shamsi Iqbal, Paul N. Bennett, Kori Inkpen, Jaime Teevan, Ruth Kikin-Gil, and Eric Horvitz.
Guidelines for Human-AI Interaction. In Proceedings of the 2019 CHI Conference on Human Factors in
ComputingSystems, pages 1–13, Glasgow Scotland Uk, May 2019. ACM. ISBN 978-1-4503-5970-2. doi:
10.1145/3290605.3300233.
URLhttps://dl.acm.org/doi/10.1145/3290605.3300233.
JenniferAmsterlawandHenryM.Wellman. TheoriesofMindinTransition: AMicrogeneticStudyofthe
Development of False Belief Understanding. Journal of Cognition and Development, 7(2):139–172, 2006.
ISSN1532-7647.
|     | Place: | USPublisher: |     | LawrenceErlbaum. |     |     |     |     |     |
| --- | ------ | ------------ | --- | ---------------- | --- | --- | --- | --- | --- |
Geoffrey R. Amthor. Multimedia in education: an introduction. Int. Business Mag., pages 32–39, 1992.
ISSN0192-592X.
Natalia Andrienko, Gennady Andrienko, Linara Adilova, Stefan Wrobel, and Theresa-Marie Rhyne. Vi-
sual Analytics for Human-Centered Machine Learning. IEEE computer graphics and applications, 42(1):
| 123–133,February2022. |     | ISSN1558-1756. |     | doi: | 10.1109/MCG.2021.3130314. |     |     |     |     |
| --------------------- | --- | -------------- | --- | ---- | ------------------------- | --- | --- | --- | --- |

bibliography 253
Ariful Islam Anik and Andrea Bunt. Data-Centric Explanations: Explaining Training Data of Machine
LearningSystemstoPromoteTransparency. InProceedingsofthe2021CHIConferenceonHumanFactors
in Computing Systems, pages 1–13, Yokohama Japan, May 2021. ACM. ISBN 978-1-4503-8096-6. doi:
10.1145/3411764.3445736. URLhttps://dl.acm.org/doi/10.1145/3411764.3445736.
Anthropic. DecomposingLanguageModelsIntoUnderstandableComponents,October2023. URLhttp
s://www.anthropic.com/index/decomposing-language-models-into-understandable-components.
Accessed2023-12-12.
Hilary Arksey and Lisa O’Malley. Scoping studies: towards a methodological framework. Inter-
national Journal of Social Research Methodology, 8(1):19–32, February 2005. ISSN 1364-5579. doi:
10.1080/1364557032000119616. URL https://doi.org/10.1080/1364557032000119616. Publisher:
Routledge_eprint: https://doi.org/10.1080/1364557032000119616.
Vijay Arya, Rachel K. E. Bellamy, Pin-Yu Chen, Amit Dhurandhar, Michael Hind, Samuel C. Hoffman,
Stephanie Houde, Q. Vera Liao, Ronny Luss, Aleksandra Mojsilovic´, Sami Mourad, Pablo Pedemonte,
Ramya Raghavendra, John Richards, Prasanna Sattigeri, Karthikeyan Shanmugam, Moninder Singh,
Kush R. Varshney, Dennis Wei, and Yunfeng Zhang. One Explanation Does Not Fit All: A Toolkit
and Taxonomy of AI Explainability Techniques. arXiv:1909.03012 [cs, stat], September 2019. URL
http://arxiv.org/abs/1909.03012. arXiv: 1909.03012.
S. Atakishiyev, H. Babiker, N. Farruque, R. Goebel1, M.-Y. Kima, M. H. Motallebi, J. Rabelo, T. Syed,
and O. R. Zaïane. A multi-component framework for the analysis and design of explainable artificial
intelligence,May2020. URLhttp://arxiv.org/abs/2005.01908. arXiv:2005.01908[cs].
AkankshaAtrey,KaleighClary,andDavidJensen.ExploratoryNotExplanatory: CounterfactualAnalysis
ofSaliencyMapsforDeepReinforcementLearning,February2020. URLhttp://arxiv.org/abs/1912
.05743. arXiv:1912.05743[cs].
Autorité de Contrôle Prudentiel et de Résolution. Annual Repport of the ACPR 2022. Technical report,
ACPR,BankofFrance,May2023a. URLhttps://acpr.banque-france.fr/sites/default/files/med
ias/documents/20230524_rapport_annuel_colb_2022.pdf. Accessed11/29/2023.
AutoritédeContrôlePrudentieletdeRésolution. Thematicreviewonautomatedsystemsformonitoring
AML/CFTtransactions. Technicalreport,ACPR,BankofFrance,April2023b. URLhttps://acpr.ban
que-france.fr/dispositifs-automatises-de-surveillance-des-operations-en-matiere-de-lcb
-ft. Accessed2023-08-26.
MichelAvitalandDovTe’eni. Fromgenerativefittogenerativecapacity: exploringanemergingdimen-
sion of information systems design and task performance. Information Systems Journal, 19(4):345–367,
2009. ISSN 1365-2575. doi: 10.1111/j.1365-2575.2007.00291.x. URL https://onlinelibrary.wiley.co
m/doi/abs/10.1111/j.1365-2575.2007.00291.x.
S. Sandra Bae, Clement Zheng, Mary Etta West, Ellen Yi-Luen Do, Samuel Huron, and Danielle Albers
Szafir. Making Data Tangible: A Cross-disciplinary Design Space for Data Physicalization. In CHI
Conference on Human Factors in Computing Systems, pages 1–18, New Orleans LA USA, April 2022.
ACM. ISBN 978-1-4503-9157-3. doi: 10.1145/3491102.3501939. URL https://dl.acm.org/doi/10.11
45/3491102.3501939.
N. Bagheri and G. Jamieson. Considering subjective trust and monitoring behavior in assessing
automation-induced “complacency”. 2004. URL https://www.semanticscholar.org/paper/CONS
IDERING-SUBJECTIVE-TRUST-AND-MONITORING-IN-Bagheri-Jamieson/4338960e130f8ddb57815b67f34c
4a03264ab820. Accessed2024-01-09.
N.R.BaileyandM.W.Scerbo. Automation-inducedcomplacencyformonitoringhighlyreliablesystems:
the role of task complexity, system experience, and operator trust. Theoretical Issues in Ergonomics
Science, 8(4):321–348, July 2007. ISSN 1463-922X. doi: 10.1080/14639220500535301. URL https://
doi.org/10.1080/14639220500535301. _eprint: https://doi.org/10.1080/14639220500535301 tex.ids=
bailey_automation-induced_2007publisher: Taylor&Francis.

254 the explanation paradox and the human centric path
-
Lisanne Bainbridge. Ironies of automation. Automatica, 19(6):775–779, November 1983. ISSN 0005-1098.
URLhttps://www.sciencedirect.com/science/article/pii/0005109883900468.
Ramnath Balasubramanian, Ari Chester, and Nick Milinkovich. Rewriting the rules: Digital and AI-
powered underwriting in life insurance. Consultancy Report, McKinsey & Company, July 2020. URL
https://www.mckinsey.com/industries/financial-services/our-insights/rewriting-the-rules
-digital-and-ai-powered-underwriting-in-life-insurance. Accessed2023-01-31.
Ramnath Balasubramanian, Ari Libarikian, and DougMcElhaney. Insurance2030—Theimpact ofAI on
thefutureofinsurance. Technicalreport,McKinsey&Company,March2021. URLhttps://www.mcki
nsey.com/industries/financial-services/our-insights/insurance-2030-the-impact-of-ai-on-t
he-future-of-insurance. Accessed2023-01-31.
Agathe Balayn, Mireia Yurrita, Jie Yang, and Ujwal Gadiraju. Fairness Toolkits, A Checkbox Culture?
On the Factors that Fragment Developer Practices in Handling Algorithmic Harms. In Proceedings of
the2023AAAI/ACMConferenceonAI,Ethics,andSociety,AIES’23,pages482–495,NewYork,NY,USA,
2023. Association for Computing Machinery. ISBN 9798400702310. doi: 10.1145/3600211.3604674.
URLhttps://dl.acm.org/doi/10.1145/3600211.3604674.
Gagan Bansal, Tongshuang Wu, Joyce Zhou, Raymond Fok, Besmira Nushi, Ece Kamar, Marco Tulio
Ribeiro,andDanielWeld. DoestheWholeExceeditsParts? TheEffectofAIExplanationsonComple-
mentary Team Performance. In Proceedings of the 2021 CHI Conference on Human Factors in Computing
Systems,CHI’21,pages1–16,NewYork,NY,USA,2021.AssociationforComputingMachinery. ISBN
978-1-4503-8096-6. doi: 10.1145/3411764.3445717. URLhttps://doi.org/10.1145/3411764.3445717.
NatãM.BarbosaandMonchuChen. RehumanizedCrowdsourcing: ALabelingFrameworkAddressing
BiasandEthicsinMachineLearning. InProceedingsofthe2019CHIConferenceonHumanFactorsinCom-
putingSystems,CHI’19,pages1–12,NewYork,NY,USA,2019.AssociationforComputingMachinery.
ISBN 978-1-4503-5970-2. doi: 10.1145/3290605.3300773. URL https://doi.org/10.1145/3290605.33
00773.
PabloBarceló,EgorVKostylev,MikaëlMonet,JorgePérez,JuanReutter,andJuan-PabloSilva.Thelogical
expressiveness of graph neural networks. In 8th International Conference on Learning Representations
(ICLR2020),Virtualconference,Ethiopia,April2020. URLhttps://hal.science/hal-03356968.
PhilipBarker. DesigningInteractiveLearning. InTondeJongandLuigiSarti,editors,DesignandProduc-
tionofMultimediaandSimulation-basedLearningMaterial, pages 1–30. Springer Netherlands, Dordrecht,
1994. ISBN978-94-011-0942-0. URLhttps://doi.org/10.1007/978-94-011-0942-0_1.
SolonBarocas,AndrewD.Selbst,andManishRaghavan. Thehiddenassumptionsbehindcounterfactual
explanations and principal reasons. In Proceedingsofthe2020ConferenceonFairness,Accountability,and
Transparency, FAT* ’20, pages 80–89, New York, NY, USA, January 2020. Association for Computing
Machinery. ISBN 978-1-4503-6936-7. doi: 10.1145/3351095.3372830. URL https://doi.org/10.1145/
3351095.3372830.
AlejandroBarredoArrieta,NataliaDíaz-Rodríguez,JavierDelSer,AdrienBennetot,SihamTabik,Alberto
Barbado, Salvador Garcia, Sergio Gil-Lopez, Daniel Molina, Richard Benjamins, Raja Chatila, and
Francisco Herrera. Explainable Artificial Intelligence (XAI): Concepts, taxonomies, opportunities and
challenges toward responsible AI. Information Fusion, 58:82–115, June 2020. ISSN 1566-2535. doi:
10.1016/j.inffus.2019.12.012. URLhttp://www.sciencedirect.com/science/article/pii/S156625351
9308103.
SarahBayer,HennerGimpel,andMoritzMarkgraf. Theroleofdomainexpertiseintrustingandfollow-
ing explainable AI decision support systems. Journal of Decision Systems, 0(0):1–29, 2021. ISSN 1246-
0125. doi: 10.1080/12460125.2021.1958505. URL https://doi.org/10.1080/12460125.2021.1958505.
Publisher: Taylor&Francis_eprint: https://doi.org/10.1080/12460125.2021.1958505.

bibliography 255
Valérie Beaudouin, Isabelle Bloch, David Bounie, Stéphan Clémençon, Florence d’Alché Buc, James Ea-
gan, Winston Maxwell, Pavlo Mozharovskyi, and Jayneel Parekh. Flexible and Context-Specific AI
Explainability: A Multidisciplinary Approach, March 2020. URL http://arxiv.org/abs/2003.07703.
arXiv:2003.07703[cs].
SanderBeckers. CausalExplanationsandXAI,February2022. URLhttp://arxiv.org/abs/2201.13169.
arXiv:2201.13169[cs].
Esube Bekele, Wallace E. Lawson, Zachary Horne, and Sangeet Khemlani. Implementing a Ro-
bust Explanatory Bias in a Person Re-identification Network. In 2018 IEEE/CVF Conference on
Computer Vision and Pattern Recognition Workshops (CVPRW), pages 2246–22467, June 2018. doi:
10.1109/CVPRW.2018.00291. ISSN:2160-7516.
R. K. E. Bellamy, K. Dey, M. Hind, S. C. Hoffman, S. Houde, K. Kannan, P. Lohia, J. Martino, S. Mehta,
A. Mojsilovic´, S. Nagar, K. Natesan Ramamurthy, J. Richards, D. Saha, P. Sattigeri, M. Singh, K. R.
Varshney, and Y. Zhang. AI Fairness 360: An extensible toolkit for detecting and mitigating algorith-
mic bias. IBM Journal of Research and Development, 63(4/5):4:1–4:15, July 2019. ISSN 0018-8646. doi:
10.1147/JRD.2019.2942287. ConferenceName: IBMJournalofResearchandDevelopment.
Luigi Bellomarini, Eleonora Laurenza, and Emanuel Sallinger. Rule-based Anti-Money Laundering in
FinancialIntelligenceUnits: ExperienceandVision.InProceedingsofthe14thInternationalRuleChallenge,
4th Doctoral Consortium, and 6th Industry Track @ RuleML+RR 2020, page 12, Oslo, Norway, July 2020.
CEURWorkshopProceedings.
Mariette Bengtsson. How to plan and perform a qualitative study using content analysis. NursingPlus
Open, 2:8–14, January 2016. ISSN 2352-9008. doi: 10.1016/j.npls.2016.01.001. URL https://www.scie
ncedirect.com/science/article/pii/S2352900816000029.
Astrid Bertrand, Winston Maxwell, and Xavier Vamparys. Do AI-based anti-money laundering (AML)
systems violate European fundamental rights? International Data Privacy Law, 11(3):276–293, August
2021. ISSN2044-3994. doi: 10.1093/idpl/ipab010. URLhttps://doi.org/10.1093/idpl/ipab010.
Astrid Bertrand, Rafik Belloum, James R. Eagan, and Winston Maxwell. How Cognitive Biases Affect
XAI-assisted Decision-making: A Systematic Review. In Proceedings of the 2022 AAAI/ACM Conference
onAI,Ethics,andSociety,AIES’22,pages78–91,NewYork,NY,USA,2022.AssociationforComputing
Machinery. ISBN 978-1-4503-9247-1. doi: 10.1145/3514094.3534164. URL https://doi.org/10.1145/
3514094.3534164.
Cornelia Betsch, Niels Haase, Frank Renkewitz, and Philipp Schmid. The narrative bias revisited: What
drivesthebiasinginfluenceofnarrativeinformationonriskperceptions? JudgmentandDecisionMaking,
10(3):241–264, May 2015. ISSN 1930-2975. doi: 10.1017/S1930297500004654. URL https://www.camb
ridge.org/core/journals/judgment-and-decision-making/article/narrative-bias-revisited-w
hat-drives-the-biasing-influence-of-narrative-information-on-risk-perceptions/52E778EFD
11CA174B5573A4AFE3664E1. Publisher: CambridgeUniversityPress.
Umang Bhatt, Alice Xiang, Shubham Sharma, Adrian Weller, Ankur Taly, Yunhan Jia, Joydeep Ghosh,
Ruchir Puri, José M. F. Moura, and Peter Eckersley. Explainable machine learning in deployment. In
Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency, FAT* ’20, pages 648–657,
New York, NY, USA, January 2020. Association for Computing Machinery. ISBN 978-1-4503-6936-7.
doi: 10.1145/3351095.3375624. URLhttps://doi.org/10.1145/3351095.3375624.
Umang Bhatt, Javier Antorán, Yunfeng Zhang, Q. Vera Liao, Prasanna Sattigeri, Riccardo Fogliato,
Gabrielle Melançon, Ranganath Krishnan, Jason Stanley, Omesh Tickoo, Lama Nachman, Rumi Chu-
nara, Madhulika Srikumar, Adrian Weller, and Alice Xiang. Uncertainty as a Form of Transparency:
Measuring,Communicating,andUsingUncertainty. InProceedingsofthe2021AAAI/ACMConferenceon
AI,Ethics,andSociety,pages401–413,NewYork,NY,USA,2021.AssociationforComputingMachinery.
ISBN978-1-4503-8473-5. URLhttps://doi.org/10.1145/3461702.3462571.

256 the explanation paradox and the human centric path
-
Adrien Bibal, Michael Lognoul, Alexandre de Streel, and Benoît Frénay. Legal requirements on explain-
ability in machine learning. Artificial Intelligence and Law, 29(2):149–169, June 2021. ISSN 1572-8382.
doi: 10.1007/s10506-020-09270-4. URLhttps://doi.org/10.1007/s10506-020-09270-4.
CharlesE.Billings. Human-CenteredAviationAutomation: PrinciplesandGuidelines. NASATechnicalMem-
orandum,February1996.
Blair Bilodeau, Natasha Jaques, Pang Wei Koh, and Been Kim. Impossibility Theorems for Feature
Attribution,April2023. URLhttp://arxiv.org/abs/2212.11870. arXiv:2212.11870[cs].
ReubenBinns,MaxVanKleek,MichaelVeale,UlrikLyngs,JunZhao,andNigelShadbolt. ’It’sReducing
a Human Being to a Percentage’: Perceptions of Justice in Algorithmic Decisions. In Proceedings of the
2018CHIConferenceonHumanFactorsinComputingSystems,CHI’18,pages1–14,NewYork,NY,USA,
2018. Association for Computing Machinery. ISBN 978-1-4503-5620-6. doi: 10.1145/3173574.3173951.
URLhttps://doi.org/10.1145/3173574.3173951.
Julia Black. Decentring Regulation: Understanding the Role of Regulation and Self-Regulation in a
‘Post-Regulatory’ World. Current Legal Problems, 54(1):103–146, January 2001. ISSN 0070-1998. doi:
10.1093/clp/54.1.103. URLhttps://doi.org/10.1093/clp/54.1.103.
Douglas Blakey. AI in anti money laundering, December 2022. URL https://www.retailbankerintern
ational.com/comment/ai-money-laundering/. Accessed2023-08-26.
Board of Governors of the Federal Reserve System, Federal Deposit Insurance Corporation, Financial
Crimes Enforcement Network, National Credit Union Administration, and Office of the Comptroller
of the Currency. Joint Statement on Innovative Efforts to Combat Money Laundering and Terrorist
Financing. Technicalreport, FederalReserveBoard, December2018. URLhttps://www.federalreser
ve.gov/newsevents/pressreleases/files/bcreg20181203a1.pdf. Accessed11/19/2023.
MargaretA. Boden. ArtificialIntelligence. Elsevier, June1996. ISBN978-0-08-052759-8. Google-Books-ID:
_ixmRlL9jcIC.
Clara Bove, Jonathan Aigrain, Marie-Jeanne Lesot, Charles Tijus, and Marcin Detyniecki. Contextu-
alization and Exploration of Local Feature Importance Explanations to Improve Understanding and
Satisfaction of Non-Expert Users. In 27th International Conference on Intelligent User Interfaces, pages
807–819,HelsinkiFinland,March2022.ACM. ISBN978-1-4503-9144-3. doi: 10.1145/3490099.3511139.
URLhttps://dl.acm.org/doi/10.1145/3490099.3511139.
JohnBraithwaiteandToniMakkai. Trustandcompliance. PolicingandSociety,4(1):1–12,May1994. ISSN
1043-9463. doi: 10.1080/10439463.1994.9964679. URL https://doi.org/10.1080/10439463.1994.99
64679. Publisher: Routledge_eprint: https://doi.org/10.1080/10439463.1994.9964679.
LauraBrandimarte,AlessandroAcquisti,andGeorgeLoewenstein. MisplacedConfidences: Privacyand
the Control Paradox. Social Psychological and Personality Science, 4(3):340–347, May 2013. ISSN 1948-
5506. doi: 10.1177/1948550612455931. URLhttps://doi.org/10.1177/1948550612455931. Publisher:
SAGEPublicationsInc.
DawnBranley-Bell,RebeccaWhitworth,andLynneCoventry. UserTrustandUnderstandingofExplain-
able AI: Exploring Algorithm Visualisations and User Biases. In Human-Computer Interaction. Human
ValuesandQualityofLife: ThematicArea,HCI2020,HeldasPartofthe22ndInternationalConference,HCII
2020, Copenhagen, Denmark, July 19–24, 2020, Proceedings, Part III, pages 382–399, Berlin, Heidelberg,
2020. Springer-Verlag. ISBN 978-3-030-49064-5. URL https://doi.org/10.1007/978-3-030-49065-2
_27.
DavidABroniatowski. Psychologicalfoundationsofexplainabilityandinterpretabilityinartificialintelli-
gence. TechnicalReportNISTIR8367,NationalInstituteofStandardsandTechnology(U.S.),Gaithers-
burg,MD,April2021. URLhttps://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8367.pdf.

bibliography 257
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin
Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario
Amodei.LanguageModelsareFew-ShotLearners,July2020.URLhttp://arxiv.org/abs/2005.14165.
arXiv:2005.14165[cs].
Joanna J. Bryson and Andreas Theodorou. How Society Can Maintain Human-Centric Artificial Intelli-
gence. InMarjaToivonenandEveliinaSaari,editors,Human-CenteredDigitalizationandServices,Trans-
lationalSystemsSciences,pages305–323.SpringerNature,Singapore,2019. ISBN9789811377259. URL
https://doi.org/10.1007/978-981-13-7725-9_16.
SébastienBubeck,VarunChandrasekaran,RonenEldan,JohannesGehrke,EricHorvitz,EceKamar,Peter
Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, Harsha Nori, Hamid Palangi, Marco Tulio Ribeiro, and
Yi Zhang. Sparks of Artificial General Intelligence: Early experiments with GPT-4, April 2023. URL
http://arxiv.org/abs/2303.12712. arXiv:2303.12712[cs].
B.G.BuchananandE.H.Shortliffe. Rule-basedexpertsystems: Themycinexperimentsofthestanfordheuristic
programmingproject: B.G.BuchananandE.H.Shortliffe. Addison-Wesley,Reading,MA,July1985.
Mario Bunge. Philosophy of Science: From Explanation to Justification. Transaction Publishers, 1998. ISBN
978-1-4128-3083-6. Google-Books-ID:ofcy8wZeLCoC.
NadiaBurkartandMarcoF.Huber.ASurveyontheExplainabilityofSupervisedMachineLearning.Jour-
nalofArtificialIntelligenceResearch,70:245–317,January2021. ISSN1076-9757. doi: 10.1613/jair.1.12228.
URLhttp://arxiv.org/abs/2011.07876.
Jenna Burrell. How the machine ‘thinks’: Understanding opacity in machine learning algorithms. Big
Data & Society, 3(1):2053951715622512, June 2016. ISSN 2053-9517. doi: 10.1177/2053951715622512.
URLhttps://doi.org/10.1177/2053951715622512. Publisher: SAGEPublicationsLtd.
A. Bussone, S. Stumpf, and D. O’Sullivan. The Role of Explanations on Trust and Reliance in Clinical
Decision Support Systems. In 2015 International Conference on Healthcare Informatics, pages 160–169,
October2015. doi: 10.1109/ICHI.2015.26.
Zana Buçinca, Phoebe Lin, Krzysztof Z. Gajos, and Elena L. Glassman. Proxy tasks and subjective
measurescanbemisleadinginevaluatingexplainableAIsystems. InProceedingsofthe25thInternational
Conference on Intelligent User Interfaces, pages 454–464, Cagliari Italy, March 2020. ACM. ISBN 978-1-
4503-7118-6. doi: 10.1145/3377325.3377498. URL https://dl.acm.org/doi/10.1145/3377325.33774
98.
Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos. To Trust or to Think: Cognitive Forcing
Functions Can Reduce Overreliance on AI in AI-assisted Decision-making. Proceedings of the ACM
on Human-Computer Interaction, 5(CSCW1):188:1–188:21, 2021. doi: 10.1145/3449287. URL https:
//doi.org/10.1145/3449287.
ChristophBösch,BenjaminErb,FrankKargl,HenningKopp,andStefanPfattheicher.TalesfromtheDark
Side: PrivacyDarkStrategiesandPrivacyDarkPatterns. ProceedingsonPrivacyEnhancingTechnologies,
2016. ISSN2299-0984. URLhttps://petsymposium.org/popets/2016/popets-2016-0038.php.
Susanne Bødker. When second wave HCI meets third wave challenges. In Proceedings of the 4th Nordic
conference on Human-computer interaction: changing roles, pages 1–8, Oslo Norway, October 2006. ACM.
ISBN 978-1-59593-325-6. doi: 10.1145/1182475.1182476. URL https://dl.acm.org/doi/10.1145/118
2475.1182476.
Ángel Alexander Cabrera, Marco Tulio Ribeiro, Bongshin Lee, Rob DeLine, Adam Perer, and Steven M
Drucker. What Did My AI Learn? How Data Scientists Make Sense of Model Behavior. ACMTransac-
tionsonComputer-HumanInteraction,2022. Publisher: ACMNewYork,NY.

258 the explanation paradox and the human centric path
-
CarrieJ.Cai,JonasJongejan,andJessHolbrook. Theeffectsofexample-basedexplanationsinamachine
learninginterface. InProceedingsofthe24thInternationalConferenceonIntelligentUserInterfaces,IUI’19,
pages 258–262, New York, NY, USA, March 2019. Association for Computing Machinery. ISBN 978-1-
4503-6272-6. doi: 10.1145/3301275.3302289. URL https://dl.acm.org/doi/10.1145/3301275.33022
89.
Michael L. Callaham, Robert L. Wears, Ellen J. Weber, Christopher Barton, and Gary Young. Positive-
Outcome Bias and Other Limitations in the Outcome of Research Abstracts Submitted to a Scientific
Meeting. JAMA,280(3):254–257,July1998. ISSN0098-7484. doi: 10.1001/jama.280.3.254. URLhttps:
//doi.org/10.1001/jama.280.3.254.
Ana Isabel Canhoto. Leveraging machine learning in the global fight against money laundering and
terrorism financing: An affordances perspective. Journal of Business Research, 131:441–452, October
2020. ISSN 0148-2963. doi: 10.1016/j.jbusres.2020.10.012. URL http://www.sciencedirect.com/scie
nce/article/pii/S0148296320306640.
John M. Carroll. Chapter 17 - Scenario-Based Design. In Marting G. Helander, Thomas K. Landauer,
andPrasadV.Prabhu,editors,HandbookofHuman-ComputerInteraction(SecondEdition),pages383–406.
North-Holland, Amsterdam, January 1997. ISBN 978-0-444-81862-1. doi: 10.1016/B978-044481862-
1.50083-2. URLhttps://www.sciencedirect.com/science/article/pii/B9780444818621500832.
ShanCarter,ZanArmstrong, LudwigSchubert,IanJohnson,andChrisOlah. ActivationAtlas. Distill,4
(3):e15, March 2019. ISSN 2476-0757. doi: 10.23915/distill.00015. URL https://distill.pub/2019/a
ctivation-atlas.
Rich Caruana, Yin Lou, Johannes Gehrke, Paul Koch, Marc Sturm, and Noemie Elhadad. Intelligible
Models for HealthCare: Predicting Pneumonia Risk and Hospital 30-day Readmission. In Proceedings
of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, KDD ’15,
pages 1721–1730, New York, NY, USA, 2015. Association for Computing Machinery. ISBN 978-1-4503-
3664-2. doi: 10.1145/2783258.2788613. URLhttps://dl.acm.org/doi/10.1145/2783258.2788613.
Diogo V. Carvalho, Eduardo M. Pereira, and Jaime S. Cardoso. Machine Learning Interpretability: A
Survey on Methods and Metrics. Electronics, 8(8):832, August 2019. doi: 10.3390/electronics8080832.
URL https://www.mdpi.com/2079-9292/8/8/832. Number: 8 Publisher: Multidisciplinary Digital
PublishingInstitute.
A. Cawsey. User modelling in interactive explanations. User Modeling and User-Adapted Interaction, 3(3):
221–247,1993. ISSN1573-1391. doi: 10.1007/BF01257890. Springer.
Raja Chatila, Virginia Dignum, Michael Fisher, Fosca Giannotti, Katharina Morik, Stuart Russell, and
KarenYeung. TrustworthyAI. InBertrandBraunschweigandMalikGhallab,editors,ReflectionsonAr-
tificialIntelligenceforHumanity,LectureNotesinComputerScience,pages13–39.SpringerInternational
Publishing,Cham,2021. URLhttps://doi.org/10.1007/978-3-030-69128-8_2.
Aditya Chattopadhyay, Piyushi Manupriya, Anirban Sarkar, and Vineeth N. Balasubramanian. Neural
Network Attributions: A Causal Perspective, July 2019. URL http://arxiv.org/abs/1902.02302.
arXiv:1902.02302[cs,stat].
Larissa Chazette and Kurt Schneider. Explainability as a non-functional requirement: challenges and
recommendations. Requirements Engineering, 25(4):493–514, December 2020. ISSN 1432-010X. doi:
10.1007/s00766-020-00333-1. URLhttps://doi.org/10.1007/s00766-020-00333-1.
Chaofan Chen, Oscar Li, Daniel Tao, Alina Barnett, Cynthia Rudin, and Jonathan K Su. This Looks Like
That: Deep Learning for Interpretable Image Recognition. In AdvancesinNeuralInformationProcessing
Systems, volume32.CurranAssociates, Inc., 2019. URLhttps://proceedings.neurips.cc/paper/201
9/hash/adf7ee2dcf142b0e11888e72b43fcb75-Abstract.html.

bibliography 259
Valerie Chen, Q. Vera Liao, Jennifer Wortman Vaughan, and Gagan Bansal. Understanding the Role
of Human Intuition on Reliance in Human-AI Decision-Making with Explanations. Proceedings of the
ACM on Human-Computer Interaction, 7(CSCW2):370:1–370:32, October 2023. doi: 10.1145/3610219.
URLhttps://dl.acm.org/doi/10.1145/3610219.
Zhiyuan Chen, Le Dinh Van Khoa, Ee Na Teoh, Amril Nazir, Ettikan Kandasamy Karuppiah, and
KimSimLam. Machinelearningtechniquesforanti-moneylaundering(AML)solutionsinsuspicious
transactiondetection: areview. KnowledgeandInformationSystems,57(2):245–285,November2018. ISSN
0219-3116. doi: 10.1007/s10115-017-1144-z. URLhttps://doi.org/10.1007/s10115-017-1144-z.
Furui Cheng, Yao Ming, and Huamin Qu. DECE: Decision Explorer with Counterfactual Explanations
for Machine Learning Models. IEEE Transactions on Visualization and Computer Graphics, 27(2):1438–
1447, February 2021. ISSN 1941-0506. doi: 10.1109/TVCG.2020.3030342. Conference Name: IEEE
TransactionsonVisualizationandComputerGraphics.
Furui Cheng, Dongyu Liu, Fan Du, Yanna Lin, Alexandra Zytek, Haomin Li, Huamin Qu, and Kalyan
Veeramachaneni. VBridge: Connecting the Dots Between Features and Data to Explain Healthcare
Models. IEEE Transactions on Visualization and Computer Graphics, 28(1):378–388, January 2022. ISSN
1941-0506. doi: 10.1109/TVCG.2021.3114836. Conference Name: IEEE Transactions on Visualization
andComputerGraphics.
Hao-Fei Cheng, Ruotong Wang, Zheng Zhang, Fiona O’Connell, Terrance Gray, F. Maxwell Harper, and
HaiyiZhu. ExplainingDecision-MakingAlgorithmsthroughUI:StrategiestoHelpNon-ExpertStake-
holders. InProceedingsofthe2019CHIConferenceonHumanFactorsinComputingSystems,CHI’19,pages
1–12,NewYork,NY,USA,2019.AssociationforComputingMachinery. ISBN978-1-4503-5970-2. doi:
10.1145/3290605.3300789. URLhttps://doi.org/10.1145/3290605.3300789.
Michelene T. H. Chi, Nicholas De Leeuw, Mei-Hung Chiu, and Christian Lavancher. Eliciting self-
explanations improves understanding. Cognitive Science, 18(3):439–477, July 1994. ISSN 0364-0213.
doi: 10.1016/0364-0213(94)90016-7. URL https://www.sciencedirect.com/science/article/pii/03
64021394900167.
Michael Chromik and Andreas Butz. Human-XAI Interaction: A Review and Design Principles for
ExplanationUserInterfaces. InCarmeloArdito,RosaLanzilotti,AlessioMalizia,HelenPetrie,Antonio
Piccinno, Giuseppe Desolda, and Kori Inkpen, editors, Human-ComputerInteraction–INTERACT2021,
Lecture Notes in Computer Science, pages 619–640, Cham, 2021. Springer International Publishing.
ISBN978-3-030-85616-8.
Michael Chromik, Malin Eiband, Felicitas Buchner, Adrian Krüger, and Andreas Butz. I Think I Get
Your Point, AI! The Illusion of Explanatory Depth in Explainable AI. In 26th International Conference
on Intelligent User Interfaces, IUI ’21, pages 307–317, New York, NY, USA, April 2021. Association for
ComputingMachinery. ISBN978-1-4503-8017-1. doi: 10.1145/3397481.3450644. URLhttps://doi.or
g/10.1145/3397481.3450644.
Douglas Cirqueira, Dietmar Nedbal, Markus Helfert, and Marija Bezbradica. Scenario-Based Require-
mentsElicitationforUser-CentricExplainableAI. InAndreasHolzinger,PeterKieseberg,AMinTjoa,
and Edgar Weippl, editors, Machine Learning and Knowledge Extraction, Lecture Notes in Computer
Science,pages321–341,Cham,2020.SpringerInternationalPublishing. ISBN978-3-030-57321-8.
Ludovik Coba, Laurens Rook, Markus Zanker, and Panagiotis Symeonidis. Decision making strategies
differ in the presence of collaborative explanations: two conjoint studies. In Proceedings of the 24th
InternationalConferenceonIntelligentUserInterfaces,IUI’19,pages291–302,NewYork,NY,USA,March
2019. Association for Computing Machinery. ISBN 978-1-4503-6272-6. doi: 10.1145/3301275.3302304.
URLhttps://doi.org/10.1145/3301275.3302304.
Dennis Collaris and Jarke J. van Wijk. ExplainExplore: Visual Exploration of Machine Learning Ex-
planations. In 2020 IEEE Pacific Visualization Symposium (PacificVis), pages 26–35, June 2020. doi:
10.1109/PacificVis48177.2020.7090. ISSN:2165-8773.

260 the explanation paradox and the human centric path
-
Jason A. Colquitt and Jessica B. Rodell. Measuring justice and fairness. In The Oxford handbook of justice
intheworkplace,Oxfordlibraryofpsychology,pages187–202.OxfordUniversityPress,NewYork,NY,
US,2015. ISBN978-0-19-998141-0. doi: 10.1093/oxfordhb/9780199981410.013.8.
Roberto Confalonieri, Ludovik Coba, Benedikt Wagner, and Tarek R. Besold. A historical perspective of
explainableArtificialIntelligence. WIREsDataMiningandKnowledgeDiscovery,11(1):e1391,2021. ISSN
1942-4795. doi: 10.1002/widm.1391. URL https://onlinelibrary.wiley.com/doi/abs/10.1002/wi
dm.1391. _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/widm.1391.
Conseild’Orientationpourlaluttecontreleblanchimentetlefinancementduterrorisme. AnnualReport
2022. Technical report, COLB, May 2023. URL https://acpr.banque-france.fr/sites/default/fil
es/medias/documents/20230524_rapport_annuel_colb_2022.pdf.
SvenCoppers,JanVandenBergh,KrisLuyten,KarinConinx,IuliannavanderLek-Ciudin,TomVanalle-
meersch, and Vincent Vandeghinste. Intellingo: An Intelligible Translation Environment. In Proceed-
ings of the 2018 CHI Conference on Human Factors in Computing Systems, CHI ’18, pages 1–13, New
York, NY, USA, April 2018. Association for Computing Machinery. ISBN 978-1-4503-5620-6. doi:
10.1145/3173574.3174098. URLhttps://doi.org/10.1145/3173574.3174098.
Juliet Corbin and Anselm Strauss. Basics of Qualitative Research: Techniques and Procedures for Developing
GroundedTheory.SAGEPublications,Inc.2455TellerRoadThousandOaks,California91320,November
2014. ISBN978-1-4833-1568-3. Google-Books-ID:hZ6kBQAAQBAJ.
Council of Europe. History of Artificial Intelligence - Artificial Intelligence - www.coe.int, 2023. URL
https://www.coe.int/en/web/artificial-intelligence/history-of-ai.
David Daniel Cox and Thomas Dean. Neural Networks and Neuroscience-Inspired Computer Vision.
Current Biology, 24(18):R921–R929, September 2014. ISSN 0960-9822. doi: 10.1016/j.cub.2014.08.026.
URLhttps://www.sciencedirect.com/science/article/pii/S0960982214010392.
Mark Craven and Jude Shavlik. Extracting Tree-Structured Representations of Trained Networks. In
Advances in Neural Information Processing Systems, volume 8. MIT Press, 1995. URL https://proceedi
ngs.neurips.cc/paper/1995/hash/45f31d16b1058d586fc3be7207b58053-Abstract.html.
John W. Creswell. Qualitative Inquiry and Research Design: Choosing Among Five Approaches. SAGE Publi-
cations,March2012. ISBN978-1-4129-9530-6. Google-Books-ID:OJYEbDtkxq8C.
MichaelCui. ThestateofAIin2023: GenerativeAI’sbreakoutyear,April2023. URLhttps://www.mcki
nsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-2023-generative-ais-b
reakout-year.
KimberlyCulleyandPoornimaMadhavan. Trustinautomationandautomationdesigners: Implications
for HCI and HMI. Computers in Human Behavior, 29(6):2208–2210, November 2013. ISSN 0747-5632.
doi: 10.1016/j.chb.2013.04.032. URL http://www.sciencedirect.com/science/article/pii/S07475
63213001441.
M. L. Cummings. Automation Bias in Intelligent Time Critical Decision Support Systems. In AIAA 3rd
IntelligentSystemsConference,pages2004–6313.AIAA,2004.
Brigham Daniels, Mark Buntaine, and Tanner Bangerter. Testing Transparency. Northwestern University
LawReview,114:1263,2019. URLhttps://heinonline.org/HOL/Page?handle=hein.journals/illlr11
4&id=1293&div=&collection=.
DavidDanks. TheValueofTrustworthyAI. InProceedingsofthe2019AAAI/ACMConferenceonAI,Ethics,
and Society, pages 521–522, Honolulu HI USA, January 2019. ACM. ISBN 978-1-4503-6324-2. doi:
10.1145/3306618.3314228. URLhttps://dl.acm.org/doi/10.1145/3306618.3314228.

|     |     |     |     |     |     | bibliography |     | 261 |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- |
Valdemar Danry, Pat Pataranutaporn, Yaoli Mao, and Pattie Maes. Wearable Reasoner: Towards En-
hancedHumanRationalityThroughAWearableDeviceWithAnExplainableAIAssistant. InProceed-
ingsoftheAugmentedHumansInternationalConference,AHs’20,pages1–12,NewYork,NY,USA,March
| 2020.       |     |           |            |      | 978-1-4503-7603-7. | doi: 10.1145/3384657.3384799. |     |     |
| ----------- | --- | --------- | ---------- | ---- | ------------------ | ----------------------------- | --- | --- |
| Association | for | Computing | Machinery. | ISBN |                    |                               |     |     |
URLhttps://doi.org/10.1145/3384657.3384799.
Valdemar Danry, Pat Pataranutaporn, Yaoli Mao, and Pattie Maes. Don’t Just Tell Me, Ask Me: AI
SystemsthatIntelligentlyFrameExplanationsasQuestionsImproveHumanLogicalDiscernmentAc-
curacy over Causal AI explanations. In Proceedings of the 2023 CHI Conference on Human Factors in
|     |     | ’23, | 1–13, |     | 2023. |     |     |     |
| --- | --- | ---- | ----- | --- | ----- | --- | --- | --- |
Computing Systems, CHI pages New York, NY, USA, Association for Computing Ma-
|          | 978-1-4503-9421-5. |     | doi: | 10.1145/3544548.3580672. |     |                            |     |     |
| -------- | ------------------ | --- | ---- | ------------------------ | --- | -------------------------- | --- | --- |
| chinery. | ISBN               |     |      |                          | URL | https://dl.acm.org/doi/10. |     |     |
1145/3544548.3580672.
Arun Das and Paul Rad. Opportunities and Challenges in Explainable Artificial Intelligence (XAI): A
Survey,June2020. arXiv:2006.11371[cs].
URLhttp://arxiv.org/abs/2006.11371.
Richard Dazeley, Peter Vamplew, Cameron Foale, Charlotte Young, Sunil Aryal, and Francisco Cruz.
Levels of explainable artificial intelligence for human-aligned conversational explanations. Artificial
299:103525, 2021. 0004-3702. doi: 10.1016/j.artint.2021.103525.
| Intelligence, |     | October |     | ISSN |     |     | URL | https: |
| ------------- | --- | ------- | --- | ---- | --- | --- | --- | ------ |
//www.sciencedirect.com/science/article/pii/S000437022100076X.
JohnDewey. DemocracyinEducation. THEELEMENTARYSCHOOLTEACHER,page12,1903.
Berkeley J. Dietvorst, Joseph P. Simmons, and Cade Massey. Algorithm aversion: People erroneously
General,144(1):114–126,2015.
| avoidalgorithmsafterseeingthemerr. |     |     |     | JournalofExperimentalPsychology: |     |     |     |     |
| ---------------------------------- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- |
ISSN1939-2222,0096-3445. doi: 10.1037/xge0000033. URLhttp://doi.apa.org/getdoi.cfm?doi=10.
1037/xge0000033.
Alan Dix and Geoffrey Ellis. Starting simple: adding value to static visualisation through simple in-
teraction. In Proceedings of the working conference on Advanced visual interfaces, AVI ’98, pages 124–134,
|                        |          | 1998.                                     |     |               |            | 978-1-4503-7435-4. |     | doi: |
| ---------------------- | -------- | ----------------------------------------- | --- | ------------- | ---------- | ------------------ | --- | ---- |
| New York,              | NY, USA, | Association                               |     | for Computing | Machinery. | ISBN               |     |      |
| 10.1145/948496.948514. |          | URLhttps://doi.org/10.1145/948496.948514. |     |               |            |                    |     |      |
David H. Dodd and Jeffrey M. Bradshaw. Leading Questions and Memory: Pragmatic Constraints.
JournalofVerbalLearningandVerbalBehavior,19(6):695–704,December1980. EJ236855.
ERICNumber:
Jonathan Dodge, Andrew A. Anderson, Matthew Olson, Rupika Dikkala, and Margaret Burnett. How
Do People Rank Multiple Mutant Agents? In 27th International Conference on Intelligent User Interfaces,
IUI’22,pages191–211,NewYork,NY,USA,March2022.AssociationforComputingMachinery.
ISBN
| 978-1-4503-9144-3. |     | doi: 10.1145/3490099.3511115. |     |     |     |     |     |     |
| ------------------ | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
URLhttps://doi.org/10.1145/3490099.3511115.
VicenteDominguez,PabloMessina,IvaniaDonoso-Guzmán,andDenisParra. Theeffectofexplanations
and algorithmic accuracy on visual recommender systems of artistic images. In Proceedings of the 24th
InternationalConferenceonIntelligentUserInterfaces,IUI’19,pages408–416,NewYork,NY,USA,March
2019. Association for Computing Machinery. ISBN 978-1-4503-6272-6. doi: 10.1145/3301275.3302274.
URLhttps://doi.org/10.1145/3301275.3302274.
Derek Doran, Sarah Schulz, and Tarek R. Besold. What Does Explainable AI Really Mean? A
New Conceptualization of Perspectives, October 2017. URL http://arxiv.org/abs/1710.00794.
arXiv:1710.00794[cs].
FinaleDoshi-VelezandBeenKim.TowardsARigorousScienceofInterpretableMachineLearning,March
| 2017. URLhttp://arxiv.org/abs/1702.08608. |     |     |     |     | arXiv:1702.08608[cs,stat]. |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |
Finale Doshi-Velez and Mason A. Kortz. Accountability of AI Under the Law: The Role of Explanation.
Berkman Klein Center for Internet & Society working paper, Berkman Klein Center Working Group on
Explanation and the Law:17, 2017. URL https://dash.harvard.edu/handle/1/34372584. Accepted:
2017-11-21T16:33:48ZPublisher:
BerkmanKleinCenterforInternet&Society.

262 the explanation paradox and the human centric path
-
FilipKarloDošilovic´,MarioBrcˇic´,andNikicaHlupic´.Explainableartificialintelligence: Asurvey.In2018
41stInternationalConventiononInformationandCommunicationTechnology,ElectronicsandMicroelectronics
(MIPRO),pages0210–0215,May2018. doi: 10.23919/MIPRO.2018.8400040.
LaurentDupont,OlivierFliche,andSuYang. GovernanceofArtificialIntelligenceinFinance. Discussion
document,ACPR,June2020.
UpolEhsan,PradyumnaTambwekar,LarryChan,BrentHarrison,andMarkRiedl. AutomatedRationale
Generation: A Technique for Explainable AI and its Effects on Human Perceptions. arXiv:1901.03729
[cs],January2019. URLhttp://arxiv.org/abs/1901.03729. arXiv: 1901.03729.
UpolEhsan,Q.VeraLiao,MichaelMuller,MarkO.Riedl,andJustinD.Weisz. ExpandingExplainability:
TowardsSocialTransparencyinAIsystems. InProceedingsofthe2021CHIConferenceonHumanFactors
in Computing Systems, pages 1–19, Yokohama Japan, May 2021. ACM. ISBN 978-1-4503-8096-6. doi:
10.1145/3411764.3445188. URLhttps://dl.acm.org/doi/10.1145/3411764.3445188.
Malin Eiband, Daniel Buschek, Alexander Kremer, and Heinrich Hussmann. The Impact of Place-
bic Explanations on Trust in Intelligent Systems. In Extended Abstracts of the 2019 CHI Conference
on Human Factors in Computing Systems, CHI EA ’19, pages 1–6, New York, NY, USA, 2019. Asso-
ciation for Computing Machinery. ISBN 978-1-4503-5971-9. doi: 10.1145/3290607.3312787. URL
https://doi.org/10.1145/3290607.3312787.
MalinEiband,DanielBuschek,andHeinrichHussmann. HowtoSupportUsersinUnderstandingIntel-
ligentSystems? StructuringtheDiscussion. In26thInternationalConferenceonIntelligentUserInterfaces,
IUI’21,pages120–132,NewYork,NY,USA,2021.AssociationforComputingMachinery. ISBN978-1-
4503-8017-1. doi: 10.1145/3397481.3450694. URLhttps://doi.org/10.1145/3397481.3450694.
Satu Elo and Helvi Kyngäs. The qualitative content analysis process. Journal of Advanced Nurs-
ing, 62(1):107–115, 2008. ISSN 1365-2648. doi: 10.1111/j.1365-2648.2007.04569.x. URL https:
//onlinelibrary.wiley.com/doi/abs/10.1111/j.1365-2648.2007.04569.x. _eprint:
https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1365-2648.2007.04569.x.
Emmanuel Schizas, Grigory McKain, Bryan Zhang, Altantsetseg Ganbold, Pankajesh Kumar, Hatim
Hussain, Kieran James Garvey, Eva Huang, Alexander Huang, Shaoxin Wang, and Nikos Yerolemou.
The Global RegTech Industry Benchmark Report. Technical report, Cambridge Centre of Alternative
Finance,2019. URLhttps://www.jbs.cam.ac.uk/wp-content/uploads/2020/08/2019-12-ccaf-globa
l-regtech-benchmarking-report.pdf.
European Banking Authority. Guidelines on risk based supervision. Technical report, EBA, November
2016. URL https://www.eba.europa.eu/regulation-and-policy/anti-money-laundering-and-e-m
oney/guidelines-on-risk-based-supervision.
European Commission. Building Trust in Human-Centric Artificial Intelligence. Technical Report
COM(2019) 168 final, August 2019. URL https://digital-strategy.ec.europa.eu/en/library/
communication-building-trust-human-centric-artificial-intelligence.
EuropeanCommission. ProposalforaRegulationoftheEuropeanParliamentandoftheCouncillaying
downHarmonisedRulesonArtificialIntelligenceandamendingcertainUnionLegislativeActs,April
2021. URLhttps://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52021PC0206.
EuropeanCommission. AEuropeanapproachtoartificialintelligence|ShapingEurope’sdigitalfuture,
October2023. URLhttps://digital-strategy.ec.europa.eu/en/policies/european-approach-art
ificial-intelligence.
European Parliament and Council. Regulation (EU) 2016/679 of the European Parliament and of the
Councilof27April2016ontheprotectionofnaturalpersonswithregardtotheprocessingofpersonal
dataandonthefreemovementofsuchdata,andrepealingDirective95/46/EC(GeneralDataProtec-
tion Regulation) (Text with EEA relevance), April 2016. URL http://data.europa.eu/eli/reg/2016/
679/oj/eng. LegislativeBody: EP,CONSIL.

bibliography 263
2019/1150
European Parliament and Council. Regulation (EU) of the European Parliament and of the
Council of 20 June 2019 on promoting fairness and transparency for business users of online interme-
diationservices(TextwithEEArelevance),June2019. URLhttp://data.europa.eu/eli/reg/2019/11
| 50/oj/eng. | LegislativeBody: |     | EP,CONSIL. |     |     |     |     |     |     |
| ---------- | ---------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
2021/784
European Parliament and Council. Regulation (EU) of the European Parliament and of the
Council of 29 April 2021 on addressing the dissemination of terrorist content online (Text with EEA
relevance),April2021.
URLhttp://data.europa.eu/eli/reg/2021/784/oj/eng. LegislativeBody: EP,
CONSIL.
European Parliament and Council. Regulation (EU) 2022/2065 of the European Parliament and of
|     | 19  | 2022 |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
the Council of October on a Single Market For Digital Services and amending Direc-
tive 2000/31/EC (Digital Services Act) (Text with EEA relevance), October 2022. URL http://da
| ta.europa.eu/eli/reg/2022/2065/oj/eng. |     |     |     | LegislativeBody: |     | EP,CONSIL. |     |     |     |
| -------------------------------------- | --- | --- | --- | ---------------- | --- | ---------- | --- | --- | --- |
ChrisEvansandNicolaJ.Gibbons.Theinteractivityeffectinmultimedialearning.Computers&Education,
49(4):1147–1160, 2007. 0360-1315. doi: 10.1016/j.compedu.2006.01.008.
|     | December |     | ISSN |     |     |     |     | URL | https: |
| --- | -------- | --- | ---- | --- | --- | --- | --- | --- | ------ |
//www.sciencedirect.com/science/article/pii/S0360131506000285.
Gregory Falco, Ben Shneiderman, Julia Badger, Ryan Carrier, Anton Dahbura, David Danks, Martin
Eling,AlwynGoodloe,JerryGupta,ChristopherHart,MarinaJirotka,HenricJohnson,CaraLaPointe,
Ashley J. Llorens, Alan K. Mackworth, Carsten Maple, Sigurður Emil Pálsson, Frank Pasquale, Alan
Winfield, and Zee Kin Yeong. Governing AI safety through independent audits. Nature Machine
3(7):566–571, 2021. 2522-5839. doi: 10.1038/s42256-021-00370-7.
| Intelligence, |     | July | ISSN |     |     |     |     | URL | https: |
| ------------- | --- | ---- | ---- | --- | --- | --- | --- | --- | ------ |
//www.nature.com/articles/s42256-021-00370-7. Number: 7Publisher: NaturePublishingGroup.
2006.
Andrea Falcon. Aristotle on Causality. January URL https://plato.stanford.edu/ENTRIES/ari
2023-03-07.
| stotle-causality/. |     | LastModified: |     |     |     |     |     |     |     |
| ------------------ | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Peter Farley. Spotlight On Compliance Costs As Banks Get Down To Business With AI. International
| Banker, | July 2017. URL |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
https://www.bankingexchange.com/bsa-aml/item/8202-cost-of-complianc
Accessed6/15/2020.
e-expected-to-hit-181bn.
MassimoFelici,TheofrastosKoulouris,andSianiPearson. AccountabilityforDataGovernanceinCloud
Ecosystems. In 2013 IEEE 5th International Conference on Cloud Computing Technology and Science, vol-
| 2,  | 327–332, |          |              | 2013. |       | doi: | 10.1109/CloudCom.2013.157. |     |     |
| --- | -------- | -------- | ------------ | ----- | ----- | ---- | -------------------------- | --- | --- |
| ume | pages    | Bristol, | UK, December |       | IEEE. |      |                            |     | URL |
https://ieeexplore.ieee.org/abstract/document/6735445. Accessed12/12/2023.
Shi Feng and Jordan Boyd-Graber. What can AI do for me? evaluating machine learning interpretations
in cooperative play. In Proceedings of the 24th International Conference on Intelligent User Interfaces, IUI
| ’19, | 229–239, |     |     |     | 2019. |     |     |     |     |
| ---- | -------- | --- | --- | --- | ----- | --- | --- | --- | --- |
pages New York, NY, USA, March Association for Computing Machinery. ISBN
978-1-4503-6272-6. doi: 10.1145/3301275.3302265. URLhttps://doi.org/10.1145/3301275.3302265.
|     |     |     |     |     |     |     |     | Proceedings | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
Andrea Ferrario and Michele Loi. How Explainability Contributes to Trust in AI. In
’22, 1457–1466,
the 2022 ACM Conference on Fairness, Accountability, and Transparency, FAccT pages
New York, NY, USA, 2022. Association for Computing Machinery. ISBN 978-1-4503-9352-2. doi:
10.1145/3531146.3533202.
URLhttps://dl.acm.org/doi/10.1145/3531146.3533202.
Andrea Ferrario, Michele Loi, and Eleonora Viganò. In AI We Trust Incrementally: a Multi-layer Model
of Trust to Analyze Human-Artificial Intelligence Interactions. Philosophy & Technology, 33(3):523–539,
|           | 2020. | 2210-5441. | doi: | 10.1007/s13347-019-00378-3. |     |     |                              |     |     |
| --------- | ----- | ---------- | ---- | --------------------------- | --- | --- | ---------------------------- | --- | --- |
| September | ISSN  |            |      |                             |     |     | URL https://doi.org/10.1007/ |     |     |
s13347-019-00378-3.
JulianaJ.FerreiraandMateusS.Monteiro. WhatArePeopleDoingAboutXAIUserExperience? ASur-
vey on AI Explainability Research and Practice. In Aaron Marcus and Elizabeth Rosenzweig, editors,
Design,UserExperience,andUsability.DesignforContemporaryInteractiveEnvironments,LectureNotesin
ComputerScience,pages56–73,Cham,2020.SpringerInternationalPublishing. ISBN978-3-030-49760-
6.

264 the explanation paradox and the human centric path
-
Financial Action Task Force. Guidance on the risk-based approach to combating money-laundering and
terrorist financing. Technical report, FATF, June 2007. URL https://www.fatf-gafi.org/en/publica
tions/Fatfrecommendations/Fatfguidanceontherisk-basedapproachtocombatingmoneylaundering
andterroristfinancing-highlevelprinciplesandprocedures.html. Accessed12/2/2023.
FinancialActionTaskForce.Risk-BasedApproachfortheBankingSector.Technicalreport,FATF,October
2014. URL https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Risk-based-appro
ach-banking-sector.html. Accessed12/02/2023.
FinancialConductAuthority. MachinelearninginUKfinancialservices. Technicalreport,FCA,Bankof
England, October 2019. URL https://www.bankofengland.co.uk/-/media/boe/files/report/2019/
machine-learning-in-uk-financial-services.pdf.
Financial Conduct Authority. Artificial Intelligence and Machine Learning. Technical Report DP-5-22,
FCA, Bank of England, October 2022. URL https://www.bankofengland.co.uk/-/media/boe/files/
prudential-regulation/publication/2022/dp5-22--artificial-intelligence-and-machine-learn
ing.pdf.
Financial Stability Board. Artificial intelligence and machine learning in financial services. Technical
report,FSB,January2017. URLhttps://www.fsb.org/wp-content/uploads/P011117.pdf.
James D. Foley, Foley Dan Van, Andries Van Dam, Steven K. Feiner, and John F. Hughes. Computer
Graphics: PrinciplesandPractice. Addison-WesleyProfessional,1996. ISBN978-0-201-84840-3.
Sebastian Fritz-Morgenthal, Bernhard Hein, and Jochen Papenbrock. Financial Risk Management and
Explainable,Trustworthy,ResponsibleAI. FrontiersinArtificialIntelligence,5:14,2022. ISSN2624-8212.
URLhttps://www.frontiersin.org/articles/10.3389/frai.2022.779799.
JohannesFürnkranz,TomášKliegr,andHeikoPaulheim. Oncognitivepreferencesandtheplausibilityof
rule-basedmodels. MachineLearning,109(4):853–898,April2020. ISSN1573-0565. doi: 10.1007/s10994-
019-05856-5. URLhttps://doi.org/10.1007/s10994-019-05856-5.
KrzysztofZ.GajosandLenaMamykina. DoPeopleEngageCognitivelywithAI?ImpactofAIAssistance
on Incidental Learning. In 27thInternationalConferenceonIntelligentUserInterfaces, IUI ’22, pages 794–
806,NewYork,NY,USA,March2022.AssociationforComputingMachinery. ISBN978-1-4503-9144-3.
doi: 10.1145/3490099.3511138. URLhttps://doi.org/10.1145/3490099.3511138.
Bill Gaver and Heather Martin. Alternatives: exploring information appliances through conceptual de-
signproposals. InProceedingsoftheSIGCHIconferenceonHumanFactorsinComputingSystems,CHI’00,
pages 209–216, New York, NY, USA, 2000. Association for Computing Machinery. ISBN 978-1-58113-
216-8. doi: 10.1145/332040.332433. URLhttps://dl.acm.org/doi/10.1145/332040.332433.
BertramGawronski.Theory-basedbiascorrectionindispositionalinference: Thefundamentalattribution
error is dead, long live the correspondence bias. European Review of Social Psychology, 15(1):183–217,
January 2004. ISSN 1046-3283. doi: 10.1080/10463280440000026. URL https://doi.org/10.1080/10
463280440000026.
Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal
Daumé III, and Kate Crawford. Datasheets for Datasets, December 2021. URL http://arxiv.org/ab
s/1803.09010. arXiv:1803.09010[cs].
Julie Gerlings and Ioanna Constantiou. Machine Learning in Transaction Monitoring: The Prospect of
xAI,December2022. URLhttp://arxiv.org/abs/2210.07648. arXiv:2210.07648[cs].
Zoubin Ghahramani. Unsupervised Learning. In Olivier Bousquet, Ulrike von Luxburg, and Gun-
nar Rätsch, editors, Advanced Lectures on Machine Learning: ML Summer Schools 2003, Revised Lectures,
LectureNotesinComputerScience,pages72–112.Springer,Berlin,Heidelberg,2004. ISBN978-3-540-
28650-9. URLhttps://doi.org/10.1007/978-3-540-28650-9_5.

bibliography 265
Bhavya Ghai, Q. Vera Liao, Yunfeng Zhang, Rachel Bellamy, and Klaus Mueller. Explainable Active
Learning (XAL): Toward AI Explanations as Interfaces for Machine Teachers. Proceedings of the ACM
onHuman-ComputerInteraction, 4(CSCW3):1–28, January 2021. ISSN 2573-0142. doi: 10.1145/3432934.
URLhttps://dl.acm.org/doi/10.1145/3432934.
AsmaGhandeharioun,BeenKim,Chun-LiangLi,BrendanJou,BrianEoff,andRosalindW.Picard. DIS-
SECT:DisentangledSimultaneousExplanationsviaConceptTraversals. arXiv:2105.15164[cs],February
2022. URLhttp://arxiv.org/abs/2105.15164. arXiv: 2105.15164.
MarzyehGhassemi,LukeOakden-Rayner,andAndrewLBeam. Thefalsehopeofcurrentapproachesto
explainable artificial intelligence in health care. The Lancet Digital Health, 3(11):e745–e750, November
2021. ISSN2589-7500. doi: 10.1016/S2589-7500(21)00208-9. URLhttps://www.sciencedirect.com/sc
ience/article/pii/S2589750021002089.
Azin Ghazimatin, Soumajit Pramanik, Rishiraj Saha Roy, and Gerhard Weikum. ELIXIR: Learning from
UserFeedbackonExplanationstoImproveRecommenderModels. InProceedingsoftheWebConference
2021, WWW ’21, pages 3850–3860, New York, NY, USA, 2021. Association for Computing Machinery.
ISBN 978-1-4503-8312-7. doi: 10.1145/3442381.3449848. URL https://doi.org/10.1145/3442381.34
49848.
Gerd Gigerenzer. TheIntelligenceofIntuition. Cambridge University Press, October 2023. ISBN 978-1-00-
930490-0. Google-Books-ID:7IHZEAAAQBAJ.
L. H. Gilpin, D. Bau, B. Z. Yuan, A. Bajwa, M. Specter, and L. Kagal. Explaining Explanations:
An Overview of Interpretability of Machine Learning. In 2018 IEEE 5th International Conference on
Data Science and Advanced Analytics (DSAA), pages 80–89, Turin, Italy, October 2018. IEEE. doi:
10.1109/DSAA.2018.00018.
Ella Glikson and Anita Williams Woolley. Human Trust in Artificial Intelligence: Review of Empirical
Research. Academy of Management Annals, 14(2):627–660, July 2020. ISSN 1941-6520. doi: 10.5465/an-
nals.2018.0057. URL https://journals.aom.org/doi/10.5465/annals.2018.0057. Publisher:
AcademyofManagement.
Dale L. Goodhue and Ronald L. Thompson. Task-Technology Fit and Individual Performance. MIS
Quarterly,19(2):213–236,1995. ISSN0276-7783. doi: 10.2307/249689. URLhttps://www.jstor.org/st
able/249689. Publisher: ManagementInformationSystemsResearchCenter,UniversityofMinnesota.
Dimitrios Goranitis and Meral Cailali. Global fines for AML/CFT related issues increase in 2022. Tech-
nicalreport,Deloitte,February2023.
Maartje M. A. de Graaf and Bertram F. Malle. How People Explain Action (and Autonomous Intelligent
Systems Should Too). In 2017 AAAI Fall Symposium Series, page 8, Arlington, Virginia, October 2017.
AAAI. URLhttps://www.aaai.org/ocs/index.php/FSS/FSS17/paper/view/16009.
ColinM.Gray,YuboKou,BryanBattles,JosephHoggatt,andAustinL.Toombs. TheDark(Patterns)Side
ofUXDesign. InProceedingsofthe2018CHIConferenceonHumanFactorsinComputingSystems,CHI’18,
pages1–14,NewYork,NY,USA,2018.AssociationforComputingMachinery. ISBN978-1-4503-5620-6.
doi: 10.1145/3173574.3174108. URLhttps://dl.acm.org/doi/10.1145/3173574.3174108.
Ben Green and Yiling Chen. The Principles and Limits of Algorithm-in-the-Loop Decision Making.
Proceedings of the ACM on Human-Computer Interaction, 3(CSCW):50:1–50:24, November 2019. doi:
10.1145/3359152. URLhttps://doi.org/10.1145/3359152.
H. P. Grice. LogicandConversation. Brill, December 1975. ISBN 978-90-04-36881-1. URL https://brill.
com/view/book/edcoll/9789004368811/BP000003.xml. Pages: 41-58Section: SpeechActs.
G.MarkGrimes,RyanM.Schuetzler,andJustinScottGiboney. Mentalmodelsandexpectationviolations
inconversationalAIinteractions. DecisionSupportSystems,144:113515,May2021. ISSN0167-9236. doi:
10.1016/j.dss.2021.113515. URL https://www.sciencedirect.com/science/article/pii/S016792362
1000257.

| 266 | the explanation | paradox | and | the human | centric | path |     |     |
| --- | --------------- | ------- | --- | --------- | ------- | ---- | --- | --- |
-
RobGruppetta. Usingartificialintelligencetokeepcriminalfundsoutofthefinancialsystem,December
2017. URL https://www.fca.org.uk/news/speeches/using-artificial-intelligence-keep-crimi
nal-funds-out-financial-system.
Ziwei Gu, Jing Nathan Yan, and Jeffrey M. Rzeszotarski. Understanding User Sensemaking in Machine
Learning Fairness Assessment Systems. In Proceedings of the Web Conference 2021, WWW ’21, pages
658–668, New York, NY, USA, 2021. Association for Computing Machinery. ISBN 978-1-4503-8312-7.
doi: 10.1145/3442381.3450092.
URLhttps://doi.org/10.1145/3442381.3450092.
Riccardo Guidotti, Anna Monreale, Salvatore Ruggieri, Franco Turini, Fosca Giannotti, and Dino Pe-
dreschi. A Survey of Methods for Explaining Black Box Models. ACM Computing Surveys, 51(5):93:1–
| 93:42,August2018. |     | ISSN0360-0300. | doi: | 10.1145/3236009. |     |     |     |     |
| ----------------- | --- | -------------- | ---- | ---------------- | --- | --- | --- | --- |
URLhttps://doi.org/10.1145/3236009.
DavidGunningandDavidAha.DARPA’sExplainableArtificialIntelligence(XAI)Program.AIMagazine,
40(2):44–58, June 2019. ISSN 2371-9621. doi: 10.1609/aimag.v40i2.2850. URL
https://www.aaai.org
2.
| /ojs/index.php/aimagazine/article/view/2850. |     |     |     | Number: |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- |
Neil Gunningham and Darren Sinclair. Organizational Trust and the Limits of Management-Based
Regulation. Law & Society Review, 43(4):865–900, 2009. ISSN 1540-5893. doi: 10.1111/j.1540-
5893.2009.00391.x.
URL https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-5893.20
09.00391.x. _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1540-5893.2009.00391.x.
LijieGuo,ElizabethM.Daly,OznurAlkan,MassimilianoMattetti,OwenCornec,andBartKnijnenburg.
Building Trust in Interactive Machine Learning via User Contributed Interpretable Rules. In 27th
InternationalConferenceonIntelligentUserInterfaces,IUI’22,pages537–548,NewYork,NY,USA,March
| 2022. |             |               |            | 978-1-4503-9144-3. |     | doi: | 10.1145/3490099.3511111. |     |
| ----- | ----------- | ------------- | ---------- | ------------------ | --- | ---- | ------------------------ | --- |
|       | Association | for Computing | Machinery. | ISBN               |     |      |                          |     |
URLhttps://doi.org/10.1145/3490099.3511111.
RuochengGuo,LuCheng,JundongLi,P.RichardHahn,andHuanLiu. ASurveyofLearningCausality
|     |     |     |     |     | 53(4):1–37, |     | 2021. | 0360-0300, |
| --- | --- | --- | --- | --- | ----------- | --- | ----- | ---------- |
with Data: Problems and Methods. ACM Computing Surveys, July ISSN
| 1557-7341. | doi: | 10.1145/3397269. |     |     |     |     |     |     |
| ---------- | ---- | ---------------- | --- | --- | --- | --- | --- | --- |
URLhttps://dl.acm.org/doi/10.1145/3397269.
Abhishek Gupta, Dwijendra Nath Dwivedi, and Jigar Shah. Artificial Intelligence Applications in Banking
|     |     |     |     |     |     |     | 2023. | 978- |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- |
and Financial Services: Anti Money Laundering and Compliance. Springer Nature, July ISBN
| 981-9925-71-1. |     | Google-Books-ID:c2LMEAAAQBAJ. |     |     |     |     |     |     |
| -------------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
Christos Hadjiemmanuil. A Heavily Regulated Industry: The Varied Objectives of Financial Regulation,
December2015.
URLhttps://papers.ssrn.com/abstract=2733062.
Joseph Y. Halpern and Judea Pearl. Causes and Explanations: A Structural-Model Approach. Part I:
Causes. The British Journal for the Philosophy of Science, 56(4):843–887, December 2005. ISSN 0007-0882.
doi: 10.1093/bjps/axi147.
URL https://www.journals.uchicago.edu/doi/10.1093/bjps/axi147.
| Publisher: | TheUniversityofChicagoPress. |     |     |     |     |     |     |     |
| ---------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Ronan Hamon, Henrik Junklewitz, and Ignacio Sanchez. Robustness and Explainability of Artificial
JRCTechnicalReportEUR30040EN,EuropeanCommissionJointResearchCenter,2020.
Intelligence.
Ronan Hamon, Henrik Junklewitz, Ignacio Sanchez, Gianclaudio Malgieri, and Paul De Hert. Bridging
the Gap Between AI and Explainability in the GDPR: Towards Trustworthiness-by-Design in Auto-
|     |     |     |     |     |     | 17(1):72–85, |     | 2022. |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ----- |
mated Decision-Making. IEEE Computational Intelligence Magazine, February ISSN
| 1556-6048. | doi: | 10.1109/MCI.2021.3129960. |     |                 |                                   |     |     |     |
| ---------- | ---- | ------------------------- | --- | --------------- | --------------------------------- | --- | --- | --- |
|            |      |                           |     | ConferenceName: | IEEEComputationalIntelligenceMag- |     |     |     |
azine.
Polity,April2006. ISBN978-0-7456-2465-5. Google-Books-ID:XWwpRhX1tdsC.
| RussellHardin. |     | Trust. |     |     |     |     |              |       |
| -------------- | --- | ------ | --- | --- | --- | --- | ------------ | ----- |
|                |     |        |     |     |     |     | 74(1):88–95, | 1965. |
Gilbert H. Harman. The Inference to the Best Explanation. The Philosophical Review,
ISSN 0031-8108. doi: 10.2307/2183532. URL https://www.jstor.org/stable/2183532. Publisher:
[DukeUniversityPress,PhilosophicalReview].

|     |     |     |     |     |     |     |     | bibliography | 267 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
PeterHedströmandPetriYlikoski. CausalMechanismsintheSocialSciences. AnnualReviewofSociology,
36(1):49–67,2010. doi: 10.1146/annurev.soc.012809.102632. URLhttps://doi.org/10.1146/annurev.
soc.012809.102632. _eprint: https://doi.org/10.1146/annurev.soc.012809.102632.
Clément Henin and Daniel Le Métayer. Beyond explainability: justifiability and contestability of algo-
|         |                   |     |               | 37(4):1397–1410, |     |          | 2022. | 1435-5655. | doi: |
| ------- | ----------------- | --- | ------------- | ---------------- | --- | -------- | ----- | ---------- | ---- |
| rithmic | decision systems. |     | AI & SOCIETY, |                  |     | December |       | ISSN       |      |
10.1007/s00146-021-01251-8. URLhttps://doi.org/10.1007/s00146-021-01251-8.
Sam Hepenstal, Leishi Zhang, Neesha Kodagoda, and B. l. william Wong. Developing Conversational
|          |            |          |                 | ACM        | Transactions          | on Interactive |     | Intelligent Systems, | 11(3-4): |
| -------- | ---------- | -------- | --------------- | ---------- | --------------------- | -------------- | --- | -------------------- | -------- |
| Agents   | for Use in | Criminal | Investigations. |            |                       |                |     |                      |          |
| 1–35,    | 2021.      |          | 2160-6455,      | 2160-6463. | doi: 10.1145/3444369. |                |     |                      |          |
| December |            | ISSN     |                 |            |                       |                | URL | https://dl.acm.org/d |          |
oi/10.1145/3444369.
Bernease Herman. The Promise and Peril of Human Evaluation for Model Interpretability.
| arXiv:1711.07414[cs,stat],October2019. |     |     |     |                                     |     |     |     | 1711.07414. |     |
| -------------------------------------- | --- | --- | --- | ----------------------------------- | --- | --- | --- | ----------- | --- |
|                                        |     |     |     | URLhttp://arxiv.org/abs/1711.07414. |     |     |     | arXiv:      |     |
DianaC.Hernandez-BocanegraandJürgenZiegler.Conversationalreview-basedexplanationsforrecom-
mender systems: Exploring users’ query behavior. In CUI 2021 - 3rd Conference on Conversational User
Interfaces,CUI’21,pages1–11,NewYork,NY,USA,2021.AssociationforComputingMachinery. ISBN
| 978-1-4503-8998-3. |     | doi: 10.1145/3469595.3469596. |     |     |     |     |     |     |     |
| ------------------ | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
URLhttps://doi.org/10.1145/3469595.3469596.
Scarlett R. Herring, Chia-Chen Chang, Jesse Krantzler, and Brian P. Bailey. Getting inspired! under-
standing how and why examples are used in creative design practice. In Proceedings of the SIGCHI
Conference on Human Factors in Computing Systems, CHI ’09, pages 87–96, New York, NY, USA, 2009.
|             |               |     |            |      | 978-1-60558-246-7. | doi: | 10.1145/1518701.1518717. |     |     |
| ----------- | ------------- | --- | ---------- | ---- | ------------------ | ---- | ------------------------ | --- | --- |
| Association | for Computing |     | Machinery. | ISBN |                    |      |                          |     | URL |
https://doi.org/10.1145/1518701.1518717.
AIandEthics,2(1):219–225,
ChristianHerzog. Ontheriskofconfusinginterpretabilitywithexplicability.
February2022. ISSN2730-5961. doi: 10.1007/s43681-021-00121-9. URLhttps://doi.org/10.1007/s4
3681-021-00121-9.
GermundHesslow. TheProblemofCausalSelection. InDenisJ.Hilton,editor,ContemporaryScienceand
NaturalExplanation: CommonsenseConceptionsofCausality.NewYorkUniversityPress,1988.
High-LevelExpertGrouponAI(HLEG). AdefinitionofAI:MainCapabilitiesandScientificDisciplines.
Technicalreport,EuropeanCommission,Brussels,December2018.
High-LevelExpertGrouponAI(HLEG). EthicsguidelinesfortrustworthyAI|ShapingEurope’sdigital
Technicalreport,EuropeanCommission,April2019.
| future. |     |     |     |     |     | URLhttps://digital-strategy.ec.eur |     |     |     |
| ------- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- |
opa.eu/en/library/ethics-guidelines-trustworthy-ai.
Mireille Hildebrandt. Privacy as Protection of the Incomputable Self: From Agnostic to Agonistic
Machine Learning. Theoretical Inquiries in Law, 20(1):83–121, January 2019. ISSN 1565-3404. doi:
10.1515/til-2019-0004.
URL https://www.degruyter.com/document/doi/10.1515/til-2019-0004/ht
| ml. Publisher: | DeGruyter. |     |     |     |     |     |     |     |     |
| -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
DenisJ.Hilton. Logicandcausalattribution. InContemporaryscienceandnaturalexplanation: Commonsense
conceptionsofcausality, pages33–65.NewYork NY,US,1988. ISBN978-0-
|     |     |     |     |     | UniversityPress, | NewYork, |     |     |     |
| --- | --- | --- | --- | --- | ---------------- | -------- | --- | --- | --- |
8147-3443-8.
DenisJ.HiltonandBenR.Slugoski. Knowledge-basedcausalattribution: Theabnormalconditionsfocus
model. PsychologicalReview,93(1):75–88,1986. ISSN1939-1471. doi: 10.1037/0033-295X.93.1.75. Place:
| USPublisher: | AmericanPsychologicalAssociation. |     |     |     |     |     |     |     |     |
| ------------ | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
XRDS:Crossroads,TheACMMagazineforStudents,25(3):16–19,
| MichaelHind.         | ExplainingexplainableAI. |      |                  |     |     |     |     |     |     |
| -------------------- | ------------------------ | ---- | ---------------- | --- | --- | --- | --- | --- | --- |
| 2019. ISSN1528-4972. |                          | doi: | 10.1145/3313096. |     |     |     |     |     |     |
URLhttps://doi.org/10.1145/3313096.
9(8):1735–
Sepp Hochreiter and Jürgen Schmidhuber. Long Short-Term Memory. Neural Computation,
1780, November 1997. ISSN 0899-7667. doi: 10.1162/neco.1997.9.8.1735. URL https://ieeexplore.i
eee.org/abstract/document/6795963. ConferenceName: NeuralComputation.

268 the explanation paradox and the human centric path
-
Marit Hoegen, Hilko van Rooijen, and Maarten Rijssenbeek. Three fundamental changes to the Dutch
AML system, 2023. URL https://www2.deloitte.com/nl/nl/pages/finance/articles/three-funda
mental-changes-to-the-dutch-aml-system.html.
Robert R. Hoffman, Shane T. Mueller, Gary Klein, and Jordan Litman. Metrics for Explainable AI: Chal-
lenges and Prospects, February 2019. URL http://arxiv.org/abs/1812.04608. arXiv:1812.04608
[cs].
Fred Hohman, Andrew Head, Rich Caruana, Robert DeLine, and Steven M. Drucker. Gamut: A Design
ProbetoUnderstandHowDataScientistsUnderstandMachineLearningModels. InProceedingsofthe
2019 CHI Conference on Human Factors in Computing Systems, pages 1–13, Glasgow Scotland Uk, May
2019.ACM. ISBN978-1-4503-5970-2. doi: 10.1145/3290605.3300809. URLhttps://dl.acm.org/doi/1
0.1145/3290605.3300809.
Andreas Holzinger, Georg Langs, Helmut Denk, Kurt Zatloukal, and Heimo Müller. Causability and
explainability of artificial intelligence in medicine. WIREs Data Mining and Knowledge Discovery, 9(4):
e1312, 2019. ISSN 1942-4795. doi: 10.1002/widm.1312. URL https://onlinelibrary.wiley.com/do
i/abs/10.1002/widm.1312. _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/widm.1312.
Andreas Holzinger, André Carrington, and Heimo Müller. Measuring the Quality of Explanations: The
System Causability Scale (SCS). KI - Künstliche Intelligenz, 34(2):193–198, June 2020. ISSN 1610-1987.
doi: 10.1007/s13218-020-00636-z. URLhttps://doi.org/10.1007/s13218-020-00636-z.
Andreas Holzinger, Bernd Malle, Anna Saranti, and Bastian Pfeifer. Towards multi-modal causability
with Graph Neural Networks enabling information fusion for explainable AI. Information Fusion, 71:
28–37, July 2021. ISSN 1566-2535. doi: 10.1016/j.inffus.2021.01.008. URL https://www.sciencedirec
t.com/science/article/pii/S1566253521000142.
SamuelHuron. ConstructiveVisualization: Atoken-basedparadigmallowingtoassembledynamicvisualrepre-
sentationfornon-experts. Thesededoctorat,Paris11,September2014. URLhttps://www.theses.fr/20
14PA112253.
Johan Huysmans, Karel Dejaeger, Christophe Mues, Jan Vanthienen, and Bart Baesens. An empirical
evaluation of the comprehensibility of decision table, tree and rule based predictive models. Decision
Support Systems, 51(1):141–154, April 2011. ISSN 0167-9236. doi: 10.1016/j.dss.2010.12.003. URL
https://www.sciencedirect.com/science/article/pii/S0167923610002368.
InternationalOrganizationforStandardization(ISO). Ergonomicsofhuman-systeminteractionHuman-
centreddesignforinteractivesystems.
International Organization for Standardization (ISO). Artificial Overview of trustworthiness in artificial
intelligence,January2022. URLhttps://www.iso.org/standard/77608.html.
Maia Jacobs, Jeffrey He, Melanie F. Pradier, Barbara Lam, Andrew C. Ahn, Thomas H. McCoy, Roy H.
Perlis, Finale Doshi-Velez, and Krzysztof Z. Gajos. Designing AI for Trust and Collaboration in Time-
Constrained Medical Decisions: A Sociotechnical Lens. In Proceedings of the 2021 CHI Conference on
HumanFactorsinComputingSystems,pages1–14,YokohamaJapan,May2021.ACM. ISBN978-1-4503-
8096-6. doi: 10.1145/3411764.3445385. URLhttps://dl.acm.org/doi/10.1145/3411764.3445385.
AlonJacovi,AnaMarasovic´,TimMiller,andYoavGoldberg. FormalizingTrustinArtificialIntelligence:
Prerequisites, Causes and Goals of Human Trust in AI. In Proceedings of the 2021 ACM Conference on
Fairness, Accountability, and Transparency, FAccT ’21, pages 624–635, New York, NY, USA, March 2021.
Association for Computing Machinery. ISBN 978-1-4503-8309-7. doi: 10.1145/3442188.3445923. URL
https://dl.acm.org/doi/10.1145/3442188.3445923.
Lars-Erik Janlert and Erik Stolterman. The Meaning of Interactivity—Some Proposals for Defini-
tions and Measures. Human–Computer Interaction, 32(3):103–138, May 2017. ISSN 0737-0024. doi:
10.1080/07370024.2016.1226139. URL https://doi.org/10.1080/07370024.2016.1226139. Publisher:
Taylor&Francis_eprint: https://doi.org/10.1080/07370024.2016.1226139.

|     |     |     |     |     |     |     |     | bibliography | 269 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |
ShichaoJia,ZeyuLi,NuoChen,andJiawanZhang.TowardsVisualExplainableActiveLearningforZero-
Shot Classification. IEEE Transactions on Visualization and Computer Graphics, 28(1):791–801, January
| 2022. ISSN1941-0506. |     | doi: | 10.1109/TVCG.2021.3114793. |     |     |     |     |     |     |
| -------------------- | --- | ---- | -------------------------- | --- | --- | --- | --- | --- | --- |
ZhuochenJin,ShuyuanCui,ShunanGuo,DavidGotz,JimengSun,andNanCao.CarePre: AnIntelligent
ACMTransactionsonComputingforHealthcare,1(1):6:1–6:20,March
ClinicalDecisionAssistanceSystem.
2020. ISSN2691-1957. doi: 10.1145/3344258. URLhttps://doi.org/10.1145/3344258.
2018.
Joanna Bryson. AI & Global Governance: No One Should Trust AI, November URL https:
//unu.edu/cpr/blog-post/ai-global-governance-no-one-should-trust-ai. Accessed1/22/2024.
Anna Jobin, Marcello Ienca, and Effy Vayena. The global landscape of AI ethics guidelines. Nature
Machine Intelligence, 1(9):389–399, September 2019. ISSN 2522-5839. doi: 10.1038/s42256-019-0088-
| 2.  |     |     |     |     |     |     |     | 9   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
URL https://www.nature.com/articles/s42256-019-0088-2. Number: Publisher: Nature
PublishingGroup.
Patrick W. Jordan, B. Thomas, Ian Lyall McClelland, and Bernard Weerdmeester. Usability Evaluation In
Industry. CRCPress,June1996. ISBN978-1-4987-1041-1. Google-Books-ID:ujFRDwAAQBAJ.
M. Jullum, A. Løland, R.B. Huseby, G. Ånonsen, and J. Lorentzen. Detecting money laundering
|              |      |         |           |         |          |            |          | 23(1):173–186, | 2020. doi: |
| ------------ | ---- | ------- | --------- | ------- | -------- | ---------- | -------- | -------------- | ---------- |
| transactions | with | machine | learning. | Journal | of Money | Laundering | Control, |                |            |
10.1108/JMLC-07-2019-0055.
DanielKahneman. Thinking,fastandslow. Thinking,fastandslow.Farrar,StrausandGiroux,NewYork,
| NY,US,2011. | ISBN978-0-374-27563-1978-1-4299-6935-2. |     |     |     |     | Pages: | 499. |     |     |
| ----------- | --------------------------------------- | --- | --- | --- | --- | ------ | ---- | --- | --- |
DanielKahnemanandGaryKlein. Conditionsforintuitiveexpertise: Afailuretodisagree. AmericanPsy-
| chologist,64(6):515–526,2009. |     |     | ISSN1935-990X. |     | doi: 10.1037/a0016755. |     |        |              |          |
| ----------------------------- | --- | --- | -------------- | --- | ---------------------- | --- | ------ | ------------ | -------- |
|                               |     |     |                |     |                        |     | Place: | USPublisher: | American |
PsychologicalAssociation.
Daniel Kahneman and Amos Tversky. Prospect Theory: An Analysis of Decision under Risk. Economet-
rica, 47(2):263–291, 1979. ISSN 0012-9682. doi: 10.2307/1914185. URL https://www.jstor.org/stab
| le/1914185. | Publisher: |     | [Wiley,EconometricSociety]. |     |     |     |     |     |     |
| ----------- | ---------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
Daniel Kahneman, Stewart Paul Slovic, Paul Slovic, Amos Tversky, and Cambridge University Press.
|                           |                               |     |                      |     | CambridgeUniversityPress,April1982. |     |     |     | ISBN978-0- |
| ------------------------- | ----------------------------- | --- | -------------------- | --- | ----------------------------------- | --- | --- | --- | ---------- |
| JudgmentUnderUncertainty: |                               |     | HeuristicsandBiases. |     |                                     |     |     |     |            |
| 521-28414-1.              | Google-Books-ID:_0H8gwj4a1MC. |     |                      |     |                                     |     |     |     |            |
2021.
Margot E. Kaminski and Jennifer M. Urban. The Right to Contest AI, November URL https:
//papers.ssrn.com/abstract=3965041.
KatrinaZhu. TheStateofStateAILaws: 2023,August2023. URLhttps://epic.org/the-state-of-sta
te-ai-laws-2023/.
Davinder Kaur, Suleyman Uslu, Kaley J. Rittichier, and Arjan Durresi. Trustworthy Artificial Intelli-
|                  |         |                                            |           |          | 55(2):39:1–39:38, |     | 2022.   | 0360-0300. | doi: |
| ---------------- | ------- | ------------------------------------------ | --------- | -------- | ----------------- | --- | ------- | ---------- | ---- |
| gence: A         | Review. | ACM                                        | Computing | Surveys, |                   |     | January | ISSN       |      |
| 10.1145/3491209. |         | URLhttps://dl.acm.org/doi/10.1145/3491209. |           |          |                   |     |         |            |      |
Harmanpreet Kaur, Harsha Nori, Samuel Jenkins, Rich Caruana, Hanna Wallach, and Jennifer Wort-
man Vaughan. Interpreting Interpretability: Understanding Data Scientists’ Use of Interpretability
Tools for Machine Learning. In Proceedings of the 2020 CHI Conference on Human Factors in Computing
Systems, pages 1–14, New York, NY, USA, April 2020. Association for Computing Machinery. ISBN
| 978-1-4503-6708-0. |     | URLhttps://doi.org/10.1145/3313831.3376219. |     |     |     |     |     |     |     |
| ------------------ | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
D.A. Keim. Information visualization and visual data mining. IEEE Transactions on Visualization and
|          |           | 8(1):1–8, |         | 2002. | 1941-0506. | doi: | 10.1109/2945.981847. |     |            |
| -------- | --------- | --------- | ------- | ----- | ---------- | ---- | -------------------- | --- | ---------- |
| Computer | Graphics, |           | January |       | ISSN       |      |                      |     | Conference |
Name: IEEETransactionsonVisualizationandComputerGraphics.
CarmelKent,EstherLaslo,andSheizafRafaeli.Interactivityinonlinediscussionsandlearningoutcomes.
Computers & Education, 97:116–128, June 2016. ISSN 0360-1315. doi: 10.1016/j.compedu.2016.03.002.
URLhttps://www.sciencedirect.com/science/article/pii/S0360131516300537.

270 the explanation paradox and the human centric path
-
Pranav Khadpe, Ranjay Krishna, Li Fei-Fei, Jeffrey T. Hancock, and Michael S. Bernstein. Conceptual
MetaphorsImpactPerceptionsofHuman-AICollaboration. ProceedingsoftheACMonHuman-Computer
Interaction, 4(CSCW2):163:1–163:26, October2020. doi: 10.1145/3415234. URLhttps://dl.acm.org/d
oi/10.1145/3415234.
Anjali Khurana, Parsa Alamzadeh, and Parmit K. Chilana. ChatrEx: Designing Explainable Chat-
bot Interfaces for Enhancing Usefulness, Transparency, and Trust. In 2021 IEEE Symposium
on Visual Languages and Human-Centric Computing (VL/HCC), pages 1–11, October 2021. doi:
10.1109/VL/HCC51201.2021.9576440. ISSN:1943-6106.
Been Kim, Elena Glassman, Brittney Johnson, and Julie Shah. iBCM: Interactive Bayesian Case Model
Empowering Humans via Intuitive Interaction. April 2015. URL https://dspace.mit.edu/handle/17
21.1/96315. Accepted: 2015-04-01T17:30:03Z.
Been Kim, Rajiv Khanna, and Oluwasanmi O Koyejo. Examples are not enough, learn to criticize! Criti-
cismforInterpretability. InAdvancesinNeuralInformationProcessingSystems,volume29.CurranAsso-
ciates, Inc., 2016. URL https://papers.nips.cc/paper/2016/hash/5680522b8e2bb01943234bce7bf84
534-Abstract.html.
Been Kim, Martin Wattenberg, Justin Gilmer, Carrie Cai, James Wexler, Fernanda Viegas, and Rory
Sayres. Interpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation
Vectors(TCAV). InProceedingsofthe35thInternationalConferenceonMachineLearning,pages2668–2677.
PMLR,July2018. URLhttps://proceedings.mlr.press/v80/kim18d.html. ISSN:2640-3498.
Sunnie S. Y. Kim, Elizabeth Anne Watkins, Olga Russakovsky, Ruth Fong, and Andrés Monroy-
Hernández. "Help Me Help the AI": Understanding How Explainability Can Support Human-AI
Interaction. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems, CHI ’23,
pages1–17,NewYork,NY,USA,2023.AssociationforComputingMachinery. ISBN978-1-4503-9421-5.
doi: 10.1145/3544548.3581001. URLhttps://dl.acm.org/doi/10.1145/3544548.3581001.
Taenyun Kim and Hayeon Song. The Effect of Message Framing and Timing on the Acceptance of
Artificial Intelligence’s Suggestion. In Extended Abstracts of the 2020 CHI Conference on Human Factors
in Computing Systems, CHI EA ’20, pages 1–8, New York, NY, USA, 2020. Association for Computing
Machinery. ISBN 978-1-4503-6819-3. doi: 10.1145/3334480.3383038. URL https://doi.org/10.1145/
3334480.3383038.
Kim,Chris,Lin,Xiao,Collins,Christopher,Taylor,GrahamW,andAmer,MohamedR. Learn,Generate,
Rank,Explain: ACaseStudyofVisualExplanationbyGenerativeMachineLearning. ACMTransactions
on Interactive Intelligent Systems (TiiS), August 2021. doi: 10.1145/3465407. URL https://dl.acm.org
/doi/abs/10.1145/3465407. Publisher: ACMPUB27NewYork,NY.
Pieter-Jan Kindermans, Sara Hooker, Julius Adebayo, Maximilian Alber, Kristof T. Schütt, Sven Dähne,
Dumitru Erhan, and Been Kim. The (Un)reliability of saliency methods, November 2017. URL http:
//arxiv.org/abs/1711.00867. arXiv:1711.00867[cs,stat].
Alexandra Kirsch. Explain to whom? Putting the User in the Center of Explainable AI. In Proceedings
of the First International Workshop on Comprehensibility and Explanation in AI and ML 2017 co-located with
16thInternationalConferenceoftheItalianAssociationforArtificialIntelligence(AI*IA2017),Bari,Italy,2017.
URLhttps://hal.archives-ouvertes.fr/hal-01845135.
René F. Kizilcec. How Much Information? Effects of Transparency on Trust in an Algorithmic Interface.
In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, CHI ’16, pages 2390–
2395, New York, NY, USA, May 2016. Association for Computing Machinery. ISBN 978-1-4503-3362-7.
doi: 10.1145/2858036.2858402. URLhttps://doi.org/10.1145/2858036.2858402.
PaulA.Klaczynski,DavidH.Gordon,andJamesFauth. Goal-orientedcriticalreasoningandindividual
differences in critical reasoning biases. Journal of Educational Psychology, 89(3):470–485, 1997. ISSN
1939-2176. doi: 10.1037/0022-0663.89.3.470. Place: USPublisher: AmericanPsychologicalAssociation.

bibliography 271
Gary A. Klein. Sources of Power: How People Make Decisions. Nature, 1988. ISBN 978-0-262-53429-1.
Google-Books-ID:JW01DwAAQBAJ.
Tomáš Kliegr, Šteˇpán Bahník, and Johannes Fürnkranz. A review of possible effects of cognitive biases
on interpretation of rule-based machine learning models. Artificial Intelligence, 295:103458, June 2021.
ISSN0004-3702. doi: 10.1016/j.artint.2021.103458. URLhttps://www.sciencedirect.com/science/ar
ticle/pii/S0004370221000096.
Bart P. Knijnenburg, Martijn C. Willemsen, Zeno Gantner, Hakan Soncu, and Chris Newell. Explaining
theuserexperienceofrecommendersystems. UserModelingandUser-AdaptedInteraction,22(4):441–504,
October2012. ISSN1573-1391. doi: 10.1007/s11257-011-9118-4. URLhttps://doi.org/10.1007/s112
57-011-9118-4.
DerekJ.Koehler. Explanation,Imagination,andConfidenceinJudgment. 1991.
PangWeiKohandPercyLiang. UnderstandingBlack-boxPredictionsviaInfluenceFunctions,December
2020. URLhttp://arxiv.org/abs/1703.04730. arXiv:1703.04730[cs,stat].
PangWeiKoh,ThaoNguyen,YewSiangTang,StephenMussmann,EmmaPierson,BeenKim,andPercy
Liang. Concept bottleneck models. In International Conference on Machine Learning, pages 5338–5348.
PMLR,2020.
Adriano Koshiyama, Emre Kazim, Philip Treleaven, Pete Rai, Lukasz Szpruch, Giles Pavey, Ghazi
Ahamat, Franziska Leutner, Randy Goebel, Andrew Knight, Janet Adams, Christina Hitrova, Jeremy
Barnett,ParashkevNachev,DavidBarber,TomasChamorro-Premuzic,KonstantinKlemmer,MiroGre-
gorovic, Shakeel Khan, and Elizabeth Lomas. Towards Algorithm Auditing: A Survey on Managing
Legal, Ethical and Technological Risks of AI, ML and Associated Algorithms. SSRNElectronicJournal,
page31, 2021. ISSN1556-5068. doi: 10.2139/ssrn.3778998. URLhttps://www.ssrn.com/abstract=37
78998.
Yubo Kou and Xinning Gui. Mediating Community-AI Interaction through Situated Explanation: The
Case of AI-Led Moderation. Proceedings of the ACM on Human-Computer Interaction, 4(CSCW2):102:1–
102:27,October2020. doi: 10.1145/3415173. URLhttps://doi.org/10.1145/3415173.
Pigi Kouki, James Schaffer, Jay Pujara, John O’Donovan, and Lise Getoor. Personalized explanations for
hybridrecommendersystems. InProceedingsofthe24thInternationalConferenceonIntelligentUserInter-
faces,IUI’19,pages379–390,NewYork,NY,USA,March2019.AssociationforComputingMachinery.
ISBN 978-1-4503-6272-6. doi: 10.1145/3301275.3302306. URL https://doi.org/10.1145/3301275.33
02306.
Maria Kouvela, Ilias Dimitriadis, and Athena Vakali. Bot-Detective: An explainable Twitter bot detec-
tion service with crowdsourcing functionalities. In Proceedings of the 12th International Conference on
ManagementofDigitalEcoSystems, MEDES ’20, pages 55–63, New York, NY, USA, November 2020. As-
sociation for Computing Machinery. ISBN 978-1-4503-8115-4. doi: 10.1145/3415958.3433075. URL
https://doi.org/10.1145/3415958.3433075.
JosuaKrause,AdamPerer,andKenneyNg. InteractingwithPredictions: VisualInspectionofBlack-box
Machine Learning Models. In Proceedings of the 2016 CHI Conference on Human Factors in Computing
Systems, CHI ’16, pages 5686–5697, New York, NY, USA, 2016. Association for Computing Machinery.
ISBN 978-1-4503-3362-7. doi: 10.1145/2858036.2858529. URL https://doi.org/10.1145/2858036.28
58529.
Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. ImageNet Classification with Deep Convo-
lutional Neural Networks. In Advances in Neural Information Processing Systems, volume 25. Curran
Associates, Inc., 2012. URL https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c
8436e924a68c45b-Abstract.html.
JoshuaA.Kroll, JoannaHuey, SolonBarocas,EdwardW.Felten, JoelR.Reidenberg, DavidG.Robinson,
and Harlan Yu. Accountable Algorithms, March 2016. URL https://papers.ssrn.com/abstract=276
5268.

272 the explanation paradox and the human centric path
-
Luisa Kruse, Nico Wunderlich, and Roman Beck. Artificial Intelligence for the Financial Services In-
dustry: What Challenges Organizations to Succeed. In Proceedings of the 52nd Hawaii International
Conference on System Sciences, page 10, Hawaii, January 2019. ScholarSpace. ISBN 978-0-9981331-2-6.
URLhttp://hdl.handle.net/10125/60075.
Ouren Kuiper, Martin van den Berg, Joost van der Burgt, and Stefan Leijnen. Exploring explainable
AI in the financial sector: Perspectives of banks and supervisory authorities. In Artificial Intelligence
and Machine Learning: 33rd Benelux Conference on Artificial Intelligence, pages 105–119, Esch-sur-Alzette,
Luxembourg,November2021.Springer.
T. Kulesza, S. Stumpf, M. Burnett, S. Yang, I. Kwan, and W. Wong. Too much, too little, or just right?
Ways explanations impact end users’ mental models. In 2013IEEESymposiumonVisualLanguagesand
Human Centric Computing, pages 3–10, September 2013. doi: 10.1109/VLHCC.2013.6645235. ISSN:
1943-6106.
Todd Kulesza, Margaret Burnett, Weng-Keen Wong, and Simone Stumpf. Principles of Explanatory
Debugging to Personalize Interactive Machine Learning. In Proceedings of the 20th International Con-
ference on Intelligent User Interfaces, IUI ’15, pages 126–137, New York, NY, USA, March 2015. As-
sociation for Computing Machinery. ISBN 978-1-4503-3306-1. doi: 10.1145/2678025.2701399. URL
https://doi.org/10.1145/2678025.2701399.
I. Elizabeth Kumar, Suresh Venkatasubramanian, Carlos Scheidegger, and Sorelle Friedler. Problems
with Shapley-value-based explanations as feature importance measures. arXiv:2002.11097 [cs, stat],
June2020. URLhttp://arxiv.org/abs/2002.11097. arXiv: 2002.11097.
E.KurshanandH.Shen. GraphComputingforFinancialCrimeandFraudDetection: Trends,Challenges
andOutlook,March2021. URLhttp://arxiv.org/abs/2103.03227. arXiv:2103.03227[cs].
Alexander Kurz, Katja Hauser, Hendrik Alexander Mehrtens, Eva Krieghoff-Henning, Achim Hekler,
Jakob Nikolas Kather, Stefan Fröhling, Christof von Kalle, and Titus Josef Brinker. Uncertainty Es-
timation in Medical Image Classification: Systematic Review. JMIR Medical Informatics, 10(8):e36427,
August 2022. doi: 10.2196/36427. URL https://medinform.jmir.org/2022/8/e36427. Company:
JMIRMedicalInformaticsDistributor: JMIRMedicalInformaticsInstitution: JMIRMedicalInformatics
Label: JMIRMedicalInformaticsPublisher: JMIRPublicationsInc.,Toronto,Canada.
Dattatray Vishnu Kute, Biswajeet Pradhan, Nagesh Shukla, and Abdullah Alamri. Deep Learning and
ExplainableArtificialIntelligenceTechniquesAppliedforDetectingMoneyLaundering–ACriticalRe-
view. IEEEAccess,9:82300–82317,2021. ISSN2169-3536. doi: 10.1109/ACCESS.2021.3086230. Confer-
enceName: IEEEAccess.
Bum Chul Kwon, Min-Je Choi, Joanne Taery Kim, Edward Choi, Young Bin Kim, Soonwook Kwon, Ji-
meng Sun, and Jaegul Choo. RetainVis: Visual Analytics with Interpretable and Interactive Recurrent
NeuralNetworksonElectronicMedicalRecords. IEEETransactionsonVisualizationandComputerGraph-
ics,25(1):299–309,January2019. ISSN1941-0506. doi: 10.1109/TVCG.2018.2865027. ConferenceName:
IEEETransactionsonVisualizationandComputerGraphics.
Nevine Makram Labib, Mohammed Abo Rizka, and Amr Ehab Muhammed Shokry. Survey of Ma-
chine Learning Approaches of Anti-money Laundering Techniques to Counter Terrorism Finance.
In Atef Zaki Ghalwash, Nashaat El Khameesy, Dalia A. Magdi, and Amit Joshi, editors, Internet of
Things—ApplicationsandFuture,LectureNotesinNetworksandSystems,pages73–87,Singapore,2020.
Springer. ISBN9789811530753.
Vivian Lai and Chenhao Tan. On Human Predictions with Explanations and Predictions of Machine
Learning Models: A Case Study on Deception Detection. In Proceedings of the Conference on Fairness,
Accountability,andTransparency,FAT*’19,pages29–38,NewYork,NY,USA,January2019.Association
for Computing Machinery. ISBN 978-1-4503-6125-5. doi: 10.1145/3287560.3287590. URL https:
//doi.org/10.1145/3287560.3287590.

bibliography 273
Vivian Lai, Chacha Chen, Q. Vera Liao, Alison Smith-Renner, and Chenhao Tan. Towards a Science of
Human-AI Decision Making: A Survey of Empirical Studies, December 2021. URL http://arxiv.or
| g/abs/2112.11471. |     | arXiv:2112.11471[cs]. |     |     |
| ----------------- | --- | --------------------- | --- | --- |
HimabinduLakkarajuandOsbertBastani."HowdoIfoolyou?": ManipulatingUserTrustviaMisleading
BlackBoxExplanations. ProceedingsoftheAAAI/ACMConferenceonAI,Ethics,andSociety,pages79–85,
2020. URLhttps://doi.org/10.1145/3375627.3375833.
Himabindu Lakkaraju, Ece Kamar, Rich Caruana, and Jure Leskovec. Interpretable & Explorable Ap-
proximationsofBlackBoxModels. arXiv:1707.01154[cs],July2017. URLhttp://arxiv.org/abs/1707
| .01154. | arXiv: 1707.01154. |     |     |     |
| ------- | ------------------ | --- | --- | --- |
M. Langer, D. Oster, T. Speith, H. Hermanns, L. Kästner, E. Schmidt, A. Sesing, and K. Baum. What
do we want from Explainable Artificial Intelligence (XAI)? – A stakeholder perspective on XAI and
a conceptual model guiding interdisciplinary XAI research. Artificial Intelligence, 296, 2021. doi:
10.1016/j.artint.2021.103473.
Matthias Laporte. ACPR Conference, p.85, "LUCIA": a SupTech tool to support the fight against money
| laundering | and terrorism | financing, | November | 2021. URL |
| ---------- | ------------- | ---------- | -------- | --------- |
https://acpr.banque-france.fr/sites/d
efault/files/media/2022/11/15/20211126_presentations_des_intervenants_de_la_matinee.pdf.
DavidB.Leake. Goal-basedexplanationevaluation. CognitiveScience,15(4):509–545,October1991. ISSN
| 0364-0213. | doi: 10.1016/0364-0213(91)80017-Y. |     |     | URL |
| ---------- | ---------------------------------- | --- | --- | --- |
https://www.sciencedirect.com/science/arti
cle/pii/036402139180017Y.
David B. Leake. Abduction, experience, and goals: a model of everyday abductive explanation. Journal
of Experimental & Theoretical Artificial Intelligence, 7(4):407–428, October 1995. ISSN 0952-813X. doi:
10.1080/09528139508953820.
|                  |                                            | URL | https://doi.org/10.1080/09528139508953820. | Publisher: Taylor |
| ---------------- | ------------------------------------------ | --- | ------------------------------------------ | ----------------- |
| &Francis_eprint: | https://doi.org/10.1080/09528139508953820. |     |                                            |                   |
Matthew L. Leavitt and Ari Morcos. Towards falsifiable interpretability research. arXiv:2010.12016 [cs,
stat],October2020. 2010.12016.
URLhttp://arxiv.org/abs/2010.12016. arXiv:
Freddy Lecue. On the role of knowledge graphs in explainable AI. Semantic Web, 11(1):41–51, January
| 2020. ISSN | 1570-0844. | doi: 10.3233/SW-190374. |     | URL |
| ---------- | ---------- | ----------------------- | --- | --- |
https://content.iospress.com/articles/se
| mantic-web/sw190374. |     | Publisher: IOSPress. |     |     |
| -------------------- | --- | -------------------- | --- | --- |
YannLeCun,YoshuaBengio,andGeoffreyHinton. Deeplearning. Nature,521(7553):436–444,May2015.
ISSN 1476-4687. doi: 10.1038/nature14539. URL https://www.nature.com/articles/nature14539.
7553Publisher:
| Number: |     | NaturePublishingGroup. |     |     |
| ------- | --- | ---------------------- | --- | --- |
John Lee and Neville Moray. Trust, control strategies and allocation of function in human-machine sys-
tems. Ergonomics, 35(10):1243–1270, October 1992. ISSN 0014-0139. doi: 10.1080/00140139208967392.
URL https://doi.org/10.1080/00140139208967392. Publisher: Taylor & Francis _eprint:
https://doi.org/10.1080/00140139208967392.
John D. Lee and Katrina A. See. Trust in Automation: Designing for Appropriate Reliance. Human
|     | 46(1):50–80, | 2004. | 0018-7208. |     |
| --- | ------------ | ----- | ---------- | --- |
Factors, March ISSN URL https://journals.sagepub.com/doi/abs/10.
| 1518/hfes.46.1.50_30392. |     | Publisher: | SAGEPublicationsInc. |     |
| ------------------------ | --- | ---------- | -------------------- | --- |
Min Kyung Lee, Anuraag Jain, Hea Jin Cha, Shashank Ojha, and Daniel Kusbit. Procedural Justice in
AlgorithmicFairness: LeveragingTransparencyandOutcomeControlforFairAlgorithmicMediation.
Proceedings of the ACM on Human-Computer Interaction, 3(CSCW):182:1–182:26, November 2019. doi:
10.1145/3359284.
URLhttps://doi.org/10.1145/3359284.
RandyLee. LouisBrandeis’sVisionofLightandJusticeasArticulatedontheSideofCoffeeMug. Touro
LawReview,33:323,2017. URLhttps://heinonline.org/HOL/Page?handle=hein.journals/touro33&i
d=331&div=&collection=.

| 274 | the | explanation | paradox |     | and the | human | centric | path |     |     |     |
| --- | --- | ----------- | ------- | --- | ------- | ----- | ------- | ---- | --- | --- | --- |
-
|     |     |     |     |     |     |     |     | 34:289–375, |     | 2006. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --- |
Michael Levi and Peter Reuter. Money Laundering. Crime and Justice, January ISSN
0192-3234. doi: 10.1086/501508. URL https://www.journals.uchicago.edu/doi/abs/10.1086/5015
| 08. | Publisher: | TheUniversityofChicagoPress. |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2011.
David Levi-Faur. Handbook on the Politics of Regulation. Edward Elgar Publishing, January ISBN
| 978-0-85793-611-0. |     | Google-Books-ID:KOKtKzEyQlYC. |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
MichaelE.LevineandJenniferL.Forrence. RegulatoryCapture,PublicInterest,andthePublicAgenda:
|     |     |     |     |     |     |     | 6:167, | 1990. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- | --- |
TowardaSynthesis. JournalofLaw,Economics,andOrganization, URLhttps://heinonline
.org/HOL/Page?handle=hein.journals/jleo6&id=651&div=&collection=. Accessed11/29/2023.
James R. Lewis. Psychometric evaluation of an after-scenario questionnaire for computer usabil-
|                        |          |          |                                           |        |           | 23(1):78–81, |         | 1991. |      | 0736-6906. | doi: |
| ---------------------- | -------- | -------- | ----------------------------------------- | ------ | --------- | ------------ | ------- | ----- | ---- | ---------- | ---- |
| ity                    | studies: | the ASQ. | ACM                                       | SIGCHI | Bulletin, |              | January |       | ISSN |            |      |
| 10.1145/122672.122692. |          |          | URLhttps://doi.org/10.1145/122672.122692. |        |           |              |         |       |      |            |      |
Q. Vera Liao and Kush R. Varshney. Human-Centered Explainable AI (XAI): From Algorithms to User
| Experiences,April2022. |     |     |     |     |     |     |     | arXiv:2110.10790[cs]. |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
URLhttp://arxiv.org/abs/2110.10790.
Q. Vera Liao, Daniel Gruen, and Sarah Miller. Questioning the AI: Informing Design Practices for Ex-
plainableAIUserExperiences. InProceedingsofthe2020CHIConferenceonHumanFactorsinComputing
|     |     | ’20, | 1–15, |     |     |     | 2020. |     |     |     |     |
| --- | --- | ---- | ----- | --- | --- | --- | ----- | --- | --- | --- | --- |
Systems, CHI pages New York, NY, USA, April Association for Computing Machinery.
ISBN 978-1-4503-6708-0. doi: 10.1145/3313831.3376590. URL https://doi.org/10.1145/3313831.33
76590.
Q.VeraLiao,HariharanSubramonyam,JenniferWang,andJenniferWortmanVaughan. DesignerlyUn-
derstanding: Information Needs for Model Transparency to Support Design Ideation for AI-Powered
UserExperience. InProceedingsofthe2023CHIConferenceonHumanFactorsinComputingSystems,pages
| 1–21, |         |          |       | 2023. |      | 978-1-4503-9421-5. |     | doi: | 10.1145/3544548.3580652. |     |     |
| ----- | ------- | -------- | ----- | ----- | ---- | ------------------ | --- | ---- | ------------------------ | --- | --- |
|       | Hamburg | Germany, | April |       | ACM. | ISBN               |     |      |                          |     |     |
URLhttps://dl.acm.org/doi/10.1145/3544548.3580652.
Brian Y. Lim and Anind K. Dey. Assessing demand for intelligibility in context-aware applications. In
|     |     |     |     |     |     |     |     |     | ’09, |     | 195–204, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | -------- |
Proceedings of the 11th international conference on Ubiquitous computing, UbiComp pages
NewYork,NY,USA,September2009.AssociationforComputingMachinery. ISBN978-1-60558-431-7.
doi: 10.1145/1620545.1620576.
URLhttps://doi.org/10.1145/1620545.1620576.
GabrielLima,NinaGrgic´-Hlacˇa,JinKeunJeong,andMeeyoungCha. TheConflictBetweenExplainable
and Accountable Decision-Making Algorithms. In Proceedings of the 2022 ACM Conference on Fairness,
|     |     |     |     |     | ’22, | 2103–2113, |     |     |     | 2022. |     |
| --- | --- | --- | --- | --- | ---- | ---------- | --- | --- | --- | ----- | --- |
Accountability, and Transparency, FAccT pages New York, NY, USA, Association
|     |           |            |     | 978-1-4503-9352-2. |     |     | doi: 10.1145/3531146.3534628. |     |     |     |        |
| --- | --------- | ---------- | --- | ------------------ | --- | --- | ----------------------------- | --- | --- | --- | ------ |
| for | Computing | Machinery. |     | ISBN               |     |     |                               |     |     | URL | https: |
//dl.acm.org/doi/10.1145/3531146.3534628.
AdamDahlgrenLindström,WendyE.Mackay,andVirginiaDignum.ThinkingFastAndSlowInHuman-
Centered AI. In ThinkingFastandSlowandOtherCognitiveTheoriesinAI,AAAIFallsymposiumFSS-22,
pages3–pages,2022. URLhttps://inria.hal.science/hal-03991946/document.
|     |     |     |     |     |     |     | 1993. |     | 978-1-56000-677-0. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------------------ | --- | --- |
Walter Lippmann. The Phantom Public. Transaction Publishers, ISBN Google-
Books-ID:AUJTAQAAQBAJ.
Peter Lipton. Contrastive Explanation. Royal Institute of Philosophy Supplements, 27:247–266, March 1990.
ISSN1755-3555,1358-2461.
|     |     |     | Publisher: |     | CambridgeUniversityPress. |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
61(10):36–43,
Zachary C. Lipton. The mythos of model interpretability. Communications of the ACM,
September2018. ISSN0001-0782. doi: 10.1145/3233231. URLhttps://doi.org/10.1145/3233231.
Han Liu, Vivian Lai, and Chenhao Tan. Understanding the Effect of Out-of-distribution Examples and
Interactive Explanations on Human-AI Decision Making. Proceedings of the ACM on Human-Computer
Interaction, 5(CSCW2):408:1–408:45, October2021. doi: 10.1145/3479552. URLhttps://doi.org/10.1
145/3479552.

bibliography 275
Jiali Liu. Data expression : understanding and supporting alternatives in data analysis processes. phdthesis,
InstitutPolytechniquedeParis,September2021. URLhttps://theses.hal.science/tel-03577013.
TaniaLombrozo. Thestructureandfunctionofexplanations. TrendsinCognitiveSciences,10(10):464–470,
October 2006. ISSN 1364-6613. doi: 10.1016/j.tics.2006.08.004. URL http://www.sciencedirect.com/
science/article/pii/S1364661306002117.
Tania Lombrozo. Simplicity and probability in causal explanation. Cognitive Psychology, 55(3):232–257,
November2007. ISSN0010-0285. doi: 10.1016/j.cogpsych.2006.09.006. URLhttps://www.sciencedir
ect.com/science/article/pii/S0010028506000739.
Tania Lombrozo. Explanatory Preferences Shape Learning and Inference. TrendsinCognitiveSciences, 20
(10):748–759,October2016. ISSN1364-6613. doi: 10.1016/j.tics.2016.08.001. URLhttps://www.scienc
edirect.com/science/article/pii/S136466131630105X.
Tanya Lombrozo. Explanation and Abductive Inference. In Keith J. Holyoak and Robert G. Morrison,
editors, The Oxford Handbook of Thinking and Reasoning, page 0. Oxford University Press, March 2012.
ISBN 978-0-19-973468-9. doi: 10.1093/oxfordhb/9780199734689.013.0014. URL https://doi.org/10
.1093/oxfordhb/9780199734689.013.0014.
Luca Longo, Randy Goebel, Freddy Lecue, Peter Kieseberg, and Andreas Holzinger. Explainable Arti-
ficial Intelligence: Concepts, Applications, Research Challenges and Visions. In Andreas Holzinger,
Peter Kieseberg, A Min Tjoa, and Edgar Weippl, editors, Machine Learning and Knowledge Extraction,
Lecture Notes in ComputerScience, pages1–16, Cham, 2020.Springer InternationalPublishing. ISBN
978-3-030-57321-8.
Joana Lorenz, Maria Inês Silva, David Aparício, João Tiago Ascensão, and Pedro Bizarro. Machine
learningmethodstodetectmoneylaunderingintheBitcoinblockchaininthepresenceoflabelscarcity.
arXiv:2005.14635 [cs, stat], May 2020. URL http://arxiv.org/abs/2005.14635. arXiv: 2005.14635
version: 1.
JordanJLouviere,TerryNFlynn,andRichardTCarson. DiscreteChoiceExperimentsAreNotConjoint
Analysis. Journal of Choice Modelling, 3(3):57–72, January 2010. ISSN 1755-5345. doi: 10.1016/S1755-
5345(13)70014-9. URLhttps://www.sciencedirect.com/science/article/pii/S1755534513700149.
AnaLucic,HindaHaned,andMaartendeRijke. Whydoesmymodelfail? contrastivelocalexplanations
for retail forecasting. In Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency,
FAT*’20,pages90–98,NewYork,NY,USA,January2020.AssociationforComputingMachinery. ISBN
978-1-4503-6936-7. doi: 10.1145/3351095.3372824. URLhttps://doi.org/10.1145/3351095.3372824.
Scott M. Lundberg and Su-In Lee. A unified approach to interpreting model predictions. In Proceedings
of the 31st International Conference on Neural Information Processing Systems, NIPS’17, pages 4768–4777,
RedHook,NY,USA,2017.CurranAssociatesInc. ISBN978-1-5108-6096-4.
Scott M. Lundberg, Gabriel G. Erion, and Su-In Lee. Consistent Individualized Feature Attribution for
TreeEnsembles,March2019. URLhttp://arxiv.org/abs/1802.03888. arXiv:1802.03888[cs,stat].
MichalLuria. Co-DesignPerspectivesonAlgorithmTransparencyReporting: GuidelinesandPrototypes.
In2023ACMConferenceonFairness,Accountability,andTransparency,pages1076–1087,ChicagoILUSA,
June2023.ACM. ISBN9798400701924. doi: 10.1145/3593013.3594064. URLhttps://dl.acm.org/doi
/10.1145/3593013.3594064.
Henrietta Lyons, Eduardo Velloso, and Tim Miller. Designing for Contestation: Insights from Adminis-
trative Law. arXiv:2102.04559 [cs], February 2021. URL http://arxiv.org/abs/2102.04559. arXiv:
2102.04559.
Légifrance. Arrêtédu3novembre2014relatifaucontrôleinternedesentreprisesdusecteurdelabanque,
desservicesdepaiementetdesservicesd’investissementsoumisesaucontrôledel’Autoritédecontrôle
prudentiel et de résolution, August 2023a. URL https://www.legifrance.gouv.fr/loda/id/JORFTEX
T000029700770.

276 the explanation paradox and the human centric path
-
Légifrance. ChapitreIer: Obligationsrelativesàlaluttecontreleblanchimentdescapitauxetlefinance-
ment du terrorisme (Articles L561-1 à L561-50), August 2023b. URL https://www.legifrance.gouv.
fr/codes/section_lc/LEGITEXT000006072026/LEGISCTA000006154830/.
Wendy E. Mackay and Anne-Laure Fayard. HCI, natural science and design: a framework for tri-
angulation across disciplines. In Proceedings of the 2nd conference on Designing interactive systems:
processes, practices, methods, and techniques, DIS ’97, pages 223–234, New York, NY, USA, 1997. As-
sociation for Computing Machinery. ISBN 978-0-89791-863-3. doi: 10.1145/263552.263612. URL
https://dl.acm.org/doi/10.1145/263552.263612.
PoornimaMadhavan,DouglasA.Wiegmann,andFrankC.Lacson. AutomationFailuresonTasksEasily
Performed by Operators Undermine Trust in Automated Aids. Human Factors, 48(2):241–256, June
2006. ISSN 0018-7208. doi: 10.1518/001872006777724408. URL https://doi.org/10.1518/00187200
6777724408. Publisher: SAGEPublicationsInc.
P. Madumal, L. Sonenberg, T. Miller, and F. Vetere. A grounded interaction protocol for explainable
artificialintelligence. volume2,pages1033–1041,2019.
Bertram F. Malle. How the Mind Explains Behavior: Folk Explanations, Meaning, and Social Interaction. A
BradfordBook,Cambridge,MA,USA,September2004. ISBN978-0-262-13445-3.
NicholasMaltbie,NanNiu,MatthewVanDoren,andReeseJohnson.XAItoolsinthepublicsector: acase
studyonpredictingcombinedseweroverflows. InProceedingsofthe29thACMJointMeetingonEuropean
Software Engineering Conference and Symposium on the Foundations of Software Engineering, ESEC/FSE
2021,pages1032–1044,NewYork,NY,USA,2021.AssociationforComputingMachinery. ISBN978-1-
4503-8562-6. doi: 10.1145/3468264.3468547. URLhttps://doi.org/10.1145/3468264.3468547.
YOKOI-ARAI Mamiko. The Impact of Big Data and Artificial Intelligence (AI) in the Insurance Sector.
Technical report, OECD, January 2020. URL http://www.oecd.org/finance/Impact-Big-Data-AI-i
n-the-Insurance-Sector.htm.
Marisa Tschopp. Digital transformation - Three wrong questions about trust and AI, September 2020.
URL https://digital-commerce.post.ch/en/pages/blog/2020/trust-in-artificial-intelligenc
e. Accessed1/11/2024.
Aniek F. Markus, Jan A. Kors, and Peter R. Rijnbeek. The role of explainability in creating trustworthy
artificial intelligence for health care: A comprehensive survey of the terminology, design choices, and
evaluation strategies. Journal ofBiomedical Informatics, 113:103655, January 2021. ISSN 1532-0464. doi:
10.1016/j.jbi.2020.103655. URL https://www.sciencedirect.com/science/article/pii/S153204642
0302835.
David Martens, Camille Dams, James Hinns, and Mark Vergouwen. Tell Me a Story! Narrative-Driven
XAI with Large Language Models, September 2023. URL http://arxiv.org/abs/2309.17057.
arXiv:2309.17057[cs].
Jerry L Mashaw. Small things like reasons are put in a jar: reason and legitimacy in the administrative
state. FordhamLawReview,70(1),2001.
Arunesh Mathur, Gunes Acar, Michael J. Friedman, Eli Lucherini, Jonathan Mayer, Marshini Chetty,
and Arvind Narayanan. Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites.
Proceedings of the ACM on Human-Computer Interaction, 3(CSCW):81:1–81:32, November 2019. doi:
10.1145/3359183. URLhttps://dl.acm.org/doi/10.1145/3359183.
WinstonMaxwell. TheGDPRandPrivateSectorMeasurestoDetectCriminalActivity,March2021. URL
https://papers.ssrn.com/abstract=3964066.
Winston Maxwell. Meaningful Human Control to Detect Algorithmic Errors. In Céline Castets-Renard
and Jessica Eynard, editors, ArtificialIntelligenceLaw: BetweenSectoralRulesandComprehensiveRegime-
ComparativeLawPerspectives.Bruylant,2023. URLhttps://hal.science/hal-04026883.

bibliography 277
WinstonMaxwellandBrunoDumas. MeaningfulXAIbasedonuser-centricdesignmethodology: Com-
bining legal and human-computer interaction (HCI) approaches to achieve meaningful algorithmic
explainability. Technicalreport,CERRE,2023.
RogerC.Mayer,JamesH.Davis,andF.DavidSchoorman. AnIntegrativeModelofOrganizationalTrust.
TheAcademyofManagementReview, 20(3):709–734, 1995. ISSN 0363-7425. URL https://www.jstor.or
g/stable/258792. Publisher: AcademyofManagement.
Elizabeth McCaul. Technology is neither good nor bad, but humans make it so, July 2022. URL https:
//www.bankingsupervision.europa.eu/press/speeches/date/2022/html/ssm.sp220713~73f22a486
e.en.html.
MikeMcConville. ResearchMethodsforLaw. EdinburghUniversityPress,January2017. ISBN978-1-4744-
0425-9. Google-Books-ID:4jRWDwAAQBAJ.
Ann L.McGilland JillG. Klein. Contrastive andcounterfactual reasoningin causaljudgment. Journalof
PersonalityandSocialPsychology,64(6):897–905,1993. ISSN1939-1315. doi: 10.1037/0022-3514.64.6.897.
Place: USPublisher: AmericanPsychologicalAssociation.
Joseph E. Mcgrath. Methodology Matters: Doing Research in the Behavioral and Social Sciences. In
Ronald M. Baecker, Jonathan Grudin, William A.S. Buxton, and Saul Greenberg, editors, Readings
in Human–Computer Interaction, Interactive Technologies, pages 152–169. Morgan Kaufmann, January
1995. ISBN 978-0-08-051574-8. doi: 10.1016/B978-0-08-051574-8.50019-4. URL https://www.scienced
irect.com/science/article/pii/B9780080515748500194.
Michael McKenna and D. Justin Coates. Compatibilism. In Edward N. Zalta, editor, The Stanford En-
cyclopedia of Philosophy. Metaphysics Research Lab, Stanford University, fall 2021 edition, 2021. URL
https://plato.stanford.edu/archives/fall2021/entries/compatibilism/.
D. Mcknight, Michelle Carter, Jason Thatcher, and Paul Clay. Trust in a specific technology: An Investi-
gationofitsComponentsandMeasures. ACMTransactionsonManagementInformationSystems,2:12–32,
June2011. doi: 10.1145/1985347.1985353.
D. Harrison McKnight, Vivek Choudhury, and Charles Kacmar. Developing and Validating Trust Mea-
suresfore-Commerce: AnIntegrativeTypology. InformationSystemsResearch,13(3):334–359,September
2002. ISSN1047-7047. doi: 10.1287/isre.13.3.334.81. URLhttps://pubsonline.informs.org/doi/10.
1287/isre.13.3.334.81. Publisher: INFORMS.
Jessie McWaters and Matthew Blake. Navigating Uncharted Waters: A Roadmap to Responsible Inno-
vation with AI in Financial Services. Part of the Future of Financial Services Series. World Economic
Forum. Technical report, World Economic Forum, 2019. URL https://www3.weforum.org/docs/WEF_
Navigating_Uncharted_Waters_Report.pdf.
Gaspar Isaac Melsión, Ilaria Torre, Eva Vidal, and Iolanda Leite. Using Explainability to Help Children
UnderstandGender Bias in AI. In Interaction Design and Children, pages 87–99, Athens Greece, June
2021.ACM. ISBN978-1-4503-8452-0. doi: 10.1145/3459990.3460719. URLhttps://dl.acm.org/doi/1
0.1145/3459990.3460719.
Bertalan Meskó and Eric J. Topol. The imperative for regulatory oversight of large language mod-
els (or generative AI) in healthcare. npj Digital Medicine, 6(1):1–6, July 2023. ISSN 2398-6352. doi:
10.1038/s41746-023-00873-0. URLhttps://www.nature.com/articles/s41746-023-00873-0. Number:
1Publisher: NaturePublishingGroup.
Danaë Metaxa, Joon Sung Park, Ronald E. Robertson, Karrie Karahalios, Christo Wilson, Jeff Hancock,
and Christian Sandvig. Auditing Algorithms: Understanding Algorithmic Systems from the Outside
In. FoundationsandTrends®inHuman–ComputerInteraction, 14(4):272–344, 2021. ISSN 1551-3955, 1551-
3963. doi: 10.1561/1100000083. URLhttp://www.nowpublishers.com/article/Details/HCI-083.

| 278 | the explanation |     | paradox | and | the | human | centric | path |     |     |     |
| --- | --------------- | --- | ------- | --- | --- | ----- | ------- | ---- | --- | --- | --- |
-
MartijnMillecamp,NyiNyiHtun,CristinaConati,andKatrienVerbert. Toexplainornottoexplain: the
effects of personal characteristics when explaining music recommendations. In Proceedings of the 24th
InternationalConferenceonIntelligentUserInterfaces,IUI’19,pages397–407,NewYork,NY,USA,March
| 2019. |             |     |           |            |      | 978-1-4503-6272-6. |     | doi: | 10.1145/3301275.3302313. |     |     |
| ----- | ----------- | --- | --------- | ---------- | ---- | ------------------ | --- | ---- | ------------------------ | --- | --- |
|       | Association | for | Computing | Machinery. | ISBN |                    |     |      |                          |     |     |
URLhttps://doi.org/10.1145/3301275.3302313.
Tim Miller. Explanation in artificial intelligence: Insights from the social sciences. Artificial Intelligence,
267:1–38, 2019. 0004-3702. doi: 10.1016/j.artint.2018.07.007.
|     | February |     | ISSN |     |     |     |     |     | URL http://www.scienc |     |     |
| --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
edirect.com/science/article/pii/S0004370218305988.
Tim Miller. Contrastive explanation: a structural-model approach. The Knowledge Engineering Review,
36:e14, 2021. 0269-8889, 1469-8005. doi: 10.1017/S0269888921000102.
|     | January |     | ISSN |     |     |     |     |     |     | URL | https: |
| --- | ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | ------ |
//www.cambridge.org/core/journals/knowledge-engineering-review/article/abs/contrastiv
e-explanation-a-structuralmodel-approach/69A2E32B160C2C7FB65BC88670D7AEA7. Publisher:
CambridgeUniversityPress.
Tim Miller. Are we measuring trust correctly in explainability, interpretability, and transparency re-
search?,August2022. URLhttp://arxiv.org/abs/2209.00651. arXiv:2209.00651[cs].
Tim Miller. Explainable AI is Dead, Long Live Explainable AI! Hypothesis-driven decision support,
February2023. URLhttp://arxiv.org/abs/2302.12389. arXiv:2302.12389[cs].
TimMiller,PiersHowe,andLizSonenberg. ExplainableAI:BewareofInmatesRunningtheAsylumOr:
How I Learnt to Stop Worrying and Love the Social and Behavioural Sciences. arXiv:1712.00547 [cs],
| December2017. |     |                                     |     |     |     |     |        | 1712.00547. |     |     |     |
| ------------- | --- | ----------------------------------- | --- | --- | --- | --- | ------ | ----------- | --- | --- | --- |
|               |     | URLhttp://arxiv.org/abs/1712.00547. |     |     |     |     | arXiv: |             |     |     |     |
Yao Ming, Huamin Qu, and Enrico Bertini. RuleMatrix: Visualizing and Understanding Classifiers with
IEEETransactionsonVisualizationandComputerGraphics,25(1):342–352,January2019. ISSN1941-
Rules.
| 0506. | doi: 10.1109/TVCG.2018.2864812. |     |     |     |            |     |            |              |                  |     |     |
| ----- | ------------------------------- | --- | --- | --- | ---------- | --- | ---------- | ------------ | ---------------- | --- | --- |
|       |                                 |     |     |     | Conference |     | Name: IEEE | Transactions | on Visualization |     | and |
ComputerGraphics.
Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson,
Elena Spitzer, Inioluwa Deborah Raji, and Timnit Gebru. Model Cards for Model Reporting. In Pro-
ceedings of the Conference on Fairness, Accountability, and Transparency, FAT* ’19, pages 220–229, New
|     |     |     | 2019. |     |     |     |     |     | 978-1-4503-6125-5. |     | doi: |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | ------------------ | --- | ---- |
York, NY, USA, January Association for Computing Machinery. ISBN
10.1145/3287560.3287596. URLhttps://dl.acm.org/doi/10.1145/3287560.3287596.
Melanie Mitchell. Why AI is Harder Than We Think. arXiv:2104.12871 [cs], April 2021. URL http:
2104.12871.
| //arxiv.org/abs/2104.12871. |     |     |     | arXiv: |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
NatureMachineIntelligence,1(11):501–507,
| BrentMittelstadt. |     | PrinciplesalonecannotguaranteeethicalAI. |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
November2019. ISSN2522-5839. doi: 10.1038/s42256-019-0114-4. URLhttps://www.nature.com/art
11Publisher:
| icles/s42256-019-0114-4. |     |     | Number: |     |     | NaturePublishingGroup. |     |     |     |     |     |
| ------------------------ | --- | --- | ------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- |
Brent Mittelstadt, Chris Russell, and Sandra Wachter. Explaining Explanations in AI. In Proceed-
ings of the Conference on Fairness, Accountability, and Transparency, FAT* ’19, pages 279–288, New
|     |     |     | 2019. |     |     |     |     |     | 978-1-4503-6125-5. |     | doi: |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | ------------------ | --- | ---- |
York, NY, USA, January Association for Computing Machinery. ISBN
10.1145/3287560.3287574.
URLhttps://doi.org/10.1145/3287560.3287574.
Akira Miyake and Priti Shah, editors. Models of working memory: Mechanisms of active maintenance and
executivecontrol.Modelsofworkingmemory:
Mechanismsofactivemaintenanceandexecutivecontrol.
CambridgeUniversityPress,NewYork,NY,US,1999. ISBN978-0-521-58325-1978-0-521-58721-1. doi:
| 10.1017/CBO9781139174909. |     |     |     | Pages: xx,506. |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
David Moher, Alessandro Liberati, Jennifer Tetzlaff, Douglas G. Altman, and The PRISMA Group. Pre-
ferred Reporting Items for Systematic Reviews and Meta-Analyses: The PRISMA Statement. PLoS
Medicine, 6(7):e1000097, July 2009. ISSN 1549-1676. doi: 10.1371/journal.pmed.1000097. URL
https://dx.plos.org/10.1371/journal.pmed.1000097.

bibliography 279
Sina Mohseni, Jeremy E Block, and Eric Ragan. Quantitative Evaluation of Machine Learning Ex-
planations: A Human-Grounded Benchmark. In 26th International Conference on Intelligent User In-
terfaces, pages 22–31, College Station TX USA, April 2021a. ACM. ISBN 978-1-4503-8017-1. doi:
10.1145/3397481.3450689. URLhttps://dl.acm.org/doi/10.1145/3397481.3450689.
SinaMohseni,NiloofarZarei,andEricD.Ragan. AMultidisciplinarySurveyandFrameworkforDesign
and Evaluation of Explainable AI Systems. ACM Transactions on Interactive Intelligent Systems, 11(3-4):
24:1–24:45, September 2021b. ISSN 2160-6455. doi: 10.1145/3387166. URL https://dl.acm.org/doi
/10.1145/3387166.
Robert Molloy and Raja Parasuraman. Monitoring an Automated System for a Single Failure: Vigi-
lance and Task Complexity Effects. Human Factors, 38(2):311–322, June 1996. ISSN 0018-7208. doi:
10.1177/001872089606380211. URLhttps://doi.org/10.1177/001872089606380211. Publisher: SAGE
PublicationsInc.
ChristophMolnar. InterpretableMachineLearning. 2019. URLhttps://christophm.github.io/interpret
able-ml-book/.
David L. Morgan. Focus Groups. Annual Review of Sociology, 22(1):129–152, 1996. doi: 10.1146/an-
nurev.soc.22.1.129. URL https://doi.org/10.1146/annurev.soc.22.1.129. _eprint:
https://doi.org/10.1146/annurev.soc.22.1.129.
Jessica Morley, Caio C. V. Machado, Christopher Burr, Josh Cowls, Indra Joshi, Mariarosaria Taddeo,
and Luciano Floridi. The ethics of AI in health care: A mapping review. Social Science & Medicine,
260:113172, September 2020. ISSN 0277-9536. doi: 10.1016/j.socscimed.2020.113172. URL https:
//www.sciencedirect.com/science/article/pii/S0277953620303919.
Cecily Morrison, Kit Huckvale, Bob Corish, Richard Banks, Martin Grayson, Jonas Dorn, Abigail Sellen,
and Sân Lindley. Visualizing Ubiquitously Sensed Measures of Motor Ability in Multiple Sclerosis:
ReflectionsonCommunicatingMachineLearninginPractice. ACMTransactionsonInteractiveIntelligent
Systems, 8(2):1–28, July2018. ISSN2160-6455, 2160-6463. doi: 10.1145/3181670. URLhttps://dl.acm
.org/doi/10.1145/3181670.
DavidA.Moss,DavidMoss,andJohnCisternino. NewPerspectivesonRegulation. TheTobinProject,2009.
ISBN978-0-9824788-0-6. Google-Books-ID:wEQ6QGS6sPkC.
Stephen Muggleton. Inductive logic programming. New Generation Computing, 8(4):295–318, February
1991. ISSN1882-7055. doi: 10.1007/BF03037089. URLhttps://doi.org/10.1007/BF03037089.
C.D.Mulrow. SystematicReviews: Rationaleforsystematicreviews. BMJ,309(6954):597–599,September
1994. ISSN 0959-8138, 1468-5833. doi: 10.1136/bmj.309.6954.597. URL https://www.bmj.com/conten
t/309/6954/597. Publisher: BritishMedicalJournalPublishingGroupSection: Educationanddebate.
Zachary Munn, Micah D. J. Peters, Cindy Stern, Catalin Tufanaru, Alexa McArthur, and Edoardo Aro-
mataris. Systematicrevieworscopingreview? Guidanceforauthorswhenchoosingbetweenasystem-
atic or scoping review approach. BMC Medical Research Methodology, 18(1):143, November 2018. ISSN
1471-2288. doi: 10.1186/s12874-018-0611-x. URLhttps://doi.org/10.1186/s12874-018-0611-x.
JakobMökander,JonasSchuett,HannahRoseKirk,andLucianoFloridi.Auditinglargelanguagemodels:
a three-layered approach. AI and Ethics, 3(2):31, May 2023. ISSN 2730-5961. doi: 10.1007/s43681-023-
00289-2. URLhttps://doi.org/10.1007/s43681-023-00289-2.
BerndtMüller,JoachimReinhardt,andMichaelT.Strickland. NeuralNetworks: AnIntroduction. Springer
Science&BusinessMedia,October1995. ISBN978-3-540-60207-1.
Mohammad Naiseh, Nan Jiang, Jianbing Ma, and Raian Ali. Personalising Explainable Recommen-
dations: Literature and Conceptualisation. In Álvaro Rocha, Hojjat Adeli, Luís Paulo Reis, Sandra
Costanzo, Irena Orovic, and Fernando Moreira, editors, Trends and Innovations in Information Systems
andTechnologies,AdvancesinIntelligentSystemsandComputing,pages518–533,Cham,2020.Springer
InternationalPublishing. ISBN978-3-030-45691-7.

| 280 | the | explanation | paradox |     | and the | human | centric | path |     |     |     |     |
| --- | --- | ----------- | ------- | --- | ------- | ----- | ------- | ---- | --- | --- | --- | --- |
-
Mohammad Naiseh, Reem S. Al-Mansoori, Dena Al-Thani, Nan Jiang, and Raian Ali. Nudging through
Friction: AnApproachforCalibratingTrustinExplainableAI.In20218thInternationalConferenceonBe-
havioralandSocialComputing(BESC),pages1–5,October2021a. doi: 10.1109/BESC53957.2021.9635271.
Mohammad Naiseh, Deniz Cemiloglu, Dena Al Thani, Nan Jiang, and Raian Ali. Explainable Recom-
Computer,54(10):28–37,October2021b.
| mendationsandCalibratedTrust: |     |      |                          | TwoSystematicUserErrors. |     |                 |     |           |     |     |     |     |
| ----------------------------- | --- | ---- | ------------------------ | ------------------------ | --- | --------------- | --- | --------- | --- | --- | --- | --- |
| ISSN1558-0814.                |     | doi: | 10.1109/MC.2021.3076131. |                          |     |                 |     |           |     |     |     |     |
|                               |     |      |                          |                          |     | ConferenceName: |     | Computer. |     |     |     |     |
Luca Nannini, Agathe Balayn, and Adam Leon Smith. Explainability in AI Policies: A Critical Re-
view of Communications, Reports, Regulations, and Standards in the EU, US, and UK. In Proceed-
|     |     |     |     |     |     |     |     |     |     | ’23, |     | 1198– |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ----- |
ings of the 2023 ACM Conference on Fairness, Accountability, and Transparency, FAccT pages
| 1212, |     |           | 2023. |             |     |               |            |      | 9798400701924. |     |     | doi: |
| ----- | --- | --------- | ----- | ----------- | --- | ------------- | ---------- | ---- | -------------- | --- | --- | ---- |
|       | New | York, NY, | USA,  | Association |     | for Computing | Machinery. | ISBN |                |     |     |      |
10.1145/3593013.3594074. URLhttps://dl.acm.org/doi/10.1145/3593013.3594074.
National Transportation Safety Board. Aircract Accident Report, In-flight Breakup Over the Atlantic
|     |     |     |     | 800, |     | 747-131, | N93119 |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | -------- | ------ | --- | --- | --- | --- | --- |
Ocean, Trans World Airlines Flight Boeing Near East Moriches, New York, July
| 17,1996. |     | Technicalreport,August2000. |     |     |     |     |     |     |     |     |     |     |
| -------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Meike Nauta, Jan Trienes, Shreyasi Pathak, Elisa Nguyen, Michelle Peters, Yasmin Schmitt, Jörg Schlöt-
terer, Maurice van Keulen, and Christin Seifert. From Anecdotal Evidence to Quantitative Evaluation
Methods: ASystematicReviewonEvaluatingExplainableAI. ACMComputingSurveys,55(13s):295:1–
| 295:42,2023. |     | ISSN0360-0300. |     | doi: 10.1145/3583558. |     |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
URLhttps://dl.acm.org/doi/10.1145/3583558.
E.W.T.Ngai,YongHu,Y.H.Wong,YijunChen,andXinSun. Theapplicationofdataminingtechniques
infinancialfrauddetection: Aclassificationframeworkandanacademicreviewofliterature. Decision
Support Systems, 50(3):559–569, February 2011. ISSN 0167-9236. doi: 10.1016/j.dss.2010.08.006. URL
https://www.sciencedirect.com/science/article/pii/S0167923610001302.
Anh Nguyen, Jason Yosinski, and Jeff Clune. Multifaceted Feature Visualization: Uncovering the
2016.
Different Types of Features Learned By Each Neuron in Deep Neural Networks, May URL
| http://arxiv.org/abs/1602.03616. |     |     |     |     | arXiv:1602.03616[cs]. |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
Jakob Nielsen. Finding usability problems through heuristic evaluation. In Proceedings of the SIGCHI
ConferenceonHumanFactorsinComputingSystems, ’92, 373–380, 1992.
|             |     |               |            |     |      | CHI                | pages |                             | New York, | NY, | USA, |     |
| ----------- | --- | ------------- | ---------- | --- | ---- | ------------------ | ----- | --------------------------- | --------- | --- | ---- | --- |
|             |     |               |            |     |      | 978-0-89791-513-7. |       | doi: 10.1145/142750.142834. |           |     |      |     |
| Association |     | for Computing | Machinery. |     | ISBN |                    |       |                             |           |     |      | URL |
https://dl.acm.org/doi/10.1145/142750.142834.
NIST.AIRiskManagementFramework: AIRMF(1.0).TechnicalReportNISTAI100-1,NationalInstitute
ofStandardsandTechnology,Gaithersburg,MD,2023. URLhttps://nvlpubs.nist.gov/nistpubs/ai
/NIST.AI.100-1.pdf.
Mahsan Nourani, Chiradeep Roy, Jeremy E Block, Donald R Honeycutt, Tahrima Rahman, Eric Ragan,
andVibhavGogate. AnchoringBiasAffectsMentalModelFormationandUserRelianceinExplainable
AI Systems. In26thInternationalConferenceonIntelligentUserInterfaces, pages 340–350, New York, NY,
| USA,2021.AssociationforComputingMachinery. |     |     |     |     |     | ISBN978-1-4503-8017-1. |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
URLhttps://doi.org/10
.1145/3397481.3450639.
Brendan Nyhan and Jason Reifler. When corrections fail: The persistence of political misperceptions.
PoliticalBehavior,32(2):303–330,2010.ISSN1573-6687.doi: 10.1007/s11109-010-9112-2.Place: Germany
| Publisher: |     | Springer. |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
JonathanA.Obar. Sunlightaloneisnotadisinfectant: ConsentandthefutilityofopeningBigDatablack
|       |          |              |     |      |            | 7(1):2053951720935615, |     |         | 2020. |      | 2053-9517. |     |
| ----- | -------- | ------------ | --- | ---- | ---------- | ---------------------- | --- | ------- | ----- | ---- | ---------- | --- |
| boxes | (without | assistance). | Big | Data | & Society, |                        |     | January |       | ISSN |            |     |
doi: 10.1177/2053951720935615. URL https://doi.org/10.1177/2053951720935615. Publisher:
SAGEPublicationsLtd.
HeatherL.O’BrienandElaineG.Toms. Whatisuserengagement? Aconceptualframeworkfordefining
user engagement with technology. JournaloftheAmericanSocietyforInformationScienceandTechnology,
59(6):938–955, 2008. ISSN 1532-2890. doi: 10.1002/asi.20801. URL https://onlinelibrary.wiley.co
https://onlinelibrary.wiley.com/doi/pdf/10.1002/asi.20801.
| m/doi/abs/10.1002/asi.20801. |     |     |     | _eprint: |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |

bibliography 281
OECD. Recommendation of the Council on Artificial Intelligence. Technical report, OECD, May 2019.
URLhttps://legalinstruments.oecd.org/en/instruments/oecd-legal-0449.
OECD. Transparency and explainability (OECD AI Principle) - OECD.AI, 2019. URL https://oecd.ai/
en/dashboards/ai-principles/P7.
OECD. OECD Business and Finance Outlook 2021: AI in Business and Finance, Chapter 5: The use of
SupTech to enhance market supervision and integrity. OECD Business and Finance Outlook. OECD,
September2021a. ISBN978-92-64-64469-4978-92-64-70629-3978-92-64-57363-5978-92-64-76483-5. doi:
10.1787/ba682899-en. URL https://www.oecd-ilibrary.org/finance-and-investment/oecd-busin
ess-and-finance-outlook-2021_ba682899-en.
OECD. Risk-based regulation. In OECD Regulatory Policy Outlook 2021. OECD, October 2021b. ISBN
978-92-64-94868-6 978-92-64-80247-6 978-92-64-87415-2 978-92-64-52892-5. doi: 10.1787/9d082a11-en.
URL https://www.oecd-ilibrary.org/governance/oecd-regulatory-policy-outlook-2021_9d082a
11-en.
Jeroen Ooge. Explaining Artificial Intelligence With Tailored Interactive Visualisations. PhD thesis, October
2023.
JeroenOoge,ShotalloKato,andKatrienVerbert. ExplainingRecommendationsinE-Learning: Effectson
Adolescents’ Trust. In 27th International Conference on Intelligent User Interfaces, IUI ’22, pages 93–105,
NewYork,NY,USA,March2022.AssociationforComputingMachinery. ISBN978-1-4503-9144-3. doi:
10.1145/3490099.3511140. URLhttps://doi.org/10.1145/3490099.3511140.
Antti Oulasvirta, Jussi P. P. Jokinen, and Andrew Howes. Computational Rationality as a Theory of
Interaction. In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems, CHI ’22,
pages1–14,NewYork,NY,USA,2022.AssociationforComputingMachinery. ISBN978-1-4503-9157-3.
doi: 10.1145/3491102.3517739. URLhttps://dl.acm.org/doi/10.1145/3491102.3517739.
ErikOverrein. Howmachinelearningcandramaticallyreducefinancialinstitutions’costofcompliance,
May 2020. URL https://www.bearingpoint.com/en-no/insights-events/insights/machine-learn
ing-is-the-key-to-efficient-and-effective-aml/. Accessed8/27/2023.
HeatherO’BrienandPaulCairns. AnempiricalevaluationoftheUserEngagementScale(UES)inonline
news environments. Information Processing & Management, 51(4):413–427, July 2015. ISSN 0306-4573.
doi: 10.1016/j.ipm.2015.03.003. URLhttps://www.sciencedirect.com/science/article/pii/S03064
57315000412.
Heather L. O’Brien, Paul Cairns, and Mark Hall. A practical approach to measuring user engagement
withtherefineduserengagementscale(UES)andnewUESshortform. InternationalJournalofHuman-
ComputerStudies,112:28–39,April2018. ISSN1071-5819. doi: 10.1016/j.ijhcs.2018.01.004. URLhttps:
//www.sciencedirect.com/science/article/pii/S1071581918300041.
Matthew J Page, Joanne E McKenzie, Patrick M Bossuyt, Isabelle Boutron, Tammy C Hoffmann, Cyn-
thia D Mulrow, Larissa Shamseer, Jennifer M Tetzlaff, Elie A Akl, Sue E Brennan, and others. The
PRISMA2020statement: anupdatedguidelineforreportingsystematicreviews. Systematicreviews,10
(1):1–11,2021. Publisher: BioMedCentral.
Cecilia Panigutti, Andrea Beretta, Daniele Fadda, Fosca Giannotti, Dino Pedreschi, Alan Perotti, and
Salvatore Rinzivillo. Co-design of Human-centered, Explainable AI for Clinical Decision Support.
ACM Transactions on Interactive Intelligent Systems, 13(4):21:1–21:35, 2023a. ISSN 2160-6455. doi:
10.1145/3587271. URLhttps://dl.acm.org/doi/10.1145/3587271.
CeciliaPanigutti,RonanHamon,IsabelleHupont,DavidFernandezLlorca,DeliaFanoYela,HenrikJun-
klewitz, Salvatore Scalzo, Gabriele Mazzini, Ignacio Sanchez, Josep Soler Garrido, and Emilia Gomez.
TheroleofexplainableAIinthecontextoftheAIAct. In2023ACMConferenceonFairness,Accountabil-
ity,andTransparency, pages 1139–1150, Chicago IL USA, June 2023b. ACM. ISBN 9798400701924. doi:
10.1145/3593013.3594069. URLhttps://dl.acm.org/doi/10.1145/3593013.3594069.

| 282 the | explanation |     |     | paradox | and the | human | centric | path |     |     |     |
| ------- | ----------- | --- | --- | ------- | ------- | ----- | ------- | ---- | --- | --- | --- |
-
Raja Parasuraman and Dietrich H. Manzey. Complacency and Bias in Human Use of Automa-
tion: An Attentional Integration. Human Factors, 52(3):381–410, June 2010. ISSN 0018-7208. doi:
10.1177/0018720810376055. URL https://doi.org/10.1177/0018720810376055. Publisher: SAGE
PublicationsInc.
Raja Parasuraman and Victor Riley. Humans and Automation: Use, Misuse, Disuse, Abuse. Human
Factors, 39(2):230–253, June 1997. ISSN 0018-7208. URL https://doi.org/10.1518/0018720977785438
| 86. Publisher: |     | SAGEPublicationsInc. |     |     |     |     |     |     |     |     |     |
| -------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Raja Parasuraman, Robert Molloy, and Indramani Singh. Performance Consequences of Automation
InducedComplacency. InternationalJournalofAviationPsychology,3,February1993.
HyangheePark,DaehwanAhn,KartikHosanagar,andJoonhwanLee. Human-AIInteractioninHuman
Resource Management: Understanding Why Employees Resist Algorithmic Evaluation at Workplaces
andHowtoMitigateBurdens. InProceedingsofthe2021CHIConferenceonHumanFactorsinComputing
Systems,CHI’21,pages1–15,NewYork,NY,USA,2021.AssociationforComputingMachinery. ISBN
| 978-1-4503-8096-6. |     | doi: | 10.1145/3411764.3445304. |     |     |     |     |     |     |     |     |
| ------------------ | --- | ---- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
URLhttps://doi.org/10.1145/3411764.3445304.
Frank Pasquale. TheBlackBoxSociety: TheSecretAlgorithmsThatControlMoneyandInformation. Harvard
UniversityPress,2015. ISBN978-0-674-36827-9. URLhttps://www.jstor.org/stable/j.ctt13x0hch.
Paul Fehlinger. Enabling the responsible use of technology at scale. Technical report, SITRA, October
2023.
URL https://www.sitra.fi/en/publications/enabling-the-responsible-use-of-technolog
y-at-scale/.
PaulThagard. Explanatorycoherence. Behavioralandbrainsciences,12:435–502,1989.
Georgios Pavlidis. Deploying artificial intelligence for anti-money laundering and asset recovery: the
|     |     |     |     |     |     |     | 26(7):155–166, |     | 2023. | 1368-5201. |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ---------- | --- |
dawn of a new era. Journal of Money Laundering Control, January ISSN
doi: 10.1108/JMLC-03-2023-0050. URL https://doi.org/10.1108/JMLC-03-2023-0050. Publisher:
EmeraldPublishingLimited.
Sean Penney, Jonathan Dodge, Claudia Hilderbrand, Andrew Anderson, Logan Simpson, and Margaret
Burnett. TowardForagingforUnderstandingofStarCraftAgents: AnEmpiricalStudy. In23rdInterna-
tionalConferenceonIntelligentUserInterfaces, IUI ’18, pages 225–237, New York, NY, USA, March 2018.
|             |     |               |     |            |      | 978-1-4503-4945-1. |     | doi: 10.1145/3172944.3172946. |     |     |     |
| ----------- | --- | ------------- | --- | ---------- | ---- | ------------------ | --- | ----------------------------- | --- | --- | --- |
| Association |     | for Computing |     | Machinery. | ISBN |                    |     |                               |     |     | URL |
https://doi.org/10.1145/3172944.3172946.
Nancy Pennington and Reid Hastie. Reasoning in explanation-based decision making. Cognition, 49(1):
| 123–163, |         | 1993. |      | 0010-0277. | doi: | 10.1016/0010-0277(93)90038-W. |     |     |                      |     |     |
| -------- | ------- | ----- | ---- | ---------- | ---- | ----------------------------- | --- | --- | -------------------- | --- | --- |
|          | October |       | ISSN |            |      |                               |     |     | URL https://www.scie |     |     |
ncedirect.com/science/article/pii/001002779390038W.
Jonas Peters, Dominik Janzing, and Bernhard Schlkopf. Elements of Causal Inference: Foundations and
| LearningAlgorithms. |     |     | TheMITPress,October2017. |     |     |     | ISBN978-0-262-03731-0. |     |     |     |     |
| ------------------- | --- | --- | ------------------------ | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
Lawrence D. Phillips and Ward Edwards. Conservatism in a simple probability inference task. Journal
|                 |                                   |             |     | 72(3):346–354, | 1966. |      | 0022-1015. | doi: 10.1037/h0023653. |     |        |     |
| --------------- | --------------------------------- | ----------- | --- | -------------- | ----- | ---- | ---------- | ---------------------- | --- | ------ | --- |
| of Experimental |                                   | Psychology, |     |                |       | ISSN |            |                        |     | Place: | US  |
| Publisher:      | AmericanPsychologicalAssociation. |             |     |                |       |      |            |                        |     |        |     |
Sayantan Polley, Suhita Ghosh, Marcus Thiel, Michael Kotzyba, and Andreas Nürnberger. SIMFIC: An
Explainable Book Search Companion. In 2020IEEEInternationalConferenceonHuman-MachineSystems
(ICHMS),pages1–6,September2020. doi: 10.1109/ICHMS49158.2020.9209581.
David Poole, Randy Goebel, and Romas Aleliunas. Theorist: A Logical Reasoning System for Defaults
InTheKnowledgeFrontier,pages331–352.SpringerNewYork,NewYork,NY,1987.
andDiagnosis.
Harry E. Pople. On the mechanization of abductive logic. In Proceedings of the 3rd international joint
conference on Artificial intelligence, IJCAI’73, pages 147–152, San Francisco, CA, USA, 1973. Morgan
KaufmannPublishersInc.

bibliography 283
Forough Poursabzi-Sangdeh, Daniel G. Goldstein, Jake M. Hofman, Jennifer Wortman Vaughan, and
HannaWallach. ManipulatingandMeasuringModelInterpretability. arXiv:1802.07810[cs],November
2019. URLhttp://arxiv.org/abs/1802.07810. arXiv: 1802.07810.
ForoughPoursabzi-Sangdeh,SamiraSamadi,JenniferWortmanVaughan,andHannaWallach. AHuman
intheLoopisNotEnough: TheNeedforHuman-SubjectExperimentsinFacialRecognition.May2020.
URL https://www.microsoft.com/en-us/research/publication/a-human-in-the-loop-is-not-eno
ugh-the-need-for-human-subject-experiments-in-facial-recognition/.
AimeePrawitz,E.ThomasGarman,BenoitSorhaindo,BarbaraO’Neill,JinheeKim,andPatriciaDrentea.
Incharge Financial Distress/Financial Well-Being Scale: Development, Administration, and Score In-
terpretation,2006. URLhttps://papers.ssrn.com/abstract=2239338.
Garima Pruthi, Frederick Liu, Satyen Kale, and Mukund Sundararajan. Estimating Training Data In-
fluence by Tracing Gradient Descent. In Advances in Neural Information Processing Systems, volume 33,
pages 19920–19930. Curran Associates, Inc., 2020. URL https://proceedings.neurips.cc/paper/202
0/hash/e6385d39ec9394f2f3a354d9d2b88eec-Abstract.html.
Inioluwa Deborah Raji and Joy Buolamwini. Actionable Auditing: Investigating the Impact of Publicly
NamingBiasedPerformanceResultsofCommercialAIProducts. InProceedingsofthe2019AAAI/ACM
ConferenceonAI,Ethics,andSociety, pages 429–435, Honolulu HI USA, January 2019. ACM. ISBN 978-
1-4503-6324-2. doi: 10.1145/3306618.3314244. URL https://dl.acm.org/doi/10.1145/3306618.331
4244.
InioluwaDeborahRaji,AndrewSmart,RebeccaN.White,MargaretMitchell,TimnitGebru,BenHutchin-
son, Jamila Smith-Loud, Daniel Theron, and Parker Barnes. Closing the AI accountability gap: defin-
ing an end-to-end framework for internal algorithmic auditing. In Proceedings of the 2020 Conference
on Fairness, Accountability, and Transparency, pages 33–44, Barcelona Spain, January 2020. ACM. ISBN
978-1-4503-6936-7. doi: 10.1145/3351095.3372873. URLhttps://dl.acm.org/doi/10.1145/3351095.3
372873.
Gabriëlle Ras, Marcel van Gerven, and Pim Haselager. Explanation Methods in Deep Learning: Users,
Values,ConcernsandChallenges. InHugoJairEscalante,SergioEscalera,IsabelleGuyon,XavierBaró,
Yag˘mur Güçlütürk, Umut Güçlü, and Marcel van Gerven, editors, Explainable and Interpretable Models
in Computer Vision and Machine Learning, The Springer Series on Challenges in Machine Learning,
pages 19–36. Springer International Publishing, Cham, 2018. ISBN 978-3-319-98131-4. URL https:
//doi.org/10.1007/978-3-319-98131-4_2.
CharviRastogi,YunfengZhang,DennisWei,KushR.Varshney,AmitDhurandhar,andRichardTomsett.
DecidingFastandSlow: TheRoleofCognitiveBiasesinAI-assistedDecision-making. arXiv:2010.07938
[cs],October2020. URLhttp://arxiv.org/abs/2010.07938. arXiv: 2010.07938.
Stephen J. Read and Amy Marcus-Newhall. Explanatory coherence in social explanations: A parallel
distributed processing account. Journal of Personality and Social Psychology, 65(3):429–447, 1993. ISSN
1939-1315. doi: 10.1037/0022-3514.65.3.429. Place: USPublisher: AmericanPsychologicalAssociation.
Juan Rebanal, Jordan Combitsis, Yuqi Tang, and Xiang ’Anthony’ Chen. XAlgo: a Design Probe of
Explaining Algorithms’ Internal States via Question-Answering. In 26th International Conference on
IntelligentUserInterfaces,IUI’21,pages329–339,NewYork,NY,USA,2021.AssociationforComputing
Machinery. ISBN 978-1-4503-8017-1. doi: 10.1145/3397481.3450676. URL https://doi.org/10.1145/
3397481.3450676.
Chris Reed. How should we regulate artificial intelligence? Philosophical Transactions of the Royal
Society A: Mathematical, Physical and Engineering Sciences, 376(2128):20170360, August 2018. doi:
10.1098/rsta.2017.0360. URL https://royalsocietypublishing.org/doi/10.1098/rsta.2017.0360.
Publisher: RoyalSociety.
Bob Rehder. When similarity and causality compete in category-based property generalization. Memory
&Cognition,34(1):3–16,January2006. ISSN0090-502X. doi: 10.3758/bf03193382.

| 284 the | explanation | paradox | and the human | centric | path |     |     |
| ------- | ----------- | ------- | ------------- | ------- | ---- | --- | --- |
-
DentM.RhodesandJanetWhiteAzbell. DesigningInteractiveVideoInstructionProfessionally. Training
andDevelopmentJournal,39(12):31–33,1985.
Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. "Why Should I Trust You?": Explaining the
PredictionsofAnyClassifier. InProceedingsofthe22ndACMSIGKDDInternationalConferenceonKnowl-
|     |     |     | ’16, 1135–1144, |     |     |     | 2016. |
| --- | --- | --- | --------------- | --- | --- | --- | ----- |
edge Discovery and Data Mining, KDD pages New York, NY, USA, August As-
|           |               |            | 978-1-4503-4232-2. | doi: | 10.1145/2939672.2939778. |     |     |
| --------- | ------------- | ---------- | ------------------ | ---- | ------------------------ | --- | --- |
| sociation | for Computing | Machinery. | ISBN               |      |                          |     | URL |
https://doi.org/10.1145/2939672.2939778.
Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. Anchors: High-Precision Model-Agnostic
|     |     |     |     |     | 32(1), | 2018. | 2374- |
| --- | --- | --- | --- | --- | ------ | ----- | ----- |
Explanations. Proceedings of the AAAI Conference on Artificial Intelligence, April ISSN
| 3468. |     |     |     |     |     | 1.  |     |
| ----- | --- | --- | --- | --- | --- | --- | --- |
URLhttps://ojs.aaai.org/index.php/AAAI/article/view/11491. Number:
Mireia Ribera and Agata Lapedriza. Can we do better explanations? A proposal of User-Centered
| ExplainableAI. | LosAngeles,page7,2019. |     |     |     |     |     |     |
| -------------- | ---------------------- | --- | --- | --- | --- | --- | --- |
YvonneRogers,HelenSharp,andJennyPreece. InteractionDesign: beyondhuman-computerinteraction(6th
edition). John Wiley & Sons, March 2023. ISBN 978-1-119-90109-9. URL https://oro.open.ac.uk/887
58/.
Katharina J. Rohlfing, Philipp Cimiano, Ingrid Scharlau, Tobias Matzner, Heike M. Buhl, Hen-
drik Buschmeier, Elena Esposito, Angela Grimminger, Barbara Hammer, Reinhold Häb-Umbach,
Ilona Horwath, Eyke Hüllermeier, Friederike Kern, Stefan Kopp, Kirsten Thommes, Axel-Cyrille
Ngonga Ngomo, Carsten Schulte, Henning Wachsmuth, Petra Wagner, and Britta Wrede. Explana-
tion as a Social Practice: Toward a Conceptual Framework for the Social Design of AI Systems. IEEE
Transactions on Cognitive and Developmental Systems, 13(3):717–728, September 2021. ISSN 2379-8939.
doi: 10.1109/TCDS.2020.3044366.
|           |                                                     |     | URL https://ieeexplore.ieee.org/document/9292993. |     |     |     | Confer- |
| --------- | --------------------------------------------------- | --- | ------------------------------------------------- | --- | --- | --- | ------- |
| enceName: | IEEETransactionsonCognitiveandDevelopmentalSystems. |     |                                                   |     |     |     |         |
Avi Rosenfeld and Ariella Richardson. Explainability in human–agent systems. Autonomous Agents and
Multi-AgentSystems,33(6):673–705,November2019. ISSN1573-7454. doi: 10.1007/s10458-019-09408-y.
URLhttps://doi.org/10.1007/s10458-019-09408-y.
Andrew Ross, Nina Chen, Elisa Zhao Hang, Elena L. Glassman, and Finale Doshi-Velez. Evaluating
the Interpretability of Generative Models by Interactive Reconstruction. In Proceedings of the 2021 CHI
ConferenceonHumanFactorsinComputingSystems,pages1–15,YokohamaJapan,May2021.ACM. ISBN
| 978-1-4503-8096-6. | doi: | 10.1145/3411764.3445296. |     |     |     |     |     |
| ------------------ | ---- | ------------------------ | --- | --- | --- | --- | --- |
URLhttps://dl.acm.org/doi/10.1145/3411764.3
445296.
Mary Beth Rosson and John M. Carroll. Scenario-based design. In Human-computer Interaction,
page 20. CRC Press, Boca Raton, 1st edition edition, March 2009. ISBN 978-0-429-13939-0. doi:
10.1201/9781420088892-14.
URL https://www.taylorfrancis.com/chapters/edit/10.1201/9781
161-180
420088892-14/scenario-based-design-mary-beth-rosson-john-carroll. Pages: Publica-
| tionTitle: | Human-ComputerInteraction. |     |     |     |     |     |     |
| ---------- | -------------------------- | --- | --- | --- | --- | --- | --- |
Paul A. Roth. How Narratives Explain. Social Research, 56(2):449–478, 1989. ISSN 0037-783X. URL
| https://www.jstor.org/stable/40970551. |     |     | Publisher: | TheNewSchool. |     |     |     |
| -------------------------------------- | --- | --- | ---------- | ------------- | --- | --- | --- |
Steven F. Roth and Joe Mattis. Data characterization for intelligent graphics presentation. In Proceed-
|     |     |     |     |     | ’90, | 193–200, |     |
| --- | --- | --- | --- | --- | ---- | -------- | --- |
ings of the SIGCHI Conference on Human Factors in Computing Systems, CHI pages New
York, NY, USA, March 1990. Association for Computing Machinery. ISBN 978-0-201-50932-8. doi:
| 10.1145/97243.97273. |     | URLhttps://doi.org/10.1145/97243.97273. |     |     |     |     |     |
| -------------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
Denise M. Rousseau, Sim B. Sitkin, Ronald S. Burt, and Colin Camerer. Introduction to Special Topic
Forum: Not so Different after All: A Cross-Discipline View of Trust. The Academy of Management
Review,23(3):393–404,1998.
URLhttp://www.jstor.org/stable/259285.
Maria Roussou. Learning by doing and learning through play: an exploration of interactivity
in virtual environments for children. Computers in Entertainment, 2(1):10, January 2004. doi:
10.1145/973801.973818.
URLhttps://doi.org/10.1145/973801.973818.

|     |     |     |     |     |     |     |     | bibliography |     | 285 |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- |
AntoinetteRouvroy. Theend(s)ofcritique: Databehaviourismversusdueprocess. InPrivacyDueProcess
and the Computational Turn: The Philosophy of Law Meets the Philosophy of Technology, pages 143–167.
Taylor & Francis, 2013. ISBN 978-0-203-42764-4. doi: 10.4324/9780203427644. URL
http://www.scop
us.com/inward/record.url?scp=84917399654&partnerID=8YFLogxK.
Hofit Wasserman Rozen, Niva Elkin-Koren, and Ran Gilad-Bachrach. The Case Against Explainability,
| May2023. | URLhttp://arxiv.org/abs/2305.12167. |     |     |     | arXiv:2305.12167[cs]. |     |     |     |     |     |
| -------- | ----------------------------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- |
Cynthia Rudin. Stop explaining black box machine learning models for high stakes decisions and use
|     |     |     |     | NatureMachineIntelligence,1(5):206–215,May2019. |     |     |     | ISSN2522-5839. |     | doi: |
| --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | -------------- | --- | ---- |
interpretablemodelsinstead.
10.1038/s42256-019-0048-x. URLhttps://www.nature.com/articles/s42256-019-0048-x. Number: 5
| Publisher: | NaturePublishingGroup. |     |     |     |     |     |     |     |     |     |
| ---------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2010.
| StuartJRussellandPeterNorvig. |     |     |     | Artificialintelligenceamodernapproach. |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- |
ChristianSandvig,KevinHamilton,K.Karahalios,andCédricLangbort. AuditingAlgorithms: Research
Methods for Detecting Discrimination on Internet Platforms. In Preconference at the 64th Annual Meet-
ing of the International Communication Association, page 23, Seattle, WA, USA, May 2014. University of
Michigan.
JamesSchaffer,PrasannaGiridhar,DebraJones,TobiasHöllerer,TarekAbdelzaher,andJohnO’Donovan.
Getting the Message? A Study of Explanation Interfaces for Microblog Data Analysis. In Pro-
|     |     |     |     |     |     |     |     | ’15, | 345–356, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------- | --- |
ceedings of the 20th International Conference on Intelligent User Interfaces, IUI pages New
|     |     |     | 2015. |     |     |     |     | 978-1-4503-3306-1. |     | doi: |
| --- | --- | --- | ----- | --- | --- | --- | --- | ------------------ | --- | ---- |
York, NY, USA, March Association for Computing Machinery. ISBN
10.1145/2678025.2701406. URLhttps://doi.org/10.1145/2678025.2701406.
JamesSchaffer,JohnO’Donovan,JamesMichaelis,AdrienneRaglin,andTobiasHöllerer. Icandobetter
thanyourAI:expertiseandexplanations. InProceedingsofthe24thInternationalConferenceonIntelligent
User Interfaces, IUI ’19, pages 240–251, New York, NY, USA, March 2019. Association for Computing
|            |      | 978-1-4503-6272-6. |     | doi: | 10.1145/3301275.3302308. |     |     |                          |     |     |
| ---------- | ---- | ------------------ | --- | ---- | ------------------------ | --- | --- | ------------------------ | --- | --- |
| Machinery. | ISBN |                    |     |      |                          |     | URL | https://doi.org/10.1145/ |     |     |
3301275.3302308.
|           |          |        |          |          |             | 47(4):633–659, | 1995. |      | 0038-9765. | doi: |
| --------- | -------- | ------ | -------- | -------- | ----------- | -------------- | ----- | ---- | ---------- | ---- |
| Frederick | Schauer. | Giving | Reasons. | Stanford | Law Review, |                |       | ISSN |            |      |
10.2307/1229080. URLhttps://www.jstor.org/stable/1229080. Publisher: StanfordLawReview.
Frederick Schauer. Transparency in Three Dimensions. University of IllinoisLaw Review, 2011:1339, 2011.
URLhttps://heinonline.org/HOL/Page?handle=hein.journals/unilllr2011&id=1347&div=&collec
tion=.
KaraSchick-Makaroff,MarjorieMacDonald,MarilynPlummer,JudyBurgess,andWendyNeander.What
Synthesis Methodology Should I Use? A Review and Analysis of Approaches to Research Synthesis.
3(1):172–215, 2016. 2327-8994. doi: 10.3934/publichealth.2016.1.172.
| AIMS public | health, |     |     | March | ISSN |     |     |     |     |     |
| ----------- | ------- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- |
URLhttps://www.ncbi.nlm.nih.gov/pmc/articles/PMC5690272/.
JohanesSchneiderandJoshuaHandali. Personalizedexplanationinmachinelearning: Aconceptualiza-
2019,
tion. In Proceedings of the European Conference on Information Systems, ECIS Stockholm-Uppsala,
Sweden, June 2019. arXiv. doi: 10.48550/arXiv.1901.00770. URL https://aisel.aisnet.org/ecis201
| 9_rp/171. | arXiv:1901.00770[cs,stat]. |     |     |     |     |     |     |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
15(1):60–82,
Jonas Schuett. Defining the scope of AI regulations. Law, InnovationandTechnology, January
| 2023. | 1757-9961. |     | doi: | 10.1080/17579961.2023.2184135. |     |     |                                |     |     |     |
| ----- | ---------- | --- | ---- | ------------------------------ | --- | --- | ------------------------------ | --- | --- | --- |
| ISSN  |            |     |      |                                |     | URL | https://doi.org/10.1080/175799 |     |     |     |
61.2023.2184135. Publisher: Routledge_eprint: https://doi.org/10.1080/17579961.2023.2184135.
RichardSchwierandEarlR.Misanchuk. InteractiveMultimediaInstruction. EducationalTechnology,1993.
ISBN978-0-87778-251-3.
Abigail See, Stephen Roller, Douwe Kiela, and Jason Weston. What makes a good conversation? How
controllable attributes affect human judgments, April 2019. URL http://arxiv.org/abs/1902.08654.
arXiv:1902.08654[cs].

| 286 | the | explanation |     |     | paradox | and | the | human | centric |     | path |     |     |
| --- | --- | ----------- | --- | --- | ------- | --- | --- | ----- | ------- | --- | ---- | --- | --- |
-
2018.
Andrew D. Selbst and Solon Barocas. The Intuitive Appeal of Explainable Machines, March URL
https://papers.ssrn.com/abstract=3126971.
Rita Sevastjanova, Wolfgang Jentner, Fabian Sperrle, Rebecca Kehlbeck, Jürgen Bernard, and Men-
natallah El-assady. QuestionComb: A Gamification Approach for the Visual Explanation of Lin-
guistic Phenomena through Interactive Labeling. ACM Transactions on Interactive Intelligent Systems,
11(3-4):1–38, December 2021. ISSN 2160-6455, 2160-6463. doi: 10.1145/3429448. URL
https:
//dl.acm.org/doi/10.1145/3429448.
Patrick Shafto and John D. Coley. Development of categorization and reasoning in the natural world:
novicestoexperts,naivesimilaritytoecologicalknowledge. JournalofExperimentalPsychology.Learning,
Memory,andCognition,29(4):641–649,July2003. ISSN0278-7393. doi: 10.1037/0278-7393.29.4.641.
Lei Shi, Zhiyang Teng, Le Wang, Yue Zhang, and Alexander Binder. DeepClue: Visual Interpretation of
Text-BasedDeepStockPrediction.IEEETransactionsonKnowledgeandDataEngineering,31(6):1094–1108,
|      | 2019. |      | 1558-2191. |     | doi: | 10.1109/TKDE.2018.2854193. |     |     |     |            |       |                   |     |
| ---- | ----- | ---- | ---------- | --- | ---- | -------------------------- | --- | --- | --- | ---------- | ----- | ----------------- | --- |
| June |       | ISSN |            |     |      |                            |     |     |     | Conference | Name: | IEEE Transactions |     |
onKnowledgeandDataEngineering.
AsayaShimojo,KazuhisaMiwa,andHitoshiTerai. HowDoesExplanatoryVirtueDetermineProbability
11, 2020.
Estimation?—Empirical Discussion on Effect of Instruction. Frontiers in Psychology, ISSN
1664-1078. URLhttps://www.frontiersin.org/article/10.3389/fpsyg.2020.575746.
Dajung Diane Shin and Sung-il Kim. Homo Curious: Curious or Interested? Educational Psychology
Review,31(4):853–874,December2019. ISSN1573-336X. doi: 10.1007/s10648-019-09497-x.
URLhttps:
//doi.org/10.1007/s10648-019-09497-x.
Donghee Shin. The effects of explainability and causability on perception, trust, and acceptance: Impli-
|     |     |     |     |     |     |     |     |     |     |     | 146:102551, |     | 2021. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- |
cations for explainable AI. InternationalJournalofHuman-ComputerStudies, February
|      | 1071-5819. |     | doi: | 10.1016/j.ijhcs.2020.102551. |     |     |     |     |                                          |     |     |     |     |
| ---- | ---------- | --- | ---- | ---------------------------- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
| ISSN |            |     |      |                              |     |     |     | URL | https://www.sciencedirect.com/science/ar |     |     |     |     |
ticle/pii/S1071581920301531.
Ben Shneiderman. Bridging the Gap Between Ethics and Practice: Guidelines for Reliable, Safe, and
10(4):
Trustworthy Human-centered AI Systems. ACM Transactions on Interactive Intelligent Systems,
26:1–26:31, October 2020. ISSN 2160-6455. doi: 10.1145/3419764. URL https://dl.acm.org/doi/10.
1145/3419764.
Auste Simkute, Ewa Luger, Mike Evans, and Rhianne Jones. Experts in the Shadow of Algorithmic
Systems: Exploring Intelligibility in a Decision-Making Context. In Companion Publication of the 2020
ACMDesigningInteractiveSystemsConference,DIS’20Companion,pages263–268,NewYork,NY,USA,
| 2020. |             |     |     |           |     |            |      | 978-1-4503-7987-8. |     |     | doi: 10.1145/3393914.3395862. |     |     |
| ----- | ----------- | --- | --- | --------- | --- | ---------- | ---- | ------------------ | --- | --- | ----------------------------- | --- | --- |
|       | Association |     | for | Computing |     | Machinery. | ISBN |                    |     |     |                               |     |     |
URLhttps://doi.org/10.1145/3393914.3395862.
|     |     |     |     |     |     |     |     |     |     |     | 7(1-3):1–15, |     | 2000. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- |
Daniel J. Simons. Current Approaches to Change Blindness. Visual Cognition, January
|            | 1350-6285. |                   | doi: | 10.1080/135062800394658. |                                          |     |     |     |                                          |     |     |     |     |
| ---------- | ---------- | ----------------- | ---- | ------------------------ | ---------------------------------------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
| ISSN       |            |                   |      |                          |                                          |     |     | URL | https://doi.org/10.1080/135062800394658. |     |     |     |     |
| Publisher: |            | Routledge_eprint: |      |                          | https://doi.org/10.1080/135062800394658. |     |     |     |                                          |     |     |     |     |
Karen Simonyan, Andrea Vedaldi, and Andrew Zisserman. Deep Inside Convolutional Networks: Visu-
alisingImageClassificationModelsandSaliencyMaps,April2014.
URLhttp://arxiv.org/abs/1312
| .6034.     |       | arXiv:1312.6034[cs]. |                                |     |           |           |     |     |       |           |                |       |      |
| ---------- | ----- | -------------------- | ------------------------------ | --- | --------- | --------- | --- | --- | ----- | --------- | -------------- | ----- | ---- |
|            |       |                      |                                |     |           | Computers |     | in  | Human | Behavior, | 13(2):157–180, | 1997. |      |
| Rod        | Sims. | Interactivity:       |                                | A   | forgotten | art?      |     |     |       |           |                | May   | ISSN |
| 0747-5632. |       | doi:                 | 10.1016/S0747-5632(97)00004-6. |     |           |           |     |     |       |           |                |       |      |
URLhttps://www.sciencedirect.com/science/arti
cle/pii/S0747563297000046.
RadishSingh,MiguelFernandes,NickLim,andEricAng. Thecaseforartificialintelligenceincombating
2018.
money laundering and terrorist financing. Technical report, Deloitte, URL https://www2.deloi
tte.com/mm/en/pages/financial-advisory/articles/the-case-for-artificial-intelligence-i
n-combating-money-laundering-and-terrorist-financing.html.

bibliography 287
Frédérique Six. Trust in Regulatory Relations. Public Management Review, 15(2):163–185, February 2013.
ISSN 1471-9037. doi: 10.1080/14719037.2012.727461. URL https://doi.org/10.1080/14719037.201
2.727461. Publisher: Routledge_eprint: https://doi.org/10.1080/14719037.2012.727461.
Dylan Slack, Anna Hilgard, Sameer Singh, and Himabindu Lakkaraju. Reliable Post hoc Explanations:
ModelingUncertaintyinExplainability.InAdvancesinNeuralInformationProcessingSystems,volume34,
pages 9391–9404. Curran Associates, Inc., 2021. URL https://proceedings.neurips.cc/paper_files
/paper/2021/hash/4e246a381baf2ce038b3b0f82c7d6fb4-Abstract.html.
Dylan Slack, Satyapriya Krishna, Himabindu Lakkaraju, and Sameer Singh. TalkToModel: Explaining
Machine Learning Models with Interactive Natural Language Conversations, September 2022. URL
http://arxiv.org/abs/2207.04154. arXiv:2207.04154[cs].
Nathalie A. Smuha. From a ‘race to AI’ to a ‘race to AI regulation’: regulatory competition for arti-
ficial intelligence. Law, Innovation and Technology, 13(1):57–84, January 2021. ISSN 1757-9961. doi:
10.1080/17579961.2021.1898300. URL https://doi.org/10.1080/17579961.2021.1898300. Publisher:
Routledge_eprint: https://doi.org/10.1080/17579961.2021.1898300.
DominicS.B.SohandNonnaMartinov-Bennie. Theinternalauditfunction: Perceptionsofinternalaudit
roles, effectiveness and evaluation. Managerial Auditing Journal, 26(7):605–622, January 2011. ISSN
0268-6902. doi: 10.1108/02686901111151332. URL https://doi.org/10.1108/02686901111151332.
Publisher: EmeraldGroupPublishingLimited.
Kacper Sokol and Peter Flach. Explainability fact sheets: a framework for systematic assessment
of explainable approaches. In Proceedings of the 2020 Conference on Fairness, Accountability, and
Transparency, pages 56–67, Barcelona Spain, January 2020. ACM. ISBN 978-1-4503-6936-7. doi:
10.1145/3351095.3372870. URLhttp://dl.acm.org/doi/10.1145/3351095.3372870.
Francesco Sovrano and Fabio Vitali. From Philosophy to Interfaces: an Explanatory Method and a Tool
Inspired by Achinstein’s Theory of Explanation. In 26th International Conference on Intelligent User
Interfaces, pages 81–91, College Station TX USA, April 2021. ACM. ISBN 978-1-4503-8017-1. doi:
10.1145/3397481.3450655. URLhttps://dl.acm.org/doi/10.1145/3397481.3450655.
Thilo Spinner, Udo Schlegel, Hanna Schäfer, and Mennatallah El-Assady. explAIner: A Visual Analytics
Framework for Interactive and Explainable Machine Learning. IEEE Transactions on Visualization and
Computer Graphics, 26(1):1064–1074, January 2020. ISSN 1941-0506. doi: 10.1109/TVCG.2019.2934629.
ConferenceName: IEEETransactionsonVisualizationandComputerGraphics.
Clay Spinuzzi. The Methodology of Participatory Design. Technical Communication, 52(2):163–174, May
2005.
JostTobiasSpringenberg,AlexeyDosovitskiy,ThomasBrox,andMartinRiedmiller. StrivingforSimplic-
ity: The All Convolutional Net, April 2015. URL http://arxiv.org/abs/1412.6806. arXiv:1412.6806
[cs].
AaronSpringerandSteveWhittaker.Progressivedisclosure: empiricallymotivatedapproachestodesign-
ingeffectivetransparency. InProceedingsofthe24thInternationalConferenceonIntelligentUserInterfaces,
IUI’19,pages107–120,NewYork,NY,USA,March2019.AssociationforComputingMachinery. ISBN
978-1-4503-6272-6. doi: 10.1145/3301275.3302322. URLhttps://doi.org/10.1145/3301275.3302322.
BrianStantonandTheodoreJensen. TrustandArtificialIntelligence. preprint,March2021. URLhttps:
//nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8332-draft.pdf.
Constantine Stephanidis, Gavriel Salvendy, Demosthenes Akoumianakis, Albert Arnold, Nigel Bevan,
DanielDardailler,PierLuigiEmiliani,IliasIakovidis,PhilJenkins,ArthurKarshmer,PeterKorn,Aaron
Marcus, Harry Murphy, Charles Oppermann, Christian Stary, Hiroshi Tamura, Manfred Tscheligi,
Hirotada Ueda, Gerhard Weber, and Juergen Ziegler. Toward an Information Society for All: HCI
Challenges and R&D Recommendations. International Journal of Human–Computer Interaction, 11(1):
1–28,January1999. ISSN1044-7318. URLhttps://doi.org/10.1207/s15327590ijhc1101_1.

| 288 the | explanation |     | paradox | and | the human | centric path |     |     |     |
| ------- | ----------- | --- | ------- | --- | --------- | ------------ | --- | --- | --- |
-
Ilia Stepin, Jose M. Alonso, Alejandro Catala, and Martín Pereira-Fariña. A Survey of Contrastive and
CounterfactualExplanationGenerationMethodsforExplainableArtificialIntelligence. IEEEAccess,9:
11974–12001,2021. ISSN2169-3536. doi: 10.1109/ACCESS.2021.3051315. URLhttps://ieeexplore.i
| eee.org/document/9321372. |     |     | ConferenceName: |     | IEEEAccess. |     |     |     |     |
| ------------------------- | --- | --- | --------------- | --- | ----------- | --- | --- | --- | --- |
Jonathan Steuer. Defining Virtual Reality: Dimensions Determining Telepresence. JournalofCommunica-
tion,pages73–93,1992.
Simone Stumpf, Vidya Rajaram, Lida Li, Weng-Keen Wong, Margaret Burnett, Thomas Dietterich, Erin
Sullivan, and Jonathan Herlocker. Interacting meaningfully with machine learning systems: Three
|     |     |     |     |     |     | 67(8):639–662, |     | 2009. | 1071- |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | ----- |
experiments. International Journal of Human-Computer Studies, August ISSN
| 5819. | doi: 10.1016/j.ijhcs.2009.03.004. |     |     |     |     |     |     |     |     |
| ----- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
URL https://www.sciencedirect.com/science/article/pii/
S1071581909000457.
Mark C. Suchman. Managing Legitimacy: Strategic and Institutional Approaches. The Academy of
|                                |         | 20(3):571–610, |     | 1995.      | 0363-7425.           | doi: 10.2307/258788. |     |     |        |
| ------------------------------ | ------- | -------------- | --- | ---------- | -------------------- | -------------------- | --- | --- | ------ |
| Management                     | Review, |                |     |            | ISSN                 |                      |     | URL | https: |
| //www.jstor.org/stable/258788. |         |                |     | Publisher: | AcademyofManagement. |                      |     |     |        |
Jiao Sun, Q. Vera Liao, Michael Muller, Mayank Agarwal, Stephanie Houde, Kartik Talamadupula,
and Justin D. Weisz. Investigating Explainability of Generative AI for Code through Scenario-based
Design. In 27th International Conference on Intelligent User Interfaces, IUI ’22, pages 212–228, New
|     |     | 2022. |     |     |     |     | 978-1-4503-9144-3. |     | doi: |
| --- | --- | ----- | --- | --- | --- | --- | ------------------ | --- | ---- |
York, NY, USA, March Association for Computing Machinery. ISBN
10.1145/3490099.3511119. URLhttps://doi.org/10.1145/3490099.3511119.
S.ShyamSundar,QianXu,andSaraswathiBellur. Designinginteractivityinmediainterfaces: acommu-
nications perspective. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems,
|     | ’10, 2247–2256, |     |     |     | 2010. |     |     |     |     |
| --- | --------------- | --- | --- | --- | ----- | --- | --- | --- | --- |
CHI pages New York, NY, USA, Association for Computing Machinery. ISBN
978-1-60558-929-9. doi: 10.1145/1753326.1753666. URLhttps://doi.org/10.1145/1753326.1753666.
AxiomaticAttributionforDeepNetworks,June2017.
MukundSundararajan,AnkurTaly,andQiqiYan.
| URLhttp://arxiv.org/abs/1703.01365. |     |     |     |     | arXiv:1703.01365[cs]. |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- |
Harry Surden. Artificial Intelligence and Law: An Overview, June 2019. URL https://papers.ssrn.co
m/abstract=3411869.
HariniSuresh,StevenR.Gomez,KevinK.Nam,andArvindSatyanarayan. BeyondExpertiseandRoles:
A Framework to Characterize the Stakeholders of Interpretable Machine Learning and their Needs.
In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems, CHI ’21, pages 1–
16, New York, NY, USA, 2021. Association for Computing Machinery. ISBN 978-1-4503-8096-6. doi:
10.1145/3411764.3445088.
URLhttps://doi.org/10.1145/3411764.3445088.
Harini Suresh, Kathleen M Lewis, John Guttag, and Arvind Satyanarayan. Intuitively Assessing ML
Model Reliability through Example-Based Explanations and Editing Model Inputs. In 27th Interna-
tionalConferenceonIntelligentUserInterfaces, IUI ’22, pages 767–781, New York, NY, USA, March 2022.
|             |               |     |            |     | 978-1-4503-9144-3. | doi: 10.1145/3490099.3511160. |     |     |     |
| ----------- | ------------- | --- | ---------- | --- | ------------------ | ----------------------------- | --- | --- | --- |
| Association | for Computing |     | Machinery. |     | ISBN               |                               |     |     | URL |
https://doi.org/10.1145/3490099.3511160.
Maxwell Szymanski, Martijn Millecamp, and Katrien Verbert. Visual, textual or hybrid: the effect
of user expertise on different explanations. In 26th International Conference on Intelligent User In-
|           | 109–119, |     |         |         |               | 2021.     | 978-1-4503-8017-1. |     | doi: |
| --------- | -------- | --- | ------- | ------- | ------------- | --------- | ------------------ | --- | ---- |
| terfaces, | pages    |     | College | Station | TX USA, April | ACM. ISBN |                    |     |      |
10.1145/3397481.3450662. URLhttps://dl.acm.org/doi/10.1145/3397481.3450662.
Stefano Teso, Öznur Alkan, Wolfgang Stammer, and Elizabeth Daly. Leveraging explanations in interac-
tive machine learning: An overview. Frontiers in Artificial Intelligence, 6, 2023. ISSN 2624-8212. URL
https://www.frontiersin.org/articles/10.3389/frai.2023.1066049.
PaulThagard. Explanatorycoherence. BehavioralandBrainSciences,12(3):435–467,September1989. ISSN
| 1469-1825, | 0140-525X. | doi: | 10.1017/S0140525X00057046. |     |     |     |     |     |     |
| ---------- | ---------- | ---- | -------------------------- | --- | --- | --- | --- | --- | --- |
URLhttps://www.cambridge.org/core/jou
rnals/behavioral-and-brain-sciences/article/abs/explanatory-coherence/E05CB61CD64C26138
| E794BC601CC9D7A. |     | Publisher: | CambridgeUniversityPress. |     |     |     |     |     |     |
| ---------------- | --- | ---------- | ------------------------- | --- | --- | --- | --- | --- | --- |

bibliography 289
The Federal Reserve Board of Governors in Washington DC. The Fed - Supervisory Letter SR 11-7 on
guidance on Model Risk Management, April 2011. URL https://www.federalreserve.gov/supervi
sionreg/srletters/sr1107.htm.
The White House. Executive Order on the Safe, Secure, and Trustworthy Development and Use of
Artificial Intelligence. October 2023. URL https://www.whitehouse.gov/briefing-room/presidenti
al-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-a
nd-use-of-artificial-intelligence/.
ArthurThuyandDriesF.Benoit. Explainabilitythroughuncertainty: Trustworthydecision-makingwith
neural networks. European Journal of Operational Research, September 2023. ISSN 0377-2217. doi:
10.1016/j.ejor.2023.09.009. URL https://www.sciencedirect.com/science/article/pii/S037722172
3007105.
Nava Tintarev. Explanations of recommendations. In Proceedings of the 2007 ACM conference on Rec-
ommender systems, RecSys ’07, pages 203–206, New York, NY, USA, October 2007. Association for
Computing Machinery. ISBN 978-1-59593-730-8. doi: 10.1145/1297231.1297275. URL https:
//doi.org/10.1145/1297231.1297275.
AdelineToader. AuditabilityofAISystems–BrakeorAccelerationtoInnovation?,November2019. URL
https://papers.ssrn.com/abstract=3526222.
Dylan Tokar. Google Cloud Launches Anti-Money-Laundering Tool for Banks, Betting on the Power of
AI. WallStreetJournal, June 2023. ISSN 0099-9660. URL https://www.wsj.com/articles/google-clo
ud-launches-anti-money-laundering-tool-for-banks-betting-on-the-power-of-ai-2512ccce.
Richard Tomsett, Dave Braines, Dan Harborne, Alun Preece, and Supriyo Chakraborty. Interpretable to
Whom? A Role-based Model for Analyzing Interpretable Machine Learning Systems. In 2018 ICML
Workshop on Human Interpretability in Machine Learning, page 7, Stockholm, Sweden, June 2018. arXiv.
URLhttp://arxiv.org/abs/1806.07552. arXiv: 1806.07552.
Trade and Industry Appeals Tribunal. Bunq vs. DNB, ECLI:NL:CBB:2022:707, 21/323 and 21/1108, Oc-
tober 2022. URL https://deeplink.rechtspraak.nl/uitspraak?id=ECLI:NL:CBB:2022:707. Soort:
Uitspraak.
Andrea C. Tricco, Erin Lillie, Wasifa Zarin, Kelly K. O’Brien, Heather Colquhoun, Danielle Levac, David
Moher,MicahD.J.Peters,TanyaHorsley,LauraWeeks,SusanneHempel,ElieA.Akl,ChristineChang,
JessieMcGowan,LesleyStewart,LisaHartling,AdrianAldcroft,MichaelG.Wilson,ChantelleGarritty,
Simon Lewin, Christina M. Godfrey, Marilyn T. Macdonald, Etienne V. Langlois, Karla Soares-Weiser,
Jo Moriarty, Tammy Clifford, Özge Tunçalp, and Sharon E. Straus. PRISMA Extension for Scoping
Reviews(PRISMA-ScR):ChecklistandExplanation. AnnalsofInternalMedicine,169(7):467–473,October
2018. ISSN 0003-4819. doi: 10.7326/M18-0850. URL https://www.acpjournals.org/doi/10.7326/M1
8-0850. Publisher: AmericanCollegeofPhysicians.
Jon Truby, Rafael Brown, and Andrew Dahdal. Banking on AI: mandating a proactive approach to AI
regulationinthefinancialsector.LawandFinancialMarketsReview,14(2):110–120,April2020.ISSN1752-
1440. doi: 10.1080/17521440.2020.1760454. URL https://doi.org/10.1080/17521440.2020.1760454.
Publisher: Routledge_eprint: https://doi.org/10.1080/17521440.2020.1760454.
Chun-Hua Tsai, Yue You, Xinning Gui, Yubo Kou, and John M. Carroll. Exploring and Promoting Di-
agnosticTransparencyandExplainabilityinOnlineSymptomCheckers. InProceedingsofthe2021CHI
Conference on Human Factors in Computing Systems, CHI ’21, pages 1–17, New York, NY, USA, 2021.
Association for Computing Machinery. ISBN 978-1-4503-8096-6. doi: 10.1145/3411764.3445101. URL
https://doi.org/10.1145/3411764.3445101.
Miles Turpin, Julian Michael, Ethan Perez, and Samuel R. Bowman. Language Models Don’t Always
SayWhatTheyThink: UnfaithfulExplanationsinChain-of-ThoughtPrompting,December2023. URL
http://arxiv.org/abs/2305.04388. arXiv:2305.04388[cs].

| 290 | the | explanation |     | paradox | and | the human | centric | path |     |     |     |
| --- | --- | ----------- | --- | ------- | --- | --------- | ------- | ---- | --- | --- | --- |
-
Alec Tyson and Emma Kikuchi. Growing public concern about the role of artificial intelligence in daily
life, August 2023. URL https://www.pewresearch.org/short-reads/2023/08/28/growing-public-c
oncern-about-the-role-of-artificial-intelligence-in-daily-life/.
Brigitte Unger and Elena Madalina Busuioc. The Scale and Impacts of Money Laundering. Edward Elgar
| Publishing,March2007. |     |     | ISBN978-1-78100-762-4. |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
UNODC. Estimating illicit financial flows resulting from drug trafficking and other transnational orga-
2011.
nized crimes. Discussion paper, United Nations, October URL https://www.unodc.org/docume
nts/data-and-analysis/Studies/Illicit_financial_flows_2011_web.pdf.
Amy Unruh and Sarah Robinson. Explaining Model Predictions On Structured Data, March 2020. URL
https://liwaiwai.com/2020/03/04/explaining-model-predictions-on-structured-data/.
Betty Vandenbosch and Michael J. Ginzberg. Lotus Notes® and Collaboration: Plus ça change...
|         |     |               |             |     |          | 13(3):65–81, |          |     | 1996. | 0742-1222. | doi: |
| ------- | --- | ------------- | ----------- | --- | -------- | ------------ | -------- | --- | ----- | ---------- | ---- |
| Journal |     | of Management | Information |     | Systems, |              | December |     | ISSN  |            |      |
10.1080/07421222.1996.11518134. URL https://doi.org/10.1080/07421222.1996.11518134. Pub-
https://doi.org/10.1080/07421222.1996.11518134.
| lisher: | Routledge_eprint: |     |     |     |     |     |     |     |     |     |     |
| ------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
HelenaVasconcelos, MatthewJörke, MadeleineGrunde-McLaughlin,TobiasGerstenberg, MichaelBern-
stein, and Ranjay Krishna. Explanations Can Reduce Overreliance on AI Systems During Decision-
Making,December2022. URLhttp://arxiv.org/abs/2212.06823. arXiv:2212.06823[cs].
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez, Łukasz
|          |     |                            |     |           |     |                                                   |     | Advances | in Neural | Information | Processing |
| -------- | --- | -------------------------- | --- | --------- | --- | ------------------------------------------------- | --- | -------- | --------- | ----------- | ---------- |
| Kaiser,  | and | Illia Polosukhin.          |     | Attention |     | is All you Need.                                  | In  |          |           |             |            |
|          |     | volume30.CurranAssociates, |     |           |     | 2017.                                             |     |          |           |             |            |
| Systems, |     |                            |     |           |     | Inc., URLhttps://proceedings.neurips.cc/paper_fil |     |          |           |             |            |
es/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html.
JenniferWortmanVaughanandH.Wallach. AHuman-CenteredAgendaforIntelligibleMachineLearn-
Inundefined.2020.
ing. URL/paper/A-Human-Centered-Agenda-for-Intelligible-Machine-Vaughan
-Wallach/bc89a6fbf43cf911f71e5428d0b4a70fa5a40be9.
BrianaVecchione,KarenLevy,andSolonBarocas. AlgorithmicAuditingandSocialJustice: Lessonsfrom
the History of Audit Studies. In Equity and Access in Algorithms, Mechanisms, and Optimization, pages
| 1–9, |      |              |     | 2021. |     | 978-1-4503-8553-4. |     | doi: | 10.1145/3465416.3483294. |     |     |
| ---- | ---- | ------------ | --- | ----- | --- | ------------------ | --- | ---- | ------------------------ | --- | --- |
|      | – NY | USA, October |     | ACM.  |     | ISBN               |     |      |                          |     | URL |
https://dl.acm.org/doi/10.1145/3465416.3483294.
Oleksandra Vereschak, Gilles Bailly, and Baptiste Caramiaux. How to Evaluate Trust in AI-Assisted
Decision Making? A Survey of Empirical Methodologies. In CSCW 2021 - The 24th ACM Con-
|     |     |     |     |     |     |     |     |     | 5,  |     | 2021. doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
ference on Computer-Supported Cooperative Work and Social Computing, volume October
| 10.1145/3476068. |     |                                                     |     |     |     |     |     |     |        | CSCW2. |     |
| ---------------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- |
|                  |     | URLhttps://hal.sorbonne-universite.fr/hal-03280969. |     |     |     |     |     |     | Issue: |        |     |
IrisVesseyandDennisGalletta.CognitiveFit: AnEmpiricalStudyofInformationAcquisition.Information
Systems Research, 2(1):63–84, March 1991. ISSN 1047-7047. doi: 10.1287/isre.2.1.63. URL https:
//pubsonline.informs.org/doi/abs/10.1287/isre.2.1.63. Publisher: INFORMS.
Marco Virgolin, Andrea De Lorenzo, Francesca Randone, Eric Medvet, and Mattias Wahde. Model
learning with personalized interpretability estimation (ML-PIE). In Proceedings of the Genetic and Evo-
lutionary Computation Conference Companion, GECCO ’21, pages 1355–1364, New York, NY, USA, 2021.
|             |     |               |     |            |     | 978-1-4503-8351-6. |     | doi: | 10.1145/3449726.3463166. |     |     |
| ----------- | --- | ------------- | --- | ---------- | --- | ------------------ | --- | ---- | ------------------------ | --- | --- |
| Association |     | for Computing |     | Machinery. |     | ISBN               |     |      |                          |     | URL |
https://doi.org/10.1145/3449726.3463166.
Sophie von Stumm, Benedikt Hell, and Tomas Chamorro-Premuzic. The hungry mind: Intellectual
curiosityisthe thirdpillarofacademicperformance. PerspectivesonPsychologicalScience, 6(6):574–588,
| 2011. | ISSN1745-6924. |     | doi: | 10.1177/1745691611421204. |     |     |        |              |                   |     |     |
| ----- | -------------- | --- | ---- | ------------------------- | --- | --- | ------ | ------------ | ----------------- | --- | --- |
|       |                |     |      |                           |     |     | Place: | USPublisher: | SagePublications. |     |     |
Sandra Wachter, Brent Mittelstadt, and Luciano Floridi. Why a Right to Explanation of Automated
Decision-Making Does Not Exist in the General Data Protection Regulation. InternationalDataPrivacy
Law,7(2):76–99,May2017. ISSN2044-3994. doi: 10.1093/idpl/ipx005. URLhttps://doi.org/10.109
3/idpl/ipx005.

bibliography 291
Ari Ezra Waldman. Cognitive biases, dark patterns, and the ‘privacy paradox’. Current Opinion in
Psychology,31:105–109,February2020.ISSN2352-250X. doi: 10.1016/j.copsyc.2019.08.025.URLhttps:
//www.sciencedirect.com/science/article/pii/S2352250X19301484.
Danding Wang, Qian Yang, Ashraf Abdul, and Brian Y. Lim. Designing Theory-Driven User-Centric
Explainable AI. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, CHI
’19, pages 1–15, New York, NY, USA, May 2019a. Association for Computing Machinery. ISBN 978-1-
4503-5970-2. doi: 10.1145/3290605.3300831. URLhttps://doi.org/10.1145/3290605.3300831.
Junpeng Wang, Liang Gou, Han-Wei Shen, and Hao Yang. DQNViz: A Visual Analytics Approach to
Understand Deep Q-Networks. IEEE Transactions on Visualization and Computer Graphics, 25(1):288–
298, January 2019b. ISSN 1077-2626, 1941-0506, 2160-9306. doi: 10.1109/TVCG.2018.2864504. URL
https://ieeexplore.ieee.org/document/8454905/.
Mark Weber, Jie Chen, Toyotaro Suzumura, Aldo Pareja, Tengfei Ma, Hiroki Kanezashi, Tim Kaler,
Charles E. Leiserson, and Tao B. Schardl. Scalable Graph Learning for Anti-Money Laundering: A
FirstLook,November2018. URLhttp://arxiv.org/abs/1812.00076. arXiv:1812.00076[cs].
Patrick Weber, K. Valerie Carl, and Oliver Hinz. Applications of Explainable Artificial Intelligence in
Finance—asystematicreviewofFinance,InformationSystems,andComputerScienceliterature. Man-
agement Review Quarterly, 73(1):41, February 2023. ISSN 2198-1639. doi: 10.1007/s11301-023-00320-0.
URLhttps://doi.org/10.1007/s11301-023-00320-0.
Lisa Webley. Qualitative Approaches to Empirical Legal Research. In Peter Cane and Herbert M.
Kritzer, editors, The Oxford Handbook of Empirical Legal Research, page 0. Oxford University Press, Ox-
ford, November 2010. ISBN 978-0-19-954247-5. doi: 10.1093/oxfordhb/9780199542475.013.0039. URL
https://doi.org/10.1093/oxfordhb/9780199542475.013.0039.
Jane Webster and Richard T. Watson. Analyzing the Past to Prepare for the Future: Writing a Literature
Review. MISQuarterly, 26(2):xiii–xxiii, 2002. ISSN 0276-7783. URL https://www.jstor.org/stable/4
132319. Publisher: ManagementInformationSystemsResearchCenter,UniversityofMinnesota.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le,
andDennyZhou. Chain-of-ThoughtPromptingElicitsReasoninginLargeLanguageModels,January
2023. URLhttp://arxiv.org/abs/2201.11903. arXiv:2201.11903[cs].
K.Weitz,D.Schiller,R.Schlagowski,T.Huber,andE.André. “Letmeexplain!”: exploringthepotential
ofvirtualagentsinexplainableAIinteractiondesign. JournalonMultimodalUserInterfaces,15(2):87–98,
2021. doi: 10.1007/s12193-020-00332-0.
Daniel S. Weld and Gagan Bansal. The Challenge of Crafting Intelligible Intelligence. arXiv:1803.04263
[cs],October2018. URLhttp://arxiv.org/abs/1803.04263. arXiv: 1803.04263.
Michael R. Wick and William B. Thompson. Reconstructive expert system explanation. Artificial In-
telligence, 54(1):33–70, March 1992. ISSN 0004-3702. doi: 10.1016/0004-3702(92)90087-E. URL
https://www.sciencedirect.com/science/article/pii/000437029290087E.
Christopher D. Wickens, Stephen Rice, David Keller, Shaun Hutchins, Jamie Hughes, and Krisstal Clay-
ton. False Alerts in Air Traffic Control Conflict Alerting System: Is There a “Cry Wolf” Effect?
Human Factors, 51(4):446–462, August 2009. ISSN 0018-7208. doi: 10.1177/0018720809344720. URL
https://doi.org/10.1177/0018720809344720. Publisher: SAGEPublicationsInc.
DariciaWilkinson,ÖznurAlkan,Q.VeraLiao,MassimilianoMattetti,IngeVejsbjerg,BartP.Knijnenburg,
andElizabethDaly. WhyorWhyNot? TheEffectofJustificationStylesonChatbotRecommendations.
ACMTransactionsonInformationSystems,39(4):1–21,October2021. URLhttps://dl.acm.org/doi/10.
1145/3441715.
Leland Wilkinson. The Grammar of Graphics: Introduction. In The Grammar of Graphics, Statistics and
Computing,pages1–19.Springer,NewYork,NY,2005. ISBN978-0-387-28695-2. URLhttps://doi.or
g/10.1007/0-387-28695-0_1.

292 the explanation paradox and the human centric path
-
Joseph J. Williams and Tania Lombrozo. The Role of Explanation in Discovery and Generalization:
Evidence From Category Learning. Cognitive Science, 34(5):776–806, 2010. ISSN 1551-6709. doi:
10.1111/j.1551-6709.2010.01113.x. URL https://onlinelibrary.wiley.com/doi/abs/10.111
1/j.1551-6709.2010.01113.x. _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1551-
6709.2010.01113.x.
Jeannette M. Wing. Trustworthy AI. CommunicationsoftheACM, 64(10):64–71, October 2021. ISSN 0001-
0782,1557-7317. doi: 10.1145/3448248. URLhttps://dl.acm.org/doi/10.1145/3448248.
Terry Winograd and Fernando Flores. Understanding Computers and Cognition: A New Foundation for
Design. Addison-Wesley,1987.
ChristineT.Wolf. Explainabilityscenarios: towardsscenario-basedXAIdesign. InProceedingsofthe24th
International Conference on Intelligent User Interfaces, pages 252–257, Marina del Ray California, March
2019.ACM. ISBN978-1-4503-6272-6. doi: 10.1145/3301275.3302317. URLhttps://dl.acm.org/doi/1
0.1145/3301275.3302317.
RobertWolfe. Doessunshinemakeadifference? HandbookofGlobalEconomicGovernance,2013. Publisher:
Routledge.
Claire Woodcock, Brent Mittelstadt, Dan Busbridge, and Grant Blank. The Impact of Explanations on
LaypersonTrustinArtificialIntelligence-DrivenSymptomCheckerApps: ExperimentalStudy. Journal
ofMedicalInternetResearch,23(11):e29386,November2021. ISSN1438-8871. doi: 10.2196/29386.
Brenda Wright. Chapter 17 - Audits and Inspections. In Delva Shamley and Brenda Wright, editors, A
ComprehensiveandPracticalGuidetoClinicalTrials, pages 181–183. Academic Press, January 2017. ISBN
978-0-12-804729-3. doi: 10.1016/B978-0-12-804729-3.00017-1. URL https://www.sciencedirect.com/
science/article/pii/B9780128047293000171.
Tongshuang Wu, Marco Tulio Ribeiro, Jeffrey Heer, and Daniel S Weld. Polyjuice: Generating counter-
factualsforexplaining,evaluating,andimprovingmodels. arXivpreprintarXiv:2101.00288,2021.
Yaniv Yacoby, Ben Green, Christopher L. Griffin Jr., and Finale Doshi Velez. "If it didn’t happen, why
would I change my decision?": How Judges Respond to Counterfactual Explanations for the Public
SafetyAssessment,August2022. URLhttp://arxiv.org/abs/2205.05424. arXiv:2205.05424[cs].
Jing Nathan Yan, Ziwei Gu, Hubert Lin, and Jeffrey M. Rzeszotarski. Silva: Interactively Assessing
MachineLearningFairnessUsingCausality. InProceedingsofthe2020CHIConferenceonHumanFactors
in Computing Systems, CHI ’20, pages 1–13, New York, NY, USA, 2020. Association for Computing
Machinery. ISBN 978-1-4503-6708-0. doi: 10.1145/3313831.3376447. URL https://doi.org/10.1145/
3313831.3376447.
Jia-YuYao,Kun-PengNing,Zhen-HuiLiu,Mu-NanNing,andLiYuan. LLMLies: Hallucinationsarenot
Bugs,butFeaturesasAdversarialExamples,October2023a. URLhttp://arxiv.org/abs/2310.01469.
arXiv:2310.01469[cs].
ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,KarthikNarasimhan,andYuanCao. ReAct:
Synergizing Reasoning and Acting in Language Models, March 2023b. URL http://arxiv.org/abs/
2210.03629. arXiv:2210.03629[cs].
Ji Soo Yi, Youn ah Kang, John Stasko, and J.A. Jacko. Toward a Deeper Understanding of the Role of
InteractioninInformationVisualization. IEEETransactionsonVisualizationandComputerGraphics,13(6):
1224–1231,November2007. ISSN1941-0506. doi: 10.1109/TVCG.2007.70515. ConferenceName: IEEE
TransactionsonVisualizationandComputerGraphics.
Yvette D. Clarke. Algorithmic Accountability Act of 2023, September 2023. URL https://www.govinf
o.gov/app/details/BILLS-118hr5628ih. Call Number: Y 1.6:, Y 1.4/6: Committee: Committee on
EnergyandCommercePublisher: U.S.GovernmentPublishingOfficeSource: DGPO.

bibliography 293
MatthewD.ZeilerandRobFergus. VisualizingandUnderstandingConvolutionalNetworks,November
2013. URLhttp://arxiv.org/abs/1311.2901. arXiv:1311.2901[cs].
John Zerilli, Alistair Knott, James Maclaurin, and Colin Gavaghan. Algorithmic Decision-Making and
the Control Problem. Minds and Machines, 29(4):555–578, December 2019. ISSN 1572-8641. doi:
10.1007/s11023-019-09513-7. URLhttps://doi.org/10.1007/s11023-019-09513-7.
BaobaoZhang. PublicOpiniontowardArtificialIntelligence. InJustinB.Bullock,Yu-CheChen,Johannes
Himmelreich,ValerieM.Hudson,AntonKorinek,MatthewM.Young,andBaobaoZhang,editors,The
OxfordHandbookofAIGovernance,page0.OxfordUniversityPress,October2021.ISBN978-0-19-757932-
9. doi: 10.1093/oxfordhb/9780197579329.013.36. URL https://doi.org/10.1093/oxfordhb/9780197
579329.013.36.
Xiaoge Zhang, Felix T. S. Chan, and Sankaran Mahadevan. Explainable machine learning in image
classification models: An uncertainty quantification perspective. Knowledge-Based Systems, 243:108418,
May 2022. ISSN 0950-7051. doi: 10.1016/j.knosys.2022.108418. URL https://www.sciencedirect.co
m/science/article/pii/S095070512200168X.
Zelun Tony Zhang, Yuanting Liu, and Heinrich Hussmann. Forward Reasoning Decision Support: To-
wardaMoreCompleteViewoftheHuman-AIInteractionDesignSpace. InCHItaly2021: 14thBiannual
Conference of the Italian SIGCHI Chapter, pages 1–5, Bolzano Italy, July 2021. ACM. ISBN 978-1-4503-
8977-8. doi: 10.1145/3464385.3464696. URLhttps://dl.acm.org/doi/10.1145/3464385.3464696.
XunZhao,YanhongWu,DikLunLee,andWeiweiCui. iForest: InterpretingRandomForestsviaVisual
Analytics. IEEE Transactions on Visualization and Computer Graphics, 25(1):407–416, January 2019. ISSN
1941-0506. doi: 10.1109/TVCG.2018.2864475.URLhttps://ieeexplore.ieee.org/document/8454906.
ConferenceName: IEEETransactionsonVisualizationandComputerGraphics.
Sarah Zheng and Jane Zhang. China Tries to Balance State Control and State Support of AI. TIME,
August2023. URLhttps://time.com/6304831/china-ai-regulations/.
Joyce Zhou and Thorsten Joachims. How to Explain and Justify Almost Any Decision: Potential
Pitfalls for Accountability in AI Decision-Making. In Proceedings of the 2023 ACM Conference on
Fairness, Accountability, and Transparency, FAccT ’23, pages 12–21, New York, NY, USA, 2023. As-
sociation for Computing Machinery. ISBN 9798400701924. doi: 10.1145/3593013.3593972. URL
https://dl.acm.org/doi/10.1145/3593013.3593972.
J. Zhu, A. Liapis, S. Risi, R. Bidarra, and G. M. Youngblood. Explainable AI for Designers: A Human-
CenteredPerspectiveonMixed-InitiativeCo-Creation. In2018IEEEConferenceonComputationalIntelli-
genceandGames(CIG),pages1–8,August2018. doi: 10.1109/CIG.2018.8490433. ISSN:2325-4289.
Alexandra Zytek, Dongyu Liu, Rhema Vaithianathan, and Kalyan Veeramachaneni. Sibyl: Understand-
ing and Addressing the Usability Challenges of Machine Learning In High-Stakes Decision Making.
arXiv:2103.02071[cs],September2021. URLhttp://arxiv.org/abs/2103.02071. arXiv: 2103.02071.

Titre : Confiance de´place´e dans l’IA : le paradoxe de l’explication et l’approche centre´e sur l’homme. Une
caracte´risationdesde´fiscognitifspourfaireconfiancedemanie`reapproprie´eauxde´cisionsalgorithmiqueset
applicationsdanslesecteurfinancier.
Mots cle´s : explicabilite´, apprentissage automatique, approche centre´e sur l’humain, lutte anti-blanchiment,
robo-advisor,supervisionfinancie`re
Re´sume´ : L’IA devenant de plus en plus pre´sente unetaxonomiedesdiffe´rentesfac¸onsd’interagiravec
dans nos vies, nous sommes soucieux de com- les solutions d’explicabilite´. La deuxie`me partie se
prendrelefonctionnementdecesstructuresopaques. concentre sur des contextes financiers pre´cis. Une
Pourre´pondrea` cettedemande,ledomainedelare- e´tude porte sur les syste`mes de recommandation et
cherche en explicabilite´ (XAI) s’est conside´rablement de souscription en ligne de contrats d’assurance-vie.
de´veloppe´ au cours des dernie`res anne´es. Cepen- L’e´tudesoulignequelesexplicationspre´sente´esdans
dant, peu de travaux ont e´tudie´ le besoin en expli- ce contexte n’ame´liorent pas de manie`re significa-
cabilite´ des re´gulateurs ou des consommateurs a` la tive la compre´hension de la recommandation par les
lumie`red’exigencesle´galesenmatie`red’explications. utilisateurs non experts. Elles ne suscitent pas da-
Cette the`se s’attache a` comprendre le roˆle des ex- vantage la confiance des utilisateurs que si aucune
plications pour permettre la conformite´ re´glementaire explication n’e´tait fournie. Une autre e´tude analyse
des syste`mes ame´liore´s par l’IA dans des applica- les besoins des re´gulateurs en matie`re d’explication
tions financie`res. La premie`re partie passe en re- dans le cadre de la lutte contre le blanchiment d’ar-
vue le de´fi de prendre en compte les biais cogni- gent et le financement du terrorisme. Elle constate
tifs de l’homme dans les explications des syste`mes quelesautorite´sdecontroˆleontbesoind’explications
d’IA.L’analysefournitplusieurspistespourmieuxali- pour e´tablir le caracte`re re´pre´hensible des cas de
gner les solutions d’explicabilite´ sur les processus de´faillance e´chantillonne´s, ou pour ve´rifier et contes-
cognitifs des individus, notamment en concevant des terlabonnecompre´hensiondel’IAparlesbanques.
explications plus interactives. Elle pre´sente ensuite
Title : Misplaced trust in AI: the explanation paradox and the human-centric path. A characterisation of the
cognitivechallengestoappropriatelytrustalgorithmicdecisionsandapplicationsinthefinancialsector.
Keywords:explainability,machinelearning,human-centeredapproach,anti-moneylaundering,robo-advisor,
financialsupervision
Abstract : As AI is becoming more widespread in moreinteractiveexplanations.Itthenpresentsataxo-
our everyday lives, concerns have been raised about nomy of the different ways to interact with explai-
comprehending how these opaque structures ope- nability solutions. The second part focuses on spe-
rate. In response, the research field of explainabi- cific financial contexts. One study takes place in
lity(XAI)hasdevelopedconsiderablyinrecentyears. the domain of online recommender systems for life-
However, little work has studied regulators’ need for insurancecontracts.Thestudyhighlightsthatfeature-
explainability or considered effects of explanations based explanations do not significantly improve non
on users in light of legal requirements for expla- expert users’ understanding of the recommendation,
nations. This thesis focuses on understanding the nor lead to more appropriate reliance compared to
role of AI explanations to enable regulatory com- having no explanation at all. Another study analyzes
pliance of AI-enhanced systems in financial applica- theneedsofregulatorsforexplainabilityinanti-money
tions. The first part reviews the challenge of taking launderingandfinancingofterrorism.Itfindsthatsu-
into account human cognitive biases in the expla- pervisors need explanations to establish the repre-
nations of AI systems. The analysis provides seve- hensibility of sampled failure cases, or to verify and
ral directions to better align explainability solutions challengebanks’correctunderstandingoftheAI.
withpeople’scognitiveprocesses,includingdesigning
InstitutPolytechniquedeParis
91120Palaiseau,France