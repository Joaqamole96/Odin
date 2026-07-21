---
conversion_metadata:
  converted_at: "2026-07-21T05:14:13Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Abd-Ellatif et al.pdf"
  source_pdf_sha256: "a9c9fa02dcc3f113e4206d6920efd1dcba3ddc7045024ab1322c2e46283e6352"
  page_count: 16
  markdown_char_count: 39025
---

AdvancesinArtificialIntelligenceandMachineLearning;Research5(2)3988-4003 Received13-04-2025;Accepted21-06-2025;Published28-06-2025
ATAD-Net: An Adaptive Deep Learning Framework for Real-Time
Financial Fraud Detection
LailaAbd-Ellatif laila.a@aou.edu.om
FacultyofComputerStudies(FCS),
ArabOpenUniversity,Oman
Muscat130,Oman
MohammadAbrar abrar.m@aou.edu.om
FacultyofComputerStudies(FCS),
ArabOpenUniversity,OmanMuscat130,Oman
AlaaA.K.Ismaeel alaa.ismaeel@aou.edu.om
FacultyofComputerStudies(FCS),
ArabOpenUniversity,Oman
Muscat130,Oman
CorrespondingAuthor:LailaAbd-Ellatif
Copyright © 2025 Laila Abd-Ellatif, et al. This is an open access article distributed under the Creative Commons
AttributionLicense,whichpermitsunrestricteduse,distribution,andreproductioninanymedium,providedtheoriginal
workisproperlycited.
Abstract
With the fast growth of financial transaction fraud, there is a need for advanced detection
systemscapableofreal-timeanalysis. Rule-basedandmachine-learningapproachestofraud
traditionallysufferfrombeingunabletoadapttochangingfraudpatterns,returningveryhigh
back result rates and much inefficiency in the security of financial operations. However,
convolutional neural networks (CNNs) and recurrent neural networks (RNNs) methods are
suitable, but they lack adaptability and interpretability. This paper proposes an Adaptive
Transactional Anomaly Detection Network (ATAD-Net), a new deep learning (DL) frame-
work for improving fraud detection accuracy, minimizing false positives, and guaranteeing
real-timeadaptability. ATAD-Netdynamicallyadjuststoevolvingfraudtacticsbyintegrat-
ingCNNsforlocalpatternrecognitionandLongShort-TermMemory(LSTM)forsequential
transaction analysis. After training and testing the model using the IEEE CIS Credit Card
Fraud Detection Dataset, a large-scale benchmark for evaluating financial fraud detection
models,theaccuraciesofthedifferentmodelswereassessed.
This study applied the Synthetic Minority Sampling Technique (SMOTE) to address data
imbalance and ensure that fraud transactions were represented fairly. Accuracy, precision,
recall,andF1score,aswellasreal-timeprocessinglatency,wereusedtoperformtheperfor-
manceevaluation. TheresultsshowedthatATAD-Netperformedmuchbetterthanbaseline
CNNandRNNmodelswithanaccuracyof98.65%,fewerfalsepositives,andareal-timede-
tectionlatencyof8.2millisecondspertransaction. ATAD-Netaddressesthisbydynamically
adaptingtoevolvingfinancialfraudstrategies,thusenhancingfinancialfrauddetectionand
offeringfinancialinstitutionsaveryaccurateandefficientreal-timefinancialfrauddetection
solution.
3988
Citation: Laila Abd-Ellatif, et al. ATAD-Net: An Adaptive Deep Learning Framework for Real-Time Financial Fraud Detection.
AdvancesinArtificialIntelligenceandMachineLearning,2025;5(2):225.

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
Keywords: Financialfrauddetection,Deeplearning,ATAD-Net,Adaptivelearning,CNN,
LSTM
1. INTRODUCTION
FinancialtransactionfraudhasbecomeoneofthemostseriousissuesinthecontemporaryInternet
economy. Since the reliance on electronic transactions is growing and fraudsters are constantly
developing sophisticated schemes to exploit vulnerabilities in a financial system, the scope of the
fraud has increased [1]. The fraudulent activities are usually the unauthorized use of financial
accounts or the deceiving in obtaining financial gain, which leads to the loss of large sums in
accounts to both institutions and individuals [2]. Common fraudulent techniques of today include
creditcardfraud,identitytheft,phishing,andunauthorizedfundtransfers[3].
According to recent reports, global financial institutions have lost billions yearly to transaction
fraud. Forexample,Nilsonreportedthat2030globalcreditcardfraudwouldexceed$49billion[4].
Generally,thesealarmingnumbersnotonlydepictfinanciallossesbutalsoreflectextraoperational
burdensandlowercustomertrustinfinancialinstitutions[5]. Detectingfinancialtransactionfraud
is usually hard because criminals are constantly developing new ways to commit the crime. The
traditionaldetectionmethodsdependonrule-basedsystemsandhistoricaltransactiondataanalysis.
However, these methods fail to keep up with the fast-changing fraud patterns and are ineffective
in real-time scenarios [6]. Fraud might be undetected and continued until considerable harm is
done. In recent years, advanced ML and DL methods have been used more to address traditional
techniques’troublespots. Ithasbeendemonstratedbypreviousresearchthatseveralanomaliesthat
indicate fraud, including rare and hidden patterns, can be recognized better using Convolutional
NeuralNetworksandRecurrentNeuralNetworks[7].
Nevertheless,DLmodelshavenotreachedahighlevelofadaptabilityandsometimeshaveunclear
reasoning for their decisions [8]. Since these weaknesses have been identified, this research dis-
cusses ATAD-Net, a new network-based model that smoothly adjusts ATAD to emergent threats.
Carryingoutthisresearchmayresultin: betteraccuracyincatchingfraudsters,fewerfalsepositive
errors,quickerresponse,andmoretrustingcustomersinfinancialservices. Nevertheless,somevital
problems can be found in current fraud detection methods. Rules in a system are based on stable,
fixed,andpresetboundaries. Theyaren’tabletospotnewkindsoffraudand,astheygeneratealotof
incorrectalerts,canmistakegoodpaymentsforbadones[9]. Itcausesinconveniencetocustomers
andincursoperationalcoststofinancialinstitutionsconductingmanualreviews. Detectionaccuracy
has been improved compared to rule-based methods using ML approaches such as decision trees,
logisticregression,andsupportvectormachines[10].
Nevertheless, these models still heavily rely on manually engineered features and depending on
the historically labeled data, making them prone to fast-changing environments [11]. Further,
even for these techniques, they are not able to handle effectively imbalanced datasets—fraudulent
transactionsbeingaverysmallportionofalltransactions—andtherebymakebiasedpredictionsand
have poor reliability [12]. DL techniques such as CNNs and RNNs have manifested themselves
to be promising in extracting complex patterns from big-scale data these past years. However,
existing DL models still have numerous problems. First, the models are not interpretive, so it is
hardtounderstandwhysometransactionsarelabeledfraudulent. Withouttransparency,usertrustis
3989

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
required,andregulatorycomplianceisdifficult[13]. Inaddition,DLmethodsusuallydemandlarge
amounts of computation, and their real-time detection performance may not be guaranteed, which
iscriticalinfinancialapplications[14]. Toovercometheexistinglimitations,amoreadaptiveand
transparentDLframeworkisthereforeneeded.
ThisstudyaddressesexistinggapsbyintroducinganoveladaptiveDL-basedfrauddetectionmodel,
theATAD-Net. Specifically,theresearchobjectivesare:
• TodesignanadaptiveDLframeworkthatdynamicallylearnsevolvingfraudpatternsinreal-
timefinancialtransactions.
• To improve fraud detection accuracy, significantly reduce false-positive alerts, and enable
real-timedecision-making.
• To develop a model architecture that effectively addresses the data imbalance problem com-
moninfrauddetectiondatasets.
• ToevaluateandbenchmarktheproposedmodelagainsttraditionalMLandDLmodelsusing
standardperformancemetrics,suchasaccuracy,precision,recall,andF1-score.
• Toenhancemodelinterpretabilitybyprovidingclearinsightsintodecision-makingprocesses,
improvingusertrustandfacilitatingregulatorycompliance.
These objectives can help both the financial institutions and the customers to place more trust in
them and at the same time help in developing robust fraud detection solutions and to make digital
transactions reliable as possible. This paper introduces ATAD-Net, a DL framework adapted to
identifyfinancialfraudsinrealtime. ThisworkcontributestothedesignofahybridCNN-LSTM
architecture that is capable of learning both spatial and sequential fraud patterns, leading to an
improvementindetectionaccuracy. TheDynamicPatternAdjustmentModule(DPAM)allowsthe
modeltorespondtoadjustmentsinthetacticappliedwithminimalretraining. Thepaperalsouses
SMOTEtoalleviatetheproblemofclassimbalancetoincreasethenumberoffraudulenttransactions
thataredetected.
Thispaperisorganizedasfollows: Section2reviewsexistingfrauddetectionmethodsandresearch
gaps. Section 3 details ATAD-Net’s architecture, preprocessing, and adaptive learning. Section
4 presents experimental results, comparing ATAD-Net with CNN and RNN models. Section 5
concludeswithkeyfindingsandfutureresearchdirections.
2. RELATED WORK
Frauddetectioninfinancialtransactionshasbeenanactiveresearchareaforseveraldecades. Vari-
ousmethodologieshaveemerged,eachattemptingtobalanceaccuracy,efficiency,andadaptability
toevolvingfraudulentbehaviors. Broadly,frauddetectionmethodsfallintothreemaincategories:
traditionalrule-basedmethods,MLtechniques,andDL-basedapproaches. Initially,financialinsti-
tutions primarily relied on rule-based systems, which detect fraudulent activities using predefined
rulesandthresholds. Thesemethodsapplylogicalconditionstotransactionfeatures,suchastrans-
actionamounts,locationmismatches,frequencyoftransactions,andunusualspendingpatterns[15].
Somesystemsexhibitnotabledrawbacks,theyfailtoidentifynovelfraudschemesthatdonotmatch
existingrulesandaresusceptibletohighfalse-positiverates[16]. Consequently,extensivehuman
intervention becomes necessary, increasing operational costs and customer dissatisfaction [17].
3990

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
Giventhelimitationsofrule-basedsystems,researchersandpractitionerstransitionedtowardsML
approaches. CommonMLmethodsincludeDecisionTrees,RandomForests,LogisticRegression,
SVM,andBayesianNetworks. Bhattacharyyaetal. (2011)[9],comparedvariousMLmethodsand
highlightedthatRandomForestandSVMmodelssignificantlyimprovedetectionaccuracy. These
techniqueslearnpatternsfromhistoricaltransactiondataandpredictfraudulentbehaviorbasedon
learnedfeatures[18].
However, ML approaches heavily depend on manual feature engineering, and their performance
can degrade when facing imbalanced data, a common scenario in fraud detection datasets [12].
More recently, unlike traditional ML methods, DL models automatically extract complex patterns
fromrawtransactiondata,significantlyreducingtherelianceonmanualfeatureengineering. CNNs
haveshowneffectivenessinspatialdatarepresentation,suchastransactionfeaturemaps,capturing
intricate anomalies within transactional behavior [19]. Similarly, RNNs and Long Short-Term
Memory(LSTM)networkseffectivelymodelsequentialtransactionpatterns,allowingthedetection
oftemporalfraudpatternsandtransaction-levelanomalies[8]. Royetal. (2018)[7],demonstrated
therobustnessofDLmethods, specificallyCNNandLSTMarchitectures, indetectingcreditcard
fraud. Milad (2025) [20], further validated that deep neural networks outperform traditional ML
algorithmsintermsofaccuracyandfalse-positiverates. Despitetheirstrengths,DLmodelsrequire
significant computational resources and often struggle with interpretability, making it challenging
foruserstounderstandmodeldecisionsclearly[20]. Despitethedifferencesintheadvantagesthat
each of the above categories of methods offers, none of them is capable of fully addressing all
thesechallenges. Forthisreason,thereisstillaneedforfurtherresearcheffortstowardsadaptive,
efficient,andinterpretableDLmethodologies.
TheuseofDLhasgreatlyenhancedfrauddetectionstrategiesbyautomaticallydiscoveringhidden
patterns within large and complex datasets. DL algorithms differ from that of traditional ML
because, rather than requiring extensive feature engineering, they can easily work with raw data
efficiently. TwowidelyusedDLarchitecturesforfrauddetectionincludeCNNsandRNNs. CNNs
havebecomeprominentduetotheirsuccessinextractingspatialpatternsfromdata,initiallygaining
popularityinimage-processingtasks[21]. Recently,CNNshavedemonstratedstrongperformance
infrauddetectiontasksbytreatingtransactiondataasstructuredinputsandidentifyingrelationships
amongtransactionfeaturesmoreeffectively[22]. Royetal. (2018)[7],appliedCNNssuccessfully
to credit card fraud detection, reporting improved accuracy and reduced false positives compared
to classical ML methods. CNNs and RNNs are designed specifically for sequential data analysis,
making them suitable for modeling transaction histories and temporal patterns. RNNs, particu-
larly LSTM networks excel in identifying anomalies based on transaction sequences and patterns
evolving[7]. Almazroietal. (2023)[23],appliedLSTM-basedRNNstofrauddetectioninmobile
payment systems, significantly outperforming traditional ML models, especially when handling
data exhibiting temporal dependencies. Traditional DL methods have many important drawbacks
despitetheirconsiderablesuccesses. Second, CNNandRNNarchitectureareusuallytrainedwith
large amounts of labeled data [24]. However, financial transaction datasets are usually highly
imbalanced as only a small fraction of records are of fraudulent kind, which causes poor model
performance [12]. In addition, these DL models are often “black boxes that exhibit a low amount
of interpretability and transparency, which makes regulators, financial institutions, and customers
forcomplianceandtrustreasons[13]. Inaddition,traditionalDLmodelsaregenerallyincapableof
performing fast responses to the evolution of fraud strategies, which renders them less efficient in
dealingwithnewfraudpatternsarisinginreal-timeenvironments[8].
3991

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
Thus, there is still a clear lack of research in designing interpretable, flexible, and responsive DL
systems for detecting fraud. Because the current DL methods are not flexible and generally do
not change in response to changing fraud tactics, it becomes costly and inefficient to retrain these
toolsoften[25]. Inaddition,sincetransparencyislackinginthemodel,financialstakeholderskeep
doubtingitsvalidity. Itisrequiredtodesignalearningmethodthatrespondsflexiblytothechanges
intransactionsandtotransactionalfraudpatterns. Becauseofthis,thefrauddetectionmodelswork
better and faster since they depend less on old data and continue to be retrained [26]. Hence, an
adaptive technique such as the ATAD-Net suggested by this study should be used to resolve these
shortcomings.
3. PROPOSED METHODOLOGY OF ATAD-NET
3.1 ConceptualFrameworkofATAD-Net
TheATAD-Netisabletofindanddetectfraudbyadaptingtonewchangesinthewaytransactions
areconducted. TheInputLayerpicksupdataonreal-timetransactions,whichincludestheamount,
the time stamp, the place where they happen, the type, and how people behave. The Adaptive
Preprocessing Module preprocesses the data, ensuring it is normalized as fraud patterns continue
todevelop. TheFeatureExtractionModulecombinesCNNandRNNlayerstodetectlocalandse-
quentialfraudpatterns. TheAdaptiveLearningMechanismupdatesmodelparametersinreal-time,
adaptingtonewfraudtactics. TheAnomalyDetectionEngineclassifiestransactionsandgenerates
fraudalertsinstantly. TheInterpretabilityModulevisualizesmodeldecisionsfortransparency. The
FeedbackLoopcontinuouslyrefinesthemodel,improvingdetectionaccuracyovertime. FIGURE
1illustratestheoverallconceptualframeworkoftheproposedmodel,highlightingthekeyprocesses
andcomponentsinvolvedinreal-timefrauddetection.
3.2 DatasetandPreprocessing
To evaluate the effectiveness of the proposed ATAD-Net model, we utilize the publicly available
IEEE-CISCreditCardFraudDetectiondatasetToevaluatetheeffectivenessoftheproposedATAD-
Net model, this research utilizes the widely recognized IEEE-CIS Credit Card Fraud Detection
dataset [27]. This benchmark dataset comprises approximately 590,540 transactions, each labeled
as either legitimate or fraudulent, and is widely recognized for its realistic simulation of financial
transaction behaviors. The dataset includes both numerical and categorical features such as trans-
actionamount,transactiontime,devicetype,anonymizeduserbehaviorindicators,andidentifiers.
Duetotheinherentclassimbalance—only3.5%oftransactionsarefraudulent—SyntheticMinority
Over-sampling Technique (SMOTE) was applied to balance the data. The dataset was partitioned
into70%fortraining,15%forvalidation,and15%fortesting. Inputfeatureswerenormalizedusing
Min-MaxandZ-scorescaling,andcategoricalfeaturesweretransformedviaone-hotencoding. For
modelinput, thepreprocesseddatawasstructuredintosequences: CNNlayersfirstextractspatial
featuresfromeachtransactioninstance,andtheseprocessedfeaturemapsarethenpassedtoLSTM
layers,whichmodelthetemporalandsequentialpatternsacrosstransactions. Thissequentialflow
enables ATAD-Net to effectively learn both localized and time-dependent patterns indicative of
fraudulentbehavior. ThisbenchmarkdatasetispubliclyavailablethroughKaggleandisfrequently
3992

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
Figure1: ConceptualFrameworkoftheATAD-Net.
used to assess fraud detection models due to its realistic representation of financial transaction
behavior. The dataset consists of approximately 590,540 transactions labeled as either legitimate
or fraudulent. The data contains numerical and categorical attributes such as transaction amount,
transaction time, device information, user identifiers, and anonymized user behavioral features,
providingacomprehensivebasisfortrainingrobustmodels. Onechallengeinusingthisdatasetis
itssignificantclassimbalance,asfraudulenttransactionsconstituteonly3.5%oftheentiredataset,
closelyresemblingreal-worldscenarios[28].
To ensure the effectiveness of the ATAD-Net model, the dataset undergoes several preprocessing
steps. Transactions containing extensive missing values or inconsistent entries were removed to
maintaindataquality. Forminormissingvalues,medianimputationwasappliedtonumericfeatures,
whilemodeimputationwasusedforcategoricalattributes. Numericalfeaturessuchastransaction
amount and timestamp were normalized using Min-Max scaling, and Z-score normalization was
applied where appropriate to ensure consistent feature distributions. Categorical variables such as
device type, transaction type, and payment method were converted into a numerical format using
one-hotencodingtoenablecompatibilitywiththedeeplearningmodel.
Giventhehighlyimbalancednatureofthedataset—withfraudulenttransactionsrepresentingonly
3.5%ofallrecords—theSyntheticMinorityOver-samplingTechnique(SMOTE)[21]wasapplied
to the training data after splitting to prevent data leakage. SMOTE generates synthetic examples
of the minority class by interpolating between existing fraudulent samples in feature space, thus
3993

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
enhancingthemodel’sabilitytodetectfraudwhilemaintaininggeneralization. Thisapproachhelps
reduceclassbiasandimprovetherobustnessoftheATAD-Netmodelactionscontainingextensive
missingvaluesorinconsistententrieswereremovedtomaintaindataquality. Forminormissingdata
points,medianimputationtechniqueswereappliedtonumericfeatures,whilemodeimputationwas
usedforcategoricalattributes. Numericalfeaturessuchastransactionamountandtimestampwere
normalized using Min-Max normalization to scale values within a consistent range (0 to 1). This
reducesthebiasthatarisesduetoscaledifferencesamongfeatures. Categoricalattributeslikedevice
type, transaction type, and payment methods were transformed into numerical form using one-hot
encodingtechniques. ThisensuresthatcategoricalfeaturesareaccuratelyrepresentedwithintheDL
model. Duetothehighlyimbalancednatureofthedataset,theSMOTEwasimplementedtobalance
fraudulentandlegitimatetransactionclasses. SMOTEeffectivelyincreasesminority-classinstances
(fraudulenttransactions),enhancingthemodel’sabilitytoaccuratelydetectfraudwithoutbias[21].
Z-score normalization was applied to scale numeric transaction features, ensuring uniformity in
data distribution and facilitating efficient model training. these preprocessing steps ensure high-
quality,balancedinputdata,thusenhancingthereliabilityandrobustnessoftheATAD-Netmodel’s
performance.
3.3 ProposedMethodology: ArchitecturalDesignofATAD-Net
ATAD-Netintegrates advanced DL modules to detect evolving fraud patterns in financial transac-
tionsdynamically. Itsarchitectureconsistsofthreekeymodules: anAdaptiveSequentialLearning
Mechanism,Multi-LevelFeatureExtractionlayers,andaDynamicPatternAdjustmentModule.
3.3.1 Adaptivesequentiallearningmechanism
ATAD-NetintegratesRecurrentNeuralNetworklayers(specifically,LSTMunits)designedtolearn
𝑋
temporal dependencies and sequential transaction patterns. Given a sequence of transactions =
𝑥 ,𝑥 ,𝑥 ,...𝑥 𝑡,eachtransaction𝑥 comprisesmultiplefeatures. TheLSTMlayermaintainshidden
1 2 3 𝑖
statesthatencodesequentialpatternsasfollows:
|     |         | (cid:0)     |        |         | (cid:1) |     |
| --- | ------- | ----------- | ------ | ------- | ------- | --- |
|     | 𝑓 𝜎     | 𝑊 ·         | [ℎ ,𝑥] | +𝑏      |         |     |
|     | 𝑡 =     | 𝑓           | 𝑡−1    |         | 𝑓       | (1) |
|     | (cid:0) |             |        |         | (cid:1) |     |
| 𝑖   | = 𝜎 𝑊   | 𝑥 +𝑊ℎ       | ℎ      | +𝑏      |         | (2) |
| 𝑡   |         | 𝑥 𝑖 𝑡       | 𝑖      | 𝑡−1     | 𝑓       |     |
| 𝑜   | 𝜎(𝑊     | ·           | [ℎ ,𝑥  | ] +𝑏    | )       |     |
|     | 𝑡 =     | 𝑜           | 𝑡−1    | 𝑡       | 𝑜       | (3) |
| 𝐶˜  | =𝑡𝑎𝑛ℎ(𝑊 |             | · [ℎ   | ,𝑥 ] +𝑏 | )       |     |
| 𝑡   |         | 𝐶           | 𝑡−1    | 𝑡       | 𝐶       | (4) |
|     | 𝐶 =     | 𝑓 ·𝐶        | +𝑖     | ·𝐶˜     |         | (5) |
|     | 𝑡       | 𝑡           | 𝑡−1    | 𝑡 𝑡     |         |     |
|     | ℎ       | = 𝑜 ·𝑡𝑎𝑛ℎ(𝐶 |        | )       |         | (6) |
|     | 𝑡       | 𝑡           |        | 𝑡       |         |     |
Here, ℎ 𝑡 represents the hidden state capturing the transaction’s temporal features, and 𝐶 𝑡 is the
memory cell state at the time t. The adaptive nature of LSTM allows the ATAD-Net to maintain
historicalcontext,enablingdynamicrecognitionofemergingfraudulentbehaviors.
3.3.2 CNN:Multi-levelfeatureextraction
CNN layers are integrated into the ATAD-Net architecture to extract complex, localized features
fromtransactiondata. Transactionsarerepresentedasstructuredfeaturemaps,enablingCNNlayers
3994

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
to effectively detect subtle patterns indicative of fraud. The convolution operation is represented
mathematicallyasfollows:
(cid:213)
' “
𝐹 𝑗 = 𝑓 › 𝑋 𝑖 ·𝑊 𝑖𝑗 +𝑏 𝑗 fi (7)
«𝑖∈𝑀 𝑗 ‹
Here, 𝑋 𝑖 denotesinputfeaturesfromthetransaction,𝑊 𝑖𝑗 representsconvolutionalkernelweights,
𝑏 𝑗 isthebiasterm,and 𝑓(·) istheactivationfunction,typicallyaRectifiedLinearUnit(ReLU):
𝑓(𝑥) = 𝑚𝑎𝑥(0,𝑥) (8)
Pooling layers subsequently condense the extracted features, focusing on the most informative
featurestoenhancemodelperformanceandreducecomputationalcomplexity.
3.3.3 Dynamicpatternadjustmentmodule
A key innovation in ATAD-Net is the Dynamic Pattern Adjustment Module (DPAM), designed
to address the challenge of adapting to evolving fraud tactics in real time. Unlike conventional
deep learning models that require full retraining, DPAM performs incremental parameter updates
basedonnewtransactiondata. Themodulemonitorsincomingtransactionsusingasliding-window
strategy, selecting a recent subset of data to periodically assess shifts in transactional behavior.
Modelparametersareupdatedusinggradient-basedoptimization:
𝜕𝐿(𝑋,𝑌)
𝑊𝑛𝑒𝑤 =𝑊𝑜𝑙𝑑 −𝜂· (9)
𝜕𝑊
where𝑊 representsthemodelweights,𝜂isthelearningrate,and𝐿(𝑋,𝑌)isthelosscalculatedfrom
recentinputs 𝑋 andandthiertruelabels𝑌.
Becauseofthismechanism,ATAD-Netisabletorespondtonewtypesoffraudwithoutusingmuch
computingpower. SinceDPAMfocusesonlearningfrommostrecentchangesandnofullretraining
isneeded,themodelperformswellwhentransactionschangerapidly. Theseadvancementsaidboth
thedeliveryandefficiencyoftheAPIs.
Along with high accuracy, ATAD-Net features an Interpretability Module to make the workings
of the AI more understandable to users. This module emphasizes important parts of a transaction,
usingdetailsfromitsinternallytrainedmodel,topointoutwhichkeyfactorscontributedthemostto
identifyingfraudpredictions. Forinstance,ariseintheamountofmoneygoingthroughtransactions
or transactions occurring when not expected by the model are brought to attention. They enable
analysts to check and understand what the model is generating. In the future, we plan to use
SHAPandLIMEtoclarifyATAD-Net’sdecisionsandhelpnon-technicalpeoplecomprehendthem,
meetingtheneededstandardsforfinancialcompliance.
The integration of CNN and LSTM in ATAD-Net is intentional to leverage the strengths of both
architectures. CNN layers are effective at capturing localized transactional anomalies—such as
unusual amounts or locations—by treating transaction features as structured inputs. However,
CNNslacktemporalawareness. LSTMlayers,incontrast,areadeptatmodelingthesequentialand
behavioralaspectsoftransactionsovertime. BycombiningCNN’sabilitytodetectspatialpatterns
withLSTM’sstrengthinlearninglong-termdependencies,ATAD-Netcanrecognizecomplexfraud
3995

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
schemesthatevolvebothlocallyandtemporally. Thishybridarchitecturethusenablesmorerobust
detectioncomparedtostandaloneCNNorLSTMmodels.
3.4 TrainingStrategyandHyperparameterOptimization
TheATAD-Netwastrainedthroughasupervisedlearningapproach. TheAdamoptimizerwasused
for training with a batch size of 128 transactions. Hyperparameters such as learning rate, epochs,
dropoutrates,etc.,wereoptimizedusingagridsearchmethodand5-foldcross-validationtoavoid
overfitting and achieve robust model performance. To cope with class imbalance, weighted loss
functions with emphasis on minority class (fraudulent transactions) errors were used to increase
sensitivitytorarefraudulenttransactions.
3.5 EvaluationandValidation
Aseparatetestdatasetisusedtocalculatestandardevaluationmetrics: accuracy,precision,recall,
and F1 score, to validate the effectiveness of ATAD-Net. Evaluation of the computational latency
pertransactionwascarriedouttoalsomeasurethereal-timecapabilityofthemodel.
4. RESULTS AND DISCUSSION
TheexperimentalevaluationoftheproposedATAD-NetusingthepreviouslymentionedIEEEFraud
Detection benchmark dataset is performed in this section. Finally, the model performance was
evaluated about the standard classification metrics: accuracy, precision, recall, and F1 score. The
evaluationmetricsofATAD-Netw.r.tconventionalDLmodels,CNN,andRNNaresummarizedin
TABLE1. ResultsoftheevaluationdepictedthatATAD-Netperformedbetteronallthemetrics.
The confusion matrix shown in FIGURE 2, highlights ATAD-Net’s efficacy, showing fewer false
positivesandfalsenegatives. FIGURE3demonstratestheprecision-recallcurves,confirmingthat
ATAD-Neteffectivelyhandlestheimbalancednatureofthedataset.
Model Accuracy(%) Precision(%) Recall(%) F1-Score(%)
CNN 97.23 79.20 81.40 82.30
RNN 97.05 83.40 82.60 84.20
ATAD-Net 98.65 97.12 96.74 96.93
Table1: PerformancecomparisonbetweenATAD-Net,CNN,andRNNmodels.
Inaddition,theevaluationofreal-timeperformance(latencypertransaction)(FIGURE4)indicates
thatATAD-Netsuccessfullyanalyzestransactionswithinmilliseconds,meetingpracticalreal-time
detectionrequirements. FIGURE5illustratesthetrainingandvalidationlosscurvesforATAD-Net,
showingconvergenceandminimaloverfitting,confirmingtheeffectivenessoftheadaptivelearning
strategy. ATAD-Netalsoeffectivelyaddressedtheclassimbalancechallenge. AsshowninFIGURE
6,usingSMOTEincreasedtherepresentationoffraudulentsamples,significantlyenhancingoverall
modelaccuracyandrecall.
3996

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
Figure2: ConfusionMatrixofATAD-Net.
Figure3: Precision-RecallCurveofATAD-Net.
TheseexperimentalresultsconfirmthattheATAD-Netishighlyeffectiveforreal-timefrauddetec-
tioninfinancialtransactions,offeringsignificantimprovementsovertraditionalDLmodels. Real-
timefrauddetectioncapabilityiscriticalforpracticaldeploymentinfinancialsystems. Toevaluate
thereal-timeefficiencyoftheATAD-Netmodel, thetransactionprocessing latencywasmeasured
usingthebenchmarkdataset. Specifically,latency—thetimefromtransactioninitiationtoanomaly
3997

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
14
12.5
12
10.6
)s
m 10
(
y
8.2
c 8
n
e
t
a
L 6
e
g
a
r e 4
v
A
2
0
CNN RNN ATAD-Net
Detection Model
Figure4: Real-timePerformance(LatencyperTransaction).
Figure5: TrainingandValidationLossCurvesforATAD-Net.
alertgeneration—wasevaluatedasaprimaryindicator. TABLE2summarizestheaveragedetection
latencyforATAD-Netcomparedwithotherstandardmodels. ItclearlyshowsATAD-Net’ssuperior
real-timeprocessingcapability.
TofurtherdemonstratetheconsistencyofATAD-Net’sreal-timeprocessingcapability,transaction
processing times were recorded over continuous real-time simulation periods. As illustrated in
FIGURE7,ATAD-Netmaintainedstableandminimallatencyevenduringpeaktransactionloads.
3998

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
Before SMOTE (%) After SMOTE (%)
96.5
100
)% 80
(
e
g
a
tn 60
50 50
e
c
r
e
P 40
20
3.5
0
Legitimate Transactions Fraudulent Transactions
Class
Figure6: ClassDistributionBeforeandAfterSMOTE.
DetectionModel AverageLatency(ms)
CNN 10.6
RNN 12.5
ATAD-Net 8.2
Table2: Averagelatencypertransactionforreal-timefrauddetection.
Figure7: ATAD-NetReal-TimeLatencyunderPeakTransactionLoad.
3999

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
Tofurtherverifythemodel’sabilitytohandlestreamingdataeffectively,weconductedthroughput
tests, evaluating how many transactions ATAD-Net processes per second (FIGURE 8). Addition-
ally, the real-time detection accuracy was tested by simulating live transactions over a 60-minute
time window. ATAD-Net consistently identified fraudulent transactions promptly and accurately
(TABLE3).
350
)S
P 290
T 300
(
d
n
o 250
c 220
e
S 200
r e 200
p
s
n
o 150
itc
a
s 100
n
a
r
T
50
0
CNN RNN ATAD-Net
Model
Figure8: TransactionsperSecond(TPS)PerformanceComparison.
TimePeriod TotalTransactions FraudulentTransactions DetectedFraud Accuracy
0-15min 12,520 360 349 97.30%
16-30min 11,230 420 411 96.50%
31-45min 12,500 410 399 97.32%
46-60min 13,500 425 415 97.64%
61-75min 14,000 440 430 97.72%
Table3: Real-timedetectionaccuracyunderlivetransactionsimulation.
Overall,theevaluationclearlydemonstratesATAD-Net’sexceptionalreal-timedetectioncapabili-
ties. Byeffectivelyidentifyingfraudwithinmilliseconds,ATAD-Netmeetsthestrictrequirements
ofmodernfinancialinstitutions. Thisreal-timeresponsivenesssignificantlyimprovestheproposed
model’s practicality and applicability for real-world fraud prevention. TABLE 4 presents a com-
parativeevaluationofATAD-Netagainstrecentstate-of-the-artdeeplearningmodelsforfinancial
fraud detection. The models include CNN-based, LSTM-based, and GNN-based approaches. Re-
sults show that ATAD-Net consistently achieves higher accuracy, precision, and recall, while also
maintaining the lowest latency, demonstrating its superiority in both detection performance and
real-timeresponsiveness.
These results highlight the effectiveness of ATAD-Net in handling imbalanced datasets, learning
complexfraudpatterns,andrespondingtotransactionsinrealtime. Comparedtootherstate-of-the-
art models, ATAD-Net demonstrates lower latency, making it well-suited for deployment in high-
throughput financial environments. The combination of CNN and LSTM architectures, enhanced
4000

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
Ref. Dataset Accuracy Precision Recall Latency
(ms)
[7] IEEE-CISCreditCardDataset 96.21% 85.40% 83.90% Not
reported
[20] IEEE-CISCreditCardDataset 97.42% 90.10% 89.80% 11.5
[21] Synthetic/RealTransactionGraph 98.11% 92.60% 91.40% 10.2
ATAD-Net IEEE-CISCreditCardDataset 98.65% 97.12% 96.74% 8.2
(Proposed)
Table4: ComparisonwithState-of-the-ArtDeepLearningModels.
with the Dynamic Pattern Adjustment Module (DPAM), enables ATAD-Net to adaptively capture
localizedandsequentialfraudpatterns. ThesefindingsaffirmATAD-Net’spotentialasarobustand
practicalsolutionforreal-timefinancialfrauddetection.
5. CONCLUSION AND FUTURE WORK
Thisresearchpresentsaninnovativedeep-learningsolutiontailoredtothetaskofreal-timefinancial
frauddetection,referredtoastheATAD-Net. Thekeygoalwastoovercomethelimitationsofthe
existingfrauddetectionsolutions,limitedresponsiveness,inabilitytochangedynamically,andhan-
dlinghighlyimbalanceddata. ThearchitectureoftheATAD-Netisuniqueasitintegratesadaptive
sequentiallearningmechanisms,multi-levelfeatureextraction,andaDPAM,toallowittoperform
efficiently fraud detection and response in response to evolving fraud patterns. Empirical evalua-
tionon the IEEE-CIS benchmark dataset showed that the proposedATAD-Netmodel consistently
significantlyoutperformedotherexistingmethodslikeCNNandRNN-basedmodels. Inparticular,
ATAD-Net achieved significant improvements in the critical metrics of accuracy (98.65%), preci-
sion (97.12%), recall (96.74%), and F1-score (96.93%). ATAD-Net also showed good real-time
detection capabilities, with an average latency per transaction of about 8.2 milliseconds, which is
verysuitablefordeploymentsinpracticalfinancialtransactionsystems. Tosuccessfullyaddressthe
balanceoftheproblemofimbalance,SMOTEwasusedinATAD-Net,withATADNetgreatlyim-
provingitsabilitytoaccuratelyclassifyrarefraudulenttransactions. Interpretabilityimprovements
within ATAD-Net also enabled a better understanding of the model’s decision-making process,
whichgreatlyhelpedregulatorycomplianceandstakeholdertransparency.
ATAD-Net has performed better in interpretability than other DL models, simplification and clar-
ification of decisions could be further simplified. Future research should find ways to combine
advancedexplainedmethods(e.g. SHAPorLIME)toprovideevenmoreclearandunderstandable
explanations to non-technical stakeholders, regulators, and end users. In the last section, it is
worthexploringtheapplicabilityandgeneralizabilityofATAD-Nettoothertransactionaldomains,
includingcryptocurrencyexchanges,mobilepaymentsystems,etc.,whichconstitutesfuturework.
Bytestingandadaptingthemodelinthesebroadertransactionalcontexts,theversatility,robustness,
andoverallimpactoftheproposedmethodcanbesignificantlyexpanded.
4001

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
6. ACKNOWLEDGEMENT
Research reported in this publication was supported by Arab Open University Oman under the
internalfundgrantnumber[AOU_OM/2023/FCS4].
References
[1] Sahin Y, Duman E. Detecting Credit Card Fraud by Decision Trees and Support Vector
Machines. In Proceedings of the international multiconference of engineers and computer
scientists.2011:442–447.
[2] Carcillo F, Le Borgne YA, Caelen O, Bontempi G. Streaming Active Learning Strategies for
Real-Life Credit Card Fraud Detection: Assessment and Visualization. Int J Data Sci Anal.
2018;5:285-300.
[3] VanVlasselaerV,BravoC,CaelenO,Eliassi-RadT,AkogluL,SnoeckM,BaesensB.APATE:
ANovel Approach for AutomatedCredit Card TransactionFraud Detection Using Network-
BasedExtensions.DecisSupportSyst.2015;75:38-48.
[4] ThangavelV.GlobalIdentificationofSmartCardTechnologies-SafeandSecure: AResearch.
2023.Availableat: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4460999
[5] Asha RB, KR SK. Credit Card Fraud Detection Using Artificial Neural Network. Global
TransitionsProceedings.2021;2:35-41.
[6] Dal Pozzolo A, Caelen O, Bontempi G. When Is Undersampling Effective in Unbalanced
Classification Tasks? In: Appice A, Rodrigues P, Santos Costa V, Soares C, Gama J, Jorge
A.editors,MachineLearningandKnowledgeDiscoveryinDatabases,SpringerInternational
Publishing.2015:200-215.
[7] Roy A, Sun J, Mahoney R, Alonzi L, Adams S, Beling P. Deep Learning Detecting Fraud in
Credit Card Transactions. In 2018 systems and information engineering design symposium
(SIEDS).IEEE.2018:129-134.
[8] Lavin A, Ahmad S. Evaluating Real-Time Anomaly Detection Algorithms–the Numenta
Anomaly Benchmark. In 2015 IEEE 14th international conference on machine learning and
applications(ICMLA).IEEE.2015:38-44.
[9] BhattacharyyaS,JhaS,TharakunnelK,WestlandJC.DataMiningforCreditCardFraud: A
ComparativeStudy.DecisSupportSyst.2011;50:602-613.
[10] SadgaliI,SaelN,BenabbouF.PerformanceofMachineLearningTechniquesintheDetection
ofFinancialFrauds.ProcediaComputSci.2019;148:45-54.
[11] Ngai EW, Hu Y, Wong YH, Chen Y, Sun X. The Application of Data Mining Techniques
in Financial Fraud Detection: A Classification Framework and an Academic Review of
Literature.DecisSupportSyst.2011;50:559-569.
[12] Dal Pozzolo A, Boracchi G, Caelen O, Alippi C, Bontempi G. Credit Card Fraud Detection:
A Realistic Modeling and a Novel Learning Strategy. IEEE transactions on neural networks
andlearningsystems.2017;29:3784-3797.
4002

https://www.oajaiml.com/|June2025 LailaAbd-Ellatif,etal.
[13] MolnarC.InterpretableMachineLearning.3rdedition.Lulu.com.2020.
[14] Thennakoon A, Bhagyani C, Premadasa S, Mihiranga S, Kuruwitaarachchi N. Real-Time
Credit Card Fraud Detection Using Machine Learning. In 2019 9th International Conference
onCloudComputing,DataScience&Engineering(Confluence).IEEE.2019:488-493.
[15] BoltonRJ,HandDJ.StatisticalFraudDetection: AReview.StatSci.2002;17:235-255.
[16] BaesensB,VanVlasselaerV,VerbekeW.FraudAnalyticsUsingDescriptive,Predictive,and
SocialNetworkTechniques: AGuidetoDataScienceforFraudDetection.JohnWiley&Sons.
2015.
[17] https://difusion.ulb.ac.be/vufind/Record/ULB-DIPOT:oai:dipot.ulb.ac.be:2013/221654/Details
[18] Shamsudin H, Yusof UK, Jayalakshmi A, Khalid MN. Combining Oversampling and
UndersamplingTechniquesforImbalancedClassification: AComparativeStudyUsingCredit
Card Fraudulent Transaction Dataset. In 2020 IEEE 16th international conference on control
&automation(ICCA).IEEE.2020:803-808.
[19] Nama FA, Obaid AJ. Financial Fraud Identification Using Deep Learning Techniques. Al-
SalamJEngTechnol.2024;3:141-147.
[20] Rahmati M. Real-Time Financial Fraud Detection Using Adaptive Graph Neural Networks
andFederatedLearning.IntJManagementandDataAnalytics.2025;5:98-110.
[21] LeCunY,BengioY,HintonG.DeepLearning.Nature.2015;521:436-444.
[22] Carcillo F, Dal Pozzolo A, Le Borgne YA, Caelen O, Mazzer Y, et al. Scarff: A Scalable
FrameworkforStreamingCreditCardFraudDetectionWithSpark.InfFusion.2018;41:182-
94.
[23] Almazroi AA, Ayub N. Online Payment Fraud Detection Model Using Machine Learning
Techniques.IEEEAccess.2023;11:137188-203.
[24] GoodfellowI,BengioY,CourvilleA,BengioY.DeepLearning.Cambridge.MITpress.2016.
[25] AhmedM,MahmoodAN,IslamMR.ASurveyofAnomalyDetectionTechniquesinFinancial
Domain.FutureGenerComputSyst.2016;55:278-88.
[26] Bello HO, Ige AB, Ameyaw MN. Adaptive Machine Learning Models: Concepts for Real-
Time Financial Fraud Prevention in Dynamic Environments. World J Adv Eng Technol. Sci.
2024;12:21-34.
[27] NajadatH,AltitiO,AqoulehAA,YounesM.CreditCardFraudDetectionBasedonMachine
andDeepLearning.In202011thInternationalConferenceonInformationandCommunication
Systems(ICICS).2020:204-208.IEEE.
[28] Chawla NV, Bowyer KW, Hall LO, Kegelmeyer WP. Smote: Synthetic Minority Over-
SamplingTechnique.JArtifIntellRes.2002;16:321-357.
4003