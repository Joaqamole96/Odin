Received21September2025,accepted7October2025,dateofpublication24October2025,dateofcurrentversion17November2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3625441
Deep Feature Extraction Method for Automatic
Classification and Processing of Accounting
Information
FENGRUILIU
LiaoningDongdingCertifiedPublicAccountants,Benxi117000,China
e-mail:terkinmeosh@hotmail.com
ABSTRACT In the context of advancing intelligent accounting systems within the broader field of
computationalmethodsanddataprocessing,thisstudyfocusesonovercomingcriticallimitationsinherentin
conventionalaccountinginformationclassificationmethodologies.Thesetraditionalsystemsoftenexhibit
low adaptability to rapidly evolving data characteristics and a heavy dependence on manually crafted
feature engineering pipelines. Existing approaches predominantly rely on predefined statistical heuristics
or shallow machine learning models, which are insufficient for capturing the intricate, non-linear, and
high-dimensionalrelationshipsembeddedinmodernfinancialdatasets—especiallythosegeneratedbylarge-
scale enterprise resource planning systems. To address these constraints, we propose a novel deep feature
extraction framework grounded in convolutional autoencoder architectures. This framework is designed
to autonomously learn multi-level hierarchical feature representations directly from raw journal entries,
eliminating the need for domain-specific feature selection. Our approach incorporates a dual-objective
designthatsimultaneouslyperformsinputreconstructionandclassification,allowingthenetworktopreserve
input fidelity while promoting discriminative learning. Furthermore, an adversarial training component is
introducedtoenhancegeneralizationperformance,especiallyunderconditionsofclassimbalanceandinput
noise—bothcommonissuesinfinancialtransactiondata.Weevaluateourmethodonacomprehensivereal-
worldaccountingdatasetcomposedofannotatedjournallogsacrossmultiplebusinessunits.Experimental
resultsdemonstratesubstantialimprovementsinbothclassificationaccuracyandanomalydetectionF1-score
whencomparedtotraditionalbaselinemodelssuchaslogisticregressionanddecisiontrees.Ourfindings
illustratethepotentialofdeeplearning-basedarchitecturesforintelligentaccountingsystemsandcontribute
tothegrowingbodyofresearchonadaptive,scalable,andautomatedsolutionsforfinancialdataanalysis
andauditingincomputationalfinance.
INDEX TERMS Deepfeatureextraction,automaticaccountingclassification,convolutionalautoencoder,
anomalydetection,adversarialrepresentationlearning.
I. INTRODUCTION data volume and heterogeneity continue to grow, reliance
The rapid expansion of enterprise data and the increasing on manual inspection and rule-based protocols becomes
complexity of financial environments have made the auto- increasingly unsustainable, particularly in large-scale and
maticclassificationandprocessingofaccountinginformation time-sensitivebusinessoperations[1].Therefore,developing
a critical research task. Traditional manual methods are efficient, accurate, and scalable computational methods for
not only labor-intensive but also prone to errors, which handling accounting data is of vital importance. Not only
can severely impact decision-making quality. As financial can automated systems reduce operational costs, but they
alsoimproveconsistencyandaccuracyinfinancialreporting
by minimizing human error and subjectivity. Automation
The associate editor coordinating the review of this manuscript and
enables faster reconciliation of accounts, real-time anomaly
approvingitforpublicationwasOlarikSurinta .
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
193232 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
detection,andcompliancemonitoring,allofwhichareessen- limited their ability to generalize or learn from historical
tialintoday’shigh-stakesfinancialecosystem.Furthermore, patterns,renderingthemineffectiveinscenariosthatrequired
withthedigitizationoffinancialtransactionsandtheadvent contextual awareness or adaptive decision-making. As a
of intelligent financial systems, such as enterprise resource result, although rule-oriented frameworks laid an important
planning (ERP) platforms and robotic process automation foundation for automating accounting classification, they
(RPA), there is a growing demand for advanced techniques highlightedtheneedformoreintelligentsystemscapableof
thatcanunderstandandprocessbothunstructuredandstruc- evolving with data and minimizing dependence on manual
turedaccountingdatainrealtime[1],[2],[3].Theseinclude rule curation. These limitations ultimately catalyzed the
journal entries, receipts, invoices, emails, spreadsheets, and exploration of more flexible computational strategies that
transaction logs, which often exhibit irregular formats, could adapt to new data distributions and capture subtle
semantic ambiguity, and inconsistent quality. This diversity patternsbeyondthereachofhand-codedlogic[9],[10].
introduces new technical challenges in data representation To improve adaptability and reduce dependence on rigid
andprocessingthattraditionalsystemsfailtoaccommodate. rule structures, statistical learning models were developed
As a result, recent research has increasingly focused on to identify classification patterns from annotated financial
learning-basedfeatureextractionmethodsthatautomatically logs.Byutilizingsupervisedalgorithmsthatlearneddecision
uncover latent structure from complex accounting records boundaries from examples, these models achieved better
without relying on predefined templates. Among these, generalization across various scenarios, especially when
deeplearning-basedtechniques,particularlythoseemploying the transaction data exhibited variability in structure and
hierarchicalneuralnetworks,haveshownremarkablesuccess semantics. Techniques such as logistic regression, decision
in modeling the intricate dependencies present in financial trees, support vector machines, and ensemble methods
data. This underscores the necessity of exploring and like random forests became widely adopted in accounting
enhancing deep feature extraction methods, which promise informationclassificationtasks[11],[12].Theseapproaches
a higher level of automation, adaptability, and intelligence offered notable improvements over rule-based systems by
infinancialdatahandling,ultimatelydrivingmoreinformed allowing models to infer data-label relationships directly
decision-making and resilient financial infrastructures [4], from historical observations, rather than relying solely on
[5]. expert-crafted rules. For instance, models could learn to
Initial efforts to address these challenges introduced associate specific account codes with textual descriptions
rule-oriented frameworks that formalized domain expertise or identify fraud-prone behavior from numerical attributes.
into structured processing routines. These systems were Thisshiftintroducedamoredata-centricparadigmthatwas
built on deterministic rules and heuristic decision trees to fastertodeployacrosssimilartaskdomainsandmoderately
emulateaccountinglogicandlabeltransactionsaccordingly. resilient to noise or inconsistencies in input. Nevertheless,
By encoding predefined mappings between input patterns despite these advancements, statistical learning models still
and accounting labels, such frameworks offered a degree of required significant human intervention in the form of
transparency and interpretability, which made them suitable handcrafted features. Designing effective input variables—
for early-stage automation in financial institutions. Their suchastransactionfrequency,monetarythresholds,counter-
close alignment with established accounting principles also party identifiers, categorical tags, and semantic patterns—
provided a sense of regulatory compliance and traceability, demandeddeepdomainknowledgeanditerativerefinement.
both of which are crucial in the auditing and reporting Thesefeaturesoftencapturedonlysurface-levelrelationships
process. However, these advantages came at the cost of and failed to reflect deeper contextual interactions among
flexibilityandscalability[6],[7].Asfinancialrecordsdiver- financialentitiesortemporalsequences[2],[13].Asfinancial
sified in format and content—ranging from digital receipts datasets became more complex, encompassing multimodal
and structured ledger entries to semi-structured emails records like textual justifications, invoice images, and tem-
and invoices—these static systems struggled to maintain poral sequences of interrelated entries, conventional feature
performance. The hard-coded rules failed to accommodate engineering approaches struggled to keep pace. Moreover,
edge cases, inconsistencies, and emerging transaction types the fixed feature representations limited model flexibility
thatdeviatedfromtheirpredefinedtemplates.Moreover,the when applied to new institutions or accounting standards,
maintenance of such systems required continuous involve- often necessitating manual redesign and retraining. Models
mentofdomainexperts,whoneededtoupdaterulesandlogic also became vulnerable to changes in data distribution or
inresponsetopolicychanges,systemmigrations,andmarket previouslyunseentransactiontypes,resultinginperformance
innovations. This led to a bottleneck in scalability, as the degradation under real-world deployment conditions. The
cost and complexity of upkeep escalated with the volume curse of dimensionality posed further challenges as the
and variety of data. In dynamic enterprise settings, where number of input features increased. Redundant, noisy,
thousandsoftransactionsareprocesseddailyacrossmultiple or irrelevant features introduced variance and instability,
departments and business units, this approach quickly requiring careful feature selection and regularization tech-
becameuntenable[8].Therigidityofrule-basedsystemsalso niquestopreservemodelaccuracy[14],[15].Thesepractical
VOLUME13,2025 193233

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
bottlenecksunderscoredthenecessityoftransitioningtoward To address the limitations of previous approaches—
more autonomous and expressive learning frameworks. The including symbolic systems’ lack of adaptability, machine
increasing demand for models that could ingest raw or learning’sdependenceonmanualfeatures,anddeepmodels’
minimally processed data while automatically discovering computational overhead—we propose a refined feature
meaningfulabstractionssetthestagefordeeperarchitectures extractionframeworktailoredtotheautomaticclassification
capable of end-to-end learning without exhaustive manual andprocessingofaccountinginformation.Thismethodinte-
preprocessing. grates domain-specific attention mechanisms with efficient
In response, a new generation of models has emerged, deep architectures to capture both global transaction trends
capable of directly processing raw accounting data through and local entry nuances. Unlike prior models, which either
hierarchical representation learning. These models leverage focused narrowly on structured data or required extensive
the expressive power of deep neural networks to automati- labeled corpora, our approach balances generalization with
cally capture latent structures in complex financial records specificity,adaptingacrossdiverseaccountingcontextswith
withouttheneedforexhaustivemanualfeatureengineering. minimal supervision. Moreover, it incorporates lightweight
Architecturessuchasconvolutionalneuralnetworks(CNNs), transfer learning strategies, enabling effective performance
recurrent neural networks (RNNs), and transformer-based withlimitedcomputationalresources.Thisshifttowardmore
models have proven particularly effective in this domain. specialized yet scalable solutions is essential for meeting
CNNs have been applied to extract spatial correlations in the increasing demands of intelligent financial information
| structured | accounting |     | matrices | or  | numerical | embeddings, |     | systems. |     |     |     |     |     |     |
| ---------- | ---------- | --- | -------- | --- | --------- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
while RNNs and gated variants like LSTM and GRU have In summary, our proposed framework offers a robust and
demonstrated success in modeling the sequential nature intelligentsolutiontothechallengesinautomatedaccounting
of financial transactions, where the order and context of information processing. Below, we summarize the main
entriesoftenholdcriticalinformation.Attentionmechanisms innovationsofthiswork:
have enabled models to selectively focus on salient aspects • Domain-Attentive Graph Modeling: We introduce a
of the input, facilitating a more nuanced understanding novel graph encoder that captures temporal evolution,
| of interrelated |     | entries | across | long | sequences |     | or multi- |     |     |     |     |     |     |     |
| --------------- | --- | ------- | ------ | ---- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
semanticstructure,andtransactiondependenciesacross
document records [5], [16]. These advancements have financialrecords.
| enabled | end-to-end | learning |     | systems | that | can process | raw |     |     |     |     |     |     |     |
| ------- | ---------- | -------- | --- | ------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
• Audit-InformedReinforcementLearning:OurAIRP
journal entries, parse invoice metadata, and even integrate module integrates compliance constraints directly into
textual annotations or receipts. By learning both local and the policy learning process, enabling interpretable and
| global patterns, |     | these | models | excel | at tasks | such | as auto- |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | ------ | ----- | -------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
regulation-awarefiscaldecision-making.
matic account classification, fraud detection, and anomaly • Hybrid Symbolic-Neural Integration: The model
| recognition, | achieving |     | higher | accuracy |     | and generalization |     |          |          |     |             |      |      |          |
| ------------ | --------- | --- | ------ | -------- | --- | ------------------ | --- | -------- | -------- | --- | ----------- | ---- | ---- | -------- |
|              |           |     |        |          |     |                    |     | connects | symbolic |     | audit rules | with | deep | learning |
compared to earlier statistical techniques. Furthermore, architectures, bridging the gap between transparency
the use of pretraining on large-scale financial corpora andpredictiveperformance.
| or transfer | learning    |     | from            | general    | language   |              | models has |               |             |              |         |              |                 |       |
| ----------- | ----------- | --- | --------------- | ---------- | ---------- | ------------ | ---------- | ------------- | ----------- | ------------ | ------- | ------------ | --------------- | ----- |
|             |             |     |                 |            |            |              |            | These         | innovations | collectively |         | address      | the limitations |       |
| enhanced    | performance |     | in low-resource |            | scenarios, |              | allowing   |               |             |              |         |              |                 |       |
|             |             |     |                 |            |            |              |            | of rule-based | and         | shallow      | models, | establishing |                 | a new |
| models      | to adapt    | to  | varied          | accounting |            | vocabularies | and        |               |             |              |         |              |                 |       |
directionforscalable,explainable,andcompliantaccounting
| practicesacrossorganizations[7],[17].Despitethesepromis- |     |     |            |     |         |      |        | automation. |     |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | ---------- | --- | ------- | ---- | ------ | ----------- | --- | --- | --- | --- | --- | --- |
| ing developments,                                        |     | key | challenges |     | remain. | Deep | models |             |     |     |     |     |     |     |
often behave as BB, making it difficult for auditors and II. RELATEDWORK
financial professionals to understand the reasoning behind A. DEEPLEARNINGINACCOUNTING
their outputs. This lack of transparency poses significant Recent advancements in deep learning have significantly
|          |                |     |          |      |        |     |              | transformed | the landscape |     | of accounting | information |     | sys- |
| -------- | -------------- | --- | -------- | ---- | ------ | --- | ------------ | ----------- | ------------- | --- | ------------- | ----------- | --- | ---- |
| concerns | in high-stakes |     | settings | that | demand |     | traceability |             |               |     |               |             |     |      |
and compliance with financial regulations. Moreover, the tems by enabling automatic classification and intelligent
high data requirements and computational costs associated processing of complex financial data. One of the most
with training such models may limit their accessibility for influential applications has been the utilization of neural
smaller enterprises or real-time applications. Consequently, networks,particularlyconvolutionalneuralnetworks(CNNs)
ongoing research is increasingly focused on improving and recurrent neural networks (RNNs), to extract semantic
interpretabilitythroughtechniquessuchassaliencymapping, andstructuralfeaturesfromlargevolumesofunstructuredor
attributionscores,andprototypelearning,aswellasenhanc- semi-structured accounting data. These models can process
ingdataefficiencyviasemi-supervisedlearning,knowledge various forms of financial inputs, such as invoices, ledgers,
distillation, and compact network design. These efforts balancesheets,andnarrativereports,identifyingpatternsthat
aim to bridge the gap between high model performance areimperceptibletotraditionalstatisticalmethods[1],[19].
and practical usability in modern accounting intelligence TheintegrationofwordembeddingslikeWord2Vec,GloVe,
systems[10],[18]. and BERT within these frameworks has allowed models to
| 193234 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
capturecontextualanddomain-specificmeaningsofaccount- employed hierarchical attention mechanisms to model the
ingterms,enhancingclassificationaccuracy.Studiessuchas interdependencebetweendocumentsectionssuchasheaders,
those by Zhang et al. [38] have shown that deep learning lineitems,footnotes,andannotations.Forinstance,methods
outperformsrule-basedandmachinelearningapproachesin like LayoutLM and its successors integrate visual layout
frauddetectionandauditriskassessment.Similarly,autoen- information with text embeddings to better understand
coders have been applied to compress high-dimensional document context, which is particularly crucial in financial
accountingfeaturesintocompactrepresentationssuitablefor statementswherespatialpositioningconveyssemanticroles.
downstreamclassificationtasks.Theserepresentationsoften Graph neural networks (GNNs) have also emerged as a
capturelatentvariablessuchastransactionregularities,cost powerfultoolformodelingrelationshipsbetweenaccounting
structures,oranomalyindicatorsthatarecriticalforfinancial entities,enablingthediscoveryoflatentlinkssuchasrelated
decision-making [12], [20]. Furthermore, recent attention- partytransactionsornetworkedfinancialdependencies[17],
based models and architectures, such as BERT and its [27]. In tasks such as automatic journal entry classification,
accounting-specificadaptations,havedemonstratedsuperior entity recognition, and audit trail reconstruction, deep
capabilitiesinhandlinglong-rangedependenciesinfinancial features extracted from pre-trained language models are
narratives, allowing for more nuanced document classifica- fine-tunedtocapturedomain-specificregularities.Moreover,
tionandsentimentanalysis.Integrationwithopticalcharacter cross-documentattentionandretrievalmodelsallowsystems
recognition (OCR) tools has extended these capabilities to to contextualize entries by referencing related documents,
scannedandhandwrittenfinancialdocuments,providingend- suchaslinkinganexpenseclaimtoacontractorprocurement
to-endautomationpipelines[13],[21].However,challenges record. Despite these advances, generalization remains a
remain in ensuring interpretability, regulatory compliance, significant hurdle due to the diversity in document formats,
and robustness to adversarial inputs, particularly in high- accountingstandards,andterminologiesacrossorganizations
stakes accounting environments. The field continues to andjurisdictions[28],[29].Effortsareunderwaytoconstruct
evolve towards hybrid models that combine rule-based large-scale, annotated corpora of accounting documents
domain knowledge with deep representations, aiming to and to develop domain-adaptive pretraining methods that
preserveexplainabilitywhileleveragingthepowerofneural align linguistic and numerical patterns with accounting
computation[15],[22]. logic. The pursuit of explainable AI (XAI) in financial
Recent advances in the application of deep learning documentanalysisisalsogainingmomentum,withattention
and explainable AI (XAI) have significantly influenced the visualization and concept attribution being employed to
accountingandauditingdomains.Zhangetal.emphasizethe enhancemodeltransparencyandtrustworthinessforauditors
growing importance of explainability in auditing processes, andregulators[1],[30].
highlighting how XAI techniques can improve trust, trans-
parency,andregulatoryalignmentinfinancialsystems[23].
Similarly,WuandDudemonstratethatdeeplearningmodels C. AUTOMATEDACCOUNTINGCLASSIFICATION
can effectively detect financial statement fraud in complex Automated classification of accounting entries and transac-
and data-rich environments, such as those found in Chinese tions is a foundational component of intelligent financial
listed firms [24]. Craja et al. further explore various deep systems,andrecentdeeplearningtechniqueshavemarkedly
learning architectures and show their superiority over tradi- improved performance in this domain by enabling sophis-
tional statistical methods in identifying fraudulent patterns ticated feature extraction from raw and semi-structured
in financial disclosures [25]. These studies underscore the inputs. Traditional accounting systems rely heavily on
potentialofAIinenhancingaccountingpractices.Ourwork manually crafted rules and extensive domain knowledge,
builds on these foundations by incorporating constraint- which are both labor-intensive and inflexible to evolving
aware learning and temporal-structural graph modeling to data landscapes [19]. In contrast, modern systems utilize
supportreal-timeandregulation-sensitivefinancialdecision- end-to-end deep learning pipelines that learn hierarchical
making. representations of transactions directly from data, cap-
turing intricate dependencies between attributes such as
date, amount, category, vendor, and narrative description.
B. FINANCIALDOCUMENTUNDERSTANDING Transformer-based models, particularly those adapted for
The domain of financial document understanding has tabular and sequence data, have demonstrated exceptional
seen remarkable progress with the advent of deep fea- capabilities in capturing both local syntactic features and
ture extraction techniques tailored to the unique structure globalsemanticpatternsinaccountingrecords.Sequence-to-
and semantics of accounting texts. Unlike general-purpose sequencemodelshavebeenappliedtotaskssuchasaccount
document classification tasks, accounting documents often mapping, VAT code classification, and regulatory tagging,
containheterogeneousdatatypesincludingnumericaltables, while attention mechanisms ensure that critical transaction
textualnarratives,andstructuredmetadata.Thiscomplexity featuresreceivehigherimportanceduringclassification[20],
necessitatesspecializedarchitecturesthatcanjointlyprocess [31]. Transfer learning and domain adaptation techniques
multimodal inputs [16], [26]. State-of-the-art systems have further enhance these models by incorporating financial
VOLUME13,2025 193235

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
knowledge from publicly available datasets and adapting definingaunifiednotationsystemandmathematicalformu-
toorganization-specificidiosyncrasies[21].Integrationwith lationtoabstractandmodelthedynamicsoffinancialassets,
external knowledge bases, such as accounting standards or liabilities, operational flows, and compliance constraints.
taxonomies, allows for constraint-aware classification that sectionlaysthegroundworkbyexpressingkeyfinancialinter-
respectsregulatoryframeworks.Reinforcementlearningand actions as structured operators over time-indexed variable
active learning paradigms have also been proposed to itera- spaces,enablingsymbolicreasoningandanalyticaltractabil-
tivelyrefineclassificationstrategiesbasedonfeedbackfrom ity. In Section III-C, we introduce our novel architectural
humanaccountants,improvingmodelperformanceovertime. formulation, titled FinGraphNet, which reconceptualizes
Despite these advancements, challenges persist in handling financial management as a graph-based temporal reasoning
noisy data, imbalanced class distributions, and ambiguous task. FinGraphNet encodes multi-source financial data—
transaction descriptions [22]. Research is also focusing includingbudgetaryforecasts,real-timetransactionstreams,
on continual learning approaches that allow classification and compliance logs—into an adaptive, structured graph
systems to update their models in response to new data representation. By coupling dynamic embedding modules
without catastrophic forgetting. The convergence of deep with constrained optimization layers, our model supports
feature extraction, domain-specific knowledge integration, both fine-grained inference and high-level fiscal decision
andinteractivelearningispoisedtoredefinetheautomation modeling.Thisstructuralmodeldivergesfromconventional
landscape of accounting information processing, paving the ledger-based systems by emphasizing temporal correlation,
way for more efficient, accurate, and adaptive financial dependencypropagation,andstructuralregularizationacross
systems[26]. fiscal entities. Section III-D articulates our strategic engine,
coined Audit-Informed Reinforcement Planning (AIRP),
III. METHOD designedtoleveragedomain-specificaudittrailsandcontrol
A. OVERVIEW signals to steer financial decision paths. AIRP constructs a
To clearly articulate the innovative contributions of this knowledge-drivenfeedbackmechanismintothemanagement
work, we emphasize three core aspects that distinguish our loop by extracting implicit constraints from historical audit
framework from prior methods. Our model introduces a records and encoding them into reinforcement learning
noveldomain-attentivedynamicgraphencoderthatcaptures agents.Theseagentssimulatecounterfactualfiscalscenarios
not only the temporal evolution of financial transactions and optimize decision policies under uncertainty and com-
but also the semantic and hierarchical roles of accounting pliance constraints, making the financial system not only
entities, enabling fine-grained feature extraction beyond reactive but alsoanticipatory. Collectively, these threecom-
traditional sequence-based models. We embed regulatory ponents construct a cohesive methodology that transcends
and compliance constraints directly into the learning and staticfinancialreporting,aligningfinancialintelligencewith
decision-making pipeline through a constraint-aware opti- organizationalagilityandregulatoryrobustness.Byembed-
mization layer and audit-guided reinforcement planning ding semantic structure, algorithmic interpretability, and
(AIRP), which ensures both accuracy and accountability in strategic feedback into enterprise financial operations, this
fiscalactions.Ourhybridintegrationofsymbolicauditrules approachproposesascalableandformallygroundedpathway
with deep neural representations bridges the gap between to modernize EFM practices. The remainder of this section
explainability and performance, addressing a long-standing outlines the critical roles and interconnections among the
challengeinfinancialautomation.Theseinnovationsjointly upcoming subsections, offering a roadmap for the method-
contribute to a scalable, interpretable, and regulation-aware ologicalinnovationsthatfollow.
frameworkforintelligentaccountinginformationprocessing. To ensure clarity for readers from both technical and
Enterprisefinancialmanagement(EFM)standsatthecore accounting backgrounds, we include a glossary of key
of organizational sustainability and strategic progression, financialtermsusedthroughoutthepaper.Thesedefinitions
integrating a wide array of fiscal activities to ensure opera- provide concise explanations of fundamental concepts—
tional stability, regulatory compliance, and long-term value such as assets, liabilities, liquidity, and audit constraints—
creation.Asbusinessesnavigateincreasinglyvolatileglobal that are central to our modeling framework. The glossary
markets, the demand for intelligent, data-driven financial (see Table 1) aims to assist interdisciplinary readers in
systems has intensified, prompting a shift from traditional understanding the domain-specific context in which the
accounting practices to comprehensive, digitized financial proposedmethodsoperate.
ecosystems.Thispaperpresentsastructuredmethodological
framework to advance the analytical depth and operational
precision of enterprise financial management through a B. PRELIMINARIES
formal,model-driven,andalgorithmiclens. EnterpriseFinancialManagement(EFM)canbeformalized
The forthcoming sections delineate the foundational as a multi-layered dynamic system operating over discrete
constructs, architectural enhancements, and strategic mech- fiscal periods. Let T = {t ,t ,...,t } denote a sequence
1 2 N
anismsproposedinthiswork.InSectionIII-B,weestablish of time-indexed decision epochs, where each t represents
i
the formal underpinnings of enterprise financial processes, theclosureofafinancialreportingcycle.Atthecoreofour
193236 VOLUME13,2025

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
TABLE1. Glossaryofkeyaccountingterms.
formulationisthemodelingofanenterprise’sfinancialstate
asastructuredtupleoveratime-varyingdomain.
|                  | Wedefinethefinancialstateattimet |     |                  |         | as,               |         |     |     |     |     |     |     |     |     |     |
| ---------------- | -------------------------------- | --- | ---------------- | ------- | ----------------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                  |                                  |     | =(A ,L           | ,R ,C   | ,E ),             |         |     |     |     |     |     |     |     |     |     |
|                  |                                  | S   | t t              | t t     | t t               |         | (1) |     |     |     |     |     |     |     |     |
| where            | A denotes                        | the | asset            | vector, | L the liability   | vector, | R   |     |     |     |     |     |     |     |     |
|                  | t                                |     |                  |         | t                 |         | t   |     |     |     |     |     |     |     |     |
| therevenueflow,C |                                  |     | thecostflow,andE |         | theequityposition |         |     |     |     |     |     |     |     |     |     |
|                  |                                  |     | t                |         | t                 |         |     |     |     |     |     |     |     |     |     |
attimet.
|     | To reflect | financial | operations, |     | we define | the net | cash |     |     |     |     |     |     |     |     |
| --- | ---------- | --------- | ----------- | --- | --------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
transformationoperatorandliquidityevolutionas,
|        |                                       |     |    |     |      |      |     |     |     |     |     |     |     |     |     |
| ------ | ------------------------------------- | --- | --- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|        |                                       |     | n   |     | m     |      |     |     |     |     |     |     |     |     |     |
|        |                                       |     | X   | i)− | X (j) |      |     |     |     |     |     |     |     |     |     |
|        | LQ                                    | =LQ | +   | R ( | C     | −D , | (2) |     |     |     |     |     |     |     |     |
|        | t+1                                   |     | t  | t   | t    | t    |     |     |     |     |     |     |     |     |     |
|        |                                       |     | i=1 |     | j=1   |      |     |     |     |     |     |     |     |     |     |
| whereD | t representsdebtservicingobligations. |     |     |     |       |      |     |     |     |     |     |     |     |     |     |
TheintertemporalobjectiveofEFMintegratesdiscounted
utilityoffinancialstrategies,
|     |     |     | " T |     | #   |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
X
|     |     |     | =E  | γtU(S | ,U ,  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | J   |     |       | t t ) |     | (3) |     |     |     |     |     |     |     |     |
t=1
|     | isautilityfunction,andγ |     |     |     | ∈ (0,1)isthediscount |     |     |     |     |     |     |     |     |     |     |
| --- | ----------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whereU
factor.
Weimposeregulatorycomplianceviaconstraintfunctions, FIGURE1. High-levelarchitectureofFinGraphNet.Theprocessbegins
withrawaccountingdata,whichistransformedintoatime-varying
(ℓ) f i n a n c i a l g r a p h s tr u ct u re . D y n am i c g ra p h e n c o d i n g c o m p u t e s
|     | C   | : gℓ(S | ,U )≤0, |     | ℓ=1,...,L, |     | (4) |     |     |     |     |     |     |     |     |
| --- | --- | ------ | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t t t c o n t e x t u a l iz e d n o d e a n d e d g e re p re s e n ta ti o n s ( E q u a t io n s 3 – 7).These
representationsarepropagatedthroughatemporal-awaremessage
capturing rules on debt ratios, coverage thresholds, and passingmechanismwithattention(Equations8–10),followedby
financialmemoryupdatesviarecurrentandsmoothinglayers
exposurelimits.
(Equations11–13).Aconstraint-awareprojectionlayerensuresregulatory
The planning objective is to determine optimal decisions feasibility(Equations14–16),andtheoutputscoresareusedtoguide
| {U  | }T  |     |     |     |     |     |     | reinforcementplanning(Equations17–18). |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
t t=1 overafeasibleset,
C(ℓ)
maxJ subjectto andfiscalconstraints. (5) 1) DYNAMICGRAPHENCODING
t
{Ut } Let V = {v ( t),v ( t),...,v ( t)} denote the set of financial
|     |     |     |     |     |     |     |     |          | t       | 1 2      | n    |      |            |             |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | -------- | ---- | ---- | ---------- | ----------- | --- |
|     |     |     |     |     |     |     |     | entities | at time | t, where | each | node | represents | a financial |     |
C. FINGRAPHNET
item(AsshowninFigure2).
WeintroduceFinGraphNet,astructuredgraph-basedmodel Each node v (t) is associated with a multivariate feature
i
| tailoredtoenterprisefinancialmanagement,whichintegrates |     |     |     |     |     |     |     |        | (t) |                   |     |      |      |          |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------------- | --- | ---- | ---- | -------- | --- |
|                                                         |     |     |     |     |     |     |     | vector | x   | ∈ Rd, constructed |     | from | both | temporal | and |
i
multivariate temporal data, fiscal structure semantics, and structuralattributes,
| regulatory |     | logic into | a unified |     | learning and | reasoning |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --------- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|            |     |            |           |     |              |           |     |     |     |     | h   |     |     | i   |     |
framework. The model treats financial entities and their x (t) =φ(v (t) )= hist (t),sector,risk,flow (t) , (6)
|              |     |          |     |       |               |          |     |     | i   | i   | i   | i   | i   | i   |     |
| ------------ | --- | -------- | --- | ----- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| interactions |     | as nodes | and | edges | in a dynamic, | directed |     |     |     |     |     |     |     |     |     |
multigraphG = (V ,E )ateachtimestept ∈ T(Asshown where hist (t) captures trailing time-series indicators, sector
|     |     | t   | t t |     |     |     |     |     | i   |     |     |     |     |     | i   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
inFigure1). encodes the hierarchical role of the node, risk i represents
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 193237 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
This dynamic encoding enables the formation of time-
varyingmultigraphsthatevolvewithfiscalsignals,allowing
downstream models to access structurally enriched, tempo-
rallygroundedfinancialrepresentations.
2) TEMPORAL-AWAREPROPAGATION
FinGraphNetpropagatesinformationacrossfinancialgraphs
throughatemporallycontextualized,relation-awaremessage
passing mechanism that enables both short- and long-range
(t)
dependency modeling. Each node v aggregates messages
i
fromitslocalneighborhoodN(i)usinganattention-weighted
scheme,
FIGURE2. Detailedviewofthedynamicgraphencoder.Thisfigureshows
howrawfinancialentitiesaretransformedintographrepresentations.  
N hi o e d ra e rc e h m y b ,r e i d sk di w ng e s ig a h r t e s, c a o n n d st c ru a c s t h ed flo u w si s n ( g E h q i u s a to ti r o ic n a 3 l ) t . re E n d d g s e , f s e e a c t t u o r r es h ( i t+1) =σ  X α i ( j t) W i ( j t) h ( j t)+Ux i (t)+b i , (12)
encodedirectionalrelationshipsusingtransformationmatrices,semantic j∈N(i)
relations,andelasticity(Equation5).Bilateraledgeconstraints
(Equation7)maintainconsistencyinpairwiserelations. whereh (t) istheprevioushiddenstateofneighborv,W (t) is
j j ij
(t) theedge-type-specifictransformationmatrix,Uisalearnable
systemic exposure weights, and flow quantifies net cash
i linearprojectionappliedtothecurrentnode’sfeatures,b is
movementduringthecurrentepoch. i
abiasterm,andσ isanonlinearactivationsuchasReLUor
We define the normalized node degree as an auxiliary
GELU.
regularizer,
Theattentioncoefficientα(t)
reflectstherelevanceofeach
ij
d (t) = 1 X ∥flow (t)∥ , (7) neighbor v j to v i at time t, jointly considering structural
i |N i | ij 1 relationembeddingsandlatentnodestates,
j∈Ni
α(t)
where N is the neighborhood of v (t) and flow (t) represents ij
i i ij (cid:16) (cid:17)
directedcashflowmagnitudebetweenv i andv j . exp a⊤tanh(W q h ( i t)+W k h ( j t)+W r r ij +W f f i ( j t) )
tio T ns h h e ip ed s g b e et s w et e E e t n = fin { a ( n v ( i c t i ) a → lno v d ( j t e ) s , , e c ( ij t a ) p )} tu m ri o n d g e c ls re d d i i r t e t c r t a e n d s r f e e l r a s - , = P k∈N(i) exp (cid:16) a⊤tanh(W q h ( i t)+W k h ( k t)+W r r ik +W f f i ( k t) ) (cid:17) ,
investmentdependencies,orregulatorytransfers.Eachedge (13)
embedding includes a transformation matrix W (t) ∈ Rd×d
ij where f (t) is a flow-contextual edge feature such as recent
andasemanticrelationvectorr ∈Rk, ij
ij transaction activity or cumulative volume, and W its
f
h i
e (t) =ψ(v (t),v (t) )= W (t),r ,λ(t) , (8) transformationmatrix.Thisattentionintegratessemanticand
ij i j ij ij ij
quantitativerelationawareness.
where λ(t) is a learned scalar denoting the elasticity of the To incorporate temporal continuity, FinGraphNet models
ij
financialinteractionunderstressscenarios. the evolution of hidden states with a gated recurrent
To enforce directed consistency, we introduce a bilateral mechanism,
edgeconstraint, s (t+1) =GRU(h (t+1),s (t) ), (14)
i i i
ψ(v (t),v (t) )+ψ(v (t),v (t) )≈I(t), (9) (t)
i j j i ij where s is a time-evolving latent vector that encodes
i
where I(t) denotes an identity-preserving neutral transfer financialmemoryofaccountv i .Itcapturesbothlatentbehav-
ij ioral drift and transaction periodicity, enabling recurrent
operator,facilitatingantisymmetricbalanceencoding.
aggregationofcontextualtrends.
The inter-temporal continuity of financial behavior is
Weintroduceatemporalsmoothingmechanismtomitigate
capturedusingadecay-regularizedupdateofnodefeatures,
abrupttransitionsandamplifystabledynamics,
x i (t) =γx i (t−1)+(1−γ)·φ(v ( i t) ), (10) s¯(t+1) =βs (t+1)+(1−β)·s¯(t), (15)
i i i
withdecaycoefficientγ ∈ (0,1)controllingthememoryof
where s¯(t) is the smoothed state vector and β ∈ (0,1)
historicalfeaturedynamics. i
is a smoothing coefficient. This representation is used
Toenhancestructuralgranularity,wegenerateacomposite
fordownstreamdecisionmodulesrequiringtrend-consistent
edgestrengthmetricacrossrelationtypes,
features.
k By layering multiple propagation and recurrent units
ζ i ( j t) = X ω τ ·r i ( j τ), (11) across epochs, the model builds hierarchical node embed-
τ=1 dings that are responsive to evolving fiscal conditions and
whereω τ aretrainableweightsforeachrelationdimensionτ. inter-entitydependencies.
193238 VOLUME13,2025

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
3) CONSTRAINT-AWAREOPTIMIZATION D. AUDIT-INFORMEDREINFORCEMENTPLANNING
| Toensurethatpredictedfinancialflowsadheretoregulatory |     |     |     |     |     |     |     | (AIRP) |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
constraints, we formulate the problem as a constrained To operationalize the predictive insights of FinGraphNet
projectiontask.Givenapredictedflowvectorx˜(t+1)thatmay into adaptive fiscal decision-making, we propose a novel
violate constraints, our goal is to find the closest feasible strategymodulenamedAudit-InformedReinforcementPlan-
flowvectorxˆ(t+1)withintheadmissibleregionF definedby ning (AIRP). This mechanism integrates historical audit
linearinequalities.Thisisformallyexpressedasaquadratic data and compliance records into a reinforcement learning
optimizationproblem.First,wedefinethefeasibleregionas: (RL) framework, enabling strategic financial control under
|       |     |      | n           |          | o        |             |      | constraintsanduncertainty(AsshowninFigure3). |     |     |     |     |     |     |     |
| ----- | --- | ---- | ----------- | -------- | -------- | ----------- | ---- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|       |     |      | ∈Rd         |          | ,        |             |      |                                              |     |     |     |     |     |     |     |
|       |     | F    | = x         | |Gx      | ≤h       |             | (16) |                                              |     |     |     |     |     |     |     |
| where | G ∈ | RL×d | is a matrix | encoding | L linear | constraints |      |                                              |     |     |     |     |     |     |     |
(e.g.,budgetceilings,debtcoverageratios),andh∈RListhe
correspondingthresholdvector.Then,tofindtheclosestpoint
withinF totheunconstrainedpredictionx˜(t+1),wesolvethe
followingoptimizationproblem:
|     |     | xˆ(t+1) | =argmin∥x−x˜(t+1)∥2. |     |     |     | (17) |     |     |     |     |     |     |     |     |
| --- | --- | ------- | -------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
2
x∈F
| This | problem | minimizes |     | the squared | Euclidean |     | distance |     |     |     |     |     |     |     |     |
| ---- | ------- | --------- | --- | ----------- | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
betweentheoriginalpredictionandthefeasiblepoint,subject
| to linear   | inequality |      | constraints. | It    | is a standard | Quadratic |        |     |     |     |     |     |     |     |     |
| ----------- | ---------- | ---- | ------------ | ----- | ------------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Programming |            | (QP) | problem,     | which | is convex     | and       | can be |     |     |     |     |     |     |     |     |
solvedefficientlyusingprojectionmethodsorQPsolvers.
| To  | respect | financial | regulations |     | and policy | constraints, |     |     |     |     |     |     |     |     |     |
| --- | ------- | --------- | ----------- | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
weintroduceaconstraint-satisfactionprojectionlayer.Given
predictedflowsx˜(t+1),weenforcefeasibilityvia,
|     |     | xˆ(t+1) | =argmin∥x−x˜(t+1)∥2, |     |     |     | (18) |     |     |     |     |     |     |     |     |
| --- | --- | ------- | -------------------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
2
x∈F
| where     | F = | {x |Gx     | ≤h} | encodes | budget       | limits,    | liquidity |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | ------- | ------------ | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| reserves, | and | compliance |     | bounds  | using matrix | inequality |           |     |     |     |     |     |     |     |     |
representations.
Toevaluateandprioritizefinancialstrategies,wedefinea
scoringfunction,
|     |     | Score(v | (t) )=ρ⊤ | s (t)−κ⊤ξ(t), |     |     | (19) |          |                                                      |     |     |     |     |     |     |
| --- | --- | ------- | -------- | ------------- | --- | --- | ---- | -------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|     |     |         | i        | i             | i   |     |      |          |                                                      |     |     |     |     |     |     |
|     |     |         |          |               |     |     |      | FIGURE3. | Audit-InformedReinforcementPlanning(AIRP)module.This |     |     |     |     |     |     |
arelearnablerisk/rewardweights,andξ(t)
whereρandκ isa figuredetailstheAIRPmechanism,whereFinGraphNetembeddingsare
i
usedtogeneratecandidatefinancialactions.Theseactionsarechecked
vectorofestimatedexposuremetrics. againstaudit-informedconstraints(Equation24)andprojectedintoa
The model is trained on historical transaction data with feasiblesetviaquadraticprogramming(Equation25).Auditconformity
supervisory signals such as future cash position L ˆ Q and a n d s la c k l o s se s ( E q u a t io n s 2 6 – 2 7 ) a re in t eg r a te d in t o t h e fi n a l p o l ic y
|     |     |     |     |     |     |     | t+τ | lo s s (E q u a | t io n 2 9 ) | , e n a b li n | g c o m p l ia | n ta n d a d a | p tiv e d e | c is io n - m | a k i n g . |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------ | -------------- | -------------- | -------------- | ----------- | ------------- | ----------- |
ˆ
| realizedvaluecreationE |           |              | t+τ, |                   |                |      |              |     |     |     |     |     |     |     |     |
| ---------------------- | --------- | ------------ | ---- | ----------------- | -------------- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|                        | X(cid:13) | ˆ            |      | p re d (cid:13) 2 | (cid:13) ˆ     | p re | d (cid:13) 2 |     |     |     |     |     |     |     |     |
| L                      | =         | (cid:13) L Q | −LQ  | (cid:13) +η       | (cid:13) E t+τ | −E   | (cid:13) ,   |     |     |     |     |     |     |     |     |
reg (cid:13) t+τ t+ τ (cid:13) (cid:13) t + τ (cid:13) 1) CONSTRAINT-AWAREMDPFORMULATION
|     |     |     |     | 2   |     |     | 2   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
t
|     |     |     |     |     |     |     | (20) | WemodelthedecisionenvironmentasaconstrainedMarkov |         |       |     |                       |     |     |          |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------- | ------- | ----- | --- | --------------------- | --- | --- | -------- |
|     |     |     |     |     |     |     |      | Decision                                          | Process | (MDP) | M   | = (S,A,T,R,(cid:48)), |     |     | tailored |
whereηbalancesliquidityversusequitytracking.
|     |     |     |     |     |     |     |     | to financial | planning |     | under | structural, | regulatory, |     | and risk- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ----- | ----------- | ----------- | --- | --------- |
Wepenalizeconstraintviolationsusingahinge-likeloss,
|     |     |     |     |                      |     |     |      | aware constraints. |            | The | state  | space     | S consists |              | of latent |
| --- | --- | --- | --- | -------------------- | --- | --- | ---- | ------------------ | ---------- | --- | ------ | --------- | ---------- | ------------ | --------- |
|     |     |     | L   |                      |     |     |      | financial          | embeddings |     | s ∈ Rd | generated | by         | FinGraphNet, |           |
|     |     |     | X   |                      |     |     |      |                    |            |     | t      |           |            |              |           |
|     |     | L   | =   | max(0,gℓ(xˆ(t+1)))2. |     |     | (21) |                    |            |     |        |           |            |              |           |
cons capturing the evolving economic posture of an enterprise.
|     |               |     | ℓ=1       |            |            |     |          | TheactionspaceAcontainsfiscalactionssuchasallocation |         |     |       |       |         |            |     |
| --- | ------------- | --- | --------- | ---------- | ---------- | --- | -------- | ---------------------------------------------------- | ------- | --- | ----- | ----- | ------- | ---------- | --- |
|     |               |     |           |            |            |     |          | strategies,                                          | denoted | A   | ∈ Rm, | which | include | investment |     |
| The | full training |     | objective | integrates | prediction |     | accuracy |                                                      |         |     | t     |       |         |            |     |
andconstraintadherence, proportions,debtrepayments,andliquiditybuffers(Asshown
inFigure4).
|                                |                  |         | =L        | +λL        | +µ∥(cid:50)∥2, |         |      |                                                       |     |     |       |       |     |     |        |
| ------------------------------ | ---------------- | ------- | --------- | ---------- | -------------- | ------- | ---- | ----------------------------------------------------- | --- | --- | ----- | ----- | --- | --- | ------ |
|                                |                  | L total | reg       | cons       |                |         | (22) |                                                       |     |     |       |       |     |     |        |
|                                |                  |         |           |            |                | 2       |      | Statetransitionsfollowparameterizedfinancialdynamics, |     |     |       |       |     |     |        |
| where                          | (cid:50) denotes |         | all model | parameters |                | and λ,µ | are  |                                                       |     |     |       |       |     |     |        |
|                                |                  |         |           |            |                |         |      |                                                       |     | s   | =fφ(s | ,A ,ω | ),  |     | (23)   |
| regularizationhyperparameters. |                  |         |           |            |                |         |      |                                                       |     | t+1 |       | t t   | t   |     |        |
| VOLUME13,2025                  |                  |         |           |            |                |         |      |                                                       |     |     |       |       |     |     | 193239 |

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
Constraintviolationisfurtherformalizedasasoftpenalty
function,
L
|     |     |     |     |     |     |     |     |     |     |           | X   | max(0,c | ⊤   | −dℓ)2, |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------- | --- | ------ | ---- |
|     |     |     |     |     |     |     |     |     |     | Violation | =   |         | ℓ A |        | (26) |
|     |     |     |     |     |     |     |     |     |     |           | t   |         | t   |        |      |
ℓ=1
|     |     |     |     |     |     |     |     | where(cℓ |     | ,dℓ)encodestheℓ-thlinearinequalityderivedfrom |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
auditrulesorinternalcontrolpolicies.
|     |     |     |     |     |     |     |     |     | To ensure | conservative | fiscal | behavior |     | under uncertainty, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------ | -------- | --- | ------------------ | --- |
weaugmenttherewardwithadownsideriskterm,
|     |     |     |     |     |     |     |     |       |          |        | h            |         |        | i                |      |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ------ | ------------ | ------- | ------ | ---------------- | ---- |
|     |     |     |     |     |     |     |     |       |          |        | =E           | ∥s −E[s |        | ]∥2 ,            |      |
|     |     |     |     |     |     |     |     |       |          | Risk t | ω            | t+1     | t+1    |                  | (27) |
|     |     |     |     |     |     |     |     |       |          |        | t            |         |        | 2                |      |
|     |     |     |     |     |     |     |     | which | captures | the    | second-order |         | moment | of the predicted |      |
state,penalizingvolatiletrajectories.
|     |     |     |     |     |     |     |     |     | The admissible |     | action set | (cid:48) (s ) | is dynamically |     | extracted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ------------- | -------------- | --- | --------- |
t t
|     |     |     |     |     |     |     |     | from | compliance |     | records, | ensuring | that | policy generation |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | --- | -------- | -------- | ---- | ----------------- | --- |
remainsinalignmentwithlegalandstrategicboundaries,
|     |     |     |     |     |     |     |     |     |     | )=(cid:8)   |     |        |      | (cid:9), |      |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | ---- | -------- | ---- |
|     |     |     |     |     |     |     |     |     |     | (cid:48) (s | A   | ∈Rm |G | A ≤h |          | (28) |
|     |     |     |     |     |     |     |     |     |     | t t         | t   |        | t t  | t        |      |
,h
|     |     |     |     |     |     |     |     | where | (G  | ) represents |     | time-indexed | constraint |     | matrices, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ------------ | --- | ------------ | ---------- | --- | --------- |
|     |     |     |     |     |     |     |     |       |     | t t          |     |              |            |     |           |
derivedfrompastauditdocumentsandrisksimulations.
|     |     |     |     |     |     |     |     | 2)  | AUDIT-GUIDEDACTIONPROJECTION |        |                 |     |         |               |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | ------ | --------------- | --- | ------- | ------------- | --- |
|     |     |     |     |     |     |     |     | To  | ensure                       | fiscal | decision-making |     | adheres | to regulatory |     |
FIGURE4. Constraint-AwareMDPCellwithinAIRP.Thisdiagramoutlines and historical compliance patterns, we incorporate audit-
asingledecisionstepintheMDPformulationofAIRP.Acandidateaction informed constraints into the policy execution phase. His-
issampledfromthecurrentpolicyandevaluatedthrougha
constraint-awaretransitionfunction(Equation21).Therewardis torical audit logs A are mined using pattern extraction
log
computedbyincorporatingauditviolationsanddownsiderisk algorithms and domain templates to derive interpretable
(Equations23–27),andthepolicyisupdatedusingatrust-regionmethod
(Equation29)toensurestableoptimization. linearconstraintsthatformalizefinancialcontrolboundaries.
|     |     |     |     |     |     |     |     | The | extracted | set of | admissible | actions | at  | time t is | denoted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ | ---------- | ------- | --- | --------- | ------- |
as,
| wherefφisadifferentiabletransitionfunction,andω |     |     |     |     |     |     | denotes |          |     |       |         |       |       |            |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ----- | ------- | ----- | ----- | ---------- | --- |
|                                                 |     |     |     |     |     | t   |         |          | n   |       |         |       | o     |            |     |
|                                                 |     |     |     |     |     |     |         | (cid:48) | =   | A ∈Rm | |∀ℓ:c ⊤ | A ≤dℓ | , (cℓ | ,dℓ)∈Audit | ,   |
stochastic exogenous shocks, such as inflation, tax policy t t ℓ t t
| shifts,ordemandvolatility. |     |     |     |         |     |     |     |     |     |     |     |     |     |     | (29) |
| -------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
|                            |     |     | π   | θ(A | s |     |     |     |     |     |     |     |     |     |     |      |
The stochastic policy t t ) maps financial states ,dℓ)representsaconstraintinducedfromaudit
whereeach(cℓ
| to  | action | distributions | and | is optimized | to  | maximize | the |     |     |     |     |     |     |     |     |
| --- | ------ | ------------- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
triggerssuchasoverspendingoncapital,excessiveleverage,
expecteddiscountedcumulativereward,
orunderfundingofreserves.
|     |     |     | "   |     | #   |     |     |     | GivenanactionproposalA |     |     | sampledfromthepolicyπ |     |     | θ,  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --------------------- | --- | --- | --- |
|     |     |     |     | T   |     |     |     |     |                        |     |     | t                     |     |     |     |
X i t is n ot dir ec t ly e x ec u t e d b u t p r o j e c te d b a ckintothefeasible
|     |     | J(θ)=E | πθ  | γtR(s | ,A ) , |     | (24) |      |          |               |              |                |              |     |     |
| --- | --- | ------ | --- | ----- | ------ | --- | ---- | ---- | -------- | ------------- | ------------ | -------------- | ------------ | --- | --- |
|     |     |        |     | t     | t      |     |      |      | (cid:48) |               |              |                |              |     |     |
|     |     |        |     |       |        |     |      | r eg | io n t   | to e n su r e | c o n s tr a | in t s a t i s | fa c tio n , |     |     |
t=1
|     |     |     |     |     |          |     |          |     |     | ˜   | =argmin∥A−A |     | ∥2, |     |      |
| --- | --- | --- | --- | --- | -------- | --- | -------- | --- | --- | --- | ----------- | --- | --- | --- | ---- |
|     |     |     |     |     | (cid:48) |     | (cid:48) |     |     | A   | t           |     | t   |     | (30) |
subject to the feasibility constraint A t ∈ t (s t ), where t 2
A∈(cid:48) t
| denotes | the | admissible | action | space derived | from | historical |     |     |     |     |     |     |     |     |     |
| ------- | --- | ---------- | ------ | ------------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
whichisaquadraticprogramsolvableinclosed-formorvia
auditconstraintsandstructuralfiscalrules.
|       |             |          |            |                   |          |     |        | projected  |     | gradient | descent, | depending | on  | the complexity | of  |
| ----- | ----------- | -------- | ---------- | ----------------- | -------- | --- | ------ | ---------- | --- | -------- | -------- | --------- | --- | -------------- | --- |
|       | The reward  | function | is         | shaped to reflect | multiple |     | enter- |            |     |          |          |           |     |                |     |
|       |             |          |            |                   |          |     |        | (cid:48) . |     |          |          |           |     |                |     |
| prise | performance |          | indicators | and penalize      | risk     | and | non-   | t          |     |          |          |           |     |                |     |
Tooperationalizesoftconstraintadherenceduringtraining,
compliance,
|     |         |     |      |          |     |            |        | we                                          | define | an audit-conformity |     |                 | regularization | loss      | that |
| --- | ------- | --- | ---- | -------- | --- | ---------- | ------ | ------------------------------------------- | ------ | ------------------- | --- | --------------- | -------------- | --------- | ---- |
|     | ,A      |     |      |          |     |            |        | penalizesdeviationsfromcriticalhyperplanes, |        |                     |     |                 |                |           |      |
|     | R(s t   | t ) |      |          |     |            |        |                                             |        |                     |     |                 |                |           |      |
|     | =ν ·ROE | +ν  | ·LCR | −ν ·Risk | −ν  | ·Violation | ,      |                                             |        |                     | Lt  |                 |                |           |      |
|     | 1       | t   | 2    | t 3      | t 4 |            | t      |                                             |        |                     | XX  |                 |                |           |      |
|     |         |     |      |          |     |            |        |                                             |        | L =                 |     | max(0,(cid:49)⊤ | A              | −b t,ℓ)2, | (31) |
|     |         |     |      |          |     |            | ( 2 5) |                                             |        | audit               |     |                 | t,ℓ t          |           |      |
t ℓ=1
|     |     |     |     |     |     |     |     |     | ((cid:49) | ,b  |     | ℓ-th |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | ---- | --- | --- | --- |
wherereturnonequity(ROE),liquiditycoverageratio(LCR), where t,ℓ t,ℓ) denotes the regulatory hyperplane
and constraint violations are computed from both predicted at time t, reflecting either statutory thresholds or internal
cashflowmodelsandreal-timeregulatoryassessments. compliancemetricsextractedfromflaggedentriesinA log .
| 193240 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
Furthermore, to allow dynamic flexibility while retaining particularly valuable for personal finance management and
auditawareness,wedefineasoft-boundrelaxationpenalty, consumerbehavioranalysis.Itencompassesbothstructured
|     |     |     |     |     |     |     |     | and unstructured | information—such |     |     | as timestamps, |     | vendor |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------------- | --- | --- | -------------- | --- | ------ |
Lt
XX (cid:49)⊤ names,transactionmodes,andcategoricallabels—enablinga
| L   | =     |     | ξ 2 , | s.t. | A ≤b  | t,ℓ+ξ t,ℓ | , (32) |     |     |     |     |     |     |     |
| --- | ----- | --- | ----- | ---- | ----- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
|     | slack |     | t ,ℓ  |      | t,ℓ t |           |        |     |     |     |     |     |     |     |
widerangeofapplicationsincludingclassification,sequence
t ℓ=1
modeling,andrecommendationsystemsinreal-worldfinan-
| where      | ξ represents |     | slack | variables    | that         | permit | bounded |                                                         |     |     |     |     |     |     |
| ---------- | ------------ | --- | ----- | ------------ | ------------ | ------ | ------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            | t,ℓ          |     |       |              |              |        |         | cialscenarios.TheOrbisdataset[31]consistsofquarterlyand |     |     |     |     |     |     |
| constraint | violations   |     | for   | optimization | flexibility, |        | and are |                                                         |     |     |     |     |     |     |
annualcorporaterevenuedataacrossavarietyofindustries.
regularizedtoremainsmall.
Itincludescomplementaryfeaturessuchasmarketingexpen-
| To  | unify constraint |     | projection |     | and learning, | the | adjusted |     |     |     |     |     |     |     |
| --- | ---------------- | --- | ---------- | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
diture,productlaunches,andindustrytrends,supportinguse
| action | is incorporated |     | into | the | actor update | via | a dual |          |               |         |              |     |            |     |
| ------ | --------------- | --- | ---- | --- | ------------ | --- | ------ | -------- | ------------- | ------- | ------------ | --- | ---------- | --- |
|        |                 |     |      |     |              |     |        | cases in | benchmarking, | revenue | forecasting, |     | and return | on  |
objective,
investment(ROI)analysis.Theinclusionofmacroeconomic
|     |     | (cid:13) | (cid:13) |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
˜ 2 indicators like interest rates and GDP enhances its utility
|     | L = | (cid:13)A −A | (cid:13) | +α·L | +β·L | ,   | (33) |     |     |     |     |     |     |     |
| --- | --- | ------------ | -------- | ---- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
proj (cid:13) t t(cid:13) audit slack for correlation and impact studies. Notably, the data is
2
where α and β are tunable weights balancing hard and normalized across fiscal calendars, promoting consistency
soft regulatory conformance. This enables reinforcement incomparativeanalytics.TheCSMARdataset[27]contains
|            |     |        |           |       |            |            |     | monthly-level | financial | records | detailing | cash | inflows | and |
| ---------- | --- | ------ | --------- | ----- | ---------- | ---------- | --- | ------------- | --------- | ------- | --------- | ---- | ------- | --- |
| strategies | to  | remain | proactive | while | respecting | compliance |     |               |           |         |           |      |         |     |
boundariesthroughoutlearningandexecution. outflowsfromoperational,investing,andfinancingactivities
offirmsvaryinginsizeandgeography.Itispurpose-builtfor
studiesonliquiditymanagement,bankruptcyriskprediction,
3) RISK-DRIVENPOLICYLEARNING
|     |     |     |     |     |     |     |     | and working | capital | optimization. | Annotated |     | with financial |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ------------- | --------- | --- | -------------- | --- |
Weestimatefinancialvolatilityviaconditionalvariance,
|     |     |      |         |     |           |     |      | events—such | as credit | line | changes | or tax | deadlines—the |     |
| --- | --- | ---- | ------- | --- | --------- | --- | ---- | ----------- | --------- | ---- | ------- | ------ | ------------- | --- |
|     |     | Risk | =Tr(V[S |     | |s ,A ]), |     | (34) |             |           |      |         |        |               |     |
t t+1 t t dataset enables deeper temporal modeling and causality
analysisincorporatefinanceresearch.
usingempiricalbootstrappingoverFinGraphNetpredictions.
C
| AIRP | includes | a   | counterfactual |     | simulator | estimating |     |                        |     |     |     |     |     |     |
| ---- | -------- | --- | -------------- | --- | --------- | ---------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
|      |          |     |                |     |           |            |     | B. EXPERIMENTALDETAILS |     |     |     |     |     |     |
alternatefiscalpaths,
|     |     |     |        |     |        |     |     | All experiments | are | conducted | using | PyTorch | on NVIDIA |     |
| --- | --- | --- | ------ | --- | ------ | --- | --- | --------------- | --- | --------- | ----- | ------- | --------- | --- |
|     |     | sˆc | f =C(s | ,Aa | lt,τ), |     |     |                 |     |           |       |         |           |     |
t+ τ t (35) A100 GPUs. We adopt the Adam optimizer with a learning
t
|     |     |     |     |     |     |     |     | rate of | 1e-4 and apply | a   | cosine annealing |     | schedule | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | ---------------- | --- | -------- | --- |
usedtoevaluatehypotheticaldecisionsunderhistoricalstress
dynamicadjustment.Batchsizeisfixedat64foralldatasets
scenarios.
toensureconsistency.Fortrainingstability,weemploygradi-
Weadoptatrust-regionmethodforrobustlearning,
entclippingwithathresholdof1.0andusemixed-precision
←argmaxJ(θ′
θ )−η·KL(π θ′ ∥π θ), (36) training via AMP. Dropout with a rate of 0.1 is applied in
θ′ all feedforward and attention layers to mitigate overfitting.
whereηcontrolsthestepsizeinpolicyspace. Models are trained for 100 epochs with early stopping
Thefulltraininglossincorporatesstrategicutility,risk,and based on validation loss to prevent overfitting. We employ
|     |     |     |     |     |     |     |     | a standard | train/validation/test |     | split | of 70%/15%/15% |     | for |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------- | --- | ----- | -------------- | --- | --- |
auditalignment,
|     |     |            |     |     |           |     |      | all datasets. | For temporal |     | datasets such | as  | Compustat | and |
| --- | --- | ---------- | --- | --- | --------- | --- | ---- | ------------- | ------------ | --- | ------------- | --- | --------- | --- |
|     | L   | =−J(θ)+α·L |     |     | +β·E[Risk | ],  | (37) |               |              |     |               |     |           |     |
total audit t CSMAR, we strictly follow chronological order to avoid
|          |                                         |     |     |     |     |     |     | data leakage. | Input | sequences | of length | 12  | (corresponding |     |
| -------- | --------------------------------------- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --------- | --------- | --- | -------------- | --- |
| whereα,β | weightregulatoryandstabilitycomponents. |     |     |     |     |     |     |               |       |           |           |     |                |     |
to12monthsorquarters,dependingonthedataset)areused
IV. EXPERIMENTALSETUP topredictthenextstep.Forsequencemodeling,weadopta
A. DATASET Transformer-basedarchitecturewithfourencoderlayersand
The Compustat dataset [29] provides comprehensive time- amodeldimensionof256.Positionalencodingsarelearned
series financial data, emphasizing projected budgets across ratherthanfixedtoaccommodatevariable-lengthsequences.
departments. It facilitates the study of long-term fiscal Layer normalization is applied after each sublayer, and
planning and inter-departmental resource allocation. With residualconnectionsaremaintainedthroughoutthenetwork.
quarterly forecasts, historical expenditures, and relevant Multi-head attention uses 8 heads with dimensionality
economic indicators, the dataset captures fluctuations in 32each.ForclassificationtaskswithintheEDGARdataset,
budgetestimationsdrivenbypolicyshiftsormacroeconomic weconvertthetaskintoamulti-classsettingwhereeachclass
conditions.Itiswell-suitedfortaskssuchastemporalmod- corresponds to a transaction category. Cross-entropy loss is
eling,budgetanomalydetection,andmultivariateregression, used as the objective function. In contrast, for regression
and includes metadata like region, sector, and reporting tasks such as revenue or budget forecasting, we employ
authority for enriched contextual analysis. The EDGAR MeanSquaredError(MSE)loss.MeanAbsolutePercentage
dataset[30]offersdaily-levelfinancialtransactiondataacross Error (MAPE) and Root Mean Square Error (RMSE) are
diverse user profiles and spending categories, making it reportedforcomprehensiveevaluation.Allhyperparameters
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 193241 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
TABLE2. Evaluationofourmethodincontrastwithcurrentbest-performingapproachesontheCompustatandEDGARdatasets.
TABLE3. Comparativestudyofourapproachandtop-performingmethodsontheOrbisandCSMARdatasets.
are selected based on a combination of grid search and andthecoefficientofdetermination(R2).Acrossalldatasets
prior work from top-tier conferences such as NeurIPS and metrics, our method consistently outperforms existing
and ICLR. For baseline comparisons, we include classical models, showcasing its robustness and superior forecasting
statistical methods (ARIMA, VAR), traditional machine accuracy. on the Compustat dataset, our model achieves the
learningapproaches(RandomForest,XGBoost),andrecent lowestMAEof9.84,outperformingInformerandN-BEATS
deep learning models (LSTM, GRU, Transformer). Each by a significant margin. In parallel, our approach attains
baseline is carefully tuned to achieve its best performance a 7.29 MAPE, demonstrating its effectiveness in reducing
under the same data split and evaluation metrics. Data relativepredictionerror,especiallycomparedtomodelslike
preprocessing includes normalization via z-score transfor- Transformer and GRU. Similarly, in the EDGAR dataset,
mation,missingvalueimputationusinglinearinterpolation, our model achieves a high R2 of 0.869, indicating strong
and categorical embedding for all non-numeric metadata. fit and reliability in capturing temporal spending behavior.
Wealsoapplyfeatureselectionusingmutualinformationfor Thissuggestsourmethodgeneralizeswelltobothstructured
datasetswithhigh-dimensionalinputslikeOrbis.Toevaluate fiscalplanningdataandfine-grainedusertransactionrecords.
generalization,weperform5-foldcross-validationandreport Our attention-based sequence aggregation and regularized
theaverageperformance.Allexperimentsarerepeatedwith temporalencodingsofferadvantagesparticularlyincapturing
three different random seeds to ensure robustness, and hierarchical periodicity and suppressing outlier influence—
the variance is reported along with the mean. The entire characteristicscommoninbothgovernmentalandconsumer
pipeline is implemented using reproducible code with fixed financialdata.
seeds, deterministic CUDA settings, and version-controlled In Figure 5, the superiority of our model extends to the
dependencies. Orbis and CSMAR datasets. On Orbis, our model achieves
anMAEof9.96andaR2 of0.896,significantlysurpassing
C. COMPARISONWITHSOTAMETHODS Transformer and Informer. Notably, while models like N-
We conduct a comprehensive comparison between our pro- BEATS and DeepAR perform decently, they struggle to
posedmethodandseveralstate-of-the-art(SOTA)baselines, capture irregular seasonality and external drivers such as
acrossallfourdatasets.TheresultsarepresentedinTable2 macroeconomic volatility. Our method, by incorporating
and Table 3. We evaluate using four standard metrics adaptive feature weighting and recurrent residuals, effec-
including Mean Absolute Error (MAE), Root Mean Square tively models both short-term surges and long-term trends.
Error (RMSE), Mean Absolute Percentage Error (MAPE), In the CSMAR dataset, where periodicity and irregular
193242 VOLUME13,2025

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
FIGURE5. Evaluationofourmethodincontrastwithcurrentbest-performingapproachesontheCompustat
andEDGARdatasets.
VOLUME13,2025 193243

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
FIGURE6. Comparativestudyofourapproachandtop-performingmethodsontheOrbisandCSMARdatasets.
expenditurescoexist,ourmethodachievesthelowestMAPE bias that adapts to seasonal shifts and irregular gaps, giving
of 8.21 and highest R2 of 0.872. This result highlights the us a predictive edge. Moreover, callback to our method’s
model’scapacitytobalanceinflow-outflowvariationswhile contribution —such as adaptive multiscale embedding and
minimizing forecast drift. Moreover, our improvement in noise suppression—explains the robust performance across
RMSE across all datasets—particularly a 13.47 score in dynamicfinancialenvironments.Theseadvantagesculminate
CSMAR—indicates reduced sensitivity to extreme errors, inconsistentSOTAperformanceacrossallfourbenchmarks,
a common pitfall in financial domains. The result affirms validating our architectural innovations and demonstrating
our method’s resilience to variance and its ability to practicalutilityinreal-worldfiscalandfinancialforecasting.
retainmeaningfultemporalfeaturesacrossdifferentbusiness
cycles. These improvements are not trivial fluctuations but
statisticallyrobustgainsconsistentlyacrossfoldsandseeds. D. ABLATIONSTUDY
In Figure 6, to further interpret the performance gain, To validate the effectiveness of each core component of
we analyze the strengths of our model in light of its design our model, we conduct ablation experiments across all
choices and experimental results. Compared to Informer, four datasets. The results are presented in Table 4 and
which benefits from long sequence handling but suffers Table5,whereweanalyzetheimpactofremovingindividual
fromstaticattentionspread,ourmodelappliestime-decaying modules including (Dynamic Graph Encoding) adaptive
dynamic attention that prioritizes recent events while pre- temporal attention, (Temporal-Aware Propagation) multi-
serving historical context via gated residuals. DeepAR and scale feature encoder, and (Risk-Driven Policy Learning)
LSTMoftenfailtogeneralizeinregimeswithabruptchanges regularized residual integration. From the results, it is
or heterogeneous patterns due to their lack of adaptive evidentthateachcomponentcontributessignificantlytothe
reweighting, whereas our model benefits from learnable overall performance. The full model consistently achieves
attention fusion and temporal bias correction modules. The thebestresultsacrossallmetricsanddatasets.Forexample,
advantage is especially evident in datasets like EDGAR, on the Compustat dataset, removing component Dynamic
wheretransactionsequencesarenoisyanddiverse.Thesupe- Graph Encoding leads to a notable degradation in R2
riorityonOrbiscanbeattributedtoourmodel’shierarchical (0.902to0.887)andincreasedMAEandRMSE,highlighting
temporal block that captures quarterly and yearly variations the critical role of our adaptive attention mechanism in
simultaneously.ComparedtoTransformer,whichusesfixed learningdynamictemporaldependencies.Similarly,removal
positionalencodings,ourmodelemployslearnablepositional of Temporal-Aware Propagation or Risk-Driven Policy
193244 VOLUME13,2025

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
TABLE4. EvaluatingmodulecontributionsinourframeworkusingCompustatandEDGARdata.
FIGURE7. EvaluatingmodulecontributionsinourframeworkusingCompustatand
EDGARdata.
Learning leads to increased errors across both Compustat and residual integration are complementary in capturing
and EDGAR datasets, confirming that multi-scale encoding hierarchicalandnoisypatterns.
VOLUME13,2025 193245

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
TABLE5. ComponentevaluationofourframeworkusingOrbisandCSMARdata.
TABLE6. Robustnessevaluationunderhigh-noisescenarios(Gaussian
noiseσ=0.15).
importance of multi-scale modeling in handling varying
temporal granularity common in quarterly financial reports.
Removing component Risk-Driven Policy Learning results
in reduced R2 from 0.896 to 0.884 and increased RMSE
from 14.88 to 15.25, implying that regularized residual
connectionsnotonlystabilizetrainingbutalsocapturelong-
range dependencies that simpler skip connections overlook.
On the CSMAR dataset, each ablation results in consistent
dropsacrossallmetrics.Themodelwithoutadaptiveattention
(w./o.DynamicGraphEncoding)showsthemostsignificant
errorinflation,aligningwiththefactthatcashflowdataoften
contains irregular bursts and lulls, which require adaptive
temporal sensitivity to model accurately. This affirms that
componentDynamicGraphEncodingisparticularlyvitalin
scenarios with non-stationary input sequences and volatile
intervals.
In Figure 8, callback to the design motivations—
component Dynamic Graph Encoding enables temporal
relevance weighting based on learned context, compo-
nent Temporal-Aware Propagation allows our model to
disentangle overlapping temporal patterns through parallel
convolutional encoders, and component Risk-Driven Policy
Learning injects structured memory that preserves high-
level trends without overfitting to short-term noise. These
design choices result in a model that is not only accurate
FIGURE8. ComponentevaluationofourframeworkusingOrbisand but also robust and interpretable across various financial
CSMARdata.
scenarios.Theperformancegapbetweenthefullmodeland
theablatedversionsconfirmsthatthestrengthofourmethod
In Figure 7, the performance drop observed in the liesnotinanysinglemodulebutinthesynergisticintegration
Orbis and CSMAR datasets upon removing components of all three. Together, these components offer complemen-
Dynamic Graph Encoding, Temporal-Aware Propagation, tary benefits including attention provides dynamic focus,
or Risk-Driven Policy Learning further emphasizes the multi-scale encoding improves representation diversity, and
generalizabilityofourdesign.WithoutcomponentTemporal- residualintegrationenhancestemporalcontinuity.Therefore,
Aware Propagation, MAE increases from 9.96 to 10.21 and thefullarchitectureisessentialforachievingstate-of-the-art
MAPE rises from 7.48 to 7.60 on Orbis, indicating the resultsacrossdiverseandcomplexfinancialforecastingtasks.
193246 VOLUME13,2025

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
As shown in Table 6, we evaluate the robustness of accuracy by 12 percentage points and anomaly detection
FinGraphNet and four baseline models under high-noise F1-scoreby15percentagepointscomparedtoconventional
conditions, where Gaussian noise with a standard deviation shallowmodels.Thesefindingshighlighttheefficacyofdeep,
of0.15isaddedtotheinputtransactionfeatures.Theresults automated feature learning in capturing complex patterns
demonstrate that FinGraphNet achieves the lowest MAE within accounting datasets, aligning with the growing trend
(0.832) and RMSE (1.205), while maintaining the highest ofscalable,intelligentfinancialsystems.
R2score(0.781).Incontrast,baselinemodelssuchasLSTM Despite the promising results, our method has several
andGRUexhibitmoresignificantperformancedegradation, limitations.First,theconvolutional-autoencoderarchitecture,
with RMSE values exceeding 1.45 and R2 dropping below while effective, may still struggle with extremely sparse
0.65. These findings suggest that FinGraphNet is more or irregular financial data that lacks sufficient structure
resilient to noise perturbations, likely due to its structure- for convolutional learning. Second, the adversarial training
aware graph encoding and constraint-regularized learning, introducesadditionalcomputationalcomplexityandsensitiv-
which collectively enhance its stability in volatile financial ity to hyperparameter settings, which may hinder real-time
environments. deployment in high-frequency accounting environments.
|     |     |     |     |     |     |     |     | Third, while | our | graph-based | temporal | encoding |     | is advan- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------- | -------- | -------- | --- | --------- |
TABLE7. Sensitivityofmodelperformancetotheconstraintpenalty tageous for modeling long-range dependencies, it involves
weightλ.
pairwiseinteractionswithquadratictimecomplexity(O(n2))
|     |     |     |     |     |     |     |     | in graph | operations. | This | can become |     | a computational |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ---- | ---------- | --- | --------------- | --- |
bottleneckinlarge-scaleenterprisesystems.Fourth,thedeep
architecturemayexhibitoverfittingtendencieswhenapplied
|     |     |     |     |     |     |     |     | to small-scale     |     | or low-diversity | accounting |     | datasets, | limiting   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------------- | ---------- | --- | --------- | ---------- |
|     |     |     |     |     |     |     |     | its generalization |     | capability.      | In future  |     | work,     | we plan to |
explorehybridmodelsthatcombinesymbolicreasoningwith
deeplearningtobetterhandlesparsedatascenarios.Wewill
|              |           |     |      |             |     |                 |     | also investigate |      | efficient         | approximations |        | for graph | message |
| ------------ | --------- | --- | ---- | ----------- | --- | --------------- | --- | ---------------- | ---- | ----------------- | -------------- | ------ | --------- | ------- |
| In practice, | enforcing |     | hard | constraints | in  | a reinforcement |     |                  |      |                   |                |        |           |         |
|              |           |     |      |             |     |                 |     | passing,         | such | as sampling-based | or             | sparse | attention | mecha-  |
learningsettingcanbeproblematicduetotheneedforfeasi-
nisms,toreducegraphoperationoverheadwhilepreserving
bleactionsamplingandpolicygradientstability.Therefore,
we adopt a soft penalty mechanism that incorporates con- modeling capacity. Furthermore, we aim to incorporate
|     |     |     |     |     |     |     |     | regularization |     | techniques | and meta-learning |     |     | strategies to |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ----------------- | --- | --- | ------------- |
straintviolationsintothelossfunctionusingasquaredhinge
mitigateoverfittingrisks,especiallyinlow-resourcesettings.
form.Thisapproachenablesthepolicytolearnnear-feasible
|     |     |     |     |     |     |     |     | Another | promising | direction | is to | leverage | domain-specific |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --------- | ----- | -------- | --------------- | --- |
actionsthatgraduallyalignwithcomplianceboundarieswith-
|     |     |     |     |     |     |     |     | pretraining | on  | large-scale | financial | corpora |     | to improve |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --------- | ------- | --- | ---------- |
outcompletelyeliminatingexploratorybehavior.Tovalidate
this design choice, we conduct a sensitivity analysis on the the robustness and generalization of our framework across
penaltyweightparameterλintheconstraintlosscomponent. diverseaccountingenvironments.
| As shown | in Table | 7,    | we test | values  | ranging | from          | 0.1 to |                             |     |     |     |     |     |     |
| -------- | -------- | ----- | ------- | ------- | ------- | ------------- | ------ | --------------------------- | --- | --- | --- | --- | --- | --- |
| 5.0      |          |       |         |         |         |               |        | CONFLICTOFINTERESTSTATEMENT |     |     |     |     |     |     |
| and      | observe  | their | impact  | on both | reward  | and violation |        |                             |     |     |     |     |     |     |
frequency.Theresultsindicatethatsettingλwithin[1.0,2.0] The author declares that the research was conducted in the
|          |             |                     |     |     |     |           |        | absence | of any | commercial | or financial |     | relationships | that |
| -------- | ----------- | ------------------- | --- | --- | --- | --------- | ------ | ------- | ------ | ---------- | ------------ | --- | ------------- | ---- |
| achieves | a favorable | trade-off—producing |     |     |     | compliant | fiscal |         |        |            |              |     |               |      |
couldbeconstruedasapotentialconflictofinterest.
| actions      | while maintaining |               | strong | performance. |            | In contrast, |        |     |     |     |     |     |     |     |
| ------------ | ----------------- | ------------- | ------ | ------------ | ---------- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| values above | 3.0               | significantly |        | reduce       | violations | but          | at the |     |     |     |     |     |     |     |
costofrewardstagnation,illustratingthediminishingreturn ACKNOWLEDGMENT
|     |     |     |     |     |     |     |     | This is | a short | text to | acknowledge | the | contributions | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------- | ----------- | --- | ------------- | --- |
ofover-penalization.
|                            |          |         |                |         |            |                |        | specific            | colleagues, | institutions, | or  | agencies | that | aided the |
| -------------------------- | -------- | ------- | -------------- | ------- | ---------- | -------------- | ------ | ------------------- | ----------- | ------------- | --- | -------- | ---- | --------- |
| V. CONCLUSIONANDFUTUREWORK |          |         |                |         |            |                |        | effortsoftheauthor. |             |               |     |          |      |           |
| In this study,             | we       | address | the persistent |         | challenges | of             | adapt- |                     |             |               |     |          |      |           |
| ability and                | reliance | on      | manual         | feature | design     | in traditional |        | REFERENCES          |             |               |     |          |      |           |
accountinginformationclassificationsystems.Toovercome [1] R. M. Bushman and A. J. Smith, ‘‘Financial accounting information
these issues, we propose a deep feature extraction frame- and corporate governance,’’ J. Accounting Econ., vol. 32, nos. 1–3,
pp.237–333,Dec.2001.
| work based | on  | convolutional |     | autoencoders. |     | This model | is  |                                                                     |     |     |     |     |     |     |
| ---------- | --- | ------------- | --- | ------------- | --- | ---------- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|            |     |               |     |               |     |            |     | [2] B.Ballou,D.L.Heitger,andD.Stoel,‘‘Data-drivendecision-makingand |     |     |     |     |     |     |
designed to learn hierarchical representations directly from itsimpactonaccountingundergraduatecurriculum,’’J.AccountingEduc.,
vol.44,pp.14–24,Sep.2018.
| raw accounting |               | data,           | eliminating | the      | need       | for handcrafted |      |                                                                |              |                |             |     |          |              |
| -------------- | ------------- | --------------- | ----------- | -------- | ---------- | --------------- | ---- | -------------------------------------------------------------- | ------------ | -------------- | ----------- | --- | -------- | ------------ |
|                |               |                 |             |          |            |                 |      | [3] U.Upadhyay,A.Kumar,G.Sharma,S.Sharma,V.Arya,P.K.Panigrahi, |              |                |             |     |          |              |
| features.      | Our framework |                 | integrates  | joint    | objectives | for             | data |                                                                |              |                |             |     |          |              |
|                |               |                 |             |          |            |                 |      | and                                                            | B. B. Gupta, | ‘‘A systematic | data-driven |     | approach | for targeted |
| reconstruction | and           | classification, |             | enhanced |            | by adversarial  |      |                                                                |              |                |             |     |          |              |
marketinginenterpriseinformationsystem,’’EnterpriseInf.Syst.,vol.18,
no.8,Aug.2024,Art.no.2356770.
trainingtopromoterobustnessagainstnoisyandimbalanced
|          |              |     |            |            |     |            |      | [4] Z.Liu,‘‘Accounting-orientedresearchonnoterecognitionmodelbased |     |     |     |     |     |     |
| -------- | ------------ | --- | ---------- | ---------- | --- | ---------- | ---- | ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
| entries. | Experimental |     | results on | real-world |     | accounting | logs |                                                                    |     |     |     |     |     |     |
oninformationextractionalgorithm,’’WSEASTrans.Bus.Econ.,vol.21,
show that our method significantly improves classification pp.2640–2652,Dec.2024.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 193247 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

F.Liu:DeepFeatureExtractionMethodforAutomaticClassification
[5] S. Feng and R. Zhong, ‘‘Optimization and analysis of intelligent [27] J.Li,C.Xu,B.Feng,andH.Zhao,‘‘Creditriskpredictionmodelforlisted
accountinginformationsystembasedondeeplearningmodel,’’Comput. companiesbasedonCNN-LSTMandattentionmechanism,’’Electronics,
Intell.Neurosci.,vol.2022,Jul.2022,Art.no.1284289. vol.12,no.7,p.1643,Mar.2023.
[6] O. M. Lehner, C. Knoll, S. Leitner-Hanetseder, and C. Eisl, ‘‘The [28] J.J.Wild,FinancialAccounting:InformationforDecisions.NewYork,
dynamics of artificial intelligence in accounting organisations,’’ in The NY,USA:McGraw-Hill,2017.
RoutledgeHandbookofAccountingInformationSystems.Evanston,IL, [29] B.Ayash,Z.Bednarek,andA.Bordeman,‘‘Compustatfinancialstate-
USA:Routledge,2022,pp.121–139. mentdataarticulation:Asimplifiedapproach,’’J.FinancialReporting,
[7] T. Sun, ‘‘Applying deep learning to audit procedures: An illustrative vol.2025,pp.1–18,Jun.2025.
framework,’’AccountingHorizons,vol.33,no.3,pp.89–109,Sep.2019. [30] M. Choulga, G. Janssens-Maenhout, I. Super, E. Solazzo, A. Agusti-
[8] T. Sun, ‘‘Accounting information systems outputs: XBRL, AI and in- Panareda,G.Balsamo,N.Bousserez,M.Crippa,H.DeniervanderGon,
memory technologies,’’ in The Routledge Companion To Accounting R. Engelen, D. Guizzardi, J. Kuenen, J. McNorton, G. Oreggioni, and
InformationSystems.Evanston,IL,USA:Routledge,2017,pp.108–119. A.Visschedijk,‘‘GlobalanthropogenicCO2emissionsanduncertainties
[9] J. M. Corchado, L. Borrajo, M. A. Pellicer, and J. C. Yáñez, ‘‘Neuro- asapriorforEarthsystemmodellinganddataassimilation,’’EarthSyst.
symbolicsystemforbusinessinternalcontrol,’’inProc.Ind.Conf.data Sci.Data,vol.13,no.11,pp.5311–5335,Nov.2021.
mining,2004,pp.1–10. [31] J. Hromas, ‘‘Misalignment between profits and economic activity:
[10] M.Hall,A.Ramsay,andJ.Raven,‘‘Changingthelearningenvironment Evidencefromtwodistinctdatasets,’’Tech.Rep.,2025.
topromotedeeplearningapproachesinfirst-yearaccountingstudents,’’ [32] S.M.Al-Selwi,M.F.Hassan,S.J.Abdulkadir,A.Muneer,E.H.Sumiea,
AccountingEduc.,vol.13,no.4,pp.489–505,Dec.2004. A. Alqushaibi, and M. G. Ragab, ‘‘RNN-LSTM: From applications to
[11] T.C.Redman,DataDriven:ProfitingFromYourMostImportantBusiness modeling techniques and beyond—Systematic review,’’ J. King Saud
Asset.Brighton,MA,USA:HarvardBus.Press,2008. Univ.-Comput.Inf.Sci.,vol.36,no.5,Jun.2024,Art.no.102068.
[12] X. Zhang, ‘‘Application of data mining and machine learning in [33] S. Nosouhian, F. Nosouhian, and A. K. Khoshouei, ‘‘A review of
managementaccountinginformationsystem,’’J.Appl.Sci.Eng.,vol.24, recurrentneuralnetworkarchitectureforsequencelearning:Comparison
no.5,pp.813–820,2021. betweenLSTMandGRU,’’Tech.Rep.,2021.[Online].Available:https://
[13] S.Cho,M.A.Vasarhelyi,T.Sun,andC.Zhang,‘‘Learningfrommachine www.preprints.org/frontend/manuscript/3fa37c0d5d54bea69f5b855f2530
learning in accounting and assurance,’’ J. Emerg. Technol. Accounting, 6b5e/download_pub
vol.17,no.1,pp.1–10,Mar.2020. [34] C.GenerativePre-TrainedTransformerandA.Zhavoronkov,‘‘Rapamycin
[14] L.Judijantoetal.,‘‘Data-drivenmarketingcommunications:Thecrucial in the context of Pascal’s wager: Generative pre-trained transformer
roleofaccountinginformationsystems,’’Int.J.Financialecon.,vol.1, perspective,’’Oncoscience,vol.9,pp.82–84,Dec.2022.
no. 2, pp.511–520, 2024. [Online]. Available: https://onlinelibrary. [35] N.Schaduangrat,N.Anuwongcharoen,P.Charoenkwan,andW.Shoom-
wiley.com/doi/abs/10.1002/cbdv.202402479 buatong, ‘‘DeepAR: A novel deep learning-based hybrid framework
[15] S.Askary, N.Abu-Ghazaleh,and Y.Tahat,‘‘Artificial intelligenceand for the interpretable prediction of androgen receptor antagonists,’’ J.
reliability of accounting information,’’ in Proc. Conf. E-Bus. Cham, Cheminformatics,vol.15,no.1,p.50,May2023.
Switzerland:Springer,2018,pp.315–324. [36] B.N.Oreshkin,G.Dudek,P.Pełka,andE.Turkina,‘‘N-BEATSneural
[16] P. O’Regan, Financial Information Analysis: The Role of Accounting networkformid-termelectricityloadforecasting,’’Appl.Energy,vol.293,
InformationinModernSociety.Evanston,IL,USA:Routledge,2015. Jul.2021,Art.no.116918.
[17] S. Cohen, F. Manes Rossi, X. Mamakou, and I. Brusca, ‘‘Financial [37] Q. Zhu, J. Han, K. Chai, and C. Zhao, ‘‘Time series analysis based
accounting information presented with infographics: Does it improve on informer algorithms: A survey,’’ Symmetry, vol. 15, no. 4, p.951,
financialreportingunderstandability?’’J.PublicBudgeting,Accounting Apr.2023.
FinancialManage.,vol.34,no.6,pp.263–295,Dec.2022. [38] Y.Zhang,C.Chen,S.Zhu,C.Shu,D.Wang,J.Song,Y.Song,W.Zhen,
[18] A.-D. Socea, ‘‘Managerial decision-making and financial accounting Z.Feng,G.Wu,J.Xu,andW.Xu,‘‘Isolationof2019-nCoVfromastool
information,’’Proc.SocialBehav.Sci.,vol.58,pp.47–55,Oct.2012. specimenofalaboratory-confirmedcaseofthecoronavirusdisease2019
[19] V. Chakraborty, V. Chiu, and M. Vasarhelyi, ‘‘Automatic classification (COVID-19),’’ChinaCDCWeekly,vol.2,no.8,pp.123–124,Feb.2020.
of accounting literature,’’ Int. J. Accounting Inf. Syst., vol. 15, no. 2, [Online].Available:https://pmc.ncbi.nlm.nih.gov/articles/PMC8392928/
pp.122–148,Jun.2014.
[20] M. R. Garnsey, ‘‘Automatic classification of financial accounting con-
cepts,’’J.Emerg.Technol.Accounting,vol.3,no.1,pp.21–39,Jan.2006.
[21] A. Effiong, ‘‘Computerized accounting systems: Measuring structural
characteristics,’’Res.J.FinanceAccounting,vol.11,no.16,pp.38–54,
2020.
[22] S.Yang,‘‘Strengtheningaccountinginformationsystemswithadvanced FENGRUI LIU receivedthebachelor’sdegreeinaccountingfromHunan
bigdataminingalgorithms:Innovativeexplorationofdatacleaningand University, Changsha, China, in 2022. From 2018 to 2024, he was an
conversionautomation,’’Informatica,vol.49,no.11,pp.1–12,Jan.2025.
Auditor. Since 2023, he has been a Certified Public Accountant with
[23] C. A. Zhang, S. Cho, and M. Vasarhelyi, ‘‘Explainable artificial
Liaoning Dongding Certified Public Accountants, Benxi, China. He has
intelligence (XAI) in auditing,’’ Int. J. Accounting Inf. Syst., vol. 46,
participatedinandledmultiplefinancialauditingprojectsinvolvingstate-
Sep.2022,Art.no.100572.
owned enterprises and listed companies. He has authored several articles
[24] W.XiuguoandD.Shengyong,‘‘Ananalysisonfinancialstatementfraud
inthefieldsoffinancialsupervision,auditinformatization,andenterprise
detectionforChineselistedcompaniesusingdeeplearning,’’IEEEAccess,
riskmanagement.Hisresearchinterestsincludeintelligentauditingsystems,
vol.10,pp.22516–22532,2022.
data-drivenfinancialanalysis,anddeeplearningapplicationsinaccounting
[25] P. Craja, A. Kim, and S. Lessmann, ‘‘Deep learning for detecting
financial statement fraud,’’ Decis. Support Syst., vol. 139, Dec. 2020, practices. He is a member of the Chinese Institute of Certified Public
Art.no.113421. Accountants.Heactivelycontributestoregionalforumsonsmartauditing
[26] O. V. Adamyk, ‘‘Difference between concepts ‘automated’, ‘computer’ transformationandhasservedasapeerreviewerforjournalsinaccounting
and‘information’accountingsystems:Transformationofelementsofthe informationsystems.
method,’’Ekonomichnyyanaliz,vol.26,no.1,pp.163–169,2016.
193248 VOLUME13,2025