---
conversion_metadata:
  converted_at: "2026-07-21T05:23:32Z"
  converter_tool: "markitdown"
  converter_version: "0.1.6"
  source_pdf: "Andersson.pdf"
  source_pdf_sha256: "af30729c214dba337fa876da5ec820e08014d426d01c1d4c95e6caf4610520be"
  page_count: 11
  markdown_char_count: 62030
---

Insights into the temporal dynamics of
identifying problem gambling on an online
casino: A machine learning study on routinely
collected individual account data
Journal of Behavioral SAM ANDERSSON1p , PER CARLBRING2,3 ,
Addictions KEENAN LYON4 , MÅNS BERMELL4 and PHILIP LINDNER1
14 (2025) 1, 490–500
1CentreforPsychiatry Research,DepartmentofClinicalNeuroscience, KarolinskaInstitutet, &
DOI:
Stockholm HealthCareServices, RegionStockholm,Stockholm,Sweden
10.1556/2006.2025.00013
©2025TheAuthor(s) 2DepartmentofPsychology,Stockholm University,Stockholm,Sweden
3SchoolofPsychology,Korea University,Seoul,SouthKorea
4LeoVegasGroup, Stockholm,Sweden
Received:October7,2024 (cid:129) Revisedmanuscriptreceived:January29,2025 (cid:129) Accepted:February1,2025
Publishedonline:February27,2025
FULL-LENGTH REPORT
ABSTRACT
Background and Aims: The digitalization of gambling provides unprecedented opportunities for early
identificationofproblemgambling,awell-recognizedpublichealthissue.Thisstudyaimedtoadvance
current practices by employing advanced machine learning techniques to predict problem gambling
behaviorsandassessthetemporalstabilityofthesepredictions.Methods:Weanalyzedplayeraccount
datafromamajorSwedishonlinegamblingprovider,coveringa4.5-yearperiod.Featureengineering
wasappliedtocapturegamblingbehaviordynamics.Wetrainedmachinelearningmodels,XGBoost,to
classify players into low-risk and higher-risk categories. Temporal stability was evaluated by progres-
sivelytruncatingthetrainingdatasetatvarioustimepoints(30,60,and90days)andassessingmodel
performance across truncations. Results: The models demonstrated considerable predictive accuracy
and temporal stability. Key features such as loss-chasing behavior and net balance trend consistently
contributedtoaccuratepredictionsacrossalltruncationperiods.Themodel’sperformanceevaluatedon
a separate holdout set, measured by metrics like F1 score and ROC AUC, remained robust, with no
significant decline observed even with reduced data, supporting the feasibility of early and reliable
detection. Discussion and Conclusions: These findings indicate that machine learning can reliably
predict problem gambling behaviors over time, offering a scalable alternative to traditional methods.
Temporal stability highlights their potential for real-time application in gambling operators’ Duty of
Care. Consequently, advanced techniques could strengthen early identification and intervention stra-
tegies,potentiallyimprovingpublichealthoutcomesbypreventingtheescalationofharmfulbehaviors.
KEYWORDS
problem gambling, machinelearning,temporalstability,predictive analytics,gamblingbehavior, publichealth
INTRODUCTION
Due to the high societal and individual costs associated with problem gambling, early identi-
fication is crucial (Eadington, 2003; Hofmarcher, Romild, Spångberg, Persson, & Håkansson,
pCorrespondingauthor.
2020; Jonsson, Abbott, Sjöberg, & Carlbring, 2017). The digitalization of gambling (Jonsson,
E-mail:sam.andersson@ki.se
Munck, Volberg, & Carlbring, 2017) offers unprecedented opportunities to do so, since every
login, deposit, bet, and outcome is logged. Once identified, timely interventions can signifi-
cantly increase the likelihood that individuals are helped before gambling-related harm
accumulates (Clune et al., 2024). Existing methods for identifying problem gambling, such as
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

| Journal | of Behavioral |     | Addictions | 14 (2025) |     | 1, 490–500 |     |     |     |     |     |     | 491 |
| ------- | ------------- | --- | ---------- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
self-report questionnaires and behavioral tracking, have The Swedish Gambling Act, mandates counteracting
varyingdegreesofvalidityandreliability(Edgrenetal.,2016; excessive gambling through continuous monitoring of
Jonsson,Munck,etal.,2017).Self-reportmethodsdependon gamblingbehavior(Swedish GamblingAct,2018).Whether
individuals accurately reporting their behaviors and experi- the Duty of Care should extend to predictive analytics that
ences. However, these methods can be susceptible to under- foresee problematic patterns before they fully develop re-
reporting and bias (Goldstein et al., 2017; Sato & Kawahara, mainstobethoroughlyexaminedandempiricallyvalidated.
2011),whereasbehavioraltrackingrequiressophisticateddata This study aims to enhance understanding of the temporal
analytics to interpret effectively (Bitar et al., 2017; Catania & dynamics in identifying problem gambling by applying
Griffiths, 2021; Haeusler, 2016; Kuentzel, Henderson, & advanced machine learning methods focused on predicting
Melville, 2008). Thus, the multifaceted nature of gambling, manualassessmentsandevaluatingthetemporalstabilityof
which involves various psychological, social, and situational these predictions through truncating the training set at
factors, makes it challenging to assess with a singular varioustimepoints.Ourapproachleveragesaggregateddata
approach (Browne et al.,2017; Hahmann, Hamilton-Wright, to capture broader behavioral indicators, ensuring compre-
Ziegler, & Matheson, 2021). For example, individuals may hensive analysis and improved prediction accuracy. By
stopgamblingfordiversereasons,includingnotonlyharmor transitioning from monitoring to proactive prediction, our
financial loss but also personal or strategic considerations research enables gambling operators to implement timely
(Weatherly, Montes, Peters, & Wilson, 2012). interventionstopreventtheescalationofproblemgambling
Much of the existing literature on identification focuses behaviors. Such advancements align with legislative frame-
on cross-sectional data (Gainsbury, Sadeque, Mizerski, & works and could significantly improve public health out-
Blaszczynski, 2013), which provides only a snapshot of comes by reducing gambling-related harms through early
| gambling | behavior     | at       | a single | point       | in time | and fails | to     | prediction. |     |     |     |     |     |
| -------- | ------------ | -------- | -------- | ----------- | ------- | --------- | ------ | ----------- | --- | --- | --- | --- | --- |
| capture  | the temporal |          | dynamics | by design.  | While   |           | under- |             |     |     |     |     |     |
| standing | the          | temporal | patterns | of gambling |         | behavior  | is     |             |     |     |     |     |     |
METHODS
| crucial,  | as it allows | for        | a more    | accurate        | identification |             | of  |              |     |     |     |     |     |
| --------- | ------------ | ---------- | --------- | --------------- | -------------- | ----------- | --- | ------------ | --- | --- | --- | --- | --- |
| problem   | gambling     | at         | different | timepoints      |                | (Braverman, |     |              |     |     |     |     |     |
| LaPlante, | Nelson,      | & Shaffer, |           | 2013; Braverman |                | & Shaffer,  |     | Participants |     |     |     |     |     |
2012;Deng,Lesch,&Clark,2019),itisequallyimportantto
WeutilizedplayeraccountdatafromoneofSweden’slargest
| consider | aggregated   | behavioral |      | data that          | captures | broader  |     |                 |                     |     |          |           |      |
| -------- | ------------ | ---------- | ---- | ------------------ | -------- | -------- | --- | --------------- | ------------------- | --- | -------- | --------- | ---- |
|          |              |            |      |                    |          |          |     | licensed online | gambling providers, |     | covering | 4.5 years | from |
| trends   | and patterns |            | over | time. Longitudinal |          | studies, |     |                 |                     |     |          |           |      |
although more complex, offer the potential for deeper in- January 1, 2019 (at which point Sweden switched to a
|     |     |     |     |     |     |     |     | licensed gambling | market), | to July | 1, 2023. | The | dataset |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | -------- | ------- | -------- | --- | ------- |
sightsintotheevolutionofgamblingbehaviorandtheonset
|            |          |          |     |         |       |           |     | included extensive | behavioral | and | transactional | details | for |
| ---------- | -------- | -------- | --- | ------- | ----- | --------- | --- | ------------------ | ---------- | --- | ------------- | ------- | --- |
| of problem | gambling | (Dowling |     | et al., | 2017) | and could | in  |                    |            |     |               |         |     |
5
theoryextendthepredictionwindow,allowingidentification n 35,048 unique, authenticated players, all of whom are
|             |           |             |           |         |             |           |       | based in Sweden,   | allowing | for a comprehensive |          | analysis | of  |
| ----------- | --------- | ----------- | --------- | ------- | ----------- | --------- | ----- | ------------------ | -------- | ------------------- | -------- | -------- | --- |
| of not just | current   | problem     | gamblers, |         | but also    | future    | ones. |                    |          |                     |          |          |     |
|             |           |             |           |         |             |           |       | gambling behaviors | within   | this specific       | context. |          |     |
| With        | access    | to player   | account   | data,   | predictive  | analytics |       |                    |          |                     |          |          |     |
| can develop | scalable, | data-driven |           | methods | to identify |           | prob- |                    |          |                     |          |          |     |
Measures
| lem gamblers |     | (Auer & | Griffiths, | 2022; | Perrot | et al., | 2022). |     |     |     |     |     |     |
| ------------ | --- | ------- | ---------- | ----- | ------ | ------- | ------ | --- | --- | --- | --- | --- | --- |
Various machine learning models have shown promise in Data preprocessing and feature engineering. All data pre-
identifying problem gamblers (Kairouz et al., 2023; Murch processing and analyses were conducted using Python
et al., 2023; Perrot et al., 2022), revealing that they can (3.11);thefullyreproduciblecodeisavailableonline(https://
leveragecomplexdatasetsandscientificallyinformedfeature
github.com/SamAndersson-C/temporal-dynamics-problem-
engineeringtoidentifypatternsofgamblingbehaviorrelated gambling). We performed extensive feature engineering on
to problem gambling. However, while these studies demon- raw data consisting of 11 data frames, which included in-
significant
strate potential, they also have limitations. For formation on bets, transactions, sessions, demographics,
instance, many existing models often rely on self-reported payments, responsible gambling actions and predictions,
data, which can be prone to biases and inaccuracies (Percy, manual risk assessments, and multiple accounts. Using
França, Dragi(cid:1)cević, & d’Avila Garcez, 2016). Moreover, in SQL scripts, we combined the data shards into raw tables
many predictive studies, researchers often not only utilize within a PostgreSQL database. As in past research (Hopf-
Griffiths,
cross-sectional data but also frame the prediction problem gartner, Auer, & Helic, 2022, 2024) features were
itself as a cross-sectional analysis, rather than leveraging derived to reflect various aspects of online gambling
longitudinal or retrospective data windows (Paterson, Tay- behavior, such as loss chasing, betting frequency, session
lor,&Gray,2020).Thisapproach,particularlyinhowdatais lengths, and spending patterns. Accurate alignment of all
aggregated and features are engineered, often overlooks the tables was crucial due to the granularity of the timestamps,
temporal richness inherent in the raw data (Suzuki, Naka- ensuringmeaningfulfeatureengineering(Wangetal.,2009)
mura, Inagaki, Watanabe, & Takagi, 2019), potentially and to capture the evolution of gambling behaviors and
significant
skewingtheresultstowardsrecentdatapointswhilemissing detect changes or trends, we ensured temporal
out on longer-term trends and broader progressions over alignment of data tables and took specific care to avoid
time (Park, Eom, Seo, & Choi, 2020). data leakage (using information from outside the training
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

492 Journal of Behavioral Addictions 14 (2025) 1, 490–500
set in model training). We enhanced performance through Nascimento, Guedes, & Monsueto, 2023). We employed a
indexing, partitioning, and query optimization. By precisely data truncation strategy based on timestamps from the
aligning and securely managing the data, we prevented gambling operator’s raw data to further assess temporal
inadvertent leakage that could produce overly optimistic stability. Using June 1, 2022, as a general reference, we
results.Allfeatureaggregationsstrictlyusedactivitydataup truncatedeachplayer’sdatabyremovingrecords30,60,and
to each labeling date (Fig. 1). 90 days prior to their maximum timestamp in the training
Nominal variables were numerically coded to facilitate set. This resulted in three distinct datasets: 30-day, 60-day,
modeling.Featureswithmorethan50%missingvalueswere and 90-day truncated data, each undergoing the same
excluded, while others underwent median imputation to feature engineering for model training and evaluation. This
preserve data integrity. Heavily skewed features with an allowed us to analyze how model performance varies with
excessofzerovalueswerelog-transformedtoachieveamore different amounts of historical data, providing insights into
normalized distribution. To evaluate the temporal stability the temporal stability of the predictions over varying time
of our predictions, we implemented a temporal division for horizons.
training and test sets, reserving the final year’s data for
testing. This ensured the model was evaluated on unseen Labeling. The primary label indicating customer risk was
data, simulating a real-world deployment scenario (Barros, derived from manual assessments conducted by the
Fig.1.Datapre-processing andanalysis pipeline
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

Journal of Behavioral Addictions 14 (2025) 1, 490–500 493
gambling provider as part of their Responsible Gambling SHAP(SHapleyAdditiveexPlanations)(Lundberg,Allen,&
operationsaspertheirDutyofCarecommitment(Cisneros Lee, n.d.; Ukhov, Bjurgert, Auer, & Griffiths, 2021) value
Örnberg & Hettne, 2018). These assessments targeted plotsbasedonourpreliminarymodels.Fromtheseplots,we
players exhibiting concerning gambling behaviors, classi- selectedthetop25mostinfluentialvariablesandusedthem
fying them into five risk levels based on deposit patterns, in a hierarchical clustering analysis with the complete link-
session length, denied transactions, and responsible age method, known for its robustness to noise and outliers
gamblingtooluse.Higher-riskcasesinvolvedpersistenthigh (Laurikkala & Juhola, 2001). Euclidean distance was used;
deposits, prolonged play, or self-reported loss of control. single linkagewas also consideredbut found unsuitable due
Additionally, certain customers were flagged for manual to data noise. This analysis revealed that the data naturally
review by the support team if communication raised con- clustered into two groups: low-risk and higher-risk. This
cerns. Since assessments focused on flagged individuals supported our decision to binarize the labels into low risk
rather than a random sample, the study population pri- andallotherrisklevels.Thisbinaryframeworkallowedusto
marily reflects at-risk players rather than all gamblers, focus on distinguishing low-risk customers from those at
congruent with the aim of prediction algorithms in this elevated risk, aligning with responsible gambling objectives.
context.Adatabaseloggingerrorwasdiscoveredduringthe
analysis, revealing that most of the manually assessed labels
Procedure
were concentrated at the beginning of the dataset’s time
frame, with some customers (n 5 5,848) being flagged with Feature selection. After initial feature engineering in SQL,
“unknown risk” as their label. These were accounts that the we conducted feature selection using SHAP values (Lund-
operator’s RG analysts began to review but could not com- berg et al., n.d.; Ukhov et al., 2021) and Generalized Matrix
plete due to unsuccessful attempts to contact the individual Learning Vector Quantization (GMLVQ) (Lövdal & Biehl,
inquestion,resultinginthesuspensionofthereview.These 2024) to identify the most relevant features for the binary
accounts were temporarily restricted from gambling until classification task. SHAP values decompose a model’s pre-
the company could establish contact with the individuals, diction for an individual instance into contributions from
allowingthemtocompletethereviewprocessinaccordance each feature, providing local and consistent explanations.
with the Responsible Gambling (RG) procedures. These They ensure that the sum of SHAP values equals the dif-
customers were included in the training data if they had a ferencebetweenthemodel’spredictionforthatinstanceand
correspondingrisklabelfromtheRGpredictiontableonthe the average prediction over the dataset,making them useful
samedateasthe“unknownrisk”label(n51,844).Ifsucha for interpreting complex models with clear, additive feature
labelwasavailable,wereplacedthe“unknownrisk”withthe contributions.
corresponding RG prediction label. Subsequent customers In parallel, we applied GMLVQ, a supervised learning
labeled as “unknown risk” without a corresponding RG technique designed to enhance the discriminative power of
prediction label were discarded from the training data features by optimizing a relevance matrix. GMLVQ adjusts
(n 5 4,004) while all “unknown risk” customers were dis- the feature space to maximize the margin between classes,
carded from the hold-out set (n 5 1,902). This approach which is crucial for effectively distinguishing between clas-
aimedtofillthegapsinthetrainingdata,therebyenhancing ses. GMLVQ assigns different levels of relevance to each
the dataset’s coverage and the robustness of the predictive feature, thereby improving the model’s ability to focus on
models and providing us with a more comprehensive and the most discriminative features for accurate predictions.
temporally distributed training dataset. This approach not only aids in classification but also pro-
We acknowledge that this imputation method, while vides a way to interpret the contribution of each feature to
beneficial, does introduce some potential noise into the the decision boundaries defined by the model.
model.However,thisnoisecanhavearegularizingeffecton Toensureequalcontributionofallfeaturesduringmodel
the complex model. Since the imputation was applied only training,wescaledthemusingastandardscaler.Wereduced
to the training data, we avoided any potential data leakage. redundancy by calculating a correlation matrix and
Without imputation, largetemporal gaps between manually removing one feature from each pair of highly correlated
assessed labels could have led to overfitting on sparse data features(Yu&Liu,2003).Subsequently,wetrainedamodel
patterns. By filling these gaps, we provided a more contin- on the scaled training dataset: XGBoost (Chen & Guestrin,
uousanddiversesetoftrainingexamples,helpingthemodel 2016). SHAP values were computed to evaluate the impor-
generalize better to unseen data. This regularizing effect tance of each feature in the prediction process.
reducedoverfitting,enhancingtherobustnessandreliability Tofinalizethefeatureselection,wecombinedthetop25
of the model’s predictions. features identified by each method. Choosing 25 features
Initially, customers were categorized into six risk levels, was a heuristic decision to balance model complexity and
creating a multi-class classification problem. However, pre- interpretability. This subset size ensured the final models
liminary models performed poorly, as fine-grained classifi- were both accurate and interpretable, maintaining manage-
cation can introduce unnecessary complexity and variance able complexity. By merging the most informative and
(Blanco,Perez-de-Viñaspre,Pérez,&Casillas,2020;Elyan& discriminative features from both methods, we created a
Gaber, 2017). To gain deeper insight into risk labels and comprehensive and optimized feature set for the classifica-
reduce the number of categories, we first generated average tion task.
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

| 494         |      |          |             |           |     |      |          |     | Journal | of Behavioral | Addictions |     | 14 (2025) | 1, 490–500 |     |
| ----------- | ---- | -------- | ----------- | --------- | --- | ---- | -------- | --- | ------- | ------------- | ---------- | --- | --------- | ---------- | --- |
| Statistical |      | analysis |             |           |     |      |          |     | RESULTS |               |            |     |           |            |     |
| We          | used | XGBoost  | to classify | customers |     | into | low-risk | and |         |               |            |     |           |            |     |
higher-risk categories. Comprehensive hyperparameter Predictions of problem gambling exhibited considerable
|        |     |           |       |        |         |     |       |         | temporal | stability, | even | with progressively |     | truncated | data. |
| ------ | --- | --------- | ----- | ------ | ------- | --- | ----- | ------- | -------- | ---------- | ---- | ------------------ | --- | --------- | ----- |
| tuning | was | conducted | using | Optuna | (Akiba, |     | Sano, | Yanase, |          |            |      |                    |     |           |       |
Ohta, & Koyama, 2019), an automated optimization Across all truncation periods (30-day, 60-day, 90-day, and
model’s full data), “loss chasing behavior weekly log transformed,”
| framework, |     | to ensure | the |     | accuracy | and | generaliz- |     |     |     |     |     |     |     |     |
| ---------- | --- | --------- | --- | --- | -------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
“netbalancetrend,”“maxdepositlogtransformed,”“session
| ability | across | different | datasets. |     | We focused |     | on optimizing |     |     |     |     |     |     |     |     |
| ------- | ------ | --------- | --------- | --- | ---------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
sump25,”and“totalbetsdailylogtransformed”consistently
| the             | F1 score | to   | balance | precision | and   | recall, | exploring |         |         |         |              |            |     |          |           |
| --------------- | -------- | ---- | ------- | --------- | ----- | ------- | --------- | ------- | ------- | ------- | ------------ | ---------- | --- | -------- | --------- |
|                 |          |      |         |           |       |         |           |         | had the | highest | SHAP values, | indicating |     | a strong | influence |
| hyperparameters |          | such | as      | learning  | rate, | number  | of        | estima- |         |         |              |            |     |          |           |
onthemodel’spredictions(Fig.2).AsshowninFig.3,hold-
| tors, | maximum | tree | depth, | subsampling |     | ratio, |     | column |     |     |     |     |     |     |     |
| ----- | ------- | ---- | ------ | ----------- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
outsetmetricsimprovedslightlywithmoredata,suggesting
| sampling |     | ratio, and | regularization |     | parameters. |     | We  | also |     |     |     |     |     |     |     |
| -------- | --- | ---------- | -------------- | --- | ----------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
optimized a probability threshold for converting predicted larger datasets enhance generalization and decision bound-
aries—particularly
probabilities into binary classifications. To respect the in identifying true positives. Overall,
|               |     |           |     |     |             |       |           |     | model performance |     | was | modest yet | consistent | (Table | 1). |
| ------------- | --- | --------- | --- | --- | ----------- | ----- | --------- | --- | ----------------- | --- | --- | ---------- | ---------- | ------ | --- |
| chronological |     | structure | of  | the | data during | model | selection |     |                   |     |     |            |            |        |     |
and avoid any leakage from future observations, we A bootstrap analysis of linear slopes across truncation
employed a nested forward-chaining cross-validation pro- periods (Full → 30-day → 60-day → 90-day) found no
|     | Specifically, |     |     |     |     |     |     |     | significant |     |     |     |     | confidence |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | ---------- | --- |
cedure. we sorted all training instances by date trend for most metrics, as their 95%
[(cid:1)0.009,
and split them into a 5-fold outer loop using a time-series intervals included zero: Accuracy 0.031], Recall
|        |          |      |      |            |      |      |          |       | (Sensitivity) | [(cid:1)0.018, | 0.095], | F1 Score | [(cid:1)0.008, | 0.035], | and |
| ------ | -------- | ---- | ---- | ---------- | ---- | ---- | -------- | ----- | ------------- | -------------- | ------- | -------- | -------------- | ------- | --- |
| split, | ensuring | that | each | validation | fold | came | strictly | after |               |                |         |          |                |         |     |
ROCAUC[(cid:1)0.008,0.008].However,Precision(PPV)hada
| the | training | folds | in time. | Within | each | outer | training | fold, |     |     |     |     |     |     |     |
| --- | -------- | ----- | -------- | ------ | ---- | ----- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
we performed a 3-fold time-series split in an inner loop to 95% CI entirely below zero [(cid:1)0.005, (cid:1)0.001], indicating a
refinehyperparameters,againpreservingthetemporalorder. consistently negative slope with increasing truncation.
This approach minimized overfitting and ensured that each Practically, Precision dropped slightly when moving from
|      |     |                |     |         |     |       |            |     | full to truncated |     | data. Despite | this, | overall | model | perfor- |
| ---- | --- | -------------- | --- | ------- | --- | ----- | ---------- | --- | ----------------- | --- | ------------- | ----- | ------- | ----- | ------- |
| step | of  | hyperparameter |     | tuning, | and | model | evaluation |     |                   |     |               |       |         |       |         |
respected the temporal sequence of events. mance remained stable across all truncation periods.
Weranupto1,000Optunatrials,trainingXGBoostwith We used a regression model to predict continuous risk
scores—groupedaslow,medium,andhighrisk—toevaluate
| different |     | hyperparameters |     | and | selecting | the | best based | on  |     |     |     |     |     |     |     |
| --------- | --- | --------------- | --- | --- | --------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
average F1 score across inner cross-validation folds. Using performance by risk level (Table 2 and Fig. 4). The model
|     |     |     |     |     |     |     |     |     | performed | well | for medium- | and | high-risk | categories, | with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---- | ----------- | --- | --------- | ----------- | ---- |
theseoptimalparameters,wetrainedfinalmodelsonthefull
datasetandeachtruncationperiod(30-day,60-day,90-day) predicted means closely matching true means. For instance,
group’s
before evaluating them on a hold-out test set (the unused in the 30-day dataset,the medium-risk actual mean
|       |           |            |     |                   |     |     |     |     | was 0.618 | vs. a | predicted | mean of | 0.500, | and the | high-risk |
| ----- | --------- | ---------- | --- | ----------------- | --- | --- | --- | --- | --------- | ----- | --------- | ------- | ------ | ------- | --------- |
| data) | to assess | real-world |     | generalizability. |     |     |     |     |           |       |           |         |        |         |           |
group’s
Predicted probabilities were converted into binary pre- actual mean was 0.761 vs. 0.758. In the 60-day
|          |       |     |           |            |     |     |             |     | dataset, | the high-risk | group’s | actual | mean | was | 0.765 vs. |
| -------- | ----- | --- | --------- | ---------- | --- | --- | ----------- | --- | -------- | ------------- | ------- | ------ | ---- | --- | --------- |
| dictions | using | the | optimized | threshold, |     | and | performance |     |          |               |         |        |      |     |           |
metrics—including
F1 score, ROC AUC, precision, recall, 0.755. However, the model consistently underestimated risk
accuracy, and confusion matrices—were computed. To forthelow-riskcategoryineverydataset:forexample,inthe
60-daydataset,thelow-riskgroup’struemeanwas0.529vs.
assessthestabilityofpredictionsacrossdifferentamountsof
historical data, we repeated this process for each truncation a predicted mean of 0.248, and in the full dataset, 0.557 vs.
period (30-day, 60-day, 90-day, and full) and compared 0.219. Thus, the model effectively identifies medium- and
performancemetrics.Finally,weappliedlinearregressionto high-riskindividualsbutstrugglestoaccuratelycapturelow-
| these     | metrics | to       | identify      | trends | as the | amount  | of         | data | risk cases.                                   |     |     |     |     |     |     |
| --------- | ------- | -------- | ------------- | ------ | ------ | ------- | ---------- | ---- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
|           |         |          |               |        |        |         | confidence |      | Figure4showsbetterperformanceinmediumandhigh- |     |     |     |     |     |     |
| decreased |         | and used | bootstrapping |        | to     | compute |            |      |                                               |     |     |     |     |     |     |
intervals for the slopes, determining whether changes in risk groups, with smaller gaps between true and predicted
performance were statistically significant over time. means, whereas the model underestimated risk in the low-
|     |             |     |                 |     |              |     |              |     | risk group | (the | gap increased | with | longer | truncation). | This |
| --- | ----------- | --- | --------------- | --- | ------------ | --- | ------------ | --- | ---------- | ---- | ------------- | ---- | ------ | ------------ | ---- |
|     | In addition | to  | classification, |     | we conducted |     | a regression |     |            |      |               |      |        |              |      |
analysis to predict continuous risk scores, providing a more was most pronounced in the full dataset, where the differ-
|          |     |               |     |        | model’s |            |          |     | enceforlow-riskcasesreached0.337,comparedto0.188for |     |     |     |     |     |     |
| -------- | --- | ------------- | --- | ------ | ------- | ---------- | -------- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| granular |     | understanding |     | of the |         | predictive | capabil- |     |                                                     |     |     |     |     |     |     |
ities. We used XGBoost as a regressor to predict risk scores medium risk and 0.057 for high risk.
| on   | a continuous | scale,  | which         | were | subsequently |     | categorized |     |     |     |     |     |     |     |     |
| ---- | ------------ | ------- | ------------- | ---- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
| into | low,         | medium, | and high-risk |      | levels.      |     |             |     |     |     |     |     |     |     |     |
DISCUSSION
Ethics
The study procedures were carried out in accordance with The results suggest that machine learning predictions of
the Declaration of Helsinki. The study was reviewed and problem gambling, assessed manually or through proxy
approved by the Swedish Ethical Review Authority (Dnr measures, show relative stability over time, with time being
2023-07288-02).Informedconsentwaswaivedbythereview intrinsicallylinkedtodata amount.Thisindicatesthatearly
board to permit research on pre-existing registry data. predictions are consistent and reliable, highlighting our
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

| Journal of Behavioral | Addictions | 14 (2025) 1, 490–500 |                         |                     | 495 |
| --------------------- | ---------- | -------------------- | ----------------------- | ------------------- | --- |
|                       |            | Fig.                 | 2.Featureimportanceplot |                     |     |
|                       |            | Fig.3.Temporal       | evaluationand           | predictionstability |     |
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

| 496 |     |                         |     |                     | Journal | of Behavioral    | Addictions |     | 14 (2025) | 1, 490–500 |
| --- | --- | ----------------------- | --- | ------------------- | ------- | ---------------- | ---------- | --- | --------- | ---------- |
|     |     | Table1.Modelperformance |     | metricsfordifferent |         | truncationlabels |            |     |           |            |
Truncation Accuracy Precision(PPV) Recall(Sensitivity) F1Score ROCAUC Specificity NPV
30-day-truncated-data 0.668 0.691 0.929 0.793 0.621 0.107 0.411
60-day-truncated-data 0.659 0.690 0.911 0.785 0.613 0.117 0.378
90-day-truncated-data 0.684 0.687 0.984 0.810 0.608 0.036 0.515
| Fulldata | 0.637 |     | 0.696 |     | 0.834 | 0.758 |     | 0.613 | 0.213 | 0.374 |
| -------- | ----- | --- | ----- | --- | ----- | ----- | --- | ----- | ----- | ----- |
Table2.Riskcategorypredictiontablewithdifference
| Dataset               |     | RiskCategory |                          |     | TrueMean         |       | PredictedMean |       |     | Difference |
| --------------------- | --- | ------------ | ------------------------ | --- | ---------------- | ----- | ------------- | ----- | --- | ---------- |
| 30-day-truncated-data |     | LowRisk      |                          |     | 0.600            |       |               | 0.242 |     | 0.358      |
| 30-day-truncated-data |     | MediumRisk   |                          |     | 0.618            |       |               | 0.500 |     | 0.118      |
| 30-day-truncated-data |     | HighRisk     |                          |     | 0.761            |       |               | 0.758 |     | 0.003      |
| 60-day-truncated-data |     | LowRisk      |                          |     | 0.529            |       |               | 0.248 |     | 0.281      |
| 60-day-truncated-data |     | MediumRisk   |                          |     | 0.625            |       |               | 0.497 |     | 0.127      |
| 60-day-truncated-data |     | HighRisk     |                          |     | 0.765            |       |               | 0.755 |     | 0.010      |
| 90-day-truncated-data |     | LowRisk      |                          |     | 0.588            |       |               | 0.255 |     | 0.333      |
| 90-day-truncated-data |     | MediumRisk   |                          |     | 0.609            |       |               | 0.538 |     | 0.072      |
| 90-day-truncated-data |     | HighRisk     |                          |     | 0.771            |       |               | 0.724 |     | 0.047      |
| Fulldata              |     | LowRisk      |                          |     | 0.557            |       |               | 0.219 |     | 0.337      |
| Fulldata              |     | MediumRisk   |                          |     | 0.646            |       |               | 0.458 |     | 0.188      |
| Fulldata              |     | HighRisk     |                          |     | 0.779            |       |               | 0.722 |     | 0.057      |
|                       |     |              | Fig. 4.Differencebetween |     | trueandpredicted | means |               |       |     |            |
model’s robustness. Our claims are based on the model’s score remained consistent across data truncation levels,
performance on a holdout validation set. By reserving a full indicating model reliability. Bootstrapping showed no sig-
year of data for validation, we evaluated the model on un- nificant slopesfor Accuracy,Recall,F1, andROC AUC,but
seendata,mimickingreal-worldconditionsforDutyofCare Precisionexhibitedaslight,consistentlynegativeslopefrom
findings confirm
obligations. Our that predictive analytics full data to 30-, 60-, and 90-day truncations. Despite this,
and machine learning are promising in identifying problem overall performance stayed relatively stable. Unlike pre-
Griffiths,
gamblers (Auer & 2022; Deng et al., 2019; Perrot liminary analysis based on training data and time series
etal.,2022),validatingtheeffectivenessofthesemethodsin cross-validation, the holdout evaluation did not show a
atemporallyrobustmanner.MetricslikeROCAUCandF1 declineinperformancemetricswiththefulldataset;instead,
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

| Journal | of Behavioral | Addictions |     | 14 (2025) | 1,  | 490–500 |     |     |     | 497 |
| ------- | ------------- | ---------- | --- | --------- | --- | ------- | --- | --- | --- | --- |
metricssuchasrecallandF1scoreimprovedwithincreased and accuracy of the labels. Despite this potential bias,
datasetsize,underscoringtheimportanceofusingaseparate manual assessments are generally considered more reli-
|     |     |     | reflection |     | model’s |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | ------- | --- | --- | --- | --- | --- |
validation set for an accurate of the true able than self-assessments, which are often prone to
performance. Therefore, our methods avoid the limitations inaccuracies (either deliberate or indeliberate) and
| of traditional | approaches |     | like self-report |     | questionnaires | and | inconsistencies. |     |     |     |
| -------------- | ---------- | --- | ---------------- | --- | -------------- | --- | ---------------- | --- | --- | --- |
simple behavioral tracking, which often suffer from validity Third, our truncation strategy intended to ensure tem-
and reliability issues (Edgren et al., 2016; Hodgins & poralstabilitybyfocusingonconsistentwindowsofactivity.
Makarchuk, 2003; MacKillop, Anderson, Castelda,Mattson, However, it may have inadvertently caused accounts with
&Donovick,2006).Ourmachinelearningapproachoffersa the most cumulative activity to contribute disproportion-
more reliable and scalable solution. The model consistently ately to the predictions. Initially, we attempted to use ac-
demonstrates reliable performance across different trunca- counts with 30, 60, or 90 days of total activity, but too few
tion periods, with SHAP values clarifying which features accounts met these criteria for meaningful model training.
model’s
drive its predictions. This highlights the ability to Consequently,weoptedforanactivitytruncationstrategyas
effectivelyinterpretcomplexbehavioraldatathattraditional a compromise, including enough data points for model
methods might not capture. training but possibly biasing the model toward accounts
Finally,studiesrelyingoncross-sectionaldatainherently with more extensive histories.
struggle to capture the temporal dynamics of gambling Fourth, our dataset comes from a single gambling
behavior or (Castrén, Kontto, Alho, & Salonen, 2018; operator in a competitive market, and does not include any
Gainsbury et al., 2013; Paterson et al., 2020). Our study given gamblers’ activity at other operators. Problem gam-
addresses this gap by evaluating the temporal stability of blers are typically more likely to gamble with multiple op-
predictions. The consistent importance of key features erators. Incomplete behavioral histories can lead to
across different truncation periods, as shown by SHAP underestimation or misclassification of certain gambling
behaviorsandlimitthebroaderapplicabilityofourfindings.
| values and | performance |     | metrics, | underscores | this | stability. |     |     |     |     |
| ---------- | ----------- | --- | -------- | ----------- | ---- | ---------- | --- | --- | --- | --- |
This is critical for developing models that can accurately Ideally, a “single customer view” mechanism—aggregating
operators—would
predictproblemgamblingoverextendedperiods,enhancing data from multiple yield more compre-
our understanding of gambling behavior dynamics. hensive insights and potentially more accurate predictive
The findings have practical implications for early iden- models. In lieu of a centralized system for sharing account-
operator-specific
tification and intervention in problem gambling. The sta- tracking data across operators, predictions
bility of predictions supports the timely implementation of remain the pragmatic approach to minimizing gambling
| preventivemeasures,whichcanmitigatetherisksassociated |     |     |     |     |     |     | harms. |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- |
setup—tem-
with problem gambling and aid stakeholders in developing Lastly, although the analysis uses a robust
effective public health monitoring and intervention pro- poralholdoutsplitsandnestedcross-validation—thelimited
grams (Jonsson, Munck, Hodgins, & Carlbring, 2023). bootstrapping approach (four samples per metric) may
|     |     |     |     |     |     |     | reduce sensitivity | to subtle trends. | Even so, narrow | confi- |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | ----------------- | --------------- | ------ |
Limitations dence intervals suggest stable performance metrics over
|            |             |              |      |           |              |          | time, indicating | temporal consistency. | Future research | with     |
| ---------- | ----------- | ------------ | ---- | --------- | ------------ | -------- | ---------------- | --------------------- | --------------- | -------- |
| This study | has several | limitations. |      | First,    | inconsistent | appli-   |                  |                       |                 |          |
|            |             |              |      |           |              |          | larger samples   | or alternativemethods | couldfurther    | validate |
| cation of  | risk labels | over         | time | may cause | the          | model to |                  |                       |                 |          |
findings.
these
| capture       | temporal   | biases       | rather than | genuine    | risk     | patterns, |                 |            |     |     |
| ------------- | ---------- | ------------ | ----------- | ---------- | -------- | --------- | --------------- | ---------- | --- | --- |
| especially    | in dynamic | environments |             | like       | gambling | where     |                 |            |     |     |
|               |            |              |             |            |          |           | Future research | directions |     |     |
| user behavior | and        | risk         | profiles    | can change | rapidly. | The       |                 |            |     |     |
|               | “unknown   | risk”        |             |            |          |           |                 |            |     |     |
presence of labels lead to an imbalanced Our findings suggest several avenues for future research.
dataset, underrepresenting certain risk categories and One key area is determining the optimal data window for
model’s
potentially skewing the learning process toward reliable predictions, balancing data sufficiency with model
strategy—filling
more prevalent categories. Our imputation performance. Exploring other machine learning techniques
gaps with responsible gambling (RG) prediction labels or refining labeling methods could further enhance accu-
—aimed
to mitigate this by improving the quality and racy. Validating the model with different datasets or in
quantity of labeled training data. This approach increased varied contexts will improve its generalizability and
| the number | of labeled |     | data points | and | ensured | a more | robustness. |     |     |     |
| ---------- | ---------- | --- | ----------- | --- | ------- | ------ | ----------- | --- | --- | --- |
uniform temporal distribution, allowing the models to To improve predictive capabilities, gambling operators
learnfromabroaderandmorerepresentativesample.While should routinely collect relevent features reflecting various
overfitting gambling—beyond
this enhanced dataset reduced the risk of and risk levels of problem purely trans-
increased generalizability, inherent imbalances may still actional data. This might include browsing patterns, time
pose challenges. Importantly, the hold-out validation data spent on different site areas, or engagement with specific
did not suffer from this limitation. features. Like how physical casinos observe customer
Second, potential bias introduced by manual assess- behavior on the floor, incorporating such behavioral in-
|            |              |     |         |               |     | Analysts’ | dicatorsonlinecouldenhancethemodel’sabilitytoidentify |     |     |     |
| ---------- | ------------ | --- | ------- | ------------- | --- | --------- | ----------------------------------------------------- | --- | --- | --- |
| ments used | for labeling |     | must be | acknowledged. |     |           |                                                       |     |     |     |
subjectivejudgmentscouldhaveimpactedtheconsistency at-risk individuals more accurately.
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

498 Journal of Behavioral Addictions 14 (2025) 1, 490–500
CONCLUSIONS this tool, the authors thoroughly reviewed and edited the
content as required, taking full responsibility for the final
content of the publication. The AI’s role was limited to
This study demonstrates the value of advanced machine
enhancing clarity, coherence, and presentation of the
learningtechniquesandrigorousmethodologiesingambling
manuscript.
research. Our findings show stable long-term prediction
performance, evidenced by consistent metrics across
Acknowledgements:WewouldliketoacknowledgeProf.Ion
different truncation periods. This supports the feasibility of
Petre at the University of Turku, whose lecture series
early detection and timely interventions, underscoring the
“Foundations of Machine Learning I-III” inspired much of
importance of methodological rigor in developing reliable
the analysis pipeline used in this study.
predictive models. These results have significant implica-
tions,providingastrongfoundationforfurtherresearchand
development in the field.
REFERENCES
Funding sources: This study was funded by the LeoVegas
Group, a licensed gambling operator in Sweden. Akiba, T., Sano, S., Yanase, T., Ohta, T., & Koyama, M. (2019).
Optuna: A next-generation hyperparameter optimization
Authors’ contributions: SA conceived the analysis pipeline, framework. http://arxiv.org/abs/1907.10902.
designed the methods, performed all statistical analyses, Auer, M., & Griffiths, M. D. (2022). Predicting limit-setting
developed and executed the modeling and feature engineer- behavior of gamblers using machine learning algorithms:
ing,builtthedatabase,anddraftedthemanuscript.PL,asthe Areal-worldstudyofNorwegiangamblersusingaccountdata.
mainsupervisor,wasresponsibleforprojectorganizationand International Journal of Mental Health and Addiction, 20(2),
oversight, providing critical revision of the manuscript and
771–788.https://doi.org/10.1007/s11469-019-00166-2.
engaging in discussions regarding study concept and meth- Barros, B. de M., Nascimento, H. A. D. do, Guedes, R., &
odological and analysis approaches particularly around tem- Monsueto, S. E. (2023). Evaluating splitting approaches in the
poral stability. PC, as co-supervisor, contributed to thestudy context of student dropout prediction. https://arxiv.org/abs/
concept alongside PL and provided feedback during critical 2305.08600.
revision of the manuscript. KL, a data scientist at LeoVegas, Bitar, R., Nordt, C., Grosshans, M., Herdener, M., Seifritz, E., &
supervised thedatascienceaspects,providedtechnicalinput, Mutschler, J. (2017). Telecommunications network measure-
facilitated data transfer, and participated in discussions on mentsofonlinegamblingbehaviorinSwitzerland:Afeasibility
machinelearningandstatisticalmethods.MB,asheadofdata study. European Addiction Research, 23(2), 106–112. https://
science at LeoVegas, contributed to data acquisition, doi.org/10.1159/000471482.
addressed data-related queries, and provided expertise on Blanco,A.,Perez-de-Viñaspre,O.,Pérez,A.,&Casillas,A.(2020).
study feasibility, technical aspects, and conceptual input. All Boosting ICD multi-label classification of health records with
authors were part of the steering group, which met monthly contextual embeddings and label-granularity. Computer
andwasorganizedbyPL.SAandPLhadfullaccesstoalldata MethodsandProgramsinBiomedicine,188,105264.https://doi.
in the study and take responsibility for the integrity of the org/10.1016/j.cmpb.2019.105264.
data and the accuracy of the data analysis. All authors Braverman,J.,LaPlante,D.A.,Nelson,S.E.,&Shaffer,H.J.(2013).
approved the final manuscript.
Usingcross-gamebehavioralmarkersforearlyidentificationof
high-risk internet gamblers. Psychology of Addictive Behaviors,
Conflict of interest: This study is part of an industry-
27(3),868–877.https://doi.org/10.1037/a0032818.
academia collaboration on Responsible Gambling, financed Braverman, J., & Shaffer, H. J. (2012). How do gamblers start
by the LeoVegas Group, a licensed gambling operator in gambling: Identifying behavioural markers for high-risk
Sweden. The research was planned, performed and sub- internet gambling. The European Journal of Public Health,
mitted under full academic freedom, guaranteed per a
22(2),273–278.https://doi.org/10.1093/eurpub/ckp232.
writtenagreement.Thefundershadnoroleinthedesignor Browne, M., Rawat, V., Greer, N., Langham, E., Rockloff, M., &
execution of the study, nor the decision to publish. Hanley,C.(2017).Whatistheharm?Applyingapublichealth
SA’s doctoral position is financed by the LeoVegas Group methodologytomeasuretheimpactofgamblingproblemsand
but is an employee of Karolinska Institutet and reports no harmonqualityoflife.JournalofGamblingIssues,36.https://
otherpotentialconflictsofinterest.PLandPCreportspastand doi.org/10.4309/jgi.v0i36.3978.
ongoing industry-academia collaborations with several Castrén, S., Kontto, J., Alho, H., & Salonen, A. H. (2018). The
gambling providers, including project-specific funding, but relationship between gambling expenditure, socio‐de-
have no personal ties to the gambling industry, financial or mographics, health‐related correlates and gambling behaviour
otherwise. MB is employed by the LeoVegas Group. —across‐sectional population‐based survey in Finland. Addic-
tion,113(1),91–106.https://doi.org/10.1111/add.13929.
Generative AI use: During the preparation of this work, the Catania, M., & Griffiths, M. D. (2021). Understanding online
corresponding author utilized ChatGPT to enhance writing voluntaryself-exclusioningambling:Anempiricalstudyusing
styleandcorrectgrammarandspelling.Followingtheuseof account-basedbehavioraltrackingdata.InternationalJournalof
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

Journal of Behavioral Addictions 14 (2025) 1, 490–500 499
EnvironmentalResearchandPublicHealth,18(4),2000.https:// Hofmarcher, T., Romild, U., Spångberg, J., Persson, U., &
doi.org/10.3390/ijerph18042000. Håkansson, A. (2020). Thesocietal costs ofproblem gambling
Chen,T.,&Guestrin,C.(2016).XGBoost:Ascalabletreeboosting inSweden.BMCPublicHealth,20(1),1921.https://doi.org/10.
system.https://doi.org/10.1145/2939672.2939785. 1186/s12889-020-10008-9.
Cisneros Örnberg, J., & Hettne, J. (2018). The future Swedish Hopfgartner, N., Auer, M., Griffiths, M. D., & Helic, D. (2022).
gambling market: Challenges in law and public policies. In Predictingself-exclusionamongonlinegamblers:Anempirical
Gambling Policies in European welfare states (pp. 197–216). real-world study. Journal of Gambling Studies, 39(1), 447–465.
Springer International Publishing. https://doi.org/10.1007/978- https://doi.org/10.1007/s10899-022-10149-z.
3-319-90620-1_11. Hopfgartner, N., Auer, M., Helic, D., & Griffiths, M. D. (2024).
Clune, S., Ratnaike, D., White, V., Donaldson, A., Randle, E., Using artificial intelligence algorithms to predict self-reported
O’Halloran, P., & Lewis, V. (2024). What is known about problem gambling among online casino gamblers from
population level programs designed to address gambling- different countries using account-based player data. Interna-
related harm: Rapid review of the evidence. Harm Reduction tionalJournalofMentalHealthandAddiction.Advanceonline
Journal,21(1).https://doi.org/10.1186/s12954-024-01032-8. publication.https://doi.org/10.1007/s11469-024-01312-1.
Deng, X., Lesch, T., & Clark, L. (2019). Applying data science to Jonsson, J., Abbott, M. W., Sjöberg, A., & Carlbring, P. (2017).
behavioralanalysisofonlinegambling.CurrentAddictionReports, Measuring gambling reinforcers, over consumption and fal-
6(3),159–164.https://doi.org/10.1007/s40429-019-00269-9. lacies: The psychometric properties and predictive validity of
Dowling, N. A., Merkouris, S. S., Greenwood, C. J., Oldenhof, E., theJonsson-Abbottscale.FrontiersinPsychology,8.https://doi.
Toumbourou, J. W., & Youssef, G. J. (2017). Early risk and org/10.3389/fpsyg.2017.01807.
protective factors for problem gambling: A systematic review Jonsson, J., Munck, I., Hodgins, D. C., & Carlbring, P. (2023).
and meta-analysis of longitudinal studies. Clinical Psychology Reachingouttobiglosers:Exploringinterventioneffectsusing
Review,51,109–124.https://doi.org/10.1016/j.cpr.2016.10.008. individualized follow-up. Psychology of Addictive Behaviors,
Eadington,W.R.(2003).Measuringcostsfrompermittedgaming: 37(7),886–893.https://doi.org/10.1037/adb0000906.
Conceptsandcategoriesinevaluatinggambling’sconsequences. Jonsson, J., Munck, I., Volberg, R., & Carlbring, P. (2017).
JournalofGamblingStudies,19(2),185–213.https://doi.org/10. GamTest:Psychometricevaluationandtheroleofemotionsin
1023/A:1023681315907. an online self-test for gambling behavior. Journal of Gambling
Edgren, R., Castrén, S., Mäkelä, M., Pörtfors, P., Alho, H., & Studies, 33(2), 505–523. https://doi.org/10.1007/s10899-017-
Salonen, A. H. (2016). Reliability of instruments measuring 9676-4.
at-risk and problem gambling among young individuals: Kairouz, S., Costes, J.-M., Murch, W. S., Doray-Demers, P.,
A systematic review covering years 2009–2015. Journal of Carrier,C.,&Eroukmanoff,V.(2023).Enablingnewstrategies
Adolescent Health, 58(6), 600–615. https://doi.org/10.1016/ to prevent problematic online gambling: A machine learning
j.jadohealth.2016.03.007. approach for identifying at-risk online gamblers in France.
Elyan,E.,&Gaber,M.M.(2017).Ageneticalgorithmapproachto InternationalGamblingStudies,23(3),471–490.https://doi.org/
optimising random forests applied to class engineered data. 10.1080/14459795.2022.2164042.
Information Sciences, 384, 220–234. https://doi.org/10.1016/j. Kuentzel, J. G., Henderson, M. J., & Melville, C. L. (2008). The
ins.2016.08.007. impact of social desirability biases on self-report among col-
Gainsbury,S.,Sadeque,S.,Mizerski,D.,&Blaszczynski,A.(2013). lege student and problem gamblers. Journal of Gambling
Wagering in Australia: A retrospective behavioural analysis of Studies, 24(3), 307–319. https://doi.org/10.1007/s10899-008-
betting patterns based on player account data. The Journal of 9094-8.
GamblingBusinessandEconomics,6(2),50–68.https://doi.org/ Laurikkala, J., & Juhola, M. (2001). Hierarchical clustering of
10.5750/jgbe.v6i2.581. female urinary incontinence data having noise and outliers
Goldstein,A.L.,Vilhena-Churchill,N.,Munroe,M.,Stewart,S.H., (pp.161–167). https://doi.org/10.1007/3-540-45497-7_24.
Flett,G.L.,&Hoaken,P.N.S.(2017).Understandingtheeffects Lövdal, S., & Biehl, M. (2024). Iterated relevance matrix analysis
of social desirability on gambling self-reports. International (IRMA)fortheidentificationofclass-discriminativesubspaces.
Journal of Mental Health and Addiction, 15(6), 1342–1359. Neurocomputing, 577, 127367. https://doi.org/10.1016/j.
https://doi.org/10.1007/s11469-016-9668-0. neucom.2024.127367.
Haeusler,J.(2016).Followthemoney:Usingpaymentbehaviouras Lundberg,S.M.,Allen,P.G.,&Lee,S.-I.(n.d.).Aunifiedapproach
predictor for future self-exclusion. International Gambling tointerpretingmodelpredictions.https://github.com/slundberg/
Studies,16(2),246–262.https://doi.org/10.1080/14459795.2016. shap.
1158306. MacKillop, J., Anderson, E. J., Castelda, B. A., Mattson, R. E., &
Hahmann, T., Hamilton-Wright, S., Ziegler, C., & Matheson, F. I. Donovick, P. J. (2006). Divergent validity of measures of
(2021). Problem gambling within the context of poverty: A cognitive distortions, impulsivity, and time perspective in
scopingreview.InternationalGamblingStudies,21(2),183–219. pathological gambling. Journal of Gambling Studies, 22(3),
https://doi.org/10.1080/14459795.2020.1819365. 339–354.https://doi.org/10.1007/s10899-006-9021-9.
Hodgins, D. C., & Makarchuk, K. (2003). Trusting problem gam- Murch, W. S., Kairouz, S., Dauphinais, S., Picard, E., Costes, J., &
blers: Reliability and validity of self-reported gambling French, M. (2023). Using machine learning to retrospectively
behavior. Psychology of Addictive Behaviors, 17(3), 244–248. predict self‐reported gamblingproblemsinQuebec. Addiction,
https://doi.org/10.1037/0893-164X.17.3.244. 118(8),1569–1578.https://doi.org/10.1111/add.16179.
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC

500 Journal of Behavioral Addictions 14 (2025) 1, 490–500
Park, Y., Eom, D., Seo, B., & Choi, J. (2020). Improved predictive behavioralchangesusingshapelets.InProceedings-2019IEEE/
deep temporal neural networks with trend filtering. In Pro- WIC/ACM international Conference on web intelligence, WI
ceedings of the first ACM international conference on AI in 2019 (pp.367–372).https://doi.org/10.1145/3350546.3352549.
finance(pp.1–8).https://doi.org/10.1145/3383455.3422565. Swedish Gambling Act, Pub. L. No. 2018:1138, Swedish code of
Paterson,M.,Taylor,M.,&Gray,M.(2020).Trajectoriesofsocial statutes(2018).
and economic outcomes and problem gambling risk in Ukhov,I.,Bjurgert,J.,Auer,M.,&Griffiths,M.D.(2021).Online
Australia. Social Indicators Research, 148(1), 297–321. https:// problemgambling:Acomparisonofcasinoplayersand sports
doi.org/10.1007/s11205-019-02194-w. bettorsviapredictivemodelingusing behavioraltrackingdata.
Percy, C., França, M., Dragi(cid:1)cević, S., & d’Avila Garcez, A. (2016). JournalofGamblingStudies,37(3),877–897.https://doi.org/10.
Predicting online gambling self-exclusion: an analysis of the 1007/s10899-020-09964-z.
performance of supervised machine learning models. Interna- Wang,T.D.,Plaisant,C.,Shneiderman,B.,Spring,N.,Roseman,D.,
tional Gambling Studies, 16(2), 193–210. https://doi.org/10. Marchand,G.,…Smith,M.(2009).Temporalsummaries:Sup-
1080/14459795.2016.1151913. portingtemporalcategoricalsearching,aggregationandcompar-
Perrot,B.,Hardouin,J.B.,Thiabaud,E.,Saillard,A.,Grall-Bronnec,M., ison.IEEETransactionsonVisualizationandComputerGraphics,
& Challet-Bouju, G. (2022). Development and validation of a 15(6),1049–1056.https://doi.org/10.1109/TVCG.2009.187.
predictionmodelforonlinegamblingproblemsbasedonplayers’ Weatherly,J.N.,Montes,K.S.,Peters,D.,&Wilson,A.N.(2012).
account data. Journal of Behavioral Addictions, 11(3), 874–889. Gambling behind the walls: A behavior-analytic perspective.
https://doi.org/10.1556/2006.2022.00063. The Behavior Analyst Today, 13(3–4), 2–8. https://doi.org/10.
Sato,H.,&Kawahara,J.(2011).Selectivebiasinretrospectiveself- 1037/h0100725.
reportsofnegativemoodstates.Anxiety,Stress&Coping,24(4), Yu, L., & Liu, H. (2003). Efficiently handling feature redundancy
359–367.https://doi.org/10.1080/10615806.2010.543132. in high-dimensional data. In Proceedings of the Ninth ACM
Suzuki, H., Nakamura, R., Inagaki, A., Watanabe, I., & Takagi, T. SIGKDD international conference on knowledge discovery and
(2019). Early detection of problem gambling based on datamining,pp.685–690.https://doi.org/10.1145/956750.956840.
OpenAccessstatement.Thisisanopen-accessarticledistributedunderthetermsoftheCreativeCommonsAttribution-NonCommercial4.0InternationalLicense
(https://creativecommons.org/licenses/by-nc/4.0/),whichpermitsunrestricteduse,distribution,andreproductioninanymediumfornon-commercialpurposes,provided
theoriginalauthorandsourcearecredited,alinktotheCCLicenseisprovided,andchanges–ifany–areindicated.
Unauthenticated | Downloaded 07/01/26 08:54 AM UTC