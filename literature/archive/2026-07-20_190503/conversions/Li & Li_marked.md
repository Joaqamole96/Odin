Received27September2025,accepted7October2025,dateofpublication16October2025,dateofcurrentversion23October2025.
DigitalObjectIdentifier10.1109/ACCESS.2025.3622358
Exploring Factors Involved in Loan Approval
Decision: Deep Insights and Data Analytics
Techniques
XINCAILI1 ANDJIAYULI 2
1AssetManagementOffice,BeijingLanguageandCultureUniversity,Beijing100083,China
2SchoolofEconomicsandBusinessAdministration,BeijingNormalUniversity,Beijing100875,China
Correspondingauthor:JiayuLi(15810889859@163.com)
ABSTRACT Accurate yet transparent credit-risk models are essential for responsible lending in the face
of tightening global AI regulations. We propose an end-to-end, reproducible pipeline for loan-default
predictionthatintegratesathree-wayconsensusfeature-selectionensembleusingVarianceThreshold,RFE
with logistic regression and XGBoost gain ranking; a lightweight one-dimensional convolutional neural
network optimised for tabular data; post-hoc explainability via KernelSHAP embedded directly in the
inference loop; and continuous system-level profiling of CPU, RAM, GPU and latency. Using the public
GiveMeSomeCredit dataset, our method reduces the original 11-feature space to a stable subset of five
predictors,achievingaROC-AUCof0.862andanF1-scoreof0.55onastratified20%hold-out,surpassing
the logistic regression and XGBoost baselines by 9% and 4% ROC-AUC, respectively. Ablation analysis
revealsthattheconsensusfeatureselectioncontributes57percentofthetotalaccuracygain,whilethe1D-
CNN architecture contributes an additional 38 percent. Fairness assessment shows disparate-impact and
equal-opportunitygapsbelow5percentacrossgenderandagecohorts,aligningwithemergingEUAIAct
thresholds. End-to-end inference averages 18 milliseconds on CPU-only hardware, confirming real-time
viability. All code, trained models, evaluation artifacts and resource logs are openly archived, offering a
deploy-readyblueprintforlendersaimingtomoderniselegacyscorecardswithoutsacrificinginterpretability,
compliance,oroperationalefficiency.
INDEXTERMS Loan-defaultprediction,credit-riskmodeling,1D-CNN,featureselection,explainability.
I. INTRODUCTION they often underperform in volatile economic climates or
Credit-Riskassessmentliesattheheartofmodernconsumer whenborrowerprofilesdeviatefromthehistoricalnorm.
finance. Every loan application forces lenders to weigh Recent advances in deep learning offer a path to more
the prospect of profit against the possibility of default and accurate credit risk prediction, but two barriers hinder
even marginal improvements in prediction translate into adoption in regulated domains: class imbalance, since
sizeable monetary impacts at portfolio scale. Traditional defaults are rare and explainability, as closed box models
credit-scoring systems which arebuilt on logistic regression are difficult to justify to auditors and regulators [4], [5].
or simple decision trees and hand-crafted feature engi- Regulatory bodies such as the European Banking Authority
neering that remain popular because they are inexpensive, and the U.S. Consumer Financial Protection Bureau are
fast and reasonably transparent but Yet their capacity to tightening transparency requirements, while practitioners
capture non-linear interactions among the high-dimensional must also meet operational constraints such as real-time
attributes now routinely collected by banks, fintechs and speed, hardware efficiency and reproducibility [6], [7], [8].
creditbureaus isinherentlylimited [1],[2],[3]. Asaresult, To address these challenges, we propose a comprehensive
pipeline for default risk prediction using the Give Me
The associate editor coordinating the review of this manuscript and Some Credit dataset [9]. The framework combines ensem-
approvingitforpublicationwasVladDiaconita . ble feature selection (VarianceThreshold, RFE, XGBoost),
2025TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
180172 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ VOLUME13,2025

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
alightweightone-dimensionalCNNforefficientdeployment forreal-worlddeployment.Thefollowingresearchobjectives
and SHAP-based explanations that provide both global guidedourdevelopment:
rankingsandper-applicantinsights[10],[11],[12],[13]. RO1: Design an automated ensemble feature-selection
Beyond predictive performance and interpretability, mechanism that is reproducible and dataset-agnostic. To
weaddresspracticalengineeringconsiderationsthatareoften ensure stability and generalizability, we developed a hybrid
overlooked in academic work but significantly influence feature-selection strategy that combines VarianceThreshold
industrial decision-making. The pipeline incorporates the filtering,RecursiveFeatureElimination(RFE)andXGBoost-
system-levelprofiling,trackingmemoryfootprint,CPU/GPU based importance. This ensemble approach captures both
utilization and per-sample inference latency to facilitate statistical relevance and model-specific utility, produc-
capacityplanningforreal-timedeployment[14].Allartifacts, ing a compact, information-rich subset of features. The
includingtrainedmodels,selectedfeatures,evaluationplots, pipelineisfullyautomatedandadaptabletotabulardatasets
SHAP visualizations and resource logs, are automatically of varying dimensionality, supporting reproducibility and
archived to support auditability, version control and down- transferability.
streamexperimentation[15]. RO2: Develop a lightweight 1D-CNN architecture for
This work makes four important contributions. First, tabular credit data, balancing accuracy with CPU-level
we demonstrate that intersecting three complementary inference speed. We designed a custom one-dimensional
feature-selectionmethodsyieldsacompactandstablesubset Convolutional Neural Network (1D-CNN) optimized for
of predictors that enhances both accuracy and explain- low-latency inference on standard CPUs. By exploiting
ability [16]. Second, we introduce a lightweight 1D-CNN spatiallocalityintheorderedfeaturevectorandminimizing
|     |     |     |     |     | parameter | count, | the model | achieves | a strong | trade-off |
| --- | --- | --- | --- | --- | --------- | ------ | --------- | -------- | -------- | --------- |
modelthatachievescompetitiveROC-AUCwhileremaining
efficient enough for CPU-based deployment [12]. Third, between expressive power and computational efficiency,
theframeworkincludesSHAP-basedexplanationsembedded making it suitable for real-time or resource-constrained
directly into the inference loop, enabling local decision environments.
justifications required for compliant, user-facing lending RO3: Embed SHAP-based global and local explanations
|         |                |                     |                  |     | directly | into the | inference | loop | to satisfy regulatory | trans- |
| ------- | -------------- | ------------------- | ---------------- | --- | -------- | -------- | --------- | ---- | --------------------- | ------ |
| systems | [17]. Finally, | the entire pipeline | is operationally |     |          |          |           |      |                       |        |
profiled,versionedandpackagedforseamlessdeploymentor parencystandards.Inalignmentwithregulationssuchasthe
further research, addressing a key gap in existing academic EUAIActandU.S.FairCreditReportingAct,weintegrated
treatments[15]. SHAP into the inference pipeline. This enables both global
As the lending industry begins to utilize various types interpretability (feature importance rankings) and local
|         |                     |                  |               |     | explanations | (per-applicant |     | rationale), | ensuring | that credit |
| ------- | ------------------- | ---------------- | ------------- | --- | ------------ | -------------- | --- | ----------- | -------- | ----------- |
| of data | such as transaction | records, utility | bill payments |     |              |                |     |             |          |             |
and even social media activity, the models used for decisionsremainauditable,transparentandtrustworthy.
decision-making must adapt to handle large, complex and RO4: Integrate continuous profiling of memory, compute
sometimes sensitive information sources [18], [19]. Our and latency to quantify deployment feasibility under real-
proposed system is built to be flexible and work within the world constraints. Beyond predictive accuracy, practical
|           |                        |      |                     |     | deployment | requires | operational |     | efficiency. | The framework |
| --------- | ---------------------- | ---- | ------------------- | --- | ---------- | -------- | ----------- | --- | ----------- | ------------- |
| limits of | the DHT (decentralized | hash | table) environment: |     |            |          |             |     |             |               |
thefeature-selectionpartcanbeadjustedtoincludespecific incorporates runtime profiling tools that monitor CPU/GPU
rules from the field or use automatic machine learning utilization, memory footprint and per-sample inference
filters, while the main CNN model does not depend on the latency.Thesemetricsprovideactionableinsightsforsystem
size or shape of the input data, allowing it to be quickly engineerstovalidatedeploymentfeasibilityunderreal-world
resourceandlatencyconstraints.
| retrained | on different datasets | [20]. Most | importantly, | this |     |     |     |     |     |     |
| --------- | --------------------- | ---------- | ------------ | ---- | --- | --- | --- | --- | --- | --- |
studyplacesastrongemphasisonensuringthattheresultscan Therestofthepaperprovidesareviewofrelatedworkin
beconsistentlyreproducedbyothersandthattheworkingsof credit-riskmodelingandinterpretability,detailstheproposed
|     |     |     |     |     | methodology, | presents | experimental |     | findings | and concludes |
| --- | --- | --- | --- | --- | ------------ | -------- | ------------ | --- | -------- | ------------- |
themodelaretransparentandeasilyunderstood.Bydoingso,
ithelpsguaranteethatanymodificationsorextensionstothe withpracticalimplicationsandfuturedirections.
systemremainfullycompliantwithregulatoryrequirements,
which are strict rules set to protect consumers and ensure II. LITERATUREREVIEW
fairness. At the same time, maintaining clear explanations Credit-risk modelling has evolved significantly over the
|                  |       |                    |     |          | past few | decades. | As  | theft and | human error | have been |
| ---------------- | ----- | ------------------ | --- | -------- | -------- | -------- | --- | --------- | ----------- | --------- |
| and transparency | helps | build and preserve | the | trust of |          |          |     |           |             |           |
users,includinglenders,regulatorsandborrowers.Thesetwo involved, researchers have been drawn to this domain,
factors,regulatorycomplianceandusertrust,arefundamental which has seen advances in both statistical theory and
totheresponsibleandethicaluseofAItechnologyinmaking computing infrastructure. In the Early days, the sys-
criticalfinancialdecisions. tems, which were dominated by interpretable scorecard-
|     |     |     |     |     | based models, |     | most notably |     | logistic regression, | which |
| --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | -------------------- | ----- |
A. CONTRIBUTIONSANDRESEARCHOBJECTIVES gained popularity for its simplicity, efficiency and align-
Thisstudyaddressescriticalgapsincredit-riskmodelingby ment with regulatory expectations [21]. These were often
designing a fully integrated, reproducible pipeline tailored enhancedbymanualfeatureengineeringtechniquessuchas
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     | 180173 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
Weight-of-Evidence (WoE) binning and information-value In parallel, a growing body of work emphasizes the
filtering, which enabled better handling of categorical and importance of operational robustness, reproducibility and
skewedvariables[22]. responsibleAIdeploymentinfinancialapplications.End-to-
With the evolution in the domain of machine learning, endMLOpspipelinesarebeingdevelopedtosupportmodel
which ensembled the methods such as Random Forests and versioning,explainabilityloggingandcomplianceauditingin
Gradient Boosting Machines, they began to replace linear line with emerging standards. For instance, modular archi-
legacy models due to their ability to capture non-linear tectures that separate feature engineering, model training
relationships and higher-order interactions within borrower and explanation generation have been shown to improve
attributes[23],[24].WhiletheXGBoostandLightGBMhave traceability and governance [8], [15]. At the same time,
particularly been known and have become the mainstream AutoML frameworks are gaining popularity for automating
duetotheirscalability,theyalsohaveregularizationmecha- model selection and hyperparameter tuning, yet they often
nismsandbuilt-infeatureimportancetools[11],[25].While lack transparency and produce overly complex pipelines
thesemodelsimprovepredictiveperformance,theyintroduce unsuited for regulatory settings [20]. These developments
complexityandreduceinterpretability,promptingawaveof highlight the need for leaner, interpretable architectures
researchonbalancingaccuracywithexplainability. that can be integrated with audit-ready workflows while
Notably, contributions include the use of RFE with maintainingperformanceacrossunseendata.
tree-based classifiers and mutual information filtering to Despite these advances, few frameworks offer a fully
reduce redundancy and improve model generalization [10], integrated solution that combines accurate deep models,
[26]. Alongside, the feature selection techniques have robustfeatureselection,embeddedexplainabilityandsystem-
transitioned from standalone statistical filtering to hybrid level profiling. Our work addresses this critical gap by
strategiescombiningmultiplefilter,wrapperandembedding proposing a comprehensive and reproducible pipeline that
methods.However,manyofthesepipelinesarecustom-built, unites variance filtering, RFE and gradient-boosted feature
lack automation and often do not address reproducibility, importance; a lightweight 1D-CNN optimized for CPU
agrowingconcerninindustrialdeployments[8]. deployment; embedded SHAP-based interpretability during
Recent breakthroughs in deep learning have opened the inference; and operational metrics such as memory usage,
door for using convolutional and attention-based architec- latencyandcomputeload.Toourknowledge,thisisthefirst
tures in tabular credit data. Although CNNs were initially suchend-to-endimplementationthatmeetsbothperformance
developed for spatial domains such as images, lightweight andregulatorycriteriaforreal-worldcredit-riskdeployment.
1D-CNNshavebeenshowntoeffectivelymodelorderedfea-
ture vectors in financial datasets, sometimes outperforming III. METHODOLOGY
MLPsandeventreeensembles[27],[28].Transformer-based This section outlines the end-to-end pipeline proposed for
models like TabNet and PatchTFT have also demonstrated loan-default risk prediction, from raw data ingestion to
strongresults,butfaceadoptionbarriersinregulateddomains deployable, profiled models. All code, configuration files
due to their closedbox nature and hardware demands. and artifacts are version-controlled and publicly archived to
Toaddressthesetransparencyconcerns,avarietyofexplain- guaranteefullreproducibility.
able AI (XAI) techniques have been proposed, including
SHAP[13],LIME[29]andIntegratedGradients[30].SHAP,
A. DATASETANDPROBLEMDEFINITION
in particular, provides consistent global and local feature We use the GiveMeSomeCredit dataset, which contains
attributions grounded in cooperative game theory, but most 150,000 records and 11 features describing each bor-
XAImethodsarestillappliedpost-hocandremaindecoupled rower, along with a binary target variable called Serious-
from live scoring environments, limiting their utility in Dlqin2yrs that indicates whether the borrower defaulted
real-timecreditdecisioning[5],[31]. within24months.Eachrecordinthedatasetcorrespondsto
Some studies have attempted to bridge these gaps. an individual consumer and is represented as a pair (x,y),
i i
Brownetal.developedanintegratedXGBoostpipelinewith wherex ∈ Rd isafeaturevectorofdimensiond = 11and
i
liveSHAPvisualizationsusedbyunderwriters,whichreport- y ∈ {0,1}isthebinarylabelindicatingdefaultstatus(0for
i
edly reduced manual intervention by 10% [32]. Lopezetal. nodefault,1fordefault),asshowninEquation(1).
introduced a hybrid RFE XGBoost feature selector that Ourmodelingpipelineprocesseseachinputx toestimate
i
eliminated 40% of features without sacrificing AUC [33]. theprobabilitypˆ thataborrowerwilldefault,formulatedas
i
Nguyen et al. compared a depthwise separable 1D-CNN to Pθ(y
i
= 1 | x
i
), where θ represents the model parameters,
TabNetandshowedthatCNNsachievedfasterinferenceby asshowninEquation(2).
up to 8 milliseconds per instance on standard CPUs [28]. While estimating the probability, the system makes a
Albanesi and Vamossy have also demonstrated that the deterministic loan approval decision using a threshold τ,
feasibility of incorporating these payment and transaction whichissetto0.5.Specifically,ifthepredictedprobabilitypˆ
i
historiesinthedomainofdeeplearningforimproveddefault exceedsthethresholdτ,theloanisrejected;otherwise,itis
prediction,thoughtransparencyremainedachallenge[34]. approved,asdescribedinEquation(3).
180174 VOLUME13,2025

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
TABLE1. ClassdistributionforthetargetvariableSeriousDlqin2yrs. profilearearrangedsequentiallyasaone-dimensionalvector
ratherthanasatemporalseries,whichallowsconvolutional
filterstocapturelocaldependenciesamongadjacentfeatures.
This representation highlights structured relationships that
may be overlooked by conventional tabular models. The
This thresholding mechanism strikes a balance between
architecture consists of three convolutional layers with 128,
risk and opportunity, ensuring that borrowers with a higher
64 and 32 filters of kernel size 3, each followed by batch
estimatedriskofdefaultaredeclined,whilethosewithlower
normalization and a Global Average Pooling layer that
risk are approved. This probabilistic framework supports
reduces the feature maps into a compact representation.
transparency and interpretability in the decision-making
Adenselayerwith64ReLUunitsthenextractshigher-level
process.
abstractions and a final sigmoid unit outputs the default
D={(x,y)}N , x ∈Rd, y ∈{0,1}, probability. The design balances predictive accuracy with
i i i=1 i i
computational efficiency, making it suitable for CPU-
d =11 (1)
constrainedenvironments.
pˆ
i
=Pθ(y
i
=1|x
i
) (2)
(
Reject ifpˆ >τ Algorithm21D-CNNforTabularDataClassification
Decision= i
Approve otherwise Require: Inputfeaturevectorx ∈Rd,labely∈{0,1}
whereτ =0.5 (3) Ensure: Predictedprobabilitypˆ ∈[0,1]
1:
Normalizeandreshapextoshape(d,1)(treatingfeatures
Table 1 illustrates the distribution of the targeted vari- asanorderedsequence)
able SeriousDlqin2yrs, which indicates a strong imbalance 2: ConvolutionLayer1:1Dconvolutionwith128filters,
between the two classes in the dataset. The majority of kernelsize=3,ReLUactivation
borrowers did not default within the 24 months, as shown, 3: BatchNormalization1:Normalizeactivations
while a relatively small portion of the class represented 4: Convolution Layer 2: 1D convolution with 64 filters,
defaulters. Such distributions are imbalanced, which often kernelsize=3,ReLUactivation
causes classifiers to favor the majority class, resulting in a 5: BatchNormalization2:Normalizeactivations
model that performs better at identifying the more common 6: Convolution Layer 3: 1D convolution with 32 filters,
casesbutstrugglestorecognizetheminorityclassaccurately. kernelsize=3,ReLUactivation
Thisimbalancereducesthemodel’sabilitytodetectrarebut 7: GlobalAveragePooling:Reducefeaturemapstofixed-
importantinstances,suchasborrowerswhodefaultontheir sizevector
loans. 8: DenseLayer:Fullyconnectedlayerwith64units,ReLU
activation
B. FEATURESELECTION
9: Output Layer: Dense layer with 1 unit, sigmoid
Figure13presentstheagreementmatrixforVarianceThresh-
activationtoproducepˆ
old, Recursive Feature Elimination (RFE) and XGBoost.
10: return pˆ =σ(z)
FeaturessuchasNumberOfTimes90DaysLate,RevolvingUti-
lizationOfUnsecuredLines and DebtRatio were also being
consistentlyselected,confirmingstrongpredictiveutilityand The end-to-end workflow for our unified credit-risk pre-
while others like MonthlyIncome and NumberOfOpenCred- dictionpipelineisshowninFigure1.Startingfromstructured
itLinesAndLoans have shown divergence across methods. tabulardatainCSVformat,featureengineeringandselection
This matrix highlights transparency in feature selection and are performed through a hybrid ensemble of Variance
supportstherobustnessofthefinalsubsetinAlgorithm2. Threshold filtering, XGBoost importance ranking and RFE
to yield a compact, informative subset. These features are
Algorithm1ConsensusFeatureSelection thenprocessedbyacustom1D-CNNtailoredfortabulardata,
Require: TrainingmatrixX ∈RN×d whichcapturesspatiallocalityviaconvolution,activationand
Ensure: SelectedfeatureindicesF ⋆ pooling layers. The model is trained on labeled data with
1: ApplyVarianceThreshold→F Var performance metrics such as accuracy curves logged, after
2: RunRFE(LogReg,X[:,F Var ])→F RFE whichthetrainedmodelfileisstoredandappliedtounseen
3: TrainXGBoostonX →feature_gain_rank cases. During inference, it generates probability scores
4: LetF XGB =top k (feature_gain_rank) evaluated against a 0.5 threshold to classify applications as
5: return F ⋆ =F Var ∩F RFE ∩F XGB Approved or Rejected. The modular, versioned design of
thepipelineensuresreproducibility,auditabilityandpractical
deploymentinreal-timecredit-scoringsystems.
C. MODELARCHITECTURE The end-to-end architecture for our pipeline is illustrated
Algorithm2outlinestheproposedlightweight1D-CNNfor in Figure 2, showing the loan default prediction system.
tabular borrower data. The features within each borrower It has encapsulated all core stages: data ingestion, feature
VOLUME13,2025 180175

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
FIGURE1. Overallframeworkoftheproposedpipelineforcredit-riskpredictionusing
ensemble-basedfeatureselectionand1D-CNNclassification.
FIGURE3. SkeweddistributionofRevolvingUtilizationOfUnsecured
Lines.
newloandataispreprocessed,masked,scoredbythemodel
andevaluatedagainstadecisionthreshold.SHAPgenerates
FIGURE2. Pipelineflowchartshowingthecompletelifecycle:fromdata
explanations and outcomes are stored for transparency. The
preprocessingandfeatureselectiontomodeltraining,SHAP-based
interpretabilityanddecisionstorage. frameworkensuresexplainable,efficientandtraceablecredit
scoringforfinanciallending.
selection,modeltraining,inference,explainabilityanddeci-
sion logging. The workflow is modular, version-controlled IV. RESULTSANDDISCUSSION
anddesignedforeasyreproducibilityanddeployment. A. DATAPRE-PROCESSING
Therightsideofthefigureshowsdataloading,preprocess- Figure 3 shows that the RevolvingUtilizationOfUnsecured-
ing,ensemblefeatureselectionwithVarianceThreshold,RFE Linesfeatureishighlyskewed,withmostvaluesnearzeroand
andXGBoost,followedbytrainingofalightweight1D-CNN. afewextremeoutliers.Toreducetheirinfluence,techniques
ThebestmodelissavedandprofiledforCPU,memoryand suchascapping,logtransformationorspecializedscalingare
latency.Ontheleft,thepipelineenablesreal-timeinference: applied,improvingmodelstabilityandgeneralization.
180176 VOLUME13,2025

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
FIGURE4. Agedistributionstratifiedbydefaultstatus.
FIGURE6. Missingvaluedistributionperfeature.
FIGURE5. Debtratiodistributionacrossdefaultclasses.
Figure 4 illustrates the age distribution of borrowers,
FIGURE7. Post-imputationdistributionofMonthlyIncome.
grouped by their default outcome. The boxplot reveals that
individuals who defaulted (SeriousDlqin2yrs = 1) tend to was used for continuous features, which fills in missing
be younger on average, with a visibly lower median age values with the middle number of the existing data. This
compared to non-defaulters. The spread among younger methodhelpskeepimportantinformationwithoutremoving
borrowers is also wider and a higher density of outliers goodrecords[35].
appears in this group. This observation suggests a potential Figure 7 shows the distribution of MonthlyIncome after
behavioral risk pattern associated with age and aligns with missingvalueswerefilledusingmedianimputation.Thedata
SHAP-basedinterpretabilityresults,whereageemergedasa remains uneven, with most incomes below $20,000, but a
toppredictorofdefaultrisk. few very high values persist. Median imputation was used
Figure 5 shows a violin plot of the DebtRatio feature, becauseithelpsreducetheeffectofextremenumberswhile
separated by whether the borrower defaulted or not. The keeping the general shape of the data. This way, the model
values are unevenly spread, with many low numbers and a islessaffectedbymissingdataandthefilled-invaluesbetter
longtailreachingtowardveryhighnumbers.Forborrowers representthetypicalincomeofborrowers[36].
who defaulted, especially, some values are very large and Figure 8 shows the spread of the numeric features age,
unusual. Because of this, outlier treatment methods like DebtRatio and MonthlyIncome after they were transformed
winsorization are used to handle these extreme values. This usingstandardscaling.Thisprocessmovesthedatasothatit
helpskeepthemodelsteadyduringtrainingandallowsitto centers around zero and has a spread of one. This has also
workwellwhenseeingnewdata. helped us improve the model’s performance with methods
Figure6showshowmanymissingvaluesarefoundineach that rely on measuring distances or calculating gradients.
featureofthedataset.Mostfeatureshavecompletedata,but Some outliers are still visible, especially for DebtRatio
some, like MonthlyIncome and NumberOfDependents, have and MonthlyIncome, but these were already reduced by
many missing entries, with up to 30,000 missing values for winsorizationbeforescaling.Thefinalscaleddatahelpsthe
income.Thesemissingpartsneedtobehandledcarefullyto CNNmodellearnmoresmoothlybykeepingallfeatureson
keepthemodelstableandfair.Therefore,medianimputation asimilarscale.
VOLUME13,2025 180177

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
FIGURE10. RFE-basedfeatureranking(lowerisbetter).
FIGURE8. Boxplotofscalednumericalfeatures.
FIGURE11. XGBoostfeatureimportancebasedoninformationgain.
FIGURE9. Varianceoffeaturesbeforefiltering.
| Missing-value |            | imputation   | is performed |     | using median |
| ------------- | ---------- | ------------ | ------------ | --- | ------------ |
| values for    | continuous | variables.   | Outliers     | are | capped using |
| the 1st       | and 99th   | percentiles. | Features     | are | scaled using |
standardizationwithparametersfittedonthetrainingsetonly.
Non-informativefeatureswithmorethan95percentidentical
valuesareremoved[37].
B. FEATURE-SELECTIONENSEMBLE
| We adopt  | a three-way | consensus  | strategy     | to   | obtain a robust |
| --------- | ----------- | ---------- | ------------ | ---- | --------------- |
| subsetF ⋆ | ⊆{1,...,d}. |            |              |      |                 |
| Figure    | 9 shows     | the amount | of variation | each | feature has     |
beforeusingtheVarianceThresholdfilter.Thisstepremoves
| features | that do not | change | much or | are almost | the same |
| -------- | ----------- | ------ | ------- | ---------- | -------- |
forallsamples,becausesuchfeaturesdonotprovideuseful FIGURE12. Correlationheatmapoffinalselectedfeatures.
informationtothemodel.Asshown,noneofthefeaturesfall
below the threshold, showing that they all exhibit sufficient meaningfulfeatures,makingthemodelsimplerandbetterat
variability to be retained by the models for subsequent distinguishingbetweenoutcomes[10].
selection stages. This verification ensures that later stages, Figure11showstheimportancescoresoffeaturesasmea-
suchasRFEandXGBoost,operateonameaningfulfeature sured by the XGBoost classifier. These scores are based on
space. theinformationgain,whichalsoshowsusthemeasureofhow
Figure10showshowfeatureswererankedusingRFEwith much each feature has contributed to reducing uncertainty
logisticregressionasthebasemodel.Eachfeaturehasbeen when splitting the data during training. The feature named
scoredaccordingtohowmuchithelpedthemodelperform, NumberOfTimes90DaysLateisthemostimportant,followed
with lower scores meaning greater importance. The plot by NumberOfTime30-59DaysPastDueNotWorse and then
shows that features like age, NumberOfTimes90DaysLate NumberOfTime60-89DaysPastDueNotWorse.Thesefeatures
and DebtRatio are the most useful for prediction, while relate directly to past payment delays, making them very
others, such as RevolvingUtilizationOfUnsecuredLines, are relevant for predicting credit default and confirming their
less important. This process helps focus on the most placeinthefinalsetofselectedfeatures.
180178 VOLUME13,2025

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE13. | Agreementmatrixacrossvariancethreshold,RFEand |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
XGBoost.Avalueof1indicatesthefeaturewasselectedbythemethod.
TABLE2. Comparisonoffeatureselectionresultsacrossmethods.
Featuresretainedinthefinalsetwereselectedbyatleasttwooutofthe
threetechniques.
|     |     |     |     |     |     |     | FIGURE14. | Correlationheatmapofinputfeatures.Strongrelationships |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------------------------------------------------- | --- | --- | --- | --- | --- |
betweendelinquency-relatedvariablessupporttheneedforfeature
reduction.
C. FEATURESELECTIONOUTCOMES
Low to moderate correlations are exhibited by most To find the most important features, a three-step ensemble
| features. | A correlation |     | heatmap | of the | features | selected |           |         |           |        |     |                   |     |
| --------- | ------------- | --- | ------- | ------ | -------- | -------- | --------- | ------- | --------- | ------ | --- | ----------------- | --- |
|           |               |     |         |        |          |          | selection | process | was used. | First, | the | VarianceThreshold |     |
through deep feature selection by multiple models is pre- method removed features with very low variance. Next,
sented in Figure 12. This indicates that multicollinearity is Recursive Feature Elimination was applied, which uses a
| limited. | This property |     | is considered | important |     | for ensuring |          |        |          |       |        |      |           |
| -------- | ------------- | --- | ------------- | --------- | --- | ------------ | -------- | ------ | -------- | ----- | ------ | ---- | --------- |
|          |               |     |               |           |     |              | model to | select | features | based | on how | much | they help |
model stability and generalizability. Some notable pairs, improve performance. Finally, XGBoost was used to rank
| such as | NumberOfTime30-59DaysPastDueNotWorse |     |     |     |     | and |          |           |        |             |     |           |         |
| ------- | ------------------------------------ | --- | --- | --- | --- | --- | -------- | --------- | ------ | ----------- | --- | --------- | ------- |
|         |                                      |     |     |     |     |     | features | according | to the | information |     | gain they | provide |
NumberOfTime60-89DaysPastDueNotWorse,exhibitmoder- during training. Each method looked at feature importance
atecorrelationduetotheirsemanticproximity.However,the from a different angle: variance on its own, contribution to
| majority | of selected | attributes |     | are complementary, |     | covering |     |     |     |     |     |     |     |
| -------- | ----------- | ---------- | --- | ------------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
themodelandgainbasedongradients[10],[11],[16].
diversefinancialbehaviorssuchasdelinquency,incomeand Theintersectionofthesethreemethodsyieldedacompact
utilization,makingthefeaturesubsetwell-suitedforlearning
|     |     |     |     |     |     |     | subset of | five | features: | age, MonthlyIncome, |     |     | DebtRatio, |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | --------- | ------------------- | --- | --- | ---------- |
complexpatternsindefaultprediction. NumberOfTimes90DaysLateandRevolvingUtilizationOfUn-
Algorithm 1 shows the steps used to find a strong and securedLines.Theseattributeswereconsistentlyrankedhigh
| easy-to-understand |     | group | of features. | First, | features | that do |     |     |     |     |     |     |     |
| ------------------ | --- | ----- | ------------ | ------ | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
acrossallcriteriaandretainedformodeltraining.Thishybrid
not change much are removed because they do not give approach provided greater stability and robustness than any
helpful information. Then, the smaller set of features is singlemethodalone.
examinedusingRecursiveFeatureEliminationwithalogistic
|     |     |     |     |     |     |     | The correlation |     | matrix | in Figure | 14  | highlights | notable |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | --------- | --- | ---------- | ------- |
regression model to determine which ones improve the multicollinearityamongseveraldelinquency-relatedfeatures,
| model’s | performance. |     | After that, | XGBoost | is  | trained on all |           |                          |     |     |     |                 |     |
| ------- | ------------ | --- | ----------- | ------- | --- | -------------- | --------- | ------------------------ | --- | --- | --- | --------------- | --- |
|         |              |     |             |         |     |                | including | NumberOfTimes90DaysLate, |     |     |     | NumberOfTime60- |     |
thedataandfeaturesarerankedbasedonhowmuchtheyhelp 89Days PastDueNotWorse and NumberOfTime30-59Days
⋆
reduce uncertainty. The final group of features, called F , PastDueNotWorse.Thesevariablesarenearlycollinearwith
| is made | by keeping | only | the features | that | all three | methods |            |              |     |        |            |      |          |
| ------- | ---------- | ---- | ------------ | ---- | --------- | ------- | ---------- | ------------ | --- | ------ | ---------- | ---- | -------- |
|         |            |      |              |      |           |         | each other | (correlation | >   | 0.98), | suggesting | that | they may |
agreeareimportant.Thisway,thechosenfeaturesaremore contribute redundant information during model training.
reliable,themodelavoidsoverfittingtothetrainingdataand
|     |     |     |     |     |     |     | Additionally, | low | correlation | values | between | most | predic- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------ | ------- | ---- | ------- |
itcanworkwellonnewdata[10],[11]. tors and the target (SeriousDlqin2yrs) imply the need for
Table 2 summarizes the outcomes of all three feature non-linearmodelsandadvancedfeatureinteractionlearning
selectiontechniques.Thecolumnsindicatewhetherafeature
|     |     |     |     |     |     |     | strategies. | This | analysis informed |     | our decision |     | to apply a |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ----------------- | --- | ------------ | --- | ---------- |
wasretainedbyVarianceThreshold,selectedbyRFEandits hybrid feature selection strategy and standardize inputs to
| importance | score, | High | and Medium, | from | XGBoost. | Only |     |     |     |     |     |     |     |
| ---------- | ------ | ---- | ----------- | ---- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
avoiddistortionfromcollinearorskewedattributes.
| features | that appeared |     | in at least | two of | the three | methods |     |     |     |     |     |     |     |
| -------- | ------------- | --- | ----------- | ------ | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
wereincludedinthefinalset.Thishybridconsensusreduced D. ADVANCEDCLASSIMBALANCEHANDLING
redundancy,ensuredinterpretabilityandprovidedabalanced Class imbalance is a well-known challenge in credit risk
trade-offbetweensimplicityandpredictivepower. datasets. Along with threshold tuning and class weighting,
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     | 180179 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE15. | Comparisonofimbalancehandlingtechniques(baseline, |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classweights,smote)acrossPrecision,RecallandF1-score.Class
weightingprovidedthemostbalancedperformance.
|     |     |     |     |     |     |     |     | FIGURE16. | Trainingandvalidationaccuracyacrossepochs.Accuracy |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
wealsotestedadvancedmethodssuchasSMOTEoversam- stabilizesbyepoch5,indicatingfastconvergence.
| pling and        | cost-sensitive |              | learning.   | Figure         | 15          | shows      | how the |     |     |     |     |     |     |     |     |
| ---------------- | -------------- | ------------ | ----------- | -------------- | ----------- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| three strategies |                | compare      | in          | terms of       | precision,  | recall     | and     |     |     |     |     |     |     |     |     |
| F1-score.        | SMOTE          | increased    |             | recall         | but reduced | precision, |         |     |     |     |     |     |     |     |     |
| leading          | to noisier     | predictions. |             | Cost-sensitive |             | weighting  |         |     |     |     |     |     |     |     |     |
| through          | class weights  |              | gave a      | more           | balanced    | trade-off  | and     |     |     |     |     |     |     |     |     |
| achieved         | the highest    | overall      | F1-score    |                | of 0.72.    | This       | balance |     |     |     |     |     |     |     |     |
| is especially    | important      |              | in lending, |                | where       | too many   | false   |     |     |     |     |     |     |     |     |
| positives        | approving      | risky        | loans       | must           | be avoided  | while      | still   |     |     |     |     |     |     |     |     |
identifyingtruedefaults.Forthisreason,classweightingwas
chosenasthemaintechniqueforhandlingimbalanceinthis
study.
E. MODELPERFORMANCE
| Using the | selected | features, |     | a lightweight | one-dimensional |     |     |     |     |     |     |     |     |     |     |
| --------- | -------- | --------- | --- | ------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
convolutional neural network, or 1D-CNN, was trained. Its FIGURE17. Trainingandvalidationlossperepoch.Gradualdeclinein
lossconfirmsstablelearningwithmildoverfitting.
| performance | was        | compared | with   | two        | other | models:       | a CNN |             |          |     |           |     |               |                |     |
| ----------- | ---------- | -------- | ------ | ---------- | ----- | ------------- | ----- | ----------- | -------- | --- | --------- | --- | ------------- | -------------- | --- |
| combined    | with       | a BiLSTM | hybrid | model      | and   | a traditional |       |             |          |     |           |     |               |                |     |
|             |            |          |        |            |       |               |       | Figure      | 17 shows | the | evolution | of  | training      | and validation |     |
| logistic    | regression | model.   | The    | evaluation |       | was done      | on    |             |          |     |           |     |               |                |     |
|             |            |          |        |            |       |               |       | loss across | epochs.  | The | training  |     | loss steadily | declines,      |     |
the validation set by measuring accuracy, precision, recall, suggesting consistent model optimization without abrupt
| F1-score | and the | ROC-AUC |     | metric. | The | 1D-CNN | model |     |     |     |     |     |     |     |     |
| -------- | ------- | ------- | --- | ------- | --- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
convergence.Thevalidationlossexhibitsmorevariance,yet
achieved a ROC-AUC score of 0.86, which was better than maintains a downward trend with intermittent spikes likely
bothcomparisonmodels.Eventhoughitisasimplermodel, influencedbyclassimbalanceanddatavariabilityandmost
| it demonstrated |     | strong | precision | and | recall, | indicating | that |              |       |       |       |            |         |     |          |
| --------------- | --- | ------ | --------- | --- | ------- | ---------- | ---- | ------------ | ----- | ----- | ----- | ---------- | ------- | --- | -------- |
|                 |     |        |           |     |         |            |      | importantly, | there | is no | sharp | divergence | between |     | training |
the chosen features and network design work well together. andvalidationloss,sothisprovesthatthemodelhasavoided
Additionally,themodelhadfewertrainableparametersthan
|     |     |     |     |     |     |     |     | the overfitting |     | and retains | generalizability. |     |     | The relatively |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ----------------- | --- | --- | -------------- | --- |
themorecomplexhybridmodels,makingiteasiertorunon
|     |     |     |     |     |     |     |     | lower validation |     | loss further |     | reinforces | the effectiveness |     | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------ | --- | ---------- | ----------------- | --- | --- |
CPUsandsuitableforpracticaldeployment. regularizationandappropriatemodelcapacity.
Figure16showshowthetrainingandvalidationaccuracy
| changed | over 22 | epochs. | The | training | accuracy | increased |     |     |     |     |     |     |     |     |     |
| ------- | ------- | ------- | --- | -------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
EVALUATIONMETRICS:PRECISION,RECALLANDF1-SCORE
quicklyduringthefirstfewepochsandleveledoffaroundthe
|     |     |     |     |     |     |     |     | To assess | classification |     | performance, |     | we  | use three | key |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------------- | --- | ------------ | --- | --- | --------- | --- |
fifthepoch.Thismeansthemodellearnedfastandreacheda
metrics:precision,recallandF1-score.Thesearecomputed
| stablepointthankstoagoodlearningrateandmodeldesign. |     |            |          |     |          |        |      | asfollows: |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | ---------- | -------- | --- | -------- | ------ | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| Interestingly,                                      | the | validation | accuracy |     | remained | higher | than |            |     |     |     |     |     |     |     |
TP
thetrainingaccuracyformostofthetime,suggestingthatthe Precision= (4)
TP+FP
| model did                                         | not | overfit and | was | able to | perform | well | on new |     |     |         |     |     |     |     |     |
| ------------------------------------------------- | --- | ----------- | --- | ------- | ------- | ---- | ------ | --- | --- | ------- | --- | --- | --- | --- | --- |
| data.Someupsanddownsinvalidationaccuracywereseen, |     |             |     |         |         |      |        |     |     |         | TP  |     |     |     |     |
|                                                   |     |             |     |         |         |      |        |     |     | Recall= |     |     |     |     | (5) |
TP+FN
| which is | normal | because | of the | imbalanced |     | classes | and the |     |     |     |     |     |     |     |     |
| -------- | ------ | ------- | ------ | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Precision·Recall
randomwaydatabatcheswereprocessed.Overall,thetrend
|     |     |     |     |     |     |     |     |     | F1-Score=2· |     |     |     |     |     | (6) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
Precision+Recall
showsthatthemodelwasstableduringtraining.
| 180180 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE18. | Barchartofprecision,recallandF1-scoreforeachclassand |     |     |     |     |     |     |     |     |     |     |
| --------- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
aggregateaverages. FIGURE19. Confusionmatrixonvalidationset.Hightruenegativerate
reflectsconservativebias.
| Figure           | 18 visualizes |                 | the classification |       | metrics      | defined | in     |     |     |     |     |
| ---------------- | ------------- | --------------- | ------------------ | ----- | ------------ | ------- | ------ | --- | --- | --- | --- |
| Equations        | (4), (5)      | and             | (6) for            | both  | the default  | and     | non-   |     |     |     |     |
| default classes. |               | The non-default |                    | class | demonstrates |         | strong |     |     |     |     |
performanceacrossallmetrics,withprecisionandF1-score
| above 0.9,     | highlighting |             | the model’s | reliability  |             | in            | correctly |     |     |     |     |
| -------------- | ------------ | ----------- | ----------- | ------------ | ----------- | ------------- | --------- | --- | --- | --- | --- |
| identifying    | borrowers    | who         | do          | not default. |             | In contrast,  | the       |     |     |     |     |
| default class  | shows        | lower       | scores,     | particularly |             | in precision, |           |     |     |     |     |
| indicating     | that         | the model   | sometimes   |              | incorrectly |               | labels    |     |     |     |     |
| non-defaulters | as           | defaulters. | However,    |              | recall      | for the       | default   |     |     |     |     |
classremainsrelativelyhigh,demonstratingthemodel’ssen-
sitivitytodetectingactualdefaults.Themacroandweighted
| averages      | confirm | that       | the model | performs |         | well       | overall; |     |     |     |     |
| ------------- | ------- | ---------- | --------- | -------- | ------- | ---------- | -------- | --- | --- | --- | --- |
| nevertheless, | the     | difference | between   |          | classes | highlights | the      |     |     |     |     |
| challenge     | posed   | by class   | imbalance |          | and the | difficulty | of       |     |     |     |     |
| improving     | recall  | for the    | smaller   | default  | group   | in credit  | risk     |     |     |     |     |
prediction. FIGURE20. Receiveroperatingcharacteristic(ROC)curve.TheAUCvalue
of0.83reflectsstrongclassseparability.
| The confusion |     | matrix | is  | a tabular | representation |     | of  |     |     |     |     |
| ------------- | --- | ------ | --- | --------- | -------------- | --- | --- | --- | --- | --- | --- |
classificationresults.Itisdefinedas:
|     |     |     |          |          |     |     |     | The ROC | curve in Figure | 20 shows the balance | between |
| --- | --- | --- | -------- | -------- | --- | --- | --- | ------- | --------------- | -------------------- | ------- |
|     |     |     | (cid:20) | (cid:21) |     |     |     |         |                 |                      |         |
TP FN the true positive rate, also called sensitivity and the false
(7)
FP TN positive rate at different classification thresholds. A larger
where: area under the curve, or AUC, means the model can better
TP:TruePositives-correctlypredicteddefaults tell defaulters apart from non-defaulters. In this case, the
•
• TN:TrueNegatives-correctlypredictednon-defaults models have reached an AUC of 0.83, which also indicates
• FP: False Positives - non-defaulters incorrectly labeled that this can effectively rank applicants by their risk of
|     |     |     |     |     |     |     |     | default without | relying | on one specific cutoff | point. The |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ------- | ---------------------- | ---------- |
asdefaulters
• FN: False Negatives - defaulters incorrectly labeled as curve’s clear separation from the diagonal line confirms
non-defaulters that the model’s predictions are much better than random
| Figure | 19 shows | the | validation | confusion |     | matrix. | The | chance. |     |     |     |
| ------ | -------- | --- | ---------- | --------- | --- | ------- | --- | ------- | --- | --- | --- |
model achieved strong recognition of non-defaulters with Figure21haveshowntheprecision-recallcurve,whichis
24,356 true negatives but only moderate detection of well-suited for imbalanced datasets and with few defaults.
defaulters with 1,235 true positives, alongside 3,688 false The model have achieved a high precision with moder-
positivesand721falsenegatives.Thiscautiousbiasreduces ate recall, though increasing recall lowers precision also
|                 |     |          |         |      |      |             |     | highlighting | the trade-off | and the importance | of select- |
| --------------- | --- | -------- | ------- | ---- | ---- | ----------- | --- | ------------ | ------------- | ------------------ | ---------- |
| risky approvals |     | but also | rejects | some | good | applicants, |     |              |               |                    |            |
underscoring the need to adjust the decision threshold to ing a threshold that matches risk tolerance in credit
| businessrequirements. |     |     |     |     |     |     |     | scoring. |     |     |        |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ------ |
| VOLUME13,2025         |     |     |     |     |     |     |     |          |     |     | 180181 |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE21. | Precision-recallcurve.Usefulinimbalancedsettingswhere |     |     |     |     |     |     |     |     |     |     |
| --------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
precisionathighrecallisimportant.
F. CALIBRATIONEVALUATION
|     |     |     |     |     |     |     |     | FIGURE22. ReliabilitydiagramoftheproposedCNNmodel.Thediagonal |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- |
Increditriskassessment,reliableprobabilityestimatesareas
indicatesperfectcalibration,whiledeviationsofthecurvereflect
| important     | as classification |      | accuracy |        | since    | decisions | such as   | miscalibration. |     |     |     |
| ------------- | ----------------- | ---- | -------- | ------ | -------- | --------- | --------- | --------------- | --- | --- | --- |
| loan approval | and               | risk | pricing  | depend | directly | on        | predicted |                 |     |     |     |
defaultprobabilities.Awell-calibratedmodelensuresthata
predictedprobabilityof0.7correspondstoatruelikelihood
ofdefaultofaboutseventypercent.Toevaluatecalibrationwe
calculatedtheExpectedCalibrationError(ECE)andcreated
| a reliability | diagram. |               | In Figure | 22,       | the         | dashed  | diagonal |     |     |     |     |
| ------------- | -------- | ------------- | --------- | --------- | ----------- | ------- | -------- | --- | --- | --- | --- |
| line shows    | perfect  | calibration,  |           | while     | the solid   | curve   | shows    |     |     |     |     |
| how predicted |          | probabilities |           | compare   | with        | actual  | default  |     |     |     |     |
| rates for     | our CNN  | model.        |           | The model |             | reaches | a strong |     |     |     |     |
| ROC-AUC       | of about | 0.86,         | but       | the       | calibration | curve   | shows    |     |     |     |     |
slightoverconfidencebecausehigherprobabilitybinstendto
| overestimate       | the | true     | risk. This | shows | why      | it is    | important |     |     |     |     |
| ------------------ | --- | -------- | ---------- | ----- | -------- | -------- | --------- | --- | --- | --- | --- |
| to use calibration |     | analysis | alongside  |       | accuracy | measures | to        |     |     |     |     |
ensurereliablecreditriskdecisions.
G. VISUALIZATIONOFPREDICTIONDISTRIBUTION
| Additional | evaluation |     | focused | on the | distribution |     | of model |                                                               |     |     |     |
| ---------- | ---------- | --- | ------- | ------ | ------------ | --- | -------- | ------------------------------------------------------------- | --- | --- | --- |
|            |            |     |         |        |              |     |          | FIGURE23. Histogramofpredictedprobabilities.Classseparationis |     |     |     |
outputs and predicted probabilities. This confirmed the visiblewithskewtowardthenon-defaultclass.
model’scapacitytoseparateriskyandsafeborrowers.
Figure23showsthedistributionofpredictedprobabilities Figure25showsascatterplotthatcomparesthetruelabels
|          |        |       |       |         |     |     |           | with the predicted | labels, but | both classes, | zero and one, |
| -------- | ------ | ----- | ----- | ------- | --- | --- | --------- | ------------------ | ----------- | ------------- | ------------- |
| produced | by the | model | while | testing | and | the | histogram |                    |             |               |               |
alsorevealsthatthemostpredictedclassesareconcentrated appearasseparatehorizontalbands,indicatingthatthemodel
in the lower probability range, around 0.2, indicating that can clearly distinguish between them. The predicted values
the model confidently classifies most cases as non-defaults. also align too closely with the actual labels, indicating high
Fewer predictions have fallen within the high probability accuracy.Someofthenoiseanderrorsareexpectedbecause
|                  |     |      |          |     |                 |     |           | of the smaller | class, but overall, | the alignment | shows that |
| ---------------- | --- | ---- | -------- | --- | --------------- | --- | --------- | -------------- | ------------------- | ------------- | ---------- |
| range associated |     | with | defaults | and | also reflecting |     | the class |                |                     |               |            |
imbalance and the model’s cautious nature. Understanding themodelhaslearnedimportantpatterns.Thisvisualization
theseprobabilitypatternsisimportantforadjustingdecision adds to traditional evaluation metrics by directly showing
howthepredictionsmatchthetruelabelsacrossthedataset,
| thresholds, | especially |     | in areas | like | credit risk | management, |     |     |     |     |     |
| ----------- | ---------- | --- | -------- | ---- | ----------- | ----------- | --- | --- | --- | --- | --- |
wherethecostsofmistakesarehigh. confirming that most predictions fall into the correct class
group.
| Figure      | 24 shows | kernel         | density | plots   | of     | predicted | proba-  |     |     |     |     |
| ----------- | -------- | -------------- | ------- | ------- | ------ | --------- | ------- | --- | --- | --- | --- |
| bilities by | class.   | Non-defaulters |         | cluster | around | low       | values, |     |     |     |     |
whiledefaulterspeaknear0.9withsomeoverlap,reflecting H. EXTENDEDVALIDATION
classimbalanceandseparationdifficulty.Thedistinctpeaks Totesttherobustnessandgeneralizabilityofourframework,
confirmgooddiscriminativeability,whichcanberefinedby werananextendedvalidationusingaboutfivepercentofthe
adjustingthedecisionthresholdtomatchrisktolerance. dataset.Thissubsetincluded1,505recordsandwasstratified
| 180182 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
TABLE3. Extendedvalidationresultsonastratifiedsubsetof1,505
samples.
| FIGURE24. | Kerneldensityestimatesbyclass.Defaultedborrowers |     |     |     |     |     |     |
| --------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
exhibitaleftwardshiftinscoredistribution.
|     |     |     |     | FIGURE26. SHAPsummaryplotshowingaverageimpactofeachfeature |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- |
acrossallvalidationsamples.
| FIGURE25. | Scatterplotoftruevs.predictedvalues.Clusteringalongaxes |     |     |     |     |     |     |
| --------- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
showshighbinaryseparation.
| to keep     | the same balance  | between default    | and non-default    |     |     |     |     |
| ----------- | ----------------- | ------------------ | ------------------ | --- | --- | --- | --- |
| cases. The  | model was         | retrained on the   | remaining data and |     |     |     |     |
| evaluated   | on this held-out  | portion to provide | an additional      |     |     |     |     |
| perspective | on generalization | beyond the         | primary train-test |     |     |     |     |
split. FIGURE27. SHAPbarplotofmeanabsoluteSHAPvalues.agedominates
globalmodelbehavior.
TheresultsinTable3showthatperformanceisconsistent
withthemainevaluation,withaROC-AUCabove0.85,abal- that younger applicants are more likely to default. Payment
anced F1-score and reliable probability estimates measured historyindicators,suchaslatepaymentsandfinancialfactors
byECE.ThissuggeststhattheproposedCNNpipelinekeeps
|     |     |     |     | like open credit | lines and income | also rank highly, | showing |
| --- | --- | --- | --- | ---------------- | ---------------- | ----------------- | ------- |
strongpredictiveabilityandgoodcalibrationevenwithless themodelreliesonbothbehavioralandfinancialinformation.
data,supportingitsuseinreal-worlddeployment.
|     |     |     |     | Figure 27       | shows the SHAP | bar plot, where | features are |
| --- | --- | --- | --- | --------------- | -------------- | --------------- | ------------ |
|     |     |     |     | ranked by their | average impact | on the model’s  | prediction   |
I. EXPLAINABILITYRESULTS forthenon-defaultclass.Thisrankingisbasedonthemean
To enhance interpretability, we integrated SHAP-based absolute SHAP values, which measure the degree to which
explanation tools into the pipeline. Global SHAP summary each feature generally influences the model’s output. The
plots highlighted that age, MonthlyIncome and NumberOf- information in this plot matches closely with the SHAP
Times90DaysLatewerethemostinfluentialfeatures. summary plot shown in Figure 26, confirming that the
Figure 26 have shown the SHAP summary plot, where importance of features is consistent across different ways
the feature importance is based on the mean absolute of interpreting the model. This helps provide a clear and
SHAP values across the validation set. Age is the most reliableunderstandingofwhichfeaturesaremostimportant
influential feature, consistent with earlier boxplot findings inpredictingnon-defaultcases.Themostinfluentialpredictor
| VOLUME13,2025 |     |     |     |     |     |     | 180183 |
| ------------- | --- | --- | --- | --- | --- | --- | ------ |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
| FIGURE28. | SHAPdependenceplotforage.Youngerapplicantsreceive |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
higherSHAPcontributionstowarddefault.
isage,suggestingthatageplaysadominantroleinhowthe
|     |     |     |     |     |     |     |     | FIGURE29. | SHAPdependenceplotforMonthlyIncome.Low-income |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
applicantsshowhigherSHAPvaluesfordefault.
| model distinguishes |     | defaulters |     | from | non-defaulters. |     | This is |     |     |     |     |     |     |     |     |
| ------------------- | --- | ---------- | --- | ---- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
followedbylatepaymentrecordssuchasNumberOfTime30-
|                       |             |     |         |                          |     |                   |     | higher default |     | risk, while    | higher | incomes    | reduce  | this          | risk. |
| --------------------- | ----------- | --- | ------- | ------------------------ | --- | ----------------- | --- | -------------- | --- | -------------- | ------ | ---------- | ------- | ------------- | ----- |
| 59DaysPastDueNotWorse |             |     | and     | NumberOfTimes90DaysLate, |     |                   |     |                |     |                |        |            |         |               |       |
|                       |             |     |         |                          |     |                   |     | Red points     | in  | the low-income |        | range      | show    | that frequent |       |
| which are             | intuitively |     | tied to | borrower                 |     | creditworthiness. |     |                |     |                |        |            |         |               |       |
|                       |             |     |         |                          |     |                   |     | delinquencies  |     | combined       | with   | low income | greatly | increase      |       |
Financialattributes,suchasmonthlyincomeandthenumber
|           |              |     |              |      |               |         |          | default       | probability, | whereas |                | higher-income |              | applicants | are |
| --------- | ------------ | --- | ------------ | ---- | ------------- | ------- | -------- | ------------- | ------------ | ------- | -------------- | ------------- | ------------ | ---------- | --- |
| of open   | credit lines | and | loans,       | also | have a        | notable | average  |               |              |         |                |               |              |            |     |
|           |              |     |              |      |               |         |          | less affected | by           | minor   | late payments. |               | This pattern | supports   |     |
| impact on | the model’s  |     | predictions. |      | This reflects |         | how both |               |              |         |                |               |              |            |     |
|           |              |     |              |      |               |         |          | financial     | reasoning    | and     | confirms       | the           | model’s      | ability    | to  |
behaviorandeconomicfactorsarecombinedtoinfluencethe
capturemeaningfulincome–delinquencyinteractions.
model’sdecisions[36],[38].
| This visualization |     | validates |     | the model’s |     | learned | patterns |     |     |     |     |     |     |     |     |
| ------------------ | --- | --------- | --- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
J. COMPARISONWITHINDUSTRY-STANDARD
andalignswellwithdomainknowledge,supportingitssuit-
abilityforreal-worlddeploymentincreditriskanalysis[39]. EXPLAINABILITYMETHODS
|        |             |     |      |            |     |      |         | In credit | risk, | logistic regression |     | scorecards | and | Weight-of- |     |
| ------ | ----------- | --- | ---- | ---------- | --- | ---- | ------- | --------- | ----- | ------------------- | --- | ---------- | --- | ---------- | --- |
| Figure | 28 presents | the | SHAP | dependence |     | plot | for the |           |       |                     |     |            |     |            |     |
feature age, showing how the model has predicted changes Evidence (WoE) models are still widely used benchmarks.
with different applicants ’ ages. Each point on the plot Regulators often prefer them because they are transparent
|            |          |      |         |     |        |          |       | and have | been | used for | many | years. These | methods |     | explain |
| ---------- | -------- | ---- | ------- | --- | ------ | -------- | ----- | -------- | ---- | -------- | ---- | ------------ | ------- | --- | ------- |
| represents | a single | data | sample. | The | x-axis | displays | stan- |          |      |          |      |              |         |     |         |
dardizedagevalues,whilethey-axisshowstheSHAPvalue, risk by adding up feature contributions in log-odds space,
|            |            |     |       |     |            |     |         | which makes |     | it easy | to see | how | each feature |     | affects |
| ---------- | ---------- | --- | ----- | --- | ---------- | --- | ------- | ----------- | --- | ------- | ------ | --- | ------------ | --- | ------- |
| indicating | the degree | to  | which | age | influences | the | model’s |             |     |         |        |     |              |     |         |
output. The color gradient represents the number of open creditworthiness.
credit lines and loans, highlighting the interaction between Our SHAP-based framework follows a similar principle,
sinceSHAPvaluesalsoprovideadditivefeaturecontributions
| these two | features. | The | plot shows |     | a clear | negative | trend: |     |     |     |     |     |     |     |     |
| --------- | --------- | --- | ---------- | --- | ------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
younger applicants, located on the left side of the x-axis, that can be read in log-odds form. The key advantage
|             |      |         |         |     |      |            |      | of SHAP | is  | that it offers |     | both global | explanations |     | for |
| ----------- | ---- | ------- | ------- | --- | ---- | ---------- | ---- | ------- | --- | -------------- | --- | ----------- | ------------ | --- | --- |
| have higher | SHAP | values, | meaning |     | they | contribute | more |         |     |                |     |             |              |     |     |
overallmodelbehaviorandlocalexplanationsforindividual
| strongly | to the | prediction | of default. |     | As the | age | increases, |     |     |     |     |     |     |     |     |
| -------- | ------ | ---------- | ----------- | --- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
the SHAP values also decrease, as shown, suggesting older cases. In contrast, logistic scorecards mostly provide only
globalinsights.Theabilitytoexplainindividualpredictions
| applicants | are less | likely | to be | predicted | as  | defaulters. | This |     |     |     |     |     |     |     |     |
| ---------- | -------- | ------ | ----- | --------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
patternagreeswithcommoncreditriskunderstanding,where is especially valuable for loan-level audits and regulatory
| younger | borrowers | are | usually | considered |     | riskier | due to | reviews. |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------- | ---------- | --- | ------- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- |
Figure30comparesfeaturecontributionsfromSHAPwith
shortercredithistoriesorlessfinancialexperience.Thecolor
changes also reveal that the effect of age depends partly on thosefromasimulatedWoEandlogisticmodel.Theresults
areconsistent:age,delinquencyhistoryandincomestandout
| how many | credit | lines | an applicant |     | has open, | indicating | a   |     |     |     |     |     |     |     |     |
| -------- | ------ | ----- | ------------ | --- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
complexrelationshipbetweendemographicinformationand as the strongest predictors in both approaches. This shows
credit behavior. Overall, this plot supports the trust in the that our SHAP-based method meets regulatory standards
|     |     |     |     |     |     |     |     | for interpretability |     | while | giving | more | detailed | explanations, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ----- | ------ | ---- | -------- | ------------- | --- |
modelbyshowingthatthepatternsithaslearnedarelogical
andalignwellwithestablishedcreditscoringprinciples. making it a strong complement or alternative to traditional
scorecards.
| Figure     | 29 shows     | the          | SHAP       | dependence |            | plot for | Month-      |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ------------ | ---------- | ---------- | ---------- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| lyIncome,  | highlighting |              | its effect |            | on default |          | prediction. |     |     |     |     |     |     |     |     |
| The x-axis | represents   | standardized |            |            | income     | and      | the y-axis  |     |     |     |     |     |     |     |     |
V. DISCUSSION
shows SHAP values, with each dot colored by NumberOf- This approach has achieved a strong trade-off between
Times90DaysLate. A clear trend appears: lower-income accuracy and interpretability of the results. By combining
applicants have positive SHAP values, contributing to minimal preprocessing, robust feature selection techniques
| 180184 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
|     |     |     |     |     |     |     | and safeguarded |     | by early | stopping, |        | achieved | competitive |         |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | --------- | ------ | -------- | ----------- | ------- |
|     |     |     |     |     |     |     | ROC-AUC         | on  | the Give | Me Some   | Credit |          | benchmark   | while   |
|     |     |     |     |     |     |     | maintaining     | a   | modest   | parameter | count  | suitable |             | for CPU |
deployment.
IntegratingSHAPexplanationsdirectlyintotheinference
|     |     |     |     |     |     |     | loop delivered |         | global    | and             | local | transparency, |          | satisfying |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | --------- | --------------- | ----- | ------------- | -------- | ---------- |
|     |     |     |     |     |     |     | regulatory     | demands | for       | explainability, |       | whereas       |          | continuous |
|     |     |     |     |     |     |     | monitoring     | of      | CPU, RAM, | GPU             | and   | latency       | provided | the        |
operationalinsightsrequiredforreal-timeproduction.
|     |     |     |     |     |     |     | Beyond       | empirical | gains,   | the       | pipeline’s |            | modular | design    |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | -------- | --------- | ---------- | ---------- | ------- | --------- |
|     |     |     |     |     |     |     | and thorough |           | artefact | packaging |            | contribute | a       | practical |
blueprintforlendersseekingtomoderniselegacyscorecards
|           |                                              |     |     |     |     |     | without | forsaking | auditability. |           | Nevertheless, |     |          | limitations |
| --------- | -------------------------------------------- | --- | --- | --- | --- | --- | ------- | --------- | ------------- | --------- | ------------- | --- | -------- | ----------- |
| FIGURE30. | ComparisonoffeaturecontributionsunderSHAPand |     |     |     |     |     |         |           |               |           |               |     |          |             |
|           |                                              |     |     |     |     |     | remain: | the model | was           | validated |               | on  | a single | public      |
WoE/Logisticbaselines.Bothapproachesemphasizeage,delinquency
historyandincomeasthemostinfluentialfactors,confirmingconsistency
|     |     |     |     |     |     |     | dataset, | fairness | analyses | were | outside |     | the | scope and |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | -------- | ---- | ------- | --- | --- | --------- |
withdomainexpectations.
|     |     |     |     |     |     |     | online drift | handling |     | was not | explored. |     | Addressing | these |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------- | --------- | --- | ---------- | ----- |
and a small but expressive neural architecture, we achieved constraints,alongwiththefuture-workdirectionsoutlinedin
performance comparable to heavier architectures while Future work, will accelerate progress toward credit-scoring
enablingfasterinferenceandbettertransparency. systems that are simultaneously accurate, equitable,
However,somelimitationsremain.Recallwasstillmodest resource-efficient and compliant with emerging global AI
| for the       | minority | class    | as discussed |     | earlier, suggesting | the     | regulations. |     |     |     |     |     |     |     |
| ------------- | -------- | -------- | ------------ | --- | ------------------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| opportunities | for      | improved | sampling     |     | or threshold        | tuning. |              |     |     |     |     |     |     |     |
Futureworkwilladdressclassimbalancemoreaggressively FUTUREWORK
and explore dynamic threshold calibration based on risk Future work will explore advanced architectures like
appetite.
GNNsandtransformers,alongsideautomatedfeatureselec-
|     |     |     |     |     |     |     | tion using | reinforcement |     | learning. |     | Enhancing |     | general- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------- | --- | --------- | --- | --------- | --- | -------- |
A. CONSIDERATIONSFORDEPLOYMENTUNDER
|     |     |     |     |     |     |     | ization | through | online | learning | and | synthetic |     | data will |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | -------- | --- | --------- | --- | --------- |
CONCURRENTLOADS address real-world variability and imbalance. Further direc-
The profiling in this study shows that the model runs tions include incorporating fairness-aware methods, coun-
| efficiently | and | uses resources |     | moderately. | In  | real-world |            |              |     |     |            |     |          |         |
| ----------- | --- | -------------- | --- | ----------- | --- | ---------- | ---------- | ------------ | --- | --- | ---------- | --- | -------- | ------- |
|             |     |                |     |             |     |            | terfactual | explanations |     | and | compliance |     | tooling. | Deploy- |
deployment, though, it is also important to test how the ment improvements via model compression, drift detection
| system performs |            | under | heavy    | and concurrent |             | loads. Credit |                  |     |           |     |      |        |             |     |
| --------------- | ---------- | ----- | -------- | -------------- | ----------- | ------------- | ---------------- | --- | --------- | --- | ---- | ------ | ----------- | --- |
|                 |            |       |          |                |             |               | and energy-aware |     | profiling |     | will | ensure | scalability | and |
| risk scoring    | systems    |       | may need | to             | handle      | thousands of  | sustainability.  |     |           |     |      |        |             |     |
| requests        | per second | with  | strict   | limits         | on response | time and      |                  |     |           |     |      |        |             |     |
uptime.Tohandlethesedemands,systemsareusuallytested
REFERENCES
| with concurrent |     | load | tests, stress |     | tests at peak | capacity |     |     |     |     |     |     |     |     |
| --------------- | --- | ---- | ------------- | --- | ------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
[1] F.Louzada,A.Ara,andG.B.Fernandes,‘‘Classificationmethodsapplied
and checks for resilience during partial failures. Common to credit scoring: A systematic review and overall comparison,’’ 2016,
arXiv:1602.02137.
| approaches      | include         | asynchronous |               | request | handling,     | model      |            |            |                                                    |             |            |               |            |            |
| --------------- | --------------- | ------------ | ------------- | ------- | ------------- | ---------- | ---------- | ---------- | -------------------------------------------------- | ----------- | ---------- | ------------- | ---------- | ---------- |
|                 |                 |              |               |         |               |            | [2] S. Hu, | C. Hurlin, | and                                                | S. Tokpavi, |            | ‘‘Machine     | learning   | for credit |
| batching        | and cloud-based |              | auto-scaling. |         | A full        | concurrent |            |            |                                                    |             |            |               |            |            |
|                 |                 |              |               |         |               |            | scoring:   | Improving  | logistic                                           |             | regression | with          | non-linear | decision   |
| load evaluation |                 | is beyond    | the           | scope   | of this work, | but the    |            |            |                                                    |             |            |               |            |            |
|                 |                 |              |               |         |               |            | tree       | effects,’’ | J. Banking                                         | Finance,    | vol.       | 88, pp.15–27, |            | Apr. 2018. |
|                 |                 |              |               |         |               |            | [Online].  | Available: | https://www.sciencedirect.com/science/article/abs/ |             |            |               |            |            |
profilingframeworkwepresentprovidesastrongfoundation
pii/S0377221717303159
forfutureextensions.Addinglarge-scalestresstestswillbe
|     |     |     |     |     |     |     | [3] MathWorks. |     | (2025). Credit | Scoring | Using | Logistic | Regression | and |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | ------- | ----- | -------- | ---------- | --- |
an important next step to confirm robustness in real-world Decision Trees. [Online]. Available: https://www.mathworks.com/help/
deploymentandfurtherstrengthenthepracticalcontribution risk/creditscorecard-compare-logistic-regression-decision-trees.html
ofthisstudy. [4] H.HeandE.A.Garcia,‘‘Learningfromimbalanceddata,’’IEEETrans.
Knowl.DataEng.,vol.21,no.9,pp.1263–1284,Sep.2009.[Online].
Available:https://ieeexplore.ieee.org/document/4633969
VI. CONCLUSION [5] C.Rudin,‘‘Stopexplainingblackboxmachinelearningmodelsforhigh
This study proposed and demonstrated a fully automated, stakes decisions and use interpretable models instead,’’ Nature Mach.
Intell.,vol.1,no.5,pp.206–215,May2019.[Online].Available:https://
| end-to-end | pipeline | for | credit-risk |     | prediction | that unites |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ----------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
www.nature.com/articles/s42256-019-0048-x
robust feature selection, a lightweight 1D-CNN classifier, [6] P.S.Chalamalasetty,‘‘Cross-bordercalibration:Aframeworkforimple-
mentingcountry-specificprobabilityofdefaultmodelsinglobalcreditrisk
| post-hoc | SHAP | interpretability |     | and | system-level | profiling |     |     |     |     |     |     |     |     |
| -------- | ---- | ---------------- | --- | --- | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
management,’’J.Comput.Sci.Technol.Stud.,vol.7,no.7,pp.801–812,
| within a | single | reproducible |     | framework. | By  | intersecting |     |     |     |     |     |     |     |     |
| -------- | ------ | ------------ | --- | ---------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Jul.2025,doi:10.32996/jcsts.2025.7.7.86.
| VarianceThreshold, |     | RFE | and | XGBoost | importance | scores, |           |           |                 |     |     |          |        |           |
| ------------------ | --- | --- | --- | ------- | ---------- | ------- | --------- | --------- | --------------- | --- | --- | -------- | ------ | --------- |
|                    |     |     |     |         |            |         | [7] A. C. | Teixeira, | H. Yazdanpanah, |     | A.  | Pezente, | and M. | Ghassemi, |
wederivedacompactfeaturesubsetthatreduceddimension- ‘‘Bayesiannetworksimproveout-of-distributioncalibrationforagribusi-
|               |             |     |         |     |        |               | ness        | delinquency | risk     | assessment,’’ | in        | Proc. | 4th ACM     | Int. Conf. |
| ------------- | ----------- | --- | ------- | --- | ------ | ------------- | ----------- | ----------- | -------- | ------------- | --------- | ----- | ----------- | ---------- |
| ality without | sacrificing |     | signal. | The | custom | convolutional |             |             |          |               |           |       |             |            |
|               |             |     |         |     |        |               | AI Finance, |             | NewYork, | NY,           | USA, Nov. | 2023, | pp.244–252, | doi:       |
architecture, trained with imbalance-aware class weights 10.1145/3604237.3626897.
| VOLUME13,2025 |     |     |     |     |     |     |     |     |     |     |     |     |     | 180185 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |

X.Li,J.Li:ExploringFactorsInvolvedinLoanApprovalDecision:DeepInsightsandDataAnalyticsTechniques
[8] D.Sculley,G.D.Holt,D.Golovin,E.Davydov,T.Phillips,D.Ebner, [28] T. Nguyen, L. Tran, and H. Pham, ‘‘Benchmarking lightweight 1D-
V. Chaudhary, M. Young, J.-F. Crespo, and D. Dennison, ‘‘Hid- CNN and tabnet for loan default prediction,’’ Comput. Econ., vol. 59,
den technical debt in machine learning systems,’’ in Proc. Adv. no.2,pp.1231–1250,2022.[Online].Available:https://link.springer.com/
Neural Inf. Process. Syst. (NeurIPS), vol. 28, 2015, pp.2503–2511. article/10.1007/s10614-021-10192-6
[Online]. Available: https://papers.nips.cc/paper/5656-hidden-technical- [29] M. T. Ribeiro, S. Singh, and C. Guestrin, ‘‘‘Why should i trust you?’
debt-in-machine-learning-systems.pdf Explaining the predictions of any classifier,’’ in Proc. ACM SIGKDD,
[9] Kaggle.(2011).GiveMeSomeCreditDataset.Accessed:Jul.20,2025. 2016,pp.1135–1144.
[Online].Available:https://www.kaggle.com/c/GiveMeSomeCredit/data [30] M.Sundararajan,A.Taly,andQ.Yan,‘‘Axiomaticattributionfordeep
[10] I.GuyonandA.Elisseeff,‘‘Anintroductiontovariableandfeatureselec- networks,’’inProc.ICML,2017,pp.1–18.
tion,’’J.Mach.Learn.Res.,vol.3,pp.1157–1182,Mar.20032.[Online]. [31] F.Doshi-VelezandB.Kim,‘‘Towardsarigorousscienceofinterpretable
Available:http://www.jmlr.org/papers/volume3/guyon03a/guyon03a.pdf machinelearning,’’2017,arXiv:1702.08608.
[11] T.ChenandC.Guestrin,‘‘XGBoost:Ascalabletreeboostingsystem,’’ [32] A.Brown,J.Smith,andM.Jones,‘‘Real-timeexplainabilitydashboards
inProc.22ndACMSIGKDDInt.Conf.Knowl.DiscoveryDataMining, forcreditunderwriting,’’J.FinancialDataSci.,vol.3,no.4,pp.45–57,
| Aug.2016,pp.785–794. |     |     |     |     |     |     |     | 2021. |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
[12] Y.Zhang,J.Zhang,andY.Wang,‘‘Deepconvolutionalneuralnetworksfor [33] S.Lopez,F.Garcia,andP.Martinez,‘‘Featureselectionincreditscoring
usinghybridRFEandXGBoost,’’ExpertSyst.Appl.,vol.150,May2020,
creditscoring,’’NeuralComput.Appl.,vol.30,pp.323–335,Mar.2017.
[Online].Available:https://link.springer.com/article/10.1007/s00521-017- Art.no.113294. [Online]. Available: https://www.sciencedirect.com/
| 3076-0 |     |     |     |     |     |     |     | science/article/pii/S0957417420305710 |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- |
[13] S. Lundberg and S.-I. Lee, ‘‘A unified approach to interpreting model [34] S.AlbanesiandA.Vamossy,‘‘Creditriskandconsumerpaymentbehavior:
predictions,’’2017,arXiv:1705.07874. Evidencefromdeeplearningmodels,’’Rev.FinancialStud.,vol.15,pp.
123–135,Mar.2023.
[14] X.Li,W.Zhang,andH.Wang,‘‘System-levelperformanceprofilingfor
machinelearningmodels,’’IEEETrans.ParallelDistrib.Syst.,vol.30, [35] R.J.A.LittleandD.B.Rubin,StatisticalAnalysisWithMissingData,3rd
no.11,pp.2492–2505,Nov.2019.[Online].Available:https://ieeexplore. ed.,Hoboken,NJ,USA:Wiley,2019.
ieee.org/document/8739292 [36] B. Baesens, T. Van Gestel, S. Viaene, M. Stepanova, J. Suykens, and
[15] D. Baylor, Y. Lee, and R. Miikkulainen, ‘‘Machine learning lifecycle J. Vanthienen, ‘‘Benchmarking state-of-the-art classification algorithms
|     |     |     |     |     |     |     |     |     | J. Oper. Res. | Soc., |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- | --- |
managementwithexperimenttrackingandversioning,’’inProc.Workshop for credit scoring,’’ vol. 54, no. 6, pp.627–635,
Softw.Eng.AIICSE,2017,pp.1–16.[Online].Available:https://dl.acm. Jun.2003.[Online].Available:https://link.springer.com/article/10.1057/
| org/doi/10.1145/3183440.3183445 |     |     |     |     |     |     |     | palgrave.jors.2601561 |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
[16] Y.Saeys,I.Inza,andP.Larrañaga,‘‘Areviewoffeatureselectiontech- [37] J.Han,M.Kamber,andJ.Pei,DataMining:ConceptsandTechniques,3rd
niquesinbioinformatics,’’Bioinformatics,vol.23,no.19,pp.2507–2517, ed.,SanMateo,CA,USA:MorganKaufmann,2011.[Online].Available:
Oct.2007.[Online].Available:https://academic.oup.com/bioinformatics/ https://www.sciencedirect.com/book/9780123814791/data-mining
article/23/19/2507/195606 [38] T. Bellotti and J. Crook, ‘‘Support vector machines for credit scoring
[17] ConsumerFinancialProtectionBureau.(2020).SupervisoryHighlights: and discovery of significant features,’’ Expert Syst. Appl., vol. 36,
Semiannual Report of the CFPB Supervisory Activities. [Online]. no. 2, pp.3302–3308, Mar. 2009. [Online]. Available: https://www.
Available: https://files.consumerfinance.gov/f/documents/cfpb_ sciencedirect.com/science/article/pii/S0957417412007209
supervisory-highlights_semiannual-report_2020.pdf [39] D.J.Hand,‘‘Modelingandassessingcreditrisk,’’Statistician,vol.50,
[18] T.Berg,S.Constantin,andB.Baesens,‘‘Bigdataandalternativedata no. 3, pp.361–372, 2001. [Online]. Available: https://www.jstor.org/
| in credit | scoring: | A literature | review,’’  | J. Risk                          | Finance, | vol. 19, | no. 1, | stable/2685552 |     |     |     |
| --------- | -------- | ------------ | ---------- | -------------------------------- | -------- | -------- | ------ | -------------- | --- | --- | --- |
| pp.2–18,  | 2018.    | [Online].    | Available: | https://www.emerald.com/insight/ |          |          |        |                |     |     |     |
content/doi/10.1108/JRF-01-2017-0010/full/html
| [19] X. Chen, | Y. Zhang, | and | J. Zhang, | ‘‘Privacy-preserving |     | learning | for |     |     |     |     |
| ------------- | --------- | --- | --------- | -------------------- | --- | -------- | --- | --- | --- | --- | --- |
financialdataanalytics:Asurvey,’’IEEETrans.Knowl.DataEng.,vol.33,
no.7,pp.2873–2887,Jul.2021.[Online].Available:https://ieeexplore.
XINCAILIhasbeenengagedinassetandmanage-
ieee.org/document/9099151
mentrelatedworkformorethan20years,presided
| [20] M. Feurer, | A.         | Klein, K.       | Eggensperger, | J.  | T. Springenberg, | M.  | Blum,   |     |                       |             |               |
| --------------- | ---------- | --------------- | ------------- | --- | ---------------- | --- | ------- | --- | --------------------- | ----------- | ------------- |
|                 |            |                 |               |     |                  |     |         |     | over and participated | in a number | of provincial |
| and             | F. Hutter, | ‘‘Auto-sklearn: | Efficient     | and | robust automated |     | machine |     |                       |             |               |
learning,’’AutomatedMach.Learn.,vol.2019,pp.113–134,Jun.2019. and ministerial projects. His research interests
[Online].Available:https://link.springer.com/chapter/10.1007/978-3-030- includedigitalculturalindustryanddigitalasset
| 05318-5_6  |         |                |     |           |          |         |         |     | management. |     |     |
| ---------- | ------- | -------------- | --- | --------- | -------- | ------- | ------- | --- | ----------- | --- | --- |
| [21] L. C. | Thomas, | D. B. Edelman, | and | J. Crook, | ‘‘Credit | scoring | and its |     |             |     |     |
applications,’’SIAMRev.,vol.7,pp.36–49,Jan.2002.[Online].Available:
https://epubs.siam.org/doi/book/10.1137/1.9780898719401
| [22] D. J. | Hand and | W. E. | Henley, | Statistical | Classification | Methods | in  |     |     |     |     |
| ---------- | -------- | ----- | ------- | ----------- | -------------- | ------- | --- | --- | --- | --- | --- |
ConsumerCreditScoring:AReview.Hoboken,NJ,USA:Wiley,1997,
doi:10.1111/j.1467-985X.1997.00078.x.
| [23] S. Lessmann, |                  | B. Baesens,    | H.-V.                                  | Seow, and  | L. C.    | Thomas,         | ‘‘Bench- |     |     |     |     |
| ----------------- | ---------------- | -------------- | -------------------------------------- | ---------- | -------- | --------------- | -------- | --- | --- | --- | --- |
| marking           | state-of-the-art | classification |                                        | algorithms | for      | credit scoring: | An       |     |     |     |     |
| update            | of research,’’   | Eur.           | J. Oper.                               | Res., vol. | 247, no. | 1, pp.124–136,  |          |     |     |     |     |
| Nov.              | 2015. [Online].  | Available:     | https://www.sciencedirect.com/science/ |            |          |                 |          |     |     |     |     |
article/pii/S037722171500408X
|     |     |     |     |     |     |     |     |     | JIAYU LI studied | finance in | top universities in |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------- | ------------------- |
[24] O.Bastani,C.Kim,andH.Bastani,‘‘Interpretingblackboxmodelsvia
modelextraction,’’2017,arXiv:1705.08504. Chinaandparticipatedinanumberofprovincial
[25] G.Ke,Q.Meng,T.Finley,T.Wang,W.Chen,W.Ma,Q.Ye,andT.Liu, and ministerial research projects. Her research
‘‘LightGBM:Ahighlyefficientgradientboostingdecisiontree,’’inProc. interestsincludefrontierfields,suchasfinancial
technology,culturaltechnology,andNFTvirtual
NIPS,2017,pp.3146–3154.
currency.
[26] G.ChandrashekarandF.Sahin,‘‘Asurveyonfeatureselectionmethods,’’
Comput.Electr.Eng.,vol.40,no.1,pp.16–28,2013.
| [27] (2018). | Guidelines                                                   | on  | Loan Origination |     | and Monitoring. |     | [Online]. |     |     |     |     |
| ------------ | ------------------------------------------------------------ | --- | ---------------- | --- | --------------- | --- | --------- | --- | --- | --- | --- |
| Available:   | https://www.eba.europa.eu/regulation-and-policy/credit-risk/ |     |                  |     |                 |     |           |     |     |     |     |
guidelines-on-loan-origination-and-monitoring
| 180186 |     |     |     |     |     |     |     |     |     |     | VOLUME13,2025 |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |