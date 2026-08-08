DOI:10.1111/eufm.12408
EUROPEAN
| ORIGINAL     | ARTICLE      |          |          |         |           |             |     | FINANCIAL MANAGEMENT |     |     |
| ------------ | ------------ | -------- | -------- | ------- | --------- | ----------- | --- | -------------------- | --- | --- |
| Machine      |              | learning |          | methods |           | in finance: |     |                      |     |     |
| Recent       | applications |          |          | and     | prospects |             |     |                      |     |     |
| Daniel Hoang |              | | Kevin  | Wiegratz |         |           |             |     |                      |     |     |
InstituteforFinance,KarlsruheInstitute
| ofTechnology(KIT),Karlsruhe, |     |     |     | Abstract                                     |     |             |     |          |           |      |
| ---------------------------- | --- | --- | --- | -------------------------------------------- | --- | ----------- | --- | -------- | --------- | ---- |
| Germany                      |     |     |     | Westudyhowresearcherscanapplymachinelearning |     |             |     |          |           |      |
|                              |     |     |     | (ML) methods                                 |     | in finance. |     | We first | establish | that |
Correspondence
DanielHoang,InstituteforFinance, the two major categories of ML (supervised and
KarlsruheInstituteofTechnology,
|     |     |     |     | unsupervised | learning) |     | address | fundamentally |     | differ- |
| --- | --- | --- | --- | ------------ | --------- | --- | ------- | ------------- | --- | ------- |
Kaiserstr.12,76131Karlsruhe,Germany.
entproblemsthantraditionaleconometricapproaches.
Email:daniel.hoang@kit.edu
Then,wereviewthecurrentstateofresearchonMLin
|     |     |     |     | finance        | and identify | three       | archetypes  |          | of applications: |           |
| --- | --- | --- | --- | -------------- | ------------ | ----------- | ----------- | -------- | ---------------- | --------- |
|     |     |     |     | (i) the        | construction | of          | superior    | and      | novel            | measures, |
|     |     |     |     | (ii) the       | reduction    | of          | prediction  | error,   | and              | (iii) the |
|     |     |     |     | extension      | of the       | standard    | econometric |          | toolset.         | With      |
|     |     |     |     | this taxonomy, |              | we give     | an outlook  | on       | potential        | future    |
|     |     |     |     | directions     | for both     | researchers |             | and      | practitioners.   | Our       |
|     |     |     |     | results        | suggest      | many        | benefits    | of ML    | methods          | com-      |
|     |     |     |     | pared to       | traditional  | approaches  |             | and      | indicate         | that ML   |
|     |     |     |     | holds great    | potential    | for         | future      | research | in finance.      |           |
KEYWORDS
artificialintelligence,bigdata,machinelearning
|     |     |     |     | JEL CLASSIFICATION |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
C45,G00
We appreciate helpful comments and suggestions made by John A. Doukas (the editor), two anonymous referees,
RenéeAdams,AndreasBenz,FrancescoD'Acunto,MartinRuckes,FabianSilbereis,MichaelWeber,andparticipants
atthe2022EuropeanConferenceoftheFinancialManagementAssociation(Lyon).
ThisisanopenaccessarticleunderthetermsoftheCreativeCommonsAttribution‐NonCommercial‐NoDerivsLicense,whichpermits
useanddistributioninanymedium,providedtheoriginalworkisproperlycited,theuseisnon‐commercialandnomodificationsor
adaptationsaremade.
©2022TheAuthors.EuropeanFinancialManagementpublishedbyJohnWiley&SonsLtd.
|
EurFinancManag.2023;29:1657–1701. wileyonlinelibrary.com/journal/eufm 1657

|
1658
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
1 | INTRODUCTION
Artificial intelligence is increasingly entering our day‐to‐day life with impressive applications:
face detection enables safe and efficient airport travel, voice recognition allows for seamless
communication with personal assistants on smartphones and smart home devices, and ever
more firms are using chatbots for quick customer support. Almost everyone interacts with
modern artificial intelligence many times per day.
The main technology behind artificial intelligence is machine learning (ML). ML methods
enable machines to conduct such complex tasks as detecting faces, understanding speech, or
answering messages. Given the power of ML technology, it is natural to ask whether ML
methodscanalsobeappliedelsewhere.ThispaperaddressestheuseofMLtosolveproblemsin
finance research.
SeveraloverviewpapersindicatethepotentialofMLinfinance.Varian(2014)describesML
asanappropriatetoolintheeconomicanalysisofbigdataandpresentssomeMLmethodswith
examples in economics. He further hints at potential ML applications in econometrics.
Mullainathan and Spiess (2017) identify prediction problems as the main use case of ML in
economicsandpresentdifferentcategories ofexistingandpotential futureapplications.Athey
and Imbens (2019) illustrate the most relevant ML methods from an econometric perspective.
TheyalsoprovideanoverviewofML'spotentialbeyondpureprediction,especiallyforcausality
in economic questions.
WhiletheusageofMLinfinanceresearchisstillinitsinfancy,thenumberofapplications
that exploit the potential of ML has grown tremendously over the last few years. In 2018, the
numberofMLpublicationsmorethantripledcomparedtotheyearlyaverageoftheyears2010
to2017.In2019,theincreasewasalreadymorethanfivefold.In2020,theincreasewasalmost
sevenfold,andin2021,therewerealmost11timesasmanypublicationsusingMLthanbefore.
EventhoughtheuniverseofMLapplicationsinfinancehasgreatlyexpandedrecently,itisstill
mostly unclear where and how to apply ML to solve research problems in finance.
Thecontributionofthispaperis threefold.First,wepresentahigh‐levelprimeronMLfor
financial economists. We illuminate the different types of ML, their purposes and
functionalities, and the available methods for each type. Given our focus on finance, we place
specialemphasisonthedifferencebetweentraditionaleconometricmethodsandML.Wealso
demonstrate the benefits of ML over traditional linear methods (particularly for prediction
problems) by applying ML to a high‐dimensional asset pricing problem in finance. Our
introduction allows researchers in the field to quickly grasp the essentials of ML that are
relevant for applications in finance without assuming any prior knowledge of ML.
Second, we construct a taxonomy of current and future ML applications in finance. Given
the increasing number of recent studies, earlier classifications do not capture existing
applications well. We review the up‐to‐date literature in the field and divide it into three
distinct archetypes.Ourtaxonomyallows researchers tobetterunderstand thecurrentstateof
the literature and how different contributions relate to each other. Furthermore, it serves as
guidance for future ML applications in finance.
Third, we study future prospects of ML applications in finance. We systematically analyse
ML applications in finance and how their publication success differs by research field (asset
pricing, corporate finance, financial intermediation, household finance) and application type.
Our results not only suggest a high potential for ML applications in general but also provide
researchers with indications of the most promising future directions.
1468036x,
2023,
5, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1659
FINANCIAL MANAGEMENT
Traditional econometrics aims to provide causal explanations for economic phenomena by
analysingrelationshipsbetweeneconomicvariables.ML,incontrast,allowsresearcherstoobtain
uniqueinsightsfromhigh‐dimensionaldata.Therearetwomajortypesofhigh‐dimensionaldata
forwhichMLoffersbenefitsovertraditionalmethodssuchaslinearregression.First,MLcandeal
with high‐dimensional, numerical data, that is, data consisting of a high number of variables
relativetothenumberofobservations.Suchhigh‐dimensionaldataarisesifthereisaplethoraof
economicallyrelevantvariablesorifnonlinearitiesandinteractioneffectsplayanimportantrole.
ML methods leverage the informational content of such data for predictions with small out‐of‐
samplepredictionerrors.Second,incontrasttotraditionalmethods,MLallowstheexploitationof
unconventionaldata(suchastext,images,orvideos),whichareinherentlyhigh‐dimensional.ML
methods can extract economically relevant information from such data, which then serves as a
starting point for further economic analyses.
ML is strongly related to the concept of big data. Big data consists of a high number of
observations, a high number of variables, or both (Stock & Watson, 2020, p. 515). In general,
datawithahighnumberofobservationsimprovetheaccuracyofMLpredictions(inasimilar
waytohowtheyimprovetheprecisionofparameterestimatesofordinaryleastsquares[OLS]
regressions). If the data exhibit a high number of variables (relative to the number of
observations),MLoutperformssimpler,traditionalmethodssuchaslinearregression.Applying
ML to data with high numbers of observations and variables combines both benefits as it can
yield high prediction accuracy as well as outperformance over traditional methods.
Basedonourreviewofthefinanceliterature,weclassifyMLapplicationsintothreedistinct
archetypes:(1)constructionofsuperiorandnovelmeasures,(2)reductionofpredictionerrorin
economic prediction problems, and (3) extension of the existing econometric toolset.
First,researcherscanuseMLtoconstructsuperiorandnovelmeasures.Forinstance,when
applied to exploit unconventional data, the extracted information can serve as a superior or
novelmeasureofaneconomicvariable.SuperiorMLmeasuresmayexhibitlowermeasurement
error and, therefore, can enable more precise estimates of economic relationships than
traditional measures can. Novel ML measures enable analyses with previously unmeasurable
economic variables.
Second, researchers can use ML to reduce prediction error in economic prediction
problems. For instance, the fundamental problem of pricing financial or real assets is the
prediction of adequate market prices.Given that amain functionality of ML is prediction, ML
methods can provide better results than traditional approaches in solving such economic
prediction problems.
Third,researcherscanuseMLtoextendtheexistingeconometrictoolset.Econometrictools
often contain a prediction component. For instance, thefirst stageof an instrumental variable
designiseffectivelyapredictionproblem.MLmethodscanenhancesuchexistingeconometric
tools by improving the performance of their prediction component. Furthermore, some ML
methodsthemselvesdirectlyserveasneweconometrictools.Forinstance,ML‐basedclustering
methods extend the set of existing clustering methods from econometrics.
TodemonstratethebenefitsofMLovertraditionalmethodsatatypicalpredictionproblem,
weapplyMLtorealestateassetpricing,whichisparticularlyrelevantintheareasofhousehold
finance and real estate economics.1 Real estate asset pricing is an inherent high‐dimensional
problem due to the large number of property characteristics, nonlinearities, and interaction
1OurexemplaryapplicationcannotyieldgeneralisableresultsabouttheperformanceofMLcomparedtotraditionalmethods,but
illustrateshowtoapplyMLtoatypicalprobleminfinancewithhigh‐dimensionaldata.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1660
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
effects (for instance, a kitchen's marginal value likely interacts with house type, e.g., luxury
apartment vs.standardsingle‐family house.)Wepredictreal estateassetpricesin theGerman
residential housing market using various ML methods (which exploit the large number of
individual property characteristics in our data set) and compare their accuracy with estimates
fromtraditionalhedonicpricing(linearregressionwiththeOLSestimator).Figure1illustrates
our key results. The two charts compare the actual property prices with the OLS estimates
(chartontheleft) andwith thepricepredictionsof ourbest‐performing ML method(charton
theright,boostedregressiontrees).Onaverage,thepricepredictionsfromtheMLapproachare
much closer to the actual prices than the OLS estimates. The difference in pricing accuracy is
especiallypronouncedattheupperendofthepricerange:whiletheOLSestimatesshowlarge
deviations from the actual prices, the ML‐based price predictions are much closer.
In the final part of our paper, we conduct a bibliometric analysis and examine the
publicationsuccessofarticlespublishedinmajorfinancejournalsduringthe2010–2021period.
Specifically, we address the following questions: (1) How important is ML as a novel
methodology for research in finance? (2) What is the methodological purpose of ML (beyond
prediction) in its applications for research in finance? (3) How do these findings differ across
the various subfields in finance?
We find that although ML is a relatively new method in finance research, it has already
found broad acceptance in the scientific community. The share of ML papers has grown in
recentyearsandaccountsforapproximately3%–4%ofthepublicationsinthetopthreefinance
journals (The Journal of Finance, Journal of Financial Economics, The Review of Financial
Studies) in 2021. This share is similar for somewhat lower‐ranked journals. Furthermore, our
analysis reveals that the two main areas of finance—financial markets/asset pricing and
banking/corporate finance—leverage the potential of ML in fundamentally different ways.
While the literature in the field of financial markets/asset pricing tends to apply ML to
FIGURE 1 Comparisonoftheaccuracyofhedonicpricing(OLS)andMLinpredictingrealestateasset
prices.Thisfiguredepictstheaccuracyoftraditionalhedonicpricing(OLS)andMLinpredictingrealestate
assetpricesintheGermanresidentialhousingmarket.Onaverage,theML‐basedpriceestimatesaremuch
closertotheactualpricesthantheOLSestimatesare.ThebenefitofMLismostpronouncedattheupperendof
thepricerange,whereOLSperformsespeciallypoorly.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1661
FINANCIAL MANAGEMENT
economicpredictionproblems,mostpublicationsinthefieldsofbankingandcorporatefinance
use ML to construct superior and novel measures. Interestingly, publications in the highest‐
rankedjournalsuseMLdisproportionallyoftentoconstructsuperiorandnovelmeasures.This
effectisespeciallylargewithinthefieldsofbankingandcorporatefinance.Ourresultsindicate
a particularly large potential of applying ML to unconventional data toconstruct superior and
novel measures for topics related to financial institutions and corporate finance.
Overall, our results suggest a promising future for ML applications in finance. The many
benefitsofMLovertraditionaleconometricmethods,thestrongandconsistentincreaseinthe
number of ML publications in the last few years, and the widespread usage of ML by studies
published in the highest‐ranked journals of the profession leave little reason to expect
otherwise.2
Our paper is related to a growing literature focused on ML applications in finance. For
instance, there is a small number of finance textbooks that either survey specific areas of
financeinwhichMLtechniqueshaverecentlyemerged(e.g.,Nagel,2021,forassetpricing;De
Prado, 2018, for asset management) or provide mathematical foundations for ML in
quantitative finance (e.g., Dixon et al., 2020). The aim of these important contributions is to
showhowtocarefullyadaptMLtechniquesandhowtodealwiththespecificcharacteristicsof
certain subfields in finance—with a particular focus on financial markets. Our perspective on
MLisclearlydifferentfromtheonesusedintheseimportantcontributionsasourinterestlies
indetectingpromisingMLapplicationsbeyond(predictionproblemsin)financialmarkets.We
also add to a small number of survey papers that review the applications of ML in finance.
These studies differ from ours in their use of classification techniques, scope, and focus. One
groupofsurveysuses(mostly)automatedtechniques,suchastextualanalysis(Azizetal.,2022)
orcitation‐basedapproaches(Goodelletal.,2021),toclassifyMLapplicationsacrossallfinance
subfields into application areas (such as risk forecasting or financial fraud). Another group of
surveys adopts a more selective perspective and manually reviews either ML applications in
certain subfields of finance, such as risk management (Aziz & Dowling, 2019), or applications
ofspecificMLmethods,suchasdeeplearning(Ozbayogluetal.,2020).Ourstudydiffersfrom
these studies, which focus on application areas (i.e., where ML is applied), in that we classify
the literature based on the methodological purpose of ML in finance (i.e., how ML is applied).
This somewhat different angle—based on our novel taxonomy—allows us to uncover a
frequentlyoverlooked(butpromising)groupofMLapplicationsinfinance:Whilemanyofthe
existingsurveys(tendto)focusonMLforpredictionpurposes,weshowthattwoothertypesof
ML applicationsare gainingimportance: theconstructionof superior andnovel measures and
the extension of the existing econometric toolset for finance research. Furthermore, we also
manually review all these ML papers instead of relying on automated techniques that might
missimportantcontext.Additionally,tothebestofourknowledge,noneoftheexistingreviews
examines ML applications in finance with a bibliometric performance analysis based on the
publication success of existing work by research field and methodological purpose.
Theremainderofthispaperisorganisedasfollows.Section2givesahigh‐levelintroduction
to ML together with an illustrative application of ML to a typical problem in finance. In
Section 3, we present the three archetypes of ML applications and review the corresponding
2MLhasreceivedconsiderableattentionnotonlyfromfinanceacademiabutalsofrompractitioners.TableA1intheappendixpresentsa
selectionofpublicannouncementsoflargeinstitutions(suchasbanks,insurancecompanies,andassetmanagementfirms)thatmake
useofMLintheirday‐to‐daybusinessoperations(e.g.,HSBCandDeutscheBankapplyMLtopredictanddetectfraudulent
transactions).Thesepracticeusecasesmostlycentrearoundpredictionproblems(thesecondarchetypeinourtaxonomy).
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1662
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
literature. Section 4 outlines the most promising future directions for applying ML in finance.
Section 5 concludes the paper.
2 | FUNDAMENTALS OF ML
Inthissection,weprovideaprimerofMLtolaythegroundworkforsubsequentchapters.Our
focusisonthemechanicsofthedifferenttypesofML,theproblemsforwhichMLhasproven
tobewellsuitedforsolving,andthemethodswithwidespreaduseinthefinanceliterature.We
also emphasise the differences between ML and traditional econometric methods.
Most studies in empirical finance aim at analysing economic relationships between
economic variables. A typical example is an analysis of how certain factors affect the capital
structure or how regulatory changes affect the expectations of economic agents. Traditional
econometric methods provide estimates βˆ for the direction and strength of these factors.
ML, in contrast, serves different purposes. Instead of providing direct insights into the
relationshipsbetweeneconomicvariables,MLtendstoserveasamethodforpredictionorfordata
structure inference. Methods for prediction take the givenobservations to infer estimates for the
dependentvariable yˆ ofnewobservationsbasedontheircovariates X.Forinstance,theobserved
pricesandpropertycharacteristicsintherealestatemarketcouldbeusedtopredictthepricesof
previously unobserved properties based on their characteristics. The first major type of ML,
supervised learning, encompasses methods to make such predictions (see Section 2.1).
Methods for data structure inference derive structural information from given data X. A
typical example is the identification of clusters in the data to learn how different observations
relatetoeachother.ThesecondmajortypeofML,unsupervisedlearning,comprisessuchmethods
to arrive at structural information from data (see Section 2.2).
Table 1 gives an overview of the differences between traditional econometrics and these two
majortypesofML,supervisedandunsupervisedlearning.Mostimportantly,thethreeapproaches
servedifferentpurposes.Asexplainedabove,traditionaleconometricsaimsatextractingeconomic
relationships (Samuelson & Nordhaus, 2009, p. 5) and thus solves so‐called βˆ‐problems
(Mullainathan & Spiess, 2017). Supervised learning provides predictions; thus, it is mainly
intended to solve so‐called yˆ‐problems (Mullainathan & Spiess, 2017). Unsupervised learning
infersthedatastructurefromgivendatawithoutaspecial y‐variable;thus,itsolves X‐problems.
The three approaches also differ with regard to their general methodology. Every approach
makes use of data. In traditional econometrics, there is a dependent variable y and multiple
independent variables X. In ML jargon, such data are called ‘labelled data’, as there is a special
label y for each observation (which is the dependent variable y in regression jargon). The
dominantmethodintraditionaleconometricsislinearregression,mainlyduetoitsflexibilityand
interpretability. Linear regression with the OLS estimator provides an explanatory model in the
form of a regression line and different metrics of statistical significance, such as t‐values and
p‐values. Finally, these results can indicate causal relationships between economic variables.
Supervised learning also relies on labelled data. The special label y represents the target
variabletobepredictedbasedonthepredictorvariables X.ApplyingasupervisedMLmethodon
the given data yields a prediction model as well as estimates for its expected prediction
performance. The prediction model can then be used to make out‐of‐sample predictions, that is,
predictions of the value of the target variable of previously unobserved examples based on their
characteristics.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

gninraeldesivrepusnudnadesivrepus:LMfosepytrojamowtehtdnascirtemonocelanoitidartneewtebsecnereffiD
1
ELBAT
desuehtotdragerhtiwreffid,gninraeldesivrepusnudnadesivrepus,LMfosepytrojamowtehtdnascirtemonocelanoitidartwohfoweivrevonastroperelbatsihT dnasnoitciderpsedivorpgninraeldesivrepuselihw,anemonehpcimonocefosnoitanalpxeselbanescirtemonocelanoitidarT.esoprupdna,egasu,stluser,dohtem,atad
.erutcurtsatadsrefnigninraeldesivrepusnu
esopruP
egasU
stluseR
dohteM
ataD
hcaorppA
’ˆβ‘noitanalpxE
pihsnoitaler)lasuaC(
lacitsitatsdnaledomyrotanalpxE
)SLO(noissergerraeniL
dellebaL
lanoitidarT
ecnacifingis
)Y,X(atad
scirtemonoce
i
i
i
’ˆy‘noitciderP
elpmas‐fo‐tuO
noitciderpdnaledomnoitciderP
dohtemLMdesivrepuS
dellebaL
gninraeldesivrepuS
snoitciderp
ecnamrofrep
)Y,X(atad i
i
i
erutcurtsataD
noitamrofnilarutcurtS
ataddnaledomerutcurtsataD
LMdesivrepusnU
dellebalnU
gninraeldesivrepusnU
’X‘ecnerefni
atadmorf
scitsiretcarahcerutcurts
dohtem
)X(atad i
i
|
HOANGANDWIEGRATZ EUROPEAN 1663
FINANCIAL MANAGEMENT
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1664
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
Unsupervised learning relies on unlabelled data, which is the defining distinction between
unsupervised and supervised learning in the literature (Hastie et al., 2009, pp. 485–486).
Unlabelled data means that there is no label y (i.e., no dependent variable y in regression
jargon);allvariablesareconsidered‘equal’.ApplyinganunsupervisedMLmethodtothegiven
datayieldsadatastructuremodelanddatastructurecharacteristics.Finally,bothresultscanbe
used to infer structural information from the data.3
In the following sections, we describe the two major categories of ML—supervised and
unsupervised learning—in more detail and give an overview (whose coverage is naturally
selective) of the relevant methods for each category. Then, we provide an illustrative
application of ML to a typical problem from the field of household finance: the prediction of
real estate prices. Finally, we discuss limitations, caveats, and drawbacks of ML.
2.1 | Supervised learning
Supervised learning aims at making out‐of‐sample predictions with high prediction
performance. To accurately assess the expected prediction performance on previously unseen
observations,thegivendataaredividedintotrainingdataandtestdata.Then,asupervisedML
method is applied to the training data to build a prediction model. Finally, applying the
prediction model to the test data yields an estimate of the expected out‐of‐sample prediction
performance.
To build a prediction model, various supervised ML methods of differing complexity have
been developed. In general, more complex methods tend to enable higher prediction
performance but reduce interpretability. Figure 2 gives an overview of common methods of
supervised ML arranged by typical prediction performance and interpretability.
The simplest method is linear regression with the OLS estimator. OLS provides excellent
interpretability.However,itsout‐of‐samplepredictionperformancehasturnedouttobegenerally
weak.OnewaytoimprovethepredictionperformanceofthelinearOLSmodelwouldbetoadd
nonlinear transformations and interactions of the original predictor variables to the model
specification.Inmanycases,however,itisexanteunclearwhichnonlinearitiesandinteractions
areactuallyrelevant.Includingallpossiblecombinationsisgenerallydifficultsinceitresultsinan
exorbitantnumberofvariablesthatcanquicklyexceedthenumberofobservations.Inmanycases,
the sheer size of the resulting data sets would also lead to computational problems.
SinceOLS(undercertainconditions)isthebestlinearunbiasedestimator(BLUE),oneway
thathasbeenproposedtoimprovethepredictionperformanceistoallowforbias.Incontrastto
explanation problems, prediction problems aim to achieve maximal prediction performance;
thus,theydonotrequireunbiasednessofvariablecoefficients.Regularisedlinearmethodsoffer
a way to systematically introduce bias to improve OLS prediction performance (Hastie et al.,
2009, pp. 61–79). More specifically, regularisation means that such methods shrink the
coefficients of the predictor variables to increase prediction performance.4 The most common
method for regularised linear regression is the least absolute shrinkage and selection operator
3WhilesupervisedandunsupervisedlearningarearguablythemostimportantcategoriesofML,therealsoexistothercategoriesofML
thatarelesscommonbutrelevantforspecificapplications:reinforcementlearningforsequentialdecisionproblems(Sutton&Barto,
2018),semisupervisedlearningforproblemswithmostlyunlabelledtrainingdata(Zhu,2005),andactivelearningforproblemswith
costlytrainingdata(Settles,2009).
4Theintroductionofbiascanincreasepredictionperformancebecauseofthebias‐variancetradeoff.See,forinstance,Hastieetal.(2009,
pp.37–38,219–228)fortechnicaldetails.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1665
FINANCIAL MANAGEMENT
FIGURE 2 OverviewofcommonmethodsinsupervisedMLarrangedbytypicalpredictionperformance
andinterpretability.ThisfiguregivesanoverviewofthemostcommonmethodsinsupervisedML.Themethods
differbycomplexity:morecomplexmethodstypicallyachievehigherpredictionperformancebutareless
interpretable.Fornumericaldata,lesscomplexmethodstendtoworkwell,whileunconventionaldata(suchas
text,images,orvideos)oftenrequiremorecomplexmethods.
(LASSO). LASSO works similarly to OLS but introduces bias by adding a penalty term in its
optimisation function to penalise large variable coefficients with little informational content.
The specific functional form of the penalty term drives irrelevant coefficients to zero. Hence,
LASSO is often used for variable selection in addition to pure prediction and also provides
relatively good interpretability.
Inaddition toLASSO,there are other regularised linearmethods that differ with regard to
thefunctionalformofthepenaltyterm.Ridgeregressionusesapenaltytermthatdoesnotdrive
coefficients to exactly zero and is therefore less interpretable. However, ridge regression often
providessuperiorprediction performancecompared toLASSO.Elasticnet regressioncombines
the two methods (Zou & Hastie, 2005). Its penalty term is a linear combination of the penalty
terms of LASSO and ridge regression to incorporate their respective strengths.
In contrast to the linear methods just discussed, more complex ML methods automatically
consider relevant nonlinearities and interaction effects. For numerical data, tree‐based ML
methods are widespread (Hastie et al., 2009, pp. 305–334). The simplest tree‐based method is
thedecisiontree,whichalsoactsasthebuildingblockofallothertree‐basedmethods.PanelA
in Figure 3 depicts a simplified decision tree trained for house price prediction. It consists of
nodes at which the tree splits depending on the value of a certain predictor variable. Decision
treestypicallycontainmultiplelayersofnodes,sotheyimplicitlyconsiderinteractionsbetween
multiple variables. When the tree reaches a leaf node, that is, a node after which there is no
furthersplit,thetreereturnsapredictionvalue.Giventhattherelevantpredictorvariablesand
thresholdsaredirectlyobservableinthesplits,decisiontreesarecharacterisedbyrelativelyhigh
interpretability.5
5Formoredetailsondecisiontrees,see,forexample,Loh(2011).
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1666
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
FIGURE 3 Illustrationsofadecisiontreeandaneuralnetwork.Thisfiguredepictsadecisiontree(PanelA)
andaneuralnetwork(PanelB).Thedecisiontreewastrainedforhousepriceprediction.Itreachesitsprediction
decisionbyevaluatingthevalueofcertainpredictorvariablesateachsplit.Neuralnetworksconsistofmultiple
layersofneuronsthroughwhichthegivendataareprocessed.Theshownneuralnetworkusesasimplefeed‐
forwardarchitecture,whichmeansthatdataonlyflowfromlefttoright.
Random forests combine multiple decision trees (Breiman, 2001). More specifically, the
random forest method repeatedly draws bootstrap samples from the given data and builds a
separate decision tree from each sample. The prediction of a random forest is then the average
predictionvalueofthedifferenttrees.Randomforeststypicallyachievemuchhigherprediction
performance than single decision trees but are inherently less interpretable.
Boosted regression trees extend the concept of random forests to further improve their
prediction performance (Hastie et al., 2009, pp. 353–358). Instead of combining many
independent decision trees, the boosted regression tree method builds the trees iteratively and
considerswhichobservationstheprevioustreescouldnotpredictwell.Boostedregressiontrees
typically not only outperform random forests but are often among the winning algorithms in
datasciencecompetitions,whichhighlightstheirstate‐of‐the‐artpredictionperformancelevel.
Whiletree‐basedMLmethodsand,inparticular,boostedregressiontreesachievestate‐of‐the‐
art prediction performance with numerical data, neural networks often excel with
unconventional data such as text, images, or videos. Panel B in Figure 3 depicts a small
neural network. A neural network consists of two components: neurons (arranged in so‐called
layers)andlinksbetweenneurons(Hastieetal.,2009,pp.389–415).Thelinksdescribetheflow
of data between the neurons. First, a neural network's input layer receives the predictor
variables, for instance, pixel‐level image data. Then, the hidden layers iteratively process the
dataanddeliverthemtotheoutputlayer,whichreturnsthefinalpredictionvalue.Initsmost
basicversion,aneuronfirstcalculatesaweightedsumofthedatathatarrivefromtheneurons
of the previous layer (the weights are determined endogenously during the training process).
Then,itappliesanonlinearfunction(e.g.,alogisticfunction)tothisweightedsum.Finally,the
neuron sends the result of this calculation to all neurons of the next layer to which it is
connected. The number of layers, the number of neurons in each layer, the links between
neurons,andthefunctionalformsofthenonlinearfunctionsare(exogenously)specifiedbythe
designeroftheneuralnetworkanddependonthegivenproblem.Neuralnetworksusedinreal
applications can be very large with many hidden layers and thousands of neurons and links.
Furthermore,theydonothavetobefullyconnected,sonoteveryneuronofalayernecessarily
needs toforward its output to every neuron of the next layer. Various architectures have been
proposed to build neural networks. One of the simplest architectures is the feed‐forward
network: neurons come in their most basic variant, and nobacklinks exist so that data simply
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1667
FINANCIAL MANAGEMENT
flowfromlefttoright.6Duetotheirhighcomplexity,neuralnetworksareinherentlydifficultto
interpret. In general, very little information can be inferred from the hidden layers, which
represent the learned knowledge of a neural network. Improving the interpretability of neural
networks is subject to ongoing research in computer science.
In addition to the methods just discussed, there are older ML methods that (compared to
newer methods) typically achieve worse prediction performance and/or provide lower
interpretability, such as the naïve Bayes method (Rish, 2001), which uses Bayes' theorem to
classify observations into categories, or support vector machine (SVM) methods (Hastie et al.,
2009, pp. 417–455). Werefer theinterested readerto thementioned literaturefor more details
on these methods.
2.2 | Unsupervised learning
The purpose of unsupervised learning is data structure inference. Since the data structure
subsumesmanydifferenttypesofinformation,wedividethemethodsofunsupervisedlearning
intodifferentsubcategories.Thetwomostcommonsubcategoriesinunsupervisedlearningare
clustering and dimensionality reduction.
Inclustering,observationsaregroupedinawaythatresultsinhighwithin‐groupsimilarity
andlowcross‐groupsimilarity.Variouskindsofclusteringmethodshavebeenproposed.First,
centroid‐based methods form clusters by arranging the observations around multiple central
points (so‐called centroids). After the initial positioning of the centroids, iterative updates of
their position yields increasingly suitable clusters. A common example of a very early but still
heavily used centroid‐based method is K‐means (MacQueen, 1967). Second, density‐based
methodsbuildclustersdependingonthedifferingdensityinthespaceofobservations.Inother
words, they group observations with many similar observations nearby into clusters. An
exampleofadensity‐basedclusteringmethodisDBSCANfromEsteretal.(1996),whichisalso
one of the most widely applied clustering methods. Third, distribution‐based methods assign
observationstoclustersbasedonwhethertheylikelybelongtothesamestatisticaldistribution.
Hence, these methods require knowledge of the distribution of the underlying data process in
advance.Fornormallydistributeddata,Gaussianmixturemodelsarewidespread(Rasmussen,
1999). Finally, hierarchical methods construct clusters that consider the hierarchical
relationship in the data. They start with initial clusters, where each cluster consists of a
singleobservation.Then,theyiterativelycombinesmallerclustersintolargerclusterstobuilda
hierarchy. A common method for hierarchical clustering is BIRCH (Zhang et al., 1996).
Dimensionality reduction aims at increasing the information density of the given data by
decreasing their dimensionality while retaining most of the inherent information. There are
various methods for dimensionality reduction, of which we cover only the two most common
ones.First,methodsbasedonprincipalcomponentanalysis(PCA)derivelinearcombinationsof
6Advancedneuralnetworksemploymorecomplexneuronsandarchitectures.Recurrentneuralnetworks(RNNs)aredesignedfor
sequentialdatasuchastext(Medsker&Jain,2001).ThespecialarchitectureofRNNsallowshidden‐layerneuronstoaccumulate
informationovermultiplerelatedobservations(forinstance,wordsinasentence).Therearedifferentpossibilitiesfordesigningthis
informationstoragemechanism.Widespreaddesignexamplesaregatedrecurrentunits(GRU)andlongshort‐termmemory(LSTM).
Convolutionalneuralnetworks(CNNs)areanothertypeofadvancedneuralnetworkswhosegeneralarchitecturefitswellwithvisual
datasuchasimagesandvideos(Albawietal.,2017).Simplyput,theirhiddenlayersrepresenttrainablefiltersthatiterativelydetect
increasinglycomplexstructures.ThearchitectureofCNNsistypicallyhighlycustomisedtowardaspecificapplication.Adequately
designedCNNsshowoutstandingperformancefortaskssuchasfacedetectionorgeneralimagerecognition.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1668
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
the original variables (‘principal components’) that cover as much of the data's variance as
possible. While the basic variant of PCA is inherently linear, nonlinear generalisations also
exist. For more details on the different PCA‐based methods, see, for instance, Hastie et al.
(2009, pp. 534–552). Second, methods based on neural networks reduce dimensionality with
special architectures. A widely used method is the autoencoder neural network (Goodfellow
et al., 2016, pp. 499–523). An autoencoder consists of an encoder network that creates a
condensed representation of the input data and a subsequent decoder network that
reconstructs the original data from the condensed representation. A special bottleneck layer
connects theencoder and decoder networks to train them ongiven data.If theautoencoder is
able to reconstruct the original data well, then the condensed data representation in the
bottlenecklayerhassuccessfullyretainedmostoftheinformationinthedatawhilereducingits
dimensionality.
Inadditiontoclusteringanddimensionalityreduction,furthersubcategoriesofunsupervised
learningexistbutare(todate)usedsomewhatlessoftenforapplicationsinfinance.Association
rule mining tries to identify relations between variables (Agrawal et al., 1993). For instance, it
can learn from customer purchase data which products are often bought together. Outlier
detection tries to find observations that substantially differ from the remaining data. While
manytraditionalmethodsforoutlierdetectionexist,ML‐basedmethodsoftenprovidesuperior
performance, especially in high‐dimensional settings (Domingues et al., 2018). Methods in
syntheticdatagenerationtrytogeneratenewdatathatsatisfycertainrequirements.Generative
adversarial networks, for instance, use neural networks to create new, synthetic data that
closely mimic the given training data (Goodfellow et al., 2020). Their neural network
architecture makes them especially useful for unconventional data, for example, to create
artificial images that are similar to existing images.
2.3 | Application: Real estate price prediction
To illustrate the differences between ML methods and more traditional approaches, we now
applyMLtotheproblemofrealestatepriceprediction.Thepredictionofrealestatepricesisa
particularlygoodexampletoillustratethebenefitsofMLtosolveproblemsinfinanceforthree
reasons. First, real estate is one of the most important asset classes in the economy. In the
United States, the total value of real estate assets is comparable to the size of the equities and
fixed income markets combined. For most households, real estate is the greatest source of
wealth.TheGlobalFinancialCrisisin2007/2008exemplifiedhowspillovereffectsfromthereal
estate sector can destabilise economies around the world. Consequently, the reduction of
predictionerrorsintheareaofrealestatepricingisofparticulareconomicimportance.Second,
realestateassetsshowahighlevelofheterogeneity(eachpropertyisunique),whichmakesreal
estatepricingchallenging.Third,thehighnumberofpropertycharacteristicsvariablesaswell
as potentially relevant nonlinearities and interaction effects makes real estate pricing an
inherently high‐dimensional problem, where ML provides unique benefits over traditional
methods.Thetraditionalapproachtoderivepriceestimatesforindividualpropertiesishedonic
pricing. Hedonic pricing first regresses the property characteristics on the observed property
priceswithOLStoobtainalinearpricingmodel.Then,thismodelcanproducepriceestimates
for new, previously unobserved properties. It is also possible to interpret the regression
coefficients as the characteristics' shadow prices. However, hedonic pricing relies on an
inherentlylinearmodelandthereforedoesnotdirectlyconsidernonlinearitiesandinteraction
1468036x,
2023,
5, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on [29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1669
FINANCIAL MANAGEMENT
FIGURE 4 Predictionperformanceandaveragepricingerrorsofhedonicpricing(OLS)andMLmethods.
PanelAdepictsthepredictionperformance(R²)oftraditionalhedonicpricing(OLS)comparedtodifferentML
methods.WhilemostMLmethodsoutperformOLS,theboostedregressiontreesmethodperformsbestbyfar
andalmostdoublestheOLSperformance.PanelBshowstheaveragepricingerror(measuredbymeanabsolute
error[MAE])forthebest‐performingMLmethod,boostedregressiontrees,andfortheOLSbaselineinthefive
pricequintiles.Inallquintiles,theboostedregressiontreesmethodsignificantlyoutperformsOLS.The
reductioninpricingerrorfromMLismostpronouncedinthehighestpricequintile,whereOLSperforms
relativelypoorly.
effects. For instance, we can assume relevant interactions between lot size and location: an
additional m² in lot size for a property in a city centre is likely worth more than in a suburb.
While we could manually add such specific effects to the linear model, there may exist a
plethora of unknown nonlinear and interaction effects. By ignoring these effects, the linear
model of hedonic pricing potentially leaves important information contained in the data
unexploited. ML methods, in contrast, automatically consider nonlinearities and interactions.
Therefore, supervised ML can potentially generate price predictions that exhibit lower pricing
errorthanthelinearmodelfromhedonicpricing.Inthefollowing,westudywhetherandhow
ML provides superior price estimates for individual real estate assets.
We exploit a comprehensive collection of more than four million residential real estate
listingsinGermanybetweenJanuary2000andSeptember2020fromthefivemajorrealestate
online platforms and major newspapers.7 The data set contains offer prices and all relevant
individualpropertycharacteristics(floorarea,numberofrooms,constructionyear,location,lot
size, etc.). We use these data to train different ML models for the prediction of individual
property prices and compare these models with the linear OLS model from hedonic pricing.
Panel A in Figure 4 shows the key result of our analysis.8 ML methods strongly improve the
accuracyofpricepredictionsovertheOLSbaseline.Ourbest‐performingMLmethod,boosted
regression trees, dramatically increases out‐of‐sample R2 to 77%, compared to 40% for OLS;
thus, it almost doubles the amount of explained price variation. On average, the predictions
fromboostedregressiontreesdeviatefromtheactualpricesbyapproximately27%,comparedto
44% for OLS. In monetary terms, the superior prediction performance of boosted regression
7Accordingtothedataprovider,thedatasetcoversmorethan95%ofthepubliclistingsduringthegivenperiod.
8Seetheonlineappendixformoredetailsonthesampleandourmethodology.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1670
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
trees corresponds to an average pricing error of approximately 94,000 EUR, compared to
176,000 EUR for OLS. Since the mean property price in our sample is 393,000 EUR, the
improvements in pricing accuracy from ML are not only statistically significant but also
economically large.
While the improvements in pricing accuracy induced by ML are already impressive on
average, their benefits become even more pronounced at the upper end of the price range.
Panel B in Figure 4 depicts the prediction performance of the best‐performing ML method,
boosted regression trees, compared to that of OLS in the five property price quintiles. The
boostedregressiontreesmethodoutperformsOLSinallquintiles.WhileOLSperformsworstat
the extremes of the price range, ML is especially useful in reducing the pricing error for the
most expensive properties. In the highest price quintile, the boosted regression trees method
lowers the average pricing error to 24%, compared to 50% for OLS. In monetary units, the
superiorpredictionperformanceofboostedregressiontreesrelativetothatofOLScorresponds
to a reduction in the average pricing error by more than 240,000 EUR in the highest price
quintile. Given that the average property price in the top quintile is approximately 884,000
EUR, the improvements in pricing power from ML are dramatic. Our results indicate that
nonlinearitiesandinteractioneffectsarerelevantinrealestatepricingandespeciallyimportant
for the most expensive properties.
OurresultsdemonstratethebenefitsofusingMLtoreducethepredictionerrorineconomic
prediction problems. ML can yield a statistically and economically significant reduction in
predictionerrorcomparedtotraditionallinearregressionwithOLS inaddressingtheproblem
ofrealestatepriceprediction.ThealreadylargebenefitsofMLonaveragefurtherincreasefor
assets at specific price ranges. Hence, ML methods not only improve prediction accuracy in
general but also especially for observations where traditional approaches struggle.9
2.4 | Limitations, caveats, and drawbacks of ML
While the results from our illustrative application of ML to real estate asset pricing show the
benefits of ML over traditional methods for problems with high‐dimensional data, there also
exist limitations, caveats, and drawbacks of using ML. In the following, we discuss three
important aspects in detail.
First, ML methods tend to exhibit low interpretability. While ML models can produce
predictionswithlowpredictionerror,itisoftennotdirectlyobservablehowthealgorithmhas
generated its results. Hence, ML is generally not suited for problems that require a deep
understandingoftheeconomicdeterminantsofthepredictiontarget.Nevertheless,thequickly
advancingfieldofinterpretableMLtriestooffersolutionstothemodelinterpretabilityproblem
with several kindsof approaches(see,for instance,Burkart &Huber, 2021, for anoverviewof
the available methods).
9OurrealestateassetpricingexampleisprimarilymeanttoillustratetheadvantagesofMLovertraditionalmethodsforaproblemwith
high‐dimensionaldata.Nevertheless,itrepresents(tothebestofourknowledge)thefirstapplicationofMLtorealestatepricingforan
entiremajoreconomy,spanningacomprehensivedatasetofallrealestatelistings—both,onlineandoffline—forasampleperiodof
morethan20years.Ourdatasetcontainsmorethanfourmillionobservations,whichfarexceedsthescaleofpriorwork.Mostexisting
studiesintherealestateassetpricingliteratureapplyMLtopredictindividualhousepricesinnarrowregionswithindifferentcountries,
suchastheUnitedStates(Mullainathan&Spiess,2017;Park&Bae,2015;Pérez‐Raveetal.,2019),France(Tchuente&Nyawa,2022),
Spain(Rico‐Juan&TaltavulldeLaPaz,2021),theNetherlands(Gulikeretal.,2022),Turkey(Erkeketal.,2020),Hong‐Kong(Hoetal.,
2021),andColombia(Pérez‐Raveetal.,2019).Inadditiontopredictingindividualrealestateprices,asmallgroupofstudiesusesMLto
predictthegeneralpricelevelintherealestatemarket(Milunovich,2020;Yuetal.,2021).
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1671
FINANCIAL MANAGEMENT
Second,MLgenerallyrequireslargedatasets.Datasetscanbelargeintwodimensions:the
number of relevant variables and the number of observations. ML offers benefits over
traditional methods for prediction tasks if the number of relevant variables is large relative
to the number of observations. At the same time, ML usually provides good prediction
performance only if there is a high number of observations on which an ML model can be
trained.Unfortunately,large‐scaledataarenotalwaysavailableformanyresearchquestionsin
finance.Insomecases,usingMLmodelsthathavealreadybeenpretrainedwithlargeamounts
ofcomparabledatacansolvethisproblem.SuchpretrainedmodelsexistformanycommonML
tasks,suchastextualanalysisorfacerecognition,soresearcherscandirectlyapplythemtothe
problem at hand independent of the amount of available data. In addition, the general trend
toward increasing data collection in all aspects of life should more and more alleviate the
data problem.
Finally, using ML often has high computational costs. Compared to traditional methods
suchaslinearregression,trainingML modelsrequiressignificantlymore timeandcomputing
power. The problem typically becomes worse with more sophisticated ML methods. In
particular, neural networks with complex architectures typically have the highest computa-
tional costs. As a result, using cloud computing services often becomes necessary to deal with
this problem.
3 | TAXONOMY OF ML APPLICATIONS IN FINANCE
AnincreasingnumberoffinancepapersthatuseMLinatleastsomepartoftheirstudygoon
tobepublished.However,manyresearchersarestillunawareofhowandwheretoapplyMLin
the fieldof finance. In this section, we present a taxonomyof existing ML applications, which
servesmultiplepurposes.First,itoutlineswhereMLcanaddvalueinfinanceresearch.Second,
it provides a systematic overview of existing ML applications in the field of finance. Third, it
enables a better understanding of new contributions and how they relate to the existing
literature. Finally, it may guide researchers in discovering possible applications and thus may
facilitate new ML studies in finance.
As explained above, ML solves different problems compared to traditional econometric
methods.Theworkhorsemodeloffinanceresearch,linearregressionwithOLS,hasonemajor
objective: identification of causal relationships between economic variables to explain
economic phenomena. In contrast, ML provides predictions that minimise prediction error
or infers structural information from given data.
TosurveytheMLliteratureinfinance,wefirstidentifyML‐relatedpapersinmajorjournals
infinance,theNBERworkingpaperseries,andtheFinancialEconomicsNetworkoftheSSRN
preprint repository; then, we search for ML method names and their variations (e.g., LASSO,
random forest, etc., see Section 2). We study these papers and categorise the ML research
strategies in these papers into the following three distinct archetypes:
(1) Construction of superior and novel measures: y = βX + ε.
(2) Reduction of prediction error in economic prediction problems: yˆ = f (X).
(3) Extension of the existing econometric toolset: y = βX + ε and ML.
StudiesofthefirstarchetypeuseMLtoconstructasuperiorornovelmeasureforoneofthe
independent variables X. The main analyses of these papers still largely rely on a traditional
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1672
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
(linear) model, which is estimated, for example, with OLS. Studies of the second archetype
use ML to reduce the prediction error of predictions yˆ in economic prediction problems.
Supervised ML methods achieve superior prediction performance by using flexible functional
forms f (*) inthepredictionmodel.StudiesofthethirdarchetypeuseMLtoextendtheexisting
econometric toolset. ML methods either serve as new econometric methods themselves or
optimise some part of a traditional econometric method. In the following subsections, we
review the literature related to each of the three archetypes of ML applications in finance in
detail.10
3.1 | Construction of superior and novel measures
The first archetype of ML applications in finance is the construction of superior and novel
measures. Studies of this archetype use ML to extract information from high‐dimensional,
unconventional data such as text, images, or videos and construct a numerical measure of an
economicvariable.Fortextualdata,traditionalapproachesusewordcountsbasedondomain‐
specificdictionaries.11Forimageandvideodata,onlyhumanassessmentshavebeenavailable
for a long time. ML‐based approaches provide easier and, at the same time, more powerful
access to the information contained in unconventional data. All types of ML methods are
applicable:predictionsfromsupervisedlearning,datastructureinformationfromunsupervised
learning, and results from other types of ML can be used to construct measures of economic
variables.
The superior or novel measure finally serves as an independent variable in the main
analysisofaneconomicrelation.Usingsuperiormeasures(i.e.,withlowermeasurementerror
thanexistingmeasures)reducesattenuationbias,whichleadstomorepreciseestimatesofthe
parameters describing an economic relationship. Novel measures enable new analyses with
previously unmeasurable economic aspects. In the main analysis, most studies that construct
ML‐basedmeasuresapplytraditionaleconometricmethodssuchaslinearregressionwithOLS.
Table2presentsaselectionofstudiesthatuseMLtoconstructsuperiorornovelmeasures.
Inthefollowing,wepresenttheminthreecategories:(1)measuresofsentiment,(2)measures
of corporate executives' characteristics, and (3) measures of firm characteristics.
3.1.1 | Measures of sentiment
Measures of sentiment describe beliefs of people, usually on a positive–negative scale. Most
studies in this subcategory construct measures of sentiment from textual data. There are
multiple approaches to construct a one‐dimensional (positive vs. negative) measure of
sentimentfromtextualdata.LoughranandMcDonald(2011)presentadictionaryapproachto
derive sentiment from financial texts. More specifically, they count negative words based on a
finance‐specificwordlist.Dictionaryapproaches,however,missthecontextofwordswithina
sentence (Loughran & McDonald, 2016). In contrast, flexible ML‐based approaches can
10Giventhequicklyevolvingnatureofthefield,ourreviewisnecessarilyselectiveregardingsomeMLapplications.Forinstance,we
maynotconsiderimportantpapersoutsideofthe‘standard’financedomain,suchasgenuinecomputersciencepapersthatapplyMLto
specificfinanceproblems.Finally,ourmanualreviewistoacertaindegreesubjective,especiallycomparedtoautomatedreview
techniques(suchastextualanalysis[Azizetal.,2022]orcitation‐basedapproaches[Goodelletal.,2021]).
11SeeLoughranandMcDonald(2016)foranoverviewofmostlytraditionaltextanalyticsmethodsinaccountingandfinance.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|  1468036x, 2023, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408 by Cochrane Philippines, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1673
| HOANGANDWIEGRATZ |     | EUROPEAN |
| ---------------- | --- | -------- |
FINANCIAL MANAGEMENT
TABLE 2 OverviewofstudiesthatuseMLtoconstructsuperiorandnovelmeasures
ThistablereportsanoverviewoftherelevantstudiesinfinancethatapplyMLtoconstructsuperiorandnovel
measures.Therearethreemaincategories:measuresofsentiment,measuresofcorporateexecutives’
characteristics,andmeasuresoffirmcharacteristics.
| Category            | Subcategory | Measures                         |
| ------------------- | ----------- | -------------------------------- |
| MeasuresofSentiment | Stocks      | – Investorsentimentinsocialmedia |
– Sentimentinnews
–
Sentimentinanalystreports
–
Sentimentinannualreports
|     | SovereignDebt | – Sentimentinnews                |
| --- | ------------- | -------------------------------- |
|     | Products      | – Consumersentimentinsocialmedia |
– Expertsentimentinproduct‐
technologyarticles
| MeasuresofCorporate        | PersonalityTraits | – BigFivescores |
| -------------------------- | ----------------- | --------------- |
| Executives’Characteristics |                   | –               |
Risktolerance
–
|     | Beliefs  | Confidenceinexpressingopinions   |
| --- | -------- | -------------------------------- |
|     | Emotions | – Facialemotions(e.g.,happiness, |
sadness,anger,fear,disgust)
–
Verbalemotions(e.g.,positive,
negative,warmth,ability)
– Vocalemotions(e.g.,valence,
arousal,happiness,sadness)
–
|     | ActionsandWorkingPatterns | Answeravoidanceinconferencecalls |
| --- | ------------------------- | -------------------------------- |
– Workingstyle(high‐vs.low‐level
activities)
–
Communicationstyle
|     | Quality | – Expectedshareholdersupport |
| --- | ------- | ---------------------------- |
|     | Looks   | – (Facial)Attractiveness     |
–
(Facial)Trustworthiness
–
(Facial)Dominance
– (Facial)Masculinity
MeasuresofFirm FinancialCharacteristicsand – Financialconstraints
– Riskexposures(e.g.,COVID‐19,
| Characteristics | RiskExposures |     |
| --------------- | ------------- | --- |
cybersecurity)
|     | CorporateCulture | – Culturalvalues(e.g.,innovation, |
| --- | ---------------- | --------------------------------- |
integrity,teamwork)
– Genderculture
– Boardresponsibilities
–
|     | Connectedness | Politicalconnectedness |
| --- | ------------- | ---------------------- |
–
Venturecapitalcommunities
– Mutualfundvotingbehaviour

|
1674
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
consider not only the context of words within a sentence but also how different sentences
interrelatewitheach other.Foranextensive review ofsentimentwith traditionaleconometric
and ML‐based approaches, see Algaba et al. (2020).
Sentimentexistsformanytopicsandisderivedfrommanysources.Infinance,ourinterest
mainly lies in the aggregate sentiment of markets such as the stock market, which is the most
common target of ML‐based measures of sentiment. The majority of the relevant studies use
measures of sentiment for stocks to study their effect on future stock returns and various
financial reporting numbers.
There are multiple studies that construct a measure of investor sentiment from social
media.AntweilerandFrank(2004)usetheMLmethodsnaïveBayesandSVMtoclassifyuser
posts on the Yahoo Finance message board as positive or negative. Then, they aggregate their
classifications to construct a measure of stock market sentiment. Renault (2017) similarly
classifiesuserpostsonthefinance‐focusedsocialnetworkStockTwitstoconstructameasureof
investor sentiment. Vamossy (2021) also relies on StockTwits but measures investor emotions
by extracting different emotional states from user posts with textual analysis based on deep
learning. The studies by Sprenger et al. (2014), Bartov et al. (2018), Giannini et al. (2018), and
Gu and Kurov (2020) derive investor sentiment from user posts on Twitter. Liew and Wang
(2016)alsoapplyMLtoextractsentimentinformationfromTwitterbutforpre‐IPOsentiment.
Inadditiontosocialmedia,newsarticlesareanothersourceofsentimentforstocks.Barbon
et al. (2019) enhance the naïve Bayes method to build a sentiment variable based on firm‐
specific news. Ke et al. (2019) implement a customised ML‐based approach that specialises in
extracting information relevant for stock returns. Their method then allows them to extract a
measureofsentimentforstocksfromDowJonesNewswirearticles.Similarly,Boudoukhetal.
(2019) also analyse Dow Jones Newswire articles but focus on the saliency of firm‐specific
news.ManelaandMoreira(2017)deviatefromthetraditionalmeasuresofsentimentthatusea
positive–negative scale. Instead, they construct a measure of stock market uncertainty from
Wall Street Journal front‐page articles. von Beschwitz et al. (2020) study how ML‐based news
analytics (i.e., computer algorithms that investors use to interpret financial news) affect stock
prices, trading volumes, and liquidity. Calomiris and Mamaysky (2019) use ML to measure
sentiment from country‐level news articles and study how it affects returns and volatilities. In
addition to the analysis of text, Obaid and Pukthuanthong (2022) apply ML to news photos to
derive a measure of sentiment for stocks and find that it can act as a substitute of text‐based
measures.
Otherstudiesuseanalystreportsorannualreportsformeasuresofsentiment.Huangetal.
(2014) apply the naïve Bayes method to analyst reports to construct a measure of stock
sentiment. Azimi and Agrawal (2021) apply deep learning methods to 10‐Ks to measure
sentiment and study its effect on abnormal returns and trading volumes.
Whilemost studies that construct ML‐based measures of sentimentconsider sentimentfor
stocks,Cathcartetal.(2020)studysentimentforsovereigndebtmarkets.Morespecifically,they
leverage news sentiment information from Thomas Reuters News Analytics to investigate the
impact of media content on sovereign credit risk.
Beyondsentimentfor financialmarkets, two studiesexamine sentimentfor products.Tang
(2018)usesacommercialservicetocreateameasure ofconsumersentimentbasedonTwitter
posts. The subsequent main analysis studies the effect of consumer sentiment on firm sales.
Nauhausetal.(2021)constructameasureofexpertsentimentfromarticlesconcerningspecific
technologydomainsandthenstudyhowitaffectsfirms'capitalallocationamongthebusiness
units engaged in these domains.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1675
FINANCIAL MANAGEMENT
3.1.2 | Measures of corporate executives' characteristics
Theprominentroleofafirm'sleadershipanditslargeimplicationshasledtoavastamountof
financeliteraturethatstudiesvariousaspectsofcorporateexecutives.Relatedtothisstreamof
the literature, ML enables the construction of superior and novel measures of executives’
characteristics. While most measures in this category rely on textual data, there are also some
studies that construct measures from analysing images and videos.
Multiple studies construct ML‐based measures of executives' personality traits. Gow et al.
(2016) use ML to extract CEOs' Big Five personality scores (agreeableness, conscientiousness,
extraversion, neuroticism, and openness to experience) from the Q&A part of conference call
transcripts. Then, the authors use the extracted scores to analyse the effect of personality on
financing choices, investment choices, and operating performance. Similarly, Hrazdil et al.
(2020) determine the Big Five personality scores of CEOs and CFOs by using the commercial
serviceIBMWatsonPersonalityInsights.Fromthesescores,theyconstructanovelmeasureof
executives' risk tolerance to analyse its effect on audit fees.
Other studies construct measures of executives' own beliefs. For instance, Du et al. (2019)
applyMLtomutualfundmanagers'letterstoshareholderstoconstructameasureofmanagers'
level of confidence in expressing opinions. Their main analysis then studies the effect of
confidence on future performance.
Recent advances in ML also enable studies that construct measures of executives' emotions.
Akansu et al. (2017) apply ML‐based face‐reading software to videos of CEOs during press
interviewstoextractfacialemotionsandquantifyCEOmood.Theymeasureemotionssuchas
anger,disgust,fear,happiness,sadness,orsurpriseandstudytheireffectonfirmperformance.
HuandMa(2021)useMLtoconstructmeasuresofstartupfounders'emotionsduringinvestor
pitch videos. More specifically, they measure three dimensions of emotions: facial emotions,
verbalemotions,andvocalemotions.Finally,theyanalysetheeffectofthethreedimensionson
theprobabilityofobtainingaventurecapitalinvestment.BreabanandNoussair(2018)useML‐
basedface‐readingsoftwaretoextracttheemotionalstateoftradersinanexperimentalsetting.
Another stream of the literature addresses executives' actions and working patterns. Barth
etal.(2020)proposeanML‐basedmeasureofthedegreetowhichexecutivesobstructtheflow
of information during earnings conference calls by giving so‐called nonanswers to investors'
and analysts' questions. Bandiera et al. (2020) apply ML to CEO survey data to construct a
measureofCEOworkingstyle.Morespecifically,theirmeasurecaptureswhetheragivenCEO
performs more low‐level or more high‐level activities. Then, this novel measure enables the
authorstostudyfirm‐CEOassignmentfrictions.Choudhuryetal.(2019)constructameasureof
executives' communication style by applying ML to transcripts and videos from interviews of
emerging market CEOs. Dávila and Guasch (2022) construct a measure of entrepreneurs'
nonverbal communication style during pitch presentations with ML‐based computer vision
software and analyse its relation to firm valuations and funding success rates.
The study by Erel et al. (2021) uses ML to measure director quality. They predict the
(excess)levelofdirectors’shareholdersupportoverthefirst3yearsoftenureusingvariousML
methods. By interpreting these predictions as a measure of director quality, the authors study
firms’ decision‐making process in the selection of corporate directors.
Finally,thelargeamountofimagedatafreelyavailableontheinternetallowsmanystudies
to systematically exploit the information that the looks of corporate executives—in particular,
their facial traits—may contain. Hsieh et al. (2020) extract a measure of trustworthiness from
executives' business headshot images. More specifically, they detect and use certain facial
1468036x,
2023,
5, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1676
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
features(suchaseyebrowangleorfaceroundness)topredictperceivedtrustworthiness.Their
main analysis studies the effect of executives' trustworthiness on audit fees. Peng et al. (2022)
leverage the social network LinkedIn and apply ML to profile photos of sell‐side analysts to
constructmeasuresoftrustworthiness,dominance,attractiveness,etc.Kamiyaetal.(2019)use
MLtofirstmeasurethewidth‐to‐heightratioofCEOs'facesfromportraitphotosandtheninfer
a measure of facial masculinity to study its effect on firms' riskiness.
3.1.3 | Measures of firm characteristics
StudiesinthethirdcategoryconstructmeasuresoffirmcharacteristicswithMLmethods.The
first subcategory consists of measures of firms' financial characteristics and risk exposures.
BuehlmaierandWhited(2018)applyMLtoannualreportstoconstructameasureoffinancial
constraints. Their ML‐based measure achieves superior performance compared to the existing
measures. Hanley and Hoberg (2019) construct a measure of aggregate risk exposure in the
financialsectorfromindividualbanks'annualreportsbyusingacommercialML‐basedservice.
They use their measure to study the effect of financial sector risk on banks' stock returns and
volatility as well as bank failure. Li et al. (2021a) apply ML‐based textual analysis methods to
construct measures of firms' exposure and response to COVID‐19 based on the information
from earnings calls. Alan et al. (2021) measure firm‐level cybersecurity risk with ML‐based
methods from computational linguistics. More generally, Lima and Keegan (2020) provide
an overview on how ML‐based textual analysis can be applied to social media to assess
cybersecurity risk.
ML can also help to study corporate culture. Li et al. (2021b) extract aspects of corporate
culturefromconferencecalltranscriptswithMLandbuildmeasuresoffivedifferentcorporate
culturevalues.Using thesemeasuresallows themtoanalysetheeffectofcorporate cultureon
firm policies such as executive compensation and risk‐taking. Furthermore, they study the
effect on firm performance metrics such as operational efficiency and firm value. Adams,
Akyol,etal.(2021)applyMLtofirms'reportstoagender‐equalityagencytoconstructmultiple
measuresofcorporategenderculture.Theirnovelmeasuresallowthemtosystematicallystudy
how firms treat female employees. Adams, Ragunathan, et al. (2021) apply ML‐based textual
analysis to extract boards' and board committees' responsibilities and meeting frequencies.
Finally, the capabilities of ML enable the construction of novel measures of firms'
connectedness. Mazrekaj et al. (2021) apply ML to construct a measure of firms' political
connections, which helps identify potential conflicts of interest. Bubna et al. (2020) study
venture capital syndications and create a measure of venture capital relatedness. More
specifically, they cluster venture capital firms using ML to identify syndication groups and
study their effect on startup maturation and innovation. Bubb and Catan (2021) apply
clustering methods from unsupervised learning to mutual funds' proxy votes to determine to
which voting parties they belong.
3.2 | Reduction of prediction error in economic prediction problems
Studies of the second archetype of ML applications in finance apply ML to reduce prediction
error in economic prediction problems. While many problems in economics require the
identification of causal relationships between economic variables, some problems directly
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on [29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1677
FINANCIAL MANAGEMENT
requireprediction.MLcanreducethepredictionerrorinsuchproblems,thatis,generatemore
accurate predictions than simpler approaches such as fitted values from linear regression
with OLS.
Predictions can be generated from numerical data as well as unconventional data such as
text,images,orvideos.SincethepurposeofMLinthiscategoryistominimisepredictionerror
ineconomicpredictionproblems,bydefinition,onlysupervisedMLisdirectlyapplicablehere.
Given the large number of available ML methods, most studies use a multitude of different
methods to assess which method works best on the given data. Applying supervised ML
methods finally results in predictions of an economic variable, which directly helps in solving
an economic prediction problem.12
Table 3 gives an overview of the relevant studies that use ML in economic prediction
problems to reduce prediction error. In the following, we present these studies in the three
categoriesof(1)predictionofassetpricesandtradingmechanisms,(2)predictionofcreditrisk,
and (3) prediction of firm outcomes and financial policy.
3.2.1 | Prediction of asset prices and trading mechanisms
The prediction of asset prices and trading mechanisms is of central importance in studying
capitalmarkets.MLcanreducethepredictionerrorinvarioustypesofpredictionproblems.We
distinguish among predictions in the following seven different subcategories: equities, bonds,
foreign exchange, derivatives, general market prices, investors, and market microstructure.
The most common ML‐based prediction in the subcategory of equities is the prediction of
future stock returns, which is closely related to the field of cross‐sectional asset pricing.
RasekhschaffeandJones(2019)provideanoverviewoftheuseofMLforpredictingthecross‐
section of stock returns and the selection of individual stocks. Martin and Nagel (2022)
emphasisethechallengesofcross‐sectionalassetpricingwithhigh‐dimensionaldata.Guetal.
(2020)directlypredictfuturestockreturnsbasedonfirmcharacteristics,historicalreturns,and
macroeconomic indicators. They use ML methods with varying complexity ranging from
regularised linear models to neural networks. Furthermore, they analyse which predictor
variablesarethemostinformativeinpredictingthecross‐sectionofstockreturns.Rossi(2018)
predictsfuturestockreturnsandfuturestockvolatilitybasedonestablishedpredictorvariables
from Welch and Goyal (2008). The studies by Moritz and Zimmermann (2016), Kelly et al.
(2019), Gu et al. (2021), and Freyberger et al. (2020) all predict future stock returns based on
firmcharacteristicsandhistoricalreturns.However,theydifferwithrespecttothespecificML
methodsapplied.Grammigetal.(2020)constructahybridapproachthatcombinestraditional
methodsbasedonfinancialtheorywithMLtopredictfutureexcessstockreturns.Chincoetal.
(2019)applyLASSOtopredictultra‐short‐termfuturestockreturnsbasedonthecross‐section
ofultrashort‐termhistoricalreturns.Akyildirimetal.(2021)usevariousMLmethodstopredict
intraday excess returns based on high‐frequency order and trade information. Amel‐Zadeh
etal.(2020)predictabnormalstockreturnsaroundearningsannouncementsbasedonfinancial
statementvariables.TheyuseLASSO,randomforests,andneuralnetworksandanalysewhich
financialstatementvariablesarethemostinformative.Chincoetal.(2021)useridgeregression
12Moststudiesonlyfocusonthepredictionsthemselves.However,therearealsosomestudiesthattrytoanalysehowthepredictor
variablesaffectthepredictions.WhilemostMLmodelsdonotallowfordirectobservationofhowthealgorithmgeneratesits
predictions,methodsfromthefieldofinterpretableMLtryto‘opentheblackbox’(see,e.g.,Murdochetal.,2019).
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|  1468036x, 2023, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408 by Cochrane Philippines, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1678
EUROPEAN HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
TABLE 3 OverviewofstudiesthatuseMLineconomicpredictionproblems
ThistablereportsanoverviewofrelevantstudiesinfinancethatapplyMLineconomicpredictionproblemsto
reducepredictionerror.TherearethreemaincategoriesofeconomicpredictionproblemsforwhichMLis
relevant:predictionofassetpricesandtradingmechanisms,predictionofcreditrisk,andpredictionoffirm
outcomesandfinancialpolicy.
| Category                   | Subcategory | Predictiontargets |
| -------------------------- | ----------- | ----------------- |
| Predictionofassetpricesand | Equities    | – Stockreturns    |
–
| tradingmechanisms |     | Stockvolatility |
| ----------------- | --- | --------------- |
– Stockcovariance
– Equityriskpremium
–
|     | Bonds | FutureexcessreturnsofUStreasury |
| --- | ----- | ------------------------------- |
bonds
|     | Foreignexchange | – Directionofchangesinexchangerates |
| --- | --------------- | ----------------------------------- |
|     | Derivatives     | – Pricesofoptionsonindexfutures     |
–
Pricesofgeneralderivatives
|     | Generalfinancialclaims | – Stochasticdiscountfactor |
| --- | ---------------------- | -------------------------- |
– Financialcrises
–
|     | Investors | Mutualfundperformance |
| --- | --------- | --------------------- |
– Retailinvestors'portfolioallocations
andperformance
–
|     | Marketmicrostructure | Lifespanoftradingorders |
| --- | -------------------- | ----------------------- |
–
Generalmicrostructurevariables
Predictionofcreditrisk Consumercreditrisk – Generalconsumerdefault
– Creditcarddelinquencyanddefault
–
Billpaymentindevelopingcountries
– Creditcardrepaymentpatterns
|     | Realestatecreditrisk | – Mortgageloanrisk |
| --- | -------------------- | ------------------ |
–
Commercialrealestatedefault
–
|     | Corporatecreditrisk | Firms'creditratingchanges |
| --- | ------------------- | ------------------------- |
– Corporatebankruptcy
– Fintechloandefault
–
Recoveryratesofcorporatebonds
Predictionoffirmoutcomesand Financialoutcomes – Capitalstructure
| financialpolicy |     | – Earnings |
| --------------- | --- | ---------- |
–
|     | Corporatemisconduct | Accountingfraud |
| --- | ------------------- | --------------- |
– Regulatoryviolations
|     | Startups'success | – Startupacquisitions |
| --- | ---------------- | --------------------- |
–
Startupvaluationsandsuccess
probabilities
todeterminetheprobabilityofencounteringstockreturnanomalies.Fengetal.(2020)propose
ML‐based
an method to evaluate the contribution of the plethora of potential risk factors in
explaining stock returns. Two studies focus on financial market volatility: Kogan et al. (2009)
predict future stock volatility based on annual reports; Osterrieder et al. (2020) predict the

|
HOANGANDWIEGRATZ EUROPEAN 1679
FINANCIAL MANAGEMENT
intraday volatility index VIX from option prices. Rossi and Timmermann (2015) use ML to
studyhowstockreturnsandeconomicactivityarerelated.Theyapplyboostedregressiontrees
to predict covariances between stock returns and a daily economic activity index.
Inadditiontopredictionsofindividualstockreturns,MLcanreducethepredictionerrorin
predicting aggregate stock market behaviour, particularly the equity risk premium. Jacobsen
et al. (2019) predict the equity risk premium based on established stock market predictor
variables from Welch and Goyal (2008) with an ensemble of multiple ML models. Routledge
(2019) predicts the equity risk premium from macroeconomic indicators and FOMC texts.
Adämmer and Schüssler (2020) extract topics discussed in general news articles with ML to
predict the equity risk premium.
Some studies predict certain aspects of bonds. For instance, Bianchi et al. (2021) apply
various ML methods to predict future excess returns of US treasury bonds from general yield
data and macroeconomic indicators.
In the subcategory of foreign exchange, the study by Colombo et al. (2019) applies SVM to
predict the direction of changes in exchange rates based on indicators of market uncertainty.
Other studies use ML to price derivatives, which is also an early application of ML in
finance. Hutchinson et al. (1994) price options on the S&P 500 future based on the Black‐
Scholes variables with an early variant of neural networks. Similarly, Yao et al. (2000) price
optionsontheNikkei225future.Inmorerecentwork,DeSpiegeleeretal.(2018)findthatML
methods can price derivatives much faster than advanced mathematical models while
achieving only slightly worse accuracy.
Instead of focusing on certain asset classes, there are also studies concerning general
financial claims. Two studies directly predict the stochastic discount factor. Chen et al. (2019)
use generative adversarial networks based on deep neural networks with different predictors,
such as firm characteristics, historical returns, and macroeconomic indicators. Kozak et al.
(2020)developacustomMLmethodbasedonBayesianpriorstopredictthestochasticdiscount
factorfromfirmcharacteristicsandhistoricalreturns.ThestudybyOhetal.(2006)appliesML
to detect and predict financial crises from financial market volatility. Similarly, Coffinet and
Kien (2019) develop an ML toolkit to detect banking crises.
Inadditiontoassetpricesandreturns,predictionproblemsalsoariseinstudiesconcerning
retail and professional investors' trading decisions and performance. Li and Rossi (2020) apply
boosted regression trees to predict mutual funds' performance, which then allows for fund
selection. Rossi and Utkus (2020) study which type of retail investors benefit (the most) from
robo‐advising. More specifically, they apply boosted regression trees to predict changes in
investors' portfolio allocations and performance.
Finally, some studies focus on predicting certain aspects of the market microstructure with
ML.McInishetal.(2019)applyrandomforeststopredictthelifespanofordersbasedonorder
characteristics and market data. Easley et al. (2021) predict a variety of variables relevant for
market participants, such as bid‐ask spreads, changes in volatility, and sequential return
correlations from established microstructure measures with random forests.
3.2.2 | Prediction of credit risk
Credit risk is a typical economic prediction problem: its ultimate goal is to know which
prospective borrowers will eventually default. As such, ML can lower prediction errors and
improve decision making, such as in loan origination. We divide the current literature
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1680
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
concerning ML‐based predictions of credit risk into the following three subcategories:
consumer credit risk, real estate credit risk, and corporate credit risk.
Studies on consumer credit risk apply ML to make default predictions for any type of
consumercredit.AlbanesiandVamossy(2019)studygeneralconsumercreditdefault.Theyuse
advanced ML methods such as boosted regression trees and deep neural networks to derive
moreaccuratepredictionsfromcreditbureaudatacomparedtostandardcreditscoringmodels.
Furthermore, they analyse which predictors are the most relevant and how the different
predictorsaffectthepredictions.Similarly,Tantri(2021)predictsconsumercreditdefaultwith
boosted regression trees based on borrower and loan characteristics data and finds that using
ML‐based default predictions can improve lending efficiency. Khandani et al. (2010) predict
consumer credit card default based on transaction data and traditional credit bureau data.
Similarly, Butaru et al. (2016) predict credit card default but consider more general account
data andmacroeconomic indicators. Theybothuse tree‐basedML methods thatautomatically
consider nonlinearities and interactions between predictor variables. Butaru et al. (2016) also
attemptstoidentifywhichpredictorvariablesdrivedefaultpredictions.BjörkegrenandGrissen
(2018, 2020) focus on bill payment and apply random forests to mobile phone metadata to
predict the payment of consumer bills in developing countries. The ability to make credit risk
predictions based on easily obtainable data from mobile phones can help unbanked people in
developing countries without a credit score obtain access to loans. Slightly different from the
studies above, Gathergood et al. (2019) use credit card transaction data to predict credit card
repayment patterns. They predict not whether customers pay their credit card bills but how
customers split repayment on multiple cards with different interest rates. They also apply
various ML methods and analyse which predictors are most informative.
Whenever algorithm‐based decisions affect people, algorithmic bias is a potential issue.
SinceML‐basedpredictionsofconsumercreditriskdirectlyaffectcreditapprovaldecisions,itis
necessary that the algorithm does not discriminate against people based on attributes such as
gender or race. The literature does not paint a uniform picture of whether ML reduces or
increases bias in consumer credit decisions. Rambachan, Kleinberg, Ludwig, et al. (2020)
andRambachan,Kleinberg,Mullainathan,etal.(2020)arguethatdiscriminationbyalgorithms
cruciallydependsonthegivendata.Sincealgorithmsbasetheirdecisionsonthedataonwhich
they have been trained, they might propagate biases present in the data. Fuster et al. (2022)
applyML toaconcretedatasettocreateanMLmodelforcreditdecisions.TheyfindthatML
increases the disparity between and within different groups relative to simpler methods. In
particular,itdisadvantagesHispanicandBlackborrowerscomparedtotraditionalapproaches.
Hence, awareness of the potential discrimination by ML‐based algorithms is required if their
predictions influence decisions that directly affect people, such as lending.
On the other hand, there are also studies showing that ML use can decrease bias in
consumer credit decisions. Based on a theoretical model, Philippon (2019) shows how
algorithmscanreducediscriminationincreditmarkets.Dobbieetal.(2021)trainanMLmodel
to maximise expected profit from credit applications and find that the resulting lending
decisionseliminatebias.Kleinbergetal.(2018)showthatincludingproblematicvariables,such
as gender and race, in ML models can actually reduce discrimination. To conclude the
discussion concerning algorithmic bias in consumer credit risk, to date, there is no uniform
picture in the literature. Some studies find that using ML to determine consumer credit risk
increases bias, while other studies find that it decreases bias.
The second subcategory of ML‐based credit risk predictions, real estate credit risk, involves
theriskofmortgagesandcommercialrealestateloans.Sadhwanietal.(2021)usedeepneural
1468036x,
2023,
5, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1681
FINANCIAL MANAGEMENT
networks to predict mortgage loan risk from mortgage origination and performance data and
macroeconomicindicators.Theyalsoanalysewhichpredictorvariablesarethemostimportant
and how they affect the predictions. Cowden et al. (2019) use various ML methods to predict
commercial real estate default based on property characteristics.
CorporatecreditriskisanotherareainwhichMLcanprovidesuperiorcreditriskpredictions.
Jones et al. (2015) predict firms' credit rating changes based on firm fundamentals, analyst
forecasts, and macroeconomic indicators. Tian et al. (2015) and Sermpinis et al. (2022) directly
predict corporate bankruptcy from firms' financial statements and market data. Lahmiri and
Bekiros (2019) similarly predict bankruptcy from firm fundamentals but additionally include
general risk indicators. They use more sophisticated neural networks. Croux et al. (2020) apply
LASSO to predict fintech loan default from loan and borrower characteristics as well as
macroeconomicindicators.Incontrasttotheabovestudies,NazemiandFabozzi(2018)focuson
thetimeaftercreditdefaultandpredicttherecoveryratesofcorporatebondsbasedonbondand
industry characteristics and macroeconomic indicators with various ML methods.
3.2.3 | Prediction of firm outcomes and financial policy
The analysis of the determinants of specific firm outcomes (e.g., capital structure), as an
importantsubjectofstudyinthefieldofcorporatefinance,canalsobethetargetofML‐based
predictions. We divide the current literature in this category into the following three
subcategories based on the specific target of the prediction: financial outcomes, corporate
misconduct, and startups' success.
TwostudiesuseMLtopredictdifferentfinancialoutcomes.Aminietal.(2021)studyfirms'
capital structure as a typical problem in corporate finance. They predict corporate leverage
based on the standard capital structure determinants in the literature (Frank & Goyal, 2009)
with various ML methods. Furthermore, they analyse which determinants are actually
informativeforcapitalstructureandhowtheyinfluencethepredictionsindetail.Thestudyby
van Binsbergen et al. (2020) applies random forests to predict firms' future earnings based on
their accounting data, macroeconomic data, and analyst forecasts.
Corporate misconduct represents another typical prediction problem in the category of firm
outcomes and financial policy. The most common type of corporate misconduct studied in the
literatureisaccountingfraud.Whiletraditionalapproachescanbeusedtopredictaccountingfraud
(such as the Beneish, 1999 model of earnings manipulation), some studies argue that ML can
providesuperiorpredictionaccuracy.Baoetal.(2020)applyboostedregressiontreestorawfinancial
statement variables to predict accounting fraud. They find that ML‐based predictions outperform
simpler existing fraud models. Brown et al. (2020) also predict accounting fraud by applying ML‐
based textual analysis to firms' annual reports. They further analyse which topics are the most
informative and how they affect fraud predictions. Bertomeu et al. (2021) use boosted regression
trees to predict material misstatements based on a large set of potential predictor variables. In
additiontoaccountingfraud,CampbellandShang(2022)applytextualanalysisandMLtopredict
generalviolationsofregulatoryrulesfromfirms' employeereviews onwebsites such asGlassdoor.
Finally, studies in the field of entrepreneurial finance use ML to predict startups' success.
Xiang et al. (2012) apply ML‐based textual analysis to predict startup acquisitions based on
firms' fundamental data and firm‐specific news. Similarly, Ang et al. (2022) predict startups'
valuations and their probabilities of success with ML‐based textual analysis and boosted
regression trees.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|  1468036x, 2023, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408 by Cochrane Philippines, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1682
EUROPEAN HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
| 3.3 | Extension | of the existing | econometric | toolset |
| --------------- | --------------- | ----------- | ------- |
StudiesofthethirdarchetypeofMLapplicationsextendtheexistingeconometrictoolset.Many
commonly used econometric methods contain a prediction component. For instance, the first
stageof instrumentalvariableregressionwith2SLSiseffectivelyapredictionproblem,asonly
the fitted (predicted) value of the instrumented variable enters the second stage. ML methods
can provide superior predictions and hence improve the capabilities of such econometric
methods. On the other hand, some ML methods already serve similar purposes as existing
econometricmethods.Forinstance,clusteringisaknownproblemineconometricsandinML.
ML‐based
methods often provide superior performance, so they can directly extend the
ML‐based
econometric toolset. Table 4 gives an overview of the literature on econometric
methods. We distinguish between causal ML that uses ML for the estimation of treatment
effects and other isolated applications of ML in econometrics. Within the category of causal
ML, we further divide the literature into ML‐enhanced methods for instrumental variable
regression, novel methods of causal trees and causal forests, and other approaches related to
causal ML. In the following, we briefly review the corresponding literature.
| 3.3.1 | Causal | ML  |     |     |
| -------------- | --- | --- | --- |
While traditional econometric methods aim for causality, ML methods are designed for
prediction or for data structure inference. The field of causal ML tries to combine the
OverviewofML‐basedmethodsthatextendtheexistingeconometrictoolset
TABLE 4
ThistablereportsthedifferentcategoriesofML‐basedmethodsthatextendtheexistingeconometrictoolset.
ThelargestcategoryiscausalMLfortheestimationoftreatmenteffects.MLenhancesexistingmethods,such
asinstrumentalvariableregression,orintroducesnewmethods,suchascausaltreesandcausalforests.MLalso
providesothermethodsrelevantfortheestimationoftreatmenteffects,suchasverifyingthebalancebetween
treatmentandcontrolgroups.ThesecondcategoryincludesspecialapplicationsofMLineconometric
approachesinadditiontotreatmenteffects,suchasthegenerationofsimulateddata.
| Category | Subcategory | Approaches |     |
| -------- | ----------- | ---------- | --- |
CausalML Instrumentalvariableregression – 2SLSfirststagewithLASSO,ridgeregression,
orneuralnetworks
|     | Causal‐treebasedmethodsand | –   |     |
| --- | -------------------------- | --- | --- |
Causaltrees
–
|     | applications  | Causalforests                            |     |
| --- | ------------- | ---------------------------------------- | --- |
|     |               | – Applicationsofcausalforests            |     |
|     | OthercausalML | – Directpredictionoftreatmenteffects     |     |
|     |               | – ML‐basedpropensityscore                |     |
|     |               | – Balanceverificationbetweentreatmentand |     |
controlgroups
–
Counterfactualprediction
| SpecialApplications |     | – Predictivepowerofeconomictheories |     |
| ------------------- | --- | ----------------------------------- | --- |
|                     |     | – Completenessofeconomictheories    |     |
–
Handlingofimbalanceddata
–
Generationofartificialdata
|     |     | – ML‐augmentedpreanalysisplans |     |
| --- | --- | ------------------------------ | --- |

|
HOANGANDWIEGRATZ EUROPEAN 1683
FINANCIAL MANAGEMENT
advantagesofbothtocreatesuperioreconometricmethodssuitableforcausalityandespecially
fortheestimationoftreatmenteffects.ThemostdevelopedmethodswithincausalMLareML‐
enhanced instrumental variable regression and the novel methods of causal trees and forests.
Asnotedbefore,MLcandirectlyimprovethefirststageofinstrumentalvariableregression.
By providing better predictions for the instrumented variable, the coefficient of determination
R²ofthefirststageimproves,resultinginmorepreciseestimatesinthesecondstage.Concrete
implementationsofthisideaalreadyexistfordifferentMLmethods,includingLASSO(Belloni
et al., 2012), ridge regression (Carrasco, 2012; Hansen & Kozbur, 2014), and neural networks
(Hartford et al., 2017). However, Angrist and Frandsen (2022) argue that ML‐enhanced
instrumental variable methods might not be superior to existing specialised approaches in
selecting instrumental variables.
For the estimation of treatment effects with ML, causal trees and causal forests are other
well‐developedmethods.TheseminalworkbyAtheyandImbens(2016)introducedthecausal
tree approach, which uses tree‐based ML methods to partition data into subpopulations with
different magnitudes of treatment effects. Causal forests proposed by Athey and Wager (2019)
extend this concept by using an entire ensemble of causal trees. Some studies apply causal
forests to concrete problems in finance. Gulen et al. (2020) apply causal forests to estimate
heterogeneous treatment effects of debt covenant violations on firms' investment levels.
O'Malley (2021) estimates the treatment heterogeneity of a legislative change in home
repossession risk on mortgage default with causal forests.
In addition to causal trees and causal forests, other approaches use ML to improve the
estimation of treatment effects. Lee et al. (2010) estimate the propensity score with ML.
MullainathanandSpiess(2017)suggesttheuseofMLtoverifythebalancebetweentreatment
and control groups. They argue that if it is possible to predict the treatment assignment with
ML, then the split into treatment and control groups cannot be balanced. However, this idea
worksinonlyonedirection:itispossibletoinferimbalancebutnotbalancebyapplyingMLto
predictthetreatment assignment(sincethechosen MLmethods maynot bepowerful enough
to predict the treatment assignment of imbalanced data). Chernozhukov et al. (2017, 2018)
directly calculate treatment effects from ML‐based predictions of treatment assignment and
outcome. Finally, Athey et al. (2019) predict the counterfactual with ensemble methods to
estimate treatment effects from panel data.
3.3.2 | Special applications of ML in econometrics
While causal ML for the estimation of treatment effects is currently the most developed
applicationofMLineconometrics,therearevariousspecialapplicationsofMLineconometrics
that also extend the existing econometric toolset.
Above, we presented how ML can create measures of economic variables. By generalising
this concept, ML can also construct a predictability measure of entire economic theories.
PeysakhovichandNaecker(2017)introducethenotionthatMLcanbeusedtoderiveanupper
bound of the predictive power of theories: the explainable variation in the dependent variable
in a given data set with ML methods. Fudenberg et al. (2019) extend this idea to construct a
completeness measure for economic theories. They calculate completeness by comparing two
prediction errors: the error achieved from using the model and variables hypothesised by
economic theory and the error achievable with ML. In general, different data sets contain
different levels of information, so they allow different levels of predictability. By comparing
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1684
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
predictionerrorstothoseachievablewithMLmethods,itispossibletocreateafairerandmore
informative measure for a comparison of different economic theories.
A different problem relevant in econometrics as well as in ML is imbalanced data. For
instance,inloanperformancedata,actualdefaultsaremuchrarerthanuneventfulrepayments.
Sigrist and Hirnschall (2019) combine ML with traditional econometric methods to address
such problem types. More specifically, they use boosted regression trees to enhance the
traditional Tobit model. They also illustrate the advantages of their method in a concrete
problem by applying it to loan defaults in Switzerland.
Inthefieldofsimulation,Atheyetal.(2021)usegenerativeadversarialnetworksinsteadof
traditional Monte Carlo methods to simulate data that more closely mimic real data. They
illustrate their method by using simulated data for performance comparisons across different
econometric estimators. Adams, Kräussl, et al. (2021) use deep neural networks to generate
artificial paintings to study gender discrimination in art prices.
Finally, Ludwig et al. (2019) introduce ML‐augmented preanalysis plans to avoid p‐hacking.
They augment standard linear regression with new regressors from ML. The new regressors
aggregatemanypotentiallyrelevantvariablesintoasingleindex.Hence,theirmethodavoidsthe
otherwise necessary prespecification of concrete analysis choices in standard preanalysis plans.
4 | FUTURE PROSPECTS OF ML IN FINANCE
ThebenefitsofMLovertraditionalmethodsasillustratedabovetogetherwiththeexistingbut
stilllimitednumberofMLapplicationsinfinancesuggestastillmostlyuntappedpotentialfor
future research. However, it is unclear whether the usage of ML methods will actually gain
broad popularity in the finance community. Furthermore, prospective users of ML need to
knowwhetherMLapplicationscanalsoreachthemostprestigiousjournalsoftheprofessionor
if they tend to be published only in specialty journals. Finally, the different application
categories of ML described by our taxonomy and the wide variety of research fields in finance
make it difficult to pinpoint exactly where the most promising applications of ML in finance
research lie. In this section, we give indicative answers to these questions by systematically
analysing the existing finance literature that already uses ML methods. In particular, we
investigate the publication success of such papers and how it differs by research field and
application type. Our results may not only indicate the future prospects of ML in finance but
also show where and how researchers can apply ML to maximise its future potential.
4.1 | Sample of finance research papers that apply ML
For a systematic analysis of the existing finance research that applies ML, we begin by
constructingasampleofrelevantpublications.Webuildoursamplebyfocusingonresearch
papersthathave beenpublished inmajor finance journals.Asourstartingpoint,we choose
the 45 most highly ranked finance journals (categories A+, A and B) of the journal ranking
of the German Academic Association of Business Research (VHB‐JOURQUAL3).13 Then,
13Inanalternativeapproach,wechoosethe37journalsthatarerankedas4*,4or3withinthefinancecategoryoftheAJG2018ranking
oftheCharteredAssociationofBusinessSchools.ThoseranksarelargelycomparabletotheA+,AandBranksoftheVHB‐
JOURQUAL3ranking.Ourresultsremainqualitativelyunchangedwhenusingthisalternativesetofjournals.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1685
FINANCIAL MANAGEMENT
wevisiteachjournalwebsiteanddownloadallpapersthathavebeenpublishedintheyears
2010 to 2021 and that contain any of the following keywords either in the title, abstract,
or full text:
– General ML‐related terms: ‘machine learning’, ‘big data’, ‘artificial intelligence’
– ML method categories: ‘supervised learning’, ‘unsupervised learning’, ‘reinforcement
learning’, ‘semisupervised learning’
– Specific ML methods: ‘lasso’, ‘ridge’, ‘elastic net’, ‘decision tree’, ‘random forest’, ‘boosted
regression trees’, ‘gradient boosting’, ‘support vector machine’, ‘support vector classifica-
tion’, ‘support vector regression’, ‘neural network’, ‘naïve bayes’
We read each paper in this initial sample and manually exclude papers that do not use
machine learning in any part of their analysis (for instance, if they mention the keyword(s)
aboveonlywhiledescribingtheworkofothers).Finally,wearriveatasamplethatconsistsof
346 papers.
To investigate possible differences in publication success by research field and
application type, we classify each paper in both dimensions. For the classification by
researchfield,wemakeuseofJELcodes.14InthefewcaseswhereEconLitprovidesnoJEL
codes or if none of the provided codes fall into the financial economics code range (G), we
instead use author‐provided JEL codes obtained directly from the papers. We then classify
each paper in our sample into exactly one of the five JEL subfields within financial
economics(G1–G5coderange).15SincesomepaperscarrymultipleJELcodes,wemanually
classify 68 papers in our sample for which the subfield assignment is ambiguous. In
29cases,wecanresolvetheambiguitybychoosingthesubfieldaccordingtothemajorityof
a paper's JEL codes. In the remaining 39 cases, we manually assign the most appropriate
subfield.
Regarding the classification by application type, we inspect each paper's methodology in
detail and then classify it into one of the three archetypes of our taxonomy described in
Section 3: (i) superior and novel measures, (ii) economic prediction problems, and (iii) new
econometric tools.
4.2 | How promising are ML applications in finance?
To provide indications of the future prospects of ML applications in finance, we first analyse
thejournalsinwhichtheexistingMLapplicationshavebeenpublished.Figure5illustratesthe
largegrowthintheusageofML.In2018,thenumberofpublicationsthatusedMLmorethan
tripledcomparedtothepreviousyears'average.In2019,theincreasewasmorethanfivefold.In
2020, there were almost seven times as many publications using ML than before, and in 2021
we found an almost elevenfold increase in the number of published ML papers.
WhilethestronggrowthinthenumberoffinancepublicationsthatapplyMLoverthelast
few years shows a clear trend toward an increasing usage of ML, the question of whether ML
14ToobtaintheJELcodesofthepapersinoursample,weusetheEconLitdatabasefromtheAEA.TheJELcodesfromEconLitare
assignedbyprofessionalstaff,ensuringsystematicclassificationcriteriaandmaximalcoverage(Falk&Andre,2021).
15JELcodesarestructuredhierarchicallyandconsistofoneletterandtwodigits(e.g.,G35),wheretheletterreferstothegeneralfieldin
economics(e.g.,Gforfinancialeconomics),thefirstdigitdescribesthesubfield(e.g.,G3forcorporatefinance),andtheseconddigit
determinesthespecificareawithinasubfield(e.g.,G35forpayoutpolicy).
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1686
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
FIGURE 5 NumberofrelevantpublicationsinfinancethatapplyMLbyyear.Thisfiguredepictshowthe
numberofpapersthatapplyMLandhavebeenpublishedinmajorfinancejournalshasevolvedovertime.Since
2018,weobserveastrongincreaseinMLpublicationscomparedtotheaverageofthepreviousyears.
applications have the potential to be published in the most prestigious journals of the
professionremainsunanswered.PanelAinTable5showshowthenumberofMLpublications
has evolved over time by journal rank. In the years until 2017, the few early ML applications
werepublishedmostlyinjournalsrankedasB.Since2018,however,asignificantportionofthe
MLpublicationsappearedinthehighest‐rankedjournals.Tocontrolforthefactthatthereexist
manymorelower‐rankedthanhigher‐rankedjournals(andthuspublicationsintherespective
journals), Panel B reports the share of ML publications relative to the total number of
publications that major finance journals of different ranks published each year. The results
show that the strong increase in the number of ML publications was not driven by a general
increase in the number of papers that journals of any rank have published; similar to the
absolutenumbers,therelativeshareofpublicationsthatuseMLhasincreasedsimilarlyintotal
andforeachjournalrank.16In2021,therearenomeaningfuldifferencesintherelativeshareof
ML publications across journal ranks: approximately 3%–4% of the publications used ML in
2021 independent of the journal rank.17
Our results in this section give two main indications of the future prospects of ML in
finance. First, there is steady and robust growth in the number of finance publications that
applyML.ItislikelythatthistrendwillcontinuewithevenmoreMLapplicationsintheyears
ahead. The benefits of ML illustrated above and the continuing increase in relevance of ML
outsideofacademiaalsoleavelittlereasontoexpectotherwise.Second,researcherswhoapply
ML in finance can reasonably expect their papers to have the potential to reach the highest‐
ranking journals of the profession. Not only are there currently numerous examples of ML
applications in such journals, but their relative share has now reached a level that is
comparabletolower‐rankedjournals.Hence,theseresultsmaysuggestabrightandpromising
future for ML applications in finance.
16Weconducttwo‐samplet‐testsforthedifferencesbetweenthe2010–2017shareofMLpapersacrossjournalsofthethreedifferent
journalcategories(A+,A,andB).Inthe2010–2017period,wedetectastatisticallysignificantdifferencebetweentheshareofML
papersinBrankedjournals(0.5%)andthatinA+andArankedjournals(0.2%/0.3%)atthe5%level.Inthe2018‐2021period,this
statisticallysignificantdifferencedisappears.
17Notably,thetotalnumberofpublicationsalsoincludestheorypapersandothermethodologies.TheshareofMLpapersamong
empiricalstudieswouldbeevenhigher.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

slanruojecnanifrojamnisnoitacilbupllaotevitalererahsriehtdnaLMylppatahtsnoitacilbupecnaniftnavelerforebmunylraeY
5
ELBAT
nidehsilbupneebevahdnaLMylppatahtsrepapforebmunetulosbaehtstroperAlenaP.knarlanruojybemitrevosnoitacilbupLMforebmunehtstroperelbatsihT rojamnisnoitacilbupllaforebmunehtotevitalersnoitacilppaLMesehtfoerahsehtstroperBlenaP.knarlanruojybdnalatotniraeyrepslanruojecnanifrojam crob,a.snoitacilbupforebmunehtybdethgieweraBlenaPni1202–8102dna7102–0102sraeyehtnisnaemehT.knarlanruojybdnalatotniraeyrepslanruojecnanif
.ylevitcepser,B/AdnaB/+A,A/+Aspuorgehtroflevel%5ehttasnoitroporpnisecnereffidfoecnacifingislacitsitatsetoned
naeM
naeM
latoT
1202–8102
1202
0202
9102
8102
7102–0102
7102
6102
5102
4102
3102
2102
1102
0102
raeY
slanruojecnanifrojamnisnoitacilbupLMforebmuN:AlenaP
643
5.66
901
96
25
63
01
51
8
12
8
9
6
7
6
latoT
93
5.8
41
8
8
4
6.0
1
0
2
0
2
0
0
0
+A
26
5.11
91
21
7
8
0.2
1
1
6
2
1
0
1
4
A
542
5.64
67
94
73
42
4.7
31
7
31
6
6
6
6
2
B
slanruojecnanifrojamnisnoitacilbupllaotevitalersnoitacilbupLMfoerahS:BlenaP
%1.1
%3.2
%4.3
%3.2
%0.2
%4.1
%4.0
%6.0
%3.0
%9.0
%3.0
%4.0
%3.0
%3.0
%3.0
latoT
%1.1
%4.2
%4.3
%2.2
%4.2
%3.1
b%2.0
%3.0
%0.0
%7.0
%0.0
%7.0
%0.0
%0.0
%0.0
+A
%8.0
%9.1
%2.3
%9.1
%2.1
%2.1
c%3.0
%2.0
%2.0
%8.0
%3.0
%1.0
%0.0
%2.0
%6.0
A
%3.1
%5.2
%5.3
%5.2
%1.2
%5.1
c,b%5.0
%8.0
%4.0
%9.0
%4.0
%5.0
%5.0
%5.0
%2.0
B
|
HOANGANDWIEGRATZ EUROPEAN 1687
FINANCIAL MANAGEMENT
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1688
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
4.3 | Which kinds of ML applications in finance are most promising?
In the previous section, we showed that ML applications have seenstrong time‐series growth in
themostprestigiousfinancejournalsoverthelastseveralyears.Wenowmoveontothequestion
ofwhatmakescertainapplicationsmorepromisingthanotherswithregardtopublicationsuccess.
Toanswerthisquestion,wefirstinvestigatedifferencesinthedistributionofMLpublicationsby
research field and across journal ranks; and then, subsequently apply the classification from our
taxonomy (see Section 3) as a third dimension (methodological purpose) to the analysis.
In Table 6, we begin with examining the distribution of ML publications by research field.
Column 1 shows that most ML publications (to date) belong to the general financial markets
(G1)category(71.1%),whichconsistsofassetpricingandrelatedareas.ConsiderablyfewerML
publications have been published in the fields of financial institutions and services (G2, 13.6%)
and corporate finance and governance (G3, 14.2%). There is a very small share of ML
publications in behavioural finance (G4, 0.9%) and household finance (G5, 0.3%).
Toaccountforheterogeneityinthedistributionofallpublishedfinancepapersbyresearch
field, we compare the distribution of ML publications to that of all publications in major
financejournals.Thiscomparisoniscrucialifthegeneralfinancialmarkets(G1)categoryalso
representsthelargestfieldinmajorfinancejournals.Ifso,thepreviousresultcouldbesimply
drivenbyalargenumberofpublicationsthatbelongtothegeneralfinancialmarketscategory
(G1). Therefore, Column 5 shows the distribution of all (2010–2021) publications across
fields,18 which we then compare with the distribution of ML publications across fields. Visual
inspection of Columns 1 and 5 already suggests that even after accounting for research field
effects, ML papers are significantly more likely in the general financial markets category
compared to other fields. A Pearson χ2‐test, which tests for systematic differences of two
distributions with categorical variables, confirms this observation at every plausible level of
significance (see last row of Table 6). In additional analyses using z‐tests for differences in
proportions, Column 9 shows that the distribution of ML publications is much more
concentrated with a substantially higher share of ML (relative to all) papers in the field of
general financial markets (G1: 71.1% vs. 47.1%, z‐stat: 8.84) and a lower share of papers in the
fields of financial institutions and services (G2: 13.6% vs. 25.4%, z‐stat: −5.03) and corporate
financeandgovernance(G3:14.2%vs.27.3%,z‐stat:−5.44).Inthefieldsofbehaviouralfinance
(G4) and household finance (G5), the sample sizes are too small to draw any economically
meaningfulconclusions.Werepeatouranalysisforeachofthethreejournalrankingcategories
(A+, A and B) in Columns 10–12 and find qualitatively similar results.
Second,weexaminethedistributionofMLpublicationsbythemethodologicalpurpose(see
our taxonomy, Section 3). Table 7 (Panel A, Column 1) shows the distribution for the full
sampleofMLpublicationsacrossallfields.Alargemajorityofpublications(69.1%)applyMLto
reduce the prediction error in economic prediction problems. Using ML to construct superior
andnovelmeasuresismuchlesswidespreadonaverage(25.1%).Veryfewfinancepublications
(5.8%) use ML to extend the econometric toolset.19 Columns 2‐4 reveal that there is strong
heterogeneity by journal rank. Specifically, publications in the highest‐ranked journals (A+)
use ML disproportionally more often to construct superior and novel measures compared to
18Weobtaindataforallfinancepublicationsinthe45majorfinancejournals(rankedasA+,A,orBaccordingtotheVHB‐JOURQUAL3
rating)fortheyears2010to2021fromEconLit.WeclassifyeachpaperintooneofthefiveJELsubfieldswithinfinancialeconomics
(G1–G5coderange)withtheproceduredescribedinSection4.1.
19NotethatthenumberofpapersinoursamplethatapplyMLtoextendtheeconometrictoolsetislowmainlybecauseweonlyconsider
papersfromfinancejournalsandthereforeignorecontributionsfromtheeconometricsliterature.
1468036x,
2023,
5, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|  1468036x, 2023, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408 by Cochrane Philippines, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1689
HOANGANDWIEGRATZ EUROPEAN
FINANCIAL MANAGEMENT
ehtstropernmuloctsrifehT.)seirogetacLEJtigid‐elgnis(dleifhcraeserybslanruojecnanifrojamnisnoitacilppahcraeserLMfonoitubirtsidehtstroperelbatsihT stluseremasehttroper8–5snmuloC.Bdna,A,+Asadeknarslanruojnisnoitacilbuprofyletarapesstluserehttroper4–2snmuloCelihw,elpmaseritneehtrofstluser
***000.0
| lacitsitatsetoned*ro**,***.snoitroporpniecnereffidehtrofstset‐zfoscitsitats‐zehttropersnmulocruoftsalehT.slanruojecnanifrojamnisnoitacilbupllarof |     | ***94.6 ***12.5− | ***21.3− | ***46.9 | ***57.1 |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ---------------- | -------- | ------- | ------- | --- |
)8(–)4(
‐
B
|     |     | ***87.2 | ***99.2− |     |     | **520.0 |
| --- | --- | ------- | -------- | --- | --- | ------- |
)7(–)3(
|     |     | 51.0 |     | 11.0− | 13.0− | ‐   |
| --- | --- | ---- | --- | ----- | ----- | --- |
A
|     | ecnereffidroftats‐z | ***76.3 |     |     |     | ***400.0 |
| --- | ------------------- | ------- | --- | --- | --- | -------- |
**72.2−
|     | )6(–)2( | 65.1 |     |     | 53.0− | ‐   |
| --- | ------- | ---- | --- | --- | ----- | --- |
slanruojecnanifrojamnisnoitacilbupllaotnosirapmocdnadleifhcraeserybecnanifnisnoitacilppaLMfonoitubirtsiD
+A
AN
***000.0
|     |     | ***48.8 ***30.5− | ***44.5− | ***27.9 |     |     |
| --- | --- | ---------------- | -------- | ------- | --- | --- |
)5(–)1(
|     |     |     |     |     | 37.0 | ‐   |
| --- | --- | --- | --- | --- | ---- | --- |
llA
|     | slanruojecnanifrojamnisnoitacilbupllA | %5.55 %1.32 | %3.12 | %0.0 | %1.0 | 572,01 ‐ |
| --- | ------------------------------------- | ----------- | ----- | ---- | ---- | -------- |
)8(
B
|     |     | %1.63 %3.13 | %4.23 | %0.0 | %2.0 | 980,5 ‐ |
| --- | --- | ----------- | ----- | ---- | ---- | ------- |
)7(
A
|     |     | %0.83 %5.32 | %3.83 | %0.0 | %3.0 | 142,3 ‐ |
| --- | --- | ----------- | ----- | ---- | ---- | ------- |
)6( +A
|     |     | %1.74 %4.52 | %3.72 | %0.0 | %1.0 | 506,81 ‐ |
| --- | --- | ----------- | ----- | ---- | ---- | -------- |
)5( llA
ecnanifrojamnisnoitacilbupLM
|     |     | %3.67 %0.9 | %1.31 | %2.1 | %4.0 | 542 ‐ |
| --- | --- | ---------- | ----- | ---- | ---- | ----- |
)4(
B
|     |     | %2.35 %3.23 | %5.41 | %0.0 | %0.0 | 26 ‐ |
| --- | --- | ----------- | ----- | ---- | ---- | ---- |
)3(
A
|     |     | %7.66 %8.21 | %5.02 | %0.0 | %0.0 | 93 ‐ |
| --- | --- | ----------- | ----- | ---- | ---- | ---- |
.level%01ro,%5,%1ehttaecnacifingis
)2( +A
slanruoj
|     |     | %1.17 %6.31 | %2.41 | %9.0 | %3.0 | 643 ‐ |
| --- | --- | ----------- | ----- | ---- | ---- | ----- |
)1( llA
|     |     | snoitutitsnilaicnaniF | dnaecnanifetaroproC |                |     | scitsitatsderauqs‐ihC |
| --- | --- | --------------------- | ------------------- | -------------- | --- | --------------------- |
|     |     |                       | )2G(secivresdna     | )3G(ecnanrevog |     |                       |
laicnaniflareneG
|     |     | )1G(stekram |     |             | )4G(ecnanif )5G(ecnanif |           |
| --- | --- | ----------- | --- | ----------- | ----------------------- | --------- |
|     |     |             |     | laruoivaheB |                         | :)eulavp( |
6 dlohesuoH
ELBAT
sboN

|  1468036x, 2023, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408 by Cochrane Philippines, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1690
EUROPEAN HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
TABLE 7 DistributionofMLapplicationsinfinancebyapplicationtypefortheentiresampleandfor
publicationsinthedifferentjournalranks
ThistablereportsthedistributionofMLresearchapplicationsinmajorfinancejournalsbyapplicationtype
fromourtaxonomy.PanelAreportstheresultsacrossallresearchfields.PanelBreportstheresultsforeach
researchfieldseparately.Thefirstcolumnreportstheresultsfortheentiresample,whileColumns2–4report
theresultsseparatelyforpublicationsinjournalsrankedasA+,A,andB.a,b,orcdenotestatistical
significanceofdifferencesinproportionsatthe5%levelforthegroups‘A+versusA’,‘A+versusB’and‘A
versusB’,respectively.
|     | All | A+  | A   | B   |
| --- | --- | --- | --- | --- |
|     | (1) | (2) | (3) | (4) |
PanelA:Distributionofapplicationtypes
|                            | n=346 | n=39     | n=62     | n=245    |
| -------------------------- | ----- | -------- | -------- | -------- |
| Superiorandnovelmeasures   | 25.1% | 56.4%a,b | 32.3%a,c | 18.4%b,c |
| Economicpredictionproblems | 69.1% | 38.5%a,b | 62.9%a,c | 75.5%b,c |
| Neweconometrictools        | 5.8%  | 5.1%     | 4.8%     | 6.1%     |
PanelB:Distributionofapplicationtypesineachresearchfield
| Generalfinancialmarkets(G1)          | n=246  | n=26      | n=33   | n=187    |
| ------------------------------------ | ------ | --------- | ------ | -------- |
|                                      |        | 38.5%b    | 33.3%c | 17.6%b,c |
| Superiorandnovelmeasures             | 22.0%  |           |        |          |
| Economicpredictionproblems           | 71.1%  | 57.7%     | 63.6%  | 74.3%    |
| Neweconometrictools                  | 6.9%   | 3.8%      | 3.0%   | 8.0%     |
| Financialinstitutionsandservices(G2) | n=47   | n=5       | n=20   | n=22     |
| Superiorandnovelmeasures             | 29.8%  | 80.0%a,b  | 30.0%a | 18.2%b   |
|                                      |        | 0.0%a,b   | 65.0%a | 81.8%b   |
| Economicpredictionproblems           | 66.0%  |           |        |          |
| Neweconometrictools                  | 4.3%   | 20.0%b    | 5.0%   | 0.0%b    |
| Corporatefinanceandgovernance(G3)    | n=49   | n=8       | n=9    | n=32     |
| Superiorandnovelmeasures             | 32.7%  | 100.0%a,b | 33.3%a | 15.6%b   |
|                                      |        | 0.0%a,b   | 55.6%a | 84.4%b   |
| Economicpredictionproblems           | 65.3%  |           |        |          |
| Neweconometrictools                  | 2.0%   | 0.0%      | 11.1%  | 0.0%     |
| Behaviouralfinance(G4)               | n=3    | n=0       | n=0    | n=3      |
| Superiorandnovelmeasures             | 100.0% | NA        | NA     | 100.0%   |
| Economicpredictionproblems           | 0.0%   | NA        | NA     | 0.0%     |
| Neweconometrictools                  | 0.0%   | NA        | NA     | 0.0%     |
| Householdfinance(G5)                 | n=1    | n=0       | n=0    | n=1      |
| Superiorandnovelmeasures             | 0.0%   | NA        | NA     | 0.0%     |
| Economicpredictionproblems           | 100.0% | NA        | NA     | 100.0%   |
| Neweconometrictools                  | 0.0%   | NA        | NA     | 0.0%     |

|
HOANGANDWIEGRATZ EUROPEAN 1691
FINANCIAL MANAGEMENT
publications in lower‐ranked journals (56.4% vs. 32.3% and 18.4%). These differences are
statistically significant at the 5% level using z‐tests for differences in proportions between
journal rank categories. On the other hand, economic prediction problems are less prevalent in
thehighest‐rankedjournals(38.5%vs.62.9%and75.5%),whichisagainstatisticallysignificant.
Todetectdifferencesinthepublicationsuccessofapplicationtypesacrossresearchfields,we
repeat the previous analysis for each research field separately in Panel B of Table7. Specifically,
weareinterestedinidentifyingsystematicpatternsacrossresearchfields,forexample,ifsuperior
and novel measures are more likely to be successful in specific fields of finance. As Panel B,
Column 1 shows, superior and novel measures are disproportionally more often used in the
financial institutions (G2) and corporate finance (G3) literatures (29.8% and 32.7% vs. 25.1%).
Interestingly, within these two fields, publications in journals ranked as A+(Column 2) almost
exclusively use ML to construct superior and novel measures (80.0% and 100.0%).
4.3.1 | Analysis by citations
To further corroborate our findings, we analyse citations as an alternative measure of publication
success.20WeobtainthenumberofcitationsfromWebofScience(asof19Sep2022)foreachML
publicationinoursampleandcompareittotheaveragenumberofcitationsforallpaperspublished
in major finance journals. Given that a paper's number of citations (as of 19 Sep 2022) naturally
dependsonthetimesincepublication,wedemeanthenumberofcitationsinthefollowingway:for
eachMLpublicationinoursample,wecalculateexcesscitations,whichisthedifferencebetweena
paper'sactualnumberofcitationsandtheaveragenumberofcitationsofallpublicationsinmajor
financejournalsfromthesameyear.21Wethenstudydifferencesinexcesscitationsbyresearchfield
and application type and conduct t‐tests against the null hypothesis that excess citations are
statisticallyindistinguishablefromzero(i.e.,therearenodifferencesincitationcountsbetweenML
publications and all publications from a given year). Table 8 shows our results. Overall, ML
publicationsreceive3.0morecitationsthantheaveragepublicationinmajorfinancejournalsfrom
the same year, which is statistically significant at the 10% level. Across application types,
publicationsthatuseMLtoconstructsuperiorandnovelmeasuresreceive10.2morecitationsthan
general publications in major finance journals, which is highly significant at the 1% level. Across
fields, ML publications in corporate finance/governance receive 7.6 more citations than general
publicationsinmajorfinancejournals,whichissignificantatthe5%level.Finally,publicationsthat
apply ML to construct superior and novel measures related to corporate finance/governance show
thehighestpotentialwithregardtocitationcountastheyreceive24.2morecitations,whichisalso
highly significant at the 1% level. Given that the average ML publication in our sample has been
cited 16.2 times, these effects are not only statistically significant but also economically large.22,23
20Wethankananonymousrefereeforencouragingthisanalysis.
21WeobtaincitationdatatocalculateaveragecitationcountsperyearfromWebofScience.
22Inuntabulatedanalyses,weaccountforpossibleunobservedyear‐levelheterogeneityincitationgrowthacrossfields(forinstance,if
citationsafterpublicationgrowstrongerincertainfields)bydemeaningcitationcountsbyyear‐and‐fieldaverages.Ourresultsare
qualitativelyandstatisticallysimilarwhenconductingthisalternativeanalysis.
23AsecondpossiblealternativetoanalysingtotalcitationcountsistoanalysetherankingofjournalsthatciteMLpublications.In
untabulatedanalyses,weshowthatpublicationsthatuseMLtoconstructsuperiorandnovelmeasurestendtobecitedfrom
higher‐rankedjournals.Again,thiseffectisespeciallypronouncedinthefieldofcorporatefinanceandgovernance.Theseadditional
analysesofcitationsthussupportourmainfindings.Thedetailedresultsareavailablefromtheauthorsuponrequest.Wethankan
anonymousrefereeforsuggestingthisanalysis.
1468036x,
2023,
5, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|  1468036x, 2023, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408 by Cochrane Philippines, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1692
|     | EUROPEAN |     |     | HOANGANDWIEGRATZ |     |
| --- | -------- | --- | --- | ---------------- | --- |
FINANCIAL MANAGEMENT
TABLE 8 MeanexcesscitationsofMLpublicationsrelativetoallpublicationsinmajorfinancejournals
ThistablereportsthemeanexcesscitationsofMLpublicationsbyfieldandapplicationtype.Excesscitations
aredefinedasthedifferencebetweenactualcitationsandtheaveragenumberofcitationsforallpublicationsin
majorfinancejournalsfromthesameyear.CitationdatacomefromWebofScienceasof19Sep,2022.***,**or
*denotestatisticalsignificanceatthe1%,5%or10%level.
|            |       |          | Superiorand | Economic   | New         |
| ---------- | ----- | -------- | ----------- | ---------- | ----------- |
|            |       |          | novel       | prediction | econometric |
|            |       | Alltypes | measures    | problems   | tools       |
| FullSample | n=346 | 3.0*     | 10.2***     | 1.2        | −7.0*       |
Byfield
| Generalfinancial | n=246 | 2.3 | 9.3** | 1.1 | −8.0** |
| ---------------- | ----- | --- | ----- | --- | ------ |
markets(G1)
| Financialinstitutions | n=47 | 2.4 | 1.0 | 3.7 | −8.2 |
| --------------------- | ---- | --- | --- | --- | ---- |
andservices(G2)
−0.9
| Corporatefinanceand | n=49 | 7.6** | 24.2*** |     | 13.7 |
| ------------------- | ---- | ----- | ------- | --- | ---- |
governance(G3)
| Behavioural | n=3 | −5.3** | −5.3** | NA  | NA  |
| ----------- | --- | ------ | ------ | --- | --- |
finance(G4)
|           |     | −1.5 |     | −1.5 |     |
| --------- | --- | ---- | --- | ---- | --- |
| Household | n=1 |      | NA  |      | NA  |
finance(G5)
In sum, the results from the citation analysis are consistent with the results from the previous
analysis using journal ranks and thus provide corroborating evidence.
Our findings in this section yield three important conclusions. First, the usage of ML to
construct superior and novel measures seems to be one application type with strong future
potential. While most publications to date apply ML to economic prediction problems, papers
higher‐ranked
that use ML for superior and novel measures have appeared in journals and
receive more citations. Second, papers that apply ML in the field of corporate finance and
governance seem to benefit from ML's ability to produce superior and new measures. Finally,
the scarcity of existing research in the fields of behavioural finance and household finance
indicates another attractive avenue for future ML applications.
5 | CONCLUSION
In this paper, we studied the question of how researchers can leverage ML technology in
finance. First, we established that different types of ML solve different problems than
traditional linear regression with OLS. While the properties of OLS are beneficial for
explanation problems, supervised ML is the superior method for prediction problems. As we
ML‐based
illustrated with a real estate asset pricing prediction problem, price predictions can
| achieve substantially | lower pricing | errors than | OLS. |     |     |
| --------------------- | ------------- | ----------- | ---- | --- | --- |
Inthesecondpartofthispaper,wedevelopedthefollowingtaxonomyofMLapplicationsin
finance: (1) construction of superior and novel measures, (2) reduction of prediction error in
economic prediction problems, and (3) extension of the existing econometric toolset. This

|
HOANGANDWIEGRATZ EUROPEAN 1693
FINANCIAL MANAGEMENT
taxonomy serves multiple purposes. First, it enables a systematic review of the existing ML
literature in finance. Second, it enables a better understanding of new contributions and how
they relate to the existing literature. Finally, it may guide researchers in discovering possible
applications and thus may facilitate new ML studies in finance.
Inthefinalpart,weprovidedindicationsofthefutureprospectsofMLapplicationsinfinanceby
analysingtheMLpaperspublishedinmajorfinancejournals.Overthelastfewyears,therehasbeen
astronggrowthinthenumberofMLapplicationsinfinance,andmanyoftheseapplicationsreached
the highest‐ranked journals of the profession. Our results suggest that ML may become even more
widespreadinfinanceresearchinthecomingyears.Theyalsoindicateaparticularlylargepotential
ofapplyingMLtounconventionaldatatoconstructsuperiorandnovelmeasuresoftopicsrelatedto
thefieldofcorporatefinanceandgovernance.Thefieldsofbehaviouralandhouseholdfinancemay
also offer a mostlyuntapped potential for MLin future research.
ACKNOWLEDGEMENTS
Open Access funding enabled and organized by Projekt DEAL.
DATA AVAILABILITY STATEMENT
The data that support the findings of this study are available from the corresponding author
upon reasonable request.
REFERENCES
Adämmer, P., &Schüssler,R. A.(2020). Forecasting theequitypremium: Mindthenews! Review ofFinance,
24,1313–1355.
Adams, R. B., Akyol, A. C., & Grosjean, P. A. (2021). Corporate gender culture (SSRN Working Paper
No.3880650).
Adams, R. B., Kräussl, R., Navone, M., & Verwijmeren, P. (2021). Gendered prices. The Review of Financial
Studies,34,3789–3839.
Adams, R. B., Ragunathan, V., & Tumarkin, R. (2021). Death by committee? An analysis of corporate board
(sub‐)committees.JournalofFinancialEconomics,141,1119–1146.
Agrawal,R.,Imieliński,T.,&Swami,A.(1993).Miningassociationrulesbetweensetsofitemsinlargedatabases.In
Proceedingsofthe1993ACMSIGMODinternationalconferenceonmanagementofdata(pp.207–216).
Akansu, A.,Cicon,J., Ferris, S.P., & Sun, Y. (2017).Firm performance inthe faceoffear: How CEO moods
affectfirmperformance.JournalofBehavioralFinance,18,373–389.
Akyildirim,E.,Nguyen,D.K.,Sensoy,A.,&Sikic,M.(2021).Forecastinghigh‐frequencyexcessstockreturns
viadataanalyticsandmachinelearning.EuropeanFinancialManagement(Forthcoming).
Alan, N. S., Karagozoglu, A. K., & Zhou, T. (2021). Firm‐level cybersecurity risk and idiosyncratic volatility.
TheJournalofPortfolioManagement,47,110–140.
Albanesi,S.,&Vamossy,D.F.(2019).Predictingconsumerdefault:Adeeplearningapproach(NBERWorking
PaperNo.26165).
Albawi,S.,Mohammed,T.A.,&Al‐Zawi,S.(2017).Understandingofaconvolutionalneuralnetwork.In2017
internationalconferenceonengineeringandtechnology(ICET),(pp.1–6).
Algaba,A.,Ardia,D.,Bluteau,K.,Borms,S.,&Boudt,K.(2020).Econometricsmeetssentiment:Anoverviewof
methodologyandapplications.JournalofEconomicSurveys,34,512–547.
Amel‐Zadeh, A., Calliess, J.‐P., Kaiser, D., & Roberts, S. (2020). Machine learning‐based financial statement
analysis(SSRNWorkingPaperNo.3520684).
Amini,S.,Elmore,R.,Öztekin,Ö.,&Strauss,J.(2021).Canmachineslearncapitalstructuredynamics?Journal
ofCorporateFinance,70,102073.
Ang,Y.Q.,Chia,A.,&Saghafian,S.(2022).Usingmachinelearningtodemystifystartupsfunding,post‐money
valuation,andsuccess.InV.Babich,J.R.Birge,&G.Hilary(Eds.),Innovativetechnologyattheinterfaceof
financeandoperations(pp.271–296).Springer.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are governed
by
the
applicable
Creative
Commons
License

|
1694
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
Angrist,J.D.,&Frandsen,B.(2022).Machinelabor.JournalofLaborEconomics,40,S97–S140.
Antweiler, W., & Frank, M. Z. (2004). Is all that talk just noise? The information content of Internet stock
messageboards.TheJournalofFinance,59,1259–1294.
Athey,S.,Bayati,M.,Imbens,G.,&Qu,Z.(2019).Ensemblemethodsforcausaleffectsinpaneldatasettings.
AEAPapersandProceedings,109,65–70.
Athey, S., & Imbens, G. (2016). Recursive partitioning for heterogeneous causal effects. Proceedings of the
NationalAcademyofSciencesoftheUnitedStatesofAmerica,113,7353–7360.
Athey, S., & Imbens, G. W. (2019). Machine learning methods that economists should know about. Annual
ReviewofEconomics,11,685–725.
Athey,S.,Imbens,G.W.,Metzger,J.,&Munro,E.(2021).UsingWassersteingenerativeadversarialnetworksfor
thedesignofMonteCarlosimulations.JournalofEconometrics(Forthcoming).
Athey, S., & Wager, S. (2019). Estimating treatment effects with causal forests: An application. Observational
Studies,5,37–51.
Azimi,M.,&Agrawal,A.(2021).Ispositivesentimentincorporateannualreportsinformative?Evidencefrom
deeplearning.TheReviewofAssetPricingStudies,11,762–805.
Aziz,S.,Dowling,M.,Hammami,H.,&Piepenbrink,A.(2022).Machinelearninginfinance:Atopicmodeling
approach.EuropeanFinancialManagement,28,744–770.
Aziz, S., & Dowling, M. (2019). Machine learning and AI for risk management. In T. Lynn, J. G. Mooney,
P.Rosati,&M.Cummins(Eds.),Disruptingfinance:FinTechandstrategyinthe21stcentury(pp.33–50).
Palgrave.
Bandiera,O.,Prat,A.,Hansen,S.,&Sadun,R.(2020).CEObehaviorandfirmperformance.JournalofPolitical
Economy,128,1325–1369.
Bao, Y., Ke, B., Li, B., Yu, Y. J., & Zhang, J. (2020). Detecting accounting fraud in publicly traded U.S. firms
usingamachinelearningapproach.JournalofAccountingResearch,58,199–235.
Barbon,A.,DiMaggio,M.,Franzoni,F.,&Landier,A.(2019).Brokersandorderflowleakage:Evidencefrom
firesales.TheJournalofFinance,74,2707–2749.
Barth, A., Mansouri, S., & Woebbeking, F. (2020). ‘Let me get back to you’—A machine learning approach to
measuringnon‐answers(SSRNWorkingPaperNo.3567724).
Bartov,E.,Faurel,L.,&Mohanram,P.S.(2018).Cantwitterhelppredictfirm‐levelearningsandstockreturns?
TheAccountingReview,93,25–57.
Belloni, A., Chen, D., Chernozhukov, V., & Hansen, C. (2012). Sparse models and methods for optimal
instrumentswithanapplicationtoeminentdomain.Econometrica,80,2369–2429.
Beneish,M.D.(1999).Thedetectionofearningsmanipulation.FinancialAnalystsJournal,55,24–36.
Bertomeu,J.,Cheynel,E.,Floyd,E.,&Pan,W.(2021).Usingmachinelearningtodetectmisstatements.Review
ofAccountingStudies,26,468–519.
von Beschwitz,B., Keim, D.B.,& Massa,M. (2020). First to‘read’ thenews: News analyticsandalgorithmic
trading.TheReviewofAssetPricingStudies,10,122–178.
Bianchi, D., Büchner, M., & Tamoni, A. (2021). Bond risk premiums with machine learning. The Review of
FinancialStudies,34,1046–1089.
van Binsbergen, J. H., Han, X., & Lopez‐Lira, A. (2020). Man versus machine learning: The term structure of
earningsexpectationsandconditionalbiases(NBERWorkingPaperNo.27843).
Björkegren, D., & Grissen, D. (2018). The potential of digital credit to bank the poor. AEA Papers and
Proceedings,108,68–71.
Björkegren,D.,&Grissen,D.(2020).Behaviorrevealedinmobilephoneusagepredictscreditrepayment.The
WorldBankEconomicReview,34,618–634.
Boudoukh,J.,Feldman,R.,Kogan,S.,&Richardson,M.(2019).Information,trading,andvolatility:Evidence
fromfirm‐specificnews.TheReviewofFinancialStudies,32,992–1033.
Breaban,A.,&Noussair,C.N.(2018).Emotionalstateandmarketbehavior.ReviewofFinance,22,279–309.
Breiman,L.(2001).Randomforests.MachineLearning,45,5–32.
Brown, N. C., Crowley, R. M., & Elliott, W. B. (2020). What are you saying? Using topic to detect financial
misreporting.JournalofAccountingResearch,58,237–291.
Bubb, R., & Catan, E. M. (2021). The party structure of mutual funds. The Review of Financial Studies, 35,
2839–2878.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1695
FINANCIAL MANAGEMENT
Bubna,A.,Das,S.R.,&Prabhala,N.(2020).Venturecapitalcommunities.JournalofFinancialandQuantitative
Analysis,55,621–651.
Buehlmaier,M.M.M.,&Whited,T.M.(2018).Arefinancialconstraintspriced?Evidencefromtextualanalysis.
TheReviewofFinancialStudies,31,2693–2728.
Burkart,N.,&Huber,M.F.(2021).Asurveyontheexplainabilityofsupervisedmachinelearning.Journalof
ArtificialIntelligenceResearch,70,245–317.
Butaru,F.,Chen,Q.,Clark,B.,Das,S.,Lo,A.W.,&Siddique,A.(2016).Riskandriskmanagementinthecredit
cardindustry.JournalofBanking&Finance,72,218–239.
Calomiris,C.W.,&Mamaysky,H.(2019).Hownewsanditscontextdriveriskandreturnsaroundtheworld.
JournalofFinancialEconomics,133,299–336.
Campbell,D.W.,&Shang,R.(2022).Toneatthebottom:Measuringcorporatemisconductriskfromthetextof
employeereviews.ManagementScience,68,7034–7053.
Carrasco,M.(2012).Aregularizationapproachtothemanyinstrumentsproblem.JournalofEconometrics,170,
383–398.
Cathcart, L., Gotthelf, N. M., Uhl, M., & Shi, Y. (2020). News sentiment and sovereign credit risk. European
FinancialManagement,26,261–287.
Chen,L.,Pelger,M.,&Zhu,J.(2019).Deeplearninginassetpricing(SSRNWorkingPaperNo.3350138).
Chernozhukov,V.,Chetverikov,D.,Demirer,M.,Duflo,E.,Hansen,C.,&Newey,W.(2017).Double/debiased/
Neymanmachinelearningoftreatmenteffects.AmericanEconomicReview,107,261–265.
Chernozhukov,V.,Chetverikov,D.,Demirer,M.,Duflo,E.,Hansen,C.,Newey,W.,&Robins,J.(2018).Double/
debiasedmachinelearningfortreatmentandstructuralparameters.TheEconometricsJournal,21,C1–C68.
Chinco, A., Clark‐Joseph, A. D., & Ye, M. (2019). Sparse signals in the cross‐section of returns. The Journal
ofFinance,74,449–492.
Chinco,A.,Neuhierl,A.,&Weber,M.(2021).Estimatingtheanomalybaserate.JournalofFinancialEconomics,
140,101–126.
Choudhury,P.,Wang,D.,Carlson,N.A.,&Khanna,T.(2019).Machinelearningapproachestofacialandtext
analysis:discoveringCEOoralcommunicationstyles.StrategicManagementJournal,40,1705–1732.
Coffinet, J., & Kien, J.‐N. (2019). Detection of rare events: A machine learning toolkit with an application to
bankingcrises.TheJournalofFinanceandDataScience,5,183–207.
Colombo,E.,Forte,G.,&Rossignoli,R.(2019).Carrytradereturnswithsupportvectormachines.International
ReviewofFinance,19,483–504.
Cowden,C.,Fabozzi,F.J.,&Nazemi,A.(2019).Defaultpredictionofcommercialrealestatepropertiesusing
machinelearningtechniques.TheJournalofPortfolioManagement,45,55–67.
Croux,C.,Jagtiani,J.,Korivi,T.,&Vulanovic,M.(2020).Importantfactorsdeterminingfintechloandefault:
Evidence from a Lendingclub consumer platform. Journal of Economic Behavior & Organization, 173,
270–296.
Dávila,A.,&Guasch,M.(2022).Managers’bodyexpansiveness,investorperceptions,andfirmforecasterrors
andvaluation.JournalofAccountingResearch,60,517–563.
Dixon,M.F.,Halperin,I.,&Bilokon,P.(2020).Machinelearninginfinance:Fromtheorytopractice.Springer
InternationalPublishing.
Dobbie, W., Liberman, A., Paravisini, D., & Pathania, V. (2021). Measuring bias in consumer lending. The
ReviewofEconomicStudies,88,2799–2832.
Domingues,R.,Filippone,M.,Michiardi,P.,&Zouaoui,J.(2018).Acomparativeevaluationofoutlierdetection
algorithms:Experimentsandanalyses.PatternRecognition,74,406–421.
Du,Q.,Jiao,Y.,Ye,P.,&Fan,W.(2019).Whenmutualfundmanagerswriteconfidently(SSRNWorkingPaper
No.3513288).
Easley,D.,LópezdePrado,M.,O'Hara,M.,&Zhang,Z.(2021).Microstructureinthemachineage.TheReview
ofFinancialStudies,34,3316–3363.
Erel,I.,Stern,L.H.,Tan,C.,&Weisbach,M.S.(2021).Selectingdirectorsusingmachinelearning.TheReviewof
FinancialStudies,34,3226–3264.
Erkek, M., Cayirli, K., & Hepsen, A. (2020). Predicting house prices in Turkey by using machine learning
algorithms.JournalofStatisticalandEconometricMethods,9,31–38.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1696
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
Ester,M.,Kriegel,H.‐P.,Sander,J.,&Xu,X.(1996).Adensity‐basedalgorithmfordiscoveringclustersinlarge
spatialdatabaseswithnoise.KDD,96,226–231.
Falk,A.,&Andre,P.(2021).What'sworthknowing?Economists’opinionsabouteconomics(SSRNWorkingPaper
No.3885426).
Feng,G.,Giglio,S.,&Xiu,D.(2020).Tamingthefactorzoo:Atestofnewfactors.TheJournalofFinance,75,
1327–1370.
Frank,M.Z.,&Goyal,V.K.(2009).Capitalstructuredecisions:Whichfactorsarereliablyimportant?Financial
Management,38,1–37.
Freyberger, J., Neuhierl, A., & Weber, M. (2020). Dissecting characteristics nonparametrically. The Review of
FinancialStudies,33,2326–2377.
Fudenberg,D.,Kleinberg,J.,Liang,A.,&Mullainathan,S.(2019).Measuringthecompletenessoftheories(SSRN
WorkingPaperNo.3018785).
Fuster, A., Goldsmith‐Pinkham, P., Ramadorai, T., & Walther, A. (2022). Predictably unequal? The effects of
machinelearningoncreditmarkets.TheJournalofFinance,77,5–47.
Gathergood,J.,Mahoney,N.,Stewart,N.,&Weber,J.(2019).Howdoindividualsrepaytheirdebt?Thebalance‐
matchingheuristic.AmericanEconomicReview,109,844–875.
Giannini,R.,Irvine,P.,&Shu,T.(2018).Nonlocaldisadvantage:Anexaminationofsocialmediasentiment.The
ReviewofAssetPricingStudies,8,293–336.
Goodell, J. W., Kumar, S., Lim, W. M., & Pattnaik, D. (2021). Artificial intelligence and machine learning in
finance: Identifying foundations, themes, and research clusters from bibliometric analysis. Journal of
BehavioralandExperimentalFinance,32,100577.
Goodfellow,I.,Bengio,Y.,&Courville,A.(2016).Deeplearning.MITPress.
Goodfellow, I., Pouget‐Abadie, J., Mirza, M., Xu, B., Warde‐Farley, D., Ozair, S., Courville, A., & Bengio, Y.
(2020).Generativeadversarialnetworks.CommunicationsoftheACM,63,139–144.
Gow,I.D.,Kaplan,S.N.,Larcker,D.F.,&Zakolyukina,A.A.(2016).CEOpersonalityandfirmpolicies(NBER
WorkingPaperNo.22435).
Grammig, J., Hanenberg, C., Schlag, C., & Sönksen, J. (2020). Diverging roads: Theory‐based vs. machine
learning‐impliedstockriskpremia(SSRNWorkingPaperNo.3536835).
Gu, C., & Kurov, A. (2020). Informational role of social media: Evidence from Twitter sentiment. Journal of
Banking&Finance,121,105969.
Gu,S.,Kelly,B.,&Xiu,D.(2020).Empiricalassetpricingviamachinelearning.TheReviewofFinancialStudies,
33,2223–2273.
Gu,S.,Kelly,B.,&Xiu,D.(2021).Autoencoderassetpricingmodels.JournalofEconometrics,222,429–450.
Gulen,H.,Jens,C.,&Page,T.B.(2020).Anapplicationofcausalforestincorporatefinance:Howdoesfinancing
affectinvestment?(SSRNWorkingPaperNo.3583685).
Guliker, E., Folmer, E., & van Sinderen, M. (2022). Spatial determinants of real estate appraisals in The
Netherlands:Amachinelearningapproach.ISPRSInternationalJournalofGeo‐Information,11,125.
Hanley,K.W.,&Hoberg,G.(2019).Dynamicinterpretationofemergingrisksinthefinancialsector.TheReview
ofFinancialStudies,32,4543–4603.
Hansen, C., & Kozbur, D. (2014). Instrumental variables estimation with many weak instruments using
regularizedJIVE.JournalofEconometrics,182,290–308.
Hartford,J.,Lewis,G.,Leyton‐Brown,K.,&Taddy,M.(2017).DeepIV:Aflexibleapproachforcounterfactual
prediction.Proceedingsofthe34thInternationalConferenceonMachineLearning,Australia,70,1414–1423.
Hastie,T.,Tibshirani,R.,&Friedman,J.(2009).Theelementsofstatisticallearning:Datamining,inference,and
prediction(2nded.).SpringerScience&BusinessMedia.
Ho,W.K.O.,Tang,B.‐S.,&Wong,S.W.(2021).Predictingpropertypriceswithmachinelearningalgorithms.
JournalofPropertyResearch,38,48–70.
Hrazdil, K., Novak, J., Rogo, R., Wiedman, C., & Zhang, R. (2020). Measuring executive personality using
machine‐learning algorithms: A new approach and audit fee‐based validation tests. Journal of Business
Finance&Accounting,47,519–544.
Hsieh,T.‐S.,Kim,J.‐B.,Wang,R.R.,&Wang,Z.(2020).Seeingisbelieving?Executives’facialtrustworthiness,
auditortenure,andauditfees.JournalofAccountingandEconomics,69,101260.
Hu,A.,&Ma,S.(2021).Persuadinginvestors:Avideo‐basedstudy(NBERWorkingPaperNo.29048).
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1697
FINANCIAL MANAGEMENT
Huang,A.H.,Zang,A.Y.,&Zheng,R.(2014).Evidenceontheinformationcontentoftextinanalystreports.
TheAccountingReview,89,2151–2180.
Hutchinson,J.M.,Lo,A.W.,&Poggio,T.(1994).Anonparametricapproachtopricingandhedgingderivative
securitiesvialearningnetworks.TheJournalofFinance,49,851–889.
Jacobsen, B., Jiang, F., & Zhang, H. (2019). Equity premium prediction with bagged machine learning (SSRN
WorkingPaperNo.3310289).
Jones,S.,Johnstone,D.,&Wilson,R.(2015).Anempiricalevaluationoftheperformanceofbinaryclassifiersin
thepredictionofcreditratingschanges.JournalofBanking&Finance,56,72–85.
Kamiya,S.,Kim,Y.H.A.,&Park,S.(2019).Thefaceofrisk:CEOfacialmasculinityandfirmrisk.European
FinancialManagement,25,239–270.
Ke,Z.,Kelly,B.T.,&Xiu,D.(2019).Predictingreturnswithtextdata(NBERWorkingPaperNo.26186).
Kelly, B. T., Pruitt, S., & Su, Y. (2019). Characteristics are covariances: A unified model of risk and return.
JournalofFinancialEconomics,134,501–524.
Khandani,A.E.,Kim,A.J.,&Lo,A.W.(2010).Consumercredit‐riskmodelsviamachine‐learningalgorithms.
JournalofBanking&Finance,34,2767–2787.
Kleinberg, J., Ludwig,J., Mullainathan,S., &Sunstein, C.R. (2018). Discrimination inthe ageof algorithms.
JournalofLegalAnalysis,10,113–174.
Kogan,S.,Levin,D.,Routledge,B.R.,Sagi,J.S.,&Smith,N.A.(2009).Predictingriskfromfinancialreports
with regression. In Proceedings of human languagetechnologies: The 2009 annual conference of the north
americanchapteroftheassociationforcomputationallinguistics,USA(pp.272–280).
Kozak, S., Nagel, S., & Santosh, S. (2020). Shrinking the cross‐section. Journal of Financial Economics, 135,
271–292.
Lahmiri, S., & Bekiros, S. (2019). Can machine learning approaches predict corporate bankruptcy? Evidence
fromaqualitativeexperimentaldesign.QuantitativeFinance,19,1569–1577.
Lee, B. K., Lessler, J., & Stuart, E. A. (2010). Improving propensity score weighting using machine learning.
StatisticsinMedicine,29,337–346.
Li, B., & Rossi, A. G. (2020). Selecting mutual funds from the stocks they hold: A machine learning approach
(SSRNWorkingPaperNo.3737667).
Li, K., Liu, X., Mai, F., & Zhang, T. (2021a). The role of corporate culture in bad times: Evidence from the
COVID‐19pandemic.JournalofFinancialandQuantitativeAnalysis,56,2545–2583.
Li,K.,Mai,F.,Shen,R.,&Yan,X.(2021b).Measuringcorporatecultureusingmachinelearning.TheReviewof
FinancialStudies,34,3265–3315.
Liew,J.K.‐S.,&Wang,G.Z.(2016).TwittersentimentandIPOperformance:Across‐sectionalexamination.The
JournalofPortfolioManagement,42,129–135.
Lima, A. Q., & Keegan, B. (2020). Chapter 3—Challenges of using machine learning algorithms for
cybersecurity: A study ofthreat‐classification models applied to social media communicationdata. In V.
Benson,&J.Mcalaney(Eds.),CyberInfluenceandCognitiveThreats(pp.33–52).AcademicPress.
Loh,W.‐Y.(2011).Classificationandregressiontrees.WIREsDataMiningandKnowledgeDiscovery,1,14–23.
Loughran,T.,&McDonald,B.(2011).Whenisaliabilitynotaliability?Textualanalysis,dictionaries,and10‐Ks.
TheJournalofFinance,66,35–65.
Loughran, T., & McDonald, B. (2016). Textual analysis in accounting and finance: A survey. Journal of
AccountingResearch,54,1187–1230.
Ludwig,J., Mullainathan,S., &Spiess,J.(2019). Augmentingpre‐analysisplans withmachine learning. AEA
PapersandProceedings,109,71–76.
MacQueen,J.(1967).Somemethodsforclassificationandanalysisofmultivariateobservations.InProceedings
ofthefifthBerkeleysymposiumonmathematicalstatisticsandprobability,USA(pp.281–297).
Manela,A.,&Moreira,A.(2017).Newsimpliedvolatilityanddisasterconcerns.JournalofFinancialEconomics,
123,137–162.
Martin,I.W.R.,&Nagel,S.(2022).Marketefficiencyintheageofbigdata.JournalofFinancialEconomics,145,
154–177.
Mazrekaj,D.,Titl,V.,&Schiltz,F.(2021).Identifyingpoliticallyconnectedfirms:Amachinelearningapproach
(SSRNWorkingPaperNo.3860029).
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
1698
EUROPEAN
HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
McInish, T. H., Nikolsko‐Rzhevska, O., Nikolsko‐Rzhevskyy, A., & Panovska, I. (2019). Fast and slow
cancellationsandtraderbehavior.FinancialManagement,49,973–996.
Medsker,L.R.,&Jain,L.C.(2001).Recurrentneuralnetworks.DesignandApplications,5,64–67.
Milunovich,G.(2020).ForecastingAustralia'srealhousepriceindex:Acomparisonoftimeseriesandmachine
learningmethods.JournalofForecasting,39,1098–1118.
Moritz,B.,&Zimmermann,T.(2016).Tree‐basedconditionalportfoliosorts:Therelationbetweenpastandfuture
stockreturns(SSRNWorkingPaperNo.2740751).
Mullainathan,S.,&Spiess,J.(2017).Machinelearning:Anappliedeconometricapproach.JournalofEconomic
Perspectives,31,87–106.
Murdoch,W.J.,Singh,C.,Kumbier,K.,Abbasi‐Asl,R.,&Yu,B.(2019).Definitions,methods,andapplications
ininterpretablemachinelearning.ProceedingsoftheNationalAcademyofSciencesoftheUniedStatesof
America,116,22071–22080.
Nagel,S.(2021).Machinelearninginassetpricing.PrincetonUniversityPress.
Nauhaus,S.,Luger,J.,&Raisch,S.(2021).Strategicdecisionmakinginthedigitalage.JournalofManagement
Studies,58,1933–1961.
Nazemi, A., & Fabozzi, F. J. (2018). Macroeconomic variable selection for creditor recovery rates. Journal of
Banking&Finance,89,14–25.
O'Malley, T. (2021). The impact of repossession risk on mortgage default. The Journal of Finance, 76,
623–650.
Obaid, K., & Pukthuanthong, K. (2022). A picture is worth a thousand words: Measuring investor
sentiment by combining machine learning and photos from news. Journal of Financial Economics,
144, 273–297.
Oh,K.J.,Kim,T.Y.,&Kim,C.(2006).Anearlywarningsystemfordetectionoffinancialcrisisusingfinancial
marketvolatility.ExpertSystems,23,83–98.
Osterrieder, J., Kucharczyk, D., Rudolf, S., & Wittwer, D. (2020). Neural networks and arbitrage in the VIX.
DigitalFinance,2,97–115.
Ozbayoglu, A. M., Gudelek, M. U., & Sezer, O. B. (2020). Deep learning for financial applications: A survey.
AppliedSoftComputing,93,106384.
Park,B.,&Bae,J.K.(2015).Usingmachinelearningalgorithmsforhousingpriceprediction:ThecaseofFairfax
County,Virginiahousingdata.ExpertSystemswithApplications,42,2928–2934.
Peng,L.,Teoh,S.H.,Wang,Y.,&Yan,J.(2022).Facevalue:Traitimpressions,performancecharacteristics,and
marketoutcomesforfinancialanalysts.JournalofAccountingResearch,60,653–705.
Pérez‐Rave,J.I.,Correa‐Morales,J.C.,&González‐Echavarría,F.(2019).Amachinelearningapproachtobig
data regression analysis of real estate prices for inferential and predictive purposes. Journal of Property
Research,36,59–96.
Peysakhovich,A.,&Naecker,J.(2017).Usingmethodsfrommachinelearningtoevaluatebehavioralmodelsof
choiceunderriskandambiguity.JournalofEconomicBehavior&Organization,133,373–384.
Philippon,T.(2019).Onfintechandfinancialinclusion(NBERWorkingPaperNo.26330).
DePrado,M.L.(2018).Advancesinfinancialmachinelearning.JohnWiley&Sons.
Rambachan,A.,Kleinberg,J.,Ludwig,J.,&Mullainathan,S.(2020).Aneconomicperspectiveonalgorithmic
fairness.AEAPapersandProceedings,110,91–95.
Rambachan, A., Kleinberg, J., Mullainathan, S., & Ludwig, J. (2020). An economic approach to regulating
algorithms(NBERWorkingPaperNo.27111).
Rasekhschaffe,K.C.,&Jones,R.C.(2019).Machinelearningforstockselection.FinancialAnalystsJournal,75,
70–88.
Rasmussen,C.(1999).TheinfiniteGaussianmixturemodel.AdvancesinNeuralInformationProcessingSystems,
12,554–560.
Renault,T.(2017).IntradayonlineinvestorsentimentandreturnpatternsintheU.S.stockmarket.Journalof
Banking&Finance,84,25–40.
Rico‐Juan,J.R.,&TaltavulldeLaPaz,P.(2021).Machinelearningwithexplainabilityorspatialhedonicstools?
AnanalysisoftheaskingpricesinthehousingmarketinAlicante,Spain.ExpertSystemswithApplications,
171,114590.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|
HOANGANDWIEGRATZ EUROPEAN 1699
FINANCIAL MANAGEMENT
Rish,I.(2001).AnempiricalstudyoftheNaiveBayesclassifier.InIJCAI2001workshoponempiricalmethodsin
artificialintelligence(Vol.3,pp.41–46).
Rossi,A.G.(2018).Predictingstockmarketreturnswithmachinelearning(WorkingPaper).RetrievedDecember
7, 2022, from https://mendoza.nd.edu/wp-content/uploads/2019/07/2018-Alberto-Rossi-Fall-Seminar-
Paper-1-Stock-Market-Returns.pdf
Rossi,A.G.,&Timmermann,A.(2015).ModelingcovarianceriskinMerton'sICAPM.TheReviewofFinancial
Studies,28,1428–1461.
Rossi, A. G., & Utkus, S. P. (2020). Who benefits from robo‐advising? Evidence from machine learning (SSRN
WorkingPaperNo.3552671).
Routledge,B.R.(2019).Machinelearningandassetallocation.FinancialManagement,48,1069–1094.
Sadhwani, A., Giesecke, K., & Sirignano, J. (2021). Deep learning for mortgage risk. Journal of Financial
Econometrics,19,313–368.
Samuelson,P.A.,&Nordhaus,W.D.(2009).Economics(19thed.).McGrawHill/Irwin.
Sermpinis,G.,Tsoukas,S.,&Zhang,Y.(2022).Modellingfailurerateswithmachine‐learningmodels:Evidence
fromapanelofUKfirms.EuropeanFinancialManagement(Forthcoming).
Settles, B. (2009). Active learning literature survey (Computer Science Technical Report No. 1648).
Retrieved December 7, 2022, from https://minds.wisconsin.edu/bitstream/handle/1793/60660/TR1648.
pdf?sequence=1
Sigrist,F.,&Hirnschall,C.(2019).Grabit:Gradienttree‐boostedTobitmodelsfordefaultprediction.Journalof
Banking&Finance,102,177–192.
DeSpiegeleer,J.,Madan,D.B.,Reyners,S.,&Schoutens,W.(2018).Machinelearningforquantitativefinance:
fastderivativepricing,hedgingandfitting.QuantitativeFinance,18,1635–1643.
Sprenger, T. O., Tumasjan, A., Sandner, P. G., & Welpe, I. M. (2014). Tweets and trades: The information
contentofstockmicroblogs.EuropeanFinancialManagement,20,926–957.
Stock,J.H.,&Watson,M.W.(2020).Introductiontoeconometrics(4thed.).Pearson.
Sutton,R.S.,&Barto,A.G.(2018).Reinforcementlearning:Anintroduction.MITPress.
Tang,V.W.(2018).Wisdomofcrowds:Cross‐sectionalvariationintheinformativenessofthird‐party‐generated
productinformationontwitter.JournalofAccountingResearch,56,989–1034.
Tantri,P.(2021).FinTechforthepoor:Financialintermediationwithoutdiscrimination.ReviewofFinance,25,
561–593.
Tchuente,D.,&Nyawa,S.(2022).RealestatepriceestimationinFrenchcitiesusinggeocodingandmachine
learning.AnnalsofOperationsResearch,308,571–608.
Tian,S.,Yu,Y.,&Guo,H.(2015).Variableselectionandcorporatebankruptcyforecasts.JournalofBanking&
Finance,52,89–100.
Vamossy,D.F.(2021).Investoremotionsandearningsannouncements.JournalofBehavioralandExperimental
Finance,30,100474.
Varian,H.R.(2014).Bigdata:Newtricksforeconometrics.JournalofEconomicPerspectives,28,3–28.
Welch,I.,&Goyal,A.(2008).Acomprehensivelookattheempiricalperformanceofequitypremiumprediction.
ReviewofFinancialStudies,21,1455–1508.
Xiang,G.,Zheng,Z.,Wen,M.,Hong,J.,Rose,C.,&Liu,C.(2012).Asupervisedapproachtopredictcompany
acquisition with factual and topic features using profiles and news articles on TechCrunch. In
Proceedings of the sixth international AAAI conference on weblogs and social media, Ireland (vol. pp.
607–610).
Yao,J.,Li,Y.,&Tan,C.L.(2000).Optionpriceforecastingusingneuralnetworks.Omega,28,455–466.
Yu,Y.,Lu,J.,Shen,D.,&Chen,B.(2021).Researchonrealestatepricingmethodsbasedondataminingand
machinelearning.NeuralComputingandApplications,33,3925–3937.
Zhang, T., Ramakrishnan, R., & Livny, M. (1996). BIRCH: An efficient data clustering method for very large
databases.ACMSIGMODRecord,25,103–114.
Zhu, X. (2005). Semi‐supervised learning literature survey (Computer Science Technical Report No. 1530).
RetrievedDecember7,2022,fromhttps://minds.wisconsin.edu/bitstream/handle/1793/60444/TR1530.pdf?
sequence=1
Zou, H., & Hastie, T. (2005). Regularization and variable selection via the elastic net. Journal of the Royal
StatisticalSociety:SeriesB(StatisticalMethodology),67,301–320.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

|  1468036x, 2023, 5, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408 by Cochrane Philippines, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
1700
EUROPEAN HOANGANDWIEGRATZ
FINANCIAL MANAGEMENT
| SUPPORTING | INFORMATION |     |     |
| ---------- | ----------- | --- | --- |
Additional supporting information can be found online in the Supporting Information section
| at the end of this | article. |     |     |
| ------------------ | -------- | --- | --- |
How to cite this article: Hoang, D.,& Wiegratz, K.(2023). Machine learning methods
in finance: Recent applications and prospects. European Financial Management, 29,
| 1657–1701. https://doi.org/10.1111/eufm.12408 |     |     |     |
| --------------------------------------------- | --- | --- | --- |
APPENDIX
SelectionofpublicannouncementsoflargefinancialinstitutionsusingMLintheirday‐to‐day
TABLE A1
businessoperations
ThistablereportsaselectionofnewswiresandpressreleasesfromNexisUnithatcontainpublic
announcementsoflargefinancialinstitutionsusingMLintheirday‐to‐daybusinessoperations.
Release
| Company | date | Source | Extract |
| ------- | ---- | ------ | ------- |
Axa 21Jul2021 MarketLine ‘AXAUKhaslaunchedanewmachinelearning
|     |     | NewsWire | tooltoaccelerateaswellasimprovethe |
| --- | --- | -------- | ---------------------------------- |
accuracyofcomplexpropertyclaims’
‘BankofAmericatodayannouncedthelaunch
| BankofAmerica | 13Jan2022 | PRNewswire |     |
| ------------- | --------- | ---------- | --- |
ofCashProForecasting,atoolthatuses
artificialintelligence(AI)andmachine
learning(ML)technologytomoreaccurately
predictfuturecashpositionsacrossclients'
accounts’
‘BlackRockinvestmentteams[…]utilise
| Blackrock | 11Apr2016 | ENPNewswire |     |
| --------- | --------- | ----------- | --- |
technology‐basedtoolsandresearch
methodologiessuchasmachinelearning,
naturallanguageprocessing,scientificdata
visualisationanddistributedcomputingto
producesustainablealpha.’
‘Thesolutionleveragesartificialintelligenceand
| DeutscheBank | 23Sep2022 | MarketLine |                                          |
| ------------ | --------- | ---------- | ---------------------------------------- |
|              |           | NewsWire   | specifiedrulestocalculatetheriskvaluefor |
eachtransaction.[…]Ourworldwide
networkandtheuseofmachinelearning
techniquesallowustodeployaglobaldata
settoreducefraud.’
| HSBC | 6Nov2019 | Malaysia     | ‘HSBChasbeenabletodealpromptlywithany |
| ---- | -------- | ------------ | ------------------------------------- |
|      |          | EconomicNews | anomalousorsuspicioustransaction      |
throughtheadoptionofnewtechnologies
namelyArtificialIntelligence(AI)and
machinelearning.’

|
HOANGANDWIEGRATZ EUROPEAN 1701
FINANCIAL MANAGEMENT
TABLE A1 (Continued)
Release
Company date Source Extract
J.P.MorganAsset 17Dec2021 PRNewswire ‘J.P.MorganAssetManagementhasrecently
Management launcheditsfirstmutualfundemployinga
datascience‐driveninvestmentprocess[…].
Theinvestmentprocessisdrivenbymachine
learning[…]’
StateStreet 18Jul2018 BusinessWire ‘StateStreetCorporation(NYSE:STT)today
announcedthelaunchofStateStreet
VerusSM,amobile‐firstapplicationthat
makesconnectionsbetweennewscoverage
andinvestors'holdingsthroughthe
applicationofbigdata,machinelearning,
naturallanguageprocessingandhuman
intelligence.Verusisdesignedtohelp
investmentprofessionalsinthefrontoffice
gaingreaterinsights,mitigaterisk,and
generatealpha’.
StateStreet 22Jun2021 BusinessWire ‘StateStreetCorporationtodayannouncedit
willimplementacloud‐based,machine
learningtechnologytotransformprivate
marketsprocessinganddocument
management’.
1468036x,
2023,
5,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1111/eufm.12408
by
Cochrane
Philippines,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License