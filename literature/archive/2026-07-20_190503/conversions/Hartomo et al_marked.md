Received9December2024,accepted6February2025,dateofpublication13February2025,dateofcurrentversion20February2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3541878
A Novel Weighted Loss TabTransformer
Integrating Explainable AI for Imbalanced
Credit Risk Datasets
KRISTOKODWIHARTOMO 1,CHRISTIANARTHUR 2,ANDYESSICANATALIANI 1
1FacultyofInformationTechnology,SatyaWacanaChristianUniversity,Salatiga50711,Indonesia
2SchoolofTransdisciplinary,UniversityofTechnologySydney,Ultimo,NSW2007,Australia
Correspondingauthor:ChristianArthur(arthur@terabyteai.com)
ThisworkwassupportedinpartbytheVice-RectorofResearch,Innovation,andEntrepreneurshipatSatyaWacanaChristianUniversity
throughtheArticleWritingBootcampProgramandInternalResearchGrant.
ABSTRACT Credit risk assessment often faces significant challenges due to class imbalance and the
opaquenatureofmachinelearningmodels,whichcanresultinbiasedpredictionsandhindertrustamong
stakeholders.Toaddresstheseissues,thisstudyproposesaframeworkcombiningtheTabTransformermodel
withweightedlosstechniquestobalanceclassdistributionsandimprovepredictiveaccuracy.Appliedtothe
BISAID and German Credit datasets, the method demonstrated notable improvements in accuracy, from
86.35%to89.27%and93%to95%,respectively,alongwithimprovedminorityclassAUCandprecision-
recall metrics. To ensure transparency and interpretability, SHAP (SHapley Additive exPlanations) was
employed,highlightingcriticalpredictorssuchas‘‘FinancingNeeds’’and‘‘CreditAmount.’’Byintegrating
fairness mechanisms through weighted loss and explainability via XAI, the proposed framework and
weightedlossTabTransformermitigatebias,enhancemodelperformance,andprovideactionableinsights
forborrowersandstakeholders.Thesefindingsestablishareliable,equitable,andtransparentapproachto
creditevaluation.
INDEXTERMS Classimbalance,creditriskassessment,deeplearning,classification,explainableartificial
intelligence.
I. INTRODUCTION which impose higher interest rates and reduce competitive-
Creditriskassessmentisacriticalprocessthatappliestoall ness and profitability [6]. Beyond MSMEs, access to credit
borrowers,rangingfromindividualstobusinesses,including is a critical issue for many types of borrowers in Indonesia,
micro,small,andmediumenterprises(MSMEs).InIndone- reflecting broader challenges in financial inclusivity. In this
sia,MSMEsformastrategicsectorthatsupportsthenational context, cooperatives and innovative financial technologies
economy, comprising 65.46 million units, which is signif- playavitalroleinbridgingthegap,providingaffordableand
icantly higher than Thailand’s 3.1 million and Malaysia’s accessiblefinancingoptionsforbothindividualandbusiness
1.2 million units [1], [2]. This sector contributes 60.3% of borrowers[7].
Indonesia’sGrossDomesticProduct(GDP),employs97%of The problem of limited financial access for borrowers
theworkforce,andaccountsfor14.4%ofnationalexports[3]. is rooted in the issue of information asymmetry, which
Despite their economic importance, MSMEs often face arisesduetotheunequaldistributionofinformationbetween
obstacles in accessing formal business financing through borrowers and financial institutions. This asymmetry arises
commercial or rural banks [4], [5]. Weak access to formal from unequal information distribution, allowing borrowers
funding drives many MSMEs to rely on informal funds, to obscure or manipulate information (adverse selection) or
misuse credit (moral hazard) [8], [9]. In developing coun-
The associate editor coordinating the review of this manuscript and tries, the risk of financial information asymmetry is more
prevalentcomparedtodevelopednations[10].Asignificant
approvingitforpublicationwasSawyerDuaneCampbell .
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME13,2025 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 31045

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
factor contributing to this asymmetry is the lack of audited Tocounterthis,theuseofweightedlossduringmodeltrain-
financial statements from borrowers, which makes it chal- ing assigns greater importance to minority classes, such as
lenging for formal financial institutions to evaluate their defaults, allowing the model to better capture high-risk pat-
creditworthiness. The Bank of Indonesia has developed a ternsthatmightotherwisebeoverlooked.Thisapproachnot
database profiling MSMEs, and the Statlog German credit only improves the model’s accuracy but also ensures that
approval dataset (containing 1,000 instances) is available in XAI outputs remain reliable and unbiased. When minority
theUCIMachineLearningRepository[11].Theseresources classesareunderrepresented,XAIinterpretationscanbecome
aim to assist financial institutions in reducing information skewed,highlightingtrendsinthemajorityclasswhileunder-
asymmetry. However, challenges persist in effectively ana- emphasizing critical risk indicators present in the minority.
lyzingandutilizingthisdata[12]. Therefore,integratingweightedlosswithXAIenhancesboth
With the use of various tools to address the prob- predictive accuracy and interpretability, providing financial
lem, Machine Learning methods have been of particular institutionswithbalanced,transparentinsightsthatareessen-
importance. Some studies indicate that lending analytics tialforfairandeffectiveMSMEcreditevaluations.
usingMLtechniquesispossible[13],[14].However,thereis Themainresearchproblemcentersonthedifficultyfinan-
asignificantlimitationinmanyconventionalMLapproaches: cial institutions face in evaluating the creditworthiness due
they are not interpretable; people tend to refer to them as to significant information asymmetry. Despite the availabil-
‘black boxes’ which make predictions but do not illustrate ity of structured data from platforms like BISAID, many
howthepredictionwasmade[15].Thislackofthinkingmay MSMEs lack audited financial statements, making it chal-
create a situation where trust and responsibility in the auto- lenging for lenders to accurately assess credit risk. This
matic evaluation of a borrower’s creditworthiness becomes asymmetry—where lenders and borrowers possess unequal
infeasible. Some ML techniques also have some problems knowledgeaboutfinancialhealth—createshigherperceived
suchasoverfitting[16],wheremodelsdevelopedintraining risksforfinancialinstitutions,hinderingtheirabilitytopro-
data are unable to generalize on unseen data [17]. Further vide adequate financing for borrowers and limiting their
complicating the situation is the fact that all the financial potential growth. In addition, financial institutions struggle
institutions have their unique policies and requirements for to determine the appropriate weighting of financial data
decidingtheeligibilityofaloanthusmakingitverydifficult during the credit decision-making process, leading to inef-
tocomeupwithastandardmodel.Theseproblemscreatean ficiency and inconsistency in assessments. Conventional AI
urge for new models that will not only improve predictive methods further complicate this issue by offering limited
performancebutalsoenableinstitutionstohaveinterpretable transparency,whichcanerodetrustamongMSMEsregarding
andflexiblemodelsthatsuitdifferentfinancialinstitutions. loandecisions.Toaddresstheseissues,thisresearchproposes
DeepLearningpresentsasolutiontothechallengesfaced a deep learning-based model that utilizes BISAID’s dataset
inassessingcreditworthinessduetoitsabilitytodetectpat- andGermanCreditdatasettomoreeffectivelyassesscredit-
ternsandtrendsinstructureddata,suchasthatprovidedby worthiness.ThemodelwillincorporateExplainableArtificial
BISAIDandtheGermancredit,asprovenbyotherresearch Intelligence(XAI)techniquestoclarifythefactorsinfluenc-
thatDLmethodsoftenoutperformtraditionalstatisticaland ingloandecisions,providingtransparencyforbothfinancial
machine learning approaches [18], [19], [20], [21], [22], institutionsandborrowers.Byestablishingaclearapproach
[23], [24]. It is essential to consider all relevant fac- to weighing financial indicators, the proposed method aims
tors influencing credit decisions, including unexpected toenhancetheefficiency,transparency,andfairnessofcredit
ones[25],[26]. The evolving paradigm of Deep Learn- assessments, fostering greater financial inclusivity for all
ing, Explainable Artificial Intelligence (XAI), has shown typesofborrowers.
significant advancements. XAI enables the explanation of
influentialfactorsinadetailedandhuman-readablemanner, II. RELATEDWORKS
providing insights into the rationale behind credit deci- A. CLASSIFICATIONAPPROACHESINDEEPLEARNING
sions [27], [28]. This capability enhances the quality of The development of classification methods in Deep Learn-
credit evaluations by formal financial institutions, mak- ing has evolved from traditional Neural Networks (NN) to
ing the MSME credit decision process more efficient and moresophisticatedarchitecturesaimedataddressingspecific
effective.Moreover,XAIhighlightsfactorsthatconventional challenges,suchasprocessingsequentialdataandimproving
AI approaches may overlook, which typically provide loan training efficiency [30]. Early classification tasks primarily
recommendations without clarifying the decision-making reliedonsimplefeed-forwardNeuralNetworks,whichcon-
factorsinvolved. sist of fully connected layers designed to capture patterns
Despitetheseadvancements,oneofthecriticalchallenges in input data through multiple hidden layers. While these
in applying deep learning and XAI to MSME credit assess- networkswereeffectiveinmanyapplications,theystruggled
ment lies in addressing data imbalance. In many cases, with time-series or sequential data due to their inability to
instancesofcreditdefaultaresignificantlylessfrequentthan retainthememoryofpastinputs[31],[32].
successfulcreditoutcomes,creatingaskeweddatasetthatcan To overcome this limitation, Recurrent Neural Networks
bias the model’s predictions toward the majority class [29]. (RNNs) were introduced [33], which allowed the model
31046 VOLUME13,2025

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
to retain information from previous inputs through hidden ofdefiniteproblemsorillnesses.Furthermore,theapproach
states. However, standard RNNs suffered from vanishing holds promise in dealing with natural language data where
gradient problems, which hindered their ability to capture commonwordscontributedisproportionatelytotrainingand
long-term dependencies. The Gated Recurrent Unit (GRU), rarer terms are more challenging to learn accurately. Thus,
asimplifiedversionoftheLSTM,wasdevelopedtomitigate weightedlosshelpsachievearicheroverallmodelthatmore
this issue by introducing gating mechanisms that control evenlyrepresentsthefullspectrumoflanguage.
the flow of information [34]. With the rise of e-commerce In two studies investigating the application of weighted
platforms for financial transactions, fraudsters also exploit loss on imbalanced datasets, namely for brain tumor and
these systems. Fraud prevention systems (FPSs) are often maize disease classification, each demonstrated signifi-
inadequate. The proposed method involves preprocessing, cant improvements in model performance metrics. The by
feature selection, and model training. Preprocessing uses LundbergandLee[44] showed that deep feature fusion and
discretization and min-max normalization, while GA-based weighted cross-entropy led to increases in accuracy, pre-
feature selection enhances model efficiency. A BiGRU-A- cision, and F-score by over 10% compared to standard
CapsNetmodelwasapplied,outperformingstandardBiGRU cross-entropy, with gains in minority classes. Furthermore,
and CapsNet, achieving 95.44% accuracy, and making it the study by Ahadianetal.[29] employed transfer learning
suitableforintrusiondetectionandfraudprevention[35]. alongside weighted loss to achieve nearly 90% accuracy,
The Transformer architecture, introduced by [36], addre- 88% precision, and a substantial increase in F-score, illus-
ssed these limitations by replacing recurrence with self- tratingtheeffectivenessofweightedlossinmitigatingclass
| attention | mechanisms, |     | allowing | the model | to process | entire | imbalance. |     |     |     |     |     |
| --------- | ----------- | --- | -------- | --------- | ---------- | ------ | ---------- | --- | --- | --- | --- | --- |
Theweightforeachclassw
sequencessimultaneously.Transformersdemonstratedsupe- i inweightedcross-entropyloss
rior performance in tasks requiring global context, such as isdeterminedby:
| NLP, and | also | proved | to be | more parallelizable, |     | signifi- |     |     |     |     |     |     |
| -------- | ---- | ------ | ----- | -------------------- | --- | -------- | --- | --- | --- | --- | --- | --- |
N
|                                                       |     |     |     |     |     |     |     |     | w = |     |     | (1) |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cantlyspeedinguptrainingtimesThisarchitecturehassince |     |     |     |     |     |     |     |     | i   |     |     |     |
N i
becomeastandardindeeplearningforvariousclassification
|             |         |            |              |            |              |     | where N represents | the total | samples | and          | N i the samples | in  |
| ----------- | ------- | ---------- | ------------ | ---------- | ------------ | --- | ------------------ | --------- | ------- | ------------ | --------------- | --- |
| tasks, such | as      | Autoformer | [37],        | which uses | Autocorrela- |     |                    |           |         |              |                 |     |
|             |         |            |              |            |              |     | class i, ensuring  | higher    | weights | for minority | classes.        | The |
| tion to     | enhance | long-term  | forecasting, | Vision     | Transformer  |     |                    |           |         |              |                 |     |
weightedcross-entropylossL
(ViT)[38],andHSI-BERT[39]forimageclassification. WeightedCross−EntropyLoss isthen
definedas:
| In recent     | years, | the TabTransformer |     | [40]         | has emerged  | as  |                             |     |     |     |                 |     |
| ------------- | ------ | ------------------ | --- | ------------ | ------------ | --- | --------------------------- | --- | --- | --- | --------------- | --- |
| an adaptation |        | of the Transformer |     | architecture | specifically |     |                             |     |     | C   |                 |     |
|               |        |                    |     |              |              |     |                             |     |     | X   | (cid:0) (cid:1) |     |
|               |        |                    |     |              |              |     | L WeightedCross−EntropyLoss |     | =−  | w   | ·y ·log yˆ      | (2) |
designed for tabular data, which often consists of a mix of i i i
| categoricalandnumericalfeatures.Extensiveexperimentson |     |     |     |     |     |     |     |     |     | i=1 |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
fifteenpubliclyavailabledatasetsshowthatTabTransformer (cid:0) yˆ(cid:1)
|                                                        |     |     |     |     |     |     | withC asclasscount,y | i   | astruelabels,and |     | i aspredicted |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | -------------------- | --- | ---------------- | --- | ------------- | --- |
| outperformsstate-of-the-artdeeplearningmethodsfortabu- |     |     |     |     |     |     | probabilities.       |     |                  |     |               |     |
lardatabyatleast1.0%onmeanAUC,whilematchingthe
C. EXPLAINABLEARTIFICIALINTELLIGENCE(XAI)
| performance | of  | tree-based | ensemble | models. | Additionally, |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | -------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
it is highly robust against missing and noisy data, offer- FORCLASSIFICATIONTASKS
ing improved interpretability through its learned contextual Explainable AI is a subdomain of artificial intelligence.
embeddings. In semi-supervised settings, an unsupervised Itdealswiththedevelopmentoftechniquesthatprovidemore
pre-trainingprocedurefurtherenhancesperformance,leading interpretable and understandable machine learning models,
especiallythoseusingdeeplearningapproaches[41].While
toanaverage2.1%AUCimprovement.
thesemodelshavecontinuedtoincreaseincomplexity,their
B. WEIGHTEDCROSS-ENTROPYLOSS decision-making processes often resemble ‘‘black boxes’’
Weighted loss serves as a well-regarded approach to han- andmakeexplanationsofthepredictiveresultsquitedifficult.
dledisproportionamongcategorieswithinmachinelearning XAI addresses this issue by providing insights into which
duties, specifically in categorization difficulties where the featuresinfluencedamodel’sdecision,offeringmuch-needed
distribution of groups is uneven. Such a lack of balance, transparency in high-stakes fields like healthcare, finance,
which arises when certain groupings are underrepresented, and legal applications [42]. Various approaches have been
can guide model prejudice where the classifier favors developed to provide explanations for classification tasks.
more recurrent groupings, eventually reducing execution on ArepresentativemethodisLIME,whichexplainsindividual
minority clusters [41]. To counteract this, weighted penalty predictionsbyapproximatingcomplexsystemswithsimpler,
functions allocate higher punishments to scant groupings, more interpretable models, such as linear classifiers, acting
consequently stabilizing the effect of each grouping on the locally around the instance in question [43]. On the other
model’s studying method. Weighted penalty functions have hand, SHAP is a powerful method based on game theory,
been applied efficiently in domains for instance healthcare which assigns a Shapley value to each feature for quantify
imagery [42] and agriculture [41], [43], where class dis- its contribution to a prediction [44]. SHAP is frequently
tributions are often imbalanced owing to the unusualness used in the context of tabular data classification, providing
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     | 31047 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
detailedinsightsintohowindividualfeaturescontributetoa D. TheSHAPvalueforafeatureiiscalculatedusingthe
model’spredictionbyassigningeachfeatureaShapleyvalue, followingformula:
ensuringtransparencyandinterpretability[45]. TheSHAPvalueforafeatureiiscalculatedusingthefollow-
| The XAI | technique, | Anchors, | explains |     | by identifying |     | ingformula: |     |     |     |     |
| ------- | ---------- | -------- | -------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- |
specific conditions or rules that invariably lead to similar |S|!·(|N|−|S|−1)!
X
predictions,thusprovidingahighdegreeofprecision,explain φ = [f (S∪{i})−f (S)]
|                |          |            |     |       |                 |     | i   |     | |N|! |     |     |
| -------------- | -------- | ---------- | --- | ----- | --------------- | --- | --- | --- | ---- | --- | --- |
| by identifying | specific | conditions | or  | rules | that invariably |     |     |     |      |     |     |
S⊆N\{i}
lead to similar predictions, thus providing a high degree of (3)
| precision | [43]. An | alternative | methodology |     | involves | coun- |     |     |     |     |     |
| --------- | -------- | ----------- | ----------- | --- | -------- | ----- | --- | --- | --- | --- | --- |
where:
| terfactual | explanations, | which | emphasize | the | provision | of  |     |     |     |     |     |
| ---------- | ------------- | ----- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- |
substitute inputs that would lead to divergent outcomes, • N isthesetofallfeatures.
therebyillustratinghowminormodificationsintheinputcan S isasubsetoffeaturesnotcontainingfeaturei.
•
(S)isthemodel’spredictionforthesetoffeaturesS.
| influence | the prediction | [46]. | Methods | that | assess | feature | • f |     |     |     |     |
| --------- | -------------- | ----- | ------- | ---- | ------ | ------- | --- | --- | --- | --- | --- |
importancearefrequentlyappliedwithintree-basedmodels, • φ is the Shapley value for feature i, representing its
i
such as Random Forests, allocating scores to each input contributiontothemodel’soutput.
| feature according | to  | their | impact on | the accuracy |     | of the |     |     |     |     |     |
| ----------------- | --- | ----- | --------- | ------------ | --- | ------ | --- | --- | --- | --- | --- |
model’spredictions[47].Similarly,saliencymaps,originally
|     |     |     |     |     |     |     | III. PROPOSEDMETHOD |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- |
designed for image processing tasks, compute the gradient Figure1illustratesthedeeplearningpipelineforloanaccep-
of the output with respect to each input feature, highlight- tance rate prediction using the BISAID and German Credit
|           |          |           |                |     |             |     | datasets. | The process | begins with | data collection, | followed |
| --------- | -------- | --------- | -------------- | --- | ----------- | --- | --------- | ----------- | ----------- | ---------------- | -------- |
| ing which | parts of | the input | most influence |     | the model’s |     |           |             |             |                  |          |
decision[48]. bypreprocessingstepssuchasfeatureengineering(e.g.,data
Most of the approaches in XAI generally fall into imputation,one-hotencoding),normalization,anddatasplit-
two distinct categories: model-agnostic and model-specific. ting(80%training,20%testing).TheTabTransformermodel,
ExamplesareLIMEandSHAP,model-agnosticapproaches enhanced with a weighted loss function to address class
imbalance,servesasthecorearchitecture,undergoinghyper-
| that are versatile | because |     | they apply | to any | type of | mach- |     |     |     |     |     |
| ------------------ | ------- | --- | ---------- | ------ | ------- | ----- | --- | --- | --- | --- | --- |
ine learning model. Model-agnostic approaches, such as parametertuningandmultipleevaluationstoensureaccurate
Grad-CAMandfeatureimportanceassociatedwithdecision predictions. Post-modeling, Explainable AI (XAI) tech-
trees,areinherentlytiedtospecificmodelarchitecturesand niques, specifically Shapley values, are applied to interpret
provideinsightsspecifictotheirinnerworkings.Incontrast, predictions, providing local explanations for borrowers to
understandthefactorsinfluencingtheirloanoutcomes.
model-agnostictechniquessuchasSHAPareoftenpreferred
| because they | generalize | across | a wide | array | of models | in a |     |     |     |     |     |
| ------------ | ---------- | ------ | ------ | ----- | --------- | ---- | --- | --- | --- | --- | --- |
consistent manner, enabling consistent explanations regard- A. DATACOLLECTING
less of the underlying model architecture. SHAP stands in The data is retrieved from the BISIAID database, con-
a unique position because the theoretical foundation behind taining various features related to MSME profiles such as
| it in cooperative | game | theory | enables | fair and | reproducible |     |        |                        |     |         |            |
| ----------------- | ---- | ------ | ------- | -------- | ------------ | --- | ------ | ---------------------- | --- | ------- | ---------- |
|                   |      |        |         |          |              |     | SEKTOR | (sector), TENAGA_KERJA |     | (number | of employ- |
feature attribution, ensuring that all feature contributions ees), TOTAL_ASET (total assets), PENJUALAN_TAHUN
collectively equal the model’s predicted output. Therefore, (annualsales),andKEBUTUHAN_PEMBIAYAAN(financ-
SHAP can be an effective tool to explain individual pre- ingneeds).Thesefeaturesareessentialfortrainingthemodel,
dictions and understand the overall behavior of models. which is designed to predict loan acceptancerates based on
VariousstudieshavehighlightedtheeffectivenessofSHAPin criteriaverifiedbyofficialBankofIndonesia.Meanwhile,the
tasksliketabulardataclassification.Forexample,[49]used GermanCreditdatasetincludesattributeslikeage,jobtype,
SHAP to explain tree ensemble models in healthcare, pro- housing status, credit amount, and loan duration, focusing
vidinginsightsintohowpatientfeaturesimpacteddiagnosis on individual credit profiles. Together, these datasets offer
predictions. Reference [50] applied SHAP to cybersecurity acomprehensivefoundationforreducinginformationasym-
anomalydetection,identifyingthekeyfeaturesdrivingmali- metryandtrainingpredictivemodels.
ciousactivitydetection.Similarly,[51]demonstratedSHAP’s
value in finance, explaining credit risk predictions by high- B. DATAPREPROCESSING
lighting important customer features like income and credit ThePreprocessingDataphaseisacrucialstepthattransforms
history. In telecommunications, [52] used SHAP for churn raw data into a form suitable for machine learning models.
prediction,identifyingfactorssuchasserviceusageandcon-
|     |     |     |     |     |     |     | This process | begins with | feature | engineering, | where vari- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- | ------- | ------------ | ----------- |
tractdurationthatinfluencecustomerretention.Lastly,[53] ous transformations are applied, including data imputation
employed SHAP in fraud detection within banking, clarify- (addressing missing values), one-hot encoding (converting
ing how transaction patterns and account history contribute categorical variables into binary format), and discretization
to flagging suspicious activities. These examples illustrate (segmentationofcontinuousvariablesintodiscreteintervals).
SHAP’sversatilityandeffectivenessindeliveringactionable
Thesetechniquesensurethatthedatacanbeeffectivelyinter-
insightsacrossvariousclassificationtasks. pretedbythedeeplearningmodel.
| 31048 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
FIGURE1. ProposedframeworkutilizingTabTransformerandweightedlossforcreditriskpredictionandexplainability.
Following feature engineering, data normalization is per- complexfeaturedependenciesintabulardatasetswheretra-
formed to standardize feature ranges, ensuring consistent ditionalmodelsmaystruggle.
scaling across features to prevent any single feature from Theevaluationofclassificationmodelsgivesrisetovari-
disproportionatelyinfluencingthemodel.Inthisstudy,nor- ouskeymetricsthatcomefromtheconfusionmatrixwhich
malization is applied using a range of −1 to 1, which helps containsTruePositives(TP),FalsePositives(FP),TrueNega-
maintain numerical stability and improves model perfor- tives(TN),andFalseNegatives(FN).Thesecomponentsare
mance. Finally, the dataset is divided into training (80%) identified in the following sense: True Positives (TP) signs
and testing (20%) subsets, facilitating the model’s develop- representcasesinwhichthemodelaccuratelyidentifiespos-
mentandsubsequentevaluationonunseendatatoassessits itiveexamples,whereasFalsePositives(FP)occurwhenthe
generalizability. modelwronglydefinesanegativesampleaspositive.Incon-
trast, the True Negatives (TN) signify the model correctly
C. MODELTRAINING identifyinganegativesample,andtheFalseNegatives(FN)
Before initiating the model training process, class weights stand for the instances where the model wrongly classifies
were calculated as required for the weighted loss function, a positive sample as negative. By these basic concepts, key
with the formula for computing these weights provided in performancemetricsarederivedtodisclosethemodel’sper-
Equation 1. The Model Training phase employs the Tab- formanceindetail.
Transformer model. This approach offers a more effective Accuracy is a measure of the overall correctness of the
solution compared to traditional models, which often strug- modelandisdefinedastheproportionofcorrectlyclassified
gle with these relationships. Figure 2 demonstrates how instances(bothpositiveandnegative)overthetotalnumber
TabTransformer works, started by embedding categorical ofinstances.Theformulaisgivenby:
featuresandpassingthemthroughTransformerlayers,lever-
TP+TN
aging multi-head attention to capture complex interactions, Accuracy= (4)
TP+TN +FP+FN
whilenormalizedcontinuousfeaturesareconcatenatedwith
the Transformer output. This combined representation is Precision, also known as the positive predictive value,
processed by a Multi-Layer Perceptron (MLP) for predic- measures the proportion of true positive predictions among
tions,makingTabTransformeraversatilemodelforhandling all positive predictions made by the model. This metric
VOLUME13,2025 31049

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
|     |     |     |     |     | The training |              | process     | is iterative, | incorporating |               | hyperpa-    |
| --- | --- | --- | --- | --- | ------------ | ------------ | ----------- | ------------- | ------------- | ------------- | ----------- |
|     |     |     |     |     | rameter      | tuning       | to optimize | key           | parameters    | such          | as learning |
|     |     |     |     |     | rate, batch  | size,        | and         | attention     | heads.        | Multiple      | rounds of   |
|     |     |     |     |     | training     | and testing  | are         | conducted     | to            | enhance       | the model’s |
|     |     |     |     |     | predictive   | performance. |             | The model’s   |               | effectiveness | will be     |
graduallyevaluatedusingmetricsoutlinedinEquations4-7.
D. XAIPOST-MODELING
|     |     |     |     |     | Following | the | model’s | development, |     | the XAI | (Explainable |
| --- | --- | --- | --- | --- | --------- | --- | ------- | ------------ | --- | ------- | ------------ |
ArtificialIntelligence)Post-Modelingphaseisimplemented
|     |     |     |     |     | to provide   | transparency |             | and interpretability |     |             | of the model’s |
| --- | --- | --- | --- | --- | ------------ | ------------ | ----------- | -------------------- | --- | ----------- | -------------- |
|     |     |     |     |     | predictions. | In           | this phase, | model-agnostic       |     | techniques, | such           |
|     |     |     |     |     | as Shapley   | values,      | are         | applied              | to  | offer       | both local and |
globalexplanationsofthemodel’sdecision-makingprocess.
|     |     |     |     |     | Shapley       | values, | rooted     | in cooperative |       | game | theory, allocate |
| --- | --- | --- | --- | --- | ------------- | ------- | ---------- | -------------- | ----- | ---- | ---------------- |
|     |     |     |     |     | contributions | to      | individual | features       | based | on   | their influence  |
ontheprediction,providinginsightintohowspecificMSME
characteristics(e.g.,creditscore,businesstenure)affectloan
acceptanceprobability.
IV. RESULTSANDDISCUSSIONS
A. DATACOLLECTING
FIGURE2. TabTransformerarchitecturebyHuangetal.[40]. Data in this study was collected from an official gov-
|     |     |     |     |     | ernment   | website    | that | has been    | managing | this        | information |
| --- | --- | --- | --- | --- | --------- | ---------- | ---- | ----------- | -------- | ----------- | ----------- |
|     |     |     |     |     | since its | inception. | In   | this study, | the      | researchers | obtained    |
is particularly important in contexts where the cost of false 2563 records, each with 12 features. Among these features,
positivesishigh.Precisioniscomputedas:
|     |     |     |     |     | five were | removed      | because | they         | contained |       | only identity- |
| --- | --- | --- | --- | --- | --------- | ------------ | ------- | ------------ | --------- | ----- | -------------- |
|     |     |     |     |     | related   | information, | such    | as reference |           | code, | research year, |
TP
|     | Precision= |     |     | (5) |           |       |     |        |               |     |                |
| --- | ---------- | --- | --- | --- | --------- | ----- | --- | ------ | ------------- | --- | -------------- |
|     |            |     |     |     | and owner | name, | and | so on. | The remaining |     | features are a |
TP+FP
mixtureofcategoricalandnumericaldata,whichisidealfor
High precision indicates that the model makes few false theTabTransformerarchitecture,asshowninTable1.
| positive errors, | which is | crucial in | domains | such as fraud |     |     |     |     |     |     |     |
| ---------------- | -------- | ---------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
detectionormedicaldiagnosis,whereincorrectpositivepre-
TABLE1. BISAIDdatasetfeaturetypesanddescriptions.
dictionscanbecostly.
| Recall,           | also referred | to as sensitivity  | or the       | true positive   |     |     |     |     |     |     |     |
| ----------------- | ------------- | ------------------ | ------------ | --------------- | --- | --- | --- | --- | --- | --- | --- |
| rate, quantifies  | the model’s   | ability            | to correctly | identify all    |     |     |     |     |     |     |     |
| relevant positive | cases.        | It is particularly | useful       | in scenarios    |     |     |     |     |     |     |     |
| where the         | cost of false | negatives is       | high, as     | it reflects the |     |     |     |     |     |     |     |
proportionofactualpositiveinstancesthatarecorrectlyiden-
tifiedbythemodel.Recallisdefinedas:
TP
Recall=
(6)
TP+FN
F2 Score is a variant of the F-measure, which provides a In the German Credit dataset, a total of 1,000 instances
|                 |              |                |          |            | were obtained, |          | each containing |              | twice | as many | features per    |
| --------------- | ------------ | -------------- | -------- | ---------- | -------------- | -------- | --------------- | ------------ | ----- | ------- | --------------- |
| balance between | precision    | and recall.    | However, | unlike the |                |          |                 |              |       |         |                 |
|                 |              |                |          |            | instance       | compared | to              | the features | in    | other   | datasets. These |
| F1 score,       | the F2 score | places greater | emphasis | on recall, |                |          |                 |              |       |         |                 |
makingitmoresuitableinsituationswherefalsenegativesare featureswerealsocomparedwithdatafromBISAID,which
demonstratedfewervariationsinfeaturecategories.Specifi-
morecriticalthanfalsepositives.TheF2scoreiscalculated
asfollows: cally,onlythe‘‘purpose’’featureexhibited10uniquevalues,
whiletheremainingfeaturesrangedfrom5,4,3,to2unique
5×Precision×Recall
|     | F2= |     |     |     | values,aspresentedinTable2. |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
(7)
4×Precision+Recall
These metrics provide a comprehensive evaluation fra- B. DATAPREPROCESSING
mework for TabTransformer model, helping to assess its The primary objective of this research is to examine the
effectiveness in handling tabular data classification tasks, featuresidentifiedbytheTabTransformermodel.Beforethe
particularlywithcomplexfeatureinteractions. dataisprocessedbythemodel,itiscompulsorytoensurethat
| 31050 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
TABLE2. Germancreditdatasetfeaturetypesanddescriptions. majorityclassandsupportingfairevaluationoftheweighted
lossperformanceduringinferencewithXAI.
| the dataset | is consistent, | particularly | in terms of numerical |     |     |     |     |     |
| ----------- | -------------- | ------------ | --------------------- | --- | --- | --- | --- | --- |
data.Tominimizebiasacrossthetraining,validation,andtest FIGURE4. GermanCreditclassdistributionacrossdatasetsplits.
| sets, class | distributions | must be balanced. | Accordingly, | this |     |     |     |     |
| ----------- | ------------- | ----------------- | ------------ | ---- | --- | --- | --- | --- |
studyemploysadatasplitratioof80:10:10fortraining,vali-
dation,andtesting,respectively.Figure3depictsthepartition C. MODELTRAINING
of the train, validation, and test sets, showing the balanced Beforetrainingthemodel,theWeightedClassLossmustbe
distributionofclasses.Eachbarinthefigureissegmentedto configured first. In this study, the author uses the original
|     |     |     |     | dataset distribution | prior | to splitting | it into | various sub- |
| --- | --- | --- | --- | -------------------- | ----- | ------------ | ------- | ------------ |
representtheproportionofeachclass(0,1,2,and3)within
the respective datasets. The colors—blue for class 0, green sets, as shown in the first figure. In the dataset containing
for class 1, yellow for class 2, and red for class 3—clearly 2563samples,thedistributionofclassesfrom0to3is379,
illustratetheclassdistributionacrossallsubsets,ensuringno 1146, 539, and 499, respectively. Table 3 shows the results
biasisintroducedduringthedatasplittingprocess. of the calculation based on Equation (1), where Class 1 has
thesmallestpenalty(2.2364)duetobeingthemajorityclass.
|     |     |     |     | In contrast, | the minority | class, Class | 0, has | the highest |
| --- | --- | --- | --- | ------------ | ------------ | ------------ | ------ | ----------- |
weight(6.7625),asthemodelisrarelyexposedtothisclass.
|     |     |     |     | The same | principle applies | to the | German Credit | Dataset, |
| --- | --- | --- | --- | -------- | ----------------- | ------ | ------------- | -------- |
whereClass1(Good)hasalowerweightcomparedtoClass0
|     |     |     |     | because | Class 0 is the | minority. Therefore, |     | the penalty is |
| --- | --- | --- | --- | ------- | -------------- | -------------------- | --- | -------------- |
higher,asdescribedintheformula,ensuringthemodelpays
moreattentiontothisclass.Thisweightingschemewilllater
beappliedtothelossfunction,asdetailedinEquation(2).
|     |     |     |     | TABLE3. | Weightedlosscalculationforeachdataset’sclasses. |     |     |     |
| --- | --- | --- | --- | ------- | ----------------------------------------------- | --- | --- | --- |
FIGURE3. BISAIDclassdistributionacrossdatasetsplits.
The German Credit dataset, obtained from the UCI After class weighting using Weighted Class Loss, the
Machine Learning Repository, consists of two classes: next step is hyperparameter tuning on the TabTransformer,
Class0andClass1.AsshowninFigure4,Class0represents considering accuracy, precision, and recall as the main
‘‘bad customers’’ with 300 instances, while Class 1 repre- metrics, evaluated using 10-fold cross-validation, as shown
sents ‘‘good customers’’ with 700 instances. To maintain in Table 3. The selected for BISAID dataset hyperparame-
consistencyacrossthetraining,validation,andtestdatasets, ters are dim=128, dim_out = 4, depth = 1, heads = 2,
the same 80:10:10 data split ratio as used in BISAID was attn_dropout = 0.1, and ff_dropout = 0.1. The feature
applied, as shown in Figure 3. The distribution within each dimension(dim)wasincreasedto128fromthepaperrecom-
setwasensuredtobeconsistent,preventingbiastowardthe mendation(32)tocapturemorecomplexpatternsasthedata
| VOLUME13,2025 |     |     |     |     |     |     |     | 31051 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ----- |

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
| contains | more categorical |     | unique | values, | while the | output |
| -------- | ---------------- | --- | ------ | ------- | --------- | ------ |
dimension(dim_out)wasadjustedtothenumberofclasses4
(Multiclass)forBISAIDdatasetand2(Binary)forGerman
Creditdataset.Thedepthwassetto1,lowerthantherecom-
mendation(6),andthenumberofattentionheadswasreduced
to2from8toreducecomputationalcomplexity.
| The dropout           | for         | the attention      |          | mechanism | (attn_dropout) |           |
| --------------------- | ----------- | ------------------ | -------- | --------- | -------------- | --------- |
| and feed-forward      |             | layer (ff_dropout) |          | were      | set to         | 0.1 each  |
| to prevent            | overfitting | without            | reducing | the       | model          | capacity. |
| These hyperparameters |             | were               | chosen   | based     | on experiments |           |
| showing               | that this   | combination        |          | provides  | the best       | balance   |
betweenperformanceandefficiency.
TABLE4. TabTransformerhyperparametersettings.
Aftercompletingtheclassweightinitializationandselect-
| ing the      | best hyperparameters |     | during   | the     | tuning phase, | the      |
| ------------ | -------------------- | --- | -------- | ------- | ------------- | -------- |
| next step    | is to train          | the | model.   | In this | phase, Table  | 2 is     |
| consistently | referenced           | in  | Equation | (2), as | are the       | hyperpa- |
rametersinTable4.Duringthetrainingprocessresearchers
usedmini-batchwithbatchsize64asrecommendedstudyby
Ioffe[54].Figure5presentsacomparisonofthelossbetween
| the training | data | and the | validation | data. | Additionally, | the |
| ------------ | ---- | ------- | ---------- | ----- | ------------- | --- |
FIGURE5. TrainvsVallossforBISAIDdataset(A)Beforeweighted(B)
evaluationateachepochshowsconsistentfluctuations,indi- Afterweightedloss.
| cating that | the model | struggles | to  | manage | the effects | of the |
| ----------- | --------- | --------- | --- | ------ | ----------- | ------ |
imbalanced class distribution during training. On the other Beyond addressing data imbalance, the evaluation also
hand,Figure1Bshowsamorestabletrainloss,eventhough tests the model with different features. Furthermore, the
it started with a higher initial loss and experienced a few study incorporates both binary (two-class) and multi-class
spikesbetweenepochs0and40.Beyondthisrange,theloss classificationstoanalyzetheimpactofweightedlosscompre-
remainedstableduetotheimplementationofweightedloss, hensively.Thetabledemonstratestheimprovementsbrought
whichhelpedaddresstheclassimbalanceeffectively. by the weighted loss. Notably, class 0 shows an increase in
Similarly, in the German Credit dataset, a similar pattern precision, albeit with a slight dip in recall. Class 1 and 3
is observed in Figure 5. In Figure 5 (a), the model behaves exhibitconsistentgainsacrossallmetrics,reflectingthepos-
differentlycomparedtotheBISAIDdataset.Boththetrain- itiveimpactoftheweightedlossonperformance.However,
ing and validation loss curves are spiky, with the model class 2 sees a trade-off with a slight drop in precision but a
showing signs of near-overfitting across more epochs. The significantgaininrecall,improvingitsoverallF1-score.The
rapid decline in validation loss indicates that, if training is increaseinoverallaccuracyfrom86%to89%furtherunder-
continued,overfittingishighlylikely.Incontrast,Figure6(b) scorestheeffectivenessoftheweightedlossinenhancingthe
demonstratestheeffectofweightedloss,whichsmoothsboth model’s performance to keep aware about minority classes,
the training and validation curves. Additionally, it shows a particularlyinhandlingmulticlassimbalance.
similar behavior where the initial loss values are generally Figure 7 presents the additional evaluation results using
highercomparedtotrainingwithoutweightedloss. the ROC (Receiver Operating Characteristic) Curve for the
After training the model using weighted loss, the evalu- four classes. The minority classes (2 and 3) show notice-
ation phase begins, leveraging the previously trained data. able improvement in AUC, increasing from 0.88 to 0.91
Inthisphase,aclassificationreportascanbeseeninTable5 and 0.86 to 0.91, respectively. For the remaining classes
is generated for each class, providing accuracy, precision, (0 and 1), Class 0 shows minimal change, with weighted
and recall metrics. This approach ensures a fair assess- and non-weighted models differing by only 0.1, where the
ment of the effectiveness of the weighted loss method. non-weighted model slightly outperforms. The majority
31052 VOLUME13,2025

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
FIGURE7. ROCcurvescomparingweightedandnon-weightedmulticlass
modelperformanceonBISAIDdatabase.
racyof93%.However,theminorityclass(Class0)suffered
|     |     |     |     | from low   | precision,   | resulting       | in           | a reduced | F1-score,          | which      |
| --- | --- | --- | --- | ---------- | ------------ | --------------- | ------------ | --------- | ------------------ | ---------- |
|     |     |     |     | indicates  | room         | for improvement |              | in        | handling           | imbalanced |
|     |     |     |     | datasets.  | Our research |                 | incorporates |           | the TabTransformer |            |
|     |     |     |     | model with | a weighted   | binary          | entropy      |           | loss function,     | which      |
hasdemonstratedsignificantimprovementsinperformance.
|     |     |     |     | Not only | did the     | overall | accuracy | increase | from | 93% to    |
| --- | --- | --- | --- | -------- | ----------- | ------- | -------- | -------- | ---- | --------- |
|     |     |     |     | 95%, but | all metrics | across  | both     | classes  | also | improved. |
Specifically,precision,recall,andF1-scorefortheminority
|     |     |     |     | class (Class | 0) rose | from | 0.85, 0.93, | and | 0.89 to | 0.88, 0.97, |
| --- | --- | --- | --- | ------------ | ------- | ---- | ----------- | --- | ------- | ----------- |
and0.92,respectively.Importantly,theseenhancementswere
|     |     |     |     | achieved | without | sacrificing | the | precision | or recall | of the |
| --- | --- | --- | --- | -------- | ------- | ----------- | --- | --------- | --------- | ------ |
FIGURE6. TrainvsVallossforGermanCreditdataset(A)Beforeweighted majority class (Class 1), which improved from an F1-score
(B)Afterweightedloss. of 0.95 to 0.96. These findings illustrate that the weighted
|     |     |     |     | loss function | is  | an effective | solution |     | for addressing | class |
| --- | --- | --- | --- | ------------- | --- | ------------ | -------- | --- | -------------- | ----- |
TABLE5. Classificationmetricscomparisonbeforeandafterapplying imbalances in binary classification tasks. By ensuring fair
weightedlossonBISAIDdataset. improvementsacrossallmetricswithoutdegradingmajority
classperformance.
TABLE6. Classificationmetricscomparisonbeforeandafterapplying
weightedlossonGermanCreditdataset.
class,however,improvesmodestlyfrom0.88to0.90.These
| results indicate     | that the proposed | weighted transformer |       |     |     |     |     |     |     |     |
| -------------------- | ----------------- | -------------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| effectively enhances | sensitivity       | to minority classes  | while |     |     |     |     |     |     |     |
maintainingstrongperformanceformajorityclasses. Figure8demonstratesasimilarpatterntotheROCcurve
Table 6 presents a detailed comparison of model per- presented in Figure 7, where both figures illustrate the
formance using a classification report format. Initially, the model’s discriminative ability between positive and nega-
traditionalTabTransformermodel,integratedwithastandard tive classes. The ROC curve in Figure 8 shows consistent
binaryentropylossfunction,achievedarelativelyhighaccu- improvementsinsensitivityandspecificitycomparedtothe
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     | 31053 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
| baseline.         | In terms of     | AUC,         | our proposed | technique   | incor-         |     |     |     |     |     |
| ----------------- | --------------- | ------------ | ------------ | ----------- | -------------- | --- | --- | --- | --- | --- |
| porating          | weighted loss   | achieves     | an AUC       | of 0.96,    | compared       |     |     |     |     |     |
| to 0.91           | in the baseline | model.       | This         | improvement | highlights     |     |     |     |     |     |
| the effectiveness | of              | the proposed | method       | in          | distinguishing |     |     |     |     |     |
betweenclasses,leadingtoamorereliableandunbiasedpre-
dictionmodelinimbalancedclassscenarioswithoutaltering
thedistributionoftheclass.
FIGURE9. FeatureimportanceanalysiswithSHAPonBISAIDdataset.
|     |     |     |     |     |     | Account/Bonds | and Present | Employment | Status | contribute |
| --- | --- | --- | --- | --- | --- | ------------- | ----------- | ---------- | ------ | ---------- |
moderately.Lessimpactfulfeatures,suchasForeignWorker
|     |     |     |     |     |     | and Telephone, | have SHAP | values below | 0.02. | This analy- |
| --- | --- | --- | --- | --- | --- | -------------- | --------- | ------------ | ----- | ----------- |
FIGURE8. ROCcurvescomparingweightedandnon-weightedmulticlass sis highlights the importance of financial and demographic
modelperformanceonGermanCreditdatabase.
|     |     |     |     |     |     | factors in credit | risk prediction | and demonstrates |     | the inter- |
| --- | --- | --- | --- | --- | --- | ----------------- | --------------- | ---------------- | --- | ---------- |
pretabilityofthetransformer-basedmodelusingSHAP.
D. XAIPOST-MODELING
| After achieving | the | desired | accuracy | and mitigating | model |     |     |     |     |     |
| --------------- | --- | ------- | -------- | -------------- | ----- | --- | --- | --- | --- | --- |
biastowardthemajorityclass,theinferenceresultsbecome
| fair for | both majority | and minority | classes. | In  | this research, |     |     |     |     |     |
| -------- | ------------- | ------------ | -------- | --- | -------------- | --- | --- | --- | --- | --- |
explainableAI(XAI)methods,specificallySHAP(SHapley
| Additive        | exPlanations), | were     | employed   | to ensure | that fea-    |     |     |     |     |     |
| --------------- | -------------- | -------- | ---------- | --------- | ------------ | --- | --- | --- | --- | --- |
| ture importance | analysis       | remains  | unbiased.  | SHAP      | not only     |     |     |     |     |     |
| highlights      | the strong     | features | associated | with      | the majority |     |     |     |     |     |
classbutalsofairlyrepresentstheminorityclass,makingthe
methodvalidandtrustworthyforevaluatingfeaturecontribu-
tionsacrossallclasses.
| As shown    | in Figure        | 9, the    | feature | Financing    | Needs has  |     |     |     |     |     |
| ----------- | ---------------- | --------- | ------- | ------------ | ---------- | --- | --- | --- | --- | --- |
| the highest | SHAP value,      | averaging |         | around 0.65, | indicating |     |     |     |     |     |
| it is the   | most significant | predictor | in      | the model.   | Following  |     |     |     |     |     |
this,AnnualSalesandTotalAssetscontributeconsiderably,
| with average | SHAP | values | of approximately |     | 0.2 and 0.15, |     |     |     |     |     |
| ------------ | ---- | ------ | ---------------- | --- | ------------- | --- | --- | --- | --- | --- |
respectively.FeaturessuchasCityandLabourhavemoderate
| impacts, | with SHAP | values | near 0.1 | and 0.05, | respectively. |     |     |     |     |     |
| -------- | --------- | ------ | -------- | --------- | ------------- | --- | --- | --- | --- | --- |
Meanwhile,ProvinceandSectorshowtheleastcontribution,
|           |        |             |      |          |              | FIGURE10. FeatureimportanceanalysiswithSHAPonGermanCredit |     |     |     |     |
| --------- | ------ | ----------- | ---- | -------- | ------------ | --------------------------------------------------------- | --- | --- | --- | --- |
| with SHAP | values | below 0.05. | This | analysis | demonstrates |                                                           |     |     |     |     |
dataset.
| that the | model primarily   | relies | on financial | and    | operational    |     |     |     |     |     |
| -------- | ----------------- | ------ | ------------ | ------ | -------------- | --- | --- | --- | --- | --- |
| metrics, | such as financing | needs  | and          | annual | sales, to make |     |     |     |     |     |
predictions.Thelowercontributionsoffeatureslikeprovince This chapter emphasized the vital role of Explainable
and sector suggest that regional and industry-based factors ArtificialIntelligence(XAI)inensuringinterpretabilityand
havelessinfluenceinthiscontext. fairness in credit scoring models. Using SHAP (SHapley
Figure10showstheSHAP-basedfeatureimportanceanal- Additive exPlanations), key features such as ‘‘Financing
ysis for the German Credit dataset. Credit Amount is the Needs’’intheBISAIDdatasetand‘‘CreditAmount’’inthe
mostinfluentialfeature,withanaverageSHAPvalueof0.12, GermanCreditdatasetwereidentified,ensuringtransparency
followed by Age (years) and Status of Existing Credit, in predictions. Weighted loss techniques addressed class
with SHAP values of 0.09 and 0.08, respectively. Other imbalances,enablingfairrepresentationofminorityclasses.
significant features include Duration (months) and Credit TheintegrationofXAIwiththeTabTransformermodelpro-
History(SHAPvaluesaround0.07and0.05),whileSavings vided a robust framework for accurate and equitable credit
| 31054 |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
evaluations, highlighting the importance of interpretable AI [4] H. Górska-Warsewicz, M. Dębski, K. Rejman, and W. Laskowski,
inpromotingfairnessandtrustinfinancialdecision-making. ‘‘The specificity of family firms providing accommodation services—
|     |     |     |     |     |     |     | The experience |     | of a post-socialist |     | country30 | years after | the economic |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------------- | --- | --------- | ----------- | ------------ |
transformation,’’Sustainability,vol.12,no.24,p.10404,Dec.2020,doi:
V. CONCLUSION
10.3390/su122410404.
This research introduces a novel framework for credit risk [5] D.S.MareandW.Bank.(2016).TheNexusofFinancialInclusionand
assessment, integrating weighted loss techniques with the FinancialStability:AStudyofTrade-offsandSynergies.[Online].Avail-
able:https://www.researchgate.net/publication/304319907
| TabTransformer | model | to effectively |     | address | class | imbal- |     |     |     |     |     |     |     |
| -------------- | ----- | -------------- | --- | ------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
[6] U.Arzubiaga,A.DeMassis,A.Maseda,andT.Iturralde,‘‘Theinfluence
| ance and | enhance predictive |     | accuracy. | The | weighted | loss |     |     |     |     |     |     |     |
| -------- | ------------------ | --- | --------- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
offamilyfirmimageonaccesstofinancialresourcesinfamilySMEs:
approach,appliedtoimbalanceddatasetssuchasBISAIDand A signaling theory perspective,’’ Rev. Managerial Sci., vol. 17, no. 1,
pp.233–258,Jan.2023,doi:10.1007/s11846-021-00516-2.
| German | Credit, demonstrated |     | significant |     | improvements | in  |     |     |     |     |     |     |     |
| ------ | -------------------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[7] R.Arifin,A.Agus,T.Ningsih,andA.K.Putri,‘‘Theimportantroleof
performancemetrics.FortheBISAIDdataset,theapplication
MSMEsinimprovingtheeconomy,’’SouthEastAsiaJ.Contemp.Bus.,
of weighted loss increased overall accuracy from 86.35% Econ.Law,vol.24,no.6,pp.52–59,2021.
[8] J.J.Macha,Y.L.Chong,andI.C.Chen,‘‘Smallholderfarmers’intention
| to 89.27%, | with AUC | for minority |     | classes | improving | from |     |     |     |     |     |     |     |
| ---------- | -------- | ------------ | --- | ------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
toadoptmicrofinanceservicesinruralareasofTanzania–abehavioural
| 0.88 to 0.91. | Similarly, | in the | German | Credit | dataset, | accu- |          |         |             |            |            |             |            |
| ------------- | ---------- | ------ | ------ | ------ | -------- | ----- | -------- | ------- | ----------- | ---------- | ---------- | ----------- | ---------- |
|               |            |        |        |        |          |       | study,’’ | Int. J. | Bus. Innov. | Res., vol. | 19, no. 3, | p.304, Jan. | 2019, doi: |
racyimprovedfrom93%to95%,andminorityclassprecision 10.1504/ijbir.2019.100325.
andrecallrosefrom0.85and0.93to0.88and0.97,respec- [9] A.Moro,M.Fink,andD.Maresch,‘‘Reductionininformationasymmetry
andcreditaccessforsmallandmedium-sizedenterprises,’’J.Financial
tively. These enhancements ensured fairer representation of Res.,vol.38,no.1,pp.121–143,Mar.2015,doi:10.1111/jfir.12054.
minority classes while maintaining robust performance for [10] T.I.Eldomiaty,‘‘Determinantsofcorporatecapitalstructure:Evidence
majorityclasses. fromanemergingeconomy,’’Int.J.CommerceManage.,vol.17,no.1,
pp.25–43,Apr.2008,doi:10.1108/10569210710774730.
Buildingonthisfoundation,ExplainableArtificialIntelli- [11] P.Pławiak,M.Abdar,J.Pławiak,V.Makarenkov,andU.R.Acharya,
gence(XAI)techniques,specificallySHAP(SHapleyAddi- ‘‘DGHNL:Anewdeepgenetichierarchicalnetworkoflearnersforpre-
dictionofcreditscoring,’’Inf.Sci.,vol.516,pp.401–418,Apr.2020,doi:
| tive exPlanations), | were | incorporated |     | to avoid | bias | toward |     |     |     |     |     |     |     |
| ------------------- | ---- | ------------ | --- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
10.1016/j.ins.2019.12.045.
themajorityclassandmakepredictionsmoretransparentfor
[12] M.M.Ahmad,A.I.Hunjra,andD.Taskin,‘‘Doasymmetricinformation
borrowersandstakeholders.SHAPenabledtheidentification and leverage affect investment decisions?’’ Quart. Rev. Econ. Finance,
vol.87,pp.337–345,Feb.2023,doi:10.1016/j.qref.2021.05.001.
| of key features | such as | ‘‘Financing |     | Needs’’ | in the | BISAID |     |     |     |     |     |     |     |
| --------------- | ------- | ----------- | --- | ------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
[13] S.Shi,R.Tse,W.Luo,S.D’Addona,andG.Pau,‘‘Machinelearning-
datasetand‘‘CreditAmount’’intheGermanCreditdataset,
|     |     |     |     |     |     |     | driven | credit risk: | A systemic | review,’’ | Neural | Comput. Appl., | vol. 34, |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | ---------- | --------- | ------ | -------------- | -------- |
providing clear and interpretable insights into the factors no.17,pp.14327–14339,Sep.2022,doi:10.1007/s00521-022-07472-2.
|                |            |      |      |       |             |     | [14] M. Mahbobi, |     | S. Kimiagari, | and M. | Vasudevan, | ‘‘Credit risk | classifica- |
| -------------- | ---------- | ---- | ---- | ----- | ----------- | --- | ---------------- | --- | ------------- | ------ | ---------- | ------------- | ----------- |
| driving credit | decisions. | This | dual | focus | on fairness | and |                  |     |               |        |            |               |             |
tion:Anintegratedpredictiveaccuracyalgorithmusingartificialanddeep
transparencyaddressesthe‘‘blackbox’’natureoftraditional
neuralnetworks,’’Ann.OperationsRes.,vol.330,nos.1–2,pp.609–637,
machine learning models, fostering trust and accountability Nov.2023,doi:10.1007/s10479-021-04114-z.
inautomatedcreditevaluationsystems. [15] N.Bussmann,P.Giudici,D.Marinelli,andJ.Papenbrock,‘‘Explainable
|               |       |          |     |         |              |     | machine | learning | in credit | risk management,’’ |     | Comput. Econ., | vol. 57, |
| ------------- | ----- | -------- | --- | ------- | ------------ | --- | ------- | -------- | --------- | ------------------ | --- | -------------- | -------- |
| This research | opens | pathways | for | further | advancements |     |         |          |           |                    |     |                |          |
no.1,pp.203–216,Jan.2021,doi:10.1007/s10614-020-10042-0.
in AI-driven credit risk assessment. Future work can focus [16] V. Kanaparthi, ‘‘Credit risk prediction using ensemble machine learn-
on scaling to larger datasets, incorporating real-time finan- ingalgorithms,’’inProc.Int.Conf.InventiveComput.Technol.(ICICT),
Apr.2023,pp.41–47,doi:10.1109/ICICT57646.2023.10134486.
cialdata,andintegratingalternativecreditsources.Adaptive [17] Y. Zhong and H. Wang, ‘‘Internet financial credit scoring models
weightedlossmechanismscouldfurtherenhancemodelper- based on deep forest and resampling methods,’’ IEEE Access, vol. 11,
formance. Collaboration with financial institutions will be pp.8689–8700,2023,doi:10.1109/ACCESS.2023.3239889.
[18] A.Casolaro,V.Capone,G.Iannuzzo,andF.Camastra,‘‘Deeplearning
keyforreal-worldvalidation,ensuringcompliancewithreg-
fortimeseriesforecasting:Advancesandopenproblems,’’Information,
ulatorystandardswhilepromotingfairnessandtransparency vol.14,no.11,p.598,Nov.2023,doi:10.3390/info14110598.
[19] K.D.HartomoandC.Arthur,‘‘EnhancedMSMEsupportallocationwith
inautomatedcreditevaluations.
integratedK-meansandTukey’soutlierdetection,’’inProc.Intell.Syst.
ACKNOWLEDGMENT Appl.Cham,Switzerland:Springer,2024,pp.241–257.
|     |     |     |     |     |     |     | [20] C. Arthur |     | and K. | D. Hartomo, | ‘‘Enhancing | breast | cancer |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------ | ----------- | ----------- | ------ | ------ |
This research is partially supported by the Vice-Rector of prediction with an advanced K-nearest neighbors (KNN) algorithm
Research,Innovation,andEntrepreneurshipatSatyaWacana integrated with feedback support mechanism,’’ in Proc. Int. Conf.
Christian University through the Article Writing Bootcamp Technol., Eng., Comput. Appl. (ICTECA), Apr. 2024, pp.1–5, doi:
10.1109/ICTECA60133.2023.10491036.
programandinternalresearchgrant.
|     |     |     |     |     |     |     | [21] C. Arthur, | N.  | Yudistira,  | and C. | Dewi, ‘‘AutoCyclic: | Deep         | learning |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ------ | ------------------- | ------------ | -------- |
|     |     |     |     |     |     |     | optimizer       | for | time series | data   | prediction,’’       | IEEE Access, | vol. 12, |
REFERENCES pp.14014–14026,2024,doi:10.1109/ACCESS.2024.3356553.
[1] E. Setiawati, K. Hadi, P. R. K. Sari, I. Ariffianti, and I. G. Narung, [22] K. D. Hartomo and Y. Nataliani, ‘‘A new model for learning-based
‘‘SMEsbuildingthenationthroughawarenessofpayingtaxes,’’Valid, forecastingprocedurebycombiningk-meansclusteringandtimeseries
JurnalPengabdian,vol.1,no.3,pp.1–10,Aug.2023.[Online].Available: forecastingalgorithms,’’PeerJComput.Sci.,vol.7,p.e534,Jun.2021,
https://journal.stieamm.ac.id/vjp/article/view/307 doi:10.7717/peerj-cs.534.
[2] N. Muhammad. Micro Enterprises Still Dominate MSMEs, How [23] K.D.Hartomo,S.Yulianto,andA.Valentina,‘‘Anewmodelofpoverty
Many Are There?. Accessed: Mar. 5, 2024. [Online]. Available: indexpredictionusingtripleexponentialsmoothingmethod,’’inProc.7th
https://databoks.katadata.co.id/pasar/statistik/cdcfe12b8f8af2b/usaha- Int. Conf. Inf. Technol., Comput., Electr. Eng. (ICITACEE), Sep. 2020,
mikro-tetap-merajai-umkm-berapa-jumlahnya pp.76–79,doi:10.1109/ICITACEE50144.2020.9239205.
[24] K.D.Hartomo,Y.Nataliani,andZ.A.Hasibuan,‘‘Vegetationindices’
| [3] B. Priyono, | G. Pancawati, | and K. | Retta | Ginting, | ‘‘The role | of women |     |     |     |     |     |     |     |
| --------------- | ------------- | ------ | ----- | -------- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
SME’s in economic recovery during the covid-19 pandemic in NTT spatialpredictionbasednovelalgorithmfordeterminingtsunamiriskareas
province,’’ KnE Social Sci., vol. 2023, pp.543–552, Jun. 2023, doi: and risk values,’’ PeerJ Comput. Sci., vol. 8, p. e935, Mar. 2022, doi:
| 10.18502/kss.v8i11.13571. |     |     |     |     |     |     | 10.7717/peerj-cs.935. |     |     |     |     |     |       |
| ------------------------- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | ----- |
| VOLUME13,2025             |     |     |     |     |     |     |                       |     |     |     |     |     | 31055 |

K.D.Hartomoetal.:NovelWeightedLossTabTransformerIntegratingExplainableAI
[25] K.He,Q.Yang,L.Ji,J.Pan,andY.Zou,‘‘Financialtimeseriesforecasting [46] S. Wachter, B. Mittelstadt, and C. Russell, ‘‘Counterfactual explana-
with the deep learning ensemble model,’’ Mathematics, vol. 11, no. 4, tions without opening the black box: Automated decisions and the
p.1054,Feb.2023,doi:10.3390/math11041054. GDPR,’’ SSRN Electron. J., vol. 31, no. 2, pp.1–47, Nov. 2018, doi:
[26] M. Niu, Y. Zhang, and Z. Ren, ‘‘Deep learning-based PM2.5 long 10.2139/ssrn.3063289.
[47] L.Breiman,‘‘Randomforests,’’Mach.Learn.,vol.45,no.1,pp.5–32,
| time-series | prediction |     | by fusing | multisource |     | data—A | case study |     |     |     |     |     |     |
| ----------- | ---------- | --- | --------- | ----------- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- |
of Beijing,’’ Atmosphere, vol. 14, no. 2, p.340, Feb. 2023, doi: 2001,doi:10.1023/A:1010933404324.
10.3390/atmos14020340. [48] K.Simonyan,A.Vedaldi,andA.Zisserman,‘‘Deepinsideconvolutional
[27] M.El-Assadyetal.,‘‘TowardsXAI:Structuringtheprocessesofexplana- networks: Visualising image classification models and saliency maps,’’
tions,’’inProc.Conf.,Hum.-CenteredMach.Learn.Perspect.Workshop, 2013,arXiv:1312.6034.
2019,pp.1–12. [49] S.M.Lundberg,G.Erion,H.Chen,A.DeGrave,J.M.Prutkin,B.Nair,
[28] IBM.WhatisExplainableAI?.Accessed:Mar.6,2024.[Online].Avail- R.Katz,J.Himmelfarb,N.Bansal,andS.-I.Lee,‘‘Fromlocalexplanations
able:https://www.ibm.com/topics/explainable-ai to global understanding with explainable AI for trees,’’ Nature Mach.
[29] K. Ahadian, N. Yudistira, B. Rahayudi, A. H. Basori, S. J. Malebary, Intell.,vol.2,no.1,pp.56–67,Jan.2020,doi:10.1038/s42256-019-0138-
| S.Alesawi,A.B.F.Mansur,A.S.Alorfi,andO.M.Barukab,‘‘Maizedis- |     |     |     |     |     |     |     | 9.  |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
easeclassificationusingtransferlearningandconvolutionalneuralnetwork [50] L.Antwarg,R.M.Miller,B.Shapira,andL.Rokach,‘‘Explaininganoma-
withweightedloss,’’Heliyon,vol.10,no.21,Nov.2024,Art.no.e39569, liesdetectedbyautoencodersusingShapleyadditiveexplanations,’’Expert
doi:10.1016/j.heliyon.2024.e39569. Syst.Appl.,vol.186,Dec.2021,Art.no.115736.
[51] I.Covert,S.Lundberg,andS.-I.Lee,‘‘Understandingglobalfeaturecon-
[30] I.D.MienyeandN.Jere,‘‘Deeplearningforcreditcardfrauddetection:
Areviewofalgorithms,challenges,andsolutions,’’IEEEAccess,vol.12, tributionswithadditiveimportancemeasures,’’2020,arXiv:2004.00668.
pp.96893–96910,2024,doi:10.1109/ACCESS.2024.3426955. [52] S. S. Poudel, S. Pokharel, and M. Timilsina, ‘‘Explaining customer
[31] P. Craja, A. Kim, and S. Lessmann, ‘‘Deep learning for detecting churn prediction in telecom industry using tabular machine learning
models,’’Mach.Learn.Appl.,vol.17,Sep.2024,Art.no.100567,doi:
| financial | statement | fraud,’’ | Decis. | Support | Syst., | vol. 139, | Dec. 2020, |     |     |     |     |     |     |
| --------- | --------- | -------- | ------ | ------- | ------ | --------- | ---------- | --- | --- | --- | --- | --- | --- |
Art.no.113421,doi:10.1016/j.dss.2020.113421. 10.1016/j.mlwa.2024.100567.
[32] J. A. Nasir, O. S. Khan, and I. Varlamis, ‘‘Fake news detection: [53] S. M. N. Nobel, S. Sultana, S. P. Singha, S. Chaki, M. J. N. Mahi,
A hybrid CNN-RNN based deep learning approach,’’ Int. J. Inf. Man- T.Jan,A.Barros,andM.Whaiduzzaman,‘‘Unmaskingbankingfraud:
age. Data Insights, vol. 1, no. 1, Apr. 2021, Art.no.100007, doi: UnleashingthepowerofmachinelearningandexplainableAI(XAI)on
|     |     |     |     |     |     |     |     | imbalanced | data,’’ Information, | vol. 15, | no. 6, p.298, | May | 2024, doi: |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------------- | -------- | ------------- | --- | ---------- |
10.1016/j.jjimei.2020.100007.
[33] D. E. Rumelhart, G. E. Hinton, and R. J. Williams, ‘‘Learning rep- 10.3390/info15060298.
resentations by back-propagating errors,’’ Nature, vol. 323, no. 6088, [54] S.Ioffe,‘‘Batchrenormalization:Towardsreducingminibatchdependence
pp.533–536,Oct.1986,doi:10.1038/323533a0. in batch-normalized models,’’ in Proc. Adv. Neural Inf. Process.
|     |     |     |     |     |     |     |     | Syst., I. Guyon, | U. Von Luxburg, | S.Bengio, | H.  | Wallach, | R. Fergus, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --------------- | --------- | --- | -------- | ---------- |
[34] Y.Gao,D.Glowacka,R.J.Durrant,andK.-E.Kim,‘‘Deepgaterecur-
rent neural network,’’ in Proc. 8th Asian Conf. Mach. Learn., 2016, S.Vishwanathan,andR.Garnett,Eds.,2017,pp.1–9.[Online].Available:
pp.350–365. https://proceedings.neurips.cc/paper_files/paper/2017/file/c54e7837e0cd0
[35] S.Vii,G.D.Rede,P.Ramesh,R.KumarA,A.Bharathi,andM.C.Joe ced286cb5995327d1ab-Paper.pdf
Anand,‘‘Optimizinge-commercefrauddetectionwithBiGRUandcapsule
networkarchitectures,’’inProc.Int.Conf.DataSci.Netw.Secur.(ICD-
KRISTOKODWIHARTOMOreceivedthePh.D.
SNS),Jul.2024,pp.1–6,doi:10.1109/icdsns62112.2024.10691229.
|     |     |     |     |     |     |     |     |     | degree in | computer | science | from the | Faculty of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | ------- | -------- | ---------- |
[36] A.Vaswani,N.Shazeer,N.Parmar,J.Uszkorei,L.Jones,A.N.Gomez,
|            |     |                |             |     |        |             |          |     | Science, | Gadjah | Mada University, |     | Yogyakarta, |
| ---------- | --- | -------------- | ----------- | --- | ------ | ----------- | -------- | --- | -------- | ------ | ---------------- | --- | ----------- |
| Ł. Kaiser, | and | I. Polosukhin, | ‘‘Attention |     | is all | you need,’’ | in Proc. |     |          |        |                  |     |             |
in2019.Hehasbeenactiveinresearch,since2008,
| Adv. | Neural | Inf. Process. | Syst., | 2017, pp.1–11. |     | [Online]. | Available: |     |     |     |     |     |     |
| ---- | ------ | ------------- | ------ | -------------- | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- |
https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee untilnowongeographyinformationsystemsand
91fbd053c1c4a845aa-Paper.pdf artificial intelligence. He is currently a Profes-
|             |        |          |        |       |               |               |     |     | sorwiththeFacultyof |     | InformationTechnology, |     |     |
| ----------- | ------ | -------- | ------ | ----- | ------------- | ------------- | --- | --- | ------------------- | --- | ---------------------- | --- | --- |
| [37] H. Wu, | J. Xu, | J. Wang, | and M. | Long, | ‘‘Autoformer: | Decomposition |     |     |                     |     |                        |     |     |
SatyaWacanaChristianUniversity,CentralJava,
| transformers | with | auto-correlation |     | for long-term | series | forecasting,’’ | in  |     |     |     |     |     |     |
| ------------ | ---- | ---------------- | --- | ------------- | ------ | -------------- | --- | --- | --- | --- | --- | --- | --- |
Proc. Adv. Neural Inf. Process. Syst., M.Ranzato, A. Beygelzimer, Indonesia.Hehaspublishedhisarticlesininterna-
Y.Dauphin,P.S.Liang,J.W.Vaughan,Eds.,Jan.2021,pp.22419–22430. tionaljournals.Moreover,hehasfivecopyrights
[Online].Available:https://proceedings.neurips.cc/paper_files/paper/2021 andhaswrittensomereferencebooksoncomputerscience.
/file/bcc0d400288793e8bdcd7c19a8ac0c2b-Paper.pdf
[38] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, CHRISTIAN ARTHUR received the bachelor’s
| T. Unterthiner, |     | M. Dehghani, |     | M. Minderer, | G.  | Heigold, | S. Gelly, |     |     |     |     |     |     |
| --------------- | --- | ------------ | --- | ------------ | --- | -------- | --------- | --- | --- | --- | --- | --- | --- |
degreeincomputersciencefromBrawijayaUni-
| J. Uszkoreit, |     | and N. Houlsby. |     | (2020). | An Image | is Worth | 16×16 |     |                     |     |                 |          |     |
| ------------- | --- | --------------- | --- | ------- | -------- | -------- | ----- | --- | ------------------- | --- | --------------- | -------- | --- |
|               |     |                 |     |         |          |          |       |     | versity, Indonesia. |     | He is currently | pursuing | the |
Words:TransformersforImageRecognitionAtScale.[Online].Available:
|     |     |     |     |     |     |     |     |     | Master of | Data Science | and | Innovation | degree |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | --- | ---------- | ------ |
https://github.com/
[39] J. He, L. Zhao, H. Yang, M. Zhang, and W. Li, ‘‘HSI-BERT: Hyper- withUTS,Australia.Duringhisacademicjourney,
spectralimageclassificationusingthebidirectionalencoderrepresentation he focused on the dynamic field of deep learn-
|     |     |     |     |     |     |     |     |     | ing, particularly |     | its application | to  | forecasting. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------------- | --- | ------------ |
fromtransformers,’’IEEETrans.Geosci.RemoteSens.,vol.58,no.1,
Hisprimaryresearchinterestincludesadvancing
pp.165–178,Jan.2020,doi:10.1109/TGRS.2019.2934760.
|                |     |         |               |     |        |         |             |     | forecasting | techniques | by combining |     | theoretical |
| -------------- | --- | ------- | ------------- | --- | ------ | ------- | ----------- | --- | ----------- | ---------- | ------------ | --- | ----------- |
| [40] X. Huang, | A.  | Khetan, | M. Cvitkovic, |     | and Z. | Karnin, | ‘‘TabTrans- |     |             |            |              |     |             |
former: Tabular data modeling using contextual embeddings,’’ 2020, knowledgewithpracticalapplicationstoimprove
arXiv:2012.06678. predictivemodeling.Heiskeenonimplementingandimprovingdeeplearn-
[41] A. Theissler, F. Spinnato, U. Schlegel, and R. Guidotti, ‘‘Explainable ingacrossvariousdomainsandremainsenthusiasticaboutcontributingto
AI for time series classification: A review, taxonomy and research innovationsinpredictiveanalyticsanddeeplearningmethodologies.
| directions,’’ | IEEE | Access, | vol. | 10, pp.100700–100724, |     |     | 2022, doi: |     |     |     |     |     |     |
| ------------- | ---- | ------- | ---- | --------------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
10.1109/ACCESS.2022.3207765.
|     |     |     |     |     |     |     |     |     | YESSICA | NATALIANI | received | the | B.S. degree |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | -------- | --- | ----------- |
[42] S.M.Mathews,‘‘ExplainableartificialintelligenceapplicationsinNLP,
inMathematicsandtheM.S.degreeinComputer
| biomedical, | and | malware | classification: |     | A literature | review,’’ | in Proc. |     |     |     |     |     |     |
| ----------- | --- | ------- | --------------- | --- | ------------ | --------- | -------- | --- | --- | --- | --- | --- | --- |
Intell.Comput.,K.Arai,R.Bhatia,S.Kapoor,Eds.,Cham,Switzerland: SciencefromGadjahMadaUniversity,Indonesia.
|     |     |     |     |     |     |     |     |     | She also | received | the Ph.D. | degree | in Applied |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --------- | ------ | ---------- |
Springer,Jan.2019,pp.1269–1292.
|     |     |     |     |     |     |     |     |     | Mathematics | from | Chung | Yuan Christian | Uni- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----- | -------------- | ---- |
[43] M.T.Ribeiro,S.Singh,andC.Guestrin.(2018).Anchors:High-Precision
|     |     |     |     |     |     |     |     |     | versity, Taiwan. | She | is currently |     | an associate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | ------------ |
Model-AgnosticExplanations.[Online].Available:www.aaai.org
|                  |     |                |             |          |     |                 |       |     | professor | at Faculty | of Information |     | Technology, |
| ---------------- | --- | -------------- | ----------- | -------- | --- | --------------- | ----- | --- | --------- | ---------- | -------------- | --- | ----------- |
| [44] S. Lundberg |     | and S.-I. Lee, | ‘‘A unified | approach |     | to interpreting | model |     |           |            |                |     |             |
predictions,’’2017,arXiv:1705.07874. SatyaWacanaChristianUniversity,Indonesia.Her
[45] M. Sahakyan, Z. Aung, and T. Rahwan, ‘‘Explainable artificial research interests include cluster analysis, data
intelligence for tabular data: A survey,’’ IEEE Access, vol. 9, mining,andmathematicalmodeling.
pp.135392–135422,2021,doi:10.1109/ACCESS.2021.3116481.
| 31056 |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |