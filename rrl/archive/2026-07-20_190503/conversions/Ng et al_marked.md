PublishedasaconferencepaperatICLR2026
| AI-BAAM: |             | AI-DRIVEN |     |      | BANK | STATEMENT |     |     | ANALYT- |
| -------- | ----------- | --------- | --- | ---- | ---- | --------- | --- | --- | ------- |
|          | ALTERNATIVE |           |     | DATA |      | MALAYSIAN |     |     | MSME    |
| ICS      | AS          |           |     |      |      | FOR       |     |     |         |
| CREDIT   | SCORING     |           |     |      |      |           |     |     |         |
ChunChetNg∗∗,ZhenHaoChu∗,JiaYuLim,
YinYinBoon,WeiZengLow&JinKhyeTan
AILens,KualaLumpur,Malaysia
chunchet.ng@ailensgroup.com
6202 rpA 6  ]TS.nif-q[  4v66061.0152:viXra
ABSTRACT
Despiteaccountingfor96.1%ofallbusinessesinMalaysia(DepartmentofStatis-
ticsMalaysia,2025),accesstofinancingremainsoneofthemostpersistentchal-
|     | lenges faced | by Micro, | Small, | and Medium |     | Enterprises | (MSMEs). |     | Newly es- |
| --- | ------------ | --------- | ------ | ---------- | --- | ----------- | -------- | --- | --------- |
tablishedbusinessesareoftenexcludedfromformalcreditmarketsastraditional
|     | underwriting | approaches | rely | heavily | on credit | bureau | data. | This study | investi- |
| --- | ------------ | ---------- | ---- | ------- | --------- | ------ | ----- | ---------- | -------- |
gatesthepotentialofbankstatementdataasanalternativedatasourceforcredit
|     | assessmenttopromotefinancialinclusioninemergingmarkets. |     |     |     |     |     |     | First,wepropose |     |
| --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --------------- | --- |
acashflow-basedunderwritingpipelinewhereweutilizebankstatementdatafor
|     | end-to-end | data extraction |     | and machine | learning | credit | scoring. | Second, | we in- |
| --- | ---------- | --------------- | --- | ----------- | -------- | ------ | -------- | ------- | ------ |
troduceanoveldatasetof611loanapplicantsfromaMalaysianconsultingfirm.
Third,wedevelopandevaluatecreditscoringmodelsbasedonapplicationinfor-
|     | mationandbanktransaction-derivedfeatures. |      |           |          |        | Empiricalresultsdemonstratethat |               |     |          |
| --- | ----------------------------------------- | ---- | --------- | -------- | ------ | ------------------------------- | ------------- | --- | -------- |
|     | incorporating                             | bank | statement | features | yields | substantial                     | improvements, |     | with our |
bestmodelachievinganAUROCof0.806onvalidationset,representinga24.6%
|     | improvement | over models |      | using application |         | information   | only. | Finally, | we will     |
| --- | ----------- | ----------- | ---- | ----------------- | ------- | ------------- | ----- | -------- | ----------- |
|     | release the | anonymized  | bank | transaction       | dataset | to facilitate |       | further  | research on |
MSMEfinancialinclusionwithinMalaysia’semergingeconomy.
1 INTRODUCTION
Financial inclusion remains a pressing challenge in emerging markets, where a significant portion
of the population lacks sufficient credit history to access formal lending. According to the Secu-
ritiesCommissionMalaysia(Malaysia,2025), MSMEsareestimatedtocontributearound60%of
Malaysia’sgrossdomesticproduct. Despitetheirsignificantcontributions, MSMEsremainunder-
servedbyfinancialinstitutionsintermsofaccesstofinancing,givingrisetoanestimatedMYR90
billionfundinggap(Corporation,2017). OnefundamentalissueisthatmanyMSMEsdonothave
lendinghistory. Traditionalcreditassessmentreliesheavilyoncreditbureaudatasuchasrepayment
history,outstandingobligations,andpastdelinquencies. Whiletraditionalcreditmodelsworkwell
forestablishedbusinesses,theyhaveshortcomingsforMSMEswiththincreditfiles. First,theyare
inherentlybackward-lookingandfocusonpastrepaymentbehaviorratherthancurrentorforward-
lookingcapacitytorepay.Second,theyoverlookreal-timefinancialsignalsoroperationaldynamics
thatcouldmoreaccuratelyreflectafirm’spresentfinancialhealth. Third,theyomitalternativeindi-
catorsofcreditworthiness,suchascashflowconsistency,receivablesandpayablespatterns,digital
transactions,andbehavioralmetricsfromdailyfinancialactivity.
On the other hand, bank statements represent an up-to-date and verifiable source of financial be-
havior that also captures income regularity, spending patterns, and cash flow stability. This study
explorestheuseofMalaysianbankstatementtransactionsasalternativedataforcreditscoringmodel
developmentandevaluatestheirpredictivevalueforMSMEs. Theobjectivesareasfollows:
• To propose a cash flow-based underwriting workflow capable of ingesting and analyzing
banktransactiondataforcreditdecisioningtonarrowtheMSMEfinancinggap.
∗Theseauthorscontributedequally.
1

PublishedasaconferencepaperatICLR2026
Figure1: Proposedend-to-endworkflowusingbankstatementtransactiondataforcreditscoring.
• Tointroducethefirst-everMalaysianbankstatementdatasetbasedonMSMEloans.
• To evaluate the performance of machine learning–based credit scoring models trained on
theproposedbankstatementtransactiondataset,andtoexaminethefeasibilityandpredic-
tivepoweroftransaction-derivedfeaturesinassessingMSMEcreditworthiness.
2 RELATED WORK
Withtherecenttechnologicaladvancementsinmachinelearningalgorithms, theresearchcommu-
nityhasrecognizedthelimitationsofexistingtraditionalcreditscoringmethods(Gote&Mendhe,
2024). SuchstudiesarecrucialforenhancingfinancialinclusionofMSMEsinemergingmarkets,
whereMSMEsareoftenthebackboneofeconomicgrowthdespitehavinglimitedaccesstofinanc-
ing(Elebe&Imediegwu,2021). Assuch,alternativedatafromnon-traditionalsourcesthatarenot
includedinstandardcreditbureaufilesarebeingusedforcreditscoring(Group,2024).
Limitations of Traditional Credit Scoring. Traditional credit scoring models used by financial
institutionsprimarilyrelyoncreditbureaudatasuchaspaymenthistory,amountofdebt,andother
indicators (Shivhare, 2024). Unfortunately, reliance on such data creates a high entry barrier for
MSMEs in emerging economies where they usually lack audited financial statements or loan ser-
vicing history required by financial institutions (Courchane & Baines, 2020; Elebe & Imediegwu,
2021). ThisleadsMSMEstobeperceivedashigh-riskapplicantsandresultsinaperpetualcycleof
financialexclusionthatseverelylimitstheirgrowthpotential(Courchane&Baines,2020). Besides,
traditionalmethodsfailtocapturerecentcashflowstatusofMSMEs,whichcanbeanaccuraterep-
resentation of financial health (Elebe & Imediegwu, 2021). A recent survey indicates that 58% of
financialinstitutionsfeellessconfidenttomakedecisionsbasedontraditionalcreditdataonly(Wat-
terson,2024). Theincreasingdissatisfactionmotivatestheurgentneedtousealternativedatafora
moreadaptiveandinclusivecreditassessment(Gote&Mendhe,2024).
CreditScoringwithAlternativeData. Inordertoovercomethelimitationsoftraditionalmethods,
creditunderwritingusingalternativedatahasemergedasanewapproach(Gote&Mendhe,2024;
Watterson,2024;Ngwenya,2024). Forinstance,mobilenetworkdataareusedforcreditscoringin
Africa(Ngwenya,2024;Gathu,2020)andbankaccounttransactionsareusedforcashflowunder-
writinginconsumerlending(Watterson,2024). Recentstudiessuggestthatincorporatingtransac-
tionaldatacanimprovepredictiveaccuracyandexpandcredittounderservedpopulations(Djeundje
etal.,2021). Forinstance,researchhasshownthatretailtransactiondatacanhelpconstructalterna-
tivecreditscores(Leeetal.,0). AstudyexaminingtwoIndianfinancialtechnology(FinTech)firms
foundthattransactionaldatafromplatformactivityworkedaswellascreditbureaudatainpredict-
ingcreditworthinessandimprovedthepredictiveaccuracywhencombinedwithbureaudata(Caire
&Vidal,2024). However,theadoptionofalternativedatainMSMElendinginMalaysiaremainsat
anearlystage,withlimitedresearchfocusfromtheindustry.
Machine Learning Models in Credit Scoring. Machine learning (ML) models have proven to
be highly effective in processing financial data to produce accurate credit scores (Bu¨cker et al.,
2022; Gunnarsson et al., 2021; Trivedi, 2020). These include statistical models like Logistic Re-
gression(LR),NaiveBayes(NB),andensemblemethodslikeRandomForest,AdaBoost,andGra-
2

PublishedasaconferencepaperatICLR2026
dientBoosting(Bu¨ckeretal.,2022;Trivedi,2020). Forexample,aRandomForestmodelachieved
the best performance on Taiwanese credit card data (Abbas & Hussein, 2024). A NB classifier
performed well on a highly imbalanced dataset from a New Zealand lender, especially when un-
declared features derived from bank statements were incorporated to supplement application form
data(Bunkeretal.,2016). GiventhepositiveimpactofMLmodelsincreditscoring,weaimtoim-
provefinancialinclusionofMalaysianMSMEsthroughproposedcashflowunderwritingworkflow.
AgenticWorkflowinCreditScoring. ThedeploymentofLargeLanguageModel(LLM)-powered
agentic systems marks a major advancement in automated credit scoring, loan approval, and cus-
tomerriskprofilingwithinfinancialservices(Okpalaetal.,2025;Ali,2025;Paleti,2024). Recent
agentic frameworks have demonstrated strong performance in complex model risk management
tasks, including credit card approval and portfolio risk modeling (Okpala et al., 2025). Beyond
these use cases, agentic workflows are transforming banking by enabling adaptive credit profiling
and predictive loan approvals, thereby improving risk assessment accuracy through bias detection
andintelligentdecisionautomation(Paleti,2024). Similarapproacheshavebeenexploredinmort-
gage lending, where machine learning-driven agents streamline underwriting and accelerate credit
evaluation (Chitturi, 2025). However, existing methods remain limited in production deployment
andlackafullygrounded,end-to-endworkflowforMSMEcreditscoring.
3 BANK STATEMENT CASH FLOW UNDERWRITING
The proposed cash flow underwriting workflow enhances traditional credit underwriting by inte-
grating bank statement-derived features into the credit decision-making process. As illustrated in
Figure1,theworkflowconsistsofsixmainmodules,eachservingadistinctpurpose. Byautomat-
ingmanualextractionandanalysistasks,itshortensturnaroundtimeandimprovesoperationaleffi-
ciencywhileexpandingcreditaccessforthin-fileMSMEswholacksufficientcreditbureauhistory.
Key Information Extraction Module. The key information extraction module employs Optical
Character Recognition (OCR) to extract essential fields from bank statements, including the bank
name,accountnumber,accountholdername,address,andstatementdate.Theseattributesarecross-
validatedacrossstatementstoensureaccuratedocumentownershipverification. Thesefieldsenable
theenginetolinkmultipleaccountsbelongingtothesamebusinessentity,providingaholisticview
ofitsfinancialactivityandcashflowacrossmultiplebankaccounts.
TransactionTableExtractionModule. Thetransactiontableextractionmodulelocalizesanddig-
itizestabulartransactiondatausingOCRandlayoutanalysis. Itidentifiestableheaders,thenmaps
rowsandcolumnstoextracttransactiondate, description, debit, credit, andbalanceamounts. Ad-
ditional pre-processing handles merged cells, page breaks, and format inconsistencies to preserve
data fidelity. The resulting structured transaction records serve as critical inputs for downstream
analyticalmodulesthatevaluatetransactionpatternsandaccount-levelcashflowdynamics.
Fraud Analysis Module. The fraud analysis module leverages Computer Vision and rule-based
techniques to detect tampered or falsified bank statements. For each document, it examines both
visual and metadata cues such as inconsistent font styles or sizes, altered layouts, metadata mis-
matches,andabnormalpixel-levelpatternsthatmayindicatedigitalediting. Oncepotentialtamper-
ingisidentified,theaffectedstatementsareautomaticallyflaggedandreturnedtobankofficersfor
manualverification. Thismoduleprovidesanadditionallayerofsecurityandassurancewithinthe
underwritingworkflow,ensuringthatonlyauthenticbankstatementsareanalyzedforcreditscoring.
NetworkAnalysisModule. Thenetworkanalysismoduleconstructstransactionnetworksfromthe
extractedtransactiondatatouncoverrelationshipsamongsendersandbeneficiariesacrossmultiple
bank accounts. Using graph-based algorithms, it maps transaction linkages to detect circular fund
flows,kitingactivities,andtransferstoblacklistedorinterrelatedentities. Thismodulealsoquanti-
fiesnetworkconnectivityandtransactiondensitytorevealabnormalmoneymovementpatternsthat
mayindicatefraudulentactivityorfinancialdistress,therebyenhancingoverallriskassessment.
CashFlowAnalysisModule. Thecashflowanalysismoduleevaluatescashflowstatusbasedon
theinflowsandoutflowsextractedfromtransactionrecords. ItthenappliesNaturalLanguagePro-
cessingtoinfertransactionintentandclassifyentriesintomeaningfulcategoriesbasedontheirde-
scriptions. Usingtheseclassifications,thismodulegroupsrelatedtransactionstoidentifyspending
andreceiptpatterns,enablingthedetectionofoutliersthatdeviatefromtypicalcashflowbehavior.
3

PublishedasaconferencepaperatICLR2026
It also computes key metrics such as average, highest, and lowest balances, quantifying cash flow
healthandprovidingpredictivefeaturesforcreditscoring.
Data&ScoringLayer(CashFlowUnderwriting). Thislayerstorestheanalyzeddataandengi-
neeredfeaturesinasecuredatabasetoensuretraceability,regulatorycompliance,andauditability.
Thestoreddataarethenpreprocessed,andfeatureselectionmethodsareappliedtoretainthemost
informative variables. Using the selected features, a predictive model is trained to estimate the
probabilityofdefaultandclassifycreditrisk.
4 BANK STATEMENT TRANSACTION DATASET
Table1: StatisticsofMSMEloanapplicationdatasets.
Split Non-Default Default Total
Train(60%) 310 56 366
Validation(40%) 208 37 245
Overall 518 93 611
Transaction data derived from bank statements represents a valuable alternative resource for cash
flow underwriting. To the best of our knowledge, no published studies have examined the use of
bankstatementdataforcreditassessmentofMSMEsinMalaysia.Incollaborationwithaconsulting
firm,weconstructedthefirstMalaysianbankstatementsdatasettoaddressthisgap.
This study adopts the Cross-Industry Standard Process for Data Mining (CRISP-DM) frame-
work(Chapmanetal.,2000)asthemethodologicalbasis. CRISP-DMisawidelyrecognizedpro-
cessmodelforsystematicFinTechstudies(Cheng,2023;Rawat,2023;daRocha&deSousaJunior,
2010)andcomprisessixmainphases,i.e.,businessunderstanding,dataunderstanding,dataprepa-
ration, modeling, evaluation, and deployment. The first phase involves evaluating bank statement
transaction data as an alternative source for MSME credit risk assessment in Malaysia. The sec-
ond phase focuses on constructing the proposed dataset of 611 MSME loan applicants. Summary
statisticsofthedatasetarepresentedinTable1.
Dataset Distribution and Preparation. The dataset is split into training (60%) and validation
(40%)setsusingstratifiedrandomsamplingtopreserveclassdistribution.Amongallapplicants,518
haveagoodcreditrecord,while93haveahistoryofdefault. Eachapplicant’srecordcontainstwo
maincomponents:applicationforminformationsubmittedduringtheloanapplicationprocess(e.g.,
demographic and business characteristics) and bank statement transaction data capturing detailed
inflowsandoutflowsoverasix-monthperiod.Thethirdphaseinvolvesdatapreparationandincludes
several key tasks: (1) cleaning and de-duplicating data to ensure consistency, (2) fixing missing
values,standardizingtransactioncategories,andvalidatingdataintegrityacrossallrecords,and(3)
derivingfeaturesandvariablesfromtransactiondata,suchasdeterminingcashflowstability,deposit
regularity,andbalancevolatility.
Dataset Masking. All personally identifiable information was anonymized prior to analysis. To
preserveconfidentiality,thefeaturesaregroupedintoapplicationinformation(7features)andbank
statementfeatures(10features). Thespecificfeaturecalculationscannotbedisclosedduetoanon-
disclosure agreement and all bank statement features are derived solely from bank statement data.
FurtherdetailsonethicaluseofdataareprovidedinSection8.
5 TRANSACTION DATA-BASED CREDIT SCORING
The fourth phase of CRISP-DM in this study employs Logistic Regression on application form
and bank transaction data derived from our dataset as the baseline credit scoring model. LR is
widelyadoptedincreditriskmodelingduetoitsinterpretability,statisticalrobustness,andcapacity
toestimatetheprobabilityofdefault(Bu¨ckeretal.,2022;Trivedi,2020;Abbas&Hussein,2024;
Bunkeretal.,2016). Toensurethatonlyinformativepredictorsareretained, featureselectionand
transformationareguidedbytheWeightofEvidence(WOE)andInformationValue(IV)framework,
which are widely used in credit risk modeling for quantifying the predictive power of individual
4

PublishedasaconferencepaperatICLR2026
variables (Ngwenya, 2024). In practice, each feature is divided into discrete intervals based on
suitable thresholds determined from the data. These bins allow the calculation of WOE and IV at
thegrouplevel,whichmakesthemeasiertointerpretwithinaLRmodel. Thefollowingnotationis
usedtoquantifythedistributionofdefaultsandnon-defaultsacrossfeaturebins:
Lety ∈ {0,1}indicatedefault(y = 1)ornon-default(y = 0)forapplicanti. Thetotalnumber
| i   |     | i   |     | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- |
ofdefaultandnon-defaultapplicantsisdefinedas:
|     |     | n        |     |     | n        |     |
| --- | --- | -------- | --- | --- | -------- | --- |
|     |     | (cid:88) |     |     | (cid:88) |     |
|     | N = | I(y =1), |     | N = | I(y =0), | (1) |
|     | b   | i        |     | g   | i        |     |
|     |     | i=1      |     |     | i=1      |     |
Furthermore,letx ij denotethevalueoffeaturej forapplicanti. Foragivenfeaturej,supposeitis
dividedintoK disjointbins{B ,...,B }; thenthecorrespondingcountswithineachbinare
|     | j   | j1  | jKj |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
definedas:
n
(cid:88) I(x )I(y
|     |     | n = | ∈B  | =1), |     |     |
| --- | --- | --- | --- | ---- | --- | --- |
|     |     | bjk | ij  | jk i |     |     |
i=1
(cid:88) n
I(x )I(y
|     |     | n gjk = | ij ∈B | jk i =0). |     | (2) |
| --- | --- | ------- | ----- | --------- | --- | --- |
i=1
Thedistributionofdefaultsandnon-defaultsineachbinis:
|     |         | n    |     |         | n    |     |
| --- | ------- | ---- | --- | ------- | ---- | --- |
|     | Dist(b) | bjk, |     | Dist(g) | gjk. |     |
|     |         | =    |     |         | =    | (3) |
|     |         | jk N |     |         | jk N |     |
|     |         | b    |     |         | g    |     |
WeightofEvidence(WOE).Firstly,wecalculatetheWOEforbinkoffeaturej using:
(cid:32) Dist(g)(cid:33)
|     |     |             |         | (cid:18) n | /N (cid:19) |     |
| --- | --- | ----------- | ------- | ---------- | ----------- | --- |
|     |     |             | jk      | gjk        | g           |     |
|     |     | WOE jk =log | =log    |            | .           | (4) |
|     |     |             | Dist(b) | n          | /N          |     |
|     |     |             | jk      | bjk        | b           |     |
A positive WOE indicates that bin B is more common among non-default cases, suggesting
|     | jk  | jk  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
lowerrisk,whereasanegativevalueindicatesahigherlikelihoodofdefault.OnceWOEiscomputed
foreachbin,theoverallpredictivestrengthoffeaturej canthenbesummarizedbyitsIV.
InformationValue(IV).Secondly,wemeasuretheIVoffeaturej byaggregatingtheWOEacross
allrespectivebins:
Kj
|     |     | (cid:16) |                 | (cid:17) |      |     |
| --- | --- | -------- | --------------- | -------- | ---- | --- |
|     |     | (cid:88) | Dist(g)−Dist(b) |          |      |     |
|     |     | IV j =   |                 | WOE      | jk . | (5) |
jk jk
k=1
AlargerIV j indicatesstrongerdiscriminatorypoweroffeaturej betweendefaultandnon-default
classes. Inthisstudy,IVservesasbothafeature-rankingcriterionandaninterpretabilitymeasure,
helpingtoidentifythemostinfluentialtransaction-levelindicatorsforcreditworthiness. Following
industrypractice(Siddiqi,2017),weadoptthecommonlyusedinterpretivethresholds: IV < 0.02
(notpredictive),0.02≤IV<0.1(weak),0.1≤IV<0.3(medium),0.3≤IV<0.5(strong),and
IV≥0.5(suspiciouslyhigh,suggestingpotentialdataleakage).
BinningofBankStatementFeatures. Specifically,weusedsupervisedmonotonicbinningtoob-
}Kj
tain{B jk forcontinuoustransaction-derivedvariables(e.g.,cashflowstability,balancevolatil-
k=1
ity) and sparse categorical variables (e.g., State/Location). Then, rare categories are grouped to
ensure that each bin contains sufficient observations of both default and non-default classes while
preserving monotonicity. Computations of WOE and IV are performed on training folds only to
avoiddataleakage.
6 EXPERIMENTS
FollowingthefifthphaseofCRISP-DM,weconductaseriesofexperimentstoevaluatetheeffec-
tiveness of the proposed cash flow underwriting workflow and the role of bank statement data in
enhancingMSMEcreditscoringperformance. Theexperimentsincludecomparativeanalyseswith
establishedmachinelearningmethodsanddetailedablationstudiesontransaction-derivedfeatures.
5

PublishedasaconferencepaperatICLR2026
6.1 IMPLEMENTATIONDETAILS
WebenchmarkthebaselineLogisticRegressionmodelagainstseveralwidelyusedmachinelearn-
ingmethods,includingRandomForest(RF)(Breiman,2001),GradientBoosting(GB)(Friedman,
2001), and AdaBoost (AB) (Schapire, 2013). All models are implemented in scikit-learn (scikit
learn,2025c;a;b;d). FortheresultsinSection6.2, modelsweretrainedwithdefaulthyperparame-
ters. In Section 6.3, hyperparameters were tuned using a randomized grid search with 50 trials to
ensure robustness. We evaluate model performance using the Area Under the Receiver Operating
CharacteristicCurve(AUROC)(Bradley,1997),whichmeasurestheabilitytodiscriminatebetween
defaultandnon-defaultcasesacrossvaryingthresholds. AnAUROCof0.5indicatesnodiscrimina-
tivepower(equivalenttorandomguessing),whereasavalueof1.0indicatesperfectdiscrimination.
Toensureinterpretabilityandsystematicanalysis,bothapplicationinformationandbankstatement
featuresaregroupedintotwocategories:
i AccountBehavior: logarithmicgrowthrateofaveragebalance,six-monthaverageaccountbal-
ance, change in 3-month minimum balance (recent), percent change in minimum balance vs
priorperiod,recent3-monthmaximumaveragebalance,anddebtrepaymentcapacity.
ii Business Demographics: business operational duration, geographic region, industry classifica-
tion(MSIC),totalboarddirectors,andminimumdirectorage.
This structured feature grouping facilitates clearer attribution of model performance to different
behavioral and demographic dimensions of MSME credit profiles. It also supports experimental
reproducibility, while respecting confidentiality constraints around proprietary feature derivations.
FurtherdetailsondeploymentandoperationalconsiderationsareprovidedinAppendixB.
6.2 QUANTITATIVERESULTS
Validation Performance. Quantitative results on the validation split are presented in Figure 2.
LogisticRegressionwithblendedfeaturesachievesthehighestvalidationAUROCof0.806,outper-
forming all ensemble methods across every feature set (GB: 0.664, RF: 0.678, AB: 0.680). This
consistentadvantageisattributabletothesmall,class-imbalancedtrainingset(310non-defaultvs.
56 default cases), where LR’s well-calibrated probabilities and lower variance outweigh the flexi-
bility of tree-based ensembles (Brown & Mues, 2012; Lessmann et al., 2015). The value of bank
statement data is evident across all algorithms. For LR, moving from application-only to bank
statement-onlyfeaturesyieldsagainof0.116AUROC(0.647→0.763),andblendingbothfeature
setsachievesafurtherimprovementto0.806,a24.6%relativegainoverapplication-only. Thispat-
ternholdsforensemblemethodsaswell,confirmingthatcashflowbehaviourcapturesdefaultrisk
dimensionsthatstaticapplicationattributesalonecannot.
Extraction Module Performance. Beyond credit scoring, we evaluate the upstream AI modules
responsible for bank statement data extraction, as their accuracy directly affects downstream fea-
ture quality. For key information extraction, we benchmark 15 OCR-GPT pipeline configurations
against our template matching approach across six Malaysian banks (Table 3 in Appendix). Our
method achieves perfect 100% exact match accuracy and Normalized Edit Distance (NED) score
acrossallfiveextractionfields(bankname,accountholder,accountnumber,address,andstatement
date),whereasthebest-performingbaseline(AzureAI4.0+GPT-4.1)reaches100%onfourfields
butdropsto94.82%onaddressextraction. Fortransactiontableextraction,weevaluate16configu-
rationsincludingrecentvision-languagemodels(Tables8and9). Ourtemplatematchingapproach
achieves the highest average matching NED of 98.08% and exact NED of 97.80% across all col-
umntypes. Theclosestcompetitor,SuryaParuchuri&Team(2025)+docTRMindee(2021)with
GPT-5-mini, attains 96.94% and 94.23% respectively. Notably, end-to-end vision models such as
olmOCR(Poznanskietal.,2025)andpaddleOCR-VL(Cuietal.,2025a)showsubstantiallylower
performanceonstructuredtableextraction, underscoringtheadvantageofspecializedpipelinede-
signsforfinancialdocuments. Thesegeneral-purposemodelsstrugglewiththehighlystructuredyet
bank-specificformattingofMalaysianbankstatements,particularlymulti-linetransactiondescrip-
tions, inconsistent date formats, and merged table cells that vary across institutions. Our template
matchingmethodsucceedsbecauseitexploitsthedeterministicandstandardizedlayoutswithineach
bank’sPDFformat,bypassingtheneedforLLMentirelyandthuseliminatingbotherrorpropaga-
tion and API dependency. Table 2 summarizes the performance of selected configurations across
6

PublishedasaconferencepaperatICLR2026
AUROC Across Algorithms, Feature Sets, and Data Splits
|     |     | Logistic Regression |     |     |     |     | Gradient Boosting |     |     |
| --- | --- | ------------------- | --- | --- | --- | --- | ----------------- | --- | --- |
1.0
|     |             | 0.821 | 0.850 | 0.806 |       |       |       |       |       |
| --- | ----------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0.8 |             | 0.763 |       |       |       |       |       |       |       |
|     |             |       |       |       |       |       | 0.705 |       | 0.720 |
|     | 0.672 0.647 |       |       |       |       |       |       |       | 0.664 |
|     |             |       |       |       | 0.578 |       |       | 0.599 |       |
| 0.6 |             |       |       |       |       | 0.519 |       |       |       |
0.4
0.2
0.0
CORUA Application Info Bank Statement Blended Application Info Bank Statement Blended
|     |     |               | Data Split: |     | Train | Validation |     |          |     |
| --- | --- | ------------- | ----------- | --- | ----- | ---------- | --- | -------- | --- |
|     |     | Random Forest |             |     |       |            |     | AdaBoost |     |
1.0
| 0.8 |             | 0.717 | 0.730 |       |       |     |       |       |             |
| --- | ----------- | ----- | ----- | ----- | ----- | --- | ----- | ----- | ----------- |
|     |             |       |       | 0.678 |       |     |       |       | 0.675 0.680 |
|     |             | 0.651 |       |       |       |     | 0.617 | 0.645 |             |
| 0.6 | 0.571 0.551 |       |       |       | 0.585 |     |       |       |             |
0.499
0.4
0.2
0.0
|     | Application Info | Bank Statement | Blended |     | Application Info |     | Bank Statement |     | Blended |
| --- | ---------------- | -------------- | ------- | --- | ---------------- | --- | -------------- | --- | ------- |
Feature Sets
Figure2: Evaluationresultsofallmodelsacrossdifferentfeaturecombinationsanddatasplits.
Table 2: Summary of extraction performance, latency, and cost for methods evaluated on key in-
formationandtransactiontableextractiontasks. Accuracyscoresareaveragedoverfivefields(key
info)andfivecolumntypes(table);F1isaveragedoversixbanks. Latencyistheaveragetotaltime
perdocument(seconds).TheproposedtemplatematchingmethodwasmeasuredonaMacBookAir
2025withM4chipand24GBunifiedmemory. CostisthetotalAPItokencostperdocument. Best
resultsareinbold;second-bestareunderlined. FullbreakdownsinAppendixTables3–14.
|        |     | KeyInformation |       | TableExtraction |       |       | Latency(s) |            | Cost(USD)  |
| ------ | --- | -------------- | ----- | --------------- | ----- | ----- | ---------- | ---------- | ---------- |
| Method |     | Exact          | NED   | Match.          | Exact | F1    | Key        | Table      | Table      |
|        |     | Match          | Score | NED             | NED   | Score | Info       | Extraction | Extraction |
docTR+GPT-4o-mini 91.87 99.20 88.41 78.52 92.16 2.38 7.59 N/A
| docTR+GPT-4.1 |     | 94.79 | 99.32 | 94.90 | 94.45 | 97.51 | 6.13 | 11.92 | 0.53 |
| ------------- | --- | ----- | ----- | ----- | ----- | ----- | ---- | ----- | ---- |
PyMuPDF+GPT-4o-mini 89.32 92.22 90.34 74.78 90.91 1.86 4.98 0.04
| PyMuPDF+GPT-4.1 |     | 93.23 | 93.86 | 94.76 | 93.49 | 97.64 | 0.81 | 10.72 | N/A |
| --------------- | --- | ----- | ----- | ----- | ----- | ----- | ---- | ----- | --- |
Pdfium+GPT-4o-mini 87.65 92.01 89.33 78.20 89.63 1.86 6.21 N/A
| Pdfium+GPT-4.1 |     | 93.57 | 94.20 | 93.82 | 89.63 | 95.66 | 0.86 | 11.19 | N/A |
| -------------- | --- | ----- | ----- | ----- | ----- | ----- | ---- | ----- | --- |
Ours(templatematching) 100.00 100.00 98.08 97.80 100.00 0.01 0.11 $0
bothextractiontasks. Fullper-bankbreakdowns,F1scores,anddetailedanalysisalongwithacom-
prehensivelatencyandcostanalysisacrossallconfigurationsareprovidedinAppendixA.5.
CostandLatencyAnalysis.OperationalefficiencyisakeyconsiderationforAI-BAAM.Wereport
latencyandcostmeasurementsacrossallconfigurationsinAppendixTables12,13,and14. Forkey
information extraction, our template matching method averages 0.01s per document with perfect
accuracy, orders of magnitude faster than the fastest LLM-based baseline (PyMuPDF (pymupdf,
2025)+GPT-4.1at0.81s). Fortableextraction,ourmethodaverages0.11scomparedto4.98sfor
PyMuPDF+GPT-4o-mini. Fortransactiontableextraction,text-basedpipelinessuchasPyMuPDF
+ GPT-4o-mini average under 5s, whereas end-to-end vision-language models require 104–150s.
AmongLLM-basedmethods, Surya+docTRwithGPT-5-mini($0.02)anddocTRwithGPT-4.1-
nano($0.03)arethemostcost-effective,whiledocTR+GPT-4.1incurs$0.53forthedataset. Our
templatematchingapproacheliminatesAPIcostsentirelywhilemaintainingsub-secondprocessing
latency,achievingthebestaccuracy–efficiencytrade-offforproductiondeployment.
7

PublishedasaconferencepaperatICLR2026
6.3 ABLATIONSTUDIES
ResultsinFigure3presentstheinformationvalueofindividualfeatures,rankedbydiscriminatory
power. Bankstatementfeaturesdominatethetoppositionswithlogarithmicgrowthrateofaverage
balance having the highest score of 0.484. In contrast, the strongest application information fea-
tureisbusinessoperationaldurationwithanIVof0.213, rankingfarbelowthetransaction-based
features. Thesefindingsreinforcethesuperiordiscriminatorystrengthofbankstatementfeaturesin
distinguishingdefaultfromnon-defaultoutcomes.
Furthermore,weconductedablationexperimentsbyprogressivelyremovingfeaturegroupstostudy
theirrelativeimportanceinMSMEscreditscoring. Weapplied5-foldcross-validationonthetrain-
ing split (366 samples) to reduce the risk that results are due to random chance and to increase
confidenceinmodelstability. FromresultsillustratedinFigure2,weobservethatLogisticRegres-
sionwithblendedfeaturesachievesthestrongestcross-validationAUROCof0.850,outperforming
GradientBoosting(0.720)andRandomForest(0.730). Whenconsideringbankstatementfeatures
alone,LRachievesavalidationAUROCof0.821,comparedto0.672foraccountinformationalone,
demonstrating a substantial uplift of 0.149 points. These results confirm that transactional data
providessignificantincrementalpredictivevalue. Acrossallfeatureconfigurationsanddatasplits,
LRconsistentlyoutperformstree-basedensembles. Moreover,modelsincorporatingbanktransac-
tiondataconsistentlyoutperformthoserelyingonapplicationinformationalone. Furtherstudiesof
thecreditscoredistributionforeachfeaturegroupaswellastheanalysisonrejectedcasescanbe
foundinAppendixA.6.1-A.6.2. Ingeneral,thesefindingsstronglysupportthehypothesisthatbank
statementtransactiondataofferssignificantpredictivepowerincreditriskassessmentforMSMEs
in Malaysia. While application form information provides some discriminatory power, the inclu-
sionofbanktransaction-basedfeaturessubstantiallyenhancesmodelperformance, reinforcingthe
effectivenessofAI-BAAM.LimitationsandfutureworkarediscussedinAppendixC.
Figure3: IVoffeaturesderivedfromapplicationinformationandbankstatementdata.
7 CONCLUSION
This study introduces bank statement transactions as alternative data for MSME credit scoring in
Malaysia and presents AI-BAAM, an end-to-end cash flow underwriting workflow spanning doc-
ument extraction, feature engineering, and predictive modeling. Empirical results confirm that
transaction-derived features capture dynamic financial behavior overlooked by traditional credit
models: models trained on bank transaction data alone substantially outperform those using only
application information, and combining both feature sets yields the highest predictive power. Be-
yondcreditscoring,webenchmarkover30OCRandLLMconfigurationsforkeyinformationand
transactiontableextractionacrosssixMalaysianbanks. Ourtemplatematchingapproachachieves
perfectaccuracyonkeyinformationfieldsandthehighestNEDandF1scoresontableextraction,
whileprocessingdocumentsinunder0.12secondswithzeroAPIcost. Incontrast,thebestLLM-
basedpipelinesrequire0.81-11.92secondsperdocumentandincuratotalof$0.53,andend-to-end
8

PublishedasaconferencepaperatICLR2026
vision-languagemodelsexhibit104-150secondslatencywithsubstantiallylowerextractionquality.
Thesefindingsdemonstratethatourtemplatematchingmethodoffersasuperioraccuracy-efficiency
trade-offovergeneral-purposeLLMpipelinesforMalaysianbankstatements.
8 ETHICAL USE OF DATA AND INFORMED CONSENT
Alldatausedinthisstudywereobtainedthroughaformaldata-sharingagreementwiththepartner-
ing Malaysian consulting firm. The dataset contains loan application records and bank statements
fromMSMEapplicantswhoconsentedtotheuseoftheirfinancialdataforcreditassessmentpur-
posesaspartoftheloanapplicationprocess. Allpersonallyidentifiableinformation,includingap-
plicantnames,nationalidentificationnumbers,bankaccountnumbers,andphysicaladdresses,was
masked or removed prior to analysis, as described in Section 4. Feature names were anonymized
and grouped into application information and bank statement features to prevent re-identification.
Thespecificfeaturederivationlogicisprotectedunderanon-disclosureagreementwiththelending
institution. Noindividual-levelpredictionsorriskscoresaredisclosedinthispaper,andallreported
results are presented in aggregate form. The anonymized dataset intended for public release will
undergo additional de-identification review to ensure compliance with Malaysia’s Personal Data
ProtectionAct2010(PDPA)andapplicableinstitutionaldatagovernancepolicies.
9 REPRODUCIBILITY
Thecompletemodelingpipeline,featureengineeringmethodology,andevaluationprotocolaredoc-
umentedinSections4–6.2. Allmachinelearningmodelsareimplementedusingscikit-learn(scikit
learn, 2025c;d;a;b), with hyperparameter configurations detailed in Section 6.2 and ablation set-
tingsinSection6.3. TheWOE/IV-basedfeaturetransformationandsupervisedmonotonicbinning
procedures are described formally in Section 4, and the feature groupings used in all experiments
are enumerated in Section 6.2. For the OCR and LLM benchmarks, the evaluated configurations
andsystemsetupsarereportedinAppendixA.3andAppendixA.4. Thedatasetusedinthisstudy
consists of real bank statements and loan records collected under a data-sharing agreement with a
Malaysianconsultingfirm. Asthedatacontainssensitivefinancialinformation,weareunabletore-
leasetherawrecordsduetocontractualobligationsandMalaysia’sPDPA.Weareworkingtowards
releasing an anonymized version pending a de-identification review, as described in Section 8. In
the meantime, researchers can replicate our workflow on their own bank statement data using the
step-by-stepmethodologydetailedthroughoutthepaperandappendix.
10 ACKNOWLEDGEMENT
WethanktheCradleFundandtheMicrosoftforStartupsprogramfortheirfundingsupport,which
madethisresearchpossible.WealsothanktheDocLab,DocSuite,andMLSuiteteamsatAILensfor
theircontributionsacrossdocumentprocessing,systemdevelopment,andmachinelearning,which
collectivelyshapedtheAI-BAAMpipelinepresentedinthiswork.
9

PublishedasaconferencepaperatICLR2026
REFERENCES
ElafAdelAbbasandNisreenAbbasHussein. Algorithmcomparisonfordataminingclassification:
Assessing bank customer credit scoring default risk. Jurnal Kejuruteraan, 36(5):1935–1944,
2024.
MohammadAsifAli. Efficientunderwritingusingagenticai. AvailableatSSRN5169848,2025.
Andrew P Bradley. The use of the area under the roc curve in the evaluation of machine learning
algorithms. Patternrecognition,30(7):1145–1159,1997.
LeoBreiman. Randomforests. Machinelearning,45(1):5–32,2001.
Iain Brown and Christophe Mues. An experimental comparison of classification algorithms for
imbalancedcreditscoringdatasets. Expertsystemswithapplications,39(3):3446–3453,2012.
Michael Bu¨cker, Gero Szepannek, Alicja Gosiewska, and Przemyslaw Biecek. Transparency, au-
ditability,andexplainabilityofmachinelearningmodelsincreditscoring. JournaloftheOpera-
tionalResearchSociety,73(1):70–90,2022.
RoryPBunker,WenjunZhang,andMAsifNaeem. Improvingacreditscoringmodelbyincorpo-
ratingbankstatementderivedfeatures. arXivpreprintarXiv:1611.00252,2016.
DeanCaireandMariaFernandezVidal.Leveragingtransactionaldataformicroandsmallenterprise
(mse) lending, March 2024. URL https://www.cgap.org/sites/default/files/
publications/Leveraging%20Transactional%20Data.pdf.
Pete Chapman, Julian Clinton, Randy Kerber, Colin Shearer Thomas Khabaza ands
Thomas Reinartz, and Ru¨diger Wirth. Crisp-dm 1.0 step-by-step data mining guide,
2000. URL https://www.kde.cs.uni-kassel.de/wp-content/uploads/
lehre/ws2012-13/kdd/files/CRISPWP-0800.pdf.
AijunCheng. Evaluatingfintechindustry’srisks: Apreliminaryanalysisbasedoncrisp-dmframe-
work. FinanceResearchLetters,55:103966,2023.
NaganarendarChitturi. Agenticartificialintelligence: Architecturalparadigmsandtransformative
impactofautonomousfinancialassistantsacrossthemortgagelendinglifecycle. JournalofCom-
puterScienceandTechnologyStudies,7(8):1155–1165,2025.
InternationalFinanceCorporation. MSMEFinanceGap: AssessmentoftheShortfallsandOppor-
tunitiesinFinancingMicro,Small,andMediumEnterprisesinEmergingMarkets. WorldBank,
Washington,D.C.,UnitedStates,2017.
MJ Courchane and AP Baines. The use of cash-flow data in underwriting
credit, October 2020. URL https://finreglab.org/wp-content/
uploads/2023/12/FinRegLab_2020-03-03_Research-Report_
The-Use-of-Cash-Flow-Data-in-Underwriting-Credit_
Market-Context-and-Policy-Analysis.pdf.
Cheng Cui, Ting Sun, Suyin Liang, Tingquan Gao, Zelun Zhang, Jiaxuan Liu, Xueqing Wang,
Changda Zhou, Hongen Liu, Manhui Lin, et al. Paddleocr-vl: Boosting multilingual docu-
mentparsingviaa0.9bultra-compactvision-languagemodel. arXivpreprintarXiv:2510.14528,
2025a.
ChengCui,TingSun,ManhuiLin,TingquanGao,YuboZhang,JiaxuanLiu,XueqingWang,Zelun
Zhang, Changda Zhou, Hongen Liu, Yue Zhang, Wenyu Lv, Kui Huang, Yichao Zhang, Jing
Zhang, Jun Zhang, Yi Liu, Dianhai Yu, and Yanjun Ma. Paddleocr 3.0 technical report, 2025b.
URLhttps://arxiv.org/abs/2507.05595.
BCarneirodaRochaandRTimoteodeSousaJunior. Identifyingbankfraudsusingcrisp-dmand
decision trees. International Journal of Computer Science and Information Technology, 2(5):
162–169,2010.
10

PublishedasaconferencepaperatICLR2026
DOSM Department of Statistics Malaysia. Profile of msmes in 2015-2024, Au-
gust 2025. URL https://smecorp.gov.my/index.php/en/policies/
2020-02-11-08-01-24/profile-and-importance-to-the-economy.
VianiBDjeundje,JonathanCrook,RaffaellaCalabrese,andMonaHamid.Enhancingcreditscoring
withalternativedata. ExpertSystemswithApplications,163:113766,2021.
Adrien Ehrhardt, Christophe Biernacki, Vincent Vandewalle, Philippe Heinrich, and Se´bastien
Beben. Reject inference methods in credit scoring. Journal of Applied Statistics, 48(13-15):
2734–2754,2021. doi: 10.1080/02664763.2021.1929090.
Okeoghene Elebe and Chikaome Chimara Imediegwu. A credit scoring system using transaction-
level behavioral data for msmes. Journal of Frontiers in Multidisciplinary Research, 2(1):312–
322,2021.
Jerome H Friedman. Greedy function approximation: a gradient boosting machine. Annals of
statistics,pp.1189–1232,2001.
Anthony Gathu. The Role of alternative data in accurately determining credit score for mobile
lendingondigitalwalletsinKenya. PhDthesis,StrathmoreUniversity,2020.
AmolGoteandVikasMendhe. Buildingacashflowunderwritingsystem:Insightsfromimplemen-
tation. InternationalJournalofComputerTrendsandTechnology,72(2):70–74,2024.
World Bank Group. The use of alternative data in credit risk assess-
ment: Opportunities, risks, and challenges, 2024. URL https://
documents1.worldbank.org/curated/en/099031325132018527/pdf/
P179614-3e01b947-cbae-41e4-85dd-2905b6187932.pdf.
Bjo¨rn Rafn Gunnarsson, Seppe Vanden Broucke, Bart Baesens, Mar´ıa O´skarsdo´ttir, and Wilfried
Lemahieu. Deep learning for credit scoring: Do or don’t? European Journal of Operational
Research,295(1):292–305,2021.
ExperianInsights. Rejectinferenceandunderwriting: Adeepdive,2024. URLhttps://www.
experian.com/blogs/insights/reject-inference/.
EunjiKim,JehyukLee,HunsikShin,HoseongYang,SungzoonCho,Seung-kwanNam,Youngmi
Song, Jeong-a Yoon, and Jong-il Kim. Champion-challenger analysis for credit card fraud de-
tection: Hybrid ensemble and deep learning. Expert Systems with Applications, 128:214–224,
2019.
Jung Youn Lee, Joonhyuk Yang, and Eric T. Anderson. Express: Who benefits from alter-
native data for credit scoring? evidence from peru. Journal of Marketing Research, 0(ja):
00222437251360996, 0. doi: 10.1177/00222437251360996. URLhttps://doi.org/10.
1177/00222437251360996.
Stefan Lessmann, Bart Baesens, Hsin-Vonn Seow, and Lyn C Thomas. Benchmarking state-of-
the-art classification algorithms for credit scoring: An update of research. European journal of
operationalresearch,247(1):124–136,2015.
ZhangLi,YuliangLiu,QiangLiu,ZhiyinMa,ZiyangZhang,ShuoZhang,ZidunGuo,JiaruiZhang,
XinyuWang,andXiangBai.Monkeyocr:Documentparsingwithastructure-recognition-relation
tripletparadigm. arXivpreprintarXiv:2506.05218,2025.
Minghui Liao, Zhaoyi Wan, Cong Yao, Kai Chen, and Xiang Bai. Real-time scene text detection
withdifferentiablebinarization. InProceedingsoftheAAAIconferenceonartificialintelligence,
volume34,pp.11474–11481,2020.
Security Commissions Malaysia. Enabling a more relevant, efficient and diversified mar-
ket,2025.URLhttps://www.sc.com.my/api/documentms/download.ashx?id=
61f72817-e06d-4e54-b25c-8be8abddcd28.
Mindee. doctr: Documenttextrecognition. https://github.com/mindee/doctr,2021.
11

PublishedasaconferencepaperatICLR2026
AndrewYNg. Featureselection,l1vs.l2regularization,androtationalinvariance. InProceedings
ofthetwenty-firstinternationalconferenceonMachinelearning,pp. 78,2004.
MfanasibiliNgwenya.Creditscoringinafrica:Employinglogisticregressiononalternativedata.In
20244thInternationalConferenceonElectrical,Computer,CommunicationsandMechatronics
Engineering(ICECCME),pp.1–6,Maldives,2024.IEEE. doi: 10.1109/ICECCME62383.2024.
10796011.
IzunnaOkpala,AshkanGolgoon,andArjunRaviKannan. Agenticaisystemsappliedtotasksinfi-
nancialservices:modelingandmodelriskmanagementcrews. arXivpreprintarXiv:2502.05439,
2025.
Srinivasarao Paleti. Agentic ai in financial decision-making: Enhancing customer risk profiling,
predictive loan approvals, and automated treasury management in modern banking. Multidisci-
plinary,ScientificWorkandManagementJournal,2024.
Vikas Paruchuri and Datalab Team. Surya: A lightweight document ocr and analysis toolkit.
https://github.com/VikParuchuri/surya,2025. GitHubrepository.
Jake Poznanski, Jon Borchardt, Jason Dunkelberger, Regan Huff, Daniel Lin, Aman Rangapur,
Christopher Wilhelm, Kyle Lo, and Luca Soldaini. olmOCR: Unlocking Trillions of Tokens
in PDFs with Vision Language Models, 2025. URL https://arxiv.org/abs/2502.
18443.
pymupdf. Pymupdf. https://github.com/pymupdf/PyMuPDF,2025. GitHubrepository.
KuldeepRawat. Applyingcrisp-dmmethodologyindevelopingmachinelearningmodelforcredit
riskprediction. InScienceandInformationConference,pp.522–538.Springer,2023.
RobertESchapire. Explainingadaboost. InEmpiricalinference: festschriftinhonorofvladimirN.
Vapnik,pp.37–52.Springer,2013.
scikit learn. Adaboostclassifier, 2025a. URL https://scikit-learn.org/stable/
modules/generated/sklearn.ensemble.AdaBoostClassifier.html.
scikit learn. Gradientboostingclassifier, 2025b. URL https://
scikit-learn.org/stable/modules/generated/sklearn.ensemble.
GradientBoostingClassifier.html.
scikit learn. Logisticregression, 2025c. URL https://scikit-learn.org/stable/
modules/generated/sklearn.linear_model.LogisticRegression.html.
scikitlearn. Randomforestclassifier, 2025d. URLhttps://scikit-learn.org/stable/
modules/generated/sklearn.ensemble.RandomForestClassifier.html.
BaoguangShi,XiangBai,andCongYao. Anend-to-endtrainableneuralnetworkforimage-based
sequencerecognitionanditsapplicationtoscenetextrecognition. IEEEtransactionsonpattern
analysisandmachineintelligence,39(11):2298–2304,2016.
TanmayShivhare. HowtoUtilizeBankStatementsasaNewCreditScoringMethod. PhDthesis,
Dublin,NationalCollegeofIreland,2024.
NaeemSiddiqi. Intelligentcreditscoring: Buildingandimplementingbettercreditriskscorecards.
JohnWiley&Sons,NorthCarolina,USA,2017. ISBN9781119282396.
Shrawan Kumar Trivedi. A study on credit scoring modeling with different feature selection and
machinelearningapproaches. TechnologyinSociety,63:101413,2020.
BinWang,ChaoXu,XiaomengZhao,LinkeOuyang,FanWu,ZhiyuanZhao,RuiXu,KaiwenLiu,
Yuan Qu, Fukai Shang, et al. Mineru: An open-source solution for precise document content
extraction,2024a. arXivpreprintarXiv:2409.18839.
12

PublishedasaconferencepaperatICLR2026
Stewart Watterson. Cash flow underwriting: Reshaping the lending landscape,
November 2024. URL https://assets.ctfassets.net/ss5kfr270og3/
2LceEfOxttxwSpVtkiAPUw/dd87916c5d598b4fa8950d12f896ab1d/
20241203_Cash_Flow_Underwriting_Reshaping_the_Lending_Landscape_
White_Paper_Plaid.pdf.
Haoran Wei, Yaofeng Sun, and Yukun Li. Deepseek-ocr 2: Visual causal flow. arXiv preprint
arXiv:2601.20552,2026.
13

PublishedasaconferencepaperatICLR2026
A APPENDIX
A.1 LOGISTICREGRESSIONMODEL
Given thatWOE provides alog-odds transformation of eachfeature, this alignsnaturally with the
LR model. The WOE transformed feature value can be represented as WOE (x ) and the LR
j ij
modelcanbeexpressedinasimplifiedformas:
d
log P(y i =1|x i ) =β + (cid:88) β WOE (x ). (6)
P(y =0|x ) 0 j j ij
i i
j=1
where β is the intercept and β represents the coefficient for feature j. This allows direct inter-
0 j
pretationofcoefficientsintermsofthecreditriskassociatedwitheachfeature. Positiveβ values
j
indicatethathigherWOEcorrespondstolowerdefaultrisk,andviceversa. Hence,WOEencoding
stabilizesestimationandsupportsconsistent,monotonicrelationshipsbetweenpredictorsandcredit
outcomes.
Formally, let x ∈ Rd denote the feature vector for applicant i, where d is the number of features
i
engineeredfrombothapplicationformdataandbankstatementtransactions,andlety ∈{0,1}be
i
thebinaryoutputindicatingdefault(y = 1)ornon-default(y = 0). TheLRmodelspecifiesthe
i i
conditionalprobabilityofdefaultas
P(y =1|x ;β)=σ(β +x⊤β), (7)
i i 0 i
where σ(z) = 1 is the sigmoid function, β ∈ R is the intercept term, and β ∈ Rd is the
1+e−z 0
coefficientvectorassociatedwiththepredictors. Theparametersareestimatedbymaximizingthe
penalizedlog-likelihoodfunction:
n
(cid:88)
L(β)= [y logp +(1−y )log(1−p )]−λ∥β∥2, (8)
i i i i 2
i=1
wherep = P(y = 1 | x ;β)andλ ≥ 0controlsthestrengthoftheℓ regularization(Ng,2004).
i i i 2
Thismitigatesoverfittingbyshrinkingcoefficientmagnitudes,whichisparticularlyimportantwhen
modelinghigh-dimensional,transaction-derivedfeatures.
A.2 USEOFLARGELANGUAGEMODELS
A.2.1 DATASET
We gathered bank statements of various consulting firms in Malaysia. The dataset consists of ap-
proximately110uniquebankstatementPDFsfromthetop6banksinMalaysia: Maybank,Public
Bank,CIMBBank,RHBBank,HongLeongBank,andAmBank.Eachbankstatementcontainskey
informationfieldssuchasbankname,accountholdername,accountnumber,address,andstatement
date,aswellastransactiontableslistingindividualtransactionswithdetailssuchasdate,description,
debitamount,creditamount,andbalance.
A.2.2 MODELCHOICES
PrecisetextboundingboxcoordinatesforOCRresultsarerequiredbecausebankofficersmustcross-
checkextractionresultsbeforetheycanbeusedforsubsequentprocessing;thisensurestransparency,
traceability, and auditability of our AI results, and explains our design choice of using OCR and
LLMs for financial information extraction. The OCR models used are mainly from Azure with
different variations: prebuilt-bankStatement.us is an Azure Document Intelligence prebuilt OCR
modelspecificallydesignedforbankstatementsintheUS,whilepretrained-readisamoregeneral
OCRmodelthatcanbefine-tunedforvariousdocumenttypes. TheAzureVision4.0modelrefers
totheAzuregenericOCRmodel. TheGPTmodelsusedareGPT-4o-miniandGPT-4.1,whichare
differentversionsofOpenAI’sGPT-4architecturewithvaryingcapabilitiesandperformancelevels.
14

PublishedasaconferencepaperatICLR2026
Certain specialized OCR models such as MinerU (Wang et al.), PyMuPDF (pymupdf, 2025) and
PPStructureV3(Cuietal.,2025b)areincludedforcomparisonsincetheyarewidelyadoptedinthe
industryfordocumentprocessingtasks. PyMuPDF-Formattedreferstoformattingtheoutputfrom
document parser to imitate actual document layout before passing them into LLM. LLM-based
OCR models such as olmOCR (Poznanski et al., 2025), paddleOCR-VL (Cui et al., 2025a), and
Surya(Paruchuri&Team,2025)arealsoincludedfortableextractioncomparisons. Ourtemplate
matchingmethodisbuiltbasedonthelayoutofthebankstatementsinourdataset,wherewemanu-
allydefinetheregionsofinterestforkeyinformationfieldsandtransactiontables. Forourmethod,
weuseDBwithResNet50backbone(Liaoetal.,2020)fortextdetectionandCRNNwithVGG16
backbone(Shietal.,2016)fortextrecognition.Thenwebuildourowntemplatematchingalgorithm
in Python logic. Do note that we are the only method that is not using any LLMs for information
extraction.
AsshowninTables3,4,8,and9,ourtemplatematchingmethodachievesthebestperformancewhen
the bank statement formats are consistent, which is the case in Malaysia. In real-world scenarios
where bank statement formats can vary significantly, template matching methods may not be as
effectiveasmoreflexibleOCRmodels.Infuturework,weplantoexploremoreadvancedtechniques
such as OCR+LLM-based layout analysis and document understanding models (Deepseek-OCR
2 (Wei et al., 2026), MonkeyOCR (Li et al., 2025)) to improve the robustness of key information
andtableextractionacrossdiversebankstatementformats.
A.2.3 EVALUATIONMETRIC
Key information results are evaluated based on exact match accuracy between the extracted text
andthegroundtruthforeachfield. Anexactmatchiscountedwhentheextractedtextmatchesthe
groundtruthcharacterbycharacter,includingspacesandpunctuation. Theaccuracyisthencalcu-
latedasthepercentageofexactmatchesoverthetotalnumberofkeyinformationfieldsevaluated.
Table extraction results are evaluated based on the normalized edit distance (NED) between the
extracted text and the ground truth for each transaction row. The NED for a single row entry is
calculatedasfollows:
EditDistance
NED=1− (9)
max(LengthofExtractedText,LengthofGroundTruthText)
whereEditDistanceistheminimumnumberofoperations(insertions,deletions,substitutions)re-
quiredtotransformtheextractedtextintothegroundtruthtext.AhigherNEDvalueindicatesbetter
accuracy,withamaximumof1.0representingaperfectmatch. Thescoreisthenscaledtotherange
of0to100foreasierinterpretation.
Wereporttwovariantsoftheper-columnsimilarityscoretocapturedifferentaspectsofextraction
quality:
MatchingNEDScore(%). Foreachcolumn(date,description,debit,credit,balance),wecompute
the NED for every matched row. Only rows with NED > 70% are retained, and the per-column
scoreistheaverageNEDacrossthesefilteredrowsforagivenbank. Thismetricmeasureshowac-
curatelythesystemextractscontentforrowsthatithasreasonablyidentified,byexcludingseverely
misaligned or garbled entries that fall below the 70% threshold. It thus reflects extraction quality
conditionedonsuccessfulrowmatching.
ExactNEDScore(%). Foreachcolumn,wecomputetheNEDforeveryrowwithoutanyfiltering
threshold. All rows are included regardless of their NED value, and the per-column score is the
averageNEDacrossallrowsforagivenbank. Thismetricprovidesastricterevaluationthatpenal-
izesbothcharacter-levelextractionerrorsandrow-levelalignmentfailures(e.g.,missedrows,extra
rows,ormisalignedentries),asthesecontributelowNEDvaluesthatreducetheoverallaverage.
Thekeydifferencebetweenthetwometricsliesintheirtreatmentofpoorlymatchedrows. Match-
ing NED isolates extraction accuracy by filtering out rows with NED ≤ 70%, while exact NED
capturesthefullpictureincludingrowdetectionfailures. Alargegapbetweenmatchingandexact
NEDscoresforagivenconfigurationindicatesthatthesystemproducesaccurateextractionswhen
itcorrectlyidentifiesrows,butfrequentlyfailsatrow-levelalignmentormissesrowsentirely. Con-
versely,similarmatchingandexactNEDscoressuggestconsistentrowdetectionwithfewalignment
failures.
15

PublishedasaconferencepaperatICLR2026
A.3 QUANTITATIVERESULTSFORKEYINFORMATIONEXTRACTION
We evaluate key information extraction across the top six largest Malaysian banks: Maybank
(MBBE), Public Bank (PBBE), CIMB Bank (CIBB), RHB Bank (RHBB), Hong Leong Bank
(HLBB), and AmBank (ARBK). The evaluation covers five structured fields: bank name, account
holder, account number, address, and statement date. We report both exact match accuracy with
strict character-level equality and Normalized Edit Distance (NED) similarity with a tolerance for
minor character-level discrepancies. Tables 3 and 4 summarize the average exact match accuracy
and NED score performance across all banks respectively, while Tables 5 and 6 provide per-bank
breakdowns.
Overall Performance. Our template matching approach achieves a perfect 100% on both exact
match accuracy and NED score across all five fields and all six banks, demonstrating robust and
consistentextractionwithoutrelianceonexternalOCRorLLMAPIs. Amongthebaselines,config-
urations pairing high-quality OCR engines (Pretrained-Read, Azure AI 4.0) with GPT-4.1 achieve
near-perfect results, with Azure AI 4.0 + GPT-4.1 reaching 100% exact match accuracy on four
fields (bank name, account holder, account number, and statement date) and 94.82% on address.
Theaddressfieldprovesmostchallengingacrossallconfigurationsduetomulti-lineformattingand
bank-specificlayoutvariations.
OCR Engine Impact. The choice of OCR engine substantially influences downstream extraction
quality. Cloud-basedOCRsolutions(Pretrained-Read,AzureAI4.0)consistentlyoutperformopen-
source alternatives. MinerU exhibits the weakest bank name extraction (28.33%–41.30% exact
match accuracy) due to its inability to parse graphical logos and stylized text commonly found in
Malaysianbankstatementheaders. Text-basedextractors(PyMuPDF,Pdfium)showvariablebank
nameaccuracy(58.76%–74.87%), astheyrelyonthePDFtextlayer, whichmaynotencodebank
names embedded in header images. In contrast, docTR achieves 100% bank name accuracy by
leveragingdeeplearning-basedtextdetectiononrenderedpageimages.
GPT Model Impact. Across all OCR engines, upgrading from GPT-4o-mini to GPT-4.1 consis-
tentlyimprovesextractionaccuracy,particularlyforaddressandstatementdatefields. Forexample,
with docTR, the address exact match accuracy improves from 73.97% to 80.82% when switching
to GPT-4.1. This improvement stems from GPT-4.1’s enhanced ability to parse multi-line address
formatsandnormalizedaterepresentationsacrossdifferentbanktemplates.
Per-BankVariation.AmBankandHongLeongBankstatementsaregenerallyeasiertoprocessdue
totheirstandardizeddigital-nativePDFformats,achievingnear-perfectscoresacrossmostconfigu-
rations. RHBBankandCIMBBankpresentgreaterchallenges: RHBBank’smulti-columnlayouts
reduceMinerU’sperformanceto40–70%acrossmostfields,whileCIMBBank’sheaderformatting
leads to lower bank name recognition for text-based extractors. These per-bank variations under-
scoretheimportanceofbank-specificevaluationwhendeployingextractionsystemsinmulti-bank
productionenvironments.
Table3: Averageexactmatchaccuracyscoresacrossalltopsixlargestbanks.
KeyInformationExtraction-ExactMatchAccuracy
| OCR       | GPT |          |           |           |         |               |
| --------- | --- | -------- | --------- | --------- | ------- | ------------- |
|           |     | BankName | AccHolder | AccNumber | Address | StatementDate |
| Prebuilt- | N/A | 93.39    | 80.82     | 92.86     | 92.77   | 77.51         |
BankStatement
| Pretrained-Read | gpt-4o-mini | 100.00 | 96.48  | 100.00 | 89.10 | 97.62  |
| --------------- | ----------- | ------ | ------ | ------ | ----- | ------ |
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 92.43 | 100.00 |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 98.15  | 100.00 | 88.20 | 97.62  |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 94.82 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 87.78  | 100.00 | 73.97 | 97.62  |
| docTR           | gpt-4.1     | 100.00 | 93.15  | 100.00 | 80.82 | 100.00 |
| MinerU          | gpt-4o-mini | 28.33  | 86.48  | 90.95  | 61.43 | 95.00  |
| MinerU          | gpt-4.1     | 41.30  | 86.67  | 93.33  | 72.14 | 95.00  |
| PyMuPDF         | gpt-4o-mini | 62.09  | 96.30  | 100.00 | 90.58 | 97.62  |
| PyMuPDF         | gpt-4.1     | 71.16  | 98.33  | 100.00 | 96.67 | 100.00 |
Continuedonnextpage
16

PublishedasaconferencepaperatICLR2026
Table3–Continuedfrompreviouspage
KeyInformationExtraction-ExactMatchAccuracy
| OCR      | GPT         |          |           |           |         |               |
| -------- | ----------- | -------- | --------- | --------- | ------- | ------------- |
|          |             | BankName | AccHolder | AccNumber | Address | StatementDate |
| PyMuPDF- | gpt-4o-mini | 61.92    | 98.15     | 100.00    | 92.25   | 100.00        |
Formatted
| PyMuPDF- | gpt-4.1 | 74.87 | 98.15 | 100.00 | 96.48 | 100.00 |
| -------- | ------- | ----- | ----- | ------ | ----- | ------ |
Formatted
| Pdfium                 | gpt-4o-mini                                          | 58.76  | 96.30  | 100.00 | 83.17  | 100.00 |
| ---------------------- | ---------------------------------------------------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1                                              | 71.16  | 100.00 | 100.00 | 96.67  | 100.00 |
| Ours(templatematching) |                                                      | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
|                        | Table4: AverageNEDscoresacrossalltopsixlargestbanks. |        |        |        |        |        |
KeyInformationExtraction-NEDScore
| OCR       | GPT |          |           |           |         |               |
| --------- | --- | -------- | --------- | --------- | ------- | ------------- |
|           |     | BankName | AccHolder | AccNumber | Address | StatementDate |
| Prebuilt- | N/A | 93.39    | 82.75     | 95.11     | 98.40   | 79.13         |
BankStatement
| Pretrained-Read | gpt-4o-mini | 100.00 | 97.36  | 100.00 | 96.30 | 99.70  |
| --------------- | ----------- | ------ | ------ | ------ | ----- | ------ |
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 99.34 | 100.00 |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 98.59  | 100.00 | 96.90 | 99.70  |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 99.59 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 98.44  | 100.00 | 97.84 | 99.70  |
| docTR           | gpt-4.1     | 100.00 | 98.02  | 100.00 | 98.60 | 100.00 |
| MinerU          | gpt-4o-mini | 37.00  | 88.29  | 92.74  | 77.46 | 97.50  |
| MinerU          | gpt-4.1     | 43.79  | 86.67  | 93.33  | 84.20 | 96.25  |
| PyMuPDF         | gpt-4o-mini | 64.99  | 97.28  | 100.00 | 99.11 | 99.70  |
| PyMuPDF         | gpt-4.1     | 71.17  | 98.33  | 100.00 | 99.82 | 100.00 |
| PyMuPDF-        | gpt-4o-mini | 69.36  | 98.15  | 100.00 | 99.17 | 100.00 |
Formatted
| PyMuPDF- | gpt-4.1 | 75.77 | 99.32 | 100.00 | 99.50 | 100.00 |
| -------- | ------- | ----- | ----- | ------ | ----- | ------ |
Formatted
| Pdfium                 | gpt-4o-mini | 63.96  | 97.13  | 100.00 | 98.97  | 100.00 |
| ---------------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     | 71.17  | 100.00 | 100.00 | 99.82  | 100.00 |
| Ours(templatematching) |             | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
Table5: KeyinformationextractionexactmatchaccuracyscoregroupedbybankacrossOCRand
GPTconfigurations.
KeyInformationExtraction-ExactMatchAccuracy
| OCR | GPT |          |           |           |         |               |
| --- | --- | -------- | --------- | --------- | ------- | ------------- |
|     |     | BankName | AccHolder | AccNumber | Address | StatementDate |
CIMBBank(7UniquePDFs)
| Prebuilt- | N/A | 71.43 | 71.43 | 57.14 | 85.71 | 42.86 |
| --------- | --- | ----- | ----- | ----- | ----- | ----- |
BankStatement
| Pretrained-Read | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 85.71  | 85.71  |
| --------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 85.71  | 100.00 |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 71.43  | 85.71  |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 57.14  | 85.71  |
| docTR           | gpt-4.1     | 100.00 | 100.00 | 100.00 | 57.14  | 100.00 |
| MinerU          | gpt-4o-mini | 0.00   | 100.00 | 85.71  | 85.71  | 100.00 |
| MinerU          | gpt-4.1     | 0.00   | 100.00 | 100.00 | 100.00 | 100.00 |
| PyMuPDF         | gpt-4o-mini | 71.43  | 100.00 | 100.00 | 85.71  | 85.71  |
| PyMuPDF         | gpt-4.1     | 71.43  | 100.00 | 100.00 | 100.00 | 100.00 |
| PyMuPDF-        | gpt-4o-mini | 71.43  | 100.00 | 100.00 | 85.71  | 100.00 |
Formatted
Continuedonnextpage
17

PublishedasaconferencepaperatICLR2026
Table5–Continuedfrompreviouspage
KeyInformationExtraction-ExactMatchAccuracy
| OCR      | GPT     |          |           |           |         |               |
| -------- | ------- | -------- | --------- | --------- | ------- | ------------- |
|          |         | BankName | AccHolder | AccNumber | Address | StatementDate |
| PyMuPDF- | gpt-4.1 | 71.43    | 100.00    | 100.00    | 100.00  | 100.00        |
Formatted
| Pdfium                 | gpt-4o-mini | 71.43  | 100.00 | 100.00 | 85.71  | 100.00 |
| ---------------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     | 71.43  | 100.00 | 100.00 | 100.00 | 100.00 |
| Ours(templatematching) |             | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
RHBBank(10UniquePDFs)
| Prebuilt- | N/A | 100.00 | 90.00 | 100.00 | 70.00 | 100.00 |
| --------- | --- | ------ | ----- | ------ | ----- | ------ |
BankStatement
Pretrained-Read gpt-4o-mini 100.00 100.00 100.00 90.00 100.00
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 80.00  | 100.00 |
| --------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 80.00  | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 70.00  | 100.00 | 80.00  | 100.00 |
| docTR           | gpt-4.1     | 100.00 | 70.00  | 100.00 | 70.00  | 100.00 |
| MinerU          | gpt-4o-mini | 70.00  | 50.00  | 70.00  | 40.00  | 70.00  |
| MinerU          | gpt-4.1     | 70.00  | 50.00  | 70.00  | 40.00  | 70.00  |
| PyMuPDF         | gpt-4o-mini | 90.00  | 100.00 | 100.00 | 80.00  | 100.00 |
| PyMuPDF         | gpt-4.1     | 100.00 | 100.00 | 100.00 | 80.00  | 100.00 |
| PyMuPDF-        | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
Formatted
| PyMuPDF- | gpt-4.1 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| -------- | ------- | ------ | ------ | ------ | ------ | ------ |
Formatted
| Pdfium                 | gpt-4o-mini | 70.00  | 100.00 | 100.00 | 80.00  | 100.00 |
| ---------------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     | 100.00 | 100.00 | 100.00 | 80.00  | 100.00 |
| Ours(templatematching) |             | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
HongLeongBank(9UniquePDFs)
| Prebuilt- | N/A | 100.00 | 88.89 | 100.00 | 100.00 | 100.00 |
| --------- | --- | ------ | ----- | ------ | ------ | ------ |
BankStatement
Pretrained-Read gpt-4o-mini 100.00 88.89 100.00 100.00 100.00
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| --------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 88.89  | 100.00 | 88.89  | 100.00 |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 66.67  | 100.00 | 88.89  | 100.00 |
| docTR           | gpt-4.1     | 100.00 | 88.89  | 100.00 | 100.00 | 100.00 |
| MinerU          | gpt-4o-mini | 0.00   | 88.89  | 100.00 | 100.00 | 100.00 |
| MinerU          | gpt-4.1     | 44.44  | 100.00 | 100.00 | 100.00 | 100.00 |
| PyMuPDF         | gpt-4o-mini | 100.00 | 88.89  | 100.00 | 88.89  | 100.00 |
| PyMuPDF         | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| PyMuPDF-        | gpt-4o-mini | 100.00 | 88.89  | 100.00 | 88.89  | 100.00 |
Formatted
| PyMuPDF- | gpt-4.1 | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| -------- | ------- | ------ | ------ | ------ | ------ | ------ |
Formatted
| Pdfium                 | gpt-4o-mini | 100.00 | 88.89  | 100.00 | 44.44  | 100.00 |
| ---------------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| Ours(templatematching) |             | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
AmBank(7UniquePDFs)
| Prebuilt- | N/A | 100.00 | 85.71 | 100.00 | 100.00 | 100.00 |
| --------- | --- | ------ | ----- | ------ | ------ | ------ |
BankStatement
Pretrained-Read gpt-4o-mini 100.00 100.00 100.00 100.00 100.00
| Pretrained-Read | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| --------------- | ----------- | ------ | ------ | ------ | ------ | ------ |
| AzureAI4.0      | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| AzureAI4.0      | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| docTR           | gpt-4o-mini | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| docTR           | gpt-4.1     | 100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| MinerU          | gpt-4o-mini | 0.00   | 100.00 | 100.00 | 42.86  | 100.00 |
| MinerU          | gpt-4.1     | 0.00   | 100.00 | 100.00 | 42.86  | 100.00 |
Continuedonnextpage
18

PublishedasaconferencepaperatICLR2026
Table5–Continuedfrompreviouspage
KeyInformationExtraction-ExactMatchAccuracy
| OCR      | GPT         |          |      |           |           |        |         |               |
| -------- | ----------- | -------- | ---- | --------- | --------- | ------ | ------- | ------------- |
|          |             | BankName |      | AccHolder | AccNumber |        | Address | StatementDate |
| PyMuPDF  | gpt-4o-mini |          | 0.00 | 100.00    |           | 100.00 | 100.00  | 100.00        |
| PyMuPDF  | gpt-4.1     |          | 0.00 | 100.00    |           | 100.00 | 100.00  | 100.00        |
| PyMuPDF- | gpt-4o-mini |          | 0.00 | 100.00    |           | 100.00 | 100.00  | 100.00        |
Formatted
| PyMuPDF- | gpt-4.1 |     | 0.00 | 100.00 |     | 100.00 | 100.00 | 100.00 |
| -------- | ------- | --- | ---- | ------ | --- | ------ | ------ | ------ |
Formatted
| Pdfium                 | gpt-4o-mini |     | 0.00   | 100.00 |     | 100.00 | 100.00 | 100.00 |
| ---------------------- | ----------- | --- | ------ | ------ | --- | ------ | ------ | ------ |
| Pdfium                 | gpt-4.1     |     | 0.00   | 100.00 |     | 100.00 | 100.00 | 100.00 |
| Ours(templatematching) |             |     | 100.00 | 100.00 |     | 100.00 | 100.00 | 100.00 |
Table6: KeyinformationextractionsimilarityscoregroupedbybankacrossOCRandGPTconfig-
urations.
KeyInformationExtraction-NEDScore
| OCR | GPT |          |     |           |     |           |         |               |
| --- | --- | -------- | --- | --------- | --- | --------- | ------- | ------------- |
|     |     | BankName |     | AccHolder |     | AccNumber | Address | StatementDate |
Maybank(10UniquePDFs)
| prebuilt- | N/A |     | 100 | 69.09 |     | 100 | 100 | 100 |
| --------- | --- | --- | --- | ----- | --- | --- | --- | --- |
bankStatement.us
| pretrained-read        | GPT-4o-mini |     | 100 | 92.63 |     | 100 | 82.01 | 100 |
| ---------------------- | ----------- | --- | --- | ----- | --- | --- | ----- | --- |
| pretrained-read        | GPT-4.1     |     | 100 | 100   |     | 100 | 100   | 100 |
| AzureAI4.0             | GPT-4o-mini |     | 100 | 100   |     | 100 | 87.24 | 100 |
| AzureAI4.0             | GPT-4.1     |     | 100 | 100   |     | 100 | 100   | 100 |
| MinerU                 | GPT-4o-mini |     | 100 | 85.14 |     | 90  | 27.41 | 100 |
| MinerU                 | GPT-4.1     |     | 100 | 70    |     | 90  | 66.36 | 100 |
| PyMuPDF                | GPT-4o-mini |     | 100 | 100   |     | 100 | 100   | 100 |
| PyMuPDF                | GPT-4.1     |     | 100 | 90    |     | 100 | 100   | 100 |
| pdfium                 | GPT-4o-mini |     | 100 | 100   |     | 100 | 100   | 10  |
| pdfium                 | GPT-4.1     |     | 100 | 100   |     | 100 | 100   | 10  |
| Ours(templatematching) |             |     | 100 | 100   |     | 100 | 100   | 100 |
PublicBank(9UniquePDFs)
| prebuilt- | N/A |     | 88.89 | 88.89 |     | 100 | 98.60 | 31.94 |
| --------- | --- | --- | ----- | ----- | --- | --- | ----- | ----- |
bankStatement.us
| pretrained-read        | GPT-4o-mini |     | 100   | 100   |     | 100 | 99.74 | 100 |
| ---------------------- | ----------- | --- | ----- | ----- | --- | --- | ----- | --- |
| pretrained-read        | GPT-4.1     |     | 100   | 100   |     | 100 | 98.60 | 100 |
| AzureAI4.0             | GPT-4o-mini |     | 100   | 100   |     | 100 | 98.60 | 100 |
| AzureAI4.0             | GPT-4.1     |     | 100   | 100   |     | 100 | 98.60 | 100 |
| MinerU                 | GPT-4o-mini |     | 20.16 | 100   |     | 100 | 100   | 100 |
| MinerU                 | GPT-4.1     |     | 41.83 | 100   |     | 100 | 100   | 100 |
| PyMuPDF                | GPT-4o-mini |     | 16.88 | 92.16 |     | 100 | 98.60 | 100 |
| PyMuPDF                | GPT-4.1     |     | 55.56 | 100   |     | 100 | 100   | 100 |
| pdfium                 | GPT-4o-mini |     | 20.85 | 91.27 |     | 100 | 98.60 | 100 |
| pdfium                 | GPT-4.1     |     | 55.56 | 100   |     | 100 | 100   | 100 |
| Ours(templatematching) |             |     | 100   | 100   |     | 100 | 100   | 100 |
CIMBBank(7UniquePDFs)
| prebuilt- | N/A |     | 71.43 | 73.91 |     | 70.68 | 99.77 | 42.86 |
| --------- | --- | --- | ----- | ----- | --- | ----- | ----- | ----- |
bankStatement.us
| pretrained-read | GPT-4o-mini |     | 100   | 100 |     | 100   | 98.51 | 98.21 |
| --------------- | ----------- | --- | ----- | --- | --- | ----- | ----- | ----- |
| pretrained-read | GPT-4.1     |     | 100   | 100 |     | 100   | 98.51 | 100   |
| AzureAI4.0      | GPT-4o-mini |     | 100   | 100 |     | 100   | 97.59 | 98.21 |
| AzureAI4.0      | GPT-4.1     |     | 100   | 100 |     | 100   | 100   | 100   |
| MinerU          | GPT-4o-mini |     | 5.04  | 100 |     | 96.43 | 98.51 | 100   |
| MinerU          | GPT-4.1     |     | 0     | 100 |     | 100   | 100   | 100   |
| PyMuPDF         | GPT-4o-mini |     | 71.43 | 100 |     | 100   | 98.51 | 98.21 |
| PyMuPDF         | GPT-4.1     |     | 71.43 | 100 |     | 100   | 100   | 100   |
Continuedonnextpage
19

PublishedasaconferencepaperatICLR2026
Table6–Continuedfrompreviouspage
KeyInformationExtraction-NEDScore
| OCR                    | GPT         |          |           |           |         |               |
| ---------------------- | ----------- | -------- | --------- | --------- | ------- | ------------- |
|                        |             | BankName | AccHolder | AccNumber | Address | StatementDate |
| pdfium                 | GPT-4o-mini | 71.43    | 100       | 100       | 98.51   | 100           |
| pdfium                 | GPT-4.1     | 71.43    | 100       | 100       | 100     | 100           |
| Ours(templatematching) |             | 100      | 100       | 100       | 100     | 100           |
RHBBank(10UniquePDFs)
| prebuilt- | N/A | 100 | 90  | 100 | 92.01 | 100 |
| --------- | --- | --- | --- | --- | ----- | --- |
bankStatement.us
| pretrained-read        | GPT-4o-mini | 100   | 100   | 100 | 99.35 | 100   |
| ---------------------- | ----------- | ----- | ----- | --- | ----- | ----- |
| pretrained-read        | GPT-4.1     | 100   | 100   | 100 | 98.92 | 100   |
| AzureAI4.0             | GPT-4o-mini | 100   | 100   | 100 | 100   | 100   |
| AzureAI4.0             | GPT-4.1     | 100   | 100   | 100 | 98.92 | 100   |
| MinerU                 | GPT-4o-mini | 70    | 55.69 | 70  | 40    | 85    |
| MinerU                 | GPT-4.1     | 70    | 50    | 70  | 40    | 77.50 |
| PyMuPDF                | GPT-4o-mini | 93.03 | 100   | 100 | 98.92 | 100   |
| PyMuPDF                | GPT-4.1     | 100   | 100   | 100 | 98.92 | 100   |
| pdfium                 | GPT-4o-mini | 79.09 | 100   | 100 | 98.92 | 100   |
| pdfium                 | GPT-4.1     | 100   | 100   | 100 | 98.92 | 100   |
| Ours(templatematching) |             | 100   | 100   | 100 | 100   | 100   |
HongLeongBank(9UniquePDFs)
| prebuilt- | N/A | 100 | 88.89 | 100 | 100 | 100 |
| --------- | --- | --- | ----- | --- | --- | --- |
bankStatement.us
| pretrained-read        | GPT-4o-mini | 100   | 91.53 | 100 | 100   | 100 |
| ---------------------- | ----------- | ----- | ----- | --- | ----- | --- |
| pretrained-read        | GPT-4.1     | 100   | 100   | 100 | 100   | 100 |
| AzureAI4.0             | GPT-4o-mini | 100   | 91.53 | 100 | 97.99 | 100 |
| AzureAI4.0             | GPT-4.1     | 100   | 100   | 100 | 100   | 100 |
| MinerU                 | GPT-4o-mini | 11.85 | 88.89 | 100 | 100   | 100 |
| MinerU                 | GPT-4.1     | 50.88 | 100   | 100 | 100   | 100 |
| PyMuPDF                | GPT-4o-mini | 100   | 91.50 | 100 | 98.64 | 100 |
| PyMuPDF                | GPT-4.1     | 100   | 100   | 100 | 100   | 100 |
| pdfium                 | GPT-4o-mini | 100   | 91.50 | 100 | 97.80 | 100 |
| pdfium                 | GPT-4.1     | 100   | 100   | 100 | 100   | 100 |
| Ours(templatematching) |             | 100   | 100   | 100 | 100   | 100 |
AmBank(7UniquePDFs)
| prebuilt- | N/A | 100 | 85.71 | 100 | 100 | 100 |
| --------- | --- | --- | ----- | --- | --- | --- |
bankStatement.us
| pretrained-read        | GPT-4o-mini | 100   | 100 | 100 | 100   | 100 |
| ---------------------- | ----------- | ----- | --- | --- | ----- | --- |
| pretrained-read        | GPT-4.1     | 100   | 100 | 100 | 100   | 100 |
| AzureAI4.0             | GPT-4o-mini | 100   | 100 | 100 | 100   | 100 |
| AzureAI4.0             | GPT-4.1     | 100   | 100 | 100 | 100   | 100 |
| MinerU                 | GPT-4o-mini | 14.97 | 100 | 100 | 98.82 | 100 |
| MinerU                 | GPT-4.1     | 0     | 100 | 100 | 98.82 | 100 |
| PyMuPDF                | GPT-4o-mini | 8.57  | 100 | 100 | 100   | 100 |
| PyMuPDF                | GPT-4.1     | 0     | 100 | 100 | 100   | 100 |
| pdfium                 | GPT-4o-mini | 12.38 | 100 | 100 | 100   | 100 |
| pdfium                 | GPT-4.1     | 0     | 100 | 100 | 100   | 100 |
| Ours(templatematching) |             | 100   | 100 | 100 | 100   | 100 |
A.4 QUANTITATIVERESULTSFORTRANSACTIONTABLEEXTRACTION
WeevaluatetransactiontableextractionacrossthesamesixMalaysianbanks. Thistaskissubstantiallymore
challengingthankeyinformationextraction,asitrequireslocalizingtableboundaries,parsingmulti-pagetables
withvaryingrowcounts,andcorrectlyaligningfivecolumntypes:date,description,debit,credit,andbalance.
We report matching NED (tolerance for row-level alignment differences) in Table 8 and exact NED (strict
row-levelmatching)inTable9,F1scoresforrowdetectioninTable7,andper-bankbreakdownsinTables10
and11.
Overall Performance. Our template matching approach achieves the highest or near-highest performance
acrossallmetrics.OnmatchingNED,itattains100%ondateanddescriptioncolumns,91.12%ondebit,100%
20

PublishedasaconferencepaperatICLR2026
on credit, and 99.28% on balance, with an average of 98.08%. For exact NED, it achieves 98.08% (date),
98.35%(description),99.87%(debit),92.68%(credit),and100%(balance). TheF1scoreisaperfect100%
acrossallsixbanks,indicatingthatourmethodcorrectlyidentifiesalltransactionrowswithoutfalsepositives
ormissedentries. TheSurya+docTRpipelinewithGPT-5-miniistheclosestcompetitor,achieving98.95%
matchingNEDondateand96.94%average,withstrongF1scores(98.28–100%)acrossbanks.
LLM-Based vs. End-to-End Approaches. Configurations using GPT-4.1 as the structuring model consis-
tentlyoutperformthoseusingGPT-4o-miniorsmallermodels.Forinstance,docTR+GPT-4.1achieves95.28%
matchingNEDondescription,comparedto92.82%withGPT-4o-mini. Thegapwidensfornumericalfields:
debitmatchingNEDincreasesfrom80.00%(GPT-4o-mini)to98.78%(GPT-4.1)withdocTR.Thisindicates
thatlargerlanguagemodelsarebetteratparsingambiguousnumericalformats(e.g., MalaysianRinggitfor-
mattingwithcommasandperiods)andhandlingmulti-linetransactiondescriptions. Conversely, end-to-end
visionmodelsshowmixedresults.WhileolmOCRachievesreasonablematchingNED(77–91%percolumn),
its exact NED drops substantially (71–84%), indicating frequent minor character-level errors in numerical
fields. PPStructureV3andPaddleOCR-VL(0.9B)demonstratetheweakestoverallperformance,particularly
onbalancecolumns(43.79%and53.44%matchingNEDrespectively),likelyduetotheirlimitedtrainingon
SoutheastAsianfinancialdocumentformats.
Per-BankAnalysis. Performancevariesacrossbanksduetodifferencesinstatementformatting. PublicBank
statements,withtheircleantabularlayouts,achievenear-perfectextractionacrossmostconfigurations(100%
matchingNEDforourmethod).Incontrast,RHBBank’smulti-columnbalancepresentationandCIMBBank’s
merged description cells present greater challenges, reducing baseline performance by 5–15% on average.
HongLeongBankstatementswithwrappedtransactiondescriptionscausethelargestperformancedropsfor
text-basedextractors(PyMuPDF+GPT-4o-minidropsto70.91%datematchingNED).Thesebank-specific
challengesvalidatetheneedforrobustextractionpipelinesthatcangeneralizeacrossdiverseformats.
F1ScoreAnalysis. Row-leveldetectionaccuracy,measuredbyF1score(Table7),revealsthatourtemplate
matchingmethodandGPT-4.1-basedconfigurationsachievenear-perfectrowdetection(98–100%F1across
banks).PaddleOCR-basedmethodsshowthemostinconsistency,withF1scoresdroppingto10.26%onCIMB
Bankand14.29%onMaybankforPPStructureV3, indicatingcatastrophictabledetectionfailuresoncertain
bankformats. Thishighlightstheunreliabilityofgeneral-purposetabledetectionmodelsforproductionde-
ploymentonMalaysianbankstatementswithoutformat-specificadaptation.
Table7: F1scoresacrossallbanksfortransactiontableextraction.
| OCR                | GPT             | MBBE  | PBBE CIBB RHBB     | HLBB ARBK     |
| ------------------ | --------------- | ----- | ------------------ | ------------- |
| prebuilt-layout    | N/A             | 93.67 | 89.47 97.41 81.60  | 99.58 100.00  |
| PPStructureV3      | N/A             | 14.29 | 70.97 10.26 23.19  | 80.89 92.12   |
| docTR              | gpt-4o-mini     | 92.73 | 88.70 87.37 100.00 | 85.34 98.81   |
| docTR              | gpt-4.1         | 96.04 | 90.09 98.95 100.00 | 100.00 100.00 |
| docTR              | gpt-4.1-mini    | 91.74 | 97.30 81.14 88.24  | 91.38 96.93   |
| docTR              | gpt-4.1-nano    | 36.11 | 73.87 71.79 96.49  | 83.19 93.26   |
| docTR              | gpt-5-mini      | 98.71 | 96.43 100.00 94.74 | 91.21 100.00  |
| docTR              | gpt-5-mini(low) | 94.64 | 100.00 95.70 85.96 | 90.35 96.34   |
| docTR              | gpt-5-nano      | 94.64 | 91.89 98.95 66.67  | 68.38 97.01   |
| PyMuPDF            | gpt-4o-mini     | 94.64 | 89.26 87.18 100.00 | 76.19 98.20   |
| PyMuPDF            | gpt-4.1         | 94.69 | 92.59 98.95 100.00 | 99.58 100.00  |
| pdfium             | gpt-4o-mini     | 94.17 | 88.52 80.77 98.25  | 79.65 96.43   |
| pdfium             | gpt-4.1         | 93.75 | 83.64 99.47 100.00 | 98.31 98.81   |
| olmOCR-2-7B-1025   | N/A             | 87.93 | 63.04 100.00 73.68 | 83.84 98.20   |
| paddleOCR-VL(0.9B) | N/A             | 61.31 | 61.18 17.89 22.22  | 64.16 95.65   |
Surya+docTR gpt-5-mini(header) 100.00 100.00 98.96 98.28 99.15 100.00
| Ours(templatematching) |     | 100.00 | 100.00 100.00 100.00 | 100.00 100.00 |
| ---------------------- | --- | ------ | -------------------- | ------------- |
Table8:Averageper-columnmatchingNEDscoresacrossallbanksfortransactiontableextraction.
TransactionTableExtraction-MatchingNEDScore
| OCR             | GPT |             |              |         |
| --------------- | --- | ----------- | ------------ | ------- |
|                 |     | Date Desc   | Debit Credit | Balance |
| prebuilt-layout | N/A | 89.59 95.54 | 95.88 98.31  | 94.15   |
| PPStructureV3   | N/A | 63.29 66.43 | 74.30 82.56  | 43.79   |
Continuedonnextpage
21

PublishedasaconferencepaperatICLR2026
Table8–Continuedfrompreviouspage
TransactionTableExtraction-MatchingNEDScore
| OCR              |     | GPT             |             |              |         |
| ---------------- | --- | --------------- | ----------- | ------------ | ------- |
|                  |     |                 | Date Desc   | Debit Credit | Balance |
| docTR            |     | gpt-4o-mini     | 86.41 92.82 | 80.00 86.07  | 96.76   |
| docTR            |     | gpt-4.1         | 88.05 95.28 | 98.78 96.65  | 95.72   |
| docTR            |     | gpt-4.1-mini    | 88.48 94.60 | 86.79 91.85  | 94.66   |
| docTR            |     | gpt-4.1-nano    | 84.87 78.88 | 80.02 78.64  | 73.55   |
| docTR            |     | gpt-5-mini      | 86.64 97.73 | 93.74 94.78  | 96.00   |
| docTR            |     | gpt-5-mini(low) | 80.44 95.81 | 87.10 90.94  | 88.77   |
| docTR            |     | gpt-5-nano      | 82.65 90.68 | 79.31 80.05  | 92.55   |
| PyMuPDF          |     | gpt-4o-mini     | 88.45 93.29 | 86.07 88.72  | 95.17   |
| PyMuPDF          |     | gpt-4.1         | 87.13 95.79 | 97.80 97.08  | 96.02   |
| pdfium           |     | gpt-4o-mini     | 88.48 91.66 | 85.32 87.95  | 93.26   |
| pdfium           |     | gpt-4.1         | 88.08 92.85 | 99.69 95.03  | 93.46   |
| olmOCR-2-7B-1025 |     | N/A             | 82.94 90.53 | 82.58 79.08  | 77.87   |
| paddleOCR-VL     |     | N/A             | 79.18 58.94 | 69.44 80.67  | 53.44   |
(0.9B)
| Surya+docTR |     | gpt-5-mini | 98.95 98.59 | 90.79 97.97 | 98.39 |
| ----------- | --- | ---------- | ----------- | ----------- | ----- |
(header)
|     | Ours(templatematching) |     | 100 100 | 91.12 100 | 99.28 |
| --- | ---------------------- | --- | ------- | --------- | ----- |
Table9: Averageper-columnexactNEDscoresacrossallbanksfortransactiontableextraction.
TransactionTableExtraction-ExactNEDScore
| OCR              |     | GPT             |       |                   |         |
| ---------------- | --- | --------------- | ----- | ----------------- | ------- |
|                  |     |                 | Date  | Desc Debit Credit | Balance |
| prebuilt-layout  |     | N/A             | 83.52 | 75.34 89.29 94.29 | 78.31   |
| PPStructureV3    |     | N/A             | 55.79 | 42.70 58.65 72.54 | 47.19   |
| docTR            |     | gpt-4o-mini     | 83.83 | 79.91 68.45 82.04 | 78.35   |
| docTR            |     | gpt-4.1         | 85.42 | 92.80 98.95 98.35 | 96.72   |
| docTR            |     | gpt-4.1-mini    | 79.12 | 70.17 60.73 72.03 | 57.50   |
| docTR            |     | gpt-4.1-nano    | 75.73 | 54.52 63.43 70.45 | 56.24   |
| docTR            |     | gpt-5-mini      | 83.08 | 91.30 92.14 95.15 | 94.97   |
| docTR            |     | gpt-5-mini(low) | 74.88 | 71.20 65.70 72.59 | 59.10   |
| docTR            |     | gpt-5-nano      | 79.01 | 80.45 77.38 76.08 | 84.06   |
| PyMuPDF          |     | gpt-4o-mini     | 81.36 | 70.96 71.08 78.31 | 72.17   |
| PyMuPDF          |     | gpt-4.1         | 85.15 | 93.19 96.32 98.48 | 94.33   |
| pdfium           |     | gpt-4o-mini     | 83.03 | 75.67 74.08 81.01 | 77.19   |
| pdfium           |     | gpt-4.1         | 84.96 | 86.32 95.32 93.41 | 88.13   |
| olmOCR-2-7B-1025 |     | N/A             | 84.18 | 76.51 71.42 77.04 | 71.11   |
| paddleOCR-VL     |     | N/A             | 65.86 | 41.18 55.70 62.36 | 40.58   |
(0.9B)
| Surya+docTR |     | gpt-5-mini | 89.76 | 94.80 95.01 96.91 | 94.65 |
| ----------- | --- | ---------- | ----- | ----------------- | ----- |
(header)
|     | Ours(templatematching) |     | 98.08 | 98.35 99.87 92.68 | 100 |
| --- | ---------------------- | --- | ----- | ----------------- | --- |
Table10: TransactiontableextractionmatchingNEDgroupedbybankacrossOCRandGPTcon-
figurations.
TransactionTableExtraction-MatchingNEDScore
| OCR |     | GPT |                  |              |                 |
| --- | --- | --- | ---------------- | ------------ | --------------- |
|     |     |     | Date Description | Debit Credit | Balance Average |
Maybank(10UniquePDFs)
| prebuilt-layout |     | N/A         | 98.61  | 95.77 94.44 99.21   | 91.27 95.86 |
| --------------- | --- | ----------- | ------ | ------------------- | ----------- |
| PPStructureV3   |     | N/A         | 59.92  | 54.19 70.45 89.47   | 7.69 56.34  |
| PyMuPDF         |     | gpt-4o-mini | 85.59  | 91.16 88.98 97.46   | 89.83 90.60 |
| PyMuPDF         |     | gpt-4.1     | 100.00 | 95.64 100.00 100.00 | 92.37 97.60 |
Continuedonnextpage
22

PublishedasaconferencepaperatICLR2026
Table10–Continuedfrompreviouspage
TransactionTableExtraction-MatchingNEDScore
| OCR                | GPT         |                  |              |                 |
| ------------------ | ----------- | ---------------- | ------------ | --------------- |
|                    |             | Date Description | Debit Credit | Balance Average |
| pdfium             | gpt-4o-mini | 83.90 90.02      | 88.14 96.61  | 88.14 89.36     |
| pdfium             | gpt-4.1     | 81.92 57.24      | 61.02 37.85  | 22.03 52.01     |
| olmOCR-2-7B-1025   | N/A         | 100.00 98.39     | 99.15 99.15  | 95.76 98.49     |
| paddleOCR-VL(0.9B) | N/A         | 83.90 93.39      | 91.53 98.31  | 93.22 92.07     |
| Surya+docTR        | gpt-5-mini  | 97.46 93.96      | 98.31 99.15  | 89.83 95.74     |
| docTR              | gpt-4o-mini | 85.59 93.39      | 92.37 97.46  | 93.22 92.41     |
| docTR              | gpt-4.1     | 94.12 93.28      | 95.80 98.32  | 91.60 94.62     |
| docTR              | gpt-4o-mini | 85.59 92.80      | 92.37 96.61  | 92.37 91.95     |
| docTR              | gpt-4.1     | 95.60 92.16      | 99.16 98.32  | 89.92 95.03     |
| olmOCR-2-7B-1025   | N/A         | 73.37 85.79      | 92.31 88.46  | 78.46 83.68     |
| paddleOCR-VL(0.9B) | N/A         | 90.63 60.63      | 55.79 70.53  | 50.53 65.62     |
Surya+docTR gpt-5-mini(header) 100.00 100.00 90.66 100.00 99.83 98.10
Ours(templatematching) 100.00 100.00 90.66 100.00 99.25 97.98
PublicBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 100.00 100.00 | 90.62 90.62  | 100.00 96.25 |
| ------------------ | ----------- | ------------- | ------------ | ------------ |
| PPStructureV3      | N/A         | 98.40 73.61   | 96.00 96.00  | 66.00 86.00  |
| PyMuPDF            | gpt-4o-mini | 89.06 91.60   | 82.81 85.94  | 93.75 88.63  |
| PyMuPDF            | gpt-4.1     | 70.49 81.92   | 100.00 81.97 | 81.97 83.27  |
| pdfium             | gpt-4o-mini | 92.98 97.75   | 87.72 87.72  | 98.25 92.88  |
| pdfium             | gpt-4.1     | 88.57 70.10   | 81.43 78.57  | 81.43 80.02  |
| olmOCR-2-7B-1025   | N/A         | 62.41 95.35   | 100.00 94.83 | 93.10 89.14  |
| paddleOCR-VL(0.9B) | N/A         | 44.64 99.20   | 98.21 98.21  | 100.00 88.05 |
| Surya+docTR        | gpt-5-mini  | 46.67 93.36   | 88.33 86.67  | 95.00 82.01  |
| docTR              | gpt-4o-mini | 98.51 91.00   | 89.55 89.55  | 92.54 92.23  |
| docTR              | gpt-4.1     | 70.69 86.21   | 93.10 86.21  | 86.21 84.48  |
| docTR              | gpt-4o-mini | 98.53 90.00   | 88.24 89.71  | 89.71 91.24  |
| docTR              | gpt-4.1     | 78.12 71.88   | 100.00 71.88 | 71.88 78.75  |
| olmOCR-2-7B-1025   | N/A         | 67.62 71.74   | 87.30 63.49  | 47.62 67.55  |
| paddleOCR-VL(0.9B) | N/A         | 89.49 64.53   | 94.07 97.46  | 55.93 80.30  |
Surya+docTR gpt-5-mini(header) 100.00 100.00 100.00 100.00 100.00 100.00
Ours(templatematching) 100.00 100.00 100.00 100.00 100.00 100.00
CIMBBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 96.94 98.50  | 95.92 100.00 | 95.92 97.45  |
| ------------------ | ----------- | ------------ | ------------ | ------------ |
| PPStructureV3      | N/A         | 45.25 59.69  | 66.49 48.65  | 8.11 45.64   |
| PyMuPDF            | gpt-4o-mini | 90.57 85.03  | 71.03 71.03  | 100.00 83.53 |
| PyMuPDF            | gpt-4.1     | 97.92 97.91  | 97.92 97.92  | 100.00 98.33 |
| pdfium             | gpt-4o-mini | 96.74 92.53  | 75.00 78.26  | 96.74 87.85  |
| pdfium             | gpt-4.1     | 95.60 70.81  | 87.33 86.67  | 61.33 80.35  |
| olmOCR-2-7B-1025   | N/A         | 100.00 99.86 | 93.68 93.68  | 100.00 97.45 |
| paddleOCR-VL(0.9B) | N/A         | 93.81 94.98  | 79.38 83.51  | 93.81 89.10  |
| Surya+docTR        | gpt-5-mini  | 100.00 98.85 | 70.83 69.79  | 100.00 87.90 |
| docTR              | gpt-4o-mini | 92.55 85.97  | 79.09 78.18  | 92.73 85.70  |
| docTR              | gpt-4.1     | 97.92 97.92  | 97.92 97.92  | 100.00 98.33 |
| docTR              | gpt-4o-mini | 93.39 80.17  | 79.03 79.03  | 84.68 83.26  |
| docTR              | gpt-4.1     | 98.95 99.29  | 98.95 100.00 | 98.95 99.23  |
| olmOCR-2-7B-1025   | N/A         | 94.74 100.00 | 85.26 85.26  | 94.74 92.00  |
| paddleOCR-VL(0.9B) | N/A         | 54.91 58.73  | 77.46 77.46  | 9.83 55.68   |
Surya+docTR gpt-5-mini(header) 97.94 100.00 97.94 97.94 98.96 98.56
Ours(templatematching) 100.00 100.00 96.21 100.00 97.18 98.68
RHBBank(10UniquePDFs)
| prebuilt-layout | N/A         | 71.36 80.45 | 94.29 100.00 | 78.57 84.93  |
| --------------- | ----------- | ----------- | ------------ | ------------ |
| PPStructureV3   | N/A         | 16.10 45.22 | 48.36 71.31  | 17.21 39.64  |
| PyMuPDF         | gpt-4o-mini | 89.39 94.97 | 66.67 87.72  | 100.00 87.75 |
| PyMuPDF         | gpt-4.1     | 89.39 98.87 | 94.74 100.00 | 100.00 96.60 |
| pdfium          | gpt-4o-mini | 86.57 98.57 | 88.89 100.00 | 95.56 93.92  |
| pdfium          | gpt-4.1     | 89.41 89.03 | 88.14 94.92  | 100.00 92.30 |
Continuedonnextpage
23

PublishedasaconferencepaperatICLR2026
Table10–Continuedfrompreviouspage
TransactionTableExtraction-MatchingNEDScore
| OCR                | GPT         |                  |               |                 |
| ------------------ | ----------- | ---------------- | ------------- | --------------- |
|                    |             | Date Description | Debit Credit  | Balance Average |
| olmOCR-2-7B-1025   | N/A         | 89.42 98.28      | 85.00 93.33   | 88.33 90.87     |
| paddleOCR-VL(0.9B) | N/A         | 89.54 97.91      | 75.38 81.54   | 73.85 83.64     |
| Surya+docTR        | gpt-5-mini  | 91.05 72.65      | 56.58 59.21   | 93.42 74.58     |
| docTR              | gpt-4o-mini | 89.39 98.44      | 100.00 100.00 | 100.00 97.57    |
| docTR              | gpt-4.1     | 89.39 98.87      | 100.00 100.00 | 100.00 97.65    |
| docTR              | gpt-4o-mini | 89.58 97.09      | 91.38 91.38   | 100.00 93.88    |
| docTR              | gpt-4.1     | 89.39 98.99      | 100.00 100.00 | 100.00 97.68    |
| olmOCR-2-7B-1025   | N/A         | 91.46 93.84      | 59.72 62.50   | 56.94 72.89     |
| paddleOCR-VL(0.9B) | N/A         | 70.39 14.09      | 35.16 60.16   | 14.06 38.77     |
Surya+docTR gpt-5-mini(header) 96.61 93.22 86.36 91.53 95.58 92.66
Ours(templatematching) 100.00 100.00 89.39 100.00 99.74 97.83
HongLeongBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 78.98 98.54 | 100.00 100.00 | 99.16 95.34  |
| ------------------ | ----------- | ----------- | ------------- | ------------ |
| PPStructureV3      | N/A         | 70.12 71.14 | 76.87 95.52   | 80.60 78.85  |
| PyMuPDF            | gpt-4o-mini | 70.91 94.57 | 75.19 78.95   | 96.99 83.32  |
| PyMuPDF            | gpt-4.1     | 78.80 97.32 | 100.00 100.00 | 100.00 95.22 |
| pdfium             | gpt-4o-mini | 73.09 92.71 | 88.10 92.06   | 95.24 88.24  |
| pdfium             | gpt-4.1     | 71.58 90.91 | 72.73 78.03   | 76.52 77.95  |
| olmOCR-2-7B-1025   | N/A         | 76.31 94.52 | 84.62 87.69   | 100.00 88.63 |
| paddleOCR-VL(0.9B) | N/A         | 70.74 92.94 | 84.00 88.80   | 77.60 82.82  |
| Surya+docTR        | gpt-5-mini  | 70.02 87.27 | 62.99 70.13   | 80.52 74.19  |
| docTR              | gpt-4o-mini | 71.70 92.91 | 60.14 70.63   | 93.71 77.82  |
| docTR              | gpt-4.1     | 78.98 98.46 | 100.00 100.00 | 98.32 95.15  |
| docTR              | gpt-4o-mini | 71.85 92.67 | 65.47 75.54   | 92.81 79.67  |
| docTR              | gpt-4.1     | 75.82 95.99 | 100.00 100.00 | 100.00 94.36 |
| olmOCR-2-7B-1025   | N/A         | 70.42 92.57 | 74.44 75.94   | 89.47 80.57  |
| paddleOCR-VL(0.9B) | N/A         | 69.65 59.63 | 61.28 79.57   | 97.45 73.51  |
Surya+docTR gpt-5-mini(header) 99.16 98.32 78.08 98.32 96.36 94.05
Ours(templatematching) 100.00 100.00 78.80 100.00 99.48 95.65
AmBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 91.67 100.00 | 100.00 100.00 | 100.00 98.33 |
| ------------------ | ----------- | ------------ | ------------- | ------------ |
| PPStructureV3      | N/A         | 89.92 94.73  | 87.64 94.38   | 83.15 89.96  |
| PyMuPDF            | gpt-4o-mini | 92.94 99.58  | 95.29 95.29   | 100.00 96.62 |
| PyMuPDF            | gpt-4.1     | 91.67 100.00 | 100.00 100.00 | 100.00 98.33 |
| pdfium             | gpt-4o-mini | 97.62 96.02  | 92.86 96.43   | 94.05 95.39  |
| pdfium             | gpt-4.1     | 82.11 95.17  | 89.47 95.79   | 100.00 92.51 |
| olmOCR-2-7B-1025   | N/A         | 91.67 100.00 | 100.00 100.00 | 98.81 98.10  |
| paddleOCR-VL(0.9B) | N/A         | 100.00 96.42 | 94.12 95.29   | 94.12 95.99  |
| Surya+docTR        | gpt-5-mini  | 90.70 97.98  | 98.84 95.35   | 96.51 95.88  |
| docTR              | gpt-4o-mini | 92.94 98.04  | 95.29 96.47   | 98.82 96.31  |
| docTR              | gpt-4.1     | 91.67 100.00 | 100.00 100.00 | 100.00 98.33 |
| docTR              | gpt-4o-mini | 91.95 97.25  | 95.40 95.40   | 100.00 96.00 |
| docTR              | gpt-4.1     | 90.59 98.80  | 100.00 100.00 | 100.00 97.88 |
| olmOCR-2-7B-1025   | N/A         | 100.00 99.24 | 96.47 98.82   | 100.00 98.91 |
| paddleOCR-VL(0.9B) | N/A         | 100.00 96.00 | 92.86 98.81   | 92.86 96.11  |
Surya+docTR gpt-5-mini(header) 100.00 100.00 91.67 100.00 99.58 98.25
Ours(templatematching) 100.00 100.00 91.67 100.00 100.00 98.33
24

PublishedasaconferencepaperatICLR2026
Table11: TransactiontableextractionexactNEDgroupedbybankacrossOCRandGPTconfigu-
rations.
TransactionTableExtraction-ExactNEDScore
| OCR | GPT |                  |              |                 |
| --- | --- | ---------------- | ------------ | --------------- |
|     |     | Date Description | Debit Credit | Balance Average |
Maybank(10UniquePDFs)
| prebuilt-layout        | N/A                | 75.71 78.84 | 81.19 93.02 | 71.99 80.15 |
| ---------------------- | ------------------ | ----------- | ----------- | ----------- |
| PPStructureV3          | N/A                | 24.25 57.78 | 39.86 84.39 | 13.33 43.92 |
| PyMuPDF                | gpt-4o-mini        | 74.34 66.66 | 60.56 73.39 | 40 62.99    |
| PyMuPDF                | gpt-4.1            | 87.49 87.89 | 90.91 97.41 | 82.31 89.20 |
| pdfium                 | gpt-4o-mini        | 75.77 71.55 | 70.56 76.25 | 50 68.83    |
| pdfium                 | gpt-4.1            | 84.64 77.7  | 78.6 86.95  | 63.08 78.19 |
| olmOCR-2-7B-1025       | N/A                | 70.45 73.71 | 62.73 78.11 | 53.68 67.74 |
| paddleOCR-VL(0.9B)     | N/A                | 57.59 41.18 | 61.99 71.1  | 49.21 56.21 |
| Surya+docTR            | gpt-5-mini(header) | 90.07 99.16 | 100 100     | 100 97.85   |
| Ours(templatematching) |                    | 90.07 99.24 | 100 100     | 100 97.86   |
PublicBank(10UniquePDFs)
| prebuilt-layout        | N/A                | 94.39 25.27 | 85.36 89.82 | 41.94 67.36 |
| ---------------------- | ------------------ | ----------- | ----------- | ----------- |
| PPStructureV3          | N/A                | 91.39 15.05 | 82.74 90.28 | 30.28 61.95 |
| PyMuPDF                | gpt-4o-mini        | 89.17 67.78 | 68.39 85.42 | 70.47 76.25 |
| PyMuPDF                | gpt-4.1            | 72.14 89.91 | 93.33 96.67 | 90 88.41    |
| pdfium                 | gpt-4o-mini        | 94.44 64.97 | 67.97 85.56 | 70.2 76.63  |
| pdfium                 | gpt-4.1            | 75.14 79.91 | 100 84      | 80 83.81    |
| olmOCR-2-7B-1025       | N/A                | 93.52 48.11 | 85.71 65.81 | 48.26 68.28 |
| paddleOCR-VL(0.9B)     | N/A                | 82.15 21.84 | 79.17 81.74 | 51.48 63.28 |
| Surya+docTR            | gpt-5-mini(header) | 100 99.46   | 100 100     | 100 99.89   |
| Ours(templatematching) |                    | 100 100     | 100 100     | 100 100     |
CIMBBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 88.69 85.53 | 87.94 90.48 | 83.18 87.16 |
| ------------------ | ----------- | ----------- | ----------- | ----------- |
| PPStructureV3      | N/A         | 32.12 38.08 | 50.24 41.41 | 23.41 37.05 |
| PyMuPDF            | gpt-4o-mini | 90.77 75.35 | 76.47 82.75 | 90.86 83.24 |
| PyMuPDF            | gpt-4.1     | 98.81 97.27 | 98.41 98.41 | 100 98.58   |
| pdfium             | gpt-4o-mini | 84.63 65.63 | 71.48 73.49 | 78.42 74.73 |
| pdfium             | gpt-4.1     | 97.62 90.02 | 93.33 89.52 | 85.71 91.24 |
| olmOCR-2-7B-1025   | N/A         | 95.56 98.32 | 85.95 85.95 | 93.62 91.88 |
| paddleOCR-VL(0.9B) | N/A         | 33.01 78.28 | 66.51 66.5  | 28.57 54.58 |
Surya+docTR gpt-5-mini(header) 91.09 83.2 77.55 89.8 70.68 82.47
| Ours(templatematching) |     | 91.43 95.22 | 100 100 | 100 97.33 |
| ---------------------- | --- | ----------- | ------- | --------- |
RHBBank(10UniquePDFs)
| prebuilt-layout    | N/A         | 73.66 66.77 | 86.36 92.42 | 72.73 78.39 |
| ------------------ | ----------- | ----------- | ----------- | ----------- |
| PPStructureV3      | N/A         | 49.35 21.28 | 63.21 81.24 | 49.23 52.86 |
| PyMuPDF            | gpt-4o-mini | 84.02 79.69 | 97.22 97.22 | 100 91.63   |
| PyMuPDF            | gpt-4.1     | 84.02 88.69 | 100 100     | 100 94.54   |
| pdfium             | gpt-4o-mini | 84.02 87.71 | 91.94 91.94 | 100 91.12   |
| pdfium             | gpt-4.1     | 84.02 73.51 | 100 100     | 100 91.5    |
| olmOCR-2-7B-1025   | N/A         | 84.02 90.75 | 78.05 76.67 | 76.67 81.23 |
| paddleOCR-VL(0.9B) | N/A         | 87.3 12.56  | 31.12 34.84 | 26.13 38.39 |
Surya+docTR gpt-5-mini(header) 88.19 97.42 92.5 91.67 98.61 93.68
| Ours(templatematching) |     | 84.02 99.53 | 100 100 | 100 96.71 |
| ---------------------- | --- | ----------- | ------- | --------- |
HongLeongBank(10UniquePDFs)
| prebuilt-layout  | N/A         | 77.05 95.7  | 94.87 100   | 100 93.53   |
| ---------------- | ----------- | ----------- | ----------- | ----------- |
| PPStructureV3    | N/A         | 51.35 48.21 | 33.54 59.51 | 67.87 52.09 |
| PyMuPDF          | gpt-4o-mini | 63.65 56.72 | 41.78 43.37 | 55.28 52.16 |
| PyMuPDF          | gpt-4.1     | 76.82 95.36 | 95.24 98.41 | 93.65 91.9  |
| pdfium           | gpt-4o-mini | 65.3 66.6   | 46.33 62.65 | 64.54 61.08 |
| pdfium           | gpt-4.1     | 76.71 97.58 | 100 100     | 100 94.86   |
| olmOCR-2-7B-1025 | N/A         | 63.84 57.34 | 31.29 61.15 | 64.43 55.61 |
Continuedonnextpage
25

PublishedasaconferencepaperatICLR2026
Table11–Continuedfrompreviouspage
TransactionTableExtraction-ExactNEDScore
| OCR                |     | GPT |       |             |              |                 |
| ------------------ | --- | --- | ----- | ----------- | ------------ | --------------- |
|                    |     |     | Date  | Description | Debit Credit | Balance Average |
| paddleOCR-VL(0.9B) |     | N/A | 46.95 | 47.44       | 76.48 83.72  | 86.88 68.3      |
Surya+docTR gpt-5-mini(header) 77.6 95.51 100 100 98.61 94.34
|     | Ours(templatematching) |     | 78.33 | 99.47 | 100 100 | 100 95.56 |
| --- | ---------------------- | --- | ----- | ----- | ------- | --------- |
AmBank(10UniquePDFs)
| prebuilt-layout    |                        | N/A                | 91.61 | 99.91 | 100 100     | 100 98.3    |
| ------------------ | ---------------------- | ------------------ | ----- | ----- | ----------- | ----------- |
| PPStructureV3      |                        | N/A                | 86.27 | 75.79 | 82.53 83.96 | 75.27 80.77 |
| PyMuPDF            |                        | gpt-4o-mini        | 86.18 | 79.54 | 82.04 87.69 | 76.4 82.37  |
| PyMuPDF            |                        | gpt-4.1            | 91.61 | 100   | 100 100     | 100 98.32   |
| pdfium             |                        | gpt-4o-mini        | 93.99 | 97.58 | 96.19 96.19 | 100 96.79   |
| pdfium             |                        | gpt-4.1            | 91.61 | 99.18 | 100 100     | 100 98.16   |
| olmOCR-2-7B-1025   |                        | N/A                | 97.71 | 90.81 | 84.76 94.52 | 90 91.56    |
| paddleOCR-VL(0.9B) |                        | N/A                | 88.17 | 45.76 | 18.92 36.28 | 1.19 38.07  |
| Surya+docTR        |                        | gpt-5-mini(header) | 91.61 | 94.03 | 100 100     | 100 97.13   |
|                    | Ours(templatematching) |                    | 91.61 | 100   | 100 100     | 100 98.32   |
A.5 LATENCYANDCOSTANALYSIS
Practicaldeploymentofbankstatementextractionsystemsrequirescarefulconsiderationofprocessinglatency
and operational cost. We provide latency measurements for both key information extraction (Table 12) and
transaction table extraction (Table 13), along with cost analysis for table extraction (Table 14). All latency
measurementsarereportedinsecondsperdocument,decomposedintoOCRprocessingtimeandGPTinference
timewhereapplicable.
|     | Table12: | Latencyanalysisforkeyinformationextraction(seconds). |           |      |                |                |
| --- | -------- | ---------------------------------------------------- | --------- | ---- | -------------- | -------------- |
|     |          |                                                      | OCR       |      | GPT            | Total          |
| OCR |          | GPT                                                  |           |      |                |                |
|     |          |                                                      | Min. Avg. | Max. | Min. Avg. Max. | Min. Avg. Max. |
Prebuilt-BankStatement.us N/A N/A N/A N/A N/A N/A N/A 5.26 9.28 17.27
Pretrained-Read gpt-4o-mini 1.64 3.26 6.07 0.88 1.70 3.64 2.52 4.96 7.90
Pretrained-Read gpt-4.1 1.61 2.87 5.15 0.59 0.96 4.16 2.34 3.83 7.07
AzureAI4.0 gpt-4o-mini 1.03 1.71 3.41 1.12 1.71 3.41 2.37 3.34 5.01
AzureAI4.0 gpt-4.1 1.01 1.42 2.35 0.63 1.09 3.65 1.86 2.72 5.50
docTR gpt-4o-mini 0.32 0.63 1.31 1.00 1.75 5.49 1.34 2.38 6.51
| docTR |     | gpt-4.1 | 2.96 5.20 | 7.59 | 0.54 0.94 2.93 | 3.58 6.13 8.56 |
| ----- | --- | ------- | --------- | ---- | -------------- | -------------- |
MinerU gpt-4o-mini 28.69 32.18 38.72 1.27 2.05 3.62 30.10 34.24 41.88
MinerU gpt-4.1 33.51 44.32 55.03 0.83 1.18 8.40 34.38 45.50 60.62
PyMuPDF gpt-4o-mini 0.00 0.02 0.04 0.95 1.85 3.89 0.97 1.86 3.92
| PyMuPDF |     | gpt-4.1 | 0.00 0.01 | 0.04 | 0.56 0.80 1.46 | 0.57 0.81 1.47 |
| ------- | --- | ------- | --------- | ---- | -------------- | -------------- |
PyMuPDF-Formatted gpt-4o-mini 0.01 0.02 0.05 0.85 1.50 6.08 0.87 1.53 6.10
PyMuPDF-Formatted gpt-4.1 0.00 0.02 0.06 0.53 0.72 1.36 0.55 0.74 1.39
Pdfium gpt-4o-mini 0.00 0.02 0.09 0.95 1.84 4.91 0.97 1.86 4.92
| Pdfium |     | gpt-4.1 | 0.00 0.01 | 0.03 | 0.54 0.85 1.66 | 0.55 0.86 1.67 |
| ------ | --- | ------- | --------- | ---- | -------------- | -------------- |
Ours(templatematching) 0.01 0.01 0.01 N/A N/A N/A 0.01 0.01 0.01
Key Information Extraction Latency. The latency profiles for key information extraction (Table 12) re-
veal substantial variation across pipeline configurations. Text-based extractors (PyMuPDF, Pdfium) achieve
near-instantaneousOCRprocessing(0.01–0.02saverage),withtotallatencydominatedbytheGPTinference
component. PyMuPDF + GPT-4.1 achieves the lowest average total latency at 0.81 seconds, followed by
PyMuPDF-Formatted+GPT-4.1at0.74seconds. Ourtemplatematchingmethodaverages0.01secondsper
document,makingitthefastestconfigurationoverallwhileeliminatingdependencyonexternalAPIs. Cloud-
basedOCRsolutionsintroducehigherlatency: Pretrained-Readaverages2.87–3.26secondsforOCRalone,
whileMinerUexhibitsthehighestlatencyat34–45secondsaverageduetoitscomputationallyintensivedoc-
umentunderstandingpipeline.ThePrebuilt-BankStatementendpoint(Azure’sturnkeysolution)averages9.28
secondstotalbutdoesnotexposeseparateOCR/GPTcomponents. DocTRpresentsaninterestingtrade-off:
itsOCRcomponentisfast(0.63saveragewithGPT-4o-mini)butincreasessubstantiallywithGPT-4.1(5.20s),
suggestingthattherenderingandimagepreparationstepscaleswithdownstreammodelexpectations.
26

PublishedasaconferencepaperatICLR2026
Table13: Latencyanalysisfortransactiontableextraction(seconds).
|                 |     |      | OCR  |      | GPT       |           | Total |       |
| --------------- | --- | ---- | ---- | ---- | --------- | --------- | ----- | ----- |
| OCR             | GPT |      |      |      |           |           |       |       |
|                 |     | Min. | Avg. | Max. | Min. Avg. | Max. Min. | Avg.  | Max.  |
| prebuilt-layout | N/A | N/A  | N/A  | N/A  | N/A N/A   | N/A 2.56  | 4.58  | 7.46  |
| PPStructureV3   | N/A | N/A  | N/A  | N/A  | N/A N/A   | N/A 15.26 | 40.95 | 98.17 |
docTR gpt-4o-mini 0.78 1.18 1.59 1.32 6.41 14.83 2.30 7.59 15.93
docTR gpt-4.1 0.34 0.89 1.56 0.89 11.03 153.16 2.07 11.92 153.50
docTR gpt-4.1-mini 0.57 0.96 1.60 1.12 5.38 12.47 2.08 6.33 13.51
docTR gpt-4.1-nano 0.28 0.67 1.02 1.14 3.13 6.59 1.76 3.80 7.31
docTR gpt-5-mini 0.30 0.74 1.19 11.15 24.54 54.64 11.70 25.27 55.20
docTR gpt-5-mini(low) 0.66 1.07 1.54 1.48 5.77 11.64 2.74 6.84 12.93
docTR gpt-5-nano 0.36 0.87 1.76 7.47 31.51 60.65 8.07 32.38 61.23
PyMuPDF gpt-4o-mini 0.00 0.01 0.04 1.08 4.97 12.12 1.09 4.98 12.13
PyMuPDF gpt-4.1 0.00 0.01 0.05 0.84 10.72 157.78 0.85 10.72 157.79
pdfium gpt-4o-mini 0.00 0.02 0.04 1.36 6.19 16.90 1.39 6.21 16.92
pdfium gpt-4.1 0.00 0.02 0.04 0.77 11.17 155.22 0.79 11.19 155.23
olmOCR-2-7B-1025 N/A N/A N/A N/A N/A N/A N/A 42.58 104.45 175.93
paddleOCR-VL(0.9B) N/A 23.20 150.10 341.10 N/A N/A N/A 23.20 150.10 341.10
Surya+docTR gpt-5-mini(header) 2.26 4.28 7.34 0.75 1.19 1.85 1.67 2.51 9.19
Ours(templatematching) 0.10 0.11 0.13 N/A N/A N/A 0.10 0.11 0.13
TransactionTableExtractionLatency.Tableextractionlatency(Table13)isgenerallyhigherthankeyinfor-
mationextractionduetotheincreasedcomplexityofparsingmulti-pagetabulardata. Ourtemplatematching
methodachievesthefastestaveragetotallatencyat0.11seconds,followedbytheSurya+docTRpipelineat
2.51secondsandtheprebuilt-layoutAPIat4.58seconds. GPT-4.1-basedconfigurationsexhibithighlatency
variancewithmaximumprocessingtimesreaching153–158secondsforcertaindocuments,likelycausedby
complexmulti-pagestatementsthatrequireextensivereasoning.Incontrast,GPT-4o-miniconfigurationsmain-
tainmoreconsistentlatency(4.97–7.59saverage),suggestingthatsmallermodels,whilelessaccurate,provide
morepredictableprocessingtimessuitableforlatency-sensitiveproductionenvironments. End-to-endvision
modelsexhibitthehighestlatencies: PaddleOCR-VLaverages150.10secondsandolmOCRaverages104.45
seconds,makingthemimpracticalforreal-timeprocessingofbankstatements. GPT-5-miniandGPT-5-nano,
despitebeingmorerecentmodels,showelevatedlatency(25.27sand32.38srespectively)duetotheirreasoning
tokenoverhead.
CostAnalysis. Thecost analysisfor tableextraction(Table 14)reveals thatper-document processingcosts
varyfromeffectivelyzero(templatematching,open-sourcemodels)to$0.01perPDF(GPT-4.1,GPT-5-mini).
GPT-4.1-nano offers the lowest API cost at $0.03 total, while GPT-4.1 incurs the highest at $0.53 due to
itslargerpromptandcompletiontokenconsumption. Reasoning-capablemodels(GPT-5-mini,GPT-5-nano)
allocateasignificantproportionoftheircompletioncosttoreasoningtokens($0.35outof$0.43forGPT-5-
mini), which explains both their improved accuracy and higher cost. The Surya + docTR with GPT-5-mini
(header)configurationachievesthebestcost-accuracybalanceamongAPI-dependentsolutionsatonly$0.02
totalcostwhileachieving96.94%averagematchingNED.Ourtemplatematchingapproachandopen-source
models (olmOCR, PaddleOCR-VL) incur no API cost, though they require local compute resources. For a
productiondeploymentprocessinghundredsofbankstatementsdaily,thecumulativecostdifferencebetween
configurationsbecomessignificant,makingthetemplatematchingapproachadvantageousforhigh-throughput
scenarios.
Table14: Costanalysisfortransactiontableextraction(USD).TotalcostrepresentsaggregateAPI
expensesacrossalldocumentsintheevaluationdatasetwherePerPDFshowstheaveragecostper
individualdocument.
|                 |              |        | TokenCost  |      |                 | CostBreakdown |     |        |
| --------------- | ------------ | ------ | ---------- | ---- | --------------- | ------------- | --- | ------ |
| OCR             | GPT          |        |            |      |                 |               |     |        |
|                 |              | Prompt | Completion |      | Total Reasoning | Comp-Reason   |     | PerPDF |
| prebuilt-layout | N/A          | N/A    |            | N/A  | N/A N/A         |               | N/A | N/A    |
| PPStructureV3   | N/A          | N/A    |            | N/A  | N/A N/A         |               | N/A | N/A    |
| docTR           | gpt-4o-mini  | N/A    |            | N/A  | N/A N/A         |               | N/A | N/A    |
| docTR           | gpt-4.1      | 0.19   |            | 0.34 | 0.53 N/A        |               | N/A | 0.01   |
| docTR           | gpt-4.1-mini | 0.04   |            | 0.07 | 0.11 N/A        |               | N/A | 0.00   |
| docTR           | gpt-4.1-nano | 0.01   |            | 0.02 | 0.03 N/A        |               | N/A | 0.00   |
Continuedonnextpage
27

PublishedasaconferencepaperatICLR2026
Table14–Continuedfrompreviouspage
|                        |                    | TokenCost         |                 | CostBreakdown |        |
| ---------------------- | ------------------ | ----------------- | --------------- | ------------- | ------ |
| OCR                    | GPT                |                   |                 |               |        |
|                        |                    | Prompt Completion | Total Reasoning | Comp-Reason   | PerPDF |
| docTR                  | gpt-5-mini         | 0.02 0.43         | 0.45 0.35       | 0.08          | 0.01   |
| docTR                  | gpt-5-mini(low)    | 0.02 0.08         | 0.10 0.00       | 0.08          | 0.00   |
| docTR                  | gpt-5-nano         | 0.00 0.24         | 0.25 0.23       | 0.02          | 0.00   |
| PyMuPDF                | gpt-4o-mini        | 0.01 0.03         | 0.04 N/A        | N/A           | 0.00   |
| PyMuPDF                | gpt-4.1            | N/A N/A           | N/A N/A         | N/A           | N/A    |
| pdfium                 | gpt-4o-mini        | N/A N/A           | N/A N/A         | N/A           | N/A    |
| pdfium                 | gpt-4.1            | N/A N/A           | N/A N/A         | N/A           | N/A    |
| olmOCR-2-7B-1025       | N/A                | N/A N/A           | N/A N/A         | N/A           | N/A    |
| paddleOCR-VL(0.9B)     | N/A                | N/A N/A           | N/A N/A         | N/A           | N/A    |
| Surya+docTR            | gpt-5-mini(header) | 0.01 0.01         | 0.02 0.00       | 0.01          | 0.00   |
| Ours(templatematching) |                    | N/A N/A           | N/A N/A         | N/A           | N/A    |
Note:
1.N/Aindicatedatanotavailableornotapplicable.
2.Prompt=Prompttokencost.
3.Completion=Completiontokencost.
4.Reasoning=Reasoningtokencost.
5.Comp-Reason=Completioncostminusreasoningcost.
6.PerPDF=AveragecostperPDFdocument.
7.OCR=OCRprocessingtimeinseconds.
8.GPT=GPTinferencetimeinseconds.
9.Total=Totalprocessingtimeinseconds.
A.6 ABLATIONSTUDIESFORCREDITSCORING
A.6.1 CREDITSCOREDISTRIBUTION
WeevaluatethescoredistributionofourLogisticRegressionbaselineacrossthreefeaturesetconfigurations:
application information only, bank statement only, and blended. Figure 4–6 present score distributions for
goodaccounts(green)andbadaccounts(red),withEarthMover’sDistance(EMD)quantifyingdistributional
divergenceasameasureofdiscriminatorypower.
Application Information: Figure 4 shows limited separation between good and bad accounts when using
applicationfeaturesalone. Thehistogramandkerneldensityestimation(KDE)curvesrevealgoodaccounts
clusteringathigherscores(meanof665.7)andbadaccountsatlowerscores(meanof641.5),yieldinganEMD
of24.11. Thismodestdivergenceindicatesreasonablebutconstraineddiscriminatorypowerfromtraditional
applicationdata.
BankStatement: Figure5demonstratesmarkedlyimprovedseparationwhenusingbankstatementfeatures.
Goodaccountsexhibitameanscoreof699.2whilebadaccountsconcentratenear625.7. TheEMDincreases
to74.48, a3.1×improvementoverapplicationinformationalone, reflectingthestrongersignalprovidedby
transactional cash flow indicators. This result suggests bank statement-derived features create more distinct
riskprofiles.
Blended: Figure 6 displays the combined model using both application and bank statement features. This
blendedapproachachievesthestrongestdistributionseparation,withgoodaccountscenterednear708.4and
bad accounts near 612.6. The EMD reaches 96.84, a 4.0× improvement over application information and
1.3×overbankstatementalone,demonstratingthatcombiningfeaturesourcesenhancesdiscriminatorypower
beyondeitherindividualapproach.TheprogressiveEMDimprovementfrom24.11(applicationonly)to74.48
(bankstatement)to96.84(blended)alsoshowsthattransaction-derivedfeaturesaretheprimarydriverofscore
separationbetweengoodandbadaccounts.
A.6.2 REJECTEDCASESANALYSIS
ProblemStatement. Creditscoringmodelstrainedexclusivelyonapprovedapplicantssufferfromselection
bias,astheycaptureonlythesubsetoftheapplicantpopulationdeemedacceptablebyhistoricalunderwriting
decisions(Ehrhardtetal.,2021). Thiscreatesatwo-foldproblem: (1)themodellacksevidenceabouthow
rejectedapplicantswouldhaveperformedifapproved,leadingtopotentialunderestimationofactualportfolio
risk,and(2)themodel’sdecisionboundaryiscalibratedtoabiaseddistributionratherthanthetrueapplicant
28

PublishedasaconferencepaperatICLR2026
16
14
12
10
8
6
4
2
0
567 587 607 627 647 667 687 707 727 747 767 787
Score Points
ytisneD
/
ycneuqerF
Score Distribution Chart:
Logistic Regression - Application Info Features
Earth Mover's Distance: 24.11 Good Accounts (Histogram)
Bad Accounts (Histogram)
Good Accounts (Smoothed)
Bad Accounts (Smoothed)
Good Mean: 665.7
Bad Mean: 641.5
Figure 4: Score distribution for the application information model. Good accounts (green) cluster
at higher scores (mean 665.7) while bad accounts (red) concentrate lower (mean 641.5). EMD of
24.11indicatesmoderatediscriminatorypower.
population(Insights,2024). Toaddressthislimitation,weconductedrejectedcasesanalysison264rejected
loanapplicants.
Methodology. This analysis applies the scorecard model developed on approved applicants to the rejected
population, generating predicted risk scores without retraining. This non-augmentation approach allows us
to assess model consistency and identify systematic characteristics that distinguish rejected from approved
applicants.Byscoringrejectedapplicantswiththeexistingmodel,wecanobservewhetherrejectiondecisions
alignwithpredictedriskprofilesandunderstandthekeyfinancialbehaviorsdrivingrejectiondecisions.
ApplyingourLogisticRegressionscorecardtotheserejectedapplicantsrevealsthat96.97%(256of264)are
classified as high risk, 3.03% (8 of 264) as medium risk, and 0% as low risk (Table 15). This distribution
demonstratesstrongalignmentbetweentheconsultingfirm’srejectiondecisionsandourmodel’sriskassess-
ment, validatingthatthescorecardaccuratelycapturestheunderlyingriskfactorsthatmotivatedoriginalre-
jection decisions. Critically, no rejected applicant scored in the low-risk category, indicating that rejection
decisionswerenotarbitrarybutrathergroundedingenuinecreditriskindicatorsobservableintransactiondata.
Table15: RiskDistributionofRejectedLoanApplicantsviaScorecardModelPrediction
RiskLevel HighRisk MediumRisk LowRisk
Count 256(96.97%) 8(3.03%) 0(0.00%)
Implications.Thisanalysisservestwocriticalpurposes.First,itvalidatesthatourscorecardmodelgeneralizes
consistentlytotherejectedpopulation,withrejectiondecisionsstronglyalignedtopredictedrisk. Second,it
provides evidence that bank statements contain sufficient cash flow signal to identify high-risk applicants,
andthatrejectiondecisionsweredata-drivenratherthanarbitrary. Thefindingthatallrejectedapplicantsare
eitherhighormediumrisk,withaconcentrationinhighrisk,suggestingthattheconsultingfirm’shistorical
underwritingwasappropriatelyconservativeandthatourmodelcapturesthelegitimateriskfactorsunderlying
thosedecisions.Theseresultsstrengthenconfidencethatthescorecardcanbereliablyextendedtonewapplicant
populationswithlimitedcredithistory.
29

PublishedasaconferencepaperatICLR2026
8
6
4
2
0
416 436 456 476 496 516 536 556 576 596 616 636 656 676 696 716 736 756 776 796 816 836 856 876 896 916 936 956 976 996 1016 1036
Score Points
ytisneD
/
ycneuqerF
Score Distribution Chart:
Logistic Regression - Bank Statement Features
Earth Mover's Distance: 74.48 Good Accounts (Histogram)
Bad Accounts (Histogram)
Good Accounts (Smoothed)
Bad Accounts (Smoothed)
Good Mean: 699.2
Bad Mean: 625.7
Figure5: Scoredistributionforthebankstatementmodel. Bankstatement-derivedcashflowindi-
catorsproducestrongerseparationwithgoodaccounts(mean699.2)andbadaccounts(mean625.7)
showingclearerdivergence. EMDof74.48(3.1×higherthanapplicationinformation)reflectsthe
discriminatoryadvantageoftransactionaldata.
8
7
6
5
4
3
2
1
0
374 394 414 434 454 474 494 514 534 554 574 594 614 634 654 674 694 714 734 754 774 794 814 834 854 874 894 914 934 954 974 994 1014
Score Points
ytisneD
/
ycneuqerF
Score Distribution Chart:
Logistic Regression - Blended Features
Earth Mover's Distance: 96.84 Good Accounts (Histogram)
Bad Accounts (Histogram)
Good Accounts (Smoothed)
Bad Accounts (Smoothed)
Good Mean: 708.4
Bad Mean: 612.6
Figure 6: Score distribution for the blended model. Combining application and bank statement
featuresachievesthestrongestseparationwithgoodaccounts(mean708.4)andbadaccounts(mean
612.6) showing maximal divergence. EMD of 96.84 (4.0× higher than application information
alone)demonstratescomplementaryvalueofbothfeaturesources.
30

PublishedasaconferencepaperatICLR2026
B DEPLOYMENT AND OPERATIONAL FRAMEWORK
ThesixthphaseofCRISP-DMfocusesonthedeploymentoftheproposedcashflowunderwritingworkflow
inaproductionenvironment.Thisworkflowisdesignedtoleverageverifiabletransactiondatatoenabletrans-
parentandevidence-basedcreditdecisionswhileestablishingacontinuousfeedbackcyclefordatacollection,
modelretraining,andperformancemonitoringwithinexistingcorebankingsystems. Tosupportthis,arobust
machinelearningoperationsframeworkisimplementedtostructuretheend-to-endpipelineintofivekeystages.
Lastly,anintegratedcreditscoringframeworkisintroducedtoprovidecomprehensiveriskevaluationforboth
establishedandnew-to-creditMSMEs.
B.1 DATAINGESTION
Thepipelinebeginswhenbankstatementsarereceived. Extractionmodulesparseandstructuretherawtrans-
actiondatausingOCRandlayoutanalysistechniques. Thisprocesstransformsunstructureddocumentsinto
astandardizedtabularformatsuitablefordownstreamprocessing. Theingestionstagealsoperformsintegrity
verificationanddatavalidationcheckstoensuredocumentauthenticity.
B.2 FEATUREENGINEERINGANDFEATURESTORE
Followingingestion,structureddataarefedintothefeatureengineeringmodule,whichcomputestransaction-
derivedandbehavioralfeatures.Thesefeaturesaretime-stamped,versioned,andstoredinacentralizedreposi-
tory.Thefeaturestoreprovidesasinglesourceoftruthforbothtrainingandinference,ensuringthesamelogic
usedtogeneratehistoricalfeaturesisconsistentlyappliedtonewapplicantsinrealtime.Thisdesignguarantees
reproducibility,preventsfeatureskew,andsupportstraceabilityacrossmodeliterations.
B.3 CONTINUOUSINTEGRATION(CI)
TheCIpipelineautomatesmodelretrainingandvalidationpriortointegrationintotheproductionregistry. It
istriggeredbytwoprimaryevents: (1)apredefinedschedule(e.g.,annually)whennewlabeleddatabecome
availablefromthecorebankingsystem,and(2)alertsfromthemonitoringsystemindicatingpotentialmodel
or data drift. Upon activation, the pipeline retrieves the latest versioned feature set and ground truth labels,
retrainsthemodel, andevaluatesitsperformanceagainstthecurrentproductionmodelusingpredefinedand
consistentevaluationmetrics.
B.4 MODELREGISTRYANDCONTINUOUSDEPLOYMENT(CD)
Iftheretrainedmodeldemonstratessuperiorperformance,itisautomaticallyversionedandstoredinthemodel
registry.TheCDprocessthenpackagesthevalidatedmodelintoacontainerizedmicroserviceanddeploysitas
asecureRESTAPIendpoint.Toensurereliabilityandminimizeproductionrisk,acanarydeploymentstrategy
isapplied,initiallyroutingasmallfractionoflivetraffictothenewmodelforperformancevalidationbefore
full-scalerollout.
B.5 CONTINUOUSMONITORINGANDFEEDBACKLOOP
Once the bank statement-based credit scoring model is deployed, it operates within a Champion-Challenger
framework(Kimetal.,2019)toenablecontinuousperformanceoptimization. TheChampionmodelservesas
thecurrentproductionbaseline,whileoneormoreChallengermodelsareperiodicallyretrainedonthelatest
dataandevaluatedinparallel. Modelperformanceiscontinuouslymonitoredandcomparedacrosspredefined
metrics. When a Challenger consistently outperforms the Champion, the system automatically notifies des-
ignatedbankofficerstoreviewtheresultsandpromotethenewmodeltoproduction. Thisapproachensures
sustainedmodelimprovement,robustness,andoperationalstability.
B.6 INTEGRATEDCREDITSCORINGFRAMEWORK
Inproduction,thecashflowunderwritingsystemfunctionsasanintegrateddecisionengineembeddedwithin
the lending process. Upon submission of bank statements, AI modules automatically extract and structure
therawdatausingOCRandnaturallanguageprocessingmodels. Theprocesseddatathenundergoesfraud
detection,cashflowanalysis,andnetworkanalyticstogeneratetransaction-derivedfeaturesandcreditscores
for MSME applicants. The existing bureau-based scorecard, designed for borrowers with established credit
histories, operates in parallel with the newly developed cash flow-based model. Each model independently
producesariskrating,andariskoverridemechanismensuresconservativedecisioning;ifeithermodelindicates
higherrisk,thefinalclassificationadoptsthatrating. Thisframeworkprovidesatransparent,evidence-based,
31

PublishedasaconferencepaperatICLR2026
anddata-drivenapproachtoMSMEcreditassessmentusingadaptive,explainableAIscoring. Italsoextends
financialaccesstonew-to-creditbusinessesthroughverifiabletransactiondata.
C LIMITATIONS AND FUTURE WORK
Thisworkhasseverallimitationsthatshouldbeaddressedinfutureresearch. First,thedatasetcomprises611
loanapplicationsfromasingleMalaysianconsultingfirm. Whilethedatasetrepresentsreal-worldproduction
datacollectedoveratwo-yearperiod,thesamplesizeisconstrainedbythepracticalrealitiesofMSMElend-
inginemergingmarkets,wheredataavailabilityremainslimitedduetostringentdataprivacyandregulatory
requirements. Future work should validate these findings across multiple institutions and larger datasets as
additionalMSMElendingdatabecomeavailable.
Second,theclassimbalanceinourdataset(518non-defaultvs.93defaultcases)reflectsthenaturaldistribution
observedinreal-worldlendingportfolios,wherethemajorityofborrowerssuccessfullyrepaytheirloans.While
thisimbalanceposesmodelingchallenges, itaccuratelyreflectsreal-worldcreditrisksettings. Inthiswork,
weaddressedthislimitationthroughappropriatemodelselection,WOE-basedfeatureengineering,andcareful
evaluationusingAUROC,whichisrobusttoclassimbalance.Itisimportanttonotethatclassimbalanceisnot
alimitationthatcanbefullyeliminated,butratheraninherentcharacteristicofcreditscoringdatasets.Ascredit
assessmentmodelsimproveandlendingdecisionsbecomemoreaccurate,successfulrepaymentratesincrease,
thereby maintaining or even intensifying this natural imbalance. Nevertheless, future studies could explore
advancedresamplingtechniquesorcost-sensitivelearningmethodstofurtherenhancemodelperformanceon
minorityclassprediction.
Third,whilewedescribemultipleAImodulesfordocumentprocessing,frauddetection,andtransactionanal-
ysiswithintheproposedend-to-endcashflowunderwritingworkflow,theevaluationfocusesonoverallcredit
scoringperformanceratherthantheeffectivenessofindividualmodules. However,detailedmodule-levelas-
sessmentisconstrainedbytheuseofproprietarymethodsandsensitiveoperationaldatathatcannotbepub-
liclydisclosed. Futureworkutilizingsyntheticoranonymizeddatacouldenablemoregranularmodule-level
analysisandbenchmarking.Additionally,futureresearchcouldexploreformalizingthesemodulesasfullyau-
tonomousagents,enablingthedevelopmentofamulti-agentcreditscoringarchitecturewithclearerinter-agent
responsibilitiesandinteractions.
Fourth,theproposedworkflowhasbeendeployedinaproductionenvironmentwithoneMalaysianconsulting
firm. Whilethisdemonstratesreal-worldapplicability,broadervalidationacrossdifferentlendinginstitutions,
regulatoryenvironments,andMSMEsegmentswouldstrengthenthegeneralizabilityofourfindings. Further
research is needed to systematically integrate the proposed cash flow underwriting workflow with existing
credit assessment systems that rely on behavioral and credit bureau data, ensuring coherent and robust risk
evaluation. Additionally,longitudinalstudiesexaminingmodelperformancestabilityacrosseconomiccycles
wouldprovidevaluableinsightsintothetemporalrobustnessandadaptabilityofbankstatement-basedfeatures
undervaryingmacroeconomicconditions.
32