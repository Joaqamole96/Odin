Received1May2025,accepted19May2025,dateofpublication22May2025,dateofcurrentversion12June2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3572865
Machine Learning in E-Commerce: Trends,
Applications, and Future Challenges
ELIASDRITSAS ANDMARIATRIGKA
DepartmentofInformaticsandComputerEngineering,UniversityofWestAttica,12243Athens,Greece
Correspondingauthor:EliasDritsas(idritsas@uniwa.gr)
ThepublicationofthearticleinOAmodewasfinanciallysupportedbyHEAL-Link.
ABSTRACT The rapid evolution of e-commerce has been significantly influenced by the integration of
machinelearning(ML)anddatasciencetechniques.Thepresentsurveyprovidesacomprehensiveoverview
ofhowMLmethodsareappliedacrossvariousfunctionaldomainsine-commerce,includingpersonalized
recommendations, dynamic pricing, fraud detection, customer segmentation, and behavioral analysis.
WecategorizeandevaluateawiderangeofMLparadigms,namelysupervised,unsupervised,reinforcement,
and hybrid learning, as well as emerging approaches such as neurosymbolic artificial intelligence (AI),
federatedlearning(FL),andquantumML(QML).Keychallengesrelatedtoscalability,interpretability,cold-
startproblems,datasparsity,andprivacyarecriticallyanalyzed.Additionally,wehighlightunderexplored
areas,suchascontinuallearning(CL)andmulti-agentarchitecturesincommerce.Thesurveyincorporates
comparative tables, real-world use cases, and a taxonomy of methods to support both academic
and industrial perspectives. Ultimately, by analyzing trends and gaps in the literature, we provide a
forward-lookingresearchroadmapthatbridgesMLinnovationswiththeevolvingdemandsofe-commerce
ecosystems.
INDEX TERMS Machine learning, e-commerce, predictive analytics, recommendation systems,
personalization,optimization.
I. INTRODUCTION segmentation, and dynamic pricing strategies. By lever-
The rapid expansion of e-commerce has transformed how aging techniques such as supervised and unsupervised
businesses interact with consumers, manage supply chains, learning, deep learning (DL), and reinforcement learning
and optimize operations. The increasing digitization of (RL), businesses can extract meaningful insights from
commercehasgeneratedvastvolumesofdatafromconsumer data, anticipate consumer needs, and optimize operational
interactions, product searches, transaction histories, and efficiency[3].
behavioural analytics. Traditional rule-based approaches In addition, recommendation engines, powered by col-
to managing these data streams have proven inadequate laborative filtering and neural networks, personalize user
in handling the complexity and dynamism of modern experiences by predicting product preferences. At the same
digital marketplaces. ML has emerged as a transformative time, fraud detection models employ anomaly detection
force, offering intelligent automation, adaptive decision- techniques to secure financial transactions against cyber
making, and predictive analytics to enhance e-commerce threats[4],[5].
efficiency[1],[2]. Despite its transformative potential, integrating ML
ML algorithms play a pivotal role in multiple aspects of into e-commerce presents several challenges. Data privacy
e-commerce, including personalized recommendation sys- concerns, interpretability issues, computational constraints,
tems, fraud detection, demand forecasting, customer and evolving fraud tactics pose significant obstacles to
widespread adoption. Ensuring transparency in AI-driven
The associate editor coordinating the review of this manuscript and decision-making remains a critical issue, particularly in
domainssuchasalgorithmicpricingandtargetedadvertising.
approvingitforpublicationwasAymanEl-Baz .
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
99048 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
Furthermore, the need for scalable, real-time ML models werecustomizedperdatabaseusingappropriateBooleanand
capable of handling billions of transactions and user inter- truncationoperators.
actions highlights the growing demand for computational Inclusion criteria required that studies be peer-reviewed,
efficiencyandrobustmodelarchitectures[6],[7]. writteninEnglish,andfocusedontheapplication,evaluation,
or deployment of ML models within e-commerce contexts.
Articles also needed to contain technical insights, system-
A. MOTIVATION level contributions, or architectural innovations relevant to
The proliferation of e-commerce has led to increasingly commercial environments. We excluded purely theoretical
complex,high-velocitydigitalmarketplaceswhereconsumer works, non-peer-reviewed sources, non-English texts, and
expectations, fraud vectors, and product dynamics evolve duplicateentries.
in real-time. In this environment, conventional rule-based The selected literature was then classified across three
systems fail to provide the adaptability, scalability, and analytical dimensions. The first considered the various
personalization required for modern commerce. Although typesofMLapproaches,includingsupervised,unsupervised,
MLoffersapathforwardthroughintelligentautomationand reinforcement,hybrid,meta-learning,neurosymbolicAI,FL,
predictivemodeling,itsintegrationintoe-commercesystems and quantum models. The second dimension focused on
isstillhinderedbymajorchallenges,includingdatasparsity, the functional domain, such as recommendation, customer
modelinterpretability,complianceconstraints,andreal-time segmentation, dynamic pricing, fraud detection, and inven-
processingbottlenecks. toryforecasting.Thethirddimensioncapturedcross-cutting
Moreover, while the literature on ML in e-commerce challenges like scalability, latency, interpretability, data
is expanding, it remains fragmented across domains such sparsity,andprivacy.
as recommendation systems, fraud detection, and pricing Thisthematicclassificationguidedthetaxonomy,compar-
optimization. Prior surveys often lack technical depth, ativetables,andsynthesispresentedinsubsequentsections.
focus on limited use cases, or fail to incorporate emerging It also provided the basis for identifying gaps in current
paradigms like neurosymbolic AI, CL, FL, and QML. As a practiceandopportunitiesforfutureresearchinML-powered
result, there is a pressing need for a unified, technically e-commercesystems.
rigorous synthesis bridging foundational and frontier ML Figure 1 offers a synthesized map of the survey’s
techniqueswithe-commerce-specificchallenges. thematicscope,illustratinghowMLtechniquesintersectwith
This survey responds to that gap by systematically practicaldemandsandunresolvedchallengesine-commerce.
mapping ML paradigms to functional domains in digital It captures the interplay between learning strategies, their
commerce,analyzingtrade-offs,andsurfacingunderexplored operationalroles,systemicbottlenecks,andforward-looking
research directions. The goal is to provide researchers and innovations,servingasavisualreferenceforthestructureand
practitioners with a comprehensive reference framework to flowoftheanalysisthatfollows.
guidethescalable,trustworthy,andfuture-proofdeployment
ofMLincomplexe-commerceecosystems.
C. CONTRIBUTION
This survey presents a comprehensive and forward-looking
B. METHODOLOGY frameworkthatnotonlyconsolidatesrecentMLapplications
Thissurveyadoptsastructuredandtransparentmethodology ine-commercebutalsoextendspriorworkbysystematically
inspiredbybestpracticesinAIsystemsresearch,particularly aligning ML paradigms with functional roles, system-level
the multi-stage framework outlined in recent literature on constraints, and emerging research challenges. In contrast
artificial general intelligence development [8]. The review to earlier surveys that either focus on narrow use cases
process was designed to ensure both coverage and repro- (e.g., churn prediction or recommendation only) or offer
ducibility through a sequence of defined stages, including generalized overviews without technical depth, our paper
databasequerying,filtering,classification,andsynthesis. makesthefollowingdistinctcontributions
We conducted a targeted search across major academic
databases, such as IEEE Xplore, ACM Digital Library, • We dissect five ML paradigms—supervised, unsuper-
SpringerLink,ScienceDirect,andGoogleScholar.Thesearch vised,reinforcement,hybrid,andmeta-learning,linking
focusedonpublicationsfromthelastsevenyearstocapture eachtospecifice-commercefunctions(e.g.,frauddetec-
themostrecentadvancementsinMLanditsintegrationinto tion, inventory management, conversational AI) and
digital commerce. Search queries combined terms related elaboratingonarchitecturalvariantsandcomputational
to core ML techniques and e-commerce domains. For trade-offs.Thismovesbeyondtaxonomytoafunctional
example, combinations such as (‘‘machine learning’’ OR andoperationalmapping.
‘‘deep learning’’ OR ‘‘reinforcement learning’’) AND ‘‘e- • The survey is among the first to contextualize neu-
commerce’’ were used alongside more specific terms like rosymbolicAI,QML,multimodalAI,anddecentralized
(‘‘recommendation systems’’ OR ‘‘fraud detection’’) AND MLframeworks(e.g.,FL,blockchain-basedAI)within
(‘‘artificial intelligence’’ OR ‘‘machine learning’’). Queries e-commerce environments. Prior surveys have largely
VOLUME13,2025 99049

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
overlookedtheseparadigmsortreatedtheminisolation architectureslikeconvolutionalneuralnetworks(CNNs)and
fromcoreMLapplications. recurrentneuralnetworks(RNNs).Thesetechniquesenhance
• We propose a structured comparison of limitations, model generalization by capturing complex historical trans-
such as data sparsity, latency, adversarial robustness, actionalandbehaviouraldatapatterns[9],[10],[11].
and interpretability, and match them with targeted In fraud detection, supervised models train on labelled
ML strategies (e.g., CL for model drift, graph neural datasets containing historical fraud cases, enabling them to
networks for fraud adaptation, or edge AI for latency differentiatebetweenlegitimateandanomaloustransactions
reduction). This enables solution-oriented guidance, accurately. However, the reliance on annotated data poses
fillingthegapbetweentheoryanddeployment. challenges, particularly when fraud patterns evolve dynam-
• Section VI presents a systematic meta-analysis of ically.Tomitigatethis,semi-supervisedlearningtechniques,
various major prior surveys, highlighting how our whichleveragesmallamountsoflabelleddatacombinedwith
work advances beyond them in scope (encompassing a large volume of unlabeled data, have been integrated into
moreapplicationdomains),depth(offeringalgorithmic modernfrauddetectionframeworks[12],[13].
insights),andforesight(providingaresearchroadmap). Supervised learning also plays a pivotal role in customer
In doing so, we bridge the foundational literature with sentimentanalysis,wherenaturallanguageprocessing(NLP)
disruptiveinnovations,agapabsentinearlierreviews. models classify user reviews and feedback into predefined
• The inclusion of Figure 1 and Tables 1–5 presents an categories. Transformer-based architectures, such as BERT
integratedvisualtaxonomythatconnectslearningtypes, (Bidirectional Encoder Representations from Transformers)
functionaldomains,technicalchallenges,andemerging and RoBERTa (a Robustly Optimized BERT Pretraining
| research | directions—serving |     |     | as a | reference | model for |            |        |           |            |     |     |               |     |
| -------- | ------------------ | --- | --- | ---- | --------- | --------- | ---------- | ------ | --------- | ---------- | --- | --- | ------------- | --- |
|          |                    |     |     |      |           |           | Approach), | refine | sentiment | prediction |     | by  | understanding |     |
both academic researchers and practitioners in digital contextual dependencies, significantly improving the accu-
commerce. racy of automated sentiment classification. In the domain
|               |            |        |                   |               |     |              | of demand | forecasting, |                   | long short-term |             | memory |        | (LSTM) |
| ------------- | ---------- | ------ | ----------------- | ------------- | --- | ------------ | --------- | ------------ | ----------------- | --------------- | ----------- | ------ | ------ | ------ |
| The remainder |            | of the | paper             | is structured |     | as follows.  |           |              |                   |                 |             |        |        |        |
|               |            |        |                   |               |     |              | networks  | and          | Transformer-based |                 | time-series |        | models | have   |
| Section       | II focuses | on     | the methodologies |               |     | and learning |           |              |                   |                 |             |        |        |        |
beenincreasinglyadopted,offeringsuperiorperformancein
paradigmsine-commerce.SectionIIInotesMLapplications
capturingseasonalityandtrendshiftswithinsalesdata[14],
| in e-commerce. |     | Moreover, | Section | IV  | provides | challenges |     |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
[15],[16].
| and limitations. |       | Besides, | Section | V outlines |     | future research |     |     |     |     |     |     |     |     |
| ---------------- | ----- | -------- | ------- | ---------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| directions.      | Next, | Section  | VI      | discusses  | the | findings and    |     |     |     |     |     |     |     |     |
comparesthemwithexistingresearchonMLine-commerce.
B. UNSUPERVISEDLEARNINGFORPATTERN
Finally,SectionVIIsummarizesthefindingsofthissurvey.
RECOGNITIONANDBEHAVIORALCLUSTERING
Unlikesupervisedlearning,whichreliesonlabelleddatasets,
II. METHODOLOGIESANDLEARNINGPARADIGMS unsupervisedlearningdiscoverslatentstructureswithindata
| ML methodologies |     | in e-commerce |     | encompass |     | a diverse set |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------- | --- | --------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
withoutpredefinedcategories.Thisparadigmisparticularly
of paradigms, each designed to address distinct challenges effective in customer segmentation, anomaly detection, and
| across recommendation |         |             | systems, | fraud        | detection, | inventory   |         |                 |          |          |     |            |            |     |
| --------------------- | ------- | ----------- | -------- | ------------ | ---------- | ----------- | ------- | --------------- | -------- | -------- | --- | ---------- | ---------- | --- |
|                       |         |             |          |              |            |             | market  | trend analysis. | This     | includes |     | clustering | algorithms |     |
| forecasting,          | pricing | strategies, |          | and customer |            | engagement. |         |                 |          |          |     |            |            |     |
|                       |         |             |          |              |            |             | such as | k-means,        | Gaussian | mixture  |     | models     | (GMM),     | and |
The evolution of learning paradigms has expanded from hierarchicalclusteringwhicharewidelyemployedtoidentify
| conventional | supervised |     | and unsupervised |     | learning | to more |          |          |        |       |             |     |          |        |
| ------------ | ---------- | --- | ---------------- | --- | -------- | ------- | -------- | -------- | ------ | ----- | ----------- | --- | -------- | ------ |
|              |            |     |                  |     |          |         | distinct | customer | groups | based | on purchase |     | history, | brows- |
sophisticatedRLframeworks,meta-learningtechniques,and
|     |     |     |     |     |     |     | ing behaviour, |     | and demographic |     | attributes. |     | The resulting |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------- | --- | ----------- | --- | ------------- | --- |
hybridmodelsthatintegratemultipleapproachestooptimize
|     |     |     |     |     |     |     | segmentation |     | allows e-commerce |     | businesses |     | to personal- |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------------- | --- | ---------- | --- | ------------ | --- |
performance.Understandingthesemethodologies’computa-
|     |     |     |     |     |     |     | ize marketing |     | campaigns, | optimize | pricing |     | strategies, | and |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---------- | -------- | ------- | --- | ----------- | --- |
tionalfoundationsandpracticalimplicationsprovidesdeeper enhance user engagement by catering to specific consumer
| insights | into their | effectiveness |     | in real-world |     | e-commerce |     |     |     |     |     |     |     |     |
| -------- | ---------- | ------------- | --- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
preferences[17],[18],[19].
applications.
|     |     |     |     |     |     |     | Beyond | clustering, | dimensionality |     |     | reduction | techniques |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | -------------- | --- | --- | --------- | ---------- | --- |
suchasprincipalcomponentanalysis(PCA)andt-distributed
A. SUPERVISEDLEARNINGFORPREDICTIVEAND stochasticneighbourembedding(t-SNE)facilitateextracting
PRESCRIPTIVEANALYTICS meaningful features from high-dimensional data. These
Supervised learning remains one of the most extensively methods are crucial in reducing computational overhead
applied methodologies in e-commerce, offering robust whilepreservingessentialdatacharacteristics,whichisvalu-
predictive capabilities through labelled data-driven model able for recommendation engines that require feature-rich
training.Thisparadigmunderpinsapplicationssuchasfraud userandproductrepresentations[20],[21].
detection, customer retention prediction, and demand fore- In fraud detection, unsupervised anomaly detection mod-
casting.Traditionalapproachesrelyonlogisticregressionand els, including autoencoders and isolation forests, identify
decision trees. Still, recent advances incorporate ensemble deviationsfromnormaltransactionpatterns,detectingprevi-
methods,suchasgradientboostingmachines(GBM)andDL ouslyunseenfraudulentactivities.Thesetechniquesoperate
| 99050 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
FIGURE1. SurveyedtopicsinE-Commerce:LearningParadigms,FunctionalDomains,Challenges,andFutureResearchDirections.
without explicit fraud labels, making them particularly methods, enhances pricing strategies by continuously learn-
advantageous in scenarios where fraudulent behaviours ingfromtransactiondata,optimizingrevenuegeneration,and
continuously evolve. Moreover, generative models such as maintainingcustomersatisfaction[28],[29].
variational autoencoders (VAEs) and generative adversarial Recommendation systems benefit significantly from RL,
networks (GANs) are increasingly utilized to generate syn- where policy-based learning frameworks complement tradi-
thetic user behaviour profiles, augmenting training datasets tionalcollaborativefilteringmodels.Unlikestaticmodelsthat
andimprovingtherobustnessofpredictivemodels[22],[23], generate recommendations based on historical interactions,
[24],[25]. RL-powered systems adapt to real-time user feedback,
|     |     |     |     |     | optimizing | engagement by presenting | contextually | relevant |
| --- | --- | --- | --- | --- | ---------- | ------------------------ | ------------ | -------- |
C. REINFORCEMENTLEARNINGFORADAPTIVE products. Multi-armed bandit algorithms, a subset of RL,
DECISION-MAKING balance exploration and exploitation, dynamically refining
RL has emerged as a powerful paradigm for optimizing recommendationpoliciesbasedonuserresponses[30],[31],
[32].
| dynamic | decision-making | processes | in e-commerce. | Unlike |     |     |     |     |
| ------- | --------------- | --------- | -------------- | ------ | --- | --- | --- | --- |
traditional learning approaches that rely on static datasets, Additionally, RL has been effectively applied to sup-
RL continuously interacts with its environment, refining ply chain and logistics optimization, which aids in route
strategies based on observed rewards. This methodology planning, warehouse management, and delivery scheduling.
has gained prominence in dynamic pricing, personalized RLagentsoptimiseresourceallocationbymodellinglogistics
|                  |     |           |                   |       | operations | as sequential decision-making | problems | while |
| ---------------- | --- | --------- | ----------------- | ----- | ---------- | ----------------------------- | -------- | ----- |
| recommendations, | and | automated | customer support, | where |            |                               |          |       |
real-timeadaptabilityisessential[26],[27]. minimizing operational costs and delivery times. Multi-
Indynamicpricing,RLagentssimulatemarketconditions, agent RL (MARL) extends this paradigm by coordinating
adjustingproductpricesinresponsetodemandfluctuations, interactions among multiple autonomous agents, enhancing
competitorpricing,andmacroeconomicindicators.DeepRL, decision-making efficiency in complex supply chain net-
works[33],[34],[35].
| particularly  | deep Q-networks | (DQNs) | and policy | gradient |     |     |     |       |
| ------------- | --------------- | ------ | ---------- | -------- | --- | --- | --- | ----- |
| VOLUME13,2025 |                 |        |            |          |     |     |     | 99051 |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
D. HYBRIDLEARNINGMODELSFORENHANCED individual user preferences. Instead of retraining models
|     |     |     |     |     |     |     |     | from scratch, | meta-learning |     | frameworks |     | fine-tune | ranking |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------------- | --- | ---------- | --- | --------- | ------- |
GENERALIZATION
Hybrid learning models, which integrate multiple learning algorithms based on limited user interactions, optimizing
paradigms, have gained traction in e-commerce due to their searchrelevanceandusersatisfaction[53],[54].
ability to leverage the strengths of different approaches. TheoveralllandscapeofMLmethodologies,correspond-
These models combine supervised, unsupervised, and RL ing models, and e-commerce applications is illustrated
|     |     |     |     |     |     |     |     | in Figure | 2. Moreover, |     | Table | 1 presents | an  | analytical |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ----- | ---------- | --- | ---------- |
techniquestoenhancegeneralization,robustness,andadapt-
abilityacrossdiverseapplications[36],[37]. and comparative overview of core ML paradigms applied
For instance, hybrid recommendation systems integrate in e-commerce. It systematically contrasts five primary
content-basedfilteringwithcollaborativefilteringandRLto approaches,supervisedlearning,unsupervisedlearning,RL,
address challenges such as data sparsity and evolving user hybridlearningmodels,andmeta-learning/few-shotlearning
acrossthreecriticaldimensions:theirtypicale-commerceuse
| preferences. | By  | combining | explicit |     | and implicit |     | feedback |     |     |     |     |     |     |     |
| ------------ | --- | --------- | -------- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
mechanisms, these models improve recommendation accu- cases,algorithmicstrengths,andcontext-specificlimitations.
racyandpersonalization[38]. By introducing concrete examples (e.g., real-time cold-start
In fraud detection, hybrid approaches merge supervised personalizationorfrauddetectionwithevolvingpatterns),the
classificationwithunsupervisedanomalydetection,ensuring tablesupportsamorenuancedunderstandingofthetrade-offs
associatedwitheachmethodologyinreal-worlddeployment.
comprehensivefraudidentificationeveninpreviouslyunseen
attackscenarios.Byleveragingensemblelearningtechniques
suchasstackingandboosting,hybridfrauddetectionmodels
III. MACHINELEARNINGAPPLICATIONSIN
significantlyenhancepredictiveperformancewhilereducing
E-COMMERCE
falsepositives[39],[40],[41].
|     |     |     |     |     |     |     |     | The proliferation |     | of  | ML in | e-commerce | has | redefined |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ----- | ---------- | --- | --------- |
ConversationalAIsystemsalsobenefitfromhybridlearn- how digital marketplaces operate, enhancing the efficiency
ingframeworks,wheresupervisedfine-tuningoftransformer
|     |     |     |     |     |     |     |     | and intelligence |     | of various | ecosystem |     | components. | ML’s |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ---------- | --------- | --- | ----------- | ---- |
modelsiscombinedwithRLtooptimizechatbotinteractions.
|     |     |     |     |     |     |     |     | integration | enables | a   | deeper understanding |     | of  | consumer |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | -------------------- | --- | --- | -------- |
RLfromhumanfeedback(RLHF)refineschatbotresponses behaviour,fraudmitigation,demandprediction,supplychain
| based on | user engagement |     | metrics, | continuously |     | improving |     |     |     |     |     |     |     |     |
| -------- | --------------- | --- | -------- | ------------ | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
management,andmarketingoptimization.Thediverseappli-
dialoguequalityandcontextualrelevance[42],[43],[44]. cationsofMLwithine-commerceencompassaspectrumof
| Hybrid   | learning | is         | further | applied | in  | demand        | fore- |              |         |      |              |         |      |         |
| -------- | -------- | ---------- | ------- | ------- | --- | ------------- | ----- | ------------ | ------- | ---- | ------------ | ------- | ---- | ------- |
|          |          |            |         |         |     |               |       | interrelated | domains | that | collectively | enhance | user | experi- |
| casting, | where    | supervised | LSTM    | models  |     | are augmented |       |              |         |      |              |         |      |         |
ence,operationaleffectiveness,andbusinessintelligence.
| with RL-based |     | inventory | control | mechanisms. |     | This | fusion |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ------- | ----------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
enablesmoreaccuratedemandpredictionswhiledynamically
A. PERSONALIZEDRECOMMENDATIONANDCONSUMER
| adjusting | inventory | replenishment |     | strategies |     | in response | to  |     |     |     |     |     |     |     |
| --------- | --------- | ------------- | --- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
BEHAVIORMODELING
real-timemarketconditions[45],[46].
|     |     |     |     |     |     |     |     | Modern e-commerce |            | platforms |               | employ   | sophisticated | ML         |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ---------- | --------- | ------------- | -------- | ------------- | ---------- |
|     |     |     |     |     |     |     |     | algorithms        | to predict |           | and influence | consumer |               | purchasing |
E. META-LEARNINGANDFEW-SHOTLEARNINGFOR patterns,creatingpersonalizedshoppingexperiencestailored
ADAPTIVEE-COMMERCESYSTEMS to individual preferences. Traditional approaches relied
Meta-learning,oftencalled‘‘learningtolearn,’’hasemerged on heuristic-based filtering techniques, but advancements
asatransformativeapproachinscenarioswheree-commerce in DL have introduced neural collaborative filtering and
systems must rapidly adapt to new data with minimal RL frameworks that dynamically adapt to users’ evolving
retraining. Unlike conventional ML models that require interests.MLmodelsconstructuserembeddingsthatreflect
extensive labelled datasets, meta-learning frameworks gen- underlyingpurchasingtendenciesbyanalyzingtransactional
eralize across tasks, enabling rapid adaptation to novel histories, search queries, browsing behaviours, and contex-
products, user behaviours, and emerging trends [47], [48], tualcues[55],[56],[57].
| [49]. |     |     |     |     |     |     |     | Context-aware |     | recommendation |     | engines | further | refine |
| ----- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | ------- | ------- | ------ |
Few-shot learning, a subset of meta-learning, is particu- this process by incorporating temporal signals, geograph-
larlyvaluableforcold-startrecommendationproblemswhere ical preferences, and session-based interactions to provide
historicaldataislimited.Byleveragingepisodictrainingand real-time, highly relevant product suggestions. Initially
metric-basedlearning,few-shotmodelslearnrepresentations developed for NLP, transformer-based architectures have
that generalize effectively to unseen items and users. This demonstratedremarkableeffectivenessinsequentialrecom-
capability significantly enhances recommendation systems mendation tasks, capturing long-term dependencies in con-
fornewlylaunchedproducts,ensuringpersonalizedsugges- sumer behaviour. Hybrid models combining content-based
tionsevenindata-scarceenvironments[50],[51],[52]. and collaborative filtering techniques enhance robustness
Moreover,meta-learningiscrucialinpersonalizedsearch againstdatasparsityandcold-startissues,ensuringaccurate
ranking, where search engines must continuously adapt to predictionsevenfornewusersandproducts[58],[59],[60].
| 99052 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
FIGURE2. LandscapeofMachineLearningParadigms,Techniques,andApplicationsinE-Commerce.
B. INTELLIGENTFRAUDDETECTIONANDRISK proactively identifying vulnerabilities that fraudsters may
exploit.IntegratingMLwithblockchain-basedauthentication
MITIGATION
Theexpansionofonlinetransactionshasheightenedconcerns systems further strengthens security protocols, reducing
regarding fraudulent activities, necessitating the deploy- identitytheftandpaymentfraudrisks[64],[65],[66],[67].
mentofML-drivensecuritymechanisms.Unlikerule-based
fraud detection systems that rely on predefined thresholds, C. DYNAMICPRICINGANDREVENUEOPTIMIZATION
MLmodelsemployanomalydetectiontechniquestoidentify
ImplementingMLinpricingstrategiesenablese-commerce
suspiciouspatternswithhighprecision.Supervisedlearning platforms to generate optimal revenue while maximizing
approaches, such as ensemble classifiers, leverage labelled consumersatisfaction.Traditionalstaticpricingmechanisms
fraud datasets to distinguish legitimate transactions from are replaced with dynamic pricing algorithms that adjust
fraudulentones.However,thedynamicnatureofcyberthreats prices based on market demand, competitor pricing, user
| necessitates | adopting unsupervised |     | and semi-supervised |     |            |              |              |             |         |
| ------------ | --------------------- | --- | ------------------- | --- | ---------- | ------------ | ------------ | ----------- | ------- |
|              |                       |     |                     |     | behaviour, | and external | factors such | as economic | indica- |
learning strategies to detect previously unseen fraud pat- tors. RL frameworks, particularly those employing DQNs,
terns[61],[62],[63]. optimize pricing decisions by continuously learning from
Graph-basedMLmodelshaveemergedaspowerfultools real-timesalesdataandmarketfluctuations[68],[69].
for financial fraud detection. They analyze transactional Predictiveanalyticsiscrucialinestimatingpriceelasticity,
| networks | and identify | malicious | entities based | on their |          |               |                        |     |             |
| -------- | ------------ | --------- | -------------- | -------- | -------- | ------------- | ---------------------- | --- | ----------- |
|          |              |           |                |          | allowing | businesses to | implement personalized |     | discounting |
relational structures. These models construct a graph rep- strategiesthatmaximizeconversions.Bayesianoptimization
resentation of financial activities, detecting collusion and techniquesfurtherrefinepricingmodelsbybalancingexplo-
fraudulent behaviour that traditional statistical approaches ration and exploitation, enabling adaptive price adjustments
mightoverlook.Additionally,adversarialMLtechniquesare thatpreventrevenuelossduetosuboptimalpricing.Integrat-
| being explored | to enhance | fraud | detection robustness | by  |               |          |                     |       |            |
| -------------- | ---------- | ----- | -------------------- | --- | ------------- | -------- | ------------------- | ----- | ---------- |
|                |            |       |                      |     | ing sentiment | analysis | into pricing models | helps | businesses |
| VOLUME13,2025  |            |       |                      |     |               |          |                     |       | 99053      |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
TABLE1. Taxonomyofmachinelearningparadigms:applicability,advantages,anddrawbacksinE-Commerce.
gaugeconsumersentimenttowardpricingchanges,ensuring purchasingdecisions,enablinghyper-personalizedmarketing
price adjustments align with customer expectations and campaigns[80],[81],[82].
perceivedproductvalue[70],[71],[72]. Behaviouralanalyticsextendsbeyondstaticsegmentation
byincorporatingreal-timeinteractiondatatotrackevolving
consumerpreferences.RNNsandattentionmechanismscap-
D. DEMANDFORECASTINGANDINVENTORY
turesequentialuserbehaviours,identifyingshiftsinshopping
MANAGEMENT
|          |        |             |     |             |     |              | habits that | signal | churn | risk | or emerging | product |     | interests. |
| -------- | ------ | ----------- | --- | ----------- | --- | ------------ | ----------- | ------ | ----- | ---- | ----------- | ------- | --- | ---------- |
| Accurate | demand | forecasting |     | is integral | to  | supply chain |             |        |       |      |             |         |     |            |
Theseinsightsareinstrumentalincraftingautomatedengage-
| efficiency, | minimizing | stockouts |          | and | overstocking | issues |                  |     |         |              |     |       |            |      |
| ----------- | ---------- | --------- | -------- | --- | ------------ | ------ | ---------------- | --- | ------- | ------------ | --- | ----- | ---------- | ---- |
|             |            |           |          |     |              |        | ment strategies, |     | such as | personalized |     | email | campaigns, | tai- |
| that lead   | to revenue | losses.   | ML-based |     | forecasting  | models |                  |     |         |              |     |       |            |      |
loredpushnotifications,andcontextualadvertising.Theinte-
| surpass | traditional | statistical | approaches |     | by  | incorporating |     |     |     |     |     |     |     |     |
| ------- | ----------- | ----------- | ---------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
grationofsentimentanalysisenhancesbehaviouralanalytics
multidimensionaldatasources,includingsocialmediatrends,
|               |             |             |     |            |           |               | by extracting | emotions |       | from      | customer | reviews, |             | enabling |
| ------------- | ----------- | ----------- | --- | ---------- | --------- | ------------- | ------------- | -------- | ----- | --------- | -------- | -------- | ----------- | -------- |
| macroeconomic |             | indicators, | and | competitor | inventory | levels.       |               |          |       |           |          |          |             |          |
|               |             |             |     |            |           |               | brands to     | refine   | their | messaging | and      | product  | positioning |          |
| Time-series   | forecasting | algorithms, |     | such       | as        | Prophet, LSTM |               |          |       |           |          |          |             |          |
accordingly[83],[84],[85],[86].
networks,andattention-basedtransformers,predictdemand
fluctuationswithhighaccuracy,enablingproactiveinventory
F. CONVERSATIONALAIANDAUTOMATEDCUSTOMER
management[73],[74],[75].
SUPPORT
| The convergence  |            | of ML          | with | Internet       | of         | Things (IoT)  |                     |                |          |             |                    |                 |          |          |
| ---------------- | ---------- | -------------- | ---- | -------------- | ---------- | ------------- | ------------------- | -------------- | -------- | ----------- | ------------------ | --------------- | -------- | -------- |
|                  |            |                |      |                |            |               | Adopting            | conversational |          | AI has      | transformed        |                 | customer | sup-     |
| data has         | further    | revolutionized |      | inventory      |            | optimization. |                     |                |          |             |                    |                 |          |          |
|                  |            |                |      |                |            |               | port in e-commerce, |                |          | providing   | intelligent,       |                 | scalable | solu-    |
| Smart warehouses |            | equipped       | with | sensor-enabled |            | systems       |                     |                |          |             |                    |                 |          |          |
|                  |            |                |      |                |            |               | tions that          | enhance        | user     | experience. |                    | Traditional     |          | chatbots |
| transmit         | real-time  | inventory      | data | to             | ML models, | facilitat-    |                     |                |          |             |                    |                 |          |          |
|                  |            |                |      |                |            |               | have evolved        | into           | advanced |             | virtual assistants |                 | powered  | by       |
| ing autonomous   |            | replenishment  |      | decisions.     |            | RL techniques |                     |                |          |             |                    |                 |          |          |
|                  |            |                |      |                |            |               | transformer-based   |                | models,  | such        | as                 | GPT (generative |          | pre-     |
| optimize         | restocking | strategies     |      | by considering |            | procurement   |                     |                |          |             |                    |                 |          |          |
trainedtransformer)andBERT,whicharecapableofunder-
| lead times,    | supplier | reliability, |                  | and   | demand   | uncertainty. |                 |          |            |            |           |            |              |         |
| -------------- | -------- | ------------ | ---------------- | ----- | -------- | ------------ | --------------- | -------- | ---------- | ---------- | --------- | ---------- | ------------ | ------- |
|                |          |              |                  |       |          |              | standing        | natural  | language   | queries    | with      | contextual |              | depth.  |
| Furthermore,   | FL       | approaches   | are              | being | explored | to enhance   |                 |          |            |            |           |            |              |         |
|                |          |              |                  |       |          |              | These AI-driven |          | assistants | facilitate |           | seamless   | interactions |         |
| cross-platform |          | inventory    | synchronization, |       | enabling | collabo-     |                 |          |            |            |           |            |              |         |
|                |          |              |                  |       |          |              | by resolving    | customer |            | inquiries, | assisting |            | with         | product |
rativeinventorymanagementamongmultipleretailerswhile
|     |     |     |     |     |     |     | recommendations, |     | and | handling | transactional |     | processes |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | -------- | ------------- | --- | --------- | --- |
preservingdataprivacy[76],[77],[78],[79].
autonomously[87],[88],[89].
|     |     |     |     |     |     |     | Multimodal | AI  | systems | integrate | text, | voice, | and | visual |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | --------- | ----- | ------ | --- | ------ |
E. CUSTOMERSEGMENTATIONANDBEHAVIORAL recognition capabilities, enabling a more intuitive customer
ANALYTICS supportexperience.Visualsearchfunctionalities,poweredby
The ability to categorize customers based on their pur- CNNs, allow users to find products by uploading images,
chasing behaviours, preferences, and engagement levels providingcontinuitybetweendigitalandphysicalretailexpe-
is critical for targeted marketing and retention strategies. riences. Sentiment-aware chatbots analyze user emotions in
ML-powered clustering algorithms, including GMM and real-time, adapting their responses to provide empathetic
spectral clustering, identify latent customer segments that and contextually relevant support. The integration of RL in
traditionaldemographic-basedsegmentationapproachesfail chatbot development further enhances conversational flow
to capture. By analysing high-dimensional user interac- by enabling adaptive dialogue management based on user
tion data, ML models uncover hidden patterns that drive interactions[90],[91],[92].
| 99054 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
G. REAL-TIMESEARCHOPTIMIZATIONANDQUERY limitations.Addressingthesechallengesiscrucialtoensuring
|     |     |     |     |     |     |     | robust, efficient, |     | and ethical | implementations |     |     | of ML-driven |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------- | --------------- | --- | --- | ------------ |
UNDERSTANDING
Search engines within e-commerce platforms rely on e-commercesolutions.
| sophisticated | ML  | models | to enhance | search | accuracy | and |     |     |     |     |     |     |     |
| ------------- | --- | ------ | ---------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
relevance.Traditionalkeyword-basedretrievalsystemshave A. DATAPRIVACY,SECURITY,ANDETHICAL
| been replaced | by  | semantic | search | models | that | understand |     |     |     |     |     |     |     |
| ------------- | --- | -------- | ------ | ------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
CONSIDERATIONS
userintentbeyondliteralkeywordmatches.DLarchitectures, One of the most pressing challenges in ML-driven e-
| including            | BERT-based |           | retrieval | models, | enable    | contextual |                   |         |          |           |     |           |            |
| -------------------- | ---------- | --------- | --------- | ------- | --------- | ---------- | ----------------- | ------- | -------- | --------- | --- | --------- | ---------- |
|                      |            |           |           |         |           |            | commerce          | systems | is the   | handling  | of  | sensitive | user data  |
| query understanding, |            | improving |           | search  | precision | even in    |                   |         |          |           |     |           |            |
|                      |            |           |           |         |           |            | while maintaining |         | privacy, | security, | and | ethical   | integrity. |
ambiguousqueries[93],[94]. Asbusinessesrelyonvastamountsofpersonalinformation—
| Personalized | search |     | ranking | algorithms | adapt | search |              |             |     |           |              |     |            |
| ------------ | ------ | --- | ------- | ---------- | ----- | ------ | ------------ | ----------- | --- | --------- | ------------ | --- | ---------- |
|              |        |     |         |            |       |        | ranging from | transaction |     | histories | and browsing |     | behaviours |
results based on individual user preferences, browsing his- to location-based interactions—ensuring compliance with
tory,andinferredintent.Multimodalsearchenginesintegrate regulatory frameworks such as the General Data Protection
textual,visual,andvoice-basedinputstoprovideaseamless
Regulation(GDPR)andtheCaliforniaConsumerPrivacyAct
shopping experience across different interaction modes. (CCPA)isimperative.Violationscanleadtolegalrepercus-
| RL in | search ranking |     | enables | continuous | optimization, |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | ------- | ---------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
sionsandlossofconsumertrust,makingprivacy-preserving
refining result rankings based on user engagement metrics MLtechniques,suchasFLanddifferentialprivacy,essential
suchasclick-throughratesanddwelltime[95],[96],[97]. formitigatingrisks[104],[105],[106].
|     |     |     |     |     |     |     | Furthermore,    |     | the ethical | implications |         |     | of AI-driven |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ------------ | ------- | --- | ------------ |
|     |     |     |     |     |     |     | decision-making |     | introduce   | concerns     | related | to  | algorithmic  |
H. SUPPLYCHAINOPTIMIZATIONANDLOGISTICS
INTELLIGENCE bias, data exploitation, and consumer manipulation. Biased
|               |            |                 |        |     |                  |              | training datasets |     | can lead         | to discriminatory |                | pricing | models, |
| ------------- | ---------- | --------------- | ------ | --- | ---------------- | ------------ | ----------------- | --- | ---------------- | ----------------- | -------------- | ------- | ------- |
| ML is pivotal | in         | streamlining    | supply |     | chain operations | by           |                   |     |                  |                   |                |         |         |
|               |            |                 |        |     |                  |              | unfair targeting, |     | and exclusionary |                   | recommendation |         | systems |
| optimizing    | logistics, | transportation, |        | and | order            | fulfillment. |                   |     |                  |                   |                |         |         |
Predictive analytics models anticipate shipment delays, thatfavourcertainuserdemographicsoverothers.Achieving
|     |     |     |     |     |     |     | transparency | in  | ML models | while | preventing |     | exploitative |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ----- | ---------- | --- | ------------ |
enablingproactivemitigationstrategiesthatenhancedelivery
efficiency. Route optimization algorithms powered by RL tactics such as dark patterns, which nudge users into
|             |        |          |       |       |              |         | unintended | purchases, | is  | an ongoing | challenge |     | in AI ethics |
| ----------- | ------ | -------- | ----- | ----- | ------------ | ------- | ---------- | ---------- | --- | ---------- | --------- | --- | ------------ |
| dynamically | adjust | delivery | paths | based | on real-time | traffic |            |            |     |            |           |     |              |
withine-commerce[107],[108].
conditionsandfuelefficiencymetrics[98],[99],[100].
| Integrating | robotic | process | automation |     | (RPA) | with ML- |     |     |     |     |     |     |     |
| ----------- | ------- | ------- | ---------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
driven decision-making has significantly improved ware- B. MODELINTERPRETABILITYANDTRUSTWORTHINESS
house automation. Autonomous robotic systems, guided by As e-commerce increasingly integrates DL-based systems,
computer vision and Deep RL, optimize warehouse nav- the lack of interpretability in these models raises concerns
igation and order-picking efficiency. Implementing digital about decisiontransparency. Many ML models,particularly
| twins in | logistics | enables | virtual | modelling | of supply | chain |                  |     |      |              |     |                       |     |
| -------- | --------- | ------- | ------- | --------- | --------- | ----- | ---------------- | --- | ---- | ------------ | --- | --------------------- | --- |
|          |           |         |         |           |           |       | neural networks, |     | lack | transparency |     | and interpretability, |     |
processes, allowing ML models to simulate and optimize makingitdifficulttoexplainhowspecificrecommendations,
operational workflows before real-world deployment [101], pricingdecisions,orfrauddetectionalertsaregenerated.This
[102],[103]. opacity poses a barrier to regulatory compliance and user
Table2offersacomprehensiveandcomparativeoverview trust, particularly in domains such as financial transactions
| of how | ML techniques |     | are applied | across | major | functional |     |     |     |     |     |     |     |
| ------ | ------------- | --- | ----------- | ------ | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- |
andpersonalizedadvertising[109],[110].
domains in e-commerce. Beyond listing methodologies and To enhance model interpretability, recent advances in
benefits,thetableanalyticallymapseachapplicationareato Explainable AI (XAI) techniques, including SHAP (Shap-
its core functional scope, the ML techniques employed, the ley Additive Explanations) and LIME (Local Interpretable
observedbusinessbenefits,andexistinggapsorchallenges. Model-agnostic Explanations), attempt to provide post-hoc
This side-by-side structure enables clearer insight into explanations for predictions. However, achieving both high
both the strengths and unresolved limitations of ML-driven accuracyandinterpretabilitysimultaneouslyremainsafunda-
e-commerce systems, guiding research and development mentalchallenge.Businessesmustbalancepredictivepower
directions. with transparency to ensure accountability in automated
decision-making[111],[112],[113],[114].
IV. CHALLENGESANDLIMITATIONS
DespiteML’stransformativeimpactone-commerce,several C. COMPUTATIONALCOMPLEXITYANDSCALABILITY
challenges and limitations hinder its seamless deployment CONSTRAINTS
and optimization. The increasing complexity of digital Theexponentialgrowthofe-commercedatasetsnecessitates
commerce,coupledwithvastandevolvingdatasets,presents highly efficient ML architectures capable of real-time
obstacles ranging from data privacy concerns and inter- processing. Traditional ML models struggle to scale when
pretabilityissuestocomputationalconstraintsandscalability dealing with millions of users, billions of transactions, and
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 99055 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
TABLE2. ApplicationdomainsandmachinelearningtechniquesinE-Commerce:comparativefunctionalmapping.
continuously evolving product catalogues. DL approaches, approachesareincreasinglybeingexploredtoenablemodels
whilepowerful,demandsubstantialcomputationalresources. to adjust dynamically to shifting patterns. However, these
They often require high-performance graphics processing techniques introduce additional computational complexity
units(GPUs),tensorprocessingunits(TPUs),ordistributed andtheriskofcatastrophicforgetting—aphenomenonwhere
cloud infrastructure to manage inference workloads effec- a model abruptly loses performance on previously learned
tively[115],[116],[117]. taskswhileadaptingtonewinformation[123],[124],[125],
| In recommendation |         | systems,    | for example,  | real-time per- | [126]. |     |     |     |     |
| ----------------- | ------- | ----------- | ------------- | -------------- | ------ | --- | --- | --- | --- |
| sonalization      | demands | low-latency | model updates | to reflect     |        |     |     |     |     |
recentuserbehaviour.However,retraininglarge-scalemodels
frequently is computationally prohibitive. Approximation E. FRAUDADAPTATIONANDADVERSARIALATTACKS
Frauddetectionsystemsmustconstantlyevolvetocounteract
| techniques, | such as | knowledge | distillation, | model pruning, |     |     |     |     |     |
| ----------- | ------- | --------- | ------------- | -------------- | --- | --- | --- | --- | --- |
and quantization, are being explored to reduce complexity theincreasinglysophisticatedtacticsemployedbycybercrim-
without significant accuracy loss. In addition, edge AI is inals.Traditionalfrauddetectionmodelsoftenrelyonstatic
emerging as a potential solution by shifting certain compu- heuristics,butasfraudstersdevelopnewattackvectors,such
tations from cloud-based systems to on-device processing, models become ineffective. The adversarial nature of fraud
|          |             |           |            |                 | necessitates | ML systems | that | are continuously | updated to |
| -------- | ----------- | --------- | ---------- | --------------- | ------------ | ---------- | ---- | ---------------- | ---------- |
| reducing | latency and | enhancing | efficiency | in real-time e- |              |            |      |                  |            |
commerceapplications[118],[119],[120]. detectemergingthreats[127],[128].
|     |     |     |     |     | A major   | challenge             | in fraud | detection    | is the adversarial |
| --- | --- | --- | --- | --- | --------- | --------------------- | -------- | ------------ | ------------------ |
|     |     |     |     |     | nature of | the problem—attackers |          | deliberately | exploit weak-      |
D. DATAQUALITY,BIAS,ANDGENERALIZATIONISSUES nesses in ML models, launching adversarial attacks that
MLmodelsareonlyasgoodasthedatatheyaretrainedon, manipulatetransactionaldataordeceivefraudclassification
makingdataqualityafundamentalchallengeine-commerce. algorithms.Techniquessuchasadversarialretraining,robust
Noisy,inconsistent,orbiaseddatasetscanleadtoerroneous feature engineering, and ensemble-based anomaly detection
predictions, negatively affecting recommendation accuracy, are being deployed to counteract these threats. However,
demandforecastingprecision,andfrauddetectionrobustness. fraudstersfrequentlyadapt,requiringconstantinnovationin
Aparticularchallengearisesfromuserbehaviourdrift,where defencestrategies[129],[130],[131].
consumer preferences evolve over time, rendering static Moreover, fraud detection models face the dilemma of
modelsineffective[121],[122]. minimizing false positives, where legitimate transactions
Ensuring that models generalize well across diverse cus- are incorrectly flagged as fraud, while still maintaining a
tomersegmentsandgeographicalregionsisalsoasignificant high true positive rate. Excessive false positives can lead
hurdle.AnMLmodeltrainedondatafromonemarketmay to revenue loss due to rejected transactions, while false
fail to perform optimally in another due to cultural, eco- negatives allow fraudulent activities to persist undetected.
nomic, or seasonal variations. Transfer learning techniques, Finding the optimal trade-off remains an ongoing challenge
domainadaptationstrategies,andcontinuousonlinelearning ine-commercesecurity[132],[133].
| 99056 |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
F. REAL-TIMEPROCESSINGANDLATENCYCONSTRAINTS intelligence. Rapid advancements in generative AI, FL,
neurosymbolicsystems,andquantum-enhancedoptimization
| E-commerce |     | platforms | operate | in  | a high-speed |     | digital |     |     |     |     |     |     |     |     |
| ---------- | --- | --------- | ------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
environment where real-time decision-making is essential. offernoveltoolstoaddresslongstandingchallengesinscala-
From dynamically adjusting product recommendations to bility,personalization,interpretability,andtrust.Thissection
processing fraud detection alerts, ML models must execute outlines key research directions that promise to reshape
complexcomputationsinmillisecondstopreventdelaysthat thetechnicalandoperationalfoundationsofnext-generation
digitalcommerce.
| impact | user experience. |     | Achieving | this | level | of responsive- |     |     |     |     |     |     |     |     |     |
| ------ | ---------------- | --- | --------- | ---- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
nessisparticularlychallengingforDLmodels,whichrequire
multiplelayersofcomputationtogeneratepredictions[134],
|     |     |     |     |     |     |     |     | A. FEDERATEDANDPRIVACY-PRESERVINGLEARNING |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[135],[136].
|     |     |     |     |     |     |     |     | The growing | concerns |     | surrounding | data | privacy, | regulatory |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ----------- | ---- | -------- | ---------- | --- |
DeployingMLsolutionsthatmeetreal-timeperformance
compliance,andethicalAInecessitateresearchintoFLand
requirements involves a combination of low-latency infer- privacy-enhancingMLtechniques.Conventionalcentralized
| ence architectures, |         | optimized   |                | data pipelines, |     | and      | caching |           |              |         |                    |          |         |            |          |
| ------------------- | ------- | ----------- | -------------- | --------------- | --- | -------- | ------- | --------- | ------------ | ------- | ------------------ | -------- | ------- | ---------- | -------- |
|                     |         |             |                |                 |     |          |         | ML models | require      |         | aggregating        | vast     | amounts |            | of user  |
| mechanisms.         |         | Graph-based | recommendation |                 |     | systems, | for     |           |              |         |                    |          |         |            |          |
|                     |         |             |                |                 |     |          |         | data on   | a central    | server, | raising            | concerns |         | about      | security |
| instance,           | require | efficient   | traversal      | operations      |     | to serve | per-    |           |              |         |                    |          |         |            |          |
|                     |         |             |                |                 |     |          |         | breaches, | unauthorized |         | data exploitation, |          | and     | compliance |          |
sonalizedrecommendationsinstantly.Content-basedfiltering
|     |     |     |     |     |     |     |     | with stringent |     | privacy | laws such | as  | the GDPR. | FL, | which |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | --------- | --- | --------- | --- | ----- |
algorithmsmustrapidlyadapttonewlyintroducedproducts, enables decentralized model training across multiple edge
| ensuring   | fresh     | and relevant | suggestions |              | for  | users. However, |        |                  |             |          |        |          |           |             |          |
| ---------- | --------- | ------------ | ----------- | ------------ | ---- | --------------- | ------ | ---------------- | ----------- | -------- | ------ | -------- | --------- | ----------- | -------- |
|            |           |              |             |              |      |                 |        | devices          | without     | exposing | raw    | data,    | presents  | a promising |          |
| balancing  | real-time | processing   |             | speed        | with | predictive      | accu-  |                  |             |          |        |          |           |             |          |
|            |           |              |             |              |      |                 |        | solution.        | By allowing |          | models | to learn | from      | distributed | data     |
| racy is an | ongoing   | challenge,   |             | particularly | when | scaling         | ML     |                  |             |          |        |          |           |             |          |
|            |           |              |             |              |      |                 |        | while preserving |             | privacy, | this   | approach | mitigates |             | security |
| solutions  | to global | e-commerce   |             | ecosystems   |      | [137],          | [138], |                  |             |          |        |          |           |             |          |
risksandfostersusertrust[147],[148].
[139],[140]. However, FL introduces challenges related to communi-
cationoverhead,heterogeneityinuserdatadistributions,and
G. INTEGRATIONCOMPLEXITYANDMAINTENANCE modelaggregationtechniques.Researchisneededtodevelop
CHALLENGES adaptiveFLframeworksthatoptimizemodelsynchronization
Adopting ML in e-commerce requires seamless integration acrossdistributednodes,ensuringefficiencyandrobustness.
|     |     |     |     |     |     |     |     | Additionally, |     | integrating | differential |     | privacy | and | secure |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------------ | --- | ------- | --- | ------ |
intoexistingbusinessworkflows,whichcanbecomplexdue
to compatibility issues between legacy systems and modern multi-party computation into FL architectures will further
AI architectures. Many traditional e-commerce platforms enhance security while maintaining predictive accuracy.
are built on monolithic architectures that do not easily Futureadvancementsinprivacy-preservingMLwilldrivethe
accommodatereal-timeMLmodels,necessitatingexpensive adoptionofuser-centricAI,enablinge-commerceplatforms
toleveragepersonalizedinsightswhileadheringtoethicalAI
infrastructureupgradesorcompletesystemoverhauls[141],
| [142].        |     |           |         |            |     |             |     | standards[149],[150],[151]. |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ------- | ---------- | --- | ----------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Additionally, |     | ML models | require | continuous |     | monitoring, |     |                             |     |     |     |     |     |     |     |
retraining,andfine-tuningtomaintainoptimalperformance.
|              |       |           |     |            |       |              |     | B. NEUROSYMBOLICAIFOREXPLAINABLEAND |     |     |     |     |     |     |     |
| ------------ | ----- | --------- | --- | ---------- | ----- | ------------ | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Model drift, | where | a model’s |     | predictive | power | deteriorates |     |                                     |     |     |     |     |     |     |     |
GENERALIZABLELEARNING
over time due to shifts in user behaviour or market trends, Despite significant progress in DL, many ML models
| necessitates   | proactive |         | retraining   | strategies.    |            | Implementing |         |            |               |           |              |               |          |           |           |
| -------------- | --------- | ------- | ------------ | -------------- | ---------- | ------------ | ------- | ---------- | ------------- | --------- | ------------ | ------------- | -------- | --------- | --------- |
|                |           |         |              |                |            |              |         | deployed   | in e-commerce |           | remain       | opaque,       | making   |           | interpre- |
| automated      | MLOps     | (ML     | Operations)  |                | frameworks | is           | crucial |            |               |           |              |               |          |           |           |
|                |           |         |              |                |            |              |         | tation and | reasoning     |           | difficult.   | Neurosymbolic |          | AI,       | which     |
| for managing   |           | model   | lifecycle    | processes,     |            | including    | data    |            |               |           |              |               |          |           |           |
|                |           |         |              |                |            |              |         | combines   | the           | strengths | of           | deep neural   |          | networks  | with      |
| preprocessing, |           | feature | engineering, | hyperparameter |            |              | tuning, |            |               |           |              |               |          |           |           |
|                |           |         |              |                |            |              |         | symbolic   | reasoning,    | offers    | a compelling |               | research | direction |           |
andversioncontrol.However,implementingMLOpscomes to enhance model transparency and generalization. Unlike
| with significant |     | resource | requirements, |     |     | particularly | for |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | ------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
purelydata-drivenMLsystemsthatrelyonpatternrecogni-
| smaller | e-commerce | businesses |     | that may | lack | dedicated | AI  |     |     |     |     |     |     |     |     |
| ------- | ---------- | ---------- | --- | -------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tion,neurosymbolicarchitecturesintegratelogicalinference
engineeringteams[143],[144],[145],[146].
|     |     |     |     |     |     |     |     | mechanisms, | enabling |     | models | to reason | about | cause-and- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ------ | --------- | ----- | ---------- | --- |
Table3providesastructuredanalysisofthekeyobstacles
|           |     |           |            |     |     |                |     | effect relationships |     |     | within consumer |     | interactions |     | [152], |
| --------- | --- | --------- | ---------- | --- | --- | -------------- | --- | -------------------- | --- | --- | --------------- | --- | ------------ | --- | ------ |
| hindering | the | effective | deployment | of  | ML  | in e-commerce. |     | [153],[154].         |     |     |                 |     |              |     |        |
Itcategorizesmajorchallenges,highlightstheirdirectimpact
Forinstance,indynamicpricingoptimization,aneurosym-
| on e-commerce |     | systems, | notes | limitations, |     | and | outlines |          |        |       |             |          |     |          |     |
| ------------- | --- | -------- | ----- | ------------ | --- | --- | -------- | -------- | ------ | ----- | ----------- | -------- | --- | -------- | --- |
|               |     |          |       |              |     |     |          | bolic AI | system | could | incorporate | economic |     | theories | and |
potentialsolutionsthatcanmitigatetheseissues.
|     |     |     |     |     |     |     |     | behavioural | patterns    |     | alongside         | statistical | learning, |              | leading |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | ----------------- | ----------- | --------- | ------------ | ------- |
|     |     |     |     |     |     |     |     | to more     | explainable |     | and context-aware |             | price     | adjustments. |         |
Similarly,infrauddetection,integratingsymbolicruleswith
V. FUTURERESEARCHDIRECTIONS
As ML continues to transform e-commerce, emerging tech- anomaly detection models can improve fraud identification
nologiesareopeningnewfrontiersthatextendbeyondpredic- by ensuring that predictions align with established risk
tiveanalyticstowardgenerative,adaptive,anddecentralized factors rather than relying solely on statistical correlations.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 99057 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
TABLE3. ComparisonofchallengesandlimitationsinmachinelearningforE-Commerce.
ResearchintoneurosymbolicAIwilldrivethedevelopment product catalogues. For inventory and logistics optimiza-
ofinterpretable,reasoning-drivenMLmodelsthatbridgethe tion, quantum-enhanced RL could significantly improve
gap between empirical learning and structured knowledge supply chain management, reducing inefficiencies in rout-
representation[155],[156],[157]. ing, demand forecasting, and warehouse allocation. How-
ever, the practical implementation of QML remains in
its infancy, necessitating extensive research into hybrid
C. QUANTUMMACHINELEARNINGFORLARGE-SCALE quantum-classicalalgorithmsthatbridgequantumcomputing
OPTIMIZATION withexistingMLinfrastructures.Developingquantum-ready
As e-commerce datasets continue to grow in size and ML architectures that integrate with current e-commerce
complexity, traditional ML algorithms face computational platformswillbeakeyresearchpriorityasquantumhardware
bottlenecks in handling large-scale optimization problems. matures[160],[161],[162],[163].
Quantumcomputing,whichleveragestheprinciplesofsuper-
positionandentanglementtoperformparallelcomputations, D. MULTIMODALAIFORENHANCEDUSERINTERACTION
presents a transformative opportunity for ML-driven e- The modern e-commerce experience is no longer limited
commerceapplications.QMLhasthepotentialtoaccelerate to text-based interactions but incorporates images, voice
model training, enhance combinatorial optimization tasks, commands,andreal-timeengagementacrossmultiplemodal-
and solve high-dimensional problems with unprecedented ities.Traditionalrecommendationsystemsrelyprimarilyon
efficiency[158],[159]. transactional and behavioural data, but the integration of
In the context of recommendation systems, QML could multimodalAI,whichfusestextual,visual,andauditorydata,
revolutionize personalized search and ranking algorithms offersanewfrontierforpersonalizeduserexperiences[164],
by performing faster similarity computations across vast [165].
99058 VOLUME13,2025

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
Futureresearchwillfocusondevelopingtransformer-based promptingresearchintodecentralizedMLframeworkspow-
multimodalarchitecturescapableofprocessingandaligning ered by blockchain technology. Blockchain-based AI has
diverse data sources. For instance, a shopper browsing an the potential to enhance security in fraud detection, ensure
online store could receive AI-driven recommendations not transparent AI decision-making, and establish decentralized
only based on previous purchases but also on visual prefer- marketplaces where consumers retain control over their
ences,voicequeries,andfacialexpressions.Theconvergence data[180],[181].
of NLP, computer vision, and affective computing will Future research in this area will explore the integration
enabledeeperuserengagement,allowingMLmodelstoinfer of smart contracts with ML-based fraud detection, where
user intent more holistically. Moreover, real-time emotion- AI-driven risk assessments are recorded on an immutable
aware AI will enable adaptive personalization, where AI ledger,preventingtamperingandensuringauditability.Addi-
systemsdynamicallyadjustrecommendationsbasedonuser tionally,decentralizedautonomousrecommendationsystems
sentimentandmicro-expressionsduringaninteraction[166], (DARS) could allow users to personalize their shopping
[167],[168]. experiences without relying on centralized platforms that
Advancements in multimodal fusion techniques will be monetizeuserdata[182],[183],[184].
critical in enabling AI systems to interpret and synthe- Addressingthecomputationalinefficienciesofblockchain-
size complex user interactions seamlessly. Future research basedAIremainsacriticalresearchchallenge.Keyareasof
must address challenges such as cross-modal alignment, exploration will include optimizing consensus mechanisms,
efficient representation learning, and real-time inference reducing the energy consumption of decentralized AI
latency to unlock the full potential of multimodal AI in networks, and developing scalable federated blockchain
e-commerce[169],[170]. architectures.Ase-commerceplatformsseektoenhanceuser
|     |     |     |     |     |     |     |     | trust and | reduce | reliance | on intermediaries, |         |          | decentralized |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | -------- | ------------------ | ------- | -------- | ------------- | --- |
|     |     |     |     |     |     |     |     | AI will   | play a | pivotal  | role in            | shaping | the next | generation    |     |
E. SELF-SUPERVISEDANDCONTINUALLEARNINGFOR
ofsecureanduser-centricdigitalmarketplaces[185],[186],
ADAPTIVEAI
[187].
Thefast-evolvingnatureofconsumerbehaviourandproduct
| trends presents |     | a fundamental |     | challenge | for | traditional | ML  |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
models,whichrequireperiodicretrainingonnewlylabelled
|           |     |                  |     |           |     |     |         | G. GENERATIVEAIFORINTELLIGENTE-COMMERCE |     |     |     |     |     |     |     |
| --------- | --- | ---------------- | --- | --------- | --- | --- | ------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| datasets. | SSL | (self-supervised |     | learning) | and | CL  | present |                                         |     |     |     |     |     |     |     |
RecentadvancesingenerativeAIandlargefoundationmod-
promisingresearchdirectionstoenableAIsystemsthatlearn
|              |      |          |      |         |         |     |           | els, such | as GPT, | Claude, | and | PaLM | (Pathways | Language |     |
| ------------ | ---- | -------- | ---- | ------- | ------- | --- | --------- | --------- | ------- | ------- | --- | ---- | --------- | -------- | --- |
| continuously | from | evolving | data | streams | without |     | requiring |           |         |         |     |      |           |          |     |
Model),arepoisedtoredefinetheoperationalandexperien-
extensivemanualannotations[171],[172].
tiallandscapeofe-commerce.Thesemodelsexhibitpowerful
| SSL enables |     | models | to extract | meaningful |     | representa- |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------ | ---------- | ---------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
capabilitiesinnaturallanguagegeneration,imagesynthesis,
| tions from | unlabeled | data, | reducing |     | dependency |     | on large |     |     |     |     |     |     |     |     |
| ---------- | --------- | ----- | -------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
multimodalunderstanding,andcontextualdialogue,enabling
| annotated | datasets | while | improving |     | generalization |     | across |       |          |             |           |              |     |         |     |
| --------- | -------- | ----- | --------- | --- | -------------- | --- | ------ | ----- | -------- | ----------- | --------- | ------------ | --- | ------- | --- |
|           |          |       |           |     |                |     |        | a new | class of | intelligent | services. | Applications |     | include |     |
domains.Forinstance,SSL-basedrecommendationsystems
dynamicproductdescriptiongeneration,AI-generatedvisual
| can autonomously |     | learn | user | preferences |     | by identifying |     |          |              |     |           |             |     |               |     |
| ---------------- | --- | ----- | ---- | ----------- | --- | -------------- | --- | -------- | ------------ | --- | --------- | ----------- | --- | ------------- | --- |
|                  |     |       |      |             |     |                |     | content, | personalized |     | marketing | narratives, |     | and conversa- |     |
patternsinimplicitinteractions,suchasscrollingbehaviour,
|                   |     |            |           |     |      |            |     | tional agents | that     | adapt     | to individual |              | customer |           | intents |
| ----------------- | --- | ---------- | --------- | --- | ---- | ---------- | --- | ------------- | -------- | --------- | ------------- | ------------ | -------- | --------- | ------- |
| session duration, |     | and cursor | movement. |     | This | eliminates | the |               |          |           |               |              |          |           |         |
|                   |     |            |           |     |      |            |     | with high     | semantic | fidelity. | These         | capabilities |          | introduce | a       |
needforextensivelabelledfeedbackwhileenablingreal-time
paradigmshiftfromstaticpersonalizationtowardgenerative
personalization[173],[174],[175].
personalizationatscale[188],[189].
| Conversely, | continuous |                   | learning | equips  | AI        | systems | with  |         |                 |           |            |                    |      |            |     |
| ----------- | ---------- | ----------------- | -------- | ------- | --------- | ------- | ----- | ------- | --------------- | --------- | ---------- | ------------------ | ---- | ---------- | --- |
|             |            |                   |          |         |           |         |       | Despite | these           | promising | use        | cases, integrating |      | generative |     |
| the ability | to         | retain previously |          | learned | knowledge |         | while |         |                 |           |            |                    |      |            |     |
|             |            |                   |          |         |           |         |       | models  | into e-commerce |           | ecosystems | raises             | open | challenges |     |
incorporatingnewinformation.UnliketraditionalMLmod-
|                 |           |              |         |             |     |               |          | in controllability, |                 | latency,  | fine-tuning  | efficiency, |          | and       | align- |
| --------------- | --------- | ------------ | ------- | ----------- | --- | ------------- | -------- | ------------------- | --------------- | --------- | ------------ | ----------- | -------- | --------- | ------ |
| els that suffer | from      | catastrophic |         | forgetting, |     | CL frameworks |          |                     |                 |           |              |             |          |           |        |
|                 |           |              |         |             |     |               |          | ment with           | brand           | and legal | constraints. |             | Research | is needed |        |
| ensure that     | AI-driven | e-commerce   |         | platforms   |     | adapt         | to new   |                     |                 |           |              |             |          |           |        |
|                 |           |              |         |             |     |               |          | to develop          | domain-specific |           | foundation   |             | models   | that      | are    |
| market trends,  |           | emerging     | product | categories, |     | and           | evolving |                     |                 |           |              |             |          |           |        |
optimizedforproductcatalogs,customerreviews,behavioral
fraudtacticswithoutlosingpriorknowledge.Researchefforts
|     |     |     |     |     |     |     |     | signals, | and regulatory |     | frameworks. | Equally |     | important | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ----------- | ------- | --- | --------- | --- |
inmemory-augmentedneuralnetworksanddynamicweight
|            |      |            |     |            |     |         |      | the investigation |     | of techniques |     | for hallucination |     | mitigation, |     |
| ---------- | ---- | ---------- | --- | ---------- | --- | ------- | ---- | ----------------- | --- | ------------- | --- | ----------------- | --- | ----------- | --- |
| adaptation | will | be crucial | in  | developing | AI  | systems | that |                   |     |               |     |                   |     |             |     |
brand-safegeneration,andlow-resourcedeployment,partic-
| learn persistently, |     | maintaining |     | relevance | over | time | without |     |     |     |     |     |     |     |     |
| ------------------- | --- | ----------- | --- | --------- | ---- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ularlyformobileandedge-basedcommercescenarioswhere
requiringcompleteretraining[176],[177],[178],[179].
inferencelatencyiscritical.Thetrade-offbetweengeneration
quality,real-timeperformance,andinterpretabilitymustalso
F. DECENTRALIZEDANDBLOCKCHAIN-BASEDAIFOR be addressed through novel architecture and compression
| TRUSTANDSECURITY |     |     |     |     |     |     |     | strategies[190],[191]. |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
TherelianceoncentralizedAIsystemsine-commerceraises Future directions include generative agents that support
concernsabouttrust,transparency,anddatamonopolization, multi-turn interactions, negotiation, and adaptive product
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 99059 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
TABLE4. FutureresearchdirectionsinmachinelearningforE-Commerce.
discovery by combining generative transformers with RL architecturalgeneralizability.Also,[201]alignsMLmodels
and structured knowledge bases. Additionally, generative with business goals but lacks deployment-oriented anal-
models can be leveraged to synthesize rare user behaviors ysis. Reference [199] emphasizes analytics pipelines but
and simulate fraud patterns, contributing to more robust downplays interpretability and robustness. Moreover, [202]
training pipelines. As generative AI continues to evolve, its examines security and privacy trends, yet their analysis is
convergence with CL, neurosymbolic systems, and decen- notcommerce-specific.Finally,[203]discussese-commerce
tralized inference will likely result in deeply personalized, evolution but does not engage with model-level ML trade-
| trustworthy,andcontext-awaree-commerceplatforms[192], |     |     |     |     |     |     |     | offs. |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
[193],[194]. Thepresentsurveyaddressesthoselimitationsbylinking
Table4providesaresearch-focusedoverviewofemerging learning paradigms to both commercial functionality and
MLadvancementsthatwillshapethefutureofdigitalcom- system-level constraints, such as latency, explainability,
merce.Itcategorizesvariouskeyresearchareas,identifiesthe and regulatory compliance. It also incorporates underrepre-
primarychallengesassociatedwitheach,proposespotential sentedmethods,suchasneurosymbolicinferenceandQRL,
solutions, and outlines the expected impact on e-commerce which are largely absent from commerce-focused reviews.
applications. Rather than emphasizing algorithmic classification alone,
|     |     |     |     |     |     |     |     | the analysis | considers | practical |     | trade-offs | in  | real-world | ML  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --------- | --- | ---------- | --- | ---------- | --- |
deployment.
VI. DISCUSSION
|             |         |     |            |     |        |            |     | In addition |     | to paradigm-based |     | categorization, |     | lifecycle- |     |
| ----------- | ------- | --- | ---------- | --- | ------ | ---------- | --- | ----------- | --- | ----------------- | --- | --------------- | --- | ---------- | --- |
| This survey | reveals | a   | transition | in  | how ML | is adopted | in  |             |     |                   |     |                 |     |            |     |
awaremodelingprovidesavaluableperspective.Asreviewed
| e-commerce, | moving          |      | from isolated |               | use cases | to integrated |     |           |           |           |             |           |            |               |        |
| ----------- | --------------- | ---- | ------------- | ------------- | --------- | ------------- | --- | --------- | --------- | --------- | ----------- | --------- | ---------- | ------------- | ------ |
|             |                 |      |               |               |           |               |     | in [204], | aligning  | ML        | systems     | to        | specific   | stages        | in the |
| systems     | that prioritize |      | adaptability, | real-time     |           | inference,    | and |           |           |           |             |           |            |               |        |
|             |                 |      |               |               |           |               |     | customer  | journey   | (e.g.,    | onboarding, |           | retention, | reactivation) |        |
| privacy.    | Advances        | such | as FL,        | neurosymbolic |           | models,       | CL, |           |           |           |             |           |            |               |        |
|             |                 |      |               |               |           |               |     | enhances  | targeting | precision |             | and model | relevance. |               | Future |
andtransformer-basedgenerativearchitecturesarereshaping
|              |                  |          |       |               |     |     |           | surveys  | might   | benefit  | from | hybrid    | frameworks  | that | map      |
| ------------ | ---------------- | -------- | ----- | ------------- | --- | --- | --------- | -------- | ------- | -------- | ---- | --------- | ----------- | ---- | -------- |
| tasks like   | personalization, |          | fraud | detection,    |     | and | customer  |          |         |          |      |           |             |      |          |
|              |                  |          |       |               |     |     |           | learning | methods | not only | to   | technical | constraints |      | but also |
| segmentation | by               | enabling | more  | context-aware |     | and | resilient |          |         |          |      |           |             |      |          |
touserbehaviorstates.
decision-making.
|                  |                     |              |          |               |        |           |          | Emerging       | ML           | techniques   |                 | are not       | without | operational    |         |
| ---------------- | ------------------- | ------------ | -------- | ------------- | ------ | --------- | -------- | -------------- | ------------ | ------------ | --------------- | ------------- | ------- | -------------- | ------- |
| Table            | 5 synthesizes       |              | prior    | surveys.      | The    | authors   | in [195] |                |              |              |                 |               |         |                |         |
|                  |                     |              |          |               |        |           |          | challenges.    | FL           | introduces   | synchronization |               |         | overhead       | and     |
| and [198]        | review              | core         | ML       | and DL        | models | for       | standard |                |              |              |                 |               |         |                |         |
|                  |                     |              |          |               |        |           |          | hardware       | distribution | constraints. |                 | QML           | remains |                | experi- |
| applications,    | yet                 | they         | overlook | architectural |        | issues    | such as  |                |              |              |                 |               |         |                |         |
|                  |                     |              |          |               |        |           |          | mental,        | with         | issues in    | reproducibility |               | and     | accessibility. |         |
| privacy          | and sustainability. |              | Besides, |               | [196]  | focuses   | narrowly |                |              |              |                 |               |         |                |         |
|                  |                     |              |          |               |        |           |          | As highlighted |              | by [205],    | the             | environmental |         | impact         | of      |
| on blockchain-ML |                     | integration, |          | while         | [197]  | and [200] | con-     |                |              |              |                 |               |         |                |         |
large-scaletrainingandfrequentmodelupdates—especially
| tribute insights |     | into churn | and | retention |     | but offer | limited |     |     |     |     |     |     |               |     |
| ---------------- | --- | ---------- | --- | --------- | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | ------------- | --- |
| 99060            |     |            |     |           |     |           |         |     |     |     |     |     |     | VOLUME13,2025 |     |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
TABLE5. Summaryandthematicscopeofreviewedsurveyarticles.
inFLsettings—raisesimportantsustainabilityconcernsthat mustbeengineeredintotheMLlifecycle,fromdeployment
areunderexploredincurrentliterature. training,ratherthanappendedafterthefact.
This survey offers guidance for model selection under Whilethistaxonomyintroducesastructuredandfunctional
deploymentconstraintsforpractitioners.Forexample,FLcan lens for mapping ML technologies in e-commerce, it is not
enable privacy-preserving personalization in compliance- exhaustive.Asthefieldevolves,futureworkshouldincorpo-
heavy domains, while lightweight transformers may sup- rateethical,social,andenvironmentalperspectivesalongside
port mobile-first fraud detection. Trade-offs between inter- computational considerations. Flexible, multi-stakeholder
pretability, accuracy, and latency should inform system taxonomies will be essential for guiding responsible AI
designinlivecommerceenvironments. developmentincommercialecosystems.
Theoretically, the paper highlights directions for deeper In summary, this discussion offers a comparative lens
exploration, including hybrid symbolic–subsymbolic archi- on existing literature, distills actionable insights for both
tectures for personalization, and CL systems that adapt to implementationandresearch,andhighlightshowthissurvey
changing consumer behavior without repeated retraining. complements prior work with a constraint-aware, multi-
It also points to the need for cross-disciplinary integration paradigm taxonomy. Future extensions should aim to inte-
across AI, behavioral science, and digital policy to shape grateenvironmentalmetrics,stakeholderroles,andadaptive
responsiblee-commerceinnovation. learningstagesintocommerce-specificAIsystems.
| Future       | commerce platforms | will likely intersect     | with |     |     |     |
| ------------ | ------------------ | ------------------------- | ---- | --- | --- | --- |
| technologies | such as immersive  | interfaces, decentralized |      |     |     |     |
VII. CONCLUSION
| identity, | and real-time generative | content. These | shifts                |            |             |             |
| --------- | ------------------------ | -------------- | --------------------- | ---------- | ----------- | ----------- |
|           |                          |                | ML has revolutionized | e-commerce | by enabling | intelligent |
demandMLsystemsthatarenotonlyadaptivebutalsosecure
decision-making,enhancinguserexperience,andoptimizing
andexplainablebydesign.Aspaper[202]emphasizes,trust
|               |     |     | business operations. | This survey | has provided | a structured |
| ------------- | --- | --- | -------------------- | ----------- | ------------ | ------------ |
| VOLUME13,2025 |     |     |                      |             |              | 99061        |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
| exploration | of ML | applications       |     | in e-commerce, |             | methodolo- |     | REFERENCES |     |     |     |     |     |     |
| ----------- | ----- | ------------------ | --- | -------------- | ----------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| gies that   | drive | these innovations, |     | inherent       | challenges, |            | and |            |     |     |     |     |     |     |
[1] M.Iqbal,‘‘Machinelearningapplicationsine-commerce,’’Org.,Bus.
future research directions that promise to redefine digital Manage.,vol.65,pp.1–15,Jan.2022.
commerce. The increasing complexity of online markets [2] I.Oktaviani,E.Purawanto,andT.Triana,‘‘AnalysisofAI-basedbigdata
forstrategicdecision-makingine-commerce,’’inProc.Int.Conf.Sci.
necessitates the integration of adaptive, scalable, and XAI HealthTechnol.,Sep.2024,vol.5,no.1,p.4192.
modelsthatcatertodynamicconsumerbehaviours,security [3] R.ElYoubi,F.Messaoudi,andM.Loukili,‘‘Machinelearning-driven
threats,andcomputationalconstraints. dynamicpricingstrategiesine-commerce,’’inProc.14thInt.Conf.Inf.
Commun.Syst.(ICICS),Nov.2023,pp.1–5.
Whilesupervisedandunsupervisedlearningremainfunda-
[4] R.Khurana,‘‘FrauddetectionineCommercepaymentsystems:Therole
mentaltopredictiveanalyticsandpatterndiscovery,RLhas
ofpredictiveAIinreal-timetransactionsecurityandriskmanagement,’’
|         |               |     |      |                |     |         |         | Int. J. | Appl. Mach. | Learn. | Comput. | Intell., | vol. 10, | no. 6, pp.1–32, |
| ------- | ------------- | --- | ---- | -------------- | --- | ------- | ------- | ------- | ----------- | ------ | ------- | -------- | -------- | --------------- |
| emerged | as a powerful |     | tool | for optimizing |     | pricing | strate- |         |             |        |         |          |          |                 |
Jun.2020.
| gies, recommendation |     |     | systems, | and logistics |     | management. |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | -------- | ------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
[5] J.Hu,R.Hu,Z.Wang,D.Li,J.Wu,L.Ren,Y.Zang,Z.Huang,and
| Hybrid | and neurosymbolic |     | AI  | models | are bridging |     | the gap |          |                 |     |       |            |                   |         |
| ------ | ----------------- | --- | --- | ------ | ------------ | --- | ------- | -------- | --------------- | --- | ----- | ---------- | ----------------- | ------- |
|        |                   |     |     |        |              |     |         | M. Wang, | ‘‘Collaborative |     | fraud | detection: | How collaboration | impacts |
between interpretability and predictive accuracy, addressing frauddetection,’’inProc.31stACMInt.Conf.Multimedia,Oct.2023,
long-standing concerns regarding algorithmic transparency. pp.8891–8899.
[6] T.Karunaratne,‘‘Machinelearningandbigdataapproachestoenhancing
Additionally, advancements in FL and privacy-preserving e-commerceanomalydetectionandproactivedefensestrategiesincyber-
AI techniques are mitigating risks associated with data security,’’ J. Adv. Cybersecurity Sci., Threat Intell., Countermeasures,
securityandcompliance,allowinge-commerceplatformsto vol.7,no.12,pp.1–16,2023.
[7] V.M.ReddyandL.N.Nalla,‘‘Real-timedataprocessingine-commerce:
leveragevastconsumerdatasetswhileadheringtoregulatory
Challengesandsolutions,’’Int.J.Adv.Eng.Technol.Innov.,vol.1,no.3,
| frameworks. |     |     |     |     |     |     |     | pp.297–325,2024. |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
Despitetheseadvancements,significantobstaclespersist, [8] R. Raman, R. Kowalski, K. Achuthan, A. Iyer, and P. Nedungadi,
‘‘Navigatingartificialgeneralintelligencedevelopment:Societal,tech-
rangingfromreal-timeinferencelatencyandmodelscalabil-
nological,ethical,andbrain-inspiredpathways,’’Sci.Rep.,vol.15,no.1,
itytoethicalconsiderationssurroundingAI-drivendecision-
pp.1–22,Mar.2025.
making. Fraud detection systems must continuously evolve [9] R.Jhangiani,D.Bein,andA.Verma,‘‘Machinelearningpipelinefor
to counteract adversarial attacks, while recommendation fraud detection and prevention in e-commerce transactions,’’ in Proc.
IEEE10thAnnu.UbiquitousComput.,Electron.MobileCommun.Conf.
| engines | require | continuous | learning |     | mechanisms |     | to adapt |     |     |     |     |     |     |     |
| ------- | ------- | ---------- | -------- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
(UEMCON),Oct.2019,pp.0135–0140.
to shifting consumer preferences. Integrating SSL and CL [10] A. Panarese, G. Settanni, V. Vitti, and A. Galiano, ‘‘Developing and
is a promising avenue for enhancing model robustness preliminary testing of a machine learning-based platform for sales
|         |           |             |     |          |       |            |     | forecasting | using | a gradient | boosting | approach,’’ |     | Appl. Sci., vol. 12, |
| ------- | --------- | ----------- | --- | -------- | ----- | ---------- | --- | ----------- | ----- | ---------- | -------- | ----------- | --- | -------------------- |
| without | excessive | retraining. |     | However, | these | techniques |     |             |       |            |          |             |     |                      |
no.21,p.11054,Oct.2022.
introducechallengesrelatedtocomputationalefficiencyand
|     |     |     |     |     |     |     |     | [11] S. Wang, | C. Liu, | X. Gao, | H. Qu, | and W. | Xu, ‘‘Session-based | fraud |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ------- | ------- | ------ | ------ | ------------------- | ----- |
long-termknowledgeretention,necessitatingfurtherresearch detection in online e-commerce transactions using recurrent neural
|                   |     |            |     |              |              |     |      | networks,’’ | in  | Proc. Joint | Eur. | Conf. Mach. | Learn. | Knowl. Discovery |
| ----------------- | --- | ---------- | --- | ------------ | ------------ | --- | ---- | ----------- | --- | ----------- | ---- | ----------- | ------ | ---------------- |
| into optimization |     | strategies |     | that balance | adaptability |     | with |             |     |             |      |             |        |                  |
Databases,Skopje,Macedonia.Cham,Switzerland:Springer,Jan.2017,
operationalfeasibility.
pp.241–252.
Looking ahead, the convergence of QML, blockchain- [12] D.Wang,J.Lin,P.Cui,Q.Jia,Z.Wang,Y.Fang,Q.Yu,J.Zhou,S.Yang,
andY.Qi,‘‘Asemi-supervisedgraphattentivenetworkforfinancialfraud
| based AI, | and | multimodal |     | intelligence | will | reshape | the |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | ------------ | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
detection,’’inProc.IEEEInt.Conf.DataMining(ICDM),Nov.2019,
| landscape | of e-commerce. |     | Quantum-enhanced |     |     | models | hold |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ---------------- | --- | --- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- |
pp.598–607.
thepotentialtoacceleratecomplexoptimizationsinpersonal- [13] T.Hu,Q.Guo,X.Shen,H.Sun,R.Wu,andH.Xi,‘‘Utilizingunlabeled
izationandlogistics,whiledecentralizedAIframeworkswill datatodetectelectricityfraudinAMI:Asemisuperviseddeeplearning
|     |     |     |     |     |     |     |     | approach,’’ | IEEE | Trans. | Neural | Netw. Learn. | Syst., | vol. 30, no. 11, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | ------ | ------------ | ------ | ---------------- |
redefine data ownership, transparency, and fraud mitigation pp.3287–3299,Nov.2019.
strategies. Multimodal AI, integrating textual, visual, and [14] K.N.Prasanthi,R.E.Madhavi,D.N.S.Sabarinadh,andB.Sravani,
auditory data, will drive the next wave of immersive and ‘‘AnovelapproachforsentimentanalysisonsocialmediausingBERT
&ROBERTAtransformer-basedmodels,’’inProc.IEEE8thInt.Conf.
| hyper-personalized |     | shopping |     | experiences. | These |     | emerging |     |     |     |     |     |     |     |
| ------------------ | --- | -------- | --- | ------------ | ----- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Converg.Technol.(I2CT),Apr.2023,pp.1–6.
| technologies | will       | enhance | predictive   |     | accuracy   | and | improve |                 |     |            |           |              |     |                  |
| ------------ | ---------- | ------- | ------------ | --- | ---------- | --- | ------- | --------------- | --- | ---------- | --------- | ------------ | --- | ---------------- |
|              |            |         |              |     |            |     |         | [15] A. Sharma, | N.  | Patel, and | R. Gupta, | ‘‘Leveraging |     | LSTM and prophet |
| the overall  | efficiency |         | and security | of  | e-commerce |     | ecosys- |                 |     |            |           |              |     |                  |
modelsforenhancedAI-drivendemandpredictionine-commerce,’’Eur.
Adv.Artif.Intell.J.,vol.3,no.2,pp.45–58,Dec.2021.
tems.
[16] H.XuandY.Lv,‘‘Miningandapplicationoftourismonlinereviewtext
| To fully | harness | the | potential | of  | ML in | e-commerce, |     |     |     |     |     |     |     |     |
| -------- | ------- | --- | --------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
basedonnaturallanguageprocessingandtextclassificationtechnology,’’
interdisciplinary collaboration between AI researchers, WirelessCommun.MobileComput.,vol.2022,pp.1–13,May2022.
behavioural economists, cybersecurity experts, and industry [17] B.Shen,‘‘E-commercecustomersegmentationviaunsupervisedmachine
practitioners is imperative. The adoption of ML should learning,’’inProc.2ndInt.Conf.Comput.DataSci.,Jan.2021,pp.1–7.
|     |     |     |     |     |     |     |     | [18] S. Chandra, | S.  | Verma, | W. M. | Lim, S. | Kumar, | and N. Donthu, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------ | ----- | ------- | ------ | -------------- |
be guided by ethical principles that prioritize fairness, ‘‘Personalizationinpersonalizedmarketing:Trendsandwaysforward,’’
inclusivity, and user-centric design. Future innovations Psychol.Marketing,vol.39,no.8,pp.1529–1562,Aug.2022.
[19] N.D.Sugiharto,D.Elbert,J.Arnold,I.S.Edbert,andD.Suhartono,
| must address | existing |                   | limitations | while | fostering |      | scalable, |        |          |            |       |          |         |                 |
| ------------ | -------- | ----------------- | ----------- | ----- | --------- | ---- | --------- | ------ | -------- | ---------- | ----- | -------- | ------- | --------------- |
|              |          |                   |             |       |           |      |           | ‘‘Mall | customer | clustering | using | Gaussian | mixture | model, K-means, |
| explainable, | and      | privacy-conscious |             | AI    | models    | that | align     |        |          |            |       |          |         |                 |
andBIRCHalgorithm,’’inProc.6thInt.Conf.Inf.Commun.Technol.
| with the | evolving | needs | of digital | commerce. |     | By advancing |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | ---------- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
(ICOIACT),Nov.2023,pp.212–217.
researchinthesecriticalareas,MLwillcontinuetodrivethe [20] F. Anowar, S. Sadaoui, and B. Selim, ‘‘Conceptual and empirical
comparisonofdimensionalityreductionalgorithms(PCA,KPCA,LDA,
| transformation |     | of e-commerce, |     | shaping | a more | intelligent, |     |      |           |         |     |                |     |                    |
| -------------- | --- | -------------- | --- | ------- | ------ | ------------ | --- | ---- | --------- | ------- | --- | -------------- | --- | ------------------ |
|                |     |                |     |         |        |              |     | MDS, | SVD, LLE, | ISOMAP, | LE, | ICA, t-SNE),’’ |     | Comput. Sci. Rev., |
secure,anduser-drivenmarketplaceintheyearstocome. vol.40,May2021,Art.no.100378.
| 99062 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
[21] Y.Hu,‘‘Researchone-commerceshortvideorecommendationsystem [43] K. R. Praneeth, T. S. Ruprah, J. N. Madhuri, A. L. Sreenivasulu,
based on user behavior data mining and feature extraction,’’ in Proc. S.Shareefunnisa, and V. S. Rao, ‘‘Optimizing customer interactions:
Int. Conf. Comput., Inf. Process. Adv. Educ. (CIPAE), Aug. 2024, A BERT and reinforcement learning hybrid approach to chatbot
pp.119–126. development,’’ Int. J. Adv. Comput. Sci. Appl., vol. 15, no. 9,
[22] Ö. Özkum, ‘‘Credit card fraud detection with autoencoders, one-class pp.569–578,2024.
svmsandisolationforests,’’M.S.thesis,GraduateSchoolNaturalAppl. [44] M. Ahmed, H. U. Khan, and E. U. Munir, ‘‘Conversational AI:
Sci.,MiddleEastTech.Univ.,Ankara,Türkiye,2023. An explication of few-shot learning problem in transformers-based
[23] Y. Ding, W. Kang, J. Feng, B. Peng, and A. Yang, ‘‘Credit card chatbotsystems,’’IEEETrans.Computat.SocialSyst.,vol.11,no.2,
fraud detection based on improved variational autoencoder generative pp.1888–1906,Apr.2024.
adversarialnetwork,’’IEEEAccess,vol.11,pp.83680–83691,2023. [45] R. V. Joseph, A. Mohanty, S. Tyagi, S. Mishra, S. K. Satapathy, and
[24] J.Shan,SyntheticDataGenerationforFraudDetection.LosAngeles, S. N. Mohanty, ‘‘A hybrid deep learning framework with CNN and
CA,USA:UniversityofCalifornia,2023. bi-directionalLSTMforstoreitemdemandforecasting,’’Comput.Electr.
[25] A.Iqbal,E.Ahmed,A.Rahman,andM.R.H.Ontor,‘‘Enhancingfraud
Eng.,vol.103,Oct.2022,Art.no.108358.
[46] A.K.Kalusivalingam,A.Sharma,N.Patel,andV.Singh,‘‘Optimizing
detection and anomaly detection in retail banking using generative ai
inventorymanagementwithAI:Leveragingdeepreinforcementlearning
andmachinelearningmodels,’’Amer.J.Eng.Technol.,vol.6,no.11,
and neural networks for enhanced demand forecasting and stock
pp.78–91,Nov.2024.
replenishment,’’Int.J.Artif.Intell.Mach.Learn.,vol.1,no.1,p.43,
[26] N.Chopra,A.Patel,N.Singh,andV.Sharma,‘‘Leveragingreinforcement
Dec.2024.
learningandneuralnetworksforoptimizeddynamicpricingstrategiesin
[47] B. Wu, Z. Meng, Q. Zhang, and S. Liang, ‘‘Meta-learning helps
e-commerce,’’Int.J.AIAdvancement,vol.9,no.4,pp.45–58,Dec.2020.
personalized product search,’’ in Proc. ACM Web Conf., Apr. 2022,
[27] H.Meisheri,V.Baniwal,N.N.Sultana,B.Ravindran,andH.Khadilkar,
pp.2277–2287.
‘‘Reinforcement learning for multi-objective optimization of online
[48] Y. Wang, Q. Yao, J. T. Kwok, and L. M. Ni, ‘‘Generalizing from a
decisionsinhigh-dimensionalsystems,’’2019,arXiv:1910.00211.
fewexamples:Asurveyonfew-shotlearning,’’ACMComput.Surveys,
[28] J. Liu, Y. Zhang, X. Wang, Y. Deng, and X. Wu, ‘‘Dynamic pricing
vol.53,no.3,pp.1–34,May2021.
on e-commerce platform with deep reinforcement learning: A field [49] A.AgnihotriandI.I.Raj,‘‘Advanceddeepreinforcementlearningframe-
experiment,’’2019,arXiv:1912.02572. workfordynamicpricingoptimizationine-commercemarketplaces,’’
[29] P.FamilAlamdarandA.Seifi,‘‘AdeepQ-learningapproachtooptimize inProc.15thInt.Conf.Comput.Commun.Netw.Technol.(ICCCNT),
ordering and dynamic pricing decisions in the presence of strategic Jun.2024,pp.1–6.
customers,’’Int.J.Prod.Econ.,vol.269,Mar.2024,Art.no.109154. [50] M. Li, S. Hu, F. Zhu, and Q. Zhu, ‘‘Few-shot learning for cold-start
[30] X.Tang,Y.Chen,X.Li,J.Liu,andZ.Ying,‘‘Areinforcementlearning recommendation,’’inProc.JointInt.Conf.Comput.Linguistics,Lang.
approach to personalized learning recommendation systems,’’ Brit. Resour.Eval.(LREC-COLING),May2024,pp.7185–7195.
J.Math.Stat.Psychol.,vol.72,no.1,pp.108–135,Feb.2019. [51] M. Kim, H. Song, Y. Shin, D. Park, K. Shin, and J.-G. Lee, ‘‘Meta-
[31] N.Silva,H.Werneck,T.Silva,A.C.M.Pereira,andL.Rocha,‘‘Multi- learningforonlineupdateofrecommendersystems,’’inProc.AAAIConf.
armed bandits in recommendation systems: A survey of the state-of- Artif.Intell.,Jun.2022,vol.36,no.4,pp.4065–4074.
the-art and future directions,’’ Expert Syst. Appl., vol. 197, Jul. 2022, [52] D. Wang, M. Zhang, Y. Xu, W. Lu, J. Yang, and T. Zhang, ‘‘Metric-
Art.no.116669. basedmeta-learningmodelforfew-shotfaultdiagnosisundermultiple
[32] M. Fu, L. Huang, A. Rao, A. A. Irissappane, J. Zhang, and H. Qu, limiteddataconditions,’’Mech.Syst.SignalProcess.,vol.155,Jun.2021,
‘‘A deep reinforcement learning recommender system with multiple Art.no.107510.
policiesforrecommendations,’’IEEETrans.Ind.Informat.,vol.19,no.2, [53] R.Yu,Y.Gong,X.He,Y.Zhu,Q.Liu,W.Ou,andB.An,‘‘Personalized
pp.2049–2061,Feb.2023. adaptivemetalearningforcold-startuserpreferenceprediction,’’inProc.
[33] L.Kemmer,H.vonKleist,D.deRochebouët,N.Tziortziotis,andJ.Read, AAAIConf.Artif.Intell.,May2021,vol.35,no.12,pp.10772–10780.
‘‘Reinforcementlearningforsupplychainoptimization,’’inProc.Eur. [54] Q.Wang,X.Liu,W.Liu,A.-A.Liu,W.Liu,andT.Mei,‘‘MetaSearch:
WorkshopReinforcementLearn.,vol.14,Oct.2018,pp.1–15. Incrementalproductsearchviadeepmeta-learning,’’IEEETrans.Image
[34] X.Liu,M.Hu,Y.Peng,andY.Yang,‘‘Multi-agentdeepreinforcement Process.,vol.29,pp.7549–7564,2020.
learningformulti-echeloninventorymanagement,’’Prod.Oper.Manage., [55] F. Messaoudi and M. Loukili, ‘‘E-commerce personalized recommen-
vol.33,no.12,Dec.2022,Art.no.10591478241305863. dations:Adeepneuralcollaborativefilteringapproach,’’inOperations
[35] Y. Yan, A. H. F. Chow, C. P. Ho, Y.-H. Kuo, Q. Wu, and C. Ying, ResearchForum,vol.5.Cham,Switzerland:Springer,2024,p.5.
‘‘Reinforcement learning for logistics and supply chain management: [56] Q.Sun,Y.Xue,andZ.Song,‘‘Adaptiveuserinterfacegenerationthrough
Methodologies,stateoftheart,andfutureopportunities,’’Transp.Res. reinforcementlearning:Adata-drivenapproachtopersonalizationand
E,LogisticsTransp.Rev.,vol.162,Jun.2022,Art.no.102712. optimization,’’2024,arXiv:2412.16837.
[57] T.Hagendorff,‘‘Linkinghumanandmachinebehavior:Anewapproach
[36] R.VenkatesanandA.Sabari,‘‘Deepsentimodels:Anovelhybriddeep
toevaluatetrainingdataqualityforbeneficialmachinelearning,’’Minds
learning model for an effective analysis of ensembled sentiments in
Mach.,vol.31,no.4,pp.563–593,Dec.2021.
e-commerceands-commerceplatforms,’’Cybern.Syst.,vol.54,no.4,
[58] S. Raza and C. Ding, ‘‘Progress in context-aware recommender
pp.526–549,May2023.
systems—An overview,’’ Comput. Sci. Rev., vol. 31, pp.84–97,
[37] D. D. Dasig, D. J. R. Calantoc, R. V. F. Guarin, M. A. B. Taduyo,
Feb.2019.
C. N. Ferrer, E. E. Claricia, and G. E. Agus, ‘‘Predicting customer
[59] V.G.Morales-Murillo,D.Pinto,F.Perez-Tellez,andF.Rojas-Lopez,
purchasedecisionsusingdataminingtechnique,’’inProc.IEEE14th
‘‘A transformer-based multi-domain recommender system for e-
Int. Conf. Humanoid, Nanotechnol., Inf. Technol., Commun. Control,
commerce,’’Int.J.Combinat.Optim.ProblemsInformat.,vol.15,no.2,
Environ.,Manage.(HNICEM),Dec.2022,pp.1–6.
pp.95–123,Jun.2024.
[38] Y. Afoudi, M. Lazaar, and M. A. Achhab, ‘‘Hybrid recommendation
[60] H. Li and D. Han, ‘‘A time-aware hybrid recommendation scheme
system combined content-based filtering and collaborative prediction
combiningcontent-basedandcollaborativefiltering,’’FrontiersComput.
usingartificialneuralnetwork,’’Simul.Model.Pract.Theory,vol.113,
Sci.,vol.15,no.4,Aug.2021,Art.no.154613.
Dec.2021,Art.no.102375.
[61] J. Gupta, ‘‘Credit card fraud detection using machine learning algo-
[39] E.F.Malik,K.W.Khaw,B.Belaton,W.P.Wong,andX.Chew,‘‘Credit rithms,’’Int.J.Sci.Res.,vol.12,no.11,pp.1774–1779,Nov.2023.
cardfrauddetectionusinganewhybridmachinelearningarchitecture,’’ [62] T.DeLise,‘‘Deepsemi-supervisedanomalydetectionforfindingfraudin
Mathematics,vol.10,no.9,p.1480,Apr.2022. thefuturesmarket,’’2023,arXiv:2309.00088.
[40] T.ZhouandH.Jiao,‘‘Explorationofthestackingensemblemachine [63] S. Carta, G. Fenu, D. Reforgiato Recupero, and R. Saia, ‘‘Fraud
learning algorithm for cheating detection in large-scale assessment,’’ detection for e-commerce transactions by employing a prudential
Educ.Psychol.Meas.,vol.83,no.4,pp.831–854,Aug.2023. multiple consensus model,’’ J. Inf. Secur. Appl., vol. 46, pp.13–22,
[41] X.Niu,L.Wang,andX.Yang,‘‘Acomparisonstudyofcreditcardfraud Jun.2019.
detection:Supervisedversusunsupervised,’’2019,arXiv:1904.10604. [64] A.Kotiyal,L.Hussein,A.Deepak,A.Rana,Manjunatha,K.K.Dixit,
[42] N.Esfandiari,K.Kiani,andR.Rastgoo,‘‘Transformer-basedgenerative andR.A.Reddy,‘‘Graph-basedmachinelearningapproachesforfraud
chatbotusingreinforcementlearning,’’J.AIDataMining,vol.12,no.3, detection in financial networks,’’ in Proc. 7th Int. Conf. Contemp.
pp.349–358,Jul.2024. Comput.Informat.(IC3I),Sep.2024,pp.1714–1720.
VOLUME13,2025 99063

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
[65] U. Fiore, A. De Santis, F. Perla, P. Zanetti, and F. Palmieri, ‘‘Using [87] K.Prasad,L.A.Xavier,S.Jain,R.Subba,S.Mittal,andN.Anute,‘‘AI-
generativeadversarialnetworksforimprovingclassificationeffectiveness drivenchatbotsfore-commercecustomersupport,’’inProc.Int.Conf.
increditcardfrauddetection,’’Inf.Sci.,vol.479,pp.448–455,Apr.2019. Adv.Comput.,Commun.Appl.Informat.(ACCAI),May2024,pp.1–5.
[66] M. Das, H. Luo, and J. C. Cheng, ‘‘Securing interim payments in [88] J. J. Bird and A. Lotfi, ‘‘Customer service chatbot enhancement
constructionprojectsthroughablockchain-basedframework,’’Autom. with attention-based transfer learning,’’ Knowl.-Based Syst., vol. 301,
Construct.,vol.118,Oct.2020,Art.no.103284. Oct.2024,Art.no.112293.
[67] M.Thilagavathi,R.Saranyadevi,N.Vijayakumar,K.Selvi,L.Anitha, [89] A.T.ImamandI.Altawaiha,‘‘Theuseofthepre-trainedBERTandGPT-
andK.Sudharson,‘‘AI-drivenfrauddetectioninfinancialtransactions 3modelstoautomatethecomposingofusecasedescriptions,’’Authorea
withgraphneuralnetworksandanomalydetection,’’inProc.Int.Conf. Preprints,Aug.2023.
Sci.Technol.Eng.Manage.(ICSTEM),Apr.2024,pp.1–6. [90] X. Zhang and C. Guo, ‘‘Research on multimodal prediction of
[68] C.YinandJ.Han,‘‘Dynamicpricingmodelofe-commerceplatforms e-commercecustomersatisfactiondrivenbybigdata,’’Appl.Sci.,vol.14,
based on deep reinforcement learning,’’ Comput. Model. Eng. Sci., no.18,p.8181,Sep.2024.
vol.127,no.1,pp.291–307,2021. [91] R. B. Yousif, M. G. Abd Alkreem, and A. B. Yousif, ‘‘Personalized
[69] X.Zhu,L.Jian,C.Xin,andQ.Zhao,‘‘DeepQ-learningformulti-flight chatbot responses using reinforcement learning and user modeling,’’
dynamicpricing:Maximizingrevenuewithanovelutilityfunctionin J.Educ.PureSci.,vol.14,no.4,p.462,Dec.2024.
airlinerevenuemanagement,’’Comput.Ind.Eng.,vol.193,Jun.2024, [92] M.G.Sivasathiya,‘‘Emotion-awaremultimediasynthesis:Agenerative
Art.no.110302. AI framework for personalized content generation based on user
[70] P.Das,T.Pervin,B.Bhattacharjee,M.R.Karim,N.Sultana,M.S.Khan, sentiment analysis,’’ in Proc. 2nd Int. Conf. Intell. Data Commun.
M. A. Hosien, and F. Kamruzzaman, ‘‘Optimizing real-time dynamic Technol.InternetThings(IDCIoT),Jan.2024,pp.1344–1350.
pricing strategies in retail and e-commerce using machine learning [93] S.Dhar,‘‘BERTbasedsequentialminingforrichercontextualsemantics
models,’’Amer.J.Eng.Technol.,vol.6,no.12,pp.163–177,Dec.2024. e-commercerecommendation(BERT-SEMSRec),’’M.S.thesis,School
[71] A.K.Kalusivalingam,A.Sharma,N.Patel,andV.Singh,‘‘Leveraging Comput.Sci.,Univ.Windsor,Windsor,ON,Canada,2024.
reinforcementlearningandBayesianoptimizationforenhanceddynamic [94] M.Wen,D.K.Vasthimal,A.Lu,T.Wang,andA.Guo,‘‘Buildinglarge-
pricingstrategies,’’Int.J.AIML,vol.1,no.3,pp.1–14,Apr.2020. scaledeeplearningsystemforentityrecognitionine-commercesearch,’’
[72] M. A. A. Montaser, B. P. Ghosh, A. Barua, F. Karim, B. C. Das, inProc.6thIEEE/ACMInt.Conf.BigDataComput.,Appl.Technol.,
R.E.R.Shawon,andM.S.R.Chowdhury,‘‘Sentimentanalysisofsocial Dec.2019,pp.149–154.
mediadata:BusinessinsightsandconsumerbehaviortrendsintheUSA,’’ [95] D.JannachandM.Ludewig,‘‘Investigatingpersonalizedsearchine-
EdelweissAppl.Sci.Technol.,vol.9,no.1,pp.515–535,Jan.2025. commerce,’’inProc.30thInt.FlairsConf.,Jan.2017,pp.645–650.
[73] J.Feizabadi,‘‘Machinelearningdemandforecastingandsupplychain [96] Z. Tang, X. Zhang, Z. Long, and X. Fu, ‘‘Multimodal neural
performance,’’Int.J.LogisticsRes.Appl.,vol.25,no.2,pp.119–142, machine translation with search engine based image retrieval,’’ 2022,
Feb.2022. arXiv:2208.00767.
[74] C. Junior, P. Gusmão, J. Moreira, and A. M. M. Tome, ‘‘Time series [97] Y.Hu,Q.Da,A.Zeng,Y.Yu,andY.Xu,‘‘Reinforcementlearningtorank
forecastinginretailsalesusingLSTMandprophet,’’inHandbookof ine-commercesearchengine:Formalization,analysis,andapplication,’’
ResearchonAppliedDataScienceandArtificialIntelligenceinBus.and inProc.24thACMSIGKDDInt.Conf.Knowl.DiscoveryDataMining,
Industry.Hershey,PA,USA:IGIGlobal,2021,pp.241–262. Jul.2018,pp.368–377.
[75] J.M.OliveiraandP.Ramos,‘‘Evaluatingtheeffectivenessoftimeseries [98] C. Han and Q. Zhang, ‘‘Optimization of supply chain efficiency
transformers for demand forecasting in retail,’’ Mathematics, vol. 12, management based on machine learning and neural network,’’ Neural
no.17,p.2728,Aug.2024. Comput.Appl.,vol.33,no.5,pp.1419–1433,Mar.2021.
[76] A.Anoop,M.Thomas,andK.Sachin,‘‘IoTbasedsmartwarehousing [99] Y.Geng,E.Liu,R.Wang,Y.Liu,W.Rao,S.Feng,Z.Dong,Z.Fu,and
usingmachinelearning,’’inProc.AsianConf.Innov.Technol.(ASIAN- Y.Chen,‘‘Deepreinforcementlearningbaseddynamicrouteplanningfor
CON),Aug.2021,pp.1–6. minimizingtraveltime,’’inProc.IEEEInt.Conf.Commun.Workshops
[77] V.Pasupuleti,B.Thuraka,C.S.Kodete,andS.Malisetty,‘‘Enhancing (ICCWorkshops),Jun.2021,pp.1–6.
supplychainagilityandsustainabilitythroughmachinelearning:Opti- [100] R. S. Khan, M. R. M. Sirazy, R. Das, and S. Rahman, ‘‘An AI and
mizationtechniquesforlogisticsandinventorymanagement,’’Logistics, ML-enabled framework for proactive risk mitigation and resilience
vol.8,no.3,p.73,Jul.2024. optimizationinglobalsupplychainsduringnationalemergencies,’’Sage
[78] G.Zheng,D.Ivanov,andA.Brintrup,‘‘Anadaptivefederatedlearning Sci.Rev.Appl.Mach.Learn.,vol.5,no.2,pp.127–144,Nov.2022.
system for information sharing in supply chains,’’ Int. J. Prod. Res., [101] J.Mendling,G.Decker,R.Hull,H.A.Reijers,andI.Weber,‘‘Howdo
vol.63,pp.1–23,Jan.2025. machinelearning,roboticprocessautomation,andblockchainsaffectthe
[79] N.Singh,‘‘AIandIoT:Afutureperspectiveoninventorymanagement,’’ humanfactorinbusinessprocessmanagement?’’Commun.Assoc.Inf.
Int. J. Res. Appl. Sci. Eng. Technol., vol. 11, no. 11, pp.2753–2757, Syst.,vol.43,no.1,p.19,2018.
Nov.2023. [102] A. Z. Abideen, V. P. K. Sundram, J. Pyeman, A. K. Othman, and
[80] A. Garcia, ‘‘Machine learning for customer segmentation and tar- S.Sorooshian, ‘‘Digital twin integrated reinforced learning in supply
geted marketing,’’ in Proc. Mach. Learn. Appl. Conf., vol. 3, 2023, chainandlogistics,’’Logistics,vol.5,no.4,p.84,Nov.2021.
pp.1–15. [103] T.M.Ho,K.-K.Nguyen,andM.Cheriet,‘‘Federateddeepreinforcement
[81] K. Wang, T. Zhang, T. Xue, Y. Lu, and S.-G. Na, ‘‘E-commerce learning for task scheduling in heterogeneous autonomous robotic
personalized recommendation analysis by deeply-learned system,’’ IEEE Trans. Autom. Sci. Eng., vol. 21, no. 1, pp.528–540,
clustering,’’ J. Vis. Commun. Image Represent., vol. 71, Aug. 2020, Jan.2024.
Art.no.102735. [104] J.Arora,G.Kaur,M.Sethi,andS.Singh,‘‘AIandmachinelearning
[82] R.S.SucharithaandS.Lee,‘‘GMMclusteringforin-depthfoodaccessi- applications for preserving privacy and data leakage of e-commerce
bilitypatternexplorationandpredictionmodeloffooddemandbehavior,’’ data,’’inAdvancesinElectronicCommerce,2024,pp.59–78.
Socio-EconomicPlanningSci.,vol.83,Oct.2022,Art.no.101351. [105] A.E.OuadrhiriandA.Abdelhadi,‘‘Differentialprivacyfordeepandfed-
[83] M.AlojailandS.Bhatia,‘‘Anoveltechniqueforbehavioralanalytics eratedlearning:Asurvey,’’IEEEAccess,vol.10,pp.22359–22380,2022.
usingensemblelearningalgorithmsine-commerce,’’IEEEAccess,vol.8, [106] S.PatelandA.Rahman,‘‘Dataprivacyinthedigitalage:Navigating
pp.150072–150080,2020. complianceandethicalchallenges,’’BalticMultidisciplinaryRes.Lett.
[84] T.LangandM.Rettenmeier,‘‘Understandingconsumerbehaviorwith J.,vol.1,no.3,pp.13–24,Nov.2024.
recurrentneuralnetworks,’’inProc.WorkshopMach.Learn.Methods [107] S. Narula, A. Afaq, S. Nagar, and M. Chaudhary, ‘‘Transformative
RecommenderSyst.,2017,pp.1–12. potentialandethicalchallengesofgenerativeAIine-commerce:Data
[85] M.Kasimu,N.Hellen,andG.Marvin,‘‘Explainablesentimentanalysis bias, algorithm bias,’’ in Advances in Computational Intelligence and
fortextilepersonalizedmarketing,’’inTheFourthIndustrialRevolution Robotics,2024,pp.317–336.
andBeyond:SelectProceedingsofIC4IR+.Cham,Switzerland:Springer, [108] M. A. Shah and P. Kumar, ‘‘Leveraging machine learning techniques
2023,pp.473–488. to project customer behaviour through predictive analysis and ethical
[86] M.Singh,X.Hoque,D.Zeng,Y.Wang,K.Ikeda,andA.Dhall,‘‘Do marketing,’’inMarketGrooming,2024,pp.121–138.
Ihaveyourattention:Alargescaleengagementpredictiondatasetand [109] P.Urbanke,A.Uhlig,andJ.J.Kranz,‘‘Acustomizedandinterpretable
baselines,’’ in Proc. Int. Conf. MULTIMODAL Interact., Oct. 2023, deepneuralnetworkforhigh-dimensionalbusinessdata-evidencefrom
pp.174–182. ane-commerceapplication,’’inProc.ICIS,2017,pp.1–10.
99064 VOLUME13,2025

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
[110] S. N. Cohen, D. Snow, and L. Szpruch, ‘‘Black-box model risk in [132] U.PorwalandS.Mukund,‘‘Creditcardfrauddetectionine-commerce,’’
finance,’’inMachineLearningandDataSciencesforFinancialMarkets: in Proc. 18th IEEE Int. Conf. Trust, Secur. Privacy Comput. Com-
A Guide to Contemporary Practices. Cambridge Univ. Press, 2023, mun./13thIEEEInt.Conf.BigDataSci.Eng.(TrustCom/BigDataSE),
pp.687–717. Aug.2019,pp.280–287.
[111] P.Linardatos,V.Papastefanopoulos,andS.Kotsiantis,‘‘ExplainableAI: [133] E.M.Al-Dahasi,R.K.Alsheikh,F.A.Khan,andG.Jeon,‘‘Optimizing
Areviewofmachinelearninginterpretabilitymethods,’’Entropy,vol.23, fraud detection in financial transactions with machine learning and
no.1,p.18,Dec.2020. imbalancemitigation,’’ExpertSyst.,vol.42,no.2,p.13682,Feb.2025.
[112] J.Narkhede,‘‘Comparativeevaluationofpost-hocexplainabilitymethods [134] K. H. Leung, D. Y. Mo, G. T. S. Ho, C. H. Wu, and G. Q. Huang,
inAI:LIME,SHAP,andgrad-CAM,’’inProc.4thInt.Conf.Sustain. ‘‘Modellingnear-real-timeorderarrivaldemandine-commercecontext:
ExpertSyst.(ICSES),Oct.2024,pp.826–830. Amachinelearningpredictivemethodology,’’Ind.Manage.DataSyst.,
[113] M. Sarkar, ‘‘Explainable AI in e-commerce: Enhancing trust and vol.120,no.6,pp.1149–1174,May2020.
transparencyinAI-drivendecisions,’’InnovatechEng.J.,vol.2,no.1, [135] Z. Liao, R. Zhang, S. He, D. Zeng, J. Wang, and H.-J. Kim, ‘‘Deep
pp.12–39,Jan.2024. learning-based data storage for low latency in data center networks,’’
[114] M. Battaglini and S. Rasmussen, ‘‘Transparency, automated IEEEAccess,vol.7,pp.26411–26417,2019.
decision-makingprocessesandpersonalprofiling,’’J.DataProtection [136] Y. Vasa, S. R. Mallreddy, and S. Jaini, ‘‘AI and deep learning
Privacy,vol.2,no.4,pp.331–349,2019. synergy:Enhancingreal-timeobservabilityandfrauddetectionincloud
[115] D. Shankar, S. Narumanchi, H. A. Ananya, P. Kompalli, and environment,’’ Int. J. Res. Eng. Manage., vol. 6, no. 4, pp.32–35,
K.Chaudhury,‘‘Deeplearningbasedlargescalevisualrecommendation Aug.2023.
andsearchfore-commerce,’’2017,arXiv:1703.02344. [137] Y. Yang, L. Zhao, Y. Li, H. Zhang, J. Li, M. Zhao, X. Chen, and
[116] W. Li, M. Mikailov, and W. Chen, ‘‘Scaling the inference of digital K. Li, ‘‘INFless: A native serverless system for low-latency, high-
pathology deep learning models using CPU-based high-performance throughput inference,’’ in Proc. 27th ACM Int. Conf. Architectural
computing,’’ IEEE Trans. Artif. Intell., vol. 4, no. 6, pp.1691–1704, SupportProgram.Lang.OperatingSyst.,Feb.2022,pp.768–781.
Dec.2023. [138] Z.BasystiukandZ.Rybchak,‘‘Recommendationsystemsine-commerce
[117] A.Rangra,V.K.Sehgal,andS.Shukla,‘‘Anovelapproachofcloudbased applications,’’Inf.Syst.Netw.,vol.15,pp.252–259,Jul.2024.
schedulingusingdeep-learningapproachine-commercedomain,’’Int. [139] A.TewariandA.Barman,‘‘Collaborativerecommendationsystemusing
J.Inf.Syst.Model.Design,vol.10,no.3,pp.59–75,Jul.2019. dynamic content based filtering, association rule mining and opinion
[118] X. Du, B. Bhushanam, J. Yu, D. Choudhary, T. Gao, S. Wong, mining,’’Int.J.Intell.Eng.Syst.,vol.10,no.5,pp.57–66,Oct.2017.
L. Feng, J. Park, Y. Cao,and A. Kejariwal, ‘‘Alternate model growth [140] G.Dobriţa,‘‘Adaptivemicroservicesfordynamice-commerce:Enabling
and pruning for efficient training of recommendation systems,’’ in personalized experiences through machine learning and real-time
Proc. 20th IEEE Int. Conf. Mach. Learn. Appl. (ICMLA), Dec. 2021, adaptation,’’ Econ. Insights-Trends Challenges, vol. 2023, no. 1,
pp.1421–1428. pp.95–103,2023.
[119] M. F. Álvarez, ‘‘Edge computing security approaches and their [141] K.Xu,H.Zhou,H.Zheng,M.Zhu,andQ.Xin,‘‘Intelligentclassification
influence on latency reduction in e-commerce payment networks,’’ and personalized recommendation of e-commerce products based on
J.Artif.Intell.Mach.Learn.CloudComput.Syst.,vol.5,no.11,pp.1–8, machinelearning,’’2024,arXiv:2403.19345.
Nov.2021. [142] A.H.Adepoju,A.Eweje,andA.Collins,‘‘Frameworkformigrating
[120] S.Kang,‘‘Knowledgedistillationapproachesforaccurateandefficient legacysystemstonext-generationdataarchitectureswhileensuringseam-
recommendersystem,’’2024,arXiv:2407.13952. less integration and scalability,’’ Int. J. Multidisciplinary Res. Growth
[121] Y.Liu,J.Lu,F.Mao,andK.Tong,‘‘Theproductqualityriskassessment Eval.,vol.5,no.6,pp.1462–1474,Jan.2024.
of e-commerce by machine learning algorithm on spark in big data [143] B. Celik and J. Vanschoren, ‘‘Adaptation strategies for automated
environment,’’ J. Intell. Fuzzy Syst., vol. 37, no. 4, pp.4705–4715, machine learning on evolving data,’’ IEEE Trans. Pattern
Oct.2019. Anal.Mach.Intell.,vol.43,no.9,pp.3067–3078,Sep.2021.
[122] L.Caroprese,F.S.Pisani,B.M.Veloso,M.Konig,G.Manco,H.Hoos, [144] E. Raj, Engineering MLOps: Rapidly Build, Test, and Manage
and J. Gama, ‘‘Modelling concept drift in dynamic data streams for Production-ReadyMachineLearningLifeCyclesatScale.Birmingham,
recommendersystems,’’ACMTrans.RecommenderSyst.,vol.3,no.2, U.K.:PacktPublishing,2021.
pp.1–28,Jun.2025. [145] N. Kodakandla, ‘‘Decoding MLOps: Bridging the gap between data
[123] J. Yu, M. Qiu, J. Jiang, J. Huang, S. Song, W. Chu, and H. Chen, scienceandoperationsforscalableAIsystems,’’Int.J.Sci.Res.Arch.,
‘‘Modellingdomainrelationshipsfortransferlearningonretrieval-based vol.11,no.1,pp.2615–2624,Jan.2024.
question answering systems in e-commerce,’’ in Proc. 11th ACM [146] X.-Y.Liu,Z.Xia,H.Yang,J.Gao,D.Zha,M.Zhu,C.D.Wang,Z.Wang,
Int.Conf.WebSearchDataMining,Feb.2018,pp.682–690. andJ.Guo,‘‘Dynamicdatasetsandmarketenvironmentsforfinancial
[124] A.Zhao,‘‘Deepreinforcementlearning-basedtradingdecisionmodels reinforcementlearning,’’Mach.Learn.,vol.113,no.5,pp.2795–2839,
insmarteconomicmanagement:Cross-marketforecastingandoptimiza- May2024.
tion,’’SSRNElectron.J.,vol.2024,pp.1–21,Sep.2024. [147] L.-E. Wang, Y. Wang, Y. Bai, P. Liu, and X. Li, ‘‘POI recommenda-
[125] V.V.Ramasesh,A.Lewkowycz,andE.Dyer,‘‘Effectofscaleoncatas- tion with federated learning and privacy preserving in cross domain
trophicforgettinginneuralnetworks,’’inProc.Int.Conf.Learn.Repre- recommendation,’’inProc.IEEEConf.Comput.Commun.Workshops
sent.,2021,pp.1–12. (INFOCOMWKSHPS),May2021,pp.1–6.
[126] G.M.vandeVen,N.Soures,andD.Kudithipudi,‘‘Continuallearning [148] S. R. Chalamala, N. K. Kummari, A. K. Singh, A. Saibewar,
andcatastrophicforgetting,’’2024,arXiv:2403.05175. and K. M. Chalavadi, ‘‘Federated learning to comply with data
[127] Q. Guo, Z. Li, B. An, P. Hui, J. Huang, L. Zhang, and M. Zhao, protection regulations,’’ CSI Trans. ICT, vol. 10, no. 1, pp.47–60,
‘‘Securingthedeepfrauddetectorinlarge-scalee-commerceplatformvia Mar.2022.
adversarialmachinelearningapproach,’’inProc.WorldWideWebConf., [149] J.Li,T.Cui,K.Yang,R.Yuan,L.He,andM.Li,‘‘Demandforecastingof
May2019,pp.616–626. e-commerceenterprisesbasedonhorizontalfederatedlearningfromthe
[128] M. F. Zeager, A. Sridhar, N. Fogal, S. Adams, D. E. Brown, perspectiveofsustainabledevelopment,’’Sustainability,vol.13,no.23,
and P. A. Beling, ‘‘Adversarial learning in credit card fraud detec- p.13050,Nov.2021.
tion,’’ in Proc. Syst. Inf. Eng. Design Symp. (SIEDS), Apr. 2017, [150] X.Wu,Y.Zhang,M.Shi,P.Li,R.Li,andN.N.Xiong,‘‘Anadaptive
pp.112–116. federatedlearningschemewithdifferentialprivacypreserving,’’Future
[129] F.Cartella,O.Anunciacao,Y.Funabiki,D.Yamaguchi,T.Akishita,and Gener.Comput.Syst.,vol.127,pp.362–372,Feb.2022.
O.Elshocht,‘‘Adversarialattacksfortabulardata:Applicationtofraud [151] L.Shanmugam,R.Tillu,andM.Tomar,‘‘Federatedlearningarchitecture:
detectionandimbalanceddata,’’2021,arXiv:2101.08030. Design, implementation, and challenges in distributed AI systems,’’
[130] W.Hilal,S.A.Gadsden,andJ.Yawney,‘‘Financialfraud:Areviewof J.Knowl.Learn.Sci.Technol.,vol.2,no.2,pp.371–384,Sep.2023.
anomalydetectiontechniquesandrecentadvances,’’ExpertSyst.Appl., [152] X. Zhang and V. S. Sheng, ‘‘Neuro-symbolic AI: Explainability,
vol.193,May2022,Art.no.116429. challenges,andfuturetrends,’’2024,arXiv:2411.04383.
[131] R.Udayakumar,A.Joshi,S.S.Boomiga,andR.Sugumar,‘‘Deepfraud [153] M. Ansari, S. A. Ali, M. Alam, K. Chaudhary, and S. Rakshit,
net: A deep learning approach for cyber security and financial fraud ‘‘Unlockingthepowerofexplainableaitoimprovecustomerexperiences
detectionandclassification,’’J.InternetServicesInf.Secur.,vol.13,no.4, in e-commerce,’’ in AI-Based Data Analytics. Boca Raton, FL, USA:
pp.138–157,Dec.2023. AuerbachPublications,2023,pp.31–48.
VOLUME13,2025 99065

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
[154] B. P. Bhuyan, A. Ramdane-Cherif, T. P. Singh, and R. Tomar, [176] N. Acharya, A.-M. Sassenberg, and J. Soar, ‘‘Effects of cognitive
‘‘Neuro-symbolic AI: The fusion of symbolic reasoning and machine absorption on continuous use intention of AI-driven recommender
learning,’’inNeuro-SymbolicArtificialIntelligence:BridgingLogicand systems in e-commerce,’’ Foresight, vol. 25, no. 2, pp.194–208,
| Learning.Cham,Switzerland:Springer,2024,pp.17–27. |     |     |     |     |     |     |     | Apr.2023. |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
[155] K. Anderson, ‘‘Neurosymbolic AI revolutionizing fraud prevention [177] E. L. Aleixo, J. G. Colonna, M. Cristo, and E. Fernandes, ‘‘Catas-
systems,’’Tech.Rep.,2022. trophicforgettingindeeplearning:Acomprehensivetaxonomy,’’2023,
[156] X.Ding,N.Seleznev,S.Kumar,C.B.Bruss,andL.Akoglu,‘‘From arXiv:2312.10549.
detectiontoaction:Ahuman-in-the-looptoolkitforanomalyreasoning [178] D. Muthirayan and P. P. Khargonekar, ‘‘Memory augmented
andmanagement,’’inProc.4thACMInt.Conf.AIFinance,Nov.2023, neural network adaptive controllers: Performance and stability,’’
pp.279–287. IEEE Trans. Autom. Control, vol. 68, no. 2, pp.825–838,
| [157] Z. Lu, | I. Afridi, | H. J. | Kang, I. | Ruchkin, | and X. | Zheng, ‘‘Surveying |     | Feb.2023. |     |     |     |     |     |
| ------------ | ---------- | ----- | -------- | -------- | ------ | ------------------ | --- | --------- | --- | --- | --- | --- | --- |
neuro-symbolicapproachesforreliableartificialintelligenceofthings,’’ [179] N.XiaoandL.Zhang,‘‘Dynamicweightedlearningforunsupervised
J.ReliableIntell.Environments,vol.10,no.3,pp.257–279,Sep.2024. domain adaptation,’’ in Proc. IEEE/CVF Conf. Comput. Vis. Pattern
[158] R.C.Tanguturi,A.Devendran,andS.Umarani,‘‘Theroleofquantum Recognit.(CVPR),Jun.2021,pp.15237–15246.
machinelearninginoptimizingneuromarketinginsightsforretailande- [180] Z. Zhou, M. Wang, C.-N. Yang, Z. Fu, X. Sun, and Q. M. J. Wu,
commerce,’’inTheQuantumAIEraofNeuromarketing.Hershey,PA, ‘‘Blockchain-based decentralized reputation system in e-commerce
USA:IGIGlobalScientificPublishing,2025,pp.243–254. environment,’’ Future Gener. Comput. Syst., vol. 124, pp.155–167,
| [159] F.TellezandJ.Ortiz,‘‘ComparingAIalgorithmsforoptimizingelliptic |     |     |     |     |     |     |     | Nov.2021. |     |     |     |     |     |
| --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
curve cryptography parameters in e-Commerce integrations: A pre- [181] D. Martinez, L. Magdalena, and A. N. Savitri, ‘‘AI and blockchain
quantum analysis,’’ Int. J. Adv. Comput. Sci. Appl., vol. 15, no. 6, integration: Enhancing security and transparency in financial
pp.1539–1552,2024. transactions,’’ Int. Trans. Artif. Intell., vol. 3, no. 1, pp.11–20,
| [160] J. Shi, | F. Shang, | S. Zhou, | X. Zhang, | and | G. Ping, | ‘‘Applications | of  | Nov.2024. |     |     |     |     |     |
| ------------- | --------- | -------- | --------- | --- | -------- | -------------- | --- | --------- | --- | --- | --- | --- | --- |
quantummachinelearninginlarge-scalee-commercerecommendation [182] H. Oluwabunmi Bello, C. Idemudia, and T. V. Lyelolu, ‘‘Integrating
systems: Enhancing efficiency and accuracy,’’ J. Ind. Eng. Appl. Sci., machinelearningandblockchain:Conceptualframeworksforreal-time
vol.2,no.4,pp.90–103,2024. frauddetectionandprevention,’’WorldJ.Adv.Res.Rev.,vol.23,no.1,
[161] L.M.Gutta,B.Dhamodharan,P.K.Dutta,andP.Whig,‘‘AI-infused pp.56–68,Jul.2024.
|     |     |     |     |     |     |     |     | [183] Y.Xiao,C.Zhou,X.Guo,Y.Song,andC.Chen,‘‘Anoveldecentralized |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- |
quantummachinelearningforenhancedsupplychainforecasting,’’in
Quantum Computing and Supply Chain Management: A New Era of e-commercetransactionsystembasedonblockchain,’’Appl.Sci.,vol.12,
Optimization.Hershey,PA,USA:IGIGlobal,2024,pp.48–63. no.12,p.5770,Jun.2022.
[162] R. Khurana, ‘‘Applications of quantum computing in telecom [184] E.R.Onwubuariri,B.O.Adelakun,O.P.Olaiya,andJ.E.K.Ziork-
|             |     |          |         |       |     |     |          | lui, ‘‘AI-driven | risk assessment: | Revolutionizing |     | audit | planning and |
| ----------- | --- | -------- | ------- | ----- | --- | --- | -------- | ---------------- | ---------------- | --------------- | --- | ----- | ------------ |
| e-commerce: |     | Analysis | of QKD, | QAOA, | and | QML | for data |                  |                  |                 |     |       |              |
encryption, speed optimization, and AI-driven customer experience,’’ execution,’’FinanceAccountingRes.J.,vol.6,no.6,pp.1069–1090,
| Quart.J.Emerg.Technol.Innov.,vol.7,no.9,pp.1–15,2022. |     |     |     |     |     |     |     | Jun.2024. |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
[163] F. Phillipson, ‘‘Quantum computing in logistics and supply chain [185] M.T.A.Tonoy,A.Islam,A.K.Das,M.K.Sah,andA.K.Mansoor,
managementanoverview,’’2024,arXiv:2402.17520. ‘‘Mitigatinge-commercesecurityriskswithblockchain:Amulti-layered
|             |            |        |               |     |        |               |     | architecture,’’ | in Proc. | Int. Conf. Intell. | Syst. | Cybersecurity | (ISCS), |
| ----------- | ---------- | ------ | ------------- | --- | ------ | ------------- | --- | --------------- | -------- | ------------------ | ----- | ------------- | ------- |
| [164] T. K. | Vashishth, | Vikas, | K. K. Sharma, | B.  | Kumar, | S. Chaudhary, | and |                 |          |                    |       |               |         |
R.Panwar,‘‘EnhancingcustomerexperiencethroughAI-enabledcontent May2024,pp.1–6.
personalization in e-commerce marketing,’’ in Advances in Digital [186] B. Girimurugan, T. Venkatesan, S. Ananthavalli, S. S. S. Gogada,
MarketingintheEraofArtificialIntelligence.BocaRaton,FL,USA: G.Fufa,andM.Peswani,‘‘Blockchainfore-commerce:Revolutionizing
securityandtrust,’’inStrategiesforE-CommerceDataSecurity:Cloud,
CRCPress,2024,pp.7–32.
[165] H. Ko, S. Lee, Y. Park, and A. Choi, ‘‘A survey of recommendation Blockchain,AI,andMachineLearning.Hershey,PA,USA:IGIGlobal,
systems:Recommendationmodels,techniques,andapplicationfields,’’ 2024,pp.333–360.
Electronics,vol.11,no.1,p.141,Jan.2022. [187] S.K.Lo,Y.Liu,Q.Lu,C.Wang,X.Xu,H.-Y.Paik,andL.Zhu,‘‘Toward
[166] H.Liu,Y.Wei,X.Song,W.Guan,Y.-F.Li,andL.Nie,‘‘MMGRec: trustworthyAI:Blockchain-basedarchitecturedesignforaccountability
|     |     |     |     |     |     |     |     | and fairness | of federated | learning systems,’’ |     | IEEE Internet | Things J., |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------ | ------------------- | --- | ------------- | ---------- |
Multimodalgenerativerecommendationwithtransformermodel,’’2024,
| arXiv:2404.16555. |     |     |     |     |     |     |     | vol.10,no.4,pp.3276–3284,Feb.2023. |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
[167] F.Pervez,M.Shoukat,M.Usama,M.Sandhu,S.Latif,andJ.Qadir, [188] A.Wasilewski,‘‘HarnessinggenerativeAIforpersonalizede-commerce
‘‘Affective computing and the road to an emotionally intelligent productdescriptions:Aframeworkandpracticalinsights,’’Comput.Stan-
dardsInterface,vol.94,Aug.2025,Art.no.104012.
metaverse,’’IEEEOpenJ.Comput.Soc.,vol.5,pp.195–214,2024.
[168] K.Bayoudh,R.Knani,F.Hamdaoui,andA.Mtibaa,‘‘Asurveyondeep [189] C.Li,Z.Gan,Z.Yang,J.Yang,L.Li,L.Wang,andJ.Gao,‘‘Multimodal
multimodallearningforcomputervision:Advances,trends,applications, foundation models: From specialists to general-purpose assistants,’’
anddatasets,’’Vis.Comput.,vol.38,no.8,pp.2939–2970,Aug.2022. Found.TrendsComput.Graph.Vis.,vol.16,nos.1–2,pp.1–214,2024.
|     |     |     |     |     |     |     |     | [190] C. Herold, | M. Kozielski, | T. Bazazo, | P. Petrushkov, | S.  | H. Hashemi, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------- | ---------- | -------------- | --- | ----------- |
[169] M.Kim,W.Shin,S.Kim,andH.-W.Kim,‘‘Predictingsessionconversion
one-commerce:Adeeplearning-basedmultimodalfusionapproach,’’ P. Cieplicka, D. Basaj, and S. Khadivi, ‘‘Domain adaptation
AsiaPacificJ.Inf.Syst.,vol.33,no.3,pp.737–767,Sep.2023. of foundation LLMs for e-commerce,’’ 2025, arXiv:2501.
| [170] F. Wang, | Y.  | Zhou, S. | Wang, V. | Vardhanabhuti, | and | L. Yu, | ‘‘Multi- | 09706. |     |     |     |     |     |
| -------------- | --- | -------- | -------- | -------------- | --- | ------ | -------- | ------ | --- | --- | --- | --- | --- |
granularitycross-modalalignmentforgeneralizedmedicalvisualrepre- [191] R. Zhang, J. He, X. Luo, D. Niyato, J. Kang, Z. Xiong, Y. Li, and
sentationlearning,’’inProc.Adv.NeuralInf.Process.Syst.,Jan.2022, B. Sikdar, ‘‘Toward democratized generative AI in next-generation
pp.33536–33549. mobile edge networks,’’ IEEE Netw., vol. 39, no. 3, p.1,
| [171] S. Purushwalkam, |     | P.  | Morgado, | and A. | Gupta, ‘‘The | challenges | of  | May2025. |     |     |     |     |     |
| ---------------------- | --- | --- | -------- | ------ | ------------ | ---------- | --- | -------- | --- | --- | --- | --- | --- |
continuousself-supervisedlearning,’’inProc.Eur.Conf.Comput.Vis. [192] S. Chandran, S. R. Syam, S. Sankaran, T. Pandey, and K. Achuthan,
|     |     |     |     |     |     |     |     | ‘‘From | static to AI-driven | detection: | A   | comprehensive | review |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------- | ---------- | --- | ------------- | ------ |
Cham,Switzerland:Springer,Jan.2022,pp.702–721.
[172] L. Caccia and J. Pineau, ‘‘SPeCiaL: Self-supervised pretraining of obfuscated malware techniques,’’ IEEE Access, vol. 13,
for continual learning,’’ in Proc. Int. Workshop Continual Semi- pp.74335–74358,2025.
Supervised Learn. Cham, Switzerland: Springer, Jan. 2022, [193] S. Agrawal, S. Merugu, and V. Sembium, ‘‘Enhancing e-commerce
pp.91–103. productsearchthroughreinforcementlearning-poweredqueryreformu-
[173] J.Yu,H.Yin,X.Xia,T.Chen,J.Li,andZ.Huang,‘‘Self-supervised lation,’’inProc.32ndACMInt.Conf.Inf.Knowl.Manage.,Oct.2023,
| learningforrecommendersystems:Asurvey,’’IEEETrans.Knowl.Data |     |     |     |     |     |     |     | pp.4488–4494. |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
Eng.,vol.36,no.1,pp.335–355,Jan.2024. [194] K. Balog and C. Zhai, ‘‘User simulation in the era of generative AI:
[174] H. Qian, Z. Dou, Y. Zhu, Y. Ma, and J.-R. Wen, ‘‘Learning implicit Usermodeling,syntheticdatageneration,andsystemevaluation,’’2025,
arXiv:2501.04410.
userprofileforpersonalizedretrieval-basedchatbot,’’inProc.30thACM
Int.Conf.Inf.Knowl.Manage.,Oct.2021,pp.1467–1477. [195] X.Zhang,F.Guo,T.Chen,L.Pan,G.Beliakov,andJ.Wu,‘‘Abrief
[175] Y.Li,R.Pogodin,D.J.Sutherland,andA.Gretton,‘‘Self-supervised surveyofmachinelearninganddeeplearningtechniquesfore-commerce
learningwithkerneldependencemaximization,’’inProc.Adv.Neural research,’’ J. Theor. Appl. Electron. Commerce Res., vol. 18, no. 4,
pp.2188–2216,Dec.2023.
Inf.Process.Syst.,Jan.2021,pp.15543–15556.
| 99066 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

E.Dritsas,M.Trigka:MachineLearninginE-Commerce:Trends,Applications,andFutureChallenges
[196] H.Jebamikyous,M.Li,Y.Suhas,andR.Kashef,‘‘Leveragingmachine ELIAS DRITSAS received the Diploma, M.Sc.,
learningandblockchainine-commerceandbeyond:Benefits,models, and Ph.D. degrees in computer science and
and application,’’ in Discover Artificial Intelligence, vol. 3, no. 1. informatics from the Department of Computer
Springer,2023,p.3.[Online].Available:https://doi.org/10.1007/s44163- EngineeringandInformatics,UniversityofPatras,
| 022-00046-0 |     |     |     |     |     |     |     |     | Greece,andtheM.B.A.degreefromtheUniversity |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
[197] P.GopalandN.B.MohdNawi,‘‘Asurveyoncustomerchurnprediction
|          |         |              |          |         |            |                  |         |     | of Derby,  | U.K.         | His  | research    | interests      | focus on |
| -------- | ------- | ------------ | -------- | ------- | ---------- | ---------------- | ------- | --- | ---------- | ------------ | ---- | ----------- | -------------- | -------- |
| using    | machine | learning     | and data | mining  | techniques | in e-commerce,’’ |         |     |            |              |      |             |                |          |
|          |         |              |          |         |            |                  |         |     | artificial | intelligence |      | and machine | learning,      | big      |
| in Proc. | IEEE    | Asia–Pacific | Conf.    | Comput. | Sci.       | Data Eng.        | (CSDE), |     |            |              |      |             |                |          |
|          |         |              |          |         |            |                  |         |     | data,      | databases,   | data | mining,     | human–computer |          |
Dec.2021,pp.1–8.
[198] M. A. Al-Ebrahim, S. Bunian, and A. A. Nour, ‘‘Recent machine- interaction,cloudcomputing,security,andtrust.
learning-driven developments in e-commerce: Current challenges Heistheauthorandco-authorofpublicationsin
|     |        |                 |            |     |       |        |         | the area of machine | learning        | and data | analysis. | He participated |     | in many   |
| --- | ------ | --------------- | ---------- | --- | ----- | ------ | ------- | ------------------- | --------------- | -------- | --------- | --------------- | --- | --------- |
| and | future | perspectives,’’ | Engineered |     | Sci., | no. 1, | p.1044, |                     |                 |          |           |                 |     |           |
|     |        |                 |            |     |       |        |         | development         | projects funded | by the   | European  | Commission      |     | and Greek |
Dec.2023.
[199] S. Dheva Rajan, S. Vavilapalli, S. Hasan, R. Kumar, N. Rafa, and SecretariatofResearchandTechnology.HeisamemberoftheTechnical
I.Muda,‘‘Asurveyontheimpactofdataanalyticsandmachinelearning ChamberofGreeceandtheAssociationforComputingMachinery.Heserves
techniques in e-commerce,’’ in Proc. 5th Int. Conf. Contemp. Com- asaregularreviewerforseveraltechnicaljournalsandconferences.
put.Informat.(IC3I),Dec.2022,pp.1117–1122.
| [200] C. C.  | Ike, A.        | B. Ige, S. | A. Oladosu,    | P.      | A. Adepoju,    | O. O.          | Amoo,    |     |                                          |        |          |          |           |         |
| ------------ | -------------- | ---------- | -------------- | ------- | -------------- | -------------- | -------- | --- | ---------------------------------------- | ------ | -------- | -------- | --------- | ------- |
| and          | A. I. Afolabi, |            | ‘‘Advancing    | machine | learning       | frameworks     |          |     |                                          |        |          |          |           |         |
| for customer |                | retention  | and propensity |         | modeling       | in e-commerce  |          |     |                                          |        |          |          |           |         |
| platforms,’’ | GSC            | Adv.       | Res. Rev.,     | vol.    | 14, no.        | 2, pp.191–203, |          |     |                                          |        |          |          |           |         |
|              |                |            |                |         |                |                |          |     | MARIA                                    | TRIGKA | received | the      | Diploma   | degree  |
| Feb.2023.    |                |            |                |         |                |                |          |     | fromtheDepartmentofElectricalandComputer |        |          |          |           |         |
| [201] L. M.  | Policarpo,     | D. E.      | da Silveira,   | R.      | da Rosa Righi, | R. A.          | Stoffel, |     |                                          |        |          |          |           |         |
|              |                |            |                |         |                |                |          |     | Engineering                              |        | and the  | master’s | and Ph.D. | degrees |
C.A.daCosta,J.L.V.Barbosa,R.Scorsatto,andT.Arcot,‘‘Machine
insignalprocessingforwirelesscommunications
| learning   | through    | the lens  | of e-commerce |      | initiatives: | An up-to-date |       |     |      |                |            |             |            |             |
| ---------- | ---------- | --------- | ------------- | ---- | ------------ | ------------- | ----- | --- | ---- | -------------- | ---------- | ----------- | ---------- | ----------- |
|            |            |           |               |      |              |               |       |     | from | the Department |            | of Computer |            | Engineering |
| systematic | literature | review,’’ | Comput.       | Sci. | Rev.,        | vol. 41, Aug. | 2021, |     |      |                |            |             |            |             |
|            |            |           |               |      |              |               |       |     | and  | Informatics,   | University |             | of Patras, | Greece.     |
Art.no.100414.
[202] K.Achuthan,S.Ramanathan,S.Srinivas,andR.Raman,‘‘Advancing As a Ph.D. Candidate, she was a Research
cybersecurity and privacy with artificial intelligence: Current trends ScholarundertheProject‘‘StrengtheningHuman
andfutureresearchdirections,’’FrontiersBigData,vol.7,Dec.2024, Research Potential through Doctoral Research’’
Art.no.1497535. co-financed by Greece-State Scholarships Foun-
| [203] M. Sharma, | V.  | Sharma, | and R. | Kapoor, | ‘‘Study | of e-commerce | and |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ------ | ------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
dation(IKY)andEuropeanUnion.Also,shehasbeeninvolvedinresearch
impactofmachinelearningine-commerce,’’inEmpiricalResearchfor
projectsco-financedbyEuropeanUnionandGreeknationalfundsthrough
E-CommerceFuturisticSystems:FoundationsandApplications.Hershey, theOperationalProgramCompetitiveness,EntrepreneurshipandInnovation,
PA,USA:IGIGlobalz,2022,pp.1–22. underthecallRESEARCH–CREATE–INNOVATEthatemphasizedAIand
| [204] M. A.  | Gomes      | and T.       | Meisen,  | ‘‘A review | on        | customer segmenta- |     |                      |                 |          |              |           |           |             |
| ------------ | ---------- | ------------ | -------- | ---------- | --------- | ------------------ | --- | -------------------- | --------------- | -------- | ------------ | --------- | --------- | ----------- |
|              |            |              |          |            |           |                    |     | ML for developing    | health and      | cultural | services     | for the   | hard      | of hearing. |
| tion methods | for        | personalized | customer |            | targeting | in e-commerce      | use |                      |                 |          |              |           |           |             |
|              |            |              |          |            |           |                    |     | She is the author    | and co-author   | of       | publications | in        | the areas | of signal   |
| cases,’’     | Inf. Syst. | e-Business   | Manage., |            | vol. 21,  | no. 3, pp.527–570, |     |                      |                 |          |              |           |           |             |
|              |            |              |          |            |           |                    |     | processing, wireless | communications, |          | and machine  | learning. |           | Her general |
Sep.2023.
[205] K. Achuthan, S. Sankaran, S. Roy, and R. Raman, ‘‘Integrating research interests span the scientific areas of statistical signal processing
sustainability into cybersecurity: Insights from machine learning and learning, focusing on estimation theory, adaptive/distributed signal
based topic modeling,’’ Discover Sustainability, vol. 6, no. 1, p.44, processing,andsparserepresentations.
Jan.2025.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 99067 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |