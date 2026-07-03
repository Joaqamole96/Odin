|                       | Predicting    |             | problem   |          | gambling  |           |             | among      | online |
| --------------------- | ------------- | ----------- | --------- | -------- | --------- | --------- | ----------- | ---------- | ------ |
|                       | sports        |             | and race  | bettors: |           | Assessing |             | the        | value  |
|                       | of            | machine     | learning  |          | using     |           | behavioural |            | and    |
|                       | self-reported |             |           | data     |           |           |             |            |        |
|                       |               |             | HEIRENE1p |          |           | ZHANG2    |             |            |        |
| Journal of Behavioral | ROBERT        | M.          |           |          | , EDEN    |           |             | ,          |        |
| Addictions            |               | VANICHKINA2 |           |          |           |           |             | LEAU1,3,   |        |
|                       | DARYA         |             |           |          | , CHARLES |           | T. DE       |            |        |
|                       |               |             | HUYNH1    |          |           |           |             | GAINSBURY1 |        |
|                       | EUNICE        | L.          | Y.        |          | and       | SALLY     | M.          |            |        |
DOI:
10.1556/2006.2025.00525 1Brain&MindCentre, SchoolofPsychology,University ofSydney, NSW,Australia
©2026TheAuthor(s)
|     | 2SydneyInformaticsHub, |     | UniversityofSydney,NSW,Australia |     |     |     |     |     |     |
| --- | ---------------------- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- |
3Developmentand Psychopathology(ADAPT)-Lab,DepartmentofPsychology,University
|     | ofAmsterdam,             | TheNetherlands |                                               |     |     |     |     |                              |     |
| --- | ------------------------ | -------------- | --------------------------------------------- | --- | --- | --- | --- | ---------------------------- | --- |
|     | Received:November10,2025 |                | (cid:129) Revisedmanuscriptreceived:May6,2026 |     |     |     |     | (cid:129) Accepted:May7,2026 |     |
FULL-LENGTH REPORT
ABSTRACT
Background and aims: Online gambling operators collect detailed behavioural data that can identify
customers at risk ofharmful gambling. However, there is limited clarity on howto optimally achieve
this in practice, including which variables are most useful and whether short-term data windows are
sufficient for risk detection. These details are increasingly important as regulatory frameworks
emphasise timely intervention. We examined the value of machine learning in this context by
comparing models trained on 30 days versus six months of behavioural data and exploring whether
incorporatingsurveyresponsesenhancedperformance.Methods:CustomersfromtwoAustraliansports
andracebettingsites(N51,470)completedasurveyincludingtheProblemGamblingSeverityIndex
(PGSI)andmeasuresofemployment,income,gamblingsatisfaction,andnumberofgamblingaccounts.
Webuiltmachinelearningmodelstoclassifyparticipantsintoriskgroups(PGSI1–7[no-to-moderate-
PGSI≥8
risk] vs. [high-risk]), comparing performance across data windows (30 days vs. six months),
and with or without survey variables. Results: Models using only behavioural data achieved adequate
classificationaccuracy(AUROC50.74–0.75),withsimilarperformanceacross30-dayandsix-month
windows.Themostpredictiveaccount-basedvariableswereage,depositsperactiveday,averagestake,
anddayssincebetting.Combiningbehaviouraldatawithself-reportedvariablesenhancedperformance
(AUROC50.76–0.85).Twoself-reportedvariables—numberofgamblingaccountsheldandgambling
satisfaction—wereprimarilyresponsiblefortheseimprovements.Conclusions:Machinelearningmodels
candetectat-riskcustomersononlinesportsandracebettingsitesusingonly30daysofbehavioural
data.Performance canbe improvedbyaddingminimal, non-intrusiveself-report measures.
KEYWORDS
|     | gamblingdisorder,risk |     | detection,artificial |     | intelligence, | algorithm,behavioural |     | marker |     |
| --- | --------------------- | --- | -------------------- | --- | ------------- | --------------------- | --- | ------ | --- |
INTRODUCTION
Onlinegamblingaccountsforalargeandgrowingproportionoftheglobalgamblingmarket
pCorrespondingauthor.
and,insomejurisdictions,hassurpassedland-basedgambling(EuropeanGaming&Betting
E-mail:robert.heirene@sydney.edu.au
Association, 2025). In Australia, more than one in ten people report gambling online
(ACMA,2022).Participationinonlinegambling,comparedtotraditionalland-basedforms,
has been linked to higher rates of problematic gambling (Allami et al., 2021); although the
highest rates are found among those who combine both forms (Hing, Russell, et al., 2022).
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

2 Journal of Behavioral Addictions
Online gambling harms are attributed to structural features Recent machine learning studies have used self-reported
relating to the speed, accessibility, ease of betting; the lower problem gambling scores to provide a more reliable indi-
salience of digital spending; aggressive marketing and cation of risk than VSE. Combining self-report customer
frequent promotions; and, in many jurisdictions, less regu- survey and behavioural account datasets is increasingly
lation and consumer protections than land-based gambling feasible with partnerships between researchers and opera-
(Hing et al., 2024; Hing, Smith, et al., 2022). tors, in some cases facilitated by gambling regulators
Unlike anonymous cash-based gambling, online (Delfabbroetal.,2023;Forrest&McHale,2022).Todate,at
gambling operators collect detailed data on all customer least six studies have built models using account data to
transactions and site interactions (Delfabbro, Parke, & detect self-reported problem gambling status as determined
Catania, 2023; Gainsbury, 2011). This behavioural account via the Problem Gambling Severity Index (PGSI; Ferris &
or tracking data offers a powerful tool for detecting cus- Wynne, 2001). These studies (Auer & Griffiths, 2022;
tomersatriskofproblematicorharmfulgamblingandcould Hopfgartner, Auer, Helic, & Griffiths, 2024; Kairouz et al.,
enable timely, personalised interventions (Auer & Griffiths, 2023; Luquiens et al., 2016; Murch etal., 2023; Perrot et al.,
2014; Gainsbury, 2011; LaBrie & Shaffer, 2011). Artificial 2022) have obtained adequate–good classification perfor-
Intelligence (AI), including machine learning algorithms, is mance (Area Under the Receiver Operating Characteristic
being increasingly used in this risk detection context (Gha- Curve [AUROC] 5 0.72–0.88) and similarly find that
harian et al., 2023; Marionneau, Ristolainen, & Roukka, Random Forest models perform well.
2025). Machine learning presents an efficient and econom- While the understanding of online gambling risk detec-
icalwaytoprocesslargedatasetsofbehaviouralaccountdata tion has been advanced by studies linking behavioural and
andidentifypatternsacrossmultiplebehaviouralmarkersof survey datasets, further efforts are needed to understand
harm (e.g., time and money spent). Machine learning how machine learning models can be optimised in this
models can distinguish between lower- and higher-risk context.Inarecentprioritysettingexercise,using“bigdata”
users, supporting operators in delivering targeted harm- and approaches such as machine learning to better under-
reduction strategies. standindicatorsofrisky/harmful gamblingandhowwecan
Licensing bodies typically require online operators to identify and support at-risk consumers was raised as an
provide a voluntary self-exclusion (VSE) feature that allows importantresearchpriorityandultimatelyranked22nd(out
customers to request that operators block them from of 41) in important topics relating to interventions. Others
gambling with their site(s) (Gainsbury, 2014). Studies have also recently highlighted the need for more research
applying machine learning for risk detection often use VSE that can assist with the early identification of at-risk in-
asaproxyforproblem orhigh-riskgamblingastheirtarget dividuals (Bowden-Jones et al., 2022). Several jurisdictions
or outcome variable. This assumes that VSE is primarily now require operators to actively monitor their customers
motivated by gambling-related harms (Catania & Griffiths, for signs of problematic gambling, including the UK (UK
2021). Studies using VSE as their outcome have obtained Gambling Commission, 2022) and Sweden (Lakew &
adequate to excellent classification performance1 and often Lindner,2025).Thisdemonstratestheneedforresearchthat
show that Random Forest (a commonly used machine can guide the implementation of effective risk detection
learning algorithm that combines multiple decision trees to systems (for a recent overview of countries requiring
make predictions) outperforms other approaches (Finken- customer risk monitoring, see Auer & Griffiths, 2026).
wirth, MacDonald, Deng, Lesch, & Clark, 2020; Hopfgart- The variation in the performance of machine learning
ner,Auer,Griffiths,&Helic,2022;Percy,França,Dragi(cid:1)cević, models by the data windows available to train the models
& d’Avila Garcez, 2016). VSE captures a clearly defined (e.g., one weekvs. oneyear ofbehavioural data)remainsan
group and is easily recorded by operators; however, it is an area in need of investigation. One study of 35,048 Swedish
unreliable proxy for problem gambling (Griffiths & Auer, onlinecasinogamblingcustomersdemonstratedthatmodels
2016). Individuals may self-exclude for reasons that do not trained on different behavioural data timeframes (30, 60,
include the experience of gambling harms, including to and 90 days) performed similarly, with marginally better
prevent harms or to simply stop using the site (Hayer & performance for the shorter timeframes (Andersson,
Meyer,2011).CataniaandGriffiths(2021)foundhalfofthe Carlbring, Lyon, Bermell, & Lindner, 2025). This is impor-
customers who used VSE did so within the first seven days tantasidentifyingriskygamblingearlyinaperson’saccount
of registration and spent less money than those who closed history can prompt earlier interventions. However, partici-
theiraccountsduetogamblingproblems.Thus,modelsbuilt pants in the study were given non-precise labels (higher-or
to predict VSE may subsequently fail to identify individuals lower-risk)basedonassessmentsconductedbythegambling
who are genuinely at risk of experiencing gambling operator. Verification of these classifications was not
problems. includedinthestudyandtheyappeartohavebeenpartially
basedonthesamevariablesusedintheclassificationmodel
(e.g., deposit patterns, session duration). This creates a risk
of circularity, wherein the accuracy of model predictions is
inflatedastheywereinformedbythesameinformationused
1As defined by Area Under the Receiver Operating Characteristic Curve
(AUROC)valuesintherangeof0.75–0.94.SeeStatisticalanalysissection to establish initial classifications. Further studies have not
foradescriptionofthismetric. compared different windows of behavioural data for model
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

Journal of Behavioral Addictions 3
development, typically focusing on a 12-month period operators or regulators with minimal disruption to con-
(Murch et al., 2023; Perrot et al., 2022). In practice, waiting sumers,which was operationalisedas beingobtainable via a
to obtain protracted behavioural data before applying these single question, and [2] the information must have an
models may delay the identification of at-risk customers, obvious connection with risk, such that consumers could
thus contributing to greater harms. Contemporary regula- easily understand the request without needing additional
toryframeworksnowrequiremanyoperatorstoidentifyand explanation (e.g., income, but not marital status).
respondtoriskovershorttimeframes.Forexample,theUK
Gambling Commission requires operators to continuously
METHODS
monitor customer behaviour and act in a timely manner,
which may include real-time interventions when indicators
of harm are observed (UK Gambling Commission, 2023). No hypotheses or data analysis plans were preregistered as
Self-reported data from consumers provides valuable thiswasanexploratorystudy.Whilstweplannedtousethe
context related to risk of problematic gambling unavailable data for this purpose before collection, the methods were
in operator-held data (Forrest & McHale, 2022). The inte- finalised after observing the data. The overall methods used
gration of self-reported data into machine learning models were, however, preregistered on Open Science Framework
hasnotyetbeenwellresearched.Recentstudiesindicatethat (https://osf.io/vdsmw), including the recruitment strategy,
this approach may hold value. Auer and Griffiths (2023) participant eligibility, data collection survey, and variables
developed a linear model to predict responses to a single collected.
item(“Mygamblingisaproblemsometimes”)bycombining
a small number of self-reported and account variables from Participants and procedures
race betting consumers in Norway (N 5 3,627). Sacco and
Customersfromtwoonlinesportsandracewageringsitesin
Jeong (2025) combined ticket upload data and survey re-
sponses from 5,903 US lottery players, finding that the six Australia owned by the same parent company (Entain
Australia) were invited to take part in a survey about their
most important variables in their model were all self-re-
gambling.Eligiblecustomershadtohaveplacedatleastone
ported, including frequency of other gambling, income,
bet with the site in the preceding six months, held an ac-
education,age,andemploymentstatus.Overall,thisnascent
count for at least 30 days, and could not have a suspended
approach requires more extensive investigation.
account, be self-excluded, or be on a timeout/take-a-break.
To our knowledge, no studies have developed machine
Two cohorts from the total eligible population were identi-
learningmodelsforidentifyingat-riskconsumersonAustralian
fied for inclusion in the study by the operator. These
sitesorspecificallyinanonlinesportsandracebettingcontext.
included all customers flagged by the operator’s internal
Evidence suggests that regional differences in gambling
risk-detection system as “at-risk” in the six months prior
behaviour may impact model efficacy (Hopfgartner et al.,
and a random sample of all “not-at-risk” customers at a
2024).Australiarepresentsauniquejurisdictionwithhighper
20:80at-risk/not-at-risk ratio. This resulted in a sample of
capitagamblingexpenditure(Greeretal.,2023)andanonline
4,829“at-risk”and20,000“not-at-risk”customers(rounded
marketrestrictedtosportsandracebettingandlottery.Existing
to the nearest thousand). These 24,829 customers were
machine learning studies attempting to predict self-reported
invited to take part in a survey about their gambling in
problem gambling have focused on online casino (Auer &
Griffiths,2022;Hopfgartneretal.,2024),poker(Luquiensetal., January 2024. Email invitations were sent via the operator,
and an SMS reminder was sent eight days later. In total,
2016), or mixed modalities (Murch et al., 2023; Perrot et al.,
2022), precluding specific insights into the unique risk behav- 3,867 people opened the survey and 1,470 answered all
questions.Participantsweregiventheoptiontoenteraprize
ioursinasportsandracebettingenvironment(e.g.,variability
drawtowinoneof20e-giftvouchersvaluedat$250,which
in sports bet on, odds selections). The performance of these
could not be redeemed for cash or spent on gambling.
models in an Australian sports and race betting context, and
In a separate analysis of the data used here, we showed
which variables are most predictive of risky play, remains un-
that the survey sample (i.e., the 1,959 people completing all
clear.Inthisstudy,weaimedtoextendtheexistingliteratureon
PGSI items) was broadly representative of the wider popu-
online gambling risk detection by:
lationinvitedtotakepart,butwasmoreengagedonaverage
1. building machine learning models to predict self-re- (Heirene, Cobb-Clark,Tymula, Santos, &Gainsbury,2025).
portedproblemgamblingusingbehaviouralaccountdata Most notably, survey responders bet more regularly in
from Australian sports and race betting consumers the preceding six months than non-responders (Cohen’s
2. comparingtheclassificationperformanceofmodelsbuilt d50.58),hadplacedabetmorerecently(d5(cid:1)0.51),were
using past-30-day versus past-six-month behavioural older (d 5 0.40), and made more deposits (d 5 0.32).
account data A summary of the demographic characteristics of the two
3. comparingtheclassificationperformanceofmodelsbuilt samples used in our analyses are presented in Table 1.
with and without survey-based variables.
Measures & feature generation
To enhance the practical relevance of results, survey-
based variables were included only if they satisfied two Outcome variable. The Problem Gambling Severity Index
criteria: [1] the information could be plausibly collected by (PGSI; Ferris & Wynne, 2001) was used to assess
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

| 4   |     |     |     |     | Journal | of Behavioral Addictions |
| --- | --- | --- | --- | --- | ------- | ------------------------ |
Table1.Sampledemographic characteristics
|     |     |     |     | Fullsample | Subsample | with6monthsofbetting |
| --- | --- | --- | --- | ---------- | --------- | -------------------- |
|     |     |     |     | N51,470    |           | N51,349              |
Characteristic
| Age |     |     |     | 40(30,52) |     | 40(30,53) |
| --- | --- | --- | --- | --------- | --- | --------- |
Gender
| Female |     |     |     | 154(10%)   |     | 135(10%)   |
| ------ | --- | --- | --- | ---------- | --- | ---------- |
| Male   |     |     |     | 1,292(88%) |     | 1,190(88%) |
Unknownp
|     |     |     |     | 24(1.6%) |     | 24(1.8%) |
| --- | --- | --- | --- | -------- | --- | -------- |
Employment
| Employed   |     |     |     | 1,384(94%) |     | 1,273(94%) |
| ---------- | --- | --- | --- | ---------- | --- | ---------- |
| Unemployed |     |     |     | 86(5.9%)   |     | 76(5.6%)   |
Education#
Year11orbelow(includesCertificateI/II/n)
|                   |                 |     |     | 246(17%)  |     | 224(17%)  |
| ----------------- | --------------- | --- | --- | --------- | --- | --------- |
| Year12            |                 |     |     | 359(24%)  |     | 329(24%)  |
| CertificateIII/IV |                 |     |     | 255(17%)  |     | 236(17%)  |
| Advanced          | diploma/diploma |     |     | 128(8.7%) |     | 116(8.6%) |
| Bachelor’sdegree  |                 |     |     | 276(19%)  |     | 256(19%)  |
diplomaorgraduatelevelcertificate
| Graduate |     |     |     | 117(8.0%) |     | 105(7.8%) |
| -------- | --- | --- | --- | --------- | --- | --------- |
Master’sdegree
|                                       |                    |     |     | 76(5.2%) |     | 72(5.3%) |
| ------------------------------------- | ------------------ | --- | --- | -------- | --- | -------- |
| Doctoraldegree                        |                    |     |     | 13(0.9%) |     | 11(0.8%) |
| Householdincome                       | (pre-tax)          |     |     |          |     |          |
| NegativeorZeroIncome                  |                    |     |     | 11(0.7%) |     | 8(0.6%)  |
| $1–$49,999/yr                         | ($1–$959/wk)       |     |     |          |     |          |
|                                       |                    |     |     | 169(11%) |     | 151(11%) |
| $50,000–$59,999/yr                    | ($960–$1,149/wk)   |     |     |          |     |          |
|                                       |                    |     |     | 72(4.9%) |     | 66(4.9%) |
| $60,000–$79,999/yr                    | ($1,150–$1,529/wk) |     |     | 148(10%) |     | 136(10%) |
| $80,000–$99,999/yr                    | ($1,530–$1919/wk)  |     |     | 177(12%) |     | 163(12%) |
| $100,000–$124,999/yr($1920–$2,399/wk) |                    |     |     | 166(11%) |     | 150(11%) |
$125,000–$149,999/yr($2,400–$2,879/wk)
|     |     |     |     | 120(8.2%) |     | 116(8.6%) |
| --- | --- | --- | --- | --------- | --- | --------- |
$150,000–$199,999/yr($2,880–$3,839/wk)
|                          |     |     |     | 194(13%) |     | 184(14%) |
| ------------------------ | --- | --- | --- | -------- | --- | -------- |
| $200,000þ/yr($3,840þ/wk) |     |     |     | 231(16%) |     | 210(16%) |
| Don’tknow                |     |     |     | 28(1.9%) |     | 27(2.0%) |
| Prefernottosay           |     |     |     | 154(10%) |     | 138(10%) |
| PGSIscore                |     |     |     | 3(1,7)   |     | 3(1,7)   |
Number ofgamblingaccounts
| 1   |     |     |     | 264(18%) |     | 238(18%) |
| --- | --- | --- | --- | -------- | --- | -------- |
| 2   |     |     |     | 441(30%) |     | 398(30%) |
| 3   |     |     |     | 363(25%) |     | 337(25%) |
| 4   |     |     |     | 179(12%) |     | 169(13%) |
5þ
|     |     |     |     | 223(15%) |     | 207(15%) |
| --- | --- | --- | --- | -------- | --- | -------- |
Dayssincesiteregistration 1,211(510, 2,182) 1,333(694, 2,254)
| Dayssincelast | betonsite |     |     | 4(2,28) |     | 4(2,27) |
| ------------- | --------- | --- | --- | ------- | --- | ------- |
Valuespresented: continuous variables:Median (IQR);categoricalvariables: N(percentofsample).
pGender
| notreported | tooperator. |     |     |     |     |     |
| ----------- | ----------- | --- | --- | --- | --- | --- |
#Orderedfromlower
tohigherlevelsofeducation.
self-reported problem gambling via the survey. The PGSI items to indicate the absence of harm. Second, we ran our
consists of nine items assessing problem gambling behav- firstmodel(seeFig.2)withandwithoutthosewhofailedthe
finding
iours and adverse consequences of gambling (Ferris & attention check included, negligible differences in
Wynne, 2001). Respondents rate their agreement with the model performance (AUROC 5 0.748 with them excluded,
ninestatementsonascalefrom0(Never)to4(Always).Itis AUROC 5 0.752 with them included) and variable impor-
possible that some participants may have provided inaccu- tance (see Supplemental Figure S1 for the full outcomes
rate or rushed responses to the PGSI and other survey fromthismodel).HistogramsofthePGSIscoresforthetwo
questions.Whilstwedidincludeanattentioncheckearlyin samplesusedinouranalysesarepresentedinFig.1,showing
the survey in the Gambling Harm Measure (GHM) (par- noclearabnormalitiesindistribution(e.g.,largenumbersof
ticipants were asked to select “Yes” to the question, which people scoring the maximum value).
| for the other | GHM items | would indicate | experiencing | that |     |     |
| ------------- | --------- | -------------- | ------------ | ---- | --- | --- |
harm), we chose not to exclude participants who did not Predictor variables. Behavioural features from account
pass this for two reasons. First, 78% of those who failed the data: The operator provided account data for all 24,879
GHM attention check scored 0 on all items of the GHM, customers invited to the survey for a period spanning six
suggesting that they defaulted to responding “No” to all months before and after the survey. Account data included
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

Journal of Behavioral Addictions 5
Fig.1.PGSItotalscoredistributionforthetwosamples
Note:PanelA:TotalPGSIscoredistributionforthefullsample(N5 1,470).PanelB:TotalPGSIscoredistributionforthesmaller
subsample withsixmonthsofbettinghistory(N51,349).
Fig.2. ClassificationperformanceandvariableimportanceforoptimalPhase1model(30-daywindowusingonlyaccount-basedfeatures)
Note:PanelA:Confusion matrixshowingthemodel-predicted versusactualratesofconsumersineachPGSIclassification. PanelB:
ReceiverOperatingCharacteristic Curveshowing therelationshipbetweensensitivity(truepositiverate)and 1-specificity(falsepositive
rate)acrossdecisioncut-offs.PanelC:Top20mostimportantvariablesusedbythemodeltomakeitsclassifications.PanelD:Precision-
recallcurveshowingtherelationshipbetweenprecision(i.e.,proportionofthosepredictedtobeapositiveclasswhoaretrulyat-risk)and
recall(i.e.,sensitivity, ortruepositiverate)across decisioncut-offs.
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

| 6   |     |     |     |     |     |     |     |     | Journal | of Behavioral |     | Addictions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ---------- |
all bets and transactions (i.e., deposits and withdrawals) low-incomeearners).Alowscoreindicatesrelativelygreater
made,aswellasdemographicdetails(i.e.,age,sex,postcode, disadvantage and a lack of advantage in general. As IRSAD
and account registration date), and engagement with con- scoresaredeterminedusingpostcodes,eachparticipantmay
sumer protection tools (CPTs, e.g., deposit limits, self- vary from this summary score.3
exclusion) for an extended timeframe covering two years Other betting accounts: The survey included the
before survey invitation (allowing assessment of CPTs set followingquestion:“Includingthisaccount,howmanyonline
months?”
before our six-month pre-survey window). gambling accounts have you used in the past 12
5þ).
Weengineeredmultiplefeatures(variables)summarising (response options: 1, 2, 3, 4, and Responses were
participants’ gambling behaviour over the 30 days and six converted to a continuous variable (1–5) to reflect each
participant’s
monthsprecedingthedatetheycompletedthesurvey,which number of active accounts.
were usedas predictors in our models. For example, for the Estimations of gambling expenditure: Five questions
30-daypre-surveywindow,featuressuchastotalnumberof asked participants about their past-30-day expenditure with
bets placed, total number of betting days, and deposit in- their respective site, including net outcome (total amount
tensity (i.e., deposits per active betting day) were computed won/lost), spend (total amount staked on bets), win (total
person’s
using each past-30-day data. The same features amount won on bets), deposit, and withdrawal amounts
were computed for the six-month pre-survey window, with (e.g.,“Approximately,howmuchmoneydidyoudepositwith
the addition of monthly average variables (e.g., average [site name] over the last 30 days?”). We computed partici-
pants’
monthlynetoutcome,averagemonthlynumberofdeposits) actual past-30-day values to compare with their
alongside six-month aggregate variables (e.g., overall net estimates. “Percentage discrepancy” variables were engi-
outcome, total number of bets placed). We aimed to neered to represent the difference between estimated and
generatefeaturesthatachievedoneorbothofthefollowing: actual values as a percentage of the actual value (e.g., a
[1]capture thegeneralgamblingprofileofparticipants;and participant who estimated that they deposited $50 but
reflect
[2] the features most predictive of risk status in actually deposi(cid:1)ted$75(cid:3)wouldhave apercentage discrepancy
| similar | studies | (e.g., maximum | number |     | of bets | placed in a |     |       |        |     |     |     |
| ------- | ------- | -------------- | ------ | --- | ------- | ----------- | --- | ----- | ------ | --- | --- | --- |
|         |         |                |        |     |         |             |     | 75−50 | 3100). |     |     |     |
value of 50%;
| singleday,averagenumberofdepositsinaday;Murchetal., |     |     |     |     |     |     |     | 50  |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2023; Perrot et al., 2022). Life and gambling satisfaction: Modelled on a single
| Income | and | related features: |     | Pre-tax | household | income |              |         |              |      |     |            |
| ------ | --- | ----------------- | --- | ------- | --------- | ------ | ------------ | ------- | ------------ | ---- | --- | ---------- |
|        |     |                   |     |         |           |        | item measure | of life | satisfaction | from | the | Household, |
was assessed via a single question in the survey that pre- Income and Labour Dynamics in Australia survey (HILDA;
sented income brackets to select (e.g., $60,000–$79,999 per Ambrey & Fleming, 2014) “How satisfied are you with your
year). We took the middle value within each bracket to life,allthingsconsidered?”,wedevelopedasinglequestionto
representannualincome(e.g.,“$80,000–$99,999/yr”became
|            |           |        |        |      |      |             | assess gambling | satisfaction: |     | “How satisfied | are  | you with   |
| ---------- | --------- | ------ | ------ | ---- | ---- | ----------- | --------------- | ------------- | --- | -------------- | ---- | ---------- |
| $90,000).2 | Estimated | income | values | were | used | to engineer | gambling?”      |               |     |                |      |            |
|            |           |        |        |      |      |             | your            | (recorded     |     | on a scale     | from | 0 [totally |
toparticipants’percentageofincome
features relating spent dissatisfied with my gambling] to 10 [totally satisfied with
| on bets    | (i.e., staked) | and     | deposited | into  | their accounts. |          | my gambling]). |     |     |     |     |     |
| ---------- | -------------- | ------- | --------- | ----- | --------------- | -------- | -------------- | --- | --- | --- | --- | --- |
| Employment |                | status: | Assessed  | using | a survey        | question |                |     |     |     |     |     |
“Employed”
| with response    |           | options    | dichotomised |           | into         |              | Statistical | analysis   |          |               |     |         |
| ---------------- | --------- | ---------- | ------------ | --------- | ------------ | ------------ | ----------- | ---------- | -------- | ------------- | --- | ------- |
| (including       | responses | indicating |              | part-time | and          | casual posi- |             |            |          |               |     |         |
|                  |           |            |              |           | “Unemployed” |              | Overall     | design. We | employed | a three-phase |     | machine |
| tions, full-time |           | study, and | retirement)  |           | and          |              |             |            |          |               |     |         |
“tidymodels”
(including responses indicating no current employment or learning approach using the (Kuhn & Wick-
being principally engaged in domestic duties). ham, 2020) framework in R (version 4.4.2; R Core Team,
Socio-economic status: We used customer postcodes 2024).Allanalysiscodeisavailablehere:https://github.com/
provided by the operator to determine each person’s Index Sydney-Informatics-Hub/Wagering-2025/. Our analysis
|             |                |     |           |     |     |              | utilised | two distinct | datasets | filtered to | keep | only partici- |
| ----------- | -------------- | --- | --------- | --- | --- | ------------ | -------- | ------------ | -------- | ----------- | ---- | ------------- |
| of Relative | Socio-economic |     | Advantage |     | and | Disadvantage |          |              |          |             |      |               |
(IRSAD) score. IRSAD scores are computed by the pants with complete survey data: a 30-day dataset
Australian Bureau of Statistics (ABS, 2023) and summarise comprising 1,470 participants and a six-month dataset
|             |       |            |     |          |            |     | containing | 1,349 participants, |     | with the | difference | reflecting |
| ----------- | ----- | ---------- | --- | -------- | ---------- | --- | ---------- | ------------------- | --- | -------- | ---------- | ---------- |
| information | about | the social | and | economic | conditions | of  |            |                     |     |          |            |            |
people and households in an area, including both relative the availability of extended historical data. Risk status was
determinedusingthePGSI,withthreeclassificationschemes
| advantage | (e.g., | % employed | as  | professionals; |     | % of high- |     |     |     |     |     |     |
| --------- | ------ | ---------- | --- | -------------- | --- | ---------- | --- | --- | --- | --- | --- | --- |
incomeearners)anddisadvantage(e.g.,%unemployed;%of considered. First, a multiclass approach categorising partic-
|     |     |     |     |     |     |     | ipants into | no, low, moderate, |         | and high-risk  | groups     | (PGSI |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------ | ------- | -------------- | ---------- | ----- |
|     |     |     |     |     |     |     | scores of   | 0, 1–2, 3–7,       | and 8þ, | respectively), | consistent | with  |
2Toidentifyanappropriatevalueforparticipantswhoindicatedthattheir conventional categorisations of the measure (Ferris &
|     |     |     |     |     |     |     | Wynne, | 2001). Second, | a binary | classification |     | with a PGSI |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------------- | -------- | -------------- | --- | ----------- |
incomewasinthehighestbracketofmorethan$200,000ayear,weused
AustralianBureauofStatistics(2024)censusdatatolookatthenumberof
peopleintheirincomebracketsforthoseearningabove$200,000ayear,
3Whilstthisvariablewasgeneratedfromexistingaccountdata,weconsider
| computed | the median | value for | each of | these brackets, |     | and worked out |          |     |     |     |     |         |
| -------- | ---------- | --------- | ------- | --------------- | --- | -------------- | -------- | --- | --- | --- | --- | ------- |
|          |            |           |         |                 |     |                | “survey” |     |     |     |     | defined |
whichvaluemostcloselysplitallpeopleearningmorethan200,000ayear it a feature in this study, as these variables are by the
evenly50:50(i.e.,themedian).Thisvaluewas$257,374andwasthusused inclusion of additional information not routinely used for risk detection
| astheestimatedincomevalueforthisgroup. |     |     |     |     |     |     | models. |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

| Journal of | Behavioral | Addictions |     |     |     |     |     |     |     |     | 7   |
| ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
≥5threshold(“Moderatetohigh-risk”vs.“Lowtonorisk”). approach (i.e., model and classification type) from Phase 1,
|     | classification |     |     |     | ≥8  |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Third, a binary with a PGSI threshold expanding to 62 features built from account history span-
| (“High-risk” | “Moderate |     |     | risk”). |     |     |     |     |     |     |     |
| ------------ | --------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
vs. to no Both binary classi- ning six months before the survey, including both 30-day
ficationshavebeenusedinsimilarstudiesrecently(Kairouz and six-month aggregate variables (e.g., number of betting
et al., 2023; Murch et al., 2023). days), as well as monthly averages (e.g., average monthly
|                    |     |      |                |     |            | deposit amount). | Phase | 3 further | enhanced | the feature | sets |
| ------------------ | --- | ---- | -------------- | --- | ---------- | ---------------- | ----- | --------- | -------- | ----------- | ---- |
| Model development. |     | Data | pre-processing |     | followed a |                  |       |           |          |             |      |
byintegratingsurveydatacoveringaspectssuchasgambling
5
consistentprotocolacrossallphases.Thedatasetsweresplit satisfaction and percentage of income spent (N 11
intotrainingandtestingsetsusinga70/30ratiostratifiedto [30-day]/13 [30-day þsix-month]).The data window in all
maintain class distribution of customers who had histori- phases was relative to the date each participant completed
site’s
cally been flagged by their risk detection system and thesurvey(i.e.,30daysor6monthspriortothespecificdate
those who had not. Hyperparameters were tuned using of survey completion). A summary of feature sets included
five
10-fold cross-validation repeated times. Standard pre- in models ateach phaseis presentedinTable2.Alist of all
processing steps included feature normalisation, categorical features included in models is available in Supplemental
definitions
variable encoding, handling of missing values (median Table S1, and feature are presented in
imputation for numeric variables and mode imputation for Supplemental Table S2.
categorical variables), removal of near-zero variance pre- Our primary measure of model performance was Area
dictors, and management of outliers. To address class Under the Receiver Operating Characteristic curve
imbalance in the outcome variable (where the minority to (AUROC)values,whichrepresentsoverallperformanceina
majority class ratio was less than 0.3), we implemented binaryclassificationscenario.AUROCvaluestypicallyrange
Synthetic Minority Oversampling Technique (SMOTE) to from 0.5 (no better than chance) to 1 (perfect discrimina-
generate synthetic samples of the minority class. We tion). As this was our primary outcome measure, we
| confirmed |     |     |     |     |     |     | confidence |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- |
that our models performed better (as measured computed 95% intervals for these values using
by AUROC) on test data after being trained on data sub- bootstrapping with 1,000 re-samples. We interpreted
| jected to | SMOTE | than without | its | application. |     |              |              |              |             |        | (0.50– |
| --------- | ----- | ------------ | --- | ------------ | --- | ------------ | ------------ | ------------ | ----------- | ------ | ------ |
|           |       |              |     |              |     | AUROC values | using        | conventional | guidelines: | failed |        |
|           |       |              |     |              |     |              | (0.60–0.69), |              | (0.7–0.79), |        |        |
Five distinct machine learning algorithms were consid- 0.59), poor fair/adequate good
ered: [1] Logistic Regression (using the “glm” library), (0.80–0.89),orexcellent(≥0.9)(Çorbacıo(cid:3)glu&Aksel,2023).
(“ranger”), Theperformanceofthefinalmodelsforeachphasewasalso
| [2] Random | Forest |     |     | [3] XGBoost | (extreme |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | ----------- | -------- | --- | --- | --- | --- | --- | --- |
gradient boosting; “xgboost”), [4] Decision Tree (“rpart”), assessed using sensitivity, specificity, precision, accuracy,
and [5] Neural Network (“nnet”). For model optimisation, andbalancedaccuracy([sensitivityþspecificity]/2).Finally,
space-filling
we employed a design to generate 100 hyper- we reportArea Underthe Precision-Recall Curve (AUPRC)
parameter combinations. values for our final models, consistent with the recommen-
|     |     |     |     |     |     | dations of | Marionneau | et al. | (2025). AUPRC | provides | a   |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | ------ | ------------- | -------- | --- |
Phased process of model testing and comparison. We used single-number summary of binary classification perfor-
a phased approach to test and compare model performance mance, like AUROC, but focuses on the positive class and
influenced
under different scenarios. Phase 1 considered the perfor- may therefore be less by imbalanced datasets.
| mance of            | the five | model types | for      | each of | the three classi- |     |     |     |     |     |     |
| ------------------- | -------- | ----------- | -------- | ------- | ----------------- | --- | --- | --- | --- | --- | --- |
| fication approaches |          | using 31    | features | derived | from 30-day       |     |     |     |     |     |     |
Ethics
| account data, | including | behavioural |     | metrics | such as deposit |     |     |     |     |     |     |
| ------------- | --------- | ----------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- |
frequency as well as demographic information (i.e., age and Ethics approval for this study was obtained from the
gender).Phase2focusedexclusivelyonthebest-performing University of Sydney Ethics Committee (ID: 2023/029).
|     |     |     |     |     | Table2.Feature setsincludedinmodels |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
Phase3
|     |     |     |     | Phase1 |     | Phase2 |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- |
6-monthwindow:
30-daywindow: 6-monthwindow: 30-daywindow:account account&survey data
Featureset accountdatamodel accountdatamodel &survey datamodel model
|                             |                 |     |     | ✓   |     | ✓   |     | ✓   |     | ✓   |     |
| --------------------------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Demographic                 | characteristics |     |     |     |     |     |     |     |     |     |     |
| Past30-daybettingbehaviour  |                 |     |     | ✓   |     | ✓   |     | ✓   |     | ✓   |     |
| ActiveuseofCPTs             |                 |     |     | ✓   |     | ✓   |     | ✓   |     | ✓   |     |
| Past6-monthbettingbehaviour |                 |     |     |     |     | ✓   |     |     |     | ✓   |     |
|                             |                 |     |     |     |     | ✓   |     |     |     | ✓   |     |
Past6-monthchangestoCPTs
|     |     |     |     |     |     | ✓   |     |     |     | ✓   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Average monthlybetting
| behaviour(past         | 6months) |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Surveyresponsefeatures |          |     |     |     |     |     |     | ✓   |     | ✓   |     |
| Totalno.features       |          |     |     | 31  |     | 62  |     | 42  |     | 75  |     |
5Consumer
| Note:CPT |     | protectiontool(e.g.,deposit |     |     | limit). |     |     |     |     |     |     |
| -------- | --- | --------------------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

8 Journal of Behavioral Addictions
Allparticipantsreadastudyinformationsheetandprovided sensitivity). Based on these initial assessments, we estab-
their consent before starting the survey. lished the PGSI ≥8 threshold using XGBoost as our
preferred model architecture for subsequent phases.
RESULTS Phase 2 model: expanding to six months of account
data
Phase 1 models: establishing an optimal approach
Changing the temporal framework to the preceding six
using 30 days of account data
monthsyieldedamarginalreductioninoverallperformance
(test AUROC of 0.743) but slight improvements in sensi-
We started by comparing the overall performance of the
tivity (67.5%) and specificity (72.1%). Figure 3 presents the
different model types for each of the three classification
scenarios, optimising for Youden’s J (J 5 sensitivity þ full set of results for this model.
specificity (cid:1)1), and using the 30-day account data to
develop these baseline models. The multiclass classification Phase 3 models: integration of survey responses
framework exhibited limited discriminative capacity, with
IntegrationofsurveydatainPhase3substantiallyenhanced
eventhehighest-performingmodel(decisiontree)achieving
overall performance, particularly for the 30-day model
only a test AUROC of 0.613 (Table 3). In contrast, binary
(Fig. 4), which achieved the highest overall test AUROC of
classification frameworks consistently demonstrated
0.850. Sensitivity remained at 66.2% for the 30-day model
enhanced discriminative capability, with particularly strong with added survey features, whereas specificity improved to
results for the PGSI ≥8 threshold. The binary PGSI ≥8 or
84.4%,representinga12.9%increaseoverthe30-daymodel
lower classification approach implemented through
in Phase 1. The six-month model with survey features also
XGBoost achieved the highest test AUROC (0.752).
demonstrated improved overall performance relative to the
Accordingly, more extensive outcomes for this model are
six-month model in Phase 2, with a test AUROC of 0.832
presentedinFig.2.Thismodelcorrectlyidentified66.2%of
(Fig. 5). Gains were seen in specificity, which increased by
high-risk cases (sensitivity) and 71.5% of moderate-to-no-
12.0 to 84.1%, while sensitivity decreased by 1.2 to 66.3%.
risk cases (specificity).
TheXGBoostalgorithmprovidedthebestdiscriminative
Variable importance
capacity for identifying high-risk gambling behaviour while
maintaining an appropriate balance between false positives In Phases 1 and 2, age (20.2% relative importance in the
and false negatives (see Supplemental Table S3 for model optimal 30-day model; 9.5% in the six-month model), de-
parameters when using alternative optimisation metrics for posit intensity (9.9%; 29.3%), average stake size (10.3%;
model selection other than Youden’s J index; e.g., AUROC, 11.2%), and the number of days since placing a bet (10.8%;
Table3.Comparisonofclassificationapproaches
Cross-validation metrics Testsetperformance Modelstability
Model AUROC Std.Error AUROC Accuracy ROCΔ ROCstability
Classification:multi-class PGSIgroupings
Decisiontree 0.628 0.005 0.613 0.317 0.014 0.008
XGBoost 0.663 0.004 0.610 0.305 0.054 0.007
Multinomialregression 0.643 0.004 0.601 0.333 0.042 0.007
RandomForest 0.656 0.005 0.595 0.319 0.061 0.007
Neuralnetwork 0.611 0.005 0.570 0.290 0.042 0.008
Classification:PGSI≥5
Logisticregression 0.701 0.006 0.678 0.688 0.023 0.009
RandomForest 0.723 0.007 0.669 0.683 0.054 0.009
XGBoost 0.707 0.007 0.652 0.686 0.055 0.009
Neuralnetwork 0.653 0.007 0.647 0.654 0.006 0.011
Decisiontree 0.652 0.008 0.639 0.672 0.013 0.012
Classification:PGSI≥8
XGBoost 0.719 0.008 0.752 0.706 0.033 0.011
RandomForest 0.700 0.008 0.705 0.756 0.006 0.011
Decisiontree 0.652 0.010 0.704 0.686 0.052 0.016
Logisticregression 0.673 0.008 0.697 0.654 0.023 0.012
Neuralnetwork 0.645 0.009 0.650 0.670 0.005 0.014
Note:AUROC5AreaUndertheReceiverOperatingCharacteristicCurve;StdError5standarderrorofthemeanAUROCachievedin
cross-validationfolds;Accuracy5percentageoftotalcasescorrectlyclassified;ROCΔ:Absolutedifferencebetweencross-validationand
testsetAUROC;ROC stability5 StabilityofROCacrossfolds.The emboldenedrowrepresentsthebest-performing model.
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

Journal of Behavioral Addictions 9
Fig.3. Classificationperformance and variableimportanceforPhase2model (six-monthwindowusingonlyaccount-basedfeatures)
Note:PanelA:Confusion matrixshowingthemodel-predicted versusactualratesofconsumersineachPGSIclassification. PanelB:
ReceiverOperatingCharacteristic Curveshowing therelationshipbetweensensitivity(truepositiverate)and 1-specificity(falsepositive
rate)acrossdecisioncut-offs.PanelC:Top20mostimportantvariablesusedbythemodeltomakeitsclassifications.PanelD:Precision-
recallcurveshowingtherelationshipbetweenprecision(i.e.,proportionofthosepredictedtobeapositiveclasswhoaretrulyat-risk)and
recall(i.e.,sensitivity,ortruepositiverate)acrossdecisioncut-offs.“6m”5featurebasedonsix-monthwindowprecedingparticipation;
“30d”5featurebased on30-daywindowprecedingparticipation.
4.9%)servedaskeypredictors(Figs2Cand3C).InPhase3, building a series of models that systematically integrated or
gambling satisfaction emerged as the primary predictor excluded these features to determine their relative value in
(32.2%inthe30-daymodel;40.2%inthesix-monthmodel) improvingclassificationperformance,plottingROCandpreci-
in both temporal frameworks (Figs 4C and 5C). Other top sion-recallcurvesforeachmodel(Fig.6).AUROCwashighest
predictors in Phase 3 models included the number of active whenbothsurveyvariableswereincorporatedintoabasemodel
gamblingaccounts(12.0%;9.0%)andthedifferencebetween withaccountfeaturesfromthe30-dayhistory,andAUPRCwas
estimatedandactualwithdrawal(4.5%;7.9%),deposit(4.6%; highest when only gambling satisfaction was added (see
2.3%), and net outcome (3.2%; 2.6%) amounts. SupplementalFiguresS2–4forfullmodeloutcomes).
Phase 4 models: incremental gains from select survey Overall model comparison
features
Table 4 compares the performance metrics of models from
Giventhepredominanceoftwoself-reportvariablesinPhase3 allfourphases,demonstratingsuperiorperformanceamong
models—gamblingsatisfactionandnumberofactivegambling the Phase 3 and 4 models that combined account data with
accounts—we conducted a fourth exploratory analysis phase, varying numbers of survey features.
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

| 10  |     |     |     |     |     |     |     |     |     | Journal | of Behavioral | Addictions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ---------- | --- |
4.Classificationperformance
Fig. andvariableimportance forPhase3model (30-daywindowcombiningaccount-and survey-based
features)
Note: PanelA:Confusionmatrix showingthemodel-predicted versusactualratesofconsumers ineachPGSIclassification. PanelB:
ReceiverOperatingCharacteristic Curveshowingtherelationship betweensensitivity(truepositiverate)and1-specificity(falsepositive
rate)acrossdecisioncut-offs.PanelC:Top20mostimportantvariablesusedbythemodeltomakeitsclassifications.PanelD:Precision-
recallcurveshowingtherelationshipbetweenprecision(i.e.,proportionofthosepredictedtobeapositiveclasswhoaretrulyat-risk)and
|     |     |     | recall(i.e.,sensitivity, |     |     | ortruepositiverate)acrossdecisioncut-offs. |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------ | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
DISCUSSION ensure adequate sensitivity (i.e., detection of high-risk
|             |          |                       |          |          |        |          | customers; |       | Murch et    | al., 2023).  |        |            |          |
| ----------- | -------- | --------------------- | -------- | -------- | ------ | -------- | ---------- | ----- | ----------- | ------------ | ------ | ---------- | -------- |
|             |          |                       |          |          |        |          |            | Model | performance | was stronger | when   | predicting | PGSI     |
| Our machine | learning | models                | achieved | adequate |        | to good  |            |       |             |              |        |            |          |
|             |          |                       |          |          |        |          | scores     | of    | ≥8 compared | to scores    | of ≥5, | consistent | with the |
| performance | in       | correctly classifying | online   |          | sports | and race |            |       |             |              |        |            |          |
≥8thresholdreflectingamoredistinctandseveresymptom
| betting customers |       | into higher-      | and         | lower-risk  | PGSI        | cate- | profile |          |            |                 |        |             |        |
| ----------------- | ----- | ----------------- | ----------- | ----------- | ----------- | ----- | ------- | -------- | ---------- | --------------- | ------ | ----------- | ------ |
|                   |       |                   |             |             | findings).  |       |         | (Currie, | Hodgins,   | & Casey,        | 2013). | Kairouz     | et al. |
| gories (see       | Table | 5 for a           | lay-summary | of          |             | The   |         |          |            |                 |        |             |        |
|                   |       |                   |             |             |             |       | (2023)  | found    | marginally | improved        | model  | performance | for    |
| models we         | built | showed reasonable |             | sensitivity | (66.2–75.6) |       |         |          |            |                 |        |             |        |
|                   |       |                   |             |             |             |       |         | ≥8       | ≥5         | classification, |        |             |        |
specificity (71.5–84.4), (32.9–50.5). the over the although Murch et al.
and but poor precision (2023)foundtheconverse.Overall,ourfindingsandthoseof
| This is similar | to  | previous        | studies that | have       | used | a compa- |          |      |                  |            |         |            |            |
| --------------- | --- | --------------- | ------------ | ---------- | ---- | -------- | -------- | ---- | ---------------- | ---------- | ------- | ---------- | ---------- |
|                 |     |                 |              |            |      |          | previous |      | studies (Kairouz | et al.,    | 2023;   | Murch et   | al., 2023) |
| rable design    | to  | ours (precision | rates:       | 29.5–49.6; |      | Kairouz  |          |      |                  |            |         |            |            |
|                 |     |                 |              |            |      |          | indicate | that | these            | models can | perform | adequately | across     |
etal.,2023;Murchetal.,2023).Inthisstudy,precisionrefers
|     |     |     |     |     |     |     | different |     | risk thresholds. | In applied | settings, | the | choice of |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------------- | ---------- | --------- | --- | --------- |
totheproportionofcustomerspredictedtobehigh-riskwho
define
|            |             | ≥8.        |              |            |           |          | how           | to        | the high-risk | group   | may  | be better         | guided by |
| ---------- | ----------- | ---------- | ------------ | ---------- | --------- | -------- | ------------- | --------- | ------------- | ------- | ---- | ----------------- | --------- |
| reported   | PGSI scores | Thus,      | a large      | proportion |           | of those |               |           |               |         |      |                   |           |
|            |             |            |              |            |           |          | risk          | detection | preferences,  | rather  | than | model performance |           |
| flagged by | these       | models for | intervention | may        | not       | be truly |               |           |               |         |      |                   |           |
|            |             |            |              |            |           |          | optimisation. |           | Selecting     | a lower | PGSI | cut-off           | may be    |
| high-risk, | although    | this may   | be a         | necessary  | trade-off | to       |               |           |               |         |      |                   |           |
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

Journal of Behavioral Addictions 11
Fig. 5.Classificationperformance andvariableimportance forPhase3model(six-monthwindowcombiningaccount-andsurvey-based
features)
Note:PanelA:Confusion matrixshowingthemodel-predicted versusactualratesofconsumersineachPGSIclassification. PanelB:
ReceiverOperatingCharacteristic Curveshowing therelationshipbetweensensitivity(truepositiverate)and 1-specificity(falsepositive
rate)acrossdecisioncut-offs.PanelC:Top20mostimportantvariablesusedbythemodeltomakeitsclassifications.PanelD:Precision-
recallcurveshowingtherelationshipbetweenprecision(i.e.,proportionofthosepredictedtobeapositiveclasswhoaretrulyat-risk)and
recall(i.e.,sensitivity, ortruepositiverate)across decisioncut-offs. 6m5variable basedonsix-monthwindowprecedingparticipation;
30d5variablebased on30-daywindowprecedingparticipation.
preferred when emphasising the early detection of poten- scenarios (Bentéjac, Csörgő, & Martínez-Muñoz, 2021).
tially at-risk individuals, whilst using a higher cut-off may Gambling researchers should consider XGBoost and other
reflect a preference for reducing misclassifications of those gradient-boosted models in future risk detection studies.
not experiencing problems. Adequate classification was achieved using only 30 days
Amongthemodelswetested,XGBoostachievedthebest of data, and longer account histories (six months) did not
classification accuracy. To our knowledge, our study is the meaningfully improve model performance. This is consis-
first to include XGBoost when predicting self-reported tentwithAnderssonetal.(2025),whofoundmodelstrained
problemgambling(butnotVSE),with prior studies finding on 30,60, and90daysof data performed similarly.The 30-
Random Forest performs best in this context (Auer & day models inourstudyappearedtoprovidelargely similar
Griffiths,2022;Hopfgartneretal.,2024;Kairouzetal.,2023; sensitivity and specificity, but lower precision (i.e., lower
Murch et al., 2023; Perrot et al., 2022). Outside of the proportionsofthosepredictedtobeat-riskwhoaretrulyat-
gamblingfield,XGBoostmodelshavebeenfoundtoachieve risk)thansix-monthmodels.Itisimportanttonotethatthe
good to excellent accuracy in different classification 30-daydatausedinthisstudywasnotnecessarilythefirst30
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

| 12  |     |     |     |     |     |     | Journal | of Behavioral | Addictions |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | ---------- | --- |
Fig.6.Comparison ofmodelsincluding orexcludinghighlypredictive surveyvariables(Phase 4)
Note:Outcomesforfourseparatemodelsarepresentedinbothpanels,includingabaselinemodelusingonlypast-30-dayaccountdata,the
baselinemodelplusthegamblingsatisfactionvariable,thebaselinemodelplusthenumberofaccountsvariable,andthebaselinemodelplus
bothsurveyvariables.PanelA:ReceiverOperatingCharacteristicCurveplotshowingtherelationshipbetweensensitivity(truepositiverate)
and1-specificity(falsepositiverate)acrossdecisioncut-offsforeachmodel.PanelB:Precision-recallcurveplotshowingtherelationship
between precision(i.e., proportionofthosepredictedtobeinthepositiveclasswhoaretrulyat-risk) andrecall(i.e.,sensitivity, ortrue
|     |     |     | positiverate)across     | decisioncut-offsforeachmodel. |            |     |     |     |     |     |
| --- | --- | --- | ----------------------- | ----------------------------- | ---------- | --- | --- | --- | --- | --- |
|     |     |     | Table4.Modelperformance |                               | comparison |     |     |     |     |     |
AUROC
Model [95%CIs] AUPRC Sensitivity Specificity Precision Accuracy Balancedaccuracy
Phase1
30days-accountfeatures 0.752 0.376 66.23 71.51 32.90 70.59 68.87
[0.692,0.808]
Phase2
6months-accountfeatures 0.743 0.382 67.50 72.09 37.24 71.18 69.80
[0.690,0.796]
Phase3
30days-account&survey features 0.850 0.562 66.22 84.38 47.22 81.22 75.31
[0.805,0.888]
50.48
6months-account&survey features 0.832 0.509 66.25 84.05 80.54 75.15
[0.790,0.874]
Phase4
30days-account&gambling 0.837 0.608 72.73 77.53 40.60 76.70 75.13
| satisfaction |     |     | [0.781,0.883] |     |     |     |     |     |     |     |
| ------------ | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
30days-account&no.accounts 0.758 0.359 64.94 74.79 35.21 73.08 69.87
[0.704,0.815]
|                           |     |      | 0.850 |       | 75.64 |       |       |       | 77.96 |     |
| ------------------------- | --- | ---- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | --- |
| 30days-account&bothsurvey |     | vars |       | 0.596 |       | 80.27 | 45.04 | 79.46 |       |     |
[0.802,0.897]
Note:AUROC5Areaunderthereceiveroperatingcharacteristiccurve;CIs5ConfidenceIntervals;AUPRC5Areaundertheprecision
recallcurve;Sensitivity5Percentageofat-riskparticipantspredictedtobeat-riskbythemodel(truepositiverate);Specificity5Percentage
ofnot-at-riskparticipantspredictedtobenot-at-riskbythemodel(truenegativerate);Precision5Percentageofparticipantspredictedto
|                                                       |                               |     | Accuracy5Totalpercentage |                      |                   |             | correctlyclassified;Balancedaccuracy |             |               | 5   |
| ----------------------------------------------------- | ----------------------------- | --- | ------------------------ | -------------------- | ----------------- | ----------- | ------------------------------------ | ----------- | ------------- | --- |
| beat-riskbythemodelwhoweretrulyat-risk;               |                               |     |                          |                      | ofallparticipants |             |                                      |             |               |     |
| Meanofsensitivityand                                  | specificity;Emboldenedvalues5 |     |                          | highestrateachieved. |                   |             |                                      |             |               |     |
| daysofsomeone’saccounthistory;nonetheless,ourfindings |                               |     |                          |                      |                   |             |                                      | first       |               |     |
|                                                       |                               |     |                          |                      | models            | built using | data from                            | the 30 days | after account |     |
indicate risk-detection efforts can begin early after registration, or even shorter periods, can achieve adequate
| registration. | Future research | should | determine | whether | performance. |     |     |     |     |     |
| ------------- | --------------- | ------ | --------- | ------- | ------------ | --- | --- | --- | --- | --- |
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

Journal of Behavioral Addictions 13
Table5.Summaryofkeyfindings
(cid:3) Machinelearningmodelsarecomputer-basedalgorithmsthatcananalyselargeamountsofdatatofindpatternsandmakepredictions.
(cid:3) We aimedtodetermine whetherthese modelscouldbeused toidentify onlinesportsandracebettingcustomers withself-reported
gambling problems(PGSI scores≥5and≥8) usingbehaviouraltrackingdatathatisroutinelycollectedbybettingsites.
(cid:3) ThemodelsdistinguishedbetweencustomerriskgroupsbetterwhenweusedPGSIscores≥8todefinethehigh-riskgroup(comparedto
whenusing scores≥5).
(cid:3) Accuracy:Thesemodelswereabletocorrectlyclassify71-81%ofallcustomersaccordingtotheiractualstatusaseitherno-to-moderate-
risk(PGSI <8)orhigh-risk(PGSI ≥8).
(cid:3) Sensitivity:65–76%ofhigh-riskcustomers werecorrectlyclassified ashigh-riskbythemodelswe tested,meaning24-35%wereincor-
rectly classifiedasno-to-moderate-risk customers.
(cid:3) Specificity:71–84%ofno-to-moderate-riskcustomerswerecorrectlyclassifiedassuchbythemodelswetested,meaning16–29%were
incorrectly classified ashigh-riskcustomers.
(cid:3) Precision: only33–50%ofthosepredictedtobehigh-riskbyourmodelsweretrulyhigh-risk(i.e.,PGSI≥8).
(cid:3) We builtmodelsusingeither 30daysorsix monthsofcustomers’behaviouralaccountdataand foundthey performedsimilarly, sug-
gesting extendedperiodsofhistorical dataarenotneededtousethese modelsandtheycanbe implementedsoonafterregistration.
(cid:3) The account-basedvariablesmostpredictive ofriskstatus wereyoung age,highdepositintensity (definedastheaveragenumberof
depositsper activebettingdate),highaveragestakesize, andfewerdayssincelastplacing abet.
(cid:3) Whenweintegratedresponses fromacustomersurvey,themodels’abilitytoaccuratelyclassifycustomers substantiallyimproved.
(cid:3) Theself-reportvariablesmostpredictiveofriskstatusweregamblingsatisfactionandthenumberofonlinegamblingaccountssomeone
held.
(cid:3) The bestmodel webuilt(seeFigure4)combined30daysofbehaviouralaccountdatawith self-reportvariables.
One of the most novel findings from this study was the transactions across gambling sites irrespective of their
substantial performance improvements achieved by inte- paymentmethodislikelytobemosteffectiveatidentifying
grating survey variables into models. Our best performing and supporting high-risk consumers; this could be devel-
model combined 30-day account data and survey variables, oped by regulators, financial institutions, or trusted third
suggesting self-reports and recent behaviour may act syn- parties using account data, ideally in real-time (Swanton,
ergistically to predict problem gambling. We observed Gainsbury, & Blaszczynski, 2019).
meaningful improvements by adding just two survey vari- Finally, because both the survey predictors and PGSI
ables to models in isolation or combination: gambling scores rely on self-report, any individual differences in
satisfaction and the number of active wagering accounts. response styles will influence both sets of measures in a
Gambling satisfaction was strongly predictive of problem correlated way. This shared method variance can artificially
gambling risk status, with lower scores observed among inflate the association between survey predictors and the
higher-risk customers. This novel variable is likely less outcome, a problem referred to as “common method bias”
biasedthandirectlyaskingcustomersabouttheirexperience (Kock, Berbekova, & Assaf, 2021). A second and related
of gambling harms as people may deny and/or fail to reasonisthatthetimingofcollectionwasidentical,meaning
recognise these. We recommend further research to explore participants’ current emotional state and recent gambling
the concept of gambling satisfaction and its value as an in- experiences could affect all their survey responses simulta-
dicator of risk. neously. For example, dissatisfaction with recent gambling
Thereareseveralreasonswhyself-reporteddatamaybe outcomes might lead someone to endorse more PGSI items
morepredictive ofrisk than account-based variables.First, and report lower gambling satisfaction. These issues high-
the relationship between time or money spent gambling light the need for future research to confirm the predictive
and the perceived sense of problems may be complex and ability of key self-report variables identified here with other
variable. There is likely variation between individuals in possiblemeasuresofrisk(e.g.,reportsfromoperatorcontact
[1]thenumberofinternalandexternal resources available withcustomers)andtoseparatethetimingofpredictorand
to help them manage the impact of their gambling, and outcome measurement.
[2]theirinterpretationoftheimpactgamblingishavingon Our findings should be viewed in the context of some
them. Second, account-based variables only capture limitations. We considered account data from only two
behaviour on one site. Survey-based variables, by com- sitesandwereunabletotrackgamblingbeyondthesingle
parison, can reflect a person’s entire experience with site each customer was registered with. As our outcomes
gambling.Thisexplanationissupportedbyourfindingthat demonstrate, high-risk individuals are more likely to
the number of active online gambling accounts someone gamble with multiple sites (see also: The UK Behavioural
held provided a strong signal for differentiating risk Insights Team, 2021). We attempted to address this by
groups. A single customer view of gambling using bank or capturing the number of other sites recently gambled
digital wallet records could provide a complete picture of with, but this is unlikely to fully reflect the extent and
consumption across sites and has demonstrated value in a variationofgamblingacrossothersites.Second,whilstwe
UK-based study of open banking data (Zendle & Newall, obtained a moderately large sample (N 5 1,349–1,470),
2024). A dedicated service that can track individuals’ similar studies in the field have obtained sample sizes
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

| 14  |     |     |     |     |     |     |     |     |     | Journal | of Behavioral |     | Addictions |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------- | --- | ---------- | --- |
ranging from 5,404 (Perrot et al., 2022) to 14,261 part of the Gambling Research Capacity Grant program,
(Luquiens et al., 2016), potentially enhancing the repre- administeredbytheOfficeofResponsibleGambling(ORG).
Bally’s
sentativeness of their datasets. However, unlike prior Entain, ICRG, Corporation, and the NSW ORG
studies, our survey was extensive and burdensome for didnothaveanyinputintotheresearchquestion(s),design,
dataanalysis,orinterpretationoffindingsofthisstudy.The
| participants, | including |     | the | PGSI alongside |     | measures of |     |     |     |     |     |     |     |     |
| ------------- | --------- | --- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
estimated expenditure, demographic characteristics, firstversionofthisarticlewasprovidedtoEntaininadvance
gambling satisfaction, and several other constructs not of submission to the journal, but Entain was unable to
central to the present analyses. Sample size concerns request changes to this work or preclude dissemination of
| in this type  | of      | research | highlight |        | a limitation | of using         | any findings. |     |     |     |     |     |     |     |
| ------------- | ------- | -------- | --------- | ------ | ------------ | ---------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| self-reported | problem |          | gambling  | scores | as           | the target vari- |               |     |     |     |     |     |     |     |
Authors’
able. While VSE has limitations in this context that are contribution: RMH: conceptualization (lead), data
discussed above (e.g., heterogeneous motivations for curation (lead), formal analysis, funding acquisition, inves-
|                  |     |       |           |           |     |               | tigation | (lead), | methodology |     | (lead), project |     | administration, |     |
| ---------------- | --- | ----- | --------- | --------- | --- | ------------- | -------- | ------- | ----------- | --- | --------------- | --- | --------------- | --- |
| self-excluding), |     | it is | routinely | available | in  | operator data |          |         |             |     |                 |     |                 |     |
without the need to encourage customers to complete a visualisation, writing - original draft (lead), and writing -
|                |     |                    |     |     |            |          | review & | editing | (lead). | EZ: | formal analysis |     | (lead), | visual- |
| -------------- | --- | ------------------ | --- | --- | ---------- | -------- | -------- | ------- | ------- | --- | --------------- | --- | ------- | ------- |
| survey. Sample |     | representativeness |     |     | is another | concern. |          |         |         |     |                 |     |         |         |
In a separate analysis of the dataset used here, our team isation(lead),writing-originaldraft,andwriting-review&
was able to determine that the sample used in this study editing.DV:conceptualisation,formalanalysis,andwriting-
|     |     |     |     |     |     |     | review & | editing. | CTdL: | formal | analysis, | writing | -   | original |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ----- | ------ | --------- | ------- | --- | -------- |
wasnotfullyrepresentativeofthewidercustomerbase,as
more engaged bettors self-selected into the survey (Heir- draft, and writing - review & editing. EH: writing - original
|             |        |      |                  |     |     |              | draft, and | writing | - review | &   | editing. | SMG: | conceptualisa- |     |
| ----------- | ------ | ---- | ---------------- | --- | --- | ------------ | ---------- | ------- | -------- | --- | -------- | ---- | -------------- | --- |
| ene et al., | 2025). | This | is unsurprising, |     | as  | more engaged |            |         |          |     |          |      |                |     |
bettors are more likely to be active and interested in tion,datacuration,fundingacquisition(lead),investigation,
completingasurveyabouttheirgambling.Futureresearch methodology, supervision, and writing - review & editing.
isneededtounderstandhowtoscalethecollectionofself-
reportmeasuresononlinesitesandensurerepresentation Conflict of interest: RH has worked on a project funded by
across activity levels. Responsible Wagering Australia (a representative body of
|           |              |     |     |             |     |     | Australian | online | wagering | operators;   |                | University | of  | Sydney,   |
| --------- | ------------ | --- | --- | ----------- | --- | --- | ---------- | ------ | -------- | ------------ | -------------- | ---------- | --- | --------- |
| Practical | implications |     | and | conclusions |     |     |            |        |          |              |                |            |     |           |
|           |              |     |     |             |     |     | 2019–2021) | and    | as an    | independent, | sub-contracted |            |     | statisti- |
Our findings suggest that machine learning models can be cal consultant for PRET Solutions Inc on a commissioned
used to identify online bettors who may be experiencing project (funded by the Australian Casino operator Crown;
|          |           |      |           |          |     |                | 2023). | RH has | received | funding | from | the | International |     |
| -------- | --------- | ---- | --------- | -------- | --- | -------------- | ------ | ------ | -------- | ------- | ---- | --- | ------------- | --- |
| gambling | problems. | They | correctly | identify |     | most customers |        |        |          |         |      |     |               |     |
who report gambling problems as high-risk, although a CenterforResponsibleGaming(ICRG);theBrainandMind
notable proportion of those flagged as being high-risk may Centre and wider University of Sydney; and the New South
notbeexperiencingproblems.Falsepositivesareacommon Wales(NSW)ResponsibleGamblingFund,administeredby
feature of these models and may be a trade-off required to the Office of Responsible Gambling (ORG).
identify most truly high-risk customers. Operators can EZ and DV have no competing interests to declare.
employthesemodelswithjust30daysofhistoricalcustomer CTdL has received funding from ZonMW, a legal entity
data, using them to inform responsive interventions. Self- created by the Dutch Government that funds healthcare
report data that are not personal, sensitive, or difficult to research. He has not received any funding to support his
provide accurately can substantially enhance model perfor- involvement in this research.
mance. Collecting information such as customers’ self-re- ELYHhasworkedonprojectsfundedthroughtheICRG,
ported gambling satisfaction and number of other accounts awarded to SG and RH.
can shift towards more person-centred approaches to risk SG has received direct and indirect funding since 2020
detection that account for individual experiences and be- through the University of Sydney from Australian Leisure
haviours across platforms. and Hospitality Group Pty Ltd, Entain Australia, Sportsbet,
|     |     |     |     |     |     |     | NSW Office | of  | ResponsibleGambling, |     |     | WestHQ, | Brain | and |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------------- | --- | --- | ------- | ----- | --- |
Fundingsources:Thecustomerdataanalysedforthisproject MindCentre,CambridgeHealthAlliance,AristocratLeisure
was provided by the online wagering operator Entain, who Limited, and ICRG. SG has received consulting funds for
also facilitated the collection of survey data (PI: Prof. providing subject matter expertise for New Zealand Crown
Gainsbury, University of Sydney, IRMA ID: 217448 Safer Counsel, NSW Liquor & Gaming Authority, New Zealand
GamblingProject).Entaindoesnotandwillnothaveaccess GamingMachineAssociation,SingaporeMinistryofHealth,
to survey responses. This research was funded in part by a Betcloud, NZ BlueCloud, UK Behavioural Insights Team,
grantfromtheInternationalCenterforResponsibleGaming KPMG, QBE, Coms Systems Limited, Advance Gaming
(ICRG), funded by Bally’s Corporation. Its contents are (NZ) Limited, GambleAware, Star Entertainment, GREO,
solely the responsibility of the author(s) and do not neces- Senet, and Norths Collective. SG has received honorarium
sarily represent the official views of the ICRG or Bally’s and/or travel costs for presentations for Cyprus National
Corporation. Betting Authority, Asian Racing Federation, Leagues Club
RHwassupportedbyapost-doctoralfellowshipfromthe Australia, Australian Cricketers Association, Star Enter-
New South Wales (NSW) Responsible Gambling Fund as tainment, CAMH, Behavioural Insights Team, National
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

| Journal of | Behavioral | Addictions |     |     |     |     |     |     |     |     |     |     |     | 15  |
| ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Council on Problem Gambling, GambleAware, GREO, Gambling Studies, 39(3), 1273–1294. https://doi.org/10.1007/
Informa,andWashingtonStateCouncil,EuropeanLotteries s10899-022-10139-1
Griffiths,
Association. SG holds unpaid appointments as an invited Auer, M., & M. D. (2023). Reasons for gambling and
member on the NSW Independent Panel on Gambling Re- problem gambling among Norwegian horse bettors: A real-
form, is the Pillar Champion for Technology and Environ- world study utilizing combining survey data and behavioral
ment for the QLD Responsible Gambling Advisory player data. International Journal of Mental Health and
740–755.
Committee, is a board member for the Asian Racing Addiction, 21(2), https://doi.org/10.1007/s11469-020-
| Federation | Council | on  | Anti-Illegal | Betting |     | and Related |     | 00442-6 |     |     |     |     |     |     |
| ---------- | ------- | --- | ------------ | ------- | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- |
Financial Crime. SG receives an honorarium for her role as Auer,M.,&Griffiths,M.D.(2026).Differencesinonlinegambling
Co-Editor-in-ChiefforInternationalGamblingStudiesfrom expenditure between players from Germany, Spain,
Taylor & Francis. Netherlands,GreatBritain,USandCanada:Alargescaleonline
|     |     |     |     |     |     |     |     | player | tracking | study. | Acta Psychologica, |     | 266, 106864. | https:// |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------ | ------------------ | --- | ------------ | -------- |
Data availability: Data used for this study arecommercially doi.org/10.1016/j.actpsy.2026.106864
sensitive and cannot be shared beyond the research team. AustralianBureauofStatistics.(2023). Socio-EconomicIndexesfor
The survey and additional methodological details can be Areas (SEIFA), Australia. ABS. https://www.abs.gov.au/
accessed here: https://osf.io/vdsmw. All analysis code has statistics/people/people-and-communities/socio-economic-
been made openly available here: https://github.com/ indexes-areas-seifa-australia/2021.
Csörgő,
Sydney-Informatics-Hub/Wagering-2025/ Bentéjac, C., A., & Martínez-Muñoz, G. (2021). A
comparativeanalysisofgradientboostingalgorithms.Artificial
1937–1967.
Acknowledgements: The authors acknowledge the technical Intelligence Review, 54(3), https://doi.org/10.1007/
assistance provided by the Sydney Informatics Hub, a Core s10462-020-09896-5
Research Facility of the University of Sydney. Bowden-Jones, H., Hook, R. W., Grant, J. E., Ioannidis, K.,
…
|               |     |      |     |     |     |     |     | Corazza, | O., Fineberg, |             | N. A., | Chamberlain, |            | S. R. (2022). |
| ------------- | --- | ---- | --- | --- | --- | --- | --- | -------- | ------------- | ----------- | ------ | ------------ | ---------- | ------------- |
|               |     |      |     |     |     |     |     | Gambling | disorder      | in the      | UK:    | Key research | priorities | and the       |
| SUPPLEMENTARY |     | DATA |     |     |     |     |     |          |               |             |        |              |            |               |
|               |     |      |     |     |     |     |     | urgent   | need for      | independent |        | research     | funding.   | The Lancet    |
321–329.
|     |     |     |     |     |     |     |     | Psychiatry, | 9(4), |     | https://doi.org/10.1016/S2215- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --- | ------------------------------ | --- | --- | --- |
0366(21)00356-4
| Supplementary | data | to  | this article | can | be found | online | at  |     |     |     |     |     |     |     |
| ------------- | ---- | --- | ------------ | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Griffiths,
https://doi.org/10.1556/2006.2025.00525. Catania, M., & M. D. (2021). Understanding online
voluntaryself-exclusioningambling:Anempiricalstudyusing
account-basedbehavioraltrackingdata.InternationalJournalof
REFERENCES EnvironmentalResearchandPublicHealth,18(4),4.https://doi.
org/10.3390/ijerph18042000
Çorbacıo(cid:3)glu,
|     |     |     |     |     |     |     |     |     | S¸.K., | & Aksel,G. | (2023). | Receiver | operating | charac- |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ------- | -------- | --------- | ------- |
ACMA.(2022).OnlinegamblinginAustralia,findingsfromthe2021 teristiccurveanalysisindiagnosticaccuracystudies:Aguideto
interpretingtheareaunderthecurvevalue.TurkishJournalof
| ACMA annual |     | consumer | survey. | Australian | Communications |     |     |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ------- | ---------- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
and Media Authority. https://www.acma.gov.au/publications/ Emergency Medicine.https://doi.org/10.4103/tjem.tjem_182_23
2022-02/report/online-gambling-australia-snapshot. Currie,S.R.,Hodgins,D.C.,&Casey,D.M.(2013).Validityofthe
Allami, Y., Hodgins, D. C., Young, M., Brunelle, N., Currie, S., problem gambling severity index interpretive categories. Jour-
Dufour,M.,…Nadeau,L.(2021).Ameta-analysisofproblem nal of Gambling Studies, 29(2), 311–327. https://doi.org/10.
1007/s10899-012-9300-6
gamblingriskfactorsinthegeneraladultpopulation.Addiction
2968–2977.
(Abingdon, England), 116(11), https://doi.org/10. Delfabbro,P.,Parke,J.,&Catania,M.(2023).Behaviouraltracking
1111/add.15449 andprofilingstudiesinvolvingobjectivedataderivedfromonline
Ambrey, C. L., & Fleming, C. M. (2014). Life satisfaction in operators:Areviewoftheevidence.JournalofGamblingStudies,
Australia:EvidencefromtenyearsoftheHILDAsurvey.Social 40(2),639–671.https://doi.org/10.1007/s10899-023-10247-6
691–714. EuropeanGaming&BettingAssociation.(2025).Gamblingmarket
| Indicators | Research, | 115(2), |     | https://doi.org/10.1007/ |     |     |     |     |     |     |     |     |     |     |
| ---------- | --------- | ------- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s11205-012-0228-0 revenue and online share by country (2023). https://www.egba.
Andersson, S., Carlbring, P., Lyon, K., Bermell, M., & Lindner, P. eu/resource-post/online-gambling-shares-of-national-
(2025). Insights into the temporal dynamics of identifying gambling-markets-in-europe/.
problem gambling on an online casino: A machine learning Ferris, J. A., & Wynne, H. J. (2001). The Canadian problem
studyonroutinelycollectedindividualaccountdata.Journalof gambling index: User manual. Canadian Centre on Substance
490–500.
| Behavioral | Addictions,14(1), |     |     | https://doi.org/10.1556/ |     |     |     | Abuse. |     |     |     |     |     |     |
| ---------- | ----------------- | --- | --- | ------------------------ | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
2006.2025.00013 Finkenwirth, S., MacDonald, K., Deng, X., Lesch, T., & Clark, L.
Griffiths,
Auer, M., & M. D. (2014). Personalised feedback in the (2020).Usingmachinelearningtopredictself-exclusionstatus
promotion of responsible gambling: A brief overview. Respon- in online gamblers on the playNow.com platform in British
sibleGambling Review,1(1), 27–36. Columbia. International Gambling Studies, 1–18. https://doi.
|     | Griffiths, |     |     |     | artificial |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Auer, M., & M. D. (2022). Using intelligence org/10.1080/14459795.2020.1832132
algorithms to predict self-reported problem gambling with ac- Forrest,D.,&McHale,G.(2022).Patternsofplay.Technicalreport
|                   |     |      |             |        |          |         |     | 2:Accountdatastage.NatCen |     |     |     | SocialResearch. |     |     |
| ----------------- | --- | ---- | ----------- | ------ | -------- | ------- | --- | ------------------------- | --- | --- | --- | --------------- | --- | --- |
| count-basedplayer |     | data | inan online | casino | setting. | Journal | of  |                           |     |     |     |                 |     |     |
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

16 Journal of Behavioral Addictions
Gainsbury,S.M.(2011).Playeraccount-basedgambling:Potentials International Journal of Mental Health and Addiction. https://
for behaviour-based research methodologies. International doi.org/10.1007/s11469-024-01312-1
Gambling Studies, 11(2), 153–171. https://doi.org/10.1080/ Kairouz, S., Costes, J.-M., Murch, W. S., Doray-Demers, P.,
14459795.2011.571217 Carrier,C.,&Eroukmanoff,V.(2023).Enablingnewstrategies
Gainsbury, S. M. (2014). Review of self-exclusion from gambling to prevent problematic online gambling: A machine learning
venues as an intervention for problem gambling. Journal of approach for identifying At-risk online gamblers in France.
Gambling Studies, 30(2), 229–251. https://doi.org/10.1007/ InternationalGamblingStudies,23(3),471–490.https://doi.org/
s10899-013-9362-0 10.1080/14459795.2022.2164042
Ghaharian, K., Abarbanel, B., Phung, D., Puranik, P., Kraus, S., Kock,F.,Berbekova,A.,&Assaf,A.G.(2021).Understandingand
Feldman, A., & Bernhard, B. (2023). Applications of data sci- managing the threat of common method bias: Detection, pre-
enceforresponsiblegambling:Ascopingreview.International ventionand control.TourismManagement,86,104330.
Gambling Studies, 23(2), 289–312. https://doi.org/10.1080/ Kuhn, M., & Wickham, H. (2020). Tidymodels: A collection of
14459795.2022.2135753 packages for modeling and machine learning using tidyverse
Greer, N., Jenkinson, R., Vandenberg, B., & Sakata, K. (2023). principles.[Computersoftware]https://www.tidymodels.org.
Regular online betting in Australia, 2022: National Gambling LaBrie, R., & Shaffer, H. J. (2011). Identifying behavioral markers of
TrendsStudy.AustralianGamblingResearchCentre,Australian disorderedinternetsportsgambling.AddictionResearch&Theory,
Institute of Family Studies. https://aifs.gov.au/all-research/ 19(1),56–65.https://doi.org/10.3109/16066359.2010.512106
research-snapshots/regular-online-betting-australia-2022. Lakew,N.,&Lindner,P.(2025).Whatdotheysaytheyaredoing?
Griffiths,M.D.,&Auer,M.(2016).Shouldvoluntaryselfexclusion Amixed-methodsanalysisofSwedishgamblingoperators’duty
bygamblersbeusedasaproxymeasureforproblemgambling? of care action plans. Harm Reduction Journal, 22(1), 196.
MOJAddictionMedicine&Therapy,2(2),1–3.https://doi.org/ https://doi.org/10.1186/s12954-025-01349-y
10.15406/mojamt.2016.2.00019 Luquiens, A., Tanguy, M. L., Benyamina, A., Lagadec, M.,
Hayer, T., & Meyer, G. (2011). Internet self-exclusion: Character- Aubin, H. J., & Reynaud, M. (2016). Tracking online poker
isticsofself-excludedgamblersandpreliminaryevidenceforits problem gamblers with player account-based gambling data
effectiveness. International Journal of Mental Health and only. International Journal of Methods in Psychiatric Research,
Addiction, 9(3), 296–307. https://doi.org/10.1007/s11469-010- 25(4),333–342.https://doi.org/10.1002/mpr.1510
9288-z Marionneau,V.,Ristolainen,K.,&Roukka,T.(2025).Dutyofcare,
Heirene, R. M., Cobb-Clark, D., Tymula, A., Santos, T., & data science, and gambling harm: A scoping review of risk
Gainsbury, S. M. (2025). Non-response bias in gambling sur- assessmentmodels.ComputersinHumanBehaviorReports,18,
veys. International Gambling Studies, 1–24. https://doi.org/10. 100644. https://doi.org/10.1016/j.chbr.2025.100644
1080/14459795.2025.2530106 Murch,W.S.,Kairouz,S.,Dauphinais,S.,Picard,E.,Costes,J.-M.,
Hing, N., Russell, A. M. T., Black, A., Rockloff, M., Browne, M., &French,M.(2023).Usingmachinelearningtoretrospectively
Rawat, V., … Woo, L. (2022). Gambling prevalence and predictself-reportedgamblingproblemsinQuebec.Addiction,
gambling problems amongst land-based-only, online-only and 118(8),1569–1578.https://doi.org/10.1111/add.16179
mixed-mode gamblers in Australia: A national study. Com- Percy, C., França, M., Dragi(cid:1)cević, S., & d’Avila Garcez, A. (2016).
puters in Human Behavior, 132, 107269. https://doi.org/10. Predicting online gambling self-exclusion: An analysis of the
1016/j.chb.2022.107269 performance of supervised machine learning models. Interna-
Hing, N., Smith, M., Rockloff, M., Thorne, H., Russell, A. M. T., tional Gambling Studies, 16(2), 193–210. https://doi.org/10.
Dowling,N.A.,&Breen,H.(2022).Howstructuralchangesin 1080/14459795.2016.1151913
online gambling are shaping the contemporary experiences Perrot, B., Hardouin, J. B., Thiabaud, E., Saillard, A.,
andbehavioursofonlinegamblers:Aninterviewstudy.BMC Grall-Bronnec, M., & Challet-Bouju, G. (2022). Development
Public Health, 22(1), 1620. https://doi.org/10.1186/s12889- and validation of a prediction model for online gambling
022-14019-6 problemsbasedonplayers’accountdata.JournalofBehavioral
Hing,N.,Thorne,H.,Russell,A.M.T., Newall,P.W.S.,Lole, L., Addictions, 11(3), 874–889. https://doi.org/10.1556/2006.2022.
Rockloff, M., … Tulloch, C. (2024). ‘Immediate access … 00063
everywhere you go’: A grounded theory study of how smart- RCoreTeam.(2024).R:Alanguageandenvironmentforstatistical
phone betting can facilitate harmful sports betting behaviours computing. R Foundation for Statistical Computing. https://
amongst young adults. International Journal of Mental Health www.r-project.org/
and Addiction, 22(3), 1413–1432. https://doi.org/10.1007/ Sacco, P., & Jeong, J. (2025). Assessing the risk of problem
s11469-022-00933-8 gamblingamonglotteryloyaltyprogrammembers:Amachine
Hopfgartner, N., Auer, M., Griffiths, M. D., & Helic, D. (2022). learning approach. Addictive Behaviors, 168, 108372. https://
Predictingself-exclusionamongonlinegamblers:Anempirical doi.org/10.1016/j.addbeh.2025.108372
real-world study. Journal of Gambling Studies, 39(1), 447–465. Swanton, T. B., Gainsbury, S. M., & Blaszczynski, A. (2019). The
https://doi.org/10.1007/s10899-022-10149-z role of financial institutions in gambling. International
Hopfgartner, N., Auer, M., Helic, D., & Griffiths, M. D. (2024). Gambling Studies, 19(3), 377–398. https://doi.org/10.1080/
Using artificial intelligence algorithms to predict self-reported 14459795.2019.1575450
problem gambling among online casino gamblers from TheUKBehaviouralInsightsTeam.(2021).Gamblingbehaviour:
different countries using account-based player data. What can bank transaction data tell us? The feasibility study.
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC

Journal of Behavioral Addictions 17
Part 2: Analysis of HSBC UK customer data. Behavioural UKGamblingCommission.(2023).Customerinteractionguidance
Insights Team. https://www.bi.team/blogs/dealing-new-data- forremotegamblinglicensees(FormalguidanceunderSRcode
what-bank-transactions-can-tell-us-about-gambling- provision 3.4.3). https://www.gamblingcommission.gov.uk/
behaviour/. licensees-and-businesses/guide/customer-interaction-formal-
UK Gambling Commission. (2022). Gambling commission sets guidance-for-remote-gambling-operators.
new rules on action for at risk customers. Available at: Zendle,D.,&Newall,P.(2024).Therelationshipbetweengambling
https://www.gamblingcommission.gov.uk/news/article/ behaviourandgambling-relatedharm:Adatafusionapproach
gambling-commission-sets-new-rules-on-action-for-at-risk- using open banking data. Addiction, 119(10), 1826–1835.
customers. https://doi.org/10.1111/add.16571
OpenAccessstatement.Thisisanopen-accessarticledistributedunderthetermsoftheCreativeCommonsAttribution-NonCommercial4.0InternationalLicense
(https://creativecommons.org/licenses/by-nc/4.0/),whichpermitsunrestricteduse,distribution,andreproductioninanymediumfornon-commercialpurposes,provided
theoriginalauthorandsourcearecredited,alinktotheCCLicenseisprovided,andchanges–ifany–areindicated.
Unauthenticated | Downloaded 07/01/26 08:58 AM UTC