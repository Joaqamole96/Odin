SystematicReview
Performance, Fairness, and Explainability in AI-Based Credit
Scoring: A Systematic Literature Review
RashedBahlool* ,NabilHewahi andWaelElmedany
CollegeofInformationTechnology,UniversityofBahrain,SakhirCampus,Zallaq1054,Bahrain;
nhewahi@uob.edu.bh(N.H.);welmedany@uob.edu.bh(W.E.)
* Correspondence:20083051@stu.uob.edu.bh
Abstract
Theintegrationofartificialintelligence(AI)inthefinancialsectorhasseenarapidincrease
overthepastfewyears,offeringnewpossibilitiestostreamlineprocesseswhileensuring
profitabilityforlendinginstitutions. Withitsdata-drivencapability,predictingthecred-
itworthinessofapplicantshasdemonstratedstrongpredictiveperformance,particularly
for thin-file clients. Despite these advances, growing concerns regarding AI’s fairness,
explainability,andregulatoryaccountabilityhaveincreasinglylimiteditsadoptioninhigh-
stakescreditdecision-making. Thispaperpresentsasynthesisderivedfromasystematic
literature review (SLR) of 43 peer-reviewed studies published between 2020 and 2025,
focusingonAI-basedcreditscoringandaddressingatleastoneoftheperformance,fair-
ness,orexplainabilitydimensions. Eligiblestudieswerelimitedtopeer-reviewedjournal
andconferencearticles(2020–2025)retrievedfromIEEEXplore,Scopus,WebofScience,
andScienceDirect(lastsearched: 30September), examiningAI-drivencreditscoringin
consumerorlendingdecisioncontexts. GuidedbytheRelevance,Rigor,Reproducibility,
andQuality(3Rs&Q)appraisalframework,thereviewanalyzeshowexistingapproaches
navigatetheinterplayamongperformance,fairness,andexplainabilityunderregulatory
and human oversight considerations. The findings indicate that these dimensions are
predominantly addressed in isolation, with limited attention to their joint treatment in
regulateddeploymentsettings. Byconsolidatingempiricalandconceptualevidence,this
reviewprovidesactionableguidancefordesigninganddeployingcreditscoringmodels
inpractice.
Keywords: creditscoring;explainableAI;algorithmicfairness;AIgovernance;regulatory
compliance
1. Introduction
AcademicEditor:ThanasisStengos Inthecontinuedpursuitofnationwideeconomicgrowth,financialinstitutionsprovide
consumerfacilitiesasoneoftheircorebusinessfunctions. Creditscoringplaysapivotal
Received:12January2026
Revised:26January2026 roleindecidingwhetheraloanshouldbegrantedtoanapplicant, wherebyapplicants
Accepted:29January2026 undergo a rigorous risk assessment process to evaluate their financial stability prior to
Published:3February2026 approvingthefacility(Adegokeetal.,2024). Theproblemofassessingthecreditworthiness
Copyright:©2026bytheauthors. ofloanapplicantsisoneriskexposureforlendinginstitutions,amongotherrisksources
LicenseeMDPI,Basel,Switzerland.
that organizations must address. If not properly evaluated, the likelihood of financial
Thisarticleisanopenaccessarticle
loss increases due to higher loan default rates, ultimately putting financial institutions
distributedunderthetermsand
atrisk(Xieetal.,2025). Incontrast,successfullydistinguishingbetweendefaultersand
conditionsoftheCreativeCommons
Attribution(CCBY)license.
J.RiskFinancialManag.2026,19,104 https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 2of36
non-defaulterswouldensureprofitabilityfortheinstitution. Commoncreditriskassess-
mentsincludeapplicationandbehavioralcreditscoring,withotherassessments,suchas
collection,fraud,andcreditrenewal,alsocoexisting(Muñoz-Cancinoetal.,2023). These
riskassessmentshavebeenextensivelyrelieduponbyfinancialinstitutionstominimize
potentiallossesacrosstheirproductlines. Theyenableinstitutionstoquantify,monitor,
andmitigateassociatedrisks,dependingonthetypeofsituationalinputsandregulatory
mandates(BaselCommitteeonBankingSupervision,2013;EuropeanCentralBank,2024).
Application and behavioral scoring differ substantially in the timing of the credit-
worthiness assessment. On one hand, application scoring aims to assess the eligibility
of applicants prior to receiving the loan (Berg et al., 2020). To perform the assessment,
customersmustundergoarigorousprocessknownasKnowYourCustomer(KYC),which
mandatesthatlendinginstitutionscapturepersonalandrepaymentrecords,oftenretrieved
from national credit bureaus (Mestiri & Hiboun, 2024). The data include demographic
information,loanrepaymentbehavior,andcreditbureaudatashowingoutstandingdebts
andothercreditinquiries,alldeemednecessarytoensureadata-drivenassessmentofcred-
itworthiness. Ontheotherhand,behavioralscoringisanongoingandperiodicevaluation
procedureusedtoassessthecreditbehaviorofexistingcustomers, therebymonitoring
riskintheactiveportfolioofaninstitution(Y.Lietal.,2020). Itreliesonasubsetofthe
informationusedinapplicationscoring,suchaspaymenthistoryandarrearspatterns,and
offersearlysignsofdefaultforproactiveinterventions. Withthesetwoscoringmethodsin
mind,financialinstitutionscantakepreventivemeasureswithapplicantswhoarelikelyto
defaultontheirloans. Together,bothmethodsenableafullcreditlife-cyclemanagement
strategythatensurestheapprovalofeligiblecustomersandtheongoingmonitoringof
repaymentbehavior(Roaetal.,2021).
Beyondinstitutionalrisk,theimplicationofdecisionsmadebycreditscoringextends
tocoversocioeconomicfactors,includingfinancialinclusionandexclusion,wealthdistri-
bution,equity,andsocietalwell-being(Bartlettetal.,2022). Theseconsequencesweigh
heavilyonfinancialinstitutionsand,ifnotaddressed,resultinexclusionarypracticesthat
adverselyaffectunderservedpopulations. Individualsorentitieswithaccesstocreditcan
contributetosocialmobility,whileunfaircreditscoringcanleadtoinequalitiesandlimited
opportunitiesforminoritygroups. Theconsequencesoflendingdecisionshavelongbeen
theinterestofresearchers,mainlyduetotheiradverseimpactuponfundamentalhuman
rights(Jiangetal.,2024). Regardlessofwhethertheoutcomesareintentionalordrivenby
algorithmicdetermination,ofteninfluencedbyhumanbiasintheformofbiasedhistorical
data,itisestimatedthat1.3millionmortgageloansarerejectedintheUnitedStates,mainly
duetodiscrimination(Bartlettetal.,2022). Consequently,minoritygroups,classifiedbased
on gender, ethnicity, religion, or nationality, are more vulnerable to rejection, or in the
best-case scenario, pay higher interest rates. In the long term, this could lead to unfair
wealthaccumulationandthereforeperpetuategenerationalpoverty.
Thesocioeconomicfactorsinvolvedincreditscoringwerekeymotivationsforregula-
torstostepin,ensuringethicalpracticesandproperoversightofthelendingprocess. Asa
result,countriessuchastheUSandtheEuropeanUnionhavepassedtheEqualCreditOp-
portunityAct(ECOA)andtheEUCharterofFundamentalRights,respectively,toprohibit
discriminatorylendingactsagainstpersonalcharacteristics(Griffith,2023). Theseprotec-
tionsincluderace,gender,nationalorigin,andmaritalstatus,and,moreimportantly,they
emphasizethatlendinginstitutionsmustrelysolelyonfinancialandapplicationattributes.
These laws have emerged with the intent to foster transparency in the lending process
andreducemistrustinthefinancialsystemthat,whenundermined,potentiallyleadsto
socialandpoliticalbacklashes. Fromariskmanagementperspective,failuresinfairnessor
explainabilitytranslatedirectlyintoregulatory,legal,andreputationalrisksforlending
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 3of36
institutions. Consideringthelong-standingethicalconcernsincreditscoringandtheircom-
plexrelationtosocietalandeconomicvectors,creditscoringefficiencydoesnotmerelyseek
toimprovelendingdecisionperformance,butalsoaccountsforthebroaderconsequences
ofsociallyandethicallyinadequatedecision-making(Chenetal.,2024;Kumaretal.,2022;
Talaatetal.,2024). Havingsaidthat,despitemanyeffortstocombatbiaseddecisionsin
algorithmicscoring,thereisnoconsensusonauniversalfairnessmodelthatiscompatible
acrossalljurisdictionalsettings,consideringalsothatthedefinitionoffairnessvariesacross
differentnotionsoffairness(Alvesetal.,2023;Caton&Haas,2024;Goethalsetal.,2024).
Giventhatfairnessiscrucialincreditscoringpractices,explainabilityiscentraland
enableskeystakeholderstointerpretandcomprehendmodeloutputs,providingthemwith
arationalebehindparticularoutcomes(Wangetal.,2020). Itallowscomplianceofficers
toquestionandcorrectpotentiallydiscriminatorydecisionpatterns,invitingintervention
whenbiaseddecisionsarise,therebysupportingresponsibleandethicaladoptionofAI
(Valdrighietal.,2025). Explainabilityalsohelpsensurealignmentwithlocalregulations,
AIethicsanddataprivacyguidelinesbyallowinglenderstorespondtoauditsandjustify
rejectedapplicationsmoretransparently(Hlongwaneetal.,2024). However,asAImod-
elsbecomemoresophisticatedandcapableofachievingrecord-breakingprecisionand
accuracy,theirperformanceoftencomesatthecostofexplainability(Dessainetal.,2023),
resemblinganotabletensionbetweenmodelperformanceandtransparency.
Despitealltheadvancementsmadeacrossthethreedimensions—performance,fair-
ness,andexplainability—thecurrentresearchontheapplicationofAItosolvethecredit
scoringproblemremainsfragmented. Acrossthereviewedliterature,thesedimensionsare
mostoftenaddressedinisolationratherthantreatedasjointlyoptimizedobjectives. The
existingliteratureoftenemphasizesonepillarattheexpenseofothers,resultinginmodels
that are highly predictive but lack transparency, underperforming but inherently inter-
pretable,orfairbutoperationallyinconsistentwithregulatorymandates. Moreimportantly,
theinteractionsamongthesethreepillars,togetherwithregulatorycompliance,remain
underexplored,leavinguncertaintyaroundhowfairnesscanbepracticallyimplemented
withoutcompromisingperformanceorinterpretability. InrelationtoexistingSLRs,this
reviewextendspriorworkbyexplicitlyexaminingtheintersectionsbetweenperformance,
fairness,andexplainabilityinAI-basedcreditscoring,ratherthansynthesizingthesedi-
mensionsinisolation. Thisintersection-orientedsynthesisyieldsnewinsightsintohow
thesepillarsinteractinpractice,wheretrade-offsareempiricallyquantified,andwhich
methodologicalandregulatoryconstraintsremainunder-addressedindeployablecredit
decisionpipelines.
In light of that, this study has three core objectives: (i) to systematically survey
AI-basedcreditscoringresearchpublishedbetween2020and2025; (ii)toexaminehow
existing approaches address predictive performance, interpretability, and fairness; and
(iii)toidentifymethodologicalandregulatorygapsthatinfluencethepracticaldeployment
ofresponsiblecreditscoringmodels. Byconsolidatingevidenceacrossthesedimensions,
thisreviewcontributesagovernance-orientedsynthesisofAI-basedcreditscoringresearch
that clarifies existing trade-offs and highlights gaps relevant to regulated deployment.
The remainder of this work is structured as follows. Section 2 outlines the systematic
literaturereview(SLR)methodology,detailingthesearchstrategy,selectioncriteria,and
datasynthesisprocessusedtoensurearigorousandscientificallyadequateinvestigation
ofthecurrentstateofknowledge. Section3presentstheresultsoftheSLRsearchthatalign
withtheresearchobjectivesandoutlinestheselectionandassessmentcriteria. Section4
provides a synthesis of the findings to answer the research questions comprehensively
acrossalldimensionsdiscussedearlier. Finally,Section5concludesbyidentifyingcurrent
researchgapsandoutliningdirectionsforfuturework.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 4of36
2. Methodology
To ensure a comprehensive and unbiased survey of key elements reported in the
literature, the SLR protocol was strictly followed to generate the synthesis while main-
tainingtransparencyandreproducibilityoftheresults. ThePreferredReportingItemsfor
SystematicReviewsandMeta-Analyses(PRISMA)framework(Moheretal.,2010)was
adoptedtorecordtheresearchelements,includingtheidentification,screening,inclusion,
andexclusionofresearchpapers. Thissystematicliteraturereviewwasconductedand
reportedinaccordancewiththePRISMA2020guidelines(Pageetal.,2021). Thereview
protocolwasnotregisteredinPROSPEROoranyotherpublicregistry.
Tocomplywiththereviewprotocol,theprocessconsistedofseveralphases,begin-
ningwiththeformulationofresearchquestionsandconcludingwiththeidentification
ofmethodologicalpatterns. Withinthissystematicprocess, anexplicitsearchplanwas
constructedtolocatepotentiallyrelevantstudiesmadeavailableinpublicdatabases. This
step ensures that the evidence base is comprehensive and not selectively gathered. To
guideandrefinethesearchpriortothein-depthreading,explicitinclusionandexclusion
criteriaweredefinedtodeterminewhichstudiestoincludeandwhichtodiscard. Subse-
quently,forstudiesthatpassedtheselectioncriteria,structuredextractionwasperformed
tocollectkeyvariablessuchasmethodsusedforexplainability,fairnessconsiderations,
orregulatoryaspects. Thesedatawerelaterorganizedinapredefinedschema,allowing
consistentcomparisonandtaggingacrossdifferentpapers. Theextractedinformationwas
later synthesized to identify methodological patterns across the literature, from which
futuredirectionsareanticipated. Figure1illustratesthephasesinvolvedinformulating
thestudy’skeyfindings. Thereviewprocessfollowedsixsequentialphases,beginning
withdefiningresearchquestionsanddevelopingsearchstrategies,followedbyestablishing
inclusionandexclusioncriteria. Datawerethensystematicallyextracted,organized,and
synthesizedtoidentifymethodologicalpatterns.
Figure1.Phasesofthesystematicliteraturereviewprocess.
2.1. ResearchQuestions(RQs)Formulation
Tostrengthenthegoalofthisstudywhileensuringacohesiveandstructuredapproach
guidingtheformulationofthesearchstrategyacrossthethreemainpillars—performance,
explainability,andfairness—aPopulation,Intervention,Comparison,Outcome,andCon-
text(PICOC)framework(Keele,2007)wasadoptedtotranslatethebroadertopicofem-
ployingAIincreditscoringintoanoperationallyprecisescopeattheplanningstageprior
to screening. By articulating the Population, Intervention, Comparison, Outcome, and
Context, the framework guides the search string construction, reduces bias by making
relevance criteria traceable to a predefined scope, and increases reproducibility by for-
mulating auditable selection choices. Using the PICOC framework, this work aims to
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 5of36
exploretherelationshipsandinteractionsamongthethreepillars,quantifytheirtrade-offs,
andacknowledgethatmorethanonepillarcanoperatejointlyandinfluenceanotherina
quantifiablemanner.
Table 1 explains the PICOC components and their relationship to the domain and
subject of this research, guiding RQ formulation and the search strategy developed to
alignthefindingswiththeoverallobjectives. ThePICOCframeworkdefinesthedomain
and subject of deployed AI models highlighted in past studies by referring to credit
scoringpredictionsbasedonevaluatingdefaultrisksusinghistoricalfinancialinformation
exclusivetoapplicationriskassessments.Thisreflectsthetechniquesormethodsemployed
toaddresssingleorjointchallengesincreditscoring,includingperformance,fairness,and
explainability,correspondingtothedeploymentofAItosolvethecreditscoringprediction
problemandincorporatingmultiplepillars. Itspecifieswhattheinterventionisevaluated
againstbyrequiringstudiestomakeuseofexistingbaselinestobenchmarktheirmethods
orhighlightthetrade-offsacrossthepillars,analyzingpillarinteractions. Italsocaptures
themeasuredandreportedperformanceindicators,fairnessmetrics,explainabilitywith
humancomprehension,andquantitativeassessmentoftrade-offanalysisbetweenpillars.
Finally,itdefinestheapplicationenvironmentandpublicationconstraintsbydetermining
whetherthestudyisexclusivetothecreditscoringdomain,publishedinapeer-reviewed
venue, ordemonstratesrecencyinreportingfairnessandexplainabilityintegratedinto
modeling,anditidentifieswheretrade-offsorresearchgapsemergeamongthethreepillars.
Table1.PICOCframeworkusedforresearchquestionformulation.
Component Definition
DefinesthedomainandsubjectofdeployedAImodelshighlightedinpast
studies. Itreferstocreditscoringpredictionsthatarebasedonevaluating
Population
defaultrisksusinghistoricalfinancialinformationthatisexclusiveto
applicationriskassessments.
Referstothetechniqueormethodemployedtotacklesingleorjoint
problemsgivenincreditscoring,includingperformance,fairnessand
Intervention
explainability. ItcorrespondstothedeploymentofAItosolvethecredit
scoringpredictionproblemandcanincorporatemultiplepillars.
Specifieswhattheinterventionisevaluatedagainst. Inthiscontext,studies
mustmakeuseofexistingbaselinestobenchmarktheirmethodsor
Comparison
highlightthetrade-offsacrossthepillars. Thiselementiscrucial,asit
analyzespillarinteractions.
Captureswhatwasmeasuredandreported,illustratingtheoutcomesof
interest,suchasperformanceindicators,fairnessmetrics,explainability
Outcome
withhumancomprehension,andquantitativeassessmentofthetrade-off
analysisbetweenpillars.
Definestheapplicationenvironmentandpublicationconstraints. It
determineswhetherthestudyisexclusivetothecreditscoringdomain,
publishedinapeer-reviewedjournalorconference,ordemonstrates
Context
recencyintermsofreportingfairnessandexplainabilityintegratedinto
modeling. Inaddition,itpinpointswheretrade-offsariseorothergaps
exist,giventhethreepillars.
DrawingonthePICOCframework,thefollowingresearchquestionshavebeenfor-
mulatedtodefinethecontextandobjectivesofthisresearch. Collectively,threeresearch
questionswerealignedwiththestudy’soverarchingaimtoexplorehowcreditscoring
frameworkscanbalancepredictiveperformancewithfairness,explainability,andregula-
toryaccountabilitythroughhuman-in-the-loopconsiderations. Morespecifically,RQ1ex-
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 6of36
aminesthetrade-offsbetweenperformance,interpretability,andfairness,RQ2investigates
thecurrentbiasmitigationstrategiesfocusingontheireffectiveness,andRQ3addresses
theroleofregulationandhumanoversightinensuringethicallyalignedAIsystems.
• RQ1:Towhatextentcancreditscoringframeworksachievecompellingperformance
whilebalancingexplainabilityandfairnesstrade-offs? TheextenttowhichAImod-
elsoperateopaquelyindeterminingcreditworthinessnotonlyhinderstheiradoption
butalsoposesthreatstotheirfairnessandtrustworthiness(Ribeiro-Fluchtetal.,2024).
Inresponse,numerouseffortswithinthecreditscoringlandscapehaveprioritized
transparencyandexplainabilitytodevelopcomplementaryorembeddedmethods
that clarify the rationale and reasoning behind AI-generated outcomes. Model ex-
plainability and interpretability are foundational in the deployment of AI and are
considerednolessimportantthantheperformanceitself. Apartfromdescribingthe
motive,bothcanfundamentallyservetheabilitytoexplaincausesleadingtobiasedor
uncertaindecisions(Alufaisanetal.,2021). High-stakesapplicationsdependcritically
ontheabilitytoreasonaboutandjustifymodeldecisions,wherebythelackoftrans-
parentdecision-makingposesasignificantdrawbackandmayresultinmistrustand
non-compliancewithlocalregulations(Wangetal.,2020). Consideringthecriticality
ofthethreepillars,thisresearchquestionexaminestheextenttowhichthesepillars
canbeelevatedjointlyoriftherearepotentialtrade-offs.
• RQ2: Howdohistoricalrepaymentdata,classimbalance,andprotectedattributes
contributetobiasedpredictions,andwhatmitigationstrategiesaremosteffective?
AcommonissueacrossdatasetsusedtotrainAImodelsisclassimbalance,which
hindersAImodelsfromproducingaccurateresults(Chenetal.,2024). Thisproblem
ispervasiveacrosscreditscoringdatasetswherethenumberofdefaultersissignifi-
cantlylessthanthatofnon-defaulters. Suchanimbalanceadverselyaffectsaccuracy,
suggestingtheneedformoreadaptivetechniquesthattreatallclassesequitably. In
addition,thepresenceofprotectedattributesacrossdifferentcreditscoringdatasets
potentiallyamplifiesthehistoricaldiscriminationagainstminoritygroups,leaving
structuraltracesintrainingdata(Hurlinetal.,2024;Talaatetal.,2024). Forinstance,
certainethnicgroupshavehistoricallybeengrantedcreditlessfrequently, thereby
appearing more frequently in the “bad” class, not due to actual risk but because
theyweredeniedfavorableproductsorguidance. Addressingthisresearchquestion
revealstherelationshipsamongclassimbalance,aswellastheirpotentialeffecton
protectedattributes,andprovidesmeanstounderstandthemitigationstrategiesthat
eliminatebiaseddecisions.
• RQ3: Howdoregulatoryframeworksandhuman-in-the-loop(HITL)approaches
influence the interpretation of fairness across different contexts, and how can
theybeincorporatedintoethicallyalignedAImodels? GiventhatAImodelsare
pronetobiaseddecisionsandlacktransparencyinhowtheirresultsaredetermined,
the intervention of regulatory bodies underscores the importance of consciously
adoptingAIindomainsinvolvingmonetarydecisionsandfundamentalhumanrights.
Whileprecisionandaccuracyweretheultimategoalssoughtinthepast,thelossof
transparencyhasprovenfarmorecostlyincriticalandregulateddomains,making
explainability a necessity rather than an option (Chen et al., 2024). Ensuring this
balanceenablestheresponsibleandaccountabledeploymentofAIincreditscoring
domains, supported by adequate human oversight to maintain compliance with
localregulations,andensuresthatresultsremaincomprehensibletohumandecision-
makers(Pengetal.,2023).
Guidedbytheseresearchquestions,thisworkaimstoexplorethepotentialtrade-offs
andpossibilitiestoincorporatemultipledimensionstoformanintersectionalframework
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 7of36
builtaroundthetriadofperformance,explainability,andfairness,withRegulationand
HITL. Figure 2 illustrates the conceptual framework showing the intersections among
performance,explainability,andfairnessinAI-drivencreditscoring. Theouterlayersrep-
resentregulatoryoversightandhumaninterventionascontextualdimensionsinfluencing
allthreepillars. Eachoverlapcorrespondstotheresearchquestions(RQ1–RQ3)guiding
thissystematicliteraturereview.
Figure2.Conceptualframeworkofperformance,fairness,andexplainabilityinAIcreditscoring.
2.2. SearchStrategy
Toensuretheretrievaloftherelevantliteratureandrefinethescope,thesearchstring
wascarefullycraftedtoemphasizetheintersectionbetweenthethreepillarshighlighted
earlier. Moreimportantly,italsohighlightsrecentadvancementsrelatedtobalancingor
interactionacrossthesedistinctdimensions. Therefore,thestudywasconductedusing
theIEEE,Scopus,WebofScience,andScienceDirectdatabasestoensurecomprehensive
andsufficientcoverageofpeer-reviewedjournalarticlesandconferenceproceedings. In
addition, Scopus included records from major indexing services such as ScienceDirect,
SpringerLink,WileyOnline,Taylor&FrancisOnline,IEEEXplore,andACMDigitalLibrary.
Thisensuredbroadinterdisciplinarycoverageofrelevantsourcesandthatthesearchwas
conductedacrossmultiplemajordatabasestoreducethelikelihoodofdatabase-specific
omission and bias in the retrieval process. Table 2 presents the search string used for
literatureretrieval.
Table2.Booleansearchstringusedtoretrievepublicationsbetween2020and2025.
TITLE-ABS-KEY(“creditscoring”OR“creditrisk”)
AND TITLE-ABS-KEY (“machine learning” OR “deep learning” OR “artificial intelligence” OR
“reinforcementlearning”OR“deepreinforcementlearning”)
ANDTITLE-ABS-KEY(“explainableAI”OR“interpretability”OR“modeltransparency”OR“XAI”
OR“fairness”OR“bias”OR“discrimination”OR“protectedattribute*”)
ANDPUBYEAR≥2020ANDPUBYEAR≤2025
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 8of36
Thesearchstringwasdesignedtolocaterelevantpapersbymatchingthespecified
keywordsacrossthetitles,abstracts,andkeywordssections;therefore,thefieldcode(TITLE-
ABS-KEY)wasused. Inaddition,keytermsandsynonymswereselectedtorepresentthe
coredimensionsofthisstudy,i.e.,explainability,fairnessandperformance. Optionally,
paperswererequiredtoaddressatleastonesecondarydimensionrelatedtofairnessor
explainability,ratherthanfocusingsolelyonperformance. Thisprocessinitiallyretrieveda
totalof436paperspriortotheselectionandscreeningstages.
2.3. SelectionCriteria
Togoverntheselectionofrecords,asetofselectioncriteriawasestablishedtocover
bothinclusionandexclusionprinciples. Thisincludesscreeningatthetitleorabstractlevel
andfull-textexclusion. Itensuresthattheselectionisstructuredandreproducible,that
the pool of studies aligns well with the research questions, and that biased selection is
prevented. Duetothelargevolumeofrecords,onlyarepresentativesubsetofpaperswas
considered,guidedbythePICOCcomponentsspecifiedearlier.
2.3.1. InclusionCriteria
Only studies that were published from 2020 onward in reputable, peer-reviewed
venues,suchasACM,IEEE,Springer,andElsevier,wereconsideredinthiswork. Thistem-
poralscopewasintentionallyselectedtocapturethemostrecentphaseofAI-basedcredit
scoringresearchshapedbytherapidadoptionofexplainableAI(XAI)andfairness-aware
learning,alongsideincreasingregulatoryscrutinyofautomateddecision-makinginhigh-
stakesdomains. Theperiodfrom2020onwardreflectsthegrowingmaturityofexplanation
techniques,counterfactualrecourse,andfairnessconstraintsintegratedintomodernlearn-
ingobjectives,aswellastheincreasingemphasisontransparency,non-discrimination,and
auditabilityincreditdecisionpipelines,alignedwithemergingAIgovernanceandaccount-
abilityrequirements. Moreimportantly,restrictingthescopetorecentstudiesincreasesthe
likelihoodofcapturingmethodsandevidencethatjointlyaddressmultiplepillarswithin
thesameexperimentalsetting,whichisessentialforintersection-orientedassessment.
The eligibility of papers was later assessed based on their coverage of at least one
additionaldimensionbeyondtheperformanceofcreditscoringmodels,namelyexplain-
ability and fairness, as highlighted earlier. In addition, the context and domain of the
researchmustbeexclusivetocreditscoringorcreditriskassessment,andthestudiesmust
demonstratemeasurableorinterpretableoutcomesor,ataminimum,conceptuallysupport
integratingfairnessandexplainabilityintocreditscoringframeworkstoestablishclear
linksforethicalframeworkassessment.
2.3.2. ExclusionCriteria
Studiesnotmeetingtheinclusioncriteriawereexcludedordeemedinsufficientto
explicitlyintegratethedifferentdimensionsofthisstudy. Thisincludedstudiesfalling
outsidethecreditscoringdomainoraddressingirrelevantAIapplicationssuchasNLP,
frauddetection,orinsurancerisk. Further,non-peer-reviewedmaterials,pre-2020pub-
lications,andoverlygenericworkswerealsoomitted. Additionalexclusionsappliedto
papersfocusingonlyonperformanceorfeatureselectionwithoutfairnessorexplainabil-
ity,orthoseaddressingcorporatelending,profitorlossprediction,ortransferlearning
basedonexternaldatasets. Purelyconceptualorregulatorydiscussionswereexcluded
unlessdirectlyrelevanttofairnessandexplainabilityunderRQ3. Lastly,studiesaddressing
creditscoringforcorporateloansandSmallandMediumEnterprises(SMEs)werealso
omittedfromthisstudy,astheydonotrelatetodataprivacyandtheinclusionofsensitive
(protected)attributes.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 9of36
2.4. ScreeningProcess
Followingtheinclusionandexclusioncriteriaspecifiedintheearliersubsection,the
PRISMA 2020 guidelines (Page et al., 2021) were followed, ensuring records identified
through database searches were screened by title, abstract, and full text to ensure their
alignment with the RQs. Figure 3 provides a summary of the systematic flow of study
identification,screening,eligibilityassessment,andinclusion.
Figure3.PRISMA2020flowdiagramforthesystematicidentificationandscreeningofstudies.
Theinitialsearchresultreturned436recordsfromelectronicdatabases,withnoaddi-
tionalrecordsfromregistersbeingconsidered. Duringtheidentificationphase,132records
wereexcludedduetoduplication(i.e.,identicalpapersretrievedfrommultipledatabases),
irrelevance,methodologicaloverlap,ordiscrepantmetadata. Theremaining304records
weresubjectedtotitleandabstractscreening,duringwhich227recordswereexcludedfor
failingtomeettheinclusioncriteriaspecified. Thisincluded,forinstance,applicationsof
AIincorporatecreditscoring,unrelateddomains,ornon–peer-reviewedmaterials.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 10of36
In the eligibility assessment stage, 77 reports were sought for full-text retrieval, of
which19couldnotbeaccessedduetounavailabilityorsubscription-basedrestrictions.
Theremaining58reportsunderwentfull-textassessmentagainstthequalityassessment,
basedonwhich10reportswereexcludedduetolow-qualityappraisalscores,and5were
excludedduetooverlappingscopeoroutdatedsurveycontent,asdetailedinAppendixA.
Finally,43studieswereincludedinthisreview,formingthefinalcorpusanalyzedacross
thedimensionsofperformance,explainability,andfairness.
Allrecordsretrievedfromtheselecteddatabaseswerescreenedbyonereviewerusing
thepredefinedinclusionandexclusioncriteria. Thescreeningwasperformedintwostages,
i.e., title/abstractscreeningfollowedbyfull-textassessment. Anyuncertaintiesduring
screeningwereresolvedthroughrepeatedmanualverificationagainsttheeligibilitycriteria.
2.5. DataExtraction
Tosystematicallyrecordthebibliographicinformation,methodologicaldetails,and
thematicattributionsofthe43includedstudies,astructureddatasheetwascreated,andthe
dataextractionwasperformedbyonereviewertoensureconsistencyandreproducibility.
MetadataextractedfromthesearchdatabaseswereimportedintoZoteroastheprimary
referencemanagementtool,thenexportedtoExcelforcodingandsynthesis. Bibliographic
details such as title, abstract, authors, DOIs, publication year, and venue formed the
evidencebaseforsubsequentanalysis.
Forthematicclassification,eachstudywastaggedtoreflectitsdominantthemesacross
performance,explainability,andfairness,aswellasconnectionstoregulatoryandHITL
concepts. Thesetagswereinstrumentalinidentifyingintersectionsamongthedimensions,
supportingtheconceptualframeworkdescribedinFigure2. Tominimizetranscription
errors,theextractedentrieswerecross-checkedagainsttheoriginalarticlesbeforesynthesis.
Noautomationtoolswereusedforextraction,andthestudy’sauthorswerenotcontacted
foradditionalinformation.
2.6. QualityAssessment
Sincetheincludedstudiesaremethodologicallydiverseandtargetatleastonepillar,
andsincethesynthesisofthisworkisnarrativeratherthaneffect-sizebased,thisreview
did not employ a domain-specific risk-of-bias tool. Instead, to ensure the inclusion of
methodologicallyandconceptuallyalignedstudies,astructuredmulti-criteriaappraisal
(Keele, 2007) was conducted by leveraging evidence weighting practices to assess the
relevance and rigor of each study. To support this, a customized 3Rs&Q framework
wasdesignedtoassessthecontributionofeachworktowardtheinteractionamongthe
three main pillars while also accounting for contextual dimensions such as regulation
andhumanintervention. Thescoringscalerangedfrom0to3,wherebyvaluesof0and
3 indicate the lowest and highest scores, respectively. Considering each 3Rs&Q metric
consistsoftwosub-metrics(R1–R6andQ1–Q2),thetotalattainablescorewas24,asshown
inTable3. Thetierthresholds(high: 17–24;medium: 9–16;low: <9)weredetermineda
prioribasedonequaldistributionacrossthe24-pointscaleandreflectincreasinglevelsof
methodologicalalignmentwiththethreepillars. Thisdistribution-basedapproachalso
ensuresthatpapersscoring8orbelowfallnaturallywithinthelower-qualitytierofthe
3Rs&Q scale. Papers demonstrating strong methodological and conceptual rigor were
scoredbetween17and24,formingthehigh-qualitytier. Inaddition,papersthatprovided
partialcoverageofisolateddimensions,suchasfocusingonlyonfairness,butstilloffered
usefulinsights,receivedscoresrangingfrom9to16andbelongedtothemedium-quality
tier. Lastly,theremainderofthestudiesthatscoredbelow9pointswerenotconsidered
duetolimitedconnectiontothereview’scoredimensions.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
11of36
Thiscustomized3Rs&Qappraisalframeworkwasappliedasastructuredrubricto
supportconsistentqualityappraisalacrossincludedstudies. Sincerubric-basedscoring
may introduce assessor subjectivity, scores were assigned using evidence-driven rules
thatreliedonlyonexplicitlyreportedinformationwithineachpaperratherthaninferred
intentions. Borderlinecaseswerere-checkedagainsttheoriginaltextandscoredconserva-
tivelywhenevidencewasinsufficient,ensuringthattheappraisalreflectsdocumentedand
relevantcontributionstothereview’scoredimensions.
Table3.The3Rs&Qqualityassessmentframeworkforevaluatingstudyinclusion.
| Dimension | Submetric | Description | ScoringCriteria(0–3) |
| --------- | --------- | ----------- | -------------------- |
Doesthestudyexplicitly
addressatleastoneofthe
sixconceptualpillars
none,peripheral,central
| Relevance | PillarAlignment(R1) | (ExplainableAI,Fairness, |     |
| --------- | ------------------- | ------------------------ | --- |
andfocus
Imbalance,Protected
Attributes,Regulation,
HumanIntervention)?
Doesthepapercontribute
|           |           | evidencetowardoneor    | none,weak,moderateand |
| --------- | --------- | ---------------------- | --------------------- |
| Relevance | RQFit(R2) |                        |                       |
|           |           | moreofthethreeresearch | strong                |
questions(RQs)?
Arethemodelsormethods
|     | MethodologicalSoundness | clearlydescribed, | poor,basic,robust,and |
| --- | ----------------------- | ----------------- | --------------------- |
Rigor
|     | (R3) | validated,and | stateoftheart |
| --- | ---- | ------------- | ------------- |
reproducible?
Doesthestudyuse
real-worlddatasets,
minimal,partial,strong
| Rigor | EvaluationDepth(R4) | multiplemetrics(e.g.,AUC, |     |
| ----- | ------------------- | ------------------------- | --- |
andcomprehensive
fairnessmeasures),or
comparativebaselines?
Doesthestudyconsider
regulatorycompliance(e.g.,
|       | Cross-ContextAwareness |              | none,partial,clearattempt, |
| ----- | ---------------------- | ------------ | -------------------------- |
| Reach |                        | ECOA,GDPR)or |                            |
|       | (R5)                   |              | anddeepanalysis            |
cross-nationalfairness
transferability?
Doesitcombinemultiple
siloed,minorcombination,
|       | IntegrationofDimensions | pillars(e.g.,fairness+    |                       |
| ----- | ----------------------- | ------------------------- | --------------------- |
| Reach |                         |                           | partialintegrationand |
|       | (R6)                    | explainabilityorimbalance |                       |
holisticframework
+regulation)?
Arecode,data,or
|     | Transparency(Q1)and | supplementary | notavailable,vague,partial |
| --- | ------------------- | ------------- | -------------------------- |
Quality
Reproducibility reproducibilityresources andopenandreproducible
available?
Doesthestudyprovide
actionableinsightsfor
theoretical,limited,
| Quality | PracticalRelevance(Q2) | deployment(e.g.,industry |     |
| ------- | ---------------------- | ------------------------ | --- |
moderateandstrong
adoption,humanoversight,
legalcompliance)?
3. Results
3.1. StudySelection
Followingthequalityassessment,atotalof58paperswerethoroughlyassessedand
scored. Amongthese,15papersforming25.8%oftheselectedstudieswereexcludeddueto
lowscores(≤8),failuretomeettheeligibilitycriteriaandoverlappingscopes.Consequently,
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 12of36
theyweredeemedunsuitabletoaddresstheobjectivesofthiswork. Adetailedsummary
ofthe43studiesconsideredintheanalysisandresultsisprovidedinAppendixB.
3.2. CharacteristicsofSelectedStudies
Consideringthe multidisciplinary natureof thecreditscoring problem, studiesin-
cludedinthisreviewwerepublishedacrossvariousvenues,with95.4%and4.6%published
asjournalarticlesandconferencepapers,respectively. Amongindexedsources,13.95%
ofstudieswereretrievedfromIEEEXplore,followedbySpringerLink,withover11.63%.
Bothvenuesrepresentedasubstantialportionoftechnicalandcomputationalresearchin
theselectedsample. Additionally,smallerbutnotableportionsoftheselectedstudieswere
obtainedfromElsevier’sScienceDirectandopen-accesspublications,suchasPLOSONE,
both equally forming 6.98%. Other publications from ACM Digital Library and MDPI
accountedfor2.33%ofthefinalset.
Table4showsthedistributionofstudiescategorizedbypublishedfamily. Giventhat
creditscoringintersectsfinance, statistics, artificialintelligence, andregulatorystudies,
morethanhalfoftheselectedsample(55.81%)waselicitedfromdomain-specificjournals
orconferencevenuesthatdonotbelongtoaparticulardigitallibrary. Furthermore,most
ofthestudiesincludedhereinwerepublishedbetween2023and2024,forming30.2%and
48.8%forthesameyears,respectively. Theremainingstudies—publishedbetween2020
and 2022—formed only 21%, thereby confirming the recency of the intersection across
dimensionsconsideredinthisstudy.
Table4.Distributionofstudiesbypublisherfamily.
Database/PublisherFamily Count %
IEEEXplore 6 13.95%
SpringerLink 5 11.63%
Elsevier(ScienceDirect) 3 6.98%
OpenAccess(Public) 3 6.98%
ACMDigitalLibrary 1 2.33%
MDPI 1 2.33%
Other/Misc. 24 55.81%
3.3. TopicCoverage
Thetrendsobservedinthecoverageacrossdimensions,asshowninFigure4,reveala
clearshiftintheresearchagendaofcreditscoringfrom2023onward,withalowercount
for 2025 since the year was still in progress at the time of data collection. Prior to this,
asmallnumberofstudiescoveredanyoftheinvestigateddimensionsandweremostly
fragmented. While the concept of fairness was simply being applied in AI disciplines,
humaninterventionandregulatoryaspectswerealmostabsent. Thissuggeststhatstudies
priorto2023wereprimarilyfocusedonperformanceand,toacertainextent,onmitigating
biasassociatedwithprotectedattributes.
However, in 2023, there is an evident surge across all investigated dimensions. It
is worth noting that studies increasingly incorporate protected attributes and examine
theireffectsonfairnessandexplainability,underscoringtheirgrowingimportanceinmore
recentstudies. Thissuggestsaturningpointwherethefieldbegantooperationalizean
ethicalandtransparentmodeldesignratherthanbeingmerelyperformance-focused. This
shiftalignswellwiththepolicypressureimposedbyregulators,whichlikelystimulated
regulatoryresponsestoaddressethicalandsocialaccountabilityconcernsintheliterature.
Among all considered dimensions, explainability showed the strongest expansion
between2023and2024,markingitasthedominantandmostsubstantialpillarofrecent
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 13of36
creditscoringresearch. Ontheotherhand,studiesconcerningprotectedattributesand
their regulation in algorithmic decision-making also increased significantly after 2022,
signalingasignificantsurgeincompliancewithgovernanceandlegalframeworks. Human
intervention,however,remainscomparativelyunder-represented,despiteitssignificance
inhigh-stakessettings,particularlywhenthetrade-offbetweenperformanceandfairness
ispresumed. Overall,thistrendrepresentsamajortransitionfromperformance-focused
representationofthecreditscoringproblemtowardbiasandinterpretability-awarecredit
scoring,withregulationandhumaninterventionbeingcentraltoresponsibledeployment.
Figure4.Topiccoveragebyyear.
Furthermore, to quantify the intersections between different dimensions, Table 5
presentsthepairwiseintersectionsbetweenallconsidereddimensionsgroupedbybase
dimension. Notably, fairness and protected attributes represented the largest portion
ofstudiesthataccountedformeasuringfairnessacrosssensitive/privatefeatures,with
21papersdiscussingthisassociation. Thisconfirmsthatfairnessdiscourseisprimarily
anchoredingroupfairnessdefinitions. Moreover,theassociationbetweenfairnessand
otherdimensions,includingregulationandhumanintervention,wasrankedsecondfrom
thepointofviewoffairness,having11papersrelatingittohumancomprehensionand
regulatoryframeworks. Thispatternsuggeststhatwhenfairnessandprotectedattributes
are foregrounded, regulatory requirements involving human oversight are simultane-
ouslyconsidered.
Despitethat,mid-tierintersectionsbetweenexplainabilityandotherpillars,including
fairness,thepresenceofprotectedattributes,regulationandhumanoversightwerefoundin
sevenorfewerpapers,highlightingthisassociation. Thissuggeststhatwhileexplainability
isincreasinglypresentinbias-awareframeworks,itremainsanauxiliaryfunctionandnot
yetcentral.Inotherwords,explainabilityincreditscoringtendstoserveasabias-diagnostic
ratherthanacompliance-orfairness-enforcingmechanism.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
14of36
Table5.Pairwiseintersectionsgroupedbybasedimension.
| Dimension      | Intersect           | Count |
| -------------- | ------------------- | ----- |
|                | Imbalance           | 10    |
|                | Fairness            | 7     |
| Explainability | ProtectedAttributes | 6     |
|                | Regulation          | 6     |
|                | HumanIntervention   | 6     |
|                | ProtectedAttributes | 21    |
|                | Regulation          | 11    |
Fairness
|                     | HumanIntervention | 11  |
| ------------------- | ----------------- | --- |
|                     | Imbalance         | 6   |
|                     | Regulation        | 11  |
| ProtectedAttributes | HumanIntervention | 11  |
|                     | Imbalance         | 4   |
| Regulation          | HumanIntervention | 10  |
4. Discussion
Thissectionexaminesthetrade-offsandassessescompatibilityacrossperformance,
fairness,andexplainabilityasthreecrucialelementsintheethicalandresponsibledeploy-
mentofAIwithinthecreditscoringdomain. Toachievethat,theinteractionsamongthese
pillarsaresynthesizedtodeterminetheircompatibilityanddescribeobservedpatterns.
Inaddition,thissectionhighlightscommonbiasmitigationstrategiesandcomparestheir
effectivenessinthedeploymentpipeline,anditconceptuallyrelatesmodelinterpretation
to human comprehension to support ethically aligned deployment. Where applicable,
the discussion is supported by empirical and conceptual evidence reported in the re-
viewedliterature.
4.1. CompatibilitiesandTrade-Offs(RQ1)
| Performancevs. Explainability |     |     |
| ----------------------------- | --- | --- |
ConsideringthewideadoptionofAImodels,rangingfrominherentlyinterpretable
toblack-boxmodels,thereisnoconsensusfromtheliteratureconfirmingtheavailability
ofuniversallycompliantmodels. Althoughthetermsinterpretabilityandexplainability
areusedinterchangeablyinthiswork,bothdenotetheconsciousadoptionofAIaimed
atestablishingthegroundsforunderstandingmodeloutcomes(Ratuletal.,2021). Over
theyears, modelshavebeenprimarilyperformance-focused, achievinghighpredictive
accuracybutoftenfailingtoexplaintheirresultsduetotheircomplexity. Aclearexampleis
thetransitionfromtraditionalmodels,suchaslogisticregression(LR)andshallowdecision
trees(DTs),tomoresophisticatedboostinganddeeplearning(DL)architectures. Arguably,
despitebothapproachesbeingextensivelyexploredandsharingsimilarities,deeplearning
demonstratesgreatersuitabilityinaddressingmodernandcomplexcreditscoringcontexts.
However,thisadvancementcomesatthecostofinterpretability,whichposeschal-
lengesinhighlyregulated,high-stakesdomains(Bückeretal.,2022). Understandingthe
model’sreasonsforidentifyingdefaultersisfoundationalinthefinancialsector,particu-
larlyincreditriskdomains(Valdrighietal.,2025),consideringthatthisopacityposesa
limitationforcreditassessorsinvalidatingandtrustingtheirresults. Bycontrast,tradi-
tionalandshallowtree-basedmodelsaregenerallymoreinterpretableandcanprovide
insightsintohoweligibilityisdetermined(Kanaparthi,2023). Forinstance,thecoefficients
optimizedinLRreflectthemagnitudeoffeatureinfluenceontheoutput,whileDTsoffer
atransparenttree-likestructureshowingthecollectivedecisionpathsleadingtothefinal
outcome. Conversely,DLmethodsrelyheavilyonpost-hocexplainabilitytechniquesto
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 15of36
compensatefortheiropacity,whichoftenraisescomplianceconcernsinregulatedsectors
(Hjelkrem&Lange,2023).
Consequently,therehasbeenanoticeableexpansionintheadoptionofpost-hocmeth-
ods,particularlySHAPandLIME(Aruleba&Sun,2024;S.Hanetal.,2024;Hjelkrem&
Lange,2023;Hlongwaneetal.,2024;Nwaforetal.,2024;Zhangetal.,2025),whichcan
operateindependentlyofmodeldesign. Forexample,Nwaforetal.(2024)proposedahy-
bridapproachcombiningasingle-dimensionalCNNandXGBoosttoformulateastacking
architectureforcreditscoringwhileensuringexplainability. Theirresultsdemonstrated
greater performance of the hybrid model when compared with native models, such as
CNN,XGBoost,andLR,attaininganaccuracyof96%,exceedingthatoftheinterpretable
LRmodelby4%. AsimilarexamplewasobservedintheworkofHlongwaneetal.(2024).
Theyarguedthatwhiletree-basedmodelssuchasXGBoostandRFprovidepromising
performanceresults,theylacksufficientinterpretabilitytoexplainthem. Byintegrating
SHAP into their deployment pipeline, they successfully visualized feature attributions
towardpredictionoutcomes. However,whentheAUCmeasureswerecomparedagainst
LR,bothRFandXGBoostoutperformedLRbyonly1%.
Theseexamplesprovideconcreteevidencethatthetrade-offbetweenexplainability
andperformanceislargelyassumedratherthanempiricallymeasured. Thisobservationis
inlinewiththeonehighlightedbyDessainetal.(2023),wheretheyexplicitlystatedthatthe
trade-offbetweenperformanceandexplainabilitystemsfromthemovetowardcomplex
black-boxmodelslackingintrinsicinterpretability. Intheirexperiment,theyquantifiedthis
trade-offacross12models,includinginherentlyexplainableandblack-boxmodels. From
abusinessstandpoint, theyconcludedthattheperformancegapbetweeninterpretable
and black-box models corresponds to only 0.14–0.21% in annual return on investment.
Despitethat,theyappliedisotonicsmoothingtoGAMsinordertoincreaseinterpretability
withoutfurtherfinancialloss, achievingperformanceclosetothatofblack-boxmodels.
Therefore,thechoicebetweeninherentlyinterpretableandblack-boxmodelsisprimarily
determinedbyaninstitution’srisktolerance. Itisalsoworthnotingthatstudiesmeasuring
thistrade-offwererelativelylimited,underscoringtheneedforempiricalmeasurementif
inherentlyinterpretablemodelsaretobeconsidered.
Overall,theliteratureindicatesthatexplainabilityispredominantlyintroducedasa
post-hocadditiontoblack-boxmodelsratherthanbeingembeddedorenhancedwithin
inherentlyinterpretableones. Thepresumedtrade-offbetweenperformanceandexplain-
abilityisthusoftenassertedratherthandemonstrated,withalimitednumberofstudies
quantifyingthiscostandobservingittobemarginal. Ingeneral,itisobservedthatthe
currentpracticeincreditscoringfavorspreservingpredictivestrengthwhilemitigating
opacitythroughauxiliaryexplainabilitymethodsratherthanprioritizinginterpretability
fromtheoutset.
Despiterecurringclaimsthatmodeltransparencydegradespredictivestrength,empir-
icalevidenceshowsthattheperformancegapsbetweentransparentandblack-boxmodels
areconsistentlymarginal,asillustratedinTable6,withlimitedstudiesdemonstratinga
substantialperformancedegradationwhenusinginterpretablebaselines. Itisalsoworth
notingthatthecomparisonresultsshouldbeperceivedunderafairsetting, wherepre-
processingandfeaturepreparationstepsareappliedconsistentlyacrossbothinterpretable
andblack-boxmodels,ensuringthatobserveddifferencesreflectmodelcapacityrather
than unequal data treatment. In some cases, the gain from complex models was even
negligible,denotingthattheperceivedtrade-offislargelyassumedbutrarelyquantified.
Asaresult,modelexplainabilitytendstobeincorporatedaftermodelselectionratherthan
shapingit,implyingthattheperformanceandexplainabilityconflictislessstructuralthan
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
16of36
commonlyportrayed,particularlyinregulatedcreditscoringcontextswhereevenmarginal
gainsrarelyjustifyopacity.
Table6.Comparisonofinterpretablevs.black-boxmodelperformanceinincludedstudies.
| Paper | Dataset | ModelsCompared | Metric  | Interp. Black-Box | ∆     |
| ----- | ------- | -------------- | ------- | ----------------- | ----- |
|       |         |                | AUC     | 0.95 0.99         | +0.04 |
|       |         |                | H-score | 0.95 0.95         | 0.00  |
Nwaforetal.(2024) LendingClub LRvs.XGB Precision(w) 0.93 0.95 +0.02
|     |     |     | Recall(w)   | 0.92 0.94 | +0.02 |
| --- | --- | --- | ----------- | --------- | ----- |
|     |     |     | F1-score(w) | 0.92 0.94 | +0.02 |
S.Hanetal.(2024) HE&GMSC(best-case) LRvs.RF/GB AUC 0.9750 0.9891 +0.0141
Chaietal.(2025) Farmers(best-case) DTvs.LCE AUC 0.622 0.784 +0.162
|     | Taiwan | LRvs.RF(best-case) | AUC | 0.74891 0.75929 | +0.01038 |
| --- | ------ | ------------------ | --- | --------------- | -------- |
Hlongwaneetal.(2024)
|                         | HomeCredit             | LRvs.XGB(best-case) | AUC      | 0.69644 0.69766 | +0.00122 |
| ----------------------- | ---------------------- | ------------------- | -------- | --------------- | -------- |
|                         |                        |                     | AUC      | 86.81 89.17     | +2.36    |
| Zhangetal.(2025)        | PCL                    | DTvs.IAIBS          | Accuracy | 76.95 79.32     | +2.37    |
|                         |                        |                     | F1       | 56.79 59.39     | +2.60    |
|                         |                        | LRvs.IAIBS          | AUC      | 77.48 79.86     | +2.38    |
|                         | FICO                   |                     | Accuracy | 71.52 74.55     | +3.03    |
|                         |                        |                     | F1       | 73.93 76.51     | +2.58    |
|                         |                        | DTvs.IAIBS          | AUC      | 96.04 97.48     | +1.44    |
|                         | CCF                    | LRvs.IAIBS          | Accuracy | 97.45 97.56     | +0.11    |
|                         |                        |                     | F1       | 86.71 88.69     | +1.98    |
|                         |                        | LRvs.IAIBS          | AUC      | 61.91 66.03     | +4.12    |
|                         | VL                     |                     | Accuracy | 59.32 62.70     | +3.38    |
|                         |                        |                     | F1       | 60.18 63.31     | +3.13    |
|                         |                        |                     | Accuracy | 0.720 0.783     | +0.063   |
|                         |                        | DTvs.ANN            | F1-score | 0.644 0.747     | +0.103   |
| AliShaheeandPatel(2025) | Proprietary            |                     |          |                 |          |
|                         |                        | (ADASYN+FL)         | AUC      | 0.737 0.812     | +0.075   |
|                         |                        |                     | G-mean   | 0.602 0.747     | +0.145   |
|                         |                        | LRvs.LightGBM       | AUC      | 0.91 0.94       | +0.03    |
|                         |                        | LRvs.CatBoost       | AUC      | 0.91 0.94       | +0.03    |
|                         |                        | LRvs.RF             | AUC      | 0.91 0.93       | +0.02    |
|                         |                        | LRvs.MLP            | AUC      | 0.91 0.91       | +0.00    |
|                         |                        | SVMvs.LightGBM      | AUC      | 0.88 0.94       | +0.06    |
|                         |                        | SVMvs.CatBoost      | AUC      | 0.88 0.94       | +0.06    |
|                         |                        | SVMvs.RF            | AUC      | 0.88 0.93       | +0.05    |
|                         |                        | SVMvs.MLP           | AUC      | 0.88 0.91       | +0.03    |
|                         |                        | NBvs.LightGBM       | AUC      | 0.89 0.94       | +0.05    |
|                         |                        | NBvs.CatBoost       | AUC      | 0.89 0.94       | +0.05    |
|                         |                        | NBvs.RF             | AUC      | 0.89 0.93       | +0.04    |
|                         |                        | NBvs.MLP            | AUC      | 0.89 0.91       | +0.02    |
| L.H.Lietal.(2025)       | LendingClub(2007–2020) |                     |          |                 |          |
|                         |                        | LRvs.LightGBM       | Accuracy | 0.83 0.87       | +0.04    |
|                         |                        | LRvs.CatBoost       | Accuracy | 0.83 0.86       | +0.03    |
|                         |                        | LRvs.RF             | Accuracy | 0.83 0.86       | +0.03    |
|                         |                        | LRvs.MLP            | Accuracy | 0.83 0.84       | +0.01    |
|                         |                        | SVMvs.LightGBM      | Accuracy | 0.83 0.87       | +0.04    |
|                         |                        | SVMvs.CatBoost      | Accuracy | 0.83 0.86       | +0.03    |
|                         |                        | SVMvs.RF            | Accuracy | 0.83 0.86       | +0.03    |
|                         |                        | SVMvs.MLP           | Accuracy | 0.83 0.84       | +0.01    |
|                         |                        | NBvs.LightGBM       | Accuracy | 0.81 0.87       | +0.06    |
|                         |                        | NBvs.CatBoost       | Accuracy | 0.81 0.86       | +0.05    |
|                         |                        | NBvs.RF             | Accuracy | 0.81 0.86       | +0.05    |
|                         |                        | NBvs.MLP            | Accuracy | 0.81 0.84       | +0.03    |
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 17of36
To interpret the performance gap between inherently interpretable and black-box
models, the marginal differences reported in Table 6 should be viewed as dataset- and
method-dependent rather than consistent across all settings. While most comparisons
indicateonlyminorperformancevariations,somestudiesreportlargergainswhenthe
modellingapproachintroducesadditionalcapacitytocapturehigher-orderinteractions
andnon-lineardecisionpatterns. Consequently,theobserveddifferencesareconditional
not only on the characteristics of the underlying datasets but also on the experimental
andpre-processingchoicesadoptedineachstudy. Akeydriverofreducedperformance
gaps is the extent of data refinement and feature reduction that simplifies the learning
problem. ThisisdemonstratedbyNwaforetal.(2024),wheretheLendingClubdataset
was reduced from over 1 million observations and 145 features to 25,535 observations
with25featuresthroughexploratoryanalysisandfeaturefiltering. Thisdimensionality
reductionlikelydecreasedredundancyandnoise,enablinginterpretablebaselinessuch
aslogisticregressiontoremaincompetitiveandlimitingtheincrementalgainachieved
byXGBoost.
A similar trend is observed in the work of L. H. Li et al. (2025), where extensive
pre-processing,featurefiltering,andnormalizationappliedtotheLendingClubdataset
resultedinperformanceimprovementsthatremainbroadlycomparableacrossinterpretable
andblack-boxmodels. Evidenceofanevensmallertrade-offisprovidedbyHlongwane
etal.(2024),wherediscretization,featureengineering,andvariableselectionwereused
toconstrainfinalscorecardcomplexityintheTaiwanandHomeCreditdatasets. Under
thiscontrolledsetup,performancedifferencesbetweenlogisticregressionandtree-based
modelsbecamenear-negligible,particularlyinHomeCredit,whereXGBoostyieldedonly
aminimalAUCimprovementoverlogisticregression. Collectively,thesefindingssuggest
thatwheninputdimensionalityisreduced,noiseiscontrolled,andpre-processingsteps
are applied uniformly across model families, the advantage of black-box models often
becomesmarginal.
In contrast, pipelines that do not consider observation and complexity reduction
techniquescanyieldlargergains,particularlywhenexplicitlytargetingcomplexregionsof
thefeaturespacethatinterpretablemodelsstruggletocapture.Zhangetal.(2025)exemplify
thisbyproposingaboundary-focusedhybridframeworkthatretainslogisticregressionas
atransparentbaselinewhileintroducingadeeplearningcomponenttrainedonboundary
samples. Rather than simplifying the feature space through reduction techniques, the
studyappliespre-processingprimarilyforimbalancemitigation,enablingmodelstolearn
moreeffectivelyfromcomplexdecisionboundaries. Thisdesignincreasesmodelcapacity
specificallyinregionswherelineardecisionfunctionsunderperform,helpingtoexplainthe
comparativelylargerimprovementsreportedintheirexperiments. Inconclusion,Table6
indicatesthatthetrade-offbetweenexplainabilityandperformanceisnotuniversalbut
greatly shaped by the complexity of datasets, the extent of pre-processing and feature
reductionapplieduniformlyacrossdifferenttypesofmodels,andwhethertheblack-box
approach is a standard global learner or an advanced architecture designed to capture
high-orderpatterns.
Performancevs. Fairness
Fairness represents a long-standing challenge inherently present in credit scoring
datasets. It reflects a well-known tension with predictive performance, although this
tensionisnotabsolutebutconditionalinmostcases. Itsadverseeffectsonunderserved
and excluded populations stem primarily from historical data, which are often biased
and reflect past human decisions (Das et al., 2023; Valdrighi et al., 2025). When these
biaseddecisionsremainunaddressed,theriskofamplifyingtheirimpactincreaseswiththe
integrationofAImodels,assuchmodelstendtoreproducetheembeddedbiaseswithin
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 18of36
acceptedloanapplications(Chaietal.,2025;Kozodoietal.,2025). Asaresult,fairnessis
integraltoanycreditscoringpractice,whetheritistraditional,statistical,orAI-based,and
ignoringitperpetuatesdiscrimination.
Acrosstheliterature,giventhatbiasisinevitable,fairnessisoftentreatedasamulti-
objectiveoptimizationproblemthataimstooptimizepredictionsundersoftconstraints
(S.Liu&Vicente,2022;Martinezetal.,2020). Thismeansthatpredictivecapabilityand
equitablegrouptreatmentarejointlyoptimizedratherthanonebeingmaximizedatthe
expenseoftheother. Forinstance,BalashankarandLees(2022)arguedthatfairnessinML
canbeachievedbytransparentlypresentingnon-dominantandbest-performingtrade-offs
between demographic group accuracy and overall prediction. Using a Pareto frontier,
humaninvolvementbecomescentraltodeterminethebesttrade-offbetweenperformance
andfairness(Zehlikeetal.,2025). Similarapproacheshavebeenreportedinotherstudies
(Badar&Fisichella,2024;S.Liu&Vicente,2022;Martinezetal.,2020),confirmingthatthe
trade-offbetweenperformanceandfairnessisunavoidableandistypicallymodeledasan
optimizationproblemseekingtobalancebothobjectives.
Havingsaidthat,Kozodoietal.(2022)andBadarandFisichella(2024)furthernoted
thatfairnesscanbeimprovedwhileensuringminimumlossinprofitandperformance,
providedthatparityconstraintsarenotenforcedtoostrictly.Incontrast,havingstrictparity
conditionscouldpotentiallyleadtodeteriorationinpredictionutility.Thisobservation
was empirically reported by S. Liu and Vicente (2022), where they concluded that fair-
nessconstraintsreduceaccuracyprogressivelyastheytighten.Byadjustingtheobjective
functiontominimizepredictionlossandfairnessviolationterms, theyderivedacurve
ofoptimaltrade-offs, demonstratingaproportionalrelationshipbetweenaccuracyand
fairness violations. In other words, minimizing fairness violation results in degraded
accuracy, and vice versa, confirming that fairness is tunable and not strictly achieved.
Therefore,dataimbalancestrategiescontributetofairnesstotheextentthattheyrestore
representativenessandreconstructmissinggroupsthatwouldotherwiseberepresentedas
astructuraldiscrimination.
Furthermore,althoughfairnessanddataimbalancearetreatedseparatelyacrossthe
literature,theyimplicitlyinfluenceoneanotherandcanpotentiallydegradefairnessacross
protectedgroupsifnotaddressed(Brzezinskietal.,2024;J.Liuetal.,2024;Shietal.,2025).
Itformsnotonlyatechnicalissuehinderingperformance,butalsoamaterialexclusion
systemembeddedintocreditscoringmodels. Consideringthatprotectedgroupsarenot
presentatequalratesacrossdifferentoutcomes,dataimbalancetechniquescanrectifythe
adverseeffectsbyover-representingtheseminoritygroupsintheminority(default)class.
Asimilartrade-offpatterncanbeobservedwhenconsideringdataimbalancemitiga-
tionstrategies. Forinstance,theworkofKozodoietal.(2025)demonstratedarecoverable
36%ofperformancelossusingtheirproposedBASLrejectioninferenceframeworkwhile
simultaneouslyimprovingfairnesscomparedwithtraditionalsamplingtechniques. The
goaloftheirframeworkwastograduallyinferlabelstounlabeledsamplesiteratively,until
model performance improves. The process of relabeling continues until all samples in
adatasetarelabeledandreadyforfinaltraining. However,theysimplynotedthatthis
iterativeprocessispronetosamplingbias,henceincreasingtheriskofoverconfidenceand
overfittingofamodel,andtherebydegradingthegeneralizationofthemodel. Thesame
observationwasalsomadebySulastrietal.(2025)andAtif(2025),wherestronginclusion
adjustmentspotentiallyharmgeneralizationandstability.
Overall,theliteraturesuggeststhatwhilethereexistsanotabletrade-off,fairnessis
neitherimpossiblenorcompletelyachievable,buttunable. Thisindicatesthatfairnessis
anoptimizationdecisionthatisboundedbyrisktoleranceandsocietalconstraintsrather
thanbeingatechnicalimpossibility.Theliteratureshowedsomecaseswheremoderate
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 19of36
fairnessadjustmentsachievedcompellingresultsintermsofperformanceaswellasfairness,
whereasaggressivecorrectionstendtodistortdatadistributionsandoftenleadtooverfitting
andinstability.
4.2. FairnessStrategiesinDeploymentPipelines(RQ2)
DespitethenotablegrowthinintegratingfairnessintoAIdeployments,asshownin
Figure 4, out of the selected 43 papers, only 10 explicitly measured the effectiveness
of existing mitigation strategies or proposed novel ones to counter bias in the credit
scoringdomain.Thisrepresentsnomorethan23.25%ofthetotalreviewedstudies,despite
fairnessbeinganintegralandlong-standingconcernincreditscoringratherthananewly
introduced concept (Brzezinski et al., 2024; Kozodoi et al., 2022). As a result, relatively
few studies have addressed the adverse implications of protected attributes in lending
decisions,particularlyinalgorithmicdecision-makingsettingsthatarepronetoproducing
discriminatoryoutcomesthatdisproportionatelyaffectminoritygroups(Moldovan,2023).
ThispatternalignswiththeobservationofKozodoietal.(2022),whoexplicitlystatedthat
fairnessremainsunderexploredrelativetoexplainabilityandclassimbalance.
Before delving into fairness mitigation strategies, it is worth noting that fairness
comesintwodifferentnotions: individualandgroupfairness(Valdrighietal.,2025). The
latterisfocusedongeneralizingcreditdecisionsacrossgroupscharacterizedbyprotected
attributessuchasgender,ethnicity,andreligion. Allstudiesincludedhereinoperationalize
group fairness, whereas individual fairness was mentioned only conceptually in a few
studies,suchastheworkofKozodoietal.(2022),aswellasValdrighietal.(2025),without
empiricalimplementation. Todeterminefairnesseffectiveness,commonlyknownmetrics
areusedtoevaluatetheirsuitabilityacrossdifferentnotions,whichincludeindependence,
separation, and sufficiency (Kozodoi et al., 2025; Moldovan, 2023). These metrics were
foundtobeincompatiblewhencombined,andthereisnouniversalagreementonwhich
metric should be prioritized (Brzezinski et al., 2024; Zehlike et al., 2025). Due to this,
Zehlikeetal.(2025)proposedanovelalgorithmcalledFairInterpolationMethod(FAIM)
thatinterpolatesbetweenthethreefairnesscriteriatodevelopareward/penaltyobjective
functionthatrelaxesthenotionofcompetingmetrics,resultinginaweightedcombination
offairnesscriteria.
Considering that bias may enter the deployment pipeline at multiple stages (Das
etal.,2023),fairnessmetricsareconsistentlyappliedasdownstreamevaluationmeasures,
regardlessoftheinterventionpoint. Accordingly,theliteratureorganizesfairnessinter-
ventionsintothreebroadcategoriesbasedontheirpositioninthedeploymentpipeline:
pre-processing, in-processing, and post-processing (Valdrighi et al., 2025). To date, no
consensusexistsregardingauniversallydominantmitigationstrategy,renderingfairness
apracticalchallengeforlendinginstitutions,aseachcategoryexhibitsdistinctstrengths
and limitations (Kozodoi et al., 2022; Moldovan, 2023). The full set of fairness mitiga-
tionstrategiesidentifiedfromthereviewedliterature,categorizedbyinterventionstage
andmethodologicalcharacteristics,issummarizedinAppendixC.Acrosscategories,no
mitigation strategy consistently dominates others, reinforcing the view of fairness as a
context-dependentoptimizationproblemratherthanauniversalcorrection. Accordingly,
thecomparisonscopeisinevitablylarge,withtheexistenceofcommonaspectsthattouch
oneachmitigationstrategy. Forexample, pre-processingmethodsintervenebeforethe
trainingphaseofAImodelsandaimtomodifythedistributionofdatapriortotraining
(S.Hanetal.,2024). Thisoftenleadstolowerdeploymentcostsandtheabilitytoimprove
fairnesswithouthavingtoretrainmodels,consideringmodelretrainingistime-consuming
(Kozodoietal.,2022). Nonetheless,sincepre-processingstrategiesaremodelagnostic,they
oftenrequirerepeatedadjustmentstothedatapipelineandpotentiallyleadtooverfitting
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 20of36
whenfairnessisstrictlyenforced,makingthemgoodstrategiestotuneandreducebias,
ratherthancompletelyeliminateit(Chaietal.,2025).
Additionally,accordingtoKozodoietal.(2022),in-processingtechniquesconsistently
achievelargerfairnessgainswithminimallossinpredictiveutility,assumingthatfairness
isembeddedintotheoptimizationobjectiveitself. Sincetheytypicallyreportthetrade-off
between accuracy and equity in a Pareto frontier, in-processing techniques offer better
controlandoversighttorealizePareto-efficientcompromises. Severalotherstudiesalso
reportedthisbehavior,confirmingthatthetrade-offismoretunablewhilehavingexplicit
control over the outcomes (S. Liu & Vicente, 2022; Moldovan, 2023). Conversely, since
they account for multiple objectives simultaneously, they incur higher computational
costandoftenrequirehyperparametertuningtoidentifytheoptimalconfigurationdue
totheirmodel-specificmechanism, therebyresultinginhigherimplementationburden
(Valdrighietal.,2025).
Similartopre-processingmethods,post-processingisanotherformofmodel-agnostic
techniques that aim to adjust model outputs post-training to meet fairness criteria
(Zehlikeetal.,2025). Thismakesthemaversatileoptionforblack-boxmodelsandstrictly
governed scorecards, since bias mitigation is performed in isolation from the model’s
training and prediction themselves (Valdrighi et al., 2025). Despite this, they incur the
highestutilitycostperfairnessgainandcannotrepairupstreambiassincetheyactsolely
on the decision boundary. As a result, post-processing techniques exhibit a substantial
decreaseinprofitabilityrelativetoin-processingoptions,andtheyarelesstunablethan
in-processingtechniquessincetheyoperateonoutputsinsteadoflearnedrepresentations
(Kozodoietal.,2022).
Synthesizing the findings across studies reveals that fairness mitigation should be
viewed as an optimization problem rather than a one-time corrective step, with trade-
offs emerging between predictive performance, implementation complexity, and regu-
latory suitability. Pre-processing methods intervene before model training by modify-
ing data distributions (S. Han et al., 2024), often offering lower deployment costs and
model-agnosticapplicability. However, strictenforcementoffairnessconstraintsatthe
data level may require repeated adjustments and can introduce overfitting risks, mak-
ing such approaches more suitable for bias reduction rather than complete mitigation
(Chaietal.,2025;Kozodoietal.,2022).
Overall,whileeachfairnessstrategyhasitsownstrengthsandweaknesses,thelitera-
turemakesitevidentthatthereexistsnouniversallydominantstrategyacrossthescoring
pipeline. Rather,thesestrategiesemergeasacase-dependentoptimizationproblemthat
ismainlyinfluencedbytheregulatoryenvironmentandthelevelofriskappetitewithin
the institution. Consequently, this positions fairness as a continuous process that must
beintegratedholisticallythroughoutthedeploymentpipeline,ratherthancorrectedata
singlestage,asalreadyhighlightedbyDasetal.(2023).
4.3. Regulatory,Ethical,andGovernanceFoundationsforFairAICreditScoring(RQ3)
IntheUnitedStates,theEqualCreditOpportunityAct(ECOA)andtheFairCredit
ReportingAct(FCRA)havecollectivelyimposedobligationstoensureequaltreatment
acrossprotectedgroups,andmoreimportantly,toprovide“adversedecisionjustifications”
withinstricttimelines(Kumaretal.,2022).Thesestatutoryrequirementsimplicitlymandate
interpretableAIsystemscapableofsupportingsupervisoryexaminationsandconsumer
recourse. Similarly,inEurope,modelsthatoperateopaquelyandfailtoprovideadequate
justificationforalgorithmicallydeterminedresultsweresubjectedtomistrust,viewedas
presentingheightenedbiasrisks,andclassifiedashigh-riskapplications(Langenbucher,
2020). Accordingly,theEuropeanUnionenforcedfairness-through-explainabilityrequire-
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 21of36
mentsundertheforthcomingAIAct, emphasizingtransparencyandadequatefairness
measures(Perryetal.,2023). Additionally,privacylawssuchasGDPRintersectwiththese
fairnessobligations,assensitiveattributesmaydirectlyorindirectlyinfluenceoutcomes,
posingdiscriminatoryrisksifleftunmitigated(Ridzuanetal.,2024).
Beyond Western regulatory frameworks, the ASEAN region also experienced the
riseofgovernanceapproachesthatprioritizefairnessinthealgorithmiclendingprocess,
withadditionalemphasisonhumanoversight(Lainez&Gardner,2023). Similartothe
EUAIActproposal,ASEANpolicyguidanceencouragestheHITLreview,particularly
in high-stakes and credit scoring domains, while also stressing explainability as a key
enablerforasupervisedevaluation(Ridzuanetal.,2024). Thismakeshumanintervention
central to validating outcomes and correcting undesired results. While these laws and
actsreferencedintheliteraturemightseemlessprescriptive,theysignalagrowingglobal
convergencetowardresponsibleAIcreditscoring,withnotablevariationinmaturityand
enforcementintensity. However,acrossmultiplejurisdictionalsettings,theseexpectations
converge on the principle of fairness in algorithmic decision-making, which cannot be
achievedwithoutconsciouslyadoptingAIsystemsthatprovideadequateexplainability.
Explainabilityservesasthemechanismthroughwhichdiscriminatoryriskscanberevealed,
adverseeffectscanbejustified,and,inthemostseverecases,correctedthroughhuman
oversight. Thus,itfunctionsnotmerelyasatransparencytoolbutasapivotalenablerfor
equity,accountability,andtheethicaldeploymentofAI(Langenbucher,2020).
TheincludedliteratureprovidesricherdetailforWesternandASEANregions,whereas
coveragebeyondthesesettingsbecomescomparativelysparseandfragmented. Inthese
cases, explicit governance and privacy references appear less frequently and are often
discussedatahigherlevelofabstraction. Forexample, additionalevidencefromother
Asian settings includes institutional governance signals, such as the Bank of Indonesia
supportingcredit-relateddecision-makingthroughMSMEprofiling(Hartomoetal.,2025)
andHongKongSARbankingguidanceonconsumerprotectionandhigh-levelAIusage
principles(Ridzuanetal.,2024). WithinASEAN,Vietnamprovidescomparativelyricher
legal framing, where algorithmic credit scoring is described as expanding amid weak
oversight,motivatingproposalsforstrongersafeguards,includinglimitsondatacollection,
consumer rights to explanation and appeal, and inspection powers by regulators such
astheStateBankofVietnam,togetherwithexplicitobligationsalignedtopersonaldata
protectionsuchasconsent,correction,deletionafteruse,andnotificationofthird-party
transfers(Lainez&Gardner,2023).InAfrica,onestudynotesthatcreditregulatorsinSouth
Africarequirecreditdecisionmodelstoprovidehuman-understandableinterpretations
(Hlongwaneetal.,2024),whileevidencelinkedtoLatinAmericahighlightsthatregulatory
and privacy requirements constrain the availability of comprehensive public financial
datasetsforresearchandbenchmarking,particularlyinBrazil(Valdrighietal.,2025).
Nonetheless, the literature increasingly shifts from treating fairness, often framed
throughanti-discriminationandconsumerprotectionexpectations,andexplainabilityas
optionaladd-onstorecognizingthemasfoundationalnecessitiesinAIcreditscoring,re-
flectinghowgloballawsandregulatorycontextsareshapingalgorithmicdecision-making.
Although explainability and fairness were addressed separately in most of the works
included herein, the reviewed studies consistently emphasize their conceptual interde-
pendence(Langenbucher,2020). Modelexplainabilityconstitutestheoperationalbridge
between fairness goals, compliance and human judgment and thereby supports audit-
ing,adverse-actionreasoning,andregulatorydisclosure(Dasetal.,2023).Althoughmost
reviewedstudiesaddressthesepillarsseparately,theworkofHickeyetal.(2020)opera-
tionalizedtheroleofexplainabilitytosupportfairnessinthelendingprocess. Theyargued
thatwhilepost-hocexplainabilityiswidelyadopted,itdoesnotitselfresolvefairnessissues
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 22of36
butratherguidestheiroperationalization. Toaddressthis,theyproposedaSHAP-based
regularizationtermthatpenalizespredictionscorrelatedwithprotectedattributes. This
penaltywasincorporatedintothemodel’slossfunctiontodiscourageitfromprovidingpre-
dictionsthathighlydependonprotectedattributes. Thisadversarialtechniqueconstrains
theattributionstoforcefairnessthroughexplainability,therebyservingasthemechanism
thatdirectlyexposesandregulatesamodel’sdependenceonprotectedattributes.
Insupportoffairness,however,theEUAIAct,aswellasECOA,explicitlyempha-
size the right to contest adverse action notices, extending auditors’ ability to challenge
automatedoutcomesandobtainmeaningfulreconsiderationtoensureessentialprocedu-
ral safeguards (Kumar et al., 2022; Langenbucher, 2020). This captures a key idea that
explainability is not merely for consumers but for supervisory examination and audit
trails,enablingindividualstoappealorseekreconsiderationwhenoutcomesaredoubtful.
Theconceptofchallengingoutcomesthroughhumanoversightandprovidingmeansto
correctunintentionaladverseoutcomesalignswellwiththequalitativestudyconducted
byKuiperetal.(2021),wheretheymanagedtoinvestigatethedisparitybetweenpractice
andlegalframeworksconcerningexplainability. Theyreportedthatwheninterpretability
isinherent,additionalexplainabilitybecomeslesscritical. However,theyalsonotedthat
explainabilitybecomesevidentlycrucialwhenadvancedAImodelsproduceresultsthat
conflictwiththeoutcomesmadebytraditionalmodels,encouraginghumanintervention
toactasapotentialethicalsafeguard.
In addition, given the fairness–performance trade-off, human-in-the-loop (HITL)
oversight can be operationalized as a recurring governance mechanism across the fair-
nesspipeline,ensuringthathumanjudgmentremainsembeddedthroughoutmodelde-
velopment and deployment. First, HITL can be applied between pre-processing and
in-processingstagestocertifyaugmentedandrebalanceddatasetsandverifythataugmen-
tationdoesnotamplifyhistoricalbiasthroughhistoricalrepaymentrecords,particularly
giventhatleakageofprotectedattributesthroughproxiesisaknownriskincreditscor-
ing(Dasetal.,2023).Second,HITLcansupportmodelselectionduringin-processingby
determininganappropriatetrade-offamongParetonon-dominantsolutionsreturnedby
fairness-awarelearningtechniques,aligningwiththefairness–performancetensiondis-
cussedinRQ2andenablinginstitutionstoselectmodelsthatsatisfyregulatoryexpectations
withoutincurringunjustifiedperformancedegradation. Lastly,HITLremainsessentialin
post-processingasacorrectivelayerthatmitigatesresidualorleakedbiasbyreviewing
flaggedoutcomesandoverridingadversedecisionsthatconflictwithfairnesspoliciesor
governancerequirements. Together,theseoperationalrolesdemonstratethatHITLisnot
merelyanoptionalinterventionbutapracticalgovernancelayerthatsupportscertifiable
fairnessandaccountabilityunderrealisticdeploymentconditions.
Insummary,whilesupervisoryframeworksdonotexplicitlystatehowfairnessand
explainabilitymustbeenforcedtoensureethicaldeployments,theyplayedapivotalrole
inshapingmoderncreditscoring. Initially,itstartedbymandatingjustificationofadverse
effectsandenablingrecoursemechanisms,butfurtherextendedbeyondconsumer-facing
transparencytoenablingcontestingandcorrectingunintendedresultsthatpotentiallylead
todiscriminatoryeffects.Moreover,asthelegalsystemsprioritizefairnessandexplain-
abilityequally,theyalsounveilawell-establishedtiebetweenthetwo. Fairnessmustbe
operationalizedthroughinterpretableandcontestableAIsystems,withhumanjudgment
servingastheethicalsafeguardthatensuresalignmentwithregulatoryandsocietalexpec-
tations. Therefore,regulatoryframeworksandethicalgovernancedonotmerelyinfluence
fairnessinterpretation;rather,theystructurallyintegrateexplainabilityasthemechanism
throughwhichfairnessisevaluated,enforced,andethicallyoperationalizedinAIcredit
scoringsystems.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 23of36
5. GapsandFutureDirections
Despitevariouseffortstoaddressperformance,fairness,andexplainabilityasthree
core pillars in the ethical deployment of AI-based credit scoring, several gaps persist
thatrequirefurtherinvestigation. Fromatechnicalandmethodologicalstandpoint, fu-
tureresearchmustmovebeyondpost-hocexplainabilitytodevelopstandardizedframe-
worksthatincorporateexplainabilityasamodelconstraint,enablinga“fairness-through-
explainability” paradigm that reduces model opacity. This paradigm aligns well with
anticipatedregulatoryrequirements,suchastheabilitytodetectbiasinresults,including
those caused by proxy, protected attributes, correct adverse outcomes through human
oversight, and justify adverse decisions to consumers, all of which cannot be achieved
withoutestablishingstricttiesbetweenfairnessandexplainability. Thistransitionredefines
explainabilityfromatechnicaladd-ontoameaningfulcapabilitythatfacilitatesfairness
andinviteshumanjudgmentwhennecessary.
Fromaregulatoryandauditingperspective,althoughmanystudiesacknowledgethe
importanceofhuman-in-the-loop(HITL)oversight,itremainsunder-specifiedintermsof
practicalimplementation. Inparticular,theliteraturerarelydefinesmeasurableescalation
triggers such as borderline cases, low-confidence predictions, or fairness-related flags,
standardized reviewer actions, or mechanisms for incorporating human feedback into
modelmonitoringandgovernance. FutureworkshouldthereforeformalizeHITLasan
operationalprotocolwithincreditscoringpipelines,ensuringtraceablereview,contesta-
bilityofadverseoutcomes,andconsistentalignmentwithlocalcomplianceandauditing
requirements.Thisisespeciallyimportantwhenfairnessconstraintsintroduceperformance
trade-offs,wherehumangovernanceisneededtojustifymodeladoptiondecisionsunder
institutionalrisktolerance.
Furthermore, while the conflict between explainability and performance is widely
debated, it is rarely quantified. Since there are no explicit legal mandates dictating the
choicebetweeninherentlyinterpretableandblack-boxmodels,itsignalstheneedformore
standardizedmethodologiesthatquantifytheperformancelossincurredwhencompro-
misingperformanceformodeltransparency. Reportingpotentiallossinperformancefor
inherentlyinterpretablemodelscanserveaspracticalguidanceforlendinginstitutions,
enablingthemtoselectbetweentransparentandblack-boxmodelsandjustifythemove
towardblack-boxesifnecessary,allofwhichdependheavilyonthelevelofrisktolerance
andappetite.
Inaddition,giventhatnofairnessmetricormethodisuniversal,andsinceregulatory
frameworkstypicallymandatefairnessoutcomeswithoutexplicitlyspecifyingtechnical
metrics, it is anticipated that future work must focus on interpolating and reconciling
incompatiblefairnessmetrics,ensuringcontext-awaremetricandmethodologicalselection
thatalignswiththelegaldefinitionofnon-discriminationacrossdifferentjurisdictional
settings. Thisincludesdeterminingwhichmetric,orcombinationthereof,alignswellwith
legaldefinitionsthatconcernnon-discrimination.
Overall, the most significant gap would be the absence of standardized AI credit
scoringframeworksthatjointlyoptimizeallthreepillarssimultaneouslywhileestablishing
well-grounded,structuraltiesbetweenthem. Currentmethodsofteninvolvetrainingfor
performance,thenincorporatingexplainabilitymethods,andthenadjustingforfairness,
wheninreality,thesedimensionsintersectacrossallstagesofthedeploymentpipeline.
Therefore,futureresearchmustfocusonproposingunified,multi-objectiveframeworksthat
treatperformance,fairness,andexplainabilityasinterdependentconstraints,addressing
HITLandregulatoryrequirementsconcurrently.
Finally,thissystematicreviewisintendedtoserveasafoundationforafutureapplied
studyaimedatdevelopingandvalidatinganAIcreditscoringmodelthatoperationalizes
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 24of36
the review conclusions within a deployable pipeline. While this work is an evidence
synthesis and does not propose a deployable system, these findings will guide model
selection under practical constraints, support integrating explainability as a structural
requirementratherthanapost-hocadd-on,andevaluatefairnessandperformancestability
underrealisticconditionsthatsupporthumanjudgmentwhennecessary.Suchworkwould
enable empirical verification of unified, multi-objective credit scoring frameworks that
alignperformance,fairness,explainability,andHITLrequirementswithregulatoryand
auditingexpectations.
6. Conclusions
Thissystematicliteraturereview(SLR)synthesizes43high-qualityacademicpapers
publishedbetween2020and2025,focusingontheintersectionofperformance,fairness,
andexplainabilityinAIcreditscoring. ByadheringtoPRISMAguidelinesandemploying
adetailed3Rs&Qappraisalframework,thereviewestablishedthatwhilecreditscoring
modelscontinuetograpplewithperformancetrade-offs,explainabilityhasbecomethe
dominantresearchpillarsince2023. Thisshiftislargelydrivenbyregulatoryframeworks,
suchastheEUAIAct,ECOA,andASEANprinciples,whichmandateinterpretablesystems
capableofdeliveringadversedecisionjustifications,therebyreinforcingtheneedforhuman
oversight. Althoughthetrade-offbetweenexplainabilityandperformancepersists,the
choicebetweeninterpretableandblack-boxmodelsisshapedprimarilybytherisktolerance
levelofalendinginstitution,andthistrade-offisscarcelymeasuredacrosstheliterature.
In relation to the research questions, the review finds that (RQ1) the widely cited
trade-offbetweenexplainabilityandperformanceislargelyassumedratherthanempiri-
callydemonstrated;thelimitedstudiesthatquantifythisrelationshipshowonlymarginal
differences between inherently interpretable and black-box models, indicating that the
choicebetweenthemisdeterminedprimarilybyaninstitution’srisktoleranceratherthan
measurablepredictiveloss. Incontrast,thetrade-offbetweenperformanceandfairness
isconsistentlyconfirmedacrosstheliterature: fairnessistreatedasamulti-objectiveopti-
mizationproblem,andaggressiveenforcementoffairnessconstraintsresultsinsignificant
performancedegradation,whereasmoderatefairnessadjustmentstendtoyieldbalanced
improvements. (RQ2)Biasoriginatesprimarilyfromhistoricaldatapatterns,classimbal-
ance,andtheinclusionofprotectedattributes,withmitigationstrategiesappliedacross
different stages differing in strengths, but no universally optimal solution. (RQ3) Reg-
ulatoryandgovernanceframeworksincreasinglyemphasizeexplainabilityandhuman
oversight,yetexistingstudieshavenotfullyintegratedtheserequirementsintounified,
end-to-endcreditscoringpipelines.
Inaddition,despitesignificantresearchintomulti-objectiveoptimizationforbalancing
performanceandfairness,thecurrentliteraturepredominantlyreliesonfragmentedand
sequentialapproaches. Modelsareoftenoptimizedforaccuracyfirst,withfairnessand
explainabilityappliedasadjustments. Thisdeficiencyrepresentsthemostpressingfinding
ofthereview,demonstratingtheabsenceofaunified,holisticAIcreditscoringframework
thatco-optimizesallthreepillarssimultaneouslyacrossallstages. Suchsequentialmethod-
ologiesareinadequateformeetingthestrictcomplianceexpectationsofmodernregulatory
environmentsandfailtoembedtransparencyfromthegroundup.
Toaddressthiscriticalgap,thereviewrecommendsthreekeydirectionsforfuture
research. First,scholarsmustfocusondevelopingnovel,unifiedco-optimizationframe-
worksthattreatperformance,fairness,andexplainabilityasinterdependentconstraints
throughouttheentiremodeldesignlife-cycle. Second,researchmustadvancebeyondsta-
tisticaldefinitionsoffairnessbydevelopingandvalidatingcontextualizedfairnessmetrics
tailoredtospecificlendingmarketsandtheirsocio-economiceffectsonprotectedgroups.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
25of36
Finally,empiricalinvestigationsintohuman-in-the-loop(HITL)integrationarerequiredto
examinehowauditorsandcomplianceofficerscaneffectivelyleverageexplainabilityto
ensureregulatorycomplianceandproducecredible,real-worldoutcomes.
AuthorContributions:Conceptualization,R.B.;methodology,R.B.,N.H.andW.E.;software,R.B.;
validation,N.H.andW.E.;formalanalysis,R.B.;investigation,R.B.;resources,W.E.;datacuration,
R.B.;writing—originaldraftpreparation,R.B.;writing—reviewandediting,N.H.andW.E.;supervi-
sion,N.H.andW.E.;projectadministration,N.H.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement: Thisstudyisbasedonthepreviouslypublishedliterature. Nonew
datasetsweregeneratedoranalyzed.Allreferenceddatasetsarepubliclyavailablefromthesources
citedinthecorrespondingstudies.Thestudyselectionprotocolandappraisalcriteriaareavailable
fromthecorrespondingauthoruponreasonablerequest.
ConflictsofInterest:Theauthorsdeclarenoconflictofinterest.
AppendixA
TableA1.Full-textexcludedstudiesandreasonsforexclusion(Part1:IDs1–8).
| ID Author(s) | Title | ExclusionReason | PRISMABucket |
| ------------ | ----- | --------------- | ------------ |
Excludedduetooverlappingscope,asexplainabilityis
Designingafeatureselection
appliedmainlyaspost-hocSHAP-basedfeature
1 Zachariasetal.(2022) methodbasedonexplainable Overlappingscope
attributionwithinaperformance-drivenpipelinethatis
artificialintelligence
alreadywellrepresentedamongtheincludedstudies.
Excludedduetooverlappingscope,asasurvey-style
|     | AReviewofGenderBias | reviewsummarizingbiasmitigationstrategies,whichis |     |
| --- | ------------------- | ------------------------------------------------- | --- |
Corrales-Barqueroetal.
2 MitigationinCredit alreadycoveredbymorerecentorsynthesis-relevant Overlappingscope
(2021)
|     | ScoringModels | includedsources,contributinglimitedadditionalevidence |     |
| --- | ------------- | ----------------------------------------------------- | --- |
tothereviewobjectives.
Excludedduetooverlappingscope,asthestudyis
|     | TowardsFairAI:MitigatingBias | primarilyasurveysummarizingfairnessandbias |     |
| --- | ---------------------------- | ------------------------------------------ | --- |
deCastroVieiraetal.
3 inCreditDecisions—A mitigationwithoutprovidingdistinctempiricalevidence Overlappingscope
(2025)
|     | SystematicLiteratureReview | orintegratedanalysisacrossperformance,fairness,and |     |
| --- | -------------------------- | -------------------------------------------------- | --- |
explainabilitybeyondincludedworks.
Excludedasoutofscope,asitaddressesAIinfinancial
AIintegrationinfinancial
|                       |                              | servicesbroadlyratherthanAI-basedcreditscoringand   | Didnotmeet  |
| --------------------- | ---------------------------- | --------------------------------------------------- | ----------- |
| 4 Vukovic´etal.(2025) | services:asystematicreviewof |                                                     |             |
|                       |                              | doesnotprovidecreditscoring-specificevidencealigned | eligibility |
trendsandregulatorychallenges
withtherevieweligibilitycriteria.
Excludedduetooverlappingscope,asthestudy
AGeneralArchitecturefora
emphasizesaperformance-orientedarchitecturewith
TrustworthyCreditworthiness-
5 Cornacchiaetal.(2023) explainabilitytreatedprimarilyasapost-hoccomponent, Overlappingscope
AssessmentPlatforminthe
overlappingwithincludedworksaddressingsimilar
FinancialDomain
post-hocexplainabilityconfigurations.
|     | Cost-awareCredit-scoring | Excludedasperformance-orientedonly,focusingonclass |     |
| --- | ------------------------ | -------------------------------------------------- | --- |
FrameworkBasedon imbalancehandling,resampling,andfeatureselectionfor Didnotmeet
6 Mouetal.(2024)
ResamplingandFeature cost-awareoptimizationwithoutsubstantivetreatmentof eligibility
|     | Selection | fairnessorexplainabilityasprimaryreviewpillars. |     |
| --- | --------- | ----------------------------------------------- | --- |
Excludedasperformance-orientedonly,asitevaluates
Ensemblemethodsforcredit
|                  |                              | ensemblelearningprimarilyforpredictiveperformance    | Didnotmeet  |
| ---------------- | ---------------------------- | ---------------------------------------------------- | ----------- |
| 7 Caoetal.(2021) | scoringofChinesepeer-to-peer |                                                      |             |
|                  |                              | withoutexplicitfairness,explainability,orregulatory/ | eligibility |
loans
HITLconsiderationsalignedwiththereviewscope.
|     | A‘divideandconquer’reject | Excludedasreject-inference/performance-oriented,where |     |
| --- | ------------------------- | ----------------------------------------------------- | --- |
rejectinferenceisusedtoaddresssampleselectionbias
|                 | inferenceapproachleveraging |                                        | Didnotmeet  |
| --------------- | --------------------------- | -------------------------------------- | ----------- |
| 8 Wuetal.(2025) |                             | andimprovepredictiveperformancewithout |             |
|                 | graph-basedsemi-supervised  |                                        | eligibility |
protected-attributefairnessanalysisorexplainability
learning
objectivesalignedwiththereviewsynthesisgoals.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
26of36
TableA2.Full-textexcludedstudiesandreasonsforexclusion(Part2:IDs9–15).
| ID Author(s) | Title | ExclusionReason | PRISMABucket |
| ------------ | ----- | --------------- | ------------ |
Excludedasperformance/sample-biasoriented,focusing
CombatingSamplingBias:A
|                   |                             | onaccepted-onlysamplingbiasusingself-trainingwithout    | Didnotmeet  |
| ----------------- | --------------------------- | ------------------------------------------------------- | ----------- |
| 9 Liaoetal.(2022) | Self-TrainingMethodinCredit |                                                         |             |
|                   |                             | explicitlyaddressingfairnessacrossprotectedattributesor | eligibility |
RiskModels
explainabilityascoreobjectives.
Excludedasperformance-orientedonly,proposing
cost-sensitivereinforcementlearningtooptimizecredit
|     | Cost-sensitivereinforcement |     | Didnotmeet |
| --- | --------------------------- | --- | ---------- |
10 C-Rellaetal.(2025) riskdecisioningwithoutoperationalizingfairness,
|     | learningforcreditrisk |     | eligibility |
| --- | --------------------- | --- | ----------- |
explainability,orregulatory/HITLrequirementscentralto
therevieweligibilitycriteria.
Excludedasnoteligible,asitisprimarilyalegal/policy
discussionofautomationandAIethicswithoutcredit
|     | Humancontroloverautomation: |     | Didnotmeet |
| --- | --------------------------- | --- | ---------- |
11 Koulu(2019) scoring-specificempiricalmethodsoroperationalevidence
|     | EUpolicyandAIethics |     | eligibility |
| --- | ------------------- | --- | ----------- |
supportingsynthesisacrossperformance,fairness,and
explainability.
Excludedasreject-inference/performance-oriented,
|     | Inferringtheoutcomesof | focusingonoutcomeinferenceforrejectedapplicantsto |     |
| --- | ---------------------- | ------------------------------------------------- | --- |
Didnotmeet
12 Z.Lietal.(2020) rejectedloans:anapplicationof enhancepredictionperformance,withfairnessand
eligibility
|     | semisupervisedclustering | explainabilitynottreatedascentral, |     |
| --- | ------------------------ | ---------------------------------- | --- |
operationalizedobjectives.
Excludedduetooverlappingscope,asXAIisapplied
BoostingCreditRiskData
mainlyfordata/modeldiagnostics,andexplainabilityis
13 Tiukhovaetal.(2025) QualityUsingMachineLearning Overlappingscope
treatedaspost-hocanalysis,closelyoverlappingwith
andeXplainableAITechniques
includedSHAP-post-hocexplainabilitystudies.
Excludedasoutofscope,asittargetsfinancialrisk
Adata-drivenexplainable
|                    |                             | detectionratherthancreditscoring/creditworthiness | Didnotmeet  |
| ------------------ | --------------------------- | ------------------------------------------------- | ----------- |
| 14 W.Lietal.(2022) | case-basedreasoningapproach |                                                   |             |
|                    |                             | assessment,anditdoesnotalignwiththereview’s       | eligibility |
forfinancialriskdetection
domain-specificeligibilitycriteria.
|     | EnhancingFairnessand | Excludedduetoinsufficientoperationalizationoffairness, |     |
| --- | -------------------- | ------------------------------------------------------ | --- |
ChackoandAravindhar AccuracyinCreditScore asfairnessisreferencedbutnotclearlydefinedusing Didnotmeet
15
(2025) Analysis:ANovelFramework explicitmetricsorevaluationprotocolsthatsupport eligibility
|     | UtilizingKernelPCA | structuredsynthesisundertherevieweligibilitycriteria. |     |
| --- | ------------------ | ----------------------------------------------------- | --- |
AppendixB
TableA3.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part1:IDs1–6).
| ID Author(s) | Title | Summary | RelatedRQs |
| ------------ | ----- | ------- | ---------- |
Examinestrade-offsbetweenfairnessandprofitabilityin
creditscoring.IntegratesfairnessmetricsintoMLpipelines
|     | FairnessinCreditScoring: | andevaluatespre-,in-,andpost-processingmethods |     |
| --- | ------------------------ | ---------------------------------------------- | --- |
1 Kozodoietal.(2022) Assessment,Implementationand (reweighing,prejudiceremover,adversarialdebiasing,reject RQ1,RQ2
|     | ProfitImplications | option)acrosssevendatasets.Concludesfairnesscan |     |
| --- | ------------------ | ----------------------------------------------- | --- |
improvewithoutmajorperformanceloss,supporting
regulatorycomplianceandethicallending.
Explorestheexplainability–performancetrade-offincredit
scoring.Comparesblack-boxandinterpretablemodels
|     | CostofExplainabilityinAI:An | (XGBoost,NN,LR,GAMs)underECBcompliance. |     |
| --- | --------------------------- | --------------------------------------- | --- |
2 Dessainetal.(2023) ExamplewithCreditScoring Introducesisotonicsmoothingtoalignexpertjudgement RQ1,RQ3
|     | Models | withregulatorymaster-scalegrading.FindsGAM-style |     |
| --- | ------ | ------------------------------------------------ | --- |
modelsachievenear-black-boxaccuracywhilepreserving
inherentinterpretabilityandmeetingregulatorystandards.
Assessesalgorithmicbiasandcompares12mitigation
strategiesacrossfivefairnessmetricsusingGermanand
Romaniandatasets.Highlightsthatnosinglefairness
AlgorithmicDecisionMaking measuresatisfiesfairness,performance,andprofitability
| 3 Moldovan(2023) |     |     | RQ1,RQ2,RQ3 |
| ---------------- | --- | --- | ----------- |
MethodsforFairCreditScoring simultaneously.Showsincompatibilitiesamongmetrics
(independence,separation,sufficiency)andstresses
regulatoryambiguityandtheneedforbalanced,
multi-methodapproaches.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 27of36
TableA3.Cont.
ID Author(s) Title Summary RelatedRQs
IntroducestheFairInterpolationMethod(FAIM),a
post-processingalgorithmusingoptimaltransportto
BeyondIncompatibility:Trade-offs
interpolatebetweencalibration,balanceforpositives,and
BetweenMutuallyExclusive
4 Zehlikeetal.(2025) balancefornegatives.MotivatedbytheEUAIAct,it RQ1,RQ2,RQ3
FairnessCriteriainMachine
addressesfairnessincompatibilityandlegalambiguity,
LearningandLaw
emphasizingregulatorinvolvementandhumanoversight
fortrade-offmanagementacrossjurisdictions.
SituatesfairnesswithinECOA,FCRA,andsupervisoryrules;
distinguishesindividualvs.groupfairness.Arguesbiascan
enterpre-,in-,orpost-trainingandcataloguesdatasetbiases
5 Dasetal.(2023) AlgorithmicFairness RQ2,RQ3
andmetrics(e.g.,DI,EO,equalizedodds,predictiveparity).
Advocatesasystemicapproachcombiningdataquality,
interpretability,andregulatoryalignment.
Analyzeseffectsofclassimbalanceandprotected-groupratios
PropertiesofFairnessMeasuresin onfairnessmetricsusingtheUCIAdultdataset.Finds
theContextofVaryingClass StatisticalParityDifferenceandDisparateImpactarehighly
6 Brzezinskietal.(2024) RQ2
ImbalanceandProtected sensitivetoimbalance,whileEqualOpportunityandAverage
GroupRatios OddsDifferencearemorestable.Recommendscontextual
evaluationcombiningfairnessandperformanceindicators.
TableA4.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part2:IDs7–12).
ID Author(s) Title Summary RelatedRQs
ExaminesregulatoryandethicalchallengesinAI-driven
creditscoringunderGDPR,ECOA,FCRA,andGLBA.
Highlightsprivacyrisks,proxydiscrimination,and
Langenbucherand ResponsibleAICreditScoring–A
7 fairness–accuracytrade-offs.Recommendstransparency, RQ1,RQ3
Corcoran(2022) LessonfromUpstart.com
fairnessaudits,human-in-the-loopoversight,andregulator
collaborationtoensurecompliantandexplainablelending
decisions.
OutlinesalegalframeworkforresponsibleAIcreditscoring
basedontransparency,fairness,andaccountability.Warns
ResponsibleA.I.-basedCredit opaquemodelscanconflictwithGDPR’s“righttoexplain.”
8 Langenbucher(2020) RQ3
Scoring–ALegalFramework Recommendsembeddinginterpretability,validatingfairness
throughoutmodelphases,enforcinghumanoversight,and
assigningaccountabilityrolesforlawfuldeployment.
Addressesbias,transparency,andrejectinferencein
AI-basedcreditscoringacrossGerman,Taiwanese,and
HomeCreditdatasets.Discussesbiasorigins,fairness
BestPracticesforResponsible
9 Valdrighietal.(2025) metrics(groupandindividual),andmitigationacrosspre-, RQ1,RQ2
MachineLearninginCreditScoring
in-,andpost-processing.Highlightstransparencytools
(LIME,SHAP,PD,ICE)andemphasizesinclusive,
responsibledeployment.
ReportsqualitativefindingsfromDutchbanksand
regulatorsonintegratingXAIintocreditscoring.Defines
ExploringExplainableAIinthe explainabilityastransparencyintomodelreasoning,data,
10 Kuiperetal.(2021) FinancialSector:Perspectivesof anddesign.Notesrelianceoninterpretabletraditional RQ1,RQ3
BanksandSupervisoryAuthorities models,humansafeguards,andphaseddeployment.
Positionsexplainabilityasessentialforethical,accountable,
regulatory-alignedAI.
Highlightsfairnessasjurisdiction-dependent.UsesPareto
principlestobalancegroup-andoverall-levelaccuracies
TheNeedforTransparent
withhuman-in-the-loopoversight.Showsintersecting
BalashankarandLees DemographicGroupTrade-Offsin
11 protectedattributesreducesamplesizesanddegrade RQ1,RQ2,RQ3
(2022) CreditRiskandIncome
accuracy,motivatingdataimprovements.Advocates
Classification
transparenttrade-offvisualizationtoalignfairness,
performance,andsocialobjectives.
Quantifiesaccuracy–interpretabilitytrade-offsintabular
learningusing45datasets.Findslessthan4%accuracyloss
ExploringAccuracyand
betweenblack-boxandinherentlyinterpretablemodels.
InterpretabilityTrade-offinTabular
12 Amekoeetal.(2024) ProposesaTabSRAattention-basedensembleinspiredby RQ1,RQ3
LearningwithNovel
GAMs,offeringfeature-levelinterpretabilityandstable
Attention-basedModels
performance;arguesforinherentinterpretabilityin
high-stakesdomains.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 28of36
TableA5.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part3:IDs13–18).
ID Author(s) Title Summary RelatedRQs
Formulatesfairness–accuracytrade-offsasastochastic
multi-objectiveoptimizationproblem.Proposesthe
AccuracyandFairnessTrade-offsin StochasticMulti-Gradient(SMG)algorithmusingDisparate
S.LiuandVicente
13 MachineLearning:AStochastic ImpactandEqualOpportunityasconstraints.Demonstrates RQ1,RQ2
(2022)
Multi-objectiveApproach ParetofrontiersontheUCIAdultdataset,showingtension
betweenfairnessandaccuracydrivenbyproxyand
protectedattributes.
Modelsgroupfairnessasmulti-objectiveoptimizationwhere
eachsensitivegroupdefinesafairnessobjective.Proposes
MinimaxParetoFairness:A Minimum-MaximumParetoFairness(MMPF)usingneural
14 Martinezetal.(2020) RQ1,RQ2
Multi-objectivePerspective networkswithpost-hoccorrectionstoreduceriskdisparity.
EvaluatedonGermanCreditandAdultIncomedatasets
withaccuracy,Brierscore,andcross-entropymetrics.
ProposesFair-CMNB,afairness-andimbalance-aware
MixedNaïveBayesmodelforstreamingcreditdatausing
Fair-CMNB:Advancing
multi-objectiveoptimization.Introducesdynamicinstance
BadarandFisichella Fairness-AwareStreamLearning
15 weightingtoprioritizeminorityupdatesandcontrol RQ1,RQ2
(2024) withNaïveBayesand
discrimination.Reportsimprovedaccuracyandfairness
Multi-ObjectiveOptimization
overbaselines,emphasizingscalabilityandpracticalityfor
high-stakescreditscoring.
AppliescausalMLwithBayesiannetworkstomodel
CreditRiskPredictionBasedon cause–effectrelationsandenabletransparentdecision
CausalMachineLearning:Bayesian analysisviaDAGs.UsesSMOTEandL1regularizationfor
16 J.Liuetal.(2024) RQ1,RQ2,RQ3
NetworkLearning,Default imbalancehandlingandfeatureselection.Supports
Inference,andInterpretation interpretable,regulation-orientedwhat-ifanalysisacrosssix
realdatasets.
ProposesanadversarialSHAPframeworklinkingfairness
andexplainabilitybypenalizingpredictionscorrelatedwith
protectedattributesviaSHAP-basedregularization.Uses
FairnessbyExplicabilityand
17 Hickeyetal.(2020) surrogateauditingtomirroroversight.Demonstrates RQ1,RQ2,RQ3
AdversarialSHAPLearning
improvedfairnessandinterpretabilityonAdultIncomeand
proprietarycreditdatasetswhilemaintainingstrong
predictiveperformance.
AnalyzesregulatorygapsandethicalrisksinVietnam’s
AlgorithmicCreditScoringin adoptionofalgorithmiccreditscoring.Highlights
LainezandGardner Vietnam:ALegalProposalfor discrimination,bias,opacity,andprivacyconcernsunder
18 RQ3
(2023) MaximizingBenefitsand FCRA,ECOA,FCA,andtheEUAIAct.Advocatesstronger
MinimizingRisks legaloversightandinterpretabilitystandardstorestoretrust
andfairness.
TableA6.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part4:IDs19–24).
ID Author(s) Title Summary RelatedRQs
ProposesahybridCNN–XGBooststackingmodeltoimprove
EnhancingTransparencyand accuracyandinterpretabilityincreditscoring.UsesSHAP
FairnessinAutomatedCredit globalexplanationstoexaminefeatureeffectsontheLending
19 Nwaforetal.(2024) RQ1,RQ2
Decisions:AnExplainableNovel Clubdataset.Reportshighpredictiveperformancewhile
HybridMachineLearningApproach enhancingtransparencyandtrustinautomatedlending
decisions.
IntroducesNOTE,anon-parametricoversamplingapproach
combiningstackedautoencodersandconditionalWasserstein
NOTE:Non-parametric GANstoaddresssevereclassimbalance.EvaluatedonHome
20 S.Hanetal.(2024) OversamplingTechniquefor EquityandGiveMeSomeCreditdatasets;reportsimproved RQ1,RQ2
ExplainableCreditScoring accuracyoverADSGANandDeepSMOTE.UsesSHAPfor
globalinterpretability,linkingimbalancecorrectionwith
explainablecreditscoring.
ProposesBASL,abias-awareself-learningframework
addressingsamplingbiasfrommissingrejectedapplicants.
FightingSamplingBias:A Usesasemi-supervisedBayesianapproachtoiterativelylabel
21 Kozodoietal.(2025) FrameworkforTrainingand unlabeleddatawhilefilteringoutliers.AppliedtoMonedo’s RQ1,RQ2
EvaluatingCreditScoringModels real-worlddataset;recoversupto36%performancelossdueto
samplingbiasandoutperformsreweightingand
Heckman-stylemethods.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 29of36
TableA6.Cont.
ID Author(s) Title Summary RelatedRQs
ProposesahybridLSTM-basedframeworkcapturingtemporal
borrowerbehaviorforcreditscoring.UsesSMOTE,
CreditScoringPredictionUsingDeep
normalization,andone-hotencodingforimbalancehandling.
22 Shietal.(2025) LearningModelsintheFinancial RQ1,RQ2
Introducesahybridlosswithinterpretabilityregularization
Sector
enforcingfeaturesparsity,aimingtoretaintransparency
withoutrelyingonpost-hocexplainers.
ComparesSHAPwithcounterfactualmethodsfor
interpretabilityincreditscoring.UsesGeneticAlgorithmsto
MachineLearningInterpretabilityfor
generatecounterfactualsidentifyingminimalfeaturechanges
23 Bueffetal.(2022) aStressScenarioGenerationinCredit RQ1,RQ2
neededtoalteroutcomes.Linksinterpretabilitytorobustness
ScoringBasedonCounterfactuals
understressscenariosandhighlightshowcounterfactuals
exposesensitivedecisionboundariesandbias-pronefeatures.
AlignsalgorithmicfairnessresearchwithUS
EqualizingCreditOpportunityin anti-discriminationlaws(ECOA,FCRA,HMDA).Discusses
Algorithms:AligningAlgorithmic disparateimpact/treatmentaslegalfairnesscriteriaandthe
24 Kumaretal.(2022) RQ2,RQ3
FairnessResearchwithU.S.Fair roleofproxyattributesinbias.Advocatescausaland
LendingRegulation counterfactualanalysisandregulatoryoversightforequitable,
transparentAI-drivenlendingpractices.
TableA7.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part5:IDs25–30).
ID Author(s) Title Summary RelatedRQs
ProposesahybridADASYN–LCEmodelcombiningadaptive
Farmers’CreditRiskEvaluationwith resamplingandlocalcascadingensemblesformicrofinance
anExplainableHybridEnsemble creditscoring.UsesSHAPandLIMEforinterpretabilityand
25 Chaietal.(2025) RQ1,RQ2
Approach:ACloserLookin fairnessvalidation.Reportsimprovedrobustnessandvisibility
Microfinance forunderservedpopulationsthroughbalancedlearningand
explainableensemblemodeling.
IntegratesSHAPexplanationsintocreditscoringpipelines
usingXGBoostandRandomForestmodels.Improves
ANovelFrameworkforEnhancing
transparency,regulatoryalignment,andconsumertrustby
Hlongwaneetal. TransparencyinCreditScoring:
26 visualizingfeatureattributions.EvaluatedonTaiwaneseand RQ1
(2024) LeveragingShapleyValuesfor
HomeCreditdatasets,demonstratinginterpretable
InterpretableCreditScorecards
performancealignedwithexplainabilityexpectations
inlending.
ProposesIAIBS,combininglogisticregressionanddeep
AnInterpretableCreditRisk learningtohandleambiguousboundarysamples.UsesARPD
27 Zhangetal.(2025) AssessmentModelwithBoundary toclassifynoise/anomaliesandappliesSHAPfor RQ1
SampleIdentification interpretability.ReportsimprovedAUCwhileenhancing
transparencyviaboundary-awarepre-processing.
Compares1D-CNNandtransfer-learningBERTmodelsusing
openbankingtransactionsforcreditscoring.UsesSHAPto
ExplainingDeepLearningModelsfor
HjelkremandLange interpretdeepmodelsandsupportjustificationunder
28 CreditScoringwithSHAP:ACase RQ1
(2023) regulatorymandates.Findsthat1D-CNNoutperformsBERT
StudyUsingOpenBankingData
inAUCandBrierscore,emphasizingexplainabledeep
learningforcompliantcreditassessment.
Addressesmulti-classcreditriskpredictionusinghybrid
ensembles(LR,RF,SVM,NB,MLP)withSMOTEand
AHybridApproachtoCreditRisk
ADASYN.UsesMutualInformationtocaptureproxy
BulutandArslan AssessmentUsingBillPayment
29 interactionsandappliesSHAP/LIMEforinterpretability. RQ1,RQ2
(2025) HabitsDataandExplainable
Reportsstrongperformancewithtree-basedmodelsand
ArtificialIntelligence
highlightsexplainable,balancedriskassessmentin
alternative-datasettings.
ProposesanANNintegratingADASYNresamplingandFocal
Losstomitigateimbalance.TestedontheGermandataset;
AnExplainableADASYN-Based
AliShaheeandPatel reportsimprovedaccuracyandAUCoverbaselines.Uses
30 FocalLossApproachforCredit RQ1,RQ2
(2025) SHAPandLIMEforfeatureattribution,aimingtocombine
Assessment
predictiveperformancewithinterpretabilityincredit
assessment.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 30of36
TableA8.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part6:IDs31–36).
ID Author(s) Title Summary RelatedRQs
IntroducesaGA-basedcounterfactualexplanation
frameworkforblack-boxcreditmodels.Searches
neighbouringinstancesthatflippredictionswithminimal
Model-AgnosticCounterfactual
31 Dastileetal.(2022) featurechanges,exposingdecisionboundariesandpotential RQ1
ExplanationsinCreditScoring
biassources.ValidatedonGermanandHMEQdatasets,
supportingmodel-agnosticinterpretabilityfortransparency
andauditing.
ProposesVAE-INN,avariationalautoencoderguidedby
VAE-INN:VariationalAutoencoder weightedlosstocounterclassimbalanceinlatentspace.
withIntegratedNeuralNetwork AssignshigherweightstominorityclassestoreduceTypeII
32 Atif(2025) RQ1,RQ2
ClassifierforImbalancedCredit errors.TestedontheTaiwanesecreditdatasetandreports
Scoring improvedbalancedaccuracyandreliabilityover
SMOTE/ADASYN-basedbaselines.
CombinesTabTransformerwithweightedlosstoaddress
ANovelWeightedLoss classimbalancewhilepreservinginterpretability.Applies
TabTransformerIntegrating SHAPforglobalfeatureattribution.EvaluatedonGerman
33 Hartomoetal.(2025) RQ1,RQ2
ExplainableAIforImbalanced andBISAIDdatasets,reportingaccuracy/AUC
CreditRiskDatasets improvementsanddemonstratingexplainable,balanced
performancefortabularcreditscoring.
IntroducesMLMVS,astackingensemble(LR,MLP,RF,
KNN)withmulti-viewpartitioning(personal,behavioral,
AMulti-layerMulti-viewStacking historyfeatures).UsesLIMEforinstance-level
34 W.Hanetal.(2023) RQ1
ModelforCreditRiskAssessment interpretability.Reportsgainsinaccuracy,precision,and
specificityoverbaselines,supportinginterpretableensemble
learningfordefaultprediction.
DiscussesAIgovernanceinfinance,emphasizingregulation,
ethicalresponsibility,andhumanoversight.Identifieskey
AIintheFinancialSector:TheLine
challenges(privacy,fairness,accountability)andpositions
35 Ridzuanetal.(2024) BetweenInnovation,Regulationand RQ3
explainabilityascentralforhumandecision-making.
EthicalResponsibility
Advocatesgovernanceapproachesalignedwithsocietal
valuestofostertrustinregulatedfinancialAI.
ExamineswhetherAIcanexpandmortgageaccesswhile
managingbiasandequityconcerns.Warnshistoricaldata
AlgorithmsforAll:CanAIinthe
mayperpetuatediscrimination.RecommendsaligningAI
36 Perryetal.(2023) MortgageMarketExpandAccessto RQ2,RQ3
outcomeswithlegalandethicalframeworks,ensuring
Homeownership?
demographicfairness,transparency,andhumanoversightto
preventdisparateimpact.
TableA9.Summaryofincludedstudiesandtheirmappingtoresearchquestions(Part7:IDs37–43).
ID Author(s) Title Summary RelatedRQs
Proposesadeeplearningframeworkthatinjects
interpretabilityconstraintsintotrainingviamulti-objective
optimization.Usessoftconstraintsandweighted-sum
MulticriteriaInterpretabilityDriven
37 Repetto(2025) scalarizationtobalancecriteria.DemonstratesonthePolish RQ1
DeepLearning
bankruptcydatasetandvisualizeseffectsusingALEplots,
indicatinginterpretability-awaretrainingcansupport
generalizationinhigh-stakestasks.
Proposesfeature-weightadjustment,penalty-based
modeling,andahybridmethodtoenhanceinclusionin
SensitivityAnalysis:Improving
creditscoring.Evaluatesinclusivityandperformance
InclusiveCreditScoringAlgorithm
38 Sulastrietal.(2025) acrossextensivehyperparametercombinationsusing RQ1,RQ2
ThroughFeatureWeightand
XGBoost,CatBoost,RF,andDT.Improvesinclusionby
Penalty-BasedApproach
reweightingsensitivefeaturesbutnotesrisksof
dataset-specificoverfittingandlimitedgeneralizability.
ImplementsLightGBMwithLIMEandSHAPfor
global/localinterpretabilityincreditscoring.Uses
ExplainableAI-basedLightGBM
samplingandRFEtoaddressimbalanceand
PredictionModeltoPredictDefault
39 L.H.Lietal.(2025) dimensionalityontheLendingClubdataset.Reportsstrong RQ1
BorrowerinSocialLending
predictiveperformanceandprovidesareferencepipeline
Platform
forintegratingexplainabilitywithensemblemodelsin
sociallending.
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
31of36
TableA9.Cont.
| ID Author(s) |     | Title | Summary |     | RelatedRQs |
| ------------ | --- | ----- | ------- | --- | ---------- |
Proposesacounterfactualexplanationmethodoptimizing
validityandsparsitytoimproveinterpretability.UsesGA
CounterfactualExplanationswith andPSOtofindminimalfeaturechangesthatalter
40 DastileandCelik(2024) MultiplePropertiesinCredit predictions.Highlightschallengessuchasdriftsensitivity RQ1,RQ3
Scoring andmissingdata,andpositionscounterfactualsasa
transparentalternativetofeature-importanceexplanations
forauditing.
Presentsanensembleframework(RF,AdaBoost,XGBoost,
LightGBM)withSMOTE-ENNforimbalancecorrection
EffectiveCreditRiskPrediction
andSHAPforinterpretation.EvaluatedonGermanand
| 41 ArulebaandSun(2024) |     | UsingEnsembleClassifiersWith |     |     | RQ1,RQ2 |
| ---------------------- | --- | ---------------------------- | --- | --- | ------- |
Australiandatasets;reportsimprovedrecall/specificityand
ModelExplanation
arguesbalanced,explainableensemblelearningimproves
generalizationandauditability.
ProposesanAutoMLframeworkintegratingLIMEforlocal
AnInterpretableAutomated interpretabilityofcomplexmodels.Reportsnear–deep
42 Patronetal.(2020) MachineLearningCreditRisk learningperformancewhilemaintainingtransparency RQ1
Model throughlocalperturbation-basedexplanations,supporting
expertvalidationandcontestabilityincreditriskdecisions.
AnalyzesAI’simpactonfinancialinclusionusingdatafrom
TheEffectofAI-enabledCredit overonemillionunderservedborrowers.Introducesweak
ScoringonFinancialInclusion: signals(featuresweaklytiedtofinancialstatus)tostudy
43 C.Lietal.(2024) RQ2,RQ3
EvidencefromanUnderserved inclusionandbiastrade-offs.Warnsprotectedattributes
PopulationofOverOneMillion mayamplifydiscriminationandarguesforbalanced
adoptiontoimproveaccesswhilemanagingequityrisks.
AppendixC
TableA10.Summaryoffairnessmitigationstrategiesincreditscoring(Part1:Rows1–6).
| Author | Category | Method | Mechanism | Strengths | Limitations |
| ------ | -------- | ------ | --------- | --------- | ----------- |
Smallerfairnessgainsthan
Model-agnostic;simple
|     |     |     | Adjuststrainingsampleweights |     | thestrongestpost- |
| --- | --- | --- | ---------------------------- | --- | ----------------- |
toapplybeforetraining;
Kozodoietal. sodisadvantagedgroupsreceive processingoptionintheir
|        | Pre-processing | Reweighing |                                | canreduce |                       |
| ------ | -------------- | ---------- | ------------------------------ | --------- | --------------------- |
| (2022) |                |            | higherinfluenceduringtraining, |           | comparison;mayrequire |
discriminationatlow
|     |     |     | targetingindependence(parity). |     | repeateddata-pipeline |
| --- | --- | --- | ------------------------------ | --- | --------------------- |
implementationcost.
adjustments.
Transformsfeaturevaluesto
|     |     |     |     | Improvesfairness | Worseprofit–fairness |
| --- | --- | --- | --- | ---------------- | -------------------- |
reducedistributiondifferences
Kozodoietal. DisparateImpact withoutchangingmodel trade-offthanthebest
|     | Pre-processing |     | acrossprotectedgroups,reducing |     |     |
| --- | -------------- | --- | ------------------------------ | --- | --- |
(2022) Remover(DIR) dependenceonprotected architecture; in-processingoption(PRR)
|     |     |     |     | model-agnostic. | intheirreportedresults. |
| --- | --- | --- | --- | --------------- | ----------------------- |
attributes.
|     |     |     | Addsaregularizationtermtothe | Tunabletrade-off; | Invasive;modifiesthe |
| --- | --- | --- | ---------------------------- | ----------------- | -------------------- |
Kozodoietal. PrejudiceRemover trainingobjectivethatpenalizes achievesbetterprofit– trainingobjective/
In-processing
(2022) Regularizer(PRR) unfairnessusingaprejudiceindex, fairnesstrade-offthan scorecardsandincreases
|     |     |     | withatunablepenaltyweight.       | DIRintheirevaluation. | implementationburden. |
| --- | --- | --- | -------------------------------- | --------------------- | --------------------- |
|     |     |     | Trainsapredictorwhileanauxiliary |                       | Requiresretrainingand |
Tunablefairness–profit
Kozodoietal. Adversarial adversarytriestoinfertheprotected pipelinechanges;more
|     | In-processing |     |     | balancevia |     |
| --- | ------------- | --- | --- | ---------- | --- |
(2022) Debiasing attribute;penalizesthepredictor invasivethan
|     |     |     | whentheadversarysucceeds. | meta-parameters. | post-processing. |
| --- | --- | --- | ------------------------- | ---------------- | ---------------- |
Optimizesaclassifierunder
|              |     |           | fairnessconstraints(e.g., | Explicitcontrolover | Model/trainingspecific; |
| ------------ | --- | --------- | ------------------------- | ------------------- | ----------------------- |
| Kozodoietal. |     | Meta-fair |                           |                     |                         |
In-processing independence/separation)with fairness–accuracy requiresretrainingand
| (2022) |     | Classification |                          |             |                    |
| ------ | --- | -------------- | ------------------------ | ----------- | ------------------ |
|        |     |                | trade-offmeta-parameters | trade-offs. | integrationeffort. |
controllingaccuracyvs.fairness.
|     |     |     | Relabelsdecisionsinan | Strongfairnessgains; | Canreduceprofitability |
| --- | --- | --- | --------------------- | -------------------- | ---------------------- |
Kozodoietal. RejectOption uncertaintyregioninfavorofthe largelypreservesthe comparedtoin-processing
Post-processing
(2022) Classification(ROC) disadvantagedgrouptoimprove existingscoring approaches;actsonlyon
|     |     |     | groupparity. | pipeline. | thedecisionboundary. |
| --- | --- | --- | ------------ | --------- | -------------------- |
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
32of36
TableA11.Summaryoffairnessmitigationstrategiesincreditscoring(Part2:Rows7–12).
| Author | Category | Method | Mechanism | Strengths                | Limitations       |
| ------ | -------- | ------ | --------- | ------------------------ | ----------------- |
|        |          |        |           | Post-hoc;model-agnostic; | Strictfairnessmay |
Usesgroup-specificthresholdsto
Kozodoietal. EqualizedOdds canreducediscrimination requirelarge
|     | Post-processing |     | equalizeerrorratesacrossgroups |     |     |
| --- | --------------- | --- | ------------------------------ | --- | --- |
(2022) Post-processing atlowcostuptoapoint profit/utilitysacrifices
(separation/equalizedodds).
|     |     |     |     | ontheParetofrontier. | acrossdatasets. |
| --- | --- | --- | --- | -------------------- | --------------- |
Inheritspost-processing
Post-hoc;preserves
|              |     |                 | Calibratespredictedprobabilities |                   | trade-offs;doesnot |
| ------------ | --- | --------------- | -------------------------------- | ----------------- | ------------------ |
| Kozodoietal. |     | Group-wisePlatt |                                  | pipeline;supports |                    |
Post-processing pergrouptosatisfysufficiency(risk addressupstreambias;
| (2022) |     | Scaling |                                 | calibrationforsufficiency- |                          |
| ------ | --- | ------- | ------------------------------- | -------------------------- | ------------------------ |
|        |     |         | meaningconsistentacrossgroups). |                            | cannotsatisfyallcriteria |
|        |     |         |                                 | orientedcompliance.        | simultaneously.          |
|        |     |         | Learner–auditoradversarial      | Explicitlytargets          |                          |
Moldovan approachminimizingunfairness individual-level Hardtotune;mayoverfit
|     | In-processing | GerryFair |     |     |     |
| --- | ------------- | --------- | --- | --- | --- |
(2023) viaiterativeconstraintenforcement unfairness,notonly onsmallcreditdatasets.
|     |     |     | (targetsindividualfairness). | groupparity. |     |
| --- | --- | --- | ---------------------------- | ------------ | --- |
Reformulateslearningasa
|          |               |            |                             | Allowsexplicit          | Accuracymaydegrade |
| -------- | ------------- | ---------- | --------------------------- | ----------------------- | ------------------ |
| Moldovan |               | GridSearch | cost-sensitivereductionand  |                         |                    |
|          | In-processing |            |                             | explorationandselection | sharplyunderstrict |
| (2023)   |               | Reduction  | searchesconstraintweightsto |                         |                    |
|          |               |            |                             | oftrade-offpoints.      | constraints.       |
obtainfairness–accuracytrade-offs.
|              |     |     | Optimal-transportinterpolation | Providesatunable    | Weightselectionembeds |
| ------------ | --- | --- | ------------------------------ | ------------------- | --------------------- |
|              |     |     | betweenincompatiblefairness    |                     | normative/legal       |
| Zehlikeetal. |     |     |                                | mechanismtonavigate |                       |
Post-processing FAIM criteria(calibration,balancefor judgment;maynot
| (2025) |     |     |                                | incompatibilitybetween |                        |
| ------ | --- | --- | ------------------------------ | ---------------------- | ---------------------- |
|        |     |     | positives,balancefornegatives) |                        | matchasingleregulatory |
fairnesscriteria.
|     |     |             | usingweightedconstraints.    |     | interpretation.   |
| --- | --- | ----------- | ---------------------------- | --- | ----------------- |
|     |     | Demographic | ModifiesLRtrainingtominimize |     | Requiressensitive |
Valdrighietal. Parity/Equal losssubjecttoacorrelationconstraint Simpleandinterpretable; attributesduringtraining;
In-processing
(2025) Opportunity betweenpredictionsandsensitive tunabletrade-off. remainsatrade-offrather
|     |     | Classifier | attributes(tunableconstant). |     | thanaguarantee. |
| --- | --- | ---------- | ---------------------------- | --- | --------------- |
TableA12.Summaryoffairnessmitigationstrategiesincreditscoring(Part3:Rows13–18).
| Author | Category | Method | Mechanism | Strengths     | Limitations          |
| ------ | -------- | ------ | --------- | ------------- | -------------------- |
|        |          |        |           | Strongtabular | Model-classspecific; |
Altersboostingtojointlyminimize
|                |               | FairGBM      |                                  | performancewith  | dependsonproxy |
| -------------- | ------------- | ------------ | -------------------------------- | ---------------- | -------------- |
| Valdrighietal. |               |              | predictionlossandadifferentiable |                  |                |
|                | In-processing | (constrained |                                  | embeddedfairness | designand      |
(2025) gradientboosting) proxyofafairnessmetric(e.g., controlusingconstrained differentiabilityof
DP/EO)duringtraining.
|     |     |     |                            | learning. | fairnessobjectives. |
| --- | --- | --- | -------------------------- | --------- | ------------------- |
|     |     |     | BuildsseparateROCcurvesper |           | Requiressensitive   |
Consistentlyreaches
|                |     |           | groupandselectsthresholdsthat |                     | attributesatprediction |
| -------------- | --- | --------- | ----------------------------- | ------------------- | ---------------------- |
| Valdrighietal. |     | Threshold |                               | fairnesstargetswith |                        |
Post-processing minimizelosswithinthefeasiblefair time,whichmaybe
| (2025) |     | Optimizer |                               | minimumaccuracyloss |                     |
| ------ | --- | --------- | ----------------------------- | ------------------- | ------------------- |
|        |     |           | region,yieldinggroup-specific |                     | legally/practically |
intheircomparisons.
|     |     |     | thresholds. |     | constrained. |
| --- | --- | --- | ----------- | --- | ------------ |
Lesstunablethan
Altersoutputsofblack-boxmodels
|                |                 | Positionon |                                    | Versatileandsuitablefor | in-processing;may |
| -------------- | --------------- | ---------- | ---------------------------------- | ----------------------- | ----------------- |
| Valdrighietal. | Post-processing |            | tosatisfyfairnessconstraints(e.g., |                         |                   |
(2025) (general) post-processing groupthresholds)withoutchanging black-boxesandfixed yieldweaker
|     |     | (general) |     | scorecards. | improvementsrelative |
| --- | --- | --------- | --- | ----------- | -------------------- |
modeltraining.
topre-/in-processing.
|          |     |                | Framesfairnessasstochastic     |                      | Notreported(explicit |
| -------- | --- | -------------- | ------------------------------ | -------------------- | -------------------- |
|          |     | Stochastic     |                                | ProducessmoothPareto |                      |
|          |     |                | multi-objectiveoptimizationand |                      | method-level         |
| S.Liuand |     | Multi-Gradient |                                | frontiersandstable   |                      |
In-processing aggregatesgradientsofpredictionloss limitationsnotstated
| Vicente(2022) |     | (SMG)bi-objective |                                  | convergenceacross    |               |
| ------------- | --- | ----------------- | -------------------------------- | -------------------- | ------------- |
|               |     |                   | andfairnesspenaltyalongthePareto |                      | beyondgeneral |
|               |     | optimization      |                                  | fairnessconstraints. |               |
|               |     |                   | frontier(e.g.,DI/EOconstraints). |                      | trade-offs).  |
Stream-learningMixedNaïveBayes
Lowdiscrimination(SP
|          |        |           | withmulti-objectiveoptimization; | near0)whileimproving | Doesnotguarantee     |
| -------- | ------ | --------- | -------------------------------- | -------------------- | -------------------- |
| Badarand |        |           | dynamicinstanceweightingfor      |                      | globalfairnessacross |
|          | Hybrid | Fair-CMNB |                                  | accuracyrelativeto   |                      |
Fisichella(2024) imbalanceanddiscrimination settings;gainsare
baselines;supports
|     |     |     | control(targetsStatisticalParity; |     | dataset-dependent. |
| --- | --- | --- | --------------------------------- | --- | ------------------ |
streamingsettings.
usescausalfairnessviaATE/FACE).
Non-parametricstacked
Strongerperformance
autoencoderstolearnlatent
thanclassic
| S.Hanetal. | Pre-processing |      | structure,thenconditional     |                    |              |
| ---------- | -------------- | ---- | ----------------------------- | ------------------ | ------------ |
|            |                | NOTE |                               | oversampling(e.g., | Notreported. |
| (2024)     | (oversampling) |      | WassersteinGANoversamplingfor |                    |              |
SMOTE)intheir
mixedcategorical/
|     |     |     | numericalfeatures. | comparisons. |     |
| --- | --- | --- | ------------------ | ------------ | --- |
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104
33of36
TableA13.Summaryoffairnessmitigationstrategiesincreditscoring(Part4:Rows19–21).
| Author | Category | Method | Mechanism | Strengths | Limitations |
| ------ | -------- | ------ | --------- | --------- | ----------- |
Outperformsparceling,
|     |     |     | Semi-supervisedapproachthat | reweighting,and |     |
| --- | --- | --- | --------------------------- | --------------- | --- |
Pre-processing
|              |             |                 | iterativelyinferslabelsfor    | Heckman-stylecorrection; |              |
| ------------ | ----------- | --------------- | ----------------------------- | ------------------------ | ------------ |
| Kozodoietal. | (bias-aware | BASL:Bias-Aware |                               |                          |              |
|              |             |                 | rejected/unlabeledinstancesto | recoversasubstantial     | Notreported. |
| (2025)       | rejection   | Self-Learning   |                               |                          |              |
|              |             |                 | reducesamplingbiasandimprove  | shareofpredictiveloss    |              |
inference)
|     |     |     | trainingrepresentativeness. | attributedtosamplingbias |     |
| --- | --- | --- | --------------------------- | ------------------------ | --- |
intheircasestudy.
CombinesADASYNoversampling
|     |     |     | withaLocalCascadingEnsemble | Improvesgeneralization | Maystruggletoaddress |
| --- | --- | --- | --------------------------- | ---------------------- | -------------------- |
biasandvariance
| Chaietal. |                |            | (bagging/boosting/local       | underimbalance;LCE    |                     |
| --------- | -------------- | ---------- | ----------------------------- | --------------------- | ------------------- |
|           | Pre-processing | ADASYN-LCE |                               |                       | simultaneouslyunder |
| (2025)    |                |            | cascading)toimproverobustness | balancesbias–variance |                     |
someconditions(as
|     |     |     | forunderservedpopulationsunder | acrosssubsetsofthedata. |     |
| --- | --- | --- | ------------------------------ | ----------------------- | --- |
notedbytheauthors).
imbalance.
Supportsjoint
|     |     |     | Integratesaweighted | improvementsin |     |
| --- | --- | --- | ------------------- | -------------- | --- |
Pronetooverfittingif
| Hartomo |               | Weighted | cross-entropyobjectiveinto | performanceunder |             |
| ------- | ------------- | -------- | -------------------------- | ---------------- | ----------- |
|         | In-processing |          |                            |                  | weightingis |
etal.(2025) TabTransformer TabTransformertogivelarger imbalanceand
mis-specified.
|     |     |     | gradientstominorityclasses. | fairness-relatedobjectives |     |
| --- | --- | --- | --------------------------- | -------------------------- | --- |
intheirframing.
References
Adegoke,T.,Ofodile,O.,Ochuba,N.,&Akinrinol,O.(2024).Evaluatingthefairnessofcreditscoringmodels:Aliteraturereviewon
mortgageaccessibilityforunder-reservedpopulations.GSCAdvancedResearchandReviews,18(3),189–199.[CrossRef]
AliShahee,S.,&Patel,R.(2025).AnexplainableADASYN-basedfocallossapproachforcreditassessment.JournalofForecasting,44,
1513–1530.[CrossRef]
Alufaisan,Y.,Marusich,L.R.,Bakdash,J.Z.,Zhou,Y.,&Kantarcioglu,M.(2021). Doesexplainableartificialintelligenceimprove
humandecision-making? InProceedingsoftheAAAIconferenceonartificialintelligence(Vol.35, pp.6618–6626). AAAIPress.
[CrossRef]
Alves,G.,Bernier,F.,Couceiro,M.,Makhlouf,K.,Palamidessi,C.,&Zhioua,S.(2023).Surveyonfairnessnotionsandrelatedtensions.
EUROJournalonDecisionProcesses,11,100033.[CrossRef]
Amekoe,K.M.,Azzag,H.,Dagdia,Z.C.,Lebbah,M.,&Jaffre,G.(2024).Exploringaccuracyandinterpretabilitytrade-offintabular
learningwithnovelattention-basedmodels.NeuralComputingandApplications,36(30),18583–18611.[CrossRef]
Aruleba, I., &Sun, Y.(2024). Effectivecreditriskpredictionusingensembleclassifierswithmodelexplanation. IEEEAccess, 12,
115015–115025.[CrossRef]
Atif,D.(2025).VAE-INN:Variationalautoencoderwithintegratedneuralnetworkclassifierforimbalancedcreditscoring,utilizing
weightedlossforimprovedaccuracy.ComputationalEconomics.[CrossRef]
Badar, M., &Fisichella, M.(2024). Fair-CMNB:Advancingfairness-awarestreamlearningwithnaïvebayesandmulti-objective
optimization.BigDataandCognitiveComputing,8(2),16.[CrossRef]
Balashankar,A.,&Lees,A.(2022).Theneedfortransparentdemographicgrouptrade-offsincreditriskandincomeclassification.In
Proceedingsoftheinternationalconferenceoninformation(pp.344–354).SpringerInternationalPublishing.
Bartlett,R.,Morse,A.,Stanton,R.,&Wallace,N.(2022). Consumer-lendingdiscriminationintheFinTechera. JournalofFinancial
Economics,143(1),30–56.[CrossRef]
BaselCommitteeonBankingSupervision.(2013).Principlesforeffectiveriskdataaggregationandriskreporting(Technicalreportno.8,Basel
committeepublicationno.239).BankforInternationalSettlements.Availableonline:https://www.bis.org/publ/bcbs239.htm
(accessedon30September2025).
Berg,T.,Burg,V.,Gombovic´,A.,&Puri,M.(2020). OntheriseofFintechs: Creditscoringusingdigitalfootprints. TheReviewof
FinancialStudies,33(7),2845–2897.[CrossRef]
Brzezinski,D.,Stachowiak,J.,Stefanowski,J.,Szczech,I.,Susmaga,R.,Aksenyuk,S.,&Yasinskyi,O.(2024). Propertiesoffairness
measuresinthecontextofvaryingclassimbalanceandprotectedgroupratios.ACMTransactionsonKnowledgeDiscoveryfrom
Data,18(7),1–18.[CrossRef]
Bueff,A.C.,Cytryn´ski,M.,Calabrese,R.,Jones,M.,Roberts,J.,Moore,J.,&Brown,I.(2022).Machinelearninginterpretabilityfora
stressscenariogenerationincreditscoringbasedoncounterfactuals.ExpertSystemswithApplications,202,117271.[CrossRef]
Bulut,C.,&Arslan,E.(2025).Ahybridapproachtocreditriskassessmentusingbillpaymenthabitsdataandexplainableartificial
intelligence.AppliedSciences,15(10),5723.[CrossRef]
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 34of36
Bücker,M.,Szepannek,G.,Gosiewska,A.,&Biecek,P.(2022). Transparency,auditability,andexplainabilityofmachinelearning
modelsincreditscoring.JournaloftheOperationalResearchSociety,73(1),70–90.[CrossRef]
Cao,W.,He,Y.,Wang,W.,Zhu,W.,&Demazeau,Y.(2021).Ensemblemethodsforcreditscoringofchinesepeer-to-peerloans.Journal
ofCreditRisk,17,79–115.[CrossRef]
Caton,S.,&Haas,C.(2024).Fairnessinmachinelearning:Asurvey.ACMComputingSurveys,56(7),1–38.[CrossRef]
Chacko, A., &Aravindhar, D.J.(2025, February21–22). Enhancingfairnessandaccuracyincreditscoreanalysis: Anovelframework
utilizingkernelPCA.2025InternationalConferenceonInformationTechnology,InnovationandIntelligentSystems(ICITIIT),
Kottayam,India.[CrossRef]
Chai,N.,Abedin,M.Z.,Yang,L.,&Shi,B.(2025).Farmers’creditriskevaluationwithanexplainablehybridensembleapproach:A
closerlookinmicrofinance.Pacific-BasinFinanceJournal,89,102612.[CrossRef]
Chen,Y.,Calabrese,R.,&Martin-Barragán,B.(2024).Interpretablemachinelearningforimbalancedcreditscoringdatasets.European
JournalofOperationalResearch,312(1),357–372.[CrossRef]
Cornacchia,G.,Anelli,V.W.,Narducci,F.,Ragone,A.,&DiSciascio,E.(2023).Ageneralarchitectureforatrustworthycreditworthiness-
assessmentplatforminthefinancialdomain.AETiC,7,56–64.[CrossRef]
Corrales-Barquero,R.,Marín-Raventós,G.,&Barrantes,E.G.(2021,October27–28).Areviewofgenderbiasmitigationincreditscoring
models.2021InternationalConferenceonElectrical,ElectronicsandRelatedDataScience(EE-RDS),Johannesburg,SouthAfrica.
[CrossRef]
C-Rella,J.,Martínez-Rego,D.,&VilarFernández,J.M.(2025).Cost-sensitivereinforcementlearningforcreditrisk.ExpertSystemswith
Applications,272,126708.[CrossRef]
Das,S.,Stanton,R.,&Wallace,N.(2023).Algorithmicfairness.AnnualReviewofFinancialEconomics,15(1),565–593.[CrossRef]
Dastile,X.,&Celik,T.(2024).Counterfactualexplanationswithmultiplepropertiesincreditscoring.IEEEAccess,12,110713–110728.
[CrossRef]
Dastile,X.,Celik,T.,&Vandierendonck,H.(2022). Model-agnosticcounterfactualexplanationsincreditscoring. IEEEAccess,10,
69543–69554.[CrossRef]
deCastroVieira,J.R.,Barboza,F.L.D.M.,Cajueiro,D.O.,&Kimura,H.(2025).TowardsfairAI:Mitigatingbiasincreditdecisions—A
systematicliteraturereview.JournalofRiskandFinancialManagement,18,228.[CrossRef]
Dessain,J.,Bentaleb,N.,&Viñas,F.(2023).CostofexplainabilityinAI:Anexamplewithcreditscoringmodels.InProceedingsofthe
worldconferenceonexplainableartificialintelligence(pp.498–516).SpringerNature.[CrossRef]
European Central Bank. (2024). Supervisory guide on risk data aggregation and risk reporting (Technical report, supervisory guide).
EuropeanCentralBank,BankingSupervision.Availableonline:https://www.bankingsupervision.europa.eu/ecb/pub/pdf/
ssm.supervisory_guides240503_riskreporting.en.pdf(accessedon30September2025).
Goethals,S.,Martens,D.,&Calders,T.(2024).Precof:Counterfactualexplanationsforfairness.MachineLearning,113(5),3111–3142.
[CrossRef]
Griffith,M.A.(2023). AIlendingandtheECOA:Avoidingaccidentaldiscrimination. NorthCarolinaBankingInstitute,27,349–381.
Availableonline:https://scholarship.law.unc.edu/ncbi/vol27/iss1/16(accessedon30September2025).
Han,S.,Jung,H.,Yoo,P.D.,Provetti,A.,&Calì,A.(2024). NOTE:Non-parametricoversamplingtechniqueforexplainablecredit
scoring.ScientificReports,14(1),26070.[CrossRef]
Han,W.,Gu,X.,&Jian,L.(2023).Amulti-layermulti-viewstackingmodelforcreditriskassessment.IntelligentDataAnalysis,27(5),
1457–1475.[CrossRef]
Hartomo,K.D.,Arthur,C.,&Nataliani,Y.(2025).AnovelweightedlosstabtransformerintegratingexplainableAIforimbalanced
creditriskdatasets.IEEEAccess,13,31045–31056.[CrossRef]
Hickey,J.M.,DiStefano,P.G.,&Vasileiou,V.(2020). FairnessbyexplicabilityandadversarialSHAPlearning. InJointEuropean
conferenceonmachinelearningandknowledgediscoveryindatabases(ECMLPKDD)(pp.174–190).SpringerInternationalPublishing.
Hjelkrem,L.O.,&Lange,P.E.D.(2023).Explainingdeeplearningmodelsforcreditscoringwithtextualtransactiondata.Journalof
RiskandFinancialManagement,16(4),221.[CrossRef]
Hlongwane,R.,Ramabao,K.,&Mongwe,W.(2024).Anovelframeworkforenhancingtransparencyincreditscoring:Leveraging
Shapleyvaluesforinterpretablecreditscorecards.PLoSONE,19(8),e0308718.[CrossRef][PubMed]
Hurlin,C.,Pérignon,C.,&Saurin,S.(2024).Thefairnessofcreditscoringmodels.ManagementScience,70(11),1234–1256.[CrossRef]
Jiang,Y.,Fang,X.,&Wang,Z.(2024).Disparityanddiscriminationinconsumercreditmarkets:Evidencefromonlinepeer-to-peer
lending.Pacific-BasinFinanceJournal,83,102237.[CrossRef]
Kanaparthi,V.(2023,April26–28).Creditriskpredictionusingensemblemachinelearningalgorithms.2023InternationalConferenceon
InventiveComputationTechnologies(ICICT)(pp.41–47),Lalitpur,Nepal.[CrossRef]
Keele,S.(2007).Guidelinesforperformingsystematicliteraturereviewsinsoftwareengineering(EBSEtechnicalreport,version2.3).Available
online:https://www.elsevier.com/__data/promis_misc/525444systematicreviewsguide.pdf(accessedon17October2025).
Koulu,R.(2020).Humancontroloverautomation:EUpolicyandAIethics.EuropeanJournalofLegalStudies,12,9–46.[CrossRef]
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 35of36
Kozodoi,N.,Jacob,J.,&Lessmann,S.(2022).Fairnessincreditscoring:Assessment,implementationandprofitimplications.European
JournalofOperationalResearch,297(3),1083–1094.[CrossRef]
Kozodoi,N.,Lessmann,S.,Alamgir,M.,Moreira-Matias,L.,&Papakonstantinou,K.(2025).Fightingsamplingbias:Aframeworkfor
trainingandevaluatingcreditscoringmodels.EuropeanJournalofOperationalResearch,324(2),616–628.[CrossRef]
Kuiper,O.,vandenBerg,M.,vanderBurgt,J.,&Leijnen,S.(2021). ExploringexplainableAIinthefinancialsector: Perspectives
of banks and supervisory authorities. In Proceedings of the benelux conference on artificial intelligence (pp. 105–119). Springer
InternationalPublishing.
Kumar,I.E.,Hines,K.E.,&Dickerson,J.P.(2022).Equalizingcreditopportunityinalgorithms:Aligningalgorithmicfairnessresearch
withUSfairlendingregulation.InProceedingsofthe2022AAAI/ACMconferenceonAI,ethics,andsociety(pp.357–368).Association
forComputingMachinery.[CrossRef]
Lainez,N.,&Gardner,J.(2023).AlgorithmiccreditscoringinVietnam:Alegalproposalformaximizingbenefitsandminimizingrisks.
AsianJournalofLawandSociety,10(3),401–432.[CrossRef]
Langenbucher,K.(2020). ResponsibleAI-basedcreditscoring—Alegalframework. EuropeanBusinessLawReview,31(4),527–572.
[CrossRef]
Langenbucher,K.,&Corcoran,P.(2022).ResponsibleAIcreditscoring—Alessonfromupstart.com.InDigitalfinanceinEurope:Law,
regulation,andgovernance.DeGruyter.
Li,C.,Wang,H.,Jiang,S.,&Gu,B.(2024).TheeffectofAI-enabledcreditscoringonfinancialinclusion:Evidencefromanunderserved
populationofoveronemillion.MISQuarterly,48(4),1803–1834.[CrossRef]
Li,L.H.,Sharma,A.K.,&Cheng,S.T.(2025).ExplainableAIbasedLightGBMpredictionmodeltopredictdefaultborrowerinsocial
lendingplatform.IntelligentSystemswithApplications,26,200514.[CrossRef]
Li,W.,Paraschiv,F.,&Sermpinis,G.S.(2022).Adata-drivenexplainablecase-basedreasoningapproachforfinancialriskdetection.
QuantitativeFinance,22,2257–2274.[CrossRef]
Li,Y.,Wang,X.,Djehiche,B.,&Hu,X.(2020).Creditscoringbyincorporatingdynamicnetworkedinformation.EuropeanJournalof
OperationalResearch,286(3),1103–1112.[CrossRef]
Li,Z.,Hu,X.,Li,K.,Zhou,F.,&Shen,F.(2020).Inferringtheoutcomesofrejectedloans:Anapplicationofsemisupervisedclustering.
JournaloftheRoyalStatisticalSociety:SeriesA,183,631–654.[CrossRef]
Liao,J.,Wang,W.,Xue,J.,Lei,A.,Han,X.,&Lu,K.(2022).Combatingsamplingbias:Aself-trainingmethodincreditriskmodels.
ProceedingsoftheAAAIConferenceonArtificialIntelligence,36,12566–12572.[CrossRef]
Liu,J.,Zhang,X.,&Xiong,H.(2024).Creditriskpredictionbasedoncausalmachinelearning:Bayesiannetworklearning,default
inference,andinterpretation.JournalofForecasting,43(5),1625–1660.[CrossRef]
Liu, S., & Vicente, L. N. (2022). Accuracy and fairness trade-offs in machine learning: A stochastic multi-objective approach.
ComputationalManagementScience,19(3),513–537.[CrossRef]
Martinez,N.,Bertran,M.,&Sapiro,G.(2020,July13–18).Minimaxparetofairness:Amulti-objectiveperspective.InternationalConference
onMachineLearning(ICML)(pp.6755–6764),Virtual.
Mestiri,S.,&Hiboun,S.M.(2024).Creditscoringusingmachinelearninganddeeplearning-basedmodels.DataScienceinFinanceand
Economics,4(2),236–248.[CrossRef]
Moher,D.,Liberati,A.,Tetzlaff,J.,Altman,D.G.,&Group,P.(2010).Preferredreportingitemsforsystematicreviewsandmeta-analyses:
ThePRISMAstatement.InternationalJournalofSurgery,8(5),336–341.[CrossRef]
Moldovan,D.(2023).Algorithmicdecisionmakingmethodsforfaircreditscoring.IEEEAccess,11,59729–59743.[CrossRef]
Mou,Y.,Pu,Z.,Feng,D.,Luo,Y.,Lai,Y.,Huang,J.,Tian,Y.,&Xiao,F.(2025).Cost-awarecredit-scoringframeworkbasedonresampling
andfeatureselection.ComputationalEconomics,66,3007–3032.[CrossRef]
Muñoz-Cancino,R.,Bravo,C.,Ríos,S.A.,&Graña,M.(2023).Onthedynamicsofcredithistoryandsocialinteractionfeatures,and
theirimpactoncreditworthinessassessmentperformance.ExpertSystemswithApplications,218,119599.[CrossRef]
Nwafor,C.N.,Nwafor,O.,&Brahma,S.(2024).Enhancingtransparencyandfairnessinautomatedcreditdecisions:Anexplainable
novelhybridmachinelearningapproach.ScientificReports,14(1),25174.[CrossRef]
Page,M.J.,McKenzie,J.E.,Bossuyt,P.M.,Boutron,I.,Hoffmann,T.C.,Mulrow,C.D.,Shamseer,L.,Tetzlaff,J.M.,Akl,E.A.,Brennan,
S.E.,Chou,R.,Glanville,J.,Grimshaw,J.M.,Hróbjartsson,A.,Lalu,M.M.,Li,T.,Loder,E.W.,Mayo-Wilson,E.,McDonald,S.,&
Moher,D.(2021).Updatingguidanceforreportingsystematicreviews:DevelopmentofthePRISMA2020statement.Journalof
ClinicalEpidemiology,134,103–112.[CrossRef]
Patron,G.,Leon,D.,Lopez,E.,&Hernandez,G.(2020).Aninterpretableautomatedmachinelearningcreditriskmodel.InWorkshop
onengineeringapplications(pp.16–23).SpringerInternationalPublishing.
Peng,Z.,Mo,W.,Duan,C.,Li,Q.,&Zhou,B.(2023).Learningfromactivehumaninvolvementthroughproxyvaluepropagation.In
Proceedingsofthe37thconferenceonneuralinformationprocessingsystems(NeurIPS2023).CurranAssociates,Inc.Availableonline:
https://metadriverse.github.io/pvp(accessedon17October2025).
https://doi.org/10.3390/jrfm19020104

J.RiskFinancialManag.2026,19,104 36of36
Perry,V.G.,Martin,K.,&Schnare,A.(2023).Algorithmsforall:CanAIinthemortgagemarketexpandaccesstohomeownership?AI,
4(4),888–903.[CrossRef]
Ratul,Q.E.A.,Serra,E.,&Cuzzocrea,A.(2021,December15–18).Evaluatingattributionmethodsinmachinelearninginterpretability.2021
IEEEInternationalConferenceonBigData(BigData)(pp.5239–5245),Orlando,FL,USA.
Repetto,M.(2025).Multicriteriainterpretabilitydrivendeeplearning.AnnalsofOperationsResearch,346(2),1621–1635.[CrossRef]
Ribeiro-Flucht,L.,Chen,X.,&Meurers,D.(2024).ExplainableAIinlanguagelearning:Linkingempiricalevidenceandtheoretical
conceptsinproficiencyandreadabilitymodelingofportuguese. InProceedingsofthe19thworkshoponinnovativeuseofNLP
for building educational applications (BEA 2024) (pp. 199–209). Association for Computational Linguistics. Available online:
https://aclanthology.org/2024.bea-1.17(accessedon4October2025).
Ridzuan,N.N.,Masri,M.,Anshari,M.,Fitriyani,N.L.,&Syafrudin,M.(2024).AIinthefinancialsector:Thelinebetweeninnovation,
regulationandethicalresponsibility.Information,15(8),432.[CrossRef]
Roa,L.,Correa-Bahnsen,A.,Suarez,G.,Cortés-Tejada,F.,Luque,M.A.,&Bravo,C.(2021).Super-appbehavioralpatternsincreditrisk
models:Financial,statisticalandregulatoryimplications.ExpertSystemswithApplications,169,114486.[CrossRef]
Shi, X., Tang, D., & Yu, Y. (2025). Credit scoring prediction using deep learning models in the financial sector. IEEE Access, 13,
130731–130746.[CrossRef]
Sulastri,R.,Ding,A.Y.,&Janssen,M.(2025,June18–20).Sensitivityanalysis:Improvinginclusivecreditscoringalgorithmthroughfeature
weightandpenalty-basedapproach.2025EleventhInternationalConferenceonEdemocracy&Egovernment(ICEDEG)(pp.54–61),
Bern,Switzerland.[CrossRef]
Talaat,F.M.,Aljadani,A.,Badawy,M.,&Elhosseini,M.(2024).Towardinterpretablecreditscoring:Integratingexplainableartificial
intelligencewithdeeplearningforcreditcarddefaultprediction.NeuralComputingandApplications,36(9),4847–4865.[CrossRef]
Tiukhova,E.,Salcuni,A.,Oguz,C.,Niglio,M.,Storti,G.,Forte,F.,Baesens,B.M.,&Snoeck,M.(2025).Boostingcreditriskdataquality
usingmachinelearningandeXplainableAItechniques. InMachinelearningandprinciplesandpracticeofknowledgediscoveryin
databases.Springer.[CrossRef]
Valdrighi,G.,Ribeiro,A.M.,Pereira,J.S.B.,Guardieiro,V.,Hendricks,A.,MirandaFilho,D.,&MedeirosRaimundo,M.(2025).Best
practicesforresponsiblemachinelearningincreditscoring.NeuralComputingandApplications,37,20781–20821.[CrossRef]
Vukovic´,D.B.,Dekpo-Adza,S.,&Matovic´,S.(2025).AIintegrationinfinancialservices:Asystematicreviewoftrendsandregulatory
challenges.HumanitiesandSocialSciencesCommunications,12,562.[CrossRef]
Wang,W.,Lesner,C.,Ran,A.,Rukonic,M.,Xue,J.,&Shiu,E.(2020).Usingsmallbusinessbankingdataforexplainablecreditrisk
scoring.InProceedingsoftheAAAIConferenceonArtificialIntelligence(Vol.34,pp.13396–13401).AAAIPress.[CrossRef]
Wu,Z.,Dong,Y.,Li,Y.,&Liu,Y.(2025).A‘DivideandConquer’rejectinferenceapproachleveraginggraph-basedsemi-supervised
learning.AnnalsofOperationsResearch.[CrossRef]
Xie,W.,He,J.,Huang,F.,&Ren,J.(2025).Operationalriskassessmentofcommercialbanks’supplychainfinance.Systems,13(2),76.
[CrossRef]
Zacharias,J.,vonZahn,M.,Chen,J.,&Hinz,O.(2022).Designingafeatureselectionmethodbasedonexplainableartificialintelligence.
ElectronicMarkets,32,2159–2184.[CrossRef]
Zehlike,M.,Loosley,A.,Jonsson,H.,Wiedemann,E.,&Hacker,P.(2025). Beyondincompatibility: Trade-offsbetweenmutually
exclusivefairnesscriteriainmachinelearningandlaw.ArtificialIntelligence,340,104280.[CrossRef]
Zhang,R.,Li,I.,&Ding,Z.(2025).AnInterpretablecreditriskassessmentmodelwithboundarysampleidentification.PeerJComputer
Science,11,e2988.[CrossRef][PubMed]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/jrfm19020104