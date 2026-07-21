---
conversion_metadata:
  converted_at: "2026-07-21T06:43:36Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Jiang et al.pdf"
  source_pdf_sha256: "cd1e207e632e3858aa7c4968f828de059863f5b4cbb832fafe619ce70ae5091b"
  page_count: 25
  markdown_char_count: 135257
---

Received30January2026,accepted1March2026,dateofpublication5March2026,dateofcurrentversion17March2026.
DigitalObjectIdentifier10.1109/ACCESS.2026.3670857
A Dynamic Framework for Causal User Profiling
and Treatment Segmentation via Uplift Modeling
in Internet Lending
JIANQINGJIANG 1,NORASILAHWATIABDULHAMID 1,2,(SeniorMember,IEEE),
NGKENGYAP 1,2,(SeniorMember,IEEE),ANDCHOOWEICHONG3
1InstituteforMathematicalResearch(INSPEM),UniversitiPutraMalaysia(UPM),Serdang,Selangor43400,Malaysia
2FacultyofComputerScienceandInformationTechnology,UniversitiPutraMalaysia(UPM),Serdang,Selangor43400,Malaysia
3SchoolofBusinessandEconomics(SBE),UniversitiPutraMalaysia(UPM),Serdang,Selangor43400,Malaysia
Correspondingauthor:ChooWeiChong(wcchoo@upm.edu.my)
ABSTRACT The growth of internet lending has created a need for decision frameworks based on
models that are both personalized and causally interpretable. Conventional uplift models detect treatment
responsiveness without recognizing user heterogeneity, the temporal consistency of user behavior, or the
upstream design choices that carry important causal implications. This paper proposes an integrated and
reproducible Causal User Profiling (CUP) framework that combines causal inference, uplift modeling,
and response-based segmentation within a single pipeline. CUP realizes treatment-effect heterogeneity
throughafour-typeresponsetaxonomy(Persuadable,SureThing,LostCause,Do-Not-Disturb)andembeds
it in a multi-stage pipeline involving hybrid feature selection (Information Value (IV), Causal Forest
importance,PopulationStabilityIndex(PSI)stability,andStepwiserefinement),stratifiedclusteringwith
a ‘‘C2 replacement strategy,’’ and meta-learning via both the X-Learner and the Doubly Robust (DR)
Learner using Logistic Regression (LR). A component-wise ablation analysis finds that feature selection
increases AUUC by 25–30%, C2 clustering by 10–12%, and the DR-Learner + LR by another 5–8%.
Overall, the integrated CUP framework yields 45–50% higher AUUC than the baseline (‘‘all features +
no clustering + standard learner’’) while retaining behaviorally coherent and temporally stable insights.
Methodologically,weprovide:1)anend-to-endcausaluserprofilingframeworkthatinteroperatesprofiling,
causal estimation, clustering, and uplift evaluation; 2) a behaviorally and causally consistent response
segmentation mechanism grounded in the potential-outcomes model; and 3) a reproducible experimental
design that quantifies pipeline-level uplift gains through systematic ablation. Applied to large-scale
internet-lending data, CUP reveals opportunities for treatment-aware personalization, enabling financial
institutions to target Persuadables, support Sure Things, and avoid disturbing Do-Not-Disturbs based on
causalevidence.
INDEX TERMS C2 clustering strategy, causal precision, causal user profiling, decision support systems,
DR-learner, feature selection, heterogeneous treatment effects, internet lending, meta-learners, response
segmentation,upliftmodeling,X-learner.
I. INTRODUCTION In this tussle, user profiling [1], [2], [3]—the process
The rapid evolution of digital platforms has heightened of acquiring, analyzing, and organizing multi-dimensional
the importance of personalization and targeting, shifting user data to create static and/or dynamic user profiles or
attentiontowardcoreaspectsofdata-drivendecision-making. models of the user’s behaviors, tastes, preferences, and
otherdemographics—isfoundationaltodata-drivensystems.
The associate editor coordinating the review of this manuscript and Profiling helps design interpretable user representations
approvingitforpublicationwasDiegoBellan . that drive downstream applications such as recommender
2026TheAuthors.ThisworkislicensedunderaCreativeCommonsAttribution4.0License.
VOLUME14,2026 Formoreinformation,seehttps://creativecommons.org/licenses/by/4.0/ 40147

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
systems,targetedmarketing,andriskassessment[4],[5]but In practical internet lending systems, interventions such
conventional profiling pipelines are observational in nature, as interest coupons, fee reductions, credit line adjustments,
concerned with who the user is instead of how the user and targeted reminders are routinely deployed to influence
would react if acted upon [6], and almost entirely ignore user borrowing behavior. When such actions are guided
causation [7], relegating them to use-case-specific opaque solelybypredictivemodelsorrawtreatment-effectestimates,
modelscomponents[8]. platforms may repeatedly allocate incentives to users who
Duringthesameperiod,ashiftinthewaythefieldthought would borrow regardless of intervention, while failing to
aboutthephrase‘‘learningfromdata’’influencedhowdata— activate users who are truly responsive to targeted actions.
used for the targeted deployment of algorithms—came to Moreover, these interventions are often applied repeatedly
beconceptualized.Awidelyusedformulationcharacterizes under budget and risk constraints, making it difficult to
learningfromdataastheprocessinwhich‘‘aprogramissaid translateheterogeneoustreatmenteffectestimatesintostable,
tolearnfromexperienceEwithrespecttosomeclassoftasks interpretable,anddecision-aligneduserrepresentations.
T and performance measure P if its performance at tasks in Concurrently with the emerging HTE literature, uplift
T, as measured by P, improves with experience E.’’ While modeling first arose in applied domains such as marketing,
predictivepowerinanalyticsisimpressive,machinelearning healthcare, and finance to directly estimate incremental
(ML)algorithmsarelimitedbythefactthatmakingdecisions impact: the difference between the probability of response
canchangetheverydistributionoftheoutcomesonewishes fromagroupexposedtotreatmentandthatofacomparable
to predict [9]. In many situations, prediction is insufficient, group not exposed [17]. In practical terms, this quantity
andoneneedstounderstandthecausalstructureoftheworld answers how much more likely a user is to respond
because interventions change the distribution of data [10]. as a direct result of an intervention, rather than due to
It is this limitation that led to additional research on causal baseline propensity. Uplift models [18], [19] that focus on
inference,definedas‘‘thestudyoftherelationshipbetween modelingthe‘‘treatmenteffectinduced,’’ratherthanoverall
cause and effect’’ [9], which also extensively informs predictiveaccuracy,canemploytree-basedapproaches.The
decision-makingsinceMLnecessarilyrestrictsitspowerby ‘‘four-type’’ consumer classes—Persuadables, Sure Things,
learning only patterns instead of, for instance, generating Lost Causes, and Do-Not-Disturbs—serve as the concep-
causalrelationsforitspredictions.Causalinferencehastwo tual framework for studying individual causal response
paradigms which can inform solutions to these problems. [20], [21], [22]. This taxonomy is widely used to align
The first is the potential outcomes framework, where ‘‘the incremental-effect estimation with operational targeting,
causal effect of a treatment on a unit is the difference because it distinguishes true incremental responders (Per-
between the outcome when the unit receives the treatment suadables) from always-responders (Sure Things), never-
and the outcome when the unit does not’’ [11]. The responders (Lost Causes), and users for whom treatment
second is ‘‘the process of using data together with causal may be harmful (Do-Not-Disturbs). [20], [21], [22] Uplift
assumptions to answer questions about causal relations— modeling evaluates targeting strategies against metrics such
such as predicting the effect of interventions or explaining asAreaUndertheUpliftCurve(AUUC)andQinicoefficient,
observed dependencies’’ [9]. The first provides a coherent which capture the incremental gain produced [17], [19].
underpinning for counterfactual reasoning [12], and the Recentlyconducted reviewswarn thatuplift performanceis
secondprovidesmodelsforreasoningqualitativelyaboutthe verysensitivetoupstreamdesignchoices—featureselection,
data-generatingprocessandiscriticalforthetransportability clustering,andlabeling—andthatthevalueofanintegrated
ofcausalknowledge[9].Thesynthesisofthetwoisclear:‘‘by and transparent pipeline is greater than isolated model and
leveraging causal inference, you go beyond description and algorithmcomparisons[8],[22].
association,’’beingabletoaskwhatalternativeactionswould Yet, ‘‘traditional’’ user profiling continues to follow the
do under differing situations [10]. These advances form the predictable, descriptive steps of data collection, normal-
basis of heterogeneous treatment effect (HTE) estimation, ization and cleansing, feature extraction, clustering, and
which directly focuses on individual-level responsiveness performanceevaluation.Theprimarygoalremainspredictive
to interventions [6], [13], [14]. In this line of work, segmentation and operational classification [4], [23], [24].
Causal Trees reveal treatment heterogeneity using recursive Currentprofilingsystems,effectiveastheyareforprediction,
partitioning[6],andCausalForestsextendthismethodology, are not designed to estimate how users would respond to
resultinginconsistentConditionalAverageTreatmentEffects interventions, nor do they derive properties from causal
(CATEs) [13]. Meta-learners (e.g., S-, T-, X-, and R- heterogeneity [7]. From the perspective of profiling, causal
learners) [15] reformulate the causal estimation task into reasoning has not yet been embedded into an end-to-end
modularsupervised-learningsettingsthatallowforflexibility analysis pipeline, and we ask three broad methodology
and scalability across data environments [15]. Beyond questions: (i) how to design new AAUC-driven response
estimation, policy learning integrates causal inference with segmentation, where labeling both informs and determines
decision-making contexts, creating decision rules from evaluation; (ii) how to integrate feature selection, stratified
estimatesoftreatmenteffects[16]. clustering, bias adjustment, and treatment-effect estimation
40148 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
into a new unified causal user profiling workflow; and (iii) II. RELATEDWORK
how to measure the marginal contribution of each pipeline A. UPLIFTMODELINGANDEVALUATION
componentthroughcomponent-wiseablationanalysis[22]. Uplift modeling—also referred to as incremental response
This work intends to close these gaps by introducing a modeling—reconceptualizes prediction as the estimation
unified method called Causal User Profiling (CUP), inte- of differential treatment response, emphasizing the causal
gratinguserprofiling,causalinference,andupliftmodeling effect of an intervention rather than its absolute outcome
into a single analysis process, building on the previous level.Incontrasttoconventionalpredictivemodeling,which
descriptive roadmap but embedding causal estimation and estimates the likelihood of an outcome, uplift modeling
uplift-based evaluation into its core. Conceptually, it allows explicitly focuses on the change in outcome probability
causal reasoning to take form inside profiling methods, attributable to an action. As Radcliffe and Surry [17] state,
stating not only who users are, but how they respond to uplift defines the notion of ‘‘the difference in response
actionsperformedonthem[25]. rates attributable to a treatment’’ that ‘‘shifts analytics from
Wesummarizethreecontributions: descriptive prediction into the prescriptive space.’’ Early
(1) Causal User Profiling Framework. We propose an approachesadoptedatwo-modelstrategy,inwhichseparate
integrated methodological framework that connects feature predictivemodelsaretrainedfortreatedanduntreatedgroups,
selection, clustering, confounding adjustment, and causal andthedifferenceisinterpretedastheincrementaleffect[20].
effect estimation into a coherent causal user profiling Althoughsimpletoconceptualize,two-modelapproachescan
pipeline. be unstable and lead to biased estimates when treatment
(2) AAUC-Driven Post-Evaluation Response Segmenta- allocationisimbalancedorwhencovariatedistributionsdiffer
tion. We develop a performance-based segmentation mech- substantiallyacrossgroups.
anism that classifies users into the four causal response A significant methodological advance arrived with
types (Persuadables, Sure Things, Lost Causes, and Do- tree-based uplift models, which introduced recursive parti-
Not-Disturbs) based on AAUC results, bridging model tioning to seek maximum treatment–control heterogeneity
evaluation with actionable user interpretation. For example, within subgroups [18]. These Uplift Decision Trees offered
separating Persuadables from Sure Things clarifies whether interpretable segmentation rules and provided groundwork
ahigh-responsesegmentreflectstrueincrementalimpactor for subsequent ensemble extensions. Uplift random forests
merelyhighbaselinepropensity. and causal forests improved robustness and consistency
(3)Component-WiseAblationandPerformanceAnalysis. throughaggregation,althoughatsomecosttointerpretability
We quantify the marginal contribution of each pipeline [6], [13]. This line of work reflects a broader methodolog-
stage—feature selection, clustering, bias adjustment, and ical transition toward explicitly modeling heterogeneous
causal estimation—to overall uplift performance, providing treatment effects (HTE) to inform intervention decisions.
reproduciblemethodologicalinsightsforpractitioners. As summarized by Devriendt et al. [22], this evolution
Validatingonaninternet-lendingdataset,resultsillustrate represents a broader shift from purely predictive response
how embedding causal reasoning within user profiling models to prescriptive analytics that conceptually situates
providesameanstodeliveradditionalvaluetocustomersand upliftmodelingwithinmoderncausalinference.
businessesalike,ultimatelyleadingtobetterpersonalization, Parallel advances occurred in meta-learning approaches
more precise targeting, and more effective data-driven thatreinterpretupliftestimationassuperimposedsupervised
decision-makingunderreal-worldconstraints[22],[23]. learning tasks. Frameworks like the S-, T-, X-, R-, and
DR-learners unify heterogeneous treatment effect (HTE)
a: ORGANIZATIONOFTHEPAPER estimationandupliftpredictionunderflexibletemplates[14],
Theremainderofthispaperisorganizedasfollows.SectionII [15].Theseapproachesdecoupletheestimationofnuisance
reviews related work on heterogeneous treatment effect components, such as outcome and treatment assignment
estimation,upliftmodeling,causalinferenceinrecommender models, from the final treatment-effect estimator, enabling
systems,anduserprofiling,andidentifiesthemethodological flexible combinations with different base learners. In prac-
gapsaddressedinthisstudy.SectionIIIintroducestheCausal tice,meta-learnersdiffermainlyinhowtheyreuseoutcome
UserProfiling(CUP)framework,detailingitscoremodules modelsandpropensityinformationunderimbalanceandlim-
includingfeatureselection,causalestimation,clustering,and ited overlap, and their stability is therefore strongly shaped
response-type segmentation. Section IV describes the data by base-learner choice and nuisance-model specification.
source, preprocessing procedures, and experimental design. [14],[15],[19]Thesemethodsyieldadditionalgeneralization
Section V presents and discusses the empirical results, acrosssettingsbutremainsensitivetobase-learnerselection,
focusingonmodelperformance,stability,andinterpretability sample size, and hyperparameter tuning. Until now, tabular
under repeated interventions. Section VI outlines the lim- models and representation-learning–based causal networks,
itations of the proposed framework. Finally, Section VII such as TARNet, CFRNet, DragonNet, and GANITE, have
concludes the paper and discusses directions for future adopted deep architectures to mitigate covariate imbalance,
research. reduce the burden of counterfactuals, or model nonlinear
VOLUME14,2026 40149

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
treatment effects on the response [26], [27], [28]. While Tree-basedmethodssuchasCausalTreesstartwiththefull
suchmodelsimproveexpressivecapacity,priorstudiesnote covariatespaceandrecursivelypartitionittoidentifyregions
trade-offs in interpretability, stability, and reproducibility, with distinct treatment effects. Causal Forests, for several
particularlyinprofiling-orientedapplications. well-foundedreasons,insteademployensembleaggregation,
As models improved, so did evaluation. Uplift modeling yielding more consistent estimators and supporting valid
concerns incremental gain; thus standard accuracy metrics statistical inference across regions [6], [13]. Generalized
are not useful. Uplift-specific ranking measures such as Random Forests (GRF) extend this local/posterior forest
the ‘‘Qini coefficient(s)’’ and the ‘‘Area Under the Uplift framework,unifyingalargeclassofforest-basedestimators
Curve (AUUC)’’ are now standard [17], [19]. Both met- into a general nonparametric framework [16]. Beyond tree
rics evaluate how effectively a model ranks individuals ensembles, Bayesian and nonparametric approaches intro-
by incremental response rather than by absolute outcome duceuncertaintyquantificationthroughcredibleintervalsand
likelihood.TheQinicoefficientsumscumulativedifferences yieldmorerobustestimatesinsmall-sampleorhigh-variance
across incremental uplift-ranked segments between treated settings [31], [32] via methods such as Bayesian Additive
and control groups. AUUC measures the total incremental Regression Trees (BART), Bayesian Causal Forests (BCF),
effect via the area between the uplift curve and a diagonal and Gaussian Process models. These approaches are often
baseline. The latter can be sensitive to treatment imbalance preferred in settings where variance control and uncertainty
or sparse samples, and recent advances have introduced assessmentarecriticaltodownstreamdecision-making.
multi-treatment AUUC and cross-treatment gain surfaces Whilelighter-weightestimatorsrelaxassumptionsrequired
to cover multi-arm and dose-response settings [29], [30]. for CATE estimation, meta-learning approaches—S-, T-,
Intuitively, gain-surface style evaluations summarize how X-, R-, and DR-learners—decompose the CATE estimation
incremental ranking performance varies across intervention task into modular supervised learning problems and offer
arms, making cross-arm trade-offs and sensitivity to treat- flexibility in base-learner choice and treatment-variable
ment choice explicit. [29], [30] Reviews emphasize that specification [14], [15]. The combination of meta-learners
the ability to generate strong uplift curves is attributable with different base learners is motivated by the need to
largely to upstream pipeline design choices, particularly balance bias, variance, and robustness under heterogeneous
featureselection,usersegmentation,andresponse-type/target data-generating conditions, rather than by any universally
labeling [8], [22]. Other comparative studies consider uplift optimal configuration. Empirical analyses show no uni-
algorithmstobe‘‘opaquemodels’’andprovidelimiteddetail versally dominant learner, highlighting that pipeline-level
onimplementationorsensitivityanalyses,whichundermines optimization is preferred over naive model substitution
reproducibility and reduces practical interpretability [17], [22]. Representation-learning–based causal models such
[18]. In this study, reproducibility refers to reporting and as TARNet, CFRNet, DragonNet, and GANITE build
structuring the full pipeline—feature construction/selection, deep latent representations to reduce covariate imbalance
clustering settings, propensity modeling, learner configu- and improve counterfactual estimation [26], [27], [28].
ration, and labeling rules—so that an independent team While these models increase expressive capacity, prior
can rerun the workflow and obtain consistent uplift curves studies note trade-offs in transparency, stability, and repro-
and response-type assignments under the same data and ducibility, particularly when interpretability is required for
protocol. These concerns motivate a methodological shift profiling-orientedanalysis[7].
fromisolatedmodelcomparisontowardworkflow-levelopti- Evaluation frameworks in the HTE literature closely
mization, focusing on transparent design choices, pipeline parallel those used in uplift modeling. Metrics such as
configuration, and component-wise diagnostics—principles Incremental AUUC and Qini measure incremental ranking
that underpin the Causal User Profiling (CUP) framework performance,whilePrecisioninEstimationofHeterogeneous
introducedinthisstudy. Effects (PEHE) and Mean Squared Error of Individual
TreatmentEffects(MSE(ITE))arecommoninsemi-synthetic
B. HETEROGENEOUSTREATMENTEFFECTS(HTE)AND benchmarks [15]. For joint learning of treatment policies,
CATEESTIMATION policy value and doubly robust off-policy evaluation (OPE)
Although uplift modeling is used mostly in marketing assess expected reward of policies derived from estimated
and intervention targeting, the concept of Heterogeneous treatment effects [33]. When multiple interventions are
TreatmentEffects(HTE)providesthetheoreticalfoundation available, multi-treatment AUUC and consistency-based
for uplift modeling. HTE methods aim to estimate the metricsfurthercharacterizethestabilityofrankingandpolicy
Conditional Average Treatment Effect (CATE) for each decisionsacrosstreatmentarms[29],[30].
individual or subgroup in the population—that is, the Recentreviewsprovideempiricalinsightintotheadoption
expected causal effect conditional on observed features [6], and implementation of HTE methods across domains.
[13]. From this perspective, uplift modeling can be viewed Aforthcoming2024methodologicalreviewofCausalForest
as an operationalization of HTE estimation that emphasizes applicationsanalyzes133peer-reviewedstudiesacrossareas
ranking and targeting decisions rather than pointwise effect from healthto marketing,documenting widespreadreliance
estimationalone. on the grf package but limited reporting of identification
40150 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
TABLE1. RepresentativemethodsandevaluationframeworksinHTEandupliftmodeling.
assumptions and tuning parameters [34]. A PRISMA- systemsemphasizedataenrichment,privacyprotection,and
guided scoping review of HTE estimation in randomized governanceconsiderationsratherthanresponse-drivencausal
controlled trials (RCTs) using machine learning reports mechanisms.Purificatoetal.[7]observethatmanyexisting
predominance of forest-based (60%) and Bayesian (53%) profilingapproaches‘‘focusoncorrelationsratherthancausal
models in domains such as health and education, while mechanisms,’’ limiting their ability to support responsive
again noting incomplete documentation of generalizability interventionsorpredictuser-leveltreatmentresponsiveness.
checks and identification strategies [35]. In RCT-emulation Thus, although causal recommender modeling has seen
pipelines that benchmark recent methodologies—including significant advances, operational techniques that integrate
Ding et al. ’s RIF—reviews report frequent failures in causalinferenceintouser-profilingpipelinesremaincompar-
confoundingadjustmentorvalidation,reinforcingtheimpor- ativelyscarce.Inparticular,conventionalprofilingworkflows
tance of reproducibility, variance control, and coherent typicallylackexplicitcomponentsfortreatment-effectidenti-
pipelinedesign[36]. fication,response-typelabeling,anduplift-basedevaluation.
Aconceptualgapthereforepersistsbetweenprofilingwork-
flowsandcausal-inferencepipelines.Addressingthisgapis
C. CAUSALINFERENCEINRECOMMENDERSYSTEMS essential for moving beyond static or purely predictive user
ANDTHEUSER-PROFILINGPIPELINE profiles toward representations that capture how users are
Inrecommendersystems,causalinferencehasbeenapplied likelytorespondunderalternativeinterventions.
to address exposure bias, selection bias, and to conduct
policy evaluation [23]. Rather than focusing solely on
predictive accuracy, this stream of work explicitly treats D. GAPSOURWORKADDRESSES
recommendationactionsasinterventionsandevaluatestheir Across the surveyed literatures, two practice-oriented gaps
causaleffectsonuserbehavior.Recentreviewsidentifycore ariserepeatedly.
causalobjectivesalongthreeinterrelateddimensions: First, applications of HTE estimation and Causal Forest
(1)causalobjectives,suchasde-biasingitemexposureand modeling often under-report critical design and tuning
estimatingthetreatmenteffectsofrecommendationactions; decisions,makingitdifficulttoreproduceresultsuniformly
(2) identification strategies, including inverse propen- or determine which components of the pipeline actually
sity scoring (IPS), doubly robust estimation (DR), and contribute to uplift or CATE performance. Rehill [34],
instrumental-variable(IV)approaches; Inoue et al. [35], and Ling et al. [36] show that studies
(3)evaluationparadigms,coveringofflinepolicylearning, frequently rely on heavy default hyperparameters, rarely
counterfactualsimulation,andonlinecontextualbandits. justify identification assumptions, and often omit report-
Together, these components form an integrated end-to- ing clustering or feature-selection strategies. As a result,
end causal pipeline spanning data collection, identification, itremainsunclearwhetherobservedperformancedifferences
policy optimization, and evaluation. This pipeline perspec- stem from causal estimators themselves or from upstream
tive emphasizes decision-oriented evaluation under explicit designchoicessuchasfeatureselection,clustering,orlabel-
interventionsratherthanstaticprediction. ing.Thisleavesunclearwhetherfeatureselection,clustering,
Conversely, traditional user-profiling research remains labeling,orotherdesignchoicesareresponsibleforobserved
largelypredictive.AssummarizedbyWuetal.[8],profiling upliftorCATEperformancedifferences[22].
pipelines typically consist of five sequential components— Second, mainstream user-profiling frameworks are com-
datacollection,datapreprocessing,featureextraction,model- prehensive in data preparation and feature engineering, but
ing,andevaluation—eachoriginallydesignedfordescriptive remain largely descriptive and correlation-based [7], [8].
segmentationorpredictiveaccuracyratherthaninterpretabil- Theygenerallylackcomponentsforcausalestimation,uplift-
ity. Similarly, Maraj et al. [37] argue that most profiling based evaluation, or assignment of causal response types.
VOLUME14,2026 40151

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Consequently,existingprofilingsystemsarenotdesignedto consistency,andreadinessforanalysis[8].Nextcomesfea-
representhowusersareexpectedtorespondunderalternative tureextraction,convertingbehaviorallogsanddemographic
interventions, limiting their suitability for decision-oriented informationintorepresentationssuitableformodeling.
personalization.Thisdisconnectbetweenpredictiveprofiling AlthoughnotshowninFigure1asared-arrowcomponent
andcausalreasoninginhibitsexistingsystemsfromexplain- of its own, feature selection is an essential overhead to this
ing how users will respond to user-level interventions. Yet step, ensuring that only variables with both predictive and
such capabilities are core to adaptive personalization, broad causal relevance move down the causal analysis pipeline.
targetingoptimization,andprescriptiveanalytics. Ekeetal.[4]emphasizethatprofilingbasedonuserbehaviors
To address these gaps, we offer two methodological requiresappropriatechoiceofrepresentativevariables,while
contributions. Wager and Athey [13] warn that it is easy to accept
First, we introduce a module called Four-Type Response predictive but non-causal features with varying predictive
Segmentation, aligned with uplift theory, which uses noise(whichtendstodiluteestimatedtreatmenteffects).CUP
high-confidence uplift thresholds, model-assisted infer- thereforeusesatwo-prongedapproach:informationvaluefor
ence, and post-hoc label refinement to operationalize the predictiveimportance,andcausalimportancefromaCausal
dependence between AAUC-based evaluation metrics and Forestsapproach[13]tostabilizetheinterventions.
response-type labeling [18], [20]. This design explicitly The first truly new component of CUP is clustering
links model evaluation outcomes to interpretable response for stratification, grouping users into behaviorally similar
categories,addressingtheambiguitybetweenrankingperfor- and causally comparable groups. As Wu et al. [8] remark,
manceanduser-levelinterpretationnotedinpriorstudies. ‘‘mostpriorclusteringmethodsforuserprofilingaremainly
Second, we propose improved Causal User Profiling descriptiveandstatic;causalanalysisbenefitsfromgrouping
(CUP) Roadmap, which embeds feature selection, clus- such that the treatment and control users in a group are
tering, confounding adjustment, causal estimation, and balanced in terms of their distributions.’’ This aligns with
response-type labeling into a unified, reproducible, and findings from Devriendt et al. [22], who show that uplift
resource-aware workflow. By structuring these components modelsaresensitivetosampleimbalanceandperformbetter
asanintegratedpipelineratherthanisolatedmodelingsteps, inreliableupliftsegments.Thus,CUP’sclusteringsteptrades
CUP directly responds to reproducibility and transparency off descriptive interpretability for causal validity by pairing
concerns highlighted in the HTE and uplift literature. comparabilitywithsegmentation.
By combining causal inference, uplift modeling, and user Treatment(T)isdefinedasabinaryindicatorofwhethera
profiling into a single analytic pipeline, CUP addresses the userreceivedthetargetedinterventionwithinagivenmonth.
reproducibility issues and methodological silos highlighted Outcome (Y) is defined as whether the user initiated a
inearlierwork,providingaprincipledfoundationforcausal loanapplicationduringthesameevaluationwindow.Causal
userprofiling—anext-generationframeworkfordata-driven effects are estimated—after treatment-control selection—in
personalization,targeting,andinterventiondesign. the next submodule, confounding and bias adjustment. This
step helps ensure that treatment and control groups are
III. RESEARCHFRAMEWORK comparabletopermitcausalattributioninnon-experimental
This paper proposes an integrated methodological frame- settings.Bias-adjustmentmethodsincludeinverseprobability
work, Causal User Profiling (CUP), that connects three weighting(IPW)andstratifiedreweighting(see[6]and[14]).
previously disparate domains—user profiling, causal infer- Through these techniques, CUP mitigates selection bias
ence,andupliftmodeling—intoacommonanalyticpipeline and strengthens internal validity. To ensure comparabil-
for personalized treatment analysis. This comes from our ity between treated and control groups in the empirical
observation that user-profiling studies typically investigate analysis, treatment assignment probabilities are estimated
who the user is, identifying demographic and behavioral using observed covariates and incorporated through inverse
segments [4], [8], while ‘‘for practical intervention it is propensity weighting during uplift evaluation. This adjust-
important to first understand how a user would react if mentmitigatestreatmentimbalancearisingfromnon-random
we act’’ [6]. ‘‘Current user-modeling methods ...focus intervention assignment and reduces bias when comparing
on correlations rather than causal mechanisms,’’ as noted incrementaloutcomesbetweentreatmentarms.
by Purificato et al. [7], which limits their interpretability Next, within the potential-outcomes framework [11],
for strategic targeted interventions. The CUP framework isthecausal-effectestimationmodule.Ourcausalestimation
addresses this issue by embedding causal estimation and follows the standard potential-outcomes framework, which
response-based labeling into the profiling pipeline, turning assumes (i) SUTVA, (ii) conditional ignorability given
thede-factodescriptiveworkflowintoacausallyinterpretable observed covariates, and (iii) overlap (0 < P(T =
andresponse-awareanalyticsystem[22]. 1|X) < 1). Under these identification conditions, IPW
The CUP pipeline (Figure 1) builds on the conventional and DR learners provide consistent estimates of treatment
user-modeling workflow. It starts with data collection: effects. Causal Trees [6] track treatment heterogeneity
behavioralandcontextualdataarecapturedfromproduction using recursive partitioning, and this logic is extended in
platforms,followedbydatapreprocessingtoensurequality, Causal Forests [14]. CATEs (conditional average treatment
40152 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE1. TraditionalversusnewlydesignedCausalUserProfiling(CUP)roadmap.Bluearrowsrepresentthetraditionaluserprofiling
process—DataCollection,DataPreprocessing,FeatureExtraction,Modeling,andPerformanceEvaluation—whileredarrowsrepresentCUP
extensions:ClusteringforStratification,ConfoundingandBiasAdjustment,CausalEffectEstimation,andResponse-TypeLabeling.
effects) are the resulting estimands from such hierarchical Response-type labeling occurs after performance evalu-
estimators.Meta-learningalgorithmssuchasT-,S-,X-,and ation. Using AUUC-based results, users are tagged to the
R-learners [15] restate causal estimation as modular (still fourclassic causal-responsecategories—Persuadables,Sure
supervised-learning) tasks that may be adjusted for cross- Things, Lost Causes, and Do-Not-Disturbs—as defined by
environment flexibility. These estimators output each user’s Radcliffe and Surry [17] and extended by Jaskowski and
upliftvalue(theeffectaninterventionhasonuserbehavior). Jaroszewicz [21]. The result of this post-evaluation process
Following causal estimation, the performance-evaluation is interpreting user-model outputs into actionable causal
submodule measures the captured impact. The Area Under profiles,completingthecausal-profilingloop.
the Uplift Curve (AUUC) is, according to Devriendt et al. CUP brings descriptive profiling and causal inference
[22]andGutiérrezandGérardy[19],thepreferredmetricfor closer together in a single sequence. Preservation of inter-
uplift performance—measuring not predictive accuracy, but pretability from user profiling [4], [8], combined with the
incremental impact captured (see [17]). We denote AUUC structure of causal-effect estimation formalism [6], [15],
as the monthly Area Under the Uplift Curve computed is central to the method, as is adopting the evaluative rigor
withineachevaluationwindow.AAUCreferstotheaverage of uplift modeling [17], [22]. With utility demonstrated on
AUUCacrossthesixmonthlyevaluationsusedinourrolling anInternet-lendingdataset,theCUPframeworkshowshow
experimental design. To interpret user-response behavior causal ‘‘laws’’ can be operationalized within profiling to
and to disentangle module contributions, CUP performs supportpersonalizedanddata-drivendecision-makingunder
component-wise ablation analysis, isolating the per-stage real-worldconstraints.
effectofthefourmodules:featureselection,clustering,bias
adjustment,andcausalestimation.Thisfollowstheprinciple A. FOUR-TYPERESPONSESEGMENTATIONMODULE
that ‘‘uplift performance depends strongly on upstream 1) CONCEPTANDTAXONOMY
design choices’’ [22]. The purpose of the ablation analysis Based on the potential outcomes framework [11], the
inthisstudyisnottoconductformalhypothesistesting,but Four-TypeResponsemoduleassignsuserstofourcanonical
toassesstherelativecontributionandstabilityofindividual causal-response types—Persuadable (A), Sure Thing (B),
pipelinecomponentsunderrepeatedreal-worlddeployments. Lost Cause (C), and Do-Not-Disturb (D). These types
Each ablation experiment removes one component from describehowanindividual’soutcomewouldchangewerethe
the CUP workflow while keeping all others fixed, and intervention present or absent, capturing causal responsive-
performance differences are evaluated consistently across nessratherthanbehavioralsimilarity[17],[20].
six consecutive monthly datasets. By examining whether In contrast to typical segmentation methods that cluster
performance changes persist across time periods rather users based on demographic or behavioral factors, uplift-
than relying on a single snapshot, the analysis provides basedprofilingemphasizesincrementalimpactestimation—
empiricalevidenceonwhetherobservedgainsaresystematic the assessment of how the probability that a user takes the
rather than incidental. Given the operational nature of desiredactionchangeswhenthetreatmentisapplied.Framed
the study and the use of large-scale observational data, in this way, user profiling becomes not merely descriptive,
we focus on temporal consistency and magnitude of perfor- butatreatment-awaredecisionprocess,informingthedesign
mance differences rather than formal statistical significance and evaluation of personalized interventions in marketing,
testing. healthcare,andcredit-analyticsdomains[18],[19],[22].
VOLUME14,2026 40153

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Algorithm1Version1–Uplift-onlyTriage(High/Medium
TABLE2. Behavioralevidencepartitionlinkingtheoreticalresponse
categorieswithobservedtreatment–outcomepatterns. /Low)
Input: Dataset D with column uplift_score u (or u =
pˆ −pˆ ifavailable)
1 0
Output: Triage label ∈ {High,Medium,Low} for each
sample
Protocol:SplitDintooutertrain/valid/test;selectδonvalid
tomaximizeAUUC;freezeδfortest(noleakage)
2) BEHAVIORALEVIDENCEPARTITION
1: foreachi∈Ddo
Toprovideempiricallygroundedbaselinesforthetheoretical 2: ifu i >δthen
response types above, users are partitioned by treatment
3: label ←High
assignment T and outcome Y, resulting in four cells of 4: elseif|u i |<δthen
evidencebasedonobservedbehavioralcongruencyexpected
5: label ←Medium
across the categories (Table 2). This integrates causal
6: else
estimation and response-based labeling into the profiling
7: label ←Low
pipeline, converting the conventional descriptive workflow
8: endif
into a causally interpretable and response-aware analytic
9: endfor
system[22].
Optionalmapping:
This partition restricts theoretical labeling to behavioral
realizability: a user assigned label ‘‘A’’ but found in • ifu i ≥δ →candidateforA(Persuadable)
T = 1,Y = 0(Set 2) would exhibit an anchored • ifu i ≤−δ →candidateforD(DoNotDisturb)
violation of behavioral consistency and would therefore be • if |u i | < δ → candidate region for B/C (resolved by
V2/V3)
de-provisioned of the ‘‘A’’ label (referencing ‘‘refinement’’
from the previous subsection). Such anchoring makes the
Four-Typetaxonomybothcausallyinterpretableandempiri-
callygrounded. b: V2
Thesecondversion(V2)extendstheframeworkbyintroduc-
ingacounterfactualmappingbetweentreatmentandcontrol
3) EVOLVINGTHESEGMENTATIONDESIGNSFOR
outcome probabilities, constructing a two-dimensional pre-
FOUR-TYPERESPONSE(V1-3)
dictionspace:
The Four-Type Response Segmentation module evolved
through three generations of increasing interpretability and pˆ 1 =P(Y =1|T =1,X),
robustnessasweaddressedlimitationsinearlierdesigns.The pˆ =P(Y =1|T =0,X),
0
keymethodologicaldistinctionsaresummarizedconciselyin u=pˆ −pˆ . (2)
1 0
Table3.
Based on calibrated thresholds (yth,yth,δ) users are
1 0
assignedtothefourcanonicalresponsetypesasfollows:
a: V1
This design corresponds closely to the uplift-modeling
Theinitialversion(V1)adoptsasimpletriageapproachthat
literatures[6]and[18]andenablesinterpretabilityasitvisu-
partitions users into High, Medium, or Low responsiveness
groupssolelybasedontheupliftscore: alizes causal responsiveness across probability quadrants.
In reality, however, only a fraction of users are cleanly
pˆ =P(Y =1|T =1,X), segmented into these quadrants; many lie close to decision
1
boundaries, resulting in ambiguous labels or oscillating
pˆ =P(Y =1|T =0,X),
0 between them. V2 therefore has better interpretability than
u=pˆ
1
−pˆ
0
.
V1, but at the cost of robustness, as demonstrated during
 High, u ≥δ, evaluation[22].
 i
label
i
= Low, u
i
≤−δ, (1)
c: V3
Medium, otherwise.
V3 introduces a hybrid causal–behavioral architecture that
uses uplift estimation, behavioral validation, and model
Thisdesignprovidesalightweightwaytoregisterindivid- re-assessment to produce a joint labeling framework. V3
ual sensitivity to intervention and offers a computationally begins with high-confidence lift-based labeling and recon-
inexpensive method for identifying users likely to be ciles theoretical label assignments with empirical behavior,
affected. However, it does not provide structural causal followed by classifier-based refinement to re-label ambigu-
interpretability,norcananypurelyuplift-baseddesign;thusit ousorconflictingcases.
remainsadescriptiveratherthanafullycausalsegmentation The V3 hybrid causal–behavioral procedure consists of
method. fourstages,illustratedbelow:
40154 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
TABLE3. Comparisonofthethreesegmentationdesigns(V1–V3)byinputdependenciesandmethodologicalfocus.
FIGURE2. V3-BasedFour-StageCausalLabelingFramework.
TABLE4. Counterfactualquadrantmappingforfour-typelabeling. Usingthismulti-stageinfusionofupliftprediction,coun-
terfactualreasoning,andbehavioralcorrection,V3produces
causally interpretable and empirically consistent response-
typesegmentation,achievingsignificantAUUCstabilityand
behavioral-consistency improvements over prior versions.
By anchoring response-type assignments to both uplift
estimates and observed (T,Y) behavioral evidence, the V3
designpromoteslabelconsistencyacrosstimewindowswhile
allowing individual users to transition between response
statesastheirbehaviorevolves.
ThissegmentationlogicoftheV3hybridlabelingframe-
workshows:
Whatistheupliftdistribution?
It is partitioned into five pieces by adjustable thresholds,
whichcorrespondtothefourstagesofthelabelingpipeline:
(1)uplift-basedextremesegmentation;
(2)behavioralexpansionofA/Dboundaries;
(3)model-assistedtaggingofambiguouscases;and
(4)finalintegrationandauditing.
Thenetresult:maximumcoverageofAandDuserswhile
keeping (T,Y) behavior consistent across all four response
types.
4) SUMMARYANDDISCUSSION
Thethreeversionsofusersegmentationrepresentajourney
from the very light-handed uplift-based stratification (V1),
VOLUME14,2026 40155

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Algorithm 2 Version 2 – Counterfactual Four-Quadrant Algorithm3HybridLabeling(CompactLayout)
| Segmentation |         |        |         |     |             |     |     | Input:DatasetD,T            |     |     | ∈{0,1},Y | ∈{0,1} |     |     |
| ------------ | ------- | ------ | ------- | --- | ----------- | --- | --- | --------------------------- | --- | --- | -------- | ------ | --- | --- |
|              |         |        |         |     | ),y0_prob(p |     |     | Output:Type∈{A,B,C,D},Flags |     |     |          |        |     |     |
| Input:       | Dataset | D with | columns |     | y1_prob(p 1 |     | 0 ) |                             |     |     |          |        |     |     |
(arm-wisecalibrated); upliftu=p −p Protocol:Train/Valid/Testsplit;maximizeAUUConValid;
|                                            |     |     |     |     | 1 0 |     |     |               |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| Output:Responsetype∈{A,B,C,D}foreachsample |     |     |     |     |     |     |     | freezeonTest. |     |     |     |     |     |     |
Protocol: Outer train/validation/test split; grid-search (A) Arm-wisemodels&Calibration
| (h,ℓ,δ) |     | on validation | to  | maximize | AUUC; |     | fix |        |     |       |                        |     |     |     |
| ------- | --- | ------------- | --- | -------- | ----- | --- | --- | ------ | --- | ----- | ---------------------- | --- | --- | --- |
|         |     |               |     |          |       |     |     | Trainp | 1   | (x)&p | 0 (x);Calibrateperarm. |     |     |     |
(h∗,ℓ∗,δ∗)ontest;dropsamplesviolatingoverlap.
|     |     |     |     |     |     |     |     | u(x)=p |     | −p  | ;dropoverlapviolators. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---------------------- | --- | --- | --- |
1 0
|     | foreachsamplei∈Ddo |     |     |     |     |     |     | (B) Behavioralevidencepartition |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
1:
|     |        | ≥h∗andp                |     | ≤ℓ∗andu | ≥δ∗    |      |     |     |     |     |     |            |       |     |
| --- | ------ | ---------------------- | --- | ------- | ------ | ---- | --- | --- | --- | --- | --- | ---------- | ----- | --- |
| 2:  | if     | p 1,i                  | 0,i |         | i then |      |     |     |     |     |     |            |       |     |
|     |        | label ←A(Persuadable)  |     |         |        |      |     |     |     | S   | ={T | ,Y },S ={T | ,Y }, |     |
| 3:  |        | i                      |     |         |        |      |     |     |     | 1   | 1   | 1 2        | 1 0   |     |
|     |        | ≤ℓ∗andp                |     | ≥h∗andu | ≤−δ∗   |      |     |     |     |     |     |            |       |     |
| 4:  | elseif | p 1,i                  |     | 0,i     | i      | then |     |     |     |     |     |            |       |     |
| 5:  |        | label ←D(DoNotDisturb) |     |         |        |      |     |     |     |     |     |            |       |     |
i
|     | elseif | p ≥h∗andp             |     | ≥h∗and|u | |<δ∗ | then |     |     |     |     |     |            |       |     |
| --- | ------ | --------------------- | --- | -------- | ---- | ---- | --- | --- | --- | --- | --- | ---------- | ----- | --- |
| 6:  |        | 1,i                   |     | 0,i      | i    |      |     |     |     |     | ={T | ,Y },S ={T | ,Y }. |     |
|     |        |                       |     |          |      |      |     |     |     | S 3 | 0   | 1 4        | 0 0   |     |
| 7:  |        | label i ←B(SureThing) |     |          |      |      |     |     |     |     |     |            |       |     |
8: elseif p 1,i ≤ℓ∗andp 0,i ≤ℓ∗and|u |<δ∗ then (C) High/Mid-confidenceA/Drules
i
|     |     | ←C      |             |     |     |     |     |        |     | ,u  |                  |     |     |     |
| --- | --- | ------- | ----------- | --- | --- | --- | --- | ------ | --- | --- | ---------------- | --- | --- | --- |
| 9:  |     | label i | (LostCause) |     |     |     |     | Tune(u |     |     | )onValid.Fori∈D: |     |     |     |
high mid
10: else
|     |     |                          |     |     |                  |     |     |     | a) High-confidencerule. |     |     |     |     |     |
| --- | --- | ------------------------ | --- | --- | ---------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
|     |     | l ab el ←NearestCorner(p |     |     | ,p ;h∗,ℓ∗,sign(u |     | ))  |     |                         |     |     |     |     |     |
1 1 : i 1,i 0,i i I f | u | ≥ u : a s sign A if u > 0, otherwise
|     |      |      |     |     |     |     |     |     | •   | i          | h igh     |     | i   |     |
| --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --- | --- |
| 1 2 | : en | d if |     |     |     |     |     |     |     |            |           | <   |     |     |
|     |      |      |     |     |     |     |     |     |     | a ss i g n | D i f u i | 0 . |     |     |
13: endfor
return {label } b) Mid-confidence behavioral expansion. Else,
| 14:                                                 |     | i   |     |     |     |     |     |     |        |          |                       |             |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------------------- | ----------- | --- | --- |
|                                                     |     |     |     |     |     |     |     |     | checku |          | -behaviorconsistency: |             |     |     |
| Note:Figure2bpresentstheconceptualdiagramofcounter- |     |     |     |     |     |     |     |     |        | mid      |                       |             |     |     |
|                                                     |     |     |     |     |     |     |     |     | •      | Ifu i ≥u | mid &(S               | 1 orS 4 )→A |     |     |
factualsegmentationunderV2.
|     |     |     |     |     |     |     |     |     | •   | Ifu ≤−u |     | &(S orS | )→D |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     | i       | mid | 2       | 3   |     |
Elseconflict→AD_conflict
•
TABLE5. StagesandfunctionalRolesintheV3causallabeling (D) InitialB/Cwithconflictflags
framework.
Forremainingi:
|     |     |     |     |     |     |     |     |     |       | =1:(u | <−u | ?B_conflict:B) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | -------------- | --- | --- |
|     |     |     |     |     |     |     |     |     | • IfY |       | i   | conf           |     |     |
>u
|     |     |     |     |     |     |     |     |     | • IfY | =0:(u |     | ?C_conflict:C) |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | -------------- | --- | --- |
i conf
Model-assistedA↔Drefinement
(E)
TrainClassifieronStep(C)labels(stratified).
|     |     |     |     |     |     |     |     | ReassignifProb≥τ |     |     |     | &consistentquadrant. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | -------------------- | --- | --- |
AD
|     |     |     |     |     |     |     |     | (F) Model-assistedB↔Crefinement |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- |
UsecleanB/Cfrom(D)assupervision.
Train/CalibrateBvsCmodels.
|     |     |     |     |     |     |     |     | Refineifconsensus≥τ |     |     |     | .   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
BC
|     |     |     |     |     |     |     |     | (G) Output |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Returnfinallabels,conflicttypes&diagnostics.
|     |     |     |     |     |     |     |     | Note:  | Figure   | 2c presents |      | the conceptual | diagram    | of the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ----------- | ---- | -------------- | ---------- | ------ |
|     |     |     |     |     |     |     |     | hybrid | labeling | workflow    | (P3) | combining      | confidence | rules  |
andmodelrefinement.
throughthemorecomplexcounterfactualsegmentation(V2), B. IMPROVEDEXPERIMENTALDESIGN
tothecausal–behavioralhybridrefinement(V3)withwhich Re-approaching uplift modeling as an evaluation of user
the final design aligns. The addition of counterfactual profiling, the improved experimental design strengthens the
estimation and user profiling into the approach of V2 reasoning behind how components of uplift modeling work
makes the return to descriptive profiling reach toward a together.Ratherthaniterativelyoptimizingasinglepredictive
causal user-description framework that is interpretable and model,wereframetheassessmentofinterventionapproaches
groundedinthedata.Thisjourneyreflectshowtheprinciples andrefineallmethodologicalcomponents(featureselection,
of causal inference can help operationalize user profiling, clustering, causal estimation, response labeling), each of
bridgingincremental-impactmodelingwithbehavioralreal- which shapes the overall Area Under the Uplift Curve
ism to support decision-making within systems that rely on (AUUC). With a structured modular approach in place, the
interventions. pipeline evaluation allows us to identify how components
| 40156 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
work together transparently, ensuring that an uplift-based Regression often serves as the baseline learner for com-
user-profilingpipelineisreproducibleandasinterpretableas putational efficiency, while Random Forests, GBDT, and
| possible. |     |     |     |     |     |     | XGBoostareemployedassanitychecks.Eachlearner’sout- |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
putsarethenpassedtotheFour-TypeResponseSegmentation
|     |     |     |     |     |     |     | Module | (Section | III-B) | to yield | CATE/uplift |     | scores | tagged |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------ | -------- | ----------- | --- | ------ | ------ |
1) PIPELINEOVERVIEW
withbehavioralnamesorinterpretabletypes.
| The framework |     | for | user | profiling | is based | on causal |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | ---- | --------- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Inafinalsteptofacilitatecausalinterpretability,wecluster
| principles. | Following |     | from causal | user | profiling, | we add to |            |          |             |     |         |             |     |      |
| ----------- | --------- | --- | ----------- | ---- | ---------- | --------- | ---------- | -------- | ----------- | --- | ------- | ----------- | --- | ---- |
|             |           |     |             |      |            |           | users into | causally | homogeneous |     | strata. | Recognizing |     | that |
thepipeline(Figure3)auser-profilingand‘‘de-causalizing’’
|             |       |     |            |            |     |               | real-world | behavioral |     | heterogeneity |     | drives | treatment-effect |     |
| ----------- | ----- | --- | ---------- | ---------- | --- | ------------- | ---------- | ---------- | --- | ------------- | --- | ------ | ---------------- | --- |
| methodology | based |     | on feature | uniqueness |     | and response. |            |            |     |               |     |        |                  |     |
variation,CUPemploysK-Meansclusteringonstandardized
| In particular,     | clustering, |     | causal   | estimation,      |     | user profiling, |            |         |            |                 |     |            |         |         |
| ------------------ | ----------- | --- | -------- | ---------------- | --- | --------------- | ---------- | ------- | ---------- | --------------- | --- | ---------- | ------- | ------- |
|                    |             |     |          |                  |     |                 | features   | to form | stable     | subpopulations, |     | each       | serving | as a    |
| and component-wise |             |     | ablation | are incorporated |     | to quantify     |            |         |            |                 |     |            |         |         |
|                    |             |     |          |                  |     |                 | contextual | unit    | for uplift | estimation      |     | [8], [22]. | The     | optimal |
contributions.
|                 |     |              |         |               |              |           | number    | of clusters | K        | is chosen | via              | elbow   | and  | silhouette |
| --------------- | --- | ------------ | ------- | ------------- | ------------ | --------- | --------- | ----------- | -------- | --------- | ---------------- | ------- | ---- | ---------- |
| Operating       | on  | a            | monthly | rolling       | basis—across | both      |           |             |          |           |                  |         |      |            |
|                 |     |              |         |               |              |           | criteria. | Clusters    | below    | 2%        | of total         | samples | or   | yielding   |
| cross-sectional |     | and temporal |         | vigilance—the | pipeline     | allows    |           |             |          |           |                  |         |      |            |
|                 |     |              |         |               |              |           | AUUC      | lower       | than the | baseline  | are              | merged  | into | others.    |
| examination     | of  | how feature  |         | selection,    | clustering,  | response- |           |             |          |           |                  |         |      |            |
|                 |     |              |         |               |              |           | Notably,  | clustering  |          | enhances  | interpretability |         | and  | reveals    |
interactioninformation,andcausaladjustmentworktogether
behavioralregimesthatwouldotherwiseremainhidden.
| as individual | components |             | of  | a Causal | User Profiling | (CUP)      |     |     |     |     |     |     |     |     |
| ------------- | ---------- | ----------- | --- | -------- | -------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
| pipeline.     | All        | experiments |     | share a  | common         | time-based |     |     |     |     |     |     |     |     |
3) EVALUATIONANDABLATIONDESIGN
| train/validation/test |     | protocol |     | with shared | random | seeds and |     |     |     |     |     |     |     |     |
| --------------------- | --- | -------- | --- | ----------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisevaluationprocedurequantifieshoweachdecisioneither
| fixed preprocessing |                 | across | months,       | highlighting |     | that these  |          |      |           |            |          |        |              |          |
| ------------------- | --------------- | ------ | ------------- | ------------ | --- | ----------- | -------- | ---- | --------- | ---------- | -------- | ------ | ------------ | -------- |
|                     |                 |        |               |              |     |             | promoted | or   | detracted | from       | ultimate | uplift | performance. |          |
| choices             | drive stability |        | and practical | reliability  |     | in modeling |          |      |           |            |          |        |              |          |
|                     |                 |        |               |              |     |             | We use   | area | under     | the uplift | curve    | (AUUC) | as           | the core |
userprofilingunderthecausalframework.
|     |     |     |     |     |     |     | performance |       | measure, | as well | as the      | Qini | coefficient | and     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | -------- | ------- | ----------- | ---- | ----------- | ------- |
|     |     |     |     |     |     |     | uplift@k    | [17], | [19],    | [22].   | We separate |      | marginal    | effects |
2) COREMODULES:FROMFEATURESELECTIONTOCAUSAL
|     |     |     |     |     |     |     | through | component-wise |     | ablation | (e.g., | removing |     | the clus- |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --- | -------- | ------ | -------- | --- | --------- |
ESTIMATION tering,causalfeatureselection,orlabelrefinementmodule).
The pipeline begins by identifying features that are both Performanceisevaluatedbothgloballyandbycluster,using
stable and causally relevant, allowing us to draw causal aweightedmetric:
| insights | generalizable |     | to unseen | treatment | groups. | A multi- |     |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | --------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
K
| stageselectionprocesscombinesstatisticalrelevance(Infor- |     |               |     |           |             |           |     |               |     |     | X   |       |     |     |
| -------------------------------------------------------- | --- | ------------- | --- | --------- | ----------- | --------- | --- | ------------- | --- | --- | --- | ----- | --- | --- |
|                                                          |     |               |     |           |             |           |     | WeightedAUUC= |     |     | w   | ·AUUC | ,   | (3) |
|                                                          |     |               |     |           |             |           |     |               |     |     |     | k     | k   |     |
| mation Value,                                            |     | IV), temporal |     | stability | (Population | Stability |     |               |     |     |     |       |     |     |
k=1
| Index, PSI), | and | causal   | importance  | (Causal |       | Forest variable |        |                                                |     |     |     |     |     |     |
| ------------ | --- | -------- | ----------- | ------- | ----- | --------------- | ------ | ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
|              |     |          |             |         |       |                 | wherew | k denotestherelativeproportionofvalidsamplesin |     |     |     |     |     |     |
| importance   | and | stepwise | regression) |         | [13]. | This produces   |        |                                                |     |     |     |     |     |     |
clusterk.
| multiple | feature | sets from | the | base DataFrame: |     | IV-only/PSI |     |     |     |     |     |     |     |     |
| -------- | ------- | --------- | --- | --------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
subsets,CF-only/PSI,andhybridtypes(IV+CF,IV+CF Otherdiagnosticsinclude:
+STEP).Theaimistoobtainaparsimonioussetoffeatures Labeladherencerates(band,quadrant,andbehavioral-
•
representativeofthepopulation,standardizedandimputedon cellconsistency)
thesamefoldstoensurefairnessandcausalinterpretability. • Type-wise outcome balance between treatment and
Before uplift estimation, we must address any remaining controlgroups
κ
treatment-control imbalances, often done using Propensity • Temporal stability measured via Cohen’s across
months
| Score Matching |     | (PSM) | and | Inverse Probability |     | Weighting |     |     |     |     |     |     |     |     |
| -------------- | --- | ----- | --- | ------------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
(IPW) [10], [38]. These covariate-adjustment techniques • Computationalefficiency(runtimeandconvergence)
reweight samples to render treated and control groups We computed robustness via bootstrap confidence inter-
comparable so that the uplift reflects the genuine treatment vals, out-of-time validation, and selective sweeps through
effect rather than asymmetries in treatment allocation (i.e., subsampleswhentheuplifttheycontainedappearederratic.
selection bias). For randomized subsets, they also serve as We performed all experiments with fixed random seeds,
a sanity check for stability: estimated uplift effects should version-controlled datasets, and standardized preprocessing
confirmconfoundingcontrol. pipelines. We took comprehensive logs of AUUC, variable
Uplift estimation is conducted using two families of importance,andclusterdiagnosticsfromeachrun,andthen
models: meta-learners and Causal Forests. Meta-learners stitched together the pieces. This provided a transparent
such as T-, S-, X-, R-, and DR-learners factor CATE ‘‘causal audit trail’’ enabling independent replication of our
| estimationintomodularsupervised-learningtasks[14],[15], |     |     |     |     |     |     | results. |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
while Causal Forests provide nonparametric and asymptoti- To avoid ad-hoc decisions outside the evaluation frame-
callyconsistentestimatesofheterogeneoustreatmenteffects work,wemadereproducibilityafoundationwithinourevalu-
[16]. To preserve causal integrity, all learners share the ationratherthanseparateitoutasitsownstage.Thistrade-off
same preprocessing, data, and evaluation strategy. Logistic between methodological rigor and operational reliability
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 40157 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE3. ImprovedexperimentalpipelineoftheCausalUserProfiling(CUP)framework.Thepipelineintegratesfeatureselection,
clustering,confoundingadjustment,causaleffectestimation,andevaluationintoareproducibleworkflowexecutedinmonthlyrolling
loops.
wasempiricallyobserved:thisevaluationstrategystabilized status—including both static user attributes and dynamic
the AUUC variance across monthly slices. It reduced the financial indicators—comprising: gender, age, and city tier;
damage from confounding-driven fluctuations while giving borrowing frequency; repayment performance; credit-line
usareliablemeasureoftruetreatmentheterogeneity. utilizationlimits;overduehistoryandrepaymentdiscipline;
|     |     |     |     |     |     | and consumption-related |     | activity. | These | variables |     | capture |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --------- | ----- | --------- | --- | ------- |
C. SUMMARY treatment heterogeneity and user-specific behavior in gen-
| In this chapter | we  | presented | an enhanced | experimental |     | eral. |     |     |     |     |     |     |
| --------------- | --- | --------- | ----------- | ------------ | --- | ----- | --- | --- | --- | --- | --- | --- |
Priortomodelfitting,severalprocedureswereconducted
designthatintegratesbothcausalinferenceanduserprofiling
into a single uplift-modeling approach. The Four-Type to improve comparability and robustness within and across
Response Segmentation Module guarantees causal labeling potentialcovariates.Followingbusinessconventions,missing
robustness, while component-wise ablation analysis gauges or invalid values were set according to domain logic;
thecontributionofeachmethodologicalcomponent—feature numerouscontinuousfeatureswerescaledfornumericcom-
|                        |     |            |               |     |            | parability; | and feature | selection | was | subsequently |     | applied |
| ---------------------- | --- | ---------- | ------------- | --- | ---------- | ----------- | ----------- | --------- | --- | ------------ | --- | ------- |
| selection, clustering, |     | and causal | estimation—to |     | the uplift |             |             |           |     |              |     |         |
score.Allofthisisimplementedinoneconsolidatedprocess through a diagnostic three-stage procedure consistent with
thatweavesevaluationandreproducibilitytogether,thereby previously documented theory [22]. This screening stage is
laying the groundwork for a transparent, interpretable, and performed before constructing the downstream feature-set
empiricallyvalidatedbasisfordynamiccausaluserprofiling. configurations (e.g., IV-only, Causal, and hybrid sets),
|     |     |     |     |     |     | ensuring | that all reported | feature | sets | are derived | from | the |
| --- | --- | --- | --- | --- | --- | -------- | ----------------- | ------- | ---- | ----------- | ---- | --- |
IV. DATADESCRIPTION samefilteredandstability-checkedcandidatepool:
In our empirical analysis we employ proprietary data 1. Information Value (IV) was computed to quantify
predictiverelevanceforthetargetoutcome.
| collected from | users | of a leading | Chinese | internet | finance |     |     |     |     |     |     |     |
| -------------- | ----- | ------------ | ------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
platform’s mobile app. To enable causal interpretability, 2. Population Stability Index (PSI) was used to evaluate
|     |     |     |     |     |     | temporal | stability and | detect | distributional |     | shifts | across |
| --- | --- | --- | --- | --- | --- | -------- | ------------- | ------ | -------------- | --- | ------ | ------ |
weconsideronlyactiveborrowers,i.e.,userswithoutstand-
| ing loan balances |     | in the observation | window. | Compared | to  | months. |     |     |     |     |     |     |
| ----------------- | --- | ------------------ | ------- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- |
non-borrowers(whoarenotindebtedorhavesatisfiedprior 3.Pairwisecorrelationanalysisidentifiedredundantvari-
ablesandmitigatedmulticollinearity.
| loan demands), | active | borrowers | are more | homogeneous: |     |     |     |     |     |     |     |     |
| -------------- | ------ | --------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
they seek credit more consistently, reducing the number of Variables having IV < 0.05 or PSI > 0.25 were dropped,
|                      |     |         |                |     |           | and features | were merged | when | their | pairwise | correlation |     |
| -------------------- | --- | ------- | -------------- | --- | --------- | ------------ | ----------- | ---- | ----- | -------- | ----------- | --- |
| possible confounders |     | arising | from variation | in  | borrowing |              |             |      |       |          |             |     |
motives. By ensuring behavioral comparability between exceeded 0.8 in absolute terms. This process produced
treated and control users, this focus improves the power of a balanced set of features encompassing interpretability,
|     |     |     |     |     |     | robustness, | and predictive | capability—in |     | line | with | recent |
| --- | --- | --- | --- | --- | --- | ----------- | -------------- | ------------- | --- | ---- | ---- | ------ |
causalidentification.
The dataset consists of an intermingled trove of infor- methodological standards in heterogeneous treatment-effect
researchforsimilarusecases[41].
| mation covering |     | demographic | behavior | as well | as credit |     |     |     |     |     |               |     |
| --------------- | --- | ----------- | -------- | ------- | --------- | --- | --- | --- | --- | --- | ------------- | --- |
| 40158           |     |             |          |         |           |     |     |     |     |     | VOLUME14,2026 |     |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Algorithm 4 Core Experimental Loop (Baseline and the strongest predictive power, mirroring previous research
Clustering-Enabled) showing that dynamic behavioral attributes are highly pre-
| Input:DatasetD;FeatureSets{F |     | ,...,F | };  |     |     |     |     |     |
| ---------------------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
1 6 dictive of treatment responsiveness. Correlation diagnostics
Metalearners {T, S, X, DR, CF}; Baselearners {LR, RF, confirmthatweeffectivelycontrolledformulticollinearity.
| GBDT,XGB};Months{M |     | ,...,M | }   |     |                  |             |                     |       |
| ------------------ | --- | ------ | --- | --- | ---------------- | ----------- | ------------------- | ----- |
|                    |     | 1      | 6   |     | These procedures | ensure that | the empirical model | iden- |
Output:AUUCscores;clusterstatistics;variableimportance tifies true behavioral heterogeneity rather than confounding
foreachmonthm⊆{M ,...,M }do arisingfromunstableorsuperfluouspredictors.Insummary,
| 1:  |     | 1   | 6   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
2: D ←subset(D,month=m) thedatasetunderwentasystematicandjudiciousfilteringand
m
foreachfeaturesetF inFeatureSetsdo refinement process consistent with best practices in causal
3:
,F);
4: X ← select_features(D m T ← treatment; inference and comparable recent works in the literature.
Y ←outcome The resulting analysis environment is stable, representative,
∈Metalearnersdo andamenabletoestimatingheterogeneoustreatmenteffects,
5: foreachML
6: foreachBL ∈Baselearnersdo as well as to implementing causal models of users in
|     | ifclustering_enabledthen |     |     |     | subsequentsections. |     |     |     |
| --- | ------------------------ | --- | --- | --- | ------------------- | --- | --- | --- |
7:
clusters←KMeans(X,K)
8:
9: foreachclustercinclustersdo A. SEGMENTATIONANDDISTRIBUTIONOFFOUR
| 10: | ifvalid_cluster(c)then |     |     |     | RESPONSETYPES |     |     |     |
| --- | ---------------------- | --- | --- | --- | ------------- | --- | --- | --- |
11: model ←train(ML,BL,X ,T ,Y ) This section presents the empirical results of the Four-Type
|     |     | c   |     | c c c |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
score ← Response Segmentation Module introduced in Chapter 3,
| 12: |     | c   |     |       |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     |     |     | ,X  | ,T ,Y |     |     |     |     |
evaluate_AUUC(model c c c c ) illustrating how uplift-based causal labeling emerges in the
13: else dataset.Withinthecausaluser-profilingframework,usersare
skip
| 14: |     |     |     |     | segmentedbasedontheirIndividualTreatmentEffect(ITE) |     |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------- | --- | --- | --- |
15: endif underthepotential-outcomesmodel.Inparticular,wedefine
|     | endfor |     |     |     | fourcanonicalresponsetypesas: |     |     |     |
| --- | ------ | --- | --- | --- | ----------------------------- | --- | --- | --- |
16:
clusters←merge_low_AUUC(clusters)
| 17: |      |     |     |     | • Persuadables(TypeA):performthetargetactiononly |     |     |     |
| --- | ---- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- |
| 18: | else |     |     |     |                                                  |     |     |     |
iftreated
model ←train(ML,BL,X,T,Y)
19:
|     | score←evaluate_AUUC(model,X,T,Y) |     |     |     |     | =1,y | =0) |     |
| --- | -------------------------------- | --- | --- | --- | --- | ---- | --- | --- |
| 20: |                                  |     |     |     |     | (y 1 | 0   |     |
endif
21:
• SureThings(TypeB):performtheactionregardlessof
| 22: | endfor |     |     |     |     |     |     |     |
| --- | ------ | --- | --- | --- | --- | --- | --- | --- |
treatment
23: endfor
endfor
| 24: |     |     |     |     |     | (y =1,y | =1) |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- |
|     |     |     |     |     |     | 1       | 0   |     |
25: endfor
LostCauses(TypeC):neverperformtheaction
•
|             |            |         |             |          |                | (y =0,y   | =0) |     |
| ----------- | ---------- | ------- | ----------- | -------- | -------------- | --------- | --- | --- |
|             |            |         |             |          |                | 1         | 0   |     |
| Descriptive | statistics | for our | dataset are | shown in |                |           |     |     |
|             |            |         |             |          | Do Not Disturb | (Type D): |     |     |
Table4-1.Thedatasetcontainsapproximately720,000user- • perform the action only if
nottreated
monthsgeneratedfromsixcalendarmonths.Thesix-month
| window reflects | a practical | trade-off   | between      | behavioral |     |         |     |     |
| --------------- | ----------- | ----------- | ------------ | ---------- | --- | ------- | --- | --- |
|                 |             |             |              |            |     | (y =0,y | =1) |     |
|                 |             |             |              |            |     | 1       | 0   |     |
| stability and   | sample      | coverage in | a real-world | lending    |     |         |     |     |
system, providing repeated exposure to interventions for Thistypologyprovidesconceptualclaritytoheterogeneous
temporal robustness checks while limiting structural drift behavioral patterns and enables causal modelling, tailored
in user composition and platform policy. All loans have a interventionstrategies,andmarketingresourceallocationto
mean utilization rate of 62.8% (SD = 24.5%), indicating beginconceptually.Inpractice,thefrequencyoftypesacross
behavioral heterogeneity. An average repayment-timeliness users is summarized in Figure 5a. There are significantly
index of 0.91 reflects a disciplined borrower population. more Persuadables and Lost Causes relative to Sure Things
Approximately78%ofusersliveinatier-2orlower-tiercity. in the user population, meaning that there are slightly more
Users in the treatment group appear to exhibit somewhat people who will change behaviour under some treatment
higher utilization and higher-frequency engagement than than will remain the same across any treatment; but the
usersinthecontrolgroup,implyingheterogeneousinterven- mostobservationsareofuserswhoareresistanttotreatment.
tion responses relevant for uplift analyses. Feature stability Sure Things should have stable demand, although—as with
andrelevancediagnosticsfurtheraffirmtherobustnessofthis everythingelse—theyshouldbegivenequalratesofexposure
variableset:theaverageIVacrossretainedfeaturesis0.23, in the broadest possible sense of the term. Do-Not-Disturb
and the average PSI is 0.07, both within accepted stability users are a hindrance, and serve as an indicator of potential
bounds [42]. Behavioral and repayment indicators have adverse intervention effects, serving as a caution against
| VOLUME14,2026 |     |     |     |     |     |     |     | 40159 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | ----- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE4. WorkflowofDataPreprocessingandVariableSelection.Note.Theworkflowdepictssequentialdatapreparationsteps:Raw
DataCollection→DataCleaningandMissingValueTreatment→NormalizationandStandardization→IVComputation→PSIEvaluation
→CorrelationFiltering→FeatureRetentionforModeling.
TABLE6. Descriptivestatisticsofthesample.
over-targeting and treatment fatigue, even if they constitute whereasCausalfeaturesassistwithoverallmodelstability,
onlyasmallportionofthetotalcohort. particularlyforthelargerDR-Learner.
To make even clearer how this segmentation might Because benefits come from different sources, it is not
typically be done, Figure 5b plots the empirical joint obvious a priori how the responses will sort themselves
|     |     | ,y  |     |     |     |     |     |     | +   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distributionof(y 0 1 )andnotesthefourdecisionregionsas out when combining them. The IV Causal set produces
dictatedbythepotential-outcomesformulation. the overall highest mean AUUC—validating that ‘‘picking
|     |     |     |     |     |     | dimensions | gives you information |     | gain, and picking | good |
| --- | --- | --- | --- | --- | --- | ---------- | --------------------- | --- | ----------------- | ---- |
dimensionsgivesyoucausalrelevance.’’Oncethisouter-join
B. EMPIRICALEVALUATIONOFTHECUPFRAMEWORK
|     |     |     |     |     |     | set of dimensions | is added, | Stepwise | refinement | can then |
| --- | --- | --- | --- | --- | --- | ----------------- | --------- | -------- | ---------- | -------- |
ThissectiondescribestheempiricalevaluationoftheCausal
|                |     |       |            |              |             | be incorporated. | These hybrid          | sets            | exhibit slightly | lower    |
| -------------- | --- | ----- | ---------- | ------------ | ----------- | ---------------- | --------------------- | --------------- | ---------------- | -------- |
| User Profiling |     | (CUP) | framework. | We evaluated | each of the |                  |                       |                 |                  |          |
|                |     |       |            |              |             | mean AUUC        | but are less volatile | month-to-month, |                  | yielding |
corecomponentsofCUP—featureselection,clustering,and
smalleruplift-consistency(UC)indices.Althoughtheirmean
meta-learnerconfiguration—individuallyandasacombined
AUUCismarginallylower,theabilitytodependonthemodel
| system | to assess | their | influence | on uplift | performance, |     |     |     |     |     |
| ------ | --------- | ----- | --------- | --------- | ------------ | --- | --- | --- | --- | --- |
producingsimilarresultsacrossmonthsisworththetrade-off
asmeasuredbytheAreaUndertheUpliftCurve(AUUC).
inmeanvalues.
Insummary:
1) FEATURESELECTIONANDUPLIFTPERFORMANCE IV + Causal accelerates accuracy at the cost of some
| To explore | how | variable | screening | affects | heterogeneous | stability. |     |     |     |     |
| ---------- | --- | -------- | --------- | ------- | ------------- | ---------- | --- | --- | --- | --- |
treatment-effectestimation,sixfeaturesetswerecompared: IV + Causal + Stepwise favours stability at the cost of
| ALL—allvariables; |     |     |     |     |     | someaccuracy. |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- |
IV—selectedbyinformationvalue; The second approach is more deployment-ready and is
Causal — chosen by causal-forest importance and PSI therefore used as ‘‘the features’’ moving forward. Across
stability;
|     |     |     |     |     |     | learners | as well, the meta- | and | base-learners | perform |
| --- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | ------------- | ------- |
Stepwise—retainedthroughcross-fittedregression; relativelyconsistently.LogisticRegression(LR)standsoutas
IV+Causal—intersectionofthefirsttwo; thestrongestbaselearnerunderthehybridfeaturesets,while
IV+Causal+Stepwise—thehybridrefinement.
tree-basedlearnersshowweaknesswhennoiseremainsinthe
Findingsshowthatappropriatevariableselectioniscritical embeddings. Therefore, feature selection forms the skeletal
| to uplift | modeling. | Using |     | ALL resulted | in the lowest |     |     |     |     |     |
| --------- | --------- | ----- | --- | ------------ | ------------- | --- | --- | --- | --- | --- |
structureforCUP.
| mean AUUC |        | and the | highest | variance—it     | appears that   |     |     |     |     |     |
| --------- | ------ | ------- | ------- | --------------- | -------------- | --- | --- | --- | --- | --- |
| when the  | models | must    | learn   | in the presence | of substantial |     |     |     |     |     |
noise, it severely weakens identification with respect to the 2) CLUSTERINGSTRATEGIESANDAUUCENHANCEMENT
heterogeneouseffectsthemselves. Clustering was introduced to investigate local treatment
BothIVandCausalselectionsproducemeaningfullybetter heterogeneity independent of an explicit association with
resultsthanthebaseline,butindifferentways: outcomes, consistent with the notion that subgroups with
IV features push the AUUC higher on the simpler meta- different causal effects can be mapped out by recursive
learners(T-andX-Learners), partitioning[6].Theempiricalresultssuggestthatclustering
| 40160 |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE5. Empiricaldistributionoffourcausalresponsetypes(left)andjointdistributionofpotentialoutcomes(y0 ,y1)
illustratingABCDregions(right).
is helpful but is conditional rather than absolute, and as a weakclusterswithglobalpredictions,C2hasaregularizing
consequenceshouldbeusedcautiously. effect, balancing local adaptivity and global stability. This
The contrast between Direct, C1 (Merging), and C2 variance-reducing characteristic maps onto the findings of
(Replacement) shows a clear trade-off. The Elbow Method Devriendt et al. [22], who show that ‘‘ensemble-style’’
suggests optimal clusters around K=6, at which point upliftmodelsproducelowervariance(andgreaterreliability)
the silhouette score levels off (see Figure 7a). This is than ‘‘isolated’’ two-model structures. In our case, Direct
parsimonious and easy to interpret, and we derive clusters identifies behavioral heterogeneity but does not produce
followingthisthroughoutouranalysis. stable models. C1 reduces this variance somewhat, but part
Across the three methods, the C2 step is consistently the of it remains. Empirically, the clustering order is C2 > C1
strongest, yielding the highest uplift effect: mean AUUC >Direct(seeFigure7b),placingclusteringasarefinement
(≈0.09)withthelowestvariance(±0.01).By‘‘replacing’’ ratherthanarequisite.
VOLUME14,2026 40161

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE6. Evaluationoffeature-selectionstrategiesandmeta-learnerinteractionsinupliftmodeling.
(a)BoxplotsofAUUCvaluesacrosssixfeaturesets,illustratingperformancevariabilityacross
configurations.(b)TemporalmeanAUUCoversixmonthscomparingIV+CausalandStep_IV+Causal
featuresets,withthelowerpanelshowingthepopulationstandarddeviationofAUUCacrossmonths
toevaluatetemporalstability.(c)HeatmapofMeta-Learner×Feature-Setinteractions,showing
averageAUUCvaluesfordifferentlearner-featurecombinations.TheDR-Learnerachievesthehighest
upliftperformanceunderIV+CausalandStep_IV+Causalfeatureconfigurations.(d)Standard
deviationofAUUCacrosspairedfeatureconfigurations,illustratingthevariance-reductioneffectof
stepwiserefinement.
40162 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
Clustering interacts differently with the various meta- set. Among the meta-learners, the DR-Learner consistently
learners. As reflected in Figure 7c, the X-Learner shows produced the highest mean AUUC, albeit with higher
the most robust and consistent improvement, reflecting its varianceacrossmonths,indicatingrobustnessinpointperfor-
theoretical gain in segmented or unbalanced samples [15]. mancebutsensitivitytotemporalfluctuations.TheX-Learner
Incontrast,theDR-LearnerandT-LearnershowAUUCdrops offers strong competition, particularly under treatment-
or inconsistencies after clustering, and the Causal Forest imbalance situations, whereas the T- and S-Learners are
(CF) even experiences extreme performance deterioration. farmoreunreliableincomplex,high-varianceenvironments.
Thisisconsistentwithearlierfindingsthattree-basedcausal Amongthebaselearners,LogisticRegression(LR)performs
estimators lose efficiency when subgroup sample sizes are bestintermsofstabilityandinterpretability,whiletree-based
small or unbalanced [13], [35] —meta-learners capable of learnersexhibitsubstantiallymorevariabilityoverall.
‘‘cross-arm information sharing’’ (such as the X-Learner)
remain stable under segmentation, whereas others are sen- 4) OPTIMALPATHWAYANDOVERALLEFFECT
sitive to fragmentation. Figure 7d illustrates cluster-level Putting all these pieces together, the final CUP workflow
performance under the X-Learner. As expected, clustering uses a hybrid IV + (Causal ∩ Stepwise) feature-selection
amplifies both signal and noise: some cluster-level AUUC design, employs the C2 ‘‘replacement strategy’’ with a
values improve substantially, while others drop sharply. moderate number of clusters K, and adopts a DR-Learner
This follows the familiar ‘‘variance-amplifying effect,’’ withLogisticRegressionasthemodelingconfiguration.This
wheresmallersubsamplesincreasebothestimationbiasand integrated pathway yields a large and stable improvement
variance[13].Thus,clusteringuncoverslatentheterogeneity in AUUC relative to the baseline (‘‘all features + no
butcanalsoamplifyrandomnoise,helpingtoexplainwhyits clustering + standard learner’’). The main performance
performancevariesacrossdatasetsandtimeperiods. gains come from variables that are informative (high IV)
The effectiveness of clustering depends critically on the and causally relevant, and the C2 approach provides a
feature space used. In Figure 7, clustering derived from form of structural regularization that prevents overfitting
the Causal feature set yields the most consistent gains, andstabilizesheterogeneoustreatmentestimation.Together,
outperforming clustering based on IV-only or ALL-variable these components lead to a balanced pipeline that improves
feature sets. This indicates that clustering is effective only bothaccuracyandinterpretability.
when the feature space encodes causally relevant informa- Quantitatively, each module of the CUP framework
tion:causalfeaturesyieldamorecoherentandinterpretable contributes a distinct and measurable improvement to uplift
mapoftheunderlyingterrain,enablingclusteringtoidentify performance. Feature selection alone increases AUUC by
more precise treatment heterogeneity [43], [44]. To recap: approximately 25–30%, reflecting the value of filtering
causal features structure the space, and clustering amplifies out noisy predictors and emphasizing causally important
heterogeneity. Clustering based solely on predictive or variables.IncorporatingC2clusteringprovidesanadditional
correlation-drivenvariablestendstoamplifynoise. 10–12% gain by stabilizing weak clusters and harmonizing
Clusteringdoesnotuniversallyimproveoutcomes.Itpro- local heterogeneity with global patterns. Optimizing the
ducesawidespreadinAUUCacrossclusters;improvement meta/baseconfiguration(DR-Learner+LogisticRegression)
in some clusters may be accompanied by deterioration in yields a further 5–8% improvement, enhancing robustness
others. This dual-edged nature makes clustering powerful while maintaining interpretability. Cumulatively, the inte-
but dangerous. Clustering should be viewed as a ‘‘positive grated CUP workflow achieves roughly 45–50% higher
calibrationmechanism,’’effectiveonlywhenstronglyrooted AUUC than the standard uplift-modeling baseline, demon-
in causal features and paired with robust learners (such as stratingthateachcomponentcontributesaclearandpersistent
the X-Learner) that remain stable under segmentation. Its incrementacrossthesixmonthlyslices.
feedback on the Four-Type causal segmentation (Persuad-
able,SureThing,LostCause,Do-Not-Disturb)mustalsobe V. DISCUSSION
monitored, as behavioral balance can be distorted through The empirical validation of the framework demonstrates
subgroupredistribution. thatcausalinferenceandupliftmodellingcanberigorously
In summary, clustering improves uplift estimation only brought to bear on user analytics, closing a classic gap in
‘‘under reasonably complete causal feature structures’’ and theanalyticsspacebetweenpredictionandintervention.This
with‘‘meta-learnersthatremainstableundersegmentation.’’ sectiondiscussestheempiricalfindingsinrelationtoexisting
Clustering performs best with the C2 replacement strategy. upliftmodelinganduserprofilingapproaches,withemphasis
Given that clustering can amplify both gains and volatility, onstability,interpretability,andoperationalrelevance.
it should be treated as a calibrated instrument, not as a The Causal User Profiling (CUP) framework moves
mandatorycomponentofeverycausaluser-profilingpipeline. beyond descriptive or purely predictive profiling by cen-
tering treatment responsiveness as its primary analytical
3) META-LEARNERANDBASE-LEARNERCONFIGURATIONS dimension.Thisreframingabstractsusermodellingfromthe
Atotalofsixteenmeta/basecombinations(fourmeta-learners question of who users are, to how users behave when acted
×fourbaselearners)wereexploredusingtheoptimalfeature on [6] and [22]. This move from correlation to causation
VOLUME14,2026 40163

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE7. Evaluationofclusteringstrategiesandmeta-learnerperformanceunderclustered
upliftmodeling.(a)Elbowcurvebasedonsilhouettescoresforselectingtheoptimalnumber
ofclusters.ThesilhouettescorestabilizesnearK=48,indicatingasuitabletrade-off
betweenclustercohesionandseparation.(b)Comparisonofclusteringstrategies(Direct,C1,
C2)usingmultipleAUUCindicators,includingbaselineAUUC,weightedAUUC,clusterAUUC,
andextremeclusterAUUCvalues.ResultsindicatetheperformancerankingC2>C1>
Direct,withC2achievingthehigheststabilityandlowestvariance.(c)Meta-learner
performancecomparisonunderclusteringacrossmonths.ResultsshowthattheXLearner
demonstratesthemostconsistentimprovement,whereasDR-,T-,andCF-Learnersexhibit
greaterfluctuationsorperformancedecline.
40164 VOLUME14,2026

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE7. (Continued).Evaluationofclusteringstrategiesandmeta-learnerperformanceunder
clusteredupliftmodeling.(a)Elbowcurvebasedonsilhouettescoresforselectingtheoptimalnumber
ofclusters.ThesilhouettescorestabilizesnearK=48,indicatingasuitabletrade-offbetweencluster
cohesionandseparation.(b)Comparisonofclusteringstrategies(Direct,C1,C2)usingmultipleAUUC
indicators,includingbaselineAUUC,weightedAUUC,clusterAUUC,andextremeclusterAUUCvalues.
ResultsindicatetheperformancerankingC2>C1>Direct,withC2achievingthehigheststabilityand
lowestvariance.(c)Meta-learnerperformancecomparisonunderclusteringacrossmonths.Results
showthattheXLearnerdemonstratesthemostconsistentimprovement,whereasDR-,T-,and
CF-Learnersexhibitgreaterfluctuationsorperformancedecline.
VOLUME14,2026 40165

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE8. HeatmapshowingthemeanAAUCvaluesforallMeta-Learner×Base-Learnerconfigurations.Darkercellsindicate
higherupliftperformance.TheDR-LearnercombinedwithLogisticRegression(LR)achievesthehighestmeanAAUCandlowest
variance,demonstratingthemostbalancedtrade-offbetweenaccuracy,stability,andinterpretability.
representsatransformationintheconceptualunderpinnings A second insight relates to methodological integration,
ofpersonalizationscience,towardaframeworkthatpredicts which contributes directly to the robustness of CUP. Rather
behaviour while also explaining why effects transpire. The than operating as isolated modules, feature selection, clus-
empirical findings confirm that causal interpretability is tering, and causal estimation work synergistically. The C2
distinctive in its potential to redefine user segmentation. replacement strategy compensates for unstable clusters by
Rootedinthepotentialoutcomesframework[11],lateraug- substitutingtheirpredictionswiththoseoftheglobalmodel,
mentedintothemetalevelframeworkofmeta-learning[15], producing a hierarchical regularization effect that maintains
CUPquantifiesheterogeneoustreatmenteffectsthroughthe localsensitivitywhileensuringglobalconsistency[4].Within
four-type response taxonomy of Persuadables, Sure Things, this structure, the Doubly Robust (DR) Learner combined
LostCauses,andDo-Not-Disturbs[17]. withLogisticRegression(LR)deliversafavourablebalance
This treatment-aware representation of user behaviour between robustness and interpretability. While alternative
indicates that the heterogeneity observed in behaviour is configurationssuchastheX-Learnermayperformwellunder
not an artefact of random variation but rather a marker certain imbalance conditions, the DR–LR configuration
of differential responsiveness to intervention. In the digital demonstrated greater temporal stability across repeated
lending case-study context, these distinctions illustrate how deployments,whichisessentialinoperationalenvironments.
interventions may activate engagement, reinforce inevitable From a practical perspective, CUP grounds causal rea-
outcomes,protectusersfromunnecessaryactions,orrespect soning in consequences experienced by decision-makers.
non-responsiveness. Compared with conventional uplift By estimating conditional treatment effects rather than
modeling pipelines that emphasize ranking accuracy predictive probabilities, the framework enables intervention
alone, CUP aligns estimation, evaluation, and response designbasedoncausalevidenceratherthanintuitionorcorre-
interpretationwithinaunifiedanalyticalframework,yielding lation.Empirically,thesequentialstackingofmethodological
morestablegainsunderrepeatedinterventions. components yields meaningful and interpretable gains in
| A first           | salient | insight | from    | the      | results | concerns the | performance:   |                    |     |      |             |
| ----------------- | ------- | ------- | ------- | -------- | ------- | ------------ | -------------- | ------------------ | --- | ---- | ----------- |
| interrelationship |         | between | feature | quality, | model   | stability,   |                |                    |     |      |             |
|                   |         |         |         |          |         |              | Hybrid feature | selection improves |     | AUUC | by approxi- |
•
| and causal | validity. | The | hybrid | feature | selection | strategy— |     |     |     |     |     |
| ---------- | --------- | --- | ------ | ------- | --------- | --------- | --- | --- | --- | --- | --- |
mately25–30%overthebaseline;
| combining | Information |     | Value | (IV), | Causal Forest | impor- |     |     |     |     |     |
| --------- | ----------- | --- | ----- | ----- | ------------- | ------ | --- | --- | --- | --- | --- |
• Clusteringcontributesanadditional10–12%throughthe
| tance, and | Stepwise | refinement—produced |     |     | the | most stable |     |     |     |     |     |
| ---------- | -------- | ------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- |
C2refinementstrategy;
upliftperformanceacrossmonthlysamples.Thisobservation
|          |              |     |      |                   |     |            | • The DR-Learner | + LR configuration |     | adds | a further |
| -------- | ------------ | --- | ---- | ----------------- | --- | ---------- | ---------------- | ------------------ | --- | ---- | --------- |
| confirms | the argument |     | that | causal estimation |     | depends as |                  |                    |     |      |           |
5–8%uplift.
| much on | data stability |     | and regime | design | as on | algorithmic |     |     |     |     |     |
| ------- | -------------- | --- | ---------- | ------ | ----- | ----------- | --- | --- | --- | --- | --- |
sophistication [6]. High-IV variables ensure that the model Cumulatively,thefull CUPpipelineachievesanapproxi-
mately45–50%improvementinmodelperformancerelative
learnsfrominformation-richdimensions;causalimportance
anchorsrelevancetotreatmenteffects;andStepwiseselection to conventional profiling approaches. More importantly,
serves as a form of variance regularization. Together, these thesegainspersistacrossmultipletimewindows,indicating
|            |       |            |     |         |              |          | systematic rather | than incidental | improvements. |     | From a |
| ---------- | ----- | ---------- | --- | ------- | ------------ | -------- | ----------------- | --------------- | ------------- | --- | ------ |
| components | yield | a ‘‘causal |     | feature | space’’ that | balances |                   |                 |               |     |        |
predictivestrengthwithgeneralizablestructuralcharacteris- computationalstandpoint,theruntimeofCUPisdominated
bybaselearnertrainingandclusteringstagesandintroduces
tics.Thisfindingreinforcesthenotionof‘‘datarefinement’’
[4], consistent with evidence in causal machine learning no additional asymptotic complexity beyond standard uplift
that emphasizes disciplined feature design over increasing modelingpipelines,makingittractableforlarge-scaletabular
datasets.
algorithmiccomplexity.
| 40166 |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
FIGURE9. CumulativegaincurvescomparingtheoptimizedCUPpathwaywiththebaseline;theCUP
curveuniformlydominates.
VI. LIMITATIONSOFTHESTUDY externalgeneralizability.FutureresearchshouldassessCUP
Despite its empirical strengths, this study has several across additional domains such as e-commerce, insurance,
limitations. First, the analysis is based on data from a andpublicfinancetoevaluatecross-contextrobustness.
singledigitallendingplatform.Whilethisenablescontrolled Second, the treatment variable aggregates heterogeneous
evaluation under realistic operational conditions, it limits interventions (e.g., coupons, credit-line increases, outbound
VOLUME14,2026 40167

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
calls), which may obscure intervention-specific behavioural outcomes,ensuringcausalinterpretabilitywhilemaintaining
mechanisms. Extending CUP to explicit multi-treatment or temporalstability.
dynamic intervention settings would enable finer-grained For each deployment period, uplift scores are first
analysisofintervention-specificcausaleffects. estimated using the selected meta-learner configuration.
Third, the evaluation emphasizes temporal consistency High-confidence uplift thresholds are applied to identify
acrosssixmonthlydeploymentsratherthanformalstatistical users with strong positive or negative estimated treatment
hypothesistesting.Thisdesignchoicereflectsanoperational effects. These uplift-based signals are then cross-validated
(T,Y)
focusonstabilityandreproducibilitybutmaylimitinference against observed realizations to refine response-type
insettingsthatrequireformalsignificancetesting. assignmentsandtopreventlogicallyinconsistentlabels.
Finally,issuesoffairness,transparency,andethicaldeploy- Specifically, Persuadables and Do-Not-Disturb users are
mentwarrantfurtherattention.Incorporatingfairness-aware identified through a combination of uplift magnitude and
learning and causal explainability into CUP represents an treatment-outcome alignment, while Sure Things and Lost
importantdirectionforfuturework,particularlyinsensitive Causes are distinguished based on behavioral invariance
financialapplications[1],[4]. withrespecttotreatmentexposure.Thistwo-stageprocedure
|     |     |     |     |     |     |     |     | mitigates | label noise | arising | from | estimation | uncertainty |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ------- | ---- | ---------- | ----------- | --- |
VII. CONCLUSIONANDFUTUREWORK and ensures that response categories remain behaviorally
| This study | contributes |     | to the | growing | literature | on  | causal | meaningful. |     |     |     |     |     |     |
| ---------- | ----------- | --- | ------ | ------- | ---------- | --- | ------ | ----------- | --- | --- | --- | --- | --- | --- |
analyticsbypositioningcausalityastheorganizingprinciple To promote consistency across time windows,
of user profiling. We propose Causal User Profiling (CUP), response-type definitions are held fixed, while individual
an integrated pipeline that combines feature selection, usersareallowedtotransitionbetweenresponsestatesastheir
clustering, and meta-learning into a reproducible and inter- behavior evolves. This design yields stable population-level
pretable workflow that connects causal estimation with semanticswhilepreservingindividual-leveldynamicsunder
| actionabledecision-making. |     |     |     |     |     |     |     | repeatedinterventions. |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
Empirically,CUPcapturesheterogeneoustreatmenteffects
| with temporal |     | stability; | conceptually, |     | it  | reframes | user |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | ------------- | --- | --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
APPENDIXB
| profiling | as the | causal | understanding |     | of  | behavioural |     |     |     |     |     |     |     |     |
| --------- | ------ | ------ | ------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
C2REPLACEMENTSTRATEGY
| response;                     | and practically, |       | it provides     |     | a scalable         | foundation    |           |                  |              |            |            |            |               |          |
| ----------------------------- | ---------------- | ----- | --------------- | --- | ------------------ | ------------- | --------- | ---------------- | ------------ | ---------- | ---------- | ---------- | ------------- | -------- |
|                               |                  |       |                 |     |                    |               |           | In the CUP       | framework,   | clustering | is         | treated    | as a          | flexible |
| for treatment-awarestrategies |                  |       | indiverse       |     | digitalecosystems. |               |           |                  |              |            |            |            |               |          |
|                               |                  |       |                 |     |                    |               |           | and corrective   | component    | rather     | than       | a hard     | segmentation  |          |
| Rather                        | than competing   |       | with predictive |     | machine            |               | learning, |                  |              |            |            |            |               |          |
|                               |                  |       |                 |     |                    |               |           | step. Clustering | is performed |            | at the     | individual | level,        | while    |
| CUP complements               |                  | it    | by explaining   |     | why                | interventions |           |                  |              |            |            |            |               |          |
|                               |                  |       |                 |     |                    |               |           | model evaluation | and          | stability  | assessment |            | are conducted |          |
| work and                      | for              | whom, | advancing       |     | personalization    |               | from      |                  |              |            |            |            |               |          |
acrossmonthlydeploymentwindowstoreflectsystem-level
outcomepredictiontowardcausalunderstandinganddecision
performanceunderrepeatedinterventions.
optimization.
|     |     |     |     |     |     |     |     | After          | initial clustering, | uplift   | performance |     | is evaluated    |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | -------- | ----------- | --- | --------------- | --- |
|     |     |     |     |     |     |     |     | at the cluster | level and           | compared | against     |     | a non-clustered |     |
ACKNOWLEDGMENT (Direct)baselineusingthesamemonthlyevaluationprotocol.
| This study | benefited | from | the | Haier | Group | Digital | Finance |               |            |       |      |         |          |     |
| ---------- | --------- | ---- | --- | ----- | ----- | ------- | ------- | ------------- | ---------- | ----- | ---- | ------- | -------- | --- |
|            |           |      |     |       |       |         |         | Cluster-based | prediction | paths | that | exhibit | unstable | or  |
InnovationInitiative(whichprovidedtheaccesstodataand
inferiorupliftperformancerelativetotheDirectglobalmodel
computerresourcesforempiricalvalidationofourproposed
arenotpropagatedtodownstreamresponse-typeassignment.
model),andtheauthorsareespeciallygratefultothemforthe
Thiscomparisongivesrisetothreeevaluationpaths:
implementationoftheCUP.
• Direct:upliftestimationwithoutclustering;
DATAAVAILABILITYSTATEMENT • C1:upliftestimationwithinclusters;
The dataset used in this study is subject to institutional C2: cluster-level evaluation followed by fallback to
•
andcommercialrestrictionsandthereforecannotbepublicly Directpredictionswhenclusteringdegradesstabilityor
released at this time. Aggregated statistics and derived performance.
experimentalresultsarereportedinthemanuscript.
|           |           |         |          |                   |                |     |          | Rather     | than enforcing | cluster-specific |          | predictions |                 | at the |
| --------- | --------- | ------- | -------- | ----------------- | -------------- | --- | -------- | ---------- | -------------- | ---------------- | -------- | ----------- | --------------- | ------ |
| The       | authors   | plan to | release  | a reproducibility |                |     | package, |            |                |                  |          |             |                 |        |
|           |           |         |          |                   |                |     |          | individual | level, the     | C2 strategy      | operates |             | as a path-level |        |
| including | synthetic | data    | examples | and               | representative |     | code     |            |                |                  |          |             |                 |        |
regularizationmechanism.Itpreservescluster-basedhetero-
| implementations, |     | subject | to data-sharing |     | approval |     | in future |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | --------------- | --- | -------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
geneitywhenbeneficial,whilerevertingtotheglobalmodel
work.
whenclusteringintroducesnoiseorinstability.
APPENDIXA
| RESPONSE-TYPELABELCONSTRUCTIONAND |     |     |     |     |     |     |     | APPENDIXC              |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
| CONSISTENCY                       |     |     |     |     |     |     |     | ABLATIONANALYSISDESIGN |     |     |     |     |     |     |
Response-type labels in CUP are constructed to reflect The purpose of the ablation analysis in this study is not to
both estimated treatment effects and observed behavioral conduct formal hypothesis testing, but to assess the relative
| 40168 |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
contributionandstabilityofindividualcomponentswithinthe selected data summaries or code components may be made
| CUPpipelineunderrepeatedreal-worlddeployments. |     |     |     |     |     |     |     | available. |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Each ablation experiment removes or modifies one com- From a computational perspective, the CUP framework
ponent of the framework while keeping all others fixed. is designed to remain tractable for large tabular datasets.
Performance differences are evaluated consistently across The dominant computational costs arise from repeated
six consecutive monthly datasets, allowing assessment of uplift model estimation, causal feature screening, and
whetherobservedeffectspersistovertimeratherthanarising clustering-based analyses across multiple monthly deploy-
fromasinglesnapshot. ments. While no additional asymptotic complexity is intro-
Given the operational nature of the study and the use ducedbeyondstandardupliftmodelingpipelines,thecumu-
of large-scale observational data, emphasis is placed on lativeexperimentalworkloadissubstantialduetothebreadth
temporal consistency and the magnitude of performance ofmodelconfigurationsandablationsettingsevaluated.
differencesratherthanformalstatisticalsignificancetesting. Inthisstudy,extensiveablationexperimentsandstability
Thisdesignprovidesempiricalevidenceonwhetherobserved checks were prioritized to assess robustness under repeated
gains are systematic and reproducible under repeated inter- deployment.Asaresult,certainalgorithmicchoices—suchas
ventionsettings. theselectionofclusteringmethodsandbaselearners—reflect
|     |     |     |     |     |     |     |     | a deliberate | trade-off     |     | between   | methodological |                | coverage |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | --------- | -------------- | -------------- | -------- |
|     |     |     |     |     |     |     |     | and feasible | computational |     | execution | under          | single-machine |          |
APPENDIXD
| FEATURESCREENINGANDSCALINGSTRATEGY |     |     |     |     |     |     |     | constraints. |     |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
Feature preprocessing in CUP is designed to enhance FutureworkwillextendtheCUPframeworktoincorporate
|     |     |     |     |     |     |     |     | additional | feature | selection | strategies, | uplift | estimators, | and |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | --------- | ----------- | ------ | ----------- | --- |
numericalcomparability,stability,andcausalrelevanceprior
to model estimation, rather than to optimize predictive clustering algorithms as computational resources permit.
accuracythroughaggressivenormalizationortransformation. Theseextensionsareexpectedtofurtherenrichcomparative
Before model fitting, all candidate covariates undergo analysiswithoutalteringthecoremethodologicalprinciples
a unified screening process to ensure consistency across establishedinthepresentstudy.
downstreamfeatureconfigurations.Continuousvariablesare
rescaledtoacommonnumericalrangetoimprovecompara-
REFERENCES
bilityacrossfeatureswithheterogeneousmagnitudesandto
|     |     |     |     |     |     |     |     | [1] E. Rich, | ‘‘User | modeling | via stereotypes,’’ | Cognit. | Sci., | vol. 3, no. 4, |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | -------- | ------------------ | ------- | ----- | -------------- |
facilitatestableoptimizationinsubsequentmodelingstages. pp.329–354,1979.
Thisrescalingisapplieduniformlyanddoesnotaltertherel-
|     |     |     |     |     |     |     |     | [2] G. Adomavicius |     | and A.   | Tuzhilin, | ‘‘Toward                | the next | generation of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | -------- | --------- | ----------------------- | -------- | ------------- |
|     |     |     |     |     |     |     |     | recommender        |     | systems: | A survey  | of the state-of-the-art |          | and possible  |
ativeorderingordistributionalshapeofindividualfeatures.
extensions,’’IEEETrans.Knowl.DataEng.,vol.17,no.6,pp.734–749,
Featureselectionproceedsthroughadiagnosticmulti-stage
Jun.2005,doi:10.1109/TKDE.2005.99.
| procedure | that | combines |     | complementary |     | criteria: |     |                                                                   |     |     |     |     |     |     |
| --------- | ---- | -------- | --- | ------------- | --- | --------- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|           |      |          |     |               |     |           |     | [3] P.BrusilovskyandE.Millán,‘‘Usermodelsforadaptivehypermediaand |     |     |     |     |     |     |
(i)information-basedscreeningtoretainvariableswithsuffi- adaptiveeducationalsystems,’’inTheAdaptiveWeb.Cham,Switzerland:
cient outcome relevance, (ii) causal importance assessment Springer,2007,pp.3–53.
|     |     |     |     |     |     |     |     | [4] C.I.Eke,A.A.Norman,andW.Ozuem,‘‘Userprofilinginpersonalized |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
to identify features consistently associated with treatment recommender systems: A systematic review,’’ IEEE Access, vol. 7,
effects across time windows, and (iii) stepwise refinement pp.146923–146940,2019,doi:10.1109/ACCESS.2018.2887321.
tocontrolredundancyandvarianceinflation. [5] D.Mirylenka,F.Ricci,andL.Rokach,‘‘Usermodelingandpersonaliza-
tion,’’inRecommenderSystemsHandbook.NewYork,NY,USA:Springer,
| Importantly, |     | this screening |     | stage is | performed | prior | to  |     |     |     |     |     |     |     |
| ------------ | --- | -------------- | --- | -------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
2019,doi:10.1145/3357384.3357818.
| constructing       | downstream |               | feature-set |           | configurations |          | (e.g., |                                                                      |       |            |           |           |         |               |
| ------------------ | ---------- | ------------- | ----------- | --------- | -------------- | -------- | ------ | -------------------------------------------------------------------- | ----- | ---------- | --------- | --------- | ------- | ------------- |
|                    |            |               |             |           |                |          |        | [6] S.AtheyandG.Imbens,‘‘Recursivepartitioningforheterogeneouscausal |       |            |           |           |         |               |
| information-based, |            | causal-based, |             | or hybrid | sets),         | ensuring |        |                                                                      |       |            |           |           |         |               |
|                    |            |               |             |           |                |          |        | effects,’’                                                           | Proc. | Nat. Acad. | Sci. USA, | vol. 113, | no. 27, | pp.7353–7360, |
that all reported models draw from a common pool of Jul.2016,doi:10.1073/pnas.1510489113.
filtered and stability-checked covariates. This design avoids [7] F. Purificato, A. Rago, A. Belkhir, P. Lanzini, and P. Cirillo, ‘‘Deep
causalmodels:Asurvey,’’Inf.Process.&Manag.,vol.61,no.3,2024,
feature-induced confounding when comparing alternative Art.no.103579,doi:10.1016/j.ipm.2023.103579.
model specifications and promotes reproducibility under [8] W.Wu,F.Yuan,J.Huang,X.Yu,andM.Zhang,‘‘Social-network-based
repeateddeployment. userprofiling:Asurvey,’’Inf.Sci.,vol.648,Oct.2024,Art.no.119021,
doi:10.1016/j.ins.2024.119021.
|     |     |     |     |     |     |     |     | [9] J.Pearl,Causality:Models,Reasoning,andInference,2nded.,Cambridge, |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
APPENDIXE
U.K.:CambridgeUniv.Press,2009,doi:10.1017/CBO9780511803478.
COMPUTATIONALCONSIDERATIONS [10] M.A.HernánandJ.M.Robins,CausalInference:WhatIf.London,U.K.:
Theempiricalstudywasconductedusinglarge-scaleobser- Chapman&Hall,2020,doi:10.1201/9780429259654.
vationaldatafromareal-worlddigitallendingplatform.Due [11] D.B.Rubin,‘‘Estimatingcausaleffectsoftreatmentsinrandomizedand
nonrandomizedstudies,’’J.Educ.Psychol.,vol.66,no.5,pp.688–701,
totheinvolvementofsensitivecustomer-levelfinancialinfor-
Oct.1974,doi:10.1037/h0037350.
| mation, | the underlying |     | dataset | cannot | be publicly | released |     |                                                                     |     |     |     |     |     |     |
| ------- | -------------- | --- | ------- | ------ | ----------- | -------- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|         |                |     |         |        |             |          |     | [12] G.W.ImbensandD.B.Rubin,CausalInferenceforStatistics,Social,and |     |     |     |     |     |     |
at this stage. Data access was granted under institutional BiomedicalSciences.Cambridge,U.K.:CambridgeUniv.Press,2015,doi:
10.1017/CBO9781139025751.
collaborationandconfidentialityagreements,andresultsare
|          |               |     |     |            |       |         |     | [13] S. Wager | and     | S. Athey, | ‘‘Estimation | and inference          |     | of heterogeneous |
| -------- | ------------- | --- | --- | ---------- | ----- | ------- | --- | ------------- | ------- | --------- | ------------ | ---------------------- | --- | ---------------- |
| reported | in aggregated |     | and | anonymized | form. | Subject | to  |               |         |           |              |                        |     |                  |
|          |               |     |     |            |       |         |     | treatment     | effects | using     | random       | forests,’’ Biometrika, |     | vol. 105, no. 2, |
future approval and appropriate de-identification protocols, pp.287–301,2018,doi:10.1093/biomet/asx045.
| VOLUME14,2026 |     |     |     |     |     |     |     |     |     |     |     |     |     | 40169 |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
[14] X. Nie and S. Wager, ‘‘Quasi-oracle estimation of heterogeneous [40] N. Hu, ‘‘Heterogeneous treatment effects analysis for social scientists:
treatmenteffects,’’Ann.Statist.,vol.49,no.6,pp.3935–3963,3935,doi: A review,’’ Social Sci. Res., vol. 109, Jan. 2023, Art.no.102810, doi:
| 10.1214/20-AOS1964. |     |     |     |     |     |     |     | 10.1016/j.ssresearch.2022.102810. |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
[15] S.R.Künzel,J.S.Sekhon,P.J.Bickel,andB.Yu,‘‘Metalearnersfor [41] Z.Zhang,P.Zhao,X.Li,andY.Liu,‘‘Causalrepresentationlearning,’’in
estimatingheterogeneoustreatmenteffectsusingmachinelearning,’’Proc. Proc.KDD,2021,pp.2663–2673,doi:10.1145/3447548.3467381.
Nat.Acad.Sci.USA,vol.116,no.10,pp.4156–4165,Mar.2019,doi: [42] A.M.AlaaandM.V.D.Schaar,‘‘Limitsofestimatingheterogeneous
10.1073/pnas.1804597116. treatmenteffects:Guidelinesforpracticalalgorithmdesign,’’IEEETrans.
[16] S. Athey, J. Tibshirani, and S. Wager, ‘‘Generalized random forests,’’ NeuralNetw.Learn.Syst.,pp.129–138,Jan.2018.
Ann.Statist.,vol.47,no.2,pp.1148–1178,Jan.2019,doi:10.1214/18- [43] X. Guo, K. Yu, L. Liu, F. Cao, and J. Li, ‘‘Causal representation
AOS1709. learning:Asurvey,’’Artif.Intell.,vol.320,Nov.2024,Art.no.104072,
[17] N.J.RadcliffeandP.D.Surry,‘‘Upliftmodellingwithsignificance-based doi:10.1016/j.artint.2024.104072.
trees,’’StochasticSolutions,London,U.K.,Tech.Rep.,2011. [44] Z. Zhang, P. Zhao, X. Li, and Y. Liu, ‘‘Deep causal models for ITE
[18] P.RzepakowskiandS.Jaroszewicz,‘‘Decisiontreesforupliftmodeling estimation:Asurvey,’’ACMComput.Surv.,vol.55,no.12,pp.1–38,2023,
with single and multiple treatments,’’ Knowl. Inf. Syst., vol. 32, no. 2, doi:10.1145/3527154.
pp.303–327,Aug.2012,doi:10.1007/s10115-011-0434-0.
[19] P.GutierrezandJ.Y.Gérardy,‘‘Causalinferenceandupliftmodelling:A
reviewoftheliterature,’’Inf.Sci.,vol.420,pp.590–598,Jun.2017,doi:
10.1016/j.ins.2017.02.002.
| [20] N. J. | Radcliffe, | ‘‘Using | control | groups | to target on | predicted | lift,’’ |     |     |     |     |     |     |     |
| ---------- | ---------- | ------- | ------- | ------ | ------------ | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
StochasticSolutions,London,U.K.,Tech.Rep.,2007.
| [21] M. Jaskowski |     | and S. | Jaroszewicz, | ‘‘Uplift   | modeling | for       | clinical |     |     |     |     |     |     |     |
| ----------------- | --- | ------ | ------------ | ---------- | -------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| trial data,’’     | in  | Proc.  | ICDM         | Workshops, | 2012,    | pp.17–23, | doi:     |     |     |     |     |     |     |     |
10.1109/ICDMW.2012.103. JIANQING JIANG is currently pursuing the
[22] F. Devriendt, D. Moldovan, and W. Verbeke, ‘‘A literature survey and Ph.D.degreewiththeInstituteforMathematical
experimental evaluation of the state-of-the-art in uplift modeling: A Research (INSPEM), Universiti Putra Malaysia.
| stepping | stone | toward the | development | of  | prescriptive | analytics,’’ | Big |     |     |              |      |                     |     |              |
| -------- | ----- | ---------- | ----------- | --- | ------------ | ------------ | --- | --- | --- | ------------ | ---- | ------------------- | --- | ------------ |
|          |       |            |             |     |              |              |     |     |     | His research | lies | at the intersection |     | of user pro- |
Data,vol.6,no.1,pp.13–41,Mar.2018,doi:10.1089/big.2017.0104.
|     |     |     |     |     |     |     |     |     |     | filing, | causal machine | learning, | uplift | modeling, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------------- | --------- | ------ | --------- |
[23] Z.Zhang,P.Zhao,X.Li,andY.Liu,‘‘Deepcausalmodels:Taxonomyand
|     |     |     |     |     |     |     |     |     |     | and heterogeneous |     | treatment | effect | estimation, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --------- | ------ | ----------- |
roadmap,’’ACMComput.Surveys,vol.56,no.3,pp.1–36,2024.
withaparticularfocusondynamicuserprofiling
[24] J.Chen,Y.Wang,andX.Li,‘‘Asurveyofuserprofiling:State-of-the-
art,challengesandsolutions,’’Inf.Process.Manage.,vol.61,no.2,2024, and personalized intervention design. He has
Art.no.103676,doi:10.1016/j.ipm.2023.103676. more thanseven years ofindustry experience in
[25] F. Devriendt, D. Moldovan, and W. Verbeke, ‘‘Prescriptive analytics data science and business intelligence, holding
through uplift modeling: A review,’’ Inf. Fusion, vol. 73, pp.67–86, professional roles in China and Singapore in credit analytics, customer
modeling,andenterprisedatasystems.PriortohisPh.D.studies,hewas
Sep.2021,doi:10.1016/j.inffus.2021.02.003.
[26] U.Shalit,F.D.Johansson,andD.Sontag,‘‘Estimatingindividualtreatment a Senior Data Scientist developing credit scoring models, customer
effect:Generalizationboundsandalgorithms,’’inProc.34thInt.Conf. segmentationframeworks,andlarge-scaledatagovernanceplatforms.His
Mach.Learn.,2017,pp.3076–3085. current research integrates causal inference with behavioral modeling
[27] C.Shi,D.M.Blei,andV.Veitch,‘‘Adaptingneuralnetworksforcausal to improve decision-making in internet lending and other high-stakes
| inference,’’2019,arXiv:1905.12776. |            |     |        |             |           |            |     | operationalenvironments. |     |     |     |     |     |     |
| ---------------------------------- | ---------- | --- | ------ | ----------- | --------- | ---------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
| [28] J. Yoon,                      | J. Jordon, | and | M. Van | Der Schaar, | ‘‘GANITE: | Estimating |     |                          |     |     |     |     |     |     |
individualizedtreatmenteffects,’’2018,arXiv.1806.04968.
[29] D.Olaya,H.Ponce,M.A.Gutiérrez-Andrade,andO.Martínez-Velázquez,
‘‘Multi-treatmentupliftmodeling,’’inProc.KDD,2020,p.106533,doi:
10.1145/3394486.3403196.
| [30] K. Lee | and       | J. Berger, | ‘‘Cross-treatment |           | gain surface         | and | multi- |     |     |     |     |     |     |     |
| ----------- | --------- | ---------- | ----------------- | --------- | -------------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| treatment   | uplift,’’ | Inf. Sci., | vol.              | 694, Jan. | 2024, Art.no.119240, |     | doi:   |     |     |     |     |     |     |     |
10.1016/j.ins.2024.119240.
[31] J.L.Hill,‘‘Bayesiannonparametricmodelingforcausalinference,’’Stat.
Sci.,vol.26,no.1,pp.1–27,2011,doi:10.1214/11-STS367.
| [32] P. R. Hahn, | J.  | S. Murray, | and C.     | M. Carvalho,    | ‘‘Bayesian |              | regression |     |     |     |     |     |     |     |
| ---------------- | --- | ---------- | ---------- | --------------- | ---------- | ------------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| tree models      | for | causal     | inference: | Regularization, |            | confounding, | and        |     |     |     |     |     |     |     |
heterogeneouseffects(withdiscussion),’’BayesianAnal.,vol.15,no.3, NOR ASILAH WATI ABDUL HAMID (Senior
pp.965–1056,Sep.2020,doi:10.1214/19-ba1195. Member,IEEE)receivedthePh.D.degreeincom-
|     |     |     |     |     |     |     |     |     |     | puter science | from | The University |     | of Adelaide, |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | -------------- | --- | ------------ |
[33] M.Dudik,J.Langford,andL.Li,‘‘Doublyrobustpolicyevaluationand
| learning,’’2011,arXiv:1103.4601. |     |     |     |     |     |     |     |     |     | Australia,in2008. |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
[34] J. Rehill, ‘‘A gentle introduction to uplift modelling,’’ 2024, From2013to2015,shewasaVisitingScholar
arXiv.2403.03822. with the High Performance Computing Labora-
[35] T. Inoue, K. Yamamoto, and T. Okuno, ‘‘Machine-learning-based het- tory, The George Washington University, USA.
erogeneoustreatmenteffectestimationinrandomizedtrials:APRISMA In 2015, she was awarded the CUDA Teaching
review,’’Trials,vol.25,no.134,pp.1–21,2024,doi:10.1186/s13063-
CentrerecognitionbyNVIDIAandsubsequently
024-07943-0.
establishedtheCUDALaboratoryatherfaculty.
[36] C.Ling,D.Sutherland,F.Johansson,andJ.Wiens,‘‘Causalinference
|     |     |     |     |     |     |     |     | She is currently | the | Deputy Director | of  | the Institute | for | Mathematical |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------- | --- | ------------- | --- | ------------ |
pipelinesforRCTemulation,’’2023,arXiv.2302.03070.
|     |     |     |     |     |     |     |     | Research | (INSPEM), | Universiti | Putra Malaysia. | She | is also | an Associate |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---------- | --------------- | --- | ------- | ------------ |
[37] A.Maraj,M.Vuković,andD.Hotovec,‘‘Asystematicreviewofuplift
modeling,’’Inf.Process.Manag.,vol.61,no.2,2024,Art.no.103692, ProfessorwiththeDepartmentofCommunicationTechnologyandNetwork,
FacultyofComputerScienceandInformationTechnology.Shehasauthored
doi:10.1016/j.ipm.2023.103692.
|            |           |     |       |        |               |      |        | or co-authored | more | than 80 journal | articles | and | conference | papers. Her |
| ---------- | --------- | --- | ----- | ------ | ------------- | ---- | ------ | -------------- | ---- | --------------- | -------- | --- | ---------- | ----------- |
| [38] P. R. | Rosenbaum | and | D. B. | Rubin, | ‘‘The central | role | of the |                |      |                 |          |     |            |             |
researchhasbeensupportedbybothgovernmentandindustryfunding,with
| propensity | score,’’ | Biometrika, |     | vol. 70, | no. 1, pp.41–55, | 1983, | doi: |     |     |     |     |     |     |     |
| ---------- | -------- | ----------- | --- | -------- | ---------------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
interestsfocusedonparallelanddistributedhigh-performancecomputing,
10.1093/biomet/70.1.41.
[39] A.Caron,G.Baio,andI.Manolopoulou,‘‘Estimatingindividualtreatment cloudcomputing,anddata-intensivecomputing.
effectsusingnon-parametricregressionmodels:Areview,’’J.Roy.Stat. Dr. Abdul Hamid is the Editor-in-Chief of Malaysian Journal of
Soc.Ser.A,Statist.Soc.,vol.185,no.3,pp.1115–1149,Jul.2022,doi: MathematicalSciencesandservesasareviewerforseveralwell-regarded
10.1111/rssa.12824. journalsandinternationalconferenceproceedings.
| 40170 |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME14,2026 |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |

J.Jiangetal.:DynamicFrameworkforCUPandTreatmentSegmentationviaUpliftModeling
NGKENGYAP(SeniorMember,IEEE)received CHOO WEI CHONG received the bachelor’s
theB.Sc.andM.Sc.degreesincomputerscience degreeinscience(statistics)andtheMaster’sof
fromUniversitiPutraMalaysia,in2001and2005, SciencedegreeinbusinessstatisticsfromUniver-
respectively, and the Ph.D. degree in computer sitiPutraMalaysia(UPM),andthePh.D.andPost-
sciencefromTheUniversityofManchester,U.K., doctoraldegreesinmanagementstudies/decision
in 2015. He is currently a Senior Lecturer with sciencefromtheUniversityofOxford,U.K.Heis
theFacultyofComputerScienceandInformation currentlyanAssociateProfessorwiththeSchool
Technology, Universiti Putra Malaysia. He has of Business and Economics, UPM. His research
authoredarticlesinIEEEACCESSandotherindexed focuses on volatility modeling, high-frequency
journals.Hehasbeeninvolvedinmultipleresearch financial data, machine learning–econometrics
projects, including studies on palm oil production analytics, traffic flow hybridforecasting,text-basedanalytics,andAIapplicationsinhealthcare
analysis, and disruptive technology in construction project management. andtourism.
Hisresearchinterestsincludesoftwarecomponents,businessanalytics,and
softwareengineeringforartificialintelligence(SE4AI)systems.
VOLUME14,2026 40171