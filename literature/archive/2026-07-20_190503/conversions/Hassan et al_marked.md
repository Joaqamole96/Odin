Received13December2023,accepted21January2024,dateofpublication26January2024,dateofcurrentversion5February2024.
DigitalObjectIdentifier10.1109/ACCESS.2024.3359053
GCZRec: Generative Collaborative
Zero-Shot Framework for Cold
Start News Recommendation
SYEDZAINULHASSAN 1,MUHAMMADRAFI 1,
ANDJAROSLAVFRNDA 2,3,(SeniorMember,IEEE)
1DepartmentofComputerScience,SchoolofComputing,NationalUniversityofComputerandEmergingSciences,Islamabad44000,Pakistan
2DepartmentofQuantitativeMethodsandEconomicInformatics,FacultyofOperationandEconomicsofTransportandCommunications,UniversityofZ˘ilina,
01026Z˘ilina,Slovakia
3DepartmentofTelecommunications,FacultyofElectricalEngineeringandComputerScience,VSB—TechnicalUniversityofOstrava,70800Ostrava,Czech
Republic
Correspondingauthor:JaroslavFrnda(jaroslav.frnda@uniza.sk)
ThisworkwassupportedbytheEuropeanUnionwithintheREFRESHProject—ResearchExcellenceforRegionSustainabilityand
High-TechIndustriesoftheEuropeanJustTransitionFundunderGrantCZ.10.03.01/00/22003/0000048.
ABSTRACT The aim of personalized news recommendation is to suggest news stories to the users that
aremostinterestingforthem.Toimprovetheuserexperience,itisimportantthatthesenewsitemsarenot
onlyrelevanttotheuserbutalsogetrecommendedtothemassoonastheyareavailable.Theinabilityof
traditional collaborative filtering approach to recommend such cold start items has led to techniques that
incorporate latent features of items in order to make cold start recommendations such as content based
filtering and deep neural network-based approaches. However, these existing techniques do not make use
of any collaborative information between users and items as well as latent features at the same time and
thus fail to provide any serendipity which is an important aspect of any recommender system. Moreover,
theseunderlyingcollaborativesignalsbetweenusersanditemsarecrucialtoimprovingtheoverallqualityof
recommendersystemsandcanalsobeutilizedtomakecoldstartrecommendations.Inthispaper,wepropose
theGenerativeCollaborativeZero-ShotRecommenderSystemframework(GCZRec)whichmakesuseof
boththelatentuseranditemfeaturesaswellastheunderlyingcollaborativeinformationtogenerateboth
warmstartandcoldstartrecommendations.Weevaluateourframeworkfornewsrecommendationtaskgiven
coldstartandwarmstartcasesforbothusersandnewsitems.Wealsodiscussthatourmodelcanbeplugged
inandusedaspreprocessingtoimprovetheperformanceofanexistingrecommendersystem.
INDEXTERMS Newsrecommendation,coldstartproblem,zero-shotlearning,recommendersystem.
I. INTRODUCTION interestingandpersonalized.Butcomparedtorecommending
The improvement in media technology and online services movies and products, news article recommendations often
have resulted in an overload of information especially with entail some additional challenges such as the latest news
online news articles as the people realize the need to be articles being posted frequently and lacking any historical
well-informed at all times [1], [2]. Recommender systems interactions that can be used for recommending these news
canthereforeimprovetheuserexperiencebysuggestingnews items[3].Thisseverecaseofcoldstartproblemisachallenge
articles that are most recent, relevant and contain value for in news recommendations. Moreover, from the user point
her.Thesesystemscanhelptheusersfindinformationthatis of view, these news stories need to be recent but highly
personalized, while from the item perspective, it should be
The associate editor coordinating the review of this manuscript and recommended to the users based strictly on its relevance to
approvingitforpublicationwasChaoTong . thoseparticularusers.
2024TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution-NonCommercial-NoDerivatives4.0License.
16610 Formoreinformation,seehttps://creativecommons.org/licenses/by-nc-nd/4.0/ VOLUME12,2024

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
The conventional collaborative recommendation algo-
rithms rely on historical interaction data of users and items
to find hidden patterns based on similarity [4], [5]. The
performance of these algorithms decreases when the data
contains missing user interaction entries for the items. This
lackofdataismostlyseeninthecaseofnewsarticleswhich
are often posted without any prior interaction information.
Thisleadstoaseverecaseofcoldstartproblem.
Other techniques such as Matrix Factorization [6] and
content-based filtering [7] also suffer from cold start user
problem[8],[9],[10].IncaseofMatrixFactorization,itcan FIGURE1. Illustrationofthecoldstartnewsrecommendationproblem.
additionally suffer from both over-fitting and under-fitting
giventheavailablehistoricaldata.Anotherproblemthatboth
and items. In the same way that an unseen class label is
of these techniques face is the assumption that features are
used for prediction by leveraging the features of the novel
always independent. This condition is difficult to hold true
sample, the conditional input of the generator network can
in most real-world scenarios where not only the features
also be learned from the available item and user feature
but items also have relative dependence on features and
representations.
themselves.
Based on the previous discussion, we propose a novel
The cold start problem in recommender systems can be
recommender system framework, GCZRec, to synthesize
remodeledasaclassicalzero-shotlearningtaskwhichcomes
bothcoldstartandwarmstartinteractionsforusersandnews
from the computer vision domain [11], [12]. In zero-shot
items.Ourtechniqueutilizesthehiddenfeatureinformation
classification, the set of classes in the training data and set
of users and items to perform cold start recommendations
of classes in the samples to be classified can be disjoint.
as zero-shot predictions. The proposed model is capable
Similarly, in cold start item recommendations, the aim is to
of learning collaborative signals between users and among
predictwhetheranitemshouldberecommendedtoapartic-
items to generate interactions thus allowing diverse rec-
ularuserwithoutanyavailablehistoricalinteractionsforthat
ommendations. The framework also allows the ranking of
item. In cold start user case, items are to be recommended
these recommendations. At its core, GCZRec framework
toaparticularuserforwhichtherearenoexistinghistorical
consists of two separate classifiers for zero-shot labelling
information [13]. Following this intuition, the features of
of cold start news and cold start user. These predicted
news items and users can be used to deduce the behavioral
classes are used as input to conditional Wasserstein GAN
context of cold start items and users in recommendation
(cWGAN) for generating interactions. During training, two
schemejustlikeaclasslabelcanbepredictedforanunseen
separate generator networks are independently trained such
datasampleusingthegeneralizationfromknownsamplesin
that each training sample of the first network represent a
zero-shotclassification.Someexistingstudies[14],[15]have
newsitemwithinteraction.Thisgeneratornetworkistrained
usedthisrelationtoproposerecommendationmodelsforcold
on samples each one of which is an interaction vector
startitems.
containing both interactions of users for news items. The
Butthesetechniquesdonottakeintoaccountserendipity,
experimentswereconductedontwopubliclyavailablenews
whichisanimportantaspectofarecommendersystem[16],
recommendation datasets Microsoft News Dataset (MIND)
[17],[18],[19].Thislackofdiversitystemsfromtheinability
[20] and Addressa [21] in order to provide the proof of
of these models to make use of the latent collaborative
conceptforourresearch.Furthermore,ourframeworkallows
information between users as well as items. These neigh-
this problem to be formulated as an extreme multi-label
borhoodsignalsarethereforeimportanttomakefine-grained
classification task where the class labels are news items to
recommendationsthatarenotonlyrelevanttotheactiveusers
berecommended.
butalsoprovidediversityinchoicesforthem.
Themaincontributionsofthisresearchareasfollows:
We observe that by directly synthesizing the interactions
based on feature representations can eliminate the need • We propose a novel GCZRec framework capable of
for any external click predictor model and can also pro- usinglatentcollaborativeinformationtomakebothcold
vide an effective method to not only allow item-to-user startandwarmstartrecommendationsofnewsitemsin
interactions prediction but also projection of user-to-item generativemannerandallowingtherecommendeditems
interactions. This synthesis of interactions can also allow toberanked.
us an efficient method to rank the predicted interactions. • We present a formulation of cold start recommenda-
Thiscanbeachievedbyincorporatingagenerativenetwork tion as zero-shot learning problem and utilize hidden
withconditionalinformationtolearnthelatentcollaborative features of both users and items in order to make
information between users and items. This allows us to recommendations.
use these hidden patterns in the available historical data • Our framework can also be used for typical extreme
to directly synthesize the interactions for cold start users multi-label classification task and provides an efficient
VOLUME12,2024 16611

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
approachforpredictingthesubsetoflabelsfromalarge III. RELATEDWORK
spacegivenanewinstance. Over the years, numerous techniques have been proposed
|     |     |     |     |     | to deal with | recommendation     | problem   | with | Collaborative   |
| --- | --- | --- | --- | --- | ------------ | ------------------ | --------- | ---- | --------------- |
|     |     |     |     |     | Filtering    | [4], Content-based | Filtering | [6], | [22] and Matrix |
II. PRELIMINARIES
The goal of a recommender system is to present the users Factorization[7]amongtheprominentapproaches.However,
with an ordered set of items which are ranked based on the theproblemofnewsrecommendationpresentsanadditional
preference and relevance of these items for each particular challengethattheitemmustbelinkedtoatargetsetofreaders
user. This section defines the relevant concepts pertaining soonuponentryintothesystem.
to the overall recommendation problem and provides the In this section, we first review the news recommendation
necessary basis for further discussion on these topics in the problem and the techniques that were employed for this
subsequentsections. specific task and then we shift our attention to generative
Definition1: Given set of users U and items I, the U x I adversarialapproachesforrecommendationsthatarepresent
| interactionmatrixℜrepresentsthehistoricalchoicesofusers |     |     |     |     | inliterature. |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
anditemsr(u∈U,i∈I).Acoldstartuserproblemoccurwhen
|                                      |     |                    |     |     | A. NEWSRECOMMENDATION |     |     |     |     |
| ------------------------------------ | --- | ------------------ | --- | --- | --------------------- | --- | --- | --- | --- |
| r(u new ,i)isundefinedforanoveluseru |     | new andallvaluesof |     |     |                       |     |     |     |     |
Theearliestnewsrecommendationswerefocusedonsimilar-
itemsiinI.Whereas,acoldstartitemproblemoccurswhen
r(u,i )isundefinedforanovelitemi andallvaluesof ityandclassicalmachinelearningalgorithms.In[22],simi-
| new |     | new |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
laritybetweenusermodelandnewsarticlesareexploitedto
uinU.
generatepersonalizedrecommendations.Forfindingrelevant
| The cold | start problem | in recommender | systems | is  |     |     |     |     |     |
| -------- | ------------- | -------------- | ------- | --- | --- | --- | --- | --- | --- |
newsitems,[23]proposedtheideaofusingsemanticsofthe
| comparable | to zero-shot classification | problem | in computer |     |     |     |     |     |     |
| ---------- | --------------------------- | ------- | ----------- | --- | --- | --- | --- | --- | --- |
newsarticles.SF-IDFincombinationwithdifferentsemantic
vision.
Definition2: In zero-shot learning, the classification similarity measures were used to find relevant news items
wheretheonlysemanticcontexttheyincorporatedwasbased
| model generalizes | feature information | from | seen classes | to  |              |              |          |        |             |
| ----------------- | ------------------- | ---- | ------------ | --- | ------------ | ------------ | -------- | ------ | ----------- |
|                   |                     |      |              |     | on synonyms. | The approach | of using | SF-IDF | was further |
anunseenclassinordertopredictit.Mathematically,given
asetofinstancesXandsetoflabelsYwhereYcontainsboth extendedby[24]intheirworkwhichusedanupdatedSF-IDF
|     |     |     |     |     | measure | for finding semantic | similarity | while | taking into |
| --- | --- | --- | --- | --- | ------- | -------------------- | ---------- | ----- | ----------- |
seenandunseenclasses,andfeaturespaceZ,theobjectiveof
zero-shotlearningistolearnthemappingffrominputstate account the relationship between synonym sets. In a graph-
basedapproach,[25]discussedtheuseofknowledgegraphs
XtosemanticspaceZ:
byconnectingnamedentities,eventsandplacespresentinthe
:X →Z
|     | f   |     |     | (1) | newsarticles. |              |               |           |            |
| --- | --- | --- | --- | --- | ------------- | ------------ | ------------- | --------- | ---------- |
|     |     |     |     |     | The idea      | of employing | collaborative | filtering | along with |
AndalsolearnthemappinggfromsemanticspaceZtolabel
|     |     |     |     |     | content-based | approach | to make | news recommendation |     |
| --- | --- | --- | --- | --- | ------------- | -------- | ------- | ------------------- | --- |
spaceY:
|     |     |     |     |     | was also  | explored in research.  |                 | One such | example was     |
| --- | --- | --- | --- | --- | --------- | ---------------------- | --------------- | -------- | --------------- |
|     |     |     |     |     | NewsDude  | [26] which recommended |                 | news     | by sequentially |
|     | g:Z | →Y  |     | (2) |           |                        |                 |          |                 |
|     |     |     |     |     | employing | three modules.         | A content-based |          | recommender,    |
Since, in a recommendation problem, there are typically a followed by classical collaborative component and a Naïve
largenumberofusersanditemsinvolved.Theselectionofa Bayes classifier. In [27], a hybrid algorithm was presented
smallsubsetofrelevantitemsfortheuserfromalargespace that combined content-based recommender system with
ofavailableitemsisanalogoustopredictingclasslabelsinan collaborative filtering to recommend sports news articles.
extrememulti-labelclassificationproblem. The inability of collaborative version to handle cold start
Definition3: In extreme multi-label classification, the items was dissimulated by the content-based component.
objective is to predict a subset of most relevant labels from Inanothersuchwork[28]proposedthetechniqueforfusion
a high-dimensional label space containing a vast number of collaborative filtering and content-based modelling to
of potential labels, given an input instance. Mathematically, generatenewsrecommendations.Thecontent-basedmodule
χ
given an input space and a high-dimensional label space wasusedtoconstructuserprofilewhileusergroupssimilar
|L|. The objective in extreme multi-label classification is to to the active user were found in much the same way as in
trainamodel thatcanfindasetl containingrelevantlabels a collaborative approach. Then a fusion model with user’s
foranovelinstancex given l ⊆|L|. currentandpotentialinterestswasdevelopedtorecommend
Wenowintroduceserendipitywhichcangenerallybeseen news by finding similarity between the fusion model and
asthemeasureofdiversityinrecommendationsproducedby contentofthenewsarticles.
analgorithmandisanimportantcharacteristicforimproving In a different approach for finding personalized news
theoveralluserexperience. articles, [29], [30], [31] used deep neural networks as
Definition4: In the context of recommender systems, their recommendation model. In [29], a news encoder and
serendipityreferstotheabilityofanalgorithmtorecommend user encoder were trained such that the news encoder
unexpectedanddiverseitemstotheuserstoexpandtheirtaste used attention mechanism to find topic information from
intoneighboringinterestareas. news articles through classification. The user encoder was
| 16612 |     |     |     |     |     |     |     |     | VOLUME12,2024 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
constructed with the help of users click behavior on news for items across different users. Due to the click prediction
articles. The news encoder was constructed in much the objectiveoftheirwork,therecommendationtaskisreduced
samewayby[30].However,theyarguedthatcapturingboth tobinaryclassificationandcouldnotbeextendedtoallowfor
long-term and short-term interests of the users is necessary multi-labelformulationoftheproblem.
for recommending highly personalized news items. The In an earlier work on generative recommendations, [38]
long-termrepresentationswerecapturedbytheembeddings proposed autoencoders are generators for collaborative rec-
of user IDs while the short-term representation of the users ommendations in CAAE model and to extract latent factors
wasguidedbytheirbrowsedarticlesusingaGRUnetwork. fromuser-iteminteractions,however,theirframeworkdidnot
The idea of different users who click on the same article utilizetheseparatefeaturespaceofusersanditemstomake
with attention on different aspects was discussed by [31] in recommendationincasetherewasacoldstartuserorproduct.
theirpaper.Theyusedconvolutionalneuralnetwork(CNN)
tolearnnewsitemrepresentationfromitstitle.Theattention IV. GCZRECFRAMEWORK
mechanismwasusedatnews-levelandword-levelinthenews The architecture of our proposed GCZRec framework con-
modelsinceaparticularnewsmayhavedifferentimportance sistsofdualgeneratornetworks,implementedasconditional
orrelevancefordifferentusers. WassersteinGAN.Thegeneratorfornews-to-userinteraction
is trained on mapping a given news item to a distribution
B. GENERATIVEMETHODS representing users’ interest score for the item. Whereas the
Among the first to use GAN for recommendation problem companion generator for user-to-news interaction is trained
were IRGAN [32] and GraphGAN [33]. These methods to generate a distribution of interaction scores of all news
exploredthepotentialofGANforrecommendersystemsbut items for a given user. Another important component of the
suffered from the well-known ‘‘label confusion’’ problem; GCZRec model are two independent classifiers for news
thatisthemodellearningtolabelanitemwithpositiveand and users. These pre-trained classifiers are used to perform
negative labels at the same time resulting in performance zero shot prediction of a cold start news or user in order
degradation of the model. As an application of minimax toprovidethegeneratornetworkstheirconditionalinputfor
optimization inherently present in GANs, [32] proposed synthesizingtheinteractions.
item recommendation as a generalized information retrieval The proposed framework utilizes generative capabilities
task with an objective function of matching top-k relevant ofthetraditionalGANarchitecturetosynthesizeinteractions.
documentstotheuser. The individual classifiers are trained to use semantic space
Intheirpaper,[33]proposedamodelthatsetanobjective and classify both seen and unseen news item and user in
of generating the connectivity distribution for a given order to provide our generators a conditional input. This
vertex. In the recommendation application, the connectivity design of our model also opens the door for a novel way
distribution between a given vertex and all relevant items of performing zero-shot extreme multi-label classification
was discussed. It was discussed by [34] in their paper that efficiently. In the subsequent subsections, each component
treating missing user-item as negative rating can deteriorate of our model is discussed in detail. In Fig. 2, the overall
the recommendation performance since the negative ratings architectureofGCZRecisillustrated.
could just be due to the user unaware of the item. They
used GANs to generate pairwise recommendation for each A. NOTATIONALCONVENTIONS
user and item with positive-unlabeled sampling. The idea Intheremainderofthispaper,thegeneralnotationusedfora
of using conditional variant of GAN for recommendation news is N and for active user it is U. We also denote warm
was presented by [35] in their research. Their GAN was news, cold news, warm user and cold user by w , c , w ,
n n u
conditionedonfashionitemasaclass,givenwhichanother c respectively.Thefourpossiblecasestobeconsideredare
u
complementaryitemwasgeneratedasarecommendation. thusrepresentedasw w ,w c ,c w ,c c .Thesecasesare
n u n u n u n u
A GAN-based approach to handle the problem of data representedinthemodelwiththehelpofa2-bitvectorwhich
imbalance in recommender systems was proposed by [36]. serves as the item-user state gate g and can determine the
s
TheymadeuseofconditionalWassersteinGANtogenerate synthesizertobeusedforgeneratinginterestvector.Werefer
missingdataforminorityclasstoperformrecommendations. to the generator responsible for synthesizing interactions
Their work used PacGAN in the discriminator architecture for each user given a particular news item as gen and its
N
with an aim to alleviate the performance of missing data companion generator which is responsible for generating
and improve the performance of recommendation models. interactionsforeachnewsgivenauserasgen .Apartfrom
U
InanotherWassersteinGANbasedframework,[37]proposed thesegenerators,thezero-shotclassifiersfornovelnewsitem
GAZRecmodeltogeneratesyntheticfeaturerepresentations anduserwillbecallednewslabelpredictorP anduserlabel
N
for both cold start news and user. To find the probability predictorP .Theseclassifiersarejointlyreferredtoaszero-
U
of click behavior, their framework adopted a separate click shot predictors. For encoding the identifiers of warm start
predictor module given a single user and news item. The news item and warm start users and map them to a unique
model did not use the behavioral representations to train numericidentifier,theencodersemployedarereferredtoas
thegeneratorforlearningdistributionofinteractionsdirectly E andE respectively.
N U
VOLUME12,2024 16613

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
FIGURE2. ArchitectureofproposedGCZRecframework.
B. NEWSINTERESTSCOREGENERATORGEN ThegeneralobjectivefunctionofcWGANisgivenas:
N
| The generator |     | gen N in | GCZRec | framework |     | is responsible |     |              |     |           |     |
| ------------- | --- | -------- | ------ | --------- | --- | -------------- | --- | ------------ | --- | --------- | --- |
|               |     |          |        |           |     |                | min | max V(D,G)=E |     | [D(x ,c)] |     |
for handling the st ates w w , c w and c c . These input G D c,x∼true true
|     |     |     | n u | n u | n   | u   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
statesaredeterminedpriortoitbystategateg .Thisnetwork −E [D(G(z,c)),c] (3)
|             |             |     |       |          | s            |           |     |     | c,z |     |     |
| ----------- | ----------- | --- | ----- | -------- | ------------ | --------- | --- | --- | --- | --- | --- |
| synthesizes | interaction |     | score | for each | of the users | given the |     |     |     |     |     |
Inthecontextofnewsrecommendation,thegeneratorgen
| news item | label | y as | its conditional |     | input. | The relevancy |     |     |     |     | N   |
| --------- | ----- | ---- | --------------- | --- | ------ | ------------- | --- | --- | --- | --- | --- |
N
|              |      |      |       |          |               |      | aims to minimize | this combined    | objective | function,  | while   |
| ------------ | ---- | ---- | ----- | -------- | ------------- | ---- | ---------------- | ---------------- | --------- | ---------- | ------- |
| of an active | news | item | for a | user can | be determined | from |                  |                  |           |            |         |
|              |      |      |       |          |               |      | the critic       | aims to maximize | it. This  | leads to a | minimax |
thecorrespondingvaluegeneratedbythenetworkwherethis
gamewherethegeneratortriestoproducerealisticsynthetic
| value is | essentially | an  | interest | score. | The overall | output of |     |     |     |     |     |
| -------- | ----------- | --- | -------- | ------ | ----------- | --------- | --- | --- | --- | --- | --- |
samples,andthecritictriestoeffectivelydistinguishbetween
| gen is | a vector | of interest |     | scores predicted |     | to be given |                                |     |     |      |            |
| ------ | -------- | ----------- | --- | ---------------- | --- | ----------- | ------------------------------ | --- | --- | ---- | ---------- |
| N      |          |             |     |                  |     |             | realandsyntheticsamples.WhereE |     |     | [D(x | ,c)]repre- |
by each user in the system to the active news item. Each c,xtrue true
sentsexpectationoverrealdatawhereasE
c,z [D(G(z,c)),c]is
positioninthisvectorrepresentsauniqueuserandthevalue
theexpectationovervaluesgeneratedbysynthesis.Interms
| is a score | that  | shows preference |       | of that | particular | user for     |               |                 |          |            |         |
| ---------- | ----- | ---------------- | ----- | ------- | ---------- | ------------ | ------------- | --------------- | -------- | ---------- | ------- |
|            |       |                  |       |         |            |              | of generating | interest scores | of users | given news | item as |
| the active | item. | With the         | value | closer  | to +1      | meaning that |               |                 |          |            |         |
conditionalinput.
| the user                                             | would | like this | news | article | whereas | any score |                           |     |                         |     |     |
| ---------------------------------------------------- | ----- | --------- | ---- | ------- | ------- | --------- | ------------------------- | --- | ----------------------- | --- | --- |
|                                                      |       |           |      |         |         |           | Theobjectivefunctionofgen |     | canthereforebestatedas: |     |     |
| closerto-1implyingtheuser’sdislikefortheitem.Instate |       |           |      |         |         |           |                           |     | N                       |     |     |
w n w u , the gen N takes encoded news label as conditional minL =−E [D(G(z,y )),y ] (4)
|            |      |         |     |             |     |                 |     | genN yN,Z∼Pg(x) |     | N N |     |
| ---------- | ---- | ------- | --- | ----------- | --- | --------------- | --- | --------------- | --- | --- | --- |
| input from | news | encoder | E   | to generate |     | the interaction |     |                 |     |     |     |
N
scores as its output distribution. For both states c w and Formally,thisgeneratortakesrandomnoisezfromaguassian
|     |     |     |     |     |     | n u |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c n c u the generator gen N uses label provided by P N for distributiong(x)aslatentinputandgivenanewsclasslabel
synthesizing interaction scores. Due to its stability and the y , it generates a vector of synthetic interest scores G(·)
N
inherent sparsity in the historical interactions present in for all users and aims to minimize the distance between
our data, we used a conditional gan that uses Wasserstein fake and ground truth interactions between user-news pairs.
loss called conditional Wasserstein GAN (cWGAN) with The critic evaluates how well the generated scores match
the critic network during training to implement the gen N real user interest scores given the corresponding news item
model. and produces D(·) which is the output when it evaluates
| 16614 |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
FIGURE3. FlowdiagramofnewsrecommendationinGCZRecframework.
the sample G(·) generated by gen . As part of adversarial The model gen takes latent vector z from the gaussian
N U
training, the critic network aims to discern the synthetic distributionasinputalongwithuserclasslabely togenerate
U
interactiondistributionfromtherealonethatisproducedby thedistributionG(·)ofsyntheticinterestscoresforallnews
the generator. The activation used in the dense and output items with respect to the active user. The critic outputs its
layersofthisnetworkareLeakyReLUandtanhrespectively. evaluationD(·)ofthegeneratedinteractionscoresproduced
Thecriticnetworkuseslinearactivationsinsteadofsigmoid and gen tries to minimize the loss between real and fake
U
in the output layer and its output is the approximation of distributionofinteractionscores.
Wasserstein distance hence assigning lower values to fake
interactions. In the dense layers of this model, LeakyReLU D. WARMSTARTENCODERS
activationsareused.Duringtraining,theweightsofthecritic For warm start news, the class label y to be served to the
N
areclampedtoasmallrangeandthisnetworkisupdatedfive interestscoregeneratorgen isencodedbymappingtheraw
N
timescomparedtoasingleupdateofthegeneratorinorderto identifieroftheactivenewsitemtoauniquenumericid.This
improvethegenerationquality. encoded id is then used by E to collect the corresponding
N
labelofthenewsfromhistoricaldata.Inthesameway,warm
C. USERINTERESTSCOREGENERATORGEN U startuseridisencodedbyE U toauniquenumericidinorder
The input states determine the use of gen U for synthesizing toextracttheavailableclassy U ofthisactivewarmstartuser
interest scores for active news. These states are handled by inordertoprovideconditionalinputtogen U network.
g .Thegen takestheuserclasslabely oftheactiveuser
s U U
asitsconditionalinputandgeneratesfakeinterestscoresfor E. LATENTFEATUREREPRESENTATION
each news item in the system. The possible states managed In the GCZRec approach, we represent each news item N
by the gen are w w , w c and c c . The output of gen as a latent feature vector, denoted by δ. This representation
U n u n u n u U
is a vector of interest scores showing preferences given by isobtainedbyfeatureextractionprocessθ usingpre-trained
thisusertoeachoneofthenewsitems.Eachpositionofthis embedding to extract informative features from the textual
interaction vector representing a unique news and the value contentofthenewsitem.Thefeaturerepresentationyielded
at that index indicating a score in range -1 to +1 to show isδ=θ(N).
if that particular item can be interesting for the active user. Since the MIND and Addressa datasets do not contain
For state w w , the conditional variable for this model is any explicit user entity features, we transformed each user
n u
providedbytheuserencoderE asy .Forcasesw c and U into latent feature representation λ with the help of her
U U n u
c c thepredictedclasslabelyˆ fromthezero-shotpredictor historicalinteractionswiththenewscategories.Allthenews
n u U
P is used. Similar to gen the training of this network the user interacted with previously are treated as positive
U U
is done in an adversarial manner by employing a cWGAN samplesandusetoextractthehiddenfeatures.Thesefeatures
and a critic that uses Wasserstein loss. The activation in the are constructed as a process ρ which converts the list of
dense layers of both generator and critic are LeakyReLU categories and subcategories of each interacted news into
while the output layer of the critic uses linear activation one-hotencoding.Henceλ=ρ(U)becomestheuserprofile
and tanh activation is used for the output layer of the ofactiveuser.
synthesizer.
Theobjectivefunctionofgen canbestatedas: F. ZERO-SHOTCLASSIFIERS
U
Thecoldstartproblemforbothnewsitemsandusersistreated
minL genU =−E yU,Z∼Pg(x) [D(G(z,y U )),y U ] (5) aszero-shotclassificationtaskintheGCZRecapproach.For
VOLUME12,2024 16615

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
TABLE1. StatisticsofadressaandMINDdatasets. B. DATASETPREPROCESSING
|     |     |     |     |     |     |     | From the | users’ | behavioral |     | data provided | including |     | their |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --- | ------------- | --------- | --- | ----- |
impressionslogandnewsclickhistory,wefirstsampled70%
datafortrainingourmodelandleftthe30%forpost-training
evaluation.Foreachuser,thenewsitemforwhichtheyhave
|     |     |     |     |     |     |     | positive | interactions | were | found | by extracting |     | the news | id  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ---- | ----- | ------------- | --- | -------- | --- |
amongtheirnewsclickhistoryandalsofromtheimpressions
wheretheuserhada‘‘1’’asaclickbehaviorforaparticular
news.Weencodedallthepositiveinteractionsbetweenuser
andnewsasthevalue‘‘1’’duringtrainingdataconstruction.
| these zero-shot | predictions, |     | we  | employ | two classifiers | that |     |     |     |     |     |     |     |     |
| --------------- | ------------ | --- | --- | ------ | --------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
Thenegativeinteractionsbetweenusersandnewswerefound
| use the | latent feature | representation |     | to predict | a class | label |     |     |     |     |     |     |     |     |
| ------- | -------------- | -------------- | --- | ---------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
whentheuserdidnotclickthenewsandhencehasa0forthat
| for item | and user. | As a | result, | this allows | the predictors | to  |            |      |       |                 |      |     |         |      |
| -------- | --------- | ---- | ------- | ----------- | -------------- | --- | ---------- | ---- | ----- | --------------- | ---- | --- | ------- | ---- |
|          |           |      |         |             |                |     | particular | news | id in | the impressions | log. | We  | encoded | this |
leveragehiddencollaborativesignalsbetweenitemsandalso
|     |     |     |     |     |     |     | negative | interaction | as  | ‘‘-1’’ | in the training | data. | For | all the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ------ | --------------- | ----- | --- | ------- |
usersforpredictinglabelsintermsofsimilarityinthelatent
|     |     |     |     |     |     |     | news not | present | in either | a   | user’s historical | interactions |     | or  |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------- | --- | ----------------- | ------------ | --- | --- |
featurespace.
impressionslog,itwasassumedthattheuserwasnevershow
thenewsitemanddidnotinteractwithit.Theseinteractions
1) NEWSLABELPREDICTORP
|     |     |     | N   |     |     |     | are encoded | as  | ‘‘0’’ | for training. | Moreover, |     | for indexing |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ------------- | --------- | --- | ------------ | --- |
δ,
Given the latent news feature representation we classify purpose, each news id and user id is mapped to a unique
| a novel | item into | one of | K predefined |     | categories, | denoted |     |     |     |     |     |     |     |     |
| ------- | --------- | ------ | ------------ | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
numericnewsidandnumericuseridrespectively.Basedon
,...,
by y N1 , y N2 , y N3 y NK where K is the total number of their numeric indices, the final training set for gen was
N
newscategoriesinthedomain.Weimplementthenewslabel constructed by using the numeric id as index for a unique
predictorasa1Dconvolutionalneuralnetworkwithsoftmax
|     |     |     |     |     |     |     | instance | (row) | and each | numeric | user id | as a | feature | value |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------- | ------- | ------- | ---- | ------- | ----- |
activation in the output layer for prediction. The classifier (column).Inasimilarmanner,thefinaltrainingdataforgen
U
| calculates | the probability |     | P(y | |δ) for the | given news | item |                 |     |          |         |      |       |       |         |
| ---------- | --------------- | --- | --- | ----------- | ---------- | ---- | --------------- | --- | -------- | ------- | ---- | ----- | ----- | ------- |
|            |                 |     | Ni  |             |            |      | was constructed |     | by using | numeric | user | id as | index | for the |
belongingtoclassy Ni asstatedinequation6. instance(row)andeachnumericnewsidasindexforfeature
value(column).
ewi ·δ
|     |     | P(y |δ)= |     |     |     | (6) |                   |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | Ni       | Pk  | ·δ  |     |     |                   |     |     |     |     |     |     |     |
|     |     |          |     | ewj |     |     | C. IMPLEMENTATION |     |     |     |     |     |     |     |
j=1
|                           |     |     |     |                |     |     | For constructing |     | latent | feature | representations, |     | we  | used |
| ------------------------- | --- | --- | --- | -------------- | --- | --- | ---------------- | --- | ------ | ------- | ---------------- | --- | --- | ---- |
| Theassignednewscategoryyˆ |     |     |     | isexpressedas: |     |     |                  |     |        |         |                  |     |     |      |
N hierarchical clustering to assign contextual labels to each
|     |     |     |     |     |     |     | news item | based | on its | rich textual | features. | The | number | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------ | ------------ | --------- | --- | ------ | --- |
yˆ =argma x P(y |δ) (7) clusters selected based on silhouette score and discernment
|     |     | N   |     | Ni  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i
|     |     |     |     |     |     |     | was 32. | For        | user labels, | the    | hyperparameter |     | value     | for |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ------------ | ------ | -------------- | --- | --------- | --- |
|     |     |     |     |     |     |     | number  | of classes | was          | set to | 18 classes.    | The | embedding |     |
2) USERLABELPREDICTORP
U
Thisclassifierisusedtopredictthelabelforauserbasedon size for news and user is set to 300 to allow for baseline
|             |                |     | λ.      |         |                  |     | comparison. | For     | news, | pre-trained | Word2Vec   |               | embedding |     |
| ----------- | -------------- | --- | ------- | ------- | ---------------- | --- | ----------- | ------- | ----- | ----------- | ---------- | ------------- | --------- | --- |
| its feature | representation |     | Similar | to news | label predictor, |     |             |         |       |             |            |               |           |     |
|             |                |     |         |         |                  |     | are used    | whereas | for   | users we    | used count | vectorization |           | to  |
thearchitectureofthismodelisa1Dconvolutionalnetwork
with softmax function for finding the probability P(y |λ) perform the behavior encoding. The same architecture for
U
|             |         |      |        |       | ,...,   | i   | gen and | gen | is used | with | a dropout | rate of | 0.5, learning |     |
| ----------- | ------- | ---- | ------ | ----- | ------- | --- | ------- | --- | ------- | ---- | --------- | ------- | ------------- | --- |
| of the user | falling | into | one of | the y | , y , y | y   | N       | U   |         |      |           |         |               |     |
U1 U2 U3 UM rateof0.0002,LeakyReLUasactivationinthedenselayers,
categories.Theposteriorprobabilityforfindingtheuserlabel
andlabelassignmentisshownasfollows: tanh as non-linearity for the generator output layer. Adam
|     |     |      |     |     |     |     | is used as                                       | optimizer |     | with hyperparameters |     | β1  | =0.9 | and |
| --- | --- | ---- | --- | --- | --- | --- | ------------------------------------------------ | --------- | --- | -------------------- | --- | --- | ---- | --- |
|     |     |      | ewi | ·λ  |     |     | β2=0.999.AspartofthecWGAN,thecriticistrainedwith |           |     |                      |     |     |      |     |
|     | P(y | |λ)= |     |     |     | (8) |                                                  |           |     |                      |     |     |      |     |
Ui Pk ·λ clippedweights.Boththezero-shotpredictorsaretrainedas
ewj
|     |     |     | j=1     |     |     |     | multi-classclassifierswithconv1dhiddenlayers,batchnorm  |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | yˆ  | =argmax | P(y | |λ) | (9) |                                                         |     |     |     |     |     |     |     |
|     |     | U   |         | Ui  |     |     | regularization,dropoutrateof0.5,learningrateof0.0005and |     |     |     |     |     |     |     |
i
softmaxactivation.
V. EXPERIMENTS
| A. DATASETDETAILS |              |     |         |     |                    |     | D. BASELINEMODELS |        |                |      |              |     |             |     |
| ----------------- | ------------ | --- | ------- | --- | ------------------ | --- | ----------------- | ------ | -------------- | ---- | ------------ | --- | ----------- | --- |
|                   |              |     |         |     |                    |     | In terms          | of the | recommendation |      | objective,   |     | the GCZRec  |     |
| For the           | experiments, |     | we used | the | publicly available |     |                   |        |                |      |              |     |             |     |
|                   |              |     |         |     |                    |     | framework         | is     | compared       | with | the existing |     | recommender |     |
MIND[20]andAdressa[21]newsrecommendationdatasets.
The key statistics for both of these datasets are provided in modelstovalidatetheperformanceoftheproposedapproach.
Themodelsarelistedas:
Table1.Thedatasetscontainsclickbehaviorofusersfornews
items. The data include information like impressions, news • GAZRec-NPA [37]: A three-tower generative zero-
categories,subcategories,abstractandtextualcontent. shot framework to generate generalized behavior
| 16616 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
TABLE2. ComparativeresultsofGCZReconMINDandadressadatasetsinexclusivelycoldstartcase.
TABLE3. ComparativeresultsofGCZReconMINDandadressadatasetsinmixedcoldstartandwarmstartcase.
| representationsofusersanditemsforrecommendation |     |     |     |     |     |     | positionk: |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
andthenusetheserepresentationforcoldstartandwarm
DCG@k
| startpredictionsusinganeuralclickpredictor. |     |     |     |     |     |     |     |     | nDCG@k | =   |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
(11)
| GNUD[39]:Theuserandnewsinteractionsaretreated |     |     |     |     |     |     |     |     |     | IDCG@k |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
•
ashigh-ordergraphinordertoexploitlatentpreference Tomeasuretheperformanceofrecommendersystemusing
factorsoftheusertoperformrecommendation.
averageprecisiongiventop-krecommendationsovermultiple
• NAML[40]:Aneuralnewsrecommendationapproach valuesofkweuseMAPwhichisdefinedas:
| with | attentive | multi-view |     | learning | in which | user repre- |     |     |     |     |     |     |     |
| ---- | --------- | ---------- | --- | -------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
PK
sentationislearnedusingtheirbrowsedhistoryandother AveragePrecision@k
|     |     |     |     |     |     |     |     | MAP= | k=1 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
(12)
| information |     | as well | as news | attributes | such | as title and |     |     |     |     | K   |     |     |
| ----------- | --- | ------- | ------- | ---------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
categoryareusedforitemrepresentation.
F. TESTENVIRONMENT
|     |     |     |     |     |     |     | For model | training | and | performance | evaluation |     | we divided |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ----------- | ---------- | --- | ---------- |
E. EVALUATIONMETRICS
|             |         |             |               |        |            |        | the test    | data into | two distinct | sets. | From           | the total | test data |
| ----------- | ------- | ----------- | ------------- | ------ | ---------- | ------ | ----------- | --------- | ------------ | ----- | -------------- | --------- | --------- |
| To evaluate | the     | performance |               | of the | proposed   | GCZRec |             |           |              |       |                |           |           |
|             |         |             |               |        |            |        | we selected | 50%       | cold start   | items | for evaluating |           | the model |
| framework   | against |             | the baseline, | four   | evaluation | mea-   |             |           |              |       |                |           |           |
inanexclusivelycoldstartsetting.Theremainingcoldstart
| sures are | used  | as performance |        | indicators. | These | metrics    |             |      |          |       |          |      |             |
| --------- | ----- | -------------- | ------ | ----------- | ----- | ---------- | ----------- | ---- | -------- | ----- | -------- | ---- | ----------- |
|           |       |                |        |             |       |            | items along | with | the warm | start | data was | used | to generate |
| are Area  | Under | Curve          | (AUC), | normalized  |       | Discounted |             |      |          |       |          |      |             |
recommendationsformixedcold-warmnewsitems.
| Cumulative | Gain | (nDCG@k) |     | and Mean | Average | Precision |     |     |     |     |     |     |     |
| ---------- | ---- | -------- | --- | -------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
Thethresholdvalueforrecommendationofagivenitemis
(MAP).
fixedto0.5andthevaluesusedforhyperparameterkare1,
| The AUC                           | can | be measured |     | in terms | of true | positive rate |                          |     |     |     |     |     |     |
| --------------------------------- | --- | ----------- | --- | -------- | ------- | ------------- | ------------------------ | --- | --- | --- | --- | --- | --- |
| (TPR)andfalsepositiverate(FPR)as: |     |             |     |          |         |               | 5and10.                  |     |     |     |     |     |     |
|                                   | n   |             |     |          |         |               | VI. RESULTSANDDISCUSSION |     |     |     |     |     |     |
X1
AUC ≈ (TPR +TPR )(FPR −FPR ) (10) In this section, the effectiveness of the proposed approach
|     |     |     | i   | i−1 | i   | i−1 |              |     |     |                    |     |                 |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ------------------ | --- | --------------- | --- |
|     |     | 2   |     |     |     |     | is evaluated | and | the | results indicating |     | the performance |     |
i=1
|     |     |     |     |     |     |     | on benchmark |     | datasets | are reported. |     | These | results are |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | ------------- | --- | ----- | ----------- |
The nDCG@k is a measure of ranking quality in the list summarizedinTable2forcoldstartcaseandinTable3for
of recommended items with IDCG as the ideal DCG and mixedcaseofbothcoldstartandwarmstartitems.
| VOLUME12,2024 |     |     |     |     |     |     |     |     |     |     |     |     | 16617 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
Abreakdownofmodelperformanceintodifferentaspects TABLE4. Percentageofnovelnews.
| is needed | in         | order | to effectively | discuss     |     | the outcomes |     |     |     |     |     |
| --------- | ---------- | ----- | -------------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- |
| of GCZRec | framework. |       | These          | performance |     | aspects      | are |     |     |     |     |
presentedinthefollowingsubsections.
A. CLASSIFICATIONPERFORMANCE
| The performance |            | of  | generator | networks       | in  | the GCZRec |     |     |     |     |     |
| --------------- | ---------- | --- | --------- | -------------- | --- | ---------- | --- | --- | --- | --- | --- |
| for scores      | generation |     | is done   | in the context |     | of number  | of  |     |     |     |     |
correctinterestscoregenerationforagivennewsitem.With
| the help | of threshold |          | value, | each individual |     | interest | score |     |     |     |     |
| -------- | ------------ | -------- | ------ | --------------- | --- | -------- | ----- | --- | --- | --- | --- |
| produced | in the       | interest | vector | can itself      | be  | treated  | as a  |     |     |     |     |
binaryclassprediction.Thecombinedperformanceofthese
| positive     | and negative |                 | scores      | generation | are represented |            | by     |                                                 |     |     |     |
| ------------ | ------------ | --------------- | ----------- | ---------- | --------------- | ---------- | ------ | ----------------------------------------------- | --- | --- | --- |
| the AUC      | values       | as presented    |             | in Table   | 2 and           | Table      | 3. The |                                                 |     |     |     |
| results show | significant  |                 | improvement | in         | cold            | start case | for    |                                                 |     |     |     |
|              |              |                 |             |            |                 |            |        | FIGURE4. Precision-recallcurveforcoldstartcase. |     |     |     |
| MIND but     | slightly     | under-performed |             | on         | Adressa         | against    | the    |                                                 |     |     |     |
baselineformixedcold-warmstartcase.Thismaybedueto
| the label | encoding | scheme | used | for the | Adressa | categories. |     |     |     |     |     |
| --------- | -------- | ------ | ---- | ------- | ------- | ----------- | --- | --- | --- | --- | --- |
Itcanbefurtherinvestigatedwhethercategorycondensation
inthedatasetaffectedthepredictionaccuracy.
B. PRECISION-RECALLTRADE-OFF
| The GCZRec   |            | model | offers | significant    | improvement |           | over   |     |     |     |     |
| ------------ | ---------- | ----- | ------ | -------------- | ----------- | --------- | ------ | --- | --- | --- | --- |
| the existing | approaches |       | and    | the positional |             | relevance | of     |     |     |     |     |
| recommended  |            | news  | items  | are taken into | account     |           | by the |     |     |     |     |
syntheticinteractiongenerators.ForbothMINDandAdressa
dataset,theMAPscoregivenbytheproposedmodelshows
|                |     |          |      |                |       |           |     | FIGURE5. Precision-recallcurveformixedcold-warmstartcase. |     |     |     |
| -------------- | --- | -------- | ---- | -------------- | ----- | --------- | --- | --------------------------------------------------------- | --- | --- | --- |
| an improvement |     | in both  | cold | start and      | mixed | warm-cold |     |                                                           |     |     |     |
| start cases.   | But | compared |      | to purely cold | start | items,    | the |                                                           |     |     |     |
improvements in mixed case recommendations were much findingthepercentageofnewhighinterestnewsitemfound
more significant. The precision-recall curve for k=1, 5 and over5,10,25and50generationsgiventhesameuserasinput
10forMINDandAdressadatasetsinbothcasesisillustrated to gen . A summary of this is presented in Table 4. It can
U
alsobearguedthatthediversityismeasurableforgenerations
inFig.4andFig.5.
|     |     |     |     |     |     |     |     | producedbythegen | N inthesamemanner. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------------ | --- | --- |
C. RANKINGQUALITY Basedonthecomparativeresults,itcanbestatedthatthe
In terms of the ranking quality of news items in both cold proposed GCZRec framework provides more accurate and
startandwarmstartcases,theproposedGCZRecframework relevantrankedrecommendationofcoldstartandwarmstart
newsitemstousersalsoincorporatesdiversitybyleveraging
clearlyoutperformsbaselinemodelswiththehighestaverage
improvement of +0.1113 is observed when top-5 items are latent collaborative information present in feature space of
considered as shown by ndcg@k values for k=1, 5 and usersanditems.
| 10. The | overall | value | of relative | ranking | in  | the proposed |     |     |     |     |     |
| ------- | ------- | ----- | ----------- | ------- | --- | ------------ | --- | --- | --- | --- | --- |
approach can be attributed to the gen and gen learning VII. CONCLUSION
|     |     |     |     | N   |     | N   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theunderlyinginterestdistributionfromthedatatoproduce Inthispaper,wepresentedtheGCZRecframeworkforcold
synthetic interest scores. These scores in their raw form are start news recommendation. We formulated the problem of
used as is to provide the ranking of relevant items that are cold start recommendation as zero-shot classification task
recommended. and proposed that these recommendations can be diverse
|     |     |     |     |     |     |     |     | and have serendipity | if user and | item information | are |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ----------- | ---------------- | --- |
D. SERENDIPITY implicitly used during training. Unlike existing models,
For the inherently challenging and subjective aspect of the GCZRec approach allows the interest scores to be
evaluating the proposed system in terms of expanding the generated directly for a given news or user in both warm
interestofusersintoneighbouringnewscategories,wemodel start and cold start cases. Two separate wCGAN networks
the results of GCZRec as a collaborative recommendation are trained on interaction between users and news items in
outcome. This is done in an implicit manner as the order to allow collaborative signals to be implicitly used
output generated by gen N and gen U use the interaction for producing synthetic interactions at testing time. For any
between similar user and news. We measure the diversity unseenuserornewsitem,themodelmakesuseofzero-shot
ofrecommendationsproducedusingGCZRecframeworkby predictors implemented as 1D-CNN classifiers. Results on
| 16618 |     |     |     |     |     |     |     |     |     | VOLUME12,2024 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
twobenchmarkdatasetsindicatethatourproposedapproach [15] H. Ding, Y. Ma, A. Deoras, Y. Wang, and H. Wang, ‘‘Zero-shot
offers significant improvement in the accuracy and ranking recommendersystems,’’2021,arXiv:2105.08318.
[16] R.J.ZiaraniandR.Ravanmehr,‘‘Serendipityinrecommendersystems:
| of news | items for cold | start | recommendation |     | and also sets |     |     |     |     |     |     |     |
| ------- | -------------- | ----- | -------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Asystematicliteraturereview,’’J.Comput.Sci.Technol.,vol.36,no.2,
| a standard | for incorporating |     | serendipity | by  | implicitly using |     |     |     |     |     |     |     |
| ---------- | ----------------- | --- | ----------- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
pp.375–396,Apr.2021.
|               |             |      |              |     |             | [17] D. Kotkov, | J. Veijalainen, |     | and S. | Wang, ‘‘How | does | serendipity affect |
| ------------- | ----------- | ---- | ------------ | --- | ----------- | --------------- | --------------- | --- | ------ | ----------- | ---- | ------------------ |
| collaborative | information | with | a generative |     | recommender |                 |                 |     |        |             |      |                    |
diversityinrecommendersystems?Aserendipity-orientedgreedyalgo-
systeminzero-shotmanner.
rithm,’’Computing,vol.102,no.2,pp.393–411,Feb.2020.
|     |     |     |     |     |     | [18] S. Inoue | and M. | Tokumaru, | ‘‘Serendipity |     | recommender | system for |
| --- | --- | --- | --- | --- | --- | ------------- | ------ | --------- | ------------- | --- | ----------- | ---------- |
academicdisciplines,’’inProc.Joint11thInt.Conf.SoftComput.Intell.
A. LIMITATIONSANDFUTUREWORK
Syst.21stInt.Symp.Adv.Intell.Syst.(SCIS-ISIS),Dec.2020,pp.1–4.
| The current | limitation | of our | model | include | its inability |                 |     |          |              |     |            |                |
| ----------- | ---------- | ------ | ----- | ------- | ------------- | --------------- | --- | -------- | ------------ | --- | ---------- | -------------- |
|             |            |        |       |         |               | [19] T. Dorjmaa | and | T. Shin, | ‘‘Evaluating | the | quality of | recommendation |
to consider the correlation between news items and tem- systembyusingserendipitymeasure,’’vol.25,no.4,pp.89–103,2019.
[20] F.Wu,Y.Qiao,J.-H.Chen,C.Wu,T.Qi,J.Lian,D.Liu,X.Xie,J.Gao,and
| poral relation | between | news | clicks. | Both of | these aspects, |     |     |     |     |     |     |     |
| -------------- | ------- | ---- | ------- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
W.Wu,‘‘MIND:Alarge-scaledatasetfornewsrecommendation,’’inProc.
if incorporated, can be important in further improving the 58thAnnu.MeetingAssoc.Comput.Linguistics,2020,pp.3597–3606.
recommendationqualityoftheGCZRecmodel. [21] J.A.Gulla,L.Zhang,P.Liu,Ö.Özgöbek,andX.Su,‘‘Theadressadataset
Infuturework,wealsoaimtoimproveourframeworkto fornewsrecommendation,’’inProc.Int.Conf.WebIntell.,Aug.2017,
pp.1042–1048.
allowcross-domainrecommendationproblemstobehandled. [22] M.KompanandM.Bieliková,‘‘Content-basednewsrecommendation,’’in
Forthis,existingknowledgedistillationmodelscanbeused Proc.11thInt.Conf.e-commerceWebTechnol.(EC-Web)(LectureNotes
to allow learned knowledge from source domain to be in Business Information Processing). Berlin, Germany: Springer, 2010,
pp.61–72.
transferredtoamodelsettorecommenditemsthatarepresent [23] M.Capelle,F.Frasincar,M.Moerland,andF.Hogenboom,‘‘Semantics-
intargetdomain. basednewsrecommendation,’’inProc.2ndInt.Conf.WebIntell.,Mining
Semantics,Jun.2012,pp.1–9.
[24] M.Moerland,F.Hogenboom,M.Capelle,andF.Frasincar,‘‘Semantics-
REFERENCES basednewsrecommendationwithSF-IDF+,’’inProc.3rdInt.Conf.Web
Intell.,MiningSemantics,Jun.2013,pp.1–8.
[1] A.Bermes,‘‘Informationoverloadandfakenewssharing:Atransactional
stressperspectiveexploringthemitigatingroleofconsumers’resilience [25] K.JosephandH.Jiang,‘‘Contentbasednewsrecommendationviashortest
during COVID-19,’’ J. Retailing Consum. Services, vol. 61, Jul. 2021, entitydistanceoverknowledgegraphs,’’inProc.CompanionWorldWide
| Art.no.102555. |     |     |     |     |     | WebConf.,May2019,pp.690–699. |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
[26] D.BillsusandM.J.Pazzani,‘‘Usermodelingforadaptivenewsaccess,’’
[2] S.Feng,J.Meng,andJ.Zhang,‘‘Newsrecommendationsystemsinthe
UserModel.User-AdaptedInteract.,vol.10,pp.147–180,Jun.2000.
eraofinformationoverload,’’J.WebEng.,vol.20,no.2,pp.459–470,
Mar.2021. [27] P.LenhartandD.Herzog,‘‘Combiningcontent-basedandcollaborative
[3] M.Zihayat,A.Ayanso,andX.Zhao,‘‘Autility-basednewsrecommenda- filtering for personalized sports news recommendations,’’ in Proc.
CBRecSys@RecSys,2016,pp.3–10.
tionsystem,’’Decis.SupportSyst.,vol.117,pp.14–27,Feb.2019.
[28] W.Yang,R.Tang,andL.Lu,‘‘Newsrecommendationmethodbyfusion
[4] D.Goldberg,D.Nichols,B.M.Oki,andD.Terry,‘‘Usingcollaborative
ofcontent-basedrecommendationandcollaborativefiltering,’’J.Comput.
filteringtoweaveaninformationtapestry,’’Commun.ACM,vol.35,no.12,
| pp.61–70,Dec.1992. |     |     |     |     |     | Appl.,vol.36,no.2,p.414,2016. |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- |
[29] C.Wu,F.Wu,M.An,Y.Huang,andX.Xie,‘‘Neuralnewsrecommenda-
[5] Y.Koren,S.Rendle,andR.Bell,‘‘Advancesincollaborativefiltering,’’
tionwithtopic-awarenewsrepresentation,’’inProc.57thAnnu.Meeting
inRecommenderSystemsHandbook.Boston,MA,USA:Springer,2021,
Assoc.Comput.Linguistics,2019,pp.1154–1159.
pp.91–142.
|     |     |     |     |     |     | [30] M. An, | F. Wu, C. | Wu, K. | Zhang, | Z. Liu, | and X. Xie, | ‘‘Neural news |
| --- | --- | --- | --- | --- | --- | ----------- | --------- | ------ | ------ | ------- | ----------- | ------------- |
[6] P.DeHandschutter,N.Gillis,andX.Siebert,‘‘Asurveyondeepmatrix
recommendationwithlong-andshort-termuserrepresentations,’’inProc.
factorizations,’’Comput.Sci.Rev.,vol.42,Nov.2021,Art.no.100423. 57thAnnu.MeetingAssoc.Comput.Linguistics,2019,pp.336–345.
[7] M.J.PazzaniandD.Billsus,‘‘Content-basedrecommendationsystems,’’
|        |               |         |                |     |                      | [31] C. Wu, | F. Wu, | M. An, | J. Huang, | Y. Huang, | and | X. Xie, ‘‘NPA: |
| ------ | ------------- | ------- | -------------- | --- | -------------------- | ----------- | ------ | ------ | --------- | --------- | --- | -------------- |
| in The | Adaptive Web: | Methods | and Strategies | of  | Web Personalization. |             |        |        |           |           |     |                |
Neuralnewsrecommendationwithpersonalizedattention,’’inProc.25th
Berlin,Germany:Springer,2007,pp.325–341.
|     |     |     |     |     |     | ACM | SIGKDD Int. | Conf. | Knowl. | Discovery | Data Mining, | Jul. 2019, |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | --------- | ------------ | ---------- |
[8] C.N.Sunilkumar,‘‘Areviewofmovierecommendationsystem:Limita-
pp.2576–2584.
tions,surveyandchallenges,’’ELCVIAElectron.Lett.Comput.Vis.Image [32] J. Wang, L. Yu, W. Zhang, Y. Gong, Y. Xu, B. Wang, P. Zhang, and
Anal.,vol.19,no.3,pp.18–37,Sep.2020.
|                  |                 |           |            |        |                     | D. Zhang,      | ‘‘IRGAN:    | A   | minimax   | game      | for unifying | generative and |
| ---------------- | --------------- | --------- | ---------- | ------ | ------------------- | -------------- | ----------- | --- | --------- | --------- | ------------ | -------------- |
| [9] P. Lops,     | D. Jannach,     | C. Musto, | T. Bogers, | and    | M. Koolen, ‘‘Trends |                |             |     |           |           |              |                |
|                  |                 |           |            |        |                     | discriminative | information |     | retrieval | models,’’ | in Proc.     | 40th Int. ACM  |
| in content-based | recommendation: |           | Preface    | to the | special issue on    |                |             |     |           |           |              |                |
SIGIRConf.Res.Develop.Inf.Retr.,Aug.2017,pp.515–524.
recommendersystemsbasedonrichitemdescriptions,’’UserModel.User- [33] H. Wang, J. Wang, J. Wang, M. Zhao, W. Zhang, F. Zhang, X. Xie,
AdaptedInteract.,vol.29,no.2,pp.239–249,Apr.2019. andM.Guo,‘‘GraphGAN:Graphrepresentationlearningwithgenerative
| [10] M.H.Mohamed, | M.H.Khafagy,andM. |     |     | H.Ibrahim,‘‘Recommender |     |     |     |     |     |     |     |     |
| ----------------- | ----------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
adversarialnets,’’inProc.AAAIConf.Artif.Intell.,vol.32,2018,pp.1–8.
systemschallengesandsolutionssurvey,’’inProc.Int.Conf.Innov.Trends
[34] Y.Zhou,J.Xu,J.Wu,Z.T.Nasrabadi,E.Korpeoglu,K.Achan,andJ.He,
Comput.Eng.(ITCE),Feb.2019,pp.149–155.
‘‘GAN-basedrecommendationwithpositive-unlabeledsampling,’’2020,
[11] J.Li,M.Jing,K.Lu,L.Zhu,Y.Yang,andZ.Huang,‘‘Fromzero-shot arXiv:2012.06901.
learningtocold-startrecommendation,’’inProc.AAAIConf.Artif.Intell., [35] S. Kumar and M. D. Gupta, ‘‘c+GAN: Complementary fashion item
vol.33,2019,pp.4189–4196.
recommendation,’’2019,arXiv:1906.05596.
| [12] W. Wang, | V. W. Zheng, | H. Yu, | and C. Miao, | ‘‘A | survey of zero-shot |                 |           |       |     |                  |          |          |
| ------------- | ------------ | ------ | ------------ | --- | ------------------- | --------------- | --------- | ----- | --- | ---------------- | -------- | -------- |
|               |              |        |              |     |                     | [36] W. Shafqat | and Y.-C. | Byun, | ‘‘A | hybrid GAN-based | approach | to solve |
learning:Settings,methods,andapplications,’’ACMTrans.Intell.Syst. imbalanced data problem in recommendation systems,’’ IEEE Access,
Technol.,vol.10,no.2,pp.1–37,Mar.2019. vol.10,pp.11036–11047,2022.
[13] S.YinandX.Luo,‘‘Asurveyoflearning-basedmethodsforcold-start, [37] M.A.AlshehriandX.Zhang,‘‘Generativeadversarialzero-shotlearning
socialrecommendation,anddatasparsityine-commercerecommendation forcold-startnewsrecommendation,’’inProc.31stACMInt.Conf.Inf.
systems,’’ in Proc. 16th Int. Conf. Intell. Syst. Knowl. Eng. (ISKE), Knowl.Manage.,Oct.2022,pp.26–36.
Nov.2021,pp.276–283. [38] D.-K. Chae, J. A. Shin, and S.-W. Kim, ‘‘Collaborative adversarial
[14] T. Wu, E. K.-I. Chio, H.-T. Cheng, Y. Du, S. Rendle, D. Kuzmin, autoencoders:AneffectivecollaborativefilteringmodelundertheGAN
R. Agarwal, L. Zhang, J. Anderson, S. Singh, T. Chandra, E. H. Chi, framework,’’IEEEAccess,vol.7,pp.37650–37663,2019.
W.Li,A.Kumar,X.Ma,A.Soares,N.Jindal,andP.Cao,‘‘Zero-shot [39] L.Hu,S.Xu,C.Li,C.Yang,C.Shi,N.Duan,X.Xie,andM.Zhou,
heterogeneoustransferlearningfromrecommendersystemstocold-start ‘‘Graphneuralnewsrecommendationwithunsupervisedpreferencedis-
search retrieval,’’ in Proc. 29th ACM Int. Conf. Inf. Knowl. Manage., entanglement,’’inProc.58thAnnu.MeetingAssoc.Comput.Linguistics,
| Oct.2020,pp.2821–2828. |     |     |     |     |     | 2020,pp.4255–4264. |     |     |     |     |     |       |
| ---------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | ----- |
| VOLUME12,2024          |     |     |     |     |     |                    |     |     |     |     |     | 16619 |

S.Z.U.Hassanetal.:GCZRec:GenerativeCollaborativeZero-ShotFrameworkforColdStartNewsRecommendation
[40] C. Wu, F. Wu, M. An, J. Huang, Y. Huang, and X. Xie, ‘‘Neu- MUHAMMAD RAFI was born in Karachi,
ral news recommendation with attentive multi-view learning,’’ 2019, Pakistan.HereceivedtheB.S.andM.S.degrees
arXiv:1907.05576. in computer science from the FAST-Institute
of Computer Science, University of Karachi,
Pakistan,in1996and2000,respectively,andthe
Ph.D.degreeincomputersciencein2017.Hehas
more than ten years of experience in software
development and also a Consultant for the local
software industry. His current research interests
includealgorithmdevelopment,machinelearning,
information retrieval, text/data mining, time series analysis, and natural
language processing. He has received several travel grant awards for
presenting his work at the top conferences. He has served as a Judge
andaTechnicalQualityReviewTeamatmanyversionsforIEEEXtreme
Programming Competitions. He has served as a reviewer for various
internationaljournalsofhighimpact.
JAROSLAV FRNDA (Senior Member, IEEE)
was born in Slovakia, in 1989. He received the
M.Sc.andPh.D.degreesfromtheDepartmentof
SYED ZAIN UL HASSAN wasborninKarachi, Telecommunications,VSB—TechnicalUniversity
Pakistan. He received the M.C.S. degree from of Ostrava, Czech Republic, in 2013 and 2018,
theUniversityofKarachi,in2014,andtheM.S. respectively.HeiscurrentlyanAssistantProfessor
degree in computer science from the National with the University of Z˘ilina, Slovakia. He has
UniversityofComputerandEmergingSciences, authored or coauthored more than 85 journal
in2018,whereheiscurrentlypursuingthePh.D. articlesinWebofScience.Hisresearchinterests
degree in computer science. He has more than include the quality of multimedia services in IP
eight years of teaching experience and was a networks,dataanalysis,andmachinelearningalgorithms.In2022,hewas
Developeratasoftwareserviceproviderforalmost theFinalistoftheCategoryOutstandingScientistinSlovakiaundertheage
twoyears.Hisresearchinterestsincludemachine of35-ESETScienceAward,in2022.
learning,generativeAI,recommendationsystems,andlargelanguagemodel.
16620 VOLUME12,2024